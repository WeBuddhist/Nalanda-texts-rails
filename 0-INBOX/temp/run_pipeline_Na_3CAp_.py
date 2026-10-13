#!/usr/bin/env python3
"""run_batch_pipeline.py for Na_3CAp_ with one post-ingest fix: MMK 24.1 and 25.1 open
identically, so chapter 25 is anchored on its verse (pāda 3 differs) and its heading is then
moved up one block, above its lead-in `འདིར་སྨྲས་པ།`. Text is untouched (heading move only)."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_batch_pipeline as rb

orch = rb.orch
_ingest = orch.run_ingest


def run_ingest(cid):
    out = _ingest(cid)
    for f in (orch.SEGMENTED_DIR / f"{cid}.toc.md", orch.TOC_INGEST_DIR / f"{cid}.toc.md"):
        blocks = f.read_text(encoding="utf-8").split("\n\n")
        i = next(k for k, b in enumerate(blocks) if b.startswith("## མྱ་ངན་ལས་འདས་པ་བརྟག་པ། ^25-0"))
        assert blocks[i - 1].strip() == "འདིར་སྨྲས་པ།", blocks[i - 1][:40]
        blocks[i - 1], blocks[i] = blocks[i], blocks[i - 1]
        f.write_text("\n\n".join(blocks), encoding="utf-8")
        print(f"[{cid}] moved ^25-0 above its lead-in in {f.name}")
    return out


orch.run_ingest = run_ingest
rb.run_one("Na_3CAp_", 8)
