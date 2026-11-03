"""Check every text's body in 1-SOURCES against the file it was made from: by default the raw
intake file as received (0-INBOX/root/<id>.md or 0-INBOX/commentary/<id>.md), or with
--baseline docx the first extraction from the .docx (0-INBOX/Nalanda_docx/<pandita>/works/<id>.md).
Report original text that is missing or changed, and long passages that were added.

Both sides are reduced to their letters (whitespace, punctuation, footnote markers and definitions,
block IDs, link markup and heading marks removed; Unicode NFD) and split into syllables. Text of the
original that is DELETED or REPLACED is reported, and so is text the vault ADDED when it runs to
--min-insert syllables or more (shorter additions are the vault's editorial headings).

Read-only. Usage:  python audit_body_text.py [--out <tsv>] [--min-insert N] [ids ...]
"""
import argparse
import difflib
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
VAULT = Path(__file__).resolve().parents[3]
DEF_LINE = re.compile(r"^\[\^\w+\]:.*$", re.M)
MARK = re.compile(r"\[\^\w+\]")
ID_RE = re.compile(r"(?<!\S)\^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*(?=\s|$)")
LINK_RE = re.compile(r"!\[\[[^\]]*\]\]|\[\[[^\]|]*\|([^\]]*)\]\]|\[\[([^\]]*)\]\]")
FM = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.S)
SPLIT = re.compile(r"[\s་༌།༎༑༔༼༽༄༅༆༈༒​ *#>_|\-]+")


def syllables(text, heading_flags=None):
    """Syllables of the body. If heading_flags is a list, it receives one bool per syllable:
    True when the syllable comes from a markdown heading line."""
    text = FM.sub("", text)
    text = DEF_LINE.sub("", text)
    text = MARK.sub("", text)
    text = ID_RE.sub("", text)
    text = LINK_RE.sub(lambda m: m.group(1) or m.group(2) or "", text)
    text = unicodedata.normalize("NFD", text)
    out = []
    for line in text.splitlines():
        syl = [s for s in SPLIT.split(line) if s]
        out += syl
        if heading_flags is not None:
            heading_flags += [line.lstrip().startswith("#")] * len(syl)
    return out


def originals(baseline):
    """raw: the files as received (0-INBOX/root, 0-INBOX/commentary); docx: the first extraction
    from the Nalanda .docx files (0-INBOX/Nalanda_docx/<pandita>/works)."""
    if baseline == "docx":
        return {p.stem: p for p in (VAULT / "0-INBOX" / "Nalanda_docx").glob("*/works/*.md")}
    out = {}
    for folder in ("root", "commentary"):
        out.update({p.stem: p for p in (VAULT / "0-INBOX" / folder).glob("*.md")})
    return out


def audit(stem, path, orig, min_insert):
    head = []
    a, b = syllables(orig.read_text(encoding="utf-8")), syllables(path.read_text(encoding="utf-8"), head)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        # added headings are the vault's editorial structure; added body text is text the original lacks
        added_body = sum(not h for h in head[j1:j2])
        if op in ("delete", "replace") or (op == "insert" and added_body >= min_insert):
            out.append((op, i1, "་".join(a[max(0, i1 - 4):i1]), "་".join(a[i1:i2]), "་".join(b[j1:j2])))
    return len(a), out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--out", default=str(VAULT / "0-INBOX" / "body-audit.tsv"))
    ap.add_argument("--min-insert", type=int, default=15,
                    help="report added text of at least this many syllables (default 15)")
    ap.add_argument("--baseline", choices=("raw", "docx"), default="raw",
                    help="compare with the raw intake files (default) or the .docx extraction")
    args = ap.parse_args()
    orig = originals(args.baseline)
    paths = sorted(list((VAULT / "1-SOURCES" / "Text").glob("*.md")) +
                   list((VAULT / "1-SOURCES" / "Commentaries").glob("*.md")))
    if args.ids:
        paths = [p for p in paths if p.stem in set(args.ids)]
    rows, clean = [], 0
    for n, p in enumerate(paths, 1):
        if p.stem not in orig:
            rows.append((p.stem, "no-original", "", "", "", ""))
            continue
        total, diffs = audit(p.stem, p, orig[p.stem], args.min_insert)
        clean += not diffs
        for op, pos, ctx, old, new in diffs:
            rows.append((p.stem, op, str(pos), ctx, old, new))
        if n % 50 == 0:
            print(f"  {n}/{len(paths)}", flush=True)
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        f.write("id\top\tsyllable\tbefore\toriginal\tnow\n")
        for r in rows:
            f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
    print(f"{len(paths)} texts · {clean} identical to the original · {len(rows)} differences -> {args.out}")


if __name__ == "__main__":
    main()
