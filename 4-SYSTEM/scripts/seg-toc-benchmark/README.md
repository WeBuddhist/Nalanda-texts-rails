# Segmentation + TOC benchmark

Measures how close the segmentation and TOC skills get to commentaries that people have
segmented, outlined and ingested **by hand**.

**Method.** Take a gold file (human-processed commentary). Strip every heading, root-text
transclusion and block ID, and merge all content into one run (`make_input.py`). Run the
skills on that input. Score the result against the gold (`score.py`). Everything is
measured in the *squeezed content stream* (all text with whitespace removed), so layout,
transclusions and IDs never disturb the alignment.

## Tools

| Script | Does |
|---|---|
| `make_input.py <gold> <out>` | gold → merged benchmark input (checks the text is identical) |
| `score.py <gold> <pred> [--json f] [--label s]` | the scorecard (below) |
| `diff_report.py <gold> <pred>` | every missed / spurious boundary and displaced heading, with context |
| `seg_matrix.py --gold-dir D --root R [--old S]` | deterministic segmentation over **all** gold files — the overfitting check (no LLM calls) |
| `claude_reseg_shim.py dump\|stage` | runs `commentary-resegment`'s Gemini windows with Claude subagents |
| `claude_generate_shim.py --dir D -- <script> …` | runs any skill script's `_generate()` Gemini calls with Claude (prompt files out, response files in) |
| `variant.py seg\|ingest\|reseg\|qc\|finish\|rescore <ver>` | runs a pipeline **variant** over the 8-file set (`0-INBOX/bench8/config.json`); every LLM prompt is hashed and an identical earlier prompt reuses its answer, so a variant differs from v1 only where its change reaches |
| `compare.py <stage> v1 v1.1 …` | per-file and mean scores of several variants at one stage (`1-segmented`, `2-after-ingest`, `4-final`) |
| `merge_trees.py <numbered> <frame> <out>` | numbered nodes of one anchored tree + frame nodes of another |
| `repeat_report.py <fid> <ref> <run>…` | variation across independent repeats of one commentary: per-metric mean/sd/min/max, boundary and heading stability, flip map. Repeats are variants named e.g. `v2-r1…r5`, run with `BENCH_FILES=<fid> BENCH_NO_CACHE=1` so the model is re-asked |
| `reuse_answers.py <fid> <from-ver> <to-ver>` | copies one run's LLM answers into another wherever the prompt is byte-identical (pins the source run, unlike the global cache) |
| `gemini_answer.py <prompt-files-or-dirs>` | answers prompt files with the Gemini API (same system + user prompts the skills send); thinking_level, JSON mode, cut-off detection, token/time log; key from the vault-root `.env` |
| `gemini_bench.py [--files …] [--levels low high] [--runs 3]` | one-command Gemini benchmark: full pipeline per run, scored against gold and the Opus baseline → `0-INBOX/bench8/gemini-<model>-report.md` |
| `test_reorder.py <tree> <segmented> [--parents N] [--seed S]` | shuffles the sibling order of a correct anchored tree and checks `toc_tree_ingest` restores the text order exactly |

## Scorecard

| Metric | Meaning |
|---|---|
| boundary P/R/F1 | block boundaries vs gold (exact position) |
| block exact-match | share of gold blocks reproduced exactly |
| stanzas whole | share of gold verse blocks reproduced exactly |
| heading title P/R/F1 | sa bcad headings matched by normalised title |
| placement exact | matched headings inserted at exactly the gold position |
| id / level / parent | heading block ID, markdown level, parent node vs gold |
| title exact | heading text identical (ordinal + final `།` included) |
| editorial | frame headings (`^I-0`, `^a-0`, `^b-1-0` …): recall, placement, ID |
| spacing | whitespace inside blocks vs gold (Jaccard) and `། །` count — the source's own punctuation |
| body ids | `^N-n` IDs on blocks that match the gold exactly |
| **composite** | mean of: boundary F1, heading F1, placement × recall, id × recall |

Heading precision counts every non-frame predicted heading, plus any frame heading a gold
numbered heading was matched to (Drakpa's gold numbers its colophon `3 མཛད་བྱང།`).

## Variants (one change at a time)

`config.json` declares per file: input, v1 tree, gold, `quotes` (separate / inline) and
`headings` (sabcad / verses / top), and per variant: extra segmentation flags, a tree
source, extra ingest flags. Stage `2-after-ingest` is deterministic given the tree, so it
is the noise-free comparison; `4-final` adds the re-asked LLM windows.

## Running one iteration

```bash
G="<gold file>"; I=1-SOURCES/Commentaries/<id>.md
python3 4-SYSTEM/scripts/seg-toc-benchmark/make_input.py "$G" "$I"
# … run commentary-segment → commentary-toc-extract (1–5) → commentary-toc-ingest →
#   commentary-resegment → commentary-block-ids, as the SKILL.md files say (or commentary-pipeline) …
python3 4-SYSTEM/scripts/seg-toc-benchmark/score.py "$G" <final.md> --label vN --json scores.json
python3 4-SYSTEM/scripts/seg-toc-benchmark/diff_report.py "$G" <final.md>
# and always the held-out check before calling a rule change an improvement:
python3 4-SYSTEM/scripts/seg-toc-benchmark/seg_matrix.py --gold-dir <gold dir> --root <root text>
```

Reports of past iterations: `21-taras-rails/0-INBOX/benchmark-seg-toc/`.
