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
[Block 1611]
བློ་གྲོས་ཀྱིས་སོ་སོར་རྟོག་པའི༌[^1408]ཤེས་པ་ནི་ཤེས་རབ་ཀྱི་རང་བཞིན་གྱི་བློས་ཆོས་རྣམས་ལ་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པའོ། །

[Block 1612]
བདག་ལ་རྟོགས་པའི་ཤེས་པ་ནི་བདག་གི་ངོ་བོ་ཉིད་ཇི་ལྟ་བུ༌[^1409]ཡིན་པ་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པའོ། །

[Block 1613]
བདེན་པ་རྣམས་ལ་རབ་ཏུ་རྟོགས་པར༌[^1410]ཤེས་པ་ནི་འཕགས་པའི་བདེན་པ་བཞིའི་མཚན་ཉིད་མ་ནོར་བར་ཤེས་པའོ། །

[Block 1614]
དེ་དག་ཇི་ལྟར་མ་ནོར་བར་ཤེས་ཤེ་ན། དེའི་ཕྱིར་སྡུག་བསྔལ་ལ་མི་འབྱུང་བར་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སྡུག་བསྔལ་གྱི་ཕུང་པོ་ཉིད་ངོ་བོ་མེད་པས༌[^1411]མ་བྱུང་མ་སྐྱེས་པར་ཤེས་པའོ། །

[Block 1615]
ཀུན་འབྱུང་བ་ལ་མངོན་པར་འདུ་མི༌[^1412]བྱེད་པར་ཤེས་པ་ནི་ཀུན་འབྱུང་བའི་ངོ་བོ་ཉིད་མེད་པར་ཤེས་པས་སྡུག་བསྔལ་གྱི་ཕུང་པོ་སྐྱེད་པའི༌[^1413]བྱ་བ་མི་བྱེད་པར་ཤེས་པའོ། །

[Block 1616]
འགོག་པ་ལ་མཚན་ཉིད་མེད་པར་ཤེས་པ་ནི་རི་བོང་གི་རྭ་དང་མོ་གཤམ་གྱི་བུ་ལ་མཚན་ཉིད་མེད་པ༌[^1414]བཞིན་དུ་འགོག་པའི་རང་བཞིན་མྱ་ངན་ལས་འདས་པ་ཡང་དངོས་པོ་མ་ཡིན་པས་སྐྱེ་བ་དང་གནས་པ་ལ་སོགས་པའི་མཚན་ཉིད་མེད་པར་ཤེས་པའོ། །

[Block 1617]
ལམ་ལ་སྒྲོལ་བར་ཤེས་པ་ནི་འཁོར་བའི་རྒྱ་མཚོ་ལས་སྒྲོལ་བར་བྱེད་པ་ཡིན་པར་ཤེས་པའོ། །

[Block 1618]
ཆོས་རྣམས་ལ་ཚིག་རབ་ཏུ་དབྱེ་བ་ཤེས་པ་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་རྣམས་ཀྱི་དོན་སོ་སོར་འབྱེད་ཅིང་བཤད་པ་ལ་མཁས་པའོ། །

[Block 1619]
དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་ལ་དྲན་པ་མེད་པ་དང་། ཡིད་ལ་བྱེད་པ་མེད་པར་ཤེས་པ་ནི་ལུས་དང་ཚོར་བ་དང་སེམས་དང་ཆོས་རྣམས་དངོས་པོ་མེད་པས་དྲན་ཞིང་ཡིད་ལ་བྱར་མེད་པར་ཤེས་པའོ། །

[Block 1620]
དེ་ལ་འཕྲལ་དུ་ཡིད་ལ་མི་འཛིན་པ་ནི་དྲན་པ་ཤེས་པའོ། །

[Block 1621]
ཕྱིས་ཀྱང་ཡང་ནས་ཡང་དུ་ཡིད་ལ་མི་བྱེད་པ་ནི་ཡིད་ལ་བྱ་བ་མེད་པའོ། །

