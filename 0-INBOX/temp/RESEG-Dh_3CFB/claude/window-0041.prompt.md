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
ཇི་ལྟར་ན་དངོས་པོའི་བདག་ཉིད་མི་དམིགས་པ་ལས་མེད་པ་གྲུབ་ཅེ་ན། མཐོང་བ་མེད་པ་དག་གི་རྒྱུ། །མི་སྲིད་པར་ནི་གྱུར་པ་ནི།[^1080] །

[Block 1437 [VERSE]]
སྣང་བའི་དངོས་པོ་མི་དམིགས་པའི། །
དངོས་པོ་མེད་པ་རྟོགས་པར་འགྱུར། །

[Block 1438]
གལ་ཏེ་དངོས་པོར་འགྱུར་ན་བདག་ཉིད་ཇི་ལྟ་བུ་འཛིན་པ་པོའི་བྱེད་པས་དམིགས་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1439]
དེ་མཐོང་བའི་གེགས་བྱེད་པ་ཅན་བར་ཆད་ལ་སོགས་པ་དག་མེད་ན་དམིགས་པ་ཁོ་ནར་འགྱུར༌[^1081]ལ། མི་དམིགས་ན་ནི་མེད་པ་ངེས་པར་འགྱུར་ཏེ། དེ་འདྲ་བར་འགྱུར་བ༌[^1082]དམིགས་པ་ལ་འཁྲུལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1440]
གཏན་ཚིགས་འདི་ཉིད་ནི་རྒྱུ་དང་ཁྱབ་པར་བྱེད་པ་དག་མེད་པ་ལ་རིག་པར་བྱའོ། །

[Block 1441 [VERSE]]
དངོས་པོ་འགལ་བ་ཡོད་ན་ཡང་། །
དེ་ཡོད་པ་ལ་གནོད་བྱེད་ཕྱིར། །
དེ་དང་འགལ་བ་དམིགས་པ་ནི། །
མེད་པ་ཉིད་དུ་ངེས་པར་འགྱུར། །

[Block 1442]
དངོས་པོ་གང་ཞིག་གང་དང་ལྷན་ཅིག་མི་གནས་ཏེ། དེ་དག་གི་ཉེ་བར་ལེན་པ་དག་ནི་ཕན་ཚུན་མི་མཐུན་པའི་རྟེན་ཉིད་ཀྱིས་རྩོམ་པ་འགལ་བའི་ཕྱིར་རོ། །

[Block 1443]
སྔར་ཇི་སྐད་བཤད་པ་བཞིན་དུ་འགལ་བ་དེ་དག་ནི་གཅིག་ཡོད་ན་ཡང་གཞན་མེད་པ་རྟོགས་པར་འགྱུར་རོ། །

[Block 1444]
འདི་ནི་མི་དམིགས་པ་ལས་ཐ་དད་པ་རྣམ་པར་གཞག་པར་བྱ་བ་མ་ཡིན་ཏེ། དེ་ཉིད་ལས་འགལ་བ་རྟོགས་པའི་ཕྱིར་དང་། འགལ་བ་ལས་ཀྱང་མེད་པ་སྒྲུབ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1445]
དེ་ལྟ་བུའི་རྣམ་པའི་མི་དམིགས་པ་ལས་མེད་པ་རྟོགས་པར་འགྱུར་བ་ནི་བླ་སྟེ། དེ་ཡང་ཇི་ལྟར་རྗེས་སུ་དཔག་པ་ཡིན་པར་འགྱུར། ཇི་ལྟར་ཡང་མི་འགྱུར། དཔེ་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར་ཏེ། འདི་ལ་ནི་དཔེ་ཅུང༌[^1083]ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1446]
ཅིའི་ཕྱིར་ནམ་མཁའི་མེ་ཏོག་ལ་སོགས་པ་ཉེ་བར་བརྗོད་པ་མེད་པ་ཞེས་བྱ་བ་དཔེ་མ་ཡིན་ནམ། དེ་མེད་པ་ཇི་ལྟར་ཁོང་དུ་ཆུད་པར་བྱ་ཞིང་གང་གིས་དེ་ལྟར་འགྱུར། གལ་ཏེ་མི་དམིགས་པ་ཁོ་ན་ལས་སོ་ཞེ་ན། དེ་ལ་ཡང་ཇི་ལྟར་ན་དཔེ་མེད་པ་ཅན་དག་གི་མེད་པ་ཉིད༌[^1084]དུ་གྲུབ་པ་འམ། དཔེ་དང་བཅས་པ་ཅན་ཉིད་ཡིན་ན་ནི་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་བ་དེ་ལྟར་ན་ཡང་རྟོགས་པར་མི་འགྱུར་རོ། །

