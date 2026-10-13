#!/usr/bin/env python3
"""run_batch_pipeline.py, but the resegment QC step uses qc_check_batched.py (repair sent in
batches) — for files whose single QC repair call overflows the model's output limit.
Finished reseg windows are reused. Usage (vault root): python -u -X utf8 THIS.py ID"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_batch_pipeline as rb

orch = rb.orch


def run_resegment_and_qc(cid, max_workers=8):
    orch.run_cmd([sys.executable, "-u", "-X", "utf8", str(orch.TEMP_DIR / "run_parallel_reseg.py"),
                  cid, str(max_workers)])
    reseg = orch.RESEG_DIR / f"{cid}.reseg.md"
    orch.run_cmd([sys.executable, "-u", "-X", "utf8", str(orch.TEMP_DIR / "qc_check_batched.py"),
                  str(reseg), "--commentary-id", cid])
    return reseg


orch.run_resegment_and_qc = run_resegment_and_qc
rb.run_one(sys.argv[1], 8)
