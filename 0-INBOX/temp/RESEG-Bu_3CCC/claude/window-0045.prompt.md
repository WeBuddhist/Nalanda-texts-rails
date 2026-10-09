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
[Block 1576]
འདི་ལྟར་དངོས་པོ་གཞན་དུ་འགྱུར་བ་གང་ཡིན་པ་དེ་དངོས་པོ་མེད་པ་ཡིན་ནོ། །ཞེས་སྐྱེ་བོ་དག་སྨྲ་ན། དངོས་པོ་དེ་ཡང་མེད་དེ། དེ་མེད་ན་དངོས་པོ་མེད་པ་དེ་གང་གི་ཡིན་པར་འགྱུར། དངོས་པོ་མེད་པ༌[^1027]ན་ཁྱོད་ཀྱི་དེའི་གཉེན་པོ་དངོས་པོ་འཐད་པར་ག་ལ་འགྱུར།

[Block 1577]
སྨྲས་པ། འདི་ལ་དེ་ཁོ་ན་མཐོང་བས་ཐར་པར་འགྱུར་རོ། །ཞེས་བྱ་ཞིང་། དེ་ཁོ་ན༌[^1028]ཞེས་བྱ་བ་ཡང་དེའི་དངོས་པོ་ནི་དེ་ཁོ་ན་སྟེ།[^1029] དངོས་པོའི་ངོ་བོ་ཉིད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1578]
དེ་ལ་གལ་ཏེ་དངོས་པོའི་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཡིན་ན་དེ་ལྟ་ན་ཁྱོད་ལ་དེ་ཁོ་ན་མཐོང་བ་མི་འཐད་པར་མི་འགྱུར་རམ། དེ་ཁོ་ན་མཐོང་བ་མེད་ན་ཐར་པ་འཐད་པར༌[^1030]ཇི་ལྟར་འགྱུར། དེ་ལྟ་བས་ན་དངོས་པོ་རྣམས་ངོ་བོ་ཉིད་མེད་པ་ཞེས་བྱ་བར་ལྟ་བ་དེ་ནི་བཟང་པོ་མ་ཡིན་ནོ། །

[Block 1579]
བཤད་པ། ལོག་པར་མ་འཛིན་ཅིག །

[Block 1580 [VERSE]]
གང་དག་དངོས་ཉིད་གཞན་དངོས་དང་། །
དངོས་དང་དངོས་མེད་ཉིད་ལྟ་བ། །
དེ་དག་སངས་རྒྱས་བསྟན་པ་ལ། །
དེ་ཉིད་མཐོང་བ་མ་ཡིན་ནོ། །

[Block 1581]
གང་དག་དེ་ལྟར་ངོ་བོ་ཉིད་དང་གཞན་གྱི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ཉིད་ལྟ་བ་དེ་དག་ནི་འདི་ལྟར་ཡང༌[^1031]སངས་རྒྱས་ཀྱི་བསྟན་པ་མཆོག་ཏུ་ཟབ་པ་ལ་དེ་ཁོ་ན་མཐོང་བ་མ་ཡིན་ནོ། །

[Block 1582]
ཁོ་བོ་ཅག་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཉི་མ་ཤར་བས་སྣང་བར་གྱུར་པའི༌[^1032]དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་མཐོང་བས་དེའི་ཕྱིར་ཁོ་བོ་ཅག་ཉིད་ལ་དེ་ཁོ་ན་མཐོང་བ་ཡོད་པས་ཁོ་བོ་ཅག་ཁོ་ན་ལ་ཐར་པ་ཡང་འཐད་དོ། །

[Block 1583]
གལ་ཏེ་དེ་ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 1584 [VERSE]]
བཅོམ་ལྡན་དངོས་དང་དངོས་མེད་པ། །
སྟོན་པས་ཀ་ཏ༌[^1033]ཡ་ན་ཡི། །
གདམས་ངག་ལས་ནི་ཡོད་པ་དང་། །
མེད་པ་གཉི་གའང་དགག་པ་མཛད། །

[Block 1585]
གང་གི་ཕྱིར་བཅོམ་ལྡན་འདས་དོན་དམ་པའི་དེ་ཁོ་ན་ལ་མཁས་པ་དངོས་པོ་དང་དངོས་པོ་མེད་པར༌[^1034]རབ་ཏུ་སྟོན་པས་ཀ་ཏ༌[^1035]ཡ་ནའི་གདམས་ངག་ཅེས་བྱ་བའི་མདོ་ལས་ཡོད་པ་ཞེས་བྱ་བ་དང་མེད་པ་ཞེས་བྱ་བ་གཉི་ག་ཡང་དགག་པ་མཛད་པ་དེའི་ཕྱིར། གང་དག་དངོས་པོ་རྣམས་ལ་ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་དུ་རྗེས་སུ་ལྟ་བ་དེ་དག་གིས་དེ་ཁོ་ན་མི་མཐོང་བས་དེ་དག་ཉིད་ལ་ཡང་ཐར་པ་མི་འཐད་དོ། །

