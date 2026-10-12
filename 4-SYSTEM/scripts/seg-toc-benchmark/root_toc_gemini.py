#!/usr/bin/env python3
"""Root-text TOC extraction on the Gemini API — the same passes as the skill
`root-text-toc-extract`, with the same prompt files, one API call where the skill
dispatches one isolated subagent.

    py -X utf8 4-SYSTEM/scripts/seg-toc-benchmark/root_toc_gemini.py <id> --thinking low|medium|high
        [--input 0-INBOX/temp/root-seg-v2/<id>/prepared.md]
        [--out 0-INBOX/temp/root-toc-bench/<id>/<thinking>] [--workers 8]

Passes: 1 candidates (per chunk) · 2 enumerations (per chunk) · merge · 3 tree ·
4 deterministic QC + repair (max 2 rounds) · 5 anchors (in text windows for a big text) ·
6 QC against the text.
Chunks: 150 lines, overlap 25 (as the skill). Every call is logged with its tokens to
<out>/usage.jsonl; <out>/summary.json holds the totals. The API key is read by the
same loader as extract_toc_tree.py (vault-root .env or the environment), never printed.
Finished chunk outputs are kept, so a re-run resumes.
"""
import argparse, importlib.util, json, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
LIB = VAULT / "4-SYSTEM/Skills/seg-toc-lib"
PROMPTS = LIB / "prompts"
MODEL = "gemini-3.8-flash"
# USD per million tokens, input / output (thinking billed as output); third-party list prices
PRICES = {"gemini-3.8-flash": (0.75, 3.75), "gemini-3.1-flash-lite": (0.25, 1.50)}


