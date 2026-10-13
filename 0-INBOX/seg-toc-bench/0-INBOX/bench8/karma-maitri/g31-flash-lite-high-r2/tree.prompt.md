=== SYSTEM PROMPT ===
# Verse-keyed / top-level headings (for commentaries without a usable sa bcad)

Use this prompt **instead of passes 1–4** when the commentary is declared as
`headings: verses` or `headings: top` — i.e. it explains the root text verse by verse
(or in a few large parts) and either has no sa bcad, or its sa bcad is not what the
vault's editors use as headings. The output is an anchored tree in the same format as
pass 5, ready for `toc_tree_ingest.py`.

You receive:
- the **mode** (`verses` or `top`),
- the commentary,
- (for `verses`) the root text, so you can tell which root stanza each passage explains.

## Mode `verses` — one heading per root stanza

The editors' convention for a *verse-by-verse* commentary on the Praise to the
Twenty-One Tārās (adapt the stanza names for another root text):

```
* 1. <the commentary's own name for the praise proper, else བསྟོད་པ་དངོས།>
   * 1.1 ཕྱག་འཚལ་བ།            ← only if the opening homage line (ཨོཾ་རྗེ་བཙུན་མ་…ཕྱག་འཚལ་ལོ།)
                                   is quoted and explained on its own
   * 1.n ཕྱག་འཚལ་དང་པོ།  …  ཕྱག་འཚལ་ཉེར་གཅིག་པ།   ← one node per homage stanza, in order
* 2. <the commentary's own name for the next part, else ཕན་ཡོན།>
* 3. …
```

Rules:
1. **Top level (`1.`, `2.`, …)** = the parts the body really has, in order: the praise
   proper; then whatever the commentary treats as a separate part after the 21 homages —
   the mantra/application (`འཇུག་གི་དོན།`), the benefits (`ཕན་ཡོན།`), a summary of the
   meaning (`གཞུང་གི་དོན་བསྡུ་བ།`). Use the commentary's own words for each title when it
   names the part; otherwise the default in brackets above. Do **not** make top-level
   nodes for the author's opening verses, the dedication or the colophon — those are
   frame sections added separately.

   **Fixed rules for what counts as a separate part** (do not decide case by case):
   - A wrap-up or overview that follows the last stanza (`དེ་ལྟར་ན་…`, correspondences,
     enumerations of what the praise contains) stays **inside** the praise proper, under
     the last stanza node, unless the commentary announces it with its own title
     (`… བསྡུ་བ་ནི།`, `… དོན་བསྡུས་པ།`).
   - The benefits section is **always** its own part, beginning where the commentary
     turns to the root text's benefit verses or to their lead-in (`འཇུག་གི་དོན་…`,
     `ཕན་ཡོན་…`). Its title: the commentary's own phrase if it has one, else `ཕན་ཡོན།`.
     The root mantra verse, when the commentary treats it together with the benefits,
     belongs to this part (no separate part for it).
   - The commentary's explanation of the root text's **own colophon** (who spoke the
     praise, which tantra it comes from) stays **inside** the benefits part; it is not a
     top-level part and not a frame node (the frame `མཛད་བྱང།` is the commentator's own
     colophon).
   So a verse-by-verse commentary on this root text normally has exactly two parts:
   `1.` the praise proper and `2.` the benefits — more only when the commentary itself
   names a further part.
2. **Stanza nodes** use the fixed editorial titles `ཕྱག་འཚལ་<ordinal>།`:
   དང་པོ། གཉིས་པ། གསུམ་པ། བཞི་པ། ལྔ་པ། དྲུག་པ། བདུན་པ། བརྒྱད་པ། དགུ་པ། བཅུ་པ།
   བཅུ་གཅིག་པ། བཅུ་གཉིས་པ། བཅུ་གསུམ་པ། བཅུ་བཞི་པ། བཅོ་ལྔ་པ། བཅུ་དྲུག་པ། བཅུ་བདུན་པ།
   བཅོ་བརྒྱད་པ། བཅུ་དགུ་པ། ཉི་ཤུ་པ། ཉེར་གཅིག་པ། — not the commentary's own wording.
   The ordinal is the stanza's place among the 21 homage stanzas of the root text, never
   the node number: when `1.1` is `ཕྱག་འཚལ་བ།`, node `1.n` is stanza n−1 (`1.15` =
   `ཕྱག་འཚལ་བཅུ་བཞི་པ།`). Each ordinal is used exactly once, in the sequence above —
   check the finished list before writing it.
3. **Children of a stanza** only when the commentary itself splits its treatment of the
   stanza into named parts:
   - a recurring split used for every stanza, e.g. a word commentary followed by a
     visualisation (`ཚིག་འགྲེལ།` / `གསལ་འདེབས་ཚུལ།`) → give every stanza those two
     children (`1.n.1`, `1.n.2`), titled with the commentary's own label;
   - a one-off division of one stanza (`… ལ་བཞི། ཡི་གེའི་དོན། སྤྱིའི་དོན། སྦས་དོན། མཐར་ཐུག`)
     → children for that stanza only, titled as the commentary names them.
   A part after the stanzas (e.g. the mantra) may likewise get children if it is divided.
   Otherwise no children: do not invent sub-headings from the content.
4. **Node `1.` begins where the first stanza's treatment begins** (same anchor as `1.1`),
   not at preliminary remarks before it (the class of the tantra, the source of the text,
   an overview). Those preliminaries belong to the frame (`II.`, added by pass 5), never
   to the praise proper.
5. A stanza node begins where the treatment of that stanza begins: its ordinal lead-in
   if there is one (`ཚིགས་བཅད་གཉིས་པ་…`, `གཉིས་པ་ནི།`), else the first quoted words of
   the stanza, else the first words explaining it. Its first child begins at the same
   place unless the child has its own lead-in. A lead-in names the child (`ཚིག་འགྲེལ་ནི།`,
   `གསལ་འདེབས་ཚུལ་ནི།`); `ཞེས་པ་ལ།` / `ཞེས་པ་ནི།` after the quoted stanza is **not** one —
   it points back to the quote, so the quote belongs to the child that explains it: a
   stanza opening with its quote has its first child (e.g. `ཚིག་འགྲེལ།`) anchored on that
   same quote, never on `ཞེས་པ་ལ།`.

