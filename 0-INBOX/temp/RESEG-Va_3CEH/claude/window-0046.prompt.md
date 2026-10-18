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
[Block 1611 [HEADING]]
#### རྣམ་པར་མི་རྟོག་པ། ^8-18-2-0

[Block 1612 [HEADING]]
##### ཆོག་ཤེས་པས་རྣམ་པར་མི་རྟོག་པ། ^8-18-2-1-0

[Block 1613]
ཆོག་ཤེས་པ་དང་། ཕྱིན་ཅི་མ་ལོག་པ་དང་། སྤྲོས་པ་མེད་པས་རྣམ་པར་མི་རྟོག་པའི་ཕྱིར་རོ༌[^977]ཞེས་བྱ་བ་ལ། དེ་ལ་ཆོག་ཤེས་པས་རྣམ་པར་མི་རྟོག་པ་ནི་ཐོས་པ་དང་བསམས་པ་ལས་བྱུང་བའི་མཐར་ཕྱིན་པ་ཡིན་པར་བལྟ་བར་བྱ་སྟེ། ཆོག་ཤེས་པ་ལས༌[^978]རྣམ་པར་མི་རྟོག་པ་ནི་ཆོག་ཤེས་པས་རྣམ་པར་མི་རྟོག་པའོ་ཞེས་དེ་ལྟར་བྱས་ནས་ཐོས་པའམ་བསམས་པ་གང་གིས་བློ་གང་གི་མཐར་ཕྱིན་པར་གྱུར་པ་དེ་ནི་སོ་སོའི་སྐྱེ་བོའི་ས་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའི་ཆོག་ཤེས་པ་འབྱུང་བར་འགྱུར་བ་སྟེ། དེ་ནི་རེ་ཞིག་འདི་ཙམ་མོ་ཞེས་དེ་ལྟར་བྱས་པའི་དོན་འདིས་ཆོག་ཤེས་པའི་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 1614]
དོན་གཞན་ཡང་འཇིག་རྟེན་པའི་ཆོག་ཤེས་པའི་རྣམ་པར་མི་རྟོག་པར་བལྟ་བར་བྱ་སྟེ། གང་སྲིད་པའི་རྩེ་མོར་ཕྱིན་པར་གྱུར་པ་དེ་ནི་མྱ་ངན་ལས་འདའ་བར་བལྟ་བས་དེའི་ཕ་རོལ་ན་རྟོགས་པར་བྱ་བ་གཞན་མེད་དོ་ཞེས་ཆོག་ཤེས་པ་འབྱུང་བར༌[^979]འགྱུར་བའོ། །

[Block 1615 [HEADING]]
##### ཕྱིན་ཅི་མ་ལོག་པས་རྣམ་པར་མི་རྟོག་པ། ^8-18-2-2-0

[Block 1616]
ཕྱིན་ཅི་མ་ལོག་པའི་རྣམ་པར་རྟོག་པ་ནི་ཉན་ཐོས་ལ་སོགས་པ་རྣམས་ཀྱི་ཡིན་པར་བལྟ་བར་བྱ་སྟེ། གང་གི་ཕྱིར་དེ་དག་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་རབ་ཏུ་རྟོགས་པའི་ཡེ་ཤེས་དེ་ནི་མི་རྟག་པ་ལ་སོགས་པའི་ཕྱིན་ཅི་མ༌[^980]ལོག་པ་རྣམ་པ་བཞི༌[^981]ལས་དེ་རྟག་པ་ལ་སོགས་པའི་རྣམ་པ་ཕྱིན་ཅི་ལོག་ཏུ་རྣམ་པར་མི་རྟོག་པའི་ཕྱིར་རོ། །

[Block 1617 [HEADING]]
##### སྤྲོས་པ་མེད་པས་རྣམ་པར་མི་རྟོག་པ། ^8-18-2-3-0

[Block 1618]
ཡང་སྤྲོས་པ་མེད་པས་རྣམ་པར་མི་རྟོག་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཡིན་པར་བལྟ་བར་བྱ་སྟེ། གང་གི་ཕྱིར་ཆོས་ཐམས་ཅད་ནས་བྱང་ཆུབ་ཀྱི་བར་ལ༌[^982]ཡང་སྤྲོས་པ་མེད་པར་རྣམ་པར་མི་རྟོག་པ་ཉིད་ཀྱི་ཕྱིར་རྣམ་པར་རྟོག་པར་མི་བྱེད་དོ། །

[Block 1619]
ཡང་སྤྲོས་པ་མེད་པ་ནི་ངག༌[^983]གི་ཡུལ་ལས་ཡང་དག་པར་འདས་པ་དང་། འཇིག་རྟེན་པའི་ཤེས་པའི་ཡུལ་ལས་ཡང་དག་པར་འདས་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། གང་གི་ཕྱིར་ཚིག་གིས་བསྟན་པར་མི་ནུས་པ་དང་། འཇིག་རྟེན་པའི་ཤེས་པས་ཤེས་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1620 [HEADING]]
#### རྣམ་པར་མི་རྟོག་པའི་རྗེས་ལས་ཐོབ་པ། ^8-18-3-0

