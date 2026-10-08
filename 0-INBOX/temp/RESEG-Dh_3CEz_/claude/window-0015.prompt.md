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
[Block 526 [HEADING]]
###### **ཁྱད་པར།** ^1-1-5-2-1-2-3-1-2-2-3-2-0

[Block 527]
ཁྱད་པར་ནི་མཆོག་དང༌[^175]མཆོག་མ་ཡིན་པ་སྟེ། དེ་ཡང་མཆོག་ནི་སྐད་ཅིག་དང་དགའ་བ་བཞིའི་བདེ་བ་མཆོག་ཏུ་སྡོམ་པའོ། །

[Block 528]
མཆོག་མ་ཡིན་པ་ནི་དེ་ཁོ་ན་ཉིད་བཞི་བདེ་བ་མཆོག་ཏུ་སྡོམ་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 529 [HEADING]]
###### **བརྟག་པ་ཕྱི་མའི་ཚུལ་དུ་རྒྱུ་མཚན་བསྟན་པ།** ^1-1-5-2-1-2-3-2-0

[Block 530]
བརྟག་པ་ཕྱི་མའི་ཚུལ་དུ་རྒྱུ༌[^176]མཚན་བསྟན་པ་ལ་གཉིས་ཏེ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་དང་། སངས་རྒྱས་སོ། །

[Block 531 [HEADING]]
###### **ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས།** ^1-1-5-2-1-2-3-2-1-0

[Block 532]
དེ་ལ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ནི་འཁོར་ལོ་བཞི་སྐུ་བཞིར་གྲུབ་པ་དེ།[^177] འབྲས་བུ་བཞི་དང་སྡེ་པ་བཞི་དང་། རྣམ་པར་གཞག་པའི་རྒྱུ་མཚན་གྱིས་སྡེ་པ་མཆོག་ཏུ་སྡོམ་པ་དང་།

[Block 533 [HEADING]]
###### **སངས་རྒྱས།** ^1-1-5-2-1-2-3-2-2-0

[Block 534]
སངས་རྒྱས་ནི་ས་བཅུའི་བྱང་ཆུབ་སེམས་དཔའ་སྟེ། མིར་སྐྱེ་བ་དག་པའི་ཚུལ་གདོད་མ་ནས་སངས་རྒྱས་ཡིན་པས་བདེ་བ་མཆོག་ཏུ་སྡོམ་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 535 [HEADING]]
###### **མངོན་པར་རྟོགས་པ།** ^1-1-5-2-1-2-3-1-3-0

[Block 536]
མངོན་པར་རྟོགས་པ་ལ་གཉིས་ཏེ། །

[Block 537 [HEADING]]
###### **ཉམས་སུ་ལེན་པ་རླུང་ལ་བསླབ་པ་དང་གཏུམ་མོ་སྦར་བ།** ^1-1-5-2-1-2-4-0

[Block 538]
རྣམ་པར་རྟོག་པའི་གཉེན་པོ་སྟེང་སྒོ་རླུང་ལ་བསླབ་པ་དང་། ཉོན་མོངས་པའི་གཉེན་པོར་བྱང་ཆུབ་སེམས་ལ་བསླབ་པའོ། །

[Block 539 [HEADING]]
###### **རླུང་ལ་བསླབ་པ།** ^1-1-5-2-1-2-4-1-0

[Block 540]
རླུང་ལ་གཉིས་ཏེ། ཤེས་པར་བྱ་བ་དང་། བསྒོམ༌[^178]པའོ། །

[Block 541 [HEADING]]
###### **ཤེས་པར་བྱ་བ།** ^1-1-5-2-1-2-4-1-1-0

[Block 542]
[^179]དེ་ལ་ཤེས་པ་ནི་ཕྱི་དག་པར་ཤེས་པ་དང་ནང་དག་པར་ཤེས་པའོ། །

[Block 543 [HEADING]]
###### **ཕྱི་དག་པར་ཤེས་པ།** ^1-1-5-2-1-2-4-1-1-1-0

[Block 544]
དེ་ལ་ཕྱི་ནི་རྒྱལ་པོའི་ཕོ་བྲང་དང་དགེ་འདུན་གྱི་གནས་དག་ན་དབྱུ་གུ་དང་ཆུ་ཚོད་ལ་སོགས་ཏེ་རླུང་དུ་སྦྱར་བའོ། །

[Block 545 [HEADING]]
###### **ནང་དག་པར་ཤེས་པ།** ^1-1-5-2-1-2-4-1-1-2-0

[Block 546]
ནང་གི་ལྟེ་བ་སྤྲུལ་པའི་འཁོར་ལོ་ལ་སོགས་པ་འདབ་མའི་གྲངས་སྦྱར་བའོ། །