## Mode `top` — top-level parts that follow the root text's own sections

The body's top-level parts are **the root text's own sections**, in the root's order. For
the Praise to the Twenty-One Tārās the root text has three: the praise proper (from the
opening homage line `ཨོཾ་རྗེ་བཙུན་མ་…` through the root-mantra verse
`རྩ་བའི་སྔགས་ཀྱིས་བསྟོད་པ་འདི་དང་། …`), the benefits (from `ལྷ་མོ་ལ་གུས་ཡང་དག་ལྡན་པའི། །`),
and the root's own colophon (`… རྣམ་པར་སྣང་མཛད་ཀྱིས་གསུངས་པ…`). Look at the root text you
are given and use its sections. So:

```
* 1. བསྟོད་པ་དངོས།
* 2. <the commentary's own name for the benefits part, else ཕན་ཡོན།>
* 3. མཛད་བྱང།          ← only if the commentary explains the root's own colophon
```

Rules (fixed — do not decide case by case):
1. **Titles.** Part 1 is always `བསྟོད་པ་དངོས།`, whatever the commentary calls it. Part 2
   takes the commentary's own short name when it announces the part (drop the leading
   ordinal and a trailing `གྱི་དོན་ནི།` / `ཀྱི་དོན་ནི།` / `ནི།`, e.g. `གསུམ་པ་མཇུག་ཕན་ཡོན་གྱི་དོན་ནི།`
   → `མཇུག་ཕན་ཡོན།`), else `ཕན་ཡོན།`. Part 3 is always `མཛད་བྱང།`.
2. **Where each part begins.** If the commentary opens the part with its own announcement
   (`གཉིས་པ་ … ནི།`, `གསུམ་པ་ … ནི།`), the part begins there. Otherwise it begins where the
   commentary starts treating that root section:
   - part 1 at the commentary's treatment of the root's **opening homage line**
     (`ཨོཾ་རྗེ་བཙུན་མ་…`) if it quotes or explains it, else at the first stanza;
   - part 2 at the first **benefit** verse (`ལྷ་མོ་ལ་གུས་…`) — the root-mantra verse and its
     explanation stay in part 1;
   - part 3 where the commentary explains who spoke the praise / where it comes from.
3. **No descent.** Parts 1–3 get no children, even when the commentary divides them.
4. **Front matter `II.`** Anything between the homage/opening verses and part 1 is front
   matter, never a numbered part:
   - a passage that only **lists** the outline of the praise (`བསྟོད་པ་འདི་ལ་དོན་གཉིས་ཏེ། …`)
     is `* II. བསྟོད་པའི་ས་བཅད།` with **no children** — titles that are merely listed are
     never nodes;
   - a **preliminary practice** the commentary treats before the praise (the accumulation
     of merit with its seven limbs, an invitation of the field of merit …) is `* II. <its
     name>`, and keeps its own announced divisions as `II.1`, `II.2`, `II.2.1` …; it begins
     at the sentence that announces the commentary's top-level division
     (`… སྦྱོར་དངོས་མཇུག་གསུམ་ … དང་པོ་ …`), and `II.1` at the same place.

## Anchors

Append `[[context]]` to every line exactly as in pass 5: the first 12–20 syllables at
the node's beginning, copied **character for character** (same tshegs, shads and
spaces), long enough to be unique in order. A node with children begins at its own
announcement; never anchor on a place where the title is only listed in an enumeration.

## Output

```
## དཀར་ཆག / Table of Contents

* 1. <title> [[<context>]]
   * 1.1 <title> [[<context>]]
…
```

Three spaces of indentation per level. Output only numbered nodes (and `II.` lines in
`top` mode) — the `I.` homage section and the closing `a.` / `b.` sections are added by
the frame pass. Write the whole tree to the output path you are given.

=== USER PROMPT ===
Mode: verses

The root text:

---
title: "སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།"
alt_titles:
  - en: "Praise of the Twenty-One Taras"
author: "སངས་རྒྱས་བཅོམ་ལྡན་འདས (རྣམ་པར་སྣང་མཛད)"
author_in_english: "The Buddha, the Blessed One (spoken through Vairocana)"
date: unknown — canonical Kangyur text
language: Tibetan
script: Unicode Tibetan
file_type: root-text
edition_type: critical
lang_tag: bo
chapters: 1
total_verses: 29
verse_id_format: chapter-verse
source_description: "Critical edition, adopted 2026-08-07 from the sibling Liturgy vault (`Liturgy-rails/1-SOURCES/Text/སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ.md`, BDRC WA0XLF0FAD365454A). This replaced the vault's original raw OCR/transcription export (OpenPecha MDAFBF633, from 0-INBOX/raw-data/སྒྲོལ་མ་ཉེར་གཅིག/…Segmentation - corrected.txt), which was retained at 0-INBOX/root-text-backup-pre-resegmentation-2026-08-07.md. Two reasons for the switch: (1) the OCR transcription's verse segmentation was wrong — homages were split across two or three block IDs each, with inconsistent boundaries, instead of one block per four-line homage; (2) it stopped mid-clause at the end of the twenty-first homage, omitting the entire ཕན་ཡོན (benefits) section that every commentary in this vault comments on. The critical edition supplies both. The two witnesses differ in reading at 17 of the 21 homages; most are orthographic (ཏུཏྟཱ་ར / ཏུ་ཏྟྭ་ར, ཧཱུཾ / ཧཱུྃ), but several are word-level (homage 3 གསེར་སྔོ vs སེར་སྔོ; homage 12 ཟླ་བའི་རྩེ་མོས vs ཟླ་བའི་དུམ་བུས; homage 16 སྒྲོན་མ vs སྒྲོལ་མ and ངག vs སྔགས), and several of the superseded readings were apparent OCR corruptions (སྤྱོལ་ཡུལ for སྤྱོད་ཡུལ, གྲགས་པོའི for དྲག་པོའི, རྣམས་པར for རྣམ་པར)."
other_ids: "Toh 438 (Tōhoku catalogue) — from the corpus catalog, not verified against a BDRC/Wikisource record"
bdrc_work_id: WA0XLF0FAD365454A
book_id: MDAFBF633
openpecha_id: MDAFBF633
superseded_transcription: 0-INBOX/root-text-backup-pre-resegmentation-2026-08-07.md
status: ingested
source: https://webuddhist.com
license: public
category_id: LCorCb2K98p3TICt3UCDm
text_id: HyUbHGlzS9LsSrgiFQNYE
edition_id: lEmYv8BrRQkOMPY9ymQpS
toc_id: JIiakpj3bZKHd0JzYZDQI
---