[Block 1447]
དེ་བས་ན་ཉེ་བར་བརྗོད་པ་མེད༌[^1085]པར་གྲུབ་པ་དང་འདྲ་བར་གཞན་ལ༌[^1086]ཡང་དཔེ་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར། རྗེས་སུ་དཔག་པ་མ་ཡིན་ནོ། །

[Block 1448]
ཐོས་སུ་ཟིན་ཀྱང་ལྷ་རྣམས་དགའ་བས་ངེས་པར་གཟུང་བ་བསལ་བ་མེད་དོ། །

[Block 1449]
མེད་པའི་སྒྲ་དང་ཐ་སྙད་ཀྱི་རྒྱུ་མཚན་དམིགས་པ་མི་དམིགས་པ༌[^1087]དེ་ནི་བདག་ཉིད་ཐག་ཉེ་བའི་ཕྱིར་རང་གི་རྒྱུ་མཚན་ཅན་དེ་དག་སྒྲུབ་པར་བྱེད་པས་རང་གི་རྒྱུ་མཚན་གྱི་ཚོགས་པའི་རུང་བ་ཐག་ཉེ་བ་ཅན་ཐམས་ཅད་ནི་འདིར་དཔེ་ཡིན་ནོ། །

[Block 1450]
མེད་པ་ཉིད་ཀྱང་འདི་ལ་མི་དམིགས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1451]
དེ་ཉིད་ཀྱི་ཕྱིར། འདི་ནི་རྒྱུ་ལས་འབྲས་བུ་རྗེས་སུ་དཔག་པའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར། རང་བཞིན་གྱིས༌[^1088]གཏན་ཚིགས་ཀྱི་ནང་དུ་འདུས་པར་འགྱུར་རོ་ཞེས་འཆད་པར་འགྱུར་རོ། །

[Block 1452]
ཡོད་པའི་སྐྲ་དང་ཐ་སྙད་འགོག་པར་ཡང་ཚད་མ་ལོག་པས་རྒྱུ་མཚན་མ་ཚང་བ༌[^1089]ཅན་གྱི་མྱུ་གུ་ལ་སོགས་པ་དཔེ་ཡིན་གྱི། ཉེ་བར་བརྗོད་པ་མེད་པ་འབའ་ཞིག་ནི་མ་ཡིན་ནོ། །

[Block 1453]
ཉེ་བར་བརྗོད་པ་མེད་པ་ལ་ཡང་འཇུག་པ་འདི་ཉིད་འགོག་པ་ཡིན་ཏེ། མི་དམིགས་པའི་མཚན་ཉིད་ཅན་གྱི་མེད་པ་ཉིད་གྲུབ་པ་ཡིན་ནོ། །

[Block 1454]
རྒྱུ་མཚན་དང་དེ་མེད་པ་ཁས་བླངས་ནས་འཇུག་པ་དང་ལྡོག་པ་ལ་ལུགས་ལས་ཟློག༌[^1090]པར་བྱེད་པའི་རྨོངས་པ་དེ་ལ་ཇི་ལྟར་ཁས་བླངས་པ་བཞིན་དུ་ཉེ་བར་བརྗོད་པ་མེད་པ་འམ། གཞན་དང་འདྲ་བར་བསྟན་ཏོ།[^1091] །

