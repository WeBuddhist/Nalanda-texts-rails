# Upstream

| | |
|---|---|
| Source repository | https://github.com/WeBuddhist/21-taras-rails |
| Path | `4-SYSTEM/scripts/parser-commentary/` |
| Pinned commit | `2d14cddf9bdd207e34da4eff58b1d0fa98141a5f` (2026-10-01, "Add support for yigchungs in linter and parser") |
| Copied | 2026-10-12 |

Copied byte-identical, without upstream's `output/` folder. Every later commit here is a local delta.

**Why vendored:** this vault needs the same API lint → parse step for its root texts and commentaries.

## Local changes

- 2026-10-12: **durchens** (variant readings written as footnotes `[^n]`). Added `durchen.py`, shared by all four tools. The parser strips markers from `content` and TOC titles and writes `<stem>.durchens.json`. Not Nalanda-specific: offer it back to 21-taras-rails.
- 2026-10-26: **footnote types** (shared `durchen.py`): only `[^dN]` (and the old bare `[^N]`) become durchens. Generic notes `[^nN]` have no API endpoint yet: their markers are stripped from `content` and they are logged (`NOTE …`) but not sent. Same change as parser-root-text.
- 2026-10-29: **footnotes by position** (shared `durchen.py`): `[^fN]` footnotes (was `[^nN]`) get a position, the gap where the marker stood, written to `<stem>.footnotes.json`. Same change as parser-root-text.
- 2026-10-26: **odd spaces.** Same as parser-root-text: content, TOC titles and durchen texts go through `durchen.normalize_spaces()`.
