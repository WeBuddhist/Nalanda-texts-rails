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
[Block 1366 [HEADING]]
###### **ཐབས་ཙམ་བསྟན་ནས་ཕྱིས་ཡང་དག་པ་བསྟན་པ།** ^4-2-11-1-1-2-5-2-1-1-0

[Block 1367 [HEADING]]
###### **སངས་རྒྱས་མང་བ།** ^4-2-11-1-1-2-5-2-1-1-1-0

[Block 1368]
སྔ་མ་ལ་ཡང་བཞི་སྟེ། ཚིག་གཅིག་གིས་ནི་སངས་རྒྱས་མང་བ་བསྟན་ཏོ། །

[Block 1369]
ཚིག་གཅིག་གིས༌[^1261]ནི་ཐབས་ཙམ་བསྟན་ཏོ། །

[Block 1370]
ཚིག་གཅིག་གིས་ནི་ཡང་དག་པར་བསྟན་ཏོ། །

[Block 1371]
ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་ཅིའི་ཕྱིར་ཐབས་དང་ཡང་དག་པ་བསྟན་པ་བརྗོད་དོ། །

[Block 1372]
མདོ་ལས།

[Block 1373 [HEADING]]
###### **ཐབས་ཙམ་དུ་བསྟན་པ།** ^4-2-11-1-1-2-5-2-1-1-2-0

[Block 1374]
སྐྱེས་བུ་དམ་པ་དེ་དག་ཐམས་ཅད་ཀྱི། །ཞེས་པ་ནས། ཐབས་ལ་མཁས་པ་བརྒྱ་ཕྲག་དུ་མ་ཡིས། །ཞེས་པའི་བར་དུ་ནི་ཐབས་ཙམ་དུ་བསྟན་པ་བརྗོད་པའོ། །

[Block 1375]
མདོ་ལས།

[Block 1376 [HEADING]]
###### **ཡང་དག་པ་བསྟན་པ།** ^4-2-11-1-1-2-5-2-1-1-3-0

[Block 1377]
དེ་དག་ཀུན་གྱི་ཐེག་པ་གཅིག་ཏུ་བསྟན། །ཞེས་པ་ནས། །སྲོག་ཆགས་དུ་མ་བསམ་གྱིས་མི་ཁྱབ་རྣམས། །ཞེས་པའི་བར་དུ་ནི་ཡང་དག་པ་བསྟན་པའོ། །

[Block 1378]
མདོ་ལས།

[Block 1379 [HEADING]]
###### **ཅིའི་ཕྱིར་ཐབས་དང་ཡང་དག་པ་བསྟན་པ།** ^4-2-11-1-1-2-5-2-1-1-4-0

[Block 1380]
རྒྱལ་བའི་ཐབས་གཞན་རྣམ་པ་ཐ་དད་པས། །ཞེས་པ་ནས། དེ་བཞིན་གཤེགས་པས་འཇིག་རྟེན་ལྷར་བཅས་ལ།[^1262] །ཞེས་པའི་བར་དུ་ནི་ཅིའི་ཕྱིར་རྒྱལ་བས་ཐབས་ཙམ་བསྟན་པ་དང་། ཡང་དག་པ་བསྟན་པ་བརྗོད་པ་སྟེ། སེམས་ཅན་མང་པོ་ཅིག་ཅར་ཐེག་པ་གཅིག་ལ་འཇུག་མི་ནུས་ཏེ་དེ་བས་ན་དབང་པོ་དང་སྦྱར་ཏེ། སྔར་ཐབས་རྣམ་པ་ཐ་དད་པ་བསྟན་ཏེ། ཕྱིས་ཐེག་པ་གཅིག་ཏུ་བསྟན་ཏོ། །

[Block 1381]
མདོ་ལས།

[Block 1382 [HEADING]]
###### **སེམས་ཅན་རྣམས་ཆོས་ཐོས་ནས་མཐར་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པ།** ^4-2-11-1-1-2-5-2-1-2-0

[Block 1383]
སེམས་ཅན་གང་གིས༌[^1263]དེ་ལ་མངོན་སུམ་དེར། །ཞེས་པ་ནས། །དེ་དག་ཐམས་ཅད་བྱང་ཆུབ་ཐོབ་པར༌[^1264]འགྱུར། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིག་ཉི་ཤུ་རྩ་གསུམ་གྱིས་སེམས་ཅན་མང་པོ་ཆོས་ཐོས་ནས་མཐར་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་བསྟན་པ་སྟེ། དེ་ལ་ཡང་རྣམ་པ་གསུམ་མོ། །

[Block 1384]
ཐོག་མའི་ཚིག་གཉིས་ཀྱིས་ནི་སངས་རྒྱས་ད་ལྟར༌[^1265]བཞུགས་པ་བརྗོད་དོ། །

[Block 1385]
ཚིག་ཉི་ཤུས་ནི་འདས་པའི་སངས་རྒྱས་བརྗོད་དོ། །

[Block 1386]
ཚིག་གཅིག་གིས་ནི་བསྡུ་བ་བསྟན་ཏོ། །

