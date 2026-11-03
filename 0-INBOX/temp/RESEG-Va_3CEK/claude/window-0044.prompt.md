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
[Block 1541]
ཅི་རེ་ཞིག་རིམ་གྱིས་སམ་འོན་ཏེ་ཅིག་ཅར་ཡང༌[^1118]དམིགས། གལ་ཏེ་རིམ་གྱིས་ན་ནི་གཞན་དག་ལ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 1542]
འོན་ཏེ་ཅིག་ཅར་རོ་ཞེ་ན་ནི། སུ་ཞིག་འདོད་པའི་ཁམས་མཐའ་དག་གིས་འདག་པར༌[^1119]ཡིད་ཆེས་པར་འགྱུར་བའམ། མཐའ་དག་རྒྱུ་མ་ཡིན་པ་ལས༌[^1120]རྒྱུར་ཡིད་ཆེས་པར་འགྱུར། མཐའ་དག་ལ་ནི༌[^1121]ཅིག་ཅར་དུ་དམིགས་སོ་ཞེས་ནི་མི་ཟེར་རོ། །

[Block 1543]
འོན་ཀྱང་རྣམ་པ་ལྔ་པོ་ཐམས་ཅད་ཀྱང་ཅིག་ཅར་དུ་དམིགས་སོ། །

[Block 1544]
དེ་ལྟ་ན་ཡང་གང་ལ་བདག་ཏུ་ལྟ་བ་ཡོད་པ་དེ་ལ་བདག་ལ་སྲེད་པ་ཡོད་ལ།[^1122] གང་ལ་མཆོག་དང་དག་པར་ལྟ་བ་ཡོད་པ་དེ་ལ་དེའི་དོན་དུ་གཉེར་བ་ཡོད་ཅིང་། དེས་ཀྱང་ང་རྒྱལ་དུ་འགྱུར་བས་སྲེད་པ་དང་ང་རྒྱལ་དག་ཀྱང་རུང༌[^1123]ཀུན་དུ་འགྲོ་བ་ཡིན་པར་འགྱུར་རོ། །

[Block 1545]
དེ་ལྟ་ཡིན་ན་དེ་གཉི་ག་མཐོང་བ་དང་བསྒོམ་པས་སྤང་བར་བྱ་བ་ལ་དམིགས་པའི་ཕྱིར་ཅི་ཞིག་གིས་སྤང་བར་བྱ་བ་ཡིན་ཞེ་ན། འདྲེན་མ་ལ་དམིགས་པའི་ཕྱིར༌[^1124]བསྒོམ་པས་སྤང་བར་བྱ་བ་དག༌[^1125]ཡིན་ནོ། །

[Block 1546]
ཡང་ན་ལྟ་བའི་སྟོབས་བསྐྱེད་པས་བཅུ་པ༌[^1126]ཅན་ཉིད་ཡིན་པའི་ཕྱིར་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1547]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཉོན་མོངས་པ་འདི་གཉིས་རང་གི་མཚན་ཉིད་པ་ཡིན་གྱི་ཉོན་མོངས་པ་སྤྱི་པ་འདི༌[^1127]ནི་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་ཀུན་ཏུ་འགྲོ་བ་དག་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1548 [HEADING]]
### སྐལ་བ་མི་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ། ^2-14-0

[Block 1549]
ཡང༌[^1128]སྐལ་བ་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་དག་ཏུ་ཕྲ་རྒྱས་བཅུ་གཅིག་བཤད་པ་གང་དག་ཡིན་པ་དེ་དག་ལས་དགུ་གང༌[^1129]དུ་དམིགས། ལྟ་བ་གཉིས་པོ་མ་གཏོགས་སོ། །

[Block 1550]
འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། མཐར་འཛིན་པར་ལྟ་བ་ལས༌[^1130]མ་གཏོགས་པ་ཕྲ་རྒྱས་གཞན་དགུ་ནི་སྐལ་བ་མི་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་དག་ཡིན་ནོ། །

