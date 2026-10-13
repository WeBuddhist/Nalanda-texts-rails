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
དེ་ལ་གཏན་ཚིགས་མེད་པ༌[^1080]སྒྲ་རྟག་སྟེ། རེག་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རྡུལ་ཕྲ་རབ་བཞིན་ནོ༌[^1081]ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1402]
བསྒྲུབ་བྱ་མེད་པ་ནི་ལས་བཞིན་ནོ། །

[Block 1403]
གཉིས་ཀ་མེད་པ་ནི་བུམ་པ་བཞིན་ནོ། །

[Block 1404]
མི་མཐུན་པའི་ཕྱོགས་ལ་ཞུགས་པ་ནི་དཔེར་ན་གང་མི་རྟག་པ་དེ་རེག་པར་བྱ་བ་མ་ཡིན་ཏེ། མཐོང་བའི་ལས་བཞིན་རྡུལ་ཕྲ་རབ་བཞིན་ནམ་མཁའ་བཞིན་ཞེས་པ་ལྟ་བུའོ། །

[Block 1405]
དེ་དག་གིས་ནི་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་ནི༌[^1082]འབྲེལ་ན་དེའི་ཆོས་སུ་གྲུབ་པ༌[^1083]སོ་སོར་བརྗོད་དོ། །

[Block 1406]
ནམ་མཁའ་ལ་སོགས་པ་རྟག་པ་ལ་ཁས་མི་ལེན་པ་ལའོ། །

[Block 1407]
ཆོས་མི་མཐུན་པ་དེ་དག་གིས་ནི་གང་ལ་ཡང་རྗེས་སུ་འགྲོ་བ་མ་བརྗོད་དོ། །

[Block 1408]
གཏན་ཚིགས་འབའ་ཞིག་བསྒྲུབ་པར་བྱ་བའི༌[^1084]དོན་དེའི་མི་མཐུན་པའི་ཕྱོགས་དང་ལྷན་ཅིག་ཡོད་པར་བསྟན་པར་བྱ་སྟེ། རྩོལ་བ་ལས་བྱུང་བས་མི་རྟག་པ་ཉིད་རྟག་པས་རྩོལ་བ་ལས༌[^1085]མ་བྱུང་བ་སྟེ། བུམ་པ་དང་ནམ་མཁའ་བཞིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1409]
ཇི་སྐད་དུ། གཅིག་ལ་རབ་ཏུ་གྲུབ་ན་གཉིས་ཀའི་དཔེའོ་ཞེས་བརྗོད་དོ། །

[Block 1410]
དེ་དག་གིས་གཉིས་ཀ་ལ་ཡོད་པ་ཉིད་གཉིས་དང་རྗེས་སུ་འགྲོ་བ་ཕྱིན་ཅི་ལོག་དེས་དཔེ་ལྟར་སྣང་བའོ་ཞེས་བརྗོད་དོ། །

[Block 1411]
འདིར་ཡང་།

[Block 1412 [VERSE]]
རྟགས་མེད་སོགས་དང་དཔེ་མེད་དང་། །
རྗེས་འགྲོ་ཕྱིན་ཅི་ལོག་ལ་སོགས། །
འབྲེལ་པར་མ་བསྟན་པ་ཡི་ཕྱིར། །
ཉེར་འཇལ་འབྲེལ་པ་ཅན་མ་ཡིན། །

[Block 1413]
ཞེས་བྱ་བ་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 1414 [HEADING]]
### རྩོད་པ་བསྒྲུབ་པ་ན་དཔེ། ^4-3-0

[Block 1415]
རྩོད་པ་བསྒྲུབ་པ༌[^1086]ན༌[^1087]དེ་དག་གི་འབྲེལ་པ་ངེས་པར་སྟོན་པ་ནི་དཔེ་སྟེ། གང་གི་བུམ༌[^1088]པ་བཞིན་ནོ་ཞེས་བརྗོད་པ་ལྟ་བུའོ། །

[Block 1416]
གང་གིས་འབྲེལ་བ་མི་སྟོན་པ་ནི། གང་རྩོལ་བ་ལས་བྱུང་བ་དེ་མི་རྟག་པའོ་ཞེས་འབྱུང་བ་ལྟ་བུའོ།[^1089] །

