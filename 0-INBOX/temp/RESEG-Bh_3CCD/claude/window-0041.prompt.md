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
[Block 1436 [VERSE]]
སྣོད་དང་སེམས་ཅན་ཞེས་བྱ་བའི། །
འཇིག་རྟེན་གཉིས་པོ་འདི་བསྲེགས་ནས། །
དེ་ཡང་རང་ཉིད་དེ་ཉིད་དུ། །
མེ་སྒྲོན་བཞིན་དུ་ཞི་བར་འགྱུར། །

[Block 1437]
ཞེས་འབྱུང་ངོ་། །སྔོན་གྱི་སྨོན་ལམ་དང་སྙིང་རྗེ་ཆེན་པོས༌[^1008]བསྐུལ་བས་སེམས་ཅན་གྱི་དོན་འགྲུབ་པ་ཡིན་པས་ཆད་པའི་ཕྱོགས་མེད་དོ། །

[Block 1438]
སྤྲོས་པ་ཐམས་ཅད་དང་བྲལ་བའི་ཏིང་ངེ་འཛིན་ལ་རྟག་ཏུ་གཞོལ་བས་རྟག་པ་ཡང་མེད་དོ་ཞེས་སྟོང་པ་ཉིད་སྨྲ་བ་ཐེག་པ་ཆེན་པོ་པ༌[^1009]བདག་ཅག་རྣམས་ཀྱི་ཞི་གནས་དང་ལྷག་མཐོང་གི་བདག་ཉིད་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གྱི༌[^1010]ཕྱོགས་སོ། །

[Block 1439]
འོ་ན་མངོན་པར་འདུས་མ་བྱས་པའི་རྣམ་པར་ཐར་པ་ཡང་ཡོད་དེ་དེ་ཅིའི་ཕྱིར་མ་བསྟན༌[^1011]ཞེ་ན། དེ་ནི་ཡོད་པ་བདེན་ཏེ། འོན་ཀྱང་གསུམ་པ་ལ་གོམས་པས་འབད་པ་མེད་པར་ལྷུན་གྱིས་གྲུབ་པ་ཡིན་ཏེ་ཆུ་ཐིགས་བཞིན་ནོ། །

[Block 1440]
དེ་བས་དེ་ནི་བྱང་ཆུབ་ཀྱི་རྒྱུ་ཡིན་ཡང་ཤིན་ཏུ་ཉེ་བའི་ཕྱིར་འབྲས་བུ་ཡང་ཡིན་པ་ལ་སྐྱོན་གང་ཡང་མེད་དོ། །

[Block 1441]
དབུ་མ་པ་དེ་རྣམས་གལ་ཏེ་རང་བཞིན་མེད་པར་སྨྲ་ན་ཡང་སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོ་ནི་ཐབས་དུ་མས་ཁྱད་པར་དུ་འགྱུར་ཏེ། ཇི་སྐད་དུ།

[Block 1442 [VERSE]]
དོན་གཅིག༌[^1012]པ་ལ་མ་རྨོངས་ཕྱིར། །
ཐབས་མང་བས་ནི་དཀའ་ཐུབ་མེད། །
དབང་པོ་རྣོ་བའི་དབང་བྱས་ནས། །
སྔགས་ཀྱི་ཐེག་པ་ཁྱད་པར་འཕགས། །

[Block 1443]
ཞེས་འབྱུང་ངོ་། །དེ་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྣལ་འབྱོར་པས་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཀྱི༌[^1013]ངོ་བོ་ཉིད་དེ་ཁོ་ན་ཇི་ལྟར་ཐོབ་པ་བཞིན་དུ་སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོ་པ་རྣམས་ཀྱིས་ཀྱང་ཐོབ་པར༌[^1014]འགྱུར་རོ་ཞེས་འབྲས་བུ༌[^1015]ལོག་པར་རྟོག་པ༌[^1016]གང་ཡང་མེད་དོ། །

[Block 1444]
འོན་ཀྱང་དེ་རྣམས་ལ་རྨོངས་པ་ཡོད་དེ། དཔེར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཐུགས་རྗེའི་དབང་གིས་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་བྱ་བའི་ཕྱིར་དོན་གཉེར་བ་རྣམས་ལ་མགོ་བོ་ལ་སོགས་པ་སྦྱིན་པར་བྱེད་དེ། དེའི་དེས་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པར་མི་འགྱུར་ཏེ། སེམས་ཅན་གཅིག་ལ་ཕན་པ༌[^1017]ཡིན་གྱི་ཀུན་ལ་མེད་པའི་ཕྱིར་རོ། །

