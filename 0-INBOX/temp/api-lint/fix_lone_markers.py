#!/usr/bin/env python3
"""Merge footnote markers that segmentation left alone in their own block.

    py -3 0-INBOX/temp/api-lint/fix_lone_markers.py <file.toc.md> [more files ...]

A block that holds only `[^n] ^ID` has no text, so the parser writes a segment with no lines and
the API rejects the edition. In the original (0-INBOX/commentary/<stem>.md) such a marker sits at
the end of the text before it. For each lone-marker block this script appends the marker to the
previous content block (before its ID) and removes the empty block, after checking that the
original has the marker right after that block's last words. If the original does not agree, the
block is left alone and reported. Run the linter and parser afterwards.
"""
import re
import sys
from pathlib import Path

ORIG = Path(__file__).resolve().parents[3] / "0-INBOX" / "commentary"
strip = lambda t: re.sub(r"\[\^\w+\]|\s", "", t)


def fix(path):
    stem = path.name[:-len(".toc.md")]
    orig = [strip_l for strip_l in (ORIG / f"{stem}.md").read_text(encoding="utf-8").split("\n")]
    L = path.read_bytes().decode("utf-8").split("\n")
    out, moved, kept = [], 0, []
    k = 0
    while k < len(L):
        m = re.fullmatch(r"(\[\^\w+\])\s*\^[\w-]+\r?", L[k])
        if m and out:
            j = len(out) - 1
            while j >= 0 and not out[j].strip():
                j -= 1
            pm = re.search(r" \^([\w-]+)(\r?)$", out[j])
            tail = strip(out[j][:pm.start()])[-12:] if pm else ""
            marker = m.group(1)
            agrees = bool(pm) and not out[j].startswith("#") and any(
                marker in ol and re.search(re.escape(tail) + r"\W*" + re.escape(marker), re.sub(r"\s+", "", ol))
                for ol in orig)
            if agrees:
                out[j] = out[j][:pm.start()] + marker + " ^" + pm.group(1) + pm.group(2)
                moved += 1
                k += 2 if k + 1 < len(L) and not L[k + 1].strip() else 1
                while len(out) > 1 and not out[-1].strip() and not out[-2].strip():
                    out.pop()
                continue
            kept.append(L[k].strip())
        out.append(L[k])
        k += 1
    if moved:
        path.write_bytes("\n".join(out).encode("utf-8"))
    return moved, kept


if __name__ == "__main__":
    for a in sys.argv[1:]:
        p = Path(a)
        moved, kept = fix(p)
        print(f"{p.name}: moved {moved}" + (f", left {len(kept)}: {kept[:3]}" if kept else ""))
