#!/usr/bin/env python3
"""
Variation across repeated runs of the same pipeline on one commentary.

    python3 repeat_report.py <fid> <ref-ver> <run-ver> [<run-ver> …]   [--stage 4-final]

Prints: per metric mean / sd / min / max over the runs (ref shown alongside);
boundary stability (gold boundaries found in all / some / no runs; spurious boundaries
by how many runs produce them); heading stability (titles and placements per run).
Writes a markdown report to 0-INBOX/bench8/repeat-<fid>.md.
"""
import json
import statistics as st
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bench_lib import parse, norm_title  # noqa
from score import score  # noqa

cfg = json.load(open('0-INBOX/bench8/config.json'))
args = [a for a in sys.argv[1:] if not a.startswith('--')]
stage = sys.argv[sys.argv.index('--stage') + 1] if '--stage' in sys.argv else '4-final'
fid, ref, runs = args[0], args[1], args[2:]
f = cfg['files'][fid]
gold = parse(Path(f['gold']).read_text(encoding='utf-8'))

metrics = [
    ('composite', lambda s: s['composite']),
    ('boundary F1', lambda s: s['seg']['boundary_exact']['F1']),
    ('boundary P', lambda s: s['seg']['boundary_exact']['P']),
    ('boundary R', lambda s: s['seg']['boundary_exact']['R']),
    ('block exact', lambda s: s['seg']['block_exact_rate']),
    ('pred blocks', lambda s: s['seg']['pred_blocks']),
    ('heading F1', lambda s: s['toc']['heading_title']['F1']),
    ('heading placed ×R', lambda s: s['toc']['placement_exact_rate'] * s['toc']['heading_title']['R']),
    ('heading ID ×R', lambda s: s['toc']['id_exact_rate'] * s['toc']['heading_title']['R']),
    ('frame placed', lambda s: s['toc']['editorial_placement_exact'] or 0),
]


def path(v):
    return f'0-INBOX/bench8/{fid}/{v}/{stage}.md'


S = {v: score(f['gold'], path(v)) for v in [ref] + runs}
D = {v: parse(Path(path(v)).read_text(encoding='utf-8')) for v in [ref] + runs}
out = []
P = out.append

P(f'# Repeat-run variation — {fid}, stage `{stage}`, {len(runs)} independent runs (ref {ref})\n')
P('| metric | ' + ref + ' | ' + ' | '.join(runs) + ' | mean | sd | min | max |')
P('|---|' + '---:|' * (len(runs) + 5))
for name, fn in metrics:
    xs = [fn(S[v]) for v in runs]
    sd = st.pstdev(xs) if len(xs) > 1 else 0
    fmt = (lambda x: f'{x:.0f}') if name == 'pred blocks' else (lambda x: f'{x:.3f}')
    P(f'| {name} | {fmt(fn(S[ref]))} | ' + ' | '.join(fmt(x) for x in xs)
      + f' | {fmt(st.mean(xs))} | {sd:.3f} | {fmt(min(xs))} | {fmt(max(xs))} |')

# boundary stability
gb = gold.boundaries
cnt = Counter()
for v in runs:
    for b in D[v].boundaries:
        cnt[b] += 1
n = len(runs)
gold_all = sum(1 for b in gb if cnt[b] == n)
gold_some = sum(1 for b in gb if 0 < cnt[b] < n)
gold_none = sum(1 for b in gb if cnt[b] == 0)
spur = {b: c for b, c in cnt.items() if b not in gb}
P(f'\n## Boundary stability ({len(gb)} gold boundaries)\n')
P(f'- found in **all** {n} runs: {gold_all} ({gold_all / len(gb):.0%})')
P(f'- found in **some** runs only: {gold_some} ({gold_some / len(gb):.0%})')
P(f'- found in **no** run: {gold_none} ({gold_none / len(gb):.0%})')
P(f'- spurious (not in gold): {len(spur)} distinct, of which in all runs {sum(1 for c in spur.values() if c == n)}, '
  f'in some {sum(1 for c in spur.values() if 0 < c < n)}')
P(f'- pairwise boundary agreement between runs (Jaccard): ' + ', '.join(
    f'{a}/{b} {len(D[a].boundaries & D[b].boundaries) / len(D[a].boundaries | D[b].boundaries):.3f}'
    for i, a in enumerate(runs) for b in runs[i + 1:]))

# flip map: where do runs disagree (both gold-and-not)
flips = sorted(b for b, c in cnt.items() if 0 < c < n)
if flips:
    P('\n### Boundaries that flip between runs\n')
    P('| offset | in gold | runs with it | text before ‖ after |')
    P('|---:|:--:|:--:|---|')
    for b in flips:
        ctx = gold.stream[max(0, b - 25):b] + ' ‖ ' + gold.stream[b:b + 25]
        P(f'| {b} | {"✓" if b in gb else "✗"} | {cnt[b]}/{n} | {ctx} |')

# heading stability
P('\n## Heading stability\n')
hk = Counter()
for v in runs:
    for h in D[v].headings:
        hk[(norm_title(h.title), h.offset)] += 1
gold_h = {(norm_title(h.title), h.offset) for h in gold.headings}
P(f'- distinct (title, position) headings over all runs: {len(hk)}; in all runs {sum(1 for c in hk.values() if c == n)}; '
  f'in some {sum(1 for c in hk.values() if c < n)}')
P(f'- gold headings reproduced (title+position) in all runs: {sum(1 for k in gold_h if hk[k] == n)}/{len(gold_h)}; '
  f'in some: {sum(1 for k in gold_h if 0 < hk[k] < n)}; never: {sum(1 for k in gold_h if hk[k] == 0)}')
unst = sorted((k for k, c in hk.items() if c < n), key=lambda k: k[1])
if unst:
    P('\n### Headings that differ between runs\n')
    P('| position | title | runs | in gold |')
    P('|---:|---|:--:|:--:|')
    for k in unst:
        title = next(h.title for v in runs for h in D[v].headings if (norm_title(h.title), h.offset) == k)
        P(f'| {k[1]} | {title} | {hk[k]}/{n} | {"✓" if k in gold_h else ""} |')

rep = '\n'.join(out) + '\n'
Path(f'0-INBOX/bench8/repeat-{fid}.md').write_text(rep, encoding='utf-8')
print(rep)
