#!/usr/bin/env python3
"""
Error listing for one prediction against the gold: missed / spurious block boundaries
and displaced headings, each with the surrounding text, to explain what the score shows.

    python3 diff_report.py <gold.md> <pred.md> [--ctx 25] [--max 200]
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bench_lib import parse  # noqa: E402
from score import match_headings  # noqa: E402


def show(stream, off, ctx):
    return f'…{stream[max(0, off - ctx):off]} ‖ {stream[off:off + ctx]}…'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('gold')
    ap.add_argument('pred')
    ap.add_argument('--ctx', type=int, default=25)
    ap.add_argument('--max', type=int, default=200)
    a = ap.parse_args()
    g = parse(Path(a.gold).read_text(encoding='utf-8'))
    p = parse(Path(a.pred).read_text(encoding='utf-8'))
    s = g.stream
    gb, pb = g.boundaries, p.boundaries
    missed = sorted(gb - pb)
    spurious = sorted(pb - gb)
    print(f'## Missed boundaries (in gold, not in prediction): {len(missed)}')
    for o in missed[:a.max]:
        print(f'- @{o}: {show(s, o, a.ctx)}')
    print(f'\n## Spurious boundaries (in prediction, not in gold): {len(spurious)}')
    for o in spurious[:a.max]:
        print(f'- @{o}: {show(s, o, a.ctx)}')
    gs = [h for h in g.headings if not h.editorial]
    pairs = match_headings(gs, p.headings)
    print('\n## Displaced headings (title matched, position differs)')
    for gi, pi in pairs.items():
        gh, ph = gs[gi], p.headings[pi]
        if gh.offset != ph.offset:
            print(f'- {gh.block_id} → pred {ph.block_id}: Δ={ph.offset - gh.offset:+d}  '
                  f'gold at {show(s, gh.offset, a.ctx)}  |  pred at {show(s, ph.offset, a.ctx)}')
    print('\n## ID / level mismatches')
    for gi, pi in pairs.items():
        gh, ph = gs[gi], p.headings[pi]
        if gh.block_id != ph.block_id or gh.level != ph.level:
            print(f'- gold {gh.block_id} (h{gh.level}) vs pred {ph.block_id} (h{ph.level}): {gh.title}')


if __name__ == '__main__':
    main()
