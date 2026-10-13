"""Collect the context-reading results into context.json, which build.py merges into
0-INBOX/text-relations.json.

  results/pass1-*.json   file_type, confidence, evidence, named_root, root_candidates
  results/pass2-*.json   commentary_of (a file name in 1-SOURCES/Text, or null), with evidence
  results/pass3-*.json   category (one of our 13 backend categories, or null), with evidence

A later pass overrides an earlier one only for the keys it gives. Checks every key is one of
our files and every value is allowed; reports problems instead of guessing.

Run from the vault root:  venv\\Scripts\\python.exe -X utf8 0-INBOX\\temp\\text-relations\\merge_context.py
"""
import collections
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
cat = json.loads((VAULT / "1-SOURCES/text_catalog.json").read_text(encoding="utf-8"))
ours = {w["filename"] for p in cat["panditas"] for w in p["works"]}
TYPES = {"root-text", "commentary", None}

ctx, problems = {}, []
CATEGORIES = {"Prajñāpāramitā", "Liturgy", "Systematic Treatises", "Middle Way", "Tantras", "Miscellaneous",
              "Mind-only Treatises", "Logic", "Mind Trainings and Advices", "Discourses", "Monastic Rules",
              "Linguistics Treatises", "History and Stories", None}
for path in [p for n in (1, 2, 3) for p in sorted((HERE / "results").glob(f"pass{n}-*.json"))]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        problems.append(f"{path.name}: not valid JSON ({err})")
        continue
    for fn, d in data.items():
        if fn not in ours:
            problems.append(f"{path.name}: {fn} is not a file in 1-SOURCES/Text")
            continue
        if "file_type" in d and d["file_type"] not in TYPES:
            problems.append(f"{path.name}: {fn} file_type {d['file_type']!r}")
            continue
        if "category" in d and d["category"] not in CATEGORIES:
            problems.append(f"{path.name}: {fn} category {d['category']!r} is not one of ours")
            d["category"] = None
        if d.get("commentary_of") not in ours | {None}:
            problems.append(f"{path.name}: {fn} commentary_of {d['commentary_of']!r} is not one of our files")
            d["commentary_of"] = None
        e = ctx.setdefault(fn, {})
        e.update({k: v for k, v in d.items()})
        e.setdefault("read_in", []).append(path.stem)

(HERE / "context.json").write_text(json.dumps(dict(sorted(ctx.items())), ensure_ascii=False, indent=1),
                                   encoding="utf-8")
print(f"context.json: {len(ctx)} files")
print("  file_type:", dict(collections.Counter(str(e.get("file_type")) for e in ctx.values())))
print("  confidence:", dict(collections.Counter(str(e.get("confidence")) for e in ctx.values())))
print("  commentary_of set:", sum(1 for e in ctx.values() if e.get("commentary_of")))
print("  category (pass 3):", dict(collections.Counter(str(e.get("category")) for e in ctx.values() if "category" in e)))
for p in problems:
    print("  PROBLEM", p)
