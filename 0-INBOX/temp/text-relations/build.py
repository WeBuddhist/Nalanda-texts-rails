"""Build 0-INBOX/text-relations.json: one entry per file in 1-SOURCES/Text/, with its title,
author, file_type, commentary_of, translation_of, current inbox folder, its own source, the
metadata of the OpenPecha record it matches, how well the two texts match, and duplicates of
it in our corpus.

Data only — no interpretation of the texts:
  - our files:  1-SOURCES/text_catalog.json (title, pandita, wb.pub URL, docx per file)
  - relations:  the OpenPecha API dump, deleted from the vault; read from git:
                texts.json as it was before 9de3d6d4 (1,071 records: type, target, authors)
                and the instance incipit titles as they were before ee311fd8
  - metadata:   1-SOURCES/openpecha-v2-catalog.json (+ its version before 9de3d6d4 for the 12
                texts removed there); source_url / source_description and the text itself from
                the OpenPecha conversions (1-SOURCES/Text/bo-*.md), removed in 124597e4
                (or 9de3d6d4)
  - candidates: exact Tibetan title (title, alt titles, incipit titles), punctuation stripped
  - check:      each candidate's text against ours, as shared 4-syllable sequences:
                  same-text  both ways >= 80%
                  part       ours >= 80% inside it, it >= 30% inside ours (a volume of it)
                  fragment   ours >= 80% inside it, it < 30% inside ours (an excerpt)
                  contains   it >= 80% inside ours, ours < 80% inside it
                  different  neither
                  title-only no OpenPecha text to compare (record never downloaded)
                same-text, part and title-only keep the match; the rest are dropped

Rules for file_type (agreed 2026-10-12), on the kept matches:
  has a target, typed commentary          -> commentary (of that target)
  has a target, typed translation         -> translation (of that target)
  no target, other records point to it    -> root-text
  no target, nothing points to it         -> unknown
  a record whose target is itself one of the file's title matches is ignored
  data says root-text but the file sits in 0-INBOX/commentary -> unknown (a commented-on
  commentary — a sub-commentary's root — cannot be told from a root by this data)

Run from the vault root:  venv\\Scripts\\python.exe -X utf8 0-INBOX\\temp\\text-relations\\build.py
"""
import collections
import json
import re
import subprocess
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
OUT = VAULT / "0-INBOX" / "text-relations.json"
TEXTS_COMMIT = "9de3d6d4^"      # fullest texts.json
INSTANCES_COMMIT = "ee311fd8^"  # last state of the per-text folders
CONVERSIONS = ["124597e4", "9de3d6d4"]   # commits that removed the OpenPecha conversions
API = "0-INBOX/raw-data/openpecha-api"
OP_CATALOG = "1-SOURCES/openpecha-v2-catalog.json"
SAME, PART = 0.8, 0.3
KEEP = ("same-text", "part", "title-only")


def git(*args):
    return subprocess.run(["git", *args], cwd=VAULT, capture_output=True, check=True).stdout


