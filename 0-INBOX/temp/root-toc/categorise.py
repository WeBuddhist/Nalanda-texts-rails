#!/usr/bin/env python3
"""One-time: give every text in the root-text TOC batch a size class, then re-render
0-INBOX/ROOT-TOC-BATCH.md with it.

    py -X utf8 0-INBOX/temp/root-toc/categorise.py

Size = characters of 0-INBOX/root/<id>.md:
    small  <  30,000
    medium    30,000 – 199,999
    large  >= 200,000
The classes decide which Gemini run takes a text (run_gemini_batch.py: --mode low takes
small + medium, --mode medium takes large). Safe to re-run: it only (re)writes the size
fields.
"""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
SMALL, LARGE = 30_000, 200_000


def size_class(chars):
    return "small" if chars < SMALL else "large" if chars >= LARGE else "medium"


def main():
    spec = importlib.util.spec_from_file_location("status", HERE / "status.py")
    st = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(st)
    d = st.load()
    for i, r in d.items():
        chars = len((VAULT / f"0-INBOX/root/{i}.md").read_text(encoding="utf-8"))
        r["chars"], r["size"] = chars, size_class(chars)
    st.save(d)
    st.render(d)
    todo = [r for r in d.values() if r["status"] == "todo"]
    for k in ("small", "medium", "large"):
        print(f"{k:6}: {sum(1 for r in d.values() if r['size'] == k):3} texts, "
              f"{sum(1 for r in todo if r['size'] == k):3} still to do")


if __name__ == "__main__":
    main()