# ༄༅། །སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ། ^0

## མཚན་དོན་དང་འགྱུར་ཕྱག ^I-0

༄༅༅། །རྒྱ་གར་སྐད་དུ། ན་མཿཏཱ་རཱ་ཨེ་ཀ་བིཾ་ཤ་ཏི་སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ་སཱ་ཀ ། ^I-1

བོད་སྐད་དུ། སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ་ཕན་ཡོན་དང་བཅས་པ། ^I-2

ཨོཾ། རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ལོ། ། ^I-3

## བསྟོད་པ་དངོས། ^1-0

ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། །
སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །
འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །
གེ་སར་ཕྱེ་བ་ལས་ནི་བྱུང་མ། ། ^1-1

ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་དུ། །
གང་བ་བརྒྱ་ནི་བརྩེགས་པའི་ཞལ་མ། །
སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས། །
རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མ། ། ^1-2

ཕྱག་འཚལ་གསེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །
པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །
སྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་ཞི་བ། །
བཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ། ། ^1-3

ཕྱག་འཚལ་དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར། །
མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད་མ། །
མ་ལུས་ཕ་རོལ་ཕྱིན་པ་ཐོབ་པའི། །
རྒྱལ་བའི་སྲས་ཀྱིས་ཤིན་ཏུ་བསྟེན་མ། ། ^1-4

ཕྱག་འཚལ་ཏུཏྟྭ་ར་ཧཱུྃ་ཡི་གེ། །
འདོད་དང་ཕྱོགས་དང་ནམ་མཁའ་གང་མ། །
འཇིག་རྟེན་བདུན་པོ་ཞབས་ཀྱིས་མནན་ཏེ། །
ལུས་པ་མེད་པར་འགུགས་པར་ནུས་མ། ། ^1-5

ཕྱག་འཚལ་བརྒྱ་བྱིན་མེ་ལྷ་ཚངས་པ། །
རླུང་ལྷ་སྣ་ཚོགས་དབང་ཕྱུག་མཆོད་མ། །
འབྱུང་པོ་རོ་ལངས་དྲི་ཟ་རྣམས་དང་། །
གནོད་སྦྱིན་ཚོགས་ཀྱིས་མདུན་ནས་བསྟོད་མ། ། ^1-6

ཕྱག་འཚལ་ཏྲད་ཅེས་བྱ་དང་ཕཊ་ཀྱིས། །
ཕ་རོལ་འཁྲུལ་འཁོར་རབ་ཏུ་འཇོམས་མ། །
གཡས་བསྐུམ་གཡོན་བརྐྱང་ཞབས་ཀྱིས་མནན་ཏེ། །
མེ་འབར་འཁྲུགས་པ་ཤིན་ཏུ་འབར་མ། ། ^1-7

ཕྱག་འཚལ་ཏུ་རེ་འཇིགས་པ་ཆེན་མོ། །
བདུད་ཀྱི་དཔའ་བོ་རྣམ་པར་འཇོམས་མ། །
ཆུ་སྐྱེས་ཞལ་ནི་ཁྲོ་གཉེར་ལྡན་མཛད། །
དགྲ་བོ་ཐམས་ཅད་མ་ལུས་གསོད་མ། ། ^1-8

ཕྱག་འཚལ་དཀོན་མཆོག་གསུམ་མཚོན་ཕྱག་རྒྱའི། །
སོར་མོས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་མ། །
མ་ལུས་ཕྱོགས་ཀྱི་འཁོར་ལོས་བརྒྱན་པའི། །
རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་འཁྲུག་མ། ། ^1-9

ཕྱག་འཚལ་རབ་ཏུ་དགའ་བ་བརྗིད་པའི། །
དབུ་རྒྱན་འོད་ཀྱི་ཕྲེང་བ་སྤེལ་མ། །
བཞད་པ་རབ་བཞད་ཏུ་ཏྟྭ་ར་ཡིས། །
བདུད་དང་འཇིག་རྟེན་དབང་དུ་མཛད་མ། ། ^1-10

ཕྱག་འཚལ་ས་གཞི་སྐྱོང་བའི་ཚོགས་རྣམས། །
ཐམས་ཅད་འགུགས་པར་ནུས་མ་ཉིད་མ། །
ཁྲོ་གཉེར་གཡོ་བའི་ཡི་གེ་ཧཱུཾ་གིས། །
ཕོངས་པ་ཐམས་ཅད་རྣམ་པར་སྒྲོལ་མ། ། ^1-11

ཕྱག་འཚལ་ཟླ་བའི་རྩེ་མོས་དབུ་བརྒྱན། །
བརྒྱན་པ་ཐམས་ཅད་ཤིན་ཏུ་འབར་མ། །
རལ་པའི་ཁྲོད་ན་འོད་དཔག་མེད་ལས། །
རྟག་པར་ཤིན་ཏུ་འོད་ནི་མཛད་མ། ། ^1-12

ཕྱག་འཚལ་བསྐལ་པ་ཐ་མའི་མེ་ལྟར། །
འབར་བའི་ཕྲེང་བའི་དབུས་ན་གནས་མ། །
གཡས་བརྐྱང་གཡོན་བསྐུམ་ཀུན་ནས་བསྐོར་དགས། །
དགྲ་ཡི་དཔུང་ནི་རྣམ་པར་འཇོམས་མ། ། ^1-13

ཕྱག་འཚལ་ས་གཞིའི་ངོས་ལ་ཕྱག་གི། །
མཐིལ་གྱིས་བསྣུན་ཅིང་ཞབས་ཀྱིས་བརྡུང་མ། །
ཁྲོ་གཉེར་ཅན་མཛད་ཡི་གེ་ཧཱུྃ་གིས། །
རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས་མ། ། ^1-14

