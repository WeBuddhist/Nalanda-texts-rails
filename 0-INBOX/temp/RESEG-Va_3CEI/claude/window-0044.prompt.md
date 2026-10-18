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
ཡེ་ཤེས་འདི་ནི་དམ་པ་ངོ་མཚར་ཆེ། སེམས་ཅན་འདི་དག་མི་མཁས་གཏི་མུག་ལྡོངས། །ཞེས་བྱ་བ༌[^1357]ནི་ཐར་བར་བྱར་མི་རུང་བར་དགོངས་པ་སྟེ་རྒྱུ་རྣམ་བཞིའི་ཕྱིར་རོ། །

[Block 1542]
ཆོས་ཟབ་པས་ཤེས་པར་དཀའ་བ་དང་། དབང་པོ་རྟུལ་བས་ཤེས་པར་དཀའ་བ་དང་། འདོད་པ་ལ་ཆགས་པས་གཏོང་མི་ཕོད་པ་དང་། གཏི་མུག་གིས་ལྡོངས་པས་ཐར་བར་བྱར་མི་རུང་ངོ་སྙམ་དུ༌[^1358]དགོངས་སོ། །

[Block 1543]
མདོ་ལས།

[Block 1544 [HEADING]]
###### **ཐབས་ཙམ་དུ་བསྟན་པར་དགོངས་པ།** ^4-2-11-1-1-2-5-3-2-1-3-0

[Block 1545]
དེ་ཚེ་ང་ལ་གསོལ་བ་ཚངས་པ་དང་། །ཞེས་པ་ནས། ཐམས་ཅད་ཐལ་མོ་སྦྱར་ནས་གུས་པར་འཁོད། །ཅེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་ཕྱེད་དང་བཅུ་གཉིས་ཐབས་ཙམ་དུ་བསྟན་པར་དགོངས་པ་བསྟན་པ་སྟེ། དེ་ལ་ཡང་རྣམ་པ་བཞིའོ། །

[Block 1546]
དང་པོ་ནི་ཚིག་གཉིས་ཀྱིས་ནི་ལྷ་རྣམས་ཀྱི༌[^1359]ཆོས་བཤད་པར་གསོལ་བ་བཏབ་པ་བསྟན་ཏོ། །

[Block 1547]
ཚིག་གསུམ་གྱིས་ནི་དགོངས་པ་བསྟན་ཏོ། །

[Block 1548]
ཚིག་ཕྱེད་དང་ལྔས་ནི་སྐལ་བ༌[^1360]དང་ལྡན་པ་བསྟན་ཏོ། །

[Block 1549]
ཚིག་གཉིས་ཀྱིས་ནི་ཐབས་ཙམ་གྱིས་བསྟན་པ་བསྟན་ཏོ། །

[Block 1550 [HEADING]]
###### **ལྷ་རྣམས་ཀྱིས་ཆོས་བཤད་པར་གསོལ་བ་བཏབ་པ།** ^4-2-11-1-1-2-5-3-2-1-3-1-0

[Block 1551]
འདི་ནི་ཚངས་པའི་རྒྱལ་པོ་ལ་སོགས་པས་གསོལ་བ་བཏབ་ནས༌[^1361]ཐེག་པ་གསུམ་གྱི་ཆོས་བསྟན་པ་སྟེ་ཆོས་ཉིད་ཀྱིས་གསོལ་བ་མ་བཏབ་པར་ཆོས་མི་སྟོན་ཏོ། །

[Block 1552]
མདོ་ལས།

[Block 1553 [HEADING]]
###### **དགོངས་པ།** ^4-2-11-1-1-2-5-3-2-1-3-2-0

[Block 1554]
དོར༌[^1362]རྣམས་ཇི་ལྟར་བྱ་བར༌[^1363]རབ་ཏུ་བསམ། །ཞེས་པ་ནས། ང་དེང༌[^1364]ཞི་བར་མྱ་ངན་འདའ་བར་ཤོག །ཅེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིག་གསུམ་གྱིས་དགོངས་པ་བསྟན་པ་སྟེ། འདི་ལ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 1555]
ཚིག་གཉིས་ཀྱིས་ནི་ཐེག་པ་ཆེན་པོའི་སེམས་ཅན་ལ་གནོད་པར་འགྱུར་བ་བསྟན་ཏོ། །

