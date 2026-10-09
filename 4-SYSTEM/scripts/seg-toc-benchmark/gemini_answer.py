#!/usr/bin/env python3
"""
Answer prompt files with the Gemini API — the same prompt files the Claude agents
answered in the model comparison (exact SYSTEM PROMPT + USER PROMPT the skills send).

    python gemini_answer.py <prompt-file-or-dir>... [--model gemini-3.8-flash]
                            [--thinking low|medium|high] [--max-output 32768]

  window-NNNN.prompt.md → window-NNNN.response.json   (re-segmentation, JSON mode)
  call-NNN.prompt.md    → call-NNN.response.txt       (QC, JSON mode)
  tree.prompt.md        → verse-tree.md               (heading tree, plain text)

Prompt files that already have an answer are skipped. Each answer also gets a
<answer>.meta.json (model, thinking level, tokens incl. thinking, seconds,
finish reason), and every call is appended to 0-INBOX/bench8/gemini-usage.jsonl.

Settings follow Google's guidance for Gemini 3+: temperature left at its default
(1.0 — lower values can cause looping), effort set with thinking_level (thinking
cannot be switched off on 3.8 Flash), max_output_tokens counts thinking tokens too.
A reply cut off by the token limit is an error, never a partial answer.

The API key is read by _gemini_api_key() from the vault-root .env (or the
environment); it is never printed or written anywhere.
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

DEFAULT_MODEL = "gemini-3.8-flash"
DEFAULT_THINKING = "high"
MAX_RETRIES = 5


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


_client = None


def client():
    global _client
    if _client is None:
        try:
            from google import genai
        except ImportError:
            sys.exit("Error: the google-genai package is missing — run:  pip install google-genai")
        key = _gemini_api_key()
        if not key:
            sys.exit("Error: no Gemini API key found.\n  Put GEMINI_API_KEY=your-key in the .env file at "
                     "the vault root (next to 4-SYSTEM/), or set it in the environment.")
        _client = genai.Client(api_key=key)
    return _client


def split_prompt(text):
    m = re.match(r"=== SYSTEM PROMPT ===\n(.*?)\n=== USER PROMPT ===\n(.*)\Z", text, re.S)
    if not m:
        raise ValueError("prompt file lacks the '=== SYSTEM PROMPT ===' / '=== USER PROMPT ===' sections")
    return m.group(1), m.group(2)


def answer_path(p: Path):
    if p.name == "tree.prompt.md":
        return p.with_name("verse-tree.md"), False
    if p.name.startswith("window-"):
        return p.with_name(p.name.replace(".prompt.md", ".response.json")), True
    if p.name.startswith("call-"):
        return p.with_name(p.name.replace(".prompt.md", ".response.txt")), True
    raise ValueError(f"don't know where the answer for {p.name} goes")


def strip_fences(s):
    s = s.strip()
    m = re.match(r"^```[a-zA-Z]*\n(.*)\n```$", s, re.S)
    return m.group(1).strip() if m else s


def ask(prompt_file: Path, model: str, thinking: str, max_output: int, usage_log: Path | None):
    from google.genai import types
    out, is_json = answer_path(prompt_file)
    system, user = split_prompt(prompt_file.read_text(encoding="utf-8"))
    cfg = types.GenerateContentConfig(
        system_instruction=system,
        thinking_config=types.ThinkingConfig(thinking_level=thinking),
        max_output_tokens=max_output,
        response_mime_type="application/json" if is_json else None,
    )
    err = None
    for attempt in range(1, MAX_RETRIES + 1):
        t0 = time.time()
        try:
            r = client().models.generate_content(model=model, contents=user, config=cfg)
        except Exception as e:  # noqa: BLE001 — transient API errors: back off and retry
            err = e
            wait = min(60, 4 * 2 ** (attempt - 1))
            print(f"    ! {prompt_file.name}: {type(e).__name__}: {str(e)[:160]} — retry {attempt}/{MAX_RETRIES} in {wait}s")
            time.sleep(wait)
            continue
        secs = time.time() - t0
        cand = (r.candidates or [None])[0]
        finish = str(getattr(cand, "finish_reason", "") or "")
        text = strip_fences(r.text or "")
        um = r.usage_metadata
        meta = {
            "prompt": str(prompt_file), "model": model, "thinking_level": thinking,
            "max_output_tokens": max_output, "finish_reason": finish, "seconds": round(secs, 1),
            "input_tokens": getattr(um, "prompt_token_count", None),
            "output_tokens": getattr(um, "candidates_token_count", None),
            "thinking_tokens": getattr(um, "thoughts_token_count", None),
            "attempt": attempt,
        }
        if "MAX_TOKENS" in finish:
            err = RuntimeError(f"reply cut off at max_output_tokens={max_output} (thinking counts too)")
            print(f"    ! {prompt_file.name}: {err} — retry {attempt}/{MAX_RETRIES}")
            continue
        if is_json:
            try:
                json.loads(text)
            except ValueError as e:
                meta["json_error"] = str(e)[:200]
                err = e
                print(f"    ! {prompt_file.name}: reply is not valid JSON ({e}) — retry {attempt}/{MAX_RETRIES}")
                continue
        out.write_text(text + "\n", encoding="utf-8")
        out.with_name(out.name + ".meta.json").write_text(json.dumps(meta, indent=1), encoding="utf-8")
        if usage_log:
            usage_log.parent.mkdir(parents=True, exist_ok=True)
            with usage_log.open("a", encoding="utf-8") as f:
                f.write(json.dumps(meta, ensure_ascii=False) + "\n")
        return meta
    raise SystemExit(f"Gemini call failed for {prompt_file} after {MAX_RETRIES} attempts: {err}")


def pending(paths):
    for p in paths:
        p = Path(p)
        files = sorted(p.glob("*.prompt.md")) if p.is_dir() else [p]
        for f in files:
            if not answer_path(f)[0].exists():
                yield f


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--thinking", default=DEFAULT_THINKING, choices=["minimal", "low", "medium", "high"])
    ap.add_argument("--max-output", type=int, default=32768)
    ap.add_argument("--usage-log", default="0-INBOX/bench8/gemini-usage.jsonl")
    a = ap.parse_args()
    for f in pending(a.paths):
        m = ask(f, a.model, a.thinking, a.max_output, Path(a.usage_log))
        print(f"  {f.name}: {m['seconds']}s, thinking {m['thinking_tokens']} tok, output {m['output_tokens']} tok")


if __name__ == "__main__":
    main()