[Block 1455]
གལ་ཏེ་རེ་ཞིག་དམིགས་པ་མེད་པ་དེ་ཉིད་ཇི་ལྟར་གྲུབ་ཅེ་ན། དེ་ནི་ཕྱིས་འཆད་པར་འགྱུར་རོ། །

[Block 1456]
རྗེས་སུ་དཔག་པ་གཞན་ལ་ཡང་བསྒྲུབ་པར་བྱ་བའི་ཆོས་ཀྱིས་ཁྱབ་པར་འདོད་ན་ཅིའི་ཕྱིར་དཔེས་རྟོགས་པར་བྱ་བ་ཡིན་ཏེ། ཁྱབ་པར་བྱ་བ་བསྟན་པ་ཉིད་ཀྱིས་ཁྱབ་པར་བྱེད་པ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1457]
གལ་ཏེ་དོན་ངེས་ཟིན་ཀྱང་དཔེ་ནི་དྲན་པའི་དོན་ཡིན་ནོ་ཞེ་ན། དེ་ནི་ཅིག་ཤོས་ལ་ཡང་མཚུངས་སོ། །

[Block 1458]
དེ་ནི་གཞན་ལ་མི་དམིགས་པ་ཙམ་ལས་མེད་པའི་ཐ་སྙད་རྟོགས་སུ་ཟིན་ཀྱང་འདི་ལ་རྨོངས་བའི་ཕྱིར་དྲན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1459]
ཅི་སྟེ་གང་འདི་ལ་གཙོ་བོ་ལ་སོགས་པ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 1460]
དེ་ལ་ཇི་ལྟར་མེད་པའི་ཐ་སྙད་གྲུབ་པའམ༌[^1092]ཡོད་པའི་ཐ་སྙད་འགོག་པར་ཇི་ལྟར་འགྱུར། དེའི་དོན་འགོག་པ་ན་རྗོད་པར༌[^1093]བྱེད་པ་ཆོས་ཅན་གྱི་ཚིག་མི་སྦྱོར་བའི་ཕྱིར་དང་། ཡུལ་མེད་པ་ཅན་གྱི་དགག་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1461]
ཉེས་པ་དེ་ནི་མེད་དེ་འདི་ལྟར།

[Block 1462 [VERSE]]
ཐོག་མེད༌[^1094]བག་ཆགས་ལས་བྱུང་བའི། །
རྣམ་པར་རྟོག་པས་ཡོངས༌[^1095]བསྒྲུབས་པ། །
ཡོད་མེད་གཉི་ག་ལ་བརྟེན༌[^1096]པ། །
སྒྲ་དོན་ཆོས་ནི་རྣམ་པ་གསུམ། །

[Block 1463 [VERSE]]
དེར་དངོས་ཉེར་ལེན་མེད་པ་ཅན། །
བསྒྲུབ་པ༌[^1097]དེ་མི་དམིགས་པ་ནི། །
དེ་ལྟར་གཏན་ཚིགས་དེ་ཉིད་ཀྱི། །
མེད་པ་མ་ཡིན་སྒྲ་སྦྱོར་ཕྱིར། །

[Block 1464]
ཇི་ལྟར་སྒྲ་དེ་དག་རང་གི་མཚན་ཉིད་ཀྱི་ཡུལ་ཅན་མ་ཡིན་པ་དེ་ལྟར་བསྟན་ཏོ། །

[Block 1465]
ཐོག་མ་མེད་པའི་དུས་ཅན་གྱི་བག་ཆགས་ལས་བྱུང་བ་ཅན་གྱི་རྣམ་པར་རྟོག་པ་ལ་སོ་སོར་སྣང་བའི་ངང་ཅན་གྱི་དོན་ཡུལ་ཉིད་དུ་བདག་གིར་བྱེད་དོ། །

