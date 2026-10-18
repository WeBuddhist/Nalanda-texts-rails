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

[Block 1581 [HEADING]]
### རྒྱས་པར་འགྱུར་བ། ^2-16-0

[Block 1582]
ཕྲ་རྒྱས་དགུ་བཅུ་རྩ་བརྒྱད་པོ་དེ་དག་ལས༌[^1152]དུ་ནི་དམིགས་པའི་སྒོ་ནས་རྒྱས་པར་འགྱུར། དུ་ནི་མཚུངས་པར་ལྡན་པ་ཁོ་ནའི་སྒོ་ནས་རྒྱས་པར་འགྱུར་ཞེ་ན།

[Block 1583 [HEADING]]
#### དམིགས་པའི་སྒོ་ནས་རྒྱས་པར་འགྱུར་བ། ^2-16-1-0

[Block 1584 [VERSE]]
ཕྲ་རྒྱས་ཀུན་དུ་འགྲོ་རྣམས་ནི། །
དམིགས་པའི་སྒོ་ནས་རང་གི་ས། །
ཐམས་ཅད་དུ་ནི་རྒྱས་པར་འགྱུར། །

[Block 1585]
ཀུན་འགྲོ་མ་ཡིན་རང་རིས་སོ།[^1153] །ཕྲ་རྒྱས་གང་དག་ཀུན་དུ་འགྲོ་བ་དེ་དག་ནི་དམིགས་པའི་སྒོ་ནས་རང་གི་ས་པའི་རྣམ་པ་ལྔ་པོ་ཐམས་ཅད་ལ་ཡང་རྒྱས་པར་འགྱུར་རོ། །

[Block 1586]
ཐམས་ཅད་དུ་ནི༌[^1154]འགྲོ་བ་མ་ཡིན་པ་རྣམས་ནི་དམིགས་པའི་སྒོ་ནས་རང་གི་སར་རང་གི་རིས་ཁོ་ན་ལ་རྒྱས་པར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ཀྱང་སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བའི་རིས་ཁོ་ན་ལ་རྒྱས་པར་འགྱུར་ལ། དེ་བཞིན་དུ་བསྒོམ་པས་སྤང་བར་བྱ་བ་རྣམས་ཀྱང་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཁོ་ན་ལ་རྒྱས་པའི་བར་དུ་འགྱུར་གྱི། གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1587]
སྤྱིར་བཏང་བར་བྱས་ནས་དམིགས་ཀྱིས་སྟོན་པར་བྱེད་དེ། ཟག་མེད་གོང་མའི་ཡུལ་ཅན་མིན། །ཟག་པ་མེད་པ་ལ་དམིགས་པའི་ཕྲ་རྒྱས་རྣམས་ནི་དམིགས་པའི་སྒོ་ནས་རྒྱས་པར་མི་འགྱུར་བ་ཁོ་ན་ཡིན་ལ། ས་གོང་མ་ལ་དམིགས་པ་རྣམས་ཀྱང་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་དག་གི་དམིགས་པའི་དངོས་པོ་ནི། བདག་གིར་མ་བྱས་གཉེན་པོའི་ཕྱིར། །དངོས་པོ་གང་ཞིག་བདག་ཏུ་ལྟ་བ་དང་སྲེད་པ་དག་གིས་བདག་གིར་བྱས་པ་དེ་ལ་ཕྲ་རྒྱས་གཞན་དག་ཀྱང་རྒྱས་པར་འགྱུར་བར་ནུས་ཏེ། སྣམ་བུ་གཤེར་བ་ལ་རྡུལ་ཆགས་པ་བཞིན་ནོ། །

[Block 1588]
ཟག་པ་མེད་པ་ཡང་དེ་ལྟ་མ་ཡིན་ལ། ས་འོག་མ་ལ་ཡང་མ་ཡིན་པས་དེའི་ཕྱིར་དེ་དག་ལ་དམིགས་པ་རྣམས་ནི་དེ་དག་ལ་རྒྱས་པར་མི་འགྱུར་རོ། །

[Block 1589]
གང་ཞིག་འདི་ན་གནས་པ་ལས་དེ་དོན་དུ་གཉེར་བར་བྱེད་པ་དེ་ནི་མི༌[^1155]དགེ་བའི་ཆོས་ལ་འདུན་པ་ཡིན་ནོ། །