[Block 1445]
གང་གི་ཕྱིར་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ན༌[^1018]ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 1446]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་ནི༌[^1019]དགེ་བའི་འདུ་བྱེད་དེ༌[^1020]དག་གིས་གཞན་དང་གཞན་དུ་སྐྱེ་ཞིང་འཆི་འཕོ་བར་འགྱུར་རོ། །

[Block 1447]
དེ་བས་ན་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས་ཐོབ་པའི་བྱང་ཆུབ་ཅན་ནི༌[^1021]བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱའོ། །

[Block 1448]
སྔགས་ཀྱི་ཐེག་པ་ལ་གནས་པ་ལ་རྨོངས་པ་མེད་དེ། འགྲོ་བ་གསུམ་པོར་དེས་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྤྲོ་བ་ལ་སོགས་པའི་རིམ་གྱིས་ཅིག་ཅར་དུ་རྫོགས་པའི་ཕྱིར་རོ། །

[Block 1449]
སེམས་ཅན་གྱི་བསོད་ནམས་ཀྱི་བདག་པོའི་རྐྱེན་དང་དེ་རྣམས་ཀྱི་སྐལ་བ་ཉིད་ཀྱིས་ཀྱང་བསམ་པ༌[^1022]ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ། །

[Block 1450]
ཇི་སྐད་དུ།

[Block 1451 [VERSE]]
ལྷ་ཡི་དབང་པོས་ཆར་ཕབ༌[^1023]ཀྱང་། །
ས་བོན་ངན་པ༌[^1024]སྐྱེ་མི་འགྱུར། །
སངས་རྒྱས་རྣམས་ནི་བྱུང་ན་ཡང་། །
སྐལ༌[^1025]མེད་པས་ནི་འབྲས་མི་ཐོབ། །

[Block 1452]
ཅེས་འབྱུང་ངོ་། །དེ་ཉིད་ཀྱི་ཕྱིར་དེས་ནི་སྐད་ཅིག་མ་གཅིག་གིས་བྱང་ཆུབ་པ་ཡིན་ནོ། །

[Block 1453]
དེ་བཞིན་དུ་ཉན་ཐོས་པ་རྣམས་ཀྱིས༌[^1026]འབྲས་བུ་དང་ཐབས་ཡང་དག་པ་མ་ཡིན་ཏེ། མི་སྡུག་པ་ལ་སོགས་པ་བསྒོམས༌[^1027]པས་ཆོས་ཀྱི་དབྱིངས་ཐོབ་པར་མི་འགྱུར་ཏེ། དེས་ཀེང་རུས་ལ་སོགས་པ་ཙམ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 1454]
དེ་ཡང་དེ་ཁོ་ན་ཉིད་མ་ཡིན་ནོ། །

[Block 1455]
མར་མེ་ལྟ་བུ་མྱ་ངན་ལས་འདས་པ་ཚད་མ་གཉིས་དང་བྲལ་བ་རང་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ་མེད་པ་གང་ཡིན་པ་དེ་ཡང་དེ༌[^1028]ཁོ་ན་ཉིད་དུ་བསྟན་པ་མ་ཡིན་ཏེ། མཐོང་བའི་ཆོས་ཀྱིས་དེ་ཁོ་ན་ཉིད་མི་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 1456]
ཐེག་པ་ཆེན་པོ་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་ངོ་བོ་གཅིག་ཡིན་མོད་ཀྱི་འོན༌[^1029]ཀྱང་ཐབས་ནི་གཅིག་ཁོ་ན་སྟེ། རྣམ་པར་ཐར་པའི་སྒོ་ནས་སྟོང་པ་ཉིད་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 1457]
དེ་ཡང་བརྟགས་པ་པ་ཡིན་ཏེ། གཅིག་དང་དུ་མ་ལ་སོགས་པའི་གཏན་ཚིགས་ཀྱིས་དེ་རྟོགས་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1458]
མོས་པ་དང་རིགས་དང་བག་ཆགས་དང་བག་ལ་ཉལ་བ་དང་། བསམ་པ་སྣ་ཚོགས་པའི་སེམས་ཅན་གྱི་ཁམས་ལ་ལམ་གཅིག་བསྟན་པ་ནི་མི་འདོད་པའི་ཕྱིར་རོ། །

[Block 1459]
དེ་བཞིན་དུ་ཐེག་པ་ཆེན་པོ་པ་རྣམས་ཀྱིས་ཀྱང་དཀའ་ཐུབ་དང་མགོ་ལ་སོགས་པ་སྦྱིན་པ་དང་། སྟོང་པ་ཉིད་བཅོ་བརྒྱད་བསྒོམ་པ་དང་། བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས་བྱང་ཆུབ་ཐོབ་པའི་ཕྱིར་སངས་རྒྱས་ཉིད་ཐོབ་པར་འགྱུར་རོ། །

