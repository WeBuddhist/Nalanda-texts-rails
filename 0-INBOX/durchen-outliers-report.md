# Durchen outliers: footnotes with no `༼…༽` witness

## Update 2026-10-13: current `1-SOURCES/Text/` (442 root texts)

`1-SOURCES/Text/` was replaced by the processed root texts, which have frontmatter, block IDs and headings, so **the line numbers further down are out of date**. The current state:

- **12 of the 24 notes are still in root texts.** Their current lines are below. All 12 texts are held from the API linter/parser batch (`0-INBOX/temp/api-lint/holds.json`), together with `Sh_3CCm_` (held by request).
- **The other 12 are no longer in `1-SOURCES/Text/`.** Those files are commentaries: `Di_3CEo_`, `Di_3CEr_`, `Ha_3CFM`, `Sh_3CDC`, `Va_3CEA`, `Va_3CEK`. They cover all 9 lemma-only notes (A1–A9) plus C12, C13 and C14. Fix them wherever the commentaries now live.

| Ref | File | Note | Marker line | Def line |
|---|---|---|---|---|
| B1 | `Na_3CAN.md` | `[^75]` | 151 | 245 |
| C1 | `Ch_3CCU.md` | `[^1]` | 36 | 38 |
| C2 | `Na_3C9x_.md` | `[^1]` | 38 | 40 |
| C3 | `Na_3C9y_.md` | `[^2]` | 41 | 44 |
| C4 | `Sh_3CCh_.md` | `[^1]` | 37 | 39 |
| C5 | `Sh_3CCi_.md` | `[^2]` | 37 | 40 |
| C6 | `Na_3C9s_.md` | `[^1]` | 44 | 46 |
| C7 | `Ch_3CCV.md` | `[^1]` | 29 | 189 |
| C8 | `Dh_3CF3.md` | `[^40]` | 92 | 133 |
| C9 | `Sh_3CD6.md` | `[^1]` | 270 | 272 |
| C10 | `Sh_3CD7.md` | `[^1]` | 264 | 266 |
| C11 | `At_3CHK.md` | `[^3806]` | 4894 | 8701 |

---

Generated 2026-10-13 from `1-SOURCES/Text/` (553 root texts, 217,233 footnotes).

The durchen tools (`4-SYSTEM/scripts/linter-*`, `parser-*`, shared logic in `durchen.py`) expect every footnote to read:

```
[^n]: <lemma> ༼<witness sigla>༽ <variant>
```

The **lemma** sets the durchen's span: it is matched backwards from the marker. **24 footnotes have no `༼…༽`**, so there is no lemma to match. For those the tools fall back to the syllable before the marker and print a warning. One of them is an error (no text before the marker).

**Line numbers** are for `1-SOURCES/Text/<file>`: *marker* is the line with `[^n]` in the text, *def* is the `[^n]: …` line at the end of the file. The same notes also sit in the `0-INBOX/` copies of each file (`root/`, `commentary/`, `processed/…`, `Nalanda_docx/…/works/`). Fix them at the source you re-run from, or in all copies.

`1-SOURCES/` is read-only for agents. **Every fix below is a suggestion for a human editor.**

## Summary

| Kind | Count | Tool result today | Suggested fix |
|---|---|---|---|
| A. Lemma only: witness and variant missing | 9 | Warning. Span is the last syllable: right for 4, **too short for 5** | Restore `༼sigla༽ variant` from the Pedurma. Tool fix: use the whole note as the lemma when it matches |
| B. Typo: `༽` without `༼` | 1 | Warning. Treated as editorial | Add the missing `༼` |
| C. Editorial note: not a variant reading | 14 | Warning (**1 error**). Span is the last syllable | Decide policy: keep as a durchen, or move to frontmatter / main text |

---

## A. Lemma only: the witness and variant are missing (9)

The note is just the base reading: it matches the text before the marker, but says nothing about which edition differs or how. The variant was probably lost when the .docx was made.

