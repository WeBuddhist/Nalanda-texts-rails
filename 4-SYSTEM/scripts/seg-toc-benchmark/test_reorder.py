#!/usr/bin/env python3
"""
Test of toc_tree_ingest's reorder-to-text-order.

For a real anchored tree whose order is right, simulate a tree that announces some
parts in a different order than the text treats them: pick parents with ≥ 3 children,
shuffle their child subtrees and renumber them in the shuffled order. Ingest the
shuffled tree. The headings must land exactly where the original tree puts them, with
the same titles and block splits, and:
  default               each heading keeps the ID the SHUFFLED tree gave it
                        (the announced order: གཉིས་པ་… stays …-2-0 wherever it sits)
  --renumber-reordered  IDs renumbered in text order = identical to the original

    python3 test_reorder.py <anchored-tree.md> <segmented.md> [--parents N] [--seed S]
"""
import json
import random
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ING = Path(__file__).resolve().parents[2] / 'Skills/seg-toc-lib/toc_tree_ingest.py'
LINE = re.compile(r'^(\s*)\*\s+(\S+?)\.?\s(.*)$')


def parse(md):
    out = []
    for l in md.splitlines():
        m = LINE.match(l)
        if m and re.fullmatch(r'\d+(?:\.\d+)*|[IVX]+(?:\.\d+)*|[a-z](?:\.\d+)*', m.group(2).rstrip('.')):
            out.append([m.group(2).rstrip('.'), m.group(3), m.group(2).rstrip('.')])
    return out


def render(items):
    lines = ['## དཀར་ཆག / Table of Contents', '']
    for i, rest, *_ in items:
        d = i.count('.')
        lines.append('   ' * d + f'* {i}{"." if d == 0 else ""} {rest}')
    return '\n'.join(lines) + '\n'


def shuffle(items, parent, rng):
    """Shuffle the child subtrees of `parent` and renumber them in the new order."""
    pre = parent + '.' if parent else ''
    is_kid = lambda i: (i.startswith(pre) and i[len(pre):].isdigit()) if parent else i.isdigit()
    idx = [k for k, it in enumerate(items) if is_kid(it[0])]
    if len(idx) < 3:
        return items, None
    blocks = []
    for a, b in zip(idx, idx[1:] + [None]):
        end = b
        if end is None:  # last child: its subtree runs while ids start with it
            end = a + 1
            while end < len(items) and items[end][0].startswith(items[a][0] + '.'):
                end += 1
        blocks.append(items[a:end])
    tail_start = idx[-1] + len(blocks[-1])
    order = list(range(len(blocks)))
    while order == sorted(order):
        rng.shuffle(order)
    new = []
    for n, j in enumerate(order, 1):
        old = blocks[j][0][0]
        nid = pre + str(n)
        for i, rest, orig in blocks[j]:
            new.append([nid + i[len(old):], rest, orig])
    return items[:idx[0]] + new + items[tail_start:], [blocks[j][0][0] for j in order]


def ingest(tree_md, seg, tmp, name, extra=()):
    t, js, out = tmp / f'{name}.md', tmp / f'{name}.json', tmp / f'{name}.out.md'
    t.write_text(tree_md, encoding='utf-8')
    shutil.copy(seg, out)
    subprocess.run(['python3', ING, 'parse', '--input', t, '--out', js], capture_output=True, check=True)
    r = subprocess.run(['python3', ING, 'ingest', '--tree', js, '--commentary', out, '--split-frame-nodes',
                        *extra],
                       capture_output=True, text=True)
    return out.read_text(encoding='utf-8'), r.stdout


def main():
    tree, seg = Path(sys.argv[1]), Path(sys.argv[2])
    nparents = int(sys.argv[sys.argv.index('--parents') + 1]) if '--parents' in sys.argv else 3
    seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 1
    rng = random.Random(seed)
    items = parse(tree.read_text(encoding='utf-8'))
    ids = [it[0] for it in items if it[0][0].isdigit()]
    cands = [None] if sum(1 for i in ids if i.isdigit()) >= 3 else []
    cands += [p for p in ids if sum(1 for i in ids if i.startswith(p + '.') and i[len(p) + 1:].isdigit()) >= 3]
    rng.shuffle(cands)
    picked = cands[:nparents]
    shuffled = items
    for p in picked:
        shuffled, order = shuffle(shuffled, p, rng)
        if order is None:
            continue
        print(f'shuffled children of {p or "(top)"}: text order kept, tree now announces {order}')
    renumber = '--renumber-reordered' in sys.argv
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        a, _ = ingest(render(items), seg, tmp, 'orig')
        b, log = ingest(render(shuffled), seg, tmp, 'shuf', ['--renumber-reordered'] if renumber else [])
    print('\n'.join(l for l in log.splitlines() if 'REORDER' in l or 'under ' in l or 'Not found' in l))
    if not renumber:
        # expected: the original output with every heading ID relabelled to the shuffled tree's ID
        to_bid = lambda i: '-'.join(i.split('.')) + '-0'
        idmap = {to_bid(orig): to_bid(i) for i, _, orig in shuffled}
        a = re.sub(r'^(#+ .*\^)(\S+)$', lambda m: m.group(1) + idmap.get(m.group(2), m.group(2)),
                   a, flags=re.M)
    ok = a == b
    what = 'IDs renumbered in text order' if renumber else 'announced IDs kept'
    print(f'PASS — same placement as the original-order ingest, {what}' if ok else f'FAIL — output differs ({what})')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
