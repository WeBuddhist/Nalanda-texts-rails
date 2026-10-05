#!/usr/bin/env python3
"""
resegment.py — line-number block re-segmentation for Tibetan commentaries.

A simpler, safer variant of block-resegmentation. The source is a Stage-1
segmented commentary with TOC headings embedded, where **each clause sits on its
own physical line** (one line = one atomic segment). An LLM (Gemini) reads each
section and flags, by ABSOLUTE LINE NUMBER, which adjacent lines should be grouped
into one citable block. A deterministic script applies the grouping and verifies
that not a single character changed.

Each merged block is emitted as ONE physical line (its clauses joined by a single
space); blocks are separated by one blank line. The dominant — and usually only —
operation is MERGE (group adjacent lines). A line that genuinely fuses two thoughts
and would need a mid-line cut is flagged REVIEW for a human; it is never auto-split.

Pipeline:
    commentary-segmentation Stage 1
         ↓
    [TOC inclusion — headings embedded]
         ↓
    resegment.py   ← THIS SCRIPT
         ↓
    block-ID stamping

Model (boundary-edit):
    unit            = one non-blank, non-heading line
    default state   = every unit is its own block
    MERGE n..m      = lines n through m become ONE block, joined on a single line
    REVIEW n        = line n may fuse two thoughts; surfaced to a human, not applied
    headings        = pass through untouched, framed by blank lines
    blocks          = separated by exactly one blank line in the output

Setup:
    pip install google-genai
    GEMINI_API_KEY is read from the .env file at the vault root (next to 4-SYSTEM/);
    an environment variable of the same name takes precedence.

Usage:
    # basic run (commentary-id inferred from filename):
    python3 4-SYSTEM/Skills/commentary-resegment/scripts/resegment.py \\
        "1-SOURCES/commentaries/commentaries_with_toc/BCAC14_GDR_bo.toc.md"

    # explicit id:
    python3 ... "<file>" --commentary-id BCAC14_GDR_bo

    # resume an interrupted run (staged windows are skipped):
    python3 ... "<file>" --commentary-id BCAC14_GDR_bo

    # re-apply already-staged ops without new LLM calls (e.g. after hand-editing a window):
    python3 ... "<file>" --commentary-id BCAC14_GDR_bo --apply-only

    # integrity check only, write nothing:
    python3 ... "<file>" --commentary-id BCAC14_GDR_bo --dry-run
"""

import argparse
import json
import os
import random
import re
import sys
import time
from pathlib import Path


# ── Gemini API key ────────────────────────────────────────────────────────────
_KEY_NAMES = ("GEMINI_API_KEY", "GOOGLE_API_KEY")


def _gemini_api_key():
    """
    The Gemini API key: from the environment if set, otherwise from the `.env`
    file at the vault root (a folder that contains 4-SYSTEM/), found by walking
    up from this script's own location, then from the current directory; the
    nearest vault root with a .env wins (so a benchmark copy inside the vault
    still uses the vault's own .env).
    Only GEMINI_API_KEY / GOOGLE_API_KEY are read; nothing else from .env is
    loaded, and the key is never printed or logged.
    """
    for n in _KEY_NAMES:
        v = os.environ.get(n, "").strip()
        if v:
            return v
    roots = []          # every folder containing 4-SYSTEM/, nearest first
    for start in (Path(__file__).resolve().parent, Path.cwd().resolve()):
        for d in (start, *start.parents):
            if (d / "4-SYSTEM").is_dir() and d not in roots:
                roots.append(d)
    for root in roots:
        envf = root / ".env"
        if not envf.is_file():
            continue
        try:
            lines = envf.read_text(encoding="utf-8-sig").splitlines()
        except OSError:
            continue
        found = {}
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k = k.strip()
            if k.startswith("export "):
                k = k[len("export "):].strip()
            if k not in _KEY_NAMES:
                continue
            v = v.strip()
            if v[:1] in ("'", '"') and v[-1:] == v[:1] and len(v) >= 2:
                v = v[1:-1]
            else:
                v = v.split(" #", 1)[0].strip()
            if v:
                found[k] = v
        for n in _KEY_NAMES:
            if n in found:
                return found[n]
    return None