[Block 1417]
དེ་ལྟ་ན་ཡང་བུམ་པ་བཞིན་ནོ་ཞེས་བྱ་བ་དེ་ནི་མི་རིགས་ཏེ། བསྟན་པར་བྱ་བ་དཔེ་མ་ཡིན་པའི་ཕྱིར་དང་། དེ་ཙམ་གྱིས་མེད་ན་མི་འབྱུང་བ་ཉིད་མ་བསྟན་པའི༌[^1090]ཕྱིར་རོ། །

[Block 1418]
གཞན་ཡང་། དེ་དག་གི་ཞེས་བརྗོད་མི་བྱ། །ཅིའི༌[^1091]ཕྱིར་ཞེ་ན། ཕན་ཚུན་བསྒྲུབ་བྱ་ཉིད་མིན་ཕྱིར། །མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་ཉིད་དེ་གཉིས་ཀ་ལ་ཡོད་ན་ནི་ཇི་ལྟར་རྩོལ་བ་ལས་བྱུང་བའི་ཕྱིར་མི་རྟག་གོ་ཞེས་པ་བཞིན་དུ་མི་རྟག་པའི་ཕྱིར་རྩོལ་བ་ལས་བྱུང་ངོ་ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 1419]
དེའི་ཕྱིར་གཏན་ཚིགས་དེ་ཉིད་བསྒྲུབ་བྱ་དང་འབྲེལ་པར་སྟོན་པ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1420 [VERSE]]
ཆོས་མཐུན་ཙམ་གྱིས་ལྷན་ཅིག་ཏུ། །
རྒྱུ་བར་སྟོན་པ་ཡང་མ་ཡིན། །

[Block 1421]
མི་རྟག་པ་ལ་བརྟེན་པ༌[^1092]ཙམ་ཉིད་ཀྱིས་གཏན་ཚིགས་ཀྱི་མི་འཁྲུལ་བ་བསྟན་པར་ནུས་པ་ནི༌[^1093]མ་ཡིན་ནོ། །

[Block 1422]
དོན་གྱིས་གཞན་ཡང་བརྗོད་ཅེ་ན། །འདི་ལྟར་གང་རྩོལ་བ་ལས་བྱུང་བ་དེ་མི་རྟག་གོ་ཞེས་བརྗོད་པའི༌[^1094]དོན་གྱི་ཤུགས་ཀྱིས་རྟོག་པ༌[^1095]ལ་མེད་དོ་ཞེས་མཆོད་པ༌[^1096]ཡིན་ནོ་ཞེ་ན། དེ་ལྟ་ན་ནི་ཡང་། དེ་ལྟར་མི་མཐུན་ཕྱོགས་དེ་བརྗོད་མི་བྱ། །དོན་གྱིས་གོ་ན་ནི་བསྒྲུབ་བྱ་གྲུབ་པ༌[^1097]ཉིད་ཡིན་ན། གཏན་ཚིགས་དང་མི་མཐུན་པའི་ཕྱོགས་དག་གི་མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་ཞེས་བྱ་བ་འདིས་ཅི་ཞིག་བྱ།

[Block 1423 [VERSE]]
ཡིད༌[^1098]མི་འབྱུང་གི་འབྲེལ་པ་དེ། །
མི་མཐུན་ཕྱོགས་ཀྱིས་བསྟན་པ་ན། །
བསྒྲུབ་བྱ་མ་བཟུང་འགའ༌[^1099]ཡོད་མིན། །

[Block 1424]
འདི་ལྟར་རྟག་པ་རྩོལ་བ་ལས་མ་བྱུང་ངོ་ཞེས་སྒྲུབ་པའི་སྒོ་ནས་བསྟན་པ༌[^1100]རྩོལ་བ་ལས་བྱུང་བ་ཉིད་མི་རྟག་པ་ཉིད་ལ་གྲུབ་པ་ནི༌[^1101]ཅུང་ཟད་ཀྱང༌[^1102]མ་དོར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1425]
གཞན་ནི་དེ་ཡིས་སྒྲུབ་པའི་ཕྱིར། །དམ་བཅའ་མ་ཡིན་པ་ཉིད་ནི། །

[Block 1426]
དེས་དེ་རྟག་པ་རྩོལ་བ་ལས་མ་བྱུང་བ་ཉིད་ཀྱིས་བསྒྲུབས་པའི༌[^1103]ཕྱིར་རྩོལ་བ་ལས་བྱུང་བ་མི་རྟག་པ་སྒྲུབ་པ་འདིས་ནི་ཅུང་ཟད་ཀྱང་བྱས་པ་མེད་དོ། །

