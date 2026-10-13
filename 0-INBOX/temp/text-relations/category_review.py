"""Write 0-INBOX/CATEGORY-REVIEW.md: which of our texts map onto the backend's 4 categories,
which categories are missing, and which texts are practice texts (Liturgy candidates) — for
colleagues to decide. Changes no file.

Genre is read from the title only (the word shown in the table), and the OpenPecha category
from text-relations.json; both are hints for the reviewers, not decisions.

Run from the vault root:  venv\\Scripts\\python.exe -X utf8 0-INBOX\\temp\\text-relations\\category_review.py
"""
import collections
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
rel = json.loads((VAULT / "0-INBOX/text-relations.json").read_text(encoding="utf-8"))["texts"]
cat = json.loads((VAULT / "1-SOURCES/text_catalog.json").read_text(encoding="utf-8"))
pandita = {w["filename"]: w["pandita"] for p in cat["panditas"] for w in p["works"]}

OURS = {  # backend categories (2026-10-13): name -> (id, bo)
    "Prajñāpāramitā": ("uGpinx0GZlvU1uw44RyYS", "ཤེར་ཕྱིན།"),
    "Liturgy": ("LCorCb2K98p3TICt3UCDm", "ཞལ་འདོན།"),
    "Systematic Treatises": ("MZUUxphQ0yFwLBon3Vng8", "མངོན་པ།"),
    "Middle Way": ("JD5ULLPAV1cxg7RSb7L3q", "དབུ་མ།"),
    "Tantras": ("REBGnT4qFooPfPEkR5pe5", "རྒྱུད་སྡེ།"),
    "Miscellaneous": ("SoGlGBaboYkVa7b9qJvvK", "སྣ་ཚོགས།"),
    "Mind-only Treatises": ("NDXKdNtZe9Kxl6Y4yBMAr", "སེམས་ཙམ།"),
    "Logic": ("v3L4eTn4x2E30znIhHvQe", "ཚད་མ།"),
    "Mind Trainings and Advices": ("sEStEY4RRWU7U23rkiOk5", "བློ་སྦྱོང་དང་བསླབ་བྱ།"),
    "Discourses": ("XfCwZpoJMtfO7s0laQkdK", "མདོ་སྡེ།"),
    "Monastic Rules": ("4wuvGxIgXNZ5mb0bDWvkC", "འདུལ་བ།"),
    "Linguistics Treatises": ("Rrl0usffAJJbYTYe1euws", "རིག་གནས།"),
    "History and Stories": ("YQnenyXmCd2VbVHPUFGWM", "ལོ་རྒྱུས་དང་སྒྲུང་།"),
}
# OpenPecha category (catalog "en / bo") -> ours; OpenPecha spells "Miscenaleous"
DIRECT = {"Perfection of Wisdom / ཤེར་ཕྱིན།": "Prajñāpāramitā",
          "Miscenaleous / སྣ་ཚོགས།": "Miscellaneous",
          **{f"{k} / {v[1]}": k for k, v in OURS.items() if k not in ("Prajñāpāramitā", "Miscellaneous")}}
# practice-text words in a title, in order of precedence: (word, genre)
PRACTICE = [("སྒྲུབ་ཐབས", "sādhana"), ("མངོན་པར་རྟོགས་པ", "sādhana"), ("སྦྱིན་སྲེག", "fire offering"),
            ("གཏོར་མ", "torma ritual"), ("གཏོར་ཆོག", "torma ritual"), ("དཀྱིལ་འཁོར", "maṇḍala ritual"),
            ("ཆོ་ག", "ritual"), ("ཆོག", "ritual"), ("མཆོད་པ", "offering"), ("བསྔོ་བ", "dedication"),
            ("སྨོན་ལམ", "prayer"), ("གསོལ་འདེབས", "supplication"), ("གསོལ་བ་འདེབས", "supplication"),
            ("བཤགས", "confession"), ("བསྟོད", "praise"), ("ཕྱག་འཚལ", "homage"), ("གཟུངས", "dhāraṇī"),
            ("བཟླས", "recitation"), ("རབ་གནས", "consecration"), ("དབང", "empowerment")]


def genre(title):
    t = re.sub(r"[༄༅།\s]", "", title)
    for word, g in PRACTICE:
        if word in t:
            return g, word
    return None, None


def opcat(e):
    return (e.get("openpecha") or {}).get("category")


