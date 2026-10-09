# Segmentation + TOC — handoff (2 Oct 2026)

Where the work on the segmentation, TOC-extraction and TOC-ingest skills stands, for continuing in Claude Code.

## Rule that stays in force
**Never open, read, print, copy or modify `.env`.** It holds `GEMINI_API_KEY`. Scripts load the key themselves (`_gemini_api_key()`: environment first, then the vault-root `.env`, reading only `GEMINI_API_KEY`/`GOOGLE_API_KEY`). Running a script that loads it is fine. `.env` and `venv/` are in `.gitignore`; `.env` was never committed. Suggested `.claude/settings.json` rule: `{"permissions": {"deny": ["Read(./.env)", "Read(./.env.*)"]}}`.

Standing working rule: after a benchmark report, wait for the user's command.

## The pipeline (skills in `4-SYSTEM/Skills`)
1. **Segmentation** (deterministic): `commentary-segment/scripts/segment_commentary.py --units --root R --enum-chain broad --quotes separate|inline --colophon-guard`
2. **TOC tree** (LLM, `commentary-toc-extract`): mode per commentary —
   - `sabcad`: passes 1–5 (pass 5 = anchors)
   - `verses` / `top`: `prompts/verse-headings.md`, then frame nodes (I., II., a., b.) from pass 5 merged in with `merge_trees.py`
3. **Ingest** (deterministic): `Skills/seg-toc-lib/toc_tree_ingest.py parse | ingest --split-frame-nodes`
4. **Re-segmentation** (LLM): `commentary-resegment/scripts/resegment.py`, windows of 40 blocks with overlap; `[VERSE]`/`[HEADING]` blocks protected
5. **QC** (LLM): `qc_check.py`
6. **Body IDs**: `--stamp-body-ids`

Per-commentary settings: `quotes` (separate|inline), `headings` (sabcad|verses|top).

## What changed (all already in the Nalanda repo)
- **TOC reorder to text order** (`toc_tree_ingest.py`): if the commentary treats subtopics in a different order than its outline announces, siblings are reordered to match the text. Titles stay exactly as the commentary words them. Block IDs keep the *announced* order (གཉིས་པ་ keeps 1-2-0 even if it comes first) and a NOTE is printed whenever this happens. Options: `--renumber-reordered`, `--keep-tree-order`, subcommand `reorder --out-md`. Shuffle test `test_reorder.py`: 112/112.
- **pass5-anchors.md**: anchor each node where it really begins, even out of order (the ingest reorders).
- **verse-headings.md** (verses + top modes): pinned the ambiguous rules — wrap-up stays inside the praise unless titled; benefits always one part (root-mantra verse and root colophon inside it); top mode follows the root text's own sections (`1. བསྟོད་པ་དངོས།`, `2.` benefits named as the commentary names it, `3. མཛད་བྱང།` only if the colophon is explained); front-matter outline → `II. བསྟོད་པའི་ས་བཅད།` without children.
- **resegment.py**: SECOND LEVEL rule (passages opening སྦས་དོན་ནི། / ངེས་དོན་ནི། / ཟབ་དོན་ནི། etc. are their own block); overlap reconciler accepts a larger merge when it agrees with each window's visible part (cleaner logs only — measured: no merges were being lost with Opus).
- **Gemini key loader** in 7 scripts (commentary-resegment `list_models/qc_check/resegment` — formerly block-resegmentation —, the old line-wise commentary-resegment `resegment` (now in 0-INBOX/delete), `extract_toc_candidates`, `extract_toc_tree`, `find_toc_contexts`).
- **Benchmark scripts** `4-SYSTEM/scripts/seg-toc-benchmark/`: `variant.py` (seg|ingest|reseg|qc|finish|rescore; `BENCH_FILES`, `BENCH_NO_CACHE`; Windows-safe), `merge_trees.py`, `reuse_answers.py`, `repeat_report.py`, `test_reorder.py`, `gemini_answer.py`, `gemini_bench.py`.

## Benchmark
8 human-processed Tārā commentaries (gold from 21-taras-rails). Composite = mean(boundary F1, heading F1, placement × recall, ID × recall).
Self-contained bundle with inputs, gold and Opus results: `0-INBOX/seg-toc-bench/` (see its `RUN-ME.md`).

| step | result |
|---|---|
| v0 → v1 → v2 (variants v1.1–1.4 combined) | reports in project `benchmark/` |
| Run-to-run variation (Opus) | spread came from prompt ambiguity; after pinning prompts ±0.006 |
| Models | Opus ≈ Fable; Sonnet −0.07; Haiku unusable → **Opus chosen** |
| Opus with both fixes (`o2`) | mean **0.929** over 8 files (Padma 0.299→0.971, Drakpa 0.564→0.903) |
| Gemini 3.8 Flash, Tāranātha only | Opus 0.850 · Gemini low 0.863 · Gemini high **0.892** |

Gemini detail (Tāranātha): better headings (heading F1 0.964 high vs 0.893 Opus), worse block boundaries (0.775 vs 0.817 — each run had 5 overlap-zone merge conflicts not applied; likely the cause, unverified). Low ≈ no thinking, $0.07 / 19 s per run; high $0.65 / 7.7 min per run. No JSON errors or truncations.

## Next steps
1. Run Gemini on all 8: from `0-INBOX/seg-toc-bench`, `..\..\venv\Scripts\python.exe 4-SYSTEM\scripts\seg-toc-benchmark\gemini_bench.py --files all` → report `0-INBOX\bench8\gemini-gemini-3.8-flash-report.md`.
2. Check why Gemini's overlap windows disagree on merges (`reseg.log` / ops log in each `g38-*` run dir under `0-INBOX/bench8/<file>/`).
3. Depending on results, update production Gemini settings in the skill scripts: model `gemini-3.8-flash`; `thinking_level` instead of `thinking_budget=0`; drop `temperature=0.0`; larger `max_output_tokens` (it includes thinking); JSON mode; treat a MAX_TOKENS finish as an error. `resegment.py` still has `gemini-2.5-flash` / fallback `gemini-2.0-flash` (2.0 was shut down 1 June 2026).
4. Known weak spots: Drakpa boundary F1 0.611; frame `a. མཇུག་བྱང།` one sentence early on Drakpa; the top-mode rules were derived from the same gold files they are scored on — validate on commentaries outside the 8.

Detailed reports: claude.ai project "segmentation + toc", folder `benchmark/`; also 21-taras-rails `0-INBOX/benchmark-seg-toc/variants/`.
