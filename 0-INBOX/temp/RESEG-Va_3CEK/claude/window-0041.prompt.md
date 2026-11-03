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
[Block 1436]
བཟོད་པས་གཞོམ་མིན་བསྒོམ་ཁོ་ནས། །ས་ཐམས་ཅད་ན་ཕྲ་རྒྱས་གང་དག་ཤེས་པས་གཞོམ་པར༌[^1014]བྱ་བ་ཡོད་པ་དེ་དག་ནི་གཉི་གའི་ཡང་རྟག་ཏུ་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1437]
གཞན་དག་ན་རེ་ཕྱི་རོལ་པ་རྣམས་ཀྱིས་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ནི༌[^1015]སྤོང་བ་ཁོ་ན་སྟེ། འདི་ལྟར་ལས་རྣམ་པར་འབྱེད་པ་ཆེན་པོའི༌[^1016]མདོ་དང་སྔོན་གྱི་མཐའ་ལས༌[^1017]རྟོག་པ་སྤོང་བ༌[^1018]རྣམས་ལས་རྟག་པར་སྨྲ་བ་རྣམས་དང་། ལ་ལ་རྟག་པར་སྨྲ་བ་རྣམས་དང་། རྒྱུ་མེད་པ་ལས་ཀུན་དུ་འབྱུང་བར་སྨྲ་བ་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ལ༌[^1019]འདོད་པའི་ཁམས་ལས་དམིགས་པའི་ལྟ་བ་ཀུན་དུ༌[^1020]འབྱུང་བར་གསུངས་ཏེ། གཟུགས་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་རྣམས་འདོད་པའི་ཁམས་ལ་དམིགས་པ་ནི་མ་ཡིན་ཏེ། འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1438]
དེ་ལྟ་བས་ན་འདོད་པ་དང་ལྡན་པ་དེ་དག་ཁོ་ན་མ་སྤངས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1439]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་དེ་དག་ཀྱང༌[^1021]ལྟ་བ་བསྐྱེད་པ༌[^1022]དང་དུས་མཉམ་དུ་ཡོངས་སུ་ཉམས་པའི་ཕྱིར་ཏེ། ལྷ་སྦྱིན་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1440 [HEADING]]
### ལྟ་བ་ལྔའི་རང་གི་ངོ་བོ། ^2-8-0

[Block 1441]
ལྟ་བ་ལྔ་མིང་གི་སྒོ་ནས་བསྟན་གྱི་རང་གི་ངོ་བོའི་སྒོ་ནས་ནི་མ་བསྟན་པས་འདི་དག་གི་རང་གི་ངོ་བོ་ཅི་ཞེ་ན།

[Block 1442 [VERSE]]
བདག་དང་བདག་གི་རྟག་ཆད་དང་། །
མེ༌[^1023]དང་སྨན༌[^1024]ལ་མཆོག་ལྟ་དང་། །
རྒྱུ་མིན་ལམ་མིན་དེར་ལྟ་བ། །
དེ་དག་ལྟ་བ་ལྔ་ཡིན་ནོ། །

[Block 1443 [HEADING]]
#### འཇིག་ཚོགས་ལ་ལྟ་བ། ^2-8-1-0

[Block 1444]
བདག་གམ་བདག་གིར་ལྟ་བ་ནི། །འཇིག་ཚོགས་ལ་ལྟ་བའོ། །

[Block 1445]
འཇིག་པས་ན་འཇིག་པའོ། །

[Block 1446]
བསགས་པས་ན་ཚོགས་པ་སྟེ།[^1025] མང་པོ་དང་ཕུང་པོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1447]
འདི་ནི་འཇིག་པ་ཡང་ཡིན་ལ་ཚོགས་ཀྱང་ཡིན་པས་འཇིག་ཚོགས་ཏེ། ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔའོ། །

[Block 1448]
རྟག་པར་འདུ་ཤེས་པ་དང་། རིལ་པོར་འདུ་ཤེས་པ་སྤང་བའི་ཕྱིར། དེ་སྐད་དུ་བཤད་དེ། དེ་དག་ལ་བདག་ཏུ་འཛིན་པ་ནི་དེ་དག་སྔོན་དུ་འགྲོ་བ་ཅན་ཡིན་ནོ། །

[Block 1449]
འཇིག་ཚོགས་ལ་ལྟ་བས་ན༌[^1026]འཇིག་ཚོགས་ལ་ལྟ་བའོ། །