[Block 1590]
མྱ་ངན་ལས་འདས་པ་དང་ལམ་ནི་དེ་དག་ལ་དམིགས་པའི་ཉོན་མོངས་པ་རྣམས་ཀྱི་གཉེན་པོར་གྱུར་པ་ཡིན་ལ། ས་གོང་མ་ཡང་འོག་མ་རྣམས་ཀྱི་གཉེན་པོ་ཡིན་པས་དེའི་ཕྱིར་ཡང་དེ་དག་ཏུ་གནས་མི་མཐོང་སྟེ།[^1156] རྡོ་བསྲེག་པ་ལ་རྐང་མཐིལ་དག་གི་གནས་མི་མཐོང་བ༌[^1157]བཞིན་ནོ། །

[Block 1591]
གཞན་དག་ན་རེ་ཕྲ་རྒྱས་ཀྱི་དོན་ནི་རྗེས་སུ་མཐུན་པའི་དོན་ཡིན་ན་དེ་དག་ནི༌[^1158]དེ་རྣམས་ཀྱི་རྗེས་སུ་མཐུན་པ་མ་ཡིན་ཏེ། རླུང་ནད་ཅན་ལ་ཁ་ཟས་རྩུབ་པོ་རྒྱས་པར་མི་འགྱུར་བ་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1592]
དམིགས་པའི་སྒོ་ནས་རྒྱས་པར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་བཤད་ཟིན་ཏོ། །

[Block 1593 [HEADING]]
#### མཚུངས་པར་ལྡན་པའི་སྒོ་ནས་རྒྱས་པར་འགྱུར་བ། ^2-16-2-0

[Block 1594 [VERSE]]
གང་ཞིག་གང་དང་མཚུངས་ལྡན་པ། །
དེ་ནི་དེར་མཚུངས་ལྡན་སྒོ་ནས། །

[Block 1595]
རྒྱས་པར་འགྱུར་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཕྲ་རྒྱས་གང་ཞིག་ཆོས་གང་དང་མཚུངས་པར་ལྡན་པ་དེ་ནི་དེར་མཚུངས་པར་ལྡན་པའི་སྒོ་ནས་རྒྱས་པར་འགྱུར་རོ། །

[Block 1596]
ནི་ཞེས་བྱ་བའི་སྒྲ་ནི་ཇི་སྲིད་དུ་མ་སྤངས་པ་ཞེས་བྱ་བ༌[^1159]ཁྱད་པར་དུ་བྱ་བའི་ཕྱིར་རོ། །

[Block 1597]
ཟག་པ་མེད་པ་ལ་དམིགས་པ་དེག་ཀྱང་མ་ཡིན་སྐལ་བ་མི་མཉམ་པའི་ཁམས་ཀུན་ཏུ་འགྲོ་བ་དག་ཀྱང་མ་ཡིན་ལ། ཕྲ་རྒྱས་དེ་དག་ཀྱང་མཚུངས་པར་ལྡན་པའི་སྒོ་ནས་རྒྱས་པར་འགྱུར་གྱི་དམིགས་པའི་སྒོ་ནས་ནི་མ་ཡིན་པའི་ཕྲ་རྒྱས་དག་ལྟ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། སྐལ་བ་མི་མཉམ་པའི་ས་ལ་ཀུན་དུ་འགྲོ་བའི་ཕྲ་རྒྱས་རྣམས་སོ། །

[Block 1598 [HEADING]]
### མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ། ^2-17-0

[Block 1599]
ཕྲ་རྒྱས་དགུ་བཅུ་རྩ་བརྒྱད་པོ་དེ་དག་ལས་དུ་ནི་མི་དགེ་བ་ཡིན། དུ་ནི་ལུང་དུ༌[^1160]མ་བསྟན་པ་ཡིན་ཞེ་ན། གོང་མ་ཐམས་ཅད་ལུང་མ་བསྟན། །རེ་ཞིག་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཐམས་ཅད་ནི་ལུང་དུ་མ་བསྟན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1600]
ཆོས་ཉོན་མོངས་པ་ཅན་རྣམས་ཀྱི་རྣམ་པར་སྨིན་པ་ནི་སྡུག་བསྔལ་ཡིན་ན་དེ་ཡང་དེ་གཉིས་ན་མེད་དེ། ཕ་རོལ་པོ་ལ་ཡང་གནོད་པའི་རྒྱུ་མེད་པའི་ཕྱིར་རོ། །

[Block 1601 [VERSE]]
འདོད་ན་འཇིག་ཚོགས་ལྟ་བ་དང་། །
མཐར་འཛིན་ལྷན་ཅིག་མ་རིག་པ། །