# ── defaults ─────────────────────────────────────────────────────────────────

DEFAULT_MODEL          = "gemini-3.8-flash"
DEFAULT_FALLBACK_MODEL = ""   # gemini-2.0-flash was retired (June 2026); no fallback

# Gemini 3.8 Flash with high thinking. On Gemini 3.x thinking cannot be switched off and
# counts against max_output_tokens; temperature stays at the API default (Google advises
# against lowering it on 3.x — it causes looping). A reply cut off at the limit is an
# error and is retried, never used as an answer.
GEMINI_THINKING   = "high"
GEMINI_MAX_OUTPUT = 65536


def _check_finish(resp):
    """Raise if the reply was cut off at max_output_tokens (thinking counts too)."""
    cand = (getattr(resp, "candidates", None) or [None])[0]
    if "MAX_TOKENS" in str(getattr(cand, "finish_reason", "") or ""):
        raise RuntimeError(f"reply cut off at max_output_tokens={GEMINI_MAX_OUTPUT} "
                           f"(thinking counts too)")

DEFAULT_WINDOW_LINES   = 60    # max content lines per LLM window
MAX_RETRIES            = 8
RETRY_BACKOFF_BASE     = 8     # seconds; grows exponentially per attempt
MAX_BACKOFF            = 120   # cap on a single wait

TEMP_BASE   = "0-INBOX/temp"
OUTPUT_BASE = "0-INBOX/resegmented"

# Lines ending in a sentence-final particle + shad are safe window-cut points:
# a merge never crosses a sentence boundary, so cutting here loses no grouping.
TERMINAL_RE = re.compile(
    r'(?:སོ|འོ|ནོ|དོ|ཏོ|ཡོ|ངོ|བོ|མོ|རོ|ལོ)།[\s།]*$'
)

# ── prompts ───────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are an expert editor of classical Tibetan Buddhist commentary (འགྲེལ་པ་).

You are given a numbered list of LINES from one section of a commentary. Each line carries
its absolute line number and holds a single clause. The text is over-segmented: many
adjacent lines together form one coherent unit of meaning.

YOUR TASK: using the CONTENT and CONTEXT of the passage, group adjacent lines into short,
coherent PARAGRAPHS — each one sense unit (one idea, one narrative beat, one
objection-and-reply exchange). Judge the grouping by MEANING, not by surface grammar,
particles, or punctuation.

GUIDELINES
- Aim for paragraphs of about 2–4 lines. When unsure where to break, prefer the shorter
  grouping (2–3 lines).
- A paragraph carries one complete thought. Begin a new paragraph when the topic, the
  actor, or the move in the argument changes.
- Keep a citation or quoted stanza together with the words that introduce or close it when
  they belong to the same thought.
- You only point at line numbers. You NEVER retype, translate, reorder, add, or delete any
  word or character.

OUTPUT FORMAT — a JSON array, one object per paragraph that groups two or more lines:

[
  {"op": "merge", "lines": [14, 15, 16]},
  {"op": "merge", "lines": [17, 18]}
]

- "lines" must be CONSECUTIVE ascending absolute line numbers.
- Each line number appears in AT MOST ONE group.
- A line that already stands as its own paragraph may simply be omitted (it stays separate).
- Never group a heading line (headings are not shown below).
- Output ONLY the JSON array — no commentary, no code fences.
"""

USER_PROMPT_TEMPLATE = """\
Section heading: {heading}

Group the lines below into coherent sense-unit paragraphs (about 2–4 lines each), judging by
content and context. Line numbers are absolute (file-level). Output only the JSON array.

