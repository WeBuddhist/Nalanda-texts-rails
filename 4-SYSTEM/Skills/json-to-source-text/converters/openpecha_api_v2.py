#!/usr/bin/env python3
"""
openpecha_api_v2.py — converter for OpenPecha backend API v2 downloads.

Source: the old production OpenPecha backend (openpecha-backend `main`,
Firebase project `pecha-backend`), downloaded verbatim by
`4-SYSTEM/scripts/openpecha-api-download.py` into
`0-INBOX/raw-data/openpecha-api/`. One folder per text:

    texts/<text_id>/text.json                       GET /v2/texts/<id>
    texts/<text_id>/instances.json                  GET /v2/texts/<id>/instances
    texts/<text_id>/instances/<instance_id>.json    GET /v2/instances/<id>?content=true&annotation=true
    texts/<text_id>/annotations/<annotation_id>.json GET /v2/annotations/<id>

Output convention — collection vault, flat `^N` (`verse_id_format: verse`,
`annotation-conventions.md` §7). The corpus is hundreds of independent texts
with no chapter structure recorded upstream, so each file is one text:

    # <title> ^0

    <segment 1> ^1

    <segment 2> ^2

- **One block per upstream segment.** The segmentation annotation's spans are
  sorted by `start`; block `^N` is the Nth non-empty segment. The mapping
  block → upstream segment ID is written to
  `0-INBOX/raw-data/openpecha-api/block-maps/<text_id>.json` so a block can
  always be traced back to the backend.
- **No loss.** Text between segments that no span covers is emitted as its
  own paragraph without a block ID (the skill's rule for unlabelled prose);
  whitespace-only gaps are dropped. Blank lines inside a segment are
  collapsed to one line break so the segment stays one Markdown block.
  A line that would otherwise parse as Markdown structure (`#`, `>`, a
  setext underline) is backslash-escaped.
- **No segmentation upstream.** One block per non-empty line of the content,
  declared in `segmentation_source:` so nobody mistakes it for an upstream
  segmentation.
- **Instances.** The critical instance is the root text. Any further
  instance (diplomatic, collated) is written as a separate edition file with
  `file_type: edition` and `root_text:` pointing at the critical one.
- **Frontmatter.** Upstream values are copied verbatim; a key the backend
  leaves empty stays empty. The backend's own IDs go under `openpecha_v2_*`
  keys and are deliberately NOT written to `text_id` / `edition_id` /
  `category_id`: those publication fields hold IDs in the current library
  (library.webuddhist.com), where these old IDs do not exist.
- **Filenames** use the work's title in its own script
  (`About Sources.md` §2, native-script alternative): `<lang_tag>-<title>.md`.
  Titles shared by several texts get ` (<text_id>)` appended to every file in
  the clash, so no file is silently overwritten.

Usage:

    # whole corpus → 1-SOURCES/Text/, catalog, block maps
    python3 converters/openpecha_api_v2.py --corpus 0-INBOX/raw-data/openpecha-api 1-SOURCES/Text

    # one text (skill contract: json_path = that text's text.json)
    python3 converters/openpecha_api_v2.py 0-INBOX/raw-data/openpecha-api/texts/<id>/text.json out.md
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

LANGS = {
    # backend code: (language name, lang_tag, script) — sa/pi resolved by script detection
    "bo": ("Tibetan", "bo", "Unicode Tibetan"),
    "lzh": ("Literary Chinese", "zh", "Unicode Chinese"),
    "zh": ("Modern Chinese", "zh-modern", "Unicode Chinese"),   # backend keeps classical as lzh
    "en": ("English", "en", "Latin"),
    "hi": ("Hindi", "hi", "Devanāgarī"),
    "it": ("Italian", "it", "Latin"),
}

ROLE_KEYS = {"author": "author", "translator": "translator", "reviser": "reviser", "scholar": "scholar"}

BAD_FILENAME_CHARS = re.compile(r'[\\/:*?"<>|#^\[\]\x00-\x1f]')
MD_STRUCTURE_LINE = re.compile(r"^(#|>|=+\s*$|-{3,}\s*$|\*{3,}\s*$)")
PLAIN_YAML = re.compile(r"[A-Za-z0-9\u00C0-\u024F\u1E00-\u1EFF][A-Za-z0-9\u00C0-\u024F\u1E00-\u1EFF _.()/-]*")
RESERVED_YAML = re.compile(r"(?i)true|false|yes|no|on|off|null|~|[0-9._-]+")
EXCLUDED_TITLES = {"delete this"}   # upstream test records marked for deletion


# --------------------------------------------------------------------------- helpers

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def detect_script(text: str) -> str:
    sample = text[:20000]
    counts = Counter()
    for ch in sample:
        o = ord(ch)
        if 0x0900 <= o <= 0x097F:
            counts["deva"] += 1
        elif 0x0F00 <= o <= 0x0FFF:
            counts["tibt"] += 1
        elif 0x4E00 <= o <= 0x9FFF:
            counts["hani"] += 1
        elif 0x0D80 <= o <= 0x0DFF:
            counts["sinh"] += 1
        elif 0x1000 <= o <= 0x109F:
            counts["mymr"] += 1
        elif 0x0E00 <= o <= 0x0E7F:
            counts["thai"] += 1
        elif ch.isalpha() and o < 0x0250 or 0x1E00 <= o <= 0x1EFF:
            counts["latn"] += 1
    return counts.most_common(1)[0][0] if counts else "latn"


def language_fields(code: str, content: str):
    """Return (language, lang_tag, script) for a backend language code."""
    script = detect_script(content) if content else None
    if code == "sa":
        if script == "deva":
            return "Sanskrit", "sk", "Devanāgarī"
        return "Sanskrit", "sk-iast", "IAST"
    if code == "pi":
        return {
            "sinh": ("Pāli", "pi-sinh", "Sinhala"),
            "mymr": ("Pāli", "pi-mymr", "Myanmar"),
            "thai": ("Pāli", "pi-thai", "Thai"),
            "deva": ("Pāli", "pi-deva", "Devanāgarī"),
        }.get(script, ("Pāli", "pi", "Roman (Pāli)"))
    if code in LANGS:
        return LANGS[code]
    return code, code, None


def pick_title(title: dict | None, code: str) -> tuple[str, str | None]:
    """Title in the text's own language, else the first one recorded."""
    title = title or {}
    for k in (code, "lzh" if code == "zh" else "zh" if code == "lzh" else None):
        if k and title.get(k):
            return title[k].strip(), k
    for k, v in title.items():
        if v:
            return v.strip(), k
    return "", None


