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
ཅེས་བྱ་བ་སྨོས་ཏེ། དགེ་བའི་རྩ་བ་ཡང་དག་པར་ཆད་པ་དང་། དེའི་ཉིང་མཚམས་སྦྱོར་བ་དང་། ཁམས་དང་ས་ལས༌[^537]འདོད་ཆགས་དང་བྲལ་བ་དང་། ཡོངས་སུ་ཉམས་པ་དང་། འཆི་འཕོ་བ་དང་། སྐྱེ་བ་དང་། ཆོས་དྲུག་པོ་འདི་དག་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཁོ་ན་ཡིན་པར་འདོད་དོ། །

[Block 1437]
ཚོར་བ་ལས་ཀྱང་། འཆི་འཕོ་སྐྱེ་བ་བཏང་སྙོམས་ལ། །འཆི་འཕོ་བ་དང་སྐྱེ་བ་ནི་བཏང་སྙོམས་ལས་འབྱུང༌[^538]ངོ་། །ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དེ་ལ་ཡང་། རྩེ་གཅིག་སེམས་མེད་དེ་ལ་མེད། །སྐལ་བ་མི་མཉམ་པའི་ས་པ་ཡིན་པའི་ཕྱིར་དང་། མངོན་པར་འདུ་བྱེད་པ་ལས་བྱུང་བ་ཉིད་ཡིན་པའི་ཕྱིར་སེམས་རྩེ་གཅིག་པ་ལ་འཆི་འཕོ་བའམ་སྐྱེ་བ་མེད་དོ། །

[Block 1438]
སེམས་མེད་པ་ལ་ཡང་མེད་དེ། སེམས་མེད་པ་ལ་གནོད་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1439]
འཆི་བའི་སྲིད་པ་རྣམ་པ་གསུམ་དུ་བཤད་པ་ལ༌[^539]དགྲ་བཅོམ་པ་ནི། མྱ་ངན་འདས་ལུང་བསྟན་མིན་གཉིས། །སྤྱོད་ལམ་པའམ། རྣམ་པར་སྨིན་པའི་སེམས་ལས་ཏེ། །སེམས་འཆད་པའི་རྗེས་སུ་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1440]
ཡང་འཆི་བ་ན་ལུས་ཀྱི་ཕྱོགས་གང་དུ་རྣམ་པར་ཤེས་པ་འགག་ཅེ་ན། ཅིག་ཅར་འཆི་ན་ནི་ཡིད་དང་བཅས་པའི་ལུས་ཀྱི་དབང་པོ་མོད་ལ་འགག་པར་འགྱུར་རོ། །

[Block 1441]
གལ་ཏེ་རིམ་གྱིས་འཆི་འཕོ་ན་ནི་དེའི་ཚེ།

[Block 1442 [VERSE]]
འོག་མིན༌[^540]ལྷར་འགྲོ་མི་སྐྱེ་རྣམས། །
རིམ་གྱིས་འཆི་ན་རྐང་པ་དང་། །
ལྟེ་བ་སྙིང་གར་ཡིད་འཆི་འཕོ། །

[Block 1443]
ངན་སོང་དུ༌[^541]འགྲོ་བ་རྣམས་ཀྱི་ཡིད་ནི་རྐང་པ་དག་ནས་འཆི་འཕོའོ། །

[Block 1444]
མིར་འགྲོ་བ་དག་ནི་ལྟེ་བ་ནས་སོ། །

[Block 1445]
ལྷར་འགྲོ་བ་རྣམས་ནི་སྙིང་གར་རོ། །

[Block 1446]
མི་སྐྱེ་བ་ནི་དགྲ་བཅོམ་པ་དག་སྟེ། དེ་དག་གི་ཡང་ཐུགས་ཀར་རོ། །

[Block 1447]
ཁ་ཅིག་ནི་དབུ་ནས་ཞེས་སོ། །

[Block 1448]
གནད་གཅོད་པའི་ཚོར་བས་ཉེན་དེ་པེའི༌[^542]སྲོག་ཆགས་རྣམས་ནི་དེ་ལྟར་རིམ་གྱིས་འཆི་བར་འགྱུར་རོ། །

[Block 1449]
གནད་གཅོད་པ་ནི་ཆུ་སོགས་ཀྱིས། །དེ་ལྟར་འཆི་བ་ན་ཆུ་དང་མེ་དང་། རླུང་གི་ཁམས་རྣམས་བད་ཀན་དང་། མཁྲིས་པ་དང་། རླུང་གི་རང་བཞིན་དག་གི་ཚོར་བ་མི་ཟད་པ་དག་གིས་གནད་གཅོད་པར་འགྱུར་རོ། །

[Block 1450 [HEADING]]
#### ཚོགས་པ་གསུམ། ^3-1-10-0

[Block 1451]
སེམས་ཅན་གྱི་འཇིག་རྟེན་གྱི་ཚོགས་པ་གསུམ་དུ༌[^543]རྣམ་པར་གཞག་སྟེ། དེ་ལ།

[Block 1452 [VERSE]]
འཕགས་དང་མཚམས་མེད་བྱེད་པ་དག །
ཡང་དག་ལོག་པ་ཉིད་དུ་ངེས། །

[Block 1453]
གང་དག་ལ་ཟག་པ་མེད་པའི་ལམ་སྐྱེས་པ་དེ་དག་འཕགས་པ་རྣམས་ཏེ། དེ་དག་མྱ་ངན་ལས་འདས་པར་ངེས་པའི་ཕྱིར་ཡང་དག་པར་ངེས་པའི་ཚོགས་པ་ལའོ། །

