# Root-text segmentation: raw paragraphs

2026-10-08

The paragraphs in the raw root texts were made by the book's editors to follow the meaning, not to fit the printed pages. We will keep every raw paragraph break and only cut further inside paragraphs.

## What the check showed

All 565 files have the same text and the same paragraph breaks as the Word books they came from. The breaks follow meaning:

| Check | Result |
| --- | --- |
| Page breaks that fall inside a paragraph | 95% (33,015 of 34,683) |
| Paragraphs that end at a sentence or verse-line end | over 99% (21,025 of 21,185) |
| Where breaks fall | end of a chapter (after its closing line), a new topic or ritual stage, a change of speaker in a dialogue |

The paragraphs are coarse, though. 107 files are a single paragraph, and about half have five or fewer. Verse is run together with no line breaks, so most of the segmentation is still ours to do.

## How many of the 565 files this works for

We are confident in 421 files and, after a quick check of a few breaks, 35 more: 456 of 565 (81%). For another 107 the rule is safe but gives no help. 2 need separate handling.

| Files | Count | Confidence | Why |
| --- | --- | --- | --- |
| Every raw break ends a sentence or verse line | 421 | High | The breaks can be kept as they are. About 190 of these have only 2–5 paragraphs, so most of their cutting is still ours. |
| One to three doubtful breaks | 35 | High after review | 42 breaks in all end mid-sentence or on a connective (e.g. `…ཏེ། །`, `…ནས།`). A person checks them before they count as fixed. In most of these files that is 1 break out of 100–580. |
| A single paragraph (the whole text) | 107 | Depends on our own segmentation | There are no raw breaks to keep, so the result is only as good as our stanza and paragraph grouping. |
| The book's printed contents list, not text (As_3CDy_, As_3CDz_) | 2 | Does not apply | Lines of titles with page numbers. These need separate handling. |

## Headings

About 70% of section headings (48 of 69, in the root texts we processed) fall at a raw paragraph break. Every chapter that ends with its closing line (`…ཆོ་ག་སྟེ་དང་པོའོ།། །།`) ends its paragraph there.

The rest start inside a paragraph, always at a sentence end:

- the first section, which shares a paragraph with the title and homage;
- the colophon, which is the tail of the last paragraph;
- some stages in ritual texts that begin with `དེ་ནས་…` or `དེའི་རྗེས་ལ་…` without a new paragraph.

## The new approach

1. Keep every raw paragraph break. Never join two raw paragraphs into one block.
2. Cut only inside a paragraph: verse into stanzas, prose into smaller paragraphs of one point or one step each.
3. A heading may split a paragraph at a sentence end: after the front matter, before the colophon, or where the text marks a new stage.
4. Flag doubtful breaks (mid-sentence, or ending on a connective) for a person to check instead of keeping them as fixed.
5. Handle the two contents-list files separately.

## Effect on the outputs already shared

The current skill sometimes merges across raw paragraph breaks, most often in prose. Once the rule is in, these outputs will be rebuilt:

| Output | Raw breaks | Merged into one of our blocks |
| --- | ---: | ---: |
| Ar_3CBc_ (prose) | 168 | 69 |
| Ar_3CBa_ (verse) | 81 | 13 |
| Ar_3CBh_ (prose) | 34 | 11 |
| Na_3CBI (verse) | 23 | 7 |
