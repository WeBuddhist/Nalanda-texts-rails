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

[Block 1511]
འཕྲོ༌[^711]བའམ་སྡུད་པ་ནི་སྡུག་བསྔལ་ལོ། །

[Block 1512]
དབྱེ་བ་ནི་བདེ་བའོ། །

[Block 1513]
རང་རིག་ནི་གཉུག་མ་དེ་ཉིད་དོ། །

[Block 1514]
དེའི་ཕྱིར་རང་རིག༌[^712]གཉུག་མ་དེ་ཉིད་ནི་དེའི་གནས་སྐབས་ཀུན་དུ་འགྱུར་བས་རྒྱལ་པོ་དང་གཙོ་བོ་ལྟ་བུ་རྒྱུ་བར༌[^713]བྱེད་དོ། །

[Block 1515]
འོ་ན་རང་རིག་པ་གཉུག་མའི་ཆོས་དེ་དང་། དམན་པ་གློ་བུར་བ་གཉིས་ཐ་དད་དམ་ཐ་མི་དད་ཅེ་ན། ཐ་དད་ན་འགྲན༌[^714]ཐུབ་པས་ཇི་ལྟར་སྤང་དུ་བཏུབ། ཐ་མི་དད་ན་ནི་འོ་ན་རྣམ་པར་དག་པའི་ཆོས་སུ་འགྱུར་རམ། དྲི་མའི་ཆོས་སུ་འགྱུར། རྣམ་པར་དག་པའི་ཆོས་སུ་འགྱུར་ན་ནི་འབད་པ་མེད་པར་གྲོལ་བར་འགྱུར་ཏེ་ངོ་བོ་ཉིད་ཀྱིས་དག་པའི་ཕྱིར་རོ། །

[Block 1516]
མ་དག་པའི་རང་བཞིན་དུ་འགྱུར་ན་ནི་འབད་པ་འབྲས་བུ་མེད་པར་འགྱུར་ཏེ། ངོ་བོ་ཉིད་མ་དག་པའི་ཕྱིར་རོ། །

[Block 1517]
དཔེར་ན་སོལ་བ་བདར་ཀྱང་དཀར་པོ་མི་འོང་བ་བཞིན་ནོ། །

[Block 1518]
དེ་སྐད་དུ་ཡང་།

[Block 1519 [VERSE]]
གལ་ཏེ་རྣམ་དག་དེ་མ་གྱུར། །
འབད་པས་འབྲས་བུ་མེད་པར་འགྱུར། །

[Block 1520]
གལ་ཏེ་ཉོན་མོངས་དེ་མ་འགྱུར།[^715] །འབད་པ་མེད་པར་གྲོལ་བར་འགྱུར། །ཞེས་ཟེར་བ་ལ་དེ་ནི་དེ་ལྟར་མི་ལྟ་སྟེ། རང་བཞིན་རྣམ་པར་དག་པ་དང་དྲི་མ་གློ་བུར་གཉིས་གཅིག་པ་དང་ཐ་དད་པ་མ་ཡིན་ཏེ། དེ་ཉིད་དང་གཞན་དུ་བརྗོད་དུ་མེད་པ་ཡིན་པས་སྔ་མའི༌[^716]སྐྱོན་མི་འོང་ལ། རང་བཞིན་རྣམ་པར་དག་པ་ཡིན་པས་འབད་པ་དོན་མེད་པར་ཡང་མི་འགྱུར། དེ་སྐད་དུ་ཡང་།

[Block 1521 [VERSE]]
རང་བཞིན་ཉིད་ཀྱིས་རྣམ་པར་དག །
དྲི་མ་རྣམས་ནི་གློ་བུར་བ། །

[Block 1522]
གཞན་ཡང་།

[Block 1523 [VERSE]]
ཆུ་ཁམས་གསེར་དང་ནམ་མཁའ་བཞིན། །
དག་པ་ཉིད་པས་དག་པར༌[^717]འདོད། །

[Block 1524]
ཅེས་གསུངས་སོ། །

[Block 1525]
འོན་ཀྱང་དྲི་མ་གློ་བུར་བ་ཡིན་པས་སྣ་ཚོགས་པའི་རྟོག་པ་མི་འཇུག་ལ། གློ་བུར་ཙམ་སྤང་པའི་ཐབས་ནི་དགོས་ཏེ། འོག་ནས།

[Block 1526 [VERSE]]
བཞིན་ལག་ཁ་དོག་གནས་པ་ནི། །
བསྐྱེད་པ་ཙམ་གྱིས་རྣམ་པར་གནས། །
འོན་ཀྱང་བག་ཆགས་ཕལ་པས་སོ། །
རང་བཞིན་གྱིས་ནི་མྱ་ངན་འདས། །

