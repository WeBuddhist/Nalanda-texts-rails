"""Inputs for pass 2 (linking each commentary to the text it comments on).

Reads context.json (pass 1) and text-relations.json (data), and for every file whose
file_type is commentary writes a digest entry with: title, pass-1 named_root and candidates,
the files whose text it contains (exact pairwise shares of 4-syllable sequences, top 8, with
each file's pass-1 type), and its opening and closing. Also writes link-catalog.md: every file
with its title and pass-1 type. The colleague's map is NOT given to the agents (it is checked
against their independent result afterwards).

Run from the vault root:  venv\\Scripts\\python.exe -X utf8 0-INBOX\\temp\\text-relations\\build_pass2.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
BATCH = 15

ctx = json.loads((HERE / "context.json").read_text(encoding="utf-8"))
rel = json.loads((VAULT / "0-INBOX/text-relations.json").read_text(encoding="utf-8"))["texts"]
sig = json.loads((HERE / "signals.json").read_text(encoding="utf-8"))
ftype = {f: e["file_type"] for f, e in rel.items()}


def grams(f):
    t = (VAULT / "1-SOURCES/Text" / f).read_text(encoding="utf-8")
    t = re.sub(r"(?m)^\[\^\d+\]:.*$", "", t)
    t = re.sub(r"\[\^\d+\]", "", t)
    t = re.sub(r"(?m)^#.*$", "", t)
    s = re.findall(r"[ཀ-ྼ]+", t.replace("༌", "་"))
    return {hash(tuple(s[k:k + 4])) for k in range(len(s) - 3)}


G = {f: grams(f) for f in rel}
comms = [f for f in sig if ftype.get(f) == "commentary"]          # catalog order
entries = []
for f in comms:
    x = G[f]
    shares = sorted(((len(G[o] & x) / len(G[o]), o) for o in rel
                     if o != f and len(G[o]) >= 30), reverse=True)[:8]
    c = ctx.get(f, {})
    found = "; ".join(f"{o} {s:.0%} [{ftype.get(o)}] {rel[o]['title'][:45]}" for s, o in shares if s >= 0.03) or "—"
    data = rel[f].get("commentary_of")
    entries.append(
        f"## {f}\n"
        f"- title: {rel[f]['title']}\n"
        f"- pandita: {sig[f]['pandita']} · syllables: {sig[f]['syllables']}\n"
        f"- pass 1: {c.get('confidence')} — {c.get('evidence', '')}\n"
        f"- named_root (pass 1): {c.get('named_root')} · root_candidates: {c.get('root_candidates') or '—'}\n"
        + (f"- OpenPecha data says it comments on: {data.get('title')} (file in our corpus: {data.get('file')})\n" if data else "")
        + f"- share of each file's text found in this one (top 8): {found}\n\n"
        f"opening:\n```\n{sig[f]['opening']}\n```\n\nclosing:\n```\n{sig[f]['closing']}\n```\n")
out = HERE / "digests"
for old in out.glob("link-*.md"):
    old.unlink()
for b in range(0, len(entries), BATCH):
    (out / f"link-{b // BATCH + 1:02d}.md").write_text("\n".join(entries[b:b + BATCH]), encoding="utf-8")
lines = ["# All files — title and pass-1 type", ""]
for t in ("root-text", "commentary", None):
    lines += [f"## {t}", ""] + [f"- {f} — {rel[f]['title']}" for f in sig if ftype.get(f) == t] + [""]
(out / "link-catalog.md").write_text("\n".join(lines), encoding="utf-8")
print(f"{len(comms)} commentaries · {len(list(out.glob('link-0*.md')) + list(out.glob('link-1*.md')))} link batches of {BATCH} · link-catalog.md")
