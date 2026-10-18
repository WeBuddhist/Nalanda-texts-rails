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
[Block 2066 [HEADING]]
#### དམིགས་པ་ཡོངས་སུ་ཤེས་པ། ^2-32-1-0

[Block 2067]
དེ་ལ་དམིགས་པ་ཡོངས་སུ་ཤེས་པས་ནི་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ༌[^1515]མཐོང་བས་སྤང་བར་བྱ་བ་རང་གི་ས་ལ་དམིགས་པ་རྣམས་དང་། འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཟག་པ་མེད་པ་ལ་དམིགས་པ་རྣམས་ཟད་པར་འགྱུར་རོ། །

[Block 2068 [HEADING]]
#### དམིགས་པ་ཡང་དག་པར་ཟད་པ། ^2-32-2-0

[Block 2069]
དེ་ལ་དམིགས་པ་ཡང་དག་པར་ཟད་པས་ནི་སྐལ་བ་མི་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་རྣམས་ཟད་པར་འགྱུར་ཏེ། དེ་ལ་དམིགས་པ་ནི་སྐལ་བ་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་དག་ཡིན་པས་དེ་དག་སྤངས་ན་དེ་དག་ཀྱང་སྤང་བ༌[^1516]ཡིན་ནོ། །

[Block 2070 [HEADING]]
#### དམིགས་པ་སྤངས་པ། ^2-32-3-0

[Block 2071]
དམིགས་པ་སྤངས་པས་ནི་འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་རྣམས་ཟད་པར་འགྱུར་ཏེ། ཟག་པ་མེད་པ་ལ་དམིགས་པ་རྣམས༌[^1517]ནི་དེ་དག་གི་དམིགས་པ་ཡིན་པས་དེ་དག་སྤངས་ན་དེ་དག་ཀྱང་སྤང་བ༌[^1518]ཡིན་ནོ། །

[Block 2072 [HEADING]]
#### གཉེན་པོ་སྐྱེས་པ། ^2-32-4-0

[Block 2073]
བསྒོམ་པས་སྤང་བར༌[^1519]བྱ་བ་རྣམས་ནི་གཉེན་པོ་སྐྱེས་པས་ཟད་པར་འགྱུར། ཉོན་མོངས་པའི་རྣམ་པ་གང་དག༌[^1520]གི་གཉེན་པོ་ལམ་གང་ཡིན་པ་སྐྱེས་པ་དེ་སྤོང་བར་བྱེད་དོ། །གང་གི༌[^1521]གཉེན་པོ་གང་ཞིག་ཡིན་ཞེ་ན། ཆེན་པོའི་ཆེན་པོ་ནི༌[^1522]ཆུང་ངུའི་ཆུང་ངུ་ཞེས་བྱ་བ་སྟེ། རྒྱས་པར་ནི་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 2074 [HEADING]]
### གཉེན་པོ་རྣམ་བཞི། ^2-33-0

[Block 2075]
གཉེན་པོ་ཡང་རྣམ་པ་དུ་ཞིག་ཡོད་ཅེ་ན་སྨྲས་པ།

[Block 2076 [VERSE]]
གཉེན་པོ་རྣམ་བཞི་སྤོང་བ་དང་། །
གཞི༌[^1523]དང་སྲིད་ཉིད་རྣམ་པར་ནི། །

[Block 2077 [HEADING]]
#### སྤོང་བ་གཉེན་པོ། ^2-33-1-0

[Block 2078]
སུན་འབྱིན་ཞེས་བྱ་སྤོང་བ་གཉེན་པོ་ནི་བར་ཆད་མེད་པའི་ལམ་མོ། །

[Block 2079 [HEADING]]
#### གཞི་གཉེན་པོ། ^2-33-2-0

[Block 2080]
གཞི་གཉེན་པོ་ནི་དེ་ཡན་ཆད་ཀྱི་ལམ་གང་ཡིན་པ་སྟེ། གང་གིས་དེས༌[^1524]ཐོབ་པའི་སྤོང་བ༌[^1525]ཀུན་དུ་འཛིན་པར་བྱེད་པའོ། །

[Block 2081 [HEADING]]
#### ཐག་བསྲིང་བའི་ངོ་བོའི་གཉེན་པོ། ^2-33-3-0

[Block 2082]
ཐག་བསྲིང་བའི༌[^1526]ངོ་བོའི༌[^1527]གཉེན་པོ་ནི༌[^1528]རྣམ་པར་གྲོལ་བའི་ལམ་ཡན་ཆད་ཀྱི་ལམ་གང་ཡིན་པ་སྟེ། རྙེད་པ་ཆད་པ་ཐག་བསྲིང་བའི༌[^1529]ཕྱིར་རོ། །

[Block 2083]
གཞན་དག་ན་རེ་རྣམ་པར་གྲོལ་བའི་ལམ་ཡང་ཡིན་ཏེ། དེས་ཀྱང་ཐོབ་པ་དེ་ཐག༌[^1530]སྲིང་བར་བྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 2084 [HEADING]]
#### རྣམ་པར་སུན་འབྱིན་པའི་གཉེན་པོ། ^2-33-4-0