[Block 1622]
ཡང་དག་པའི་སྤོང་བ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་ཡང་དག་པའི་སྤོང་བ་རྣམ་པ་བཞི་སྟེ། དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་སྐྱེད་པ༌[^1415]དང་། སྐྱེས་པ་རྣམས་འཕེལ་བར་བྱ་བ་དང་སྡིག་པ་མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་མི་སྐྱེད་པ་དང་། སྐྱེས་པ་རྣམས་སྤང་བ༌[^1416]སྟེ། དེ་ལ་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་སྐྱེད་པ༌[^1417]དང་། སྐྱེས་པ་རྣམས་འཕེལ་བར་བྱ་བ་ནི་དགེ་བ་ལ་འཇུག་པའི་ཤེས་པའོ། །

[Block 1623]
སྡིག་པ་མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་མི་སྐྱེད་པ་དང་། སྐྱེས་པ་རྣམས་སྤོང་བ་ནི་མི་དགེ་བ་ལ་འཇུག་པའི་ཤེས་པ་ཞེས་བྱའོ། །

[Block 1624]
རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་འདུན་པ་དང་། བརྩོན་འགྲུས་དང་། སེམས་དང་། དཔྱོད་པ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་ནི་ལུས་དང་སེམས་ལས་སུ་རུང་བར་བྱེད་པ་ཡིན་པར་ཤེས་པའོ། །

[Block 1625]
དབང་པོ་རྣམས་ལ་འཇུག་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་དད་པ་ལ་སོགས་པའི་དབང་པོ་ལྔ་ནི་ཆོས་ཀྱི་དོན་མཐོང་ཞིང་རྟོགས་པར་བྱེད་པ་ཡིན་པར་ཤེས་པའོ། །

[Block 1626]
སྟོབས་ལ་མི་བརྫི་བར༌[^1418]ཤེས་པ་ཞེས་བྱ་བ་ནི་དད་པ་ལ་སོགས་པའི་སྟོབས་ལྔ་རྣམས་ལ་མ་དད་པ་ལ་སོགས་པས་མི་ཚུགས་པའི་རང་བཞིན་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1627]
བྱང་ཆུབ་ཀྱི་ཡན་ལག་རྣམས་ལ་ཆོས་ཐམས་ཅད་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རྟོག་པར༌[^1419]ཤེས་པ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན༌[^1420]རྣམས་ལ་ནི་དེ་དག་གི་ཆོས་ཐམས་ཅད་ཀུན་འགྲོ་བའི་མཚན་ཉིད་དུ་རྟོག་པར་བྱེད་པ་ཡིན་པར་ཤེས་པའོ། །

[Block 1628]
ལམ་ལ་འགྲོ་བ་དང་འོང་བ་མེད་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཡང་དག་པར་ན༌[^1421]ལམ་དང་ལམ་གྱི་འབྲས་བུ་དང་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་གཉིས་ཀྱང་མེད་པ་ཡིན་པས་འཕགས་པའི་ལམ༌[^1422]ཡན་ལག་བརྒྱད་ཀྱི༌[^1423]གང་དུ་ཡང་འགྲོ་བ་དང་འོང་བ་མེད་པར་ཤེས་པའོ། །

[Block 1629]
ཞི་གནས་ལ་གནས་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཞི་གནས་ཐམས་ཅད་ལ་སེམས་རྩེ་གཅིག་ཏུ་གནས་པའི་མཚན་ཉིད་ཡིན་པར་ཤེས་པའོ། །

