---
name: toc-tree-extraction
description: >
  Build a full nested, decimal-numbered ས་བཅད (sa bcad) table-of-contents TREE from a
  Tibetan Buddhist commentary — the complete pipeline, not just candidates. Use this skill
  whenever the user wants the WHOLE structural outline reconstructed: "build the sa bcad
  tree", "extract the TOC tree", "make the dkar chag / dkar-chag", "reconstruct the outline
  hierarchy", or "give me the nested table of contents" for a Tibetan commentary or root
  text. This is the Claude-native equivalent of the bundled extract_toc_tree.py (which uses
  the Gemini API): each inference pass — (1) section candidates, (2) verbatim enumeration
  blocks, (3) nested decimal tree, (4) QC repair, (5) anchors — runs as an ISOLATED subagent
  with only its own prompt, mirroring the separate Gemini calls; two bundled Python helpers
  do the deterministic chunking and tree QC. Pass 5 writes the [[context]] anchors (and the
  front/back-matter frame nodes) that toc-tree-ingest needs. For candidate-only extraction
  without building a tree, use toc-candidate-extraction instead.
profile: rails-vault
---

# ས་བཅད TOC Tree Extraction (Claude-native)

This skill reconstructs the **full hierarchical table of contents** (དཀར་ཆག / *dkar chag*)
of a Tibetan commentary as a single nested, decimal-numbered tree. It is the Claude-native
port of `4-SYSTEM/Skills/toc-tree-extraction/scripts/toc_tree_extractor/extract_toc_tree.py`.

## Why this is an orchestrator, not one big prompt — READ THIS FIRST

The Gemini script's precision comes from **task isolation**: each pass is a *separate API
call* with only that one task's system prompt and only the relevant input. The
candidate-extraction call never sees the tree-building instructions, so it cannot drift into
tree-building; the verbatim-copy call never sees the "interpret and reconcile" instructions,
so it stays literal. Merging the four jobs into one prompt/one context collapses that
isolation and precision drops.

**Therefore you (the orchestrating agent) must NOT perform the four passes yourself in this
context.** Each pass runs as its own **isolated subagent** (via the `Task` tool) whose entire
instruction set is one prompt file under `prompts/` plus its specific input.

**Each subagent reads its input by path and writes its own output file.** Do not paste chunk
text into the subagent prompt and do not funnel results back through your context to write
them yourself — that serialises the writes and bloats your context with every chunk's Tibetan.
Instead, hand each subagent the *paths* of its prompt file and its input, and the *path* it
must write. Distinct output filenames mean parallel subagents never collide. You only: chunk,
dispatch subagents, do the deterministic merge, run the checker, and dispatch the repair
subagent. Do not read the pass prompt files into your own context and do the work inline —
that re-merges what this design deliberately separates.

The four isolated prompts live in:

| File | Pass |
|---|---|
| `prompts/pass1-candidates.md` | section candidates (one subagent per chunk) |
| `prompts/pass2-enumerations.md` | verbatim enumeration blocks (one subagent per chunk) |
| `prompts/pass3-tree.md` | build nested decimal tree (one subagent) |
| `prompts/pass4-qc-repair.md` | repair flagged issues (one subagent per repair round) |
| `prompts/pass5-anchors.md` | anchor every node in the text + add frame nodes (one subagent) |
| `prompts/verse-headings.md` | **instead of passes 1–4**, for commentaries declared `headings: verses` / `top` (see below) |
| `prompts/pass1-candidates-root.md` | pass 1 for **root texts** (mode `root`, see below) — adds Type D, topic headers without an ordinal |

---

## Inputs

| Input | Description |
|---|---|
| `input-file` | Path to the commentary/root-text `.md`, normally under `1-SOURCES/Commentaries/` |
| `commentary-id` | Short id for output filenames (inferred from the filename if obvious) |

If the file path is missing, or the `commentary-id` is not obvious from the filename, **stop
and ask** before doing anything else.

