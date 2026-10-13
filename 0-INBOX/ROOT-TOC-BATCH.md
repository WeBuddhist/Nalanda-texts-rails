# Root-text TOC batch — extract now, ingest later

Running `root-text-toc-extract` on every root text in `0-INBOX/root/`, one text at a time.
**No ingest yet**: the headings are put into the texts later, together with the updated
segmentation. This document says where everything is and how to continue.

Updated 2026-10-13 · 442 texts · done 244 · no parts announced 179 · earlier run 19 · failed 0 · running 0 · **to do 0**

Size classes (characters of `0-INBOX/root/<id>.md`): small < 30,000 · medium 30,000–199,999 · large ≥ 200,000 — small 358 · medium 60 · large 24. How to run the rest with Gemini: `0-INBOX/temp/root-toc/README.md`.

## Where things are

| What | Path |
|---|---|
| Source texts | `0-INBOX/root/<id>.md` |
| Reading copy the TOC passes read (`root-text-segment`, deterministic; overwritten when the segmentation is re-run) | `0-INBOX/temp/root-seg-v2/<id>/prepared.md` (+ `group-in.md`, `state.json`) |
| TOC working files | `0-INBOX/temp/TOC-<id>/` — `chunk-index.tsv`, `candidates/`, `enumerations/`, `toc-candidates-<id>.md`, `toc-enumerations-<id>.md`, `toc-tree-<id>.md` |
| QC reports | `0-INBOX/temp/TOC-<id>/toc-tree-qc-<id>.md` (pass 4) · `toc-tree-qc-source-<id>.md` (pass 6, against the text) |
| **The tree to ingest later** | `0-INBOX/temp/TOC-<id>/toc-tree-anchored-<id>.md` — each node ends in `[[the words where the part begins]]` |
| Instructions each text's coordinator agent follows | `0-INBOX/temp/root-toc/COORDINATOR.md` |
| This batch's status (machine-readable) | `0-INBOX/temp/root-toc/status.json` · updated with `python 0-INBOX/temp/root-toc/status.py set <id> …` |

Texts with status `no-parts` announce no parts (most prayers and chants): no tree, and their
`## གཞུང་དངོས། ^1-0` heading stays. Texts with status `earlier-run` were done before this
batch (the 22 processed ones); their folders were left as they were.

## How to continue

**Resume the extraction:** `python 0-INBOX/temp/root-toc/status.py next` prints the next text
to do; run `root-text-segment` then `root-text-toc-extract` on it (procedure below) and set its
row. A text whose `TOC-<id>/` already holds chunk files resumes where it stopped — finished
chunks are skipped.

```bash
python 4-SYSTEM/Skills/seg-toc-lib/root_text_build.py segment "0-INBOX/root/<id>.md" "0-INBOX/temp/root-seg-v2/<id>"
# then root-text-toc-extract on 0-INBOX/temp/root-seg-v2/<id>/prepared.md, id <id> (passes 1–6)
```

**Ingest later, after the segmentation update** (no model calls for the TOC):

```bash
python 4-SYSTEM/Skills/seg-toc-lib/root_text_build.py segment "0-INBOX/root/<id>.md" "0-INBOX/temp/root-seg-v2/<id>"
python 4-SYSTEM/Skills/seg-toc-lib/root_text_build.py toc-ingest "0-INBOX/temp/root-seg-v2/<id>"     --tree "0-INBOX/temp/TOC-<id>/toc-tree-anchored-<id>.md"     # only for texts with a tree
# check the report: "not placed: 0"; then root-text-group and root-text-block-ids
```

The anchors are the text's own words, so the tree does not go stale when the segmentation
rules change. The only thing to check at ingest is `not placed: 0` — a part whose opening
words end up mid-line under the new rules is placed by hand.

## Status

`form` verse / prose / mixed · `units` lines in the reading copy · `parts` top-level parts ·
`nodes` all nodes · `qc4` pass-4 issues before→after repair · `qc6` pass-6 result against the text.

