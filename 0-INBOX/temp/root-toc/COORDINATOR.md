# Coordinator instructions — one root text, TOC extract only

You coordinate ONE root text in the vault `D:\Work\OpenPecha\Nalanda-texts-rails` (work
from that folder). The text id `<id>` is given in your prompt; the source is
`0-INBOX/root/<id>.md`.

**Job:** build its TOC tree with the skill `root-text-toc-extract`, and STOP before
ingestion. Do not ingest, group, or stamp block IDs. Do not edit any file outside
`0-INBOX/temp/root-seg-v2/<id>/` and `0-INBOX/temp/TOC-<id>/`.

Environment:
- Run Python as `py -X utf8 ...` (the `python` command is not available here). Use
  forward-slash paths in the Bash tool.
- Never open, print or read any `.env` file.

Steps:
1. Make the reading copy (deterministic, no model):
   `py -X utf8 4-SYSTEM/Skills/seg-toc-lib/root_text_build.py segment "0-INBOX/root/<id>.md" "0-INBOX/temp/root-seg-v2/<id>"`
   Note from its report: the form (verse/prose) and the number of units.
2. Read `4-SYSTEM/Skills/root-text-toc-extract/SKILL.md` IN FULL and follow its Procedure
   exactly (steps 1–8: chunk, pass 1, pass 2, merge, pass 3, pass 4 QC + repair, pass 5
   anchors, pass 6 QC against the text), with input-file =
   `0-INBOX/temp/root-seg-v2/<id>/prepared.md` and id = `<id>`.
   - Every model pass runs as its OWN isolated subagent (Agent tool, model "opus"), given
     exactly the dispatch text the skill shows, reading its input by path and writing its
     own output file, replying only with the path. Pass 1 and pass 2 run one subagent per
     chunk, in parallel. You only chunk, dispatch, merge on disk, run the checker scripts
     and dispatch repair subagents. Never do a pass's reasoning yourself and never paste
     text into a prompt.
   - **Wait for every subagent.** Launch pass subagents with `run_in_background: false`
     (several in one message for the parallel chunk passes) so each call returns only
     when the subagent has written its file. Before each next step, check on disk that
     every expected output file exists. Never send your final reply while any subagent
     is still running — a hand-back with work in flight loses that work.
   - If `0-INBOX/temp/TOC-<id>/` already holds files from an interrupted run, keep them:
     skip chunks whose output exists and continue from the first missing step.
   - If pass 1 finds no candidates in any chunk: stop there (Rule 1, the text announces no
     parts) — that is a correct result.
   - The deterministic checkers are the gates; never declare the tree clean on a
     subagent's say-so.
3. Do NOT run `root-text-toc-ingest`.

Your final reply must be ONLY one line of JSON, nothing else:

```
{"id":"<id>","status":"done|no-parts|failed","form":"verse|prose","units":N,"chunks":N,"parts":N,"nodes":N,"qc4":"<issues before>→<after>","qc6":"<short result, e.g. 0 issues / 2 accepted closing-line titles / 1 [[?]]>","note":"<anything a reviewer should know, short; empty if nothing>"}
```

For no-parts, parts/nodes = 0 and qc4/qc6 = "". For failed, say why in note.
