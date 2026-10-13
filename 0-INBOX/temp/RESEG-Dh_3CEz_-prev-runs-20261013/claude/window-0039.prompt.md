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
[Block 1366]
དང་པོ་ནག་པོ༌[^659]རབ་ཏུ་བསྒོམ། །ཞེས་པ་ལ་སོགས་པ་ནི་སྙིང་གར་ཧཱུཾ་ནག་པོ་གཅིག །

[Block 1367 [VERSE]]
དམར་པོ་ནི་མགྲིན་པར་ཨཱཾ་ངོ་། །
སེར་པོ་ནི་དཔྲལ་བར་ཛྲཱྀཾ་ངོ་། །
ལྗང་གུ་ནི་ལྟེ་བར་ཁཾ་ངོ་། །
སྔོན་པོ་ནི་ནམ་ཚོང་དུ༌[^660]ཧཱུཾ་ངོ་། །

[Block 1368]
དཀར་པོ་ནི་སྤྱི་བོར་བྷྲཱུཾ་མོ། །

[Block 1369]
དེ་རྣམས་ནི་དེ་བཞིན་གཤེགས་པ་དྲུག་གི་ངོ་བོ་ཡང་རྫོགས་པའི་རིམ་པ་ལ་འཇུག་པའི་ཡན་ལག་ཏུ་དཀྱིལ་འཁོར་གྱི་ཁ་དོག་རིམ་པ་དྲུག་ཏུ་ཡང་བསྒོམ་སྟེ་རགས་པ་ལྷའི་ཞེན་པ་སྤོང་ངོ་། །རང་བཞིན་དེ་བཞིན་གཤེགས་པ་དྲུག་ཏུ་རྒྱས་གདབ་པའོ། །

[Block 1370]
དགའ་བྲལ་མཐར་ཡང་དེ་བཞིན་ནོ། །ཞེས་པ་ནི་ཟབ་པའི་རྣལ་འབྱོར་བསྟན་པ་སྟེ་འོག་ནས་རྒྱས་པར་འཆད་དོ། །

[Block 1371 [HEADING]]
#### རྫོགས་པའི་རིམ་པ་སྡུད་པར་བྱེད་པའི་མཚམས་སྦྱོར་བ། ^1-8-5-0

[Block 1372]
ད་ནི་རྫོགས་པའི་རིམ་པ་བཤད་པའི་ཕྱིར་ཚིགས་སུ་བཅད་པ་གཅིག་དང་ཚིག་རྐང་གཅིག་དང་ཤུགས་ཀྱིས་བསྟན་པ་གཅིག་གིས་ནི་སྡུད་པར་བྱེད་པའི་མཚམས་སྦྱོར་བ་ནི་གང་ཞིག་ཆོ་གའི་ཡན་ལག་གིས་ལྷ་བསྒོམ་པ་ནི་བསྐྱེད་པའི་རིམ་པའོ། །

[Block 1373]
ཡེ་ཤེས་མངོན༌[^661]དུ་སྐྱེ་བའི་ཐབས་ནི་རྫོགས་པའི་རིམ་པའོ། །

[Block 1374]
ཡང་ན་རྫོགས་པའི་རིམ་པའི་རྟེན་དུ་གྱུར་པ་དང་བསྐྱེད་པའི་རིམ་པ་བྱིན་གྱིས་རློབ་པས་ཀྱང་མཚན༌[^662]ཏེ། བསྐྱེད་པ་དང་བསྐྱེད་པའི་རིམ་པས༌[^663]རྫོགས་པ་དང་རྫོགས་པའི་རིམ་པ་ནི་མོས་པའི་རྣལ་འབྱོར་ནས་མངོན་པར་བྱང་ཆུབ་པའི་བར་དུ་རིམ་པ་ཁ་དོག་དང་དབྱིབས་ཀྱི་རྣམ་པ་ནི་བསྐྱེད་པའོ། །

[Block 1375]
ལས་ཀྱི་ཕྱག་རྒྱ་ནས་ཕྱག་རྒྱ་ཆེན་པོའི་བར་དུ་རྫོགས་པའི་རིམ་པའོ། །

[Block 1376]
ཡེ་ཤེས་དངོས་སུ་ཤར་བ་ནི་རྫོགས་པའོ། །