[Block 1450]
ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་ཐམས་ཅད་ཀྱང་འཇིག་ཚོགས་ལ་ལྟ་བ་ཡིན་མོད་ཀྱི། ཅི་ནས་ཀྱང་འདི་ནི་འཇིག་ཚོགས་ལ་ལྟ་བ་ཡིན་གྱི། བདག་གམ་བདག་གི་ལ་ནི་མ་ཡིན་ནོ། །ཞེས་རྟོགས་པར་བྱ་བའི་ཕྱིར་བདག་དང་བདག་གིར་ལྟ་བ་ཁོ་ན་འཇིག་ཚོགས་ཇི༌[^1027]ལྟ་བར་བཤད་དེ། ཇི་སྐད་དུ་དགེ་སློང་དག་དགེ་སྦྱོང་ངམ། བྲམ་ཟེ་གང་ལ་ལ་བདག་གོ་སྙམ་དུ་ཡང་དག་པར་རྗེས་སུ་ལྟ་བ་ན་ཡང་དག་པར་རྗེས་སུ་ལྟ་བ་དེ་དག་ཐམས་ཅད་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ༌[^1028]འདི་དག་ལ་ལྟ་བ་ཁོ་ནར་ཟད་དོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 1451 [HEADING]]
#### མཐར་འཛིན་པར་ལྟ་བ། ^2-8-2-0

[Block 1452]
བདག་ཏུ་མངོན་པར་འདོད་པའི་དངོས་པོ་དེ་ཉིད་ལ་རྟག་པར་ལྟ་བའམ། ཆད་པར་ལྟ་བ་ནི་མཐར་འཛིན་པར་ལྟ་བ་སྟེ། རྟག་པ་དང་ཆད་པའི་མཐར་འཛིན་པའི་ཕྱིར་རོ། །

[Block 1453 [HEADING]]
#### ལོག་པར་ལྟ་བ། ^2-8-3-0

[Block 1454]
སྡུག་བསྔལ་བ༌[^1029]ལ་སོགས་པའི་བདེན་པ་ཡོད་ན་མེད་དོ་ཞེས་བྱ་བ༌[^1030]ནི་ལོག་པར་ལྟ་བའོ། །

[Block 1455]
ལོག་པར་ཞུགས་པའི་ལྟ་བ་ཐམས་ཅད་ལོག་པར་ལྟ་བ་ཡིན་པ་ལས་མར་དྲང་བ༌[^1031]བཞིན་དུ་ཧ་ཅང་ཚབས་ཆེན་པོ་དང་ལྡན་པའི་ཕྱིར་གཅིག་ཁོ་ན་བཤད་དེ། འདི་ནི་སྐུར་པ་འདེབས་པར་བྱེད་པ་ཡིན་ལ། གཞན་དག་ནི་སྒྲོ་འདོགས་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1456 [HEADING]]
#### ལྟ་བ་མཆོག་ཏུ་འཛིན་པ། ^2-8-4-0

[Block 1457]
དམན་པ་ལ་མཆོག་ཏུ་འཛིན་པར༌[^1032]ལྟ་བ་ནི་ལྟ་བ་མཆོག་ཏུ་འཛིན་པའོ། །

[Block 1458]
དམན་པ་ཡང་ཅི་ཞིག་ཡིན་ཞེ་ན། ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་དེ། འཕགས་པ་རྣམས་ཀྱིས་སྤང་བའི༌[^1033]ཕྱིར་རོ། །

[Block 1459]
དེ་ལ་མཆོག་ཏུ་འཛིན་པ་ནི་ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་ཡིན་ཏེ། ལྟ་བ་ལ་སོགས་པ་མཆོག་ཏུ་འཛིན་པ་ཞེས་བརྗོད་པར་བྱ་བའི་རིགས་པ་ལ་སོགས་པའི་སྒྲ་མི་མངོན་པར་བྱེད་དོ།[^1034] །

[Block 1460 [HEADING]]
#### ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ། ^2-8-5-0

