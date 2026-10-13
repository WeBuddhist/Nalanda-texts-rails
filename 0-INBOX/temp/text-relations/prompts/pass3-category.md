# Pass 3 — which category does each text belong to?

You assign each Tibetan text in your batch to **one of our 13 backend categories**. These
texts have no category from any source; you decide by reading them.

## Input

- `0-INBOX/temp/text-relations/digests/cat-guide.md` — the 13 categories, each with real
  example titles filed under it. **Read it first; follow the practice it shows.**
- `0-INBOX/temp/text-relations/digests/<batch>.md` (`cat-NN`) — for each text: title,
  pandita (whose collected works it is in), file_type (root-text / commentary), metre and
  gloss measures, the text it comments on (with that text's category, when known), and its
  opening and closing (colophon).
- You may open `1-SOURCES/Text/<file>` when the digest leaves it unclear. Read only what you need.

## Decide

Classify by **what the text is about and what it is for**, the way the examples are filed:
- **Tantras** — tantric material: sādhanas, maṇḍala rites, empowerments, fire offerings, torma
  rites and other tantric rituals, tantric instructions, completion-stage teachings, and
  commentaries on tantras (the guide shows that OpenPecha files sādhanas and tantric rites here)
- **Liturgy** — texts for recitation in practice: prayers, aspirations, praises and
  supplications that are recited, daily recitations — follow the guide's examples
- **Middle Way** — Madhyamaka treatises and their commentaries
- **Mind-only Treatises** — Yogācāra / Cittamātra treatises and their commentaries
- **Logic** — pramāṇa: epistemology and logic
- **Systematic Treatises** — Abhidharma
- **Prajñāpāramitā** — the Perfection of Wisdom sūtras and the treatises and commentaries on them
  (Abhisamayālaṃkāra literature)
- **Discourses** — sūtras, and commentaries on particular sūtras (other than Prajñāpāramitā)
- **Monastic Rules** — Vinaya
- **Mind Trainings and Advices** — advice, letters, instructions for practice, mind training
- **Linguistics Treatises** — grammar, poetics, medicine and other sciences (rig gnas)
- **History and Stories** — narratives, jātakas, histories
- **Miscellaneous** — clearly outside all of the above

A commentary normally goes with its root's category (`commentary on … (category: X)`).
Praises: a praise of the dharmadhātu or of a buddha in philosophical verse may belong with
Middle Way, a praise for recitation with Liturgy — use the guide's examples and the content.

If no category really fits, or the text is broken (e.g. only a table of contents), give `null`.

## Output

Write ONLY a JSON object to `0-INBOX/temp/text-relations/results/pass3-<batch>.json`, one key
per text in the batch, none skipped:

```json
{
  "Na_3C9R.md": {
    "category": "Tantras",
    "category_confidence": "high",
    "category_evidence": "A Mahākāla sādhana: opening sets up the deity visualisation and mantra (…); guide files sādhanas under Tantras"
  }
}
```

- `category`: exactly one of the 13 names as written in the guide's headings (`Tantras`,
  `Liturgy`, `Middle Way`, `Mind-only Treatises`, `Logic`, `Systematic Treatises`,
  `Prajñāpāramitā`, `Discourses`, `Monastic Rules`, `Mind Trainings and Advices`,
  `Linguistics Treatises`, `History and Stories`, `Miscellaneous`), or null
- `category_confidence`: `"high"`, `"medium"` or `"low"`
- `category_evidence`: one or two English sentences; quote Tibetan exactly

Reply with the output path and the counts per category.
