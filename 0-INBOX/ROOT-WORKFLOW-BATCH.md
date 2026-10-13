# Root-text workflow batch — segmentation + TOC ingest + grouping + block IDs

Gemini (gemini-3.8-flash) runs the rest of the workflow for every root text whose TOC
extraction is finished (see `0-INBOX/ROOT-TOC-BATCH.md`). How to run: `0-INBOX/temp/root-toc/README.md`.

Updated 2026-10-13 · 442 texts · done 442 · failed 0 ·
running 0 · **to do 0**

| Where | Path |
|---|---|
| Finished files (with block IDs) | `0-INBOX/processed/root-gemini/<id>.md` |
| Working folder per text | `0-INBOX/temp/root-final/<id>/` (prepared.md, group-in.md, groups-*.json, final-*.md) |
| Tree used for the headings | `0-INBOX/temp/TOC-<id>/toc-tree-anchored-<id>.md` |
| Log per text | `0-INBOX/temp/root-toc/logs/workflow-<id>.log` |

`toc` tree = the text's parts became headings · no parts = `## གཞུང་དངོས། ^1-0` only ·
`headings` = body headings placed / not placed (a not-placed heading must be put in by hand) ·
`blocks` = stanzas / paragraphs. Review the files before they replace anything in
`0-INBOX/processed/root/`.

