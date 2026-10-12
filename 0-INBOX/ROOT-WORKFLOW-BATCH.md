# Root-text workflow batch — segmentation + TOC ingest + grouping + block IDs

Gemini (gemini-3.8-flash) runs the rest of the workflow for every root text whose TOC
extraction is finished (see `0-INBOX/ROOT-TOC-BATCH.md`). How to run: `0-INBOX/temp/root-toc/README.md`.

Updated 2026-10-12 · 436 texts · done 10 · failed 0 ·
running 2 · **to do 424**

| Where | Path |
|---|---|
| Finished files (with block IDs) | `0-INBOX/processed/root-gemini/<id>-<free\|prose>.md` |
| Working folder per text | `0-INBOX/temp/root-final/<id>/` (prepared.md, group-in.md, groups-*.json, final-*.md) |
| Tree used for the headings | `0-INBOX/temp/TOC-<id>/toc-tree-anchored-<id>.md` |
| Log per text | `0-INBOX/temp/root-toc/logs/workflow-<id>.log` |

`toc` tree = the text's parts became headings · no parts = `## གཞུང་དངོས། ^1-0` only ·
`headings` = body headings placed / not placed (a not-placed heading must be put in by hand) ·
`blocks` = stanzas / paragraphs. Review the files before they replace anything in
`0-INBOX/processed/root/`.