--- BEGIN LINES ---
{lines_text}
--- END LINES ---
"""

# ── file parsing ──────────────────────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r'^---[ \t]*\r?\n.*?\r?\n---[ \t]*\r?\n', re.DOTALL)


def squeeze(text: str) -> str:
    """Strip all whitespace — used for integrity comparison."""
    return re.sub(r'\s+', '', text)


def is_heading(line: str) -> bool:
    return line.lstrip().startswith('#')


def parse_file(path: Path):
    """
    Return (newline, frontmatter, units).

    newline      : "\\r\\n" or "\\n" — the source's line ending, preserved on write.
    frontmatter  : the YAML block (verbatim, including fences) or "".
    units        : ordered list of dicts, one per non-blank body line:
                     {"lineno": int (1-based, absolute),
                      "text":   str (line content, no trailing newline),
                      "kind":   "heading" | "content"}
                   Blank lines are dropped here; boundaries are re-inserted on output.
    """
    raw = path.read_bytes().decode("utf-8")
    newline = "\r\n" if "\r\n" in raw else "\n"
    norm = raw.replace("\r\n", "\n")

    frontmatter = ""
    m = FRONTMATTER_RE.match(raw)
    if m:
        frontmatter = m.group(0).replace("\r\n", "\n")
        fm_lines = frontmatter.count("\n")
        body_start = fm_lines  # 0-based index of first body line in `norm`
    else:
        body_start = 0

    lines = norm.split("\n")
    units = []
    for idx, text in enumerate(lines):
        lineno = idx + 1  # 1-based absolute
        if idx < body_start:
            continue
        if text.strip() == "":
            continue
        kind = "heading" if is_heading(text) else "content"
        units.append({"lineno": lineno, "text": text, "kind": kind})

    return newline, frontmatter, units


# ── windowing ─────────────────────────────────────────────────────────────────

def make_windows(units, window_lines):
    """
    Build per-section windows of CONTENT lines for the LLM.

    - A heading always closes the current window (sections never span a heading).
    - Within a section, a window is capped at `window_lines`; it is cut at the
      latest line that ends in a sentence-final particle (TERMINAL_RE) so no
      thought-group is ever split across a window boundary.

    Returns a list of dicts:
      {"idx": int, "heading": str, "lines": [ {lineno, text}, ... ]}
    """
    windows = []
    cur = []
    cur_heading = "(front matter)"
    idx = 0

    def flush():
        nonlocal cur, idx
        if cur:
            windows.append({"idx": idx, "heading": cur_heading, "lines": cur})
            idx += 1
            cur = []

    for u in units:
        if u["kind"] == "heading":
            flush()
            cur_heading = u["text"]
            continue
        cur.append({"lineno": u["lineno"], "text": u["text"]})
        if len(cur) >= window_lines and TERMINAL_RE.search(u["text"]):
            flush()
    flush()
    return windows


def format_window(window):
    return "\n".join(f"[{ln['lineno']}] {ln['text']}" for ln in window["lines"])


# ── Gemini API ────────────────────────────────────────────────────────────────



def get_client():
    try:
        from google import genai  # noqa: PLC0415
    except ImportError:
        sys.exit("Error: google-genai is not installed.\n  Run: pip install google-genai")
    api_key = _gemini_api_key()
    if not api_key:
        sys.exit("Error: no API key found.\n"
                 "  Put GEMINI_API_KEY=your-key in the .env file at the vault root (next to 4-SYSTEM/),\n"
                 "  or set GEMINI_API_KEY in the environment.")
    return genai.Client(api_key=api_key)


def _is_overloaded(err) -> bool:
    s = str(err).upper()
    return any(tok in s for tok in (
        "503", "UNAVAILABLE", "OVERLOADED", "HIGH DEMAND", "429", "RESOURCE_EXHAUSTED",
    ))


def _generate(client, model, user_prompt, fallback_model="", label="window"):
    from google.genai import types  # noqa: PLC0415
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        thinking_config=types.ThinkingConfig(thinking_level=GEMINI_THINKING),
        max_output_tokens=GEMINI_MAX_OUTPUT,
    )
    models_to_try = [model]
    if fallback_model and fallback_model != model:
        models_to_try.append(fallback_model)

    last_err = None
    for mi, mdl in enumerate(models_to_try):
        if mi > 0:
            print(f"    -> '{model}' still overloaded; falling back to '{mdl}'", file=sys.stderr)
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = client.models.generate_content(model=mdl, contents=user_prompt, config=config)
                _check_finish(resp)
                return (resp.text or "").strip()
            except Exception as e:  # noqa: BLE001
                last_err = e
                if attempt < MAX_RETRIES:
                    base = min(RETRY_BACKOFF_BASE * (2 ** (attempt - 1)), MAX_BACKOFF)
                    wait = base + random.uniform(0, base * 0.25)
                    kind = "overloaded" if _is_overloaded(e) else "error"
                    print(f"    ! {label} attempt {attempt}/{MAX_RETRIES} {kind}: {e}; "
                          f"retrying in {wait:.0f}s...", file=sys.stderr)
                    time.sleep(wait)
        if not _is_overloaded(last_err):
            break
    raise RuntimeError(f"Gemini call failed after retries: {last_err}")


def call_llm_for_window(client, model, window, fallback_model=""):
    lines_text = format_window(window)
    user_prompt = USER_PROMPT_TEMPLATE.format(heading=window["heading"], lines_text=lines_text)
    label = f"window-{window['idx'] + 1}"
    raw = _generate(client, model, user_prompt, fallback_model=fallback_model, label=label)
    raw = re.sub(r'^```(?:json)?\s*', '', raw.strip())
    raw = re.sub(r'\s*```$', '', raw.strip())
    try:
        ops = json.loads(raw)
        if not isinstance(ops, list):
            print(f"  ! {label}: non-list JSON — treating as []", file=sys.stderr)
            return []
        return ops
    except json.JSONDecodeError as e:
        print(f"  ! {label}: JSON parse error ({e}) — treating as []. Raw:\n{raw[:200]}",
              file=sys.stderr)
        return []


# ── staging ───────────────────────────────────────────────────────────────────

def staging_path(staging_dir: Path, window_idx: int) -> Path:
    return staging_dir / f"window-{window_idx:04d}.json"


def save_window_result(staging_dir: Path, window: dict, ops: list):
    staging_dir.mkdir(parents=True, exist_ok=True)
    line_nos = [ln["lineno"] for ln in window["lines"]]
    data = {
        "window_idx": window["idx"],
        "heading":    window["heading"],
        "line_range": [line_nos[0], line_nos[-1]] if line_nos else [],
        "operations": ops,
    }
    staging_path(staging_dir, window["idx"]).write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load_window_result(staging_dir: Path, window_idx: int):
    p = staging_path(staging_dir, window_idx)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


# ── validate operations ───────────────────────────────────────────────────────

def validate_operations(window_results, units):
    """
    Collect and validate merge/review ops across all windows.

    Validation for a merge:
      - >= 2 line numbers, ascending and adjacent in the UNIT sequence, i.e. the
        referenced lines are directly consecutive units with nothing (in
        particular, no heading) between them,
      - every referenced line is a known content line,
      - no line is claimed by more than one operation.

    Returns (merges: list[list[int]], reviews: list[int], errors: list[str]).
    """
    # absolute lineno -> position within the FULL unit sequence (headings included).
    # Using full-unit positions means a heading between two content lines makes
    # them non-adjacent (gap of 2), so a merge can never cross a heading.
    pos = {u["lineno"]: i for i, u in enumerate(units)}
    valid_line = {u["lineno"] for u in units if u["kind"] == "content"}

    claimed: dict = {}
    merges, reviews, errors = [], [], []

    for wr in window_results:
        for op in wr.get("operations", []):
            kind = op.get("op")
            if kind == "merge":
                lines = op.get("lines", [])
                if len(lines) < 2:
                    errors.append(f"merge {lines}: need >= 2 lines — skipped")
                    continue
                if sorted(lines) != lines:
                    errors.append(f"merge {lines}: not ascending — auto-sorted")
                    lines = sorted(lines)
                bad = [ln for ln in lines if ln not in valid_line]
                if bad:
                    errors.append(f"merge {lines}: unknown/heading line(s) {bad} — skipped")
                    continue
                # consecutive in the unit sequence (no heading or gap between)
                if any(pos[lines[i + 1]] != pos[lines[i]] + 1 for i in range(len(lines) - 1)):
                    errors.append(f"merge {lines}: lines not contiguous content — skipped")
                    continue
                conflict = [ln for ln in lines if ln in claimed]
                if conflict:
                    errors.append(f"merge {lines}: line(s) {conflict} already claimed — skipped")
                    continue
                for ln in lines:
                    claimed[ln] = "merge"
                merges.append(lines)
            elif kind == "review":
                ln = op.get("line")
                if ln not in valid_line:
                    errors.append(f"review {ln}: unknown/heading line — skipped")
                    continue
                reviews.append(ln)
            else:
                errors.append(f"unknown op type: {kind} — skipped")

    merges.sort(key=lambda g: g[0])
    reviews.sort()
    return merges, reviews, errors


# ── apply operations ──────────────────────────────────────────────────────────

def apply_operations(units, merges):
    """
    Build the ordered list of output blocks from units + merge groups.

    Default: every content line is its own block; headings are their own block.
    A merge group joins its consecutive content lines into ONE block on a single
    physical line, the clauses separated by a single space.

    Returns list[str] of block strings, in document order.
    """
    start_of_group = {}     # first lineno -> full group
    member_of_group = set()  # all linenos inside any group
    for g in merges:
        start_of_group[g[0]] = g
        member_of_group.update(g)

    lineno_to_text = {u["lineno"]: u["text"] for u in units}

    blocks = []
    i = 0
    seq = units
    while i < len(seq):
        u = seq[i]
        ln = u["lineno"]
        if u["kind"] == "heading":
            blocks.append(u["text"])
            i += 1
            continue
        if ln in start_of_group:
            g = start_of_group[ln]
            merged = " ".join(lineno_to_text[x].strip() for x in g)
            blocks.append(merged)
            i += len(g)
            continue
        if ln in member_of_group:
            # already consumed as part of a group start; should not happen given ordering
            i += 1
            continue
        blocks.append(u["text"])
        i += 1
    return blocks


# ── integrity check ───────────────────────────────────────────────────────────

def render_output(frontmatter: str, blocks: list, newline: str) -> str:
    body = "\n\n".join(blocks)
    text = (frontmatter + body if frontmatter else body) + "\n"
    if newline != "\n":
        text = text.replace("\n", newline)
    return text


def check_integrity(path: Path, output_text: str):
    original = path.read_bytes().decode("utf-8")
    o, r = squeeze(original), squeeze(output_text)
    if o == r:
        return True, "OK"
    for i, (a, b) in enumerate(zip(o, r)):
        if a != b:
            return False, (
                f"First difference at squeezed char {i}:\n"
                f"  original: ...{o[max(0,i-30):i+30]!r}...\n"
                f"  result:   ...{r[max(0,i-30):i+30]!r}...")
    return False, f"Length mismatch: original {len(o)} chars, result {len(r)} chars"


# ── output writers ────────────────────────────────────────────────────────────

def write_ops_log(log_path, merges, reviews, errors, units, n_blocks, cid):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    lineno_to_text = {u["lineno"]: u["text"] for u in units}
    n_content = sum(1 for u in units if u["kind"] == "content")
    n_head = sum(1 for u in units if u["kind"] == "heading")

    def preview(t, n=70):
        return t[:n] + ("…" if len(t) > n else "")

    out = [
        f"# Line-wise Resegmentation Log — {cid}",
        "",
        f"Content lines in : {n_content}",
        f"Headings         : {n_head}",
        f"Blocks out       : {n_blocks}",
        f"Merges applied   : {len(merges)}",
        f"Review flags     : {len(reviews)}",
        f"Errors skipped   : {len(errors)}",
        "",
    ]
    if merges:
        out += ["## Merges applied", ""]
        for g in merges:
            out.append(f"**MERGE** lines {g[0]}–{g[-1]}")
            for ln in g:
                out.append(f"  [{ln}] {preview(lineno_to_text.get(ln, ''))}")
            out.append("")
    if reviews:
        out += ["## REVIEW — human decision needed (not applied)", ""]
        out += ["These lines may fuse two thoughts; a mid-line split is not done automatically.", ""]
        for ln in reviews:
            out.append(f"- [{ln}] {preview(lineno_to_text.get(ln, ''))}")
        out.append("")
    if errors:
        out += ["## Skipped (validation errors)", ""]
        for e in errors:
            out.append(f"- {e}")
        out.append("")
    log_path.write_text("\n".join(out), encoding="utf-8")


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Line-number block re-segmentation for Tibetan commentaries.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input_file", help="Stage-1 segmented commentary with TOC headings")
    parser.add_argument("--commentary-id", default="",
                        help="Short ID for output filenames (inferred from filename if omitted)")
    parser.add_argument("--window-lines", type=int, default=DEFAULT_WINDOW_LINES,
                        help=f"Max content lines per LLM window (default: {DEFAULT_WINDOW_LINES})")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Gemini model (default: {DEFAULT_MODEL})")
    parser.add_argument("--fallback-model", default=DEFAULT_FALLBACK_MODEL,
                        help=f"Fallback model (default: {DEFAULT_FALLBACK_MODEL})")
    parser.add_argument("--force", action="store_true", help="Reprocess all windows even if staged")
    parser.add_argument("--apply-only", action="store_true",
                        help="Skip LLM calls; apply already-staged operations")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run integrity check only; write no output files")
    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.exists():
        sys.exit(f"Error: input file not found: {input_path}")

    cid = args.commentary_id or input_path.stem

    vault_root = input_path.resolve().parent
    for _ in range(8):
        if (vault_root / "4-SYSTEM").exists():
            break
        vault_root = vault_root.parent
    else:
        vault_root = Path(".").resolve()

    staging_dir = vault_root / TEMP_BASE   / f"RESEG-{cid}" / "windows"
    output_path = vault_root / OUTPUT_BASE / f"{cid}.reseg.md"
    log_path    = vault_root / OUTPUT_BASE / f"{cid}.ops.md"

    newline, frontmatter, units = parse_file(input_path)
    n_content = sum(1 for u in units if u["kind"] == "content")
    n_head = sum(1 for u in units if u["kind"] == "heading")

    nl_name = "CRLF" if newline == "\r\n" else "LF"
    print(f"Input:   {input_path}")
    print(f"ID:      {cid}")
    print(f"Lines:   {n_content} content, {n_head} headings  (newline={nl_name})")

    windows = make_windows(units, args.window_lines)
    print(f"Windows: {len(windows)}  (max {args.window_lines} lines each)\n")

    # ── LLM phase ──
    if not args.apply_only:
        client = get_client()
        for win in windows:
            label = f"Window {win['idx']+1}/{len(windows)} (lines {win['lines'][0]['lineno']}–{win['lines'][-1]['lineno']})"
            already = load_window_result(staging_dir, win["idx"])
            if already and not args.force:
                print(f"  {label}: staged ({len(already.get('operations', []))} op) — skip")
                continue
            print(f"  {label}: calling LLM...")
            ops = call_llm_for_window(client, args.model, win, args.fallback_model)
            save_window_result(staging_dir, win, ops)
            print(f"    → {len(ops)} op(s)")
    else:
        print("--apply-only: loading staged results, no LLM calls.")

    # ── load staged ──
    window_results, missing = [], []
    for win in windows:
        r = load_window_result(staging_dir, win["idx"])
        if r is None:
            missing.append(win["idx"] + 1)
        else:
            window_results.append(r)
    if missing:
        print(f"\nWarning: missing staging files for {len(missing)} window(s): {missing[:10]}{'...' if len(missing) > 10 else ''}")
        print("Re-run without --apply-only to process them.\n")

    # ── validate + apply ──
    merges, reviews, errors = validate_operations(window_results, units)
    blocks = apply_operations(units, merges)

    print(f"\nMerges: {len(merges)}   Reviews: {len(reviews)}   Errors: {len(errors)}")
    print(f"Blocks: {n_content} content lines → {len(blocks)} blocks (incl. {n_head} headings)")

    output_text = render_output(frontmatter, blocks, newline)
    ok, detail = check_integrity(input_path, output_text)
    if not ok:
        print("\n✗ INTEGRITY CHECK FAILED")
        print(f"  {detail}")
        print("\nOutput NOT written.")
        sys.exit(1)
    print("✓ Integrity check passed  (squeeze(input) == squeeze(output))")

    if args.dry_run:
        print("\n--dry-run: no files written.")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_text, encoding="utf-8", newline="")
    write_ops_log(log_path, merges, reviews, errors, units, len(blocks), cid)

    print(f"\nOutput:  {output_path}")
    print(f"Ops log: {log_path}")
    if reviews:
        print(f"\n⚑ {len(reviews)} line(s) flagged REVIEW — see ops log.")


if __name__ == "__main__":
    main()
