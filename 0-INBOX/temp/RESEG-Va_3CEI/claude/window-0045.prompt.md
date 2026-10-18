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

[Block 1581]
མདོ་ལས།

[Block 1582 [HEADING]]
###### **དཀོན་མཆོག་གསུམ་བྱུང་བ།** ^4-2-11-1-1-2-5-3-2-1-4-2-0

[Block 1583]
དེ་ནས་ང་ནི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར། །ཞེས་པ་ནས།[^1383] དེར་ནི་དགེ་འདུན་སྒྲ་ཡང་དེ་བཞིན་བྱུང་། །ཞེས་པའི་བར་དུ་ནི་དཀོན་མཆོག་གསུམ་བྱུང་བ་བསྟན་པ་སྟེ། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་ནི་ལན་གསུམ་དུ་ཚུལ་བཅུ་གཉིས་ཀྱིས༌[^1384]བསྐོར་བའོ། །

[Block 1584]
འཁོར་ལོ་ཞེས་བྱ་བ་ནི་འཁོར་ཅིང་མི་གནས་པའི་དོན་ཏོ། །

[Block 1585]
འཕགས་པའི་ལམ་གྱི་ཡན་ལག་བརྒྱད་དང་ཅི་རིགས་སུ་སྦྱར་རོ། །

[Block 1586]
འཕགས་པའི་ལམ་བསྟན་པས་ཕ་རོལ་འབྲས་བུ་ཐོབ་པས་བསྐོར་བ་ཞེས་བྱའོ། །

[Block 1587]
དེ་ལྟར་འཕགས་པའི་ལམ་འཇིག་རྟེན་དུ་བྱུང་བས་དཀོན་མཆོག་གསུམ་གྱི་སྒྲ་ཡང་འཇིག་རྟེན་དུ་བྱུང་བར་གྱུར་ཏོ། །

[Block 1588]
སངས་རྒྱས་ཉིད་ནི་སངས་རྒྱས་དཀོན་མཆོག་མྱ་ངན་ལས་འདས་པ་དང་། འབྲས་བུ་དང་ཆོས་བསྟན་པ་ནི་ཆོས་དཀོན་མཆོག་གོ། །

[Block 1589]
རྟེན་ལྔ་ལ་སོགས་པ་ནི་དགེ་འདུན་དཀོན་མཆོག་གོ། །

[Block 1590]
མདོ་ལས།

[Block 1591 [HEADING]]
###### **ད་ལྟར་དང་འདས་པ་གྲུབ་པ།** ^4-2-11-1-1-2-5-3-2-1-4-3-0

[Block 1592]
ལོ་ཡི་གྲངས་ནི་མི་ཉུང་བར་ཡང་བཤད། །ཅེས་པ་ནས། དེ་བཞིན་རྟག་པར་དུས་གསུམ༌[^1385]ངས་སྨྲས་སོ། །ཞེས་པའི་བར་དུ་ད་ལྟར་དང་སྔོན་ཡང་གྲུབ་པ༌[^1386]བསྟན་པ་སྟེ། ད་ལྟར༌[^1387]གྱི་དུས་འདི་འབའ་ཞིག་ཏུ་མྱ་ངན་ལས་འདའ་བ༌[^1388]བསྟན་པ་མ་ཡིན་གྱི་ལོའི་གྲངས་མི་ཉུང་བར་སྡུག་བསྔལ་གྱི་མཐའ་ཟད་ཀྱི་བར་དུ་བཤད་ཅིང་བསྟན་ཏོ། །

[Block 1593]
མདོ་ལས།

[Block 1594 [HEADING]]
###### **ད་ལྟར་ཡང་དག་པ་ཉིད་དུ་བསྟན་པ།** ^4-2-11-1-1-2-5-3-2-2-0

[Block 1595]
ང་ནི་དེ་ཡི་ཚེ་ན་ཤཱ་རིའི་བུ། །ཞེས་པ་ནས། ཐབས་ལ་མཁས་པ་རྣམ་པ་མང་པོའོ། །ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་བདུན་གྱིས་ཆོས་འདི་བཤད་པས་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པོ་ཞེས་བསྟན་པ་སྟེ། འདི་ལ་ཡང་རྣམ་པ་བཞིའོ། །

[Block 1596]
ཐོག་མའི་ཚིག་གཉིས་ཀྱིས་ནི་དབང་པོ་སྨིན་པས་ཕྲད་པ་བསྟན་ཏོ། །

[Block 1597]
ཚིག་གཅིག་གིས་ནི་དོན་བྱ་བར་དགོངས་པ༌[^1389]བསྟན་ཏོ། །

[Block 1598]
ཚིག་གསུམ་གྱིས་ནི་ཡང་དག་པར་བཤད་པ་བསྟན་ཏོ། །

[Block 1599]
ཚིག་གཅིག་གིས་ནི་ཆོས་ཀྱི་དོན་བསྟན་ཏོ། །

[Block 1600 [HEADING]]
###### **དབང་པོ་སྨིན་པས་ཕྲད་པ།** ^4-2-11-1-1-2-5-3-2-2-1-0