def person_label(c: dict, code: str) -> str:
    names = c.get("person_name") or {}
    name = names.get(code) or names.get("en") or next((v for v in names.values() if v), "") or ""
    name = name.strip()
    if c.get("person_bdrc_id"):
        return f"{name} [bdrc:{c['person_bdrc_id']}]".strip()
    return name


def ai_label(c: dict) -> str:
    return (c.get("ai_id") or c.get("ai") or "").strip()


def yaml_scalar(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if PLAIN_YAML.fullmatch(s) and not RESERVED_YAML.fullmatch(s):
        return s
    return json.dumps(s, ensure_ascii=False)


def render_frontmatter(meta: list[tuple[str, object]]) -> str:
    """Ordered YAML. None → key omitted; "" → empty key (a truthful 'not recorded')."""
    out = ["---"]
    for k, v in meta:
        if v is None:
            continue
        if v == "":
            out.append(f"{k}:")
        elif isinstance(v, list):
            if not v:
                out.append(f"{k}: []")
                continue
            out.append(f"{k}:")
            out += [f"  - {yaml_scalar(x)}" for x in v]
        else:
            out.append(f"{k}: {yaml_scalar(v)}")
    out.append("---")
    return "\n".join(out) + "\n"


def normalise_block(s: str) -> str:
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in s.split("\n")]
    lines = [ln for ln in lines if ln.strip()]           # blank lines would split the block
    lines = [("\\" + ln if MD_STRUCTURE_LINE.match(ln) else ln) for ln in lines]
    return "\n".join(lines).strip()


