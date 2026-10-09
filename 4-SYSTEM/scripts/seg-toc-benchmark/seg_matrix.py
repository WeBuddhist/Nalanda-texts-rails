#!/usr/bin/env python3
"""
Deterministic segmentation check across every gold file (no LLM calls).

For each gold commentary: build the merged input, run segment_commentary.py in the
given configurations, and score segmentation against the gold.

    python3 seg_matrix.py --gold-dir <dir> --root <root.md> --out <table.md>
        [--old <old segment_commentary.py>] [--new <new segment_commentary.py>]
"""
import argparse, glob, os, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from score import score  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('--gold-dir', required=True)
ap.add_argument('--root')
ap.add_argument('--old')
ap.add_argument('--new', default='4-SYSTEM/Skills/commentary-segment/scripts/segment_commentary.py')
ap.add_argument('--work', default='0-INBOX/bench/heldout')
ap.add_argument('--out')
a = ap.parse_args()
here = Path(__file__).parent
os.makedirs(a.work, exist_ok=True)
configs = []
if a.old:
    configs.append(('v0 structural', a.old, ['--structural']))
configs.append(('structural', a.new, ['--structural']))
configs.append(('units', a.new, ['--units']))
if a.root:
    configs.append(('units+root', a.new, ['--units', '--root', a.root]))
rows = ['| file | gold blocks | ' + ' | '.join(f'{c[0]} F1 / exact' for c in configs) + ' |',
        '|---|---|' + '---|' * len(configs)]
tot = {c[0]: [] for c in configs}
for g in sorted(glob.glob(os.path.join(a.gold_dir, '*.md'))):
    name = os.path.basename(g)[:-3]
    inp = f'{a.work}/{name}.in.md'
    r = subprocess.run(['python3', str(here / 'make_input.py'), g, inp], capture_output=True, text=True)
    if r.returncode:
        continue
    cells, nb = [], None
    for tag, script, flags in configs:
        out = f"{a.work}/{name}.{tag.replace(' ', '_').replace('+', '_')}.md"
        r = subprocess.run(['python3', script, inp, out] + flags, capture_output=True, text=True)
        if r.returncode:
            cells.append('ERR'); continue
        s = score(g, out)['seg']
        nb = s['gold_blocks']
        tot[tag].append((s['boundary_exact']['F1'], s['block_exact_rate'], nb))
        cells.append(f"{s['boundary_exact']['F1']:.2f} / {s['block_exact_rate']:.2f}")
    rows.append(f'| {name} | {nb} | ' + ' | '.join(cells) + ' |')
def wavg(v, i):
    w = sum(x[2] for x in v)
    return sum(x[i] * x[2] for x in v) / w if w else 0
rows.append('| **block-weighted mean** | | ' + ' | '.join(
    f"**{wavg(tot[c[0]],0):.2f} / {wavg(tot[c[0]],1):.2f}**" for c in configs) + ' |')
txt = '\n'.join(rows)
print(txt)
if a.out:
    Path(a.out).write_text(txt + '\n', encoding='utf-8')
