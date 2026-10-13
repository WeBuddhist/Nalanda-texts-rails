"""Write YAML frontmatter into every text in 0-INBOX/root and 0-INBOX/commentary, from
0-INBOX/text-relations.json, and write the tracking report 0-INBOX/TEXT-METADATA-BATCH.md.

- title: from the file's own heading line, without the opening marks (༄༅། །) and the closing
  བཞུགས་སོ; the heading as written goes to alt_titles (bo), with the matched OpenPecha
  record's titles in other languages
- file_type: the reading in text-relations.json; where it is undecided, the folder
  (0-INBOX/root -> root-text, 0-INBOX/commentary -> commentary)
- root_text: the file a commentary comments on (commentary_of), as 1-SOURCES/Text/<file>
- author, bdrc_work_id, license, category: from the matched OpenPecha record (362 files);
  otherwise the key is kept with an empty value
- source / source_description: our file's own (the Nalanda printed edition); the OpenPecha
  record's own source URL is not written
Only the frontmatter is added: the body is asserted unchanged. A frontmatter block that this
script wrote (it has openpecha_text_id:) is replaced on a re-run; any other is left alone and
reported.

Run from the vault root:  venv\\Scripts\\python.exe -X utf8 0-INBOX\\temp\\text-relations\\write_frontmatter.py
"""
import collections
import datetime
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from category_review import DIRECT, OURS, genre  # noqa: E402  category mapping + title genre
VAULT = HERE.parents[2]
REPORT = VAULT / "0-INBOX/TEXT-METADATA-BATCH.md"
FOLDERS = {"0-INBOX/root": "root-text", "0-INBOX/commentary": "commentary"}
rel = json.loads((VAULT / "0-INBOX/text-relations.json").read_text(encoding="utf-8"))["texts"]
# the pandita (collected-works volume group) of each file, as text_catalog.json writes it
_cat = json.loads((VAULT / "1-SOURCES/Text/text_catalog.json").read_text(encoding="utf-8"))
PANDITA = {w["filename"]: w["pandita"] for p in _cat["panditas"] for w in p["works"]}


def q(v):
    """A YAML double-quoted scalar."""
    return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'


def heading(body):
    line = next((l for l in body.split("\n") if l.strip()), "")
    return re.sub(r"^#+\s*", "", line).strip()


def clean_title(raw):
    t = re.sub(r"^[༄༅༆།\s]+", "", raw)
    for _ in range(2):
        t = re.sub(r"[།\s]+$", "", t)
        t = re.sub(r"་?བཞུགས(?:་སོ)?$", "", t)
    t = t.rstrip("་ ")
    return t if t.endswith(("༽", "ག", "ཀ")) else t + "།"


CONTEXT = json.loads((HERE / "context.json").read_text(encoding="utf-8")) if (HERE / "context.json").exists() else {}


def cat_of(e):
    """(our category, where it came from): the matched OpenPecha record's category mapped to
    ours, else the reading (pass 3), else none."""
    c = DIRECT.get((e.get("openpecha") or {}).get("category"))
    if c:
        return c, "openpecha"
    c = (CONTEXT.get(e["_file"]) or {}).get("category")
    return (c, "reading") if c in OURS else (None, "")


# license values as our backend writes them (OpenPecha's on the left); texts with no
# OpenPecha license are public too (decided 2026-10-13)
LICENSE = {"Public Domain Mark": "public"}
DEFAULT_LICENSE = "public"
SOURCE = "https://webuddhist.com/"

# alt titles only in languages the backend knows (https://library.webuddhist.com/v2/languages,
# 2026-10-13); others — e.g. cmg, romanised Classical Mongolian — stay in text-relations.json
BACKEND_LANGS = {"bo", "en", "fr", "hi", "ja", "lzh", "mn", "mr", "ne", "pi", "ru", "sa", "th", "vi", "zh"}