def safe_filename_title(title: str, max_bytes: int = 180) -> str:
    t = unicodedata.normalize("NFC", title)
    t = BAD_FILENAME_CHARS.sub(" ", t)
    t = re.sub(r"^[\s\u0F01-\u0F14]+", "", t)             # leading yig mgo, head marks, shad
    t = re.sub(r"[\s\u0F0B-\u0F14]+$", "", t)             # trailing tsek / shad / spaces
    t = re.sub(r"\s+", " ", t).strip(" .")
    b = t.encode("utf-8")
    if len(b) > max_bytes:
        cut = b[:max_bytes].decode("utf-8", "ignore")
        # cut back to the last syllable or word boundary so no syllable is split
        m = re.match(r"^(.*[\u0F0B\s\u0F0D])", cut, re.S)
        t = (m.group(1) if m else cut).rstrip(" \u0F0B\u0F0D")
    return t or "untitled"


# --------------------------------------------------------------------------- per-text

def read_text_bundle(text_dir: str):
    text = load(os.path.join(text_dir, "text.json"))
    ipath = os.path.join(text_dir, "instances.json")
    instances = load(ipath) if os.path.exists(ipath) else []
    details = []
    for inst in instances:
        p = os.path.join(text_dir, "instances", f"{inst['id']}.json")
        if not os.path.exists(p):
            continue
        d = load(p)
        anns = {}
        for a in d.get("annotations") or []:
            ap = os.path.join(text_dir, "annotations", f"{a['annotation_id']}.json")
            if os.path.exists(ap):
                anns.setdefault(a["type"], []).append(load(ap))
        details.append({"summary": inst, "detail": d, "annotations": anns})
    # critical first, then by type name, then id — deterministic
    details.sort(key=lambda x: (x["summary"].get("type") != "critical", x["summary"].get("type") or "", x["summary"]["id"]))
    return text, details


def placeholder_reason(code: str, content: str) -> str | None:
    """Upstream test data: a Tibetan-language instance whose content is not Tibetan."""
    if code == "bo":
        letters = [ch for ch in content if ch.isalpha()]
        tib = sum(1 for ch in letters if 0x0F00 <= ord(ch) <= 0x0FFF)
        if not letters or tib / len(letters) < 0.5:
            return f"content is not Tibetan script ({content[:40]!r}) — placeholder upstream"
    return None


def build_blocks(content: str, seg_ann: dict | None):
    """Return (blocks, stats). blocks: list of (block_no|None, text, segment_id|None)."""
    stats = {"segments": 0, "empty_segments": 0, "uncovered_gaps": 0, "uncovered_chars": 0,
             "gaps_attached": 0, "overlaps": 0, "out_of_range": 0}
    blocks = []

    def add_gap(gap):
        g = gap.strip()
        if not g:
            return
        stats["uncovered_gaps"] += 1
        stats["uncovered_chars"] += len(g)
        if not re.search(r"\w", g) and blocks and blocks[-1][0] is not None:
            # punctuation the previous span stopped just short of (e.g. a text-final ".")
            n_, txt_, sid_ = blocks[-1]
            blocks[-1] = (n_, txt_ + g, sid_)
            stats["gaps_attached"] += 1
        else:
            blocks.append((None, normalise_block(gap), None))
    if seg_ann and seg_ann.get("data"):
        segs = sorted(seg_ann["data"], key=lambda s: (s["span"]["start"], s["span"]["end"]))
        stats["segments"] = len(segs)
        pos, n = 0, 0
        for s in segs:
            a, b = s["span"]["start"], s["span"]["end"]
            if a < 0 or b > len(content) or b < a:
                stats["out_of_range"] += 1
            if a > pos:
                add_gap(content[pos:a])
            elif a < pos:
                stats["overlaps"] += 1
            txt = normalise_block(content[a:b])
            if not txt:
                stats["empty_segments"] += 1
            else:
                n += 1
                blocks.append((n, txt, s["id"]))
            pos = max(pos, b)
        add_gap(content[pos:])
    else:
        n = 0
        for line in content.split("\n"):
            txt = normalise_block(line)
            if txt:
                n += 1
                blocks.append((n, txt, None))
    return blocks, stats