| # | id | size | chars | source lines | status | form | units | chunks | parts | nodes | qc4 | qc6 | note | run (model · cost · time) | tree |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ar_3CBa_ | medium | 98701 | 613 | earlier-run |  |  |  |  |  |  |  | anchored tree from an earlier run |  |  |
| 2 | Ar_3CBc_ | medium | 184118 | 914 | earlier-run |  |  |  |  |  |  |  | anchored tree from an earlier run |  |  |
| 3 | Ar_3CBe_ | small | 5391 | 48 | done | verse |  |  | 2 | 11 |  | 0 issues | earlier run: tree was already anchored (saved as toc-tree-Ar_3CBe_.md); copied to toc-tree-anchored-, pass 6 clean; preamble II. རྡོ་རྗེ་དྲིལ་བུ་བྱིན་གྱིས་བརླབ། | Claude agents (earlier run) | `TOC-Ar_3CBe_/toc-tree-anchored-Ar_3CBe_.md` |
| 4 | Ar_3CBf_ | small | 2686 | 16 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 5 | Ar_3CBg_ | medium | 32477 | 181 | earlier-run |  |  |  |  |  |  |  | anchored tree from an earlier run |  |  |
| 6 | Ar_3CBh_ | medium | 38181 | 262 | earlier-run |  |  |  |  |  |  |  | anchored tree from an earlier run |  |  |
| 7 | Ar_3CBi_ | small | 18829 | 117 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 8 | Ar_3CBj_ | small | 8792 | 44 | no-parts | verse | 241 | 1 | 0 | 0 |  |  | finished with Claude: one implicit candidate (ཤིན་ཏུ་རྙེད་དཀའི་རིམ་དབྱེ་), no enumerations — empty tree |  |  |
| 9 | Ar_3CBk_ | small | 9268 | 65 | earlier-run |  |  |  |  |  |  |  | anchored tree from an earlier run |  |  |
| 10 | Ar_3CBl_ | small | 5656 | 37 | earlier-run |  |  |  |  |  |  |  | anchored tree from an earlier run |  |  |
| 11 | Ar_3CBm_ | small | 10396 | 63 | done | prose | 113 | 4 | 4 | 4 | 0→0 | 1 accepted (closing-line title) | four modes of explanation (ཚུལ་བཞི); ཆོས་བདུན list dropped as subject matter |  | `TOC-Ar_3CBm_/toc-tree-anchored-Ar_3CBm_.md` |
| 12 | Ar_3CBn_ | small | 2421 | 15 | no-parts | verse | 64 | 2 | 0 | 0 |  |  |  |  |  |
| 13 | Ar_3CBo_ | small | 16410 | 83 | no-parts | verse | 416 | 8 | 0 | 0 |  |  |  |  |  |
| 14 | Ar_3CBp_ | small | 11627 | 109 | done | prose | 121 | 3 | 1 | 7 | 0→0 | 4 accepted (titles from the enumeration); anchors all found | REVIEW: preamble II. རྒྱུད་བརྟག་པ། (II rule: true preamble only); 1.3 enumeration says ཐབས་, text ཐམས་ཅད་; 1.5 anchored at the citation line གསང་བ་འདུས་པ་ལས། |  | `TOC-Ar_3CBp_/toc-tree-anchored-Ar_3CBp_.md` |
| 15 | Ar_3CBq_ | small | 13017 | 91 | done | verse | 299 | 6 | 3 | 4 | 0→0 | 0 issues | REVIEW: preamble II. [[མནོས་ནས་སུ།]]; candidate གཞོན་ནུའི་བརྟུལ་ཞུགས་ not kept as a node |  | `TOC-Ar_3CBq_/toc-tree-anchored-Ar_3CBq_.md` |
| 16 | Ar_3CBr_ | small | 3400 | 10 | no-parts | verse | 72 | 2 | 0 | 0 |  |  | hymn to the fifteen goddesses (rerun after an early hand-back) |  |  |
| 17 | Ar_3CBs_ | small | 12223 | 30 | done | prose | 26 | 2 | 1 | 7 | 0→0 | 1 order error → 0 after repair | REVIEW: preamble II. (homage); announced order འཕང་སྲེག་གནན, text order འཕང→མནན→སྲེག; 1.3.3 སྲེག anchor inferred |  | `TOC-Ar_3CBs_/toc-tree-anchored-Ar_3CBs_.md` |
| 18 | Ar_3CBt_ | small | 2531 | 3 | no-parts | prose | 8 | 1 | 0 | 0 |  |  | short sādhana |  |  |
| 19 | Ar_3CBu_ | small | 4331 | 15 | no-parts | prose | 75 | 2 | 0 | 0 |  |  | one candidate (དབང་བཞི་, an instruction) dropped by pass 3 as a false positive |  |  |
| 20 | Ar_3CBv_ | small | 3458 | 5 | no-parts | prose | 6 | 1 | 0 | 0 |  |  | short sādhana |  |  |
| 21 | Ar_3CBw_ | small | 3845 | 19 | done | prose | 70 | 2 | 1 | 1 | 0→0 | 0 issues | REVIEW: one node སྦྱིན་སྲེག་ཆོ་ག; the 6-item list (ཐབས/ཤིང/མེ/རྫས/དུས/ཆོ་ག) kept as content, not sub-parts |  | `TOC-Ar_3CBw_/toc-tree-anchored-Ar_3CBw_.md` |
| 22 | Ar_3CBx_ | small | 1989 | 9 | done | prose | 26 | 1 | 1 | 12 | 0→0 | 11 accepted (titles from the opening list); anchors all found, in order | REVIEW: 11 rite steps from the opening verse; 6 anchors inside one prose paragraph (line 39) — check at ingest that each falls at a sentence start; node 1 title from the title line |  | `TOC-Ar_3CBx_/toc-tree-anchored-Ar_3CBx_.md` |
| 23 | Ar_3CBy_ | small | 1682 | 10 | done | verse | 47 | 1 | 1 | 4 | 0→0 | 0 issues | one part with 3 sub-parts from the opening announcement verse |  | `TOC-Ar_3CBy_/toc-tree-anchored-Ar_3CBy_.md` |
| 24 | Ar_3CBz_ | small | 1508 | 13 | no-parts | verse | 28 | 1 | 0 | 0 |  |  | short verse text |  |  |
| 25 | Ar_3CC1 | medium | 62521 | 499 | done | verse | 1620 | 29 | 16 | 16 | 0→0 | 9 accepted (closing-line titles) | Catuḥśataka: 16 chapters, titles from their closing lines |  | `TOC-Ar_3CC1/toc-tree-anchored-Ar_3CC1.md` |
| 26 | Ar_3CC2 | small | 11593 | 65 | done | verse | 324 | 6 | 10 | 10 | 0→0 | 0 issues | REVIEW: preamble II. སྡོམ། (a summary verse, not an homage); 10 parts opened by དེ་ལ་…ནི། |  | `TOC-Ar_3CC2/toc-tree-anchored-Ar_3CC2.md` |
| 27 | Ar_3CC3 | small | 1072 | 7 | no-parts | verse | 25 | 1 | 0 | 0 |  |  | short verse text |  |  |
| 28 | Ar_3CC5 | small | 7443 | 32 | done | prose | 54 | 1 | 2 | 2 | 0→0 | 0 issues | 2 topic headers (Type D); preamble II. མཆོད་བརྗོད། |  | `TOC-Ar_3CC5/toc-tree-anchored-Ar_3CC5.md` |
| 29 | Ar_3CC6 | small | 5181 | 25 | done | verse | 154 | 3 | 1 | 5 | 0→0 | 4 accepted (closing-line titles) | REVIEW: 4 tenet schools under one division; preamble II.; the text after 1.4 (l.236 up to the colophon) falls under 1.4 |  | `TOC-Ar_3CC6/toc-tree-anchored-Ar_3CC6.md` |
| 30 | Ar_3CC7 | small | 7856 | 39 | no-parts | verse | 201 | 4 | 0 | 0 |  |  |  |  |  |
| 31 | Ar_3CC8 | small | 2910 | 7 | no-parts | verse | 72 | 2 | 0 | 0 |  |  |  |  |  |
| 32 | Ar_3CC9 | small | 1885 | 7 | no-parts | verse | 48 | 1 | 0 | 0 |  |  |  |  |  |
| 33 | Ar_3CCA | small | 2571 | 5 | no-parts | verse | 71 | 2 | 0 | 0 |  |  |  |  |  |
| 34 | Ar_3CCB | small | 1946 | 9 | no-parts | verse | 50 | 1 | 0 | 0 |  |  |  |  |  |
| 35 | As_3CDc_ | small | 2645 | 9 | no-parts | verse | 73 | 2 | 0 | 0 |  |  |  |  |  |
| 36 | As_3CDd_ | small | 7225 | 51 | no-parts | prose | 29 | 1 | 0 | 0 |  |  |  |  |  |
| 37 | As_3CDe_ | small | 3386 | 23 | no-parts | prose | 23 | 1 | 0 | 0 |  |  |  |  |  |
| 38 | As_3CDk_ | large | 301793 | 1278 | done | prose | 2032 | 42 | 3 | 156 | 0→0 | 32→10 accepted (footnote markers in titles, generic titles); anchors all found, in order | REVIEW: upper volume (སྟོད་ཆ) of the bhūmi treatise, 3 of the 17 listed parts in this volume; preamble II.; INGEST: 3.3.1–3.3.3 anchors share their first 60 characters (lines 3083/3087/3091) — place 3.3.2 and 3.3.3 by hand |  | `TOC-As_3CDk_/toc-tree-anchored-As_3CDk_.md` |
| 39 | As_3CDl_ | large | 703698 | 2870 | done | prose | 5285 | 103 | 10 | 204 | 0→0 | 26 accepted (titles from earlier lists); anchors all found, in order | bhūmi treatise, 10 bhūmis (savitarka-savicāra … anupadhika); chunks 085–102 are the footnote apparatus; resumed after a usage-limit cut-off |  | `TOC-As_3CDl_/toc-tree-anchored-As_3CDl_.md` |
| 40 | As_3CDm_ | large | 769194 | 4356 | done | prose | 3171 | 82 | 4 | 514 | 0→0 | 65→56 accepted (titles from lists, 3 siblings in one sentence); 12 order errors repaired | REVIEW: 514 nodes; lines 6551+ are footnotes; SEGMENT: translators' colophon starts at line 6543 (རྒྱ་གར་གྱི་མཁན་པོ་ཛི་ན་མི་ཏྲ་དང་།), before the མཇུག་བྱང། heading |  | `TOC-As_3CDm_/toc-tree-anchored-As_3CDm_.md` |
| 41 | As_3CDn_ | large | 843795 | 4548 | done | prose | 3959 | 94 | 11 | 380 | 0→0 | 55 accepted (titles from lists); 3 [[?]] repaired | REVIEW: 380 nodes; repair removed 2 listed-but-untreated parts; 5.2–5.12 anchored on the short definitions, not the longer second pass; lines 13–27 (overview) before node 1; lines 7933+ footnotes; resumed after a usage-limit cut-off; INGEST: part 5 anchor is only སྡོམ་ནི། (a phrase that repeats) — check its placement |  | `TOC-As_3CDn_/toc-tree-anchored-As_3CDn_.md` |
| 42 | As_3CDo_ | large | 773563 | 3394 | done | prose | 5034 | 106 | 8 | 352 | 0 | 32 accepted (titles from lists/closing lines; 2 shared anchors) | REVIEW: 352 nodes; 7.4.1.1.1–4 and 2.2.3.2.2/.3 share one anchor each (one sentence covers them) — merge at ingest?; 1.29.2 title ཁ་ཟས་ཀྱི་དངོས་པོ་ལ་མཁས་པ from the closing line, but the section treats the elements (ཁམས); resumed after a usage-limit cut-off |  | `TOC-As_3CDo_/toc-tree-anchored-As_3CDo_.md` |
| 43 | As_3CDp_ | large | 768507 | 3220 | done | prose | 4155 | 89 | 6 | 291 | 0→0 | 25→22 accepted (titles from lists); 3 order errors repaired | REVIEW: 291 nodes, 6 viniścaya sections; SEGMENT BUG: root_text_build segment failed with 'unit count changed' on a heading split across a line (prepared.md l.3477, ### ༄༅། །རྣལ་འབྱོར་སྤྱོད་པའི་ས་རྣམ་པར་ ### གཏན་ལ་དབབ་པ་བསྡུ་བ།) — state.json not written, fix before ingest; lines 8323+ footnotes |  | `TOC-As_3CDp_/toc-tree-anchored-As_3CDp_.md` |
| 44 | As_3CDq_ | large | 773663 | 3258 | done | prose | 11970 | 96 | 1 | 149 | 0 | 24 flags | Gemini run — review the top-level parts; 6 node(s) without an anchor ([[?]]) | 3.8-flash medium · $9.52 · 44.7 min | `TOC-As_3CDq_/toc-tree-anchored-As_3CDq_.md` |
| 45 | As_3CDr_ | medium | 78926 | 386 | done | prose | 1732 | 14 | 7 | 89 | 0 | 19 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.34 · 2.2 min | `TOC-As_3CDr_/toc-tree-anchored-As_3CDr_.md` |
| 46 | As_3CDs_ | medium | 101803 | 491 | done | prose | 2589 | 21 | 2 | 2 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.29 · 1.7 min | `TOC-As_3CDs_/toc-tree-anchored-As_3CDs_.md` |
| 47 | As_3CDt_ | medium | 84353 | 417 | done | prose | 1471 | 12 | 1 | 105 | 1→1→1 | 29 flags | Gemini run — review the top-level parts; 2 node(s) without an anchor ([[?]]) | 3.8-flash low · $0.50 · 2.6 min | `TOC-As_3CDt_/toc-tree-anchored-As_3CDt_.md` |
| 48 | As_3CDu_ | medium | 165231 | 840 | done | prose | 3672 | 30 | 10 | 93 | 1→0 | 24 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.74 · 3.5 min | `TOC-As_3CDu_/toc-tree-anchored-As_3CDu_.md` |
| 49 | As_3CDv_ | large | 295926 | 1791 | done | prose | 7141 | 57 | 11 | 153 | 0 | 11 flags | Gemini run — review the top-level parts | 3.8-flash medium · $3.48 · 37.5 min | `TOC-As_3CDv_/toc-tree-anchored-As_3CDv_.md` |
| 50 | As_3CDw_ | small | 24350 | 142 | done | prose | 726 | 6 | 16 | 29 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.10 · 0.8 min | `TOC-As_3CDw_/toc-tree-anchored-As_3CDw_.md` |
| 51 | At_3CFb_ | small | 20975 | 66 | done | verse | 1368 | 11 | 4 | 4 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.07 · 0.3 min | `TOC-At_3CFb_/toc-tree-anchored-At_3CFb_.md` |
| 52 | At_3CFc_ | small | 6710 | 25 | done | prose | 189 | 2 | 4 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-At_3CFc_/toc-tree-anchored-At_3CFc_.md` |
| 53 | At_3CFd_ | medium | 58760 | 174 | done | prose | 1390 | 11 | 5 | 21 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.37 · 4.8 min | `TOC-At_3CFd_/toc-tree-anchored-At_3CFd_.md` |
| 54 | At_3CFe_ | small | 7891 | 28 | done | prose | 134 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CFe_/toc-tree-anchored-At_3CFe_.md` |
| 55 | At_3CFf_ | small | 8629 | 29 | done | prose | 189 | 2 | 10 | 10 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.4 min | `TOC-At_3CFf_/toc-tree-anchored-At_3CFf_.md` |
| 56 | At_3CFg_ | small | 2980 | 18 | done | prose | 62 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CFg_/toc-tree-anchored-At_3CFg_.md` |
| 57 | At_3CFh_ | small | 5101 | 25 | no-parts | verse | 105 | 2 | 0 | 0 |  |  | Claude redo: no parts announced (the Gemini tree had made 4 sub-parts from the letters ཤྲཱི ཧེ རུ ཀ; kept as TOC-At_3CFh_.gemini) | Claude agents (redo) |  |
| 58 | At_3CFj_ | small | 4646 | 11 | no-parts | verse | 219 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 59 | At_3CFl_ | small | 2453 | 13 | no-parts | verse | 125 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 60 | At_3CFm_ | small | 6017 | 48 | no-parts | prose | 37 | 1 | 0 | 0 |  |  | Claude redo: no parts announced (Gemini tree kept as TOC-At_3CFm_.gemini) | Claude agents (redo) |  |
| 61 | At_3CFn_ | small | 4017 | 22 | no-parts | prose | 88 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 62 | At_3CFo_ | small | 2854 | 20 | no-parts | verse | 172 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 63 | At_3CFp_ | small | 2454 | 13 | no-parts | verse | 125 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 64 | At_3CFq_ | small | 795 | 9 | no-parts | prose | 45 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 65 | At_3CFr_ | small | 2108 | 11 | no-parts | prose | 49 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 66 | At_3CFs_ | small | 8680 | 82 | done | prose | 144 | 1 | 1 | 4 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-At_3CFs_/toc-tree-anchored-At_3CFs_.md` |
| 67 | At_3CFt_ | medium | 40204 | 156 | done | prose | 806 | 7 | 13 | 15 | 1→0 | 6 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.22 · 2.5 min | `TOC-At_3CFt_/toc-tree-anchored-At_3CFt_.md` |
| 68 | At_3CFu_ | small | 4479 | 17 | done | prose | 163 | 2 | 4 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CFu_/toc-tree-anchored-At_3CFu_.md` |
| 69 | At_3CFv_ | small | 2859 | 15 | no-parts | verse | 185 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 70 | At_3CFw_ | small | 2566 | 15 | done | verse | 129 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CFw_/toc-tree-anchored-At_3CFw_.md` |
| 71 | At_3CFx_ | small | 2134 | 8 | no-parts | verse | 124 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 72 | At_3CFy_ | small | 2302 | 13 | no-parts | verse | 135 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 73 | At_3CFz_ | small | 2214 | 12 | done | verse | 130 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CFz_/toc-tree-anchored-At_3CFz_.md` |
| 74 | At_3CG0 | small | 6439 | 44 | no-parts | verse | 320 | 3 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 75 | At_3CG1 | small | 20994 | 95 | done | verse | 1309 | 11 | 6 | 22 | 0 | 4 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.10 · 0.5 min | `TOC-At_3CG1/toc-tree-anchored-At_3CG1.md` |
| 76 | At_3CG2 | small | 827 | 9 | no-parts | prose | 33 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 77 | At_3CG3 | small | 2167 | 15 | done | verse | 125 | 1 | 1 | 3 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.3 min | `TOC-At_3CG3/toc-tree-anchored-At_3CG3.md` |
| 78 | At_3CG4 | small | 1997 | 14 | no-parts | verse | 110 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 79 | At_3CG5 | small | 19489 | 129 | done | verse | 1129 | 9 | 2 | 27 | 0 | 10 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.09 · 0.5 min | `TOC-At_3CG5/toc-tree-anchored-At_3CG5.md` |
| 80 | At_3CG6 | small | 5381 | 37 | done | verse | 124 | 3 | 2 | 3 | 0→0 | 0 issues | Claude redo: 2 parts (topic headers), preamble II. དམ་ཚིག་ལྷ་བསྐྱེད་པ།; anchors keep the footnote markers (Gemini tree kept as TOC-At_3CG6.gemini) | Claude agents (redo) | `TOC-At_3CG6/toc-tree-anchored-At_3CG6.md` |
| 81 | At_3CG7 | small | 1447 | 8 | no-parts | verse | 94 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 82 | At_3CG8 | small | 2298 | 17 | done | verse | 141 | 1 | 3 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CG8/toc-tree-anchored-At_3CG8.md` |
| 83 | At_3CG9 | small | 8206 | 60 | done | prose | 160 | 2 | 4 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-At_3CG9/toc-tree-anchored-At_3CG9.md` |
| 84 | At_3CGA | small | 4306 | 17 | done | verse | 219 | 2 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CGA/toc-tree-anchored-At_3CGA.md` |
| 85 | At_3CGa_ | small | 3599 | 20 | done | prose | 84 | 1 | 9 | 9 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CGa_/toc-tree-anchored-At_3CGa_.md` |
| 86 | At_3CGB | small | 11823 | 71 | done | prose | 155 | 2 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.2 min | `TOC-At_3CGB/toc-tree-anchored-At_3CGB.md` |
| 87 | At_3CGb_ | small | 3626 | 12 | done | prose | 46 | 1 | 7 | 7 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CGb_/toc-tree-anchored-At_3CGb_.md` |
| 88 | At_3CGC | small | 2975 | 13 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 89 | At_3CGc_ | small | 4376 | 20 | done | prose | 44 | 1 | 6 | 6 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CGc_/toc-tree-anchored-At_3CGc_.md` |
| 90 | At_3CGD | small | 2476 | 12 | no-parts | verse | 126 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.2 min |  |
| 91 | At_3CGd_ | small | 2757 | 10 | done | prose | 30 | 1 | 9 | 9 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.4 min | `TOC-At_3CGd_/toc-tree-anchored-At_3CGd_.md` |
| 92 | At_3CGE | small | 3906 | 23 | done | verse | 195 | 2 | 1 | 11 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.6 min | `TOC-At_3CGE/toc-tree-anchored-At_3CGE.md` |
| 93 | At_3CGe_ | small | 3033 | 10 | done | prose | 50 | 1 | 2 | 6 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CGe_/toc-tree-anchored-At_3CGe_.md` |
| 94 | At_3CGF | small | 2266 | 11 | done | verse | 135 | 1 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.7 min | `TOC-At_3CGF/toc-tree-anchored-At_3CGF.md` |
| 95 | At_3CGf_ | small | 3749 | 16 | done | prose | 40 | 1 | 3 | 3 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CGf_/toc-tree-anchored-At_3CGf_.md` |
| 96 | At_3CGG | small | 2039 | 12 | no-parts | verse | 98 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 97 | At_3CGg_ | small | 5315 | 19 | done | prose | 85 | 1 | 5 | 8 | 2→1→0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.4 min | `TOC-At_3CGg_/toc-tree-anchored-At_3CGg_.md` |
| 98 | At_3CGH | small | 2255 | 15 | no-parts | prose | 51 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 99 | At_3CGh_ | small | 3571 | 17 | done | prose | 55 | 1 | 2 | 8 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.4 min | `TOC-At_3CGh_/toc-tree-anchored-At_3CGh_.md` |
| 100 | At_3CGI | small | 1933 | 14 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 101 | At_3CGi_ | small | 3122 | 15 | no-parts | prose | 14 | 1 | 0 | 0 |  |  | Claude redo: no parts announced (the Gemini tree had listed the 13 rites of the series; kept as TOC-At_3CGi_.gemini) | Claude agents (redo) |  |
| 102 | At_3CGJ | small | 3902 | 25 | done | verse | 231 | 2 | 4 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CGJ/toc-tree-anchored-At_3CGJ.md` |
| 103 | At_3CGj_ | small | 10468 | 29 | no-parts | prose | 141 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 104 | At_3CGK | small | 1849 | 9 | done | prose | 33 | 1 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CGK/toc-tree-anchored-At_3CGK.md` |
| 105 | At_3CGk_ | small | 3469 | 9 | no-parts | prose | 8 | 1 | 0 | 0 |  |  | Claude redo: no parts — the list of signs (ཕྱི་/ནང་/མི་འགྲུབ་/ལྡོག་) is content, not parts (Gemini tree kept as TOC-At_3CGk_.gemini) | Claude agents (redo) |  |
| 106 | At_3CGL | small | 2100 | 16 | no-parts | verse | 122 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 107 | At_3CGl_ | small | 1722 | 7 | done | prose | 49 | 1 | 4 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CGl_/toc-tree-anchored-At_3CGl_.md` |
| 108 | At_3CGM | small | 5842 | 44 | done | prose | 114 | 1 | 2 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CGM/toc-tree-anchored-At_3CGM.md` |
| 109 | At_3CGm_ | small | 3399 | 13 | done | prose | 111 | 1 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CGm_/toc-tree-anchored-At_3CGm_.md` |
| 110 | At_3CGN | small | 21136 | 123 | done | prose | 549 | 5 | 21 | 35 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.10 · 0.9 min | `TOC-At_3CGN/toc-tree-anchored-At_3CGN.md` |
| 111 | At_3CGn_ | small | 4135 | 8 | done | prose | 78 | 1 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CGn_/toc-tree-anchored-At_3CGn_.md` |
| 112 | At_3CGO | small | 1669 | 9 | no-parts | verse | 99 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 113 | At_3CGo_ | small | 1787 | 5 | no-parts | verse | 79 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 114 | At_3CGP | medium | 32563 | 182 | done | prose | 890 | 7 | 2 | 21 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.10 · 0.5 min | `TOC-At_3CGP/toc-tree-anchored-At_3CGP.md` |
| 115 | At_3CGp_ | small | 1233 | 5 | no-parts | verse | 79 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 116 | At_3CGQ | small | 3596 | 18 | done | prose | 84 | 1 | 9 | 9 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CGQ/toc-tree-anchored-At_3CGQ.md` |
| 117 | At_3CGq_ | medium | 39250 | 291 | done | verse | 995 | 18 | 2 | 64 | 1→0 | 14 accepted title-not-near flags | Claude redo: 2 parts + II. preamble; repair dropped unattested 2.5.1 (Gemini tree kept as TOC-At_3CGq_.gemini) | Claude agents (redo) | `TOC-At_3CGq_/toc-tree-anchored-At_3CGq_.md` |
| 118 | At_3CGR | small | 2846 | 18 | no-parts | verse | 186 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 119 | At_3CGS | small | 13245 | 41 | done | prose | 219 | 2 | 1 | 23 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.06 · 0.6 min | `TOC-At_3CGS/toc-tree-anchored-At_3CGS.md` |
| 120 | At_3CGs_ | small | 4295 | 17 | done | verse | 273 | 2 | 1 | 7 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CGs_/toc-tree-anchored-At_3CGs_.md` |
| 121 | At_3CGT | small | 740 | 5 | no-parts | prose | 29 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 122 | At_3CGt_ | small | 3017 | 15 | done | prose | 105 | 1 | 1 | 3 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CGt_/toc-tree-anchored-At_3CGt_.md` |
| 123 | At_3CGU | small | 2338 | 9 | no-parts | prose | 47 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 124 | At_3CGu_ | small | 4149 | 32 | done | prose | 68 | 1 | 1 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CGu_/toc-tree-anchored-At_3CGu_.md` |
| 125 | At_3CGV | small | 14308 | 45 | done | prose | 161 | 2 | 3 | 17 | 0 | 9 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 0.5 min | `TOC-At_3CGV/toc-tree-anchored-At_3CGV.md` |
| 126 | At_3CGv_ | medium | 75339 | 358 | done | prose | 348 | 13 | 1 | 37 | 0→0 | 1 accepted (1.6.5 title from the enumeration) | Claude redo: 1 part (14 children) + II. preamble; repair dropped 7 listed-but-not-taken-up nodes (Gemini tree kept as TOC-At_3CGv_.gemini) | Claude agents (redo) | `TOC-At_3CGv_/toc-tree-anchored-At_3CGv_.md` |
| 127 | At_3CGW | small | 6906 | 30 | done | prose | 112 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.4 min | `TOC-At_3CGW/toc-tree-anchored-At_3CGW.md` |
| 128 | At_3CGX | small | 3442 | 15 | done | prose | 73 | 1 | 1 | 7 | 1→1→1 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.41 · 9.7 min | `TOC-At_3CGX/toc-tree-anchored-At_3CGX.md` |
| 129 | At_3CGx_ | small | 4784 | 34 | no-parts | verse | 284 | 3 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 130 | At_3CGY | small | 3873 | 17 | done | prose | 71 | 1 | 13 | 13 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.4 min | `TOC-At_3CGY/toc-tree-anchored-At_3CGY.md` |
| 131 | At_3CGy_ | small | 9773 | 38 | done | verse | 610 | 5 | 3 | 7 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.3 min | `TOC-At_3CGy_/toc-tree-anchored-At_3CGy_.md` |
| 132 | At_3CGZ | small | 3268 | 17 | no-parts | prose | 41 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 133 | At_3CH0 | small | 2151 | 8 | no-parts | verse | 140 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 134 | At_3CH1 | small | 4045 | 24 | done | verse | 236 | 2 | 2 | 2 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CH1/toc-tree-anchored-At_3CH1.md` |
| 135 | At_3CH2 | small | 4052 | 19 | no-parts | verse | 257 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 136 | At_3CH3 | small | 7228 | 44 | no-parts | prose | 158 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 137 | At_3CH4 | small | 5058 | 29 | done | prose | 181 | 2 | 1 | 21 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 0.7 min | `TOC-At_3CH4/toc-tree-anchored-At_3CH4.md` |
| 138 | At_3CH5 | small | 14020 | 88 | done | verse | 808 | 7 | 1 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 0.3 min | `TOC-At_3CH5/toc-tree-anchored-At_3CH5.md` |
| 139 | At_3CH6 | small | 2002 | 16 | no-parts | verse | 112 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 140 | At_3CH7 | small | 3664 | 18 | done | verse | 226 | 2 | 1 | 7 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 1.0 min | `TOC-At_3CH7/toc-tree-anchored-At_3CH7.md` |
| 141 | At_3CH8 | small | 9598 | 51 | done | prose | 231 | 2 | 3 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 0.7 min | `TOC-At_3CH8/toc-tree-anchored-At_3CH8.md` |
| 142 | At_3CH9 | small | 4125 | 25 | done | prose | 99 | 1 | 3 | 17 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.4 min | `TOC-At_3CH9/toc-tree-anchored-At_3CH9.md` |
| 143 | At_3CHA | small | 18911 | 104 | done | prose | 524 | 4 | 1 | 29 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.07 · 0.5 min | `TOC-At_3CHA/toc-tree-anchored-At_3CHA.md` |
| 144 | At_3CHa_ | small | 3287 | 19 | done | verse | 185 | 2 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CHa_/toc-tree-anchored-At_3CHa_.md` |
| 145 | At_3CHB | small | 3247 | 16 | done | verse | 210 | 2 | 1 | 5 | 1→0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CHB/toc-tree-anchored-At_3CHB.md` |
| 146 | At_3CHb_ | small | 1507 | 9 | no-parts | prose | 27 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 147 | At_3CHC | small | 12438 | 48 | done | prose | 166 | 2 | 5 | 5 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.4 min | `TOC-At_3CHC/toc-tree-anchored-At_3CHC.md` |
| 148 | At_3CHc_ | small | 4776 | 24 | done | verse | 256 | 2 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CHc_/toc-tree-anchored-At_3CHc_.md` |
| 149 | At_3CHD | small | 3552 | 8 | no-parts | prose | 40 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 150 | At_3CHd_ | small | 2728 | 22 | no-parts | prose | 58 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 151 | At_3CHE | small | 1932 | 19 | no-parts | prose | 39 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 152 | At_3CHe_ | small | 1305 | 7 | no-parts | prose | 25 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 153 | At_3CHF | small | 2147 | 18 | done | prose | 58 | 1 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CHF/toc-tree-anchored-At_3CHF.md` |
| 154 | At_3CHf_ | small | 10799 | 44 | done | verse | 652 | 6 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.3 min | `TOC-At_3CHf_/toc-tree-anchored-At_3CHf_.md` |
| 155 | At_3CHG | small | 2538 | 17 | no-parts | prose | 59 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 156 | At_3CHg_ | small | 3314 | 30 | no-parts | prose | 74 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 157 | At_3CHH | small | 19806 | 111 | done | prose | 357 | 3 | 8 | 13 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.06 · 0.4 min | `TOC-At_3CHH/toc-tree-anchored-At_3CHH.md` |
| 158 | At_3CHh_ | small | 4459 | 25 | done | verse | 253 | 2 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CHh_/toc-tree-anchored-At_3CHh_.md` |
| 159 | At_3CHI | small | 6404 | 39 | no-parts | verse | 383 | 3 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 160 | At_3CHi_ | small | 1463 | 13 | done | prose | 31 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CHi_/toc-tree-anchored-At_3CHi_.md` |
| 161 | At_3CHJ | small | 1322 | 9 | no-parts | verse | 85 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 162 | At_3CHj_ | small | 6480 | 48 | done | prose | 254 | 2 | 3 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CHj_/toc-tree-anchored-At_3CHj_.md` |
| 163 | At_3CHK | large | 798440 | 4302 | done | prose | 15662 | 126 | 29 | 29 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash medium · $3.62 · 21.5 min | `TOC-At_3CHK/toc-tree-anchored-At_3CHK.md` |
| 164 | At_3CHk_ | small | 8423 | 56 | done | prose | 126 | 1 | 2 | 18 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.5 min | `TOC-At_3CHk_/toc-tree-anchored-At_3CHk_.md` |
| 165 | At_3CHL | medium | 65963 | 330 | done | verse | 3958 | 32 | 9 | 9 | 1→0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.28 · 1.2 min | `TOC-At_3CHL/toc-tree-anchored-At_3CHL.md` |
| 166 | At_3CHl_ | small | 8468 | 52 | done | prose | 134 | 1 | 3 | 14 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.6 min | `TOC-At_3CHl_/toc-tree-anchored-At_3CHl_.md` |
| 167 | At_3CHM | small | 4634 | 35 | done | verse | 281 | 3 | 4 | 6 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.2 min | `TOC-At_3CHM/toc-tree-anchored-At_3CHM.md` |
| 168 | At_3CHm_ | small | 9226 | 59 | done | prose | 145 | 1 | 1 | 10 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.5 min | `TOC-At_3CHm_/toc-tree-anchored-At_3CHm_.md` |
| 169 | At_3CHN | small | 3291 | 21 | no-parts | prose | 67 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 170 | At_3CHn_ | small | 20404 | 150 | done | verse | 736 | 6 | 11 | 11 | 0 | 9 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.07 · 0.4 min | `TOC-At_3CHn_/toc-tree-anchored-At_3CHn_.md` |
| 171 | At_3CHO | small | 5051 | 31 | no-parts | prose | 71 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 172 | At_3CHo_ | small | 2053 | 12 | no-parts | verse | 134 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 173 | At_3CHP | small | 5662 | 43 | no-parts | prose | 103 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 174 | At_3CHp_ | small | 2670 | 14 | done | verse | 110 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CHp_/toc-tree-anchored-At_3CHp_.md` |
| 175 | At_3CHQ | small | 4899 | 29 | done | prose | 75 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CHQ/toc-tree-anchored-At_3CHQ.md` |
| 176 | At_3CHq_ | small | 2652 | 17 | done | verse | 155 | 2 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CHq_/toc-tree-anchored-At_3CHq_.md` |
| 177 | At_3CHR | small | 5329 | 34 | done | prose | 76 | 1 | 5 | 5 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CHR/toc-tree-anchored-At_3CHR.md` |
| 178 | At_3CHr_ | small | 2475 | 10 | done | verse | 150 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CHr_/toc-tree-anchored-At_3CHr_.md` |
| 179 | At_3CHS | small | 1796 | 13 | no-parts | prose | 27 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 180 | At_3CHs_ | small | 2612 | 13 | done | verse | 157 | 2 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CHs_/toc-tree-anchored-At_3CHs_.md` |
| 181 | At_3CHT | small | 1813 | 14 | no-parts | prose | 36 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 182 | At_3CHt_ | small | 2622 | 15 | done | verse | 153 | 2 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CHt_/toc-tree-anchored-At_3CHt_.md` |
| 183 | At_3CHU | small | 1465 | 10 | no-parts | prose | 36 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 184 | At_3CHu_ | small | 2491 | 11 | done | verse | 153 | 2 | 4 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-At_3CHu_/toc-tree-anchored-At_3CHu_.md` |
| 185 | At_3CHV | small | 3567 | 34 | done | prose | 60 | 1 | 3 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CHV/toc-tree-anchored-At_3CHV.md` |
| 186 | At_3CHv_ | small | 2672 | 15 | done | verse | 145 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CHv_/toc-tree-anchored-At_3CHv_.md` |
| 187 | At_3CHW | small | 1085 | 6 | no-parts | prose | 24 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 188 | At_3CHw_ | small | 2209 | 10 | done | verse | 138 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.1 min | `TOC-At_3CHw_/toc-tree-anchored-At_3CHw_.md` |
| 189 | At_3CHX | small | 3377 | 19 | no-parts | prose | 141 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 190 | At_3CHY | small | 1232 | 15 | no-parts | prose | 33 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 191 | At_3CHy_ | small | 4963 | 34 | done | verse | 300 | 3 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CHy_/toc-tree-anchored-At_3CHy_.md` |
| 192 | At_3CHZ | small | 2119 | 19 | no-parts | prose | 47 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 193 | At_3CHz_ | small | 2934 | 15 | no-parts | prose | 55 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 194 | At_3CI0 | small | 2575 | 18 | no-parts | prose | 40 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 195 | At_3CI1 | small | 2799 | 16 | no-parts | prose | 50 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 196 | At_3CI2 | small | 3028 | 20 | no-parts | prose | 44 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 197 | At_3CI3 | small | 3479 | 25 | done | prose | 53 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CI3/toc-tree-anchored-At_3CI3.md` |
| 198 | At_3CI4 | small | 5541 | 32 | no-parts | prose | 108 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 199 | At_3CI5 | small | 4964 | 24 | no-parts | prose | 88 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 200 | At_3CI6 | small | 2909 | 15 | no-parts | prose | 59 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 201 | At_3CI7 | small | 15587 | 103 | done | prose | 291 | 3 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.3 min | `TOC-At_3CI7/toc-tree-anchored-At_3CI7.md` |
| 202 | At_3CI8 | small | 4911 | 21 | done | prose | 167 | 2 | 1 | 5 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-At_3CI8/toc-tree-anchored-At_3CI8.md` |
| 203 | At_3CI9 | small | 1427 | 8 | done | prose | 36 | 1 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-At_3CI9/toc-tree-anchored-At_3CI9.md` |
| 204 | At_3CIA | small | 4221 | 33 | no-parts | prose | 91 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 205 | Bh_3CCH | medium | 114973 | 663 | done | prose | 3209 | 26 | 7 | 40 | 3→0 | 5 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.41 · 1.2 min | `TOC-Bh_3CCH/toc-tree-anchored-Bh_3CCH.md` |
| 206 | Bh_3CCI | medium | 143031 | 819 | done | verse | 8843 | 71 | 11 | 11 | 0 | 4 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.49 · 1.9 min | `TOC-Bh_3CCI/toc-tree-anchored-Bh_3CCI.md` |
| 207 | Bh_3CCJ | small | 2080 | 14 | done | verse | 130 | 1 | 2 | 10 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-Bh_3CCJ/toc-tree-anchored-Bh_3CCJ.md` |
| 208 | Bh_3CCK | medium | 30737 | 204 | done | prose | 736 | 6 | 3 | 71 | 0 | 18 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.16 · 1.2 min | `TOC-Bh_3CCK/toc-tree-anchored-Bh_3CCK.md` |
| 209 | Bh_3CCO | small | 2080 | 14 | done | verse | 128 | 1 | 2 | 10 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.5 min | `TOC-Bh_3CCO/toc-tree-anchored-Bh_3CCO.md` |
| 210 | Ch_3CCc_ | medium | 52346 | 75 | done | verse | 2707 | 22 | 10 | 10 | 0 | 5 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.20 · 1.2 min | `TOC-Ch_3CCc_/toc-tree-anchored-Ch_3CCc_.md` |
| 211 | Ch_3CCf_ | small | 3416 | 28 | done | verse | 200 | 2 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-Ch_3CCf_/toc-tree-anchored-Ch_3CCf_.md` |
| 212 | Ch_3CCP | small | 1606 | 9 | no-parts | verse | 101 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 213 | Ch_3CCR | medium | 32293 | 165 | done | prose | 815 | 7 | 4 | 11 | 0 | 7 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.10 · 0.5 min | `TOC-Ch_3CCR/toc-tree-anchored-Ch_3CCR.md` |
| 214 | Ch_3CCS | small | 5532 | 36 | done | prose | 156 | 2 | 5 | 5 | 1→0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 0.9 min | `TOC-Ch_3CCS/toc-tree-anchored-Ch_3CCS.md` |
| 215 | Ch_3CCU | small | 447 | 15 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 216 | Ch_3CCV | small | 7054 | 29 | done | verse | 317 | 3 | 3 | 3 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.2 min | `TOC-Ch_3CCV/toc-tree-anchored-Ch_3CCV.md` |
| 217 | Ch_3CCX | medium | 98834 | 438 | done | prose | 2010 | 16 | 3 | 56 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.36 · 1.5 min | `TOC-Ch_3CCX/toc-tree-anchored-Ch_3CCX.md` |
| 218 | Ch_3CCZ | small | 9207 | 41 | no-parts | verse | 593 | 5 | 0 | 0 | 0 | 0 flags | pass 1 found candidates, pass 3 kept none as a part (tree empty) | 3.8-flash low · $0.04 · 0.5 min |  |
| 219 | Dh_3CEy_ | small | 2748 | 12 | no-parts | verse | 120 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 220 | Dh_3CF0 | small | 6361 | 37 | no-parts | prose | 53 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 221 | Dh_3CF1 | small | 1227 | 6 | no-parts | verse | 90 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 222 | Dh_3CF2 | medium | 80633 | 489 | done | prose | 394 | 18 | 13 | 13 | 0→0 | 3 accepted closing-line titles | Claude redo: flat tree, 13 rite sections + II. preamble (Gemini tree kept as TOC-Dh_3CF2.gemini) | Claude agents (redo) | `TOC-Dh_3CF2/toc-tree-anchored-Dh_3CF2.md` |
| 223 | Dh_3CF3 | small | 8492 | 57 | no-parts | prose | 56 | 2 | 0 | 0 |  |  | Claude redo: one untitled candidate dropped as content in pass 3 (Gemini tree kept as TOC-Dh_3CF3.gemini) | Claude agents (redo) |  |
| 224 | Dh_3CF5 | large | 213273 | 1216 | done | verse | 11776 | 95 | 4 | 4 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash medium · $1.22 · 10.1 min | `TOC-Dh_3CF5/toc-tree-anchored-Dh_3CF5.md` |
| 225 | Dh_3CF6 | large | 320533 | 2177 | done | prose | 7409 | 60 | 1 | 5 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash medium · $1.69 · 14.2 min | `TOC-Dh_3CF6/toc-tree-anchored-Dh_3CF6.md` |
| 226 | Dh_3CF7 | medium | 30574 | 232 | done | prose | 558 | 5 | 3 | 23 | 0 | 4 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.10 · 0.7 min | `TOC-Dh_3CF7/toc-tree-anchored-Dh_3CF7.md` |
| 227 | Dh_3CF8 | medium | 76128 | 555 | done | prose | 1309 | 11 | 1 | 10 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.18 · 0.5 min | `TOC-Dh_3CF8/toc-tree-anchored-Dh_3CF8.md` |
| 228 | Dh_3CF9 | small | 3844 | 24 | no-parts | verse | 242 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 229 | Dh_3CFC | medium | 120052 | 690 | done | prose | 1774 | 14 | 1 | 20 | 0 | 4 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.29 · 0.8 min | `TOC-Dh_3CFC/toc-tree-anchored-Dh_3CFC.md` |
| 230 | Dh_3CFD | small | 14597 | 89 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 231 | Di_3CEe_ | medium | 42180 | 158 | done | verse | 2622 | 21 | 13 | 13 | 0 | 12 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.15 · 0.7 min | `TOC-Di_3CEe_/toc-tree-anchored-Di_3CEe_.md` |
| 232 | Di_3CEi_ | small | 483 | 18 | no-parts | prose | 24 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 233 | Di_3CEj_ | small | 642 | 13 | no-parts | prose | 19 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 234 | Di_3CEk_ | small | 3254 | 22 | no-parts | verse | 194 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 235 | Di_3CEl_ | small | 8745 | 48 | done | verse | 528 | 5 | 3 | 6 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.3 min | `TOC-Di_3CEl_/toc-tree-anchored-Di_3CEl_.md` |
| 236 | Di_3CEn_ | small | 2059 | 13 | no-parts | verse | 113 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 237 | Di_3CEq_ | medium | 30663 | 58 | done | verse | 2078 | 17 | 6 | 6 | 3→0 | 4 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.17 · 1.1 min | `TOC-Di_3CEq_/toc-tree-anchored-Di_3CEq_.md` |
| 238 | Di_3CEs_ | small | 1577 | 16 | no-parts | verse | 94 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 239 | Di_3CEu_ | small | 4510 | 22 | no-parts | verse | 302 | 3 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 240 | Di_3CEv_ | small | 12700 | 21 | done | prose | 243 | 2 | 6 | 34 | 0 | 6 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.06 · 0.6 min | `TOC-Di_3CEv_/toc-tree-anchored-Di_3CEv_.md` |
| 241 | Di_3CEw_ | small | 16346 | 100 | done | prose | 312 | 3 | 8 | 43 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.09 · 0.8 min | `TOC-Di_3CEw_/toc-tree-anchored-Di_3CEw_.md` |
| 242 | Di_3CEx_ | small | 2873 | 23 | done | verse | 127 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Di_3CEx_/toc-tree-anchored-Di_3CEx_.md` |
| 243 | Gu_3CFS | large | 390432 | 2820 | done | prose | 14838 | 119 | 40 | 40 | 0 | 36 flags | Gemini run — review the top-level parts; 4 node(s) without an anchor ([[?]]) | 3.8-flash medium · $3.35 · 14.7 min | `TOC-Gu_3CFS/toc-tree-anchored-Gu_3CFS.md` |
| 244 | Gu_3CFT | large | 611367 | 3000 | done | prose | 8494 | 68 | 16 | 133 | 0 | 13 flags | Gemini run — review the top-level parts | 3.8-flash medium · $4.41 · 42.7 min | `TOC-Gu_3CFT/toc-tree-anchored-Gu_3CFT.md` |
| 245 | Ha_3CFF | large | 645047 | 1699 | done | prose | 8517 | 68 | 63 | 63 | 0 | 19 flags | Gemini run — review the top-level parts | 3.8-flash medium · $2.88 · 24.5 min | `TOC-Ha_3CFF/toc-tree-anchored-Ha_3CFF.md` |
| 246 | Ha_3CFG | large | 711330 | 1965 | done | prose | 10303 | 83 | 19 | 22 | 0 | 19 flags | Gemini run — review the top-level parts | 3.8-flash medium · $3.38 · 30.8 min | `TOC-Ha_3CFG/toc-tree-anchored-Ha_3CFG.md` |
| 247 | Ha_3CFH | large | 749999 | 2298 | done | prose | 9694 | 78 | 14 | 102 | 0 | 71 flags | Gemini run — review the top-level parts | 3.8-flash medium · $3.79 · 38.6 min | `TOC-Ha_3CFH/toc-tree-anchored-Ha_3CFH.md` |
| 248 | Ha_3CFI | large | 670280 | 2206 | done | prose | 7792 | 63 | 3 | 51 | 0 | 33 flags | Gemini run — review the top-level parts | 3.8-flash medium · $3.72 · 38.5 min | `TOC-Ha_3CFI/toc-tree-anchored-Ha_3CFI.md` |
| 249 | Ha_3CFJ | large | 667778 | 2134 | done | prose | 8136 | 65 | 18 | 18 | 0 | 10 flags | Gemini run — review the top-level parts | 3.8-flash medium · $5.02 · 0.6 min | `TOC-Ha_3CFJ/toc-tree-anchored-Ha_3CFJ.md` |
| 250 | Ha_3CFO | medium | 88486 | 647 | done | prose | 2881 | 23 | 8 | 8 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.28 · 0.7 min | `TOC-Ha_3CFO/toc-tree-anchored-Ha_3CFO.md` |
| 251 | Ka_3CDK | large | 420177 | 1670 | no-parts | prose | 6304 | 51 | 0 | 0 |  |  |  | 3.8-flash medium · $0.61 · 2.9 min |  |
| 252 | Ka_3CDL | medium | 103971 | 433 | no-parts | verse | 6805 | 55 | 0 | 0 | 0 | 0 flags | pass 1 found candidates, pass 3 kept none as a part (tree empty) | 3.8-flash low · $0.35 · 1.4 min |  |
| 253 | Ka_3CDM | medium | 68150 | 238 | done | prose | 1060 | 9 | 3 | 12 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.16 · 0.6 min | `TOC-Ka_3CDM/toc-tree-anchored-Ka_3CDM.md` |
| 254 | Ka_3CDN | small | 8828 | 9 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 255 | Ka_3CDO | medium | 77906 | 362 | done | prose | 1424 | 12 | 3 | 35 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.22 · 0.9 min | `TOC-Ka_3CDO/toc-tree-anchored-Ka_3CDO.md` |
| 256 | Ka_3CDP | medium | 59827 | 414 | done | prose | 996 | 8 | 1 | 13 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.15 · 0.5 min | `TOC-Ka_3CDP/toc-tree-anchored-Ka_3CDP.md` |
| 257 | Ka_3CDQ | medium | 55523 | 364 | done | prose | 926 | 8 | 1 | 5 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.14 · 0.4 min | `TOC-Ka_3CDQ/toc-tree-anchored-Ka_3CDQ.md` |
| 258 | Ka_3CDR | small | 7722 | 64 | done | prose | 180 | 2 | 3 | 5 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.2 min | `TOC-Ka_3CDR/toc-tree-anchored-Ka_3CDR.md` |
| 259 | Ka_3CDV | small | 5789 | 19 | done | verse | 279 | 3 | 8 | 8 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-Ka_3CDV/toc-tree-anchored-Ka_3CDV.md` |
| 260 | Ka_3CDW | small | 17283 | 125 | no-parts | verse | 813 | 7 | 0 | 0 |  |  |  | 3.8-flash low · $0.02 · 0.1 min |  |
| 261 | Ka_3CDY | small | 2079 | 21 | no-parts | verse | 119 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 262 | Na_3C92 | small | 15593 | 112 | no-parts | verse | 924 | 8 | 0 | 0 |  |  |  | 3.8-flash low · $0.02 · 0.1 min |  |
| 263 | Na_3C93 | small | 5048 | 49 | no-parts | verse | 263 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 264 | Na_3C94 | small | 4291 | 33 | no-parts | verse | 255 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 265 | Na_3C95 | small | 1330 | 14 | no-parts | verse | 82 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 266 | Na_3C96 | small | 2043 | 19 | no-parts | verse | 125 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 267 | Na_3C97 | small | 1830 | 14 | no-parts | verse | 62 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 268 | Na_3C99 | small | 3114 | 11 | no-parts | verse | 117 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 269 | Na_3C9A | small | 3022 | 12 | no-parts | verse | 196 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 270 | Na_3C9a_ | medium | 33578 | 165 | done | verse | 2035 | 17 | 12 | 16 | 0 | 5 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.14 · 0.7 min | `TOC-Na_3C9a_/toc-tree-anchored-Na_3C9a_.md` |
| 271 | Na_3C9B | small | 7426 | 26 | no-parts | verse | 490 | 4 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 272 | Na_3C9b_ | small | 16698 | 90 | done | prose | 392 | 3 | 2 | 5 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.09 · 1.2 min | `TOC-Na_3C9b_/toc-tree-anchored-Na_3C9b_.md` |
| 273 | Na_3C9C | small | 2676 | 12 | no-parts | verse | 176 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 274 | Na_3C9c_ | medium | 80546 | 462 | done | prose | 2634 | 21 | 20 | 36 | 0 | 14 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.28 · 1.1 min | `TOC-Na_3C9c_/toc-tree-anchored-Na_3C9c_.md` |
| 275 | Na_3C9D | small | 1251 | 8 | no-parts | verse | 86 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 276 | Na_3C9d_ | small | 10605 | 54 | done | verse | 660 | 6 | 5 | 14 | 3→3→3 | 8 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.07 · 0.5 min | `TOC-Na_3C9d_/toc-tree-anchored-Na_3C9d_.md` |
| 277 | Na_3C9E | small | 1707 | 7 | no-parts | verse | 107 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 278 | Na_3C9e_ | small | 16220 | 70 | no-parts | verse | 452 | 2 | 0 | 0 |  |  | finished with Claude: pass 3 kept neither implicit candidate (བྱང་ཆུབ་སེམས་ཀྱི་བསྒོམ་པ་, རྣམ་ཤེས་རང་བཞིན་) — empty tree |  |  |
| 279 | Na_3C9F | small | 2933 | 10 | no-parts | verse | 158 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 280 | Na_3C9G | small | 1998 | 12 | no-parts | verse | 108 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 281 | Na_3C9H | small | 1865 | 13 | no-parts | verse | 93 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 282 | Na_3C9h_ | medium | 36958 | 43 | done | verse | 2391 | 19 | 5 | 16 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.15 · 0.7 min | `TOC-Na_3C9h_/toc-tree-anchored-Na_3C9h_.md` |
| 283 | Na_3C9I | small | 2748 | 17 | no-parts | verse | 141 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 284 | Na_3C9i_ | small | 23874 | 165 | done | verse | 1421 | 12 | 11 | 28 | 1→0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.20 · 2.6 min | `TOC-Na_3C9i_/toc-tree-anchored-Na_3C9i_.md` |
| 285 | Na_3C9J | small | 1406 | 6 | no-parts | verse | 96 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 286 | Na_3C9j_ | small | 15828 | 118 | done | prose | 612 | 5 | 13 | 16 | 1→0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.10 · 1.0 min | `TOC-Na_3C9j_/toc-tree-anchored-Na_3C9j_.md` |
| 287 | Na_3C9K | small | 2552 | 13 | no-parts | verse | 147 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 288 | Na_3C9k_ | medium | 81487 | 547 | done | verse | 4795 | 39 | 16 | 96 | 2→0 | 21 flags | Gemini run — review the top-level parts; 4 node(s) without an anchor ([[?]]) | 3.8-flash low · $0.42 · 1.9 min | `TOC-Na_3C9k_/toc-tree-anchored-Na_3C9k_.md` |
| 289 | Na_3C9M | small | 4771 | 24 | no-parts | verse | 306 | 3 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 290 | Na_3C9N | small | 15579 | 82 | done | prose | 352 | 3 | 1 | 8 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 0.2 min | `TOC-Na_3C9N/toc-tree-anchored-Na_3C9N.md` |
| 291 | Na_3C9n_ | medium | 34047 | 236 | done | prose | 1812 | 15 | 26 | 45 | 0 | 21 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.16 · 0.9 min | `TOC-Na_3C9n_/toc-tree-anchored-Na_3C9n_.md` |
| 292 | Na_3C9O | small | 3394 | 27 | done | verse | 73 | 2 | 4 | 7 | 0→0 | 0 issues | Claude redo: 4 topic-header parts; nodes 1 and 2 share the anchor text (lines 9 and 103) — check node 2 lands on the second (Gemini tree kept as TOC-Na_3C9O.gemini) | Claude agents (redo) | `TOC-Na_3C9O/toc-tree-anchored-Na_3C9O.md` |
| 293 | Na_3C9o_ | small | 5741 | 42 | done | verse | 338 | 3 | 6 | 7 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-Na_3C9o_/toc-tree-anchored-Na_3C9o_.md` |
| 294 | Na_3C9P | small | 7044 | 52 | done | verse | 422 | 4 | 3 | 3 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.2 min | `TOC-Na_3C9P/toc-tree-anchored-Na_3C9P.md` |
| 295 | Na_3C9p_ | small | 4062 | 31 | done | verse | 277 | 3 | 2 | 5 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-Na_3C9p_/toc-tree-anchored-Na_3C9p_.md` |
| 296 | Na_3C9Q | small | 10977 | 68 | done | prose | 220 | 2 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 0.8 min | `TOC-Na_3C9Q/toc-tree-anchored-Na_3C9Q.md` |
| 297 | Na_3C9R | small | 3236 | 32 | done | verse | 188 | 2 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.4 min | `TOC-Na_3C9R/toc-tree-anchored-Na_3C9R.md` |
| 298 | Na_3C9r_ | small | 9109 | 52 | done | prose | 200 | 2 | 4 | 4 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.3 min | `TOC-Na_3C9r_/toc-tree-anchored-Na_3C9r_.md` |
| 299 | Na_3C9S | small | 1996 | 13 | done | verse | 127 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Na_3C9S/toc-tree-anchored-Na_3C9S.md` |
| 300 | Na_3C9s_ | small | 962 | 15 | no-parts | verse | 25 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 301 | Na_3C9T | small | 2312 | 24 | done | prose | 62 | 1 | 3 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Na_3C9T/toc-tree-anchored-Na_3C9T.md` |
| 302 | Na_3C9t_ | small | 2609 | 12 | no-parts | verse | 172 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 303 | Na_3C9U | small | 1700 | 16 | no-parts | prose | 44 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 304 | Na_3C9u_ | small | 17645 | 135 | done | prose | 487 | 4 | 15 | 15 | 0 | 8 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.07 · 0.4 min | `TOC-Na_3C9u_/toc-tree-anchored-Na_3C9u_.md` |
| 305 | Na_3C9V | small | 4057 | 28 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 306 | Na_3C9v_ | small | 710 | 6 | no-parts | verse | 42 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 307 | Na_3C9W | small | 5535 | 64 | no-parts | verse | 150 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 308 | Na_3C9w_ | small | 1418 | 8 | no-parts | verse | 94 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 309 | Na_3C9X | small | 5093 | 48 | no-parts | verse | 140 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 310 | Na_3C9x_ | small | 482 | 13 | no-parts | prose | 19 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 311 | Na_3C9Y | small | 3685 | 21 | no-parts | verse | 103 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 312 | Na_3C9y_ | small | 665 | 16 | no-parts | prose | 22 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 313 | Na_3C9z_ | small | 6153 | 8 | done | verse | 422 | 4 | 4 | 4 | 1→0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.3 min | `TOC-Na_3C9z_/toc-tree-anchored-Na_3C9z_.md` |
| 314 | Na_3CA0 | small | 632 | 6 | done | verse | 42 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Na_3CA0/toc-tree-anchored-Na_3CA0.md` |
| 315 | Na_3CA1 | small | 364 | 15 | no-parts | verse | 27 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 316 | Na_3CA2 | small | 1049 | 8 | done | prose | 56 | 1 | 1 | 9 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Na_3CA2/toc-tree-anchored-Na_3CA2.md` |
| 317 | Na_3CA3 | small | 7369 | 44 | no-parts | verse | 370 | 3 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 318 | Na_3CA5 | small | 3949 | 32 | done | prose | 92 | 1 | 4 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Na_3CA5/toc-tree-anchored-Na_3CA5.md` |
| 319 | Na_3CA6 | medium | 32512 | 195 | done | prose | 655 | 6 | 10 | 14 | 0 | 5 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.10 · 0.5 min | `TOC-Na_3CA6/toc-tree-anchored-Na_3CA6.md` |
| 320 | Na_3CA7 | small | 5326 | 32 | no-parts | verse | 300 | 3 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 321 | Na_3CA8 | small | 2168 | 17 | no-parts | prose | 47 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 322 | Na_3CA9 | small | 3089 | 27 | done | verse | 169 | 2 | 6 | 6 | 0 | 5 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-Na_3CA9/toc-tree-anchored-Na_3CA9.md` |
| 323 | Na_3CAA | small | 1554 | 13 | no-parts | verse | 67 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 324 | Na_3CAB | small | 1297 | 14 | done | verse | 76 | 1 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Na_3CAB/toc-tree-anchored-Na_3CAB.md` |
| 325 | Na_3CAb_ | small | 5834 | 16 | done | verse | 382 | 3 | 3 | 3 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.2 min | `TOC-Na_3CAb_/toc-tree-anchored-Na_3CAb_.md` |
| 326 | Na_3CAC | small | 2235 | 21 | done | verse | 131 | 1 | 3 | 3 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Na_3CAC/toc-tree-anchored-Na_3CAC.md` |
| 327 | Na_3CAc_ | small | 1655 | 8 | no-parts | prose | 62 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 328 | Na_3CAD | small | 19186 | 139 | done | prose | 651 | 6 | 8 | 26 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.08 · 0.5 min | `TOC-Na_3CAD/toc-tree-anchored-Na_3CAD.md` |
| 329 | Na_3CAd_ | small | 3416 | 10 | no-parts | verse | 154 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 330 | Na_3CAE | small | 6760 | 34 | done | verse | 424 | 4 | 3 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.2 min | `TOC-Na_3CAE/toc-tree-anchored-Na_3CAE.md` |
| 331 | Na_3CAe_ | small | 2105 | 13 | no-parts | prose | 39 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 332 | Na_3CAF | medium | 33079 | 162 | done | prose | 708 | 6 | 4 | 9 | 0 | 4 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.09 · 0.3 min | `TOC-Na_3CAF/toc-tree-anchored-Na_3CAF.md` |
| 333 | Na_3CAf_ | small | 3029 | 11 | no-parts | prose | 53 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 334 | Na_3CAG | small | 7211 | 40 | done | prose | 118 | 1 | 9 | 9 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-Na_3CAG/toc-tree-anchored-Na_3CAG.md` |
| 335 | Na_3CAg_ | small | 25471 | 73 | done | verse | 1635 | 13 | 2 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.10 · 0.4 min | `TOC-Na_3CAg_/toc-tree-anchored-Na_3CAg_.md` |
| 336 | Na_3CAH | small | 1786 | 13 | no-parts | prose | 45 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 337 | Na_3CAh_ | small | 5971 | 28 | done | prose | 196 | 2 | 3 | 5 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.2 min | `TOC-Na_3CAh_/toc-tree-anchored-Na_3CAh_.md` |
| 338 | Na_3CAI | small | 1318 | 12 | no-parts | prose | 42 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 339 | Na_3CAi_ | small | 6114 | 15 | done | verse | 437 | 4 | 4 | 4 | 1→0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-Na_3CAi_/toc-tree-anchored-Na_3CAi_.md` |
| 340 | Na_3CAJ | small | 1757 | 16 | no-parts | verse | 96 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 341 | Na_3CAK | small | 1148 | 12 | no-parts | prose | 32 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 342 | Na_3CAk_ | medium | 68677 | 461 | done | verse | 4081 | 33 | 27 | 27 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.26 · 1.1 min | `TOC-Na_3CAk_/toc-tree-anchored-Na_3CAk_.md` |
| 343 | Na_3CAL | small | 1546 | 16 | no-parts | prose | 48 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 344 | Na_3CAl_ | small | 9290 | 58 | no-parts | verse | 558 | 5 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 345 | Na_3CAM | small | 7557 | 87 | no-parts | prose | 179 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 346 | Na_3CAm_ | small | 5677 | 35 | no-parts | prose | 221 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.2 min |  |
| 347 | Na_3CAN | small | 10841 | 131 | done | prose | 349 | 3 | 2 | 6 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.3 min | `TOC-Na_3CAN/toc-tree-anchored-Na_3CAN.md` |
| 348 | Na_3CAn_ | small | 11455 | 77 | no-parts | verse | 663 | 6 | 0 | 0 |  |  |  | 3.8-flash low · $0.02 · 0.1 min |  |
| 349 | Na_3CAO | small | 9886 | 83 | done | prose | 313 | 3 | 2 | 2 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.4 min | `TOC-Na_3CAO/toc-tree-anchored-Na_3CAO.md` |
| 350 | Na_3CAo_ | small | 10985 | 80 | no-parts | verse | 664 | 6 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 351 | Na_3CAP | small | 3108 | 17 | done | prose | 95 | 1 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Na_3CAP/toc-tree-anchored-Na_3CAP.md` |
| 352 | Na_3CAQ | small | 7244 | 74 | done | prose | 166 | 2 | 6 | 6 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 1.0 min | `TOC-Na_3CAQ/toc-tree-anchored-Na_3CAQ.md` |
| 353 | Na_3CAR | small | 6498 | 30 | done | prose | 106 | 1 | 2 | 5 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.06 · 1.2 min | `TOC-Na_3CAR/toc-tree-anchored-Na_3CAR.md` |
| 354 | Na_3CAS | small | 4057 | 26 | no-parts | prose | 74 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 355 | Na_3CAT | small | 21284 | 140 | done | verse | 1054 | 9 | 4 | 10 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.07 · 0.3 min | `TOC-Na_3CAT/toc-tree-anchored-Na_3CAT.md` |
| 356 | Na_3CAU | small | 1802 | 9 | done | verse | 109 | 1 | 3 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Na_3CAU/toc-tree-anchored-Na_3CAU.md` |
| 357 | Na_3CAu_ | small | 3326 | 16 | no-parts | verse | 214 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 358 | Na_3CAV | medium | 124020 | 731 | done | prose | 2237 | 41 | 27 | 31 | 0→0 | 20 accepted title-not-near flags | Claude redo: 27 topic-header parts + II. homage preamble; only node 1 has children (Gemini tree kept as TOC-Na_3CAV.gemini) | Claude agents (redo) | `TOC-Na_3CAV/toc-tree-anchored-Na_3CAV.md` |
| 359 | Na_3CAv_ | small | 710 | 5 | no-parts | prose | 57 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 360 | Na_3CAW | small | 9954 | 36 | done | prose | 150 | 1 | 8 | 8 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.4 min | `TOC-Na_3CAW/toc-tree-anchored-Na_3CAW.md` |
| 361 | Na_3CAX | medium | 30125 | 81 | done | verse | 1947 | 16 | 13 | 18 | 1→0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.14 · 0.7 min | `TOC-Na_3CAX/toc-tree-anchored-Na_3CAX.md` |
| 362 | Na_3CAx_ | small | 1396 | 11 | no-parts | verse | 85 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 363 | Na_3CAY | small | 8790 | 34 | done | prose | 270 | 2 | 6 | 6 | 0 | 6 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-Na_3CAY/toc-tree-anchored-Na_3CAY.md` |
| 364 | Na_3CAZ | small | 2851 | 11 | done | prose | 33 | 1 | 3 | 6 | 1→1→0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-Na_3CAZ/toc-tree-anchored-Na_3CAZ.md` |
| 365 | Na_3CAz_ | small | 4134 | 27 | done | prose | 143 | 1 | 4 | 4 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-Na_3CAz_/toc-tree-anchored-Na_3CAz_.md` |
| 366 | Na_3CB0 | small | 3167 | 23 | no-parts | verse | 169 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.0 min |  |
| 367 | Na_3CB1 | small | 3073 | 27 | done | verse | 195 | 2 | 5 | 5 | 0 | 5 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-Na_3CB1/toc-tree-anchored-Na_3CB1.md` |
| 368 | Na_3CB2 | small | 5935 | 34 | done | verse | 368 | 3 | 2 | 12 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-Na_3CB2/toc-tree-anchored-Na_3CB2.md` |
| 369 | Na_3CB3 | small | 7829 | 39 | no-parts | verse | 513 | 4 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 370 | Na_3CB4 | large | 268837 | 1483 | done | prose | 3761 | 30 | 17 | 17 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash medium · $1.38 · 14.5 min | `TOC-Na_3CB4/toc-tree-anchored-Na_3CB4.md` |
| 371 | Na_3CB5 | small | 7453 | 35 | done | prose | 139 | 1 | 6 | 6 | 0 | 4 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-Na_3CB5/toc-tree-anchored-Na_3CB5.md` |
| 372 | Na_3CB6 | small | 10687 | 77 | done | verse | 643 | 5 | 1 | 5 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.3 min | `TOC-Na_3CB6/toc-tree-anchored-Na_3CB6.md` |
| 373 | Na_3CBB | medium | 47793 | 376 | done | verse | 2258 | 18 | 15 | 24 | 0 | 8 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.17 · 0.7 min | `TOC-Na_3CBB/toc-tree-anchored-Na_3CBB.md` |
| 374 | Na_3CBC | small | 1759 | 8 | done | prose | 36 | 1 | 3 | 3 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Na_3CBC/toc-tree-anchored-Na_3CBC.md` |
| 375 | Na_3CBD | medium | 74311 | 491 | done | verse | 4449 | 36 | 5 | 17 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.26 · 1.0 min | `TOC-Na_3CBD/toc-tree-anchored-Na_3CBD.md` |
| 376 | Na_3CBE | small | 5816 | 41 | no-parts | verse | 309 | 3 | 0 | 0 | 0 | 0 flags | pass 1 found candidates, pass 3 kept none as a part (tree empty) | 3.8-flash low · $0.02 · 0.2 min |  |
| 377 | Na_3CBF | small | 3035 | 24 | no-parts | verse | 142 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 378 | Na_3CBG | small | 2634 | 15 | no-parts | verse | 167 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 379 | Na_3CBH | small | 24344 | 188 | no-parts | verse | 1160 | 10 | 0 | 0 | 0 | 0 flags | pass 1 found candidates, pass 3 kept none as a part (tree empty) | 3.8-flash low · $0.08 · 0.3 min |  |
| 380 | Na_3CBI | small | 29938 | 311 | earlier-run |  |  |  |  |  |  |  | anchored tree from an earlier run |  |  |
| 381 | Na_3CBJ | small | 15332 | 153 | done | verse | 547 | 5 | 2 | 2 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.06 · 0.6 min | `TOC-Na_3CBJ/toc-tree-anchored-Na_3CBJ.md` |
| 382 | Na_3CBK | small | 5199 | 44 | done | prose | 188 | 2 | 5 | 5 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-Na_3CBK/toc-tree-anchored-Na_3CBK.md` |
| 383 | Na_3CBL | small | 641 | 3 | no-parts | prose | 39 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 384 | Na_3CBM | small | 2779 | 36 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 385 | Na_3CBN | small | 29421 | 63 | done | prose | 1125 | 9 | 13 | 13 | 0 | 12 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.10 · 0.5 min | `TOC-Na_3CBN/toc-tree-anchored-Na_3CBN.md` |
| 386 | Na_3CBO | small | 19417 | 210 | no-parts | verse | 1016 | 8 | 0 | 0 |  |  |  | 3.8-flash low · $0.03 · 0.1 min |  |
| 387 | Na_3CBP | medium | 42113 | 324 | no-parts | verse | 2374 | 19 | 0 | 0 |  |  |  | 3.8-flash low · $0.05 · 0.2 min |  |
| 388 | Na_3CBQ | small | 18954 | 214 | no-parts | verse | 950 | 8 | 0 | 0 |  |  |  | 3.8-flash low · $0.02 · 0.1 min |  |
| 389 | Na_3CBR | small | 2658 | 9 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 390 | Na_3CBS | small | 3681 | 29 | no-parts | verse | 169 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 391 | Na_3CBT | small | 2107 | 16 | no-parts | verse | 104 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 392 | Na_3CBU | small | 3607 | 26 | no-parts | verse | 208 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.0 min |  |
| 393 | Na_3CBV | small | 3295 | 5 | no-parts | verse | 183 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 394 | Na_3CBW | small | 4732 | 33 | done | verse | 199 | 2 | 3 | 3 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.2 min | `TOC-Na_3CBW/toc-tree-anchored-Na_3CBW.md` |
| 395 | Na_3CBX | small | 7261 | 53 | no-parts | verse | 301 | 3 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 396 | Na_3CBY | small | 25482 | 127 | done | prose | 537 | 5 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.07 · 0.5 min | `TOC-Na_3CBY/toc-tree-anchored-Na_3CBY.md` |
| 397 | Na_3CBZ | small | 5617 | 21 | no-parts | prose | 79 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 398 | Sh_3CCh_ | small | 450 | 15 | no-parts | prose | 15 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 399 | Sh_3CCi_ | small | 579 | 16 | no-parts | prose | 18 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 400 | Sh_3CCj_ | small | 1047 | 9 | no-parts | verse | 59 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 401 | Sh_3CCl_ | small | 861 | 5 | no-parts | verse | 51 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 402 | Sh_3CCm_ | medium | 148453 | 1012 | done | verse | 8226 | 66 | 10 | 10 | 0 | 4 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.48 · 1.5 min | `TOC-Sh_3CCm_/toc-tree-anchored-Sh_3CCm_.md` |
| 403 | Sh_3CCn_ | small | 2711 | 13 | no-parts | prose | 83 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.0 min |  |
| 404 | Sh_3CCp_ | small | 22167 | 163 | done | prose | 353 | 3 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 0.2 min | `TOC-Sh_3CCp_/toc-tree-anchored-Sh_3CCp_.md` |
| 405 | Sh_3CCq_ | small | 11429 | 77 | no-parts | verse | 617 | 5 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 406 | Sh_3CCr_ | small | 4149 | 24 | done | verse | 254 | 2 | 1 | 10 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.05 · 0.9 min | `TOC-Sh_3CCr_/toc-tree-anchored-Sh_3CCr_.md` |
| 407 | Sh_3CCs_ | large | 262957 | 1702 | done | prose | 5622 | 45 | 5 | 5 | 0 | 4 flags | Gemini run — review the top-level parts | 3.8-flash medium · $1.27 · 8.3 min | `TOC-Sh_3CCs_/toc-tree-anchored-Sh_3CCs_.md` |
| 408 | Sh_3CCt_ | large | 528968 | 3306 | done | prose | 12942 | 104 | 7 | 30 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash medium · $2.75 · 20.2 min | `TOC-Sh_3CCt_/toc-tree-anchored-Sh_3CCt_.md` |
| 409 | Sh_3CCu_ | small | 16694 | 35 | done | prose | 227 | 2 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.2 min | `TOC-Sh_3CCu_/toc-tree-anchored-Sh_3CCu_.md` |
| 410 | Sh_3CCv_ | small | 1217 | 5 | no-parts | verse | 63 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 411 | Sh_3CCx_ | small | 2876 | 9 | no-parts | verse | 159 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 412 | Sh_3CCy_ | small | 2904 | 16 | done | prose | 92 | 1 | 5 | 5 | 0 | 5 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Sh_3CCy_/toc-tree-anchored-Sh_3CCy_.md` |
| 413 | Sh_3CCz_ | small | 3061 | 17 | done | prose | 97 | 1 | 3 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.01 · 0.2 min | `TOC-Sh_3CCz_/toc-tree-anchored-Sh_3CCz_.md` |
| 414 | Sh_3CD1 | medium | 41236 | 42 | done | prose | 436 | 4 | 4 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.09 · 0.3 min | `TOC-Sh_3CD1/toc-tree-anchored-Sh_3CD1.md` |
| 415 | Sh_3CD2 | medium | 54599 | 212 | done | prose | 795 | 15 | 30 | 30 | 0→0 | 0 issues | Claude redo: flat tree of 30 rite steps + II. preamble; nodes 2/3 and 5/6 are near-identical paired headers — check (Gemini tree kept as TOC-Sh_3CD2.gemini) | Claude agents (redo) | `TOC-Sh_3CD2/toc-tree-anchored-Sh_3CD2.md` |
| 416 | Sh_3CD3 | medium | 103089 | 435 | done | prose | 1065 | 9 | 1 | 16 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.26 · 0.9 min | `TOC-Sh_3CD3/toc-tree-anchored-Sh_3CD3.md` |
| 417 | Sh_3CD4 | medium | 75968 | 345 | done | prose | 1145 | 9 | 10 | 10 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.17 · 0.5 min | `TOC-Sh_3CD4/toc-tree-anchored-Sh_3CD4.md` |
| 418 | Sh_3CD5 | small | 21691 | 93 | done | prose | 281 | 3 | 6 | 6 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.06 · 0.3 min | `TOC-Sh_3CD5/toc-tree-anchored-Sh_3CD5.md` |
| 419 | Sh_3CD6 | medium | 79043 | 71 | done | prose | 725 | 6 | 4 | 16 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.19 · 0.7 min | `TOC-Sh_3CD6/toc-tree-anchored-Sh_3CD6.md` |
| 420 | Sh_3CD7 | medium | 59490 | 73 | done | prose | 621 | 5 | 4 | 4 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.13 · 0.3 min | `TOC-Sh_3CD7/toc-tree-anchored-Sh_3CD7.md` |
| 421 | Sh_3CD8 | medium | 46408 | 218 | done | prose | 1242 | 10 | 1 | 1 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.11 · 0.3 min | `TOC-Sh_3CD8/toc-tree-anchored-Sh_3CD8.md` |
| 422 | Sh_3CDA | small | 13213 | 65 | no-parts | verse | 849 | 7 | 0 | 0 |  |  |  | 3.8-flash low · $0.02 · 0.1 min |  |
| 423 | Sh_3CDE | large | 521520 | 3183 | done | verse | 31717 | 254 | 30 | 30 | 0 | 9 flags | Gemini run — review the top-level parts | 3.8-flash medium · $3.20 · 22.5 min | `TOC-Sh_3CDE/toc-tree-anchored-Sh_3CDE.md` |
| 424 | Sh_3CDF | small | 10621 | 23 | done | verse | 699 | 6 | 5 | 5 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.04 · 0.3 min | `TOC-Sh_3CDF/toc-tree-anchored-Sh_3CDF.md` |
| 425 | Sh_3CFZ | medium | 48327 | 371 | done | verse | 2265 | 18 | 15 | 15 | 0 | 8 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.20 · 1.8 min | `TOC-Sh_3CFZ/toc-tree-anchored-Sh_3CFZ.md` |
| 426 | Va_3CE0 | small | 569 | 6 | no-parts | prose | 44 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 427 | Va_3CEa_ | small | 2984 | 18 | done | verse | 188 | 2 | 2 | 9 | 0 | 3 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.02 · 0.3 min | `TOC-Va_3CEa_/toc-tree-anchored-Va_3CEa_.md` |
| 428 | Va_3CEb_ | small | 2425 | 22 | earlier-run |  |  |  |  |  |  |  | no tree (earlier run: no parts found) |  |  |
| 429 | Va_3CEc_ | small | 6688 | 53 | done | verse | 399 | 3 | 1 | 3 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.2 min | `TOC-Va_3CEc_/toc-tree-anchored-Va_3CEc_.md` |
| 430 | Va_3CEd_ | small | 1873 | 22 | no-parts | verse | 100 | 1 | 0 | 0 |  |  |  | 3.8-flash low · $0.00 · 0.1 min |  |
| 431 | Va_3CEL | small | 4237 | 20 | done | verse | 276 | 3 | 2 | 8 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-Va_3CEL/toc-tree-anchored-Va_3CEL.md` |
| 432 | Va_3CEM | small | 3303 | 19 | no-parts | verse | 211 | 2 | 0 | 0 |  |  |  | 3.8-flash low · $0.01 · 0.1 min |  |
| 433 | Va_3CEO | small | 5876 | 38 | done | verse | 360 | 3 | 3 | 16 | 0 | 8 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.3 min | `TOC-Va_3CEO/toc-tree-anchored-Va_3CEO.md` |
| 434 | Va_3CEP | small | 19751 | 99 | done | prose | 721 | 6 | 3 | 40 | 0 | 30 flags | Gemini run — review the top-level parts; 23 node(s) without an anchor ([[?]]) | 3.8-flash low · $0.09 · 0.6 min | `TOC-Va_3CEP/toc-tree-anchored-Va_3CEP.md` |
| 435 | Va_3CEQ | medium | 42280 | 240 | no-parts | prose | 468 | 4 | 0 | 0 |  |  |  | 3.8-flash low · $0.03 · 0.1 min |  |
| 436 | Va_3CER | large | 421757 | 2485 | done | prose | 8749 | 70 | 2 | 20 | 0 | 4 flags | Gemini run — review the top-level parts | 3.8-flash medium · $3.05 · 15.3 min | `TOC-Va_3CER/toc-tree-anchored-Va_3CER.md` |
| 437 | Va_3CES | medium | 40296 | 198 | done | prose | 728 | 6 | 3 | 3 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.09 · 0.3 min | `TOC-Va_3CES/toc-tree-anchored-Va_3CES.md` |
| 438 | Va_3CET | small | 4474 | 27 | earlier-run |  |  |  |  |  |  |  | anchored tree from an earlier run |  |  |
| 439 | Va_3CEX | medium | 85088 | 451 | done | verse | 5227 | 42 | 8 | 8 | 0 | 0 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.31 · 1.2 min | `TOC-Va_3CEX/toc-tree-anchored-Va_3CEX.md` |
| 440 | Va_3CEY | small | 4377 | 30 | done | verse | 250 | 2 | 1 | 4 | 0 | 2 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.03 · 0.5 min | `TOC-Va_3CEY/toc-tree-anchored-Va_3CEY.md` |
| 441 | Ch_3CCd_ | medium | 61146 | 267 | done | verse | 2875 | 23 | 10 | 10 | 0 | 1 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.20 · 0.8 min | `TOC-Ch_3CCd_/toc-tree-anchored-Ch_3CCd_.md` |
| 442 | Di_3CEp_ | medium | 33174 | 37 | done | verse | 2159 | 18 | 6 | 6 | 0 | 6 flags | Gemini run — review the top-level parts | 3.8-flash low · $0.12 · 0.6 min | `TOC-Di_3CEp_/toc-tree-anchored-Di_3CEp_.md` |
