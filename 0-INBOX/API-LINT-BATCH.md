# Root-text API batch — linter + parser

Runs `linter-root-text` then `parser-root-text` on every root text in `1-SOURCES/Text/`. How to run: the docstring of `0-INBOX/temp/api-lint/run_lint_batch.py`.

Updated 2026-10-27 · 442 texts (small 358 · medium 60 · large 24) · done 441 · failed 0 · **held 6** · to do 0 · **uploaded 436**

| What | Path |
|---|---|
| Status (one entry per text) | `0-INBOX/temp/api-lint/lint-status.json` |
| **Held texts — never run** (edit to release) | `0-INBOX/temp/api-lint/holds.json` |
| Log per text | `0-INBOX/temp/api-lint/logs/<id>.log` |
| Lint result | `4-SYSTEM/scripts/linter-root-text/output/<id>.lint.json` (or `.lint.errors.json`) |
| API payloads | `4-SYSTEM/scripts/parser-root-text/output/<id>/` (text, edition, toc, yigchungs, durchens) |
| Why the durchen texts are held | `0-INBOX/durchen-outliers-report.md` |
| Upload (script; ledger with every id) | `0-INBOX/temp/api-lint/run_upload_batch.py` · `0-INBOX/temp/api-lint/upload-status.json` |
| Titles changed to clear a title clash | `0-INBOX/temp/api-lint/retitled.json` |

`lint` OK = no errors · `err` / `warn` = linter errors / warnings (the language-list notice not counted) · `dur. warn` = footnote warnings (lemma not matched) · `src changed` = the linter rewrote the source frontmatter. Size from `0-INBOX/ROOT-WORKFLOW-BATCH.md`.

Upload columns: `upload` = uploaded / partial / failed · `text_id` = the id written into the source frontmatter · `ed.` / `toc` ✓ = created (`edition_id` / `toc_id` in the frontmatter) · `dur. up` / `yig. up` = notes sent / notes in the payload.

