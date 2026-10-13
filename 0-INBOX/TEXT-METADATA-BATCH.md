# Text metadata batch — YAML frontmatter for 0-INBOX/root and 0-INBOX/commentary

Every text in `0-INBOX/root` and `0-INBOX/commentary` got a YAML frontmatter block from `0-INBOX/text-relations.json`. This document says which texts carry OpenPecha metadata and which do not. How to re-run: `venv\Scripts\python.exe -X utf8 0-INBOX\temp\text-relations\write_frontmatter.py` (re-runnable: it replaces only the block it wrote; the text body is never changed).

Updated 2026-10-13 · 565 texts · file_type commentary 135 · file_type root-text 430 · with OpenPecha metadata 362 · without OpenPecha metadata 203

| Field | From |
|---|---|
| `title` | the file's own heading line, without `༄༅། །` and `བཞུགས་སོ` |
| `alt_titles` | the heading as written (bo) + the OpenPecha record's titles in other languages the backend knows (cmg titles are kept only in `text-relations.json`); `sa` titles transliterated from IAST to Devanagari |
| `file_type` | the reading (`text-relations.json`); where undecided, the folder |
| `root_text` | for a commentary: the file it comments on (`commentary_of`), when it is in our corpus |
| `author`, `author_in_english`, `bdrc_work_id`, `openpecha_text_id` | the matched OpenPecha record (`OpenPecha` = yes); empty otherwise |
| `license` | `public` (OpenPecha's `Public Domain Mark`, and every text without an OpenPecha license) |
| `source` | `https://webuddhist.com/` |
| `source_description` | our file (the Nalanda printed edition: corpus, docx, pandita), then its wb.pub link |
| `category_id`, `category_name` | our backend category, mapped from the matched record's OpenPecha category; empty otherwise |
| `pandita` | `1-SOURCES/Text/text_catalog.json`, as written there (e.g. `01-Nagarjuna`) |
| `language`, `lang_tag` | our file (the Nalanda printed edition) |
| `date`, `verse_id_format`, `registered_id`, `covers_verses` | not in the data: left empty |

`OpenPecha` yes = the file's text was matched to an OpenPecha record (same title, text checked). `match` = the text check (`same-text`, `part`, `title-only`) or why there is no metadata.

## Summary

| Folder | Texts | root-text | commentary | with OpenPecha metadata | without |
|---|---|---|---|---|---|
| `0-INBOX/root` | 442 | 430 | 12 | 290 | 152 |
| `0-INBOX/commentary` | 123 | 0 | 123 | 72 | 51 |
| **all** | 565 | 430 | 135 | 362 | 203 |

**OpenPecha metadata — 362 texts.** Text check of the match: same-text 357, part 4, title-only 1. Of these, 340 have an author and 361 a BDRC work id.

**No OpenPecha metadata — 203 texts:** no OpenPecha record has this title (183); title matched, text check: different (13); title matched, text check: fragment (7).

**Commentaries — 135:** `root_text` filled for 62 (the root is one of our files); for 73 the root is not in our corpus.

**`file_type` differs from the folder — 12:** Ar_3CBm_ (commentary in `root`), At_3CFd_ (commentary in `root`), At_3CGP (commentary in `root`), At_3CHH (commentary in `root`), Di_3CEl_ (commentary in `root`), Ha_3CFF (commentary in `root`), Ha_3CFG (commentary in `root`), Ha_3CFH (commentary in `root`), Ha_3CFI (commentary in `root`), Ha_3CFJ (commentary in `root`), Na_3CAF (commentary in `root`), Na_3CAY (commentary in `root`).

**Reading undecided, `file_type` from the folder — 3:** At_3CGq_ (root-text), Di_3CEh_ (commentary), Na_3C9L (commentary).

**Same text in two files — 5 pairs:** Ar_3CBf_ = Na_3C9S, At_3CFl_ = At_3CFp_, At_3CGQ = At_3CGa_, Bh_3CCJ = Bh_3CCO, Na_3CBB = Sh_3CFZ.

## Categories

`category_id` / `category_name` are our backend's (13 categories): mapped from the matched record's OpenPecha category, or — for texts without one — decided by reading the text (pass 3; column `→ our category` says which, the evidence is in `0-INBOX/temp/text-relations/context.json`).

| Our category | bo | id | from OpenPecha | by reading | texts |
|---|---|---|---|---|---|
| Prajñāpāramitā | ཤེར་ཕྱིན། | `uGpinx0GZlvU1uw44RyYS` | 10 | 10 | 20 |
| Liturgy | ཞལ་འདོན། | `LCorCb2K98p3TICt3UCDm` | 0 | 4 | 4 |
| Systematic Treatises | མངོན་པ། | `MZUUxphQ0yFwLBon3Vng8` | 4 | 3 | 7 |
| Middle Way | དབུ་མ། | `JD5ULLPAV1cxg7RSb7L3q` | 74 | 17 | 91 |
| Tantras | རྒྱུད་སྡེ། | `REBGnT4qFooPfPEkR5pe5` | 160 | 118 | 278 |
| Miscellaneous | སྣ་ཚོགས། | `SoGlGBaboYkVa7b9qJvvK` | 39 | 2 | 41 |
| Mind-only Treatises | སེམས་ཙམ། | `NDXKdNtZe9Kxl6Y4yBMAr` | 26 | 7 | 33 |
| Logic | ཚད་མ། | `v3L4eTn4x2E30znIhHvQe` | 18 | 6 | 24 |
| Mind Trainings and Advices | བློ་སྦྱོང་དང་བསླབ་བྱ། | `sEStEY4RRWU7U23rkiOk5` | 10 | 5 | 15 |
| Discourses | མདོ་སྡེ། | `XfCwZpoJMtfO7s0laQkdK` | 8 | 18 | 26 |
| Monastic Rules | འདུལ་བ། | `4wuvGxIgXNZ5mb0bDWvkC` | 8 | 5 | 13 |
| Linguistics Treatises | རིག་གནས། | `Rrl0usffAJJbYTYe1euws` | 4 | 6 | 10 |
| History and Stories | ལོ་རྒྱུས་དང་སྒྲུང་། | `YQnenyXmCd2VbVHPUFGWM` | 1 | 0 | 1 |
| **all** | | | 362 | 201 | **563** |

**No category — 2 texts:** As_3CDy_, As_3CDz_.

**Decided by reading at low confidence — 7:** Ar_3CC7 (Tantras), At_3CGp_ (Linguistics Treatises), At_3CHA (Middle Way), At_3CHF (Liturgy), Di_3CEi_ (Tantras), Sh_3CCp_ (Linguistics Treatises), Sh_3CCu_ (Linguistics Treatises).

## Texts

| # | id | folder | file_type | type from | OpenPecha | match | OpenPecha id | BDRC work | author (OpenPecha) | root_text | note | OpenPecha category | → our category | genre (title) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ar_3CBa_ | root | root-text | context | yes | same-text | XPEX73Pzgw6hAqQVWVltQ | WA0RT0484 | Caryāvratipāda |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 2 | Ar_3CBc_ | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) |  |
| 3 | Ar_3CBe_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | offering (`མཆོད་པ`) |
| 4 | Ar_3CBf_ | root | root-text | context | yes | same-text | RfiSq2NSQebaytc7bobIU | WA0RT0629 |  |  | same text as Na_3C9S | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 5 | Ar_3CBg_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 6 | Ar_3CBh_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 7 | Ar_3CBi_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 8 | Ar_3CBj_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 9 | Ar_3CBk_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 10 | Ar_3CBl_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 11 | Ar_3CBm_ | root | commentary | context | no | no OpenPecha record has this title |  |  |  | Ch_3CCa_ | reading says commentary, folder says root-text |  | Tantras (reading) |  |
| 12 | Ar_3CBn_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 13 | Ar_3CBo_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 14 | Ar_3CBp_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོག`) |
| 15 | Ar_3CBq_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 16 | Ar_3CBr_ | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | praise (`བསྟོད`) |
| 17 | Ar_3CBs_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 18 | Ar_3CBt_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 19 | Ar_3CBu_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 20 | Ar_3CBv_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 21 | Ar_3CBw_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | fire offering (`སྦྱིན་སྲེག`) |
| 22 | Ar_3CBx_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | torma ritual (`གཏོར་ཆོག`) |
| 23 | Ar_3CBy_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 24 | Ar_3CBz_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 25 | Ar_3CC1 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 26 | Ar_3CC2 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 27 | Ar_3CC3 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 28 | Ar_3CC5 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 29 | Ar_3CC6 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 30 | Ar_3CC7 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 31 | Ar_3CC8 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 32 | Ar_3CC9 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 33 | Ar_3CCA | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 34 | Ar_3CCB | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 35 | As_3CDc_ | root | root-text | context | yes | same-text | MVkHUVRd20sSBptTUtSrD | WA0RT0007 | asanga |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 36 | As_3CDd_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 37 | As_3CDe_ | root | root-text | context | yes | same-text | 5QN8xHUy0exsXEoxAMEKB | WA0RT4330 | asanga |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 38 | As_3CDk_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind-only Treatises (reading) |  |
| 39 | As_3CDl_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind-only Treatises (reading) |  |
| 40 | As_3CDm_ | root | root-text | context | yes | same-text | dRLTW3FCAjFRdKzlAko1j | WA0RT3375 | asanga |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 41 | As_3CDn_ | root | root-text | context | yes | same-text | I2FQrsNgQNyJ47Y31TSFN | WA0RT3376 | asanga |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 42 | As_3CDo_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind-only Treatises (reading) |  |
| 43 | As_3CDp_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind-only Treatises (reading) |  |
| 44 | As_3CDq_ | root | root-text | context | yes | same-text | RvNOpmhz4pYcjdaanrLdN | WA0RT3378 | asanga |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 45 | As_3CDr_ | root | root-text | context | yes | same-text | Qg5O4UsM0FM4DZ3CUW8y3 | WA0RT3379 | asanga |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 46 | As_3CDs_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind-only Treatises (reading) |  |
| 47 | As_3CDt_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind-only Treatises (reading) |  |
| 48 | As_3CDu_ | root | root-text | context | yes | same-text | BRZfa4NP4zhTRUuXAHDSS | WA0RT3387 | asanga |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 49 | As_3CDv_ | root | root-text | context | yes | same-text | tJLRgbxl8ZVoRqRfY1RhF | WA0RT3388 | asanga |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 50 | As_3CDw_ | root | root-text | context | yes | same-text | LnroVeizznKtitIAwYvF0 | WA0RT3411 | asanga |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 51 | At_3CFb_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 52 | At_3CFc_ | root | root-text | context | yes | same-text | De4TGIGzuj6LcdG5YNQ9a | WA0RT0418 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | torma ritual (`གཏོར་མ`) |
| 53 | At_3CFd_ | root | commentary | context | yes | same-text | uuWC41Y72QYUfy28FzOur | WA0RT0205 | Atiśa |  | reading says commentary, folder says root-text; root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`མངོན་པར་རྟོགས་པ`) |
| 54 | At_3CFe_ | root | root-text | context | yes | same-text | K3hfHt5kxokRQtOBoDr2z | WA0RT0206 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 55 | At_3CFf_ | root | root-text | context | yes | same-text | 8rQXayWpQpU8SRB5aiD8t | WA0RT0207 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`མངོན་པར་རྟོགས་པ`) |
| 56 | At_3CFg_ | root | root-text | context | yes | same-text | auVmEBt1TAqO3VxLdodtK | WA0RT0181 | the tiger rider |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 57 | At_3CFh_ | root | root-text | context | yes | same-text | UoheBk4d87TM1fjyRlzZa | WA0RT0209 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 58 | At_3CFj_ | root | root-text | context | yes | same-text | 0AXCDgzfRkDdquWd2aScM | WA0RT0211 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 59 | At_3CFl_ | root | root-text | context | yes | same-text | sy2lyMSSpO2UT8P9ahIir | WA0RT4268 | Atiśa |  | same text as At_3CFp_ | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 60 | At_3CFm_ | root | root-text | context | yes | same-text | A5PlE2bxUTjb5nvTshS6N | WA0RT0302 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 61 | At_3CFn_ | root | root-text | context | yes | same-text | KNkziQWBDIWdviqXFIzPh | WA0RT0303 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 62 | At_3CFo_ | root | root-text | context | yes | same-text | lpiYDKO99Te3lMG8PmXcw | WA0RT0304 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 63 | At_3CFp_ | root | root-text | context | yes | same-text | sy2lyMSSpO2UT8P9ahIir | WA0RT4268 | Atiśa |  | same text as At_3CFl_ | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 64 | At_3CFq_ | root | root-text | context | yes | same-text | nYaRRtvzttT0iH4ZvpCX3 | WA0RT0567 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོག`) |
| 65 | At_3CFr_ | root | root-text | context | yes | same-text | 3ZDfmvnJLbsVl5Qt3jsdR | WA0RT3079 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 66 | At_3CFs_ | root | root-text | context | yes | same-text | ZQemBh8B8edb7iCjcEjm4 | WA0RT0634 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | torma ritual (`གཏོར་མ`) |
| 67 | At_3CFt_ | root | root-text | context | yes | same-text | 57r8L2Eje00B9n1QoT9aI | WA0RT0755 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | empowerment (`དབང`) |
| 68 | At_3CFu_ | root | root-text | context | yes | same-text | uqSis4gZSmogAosA4CaAL | WA0RT0756 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | empowerment (`དབང`) |
| 69 | At_3CFv_ | root | root-text | context | yes | same-text | H5ejdhkNwEc1NB8UKhgqF | WA0RT0757 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 70 | At_3CFw_ | root | root-text | context | yes | same-text | GdXPD9CxLYlsgVSMH0fSu | WA0RT0808 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 71 | At_3CFx_ | root | root-text | context | yes | same-text | M67rmXd6Lf0okwmqh5T80 | WA0RT0813 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 72 | At_3CFy_ | root | root-text | context | yes | same-text | 3aU4VG3QkfXvxiGTupWtt | WA0RT0814 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 73 | At_3CFz_ | root | root-text | context | yes | same-text | N0XsANIQxHVQjhOnJAHhR | WA0RT0815 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 74 | At_3CG0 | root | root-text | context | yes | same-text | BKucmMeXnnQExpbAKclj4 | WA0RT1151 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 75 | At_3CG1 | root | root-text | context | yes | same-text | cJ41rLgnunB6kxGo24DDj | WA0RT1152 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 76 | At_3CG2 | root | root-text | context | yes | same-text | 0CjYYnCmXLHAif8x45fJx | WA0RT1201 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 77 | At_3CG3 | root | root-text | context | yes | same-text | ihPOuzu5VcQt6pz5EoDMV | WA0RT1287 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 78 | At_3CG4 | root | root-text | context | yes | same-text | 7HPpqLPKvLM0sVeKJKWeB | WA0RT1288 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 79 | At_3CG5 | root | root-text | context | yes | same-text | a9zGNBxDddAMmATledK1v | WA0RT1321 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 80 | At_3CG6 | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 81 | At_3CG7 | root | root-text | context | yes | same-text | LwdAfF7Clc5mt983kaJLS | WA0RT1477 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 82 | At_3CG8 | root | root-text | context | yes | same-text | qnKDyHFvqMlTcVAO5r4Pf | WA0RT3973 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | fire offering (`སྦྱིན་སྲེག`) |
| 83 | At_3CG9 | root | root-text | context | yes | same-text | ph5zYVylX6yUw9NlA1RAh | WA0RT1526 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 84 | At_3CGA | root | root-text | context | yes | same-text | fBhYtpmzn0iYJ5joDSNMZ | WA0RT1712 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 85 | At_3CGa_ | root | root-text | context | yes | same-text | 7wyRsny8NkbD6yJF3XybU | WA0RT2596 | Atiśa |  | same text as At_3CGQ | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 86 | At_3CGB | root | root-text | context | yes | same-text | RIM3cmtI0ud69tHQTygv8 | WA0RT1880 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 87 | At_3CGb_ | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | fire offering (`སྦྱིན་སྲེག`) |
| 88 | At_3CGC | root | root-text | context | yes | same-text | tWYYudwg93TKbJ4OWUS8q | WA0RT1881 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 89 | At_3CGc_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | offering (`མཆོད་པ`) |
| 90 | At_3CGD | root | root-text | context | yes | same-text | 9DOYusRTu4c93nsLVkBGu | WA0RT1883 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 91 | At_3CGd_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 92 | At_3CGE | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | praise (`བསྟོད`) |
| 93 | At_3CGe_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 94 | At_3CGF | root | root-text | context | yes | same-text | Viu4jNlx2ZqZ8nVckatiJ | WA0RT1897 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 95 | At_3CGf_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 96 | At_3CGG | root | root-text | context | yes | same-text | TvwTTUqjArooiMI0m3rDx | WA0RT4316 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 97 | At_3CGg_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 98 | At_3CGH | root | root-text | context | yes | same-text | r3Lb6Sc6XJYSk94bGj5w4 | WA0RT1899 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོག`) |
| 99 | At_3CGh_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 100 | At_3CGI | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོག`) |
| 101 | At_3CGi_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 102 | At_3CGJ | root | root-text | context | yes | same-text | 1KiKAhp15ugTUjgAAEvoT | WA0RT1165 | kamalashila |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 103 | At_3CGj_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 104 | At_3CGK | root | root-text | context | yes | same-text | 3Jow2uWiaBeRqvZbjQkrh | WA0RT2509 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 105 | At_3CGk_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | praise (`བསྟོད`) |
| 106 | At_3CGL | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Liturgy (reading) | praise (`བསྟོད`) |
| 107 | At_3CGl_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 108 | At_3CGM | root | root-text | context | yes | same-text | 2nSvvtvQGlu689eKvTKOi | WA0RT4276 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 109 | At_3CGm_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 110 | At_3CGN | root | root-text | context | yes | same-text | bKhOeGmLnqmIg7s4IrIhZ | WA0RT2546 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 111 | At_3CGn_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 112 | At_3CGO | root | root-text | context | yes | same-text | aq4SrzPHY79HFWEYcnevb | WA0RT2560 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 113 | At_3CGo_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | praise (`བསྟོད`) |
| 114 | At_3CGP | root | commentary | context | yes | same-text | gtSMW4FTcKrYh97M9Im2u | WA0RT2595 | Atiśa |  | reading says commentary, folder says root-text; root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | torma ritual (`གཏོར་མ`) |
| 115 | At_3CGp_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Linguistics Treatises (reading) |  |
| 116 | At_3CGQ | root | root-text | context | yes | same-text | 7wyRsny8NkbD6yJF3XybU | WA0RT2596 | Atiśa |  | same text as At_3CGa_ | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 117 | At_3CGq_ | root | root-text | folder | yes | same-text | MB7llOAAPUjdcaerSQcsF | WA0RT3149 | Atiśa |  | reading undecided — file_type from the folder | Perfection of Wisdom / ཤེར་ཕྱིན། | Prajñāpāramitā (openpecha) |  |
| 118 | At_3CGR | root | root-text | context | yes | same-text | lQ64CnLRRszHtXrMmxxW6 | WA0RT2597 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 119 | At_3CGS | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | torma ritual (`གཏོར་མ`) |
| 120 | At_3CGs_ | root | root-text | context | yes | same-text | BMpGHcZDooAyEM01w1fLK | WA0RT3247 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 121 | At_3CGT | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 122 | At_3CGt_ | root | root-text | context | yes | same-text | FbczyBG3x2dYXkXEfQgv0 | WA0RT3269 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 123 | At_3CGU | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 124 | At_3CGu_ | root | root-text | context | yes | same-text | 2dJuCpRJGECqpopHRwKqh | WA0RT3270 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 125 | At_3CGV | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 126 | At_3CGv_ | root | root-text | context | yes | same-text | CyieKwL4ol7BHseRe2zkQ | WA0RT3271 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 127 | At_3CGW | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 128 | At_3CGX | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | empowerment (`དབང`) |
| 129 | At_3CGx_ | root | root-text | context | yes | same-text | P7lHFUht04aeZVDAYQMnX | WA0RT3287 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 130 | At_3CGY | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 131 | At_3CGy_ | root | root-text | context | yes | same-text | AZqMlFYbexzCNhdVPmx56 | WA0RT3288 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 132 | At_3CGZ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 133 | At_3CH0 | root | root-text | context | yes | same-text | PZ6UUw9ya1pxW1oTGLnMV | WA0RT3290 |  |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 134 | At_3CH1 | root | root-text | context | yes | same-text | ZTl2KoAkL532xHubE6VGG | WA0RT3291 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 135 | At_3CH2 | root | root-text | context | yes | same-text | Uo5TeDAgUQytycIeyBPrh | WA0RT3292 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 136 | At_3CH3 | root | root-text | context | yes | same-text | EFcMQvcKCN2yLyPOtTYhD | WA0RT3293 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 137 | At_3CH4 | root | root-text | context | yes | same-text | IuM9WJB1gOcT8EQpKug4a | WA0RT3294 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 138 | At_3CH5 | root | root-text | context | yes | same-text | C2J6a0dL9Qlpdnzd5QL9J | WA0RT3295 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 139 | At_3CH6 | root | root-text | context | yes | same-text | svcAQV2TEKJE1um5DPLxP | WA0RT3296 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 140 | At_3CH7 | root | root-text | context | yes | same-text | YNhmCY6hhEBHUUmo4itLr | WA0RT3297 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 141 | At_3CH8 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 142 | At_3CH9 | root | root-text | context | yes | same-text | TY9lcCV6wWnhPOu7GREuQ | WA0RT3299 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 143 | At_3CHA | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 144 | At_3CHa_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 145 | At_3CHB | root | root-text | context | yes | same-text | nXb2hYHFhCQonSlOqJZfn | WA0RT4342 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 146 | At_3CHb_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 147 | At_3CHC | root | root-text | context | yes | same-text | 7ayOvKQSc0bfrswVJBZto | WA0RT3310 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) | ritual (`ཆོ་ག`) |
| 148 | At_3CHc_ | root | root-text | context | yes | same-text | Tri7le69idh2SixvICLe6 | WA0RT1856 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 149 | At_3CHD | root | root-text | context | yes | same-text | lRFGF3w7QR5UKqwbAilvQ | WA0RT3314 |  |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) | ritual (`ཆོ་ག`) |
| 150 | At_3CHd_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 151 | At_3CHE | root | root-text | context | yes | same-text | 81Fe9l8YkLZL6l6RBvBrA | WA0RT3315 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) | ritual (`ཆོ་ག`) |
| 152 | At_3CHe_ | root | root-text | context | yes | same-text | zzvlrSCcYdQbEYyo7BobX | WA0RT1858 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 153 | At_3CHF | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Liturgy (reading) | ritual (`ཆོ་ག`) |
| 154 | At_3CHf_ | root | root-text | context | yes | same-text | FANIHNA9DPvT12KoJXk0Z | WA0RT1859 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 155 | At_3CHG | root | root-text | context | yes | same-text | zNb8Wyp76h2cSu9MWKnx7 | WA0RT3317 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 156 | At_3CHg_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 157 | At_3CHH | root | commentary | context | yes | same-text | OpgvprsftCoC5mSBAth9g | WA0RT3347 | Atiśa |  | reading says commentary, folder says root-text; root not in our corpus | Discourses / མདོ་སྡེ། | Discourses (openpecha) | ritual (`ཆོ་ག`) |
| 158 | At_3CHh_ | root | root-text | context | yes | same-text | gRcyr8121dmMBgGe5FIcq | WA0RT1862 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | offering (`མཆོད་པ`) |
| 159 | At_3CHI | root | root-text | context | yes | same-text | SntbI6bqHNX4LUipG3Zps | WA0RT3526 | Atiśa |  |  | Mind Trainings and Advices / བློ་སྦྱོང་དང་བསླབ་བྱ། | Mind Trainings and Advices (openpecha) |  |
| 160 | At_3CHi_ | root | root-text | context | yes | same-text | mAJt2TmQsd22Xqexyf3xo | WA0RT1863 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 161 | At_3CHJ | root | root-text | context | yes | same-text | CYZaE5Cek0fPN2mNit1U1 | WA0RT3723 | Atiśa |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | prayer (`སྨོན་ལམ`) |
| 162 | At_3CHj_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 163 | At_3CHK | root | root-text | context | yes | same-text | E3Dc9xwUCgirTtMqSW5qS | WA0RT3302 | Atiśa |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 164 | At_3CHk_ | root | root-text | context | yes | same-text | 5fE2utTL8fIJuhwmzdDZb | WA0RT1869 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 165 | At_3CHL | root | root-text | context | yes | same-text | TZzh01N9JsyQxqoDlXmww | WA0RT4022 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 166 | At_3CHl_ | root | root-text | context | yes | same-text | CU2l6nbtcvNesGUAt2ZG6 | WA0RT1870 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 167 | At_3CHM | root | root-text | context | yes | same-text | pg6PtDNqAPc63P9RGV6TW | WA0RT0790 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 168 | At_3CHm_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 169 | At_3CHN | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 170 | At_3CHn_ | root | root-text | context | yes | same-text | UuQob8etobiWmqMcZsLCc | WA0RT2508 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 171 | At_3CHO | root | root-text | context | yes | same-text | 8Inz2PixHLIlJEARfxswO | WA0RT1773 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 172 | At_3CHo_ | root | root-text | context | yes | same-text | cK5pyPFaMUviXLno9wO9F | WA0RT0800 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 173 | At_3CHP | root | root-text | context | yes | same-text | YTirp0BSY1EyabC1ErnZi | WA0RT1778 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 174 | At_3CHp_ | root | root-text | context | yes | same-text | rt3opplwSXAzK0N9Ri0MJ | WA0RT0801 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`མངོན་པར་རྟོགས་པ`) |
| 175 | At_3CHQ | root | root-text | context | yes | same-text | a8T3sAhqYzDpOuBJhMVbX | WA0RT1779 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 176 | At_3CHq_ | root | root-text | context | yes | same-text | mapnGNPmE6AKds894aDX5 | WA0RT0802 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 177 | At_3CHR | root | root-text | context | yes | same-text | 0BNlL3GmeJYq4cvRvbIoN | WA0RT1782 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 178 | At_3CHr_ | root | root-text | context | yes | same-text | gmzmoJ4aOaFN14nnGCeWk | WA0RT0803 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 179 | At_3CHS | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 180 | At_3CHs_ | root | root-text | context | yes | same-text | oRkHGUDB1sODlFHniAZe6 | WA0RT0804 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 181 | At_3CHT | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 182 | At_3CHt_ | root | root-text | context | yes | same-text | 4J0F3JxrwYldyhcybn2RG | WA0RT0805 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 183 | At_3CHU | root | root-text | context | yes | same-text | kNOKCwWkWkt6lQ8BUMEvr | WA0RT1795 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 184 | At_3CHu_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 185 | At_3CHV | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 186 | At_3CHv_ | root | root-text | context | yes | same-text | NhbJrikNtZn33aOYMasp9 | WA0RT0807 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 187 | At_3CHW | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 188 | At_3CHw_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 189 | At_3CHX | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | torma ritual (`གཏོར་མ`) |
| 190 | At_3CHY | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 191 | At_3CHy_ | root | root-text | context | yes | same-text | COHrdlkt08dSU9Vf3rg3g | WA0RT1478 | Atiśa |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 192 | At_3CHZ | root | root-text | context | yes | same-text | pUUFkUBtfaCkDjyVd6fkH | WA0RT1830 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 193 | At_3CHz_ | root | root-text | context | yes | same-text | 29zOcqdviTRnhHhoFTOi7 | WA0RT1769 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 194 | At_3CI0 | root | root-text | context | yes | same-text | rdMTttxEuKs8r7cPURKB2 | WA0RT1771 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 195 | At_3CI1 | root | root-text | context | yes | same-text | dMbPlv1a5PkLJo89tQvvV | WA0RT1772 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 196 | At_3CI2 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 197 | At_3CI3 | root | root-text | context | yes | same-text | kbnhcbyTSpgTRnMQNU47m | WA0RT1775 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 198 | At_3CI4 | root | root-text | context | yes | same-text | je0jius1ThhuAzyA9eCD7 | WA0RT1776 | Dīpaṅkarabhadra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 199 | At_3CI5 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 200 | At_3CI6 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 201 | At_3CI7 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 202 | At_3CI8 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 203 | At_3CI9 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 204 | At_3CIA | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 205 | Bh_3CCH | root | root-text | context | yes | same-text | yWV4pFVUivGaq2w6P4yvU | WA0RT3199 | Bhavyakīrti |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 206 | Bh_3CCI | root | root-text | context | yes | same-text | hHruFUB8ZeNGVXfpAqcqc | WA0RT3200 | Bhāviveka |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 207 | Bh_3CCJ | root | root-text | context | yes | same-text | ab6m4VNCwY1qz0ycMD9ZI | WA0RT3202 | Bhāviveka |  | same text as Bh_3CCO | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 208 | Bh_3CCK | root | root-text | context | yes | same-text | ZvKS1O2bndNI4DR2yrxXl | WA0RT3477 | Bhāviveka |  |  | Monastic Rules / འདུལ་བ། | Monastic Rules (openpecha) |  |
| 209 | Bh_3CCO | root | root-text | context | yes | same-text | ab6m4VNCwY1qz0ycMD9ZI | WA0RT3202 | Bhāviveka |  | same text as Bh_3CCJ | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 210 | Ch_3CCc_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 211 | Ch_3CCd_ | root | root-text | context | yes | same-text | GK2A903wttoFBI5pgeZV1 | WA0RT3206 |  |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 212 | Ch_3CCf_ | root | root-text | context | yes | same-text | pu6qfg6lfTYd3rWvTajo9 | WA0RT3208 | Candrakīrti III |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 213 | Ch_3CCP | root | root-text | context | yes | same-text | VP4qZKzHlbsmn7LYU0gwl | WA0RT0595 | Candrakīrti I |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 214 | Ch_3CCR | root | root-text | context | yes | same-text | 5cdzXYSwADuXWJxoMENgt | WA0RT0677 | Candrakīrti I |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 215 | Ch_3CCS | root | root-text | context | yes | same-text | 0l0sOGEXDxzLKALGHkQ8c | WA0RT0679 | Candrakīrti I |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 216 | Ch_3CCU | root | root-text | context | no | title matched, text check: fragment |  |  |  |  |  |  | Tantras (reading) |  |
| 217 | Ch_3CCV | root | root-text | context | yes | same-text | rT3KpwhJQX8AVUtj1jr35 | WA0RT1551 | Candrakīrti I |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 218 | Ch_3CCX | root | root-text | context | yes | same-text | y3OWTxHecw6qI92cafRoo | WA0RT3211 | Candrakīrti I |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 219 | Ch_3CCZ | root | root-text | context | yes | same-text | nbBp7zzmdD1hrHK1uoHA3 | WA0RT3312 | Candrakīrti I |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 220 | Dh_3CEy_ | root | root-text | context | yes | same-text | x6WuGXMGHTaiIf4iGD9Vw | WA0RT0047 | Dharmakīrti I |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 221 | Dh_3CF0 | root | root-text | context | yes | same-text | Vrdxbl7NtroBuchiPxLYY | WA0RT0159 | Dharmakīrti I |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 222 | Dh_3CF1 | root | root-text | context | yes | same-text | q6Pv3X1nyTOKYGIJlmMIj | WA0RT1330 | Dharmakīrti III |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 223 | Dh_3CF2 | root | root-text | context | yes | same-text | zq1bINZfVmGmOOCxlvcS2 | WA0RT1461 | Dharmakīrti III |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | fire offering (`སྦྱིན་སྲེག`) |
| 224 | Dh_3CF3 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 225 | Dh_3CF5 | root | root-text | context | yes | same-text | uN6DbrJPaApfPK3sH7Sat | WA1KG8893 | Dharmakīrti I |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 226 | Dh_3CF6 | root | root-text | context | yes | same-text | BNJCDccR0wcKTCYnGvNa1 | WA0RT3548 | Dharmakīrti I |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 227 | Dh_3CF7 | root | root-text | context | yes | same-text | ABbmpzyTWAQY8LNXzpxCZ | WA0RT3549 | Dharmakīrti I |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 228 | Dh_3CF8 | root | root-text | context | yes | same-text | F8JPrvApJgHARl5lX2GH4 | WA0RT3550 | Dharmakīrti I |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 229 | Dh_3CF9 | root | root-text | context | yes | same-text | QvYOcTm40LCsrLxssx6Jl | WA0RT3551 | Dharmakīrti I |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 230 | Dh_3CFC | root | root-text | context | yes | same-text | toCYDDOGWW2dIUyudYRJE | WA0RT3555 | Dharmakīrti I |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 231 | Dh_3CFD | root | root-text | context | yes | same-text | k1JHxHaX9S8WXEOE49Zec | WA0RT3556 | Dharmakīrti I |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 232 | Di_3CEe_ | root | root-text | context | yes | same-text | tenb88YYccIpgcIvf0uGP | WA0RT0041 | maticitra; Dignāga |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 233 | Di_3CEi_ | root | root-text | context | no | title matched, text check: fragment |  |  |  |  |  |  | Tantras (reading) |  |
| 234 | Di_3CEj_ | root | root-text | context | no | title matched, text check: fragment |  |  |  |  |  |  | Tantras (reading) |  |
| 235 | Di_3CEk_ | root | root-text | context | yes | same-text | 5ZzdMPqpulraE8pWOMxQj | WA0RT1535 | Dignāga |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 236 | Di_3CEl_ | root | commentary | context | yes | same-text | rZPeLU1FuMdeKDxa79jnV | WA0RT3154 | Dignāga |  | reading says commentary, folder says root-text; root not in our corpus | Perfection of Wisdom / ཤེར་ཕྱིན། | Prajñāpāramitā (openpecha) |  |
| 237 | Di_3CEn_ | root | root-text | context | yes | same-text | X40QOqH14JmqHqzZQSunu | WA0RT3412 | Dignāga |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 238 | Di_3CEp_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Logic (reading) |  |
| 239 | Di_3CEq_ | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Logic (reading) |  |
| 240 | Di_3CEs_ | root | root-text | context | yes | same-text | cascasXOWd1vNmHxIfVml | WA0RT3542 | Dignāga |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 241 | Di_3CEu_ | root | root-text | context | yes | same-text | bKrpBDpoaydvgeFgoZpxE | WA0RT3544 | Dignāga |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 242 | Di_3CEv_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Logic (reading) |  |
| 243 | Di_3CEw_ | root | root-text | context | yes | same-text | aItTdzPEPszxDkieKP520 | WA0RT3545 | Dignāga |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 244 | Di_3CEx_ | root | root-text | context | yes | same-text | YlCMmu1JLSVa3o4yFOx3K | WA0RT3546 | Dignāga |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 245 | Gu_3CFS | root | root-text | context | yes | same-text | vPmTubUjrqvnHBtB6q3Nv | WA0RT3455 | Guṇaprabha |  |  | Monastic Rules / འདུལ་བ། | Monastic Rules (openpecha) |  |
| 246 | Gu_3CFT | root | root-text | context | yes | same-text | vyi9wS8ZMCVOLRS7gxOzn | WA0RT3456 | Guṇaprabha |  |  | Monastic Rules / འདུལ་བ། | Monastic Rules (openpecha) |  |
| 247 | Ha_3CFF | root | commentary | context | no | no OpenPecha record has this title |  |  |  |  | reading says commentary, folder says root-text; root not in our corpus |  | Prajñāpāramitā (reading) |  |
| 248 | Ha_3CFG | root | commentary | context | no | no OpenPecha record has this title |  |  |  |  | reading says commentary, folder says root-text; root not in our corpus |  | Prajñāpāramitā (reading) |  |
| 249 | Ha_3CFH | root | commentary | context | no | no OpenPecha record has this title |  |  |  |  | reading says commentary, folder says root-text; root not in our corpus |  | Prajñāpāramitā (reading) |  |
| 250 | Ha_3CFI | root | commentary | context | no | no OpenPecha record has this title |  |  |  |  | reading says commentary, folder says root-text; root not in our corpus |  | Prajñāpāramitā (reading) |  |
| 251 | Ha_3CFJ | root | commentary | context | no | no OpenPecha record has this title |  |  |  |  | reading says commentary, folder says root-text; root not in our corpus |  | Prajñāpāramitā (reading) |  |
| 252 | Ha_3CFO | root | root-text | context | yes | same-text | WIoz1doE1DXt8jtmwaTfM | WA0RT3609 | Mahīndrabhadra |  |  | Linguistics Treatises / རིག་གནས། | Linguistics Treatises (openpecha) |  |
| 253 | Ka_3CDK | root | root-text | context | yes | same-text | 6bQE06u6AEcl9ByI6Vsi8 | WA0RT3232 | kamalashila |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 254 | Ka_3CDL | root | root-text | context | yes | same-text | GydntTc4QtxjMuNNFwlz8 | WA0RT3233 | kamalashila |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 255 | Ka_3CDM | root | root-text | context | yes | same-text | XsynmXGwODDjmIkqiY9Px | WA0RT3234 | kamalashila |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 256 | Ka_3CDN | root | root-text | context | yes | same-text | gRF40RUwYAyfnDMbFkltn | WA0RT1417 | *Mañjuśrīmitra |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 257 | Ka_3CDO | root | root-text | context | yes | same-text | 1VsSo6lC6R5EK19rIyKxo | WA0RT4228 | kamalashila |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 258 | Ka_3CDP | root | root-text | context | yes | same-text | sBQ0KntTmGfd2Q4Ip8aRC | WA0RT4229 | kamalashila |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 259 | Ka_3CDQ | root | root-text | context | yes | same-text | U6y370Yv98qiMNb7vbaMY | WA0RT4230 | kamalashila |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 260 | Ka_3CDR | root | root-text | context | yes | same-text | 2xcOpsg1DlgJBbyj55ozA | WA0RT3260 | kamalashila |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 261 | Ka_3CDV | root | root-text | context | yes | same-text | TfbuRXaqA3o7nB7XisbkH | WA0RT3531 | kamalashila |  |  | Mind Trainings and Advices / བློ་སྦྱོང་དང་བསླབ་བྱ། | Mind Trainings and Advices (openpecha) |  |
| 262 | Ka_3CDW | root | root-text | context | yes | same-text | cGBN1UauBpEBLLSYgVLPj | WA0RT3533 | kamalashila |  |  | Mind Trainings and Advices / བློ་སྦྱོང་དང་བསླབ་བྱ། | Mind Trainings and Advices (openpecha) |  |
| 263 | Ka_3CDY | root | root-text | context | yes | same-text | kXw5ncwU0390dkRN0yqjf | WA0RT3727 | kamalashila |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | prayer (`སྨོན་ལམ`) |
| 264 | Na_3C92 | root | root-text | context | yes | same-text | 24KXRARBpSGgn4cr3fGga | WA0RT0010 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 265 | Na_3C93 | root | root-text | context | yes | same-text | 2BGRMgRuukPYoY7wsmxt8 | WA0RT0011 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 266 | Na_3C94 | root | root-text | context | yes | same-text | xJPwo6gZr125ooai8yfVA | WA0RT0012 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 267 | Na_3C95 | root | root-text | context | yes | same-text | uyZY3P6LnjLiv9kh6Aduy | WA0RT0013 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 268 | Na_3C96 | root | root-text | context | yes | same-text | UL4YHUoTk7zJP1RhZ0Z8v | WA0RT0014 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 269 | Na_3C97 | root | root-text | context | yes | same-text | 3vTc43xGGK8JysYot16OZ | WA0RT0015 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 270 | Na_3C99 | root | root-text | context | yes | same-text | fsSCTz2Vx7KP3ZXtOsZcB | WA0RT0017 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 271 | Na_3C9A | root | root-text | context | yes | same-text | 90xBMm4klw23AE5Qm185Y | WA0RT0018 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 272 | Na_3C9a_ | root | root-text | context | yes | same-text | hZtACPdZAVyTF97RVakl4 | WA0RT0660 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 273 | Na_3C9B | root | root-text | context | yes | same-text | qlwcW6qnNEoJAIhYSbGVS | WA0RT0019 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 274 | Na_3C9b_ | root | root-text | context | yes | same-text | N3Kcm9X6nLazO7tLPjbcR | WA0RT0661 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 275 | Na_3C9C | root | root-text | context | yes | same-text | 9ykJNsrDXUBFdENQgI78I | WA0RT0020 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 276 | Na_3C9c_ | root | root-text | context | yes | same-text | BlYt1pV5M88A7dZ3pcNOe | WA0RT0662 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 277 | Na_3C9D | root | root-text | context | yes | same-text | CFpNBQa0jdiMvsjZfNcPF | WA0RT0021 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 278 | Na_3C9d_ | root | root-text | context | yes | same-text | qPOC6e91k9t29DGU4oSuk | WA0RT0663 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | empowerment (`དབང`) |
| 279 | Na_3C9E | root | root-text | context | yes | same-text | AEOK5HF2A9A5wVVpbuxIV | WA0RT0022 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 280 | Na_3C9e_ | root | root-text | context | yes | same-text | YMwWqH4AlPOW2fb4e5e87 | WA0RT0664 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 281 | Na_3C9F | root | root-text | context | yes | same-text | gzD2ju2HXVHxuN4yixaTF | WA0RT0023 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 282 | Na_3C9G | root | root-text | context | yes | same-text | 5dYbgFab0LDq0mwb8hXAi | WA0RT0024 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 283 | Na_3C9H | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Miscellaneous (reading) | praise (`བསྟོད`) |
| 284 | Na_3C9h_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 285 | Na_3C9I | root | root-text | context | yes | same-text | 6lpwtoBMEDtzjtinkxi4u | WA0RT0026 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 286 | Na_3C9i_ | root | root-text | context | yes | same-text | g9cM2wpbTjcLKG1kjrYZy | WA0RT1032 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 287 | Na_3C9J | root | root-text | context | yes | same-text | NE0QcmVqnWzzspbJFRC0v | WA0RT0027 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 288 | Na_3C9j_ | root | root-text | context | yes | same-text | CKRE4xZA0luR0xNkQtGob | WA0RT1033 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 289 | Na_3C9K | root | root-text | context | yes | same-text | FOGIHaDpbO4uxQdvBgDUG | WA0RT0028 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) |  |
| 290 | Na_3C9k_ | root | root-text | context | yes | same-text | xCy9XnwIvL2NTg70ik4oL | WA0RT1047 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 291 | Na_3C9M | root | root-text | context | yes | same-text | kR7i0u4UHE9QWm3nPLLxL | WA0RT0480 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 292 | Na_3C9N | root | root-text | context | yes | same-text | n14IHXArioYtFRhp4mpp1 | WA0RT0555 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 293 | Na_3C9n_ | root | root-text | context | yes | same-text | J8HGY7cDgtAOWD4Tmjew9 | WA0RT1048 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 294 | Na_3C9O | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 295 | Na_3C9o_ | root | root-text | context | yes | same-text | KIdfPK6bcWD2dxUB2dgiQ | WA0RT1049 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 296 | Na_3C9P | root | root-text | context | yes | same-text | 86kl8TtjSRKoEj5RXrA0G | WA0RT2897 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 297 | Na_3C9p_ | root | root-text | context | yes | same-text | HUHXTE7dCrfzw2TbHgcLt | WA0RT1050 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 298 | Na_3C9Q | root | root-text | context | yes | same-text | Lw3u6vYKeY400fxSVuSVi | WA0RT0627 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 299 | Na_3C9R | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 300 | Na_3C9r_ | root | root-text | context | yes | same-text | lVGDQtgDVSQ1RqafdeR9H | WA0RT1068 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 301 | Na_3C9S | root | root-text | context | yes | same-text | RfiSq2NSQebaytc7bobIU | WA0RT0629 |  |  | same text as Ar_3CBf_ | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 302 | Na_3C9s_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 303 | Na_3C9T | root | root-text | context | yes | same-text | 56EaKecucFVdxZPI6bkaG | WA0RT0637 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 304 | Na_3C9t_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 305 | Na_3C9U | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 306 | Na_3C9u_ | root | root-text | context | yes | same-text | x0GahkJk9DN0kA0te5ko3 | WA0RT1124 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 307 | Na_3C9V | root | root-text | context | yes | same-text | KPuwarNFS3PjMYUXpCl4Z | WA0RT0639 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 308 | Na_3C9v_ | root | root-text | context | yes | same-text | 3RHQodoHklC4L1C1mgfhb | WA0RT1200 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 309 | Na_3C9W | root | root-text | context | yes | same-text | XzgjjW9G1MCrTd9rzhT8v | WA0RT0644 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 310 | Na_3C9w_ | root | root-text | context | yes | same-text | mR7YEwYH9580efjQ8RIVO | WA0RT1223 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 311 | Na_3C9X | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | praise (`བསྟོད`) |
| 312 | Na_3C9x_ | root | root-text | context | no | title matched, text check: fragment |  |  |  |  |  |  | Tantras (reading) |  |
| 313 | Na_3C9Y | root | root-text | context | yes | same-text | Ydu5w2NUDXyLiAH6Nc21V | WA0RT0646 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | praise (`བསྟོད`) |
| 314 | Na_3C9y_ | root | root-text | context | no | title matched, text check: fragment |  |  |  |  |  |  | Tantras (reading) |  |
| 315 | Na_3C9z_ | root | root-text | context | yes | same-text | kUfeDc9bjwaUBteF4yrPS | WA0RT3103 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | empowerment (`དབང`) |
| 316 | Na_3CA0 | root | root-text | context | yes | same-text | c7qoCxdsZXLe6eqd8ITNI | WA0RT1304 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 317 | Na_3CA1 | root | root-text | context | yes | same-text | oAZh09jqr7qhNprRxoDTX | WA0RT1305 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 318 | Na_3CA2 | root | root-text | context | yes | same-text | E4BzefdMojcaFJTOFzLyU | WA0RT1306 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 319 | Na_3CA3 | root | root-text | context | yes | same-text | vhteBtjBA1EjrIhJmyZPs | WA0RT1463 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 320 | Na_3CA5 | root | root-text | context | yes | same-text | wKxoTEf94BnKPz2PDQhxj | WA0RT1524 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 321 | Na_3CA6 | root | root-text | context | yes | same-text | LdR1LSQlH5iqArqwNsnUX | WA0RT1554 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 322 | Na_3CA7 | root | root-text | context | yes | same-text | C8fSos7VvrpYjus0MDqNK | WA0RT1555 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 323 | Na_3CA8 | root | root-text | context | yes | same-text | aPvlMsOX97Lk4rPMOq1Ew | WA0RT3948 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 324 | Na_3CA9 | root | root-text | context | yes | same-text | FHx2c7WoQRqb6VcUZ3Isf | WA0RT1687 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 325 | Na_3CAA | root | root-text | context | yes | same-text | ghsgH2SI3dy2wrfFKJVEf | WA0RT1688 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 326 | Na_3CAB | root | root-text | context | yes | same-text | z76a966CUtceC4zUf14sV | WA0RT1689 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 327 | Na_3CAb_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 328 | Na_3CAC | root | root-text | context | yes | same-text | 7zvlcOpd8s4qgGijKvolW | WA0RT1690 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 329 | Na_3CAc_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Liturgy (reading) | praise (`བསྟོད`) |
| 330 | Na_3CAD | root | root-text | context | yes | same-text | c9bvUTWPbZrfr0L46hot2 | WA0RT1711 | Nāgārjuna; སློབ་དཔོན་འགྲོ་བཟང་སྙིང་པོ། |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | maṇḍala ritual (`དཀྱིལ་འཁོར`) |
| 331 | Na_3CAd_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Liturgy (reading) | praise (`བསྟོད`) |
| 332 | Na_3CAE | root | root-text | context | yes | same-text | IJrODW0eXdqDi2hyKyGDc | WA0RT4299 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 333 | Na_3CAe_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 334 | Na_3CAF | root | commentary | context | yes | same-text | ZDJO2kHEvOsvmcbQjeAcu | WA0RT1890 | Nāgārjuna |  | reading says commentary, folder says root-text; root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 335 | Na_3CAf_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 336 | Na_3CAG | root | root-text | context | yes | same-text | 1PQIQSYdYz4d0eFlKNp3s | WA0RT1937 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 337 | Na_3CAg_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | torma ritual (`གཏོར་མ`) |
| 338 | Na_3CAH | root | root-text | context | yes | same-text | 1xdvkvyHnPsNZk1p7Bwxl | WA0RT2183 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 339 | Na_3CAh_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 340 | Na_3CAI | root | root-text | context | yes | same-text | FFwODm4ImY1c7whaA4Fqr | WA0RT2184 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 341 | Na_3CAi_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 342 | Na_3CAJ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 343 | Na_3CAK | root | root-text | context | yes | same-text | j2RFJwnQSlN10oINycUXd | WA0RT2186 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | dhāraṇī (`གཟུངས`) |
| 344 | Na_3CAk_ | root | root-text | context | yes | same-text | PWlDJMBgQKcTtAXnneAMO | WA0RT3169 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 345 | Na_3CAL | root | root-text | context | yes | same-text | MwOFypwDcx42klY963J1Q | WA0RT2187 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 346 | Na_3CAl_ | root | root-text | context | yes | same-text | h7EV64IBvw4ULkt8HEzWp | WA0RT3170 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 347 | Na_3CAM | root | root-text | context | yes | same-text | VmcXSrGHlcgzNt4FCuiqr | WA0RT2188 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 348 | Na_3CAm_ | root | root-text | context | yes | same-text | dsjfWmqjrOiwS2QjOq7nX | WA0RT3171 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 349 | Na_3CAN | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 350 | Na_3CAn_ | root | root-text | context | yes | same-text | em8Fu5y0Lfu4WA99ng6vd | WA0RT3172 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 351 | Na_3CAO | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 352 | Na_3CAo_ | root | root-text | context | yes | same-text | Zs3hcbFdiO2hkygZXQ0Zt | WA0RT3173 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 353 | Na_3CAP | root | root-text | context | yes | same-text | xRcEoxxp2Yu46bo76j1Km | WA0RT4261 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 354 | Na_3CAQ | root | root-text | context | yes | same-text | 0D87fWjh79PzUcxkMNjKh | WA0RT2383 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 355 | Na_3CAR | root | root-text | context | yes | same-text | QJSRtJqmjutLgjWe5Z9UZ | WA0RT2466 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 356 | Na_3CAS | root | root-text | context | yes | same-text | nSkW4yMy2jhsEsR7RwtXk | WA0RT2486 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 357 | Na_3CAT | root | root-text | context | yes | same-text | tX0fI4wLaQOmC9Zgla73w | WA0RT2550 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 358 | Na_3CAU | root | root-text | context | yes | same-text | JXWfEz5urP9y3PQbyRmK8 | WA0RT4281 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`སྒྲུབ་ཐབས`) |
| 359 | Na_3CAu_ | root | root-text | context | yes | same-text | lnXt37BWU7jE2dymjyBCv | WA0RT4305 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 360 | Na_3CAV | root | root-text | context | yes | same-text | yi3ug2dBe1KhGdKHtfk5p | WA0RT2587 | Nāgārjuna |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | torma ritual (`གཏོར་མ`) |
| 361 | Na_3CAv_ | root | root-text | context | yes | same-text | yhneFpHwafPyE0WVmmohx | WA0RT3179 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 362 | Na_3CAW | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 363 | Na_3CAX | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 364 | Na_3CAx_ | root | root-text | context | yes | same-text | kVYtjG3jPQk0vcHmlUYxs | WA0RT3181 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 365 | Na_3CAY | root | commentary | context | no | no OpenPecha record has this title |  |  |  |  | reading says commentary, folder says root-text; root not in our corpus |  | Tantras (reading) |  |
| 366 | Na_3CAZ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 367 | Na_3CAz_ | root | root-text | context | yes | same-text | Rlit7LejXaO8eqIQxRslv | WA0RT3183 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 368 | Na_3CB0 | root | root-text | context | yes | same-text | bDjeT1Kq1pXUA4e2j4egd | WA0RT3184 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 369 | Na_3CB1 | root | root-text | context | yes | same-text | yR0nq0Vkt0cFqGMhrS6U2 | WA0RT3185 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 370 | Na_3CB2 | root | root-text | context | yes | same-text | SuNBzLoiDLCR7OEKaBItQ | WA0RT3188 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 371 | Na_3CB3 | root | root-text | context | yes | same-text | Iio2R9T2SgwddN4PbDzON | WA0RT3253 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 372 | Na_3CB4 | root | root-text | context | yes | same-text | Dn0kS7whf6jE5w72XjATM | WA0RT3275 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 373 | Na_3CB5 | root | root-text | context | yes | same-text | Sk3FSL64lsKJmXYlcHydR | WA0RT3307 | Nāgārjuna |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) | ritual (`ཆོ་ག`) |
| 374 | Na_3CB6 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Discourses (reading) |  |
| 375 | Na_3CBB | root | root-text | context | yes | same-text | twcRBAHQ5xDgallelTNsI | WA0RT3462 | Śākyaprabha |  | same text as Sh_3CFZ | Monastic Rules / འདུལ་བ། | Monastic Rules (openpecha) |  |
| 376 | Na_3CBC | root | root-text | context | yes | same-text | 5VknhFEePdazJv7LSiklS | WA0RT3486 | Nāgārjuna |  |  | Monastic Rules / འདུལ་བ། | Monastic Rules (openpecha) | ritual (`ཆོ་ག`) |
| 377 | Na_3CBD | root | root-text | context | yes | same-text | 4Sb9nmMh6oDMSAHyK4b4w | WA0RT3496 | Nāgārjuna |  |  | Mind Trainings and Advices / བློ་སྦྱོང་དང་བསླབ་བྱ། | Mind Trainings and Advices (openpecha) |  |
| 378 | Na_3CBE | root | root-text | context | yes | same-text | bcsksBXFZFfTIxYBOarmn | WA0RT3498 | Nāgārjuna |  |  | Mind Trainings and Advices / བློ་སྦྱོང་དང་བསླབ་བྱ། | Mind Trainings and Advices (openpecha) |  |
| 379 | Na_3CBF | root | root-text | context | yes | same-text | 0fbVxwgYH4Ag5Hx4Vilh8 | WA0RT3499 | Nāgārjuna |  |  | Mind Trainings and Advices / བློ་སྦྱོང་དང་བསླབ་བྱ། | Mind Trainings and Advices (openpecha) |  |
| 380 | Na_3CBG | root | root-text | context | yes | same-text | ynM1FQb1hvwnHtbeOwvfV | WA0RT3500 | Nāgārjuna |  |  | Mind Trainings and Advices / བློ་སྦྱོང་དང་བསླབ་བྱ། | Mind Trainings and Advices (openpecha) |  |
| 381 | Na_3CBH | root | root-text | context | yes | same-text | dRDR9Lg1bgJftmsA24UJs | WA0RT3520 | Nāgārjuna |  |  | Mind Trainings and Advices / བློ་སྦྱོང་དང་བསླབ་བྱ། | Mind Trainings and Advices (openpecha) |  |
| 382 | Na_3CBI | root | root-text | context | yes | same-text | FG8cdcQETEfg1t4XjRuFd | WA0RT3640 | Nāgārjuna |  |  | Linguistics Treatises / རིག་གནས། | Linguistics Treatises (openpecha) |  |
| 383 | Na_3CBJ | root | root-text | context | yes | same-text | ZQIpLtqk1A92F5MC5PD6Q | WA0RT3641 | Nāgārjuna |  |  | Linguistics Treatises / རིག་གནས། | Linguistics Treatises (openpecha) |  |
| 384 | Na_3CBK | root | root-text | context | yes | same-text | WIy9aX4wi5y95zojpTvz5 | WA0RT3642 | Nāgārjuna |  |  | Linguistics Treatises / རིག་གནས། | Linguistics Treatises (openpecha) | ritual (`ཆོ་ག`) |
| 385 | Na_3CBL | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Linguistics Treatises (reading) |  |
| 386 | Na_3CBM | root | root-text | context | yes | same-text | Fe5gf3IhJo7ij4g5BI1dT | WA0RT3653 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) |  |
| 387 | Na_3CBN | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Linguistics Treatises (reading) |  |
| 388 | Na_3CBO | root | root-text | context | yes | same-text | 0HVuXEeB3PNoixxxfr4yc | WA0RT3662 | Nāgārjuna |  |  | Mind Trainings and Advices / བློ་སྦྱོང་དང་བསླབ་བྱ། | Mind Trainings and Advices (openpecha) |  |
| 389 | Na_3CBP | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind Trainings and Advices (reading) |  |
| 390 | Na_3CBQ | root | root-text | context | yes | same-text | nfBE0lINUQeEUbthclOyb | WA0RT3664 | Nāgārjuna |  |  | Mind Trainings and Advices / བློ་སྦྱོང་དང་བསླབ་བྱ། | Mind Trainings and Advices (openpecha) |  |
| 391 | Na_3CBR | root | root-text | context | yes | same-text | yciVgwMgz89jEMBtKeJ9B | WA0RT3718 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | prayer (`སྨོན་ལམ`) |
| 392 | Na_3CBS | root | root-text | context | yes | same-text | pWoa9yTj24IB8JKbzNCcB | WA0RT3719 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | prayer (`སྨོན་ལམ`) |
| 393 | Na_3CBT | root | root-text | context | yes | same-text | ve1Dz3tDHRU8F4Z1WXHEH | WA0RT3721 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | prayer (`སྨོན་ལམ`) |
| 394 | Na_3CBU | root | root-text | context | yes | same-text | cWtUjH8TyOEv1qxnVtg0i | WA0RT3722 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | prayer (`སྨོན་ལམ`) |
| 395 | Na_3CBV | root | root-text | context | yes | same-text | lcLwc8oOHrUsAzRbVa3Qt | WA0RT3729 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | prayer (`སྨོན་ལམ`) |
| 396 | Na_3CBW | root | root-text | context | yes | same-text | zOGfHME0WYcHtiL8shwYN | WA0RT4223 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) |  |
| 397 | Na_3CBX | root | root-text | context | yes | same-text | ZGJE7zkXje7lmoH7A7WSA | WA0RT4224 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) |  |
| 398 | Na_3CBY | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Linguistics Treatises (reading) |  |
| 399 | Na_3CBZ | root | root-text | context | yes | same-text | mfhg6cvluCjTm2OVQOucN | WA0RT3786 | Nāgārjuna |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | empowerment (`དབང`) |
| 400 | Sh_3CCh_ | root | root-text | context | no | title matched, text check: fragment |  |  |  |  |  |  | Tantras (reading) |  |
| 401 | Sh_3CCi_ | root | root-text | context | no | title matched, text check: fragment |  |  |  |  |  |  | Tantras (reading) |  |
| 402 | Sh_3CCj_ | root | root-text | context | yes | same-text | AZo2M7i7VqJkN9wvblwJN | WA0RT1168 | Śāntideva |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 403 | Sh_3CCl_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 404 | Sh_3CCm_ | root | root-text | context | yes | same-text | PqT7jXsnVDBWUJIUtPXw9 | WA0RT3216 | Śāntideva |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 405 | Sh_3CCn_ | root | root-text | context | yes | same-text | Re3ja5iKsqgx9utDs0gNc | WA0RT3282 | Śāntideva |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) | ritual (`ཆོ་ག`) |
| 406 | Sh_3CCp_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Linguistics Treatises (reading) |  |
| 407 | Sh_3CCq_ | root | root-text | context | yes | same-text | lNKVYkKFJsPFbvtRrLigu | WA0RT3717 | Śāntideva |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | prayer (`སྨོན་ལམ`) |
| 408 | Sh_3CCr_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 409 | Sh_3CCs_ | root | root-text | context | yes | part | BxD11EMUttisysWt8JUyi | WA0RT3281 | Śāntideva |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 410 | Sh_3CCt_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Middle Way (reading) |  |
| 411 | Sh_3CCu_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Linguistics Treatises (reading) |  |
| 412 | Sh_3CCv_ | root | root-text | context | yes | same-text | mCUJrwGC3LQJEnwOx2hzw | WA0RT0051 |  |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 413 | Sh_3CCx_ | root | root-text | context | yes | same-text | Xin9dsNQ4n3aMbHPX1T9x | WA0RT0055 | Śāntirakṣita |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 414 | Sh_3CCy_ | root | root-text | context | yes | same-text | UcsuenMGXroHmJJtK0Jey | WA0RT0447 | Śāntirakṣita |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 415 | Sh_3CCz_ | root | root-text | context | yes | same-text | GXm39KB4t0L0vleuEPTof | WA0RT0687 | Śāntadeva |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | torma ritual (`གཏོར་མ`) |
| 416 | Sh_3CD1 | root | root-text | context | no | title matched, text check: different |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 417 | Sh_3CD2 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 418 | Sh_3CD3 | root | root-text | context | yes | same-text | C0MPWS7854k4OljaFxlHR | WA0RT1952 | Bodhisattva |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | prayer (`སྨོན་ལམ`) |
| 419 | Sh_3CD4 | root | root-text | context | yes | same-text | xbDDEXXjWISDhPHtMGq2b | WA0RT1953 |  |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 420 | Sh_3CD5 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | prayer (`སྨོན་ལམ`) |
| 421 | Sh_3CD6 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 422 | Sh_3CD7 | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) | ritual (`ཆོ་ག`) |
| 423 | Sh_3CD8 | root | root-text | context | yes | same-text | SRbIzMA7iNkDx9WByWDuv | WA0RT2530 | Śāntirakṣita |  |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 424 | Sh_3CDA | root | root-text | context | yes | same-text | Tlupwd2KkkaiRIhlQRlUW | WA0RT3229 | Śāntirakṣita |  |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 425 | Sh_3CDE | root | root-text | context | yes | same-text | HwufutQgHWKfxUL6RO9eY | WA0RT3601 | Śāntirakṣita |  |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 426 | Sh_3CDF | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Tantras (reading) |  |
| 427 | Sh_3CFZ | root | root-text | context | yes | same-text | twcRBAHQ5xDgallelTNsI | WA0RT3462 | Śākyaprabha |  | same text as Na_3CBB | Monastic Rules / འདུལ་བ། | Monastic Rules (openpecha) |  |
| 428 | Va_3CE0 | root | root-text | context | yes | same-text | rh48q6V0VIfwvJNemxE3R | WA0RT0037 | Vasubandhu |  |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | ritual (`ཆོག`) |
| 429 | Va_3CEa_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind Trainings and Advices (reading) |  |
| 430 | Va_3CEb_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind Trainings and Advices (reading) |  |
| 431 | Va_3CEc_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind Trainings and Advices (reading) |  |
| 432 | Va_3CEd_ | root | root-text | context | no | no OpenPecha record has this title |  |  |  |  |  |  | Mind Trainings and Advices (reading) |  |
| 433 | Va_3CEL | root | root-text | context | yes | same-text | 4y0MSVJO2snT3ClMluqDw | WA0RT3394 | Vasubandhu |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 434 | Va_3CEM | root | root-text | context | yes | same-text | Km5PN6Sx9ue5F7qAwtaRm | WA0RT3395 | Vasubandhu |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 435 | Va_3CEO | root | root-text | context | yes | same-text | 4ZBC4NAWQgtCgxy1USAha | WA0RT3397 | Vasubandhu |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 436 | Va_3CEP | root | root-text | context | yes | same-text | ikKrp5SmvZkq2LuMAiLda | WA0RT4227 | Vasubandhu |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 437 | Va_3CEQ | root | root-text | context | yes | same-text | VxN9JZt06X3pWvy4clZDV | WA0RT3398 | Vasubandhu |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 438 | Va_3CER | root | root-text | context | yes | same-text | 1bqS65dvtI5eVyjLLViw3 | WA0RT3399 | Vasubandhu |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 439 | Va_3CES | root | root-text | context | yes | same-text | C8U4AxkIskgv8NuGkit6t | WA0RT3400 | Vasubandhu |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 440 | Va_3CET | root | root-text | context | yes | same-text | 5iuVGHNVLXLSbP3NQXQST | WA0RT3401 | Vasubandhu; Śrīdharmapāla |  |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 441 | Va_3CEX | root | root-text | context | yes | same-text | SuEjB3HRx4X1FM5fgBOsQ | WA0RT3427 | Vasubandhu |  |  | Systematic Treatises / མངོན་པ། | Systematic Treatises (openpecha) |  |
| 442 | Va_3CEY | root | root-text | context | yes | same-text | fmdStOnhC6BhXun5fHtEs | WA0RT3440 | Vasubandhu |  |  | Systematic Treatises / མངོན་པ། | Systematic Treatises (openpecha) |  |
| 443 | Ar_3CBb_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Ch_3CCa_ |  |  | Tantras (reading) |  |
| 444 | Ar_3CBd_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Tantras (reading) |  |
| 445 | Ar_3CC0 | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Ar_3CBz_ |  |  | Middle Way (reading) |  |
| 446 | Ar_3CC4 | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Ar_3CC3 |  |  | Middle Way (reading) |  |
| 447 | Ar_3CFE | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Prajñāpāramitā (reading) | sādhana (`མངོན་པར་རྟོགས་པ`) |
| 448 | As_3CDf_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) |  |
| 449 | As_3CDg_ | commentary | commentary | context | yes | same-text | ibqxNTvaaD6yu71O9Io0x | WA0RT3322 | asanga |  | root not in our corpus | Discourses / མདོ་སྡེ། | Discourses (openpecha) |  |
| 450 | As_3CDh_ | commentary | commentary | context | yes | same-text | ZjEsfBnn9fdyPWqiV4bpt | WA0RT3323 | asanga |  | root not in our corpus | Discourses / མདོ་སྡེ། | Discourses (openpecha) |  |
| 451 | As_3CDi_ | commentary | commentary | context | yes | same-text | opfi4wdNkrlGu7vg0s31t | WA0RT3324 | asanga |  | root not in our corpus | Discourses / མདོ་སྡེ། | Discourses (openpecha) |  |
| 452 | As_3CDj_ | commentary | commentary | context | yes | same-text | A9C7VqTRslvAmtUApV7hl | WA0RT3364 | asanga |  | root not in our corpus | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 453 | As_3CDx_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) |  |
| 454 | As_3CDy_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  |  |  |
| 455 | As_3CDz_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  |  |  |
| 456 | At_3CFi_ | commentary | commentary | context | yes | same-text | 3bRFy5pjoPBV1lf08tmb3 | WA0RT0210 | Atiśa | At_3CFh_ |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 457 | At_3CFk_ | commentary | commentary | context | yes | same-text | lvSpX0IeTcQRP4ZZH4R7t | WA0RT0212 | Atiśa | At_3CFj_ |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 458 | At_3CGr_ | commentary | commentary | context | yes | same-text | zlm8VM6YLBDMu4sG4nrGe | WA0RT3168 | Atiśa |  | root not in our corpus | Perfection of Wisdom / ཤེར་ཕྱིན། | Prajñāpāramitā (openpecha) |  |
| 459 | At_3CGw_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Na_3CB4 |  |  | Middle Way (reading) |  |
| 460 | At_3CGz_ | commentary | commentary | context | yes | same-text | Bk9wLEIqZNPiJOBUflCYw | WA0RT3289 | Atiśa | At_3CGy_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 461 | At_3CHx_ | commentary | commentary | context | yes | same-text | qDlqVTE6Vwq0nbZWYNPK3 | WA0RT1312 | Atiśa |  | root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 462 | Bh_3CCD | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Ch_3CCa_ |  |  | Tantras (reading) |  |
| 463 | Bh_3CCE | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Ch_3CCa_ |  |  | Tantras (reading) |  |
| 464 | Bh_3CCF | commentary | commentary | context | yes | same-text | cvU9z7rKAO2EYejLkkYe2 | WA0RT0657 | Bhāviveka | Ch_3CCa_ |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 465 | Bh_3CCG | commentary | commentary | context | yes | same-text | UGNyBiEXBGMQFGYMllqGy | WA0RT0695 | Bhavyakīrti | Na_3C9h_ |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 466 | Bh_3CCL | commentary | commentary | context | yes | same-text | KdAH4X4NeHYOvtcLKD6mf | WA0RT3198 | Bhāviveka | Na_3CAk_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 467 | Bh_3CCM | commentary | commentary | context | yes | part | JIWy0RrzXBStUOgDb4dSJ | WA0RT3201 | Bhāviveka | Bh_3CCI |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 468 | Bh_3CCN | commentary | commentary | context | yes | part | JIWy0RrzXBStUOgDb4dSJ | WA0RT3201 | Bhāviveka | Bh_3CCI |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 469 | Bu_3CCC | commentary | commentary | context | yes | same-text | T6NE3lxmesbzk0Y1u5Sfj | WA0RT3187 | Buddhapālita | Na_3CAk_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 470 | Ch_3CCa_ | commentary | commentary | context | yes | same-text | 6qEigdbAQFPIHhZOK6cBV | WA0RT0650 | Candrakīrti II |  | root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 471 | Ch_3CCb_ | commentary | commentary | context | yes | same-text | iOfLQv1BRaBzRfrS8tUga | WA0RT3205 | Candrakīrti I | Na_3CAk_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 472 | Ch_3CCe_ | commentary | commentary | context | yes | same-text | qlqFtMgkItJUf2XSFoYcI | WA0RT3207 | Candrakīrti I | Ch_3CCd_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 473 | Ch_3CCg_ | commentary | commentary | context | yes | same-text | iLAH58FozyywyGefxRDSp | WA0RT3210 | Candrakīrti I | Ar_3CC1 |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 474 | Ch_3CCQ | commentary | commentary | context | yes | same-text | ZLgteK5wzrsCIFYA7Fr8h | WA0RT0651 | Candrakīrti I |  | root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 475 | Ch_3CCT | commentary | commentary | context | yes | same-text | em3gguVpIUyFWz4E0feXg | WA0RT0680 | Candrakīrti I |  | root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | sādhana (`མངོན་པར་རྟོགས་པ`) |
| 476 | Ch_3CCW | commentary | commentary | context | yes | same-text | shsoyCVXtKZ5KNzKl1VY2 | WA0RT3209 | Candrakīrti I | Na_3CAl_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 477 | Ch_3CCY | commentary | commentary | context | yes | same-text | bAe4JcC5OuZYcd0LEZnjI | WA0RT3212 | Candrakīrti I | Na_3CAn_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 478 | Dh_3CEz_ | commentary | commentary | context | yes | same-text | Cg6Hf3hZOG33DfEgBKql5 | WA0RT0320 | Dharmakīrti III |  | root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 479 | Dh_3CF4 | commentary | commentary | context | yes | same-text | Tlro4tCJL9K4rb9QVLxHM | WA0RT3489 | Dharmakīrti II |  | root not in our corpus | History and Stories / ལོ་རྒྱུས་དང་སྒྲུང་། | History and Stories (openpecha) |  |
| 480 | Dh_3CFA | commentary | commentary | context | yes | same-text | x9nv2cZHFLdkWm34gaChx | WA0RT3552 | Dharmakīrti I | Dh_3CF9 |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 481 | Dh_3CFB | commentary | commentary | context | yes | same-text | oPcWTAohOo3L8xk5TMSPo | WA0RT3553 | Dharmakīrti I | Dh_3CF5 |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 482 | Di_3CEf_ | commentary | commentary | context | yes | same-text | YZQFE3hV12nHe4zPIS7jY | WA0RT0045 | Dignāga |  | root not in our corpus | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 483 | Di_3CEg_ | commentary | commentary | context | yes | same-text | kY292MaOwpmQGnNZlS8AS | WA0RT0046 | Dignāga |  | root not in our corpus | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 484 | Di_3CEh_ | commentary | commentary | folder | no | no OpenPecha record has this title |  |  |  |  | reading undecided — file_type from the folder; root not in our corpus |  | Miscellaneous (reading) |  |
| 485 | Di_3CEm_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) | prayer (`སྨོན་ལམ`) |
| 486 | Di_3CEo_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Va_3CEX |  |  | Systematic Treatises (reading) |  |
| 487 | Di_3CEr_ | commentary | commentary | context | yes | same-text | XND4Tdt8bPsSJcfS4J4NO | WA0RT3541 | Dignāga | Di_3CEp_ |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 488 | Di_3CEt_ | commentary | commentary | context | yes | same-text | 9nfp8G2UITP3gt7uu6alU | WA0RT3543 | Dignāga | Di_3CEs_ |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 489 | Gu_3CFP | commentary | commentary | context | yes | same-text | oZ72tS4nYhnGV9VQV3s3O | WA0RT3383 | Guṇaprabha | As_3CDn_ |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 490 | Gu_3CFQ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | As_3CDn_ |  |  | Mind-only Treatises (reading) |  |
| 491 | Gu_3CFR | commentary | commentary | context | yes | same-text | H75GVvpXSDeh0lbo8w3PO | WA0RT3405 | Guṇaprabha | Va_3CEP |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 492 | Gu_3CFU | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Gu_3CFS |  |  | Monastic Rules (reading) |  |
| 493 | Gu_3CFV | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Gu_3CFS |  |  | Monastic Rules (reading) |  |
| 494 | Gu_3CFW | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Gu_3CFS |  |  | Monastic Rules (reading) |  |
| 495 | Gu_3CFX | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Gu_3CFS |  |  | Monastic Rules (reading) |  |
| 496 | Gu_3CFY | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Gu_3CFS |  |  | Monastic Rules (reading) |  |
| 497 | Ha_3CFK | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Prajñāpāramitā (reading) | sādhana (`མངོན་པར་རྟོགས་པ`) |
| 498 | Ha_3CFL | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Prajñāpāramitā (reading) | sādhana (`མངོན་པར་རྟོགས་པ`) |
| 499 | Ha_3CFM | commentary | commentary | context | yes | same-text | d1GBmNXgtFkvmNF7Ps1L6 | WA0RT3137 | Haribhadra |  | root not in our corpus | Perfection of Wisdom / ཤེར་ཕྱིན། | Prajñāpāramitā (openpecha) |  |
| 500 | Ha_3CFN | commentary | commentary | context | yes | same-text | sRlnSYAkvUdiaZODaGTmH | WA0RT3138 | Haribhadra |  | root not in our corpus | Perfection of Wisdom / ཤེར་ཕྱིན། | Prajñāpāramitā (openpecha) | sādhana (`མངོན་པར་རྟོགས་པ`) |
| 501 | Ka_3CDa_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Sh_3CDE |  |  | Logic (reading) |  |
| 502 | Ka_3CDb_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Sh_3CDE |  |  | Logic (reading) |  |
| 503 | Ka_3CDG | commentary | commentary | context | yes | same-text | hiYrc4BPc0vbjYnPx6Ps4 | WA0RT3160 | kamalashila |  | root not in our corpus | Perfection of Wisdom / ཤེར་ཕྱིན། | Prajñāpāramitā (openpecha) |  |
| 504 | Ka_3CDH | commentary | commentary | openpecha-data | yes | same-text | 93udYd4MdkVJ1NK9gLNEi | WA0RT3162 | kamalashila |  | root not in our corpus | Perfection of Wisdom / ཤེར་ཕྱིན། | Prajñāpāramitā (openpecha) |  |
| 505 | Ka_3CDI | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Prajñāpāramitā (reading) |  |
| 506 | Ka_3CDJ | commentary | commentary | context | yes | same-text | 2s3G9cWCpRgjzSYd5arxW | WA0RT3231 | kamalashila | Sh_3CDB |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 507 | Ka_3CDS | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) | dhāraṇī (`གཟུངས`) |
| 508 | Ka_3CDT | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) |  |
| 509 | Ka_3CDU | commentary | commentary | context | yes | same-text | x3ieLYD33Av2Y9Z27FwzB | WA0RT3466 | kamalashila |  | root not in our corpus | Monastic Rules / འདུལ་བ། | Monastic Rules (openpecha) |  |
| 510 | Ka_3CDX | commentary | commentary | context | yes | same-text | jfCLr1MVFE7A2iiNeR0by | WA0RT3568 | kamalashila | Dh_3CF7 |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 511 | Ka_3CDZ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Sh_3CDE |  |  | Logic (reading) |  |
| 512 | Na_3C98 | commentary | commentary | context | yes | same-text | 712qnDL3HdkDiPrJvjjlE | WA0RT0016 | Nāgārjuna | Na_3C97 |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 513 | Na_3C9f_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Middle Way (reading) |  |
| 514 | Na_3C9g_ | commentary | commentary | context | yes | same-text | ydxruSdBmjG0YG6HSxb7M | WA0RT0693 |  | Na_3C9e_ |  | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 515 | Na_3C9L | commentary | commentary | folder | yes | same-text | KjIeO9qV2D915Doyaa6AB | WA0RT0336 | Nāgārjuna |  | reading undecided — file_type from the folder; root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) |  |
| 516 | Na_3C9l_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Tantras (reading) |  |
| 517 | Na_3C9m_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Tantras (reading) |  |
| 518 | Na_3C9q_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Tantras (reading) | sādhana (`སྒྲུབ་ཐབས`) |
| 519 | Na_3C9Z | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Tantras (reading) |  |
| 520 | Na_3CA4 | commentary | commentary | context | yes | same-text | sbfklJYpVhOtcG6puQGtx | WA0RT1499 | Nāgārjuna |  | root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | ritual (`ཆོ་ག`) |
| 521 | Na_3CAa_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Na_3CAZ |  |  | Tantras (reading) |  |
| 522 | Na_3CAp_ | commentary | commentary | context | yes | same-text | 5wPLZFpQ6gqRq4WVLz1aE | WA0RT3174 | Nāgārjuna | Na_3CAk_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 523 | Na_3CAq_ | commentary | commentary | context | yes | same-text | P5ura19dj63A3is2dMWh4 | WA0RT3175 | Nāgārjuna | Na_3CAm_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 524 | Na_3CAs_ | commentary | commentary | context | yes | same-text | XtRi3YBD08DSLXnTP2QXz | WA0RT3176 | Nāgārjuna | Na_3CAn_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 525 | Na_3CAt_ | commentary | commentary | context | yes | same-text | 0UpTWku7Q2Ync3R13WbXF | WA0RT3177 | Nāgārjuna | Na_3CAo_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 526 | Na_3CAw_ | commentary | commentary | context | yes | same-text | J4FvXlJwc21CrA78CGfUG | WA0RT3180 | Nāgārjuna | Na_3CAv_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 527 | Na_3CAy_ | commentary | commentary | context | yes | same-text | sruzmvRZ3WdlxulvpMU87 | WA0RT4226 | Nāgārjuna | Na_3CAx_ |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 528 | Na_3CB7 | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Na_3CB6 |  |  | Discourses (reading) |  |
| 529 | Na_3CB8 | commentary | commentary | context | yes | same-text | J4oZQYmTuFL2vVL26MyBY | WA0RT3345 | Nāgārjuna |  | root not in our corpus | Discourses / མདོ་སྡེ། | Discourses (openpecha) | confession (`བཤགས`) |
| 530 | Na_3CB9 | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) | prayer (`སྨོན་ལམ`) |
| 531 | Na_3CBA | commentary | commentary | context | yes | same-text | frgCczuw9Xux8CVymw39s | WA0RT3439 | Nāgārjuna |  | root not in our corpus | Systematic Treatises / མངོན་པ། | Systematic Treatises (openpecha) |  |
| 532 | Sh_3CCk_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Sh_3CCl_ |  |  | Tantras (reading) | ritual (`ཆོག`) |
| 533 | Sh_3CCo_ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) |  |
| 534 | Sh_3CCw_ | commentary | commentary | context | yes | same-text | 5ut7ZxPBxRnrgyWrUYRYK | WA0RT0052 | Śāntirakṣita | Sh_3CCv_ |  | Miscenaleous / སྣ་ཚོགས། | Miscellaneous (openpecha) | praise (`བསྟོད`) |
| 535 | Sh_3CD0 | commentary | commentary | context | yes | same-text | 50q2AU9uo62zXOFj5ey9S | WA0RT1501 | Śāntirakṣita |  | root not in our corpus | Tantras / རྒྱུད་སྡེ། | Tantras (openpecha) | dhāraṇī (`གཟུངས`) |
| 536 | Sh_3CD9 | commentary | commentary | context | yes | same-text | PSRnyejijiohh8mHs3Etn | WA0RT3228 | Śāntirakṣita |  | root not in our corpus | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 537 | Sh_3CDB | commentary | commentary | context | yes | same-text | AqirupJY5acnotaZDEAmw | WA0RT3230 | Śāntirakṣita | Sh_3CDA |  | Middle Way / དབུ་མ། | Middle Way (openpecha) |  |
| 538 | Sh_3CDC | commentary | commentary | context | yes | same-text | lyKD4cUoyc68tzBDr0tnr | WA0RT3420 | Śāntirakṣita |  | root not in our corpus | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 539 | Sh_3CDD | commentary | commentary | context | yes | same-text | 9u4HFaS9uZv2wfCifWeVt | WA0RT3575 | Śāntirakṣita | Dh_3CFC |  | Logic / ཚད་མ། | Logic (openpecha) |  |
| 540 | Sh_3CFa_ | commentary | commentary | context | yes | same-text | zf3GOdym24a6WIqK69TUN | WA0RT3463 | Śākyaprabha | Sh_3CFZ |  | Monastic Rules / འདུལ་བ། | Monastic Rules (openpecha) |  |
| 541 | Va_3CE1 | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) | dhāraṇī (`གཟུངས`) |
| 542 | Va_3CE2 | commentary | commentary | context | yes | part | MFwyJj9frTMF4aFa8Jp5l | WA0RT3153 | Vasubandhu |  | root not in our corpus | Perfection of Wisdom / ཤེར་ཕྱིན། | Prajñāpāramitā (openpecha) |  |
| 543 | Va_3CE3 | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Prajñāpāramitā (reading) |  |
| 544 | Va_3CE4 | commentary | commentary | context | yes | same-text | SNN7rW1hmwTzroG8hxrjc | WA0RT3161 | Vasubandhu |  | root not in our corpus | Perfection of Wisdom / ཤེར་ཕྱིན། | Prajñāpāramitā (openpecha) |  |
| 545 | Va_3CE5 | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) |  |
| 546 | Va_3CE6 | commentary | commentary | context | yes | same-text | 0OUgC7JNJmI0djtXhJHyz | WA0RT3328 | Vasubandhu | Va_3CEY |  | Discourses / མདོ་སྡེ། | Discourses (openpecha) |  |
| 547 | Va_3CE7 | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) | dhāraṇī (`གཟུངས`) |
| 548 | Va_3CE8 | commentary | commentary | context | yes | same-text | NQwKjbjxhETmEYypHbMGP | WA0RT3330 | Vasubandhu; Jñānadatta |  | root not in our corpus | Discourses / མདོ་སྡེ། | Discourses (openpecha) |  |
| 549 | Va_3CE9 | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) |  |
| 550 | Va_3CEA | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) |  |
| 551 | Va_3CEB | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) |  |
| 552 | Va_3CEC | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) |  |
| 553 | Va_3CED | commentary | commentary | context | yes | same-text | KKmXgN3G68fGIP8UxAT7I | WA0RT3335 | Vasubandhu |  | root not in our corpus | Discourses / མདོ་སྡེ། | Discourses (openpecha) |  |
| 554 | Va_3CEE | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) | prayer (`སྨོན་ལམ`) |
| 555 | Va_3CEF | commentary | commentary | openpecha-data | yes | title-only | JNwkKtmUZaerroM2TNY7F |  |  |  | root not in our corpus | Perfection of Wisdom / ཤེར་ཕྱིན། | Prajñāpāramitā (openpecha) |  |
| 556 | Va_3CEG | commentary | commentary | context | yes | same-text | KFtOUYAC7GyBwDSMcvbQ4 | WA0RT3367 | Vasubandhu |  | root not in our corpus | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 557 | Va_3CEH | commentary | commentary | context | yes | same-text | J2GkR2XfMj0lqk6qKpBQh | WA0RT3389 | Vasubandhu | As_3CDu_ |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 558 | Va_3CEI | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  |  | root not in our corpus |  | Discourses (reading) |  |
| 559 | Va_3CEJ | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Va_3CEX |  |  | Systematic Treatises (reading) |  |
| 560 | Va_3CEK | commentary | commentary | context | no | no OpenPecha record has this title |  |  |  | Va_3CEX |  |  | Systematic Treatises (reading) |  |
| 561 | Va_3CEN | commentary | commentary | context | yes | same-text | 0qwYR8ddEkdo7vMls5301 | WA0RT3396 | Vasubandhu | Va_3CEM |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 562 | Va_3CEU | commentary | commentary | context | yes | same-text | LE7rnhbWugyjKCKWMxMdq | WA0RT3365 | Vasubandhu |  | root not in our corpus | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 563 | Va_3CEV | commentary | commentary | context | yes | same-text | pVFCgPKkLfrCicqzyyoKU | WA0RT3391 |  | As_3CDu_ |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 564 | Va_3CEW | commentary | commentary | context | yes | same-text | MFhukLeZvy1qa2IGGLfQZ | WA0RT3406 |  | Va_3CEP |  | Mind-only Treatises / སེམས་ཙམ། | Mind-only Treatises (openpecha) |  |
| 565 | Va_3CEZ | commentary | commentary | context | yes | same-text | Hmq92AyQRl4WtXIPL0bUD | WA0RT3441 | Vasubandhu | Va_3CEY |  | Systematic Treatises / མངོན་པ། | Systematic Treatises (openpecha) |  |
