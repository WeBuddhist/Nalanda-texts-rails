"""Akutobhayā (Na_3CAp_): one node per MMK chapter from the commentary's own closers
(`X བརྟག་པ་ཞེས་བྱ་བ་སྟེ། རབ་ཏུ་བྱེད་པ་ N པའོ`), titled `X བརྟག་པ` (precedent Bu_3CCC, Ch_3CCb_)."""
import re
from pathlib import Path
U = Path("0-INBOX/temp/PIPE-Na_3CAp_/Na_3CAp_.units.md").read_text(encoding="utf-8").split("\n")
canon = lambda s: re.sub(r"\[\^\d+\]", "", s).replace("༌", "་")
closers = []
for i, l in enumerate(U):
    c = canon(l)
    if re.search(r"རབ་ཏུ་བྱེད་པ་[^།]*?(པའོ|པོའོ|པ་སྟེ་ཐ་མའོ)།", c) and ("ཞེས་བྱ་བ་སྟེ" in c or c.startswith("རབ་ཏུ་བྱེད་པ")):
        j = i if "ཞེས་བྱ་བ་སྟེ" in c else i - 1
        t = re.findall(r"([^།]*?བརྟག་པ)་?ཞེས་བྱ་བ་སྟེ", canon(U[j]))[-1]
        closers.append((i, t.strip("་ ")))
assert len(closers) == 27, len(closers)

def first_text(i):
    while not U[i].strip():
        i += 1
    return i

nodes = [("I.", "ཀླད་ཀྱི་དོན།", first_text(24))]
starts = [35] + [first_text(c + 1) for c, _ in closers[:-1]]   # line 36 = MMK homage verse
for k, ((_, title), s) in enumerate(zip(closers, starts), 1):
    nodes.append((f"{k}.", title, s))
b = next(i for i in range(closers[-1][0] + 1, len(U)) if "ག་ལས་འཇིགས་མེད་ཅེས་བྱ་བ" in U[i])
tr = next(i for i in range(b + 1, len(U)) if U[i].strip())
nodes += [("b.", "མཇུག་བྱང།", b), ("   b.1", "མཛད་བྱང།", b), ("   b.2", "འགྱུར་བྱང།", tr)]
out = ["---", "source: Na_3CAp_", "skill: commentary-toc-extract", "stage: toc-tree-anchored",
       "mode: top (chapter closers, root Na_3CAk_)", "date: 2026-10-13", "---", "", "## དཀར་ཆག / Table of Contents"]
for nid, title, i in nodes:
    ind = "   " if nid.startswith(" ") else ""
    anc = U[i].strip()
    j = i + 1
    while len(anc) < 40 and j < len(U):          # short opener (`འདིར་སྨྲས་པ།`): extend with the next line
        if U[j].strip():
            anc += " " + U[j].strip()
        j += 1
    out.append(f"{ind}* {nid.strip()} {title} [[{anc[:70]}]]")
    print(nid.strip(), i + 1, title)
Path("0-INBOX/temp/TOC-Na_3CAp_/toc-tree-Na_3CAp_.md").write_text("\n".join(out) + "\n", encoding="utf-8")