[Block 547 [HEADING]]
###### **བསྒོམ་པ།** ^1-1-5-2-1-2-4-1-2-0

[Block 548]
དེ་དག་རྣམ་པར་དག་པའི་རང་བཞིན་དུ་ཤེས་ནས་རླུང་ལ་བསྒོམ་པ་སྟེ། ཟླ་བ་ཉི་མ་ཨཱ་ལི་ཀཱ་ལི་ཉིན་མཚན་གཉིས་ལ་ཐུན་བཞི་བཞི་བརྒྱད་དུ་འབྱུང་ངོ་། །རེ་མོས་འབྱུང་བའི་འཕོ་བ་ནི་ཐུན་ཕྱེད་ཕྱེད་ནས་ཏེ་བཅུ་དྲུག་གོ། །

[Block 549]
དེ་རེ་རེ་ལ་ཡང་ཐབས་དང་ཤེས་རབ་ཀྱི་ཆས༌[^180]ཆུ་ཚོད་སུམ་ཅུ་རྩ་གཉིས་སོ། །

[Block 550]
ཡང་ཟླ་ཉི་གང་ཡང་རུང་བ་གཅིག་ལས་བྱུང་བ༌[^181]བཞི་རིམ་གྱིས་འབྱུང་བས་དབྱུ་གུ་དྲུག་ཅུ་རྩ་བཞིའོ། །

[Block 551]
དེ་ལྟར་རླུང་ལས་སུ་རུང་ནས་གྲངས་ཀྱི་རྩིས་ནི་གཞན་དུ་ཤེས་པར་བྱའོ། །

[Block 552]
བསླབ་པ་ནི་གྲངས་ལ་བཅུ་དང་བརྒྱའི་བར་དུ་བསླབ་པ་དང་།

[Block 553]
རླུང་ལྷན་ཅིག་སྐྱེས་པར་སྦྱོར་བའོ། །

[Block 554 [HEADING]]
###### **བྱང་ཆུབ་སེམས་ལ་བསླབ་པ།** ^1-1-5-2-1-2-4-2-0

[Block 555 [VERSE]]
བྱང་ཆུབ་སེམས་ལ་བསླབ་པ་ལ༌[^182]གཉིས་ཏེ།
སྒྲའི་དབྱེ་བ་དང་བཤད་ཚུལ་སྦྱོར་བའོ། །

[Block 556 [HEADING]]
###### **སྒྲའི་དབྱེ་བ།** ^1-1-5-2-1-2-4-2-1-0

[Block 557]
དེ་ལ་སྒྲའི་དབྱེ་བ་གང་དུ་འཛག་ནི༌[^183]ལྟེ་བ་སྟེ་གཉིས་པའི་དོན་ཏོ། །

[Block 558 [VERSE]]
གང་འཛག་ན་རི་བོང་ཅན་ཏེ་དང་པོའི་དོན་ཏོ། །
གང་ལས་འཛག་ན་ཧཾ་ལས་ཏེ་ལྔ་པའི་དོན་ཏོ། །

[Block 559]
གང་གིས་འཛག་ན་གཏུམ་མོ་སྦར་བ་སྟེ། གསུམ་པའི་དོན་ཏོ། །

[Block 560]
གང་གི་ཕྱིར་འཛག་ན་དེ་བཞིན་གཤེགས་པ་ལ་སོགས་པ་བསྲེགས་པའི༌[^184]དོན་ཏེ་བཞི་པའི་དོན་ཏོ། །

[Block 561 [HEADING]]
###### **བཤད་ཚུལ་སྦྱོར་བ།** ^1-1-5-2-1-2-4-2-2-0

[Block 562]
བཤད་པའི་ཚུལ་སྦྱར་བ་ལ་ཡང་གཉིས་ཏེ། བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའོ། །

[Block 563 [HEADING]]
###### **བསྐྱེད་པའི་རིམ་པ།** ^1-1-5-2-1-2-4-2-2-1-0

[Block 564]
དེ་ལ་བསྐྱེད་པ་ལ་ཡང་ལྟེ་བར་ནི་སྣ་ཚོགས་པདྨའོ། །

[Block 565 [VERSE]]
གཏུམ་མོ་ནི་རང་གི་རིག་མའོ། །
ཨཱ་ལི་ཟླ་བ་ཅན་རྡོ་རྗེ་སེམས་དཔའོ། །
འབར་བ་ནི་དེ་གཉིས་རྗེས་སུ་ཆགས་པའོ། །
དེ་བཞིན་གཤེགས་པ་ནི་ཕུང་པོ་ལྔ་སྟེ།
--- END BLOCKS ---
