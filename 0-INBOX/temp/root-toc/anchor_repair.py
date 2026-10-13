#!/usr/bin/env python3
"""Repair the anchors of a root-text TOC tree that the ingest cannot find because the
copied words differ from the text only in editorial marks: a footnote marker the model
left out (text "ངག་གི༌[^157]ཚིག་སྟེ།", anchor "ངག་གི༌ཚིག་སྟེ།") or a non-breaking tsheg
"༌" for "་". Root-text side only — the shared toc_tree_ingest.py is not changed.

    py -X utf8 0-INBOX/temp/root-toc/anchor_repair.py <anchored-tree.md> <prepared.md>

For each node whose anchor the ingest would not find (its matching: spaces and shads
dropped; the whole anchor or its first half), the anchor is looked up again with
footnote markers removed and "༌" read as "་" on both sides, after the previous node's
place. A match → the anchor is rewritten with the text's own words at that place
(markers included). The tree is changed in place; the first original is kept as
<tree>.orig.md. Prints: fixed N, unresolved [ids].
"""
import re, shutil, sys
from pathlib import Path

DROP = re.compile(r"[\s།༎༑༔]")
FN = re.compile(r"\[\^\d+\]")
LINE = re.compile(r"^(\s*\*\s+(\S+?)\.?\s+.*?)\s*\[\[(.*)\]\]\s*$")


def canon(s):
    return DROP.sub("", s)


def loose_map(text):
    """Text with footnote markers, spaces and shads removed and ༌ as ་, plus for each kept
    char its index in text."""
    out, idx, i = [], [], 0
    while i < len(text):
        m = FN.match(text, i)
        if m:
            i = m.end()
            continue
        ch = text[i]
        if not DROP.match(ch):
            out.append("་" if ch == "༌" else ch)
            idx.append(i)
        i += 1
    return "".join(out), idx


def body_text(path):
    t = Path(path).read_text(encoding="utf-8").replace("\r\n", "\n")
    if t.startswith("---\n"):
        t = t[t.index("\n---\n", 4) + 5:]
    t = re.split(r"(?m)^\[\^\d+\]:", t)[0]                 # footnote definitions
    return "\n".join(l for l in t.split("\n") if not l.lstrip().startswith("#"))


def found_by_ingest(stream, anchor):
    a = canon(anchor)
    return bool(a) and (a in stream or a[:max(12, len(a) // 2)] in stream)


def repair(tree_path, text_path):
    tree_path = Path(tree_path)
    text = body_text(text_path)
    stream = canon(text)
    loose, idx = loose_map(text)
    lines = tree_path.read_text(encoding="utf-8").split("\n")
    fixed, unresolved, pos = 0, [], 0
    for k, l in enumerate(lines):
        m = LINE.match(l)
        if not m:
            continue
        head, nid, anchor = m.group(1), m.group(2), m.group(3)
        if anchor in ("", "?") or not re.match(r"^\d", nid):
            continue
        la, _ = loose_map(anchor)
        if found_by_ingest(stream, anchor):
            j = loose.find(la, pos)
            pos = j + 1 if j >= 0 else pos
            continue
        j = loose.find(la, pos) if la else -1
        if j < 0:
            unresolved.append(nid)
            continue
        start, end = idx[j], idx[j + len(la) - 1] + 1
        # carry a footnote marker that directly follows the last character
        fm = FN.match(text, end)
        end = fm.end() if fm else end
        words = re.sub(r"\s+", " ", text[start:end]).strip()
        lines[k] = f"{head} [[{words}]]"
        fixed += 1
        pos = j + 1
    if fixed:
        orig = tree_path.with_suffix(".orig.md")
        if not orig.exists():
            shutil.copyfile(tree_path, orig)
        tree_path.write_text("\n".join(lines), encoding="utf-8")
    return fixed, unresolved


if __name__ == "__main__":
    f, u = repair(sys.argv[1], sys.argv[2])
    print(f"fixed {f}, unresolved {u}")