[Block 1527]
ཞེས་གསུངས་སོ། །

[Block 1528 [HEADING]]
##### བདེ་བ་ཆེན་པོ། ^1-8-6-11-0

[Block 1529]
ད་ནི་གཉིས་མེད་རང་རིག་ཏུ་བསྟན་ནས་བདེ་བ་ཆེན་པོ་བསྟན་པའི་ཕྱིར་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པ་ལྔའི་བདེ་བ་ནི་མཚོན་བྱེད་ལྷན་ཅིག་སྐྱེས་པ་ལས་ཀྱི་ཕྱག་རྒྱལ་ཡོད་པའོ། །

[Block 1530]
དེ་ནས་ཉམས་དགའ་ཞེས་བྱ་བ་ནི༌[^718]མཚོན་བྱ་སྟེ་ཕྱག་རྒྱ་ཆེན་པོ་ལ་གནས་པའོ། །

[Block 1531]
བཅུ་དྲུག་ཆ་ནི་ཟླ་བ་བཅུ་དྲུག་པ་ཚེས་གཅིག་དང་། གཉིས་ལ་སོགས་པས་མི་བསྐྲུན་པའམ། ཡང་ན་ཉོན་མོངས་པ་དང་བཅས་པའི་དགའ་བ་བཅུ་དྲུག་བསྡུས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོའི་ལྷན་སྐྱེས་ཏེ་རེ་རེའི་ཆས་མི་ཕོད་དོ། །

[Block 1532]
ད་ནི་རང་རིག་མི་རྟོག་པ་དང་བཅས་པ་ཅི་ཞེ་ན། དེ་ཡང་ཡིད་ཀྱི་རྒྱུ་བ་ཉོན་མོངས་པ་དང་བྲལ་བ་སྟེ། དེ་ཉིད་ཀྱི་ཤུགས་ཀྱིས་བསྟན་ཏོ། །

[Block 1533 [HEADING]]
##### དབྱེར་མེད་བཤད་པ། ^1-8-6-12-0

[Block 1534]
ད་ནི་དབྱེར་མེད་དེ་བཤད་པའི་ཕྱིར་ཆོས་འབྱུང་ནི་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །

[Block 1535]
ཡེ་ཤེས་སྐྱེས་པ་ནི་དེར་ཡེ་ཤེས་རང༌[^719]འབར་བའོ། །ཇི་ལྟ་བུ་ཞེ་ན། མཁའ་མཉམ་སྟེ་མི་རྟོག་པའོ། །

[Block 1536]
ཐབས་ནི་བདེ་བའོ། །

[Block 1537 [VERSE]]
ལྷན་ཅིག་སྐྱེས་པ་ནི་རོ་གཅིག་པའོ། །
ཐབས་དང་ཤེས་རབ་རང་བཞིན་ནོ། །
རོ་གཅིག་པ་དེ་ལས་སོ། །

[Block 1538]
འཇིག་རྟེན་གསུམ་པོ་ནི་དག་དང་མ་དག་པའི་ཆས༌[^720]ཁམས་གསུམ་མམ་སྐུ་གསུམ་མོ། །

[Block 1539]
དེ་ལས་སྐྱེས་ནི་ལྷན་ཅིག་སྐྱེས༌[^721]པ་ལས་སོ། །

[Block 1540]
དེ་ཡང་ཇི་ལྟར་ཉམས་སུ་བླངས་ཤེ་ན༌[^722]ཞུ་བའི་རྣམ་པ་ནི་ཀུན་རྫོབ་ཀུནྡ་ལྟ་བུའོ། །

[Block 1541]
བཅོམ་ལྡན་ནི་ཧེ་རུ་ཀ་སྟེ་ལོངས་སྐུའོ། །

[Block 1542]
བདེ་བ་ནི་དོན་དམ་མོ། །

[Block 1543]
གདོད་མ་ནི་བདག་མེད་མ་སྟེ་ཆོས་སྐུའོ། །

[Block 1544 [HEADING]]
##### མཇུག་བསྡུ་བ། ^1-8-6-13-0

[Block 1545]
དེ་དག་མཇུག་བསྡུ་བའི་ཕྱིར་གཅིག་དང་དུ་མ་བྲལ་བ་ནི་ཡིད་ཀྱི་རྒྱུ་བ་ཉོན་མོངས་པའི་བདེ་བ་བྲལ་བ་སྟེ་མི་རྟོག་པའོ། །
--- END BLOCKS ---
