#!/usr/bin/env python3
"""Build a chapter-level toc-tree from a commentary's own closing lines (no model).

For Indian commentaries in translation that have no sa bcad: every division ends
with a closing formula, and the next division starts right after it.

  --style gu   closers  "… X རྫོགས་སོ།། །།"              title = X
  --style ha   closers  "… ལས་ X ལེའུ (ཞེས་བྱ་བ) སྟེ N པའོ"  title = "X ལེའུ … N པ"

Output is the usual toc-tree markdown (`* N. title [[anchor]]`) for
toc_tree_ingest.py parse/ingest. Anchors are the opening text of each division
(cut mid-block with ingest --split-mid-block when a closer ends inside a block).
Frame nodes: I. (title / homage block) when the file opens with རྒྱ་གར་སྐད་དུ,
b. (colophon) when text follows the last closer.

Usage: python build_closing_tree.py UNITS.md OUT.md --style gu|ha [--id ID]
"""

import argparse
import re
from pathlib import Path

FN = re.compile(r"\[\^\d+\]")


def canon_map(s):
    """canonical text (no footnote refs, ༌→་) + index map canon→orig."""
    out, idx, i = [], [], 0
    while i < len(s):
        m = FN.match(s, i)
        if m:
            i = m.end()
            continue
        ch = "་" if s[i] == "༌" else s[i]
        out.append(ch)
        idx.append(i)
        i += 1
    idx.append(len(s))
    return "".join(out), idx


GU_RE = re.compile(r"([^།]*?)་?རྫོགས་སོ།།")
HA_RE = re.compile(r"([^།]*?ལེའུ(?:་ཞེས་བྱ(?:་བ)?)?་སྟེ་(?:སྐབས་)?[^།]{1,25}?པོ?)(?:འོ|འི་བཤད་པ)")
# "… ལས། སྐབས་དང་པོའི་འགྲེལ་པའོ།། །།"  (Haribhadra Vivṛti)
SKABS_RE = re.compile(r"([^།]*སྐབས་[^།]{1,20}?)འི་འགྲེལ་པའོ")
# "… དཀའ་འགྲེལ་ལས་ X བརྟག་པ་སྟེ། N པའོ"  (Kamalaśīla Tattvasaṃgraha-pañjikā)
BRTAG_RE = re.compile(r"དཀའ་འགྲེལ་ལས[། ]*([^།]*?བརྟགས?་པ་སྟེ)[། ]*([^།]{1,30}?པོ?)འོ")
# any division ending in a double shad pair "…།། །།" (fascicle / section ends)
DSHAD_RE = re.compile(r"([^།]+)།+ ?།།")
STYLES = {"gu": GU_RE, "ha": HA_RE, "skabs": SKABS_RE, "brtag": BRTAG_RE, "dshad": DSHAD_RE}


def title_of(clause, style):
    t = clause.strip().strip("་ ")
    if style == "ha":
        # "… སྣང་བ་ལས་ / ཚིགས་སུ་བཅད་པ་ལས་ X ལེའུ …": keep X onward
        lo = t.find("ལེའུ")
        k = max(t.rfind("བ་ལས་", 0, lo), t.rfind("པ་ལས་", 0, lo))
        if k >= 0:
            t = t[k + 5:]
    elif style == "dshad":
        t = re.sub(r"བཤད་ཟིན་ཏོ$", "བཤད་པ", t)
    else:
        t = re.sub(r"^(?:དེ་ལྟར་|དེ་ལྟ་བས་ན་|དེ་ནི་)", "", t)
    t = re.sub(r"་སྟེ$", "", t.strip("་ "))
    return t.strip("་ ") or "?"


def sentence_end(c, pos):
    """index just past the shad run that ends the sentence containing pos"""
    k = c.find("།", pos)
    if k < 0:
        return len(c)
    while k < len(c) and c[k] in "། ༎":
        k += 1
    return k


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("units")
    ap.add_argument("out")
    ap.add_argument("--style", choices=sorted(STYLES), required=True)
    ap.add_argument("--id", default="")
    a = ap.parse_args()

    blocks = [b.strip() for b in re.split(r"\n\s*\n", Path(a.units).read_text(encoding="utf-8"))]
    blocks = [b for b in blocks if b and not b.startswith("#") and not re.match(r"\[\^\d+\]:", b)]
    rx = STYLES[a.style]

    # (block index, char offset in block where the NEXT division starts, title)
    closers = []
    for bi, b in enumerate(blocks):
        c, idx = canon_map(b)
        for m in rx.finditer(c):
            if a.style == "brtag":
                clause = m.group(1) + "་" + m.group(2)
            else:
                clause = m.group(1)
                clause = clause[clause.rfind("།") + 1:] if "།" in clause else clause
            end = sentence_end(c, m.end() - 1)
            closers.append((bi, idx[end] if end < len(c) else len(b), title_of(clause, a.style)))

    def anchor_at(bi, off):
        # skip to real text: past the block end, or a block that is only footnote refs
        while bi < len(blocks) and (off >= len(blocks[bi].rstrip())
                                    or not canon_map(blocks[bi][off:])[0].strip("། ")):
            bi, off = bi + 1, 0
        if bi >= len(blocks):
            return None, None
        txt = blocks[bi][off:].lstrip()
        return bi, txt.split("\n")[0][:90]

    nodes = []  # (id, title, anchor)
    start_bi, start_off = 0, 0
    if "རྒྱ་གར་སྐད་དུ" in blocks[0]:
        nodes.append(("I", "ཀླད་ཀྱི་དོན།", blocks[0][:90]))
        start_bi = 1
    prev = (start_bi, start_off)
    n = 0
    for bi, off, title in closers:
        sbi, anc = anchor_at(*prev)
        nxt = (bi, off)
        if sbi is None or (sbi, 0) > (bi, off) or (sbi == bi and blocks[bi][:off].strip() == ""):
            prev = nxt
            continue
        n += 1
        nodes.append((str(n), title, anc))
        prev = nxt
    sbi, anc = anchor_at(*prev)
    if sbi is not None:
        nodes.append(("b", "མཇུག་བྱང།", anc))

    lines = ["---", f"source: {a.id}", "skill: commentary-toc-extract", "stage: toc-tree",
             f"method: closing-line chapters ({a.style}), no model", "---", "",
             "## དཀར་ཆག / Table of Contents"]
    for nid, title, anc in nodes:
        lines.append(f"* {nid}. {title} [[{anc}]]")
    Path(a.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{a.id}: {len(closers)} closers -> {sum(1 for x in nodes if x[0].isdigit())} chapter nodes"
          f"{' + I' if nodes and nodes[0][0] == 'I' else ''}{' + b' if nodes and nodes[-1][0] == 'b' else ''}")


if __name__ == "__main__":
    main()
