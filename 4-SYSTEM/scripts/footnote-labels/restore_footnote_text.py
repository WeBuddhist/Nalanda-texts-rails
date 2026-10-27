"""Remove block IDs that the block-ID step stamped inside footnote definitions, restoring each
damaged definition's text from the raw intake file (0-INBOX/commentary/<id>.md).

A definition is damaged when its text holds a block ID (" ^b-10 ", " ^a-4") — the 2026-10-14
block-ID step treated parts of long footnote definitions as back-matter blocks, and also put a
space after "། །" where it cut them — or when its letters match a raw definition but its spacing
does not (a cut that left no ID). The current label ([^dN] / [^nN]) is kept; only the text after
"]: " is replaced, and only by a raw definition whose letters (whitespace and IDs ignored) are
identical. Anything without such a match is reported and left alone.

Dry run by default; --write saves.  Usage:  python restore_footnote_text.py <id> [<id> ...] [--write]
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
sys.path.insert(0, str(VAULT / "4-SYSTEM" / "scripts" / "parser-commentary"))
import durchen  # noqa: E402  (normalize_spaces, shared with the parser and linter)

DEF_RE = re.compile(r"^(\[\^\w+\]:[ \t]?)(.*)$")
ID_IN_TEXT = re.compile(r"(?<!\S)\^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*(?=\s|$)")


def letters(s):
    return re.sub(r"\s+", "", ID_IN_TEXT.sub("", s))


def raw_defs(stem):
    text = (VAULT / "0-INBOX" / "commentary" / f"{stem}.md").read_text(encoding="utf-8")
    out = {}
    for line in text.splitlines():
        m = DEF_RE.match(line)
        if m:
            out.setdefault(letters(m.group(2)), []).append(durchen.normalize_spaces(m.group(2)).rstrip())
    return out


def fix(stem, write):
    path = VAULT / "1-SOURCES" / "Commentaries" / f"{stem}.md"
    raw = raw_defs(stem)
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    fixed, unmatched = 0, []
    for i, line in enumerate(lines):
        body = line.rstrip("\r\n")
        m = DEF_RE.match(body)
        if not m:
            continue
        cands = set(raw.get(letters(m.group(2)), []))
        damaged = ID_IN_TEXT.search(m.group(2))
        # a cut that left no ID still left a space after "། །" ("…ནོ། ། དེ" for "…ནོ། །དེ")
        if not damaged and not (len(cands) == 1 and m.group(2).rstrip() not in cands):
            continue
        if len(cands) != 1:
            unmatched.append((i + 1, body[:100], len(cands)))
            continue
        new = m.group(1) + cands.pop()
        print(f"  line {i + 1}: {body[:110]}")
        print(f"        -> {new[:110]}")
        lines[i] = new + line[len(body):]
        fixed += 1
    for ln, b, n in unmatched:
        print(f"  UNMATCHED line {ln} ({n} raw candidates): {b}")
    print(f"{stem}: {fixed} definition(s) {'restored' if write else 'to restore'}, {len(unmatched)} unmatched")
    if write and fixed:
        path.write_text("".join(lines), encoding="utf-8", newline="")
    return fixed, len(unmatched)


if __name__ == "__main__":
    write = "--write" in sys.argv
    for stem in [a for a in sys.argv[1:] if not a.startswith("--")]:
        fix(stem, write)
