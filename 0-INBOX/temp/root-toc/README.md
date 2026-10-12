# Root-text TOC batch on Gemini — how to run it from the command line

Builds the TOC tree (passes 1–6 of `root-text-toc-extract`, **no ingest**) for every root
text in `0-INBOX/root/` that is still to do, on the Gemini API. No Claude needed.

Progress and results: **`0-INBOX/ROOT-TOC-BATCH.md`** (re-written after every text).

## What runs where

| Mode | Texts | Model | Estimate for all remaining |
|---|---|---|---|
| `--mode low` | small + medium (< 200,000 characters) | gemini-3.8-flash, thinking **low** | ≈ $15–20, ≈ 1 h at 3 at a time |
| `--mode medium` | large (≥ 200,000 characters) | gemini-3.8-flash, thinking **medium** | ≈ $95–130, ≈ 4–5 h at 3 at a time |

Size classes: small < 30,000 · medium 30,000–199,999 · large ≥ 200,000 characters of
`0-INBOX/root/<id>.md` (set once by `categorise.py`).

Benchmark (see `0-INBOX/temp/root-toc-bench/REPORT.md`): on small and medium texts thinking
low got the top-level parts right on most texts; on the large treatise volumes even medium
got them right on only 1 of 3. **Review the top-level parts of every large text** (and
check notes marked REVIEW) before ingest.

## Before the first run (once)

1. Open a terminal in the vault folder:
   ```
   cd D:\Work\OpenPecha\Nalanda-texts-rails
   ```
2. The Gemini key must be in the `.env` file at the vault root (`GEMINI_API_KEY=...`) or
   in the environment. The scripts read it themselves; nothing prints it.
3. Use the vault's venv (it has `google-genai`): `venv\Scripts\python.exe`.
4. The size classes are already set. Only if new texts were added to `0-INBOX/root/`:
   ```
   venv\Scripts\python.exe -X utf8 0-INBOX\temp\root-toc\status.py init
   venv\Scripts\python.exe -X utf8 0-INBOX\temp\root-toc\categorise.py
   ```
   (`init` rebuilds the status list from scratch — it forgets results; do not run it
   once the batch is under way unless you mean to.)

## Run

Small + medium texts (3 texts at a time):
```
venv\Scripts\python.exe -X utf8 0-INBOX\temp\root-toc\run_gemini_batch.py --mode low
```

Large texts (3 at a time), in a second terminal if you want both at once:
```
venv\Scripts\python.exe -X utf8 0-INBOX\temp\root-toc\run_gemini_batch.py --mode medium
```

Each prints one line per text when it starts and when it ends, e.g.
`[p2] 12:35:03 done     As_3CDs_  3.8-flash low · $0.29 · 1.7 min`.

Options:

| Option | Meaning |
|---|---|
| `--procs 3` | how many texts at the same time (each in its own process) |
| `--workers 4` | Gemini calls in parallel inside one text |
| `--limit 5` | stop after 5 texts (a test run) |
| `--only Ar_3CC4 Ar_3CC7` | run just these texts |
| `--retry-failed` | also take texts whose status is `failed` |
| `--reset-running` | after a crash or Ctrl+C: put texts left `running` back to `todo` |

If you hit Gemini rate limits (errors with 429 in the logs), lower `--procs` or `--workers`.

## Stop and resume

- **Ctrl+C** stops the run. Texts that were in progress stay `running` in the report.
- To continue, run the same command again with `--reset-running` once:
  ```
  venv\Scripts\python.exe -X utf8 0-INBOX\temp\root-toc\run_gemini_batch.py --mode low --reset-running
  ```
  A text that was cut off resumes where it stopped (finished chunk files are kept).
- Texts already `done`, `no-parts` or `earlier-run` are never redone.

## Where the results go

| What | Where |
|---|---|
| Status of every text | `0-INBOX/ROOT-TOC-BATCH.md` (human) · `0-INBOX/temp/root-toc/status.json` (machine) |
| Reading copy of the text | `0-INBOX/temp/root-seg-v2/<id>/prepared.md` |
| TOC working files + QC reports | `0-INBOX/temp/TOC-<id>/` |
| **The tree to ingest later** | `0-INBOX/temp/TOC-<id>/toc-tree-anchored-<id>.md` |
| Cost / tokens of the run | `0-INBOX/temp/TOC-<id>/summary.json`, `usage.jsonl` |
| Log of each text | `0-INBOX/temp/root-toc/logs/<id>.log` |