[Block 1427]
སྒྲུབ་པ་བསྟན་པ་ཉིད་ཀྱིས་ཀྱང་། །མི་འདོད་པ་ཡི་རྟག་པ་འཐོབ། །

[Block 1428]
གལ་ཏེ་འདི་ལྟར་རྟག་པ་ཉིད་དང་། རྩོལ་བ་ལས་མ་བྱུང་བ་དག་མེད་ན་མི་འབྱུང་བ་ཉིད་དུ་སྒྲུབ་པའི་སྒོ་ནས་སྟོན་པར་བྱེད་ན་ནི་དེས་གདོན་མི་ཟ་བར་རྟག་པ་ཁས་བླང་བར༌[^1104]བྱའོ། །

[Block 1429]
རྩོལ་བ་ལས་མ་བྱུང་བ་དང་རྟག་པ་དག་ཕན་ཚུན་མེད་ན་མི་འབྱུང་བར་ཡང་འགྱུར་རོ། །

[Block 1430]
ཇི་ལྟར་རྟག་པ་རྩོལ་བ་ལས་བྱུང་བ་མ་ཡིན་ནོ་ཞེས་པ་བཞིན་དུ་རྩོལ་བ་ལས་མ་བྱུང་བ་རྟག་པའོ་ཞེས་དེ་ལྟར་ཡང་འགྱུར་ཏེ། དེ་དང་མི་མཐུན་པའི་ཕྱོགས་དག་ཕན་ཚུན་འབྲེལ་བར་རབ་ཏུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1431]
དེ་ལྟར་ཡང་འདོད་པ་མ་ཡིན་ཏེ་དེ་དང་མི་མཐུན་པའི་ཕྱོགས་དག་ཏུ་མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1432]
གང་གི་ཕྱིར་གཉིས་ཀ་ལ་ནི་མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་མེད་པ་དེའི་ཕྱིར་དེ་དང་མི་མཐུན་པའི་ཕྱོགས་དག་གིས༌[^1105]འབྲེལ་པ་ཞེས་བརྗོད་པར་མི་བྱའོ། །

[Block 1433 [HEADING]]
### མ་གྲུབ་པའི་དོན་ཉིད་དཔེ། ^4-4-0

[Block 1434]
འདི་སྐད་དུ། བློ་ཉིད་དང་བུམ་པ་ཉིད་ཅེས་བྱ་བ་ལྟ་བུ་མ་གྲུབ་པའི་དོན་ཉིད་ནི་དཔེ་ཞེས་པའོ་ཞེས་བརྗོད་པ་ལ། འདིར་འབྲེལ་པ་ཙམ་བརྗོད་པའི་དཔེ་ཡིན་པའི་ཕྱིར་ངེས་པར་བསྟན་པ་སྒྲུབ་པའི་དོན་དུ་ཡིན་པ་དེས་ན་དཔེ་ལྟར་སྣང་བ་ཉིད་དུ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1435]
འདི་སྐད་དུ་གང་རྟག་པ་དེ་རེག་པར་བྱ་བ་མ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱ་སྟེ། འདི་དཔེ་ལྟར་སྣང་བའོ། །

[Block 1436]
རེག་པར་བྱ་བ་མ་ཡིན་པ་ཉིད༌[^1106]དང་། མེད་ན་མི་འབྱུང་བ་ཉིད་དུ་བསྟན་པར་ནི་ནུས་པ་མ་ཡིན་ནོ། །

[Block 1437]
གཅིག་པ་ཉིད་ནི་དཔེའི་སྐྱོན་མ་ཡིན་ནོ་ཞེས་བསྟན་ཟིན་ཏོ། །

[Block 1438]
གཅིག་ཉིད་མ་གྲུབ་པའི་དོན་ནི་དཔེའི་ངེས་པ༌[^1107]མ་ཡིན་ནོ་ཞེས་ཁོ་བོས་བསྟན་ཟིན་ཏོ། །

[Block 1439 [HEADING]]
### རིགས་པ་ཅན་གྱི་དཔེ། ^4-5-0

[Block 1440]
རིགས་པ་ཅན་རྣམས་ན་རེ་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་མཐུན་པ་ལས་ཆོས་དེ་རྟོགས་པའི་དཔེ་དཔེར་བརྗོད་པ་དང་། དེ་བཟློག་པ་ལས་དེ་ཕྱིན་ཅི་ལོག་ལས་སོ་ཞེས་ཟེར་རོ། །
--- END BLOCKS ---
