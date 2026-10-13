# Pass 1 — root text or commentary?

You read digests of Tibetan texts from the collected works of the Nalanda masters (one
digest per file) and decide, for each file, whether it is a **root text** or a
**commentary**. Your decision is read from the text itself; there is no metadata to rely on.

## Input

`0-INBOX/temp/text-relations/digests/<batch>.md` (`root-NN` or `other-NN`) — for each file:
- title, pandita (whose collected works the printed edition put it in), syllable count
- measures: `classify` (a script's guess from gloss markers and metre — a hint only),
  metrical share, gloss markers per 1000 syllables (`ཞེས་པ་ནི`, `ཞེས་བྱ་བ་ནི` … — a commentary
  quotes a word or line of its root and then explains it), whether the title has a
  commentary word
- **contains text of**: other files in our corpus whose text is found inside this one (share of
  *that* file found here). A commentary normally quotes its root, so a high share (30–100%)
  of a shorter verse text is strong evidence that this file comments on it. Two files that
  contain each other at ~100% are copies of one text.
- **its text is found in**: files that contain this one's text
- the opening (title, translated-title formula, homage, statement of intent) and the
  closing (colophon)
- `inbox folder` — sorted by hand earlier from titles: **not evidence**, do not use it

You may open the full file `1-SOURCES/Text/<file>` when the digest leaves a file undecided
(e.g. search it for `ཞེས་པ་ནི` or for the lines it quotes). Read only what you need.

## Decide

**commentary** — the text explains, glosses, summarises or outlines **one specific other
text**. Signs:
- it quotes the other text's words or lines and explains them (`… ཞེས་པ་ནི …`, `… ཞེས་བྱ་བ་
  ལ་སོགས་པ་ནི …`, `… ཞེས་གསུངས་པ་ནི …`), line after line
- the opening or colophon names it as an explanation of a named work: `<work> ཞེས་བྱ་བའི་
  འགྲེལ་པ`, `<work>འི་རྣམ་པར་བཤད་པ`, `<work>འི་དཀའ་འགྲེལ`, `<work>འི་ཊཱི་ཀཱ`, `<work>འི་དོན་
  བསྡུས་པ`, `… བཤད་པར་བྱའོ`, `… འགྲེལ་པ་བྱའོ`
- it contains much of a (usually shorter, verse) file's text — "contains text of"
- an auto-commentary (`རང་འགྲེལ`) is a commentary (on the author's own root)
- a sub-commentary (a commentary on a commentary) is a commentary
- a summary (`བསྡུས་དོན`, `དོན་བསྡུས`), an outline (`ས་བཅད`) or a word-gloss of one
  specific text is a commentary

**root-text** — the text stands on its own: a treatise, verses, praise, prayer, sādhana,
ritual, letter, instruction, tantra, story. Signs:
- it states its own subject, not another text's words
- quoting scripture or other authors as support does **not** make it a commentary — a
  commentary follows one text through, it does not just cite
- a commentary word in the title does **not** decide it: some independent works are called
  `…འགྲེལ་པ` or `…རྣམ་འགྲེལ` (e.g. a verse work titled "commentary on bodhicitta", the
  Pramāṇavārttika `ཚད་མ་རྣམ་འགྲེལ`) — judge by what the text does

**null** — the digest (and a short look at the file, if you took one) does not let you
decide. Better null than a guess.

Also record **named_root**: when the text itself names the work it comments on (in the
title, the opening or the colophon), copy that name in Tibetan exactly as written (no
paraphrase). Otherwise null. Also list any `contains text of` file you think is its root in
`root_candidates` (file names), strongest first.

## Output

Write ONLY a JSON object to `0-INBOX/temp/text-relations/results/pass1-<batch>.json`,
one key per file in the batch, none skipped:

```json
{
  "Na_3C98.md": {
    "file_type": "commentary",
    "confidence": "high",
    "evidence": "Title and opening: སྐུ་གསུམ་ལ་བསྟོད་པ་ཞེས་བྱ་བའི་རྣམ་པར་འགྲེལ་པ; glosses lines with ཞེས་པ་ནི; contains 30% of Na_3C97.md (the praise)",
    "named_root": "སྐུ་གསུམ་ལ་བསྟོད་པ",
    "root_candidates": ["Na_3C97.md"]
  }
}
```

- `file_type`: `"root-text"`, `"commentary"` or `null`
- `confidence`: `"high"` (several independent signs agree), `"medium"` (one clear sign),
  `"low"` (leaning, weak signs)
- `evidence`: one or two English sentences naming the signs and where they are (title,
  opening, closing, glossing, contains …); quote Tibetan words exactly
- never invent Tibetan; never use knowledge about the work that is not in the digest or file

Reply with the output path and the counts (root-text / commentary / null).