[Block 1602]
འདོད་པའི་ཁམས་ན་ནི་འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། མཐར་འཛིན་པར་ལྟ་བ་དང་། དེ་དག༌[^1161]དང་མཚུངས་པར་ལྡན་པའི་མ་རིག་པ་ལུང་དུ་མ་བསྟན་པ༌[^1162]ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྦྱིན་པ་ལ་སོགས་པ་དང་མི་འགལ་བའི་ཕྱིར་དང་། [^1163]བདག་འཇིག་རྟེན་ཕ་རོལ་དུ་བདེ་བར་འགྱུར་བར་བྱའོ་ཞེས་སྦྱིན༌[^1164]པར་བྱེད། ཚུལ་ཁྲིམས་སྲུང་བར་བྱེད་དོ། །

[Block 1603]
ཆད་པར་ལྟ་བ་ཡང་ཐར་པའི་རྗེས་སུ་མཐུན་པ་དག་ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས། ཕྱི་རོལ་པའི་ལྟ་བར་གྱུར་པ༌[^1165]རྣམས་ཀྱི་ནང་ན་ནི་འདི་ལྟ་སྟེ། བདག་མེད་པར་གྱུར་ཅིག །

[Block 1604 [VERSE]]
བདག་གི་མེད་པར་གྱུར་ཅིག །
བདག་འབྱུང་བར་མ་གྱུར་ཅིག །

[Block 1605]
བདག་གི་འབྱུང་བར་མ་གྱུར་ཅིག་ཅེས་བྱ་བའི༌[^1166]ལྟ་བ་འདི་མཆོག་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 1606]
གཞན་ཡང་ལྟ་བ་འདི་གཉིས་ནི་རང་གི་རྫས་ལ་ཀུན་དུ་རྨོངས་པའི་ཕྱིར་དང་། ཕ་རོལ་པོ་ལ་གནོད་པའི་རྣམ་པར་ཞུགས་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1607]
མཐོ་རིས་ལ་སྲེད་པ་དང་། ངའོ་སྙམ་པའི་ང་རྒྱལ་དག་ཀྱང་དེ་ལྟར་ཐལ་བར་འགྱུར་རོ། །

[Block 1608]
སྔོན་གྱི་སློབ་དཔོན་རྣམས་ན་རེ། ལྷན་ཅིག་སྐྱེས་པའི་འཇིག་ཚོགས་ལ་ལྟ་བ་རི་དགས་དང་བྱ་རྣམས་ལ་ཡང་ཡོད་པ་གང་ཡིན་པ་ནི་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 1609]
རྣམ་པར་བརྟག་པ་ནི་མི་དགེ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1610]
ལྷག་མ་རྣམས་འདིར་མི་དགེ་བའོ། །

[Block 1611]
ཕྲ་རྒྱས་ལྷག་མ་རྣམས་ནི་འདོད་པའི་ཁམས་ན་མི་དགེ་བ་དག་ཡིན་ནོ། །

[Block 1612 [HEADING]]
### མི་དགེ་བའི་རྩ་བ། ^2-18-0

[Block 1613]
དུ་ནི་མི་དགེ་བའི་རྩ་བ་དག་ཡིན། དུ་ནི་མ་ཡིན་ཞེ་ན།

[Block 1614 [VERSE]]
འདོད་ན་འདོད་ཆགས་ཁོང་ཁྲོ་དང་། །
རྨོངས་རྣམས་མི་དགེའི་རྩ་བ་ཡིན། །

[Block 1615]
འདོད་པའི་ཁམས་ན་འདོད་ཆགས་ཐམས་ཅད་དང་། ཁོང་ཁྲོ་བ་ཐམས་ཅད་དང་། འཇིག་ཚོགས་དང་། མཐར་འཛིན་པར་ལྟ་བ་དང་། མཚུངས་པར་ལྡན་པ་མ་གཏོགས་པའི་རྨོངས་པ་ཐམས་ཅད་ནི་གོ་རིམས་བཞིན་དུ་མི་དགེ་བའི་རྩ་བ་གསུམ་པ༌[^1167]ཆགས་པ་མི་དགེ་བའི་རྩ་བ་དང་། ཞེ་སྡང་མི་དགེ་བའི་རྩ་བ་དང་། གཏི་མུག་མི་དགེ་བའི་རྩ་བ་ཡིན་ཏེ། གང་ཞིག་མི་དགེ་བ་ཡང་ཡིན་ལ་མི་དགེ་བའི་རྩ་བ་ཡང་ཡིན་པ་དེ་ཁོ་ན་མི་དགེ་བའི་རྩ་བ་ཡིན་པར་འདོད་དོ། །
--- END BLOCKS ---
