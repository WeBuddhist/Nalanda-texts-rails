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
[Block 1471 [HEADING]]
###### ཚིགས་སུ་བཅད་པ་གསུམ་གྱིས་བཤད་པ། ^1-8-6-4-2-0

[Block 1472 [HEADING]]
###### **ལྟ་བ་བདག་མེད་པར་བཤད་པ།** ^1-8-6-4-2-1-0

[Block 1473]
དེ་ཡང་ཚིགས་སུ་བཅད་པ་ཕྱེད༌[^700]དང་གཉིས་ཀྱིས་ནི་ལྟ་བ་བདག་མེད་པར་བཤད་ལ། ཡང་ཚིགས་སུ་བཅད་པ་གཅིག་དང་ཚིག་རྐང་པ་གཅིག་གིས་ནི་སྒོམ་པ་བདེ་བའི་རྣམ་པ་བཤད་དོ། །

[Block 1474 [HEADING]]
###### **སྒོམ་པ་བདེ་བའི་རྣམ་པ་བཤད་པ།** ^1-8-6-4-2-2-0

[Block 1475]
དོན་འདི་ཡིས་ནི་བརྗོད་པར་བྱ། །ཞེས་པ་ནི་དེ་དག་གིས་བསྡུས་པ་སྟེ། ཆོས་ཀུན་དབང་པོ་རང་སྣང་དུ་བྱིན་གྱིས་བརླབས་པའི་ཚེ་ལྟ་བ་སྤྱིའི་མཚན་ཉིད་དང་། སྒོམ་པ་རང་གི་མཚན་ཉིད་དུ༌[^701]གྱུར་པའོ། །

[Block 1476 [HEADING]]
##### ཆེ་བའི་བདག་ཉིད། ^1-8-6-5-0

[Block 1477]
ད༌[^702]ནི་ཆེ་བའི་བདག་ཉིད་བསྟན་པའི་ཕྱིར་ཚིགས་སུ་བཅད་པ་གཉིས་གསུངས་པ་ལས།

[Block 1478 [HEADING]]
###### ཤེས་བྱ་ལྷན་ཅིག་སྐྱེས་པའི་ཡོན་ཏན། ^1-8-6-5-1-0

[Block 1479]
[^703] གཅིག་གིས་ནི་ཤེས་བྱ་ལྷན་ཅིག་སྐྱེས་པའི་ཡོན་ཏན་ཡིན་ལ།

[Block 1480 [HEADING]]
###### ཉམས་སུ་བླངས་པའི་ཡོན་ཏན། ^1-8-6-5-2-0

[Block 1481]
ཡང་གཅིག་གིས་ནི་ཉམས་སུ་བླངས་པའི་ཡོན་ཏན་ནོ། །

[Block 1482 [HEADING]]
##### སྤྱོད་ལམ་དང་བསྲེ་བའི་མན་ངག། ^1-8-6-6-0

[Block 1483]
ད་ནི་སྤྱོད་ལམ་དང་བསྲེ་བའི་མན་ངག་བསྟན་པའི་ཕྱིར། ཚིགས་སུ་བཅད་པ་གཅིག་སྟེ། དེ་ཡང་གོ་རིམས་ཅུང་ཟད་དཀྲུགས་ནས་ཕྱག་རྒྱ་ཆེན་པོ་མངོན་འདོད་པ་ནི་སྔར་བཞིན་དུ་མན་ངག་ཤེས་པས་སོ། །

[Block 1484 [VERSE]]
བཟའ་བཏུང་ནི་ལྷན་ཅིག་སྐྱེས་པའི་རོའོ། །
ཁྲུས་ནི་དབང་དུ་མོས་པའོ། །
སད་པ་ནི་ཐབས་ཀྱིས་སོ། །

[Block 1485]
ཉལ་བ་ནི་ཐབས་ཀྱིས་སྙོམས་པར་འཇུག་པའོ། །

[Block 1486]
དེས་ན་སྔོན་དུ་འགྲོ་བ་ནི་རྫོགས་རིམ་ལྷག་པར་མོས་པ་རྒྱུན་མི་འཆད་པའོ། །

[Block 1487 [HEADING]]
##### སྒོམ་པ། ^1-8-6-7-0

[Block 1488]
ད་ནི་སྒོམ་པ་བསྟན་པའི་ཕྱིར་ཡིད་ཀྱིས༌[^704]མི་བསྒོམ་པ་ནི་སྤྱོད་ཡུལ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1489]
ཆུ་འཛིན་ནམ་མཁའ་དང་འདྲ་བ་ཡུལ་མེད་པ་འདི་ཡང་སྟེ་དེ་ཡང་བྲིང་པའི་ཐབས་ཀྱིས་བྱའོ། །

