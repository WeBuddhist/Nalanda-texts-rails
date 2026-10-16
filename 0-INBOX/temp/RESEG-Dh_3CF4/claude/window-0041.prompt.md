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
[Block 1436]
བརྟུལ་ཞུགས་ཀྱིས་ནི༌[^818]བསྡམས་པ་ཡང་སྨོས་པ་ཡིན་ནོ། །

[Block 1437]
མི་འཚེ་བ་དང་། བདེན་པའི་ཚིག་དང་། མི་རྐུ་བ་དང་། རྟོག་པ་མེད་པ་ཉིད་དང་ཚངས་པར་སྤྱོད་པ་སྟེ། ལྔ་པོ་འདི་དག་ནི་བརྟུལ་ཞུགས་སོ། །

[Block 1438]
བསྡམས་པ་ནི་མི་ཁྲོ་བ་དང་། བླ་མ་ལ་སྲི་ཞུ་ཆེ་བ་དང་། གཙང་སྦྲ་དང་། སྤྱོད་པ་ཡང་བ་དང་། བག་ཡོད་པ་སྟེ་ལྔ་པོ་འདི་དག་ནི་བསྡམས་བ་ཞེས་བསྒྲགས་སོ། །

[Block 1439]
བྱ་དང་རི་དྭགས་རྣམས་ཀྱང་དེ་ལ་འཁོར་ཏེ། དེ་བས་ན་ཐུབ་པ་ཞེས་བྱ་བ༌[^819]སྟེ། རྒྱུ་འདིའི་ཕྱིར་རོ། །

[Block 1440]
འདིས་ནི་དེ་ལ་ཕན་པ་དེས་དཀའ་ཐུབ་ཅན་ཁྱད་པར་དུ༌[^820]གྱུར་པ་བསྟན་ཏོ། །

[Block 1441]
སྐྱེ་བོ་དཀའ་ཐུབ་ཅན་ལ་འོས་པ་ཞེས་བྱ་བ་ནི་རྒྱུ་ཕབ་པ་བསྟན་པ་དང་ལྡན་པའོ། །

[Block 1442]
འཚོ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྤ་བ་དང་། དྲེགས་པའི་ཕྱིར་མ་ཡིན་ནོ། །

[Block 1443]
ཇི་སྲིད་དེ་ལྟར་འདོད་པ་ལ་གནས་པ་ཞེས་བསྟན་པའི་རིམ་པས་སོ། །

[Block 1444]
ལྷའི་དབང་པོ་བརྒྱ་བྱིན་ཞེས་བྱ་བ་ནི་རང་གི་ངོ་བོ་དང་ཁྱད་པར༌[^821]ལས་བསྟན་ཏོ། །

[Block 1445]
ནུས་པ་ཡིན་པས་བརྒྱ་བྱིན་ཏེ། སྤྲོ་བ་དང་། གསང་ཚིག་དང་། གཙོ་བོའི་ནུས་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1446]
བརྒྱ་བྱིན་ཞེས་བྱ་བ་འདིས་ནི་རང་གི་ངོ་བོའི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 1447]
ལྷ་རྣམས་ཀྱི་དབང་པོ་ཞེས་བྱ་བས་ནི་ལས་ཀྱི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 1448]
ཡིད་བསམ་གཏན་ལ་ཞུགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དུས་གསུམ་དུ༌[^822]མི་སྣང་བའི་རྒྱུ་ཡིད་ལ་མི་བྱེད་པས་སོ། །

[Block 1449]
འདི་ལ་འཚོལ༌[^823]བའི་དུས་སུ་དེར་མི་སྣང་བའི་རྒྱུ་ཡིད་ལ་མི་བྱེད་པ་ཅིའི་ཕྱིར་ཞེ་ན། ཡིད་བསམ་གཏན་ལ་ཞུགས་པས་ཚོལ་བའི་དུས་སུ་ཡང་དེ་མི་སྣང་བའི་རྒྱུ་ཡིད་ལ་མི་བྱེད་དོ། །

