#!/usr/bin/env python3
"""
One-command Gemini benchmark: runs the whole seg + TOC pipeline with Gemini answering
every model step, repeats it, scores it against the gold files and against the Opus
baseline, and writes a report.

Run from the benchmark folder (the one that contains 4-SYSTEM/ and 0-INBOX/bench8/):

    python 4-SYSTEM/scripts/seg-toc-benchmark/gemini_bench.py
    python 4-SYSTEM/scripts/seg-toc-benchmark/gemini_bench.py --files taranatha --levels low high --runs 3
    python 4-SYSTEM/scripts/seg-toc-benchmark/gemini_bench.py --files all

Per run and file:
  1. segmentation (deterministic, identical to the Opus runs);
  2. heading tree — `verses`/`top` files: one Gemini call with prompts/verse-headings.md
     (system) + mode, root text and commentary (user); `sabcad` files keep the fixed v2
     tree, as in the Opus runs; then the frame headings (I., a., b.) are merged in;
  3. ingest (deterministic);
  4. re-segmentation windows — Gemini answers the same window prompts the Opus agents got;
  5. QC — likewise; then finish + score.

Re-running the command continues where it stopped (answers on disk are kept).
Report: 0-INBOX/bench8/gemini-<model>-report.md. API key: vault-root .env (never printed).

--offline-from <ver> answers from an earlier run instead of the API (for testing the
pipeline without a key): trees and identical prompts are copied, anything else gets [].
"""
import argparse
import json
import os
import re
import shutil
import statistics as st
import subprocess
import sys
import time
from pathlib import Path

if not sys.flags.utf8_mode:      # Tibetan file names and text on Windows
    # os.execv on Windows starts a new process and returns to the prompt at once,
    # so the console looked stuck at the end; run the child and wait for it instead
    sys.exit(subprocess.call([sys.executable, "-X", "utf8", *sys.argv]))

HERE = Path(__file__).resolve().parent
V = Path(".").resolve()
sys.path.insert(0, str(HERE))
B = "4-SYSTEM/scripts/seg-toc-benchmark"
PROMPT = "4-SYSTEM/Skills/commentary-toc-extract/prompts/verse-headings.md"
CFGP = V / "0-INBOX/bench8/config.json"
ALL = ["taranatha", "dharmabhadra", "tenga", "gendun-drub", "karma-maitri",
       "sangye-nyenpa", "padma-namgyal", "drakpa"]


def cfg():
    return json.loads(CFGP.read_text(encoding="utf-8"))


