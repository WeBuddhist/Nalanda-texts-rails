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
[Block 1471]
ཐེག་པ་གཅིག་ནི་ཡོངས་སུ་རྫོགས་པའི་མཚན་ཉིད་ལ་བྱ་སྟེ་སྔར་བཤད་པ་བཞིན་ནོ། །

[Block 1472]
ཆོས་ཀྱི་གནས་ཉིད་ནི་ཆོས་ཐམས་ཅད་ལ་ཡང་དག་པར་གནས་པས་ཆོས་ཀྱི་གནས་ཉིད་དོ། །

[Block 1473]
ཆོས་ལ་ཉོན་མོངས་པ་དང་། རྣམ་པར་དག་པ་ཡོད་དེ་ཉོན་མོངས་པ་སྤངས་ནས་རྣམ་པ་ཐོབ་པ་ནི་ཆོས་མི་འགྱུར་པ་ཉིད་དོ། །

[Block 1474]
ཡང་དག་པའི་མཚན་ཉིད་རྟག་ཏུ་གནས་པས་མི་གཡོ་བར་གནས་པའོ། །

[Block 1475]
སྙིང་པོ་བྱང་ཆུབ་ལ་བཞུགས་ཤིང་ཆོས་ཐམས་ཅད་ལ་ཐབས་མཁས་པས་ཤིན་ཏུ་སྟོན་ཏོ། །

[Block 1476]
ཆོས་ཐམས་ཅད་ལ་རྣམ་པ་གཉིས་ཏེ་སྟོང་པ་ཉིད་དང་ཡོད་པ་ཉིད་དོ། །

[Block 1477]
སྟོང་པ་ལ་ཁྱད་པར་མེད་པས་མཚན་ཉིད་གཅིག་སྟེ། ཀུན་ཏུ་རྟོག་པ་ཞེས་བྱའོ། །

[Block 1478]
ཡོད་པ་ལ་ཁྱད་པར་ཡོད་དེ་རྣམ་པ་གཉིས་སོ། །

[Block 1479]
རྟག་པ་དང་མི་རྟག་པ་སྟེ་རྟག་པ་ནི་ཡོངས་སུ་རྫོགས་པའི་མཚན་ཉིད་དོ། །

[Block 1480]
མི་རྟག་པ་ནི་གཞན་གྱི་དབང་ལས་ཀྱི་མཚན་ཉིད་དོ། །

[Block 1481]
དེ་ལ་ཡང་གཉིས་ཏེ་ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པའོ། །

[Block 1482]
ཟག་པ་དང་བཅས་པ་ནི་གཞན་གྱི་དབང་ལས་མཚན་ཉིད་དོ། །

[Block 1483]
ཟག་པ་མེད་པ་ནི་ཡོངས་སུ་རྫོགས་པའི་མཚན་ཉིད་དེ། དེ་བས་ན་ཡོངས་སུ་རྫོགས་པའི་མཚན་ཉིད་ཀྱི་དབང་དུ་བྱས་ཏེ།[^1321] དེ་ལ་ཐེག་པ་གཅིག་ཅེས་བྱའོ། །

[Block 1484]
ཐེག་པ་གཅིག་གིས་ཡང་དག་པ་ཉིད་རིག་པས་ཆོས་ཀྱི་གནས་ཉིད་དང་ཆོས་མི་འགྱུར་བ་ཉིད་དེ། དེ་ལ་མི་གཡོ་བར་གནས་ནས་སེམས་ཅན་ལ་ཐབས་མཁས་པས་ཆོས་སྟོན་ཏོ། །

[Block 1485]
མདོ་ལས།

[Block 1486 [HEADING]]
###### **ད་ལྟར།** ^4-2-11-1-1-2-5-2-3-0

[Block 1487]
ལྷ་མི་ཀུན་གྱི་མཆོད་པ་ཕྱོགས་བཅུ་ན། །ཞེས་པ་ནས། དེ་དག་རྣམས་ཀྱང་ཐེག་པ༌[^1322]མཆོག་འདི་འཆད། །ཅེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་ཕྱེད་དང་ལྔས་ད་ལྟར་གྱི་དོན༌[^1323]སྟོན་ཏོ། །

[Block 1488]
མདོ་ལས།

[Block 1489]
ཐབས་ལ༌[^1324]མཁས་པས༌[^1325]རབ་ཏུ་འཆད་པ་དང་། །ཞེས་པ་ནས། དད་པ་ཞི་བའི་ས་འདི་རིག་ནས་སོ། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1326]ནི་སྔར་ཐབས་ཙམ་བསྟན་པ༌[^1327]ལ་ཕྱིས་ཡང་དག་པར༌[^1328]བསྟན་པའོ། །

[Block 1490]
མདོ་ལས།

[Block 1491]
ལུས་ཅན་ཀུན་གྱི་སྤྱོད་པ་རིག་པ་དང་། །ཞེས་པ་ནས། སྣ་ཚོགས་མངོན་པར་བསྒྲུབ་པ་རབ་ཏུ་བསྟན། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1329]ནི་ཅིའི་ཕྱིར་སྔར་ཐབས་ཙམ་བསྟན་ལ་ཕྱིས་ཡང་དག་པ་བསྟན་པ་ཉིད་སྟོན་པ་སྟེ། ལུས་ཅན་ཀུན་གྱི་སྤྱོད་པ་ནི་སེམས་ཀྱི་སྤྱོད་པའི་མཚན་ཉིད་དོ། །