[Block 1630]
ལྷག་མཐོང་ལ་སྣང་བར་ཤེས་པ་ཞེས་བྱ་བ་ནི་ལྷག་མཐོང་ཐམས་ཅད་ལ་ཆོས་ཀྱི་མཚན་ཉིད་རྟོག་པར༌[^1424]བྱེད་པའི་རང་བཞིན་ཡིན་པར་ཤེས་པའོ་སྒྱུ་མ་ལ་བསྒྲུབ་པ༌[^1425]ཡིན་པར་ཤེས་པ་ནི་སྒྱུ་མའི་གླང་པོ་དང་མི་ལ་སོགས་པ་ལ་སྨན་དང་སྔགས་ཀྱི་མཐུས་སྒྲུབ་པ༌[^1426]ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1631]
སྨིག་རྒྱུ་ལ་ནོར་བར་ཤེས་པ་ཞེས་བྱ་བ་ནི་སྨིག་རྒྱུ་རྣམས་ལ་ཆུ་མ་ཡིན་གྱི། ཆུ་ལྟ་བུར་འཁྲུལ་པར་སྣང་བ་ཡིན་པར༌[^1427]ཤེས་པའོ།[^1428] །རྨི་ལམ་ལ་ཡང་དག་པ་མ་ཡིན་པ་མཐོང་བར་ཤེས་པ་ཞེས་བྱ་བ་ནི་རྨི་ལམ་ན་སྣང་བའི་ཆོས་ཐམས་ཅད་མེད་བཞིན་དུ་མཐོང་བར་ཤེས་པའོ། །

[Block 1632]
བྲག་ཅ་ལ་རྐྱེན་བཞིན་དུ༌[^1429]དམིགས་པའི་ཤེས་པ་ཞེས་བྱ་བ་ནི་བྲག་ཅའི་སྒྲ་ཐམས་ཅད་སྒྲ་གཞན་གྱི༌[^1430]རྐྱེན་ལས་བྱུང་བར་ཤེས་པའོ། །

[Block 1633]
མིག་ཡོར་ལ་མི་འཕོ་བར་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཁང་པའི་ནང་གི་ཉི་ཟེར་གྱི་འོད་ལས་གཟུགས་དུ་མར་སྣང་བ་སྣང་ཡང་ཆུས་འཕོས༌[^1431]པ་མེད་པར་ཤེས་པའོ། །

[Block 1634]
མཚན་ཉིད་ཐ་དད་པ་རྣམས་ལ་མཚན་ཉིད་གཅིག་ཏུ་ཤེས་པ་ནི་མཚན་ཉིད་ཀྱི་བདེན་པའི་སྐབས་སུ་བཤད་པ་བཞིན་དུ་ཤེས་པ་ལ་བྱའོ། །

[Block 1635]
འདུ་བ་རྣམས་ལ་འབྲལ་བར་ཤེས་པ་ཞེས་བྱ་བ་ནི་འདུས་ཤིང་ཚོགས་པའི་དངོས་པོ་ཐམས་ཅད་མཐར་བྱེ་ཞིང་བྲལ་བར༌[^1432]འགྱུར་བར༌[^1433]ཤེས་པའོ། །

[Block 1636]
མཚམས་སྦྱོར་བ་ལ་མཚམས་སྦྱོར་བ་མེད་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ། ཚེ་གཅིག་ནས་གཅིག་ཏུ་ཉིང་མཚམས་སྦྱོར་བ་ནི་མཚམས་སྦྱོར་བའོ། །

[Block 1637]
དོན་དམ་པར་ན་ཆོས་གང་ཡང་སྐྱེ་ཞིང་མཚམས་སྦྱོར་བ་མེད་པར་ཤེས་པ་ནི་ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་གཞན་གྱི་སྒྲའི་རྗེས་སུ་འགྲོ་བས་འཇུག་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་ཀྱི་ཐེག་པ་ཐམས་ཅད་ལ་འདི་འདྲ་བར་ཤེས་ཏེ། མཁན་པོ་དང་སློབ་དཔོན་གྱིས་བཤད་པའི་སྒྲ་ལ་བརྟེན་ནས་གང་ཟག་ལ་བདག་མེད་པར་དམིགས་པར་བྱེད་པར་ཤེས་པའོ། །

[Block 1638]
[^1434]སངས་རྒྱས་ཀྱི་ཐེག་པ་ལ་ཞེས་བྱ་བ་ནི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་ལ་ནི་ཆོས་ཐམས་ཅད་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་མཚན་ཉིད་དུ་ཁོང་དུ་ཆུད་པར་བྱེད་པ་དང་། ལུས་དབེན་པར་གནས་པ་དང་། སེམས་དབེན་པར་གནས་པ་ཡིན་པར་ཤེས་པའོ། །

