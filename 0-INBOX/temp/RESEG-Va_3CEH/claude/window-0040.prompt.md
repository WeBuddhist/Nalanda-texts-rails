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
སྣང་བར་བྱེད་པ་ནི་རབ་ཏུ་གསལ་བར་བྱེད་པའོ། །

[Block 1402]
མི་སྣང་བར་བྱེད་པ་ནི་རབ་ཏུ་མི་སྣང་བའོ། །

[Block 1403]
དབང་ཉིད་དུ་བྱེད་པ་ནི་ཇི་ལྟར་བདུད་སངས་རྒྱས་ཉིད་དུ་བྱེད་པ་ལྟ་བུའོ། །

[Block 1404]
གཞན་གྱི་རྫུ་འཕྲུལ་རབ་ཏུ་འཇོམས་པ་ནི་གཞན་གྱི་རྫུ་འཕྲུལ་ཟིལ་གྱིས་གནོན་པར་བྱེད་པའོ། །

[Block 1405]
སྤོབས་པ་སྦྱིན་པ་ནི་འདྲི་བ་ཉིད་ལའོ། །

[Block 1406]
དྲན་པ་སྦྱིན་པ་དང་། བདེ་བ་སྦྱིན་པ་ནི་ཉན་པས༌[^902]ཏིང་ངེ་འཛིན་སྦྱིན་པའོ། །

[Block 1407]
འོད་ཟེར་གཏོང་བའི་རྫུ་འཕྲུལ་ཆེན་པོ་ནི་འཇིག་རྟེན་གྱི་ཁམས་གཞན་ནས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སྡུད་པའོ། །

[Block 1408]
རྫུ་འཕྲུལ་ཆེན་པོ་མངོན་པར་སྒྲུབ་པ་ནི་ཆེན་པོར་གྱུར་པའི་རྫུ་འཕྲུལ་ཏེ། བསྟན་མ་ཐག་པ་དེ་དག་ཉིད་ཡིན་ཏེ་དེ་དག་ནི་ཉན་ཐོས་རྣམས་ལ་མེད་དོ། །

[Block 1409 [HEADING]]
#### དཀའ་བ་སྤྱོད་པ་རྣམ་པ་བཅུ། ^7-6-2-0

[Block 1410]
བྱང་ཆུབ་སེམས་དཔའ་ནི་དཀའ་བ་སྤྱོད་པ་ཡིན་ནོ་ཞེས་གསུངས་པའི་དཀའ་བ་སྤྱོད་པ་གང་ཡིན་ཞེ་ན། དཀའ་བ་སྤྱོད་པ་རྣམ་པ་བཅུ་པོ་དེ་དག་ཐམས་ཅད་ཀྱིས་བསྟན་པ་ཡིན་ནོ། །

[Block 1411]
དེ་ལ་མི་འབྱེད་པར་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པར་དཀའ་བ་སྤྱོད་པ༌[^903]ཞེས་བྱ་བ་ནི་མི་འབྱེད་པ་ནི་འདིར་མ་ཐར་པའོ། །

[Block 1412]
འདི་ལྟ་བུ་ནི་ཐར་པ་ཡིན་ཏེ། གང་འཁོར་བ་ལས་ཀྱང་མ་གྲོལ་ལ། དེ་ཉིད་དུ་ཀུན་ནས་ཉོན་མོངས་པ་ཡང་མ་ཡིན་པའོ། །

[Block 1413]
ལྷག་མ་དཀའ་བ་སྤྱོད་པ་དགུ་ནི་དོན་གོ་སླའོ། །

[Block 1414 [HEADING]]
#### དགོངས་ཏེ་གསུངས་པའི་དགོངས་པ། ^7-6-3-0

[Block 1415]
དགོངས་ཏེ་གསུངས་པའི་དགོངས་པ་བསྟན་པར་བྱ་སྟེ། དེ་ལ་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སྦྱིན་ཕོད་པ་ཡིན་ཞེ་ན་ཞེས་བྱ་བ་ལ། སེམས་ཅན་ཐམས་ཅད་བདག་ཉིད་ལྟ་བུར་རྟོགས་པས་དེའི་ཕྱིར་དེས་སྦྱིན་པ་བྱིན་པར་གྱུར་པ་མ་ཡིན་ནོ་ཞེས་དགོངས་སོ། །ཇི་ལྟར་ན་སྦྱིན་པ་འདོད་པ་ཡིན་ཞེ་ན། ཁ་ན་མ་ཐོ་བ་དང་བཅས་པའི་སྦྱིན་པ་ལ་སོགས་པ་ལ་འདི་ལྟར་འདོད་པ་མེད་པ་སྟེ། བྱང་ཆུབ་སེམས་དཔའི་སྦྱིན་པ་ཉིད་ལ་འདོད་པར་བྱེད་པས་རོ་མྱང་བ༌[^904]མེད་པའི་དོན་ཏེ། རོ་མྱང་བར་མི་བྱེད་ཅེས་བྱ་བར་བཞེད་དོ། །