[Block 1466]
རྣམ་པར་རྟོག་པ་དེ་ལ་བརྟེན་པའི་འཆད་པ་པོ་དང་ཉན་པ་པོ་ནི་དངོས་པོ་ཇི་ལྟར་སྣང་བ་བཞིན་དུ་སྟོན་པར་འདོད་པས་སྦྱོར་བའི་ཕྱིར་དང་། དེའི་རྣམ་པ་ཅན་གྱི་རྣམ་པར་རྟོག་པ་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 1467]
ཉེ་བར་ལེན་པ་དང་འབྲས་བུའི་ཤེས་པ་ལ་སྣང་བའི་ངོ་བོ་མ་ཡིན་པ༌[^1098]ནི་དེའི་ཡུལ་ཅན་ཉིད་དུ་ངེས་པར་ནུས་པ་མ་ཡིན་ནོ། །

[Block 1468]
རྣམ་པར་རྟོག་པ་དེ་ཡང་ཡོད་པ་དང་མེད་པ་དང་གཉི་གའི་ཤེས་པ་དག་གིས་བསྒོས་པའི་བག་ཆགས་ལས་བྱུང་བའི་ཕྱིར་དང་། དེར་སྣང་བའི་རྣམ་པར་ངེས་པའི་དབང་གིས་ཡོད་པ་དང་མེད་པ་དང༌[^1099]གཉི་གའི་ཆོས་ཞེས་བརྗོད་དོ། །

[Block 1469]
དེ་བས་ན་ཆོས་ཅན་འདི་ལ་བརྟེན་ནས་ཅི་གཙོ་བོའི་སྒྲ་ལས་སྣང་བའི་དོན་འདི་ནི་དངོས་པོ་ཉེ་བར་ལེན་པ་ཅན་ནམ༌[^1100]མ་ཡིན་ཞེས་ཡོད་པ་དང་མེད་པ་ཉིད་སྤྱོད་པར་བྱེད་དོ། །

[Block 1470]
དེ་ནི་དངོས་པོའི་ཉེ་བར་ལེན་པ་ཅན་མེད་པ་ཉིད་དུ་བསྒྲུབ་པར་བྱ་བ་ལ་དེ་ཉིད་དུ་སོ་སོར་རང་གི༌[^1101]རིག་པ་ཉིད་ཡིན་པའི་ཕྱིར། སྤང་བར་འོས་པ་མ་ཡིན་པའི་དོན་ནི་ཆོས་ཅན་ཡིན་ནོ། །

[Block 1471]
དོན་དེ་ཉིད་ཀྱང་རང་གི་མཚན་ཉིད་ཡིན་ནོ་ཞེས་བརྗོད་པར་མི་ནུས་ཏེ། མ་ཐོབ་པ་དང་འགགས་པའི་དོན་དག་ཀྱང་དེ་དང་མ་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1472]
དངོས་པོ་ལ་ཕྱིན་ཅི་ལོག་པའི་རྣམ་པ་ལ་མངོན་པར་ཞེན་པ་ཅན་གྱི་གཞན་མུ་སྟེགས་པའི་ཤེས་པ་དག་ལ་ཡང་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1473 [VERSE]]
དོན་དམ་ལ་གཅིག་ཕྱོགས་ཉིད་ཡོད། །
མཐོང་བའི་བྱེ་བྲག་ཐ་དད་པའི། །
དོན་རྣམས་ལ་ནི་སྒྲ་རྣམས་ཀྱིས། །
རྒྱུ་མེད་ཅན་འཇུག་མི་འགྱུར་དང་། །

[Block 1474 [VERSE]]
འདས་དང་མ་སྐྱེས་པ་ལ་ཡང་། །
ཚིག་འགའ་ཞིག་ཀྱང་བརྫུན་པ་ཡི། །
དོན་ཅན་ཉིད་དུ་མི་འགྱུར་ཕྱིར། །
དེ་དག་བློ་དོན་ཡུལ་ཅན་འདོད། །

[Block 1475]
ཅེས་བྱ་བ་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །
--- END BLOCKS ---
