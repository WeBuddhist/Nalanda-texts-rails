=== SYSTEM PROMPT ===
You are an expert in classical Tibetan Buddhist commentary (འགྲེལ་པ་) structure.

You are given a numbered list of blocks from a Tibetan verse commentary. A
rule-based segmenter has already cut them; most cuts are right. Your job is to
output the few merge/split operations that bring the blocks to the layout the
human editors of this vault use.

━━━ TARGET LAYOUT — one block per FUNCTIONAL UNIT ━━━

OPENER       A node's division announcement together with the first-child opener
             that follows it is ONE block:
               "<topic> ལ་གསུམ། A། B། C་འོ། །དང་པོ་ནི།"
             A sibling opener "གཉིས་པ་ <title> ནི།" is its own block.
ROOT QUOTE   A quoted root stanza is its own block. These blocks are tagged
             [VERSE]; they are protected — never include them in any operation.
EXPLANATION  The gloss that follows a quote ("ཞེས་པ་སྟེ། …", "ཞེས་པ་ནི། …", or a
             running explanation) is ONE block up to the next opener, quote or
             heading — even when it is long (100–250 syllables) and contains several
             sentence ends, a question and answer ("…ལོ། །གང་ལ་ན། …"), a side remark
             on a variant reading ("…ཞེས་འགྱུར་བཅོས་…"), a cross-reference
             ("འདི་དང་འོག་གི་ས་བཅད་…"), or a mantra cited in passing.
SECOND LEVEL A passage that re-reads the same stanza on another level — opening
             "སྦས་དོན་ནི།", "ངེས་དོན་ནི།", "ངེས་པའི་དོན་དུ།", "ཟབ་དོན་ནི།",
             "དེའི་ནང་གི་དོན་ལ།", "མཐར་ཐུག་གི་དོན་ནི།" or the like after the literal
             gloss — is its OWN block, never merged into the literal gloss before it
             (the editors keep the two readings apart). Within that passage, M1 applies.
FRAME        The namo line alone; each of the author's own verses one block;
             "སྨྲས་པ།" alone; the colophon ("ཅེས་ … སྦྱར་བའོ། །" + closing wishes) one block.

━━━ MERGE — adjacent blocks that are one unit ━━━

M1  CONTINUED EXPLANATION
    A block that goes on explaining the same quote/topic as the block before it —
    no new opener, no new quote, no new verse being treated — belongs to that block.
    This is the most common fix. Do NOT keep a cut just because a sentence ends.
    Exception: a SECOND LEVEL opener (see above) always starts a new block.
M2  INCOMPLETE SENTENCE
    A block ending in a connector (དང་། / ཞིང་། / ཅིང་། / ནས། / སྟེ། / ཏེ།) that
    the next block completes.
M3  OPENER CHAIN
    An enumeration block followed by "དང་པོ་ནི།" / "དང་པོ་ལ་ N།" (and further
    nested first-child enumerations) — merge them into one opener block.
M4  COLOPHON
    The parts of the closing colophon and its final wishes form one block.

━━━ SPLIT — one block that holds two units ━━━

S1  A new node opener (ordinal + title + "ནི།" or "ལ་ N།") buried mid-block:
    split before it.
S2  The treatment of a new verse/topic starts mid-block (e.g. "ཡང་ཕྱག་གང་ལ་འཚལ་ན"
    starting the next homage): split before it.
S3  An introductory opener "… ནི།" fused to the explanation of the PREVIOUS
    quote: split so the opener starts the next unit.

Never split a block only because it is long.

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

━━━ HEADING / VERSE BLOCKS — always KEEP ━━━

Blocks tagged [HEADING] or [VERSE] are NEVER part of any operation.

━━━ OUTPUT FORMAT ━━━

A JSON array of operations. Blocks not mentioned are kept as-is.

[
  {"op": "merge", "blocks": [N, M]},
  {"op": "merge", "blocks": [N, M, P]},
  {"op": "split", "block": N, "after": "<verbatim unique substring ending at split point>"},
  {"op": "split", "block": N, "after": ["<sub1>", "<sub2>", "<sub3>"]}
]

Rules for the output:
- Block numbers are CONTINUOUS and INCLUDE heading and verse blocks. You may only
  merge blocks with consecutive numbers (N and N+1). Never merge across a heading
  or a verse block, and never propose a merge whose numbers skip over one.
