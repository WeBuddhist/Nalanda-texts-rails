# Upstream

| | |
|---|---|
| Source repository | https://github.com/WeBuddhist/21-taras-rails |
| Path | `4-SYSTEM/scripts/linter-commentary/` |
| Pinned commit | `2d14cddf9bdd207e34da4eff58b1d0fa98141a5f` (2026-10-01, "Add support for yigchungs in linter and parser") |
| Copied | 2026-10-12 |

Copied byte-identical, without upstream's `output/` folder. Every later commit here is a local delta.

**Why vendored:** this vault needs the same API lint → parse step for its root texts and commentaries.

## Local changes

- 2026-10-12: **durchens** (variant readings written as footnotes `[^n]`). Added `durchen.py`, shared by all four tools. The linter takes footnote definitions out before the block-ID check, which used to fail on them, and checks each marker against its definition and lemma. Not Nalanda-specific: offer it back to 21-taras-rails.
- 2026-10-26: **footnote types** (shared `durchen.py`): `[^dN]` durchen, `[^nN]` generic note; a bare `[^N]` is still read as a durchen (INFO asks to relabel). A generic note is only checked for a definition, an unknown label is an ERROR, and layout problems (numbering, d…/n… grouping) are warned. Same change as linter-root-text.
- 2026-10-29: **footnotes by position** (shared `durchen.py`): `[^fN]` replaces `[^nN]`. Same change as linter-root-text.
- 2026-10-30: **tag_ids** checked more closely (not a list, an unquoted id read as a number/boolean/null, spaces, repeats). Same change as linter-root-text.
- 2026-10-26: **odd spaces.** Same WARN as linter-root-text.
