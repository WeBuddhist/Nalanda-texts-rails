#!/usr/bin/env python3
"""qc_check.py with the LLM repair sent in batches of flagged blocks.

A file with many flags (Ka_3CDZ: 175) makes one repair reply overflow max_output_tokens on
every retry. This wrapper keeps qc_check.py's prompt, validation, integrity check and report,
and only splits `call_llm_repair` into batches whose ops are concatenated (all ops refer to
the same original block numbers). Same CLI as qc_check.py.
"""
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(VAULT / "4-SYSTEM" / "Skills" / "commentary-resegment" / "scripts"))
import qc_check  # noqa: E402

BATCH = 30
_one_call = qc_check.call_llm_repair


def call_llm_repair(client, model, issues, blocks, fallback_model=""):
    ops = []
    for i in range(0, len(issues), BATCH):
        part = issues[i:i + BATCH]
        print(f"  batch {i // BATCH + 1}: {len(part)} flag(s)", flush=True)
        ops += _one_call(client, model, part, blocks, fallback_model)
    return ops


qc_check.call_llm_repair = call_llm_repair
if __name__ == "__main__":
    qc_check.main()
