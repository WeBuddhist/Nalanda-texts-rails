#!/usr/bin/env python3
"""The rest of the root-text workflow, on the Gemini API, for every text whose TOC
extraction is finished: segment (new rules) → TOC ingest from the stored tree → grouping
→ block IDs + strict text gate. Several texts in parallel; the report is updated after
each text. The two modes take different texts and may run at the same time.

    venv/Scripts/python.exe -X utf8 0-INBOX/temp/root-toc/run_workflow_batch.py --mode low
    venv/Scripts/python.exe -X utf8 0-INBOX/temp/root-toc/run_workflow_batch.py --mode medium
        [--procs 3] [--limit N] [--only ID ...] [--reset-running] [--retry-failed]
        [--redo ID ...]   run these again from the start, whatever their status

    --mode low     small + medium texts, grouping on gemini-3.8-flash thinking low
    --mode medium  large texts,          grouping on gemini-3.8-flash thinking medium
                   (--thinking overrides the level)

Per text <id>:
  1. root_text_build.py segment   0-INBOX/root/<id>.md → 0-INBOX/temp/root-final/<id>/
  2. root_text_build.py toc-ingest --tree 0-INBOX/temp/TOC-<id>/toc-tree-anchored-<id>.md
     (only when that anchored tree exists; a text with no parts keeps ## གཞུང་དངོས། ^1-0)
  3. grouping on Gemini (gemini-3.8-flash, thinking --thinking): the prompts of the skill
     root-text-group (stanza-grouping.md for verse, prose-grouping.md + stanza-grouping.md
     for prose), group-split for a long input; every answer is checked (every unit once, in
     order, no block across a heading, a printed paragraph break ¶ or a prose/verse
     change) and asked again once with the error if it fails; then group-join
  4. root_text_build.py finish     → final-<free|prose>.md with block IDs, strict gate
  5. copied to 0-INBOX/processed/root-gemini/<id>.md

Status: 0-INBOX/temp/root-toc/workflow-status.json → report 0-INBOX/ROOT-WORKFLOW-BATCH.md.
Logs: 0-INBOX/temp/root-toc/logs/workflow-<id>.log. Nothing in 0-INBOX/processed/root/ is
touched (it holds the reviewed files).
"""
import argparse, datetime, importlib.util, json, os, re, shutil, subprocess, sys, threading, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
PY = sys.executable
LIB = VAULT / "4-SYSTEM/Skills/seg-toc-lib/root_text_build.py"
PROMPTS = VAULT / "4-SYSTEM/Skills/root-text-group/prompts"
RUNNER = VAULT / "4-SYSTEM/scripts/seg-toc-benchmark/root_toc_gemini.py"
WORK = VAULT / "0-INBOX/temp/root-final"
OUTDIR = VAULT / "0-INBOX/processed/root-gemini"
WST = HERE / "workflow-status.json"
DOC = VAULT / "0-INBOX/ROOT-WORKFLOW-BATCH.md"
LOGS = HERE / "logs"
MODEL = "gemini-3.8-flash"
MODES = {"low": ({"small", "medium"}, "low"), "medium": ({"large"}, "medium")}
PRICE = (0.75, 3.75)                       # USD per million tokens in / out (thinking = out)

def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

toc = _load("status", HERE / "status.py")            # the TOC batch status (read only)
gem = _load("gemrun", RUNNER)                        # its Gemini client (key loader, logging)
batch = _load("batch", HERE / "run_gemini_batch.py") # its cross-process lock
anchors = _load("anchor_repair", HERE / "anchor_repair.py")
locked = batch.locked
local = batch.local


# ── status / report ──────────────────────────────────────────────────────────

def wload():
    return json.loads(WST.read_text(encoding="utf-8")) if WST.exists() else {}