[Block 1416]
དེས་ན་རོ་མི་མྱང་བ་ནི་རོ་མྱང་བ་མེད་པའི་སྦྱིན་པའོ། །

[Block 1417]
ཇི་ལྟར་ན་སྦྱིན་པ་ལ་མོས་པ་ཡིན་ཞེ་ན། གང་གི་ཕྱིར་བདག་ཉིད་ཀྱིས་སྦྱིན་པ་བྱེད་པ་ཐོབ་པ་ཡིན་གྱི། གང་གཞན་གྱི་རྐྱེན་གྱིས་འགྲོ་བ་མ་ཡིན་པའོ། །

[Block 1418]
ཇི་ལྟར་ན་སྦྱིན་པ་ལ་འཇུག་པར་བྱེད་པ་ཡིན་ཞེས་བྱ་བ་ལ། རང་བཞིན་གྱིས་སྦྱིན་པ་གཏོང་བ་ཡིན་ཞེས་བྱ་བ་དགོངས་པ་སྟེ། འདི་ལྟར་བདག་ཉིད་ཀྱིས་ཀྱང་འཇུག་པར༌[^905]དགོས་པ་མ་ཡིན་ཏེ།[^906] སེར་སྣ་ཤིན་ཏུ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 1419]
དེས་ན་གཞན་དག་བཞུགས་པ༌[^907]ལ་ཡང་ནུས་པ་དང༌[^908]ལྡན་པར་འགྱུར་རོ། །

[Block 1420]
ཇི་ལྟར་ན་སྦྱིན་པ་ལ་མངོན་པར་དགའ་བ་ཡིན་ཞེས་བྱ་བ་ལ། རེས་འགའ་ཞིག་འགའ༌[^909]སྦྱིན་པར་བྱེད་པ་མ་ཡིན་གྱི་རྟག་ཏུ་ཅི་བདོག་པ་སྦྱིན་པའོ། །

[Block 1421]
ཇི་ལྟར་ན་སྦྱིན་པ་ལ་ཆེ་བ་ཡིན་ཞེས་བྱ་བ་ལ། སྙིང་པོ་མེད་པ་ནི་རྣམ་པར་གཡེང་བ་མེད་པ་སྟེ། དེ་ནི་འདི་ལྟར་མཉམ་པར་བཞག་པས་སྦྱིན་ཞིང་གཡེང་བ་མེད་པས་སྦྱིན་པར་བྱའོ་ཞེས་བྱ༌[^910]བའི་ཐ་ཚིག་གོ། །

[Block 1422]
ཇི་ལྟར་ན་སྦྱིན་པ་དག་པ་ཡིན་ཞེས་བྱ་བ་ལ། འབྱུང་བ་ནི་རབ་ཏུ་གནས་པ་སྟེ། སེར་སྣ་རྩ་བ་ནས་འབྱིན་པར་བྱེད་པ་སྟེ། གལ་ཏེ་སེར་སྣ་རྒྱས་པར་གྱུར་ན་འབྱིན་པར་བྱེད་ཅིང་ཉེ་བར་འབྱིན་པར་བྱེད་པའོ། །

[Block 1423]
ཇི་ལྟར་ན་སྦྱིན་པ་མཐར་ཕྱིན་པ་ཡིན་ཞེ་ན་ཞེས་བྱ་བ་ལ། གལ་ཏེ་མཐའ་ཞེས་བྱ་བ་མྱ་ངན་ལས་འདས་པ་ལ། ཉན་ཐོས་བཞིན་དུ་གནས་པར་མ་གྱུར་ནའོ། །

[Block 1424]
འདི་ལྟར༌[^911]སྦྱིན་པ༌[^912]ལ་སོགས་པའི་མི་མཐུན་པའི་ཕྱོགས་དེ་དག་གི་དབང་དུ་གྱུར་པ་མ་ཡིན་ཏེ།[^913] དེས༌[^914]སྦྱིན་པ་ལ་སོགས་པའི་དབང་དུ་གྱུར་པ་ཡིན་ཏེ། དེའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་དབང་དུ་མ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1425]
ཇི་ལྟར་ན་སྦྱིན་པ་མི་ཟད་པ་ཡིན་ཞེས་བྱ་བ་ལ། ཟད་པ་མེད་པ་ནི་འདིར་མྱ་ངན་ལས་འདས་པ་ཡིན་པར་བཞེད་དེ། འདི་ལྟར་ཉན་ཐོས་བཞིན་དུ་མྱ་ངན་ལས་འདས་པ་ལ་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1426 [HEADING]]
#### ང་ནི་སྲོག་གཅོད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་དགོངས་པ། ^7-6-4-0

