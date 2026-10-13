#!/usr/bin/env python3
"""Finish the Ka_3CD* TOC rerun (2026-10-13) for one or more ids.

For each id: QC the new anchored tree (both checkers), ingest it into the heading-free
resegmented base (PIPE-<id>/<id>.rebase.md), re-append the footnote apparatus, stamp
body block IDs and verify the text against the previous final file (backup), then copy
the result to segmented-commentary-with-toc/<id>.toc.md.

Usage (vault root):  python -X utf8 0-INBOX/temp/finish_ka_rerun.py [--qc-only] ID [ID ...]
"""

import shutil
import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
TEMP = VAULT / "0-INBOX" / "temp"
LIB = VAULT / "4-SYSTEM" / "Skills" / "seg-toc-lib"
BACKUP = TEMP / "Ka-toc-rerun-backup-20261013"
OUT_DIR = TEMP / "segmented-commentary-with-toc"


def run(args):
    p = subprocess.run([sys.executable, "-X", "utf8", *map(str, args)],
                       capture_output=True, text=True, encoding="utf-8")
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def qc(cid):
    toc = TEMP / f"TOC-{cid}"
    tree = toc / f"toc-tree-{cid}.md"
    base = TEMP / f"PIPE-{cid}" / f"{cid}.rebase.md"
    rc1, out1 = run([LIB / "qc_check_tree.py", tree, "--corpus", base,
                     "--out", toc / f"toc-tree-qc-{cid}.md"])
    rc2, out2 = run([LIB / "qc_tree_vs_source.py", tree, "--source", base,
                     "--out", toc / f"toc-tree-qc-source-{cid}.md"])
    print(f"[{cid}] qc_check_tree issues={rc1}  qc_tree_vs_source issues={rc2}")
    return rc1, rc2


def verify_source(cid):
    """Original source when the pipeline has it, else the heading-free base + footnotes
    (the previous final file with only its headings and block IDs removed)."""
    src = VAULT / "0-INBOX" / "commentary" / f"{cid}.md"
    if src.exists():
        return src
    pipe = TEMP / f"PIPE-{cid}"
    ref = pipe / f"{cid}.verify-src.md"
    foot = (pipe / f"{cid}.rebase.footnotes.md").read_text(encoding="utf-8")
    body = (pipe / f"{cid}.rebase.md").read_text(encoding="utf-8").rstrip() + "\n"
    ref.write_text(body + ("\n" + foot if foot else ""), encoding="utf-8")
    return ref


def finish(cid):
    toc = TEMP / f"TOC-{cid}"
    pipe = TEMP / f"PIPE-{cid}"
    tree_json = toc / f"toc-tree-{cid}.json"
    work = pipe / f"{cid}.rerun.toc.md"

    rc, out = run([LIB / "toc_tree_ingest.py", "parse",
                   "--input", toc / f"toc-tree-{cid}.md", "--out", tree_json])
    print(out.strip())
    if rc:
        raise RuntimeError(f"[{cid}] parse failed")

    shutil.copyfile(pipe / f"{cid}.rebase.md", work)
    rc, out = run([LIB / "toc_tree_ingest.py", "ingest", "--tree", tree_json,
                   "--commentary", work, "--split-frame-nodes"])
    print(out.strip())
    if rc:
        raise RuntimeError(f"[{cid}] ingest exit {rc}")

    foot = (pipe / f"{cid}.rebase.footnotes.md").read_text(encoding="utf-8")
    body = work.read_text(encoding="utf-8").rstrip() + "\n"
    work.write_text(body + ("\n" + foot if foot else ""), encoding="utf-8")

    rc, out = run([LIB / "toc_tree_ingest.py", "ingest", "--tree", tree_json,
                   "--commentary", work, "--stamp-body-ids",
                   "--verify-against", verify_source(cid)])
    print(out.strip())
    if rc:
        raise RuntimeError(f"[{cid}] stamp/verify exit {rc}")

    shutil.copyfile(work, OUT_DIR / f"{cid}.toc.md")
    print(f"[{cid}] DONE -> {OUT_DIR / f'{cid}.toc.md'}")


if __name__ == "__main__":
    qc_only = "--qc-only" in sys.argv
    for cid in [a for a in sys.argv[1:] if not a.startswith("--")]:
        qc(cid)
        if not qc_only:
            try:
                finish(cid)
            except Exception as e:
                print(f"FAILED: {e}")
