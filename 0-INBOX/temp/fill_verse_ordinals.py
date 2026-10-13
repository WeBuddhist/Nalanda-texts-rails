#!/usr/bin/env python3
"""Replace `ཚིགས་བཅད་{k}` placeholders in a toc-tree with Tibetan ordinal titles
(vault precedent Ch_3CCW: ཚིགས་བཅད་དང་པོ། … ཉེར་གཅིག་པ། …).
Usage: python -X utf8 fill_verse_ordinals.py TREE.md
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble_ka_3cdj_tree import ordinal as base_ordinal, UNITS, TEENS


def ordinal(n: int) -> str:
    if n < 100:
        return base_ordinal(n)
    if n == 100:
        return "བརྒྱ་པ"
    r = n - 100
    word = UNITS[r] if r < 10 else TEENS[r] if r < 20 else base_ordinal(r)[:-2]
    return f"བརྒྱ་དང་{word}་པ"


p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")
t, n = re.subn(r"ཚིགས་བཅད་\{?(\d+)\}?(?=།)",lambda m: "ཚིགས་བཅད་" + ordinal(int(m.group(1))), t)
p.write_text(t, encoding="utf-8")
print(f"filled {n} placeholders; left: {len(re.findall(r'\{\d+\}', t))}")
