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
[Block 1296]
ང་ལ་སེར་སྣ་དག་ནི་ཆུང་ཟད༌[^1217]མེད། །ཞེས་པ་ནས། །འགྲོ་བ་ཀུན་རིག་དེ་བས་ང་སངས་རྒྱས། །ཞེས་པའི་བར་དུ་ནི་ཡོན་ཏན་གྱི་ཁྱད་པར་བསྟན་པ་སྟེ། དེ་ལ་ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ང་འདོད་ཆགས་དང་བྲལ་བས་འཇིགས་པ་མེད་པའི་ཡོན་ཏན་བསྟན་ཏོ། །

[Block 1297]
ཚིག་འོག་མ་གཅིག་གིས་ནི་ཕྱི་རོལ་གྱི་རྒྱན་དང་ཡང་དག་པའི་ཆོས་ཀྱི་ཡོན་ཏན་བསྟན་ཏེ། སེར་སྣ་མེད་ཅེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོ་བཅབས་ཏེ། ཐེག་པ་ཆུང་ངུ་སྟོན་ཅིང་སེམས་ཅན་བསླུ་བའམ། སྔར་ཐེག་པ་ཆེན་པོ་སྦྱིན་པར་བྱ་བ་ལས་ཕྱིས་མ་སྦྱིན་པ༌[^1218]མ་ཡིན་པས་སེར་སྣ་མེད་དོ། །

[Block 1298]
སེམས་ཅན་གྱིས་ཐེག་པ་ཆེན་པོ་རིག་ཅིང་ཆུད་ཀྱིས༌[^1219]དོགས་པའི་ཐུགས་མི་མངའ་བས་ཕྲག་དོག་མེད་དོ། །

[Block 1299]
སྡིག་པའི་ཆོས་ནི་གང་ཉོན་མོངས་པའི་ལས་དང་བཅས་པ་སྡུག་བསྔལ་བ་འཁོར་བའི་ཆོས་ཡོངས་སུ་བཅད་པས་ཉེས་པའི་སྐྱོན་གང་ཡང་མེད་དེ། ཡང་དག་པའི་ཡེ་ཤེས་རྫོགས་ནས་ཕྱོགས་བཅུར་སེང་གེའི་སྒྲ་བསྒྲགས་ཏེ་འཇིགས་པ་མི་མངའ་བས། འགྲོ་བ་ཀུན་རིག་ང་སངས་རྒྱས། །ཞེས་བྱའོ། །

[Block 1300]
མདོ་ལས།

[Block 1301]
ཇི་ལྟར་མཚན་རྣམས་ཀྱིས་ནི་ང་བརྒྱན་ཏེ། །ཞེས་པ་ནས། །ཆོས་ཀྱི་རང་བཞིན་ཕྱག་རྒྱ་འདི༌[^1220]བཤད་དོ། །ཞེས་པའི་བར་དུ་ནི་ཕྱི་རོལ་གྱི་མཚན་གྱིས་བརྒྱན་པ་བསྟན་པ་སྟེ། མཚན་བཟང་པོས་བརྒྱན་པའི་སྐུའི་འོད་དང་། ཡེ་ཤེས་ཀྱི་འོད་ཀྱིས༌[^1221]སྣོད་ཀྱི་འཇིག་རྟེན་དང་བཅུད་ཀྱི་འཇིག་རྟེན་སྣང་བར་བྱས་ནས་སྲོག་ཆགས་ཀུན་གྱིས་ང་ལ་བཀུར་སྟི་བྱས་སོ། །

[Block 1302]
ནང་ན་ཉོན་མོངས་པ་མེད་པས་ཕྱི་རོལ་གྱི་མཚན་གྱིས་བརྒྱན་ཏེ་ཆོས་ཀྱི་རང་བཞིན་གྱི་ཕྱག་རྒྱ་འདི་བཤད་དོ། །

[Block 1303]
ཕྱག་རྒྱ་ནི་སྟོང་པ་གཉིས་ཀྱི་ཐེག་པ་ཆེན་པོའི་ཕྱག་རྒྱ་སྟེ། ཕྱག་རྒྱ་འདིས་བཏབ་པ་ནི་ཐེག་པ་ཆེན་པོའི་ཆོས་ཡང་དག་པ་ཞེས་བྱའོ། །

[Block 1304]
མདོ་ལས།

[Block 1305 [HEADING]]
###### **འཇུག་པ་ཉིད།** ^4-2-11-1-1-2-4-2-2-3-0

[Block 1306]
དེ་ལྟར་ངས་བསམས༌[^1222]ཤཱ་རིའི་བུ། །ཞེས་པ་ནས། །བདག་འོད་རང་བྱུང༌[^1223]འཇིག་རྟེན་རིག་པར༌[^1224]རོ། །ཞེས་པའི་བར་དུ་ནི་གོ་བར་བྱ་བ་བསྟན་པ་སྟེ་ཐེག་པ་ཆེན་པོ་ཡང་དག་པའི་ཡེ་ཤེས་ངས་ཇི་ལྟར་རིག་པ་བཞིན་དུ་སེམས་ཅན་ཐམས་ཅད་ལ་ཡང་བསྟན་ཞེས་པའི་དོན་ཏོ། །