[Block 1377]
དེ་དག་ནི་དེ་ཁོ་ན་ཉིད་ནི་སྒྱུ་མ་རྣམ་དག་དང་རང༌[^664]བཞིན་རྣམ་དག་གོ། །

[Block 1378 [HEADING]]
#### རྫོགས་པའི་རིམ་པ། ^1-8-6-0

[Block 1379 [HEADING]]
##### ལྷན་ཅིག་སྐྱེས་པའི་དོན། ^1-8-6-1-0

[Block 1380]
དེ་ལྟར་བསྐྱེད་པའི་རིམ་པ་བསྟན་ནས། ད་ནི་རྫོགས་པའི་རིམ་པ་བཤད་པ་ནི། ནམ་མཁའི་ཁམས་ནི་ལ་སོགས་པ་སྔར་གྱི་སྡོམ་དུ་བསྟན་པའི་དོན་གོ་རིམས་བཞིན་དུ་བཤད་པའི་ཕྱིར། ལྷན་ཅིག་སྐྱེས་པའི་དོན་གཉིས་ཏེ། ཤེས་པར་བྱ་བ་དབྱེ་བའི་སྒོ་ནས་ཤེས་པ་དང་། བསྐྱེད་ཐབས་ཀྱི་རིམ་པའི་ཉམས་སུ་བླངས་པས་ཤེས་པའོ། །

[Block 1381 [HEADING]]
###### ཤེས་པར་བྱ་བ་དབྱེ་བའི་སྒོ་ནས་ཤེས་པ། ^1-8-6-1-1-0

[Block 1382]
དབྱེ་བ་ལ་མཚོན་བྱ་དང་མཚོན་བྱེད་ཀྱིས་དབྱེ་བ་དང་། ངོ་བོ་ཉིད་ཀྱི་སྒོ་ནས་དབྱེ་བ་དང་། རྟེན་གྱི་སྒོ་ནས་དབྱེ་བ་དང་། རྣམ་པར་གཞག་པའི་སྒོ་ནས་དབྱེ་བའོ། །

[Block 1383 [HEADING]]
###### **དང་པོ་མཚོན་བྱ་དང་མཚོན་བྱེད་ཀྱིས་དབྱེ་བ།** ^1-8-6-1-1-1-0

[Block 1384]
དང་པོ་ལ་དྲུག་སྟེ། མཚོན་བྱ༌[^665]དོན་དམ་བདེ་བ་འཁོར་ལོའི་ཚུལ་དུ་བདེ་བ་དང་མངོན་སུམ་དུ་སྟེ་གསང་བའི་དབང་པོར་སྐྱེས་པའོ། །

[Block 1385]
ཀུན་རྫོབ་དེར་ཁུ་བ་ཐིག་ལེ་ཚོགས་པ་གཅིག་པའི་ཚུལ་དུ་སྟེ། གཟུགས་དང་རོ་ལྟ་བུར་བུ་རམ་དཔེ་ལྟར་སྐྱེས་པའོ། །

[Block 1386]
མཚོན་བྱེད་དབྱེར་མེད་པ་ནི༌[^666]རང་རིག་པ་དེས་དོན་རང་གི་མཚན་ཉིད་ལ་འཇུག་སྟེ་དཔེར་ན་སྤྲིན་གྱིས་ཟླ་བ་ཁེབས་པ་དེའི་མཐོང་ནས་སྣང་བ་ལྟར་བརྒྱུད་ནས་ཕྱག་རྒྱ་ཆེན་པོ་ལས་ཤེས་པར་བྱེད་དོ། །

[Block 1387]
མཚོན་བྱའི་དབང་དུ་བྱས་པ་ཀུན་རྫོབ་ལྷ་སྟེ། ཁུ་བ་ལུས་ལས༌[^667]བྱུང་བ་གནས་པ་དང་དོན་དམ་དེའི་བདེ་བ་དམྱལ་བ་ཡན་ཆད་ལ་ཡོད་པའི་བྱང་ཆུབ་སེམས་དེ་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1388]
དབྱེར་མེད་སེམས་རང་རིག་པ་བདེ་བ་ལ་མི་རྟོག་པ་སྟེ་དེ་ལྟར་དྲུག་གོ། །

