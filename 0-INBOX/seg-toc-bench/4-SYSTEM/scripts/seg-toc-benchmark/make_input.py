#!/usr/bin/env python3
"""
Build a benchmark input from a human-processed (gold) commentary.

Removes every heading (sa bcad and editorial), every root-text transclusion and
every block ID, then merges all content into one continuous run — the state a raw
commentary is in before segmentation and TOC work. The '# title' line is kept as
plain text on its own line (raw files open with it). Frontmatter is kept verbatim.

    python3 make_input.py <gold.md> <out.md> [--keep-verse-lines]

--keep-verse-lines keeps the line breaks inside a stanza (default: merged too).
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bench_lib import FRONTMATTER_RE, ID_RE, parse, squeeze  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('gold')
    ap.add_argument('out')
    ap.add_argument('--keep-verse-lines', action='store_true')
    a = ap.parse_args()
    text = Path(a.gold).read_text(encoding='utf-8')
    m = FRONTMATTER_RE.match(text)
    fm = m.group(0) if m else ''
    doc = parse(text)
    title = doc.title_block.text if doc.title_block else ''
    parts = []
    for b in doc.blocks:
        if b is doc.title_block:
            continue
        t = b.text
        if not a.keep_verse_lines:
            t = re.sub(r'[ \t]*\n[ \t]*', ' ', t)
        parts.append(t.strip())
    merged = ' '.join(parts)
    out = fm + '\n' + (title + '\n\n' if title else '') + merged + '\n'
    # integrity: same squeezed content as the gold
    assert squeeze(title) + squeeze(merged) == doc.stream, 'content mismatch'
    Path(a.out).write_text(out, encoding='utf-8')
    print(f'wrote {a.out}: {len(doc.blocks)} gold blocks, {len(doc.headings)} gold headings, '
          f'{len(doc.stream)} squeezed chars')


if __name__ == '__main__':
    main()
