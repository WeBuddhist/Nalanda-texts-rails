#!/usr/bin/env python3
"""Compare variants with v1 on one stage: python3 compare.py <stage> v1 v1.1 [v1.2 …]"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from score import score
cfg = json.load(open('0-INBOX/bench8/config.json'))
stage, vers = sys.argv[1], sys.argv[2:]
keys = [('F1', lambda s: s['seg']['boundary_exact']['F1']), ('exact', lambda s: s['seg']['block_exact_rate']),
        ('place', lambda s: s['toc']['placement_exact_rate'] * s['toc']['heading_title']['R']),
        ('hF1', lambda s: s['toc']['heading_title']['F1']),
        ('frame', lambda s: s['toc']['editorial_placement_exact'] or 0), ('comp', lambda s: s['composite'])]
print(f"{'file':14s} " + ' '.join(f"{k:>6s}" for k, _ in keys) + '   per version')
tot = {v: [] for v in vers}
for fid, f in cfg['files'].items():
    rows = []
    for v in vers:
        p = Path(f'0-INBOX/bench8/{fid}/{v}/{stage}.md')
        s = score(f['gold'], str(p)); tot[v].append(s)
        rows.append(' '.join(f"{fn(s):6.3f}" for _, fn in keys))
    print(f"{fid:14s} " + '  |  '.join(rows))
for v in vers:
    import statistics as st
    print(f"{'MEAN '+v:14s} " + ' '.join(f"{st.mean(fn(s) for s in tot[v]):6.3f}" for _, fn in keys))