# ── IAST -> Devanagari, for the sa alt titles (OpenPecha gives them romanised) ──
_V = {"a": ("अ", ""), "ā": ("आ", "ा"), "i": ("इ", "ि"), "ī": ("ई", "ी"), "u": ("उ", "ु"),
      "ū": ("ऊ", "ू"), "ṛ": ("ऋ", "ृ"), "ṝ": ("ॠ", "ॄ"), "ḷ": ("ऌ", "ॢ"), "ḹ": ("ॡ", "ॣ"),
      "e": ("ए", "े"), "ai": ("ऐ", "ै"), "o": ("ओ", "ो"), "au": ("औ", "ौ")}
_C = {"k": "क", "kh": "ख", "g": "ग", "gh": "घ", "ṅ": "ङ", "c": "च", "ch": "छ", "j": "ज",
      "jh": "झ", "ñ": "ञ", "ṭ": "ट", "ṭh": "ठ", "ḍ": "ड", "ḍh": "ढ", "ṇ": "ण", "t": "त",
      "th": "थ", "d": "द", "dh": "ध", "n": "न", "p": "प", "ph": "फ", "b": "ब", "bh": "भ",
      "m": "म", "y": "य", "r": "र", "l": "ल", "v": "व", "ś": "श", "ṣ": "ष", "s": "स", "h": "ह"}
_M = {"ṃ": "ं", "ṁ": "ं", "ḥ": "ः", "'": "ऽ"}
_TOKENS = sorted(list(_V) + list(_C) + list(_M), key=len, reverse=True)


def iast_to_deva(text):
    """Exact letter-by-letter IAST -> Devanagari: vowel signs after consonants, a virāma
    between consonants and at a word end; anything that is not IAST passes through."""
    text = unicodedata.normalize("NFC", text.replace("­", "")).lower()
    out, i, prev_c = [], 0, False
    while i < len(text):
        tok = next((t for t in _TOKENS if text.startswith(t, i)), None)
        if tok in _V:
            out.append(_V[tok][1] if prev_c else _V[tok][0])
            prev_c = False
        elif tok in _C:
            if prev_c:
                out.append("्")
            out.append(_C[tok])
            prev_c = True
        else:
            if prev_c:
                out.append("्")
            out.append(_M[tok] if tok in _M else text[i])
            prev_c = False
            tok = tok or text[i]
        i += len(tok)
    if prev_c:
        out.append("्")
    return "".join(out)


def person(p, key):
    n = p.get("name") or {}
    return n.get("bo") if key == "bo" else (n.get("en") or n.get("sa"))


def frontmatter(fn, e, body, folder):
    raw = heading(body)
    title = clean_title(raw)
    alt, seen = [], {title}
    full = re.sub(r"^[༄༅༆།\s]+", "", raw)
    if full not in seen:
        alt.append(("bo", full))
        seen.add(full)
    op = e.get("openpecha") or {}
    for d in [op.get("openpecha_title") or {}] + list(op.get("openpecha_alt_titles") or []):
        for lang, v in d.items():
            if v and v not in seen and lang in BACKEND_LANGS:
                alt.append((lang, iast_to_deva(v) if lang == "sa" else v))
                seen.add(v)
    authors = op.get("author") or []
    a_bo = [person(p, "bo") for p in authors if person(p, "bo")]
    a_en = [person(p, "en") for p in authors if person(p, "en")]
    ftype = e["file_type"] or FOLDERS[folder]
    root = (e.get("commentary_of") or {}).get("file") if ftype == "commentary" else None
    fields = [
        ("title", title),
        ("alt_titles", alt),
        ("author", a_bo),
        ("author_in_english", a_en),
        ("date", None),
        ("language", e.get("language")),
        ("file_type", ftype),
        ("lang_tag", e.get("lang_tag")),
        ("verse_id_format", None),
        ("registered_id", None),
        ("root_text", f"1-SOURCES/Text/{root}" if isinstance(root, str) else None),
        ("covers_verses", None),
        ("source_description", f"{e.get('source_description')}; {e.get('source')}"),
        ("bdrc_work_id", op.get("bdrc_work_id")),
        ("source", SOURCE),
        ("license", LICENSE.get(op.get("license"), op.get("license")) or DEFAULT_LICENSE),
        ("pandita", PANDITA.get(fn)),
        ("category_id", OURS[cat_of(e)[0]][0] if cat_of(e)[0] else None),
        ("category_name", f"{cat_of(e)[0]} / {OURS[cat_of(e)[0]][1]}" if cat_of(e)[0] else None),
        ("openpecha_text_id", op.get("openpecha_text_id")),
    ]
    out = ["---"]
    for k, v in fields:
        if isinstance(v, list) and v and isinstance(v[0], tuple):
            out.append(f"{k}:")
            out += [f"  - {lang}: {q(val)}" for lang, val in v]
        elif isinstance(v, list):
            out.append(f"{k}: {q(v[0])}" if len(v) == 1 else (f"{k}:" if not v else
                       f"{k}:\n" + "\n".join(f"  - {q(x)}" for x in v)))
        else:
            out.append(f"{k}:" if v in (None, "") else f"{k}: {q(v)}")
    out.append("---")
    return "\n".join(out) + "\n\n", ftype, title