[Block 1556]
ཚིགས་བཅད་གཅིག་གིས་ནི་ཐེག་པ་གསུམ་གྱི་སེམས་ཅན་ལ་ཕན་པར་འགྱུར་བ༌[^1365]བསྟན་པ་སྟེ། སེམས་ཅན་འདི་དག་སྡུག་བསྔལ་གྱིས་མངོན་སུམ་དུ་གཟིར་བས་ཁྱིམ་ནས་བྱུང་བ་ཡང་ཆོས་མ་ཡིན་པའི་སྡུག་བསྔལ་སྤྱོད་པས་དེ་དག་ལ་ཅིག་ཅར་ཐེག་པ་ཆེན་པོའི་ཆོས་བསྟན་ན་ཡིད་ཆེས་པར་མི་འགྱུར་ཏེ། བྱིས་པའི་བློ་ཅན་དག་སྐུར་བས་ངན་སོང་དུ་ལྷུང་བར་འགྱུར་ཏེ། ཁྱིམ་པ་རྣམས་ནི་སྡུག་བསྔལ་གྱིས་གཟིར་བས་ཡིད་ཆེས་པར་མི་འགྱུར། རབ་ཏུ་བྱུང་བ་ཕྱི་རོལ་པ་རྣམས་ནི་ཆོས་བཤད་པས་ཡིད་མི་ཆེས་ཏེ། དེ་བས་ན་ཆོས་མ་བཤད་པར་མྱུར་དུ་མྱ་ངན་ལས་འདས་ཀྱང་སླའོ་སྙམ་དགོངས་སོ། །

[Block 1557]
མདོ་ལས།

[Block 1558]
མངོན་པ་ན༌[^1366]དགའ་བ་སྔོན་གྱི་སངས་རྒྱས་དང་། །ཞེས་པ་ནས། རྣམ་པ་གསུམ་དུ་ཕྱེ་སྟེ་རབ་ཏུ་བཤད། །ཅེས་པའི་བར་དུ་ནི་ཐེག་པ་གསུམ་གྱིས༌[^1367]སེམས་ཅན་ལ་ཕན་པ་སྟེ། སངས་རྒྱས་རྣམས་དང་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1559]
མདོ་ལས།

[Block 1560 [HEADING]]
###### **སྐལ་བ་དང་ལྡན་པ།** ^4-2-11-1-1-2-5-3-2-1-3-3-0

[Block 1561]
ང་ཡིས་དོན་དེ་དེ་ལྟར་བསམས་པ་ནི། །ཞེས་པ་ནས། འཇིག་རྟེན་འདྲེན་པ་རྣམས་ཀྱི་རྗེས་ཐོབ་པ། །ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིག་ཕྱེད་དང་ལྔས་ནི་སྐལ་བ༌[^1368]དང་ལྡན་པ་ལ་འདུལ་བར་འགྱུར་བ་བསྟན་པ་སྟེ། ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་ད་ལྟར་གྱི་སངས་རྒྱས་བསྔགས་པ་བསྟན་པའོ། །

[Block 1562]
ཚིག་ཕྱེད་ཀྱིས་ནི་སངས་རྒྱས་རྣམས་དང་མཐུན་པ་བསྟན་ཏོ། །

[Block 1563]
ཚིག་ཕྱེད་དང་གསུམ་གྱིས་ནི་ཕྱི་མ་བདེན་གྱི་སྔ་མ་ཐབས་ཙམ་དུ་བསྟན་ཏོ་ཞེས་དབང་དུ་འགྱུར་བ༌[^1369]བསྟན་ཏོ། །

[Block 1564]
མདོ་ལས།

[Block 1565]
ངས༌[^1370]ཀྱང་དམ་པའི་གནས་རིག་དེ་ཡི་ཚེ། རྣམ་པ་གསུམ་དུ་ཕྱེ་སྟེ་རབ་ཏུ༌[^1371]བཤད། །ཅེས་པ་ནི་བདག་དཔང་དུ་འགྱུར་བ་བསྟན་ཏེ།[^1372] ཐབས་ཙམ་དུ་ཐེག་པ་གསུམ་བཤད་ཅེས་པའི་དོན་ཏོ། །

[Block 1566]
མདོ་ལས།