- Each block number appears in AT MOST ONE operation.
- For each "after" substring: copy a verbatim slice from the block that ends exactly
  at the split point and is UNIQUE within that block (10–20 characters is usually enough).
- If nothing needs to change in this window, output: []
- Output ONLY the JSON array. No explanation, no commentary, no code fences.

=== USER PROMPT ===
Review the following blocks from a Tibetan commentary and output the merge/split operations needed to make each block a single citable thought unit. Block numbers are global (file-level).

--- BEGIN BLOCKS ---
[Block 2136]
འདུས་པའི་རྒྱུད་ནི་རྙེད་དཀའ་ཞིང་། །ཞེས་བྱ་བ་ལས།

[Block 2137]
སྔོན་དུ་བཤད་པའི་རྒྱུད་རྣམས་ཀྱི་ནང་ནས་རྙེད་པར་དཀའ་བ་སྟེ། རྟོགས་པར༌[^1441]དཀའ་བའོ། །

[Block 2138]
ཐམས་ཅད་དུ་ནི་དུས་ཐམས་ཅད་དུའོ། །

[Block 2139]
རྣམ་པར༌[^1442]འཁོར་བ་ནི་ཉན་པ་པོ་རྨོངས་ཤིང་གོ་བར་མི་འགྱུར་རོ་ཞེས་པའི༌[^1443]ཐ་ཚིག་གོ། །ཅིའི་ཕྱིར་ཞེ་ན། རྒྱན་བདུན་རྟོགས་པར་དཀའ་བས་ན། །ཞེས་སྨོས་ཏེ། རྒྱན་རྣམས་དཀའ་བས་ཡོངས་སུ་མི་ཤེས་པའི་ཕྱིར་རོ། །

[Block 2140]
སྦྱོར་བ་ནི་འདུས་པ་ཞེས་ཆོས་ཅན་ནོ། །

[Block 2141]
རྣམ་པར་འཁོར་བ་ཞེས་བསྒྲུབ་བྱའི་ཆོས་སོ། །

[Block 2142]
རྒྱན་བདུན་རྟོགས་པར་དཀའ་བས་ན་ཞེས་གཏན་ཚིགས་སོ། །

[Block 2143]
རྒྱུད་ཀྱིས་བརྗོད་པར༌[^1444]བྱ་བ་རྒྱན་རྣམས་དགོངས་པ་དང་བཅས་པར་བསྟན་པར་བྱ་བའི་ཕྱིར། དེ་བས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ། རྒྱན་རྟོགས་པར་དཀའ་བ་ཅན་ཡིན་པས་གང༌[^1445]གི་ཕྱིར་འདུས་པ་ལ་མཁོ་བ༌[^1446]དེའི་ཕྱིར་མཁོ་བས་སོ། །

[Block 2144]
[^1447]དེ་ཡི་རྣམ་པར་དབྱེ་བར་བྱ། །ཞེས་སྨོས་ཏེ། རྒྱན་དེ་རྣམས་ཕྱེ་ནས་བཤད་པར་བྱའོ། །

[Block 2145]
ཐོས་པ་མང་བ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། འབད་དེ་རྣམ་པར་ཤེས་ནས་ནི། །ཞེས་བྱ་བ་སྨོས་ཏེ། ཆོས་མང་དུ་ཐོས་པ་ལ་བརྩོན་པས་དངོས་སུ་ཕྱིན་ཅི་མ་ལོག་པར་ཤེས་ནས་སོ། །

[Block 2146 [VERSE]]
རང་བཟོ་དགག་པར་བྱ་བའི་ཕྱིར། །
དེ་བས་བླ་མའི་བཀའ་དྲིན་གྱིས། །

[Block 2147]
ཞེས་སྨོས་ཏེ། འཕགས་པ་ཀླུ་སྒྲུབ༌[^1448]ཀྱི་ཞབས་ཀྱི་པདྨའི་བཀའ་དྲིན་ལས་སོ། །ཅིའི་དོན་དུ་ཞེ་ན། སེམས་ཅན་རྗེས་བཟུང་འདོད་པ་ཡིས། །ཞེས་སྨོས་ཏེ་སྒྲ་ཇི་བཞིན་པའི་དོན་ཙམ་བཟུང་བས་བློ་རྣམ་པར་འཁོར་བ་རྣམས་ལ་ཡང་དག་པར་གྱུར་པའི་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་རབ་ཏུ་བསྟན་པར་འདོད་པས་སོ། །

