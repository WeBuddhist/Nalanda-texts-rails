# Upstream

| | |
|---|---|
| Source repository | https://github.com/WeBuddhist/21-taras-rails |
| Path | `4-SYSTEM/scripts/parser-root-text/` |
| Pinned commit | `2d14cddf9bdd207e34da4eff58b1d0fa98141a5f` (2026-10-01, "Add support for yigchungs in linter and parser") |
| Copied | 2026-10-12 |

Copied byte-identical, without upstream's `output/` folder. Every later commit here is a local delta.

**Why vendored:** this vault needs the same API lint → parse step for its root texts and commentaries.

## Local changes

- 2026-10-12: **durchens** (variant readings written as footnotes `[^n]`). Added `durchen.py`, shared by all four tools. The parser strips markers from `content` and TOC titles and writes `<stem>.durchens.json`. Not Nalanda-specific: offer it back to 21-taras-rails.
- 2026-10-26: **footnote types.** Labels say what a footnote is: [^dN] durchen, [^nN] generic note; a bare [^N] is still read as a durchen until the sources are relabelled. Generic notes have no API endpoint yet: their markers are stripped from content and they are logged (NOTE …) but not sent. durchen.py gained kind(), is_durchen() and layout_problems(). Relabel sources with 4-SYSTEM/scripts/footnote-labels/relabel_footnotes.py.
