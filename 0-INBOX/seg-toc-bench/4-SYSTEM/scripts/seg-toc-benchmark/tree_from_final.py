#!/usr/bin/env python3
"""
Rebuild an anchored tree from a finished commentary's headings.

    python3 tree_from_final.py <final.md> <out-tree.md>

Every heading line (`### title ^1-2-0`, or `###### **title** ^…-0` below level 6)
becomes a tree node: its block ID gives the decimal ID (`^1-2-0` → `1.2`, `^b-1-0` →
`b.1`), and the first content after it (the next block that is not a heading or a
transclusion, body ID removed) gives the `[[context]]`. Ingesting the result into the
same segmented input puts every heading back where it was — so a run whose tree file
was not kept can still be re-run from its final file without asking a model again.
"""
import re
import sys
from pathlib import Path

HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*\^([0-9A-Za-z]+(?:-[0-9A-Za-z]+)*)-0\s*$")
BODY_ID_RE = re.compile(r"\s*\^[0-9A-Za-z]+(?:-[0-9A-Za-z]+)*\s*$")
CONTEXT_CHARS = 120


def blocks(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        text = text[end + 4:] if end > 0 else text
    return [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]


def main():
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    bs = blocks(src.read_text(encoding="utf-8"))
    lines = ["## དཀར་ཆག / Table of Contents", ""]
    for i, b in enumerate(bs):
        m = HEAD_RE.match(b)
        if not m:
            continue
        title = m.group(2).strip().strip("*").strip()
        did = m.group(3).replace("-", ".")
        ctx = next((BODY_ID_RE.sub("", c) for c in bs[i + 1:]
                    if not HEAD_RE.match(c) and not c.startswith("![[")), "?")
        ctx = " ".join(ctx.split())[:CONTEXT_CHARS]
        depth = did.count(".")
        lines.append(f"{'   ' * depth}* {did} {title} [[{ctx}]]")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{src}: {len(lines) - 2} nodes → {out}")


if __name__ == "__main__":
    main()
