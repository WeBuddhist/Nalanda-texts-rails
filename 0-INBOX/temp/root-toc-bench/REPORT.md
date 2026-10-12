# Root-text TOC on Gemini 3.8 Flash — thinking low / medium / high (2026-10-12)

Runner: `4-SYSTEM/scripts/seg-toc-benchmark/root_toc_gemini.py` (same prompt files and passes as
`root-text-toc-extract`, one API call per subagent). Score: `score_root_toc.py`, out of 1 =
0.4 structure (top two levels, title + parent) + 0.3 coverage (all nodes by title) + 0.3 anchors
(found in the text by pass 6). Reference = the Opus tree from the batch (QC-clean against the
text) — not a human gold.

| Text | Level | Nodes (ref) | Structure | Coverage | Anchors | **Score** | Cost | Time |
|---|---|---|---|---|---|---|---|---|
| Ar_3CC2 (707 lines, 6 chunks) | low | 10 (10) | 1.000 | 1.000 | 1.000 | **1.000** | $0.05 | 17 s |
| | medium | 12 | 0.000 | 0.909 | 1.000 | **0.573** | $0.25 | 2.7 min |
| | high | 12 | 0.000 | 0.909 | 1.000 | **0.573** | $1.31 | 11.7 min |
| As_3CDk_ (5,192 lines, 42 chunks) | low | 198 (156) | 0.000 | 0.463 | 0.914 | **0.413** | $0.98 | 3.2 min |
| | medium | 64 | 0.632 | 0.473 | 0.906 | **0.666** | $2.42 | 15.5 min |
| | high | 54, no anchors | 0.632 | 0.448 | 0 | **0.387** | $9.83 | failed |

What went wrong, per run:
- Ar_3CC2 medium / high: the 10 parts are right, but wrapped under `1. ཀླད་ཀྱི་དོན / 2. གཞུང་དངོས`
  — the segmenter's own editorial `##` headings in prepared.md, taken as text. An input problem
  (strip or flag those headings before sending), not a reading error.
- As_3CDk_ low: took the opening list of all 17 bhūmis as the tree (1 part, 17 children); 14 of
  them are not in this volume, so 16 anchors fail and the real 3-part structure is missing.
- As_3CDk_ medium: right top two levels (II. + 3 parts, sub-parts as Opus) but shallow — 64 nodes
  vs 156; misses 2.6/2.7 and most level-3 nodes; 6 unresolved anchors.
- As_3CDk_ high: same tree as medium at pass 3 (54 nodes); pass 5 failed 4 times — reading the
  whole text (216k tokens) its thinking used the full 65,536-token output budget, no answer.
  Pass 3 also used 62.9k of the budget.

## After the input fix (segmenter `#` headings blanked, root-side note) — 2026-10-12

Column "Nodes" = nodes in the Gemini tree; the Opus reference has 10 (Ar_3CC2) / 156 (As_3CDk_).

| Text | Setting | Before | **After** | Nodes | Cost | Wall time |
|---|---|---|---|---|---|---|
| Ar_3CC2 | 3.8 Flash medium | 0.573 | **0.930** | 10 | $0.36 | 6 min |
| | 3.8 Flash high | 0.573 | **0.930** | 10 | $1.35 | 22 min |
| | 3.1 Flash-Lite medium | 0.723 | 0.474 | 36 | $0.05 | 36 s |
| | 3.1 Flash-Lite high | 0.531 | **0.963** | 9 (misses part 1) | $0.07 | 53 s |
| As_3CDk_ | 3.8 Flash low | 0.407 | **0.645** | 58 | $0.91 | 2.2 min |
| | 3.8 Flash medium | 0.666 | **0.672** | 73 | $2.77 | 20 min |
| | 3.1 Flash-Lite high | 0.426 | 0.432 | 72 (17 bhūmis as parts) | $0.98 | 5.2 min |

Pass 5 runs in text windows (60,000 characters, 20 lines overlap) for a text that does not fit
one window. 3.8 Flash high on As_3CDk_ still fails pass 5 (thinking fills the 65,536-token
output limit even on a 44k-token window). Single runs: run-to-run variance is not measured.