[Block 1454]
གང་མཚམས་མེད་པ་བྱེད་པ་དེ་དག་ངན་སོང་དུ་ངེས་པའི་ཕྱིར་ལོག་པར་ངེས་པའི་ཚོགས་པ་ལའོ། །

[Block 1455]
གཞན་དག་ནི་མ་ངེས་པའི་ཚོགས་པ་ལའོ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 1456 [HEADING]]
### སྣོད་ཀྱི་འཇིག་རྟེན། ^3-2-0

[Block 1457]
སེམས་ཅན་གྱི་འཇིག་རྟེན་བཤད༌[^544]ཟིན་ནས། སྣོད་ཀྱི་འཇིག་རྟེན་བཤད་པར་བྱ༌[^545]སྟེ།

[Block 1458 [HEADING]]
#### རླུང་དང་ཆུ་དང་གསེར་གྱི་དཀྱིལ་འཁོར། ^3-2-1-0

[Block 1459 [VERSE]]
དེ་ལ་སྣོད་ཀྱི་འཇིག་རྟེན་གྱི། །
གནས་པར་འདོད་པའི་འོག་དག་གི། །
རླུང་གི་དཀྱིལ་འཁོར་རྔམས་སུ་ནི། །
ས་ཡ་དྲུག་འབུམ་གྲངས་མེད་དོ། །

[Block 1460]
འོག་ནས་ནམ་མཁའ་ལ་བརྟེན་པའི༌[^546]རླུང་གི་དཀྱིལ་འཁོར་ཏེ། དེའི་རྔམས་སུ་དཔག་ཚད་ས་ཡ་དྲུག་འབུམ་མོ། །

[Block 1461]
རྒྱར་ནི་གྲངས་མེད་དོ། །

[Block 1462]
དེའི་སྟེང་ན།

[Block 1463 [VERSE]]
ཆུ་རྔམས་འབུམ་ཕྲག་བཅུ་གཅིག་དང་། །
སྟོང་ཕྲག་དག་ནི་ཉི་ཤུའོ། །

[Block 1464]
རླུང་གི་དཀྱིལ་འཁོར་དེར༌[^547]སེམས་ཅན་རྣམས་ཀྱི་ལས་དག་གིས་སྤྲིན་རྣམས་འདུས་ནས་ཆར་གྱི་རྒྱུན་གཉའ་ཤིང་ཙམ་བབ་པ་དེ༌[^548]ཆུའི་དཀྱིལ་འཁོར་དུ་འགྱུར་ཏེ། དེའི་རྔམས་སུ༌[^549]ནི་དཔག་ཚད་འབུམ་ཕྲག་བཅུ་གཅིག་དང་ཉི་ཁྲིའོ། །

[Block 1465]
ཆུ་དེ་དག་ཀྱང་སེམས་ཅན་རྣམས་ཀྱི་ལས་ཀྱི་མཐུ་ལས་བྱུང་བའི་རླུང་དག་གིས་མངོན་པར་དཀྲུགས་པ་ན་སྟེང་མ་གསེར་དུ་འགྱུར་རོ། །

[Block 1466]
ཆུའི་དཀྱིལ་འཁོར་དེའི།

[Block 1467 [VERSE]]
ཕྱིས་ནི་རྔམས་སུ་འབུམ་ཕྲག་བརྒྱད། །
ལྷག་མ་དག་ནི༌[^550]གསེར་དུ་གྱུར།[^551] །
ལྷག་མ་གང་ཞིག་ཅེ་ན།
འབུམ་ཕྲག་གསུམ་དང་ཉི་ཁྲིའོ། །

[Block 1468]
ཆུ་དང་གསེར་གྱི་དཀྱིལ་འཁོར་གྱི་རྔམས་བཤད་ཟིན་ཏོ། །

[Block 1469 [VERSE]]
ཆུ་དང་གསེར་གྱི་དཀྱིལ་འཁོར་གྱི། །
ཐད་ཀར་འབུམ་ཕྲག་བཅུ་གཉིས་དང་། །
སྟོང་ཕྲག་གསུམ་དང་བརྒྱ་ཕྲག་ནི། །
ཕྱེད་དང་ལྔ༌[^552]རྣམས་ཁོ་ནའོ། །

[Block 1470]
འདི་གཉིས་ཀ་རྒྱར་མཉམ་མོ། །

[Block 1471]
ཁོར་ཡུག་ཏུ་ནི་སུམ་འགྱུར་རོ།[^553] །

[Block 1472]
ཁོ་ར་ཁོར་ཡུག་ཏུ་བརྩི་བ༌[^554]ནི་སུམ་འགྱུར་རོ། །

[Block 1473 [HEADING]]
#### རི་ཆེན་པོ་བརྒྱད། ^3-2-2-0

[Block 1474 [VERSE]]
དེ་ལ་ལྷུན་པོ་གཉའ་ཤིང་འཛིན། །
གཤོལ་མདའ་འཛིན་དང་སེང་ལྡེང་ཅན། །
དེ་བཞིན་བལྟ་ན་སྡུག་རི་དང་། །
རྟ་རྣ་དང་ནི་རྣམ་འདུད་དང་། །
མུ་ཁྱུད་འཛིན་རིའོ། །

[Block 1475]
འདི་ལྟར་རི་ཆེན་པོ་བརྒྱད༌[^555]ནི་གསེར་གྱི་དཀྱིལ་འཁོར་ལ་བརྟེན་པ་ཡིན་ཏེ། རི་རབ་ནི་དབུས་ནའོ། །
--- END BLOCKS ---
