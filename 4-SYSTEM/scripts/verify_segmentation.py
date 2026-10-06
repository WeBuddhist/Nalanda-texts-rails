#!/usr/bin/env python3
"""Verify that a segmented text still carries exactly the content of its source.

Segmentation, TOC ingest and block-ID stamping may only add *structure*. This
script strips everything those steps are allowed to add, from both files, and
then requires the remaining text to be identical, character for character:

    stripped before comparing            kept and compared
    ─────────────────────────            ─────────────────
    YAML frontmatter                     every syllable and shad
    heading lines (# … ######)           footnote markers  [^12]
    trailing block IDs  ^1-2 / ^1-2-0    footnote definitions  [^12]: …
    transclusion lines  ![[…]]
    [Ed: …] editorial notes
    wikilink wrappers  [[#^1-0|term]] → term
    all whitespace and line breaks

Headings are dropped from both sides because TOC headings are editorial text
that is not in the source. Use --compare-headings to check them as text too.

It also checks the footnote apparatus on its own (same numbers, same text, each
definition at the start of its own line), and reports where every difference
sits — line number and context in both files.

    python3 4-SYSTEM/scripts/verify_segmentation.py SOURCE FINAL
    python3 4-SYSTEM/scripts/verify_segmentation.py SOURCE FINAL --report 0-INBOX/verify-<id>.md

Exit code: 0 = content identical, 1 = differences found, 2 = usage error.
"""

from __future__ import annotations

import argparse
import difflib
import re
import statistics
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
BLOCK_ID_RE = re.compile(r"\s\^[A-Za-z0-9][A-Za-z0-9-]*\s*$")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")
TRANSCLUSION_RE = re.compile(r"^\s*!\[\[.*\]\]\s*$")
ED_NOTE_RE = re.compile(r"\[Ed:[^\]]*\]")
WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]|]*)\|([^\]]*)\]\]")
FOOTNOTE_DEF_RE = re.compile(r"^\[\^(\w+)\]:(.*)$")
FOOTNOTE_REF_RE = re.compile(r"\[\^(\w+)\](?!:)")
SYLLABLE_RE = re.compile(r"[^་།༎\s]+")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("﻿", "")


def normalize(text: str, compare_headings: bool):
    """Return (content string, line number of each content char, heading list)."""
    m = FRONTMATTER_RE.match(text)
    offset_lines = m.group(0).count("\n") if m else 0
    if m:
        text = text[m.end():]
    chars, lines, headings = [], [], []
    for n, line in enumerate(text.split("\n"), start=offset_lines + 1):
        if TRANSCLUSION_RE.match(line):
            continue
        line = BLOCK_ID_RE.sub("", line)
        if HEADING_RE.match(line):
            title = line.lstrip().lstrip("#").strip()
            headings.append((n, title))
            if not compare_headings:
                continue
            line = title
        line = WIKILINK_RE.sub(r"\2", line)
        line = ED_NOTE_RE.sub("", line)
        for ch in line:
            if not ch.isspace():
                chars.append(ch)
                lines.append(n)
    return "".join(chars), lines, headings


def tokenize(s: str):
    """Split into syllable-sized tokens (each ends after its tsheg/shad run) for a fast diff."""
    tokens, starts, i = [], [], 0
    for m in re.finditer(r"[^་།༎]*[་།༎]+|[^་།༎]+$", s):
        if m.group(0):
            tokens.append(m.group(0))
            starts.append(m.start())
    return tokens, starts


