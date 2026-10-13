#!/usr/bin/env python3
"""Batch commentary-pipeline driver (wraps run_pipeline_orchestrator.py).

Differences from calling the orchestrator directly:
  * segments the file first (run_step1.process_text) when no units file exists;
  * keeps the footnote apparatus ([^n]: …) OUT of the TOC passes and the
    resegment windows (body-only working copy), then re-appends it verbatim
    before block-ID stamping, so the strict text check runs on the whole file;
  * copies the final stamped file to segmented-commentary-with-toc/<id>.toc.md.

Usage (from the vault root):  python -u -X utf8 0-INBOX/temp/run_batch_pipeline.py ID [ID ...]
"""

import re
import shutil
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import run_pipeline_orchestrator as orch
import run_step1

FOOT_RE = re.compile(r"^\[\^[^\]]+\]:", re.M)


def split_footnotes(text: str):
    m = FOOT_RE.search(text)
    if not m:
        return text.rstrip() + "\n", ""
    return text[: m.start()].rstrip() + "\n", text[m.start():].strip() + "\n"


def run_one(cid: str, workers: int):
    t0 = time.time()
    units = orch.SEGMENTED_DIR / f"{cid}.units.md"
    if not units.exists():
        print(f"[{cid}] segmenting…", flush=True)
        _, passed, info = run_step1.process_text(cid)
        if not passed:
            raise RuntimeError(f"[{cid}] segmentation failed: {info}")
        print(info["res_stdout"], flush=True)

    body, foot = split_footnotes(units.read_text(encoding="utf-8"))
    src_foot = split_footnotes((orch.COMMENTARY_DIR / f"{cid}.md").read_text(encoding="utf-8"))[1]
    if foot != src_foot:
        raise RuntimeError(f"[{cid}] units footnotes differ from source footnotes")

    work = orch.TEMP_DIR / f"PIPE-{cid}"
    work.mkdir(parents=True, exist_ok=True)
    (work / f"{cid}.units.md").write_text(body, encoding="utf-8")
    (work / f"{cid}.footnotes.md").write_text(foot, encoding="utf-8")

    # TOC passes, tree, anchoring and ingest on the body-only copy
    orch.SEGMENTED_DIR = work
    closing = work / f"closing-tree-{cid}.md"
    if closing.exists():
        # no sa bcad: chapter tree from the text's own closing lines replaces the
        # Gemini tree (kept as toc-tree-<id>.gemini.md); stale reseg windows go too
        toc_folder = orch.ensure_dirs(cid)
        tree = toc_folder / f"toc-tree-{cid}.md"
        if tree.exists() and not (toc_folder / f"toc-tree-{cid}.gemini.md").exists():
            tree.rename(toc_folder / f"toc-tree-{cid}.gemini.md")
        shutil.copyfile(closing, tree)
        wins = orch.TEMP_DIR / f"RESEG-{cid}" / "windows"
        if wins.exists() and any(wins.iterdir()):
            shutil.move(str(wins), str(wins.parent / f"windows-stale-{int(time.time())}"))
            wins.mkdir()
        print(f"[{cid}] using closing-line tree {closing.name}", flush=True)
    else:
        orch.run_parallel_toc_passes_1_2(cid, max_workers=workers)
        orch.run_toc_tree_and_qc(cid)
        orch.add_frame_nodes_and_anchor(cid)
    orch.run_ingest(cid)
    orch.SEGMENTED_DIR = orch.INBOX / "segmented"
    shutil.copyfile(work / f"{cid}.toc.md", orch.SEGMENTED_DIR / f"{cid}.toc.md")

    reseg = orch.run_resegment_and_qc(cid, max_workers=workers)

    # re-append the footnote apparatus verbatim, then stamp + strict verify
    rbody, rfoot = split_footnotes(reseg.read_text(encoding="utf-8"))
    if rfoot:
        print(f"[{cid}] WARNING: reseg output carried footnote lines; replacing with source apparatus")
    reseg.write_text(rbody + ("\n" + foot if foot else ""), encoding="utf-8")
    orch.run_block_ids(cid)

    shutil.copyfile(reseg, orch.TOC_INGEST_DIR / f"{cid}.toc.md")
    print(f"[{cid}] DONE in {time.time() - t0:.0f}s -> {orch.TOC_INGEST_DIR / f'{cid}.toc.md'}", flush=True)


if __name__ == "__main__":
    ids = [a for a in sys.argv[1:] if not a.startswith("--workers=")]
    workers = next((int(a.split("=")[1]) for a in sys.argv[1:] if a.startswith("--workers=")), 8)
    failed = []
    for cid in ids:
        try:
            run_one(cid, workers)
        except Exception as e:  # keep going with the other files
            print(f"[{cid}] FAILED: {e}", flush=True)
            failed.append(cid)
    print(f"\nFinished. Failed: {failed or 'none'}")