def sh(*args, files=None, check=True):
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8", BENCH_NO_CACHE="1")
    if files:
        env["BENCH_FILES"] = ",".join(files)
    r = subprocess.run([sys.executable, *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env, cwd=V)
    if check and r.returncode != 0:
        sys.exit(f"FAILED: {' '.join(map(str, args))}\n{r.stdout[-1500:]}\n{r.stderr[-1500:]}")
    return r


def ver_name(model, level, k):
    tag = model.replace("gemini-", "").replace("-preview", "").replace(".", "")
    return f"g{tag}-{level}-r{k}"


def ensure_variant(ver):
    c = cfg()
    if ver not in c["variants"]:
        c["variants"][ver] = {"seg": ["--enum-chain broad", "--quotes {quotes}", "--colophon-guard"],
                              "tree": {"name": ver, "for": ["sabcad", "verses", "top"]},
                              "ingest": ["--split-frame-nodes"]}
        CFGP.write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")


def write_tree_prompt(fid, ver):
    c = cfg()
    f = c["files"][fid]
    d = V / "0-INBOX/bench8" / fid / ver
    user = (f"Mode: {f['headings']}\n\n"
            f"The root text:\n\n{(V / c['root']).read_text(encoding='utf-8')}\n\n"
            f"The commentary:\n\n{(d / '1-segmented.md').read_text(encoding='utf-8')}\n\n"
            "Reply with the tree only, exactly in the output format of the instructions "
            "(the `## དཀར་ཆག / Table of Contents` header and the `* …` lines), nothing else.")
    (d / "tree.prompt.md").write_text("=== SYSTEM PROMPT ===\n" + (V / PROMPT).read_text(encoding="utf-8")
                                      + "\n=== USER PROMPT ===\n" + user, encoding="utf-8")
    return d / "tree.prompt.md"


def answer(prompts, a, offline_src=None):
    """Answer prompt files with Gemini (or, offline, from an earlier run)."""
    import gemini_answer as G
    todo = list(G.pending(prompts))
    for p in todo:
        if offline_src:
            out, is_json = G.answer_path(p)
            src = Path(str(p).replace(offline_src[0], offline_src[1]))
            srco, _ = G.answer_path(src)
            if p.name == "tree.prompt.md":
                srco = next((x for x in (src.with_name("verse-tree.md"), src.with_name("toc-tree-anchored.md"))
                             if x.exists()), None)
                shutil.copy(srco, out) if srco else out.write_text("", encoding="utf-8")
            elif src.exists() and srco.exists() and src.read_bytes() == p.read_bytes():
                shutil.copy(srco, out)
            else:
                out.write_text("[]\n", encoding="utf-8")
            continue
        mo = 65536 if p.name == "tree.prompt.md" else a.max_output
        m = G.ask(p, a.model, a.level, mo, V / "0-INBOX/bench8/gemini-usage.jsonl")
        print(f"      {p.parent.parent.name}/{p.name}: {m['seconds']}s · thinking {m['thinking_tokens']} · out {m['output_tokens']}")
    return len(todo)


def run_one(fid, ver, a, offline):
    c = cfg()
    d = V / "0-INBOX/bench8" / fid / ver
    if (d / "4-final.md").exists():
        print(f"    {fid}: already finished"); return
    t0 = time.time()
    sh(f"{B}/variant.py", "seg", ver, files=[fid])
    h = c["files"][fid]["headings"]
    tree = d / "toc-tree-anchored.md"
    if not tree.exists():
        if h == "sabcad":
            shutil.copy(V / f"0-INBOX/bench8/{fid}/v2/toc-tree-anchored.md", tree)
        else:
            p = write_tree_prompt(fid, ver)
            answer([p], a, offline and (ver, offline.replace("{k}", ver.rsplit("-r", 1)[1])))
            sh(f"{B}/merge_trees.py", str(d / "verse-tree.md"),
               f"0-INBOX/bench8/{fid}/v1.3/toc-tree-anchored.md", str(tree))
    sh(f"{B}/variant.py", "ingest", ver, files=[fid])
    sh(f"{B}/variant.py", "reseg", ver, files=[fid])
    src = offline and (f"RESEG-{fid}-{ver}", f"RESEG-{fid}-" + offline.replace("{k}", ver.rsplit("-r", 1)[1]))
    answer([V / f"0-INBOX/temp/RESEG-{fid}-{ver}/claude"], a, src)
    for _ in range(4):
        sh(f"{B}/variant.py", "qc", ver, files=[fid])
        todo = json.loads((V / f"0-INBOX/bench8/todo-qc-{ver}.json").read_text(encoding="utf-8"))
        if not todo:
            break
        answer([Path(t) for t in todo], a, src)
    sh(f"{B}/variant.py", "finish", ver, files=[fid])
    (d / "run-seconds.txt").write_text(f"{time.time() - t0:.0f}\n", encoding="utf-8")
    print(f"    {fid}: done in {time.time() - t0:.0f}s")


def metrics(fid, path):
    from score import score
    s = score(cfg()["files"][fid]["gold"], str(path))
    return {"comp": s["composite"], "bf1": s["seg"]["boundary_exact"]["F1"],
            "hf1": s["toc"]["heading_title"]["F1"],
            "place": s["toc"]["placement_exact_rate"] * s["toc"]["heading_title"]["R"],
            "ident": s["text_identical"]}


def failures(fid, ver):
    d = V / "0-INBOX/bench8" / fid / ver
    ing = (d / "ingest.log").read_text(encoding="utf-8") if (d / "ingest.log").exists() else ""
    rl = (d / "reseg.log").read_text(encoding="utf-8") if (d / "reseg.log").exists() else ""
    nf = re.search(r"Not found:\s+(\d+)", ing)
    ve = re.search(r"Validation errors \((\d+)\)", rl)
    return {"not_placed": int(nf.group(1)) if nf else 0, "invalid_ops": int(ve.group(1)) if ve else 0,
            "verse_violations": rl.count("protected verse"), "json_errors": rl.count("JSON parse error")}


def usage(fid, ver):
    tot = {"input": 0, "output": 0, "thinking": 0, "calls": 0, "secs": 0.0}
    for m in list((V / "0-INBOX/bench8" / fid / ver).glob("*.meta.json")) + \
             list((V / "0-INBOX/temp" / f"RESEG-{fid}-{ver}").rglob("*.meta.json")):
        j = json.loads(m.read_text(encoding="utf-8"))
        tot["input"] += j.get("input_tokens") or 0
        tot["output"] += j.get("output_tokens") or 0
        tot["thinking"] += j.get("thinking_tokens") or 0
        tot["calls"] += 1
        tot["secs"] += j.get("seconds") or 0
    return tot


def report(files, a):
    L = [f"# Gemini benchmark — {a.model}, thinking {' vs '.join(a.levels)}, {a.runs} runs per setting\n",
         f"Baseline: Opus 5.5 runs `{a.baseline}-r1..r3` (same prompts, same scoring).",
         "Composite = mean of boundary F1, heading F1, placement × recall, ID × recall. "
         "Median over runs (min–max).\n",
         "| file | Opus 5.5 | " + " | ".join(f"Gemini {a.level_label(l)}" for l in a.levels) + " |",
         "|---|---|" + "---|" * len(a.levels)]
    detail = ["\n## Detail (medians)\n",
              "| file | setting | composite | boundary F1 | heading F1 | placement | not placed | invalid ops | verse violations | JSON errors | text identical |",
              "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    cost = ["\n## Cost and time per run (Gemini)\n",
            "| file | thinking | calls | input tok | output tok | of which thinking | API seconds | est. cost (USD) |",
            "|---|---|---:|---:|---:|---:|---:|---:|"]
    labels = ["Opus 5.5"] + [a.level_label(l) for l in a.levels]
    means = {lab: [] for lab in labels}
    for fid in files:
        row = [fid]
        settings = [("Opus 5.5", [f"{a.baseline}-r{k}" for k in range(1, 4)])] + \
                   [(a.level_label(l), [ver_name(a.model, l, k) for k in range(1, a.runs + 1)]) for l in a.levels]
        for label, vers in settings:
            ms = [(v, metrics(fid, V / "0-INBOX/bench8" / fid / v / "4-final.md")) for v in vers
                  if (V / "0-INBOX/bench8" / fid / v / "4-final.md").exists()]
            if not ms:
                row.append("—"); continue
            cs = [m["comp"] for _, m in ms]
            row.append(f"{st.median(cs):.3f} ({min(cs):.3f}–{max(cs):.3f})")
            means[label].append(st.median(cs))
            md = lambda k: st.median(m[k] for _, m in ms)
            fl = [failures(fid, v) for v, _ in ms]
            sm = lambda k: sum(x[k] for x in fl)
            detail.append(f"| {fid} | {label} | {md('comp'):.3f} | {md('bf1'):.3f} | {md('hf1'):.3f} | {md('place'):.3f} | "
                          f"{sm('not_placed')} | {sm('invalid_ops')} | {sm('verse_violations')} | {sm('json_errors')} | "
                          f"{all(m['ident'] for _, m in ms)} |")
            if label != "Opus 5.5":
                us = [usage(fid, v) for v, _ in ms]
                mu = lambda k: st.mean(u[k] for u in us)
                # Gemini 3.8 Flash intro pricing (to 31 Dec 2026): $0.75 / 1M input, $3.75 / 1M output incl. thinking
                usd = mu("input") / 1e6 * a.price_in + (mu("output") + mu("thinking")) / 1e6 * a.price_out
                cost.append(f"| {fid} | {label} | {mu('calls'):.0f} | {mu('input'):,.0f} | {mu('output') + mu('thinking'):,.0f} | "
                            f"{mu('thinking'):,.0f} | {mu('secs'):.0f} | {usd:.3f} |")
        L.append("| " + " | ".join(row) + " |")
    L.append("| **mean** | " + " | ".join(f"**{st.mean(means[lab]):.3f}**" if len(means[lab]) == len(files) else "—"
                                       for lab in labels) + " |")
    L += detail + cost
    L.append("\n(Text identical = the output's text is exactly the source text. Not placed = headings whose "
             "anchor could not be found. Invalid ops / verse violations = model operations the pipeline "
             "rejected. Prices: Gemini 3.8 Flash introductory rates; thinking is billed as output.)")
    out = V / f"0-INBOX/bench8/gemini-{a.model}-report.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[:6 + len(files) + 1]))
    print(f"\nReport: {out}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default="gemini-3.8-flash")
    ap.add_argument("--levels", nargs="+", default=["low", "high"], choices=["minimal", "low", "medium", "high"])
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--files", nargs="+", default=["taranatha"], help="commentary ids, or 'all'")
    ap.add_argument("--max-output", type=int, default=32768, help="re-segmentation / QC calls (tree: 65536)")
    ap.add_argument("--baseline", default="o2", help="Opus runs to compare with (<name>-r1..r3)")
    ap.add_argument("--price-in", type=float, default=0.75)
    ap.add_argument("--price-out", type=float, default=3.75)
    ap.add_argument("--offline-from", help="test without the API: answer from run <name>-r{k}, e.g. o2-r{k}")
    ap.add_argument("--report-only", action="store_true")
    a = ap.parse_args()
    a.level_label = lambda l: f"{a.model.replace('gemini-', '')} {l}"
    files = ALL if a.files == ["all"] else a.files
    if not a.report_only:
        if not a.offline_from:
            import gemini_answer as G
            G.client()           # fail fast if the key or the SDK is missing
        for level in a.levels:
            a.level = level
            for k in range(1, a.runs + 1):
                ver = ver_name(a.model, level, k)
                ensure_variant(ver)
                print(f"== {ver}")
                for fid in files:
                    run_one(fid, ver, a, a.offline_from)
    report(files, a)


if __name__ == "__main__":
    main()
