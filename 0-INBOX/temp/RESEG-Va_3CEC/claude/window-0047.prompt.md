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

[Block 1651]
ཡང་ན་ཆོས་ཐམས་ཅད་སྟོང་པའི་དོན་དུ་བསྟན་པས་ན་ཐོགས་པ་མེད་པར་བསྟན་པའོ། །

[Block 1652]
ཐམས་ཅད་སྒྲིབ་པ་གཉིས་ལས་འདས་པའི་མཚན་ཉིད་དུ་སྟོན་པས་ན་ཆགས་པ་མེད་པར་བསྟན་པའོ། །

[Block 1653]
དུས་གསུམ་དུ་ཡང་སྐྱེ་བ་དང་འགག་པ་མེད་པར་སྟོན་པས་ན་མི་ཟད་པར་བསྟན་པའོ། །

[Block 1654]
ཆོས་ཐམས་ཅད་མྱ་ངན་ལས་འདས་པའི་མཚན་ཉིད་དུ་སྟོན་པས་ན༌[^1452]ཆོས་ཐམས་ཅད་ཐོབ་པར་བསྟན་པ་ཞེས་བྱའོ། །

[Block 1655]
དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་དེ་ནི་ཆོས་བསྟན་པ་ལ་མི་ཟད་པ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་བསྟན་པ་དེ་ལ་བསྟན་པ་མཐའ་ཡས་ཏེ། ཟད་མི་ཤེས་པས་ན། དོན་ཐམས་ཅད་བསྟན་པ་ལ་མི་ཟད་པ་ཞེས་བྱའོ། །

[Block 1656]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས་ཀྱང༌[^1453]ཡང་དག་པར་བཀའ་སྩལ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱང་དེ་སྐད་དུ་འཆད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1657]
ཡང་དག་པར་རྗེས་སུ་ཐུགས་རང་བ་ཞེས་བྱ་བ་ནི་གཞན་དེ་ལྟར་འཆད་པ་རྣམས་ལ་ཡང་ཐུགས་དགྱེས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་ལྟར་སྟོན་པའི་དོན་ཏེ།[^1454] ཡང་དག་པ་དང་དེ་ཁོ་ན༌[^1455]དང་། མ་ལོག་པ་དང་གཞན་མ་ཡིན་པའི་ཕྱིར་རོ། །ཇི་ལྟར་ཕྱིན་ཅི་མ་ལོག་ཅེ་ན། ཤེས་རབ་དང་ཡེ་ཤེས་ཀྱི་རྟོག་པ༌[^1456]ཡིན་ལ། ཐམས་ཅད་དུ་ཁ་ན་མ་ཐོ་བ་མེད་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1658 [HEADING]]
### འདུ་ཤེས་ཤེས་པ། ^5-2-0

[Block 1659]
འདུ་ཤེས་ཤེས༌[^1457]པ་བསྟན་པའི་ཕྱིར། དེ་ལ༌[^1458]ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་གསུངས་ཏེ། འདིར་ཡང་ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པ་མི་ཟད་པ་གང་ཞེ་ན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1660]
དེ་ཡང་སོ་སོ་ཡང་དག་པར་རིག་པར་བྱ་བའི་ཆོས་རྣམས་མི་ཟད་པས་ན་མི་ཟད་པའོ། །

[Block 1661]
འདིར་དོན་དང་ཆོས་ཉིད་བྱེ་བྲག་མེད་པར༌[^1459]འདྲ་མོད་ཀྱི་དོན་ནི་བསྟན་ཅིང་རྟོགས་པའི་ཡུལ་ལྟ་བུར་རིག་པར་བྱའོ། །

[Block 1662]
ཆོས་ནི་སྟོན་ཅིང་རྟོག་པར༌[^1460]བྱེད་པ་ལྟ་བུར་རིག་པར་བྱའོ། །

[Block 1663]
ཡང་ན་ཆོས་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་སོགས་པའི་མིང་གིས་འོག་ནས་སྨོས་པ་རྣམས་ལ་བྱའོ། །