| # | id | size | chars | status | lint | err | warn | dur. warn | parse | segments | durchens | toc nodes | src changed | upload | text_id | ed. | toc | dur. up | yig. up | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ar_3CBa_ | medium | 109,595 | done | OK | 0 | 1 | 0 | OK | 637 | 445 | 33 | no | uploaded | 4F3fLiT6ZvPqDpgbrB9Ci | ✓ | ✓ | 445/445 |  |  |
| 2 | Ar_3CBc_ | medium | 192,040 | done | OK | 0 | 2 | 0 | OK | 623 | 572 | 16 | no | uploaded | jhtsov3TZAjnUl934c1sb | ✓ | ✓ | 572/572 |  |  |
| 3 | Ar_3CBe_ | small | 6,656 | done | OK | 0 | 2 | 0 | OK | 36 | 38 | 8 | no | uploaded | L3ST2FgFYWRkhBEpx2uab | ✓ | ✓ | 38/38 |  |  |
| 4 | Ar_3CBf_ | small | 4,138 | done | OK | 0 | 1 | 0 | OK | 17 | 11 | 6 | no | uploaded | ZDwz6Ib9GFU6HU5WlSvZr | ✓ | ✓ | 11/11 |  |  |
| 5 | Ar_3CBg_ | medium | 35,471 | done | OK | 0 | 2 | 0 | OK | 190 | 121 | 10 | no | uploaded | ZM95XEJkBt6VwCqWVZxSW | ✓ | ✓ | 121/121 |  |  |
| 6 | Ar_3CBh_ | medium | 40,614 | done | OK | 0 | 2 | 0 | OK | 138 | 188 | 11 | no | uploaded | zV1Ny1svv4LDusoiFfvAd | ✓ | ✓ | 188/188 |  |  |
| 7 | Ar_3CBi_ | small | 21,208 | done | OK | 0 | 3 | 1 | OK | 134 | 75 | 6 | no | uploaded | CPHehmylOiPTOfn5vyOuD | ✓ | ✓ | 75/75 |  |  |
| 8 | Ar_3CBj_ | small | 10,198 | done | OK | 0 | 2 | 0 | OK | 57 | 28 | 5 | no | uploaded | 5DhL75Gp7PyaR49U9hUcS | ✓ | ✓ | 28/28 |  |  |
| 9 | Ar_3CBk_ | small | 10,824 | done | OK | 0 | 1 | 0 | OK | 58 | 41 | 7 | no | uploaded | aFvwuFSoj5GtnZz30rlXv | ✓ | ✓ | 41/41 |  |  |
| 10 | Ar_3CBl_ | small | 7,042 | done | OK | 0 | 2 | 0 | OK | 50 | 25 | 10 | no | uploaded | czhSRGDZlm4CDHCcPjxHQ | ✓ | ✓ | 25/25 |  |  |
| 11 | Ar_3CBm_ | small | 11,939 | done | OK | 0 | 1 | 0 | OK | 76 | 33 | 8 | no | uploaded | WzmhTJuu3HCVDN3EIvjkI | ✓ | ✓ | 33/33 |  |  |
| 12 | Ar_3CBn_ | small | 3,353 | done | OK | 0 | 2 | 0 | OK | 18 | 7 | 6 | no | uploaded | pyeb9zpoSDOtU46mn9c40 | ✓ | ✓ | 7/7 |  |  |
| 13 | Ar_3CBo_ | small | 18,365 | done | OK | 0 | 2 | 0 | OK | 106 | 49 | 6 | no | uploaded | 2hIw2s3BhvIluA9MFvl6I | ✓ | ✓ | 49/49 |  |  |
| 14 | Ar_3CBp_ | small | 13,124 | done | OK | 0 | 2 | 0 | OK | 46 | 57 | 13 | no | uploaded | encpoWoRKWzfeerIy998U | ✓ | ✓ | 57/57 |  |  |
| 15 | Ar_3CBq_ | small | 14,593 | done | OK | 0 | 1 | 0 | OK | 45 | 69 | 5 | no | uploaded | 8BaAsCZI0Y1CYeR3S23Sn | ✓ | ✓ | 69/69 |  |  |
| 16 | Ar_3CBr_ | small | 4,336 | done | OK | 0 | 4 | 2 | OK | 21 | 4 | 5 | no | uploaded | XLROEy9SkjdHMELSQLdgM | ✓ | ✓ | 4/4 |  |  |
| 17 | Ar_3CBs_ | small | 13,398 | done | OK | 0 | 3 | 1 | OK | 31 | 22 | 10 | no | uploaded | iK3Ql7zzTdLrYfaxI1IMP | ✓ | ✓ | 22/22 |  |  |
| 18 | Ar_3CBt_ | small | 3,307 | done | OK | 0 | 2 | 0 | OK | 9 | 0 | 5 | no | uploaded | S0neZermDFiPjv4wbdBof | ✓ | ✓ | 0/0 |  |  |
| 19 | Ar_3CBu_ | small | 5,260 | done | OK | 0 | 2 | 0 | OK | 23 | 3 | 5 | no | uploaded | FOOGvOhIt04351ltaudYi | ✓ | ✓ | 3/3 |  |  |
| 20 | Ar_3CBv_ | small | 4,276 | done | OK | 0 | 2 | 0 | OK | 9 | 1 | 6 | no | uploaded | UFwBW9yoCVuvgXHYMZoy9 | ✓ | ✓ | 1/1 |  |  |
| 21 | Ar_3CBw_ | small | 4,784 | done | OK | 0 | 2 | 0 | OK | 27 | 3 | 3 | no | uploaded | 8GobLfF0DGzPkpoGbaC0b | ✓ | ✓ | 3/3 |  |  |
| 22 | Ar_3CBx_ | small | 3,068 | done | OK | 0 | 3 | 1 | OK | 18 | 1 | 14 | no | uploaded | pUP7NHS69gi0Tfra6ec1W | ✓ | ✓ | 1/1 |  |  |
| 23 | Ar_3CBy_ | small | 2,579 | done | OK | 0 | 2 | 0 | OK | 11 | 2 | 6 | no | uploaded | ZEQmS0BkpJHCBmNnfoj1y | ✓ | ✓ | 2/2 |  |  |
| 24 | Ar_3CBz_ | small | 2,425 | done | OK | 0 | 1 | 0 | OK | 11 | 9 | 6 | no | uploaded | cqpHDkj30ct8GfCma4ufR | ✓ | ✓ | 9/9 |  |  |
| 25 | Ar_3CC1 | medium | 69,468 | done | OK | 0 | 1 | 0 | OK | 426 | 389 | 20 | no | uploaded | SAW38UfEmuRYTt4rDomym | ✓ | ✓ | 389/389 |  |  |
| 26 | Ar_3CC2 | small | 13,377 | done | OK | 0 | 2 | 0 | OK | 51 | 37 | 16 | no | uploaded | V51V3ga71RtKCVaryl8C3 | ✓ | ✓ | 37/37 |  |  |
| 27 | Ar_3CC3 | small | 1,895 | done | OK | 0 | 2 | 0 | OK | 10 | 3 | 5 | no | uploaded | Fj3XA5lBa7idF3wI7ZKS6 | ✓ | ✓ | 3/3 |  |  |
| 28 | Ar_3CC5 | small | 8,486 | done | OK | 0 | 2 | 0 | OK | 20 | 20 | 8 | no | uploaded | TxrvC8Fk4GaCAtnFqBehd | ✓ | ✓ | 20/20 |  |  |
| 29 | Ar_3CC6 | small | 6,524 | done | OK | 0 | 2 | 0 | OK | 41 | 13 | 12 | no | uploaded | jCXrec9ODNwQLhw6fUspf | ✓ | ✓ | 13/13 |  |  |
| 30 | Ar_3CC7 | small | 9,163 | done | OK | 0 | 4 | 3 | OK | 43 | 25 | 5 | no | uploaded | orZ6EcRDvzOhXE0INGnPn | ✓ | ✓ | 25/25 |  |  |
| 31 | Ar_3CC8 | small | 3,882 | done | OK | 0 | 1 | 0 | OK | 18 | 0 | 5 | no | uploaded | alMdVc6jGHbR6OiA08eYC | ✓ | ✓ | 0/0 |  |  |
| 32 | Ar_3CC9 | small | 2,818 | done | OK | 0 | 1 | 0 | OK | 13 | 0 | 5 | no | uploaded | Hgo2fqd3QsuZFYSh8oU2c | ✓ | ✓ | 0/0 |  |  |
| 33 | Ar_3CCA | small | 3,553 | done | OK | 0 | 1 | 0 | OK | 17 | 0 | 5 | no | uploaded | B00dbH164vrSqb9nGr7Hx | ✓ | ✓ | 0/0 |  |  |
| 34 | Ar_3CCB | small | 2,874 | done | OK | 0 | 1 | 0 | OK | 10 | 0 | 6 | no | uploaded | VAeISJ4pMg5H6loIy3r4r | ✓ | ✓ | 0/0 |  |  |
| 35 | As_3CDc_ | small | 3,810 | done | OK | 0 | 1 | 0 | OK | 22 | 5 | 6 | no | uploaded | F8ik7b0uAOiQOoNt45lAV | ✓ | ✓ | 5/5 |  |  |
| 36 | As_3CDd_ | small | 8,141 | done | OK | 0 | 7 | 5 | OK | 14 | 43 | 5 | no | uploaded | udEg2T5zWRjYYim0bUkHH | ✓ | ✓ | 43/43 |  |  |
| 37 | As_3CDe_ | small | 4,330 | done | OK | 0 | 2 | 0 | OK | 14 | 17 | 6 | no | uploaded | Y8NMcBJeBAGZU1qNDh864 | ✓ | ✓ | 17/17 |  |  |
| 38 | As_3CDk_ | large | 309,723 | done | OK | 0 | 2 | 0 | OK | 601 | 1044 | 6 | no | uploaded | QQpmPjMFFWOkXQraQ6i6T | ✓ | ✓ | 1044/1044 |  |  |
| 39 | As_3CDl_ | large | 724,282 | done | OK | 0 | 2 | 0 | OK | 1733 | 2260 | 11 | no | uploaded | 63kj31p9J5saliyvuD14z | ✓ | ✓ | 2260/2260 |  |  |
| 40 | As_3CDm_ | large | 785,594 | done | OK | 0 | 2 | 0 | OK | 1042 | 3616 | 8 | no | uploaded | VO7LalclRc0h8JVJnasmY | ✓ | ✓ | 3616/3616 |  |  |
| 41 | As_3CDn_ | large | 861,034 | done | OK | 0 | 2 | 0 | OK | 1074 | 3806 | 15 | no | uploaded | iePW4cSI1KvRXbZP1odVd | ✓ | ✓ | 3806/3806 |  |  |
| 42 | As_3CDo_ | large | 793,675 | done | OK | 0 | 2 | 1 | OK | 1461 | 3132 | 11 | no | uploaded | PTeAvbIVuWhNUWmDhTOvx | ✓ | ✓ | 3132/3132 |  | retitled (see Retitled) |
| 43 | As_3CDp_ | large | 786,128 | done | OK | 0 | 2 | 0 | OK | 1316 | 2768 | 9 | no | uploaded | g6QRO1ZIXB7UlHVjfwAzy | ✓ | ✓ | 2768/2768 |  |  |
| 44 | As_3CDq_ | large | 791,378 | done | OK | 0 | 1 | 0 | OK | 1266 | 2814 | 6 | no | uploaded | ByFjqCH33rl0DO9pNTnlt | ✓ | ✓ | 2814/2814 |  |  |
| 45 | As_3CDr_ | medium | 82,226 | done | OK | 0 | 2 | 0 | OK | 201 | 316 | 11 | no | uploaded | yuBW2IlmWGYm59zVKkvof | ✓ | ✓ | 316/316 |  |  |
| 46 | As_3CDs_ | medium | 105,147 | done | OK | 0 | 1 | 0 | OK | 219 | 435 | 4 | no | uploaded | R8RjEHoQTrfvLQ0JOqIY0 | ✓ | ✓ | 435/435 |  |  |
| 47 | As_3CDt_ | medium | 86,962 | done | OK | 0 | 1 | 0 | OK | 133 | 341 | 12 | no | uploaded | 3Hwx0gQq1mkH7vvPpOxIi | ✓ | ✓ | 341/341 |  |  |
| 48 | As_3CDu_ | medium | 171,634 | done | OK | 0 | 2 | 0 | OK | 432 | 722 | 15 | no | uploaded | 0IRuOSUQsb5ekznkVG0Nf | ✓ | ✓ | 722/722 |  |  |
| 49 | As_3CDv_ | large | 309,530 | done | OK | 0 | 1 | 0 | OK | 1044 | 1545 | 16 | no | uploaded | ocnUbqsbayWJ7yTtmHj9Y | ✓ | ✓ | 1545/1545 |  |  |
| 50 | As_3CDw_ | small | 26,610 | done | OK | 0 | 1 | 0 | OK | 97 | 122 | 20 | no | uploaded | YG7C9dajerCVWAVAr6Dzd | ✓ | ✓ | 122/122 |  |  |
| 51 | At_3CFb_ | small | 23,256 | done | OK | 0 | 2 | 0 | OK | 112 | 46 | 9 | no | uploaded | zb3jVYhLJvpDEO51yTxh8 | ✓ | ✓ | 46/46 |  |  |
| 52 | At_3CFc_ | small | 7,936 | done | OK | 0 | 1 | 0 | OK | 32 | 19 | 8 | no | uploaded | rkIzElSVih6GRThZsr7ym | ✓ | ✓ | 19/19 |  |  |
| 53 | At_3CFd_ | medium | 61,762 | done | OK | 0 | 1 | 0 | OK | 209 | 126 | 10 | no | uploaded | P6FSv6SHTzHts6G6lsqC5 | ✓ | ✓ | 126/126 |  |  |
| 54 | At_3CFe_ | small | 8,936 | done | OK | 0 | 2 | 0 | OK | 27 | 20 | 6 | no | uploaded | Wgk45WKLo8z3jgypi7Hmr | ✓ | ✓ | 20/20 |  |  |
| 55 | At_3CFf_ | small | 10,059 | done | OK | 0 | 1 | 0 | OK | 27 | 21 | 14 | no | uploaded | fmF3bWkMUAKO86yTxqM17 | ✓ | ✓ | 21/21 |  |  |
| 56 | At_3CFg_ | small | 3,897 | done | OK | 0 | 1 | 0 | OK | 8 | 12 | 5 | no | uploaded | uSEe0BLSYzEl99CEI4am9 | ✓ | ✓ | 12/12 |  |  |
| 57 | At_3CFh_ | small | 6,161 | done | OK | 0 | 2 | 0 | OK | 30 | 19 | 3 | no | uploaded | X4Txa9iyUiKyW6ODSAJvi | ✓ | ✓ | 19/19 |  |  |
| 58 | At_3CFj_ | small | 5,755 | done | OK | 0 | 2 | 0 | OK | 35 | 7 | 6 | no | uploaded | 8anx96WDUtTTtHj6VhrkM | ✓ | ✓ | 7/7 |  |  |
| 59 | At_3CFl_ | small | 3,573 | done | OK | 0 | 2 | 0 | OK | 16 | 7 | 6 | no | uploaded | V5vRDyBDyQryAaw1Zqn72 | ✓ | ✓ | 7/7 |  |  |
| 60 | At_3CFm_ | small | 6,984 | done | OK | 0 | 2 | 0 | OK | 17 | 42 | 5 | no | uploaded | jWwaT3kuQ6efoxP2wgk8E | ✓ | ✓ | 42/42 |  |  |
| 61 | At_3CFn_ | small | 4,907 | done | OK | 0 | 2 | 0 | OK | 14 | 16 | 5 | no | uploaded | ZlJwtJAsVxcLJ7fsSl2zc | ✓ | ✓ | 16/16 |  |  |
| 62 | At_3CFo_ | small | 3,895 | done | OK | 0 | 1 | 0 | OK | 17 | 16 | 6 | no | uploaded | Bqf2ZkUjGklqFPLGzWUYN | ✓ | ✓ | 16/16 |  |  |
| 63 | At_3CFp_ | small | 3,470 | **held** | OK | 0 | 2 | 0 | OK | 16 | 7 | 6 | no | **failed** |  |  |  |  |  | duplicate of At_3CFl_ (uploaded): identical main text and footnotes; same BDRC WA0RT4268, same volume (Book 98) |
| 64 | At_3CFq_ | small | 1,660 | done | OK | 0 | 1 | 0 | OK | 6 | 5 | 5 | no | uploaded | WbRmdvp8FLhFfIJElL9n7 | ✓ | ✓ | 5/5 |  |  |
| 65 | At_3CFr_ | small | 2,980 | done | OK | 0 | 1 | 0 | OK | 9 | 7 | 5 | no | uploaded | YMBiOLaK5MAbrzHMsVHaE | ✓ | ✓ | 7/7 |  |  |
| 66 | At_3CFs_ | small | 9,898 | done | OK | 0 | 1 | 0 | OK | 16 | 74 | 8 | no | uploaded | bzq5Tzvzvvn1D7giAs2Wh | ✓ | ✓ | 74/74 |  |  |
| 67 | At_3CFt_ | medium | 43,103 | done | OK | 0 | 1 | 0 | OK | 137 | 124 | 18 | no | uploaded | HbeMU2TruCrQx8kOpeL4u | ✓ | ✓ | 124/124 |  |  |
| 68 | At_3CFu_ | small | 5,604 | done | OK | 0 | 2 | 0 | OK | 28 | 11 | 8 | no | uploaded | Z1BciTiaznMz4jCh5wJKn | ✓ | ✓ | 11/11 |  |  |
| 69 | At_3CFv_ | small | 3,886 | done | OK | 0 | 2 | 0 | OK | 23 | 11 | 6 | no | uploaded | lB3YaqON7ZU69zYraU0Ch | ✓ | ✓ | 11/11 |  |  |
| 70 | At_3CFw_ | small | 3,519 | done | OK | 0 | 1 | 0 | OK | 15 | 11 | 3 | no | uploaded | 5M8ItbuINllQu2mooaJh3 | ✓ | ✓ | 11/11 |  |  |
| 71 | At_3CFx_ | small | 3,072 | done | OK | 0 | 2 | 0 | OK | 15 | 4 | 5 | no | uploaded | zuzpYegnRblOcTC1wbDVo | ✓ | ✓ | 4/4 |  |  |
| 72 | At_3CFy_ | small | 3,255 | done | OK | 0 | 1 | 0 | OK | 15 | 9 | 3 | no | uploaded | AmubAh8bcmnmZJZwfb6nD | ✓ | ✓ | 9/9 |  |  |
| 73 | At_3CFz_ | small | 3,296 | done | OK | 0 | 1 | 0 | OK | 16 | 8 | 5 | no | uploaded | GowuVjXVyeNGh3uHlw0ea | ✓ | ✓ | 8/8 |  |  |
| 74 | At_3CG0 | small | 7,704 | done | OK | 0 | 1 | 0 | OK | 32 | 34 | 6 | no | uploaded | X4IRyCWyZ3MkYAImED3nQ | ✓ | ✓ | 34/34 |  |  |
| 75 | At_3CG1 | small | 23,673 | done | OK | 0 | 1 | 0 | OK | 138 | 77 | 10 | no | uploaded | 4tykpOoaBgtcpwTTW0ere | ✓ | ✓ | 77/77 |  |  |
| 76 | At_3CG2 | small | 1,650 | done | OK | 0 | 1 | 0 | OK | 5 | 5 | 3 | no | uploaded | NaOCkJuCjHboSWClOXS0a | ✓ | ✓ | 5/5 |  |  |
| 77 | At_3CG3 | small | 3,282 | done | OK | 0 | 1 | 0 | OK | 14 | 11 | 8 | no | uploaded | beyDOFnqSb9zofcfqtBu6 | ✓ | ✓ | 11/11 |  |  |
| 78 | At_3CG4 | small | 2,948 | done | OK | 0 | 1 | 0 | OK | 11 | 10 | 5 | no | uploaded | ezBA9cEBh4kISMLGR9RmI | ✓ | ✓ | 10/10 |  |  |
| 79 | At_3CG5 | small | 21,663 | done | OK | 0 | 1 | 0 | OK | 89 | 113 | 7 | no | uploaded | xoTGSfn9kuP1qa8EupWZ9 | ✓ | ✓ | 113/113 |  |  |
| 80 | At_3CG6 | small | 6,538 | done | OK | 0 | 2 | 0 | OK | 24 | 29 | 9 | no | uploaded | VmshHUukFeIGspVJfsXND | ✓ | ✓ | 29/29 |  |  |
| 81 | At_3CG7 | small | 2,620 | done | OK | 0 | 1 | 0 | OK | 9 | 4 | 5 | no | uploaded | ZtzRO1z8ydu39Raaa24dG | ✓ | ✓ | 4/4 |  | retitled (see Retitled) |
| 82 | At_3CG8 | small | 3,306 | done | OK | 0 | 1 | 0 | OK | 13 | 13 | 7 | no | uploaded | Xgkbr8VHzlJXYiV3K9bzk | ✓ | ✓ | 13/13 |  |  |
| 83 | At_3CG9 | small | 9,463 | done | OK | 0 | 2 | 0 | OK | 27 | 52 | 9 | no | uploaded | WvYhV1irVFx3dCkuaXfNh | ✓ | ✓ | 52/52 |  |  |
| 84 | At_3CGA | small | 5,484 | done | OK | 0 | 2 | 0 | OK | 38 | 13 | 6 | no | uploaded | pMXozoVDatp9azkNiTWfC | ✓ | ✓ | 13/13 |  |  |
| 85 | At_3CGB | small | 12,953 | done | OK | 0 | 1 | 0 | OK | 23 | 61 | 6 | no | uploaded | sblarb0OHvJtUnRrBvBDu | ✓ | ✓ | 61/61 |  |  |
| 86 | At_3CGC | small | 3,909 | done | OK | 0 | 2 | 0 | OK | 17 | 9 | 5 | no | uploaded | rJP5ibF3Juqbih1QtgEyy | ✓ | ✓ | 9/9 |  |  |
| 87 | At_3CGD | small | 3,473 | done | OK | 0 | 1 | 0 | OK | 14 | 8 | 6 | no | uploaded | Yw93PTPSbqwRerDkZP5As | ✓ | ✓ | 8/8 |  |  |
| 88 | At_3CGE | small | 5,228 | done | OK | 0 | 2 | 0 | OK | 23 | 15 | 16 | no | uploaded | l7tnW2fEeUZWP3oGN3tM6 | ✓ | ✓ | 15/15 |  |  |
| 89 | At_3CGF | small | 3,289 | done | OK | 0 | 2 | 0 | OK | 18 | 7 | 7 | no | uploaded | 3uer2XGwajgM5fiuUZhDy | ✓ | ✓ | 7/7 |  |  |
| 90 | At_3CGG | small | 2,967 | done | OK | 0 | 1 | 0 | OK | 12 | 6 | 4 | no | uploaded | XsuQ2skFgkxhqsDSmeX9n | ✓ | ✓ | 6/6 |  |  |
| 91 | At_3CGH | small | 3,176 | done | OK | 0 | 1 | 0 | OK | 8 | 9 | 3 | no | uploaded | Sk9mTj5CSWwC6WrnDJqS4 | ✓ | ✓ | 9/9 |  |  |
| 92 | At_3CGI | small | 2,950 | done | OK | 0 | 1 | 0 | OK | 7 | 10 | 5 | no | uploaded | VJmj5rJ0Sk7sUfFSG1Ize | ✓ | ✓ | 10/10 |  | retitled (see Retitled) |
| 93 | At_3CGJ | small | 5,090 | done | OK | 0 | 1 | 0 | OK | 26 | 15 | 8 | no | uploaded | eKTzd8nsIz50stQNTveVJ | ✓ | ✓ | 15/15 |  |  |
| 94 | At_3CGK | small | 2,750 | done | OK | 0 | 1 | 0 | OK | 8 | 5 | 6 | no | uploaded | AobdNIMloreOgZOan0vP6 | ✓ | ✓ | 5/5 |  |  |
| 95 | At_3CGL | small | 3,000 | done | OK | 0 | 2 | 0 | OK | 15 | 12 | 6 | no | uploaded | kGlQSTCd7gv7ytQlcWIcf | ✓ | ✓ | 12/12 |  |  |
| 96 | At_3CGM | small | 6,869 | done | OK | 0 | 2 | 0 | OK | 19 | 34 | 7 | no | uploaded | ysn39XOcUH5TuA7WesuNs | ✓ | ✓ | 34/34 |  |  |
| 97 | At_3CGN | small | 23,458 | done | OK | 0 | 1 | 0 | OK | 83 | 103 | 26 | no | uploaded | JZopOSKK4zlgO0bYl3aVD | ✓ | ✓ | 103/103 |  |  |
| 98 | At_3CGO | small | 2,670 | done | OK | 0 | 1 | 0 | OK | 11 | 5 | 6 | no | uploaded | 8rVQGZ4zSHwhAi7Y0Xcn7 | ✓ | ✓ | 5/5 |  |  |
| 99 | At_3CGP | medium | 34,311 | done | OK | 0 | 1 | 0 | OK | 76 | 156 | 6 | no | uploaded | oWjTBmhilMLk6wmoAlsJl | ✓ | ✓ | 156/156 |  |  |
| 100 | At_3CGQ | small | 5,020 | done | OK | 0 | 1 | 0 | OK | 14 | 14 | 14 | no | uploaded | Ds5MnCvH1J4lvToC6IpUY | ✓ | ✓ | 14/14 |  |  |
| 101 | At_3CGR | small | 3,838 | done | OK | 0 | 1 | 0 | OK | 16 | 14 | 6 | no | uploaded | HBFKH2CsSq7GGDjGiqT2P | ✓ | ✓ | 14/14 |  |  |
| 102 | At_3CGS | small | 14,542 | done | OK | 0 | 1 | 0 | OK | 34 | 21 | 10 | no | uploaded | 469ZYkRrGfCO08NyCLwl0 | ✓ | ✓ | 21/21 |  |  |
| 103 | At_3CGT | small | 1,604 | done | OK | 0 | 1 | 0 | OK | 5 | 1 | 5 | no | uploaded | r3YWk4Sm1kgCFtoFa1nkp | ✓ | ✓ | 1/1 |  |  |
| 104 | At_3CGU | small | 3,189 | done | OK | 0 | 2 | 1 | OK | 8 | 3 | 5 | no | uploaded | yr6JWNH2Cbx1O5Sp54KPb | ✓ | ✓ | 3/3 |  |  |
| 105 | At_3CGV | small | 15,374 | done | OK | 0 | 2 | 0 | OK | 27 | 17 | 8 | no | uploaded | i0VWIpwhsgTVxXuyfr5Ch | ✓ | ✓ | 17/17 |  |  |
| 106 | At_3CGW | small | 7,677 | done | OK | 0 | 2 | 0 | OK | 12 | 20 | 2 | no | uploaded | G0dtxYZ9iQ78sSFb9bDMi | ✓ | ✓ | 20/20 |  |  |
| 107 | At_3CGX | small | 4,344 | done | OK | 0 | 2 | 0 | OK | 15 | 11 | 7 | no | uploaded | jJS4tXBEi07iIPEm7ElEl | ✓ | ✓ | 11/11 |  |  |
| 108 | At_3CGY | small | 5,036 | done | OK | 0 | 2 | 0 | OK | 18 | 11 | 17 | no | uploaded | SFPoixXeWY767jVzKqXSN | ✓ | ✓ | 11/11 |  |  |
| 109 | At_3CGZ | small | 4,028 | done | OK | 0 | 2 | 0 | OK | 6 | 9 | 5 | no | uploaded | vpmmYgT5QvOujtHCpEdxZ | ✓ | ✓ | 9/9 |  |  |
| 110 | At_3CGa_ | small | 4,923 | **held** | OK | 0 | 1 | 0 | OK | 15 | 14 | 14 | no | **failed** |  |  |  |  |  | duplicate of At_3CGQ (uploaded): identical main text and footnotes (one verse is split over three lines instead of one); same BDRC WA0RT2596, same volume (Book 98) |
| 111 | At_3CGb_ | small | 4,825 | done | OK | 0 | 2 | 1 | OK | 12 | 6 | 9 | no | uploaded | kOIoQg0pyL0HxvFWUHWqX | ✓ | ✓ | 6/6 |  | retitled (see Retitled) |
| 112 | At_3CGc_ | small | 5,341 | done | OK | 0 | 2 | 0 | OK | 11 | 12 | 8 | no | uploaded | 4FfYdoll3J3isQONFpQFk | ✓ | ✓ | 12/12 |  |  |
| 113 | At_3CGd_ | small | 3,884 | done | OK | 0 | 2 | 0 | OK | 13 | 2 | 13 | no | uploaded | PPN4hm8z9ItKk7fwQJcIM | ✓ | ✓ | 2/2 |  |  |
| 114 | At_3CGe_ | small | 3,777 | done | OK | 0 | 2 | 0 | OK | 8 | 4 | 4 | no | uploaded | 1koXHXuCFRHVx4c2rCO62 | ✓ | ✓ | 4/4 |  |  |
| 115 | At_3CGf_ | small | 4,653 | done | OK | 0 | 2 | 0 | OK | 8 | 10 | 5 | no | uploaded | Mdjxo4TCc6NLSd27VtPbK | ✓ | ✓ | 10/10 |  |  |
| 116 | At_3CGg_ | small | 6,362 | done | OK | 0 | 1 | 0 | OK | 13 | 13 | 7 | no | uploaded | Ica2tfyyVllRAzngI9qHa | ✓ | ✓ | 13/13 |  |  |
| 117 | At_3CGh_ | small | 4,367 | done | OK | 0 | 2 | 0 | OK | 11 | 11 | 4 | no | uploaded | ZrphPec8Hh6qKb4dYnlg4 | ✓ | ✓ | 11/11 |  |  |
| 118 | At_3CGi_ | small | 3,852 | done | OK | 0 | 2 | 0 | OK | 10 | 5 | 3 | no | uploaded | a3vDvc5UzdaJ9tYTTqUtB | ✓ | ✓ | 5/5 |  |  |
| 119 | At_3CGj_ | small | 11,493 | done | OK | 0 | 2 | 0 | OK | 34 | 17 | 5 | no | uploaded | IWCzT3lfAW9kj0EEQoyl3 | ✓ | ✓ | 17/17 |  |  |
| 120 | At_3CGk_ | small | 4,433 | done | OK | 0 | 1 | 0 | OK | 21 | 3 | 3 | no | uploaded | aOIripKjNpNLOP2A8Zoye | ✓ | ✓ | 3/3 |  |  |
| 121 | At_3CGl_ | small | 2,639 | done | OK | 0 | 2 | 0 | OK | 10 | 3 | 8 | no | uploaded | F8Rn23PZC3Gk3RaO8jUbT | ✓ | ✓ | 3/3 |  |  |
| 122 | At_3CGm_ | small | 4,268 | done | OK | 0 | 2 | 0 | OK | 19 | 7 | 4 | no | uploaded | NLptgng3V7j3XIPGLojEc | ✓ | ✓ | 7/7 |  |  |
| 123 | At_3CGn_ | small | 4,961 | done | OK | 0 | 2 | 0 | OK | 16 | 2 | 4 | no | uploaded | uNMpgxXuRS5OQ6p9z9OpN | ✓ | ✓ | 2/2 |  |  |
| 124 | At_3CGo_ | small | 2,623 | done | OK | 0 | 2 | 0 | OK | 10 | 1 | 5 | no | uploaded | dffdNDzK1MqDSnGRdyeHc | ✓ | ✓ | 1/1 |  |  |
| 125 | At_3CGp_ | small | 2,108 | done | OK | 0 | 1 | 0 | OK | 9 | 1 | 4 | no | uploaded | Yq8vx5UvqnhMx3soVqtIK | ✓ | ✓ | 1/1 |  |  |
| 126 | At_3CGq_ | medium | 42,859 | done | OK | 0 | 1 | 0 | OK | 165 | 259 | 9 | no | uploaded | 8wwOA682tUjQc4P5pjEZP | ✓ | ✓ | 259/259 |  |  |
| 127 | At_3CGs_ | small | 5,510 | done | OK | 0 | 1 | 0 | OK | 31 | 11 | 8 | no | uploaded | jKrc5HsSwkCMGwPWrX2ty | ✓ | ✓ | 11/11 |  |  |
| 128 | At_3CGt_ | small | 4,031 | done | OK | 0 | 1 | 0 | OK | 18 | 9 | 8 | no | uploaded | aNwMPCBba0I7kwqREKwfK | ✓ | ✓ | 9/9 |  |  |
| 129 | At_3CGu_ | small | 5,149 | done | OK | 0 | 1 | 0 | OK | 12 | 22 | 8 | no | uploaded | Gfw4KPZ2eaVUNPsWwWGK8 | ✓ | ✓ | 22/22 |  |  |
| 130 | At_3CGv_ | medium | 79,405 | done | OK | 0 | 1 | 0 | OK | 232 | 298 | 22 | no | uploaded | ZhRTHgJUh6gDe4syFBr3k | ✓ | ✓ | 298/298 |  |  |
| 131 | At_3CGx_ | small | 5,947 | done | OK | 0 | 2 | 0 | OK | 32 | 28 | 5 | no | uploaded | fqo4UsewCy1mWwAbDPv1P | ✓ | ✓ | 28/28 |  |  |
| 132 | At_3CGy_ | small | 11,382 | done | OK | 0 | 2 | 0 | OK | 66 | 28 | 8 | no | uploaded | cqPOW3F25Cxc8GEtaVzLv | ✓ | ✓ | 28/28 |  |  |
| 133 | At_3CH0 | small | 3,068 | done | OK | 0 | 2 | 0 | OK | 15 | 4 | 6 | no | uploaded | vu080teLnoM5INsDwkKmF | ✓ | ✓ | 4/4 |  |  |
| 134 | At_3CH1 | small | 5,142 | done | OK | 0 | 2 | 0 | OK | 23 | 18 | 7 | no | uploaded | 2ep5DCo64XOHN9EVJ5g89 | ✓ | ✓ | 18/18 |  |  |
| 135 | At_3CH2 | small | 5,221 | done | OK | 0 | 2 | 0 | OK | 45 | 15 | 3 | no | uploaded | sqgqMqVU4WB3RTRe6EKxu | ✓ | ✓ | 15/15 |  |  |
| 136 | At_3CH3 | small | 8,269 | done | OK | 0 | 2 | 0 | OK | 23 | 34 | 6 | no | uploaded | JmwNie6DNnp6gztoxiDrK | ✓ | ✓ | 34/34 |  |  |
| 137 | At_3CH4 | small | 6,416 | done | OK | 0 | 2 | 0 | OK | 31 | 21 | 20 | no | uploaded | qKnfmZxsnIAju6u8tbt0t | ✓ | ✓ | 21/21 |  |  |
| 138 | At_3CH5 | small | 15,903 | done | OK | 0 | 2 | 0 | OK | 69 | 76 | 8 | no | uploaded | x7OS8yLXTAuwpDYyQlZko | ✓ | ✓ | 76/76 |  |  |
| 139 | At_3CH6 | small | 2,964 | done | OK | 0 | 2 | 0 | OK | 16 | 12 | 6 | no | uploaded | WkFE69m9yi5B75gpzeYuO | ✓ | ✓ | 12/12 |  |  |
| 140 | At_3CH7 | small | 4,917 | done | OK | 0 | 1 | 0 | OK | 26 | 14 | 9 | no | uploaded | NqHEFDNUBJ7AYog00Tstv | ✓ | ✓ | 14/14 |  |  |
| 141 | At_3CH8 | small | 10,726 | done | OK | 0 | 1 | 0 | OK | 21 | 43 | 8 | no | uploaded | s7orjqbMDxC5DExlMoj5Y | ✓ | ✓ | 43/43 |  |  |
| 142 | At_3CH9 | small | 5,112 | done | OK | 0 | 2 | 0 | OK | 19 | 19 | 8 | no | uploaded | TudDBkzyyF3R6KTcrusII | ✓ | ✓ | 19/19 |  |  |
| 143 | At_3CHA | small | 20,654 | done | OK | 0 | 2 | 0 | OK | 69 | 88 | 11 | no | uploaded | G0kj4K8dMPcLg0QlETGS0 | ✓ | ✓ | 88/88 |  |  |
| 144 | At_3CHB | small | 4,661 | done | OK | 0 | 1 | 0 | OK | 25 | 10 | 10 | no | uploaded | WiTiQOYfB9xc0T4ZuPZEL | ✓ | ✓ | 10/10 |  | retitled (see Retitled) |
| 145 | At_3CHC | small | 13,761 | done | OK | 0 | 2 | 0 | OK | 31 | 36 | 10 | no | uploaded | w3oF4wKG7X7QSQAbDjDRz | ✓ | ✓ | 36/36 |  |  |
| 146 | At_3CHD | small | 4,391 | done | OK | 0 | 1 | 0 | OK | 6 | 2 | 6 | no | uploaded | vN0L4Gbd4yKRJlq5523AP | ✓ | ✓ | 2/2 |  |  |
| 147 | At_3CHE | small | 2,834 | done | OK | 0 | 1 | 0 | OK | 6 | 13 | 5 | no | uploaded | cc9zjZQJ2cLAWKkvemUoF | ✓ | ✓ | 13/13 |  |  |
| 148 | At_3CHF | small | 3,034 | done | OK | 0 | 1 | 0 | OK | 11 | 14 | 6 | no | uploaded | htmfPrMYjfQGpUGNWgBd6 | ✓ | ✓ | 14/14 |  |  |
| 149 | At_3CHG | small | 3,373 | done | OK | 0 | 2 | 0 | OK | 9 | 13 | 5 | no | uploaded | eg3Nnh5x20aqrAEibknXD | ✓ | ✓ | 13/13 |  |  |
| 150 | At_3CHH | small | 21,327 | done | OK | 0 | 2 | 0 | OK | 45 | 91 | 13 | no | uploaded | nW13iRrxE99HxkoVeWi0f | ✓ | ✓ | 91/91 |  |  |
| 151 | At_3CHI | small | 7,997 | done | OK | 0 | 1 | 0 | OK | 62 | 31 | 5 | no | uploaded | goX1QGRHwWXJ8l9btguGU | ✓ | ✓ | 31/31 |  |  |
| 152 | At_3CHJ | small | 2,232 | done | OK | 0 | 1 | 0 | OK | 13 | 5 | 5 | no | uploaded | BVYEiQ5NeZYcI9NzdcPej | ✓ | ✓ | 5/5 |  |  |
| 153 | At_3CHK | large | 823,053 | done | OK | 0 | 3 | 1 | OK | 1575 | 3805 | 31 | no | uploaded | nJvofhnxmVSGqPI6qx3OT | ✓ | ✓ | 3805/3805 |  |  |
| 154 | At_3CHL | medium | 72,525 | done | OK | 0 | 1 | 0 | OK | 420 | 276 | 14 | no | uploaded | 80TBlQ74VgC0EKWhzXIyX | ✓ | ✓ | 276/276 |  | retitled (see Retitled) |
| 155 | At_3CHM | small | 5,858 | done | OK | 0 | 1 | 0 | OK | 24 | 27 | 8 | no | uploaded | obCsnBreIKkrPqBdkFZmI | ✓ | ✓ | 27/27 |  |  |
| 156 | At_3CHN | small | 4,083 | done | OK | 0 | 3 | 1 | OK | 7 | 11 | 5 | no | uploaded | D7fdkR3HBna7QsYh9UdpS | ✓ | ✓ | 11/11 |  |  |
| 157 | At_3CHO | small | 6,139 | done | OK | 0 | 1 | 0 | OK | 16 | 21 | 5 | no | uploaded | h3EDvNz8FjzIBOZvPl02j | ✓ | ✓ | 21/21 |  |  |
| 158 | At_3CHP | small | 6,757 | done | OK | 0 | 1 | 0 | OK | 15 | 31 | 5 | no | uploaded | 6tzfkSBpJqMBcuqh5M7h2 | ✓ | ✓ | 31/31 |  |  |
| 159 | At_3CHQ | small | 6,020 | done | OK | 0 | 1 | 0 | OK | 17 | 21 | 5 | no | uploaded | ihuRtnh00DBQL5CxEesVu | ✓ | ✓ | 21/21 |  |  |
| 160 | At_3CHR | small | 6,442 | done | OK | 0 | 2 | 0 | OK | 14 | 26 | 9 | no | uploaded | bTdOJefSCgoMBcb9d1J9D | ✓ | ✓ | 26/26 |  |  |
| 161 | At_3CHS | small | 2,568 | done | OK | 0 | 2 | 0 | OK | 3 | 9 | 5 | no | uploaded | 0BBbF2azDit1Z48UZ3Cgm | ✓ | ✓ | 9/9 |  |  |
| 162 | At_3CHT | small | 2,632 | done | OK | 0 | 2 | 0 | OK | 6 | 10 | 5 | no | uploaded | 0pbMOeMf6PzTriNUNZ6Nf | ✓ | ✓ | 10/10 |  |  |
| 163 | At_3CHU | small | 2,359 | done | OK | 0 | 1 | 0 | OK | 6 | 6 | 5 | no | uploaded | 3IICZacVBYQA5oPx0QCh8 | ✓ | ✓ | 6/6 |  |  |
| 164 | At_3CHV | small | 4,527 | done | OK | 0 | 2 | 0 | OK | 7 | 28 | 7 | no | uploaded | kptfC2w33ZzVcC8fBfXCW | ✓ | ✓ | 28/28 |  |  |
| 165 | At_3CHW | small | 1,860 | done | OK | 0 | 2 | 0 | OK | 6 | 2 | 5 | no | uploaded | ZvdPnlbVdNrI3pBSFstmF | ✓ | ✓ | 2/2 |  |  |
| 166 | At_3CHX | small | 4,334 | done | OK | 0 | 2 | 0 | OK | 18 | 13 | 5 | no | uploaded | VvfqG36nfyJ7huTY383Ta | ✓ | ✓ | 13/13 |  |  |
| 167 | At_3CHY | small | 2,043 | done | OK | 0 | 2 | 0 | OK | 6 | 11 | 5 | no | uploaded | g6lsDq8CApck7JYzful1p | ✓ | ✓ | 11/11 |  |  |
| 168 | At_3CHZ | small | 3,121 | done | OK | 0 | 1 | 0 | OK | 9 | 15 | 5 | no | uploaded | elqVqwKVyZJV0RBYSyeXa | ✓ | ✓ | 15/15 |  |  |
| 169 | At_3CHa_ | small | 4,268 | done | OK | 0 | 2 | 0 | OK | 17 | 15 | 6 | no | uploaded | LlncQng2CM4nYcLh9ccv8 | ✓ | ✓ | 15/15 |  |  |
| 170 | At_3CHb_ | small | 2,293 | done | OK | 0 | 2 | 0 | OK | 6 | 5 | 5 | no | uploaded | a56wyI0Gi6CkvGGmx0oWv | ✓ | ✓ | 5/5 |  |  |
| 171 | At_3CHc_ | small | 5,976 | done | OK | 0 | 1 | 0 | OK | 26 | 16 | 6 | no | uploaded | mpWs2IkWxHDm6znj6iT8t | ✓ | ✓ | 16/16 |  |  |
| 172 | At_3CHd_ | small | 3,563 | done | OK | 0 | 2 | 0 | OK | 8 | 16 | 5 | no | uploaded | cvSPLdrdCDUDKQ3G4gQdy | ✓ | ✓ | 16/16 |  |  |
| 173 | At_3CHe_ | small | 2,267 | done | OK | 0 | 1 | 0 | OK | 5 | 3 | 5 | no | uploaded | VOIwg245Y8Tg3fQ0XHjor | ✓ | ✓ | 3/3 |  |  |
| 174 | At_3CHf_ | small | 12,380 | done | OK | 0 | 1 | 0 | OK | 48 | 32 | 6 | no | uploaded | P2MiTVDLg93ZwRJUq2yoA | ✓ | ✓ | 32/32 |  |  |
| 175 | At_3CHg_ | small | 4,152 | done | OK | 0 | 2 | 0 | OK | 5 | 24 | 5 | no | uploaded | oZP2zxQdj6rQxUlDmGwrt | ✓ | ✓ | 24/24 |  |  |
| 176 | At_3CHh_ | small | 5,695 | done | OK | 0 | 1 | 0 | OK | 21 | 15 | 6 | no | uploaded | FfBozW65JBOlTB9NYZ2f6 | ✓ | ✓ | 15/15 |  |  |
| 177 | At_3CHi_ | small | 2,363 | done | OK | 0 | 1 | 0 | OK | 6 | 7 | 5 | no | uploaded | qK6ayFTlAhX4FVTJFLDtl | ✓ | ✓ | 7/7 |  |  |
| 178 | At_3CHj_ | small | 7,609 | done | OK | 0 | 2 | 0 | OK | 24 | 36 | 7 | no | uploaded | 39HBNoJuEq5cbwP92qSIp | ✓ | ✓ | 36/36 |  |  |
| 179 | At_3CHk_ | small | 9,502 | done | OK | 0 | 1 | 0 | OK | 21 | 44 | 6 | no | uploaded | yv2iCfY5j0PQnToFCAVx9 | ✓ | ✓ | 44/44 |  |  |
| 180 | At_3CHl_ | small | 9,760 | done | OK | 0 | 1 | 0 | OK | 20 | 42 | 7 | no | uploaded | tzNRdPogqdagBLDifLk7C | ✓ | ✓ | 42/42 |  |  |
| 181 | At_3CHm_ | small | 10,814 | done | OK | 0 | 2 | 0 | OK | 21 | 47 | 14 | no | uploaded | 2eyWKkAmWFMpma1YdDLlI | ✓ | ✓ | 47/47 |  |  |
| 182 | At_3CHn_ | small | 22,634 | done | OK | 0 | 2 | 0 | OK | 65 | 114 | 16 | no | uploaded | K1k0SIHqIFzig0Ggou4Mi | ✓ | ✓ | 114/114 |  |  |
| 183 | At_3CHo_ | small | 2,990 | done | OK | 0 | 1 | 0 | OK | 12 | 8 | 5 | no | uploaded | 9kN1OeCZmIsUoBhsLp3tH | ✓ | ✓ | 8/8 |  |  |
| 184 | At_3CHp_ | small | 3,667 | done | OK | 0 | 1 | 0 | OK | 14 | 10 | 5 | no | uploaded | uiCGMlpdVBwlKqe3rArMN | ✓ | ✓ | 10/10 |  |  |
| 185 | At_3CHq_ | small | 3,683 | done | OK | 0 | 1 | 0 | OK | 17 | 11 | 5 | no | uploaded | KLqYkL1aDsUKohLmTZeA7 | ✓ | ✓ | 11/11 |  |  |
| 186 | At_3CHr_ | small | 3,562 | done | OK | 0 | 1 | 0 | OK | 19 | 4 | 5 | no | uploaded | 4YO8sQoqxRIRbSSBBFrWR | ✓ | ✓ | 4/4 |  |  |
| 187 | At_3CHs_ | small | 3,600 | done | OK | 0 | 2 | 0 | OK | 17 | 9 | 5 | no | uploaded | Y7oSog98fhwhLab5JvTOr | ✓ | ✓ | 9/9 |  |  |
| 188 | At_3CHt_ | small | 3,606 | done | OK | 0 | 1 | 0 | OK | 15 | 9 | 5 | no | uploaded | UI8y21V8v60Ea1iN3wNaI | ✓ | ✓ | 9/9 |  |  |
| 189 | At_3CHu_ | small | 3,511 | done | OK | 0 | 2 | 0 | OK | 21 | 5 | 8 | no | uploaded | qmVjPCHoauf69We8D4rTC | ✓ | ✓ | 5/5 |  |  |
| 190 | At_3CHv_ | small | 3,650 | done | OK | 0 | 1 | 0 | OK | 14 | 9 | 3 | no | uploaded | STJx4Gt6DhDQlUc2cRTr4 | ✓ | ✓ | 9/9 |  |  |
| 191 | At_3CHw_ | small | 3,114 | done | OK | 0 | 2 | 0 | OK | 17 | 6 | 5 | no | uploaded | ZTQeHDcKNEnqbMKv0lzRb | ✓ | ✓ | 6/6 |  |  |
| 192 | At_3CHy_ | small | 6,341 | done | OK | 0 | 1 | 0 | OK | 33 | 26 | 7 | no | uploaded | Ba3CXJTKvlIC5qkPRlnVs | ✓ | ✓ | 26/26 |  |  |
| 193 | At_3CHz_ | small | 3,809 | done | OK | 0 | 2 | 0 | OK | 8 | 9 | 5 | no | uploaded | qzHLlHfITVc5VJAykjYF7 | ✓ | ✓ | 9/9 |  |  |
| 194 | At_3CI0 | small | 3,470 | done | OK | 0 | 2 | 0 | OK | 6 | 14 | 5 | no | uploaded | FCQCaJHx2xfvd4RbmdrzI | ✓ | ✓ | 14/14 |  |  |
| 195 | At_3CI1 | small | 3,767 | done | OK | 0 | 1 | 0 | OK | 8 | 10 | 5 | no | uploaded | NKHGA9GASCbR5b92peiU3 | ✓ | ✓ | 10/10 |  |  |
| 196 | At_3CI2 | small | 3,864 | done | OK | 0 | 2 | 0 | OK | 7 | 14 | 5 | no | uploaded | txSD3Qsz9aGSrPgK0n99W | ✓ | ✓ | 14/14 |  |  |
| 197 | At_3CI3 | small | 4,359 | done | OK | 0 | 2 | 0 | OK | 5 | 19 | 5 | no | uploaded | 6OlAuKl3gB2LJioO1HhF5 | ✓ | ✓ | 19/19 |  |  |
| 198 | At_3CI4 | small | 6,467 | done | OK | 0 | 2 | 0 | OK | 10 | 24 | 5 | no | uploaded | SvDFsIMLecoug6QYFZ9Uh | ✓ | ✓ | 24/24 |  |  |
| 199 | At_3CI5 | small | 5,888 | done | OK | 0 | 2 | 0 | OK | 17 | 20 | 5 | no | uploaded | fOmj86aCFlnn8oIQbdX66 | ✓ | ✓ | 20/20 |  |  |
| 200 | At_3CI6 | small | 3,730 | done | OK | 0 | 2 | 0 | OK | 8 | 9 | 5 | no | uploaded | 4xSJ3pEepcBdZ6IGFFLnn | ✓ | ✓ | 9/9 |  |  |
| 201 | At_3CI7 | small | 17,025 | done | OK | 0 | 1 | 0 | OK | 36 | 87 | 6 | no | uploaded | HS4DCSM0Rug3a5W8Ig0yR | ✓ | ✓ | 87/87 |  |  |
| 202 | At_3CI8 | small | 6,119 | done | OK | 0 | 2 | 0 | OK | 29 | 15 | 9 | no | uploaded | XecdaEpC5AkUKbFpnSGxf | ✓ | ✓ | 15/15 |  |  |
| 203 | At_3CI9 | small | 2,284 | done | OK | 0 | 2 | 0 | OK | 9 | 4 | 6 | no | uploaded | YYFtjAhqxVoxJ8aOPg6BB | ✓ | ✓ | 4/4 |  |  |
| 204 | At_3CIA | small | 5,129 | done | OK | 0 | 2 | 0 | OK | 9 | 25 | 5 | no | uploaded | M9j9q2HjOq4Td0VQ2SSCC | ✓ | ✓ | 25/25 |  |  |
| 205 | Bh_3CCH | medium | 121,453 | done | OK | 0 | 1 | 0 | OK | 490 | 487 | 12 | no | uploaded | JZxC8nBxIcoU0WkoiOvQZ | ✓ | ✓ | 487/487 |  |  |
| 206 | Bh_3CCI | medium | 156,613 | done | OK | 0 | 1 | 0 | OK | 952 | 611 | 16 | no | uploaded | tdgf1ZvR64FQ8aqcxZt48 | ✓ | ✓ | 611/611 |  |  |
| 207 | Bh_3CCJ | small | 3,318 | done | OK | 0 | 3 | 1 | OK | 16 | 10 | 7 | no | uploaded | E2EAsSIgrSX5zzsqAgPAC | ✓ | ✓ | 10/10 |  |  |
| 208 | Bh_3CCK | medium | 32,351 | done | OK | 0 | 1 | 0 | OK | 53 | 152 | 8 | no | uploaded | biawaNa00iaPLuZ0hQypP | ✓ | ✓ | 152/152 |  |  |
| 209 | Bh_3CCO | small | 3,224 | **held** | OK | 0 | 3 | 1 | OK | 17 | 10 | 7 | no | **failed** |  |  |  |  |  | duplicate of Bh_3CCJ (uploaded): identical text and footnotes except one editorial heading (དམ་པའི་དོན། vs དོན་དམ།); same BDRC WA0RT3202; printed in Book 34 ཆ and Book 31 ག |
| 210 | Ch_3CCP | small | 2,535 | done | OK | 0 | 2 | 0 | OK | 12 | 5 | 5 | no | uploaded | 9f5EERECqUI3Ntje1bHHO | ✓ | ✓ | 5/5 |  |  |
| 211 | Ch_3CCR | medium | 34,663 | done | OK | 0 | 1 | 0 | OK | 131 | 105 | 9 | no | uploaded | EYqawxIsIeS56UOaKB7xs | ✓ | ✓ | 105/105 |  |  |
| 212 | Ch_3CCS | small | 6,763 | done | OK | 0 | 1 | 0 | OK | 21 | 24 | 9 | no | uploaded | Yr26Oeg7fRct1vD5FpTXw | ✓ | ✓ | 24/24 |  |  |
| 213 | Ch_3CCU | small | 1,477 | done | OK | 0 | 1 | 0 | OK | 5 | 0 | 2 | no | uploaded | xeFFei4oAvczmFMylI7xG | ✓ | ✓ | 0/0 |  | retitled (see Retitled) |
| 214 | Ch_3CCV | small | 8,332 | done | OK | 0 | 2 | 1 | OK | 27 | 18 | 5 | no | uploaded | IARirxx6epVNpdmThpEW0 | ✓ | ✓ | 18/18 |  |  |
| 215 | Ch_3CCX | medium | 102,512 | done | OK | 0 | 1 | 0 | OK | 233 | 318 | 8 | no | uploaded | ACmWFR7EOLCyAS2PEAEyV | ✓ | ✓ | 318/318 |  | retitled (see Retitled) |
| 216 | Ch_3CCZ | small | 10,833 | done | OK | 0 | 2 | 0 | OK | 72 | 25 | 6 | no | uploaded | FupDtWCtILwxJ1Mdzeiwf | ✓ | ✓ | 25/25 |  |  |
| 217 | Ch_3CCc_ | medium | 57,365 | done | OK | 0 | 2 | 0 | OK | 335 | 7 | 14 | no | uploaded | Vsd56G9qyrX3J7swTYgDK | ✓ | ✓ | 7/7 |  |  |
| 218 | Ch_3CCd_ | medium | 66,337 | done | OK | 0 | 1 | 0 | OK | 328 | 195 | 14 | no | uploaded | 7SEP9SJUIhJUvECwH31AV | ✓ | ✓ | 195/195 |  |  |
| 219 | Ch_3CCf_ | small | 4,546 | done | OK | 0 | 1 | 0 | OK | 20 | 24 | 7 | no | uploaded | DIEfkAnKUrZ71uTWXTezv | ✓ | ✓ | 24/24 |  |  |
| 220 | Dh_3CEy_ | small | 3,705 | done | OK | 0 | 2 | 0 | OK | 14 | 8 | 5 | no | uploaded | hxhekmTAK0LlUbpI1aqCi | ✓ | ✓ | 8/8 |  |  |
| 221 | Dh_3CF0 | small | 7,337 | done | OK | 0 | 1 | 0 | OK | 8 | 23 | 6 | no | uploaded | yYBc1qr9qZTxYwcQPjQVD | ✓ | ✓ | 23/23 |  |  |
| 222 | Dh_3CF1 | small | 2,177 | done | OK | 0 | 1 | 0 | OK | 10 | 2 | 4 | no | uploaded | eMLnKHsf69MXpKFJNlLTt | ✓ | ✓ | 2/2 |  |  |
| 223 | Dh_3CF2 | medium | 85,326 | done | OK | 0 | 1 | 0 | OK | 251 | 429 | 20 | no | uploaded | tmOIAbbaEbQYSNiBi1nuR | ✓ | ✓ | 429/429 |  |  |
| 224 | Dh_3CF3 | small | 9,476 | done | OK | 0 | 6 | 4 | OK | 22 | 39 | 5 | no | uploaded | NVA95UKB5DSvHvwIV5Qcw | ✓ | ✓ | 39/39 |  |  |
| 225 | Dh_3CF5 | large | 235,023 | done | OK | 0 | 3 | 2 | OK | 1712 | 1068 | 9 | no | uploaded | xNRsZOBmR1HcMH4im8i1a | ✓ | ✓ | 1068/1068 |  |  |
| 226 | Dh_3CF6 | large | 333,805 | done | OK | 0 | 1 | 0 | OK | 947 | 1951 | 8 | no | uploaded | rjtZldlRYAt0IsZbygK9L | ✓ | ✓ | 1951/1951 |  |  |
| 227 | Dh_3CF7 | medium | 32,467 | done | OK | 0 | 1 | 0 | OK | 75 | 206 | 7 | no | uploaded | YS7pmQGI3dnobFzBMXDn2 | ✓ | ✓ | 206/206 |  |  |
| 228 | Dh_3CF8 | medium | 79,180 | done | OK | 0 | 1 | 0 | OK | 148 | 495 | 9 | no | uploaded | kSX57CbbGobn6t1wVwdLg | ✓ | ✓ | 495/495 |  |  |
| 229 | Dh_3CF9 | small | 4,975 | done | OK | 0 | 2 | 0 | OK | 29 | 18 | 6 | no | uploaded | DCPTSAAarI5EpWc1twNfG | ✓ | ✓ | 18/18 |  |  |
| 230 | Dh_3CFC | medium | 123,270 | done | OK | 0 | 1 | 0 | OK | 144 | 602 | 8 | no | uploaded | EowsNk9dCvyaQSQANCRux | ✓ | ✓ | 602/602 |  |  |
| 231 | Dh_3CFD | small | 15,911 | done | OK | 0 | 2 | 0 | OK | 48 | 75 | 6 | no | uploaded | Sv2sLN4W2QbosoNz2rr9K | ✓ | ✓ | 75/75 |  |  |
| 232 | Di_3CEe_ | medium | 46,979 | done | OK | 0 | 2 | 0 | OK | 286 | 128 | 18 | no | uploaded | ZMheqeCIzN5A4aM5hoV5r | ✓ | ✓ | 128/128 |  |  |
| 233 | Di_3CEi_ | small | 1,568 | done | OK | 0 | 1 | 0 | OK | 7 | 2 | 4 | no | uploaded | VSJMSQVwbdBeyrg6sRqMs | ✓ | ✓ | 2/2 |  | retitled (see Retitled) |
| 234 | Di_3CEj_ | small | 1,886 | done | OK | 0 | 1 | 0 | OK | 5 | 0 | 2 | no | uploaded | 8LJ0x9uA1PnvadohqnPfV | ✓ | ✓ | 0/0 |  | retitled (see Retitled) |
| 235 | Di_3CEk_ | small | 4,319 | done | OK | 0 | 2 | 0 | OK | 22 | 16 | 6 | no | uploaded | ncchYSVu51zrx501nsW5V | ✓ | ✓ | 16/16 |  |  |
| 236 | Di_3CEl_ | small | 10,706 | done | OK | 0 | 1 | 0 | OK | 60 | 42 | 8 | no | uploaded | 6oVC2fEDXqOQgEGuCYegg | ✓ | ✓ | 42/42 |  |  |
| 237 | Di_3CEn_ | small | 3,022 | done | OK | 0 | 2 | 0 | OK | 15 | 9 | 6 | no | uploaded | 1W01PQJlASsuGJbteRMm8 | ✓ | ✓ | 9/9 |  |  |
| 238 | Di_3CEp_ | medium | 37,183 | done | OK | 0 | 1 | 0 | OK | 285 | 7 | 11 | no | uploaded | k5Rlii3bXXISP0r8lUShf | ✓ | ✓ | 7/7 |  |  |
| 239 | Di_3CEq_ | medium | 34,486 | done | OK | 0 | 2 | 0 | OK | 278 | 30 | 10 | no | uploaded | OvKRGhnkCTPHEL05mgPw9 | ✓ | ✓ | 30/30 |  |  |
| 240 | Di_3CEs_ | small | 2,467 | done | OK | 0 | 2 | 0 | OK | 11 | 12 | 5 | no | uploaded | J69CJLzdVbQpbqZAIp4qI | ✓ | ✓ | 12/12 |  |  |
| 241 | Di_3CEu_ | small | 5,743 | done | OK | 0 | 1 | 0 | OK | 36 | 18 | 6 | no | uploaded | 0VLCW7jJtrtPemFEIwmZj | ✓ | ✓ | 18/18 |  |  |
| 242 | Di_3CEv_ | small | 13,966 | done | OK | 0 | 1 | 0 | OK | 30 | 11 | 11 | no | uploaded | rI4UGNNbc6CwjPS7cjWQb | ✓ | ✓ | 11/11 |  |  |
| 243 | Di_3CEw_ | small | 17,930 | done | OK | 0 | 1 | 0 | OK | 51 | 84 | 13 | no | uploaded | eaYYK9AL0DvSxWaNPAylc | ✓ | ✓ | 84/84 |  |  |
| 244 | Di_3CEx_ | small | 3,883 | done | OK | 0 | 2 | 0 | OK | 16 | 15 | 6 | no | uploaded | uGXT67gwO7wRRLKCxGBzK | ✓ | ✓ | 15/15 |  |  |
| 245 | Gu_3CFS | large | 405,858 | done | OK | 0 | 2 | 0 | OK | 1188 | 2090 | 39 | no | uploaded | BUFmgHSn21hSGhxBHJqqN | ✓ | ✓ | 2090/2090 |  |  |
| 246 | Gu_3CFT | large | 624,768 | done | OK | 0 | 3 | 1 | OK | 867 | 2538 | 20 | no | uploaded | 0RZcH0DVXLsMrfPvkGnhS | ✓ | ✓ | 2538/2538 |  |  |
| 247 | Ha_3CFF | large | 658,868 | done | OK | 0 | 5 | 3 | OK | 833 | 1249 | 65 | no | uploaded | zHjKL3MltmRqRNrqJufcp | ✓ | ✓ | 1249/1249 |  |  |
| 248 | Ha_3CFG | large | 727,184 | done | OK | 0 | 1 | 0 | OK | 1202 | 1515 | 20 | no | uploaded | 3ZWGBFHqWzK6gc4cOeWcF | ✓ | ✓ | 1515/1515 |  | retitled (see Retitled) |
| 249 | Ha_3CFH | large | 763,615 | done | OK | 0 | 2 | 0 | OK | 1084 | 1752 | 15 | no | uploaded | rFwVoQdwivrPEIQw8et0u | ✓ | ✓ | 1752/1752 |  |  |
| 250 | Ha_3CFI | large | 680,292 | done | OK | 0 | 3 | 1 | OK | 765 | 1626 | 5 | no | uploaded | 32BuYLjXDVjh2iBCGiavE | ✓ | ✓ | 1626/1626 |  |  |
| 251 | Ha_3CFJ | large | 680,411 | done | OK | 0 | 6 | 5 | OK | 722 | 1688 | 49 | no | uploaded | eVx546Q2x1suvW9UOZfrS | ✓ | ✓ | 1688/1688 |  | retitled (see Retitled) |
| 252 | Ha_3CFO | medium | 92,184 | done | OK | 0 | 2 | 0 | OK | 202 | 585 | 10 | no | uploaded | PuHZG606GKjReCAdhEQ2G | ✓ | ✓ | 585/585 |  |  |
| 253 | Ka_3CDK | large | 430,597 | done | OK | 0 | 3 | 2 | OK | 807 | 1316 | 5 | no | uploaded | 0Bf68a3IyhkHF5b2xXwyU | ✓ | ✓ | 1316/1316 |  |  |
| 254 | Ka_3CDL | medium | 114,478 | done | OK | 0 | 2 | 0 | OK | 747 | 351 | 5 | no | uploaded | kCBZNRtdWoWQIE4vJknDJ | ✓ | ✓ | 351/351 |  |  |
| 255 | Ka_3CDM | medium | 70,739 | done | OK | 0 | 1 | 0 | OK | 167 | 182 | 8 | no | uploaded | HkcRlyi42Ratjw2dKrWNw | ✓ | ✓ | 182/182 |  |  |
| 256 | Ka_3CDN | small | 9,976 | done | OK | 0 | 1 | 0 | OK | 38 | 0 | 6 | no | uploaded | zz2kQS2yo7ODxYpJRfyFg | ✓ | ✓ | 0/0 |  |  |
| 257 | Ka_3CDO | medium | 80,267 | done | OK | 0 | 1 | 0 | OK | 113 | 300 | 7 | no | uploaded | PD1dPdrEvEHsr0eZuIK84 | ✓ | ✓ | 300/300 |  |  |
| 258 | Ka_3CDP | medium | 62,237 | done | OK | 0 | 1 | 0 | OK | 92 | 364 | 9 | no | uploaded | GYUBWGfiJT0ghNfAOcSH7 | ✓ | ✓ | 364/364 |  |  |
| 259 | Ka_3CDQ | medium | 57,832 | done | OK | 0 | 1 | 0 | OK | 83 | 326 | 10 | no | uploaded | ZAhrHIxqnIJc4huG90E3J | ✓ | ✓ | 326/326 |  |  |
| 260 | Ka_3CDR | small | 9,003 | done | OK | 0 | 1 | 0 | OK | 25 | 54 | 8 | no | uploaded | EL6Bc1sSOZjXNTBXRyrTt | ✓ | ✓ | 54/54 |  |  |
| 261 | Ka_3CDV | small | 7,273 | done | OK | 0 | 1 | 0 | OK | 29 | 11 | 10 | no | uploaded | HE6Yq7NBYcmfq0VFHJ8T3 | ✓ | ✓ | 11/11 |  |  |
| 262 | Ka_3CDW | small | 19,066 | done | OK | 0 | 1 | 0 | OK | 64 | 111 | 2 | no | uploaded | U9AkzIcp3ZeuXdmRgDqh4 | ✓ | ✓ | 111/111 |  |  |
| 263 | Ka_3CDY | small | 3,163 | done | OK | 0 | 1 | 0 | OK | 17 | 17 | 2 | no | uploaded | tnbQed5Pi52xZegnSHFOf | ✓ | ✓ | 17/17 |  |  |
| 264 | Na_3C92 | small | 17,729 | done | OK | 0 | 1 | 0 | OK | 104 | 96 | 6 | no | uploaded | s7YQNeJz1idxD3F18ogcs | ✓ | ✓ | 96/96 |  |  |
| 265 | Na_3C93 | small | 6,248 | done | OK | 0 | 1 | 0 | OK | 29 | 41 | 6 | no | uploaded | IVZFpJV7rVdSkGPfqjfuM | ✓ | ✓ | 41/41 |  |  |
| 266 | Na_3C94 | small | 5,517 | done | OK | 0 | 1 | 0 | OK | 30 | 25 | 6 | no | uploaded | 7THDBhvveIXo6ETurTNlx | ✓ | ✓ | 25/25 |  |  |
| 267 | Na_3C95 | small | 2,229 | done | OK | 0 | 2 | 0 | OK | 10 | 8 | 5 | no | uploaded | OVN29Aw1aZnFck8fMPJj1 | ✓ | ✓ | 8/8 |  |  |
| 268 | Na_3C96 | small | 3,044 | done | OK | 0 | 1 | 0 | OK | 16 | 13 | 6 | no | uploaded | cIlvIDCi1i9IQ08cReymU | ✓ | ✓ | 13/13 |  |  |
| 269 | Na_3C97 | small | 2,760 | done | OK | 0 | 1 | 0 | OK | 8 | 8 | 6 | no | uploaded | FprabtEcHcZzkYDPzSC1l | ✓ | ✓ | 8/8 |  |  |
| 270 | Na_3C99 | small | 4,051 | done | OK | 0 | 2 | 0 | OK | 14 | 5 | 5 | no | uploaded | sAouZTnsMFvTUK9c3zewA | ✓ | ✓ | 5/5 |  |  |
| 271 | Na_3C9A | small | 4,226 | done | OK | 0 | 1 | 0 | OK | 25 | 6 | 6 | no | uploaded | 4MuO1UcCRjzJXQK2L9deD | ✓ | ✓ | 6/6 |  |  |
| 272 | Na_3C9B | small | 8,932 | done | OK | 0 | 1 | 0 | OK | 57 | 20 | 5 | no | uploaded | ORTIqK39vZHqpRzaVjcDw | ✓ | ✓ | 20/20 |  |  |
| 273 | Na_3C9C | small | 3,692 | done | OK | 0 | 2 | 0 | OK | 21 | 6 | 5 | no | uploaded | smzFx0l939iJ9MtoaJqq3 | ✓ | ✓ | 6/6 |  |  |
| 274 | Na_3C9D | small | 2,179 | done | OK | 0 | 1 | 0 | OK | 11 | 4 | 5 | no | uploaded | 2s9FslYMn9HzfDSwYsVz2 | ✓ | ✓ | 4/4 |  |  |
| 275 | Na_3C9E | small | 2,726 | done | OK | 0 | 1 | 0 | OK | 14 | 3 | 5 | no | uploaded | bILzWWbORE7xEde2P2UWe | ✓ | ✓ | 3/3 |  |  |
| 276 | Na_3C9F | small | 3,988 | done | OK | 0 | 1 | 0 | OK | 19 | 4 | 5 | no | uploaded | iIM9ZkzdJmyRaX0vuDoBR | ✓ | ✓ | 4/4 |  |  |
| 277 | Na_3C9G | small | 2,951 | done | OK | 0 | 2 | 0 | OK | 14 | 8 | 5 | no | uploaded | xMIMunHBamjFP1Cc9PIcD | ✓ | ✓ | 8/8 |  |  |
| 278 | Na_3C9H | small | 2,731 | done | OK | 0 | 4 | 2 | OK | 12 | 9 | 5 | no | uploaded | DWTJwkeBrxf3F2GfoJLlE | ✓ | ✓ | 9/9 |  |  |
| 279 | Na_3C9I | small | 3,907 | done | OK | 0 | 1 | 0 | OK | 17 | 11 | 5 | no | uploaded | eDQ5bQEwpdmJLZLBHNAga | ✓ | ✓ | 11/11 |  |  |
| 280 | Na_3C9J | small | 2,344 | done | OK | 0 | 1 | 0 | OK | 11 | 2 | 5 | no | uploaded | tCxsMH9vttBdYUsjvsoKR | ✓ | ✓ | 2/2 |  |  |
| 281 | Na_3C9K | small | 3,567 | done | OK | 0 | 1 | 0 | OK | 18 | 9 | 5 | no | uploaded | 4657FGa2WU6IiBMmHaeQF | ✓ | ✓ | 9/9 |  |  |
| 282 | Na_3C9M | small | 5,905 | done | OK | 0 | 2 | 0 | OK | 34 | 16 | 3 | no | uploaded | 5hhjxey5cOjSBkgxdG2NR | ✓ | ✓ | 16/16 |  |  |
| 283 | Na_3C9N | small | 16,874 | done | OK | 0 | 2 | 0 | OK | 39 | 64 | 8 | no | uploaded | SGthhPNJPNrhmoOVa0r6W | ✓ | ✓ | 64/64 |  |  |
| 284 | Na_3C9O | small | 4,480 | done | OK | 0 | 2 | 0 | OK | 18 | 21 | 8 | no | uploaded | Nxs2aSA8VT3LS8z3AbhU7 | ✓ | ✓ | 21/21 |  |  |
| 285 | Na_3C9P | small | 8,515 | done | OK | 0 | 1 | 0 | OK | 34 | 42 | 8 | no | uploaded | sFBKQyUlGTeau1OSjL3cY | ✓ | ✓ | 42/42 |  |  |
| 286 | Na_3C9Q | small | 12,220 | done | OK | 0 | 1 | 0 | OK | 26 | 52 | 6 | no | uploaded | QIh2pj1QNsYAhUMza8rKL | ✓ | ✓ | 52/52 |  |  |
| 287 | Na_3C9R | small | 4,215 | done | OK | 0 | 3 | 1 | OK | 14 | 24 | 7 | no | uploaded | tqCk309BX8jEt6CrKNd2m | ✓ | ✓ | 24/24 |  |  |
| 288 | Na_3C9S | small | 3,488 | **held** | OK | 0 | 1 | 0 | OK | 13 | 9 | 5 | no | **failed** |  |  |  |  |  | near-duplicate of Ar_3CBf_ (uploaded): same translation, edited separately; see source_description |
| 289 | Na_3C9T | small | 3,376 | done | OK | 0 | 1 | 0 | OK | 10 | 16 | 5 | no | uploaded | AEvMeasfXpTpPwyI5kVLO | ✓ | ✓ | 16/16 |  | retitled (see Retitled) |
| 290 | Na_3C9U | small | 2,484 | done | OK | 0 | 4 | 2 | OK | 11 | 12 | 3 | no | uploaded | QoxlQmbW2PXeLIGEeMCEQ | ✓ | ✓ | 12/12 |  |  |
| 291 | Na_3C9V | small | 5,552 | done | OK | 0 | 1 | 0 | OK | 14 | 24 | 5 | no | uploaded | iNsukPJ8ysb1S7seaiM2O | ✓ | ✓ | 24/24 |  | retitled (see Retitled) |
| 292 | Na_3C9W | small | 6,964 | done | OK | 0 | 1 | 0 | OK | 12 | 60 | 3 | no | uploaded | B3zeAmJAyeec5xNDR94n6 | ✓ | ✓ | 60/60 |  | retitled (see Retitled) |
| 293 | Na_3C9X | small | 6,426 | done | OK | 0 | 1 | 0 | OK | 13 | 44 | 5 | no | uploaded | gKEiZcr05YqJsZ7WwwdP3 | ✓ | ✓ | 44/44 |  | retitled (see Retitled) |
| 294 | Na_3C9Y | small | 4,593 | done | OK | 0 | 2 | 0 | OK | 12 | 17 | 3 | no | uploaded | yyxy8f6evgJciznvXkJpO | ✓ | ✓ | 17/17 |  |  |
| 295 | Na_3C9a_ | medium | 37,055 | done | OK | 0 | 2 | 0 | OK | 178 | 133 | 17 | no | uploaded | Rw3zayH6qfufG1WNpIR6H | ✓ | ✓ | 133/133 |  |  |
| 296 | Na_3C9b_ | small | 18,507 | done | OK | 0 | 1 | 0 | OK | 63 | 70 | 7 | no | uploaded | 42bv4SCycJxcnPkyY82Ke | ✓ | ✓ | 70/70 |  |  |
| 297 | Na_3C9c_ | medium | 85,558 | done | OK | 0 | 2 | 1 | OK | 241 | 358 | 25 | no | uploaded | ROXoQVFjLhZcac4JWJ8mW | ✓ | ✓ | 358/358 |  | retitled (see Retitled) |
| 298 | Na_3C9d_ | small | 12,290 | done | OK | 0 | 2 | 0 | OK | 61 | 38 | 10 | no | uploaded | gnEbZMmbpNrjHmMdyUBVj | ✓ | ✓ | 38/38 |  |  |
| 299 | Na_3C9e_ | small | 18,366 | done | OK | 0 | 2 | 0 | OK | 112 | 54 | 6 | no | uploaded | 6kB3PlLWXa1OhEJQ3eMSK | ✓ | ✓ | 54/54 |  |  |
| 300 | Na_3C9h_ | medium | 40,913 | done | OK | 0 | 2 | 0 | OK | 288 | 0 | 9 | no | uploaded | OLXi2JFBUwsfFLLVirPH2 | ✓ | ✓ | 0/0 |  |  |
| 301 | Na_3C9i_ | small | 26,518 | done | OK | 0 | 1 | 0 | OK | 94 | 127 | 15 | no | uploaded | M8rQxOHetcroBwlyXNoGv | ✓ | ✓ | 127/127 |  |  |
| 302 | Na_3C9j_ | small | 17,958 | done | OK | 0 | 1 | 0 | OK | 87 | 94 | 17 | no | uploaded | S2NsXdzVxMGiCfVjXiZOt | ✓ | ✓ | 94/94 |  |  |
| 303 | Na_3C9k_ | medium | 88,531 | done | OK | 0 | 1 | 0 | OK | 375 | 449 | 21 | no | uploaded | Vxo16vSL52zMrcVBkwkb8 | ✓ | ✓ | 449/449 |  |  |
| 304 | Na_3C9n_ | medium | 38,193 | done | OK | 0 | 1 | 0 | OK | 198 | 176 | 30 | no | uploaded | TMJg8JEc62EXPoKJRh97T | ✓ | ✓ | 176/176 |  |  |
| 305 | Na_3C9o_ | small | 7,088 | done | OK | 0 | 2 | 0 | OK | 31 | 34 | 10 | no | uploaded | rgptoTET50iGM7n7gX4kA | ✓ | ✓ | 34/34 |  |  |
| 306 | Na_3C9p_ | small | 5,193 | done | OK | 0 | 2 | 0 | OK | 28 | 21 | 6 | no | uploaded | r5l3pI0EL27hpQS9rhwfE | ✓ | ✓ | 21/21 |  |  |
| 307 | Na_3C9r_ | small | 10,406 | done | OK | 0 | 2 | 0 | OK | 24 | 38 | 9 | no | uploaded | eNS7bFVkFx1r0SxaqzsU6 | ✓ | ✓ | 38/38 |  |  |
| 308 | Na_3C9s_ | small | 1,722 | done | OK | 0 | 1 | 0 | OK | 6 | 0 | 4 | no | uploaded | s4d2WnQRVeqnWTv9ONUGG | ✓ | ✓ | 0/0 |  |  |
| 309 | Na_3C9t_ | small | 3,566 | done | OK | 0 | 2 | 0 | OK | 22 | 6 | 6 | no | uploaded | cS9mwX4QWwT92JPwc1uVp | ✓ | ✓ | 6/6 |  |  |
| 310 | Na_3C9u_ | small | 19,813 | done | OK | 0 | 1 | 0 | OK | 50 | 97 | 17 | no | uploaded | s3nfzJckVsSrsZWfTWdKe | ✓ | ✓ | 97/97 |  |  |
| 311 | Na_3C9v_ | small | 1,481 | done | OK | 0 | 2 | 0 | OK | 5 | 2 | 2 | no | uploaded | GaYehLC3WjCIamOgeXN4P | ✓ | ✓ | 2/2 |  |  |
| 312 | Na_3C9w_ | small | 2,475 | done | OK | 0 | 1 | 0 | OK | 10 | 4 | 5 | no | uploaded | dKW3tuIsjTY4TqV7vEuup | ✓ | ✓ | 4/4 |  |  |
| 313 | Na_3C9x_ | small | 1,505 | done | OK | 0 | 1 | 0 | OK | 6 | 0 | 2 | no | uploaded | xVc3EB0CLiUxIDOsqyI6v | ✓ | ✓ | 0/0 |  | retitled (see Retitled) |
| 314 | Na_3C9y_ | small | 1,942 | done | OK | 0 | 1 | 0 | OK | 7 | 1 | 3 | no | uploaded | 0mxQKp3McvNB51Ldwx1a2 | ✓ | ✓ | 1/1 |  | retitled (see Retitled) |
| 315 | Na_3C9z_ | small | 7,563 | done | OK | 0 | 1 | 0 | OK | 46 | 2 | 9 | no | uploaded | eX4kWdrrLm2L6KREWxnVa | ✓ | ✓ | 2/2 |  |  |
| 316 | Na_3CA0 | small | 1,432 | done | OK | 0 | 1 | 0 | OK | 5 | 2 | 2 | no | uploaded | Sq3XMPkcjK57FVl6tO1eT | ✓ | ✓ | 2/2 |  |  |
| 317 | Na_3CA1 | small | 1,091 | done | OK | 0 | 2 | 0 | OK | 6 | 1 | 2 | no | uploaded | EnUSEa5YsXGFMF1t6Xq8e | ✓ | ✓ | 1/1 |  |  |
| 318 | Na_3CA2 | small | 2,344 | done | OK | 0 | 1 | 0 | OK | 14 | 2 | 14 | no | uploaded | xEjc1yrtXKjUMxlafxKtd | ✓ | ✓ | 2/2 |  |  |
| 319 | Na_3CA3 | small | 8,635 | done | OK | 0 | 2 | 0 | OK | 32 | 34 | 6 | no | uploaded | bKPpKJLp8gSK1NPFSyiMg | ✓ | ✓ | 34/34 |  |  |
| 320 | Na_3CA5 | small | 4,975 | done | OK | 0 | 1 | 0 | OK | 11 | 22 | 8 | no | uploaded | X6SVSK0s5VCCoxf9LbA8R | ✓ | ✓ | 22/22 |  |  |
| 321 | Na_3CA6 | medium | 34,605 | done | OK | 0 | 1 | 0 | OK | 75 | 163 | 15 | no | uploaded | Qp7e6IAn3nfffYaOwGGWr | ✓ | ✓ | 163/163 |  |  |
| 322 | Na_3CA7 | small | 6,557 | done | OK | 0 | 1 | 0 | OK | 25 | 22 | 6 | no | uploaded | 4WpEAg9cK2I4tWenpp33e | ✓ | ✓ | 22/22 |  |  |
| 323 | Na_3CA8 | small | 3,041 | done | OK | 0 | 2 | 0 | OK | 9 | 9 | 5 | no | uploaded | DDnz5lQyMYqxJXzJXBrpd | ✓ | ✓ | 9/9 |  |  |
| 324 | Na_3CA9 | small | 4,271 | done | OK | 0 | 1 | 0 | OK | 17 | 21 | 11 | no | uploaded | lKqziUMDdfPDxCjSOWP7R | ✓ | ✓ | 21/21 |  |  |
| 325 | Na_3CAA | small | 2,410 | done | OK | 0 | 2 | 0 | OK | 8 | 9 | 4 | no | uploaded | 7cZTDSYItdKLKZnUWRzJJ | ✓ | ✓ | 9/9 |  |  |
| 326 | Na_3CAB | small | 2,262 | done | OK | 0 | 1 | 0 | OK | 7 | 10 | 6 | no | uploaded | YDmLzzxjTr6JZPUUIw4m8 | ✓ | ✓ | 10/10 |  |  |
| 327 | Na_3CAC | small | 3,243 | done | OK | 0 | 2 | 0 | OK | 13 | 15 | 7 | no | uploaded | oKOJjCV75uWZMNu2SMeKy | ✓ | ✓ | 15/15 |  |  |
| 328 | Na_3CAD | small | 21,313 | done | OK | 0 | 1 | 0 | OK | 90 | 113 | 10 | no | uploaded | yTz8ttbTfTxgtTWXqsFy5 | ✓ | ✓ | 113/113 |  |  |
| 329 | Na_3CAE | small | 8,079 | done | OK | 0 | 1 | 0 | OK | 27 | 28 | 8 | no | uploaded | KCS6Ab5J2VcS0x50Jp0S1 | ✓ | ✓ | 28/28 |  |  |
| 330 | Na_3CAF | medium | 35,000 | done | OK | 0 | 2 | 0 | OK | 96 | 130 | 9 | no | uploaded | g4SRVrGpwiOYpqzwFlhdt | ✓ | ✓ | 130/130 |  |  |
| 331 | Na_3CAG | small | 8,497 | done | OK | 0 | 1 | 0 | OK | 23 | 28 | 14 | no | uploaded | VbLDOwbMa6SunmmKfijMG | ✓ | ✓ | 28/28 |  |  |
| 332 | Na_3CAH | small | 2,664 | done | OK | 0 | 1 | 0 | OK | 9 | 9 | 5 | no | uploaded | d2ivbyO2OCVYf6GYgJ5Id | ✓ | ✓ | 9/9 |  |  |
| 333 | Na_3CAI | small | 2,165 | done | OK | 0 | 1 | 0 | OK | 6 | 8 | 5 | no | uploaded | qxU4WpvJjY7tEgeB8G86o | ✓ | ✓ | 8/8 |  |  |
| 334 | Na_3CAJ | small | 2,545 | done | OK | 0 | 2 | 0 | OK | 9 | 10 | 3 | no | uploaded | pAZzCniQQNudA0cuJ7qV5 | ✓ | ✓ | 10/10 |  |  |
| 335 | Na_3CAK | small | 1,926 | done | OK | 0 | 2 | 0 | OK | 4 | 8 | 4 | no | uploaded | uyEjZujT3mjrgAoIapzYK | ✓ | ✓ | 8/8 |  |  |
| 336 | Na_3CAL | small | 2,416 | done | OK | 0 | 1 | 0 | OK | 6 | 12 | 5 | no | uploaded | C4DUt5euqPDs5zbJAqKMf | ✓ | ✓ | 12/12 |  |  |
| 337 | Na_3CAM | small | 8,896 | done | OK | 0 | 1 | 0 | OK | 22 | 75 | 6 | no | uploaded | Uai66Nno1fSD3idavHOXQ | ✓ | ✓ | 75/75 |  |  |
| 338 | Na_3CAN | small | 12,388 | done | OK | 0 | 14 | 13 | OK | 36 | 107 | 4 | no | uploaded | KyzK88hXyOfRnpAonPa6G | ✓ | ✓ | 107/107 |  | retitled (see Retitled) |
| 339 | Na_3CAO | small | 11,390 | done | OK | 0 | 6 | 5 | OK | 43 | 59 | 4 | no | uploaded | A5uH9IYHyQhgzgoxMwHpq | ✓ | ✓ | 59/59 |  | retitled (see Retitled) |
| 340 | Na_3CAP | small | 4,333 | done | OK | 0 | 1 | 0 | OK | 12 | 11 | 5 | no | uploaded | Bl9EjJ77oqRGiywcgzorP | ✓ | ✓ | 11/11 |  | retitled (see Retitled) |
| 341 | Na_3CAQ | small | 8,694 | done | OK | 0 | 1 | 0 | OK | 24 | 62 | 10 | no | uploaded | hmSoogOyoLhbEmB0BKRyp | ✓ | ✓ | 62/62 |  |  |
| 342 | Na_3CAR | small | 7,509 | done | OK | 0 | 2 | 0 | OK | 17 | 22 | 7 | no | uploaded | JSFb5PcdhARm627Uup7ks | ✓ | ✓ | 22/22 |  |  |
| 343 | Na_3CAS | small | 5,042 | done | OK | 0 | 2 | 0 | OK | 18 | 18 | 6 | no | uploaded | HQUd6eH9jHWnSxtuqiC9j | ✓ | ✓ | 18/18 |  |  |
| 344 | Na_3CAT | small | 23,515 | done | OK | 0 | 1 | 0 | OK | 86 | 110 | 8 | no | uploaded | 492SYPXh6vYZJfDzLc28s | ✓ | ✓ | 110/110 |  |  |
| 345 | Na_3CAU | small | 2,796 | done | OK | 0 | 1 | 0 | OK | 15 | 5 | 5 | no | uploaded | ljVwvg0JEVXYxbZddylMq | ✓ | ✓ | 5/5 |  |  |
| 346 | Na_3CAV | medium | 133,200 | done | OK | 0 | 1 | 0 | OK | 540 | 579 | 34 | no | uploaded | Ed8m1jAOo3oyvUK4Qojfc | ✓ | ✓ | 579/579 |  |  |
| 347 | Na_3CAW | small | 11,294 | done | OK | 0 | 2 | 0 | OK | 28 | 18 | 12 | no | uploaded | GBCFXGS1862c4giguUWoo | ✓ | ✓ | 18/18 |  |  |
| 348 | Na_3CAX | medium | 33,362 | done | OK | 0 | 2 | 0 | OK | 181 | 45 | 18 | no | uploaded | 8ev59x1p3lmqe8inQzI9s | ✓ | ✓ | 45/45 |  |  |
| 349 | Na_3CAY | small | 9,884 | done | OK | 0 | 2 | 0 | OK | 31 | 10 | 8 | no | uploaded | ELUvV4K7szF6ZB8GkX1wr | ✓ | ✓ | 10/10 |  |  |
| 350 | Na_3CAZ | small | 3,756 | done | OK | 0 | 2 | 0 | OK | 10 | 3 | 7 | no | uploaded | wfIGj8WU1bteMOcNTzGWx | ✓ | ✓ | 3/3 |  |  |
| 351 | Na_3CAb_ | small | 7,062 | done | OK | 0 | 2 | 0 | OK | 37 | 4 | 7 | no | uploaded | UdX4vmkHLTNdi4sULlWox | ✓ | ✓ | 4/4 |  |  |
| 352 | Na_3CAc_ | small | 2,539 | done | OK | 0 | 1 | 0 | OK | 12 | 2 | 2 | no | uploaded | YlvDp8aEENCvAAZEsWVF3 | ✓ | ✓ | 2/2 |  |  |
| 353 | Na_3CAd_ | small | 4,335 | done | OK | 0 | 2 | 0 | OK | 18 | 6 | 5 | no | uploaded | CggzlRkAuCWfbvgeLxhFO | ✓ | ✓ | 6/6 |  |  |
| 354 | Na_3CAe_ | small | 2,937 | done | OK | 0 | 3 | 1 | OK | 6 | 5 | 6 | no | uploaded | Ng2hTGkjeFRtOdEbKwBx7 | ✓ | ✓ | 5/5 |  |  |
| 355 | Na_3CAf_ | small | 3,859 | done | OK | 0 | 2 | 0 | OK | 12 | 1 | 6 | no | uploaded | HwtS7xWaP6NM8OYYmLbD2 | ✓ | ✓ | 1/1 |  |  |
| 356 | Na_3CAg_ | small | 28,031 | done | OK | 0 | 2 | 0 | OK | 147 | 31 | 6 | no | uploaded | RKFoliwQhj3OpPRQgrxnL | ✓ | ✓ | 31/31 |  |  |
| 357 | Na_3CAh_ | small | 6,988 | done | OK | 0 | 2 | 0 | OK | 25 | 18 | 5 | no | uploaded | VBtZMwTcOQUsAsn6kgOkt | ✓ | ✓ | 18/18 |  |  |
| 358 | Na_3CAi_ | small | 7,392 | done | OK | 0 | 2 | 0 | OK | 41 | 3 | 9 | no | uploaded | ks7Q7XgIVtmtKsul1MRWG | ✓ | ✓ | 3/3 |  |  |
| 359 | Na_3CAk_ | medium | 77,042 | done | OK | 0 | 1 | 0 | OK | 480 | 397 | 32 | no | uploaded | vIS4OXrFg7ENZGxlrop73 | ✓ | ✓ | 397/397 |  |  |
| 360 | Na_3CAl_ | small | 10,969 | done | OK | 0 | 1 | 0 | OK | 65 | 48 | 6 | no | uploaded | Gj3lcC7apXesEsQTEx1Ti | ✓ | ✓ | 48/48 |  |  |
| 361 | Na_3CAm_ | small | 6,886 | done | OK | 0 | 1 | 0 | OK | 42 | 23 | 6 | no | uploaded | 3nD2S9OOxPvdFT34oTpuR | ✓ | ✓ | 23/23 |  |  |
| 362 | Na_3CAn_ | small | 13,346 | done | OK | 0 | 1 | 0 | OK | 78 | 65 | 5 | no | uploaded | xRh1pd7lknhgdk1RKtQxw | ✓ | ✓ | 65/65 |  |  |
| 363 | Na_3CAo_ | small | 12,796 | done | OK | 0 | 1 | 0 | OK | 78 | 64 | 6 | no | uploaded | baDJayFpbksFwHwJAIeTm | ✓ | ✓ | 64/64 |  |  |
| 364 | Na_3CAu_ | small | 4,428 | done | OK | 0 | 2 | 0 | OK | 27 | 10 | 6 | no | uploaded | Rr8we9F4DE2cyHtjSL73S | ✓ | ✓ | 10/10 |  |  |
| 365 | Na_3CAv_ | small | 1,547 | done | OK | 0 | 2 | 0 | OK | 13 | 1 | 3 | no | uploaded | ahcb1r39HzEiSMW7e3kow | ✓ | ✓ | 1/1 |  |  |
| 366 | Na_3CAx_ | small | 2,396 | done | OK | 0 | 1 | 0 | OK | 11 | 7 | 5 | no | uploaded | WfLVXZvMra8UhuKFOHZid | ✓ | ✓ | 7/7 |  |  |
| 367 | Na_3CAz_ | small | 5,339 | done | OK | 0 | 1 | 0 | OK | 28 | 19 | 9 | no | uploaded | B6k2oIEuzsKHSH19Rn7k8 | ✓ | ✓ | 19/19 |  |  |
| 368 | Na_3CB0 | small | 4,255 | done | OK | 0 | 1 | 0 | OK | 19 | 19 | 6 | no | uploaded | aNp7BDMo5uF7BDWdLwMRE | ✓ | ✓ | 19/19 |  |  |
| 369 | Na_3CB1 | small | 4,338 | done | OK | 0 | 1 | 0 | OK | 25 | 15 | 9 | no | uploaded | 3jr5AEz9sAAHkquKVPnbd | ✓ | ✓ | 15/15 |  |  |
| 370 | Na_3CB2 | small | 7,318 | done | OK | 0 | 2 | 0 | OK | 45 | 24 | 7 | no | uploaded | ZJBAdI9mreypcSTmXtU0T | ✓ | ✓ | 24/24 |  |  |
| 371 | Na_3CB3 | small | 9,393 | done | OK | 0 | 1 | 0 | OK | 59 | 27 | 5 | no | uploaded | ym2ryCr50bNfzdZ0OwyFj | ✓ | ✓ | 27/27 |  |  |
| 372 | Na_3CB4 | large | 276,167 | done | OK | 0 | 1 | 0 | OK | 386 | 1255 | 22 | no | uploaded | Xe4w0yidq7bi5gaDVc9xn | ✓ | ✓ | 1255/1255 |  |  |
| 373 | Na_3CB5 | small | 8,693 | done | OK | 0 | 1 | 0 | OK | 24 | 25 | 11 | no | uploaded | GJ7QLT1jx4VbhIWSW4B13 | ✓ | ✓ | 25/25 |  |  |
| 374 | Na_3CB6 | small | 12,299 | done | OK | 0 | 2 | 0 | OK | 54 | 67 | 7 | no | uploaded | vWBx0JPRQy2BDfPdXMbaa | ✓ | ✓ | 67/67 |  |  |
| 375 | Na_3CBB | medium | 53,257 | done | OK | 0 | 1 | 0 | OK | 242 | 316 | 19 | no | uploaded | D4rL3iP5a8iKso8DTYOmt | ✓ | ✓ | 316/316 |  |  |
| 376 | Na_3CBC | small | 2,716 | done | OK | 0 | 1 | 0 | OK | 6 | 4 | 6 | no | uploaded | RIiNagkrDTtKlHaII1rcA | ✓ | ✓ | 4/4 |  |  |
| 377 | Na_3CBD | medium | 81,507 | done | OK | 0 | 2 | 0 | OK | 496 | 393 | 10 | no | uploaded | 3TMHFYvVG7KsN7dYJdSae | ✓ | ✓ | 393/393 |  |  |
| 378 | Na_3CBE | small | 7,088 | done | OK | 0 | 2 | 0 | OK | 36 | 31 | 6 | no | uploaded | RRLvcQE7uMjGzuhnNH0eF | ✓ | ✓ | 31/31 |  |  |
| 379 | Na_3CBF | small | 4,032 | done | OK | 0 | 3 | 1 | OK | 16 | 18 | 5 | no | uploaded | nWX7367dHFWdSJjohrVaE | ✓ | ✓ | 18/18 |  |  |
| 380 | Na_3CBG | small | 3,701 | done | OK | 0 | 2 | 0 | OK | 22 | 9 | 6 | no | uploaded | pWFDfyDcRnIQrIxa4VcFp | ✓ | ✓ | 9/9 |  |  |
| 381 | Na_3CBH | small | 26,958 | done | OK | 0 | 1 | 0 | OK | 121 | 154 | 5 | no | uploaded | tTWollM5DFCwbwxWFzJ6E | ✓ | ✓ | 154/154 |  |  |
| 382 | Na_3CBI | small | 32,877 | done | OK | 0 | 1 | 0 | OK | 128 | 259 | 15 | no | uploaded | VP5TAhQCVAsUbPtPdkE4M | ✓ | ✓ | 259/259 |  |  |
| 383 | Na_3CBJ | small | 16,914 | done | OK | 0 | 1 | 0 | OK | 44 | 129 | 4 | no | uploaded | WxCfcP5DtRb7RUqvm2ZVa | ✓ | ✓ | 129/129 |  |  |
| 384 | Na_3CBK | small | 6,478 | done | OK | 0 | 1 | 0 | OK | 17 | 34 | 9 | no | uploaded | N5s6gh7nco2ibv394skDa | ✓ | ✓ | 34/34 |  |  |
| 385 | Na_3CBL | small | 1,497 | done | OK | 0 | 1 | 0 | OK | 7 | 0 | 5 | no | uploaded | 5ediWDuaa7ucirFte6zYr | ✓ | ✓ | 0/0 |  |  |
| 386 | Na_3CBM | small | 3,776 | done | OK | 0 | 1 | 0 | OK | 11 | 30 | 5 | no | uploaded | 1RNk3OVsoQkDl9ot4R1cv | ✓ | ✓ | 30/30 |  |  |
| 387 | Na_3CBN | small | 31,772 | done | OK | 0 | 1 | 0 | OK | 146 | 11 | 17 | no | uploaded | 1ZlVEnzP8JlAovlEkF4uE | ✓ | ✓ | 11/11 |  |  |
| 388 | Na_3CBO | small | 21,776 | done | OK | 0 | 2 | 0 | OK | 109 | 184 | 6 | no | uploaded | 3va6BxKuyahg8clDlldrN | ✓ | ✓ | 184/184 |  |  |
| 389 | Na_3CBP | medium | 46,500 | done | OK | 0 | 2 | 0 | OK | 274 | 270 | 6 | no | uploaded | lCpq9au3AgQZV0YrtjfxN | ✓ | ✓ | 270/270 |  |  |
| 390 | Na_3CBQ | small | 21,203 | done | OK | 0 | 1 | 0 | OK | 88 | 188 | 6 | no | uploaded | NhImmcokbOApK1vJTKRwr | ✓ | ✓ | 188/188 |  |  |
| 391 | Na_3CBR | small | 3,669 | done | OK | 0 | 2 | 0 | OK | 21 | 0 | 6 | no | uploaded | 1UEcpgAoggctNbZ2SywE2 | ✓ | ✓ | 0/0 |  |  |
| 392 | Na_3CBS | small | 4,706 | done | OK | 0 | 2 | 0 | OK | 19 | 23 | 5 | no | uploaded | eVTBykaehPykaEA7x9K8d | ✓ | ✓ | 23/23 |  |  |
| 393 | Na_3CBT | small | 3,082 | done | OK | 0 | 1 | 0 | OK | 11 | 12 | 5 | no | uploaded | KeBKkwFlLrwdFz4GpQ0j1 | ✓ | ✓ | 12/12 |  |  |
| 394 | Na_3CBU | small | 4,964 | done | OK | 0 | 1 | 0 | OK | 21 | 20 | 2 | no | uploaded | RJWl3r7dfDzDdNyvCmTla | ✓ | ✓ | 20/20 |  |  |
| 395 | Na_3CBV | small | 4,391 | done | OK | 0 | 1 | 0 | OK | 23 | 0 | 6 | no | uploaded | UNIH8BLETwg5J1S3rnp9k | ✓ | ✓ | 0/0 |  |  |
| 396 | Na_3CBW | small | 6,134 | done | OK | 0 | 1 | 0 | OK | 23 | 27 | 8 | no | uploaded | defNlAEiXJREjTCNXbEF5 | ✓ | ✓ | 27/27 |  | retitled (see Retitled) |
| 397 | Na_3CBX | small | 8,479 | done | OK | 0 | 2 | 0 | OK | 34 | 41 | 5 | no | uploaded | 8YqIMkwXmkq6UYrZ1MXWe | ✓ | ✓ | 41/41 |  |  |
| 398 | Na_3CBY | small | 27,856 | done | OK | 0 | 1 | 0 | OK | 169 | 85 | 5 | no | uploaded | 4sgNlcpfpGX6p6uZusu5R | ✓ | ✓ | 85/85 |  |  |
| 399 | Na_3CBZ | small | 6,779 | done | OK | 0 | 1 | 0 | OK | 17 | 11 | 5 | no | uploaded | uZCi9u874IVcrBmEdaWLH | ✓ | ✓ | 11/11 |  |  |
| 400 | Sh_3CCh_ | small | 1,468 | done | OK | 0 | 1 | 0 | OK | 6 | 0 | 2 | no | uploaded | Bnsq3egJ0pKzFV9rONUzG | ✓ | ✓ | 0/0 |  | retitled (see Retitled) |
| 401 | Sh_3CCi_ | small | 1,825 | done | OK | 0 | 1 | 0 | OK | 6 | 1 | 2 | no | uploaded | qDWOuHPTuSTXvUlWj5u16 | ✓ | ✓ | 1/1 |  | retitled (see Retitled) |
| 402 | Sh_3CCj_ | small | 1,919 | done | OK | 0 | 2 | 0 | OK | 8 | 5 | 6 | no | uploaded | LcCZ4LagU8OW8EgswLRU9 | ✓ | ✓ | 5/5 |  |  |
| 403 | Sh_3CCl_ | small | 1,656 | done | OK | 0 | 2 | 0 | OK | 7 | 1 | 5 | no | uploaded | MI7RltmRpWofsM5IXXgoo | ✓ | ✓ | 1/1 |  |  |
| 404 | Sh_3CCm_ | medium | 161,702 | **held** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | held by request (2026-10-13) |
| 405 | Sh_3CCn_ | small | 3,723 | done | OK | 0 | 1 | 0 | OK | 13 | 7 | 5 | no | uploaded | 29eBkMQJfoTOBoHMk6ocF | ✓ | ✓ | 7/7 |  |  |
| 406 | Sh_3CCp_ | small | 23,775 | done | OK | 0 | 1 | 0 | OK | 69 | 135 | 5 | no | uploaded | f1kgfnvdn8kRrN4UGhYBJ | ✓ | ✓ | 135/135 |  |  |
| 407 | Sh_3CCq_ | small | 13,171 | done | OK | 0 | 1 | 0 | OK | 69 | 73 | 2 | no | uploaded | RRp6mExkSiopulaTHiIPU | ✓ | ✓ | 73/73 |  |  |
| 408 | Sh_3CCr_ | small | 5,406 | done | OK | 0 | 2 | 0 | OK | 32 | 20 | 9 | no | uploaded | lILQJ8ziYDaUjgmc9i1pB | ✓ | ✓ | 20/20 |  |  |
| 409 | Sh_3CCs_ | large | 272,404 | done | OK | 0 | 1 | 0 | OK | 598 | 1466 | 7 | no | uploaded | 8Rny2ucutFoSoG5TmR9q5 | ✓ | ✓ | 1466/1466 |  | retitled (see Retitled) |
| 410 | Sh_3CCt_ | large | 550,395 | done | OK | 0 | 3 | 1 | OK | 1424 | 2850 | 18 | no | uploaded | gMfxq9x5JHLsGB8ZmHEJr | ✓ | ✓ | 2850/2850 |  |  |
| 411 | Sh_3CCu_ | small | 17,960 | done | OK | 0 | 1 | 0 | OK | 66 | 0 | 2 | no | uploaded | b0mux3xub6C5v2HlK6Acu | ✓ | ✓ | 0/0 |  |  |
| 412 | Sh_3CCv_ | small | 2,088 | done | OK | 0 | 2 | 0 | OK | 9 | 1 | 5 | no | uploaded | E5WOrkGUaKFOX3s9oajIu | ✓ | ✓ | 1/1 |  |  |
| 413 | Sh_3CCx_ | small | 3,891 | done | OK | 0 | 2 | 0 | OK | 20 | 5 | 5 | no | uploaded | PiWHVBdiOcvzJWScOT8Ul | ✓ | ✓ | 5/5 |  |  |
| 414 | Sh_3CCy_ | small | 4,095 | done | OK | 0 | 1 | 0 | OK | 14 | 4 | 9 | no | uploaded | DGKtIir0lGUCBbtJUK5WE | ✓ | ✓ | 4/4 |  |  |
| 415 | Sh_3CCz_ | small | 4,187 | done | OK | 0 | 2 | 0 | OK | 15 | 11 | 8 | no | uploaded | 2QOWrMhIt8rfKoMmFdkrz | ✓ | ✓ | 11/11 |  |  |
| 416 | Sh_3CD1 | medium | 42,819 | done | OK | 0 | 5 | 3 | OK | 58 | 6 | 8 | no | uploaded | myZsK7j5CWY93tpK9LJ3s | ✓ | ✓ | 6/6 |  |  |
| 417 | Sh_3CD2 | medium | 59,260 | done | OK | 0 | 2 | 0 | OK | 171 | 180 | 35 | no | uploaded | m4RuDDwAIO84WrluJ9YxU | ✓ | ✓ | 180/180 |  |  |
| 418 | Sh_3CD3 | medium | 106,268 | done | OK | 0 | 1 | 0 | OK | 147 | 341 | 10 | no | uploaded | EoWG5t2TxpWnh0oI8SAI9 | ✓ | ✓ | 341/341 |  |  |
| 419 | Sh_3CD4 | medium | 78,902 | done | OK | 0 | 1 | 0 | OK | 138 | 265 | 12 | no | uploaded | lnjdvnw1qGlrLEI4LTNm1 | ✓ | ✓ | 265/265 |  |  |
| 420 | Sh_3CD5 | small | 23,037 | done | OK | 0 | 2 | 0 | OK | 33 | 67 | 8 | no | uploaded | yMY2JjoVmjn30v1UXAy1I | ✓ | ✓ | 67/67 |  |  |
| 421 | Sh_3CD6 | medium | 81,035 | done | OK | 0 | 1 | 0 | OK | 113 | 0 | 6 | no | uploaded | M5kHkS8kCivAjA17OUvms | ✓ | ✓ | 0/0 |  |  |
| 422 | Sh_3CD7 | medium | 61,318 | done | OK | 0 | 1 | 0 | OK | 110 | 0 | 6 | no | uploaded | IufLPPxqlU9h3aAsonMx0 | ✓ | ✓ | 0/0 |  |  |
| 423 | Sh_3CD8 | medium | 48,745 | done | OK | 0 | 2 | 0 | OK | 118 | 166 | 6 | no | uploaded | IzOQAnt6OEN9n32H5k3SD | ✓ | ✓ | 166/166 |  |  |
| 424 | Sh_3CDA | small | 15,267 | done | OK | 0 | 1 | 0 | OK | 100 | 49 | 6 | no | uploaded | 1AQvtom61Uu3yhxNJZdzB | ✓ | ✓ | 49/49 |  |  |
| 425 | Sh_3CDE | large | 571,168 | done | OK | 0 | 2 | 1 | OK | 3381 | 2663 | 35 | no | uploaded | ZXnSIFwTdHCQtMXw6ExUa | ✓ | ✓ | 2663/2663 |  |  |
| 426 | Sh_3CDF | small | 12,155 | done | OK | 0 | 1 | 0 | OK | 60 | 0 | 7 | no | uploaded | BMxOpxX2FSaul3mRQnyI2 | ✓ | ✓ | 0/0 |  |  |
| 427 | Sh_3CFZ | medium | 53,853 | **held** | OK | 0 | 1 | 0 | OK | 248 | 325 | 19 | no | **failed** |  |  |  |  |  | near-duplicate of Na_3CBB (uploaded): same translation, edited separately; see source_description |
| 428 | Va_3CE0 | small | 1,431 | done | OK | 0 | 2 | 0 | OK | 6 | 2 | 5 | no | uploaded | QJIPc1h85yzpU080yQ0rO | ✓ | ✓ | 2/2 |  |  |
| 429 | Va_3CEL | small | 5,442 | done | OK | 0 | 2 | 0 | OK | 29 | 14 | 7 | no | uploaded | J4ITl7pJpeOIfg5ohX24E | ✓ | ✓ | 14/14 |  |  |
| 430 | Va_3CEM | small | 4,414 | done | OK | 0 | 2 | 0 | OK | 26 | 13 | 6 | no | uploaded | sGn4yZ2cobBWp7WBqp4uN | ✓ | ✓ | 13/13 |  |  |
| 431 | Va_3CEO | small | 7,274 | done | OK | 0 | 2 | 0 | OK | 42 | 30 | 8 | no | uploaded | fUw8zOUHL1Bq46xlU5JTV | ✓ | ✓ | 30/30 |  |  |
| 432 | Va_3CEP | small | 22,171 | done | OK | 0 | 1 | 0 | OK | 156 | 79 | 8 | no | uploaded | kzRugTuW0p3MSdou4CIM3 | ✓ | ✓ | 79/79 |  | retitled (see Retitled) |
| 433 | Va_3CEQ | medium | 43,717 | done | OK | 0 | 2 | 0 | OK | 27 | 210 | 5 | no | uploaded | EWUzRJMUZvp8mAg6Tm3US | ✓ | ✓ | 210/210 |  |  |
| 434 | Va_3CER | large | 436,361 | done | OK | 0 | 2 | 0 | OK | 1060 | 2175 | 7 | no | uploaded | ERlrGXfZY8KeDuzT8bt7B | ✓ | ✓ | 2175/2175 |  |  |
| 435 | Va_3CES | medium | 42,227 | done | OK | 0 | 2 | 0 | OK | 98 | 164 | 8 | no | uploaded | JwJwfgju6zgrxnw6GXgk6 | ✓ | ✓ | 164/164 |  |  |
| 436 | Va_3CET | small | 5,571 | done | OK | 0 | 3 | 0 | OK | 19 | 21 | 6 | no | uploaded | cBiXoCqNJ3W8WYUwP3rOA | ✓ | ✓ | 21/21 |  |  |
| 437 | Va_3CEX | medium | 93,615 | done | OK | 0 | 1 | 0 | OK | 614 | 379 | 14 | no | uploaded | OkZN3zxjraovr2PmeWnXX | ✓ | ✓ | 379/379 |  |  |
| 438 | Va_3CEY | small | 5,654 | done | OK | 0 | 2 | 0 | OK | 32 | 22 | 9 | no | uploaded | 6VRNBFWMdEWUhh7opvn0g | ✓ | ✓ | 22/22 |  |  |
| 439 | Va_3CEa_ | small | 4,108 | done | OK | 0 | 2 | 0 | OK | 24 | 12 | 7 | no | uploaded | oPWJd6xHM4ly3JwsMVyJu | ✓ | ✓ | 12/12 |  |  |
| 440 | Va_3CEb_ | small | 3,361 | done | OK | 0 | 2 | 0 | OK | 15 | 16 | 6 | no | uploaded | 6LTx5dNTDLvKpIg8hziQR | ✓ | ✓ | 16/16 |  |  |
| 441 | Va_3CEc_ | small | 8,070 | done | OK | 0 | 2 | 0 | OK | 33 | 43 | 8 | no | uploaded | G9x2fOzFrTxDAS8s43PUR | ✓ | ✓ | 43/43 |  |  |
| 442 | Va_3CEd_ | small | 2,769 | done | OK | 0 | 2 | 0 | OK | 11 | 16 | 5 | no | uploaded | 4DEeMw342tjhHlZ0ZfH7A | ✓ | ✓ | 16/16 |  |  |

