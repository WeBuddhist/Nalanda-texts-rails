# Root-text segmentation — results for feedback (2026-10-07)

Everything here was produced by the `root-text-segmentation` skill (4-SYSTEM/Skills/), with
Claude agents for the model steps. The text itself is never changed: every output file was
checked character by character against its source (footnotes included).

**What to look at:** the layout (where blocks begin and end, what is verse and what is
prose), the headings, and the frame sections. Please mark anything an editor would do
differently — each correction becomes a rule in the skill.

---

## 1. Layout in short

| Part | Layout |
|---|---|
| Title | `# <title> ^0` |
| Front matter | `## ཀླད་ཀྱི་དོན། ^I-0` — Sanskrit (or Chinese) title, Tibetan title, homage |
| Body | the text's own announced parts as headings; if none, one heading `## གཞུང་དངོས། ^1-0` |
| Colophons | `## མཛད་བྱང། ^a-0` (author), `## འགྱུར་བྱང། ^b-0` (translators) |
| Verse | one pāda per line, one stanza per block |
| Prose (new) | one paragraph per block — one point (treatise) or one step (ritual) — on one line; verse quoted inside the prose stays as stanzas |

Verse texts translated from Sanskrit come in two versions: `-sloka` (always 4 lines) and
`-free` (stanzas by sense). Prose texts have one version: `-prose`.

---

## 2. The two prose texts

| File | Text | Result |
|---|---|---|
| `Ar_3CBc_-prose.md` | སྤྱོད་པ་བསྡུས་པའི་སྒྲོན་མ། (Āryadeva) — prose treatise, 41k syllables | 11 chapters as headings (7 and 9 with two sub-parts each); 381 paragraphs, 205 stanzas (quoted tantras) |
| `Ar_3CBh_-prose.md` | ཡེ་ཤེས་དབང་ཕྱུག་མའི་སྒྲུབ་ཐབས། — sādhana | the practice (`བདག་ཉིད་སྦྱོར་བ།`), then the torma / fire-offering / offering rites as headings; 100 paragraphs, 38 stanzas |

**Please check in particular:**

- **Chapter headings in Ar_3CBc_.** The chapters are named only in their closing line
  (`…ལེའུ་དང་པོའོ།`). We put the heading where the chapter *begins* and took its title from
  that closing line; the closing line itself stays at the end of the chapter. Right?
- **Ar_3CBh_ first part** has no title in the text; `བདག་ཉིད་སྦྱོར་བ།` is taken from a later
  sentence that refers back to it. Acceptable, or should it stay `གཞུང་དངོས།`?
- **Dialogue** (Ar_3CBc_ is a disciple–master dialogue): question and answer are separate
  paragraphs where the text allows.

---

## 3. Edge cases — one sample each (`edge-cases/`)

The 440 texts in `0-INBOX/root/` were surveyed for features that the layout rules have to
handle. Counts are from that survey; one small text per case was processed.