## Outputs (all under `0-INBOX/`)

| File | Stage |
|---|---|
| `0-INBOX/temp/TOC-<id>/chunk-index.tsv` | chunk line-range index (no text duplicated) |
| `0-INBOX/temp/TOC-<id>/candidates/chunk_NNN.md` | per-chunk section candidates (resumable) |
| `0-INBOX/temp/TOC-<id>/enumerations/chunk_NNN.md` | per-chunk verbatim enumeration blocks |
| `0-INBOX/toc-candidates-<id>.md` | merged candidates |
| `0-INBOX/toc-enumerations-<id>.md` | merged verbatim enumerations |
| `0-INBOX/toc-tree-<id>.md` | the final nested decimal TOC tree |
| `0-INBOX/toc-tree-qc-<id>.md` | QC report (issues before / after repair) |
| `0-INBOX/temp/TOC-<id>/toc-tree-<id>.md` | the anchored tree (`[[context]]` on every node + frame nodes) — the input of `toc-tree-ingest` |

Drafts in `0-INBOX/` — scratch, never cited from `2-RAILS/`. The tree has **no `^toc` block
IDs**; the decimal numbering alone identifies each entry. (Inserting the tree into a
source/rails file with block IDs is a separate step — use `add-toc`.)

---

## Step 0 — Plan the chunks (deterministic helper, index-only)

Do NOT copy the text into per-chunk files. Just plan the line windows — subagents read their
range straight from the source:

```bash
python 4-SYSTEM/Skills/toc-tree-extraction/scripts/chunk_file.py \
  "<input-file>" --chunk-size 150 --overlap 25 --index-only \
  --output-dir 0-INBOX/temp/TOC-<id>
```

This writes one tiny file, `0-INBOX/temp/TOC-<id>/chunk-index.tsv`, with a row per chunk:
`chunk_id <TAB> start_line <TAB> end_line` (1-based, inclusive). The 25-line overlap
guarantees every candidate appears in full in at least one window; no source text is
duplicated on disk. Read this small index into your context — it's just numbers — and drive
the passes from it.

**Resumability:** before dispatching a pass-1/pass-2 subagent for a chunk, check whether its
output file already exists and skip if so, so an interrupted run resumes from the first
missing chunk.

---

## Pass 1 — Section candidates · ISOLATED subagent per chunk

For each chunk row whose result file does not already exist, dispatch a **separate `Task`
subagent**. Pass it the prompt path, the source path, and that chunk's line range from the
index — never chunk text:

> Read `4-SYSTEM/Skills/toc-tree-extraction/prompts/pass1-candidates.md` and follow it
> exactly. Read ONLY lines START–END of the source file `<input-file>` (use
> `sed -n 'START,ENDp' "<input-file>"`, or the Read tool with offset=START / limit=END−START+1).
> Write your output to `0-INBOX/temp/TOC-<id>/candidates/chunk_NNN.md`, starting with the
> line `<!-- chunk NNN | lines START–END | source: <id> -->`, a blank line, then the
> candidate blocks — or `<!-- no candidates -->` if the prompt yields `NO CANDIDATES`. Do no
> other task; reply only with the path you wrote.

(Substitute the actual `START`, `END`, `NNN`, and `<input-file>` from the index row.)

Independent chunks have no dependencies, so dispatch several pass-1 subagents **in parallel**
— multiple `Task` calls in one message. (The harness runs a bounded number at once and queues
the rest.) Because each writes a distinct `chunk_NNN.md`, parallel writes never collide.

---

## Pass 2 — Verbatim enumerations · ISOLATED subagent per chunk

Run **separately** over the same chunks — a different isolated subagent, because verbatim
copying must not be contaminated by the interpretive instructions of the other passes. Same
read-by-path / write-own-file pattern:

> Read `4-SYSTEM/Skills/toc-tree-extraction/prompts/pass2-enumerations.md` and follow it
> exactly. Read ONLY lines START–END of the source file `<input-file>` (use
> `sed -n 'START,ENDp' "<input-file>"`). Write your output to
> `0-INBOX/temp/TOC-<id>/enumerations/chunk_NNN.md` — the enumeration blocks, or
> `NO ENUMERATIONS`. Isolate ONLY the division-announcement clauses (start at the topic being
> divided, stop at the closing count/list marker); do NOT copy the commentary body that
> explains each part. Copy verbatim; add no interpretation. Reply only with the path you wrote.

These run in parallel too (one message, multiple `Task` calls), each writing a distinct file.

---

## Merge (deterministic — concatenate on disk, don't read into context)

Merging is mechanical text assembly, not inference. Do it with the shell so the chunk text
never enters your context. Concatenate the per-chunk candidate files (keeping their
`<!-- chunk NNN -->` headers) into `0-INBOX/toc-candidates-<id>.md`, e.g.:

```bash
cd 0-INBOX/temp/TOC-<id>/candidates && cat chunk_*.md > /tmp/cand-body.md
# then prepend frontmatter and move into place
```

Frontmatter:

```yaml
---
source: <id>
skill: toc-tree-extraction
stage: candidates
date: <YYYY-MM-DD>
total_candidates: <N>
---
```

Likewise concatenate the enumeration files (skipping `NO ENUMERATIONS` ones, in document
order) into `0-INBOX/toc-enumerations-<id>.md`. Pass 3 reads both merged files by path.

---

## Pass 3 — Build the nested decimal tree · ISOLATED subagent

Dispatch ONE subagent with only the pass-3 prompt and the paths of the two merged inputs:

> Read `4-SYSTEM/Skills/toc-tree-extraction/prompts/pass3-tree.md` and follow it exactly.
> Build the full nested decimal TOC for commentary "<id>" from the candidates in
> `0-INBOX/toc-candidates-<id>.md`, reconciled against the enumerations in
> `0-INBOX/toc-enumerations-<id>.md`. Write only the tree block (starting with
> `## དཀར་ཆག / Table of Contents`) to `0-INBOX/toc-tree-<id>.md`. Reply only with the path
> you wrote.

After it returns, prepend `stage: toc-tree` frontmatter to `0-INBOX/toc-tree-<id>.md` if the
subagent did not.

---

## Pass 4 — Deterministic QC, then ISOLATED repair subagent

First run the bundled checker yourself (NOT by hand — it encodes the exact
numbering/attestation logic and must be identical every run):

```bash
python 4-SYSTEM/Skills/toc-tree-extraction/scripts/qc_check_tree.py \
  0-INBOX/toc-tree-<id>.md \
  --corpus 0-INBOX/toc-candidates-<id>.md 0-INBOX/toc-enumerations-<id>.md \
  --out 0-INBOX/toc-tree-qc-<id>.md
```

It flags indentation errors, Tibetan-ordinal vs decimal mismatch, duplicate decimals, sibling
gaps/dups, titles not attested (possible hallucination), and ordinals not attested for a
title. Exit code = issue count.

If issues remain, dispatch ONE **isolated repair subagent** with only the pass-4 prompt and
the paths of the issue report, tree, and both sources:

> Read `4-SYSTEM/Skills/toc-tree-extraction/prompts/pass4-qc-repair.md` and follow it exactly.
> Correct the tree for commentary "<id>", fixing every issue in `0-INBOX/toc-tree-qc-<id>.md`
> against BOTH the enumerations (`0-INBOX/toc-enumerations-<id>.md`) and the candidates
> (`0-INBOX/toc-candidates-<id>.md`). The tree to fix is `0-INBOX/toc-tree-<id>.md`. Overwrite
> that same file with the corrected tree block and reply only with its path.