ཕྱག་འཚལ་བདེ་མ་དགེ་མ་ཞི་མ། །
མྱ་ངན་འདས་ཞི་སྤྱོད་ཡུལ་ཉིད་མ། །
སྭཱ་ཧཱ་ཨོཾ་དང་ཡང་དག་ལྡན་པས། །
སྡིག་པ་ཆེན་པོ་འཇོམས་པ་ཉིད་མ། ། ^1-15

ཕྱག་འཚལ་ཀུན་ནས་བསྐོར་རབ་དགའ་བའི། །
དགྲ་ཡི་ལུས་ནི་རབ་ཏུ་འགེམས་མ། །
ཡི་གེ་བཅུ་པའི་ངག་ནི་བཀོད་པའི། །
རིག་པ་ཧཱུྃ་ལས་སྒྲོན་མ་ཉིད་མ། ། ^1-16

ཕྱག་འཚལ་ཏུ་རེའི་ཞབས་ནི་བརྡབས་པས། །
ཧཱུྃ་གི་རྣམ་པའི་ས་བོན་ཉིད་མ། །
རི་རབ་མན་དཱ་ར་དང་འབིགས་བྱེད། །
འཇིག་རྟེན་གསུམ་རྣམས་གཡོ་བ་ཉིད་མ། ། ^1-17

ཕྱག་འཚལ་ལྷ་ཡི་མཚོ་ཡི་རྣམ་པའི། །
རི་དགས་རྟགས་ཅན་ཕྱག་ན་བསྣམས་མ། །
ཏཱ་ར་གཉིས་བརྗོད་ཕཊ་ཀྱི་ཡི་གེས། །
དུག་རྣམས་མ་ལུས་པར་ནི་སེལ་མ། ། ^1-18

ཕྱག་འཚལ་ལྷ་ཡི་ཚོགས་རྣམས་རྒྱལ་པོ། །
ལྷ་དང་མིའམ་ཅི་ཡིས་བསྟེན་མ། །
ཀུན་ནས་གོ་ཆ་དགའ་བའི་བརྗིད་ཀྱིས། །
རྩོད་དང་རྨི་ལམ་ངན་པ་སེལ་མ། ། ^1-19

ཕྱག་འཚལ་ཉི་མ་ཟླ་བ་རྒྱས་པའི། །
སྤྱན་གཉིས་པོ་ལ་འོད་རབ་གསལ་མ། །
ཧ་ར་གཉིས་བརྗོད་ཏུ་ཏྟྭ་ར་ཡིས། །
ཤིན་ཏུ་དྲག་པོའི་རིམས་ནི་སེལ་མ། ། ^1-20

ཕྱག་འཚལ་དེ་ཉིད་གསུམ་རྣམས་བཀོད་པའི། །
ཞི་བའི་མཐུ་དང་ཡང་དག་ལྡན་མ། །
གདོན་དང་རོ་ལངས་གནོད་སྦྱིན་ཚོགས་རྣམས། །
འཇོམས་པ་ཏུ་རེ་རབ་མཆོག་ཉིད་མ། ། ^1-21

རྩ་བའི་སྔགས་ཀྱིས་བསྟོད་པ་འདི་དང་། །
ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག ། ^1-22

## བསྟོད་པའི་ཕན་ཡོན། ^2-0

ལྷ་མོ་ལ་གུས་ཡང་དག་ལྡན་པའི། །
བློ་ལྡན་གང་གིས་རབ་ཏུ་བརྗོད་པས། ། ^2-1

སྲོད་དང་ཐོ་རངས་ལངས་པར་བྱས་ནས། །
དྲན་པས་མི་འཇིགས་ཐམས་ཅད་རབ་སྟེར། །
སྡིག་པ་ཐམས་ཅད་རབ་ཏུ་ཞི་བ། །
ངན་འགྲོ་ཐམས་ཅད་འཇོམས་པ་ཉིད་དོ། ། ^2-2

རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས། །
མྱུར་དུ་དབང་ནི་བསྐུར་བར་འགྱུར་ལ། །
འདི་ལས་ཆེ་བ་ཉིད་ནི་འཐོབ་ཅིང་། །
སངས་རྒྱས་གོ་འཕང་མཐར་ཐུག་དེར་འགྲོ། ། ^2-3

དེ་ཡི་དུག་ནི་དྲག་པོ་ཆེན་པོ། །
བརྟན་གནས་པའམ་གཞན་ཡང་འགྲོ་བ། །
ཟོས་པ་དང་ནི་འཐུངས་པ་ཉིད་ཀྱང་། །
དྲན་པས་རབ་ཏུ་སེལ་བ་ཉིད་ཐོབ། ། ^2-4

གདོན་དང་རིམས་དང་དུག་གིས་གཟིར་བའི། །
སྡུག་བསྔལ་ཚོགས་ནི་རྣམ་པར་སྤོང་སྟེ། །
སེམས་ཅན་གཞན་པ་རྣམས་ལ་ཡང་ངོ་། ། ^2-5

གཉིས་གསུམ་བདུན་དུ་མངོན་པར་བརྗོད་ན། །
བུ་འདོད་པས་ནི་བུ་ཐོབ་འགྱུར་ཞིང་། །
ནོར་འདོད་པས་ནི་ནོར་རྣམས་ཉིད་ཐོབ། །
འདོད་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་ཏེ། །
བགེགས་རྣམས་མེད་ཅིང་སོ་སོར་འཇོམས་འགྱུར་ཅིག ། ^2-6

## མཛད་བྱང། ^a-0

བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མ་ལ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས་བསྟོད་པ་གསུངས་པ་རྫོགས་སོ།། །། ^a-1

The commentary:

---
title: ཀརྨ་མཻ་ཏྲིའི་སྒྲོལ་བསྟོད་ཟིན་བྲིས།
alt_titles:
  - bo: "ཀརྨ་མཻ་ཏྲིའི་སྒྲོལ་བསྟོད་ཟིན་བྲིས་བཞུགས་སོ།"
  - en: "Notes on Karma Maitri's Praise to Tārā"