[Block 1389 [HEADING]]
###### **ངོ་བོ་ཉིད་ཀྱི་སྒོ་ནས་དབྱེ་བ།** ^1-8-6-1-1-2-0

[Block 1390]
དེ་ཉིད་མཚན་ཉིད་ཀྱིས་དབྱེ་ན་གཉིས་ཏེ།

[Block 1391 [VERSE]]
ཀུན་རྫོབ་དང་དོན་དམ་མོ། །
དེ་ལ་མཚོན་བྱེད་རིལ་ཀུན་རྫོབ།
མཚོན་བྱ་རིལ་དོན་དམ་མོ། །

[Block 1392 [HEADING]]
###### **རྟེན་གྱི་སྒོ་ནས་དབྱེ་བ།** ^1-8-6-1-1-3-0

[Block 1393]
རྟེན་གྱི་སྒོ་ནས་དབྱེ་བ་ལ་བཞི་སྟེ། ཤེས་རབ་བུད་མེད་ལ་གཉིས། ཐབས་སྐྱེས་བུ་ལ་ཡང་གཉིས་ཏེ་དོན་དམ་དང་ཀུན་རྫོབ་གཉིས་ཏེ་བཞིའོ། །

[Block 1394 [HEADING]]
###### **རྣམ་པར་གཞག་པའི་སྒོ་ནས་དབྱེ་བ།** ^1-8-6-1-1-4-0

[Block 1395]
རྣམ་པར་གཞག་པ༌[^668]ལ་བཞི་སྟེ་དགའ་བ་བཞི་ལ་ལྷན་སྐྱེས་སུ་བྱས་ཏེ། སྐད་ཅིག་བཞི་ནི་སྤངས་པའི༌[^669]ཚུལ་དང་། དགའ་བ་བཞི་ཐོབ་པའི་ཚུལ་ལོ། །

[Block 1396 [HEADING]]
###### བསྐྱེད་ཐབས་ཀྱི་རིམ་པའི་ཉམས་སུ་བླངས་པས་ཤེས་པ། ^1-8-6-1-2-0

[Block 1397]
བསྐྱེད་ཐབས་ནི་སློབ་དཔོན་གྱི་མན་ངག་གིས་དབང་གསུམ་པ་བསྟན་པས་རྟོགས་པ་གཅོད་པ་སྟེ། བདེ་བ་མངོན་སུམ་དུ་འབྱུང་། མི་རྟོག་པ་རྗེས་སུ་དཔག་པའི་ཚུལ་དུ་སྐྱེའོ། །

[Block 1398]
ནམ་མཁའི་ཁམས་ནི་པདྨ་ལ། །ཞེས་པ་ནི་ཤེས་རབ་ཀྱི་གསང་བའི་གནས་སོ། །

[Block 1399 [VERSE]]
བྷ་ག་ཞེས་པའང་ཡེ་ཤེས་བརྗོད། །
ཅེས་པ་ནི་ཐབས་ཀྱི་གསང་བའི་གནས་སོ། །

[Block 1400]
སྙོམས་འཇུག་ནི་ཨོཾ་པདྨ་སུ༌[^670]ཁ་ལ་སོགས་པས་བྱིན་གྱིས་བརླབས་པའི་ཆོས་དང་ལྡན་པའོ། །

[Block 1401]
བདེ་བ་ནི་མཚོན་བྱེད་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1402]
འཁོར་ལོ་ནི་གཅོད་ཅིང་སྦྱོང་བས་ཤེས་རབ་སྟོང་པ་ཉིད་ཟུར་ལ་སྐྱེའོ། །

[Block 1403]
སྔོན་འགྲོ་ཞེས་པ་ཞུ་བ་ནི༌[^671]མན་ངག་གི་ཤུགས་ཀྱིས་བསྟན་པ་སྟེ༌[^672]མཚོན་བྱེད་ཀུན་རྫོབ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1404]
རིགས་པ་ཇི་བཞིན་རང་རིག་ནི་མཚོན་བྱེད་དབྱེར་མེད་རང་རིག་གསལ་བའོ། །

[Block 1405]
ལྷ་བྱང་ཆུབ་སེམས་ནི་མཚོན་བྱ་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པའོ། །
--- END BLOCKS ---
