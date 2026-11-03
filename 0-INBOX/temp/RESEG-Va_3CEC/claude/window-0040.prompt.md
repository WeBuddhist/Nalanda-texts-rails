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
[Block 1401]
རིགས་འདི་ཞེས་བྱ་བ་ནི་ཚེ་རབས་དེ་དག་ཏུ་སྐྱེས་པས་ན་བདག་རིགས་བཞི་ལས་གང་དང་གང་དུ་སྐྱེས་པ་དྲན་པའོ། །

[Block 1402]
རུས་ཞེས་བྱ་བ་ནི་རིགས་བཞི་ལས་ཀྱང་མཐོན་དམན་དུ་ཕྱེ་བ་ཤེས་པས་ཏེ།[^1203] ཚེ་རབས་དེ་དག་ན་བདག༌[^1204]གི་ཕའི་རུས་ནི་འདི་ཞེས་བྱ། མའི་རུས་ནི་འདི་ཞེས་བྱ་ཞེས་བྱ༌[^1205]བ་ལ་སོགས་པའོ། །

[Block 1403]
ཁ་དོག་ནི་འདི་འདྲ་ཞེས་བྱ་བ་ནི་ཁ་དོག་ཡིད་དུ་འོང་བ་དང་། ཡིད་དུ་མི་འོང་བ་དང་། མཛེས་པ་དང་མི་མཛེས་པ་ཅི་འདྲ་བར་གྱུར་པ་དང་དྲན་པའོ། །

[Block 1404]
ཁ་ཟས་འདི་ལྟ་བུ་ཞིག་ཟ་ཟ་ཞེས་བྱ་བ་ནི་སྟོན་པ་དྲན་པ་སྟེ། ཚེ་རབས་དེ་དང་དེ་དག་ཏུ་ཁ་ཟས་ཅི་དང་ཇི་ལྟ་བུ་ཟོས་པ་དྲན་པའོ། །

[Block 1405]
ཚེའི་ཚད་ནི་འདི་ཙམ་ཞིག་ཐུབ་ཅེས་བྱ་བ་ནི༌[^1206]ཚེའི་འདུ་བྱེད་དྲན་པ་སྟེ།

[Block 1406]
ཚེ་རབས་དེ་དག་ཏུ་ཚེའི་ཚད་ཇི་སྲིད་གནས་གནས༌[^1207]པ་ལས།

[Block 1407]
ཚེ་ཟད་དེ་ནི༌[^1208]ལན་དུ་ཤི། ཡེ་འདྲོག༌[^1209]གིས་ནི་ལན་དུ་བསད་པ་དྲན་པའོ། །

[Block 1408]
བདེ་བ་དང་སྡུག་བསྔལ་མྱོང་བ་ཞེས་བྱ་བས་ནི་དར་བ་དང་རྒུད་པ་དྲན་པ་བསྟན་ཏེ། ཚེ་རབས་དེ་དང་དེ་དག་ཏུ་དར་ཅིང་བདེ་བ་ལན་མང་དུ་མྱོང་བ་དང་། རྒུད་ཅིང་སྡུག་བསྔལ་བ་ལན་མང་དུ་མྱོང་བ་སོ་སོར་དྲན་པའོ། །

[Block 1409]
ཇི་ལྟར་བདག་གིས་དྲན་པ་དེ་བཞིན་དུ་སེམས་ཅན་གཞན་གྱིས༌[^1210]ཡང་དྲན་པར་སྦྱར་རོ། །

[Block 1410]
རྣམ་པ་དང་བཅས་ཞེས་བྱ་བ་ལ་རྣམ་པ་ནི་ཚེ་རབས་གཅིག་ནས་བསྐལ་པ་བྱེ་བ་ཁྲག་ཁྲིག་མང་པོ་དྲན་པའོ། །

[Block 1411]
རྒྱུ་མཚན་ནི་དུས་དང་རུས༌[^1211]ལ་སོགས་པ་གང་ཡིན་པ་དྲན་པའོ། །