[Block 1567]
མཁས་པ་མ་ཡིན་དད་པ་ཆུང་བའི་མི། །ཞེས་པ་ནས། བྱང་ཆུབ་སེམས་དཔའ་མང་པོ་གཟུད་པར༌[^1373]བྱ། །ཞེས་པའི་བར་དུ་ནི་བྱིས་པའི་བློ་ཅན་དད་པ་ཆུང་བ་དག་ཆུང་ངུ་ལ་མོས་པས་འཚང་རྒྱ་བར་འགྱུར་བའི་དོན་ཆེན་པོ་ལ་ཡིད་མི་ཆེས་པས་སྔར་ཐེག་པ་གསུམ་ཐབས་ཙམ་དུ་བསྟན་པ་སྟེ།[^1374] བྱང་ཆུབ་སེམས་དཔའ་གཟུད་པར༌[^1375]བྱེད་དོ། །

[Block 1568]
མདོ་ལས།

[Block 1569 [HEADING]]
###### **ཐབས་ཙམ་གྱིས་བསྟན་པ།** ^4-2-11-1-1-2-5-3-2-1-3-4-0

[Block 1570]
དེ་ཡི་སྒྲ་ཐོས་པ་ནི་དགའ་གྱུར་པ།[^1376] །ཞེས་པ་ནས། དྲང་སྲོང་ཆེ་མཆོག་གདོན་མི་ཟ་བ་གསུང་། །ཞེས་པའི་བར་ཚིགས་བཅད་གཉིས་ཀྱིས་ཐབས་ཙམ་དུ་འདྲེན་པ་བསྟན་པ་སྟེ། སྒྲ་ཐོས་ཏེ་དགའ་བས་བསྟོད་པ་དང་དེའི་རྗེས་སུ་སྤྱོད་པ་དགོངས་པ་བསྟན་པའོ། །

[Block 1571]
མདོ་ལས།

[Block 1572]
བདག་ཀྱང་དེ་བཞིན་ཀུན་ཏུ་སྤྱད་པ་ནི། །ཞེས་པ་ནས། སེམས་ཅན་རྙོག་པ་ཅན་གྱི་ནང་དུ་སྐྱེས། །ཞེས་པའི་བར་དུ༌[^1377]ནི་རྗེས་སུ་སྤྱོད་པ་བསྟན་བར་དགོངས་པ་སྟེ། སྐལ་བ་དང་ལྡན་པ་ལ་རྙོག་པ་ཅན་གྱི་ནང་དུ་སྐྱེས་ཀྱང་དེའི་རྗེས་སུ་སྤྱོད་པ་དགོངས་པའོ། །

[Block 1573 [HEADING]]
###### **ཐེག་པ་གསུམ་སྤྲུལ་པ།** ^4-2-11-1-1-2-5-3-2-1-4-0

[Block 1574]
མདོ་ལས་དེ་ལྟར་ང་ཞེས་པ༌[^1378]ནས་ནི་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་ཐབས་ཀྱིས༌[^1379]རབ་ཏུ་ཞི་བའི་ཆོས་བཤད་ཅེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་ཕྱེད་དང་བཞིས་ཐེག་པ་གསུམ་སྤྲུལ་པར་ཡང་དག་པར་བསྟན་པ་སྟེ། དེ་ལ་རྣམ་པ་གསུམ་མོ། །

[Block 1575]
ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་ཐབས་ཙམ་དུ་བསྟན་ཏོ། །

[Block 1576]
[^1380]གཅིག་གིས་ནི་དཀོན་མཆོག་གསུམ་བྱུང་བ་བསྟན་ཏོ། །

[Block 1577]
ཚིག་གཅིག་གིས་ནི་ད་ལྟར་དང་འདས་པ་གྲུབ་པ་བསྟན་ཏོ། །

[Block 1578 [HEADING]]
###### **ཐབས་ཙམ་དུ་བསྟན་པ།** ^4-2-11-1-1-2-5-3-2-1-4-1-0

[Block 1579]
[^1381]བཱ་རཱ་ཎ་སཱིར་ནི་རི་དགས་ལ་མི་འཇིགས་པ་བྱིན་པའི་གནས་སོ། །

[Block 1580]
གནས་དེར་ཐོག་མར་རྟེན༌[^1382]ལྔ་པོ་ལ་ཆོས་བསྟན་ཏེ་ཐབས་ཀྱིས་རབ་ཏུ་ཞི་བའི་ཆོས་བསྟན་ཏོ། །
--- END BLOCKS ---