def render_text_file(text: dict, inst: dict, api_base: str, categories: dict, downloaded: str,
                     root_file: str | None = None) -> tuple[str, dict, list]:
    """Render one instance of one text. Returns (markdown, catalog_row, block_map)."""
    code = text.get("language") or ""
    detail = inst["detail"]
    meta_i = detail.get("metadata") or {}
    content = detail.get("content") or ""
    seg_anns = inst["annotations"].get("segmentation") or []
    seg_ann = max(seg_anns, key=lambda a: len(a.get("data") or [])) if seg_anns else None
    blocks, stats = build_blocks(content, seg_ann)

    language, lang_tag, script = language_fields(code, content)
    title, title_lang = pick_title(text.get("title"), code)
    alt_same = [t.get(title_lang) for t in (text.get("alt_titles") or []) if title_lang and t.get(title_lang)]
    other_titles = [f"{k}: {v}" for k, v in (text.get("title") or {}).items() if k != title_lang and v]
    other_titles += [f"{k}: {v}" for t in (text.get("alt_titles") or []) for k, v in t.items()
                     if k != title_lang and v]

    by_role = defaultdict(list)
    for c in text.get("contributions") or []:
        role = c.get("role") or "contributor"
        label = person_label(c, code) if (c.get("person_id") or c.get("person_name")) else ai_label(c)
        if label:
            by_role[ROLE_KEYS.get(role, role)].append(label)

    cat = categories.get(text.get("category_id") or "", {})
    cat_label = " / ".join(x for x in (cat.get("title_en"), cat.get("title_bo")) if x) or None
    is_edition = root_file is not None
    ann_ids = {t: [a["id"] for a in lst] for t, lst in inst["annotations"].items()}
    seg_source = (f"openpecha-v2 segmentation annotation {seg_ann['id']} — one block per segment, in span order"
                  if seg_ann else "none upstream — one block per non-empty line of the content")

    other_ids = []
    if text.get("wiki"):
        other_ids.append(f"wiki: {text['wiki']}")
    if meta_i.get("wiki"):
        other_ids.append(f"instance wiki: {meta_i['wiki']}")

    desc = (f"Downloaded {downloaded} from the OpenPecha backend API v2 (old production backend, "
            f"openpecha-backend `main`; {api_base}). Text {text['id']}, instance {meta_i.get('id')} "
            f"({meta_i.get('type')}); upstream source: {meta_i.get('source') or 'not recorded'}. "
            f"Raw API responses: 0-INBOX/raw-data/openpecha-api/texts/{text['id']}/.")

    fm = [
        ("title", title or ""),
        ("alt_titles", alt_same or None),
        ("other_titles", other_titles or None),
        ("author", "; ".join(by_role.pop("author", [])) or ""),
    ]
    fm += [(role, "; ".join(names)) for role, names in sorted(by_role.items())]
    fm += [
        ("date", ""),
        ("language", language),
        ("script", script),
        ("file_type", "edition" if is_edition else "root-text"),
        ("lang_tag", lang_tag),
        ("root_text", f"1-SOURCES/Text/{root_file}" if is_edition else None),
        ("total_verses", sum(1 for b in blocks if b[0] is not None)),
        ("verse_id_format", "verse"),
        ("segmentation_source", seg_source),
        ("edition_type", meta_i.get("type") or ""),
        ("license", text.get("license") or ""),
        ("copyright", text.get("copyright") or ""),
        ("source", meta_i.get("source") or ""),
        ("source_url", f"{api_base}/v2/instances/{meta_i.get('id')}?content=true&annotation=true"),
        ("source_description", desc),
        ("bdrc_work_id", text.get("bdrc") or ""),
        ("bdrc_instance_id", meta_i.get("bdrc") or None),
        ("other_ids", other_ids or None),
        ("incipit_title", json.dumps(meta_i["incipit_title"], ensure_ascii=False) if meta_i.get("incipit_title") else None),
        ("colophon", meta_i.get("colophon") or None),
        ("category", cat_label),
        ("openpecha_v2_text_id", text["id"]),
        ("openpecha_v2_instance_id", meta_i.get("id")),
        ("openpecha_v2_type", text.get("type")),
        ("openpecha_v2_language", code),
        ("openpecha_v2_category_id", text.get("category_id") or ""),
        ("openpecha_v2_date", text.get("date") or ""),
        ("openpecha_v2_target", text.get("target") or None),
        ("openpecha_v2_annotations", [f"{t}: {', '.join(ids)}" for t, ids in sorted(ann_ids.items())] or None),
        ("status", "ingested"),
    ]

    body = [f"# {title or text['id']} ^0", ""]
    for n, txt, _ in blocks:
        body.append(f"{txt} ^{n}" if n is not None else txt)
        body.append("")
    md = render_frontmatter(fm) + "\n" + "\n".join(body).rstrip("\n") + "\n"

    row = {
        "text_id": text["id"], "instance_id": meta_i.get("id"), "edition_type": meta_i.get("type"),
        "file_type": "edition" if is_edition else "root-text",
        "title": title, "title_lang": title_lang, "other_titles": other_titles,
        "author": fm[3][1], "contributions": text.get("contributions") or [],
        "language": code, "lang_tag": lang_tag, "script": script,
        "openpecha_type": text.get("type"), "category_id": text.get("category_id"), "category": cat_label,
        "bdrc_work_id": text.get("bdrc"), "bdrc_instance_id": meta_i.get("bdrc"), "wiki": text.get("wiki"),
        "license": text.get("license"), "copyright": text.get("copyright"),
        "source": meta_i.get("source"), "content_chars": len(content),
        "segmentation_id": seg_ann["id"] if seg_ann else None,
        "blocks": sum(1 for b in blocks if b[0] is not None), "segmentation_stats": stats,
        "annotations": ann_ids,
    }
    block_map = [{"block": n, "segment_id": sid} for n, _, sid in blocks if n is not None]
    return md, row, block_map


