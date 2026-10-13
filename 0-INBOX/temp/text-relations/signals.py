"""Per-file signals for the context reading of 0-INBOX/text-relations.json.

For each file in 1-SOURCES/Text/ (from text_catalog.json):
  - size, metrical share and gloss markers (root_text_build.measure: the root-text-classify
    measure), commentary words in the title
  - the opening (title lines, homage, statement of intent) and the closing (colophon)
  - text reuse inside our corpus: which other files' text this one contains (a commentary
    quotes its root) and which files contain this one, as shares of 4-syllable sequences

Writes signals.json (all of it) and digests/batch-NN.md (one readable digest per file, in
batches for the reading agents). Run from the vault root:
    venv\\Scripts\\python.exe -X utf8 0-INBOX\\temp\\text-relations\\signals.py
"""
import collections
import importlib.util
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
BATCH = 25
OPEN_SYL, CLOSE_SYL = 160, 120
COMMON = 25          # a 4-gram found in more files than this is a formula, not a quotation

spec = importlib.util.spec_from_file_location(
    "rtb", VAULT / "4-SYSTEM/Skills/seg-toc-lib/root_text_build.py")
rtb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rtb)

COMM_WORDS = re.compile(r"འགྲེལ|བཤད|ཊཱི་ཀཱ|ཊཱི་ཀ|ཊཱི་ཀཱ|དཀའ་འགྲེལ|མཆན|རྣམ་བཤད|འབྲུ་འགྲེལ|ཚིག་འགྲེལ|ས་བཅད|བསྡུས་དོན|དོན་བསྡུས")


def body(text):
    t = re.sub(r"^---\n.*?\n---\n", "", text.replace("\r\n", "\n"), flags=re.S)
    t = re.sub(r"(?m)^\[\^\d+\]:.*$", "", t)
    return t.strip()


def syllables(t):
    t = re.sub(r"\[\^\d+\]", "", t)
    t = re.sub(r"(?m)^#.*$", "", t)
    return re.findall(r"[ཀ-ྼ]+", t.replace("༌", "་"))


def clip_syl(text, n, from_end=False):
    """The first (or last) n syllables of the text, as written (lines kept)."""
    pos = [m.start() for m in re.finditer(r"[ཀ-ྼ]+", text)]
    if len(pos) <= n:
        return text.strip()
    return ("…" + text[pos[-n]:]).strip() if from_end else (text[:pos[n]] + "…").strip()


cat = json.loads((VAULT / "1-SOURCES/Text/text_catalog.json").read_text(encoding="utf-8"))
works = [w for p in cat["panditas"] for w in p["works"]]     # catalog order: by pandita, volume
folder = {}
for sub in ("root", "commentary", "translation"):
    for f in (VAULT / "0-INBOX" / sub).glob("*.md"):
        folder[f.name] = sub

files = [w["filename"] for w in works]
raw = {f: (VAULT / "1-SOURCES/Text" / f).read_text(encoding="utf-8") for f in files}
syl = {f: syllables(body(raw[f])) for f in files}
grams = {f: {hash(tuple(s[k:k + 4])) for k in range(len(s) - 3)} for f, s in syl.items()}

# text reuse through an inverted index of the less common 4-grams
post = collections.defaultdict(list)
for k, f in enumerate(files):
    for g in grams[f]:
        post[g].append(k)
shared = collections.defaultdict(collections.Counter)      # shared[a][b] = |grams a ∩ grams b|
for g, ks in post.items():
    if 1 < len(ks) <= COMMON:
        for a in ks:
            for b in ks:
                if a != b:
                    shared[a][b] += 1

signals = {}
for k, w in enumerate(works):
    f = w["filename"]
    kind, _, gloss, verse = rtb.measure(raw[f])
    contains, inside = [], []
    for b, n in shared[k].most_common():
        fb = files[b]
        of_b, of_a = n / max(1, len(grams[fb])), n / max(1, len(grams[f]))
        if of_b >= 0.15 and n >= 20:
            contains.append({"file": fb, "share_of_it_found_here": round(of_b, 2), "shared": n})
        if of_a >= 0.15 and n >= 20:
            inside.append({"file": fb, "share_of_this_found_there": round(of_a, 2), "shared": n})
    text = body(raw[f])
    lines = text.split("\n")
    rest = "\n".join(lines[1:]) if lines and lines[0].startswith("#") else text
    signals[f] = {
        "file": f, "title": w["work_title"], "pandita": w["pandita"], "folder": folder.get(f),
        "docx": w["source_docx"], "syllables": len(syl[f]),
        "classify": kind, "metrical_share": round(verse, 2), "gloss_per_1000": round(gloss, 2),
        "title_commentary_word": bool(COMM_WORDS.search(w["work_title"])),
        "contains": sorted(contains, key=lambda x: -x["share_of_it_found_here"])[:6],
        "found_in": sorted(inside, key=lambda x: -x["share_of_this_found_there"])[:6],
        "opening": clip_syl(rest, OPEN_SYL),
        "closing": clip_syl(rest, CLOSE_SYL, from_end=True),
    }

(HERE / "signals.json").write_text(json.dumps(signals, ensure_ascii=False, indent=1), encoding="utf-8")
out = HERE / "digests"
out.mkdir(exist_ok=True)
for old in out.glob("*.md"):
    old.unlink()
title = {f: s["title"] for f, s in signals.items()}
# the files in 0-INBOX/root are read first (root-NN), then commentary + translation (other-NN)
groups = [("root", [s for s in signals.values() if s["folder"] == "root"]),
          ("other", [s for s in signals.values() if s["folder"] != "root"])]
for name, ordered in groups:
  for b in range(0, len(ordered), BATCH):
    parts = []
    for s in ordered[b:b + BATCH]:
        c = "; ".join(f"{x['file']} ({x['share_of_it_found_here']:.0%} of it) {title[x['file']][:50]}"
                      for x in s["contains"]) or "—"
        i = "; ".join(f"{x['file']} ({x['share_of_this_found_there']:.0%} of this) {title[x['file']][:50]}"
                      for x in s["found_in"]) or "—"
        parts.append(
            f"## {s['file']}\n"
            f"- title: {s['title']}\n"
            f"- pandita: {s['pandita']} · inbox folder (sorted by hand earlier, not evidence): "
            f"{s['folder']} · syllables: {s['syllables']}\n"
            f"- measures: classify={s['classify']} · metrical share {s['metrical_share']:.0%} · "
            f"gloss markers (ཞེས་པ་ནི / ཞེས་བྱ་བ་ནི …) {s['gloss_per_1000']}/1000 syllables · "
            f"commentary word in title: {'yes' if s['title_commentary_word'] else 'no'}\n"
            f"- contains text of: {c}\n"
            f"- its text is found in: {i}\n\n"
            f"opening:\n```\n{s['opening']}\n```\n\nclosing:\n```\n{s['closing']}\n```\n")
    (out / f"{name}-{b // BATCH + 1:02d}.md").write_text("\n".join(parts), encoding="utf-8")
print(f"signals.json: {len(signals)} files · digests: " + ", ".join(
    f"{name} {len(list(out.glob(name + '-*.md')))} batches ({len(o)} files)" for name, o in groups))
print("files containing >=15% of another file:", sum(1 for s in signals.values() if s["contains"]))
