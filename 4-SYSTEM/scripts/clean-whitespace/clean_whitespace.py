#!/usr/bin/env python3
"""Clean odd spaces and line breaks out of source files.

What the linters warn about (durchen.odd_characters) is fixed here:

- a space-like character other than the plain space (U+00A0 no-break space,
  U+2000…U+200A, U+202F, U+205F, U+3000, U+1680) becomes a plain space;
- an invisible character (U+200B zero-width space, U+200C, U+200D, U+2060,
  U+FEFF, U+00AD soft hyphen) is removed;
- a line break other than \\n (U+2028, U+2029, U+0085, vertical tab, form feed,
  a lone \\r) becomes a line break in the file's own style (\\r\\n or \\n);
- a run of spaces that this created collapses to one space.

Nothing else changes: plain spaces that were already there stay as they are,
and the file keeps its line endings.

Dry run by default: lists every change with its line. --write saves.

    python 4-SYSTEM/scripts/clean-whitespace/clean_whitespace.py 1-SOURCES/Text/Sh_3CD6.md
    python 4-SYSTEM/scripts/clean-whitespace/clean_whitespace.py 1-SOURCES/Text/*.md --write
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "parser-root-text"))
import durchen  # noqa: E402  (SPACE_LIKE, INVISIBLE, LINE_BREAKS, char_name)

ODD = durchen.SPACE_LIKE + durchen.INVISIBLE
# a run of plain/space-like characters that contains at least one space-like one
SPACE_RUN = re.compile(f"[ {re.escape(durchen.SPACE_LIKE)}]*[{re.escape(durchen.SPACE_LIKE)}][ {re.escape(durchen.SPACE_LIKE)}]*")
INVISIBLE_RE = re.compile(f"[{re.escape(durchen.INVISIBLE)}]")
BREAK_RE = re.compile(f"[{re.escape(durchen.LINE_BREAKS)}]|\\r(?!\\n)")


def clean_line(line):
    """The line with odd spaces made plain (runs collapsed to one) and invisible characters removed."""
    line = INVISIBLE_RE.sub("", line)
    return SPACE_RUN.sub(" ", line)


def clean(text):
    """Return (new_text, changes): changes are (line number, what, before, after)."""
    nl = "\r\n" if "\r\n" in text[:2000] else "\n"
    body = text.replace("\r\n", "\n")
    breaks = BREAK_RE.findall(body)
    body = BREAK_RE.sub("\n", body)
    changes = [(0, f"{len(breaks)} odd line break(s) → newline", "", "")] if breaks else []
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if any(c in ODD for c in line):
            new = clean_line(line)
            what = ", ".join(sorted({durchen.char_name(c) for c in line if c in ODD}))
            changes.append((i + 1, what, line, new))
            lines[i] = new
    return nl.join(lines), changes


def _show(s, width=40):
    s = "".join(f"⟦U+{ord(c):04X}⟧" if c in ODD else c for c in s)
    return s if len(s) <= 2 * width else s[:width] + " … " + s[-width:]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--write", action="store_true", help="save the cleaned files")
    a = ap.parse_args()
    # expand glob patterns here too: Windows shells pass them through unexpanded
    files = [p for f in a.files for p in (sorted(Path().glob(str(f))) if any(c in str(f) for c in "*?[") else [f])]
    touched = 0
    for path in files:
        with open(path, encoding="utf-8", newline="") as f:
            text = f.read()
        new, changes = clean(text)
        if not changes:
            continue
        touched += 1
        print(f"{path}: {len(changes)} line(s)")
        for n, what, before, after in changes:
            print(f"  line {n}: {what}")
            if before:
                print(f"    before: {_show(before)}")
                print(f"    after : {_show(after)}")
        if a.write:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(new)
    print(f"{len(files)} file(s) checked, {touched} to clean" + ("" if a.write else " · dry run (--write to save)"))


if __name__ == "__main__":
    sys.exit(main())
