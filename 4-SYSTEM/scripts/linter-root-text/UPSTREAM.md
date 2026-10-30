# Upstream

| | |
|---|---|
| Source repository | https://github.com/WeBuddhist/21-taras-rails |
| Path | `4-SYSTEM/scripts/linter-root-text/` |
| Pinned commit | `2d14cddf9bdd207e34da4eff58b1d0fa98141a5f` (2026-10-01, "Add support for yigchungs in linter and parser") |
| Copied | 2026-10-12 |

Copied byte-identical, without upstream's `output/` folder. Every later commit here is a local delta.

**Why vendored:** this vault needs the same API lint → parse step for its root texts and commentaries.

## Local changes

- 2026-10-12: **durchens** (variant readings written as footnotes `[^n]`). Added `durchen.py`, shared by all four tools. The linter takes footnote definitions out before the block-ID check, which used to fail on them, and checks each marker against its definition and lemma. Not Nalanda-specific: offer it back to 21-taras-rails.
- 2026-10-26: **footnote types.** Labels say what a footnote is: [^dN] durchen, [^nN] generic note; a bare [^N] is still read as a durchen (INFO asks to relabel). A generic note is only checked for a definition (no lemma or span), an unknown label is an ERROR, and durchen.layout_problems() warns when the numbering or the d…/n… grouping of the definitions is off.
- 2026-10-29: **footnotes by position** (shared `durchen.py`): the generic-note label is now `[^fN]` (was `[^nN]`), grouped d…/f…. A footnote is still only checked for a definition (it has a position, so no lemma); the INFO line counts footnotes placed.
- 2026-10-30: **tag_ids** checked more closely: a bare `tag_ids: id` (not a list), an id YAML read as a number/boolean/null (quote it), an id with spaces, and a repeated id are errors with a fix in the message; an empty `tag_ids:` is the same as not set. Same change in linter-commentary.
- 2026-10-26: **odd spaces.** WARN for every space-like or invisible character and every line break other than \n / \r\n in the body (`durchen.odd_characters()`), with the lines; clean the source with `4-SYSTEM/scripts/clean-whitespace/clean_whitespace.py`.