| # | File | Marker | Def | Note | Text before marker | Span today | Span with the tool fix |
|---|---|---|---|---|---|---|---|
| A1 | `Di_3CEo_.md` | 99 | 755 | `[^425]: འདི་ལྟ་སྟེ་` | …ཡོད་དེ། འདི་ལྟ་སྟེ༌ | `སྟེ༌` ✗ | `འདི་ལྟ་སྟེ༌` |
| A2 | `Di_3CEo_.md` | 117 | 843 | `[^513]: རང་` | …དེ་ཡང་། རང༌ | `རང༌` ✓ | `རང༌` |
| A3 | `Di_3CEo_.md` | 259 | 1644 | `[^1314]: གསུམ་ཡང་` | …གཞན་གསུམ་ཡང་། གསུམ་ཡང༌ | `ཡང༌` ✗ | `གསུམ་ཡང༌` |
| A4 | `Sh_3CDC.md` | 25 | 182 | `[^118]: རིགས་པའི་ཚུལ་གྱིས་` | …ཡང་རུང་སྟེ། རིགས་པའི་ཚུལ་གྱིས༌ | `གྱིས༌` ✗ | `རིགས་པའི་ཚུལ་གྱིས༌` |
| A5 | `Va_3CEA.md` | 151 | 1381 | `[^775]: དེ་` | …ཡིན་ཏེ། དེ༌ | `དེ༌` ✓ | `དེ༌` |
| A6 | `Va_3CEA.md` | 223 | 1663 | `[^1057]: ཟབ་པ་ནི་གང་གི་ཕྱིར་` | …ཆེ་བའི་ཕྱིར། ཟབ་པ་ནི་གང་གི་ཕྱིར༌ | `ཕྱིར༌` ✗ | `ཟབ་པ་ནི་གང་གི་ཕྱིར༌` |
| A7 | `Va_3CEA.md` | 241 | 1769 | `[^1163]: དེས་` | …བརྩམས་པ་སྟེ། དེས༌ | `དེས༌` ✓ | `དེས༌` |
| A8 | `Va_3CEA.md` | 257 | 1869 | `[^1263]: གནོད་པ་མེད་པ་` | …སྒྲིབ་པ་མེད་པ། གནོད་པ་མེད་པ༌ | `པ༌` ✗ | `གནོད་པ་མེད་པ༌` |
| A9 | `Va_3CEA.md` | 479 | 2806 | `[^2200]: དེ་` | …སོང་བ་ནི་གང་གི་ཕྱིར། དེ༌ | `དེ༌` ✓ | `དེ༌` |

**Suggested fix**

1. **Source:** look the passage up in the Pedurma (བསྟན་འགྱུར་དཔེ་བསྡུར་མ) and complete the note, e.g. `[^1057]: ཟབ་པ་ནི་གང་གི་ཕྱིར་ ༼སྣར། པེ།༽ <variant>`. If the variant is an omission in a witness, write it the way the Pedurma does.
2. **Tool:** when a note has no `༼` but the whole note matches the text before the marker, use it as the lemma, and keep a warning that the witness is missing. This makes A1, A3, A4, A6 and A8 span correctly until the sources are completed. It is a few lines in `durchen.py` (all four copies). **Not done yet.**

---

## B. Typo: the opening `༼` is missing (1)

| # | File | Marker | Def | Note | Text before marker | Span today |
|---|---|---|---|---|---|---|
| B1 | `Na_3CAN.md` | 15 | 99 | `[^75]: ཞེས་པ། པེ། སྣར།༽ བཞེས།` | …མེ་ཏོག་དམ་པ་འདི། །ཞེས་པ༌ | `པ༌` |

**Suggested fix:** add the `༼`. The note then parses normally, with lemma `ཞེས་པ།` and span `ཞེས་པ༌`:

```
[^75]: ཞེས་པ། ༼པེ། སྣར།༽ བཞེས།
```

---

## C. Editorial notes: not variant readings (14)

These carry information *about* the text (where it was compiled from, its publication, its colophon), not a different reading of a word. Today each becomes a durchen on the last syllable before the marker. The API accepts that, but a reader will see a "variant" that is really a catalogue remark.

**Policy decision needed (once, for all of section C):**

- **Option 1: keep as durchens** on the syllable before the marker, as now. Nothing to change except C7, which is an error. The cost: the API mixes editorial remarks in with variant readings.
- **Option 2: take them out of the durchen layer.** Bibliographic and catalogue notes go to the file's frontmatter (e.g. `source_description`, or a new `editorial_notes:` field). Colophon verses go into the text as their own back-matter block, if the edition should include them. Then remove the marker and the definition. Recommended, but each one needs an editor's call.

### C-i. Compiler's note on an anthology extract (6)

The note says the verse was taken from a compilation (ཆོས་ཚན་) of verses by several masters and inserted here under the author's name. It is the same note, in two wordings, on six texts.