| # | id | size | status | toc | headings | blocks | run (cost · time) | note | output |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Ar_3CBa_ | medium | done | tree | 0 not placed | 462 | low · $0.24 · 3.4 min |  | `processed/root-gemini/Ar_3CBa_.md` |
| 2 | Ar_3CBc_ | medium | done | tree | 0 not placed | 375 | low · $0.33 · 2.3 min |  | `processed/root-gemini/Ar_3CBc_.md` |
| 3 | Ar_3CBf_ | small | done | no parts | — | 9 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CBf_.md` |
| 4 | Ar_3CBg_ | medium | done | tree | 0 not placed | 115 | low · $0.03 · 0.3 min |  | `processed/root-gemini/Ar_3CBg_.md` |
| 5 | Ar_3CBh_ | medium | done | tree | 0 not placed | 125 | low · $0.03 · 0.3 min |  | `processed/root-gemini/Ar_3CBh_.md` |
| 6 | Ar_3CBi_ | small | done | no parts | — | 132 | low · $0.04 · 0.6 min |  | `processed/root-gemini/Ar_3CBi_.md` |
| 7 | Ar_3CBk_ | small | done | tree | 0 not placed | 42 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Ar_3CBk_.md` |
| 8 | Ar_3CBl_ | small | done | tree | 0 not placed | 47 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Ar_3CBl_.md` |
| 9 | Ar_3CBm_ | small | done | tree | 0 not placed | 74 | low · $0.02 · 0.4 min |  | `processed/root-gemini/Ar_3CBm_.md` |
| 10 | Ar_3CBn_ | small | done | no parts | — | 14 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CBn_.md` |
| 11 | Ar_3CBo_ | small | done | no parts | — | 102 | low · $0.02 · 0.2 min |  | `processed/root-gemini/Ar_3CBo_.md` |
| 12 | Ar_3CBp_ | small | done | tree | 0 not placed | 44 | low · $0.02 · 0.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Ar_3CBp_.md` |
| 13 | Ar_3CBq_ | small | done | tree | 0 not placed | 45 | low · $0.02 · 0.2 min |  | `processed/root-gemini/Ar_3CBq_.md` |
| 14 | Ar_3CBr_ | small | done | no parts | — | 18 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CBr_.md` |
| 15 | Ar_3CBs_ | small | done | tree | 0 not placed | 27 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ar_3CBs_.md` |
| 16 | Ar_3CBt_ | small | done | no parts | — | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CBt_.md` |
| 17 | Ar_3CBu_ | small | done | no parts | — | 20 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ar_3CBu_.md` |
| 18 | Ar_3CBv_ | small | done | no parts | — | 5 | low · $0.01 · 0.4 min |  | `processed/root-gemini/Ar_3CBv_.md` |
| 19 | Ar_3CBw_ | small | done | tree | 0 not placed | 25 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ar_3CBw_.md` |
| 20 | Ar_3CBx_ | small | done | tree | 0 not placed | 16 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Ar_3CBx_.md` |
| 21 | Ar_3CBy_ | small | done | tree | 0 not placed | 9 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CBy_.md` |
| 22 | Ar_3CBz_ | small | done | no parts | — | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CBz_.md` |
| 23 | Ar_3CC1 | medium | done | tree | 0 not placed | 423 | low · $0.50 · 3.9 min | grouping fell back to medium for part(s) 2, 3 | `processed/root-gemini/Ar_3CC1.md` |
| 24 | Ar_3CC2 | small | done | tree | 0 not placed | 47 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Ar_3CC2.md` |
| 25 | Ar_3CC3 | small | done | no parts | — | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CC3.md` |
| 26 | Ar_3CC5 | small | done | tree | 0 not placed | 16 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ar_3CC5.md` |
| 27 | Ar_3CC6 | small | done | tree | 0 not placed | 37 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ar_3CC6.md` |
| 28 | Ar_3CC7 | small | done | no parts | — | 40 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Ar_3CC7.md` |
| 29 | Ar_3CC8 | small | done | no parts | — | 15 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CC8.md` |
| 30 | Ar_3CC9 | small | done | no parts | — | 10 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CC9.md` |
| 31 | Ar_3CCA | small | done | no parts | — | 14 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CCA.md` |
| 32 | Ar_3CCB | small | done | no parts | — | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CCB.md` |
| 33 | As_3CDc_ | small | done | no parts | — | 19 | low · $0.00 · 0.1 min |  | `processed/root-gemini/As_3CDc_.md` |
| 34 | As_3CDd_ | small | done | no parts | — | 11 | low · $0.01 · 0.1 min |  | `processed/root-gemini/As_3CDd_.md` |
| 35 | As_3CDe_ | small | done | no parts | — | 10 | low · $0.02 · 0.5 min |  | `processed/root-gemini/As_3CDe_.md` |
| 36 | As_3CDr_ | medium | done | tree | 0 not placed | 198 | low · $0.09 · 0.8 min |  | `processed/root-gemini/As_3CDr_.md` |
| 37 | As_3CDs_ | medium | done | tree | 0 not placed | 218 | low · $0.17 · 0.4 min |  | `processed/root-gemini/As_3CDs_.md` |
| 38 | As_3CDt_ | medium | done | tree | 0 not placed | 131 | low · $0.14 · 0.3 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/As_3CDt_.md` |
| 39 | As_3CDu_ | medium | done | tree | 0 not placed | 428 | low · $0.37 · 1.8 min | 8 anchor(s) repaired (footnote marker / ༌) | `processed/root-gemini/As_3CDu_.md` |
| 40 | As_3CDw_ | small | done | tree | 0 not placed | 94 | low · $0.02 · 0.2 min |  | `processed/root-gemini/As_3CDw_.md` |
| 41 | At_3CFb_ | small | done | tree | 0 not placed | 108 | low · $0.02 · 0.3 min |  | `processed/root-gemini/At_3CFb_.md` |
| 42 | At_3CFc_ | small | done | tree | 0 not placed | 29 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CFc_.md` |
| 43 | At_3CFd_ | medium | done | tree | 0 not placed | 205 | low · $0.04 · 0.3 min |  | `processed/root-gemini/At_3CFd_.md` |
| 44 | At_3CFe_ | small | done | tree | 0 not placed | 23 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CFe_.md` |
| 45 | At_3CFf_ | small | done | tree | 0 not placed | 24 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CFf_.md` |
| 46 | At_3CFg_ | small | done | tree | 0 not placed | 5 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CFg_.md` |
| 47 | At_3CFh_ | small | done | tree | — | 28 | low · $0.02 · 0.1 min |  | `processed/root-gemini/At_3CFh_.md` |
| 48 | At_3CFj_ | small | done | no parts | — | 31 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CFj_.md` |
| 49 | At_3CFl_ | small | done | no parts | — | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CFl_.md` |
| 50 | At_3CFm_ | small | done | tree | — | 14 | low · $0.02 · 0.1 min |  | `processed/root-gemini/At_3CFm_.md` |
| 51 | At_3CFn_ | small | done | no parts | — | 11 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CFn_.md` |
| 52 | At_3CFo_ | small | done | no parts | — | 13 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CFo_.md` |
| 53 | At_3CFp_ | small | done | no parts | — | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CFp_.md` |
| 54 | At_3CFq_ | small | done | no parts | — | 4 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CFq_.md` |
| 55 | At_3CFr_ | small | done | no parts | — | 7 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CFr_.md` |
| 56 | At_3CFs_ | small | done | tree | 0 not placed | 13 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CFs_.md` |
| 57 | At_3CFt_ | medium | done | tree | 0 not placed | 133 | low · $0.03 · 0.3 min |  | `processed/root-gemini/At_3CFt_.md` |
| 58 | At_3CFu_ | small | done | tree | 0 not placed | 25 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CFu_.md` |
| 59 | At_3CFv_ | small | done | no parts | — | 19 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CFv_.md` |
| 60 | At_3CFw_ | small | done | tree | 0 not placed | 13 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CFw_.md` |
| 61 | At_3CFx_ | small | done | no parts | — | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CFx_.md` |
| 62 | At_3CFy_ | small | done | no parts | — | 13 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CFy_.md` |
| 63 | At_3CFz_ | small | done | tree | 0 not placed | 13 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CFz_.md` |
| 64 | At_3CG0 | small | done | no parts | — | 28 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CG0.md` |
| 65 | At_3CG1 | small | done | tree | 0 not placed | 135 | low · $0.02 · 0.3 min |  | `processed/root-gemini/At_3CG1.md` |
| 66 | At_3CG2 | small | done | no parts | — | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CG2.md` |
| 67 | At_3CG3 | small | done | tree | 0 not placed | 10 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CG3.md` |
| 68 | At_3CG4 | small | done | no parts | — | 8 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CG4.md` |
| 69 | At_3CG5 | small | done | tree | 0 not placed | 85 | low · $0.04 · 0.7 min |  | `processed/root-gemini/At_3CG5.md` |
| 70 | At_3CG6 | small | done | tree | 0 not placed | 20 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CG6.md` |
| 71 | At_3CG7 | small | done | no parts | — | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CG7.md` |
| 72 | At_3CG8 | small | done | tree | 0 not placed | 10 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CG8.md` |
| 73 | At_3CG9 | small | done | tree | 0 not placed | 23 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CG9.md` |
| 74 | At_3CGA | small | done | tree | 0 not placed | 34 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGA.md` |
| 75 | At_3CGa_ | small | done | tree | 0 not placed | 12 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGa_.md` |
| 76 | At_3CGB | small | done | tree | 0 not placed | 21 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGB.md` |
| 77 | At_3CGb_ | small | done | tree | 0 not placed | 10 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGb_.md` |
| 78 | At_3CGC | small | done | no parts | — | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGC.md` |
| 79 | At_3CGc_ | small | done | tree | 0 not placed | 9 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGc_.md` |
| 80 | At_3CGD | small | done | no parts | — | 10 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGD.md` |
| 81 | At_3CGd_ | small | done | tree | 0 not placed | 10 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGd_.md` |
| 82 | At_3CGE | small | done | tree | 0 not placed | 19 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGE.md` |
| 83 | At_3CGe_ | small | done | tree | 0 not placed | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGe_.md` |
| 84 | At_3CGF | small | done | tree | 0 not placed | 14 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGF.md` |
| 85 | At_3CGf_ | small | done | tree | 0 not placed | 8 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGf_.md` |
| 86 | At_3CGG | small | done | no parts | — | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGG.md` |
| 87 | At_3CGg_ | small | done | tree | 0 not placed | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGg_.md` |
| 88 | At_3CGH | small | done | no parts | — | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGH.md` |
| 89 | At_3CGh_ | small | done | tree | 0 not placed | 9 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGh_.md` |
| 90 | At_3CGI | small | done | no parts | — | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGI.md` |
| 91 | At_3CGi_ | small | done | tree | — | 8 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGi_.md` |
| 92 | At_3CGJ | small | done | tree | 0 not placed | 23 | low · $0.01 · 0.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/At_3CGJ.md` |
| 93 | At_3CGj_ | small | done | no parts | — | 31 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CGj_.md` |
| 94 | At_3CGK | small | done | tree | 0 not placed | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGK.md` |
| 95 | At_3CGk_ | small | done | tree | — | 20 | low · $0.02 · 0.1 min |  | `processed/root-gemini/At_3CGk_.md` |
| 96 | At_3CGL | small | done | no parts | — | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGL.md` |
| 97 | At_3CGl_ | small | done | tree | 0 not placed | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGl_.md` |
| 98 | At_3CGM | small | done | tree | 0 not placed | 15 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGM.md` |
| 99 | At_3CGm_ | small | done | tree | 0 not placed | 17 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGm_.md` |
| 100 | At_3CGN | small | done | tree | 0 not placed | 79 | low · $0.02 · 0.2 min |  | `processed/root-gemini/At_3CGN.md` |
| 101 | At_3CGn_ | small | done | tree | 0 not placed | 14 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGn_.md` |
| 102 | At_3CGO | small | done | no parts | — | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGO.md` |
| 103 | At_3CGo_ | small | done | no parts | — | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGo_.md` |
| 104 | At_3CGP | medium | done | tree | 0 not placed | 73 | low · $0.02 · 0.1 min |  | `processed/root-gemini/At_3CGP.md` |
| 105 | At_3CGp_ | small | done | no parts | — | 8 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGp_.md` |
| 106 | At_3CGQ | small | done | tree | 0 not placed | 11 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGQ.md` |
| 107 | At_3CGq_ | medium | done | tree | 0 not placed | 161 | low · $0.04 · 0.5 min |  | `processed/root-gemini/At_3CGq_.md` |
| 108 | At_3CGR | small | done | no parts | — | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGR.md` |
| 109 | At_3CGS | small | done | tree | 0 not placed | 31 | low · $0.02 · 0.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/At_3CGS.md` |
| 110 | At_3CGs_ | small | done | tree | 0 not placed | 27 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGs_.md` |
| 111 | At_3CGT | small | done | no parts | — | 2 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGT.md` |
| 112 | At_3CGt_ | small | done | tree | 0 not placed | 14 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGt_.md` |
| 113 | At_3CGU | small | done | no parts | — | 5 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGU.md` |
| 114 | At_3CGu_ | small | done | tree | 0 not placed | 8 | low · $0.01 · 0.4 min |  | `processed/root-gemini/At_3CGu_.md` |
| 115 | At_3CGV | small | done | tree | 0 not placed | 23 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGV.md` |
| 116 | At_3CGv_ | medium | done | tree | 0 not placed | 228 | low · $0.52 · 5.5 min | grouping fell back to medium for part(s) 1 | `processed/root-gemini/At_3CGv_.md` |
| 117 | At_3CGW | small | done | tree | 0 not placed | 12 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGW.md` |
| 118 | At_3CGX | small | done | tree | 0 not placed | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGX.md` |
| 119 | At_3CGx_ | small | done | no parts | — | 29 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGx_.md` |
| 120 | At_3CGY | small | done | tree | 0 not placed | 15 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CGY.md` |
| 121 | At_3CGy_ | small | done | tree | 0 not placed | 62 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CGy_.md` |
| 122 | At_3CGZ | small | done | no parts | — | 3 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CGZ.md` |
| 123 | At_3CH0 | small | done | no parts | — | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CH0.md` |
| 124 | At_3CH1 | small | done | tree | 0 not placed | 19 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CH1.md` |
| 125 | At_3CH2 | small | done | no parts | — | 43 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CH2.md` |
| 126 | At_3CH3 | small | done | no parts | — | 19 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CH3.md` |
| 127 | At_3CH4 | small | done | tree | 0 not placed | 28 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CH4.md` |
| 128 | At_3CH5 | small | done | tree | 0 not placed | 65 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CH5.md` |
| 129 | At_3CH6 | small | done | no parts | — | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CH6.md` |
| 130 | At_3CH7 | small | done | tree | 0 not placed | 23 | low · $0.01 · 0.1 min | 2 anchor(s) repaired (footnote marker / ༌) | `processed/root-gemini/At_3CH7.md` |
| 131 | At_3CH8 | small | done | tree | 0 not placed | 17 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CH8.md` |
| 132 | At_3CH9 | small | done | tree | 0 not placed | 15 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CH9.md` |
| 133 | At_3CHA | small | done | tree | 0 not placed | 65 | low · $0.02 · 0.2 min |  | `processed/root-gemini/At_3CHA.md` |
| 134 | At_3CHa_ | small | done | tree | 0 not placed | 16 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHa_.md` |
| 135 | At_3CHB | small | done | tree | 0 not placed | 21 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHB.md` |
| 136 | At_3CHb_ | small | done | no parts | — | 4 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CHb_.md` |
| 137 | At_3CHC | small | done | tree | 0 not placed | 27 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CHC.md` |
| 138 | At_3CHc_ | small | done | tree | 0 not placed | 25 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHc_.md` |
| 139 | At_3CHD | small | done | no parts | — | 2 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHD.md` |
| 140 | At_3CHd_ | small | done | no parts | — | 6 | low · $0.02 · 0.6 min |  | `processed/root-gemini/At_3CHd_.md` |
| 141 | At_3CHE | small | done | no parts | — | 3 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHE.md` |
| 142 | At_3CHe_ | small | done | no parts | — | 3 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CHe_.md` |
| 143 | At_3CHF | small | done | tree | 0 not placed | 10 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHF.md` |
| 144 | At_3CHf_ | small | done | tree | 0 not placed | 47 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CHf_.md` |
| 145 | At_3CHG | small | done | no parts | — | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHG.md` |
| 146 | At_3CHg_ | small | done | no parts | — | 3 | low · $0.01 · 0.3 min |  | `processed/root-gemini/At_3CHg_.md` |
| 147 | At_3CHH | small | done | tree | 0 not placed | 41 | low · $0.02 · 0.2 min |  | `processed/root-gemini/At_3CHH.md` |
| 148 | At_3CHh_ | small | done | tree | 0 not placed | 20 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHh_.md` |
| 149 | At_3CHI | small | done | no parts | — | 59 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CHI.md` |
| 150 | At_3CHi_ | small | done | tree | 0 not placed | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHi_.md` |
| 151 | At_3CHJ | small | done | no parts | — | 10 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHJ.md` |
| 152 | At_3CHj_ | small | done | tree | 0 not placed | 22 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHj_.md` |
| 153 | At_3CHk_ | small | done | tree | 0 not placed | 19 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHk_.md` |
| 154 | At_3CHL | medium | done | tree | 0 not placed | 416 | low · $0.07 · 0.9 min |  | `processed/root-gemini/At_3CHL.md` |
| 155 | At_3CHl_ | small | done | tree | 0 not placed | 17 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHl_.md` |
| 156 | At_3CHM | small | done | tree | 0 not placed | 21 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHM.md` |
| 157 | At_3CHm_ | small | done | tree | 0 not placed | 19 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHm_.md` |
| 158 | At_3CHN | small | done | no parts | — | 5 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHN.md` |
| 159 | At_3CHO | small | done | no parts | — | 14 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHO.md` |
| 160 | At_3CHo_ | small | done | no parts | — | 9 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHo_.md` |
| 161 | At_3CHP | small | done | no parts | — | 13 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHP.md` |
| 162 | At_3CHp_ | small | done | tree | 0 not placed | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHp_.md` |
| 163 | At_3CHQ | small | done | tree | 0 not placed | 15 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHQ.md` |
| 164 | At_3CHq_ | small | done | tree | 0 not placed | 14 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHq_.md` |
| 165 | At_3CHR | small | done | tree | 0 not placed | 12 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHR.md` |
| 166 | At_3CHr_ | small | done | tree | 0 not placed | 16 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHr_.md` |
| 167 | At_3CHS | small | done | no parts | — | 1 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CHS.md` |
| 168 | At_3CHs_ | small | done | tree | 0 not placed | 14 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHs_.md` |
| 169 | At_3CHT | small | done | no parts | — | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHT.md` |
| 170 | At_3CHt_ | small | done | tree | 0 not placed | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHt_.md` |
| 171 | At_3CHU | small | done | no parts | — | 4 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHU.md` |
| 172 | At_3CHu_ | small | done | tree | 0 not placed | 18 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHu_.md` |
| 173 | At_3CHV | small | done | tree | 0 not placed | 5 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHV.md` |
| 174 | At_3CHv_ | small | done | tree | 0 not placed | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHv_.md` |
| 175 | At_3CHW | small | done | no parts | — | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHW.md` |
| 176 | At_3CHw_ | small | done | tree | 0 not placed | 14 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHw_.md` |
| 177 | At_3CHX | small | done | no parts | — | 16 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CHX.md` |
| 178 | At_3CHY | small | done | no parts | — | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHY.md` |
| 179 | At_3CHy_ | small | done | tree | 0 not placed | 29 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CHy_.md` |
| 180 | At_3CHZ | small | done | no parts | — | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CHZ.md` |
| 181 | At_3CHz_ | small | done | no parts | — | 6 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CHz_.md` |
| 182 | At_3CI0 | small | done | no parts | — | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CI0.md` |
| 183 | At_3CI1 | small | done | no parts | — | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CI1.md` |
| 184 | At_3CI2 | small | done | no parts | — | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CI2.md` |
| 185 | At_3CI3 | small | done | tree | 0 not placed | 3 | low · $0.01 · 0.3 min |  | `processed/root-gemini/At_3CI3.md` |
| 186 | At_3CI4 | small | done | no parts | — | 8 | low · $0.02 · 0.4 min |  | `processed/root-gemini/At_3CI4.md` |
| 187 | At_3CI5 | small | done | no parts | — | 15 | low · $0.01 · 0.1 min |  | `processed/root-gemini/At_3CI5.md` |
| 188 | At_3CI6 | small | done | no parts | — | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CI6.md` |
| 189 | At_3CI7 | small | done | tree | 0 not placed | 34 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CI7.md` |
| 190 | At_3CI8 | small | done | tree | 0 not placed | 27 | low · $0.01 · 0.2 min |  | `processed/root-gemini/At_3CI8.md` |
| 191 | At_3CI9 | small | done | tree | 0 not placed | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/At_3CI9.md` |
| 192 | At_3CIA | small | done | no parts | — | 7 | low · $0.02 · 0.5 min |  | `processed/root-gemini/At_3CIA.md` |
| 193 | Bh_3CCH | medium | done | tree | 0 not placed | 486 | low · $0.62 · 10.8 min | grouping fell back to medium for part(s) 1, 2 | `processed/root-gemini/Bh_3CCH.md` |
| 194 | Bh_3CCI | medium | done | tree | 0 not placed | 948 | low · $1.43 · 12.0 min | grouping fell back to medium for part(s) 5, 6; 1 anchor(s) repaired (footnote marker / ༌) | `processed/root-gemini/Bh_3CCI.md` |
| 195 | Bh_3CCJ | small | done | tree | 0 not placed | 12 | low · $0.00 · 0.2 min |  | `processed/root-gemini/Bh_3CCJ.md` |
| 196 | Bh_3CCK | medium | done | tree | 0 not placed | 49 | low · $0.02 · 0.1 min |  | `processed/root-gemini/Bh_3CCK.md` |
| 197 | Bh_3CCO | small | done | tree | 0 not placed | 13 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Bh_3CCO.md` |
| 198 | Ch_3CCc_ | medium | done | tree | 0 not placed | 333 | low · $0.14 · 0.7 min |  | `processed/root-gemini/Ch_3CCc_.md` |
| 199 | Ch_3CCf_ | small | done | tree | 0 not placed | 16 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Ch_3CCf_.md` |
| 200 | Ch_3CCP | small | done | no parts | — | 9 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ch_3CCP.md` |
| 201 | Ch_3CCR | medium | done | tree | 0 not placed | 127 | low · $0.03 · 0.3 min |  | `processed/root-gemini/Ch_3CCR.md` |
| 202 | Ch_3CCS | small | done | tree | 0 not placed | 18 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ch_3CCS.md` |
| 203 | Ch_3CCU | small | done | no parts | — | 6 | low · $0.01 · 0.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Ch_3CCU.md` |
| 204 | Ch_3CCV | small | done | tree | 0 not placed | 25 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ch_3CCV.md` |
| 205 | Ch_3CCX | medium | done | tree | 0 not placed | 229 | low · $0.06 · 0.5 min |  | `processed/root-gemini/Ch_3CCX.md` |
| 206 | Ch_3CCZ | small | done | no parts | — | 68 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ch_3CCZ.md` |
| 207 | Dh_3CEy_ | small | done | no parts | — | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Dh_3CEy_.md` |
| 208 | Dh_3CF0 | small | done | no parts | — | 4 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Dh_3CF0.md` |
| 209 | Dh_3CF1 | small | done | no parts | — | 9 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Dh_3CF1.md` |
| 210 | Dh_3CF2 | medium | done | tree | 0 not placed | 247 | low · $0.22 · 0.8 min |  | `processed/root-gemini/Dh_3CF2.md` |
| 211 | Dh_3CF3 | small | done | tree | — | 19 | low · $0.02 · 0.1 min |  | `processed/root-gemini/Dh_3CF3.md` |
| 212 | Dh_3CF7 | medium | done | tree | 0 not placed | 53 | low · $0.04 · 0.4 min |  | `processed/root-gemini/Dh_3CF7.md` |
| 213 | Dh_3CF8 | medium | done | tree | 0 not placed | 144 | low · $0.04 · 0.3 min |  | `processed/root-gemini/Dh_3CF8.md` |
| 214 | Dh_3CF9 | small | done | no parts | — | 25 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Dh_3CF9.md` |
| 215 | Dh_3CFC | medium | done | tree | 0 not placed | 140 | low · $0.06 · 0.2 min |  | `processed/root-gemini/Dh_3CFC.md` |
| 216 | Dh_3CFD | small | done | no parts | — | 40 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Dh_3CFD.md` |
| 217 | Di_3CEe_ | medium | done | tree | 0 not placed | 282 | low · $0.04 · 0.5 min |  | `processed/root-gemini/Di_3CEe_.md` |
| 218 | Di_3CEi_ | small | done | no parts | — | 6 | low · $0.01 · 0.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Di_3CEi_.md` |
| 219 | Di_3CEj_ | small | done | no parts | — | 5 | low · $0.01 · 0.1 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Di_3CEj_.md` |
| 220 | Di_3CEk_ | small | done | no parts | — | 18 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Di_3CEk_.md` |
| 221 | Di_3CEl_ | small | done | tree | 0 not placed | 56 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Di_3CEl_.md` |
| 222 | Di_3CEn_ | small | done | no parts | — | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Di_3CEn_.md` |
| 223 | Di_3CEq_ | medium | done | tree | 0 not placed | 275 | low · $0.04 · 0.6 min |  | `processed/root-gemini/Di_3CEq_.md` |
| 224 | Di_3CEs_ | small | done | no parts | — | 8 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Di_3CEs_.md` |
| 225 | Di_3CEu_ | small | done | no parts | — | 33 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Di_3CEu_.md` |
| 226 | Di_3CEv_ | small | done | tree | 0 not placed | 26 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Di_3CEv_.md` |
| 227 | Di_3CEw_ | small | done | tree | 0 not placed | 47 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Di_3CEw_.md` |
| 228 | Di_3CEx_ | small | done | tree | 0 not placed | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Di_3CEx_.md` |
| 229 | Ha_3CFO | medium | done | tree | 0 not placed | 200 | low · $0.06 · 0.4 min |  | `processed/root-gemini/Ha_3CFO.md` |
| 230 | Ka_3CDL | medium | done | no parts | — | 744 | low · $0.15 · 2.7 min |  | `processed/root-gemini/Ka_3CDL.md` |
| 231 | Ka_3CDM | medium | done | tree | 0 not placed | 163 | low · $0.08 · 0.6 min |  | `processed/root-gemini/Ka_3CDM.md` |
| 232 | Ka_3CDN | small | done | no parts | — | 28 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ka_3CDN.md` |
| 233 | Ka_3CDO | medium | done | tree | 0 not placed | 151 | low · $0.14 · 0.3 min |  | `processed/root-gemini/Ka_3CDO.md` |
| 234 | Ka_3CDP | medium | done | tree | 0 not placed | 88 | low · $0.12 · 2.8 min |  | `processed/root-gemini/Ka_3CDP.md` |
| 235 | Ka_3CDQ | medium | done | tree | 0 not placed | 79 | low · $0.03 · 0.2 min |  | `processed/root-gemini/Ka_3CDQ.md` |
| 236 | Ka_3CDR | small | done | tree | 0 not placed | 21 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ka_3CDR.md` |
| 237 | Ka_3CDV | small | done | tree | 0 not placed | 29 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Ka_3CDV.md` |
| 238 | Ka_3CDW | small | done | no parts | — | 64 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Ka_3CDW.md` |
| 239 | Ka_3CDY | small | done | no parts | — | 17 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ka_3CDY.md` |
| 240 | Na_3C92 | small | done | no parts | — | 100 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3C92.md` |
| 241 | Na_3C93 | small | done | no parts | — | 25 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C93.md` |
| 242 | Na_3C94 | small | done | no parts | — | 26 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C94.md` |
| 243 | Na_3C95 | small | done | no parts | — | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C95.md` |
| 244 | Na_3C96 | small | done | no parts | — | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C96.md` |
| 245 | Na_3C97 | small | done | no parts | — | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C97.md` |
| 246 | Na_3C99 | small | done | no parts | — | 11 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3C99.md` |
| 247 | Na_3C9A | small | done | no parts | — | 21 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9A.md` |
| 248 | Na_3C9a_ | medium | done | tree | 0 not placed | 174 | low · $0.23 · 4.8 min | grouping fell back to medium for part(s) 1 | `processed/root-gemini/Na_3C9a_.md` |
| 249 | Na_3C9B | small | done | no parts | — | 54 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3C9B.md` |
| 250 | Na_3C9b_ | small | done | tree | 0 not placed | 59 | low · $0.02 · 0.3 min |  | `processed/root-gemini/Na_3C9b_.md` |
| 251 | Na_3C9C | small | done | no parts | — | 18 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9C.md` |
| 252 | Na_3C9c_ | medium | done | tree | 0 not placed | 237 | low · $0.15 · 1.4 min |  | `processed/root-gemini/Na_3C9c_.md` |
| 253 | Na_3C9D | small | done | no parts | — | 8 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9D.md` |
| 254 | Na_3C9d_ | small | done | tree | 0 not placed | 57 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3C9d_.md` |
| 255 | Na_3C9E | small | done | no parts | — | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9E.md` |
| 256 | Na_3C9F | small | done | no parts | — | 16 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9F.md` |
| 257 | Na_3C9G | small | done | no parts | — | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9G.md` |
| 258 | Na_3C9H | small | done | no parts | — | 9 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9H.md` |
| 259 | Na_3C9h_ | medium | done | tree | 0 not placed | 293 | low · $0.25 · 4.2 min | grouping fell back to medium for part(s) 2 | `processed/root-gemini/Na_3C9h_.md` |
| 260 | Na_3C9I | small | done | no parts | — | 14 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9I.md` |
| 261 | Na_3C9i_ | small | done | tree | 0 not placed | 91 | low · $0.07 · 0.9 min |  | `processed/root-gemini/Na_3C9i_.md` |
| 262 | Na_3C9J | small | done | no parts | — | 8 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9J.md` |
| 263 | Na_3C9j_ | small | done | tree | 0 not placed | 84 | low · $0.09 · 1.6 min | 1 anchor(s) repaired (footnote marker / ༌) | `processed/root-gemini/Na_3C9j_.md` |
| 264 | Na_3C9K | small | done | no parts | — | 15 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9K.md` |
| 265 | Na_3C9k_ | medium | done | tree | 0 not placed | 371 | low · $0.08 · 1.2 min |  | `processed/root-gemini/Na_3C9k_.md` |
| 266 | Na_3C9M | small | done | no parts | — | 32 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3C9M.md` |
| 267 | Na_3C9N | small | done | tree | 0 not placed | 35 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3C9N.md` |
| 268 | Na_3C9n_ | medium | done | tree | 0 not placed | 195 | low · $0.19 · 3.3 min | grouping fell back to medium for part(s) 1 | `processed/root-gemini/Na_3C9n_.md` |
| 269 | Na_3C9O | small | done | tree | 0 not placed | 16 | low · $0.02 · 0.1 min |  | `processed/root-gemini/Na_3C9O.md` |
| 270 | Na_3C9o_ | small | done | tree | 0 not placed | 28 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3C9o_.md` |
| 271 | Na_3C9P | small | done | tree | 0 not placed | 30 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3C9P.md` |
| 272 | Na_3C9p_ | small | done | tree | 0 not placed | 25 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9p_.md` |
| 273 | Na_3C9Q | small | done | tree | 0 not placed | 23 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3C9Q.md` |
| 274 | Na_3C9R | small | done | tree | 0 not placed | 11 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3C9R.md` |
| 275 | Na_3C9r_ | small | done | tree | 0 not placed | 20 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3C9r_.md` |
| 276 | Na_3C9S | small | done | tree | 0 not placed | 11 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3C9S.md` |
| 277 | Na_3C9s_ | small | done | no parts | — | 5 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3C9s_.md` |
| 278 | Na_3C9T | small | done | tree | 0 not placed | 8 | low · $0.02 · 0.5 min |  | `processed/root-gemini/Na_3C9T.md` |
| 279 | Na_3C9t_ | small | done | no parts | — | 18 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9t_.md` |
| 280 | Na_3C9U | small | done | no parts | — | 9 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9U.md` |
| 281 | Na_3C9u_ | small | done | tree | 0 not placed | 50 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3C9u_.md` |
| 282 | Na_3C9V | small | done | no parts | — | 8 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9V.md` |
| 283 | Na_3C9v_ | small | done | no parts | — | 5 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9v_.md` |
| 284 | Na_3C9W | small | done | no parts | — | 10 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9W.md` |
| 285 | Na_3C9w_ | small | done | no parts | — | 7 | low · $0.00 · 0.2 min |  | `processed/root-gemini/Na_3C9w_.md` |
| 286 | Na_3C9X | small | done | no parts | — | 11 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3C9X.md` |
| 287 | Na_3C9x_ | small | done | no parts | — | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9x_.md` |
| 288 | Na_3C9Y | small | done | no parts | — | 10 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3C9Y.md` |
| 289 | Na_3C9y_ | small | done | no parts | — | 6 | low · $0.01 · 0.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Na_3C9y_.md` |
| 290 | Na_3C9z_ | small | done | tree | 0 not placed | 42 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3C9z_.md` |
| 291 | Na_3CA0 | small | done | tree | 0 not placed | 5 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CA0.md` |
| 292 | Na_3CA1 | small | done | no parts | — | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CA1.md` |
| 293 | Na_3CA2 | small | done | tree | 0 not placed | 10 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CA2.md` |
| 294 | Na_3CA3 | small | done | no parts | — | 28 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3CA3.md` |
| 295 | Na_3CA5 | small | done | tree | 0 not placed | 8 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CA5.md` |
| 296 | Na_3CA6 | medium | done | tree | 0 not placed | 71 | low · $0.02 · 0.2 min |  | `processed/root-gemini/Na_3CA6.md` |
| 297 | Na_3CA7 | small | done | no parts | — | 21 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CA7.md` |
| 298 | Na_3CA8 | small | done | no parts | — | 6 | low · $0.00 · 0.2 min |  | `processed/root-gemini/Na_3CA8.md` |
| 299 | Na_3CA9 | small | done | tree | 0 not placed | 13 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CA9.md` |
| 300 | Na_3CAA | small | done | no parts | — | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAA.md` |
| 301 | Na_3CAB | small | done | tree | 0 not placed | 5 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAB.md` |
| 302 | Na_3CAb_ | small | done | tree | 0 not placed | 34 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAb_.md` |
| 303 | Na_3CAC | small | done | tree | 0 not placed | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAC.md` |
| 304 | Na_3CAc_ | small | done | no parts | — | 12 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAc_.md` |
| 305 | Na_3CAD | small | done | tree | 0 not placed | 88 | low · $0.02 · 0.2 min |  | `processed/root-gemini/Na_3CAD.md` |
| 306 | Na_3CAd_ | small | done | no parts | — | 15 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAd_.md` |
| 307 | Na_3CAE | small | done | tree | 0 not placed | 23 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3CAE.md` |
| 308 | Na_3CAe_ | small | done | no parts | — | 2 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAe_.md` |
| 309 | Na_3CAF | medium | done | tree | 0 not placed | 92 | low · $0.02 · 0.2 min |  | `processed/root-gemini/Na_3CAF.md` |
| 310 | Na_3CAf_ | small | done | no parts | — | 7 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAf_.md` |
| 311 | Na_3CAG | small | done | tree | 0 not placed | 20 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAG.md` |
| 312 | Na_3CAg_ | small | done | tree | 0 not placed | 145 | low · $0.13 · 0.5 min |  | `processed/root-gemini/Na_3CAg_.md` |
| 313 | Na_3CAH | small | done | no parts | — | 4 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAH.md` |
| 314 | Na_3CAh_ | small | done | tree | 0 not placed | 22 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAh_.md` |
| 315 | Na_3CAI | small | done | no parts | — | 2 | low · $0.01 · 0.3 min |  | `processed/root-gemini/Na_3CAI.md` |
| 316 | Na_3CAi_ | small | done | tree | 0 not placed | 37 | low · $0.02 · 0.1 min |  | `processed/root-gemini/Na_3CAi_.md` |
| 317 | Na_3CAJ | small | done | no parts | — | 7 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAJ.md` |
| 318 | Na_3CAK | small | done | no parts | — | 3 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3CAK.md` |
| 319 | Na_3CAk_ | medium | done | tree | 0 not placed | 476 | low · $0.11 · 1.5 min |  | `processed/root-gemini/Na_3CAk_.md` |
| 320 | Na_3CAL | small | done | no parts | — | 3 | low · $0.02 · 0.4 min |  | `processed/root-gemini/Na_3CAL.md` |
| 321 | Na_3CAl_ | small | done | no parts | — | 61 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3CAl_.md` |
| 322 | Na_3CAM | small | done | no parts | — | 18 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAM.md` |
| 323 | Na_3CAm_ | small | done | no parts | — | 38 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAm_.md` |
| 324 | Na_3CAN | small | done | tree | 0 not placed | 34 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3CAN.md` |
| 325 | Na_3CAn_ | small | done | no parts | — | 75 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3CAn_.md` |
| 326 | Na_3CAO | small | done | tree | 0 not placed | 41 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAO.md` |
| 327 | Na_3CAo_ | small | done | no parts | — | 74 | low · $0.02 · 0.3 min |  | `processed/root-gemini/Na_3CAo_.md` |
| 328 | Na_3CAP | small | done | tree | 0 not placed | 9 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAP.md` |
| 329 | Na_3CAQ | small | done | tree | 0 not placed | 21 | low · $0.01 · 0.1 min | 1 anchor(s) repaired (footnote marker / ༌) | `processed/root-gemini/Na_3CAQ.md` |
| 330 | Na_3CAR | small | done | tree | 0 not placed | 13 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAR.md` |
| 331 | Na_3CAS | small | done | no parts | — | 14 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAS.md` |
| 332 | Na_3CAT | small | done | tree | 0 not placed | 85 | low · $0.02 · 0.3 min |  | `processed/root-gemini/Na_3CAT.md` |
| 333 | Na_3CAU | small | done | tree | 0 not placed | 13 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAU.md` |
| 334 | Na_3CAu_ | small | done | no parts | — | 23 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAu_.md` |
| 335 | Na_3CAV | medium | done | tree | 0 not placed | 536 | low · $0.37 · 1.4 min |  | `processed/root-gemini/Na_3CAV.md` |
| 336 | Na_3CAv_ | small | done | no parts | — | 11 | low · $0.02 · 0.5 min |  | `processed/root-gemini/Na_3CAv_.md` |
| 337 | Na_3CAW | small | done | tree | 0 not placed | 24 | low · $0.03 · 0.1 min |  | `processed/root-gemini/Na_3CAW.md` |
| 338 | Na_3CAX | medium | done | tree | 0 not placed | 177 | low · $0.21 · 4.1 min | grouping fell back to medium for part(s) 1 | `processed/root-gemini/Na_3CAX.md` |
| 339 | Na_3CAx_ | small | done | no parts | — | 8 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CAx_.md` |
| 340 | Na_3CAY | small | done | tree | 0 not placed | 28 | low · $0.02 · 0.1 min |  | `processed/root-gemini/Na_3CAY.md` |
| 341 | Na_3CAZ | small | done | tree | 0 not placed | 7 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAZ.md` |
| 342 | Na_3CAz_ | small | done | tree | 0 not placed | 24 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CAz_.md` |
| 343 | Na_3CB0 | small | done | no parts | — | 16 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CB0.md` |
| 344 | Na_3CB1 | small | done | tree | 0 not placed | 22 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CB1.md` |
| 345 | Na_3CB2 | small | done | tree | 0 not placed | 41 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CB2.md` |
| 346 | Na_3CB3 | small | done | no parts | — | 56 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3CB3.md` |
| 347 | Na_3CB5 | small | done | tree | 0 not placed | 20 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CB5.md` |
| 348 | Na_3CB6 | small | done | tree | 0 not placed | 51 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3CB6.md` |
| 349 | Na_3CBB | medium | done | tree | 0 not placed | 239 | low · $0.06 · 0.8 min |  | `processed/root-gemini/Na_3CBB.md` |
| 350 | Na_3CBC | small | done | tree | 0 not placed | 5 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CBC.md` |
| 351 | Na_3CBD | medium | done | tree | 0 not placed | 492 | low · $0.28 · 4.5 min | grouping fell back to medium for part(s) 2 | `processed/root-gemini/Na_3CBD.md` |
| 352 | Na_3CBE | small | done | no parts | — | 32 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CBE.md` |
| 353 | Na_3CBF | small | done | no parts | — | 13 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CBF.md` |
| 354 | Na_3CBG | small | done | no parts | — | 18 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CBG.md` |
| 355 | Na_3CBH | small | done | no parts | — | 121 | low · $0.08 · 0.4 min |  | `processed/root-gemini/Na_3CBH.md` |
| 356 | Na_3CBI | small | done | tree | 0 not placed | 114 | low · $0.02 · 0.3 min |  | `processed/root-gemini/Na_3CBI.md` |
| 357 | Na_3CBJ | small | done | tree | 0 not placed | 42 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3CBJ.md` |
| 358 | Na_3CBK | small | done | tree | 0 not placed | 15 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CBK.md` |
| 359 | Na_3CBL | small | done | no parts | — | 4 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CBL.md` |
| 360 | Na_3CBM | small | done | no parts | — | 9 | low · $0.01 · 0.3 min |  | `processed/root-gemini/Na_3CBM.md` |
| 361 | Na_3CBN | small | done | tree | 0 not placed | 143 | low · $0.03 · 0.3 min |  | `processed/root-gemini/Na_3CBN.md` |
| 362 | Na_3CBO | small | done | no parts | — | 105 | low · $0.02 · 0.2 min |  | `processed/root-gemini/Na_3CBO.md` |
| 363 | Na_3CBP | medium | done | no parts | — | 270 | low · $0.06 · 0.7 min |  | `processed/root-gemini/Na_3CBP.md` |
| 364 | Na_3CBQ | small | done | no parts | — | 84 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Na_3CBQ.md` |
| 365 | Na_3CBR | small | done | no parts | — | 17 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CBR.md` |
| 366 | Na_3CBS | small | done | no parts | — | 16 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CBS.md` |
| 367 | Na_3CBT | small | done | no parts | — | 8 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CBT.md` |
| 368 | Na_3CBU | small | done | no parts | — | 21 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CBU.md` |
| 369 | Na_3CBV | small | done | no parts | — | 19 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CBV.md` |
| 370 | Na_3CBW | small | done | tree | 0 not placed | 19 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Na_3CBW.md` |
| 371 | Na_3CBX | small | done | no parts | — | 31 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Na_3CBX.md` |
| 372 | Na_3CBY | small | done | tree | 0 not placed | 166 | low · $0.02 · 0.4 min |  | `processed/root-gemini/Na_3CBY.md` |
| 373 | Na_3CBZ | small | done | no parts | — | 14 | low · $0.02 · 0.5 min |  | `processed/root-gemini/Na_3CBZ.md` |
| 374 | Sh_3CCh_ | small | done | no parts | — | 6 | low · $0.01 · 0.1 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Sh_3CCh_.md` |
| 375 | Sh_3CCi_ | small | done | no parts | — | 6 | low · $0.01 · 0.1 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Sh_3CCi_.md` |
| 376 | Sh_3CCj_ | small | done | no parts | — | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Sh_3CCj_.md` |
| 377 | Sh_3CCl_ | small | done | no parts | — | 4 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Sh_3CCl_.md` |
| 378 | Sh_3CCm_ | medium | done | tree | 0 not placed | 898 | low · $1.00 · 1.7 min |  | `processed/root-gemini/Sh_3CCm_.md` |
| 379 | Sh_3CCn_ | small | done | no parts | — | 10 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Sh_3CCn_.md` |
| 380 | Sh_3CCp_ | small | done | tree | 0 not placed | 66 | low · $0.04 · 0.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Sh_3CCp_.md` |
| 381 | Sh_3CCq_ | small | done | no parts | — | 69 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Sh_3CCq_.md` |
| 382 | Sh_3CCr_ | small | done | tree | 0 not placed | 29 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Sh_3CCr_.md` |
| 383 | Sh_3CCu_ | small | done | tree | 0 not placed | 66 | low · $0.03 · 0.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Sh_3CCu_.md` |
| 384 | Sh_3CCv_ | small | done | no parts | — | 6 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Sh_3CCv_.md` |
| 385 | Sh_3CCx_ | small | done | no parts | — | 17 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Sh_3CCx_.md` |
| 386 | Sh_3CCy_ | small | done | tree | 0 not placed | 11 | low · $0.01 · 0.3 min |  | `processed/root-gemini/Sh_3CCy_.md` |
| 387 | Sh_3CCz_ | small | done | tree | 0 not placed | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Sh_3CCz_.md` |
| 388 | Sh_3CD1 | medium | done | tree | 0 not placed | 56 | low · $0.06 · 0.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Sh_3CD1.md` |
| 389 | Sh_3CD2 | medium | done | tree | 0 not placed | 169 | low · $0.09 · 0.4 min |  | `processed/root-gemini/Sh_3CD2.md` |
| 390 | Sh_3CD3 | medium | done | tree | 0 not placed | 146 | low · $0.17 · 0.2 min |  | `processed/root-gemini/Sh_3CD3.md` |
| 391 | Sh_3CD4 | medium | done | tree | 0 not placed | 136 | low · $0.05 · 0.2 min |  | `processed/root-gemini/Sh_3CD4.md` |
| 392 | Sh_3CD5 | small | done | tree | 0 not placed | 32 | low · $0.03 · 0.1 min | 1 anchor(s) repaired (footnote marker / ༌) | `processed/root-gemini/Sh_3CD5.md` |
| 393 | Sh_3CD6 | medium | done | tree | 0 not placed | 112 | low · $0.05 · 0.2 min |  | `processed/root-gemini/Sh_3CD6.md` |
| 394 | Sh_3CD7 | medium | done | tree | 0 not placed | 109 | low · $0.08 · 0.4 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/Sh_3CD7.md` |
| 395 | Sh_3CD8 | medium | done | tree | 0 not placed | 114 | low · $0.07 · 0.6 min |  | `processed/root-gemini/Sh_3CD8.md` |
| 396 | Sh_3CDA | small | done | no parts | — | 96 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Sh_3CDA.md` |
| 397 | Sh_3CDF | small | done | tree | 0 not placed | 59 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Sh_3CDF.md` |
| 398 | Sh_3CFZ | medium | done | tree | 0 not placed | 245 | low · $0.07 · 0.8 min |  | `processed/root-gemini/Sh_3CFZ.md` |
| 399 | Va_3CE0 | small | done | no parts | — | 3 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Va_3CE0.md` |
| 400 | Va_3CEa_ | small | done | tree | 0 not placed | 20 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Va_3CEa_.md` |
| 401 | Va_3CEb_ | small | done | no parts | — | 11 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Va_3CEb_.md` |
| 402 | Va_3CEc_ | small | done | tree | 0 not placed | 29 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Va_3CEc_.md` |
| 403 | Va_3CEd_ | small | done | no parts | — | 9 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Va_3CEd_.md` |
| 404 | Va_3CEL | small | done | tree | 0 not placed | 25 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Va_3CEL.md` |
| 405 | Va_3CEM | small | done | no parts | — | 22 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Va_3CEM.md` |
| 406 | Va_3CEO | small | done | tree | 0 not placed | 38 | low · $0.01 · 0.1 min |  | `processed/root-gemini/Va_3CEO.md` |
| 407 | Va_3CEP | small | done | tree | 0 not placed | 152 | low · $0.02 · 0.3 min |  | `processed/root-gemini/Va_3CEP.md` |
| 408 | Va_3CEQ | medium | done | no parts | — | 24 | low · $0.02 · 0.1 min |  | `processed/root-gemini/Va_3CEQ.md` |
| 409 | Va_3CES | medium | done | tree | 0 not placed | 94 | low · $0.07 · 0.2 min | 1 anchor(s) repaired (footnote marker / ༌) | `processed/root-gemini/Va_3CES.md` |
| 410 | Va_3CET | small | done | tree | 0 not placed | 15 | low · $0.01 · 0.4 min |  | `processed/root-gemini/Va_3CET.md` |
| 411 | Va_3CEX | medium | done | tree | 0 not placed | 586 | low · $0.10 · 1.4 min |  | `processed/root-gemini/Va_3CEX.md` |
| 412 | Va_3CEY | small | done | tree | 0 not placed | 28 | low · $0.00 · 0.2 min |  | `processed/root-gemini/Va_3CEY.md` |
| 413 | As_3CDk_ | large | done | tree | 0 not placed | 599 | medium · $0.53 · 10.4 min |  | `processed/root-gemini/As_3CDk_.md` |
| 414 | As_3CDl_ | large | done | tree | 0 not placed | 1733 | medium · $1.37 · 26.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/As_3CDl_.md` |
| 415 | As_3CDm_ | large | done | tree | 0 not placed | 1039 | medium · $1.76 · 12.7 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/As_3CDm_.md` |
| 416 | As_3CDn_ | large | done | tree | 0 not placed | 1072 | medium · $3.24 · 21.5 min |  | `processed/root-gemini/As_3CDn_.md` |
| 417 | As_3CDo_ | large | done | tree | 0 not placed | 1460 | medium · $1.21 · 22.0 min |  | `processed/root-gemini/As_3CDo_.md` |
| 418 | As_3CDp_ | large | done | tree | 0 not placed | 1314 | medium · $1.12 · 14.9 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/As_3CDp_.md` |
| 419 | Ar_3CBe_ | small | done | tree | 0 not placed | 22 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Ar_3CBe_.md` |
| 420 | At_3CHn_ | small | done | tree | 0 not placed | 61 | low · $0.02 · 0.3 min |  | `processed/root-gemini/At_3CHn_.md` |
| 421 | Ar_3CBj_ | small | done | no parts | — | 54 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Ar_3CBj_.md` |
| 422 | Na_3C9e_ | small | done | no parts | — | 111 | low · $0.02 · 0.2 min |  | `processed/root-gemini/Na_3C9e_.md` |
| 423 | As_3CDq_ | large | done | tree | 0 not placed | 1264 | medium · $2.50 · 21.2 min | 2 anchor(s) repaired (footnote marker / ༌) | `processed/root-gemini/As_3CDq_.md` |
| 424 | As_3CDv_ | large | done | tree | 0 not placed | 1040 | medium · $0.63 · 13.6 min |  | `processed/root-gemini/As_3CDv_.md` |
| 425 | At_3CHK | large | done | tree | 0 not placed | 1573 | medium · $2.29 · 61.0 min |  | `processed/root-gemini/At_3CHK.md` |
| 426 | Dh_3CF5 | large | done | tree | 0 not placed | 1179 | medium · $1.38 · 29.7 min |  | `processed/root-gemini/Dh_3CF5.md` |
| 427 | Dh_3CF6 | large | done | tree | 0 not placed | 943 | medium · $0.71 · 15.0 min |  | `processed/root-gemini/Dh_3CF6.md` |
| 428 | Gu_3CFS | large | done | tree | 0 not placed | 1184 | medium · $3.14 · 27.2 min |  | `processed/root-gemini/Gu_3CFS.md` |
| 429 | Gu_3CFT | large | done | tree | 0 not placed | 864 | medium · $2.17 · 17.9 min |  | `processed/root-gemini/Gu_3CFT.md` |
| 430 | Ha_3CFF | large | done | tree | 0 not placed | 831 | medium · $1.84 · 18.1 min | 4 anchor(s) repaired (footnote marker / ༌) | `processed/root-gemini/Ha_3CFF.md` |
| 431 | Ha_3CFG | large | done | tree | 0 not placed | 1202 | medium · $3.15 · 17.8 min |  | `processed/root-gemini/Ha_3CFG.md` |
| 432 | Ha_3CFH | large | done | tree | 0 not placed | 1084 | medium · $1.44 · 17.8 min |  | `processed/root-gemini/Ha_3CFH.md` |
| 433 | Ha_3CFI | large | done | tree | 0 not placed | 765 | medium · $1.45 · 11.6 min |  | `processed/root-gemini/Ha_3CFI.md` |
| 434 | Ka_3CDK | large | done | no parts | — | 804 | medium · $0.95 · 19.7 min |  | `processed/root-gemini/Ka_3CDK.md` |
| 435 | Na_3CB4 | large | done | tree | 0 not placed | 382 | medium · $0.70 · 13.2 min |  | `processed/root-gemini/Na_3CB4.md` |
| 436 | Sh_3CCs_ | large | done | tree | 0 not placed | 596 | medium · $0.94 · 19.9 min |  | `processed/root-gemini/Sh_3CCs_.md` |
| 437 | Sh_3CCt_ | large | done | tree | 0 not placed | 1422 | medium · $2.64 · 29.1 min |  | `processed/root-gemini/Sh_3CCt_.md` |
| 438 | Sh_3CDE | large | done | tree | 0 not placed | 3377 | medium · $3.73 · 84.8 min |  | `processed/root-gemini/Sh_3CDE.md` |
| 439 | Va_3CER | large | done | tree | 0 not placed | 1056 | medium · $0.97 · 17.8 min |  | `processed/root-gemini/Va_3CER.md` |
| 440 | Ha_3CFJ | large | done | tree | 0 not placed | 721 | medium · $3.70 · 17.8 min |  | `processed/root-gemini/Ha_3CFJ.md` |
| 441 | Ch_3CCd_ | medium | done | tree | 0 not placed | 318 | low · $0.11 · 0.6 min |  | `processed/root-gemini/Ch_3CCd_.md` |
| 442 | Di_3CEp_ | medium | done | tree | 0 not placed | 281 | low · $0.07 · 1.0 min |  | `processed/root-gemini/Di_3CEp_.md` |