class Blobs:
    """Many `git show <rev>:<path>` reads through one `git cat-file --batch` process."""

    def __init__(self):
        self.p = subprocess.Popen(["git", "cat-file", "--batch"], cwd=VAULT,
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def get(self, spec):
        self.p.stdin.write(spec.encode("utf-8") + b"\n")
        self.p.stdin.flush()
        # "<sha> <type> <size>", or "<spec> missing" (a spec may contain spaces)
        head = self.p.stdout.readline().rstrip(b"\n")
        if head.endswith((b" missing", b" ambiguous")):
            return None
        data = self.p.stdout.read(int(head.split()[-1]))
        self.p.stdout.read(1)
        return data


blobs = Blobs()


def norm(t):
    t = re.sub(r"[༄༅༆།༎༏༐༑༔\s]", "", t or "").replace("༌", "་")
    t = re.sub(r"(་?བཞུགས(་སོ)?)+$", "", t)
    return t.strip("་")


def grams(text):
    """Shared-text key: the set of 4-syllable sequences of the body (no frontmatter, no
    headings, no footnotes)."""
    t = re.sub(r"^---\n.*?\n---\n", "", text.replace("\r\n", "\n"), flags=re.S)
    t = re.sub(r"(?m)^\[\^\d+\]:.*$", "", t)
    t = re.sub(r"\[\^\d+\]", "", t)
    t = re.sub(r"(?m)^#.*$", "", t)
    s = re.findall(r"[ཀ-ྼ]+", t.replace("༌", "་"))
    return {tuple(s[k:k + 4]) for k in range(len(s) - 3)}


def overlap(a, b):
    """(share of a found in b, share of b found in a)."""
    n = len(a & b)
    return (n / len(a) if a else 0.0, n / len(b) if b else 0.0)


def verdict(ours_in, theirs_in):
    if ours_in >= SAME and theirs_in >= SAME:
        return "same-text"
    if ours_in >= SAME:
        return "part" if theirs_in >= PART else "fragment"
    if theirs_in >= SAME:
        return "contains"
    return "different"


# ── OpenPecha records and every Tibetan title each is known by ──────────────
records = {x["id"]: x for x in json.loads(blobs.get(f"{TEXTS_COMMIT}:{API}/texts.json"))}
titles = collections.defaultdict(set)
for i, x in records.items():
    for t in [(x.get("title") or {}).get("bo")] + [a.get("bo") for a in x.get("alt_titles") or []]:
        if t:
            titles[i].add(norm(t))
paths = git("ls-tree", "-r", "--name-only", INSTANCES_COMMIT, "--", f"{API}/texts").decode().split("\n")
for p in paths:
    if not re.search(r"/texts/[^/]+/instances(\.json|/[^/]+\.json)$", p):
        continue
    tid = p.split("/texts/")[1].split("/")[0]
    j = json.loads(blobs.get(f"{INSTANCES_COMMIT}:{p}"))
    for m in (j if isinstance(j, list) else [j.get("metadata", j)]):
        if isinstance(m, dict):
            alts = [a.get("bo") for a in m.get("alt_incipit_titles") or [] if isinstance(a, dict)]
            for t in [(m.get("incipit_title") or {}).get("bo")] + alts:
                if t:
                    titles[tid].add(norm(t))
by_title = collections.defaultdict(set)
for i, ts in titles.items():
    for t in ts:
        if t:
            by_title[t].add(i)
pointed_by = collections.defaultdict(list)
for x in records.values():
    if x.get("target"):
        pointed_by[x["target"]].append(x["id"])

# ── OpenPecha metadata and text: catalog + the removed conversions ───────────
catalog = {}
for raw in (blobs.get(f"{TEXTS_COMMIT}:{OP_CATALOG}"), (VAULT / OP_CATALOG).read_bytes()):
    for t in json.loads(raw)["texts"]:
        catalog[t["text_id"]] = t            # the current catalog wins
_conv = {}


# category names by id, in the catalog's "en / bo" form — for records never downloaded
# (not in the catalog), whose category_id is known from texts.json
CATEGORY_NAME = {k["id"]: f"{k.get('title_en')} / {k.get('title_bo')}"
                 for k in json.loads(blobs.get(f"{INSTANCES_COMMIT}:{API}/categories.json"))}


def conversion(i):
    """(frontmatter fields, removing commit, body 4-grams) of record i's conversion file."""
    if i in _conv:
        return _conv[i]
    out = ({}, None, None)
    path = catalog.get(i, {}).get("file")
    for c in CONVERSIONS if path else ():
        raw = blobs.get(f"{c}^:{path}")
        if raw is None:
            continue
        text = raw.decode("utf-8").replace("\r\n", "\n")
        m = re.match(r"---\n(.*?)\n---", text, re.S)
        fields = {}
        for line in (m.group(1) if m else "").split("\n"):
            kv = re.match(r"^([a-z_0-9]+):\s*(.*)$", line)
            if kv and kv.group(2):
                v = kv.group(2).strip()
                fields[kv.group(1)] = v[1:-1] if len(v) > 1 and v[0] == v[-1] == '"' else v
        out = (fields, c, grams(text))
        break
    _conv[i] = out
    return out


def people(i, role):
    """Every contributor of record i with this role (author / translator): the name in every
    language the record gives (bo, en, sa, lzh …), the other names, the BDRC person id."""
    out = []
    for c in records.get(i, {}).get("contributions") or []:
        if c.get("role") == role:
            alt = {}
            for a in c.get("alt_names") or []:
                for lang, name in a.items():
                    if name and name != (c.get("person_name") or {}).get(lang):
                        alt.setdefault(lang, []).append(name)
            out.append({"name": c.get("person_name") or {}, "alt_names": alt,
                        "bdrc_person_id": c.get("person_bdrc_id")})
    return out


def op_meta(i):
    """Metadata of OpenPecha record i, from the catalog and its removed conversion file."""
    x, c = records.get(i, {}), catalog.get(i, {})
    fm, removed_in, _ = conversion(i)
    return {
        "openpecha_text_id": i,
        "openpecha_type": x.get("type"),
        "openpecha_title": x.get("title") or {},
        "openpecha_alt_titles": x.get("alt_titles") or [],
        "author": people(i, "author"),
        "translator": people(i, "translator"),
        "former_file": c.get("file"),
        "former_file_removed_in": removed_in,
        "lang_tag": fm.get("lang_tag") or c.get("lang_tag"),
        "language": fm.get("language") or c.get("language") or x.get("language"),
        "source": fm.get("source") or c.get("source"),
        "source_url": fm.get("source_url"),
        "source_description": fm.get("source_description"),
        "bdrc_work_id": c.get("bdrc_work_id") or x.get("bdrc"),
        "license": c.get("license") or x.get("license"),
        "category_id": c.get("category_id") or x.get("category_id"),
        "category": c.get("category") or CATEGORY_NAME.get(c.get("category_id") or x.get("category_id")),
    }


# ── our files ────────────────────────────────────────────────────────────────
cat = json.loads((VAULT / "1-SOURCES/text_catalog.json").read_text(encoding="utf-8"))
works = sorted((w for p in cat["panditas"] for w in p["works"]), key=lambda w: w["filename"])
folder = {}
for sub in ("root", "commentary", "translation"):
    for f in (VAULT / "0-INBOX" / sub).glob("*.md"):
        folder[f.name] = f"0-INBOX/{sub}"
our_by_title = collections.defaultdict(list)
for w in works:
    our_by_title[norm(w["work_title"])].append(w["filename"])
our_grams = {w["filename"]: grams((VAULT / "1-SOURCES/Text" / w["filename"]).read_text(encoding="utf-8"))
             for w in works}


def ref(i):
    """A pointer to an OpenPecha record: our file if one has its title, its title, and the
    record's metadata (incl. the OpenPecha conversion file it once had in 1-SOURCES/Text)."""
    files = sorted({f for t in titles[i] for f in our_by_title.get(t, [])})
    return {"file": files[0] if len(files) == 1 else (files or None),
            "title": (records[i].get("title") or {}).get("bo"), **op_meta(i)}


texts, kept_record = {}, {}
for w in works:
    fn = w["filename"]
    where = folder.get(fn)
    title_cands = by_title.get(norm(w["work_title"]), set())
    # text check of every title match
    checks = {}
    for i in sorted(title_cands):
        g = conversion(i)[2]
        if g is None:
            checks[i] = {"result": "title-only", "openpecha_text_id": i}
        else:
            a, b = overlap(our_grams[fn], g)
            checks[i] = {"result": verdict(a, b), "openpecha_text_id": i,
                         "ours_in_openpecha": round(a, 2), "openpecha_in_ours": round(b, 2)}
    verified = [i for i in checks if checks[i]["result"] in ("same-text", "part")]
    # relations come from every match the text check does not reject: a record with no text
    # (title-only) may carry the relation that the downloaded twin lacks — a missing target
    # means "not recorded", not "no relation"
    cands = [i for i in checks if checks[i]["result"] in KEEP]
    # a record pointing at another title match (itself, as far as the title key can tell)
    # says nothing about this file
    own = [i for i in cands if records[i].get("target") and records[i]["target"] not in title_cands]
    comm = [i for i in own if records[i]["type"] == "commentary"]
    trans = [i for i in own if records[i]["type"] == "translation"]
    pointers = sorted({p for i in cands for p in pointed_by.get(i, []) if p not in title_cands})
    e = {"title": w["work_title"],
         "author": re.sub(r"^\d+-", "", w["pandita"]),
         "file_type": None, "file_type_source": None,
         "commentary_of": None, "commentary_of_source": None, "translation_of": None,
         "commented_by": [], "translated_by": [],
         "inbox_folder": where, "duplicate_of": [],
         "lang_tag": "bo", "language": "Tibetan",
         "source": w["work_url"],
         "source_description": f"{cat['corpus']}: {w['source_docx']} ({w['pandita']})",
         "openpecha": None, "match_check": None}
    best = lambda ids: max(ids, key=lambda i: (checks[i].get("ours_in_openpecha", 0)
                                               + checks[i].get("openpecha_in_ours", 0),
                                               len(pointed_by.get(i, []))))
    primary = None                    # the OpenPecha record this file is taken to be
    if not title_cands:
        ev = "no OpenPecha record has this title"
    elif not cands:
        ev = "title matches, but the text check rejects every match"
    elif comm:
        primary = best(comm)
        e["file_type"], e["file_type_source"] = "commentary", "openpecha-data"
        e["commentary_of"], e["commentary_of_source"] = ref(records[primary]["target"]), "openpecha-data"
        ev = f"OpenPecha record {primary} is a commentary with this target"
    elif trans:
        primary = best(trans)
        e["file_type"], e["file_type_source"] = "translation", "openpecha-data"
        e["translation_of"] = ref(records[primary]["target"])
        ev = f"OpenPecha record {primary} is a translation with this target"
    elif pointers:
        primary = best([i for i in cands if pointed_by.get(i)] or cands)
        n = collections.Counter(records[p]["type"] for p in pointers)
        said = ", ".join(f"{v} {k}" for k, v in sorted(n.items()))
        # having commentaries does not make a text a root: a commentary can have its own
        # sub-commentary, and "no target" only means none was recorded
        ev = f"no target recorded; pointed to by {said} (has commentaries — not proof of root-text)"
    else:
        primary = best(verified) if verified else (cands[0] if len(cands) == 1 else None)
        ev = "matched OpenPecha record(s) have no target and nothing points to them"
    if len(cands) > 1 and primary is None:
        ev += f"; title matches {len(cands)} OpenPecha records with no text to tell them apart — none chosen"
    rejected = [c for c in checks.values() if c["result"] not in KEEP]
    if rejected:
        ev += "; text check rejected " + ", ".join(f"{c['openpecha_text_id']} ({c['result']})" for c in rejected)
    for p in pointers:                       # texts recorded as commenting on / translating this one
        key = {"commentary": "commented_by", "translation": "translated_by"}.get(records[p]["type"])
        if key:
            files = sorted({f for t in titles[p] for f in our_by_title.get(t, [])})
            e[key].append({"file": files[0] if len(files) == 1 else (files or None),
                           "title": (records[p].get("title") or {}).get("bo"),
                           "openpecha_text_id": p, "language": records[p].get("language"),
                           "author": [a["name"] for a in people(p, "author")],
                           "source": "openpecha-data"})
    if e["file_type"] and where and e["file_type"].replace("-text", "") not in where:
        ev += f"; folder disagrees ({where})"
    if primary and verified and primary not in verified:
        # the relation came from a record never downloaded; the metadata block is the
        # record whose text matches ours
        ev += f"; relation from {primary} (no text to check), metadata from {best(verified)} (text matches)"
        primary = best(verified)
    if primary:
        e["openpecha"] = op_meta(primary)
        e["match_check"] = checks[primary]
        kept_record[fn] = primary
    elif rejected:
        e["match_check"] = max(rejected, key=lambda c: c.get("ours_in_openpecha", 0))
    e["evidence"] = ev
    texts[fn] = e

# ── duplicates in our corpus: files sharing a title or a matched record ──────
groups = collections.defaultdict(set)
for fs in our_by_title.values():
    for f in fs:
        groups[f] |= set(fs)
by_record = collections.defaultdict(list)
for f, i in kept_record.items():
    by_record[i].append(f)
for fs in by_record.values():
    for f in fs:
        groups[f] |= set(fs)
for f, others in groups.items():
    for o in sorted(others - {f}):
        a, b = overlap(our_grams[f], our_grams[o])
        if a >= SAME and b >= SAME:
            texts[f]["duplicate_of"].append(o)

# ── context-based decisions (read from the texts by agents), never over the data ──
CONTEXT = Path(__file__).with_name("context.json")
ctx = json.loads(CONTEXT.read_text(encoding="utf-8")) if CONTEXT.exists() else {}
for fn, c in ctx.items():
    e = texts.get(fn)
    if not e:
        continue
    e["context"] = c                          # the full decision, with its evidence
    if c.get("file_type"):
        if e["file_type"] is None:
            e["file_type"], e["file_type_source"] = c["file_type"], "context"
        elif e["file_type"] != c["file_type"]:
            e["evidence"] += f"; context reading says {c['file_type']} (data kept)"
    target = c.get("commentary_of")
    if target in texts and e["commentary_of"] is None and e["file_type"] == "commentary":
        e["commentary_of"] = {"file": target, "title": texts[target]["title"], "source": "context"}
        e["commentary_of_source"] = "context"
        texts[target]["commented_by"].append({"file": fn, "title": e["title"], "source": "context"})
for fn, e in texts.items():
    t = (e["commentary_of"] or {}).get("file")
    e["sub_commentary"] = bool(t in texts and texts[t]["file_type"] == "commentary")

about = {
    "what": "One entry per file in 1-SOURCES/Text/: title, author, file_type, commentary_of, "
            "translation_of, the 0-INBOX folder the file sits in, duplicates in our corpus, the "
            "file's own source, the metadata of the OpenPecha record it matches, and the text check "
            "of that match.",
    "built_by": "0-INBOX/temp/text-relations/build.py (re-run to rebuild; edits by hand are lost)",
    "data": f"titles and panditas: 1-SOURCES/text_catalog.json; relations: OpenPecha API dump "
            f"(texts.json at {TEXTS_COMMIT}, instance incipit titles at {INSTANCES_COMMIT}); "
            "metadata and texts: 1-SOURCES/openpecha-v2-catalog.json and the OpenPecha conversions "
            "removed in 124597e4 / 9de3d6d4",
    "file_type_values": {
        "root-text": "a root text (only from the context reading: the data never shows it)",
        "commentary": "comments on another text (commentary_of, when known)",
        "translation": "points to its source (translation_of)",
        "null": "not decided"},
    "sources": {
        "openpecha-data": "an OpenPecha relation (type + target) on a text-checked match",
        "context": "read from the text by an agent (title, opening, colophon, glossing, quoted "
                   "root text); the decision and its evidence are in the entry's `context`, and "
                   "kept in 0-INBOX/temp/text-relations/context.json. Data wins where both exist."},
    "match_check_values": {
        "same-text": "our text and the OpenPecha text share >= 80% of their 4-syllable sequences both ways",
        "part": "ours is >= 80% inside the OpenPecha text and covers >= 30% of it (one volume of it)",
        "title-only": "the OpenPecha text was never downloaded: only the title backs the match",
        "fragment / contains / different": "rejected — ours is a short excerpt of it / it is a "
            "short part of ours / the texts differ; no openpecha block, and its relations are not used"},
    "fields": {
        "author": "the master whose collected works the file is in (text_catalog pandita) — the "
                  "printed edition's grouping, not a verified authorship; OpenPecha's recorded "
                  "author is in openpecha.author",
        "duplicate_of": "our files with the same text (>= 80% shared both ways), among files that "
                        "share a title or a matched OpenPecha record",
        "lang_tag / language / source / source_description": "of our file (the Nalanda printed "
            "edition; source = its wb.pub link, which no longer resolves)",
        "openpecha": "the matched OpenPecha record: text id, type, author(s) and translator(s) (each with its name in every language given, other names, BDRC person id), the conversion file "
            "it once had in 1-SOURCES/Text (former_file, removed_in), lang_tag, language, source, "
            "source_url, source_description, bdrc_work_id, license, category_id, category; null "
            "when no match survives",
        "match_check": "the text check of that match (or of the closest rejected one)",
        "commentary_of / translation_of": "{file: ours, if one has that title; title; the "
            "target record's OpenPecha metadata as above}",
        "inbox_folder": "where the file is now (0-INBOX/root, commentary, translation) — the "
                        "folders were sorted by hand (9d4bf89e), not from this data"},
    "counts": {
        "file_type": dict(collections.Counter(str(e["file_type"]) for e in texts.values())),
        "file_type_source": dict(collections.Counter(str(e["file_type_source"]) for e in texts.values())),
        "commentary_of": dict(collections.Counter(str(e["commentary_of_source"]) for e in texts.values()
                                                  if e["file_type"] == "commentary")),
        "match_check": dict(collections.Counter((e["match_check"] or {}).get("result", "no title match")
                                                if e["openpecha"] or e["match_check"] else "no title match"
                                                for e in texts.values())),
        "with_openpecha_block": sum(1 for e in texts.values() if e["openpecha"]),
        "files_with_a_duplicate": sum(1 for e in texts.values() if e["duplicate_of"]),
    },
}
OUT.write_text(json.dumps({"about": about, "texts": texts}, ensure_ascii=False, indent=2) + "\n",
               encoding="utf-8")
print(f"{OUT.relative_to(VAULT)}: {len(texts)} texts")
for k, v in about["counts"].items():
    print(f"  {k}: {v}")
for fn, e in texts.items():
    if e["file_type_source"] == "openpecha-data" or "pointed to by" in e["evidence"]:
        print(f"  {fn:<13} {str(e['file_type']):<11} {(e['match_check'] or {}).get('result', ''):<10} "
              f"{e['inbox_folder']:<20} {e['evidence'][:90]}")