[Block 1639]
ཐེག་པ་ཆེན་པོ་ལ་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོ་ལ་ནི་ཐེག་པ༌[^1435]དེ་འདོད་མ་ཆགས་པ་ལ་སོགས་པའི་དགེ་བའི་རྩ་བ་ཐམས་ཅད་སོགས་པར་བྱེད་པ་དང་། བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཐམས་ཅད་སོགས་པར་བྱེད་པ་ཡིན་པའོ། །

[Block 1640]
དོན་སོ་སོ༌[^1436]ཡང་དག་པར༌[^1437]རིག་པའི་རྣམ་གྲངས་གཞན་ཡང་བསྟན་པའི་ཕྱིར།[^1438] གཞན་ཡང་དོན་སོ་སོ༌[^1439]ཡང་དག་པར་རིག་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1641]
དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་གང་གིས་ཞེས་བྱ་བ་ནི་དོན་སོ་སོ༌[^1440]ཡང་དག་པར༌[^1441]རིག་པའི་རིག་པ་གང་གིས་ཤེའམ། [^1442]དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་གང་གིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1642]
ཆོས་ཐམས་ཅད་ལ་དོན་ལ་རྟོན་པས༌[^1443]ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་དོན་གང་ཡིན་པའི་དོན་དེ་ལ་རྟོན། དོན་དེ་ཁོང་དུ་ཆུད་པར་བྱེད་པའི་དོན་ཏོ། །

[Block 1643]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་ཆོས་ཐམས་ཅད་ཀྱི་དོན་ལ་རྟོན་ཅེ་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1644]
དེ་ནི༌[^1444]ཞེས་བྱ་བ་ནི་སྟོང་པ་སྟེ། གཞན་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 1645]
མི་སྐྱེ་བ་ནི་མ་འོངས་པའི་དུས་སུ་མི་སྐྱེའོ།[^1445] །མ་བྱུང་བ་ནི་འདས་པའི་དུས་སུ༌[^1446]མ་སྐྱེས་པའོ། །

[Block 1646]
དངོས་པོ་མེད་པ་ནི་ད་ལྟར་གྱི་དུས་ན་ཡང་རང་བཞིན་མེད་པའོ། །

[Block 1647]
མ་ལུས་པར་དབེན་པ་ནི་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཡིན་པའི་ཕྱིར་ཏེ། འདི་ཡན་ཆད་ཀྱི༌[^1447]ཆོས་ཐམས་ཅད་ལ་བདག་མེད་པ་དེ་དོན་ཡིན་པར་བསྟན་ཏོ། །

[Block 1648]
ཆོས་ཐམས་ཅད་ནི་མ་ལུས་པར་བདག་མེད་ཅེས་བྱ་བ་མན་ཆད་ཀྱིས་གང་ཟག་ལ་བདག་མེད་པ་དོན་ཡིན་པར་སྟོན་ཏོ། །

[Block 1649]
གང་འདི་ལྟ་བུའི་ཆོས་རྟོགས་པ༌[^1448]ཞེས་བྱ་བ་ནི་གང་གོང་དུ་བསྟན་པ་ལྟ་བུར་ཆོས༌[^1449]ཐམས་ཅད་རྟོགས་པའོ། །

[Block 1650]
དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་རྒྱས་པར་བཤད་པ་རྣམས་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། གང་འདིར་བསྟན་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། མདོ་སྡེ་འདི་ལ་དོན༌[^1450]སོ་སོ་ཡང་དག་པར་རིག་པ་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་དུ་བཤད་པ་དེ་དངོས་པོ་དང་མཚན་མ་ཐམས་ཅད་ལས་འདས་པའི་ཕྱིར་ཐོགས་པ་མེད་པར༌[^1451]བསྟན་པ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
