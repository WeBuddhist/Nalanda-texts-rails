#!/usr/bin/env python3
"""Benchmark the Gemini grouping of the root-text workflow: thinking low vs medium.

    venv/Scripts/python.exe -X utf8 4-SYSTEM/scripts/seg-toc-benchmark/workflow_bench.py <id> ...
        [--levels low medium] [--out 0-INBOX/temp/workflow-bench]

Per text: segment (current rules) + TOC ingest once, then for each level a copy of that
working folder is grouped on gemini-3.8-flash and finished (block IDs + strict gate).
Score = F1 of the block boundaries (where each stanza / paragraph ends, compared on the
letters only) against the text's file in 0-INBOX/processed/root/ — the Claude-agent
grouping, reviewed by an editor for Ar_3CBa_ and Ar_3CBf_; not a gold standard for the
others. Writes <out>/REPORT.md.
"""
import argparse, importlib.util, json, re, shutil, sys, time
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("wf", VAULT / "0-INBOX/temp/root-toc/run_workflow_batch.py")
wf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wf)
DROP = re.compile(r"[\s།༔༎]")


def boundaries(path):
    t = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if t.startswith("---\n"):
        t = t[t.index("\n---\n", 4) + 5:]
    t = re.split(r"(?m)^\[\^\d+\]:", t)[0]
    S, b = "", set()
    for blk in re.split(r"\n[ \t]*\n", t):
        ls = [re.sub(r"\s\^[\w-]+\s*$", "", l) for l in blk.split("\n") if l.strip() and not l.lstrip().startswith("#")]
        if ls:
            S += DROP.sub("", "".join(ls))
            b.add(len(S))
    return S, b


def f1(ref, got):
    tp = len(ref & got)
    p, r = (tp / len(got) if got else 0), (tp / len(ref) if ref else 0)
    return 2 * p * r / (p + r) if p + r else 0, p, r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--levels", nargs="+", default=["low", "medium"])
    ap.add_argument("--out", default=str(VAULT / "0-INBOX/temp/workflow-bench"))
    a = ap.parse_args()
    out = Path(a.out)
    rows = []
    for i in a.ids:
        ref = next((VAULT / "0-INBOX/processed/root").glob(f"{i}-*.md"))
        base = out / i / "base"
        log = open(out / f"{i}.log", "a", encoding="utf-8") if out.mkdir(parents=True, exist_ok=True) is None else None
        if not (base / "state.json").exists():
            wf.run([wf.LIB, "segment", VAULT / f"0-INBOX/root/{i}.md", base], log)
            tree = VAULT / f"0-INBOX/temp/TOC-{i}/toc-tree-anchored-{i}.md"
            if tree.exists():
                wf.run([wf.LIB, "toc-ingest", base, "--tree", tree], log)
        mode = json.loads((base / "state.json").read_text(encoding="utf-8"))["modes"][0]
        prompt = (wf.PROMPTS / "stanza-grouping.md").read_text(encoding="utf-8")
        if mode == "prose":
            prompt = (wf.PROMPTS / "prose-grouping.md").read_text(encoding="utf-8") + \
                "\n\n---\n\nFor the verse lines (V) inside the prose:\n\n" + prompt
        Sr, br = boundaries(ref)
        for lv in a.levels:
            w = out / i / lv
            if w.exists():
                shutil.rmtree(w)
            shutil.copytree(base, w)
            t0 = time.time()
            g = wf.gem.Gemini(lv, w / "usage.jsonl", wf.MODEL)
            wf.run([wf.LIB, "group-split", w], log)
            parts = sorted(w.glob("group-in-part*.md"), key=lambda p: int(re.search(r"part(\d+)", p.name).group(1)))
            err = ""
            try:
                if parts:
                    for k, part in enumerate(parts, 1):
                        wf.group_one(g, prompt, part, w / f"groups-{mode}-part{k}.json", f"group-p{k}")
                    wf.run([wf.LIB, "group-join", w], log)
                else:
                    wf.group_one(g, prompt, w / "group-in.md", w / f"groups-{mode}.json", "group")
                p = wf.run([wf.LIB, "finish", w], log)
                if p.returncode:
                    err = "finish failed"
            except Exception as e:
                err = str(e)[:120]
            secs = time.time() - t0
            recs = [json.loads(x) for x in (w / "usage.jsonl").read_text(encoding="utf-8").splitlines()] \
                if (w / "usage.jsonl").exists() else []
            cost = sum(r["input"] * wf.PRICE[0] + (r["output"] + r["thought"]) * wf.PRICE[1] for r in recs) / 1e6
            final = w / f"final-{mode}.md"
            if final.exists() and not err:
                Sg, bg = boundaries(final)
                f, pr, rc = f1(br, bg) if Sg == Sr else (0, 0, 0)
                note = "" if Sg == Sr else "letters differ from the reference"
                nb = len(bg)
            else:
                f = pr = rc = 0
                nb, note = 0, err or "no final file"
            rows.append((i, mode, lv, len(br), nb, f, pr, rc, cost, secs, sum(r["thought"] for r in recs), note))
            print(f"{i} {mode} {lv}: blocks {nb} (ref {len(br)}) F1 {f:.3f} P {pr:.3f} R {rc:.3f} "
                  f"${cost:.3f} {secs:.0f}s {note}", flush=True)
    rep = ["# Workflow grouping benchmark — gemini-3.8-flash thinking low vs medium", "",
           "Block-boundary F1 against `0-INBOX/processed/root/` (Claude-agent grouping; editor-reviewed for "
           "Ar_3CBa_ and Ar_3CBf_). P = share of Gemini's block ends that the reference has; R = share of the "
           "reference's block ends that Gemini found.", "",
           "| Text | Form | Level | Blocks (ref) | F1 | P | R | Cost | Time | Thinking tok | Note |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, m, lv, nr, nb, f, pr, rc, c, s, th, note in rows:
        rep.append(f"| {i} | {m} | {lv} | {nb} ({nr}) | {f:.3f} | {pr:.3f} | {rc:.3f} | ${c:.3f} | {s:.0f} s | {th} | {note} |")
    for lv in a.levels:
        r = [x for x in rows if x[2] == lv]
        if r:
            rep.append(f"| **mean** | | {lv} | | **{sum(x[5] for x in r) / len(r):.3f}** | | | "
                       f"${sum(x[8] for x in r):.3f} total | {sum(x[9] for x in r):.0f} s total | | |")
    (out / "REPORT.md").write_text("\n".join(rep) + "\n", encoding="utf-8")
    print(f"report: {out / 'REPORT.md'}")


if __name__ == "__main__":
    main()
