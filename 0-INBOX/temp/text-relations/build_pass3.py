"""Inputs for pass 3 (category of the texts that have no OpenPecha category).

Writes digests/cat-guide.md — our 13 categories, each with example titles that OpenPecha filed
under it (whole OpenPecha catalog, 746 texts, plus our matched texts) — and digests/cat-NN.md,
one entry per uncategorised text: title, pandita, file_type, measures, opening, closing.

Run from the vault root:  venv\\Scripts\\python.exe -X utf8 0-INBOX\\temp\\text-relations\\build_pass3.py
"""
import collections
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
sys.path.insert(0, str(HERE))
from category_review import DIRECT, OURS  # noqa: E402

BATCH = 23
EXAMPLES = 14
rel = json.loads((VAULT / "0-INBOX/text-relations.json").read_text(encoding="utf-8"))["texts"]
sig = json.loads((HERE / "signals.json").read_text(encoding="utf-8"))
catalog = json.loads((VAULT / "1-SOURCES/openpecha-v2-catalog.json").read_text(encoding="utf-8"))["texts"]

# examples per our category: our own matched texts first, then the rest of the OpenPecha catalog
ex = collections.defaultdict(list)
for f, e in rel.items():
    c = DIRECT.get((e.get("openpecha") or {}).get("category"))
    if c:
        ex[c].append(f"{re.sub(r'^[༄༅།\s]+', '', e['title'])} ({e['file_type']}, ours: {f[:-3]})")
for t in catalog:
    c = DIRECT.get(t.get("category"))
    if c and t.get("lang_tag") == "bo" and len(ex[c]) < 3 * EXAMPLES:
        ex[c].append(f"{t['title']} (OpenPecha)")
guide = ["# Our 13 categories, with examples of what is filed under each", "",
         "Examples are real titles: texts of ours that OpenPecha categorised (`ours:`), and other "
         "texts in the OpenPecha catalog (`OpenPecha`). They show the practice to follow.", ""]
for name, (cid, bo) in OURS.items():
    items = ex.get(name, [])
    ours_n = sum("ours:" in x for x in items)
    guide += [f"## {name} — {bo} — `{cid}`", "",
              f"({ours_n} of our texts already in it)", ""]
    guide += [f"- {x}" for x in (items[:EXAMPLES] if items else ["(no examples)"])] + [""]
(HERE / "digests" / "cat-guide.md").write_text("\n".join(guide), encoding="utf-8")

todo = [f for f in sig if f in rel and not DIRECT.get((rel[f].get("openpecha") or {}).get("category"))]
out = HERE / "digests"
for old in out.glob("cat-[0-9]*.md"):
    old.unlink()
entries = []
for f in todo:
    s, e = sig[f], rel[f]
    co = (e.get("commentary_of") or {}).get("file")
    co_cat = DIRECT.get(((rel.get(co) or {}).get("openpecha") or {}).get("category")) if co else None
    entries.append(
        f"## {f}\n"
        f"- title: {s['title']}\n"
        f"- pandita: {s['pandita']} · file_type: {e['file_type']} · syllables: {s['syllables']} · "
        f"metrical share {s['metrical_share']:.0%} · gloss markers {s['gloss_per_1000']}/1000\n"
        + (f"- commentary on: {co} — {rel[co]['title']}"
           + (f" (category: {co_cat})" if co_cat else "") + "\n" if co else "")
        + (f"- root it names (not in our corpus): {(e.get('context') or {}).get('named_root')}\n"
           if e["file_type"] == "commentary" and not co and (e.get("context") or {}).get("named_root") else "")
        + f"\nopening:\n```\n{s['opening']}\n```\n\nclosing:\n```\n{s['closing']}\n```\n")
for b in range(0, len(entries), BATCH):
    (out / f"cat-{b // BATCH + 1:02d}.md").write_text("\n".join(entries[b:b + BATCH]), encoding="utf-8")
print(f"{len(todo)} texts without a category · {len(range(0, len(entries), BATCH))} batches of {BATCH} · cat-guide.md "
      + str({k: len(v) for k, v in ex.items()}))
