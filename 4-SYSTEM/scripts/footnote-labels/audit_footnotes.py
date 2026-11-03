"""Check every footnote in 1-SOURCES (root texts and commentaries) against what was received.

The baseline is, by default, the raw intake file the text was made from (0-INBOX/root/<id>.md or
0-INBOX/commentary/<id>.md); with --baseline docx it is the original .docx, looked up in
0-INBOX/Nalanda_docx/*/works.json. The baseline's footnotes, in order, are the source of truth.
The text's own footnotes (markers in body
order, each with its definition) are aligned to them by their letters (whitespace, IDs and markup
ignored), and each footnote is checked for:

  text     - its definition's letters differ from every .docx footnote (changed or invented)
  missing  - a .docx footnote inside the text's range has no counterpart in the text
  place    - the marker sits after different text than in the .docx (marker moved)
  lemma    - the lemma (text before the first ༼) is not the text right before the marker
  format   - a witness bracket is not closed, or the definition has no witness at all

Read-only. Writes a summary table and a TSV of every flagged footnote.
Usage:  python audit_footnotes.py [--out-dir 0-INBOX] [ids ...]
"""
import argparse
import difflib
import json
import re
import sys
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
VAULT = Path(__file__).resolve().parents[3]
DOCX_ROOT = VAULT / "0-INBOX" / "Nalanda_docx"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
CTX = 12  # letters of context compared before a marker

DEF_RE = re.compile(r"^\[\^(\w+)\]:[ \t]?(.*)$")
MARK_RE = re.compile(r"\[\^(\w+)\](?!:)")
ID_RE = re.compile(r"(?<!\S)\^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*(?=\s|$)")
LINK_RE = re.compile(r"!\[\[[^\]]*\]\]|\[\[[^\]|]*\|([^\]]*)\]\]|\[\[([^\]]*)\]\]")
NON_LETTER = re.compile(r"[\s་༌།༎༑༔༼༽༄༅༆༈༒​ *#]+")


def letters(s):
    # NFD: a precomposed letter (ཇ U+0F57) and its pair (བ + ྷ) are the same text, as are vowel
    # signs stored in a different order (ི ུ / ུ ི)
    return NON_LETTER.sub("", unicodedata.normalize("NFD", s))


def norm_def(s):
    return letters(s.replace("༌", "་"))


# ------------------------------------------------------------------ .docx side

def docx_notes(path):
    """[(note_text, context_letters_before_mark)] in document order."""
    with zipfile.ZipFile(path) as z:
        notes_xml = ET.fromstring(z.read("word/footnotes.xml"))
        doc = ET.fromstring(z.read("word/document.xml"))
    texts = {fn.get(W + "id"): "".join(t.text or "" for t in fn.iter(W + "t"))
             for fn in notes_xml.iter(W + "footnote")}
    out, stream = [], []
    for p in doc.iter(W + "p"):
        for r in p.iter(W + "r"):
            ref = r.find(W + "footnoteReference")
            if ref is not None and ref.get(W + "id") in texts:
                out.append((texts[ref.get(W + "id")], letters("".join(stream[-60:]))[-CTX:]))
            for t in r.iter(W + "t"):
                if t.text:
                    stream.append(t.text)
        stream.append(" ")
    return out


# ------------------------------------------------------------------ vault side

def vault_notes(path):
    """[(label, def_text, context_letters_before_mark, body_letters_before_mark)] in marker order."""
    text = path.read_text(encoding="utf-8")
    body = re.sub(r"\A---\r?\n.*?\r?\n---\r?\n", "", text, flags=re.S)
    defs, lines, last = {}, [], None
    for line in body.splitlines():
        m = DEF_RE.match(line)
        if m:
            last = m.group(1)
            defs[last] = m.group(2)
        elif last is not None and line.strip():
            # definitions sit at the end of the file; a later line continues the previous one
            # (a raw file may break a long variant reading over several lines)
            defs[last] += " " + line.strip()
        elif last is None and not line.lstrip().startswith("#"):
            lines.append(line)
    stream = LINK_RE.sub(lambda m: m.group(1) or "", ID_RE.sub("", "\n".join(lines)))
    out, pos = [], 0
    plain = []  # letters so far, without markers
    for m in MARK_RE.finditer(stream):
        plain.append(letters(stream[pos:m.start()].replace("༌", "་")))
        pos = m.end()
        before = "".join(plain[-40:])
        out.append((m.group(1), defs.get(m.group(1)), before[-CTX:], before))
    return out, set(defs) - {m[0] for m in out}


def docx_for(stem, index):
    return index.get(f"{stem}.md")


def raw_for(stem):
    """The raw intake file the text was made from (0-INBOX/root or 0-INBOX/commentary)."""
    for folder in ("root", "commentary"):
        p = VAULT / "0-INBOX" / folder / f"{stem}.md"
        if p.exists():
            return p
    return None


