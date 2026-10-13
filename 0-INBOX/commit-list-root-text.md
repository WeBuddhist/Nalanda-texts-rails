# Commit list — root-text work (2026-10-05)

Pick what to commit. Paths are relative to the vault root. Nothing here is committed yet.
`?? ` = new (untracked), ` M ` = modified.

---

## A. Root-text skills (the split)

| status | path | what |
|---|---|---|
| ?? | `4-SYSTEM/Skills/root-text-segmentation/SKILL.md` | **new skill** — procedure, rules, completion check |
| ?? | `4-SYSTEM/Skills/root-text-segmentation/scripts/root_text_build.py` | classify / prepare / finish script |
| ?? | `4-SYSTEM/Skills/root-text-segmentation/prompts/stanza-grouping.md` | sense-mode stanza grouping prompt |
| ?? | `.claude/commands/root-text-segmentation.md` | slash-command registration |
| ?? | `4-SYSTEM/Skills/toc-tree-extraction/prompts/pass1-candidates-root.md` | TOC mode `root` — pass 1 with Type D |
| ?? | `4-SYSTEM/Skills/toc-tree-extraction/` *(whole folder, 15 files)* | the folder is new to the repo; its `SKILL.md` now documents mode `root` |
| ?? | `4-SYSTEM/Skills/toc-tree-ingest/` *(whole folder, 2 files)* | shared by both sides; footnote-ID fix, `\n` repair, duplicate-title warning |
| ?? | `.claude/commands/toc-tree-extraction.md`, `.claude/commands/toc-tree-ingest.md` | their registrations |
| M | `4-SYSTEM/Skills/SKILLS-CATALOG.md` | adds `root-text-segmentation`; notes mode `root` and v2.1 — ⚠ this file was already modified before this session, so the diff also contains those earlier catalog changes |

```bash
git add 4-SYSTEM/Skills/root-text-segmentation .claude/commands/root-text-segmentation.md \
        4-SYSTEM/Skills/toc-tree-extraction .claude/commands/toc-tree-extraction.md \
        4-SYSTEM/Skills/toc-tree-ingest .claude/commands/toc-tree-ingest.md \
        4-SYSTEM/Skills/SKILLS-CATALOG.md
```

---

## B. Root-text outputs — `Ar_3CBe_` (Āryadeva, *Vajraghaṇṭā pūjā krama*)

Translated from Sanskrit (`རྒྱ་གར་སྐད་དུ།`), so the skill produces two versions.

| path | what |
|---|---|
| `0-INBOX/Ar_3CBe_-root/final-sloka.md` | **version 1 — śloka**: 32 stanzas, 4 pādas per block (94% quatrains) |
| `0-INBOX/Ar_3CBe_-root/final-free.md` | **version 2 — free / by sense**: 33 stanzas |
| `0-INBOX/Ar_3CBe_-root/` *(prepared.md, group-in.md, groups-sloka.json, groups-free.json, tree-top.*, state.json)* | working files (optional) |
| `0-INBOX/Ar_3CBe_-root-even/final.md` | the extra even-emphasis comparison (not produced by the skill) — optional |
| `0-INBOX/toc-candidates-Ar_3CBe_.md`, `toc-enumerations-…`, `toc-tree-…`, `toc-tree-qc-…` | TOC passes 1–4 (mode `root`) |
| `0-INBOX/temp/TOC-Ar_3CBe_/` *(8 files)* | chunk outputs + the anchored tree used for the headings |

```bash
# the two versions only:
git add 0-INBOX/Ar_3CBe_-root/final-sloka.md 0-INBOX/Ar_3CBe_-root/final-free.md
# with working files and the TOC run:
git add 0-INBOX/Ar_3CBe_-root 0-INBOX/toc-*-Ar_3CBe_.md 0-INBOX/temp/TOC-Ar_3CBe_
```

## C. Root-text benchmarks and survey

| path | what |
|---|---|
| `0-INBOX/bench-liturgy/` | verse-stanza benchmark on 10 Liturgy-rails texts: gold, inputs, both prompts' outputs, `score.py` (P-new F1 0.95 vs 0.68), `build.py`, `picks.txt` |
| `0-INBOX/text-genre-survey.json` | all 565 Nalanda texts classified by title + content (commentary / verse / prose) |

```bash
git add 0-INBOX/bench-liturgy 0-INBOX/text-genre-survey.json
```

---

## D. Commentary side — NOT root-text (listed so you can decide separately)

| status | path | what |
|---|---|---|
| ?? | `4-SYSTEM/Skills/commentary-segmentation/` (+ `.claude/commands/commentary-segmentation.md`) | v2.1 `--stanza-breaks` |
| ?? | `4-SYSTEM/Skills/block-resegmentation/` (+ command) | overlap-reconciler fix |
| ?? | `4-SYSTEM/Skills/commentary-resegment/`, `4-SYSTEM/Skills/toc-candidate-extraction/` (+ commands) | imported before this session, unchanged by it |
| ?? | `4-SYSTEM/scripts/seg-toc-benchmark/` | benchmark scripts + HANDOFF.md |
| ?? | `0-INBOX/seg-toc-bench/` | benchmark bundle + results (8.9 MB) |
| M | `.gitignore` | `.env`, `venv/` (from before this session) |

## Do NOT commit

- `0-INBOX/delete/` — caches waiting for you to delete
- `0-INBOX/commit-list-root-text.md` — this list
- any `__pycache__/`
