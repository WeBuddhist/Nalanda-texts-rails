---
name: root-text-segmentation
description: >
  Lay out a Tibetan VERSE ROOT TEXT — a treatise, praise, ritual or prayer written in its
  own voice, not a commentary — the way the vault's processed root texts are laid out:
  one pāda per line, stanzas as blocks, front matter and colophons under fixed frame
  headings, the text's own announced parts (if any) as headings, block IDs. Works on
  run-on verse without verse numbers (the Nalanda Masters files in 1-SOURCES/Text/).
  Use for "segment this root text", "format this praise / sādhana / prayer", "split the
  verses into stanzas", "add frame headings and IDs to the root text". Commentaries go to
  commentary-segmentation instead.
profile: rails-vault
---

# root-text-segmentation

Turns a verse root text that arrives as one run of text into the layout of the vault's
processed root texts (the BCA and Tārā root files, the Liturgy-rails chants): `# title ^0`;
`## ཀླད་ཀྱི་དོན། ^I-0` over the Sanskrit title, Tibetan title and homage; body headings only
where the text announces its own parts; one stanza per block with one pāda per line;
`## མཛད་བྱང། ^a-0` / `## འགྱུར་བྱང། ^b-0` over the colophons; derived block IDs. Nothing is
forced: a frame heading appears only when its element is in the text, and a text that
announces no parts gets no body headings (only `གཞུང་དངོས།` to separate it from the front
matter). The text itself is never changed — every step checks it.

It exists because the commentary skills assume a commentary (a root text to match, lemma
and gloss, sa bcad) and `format-tibetan-root-text` assumes verse numbers and chapter
colophons; neither fits a run-on verse root text.

---

## Inputs

| Input | Description |
|---|---|
| `source` | the root text, normally `1-SOURCES/Text/<id>.md` — first line the title, then the text as running prose, footnote apparatus `[^n]: …` at the end (kept as is) |
| `id` | short id for the working folder (usually the file stem) |
| `tree` *(optional)* | an anchored tree from `toc-tree-extraction` mode `root`, when the text announces its parts |
| grouping *(optional)* | `auto` (default): two versions for a text translated from Sanskrit, one otherwise — see Rules 5–6; `sloka` or `free` forces a single version |

If the source is a commentary, a prose text, or the `id` is unclear, stop and ask.

## Output

| File | What |
|---|---|
| `0-INBOX/<id>-root/prepared.md` | pādas one per block, frame and body headings inserted |
| `0-INBOX/<id>-root/group-in.md` | numbered pāda list for the grouping prompt |
| `0-INBOX/<id>-root/groups-sloka.json` | śloka groups, written by the script (translated texts only) |
| `0-INBOX/<id>-root/groups-free.json` | groups by sense, written by the prompt |
| `0-INBOX/<id>-root/final-sloka.md` | **version 1** (translated texts only): 4 pādas per block |
| `0-INBOX/<id>-root/final-free.md` | **version 2** (every text): blocks by sense |

Both versions carry the same headings, frame and text; only the stanza blocks differ. The
`1-SOURCES/` file is replaced by the chosen version only after a human approves it.

---

## Output file format

```markdown
# ༄༅། །<title> ^0

## ཀླད་ཀྱི་དོན། ^I-0

༄༅༅། །རྒྱ་གར་སྐད་དུ། <Sanskrit title> ^I-1

བོད་སྐད་དུ། <Tibetan title> ^I-2

<homage> ཕྱག་འཚལ་ལོ། ། ^I-3

## <first part, or གཞུང་དངོས།> ^1-0

<pāda> །
<pāda> །
<pāda> །
<pāda> ། ^1-1

## <next part> ^2-0
…

## མཛད་བྱང། ^a-0

<… མཛད་པ་རྫོགས་སོ།> ^a-1

## འགྱུར་བྱང། ^b-0

<… ལོ་ཙཱ་བ … བསྒྱུར་ … གཏན་ལ་ཕབ་པའོ།> ^b-1

[^1]: <footnotes exactly as in the source>
```

---

## Rules

1. **No character changes.** Only line breaks, block breaks, headings and IDs are added;
   the script asserts that the text (headings aside) is unchanged and footnotes stay as they
   are, markers included (`…ཀྱིས༌[^1]མཆོད…`).
2. **Pādas** end at a shad (`།`) or tsheg-shad (`༔`) cluster before the next syllable; a
   footnote marker stays on the line it follows. (`༔` matters: terma texts cannot be split
   without it — line F1 0.00 → 1.00.)
