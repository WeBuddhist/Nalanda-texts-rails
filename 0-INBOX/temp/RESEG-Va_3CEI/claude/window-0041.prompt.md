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
[Block 1436 [HEADING]]
###### **རོལ་མོས་མཆོད་པ།** ^4-2-11-1-1-2-5-2-1-2-2-4-2-0

[Block 1437]
དེར་ནི་གང་གིས་སིལ༌[^1300]སྙན་བརྡུང་བཅུག་པ། །ཞེས་པ་ནས། ཆུ་ལ་བརྡབས་དང་ཐལ་མོ་བརྡབས།[^1301] །ཞེས་པའི་བར་དུ་ནི་རོལ་མོས་མཆོད་པ་བྱ་བ་བསྟན་པ་སྟེ། མདོ་ལས་རོལ་མོ་དང་ན་ཆུང་བཟང་མོ་ཕ་རོལ་གྱི་སེམས་འཕྲོག་པས་སྦྱིན་པར་མི་བྱའོ་ཞེས་འབྱུང་སྟེ། སངས་རྒྱས་ལ་མཆོད་ན་འགལ་བ་མེད་དོ། །

[Block 1438]
མདོ་ལས།

[Block 1439 [HEADING]]
###### **དབྱངས་ཀྱིས་མཆོད་པ།** ^4-2-11-1-1-2-5-2-1-2-2-4-3-0

[Block 1440]
བདེ་བར་གཤེགས་པ་དེ་ལ་མཆོད་པའི་ཕྱིར། །ཞེས་པ་ནས། རིང་བསྲེལ་དེ་ལ་རྣམ་པ་མང་པོས་མཆོད། །ཅེས་པའི་བར་དུ་ནི་ཚིགས་བཅད་འདིས་དབྱངས་དང་གླུ་སྙན་པས་མཆོད་པ་བྱས་པ༌[^1302]བསྟན་པ་སྟེ། ཚངས་པའི་དབྱངས་ཐོབ་པར་འགྱུར་རོ། །

[Block 1441]
མདོ་ལས།

[Block 1442]
བདེ་གཤེགས་རིང་བསྲེལ་ལ་ནི་ཅུང་ཟད་ཀྱིས། །ཞེས་པ་ནས། དེ་དག་རིམ་གྱིས་སངས་རྒྱས་བྱེ་བ་མཐོང་། །ཞེས་པའི་བར་དུ་ནི་མེ་ཏོག་གི་མཆོད་པ་བྱ་བ་བསྟན་པ་སྟེ། སྔར་དངོས་པོ་བཞིས་མཆོད་པ་ལས་མེ་ཏོག་གི༌[^1303]མཆོད་པ་དང་ཅི་མི་འདྲ་ཞེ༌[^1304]ན། འདི་ནི་འཁྲུག་བཞིན་པའི་སེམས་ཀྱིས་མཆོད་པ་ལ་བྱའོ། །

[Block 1443]
མདོ་ལས།

[Block 1444 [HEADING]]
###### **ལུས་ཀྱི་ལས་ཀྱིས་མཆོད་པ།** ^4-2-11-1-1-2-5-2-1-2-2-4-4-0

[Block 1445]
མཆོད་རྟེན་དེ་ལ་གང་གིས་ཐལ་མོ་སྦྱར། །ཞེས་པ་ནས། དེ་བཞིན་ལན་ཅིག་ལུས་ཀྱང་བཏུད་པ་དང་། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1305]ནི་ལུས་ཀྱི་ལས་ཀྱིས༌[^1306]མཆོད་པ་བྱ་བ་སྟེ། གླུ་དང་དབྱངས་ཀྱིས་མཆོད་པ་ནི་ངག་གི་ལས་སོ། །

[Block 1446]
དེ་ལྟར་མཆོད་པ་བྱ་བར་བསམས་བ༌[^1307]ནི་ཡིད་ཀྱི༌[^1308]ལས་སོ། །

[Block 1447]
འདི་ལས་གཞན་པ་ནི་ཕྱི་རོལ་གྱི་ཟང་ཟིང་གི༌[^1309]མཆོད་པ་ཞེས་བྱའོ། །

[Block 1448]
མདོ་ལས།

[Block 1449 [HEADING]]
###### **སངས་རྒྱས་བརྗོད་པ།** ^4-2-11-1-1-2-5-2-1-2-2-5-0

[Block 1450]
ཕྱག་འཚལ་སངས་རྒྱས་ལན་ཅིག་སྨྲས་པ་དང་། །ཞེས་པ་ནས། དེ་དག་ཀུན་གྱིས་བྱང་ཆུབ་ཐོབ་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1310]ནི་སངས་རྒྱས་ཀྱི་མཚན་བརྗོད་པས་བྱང་ཆུབ་ཐོབ་པར་བསྟན་པ་སྟེ།

[Block 1451]
སངས་རྒྱས་ཀྱི་མཚན་ལན་གཅིག་བརྗོད་པས་བྱང་ཆུབ་མཆོག་ཐོབ་ན་ལན་མང་དུ་བརྗོད་པ་ལྟ་ཅི་སྨོས། །མདོ་ལས།

