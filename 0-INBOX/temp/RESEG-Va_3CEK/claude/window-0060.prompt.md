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
[Block 2101]
གཉེན་པོས་རིང་བ་ཉིད་ནི་དཔེར་ན་འཆལ་པའི་ཚུལ་ཁྲིམས་ལས་ཚུལ་ཁྲིམས་ལྟ་བུའོ། །

[Block 2102 [HEADING]]
#### ཡུལ་གྱིས་རིང་བ་ཉིད། ^2-36-3-0

[Block 2103]
ཡུལ་གྱིས་རིང་བ་ཉིད་ནི་དཔེར་ན་བསྐལ་པའི་ཡུལ༌[^1547]རྣམ་པར་ཆད་པས་ཏེ། ཤར་དང་ནུབ་ཀྱི་རྒྱ་མཚོ་བཞིན་ནོ། །

[Block 2104 [HEADING]]
#### དུས་ཀྱིས་རིང་བ་ཉིད། ^2-36-4-0

[Block 2105]
དུས་ཀྱིས༌[^1548]རིང་བ་ཉིད་ནི་དཔེར་ན༌[^1549]འདས་པ་དང་མ་འོངས་པ་ལྟ་བུའོ། །

[Block 2106]
རིང་བ་ཞེས་བྱ་བ་དེ་གང་ལས་རིང་བ་ཡིན། ད་ལྟར་ལས་སོ། །

[Block 2107]
འདས་མ་ཐག་པ་དང་། སྐྱེ་བར་འགྱུར་བ་གང་ཡིན་པ་དེ་ཇི་ལྟར་ན་རིང་བ་ཡིན། དེ་ནི་དུས་ཐ་དད་པ་ཉིད་ཀྱིས་རིང་བ་ཡིན་གྱི་ཡུན་རིང་མོ་ཞིག་ན་བྱུང་བ་དང་། འབྱུང་བ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 2108]
ད་ལྟར་ཡང་དེ་བཞིན་དུ་རིང་བར་འགྱུར་རོ། །

[Block 2109]
འོ་ན་ནི་བྱེད་པས་རིང་བ་ཉིད༌[^1550]ཡིན་ནོ། །

[Block 2110]
འདུས་མ་བྱས་ཇི་ལྟར་ན་ཉེ་བ་ཉིད་དུ་འགྲུབ། དེ་ཐམས་ཅད་དུ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 2111]
འདས་པ་དང་མ་འོངས་པ་དག་ལ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 2112]
ནམ་མཁའ་ཡང་ཇི་ལྟར་ཉེ་བ་ཡིན། དེ་ལྟ་ན༌[^1551]འོ་ན་ནི༌[^1552]འདས་པ་དང་མ་འོངས་པ་ནི༌[^1553]ད་ལྟར་གྱིས་ཆོད་པའི་ཕྱིར་ཕན་ཚུན་དུ་རིང་བ་ཉིད༌[^1554]ཡིན་ནོ། །

[Block 2113]
ད་ལྟར་ནི་གཉི་ག་དང་ཉེ་བའི་ཕྱིར་ཉེ་བ་ཡིན་ལ། འདུས་མ་བྱས་ཀྱང་ཆོད་པ་མེད་པའི་ཕྱིར་ཉེ་བ་ཡིན་ནོ། །

[Block 2114]
དེ་ལྟ་ན་ཡང་འདས་པ་དང་མ་འོངས་པ་དང༌[^1555]ད་ལྟར་བྱུང་བ༌[^1556]དང་ཉེ་བའི་ཕྱིར་གཉི་གར་འགྱུར་རོ། །

[Block 2115]
འདི་སྐད་དུ་མ་འོངས་པ་ནི་མ་ཐོབ་པའི་ཕྱིར་ཆོས་ཀྱི་རང་གི་མཚན་ཉིད་ལས་རིང་བ་ཡིན་ལ། འདས་པ་ནི་ཞིག་པའི་ཕྱིར་རིང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རིགས་པར་འགྱུར་རོ། །

[Block 2116 [HEADING]]
### བྲལ་བའི་ཐོབ་པ། ^2-37-0

[Block 2117]
ཅི་ལམ་ཁྱད་པར་དུ་འགྲོ་བའི་ཕྱིར་ཉོན་མོངས་པ་རྣམས་ཀྱི་སྤངས་པ་ཡང༌[^1557]དང་ཡང་དུ་ཁྱད་པར་དུ་འགྱུར་རམ་ཞེ་ན། དེ་ནི་མེད་དེ་ཉོན་མོངས་པ་ཐམས་ཅད་ནི་ལན་ཅིག་ཏུ་ཟད། གང་གི་སྤོང་བའི་ལམ་གང་ཡིན་པ་དེ་ཁོ་ནས༌[^1558]དེ་ཟད་པ་ཡིན་ནོ། །

[Block 2118]
དེ་དག་གི་བྲལ་བའི་ཐོབ་པ་ཡང་དང་ཡང་། དུས་དུ་ཞིག་ཏུ་ཞེ་ན། སྨྲས་པ། དུས་དྲུག་ཏུ་སྟེ།

