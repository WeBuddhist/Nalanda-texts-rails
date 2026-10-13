# Gemini benchmark — how to run

This folder is a self-contained copy of the segmentation + TOC pipeline, the 8 gold
commentaries, their inputs, and the Opus 5.5 results to compare against. Gemini
answers exactly the same prompts the Opus runs answered, and the outputs are scored
the same way.

## Once

```
pip install google-genai
```

The API key is read from the `.env` at the root of Nalanda-texts-rails (`GEMINI_API_KEY=...`).
Nothing else from `.env` is read, and the key is never printed or written anywhere.

## Run (from this folder)

```
cd D:\Work\OpenPecha\Nalanda-texts-rails\0-INBOX\seg-toc-bench
python 4-SYSTEM\scripts\seg-toc-benchmark\gemini_bench.py
```

Default: **Gemini 3.8 Flash, thinking `low` and `high`, 3 runs each, on Tāranātha** —
6 pipeline runs, about 8 API calls each. It prints each call's time and token counts.

When it finishes, the report is in `0-INBOX\bench8\gemini-gemini-3.8-flash-report.md`.
It covers:
- quality per file: Opus 5.5 vs Gemini low vs Gemini high, as median (min–max);
- failures: headings not placed, rejected operations, invalid JSON;
- tokens (including thinking), API time and estimated cost per run.

Send me the report (or just say it's done and I'll fetch it) and I'll write it up.

## Options

| option | meaning |
|---|---|
| `--files all` | all 8 commentaries instead of Tāranātha only |
| `--files taranatha drakpa` | a chosen set |
| `--levels low medium high` | thinking levels to test |
| `--runs 3` | repeats per level |
| `--model gemini-3.1-pro-preview` | another model (set `--price-in/--price-out` for the cost column) |
| `--report-only` | rebuild the report from what has run so far |

If it stops (network, quota), run the same command again: finished steps and saved
answers are kept, and it continues where it stopped.

## Settings used for every Gemini call

| setting | value | why |
|---|---|---|
| model | `gemini-3.8-flash` (pinned, no `-latest` alias) | newest stable; reproducible |
| thinking | `thinking_level` = `low` / `high` | Gemini's equivalent of Claude's effort; it cannot be switched off on 3.8 Flash |
| temperature | API default (1.0) | Google strongly advises against lowering it on Gemini 3+ (looping, worse reasoning) |
| max output | 65,536 for the heading tree, 32,768 otherwise | the limit includes thinking tokens; a reply cut off by the limit is retried, never used |
| JSON mode | on for re-segmentation and QC | the replies must be JSON arrays |
| retries | up to 5, with back-off | transient API errors |