| # | File | Marker | Def | Marker sits after | Note (start) | Span today |
|---|---|---|---|---|---|---|
| C1 | `Ch_3CCU.md` | 13 | 15 | `གསུང་ངོ་།།` | ཆོས་ཚན་འདི་ཉིད་ནང་། ཀླུ་སྒྲུབ་དང་། ཤཱནྟ་དེ་བ། … ཞལ་སྐོང་ཞུས་པའོ།། | `ངོ་།།` |
| C2 | `Na_3C9x_.md` | 11 | 13 | `གསུང་ངོ་། །` | ཆོས་ཚན་འདི་ཉིད་ནང་། ཀླུ་སྒྲུབ་དང་། ཤཱནྟ་དེ་བ། … ཞལ་སྐོང་ཞུས་པའོ།། | `ངོ་། །` |
| C3 | `Na_3C9y_.md` | 13 | 16 | `གསུང་ངོ་།།` | ཆོས་ཚན་འདི་ཉིད་ནང་། ཀླུ་སྒྲུབ་དང་། ཕྱོགས་ཀྱི་གླང་པོ། བྷུ་སུ་ཀུ་ … ཞལ་སྐོང་ཞུས་པའོ།། | `ངོ་།།` |
| C4 | `Sh_3CCh_.md` | 13 | 15 | `གསུང་ངོ་།།` | (same as C1) | `ངོ་།།` |
| C5 | `Sh_3CCi_.md` | 13 | 16 | `གསུང་ངོ་།།` | (same as C3) | `ངོ་།།` |
| C6 | `Na_3C9s_.md` | 13 | 15 | `…གཞོན་ནུ་དཔལ་གྱིས་བསྒྱུར་བའོ` | དཀར་ཆག་གི་ཟུར་མཆན། གོང་གསལ་ཆོས་ཚན་འདི་ཉིད་ནང་ … གྲུབ་མཐའ་བདུན་པ་ལས་འདི་ཉིད་གསུམ་པ་ཡིན་ནོ།། | `བའོ` |

**Suggested fix:** move the note to frontmatter (it describes where the whole text comes from), and remove the marker and definition. C6 calls itself a catalogue side note (དཀར་ཆག་གི་ཟུར་མཆན), which supports this.

### C-ii. Title note (1): the linter rejects this one

| # | File | Marker | Def | Where the marker is | Note | Result today |
|---|---|---|---|---|---|---|
| C7 | `Ch_3CCV.md` | 3 | 11 | At the **start** of the first block, right after the title heading `## ༄༅། །ཐུགས་རྗེ་ཆེན་པོ་ལ་སྨྲེ་སྔགས་ཀྱིས་བསྟོད་པ་བྱིན་རླབས་ཅན།` | `མཚན་བྱང་འདི་ཆོས་ཚན་འདིའི་མཚན་བོད་སྐད་དུ་སྨོས་པ་ལྟར་བཀོད།` ("this title is given as the compilation names it in Tibetan") | **ERROR**: no text before the marker (headings are not edition content). The parser skips it |

**Suggested fix:** the note is about the title, so move it to frontmatter next to `title`, and remove the marker and definition. Moving the marker onto the heading line does not help: footnotes in headings get no durchen.

### C-iii. Bibliographic source citation (3)

| # | File | Marker | Def | Marker sits after | Note | Span today |
|---|---|---|---|---|---|---|
| C8 | `Dh_3CF3.md` | 16 | 57 | `…ཏཱ་ར་ནཱ་ཐས་ (1575-1634) མཛད་པའི་རྒྱ་གར་ཆོས་འབྱུང་ལས`, inside an editor's note `༼རྩོམ་སྒྲིག་པའི་མཆན། …` | `རྒྱ་གར་ཆོས་འབྱུང་། སི་ཁྲོན་མི་རིགས་དཔེ་སྐྲུན་ཁང་། ༡༩༨༦ ལོ། ཤོག་གྲངས་ ༢༡༤༦` | `ལས` |
| C9 | `Sh_3CD6.md` | 69 | 71 | `…མདོ་སྡེའི་ཆོ་ག་རྫོགས་སོ།།` (end of text) | `མཁན་ཆེན་ཞི་བ་འཚོའི་གསུང་འབུམ། བོད་ལྗོངས་མི་དམངས་དཔེ་སྐྲུན་ཁང་ … ༢༠༡༣ … ཤོག་གྲངས་ ༣༣༠ ནས་ ༣༨༤ …` | `སོ།།` |
| C10 | `Sh_3CD7.md` | 71 | 73 | `…སློབ་དཔོན་ཞི་བ་འཚོས་མཛད་པ། རྫོགས་སོ།།` (end of text) | `མཁན་ཆེན་ཞི་བ་འཚོའི་གསུང་འབུམ། … ༢༠༡༣ … ཤོག་གྲངས་ ༣༨༥ ནས་ ༤༢༥ …` | `སོ།།` |