[Block 1461]
རྒྱུ་མ་ཡིན་པ་ལ་རྒྱུར་ལྟ་བ་དང་། ལམ་མ་ཡིན་པ་ལ་ལམ་དུ་ལྟ་བ་ནི་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ཡིན་ཏེ།[^1035] འདི་ལྟ་སྟེ། དབང་ཕྱུག་ཆེན་པོའམ། སྐྱེ་དགུའི་བདག་པོའམ། གཞན་ཡང་རུང་སྟེ། འཇིག་རྟེན་རྣམས་ཀྱི་རྒྱུ་མ་ཡིན་ན་དེ་ལ་ཡང་རྒྱུར་ལྟ་བ་དང་། མེ་དང་ཆུར་འཇུག་པ་ལ་སོགས་པ་མཐོ་རིས་ཀྱི་རྒྱུ་མ་ཡིན་ན་དེ་དག་ལ་ཡང་རྒྱུར་ལྟ་བ་དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ཙམ་དང་། གྲངས་ཅན་དང་རྣལ་འབྱོར་གྱི་ཤེས་པ་ལ་སོགས་པ་ཐར་པའི་ལམ་མ་ཡིན་ན་དེ་དག་ལ་ཡང་ལམ་དུ་ལྟ་བ་ལྟ་བུ་སྟེ། འདིར་ཡང་སོགས་པའི་སྒྲ་མི་མངོན་པར་བྱས་སོ་ཞེས་གྲག་གོ། །

[Block 1462]
དེ་ལྟར་ན་དེ་དག་ནི་ལྟ་བ་ལྔ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1463 [HEADING]]
### ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་སྡུག་བསྔལ་མཐོང་བས་སྤང་བྱ། ^2-9-0

[Block 1464]
གལ་ཏེ་རྒྱུ༌[^1036]ཡིན་པ་ལས༌[^1037]རྒྱུར་ལྟ་བ་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ཡིན་ན། ཅིའི་ཕྱིར་ཀུན་འབྱུང་བས༌[^1038]མཐོང་བས་སྤང་བར༌[^1039]བྱ་བ་མ་ཡིན་ཞེ་ན། གང་ལ་ལ་དབང་ཕྱུག་གམ། སྐྱེ་དགུའི་བདག་པོ་ལ་རྒྱུར་ལྟ་བ་དེ་ནི་དེ་ལ་རྟག་པ༌[^1040]གཅིག་པུ་དང་བདག་དང་བྱེད་པ་པོར་མངོན་པར་ཞེན་ནས་ལྟ་སྟེ། དེ་ལྟ་བས་ན་འདི་ལྟར། དབང་ཕྱུག༌[^1041]སོགས་རྒྱུར་མངོན་ཞེན་པ། དེ་ནི་རྟག་བདག་ཕྱིན་ཅི་ལོག་པ་ཡིས། །

[Block 1465 [VERSE]]
རབ་ཏུ་འཇུག་པས་དེ་ཕྱིར་དེ། །
སྡུག་བསྔལ་མཐོང་བས་སྤང་བྱ་ཉིད། །

[Block 1466]
དེ་དག་ལ་རྟག་པ་དང་། བདག་ཏུ་འཛིན་པ་དེ་གཉིས་ནི་སྡུག་བསྔལ་མཐོང་བ་ཁོ་ནས་སྤོང་བར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་དེས་བྱས་པ་རྒྱུར་མངོན་པར་ཞེན་པ་ཡང་དེ་ཉིད་ཀྱིས༌[^1042]སྤོང་བར་འགྱུར་རོ། །

[Block 1467]
འོ་ན་གང་མེ་དང་ཆུར་འཇུག་པ་ལ་སོགས་པས་མཐོ་རིས་སུ་སྐྱེ་བའམ། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ཀྱིས་འདག་པར་ལྟ་བ་ཇི་ལྟ་བུ་ཡིན། དེ་ཡང་སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་ཏེ། བསྟན་བཅོས་ལས་འདི་སྐད་དུ། གང་དག་སྐྱེས་བུ་གང་ཟག་གང་ཞིག་བ་ལང་གི་ཚུལ་ཁྲིམས་དང་། རི་དགས་ཀྱི་ཚུལ་ཁྲིམས་དང་བྱ་གག་གི་ཚུལ་ཁྲིམས་ཡང་དག་པར་བླངས་ཏེ་གནས་པ་སྟེ།[^1043] དེས་དག་པར་འགྱུར། གྲོལ་བར་འགྱུར། ངེས་པར་འབྱུང་བར་འགྱུར། བདེ་བ་དང་སྡུག་བསྔལ་ལས་རྣམ་པར་འདའ་བར་འགྱུར་ཞིང་བདེ་བ་དང་སྡུག་བསྔལ་ལས་རྣམ་པར་འདས་པ་ཡང་རྗེས་སུ་འཐོབ་པར་འགྱུར་རོ་ཞེས་དེ་ལྟར་ལྟ་ཞིང་དེ་སྐད་དུ་སྨྲ་བ་ནི་རྒྱུ་མ་ཡིན་པ་ལ་རྒྱུར་མངོན་པར་ཡིད་ཆེས་པས་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་སྟེ། སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་ཉིད༌[^1044]ཡིན་ནོ་ཞེས་བྱ་བ་རྒྱས་པར་འབྱུང་ངོ་། །དེ་ཅིའི་ཕྱིར་སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན། སྡུག་བསྔལ་ལ་ལོག་པར་ཞུགས་པའི་ཕྱིར་རོ། །