[Block 1551]
རེས་འགའ་ནི་སྐལ་བ་མི་མཉམ་པའི་ཁམས་གཅིག་ལ་དམིགས་སོ། །

[Block 1552]
རེས་འགའ་ནི་གཉིས་ལ་དམིགས་ཏེ། འདོད་པ་དང་ལྡན་པ་གཟུགས་དང་ལྡན་པ་ལ་དམིགས་པ་རྣམས་ལ།[^1131] གཟུགས་མེད་པ་དང་ལྡན་པ་ལ་དམིགས་པ་རྣམས་དང་། འདོད་པ་དང་ལྡན་པ་གཟུགས༌[^1132]མེད་པ་དང་ལྡན་པ་ལ་དམིགས་པའི་ཕྲ་རྒྱས་གང་དག་ཡིན་པ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1553]
གང་གི་ཚེ་འདོད་པའི་ཁམས་ན་གནས་པ་ཚངས་པ་ལ་སེམས་ཅན་དུ་ལྟ་བ་དང་། རྟག་པར་ལྟ་བ་སྐྱེད་པར་བྱེད་པ་དེའི་ཚེ་ཇི་ལྟར་འཇིག་ཚོགས་དང་། མཐར་འཛིན་པར་ལྟ་བ་སྐལ་བ་མི་མཉམ་པའི་ཁམས་ལ་དམིགས་པ་དག་མ་ཡིན་ཞེ་ན། བདག་དང་བདག་གིར་མི་འཛིན་པའི་ཕྱིར་དང་། མཐར་འཛིན་པར་ལྟ་བ་ཡང་དེས་ཀུན་ནས་བསླང་བའི་ཕྱིར་རོ། །

[Block 1554]
[^1133]འོ་ན་འདི་ལྟ་བ་གང་ཞིག་ཡིན་ཞེ་ན། ཆོས་མངོན་པ་པ་རྣམས་ན་རེ་འདི་ནི་ལྟ་བ་མ་ཡིན་གྱི་འདི་ནི་ལོག་པའི་ཤེས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1555]
ཡང༌[^1134]དེ་ལ་དམིགས་པ་གཞན་དག་ནི་ལྟ་བ་ཡིན་གྱི་འདི་ནི་ལྟ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ༌[^1135]འདི་ག་ལས་ཤེ་ན། གྲུབ་པའི་མཐའ་ནི་ཚད་མར་བྱ་དགོས་སོ། །

[Block 1556]
ཡང་ཅི་ཕྲ་རྒྱས་ཁོ་ན་ཀུན་དུ་འགྲོ་བ་དག་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ཏེ། དེ་དག་དང་ནི་ལྷན་ཅིག་གང་།[^1136] །འབྱུང་དེའང་ཀུན་འགྲོ་ཐོབ་མ་གཏོགས། །ཆོས་གཞན་ཕྲ་རྒྱས་ཀུན་དུ་འགྲོ་བ་རྣམས་དང་། ལྷན་ཅིག་འབྱུང་བ་གང་དག་ཡིན་པ་དེ་དག་ཀྱང་ཀུན་དུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 1557]
ཐོབ་པ་རྣམས་ནི་འབྲས་བུ་དུ་མའི་ཕྱིར་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 1558]
དེ་ཉིད་ཀྱི་ཕྱིར་ཕྲ་རྒྱས་ཀུན་དུ་འགྲོ་བ་དག་ཡིན་ལ་ཕྲ་རྒྱས་ཀུན་དུ་འགྲོ་བའི་རྒྱུས་རྒྱུ་མ་ཡིན་པ་དག་ཀྱང་ཡོད་ཅེས་བྱ་བ་མུ་བཞིར་བྱ་སྟེ། མུ་དང་པོ་འདི༌[^1137]མ་འོངས་པའི་ཕྲ་རྒྱས་ཀུན་དུ་འགྲོ་བ་རྣམས་སོ། །