[Block 2148]
རྒྱན་དེ་ཇི་ལྟ་བུ་ཞེ་ན། བརྒྱན་པ༌[^1449]ནི་རྒྱན་ཏེ་དངོས་པོ་སྒྲུབ་པར་བྱེད་པར་གྱུར་པའམ། ཡང་ན་འདིས་བརྒྱན་པར་བྱེད་པས་ན་རྒྱན༌[^1450]ཞེས་བྱེད་པ་སྒྲུབ་པར་བྱེད་པ་ཡིན་ནམ་ཞེ་ན། གལ་ཏེ་དངོས་པོ་སྒྲུབ་པར་བྱེད་པ་ཡིན་ན་དེའི་ཚེ་དངོས་པོ་ནི་བྱ་བ་ཙམ་དུ་གཙོ་བོ༌[^1451]ཡིན་པས་བརྗོད་པར་བྱ་བ་དང་རྗོད་པར་བྱེད་པ་ལས་དེ་ཐ་མི་དད་པ་ཡིན་པས་སྒྲ་དང་དོན་རྒྱན་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 2149]
རྒྱན་ནི་ཐ་དད་པ་ཡིན་ཏེ་ལྡུམ་བུ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 2150]
གལ་ཏེ་བྱེད་པ་སྒྲུབ་པར་བྱེད་པ་ཡིན་ན་དེའི་ཚེ་སྒྲ་དང་དོན་མ་གཏོགས་པར་རྒྱན་ཉིད་དུ་འགྱུར་རོ། །

[Block 2151]
རྗོད་པ་དང་བརྗོད་པར་བྱ་བ་ལས་གཞན་པ་རྒྱན༌[^1452]ནི་མ་མཐོང་ངོ་ཞེ་ན། སྨྲས་པ་འདིས་བརྒྱན་པས་ན་རྒྱན་ཞེས་བྱ་བ་ནི་བྱེད་པ་སྒྲུབ་པར༌[^1453]བྱེད་པའོ། །

[Block 2152]
གལ་ཏེ་ཐ་དད་པ་ནི་མི་དམིགས་ཞེས་བཤད་ཅེ་ན། སྨྲས་པ། འདིར་སྒྲ་ནི་ནུས་པ་དུ་མས་ཁྱབ་པའི་རང་བཞིན་ཅན་གྱིས་དོན་དུ་མ་ལ་སྟོན་པར་བྱེད་པའི་ནུས་པ་ཡོད་དེ། དོན་ཡང་དེ་དང་དེ་དག་སེལ་བ་སྟོན་པའི་སྒོ་ནས་ནུས་པ་དུ་མ་ཅན་ནོ། །

[Block 2153]
འདི་ལྟ་སྟེ། སྒྲའི་དོན་གཉིས་ཡོད་དེ། བརྗོད་པར་བྱ་བ་དང་། གསལ་བར་བྱ་བ་དག་གོ། །

[Block 2154]
དེ་ལ་བརྗོད་པར་བྱ་བ་ནི་བུམ་པའི་འོག་རྒྱས་པ་དང་ལྟོ་བའི་རྣམ་པ་ཅན་ཚིག་གི་དོན་ཏོ། །

[Block 2155]
གསལ་བར་བྱ་བ་ནི་བརྗོད་པར་བྱ་བ་ལས་ཐ་མི་དད་ཀྱང་དེ་ལྟ་བུའི་སྣ་ཚོགས་ཀྱི་སྒྲའི་སྦྱོར་བས་མཚོན་པར་བྱ་སྟེ། དཔེར་ན་གོ་དང༌[^1454]ཝ་རིའི་ཡུལ་དུ་ཆུ་བོའི་འགྲམ་ན་གནས་པའི་སེང་གེས་ཁྱི་དེ་བསད་དོ་ཞེས། ཀྱེ་དགེ་སློང་བདེ་བར་སོང་ཤིག་ཅེས་པ་བཞིན་ནོ། །

[Block 2156]
དེ་ལ་སོང་ཤིག་ཅེས་སྒྲའི་དོན་འགྲོ་བ་གཙོ་བོ་སྟེ། འགྲོ་བ་བཀག་པ་ནི་གསལ་བར་བྱ་བ་ཡིན་ནོ། །