[Block 1307]
མདོ་ལས།

[Block 1308 [HEADING]]
###### **ཆུད་པར་བྱ་བ།** ^4-2-11-1-1-2-4-2-3-0

[Block 1309]
ཇི་ལྟར་མཐོང་ཞིང་ཇི་ལྟར་བསམས་པ༌[^1225]དང་། །ཞེས་པ་ནས། །དུར་ས་དེ་དག་ཕྱི་ཕྱིར་སྐྱེ་བར་འགྱུར། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་གཅིག་གིས་ཆུད་པར་བྱེད་པ་བསྟན་པ་སྟེ། །སྔོན་གྱི་སྨོན་ལམ་ཡོངས་སུ་རྫོགས་ནས་སྨོན་ལམ་བཞིན་དུ་བྱང་ཆུབ་ལ་དགོད་དེ། བྱང་ཆུབ་ནི་རྒྱུའི་དོན་ཏོ། །

[Block 1310]
ས་དང་པོ་ནས་ས་བརྒྱད་ཀྱི་བར་དུ་ཆུད་པར་བྱེད་དེ། ཕྱིར་མི་ལྡོག་པ་ཐོབ་པས་སངས་རྒྱས་སུ་འགྱུར་བའི་རྒྱུའོ། །

[Block 1311 [HEADING]]
###### **སྟོན་པ།** ^4-2-11-1-1-2-4-2-4-0

[Block 1312]
འདི་མན་ཆད་ཚིག་བཅུས་ནི་སྟོན་པ་འགྲེལ་པ་སྟེ། དེ་ལ་ཐོག་མའི་ཚིག་བརྒྱད་ཀྱིས་མི་མཐུན་པ་སྟོན་ཏོ། །

[Block 1313]
ཚིག་ཕྱི་མ་གཉིས་ཀྱིས་ནི་ཕྱིས༌[^1226]མཐུན་པར་འགྱུར་བ་བསྟན་པ་སྟེ། དེ་ལ་གང་ཤེས་པ་དང་ལྡན་པས༌[^1227]ནི་དེ་བཞིན་དུ་འཛིན་པར་འགྱུར་གྱི་གང་མི་ཤེས་པ་རྣམས་ནི་དེ་ལ་མྱོས་ཏེ་སྐུར་པ་འདེབས་སོ། །

[Block 1314 [HEADING]]
###### **མི་མཐུན་པའི་མཚན་མ།** ^4-2-11-1-1-2-4-2-4-1-0

[Block 1315]
འདི་མན་ཆད་ཚིག་དྲུག་གིས་མི་མཐུན་པའི་མཚན་མ་བསྟན་ཏེ། དེ་ལ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 1316]
ཐོག་མ་ཚིག་གཅིག་གིས་ནི་དགེ་བ་མེད་ལ་སྡིག་པ་དང་བཅས་པས་མི་མཐུན་པ་བསྟན་ཏོ། །

[Block 1317]
འོག་མ་ཚིག་ལྔས་ནི་སྡིག་པ་དང་བཅས་ལ་དགེ་བ་མེད་པས་མི་མཐུན་པ་བསྟན་ཏོ། །

[Block 1318 [HEADING]]
###### **དགེ་བ་མེད་ལ་སྡིག་པ་དང་བཅས་པས་མི་མཐུན་པ།** ^4-2-11-1-1-2-4-2-4-1-1-0

[Block 1319]
སྤྱོད་པ་མ་སྤྱད་ཚེ་རབས་སྔ་མ་ལ། །ཞེས་པ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་དགེ་བའི་རྩ་བ་མ་བསྐྱེད་པ༌[^1228]སྟེ། ཅུང་ཟད་བསྐྱེད་པ༌[^1229]ཡང་ཟག་པ་མེད་པའི་རྒྱུར་འགྱུར་བ་མ་ཡིན་གྱི༌[^1230]འདོད་པ་ལྔའི་ཡོན་ཏན་གྱི་རྒྱུར་འགྱུར་བས་འདི་ལྔ་ལ་ཆགས་ཤིང་ཞེན་ཏེ། གཏི་མུག་གི༌[^1231]ལས་བྱས་པས་སྲེད་པ་སྐྱེས་ཏེ། སྐྱེ་ཤིའི་སྡོང་པོ་ཕྱི་ཕྱིར་སྐྱེ་བར་འགྱུར༌[^1232]ཏོ། །

[Block 1320 [HEADING]]
###### **སྡིག་པ་དང་བཅས་ལ་དགེ་བ་མེད་པས་མི་མཐུན་པ།** ^4-2-11-1-1-2-4-2-4-1-2-0