# --------------------------------------------------------------------------- corpus

def convert_corpus(raw_dir: str, out_dir: str, catalog_json: str, block_map_dir: str):
    manifest = load(os.path.join(raw_dir, "manifest.json")) if os.path.exists(os.path.join(raw_dir, "manifest.json")) else {}
    api_base = manifest.get("api_base", "https://api-aq25662yyq-uc.a.run.app")
    downloaded = (manifest.get("finished") or manifest.get("started") or "")[:10]
    categories = {c["id"]: c for c in load(os.path.join(raw_dir, "categories.json"))}

    bundles, skipped, skipped_instances = [], [], []
    for tid in sorted(os.listdir(os.path.join(raw_dir, "texts"))):
        tdir = os.path.join(raw_dir, "texts", tid)
        if not os.path.exists(os.path.join(tdir, "text.json")):
            continue
        text, details = read_text_bundle(tdir)
        usable = []
        for d in details:
            content = d["detail"].get("content") or ""
            why = placeholder_reason(text.get("language") or "", content) if content.strip() else "no content"
            if why:
                skipped_instances.append({"text_id": tid, "instance_id": d["summary"]["id"],
                                          "edition_type": d["summary"].get("type"), "reason": why})
            else:
                usable.append(d)
        titles = {(v or "").strip().casefold() for v in (text.get("title") or {}).values()}
        reason = ("titled 'Delete this' upstream" if titles & EXCLUDED_TITLES else
                  "no instance" if not details else
                  "no usable content (see skipped_instances)" if not usable else None)
        if reason:
            skipped.append({"text_id": tid, "title": text.get("title"), "language": text.get("language"),
                            "type": text.get("type"), "reason": reason})
            continue
        bundles.append((text, usable))

    # filenames: <lang_tag>-<title>[-<edition_type>].md; any clash gets " (<text_id>)" on every member
    def base_name(text, inst, idx):
        code = text.get("language") or ""
        content = inst["detail"].get("content") or ""
        _, tag, _ = language_fields(code, content)
        title, _ = pick_title(text.get("title"), code)
        stem = f"{tag}-{safe_filename_title(title or text['id'])}"
        if idx > 0:
            stem += f"-{inst['summary'].get('type') or 'edition'}"
        return stem

    planned = []
    for text, usable in bundles:
        for idx, inst in enumerate(usable):
            planned.append((text, inst, idx, base_name(text, inst, idx)))
    clash = Counter(p[3].casefold() for p in planned)
    names = {}
    for text, inst, idx, stem in planned:
        if clash[stem.casefold()] > 1:
            stem = f"{stem} ({text['id']})"
        names[(text["id"], inst["summary"]["id"])] = stem + ".md"

    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(block_map_dir, exist_ok=True)
    rows = []
    for text, usable in bundles:
        root_file = names[(text["id"], usable[0]["summary"]["id"])]
        for idx, inst in enumerate(usable):
            fname = names[(text["id"], inst["summary"]["id"])]
            md, row, bmap = render_text_file(text, inst, api_base, categories, downloaded,
                                             root_file=root_file if idx > 0 else None)
            with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
                f.write(md)
            row["file"] = f"1-SOURCES/Text/{fname}"
            rows.append(row)
            bm_name = f"{text['id']}.json" if idx == 0 else f"{text['id']}.{inst['summary']['id']}.json"
            with open(os.path.join(block_map_dir, bm_name), "w", encoding="utf-8") as f:
                json.dump({"file": row["file"], "text_id": text["id"], "instance_id": row["instance_id"],
                           "segmentation_id": row["segmentation_id"], "blocks": bmap},
                          f, ensure_ascii=False, indent=0)

    rows.sort(key=lambda r: (r["lang_tag"], safe_filename_title(r["title"]).casefold(), r["text_id"]))
    catalog = {
        "corpus": "OpenPecha backend API v2 — original texts (types root, translation_source, none)",
        "api_base": api_base, "api_version": manifest.get("api_version"), "downloaded": downloaded,
        "generated_by": "4-SYSTEM/Skills/json-to-source-text/converters/openpecha_api_v2.py",
        "files": len(rows), "skipped": skipped, "skipped_instances": skipped_instances, "texts": rows,
    }
    with open(catalog_json, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=1)
    write_catalog_md(rows, skipped, catalog, os.path.join(out_dir, "📑 Text_catalog.md"),
                     os.path.relpath(catalog_json, os.path.dirname(os.path.dirname(os.path.abspath(out_dir)))))
    return rows, skipped