[Block 1559]
གཉིས་པ་ནི་འདས་པ་དང་ད་ལྟར་བྱུང་བའི་ལྷན་ཅིག་འབྱུང་བ་རྣམས་སོ། །

[Block 1560]
གསུམ་པ་དང་།

[Block 1561]
བཞི་པ་དག་ནི་སྦྱར་བར༌[^1138]བྱའོ། །

[Block 1562 [HEADING]]
### ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ་ལ་དམིགས་པ། ^2-15-0

[Block 1563]
ཕྲ་རྒྱས་དགུ་བཅུ་རྩ་བརྒྱད་པོ་དེ་དག་ལས་དུ་ནི་ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་དག་ཡིན་ནོ། །

[Block 1564]
[^1139]དུ་ནི་ཟག་པ་མེད་པ་ལ་དམིགས་པ་དག་ཡིན་ཞེ་ན།

[Block 1565 [VERSE]]
འགོག་དང་ལམ་མཐོང་སྤང་བྱ་བ། །
ལོག་ལྟ་ཐེ་ཚོམ་དེ་དག་དང་། །

[Block 1566]
ལྡན་དང་འབའ་ཞིག་མ་རིག་པ།[^1140] །དྲུག་ནི་ཟག་མེད་སྤྱོད་ཡུལ་ཅན། །འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བའི་ཕྲ་རྒྱས་གསུམ་པོ་ལོག་པར་ལྟ་བ་དང་། ཐེ་ཚོམ་དང་། དེ་དག་དང་། མཚུངས་པར་ལྡན་པ་དང་མ་འདྲེས་པའི་མ་རིག་པ་དང་། ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཡང༌[^1141]གསུམ་པོ་དེ་དག་ཉིད་དེ། དེ་ལྟར་ན་དྲུག་པོ་དེ་དག་ནི་ཟག་པ་མེད་པ་ལ་དམིགས་པ་དག༌[^1142]ཡིན་ནོ། །

[Block 1567]
ལྷག་མ་རྣམས་ནི་ཟག་པ་དང་བཅས་པ་དག༌[^1143]ལ་དམིགས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པོ། །དེ་ལ་ཡང་།

[Block 1568 [VERSE]]
རང་གི་ས་པའི་འགོག་པ་དང་། །
ལམ་ནི་ཕན་ཚུན་རྒྱུ་ཡིན་པས། །
ས་དྲུག་ས་དགུའི་ལམ་ནི་དེའི། །
སྤྱོད་ཡུལ་ཅན་གྱི་ཡུལ་ཡིན་ནོ། །

[Block 1569]
འགོག་པ་ལ་དམིགས་པ་ལོག་པར་ལྟ་བ་ལ་སོགས་པའི་དམིགས་པ་ནི་རང་གི་ས་པའི་འགོག་པ་ཁོ་ན་ཡིན་ཏེ། འདོད་པ་ན་སྤྱོད་པ་རྣམས་ཀྱི་ཡང་འདོད་པའི་ཁམས་ཀྱི་ཁོ་ན་ཡིན་ལ། སྲིད་པའི་རྩེ་མོའི་ས་པ་རྣམས་ཀྱི་བར་དུ་ཡང་སྲིད་པའི་རྩེ་མོའི་ཁོ་ན་ཡིན་ནོ། །

[Block 1570]
ལམ་ལ་དམིགས་པ་འདོད་པ་ན་སྤྱོད་པ་རྣམས་ཀྱི་དམིགས་པ་ནི་ས་དྲུག་གི་ཆོས་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པའི་ལམ་ཐམས་ཅད་ཡིན་ཏེ། གང་ཡང་གཟུགས་དང་གཟུགས་མེད་པའི་གཉེན་པོ་ཡང་ཡིན་ནོ། །