def wsave(d):
    WST.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def render(d):
    t = toc.load()
    keys = ("todo", "running", "done", "failed")
    n = {k: sum(1 for r in d.values() if r["status"] == k) for k in keys}
    rows = []
    for k, (i, r) in enumerate(d.items(), 1):
        out = f"`processed/root-gemini/{i}.md`" if r["status"] == "done" else ""
        rows.append(f"| {k} | {i} | {t[i].get('size', '')} | {r['status']} | {r.get('toc', '')} | "
                    f"{r.get('headings', '')} | {r.get('blocks', '')} | {r.get('run', '')} | "
                    f"{r.get('note', '')} | {out} |")
    DOC.write_text(f"""# Root-text workflow batch — segmentation + TOC ingest + grouping + block IDs

Gemini ({MODEL}) runs the rest of the workflow for every root text whose TOC
extraction is finished (see `0-INBOX/ROOT-TOC-BATCH.md`). How to run: `0-INBOX/temp/root-toc/README.md`.

Updated {datetime.date.today().isoformat()} · {len(d)} texts · done {n['done']} · failed {n['failed']} ·
running {n['running']} · **to do {n['todo']}**

| Where | Path |
|---|---|
| Finished files (with block IDs) | `0-INBOX/processed/root-gemini/<id>.md` |
| Working folder per text | `0-INBOX/temp/root-final/<id>/` (prepared.md, group-in.md, groups-*.json, final-*.md) |
| Tree used for the headings | `0-INBOX/temp/TOC-<id>/toc-tree-anchored-<id>.md` |
| Log per text | `0-INBOX/temp/root-toc/logs/workflow-<id>.log` |

`toc` tree = the text's parts became headings · no parts = `## གཞུང་དངོས། ^1-0` only ·
`headings` = body headings placed / not placed (a not-placed heading must be put in by hand) ·
`blocks` = stanzas / paragraphs. Review the files before they replace anything in
`0-INBOX/processed/root/`.

| # | id | size | status | toc | headings | blocks | run (cost · time) | note | output |
|---|---|---|---|---|---|---|---|---|---|
""" + "\n".join(rows) + "\n", encoding="utf-8")


def has_nodes(tree):
    """A tree file with at least one numbered node (an empty tree = no parts announced)."""
    return tree.exists() and bool(re.search(r"^\s*\*\s+\d", tree.read_text(encoding="utf-8"), re.M))


def eligible(sizes):
    """Texts whose TOC stage is finished: a tree to ingest, or no parts announced."""
    out = {}
    for i, r in toc.load().items():
        if r.get("size") not in sizes:
            continue
        tree = VAULT / f"0-INBOX/temp/TOC-{i}/toc-tree-anchored-{i}.md"
        if r["status"] in ("done", "earlier-run") and tree.exists() and not has_nodes(tree):
            out[i] = "no parts"                       # the tree came out empty
        elif r["status"] == "done" or (r["status"] == "earlier-run" and tree.exists()):
            out[i] = "tree"
        elif r["status"] == "no-parts" or (r["status"] == "earlier-run" and not
                                            (VAULT / f"0-INBOX/temp/TOC-{i}/toc-tree-{i}.md").exists()):
            out[i] = "no parts"
    return out


def claim(retry_failed, only, sizes):
    with locked():
        d = wload()
        tsz = toc.load()
        for i, r in d.items():
            if tsz[i].get("size") not in sizes or (only and i not in only):
                continue
            if r["status"] == "todo" or (retry_failed and r["status"] == "failed"):
                r["status"], r["run"] = "running", f"started {time.strftime('%H:%M')}"
                wsave(d)
                render(d)
                return i, r["toc"]
    return None, None


def record(i, fields):
    with locked():
        d = wload()
        d[i].update(fields)
        wsave(d)
        render(d)


# ── grouping on Gemini ───────────────────────────────────────────────────────

UNIT = re.compile(r"^([PSV])(\d+)  ")


def group_input_info(path):
    """Unit numbers and types in a group-in file, and the unit numbers after which a block
    must end (a heading or a ¶ follows)."""
    units, types, stops, last = [], {}, set(), None
    for l in path.read_text(encoding="utf-8").split("\n"):
        m = UNIT.match(l)
        if m:
            last = int(m.group(2))
            units.append(last)
            types[last] = m.group(1)
        elif (l.startswith("#") or l.startswith("¶")) and last is not None:
            stops.add(last)
    return units, types, stops


