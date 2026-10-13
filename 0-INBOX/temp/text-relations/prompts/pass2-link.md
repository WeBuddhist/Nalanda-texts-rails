# Pass 2 — which text is each commentary a commentary of?

You link commentaries to the text they comment on, inside our corpus of 565 Tibetan texts
(`1-SOURCES/Text/`). Pass 1 has already decided, from each text, whether it is a root text or
a commentary.

## Input

- `0-INBOX/temp/text-relations/digests/<batch>.md` (`link-NN`) — for each commentary: its
  title, the work it names as its root (`named_root`, copied from its title / opening /
  colophon in pass 1, or null), pass 1's root candidates, the text-reuse figures (which of
  our files' text it contains — a commentary quotes its root, so a high share of a shorter
  verse text is strong evidence), and its opening and closing.
- `0-INBOX/temp/text-relations/digests/link-catalog.md` — every file in our corpus with its
  title and pass-1 type (`root-text`, `commentary`, `null`), grouped by type.
- You may open `1-SOURCES/Text/<file>` to check a candidate (e.g. search the commentary for a
  line of the candidate root). Read only what you need.

## Decide, in this order

1. **A root text in our corpus.** Find the file whose title is the work the commentary
   names, and/or whose text the commentary contains. Titles vary in form: `<work> ཞེས་བྱ་བ`,
   `<work>འི་ཚིག་ལེའུར་བྱས་པ`, a short name vs a full name, `༼སྟོད་ཆ།༽` / `༼སྨད་ཆ།༽` volume
   marks — match the work, not the exact string. When a root exists in several copies
   (duplicates), pick the one the commentary quotes most.
2. **Otherwise a commentary in our corpus** — a sub-commentary comments on a commentary
   (e.g. a `…དཀའ་འགྲེལ` or `…རྣམ་བཤད` on a named `…འགྲེལ་པ`). Same evidence.
3. **Otherwise null** — the commentary's root is not in our corpus (e.g. a sūtra, or a work
   by someone outside these 17 masters), or the evidence does not settle it. Do not force a
   match; record the named root in the evidence so a person can look for it later.

Evidence must come from the texts: the name in the commentary's title, opening or
colophon, and/or the quoted text (the reuse share, or a line you found). Never decide from
knowledge about the works that is not in the files.

## Output

Write ONLY a JSON object to `0-INBOX/temp/text-relations/results/pass2-<batch>.json`, one key
per commentary in the batch, none skipped:

```json
{
  "Na_3C98.md": {
    "commentary_of": "Na_3C97.md",
    "link_confidence": "high",
    "link_evidence": "Title names སྐུ་གསུམ་ལ་བསྟོད་པ, the title of Na_3C97.md; it contains 30% of Na_3C97.md's text (the verses it glosses)"
  },
  "Xx_0000.md": {
    "commentary_of": null,
    "link_confidence": null,
    "link_evidence": "Names its root as <Tibetan name as written>; no file in our corpus has this title or shares its text"
  }
}
```

- `commentary_of`: a file name from `link-catalog.md`, or null
- `link_confidence`: `"high"` (named and quoted), `"medium"` (one clear sign), `"low"`
  (leaning), or null with a null link
- `link_evidence`: one or two English sentences; quote Tibetan exactly
- if pass 1 was wrong and the file is not a commentary at all, set `commentary_of` null and
  say so in `link_evidence` (start it with `NOT A COMMENTARY:`)

Reply with the output path and the counts (linked to a root text / linked to a commentary /
null).
