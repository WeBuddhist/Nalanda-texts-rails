#!/usr/bin/env python3
"""Join per-part subtrees TOC-<id>/part-NN.md into TOC-<id>/toc-tree-<id>.md, run both
tree checkers on the PIPE working copy, and copy the tree to PIPE-<id>/closing-tree-<id>.md
so run_batch_pipeline.py ingests it.

Usage (vault root): python -X utf8 0-INBOX/temp/assemble_parts_tree.py ID
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

TEMP = Path(__file__).resolve().parent
LIB = TEMP.parents[1] / "4-SYSTEM" / "Skills" / "seg-toc-lib"
NODE = re.compile(r"^\s*\* ")


def main(cid):
    toc = TEMP / f"TOC-{cid}"
    parts = sorted(toc.glob("part-*.md"))
    nodes = []
    for p in parts:
        lines = [l.rstrip() for l in p.read_text(encoding="utf-8").splitlines() if NODE.match(l)]
        if not lines:
            print(f"WARNING: {p.name} has no node lines")
        nodes += lines
    front = [l for l in nodes if re.match(r"^\* (I|II|III)\.", l)]
    back = [l for l in nodes if re.match(r"^\s*\* [ab](\.|\.\d)", l)]
    body = [l for l in nodes if l not in front and l not in back]
    tree = toc / f"toc-tree-{cid}.md"
    tree.write_text("\n".join(
        ["---", f"source: {cid}", "skill: commentary-toc-extract", "stage: toc-tree-anchored",
         "mode: labels (per-chapter subagents)", "date: 2026-10-13", "model: claude-opus", "---", "",
         "## དཀར་ཆག / Table of Contents"] + front + body + back) + "\n", encoding="utf-8")
    print(f"{cid}: {len(parts)} parts, {len(nodes)} nodes -> {tree}")

    units = TEMP / f"PIPE-{cid}" / f"{cid}.units.md"
    for script, extra, rep in [("qc_check_tree.py", ["--corpus", units], "toc-tree-qc"),
                               ("qc_tree_vs_source.py", ["--source", units], "toc-tree-qc-source")]:
        r = subprocess.run([sys.executable, "-X", "utf8", str(LIB / script), str(tree), *map(str, extra),
                            "--out", str(toc / f"{rep}-{cid}.md")], capture_output=True, text=True,
                           encoding="utf-8")
        print(f"  {script}: {r.returncode} issues")
    shutil.copyfile(tree, TEMP / f"PIPE-{cid}" / f"closing-tree-{cid}.md")


if __name__ == "__main__":
    main(sys.argv[1])