[Block 1412]
ཡུལ་ཕྱོགས་ནི་བདག་དེ་ནས་ཤི་འཕོས་ནས་ཆེ་གེ་མོ་ཞིག་ཏུ་སྐྱེས་ཞེས་དྲན་པའོ། །

[Block 1413]
ཇི་ལྟར་དྲན་པ་བཤད་ཟིན་ཏོ། །

[Block 1414 [HEADING]]
#### དྲན་ནས་དོན་ཆེན་པོར་འགྱུར་བ། ^3-4-4-0

[Block 1415]
སྔོན་གྱི་རྒྱུ་ལས་བྱུང་བ་དྲན་ཞེས་བྱ་བ་ནི་དགེ་བའི་རྩ་བ་སྔོན་ཅི་དང་ཅི་བསགས་པ་དྲན་པའོ། །

[Block 1416]
བྱང་ཆུབ་ཏུ་ཡོངས་སུ་སྔོ་བར༌[^1212]བྱེད་དོ་ཞེས་བྱ་བ་ནི་དགེ་བའི་རྩ་བའི་རྒྱུ་ཡོད་པར་དྲན་ཞིང་ཤེས་ནས། དགེ་བའི་རྩ་བ་དེ་དག་བྱང་ཆུབ་ཏུ་སྔོ་བར༌[^1213]བྱེད་པའོ། །

[Block 1417]
སྔོན་གྱི་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་ཞེས་བྱ་བ་ནི་བདག་སྔོན་འགྱུར་བའི་སྡུག་བསྔལ་གྱིས༌[^1214]སྡུག་བསྔལ་བར་འགྱུར་བའམ། འདུ་བྱེད་ཀྱིས་སྡུག་བསྔལ་བར་གྱུར་པ་དེ་དག་དྲན་ནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1418]
སྟོན་པར་བྱེད་དོ་ཞེས་བྱ་བ་ནི་འདུ་བྱེད་རྣམས་མི་རྟག་པ་ལ༌[^1215]སོགས་པར་བལྟའོ༌[^1216]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1419]
གཟུགས་ཀྱིས་དྲེགས༌[^1217]པ་མེད་པ་ཡིན་ཞེས་བྱ་བ་ནི་དེ་ལྟར་མི་རྟག་པར་ཤེས་པས་བདག་ནི་གཟུགས་བཟང་པོ་མཛེས་པའོ་སྙམ་པའི་རློམ་སེམས་མེད་པ་སྟེ། མཛེས་པ་དེ་ཡང་དེ་མ་ཐག་ཏུ་མེད་པར་འགྱུར་བར་ཁོང་དུ་ཆུད་པའི་ཕྱིར་ཏེ། ཁ་དོག་གིས་དྲེགས་པ་མེད་པ་ལ་སོགས་པ་ལ་ཡང་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 1420]
སྐྱེ་བ་ཐམས་ཅད་འདོད་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་སྐྱེ་བའི༌[^1218]གནས་ཐམས་ཅད་དུ་སྐྱེ་བར་འདོད་པར་མི་སྐྱེ་ཞེས་བྱ༌[^1219]བའི་དོན་ཏོ། །

[Block 1421]
བསམས་བཞིན༌[^1220]དུ་སྲིད་པར་སྐྱེ་བ་འཛིན་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གྱི་དོན་དུ་ཤེས་བཞིན་དུ་ཁམས་གསུམ་དུ་སྐྱེ་བར་བྱེད་པའོ། །

[Block 1422]
སྔོན་གྱི་ཀུན་ནས་ཉོན་མོངས་པའི་སྤྱོད་པས་ངོ་ཚ་ཞིང་འཇམ༌[^1221]སྟེ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་མི་རྟག་པའི་མཚན་ཉིད་དུ་ཤེས་པས། དེ་ལྟ་བུ་དག་གི་ཕྱིར་སྔོན་སྡིག་པ་བྱས་པ་ནི་མི་རིགས་པ༌[^1222]བྱས་སོ་ཞེས་ངོ་ཚ་ཞིང་འཛེམ་པ༌[^1223]སྐྱེ་བའོ། །