Status values: `done` (tree written) · `no-parts` (the text announces no parts — correct
for most prayers) · `failed` (see the note and the log; re-run with `--retry-failed`) ·
`running` · `todo` · `earlier-run` (done before this batch, by Claude agents).

## The rest of the workflow: segmentation + TOC ingest + grouping + block IDs

`run_workflow_batch.py` finishes the texts whose TOC extraction is done
(status `done`, `no-parts`, or `earlier-run` with an anchored tree), on Gemini:

1. `segment` with the current rules (titles in one block; mantras, labels and prose
   instructions inside verse run on one line; printed paragraph breaks kept),
2. `toc-ingest` from `0-INBOX/temp/TOC-<id>/toc-tree-anchored-<id>.md` (texts with no parts
   keep `## གཞུང་དངོས། ^1-0`),
3. grouping into stanzas / paragraphs with the `root-text-group` prompts on gemini-3.8-flash
   (thinking by mode); each answer is checked and asked again with the error if it is wrong,
4. `finish`: block IDs and the strict text check (letters and spacing = the source).

Two modes, as for the TOC batch:

| Mode | Texts | Grouping model |
|---|---|---|
| `--mode low` | small + medium | gemini-3.8-flash, thinking low |
| `--mode medium` | large | gemini-3.8-flash, thinking medium |

```
venv\Scripts\python.exe -X utf8 0-INBOX\temp\root-toc\run_workflow_batch.py --mode low
venv\Scripts\python.exe -X utf8 0-INBOX\temp\root-toc\run_workflow_batch.py --mode medium
```

Same options as the TOC batch: `--procs 3`, `--limit 5`, `--only <ids>`, `--retry-failed`,
`--reset-running`; `--thinking low|medium|high` overrides the mode's level. The two modes
take different texts and can run at the same time. Run `--mode medium` once the large
texts' TOC trees exist and their top-level parts have been checked — it takes only large
texts whose TOC is finished (6 so far: the ones done by Claude agents).

Results:

| What | Where |
|---|---|
| Report, one row per text | `0-INBOX/ROOT-WORKFLOW-BATCH.md` (status: `0-INBOX/temp/root-toc/workflow-status.json`) |
| **Finished files with block IDs** | `0-INBOX/processed/root-gemini/<id>-<free\|prose>.md` |
| Working folder | `0-INBOX/temp/root-final/<id>/` |
| Log | `0-INBOX/temp/root-toc/logs/workflow-<id>.log` |

`0-INBOX/processed/root/` is never touched (it holds the reviewed files). A text whose TOC
is still to do is not in the list yet: run the TOC batch first; the workflow batch picks
newly finished texts up the next time it starts. Check rows marked REVIEW (a heading that
could not be placed) and `breaks-review.md` notes. The Gemini grouping is new — look at a
few finished files before relying on all of them.

## Ingest by hand (single text)

```
venv\Scripts\python.exe -X utf8 4-SYSTEM\Skills\seg-toc-lib\root_text_build.py segment "0-INBOX\root\<id>.md" "0-INBOX\temp\root-seg-v2\<id>"
venv\Scripts\python.exe -X utf8 4-SYSTEM\Skills\seg-toc-lib\root_text_build.py toc-ingest "0-INBOX\temp\root-seg-v2\<id>" --tree "0-INBOX\temp\TOC-<id>\toc-tree-anchored-<id>.md"
```
Check `not placed: 0` in its report. Texts with status `no-parts` skip `toc-ingest`.

## Files

| File | Does |
|---|---|
| `run_gemini_batch.py` | the TOC batch: picks texts by mode, runs them N at a time, updates the report |
| `run_workflow_batch.py` | the rest of the workflow (segment, TOC ingest, grouping, block IDs); modes low / medium |
| `categorise.py` | one-time size classes |
| `status.py` | the status list and the report renderer |
| `COORDINATOR.md` | instructions used by the earlier Claude-agent runs (not needed for Gemini) |
| `4-SYSTEM/scripts/seg-toc-benchmark/root_toc_gemini.py` | one text, all passes, on Gemini (called by the batch) |