[Block 1452 [HEADING]]
###### **བསྡུ་བ།** ^4-2-11-1-1-2-5-2-1-2-3-0

[Block 1453]
དེའི་ཚེ་བདེ་བར་གཤེགས་པ་དེ་དག་ནི། །ཞེས་པ་ནས། །དེ་དག་ཐམས་ཅད་བྱང་ཆུབ་ཐོབ་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1311]ནི་སེམས་ཅན་ཆོས་ཐོས་ནས་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པ་བསྟན་པའོ། །

[Block 1454]
མདོ་ལས།

[Block 1455 [HEADING]]
###### **མ་འོངས་པ།** ^4-2-11-1-1-2-5-2-2-0

[Block 1456]
ཕྱིས་འབྱུང༌[^1312]སངས་རྒྱས་བྱེ་བ་མང་པོ་རྣམས། །ཞེས་པ་ནས། ཐབས་འདི་ཡང་ནི་རབ་ཏུ་འཆད་པར་འགྱུར། །ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་ཕྱེད་དང་བདུན་གྱིས༌[^1313]མ་འོངས་པའི་ཆོས་བསྟན་པ་སྟེ། དེ་ལ་ཚིགས་བཅད་བྱེད་དང་བཞིས་ནི་ད་ལྟར་བཤད་པ་དང་མཐུན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 1457]
ཚིགས་བཅད་གསུམ་གྱིས་ནི་དོན་སྔ་མ་བཟླས་ཏེ་བསྟན་ཏོ། །

[Block 1458 [HEADING]]
###### **ད་ལྟར་བཤད་པ་དང་མཐུན་པ།** ^4-2-11-1-1-2-5-2-2-1-0

[Block 1459]
སྔ་མ་ལ་ཡང་གཉིས་ཏེ། ཚིགས་བཅད་གཅིག་གིས་ནི་ཐབས་ཙམ་དུ་མཐུན་པ་བསྟན་པ་དང་། ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་ཡང་དག་པ་བསྟན་ཏོ། །

[Block 1460]
ཚིགས་བཅད་གཅིག་གིས་ནི་ཅིའི་ཕྱིར་བཤད་པ་བསྟན་ཏོ། །

[Block 1461]
མདོ་ལས།

[Block 1462]
ཐབས་ལ་མཁས་པ་དག་ནི་མཐའ་ཡས་པ། །ཞེས་པ་ནས། ཆོས་འདི་ཐོས་ནས་སངས་རྒྱས་མི་འགྱུར་བ། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1314]ནི་ཡང་དག་པར་འགྲུབ་པར་འགྱུར་བ་བསྟན་པ་སྟེ། དེ་ལྟར༌[^1315]ཆོས་ཐོས་པ་ཐམས་ཅད་ཀྱིས༌[^1316]སངས་རྒྱས་སུ་མི་འགྱུར་བ་མེད་དོ། །

[Block 1463]
མདོ་ལས།

[Block 1464]
དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་སྨོན་ལམ་ནི། །ཞེས་པ་ནས། བྱང་ཆུབ་ཕྱིར་དུ་སྤྱད་ནས་སྤྱད་པར་འཇུག །ཅེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1317]ནི་ཅིའི་ཕྱིར་བཤད་པ་བསྟན་པ་སྟེ། དེ་ཡང་སྔོན་གྱི་སྨོན་ལམ་གྱི་དབང་ངོ་ཞེས་བསྟན་ཏོ། །

[Block 1465]
མདོ་ལས།

[Block 1466 [HEADING]]
###### **དོན་སྔ་མ་བཟླས་པ།** ^4-2-11-1-1-2-5-2-2-2-0

[Block 1467]
བྱེ་བ༌[^1318]སྟོང་ཕྲག་དུ་མ་ཆོས་ཀྱི་སྒོ། །ཞེས་པ་ནས། དེ་བཞིན་གཤེགས་པ་ཉིད་དུ་ཆོས་རྣམས་བཤད། །ཞེས་པའི༌[^1319]བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་གསུམ་གྱིས་དོན་སྔ་མ་བཟླས་ཏེ་བསྟན་ཏོ། །

[Block 1468]
དེ་ལ་ཚིགས་བཅད་གཅིག་གིས་ནི་སྔར་ཐབས་ཙམ་དུ་བསྟན་པ་ཡང་ཐེག་པ་གཅིག་ཏུ་ཟད་པ་དང་། ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་མཚན་ཉིད་གསུམ་གྱི་ཁུངས་བསྟན་ཏོ། །

[Block 1469]
མདོ་ལས།

[Block 1470]
འདི་ལྟར་རྟག་ཏུ་ཆོས་ཀྱི་ཚུལ་གནས་པ། །ཞེས་པ་ནས། ཐབས་ལ་མཁས་པ་ཤིན་ཏུ་སྟོན་པར་འགྱུར། ། ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས་ནི་མཚན་ཉིད་གསུམ་གྱི་ཁུངས་བསྟན་ཏོ།[^1320] །

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
--- END BLOCKS ---