def write_catalog_md(rows, skipped, catalog, path, catalog_rel):
    """Human-readable catalog beside the texts (About Sources.md §2, catalog files)."""
    def cell(s):
        return (s or "").replace("|", "\\|").replace("\n", " ")

    by_lang = Counter(r["lang_tag"] for r in rows)
    by_cat = Counter(r["category"] or "—" for r in rows)
    out = [
        "---",
        "title: Text catalog — OpenPecha API v2 original texts",
        "file_type: reference",
        f"generated_from: {catalog_rel}",
        f"source_description: \"Generated {catalog['downloaded']} by openpecha_api_v2.py from the "
        f"OpenPecha backend API v2 download in 0-INBOX/raw-data/openpecha-api/. Regenerate, do not hand-edit.\"",
        "---",
        "",
        "# Text catalog — OpenPecha API v2 original texts",
        "",
        f"{len(rows)} files, one per text (plus any extra edition), downloaded {catalog['downloaded']} from "
        f"`{catalog['api_base']}`. `OP type` is the backend's relation-derived type: `root` has commentaries, "
        "`translation_source` has translations, `none` stands alone. Author is as recorded upstream; "
        "blank means the backend records none.",
        "",
        "**By language:** " + " · ".join(f"`{k}` {v}" for k, v in sorted(by_lang.items())),
        "",
        "**By category:** " + " · ".join(f"{k} {v}" for k, v in by_cat.most_common()),
        "",
        "| # | Text | Author | Lang | Category | OP type | BDRC work | Blocks | OP text ID |",
        "|---|------|--------|------|----------|---------|-----------|--------|------------|",
    ]
    for i, r in enumerate(rows, 1):
        target = r["file"][:-3]
        out.append(f"| {i} | [[{target}\\|{cell(r['title'])}]] | {cell(r['author'])} | {r['lang_tag']} | "
                   f"{cell(r['category'])} | {r['openpecha_type']} | {r['bdrc_work_id'] or ''} | "
                   f"{r['blocks']} | `{r['text_id']}` |")
    if skipped or catalog.get("skipped_instances"):
        out += ["", "## Not converted", "",
                "Present in the backend but not written to `1-SOURCES/Text/`. Their raw API responses are "
                "kept in `0-INBOX/raw-data/openpecha-api/texts/<id>/`.", "",
                "| OP text ID | Title | Lang | OP type | Reason |", "|---|---|---|---|---|"]
        for s in skipped:
            t = next((v for v in (s["title"] or {}).values() if v), "")
            out.append(f"| `{s['text_id']}` | {cell(t)} | {s['language']} | {s.get('type') or ''} | {s['reason']} |")
    extra = catalog.get("skipped_instances") or []
    if extra:
        out += ["", "Instances left out (the text itself may still be converted from another instance):", "",
                "| OP text ID | OP instance ID | Edition | Reason |", "|---|---|---|---|"]
        out += [f"| `{x['text_id']}` | `{x['instance_id']}` | {x['edition_type']} | {cell(x['reason'])} |" for x in extra]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