After it returns, **re-run the checker** and record issues-before / issues-after in
`0-INBOX/toc-tree-qc-<id>.md`. Iterate (a fresh isolated repair subagent per round) until the
count is 0 or only genuinely-ambiguous issues remain (note those for the human). Keep the
deterministic checker as the gate — never declare the tree clean on a subagent's say-so.

---

## Pass 5 — Anchors · ISOLATED subagent

`toc-tree-ingest` places each heading by its `[[context]]` — the verbatim words where that
node's section begins. The tree from passes 3–4 has none, so this pass adds them, together
with the editorial **frame** nodes for the front and back matter (`* I. མཆོད་བརྗོད།`,
`* a. བསྔོ་བ།`, `* b. མཇུག་བྱང།` / `* b.1 མཛད་བྱང།`):

> Read `4-SYSTEM/Skills/toc-tree-extraction/prompts/pass5-anchors.md` and follow it exactly.
> The TOC tree is `0-INBOX/toc-tree-<id>.md`; the commentary is `<input-file>` (read all of
> it). Write the anchored tree to `0-INBOX/temp/TOC-<id>/toc-tree-<id>.md`. Reply only with
> the path you wrote.

The anchoring rules encode where the vault's human editors put headings: a divided node at
its own division announcement, node 1 at the work's top-level announcement, every other node
at its own opener (`གཉིས་པ་ … ནི།`) — never at the parent's listing of its title. A first
child's opener sits in the same block as its parent's announcement, so the two headings
stack. For a long commentary, give the subagent one top-level subtree (and the matching
line range) at a time.

Run `commentary-segmentation --units` on the commentary **before**
extracting the tree, so that the file the anchors are copied from is the file the headings
are ingested into.

---

## Heading mode — decide before pass 1

Not every commentary's editors use its sa bcad as headings. Declare one of four modes —
three for **commentaries**, one for **root texts**:

| Mode | When | Route |
|---|---|---|
| `sabcad` | the commentary has a full sa bcad and the editors ingest it | passes 1–5 as below |
| `verses` | the commentary explains the root verse by verse (no sa bcad, or one the editors ignore) | `prompts/verse-headings.md` (mode `verses`) in one isolated subagent, then pass 5 for the frame nodes only |
| `top` | only the large parts of the body get headings | `prompts/verse-headings.md` (mode `top`), then pass 5 for the frame nodes only |
| `root` | a **root text** — a verse treatise, praise or ritual in its own voice, called from `root-text-segmentation` | pass 1 with `prompts/pass1-candidates-root.md`, passes 2–4 as below, pass 5 **without frame nodes** (see below) |

### Mode `root` — root texts

Root texts announce their parts without the commentarial sa bcad formula — often no ordinal
and no count: `<topic> བཤད་བྱ་སྟེ།`, `<topic> ཆོ་ག་ནི།`, `<topic> སྦྱོར་བ་ལ།`. The standard pass 1
treats a chunk with no ordinal as having no outline and misses them; `pass1-candidates-root.md`
adds them as **Type D**.

- **Do not force a tree.** If pass 1 returns no candidates for every chunk, stop: the text
  announces no parts (most prayers and chants) and gets no body headings. Report that; it is
  the correct result, not a failure.
- **Pass 5:** give the subagent the extra instruction *"numbered nodes only — do not add the
  frame nodes I. / a. / b.; the front matter and colophons are headed by
  root-text-segmentation from fixed patterns."* A preliminary part before node 1 may still
  be `II.`.
- **Only the top-level nodes become headings.** In a verse root text the sub-parts are often
  shorter than a stanza (a 2- or 3-line rite); as headings they break the stanza layout or
  end up empty. `root-text-segmentation` ingests the top-level nodes and keeps the rest in
  the tree file.