[Block 1450]
ཅིའི་ཕྱིར་ཞེ་ན། ཆོག་ཤེས་པ་ལ་གོམས་པ་དང་། ཞེས་བྱ་བ་ནི་གང་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་དུས་ན་མི་སྣང་བའི་རྒྱུ་དེ་ཡིད་ལ་མི་བྱེད་པ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། ཁ་ཟས་ལ་རྨོངས་པ་མེད་པས་སོ། །

[Block 1451]
ཞེན་པ་མེད་པ་ཞེས་བྱ་བ་ནི་བསམ་པས་དོན་དུ་མི་གཉེར་བའོ། །

[Block 1452]
ཟས་ཁྱད་པར་ཅན་མི་འཚོལ་བ་ནི་སྦྱོར་བས་སོ། །

[Block 1453]
བློ་བདེ་བར་བྱས་ཏེ་གནས་སོ་ཞེས་བྱ་བ་ནི་རྒྱུ་གཉིས་པོ་དེས་སོ། །

[Block 1454]
དེ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྔ་མ་དེ་བཞིན་ནོ། །

[Block 1455]
ཤིང་དང་ཤིང་གི་ལོ་མའི་ཁ་ཟས་ཀྱིས༌[^824]བློ་བདེ་བར་གནས་པ་ཉིད་ཀྱི་རྒྱུ་བསྟན་པའི་ཕྱིར། ཆོག་ཤེས་ངེས་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 1456]
རྩྭ་དང་ལོ་མ་ཆུ་ཡི་གནས། །ཞེས་སྨོས་པས༌[^825]ནི་གསུམ་པོ་འདི་དག་ནི་འབད་པས་བསྐྱེད་མི་དགོས་པར་ཐམས་ཅད་ན་ཡང་ཡོད་པའི་ཕྱིར་ཐོབ་པ་ཉིད་ཀྱི་འཇུག་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 1457]
ལོ་མ་ལྷགས་ཤིང་རྙིངས་པ་ནི་ཅུང་ཟད་རློན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1458]
ཤིང་གི་ལོ་མའི་ཁ་ཟས་ཀྱིས་མི་དགའ་བ་མེད་པ་ནི་བློ་མི་དགའ་བ་མེད་པའོ། །

[Block 1459]
[^826]ངོམས་པའི་རྒྱུ་བསྟན་པའི་ཕྱིར་མང་དུ་ཐོས་པས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 1460]
ཚིགས་སུ་བཅད་པ་འདིའི་བསྡུས་པའི་དོན་ནི་ཁྱིམ་ན་གནས་པ་ཡང་རང་གི་བསོད་ནམས་དང་། ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ལ་འཇུག་པ་སྟེ། མངོན་པར་མཐོ་བ་དོན་དུ་གཉེར་བའོ། །

[Block 1461]
རབ་ཏུ་བྱུང་བ་ཡང་ངེས་པར་ལེགས་པ་དོན་དུ་གཉེར་བའོ། །

[Block 1462]
གང་དེ་དག་གི་དོན་རྩོམ་པ་དེའི་གཉེན་པོ་དང་རྗེས་སུ་མཐུན་པའི་ཡོན་ཏན་ཉེ་བའི་ཉོན་མོངས་པ་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1463]
སྙེམས་པ༌[^827]ནི་བདག་གིར་བྱེད་པ་སྟེ་བདག་གོ་ཞེ་ནའོ། །

[Block 1464]
དེས་ན་སྙེམས་པས་ནི་བདག་ལ་བསྟོད་པ་དང་གཞན་ལ་སྨོད་པར༌[^828]བྱེད་དེ། དེས་ན༌[^829]ཤེས་རབ་ཡོངས་སུ་ཉམས་པ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1465]
འབྱོར་པ་རྣམས་ལ་སེར་སྣས་ནི་ལོངས་སྤྱོད་བསགས་པ་དང་། ཕུན་སུམ་ཚོགས་པ་ཟད་པའི༌[^830]རྒྱུ་ཡིན་ནོ། །