def diff_content(a: str, b: str, a_lines, b_lines, context: int, max_diffs: int):
    ta, sa = tokenize(a)
    tb, sb = tokenize(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        a0 = sa[i1] if i1 < len(sa) else len(a)
        a1 = sa[i2] if i2 < len(sa) else len(a)
        b0 = sb[j1] if j1 < len(sb) else len(b)
        b1 = sb[j2] if j2 < len(sb) else len(b)
        out.append({
            "kind": {"replace": "changed", "delete": "missing in final",
                     "insert": "added in final"}[tag],
            "src_line": a_lines[min(a0, len(a_lines) - 1)] if a_lines else 0,
            "fin_line": b_lines[min(b0, len(b_lines) - 1)] if b_lines else 0,
            "src": a[a0:a1], "fin": b[b0:b1],
            "before": a[max(0, a0 - context):a0], "after": a[a1:a1 + context],
        })
        if len(out) >= max_diffs:
            break
    return out


def footnotes(text: str):
    defs, misplaced = {}, []
    for n, line in enumerate(text.split("\n"), start=1):
        m = FOOTNOTE_DEF_RE.match(line)
        rest = line
        if m:
            body = m.group(2)
            # a second definition glued onto this line is misplaced, not part of this one
            k = re.search(r"\[\^(\w+)\]:", body)
            if k:
                rest, body = body[k.start():], body[:k.start()]
            else:
                rest = ""
            defs[m.group(1)] = (n, re.sub(r"\s+", " ", BLOCK_ID_RE.sub("", body)).strip())
        for k in re.finditer(r"\[\^(\w+)\]:", rest):
            misplaced.append((n, k.group(1)))
    refs = FOOTNOTE_REF_RE.findall(re.sub(r"(?m)^\[\^\w+\]:.*$", "", text))
    return defs, misplaced, refs


def check_footnotes(src: str, fin: str):
    problems = []
    sdefs, _, srefs = footnotes(src)
    fdefs, fmis, frefs = footnotes(fin)
    for n, key in fmis:
        problems.append(f"final line {n}: definition [^{key}]: is not at the start of a line")
    for key in sorted(set(sdefs) - set(fdefs), key=_num):
        if not any(k == key for _, k in fmis):
            problems.append(f"[^{key}]: definition missing in final (source line {sdefs[key][0]})")
    for key in sorted(set(fdefs) - set(sdefs), key=_num):
        problems.append(f"[^{key}]: definition added in final (final line {fdefs[key][0]})")
    for key in sorted(set(sdefs) & set(fdefs), key=_num):
        if sdefs[key][1] != fdefs[key][1]:
            problems.append(f"[^{key}]: definition text differs (source line {sdefs[key][0]}, "
                            f"final line {fdefs[key][0]})")
    if sorted(srefs, key=_num) != sorted(frefs, key=_num):
        missing = sorted(set(srefs) - set(frefs), key=_num)
        added = sorted(set(frefs) - set(srefs), key=_num)
        problems.append(f"markers in text differ — source {len(srefs)}, final {len(frefs)}"
                        + (f"; missing {missing[:10]}" if missing else "")
                        + (f"; added {added[:10]}" if added else ""))
    return len(sdefs), len(fdefs), problems


def _num(k: str):
    return (0, int(k), "") if k.isdigit() else (1, 0, k)


def block_stats(text: str):
    text = FRONTMATTER_RE.sub("", text)
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    body = [b for b in blocks if not HEADING_RE.match(b) and not b.startswith("[^")
            and not TRANSCLUSION_RE.match(b)]
    sizes = [len(SYLLABLE_RE.findall(FOOTNOTE_REF_RE.sub("", b))) for b in body]
    ids = sum(1 for b in blocks if BLOCK_ID_RE.search(b.split("\n")[-1]))
    heads = sum(1 for b in blocks for ln in b.split("\n") if HEADING_RE.match(ln))
    if not sizes:
        return {"blocks": 0, "headings": heads, "ids": ids}
    return {"blocks": len(body), "headings": heads, "ids": ids, "min": min(sizes),
            "median": int(statistics.median(sizes)), "max": max(sizes)}


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("source", type=Path, help="the original source file")
    ap.add_argument("final", type=Path, help="the segmented file to verify")
    ap.add_argument("--compare-headings", action="store_true",
                    help="compare heading text too (default: headings are editorial and dropped)")
    ap.add_argument("--context", type=int, default=25, help="characters of context per difference")
    ap.add_argument("--max-diffs", type=int, default=30, help="stop listing after this many")
    ap.add_argument("--report", type=Path, help="also write a markdown report here (put it in 0-INBOX/)")
    args = ap.parse_args(argv)

    for p in (args.source, args.final):
        if not p.is_file():
            print(f"ERROR: not found: {p}", file=sys.stderr)
            return 2

    src_text, fin_text = read(args.source), read(args.final)
    a, a_lines, a_heads = normalize(src_text, args.compare_headings)
    b, b_lines, b_heads = normalize(fin_text, args.compare_headings)
    same = a == b
    diffs = [] if same else diff_content(a, b, a_lines, b_lines, args.context, args.max_diffs)
    n_sdef, n_fdef, fn_problems = check_footnotes(src_text, fin_text)
    ss, fs = block_stats(src_text), block_stats(fin_text)

    out = []
    out.append("# Segmentation content check\n")
    out.append(f"- Source: `{args.source}`")
    out.append(f"- Final:  `{args.final}`\n")
    out.append("| | Source | Final |\n|---|---|---|")
    out.append(f"| Content characters compared | {len(a):,} | {len(b):,} |")
    for key, label in (("blocks", "Text blocks"), ("headings", "Heading lines"), ("ids", "Block IDs")):
        out.append(f"| {label} | {ss.get(key, 0)} | {fs.get(key, 0)} |")
    if "median" in ss and "median" in fs:
        out.append(f"| Block size min / median / max (syllables) | {ss['min']} / {ss['median']} / {ss['max']}"
                   f" | {fs['min']} / {fs['median']} / {fs['max']} |")
    out.append(f"| Footnote definitions | {n_sdef} | {n_fdef} |\n")

    out.append(f"## Text content: {'✓ IDENTICAL' if same else f'✗ {len(diffs)} DIFFERENCE(S)'}\n")
    if same:
        out.append("Every syllable, shad and footnote marker of the source is present in the final "
                   "file, in the same order; only structure (headings, IDs, line breaks) differs.\n")
    for k, d in enumerate(diffs, 1):
        out.append(f"{k}. **{d['kind']}** — source line {d['src_line']}, final line {d['fin_line']}")
        out.append(f"   - source: …{d['before']}【{d['src']}】{d['after']}…")
        out.append(f"   - final:  …{d['before']}【{d['fin']}】{d['after']}…")
    if len(diffs) >= args.max_diffs:
        out.append(f"\n(listing stopped at {args.max_diffs}; raise --max-diffs to see more)")

    out.append(f"\n## Footnotes: {'✓ OK' if not fn_problems else f'✗ {len(fn_problems)} PROBLEM(S)'}\n")
    out.extend(f"- {p}" for p in fn_problems[:args.max_diffs])

    ok = same and not fn_problems
    out.append(f"\n## Result: {'✓ PASS' if ok else '✗ FAIL'}")
    report = "\n".join(out)
    print(report)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report + "\n", encoding="utf-8")
        print(f"\nReport written: {args.report}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