def raw_notes(path):
    """[(note_text, context_letters_before_mark)] from a raw file, in marker order."""
    notes, _ = vault_notes(path)
    return [(d or "", ctx) for _, d, ctx, _ in notes]


def build_index():
    index = {}
    for wj in DOCX_ROOT.glob("*/works.json"):
        for w in json.loads(wj.read_text(encoding="utf-8"))["works"]:
            index[w["filename"]] = wj.parent / w["source_docx"]
    return index


# ------------------------------------------------------------------ checks

def lemma_ok(defn, body_before):
    lem = defn.split("༼", 1)[0] if "༼" in defn else ""
    lem = norm_def(lem)
    return not lem or body_before.endswith(lem) or body_before.endswith(lem.rstrip("།"))


def fmt_problem(defn):
    if "༼" not in defn:
        return "no witness ༼…༽"
    if defn.count("༼") != defn.count("༽"):
        return "unbalanced ༼ ༽"
    return None


def audit(stem, path, docx_cache, index, flags, baseline="raw"):
    notes, orphan_defs = vault_notes(path)
    row = {"id": stem, "kind": path.parent.name, "notes": len(notes), "text": 0, "missing": 0,
           "place": 0, "lemma": 0, "format": 0, "orphan_defs": len(orphan_defs), "docx": ""}
    for lab in sorted(orphan_defs):
        flags.append((stem, lab, "orphan", "definition without a marker", ""))
    if not notes:
        return row
    dx = raw_for(stem) if baseline == "raw" else docx_for(stem, index)
    if dx is None or not dx.exists():
        row["docx"] = "no baseline"
        return row
    row["docx"] = dx.name
    if dx not in docx_cache:
        docx_cache[dx] = raw_notes(dx) if baseline == "raw" else docx_notes(dx)
    dnotes = docx_cache[dx]
    a = [norm_def(d or "") for _, d, _, _ in notes]
    b = [norm_def(t) for t, _ in dnotes]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    blocks = [bl for bl in sm.get_matching_blocks() if bl.size]
    matched = {}
    for bl in blocks:
        for k in range(bl.size):
            matched[bl.a + k] = bl.b + k
    lo = min(matched.values()) if matched else 0
    hi = max(matched.values()) if matched else -1
    used = set(matched.values())
    for i, (lab, defn, ctx, before) in enumerate(notes):
        defn = defn or ""
        if i not in matched:
            row["text"] += 1
            flags.append((stem, lab, "text", "no .docx footnote with these letters", defn[:200]))
        else:
            dctx = dnotes[matched[i]][1]
            if ctx[-8:] != dctx[-8:]:
                row["place"] += 1
                flags.append((stem, lab, "place", f"vault …{ctx} | docx …{dctx}", defn[:120]))
        if not lemma_ok(defn, before):
            row["lemma"] += 1
            flags.append((stem, lab, "lemma", f"text before marker …{before[-20:]}", defn[:160]))
        fp = fmt_problem(defn)
        if fp:
            row["format"] += 1
            flags.append((stem, lab, "format", fp, defn[:160]))
    for j in range(lo, hi + 1):
        if j not in used:
            row["missing"] += 1
            flags.append((stem, "-", "missing", f".docx footnote #{j + 1} not in the text", dnotes[j][0][:200]))
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--out-dir", default=str(VAULT / "0-INBOX"))
    ap.add_argument("--baseline", choices=("raw", "docx"), default="raw",
                    help="compare with the raw intake files (default) or the original .docx")
    args = ap.parse_args()
    index = build_index()
    paths = sorted(list((VAULT / "1-SOURCES" / "Text").glob("*.md")) +
                   list((VAULT / "1-SOURCES" / "Commentaries").glob("*.md")))
    if args.ids:
        paths = [p for p in paths if p.stem in set(args.ids)]
    cache, flags, rows = {}, [], []
    for n, p in enumerate(paths, 1):
        rows.append(audit(p.stem, p, cache, index, flags, args.baseline))
        if n % 50 == 0:
            print(f"  {n}/{len(paths)}", flush=True)
    out = Path(args.out_dir)
    with open(out / "footnote-audit.tsv", "w", encoding="utf-8", newline="") as f:
        f.write("id\tlabel\tcheck\tdetail\tdefinition\n")
        for r in flags:
            f.write("\t".join(str(x).replace("\t", " ").replace("\n", " ") for x in r) + "\n")
    (out / "footnote-audit-summary.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    tot = defaultdict(int)
    for r in rows:
        for k in ("notes", "text", "missing", "place", "lemma", "format", "orphan_defs"):
            tot[k] += r[k]
    print(f"{len(rows)} texts · " + " · ".join(f"{k} {v}" for k, v in tot.items()))
    print("no baseline:", [r["id"] for r in rows if r["docx"] == "no baseline" and r["notes"]])


if __name__ == "__main__":
    main()