[Block 1466]
ནགས་ཚལ་དུ་གནས་པ་ལ་ཆོག་མི་ཤེས་པས་ནི་ངེས་པར་ལེགས་པ་མི་འཐོབ་པོ། །ཐམས་ཅད་ལ་ཆགས་པ་མེད་པ་ལ་གོམས་པས་ནི་མྱ་ངན་ལས་འདའ་སྟེ། མྱ་ངན་ལས་འདས་པ་གསུམ་ཐོབ་པ་མངོན་པར་འདོད་པས་སོ། །

[Block 1467]
དྲོ་ལ་བབ་པའི་ཚེ་ཞེས་བྱ་བ་ནི་བཟའ་བའི་དུས་ཏེ། དུས་འདི་ལ་བཟའ་བ༌[^831]བྱའོ་ཞེས་པའོ། །

[Block 1468]
བརྟུལ་ཞུགས་ཀྱི་དུས་དེ་ནི་བརྟུལ་ཞུགས་ཀྱི་དུས་ཞེས་བྱའོ། །

[Block 1469]
ཟས་ཀྱི་དུས་ལ་བབ་པ་བསྟན་པ༌[^832]ཞེས་བྱ་བ་ནི་འདི་ནི་བདག་ཅག་གི་ཁ་ཟས་ཀྱི་དུས་སོ་ཞེས་སོ། །

[Block 1470]
མགྲོན་དུ་བོས་སོ་ཞེས་བྱ་བ་ནི་ཁྱེད་དང་འུ་བུ་ཅག་ལྷན་ཅིག་བཟའ་བར་བྱའོ་ཞེས་སོ། །

[Block 1471]
མིག་བགྲད༌[^833]བཞིན་ནི་འཛུམ་པ༌[^834]མཛེས་ཞེས་བྱ་བ་འདིས་ནི་ལུས་ཀྱི་ཁྲོ་གཉེར་དེའི་གཉེན་པོ་དགའ་བའི་མཚན་མ་ཉིད་བསྟན་ཏོ། །

[Block 1472]
ཡིད་འོང་རྣར་སྙན་ཚིག་གིས་དགའ་བར་བྱས་ནས་ནི། །ཞེས་བྱ་བ་ནི་ཚིག་རྩུབ་ཅིང་ཁྲོ་བའི་དངོས་པོ་དེའི་གཉེན་པོའི་ཚིག་ཕུན་སུམ་ཚོགས་པ་ཡང་བསྟན་ཏོ། །

[Block 1473]
དགའ་བས་ཚིམ་པར་གྱུར་ཞེས་བྱ་བ་འདིས་ནི་ཡིད་ཀྱི་རྣམ་པར་གྱུར་པའི་དངོས་པོ་དེའི་གཉེན་པོ་ཡིད་རབ་ཏུ་དགའ་བ་ཡང་བསྟན་ཏོ། །

[Block 1474]
ཡིད་རབ་ཏུ་དགའ་ནས་དེ་བཞིན་དུ་ཞེས་བྱ་བས༌[^835]ནི་ཇི་ལྟར་སྔ་མ་དེ་བཞིན་དུ་དེ་བྱེད་པར་བསྟན་ཏོ། །

[Block 1475]
སྦྱིན་པར༌[^836]འདོད་པའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་སྦྱོར་བ་འདོད་པ་ལ་ཞུམ་པ་མེད་པ་དང་ལྡན་པ་དེ་ཅིའི་ཕྱིར་ཞེ་ན། སྙིང་རྗེ་གོམས་པ་ལས་སྐྱེས་པས་སོ། །
--- END BLOCKS ---