[Block 1321]
འདི་མན་ཆད་ཚིག་ལྔས་སྡིག་པ་དང་བཅས་ལ་དགེ་བ་མེད་པས་མི་མཐུན་པར་བསྟན་ཏེ། དེ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 1322]
དེ་ལ་སྔ་མ་ཚིག་བཞིས་ནི་སྡིག་པ་དང་བཅས་པས་མི་མཐུན་པ་བསྟན་ཏོ། །

[Block 1323]
འོག་མ་ཚིག་གཅིག་གིས་ནི་དགེ་བ་མེད་པས་མི་མཐུན་པ་བསྟན་ཏོ། །

[Block 1324 [HEADING]]
###### **སྡིག་པ་དང་བཅས་པས་མི་མཐུན་པ།** ^4-2-11-1-1-2-4-2-4-1-2-1-0

[Block 1325]
སྔ་མ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། འདོད་པ་ལྔའི་ཡོན་ཏན་ལ་ཆགས་ཤིང་ཞེན་པས་མི་མཐུན་པ་དང་། བསླབ་པ་མྱོས་ཤིང་འཁྲུལ་པས་མི་མཐུན་པ་སྟེ། འདོད་པའི་དབང་གིས་མི་དགེ་བའི་ལས་འབའ་ཞིག་སྤྱད་པས་ངན་འགྲོར་ལྷུང༌[^1233]ཞེས་བྱའོ། །

[Block 1326]
ལས་འདྲེན་མར་སྤྱད་པ༌[^1234]འགྲོ་བ་དྲུག་ཏུ་ཉོན་མོངས་པར་འགྱུར་རོ། །

[Block 1327]
སྐྱེ་བ་རྣམ་བཞིར་ལས་དང་འགྲོགས་པས་སྡུག་བསྔལ་གསུམ་དང་ལྔ་དང་བརྒྱད་ཀྱིས༌[^1235]གདུངས་པས་བཙིར་བ༌[^1236]ཞེས་བྱའོ། །

[Block 1328]
ཕྱི་ཕྱིར་སྐྱེ་བར་འགྱུར་བ་ནི་འཁོར་བའི་རྒྱུན་མི་འཆད་པའོ། །

[Block 1329]
མདོ་ལས།

[Block 1330]
བསོད་ནམས་ཆུང་བས་སྡུག་བསྔལ་ཀུན་གྱིས་བཙིར།[^1237] །ཞེས་པ་ནས། །ཚེ་རབས་སྐྱེ་བ་སྟོང་ཕྲག་དུ་མའོ། །ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་བསླབ་པ་འཁྲུགས་པས༌[^1238]མི་མཐུན་པ་བསྟན་པ་སྟེ། ཐོག་མའི་ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་འཇིག་ཚོགས་སུ་ལྟ་བ་དང་མཐར་ལྟ་བས་ལྟ་བ་དྲུག་ཅུ་རྩ་གཉིས་སུ་འགྱུར་བ་བསྟན་ཏོ། །

[Block 1331]
ཕྱི་མ་ཚིག་གཅིག་གིས་ནི་ལྟ་བ་བསྙེམས་པ་དང་ཚུལ་ཁྲིམས་བསྙེམས་པའི་རྒྱུར་འགྱུར་བ་དང་། དེ་མ་ཡིན་པ་གཞན་ཡང་སྐྱེ་བ་བསྟན་ཏོ། །

[Block 1332]
སེམས་ཅན༌[^1239]ཐོག་མ་མེད་པ་ནས་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཆུང་བས་སྡུག་བསྔལ་གྱིས་བཙིར་བར༌[^1240]གྱུར་ཏོ། །

[Block 1333]
དེ་དག་ཀྱང་ཐར་པའི་ལམ་འདོད་མོད་ཀྱི་ཡང་དག་པ་དང་ལོག་པ་མ་རྟོགས་ཏེ་མུ་སྟེགས་ཅན་དུ་གྱུར་ན་ལོག་པར་ལྟ་བ་ལ་སློབ་པ་དང་། སྤྱོད་པ་འཁྲུལ་པས་ལོག་པར་ལྟ་བ་ཞེས་བྱའོ། །

[Block 1334]
ལྟ་བ་ལ་རྣམ་པ་མང་སྟེ་གང་སེམས་ཅན་གྱི་འབྱུང་བའི་ལམ་གྱི་བར་དུ་གཅོད་ཅིང་རྣམ་པར་གྲོལ་བར་མི་འགྱུར་བ་ལ་ལྟ་བ་སྟུག་པོ་ཞེས་བྱའོ། །

[Block 1335]
ཡོད་པ་དང་མེད་པ་ཞེས་བྱ་བ་ནི་ལྟ་བ་ལྔ་ལ་བཞི་ནི་ཡོད་པར་ལྟ་བའོ། །
--- END BLOCKS ---
