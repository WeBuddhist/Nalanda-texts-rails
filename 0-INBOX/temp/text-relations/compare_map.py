"""Compare 0-INBOX/commentary-root-map.md (a colleague's draft, from titles and general
knowledge) with the independent context reading (context.json: pass 1 types, pass 2 links),
and write the verdict per claim to 0-INBOX/commentary-root-map-check.md.

Needs map-check.json (check_map.py) and context.json (merge_context.py after pass 2).
Run from the vault root:  venv\\Scripts\\python.exe -X utf8 0-INBOX\\temp\\text-relations\\compare_map.py
"""
import collections
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
mc = json.loads((HERE / "map-check.json").read_text(encoding="utf-8"))
ctx = json.loads((HERE / "context.json").read_text(encoding="utf-8"))
rel = json.loads((VAULT / "0-INBOX/text-relations.json").read_text(encoding="utf-8"))["texts"]
title = {f: e["title"] for f, e in rel.items()}
dup = {f: set(e["duplicate_of"]) for f, e in rel.items()}


def link(f):
    return ctx.get(f, {}).get("commentary_of")


def same(a, b):
    return a == b or (a in dup and b in dup[a])


def short(f):
    return f"[[{f[:-3]}]]" if f else "—"


rows_a, rows_b, verdicts = [], [], collections.Counter()
for c in mc["section_a"]:
    f, r, ours = c["file"], c["root"], link(c["file"])
    t = ctx.get(f, {}).get("file_type")
    reuse = f"{c['root_found_in_it']:.0%}"
    if c["kind"] == "translation":
        v = ("agree: both texts read as the same root (other translation)"
             if t == "root-text" and ctx.get(r, {}).get("file_type") == "root-text"
             else f"check: reading says {t}")
    elif t != "commentary":
        v = f"DISAGREE: the reading says {t}, not a commentary"
    elif ours and same(ours, r):
        v = "agree"
    elif ours:
        v = f"DISAGREE: reading links it to {short(ours)}"
    else:
        v = "not confirmed: the reading found no root in our corpus"
    verdicts[v.split(":")[0]] += 1
    ev = ctx.get(f, {}).get("link_evidence") or ctx.get(f, {}).get("evidence", "")
    rows_a.append(f"| {short(r)} | {c['kind']} | {short(f)} | {reuse} | {v} | {ev[:160]} |")
for c in mc["section_b"]:
    f, ours, t = c["file"], link(c["file"]), ctx.get(c["file"], {}).get("file_type")
    if t != "commentary":
        v = f"DISAGREE: the reading says {t}, not a commentary"
    elif ours:
        v = f"DISAGREE: reading finds its root in our corpus: {short(ours)}"
    else:
        v = "agree (root not in our corpus)"
    verdicts["B " + v.split(":")[0].split(" (")[0]] += 1
    ev = ctx.get(f, {}).get("link_evidence") or ""
    rows_b.append(f"| {short(f)} | {c['comments_on']} | {v} | {ev[:160]} |")
mapped = {c["file"] for c in mc["section_a"]} | {c["file"] for c in mc["section_b"]}
extra = [f for f, e in ctx.items() if e.get("file_type") == "commentary" and f not in mapped]
rows_x = [f"| {short(f)} | {title[f]} | {short(link(f))} | {(ctx[f].get('link_evidence') or '')[:160]} |"
          for f in sorted(extra)]

out = [
    "---", "title: Check of commentary-root-map.md", "status: draft", "---", "",
    "# Check of `commentary-root-map.md`", "",
    "Scratch work, not authoritative. Each claim in the map is compared with an independent "
    "reading of the texts (`0-INBOX/temp/text-relations/`: pass 1 decides root text vs "
    "commentary, pass 2 links each commentary; neither saw the map) and with the share of "
    "the claimed root's text found in the commentary (4-syllable sequences).", "",
    "**Verdicts:** " + " · ".join(f"{k} {v}" for k, v in sorted(verdicts.items())), "",
    "## A. Root texts in our corpus with their commentaries", "",
    "| Root (map) | Kind | File | Root's text found in it | Verdict | Reading's evidence |",
    "|---|---|---|---|---|---|", *rows_a, "",
    "## B. Commentaries whose root the map puts outside our corpus", "",
    "| File | Map: comments on | Verdict | Reading's evidence |", "|---|---|---|---|", *rows_b, "",
    "## C. Commentaries the map does not list", "",
    "| File | Title | Reading links it to | Evidence |", "|---|---|---|---|", *rows_x, "",
]
(VAULT / "0-INBOX/commentary-root-map-check.md").write_text("\n".join(out), encoding="utf-8")
print("0-INBOX/commentary-root-map-check.md:", dict(verdicts), f"· not in the map: {len(extra)}")