author: ཀརྨ་མཻ་ཏྲི་
author_in_english: Karma Maitri
date: unknown
language: Tibetan
script: Unicode Tibetan
file_type: commentary
lang_tag: bo
verse_id_format: chapter-verse
registered_id: karma-maitri
root_text: 1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md
covers_verses: 1-1–2-6
source_description: "Resegmented version (chapter-verse addressing keyed to root-verse numbers, with root-text transclusions added) of the commentary already registered as karma-maitri (TARAC11_KMT; see 1-SOURCES/Commentaries/ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་བསྟོད་པའི་བསྡུས་འགྲེལ།.md, BDRC WA0XL10E024BE73B5). Opening line ('ན་མོ་གུ་རུ་ཨཱརྻ་ཏཱ་ར་ཡཻ') and first paragraph are word-for-word identical to that file, confirming same underlying work; colophon here ('ཀརྨ་མཻ་ཏྲིའི་མིང་གིས་མཁས་གྲུབ་ཀྱིས་གསུངས་པ་དག་ལས་ཟིན་ཐོར་བྲིས་པ') matches that file's own catalogued colophon note. NOTE: this file's transclusions cite root-text block IDs #^1-22 and #^2-1 through #^2-6 for the closing material, which predate the vault's 2026-08-07 root-text resegmentation (current scheme: homages ^1-1–^1-21, benefits ^a-0–^a-7) — these links should be re-checked/re-pointed before this file is promoted out of New raw data."
bdrc_work_id: WA0XL10E024BE73B5
source: https://webuddhist.com
license: public
category_id: LCorCb2K98p3TICt3UCDm
text_id: IZpPQackQMjMsG6i9laM3
edition_id: EPWPiXyjSDcgewleXnbIj
toc_id: jUgourpgWtZRVAfdftIz0
commentary_of: HyUbHGlzS9LsSrgiFQNYE
---

༄༅། །ཀརྨ་མཻ་ཏྲིའི་སྒྲོལ་བསྟོད་ཟིན་བྲིས་བཞུགས་སོ། །

ན་མོ་གུ་རུ་ཨཱརྻ་ཏཱ་ར་ཡཻ།

ཕྱག་འཚལ་ཉེར་གཅིག་ལ་བསྟོད་པ་དངོས་དང་། ཕན་ཡོན་ནོ། །

དང་པོ་ལ་ཉེར་གཅིག་ཡོད་པ་ལས། དང་པོ་ནི། ཕྱག་འཚལ། གང་ལ་ན། སྒྲོལ་མ་ལའོ། །

དེ་ལ་ཡོན་ཏན་ནམ་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན། སེམས་ཅན་སྐད་ཅིག་གིས་སྒྲོལ་བས་ན་མྱུར་མ། ཉོན་མོངས་བདུད་སྡེ་འཇོམས་པས་ན་དཔའ་མོ། སྤྱན་གྱི་འོད་ནི་སྐད་ཅིག་གིས་གློག་འཁྱུག་པ་དང་འདྲ་བས་སྒྲོལ་མ་དེ་ནི་ས་འོག་ས་སྟེང་ས་བླའི་འཇིག་རྟེན་གསུམ་གྱི་མགོན་པོ་སྤྱན་རས་གཟིགས་ཀྱི་ཆུ་སྐྱེས་ལས་སྐྱེས་པའི་ཞལ་གྱི་མེ་ཏོག་པདྨའི་གེ་སར་བྱེ་བ་ལས་ནི་ཉེ་བར་བྱུང་སྒྲོལ་མ་ལའོ། །

གཉིས་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། སྟོན་ཀའི་ཟླ་བ་ཉ་ཀུན་ཏུ་གང་བ་བརྒྱ་ཐམ་པ་ནི་རྣམས་པ་བརྩེགས་པ་ལྟར་དཀར་ཞིང་མཛེས་པའི་ཞལ་དང་ལྡན་མ། སྐར་མའི་ཚོགས་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས་འགྲན་དུ་མེད་ཅིང་རབ་ཏུ་ཕྱེ་བའི་འོད་དཀར་པོ་རབ་ཏུ་འབར་བའི་སྒྲོལ་མ་ལའོ། །

གསུམ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། གསེར་ལྟར་མཛེས་ཤིང་ཅུང་ཟད་སྔོ་བའི་མདོག་ཅན་ཆུ་ནི་སྐྱེ་ཕྱིར་པདྨ་རབ་ཏུ་བཀྲ་བས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་པའི་སྒྲོལ་མ། དེ་ཡང་སྦྱིན་པ་དང་། བརྩོན་འགྲུས་དང་། དཀའ་ཐུབ་སྟེ་ཚུལ་ཁྲིམས་དེས་ཉོན་མོངས་པ་ཞི་བར་བྱེད་པ། བཟོད་པ་དང་། བསམ་གཏན་དང་། །

བཞི་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར་ལྟར་མཆོད་པའི་གནས་སུ་གྱུར་ཅིང་། བདུད་སོགས་ཕས་རྒོལ་མཐའ་ཡས་པ་ལས་རྣམ་པར་རྒྱལ་བ་སྤྱོད་པའི་སྒྲོལ་མ། ཕར་ཕྱིན་བཅུ་དང་ས་བཅུ་མ་ལུས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་གོ་འཕང་ཐོབ་པའི་བདག་ཉིད་དེ་ལ་རྒྱལ་བའི་སྲས་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་ཐམས་ཅད་ཀྱི་ཡུམ་དུ་གྱུར་པས་གུས་པ་ཆེན་པོའི་ཤིན་ཏུ་བརྟེན་པས་སྒྲོལ་མ་ལའོ། །

ལྔ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཏུཏྟཱ་རེ་ཧཱུཾ་ཞེས་པའི་ཡི་གེས་འདོད་ཁམས་དང་། ཕྱོགས་ཏེ་གཟུགས་ཁམས་དང་། ནམ་མཁའ་སྟེ་གཟུགས་མེད་པའི་ཁམས་གང་བར་མཛད་མ་འགྲོ་བ་རྒྱུད་ལྔ་ཁམས་གོང་མ་གཉིས་ཏེ་འཇིག་རྟེན་བདུན་པོ་ཞབས་ཀྱིས་མནན་ཏེ། རིག་སྔགས་ཀྱི་མཐུས་ལུས་པ་མེད་པར་དབང་དུ་འགུགས་པར་ནུས་པའམ་མཛད་པའི་སྒྲོལ་མ་ལའོ། །

