#!/usr/bin/env python3
"""Assemble the verse-mode anchored tree for Ka_3CDJ from TOC-Ka_3CDJ/range-*.txt.

Lines in the range files:  `V <n> [[ctx]]`  or  `F <I|II title|a|b|b.1|b.2> [[ctx]]`.
Tree: I / II frame, `1. གཞུང་དོན།` (same anchor as stanza 1), `1.n ཚིགས་བཅད་<ordinal>།`
(vault precedent Ch_3CCW), then a / b frame nodes.
"""

import re
import sys
from pathlib import Path

TOC = Path(__file__).resolve().parent / "TOC-Ka_3CDJ"

UNITS = ["", "གཅིག", "གཉིས", "གསུམ", "བཞི", "ལྔ", "དྲུག", "བདུན", "བརྒྱད", "དགུ"]
TENS = {2: ("ཉི་ཤུ", "ཉེར"), 3: ("སུམ་ཅུ", "སོ"), 4: ("བཞི་བཅུ", "ཞེ"), 5: ("ལྔ་བཅུ", "ང"),
        6: ("དྲུག་ཅུ", "རེ"), 7: ("བདུན་ཅུ", "དོན"), 8: ("བརྒྱད་ཅུ", "གྱ"), 9: ("དགུ་བཅུ", "གོ")}
TEENS = {10: "བཅུ", 11: "བཅུ་གཅིག", 12: "བཅུ་གཉིས", 13: "བཅུ་གསུམ", 14: "བཅུ་བཞི",
         15: "བཅོ་ལྔ", 16: "བཅུ་དྲུག", 17: "བཅུ་བདུན", 18: "བཅོ་བརྒྱད", 19: "བཅུ་དགུ"}


def ordinal(n: int) -> str:
    if n == 1:
        return "དང་པོ"
    if n < 10:
        word = UNITS[n]
    elif n < 20:
        word = TEENS[n]
    else:
        t, u = divmod(n, 10)
        word = TENS[t][0] if u == 0 else f"{TENS[t][1]}་{UNITS[u]}"
    return f"{word}་པ"


def main():
    verses, front, back = {}, [], []
    for f in sorted(TOC.glob("range-*.txt")):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^V\s+(\d+)\s+(\[\[.*?\]\])", line)
            if m:
                verses.setdefault(int(m.group(1)), m.group(2))
                continue
            m = re.match(r"^F\s+(III|II|I|a|b\.1|b\.2|b)\b\s*(.*?)\s*(\[\[.*?\]\])", line)
            if m:
                key, title, ctx = m.groups()
                (front if key in ("I", "II", "III") else back).append((key, title, ctx))
    missing = [n for n in range(1, 98) if n not in verses]
    if missing:
        print("MISSING stanzas:", missing)

    out = ["---", "source: Ka_3CDJ", "skill: commentary-toc-extract", "stage: toc-tree-anchored",
           "mode: verses", "root: 1-SOURCES/Text/Sh_3CDA.md", "date: 2026-10-13",
           "model: claude-opus (rerun, human-reference style)", "---", "",
           "## དཀར་ཆག / Table of Contents"]
    for key, title, ctx in front:
        name = "ཀླད་ཀྱི་དོན།" if key == "I" else (title.rstrip("།") + "།")
        out.append(f"* {key}. {name} {ctx}")
    first = verses[min(verses)]
    out.append(f"* 1. གཞུང་དོན། {first}")
    for n in sorted(verses):
        out.append(f"   * 1.{n} ཚིགས་བཅད་{ordinal(n)}། {verses[n]}")
    names = {"a": "བསྔོ་བ།", "b": "མཇུག་བྱང།", "b.1": "མཛད་བྱང།", "b.2": "འགྱུར་བྱང།"}
    for key, _, ctx in back:
        indent = "   " if "." in key else ""
        out.append(f"{indent}* {key + ('.' if '.' not in key else '')} {names[key]} {ctx}")
    (TOC / "toc-tree-Ka_3CDJ.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {TOC / 'toc-tree-Ka_3CDJ.md'}: {len(verses)} stanzas, front {len(front)}, back {len(back)}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
