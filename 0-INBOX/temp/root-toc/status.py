#!/usr/bin/env python3
"""Status of the root-text TOC batch (extract only, no ingest).

    python 0-INBOX/temp/root-toc/status.py init            # build status.json from 0-INBOX/root/
    python 0-INBOX/temp/root-toc/status.py set <id> key=value [key=value ...]
    python 0-INBOX/temp/root-toc/status.py next             # print the next text still to do
    python 0-INBOX/temp/root-toc/status.py render           # rewrite 0-INBOX/ROOT-TOC-BATCH.md

Keys: status (todo | running | done | no-parts | earlier-run | failed), size, chars, run, form, units, chunks,
parts (top-level parts), nodes (all nodes), qc4 ("before→after"), qc6 (issues / accepted),
note. Every `set` re-renders the document.
"""
import json, sys, os, re, datetime
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
ST = VAULT / "0-INBOX/temp/root-toc/status.json"
DOC = VAULT / "0-INBOX/ROOT-TOC-BATCH.md"
COLS = ["status", "form", "units", "chunks", "parts", "nodes", "qc4", "qc6", "note"]

def load(): return json.loads(ST.read_text(encoding="utf-8"))
def save(d): ST.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")

def init():
    d = {}
    for f in sorted((VAULT / "0-INBOX/root").glob("*.md")):
        i = f.stem
        toc = VAULT / f"0-INBOX/temp/TOC-{i}"
        r = {"source_lines": sum(1 for _ in f.open(encoding="utf-8")), "status": "todo"}
        if toc.is_dir():
            r["status"] = "earlier-run"
            r["note"] = ("anchored tree from an earlier run" if (toc / f"toc-tree-anchored-{i}.md").exists()
                         else "tree, not anchored (earlier run)" if (toc / f"toc-tree-{i}.md").exists()
                         else "no tree (earlier run: no parts found)")
        d[i] = r
    save(d); render(d)

def render(d=None):
    d = d or load()
    n = {k: sum(1 for r in d.values() if r["status"] == k) for k in ("todo", "running", "done", "no-parts", "earlier-run", "failed")}
    sz = {k: sum(1 for r in d.values() if r.get("size") == k) for k in ("small", "medium", "large")}
    rows = []
    for k, (i, r) in enumerate(d.items(), 1):
        tree = f"`TOC-{i}/toc-tree-anchored-{i}.md`" if r["status"] == "done" else ""
        rows.append(f"| {k} | {i} | {r.get('size', '')} | {r.get('chars', '')} | {r['source_lines']} | "
                    + " | ".join(str(r.get(c, "")) for c in COLS) + f" | {r.get('run', '')} | {tree} |")
    DOC.write_text(TEMPLATE.format(today=datetime.date.today().isoformat(), total=len(d), **n, **{f"sz_{k}": v for k, v in sz.items()},
                                   rows="\n".join(rows)), encoding="utf-8")

TEMPLATE = """# Root-text TOC batch — extract now, ingest later

Running `root-text-toc-extract` on every root text in `0-INBOX/root/`, one text at a time.
**No ingest yet**: the headings are put into the texts later, together with the updated
segmentation. This document says where everything is and how to continue.

Updated {today} · {total} texts · done {done} · no parts announced {no-parts} · earlier run {earlier-run} · failed {failed} · running {running} · **to do {todo}**

Size classes (characters of `0-INBOX/root/<id>.md`): small < 30,000 · medium 30,000–199,999 · large ≥ 200,000 — small {sz_small} · medium {sz_medium} · large {sz_large}. How to run the rest with Gemini: `0-INBOX/temp/root-toc/README.md`.

## Where things are

| What | Path |
|---|---|
| Source texts | `0-INBOX/root/<id>.md` |
| Reading copy the TOC passes read (`root-text-segment`, deterministic; overwritten when the segmentation is re-run) | `0-INBOX/temp/root-seg-v2/<id>/prepared.md` (+ `group-in.md`, `state.json`) |
| TOC working files | `0-INBOX/temp/TOC-<id>/` — `chunk-index.tsv`, `candidates/`, `enumerations/`, `toc-candidates-<id>.md`, `toc-enumerations-<id>.md`, `toc-tree-<id>.md` |
| QC reports | `0-INBOX/temp/TOC-<id>/toc-tree-qc-<id>.md` (pass 4) · `toc-tree-qc-source-<id>.md` (pass 6, against the text) |
| **The tree to ingest later** | `0-INBOX/temp/TOC-<id>/toc-tree-anchored-<id>.md` — each node ends in `[[the words where the part begins]]` |
| Instructions each text's coordinator agent follows | `0-INBOX/temp/root-toc/COORDINATOR.md` |
| This batch's status (machine-readable) | `0-INBOX/temp/root-toc/status.json` · updated with `python 0-INBOX/temp/root-toc/status.py set <id> …` |

Texts with status `no-parts` announce no parts (most prayers and chants): no tree, and their
`## གཞུང་དངོས། ^1-0` heading stays. Texts with status `earlier-run` were done before this
batch (the 22 processed ones); their folders were left as they were.

## How to continue

**Resume the extraction:** `python 0-INBOX/temp/root-toc/status.py next` prints the next text
to do; run `root-text-segment` then `root-text-toc-extract` on it (procedure below) and set its
row. A text whose `TOC-<id>/` already holds chunk files resumes where it stopped — finished
chunks are skipped.

```bash
python 4-SYSTEM/Skills/seg-toc-lib/root_text_build.py segment "0-INBOX/root/<id>.md" "0-INBOX/temp/root-seg-v2/<id>"
# then root-text-toc-extract on 0-INBOX/temp/root-seg-v2/<id>/prepared.md, id <id> (passes 1–6)
```

**Ingest later, after the segmentation update** (no model calls for the TOC):

```bash
python 4-SYSTEM/Skills/seg-toc-lib/root_text_build.py segment "0-INBOX/root/<id>.md" "0-INBOX/temp/root-seg-v2/<id>"
python 4-SYSTEM/Skills/seg-toc-lib/root_text_build.py toc-ingest "0-INBOX/temp/root-seg-v2/<id>" \
    --tree "0-INBOX/temp/TOC-<id>/toc-tree-anchored-<id>.md"     # only for texts with a tree
# check the report: "not placed: 0"; then root-text-group and root-text-block-ids
```

The anchors are the text's own words, so the tree does not go stale when the segmentation
rules change. The only thing to check at ingest is `not placed: 0` — a part whose opening
words end up mid-line under the new rules is placed by hand.

## Status

`form` verse / prose / mixed · `units` lines in the reading copy · `parts` top-level parts ·
`nodes` all nodes · `qc4` pass-4 issues before→after repair · `qc6` pass-6 result against the text.

| # | id | size | chars | source lines | status | form | units | chunks | parts | nodes | qc4 | qc6 | note | run (model · cost · time) | tree |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
{rows}
"""

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "init": init()
    elif a[0] == "render": render()
    elif a[0] == "next":
        print(next((i for i, r in load().items() if r["status"] == "todo"), "nothing left"))
    elif a[0] == "set":
        d = load(); r = d[a[1]]
        for kv in a[2:]:
            k, v = kv.split("=", 1); r[k] = v
        save(d); render(d)