**Suggested fix:**
- **C9, C10:** this is the file's source edition (Zhi ba 'tsho's collected works, 2013, with page range). Put it in `source_description` (and the page range in a source field), then remove the marker and definition.
- **C8:** a citation inside an editor's own note, giving the edition of Tāranātha's history being quoted. Keep it with that note. Either fold it into the `༼རྩོམ་སྒྲིག་པའི་མཆན། …༽` text, or keep it as a durchen but move the marker so it closes the title: `རྒྱ་གར་ཆོས་འབྱུང་[^40]ལས`. Even then the span is only `འབྱུང་`, unless the tool fix in A also accepts a note that *starts* with the text before the marker.

### C-iv. Colophon and editorial remarks at the end of a text (4)

| # | File | Marker | Def | Marker sits after | Note | Span today |
|---|---|---|---|---|---|---|
| C11 | `At_3CHK.md` | 495 | 4302 | `…ལྟུང་དང་ཉོན་མོངས་གདུང་བ་ཞི་གྱུར་ཅིག ། ` (end of text) | 26 lines of verse: aspiration prayer plus translation colophon (པ་ཚབ་ … བསྒྱུར་ཅིང་ལེགས་པར་ཞུས།) | `ཅིག །` |
| C12 | `Di_3CEr_.md` | 225 | 1883 | `…བྱང་ཆུབ་མྱུར་ཐོབ་ཤོག།` (end of text) | Translator colophon: `རྒྱ་གར་གྱི་མཁན་པོ་ … བ་སུ་དྷ་ར་རཀྵི་ཏ་དང་། བོད་ཀྱི་ལོ་ཙཱ་བ་ཞ་མ་དགེ་བསྙེན་སེང་རྒྱལ་གྱིས་བསྒྱུར་ཅིང་ཞུས་ཏེ་གཏན་ལ་ཕབ་པའོ།། །།` | `ཤོག།` |
| C13 | `Ha_3CFM.md` | 187 | 1371 | `…འབྲོ་སེང་དཀར་ཤཱཀྱའི་འོད་ཀྱིས་བསྒྱུར་བའོོ།། ` (end of text) | 18 lines of translator's verse colophon (བློ་ངན་ཚོང་པ་ … འབད་པས་བལ་ཡུལ་བགྲོད་ནས་བདག་གིས་བསྒྱུར། …) ending `མངྒལཾ།། །།` | `བའོོ།།` |
| C14 | `Va_3CEK.md` | 185 | 2041 | `…མཛོད་ཀྱི༌གནས་ལྔ་པའོ།། །།སརྦ་མངྒཱ་ལཾ།། །།` (end of text) | `བསྟན་འགྱུར་ནང་མཛོད་གནས་ལྔ་པ་ཡན་སྟོད་ཆ་དང་། ཕྱི་མ་གསུམ་སྨད་ཆར་བཀོད་འདུག་ཀྱང་། འདིར་སྟོད་སྨད་གཉིས་སུ་གླེགས་བམ་སྤམ་མཐོ་དམའ་ལྟར་ཕྱེད་བགོས་ཞུས་པའོ།།` (an editor's remark on how the volumes were split) | `ལཾ།། །།` |

**Suggested fix:**
- **C11, C12, C13:** a colophon (translator or extra verses) that the source printed as a footnote. Possibly it is found only in some editions, but the note does not say which. Ask an editor whether it belongs to this edition:
  - If **yes**, move it into the text as a back-matter block (`^a-n`), and remove the marker and definition.
  - If **no** (only in some witnesses), turn it into a proper variant note: `[^n]: <last words> ༼<sigla>༽ <last words> <colophon>`.
  - Also fix `བའོོ` → `བའོ` in C13 (doubled vowel sign ོ).
- **C14:** an editorial remark about the whole file. Move it to frontmatter, and remove the marker and definition.

---

## Not in this report

Notes that *do* contain `༼…༽` but whose lemma still does not end at the marker are a separate, smaller set. They get the same fallback and warning. One example is `Ar_3CBf_.md` `[^12]`: an editorial note that mentions `༼ལ༽` as a volume number, not a witness. Another is in the segmented `Ch_3CCV` `[^18]`, whose lemma runs into the opening `༄༅༅། །` of the next text. They show up in the linter output as `lemma … does not end at the marker`. Ask for a report on those if you want one.
