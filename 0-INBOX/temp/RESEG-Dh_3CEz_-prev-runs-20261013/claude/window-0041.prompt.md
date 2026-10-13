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
[Block 1436 [VERSE]]
དེ་དག་ཇི་ལྟར་ཞེ་ན། །
དགའ་བ་ལས་ནི་དང་པོའོ། །

[Block 1437]
དཔའ་བོ༌[^689]ཉིད་ནི་སྐྱེས་བུ་ཐབས་ཀྱི་ལྷན་སྐྱེས་སོ། །

[Block 1438]
མཆོག་ཏུ་དགའ་བ་གཉིས་པའོ། །

[Block 1439 [VERSE]]
རྣལ་འབྱོར་མའི་བཙུན་མོ་ཤེས་རབ་ཀྱི་ལྷན་སྐྱེས་སོ། །
ཤིན་ཏུ་བདེ་དགའ་ནི་དགའ་བྲལ་གྱི་གསུམ་པའོ། །
ཐམས་ཅད༌[^690]དེས་ནི་ཀུན་རྫོབ༌[^691]མཚོན་བྱེད་ལྷན་སྐྱེས་སོ། །

[Block 1440]
དེ་བདེ་ཐབས་ལས་ནི་དགའ་བས་ལྷན་སྐྱེས་ཏེ་བཞི་པའོ། །

[Block 1441]
ཐམས་ཅད་རིག་ནི་དོན་དམ་པའམ་མཚོན་བྱ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1442 [HEADING]]
##### ལྷན་ཅིག་སྐྱེས་པའི་བསྒོམ་བྱའི་རིམ་པ་རྒྱུ་དང་འབྲས་བུའི་གནས་སྐབས་ཀྱིས་བསྟན་པ། ^1-8-6-3-0

[Block 1443]
ད་ནི་ལྷན་ཅིག་སྐྱེས་པའི་བསྒོམ་བྱའི་རིམ་པ་རྒྱུ་དང༌[^692]འབྲས་བུའི་གནས་སྐབས་ཀྱིས་བསྟན་པའི་ཕྱིར། དགའ་བ་བདེ་བ་ཅུང་ཟད་དེ། ཞེས་བྱ་བ་ནི་བདེ་བ་རང་གི་མཚན་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1444]
མཆོག་དགའ་ལྷག་མ་ནི་ཤེས་པ་རང་རིག་གི༌[^693]མཚན་ཉིད་ལ་སྒྲོ་བཏགས་པའོ། །

[Block 1445]
དགའ་བྲལ་ཆགས་བྲལ་ནི་གཉུག་མ་ལས་ཉམས་པའི་ཕྱིར་རོ། །

[Block 1446]
ལྷག་མ་ནི་ཡོངས་སུ་ལྷག་མ་སྟེ་དེ་གསུམ་ཆར་གྱི་རྣམ་པའི་མཆོག་དང་ལྡན་པས་སོ། །

[Block 1447]
ཡང་དང་པོ་རེག་པར་འདོད་པ་ནི་རྟེན་ཤེས་རབ་མ་སྟེ་གཉུག་མ་ཡུལ་དུ་བྱས་པས་སོ། །

[Block 1448]
གཉིས་པ་བདེ་བ་འདོད་པ་ནི་ཡིད་ཀྱི་ཡུལ་ལ་ཚིམ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1449]
འདོད་ཆགས་འཇིག་པ༌[^694]ཡང་གཉུག་མ་ལས་ཉམས་པའོ། །

[Block 1450]
བཞི་པ་བསྒོམ་པ་ནི་དགའ་བ་གསུམ་གྱི༌[^695]རྣམ་པ་ལྷན་ཅིག་སྐྱེས་པའི་རོར་བྱས་པའི་ཕྱིར་རོ། །

[Block 1451]
རང་གི་རྒྱུ་དང་གཞན་གྱི་རྐྱེན་གྱི་འབྲས་བུ་སྐྱོན་དང་ཡོན་ཏན་ཅིར་འགྱུར་ཞེ་ན།

[Block 1452 [VERSE]]
མཆོག་དགའ་སྲིད་པ་ཞེས་པ༌[^696]ནི་ཞེན་ཅིང་ཆགས་པའོ། །
དགའ་བྲལ་མྱ་ངན་ནི་ཉན་ཐོས་ལྟ་བུའོ། །
དབུ་མ་དགའ་བ་ནི་བཏང་སྙོམས་ཀྱི་འབྲས་བུའོ། །