[Block 1490]
དེ་ནས་ཕྱག་རྒྱ་ཆེན་པོ་བསྒོམ་སྟེ། ཡིད་དངས་པ་ཙམ་ནི་མ་ཡིན་ནོ། །

[Block 1491]
འགྲོ་བ་ཐམས་ཅད་བསྒོམ་པ་ནི་ལུས་ཅན་ཐམས་ཅད་ལ་ཕྱག་རྒྱ་ཆེན་པོ་ལྡན་པས་སོ། །

[Block 1492]
ཐམས་ཅད་ཆོས་ནི་ཡོངས་ཤེས་ནི་དེར་ཟག་པ་མེད་པ༌[^705]འབའ་ཞིག་ཏུ་སྣང་བའི་ཕྱིར་རོ། །

[Block 1493]
དེ་བསྡུ་བའི་ཕྱིར་སྒོམ་དུ་མེད་པ་ཉིད་ནི་རྣམ་པར་རྟོག་པ་མདུན་ན་གནས་པས་སོ། །

[Block 1494]
སྒོམ་པ་པོ་ནི་ཡེ་ཤེས་ཆེན་པོ་རྒྱབ་ན་གནས་པ་སྟེ། དེ་དག་ནི་བདེ་བ་ཆེན་པོ་བསྒོམ་པའི་ཐབས་སོ། །

[Block 1495 [HEADING]]
##### ཤེས་པ་བདག་མེད་པ། ^1-8-6-8-0

[Block 1496]
ད་ནི༌[^706]ཤེས་པ་བདག་མེད་པར་བསྟན་པའི་ཕྱིར་བརྟན་གཡོའི་དངོས་པོ་ནི་ཀུན་གཞིར་གྱུར་པའོ། །

[Block 1497]
རྩ་ལྕུག་ལ་སོགས་པ་ནི་དེར་གནས་པའི་ཆོས་ཅན་དེ་བདེ་བར་མཚོན་པའོ། །

[Block 1498]
བདག་གི་རང་བཞིན་ལས་ནི་ལྷན་ཅིག་སྐྱེས་པའི་བདེ་བའི་རང་བཞིན་ནོ། །

[Block 1499]
དམ་པ་དེ་ཉིད་ནི༌[^707]ཟག་པ་མེད་པའི་བདེ་བ་དང་སྦྱར་རོ། །

[Block 1500]
དེས་སྒོམ་ནི་བླ་མ་བརྒྱུད་པའམ་ཉམས་སུ་མྱོང་བ་གཅིག་པའོ། །

[Block 1501]
དེ་རྣམས་ནི་སྔར་གྱི་ཆོས་ཅན་དེ་རྣམས་སོ། །

[Block 1502]
གཅིག་ཉིད་ནི་བདེ་བའི་རོས་སོ། །

[Block 1503]
གཞན་ཡོད་མིན་ནི་སྣ་ཚོགས་མེད་ཅིང་སྟོང་པར་བྱས་པའོ། །

[Block 1504 [HEADING]]
##### དབྱེར་མེད་ཀྱི་འབྲས་བུ། ^1-8-6-9-0

[Block 1505]
ད་ནི་དབྱེར་མེད་ཀྱི་འབྲས་བུ་བསྟན་པའི་ཕྱིར་ཚིག་རྐང་གསུམ་སྟེ་རང་རིག་བདེ་ཆེན་ནི་རང་རིག་ཐབས་བསྡུས་པའོ། །

[Block 1506 [VERSE]]
རང་རིག་བྱང་ཆུབ་ནི་ཤེས་པས་བསྡུ་བའོ། །
རང་རིག་ཕྱིར་ན་བསྒོམ་པ་ནི།
དབྱེར་མེད་པའི་ཕྱིར་དེ་ཁོ་ན་བསྒོམ་པའོ། །

[Block 1507 [HEADING]]
##### ལྟ་བ་མངོན་རྟོགས། ^1-8-6-10-0

[Block 1508 [VERSE]]
ད་ནི་ལྟ་བ་མངོན་རྟོགས་ཀྱང་བསྟན་པའི་ཕྱིར།
རང་གི༌[^708]རིག་པ་ནི་གཉུག་མའི་རང་བཞིན་ནོ། །
འགྱུར་བ་ནི་ཐ་མལ་གྱི་གནས་སྐབས་སོ། །

[Block 1509]
དམན་པ་མི་བརྟག༌[^709]པ་ནི་གནས་སྐབས་ཀྱི་མངོན་པར་ཞེན་པའོ། །

[Block 1510]
ལས་ནི་བརྟག་པ༌[^710]སྟེ་དགེ་བ་དང་མི་དགེ་བའོ། །
--- END BLOCKS ---