དྲུག་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། བརྒྱ་བྱིན་དང་། མེ་ལྷ་དང་། ཚངས་པ་དང་། རླུང་ལྷ་དང་། སྣ་ཚོགས་དབང་ཕྱུག་སྟེ་དབང་ཕྱུག་ཆེན་པོ་དག་གིས་མཆོད་མ། ཚོགས་བདག་འབྱུང་པོ། དུར་ཁྲོད་ན་གནས་པའི་རོ་ལངས། ཟུར་ཕུད་ལྔ་སོགས་དྲི་ཟ་རྣམས་དང་། སྨུག་འཛིན་སོགས་གནོད་སྦྱིན་གྱི་ཚོགས་ཀྱིས་གང་གི་མདུན་ནས་རྟག་པར་བསྟོད་པའི་སྒྲོལ་མ་ལའོ། །

བདུན་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཞལ་ནས་ཏྲད་ཅེས་བྱ་བ་དང་། ཕཊ་ཅེས་བྱ་བ་ལ་སོགས་པའི་དྲག་པོའི་སྒྲ་ཡིས་ཕ་རོལ་པོས་གནོད་པའི་འཁྲུལ་འཁོར་རབ་ཏུ་འཇོམས་པར་མཛད་མ། གཡས་བསྐུམ་ཞིང་གཡོན་བརྐྱང་བའི་ཞབས་ཀྱིས་འཇིག་རྟེན་བདུན་པོ་མནན་ཏེ། མེ་དཔུང་འབར་ཞིང་འཁྲུགས་པ་ཤིན་ཏུ་འབར་བའི་དབུས་ན་བཞུགས་པའི་སྒྲོལ་མ་ལའོ། །

བརྒྱད་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཏུ་རེ་ལ་སོགས་པའི་གསུང་གི་འཇིགས་པ་ཆེན་པོ་བརྒྱད་ལས་སྐྱོབ་ཅིང་། ལྷའི་བུ་སོགས་བདུད་ཀྱི་དཔའ་བོ་བཞི་རྣམ་པར་འཇོམས་མ། ཆུ་ལས་སྐྱེས་པའི་མེ་ཏོག་མཛེས་པའི་ཞལ་ནས་ཁྲོ་གཉེར་དང་ལྡན་པར་མཛད་ཅིང་། ཉོན་མོངས་ལ་སོགས་པའི་དགྲ་བོ་ཐམས་ཅད་གཅིག་ཀྱང་མ་ལུས་པ་གསོད་པར་བྱེད་པའི་སྒྲོལ་མ་ལའོ། །

དགུ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཕྱག་གཡོན་མཛུབ་གུང་མཐེའུ་ཆུང་གསུམ་དཀོན་མཆོག་གསུམ་མཚོན་པའི་སྐྱབས་སྦྱིན་གྱི་ཕྱག་རྒྱའི་སོར་མོ་ཤིན་ཏུ་མཛེས་པའི་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་པར་མཛད་མ། གཅིག་མ་ལུས་པའི་ཕྱོགས་ཀྱི་འོད་ཟེར་ཐམས་ཅད་ཕྱག་གཡས་མཆོག་སྦྱིན་ཕྱག་རྒྱའི་མཐིལ་དུ་འཁོར་ལོས་བརྒྱན་པའི་ཆ་ལས་འཕྲོས་པའི་རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་རབ་ཏུ་འཁྲུགས་པས་གང་ཞིང་འོད་གཞན་རྣམས་ཟིལ་གྱིས་གནོན་པར་མཛད་མ་ལའོ། །

བཅུ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། འགྲོ་བ་ཀུན་གྱི་རེ་བ་བསྐང་བའི་རབ་ཏུ་དགའ་བ་འབྱུང་བར་བགྱིད་པའི་རིན་པོ་ཆེའི་དབུ་རྒྱན་དང་། ནོར་བུའི་དོ་ཤལ་སོགས་འོད་ཟེར་གྱི་ཕྲེང་བ་འབར་ཞིང་འཁྲུགས་པ་སྤེལ་ལེགས་པའི་བརྒྱན་པའི་སྒྲོལ་མ་བཞད་པ་དང་རབ་ཏུ་བཞེད་པའི་སྔགས་ཏུཏྟཱ་ར་ལ་སོགས་པའི་སྒྲ་ཡིས། གཞན་འཕྲུལ་དབང་བྱེད་ཀྱི་བདག་པོ་བདུད་དང་། གཞན་ཡང་འཇིག་རྟེན་ཐམས་ཅད་དབང་དུ་བསྡུ་བར་བྱེད་པའི་སྒྲོལ་མ་ལའོ། །

བཅུ་གཅིག་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཕྱོགས་སྐྱོང་བཅུ་སོགས་ས་གཞི་སྐྱོང་བའི་ཚོགས་རྣམས་མ་ལུས་པ་ཐམས་ཅད་བྲན་དུ་འགུག་པར་ནུས་མ་ཉིད་ཀྱི་སྒྲོལ་མ། ཞལ་ཁྲོ་གཉེར་གཡོ་བའི་ཐུགས་ཀར་ཡི་གེ་ཧཱུྃ་གིས་མཚན་པའི་འོད་ཀྱིས་འཇིགས་ཤིང་ཕོངས་པར་གྱུར་པའི་འགྲོ་བ་ཐམས་ཅད་སྡུག་བསྔལ་ལས་རྣམ་པར་བསྒྲལ་ནས་བདེ་བ་དམ་པ་ལ་འགོད་པར་མཛད་པའི་སྒྲོལ་མ་ལའོ། །

བཅུ་གཉིས་པ་ནི། ཕྱག་འཚལ། གང་ལ་ནི། ཟླ་བའི་དུམ་བུ་སྟེ་ཕྱེད་པའི་དབུ་ལ་བརྒྱན་ཅིང་། བརྒྱན་པ་ཐམས་ཅད་ལས་ཀྱང་འོད་དཀར་པོ་ཤིན་ཏུ་འབར་བའི་བདག་ཉིད་མ།

རལ་པའི་ཁྲོད་ན་རིགས་བདག་འོད་དཔག་མེད་བཞུགས་པ་ལས།

སེམས་ཅན་གྱི་དོན་དུ་རྟག་པར་ཤིན་ཏུ་འཚེར་བའི་འོད་རབ་ཏུ་འགྱེད་པར་མཛད་པའི་སྒྲོལ་མ་ལའོ། །

