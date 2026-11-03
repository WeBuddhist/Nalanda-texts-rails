#!/usr/bin/env python3
"""Tail of run_batch_pipeline.run_one after reseg+QC: re-append footnotes, stamp IDs, verify, copy."""
import sys, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_pipeline_orchestrator as orch
from run_batch_pipeline import split_footnotes

def tail(cid):
    foot = (orch.TEMP_DIR / f"PIPE-{cid}" / f"{cid}.footnotes.md").read_text(encoding="utf-8")
    reseg = orch.RESEG_DIR / f"{cid}.reseg.md"
    rbody, rfoot = split_footnotes(reseg.read_text(encoding="utf-8"))
    if rfoot:
        print(f"[{cid}] reseg carried footnote lines; replacing with source apparatus")
    reseg.write_text(rbody + ("\n" + foot if foot else ""), encoding="utf-8")
    orch.run_block_ids(cid)
    orch.TOC_INGEST_DIR.mkdir(parents=True, exist_ok=True)
    import shutil
    shutil.copyfile(reseg, orch.TOC_INGEST_DIR / f"{cid}.toc.md")
    print(f"[{cid}] -> {orch.TOC_INGEST_DIR / f'{cid}.toc.md'}")

if __name__ == "__main__":
    for c in sys.argv[1:]:
        try: tail(c)
        except Exception as e: print(f"[{c}] FAILED: {e}")
