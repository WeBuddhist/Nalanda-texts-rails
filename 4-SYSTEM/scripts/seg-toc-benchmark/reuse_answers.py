#!/usr/bin/env python3
"""
Copy LLM answers from one run to another wherever the prompt is byte-identical.

    python3 reuse_answers.py <fid> <from-ver> <to-ver>

Re-segmentation windows (claude/window-*.prompt.md → .response.json) and QC calls
(qc-calls/call-*.prompt.md → .response.txt). Prints what was reused and what still
needs a fresh answer. Unlike the global prompt-hash cache, this pins the source run,
so a repeat keeps its own answers and never borrows another run's.
"""
import shutil, sys
from pathlib import Path
fid, src, dst = sys.argv[1:4]
T = Path('0-INBOX/temp')
reused = new = 0
for sub, rext in (('claude', '.response.json'), ('qc-calls', '.response.txt')):
    for p in sorted((T / f'RESEG-{fid}-{dst}' / sub).glob('*.prompt.md')):
        r = p.with_name(p.name.replace('.prompt.md', rext))
        if r.exists():
            continue
        q = T / f'RESEG-{fid}-{src}' / sub / p.name
        qr = q.with_name(q.name.replace('.prompt.md', rext))
        if q.exists() and qr.exists() and q.read_bytes() == p.read_bytes():
            shutil.copy(qr, r); reused += 1
        else:
            new += 1; print(f'{fid} {dst} needs answer: {p}')
print(f'{fid} {dst}: reused {reused}, new {new}')