[Block 1621]
ཡང་རྣམ་པར་མི་རྟོག་པའི་རྗེས་ལས་ཐོབ་པ་དེ་ཡང་རབ་ཏུ་དབྱེ་བ་རྣམ་པ་ལྔར་བལྟ་བར་བྱ་བ་ཡིན་པས་རྟོགས་པ་དང་། རྗེས་སུ་དྲན་པ་དང་། རྣམ་པར་གཞག་པ་དང་། འདྲེས་པ་དང་། འབྱོར་པ་ལ་དཔྱོད་པ་ཐ་དད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ། དེ་ཡང་རྟོགས་པ༌[^984]ལ་དཔྱོད་པ༌[^985]དང་། རྗེས་སུ་དྲན་པ་ལ་དཔྱོད་པ་དང་། རྣམ་པར་གཞག་པ་ལ་དཔྱོད་པ་དང་། འདྲེས་པ་ལ་དཔྱོད་པ་དང་། འབྱོར་པ་ལ་དཔྱོད་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་དབྱེ་བ་རྣམ་པ་ལྔ་ཡིན་ནོ། །

[Block 1622 [HEADING]]
##### རྟོགས་པ་ལ་དཔྱོད་པ། ^8-18-3-1-0

[Block 1623]
དེ་ལ་རྟོགས་པ་ལ་དཔྱོད་པ་ནི། གང་རྟོགས་པའི༌[^986]དུས་ཉིད་ན་བདག་གིས་འདི་ལྟར་རྟོགས་སོ་ཞེས་དཔྱོད་པ་སྟེ། ཁོང་དུ་ཆུད་པ་ནི་འདིར་དཔྱོད་པ་ཡིན་པར་འདོད་དོ། །

[Block 1624 [HEADING]]
##### རྗེས་སུ་དྲན་པ་ལ་དཔྱོད་པ། ^8-18-3-2-0

[Block 1625]
རྗེས་སུ་དྲན་པ་ལ་དཔྱོད་པ་ནི་གང་ལངས་པ་ན་བདག་གིས་རྣམ་པར་མི་རྟོག་པ་རྟོགས་སོ་ཞེས་དྲན་པའོ། །

[Block 1626 [HEADING]]
##### རྣམ་པར་གཞག་པ་ལ་དཔྱོད་པ། ^8-18-3-3-0

[Block 1627]
རྣམ་པར་གཞག་པ་ལ་དཔྱོད་པ་ནི་གང་ཕ་རོལ་ལ་བདག་གིས་རྟོགས་པ་དེ་སྟོན་པར་བྱེད་པའོ། །

[Block 1628 [HEADING]]
##### འདྲེས་པ་ལ་དཔྱོད་པ། ^8-18-3-4-0

[Block 1629]
འདྲེས་པ༌[^987]ལ་དཔྱོད་པ་ནི་གང་ཆོས་ཐམས་ཅད་འདྲེས་ཤིང་བསྡུས་པ་ལ་དམིགས་པའི་ཡེ་ཤེས་ཀྱིས༌[^988]མཐོང་བ་སྟེ། འདི་ལྟར་རྟེན་གནས་གྱུར་པ་ཉིད་དོ། །

[Block 1630 [HEADING]]
##### འབྱོར་པ་ལ་དཔྱོད་པ། ^8-18-3-5-0

[Block 1631]
རྟེན་གནས་གྱུར་པ་དེ་ཉིད༌[^989]ལས་ནི་འབྱོར་པ་ལ་དཔྱོད་པར༌[^990]འགྱུར་ཏེ། གང་ཅི་བསམས་པ་དེ་ཐམས་ཅད་འབྱོར་པར་འགྱུར་རོ། །

[Block 1632]
དེ་ཡང་ཇི་ལྟར་ས་ལ་སོགས་པ་ཡང་དེ་ལྟར་བརྟགས་ན་གཞན་གསེར་ལ་སོགས་པར་འགྱུར་བའོ། །

[Block 1633]
ཡང་དེ་ནི་བརྟགས་པས་འབྱོར་པར་འགྱུར་བས་ན་འབྱོར་པ་ལ་དཔྱོད་པ་སྟེ།[^991] ཇི་ལྟར་དཔྱོད་པ་དེ་བཞིན་དུ་འབྱོར་པར་འགྱུར་བའོ། །

[Block 1634]
རྣམ་པར་མི་རྟོག་པའི་རྣམ་པར་གཞག་པ་བསྟན་ཟིན་ཏོ། །

[Block 1635 [HEADING]]
### སྒྲུབ་པར་བྱེད་པ། ^8-19-0

[Block 1636]
སྒྲུབ་པར་བྱེད་པ་མ་བསྟན་པས་དེ་སྟོན་པར་བྱེད་པའི་ཚིགས་སུ་བཅད་པ་ནི།