def convert_json_to_source_text(json_path: str, output_path: str) -> None:
    """Skill contract: json_path is one text's text.json inside a download folder."""
    tdir = os.path.dirname(os.path.abspath(json_path))
    raw_dir = os.path.dirname(os.path.dirname(tdir))
    manifest_p = os.path.join(raw_dir, "manifest.json")
    manifest = load(manifest_p) if os.path.exists(manifest_p) else {}
    categories = {c["id"]: c for c in load(os.path.join(raw_dir, "categories.json"))}
    text, details = read_text_bundle(tdir)
    usable = [d for d in details if (d["detail"].get("content") or "").strip()]
    if not usable:
        sys.exit(f"{text['id']}: no instance with content")
    md, _, _ = render_text_file(text, usable[0], manifest.get("api_base", ""), categories,
                                (manifest.get("finished") or "")[:10])
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)


def main():
    ap = argparse.ArgumentParser(description="OpenPecha API v2 download → 1-SOURCES/Text markdown")
    ap.add_argument("--corpus", action="store_true", help="convert a whole download folder")
    ap.add_argument("src", help="download folder (--corpus) or one text.json")
    ap.add_argument("dst", help="output folder (--corpus) or output .md")
    ap.add_argument("--catalog", help="catalog JSON path (default: <vault>/1-SOURCES/openpecha-v2-catalog.json)")
    ap.add_argument("--block-maps", help="block-map folder (default: <src>/block-maps)")
    a = ap.parse_args()
    if not a.corpus:
        convert_json_to_source_text(a.src, a.dst)
        return
    vault = os.path.dirname(os.path.dirname(os.path.abspath(a.dst)))
    catalog = a.catalog or os.path.join(vault, "1-SOURCES", "openpecha-v2-catalog.json")
    bmaps = a.block_maps or os.path.join(a.src, "block-maps")
    rows, skipped = convert_corpus(a.src, a.dst, catalog, bmaps)
    print(f"{len(rows)} files written to {a.dst}; {len(skipped)} texts skipped")
    for k, v in Counter(x["reason"] for x in skipped).items():
        print(f"  skipped — {k}: {v}")
    agg = Counter()
    for r in rows:
        for k, v in r["segmentation_stats"].items():
            agg[k] += v
    print("segmentation totals:", dict(agg))
    print("no upstream segmentation:", sum(1 for r in rows if not r["segmentation_id"]))


if __name__ == "__main__":
    main()
