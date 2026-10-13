#!/usr/bin/env python3
"""commentary-pipeline WITHOUT re-segmentation, Gemini TOC at a chosen thinking level.

  segment (if no units file) -> Gemini TOC passes 1-2 (parallel) -> tree + QC ->
  frame nodes + anchoring -> ingest headings -> re-append footnotes ->
  stamp body IDs + strict text check against the source -> segmented-commentary-with-toc/

Footnote definitions ([^n]: …) are kept out of every model pass and re-appended verbatim.
Earlier TOC-<id> / RESEG-<id> folders are archived to *-prev-runs-<time>.

Usage (vault root):  python -u -X utf8 0-INBOX/temp/run_toc_only.py ID [--thinking=medium]
"""

import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import run_pipeline_orchestrator as orch
import run_step1

FOOT_RE = re.compile(r"^\[\^[^\]]+\]:", re.M)


def split_footnotes(text):
    m = FOOT_RE.search(text)
    if not m:
        return text.rstrip() + "\n", ""
    return text[: m.start()].rstrip() + "\n", text[m.start():].strip() + "\n"


def build_tree(cid, units, thinking):
    """extract_toc_tree.py main() in a child process with GEMINI_THINKING overridden."""
    code = (
        "import sys; sys.path.insert(0, sys.argv[1]); import extract_toc_tree as e; "
        f"e.GEMINI_THINKING = {thinking!r}; "
        "sys.argv = ['extract_toc_tree.py', sys.argv[2], '--commentary-id', sys.argv[3]]; e.main()"
    )
    orch.run_cmd([sys.executable, "-X", "utf8", "-c", code,
                  str(orch.TOC_EXTRACTOR_DIR), str(units), cid])


def _content_lines(body):
    """non-empty lines of the body after any YAML front matter, headings skipped"""
    text = re.sub(r"\A---\n.*?\n---\n", "", body, flags=re.S)
    return [l.strip() for l in text.splitlines() if l.strip() and not l.lstrip().startswith("#")]


def add_front_frame(cid, body):
    """I. frame anchored on the first line of real text (the orchestrator would take the
    YAML '---' line of files that carry front matter)."""
    tree = orch.TEMP_DIR / f"TOC-{cid}" / f"toc-tree-{cid}.md"
    t = tree.read_text(encoding="utf-8")
    if re.search(r"^\s*\*\s*I\.", t, re.M):
        return
    first = _content_lines(body)[0][:80]
    t = t.replace("## དཀར་ཆག / Table of Contents\n",
                  f"## དཀར་ཆག / Table of Contents\n* I. ཀླད་ཀྱི་དོན། [[{first}]]\n", 1)
    tree.write_text(t, encoding="utf-8")
    print(f"[{cid}] Added frame node I. ཀླད་ཀྱི་དོན། [[{first[:30]}…]]", flush=True)


def add_back_frame(cid, body):
    """b. frame on the author colophon (… མཛད་པ་རྫོགས་སོ) when the tree has no sections."""
    tree = orch.TEMP_DIR / f"TOC-{cid}" / f"toc-tree-{cid}.md"
    t = tree.read_text(encoding="utf-8")
    if re.search(r"^\s*\*\s*b\.", t, re.M):
        return
    lines = _content_lines(body)
    colo = next((l for l in lines if "མཛད་པ" in l and "རྫོགས" in l), None)
    if colo:
        tree.write_text(t.rstrip() + f"\n* b. མཇུག་བྱང། [[{colo[:80]}]]\n", encoding="utf-8")


def run_one(cid, thinking, resume=False):
    t0 = time.time()
    stamp = time.strftime("%Y%m%d-%H%M")
    for d in ([] if resume else (orch.TEMP_DIR / f"TOC-{cid}", orch.TEMP_DIR / f"RESEG-{cid}")):
        if d.exists():
            d.rename(d.with_name(f"{d.name}-prev-runs-{stamp}"))
            print(f"[{cid}] archived {d.name}", flush=True)

    units = orch.SEGMENTED_DIR / f"{cid}.units.md"
    if not units.exists():
        print(f"[{cid}] segmenting…", flush=True)
        _, passed, info = run_step1.process_text(cid)
        if not passed:
            raise RuntimeError(f"segmentation failed: {info}")
        print(info["res_stdout"], flush=True)

    body, foot = split_footnotes(units.read_text(encoding="utf-8"))
    src = orch.COMMENTARY_DIR / f"{cid}.md"
    if foot != split_footnotes(src.read_text(encoding="utf-8"))[1]:
        raise RuntimeError("units footnotes differ from source footnotes")

    work = orch.TEMP_DIR / f"PIPE-{cid}"
    work.mkdir(parents=True, exist_ok=True)
    (work / f"{cid}.units.md").write_text(body, encoding="utf-8")
    (work / f"{cid}.footnotes.md").write_text(foot, encoding="utf-8")

    orch.SEGMENTED_DIR = work
    orch.ett.GEMINI_THINKING = thinking            # passes 1-2 run in this process
    orch.run_parallel_toc_passes_1_2(cid, max_workers=8)
    build_tree(cid, work / f"{cid}.units.md", thinking)
    add_front_frame(cid, body)
    tree_text = (orch.TEMP_DIR / f"TOC-{cid}" / f"toc-tree-{cid}.md").read_text(encoding="utf-8")
    if re.search(r"^\s*\*\s*\d", tree_text, re.M):
        orch.add_frame_nodes_and_anchor(cid)    # find_toc_contexts.py (thinking medium)
    else:
        # Gemini found no sections: only frame nodes, nothing for find_toc_contexts to anchor
        print(f"[{cid}] tree has no section nodes — frame nodes only", flush=True)
        add_back_frame(cid, body)
    orch.run_ingest(cid)                        # -> work/<id>.toc.md (body only)

    # re-append footnotes, stamp body IDs, strict check against the source
    final = work / f"{cid}.final.md"
    final.write_text((work / f"{cid}.toc.md").read_text(encoding="utf-8").rstrip() + "\n\n" + foot,
                     encoding="utf-8")
    tree_json = orch.TEMP_DIR / f"TOC-{cid}" / f"toc-tree-{cid}.json"
    orch.run_cmd([sys.executable, "-X", "utf8", str(orch.LIB_DIR / "toc_tree_ingest.py"), "ingest",
                  "--tree", str(tree_json), "--commentary", str(final),
                  "--stamp-body-ids", "--verify-against", str(src)])

    out = orch.TOC_INGEST_DIR / f"{cid}.toc.md"
    shutil.copyfile(final, out)
    print(f"[{cid}] DONE in {time.time() - t0:.0f}s -> {out}", flush=True)


if __name__ == "__main__":
    thinking = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--thinking=")), "medium")
    ids = [a for a in sys.argv[1:] if not a.startswith("--")]
    # --source-dir=1-SOURCES/Text : read the source from there (read-only) instead of
    # 0-INBOX/commentary; every output still goes to 0-INBOX
    src_dir = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--source-dir=")), None)
    if src_dir:
        orch.COMMENTARY_DIR = run_step1.COMMENTARY_DIR = (orch.VAULT_ROOT / src_dir).resolve()
    failed = []
    for cid in ids:
        try:
            run_one(cid, thinking, resume="--resume" in sys.argv)
        except Exception as e:
            print(f"[{cid}] FAILED: {e}", flush=True)
            failed.append(cid)
    print(f"\nFinished. Failed: {failed or 'none'}")