[Block 1423]
རྒྱས་པར་བྱེད་དོ་ཞེས་བྱ་བ་ནི་དགེ་བའི་རྩ་བ་བསགས་པ་བྱང་ཆུབ་ཏུ་བསྔོས་ནས་འཕེལ་ཞིང་རྒྱ་ཆེན་པོར་བྱེད་པའོ། །

[Block 1424]
དེས་མི་མཐུན་པའི་ཕྱོགས་ཡོངས་སུ་བསྔོ་བ༌[^1224]སྤངས་ཏེ་ཞེས་བྱ་བ་ནི་དགེ་བའི་རྩ་བ་ཅི་བསགས་པ་དང་། ཉན་ཐོས་སམ་རང་སངས་རྒྱས་སམ་ལྷ་འམ་མིར་སྐྱེ་བར་མི་བསྔོའི། དཀོན་མཆོག་གསུམ་གྱི་རིགས་རྒྱུན་མི་ཆད་པ༌[^1225]དང་། ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་བསྔོའོ། །

[Block 1425]
འདིའི་དོན་ཆེན་པོར་འགྱུར་རོ། །

[Block 1426]
སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་ཤེས་པ་མངོན་དུ༌[^1226]བྱེད་པའི་མངོན་པར་ཤེས་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1427 [HEADING]]
### མཉམ་པ་ཉིད་མངོན་སུམ་པ། ^3-5-0

[Block 1428]
མཉམ་པ་ཉིད་མངོན་སུམ་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་རྫུ་འཕྲུལ་བྱ་བ་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སྟེ།[^1227] དེ་མི་ཟད་པ་ཡང་རྫུ་འཕྲུལ། མངོན་པར་ཤེས་པ་དེ་ཡིད་ཆེས་ཤིང་སྨིན་པར་བྱ་བའི་སེམས་ཅན་མི་ཟད་པས་ན་སྨིན་པར་བྱེད་པའི་སེམས་ཅན་དེ་ཡང་མི་ཟད་པའོ། །

[Block 1429]
དེ་ཡང་རྣམ་པ་དྲུག་ཏུ་རིག་པར་བྱ་སྟེ། རྒྱུ་རྣམ་པར་དག་པས་བྱུང་བ༌[^1228]དང་། རྣམ་པ་སྣ་ཚོགས་སུ་སྟོན་པ་དང་། དབང་དུ་བྱ་བ་དང་། ཐམས་ཅད་གཟུགས་སུ་འཛུད་པ་དང་། གཞན་དུ་བྱ་བ་དང་། གཞན་གྱི་རྫུ་འཕྲུལ་ཟིལ་གྱིས་གནོན་པའོ། །

[Block 1430]
དེ་ལ་གང་འདུན་པ་དང་བརྩོན་འགྲུས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཆོ་འཕྲུལ་རྣམ་པ་དུ་མ་མྱོང་བ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^1229]རྒྱུ་རྣམ་པར་དག་པ་ལས་བྱུང་བ་བསྟན་ཏོ། །

[Block 1431]
དེའི་རྫུ་འཕྲུལ་གྱི་ཆོ་འཕྲུལ་དེ་དག་ནི་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། གཟུགས་དང་ཁ་དོག་ཏུ་སྣང་བ་དེ་དང་དེ་ཉིད་སྟོན་ཏེ། མོས་པ་ཇི་ལྟ་བ་བཞིན་དུ་སེམས་ཅན་རྣམས་ལ་ཆོས་སྟོན་ཏོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^1230]སྣ་ཚོགས་སུ་སྟོན་པ་བསྟན་ཏོ། །

[Block 1432]
དེའི་སྟོབས་གང་དང་གང་གིས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། དྲེགས་པ་འདུལ་བའི་ཕྱིར་ཆོས་སྟོན་ཏོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་དབང་དུ་བྱ་བ་བསྟན་ཏོ། །

[Block 1433]
དེ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་དེ་དག་གིས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ།[^1231] རྒྱ་མཚོ་ཆེན་པོ་ཉིད་དུ་འདུག་གོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་ཐམས་ཅད་གཟུགས་སུ་འཛུད་པ་བསྟན་ཏོ། །