| # | Edge case | Texts | Sample | What the sample shows / what to check |
|---|---|---|---|---|
| 1 | **Prose root text** — treatise | 151 prose | `Dh_3CFD-prose` (རྒྱུད་གཞན་གྲུབ་པ།) | debate: each objection (`…ཞེ་ན།`) is its own paragraph, the answer starts the next |
| 2 | Prose, quote-heavy | 15 | `Ka_3CDN-prose` (བྱང་ཆུབ་ཀྱི་སེམས་བསྒོམ་པ།) | quoted sūtra verse as stanzas inside the prose; `ཞེས་གསུངས་སོ།` opens the next paragraph |
| 3 | Prose ritual, no Sanskrit title, homage *before* the title | 117 without Skt title | `At_3CGI-prose` (གཙུག་ཏོར་དྲི་མེད་ཀྱི་གཟུངས་ཆོག) | front matter = homage + title |
| 4 | **Translated from Chinese** (`རྒྱའི་སྐད་དུ།`) | 2 | `Va_3CET-prose` (ཐེག་པ་ཆེན་པོའི་ཆོས་བརྒྱ་གསལ་བའི་སྒོ) | Chinese title in the front matter; its two announced parts (`ཆོས་ཐམས་ཅད།`, `བདག་མེད་པ།`) as headings |
| 5 | **Mixed** verse sādhana with mantras | 42 mixed | `At_3CGC-prose` (དཔལ་རྟ་མགྲིན་གྱི་སྒྲུབ་ཐབས།) | mostly stanzas; front matter = title repeated + homage |
| 6 | Verse in a **long, irregular metre** (recipes) | — | `Na_3CBM-prose` (སྤོས་ཀྱི་སྦྱོར་བ།) | 17-syllable lines that vary 14–19 |
| 7 | **Long-metre verse** (19 syllables) | 15 | `Na_3C9V-free/-sloka` (དཔལ་ནག་པོ་ཆེན་པོའི་བསྟོད་པ།) | stanzas of long lines; mantra lines inside the praise |
| 8 | 9-syllable verse | 35 | `Va_3CEb_-free/-sloka` (ཚུལ་ཁྲིམས་ཀྱི་གཏམ།) | plain case, for comparison |
| 9 | **Sections closed inside the text**; translator's own verse after the colophon | 12 | `Na_3CBI-free/-sloka` (སྦྱོར་བ་བརྒྱ་པ། — medical) | 9 sections as headings; section-closing lines as 1-line blocks; translator's dedication kept in `འགྱུར་བྱང།` |
| 10 | Verse text whose **title says "commentary"** | 2 | `Na_3C9e_-free/-sloka` (བྱང་ཆུབ་སེམས་ཀྱི་འགྲེལ་པ།) | laid out as verse, not as a commentary |
| 11 | Verse prayer with one gloss-like phrase | — | `Na_3CBR-free/-sloka` (རྡོ་རྗེའི་སྨོན་ལམ།) | earlier mistaken for a commentary; now verse |
| 12 | **Very short / fragment** | 25 | `Ch_3CCU-prose` (53 syllables) | one stanza; the same fragment is in the folder three times (`Ch_3CCU`, `Sh_3CCh_`, `Na_3C9x_`) |

Not processed, listed for discussion:

| Edge case | Texts | Example | Question |
|---|---|---|---|
| Commentary-like texts in the root folder (gloss markers ≥ 1 per 1000 syllables) | 37 | `At_3CH9` (མི་དགེ་བ་བཅུའི་ལས་ཀྱི་ལམ་བསྟན་པ།, 11 markers / 1000) | root or commentary? |
| Very long anthologies (> 50k syllables, quote-heavy) | 23 | `Sh_3CCs_` (བསླབ་པ་ཀུན་ལས་བཏུས་པ།) | same prose layout, or a different one for anthologies? |
| No colophon at all | 86 | `At_3CFy_` | fine without `མཛད་བྱང།`/`འགྱུར་བྱང།`? |

---

## 4. Questions for the editors

1. **Paragraph size in prose:** one point (treatise) / one step (ritual), usually 1–5
   sentences. Too fine, too coarse?
2. **Objection and answer** as separate paragraphs; a teaching question (`…གང་ཞེ་ན།`) kept
   with its answer. Agree?
3. **Quotation close** `ཞེས་གསུངས་སོ།` — start of the next paragraph (now), or end of the
   quotation?
4. **Mantras** — inside the paragraph of their step (now), or on their own line?
5. **Section-closing lines** (`…དཔྱད་དོ།`, `…ལེའུ་…པའོ།`) — own block (now), or the last line
   of the section's last block?
6. **Homage without a Sanskrit title** — front matter in prose texts (now); in verse texts it
   stays in the body as the first line of the first stanza. Right?
7. **A tree with one top-level part** (Ar_3CBh_'s rite section): its sub-parts become `###`
   headings. Right?
8. **Ar_3CBg_** (processed earlier as verse) now classifies as mixed — should it be redone
   in the prose layout?
9. Can you share an **edited prose root text** (treatise or sādhana) as a reference? The
   prose rules are a first draft without one.

## 5. Known rough edges (we will fix them; no need to report)

- A verse quote written with single shads (`།` instead of `། །`) is not recognised as verse
  and stays inside a paragraph (a few in Ar_3CBc_, Ka_3CDN).
- A line that closes a section straight after verse can be taken as the last verse line
  (Ar_3CBc_ unit 1763).
- In Ar_3CBh_ a few torma-invocation lines are split between verse and prose.