བཅུ་གསུམ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། བསྐལ་པ་ཐ་མ་སྟེ་འཇིག་པའི་དུས་ཀྱི་མེ་ལྟར་རབ་ཏུ་འབར་བའི་ཕྲེང་བས་བསྐོར་བའི་དབུས་ན་གནས་མ། གཡས་བརྐྱང་གཡོན་བསྐུམ་པའི་སྟབས་ཀྱིས་འོད་ཀྱི་ཕྲེང་བས་བསྐོར་བའི་བདེ་བ་སྦྱིན་པའི་དགའ་བར་མཛད་ཅིང་། དགྲ་ཡི་དཔུང་ཐམས་ཅད་རྣམ་པར་འཇོམས་པར་མཛད་མ་ལའོ། །

བཅུ་བཞི་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ས་གཞི་ངོས་ལ་སྡིགས་མཛུབ་དང་བཅས་པའི་ཕྱག་གི་མཐིལ་གྱིས་བསྣུན་ཅིང་ཞབས་ཀྱིས་བརྡུང་བར་མཛད་མ། ཁྲོ་གཉེར་ཅན་དུ་མཛད་ཅིང་། གཡས་ཀྱི་ཕྱག་མཐིལ་ན་ཡི་གེ་ཧཱུྃ་གི་འོད་འཕྲོ་བས་ས་རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས་པར་མཛད་ཅིང་། སེམས་ཅན་ཀུན་གྱི་བར་གཅོད་སེལ་བའི་སྒྲོལ་མ་ལའོ། །

བཅོ་ལྔ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཟག་མེད་ཀྱི་རང་བཞིན་བདེ་མ། ཉོན་མོངས་སྤང་བའི་དགེ་མ། རྩུབ་རེག་བྲལ་བའི་ཞི་མ། མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་མཆོག་ཏུ་རབ་ཏུ་ཞི་བའི་སྤྱོད་ཡུལ་ཅན་ཉིད་དུ་འགྱུར་བའི་སྒྲོལ་མ། སྭཱ་ཧཱ་དང་ཨོཾ་ཞེས་པ་དང་ཡང་དག་པར་ལྡན་པའི་སྔགས་ཀྱིས་སྡིག་པ་དང་སྒྲིབ་པ་ཆེན་པོ་ཐམས་ཅད་འཇོམས་པར་ནུས་པ་ཉིད་ཀྱི་སྒྲོལ་མ་ལའོ། །

བཅུ་དྲུག་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཐུགས་ཀར་འཁོར་ལོའི་ལྟེ་བར་ཨོཾ་དང་རྩིབས་རྣམས་ལ་སྔགས་ཀྱི་ཡི་གེས་ཀུན་ནས་བསྐོར་བའི་རབ་ཏུ་དགའ་བར་མཛད་པའི་སྒྲོལ་འོད་ཀྱིས། དགྲ་ཡི་ལུས་ནི་རབ་ཏུ་འགེམས་པར་མཛད་མ། ཨོཾ་ཏཱ་རེ་ཏུཏྟཱ་རེ་ཏུ་རེ་སྭཱ་ཧཱ། ཞེས་པའི་ཡི་གེ་བཅུ་པོའི་ངག་ནི་འཁོར་ལོའི་རྣམ་པར་བཀོད་པའི་རིག་པ་ཧཱུཾ་ལས།

ༀ་ན་མཿ ཏཱ་རེ་ན་མོ་ཧཱ་རེ་ཧཱུྃ་ཧཱ་རེ་སྭཱ་ཧཱ་ཞེས་བདུད་སྡེ་འཇོམས་པའི་ཁྲོ་བོའི་ཚུལ་གྱིས་སྒྲོལ་མ་ཉིད་དུ་མཛད་མ་ལའོ། །

བཅུ་བདུན་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཏུ་རེ་ནི་མྱུར་མ་སྟེ་སྒྲོལ་མའི་ཞབས་ས་ལ་བརྡབས་པས། ཧཱུཾ་གི་རྣམ་པའི་ས་བོན་ཉིད་དང་ལྡན་མ། དེས་སྟོང་གསུམ་གྱི་ཕྱི་རོལ་ན་གནས་རི་རབ་མནྡ་ར་ཞེས་པ་དང་རི་རབ་འབིགས་བྱེད་ལ་སོགས་པ་སྟེ། མདོར་ན་འཇིག་རྟེན་སྲིད་པ་གསུམ་པོ་རྣམ་པར་གཡོ་བར་མཛད་པའི་བདག་ཉིད་མ་ལའོ། །

བཅོ་བརྒྱད་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། དྭངས་ཤིང་བསིལ་བ་སོགས་ཡོན་ཏན་ཁྱད་པར་ཅན་དང་ལྡན་པའི་ལྷ་ཡི་བདུད་རྩིའི་མཚོ་ཡི་རྣམ་པའི་བདག་ཉིད་ཅན་གྱི་རི་དྭགས་རྟགས་ཅན་ཏེ་ཟླ་བ་ཕྱག་ན་བསྣམས་མ། ཏཱ་ར་གཉིས་བརྗོད་པའི་མཐར་ཕཊ་ཀྱི་ཡི་གེས་སེམས་ཅན་གང་ཞིག་བརྟན་གཡོའི་དུག་རྣམས་མ་ལུས་པ་ནི་སེལ་བའི་སྒྲོལ་མ་ལའོ། །

བཅུ་དགུ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ལྷ་ཡི་ཚོགས་རྣམས་ཀྱི་རྒྱལ་པོ་ཚངས་པ་དང་། བརྒྱ་བྱིན་དང་། ལྷ་ཕལ་པ་དང་། མིའམ་ཅི་ཡི་ཚོགས་ཐམས་ཅད་ཀྱིས་ཞབས་ལ་བརྟེན་མ། ཀུན་ནས་ལྷ་ཡི་རྣམ་པ་དང་སྔགས་ཀྱི་གོ་ཆ་དགའ་བའི་སྟེ་གཟི་བརྗིད་ཀྱིས་རྩོད་པ་དང་རྨི་ལམ་ངན་པ་ཐམས་ཅད་སེལ་བའི་སྒྲོལ་མ་ལའོ། །