[Block 1387 [HEADING]]
###### **སངས་རྒྱས་ད་ལྟར་བཞུགས་པ།** ^4-2-11-1-1-2-5-2-1-2-1-0

[Block 1388]
འདི་ནི་ཐོག་མ་སྟེ་སངས་རྒྱས་དང་ཕྲད་ནས་ཆོས་ཐོས་པས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དང་བསྡུ་བ་བཞི་ལ་སོགས་པ་ནི་བསོད་ནམས་རྣམ་པ་ཐ་དད་པ་ཞེས་བྱ་སྟེ། སངས་རྒྱས་ཀྱི་རྒྱུར་འགྱུར་བ་བསྒོམ་ཞིང་བྱང་ཆུབ་སེམས་དཔའི་སྤྱད་པ་སྤྱོད་པས་དེ་དག་ཐམས་ཅད་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1389]
མདོ་ལས།

[Block 1390 [HEADING]]
###### **འདས་པའི་སངས་རྒྱས།** ^4-2-11-1-1-2-5-2-1-2-2-0

[Block 1391]
མྱ་ངན་ལས་འདས་རྒྱལ་བ་དེ་དག་གི། །ཞེས་པ་ནས། །དེ་དག་ཐམས་ཅད་བྱང་ཆུབ་ཐོབ་པར༌[^1266]འགྱུར། །ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས༌[^1267]བཅད་ཉི་ཤུས་སངས་རྒྱས་འདས་པ་བསྟན་པ་སྟེ།[^1268] དེ་ལ་རྣམ་པ་ལྔའོ། །

[Block 1392]
ཚིག་གཅིག་གིས་ནི་བྱང་ཆུབ་སེམས་དཔའ་བསྟན་ཏོ། །

[Block 1393]
ཚིག་གཅིག༌[^1269]གིས་ནི་བྱམས་པ་བསྟན་ཏོ། །

[Block 1394]
ཚིག་ཕྱེད་དང་ལྔས༌[^1270]ནི་མཆོད་རྟེན་བྱས་པ་བསྟན་ཏོ།[^1271] །ཚིག་ཕྱེད་དང་བདུན་གྱིས་ནི་སྐུ་གཟུགས་བྱས་པ་བསྟན་ཏོ། །

[Block 1395]
ཚིག་བདུན་གྱིས་མཆོད་པ་བྱས་པ་བསྟན་ཏོ། །

[Block 1396]
ཚིག་གཅིག་གིས་ནི་སངས་རྒྱས་བརྗོད་པ་བསྟན་ཏོ། །

[Block 1397 [HEADING]]
###### **བྱང་ཆུབ་སེམས་དཔའ།** ^4-2-11-1-1-2-5-2-1-2-2-1-0

[Block 1398]
འདི་ནི་ཐོག་མ་སྟེ། བཟོད་ཀྱང་ཞི་ལ་དུལ་བ་མེད་དམ། ཞི་ལ་དུལ་ཡང་བཟོད་པ་མེད་ན་བྱང་ཆུབ་ཀྱི་སེམས་ཞེས་མི་བྱ་སྟེ། གང་བཟོད་ཅིང་ཞི་ལ་དུལ་བ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ཞེས་བྱ་སྟེ། ཚུལ་བཞིན་དུ་ཕན་པའི་དོན་དུ་འགྱུར་བ༌[^1272]ལ་རབ་ཏུ་ཞི་ཞིང་དུལ་ན་དེ་དག་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1399]
འདིའང་སངས་རྒྱས་མྱ་ངན་ལས་འདས་ནས་ཕྱི་མ་གདུལ་དཀའ་བ་རྣམས་ཀྱི་སྤྱོད་པ་ཡིན་གྱི་སངས་རྒྱས་བཞུགས་པའི་ཚེ་སྤྱོད་པ་འདིས་རྒྱུར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1400]
ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ཀྱང་སངས་རྒྱས་མྱ་ངན་ལས་འདས་ནས་ཐུན་མོང་དུ་སྤྱོད་པ་ཡིན་ཏེ། དེ་དག་ཀྱང་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1401]
མདོ་ལས།

[Block 1402 [HEADING]]
###### **མཆོད་རྟེན་བྱས་པ།** ^4-2-11-1-1-2-5-2-1-2-2-2-0

[Block 1403]
གང་གིས་རིང་བསྲེལ༌[^1273]ལ་ནི་མཆོད་བྱེད་པ། །ཞེས་པ་ནས། །དེ་དག་གིས་ཀྱང་བྱང་ཆུབ་ཐོབ་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་ཕྱེད་དང་ལྔས་མཆོད་རྟེན་བྱས་པས་བྱང་ཆུབ་ཐོབ་པ་བསྟན་པ་སྟེ། དེ་ལ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 1404]
ཐོག་མའི་ཚིགས༌[^1274]བཅད་བཞིས་ནི་མཆོད་རྟེན་བྱས་པ་བསྟན་ཏོ། །

[Block 1405]
འོག་མའི་ཚིགས༌[^1275]བཅད་ཕྱེད་ཀྱིས་ནི་མདོར་བསྡུས་པ་བསྟན་ཏོ། །
--- END BLOCKS ---