[Block 2085]
རྣམ་པར་སུན་འབྱིན་པའི༌[^1531]གཉེན་པོ་ནི་ལམ་གང་གིས་ཁམས་དེ་ལ་སྐྱོན་དུ་མཐོང་ནས་རྣམ་པར་སུན་འབྱིན་པར་བྱེད་དོ།[^1532] །གཞན་ཡང་འདི་དག་གི་གོ་རིམས་རྣམ་པར་སུན་འབྱིན་པའི༌[^1533]གཉེན་པོ་ནི་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ༌[^1534]ལ་དམིགས་པ་སྦྱོར་བའི་ལམ་མོ། །

[Block 2086]
སྤོང་བ་གཉེན་པོ་ནི་བར་ཆད་མེད་པའི་ལམ་ཐམས་ཅད་དོ། །

[Block 2087]
གཞི་གཉེན་པོ་ནི་རྣམ་པར་གྲོལ་བའི་ལམ་མོ། །

[Block 2088]
ཐག་བསྲིང་བའི༌[^1535]ངོ་བོའི༌[^1536]གཉེན་པོ་ནི་ཁྱད་པར་གྱི་ལམ་མོ་ཞེས་བྱ་བ་འདི་ནི་ཆེས་ལེགས་པར་འགྱུར་རོ། །

[Block 2089 [HEADING]]
### ཉོན་མོངས་པ་གང་ལས་སྤང་བར་བྱ་བ། ^2-34-0

[Block 2090]
ཉོན་མོངས་པ་སྤོང་བ་ན་གང་ལས་སྤང་བར༌[^1537]བྱ་ཞེ་ན། དམིགས་པ་ལས་ཉོན་མོངས་པ་ནི་སྤང་བར༌[^1538]བྱར་འདོད། མཚུངས་པར་ལྡན་པ་ལས་ནི་ཉོན་མོངས་པ་རྣམ་པར་དབྱེ་བར་མི་ནུས་སོ། །

[Block 2091]
དམིགས་པ་ལས་ནི་ནུས་ཏེ། འདི་ལྟར་ཡང་དེ་ལ་དམིགས་ནས་མི་སྐྱེའོ། །

[Block 2092]
རེ་ཞིག་མ་འོངས་པ་ནི་དམིགས་པ་ལས་རྣམ་པར་དབྱེ་བར་ཡང་ནུས་གྲང་ན་འདས་པ་གོ་ཇི་ལྟར་ནུས། འོན་ཏེ་འདིའི་དོན་ནི་དམིགས་པ་ཡོངས་སུ་ཤེས་པས་སྤང་བར་བྱ་བ་འདི་ཡིན་ནོ་ཞེ་ན་དེ་ཡང་མ་ངེས་ཏེ། དེ་ལྟ་བས་ན་འདི་བརྗོད་པར་བྱ་དགོས་སོ། །

[Block 2093 [HEADING]]
### ཇི་ཙམ་གྱིས་ན་ཉོན་མོངས་པ་སྤངས་པ། ^2-35-0

[Block 2094]
ཇི་ཙམ་གྱིས་ན་ཉོན་མོངས་པ་སྤངས་པ་ཞེས་བརྗོད་ཅེ་ན་རང་གི་རྒྱུད་ལ་ཡོད་པ་ནི་ཐོབ་པ་ཆད་པས་སོ། །

[Block 2095]
གཞན་གྱི་རྒྱུད་ལ་ཡོད་པ་ནི༌[^1539]ཉོན་མོངས་པ་དང་། གཟུགས་མེད་པ༌[^1540]ཐམས་ཅད་དང་། ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་ཆོས་ནི་དེ་དག་ལ་དམིགས་པའི་ཉོན་མོངས་པ་རང་གི་རྒྱུད་ལ་ཡོད་པ་སྤངས་པའོ།[^1541] །ཐག་བསྲིང་བའི༌[^1542]ངོ་བོ་ཞེས་བྱ་བ་ཐག་བསྲིང་བའི་ངོ་བོ༌[^1543]རྣམ་པ་དུ་ཡོད་ཅེ་ན། ཐག་བསྲིང་བའི༌[^1544]ངོ་བོ་ནི་རྣམ་པ༌[^1545]བཞི་ཡོད་དོ་ཞེས་གྲག་སྟེ།

[Block 2096 [HEADING]]
### རིང་བ་ཉིད། ^2-36-0

[Block 2097 [VERSE]]
མཚན་ཉིད་མི་མཐུན་མི་མཐུན་ཕྱོགས། །
ཡུལ་རྣམས༌[^1546]ཆད་དང་དུས་ཀྱིས་ཏེ། །
འབྱུང་དང་ཚུལ་ཁྲིམས་ཕྱོགས་དང་ནི། །
དུས་གཉིས་རིང་བ་ཉིད་ལྟ་བུའོ། །

[Block 2098 [HEADING]]
#### མཚན་ཉིད་ཀྱིས་རིང་བ་ཉིད། ^2-36-1-0

[Block 2099]
མཚན་ཉིད་ཀྱིས་རིང་བ་ཉིད་ནི་དཔེར་ན་འབྱུང་བ་ཆེན་པོ་རྣམས་ལྷན་ཅིག་སྐྱེས་པ་ཡིན་ཡང་མཚན་ཉིད་མི་མཐུན་པས་རིང་བ་ཉིད་ལྟ་བུའོ། །

[Block 2100 [HEADING]]
#### གཉེན་པོས་རིང་བ་ཉིད། ^2-36-2-0

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
--- END BLOCKS ---
