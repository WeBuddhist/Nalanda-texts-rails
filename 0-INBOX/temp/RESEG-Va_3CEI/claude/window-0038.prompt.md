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

[Block 1336]
ངན་པར་ལྟ་བ་ནི་མེད་པར་ལྟ་བའོ། །

[Block 1337]
གཞན་ཡང་ལྟ་བ་སྣ་ཚོགས་ནི་ཡོད་མེད༌[^1241]ཅེས་བྱའོ། །

[Block 1338]
གཞན་ཡང་ཡོད་པ་ནི་བདག་གི་ཕུང་པོ་ཕྱི་མ་ཡོད་པར་འཛིན་པ་སྟེ། རྟག་པར་ལྟ་བའོ། །

[Block 1339]
མེད་པ་ནི་བདག་གི་ཕུང་པོ་ཕྱི་མ་མེད་པར་འཛིན་པ་སྟེ་ཆད་པར་ལྟ་བའོ། །

[Block 1340]
མཐར་ལྟ་བ་དང་ལོག་པར་ལྟ་བ་ལས་ལྟ་བ་དྲུག་ཅུ་རྩ་གཉིས་སུ་འཛིན་པ་ནི་ཡོད་མེད་ཅེས་བྱའོ། །

[Block 1341]
དེ་ལྟར་ངར་འཛིན་པར་ལྟ་བ་དྲུག་ཅུ་རྩ་གཉིས་ལ་སོགས་པར་འཛིན་ཅིང་ཆགས་ཏེ་གཏོང་དུ་མི་བཏུབ་པས༌[^1242]ལོག་པར་བྱེད་པར༌[^1243]ང་རྒྱལ་ཅན་ཞེས་བྱའོ། །

[Block 1342 [HEADING]]
###### **དགེ་བ་མེད་པས་མི་མཐུན་པ།** ^4-2-11-1-1-2-4-2-4-1-2-2-0

[Block 1343]
འདི་མན་ཆད་ཚིག་གཅིག་གིས་ནི་དགེ་བ་མེད་པས་མི་མཐུན་པ་བསྟན་ཏེ། གང་དགེ་བ་དང་ལྡན་པ་ནི་བསྙེན་པ་བཞི་ལ་བསྙེན་པར་བྱའོ།[^1244] །དགེ་བའི་བཤེས་གཉེན་ལ་བརྟེན་པ༌[^1245]དང་ཡང་དག་པའི་ཆོས་ཉེན་པ༌[^1246]དང་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་དང་། ཐོས་པ་བཞིན་དུ་ནན་ཏན་བྱེད་པའོ། །

[Block 1344]
བྱིས་པ་གཡོ་བྱེད་པ་སྡིག་པ་ཅན་ནི་ཚེ་རབས་དུ་མར་སངས་རྒྱས་ཀྱི་མཚན་ཡང་མི་ཐོས་ན་དགེ་བའི་བཤེས་གཉེན་དང་གང་ཞིག་ཕྲད་དེ། དེ་ལྟར་སངས་རྒྱས་ཀྱང་མི་མཐོང་། ཆོས་ཀྱང་མི་ཐོས་ཏེ། ཆོས་ཐོས་པའི་སྐལ་བ་མེད་པ།[^1247] ཡིད་ལ་བྱེད་པ་དང་ནན་ཏན་དུ་སྤྱོད་པར་ག་ལ་ཞིག་འགྱུར་ཏེ། དེ་ནི་ཤིན་ཏུ་གདུལ་དཀའ་བས་ཐོག་མ་ནས་ཐེག་པ་ཆེན་པོ་བསྟན་པར་དཀའོ། །

[Block 1345]
མདོ་ལས།

[Block 1346 [HEADING]]
###### **མི་མཐུན་པ་བསྡུ་བ།** ^4-2-11-1-1-2-4-2-4-2-0

[Block 1347]
ངའི་ཐབས་ཀྱིས༌[^1248]དེ་ལ་ཤཱ་རིའི་བུ། །ཞེས་པ་ནས་དེ་དག་མྱ་ངན་ལས་འདའ་བ༌[^1249]ཉེ་བར་བསྟན་ཞེས་པའི་བར་དུ་ནི་མི་མཐུན་པ་བསྡུ་བ་བསྟན་པ་སྟེ། ངས་སྔར་ཐབས་ཀྱི་མྱ་ངན༌[^1250]ལས་འདས་པ༌[^1251]སྡུག་བསྔལ་ཞི་བ་ཙམ་བསྟན་ཏོ། །

[Block 1348]
མདོ་ལས།