[Block 1586]
ཁོ་བོ་ཅག་ཡོད་པ་ཉིད༌[^1036]མེད་པ་ཉིད་ལ་མངོན་པར་ཞེན་པ་མེད་པར་ཐ་སྙད་བྱེད་པ་དག་ལ་ནི་མི་འཐད་པ་མེད༌[^1037]དོ། །

[Block 1587]
གལ་ཏེ་དངོས་པོ་དང་དངོས་པོ་མེད་པར་མཐོང་བ་དེ་ཁོ་ན་མཐོང་བ་ཡིན་ན་ནི་དེ་ཁོ་ན་ལ༌[^1038]མ་མཐོང་བ་འགའ་ཡང་མེད་པར་འགྱུར་བས་དེ་ནི་ཁོ་ན༌[^1039]མ་ཡིན་ནོ། །

[Block 1588]
དེ་ལྟ་བས་ན་དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ནི་དེ་ཁོ་ན་ཡིན་ལ་དེ་མཐོང་བ་ཁོ་ནས་ཐར་བར་འགྱུར་ཏེ། སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 1589 [VERSE]]
སྲིད་པའི་ས་བོན་རྣམ་ཤེས་ཏེ། །
ཡུལ་རྣམས་དེ་ཡི་སྤྱོད་ཡུལ་ལོ། །
ཡུལ་ལ་བདག་མེད་མཐོང་ན་ནི། །
སྲིད་པའི་ས་བོན་འགག་པར་འགྱུར། །

[Block 1590]
ཞེས་གསུངས་སོ། །

[Block 1591]
དེ་ནི་དེ་ལྟར་ངེས་པ་ཁོ་ནར་ཤེས་པར་བྱའོ། །

[Block 1592]
གཞན་དུ་ན།

[Block 1593 [VERSE]]
[^1040]གལ་ཏེ་རང་བཞིན་ཡོད་ཉིད་ན། །
དེ་ནི་མེད་ཉིད་མི་འགྱུར་རོ། །

[Block 1594]
གལ་ཏེ་དངོས་པོ་རྣམས་རང་བཞིན་གྱིས་ཡོད་པ་ཉིད་ཡིན་པར་གྱུར་ན་ཡོད་པ་ཉིད་རང་བཞིན་གྱིས་ཡོད་པ་དེ་ནི་ཕྱིས་མེད་པ་ཉིད་དུ་མི་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 1595 [VERSE]]
རང་བཞིན་གཞན་དུ་འགྱུར་བ་ནི། །
ནམ་ཡང་འཐད་པར་མི་འགྱུར་རོ། །

[Block 1596]
འདི་ལྟར་འགྱུར་བའི་གཉེན་པོ་ནི་རང་བཞིན་ཡིན་པས་དེའི་ཕྱིར་རང་བཞིན་ནི་མི་འགྱུར༌[^1041]རྟག་པ་ཡིན་པའི་རིགས་ན། དངོས་པོ་རྣམས་ལ་ནི་གཞན་དུ་འགྱུར་བ་སྣང་བས་དེའི་ཕྱིར་དེ་དག་ལ་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པ་ཉིད་མི་འཐད་དོ། །

[Block 1597]
འདིར་སྨྲས་པ། གལ་ཏེ་དངོས་པོ་མེད་པར་མཐོང་བ་ལས་དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་པར་ཁོང་དུ་ཆུད་པས་ན་རེ་ཞིག་དངོས་པོ་རྣམས་ཀྱི་དངོས་པོ་མེད་པར་གྱུར་པ་ཡིན་ནོ། །

[Block 1598]
བཤད་པ།

[Block 1599 [VERSE]]
རང་བཞིན་ཡོད་པ་མ་ཡིན་ན། །
གཞན་དུ་འགྱུར་བ་གང་གི་ཡིན། །

[Block 1600]
གང་གི་ཚེ་དངོས་པོ་རྣམས་ལ་ཡོད་པ་ཉིད་རང་བཞིན་གྱིས་མེད་དོ་ཞེས་སྨྲས་པ་དེའི་ཚེ། དངོས་པོ་རྣམས་ཀྱི་ཡོད་པ་ཉིད་རང་བཞིན༌[^1042]ཡོད་པ་མ་ཡིན་ན་གཞན་དུ་འགྱུར་བ་དེ་ཉིད་དེ་གང་གི་ཡིན་པར་འགྱུར། སྨྲས་པ། གལ་ཏེ་དངོས་པོ་རྣམས་ཀྱི་དངོས་པོ་མེད་པ་སྣང་ལ་རང་བཞིན་ཡང་ཡོད་པ་མ་ཡིན་ན་དངོས་པོ་མེད་པ་མི་འཐད་དེ་གང་གི་དངོས་པོ་མེད་པར་འགྱུར་བའི་དངོས་པོའི་རང་བཞིན་གདོན་མི་ཟ་བར་ཡོད་པ་ཉིད་དོ། །

[Block 1601]
བཤད་པ།

[Block 1602 [VERSE]]
རང་བཞིན་ཡོད་པ་ཡིན་ན་ཡང་། །
གཞན་དུ་འགྱུར་བ༌[^1043]ཇི་ལྟར་རུང་། །