3. **Frame headings by pattern only**, and only when the element is present:
   `རྒྱ་གར་སྐད་དུ། … བོད་སྐད་དུ། … ཕྱག་འཚལ་ལོ།` → `ཀླད་ཀྱི་དོན། ^I-0` (title override:
   `--front-title མཚན་དོན་དང་འགྱུར་ཕྱག`); a colophon starts at its own wording — author
   (`…མཛད་པ་རྫོགས་སོ།`) → `མཛད་བྱང། ^a-0`, translators (`…ལོ་ཙཱ་བ… བསྒྱུར…`) →
   `འགྱུར་བྱང། ^b-0`. Closing verses in another metre stay in the body.
4. **Body headings only where the text announces parts** (`toc-tree-extraction` mode
   `root`), and **only its top-level parts**: sub-parts in a verse text are often shorter
   than a stanza and would split stanzas or stand empty. No candidates → no tree → no body
   headings. The author's own opening verses belong to the body (the first body heading is
   moved up to meet them).
5. **Two versions for a translated text, one otherwise.** A text with `རྒྱ་གར་སྐད་དུ།`
   (translated from Sanskrit) gets **both** `final-sloka.md` and `final-free.md`; a text
   without it gets only `final-free.md` — no śloka version.
   **Version `sloka`:** four pādas per block, counted from the start of each part; a part's remainder
   is a shorter last block. Editors count ślokas even when a sentence runs on (BCA: 99% of
   913 blocks are quatrains). No model step.
6. **Version `free`** (every text): an isolated subagent follows `prompts/stanza-grouping.md` — quatrains by default, a block ends where a
   sentence ends, lead lines (`ན་མོ།`, `ཨེ་མ་ཧོ།`) attach forward, prose rubrics stand alone
   (Liturgy-rails benchmark: boundary F1 0.95).
7. **Never** let a stanza cross a heading; every pāda belongs to exactly one block (the
   script refuses a `groups.json` that does not cover every pāda once, in order).
8. Never stamp IDs into a file that is cited elsewhere without re-running what cites it.

---

## Procedure

1. **Classify.** `python 4-SYSTEM/Skills/root-text-segmentation/scripts/root_text_build.py classify "<source>"`.
   Continue only on `verse` (exit 0). `commentary` → use `commentary-segmentation`;
   `prose`/`mixed` → stop and ask the editor.
2. **TOC (only if the text announces parts).** Look for announcements such as
   `<topic> བཤད་བྱ་སྟེ།`, `<topic> ཆོ་ག་ནི།`, `དང་པོ་ … ནི།`. If there are any, run
   `toc-tree-extraction` in mode `root` on a pāda-split copy (step 3 with no `--tree`
   produces one: `0-INBOX/<id>-root/prepared.md`) and keep its anchored tree. If pass 1
   finds nothing, skip — no tree.
3. **Prepare.**
   ```bash
   python 4-SYSTEM/Skills/root-text-segmentation/scripts/root_text_build.py prepare \
       "<source>" "0-INBOX/<id>-root" [--tree "<anchored tree>"] [--grouping auto|sloka|sense]
   ```
   Read its report line: pādas and metre, which frame elements were found, body headings
   placed (`not placed` must be 0), grouping mode. Check the printed heading list.
4. **Group.** The `sloka` version needs nothing (`groups-sloka.json` is written by `prepare`).
   For the `free` version (always), dispatch ONE isolated subagent: *"Read `4-SYSTEM/Skills/root-text-segmentation/prompts/stanza-grouping.md`
   and follow it exactly. The input is `0-INBOX/<id>-root/group-in.md` (read all of it). Write
   the JSON to `0-INBOX/<id>-root/groups-free.json`. Reply with the path and the block sizes."*
   Use `model: opus` at high effort. (This is the skill's only model step and it has no
   Gemini runner yet; the TOC step in 2 follows `toc-tree-extraction`'s model rules.)
5. **Finish.** `python … root_text_build.py finish "0-INBOX/<id>-root"` → `final-sloka.md`
   (translated texts) and `final-free.md`, each with IDs; the script verifies the text and
   each grouping.
6. **Review.** Report for each version: frame elements found, body headings, stanza sizes
   (blocks that are not 4 lines, and why), any odd pāda count in a part (often a real feature of the text —
   flag it, do not force it). A human chooses a version and approves it before it replaces the source.

---

## Completion check

- [ ] `classify` returned `verse`
- [ ] Frame headings present exactly for the elements found (front matter / author / translators)
- [ ] Body headings: top-level parts only, `not placed: 0` — or none, if the text announces no parts
- [ ] Translated text (`རྒྱ་གར་སྐད་དུ།`): both `final-sloka.md` and `final-free.md`; otherwise only `final-free.md`
- [ ] Each `groups-*.json` covers every pāda once; no stanza crosses a heading
- [ ] Each final file: text and footnotes unchanged (script assertion passed), IDs stamped (`^0`, `^I-n`, `^N-n`, `^a-n`, `^b-n`)
- [ ] Non-quatrain blocks listed with their reason in the report
- [ ] Source in `1-SOURCES/` untouched until a human chose and approved a version