[Block 1349 [HEADING]]
###### **ཆོས་ལ་གནས་པ།** ^4-2-11-1-1-2-5-0

[Block 1350]
འདི་ལྟར་རྟག་ཏུ་ངས་བཤད་མྱ་ངན་འདས། །ཞེས་པ་ནས། ཐེག་པ་འདི་ནི་གཅིག་སྟེ་གཉིས་སུ་མེད། །ཅེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས༌[^1252]བཅད་བདུན་ཅུ་རྩ་ཕྱེད་དང་གཅིག་གིས༌[^1253]ཆོས་ལ་གནས་པ་བསྟན་པ་སྟེ། དེ་ལ་རྣམ་པ་གསུམ་མོ། །

[Block 1351]
ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་ཕྱོགས་བཅུའི་སངས་རྒྱས་ཀྱི་ཆོས་བསྟན་ཏོ། །

[Block 1352]
བར་གྱི་ཚིགས་བཅད་སུམ་ཅུ་རྩ་ཕྱེད་དང་དགུས་ནི་དུས་གསུམ་གྱི་སངས་རྒྱས་ཀྱི་ཆོས་བསྟན་ཏོ། །

[Block 1353]
ཐ་མ༌[^1254]ཚིགས་བཅད་སུམ་ཅུ་རྩ་ཕྱེད་དང་གཅིག་གིས་ནི་ང་ཡང་དེ་བཞིན་ནོ་ཞེས་པ་བསྟན་ཏོ། །

[Block 1354 [HEADING]]
###### **ཕྱོགས་བཅུའི་སངས་རྒྱས་ཀྱི་ཆོས།** ^4-2-11-1-1-2-5-1-0

[Block 1355]
འདི་ནི་ཕྱོགས་བཅུའི་སངས་རྒྱས་ཀྱི༌[^1255]ཆོས་བསྟན་པ་སྟེ།

[Block 1356]
མདོ་ལས།

[Block 1357]
ཐེག་པ་གཅིག་སྟེ་གཉིས་སུ་མེད། །ཅེས་འབྱུང་ན་གསུམ་མེད་པར་བྱ་སྟེ། གཅིག་ཏུ་བསྡུར་ག་ལ་ཞིག་རུང་།

[Block 1358]
མདོ་ལས།

[Block 1359 [HEADING]]
###### **དུས་གསུམ་གྱི་སངས་རྒྱས་ཀྱི་ཆོས།** ^4-2-11-1-1-2-5-2-0

[Block 1360]
སྔོན་གྱི་དེ་བཞིན་གཤེགས་པ་གང་བྱུང༌[^1256]བ། །ཞེས་པ་ནས། །དེ་དག་ཚད་བཟུང༌[^1257]དུ་ནི་ཡོད་མེད་པ། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་སུམ་ཅུ་རྩ་ཕྱེད་དང་དགུས་དུས་གསུམ་ཀྱི་ངས་རྒྱས་ཀྱི་ཆོས་བསྟན་པ་སྟེ། དེ་ལ་ཡང་རྣམ་པ་གསུམ་མོ། །

[Block 1361]
ཐོག་མའི་ཚིག་ཉི་ཤུ་རྩ་ཕྱེད་དང་བརྒྱད་ཀྱིས་ནི་སྔོན་འདས་པ་བསྟན་ཏོ། །

[Block 1362]
བར་གྱི་ཚིག་དྲུག་གིས་ནི་མ་འོངས་པ་བསྟན་ཏོ། །

[Block 1363 [HEADING]]
###### **སྔོན་འདས་པ།** ^4-2-11-1-1-2-5-2-1-0

[Block 1364]
ཐ་མའི་ཚིག་བཞིས་ནི་ད་ལྟར་བསྟན་ཏེ་འདས་པ་བསྟན་པ་ལ༌[^1258]རྣམ་པ་གཉིས་ཏེ། ཐོག་མའི་ཚིག་ཕྱེད་དང་ལྔས་ནི་སངས་རྒྱས་ཀྱི་ཆོས་བསྟན་པ་ཐོག་མར་བཀྲི༌[^1259]བའི་ཐབས་ཙམ་བསྟན་ནས་ཕྱིས་ཡང་དག་པ་བསྟན༌[^1260]པའོ། །

[Block 1365]
ཚིག་ཉི་ཤུ་རྩ་གསུམ་གྱིས་ནི་སེམས་ཅན་རྣམས་ཆོས་ཐོས་ནས་མཐར་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པ་བསྟན་པའོ། །

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
--- END BLOCKS ---