[Block 1427]
གང་མདོ་སྡེ་ལས་དགེ་སློང་དག་ང་ནི་སྲོག་གཅོད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་དེ་དག་གི་དགོངས་པ་གང་གིས་གསུངས་པ་དེ་སྟོན་པར་བྱེད་པ་སྟེ། ཇི་ལྟར་ན་འདོད་པས་ལོག་པར་སྤྱོད་པ་ཡིན་ཞེས་བྱ་བ་ལ། གང་གི་ཕྱིར་འདོད་པ་འདི་དག་ནི་ལོག་པ་ཡིན་ནོ་ཞེས་དེ་ལྟར་སྤྱོད་པའོ། །ཤེས་བྱའི་ཕ་རོལ་ཏུ་གནས་པ་ཞེས་བྱ་བ་ནི་ཤེས་བྱའི་ཕ་རོལ་ཏུ་ཕྱིན་པར་བྱས་ནས་གནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1428]
ཇི་ལྟར་ན་ལོག་པར་ལྟ་བ་ཅན་ཡིན་ཞེས་བྱ་བ་ལ། གང་ཐམས་ཅད་དུ་གཏོགས་པའི་གཟུགས་ལ་སོགས་པ་དག་ལོག་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཀུན་ཏུ་བརྟགས་པ་ཉིད་དང་། གཞན་གྱི་དབང་ཉིད་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་མཐོང་བ་སྟེ། ཀུན་ཏུ་བརྟགས་པ་ཉིད་ནི་གཞན་གྱི་དབང་ལས་ལོག་པ་ཉིད་དུ་མཐོང་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1429]
ལྷག་མ་མི་དགེ་བ་བཅུའི་ལས་ཀྱི་ལམ་རྣམས་ནི་གོ་སླའོ། །

[Block 1430 [HEADING]]
#### རྟག་པའི་ཆོས་རྣམས་ལ་སོགས་པའི་དགོངས་པ། ^7-6-5-0

[Block 1431]
ཡང་མདོ་གཞན་ལས་གསུངས་པའི་རྟག་པའི་ཆོས་རྣམས་ནི་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཏེ་ཞེས་བྱ་བ། མི་གོས་པའི་ཆོས་རྣམས་ནི་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཏེ་ཞེས་གསུངས་པའི་བར་ལ་དེ་དག་ལ་དགོངས་པ་གང༌[^915]ཡིན་ཞེ་ན། དེ་བསྟན་པར་བྱ་སྟེ། རྟག་པ་ནི་ཆོས་ཀྱི་སྐུའོ། །

[Block 1432]
དེ་བས་ན་ཆོས་དེ་ནི་རྟག་པའི་ཆོས་རྣམས་ཞེས་བསྟན་ཏོ། །

[Block 1433]
ཆད་པའི་ཆོས་རྣམས་ཞེས་བྱ་བ་ནི་སྒྲིབ་པ་ཇི་སྙེད་པ་དག་དེ་ལ་ཡོངས་སུ་ཆད་པར་གྱུར་པས་དེའི་ཕྱིར་དོན་དེས་ན་དེ་ནི་ཆད་པའི་ཆོས་རྣམས་ཞེས་བརྗོད་དོ། །

[Block 1434]
དམིགས་པའི་ཆོས་རྣམས་ནི་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཏེ་ཞེས་བྱ་བ་ལ། སེམས་ཅན་གྱི་སྤྱོད་པ་གཉེན་པོ་དང་བཅས་པ་སྟོང་ཕྲག་བརྒྱད་ཅུ་རྩ་བཞི་ཉེ་བར་དམིགས་པ་སྟེ། དེས་ན་ཆོས་དེ་ནི་དམིགས་པའི་ཆོས་རྣམས་སོ། །

[Block 1435]
མི་དགེ་བའི༌[^916]ཆོས་རྣམས༌[^917]ཞེས་བྱ་བ་ལ། སྒྲིབ་པ་ཐམས་ཅད་ཀྱིས་མི་གོས་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན༌[^918]ཉིད་དོ། །

[Block 1436]
དེའི་ཕྱིར་ཆོས་དེ་ནི་མི་གོས་པའི་ཆོས་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1437 [HEADING]]
#### ཏིང་ངེ་འཛིན་རྣམས་ཀྱི་ལས། ^7-6-6-0

[Block 1438]
ལས་ཀྱི༌[^919]རབ་ཏུ་དབྱེ་བ་མ་བསྟན་པས་དེའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཏིང་ངེ་འཛིན་རྣམས་ཀྱི་ལས་གང་ཡིན་པ་བསྟན་པར་བྱའོ། །

[Block 1439]
དེ་ལ་ཏིང་ངེ་འཛིན་ལ་ཡང་དག་པར་བརྟེན་ནས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་སྒོམ་པར་བྱེད་དོ། །

[Block 1440]
དེ་བཞིན་དུ་དེ་ལ་ཡང་དག་པར་བརྟེན་ནས་སེམས་ཅན་རྣམས་ཡོངས་སུ་སྨིན་པར་བྱེད་དོ།[^920] །རྫུ་འཕྲུལ་ལ་སོགས་པ་དག་གིས་འདུན་པར་བྱས་ནས་འཇུག་པར་བྱེད་དོ། །
--- END BLOCKS ---
