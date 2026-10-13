#!/usr/bin/env python3
"""Step 1 (commentary-segment --units) for one id, with optional --root.
Same as run_step1.process_text, plus the skill's recommended --root flag.
Usage: python -X utf8 0-INBOX/temp/seg_with_root.py ID [ROOT.md]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_step1

cid = sys.argv[1]
root = sys.argv[2] if len(sys.argv) > 2 else None
if root:
    orig_run = run_step1.subprocess.run

    def run(cmd, *a, **kw):
        if str(run_step1.SEG_SCRIPT) in map(str, cmd):
            cmd = list(cmd) + ["--root", root]
        return orig_run(cmd, *a, **kw)

    run_step1.subprocess.run = run
_, passed, info = run_step1.process_text(cid)
print(info if isinstance(info, str) else info["res_stdout"] + "\n" + info["verify_summary"][-400:])
print(f"[{cid}] PASSED={passed}")
