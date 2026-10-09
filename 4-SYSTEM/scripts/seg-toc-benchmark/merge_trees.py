#!/usr/bin/env python3
"""
Combine the numbered nodes of one anchored tree with the frame nodes of another.

    python3 merge_trees.py <numbered-tree.md> <frame-tree.md> <out.md>

- numbered tree: every `* 1. …` line (and any `II…` front-matter lines it has, as the
  verse-headings prompt may emit them in `top` mode)
- frame tree:    every frame line (`I.`, `II.`, `a.`, `b.1` …) — its front-matter `II…`
  lines are dropped when the numbered tree already has its own `II…`.

Output order: front frame (I, II …) → numbered → back frame (a, b …).
"""
import re
import sys
from pathlib import Path

LINE = re.compile(r'^\s*\*\s+([0-9IVXa-z][0-9.IVX]*)\.?\s')


def lines(p):
    out = []
    for l in Path(p).read_text(encoding='utf-8').splitlines():
        m = LINE.match(l)
        if m:
            out.append((m.group(1).rstrip('.').split('.')[0], l))
    return out


def kind(top):
    if top.isdigit():
        return 'num'
    if re.fullmatch(r'[IVX]+', top):
        return 'front'
    return 'back'


def main(num_p, frame_p, out_p):
    num = lines(num_p)
    frame = lines(frame_p)
    num_front = [l for t, l in num if kind(t) == 'front' and t != 'I']   # I. always comes from the frame tree
    num_body = [l for t, l in num if kind(t) == 'num']
    has_ii = any(t != 'I' for t, l in num if kind(t) == 'front')
    front = [l for t, l in frame if kind(t) == 'front' and (t == 'I' or not has_ii)]
    back = [l for t, l in frame if kind(t) == 'back']
    body = front + num_front + num_body + back
    Path(out_p).write_text('## དཀར་ཆག / Table of Contents\n\n' + '\n'.join(body) + '\n', encoding='utf-8')
    print(f'{out_p}: {len(front)} front frame + {len(num_front)} own II + {len(num_body)} numbered + {len(back)} back frame')


if __name__ == '__main__':
    main(*sys.argv[1:4])