| # | id | size | status | toc | headings | blocks | run (cost · time) | note | output |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Ar_3CBa_ | medium | todo | tree |  |  |  |  |  |
| 2 | Ar_3CBc_ | medium | todo | tree |  |  |  |  |  |
| 3 | Ar_3CBf_ | small | todo | no parts |  |  |  |  |  |
| 4 | Ar_3CBg_ | medium | todo | tree |  |  |  |  |  |
| 5 | Ar_3CBh_ | medium | todo | tree |  |  |  |  |  |
| 6 | Ar_3CBi_ | small | todo | no parts |  |  |  |  |  |
| 7 | Ar_3CBk_ | small | todo | tree |  |  |  |  |  |
| 8 | Ar_3CBl_ | small | todo | tree |  |  |  |  |  |
| 9 | Ar_3CBm_ | small | done | tree | 0 not placed | 74 | low · $0.02 · 0.4 min |  | `processed/root-gemini/Ar_3CBm_-prose.md` |
| 10 | Ar_3CBn_ | small | done | no parts | — | 14 | low · $0.00 · 0.1 min |  | `processed/root-gemini/Ar_3CBn_-free.md` |
| 11 | Ar_3CBo_ | small | todo | no parts |  |  |  |  |  |
| 12 | Ar_3CBp_ | small | todo | tree |  |  |  |  |  |
| 13 | Ar_3CBq_ | small | todo | tree |  |  |  |  |  |
| 14 | Ar_3CBr_ | small | todo | no parts |  |  |  |  |  |
| 15 | Ar_3CBs_ | small | todo | tree |  |  |  |  |  |
| 16 | Ar_3CBt_ | small | todo | no parts |  |  |  |  |  |
| 17 | Ar_3CBu_ | small | todo | no parts |  |  |  |  |  |
| 18 | Ar_3CBv_ | small | todo | no parts |  |  |  |  |  |
| 19 | Ar_3CBw_ | small | todo | tree |  |  |  |  |  |
| 20 | Ar_3CBx_ | small | done | tree | 0 not placed | 16 | low · $0.01 · 0.2 min |  | `processed/root-gemini/Ar_3CBx_-prose.md` |
| 21 | Ar_3CBy_ | small | todo | tree |  |  |  |  |  |
| 22 | Ar_3CBz_ | small | todo | no parts |  |  |  |  |  |
| 23 | Ar_3CC1 | medium | todo | tree |  |  |  |  |  |
| 24 | Ar_3CC2 | small | todo | tree |  |  |  |  |  |
| 25 | Ar_3CC3 | small | todo | no parts |  |  |  |  |  |
| 26 | Ar_3CC5 | small | todo | tree |  |  |  |  |  |
| 27 | Ar_3CC6 | small | todo | tree |  |  |  |  |  |
| 28 | Ar_3CC7 | small | todo | no parts |  |  |  |  |  |
| 29 | Ar_3CC8 | small | todo | no parts |  |  |  |  |  |
| 30 | Ar_3CC9 | small | todo | no parts |  |  |  |  |  |
| 31 | Ar_3CCA | small | todo | no parts |  |  |  |  |  |
| 32 | Ar_3CCB | small | todo | no parts |  |  |  |  |  |
| 33 | As_3CDc_ | small | todo | no parts |  |  |  |  |  |
| 34 | As_3CDd_ | small | todo | no parts |  |  |  |  |  |
| 35 | As_3CDe_ | small | todo | no parts |  |  |  |  |  |
| 36 | As_3CDr_ | medium | todo | tree |  |  |  |  |  |
| 37 | As_3CDs_ | medium | todo | tree |  |  |  |  |  |
| 38 | As_3CDt_ | medium | todo | tree |  |  |  |  |  |
| 39 | As_3CDu_ | medium | todo | tree |  |  |  |  |  |
| 40 | As_3CDw_ | small | todo | tree |  |  |  |  |  |
| 41 | At_3CFb_ | small | todo | tree |  |  |  |  |  |
| 42 | At_3CFc_ | small | todo | tree |  |  |  |  |  |
| 43 | At_3CFd_ | medium | todo | tree |  |  |  |  |  |
| 44 | At_3CFe_ | small | todo | tree |  |  |  |  |  |
| 45 | At_3CFf_ | small | todo | tree |  |  |  |  |  |
| 46 | At_3CFg_ | small | todo | tree |  |  |  |  |  |
| 47 | At_3CFh_ | small | todo | tree |  |  |  |  |  |
| 48 | At_3CFj_ | small | todo | no parts |  |  |  |  |  |
| 49 | At_3CFl_ | small | todo | no parts |  |  |  |  |  |
| 50 | At_3CFm_ | small | todo | tree |  |  |  |  |  |
| 51 | At_3CFn_ | small | todo | no parts |  |  |  |  |  |
| 52 | At_3CFo_ | small | todo | no parts |  |  |  |  |  |
| 53 | At_3CFp_ | small | todo | no parts |  |  |  |  |  |
| 54 | At_3CFq_ | small | todo | no parts |  |  |  |  |  |
| 55 | At_3CFr_ | small | todo | no parts |  |  |  |  |  |
| 56 | At_3CFs_ | small | todo | tree |  |  |  |  |  |
| 57 | At_3CFt_ | medium | todo | tree |  |  |  |  |  |
| 58 | At_3CFu_ | small | todo | tree |  |  |  |  |  |
| 59 | At_3CFv_ | small | todo | no parts |  |  |  |  |  |
| 60 | At_3CFw_ | small | todo | tree |  |  |  |  |  |
| 61 | At_3CFx_ | small | todo | no parts |  |  |  |  |  |
| 62 | At_3CFy_ | small | todo | no parts |  |  |  |  |  |
| 63 | At_3CFz_ | small | todo | tree |  |  |  |  |  |
| 64 | At_3CG0 | small | todo | no parts |  |  |  |  |  |
| 65 | At_3CG1 | small | todo | tree |  |  |  |  |  |
| 66 | At_3CG2 | small | todo | no parts |  |  |  |  |  |
| 67 | At_3CG3 | small | todo | tree |  |  |  |  |  |
| 68 | At_3CG4 | small | todo | no parts |  |  |  |  |  |
| 69 | At_3CG5 | small | todo | tree |  |  |  |  |  |
| 70 | At_3CG6 | small | todo | tree |  |  |  |  |  |
| 71 | At_3CG7 | small | todo | no parts |  |  |  |  |  |
| 72 | At_3CG8 | small | todo | tree |  |  |  |  |  |
| 73 | At_3CG9 | small | todo | tree |  |  |  |  |  |
| 74 | At_3CGA | small | todo | tree |  |  |  |  |  |
| 75 | At_3CGa_ | small | todo | tree |  |  |  |  |  |
| 76 | At_3CGB | small | todo | tree |  |  |  |  |  |
| 77 | At_3CGb_ | small | todo | tree |  |  |  |  |  |
| 78 | At_3CGC | small | todo | no parts |  |  |  |  |  |
| 79 | At_3CGc_ | small | todo | tree |  |  |  |  |  |
| 80 | At_3CGD | small | todo | no parts |  |  |  |  |  |
| 81 | At_3CGd_ | small | todo | tree |  |  |  |  |  |
| 82 | At_3CGE | small | todo | tree |  |  |  |  |  |
| 83 | At_3CGe_ | small | todo | tree |  |  |  |  |  |
| 84 | At_3CGF | small | todo | tree |  |  |  |  |  |
| 85 | At_3CGf_ | small | todo | tree |  |  |  |  |  |
| 86 | At_3CGG | small | todo | no parts |  |  |  |  |  |
| 87 | At_3CGg_ | small | todo | tree |  |  |  |  |  |
| 88 | At_3CGH | small | todo | no parts |  |  |  |  |  |
| 89 | At_3CGh_ | small | todo | tree |  |  |  |  |  |
| 90 | At_3CGI | small | todo | no parts |  |  |  |  |  |
| 91 | At_3CGi_ | small | todo | tree |  |  |  |  |  |
| 92 | At_3CGJ | small | todo | tree |  |  |  |  |  |
| 93 | At_3CGj_ | small | todo | no parts |  |  |  |  |  |
| 94 | At_3CGK | small | todo | tree |  |  |  |  |  |
| 95 | At_3CGk_ | small | todo | tree |  |  |  |  |  |
| 96 | At_3CGL | small | todo | no parts |  |  |  |  |  |
| 97 | At_3CGl_ | small | todo | tree |  |  |  |  |  |
| 98 | At_3CGM | small | todo | tree |  |  |  |  |  |
| 99 | At_3CGm_ | small | todo | tree |  |  |  |  |  |
| 100 | At_3CGN | small | todo | tree |  |  |  |  |  |
| 101 | At_3CGn_ | small | todo | tree |  |  |  |  |  |
| 102 | At_3CGO | small | todo | no parts |  |  |  |  |  |
| 103 | At_3CGo_ | small | todo | no parts |  |  |  |  |  |
| 104 | At_3CGP | medium | todo | tree |  |  |  |  |  |
| 105 | At_3CGp_ | small | todo | no parts |  |  |  |  |  |
| 106 | At_3CGQ | small | todo | tree |  |  |  |  |  |
| 107 | At_3CGq_ | medium | todo | tree |  |  |  |  |  |
| 108 | At_3CGR | small | todo | no parts |  |  |  |  |  |
| 109 | At_3CGS | small | todo | tree |  |  |  |  |  |
| 110 | At_3CGs_ | small | todo | tree |  |  |  |  |  |
| 111 | At_3CGT | small | todo | no parts |  |  |  |  |  |
| 112 | At_3CGt_ | small | todo | tree |  |  |  |  |  |
| 113 | At_3CGU | small | todo | no parts |  |  |  |  |  |
| 114 | At_3CGu_ | small | todo | tree |  |  |  |  |  |
| 115 | At_3CGV | small | todo | tree |  |  |  |  |  |
| 116 | At_3CGv_ | medium | todo | tree |  |  |  |  |  |
| 117 | At_3CGW | small | todo | tree |  |  |  |  |  |
| 118 | At_3CGX | small | todo | tree |  |  |  |  |  |
| 119 | At_3CGx_ | small | todo | no parts |  |  |  |  |  |
| 120 | At_3CGY | small | todo | tree |  |  |  |  |  |
| 121 | At_3CGy_ | small | todo | tree |  |  |  |  |  |
| 122 | At_3CGZ | small | todo | no parts |  |  |  |  |  |
| 123 | At_3CH0 | small | todo | no parts |  |  |  |  |  |
| 124 | At_3CH1 | small | todo | tree |  |  |  |  |  |
| 125 | At_3CH2 | small | todo | no parts |  |  |  |  |  |
| 126 | At_3CH3 | small | todo | no parts |  |  |  |  |  |
| 127 | At_3CH4 | small | todo | tree |  |  |  |  |  |
| 128 | At_3CH5 | small | todo | tree |  |  |  |  |  |
| 129 | At_3CH6 | small | todo | no parts |  |  |  |  |  |
| 130 | At_3CH7 | small | todo | tree |  |  |  |  |  |
| 131 | At_3CH8 | small | todo | tree |  |  |  |  |  |
| 132 | At_3CH9 | small | todo | tree |  |  |  |  |  |
| 133 | At_3CHA | small | todo | tree |  |  |  |  |  |
| 134 | At_3CHa_ | small | todo | tree |  |  |  |  |  |
| 135 | At_3CHB | small | todo | tree |  |  |  |  |  |
| 136 | At_3CHb_ | small | todo | no parts |  |  |  |  |  |
| 137 | At_3CHC | small | todo | tree |  |  |  |  |  |
| 138 | At_3CHc_ | small | todo | tree |  |  |  |  |  |
| 139 | At_3CHD | small | todo | no parts |  |  |  |  |  |
| 140 | At_3CHd_ | small | todo | no parts |  |  |  |  |  |
| 141 | At_3CHE | small | todo | no parts |  |  |  |  |  |
| 142 | At_3CHe_ | small | todo | no parts |  |  |  |  |  |
| 143 | At_3CHF | small | todo | tree |  |  |  |  |  |
| 144 | At_3CHf_ | small | todo | tree |  |  |  |  |  |
| 145 | At_3CHG | small | todo | no parts |  |  |  |  |  |
| 146 | At_3CHg_ | small | todo | no parts |  |  |  |  |  |
| 147 | At_3CHH | small | todo | tree |  |  |  |  |  |
| 148 | At_3CHh_ | small | todo | tree |  |  |  |  |  |
| 149 | At_3CHI | small | todo | no parts |  |  |  |  |  |
| 150 | At_3CHi_ | small | todo | tree |  |  |  |  |  |
| 151 | At_3CHJ | small | todo | no parts |  |  |  |  |  |
| 152 | At_3CHj_ | small | todo | tree |  |  |  |  |  |
| 153 | At_3CHk_ | small | todo | tree |  |  |  |  |  |
| 154 | At_3CHL | medium | todo | tree |  |  |  |  |  |
| 155 | At_3CHl_ | small | todo | tree |  |  |  |  |  |
| 156 | At_3CHM | small | todo | tree |  |  |  |  |  |
| 157 | At_3CHm_ | small | todo | tree |  |  |  |  |  |
| 158 | At_3CHN | small | todo | no parts |  |  |  |  |  |
| 159 | At_3CHO | small | todo | no parts |  |  |  |  |  |
| 160 | At_3CHo_ | small | todo | no parts |  |  |  |  |  |
| 161 | At_3CHP | small | todo | no parts |  |  |  |  |  |
| 162 | At_3CHp_ | small | todo | tree |  |  |  |  |  |
| 163 | At_3CHQ | small | todo | tree |  |  |  |  |  |
| 164 | At_3CHq_ | small | todo | tree |  |  |  |  |  |
| 165 | At_3CHR | small | todo | tree |  |  |  |  |  |
| 166 | At_3CHr_ | small | todo | tree |  |  |  |  |  |
| 167 | At_3CHS | small | todo | no parts |  |  |  |  |  |
| 168 | At_3CHs_ | small | todo | tree |  |  |  |  |  |
| 169 | At_3CHT | small | todo | no parts |  |  |  |  |  |
| 170 | At_3CHt_ | small | todo | tree |  |  |  |  |  |
| 171 | At_3CHU | small | todo | no parts |  |  |  |  |  |
| 172 | At_3CHu_ | small | todo | tree |  |  |  |  |  |
| 173 | At_3CHV | small | todo | tree |  |  |  |  |  |
| 174 | At_3CHv_ | small | todo | tree |  |  |  |  |  |
| 175 | At_3CHW | small | todo | no parts |  |  |  |  |  |
| 176 | At_3CHw_ | small | todo | tree |  |  |  |  |  |
| 177 | At_3CHX | small | todo | no parts |  |  |  |  |  |
| 178 | At_3CHY | small | todo | no parts |  |  |  |  |  |
| 179 | At_3CHy_ | small | todo | tree |  |  |  |  |  |
| 180 | At_3CHZ | small | todo | no parts |  |  |  |  |  |
| 181 | At_3CHz_ | small | todo | no parts |  |  |  |  |  |
| 182 | At_3CI0 | small | todo | no parts |  |  |  |  |  |
| 183 | At_3CI1 | small | todo | no parts |  |  |  |  |  |
| 184 | At_3CI2 | small | todo | no parts |  |  |  |  |  |
| 185 | At_3CI3 | small | todo | tree |  |  |  |  |  |
| 186 | At_3CI4 | small | todo | no parts |  |  |  |  |  |
| 187 | At_3CI5 | small | todo | no parts |  |  |  |  |  |
| 188 | At_3CI6 | small | todo | no parts |  |  |  |  |  |
| 189 | At_3CI7 | small | todo | tree |  |  |  |  |  |
| 190 | At_3CI8 | small | todo | tree |  |  |  |  |  |
| 191 | At_3CI9 | small | todo | tree |  |  |  |  |  |
| 192 | At_3CIA | small | todo | no parts |  |  |  |  |  |
| 193 | Bh_3CCH | medium | todo | tree |  |  |  |  |  |
| 194 | Bh_3CCI | medium | todo | tree |  |  |  |  |  |
| 195 | Bh_3CCJ | small | todo | tree |  |  |  |  |  |
| 196 | Bh_3CCK | medium | todo | tree |  |  |  |  |  |
| 197 | Bh_3CCO | small | todo | tree |  |  |  |  |  |
| 198 | Ch_3CCc_ | medium | todo | tree |  |  |  |  |  |
| 199 | Ch_3CCf_ | small | todo | tree |  |  |  |  |  |
| 200 | Ch_3CCP | small | todo | no parts |  |  |  |  |  |
| 201 | Ch_3CCR | medium | todo | tree |  |  |  |  |  |
| 202 | Ch_3CCS | small | todo | tree |  |  |  |  |  |
| 203 | Ch_3CCU | small | todo | no parts |  |  |  |  |  |
| 204 | Ch_3CCV | small | todo | tree |  |  |  |  |  |
| 205 | Ch_3CCX | medium | todo | tree |  |  |  |  |  |
| 206 | Ch_3CCZ | small | todo | tree |  |  |  |  |  |
| 207 | Dh_3CEy_ | small | todo | no parts |  |  |  |  |  |
| 208 | Dh_3CF0 | small | todo | no parts |  |  |  |  |  |
| 209 | Dh_3CF1 | small | todo | no parts |  |  |  |  |  |
| 210 | Dh_3CF2 | medium | todo | tree |  |  |  |  |  |
| 211 | Dh_3CF3 | small | todo | tree |  |  |  |  |  |
| 212 | Dh_3CF7 | medium | todo | tree |  |  |  |  |  |
| 213 | Dh_3CF8 | medium | todo | tree |  |  |  |  |  |
| 214 | Dh_3CF9 | small | todo | no parts |  |  |  |  |  |
| 215 | Dh_3CFC | medium | todo | tree |  |  |  |  |  |
| 216 | Dh_3CFD | small | todo | no parts |  |  |  |  |  |
| 217 | Di_3CEe_ | medium | todo | tree |  |  |  |  |  |
| 218 | Di_3CEi_ | small | todo | no parts |  |  |  |  |  |
| 219 | Di_3CEj_ | small | todo | no parts |  |  |  |  |  |
| 220 | Di_3CEk_ | small | todo | no parts |  |  |  |  |  |
| 221 | Di_3CEl_ | small | todo | tree |  |  |  |  |  |
| 222 | Di_3CEn_ | small | todo | no parts |  |  |  |  |  |
| 223 | Di_3CEq_ | medium | todo | tree |  |  |  |  |  |
| 224 | Di_3CEs_ | small | todo | no parts |  |  |  |  |  |
| 225 | Di_3CEu_ | small | todo | no parts |  |  |  |  |  |
| 226 | Di_3CEv_ | small | todo | tree |  |  |  |  |  |
| 227 | Di_3CEw_ | small | todo | tree |  |  |  |  |  |
| 228 | Di_3CEx_ | small | todo | tree |  |  |  |  |  |
| 229 | Ha_3CFO | medium | todo | tree |  |  |  |  |  |
| 230 | Ka_3CDL | medium | todo | tree |  |  |  |  |  |
| 231 | Ka_3CDM | medium | todo | tree |  |  |  |  |  |
| 232 | Ka_3CDN | small | todo | no parts |  |  |  |  |  |
| 233 | Ka_3CDO | medium | todo | tree |  |  |  |  |  |
| 234 | Ka_3CDP | medium | todo | tree |  |  |  |  |  |
| 235 | Ka_3CDQ | medium | todo | tree |  |  |  |  |  |
| 236 | Ka_3CDR | small | todo | tree |  |  |  |  |  |
| 237 | Ka_3CDV | small | todo | tree |  |  |  |  |  |
| 238 | Ka_3CDW | small | todo | no parts |  |  |  |  |  |
| 239 | Ka_3CDY | small | todo | no parts |  |  |  |  |  |
| 240 | Na_3C92 | small | todo | no parts |  |  |  |  |  |
| 241 | Na_3C93 | small | todo | no parts |  |  |  |  |  |
| 242 | Na_3C94 | small | todo | no parts |  |  |  |  |  |
| 243 | Na_3C95 | small | todo | no parts |  |  |  |  |  |
| 244 | Na_3C96 | small | todo | no parts |  |  |  |  |  |
| 245 | Na_3C97 | small | todo | no parts |  |  |  |  |  |
| 246 | Na_3C99 | small | todo | no parts |  |  |  |  |  |
| 247 | Na_3C9A | small | todo | no parts |  |  |  |  |  |
| 248 | Na_3C9a_ | medium | todo | tree |  |  |  |  |  |
| 249 | Na_3C9B | small | todo | no parts |  |  |  |  |  |
| 250 | Na_3C9b_ | small | todo | tree |  |  |  |  |  |
| 251 | Na_3C9C | small | todo | no parts |  |  |  |  |  |
| 252 | Na_3C9c_ | medium | todo | tree |  |  |  |  |  |
| 253 | Na_3C9D | small | todo | no parts |  |  |  |  |  |
| 254 | Na_3C9d_ | small | todo | tree |  |  |  |  |  |
| 255 | Na_3C9E | small | todo | no parts |  |  |  |  |  |
| 256 | Na_3C9F | small | todo | no parts |  |  |  |  |  |
| 257 | Na_3C9G | small | todo | no parts |  |  |  |  |  |
| 258 | Na_3C9H | small | todo | no parts |  |  |  |  |  |
| 259 | Na_3C9h_ | medium | todo | tree |  |  |  |  |  |
| 260 | Na_3C9I | small | todo | no parts |  |  |  |  |  |
| 261 | Na_3C9i_ | small | todo | tree |  |  |  |  |  |
| 262 | Na_3C9J | small | todo | no parts |  |  |  |  |  |
| 263 | Na_3C9j_ | small | todo | tree |  |  |  |  |  |
| 264 | Na_3C9K | small | todo | no parts |  |  |  |  |  |
| 265 | Na_3C9k_ | medium | todo | tree |  |  |  |  |  |
| 266 | Na_3C9M | small | todo | no parts |  |  |  |  |  |
| 267 | Na_3C9N | small | todo | tree |  |  |  |  |  |
| 268 | Na_3C9n_ | medium | todo | tree |  |  |  |  |  |
| 269 | Na_3C9O | small | todo | tree |  |  |  |  |  |
| 270 | Na_3C9o_ | small | todo | tree |  |  |  |  |  |
| 271 | Na_3C9P | small | todo | tree |  |  |  |  |  |
| 272 | Na_3C9p_ | small | todo | tree |  |  |  |  |  |
| 273 | Na_3C9Q | small | todo | tree |  |  |  |  |  |
| 274 | Na_3C9R | small | todo | tree |  |  |  |  |  |
| 275 | Na_3C9r_ | small | todo | tree |  |  |  |  |  |
| 276 | Na_3C9S | small | todo | tree |  |  |  |  |  |
| 277 | Na_3C9s_ | small | todo | no parts |  |  |  |  |  |
| 278 | Na_3C9T | small | todo | tree |  |  |  |  |  |
| 279 | Na_3C9t_ | small | todo | no parts |  |  |  |  |  |
| 280 | Na_3C9U | small | todo | no parts |  |  |  |  |  |
| 281 | Na_3C9u_ | small | todo | tree |  |  |  |  |  |
| 282 | Na_3C9V | small | todo | no parts |  |  |  |  |  |
| 283 | Na_3C9v_ | small | todo | no parts |  |  |  |  |  |
| 284 | Na_3C9W | small | todo | no parts |  |  |  |  |  |
| 285 | Na_3C9w_ | small | todo | no parts |  |  |  |  |  |
| 286 | Na_3C9X | small | todo | no parts |  |  |  |  |  |
| 287 | Na_3C9x_ | small | todo | no parts |  |  |  |  |  |
| 288 | Na_3C9Y | small | todo | no parts |  |  |  |  |  |
| 289 | Na_3C9y_ | small | todo | no parts |  |  |  |  |  |
| 290 | Na_3C9z_ | small | todo | tree |  |  |  |  |  |
| 291 | Na_3CA0 | small | todo | tree |  |  |  |  |  |
| 292 | Na_3CA1 | small | todo | no parts |  |  |  |  |  |
| 293 | Na_3CA2 | small | todo | tree |  |  |  |  |  |
| 294 | Na_3CA3 | small | todo | no parts |  |  |  |  |  |
| 295 | Na_3CA5 | small | todo | tree |  |  |  |  |  |
| 296 | Na_3CA6 | medium | todo | tree |  |  |  |  |  |
| 297 | Na_3CA7 | small | todo | no parts |  |  |  |  |  |
| 298 | Na_3CA8 | small | todo | no parts |  |  |  |  |  |
| 299 | Na_3CA9 | small | todo | tree |  |  |  |  |  |
| 300 | Na_3CAA | small | todo | no parts |  |  |  |  |  |
| 301 | Na_3CAB | small | todo | tree |  |  |  |  |  |
| 302 | Na_3CAb_ | small | todo | tree |  |  |  |  |  |
| 303 | Na_3CAC | small | todo | tree |  |  |  |  |  |
| 304 | Na_3CAc_ | small | todo | no parts |  |  |  |  |  |
| 305 | Na_3CAD | small | todo | tree |  |  |  |  |  |
| 306 | Na_3CAd_ | small | todo | no parts |  |  |  |  |  |
| 307 | Na_3CAE | small | todo | tree |  |  |  |  |  |
| 308 | Na_3CAe_ | small | todo | no parts |  |  |  |  |  |
| 309 | Na_3CAF | medium | todo | tree |  |  |  |  |  |
| 310 | Na_3CAf_ | small | todo | no parts |  |  |  |  |  |
| 311 | Na_3CAG | small | todo | tree |  |  |  |  |  |
| 312 | Na_3CAg_ | small | todo | tree |  |  |  |  |  |
| 313 | Na_3CAH | small | todo | no parts |  |  |  |  |  |
| 314 | Na_3CAh_ | small | todo | tree |  |  |  |  |  |
| 315 | Na_3CAI | small | todo | no parts |  |  |  |  |  |
| 316 | Na_3CAi_ | small | todo | tree |  |  |  |  |  |
| 317 | Na_3CAJ | small | todo | no parts |  |  |  |  |  |
| 318 | Na_3CAK | small | todo | no parts |  |  |  |  |  |
| 319 | Na_3CAk_ | medium | todo | tree |  |  |  |  |  |
| 320 | Na_3CAL | small | todo | no parts |  |  |  |  |  |
| 321 | Na_3CAl_ | small | todo | no parts |  |  |  |  |  |
| 322 | Na_3CAM | small | todo | no parts |  |  |  |  |  |
| 323 | Na_3CAm_ | small | todo | no parts |  |  |  |  |  |
| 324 | Na_3CAN | small | todo | tree |  |  |  |  |  |
| 325 | Na_3CAn_ | small | todo | no parts |  |  |  |  |  |
| 326 | Na_3CAO | small | todo | tree |  |  |  |  |  |
| 327 | Na_3CAo_ | small | todo | no parts |  |  |  |  |  |
| 328 | Na_3CAP | small | todo | tree |  |  |  |  |  |
| 329 | Na_3CAQ | small | todo | tree |  |  |  |  |  |
| 330 | Na_3CAR | small | todo | tree |  |  |  |  |  |
| 331 | Na_3CAS | small | todo | no parts |  |  |  |  |  |
| 332 | Na_3CAT | small | todo | tree |  |  |  |  |  |
| 333 | Na_3CAU | small | todo | tree |  |  |  |  |  |
| 334 | Na_3CAu_ | small | todo | no parts |  |  |  |  |  |
| 335 | Na_3CAV | medium | todo | tree |  |  |  |  |  |
| 336 | Na_3CAv_ | small | todo | no parts |  |  |  |  |  |
| 337 | Na_3CAW | small | todo | tree |  |  |  |  |  |
| 338 | Na_3CAX | medium | todo | tree |  |  |  |  |  |
| 339 | Na_3CAx_ | small | todo | no parts |  |  |  |  |  |
| 340 | Na_3CAY | small | todo | tree |  |  |  |  |  |
| 341 | Na_3CAZ | small | todo | tree |  |  |  |  |  |
| 342 | Na_3CAz_ | small | todo | tree |  |  |  |  |  |
| 343 | Na_3CB0 | small | todo | no parts |  |  |  |  |  |
| 344 | Na_3CB1 | small | todo | tree |  |  |  |  |  |
| 345 | Na_3CB2 | small | todo | tree |  |  |  |  |  |
| 346 | Na_3CB3 | small | todo | no parts |  |  |  |  |  |
| 347 | Na_3CB5 | small | todo | tree |  |  |  |  |  |
| 348 | Na_3CB6 | small | todo | tree |  |  |  |  |  |
| 349 | Na_3CBB | medium | todo | tree |  |  |  |  |  |
| 350 | Na_3CBC | small | todo | tree |  |  |  |  |  |
| 351 | Na_3CBD | medium | todo | tree |  |  |  |  |  |
| 352 | Na_3CBE | small | todo | tree |  |  |  |  |  |
| 353 | Na_3CBF | small | todo | no parts |  |  |  |  |  |
| 354 | Na_3CBG | small | todo | no parts |  |  |  |  |  |
| 355 | Na_3CBH | small | todo | tree |  |  |  |  |  |
| 356 | Na_3CBI | small | todo | tree |  |  |  |  |  |
| 357 | Na_3CBJ | small | todo | tree |  |  |  |  |  |
| 358 | Na_3CBK | small | todo | tree |  |  |  |  |  |
| 359 | Na_3CBL | small | todo | no parts |  |  |  |  |  |
| 360 | Na_3CBM | small | todo | no parts |  |  |  |  |  |
| 361 | Na_3CBN | small | todo | tree |  |  |  |  |  |
| 362 | Na_3CBO | small | todo | no parts |  |  |  |  |  |
| 363 | Na_3CBP | medium | todo | no parts |  |  |  |  |  |
| 364 | Na_3CBQ | small | todo | no parts |  |  |  |  |  |
| 365 | Na_3CBR | small | todo | no parts |  |  |  |  |  |
| 366 | Na_3CBS | small | todo | no parts |  |  |  |  |  |
| 367 | Na_3CBT | small | todo | no parts |  |  |  |  |  |
| 368 | Na_3CBU | small | todo | no parts |  |  |  |  |  |
| 369 | Na_3CBV | small | todo | no parts |  |  |  |  |  |
| 370 | Na_3CBW | small | todo | tree |  |  |  |  |  |
| 371 | Na_3CBX | small | todo | no parts |  |  |  |  |  |
| 372 | Na_3CBY | small | todo | tree |  |  |  |  |  |
| 373 | Na_3CBZ | small | todo | no parts |  |  |  |  |  |
| 374 | Sh_3CCh_ | small | todo | no parts |  |  |  |  |  |
| 375 | Sh_3CCi_ | small | todo | no parts |  |  |  |  |  |
| 376 | Sh_3CCj_ | small | todo | no parts |  |  |  |  |  |
| 377 | Sh_3CCl_ | small | todo | no parts |  |  |  |  |  |
| 378 | Sh_3CCm_ | medium | todo | tree |  |  |  |  |  |
| 379 | Sh_3CCn_ | small | todo | no parts |  |  |  |  |  |
| 380 | Sh_3CCp_ | small | todo | tree |  |  |  |  |  |
| 381 | Sh_3CCq_ | small | todo | no parts |  |  |  |  |  |
| 382 | Sh_3CCr_ | small | todo | tree |  |  |  |  |  |
| 383 | Sh_3CCu_ | small | todo | tree |  |  |  |  |  |
| 384 | Sh_3CCv_ | small | todo | no parts |  |  |  |  |  |
| 385 | Sh_3CCx_ | small | todo | no parts |  |  |  |  |  |
| 386 | Sh_3CCy_ | small | todo | tree |  |  |  |  |  |
| 387 | Sh_3CCz_ | small | todo | tree |  |  |  |  |  |
| 388 | Sh_3CD1 | medium | todo | tree |  |  |  |  |  |
| 389 | Sh_3CD2 | medium | todo | tree |  |  |  |  |  |
| 390 | Sh_3CD3 | medium | todo | tree |  |  |  |  |  |
| 391 | Sh_3CD4 | medium | todo | tree |  |  |  |  |  |
| 392 | Sh_3CD5 | small | todo | tree |  |  |  |  |  |
| 393 | Sh_3CD6 | medium | todo | tree |  |  |  |  |  |
| 394 | Sh_3CD7 | medium | todo | tree |  |  |  |  |  |
| 395 | Sh_3CD8 | medium | todo | tree |  |  |  |  |  |
| 396 | Sh_3CDA | small | todo | no parts |  |  |  |  |  |
| 397 | Sh_3CDF | small | todo | tree |  |  |  |  |  |
| 398 | Sh_3CFZ | medium | todo | tree |  |  |  |  |  |
| 399 | Va_3CE0 | small | todo | no parts |  |  |  |  |  |
| 400 | Va_3CEa_ | small | todo | tree |  |  |  |  |  |
| 401 | Va_3CEb_ | small | todo | no parts |  |  |  |  |  |
| 402 | Va_3CEc_ | small | todo | tree |  |  |  |  |  |
| 403 | Va_3CEd_ | small | todo | no parts |  |  |  |  |  |
| 404 | Va_3CEL | small | todo | tree |  |  |  |  |  |
| 405 | Va_3CEM | small | todo | no parts |  |  |  |  |  |
| 406 | Va_3CEO | small | todo | tree |  |  |  |  |  |
| 407 | Va_3CEP | small | todo | tree |  |  |  |  |  |
| 408 | Va_3CEQ | medium | todo | no parts |  |  |  |  |  |
| 409 | Va_3CES | medium | todo | tree |  |  |  |  |  |
| 410 | Va_3CET | small | todo | tree |  |  |  |  |  |
| 411 | Va_3CEX | medium | todo | tree |  |  |  |  |  |
| 412 | Va_3CEY | small | todo | tree |  |  |  |  |  |
| 413 | As_3CDk_ | large | done | tree | 0 not placed | 599 | medium · $0.53 · 10.4 min |  | `processed/root-gemini/As_3CDk_-prose.md` |
| 414 | As_3CDl_ | large | done | tree | 0 not placed | 1733 | medium · $1.37 · 26.2 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/As_3CDl_-prose.md` |
| 415 | As_3CDm_ | large | done | tree | 0 not placed | 1073 | medium · $0.96 · 16.4 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/As_3CDm_-prose.md` |
| 416 | As_3CDn_ | large | done | tree | 0 not placed | 1074 | medium · $1.04 · 17.9 min |  | `processed/root-gemini/As_3CDn_-prose.md` |
| 417 | As_3CDo_ | large | done | tree | 0 not placed | 1460 | medium · $1.21 · 22.0 min |  | `processed/root-gemini/As_3CDo_-prose.md` |
| 418 | As_3CDp_ | large | done | tree | 0 not placed | 1314 | medium · $1.12 · 14.9 min | breaks-review.md: raw breaks ending mid-sentence | `processed/root-gemini/As_3CDp_-prose.md` |
| 419 | As_3CDq_ | large | running | tree |  |  | started 23:17 |  |  |
| 420 | As_3CDv_ | large | running | tree |  |  | started 23:27 |  |  |
| 421 | At_3CHK | large | todo | tree |  |  |  |  |  |
| 422 | Dh_3CF5 | large | todo | tree |  |  |  |  |  |
| 423 | Dh_3CF6 | large | todo | tree |  |  |  |  |  |
| 424 | Gu_3CFS | large | todo | tree |  |  |  |  |  |
| 425 | Gu_3CFT | large | todo | tree |  |  |  |  |  |
| 426 | Ha_3CFF | large | todo | tree |  |  |  |  |  |
| 427 | Ha_3CFG | large | todo | tree |  |  |  |  |  |
| 428 | Ha_3CFH | large | todo | tree |  |  |  |  |  |
| 429 | Ha_3CFI | large | todo | tree |  |  |  |  |  |
| 430 | Ka_3CDK | large | todo | no parts |  |  |  |  |  |
| 431 | Na_3CB4 | large | todo | tree |  |  |  |  |  |
| 432 | Sh_3CCs_ | large | todo | tree |  |  |  |  |  |
| 433 | Sh_3CCt_ | large | todo | tree |  |  |  |  |  |
| 434 | Sh_3CDE | large | todo | tree |  |  |  |  |  |
| 435 | Va_3CER | large | todo | tree |  |  |  |  |  |
| 436 | Ha_3CFJ | large | done | tree | 0 not placed | 772 | medium · $0.75 · 11.8 min |  | `processed/root-gemini/Ha_3CFJ-prose.md` |