if __name__ == "__main__":
    rows = []
    for f, e in rel.items():
        g, word = genre(e["title"])
        rows.append({"file": f[:-3], "title": re.sub(r"^[༄༅༆།\s]+", "", e["title"]),
                     "type": e["file_type"] or "—", "pandita": pandita.get(f, ""),
                     "opcat": opcat(e), "ours": DIRECT.get(opcat(e)), "genre": g, "word": word})

    direct = [r for r in rows if r["ours"]]
    missing = collections.Counter(r["opcat"] for r in rows if r["opcat"] and not r["ours"])
    uncat = [r for r in rows if not r["opcat"]]
    practice = [r for r in rows if r["genre"] and r["ours"] != "Liturgy"]


    def table(rs, cols):
        head = {"file": "file", "title": "title", "type": "file_type", "pandita": "pandita",
                "opcat": "OpenPecha category", "genre": "genre (title word)", "ours": "→ our category"}
        out = ["| " + " | ".join(head[c] for c in cols) + " |", "|" + "---|" * len(cols)]
        for r in rs:
            vals = []
            for c in cols:
                v = r[c] or ""
                if c == "genre" and r["genre"]:
                    v = f"{r['genre']} (`{r['word']}`)"
                vals.append(str(v).replace("|", "/"))
            out.append("| " + " | ".join(vals) + " |")
        return out


    L = ["# Category review — for the colleagues", "",
         "Our backend has 4 categories. Most of the 565 texts fit none of them, so before any "
         "`category_id` is written into the frontmatter, these lists need a decision. Nothing has "
         "been changed yet. Built by `0-INBOX/temp/text-relations/category_review.py` from "
         "`0-INBOX/text-relations.json`.", "",
         "## 1. Our categories", "",
         "| Category | bo | id |", "|---|---|---|",
         *[f"| {k} | {v[1]} | `{v[0]}` |" for k, v in OURS.items()], "",
         "## 2. Direct matches (ready to apply)", "",
         f"{len(direct)} texts carry an OpenPecha category that is the same as one of ours:", "",
         "| OpenPecha category | → our category | texts |", "|---|---|---|",
         *[f"| {k} | {DIRECT[k]} | {v} |" for k, v in collections.Counter(r['opcat'] for r in direct).most_common()], "",
         "Question: **apply these?** (they replace the OpenPecha category id with ours)", "",
         "## 3. Categories we do not have", "",
         f"{sum(missing.values())} texts carry an OpenPecha category that has no counterpart in ours. "
         "Each needs either a new category in the backend, one of our 4, or none.", "",
         "| OpenPecha category | texts | question |", "|---|---|---|",
         *[f"| {k} | {v} | new category? / map to one of ours? / none? |" for k, v in missing.most_common()], "",
         f"Another **{len(uncat)} texts have no OpenPecha category at all** (no OpenPecha match): "
         "they are listed in §5.", "",
         "## 4. Practice texts — Liturgy candidates", "",
         f"{len(practice)} texts whose title names them as a practice text (sādhana, ritual, praise, "
         "prayer, offering, dhāraṇī …). Question: **which of these go under Liturgy?** "
         "(The genre is read from the title word only — check the doubtful ones.)", "",
         "| genre | texts |", "|---|---|",
         *[f"| {k} | {v} |" for k, v in collections.Counter(r['genre'] for r in practice).most_common()], "",
         *table(sorted(practice, key=lambda r: (r["genre"], r["file"])),
                ["file", "title", "genre", "type", "opcat", "pandita"]), "",
         "## 5. Texts with no OpenPecha category", "",
         f"{len(uncat)} texts. Those with a practice word in the title are also in §4.", "",
         *table(sorted(uncat, key=lambda r: r["file"]), ["file", "title", "type", "genre", "pandita"]), "",
         "## 6. Texts with an OpenPecha category we do not have", "",
         *table(sorted([r for r in rows if r["opcat"] and not r["ours"]], key=lambda r: (r["opcat"], r["file"])),
                ["file", "title", "opcat", "type", "genre", "pandita"]), ""]
    (VAULT / "0-INBOX/CATEGORY-REVIEW.md").write_text("\n".join(L), encoding="utf-8")
    print(f"direct {len(direct)} · missing-category texts {sum(missing.values())} · no category {len(uncat)} · "
          f"practice texts {len(practice)} · {dict(collections.Counter(r['genre'] for r in practice))}")
