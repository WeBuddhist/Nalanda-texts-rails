#!/usr/bin/env python3
"""Score root-text TOC trees out of 1 when there is no human gold.

    py -X utf8 score_root_toc.py <reference-tree> <tree> [--anchored] [--qc6 <qc-source report>]

The reference is the best tree we have (the Opus run, QC-clean against the text).
Score = 0.4 structure + 0.3 coverage + 0.3 anchors:
- structure: F1 of the top two levels, a node counting only when its title AND its
  parent's title match the reference (wrong nesting = wrong headings and IDs at ingest);
- coverage: F1 of all nodes by title, any level;
- anchors: share of nodes whose anchor was found in the text with no unresolved
  pointer ([[?]]) — 0 when the run produced no anchored tree.
Titles are compared after dropping shads, tshegs, spaces, leading ordinals and trailing
particles; difflib ratio >= 0.8 counts as a match. Frame nodes (I., II., a.) are ignored.
"""
import argparse, difflib, re, sys
from pathlib import Path

ORD = ("བཅུ་བདུན་པ|བཅུ་དྲུག་པ|བཅོ་ལྔ་པ|བཅུ་བཞི་པ|བཅུ་གསུམ་པ|བཅུ་གཉིས་པ|བཅུ་གཅིག་པ|བཅུ་པ|"
       "དགུ་པ|བརྒྱད་པ|བདུན་པ|དྲུག་པ|ལྔ་པ|བཞི་པ|གསུམ་པ|གཉིས་པ|དང་པོ")
LINE = re.compile(r"^(\s*)\*\s+(\d+(?:\.\d+)*)\.?\s+(.*?)\s*(\[\[.*\]\])?\s*$")


def norm(t):
    t = re.sub(r"\[\^\d+\]", "", t)
    t = re.sub(rf"^({ORD})་?", "", t.strip())
    t = re.sub(r"[་།\s༌]", "", t)
    return re.sub(r"(ནི|ལ|སྟེ|འོ)$", "", t)


def parse(path):
    nodes = []
    for l in Path(path).read_text(encoding="utf-8").splitlines():
        m = LINE.match(l)
        if m:
            num = m.group(2)
            parent = num.rsplit(".", 1)[0] if "." in num else None
            nodes.append({"num": num, "depth": num.count(".") + 1, "title": norm(m.group(3)),
                          "parent": parent, "anchor": m.group(4)})
    by = {n["num"]: n for n in nodes}
    for n in nodes:
        n["ptitle"] = by[n["parent"]]["title"] if n["parent"] in by else None
    return nodes


def same(a, b):
    return a == b or (a and b and difflib.SequenceMatcher(None, a, b).ratio() >= 0.8)


def f1(ref, got, key):
    used, tp = set(), 0
    for g in got:
        for i, r in enumerate(ref):
            if i not in used and key(r, g):
                used.add(i); tp += 1; break
    p = tp / len(got) if got else 0
    r = tp / len(ref) if ref else 0
    return (2 * p * r / (p + r) if p + r else 0), tp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ref"); ap.add_argument("tree"); ap.add_argument("--anchored", action="store_true"); ap.add_argument("--qc6")
    a = ap.parse_args()
    ref, got = parse(a.ref), parse(a.tree)
    top = lambda ns: [n for n in ns if n["depth"] <= 2]
    s_struct, _ = f1(top(ref), top(got), lambda r, g: same(r["title"], g["title"]) and
                     (same(r["ptitle"], g["ptitle"]) if r["ptitle"] or g["ptitle"] else True))
    s_cov, _ = f1(ref, got, lambda r, g: same(r["title"], g["title"]))
    if a.anchored and got:
        bad = sum(1 for n in got if not n["anchor"] or n["anchor"] == "[[?]]")
        if a.qc6 and Path(a.qc6).exists():   # anchors pass 6 could not find in the text
            bad = max(bad, Path(a.qc6).read_text(encoding="utf-8").count("unresolved anchor"))
        s_anc = max(0.0, 1 - bad / len(got))
    else:
        s_anc = 0.0
    score = 0.4 * s_struct + 0.3 * s_cov + 0.3 * s_anc
    print(f"nodes {len(got)} (ref {len(ref)}) | structure {s_struct:.3f} | coverage {s_cov:.3f} | "
          f"anchors {s_anc:.3f} | SCORE {score:.3f}")


if __name__ == "__main__":
    main()
