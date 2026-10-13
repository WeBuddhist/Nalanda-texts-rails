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
[Block 351]
ཡང་བསྐྱེད་རིམ་དང་རྫོགས་རིམ་དང་། ཡོངས་སུ༌[^138]རྫོགས་པའི་རིམ་པའོ། །

[Block 352]
ཡོངས་གྲུབ་ཀྱི་ཀུན་བརྟགས་ནི་མཚོན་བྱ་ཀུན་རྫོབ། གཞན་དབང་གི་མཚོན་བྱ་དོན་དམ། ཡོངས་གྲུབ་ནི་དབྱེར་མེད་དོ། །

[Block 353]
ཡང་ན་སྟོང་པ་ཉིད་ཀུན་བརྟགས། རིག་པ་གསལ་བ་གཞན་དབང་། དེ་གཉིས་དབྱེར་མེད་ཡོངས་གྲུབ་བོ། །

[Block 354]
དེ་རྣམས་ཉམས་སུ་བླང་བ་ནི། དེ་ཉིད་ངེས་པར་བྱ་སྟེ། ཆོས་ལ་ལམ་དུ་བྱེད་པ་བསྐྱེད་རིམ་ལྷའི་རྣལ་འབྱོར་སྒྲུབ་ཐབས་བཞིན་དུ༌[^139]ལེའུ་གསུམ་པ་དང་། བརྟག༌[^140]པ་ཕྱི་མའི་ལེའུ་ལྔ་པ་ལྟར་བྱ་བ་དང་ལུས་ལ་ལམ་དུ་བྱེད་པ་དང་། གཞན་ལུས་དང་རང་ལུས་ཏེ། །རྩ་དང་བྱང་ཆུབ་སེམས་གཟུང་བ་ལ་སོགས་པ་དགའ་བ་བཞི་བསྒོམ་པ་སྟེ་ལེའུ་དང་པོ་དང་བརྒྱད་པ་དང་བརྟག་པ་ཕྱི་མའི་ལེའུ་གཉིས་པ་དང་ལྔ་པ་ལས་འབྱུང་བ་བསྒོམ་མོ། །

[Block 355]
སེམས་ལ་ལམ་དུ་བྱེད་པ་སེམས་ལ་བསླབ་པ་སྟེ། ཐབས་དུ་མས་བསླབ་པའོ། །

[Block 356]
ལམ་གཉིས་ཏེ་བསྐྱེད་རིམ་མང་བར་བྱ་སྟེ་རྫོགས་རིམ་ཉུང་ལྡན་སྒྲུབ་ཐབས་བཞིན་སྒོམ་པ་དང་རྫོགས་པའི་རིམ་པ་མང་ལྡན་བསྐྱེད་རིམ་ཉུང་ལྡན་ཏེ་མོས་པའི་རྣལ་འབྱོར་ལ་སོགས་པའམ་ཡན་ལག་བཞི་བསྒོམ་པའོ། །

[Block 357 [HEADING]]
###### **རྫོགས་པའི་རིམ་པ།** ^1-1-5-2-1-2-0

[Block 358]
རྫོགས་པའི་རིམ་པ་ལ་བཞི་སྟེ། ངོ་བོ་ཡེ་ཤེས་ཆེན་པོ་བསྟན་པ་དང་རྟེན་རྡོ་རྗེའི་ལུས་ལམ་དུ་བྱེད་པ་དང་། ལྡན་པའི་ཆོས་སྡོམ་པའི་དབྱེ་བ་དང་། ཉམས་སུ་ལེན་པ་རླུང་ལ་བསླབ་པ་དང་གཏུམ་མོ་སྦར་བའོ། །

[Block 359 [HEADING]]
###### **ངོ་བོ་ཡེ་ཤེས་ཆེན་པོ་བསྟན་པ།** ^1-1-5-2-1-2-1-0

[Block 360]
ཡེ་ཤེས་ཆེན་པོའི་རང་བཞིན་ལ་ཤེས་པར་བྱ་བ་དང་། སྒོམ་པ་ཉམས་སུ་ལེན་པའོ། །

[Block 361 [HEADING]]
###### **བསླབ་པ་ཤེས་པར་བྱ་བ།** ^1-1-5-2-1-2-1-1-0

[Block 362]
བསླབ་པ་ཤེས་པར་བྱ་བ་ལ་གཉིས་ཏེ། དེ་ཁོ་ན་ཉིད་བཤད་པ་དང་།

[Block 363 [HEADING]]
###### **དེ་ཁོ་ན་ཉིད་བཤད་པ།** ^1-1-5-2-1-2-1-1-1-0

[Block 364 [HEADING]]
###### **ཡེ་ཤེས།** ^1-1-5-2-1-2-1-1-1-1-0

[Block 365 [VERSE]]
རྣམ་པར་གཞག་པའི་ཆ་དབྱེ་བའོ། །
དེ་ཁོ་ན་ཉིད་ལ་གཉིས་ཏེ།
ཡེ་ཤེས་དང་ཆོས་ཉིད་དོ། །
ཡེ་ཤེས་ལ་ཡང་གཉིས་ཏེ།