[Block 1453]
ལྷན་ཅིག་སྐྱེས་པ་འདི་དག་སྤངས་པ་ནི་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 1454 [VERSE]]
འོ་ན་ལྷན་ཅིག་སྐྱེས་པ་ཅི་ཞེ་ན། །
འདོད་ཆགས་མེད་ཅིང་གཉུག་མའི་མཚན་ཉིད་གྲུབ་པ་སྟེ།

[Block 1455]
མཆོག་དགའ་ནི་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 1456]
ཆགས་བྲལ་མེད་པ་ནི་རང་གི་མཚན་ཉིད་ལས་མ་ཉམས་པ་སྟེ། དགའ་བྲལ་དུ་མི་རྟོག་པའོ། །

[Block 1457]
དབུས་མར་མི་དམིགས་པ་ནི་བདེ་བ་བཏང་སྙོམས་སུ་མི་གནས་པ་སྟེ། དགའ་བྲལ་མི་རྟོག་པའོ། །

[Block 1458 [VERSE]]
དེ་དག་ནི་རང་གི་རྒྱུའོ། །
འདི་ལ་ནི་ལྷན་སྐྱེས་སོ། །
ཐབས་ནི་སྐྱེས་བུའི་བྱེད་པའི༌[^697]མཆོག་དགའོ། །

[Block 1459 [VERSE]]
ཤེས་རབ་ནི་བཙུན་མོའི་བྱ་བ་དགའ་བྲལ་ལོ། །
དེ་གཉིས་ཀའི་དགའ་བ་སྟེ་དགའ་བྲལ་ལོ། །

[Block 1460]
ཡང་དག་དེ་ཉིད་སྣང་བ་ནི་འབྲས་བུ་འཁོར་བ་དང་ཞི་བ་དབྱེར་མེད་པའི་མི་གནས་བའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 1461]
འོ་ན་ལྷན་ཅིག་སྐྱེས་པ་དེ་རྒྱུད་ལ་ཇི་ལྟར་སྐྱེ་ཞེ་ན། བདེན་ཏེ༌[^698]མཉམ་པའམ་ལྟ་བའི་རོ་མཉམ་པ་དེ། ཤུགས་ལས་རོ་མཉམ་བསྒོམས་པས་བདེ་བ་མངོན་སུམ་དུ་སྐྱེ་སྟེ། གཞན་གྱིས་བརྗོད་མིན་ཞེས་པ་ནི་ལུང་དང་བླ་མས་སོ། །

[Block 1462]
གང་དུ་མི་རྙེད་པ་ནི་ཆོས་གང་ལ་མི་གནས་པའོ། །

[Block 1463]
འོན་ཀྱང་བླ་མའི་དུས་ཐབས་བསྟེན་པས་ཏེ་ཕྱག་རྒྱ་ཆེན་པོའི་མན་ངག་ལས་སོ། །

[Block 1464]
བདག་གི་བསོད་ནམས་ཞེས་པ་ནི་རང་གི་ནང་ནས་སྣང་བའི་བྱིན་གྱིས་བརླབས་པའོ། །

[Block 1465 [HEADING]]
##### དབང་པོ་རང་སྣང་གི་མན་ངག། ^1-8-6-4-0

[Block 1466 [HEADING]]
###### ཚིགས་སུ་བཅད་པ་གཅིག་གིས་བསྟན་པ། ^1-8-6-4-1-0

[Block 1467]
ད་ནི་དབང་པོ་རང་སྣང་གི་མན་ངག་བསྟན་པའི་ཕྱིར། དམན་དང་འབྲིང་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་བསྟན་པ་དང་། ཚིགས་སུ་བཅད་པ་གསུམ་གྱིས་བཤད་པ་སྟེ། དམན་པ་ནི༌[^699]ངན་པའམ་ཕྲ་བ་ཡང་ན་རགས་པ་དང་ཕྲ་བ་འབྲིང་བོ། མཆོག་ནི་བཟང་བའམ་རགས་པ།

[Block 1468 [VERSE]]
འབྲིང་ནི་གཉིས་ཀ་མ་ཡིན་པའོ། །
ཡང་ལྟོས་ནས་གསུམ་དུ་བཤད་དོ། །

[Block 1469]
སྒྲ་ཡང་སྙན་པ་དང་མི་སྙན་པ་གཉིས་ཀ་ལ་བརྟེན་པའོ། །

[Block 1470]
དེ་བཞིན་དུ་དྲི་རོ་རེག་བྱ་ལ་ཡང་སྦྱར་རོ། །

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
--- END BLOCKS ---