## Failures

Every text that failed lint, parse or upload. `error` is what the script recorded; `verified reason` is what investigating it found (kept in `0-INBOX/temp/api-lint/failure-reasons.json`). A text leaves this list, and its reason is removed, as soon as it succeeds.

None.

### Held — never run

Listed in `0-INBOX/temp/api-lint/holds.json`; remove a text there to release it.

| id | reason |
|---|---|
| At_3CFp_ | duplicate of At_3CFl_ (uploaded): identical main text and footnotes; same BDRC WA0RT4268, same volume (Book 98) |
| At_3CGa_ | duplicate of At_3CGQ (uploaded): identical main text and footnotes (one verse is split over three lines instead of one); same BDRC WA0RT2596, same volume (Book 98) |
| Bh_3CCO | duplicate of Bh_3CCJ (uploaded): identical text and footnotes except one editorial heading (དམ་པའི་དོན། vs དོན་དམ།); same BDRC WA0RT3202; printed in Book 34 ཆ and Book 31 ག |
| Na_3C9S | near-duplicate of Ar_3CBf_ (uploaded): same translation, edited separately; see source_description |
| Sh_3CCm_ | held by request (2026-10-13) |
| Sh_3CFZ | near-duplicate of Na_3CBB (uploaded): same translation, edited separately; see source_description |

