"""Measure every claim in 0-INBOX/commentary-root-map.md against the texts.

Section A claims "<commentary/translation> X belongs to root R" (both in our corpus): for each,
the share of R's 4-syllable sequences found in X (a commentary quotes its root; a second
translation shares wording) and of X's found in R. Section B claims "X's root is outside our
corpus": listed for the pass-2 comparison. Writes map-check.json.

Run from the vault root:  venv\\Scripts\\python.exe -X utf8 0-INBOX\\temp\\text-relations\\check_map.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
MAP = VAULT / "0-INBOX/commentary-root-map.md"


def grams(f):
    t = (VAULT / "1-SOURCES/Text" / f).read_text(encoding="utf-8")
    t = re.sub(r"(?m)^\[\^\d+\]:.*$", "", t)
    t = re.sub(r"\[\^\d+\]", "", t)
    t = re.sub(r"(?m)^#.*$", "", t)
    s = re.findall(r"[ཀ-ྼ]+", t.replace("༌", "་"))
    return {tuple(s[k:k + 4]) for k in range(len(s) - 3)}


text = MAP.read_text(encoding="utf-8")
a_part, b_part = text.split("## B.", 1)
claims_a, root = [], None
for line in a_part.split("\n"):
    m = re.match(r"^### \[\[([^\]]+)\]\]", line)
    if m:
        root = m.group(1) + ".md"
        continue
    m = re.match(r"^- \*\*(\w+)\*\* \[\[([^\]]+)\]\]\s*(.*)$", line)
    if m and root:
        claims_a.append({"root": root, "kind": m.group(1), "file": m.group(2) + ".md",
                         "note": m.group(3).strip()})
claims_b = []
for line in b_part.split("\n"):
    m = re.match(r"^\| \[\[([^\]]+)\]\] \| (.*?) \| (.*?) \|$", line)
    if m:
        claims_b.append({"file": m.group(1) + ".md", "title": m.group(2), "comments_on": m.group(3)})

cache = {}
g = lambda f: cache.setdefault(f, grams(f))
for c in claims_a:
    r, x = g(c["root"]), g(c["file"])
    n = len(r & x)
    c["root_found_in_it"] = round(n / len(r), 2) if r else 0.0
    c["it_found_in_root"] = round(n / len(x), 2) if x else 0.0
(HERE / "map-check.json").write_text(json.dumps({"section_a": claims_a, "section_b": claims_b},
                                                ensure_ascii=False, indent=1), encoding="utf-8")
print(f"section A: {len(claims_a)} claims · section B: {len(claims_b)} claims")
for c in sorted(claims_a, key=lambda c: c["root_found_in_it"]):
    print(f"  {c['root']:<12} <- {c['kind']:<11} {c['file']:<12} root found in it {c['root_found_in_it']:>4.0%}"
          f"  it found in root {c['it_found_in_root']:>4.0%}  {c['note'][:50]}")