[Block 1571]
གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་ས་བརྒྱད་པོ་རྣམས་ཀྱི་དམིགས་པ་ཡང་ས་དགུ་པའི༌[^1144]རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པའི་ལམ་ཐམས་ཅད་ཡིན་ཏེ། ལམ་ནི་ཕན་ཚུན་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1572]
གལ་ཏེ་ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དག་ཀྱང་ཕན་ཚུན་རྒྱུ་ཡིན་མོད་ཀྱི་རྗེས་སུ་ཤེས་པ་འདོད་པའི་ཁམས་ཀྱི་གཉེན་པོ་ནི་མ་ཡིན་པས་ལམ་ལ་དམིགས་པས༌[^1145]འདོད་པ་ན་སྤྱོད་པ་རྣམས་རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པའི་ལམ་ལ་ནི་མི་དམིགས་སོ། །

[Block 1573]
འོ་ན་ནི་ཆོས་ཤེས་པ་གཟུགས་དང་གཟུགས་མེད་པའི་གཉེན་པོ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་ལམ་ལ་དམིགས་པ་དེའི་ས་པ་རྣམས་ཀྱི་དམིགས་པར༌[^1146]འགྱུར་རོ་ཞེ་ན། སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ༌[^1147]ལ་ཆོས་ཤེས་པ་དག་དེ་དག་གི་གཉེན་པོ་མ་ཡིན་པའི་ཕྱིར་དང༌[^1148]མཐའ་དག་ཀྱང་གཉེན་པོ་མ་ཡིན་ལ། མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ཀྱི་གཉེན་པོ་མ་ཡིན་པའི་ཕྱིར་གཟུགས་དང་གཟུགས་མེད་པ་མཐའ་དག་གི་ཡང་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་དང་པོ་མེད་པའི་ཕྱིར་དང་།

[Block 1574]
དང་པོ་རྣམས་ཀྱི་མ་ཡིན་པའི་ཕྱིར་དམིགས་པ་མ༌[^1149]ཡིན་ནོ། །

[Block 1575]
ཡང༌[^1150]ཅིའི་ཕྱིར་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་དང་། ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་དག་ཟག་པ་མེད་པ་ལ་དམིགས་པ་དག་ཏུ་མི་འདོད་ཅེ་ན། འདོད་ཆགས་མིན་ཏེ་སྤང་བྱའི་ཕྱིར། །འདོད་ཆགས་ནི་སྤང་བར་བྱ་བ་ཡིན་ན་གལ་ཏེ་ཟག་པ་མེད་པ་ལ་དམིགས་པ་ཡིན་ན་གོ་སྤང་བར་བྱ་བ་མ་ཡིན་པར་འགྱུར་ཏེ།

[Block 1576 [VERSE]]
དགེ་བའི་ཆོས་ལ་འདུན་པ་བཞིན་ནོ། །
གནོད་མི་བྱེད་ཕྱིར་ཞེ་སྡང་མིན། །

[Block 1577]
གནོད་པར་བྱེད་པའི་དངོས་པོ་ལ་ནི་ཁོང་ཁྲོ་བ་སྐྱེ་ན་འགོག་པ་དང་ལམ་དག་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 1578 [VERSE]]
ཞི་དང་དག་དང་མཆོག་གྱུར་ཕྱིར། །
ང་རྒྱལ་མ་ཡིན་མཆོག་འཛིན་མིན། །

[Block 1579]
འགོག་པ་དང་ལམ་དག་ནི་ཞི་བ་ཡིན་པའི་ཕྱིར་དེ་དག་གིས་ཁེངས་པར་འགྱུར་བ་འོངས༌[^1151]པ་ཡང་མ་ཡིན་ལ། ཡང་དག་པའི་དོན་དུ་དག་པ་ཡིན་པའི་ཕྱིར་དེ་གཉིས་ལ་དག་པར་འཛིན་པ་ནི་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1580]
དམན་པ་ལ་མཆོག་ཏུ་འཛིན་པ་ནི་ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་ཡིན་ན་དེ་གཉིས་ནི་མཆོག་ཀྱང་ཡིན་ཏེ། དེ་ལྟ་བས་ན་དེ་དག་གི་དམིགས་པ་ཟག་པ་མེད་པ་ཡིན་པར་རིགས་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