In `verses` mode the headings are editorial: `1. བསྟོད་པ་དངོས།` (or the commentary's own
name), `1.n ཕྱག་འཚལ་<ordinal>།` per root stanza, children only where the commentary itself
divides a stanza (or splits every stanza the same way, e.g. `ཚིག་འགྲེལ།` / `གསལ་འདེབས་ཚུལ།`),
then the later parts (`ཕན་ཡོན།` …). On the 8-file benchmark this took the five non-sa-bcad
files from heading F1 0.10 to 0.83 (`4-SYSTEM/scripts/seg-toc-benchmark/`, variant v1.4).

Subagent prompt:

> Read `4-SYSTEM/Skills/toc-tree-extraction/prompts/verse-headings.md` and follow it
> exactly. Mode: `<verses|top>`. The commentary is `<segmented file>` (read all of it); the
> root text is `<root text>`. Write the tree to `0-INBOX/temp/TOC-<id>/verse-tree-<id>.md`.
> Check every `[[context]]` occurs in the commentary (whitespace removed). Reply with the path.

Then run pass 5 on that tree with the instruction "keep every numbered line verbatim; add
the frame nodes only", or combine an existing frame tree with
`python3 4-SYSTEM/scripts/seg-toc-benchmark/merge_trees.py <numbered> <frame> <out>`.

---

## Execution summary

1. Confirm `input-file` and `commentary-id` (ask if not obvious).
2. `chunk_file.py --index-only` → `chunk-index.tsv` (line ranges only, no text copied).
3. Pass 1: isolated subagent per chunk, reads its line range from the source + writes its own `candidates/chunk_NNN.md` (resumable, parallel).
4. Pass 2: isolated subagent per chunk, writes its own `enumerations/chunk_NNN.md` (parallel).
5. Merge on disk (shell `cat`) → `0-INBOX/toc-candidates-<id>.md` and `0-INBOX/toc-enumerations-<id>.md`.
6. Pass 3: one isolated subagent reads both merged files → writes `0-INBOX/toc-tree-<id>.md`.
7. Pass 4: `qc_check_tree.py` → isolated repair subagent (reads/overwrites by path) → re-check → `0-INBOX/toc-tree-qc-<id>.md`.
8. Pass 5: one isolated subagent anchors every node and adds frame nodes → `0-INBOX/temp/TOC-<id>/toc-tree-<id>.md`.
9. Report totals (candidates, enumeration blocks, issues before/after) and the output paths; hand the anchored tree to `toc-tree-ingest`.

**Isolation is the whole point.** If you ever find yourself doing a pass's reasoning in this
orchestrating context instead of in its own subagent, stop and dispatch the subagent — that is
what preserves the per-task precision the Gemini pipeline was built around.

For candidate extraction only (no tree), use `toc-candidate-extraction`.

## Models — Gemini script vs Claude subagents

| Path | Model | What it runs |
|---|---|---|
| Gemini script (batch / headless) | `gemini-3.8-flash`, thinking `high`, 65 536 output tokens, no fallback; a reply cut off at the limit is retried, never used | `scripts/toc_tree_extractor/extract_toc_tree.py` = passes 1–4; `find_toc_contexts.py` (same folder) = pass 5 anchoring. `GEMINI_API_KEY` is loaded by the scripts from the vault `.env` — never open that file. |
| Claude subagents (this procedure) | isolated subagents with `model: opus` (Opus 5.5), session effort high | passes 1–5 above, prompts from `prompts/` |

⚠ **The two paths are not equivalent yet.** The Gemini script carries its own *embedded*
v1 prompts (`SYSTEM_PROMPT`, `ENUM_SYSTEM_PROMPT`, `TREE_SYSTEM_PROMPT`,
`QC_SYSTEM_PROMPT`); passes 2 and 3 differ substantially from `prompts/` (no line-number
`[[N]]` contract on this path, stricter enumeration rules), and the script has no modes
`verses` / `top` / `root`, no Type D, and no frame nodes (add those by hand). The benchmark
numbers in this skill were measured on the Claude path. Use the Gemini script for a quick
sa bcad pass over many commentaries; use the Claude path for root texts, the non-`sabcad`
modes, and anything that will be ingested.