rows, skipped, counts = [], [], collections.Counter()
for folder in FOLDERS:
    for path in sorted((VAULT / folder).glob("*.md")):
        fn = path.name
        e = rel.get(fn)
        if not e:
            skipped.append((fn, "not in text-relations.json"))
            continue
        text = path.read_text(encoding="utf-8")
        body = text
        m = re.match(r"---\n(.*?)\n---\n\n?", text, re.S)
        if m:
            if "openpecha_text_id:" not in m.group(1):
                skipped.append((fn, "has frontmatter not written by this script — left alone"))
                continue
            body = text[m.end():]
        e["_file"] = fn
        fm, ftype, title = frontmatter(fn, e, body, folder)
        new = fm + body
        assert new[len(fm):] == body, fn
        if new != text:
            path.write_text(new, encoding="utf-8")
        op = e.get("openpecha")
        has_op = bool(op)
        counts["with OpenPecha metadata" if has_op else "without OpenPecha metadata"] += 1
        counts[f"file_type {ftype}"] += 1
        default = FOLDERS[folder]
        note = []
        if e["file_type"] is None:
            note.append("reading undecided — file_type from the folder")
        elif ftype != default:
            note.append(f"reading says {ftype}, folder says {default}")
        if ftype == "commentary" and not (e.get("commentary_of") or {}).get("file"):
            note.append("root not in our corpus")
        if e.get("duplicate_of"):
            note.append("same text as " + ", ".join(x[:-3] for x in e["duplicate_of"]))
        why = ("" if has_op else
               "no OpenPecha record has this title" if not e.get("match_check") else
               f"title matched, text check: {e['match_check']['result']}")
        rows.append((fn, folder.split("/")[1], ftype, e["file_type_source"] or "folder",
                     "yes" if has_op else "no", (e.get("match_check") or {}).get("result", "") if has_op else why,
                     (op or {}).get("openpecha_text_id", ""), (op or {}).get("bdrc_work_id") or "",
                     "; ".join(person(p, "en") or person(p, "bo") for p in (op or {}).get("author", [])),
                     ((e.get("commentary_of") or {}).get("file") or "")[:-3] if ftype == "commentary" else "",
                     "; ".join(note),
                     (op or {}).get("category") or "", " ".join(x for x in (cat_of(e)[0], f"({cat_of(e)[1]})" if cat_of(e)[0] else "") if x),
                     "{} (`{}`)".format(*genre(e["title"])) if genre(e["title"])[0] else ""))

today = datetime.date.today().isoformat()