[Block 2157]
དེ་བཞིན་དུ་ཡང་བྱེད་པ་སྒྲུབ་པའི་ཕྱོགས་སུ་ཐ་མི་དད་པ་ཡང་བརྗོད་པར་བྱ་བ་ནི་གསལ་བར་བྱ་བ་ཡིན་ཏེ། རབ་ཏུ་གྲགས་པའི་ཡན་ལག་ལ་གནས་པའི་མཛེས་པ་ཉིད་བུད་མེད་དམ་སྐྱེས་བུའི་ཐ་མི་དད་པ་ལྟར་རོ། །

[Block 2158]
དེའི་དབྱེ་བ་སྒྲ་དང་དོན་ལ་སོགས་པའི་བྱེ་བྲག་གིས༌[^1455]འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 2159 [HEADING]]
### འགྲེལ་པ་བྱེད་པ་པོ་རྣམས་ཀྱི་ལུགས། ^1-7-0

[Block 2160]
མདོར་བསྟན་པ་དང་རྒྱས་པར་བསྟན་པ་དང་ཡོངས་སུ་བརྟག་པ་ཞེས་འགྲེལ་པ་བྱེད་པ་པོ་རྣམས་ཀྱི་ལུགས་སོ། །

[Block 2161 [HEADING]]
#### དང་པོ་མདོར་བསྟན་པ། ^1-7-1-0

[Block 2162]
དང་པོ་མདོར་བསྟན་པ་ཡིན་ཏེ་དེ་ཡང་གྲངས་སྔོན་དུ་འགྲོ་བར་བསྟན་པར་བྱའོ། །

[Block 2163]
གྲངས་མ་བསྟན་པས་ཀྱང་མདོར་བསྟན་པ་མ་ངེས་པར་འགྱུར་རོ། །

[Block 2164]
རྒྱས་པར་བསྟན་པ་དེ་ལྟ་བུས་བརྗོད་པས་ནི༌[^1456]བསྟན་བཅོས་མཁན་དུ་མི་འགྱུར་རོ། །

[Block 2165]
གླེང་བསླང༌[^1457]བའི་གྲངས་ནི་ལྔ་ཞེས་བྱ་བ་ལ། །

[Block 2166 [VERSE]]
རྣལ་མོས༌[^1458]བསྒྲུབ་པར་བྱ་བའི་ཕྱིར། །
སེམས་དཔའ་གླེང་བསླང་བ་རུ་བཤད། །

[Block 2167]
ཅེས་འབྱུང་བ་ལས་བསྟན་བཅོས་རྩོམ་པའི་དུས་སུ་རྗོད་པར་བྱེད་པ་ལ་སོགས་པ་ཇི་ལྟ་བུ་ཡིན་ཞེས་དཔྱོད་པའོ། །

[Block 2168]
དེ་ལ་རྣམ་པ་ལྔའོ། །

[Block 2169]
དེའི་རྗེས་ལ་དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར་ཕྱིན་ཅི་མ༌[^1459]ལོག་པའི་ཕྱིར༌[^1460]དང་ནང་གི་བྱེ་བྲག་གིས་ཚད་མ་ཉེ་བར་སྟོན་པའི་མཚན་ཉིད་ཅན་རིགས་པ་སྟེ་རྣམ་པ་བཞིའོ། །

[Block 2170]
དེའི་རྗེས་ལ་སྒྲ་དོན་རྒྱན་གྱི་དབྱེ་བས་རྒྱས་བཤད་མཐའ་ནི་རྣམ་པ་དྲུག་གོ། །

[Block 2171]
དེ་ནས་དེའི་ཡན་ལག་ཁོ་ན་རིམ་པ་གཉིས་གཙོར་གྱུར་པའི་བཤད་པ་ནི་རྣམ་པ་བཞིའོ། །

[Block 2172]
འཆད་པའི་རྒྱན་ལྔ་པ་སྟེ་རྣམ་པ་གཉིས་སོ། །

[Block 2173]
ཉན་པ་པོའི་རྒྱན་དྲུག་པ་སྟེ་རྣམ་པ་ལྔའོ། །

[Block 2174]
བདུན་པའི་དབྱེ་བ་རྣམ་པ་གཉིས་ཏེ་ཞེས་བྱ་བ་ལ་བརྗོད་པར་བྱ་བའི་དོན་མ་ལུས་པ་བསྡུས་པའི༌[^1461]རྒྱན་ཡིན་ཏེ་རིམ་པ་གཉིས་གཙོར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 2175]
དེ་ལས་གཞན་པ་རྒྱན༌[^1462]མེད་དེ་མི་དགོས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