[Block 1460]
དེ་བཞིན་དུ་སྔགས་ཀྱི་ཐེག་པའི་སྤྱོད་པ་དང་ལྡན་པས་དཀའ་ཐུབ་དང་བརྟུལ་ཞུགས་ལ་མི་བརྟེན་ཏེ། དེ་རྣམས་ཀྱིས༌[^1030]འདོད་པའི་ཡོན་ཏན་ལྔས་སྤྱོད་པའི་སྒོ་ནས་དེ་ཉིད་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 1461]
ལེའུ་ལྔ་པ་ལས་ཀྱང་།

[Block 1462 [VERSE]]
དཀའ་ཐུབ་ཉེས་པ་མ་རུངས་ལ། །
རྟེན་པར་བྱེད་པས་འགྲུབ་མི་འགྱུར། །
འདོད་པའི་ཡོན་ཏན་ལོངས་སྤྱོད་ལ། །
བརྟེན་པས་མྱུར་དུ་འགྲུབ་པར་འགྱུར། །

[Block 1463]
ཞེས་འབྱུང་ངོ་། །གཞན་ལས་ཀྱང་། དཀའ་ཐུབ་ཉེས་པ་མ་རུངས་པས།

[Block 1464 [VERSE]]
སྡུག་བསྔལ་དང་ལྡན་ལུས་སྐམ་འགྱུར། །
སྡུག་བསྔལ་གྱིས་ནི་སེམས་གཡེངས་ཏེ། །
གཡེངས་པས༌[^1031]དངོས་གྲུབ་ཐོབ་མི་འགྱུར། །

[Block 1465]
ཞེས་འབྱུང་ངོ་། །

[Block 1466]
དེ་བཞིན་དུ་ཐེག་པ་ཆེན་པོ་པ་རྣམས་ནི་དབང་པོ་རྣོ་བ་མ་ཡིན་ཏེ། དེ་རྣམས་ཀྱི་དད་པ་ལ་སོགས་པའི་ཡོན་ཏན་རྣམས་དམན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1467]
དེ་ལྟར་ཇི་སྲིད་ཐ་མལ་པའི་ལུས་མ་སྦྱངས་པ་དེ་སྲིད་དུ་ཐ་མལ་པ་མ་ཡིན་པའི་རྡོ་རྗེའི་སྐུའི་མཚན་ཉིད་ཀྱི་སངས་རྒྱས་ཉིད༌[^1032]ཐོབ་པར་མི་འགྱུར་རོ། །

[Block 1468 [VERSE]]
དེ་ཡང་ཐེག་པ་ཆེན་པོ་ལ་མེད་དེ། །
ལྷའི་རྣམ་པ༌[^1033]བསྒོམ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1469]
དེ་མི༌[^1034]བསྒོམ་པ་ནི་དབང་པོ་རྣོ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1470]
ལུས་གང་གི་ཐ་མལ་པ་འཆིང་བ་དེ་ཉིད་ཀྱི་རྣམ་པར་སྦྱང་བ་དང་ཡོངས་སུ་ཤེས་ན་གྲོལ་བར་འགྱུར་རོ། །

[Block 1471]
དེ་ཡང་།

[Block 1472 [VERSE]]
[^1035]རྨོངས་པ་གང་གིས་འཆིང་བ་ནི། །
མཁས་པ་དེས་ནི་རབ་ཏུ་གྲོལ། །
དེ་ལྟར་བྱང་ཆུབ་བསྒོམ་པའི༌[^1036]ཕྱིར། །
ཐབས་འདི་ཐམས་ཅད་ལོག་པ་ཡིན། །

[Block 1473]
ཞེས་འབྱུང་ངོ་། །

[Block 1474 [VERSE]]
གང་དང་གང་གིས་སྐྱེ་བོ་རྣམས། །
མི་བཟད་ལས་ཀྱིས་འཆིང་འགྱུར་བ། །
ཐབས་དང་བཅས་པ་དེ་ཉིད་ཀྱིས། །
སྲིད་པའི་འཆིང་བ་ལས་གྲོལ༌[^1037]འགྱུར། །

[Block 1475]
ཞེས་འབྱུང་ངོ་། །འོད་སྲུངས་འདི་ལྟ་སྟེ། བུ་རམ་གྱི་ཤིང་དང་འབྲས་ཀྱི་ཞིང་རྣམས་ལ་ལུད་ཀྱི་ཕུང་པོ་ཕན་པར་གྱུར་པ་དེ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ལ་ཡང་ཉོན་མོངས་པ་ཁོ་ན་ཕན་པར་འགྱུར་ཞེས་གསུངས་པས་སོ། །
--- END BLOCKS ---