def check_groups(js, units, types, stops):
    st = js.get("stanzas") if isinstance(js, dict) else None
    if not isinstance(st, list) or not st:
        return "no 'stanzas' list"
    errs = []
    for g in st:
        if not (isinstance(g, list) and len(g) == 2 and all(isinstance(x, int) for x in g) and g[0] <= g[1]):
            return f"bad block {g!r} — each block is [first, last] with first <= last"
    if st[0][0] != units[0]:
        errs.append(f"the first block must start at line {units[0]}, not {st[0][0]}")
    if st[-1][1] != units[-1]:
        errs.append(f"the last block must end at line {units[-1]}, not {st[-1][1]}")
    # each block must start right after the one before: name every overlap and gap — the
    # usual slip is a block started one line after the previous block's START, not its end
    for (a0, z0), (a, z) in zip(st, st[1:]):
        if a <= z0:
            errs.append(f"block [{a}, {z}] overlaps the block before it [{a0}, {z0}] (lines {a}–{min(z, z0)} are "
                        f"in both); the block after [{a0}, {z0}] must start at line {z0 + 1}")
        elif a > z0 + 1:
            errs.append(f"lines {z0 + 1}–{a - 1} are in no block (between [{a0}, {z0}] and [{a}, {z}])")
    for a, z in st:
        if len({types.get(u) for u in range(a, z + 1)}) > 1:
            errs.append(f"block [{a}, {z}] mixes prose sentences and verse lines")
        if any(a <= s < z for s in stops):
            errs.append(f"block [{a}, {z}] runs across a heading or a ¶ (a block must end at line "
                        f"{min(s for s in stops if a <= s < z)})")
    if not errs and [u for a, z in st for u in range(a, z + 1)] != units:
        errs.append(f"blocks must cover lines {units[0]}–{units[-1]} exactly once, in order")
    return "; ".join(errs[:6]) + (f" (and {len(errs) - 6} more)" if len(errs) > 6 else "") if errs else None


def group_one(g, prompt, inp, out, label, fallback=None, tries=3):
    """Group one input file; every answer is checked, a rejected one is saved to
    rejected/<label>-<level>-a<N>.txt and asked again with the exact errors. If the level's
    tries all fail and a fallback client is given (thinking medium for a low run), that
    part — only that part — is grouped again at the fallback level. Returns the level used."""
    units, types, stops = group_input_info(inp)
    if not units:                                   # nothing to group (frame only)
        out.write_text(json.dumps({"stanzas": [], "notes": {}}), encoding="utf-8")
        return g.thinking
    user = (f"The input (use the unit numbers as given; read all of it):\n\n{inp.read_text(encoding='utf-8')}\n\n"
            "Answer with ONLY the JSON object.")
    rej = out.parent / "rejected"
    err = None
    for client in [g] + ([fallback] if fallback and fallback.thinking != g.thinking else []):
        err = None
        for attempt in range(tries):
            ask = user if not err else (user + f"\n\nYour previous answer was rejected: {err}. "
                                        "Correct exactly these points and give the whole JSON again.")
            txt = client.ask(prompt, ask, f"{label}-{client.thinking}-a{attempt}")
            m = re.search(r"\{.*\}", txt, re.S)
            try:
                js = json.loads(m.group(0)) if m else None
                if js is None:
                    err = "no JSON object in the answer"
            except json.JSONDecodeError as e:
                # the notes are optional comments; a malformed notes object ("[568, 583]: …"
                # as a key) must not throw away a good stanzas list
                s = re.search(r'"stanzas"\s*:\s*(\[\s*(?:\[\s*\d+\s*,\s*\d+\s*\]\s*,?\s*)*\])', txt)
                try:
                    js = {"stanzas": json.loads(s.group(1)), "notes": {}} if s else None
                except json.JSONDecodeError:
                    js = None
                if js is None:
                    err = f"not valid JSON ({e})"
            if js is not None:
                err = check_groups(js, units, types, stops)
                if not err:
                    out.write_text(json.dumps(js, ensure_ascii=False), encoding="utf-8")
                    return client.thinking
            rej.mkdir(exist_ok=True)
            (rej / f"{label}-{client.thinking}-a{attempt}.txt").write_text(
                f"<!-- rejected: {err} -->\n{txt}", encoding="utf-8")
    raise RuntimeError(f"grouping {inp.name}: {err}")