[Block 1434]
གལ་ཏེ་སྲེག་པའི་བསྐལ་པ༌[^1232]ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། གང་དང་གང་བྱིན་གྱི་རླབས༌[^1233]ཀྱིས་བྱིན་གྱིས་བརླབས་པ་དེ་དག་གི་དེ་ཁོ་ན་བཞིན་དུ་འདུག་གོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^1234]གཞན་དུ་བྱ་བ་བསྟན་ཏོ། །

[Block 1435]
དེའི་བྱིན་གྱི་རླབས༌[^1235]དེ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བདུད་ཀྱི་རིགས༌[^1236]ཀྱི་ལྷ་རྣམས་ཀྱིས་མི་འཕྲོགས་པ༌[^1237]སྟེ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རྫུ་འཕྲུལ་ཟིལ་གྱིས་གནོན་པ་བསྟན་ཏོ། །

[Block 1436 [HEADING]]
#### རྒྱུ་རྣམ་པར་དག་པས་བྱུང་བ། ^3-5-1-0

[Block 1437]
གང་འདུན་པ་དང་། བརྩོན་འགྲུས་དང་། སེམས་དང་དཔྱོད་པས་ཟིན་པའི་ཆོས་རྣམས་བསྒྲུབ་པ༌[^1238]དང་ཞེས་བྱ་བ་ལ། འདུན་པ་ལ་སོགས་པ་བཞི་པོ་མིང་གིས་སྨོས་པ་འདི་དག་ནི་རྫུ་འཕྲུལ་གྱི་རྐང་པ་ཞེས་བྱ་སྟེ། རྫུ་འཕྲུལ་བ༌[^1239]སྐྱེད་པའི་རྒྱུའོ། །

[Block 1438]
རྫུ་འཕྲུལ་ནི་འོག་ནས་འབྱུང་བའི་གཟུགས་དང་། སྟོབས་དང་བྱིན་གྱི་རླབས༌[^1240]ལ་སོགས་པ་ལྟ་བུར་སྤྲུལ་ཅིང་འབྱོར་པ་ནུས་པ་ལ་བྱའོ། །

[Block 1439]
དེ་སྤྲུལ་ཅིང་འབྱོར་པ་ནུས་པའི་རྒྱུ་འམ་གཞི་འམ། དེ་ལྟ་བུའི་གནས་སུ་ཕྱིན་པར་བྱེད་པ་ནི་འདུན་པ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་བཞི་པོ་འདི་རྣམས་ཡིན་པས་འདུན་པ་ལ་སོགས་པ༌[^1241]བཞི་པོ་འདི་རྣམས་ལ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་ཞེས་བྱའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། འདུན་པས་ནི་ཐོག་མ༌[^1242]ཉིད་དུ་རྫུ་འཕྲུལ་ལ་མངོན་དུ་ཕྱོགས་པའམ་དད་པར་བྱེད། བརྩོན་འགྲུས་ནི་དེ་སྒྲུབ་པར་བྱེད། །སེམས་ཀྱིས་ནི་བསྒྲུབ་པ༌[^1243]རྣམས་ཆུད་མ༌[^1244]ཟོས་པར་བཟུང་བའི་ཆོས་གཏན་ལ་ཕབ་ནས་རྟོག་པར༌[^1245]བྱེད་དེ། དེ་ལྟ་བུ་ལ་རྫུ་འཕྲུལ་འབྱུང་བའི་ཕྱིར་དེ་རྣམས་ནི་རྫུ་འཕྲུལ་གྱི་རྐང་པའོ། །

[Block 1440]
རབ་ཏུ་ཟིན་པའི་ཆོས་རྣམས་ཞེས་བྱ་བ་ལ། འདུན་པ་དང་བརྩོན་འགྲུས་དང་། སེམས་དང་དཔྱོད་པ་རྣམས་ཀྱིས་བསྒྲུབ༌[^1246]པའམ། དེ་དག་ལྡན་པའི་གཟུགས་དང་བྱིན་གྱི་རླབས༌[^1247]འོག་ནས་འབྱུང་བ་རྣམས་སྒྲུབ་ཅེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