[Block 1492]
ཅི་བསམས་པ་ནི་ཀུན་ཏུ་འགྲོ་བའི་མཚན་ཉིད་དོ། །

[Block 1493]
མཐུ་ནི་ལས་ཀྱི་མཐུའོ། །

[Block 1494]
སྟོབས་ཞེས་ཀྱང་བྱ་སྟེ་སེམས་ཅན་གྱི་དབང་པོ་སྣ་ཚོགས་ཤེས་པའི་སྟོབས་སོ། །

[Block 1495]
བརྩོན་འགྲུས་ནི་གནས་དང་གནས་མ་ཡིན་པའི་སྟོབས་སོ། །

[Block 1496]
དེ་ལྟར་སེམས་ཅན་གྱི་དད་པ་རིག་ནས༌[^1330]དཔེ་དང་གཞི༌[^1331]རྣམ་པ་མང་པོ་སེམས་ཅན་གྱི་དབང་པོ་བཞིན་དུ་སྣ་ཚོགས་མངོན་པ་སྟོན་ཏེ། མ་བྱོན་པའི་སངས་རྒྱས་རྣམས་ཀྱང་མཚན་ཉིད་གསུམ་རིག་པར་འགྱུར་རོ། །

[Block 1497]
ད་ལྟར་བཞུགས་པ་ཡང་སེམས་ཅན་གྱི་དབང་པོ་མཁྱེན་པས་སྔར་ཐབས་ཙམ་བསྟན་ནས་ཕྱིས་ཡང་དག་པར༌[^1332]སྟོན་ཏོ། །

[Block 1498]
མདོ་ལས།

[Block 1499 [HEADING]]
###### **ང་ཡང་དེ་བཞིན་ནོ་ཞེས་པ།** ^4-2-11-1-1-2-5-3-0

[Block 1500 [HEADING]]
###### **དངོས་སུ་དམིགས་ཏེ་བསྟན་པ།** ^4-2-11-1-1-2-5-3-1-0

[Block 1501]
འདྲེན་པའི་དབང་པོ་རྒྱལ་བ་ང་ཡང་འདིར། །ཞེས་པ་ནས། དེ་ནི་ང་ཡི་རང་རིག་ཡེ་ཤེས་སྟོབས། །ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་སུམ་ཅུས་ང་ཡང་དེ་བཞིན་ནོ་ཞེས་པ་བསྟན་པ་སྟེ། དེ་ལ་ཚིགས་བཅད་གཉིས་ཀྱིས་དངོས་སུ་དམིགས་ཏེ་བསྟན་ཏོ། །

[Block 1502]
ཉི་ཤུ་རྩ་བརྒྱད་ཀྱིས་ནི་རྒྱས་པར་བསྟན་ཏོ། །

[Block 1503]
མདོ་ལས།

[Block 1504 [HEADING]]
###### **རྒྱས་པར་བསྟན་པ།** ^4-2-11-1-1-2-5-3-2-0

[Block 1505]
ང་ཡིས་མཐོང་བའི་སེམས་ཅན་དབུལ་པོ་རྣམས། །ཞེས་པ་ནས། འདོད་པས་འདི་དག་རྟག་ཏུ་ལྡོངས་པར་བྱས། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1333]ནི་རྒྱས་པར་བསྟན་པ་སྟེ། ཐོག་མའི་ཚིག་ཉི་ཤུ་རྩ་ཕྱེད་དང་གཅིག་གིས་ནི་སྔར་ཐེག་པ་གསུམ་ཐབས་ཙམ་དུ་བསྟན་པ་སྟེ། ཚིག་རྐྱང་པ་ལས་སེམས་ཅན་གྱི་མོས་པ་སྣ་ཚོགས་མཁྱེན་ནོ་ཞེས་བསྟན་པའོ། །

[Block 1506]
ཚིགས་བཅད་བདུན་གྱིས་ནི་ད་ལྟར་ཡང་དག་པ་ཉིད་དུ་བསྟན་པ་བརྗོད་དེ།[^1334] སྔར་སངས་རྒྱས་ཀྱི་ཐེག་པ་གཅིག་པུ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་བསྟན་པའོ། །

[Block 1507 [HEADING]]
###### **སྔར་ཐེག་པ་གསུམ་ཐབས་ཙམ་དུ་བསྟན་པ།** ^4-2-11-1-1-2-5-3-2-1-0

[Block 1508]
སྔ་མ་ལ་ཡང་རྣམ་པ་བཞི་སྟེ་ཚིགས་བཅད་ཕྱེད་དང་བཞིས་ནི་སྐྱེ་བའི་གནས་སུ་བགེགས་ལས་ཐར་བར་བྱ་བ་བསྟན་ཏོ། །

[Block 1509]
ཚིགས༌[^1335]གསུམ་གྱིས་ནི༌[^1336]གྲོལ་བར་བྱ་བར་མི་ནུས་པ་སེམས་པ་བསྟན་པའོ། །

[Block 1510]
ཚིག་ཕྱེད་དང་བཅུ་གཉིས་ཀྱིས་ནི་ཐབས་ཙམ་དུ་བསྟན་པར་དགོངས་སོ། །
--- END BLOCKS ---