[Block 366 [HEADING]]
###### **རྟེན་བསྟན་པ།** ^1-1-5-2-1-2-1-1-1-1-1-0

[Block 367 [VERSE]]
ལུས་ལ་ཡེ་ཤེས་ཆེན་པོ་གནས། །
ཞེས་པ་རྟེན་བསྟན་པ་དང་།

[Block 368 [HEADING]]
###### **ཚུལ་ལམ་མཚན་ཉིད་རང་འབྱུང་ཡེ་ཤེས་སུ་བསྟན་པ།** ^1-1-5-2-1-2-1-1-1-1-2-0

[Block 369]
ལུས་གནས་ལུས་ལས་མ་སྐྱེས་པ། །

[Block 370]
ཞེས་པ་ཚུལ་ལམ་མཚན་ཉིད་རང་འབྱུང་ཡེ་ཤེས་སུ་བསྟན་པའོ། །

[Block 371 [HEADING]]
###### **ཆོས་ཉིད།** ^1-1-5-2-1-2-1-1-1-2-0

[Block 372 [HEADING]]
###### **རྟེན་བསྟན་པ།** ^1-1-5-2-1-2-1-1-1-2-1-0

[Block 373]
ཆོས་ཉིད་ལ་གཉིས་ཏེ། དངོས་པོ་ཀུན་ལ་ཁྱབ་ཅེས་པས་རྟེན་བསྟན་པ་དང་།

[Block 374 [HEADING]]
###### **ཚུལ་ལམ་མཚན་ཉིད་འདུས་མ་བྱས་ཏེ་དེ་བཞིན་ཉིད་བསྟན་པ།** ^1-1-5-2-1-2-1-1-1-2-2-0

[Block 375]
རྟོག་པ་ཐམས་ཅད་ཡང་དག་སྤངས། །ཞེས་པ་ཚུལ་ལམ་མཚན་ཉིད་འདུས་མ་བྱས་ཏེ་དེ་བཞིན་ཉིད་བསྟན་པའོ། །

[Block 376 [HEADING]]
###### **རྣམ་པར་གཞག་པའི་ཆ་དབྱེ་བ།** ^1-1-5-2-1-2-1-1-2-0

[Block 377 [HEADING]]
###### **རྟེན་བསྟན་པ།** ^1-1-5-2-1-2-1-1-2-1-0

[Block 378]
རྣམ་པར་གཞག་པའི་ཆ་དབྱེ་བ་ལ་བཞི་སྟེ། ཚིག་དང་པོས་རྟེན་བསྟན་པ་དང་།

[Block 379 [HEADING]]
###### **མཚན་ཉིད།** ^1-1-5-2-1-2-1-1-2-2-0

[Block 380]
རྟོག་པ་གཉིས༌[^141]པས་མཚན་ཉིད་དང་།

[Block 381 [HEADING]]
###### **ཡོན་ཏན།** ^1-1-5-2-1-2-1-1-2-3-0

[Block 382]
གསུམ་པས་ཡོན་ཏན་དང་།

[Block 383 [HEADING]]
###### **དེ་ཁོ་ན་ཉིད་ཀྱི་རང་བཞིན་སྐྱེ་མེད་དུ་བསྟན་པ།** ^1-1-5-2-1-2-1-1-2-4-0

[Block 384]
བཞི་པས་དེ་ཁོ་ན་ཉིད་ཀྱི་རང་བཞིན་སྐྱེ་མེད་དུ་བསྟན་པའོ། །

[Block 385 [HEADING]]
###### **བསྒོམ་པ་ཉམས་སུ་ལེན་པ།** ^1-1-5-2-1-2-1-2-0

[Block 386]
བསྒོམ་པ་ཉམས་སུ་ལེན་པ་ལ་གཉིས་ཏེ། མངོན་རྟོགས་ལམ་དུ་བྱས་པ་དང་། འབྲས་བུ་ལམ་དུ་བྱས་པའོ། །

[Block 387 [HEADING]]
###### **མངོན་རྟོགས་ལམ་དུ་བྱས་པ།** ^1-1-5-2-1-2-1-2-1-0

[Block 388 [VERSE]]
མངོན་རྟོགས་ལམ་དུ་བྱས་པ་ལ་གསུམ་སྟེ།
ཆགས་ཅན་དང་ཆགས་བྲལ་དང་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 389 [HEADING]]
###### **ཆགས་ཅན།** ^1-1-5-2-1-2-1-2-1-1-0

[Block 390]
དེ་ལ་ཆགས་ཅན་ནི་གཞན་ལུས་ཤེས་རབ་ལས་ཀྱི་ཕྱག་རྒྱ་ལ་བརྟེན་པ་སྟེ། དེ་ཡང་ལུས་ལ་ཞེས་པ་ནི་མཚོན་བྱེད་དབྱེར་མེད་དུ་རང་གི༌[^142]ཉམས་སུ་མྱོང་བ་སྟེ། དེ་རྟོག་པར་རང་ཤུགས་སུ་གཅོད་ཅིང་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །
--- END BLOCKS ---