# ── summary of the table ─────────────────────────────────────────────────────
# row: 0 file, 1 folder, 2 file_type, 3 type from, 4 OpenPecha, 5 match / why not,
#      6 OpenPecha id, 7 BDRC, 8 author, 9 root_text, 10 note,
#      11 OpenPecha category, 12 -> our category, 13 genre (title word)
summary = ["## Summary", "",
           "| Folder | Texts | root-text | commentary | with OpenPecha metadata | without |",
           "|---|---|---|---|---|---|"]
for name in [f.split("/")[1] for f in FOLDERS] + ["all"]:
    rs = [r for r in rows if name in ("all", r[1])]
    summary.append(f"| {'**all**' if name == 'all' else f'`0-INBOX/{name}`'} | {len(rs)} | "
                   f"{sum(r[2] == 'root-text' for r in rs)} | {sum(r[2] == 'commentary' for r in rs)} | "
                   f"{sum(r[4] == 'yes' for r in rs)} | {sum(r[4] == 'no' for r in rs)} |")
have = [r for r in rows if r[4] == "yes"]
lack = [r for r in rows if r[4] == "no"]
match = collections.Counter(r[5] for r in have)
why_not = collections.Counter(r[5] for r in lack)
comm = [r for r in rows if r[2] == "commentary"]
differ = [r for r in rows if "folder says" in r[10]]
undecided = [r for r in rows if "undecided" in r[10]]
dups = sorted({tuple(sorted([r[0][:-3]] + re.search(r"same text as ([^;]+)", r[10]).group(1).split(", ")))
               for r in rows if "same text as" in r[10]})
summary += [
    "",
    f"**OpenPecha metadata — {len(have)} texts.** Text check of the match: "
    + ", ".join(f"{k} {v}" for k, v in match.most_common())
    + f". Of these, {sum(bool(r[8]) for r in have)} have an author and "
    f"{sum(bool(r[7]) for r in have)} a BDRC work id.",
    "",
    f"**No OpenPecha metadata — {len(lack)} texts:** "
    + "; ".join(f"{k} ({v})" for k, v in why_not.most_common()) + ".",
    "",
    f"**Commentaries — {len(comm)}:** `root_text` filled for {sum(bool(r[9]) for r in comm)} "
    f"(the root is one of our files); for {sum(not r[9] for r in comm)} the root is not in our corpus.",
    "",
    f"**`file_type` differs from the folder — {len(differ)}:** "
    + (", ".join(f"{r[0][:-3]} ({r[2]} in `{r[1]}`)" for r in differ) or "none") + ".",
    "",
    f"**Reading undecided, `file_type` from the folder — {len(undecided)}:** "
    + (", ".join(f"{r[0][:-3]} ({r[2]})" for r in undecided) or "none") + ".",
    "",
    f"**Same text in two files — {len(dups)} pairs:** " + (", ".join(" = ".join(d) for d in dups) or "none") + ".",
    "",
]
# ── categories: our backend ids — from OpenPecha (mapped) or from the reading (pass 3) ──
def _cat(r):
    return (r[12].split(" (")[0], r[12].split(" (")[1].rstrip(")")) if r[12] else (None, None)


by_src = collections.defaultdict(collections.Counter)
for r in rows:
    name, src = _cat(r)
    if name:
        by_src[name][src] += 1
nocat = [r for r in rows if not r[12]]
low = [r for r in rows if _cat(r)[1] == "reading"
       and (CONTEXT.get(r[0]) or {}).get("category_confidence") == "low"]
