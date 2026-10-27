"""Put the missing space before a witness bracket in footnote definitions.

The convention is "lemma ༼witness༽ variant": a space before "༼". About 200 definitions came from
the intake files without it, always right after a shad ("…ནོ། །༼སྣར། པེ།༽ …"). Only footnote
definition lines ("[^…]: …") are touched; the body never is.

Dry run by default; --write saves. Accepts file paths or glob patterns.
Usage:  python space_before_witness.py "1-SOURCES/Commentaries/*.md" "1-SOURCES/Text/*.md" [--write]
"""
import glob
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
DEF_RE = re.compile(r"^(\[\^\w+\]:[ \t]?)(.*)$")
NO_SPACE = re.compile(r"(?<=\S)༼")


def fix_text(text):
    out, n = [], 0
    for line in text.splitlines(keepends=True):
        body = line.rstrip("\r\n")
        m = DEF_RE.match(body)
        if m:
            new, k = NO_SPACE.subn(" ༼", m.group(2))
            if k:
                n += k
                line = m.group(1) + new + line[len(body):]
        out.append(line)
    return "".join(out), n


if __name__ == "__main__":
    write = "--write" in sys.argv
    paths = sorted({p for a in sys.argv[1:] if not a.startswith("--") for p in glob.glob(a)})
    total = files = 0
    for p in paths:
        text = Path(p).read_text(encoding="utf-8")
        new, n = fix_text(text)
        if n:
            files += 1
            total += n
            print(f"  {Path(p).stem}: {n}")
            if write:
                Path(p).write_text(new, encoding="utf-8", newline="")
    print(f"{total} bracket(s) in {files} file(s) {'fixed' if write else 'to fix'}")