[Block 2119 [VERSE]]
གཉེན་པོ་སྐྱེས་དང་འབྲས་ཐོབ་དང་། །
དབང་པོ་རྣམ་པར་འཕེལ་རྣམས་སུ། །

[Block 2120]
འདི༌[^1559]ནི་གཉེན་པོའི༌[^1560]རྣམ་པར་གྲོལ་བའི་ལམ་མིན་པར༌[^1561]བསམས་པའོ། །

[Block 2121]
འབྲས་བུ་དག་ནི་དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་བཞིའོ། །

[Block 2122]
དབང་པོ་རྣམ་པར་འཕེལ་བ་ནི་དབང་པོ་ལྔ་པོ༌[^1562]འཕོ་བའོ། །

[Block 2123]
དུས་དེ་དག་ཏུ་ཉོན་མོངས་པའི་བྲལ་བ་འཐོབ་པོ། །དེ་ཡང་ཅི་རིགས་པར་ཁ་ཅིག་གིས༌[^1563]དུས་དྲུག་ཏུ་འཐོབ་པ་ནས་ཁ་ཅིག་གིས༌[^1564]ནི་དུས་གཉིས་ཀྱི་བར་དུ་འཐོབ་པར་བལྟ་བར་བྱའོ། །

[Block 2124 [HEADING]]
### ཡོངས་སུ་ཤེས་པ། ^2-38-0

[Block 2125]
བྲལ་བ་དེ་ཉིད་གནས་སྐབས་དེ་དང་དེ་དག་ཏུ་ཡོངས་སུ་ཤེས་པ་ཞེས་བྱ་བའི་མིང་འཐོབ་པོ། །ཡོངས་སུ་ཤེས་པ་ནི་གཉིས་ཏེ། ཡེ་ཤེས་ཀྱི་ཡོངས་སུ་ཤེས་པ་དང་། སྤངས་པའི་ཡོངས་སུ་ཤེས་པའོ། །

[Block 2126 [HEADING]]
#### ཡེ་ཤེས་ཀྱི་ཡོངས་སུ་ཤེས་པ། ^2-38-1-0

[Block 2127]
དེ་ལ་ཡེ་ཤེས་ཀྱི་ཡོངས་སུ་ཤེས་པ་ནི་ཟག་པ་མེད་པའི་ཤེས་པའོ། །

[Block 2128 [HEADING]]
#### སྤངས་པའི་ཡོངས་སུ་ཤེས་པ། ^2-38-2-0

[Block 2129]
སྤངས་པའི་ཡོངས་སུ་ཤེས་པ་ནི་སྤང་བ༌[^1565]ཁོ་ན་སྟེ། འབྲས་བུ་ལ་རྒྱུ་བཏགས་པའི་ཕྱིར་རོ། །

[Block 2130 [HEADING]]
##### ཡོངས་སུ་ཤེས་པ་དགུ། ^2-38-2-1-0

[Block 2131]
ཅི་སྤངས་པ་ཐམས་ཅད་ཡོངས་སུ་ཤེས་པ་གཅིག་ཁོ་ན་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 2132]
འོ་ན་ཇི༌[^1566]ལྟ་བུ་ཞེ་ན། ཡོངས་སུ་ཤེས་དགུ།

[Block 2133 [VERSE]]
དེ་ལ་རེ་ཞིག་འདོད་པ་ན། །
དང་པོའི་རྣམ་གཉིས་ཟད་ལ་གཅིག །

[Block 2134]
འདོད་པའི་ཁམས་ན་དང་པོའི་རྣམ་པ་གཉིས་ཏེ། སྡུག་བསྔལ་དང་ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བ་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པ་གཅིག་ཡིན་ནོ། །

[Block 2135]
གཉིས་ཟད་པ་ནི་དེ་གཉིས་སོ། །

[Block 2136]
འདོད་པའི་ཁམས་ཁོ་ན་ན་འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བའི་རྣམ་པ་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པ་གཅིག་ཡིན་ལ། ལམ་མཐོང་བས་སྤང་བར་བྱ་བའི་རྣམ་པ་སྤངས་པ་ཡང་གཅིག་ཡིན་ནོ། །

[Block 2137]
ཇི་ལྟར་འདོད་པ་ན་སྤྱོད་པའི༌[^1567]མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ཡོངས་སུ་ཤེས་པ་གསུམ་ཡིན་པ་ལྟར། དེ་བཞིན་གོང་མའི་དེ་གསུམ་ཉིད། །དེ་བཞིན་དུ་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི༌[^1568]མཐོང་བས་སྤང་བར་བྱ་བའི་རྣམ་པ༌[^1569]སྤངས་པ་ཡང་ཡོངས་སུ་ཤེས་པ་གསུམ་ཡིན་ཏེ། སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ནི་གཅིག་ཡིན་ནོ། །

[Block 2138]
འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ནི་གཉིས༌[^1570]ཡིན་ནོ། །

[Block 2139]
ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ནི་གསུམ༌[^1571]ཡིན་ནོ། །

[Block 2140]
དེ་ལྟར་ན་ཁམས་གསུམ་པའི་ཕྱིར༌[^1572]མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པ་དྲུག་ཡིན་ནོ། །
--- END BLOCKS ---