[Block 1603 [VERSE]]
སྔར་ཡང་རང་བཞིན་གཞན་དུ་འགྱུར་བ་ནི།
ནམ་ཡང་འཐད་པར་མི་འགྱུར་རོ། །

[Block 1604]
འདི་ལྟར་འགྱུར་བའི་གཉེན་པོ་ནི་རང་བཞིན་ཡིན་པས་དེའི་ཕྱིར་རང་བཞིན་ནི་མི་འགྱུར་བར་རྟག་པར་འགྱུར་བའི་རིགས་ན། ཞེས་མ་བཤད་དམ། དེའི་ཕྱིར་དངོས་པོ་རྣམས་ཀྱི་མེད་པ་ཉིད་ཀྱང་མི་འཐད་དོ། །

[Block 1605]
དངོས་པོ་རྣམས་ལ་ཡོད་པ་དང་མེད་པ་ཉིད་དུ་ལྟ་བ་ལ་སྐྱོན་གཞན་འདིར་ཡང་ཐལ་བར་འགྱུར་ཏེ།

[Block 1606 [VERSE]]
ཡོད་ཅེས་བྱ་བ་རྟག་པར་འཛིན། །
མེད་ཅེས་བྱ་བ་ཆད་པར་ལྟ། །
དེ་ཕྱིར་ཡོད་དང་མེད་པ་ལ། །
མཁས་པས་གནས་པར་མི་བྱའོ། །

[Block 1607]
དངོས་པོ་ཡོད་དོ་ཞེས་དངོས་པོར་ལྟ་བ་དེ་ལ་ནི་རྟག་པར་འཛིན་པར་ཐལ་བར་འགྱུར་ལ། དངོས་པོ་མེད་དོ་ཞེས་མེད་པར་ལྟ་བ་དེ་ལ་ནི་ཆད་པར་ལྟ་བར་ཐལ་བར་འགྱུར་བས། དེ་གཉི་ག་ཡང་དོན་མེད་པ་དང་གནོད་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1608]
དེའི་ཕྱིར་ཡོད་པ་དང་མེད་པ་ཉིད་དུ་ལྟ་ན་རྟག་པ་དང་ཆད་པར་ལྟ་བར་ཐལ་བར་འགྱུར་བས། དེ་ཡང་དོན་མེད་པ་དང་གནོད་པར་འགྱུར་བས། དེའི་ཕྱིར་མཁས་པ་དེ་ཁོ་ན་རྟོགས་པར་འདོད་པ་འཁོར་བའི་དགོན་པ་ལས་རྒལ་བར༌[^1044]འདོད་པས་ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་ལ༌[^1045]གནས་པར་མི་བྱའོ། །

[Block 1609]
སྨྲས་པ། ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་དུ་ལྟ་ན་ཇི་ལྟར་རྟག་པ་དང་ཆད་པར་ལྟ་བའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར། བཤད་པ།

[Block 1610 [VERSE]]
གང་ཞིག་ངོ་བོ་ཉིད་ཡོད་པ། །
དེ་ནི་མེད་པ་མིན་པས༌[^1046]རྟག །
སྔོན་བྱུང་ད་ལྟར་མེད་ཅེས་པ། །
དེས་ན་ཆད་པར་ཐལ་བར་འགྱུར། །

[Block 1611]
འདི་ལྟར་གང་ཞིག་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པ་དེ་ནི་ཕྱིས་མེད་པ་ཉིད་དུ་མི་འཐད་དེ། རང་བཞིན་ནི་མི་འགྱུར་བས་དེའི་ཕྱིར་ཡོད་པ་ཉིད་དུ་ལྟ་བ་ལས་རྟག་པར་ལྟ་བར་འགྱུར་རོ། །

[Block 1612]
དངོས་པོ་དེ་སྔོན་དུ༌[^1047]བྱུང་བ་ལ༌[^1048]ད་ལྟར་མེད་དོ་ཞེས་དངོས་པོ་ཡོད་པ་ལ་འཇིག་པར་ལྟ་བ་དེས་ན་ཆད་པར་ལྟ་བར་འགྱུར་རོ། །

[Block 1613]
དེ་ལྟར་གང་གི་ཕྱིར་དངོས་པོ་རྣམས་ལ་ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་དུ་ལྟ་བ་སྐྱོན་དུ་མར་འགྱུར་བ་དེའི་ཕྱིར་དངོས་པོ་རྣམས་ངོ་བོ་ཉིད་མེད་པ་ཞེས་བྱ་བ་དེ་ནི་དེ་ཁོ་ན་མཐོང་བ་སྟེ་དབུ་མའི་ལམ་ཡིན་ལ་དེ་ཉིད་དོན་དམ་པ་འགྲུབ་པ་ཡིན་ནོ། །

[Block 1614]
དངོས་པོ་དང་དངོས་པོ་མེད་པ་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་བཅོ་ལྔ་པའོ།། །།

[Block 1615 [HEADING]]
## བཅིངས་པ་དང་ཐར་པ་བརྟག་པ། ^16-0
--- END BLOCKS ---
