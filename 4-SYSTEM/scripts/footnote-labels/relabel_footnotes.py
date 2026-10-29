#!/usr/bin/env python3
"""Relabel a source file's footnotes by type: [^dN] durchen, [^fN] footnote.

A footnote is a durchen when its note carries witness sigla in ༼…༽
("ལ་ ༼སྣར། པེ།༽ ལས་"); everything else is a footnote (editorial remarks,
source citations, colophons printed as footnotes). A label that is already dN
or fN keeps its type, unless --by-content asks to classify it again. The old
generic-note label nN is read as fN and relabelled.

Each type is numbered 1, 2, 3… in the order its markers appear in the text, so
a note that sat between durchens leaves the durchen series and the durchens
after it close up. Definitions never marked in the text keep their type and are
numbered after the marked ones. At the end of the file the definitions are
regrouped: d1…dK, a blank line, then f1…fM.

Only labels and the definitions' place change; note text and the text body are
untouched. Line endings are kept. A file is skipped (and reported) when a
marker has no definition or a label is defined twice.

Dry run by default: prints what would change. --write saves the files.

    python 4-SYSTEM/scripts/footnote-labels/relabel_footnotes.py 1-SOURCES/Text/Ch_3CCU.md
    python 4-SYSTEM/scripts/footnote-labels/relabel_footnotes.py 1-SOURCES/Text/*.md --write
    python 4-SYSTEM/scripts/footnote-labels/relabel_footnotes.py --ids Ch_3CCU Dh_3CF3 --write
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEF_RE = re.compile(r"^\[\^([^\]\s]+)\]:[ \t]?(.*?)\s*$")
MARK_RE = re.compile(r"\[\^([^\]\s]+)\]")
FM_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.S)
# Witness sigla as they open a ༼…༽ group. ཤྣར and a bare པ are typos of སྣར and པེ seen in the sources.
WITNESS_RE = re.compile(r"༼\s*(?:སྣར|པེ|ཅོ|སྡེ|གསེར་བྲིས|ཤྣར|པ)[\s་།༽]")
VAULT = Path(__file__).resolve().parents[3]


def note_kind(label, text, by_content=False):
    if not by_content:
        if re.fullmatch(r"d[1-9]\d*", label):
            return "d"
        if re.fullmatch(r"[fn][1-9]\d*", label):
            return "f"
    return "d" if WITNESS_RE.search(text) else "f"


def relabel(text, by_content=False):
    """Return (new_text, report) or raise ValueError when the file cannot be relabelled safely."""
    nl = "\r\n" if "\r\n" in text[:2000] else "\n"
    fm = FM_RE.match(text)
    head, body = (text[:fm.end()], text[fm.end():]) if fm else ("", text)
    lines = body.split(nl)

    defs, def_rows = {}, set()
    for i, line in enumerate(lines):
        m = DEF_RE.match(line)
        if m:
            if m.group(1) in defs:
                raise ValueError(f"[^{m.group(1)}] is defined twice")
            defs[m.group(1)] = m.group(2)
            def_rows.add(i)
    if not defs:
        return text, {"d": 0, "f": 0, "notes": [], "changed": False}

    marked = []
    for i, line in enumerate(lines):
        if i not in def_rows:
            marked += [m.group(1) for m in MARK_RE.finditer(line)]
    missing = sorted({l for l in marked if l not in defs})
    if missing:
        raise ValueError("marker(s) without a definition: " + ", ".join(f"[^{l}]" for l in missing))

    kinds = {l: note_kind(l, t, by_content) for l, t in defs.items()}
    mapping, count = {}, {"d": 0, "f": 0}
    for label in list(dict.fromkeys(marked)) + [l for l in defs if l not in marked]:
        if label not in mapping:
            k = kinds[label]
            count[k] += 1
            mapping[label] = f"{k}{count[k]}"

    def sub(m):
        return f"[^{mapping.get(m.group(1), m.group(1))}]"

    out = [MARK_RE.sub(sub, line) for i, line in enumerate(lines) if i not in def_rows]
    trailing_newline = out and out[-1] == ""
    while out and not out[-1].strip():
        out.pop()
    by_new = sorted(((mapping[l], t) for l, t in defs.items()),
                    key=lambda nt: (nt[0][0] != "d", int(nt[0][1:])))
    d_lines = [f"[^{n}]: {t}" for n, t in by_new if n[0] == "d"]
    f_lines = [f"[^{n}]: {t}" for n, t in by_new if n[0] == "f"]
    for group in (d_lines, f_lines):
        if group:
            out += [""] + group
    new = head + nl.join(out) + (nl if trailing_newline else "")
    notes = [(old, mapping[old], defs[old]) for old in defs if kinds[old] == "f"]
    return new, {"d": count["d"], "f": count["f"], "notes": notes, "changed": new != text}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", type=Path)
    ap.add_argument("--ids", nargs="+", default=[], help="root-text ids in 1-SOURCES/Text/")
    ap.add_argument("--write", action="store_true", help="save the relabelled files")
    ap.add_argument("--by-content", action="store_true",
                    help="classify every footnote by its text, even one already labelled dN / fN")
    a = ap.parse_args()
    files = list(a.files) + [VAULT / "1-SOURCES" / "Text" / f"{i}.md" for i in a.ids]
    if not files:
        ap.error("give files or --ids")
    changed = skipped = 0
    for path in files:
        with open(path, encoding="utf-8", newline="") as f:
            text = f.read()
        try:
            new, rep = relabel(text, a.by_content)
        except ValueError as exc:
            skipped += 1
            print(f"SKIP {path.stem}: {exc}")
            continue
        flag = "relabel" if rep["changed"] else "ok     "
        print(f"{flag} {path.stem}: {rep['d']} durchen · {rep['f']} footnote")
        for old, nw, t in rep["notes"]:
            print(f"        footnote [^{old}] → [^{nw}]: {t[:90]}")
        if rep["changed"]:
            changed += 1
            if a.write:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write(new)
    print(f"{len(files)} file(s): {changed} to relabel, {skipped} skipped"
          + ("" if a.write else " · dry run, nothing written (--write to save)"))


if __name__ == "__main__":
    sys.exit(main())
