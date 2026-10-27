# Source audit against the raw intake files (2026-10-27)

All 563 texts in `1-SOURCES/` (root texts and commentaries) were compared with the raw files they were made from: `0-INBOX/root/<id>.md` and `0-INBOX/commentary/<id>.md`. A defect already present in the raw file is **source-side**: it was in the material as received. A defect absent from the raw file was introduced by **our** processing.

Scripts (read-only): `4-SYSTEM/scripts/footnote-labels/audit_footnotes.py` and `audit_body_text.py`, both with the default `--baseline raw`.

## Footnotes: 217,233 checked

| check | flags | origin |
|---|---|---|
| definition text changed or invented | 0 | none |
| raw footnote missing | 0 | none |
| definition without a marker | 0 | none |
| lemma does not match the text before the marker | 91 | **source**: the raw file has the same mismatch — 44 misplaced markers **moved** (see [Marker moves](#marker-moves-2026-10-27)) |
| lemma does not match | 4 | **ours**: Bh_3CCM d562; Ch_3CCb_ d747, d1147, d1151 — **fixed** |
| marker moved | 1 | **ours**: Bh_3CCM d562 — **fixed** |
| no witness `༼…༽` | 23 | by design: generic `[^nN]` notes |

All five of our flags came from the dropped body lines listed below. The definitions are identical to the raw file's. The lemma no longer matched only because the verse line before the marker was missing. With the lines restored, all five match (see [Fixed](#fixed-2026-10-27)).

Full list: [`footnote-audit.tsv`](footnote-audit.tsv), with an `origin` column.

### Our deliberate footnote changes, checked by hand

The comparison above ignores brackets, spacing and labels. These changes, which we made on purpose, were therefore paired with their raw footnotes and read one by one.

**Definitions that differ from raw: 213**

| change | count | finding |
|---|---|---|
| space added before `༼` (`། །༼` → `། ། ༼`) | 210 | each adds exactly one space; nothing else changed |
| closing `༽` added: Gu_3CFW d3016 (`༼སྣར། པེ།༽ གཉིས་ཀྱིས་`), At_3CGI d2 (`༼པེ། སྣར།༽ འཁོར་དུ།`) | 2 | correct: the bracket closes right after the sigla |
| opening `༼` added: Na_3CAN d75 (`༼པེ། སྣར།༽ བཞེས།`) | 1 | correct |

**Brackets in every durchen**
- In every durchen the brackets alternate correctly, `༼…༽` then the next `༼…༽`. No bracket is unclosed, nested or reversed.
- Every bracket contains only sigla: སྣར། པེ། སྡེ། ཅོ། and གསེར་བྲིས།, alone or combined.
- No sigla were found outside brackets. Two durchens in Ka_3CDU and one in Na_3CBJ look like it at first, but there `སྡེ` is part of the text.
- 18 durchens have a malformed siglum. Each is the same in the raw file, so the fault is in the source:
  - the final shad is missing: `༼ཅོ༽` ×6 (Sh_3CD1), `༼པེ༽` ×4, `༼སྣར། པེ༽` ×2, `༼སྣར༽`;
  - `༼སྣར་།༽`, `༼པེ། སྣར་༽`;
  - `༼པ། སྣར།༽`, which should read པེ (As_3CDd_ d10);
  - `༼པེ། ཤྣར།༽` (Na_3CAN d89).
- At_3CGX d11 has an editor's remark in parentheses after its witness, also from the source.

**Generic notes: 32**
- Every note has the same text as its raw footnote and sits after the same text.
- 9 give a lemma only, with no witness and no variant: Di_3CEo_ n1–n3, Sh_3CDC n1 and Va_3CEA n1–n5. They are like that in the raw file, so these durchens were incomplete in the source.
- The other 23 are colophons, verses printed as a footnote, source citations and editor's remarks. Some contain `༼ཉོ༽` or `༼༦༽`, but those are volume numbers, not witnesses.
- Separating them from the durchens was correct in every case.

**Renumbering: 5,355 footnotes in 13 texts**
- In each of the 13 texts the raw file numbers its footnotes 1…N in order.
- Every durchen is now `[^d(raw number − the notes before it)]`, and every note is `[^nK]` in order. There are no exceptions.
- No marker moved.
- Spot-checked in the files:

  | text | raw | ours |
  |---|---|---|
  | Va_3CEA | ^774, ^775, ^776, ^2620 | d774, n1, d775, d2615 |
  | Di_3CEo_ | ^1314, ^1315 | n3, d1312 |
  | Ch_3CCV | ^2 | d1 |

  Each pair has the same body text before the marker and the same definition.

## Body text: 563 texts, 532 identical to the raw file in every syllable

| finding | count | origin |
|---|---|---|
| verse lines dropped | 10 places (Bh_3CCM 2, Ch_3CCb_ 8) | **ours**: the 2026-10-14 block-ID step — **fixed** |
| footnote fragments appended after the colophon | 5 texts | **ours**: the same step — **fixed** |
| heading text that repeats the body line it names | 45 | not a defect (the vault's editorial headings) |

Nothing in the raw files' body text was found to be changed or lost apart from the items above.

### Stray tails

The 2026-10-14 step split the continuation lines of multi-line footnote definitions into body blocks and appended them after the end of the text. The definitions in the footnote section are still complete, so deleting these blocks loses nothing.

| text | real end | stray lines |
|---|---|---|
| Bh_3CCM | L7565 | L7567–L7579 (7 blocks) |
| Ch_3CCa_ | L11703 | L11705–L11737 (17 blocks) |
| Ch_3CCb_ | L11763 | L11765–L11843 (40 blocks) |
| Dh_3CEz_ | L3108 | L3110–L3138 (15 blocks) |
| Va_3CEF | L1355 | L1357–L1369 (7 blocks) |

### Dropped verse lines

The lost lines are verbatim from `0-INBOX/resegmented/<id>.reseg.md` and the raw file.

| text | 1-SOURCES line, before | lines lost |
|---|---|---|
| Bh_3CCM | L1925 | 1 |
| Bh_3CCM | L2297 | 1 |
| Ch_3CCb_ | L3325 | 3 |
| Ch_3CCb_ | L3339 | 1 |
| Ch_3CCb_ | L3345 | 1 |
| Ch_3CCb_ | L3351 | 2 |
| Ch_3CCb_ | L5016 | 1 |
| Ch_3CCb_ | L5046 | 3 |
| Ch_3CCb_ | L7395 | 3 |
| Ch_3CCb_ | L10603 | 2 |

Full list: [`body-audit.tsv`](body-audit.tsv), with an `origin` column.

The two problems have one cause. The 2026-10-14 step joined multi-line footnote definitions into one line. The definitions' continuation lines were left behind as body blocks after the colophon. Where a continuation line was identical to a verse line in the body, the body copy was removed instead.

## Fixed (2026-10-27)

Each fix was approved one text at a time. Every original file is backed up before it is changed:
- `0-INBOX/delete/restore-lost-lines-2026-10-27/`: Bh_3CCM and Ch_3CCb_ before their lines were restored.
- `0-INBOX/delete/strip-stray-tail-2026-10-27/`: all five texts before their tails were removed.

| # | fix | texts |
|---|---|---|
| 1 | re-inserted the 18 dropped lines, verbatim from the raw file | Bh_3CCM (2), Ch_3CCb_ (16) |
| 2 | removed the stray tail blocks; each block was first checked to be inside a footnote definition of the same file, and none is linked from anywhere in the vault | Bh_3CCM (7), Ch_3CCa_ (17), Ch_3CCb_ (40), Dh_3CEz_ (15), Va_3CEF (7) |
| 3 | re-linted, re-parsed, and re-audited against the raw file | all six |
| 4 | replaced the library edition under the existing text record: old durchens, toc and edition deleted, new ones posted | all six |

**After the fixes:**
- **Body text:** all six are identical to the raw file in every syllable. The one exception is Dh_3CEz_'s two editorial headings, which repeat their body lines.
- **Footnotes:** every definition matches the raw file. The one flag left is Dh_3CEz_ d1357, a lemma mismatch that is also in the raw file (source-side).
- **Library:** each live edition's content is identical to the local parse. Every durchen span equals its lemma, except Dh_3CEz_ d1357 (the source-side mismatch above). The old editions have no durchens left.

| text | old edition(s) | live edition | toc |
|---|---|---|---|
| Bh_3CCM | `uDwu5Dhsls0HoQ69UmhGO`, then `B6p46rAGmk2M65FSQmN2s` | `w3d01xF0kBAx3w5ZaoG6N` | `o8RJBuGqEKKxulLIguNcI` |
| Ch_3CCa_ | `SKFQrEOfR8pnprmqpTdaf` | `yef9ncyxecuv5KF7LCtrt` | `0FV6VsJJOd6HFZaS7xlF6` |
| Ch_3CCb_ | `3RdvdOK15YuSuFTnOIaEm` | `9mkfn6LrIhb7fXllI6rhX` | `XgLa4zMAuzKNy0wV9u1HN` |
| Dh_3CEz_ | `T7mdPgJflkmnrVmvhEpzG` | `yzqjrtZp5VTN6WcqMvDWN` | `OM3tsr55CEdRQ5vECc7M3` |
| Va_3CEF | `Gqn6YnrI5t1BkSygLCK3i` | `EA0SKL0TPsn6WsZZjAtWJ` | `FYs3wGN5584NPKUHEDWCR` |

The ids are recorded in each file's frontmatter and in `0-INBOX/temp/api-lint/commentary-upload-status.json`. The ledger's `replaced` list keeps every old edition with its durchen ids.

Bh_3CCM was replaced twice: once after its lines were restored, and again after its tail was removed.

## Marker moves (2026-10-27)

Of the 91 source-side lemma mismatches, 44 were a marker placed one or more syllables away from its lemma, the same in the raw file. Example: Dh_3CF4 `ཡིན༌[^d3904]ཏེ།` with `[^d3904]: ཡིན་ཏེ། ༼སྣར། པེ།༽ ཡིན་ནོ། །` — the variant replaces ཡིན་ཏེ།, so the marker belongs after ཏེ།. Each marker was moved to the end of the text its lemma names: 37 forward, 7 back. The lemma, the variant and the body text are unchanged; only the marker's position (and the `༌` before it) changed.

| text | moves |
|---|---|
| Na_3CAN | 9 |
| Na_3CAO | 4 |
| Dh_3CF4, As_3CDd_, Dh_3CF3, Sh_3CD1 | 3 each |
| Va_3CE1, Ar_3CBr_, Ka_3CDK, Na_3C9H, Na_3C9U | 2 each |
| Ka_3CDJ, Bh_3CCD, Ha_3CFM, Dh_3CF5, Ha_3CFJ, At_3CHN, Bh_3CCJ, Bh_3CCO, Na_3C9R | 1 each |

The 20 originals are backed up in `0-INBOX/delete/move-markers-2026-10-27/`.

**After the moves:**
- 43 of the 44 durchens now span exactly their lemma. Ha_3CFM d1182 sits in the right place but its span reads བའོོ, a doubled vowel in the source.
- Re-linted and re-parsed. The other durchens whose span differs from the lemma are the same as before the moves, all source-side.
- Bh_3CCO was changed locally only; it is not in the library (held as a duplicate of Bh_3CCJ).

### Library: updated in place (2026-10-28)

The other 19 texts were updated in the library **without replacing the edition**: the edition id is kept. Order: durchens and yigchungs deleted, alignments deleted (Dh_3CF5 only), toc deleted, segmentation deleted, all content removed with a `PATCH`, the new parse's content inserted with a `PATCH`, then segmentation, toc, durchens and alignments posted again.

Each live edition was then checked: the content equals the parse, every segment equals the parse (type, reference, lines), there is one toc, and the text has no other edition. Dh_3CF5's four alignment sets (from `Commentary_on_Valid_Cognition-rails`, 2,572 / 2,927 / 2,628 / 2,525 pairs) were re-sent and equal that vault's parser output.

| text | edition (kept) | new toc |
|---|---|---|
| Dh_3CF4 | `fTwrWaawshW6GuJ1XJXNk` | `0CW5Ig00IXOQcUDol0Gcm` |
| Ka_3CDJ | `f4VpUXDiMXyA3pR0iYddD` | `5lPbOTihy5J2WB9HgM6f2` |
| Va_3CE1 | `cIZlHzXAIGAwqBzXV6tv3` | `Itj6xI6EcOSpKayRVKzZm` |
| Bh_3CCD | `Ocn2Gam3ZQOLdD13SDHWg` | `A3SUaE3H6KogTtGEr7jGo` |
| Ha_3CFM | `60EVv4yV6jIUJc28EJMmC` | `kgpJ3JPQSONNKzp4yNYbv` |
| Ar_3CBr_ | `qI3ZQ6ScUkxgVsX2B2Om1` | `ZGmB8kSMereFLIBtNejsd` |
| As_3CDd_ | `GUCvW04Iql3N4vKJJuQA3` | `siEUPUx9TgFwyHRrnn8MC` |
| Dh_3CF3 | `1ovyjYwbWbVokRk2RiwuN` | `CffbDaY95dQ9tcyeHAeth` |
| Dh_3CF5 | `35KZRPj0d3oErozfsTCJ8` | `4cCfIXscxG4dQn5pscnqf` |
| Ha_3CFJ | `nNEQejsqJ0hEl8fsBetkN` | `HL206LhN0jKeMCuET9CTz` |
| Ka_3CDK | `ihWFb6626czzQtdlfdBo2` | `tOiOc2cL9rbSUes8m7bah` |
| Na_3C9H | `EMVt4FQ8Fyc1dhAT38wx3` | `hIdTpaGxZbeKZdgpNc4kt` |
| Na_3C9U | `rbDqKl1eyF3T1AYYnM9YW` | `1P7KuKSbTT4aJZCpu3zod` |
| Na_3CAN | `RxnxpwC0BkYsNWbiKdpEl` | `eiX94e3YZgAnqmYt1fevt` |
| Na_3CAO | `5iu8lDbiGq3dgdEg0uexW` | `VDhw4W6Vjax0q2Qoku1Mn` |
| Sh_3CD1 | `XL0hCaYxLkfjz5agcmgxu` | `di2Y0sFJ9B7XOBlPWV3zP` |
| At_3CHN | `SNkzK7fQApq0eV12WQAlY` | `lQYe5JRHQhiupyfSO4Hw0` |
| Bh_3CCJ | `CBnAh2lqd8sL4iaMlGq86` | `I70qazefuhfltCFmzcYmM` |
| Na_3C9R | `bVywvwfiawAyBthBh8bJt` | `102mtg28wgyJhgWYv4iSx` |

The new toc ids are in each file's frontmatter. Each ledger entry (`upload-status.json` for root texts, `commentary-upload-status.json` for commentaries) has an `updated_in_place` record with the old toc, durchen and yigchung ids; Dh_3CF5's also lists the four editions whose alignments were re-sent.

The six editions in [Fixed](#fixed-2026-10-27) were replaced (delete and re-post) before this in-place method was adopted; their old ids cannot be restored.

## Not fixed: source-side

These are in the material as received. They were left unchanged:
- 47 lemma mismatches (91 less the 44 moved markers): 13 sit in the right place but the lemma differs in spelling or is cut short, 25 need an editor to decide, and 9 are generic notes
- 18 malformed sigla
- 9 lemma-only notes
- At_3CGX d11's editor's remark