# ── one text ─────────────────────────────────────────────────────────────────

def run(cmd, log):
    p = subprocess.run([PY, "-X", "utf8", *map(str, cmd)], cwd=VAULT, capture_output=True, text=True,
                       encoding="utf-8")
    log.write(f"$ {' '.join(map(str, cmd))}\n{p.stdout}{p.stderr}\n")
    log.flush()
    return p


def process(i, kind, thinking):
    LOGS.mkdir(exist_ok=True)
    work = WORK / i
    with (LOGS / f"workflow-{i}.log").open("a", encoding="utf-8") as log:
        log.write(f"\n=== {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        t0 = time.time()
        for f in [*work.glob("groups-*.json"), *work.glob("group-in-part*.md")]:
            # a new segmentation: old groupings and old split parts are invalid
            f.unlink()
        p = run([LIB, "segment", VAULT / f"0-INBOX/root/{i}.md", work], log)
        if not (work / "state.json").exists():
            return {"status": "failed", "note": "segment failed (no state.json) — see the log"}
        heads = "—"
        tree = VAULT / f"0-INBOX/temp/TOC-{i}/toc-tree-anchored-{i}.md"
        repaired, unresolved = 0, []
        if kind == "tree" and has_nodes(tree):
            # anchors that differ from the text only by a footnote marker or "༌" are rewritten
            # with the text's own words first (anchor_repair.py; the original tree is kept)
            repaired, unresolved = anchors.repair(tree, work / "prepared.md")
            log.write(f"anchor repair: fixed {repaired}, unresolved {unresolved}\n")
            p = run([LIB, "toc-ingest", work, "--tree", tree], log)
            m = re.search(r"body headings: (\S+) not placed", p.stdout)
            heads = f"{m.group(1) if m else '?'} not placed"
            if p.returncode != 0:
                return {"status": "failed", "note": "toc-ingest failed — see the log", "headings": heads}
        state = json.loads((work / "state.json").read_text(encoding="utf-8"))
        mode = state["modes"][0]                    # free | prose
        prompt = (PROMPTS / "stanza-grouping.md").read_text(encoding="utf-8")
        if mode == "prose":
            prompt = (PROMPTS / "prose-grouping.md").read_text(encoding="utf-8") + \
                "\n\n---\n\nFor the verse lines (V) inside the prose:\n\n" + prompt
        run([LIB, "group-split", work], log)
        g = gem.Gemini(thinking, work / "usage.jsonl", MODEL)
        fb = gem.Gemini("medium", work / "usage.jsonl", MODEL) if thinking == "low" else None
        parts = sorted(work.glob("group-in-part*.md"), key=lambda p: int(re.search(r"part(\d+)", p.name).group(1)))
        used = []
        if parts:
            for k, part in enumerate(parts, 1):
                used.append((k, group_one(g, prompt, part, work / f"groups-{mode}-part{k}.json", f"group-p{k}", fb)))
            run([LIB, "group-join", work], log)
        else:
            used.append((1, group_one(g, prompt, work / "group-in.md", work / f"groups-{mode}.json", "group", fb)))
        fell_back = [k for k, lv in used if lv != thinking]
        p = run([LIB, "finish", work], log)
        final = work / f"final-{mode}.md"
        if p.returncode != 0 or not final.exists():
            tail = (p.stdout + p.stderr).strip().splitlines()[-1:] or [""]
            return {"status": "failed", "note": f"finish failed: {tail[0][:160]}", "headings": heads}
        OUTDIR.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(final, OUTDIR / f"{i}.md")
        blocks = len(json.loads((work / f"groups-{mode}.json").read_text(encoding="utf-8"))["stanzas"])
        recs = [json.loads(x) for x in (work / "usage.jsonl").read_text(encoding="utf-8").splitlines()] \
            if (work / "usage.jsonl").exists() else []
        cost = sum(r["input"] * PRICE[0] + (r["output"] + r["thought"]) * PRICE[1] for r in recs) / 1e6
        notes = []
        if fell_back:
            notes.append(f"grouping fell back to medium for part(s) {', '.join(map(str, fell_back))}")
        if (work / "breaks-review.md").exists():
            notes.append("breaks-review.md: raw breaks ending mid-sentence")
        if repaired:
            notes.append(f"{repaired} anchor(s) repaired (footnote marker / ༌)")
        if heads not in ("—", "0 not placed"):
            notes.append("REVIEW: heading(s) not placed — insert by hand"
                         + (f" (anchor not in the text: {', '.join(unresolved)})" if unresolved else ""))
        return {"status": "done", "form_out": mode, "headings": heads, "blocks": blocks,
                "run": f"{thinking} · ${cost:.2f} · {round((time.time() - t0) / 60, 1)} min",
                "note": "; ".join(notes)}


def worker(n, args, stop, counter):
    while not stop.is_set():
        with local:
            if args.limit and counter[0] >= args.limit:
                return
            counter[0] += 1
        i, kind = claim(args.retry_failed, set(args.only or []), args.sizes)
        if not i:
            return
        print(f"[p{n}] {time.strftime('%H:%M:%S')} start {i} ({kind})", flush=True)
        try:
            f = process(i, kind, args.thinking)
        except Exception as e:
            f = {"status": "failed", "note": f"error: {e}"[:200]}
        record(i, f)
        print(f"[p{n}] {time.strftime('%H:%M:%S')} {f['status']:7} {i}  {f.get('run', '')}  {f.get('note', '')}",
              flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--procs", type=int, default=3)
    ap.add_argument("--mode", required=True, choices=MODES)
    ap.add_argument("--thinking", choices=["low", "medium", "high"], help="override the mode's level")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--reset-running", action="store_true")
    ap.add_argument("--retry-failed", action="store_true")
    ap.add_argument("--redo", nargs="+", metavar="ID",
                    help="run these texts again from the start, whatever their status (e.g. after a "
                         "rule change); only these are taken")
    args = ap.parse_args()
    if args.redo:
        args.only = args.redo
    sizes, level = MODES[args.mode]
    args.sizes, args.thinking = sizes, args.thinking or level
    with locked():
        d = wload()
        for i, kind in eligible(sizes).items():   # new finished TOC texts join the list
            d.setdefault(i, {"status": "todo", "toc": kind})
        tsz = toc.load()
        for i in args.redo or []:
            if i not in d:
                sys.exit(f"{i}: not in the workflow list (its TOC is not finished, or it is not this mode's size)")
            d[i]["status"], d[i]["run"], d[i]["note"] = "todo", "", "redo"
        if args.reset_running:
            for i, r in d.items():
                if r["status"] == "running" and tsz[i].get("size") in sizes:
                    r["status"], r["run"] = "todo", ""
        wsave(d)
        render(d)
        todo = sum(1 for i, r in d.items() if r["status"] == "todo" and tsz[i].get("size") in sizes)
    print(f"workflow batch, mode {args.mode}: {MODEL} grouping thinking {args.thinking} · sizes {sorted(sizes)} · "
          f"{todo} to do · {args.procs} at a time", flush=True)
    stop, counter = threading.Event(), [0]
    ts = [threading.Thread(target=worker, args=(n + 1, args, stop, counter)) for n in range(args.procs)]
    for t in ts:
        t.start()
    try:
        while any(t.is_alive() for t in ts):
            time.sleep(1)
    except KeyboardInterrupt:
        stop.set()
        print("stopping: texts in progress stay 'running' — re-run with --reset-running")
    print("done")


if __name__ == "__main__":
    main()