[Block 1637 [VERSE]]
ཡི་དྭགས་དུད་འགྲོ་མི་རྣམས་དང་། །
ལྷ་རྣམས་ཇི་ལྟར་འོས་འོས་སུ། །

[Block 1638]
ཞེས་བྱ་བ་སྟེ། དུད་འགྲོ་རྣམས་ཀྱིས༌[^992]ཆུ་ལ། ཡི་དྭགས་རྣམས་ཀྱིས་ཐང་དུ་དང་། མི་རྣམས་ཀྱིས་མི་གཙང་བ༌[^993]དང་། དུད་འགྲོ་ཕག་ལ་སོགས་པས་གཙང་བར་མཐོང་བ་དང་། མི་རྣམས་ལ་ཟས་དེ་དག་གཙང་བ་ལ། ལྷ་རྣམས་ལ་དེ་དག་མི་གཙང་བ་དེ་ལྟར་བྱས་ནས། དངོས་གཅིག་ཡིད་ནི་ཐ་དད་པར་མཐོང་བས་ན་དོན་རྣམས་གྲུབ་པ་མེད་པར་འདོད་པར་བྱའོ། །

[Block 1639]
དེ་ལ་བདེན་པ་ཉིད་དུ་མ་གྲུབ་པས་དོན་གང་ཡང་ཡོད་པ་མ་ཡིན་ཏེ། དེས་ན་རྣམ་པར་ཤེས་པ་དམིགས་པ་མེད་པ་ཉིད་དུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 1640]
དེའི་ཕྱིར་འདི་ནི་དམིགས་པ་མེད་པ་ཡིན་ཏེ། འདིའི་དམིགས་པ་ནི་རྨི་ལམ་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 1641]
ཇི་ལྟར་འདས་པ་དང་མ་འོངས་པ་ལ་དེ་དམིགས་པ་དང་། ཇི་ལྟར་མེ་ལོང་དང་། [^994]ཏིང་ངེ་འཛིན་གྱི་སྤྱོད་ཡུལ་ལྟ་བུ་ཡིན་པས་དེ་ཚིགས་སུ་བཅད་པས་སྟོན་པ་ནི། འདས་སོགས་དེ་བཞིན་རྨི་ལམ་དང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དེ་ཡང༌[^995]ཕྱེད་སྔ་མས་ཕྱི་མ་དང་གོ་རིམས་ཇི་ལྟ་བ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 1642]
འདི་ལྟར་ཡོད་པ༌[^996]མ་ཡིན་པའི་དམིགས་པ་ནི། དམིགས་པ་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་ཏེ། དམིགས་པ་མེད་པ་ཉིད་དོ། །

[Block 1643]
དེ་ཉིད་ལ་དམིགས་པ་ནི་དེ་ལ་དམིགས་པ་སྟེ། རང་གི་གཟུགས་བརྙན་ལ་དམིགས་པ་ཉིད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1644]
དེ་ཡང་འདས་པ་དང་། མ་འོངས་པ་དང་། རྨི་ལམ་དང་། གཟུགས་བརྙན་དག་གོ་རིམས་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 1645 [VERSE]]
དོན་ནི་དོན་དུ་གྲུབ་ན་ནི། །
ཡེ་ཤེས་རྟོག་པ་མེད་མི་འགྱུར། །

[Block 1646]
ཞེས་བྱ་བ་ལ། གལ་ཏེ་དོན་གྱི་ངོ་བོ་ཉིད་དུ་ཡོད་ན་ནི་དེས་ན་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་མེད་པར་འགྱུར་རོ། །

[Block 1647]
འོན་ཏེ་དེ་མེད་པའི་ངོ་བོ་ཉིད་ནི་འདོད་པ་ཡིན་ནོ་ཞེ་ན། དེས་ན་རྣམ་པར་མི་རྟོག་པ་དེ་མེད་པས་ན་སངས་རྒྱས་ཉིད་ཀྱང་འཐོབ་པར་མི་འགྱུར་རོ། །

[Block 1648]
དེས་ན་ངེས་པར་འདི་ལྟར་འདོད་པར་བྱ་བ་ཡིན་པས། བྱང་ཆུབ་སེམས་དཔའ་དབང་ཐོབ་དང་། །ཞེས་བྱ་བ་སྟེ། དབང་ཐོབ་པར་གྱུར་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1649]
མོས་དབང་གིས་ཞེས་བྱ་བ་ནི་བསམ་པའི་དབང་གིས་དེ་ལྟ་བུ་མེད་པའི་ས་ལ་སོགས་པ་དག་འདི་ལྟར་གསེར་ལ་སོགས་པའི་རང་བཞིན་དུ་འགྱུར་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1650]
བསམ་གཏན་པའི་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་ལ་སོགས་པ་གཞན་གྱི་ཡང་ངོ་། །འདི་ལ་རྣམ་པར་འབྱེད་གྲུབ་པ། །ཞེས་བྱ་བ་ནི་ལྷག་མཐོང་གྲུབ་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