def api_key():
    spec = importlib.util.spec_from_file_location("ett", LIB / "toc_tree_extractor/extract_toc_tree.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m._gemini_api_key()


class Gemini:
    def __init__(self, thinking, log, model=MODEL):
        from google import genai
        self.genai, self.client, self.thinking, self.log = genai, genai.Client(api_key=api_key()), thinking, log
        self.model = model

    def ask(self, system, user, label, max_output=65536):
        from google.genai import types
        cfg = types.GenerateContentConfig(
            system_instruction=system, max_output_tokens=max_output,
            # no tools are used: switching automatic function calling off silences the
            # library's "Direct use of automatic function calling (AFC)…" warning
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
            thinking_config=None if self.thinking == "default"
            else types.ThinkingConfig(thinking_level=self.thinking))
        for attempt in range(1, 5):
            t0 = time.time()
            try:
                r = self.client.models.generate_content(model=self.model, contents=user, config=cfg)
            except Exception as e:                        # rate limit / transient
                if attempt == 4:
                    raise
                time.sleep(10 * attempt)
                continue
            um, fin = r.usage_metadata, str(r.candidates[0].finish_reason) if r.candidates else "NONE"
            rec = {"label": label, "model": self.model, "thinking": self.thinking, "attempt": attempt, "finish": fin,
                   "seconds": round(time.time() - t0, 1),
                   "input": um.prompt_token_count or 0, "output": um.candidates_token_count or 0,
                   "thought": getattr(um, "thoughts_token_count", 0) or 0}
            with self.log.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if "MAX_TOKENS" in fin or not (r.text or "").strip():
                continue                                    # cut off: never used
            return r.text.strip()
        raise RuntimeError(f"{label}: no complete reply after 4 attempts")


def strip_fence(t):
    return re.sub(r"^```[a-z]*\n|\n```$", "", t.strip())


def chunks(lines, size=150, overlap=25):
    out, start, k = [], 1, 0
    while True:
        end = min(start + size - 1, len(lines))
        out.append((k, start, end))
        if end >= len(lines):
            return out
        start, k = end - overlap + 1, k + 1


HEADINGS = ("Lines starting with # are editorial headings added by root-text-segment, not the "
            "author's text (in this input they are blanked): never take them as candidates or "
            "nodes, never anchor on them, never nest the tree under them.")
P5_RULE = ("Numbered nodes only — do not add the frame nodes I. / a. / b.; the front matter and "
           "colophons are headed elsewhere. A preamble before node 1 may be II. " + HEADINGS)
NODE = re.compile(r"^\s*\*\s+(\S+?)\.?\s")


def text_windows(lines, max_chars, overlap=20):
    """Consecutive line windows of at most max_chars characters (20 lines overlap)."""
    wins, s = [], 0
    while s < len(lines):
        e, n = s, 0
        while e < len(lines) and (n + len(lines[e]) + 1 <= max_chars or e == s):
            n += len(lines[e]) + 1
            e += 1
        wins.append((s + 1, e))
        if e >= len(lines):
            break
        s = max(e - overlap, s + 1)
    return wins


def pass5(g, tid, tree, lines, out, max_chars):
    """Anchor the tree. A text that fits one window: one call, as the skill. A bigger text:
    one call per window of text, in order, each returning only the nodes that begin inside
    its window (the thinking + answer of one call over the whole text can exceed the
    65,536-token output limit at thinking `high`); the script merges them in tree order."""
    system = (PROMPTS / "pass5-anchors.md").read_text(encoding="utf-8")
    wins = text_windows(lines, max_chars)
    if len(wins) == 1:
        return strip_fence(g.ask(system, f"{P5_RULE}\n\n--- TREE ---\n{tree}\n\n"
                                         f"--- TEXT ({tid}, read all of it) ---\n" + "\n".join(lines), "p5"))
    found, last = {}, None                     # node id -> full anchored line
    wdir = out / "pass5-windows"
    wdir.mkdir(exist_ok=True)
    for w, (s, e) in enumerate(wins):
        f = wdir / f"window_{w:03d}.md"
        if not f.exists():
            cursor = (f"The last node already anchored, in an earlier window, is {last}; continue "
                      f"after it." if last else "No node has been anchored yet.")
            ans = g.ask(system,
                        f"{P5_RULE}\n\nThe text is long, so it is given in windows. This is window "
                        f"{w + 1} of {len(wins)} (lines {s}–{e}). {cursor}\nOutput ONLY the lines "
                        f"`* <id> <title> [[<context>]]` of the nodes whose beginning lies inside "
                        f"THIS window, in order, titles and numbering unchanged, nothing else. If no "
                        f"node begins in this window, output exactly NONE.\n\n--- TREE ---\n{tree}\n\n"
                        f"--- TEXT WINDOW (lines {s}–{e}) ---\n" + "\n".join(lines[s - 1:e]),
                        f"p5-w{w:03d}")
            f.write_text(strip_fence(ans) + "\n", encoding="utf-8")
        for l in f.read_text(encoding="utf-8").splitlines():
            m = NODE.match(l)
            if m and "[[" in l and m.group(1) not in found:   # first window that finds it wins
                found[m.group(1)] = l.strip()
                last = m.group(1)
    rows = []
    for l in tree.splitlines():
        m = NODE.match(l)
        if not m:
            rows.append(l)
            continue
        indent = l[:len(l) - len(l.lstrip())]
        rows.append(indent + found[m.group(1)] if m.group(1) in found
                    else re.sub(r"\s*\[\[.*\]\]\s*$", "", l.rstrip()) + " [[?]]")
    for i, l in found.items():                 # a frame / preamble node the tree did not have
        if not any(NODE.match(r) and NODE.match(r).group(1) == i for r in rows):
            rows.insert(next((k + 1 for k, r in enumerate(rows) if r.startswith("## ")), 0), l)
    return "\n".join(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id")
    ap.add_argument("--thinking", required=True, choices=["default", "minimal", "low", "medium", "high"],
                    help="default = send no thinking setting (the model's own default)")
    ap.add_argument("--model", default=MODEL, choices=sorted(PRICES))
    ap.add_argument("--input")
    ap.add_argument("--out")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--window-chars", type=int, default=60000,
                    help="pass 5 text window (≈ 40k tokens of Tibetan); a text this size or "
                         "smaller is anchored in one call")
    a = ap.parse_args()
    src = Path(a.input or VAULT / f"0-INBOX/temp/root-seg-v2/{a.id}/prepared.md")
    tag = a.thinking if a.model == MODEL else f"{a.model.replace('gemini-', '')}-{a.thinking}"
    out = Path(a.out or VAULT / f"0-INBOX/temp/root-toc-bench/{a.id}/{tag}")
    (out / "candidates").mkdir(parents=True, exist_ok=True)
    (out / "enumerations").mkdir(parents=True, exist_ok=True)
    g = Gemini(a.thinking, out / "usage.jsonl", a.model)
    # The segmenter's own editorial headings (## ཀླད་ཀྱི་དོན། ^I-0, ## གཞུང་དངོས། ^1-0,
    # ## མཇུག་བྱང། ^a-0 …) are not the author's text: blank them so no pass takes them for
    # parts. Blanked, not removed, so line numbers still match prepared.md.
    lines = ["" if l.lstrip().startswith("#") else l
             for l in src.read_text(encoding="utf-8").splitlines()]
    ch = chunks(lines)
    p1, p2 = (PROMPTS / "pass1-candidates-root.md").read_text(encoding="utf-8"), \
             (PROMPTS / "pass2-enumerations.md").read_text(encoding="utf-8")

    def run_chunk(c, kind):
        k, s, e = c
        f = out / kind / f"chunk_{k:03d}.md"
        if f.exists():
            return
        text = "\n".join(lines[s - 1:e])
        head = f"<!-- chunk {k:03d} | lines {s}–{e} | source: {a.id} -->"
        if kind == "candidates":
            ans = g.ask(p1, f"Source: {a.id}, lines {s}–{e} of the text. Extract the section "
                            f"candidates from these lines only. {HEADINGS}\n\n--- TEXT ---\n{text}\n--- END ---",
                        f"p1-{k:03d}")
            ans = "<!-- no candidates -->" if ans.strip().startswith("NO CANDIDATES") else ans
            f.write_text(f"{head}\n{ans}\n", encoding="utf-8")
        else:
            ans = g.ask(p2, f"Source: {a.id}, lines {s}–{e} of the text. Copy the division "
                            f"announcements verbatim.\n\n--- TEXT ---\n{text}\n--- END ---",
                        f"p2-{k:03d}")
            f.write_text(ans + "\n", encoding="utf-8")

    t0 = time.time()
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda c: run_chunk(c, "candidates"), ch))
    cand_files = sorted((out / "candidates").glob("chunk_*.md"))
    summary = {"id": a.id, "model": a.model, "thinking": a.thinking, "chunks": len(ch), "units": len(lines)}
    if all("no candidates" in f.read_text(encoding="utf-8") for f in cand_files):
        summary["status"] = "no-parts"
    else:
        with ThreadPoolExecutor(a.workers) as ex:
            list(ex.map(lambda c: run_chunk(c, "enumerations"), ch))
        cand = out / f"toc-candidates-{a.id}.md"
        enum = out / f"toc-enumerations-{a.id}.md"
        cand.write_text("\n".join(f.read_text(encoding="utf-8") for f in cand_files), encoding="utf-8")
        enum.write_text("\n".join(t for f in sorted((out / "enumerations").glob("chunk_*.md"))
                                  if "NO ENUMERATIONS" not in (t := f.read_text(encoding="utf-8"))),
                        encoding="utf-8")
        # pass 3
        tree = out / f"toc-tree-{a.id}.md"
        if not tree.exists():
            ans = g.ask((PROMPTS / "pass3-tree.md").read_text(encoding="utf-8"),
                        f'Build the tree for "{a.id}".\n\n--- SECTION CANDIDATES ---\n'
                        f'{cand.read_text(encoding="utf-8")}\n\n--- ENUMERATIONS ---\n'
                        f'{enum.read_text(encoding="utf-8") or "NO ENUMERATIONS"}', "p3")
            tree.write_text(strip_fence(ans) + "\n", encoding="utf-8")
        # pass 4
        qc = out / f"toc-tree-qc-{a.id}.md"
        corpus = [str(cand), str(enum)]
        issues = []
        for rnd in range(3):
            subprocess.run([sys.executable, "-X", "utf8", str(LIB / "qc_check_tree.py"), str(tree),
                            "--corpus", *corpus, "--out", str(qc)], capture_output=True)
            n = int(re.search(r"issues:\s*(\d+)", qc.read_text(encoding="utf-8")).group(1))
            issues.append(n)
            if n == 0 or rnd == 2:
                break
            ans = g.ask((PROMPTS / "pass4-qc-repair.md").read_text(encoding="utf-8"),
                        f"--- TREE ---\n{tree.read_text(encoding='utf-8')}\n\n--- QC ISSUES ---\n"
                        f"{qc.read_text(encoding='utf-8')}\n\n--- ENUMERATIONS ---\n"
                        f"{enum.read_text(encoding='utf-8') or 'NO ENUMERATIONS'}\n\n"
                        f"--- SECTION CANDIDATES ---\n{cand.read_text(encoding='utf-8')}\n\n"
                        f"--- SOURCE TEXT (only for an announced-count issue) ---\n{chr(10).join(lines)}",
                        f"p4-{rnd}")
            tree.write_text(strip_fence(ans) + "\n", encoding="utf-8")
            corpus = [str(cand), str(enum), str(src)]
        summary["qc4"] = "→".join(map(str, issues))
        if not re.search(r"^\s*\*\s+\d", tree.read_text(encoding="utf-8"), re.M):
            # pass 3 kept none of the candidates as a part (a count, a list of offerings …):
            # the text announces no parts — no anchors to find, nothing to ingest
            summary.update(status="no-parts", nodes=0, parts=0,
                           note="pass 1 found candidates, pass 3 kept none as a part")
            return finish_summary(summary, out, a, t0)
        # pass 5
        anch = out / f"toc-tree-anchored-{a.id}.md"
        if not anch.exists():
            anch.write_text(pass5(g, a.id, tree.read_text(encoding="utf-8"), lines, out,
                                  a.window_chars) + "\n", encoding="utf-8")
        summary["pass5_windows"] = len(text_windows(lines, a.window_chars))
        # pass 6
        q6 = out / f"toc-tree-qc-source-{a.id}.md"
        subprocess.run([sys.executable, "-X", "utf8", str(LIB / "qc_tree_vs_source.py"), str(anch),
                        "--source", str(src), "--out", str(q6)], capture_output=True)
        m6 = re.search(r"issues:\s*(\d+)", q6.read_text(encoding="utf-8")) if q6.exists() else None
        summary["qc6"] = int(m6.group(1)) if m6 else None
        t = anch.read_text(encoding="utf-8")
        summary["nodes"] = len(re.findall(r"^\s*\*\s+\d", t, re.M))
        summary["parts"] = len(re.findall(r"^\*\s+\d+\.?\s", t, re.M))
        summary["unanchored"] = t.count("[[?]]")
        summary["status"] = "done"
    finish_summary(summary, out, a, t0)


def finish_summary(summary, out, a, t0):
    """Totals from usage.jsonl → summary.json (and print it)."""
    recs = [json.loads(l) for l in (out / "usage.jsonl").read_text(encoding="utf-8").splitlines()] \
        if (out / "usage.jsonl").exists() else []
    ti, to, tt = (sum(r[k] for r in recs) for k in ("input", "output", "thought"))
    summary.update(calls=len(recs), input_tokens=ti, output_tokens=to, thinking_tokens=tt,
                   cost_usd=round(ti / 1e6 * PRICES[a.model][0] + (to + tt) / 1e6 * PRICES[a.model][1], 3),
                   wall_seconds=round(time.time() - t0))
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