ཉི་ཤུ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཉི་མ་དང་ཟླ་བ་རབ་ཏུ་རྒྱས་པ་ལྟ་བུས་སྤྱན་གཉིས་པོ་ལས་འོད་རབ་ཏུ་གསལ་ཞིང་འབར་མ་ཧཱ་ར་གཉིས་བརྗོད་པའི་ཏུཏྟཱ་རེ་སྟེ་རིག་སྔགས་ཀྱི་ཡི་གེ་ཤིན་ཏུ་དྲག་པོས་རིམས་ནད་ཐམས་ཅད་སེལ་བར་མཛད་པའི་སྒྲོལ་མ་ལའོ། །

ཉེར་གཅིག་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། གནས་གསུམ་དེ་ཉིད་གསུམ་སྟེ་འབྲུ་གསུམ་གྱི་ཡི་གེ་རྣམས་བཀོད་པས་དེའི་འོད་ཀྱིས་ཉོན་མོངས་ཞི་བའི་མཐུ་དང་ཡང་དག་པར་ལྡན་མ། གདོན་དང་རོ་ལངས་དང་གནོད་སྦྱིན་གྱི་ཚོགས་དང་འཇིགས་པ་དང་གནོད་པ་རྣམས་འཇོམས་པ་ལ། ཏུ་རེ་རབ་མཆོག་སྟེ་ཡི་གེ་བཅུ་པའི་སྔགས་ཀྱིས་འཇོམས་པར་མཛད་པ་ཉིད་ཀྱི་སྒྲོལ་མ་ལའོ། །

རྩ་བའི་སྔགས་ཏེ་སྔར་བསྟན་པའི་ཞི་ཁྲོའི་སྔགས་ཀྱིས་བརྒྱན་པའི་བསྟོད་པ་འདི་དང་། ཕྱག་འཚལ་བ་ནི་གང་ལ་ན་རྣམ་འཕྲུལ་ཉི་ཤུ་རྩ་གཅིག་དང་ལྡན་པའི་སྒྲོལ་མ་ལའོ། །

གཉིས་པ་ཕན་ཡོན་ནི། ལྷ་མོ་སྒྲོལ་མ་ལ་གུས་པ་ཡང་དག་པ་དང་ལྡན་པའི་བློ་དང་ལྡན་པས་གང་ཟག་གིས་བསྟོད་པའི་རྒྱལ་པོ་འདི་སེམས་རབ་ཏུ་དང་བས་བརྗོད་དེ། སྲོད་ལ་དྲག་པོ་དང་ཐོ་རངས་ཞི་བ་སོགས་སྐུར་མོས་པས་ལངས་པར་བྱས་ནས། ཡིད་ལ་དྲན་པས་འཇིགས་པ་ལས་སྐྱོབ་ཅིང་མི་འཇིགས་པ་ཐམས་ཅད་རབ་ཏུ་གཏོར་རོ། །

དེར་མ་ཟད་ངན་འགྲོའི་རྒྱུ་སྡིག་པ་ཐམས་ཅད་རབ་ཏུ་ཞི་ཞིང་། འབྲས་བུ་ངན་འགྲོའི་སྡུག་བསྔལ་ཐམས་ཅད་འཇོམས་པ་ཉིད་དོ། །

རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས་ཀྱང་མྱུར་དུ་དབང་ནི་བསྐུར་བར་འགྱུར་ལ། ཚེ་འདི་ཉིད་ལ་བདེ་བ་ཆེ་བ་ཉིད་ནི་ཐོབ་ཅིང་། མཐར་ཐུག་ཏུ་ཡང་སངས་རྒྱས་ཀྱི་གོ་འཕང་ཡང་མཐར་ཐུག་པ་དེར་འགྲོ་བ་ཉིད་དོ། །

དེ་འཐོབ་པ་ལ་བར་དུ་གཅོད་པའི་དུག་ནི་དྲག་པོ་ཆེན་པོ་སྟེ་བདག་ཏུ་ལྟ་བ་དང་། རྐུན་པོ་དང་། ཤ་ཟ་ལ་སོགས་པ་བརྟེན་གནས་པ་སྟེ་རྟག་པར་གནོད་པའམ། གཞན་ཡང་འགྲོ་བ་སྦྲུལ་ལ་སོགས་པའི་དུག་ཀྱང་དྲན་པ་ཙམ་གྱིས་རབ་ཏུ་སེལ་བ་ཉིད་ཐོབ་ལ། གདོན་དང་རིམས་དང་དུག་གིས་གཟིར་བའི་སྡུག་བསྔལ་ཉེར་འཚེའི་ཚོགས་ནི་རྣམ་པར་སྤང་ཞིང་། སེམས་ཅན་རང་ལས་གཞན་པ་རྣམས་ལ་ཡང་ཕན་ཡོན་འདི་ལྟ་བུ་འབྱུང་ངོ་། ། ཉིན་མཚན་གཉིས་དང་ཉིན་མཚན་ལན་གསུམ་གསུམ་དུ་བསྟོད་པ་འདི་བདུན་བདུན་དུ་མངོན་པར་བརྗོད་ན། བུ་འདོད་པའི་ནི་བུ་ཐོབ་འགྱུར་ཞིང་། ནོར་འདོད་པའི་ནི་ནོར་རྣམས་ཉིད་ཐོབ་ཅིང་། མདོར་ན་ཡིད་ལ་ཇི་ལྟར་བསམ་པའི་འདོད་པ་ཐམས་ཅད་འགྲུབ་པར་འགྱུར་ཏེ། བགེགས་དང་བར་དུ་གཅོད་པ་ཐམས་ཅད་མེད་ཅིང་མི་འབྱུང་ལ། བྱུང་ཡང་སོ་སོར་རྗེ་བཙུན་མ་ཉིད་ཀྱི་མཐུས་འཇོམས་པར་འགྱུར་རོ། །

ཞེས་པའང་རང་གི་བརྗེད་ཐོ་ལྟ་བུར། ༸ཀརྨ་མཻ་ཏྲིའི་མིང་གིས་མཁས་གྲུབ་ཀྱིས་གསུངས་པ་དག་ལས་ཟིན་ཐོར་བྲིས་པ་ཤུ་བྷཾ།། ༎


Reply with the tree only, exactly in the output format of the instructions (the `## དཀར་ཆག / Table of Contents` header and the `* …` lines), nothing else.