[Block 1664]
དོན་ནི་དེ་ཉིད་ཀྱི་དོན་ཡོངས་སུ་དཔྱོད༌[^1461]ཅིང་བྱེ་བྲག་ཏུ་དབྱེ་བ་ལ་བྱའོ། །

[Block 1665]
ཡང་ན་ཆོས་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པ་ནི་དོན་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 1666]
ཆོས་དེ་དང་དེ་དག་གི་མིང་གང་དང་གང་ཡིན་པ་ཤེས་པ་ནི་ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 1667]
གང་ཆོས་ཐམས་ཅད་ལ་རྗེས་སུ་འཇུག་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་དགེ་བ་དང་མི་དགེ་བ་ལ་སོགས་པའི་ཆོས་མིང་གིས་སྨོས་པ་རྣམས་དོན་དང་མཐུན་པར་ཡང་དག་པར་ཤེས་པ་ལ་བྱའོ། །

[Block 1668]
ཆོས་དེ་དག་གང་ཞེ་ན། དགེ་བ༌[^1462]དང་མི་དགེ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 1669]
ཡང་ན་དགེ་བ་དང་མི་དགེ་བ་ལ་སོགས་པ་སྨོས་པའི་ཆོས་རྣམས་སོ་སོའི་མིང་གང་ཡིན་པ་དང་། དོན་གང་ཤེས་པ་ནི་ཆོས་ཐམས་ཅད་ལ་རྗེས་སུ་ཞུགས་པ་ཤེས་པ་ཞེས་བྱའོ། །

[Block 1670]
ཉེ་བར་སོང་བ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་དེ་དག་གི་རང་བཞིན་ནི༌[^1463]གྱུར་པའམ། དེ་དག་གི་ཆར་རྟོགས་པ༌[^1464]རྣམས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1671]
ཆོས་ཀྱི་དབྱིངས་མཉམ་པ་ཉིད་དུ་ཤེས་པ་ཞེས་བྱ་བ༌[^1465]ནི་དགེ་བ་དང་མི་དགེ་བའི་ཆོས་རྣམ་པ་སྣ་ཚོགས་པ༌[^1466]རྣམས་ཆོས་ཀྱི་དབྱིངས་སྟོང་པ་ཉིད་དུ་རེ་གཅིག་པའོ། །

[Block 1672]
བྱང་ཆུབ་མཉམ་པ་ཉིད་དུ་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་དབྱིངས་རྟོགས་པའི་ཡེ་ཤེས་རྣམ་པར་མི་རྟོགས་པ༌[^1467]དང་ཐ་མི་དད་པར་ཤེས་པའོ། །

[Block 1673]
ཁམས་མཉམ་པ་ཉིད་དུ་ཤེས་པ་ཞེས་བྱ་བ་ནི་མིག་གི༌[^1468]ཁམས་ལ་སོགས་པ་ཁམས་ཀྱི་སྐབས་སུ་བསྟན་པ་ལྟར་ཆོས་ཀྱི་དབྱིངས་སུ་མཉམ་པ་ཉིད་དུ་ཤེས་པའོ། །

[Block 1674]
ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པ་རྣམ་གྲངས་གཞན་བསྟན་པའི་ཕྱིར། །གཞན་ཡང་ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1675]
གང་འདོད་ཆགས་སྤྱོད་པའི་སེམས་ཅན་རྣམས་ཀྱི༌[^1469]སེམས་ལ་འཇུག་ཅིང་འབབ་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་རང་བཞིན་གྱིས༌[^1470]འདོད་ཆགས་ཅན་རྣམས་ཀྱི༌[^1471]སེམས་ལ་འདོད་ཆགས་ཅན་ཡིན་པར་ཤེས་པའོ། །