[Block 1468]
ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་ཐམས་ཅད་སྡུག་བསྔལ་ལ་ལོག་པར་ཞུགས་པའི་ཕྱིར་ཧ་ཅང་ཐལ་བར་འགྱུར་རོ། །

[Block 1469]
ཡང་ན་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ལ༌[^1045]མཐོང་བས་སྤང་བར་བྱ་བ་གཞན་ཇི་ལྟ་བུ་ཞིག་ཡོད། ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ལ་དམིགས་པ་གང་ཡིན་པའོ། །

[Block 1470]
དེ་ཡང་སྡུག་བསྔལ་ལ་ལོག་པར་ཞུགས་པ་ཡིན་ནོ། །

[Block 1471]
ཡང་གང་ལ་ལམ་ལ་དམིགས་པ་ལོག་པར་ལྟ་བའམ། ཐེ་ཚོམ་ཡོད་པ་དེ་ཐར་པའི་ལམ་མེད་དོ་ཞེས་ལྟ་བའམ། ཐེ་ཚོམ་ཟ་བ་ན༌[^1046]ཇི་ལྟར་དཔེ་དག༌[^1047]པར་ཡིད་ཆེས་པར་འགྱུར། འོན་ཏེ་ཐར་པའི་ལམ་གཞན་མཆོག་ཏུ་བཟུང་ནས་འདི་ནི་ཐར་པ་ཡིན་གྱི་ལམ་ནི་མེད་དོ་ཞེས་སྨྲའོ་ཞེ་ན། དེ་ཡང་གཞན་དེ་ཁོ་ནས་དག་པར་ཡིད་ཆེས་ཀྱི་ལོག་པར་ལྟ་བ་དེ༌[^1048]ནི་མ་ཡིན་པས་དེའི་དེ་ཡང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ལ་དམིགས་པར་མི་འགྲུབ་བོ། །

[Block 1472]
ཡང་གང་ཞིག་ཀུན་འབྱུང་དང་འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བ་ལ་དམིགས་པའི་ལོག་པར་ལྟ་བས་ཡང༌[^1049]དག་པར་ཡིད་ཆེས་པར་འགྱུར་བ་དེ་ཡང་། ཅིའི་ཕྱིར་དེ་དག་མཐོང་བས་སྤང་བར་བྱ་བ་མ་ཡིན། དེ་ལྟ་བས་ན་དོན་འདི་ནི་རྟག༌[^1050]པར་བྱ་བ༌[^1051]ཡིན་ནོ། །

[Block 1473 [HEADING]]
### ཕྱིན་ཅི་ལོག་བཞི། ^2-10-0

[Block 1474]
བདག༌[^1052]རྟག༌[^1053]ཕྱིན་ཅི་ལོག་པ་ཡིས། །ཞེས་གང་བཤད་པ། ཅི་ཕྱིན་ཅི་ལོག་དེ་གཉིས་ཁོ་ནར་ཟད་དམ་ཞེ་ན། ཕྱིན་ཅི་ལོག་ནི་བཞི་སྟེ། མི་རྟག་པ་ལ་རྟག་པ་དང་། སྡུག་བསྔལ་བ་ལ་བདེ་བ་དང་། མི་གཙང་བ་ལ་གཙང་བ་དང་། བདག་མེད་པ་ལ་བདག་ཏུ་ཕྱིན་ཅི་ལོག་པའོ། །

[Block 1475]
ཡང་ཕྱིན་ཅི་ལོག་བཞི་ཚན་འདིའི་རང་བཞིན་ཅི་ཞེ་ན། ལྟ་བ་གསུམ་ལས་ཕྱིན་ཅི་ལོག །བཞི་ཚན། མཐར་འཛིན་པར་ལྟ་བ་ལས་རྟག་པར་ལྟ་བ་ནི། རྟག་པར་ནི༌[^1054]ཕྱིན་ཅི་ལོག་གོ། །
--- END BLOCKS ---