## Retitled

Texts whose `title:` was changed because the upload stopped on a title already in the library. The old title moved into `alt_titles`. Kept by hand in `0-INBOX/temp/api-lint/retitled.json`.

| id | old title | new title | clashed with | basis |
|---|---|---|---|---|
| As_3CDo_ | རྣལ་འབྱོར་སྤྱོད་པའི་ས་རྣམ་པར་གཏན་ལ་དབབ་པ་བསྡུ་བ། | རྣལ་འབྱོར་སྤྱོད་པའི་ས་རྣམ་པར་གཏན་ལ་དབབ་པ་བསྡུ་བ།༼སྟོད་ཆ།༽ | As_3CDp_ | Part 1 (Book 56) of a two-part work; As_3CDp_ (Book 57) is already ༼སྨད་ཆ།༽ and As_3CDp_ carries the colophon. Follows As_3CDk_ / As_3CDl_. Already uploaded: title patched on the library (PATCH /v2/texts/PTeAvbIVuWhNUWmDhTOvx, 2026-10-23). |
| At_3CG7 | མི་འཁྲུགས་པའི་སྒྲུབ་ཐབས། | བཅོམ་ལྡན་འདས་མི་འཁྲུགས་པའི་སྒྲུབ་ཐབས། | At_3CG6 | Own colophon title (^a-1). At_3CG6's colophon calls itself the extensive (རྒྱས་པ) sādhana; this is the short one. |
| At_3CGI | གཙུག་ཏོར་དྲི་མེད་ཀྱི་གཟུངས་ཆོག | གཙུག་ཏོར་དྲི་མ་མེད་པའི་གཟུངས་ཀྱི་ཆོ་ག | At_3CGH | Full form from its own ^I-2 and colophon (^a-1). Note: At_3CGH ends with the same wording (^1-7) — the two remain near-identical to readers. |
| At_3CGb_ | སྦྱིན་སྲེག་གི་ཆོ་ག | ཞི་བའི་སྦྱིན་སྲེག་གི་ཆོ་ག | At_3CG8 | Editorial: no distinct title is attested. The rite is pacifying in its own words (ཞི་བར་བྱ་བའི་ཕྱིར, ཞི་བའི་ཚིག, ཤནྟི་ཀུ་རུ ×2); At_3CG8 has none of these. |
| At_3CHB | སྤྱོད་པ་བསྡུས་པའི་སྒྲོན་མ། | ཇོ་བོ་རྗེའི་སྤྱོད་པ་བསྡུས་པའི་སྒྲོན་མ། | Ar_3CBc_ | Editorial author qualifier. Different works with the same Tibetan title: Atiśa's Caryāsaṃgrahapradīpa vs Āryadeva's Caryāmelāpakapradīpa (Sanskrit titles in ^I-1). ཇོ་བོ་རྗེ from the collection title. |
| At_3CHL | དཔལ་གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་གྱི་ཆོ་ག | དཔལ་གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་གྱི་ཆོ་ག༼མར་མེ་མཛད་བཟང་པོ།༽ | Na_3C9c_ | Author from its own colophon (^a-1 སློབ་དཔོན་མར་མེ་མཛད་བཟང་པོའི་ཞལ་སྔ་ནས་མཛད་པ). Different work from Na_3C9c_ (Nāgārjuna); both carry an author tag. Already uploaded: title patched on the library. |
| Bh_3CCM | དབུ་མའི་སྙིང་པོའི་འགྲེལ་པ་རྟོག་གེ་འབར་བ། | དབུ་མའི་སྙིང་པོའི་འགྲེལ་པ་རྟོག་གེ་འབར་བ།༼སྟོད་ཆ།༽ | Bh_3CCN | Commentary. Part 1 (Book 33, bam po 1–15) of a two-part work; Bh_3CCN (Book 34, bam po 16 on) labels itself ༼སྨད་ཆ།༽. Both share bdrc WA0RT3201. Already uploaded: title patched on the library (PATCH /v2/texts/nLztNphtFnyVCn3pNvjVj, 2026-10-27). |
| Bh_3CCN | དབུ་མའི་སྙིང་པོའི་འགྲེལ་པ་རྟོག་གེ་འབར་བ། | དབུ་མའི་སྙིང་པོའི་འགྲེལ་པ་རྟོག་གེ་འབར་བ།༼སྨད་ཆ།༽ | Bh_3CCM | Commentary. Part 2 (Book 34, bam po 16 on); its own heading reads ༼སྨད་ཆ།༽. Bh_3CCM (Book 33, bam po 1–15) is part 1. Uploaded 2026-10-27 as fP3mROrpMeyUajTzGv0CS, without a bdrc id: the library keeps one text per BDRC id, so Bh_3CCM carries WA0RT3201 (as with Va_3CE2 / Va_3CE3). Its wrong alt title '…བམ་པོ་དང་པོ།' (bam po 1) was dropped. |
| Ch_3CCU | གྲུབ་ཐོབ་ལྔ་བཅུའི་རྟོགས་པ་བརྗོད་པ་ཐིག་ལེ་འོད་ཀྱི་ཕྲེང་བ་ཞེས་བྱ་བ། | གྲུབ་ཐོབ་ལྔ་བཅུའི་རྟོགས་པ་བརྗོད་པ་ཐིག་ལེ་འོད་ཀྱི་ཕྲེང་བ་ཞེས་བྱ་བ།༼ཟླ་བ་གྲགས་པ།༽ | Na_3C9x_ · Sh_3CCh_ · Di_3CEi_ | One verse by ཟླ་བ་གྲགས་པ (^1-1 ཟླ་བ་གྲགས་པས་སྨྲས་པ།) from the 50-siddhas anthology; the four extracts share its title. Name as in the compiler's note (footnote) listing ཀླུ་སྒྲུབ། ཤཱནྟ་དེ་བ། ཕྱོགས་ཀྱི་གླང་པོ། ཟླ་བ་གྲགས་པ. |
| Ch_3CCX | ཕུང་པོ་ལྔའི་རབ་ཏུ་བྱེད་པ། | ཕུང་པོ་ལྔའི་རབ་ཏུ་བྱེད་པ།༼ཟླ་བ་གྲགས་པ།༽ | Va_3CEP | Author from its own colophon (^a-1 …སློབ་དཔོན་ཟླ་བ་གྲགས་པས་མཛད་པ). Different work from Va_3CEP (Vasubandhu); both carry an author tag. Already uploaded: title patched on the library. |
| Di_3CEi_ | གྲུབ་ཐོབ་ལྔ་བཅུའི་རྟོགས་པ་བརྗོད་པ་ཐིག་ལེ་འོད་ཀྱི་ཕྲེང་བ། | གྲུབ་ཐོབ་ལྔ་བཅུའི་རྟོགས་པ་བརྗོད་པ་ཐིག་ལེ་འོད་ཀྱི་ཕྲེང་བ་ཞེས་བྱ་བ།༼ཕྱོགས་ཀྱི་གླང་པོ།༽ | Ch_3CCU · Na_3C9x_ · Sh_3CCh_ | One verse by ཕྱོགས་ཀྱི་གླང་པོ (^1-1 ཕྱོགས་ཀྱི་གླང་པོས་སྨྲས་པ།) from the 50-siddhas anthology. ཞེས་བྱ་བ added from its own colophon (^a-1), matching the other three; the Dignāga volume (Book 75) heading lacks it. Already uploaded: title patched on the library. |
| Di_3CEj_ | དཔལ་ཨུ་རྒྱན་དུ་ཚོགས་འཁོར་བྱས་པའི་དུས་སུ་རྣལ་འབྱོར་པ་གྲུབ་པ་ཐོབ་པ་བཞི་བཅུས་རྡོ་རྗེའི་མགུར་བཞེངས་པ་ཉམས་ཀྱི་མན་ངག་ཐིག་ལེ་གསེར་གྱི་ཕྲེང་བ་ཞེས་བྱ་བ། | དཔལ་ཨུ་རྒྱན་དུ་ཚོགས་འཁོར་བྱས་པའི་དུས་སུ་རྣལ་འབྱོར་པ་གྲུབ་པ་ཐོབ་པ་བཞི་བཅུས་རྡོ་རྗེའི་མགུར་བཞེངས་པ་ཉམས་ཀྱི་མན་ངག་ཐིག་ལེ་གསེར་གྱི་ཕྲེང་བ་ཞེས་བྱ་བ།༼ཕྱོགས་ཀྱི་གླང་པོ།༽ | Na_3C9y_ · Sh_3CCi_ | One verse by ཕྱོགས་ཀྱི་གླང་པོ (^1-1 སློབ་དཔོན་ཕྱོགས་ཀྱི་གླང་པོའི་ཞལ་ནས།) from the 40-siddhas anthology. Name as in the compiler's note (footnote) listing ཀླུ་སྒྲུབ། ཕྱོགས་ཀྱི་གླང་པོ། བྷུ་སུ་ཀུ. Already uploaded: title patched on the library. |
| Ha_3CFG | ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟོང་ཕྲག་ཉི་ཤུ་ལྔ་པ། | ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟོང་ཕྲག་ཉི་ཤུ་ལྔ་པ།༼དེབ་གཉིས་པ།༽ | — | Volume 2 (Book 83) was missing its volume tag. Already uploaded: deleted (old text tce5facfRtmmMP067sELa) and re-uploaded under the new title. |
| Ha_3CFJ | ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟོང་ཕྲག་ཉི་ཤུ་ལྔ་པ། | ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟོང་ཕྲག་ཉི་ཤུ་ལྔ་པ།༼དེབ་ལྔ་པ།༽ | Ha_3CFG | Volume 5 (Book 86) of a five-volume set; follows the ༼དེབ་N།༽ pattern of Ha_3CFF / Ha_3CFH / Ha_3CFI. |
| Na_3C9T | དཔལ་ནག་པོ་ཆེན་པོའི་སྒྲུབ་ཐབས། | རྡོ་རྗེ་ནག་པོ་ཆེན་པོའི་སྒྲུབ་ཐབས། | Na_3C9R | Editorial, from its own homage (^I-2). Dropped 3 alt_titles not attested in the text (…ཞེས་བྱ་བ། is Na_3C9R's wording; …སྲོག་གི་སྤུ་གྲིའི… and གུར་མགོན་ལྷ་བཅུ་བདུན… match neither). |
| Na_3C9V | དཔལ་ནག་པོ་ཆེན་པོའི་བསྟོད་པ་རྐང་པ་བརྒྱད་པ། | དཔལ་ནག་པོ་ཆེན་པོའི་བསྟོད་པ་རྐང་པ་བརྒྱད་པ།༼དཔེ་དང་པོ།༽ | Na_3C9W · Na_3C9X | Same work, different version: no distinguishing title is attested, so versions are numbered in volume order. Version 1: Sanskrit title …aṣṭapadastotra; 10 verses; colophon names Nāgārjuna only, no translator. Already uploaded: title patched on the library. |
| Na_3C9W | དཔལ་ནག་པོ་ཆེན་པོའི་བསྟོད་པ་རྐང་པ་བརྒྱད་པ། | དཔལ་ནག་པོ་ཆེན་པོའི་བསྟོད་པ་རྐང་པ་བརྒྱད་པ།༼དཔེ་གཉིས་པ།༽ | Na_3C9V · Na_3C9X | Same work, different version: no distinguishing title is attested, so versions are numbered in volume order. Version 2: Sanskrit title …aṣṭamantrastotra; verses reordered and reworded; lacks Na_3C9V's verses 4, 8 and 10; adds the ཀྵཾ verse and a closing benefit verse; no translator named. |
| Na_3C9X | དཔལ་ནག་པོ་ཆེན་པོའི་བསྟོད་པ་རྐང་པ་བརྒྱད་པ། | དཔལ་ནག་པོ་ཆེན་པོའི་བསྟོད་པ་རྐང་པ་བརྒྱད་པ།༼དཔེ་གསུམ་པ།༽ | Na_3C9V · Na_3C9W | Same work, different version: no distinguishing title is attested, so versions are numbered in volume order. Version 3: Sanskrit title …aṣṭamantrastotra; Na_3C9V's verses in the same order with spelling variants, verse 6 replaced and verse 8 missing; translated by Vairocanavajra and Ldi ri chos grags (^a-1). |
| Na_3C9c_ | དཔལ་གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་གྱི་ཆོ་ག | དཔལ་གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་གྱི་ཆོ་ག༼ཀླུ་སྒྲུབ།༽ | At_3CHL | Author from its own colophon (^a-1 …སློབ་དཔོན་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་སྔ་ནས་མཛད་པ). Different work from At_3CHL (Dīpaṃkarabhadra; ~14% shared, different homage, paṇḍita and BDRC id); both carry an author tag. |
| Na_3C9x_ | གྲུབ་ཐོབ་ལྔ་བཅུའི་རྟོགས་པ་བརྗོད་པ་ཐིག་ལེ་འོད་ཀྱི་ཕྲེང་བ་ཞེས་བྱ་བ། | གྲུབ་ཐོབ་ལྔ་བཅུའི་རྟོགས་པ་བརྗོད་པ་ཐིག་ལེ་འོད་ཀྱི་ཕྲེང་བ་ཞེས་བྱ་བ།༼ཀླུ་སྒྲུབ།༽ | Ch_3CCU · Sh_3CCh_ · Di_3CEi_ | One verse by Nāgārjuna (^1-1 ནཱ་གཱརྫུ་ནས་གསུངས་པ།) from the 50-siddhas anthology. ཀླུ་སྒྲུབ as in the compiler's note (footnote) listing ཀླུ་སྒྲུབ། ཤཱནྟ་དེ་བ། ཕྱོགས་ཀྱི་གླང་པོ། ཟླ་བ་གྲགས་པ and Na_3C9y_. |
| Na_3C9y_ | དཔལ་ཨུ་རྒྱན་དུ་ཚོགས་འཁོར་བྱས་པའི་དུས་སུ་རྣལ་འབྱོར་པ་གྲུབ་པ་ཐོབ་པ་བཞི་བཅུས་རྡོ་རྗེའི་མགུར་བཞེངས་པ་ཉམས་ཀྱི་མན་ངག་ཐིག་ལེ་གསེར་གྱི་ཕྲེང་བ་ཞེས་བྱ་བ། | དཔལ་ཨུ་རྒྱན་དུ་ཚོགས་འཁོར་བྱས་པའི་དུས་སུ་རྣལ་འབྱོར་པ་གྲུབ་པ་ཐོབ་པ་བཞི་བཅུས་རྡོ་རྗེའི་མགུར་བཞེངས་པ་ཉམས་ཀྱི་མན་ངག་ཐིག་ལེ་གསེར་གྱི་ཕྲེང་བ་ཞེས་བྱ་བ།༼ཀླུ་སྒྲུབ།༽ | Di_3CEj_ · Sh_3CCi_ | One verse by ཀླུ་སྒྲུབ (^1-1 སློབ་དཔོན་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་ནས།) from the 40-siddhas anthology; the three extracts share its title. Name as in the compiler's note (footnote) listing ཀླུ་སྒྲུབ། ཕྱོགས་ཀྱི་གླང་པོ། བྷུ་སུ་ཀུ. |
| Na_3CAN | རྡོ་རྗེ་སྒྲོལ་མའི་སྒྲུབ་ཐབས། | རྡོ་རྗེ་སྒྲོལ་མའི་སྒྲུབ་ཐབས།༼དཔེ་དང་པོ།༽ | Na_3CAO | Same work, different version: no distinguishing title is attested, so versions are numbered in volume order. Version 1: the shorter wording of the same rite sequence as Na_3CAO; homage རྡོ་རྗེ་སྒྲོལ་མ་ལ; no author or translator named. |
| Na_3CAO | རྡོ་རྗེ་སྒྲོལ་མའི་སྒྲུབ་ཐབས། | རྡོ་རྗེ་སྒྲོལ་མའི་སྒྲུབ་ཐབས།༼དཔེ་གཉིས་པ།༽ | Na_3CAN | Same work, different version: no distinguishing title is attested, so versions are numbered in volume order. Version 2: the fuller wording of the same rite sequence as Na_3CAN; homage འཕགས་མ་སྒྲོལ་མ་ལ; no author or translator named. Already uploaded: title patched on the library. |
| Na_3CAP | རྡོ་རྗེ་སྒྲོལ་མའི་སྒྲུབ་ཐབས། | རྡོ་རྗེ་སྒྲོལ་མའི་སྒྲུབ་ཐབས།༼ཀླུ་སྒྲུབ།༽ | Na_3CAN · Na_3CAO | Author tag from its own colophon (^a-1 …སློབ་དཔོན་འཕགས་པ་ཀླུ་སྒྲུབ་ཞབས་ཀྱིས་མཛད་པ); a different, much shorter sādhana than Na_3CAN / Na_3CAO (5% and 13% shared), whose texts name no author. BDRC WA0RT4261 (the other two have none). |
| Na_3CBW | བཀྲ་ཤིས་ཀྱི་ཚིགས་སུ་བཅད་པ། | དཀོན་མཆོག་གསུམ་དང་མཛད་པ་བཅུ་གཉིས་ཀྱི་བཀྲ་ཤིས་ཀྱི་ཚིགས་སུ་བཅད་པ། | Na_3CBX | Own colophon title (^a-1 དཀོན་མཆོག་གསུམ་དང་མཛད་པ་བཅུ་གཉིས་ཀྱི་བཀྲ་ཤིས་ཀྱི་ཚིགས་སུ་བཅད་པ་སློབ་དཔོན་འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱིས་མཛད་པ). Different work from Na_3CBX (20% similar; buddha and bodhisattva names), which keeps the plain title its own colophon gives. Same author and translators, so an author tag would not separate them. Already uploaded: title patched on the library. |
| Sh_3CCh_ | གྲུབ་ཐོབ་ལྔ་བཅུའི་རྟོགས་པ་བརྗོད་པ་ཐིག་ལེ་འོད་ཀྱི་ཕྲེང་བ་ཞེས་བྱ་བ། | གྲུབ་ཐོབ་ལྔ་བཅུའི་རྟོགས་པ་བརྗོད་པ་ཐིག་ལེ་འོད་ཀྱི་ཕྲེང་བ་ཞེས་བྱ་བ།༼ཤཱནྟ་དེ་བ།༽ | Ch_3CCU · Na_3C9x_ · Di_3CEi_ | One verse by ཤཱནྟ་དེ་བ (^1-1 ཤཱནྟ་དེ་བས་གསུངས་པ།) from the 50-siddhas anthology. Name as in the compiler's note (footnote) listing ཀླུ་སྒྲུབ། ཤཱནྟ་དེ་བ། ཕྱོགས་ཀྱི་གླང་པོ། ཟླ་བ་གྲགས་པ. |
| Sh_3CCi_ | དཔལ་ཨུ་རྒྱན་དུ་ཚོགས་འཁོར་བྱས་པའི་དུས་སུ་རྣལ་འབྱོར་པ་གྲུབ་པ་ཐོབ་པ་བཞི་བཅུས་རྡོ་རྗེའི་མགུར་བཞེངས་པ་ཉམས་ཀྱི་མན་ངག་ཐིག་ལེ་གསེར་གྱི་ཕྲེང་བ་ཞེས་བྱ་བ། | དཔལ་ཨུ་རྒྱན་དུ་ཚོགས་འཁོར་བྱས་པའི་དུས་སུ་རྣལ་འབྱོར་པ་གྲུབ་པ་ཐོབ་པ་བཞི་བཅུས་རྡོ་རྗེའི་མགུར་བཞེངས་པ་ཉམས་ཀྱི་མན་ངག་ཐིག་ལེ་གསེར་གྱི་ཕྲེང་བ་ཞེས་བྱ་བ།༼བྷུ་སུ་ཀུ།༽ | Na_3C9y_ · Di_3CEj_ | One verse by བྷུ་སུ་ཀུ (^1-1 བྷུ་སུ་ཀུའི་ཞལ་ནས།) from the 40-siddhas anthology. Name as in the compiler's note (footnote) listing ཀླུ་སྒྲུབ། ཕྱོགས་ཀྱི་གླང་པོ། བྷུ་སུ་ཀུ. |
| Sh_3CCs_ | བསླབ་པ་ཀུན་ལས་བཏུས་པ། | བསླབ་པ་ཀུན་ལས་བཏུས་པ།༼སྟོད་ཆ།༽ | Sh_3CCt_ | Part 1 (Book 41, chapters 1–5) of a two-part work; Sh_3CCt_ (Book 42, chapter 6 on, colophon) is already ༼སྨད་ཆ།༽. Already uploaded: title patched on the library (PATCH /v2/texts/8Rny2ucutFoSoG5TmR9q5, 2026-10-23). |
| Va_3CEP | ཕུང་པོ་ལྔའི་རབ་ཏུ་བྱེད་པ། | ཕུང་པོ་ལྔའི་རབ་ཏུ་བྱེད་པ།༼དབྱིག་གཉེན།༽ | Ch_3CCX | Author from its own colophon (^a-1 …སློབ་དཔོན་དབྱིག་གཉེན་གྱིས་མཛད་པ). Different work from Ch_3CCX (Candrakīrti, ~5× longer, different BDRC id); both carry an author tag. |
