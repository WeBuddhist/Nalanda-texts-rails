# Stanza grouping (sense mode) — root-text-segmentation

Produces the `free` version, which every verse root text gets. A text translated from Sanskrit
(`རྒྱ་གར་སྐད་དུ།` title) also gets a `sloka` version, counted by the script — that does not
change this task: group by sense as below. Measured on
10 Liturgy-rails texts: block-boundary F1 0.95, 93% of the editors' blocks reproduced exactly
(the earlier 2/4/6-only rule: 0.68 / 59%).

You receive a Tibetan verse text (a prayer, praise, aspiration or liturgy) already cut into
lines. Each line is `P<n>  <text>`. Lines end with `། །`, `ག །`, `༔`, `ཿ` or similar. `[^n]`
markers are footnote references — ignore them for meaning.

Your task: group the lines into blocks as a careful editor of a chanting text would — one
block per stanza or self-contained unit. If the input has headings (`## …`), a block never
crosses one — group each section separately. Lines marked `[frame]` (titles, homage,
colophons) are not part of any block and are not numbered.

How editors group (measured on 94 edited chanting texts: 72% of blocks are 4 lines, the
rest follow the sense — 5 lines 11%, 6 lines 4%, 3 lines 3%, 7 lines 3%, 1–2 lines 4%):

1. **Four lines is the default.** Count four lines at a time unless the sense says otherwise.
2. **A block ends where a sentence or petition ends.** Finite endings close a unit:
   `…ཤོག`, `…གསོལ་བ་འདེབས།`, `…ཕྱག་འཚལ་ལོ།`, `…མཛད་དུ་གསོལ།`, `…བྱིན་གྱིས་རློབས།`, `…འོ།`,
   an imperative or optative. Connective endings (`…སྟེ།` `…ཏེ།` `…ནས།` `…ཞིང་།` `…ཅིང་།`
   `…ལ།` `…ནི།`, genitive `…གི།` `…ཡི།` `…འི།`, `…དང་།`) mean the sentence continues.
   - If line 4 does not close the sentence, extend the block to where it closes (5–8 lines).
   - If a sentence closes after 2 or 3 lines and the next lines start a new unit, end the
     block there.
   - A refrain or repeated petition line that closes each stanza belongs to that stanza.
3. **Lead lines attach forward.** A short invocation or exclamation in a different length
   from the verse (`ན་མོ། …`, `ཨེ་མ་ཧོ།`, `ཀྱེ༔`, `ཧཱུཾ༔`, a homage formula introducing the
   stanza) belongs to the block it introduces, not to its own block and not to the block
   before.
4. **Prose rubrics stand alone.** A line that is not verse but an instruction or a
   colophon-like remark (`ཞེས་ལན་གསུམ།`, `…ཞེས་པ་འདི་ནི་…`, `ཅེས་…གྱིས་སྦྱར་བའོ།`) is its own
   block.
5. Never reorder or skip a line; every line belongs to exactly one block. Prefer four-line
   blocks whenever the sense allows them — deviate only for a reason in rules 2–4.

Output: write ONLY a JSON object to the output path:

```json
{"stanzas": [[1, 4], [5, 8], …],
 "notes": {"<first line of every block that is not 4 lines>": "one short English reason"}}
```

`[a, b]` = lines a..b inclusive, all blocks in order, covering every line exactly once.
