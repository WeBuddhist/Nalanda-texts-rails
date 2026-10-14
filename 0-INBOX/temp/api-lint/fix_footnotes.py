#!/usr/bin/env python3
"""Rejoin footnote definitions that segmentation split across lines.

    py -3 0-INBOX/temp/api-lint/fix_footnotes.py <segmented.toc.md> [more files ...] [--dry]

For each file the original is 0-INBOX/commentary/<stem>.md (stem = file name before .toc.md).
In the footnote section (from the first `[^n]:` line to the end) the script joins every
definition with the lines split off it and drops block IDs left on them (` ^b-3`). Then each
definition is checked against the original's: if the two differ only in whitespace, the
original's wording is used; if the text differs in any other way, or a label is missing or
extra, the file is NOT written and the problem is printed. The body above the footnote
section is never touched. Run the linter afterwards.
"""
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
DEF = re.compile(r"\[\^(\w+)\]:")
ORIGINALS = VAULT / "0-INBOX" / "commentary"


def fix(path, dry=False):
    stem = path.name[:-len(".toc.md")] if path.name.endswith(".toc.md") else path.stem
    orig_path = ORIGINALS / f"{stem}.md"
    if not orig_path.exists():
        return f"no original {orig_path.relative_to(VAULT)}"
    raw = path.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = [l.rstrip("\r") for l in raw.split("\n")]
    first = next((k for k, l in enumerate(lines) if DEF.match(l)), None)
    if first is None:
        return "no footnote section"

    defs = {}
    order = []
    for l in lines[first:]:
        s = l.strip()
        if not s:
            continue
        m = re.search(r"\s\^[\w-]+$", s)
        if m:
            s = s[:m.start()].rstrip()
        d = DEF.match(s)
        if d:
            order.append(d.group(1))
            defs[d.group(1)] = s
        elif order:
            defs[order[-1]] = (defs[order[-1]] + " " + s).rstrip()

    orig = {}
    for l in orig_path.read_text(encoding="utf-8").split("\n"):
        d = DEF.match(l)
        if d:
            orig[d.group(1)] = l.rstrip("\r").rstrip()
    squash = lambda t: re.sub(r"\s+", "", t)
    problems = []
    if set(defs) != set(orig):
        problems.append(f"labels differ: missing {sorted(set(orig) - set(defs))[:5]}, extra {sorted(set(defs) - set(orig))[:5]}")
    fixed = []
    for label in order:
        if label not in orig:
            continue
        if squash(defs[label]) != squash(orig[label]):
            problems.append(f"[^{label}] text differs from the original")
        else:
            if defs[label] != orig[label]:
                fixed.append(label)
            defs[label] = orig[label]
    if problems:
        return "NOT written: " + "; ".join(problems[:5])

    body = nl.join(lines[:first]).rstrip()
    new = body + nl + nl + nl.join(defs[l] for l in order) + nl
    changed = new != raw
    if changed and not dry:
        path.write_bytes(new.encode("utf-8"))
    return f"{'would fix' if dry else 'fixed'}: {len(order)} footnotes" if changed else "already fine"


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--dry"]
    for a in args:
        p = Path(a)
        print(f"{p.name}: {fix(p, dry='--dry' in sys.argv)}")