[Block 1601]
ངས་ཐབས་ཙམ་དུ་བསྟན་པ་ཡང་སྔོན་གྱི་རྒྱལ་བ་དག་ལས་ཐབས་ཙམ་དུ་བསྟན་པ་ཐོས་པས་དགེ་བའི་རྩ་བ་དང་ལྡན་ཞིང་ང་དང་ཕྲད་པ་ལས་ཆོས་བཤད་པར་དགོངས་པ་བསྟན་པའོ།[^1390]

[Block 1602]
།མདོ་ལས།

[Block 1603 [HEADING]]
###### **དོན་བྱ་བར་དགོངས་པ།** ^4-2-11-1-1-2-5-3-2-2-2-0

[Block 1604]
དེ་མ་ཐག་ཏུ་ངས་ནི་འདི་སྙམ་བསམ། །ཞེས་པ་ནས། བྱང་ཆུབ་མཆོག་དེ་འདིར་ནི་རབ་ཏུ་བཤད། །ཅེས་པའི་བར་དུ་དོན་བྱ་བར་དགོངས་པ་བསྟན་པ་སྟེ། དབང་པོ་སྨིན་པ་རྣམས་ལ་སངས་རྒྱས༌[^1391]ཡེ་ཤེས་བཤད་དེ་བྱང་ཆུབ་མཆོག་ལ་ཅི་ཕྱིར༌[^1392]དགོངས་པར༌[^1393]མི་བྱ་སྙམ་དགོངས་ཏེ། དུས་ལ་བབ་པར་བསྟན་པའོ། །

[Block 1605]
མདོ་ལས།

[Block 1606 [HEADING]]
###### **ཡང་དག་པར་བཤད་པ།** ^4-2-11-1-1-2-5-3-2-2-3-0

[Block 1607]
དེ་རིང་འདི་ལ་དད་པར་དཀའ་བ་ནི། །ཞེས་པ་ནས། མི་མཁས་པ་དང་ང་རྒྱལ་ལྡན་པའོ། །ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་གསུམ་གྱིས་ཡང་དག་པར་བཤད་པ་བསྟན་པ་སྟེ། དེ་ལ་ཚིག་གཅིག་གིས་ནི་མི་མཁས་པ་བྱིས་པའི་བློ་ཅན་འཛིན་མི་ནུས་པ་བསྟན་ཏོ། །

[Block 1608]
ཚིག་གཉིས་ཀྱིས་ནི་དབང་པོ་རྣོན་པོ་བློ་དང་ལྡན་པས་འཛིན་ནུས་པ་བསྟན་ཏོ། །

[Block 1609 [HEADING]]
###### **འཛིན་མི་ནུས་པ།** ^4-2-11-1-1-2-5-3-2-2-3-1-0

[Block 1610]
ཆོས་འཛིན་མི་ནུས་པའི་སྐྱོན་རྣམ་པ་ལྔ་སྟེ། དབང་པོ་རྟུལ་པོས་ཆོས་ཐོས་ཀྱང་དོན་མི་གོ་བ་དང་། བྱིས་པའི་བློ་ཅན་ཤེས་པ་ཆུང་བ་དང་། མཚན་མར་འདུ་ཤེས་པ་སྟེང་པ་དང་། ཡོད་པའི་མཚན་མ་གཉིས་སུ་འཛིན་པ་དང་། ང་རྒྱལ་ཅན་ལོངས་སྤྱོད་ཀྱིས་རྒྱགས་པ་དང་དྲེགས་པ་མི་མཁས་པས་ཉོན་མོངས་པ་དང་བཅས་པའོ། །

[Block 1611]
མདོ་ལས།

[Block 1612 [HEADING]]
###### **འཛིན་ནུས་པ།** ^4-2-11-1-1-2-5-3-2-2-3-2-0

[Block 1613]
དེ་ལ་ང་ཡང་འཇིགས་མེད་རབ་ཏུ་དགའ། །ཞེས་པ་ནས། འདི་དག་ཐམས་ཅད་འཇིག་རྟེན་སངས་རྒྱས་འགྱུར། །ཞེས་པའི༌[^1394]བར་དུ་འཛིན་ནུས་པ་བསྟན་པ་སྟེ། དགའ་བ་ནི་དགའ་བ་ཚད་མེད་པས་སེམས་ཅན་འཚང་རྒྱ་བ་ལ་ཕྲག་དོག་མེད་པའོ། །

[Block 1614]
འཇིགས་པ་མེད་པ་ནི་གདོན་མི་ཟ་བའི་དོན་ནི༌[^1395]སེང་གེའི་སྒྲ་སྒྲོགས་པ་ལ་གདོན་མི་ཟ་བའོ། །

[Block 1615]
རྣམ་པ༌[^1396]ཀུན་སྤངས་པ་ནི་ཐབས་ཙམ་དུ་གསུམ་དུ་བསྟན་པའོ། །
--- END BLOCKS ---