[Block 1676]
ཡང་ན་སེམས་ཅན་འདོད་ཆགས་ལ་སྤྱོད་པ༌[^1472]རྣམས་འདོད་ཆགས་སྐྱེ་བའི་ཡུལ་གང་དང་གང་ལ་དམིགས་པའི༌[^1473]འདོད་ཆགས་སྐྱེས་པར་གྱུར་པ་ན་ཡུལ་འདི་དང་འདི་ལ་དམིགས་ནས་འདོད་ཆགས་སྐྱེས་སོ་ཞེས་ཤེས༌[^1474]པ་ནི་འདོད་ཆགས་སྤྱོད་པའི་སེམས་ཅན་གྱི་སེམས་ལ་འཇུག་ཅིང་འབབ་པར་ཤེས་པ་ཞེས་བྱའོ། །

[Block 1677]
འདོད་ཆགས་སྤྱོད་པ་གང་ཡིན་དུ་ཞིག་ཡོད་ཅེ་ན། བཅོས་མའི་འདོད་ཆགས་སྤྱོད་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་ནི་ཉི་ཁྲི་ཆིག་སྟོང་ཡོད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1678]
བཅོས་མའི་འདོད་ཆགས་སྤྱོད་པ་ནི་རང་བཞིན་གྱིས་འདོད་ཆགས་ཤས་ཆེ་བ་མ་ཡིན་ཡང་གཞན་གྱི༌[^1475]སེམས་དང་སྦྱོར༌[^1476]ཞིང་ཕ་རོལ་གྱི་ངོར་འདོད་ཆགས་ཆེ་བ་ལྟ་བུར་སྟོན་པའོ། །

[Block 1679]
དེ་ལས་བཟློག༌[^1477]ནས་བཅོས་མ་མ་ཡིན་པའི་འདོད་ཆགས་སྤྱོད་པ་སྟེ། རང་བཞིན་གྱིས་འདོད་ཆགས་དང་ལྡན་པའོ། །

[Block 1680]
སྣྲེལ་ཞིའི༌[^1478]འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་ཞེ་སྡང་གི་རང་བཞིན་ཅན་ལ་འདོད་ཆགས་སྤྱོད་པ་དང་འདྲ་བར་སྣང་བའམ། འདོད་ཆགས་ཀྱི་ཤས་ཆེ༌[^1479]ལ་ཆུང་བར༌[^1480]འདྲ་བར་སྣང་བའམ། འདོད་ཆགས་ཀྱི་ཤས་ཆུང་བ་ལ༌[^1481]ཆེ་བར་སྣང་བའོ། །

[Block 1681]
ལྟ་བའི་འདོད་ཆགས་སྤྱོད་པ་ནི་ལྟ་བ་རྣམ་པ་སྣ་ཚོགས་ལ་ཆགས་པའོ། །

[Block 1682]
མི་བཟོད་པའི༌[^1482]འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ཀྱི་ཤས་ཆེ་བས་དེའི་རྐྱེན་གྱིས༌[^1483]སེམས་ཀྱང་འཁྲུགས་ཤིང༌[^1484]ལུས་ཀྱི་སྤྱོད་པ་རྣམས་ཀྱང་གྱུར་པར་སྣང་བའོ། །

[Block 1683]
འཇམ་པའི་འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ཤས་ཆུང་བས༌[^1485]དེའི་རྐྱེན་གྱིས་ལུས་དང་སེམས་འཁྲུག་པ་མེད་པའི་འདོད་ཆགས་ཅན་ནོ། །

[Block 1684]
ཡང་བའི་འདོད་ཆགས་སྤྱོད་པ་ནི་དེ་བས་ཀྱང་འདོད་ཆགས་ཤས་ཆུང་བས་འདོད་ཆགས་སྤངས་པར་སླ་བ་རྣམས་སོ། །

[Block 1685]
ཀུན་རྫོབ་ཀྱི་འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་ཀྱི་ཐ་སྙད་མང་པོ་ལ་ཆགས་པ་རྣམས་སོ། །
--- END BLOCKS ---