summary += [
    "## Categories", "",
    f"`category_id` / `category_name` are our backend's ({len(OURS)} categories): mapped from the "
    "matched record's OpenPecha category, or — for texts without one — decided by reading the text "
    "(pass 3; column `→ our category` says which, the evidence is in "
    "`0-INBOX/temp/text-relations/context.json`).", "",
    "| Our category | bo | id | from OpenPecha | by reading | texts |", "|---|---|---|---|---|---|",
    *[f"| {k} | {v[1]} | `{v[0]}` | {by_src[k]['openpecha']} | {by_src[k]['reading']} | "
      f"{sum(by_src[k].values())} |" for k, v in OURS.items()],
    f"| **all** | | | {sum(c['openpecha'] for c in by_src.values())} | "
    f"{sum(c['reading'] for c in by_src.values())} | **{sum(sum(c.values()) for c in by_src.values())}** |", "",
    f"**No category — {len(nocat)} texts:** "
    + (", ".join(r[0][:-3] for r in nocat) if len(nocat) <= 40 else "see column `→ our category`") + ".", "",
    *([f"**Decided by reading at low confidence — {len(low)}:** "
       + ", ".join(f"{r[0][:-3]} ({_cat(r)[0]})" for r in low) + ".", ""] if low else []),
    "## Texts", "",
]

lines = [
    "# Text metadata batch — YAML frontmatter for 0-INBOX/root and 0-INBOX/commentary", "",
    "Every text in `0-INBOX/root` and `0-INBOX/commentary` got a YAML frontmatter block from "
    "`0-INBOX/text-relations.json`. This document says which texts carry OpenPecha metadata and "
    "which do not. How to re-run: `venv\\Scripts\\python.exe -X utf8 "
    "0-INBOX\\temp\\text-relations\\write_frontmatter.py` (re-runnable: it replaces only the "
    "block it wrote; the text body is never changed).", "",
    f"Updated {today} · {len(rows)} texts · " + " · ".join(f"{k} {v}" for k, v in sorted(counts.items())), "",
    "| Field | From |", "|---|---|",
    "| `title` | the file's own heading line, without `༄༅། །` and `བཞུགས་སོ` |",
    "| `alt_titles` | the heading as written (bo) + the OpenPecha record's titles in other languages the backend knows (cmg titles are kept only in `text-relations.json`); `sa` titles transliterated from IAST to Devanagari |",
    "| `file_type` | the reading (`text-relations.json`); where undecided, the folder |",
    "| `root_text` | for a commentary: the file it comments on (`commentary_of`), when it is in our corpus |",
    "| `author`, `author_in_english`, `bdrc_work_id`, `openpecha_text_id` | the matched OpenPecha record (`OpenPecha` = yes); empty otherwise |",
    "| `license` | `public` (OpenPecha's `Public Domain Mark`, and every text without an OpenPecha license) |",
    "| `source` | `https://webuddhist.com/` |",
    "| `source_description` | our file (the Nalanda printed edition: corpus, docx, pandita), then its wb.pub link |",
    "| `category_id`, `category_name` | our backend category, mapped from the matched record's OpenPecha category; empty otherwise |",
    "| `pandita` | `1-SOURCES/Text/text_catalog.json`, as written there (e.g. `01-Nagarjuna`) |",
    "| `language`, `lang_tag` | our file (the Nalanda printed edition) |",
    "| `date`, `verse_id_format`, `registered_id`, `covers_verses` | not in the data: left empty |", "",
    "`OpenPecha` yes = the file's text was matched to an OpenPecha record (same title, text "
    "checked). `match` = the text check (`same-text`, `part`, `title-only`) or why there is no "
    "metadata.", "",
    *summary,
    "| # | id | folder | file_type | type from | OpenPecha | match | OpenPecha id | BDRC work | author (OpenPecha) | root_text | note | OpenPecha category | → our category | genre (title) |",
    "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
]
lines += [f"| {k} | {r[0][:-3]} | {' | '.join(str(x) for x in r[1:])} |" for k, r in enumerate(rows, 1)]
if skipped:
    lines += ["", "## Not written", ""] + [f"- {fn}: {why}" for fn, why in skipped]
REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"frontmatter written: {len(rows)} · skipped: {len(skipped)} · {dict(counts)}")
print(f"report: {REPORT.relative_to(VAULT)}")
