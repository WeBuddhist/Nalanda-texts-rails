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
[Block 421 [VERSE]]
ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་དག །
གང་རྣམས་ཐུབ་པས་གསུངས་དེ་དག །
ཚིག་གམ་མིང་ཡིན་དེ་དག་ནི། །
གཟུགས་དང་འདུ་བྱེད་དག་ཏུ་འདུས། །

[Block 422]
གང་དག་གི་ལྟར་ན་སངས་རྒྱས་ཀྱི་གསུང་ཚིག་གི་རང་བཞིན་ཡིན་པ་དེ་དག་གི་ལྟར་ན་དེ་དག་ནི་གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 423]
གང་དག་གི་ལྟར་ན་མིང་གི་རང་བཞིན་ཡིན་པ་དེ་དག་གི་ལྟར་ན་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 424]
ཡང་ཆོས་ཀྱི་ཕུང་པོའི་ཚད་ཇི་ཙམ་ཞེ་ན། ཁ་ཅིག་བསྟན་བཅོས་ཚད་ཅེས་ཟེར། །ཁ་ཅིག་ན་རེ་དེ་ནི་ཆོས་ཀྱི་ཕུང་པོ་ཞེས་བྱ་བ་བསྟན་བཅོས་མངོན་པའི་ཚད་ཙམ་མོ་ཞེས་ཟེར་ཏེ། དེ་ནི་ཤློ་ཀ་དྲུག་སྟོང་ངོ་། །ཡང་གཞན་དག་ན་རེ། ཕུང་པོ་ལ་སོགས་གཏམ་རེ་ཡིན། །ཞེས་ཟེར་ཏེ། ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་དང་། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་དང་། བདེན་པ་དང་། ཟས་དང་། བསམ་གཏན་དང་། ཚད་མེད་པ་དང་། གཟུགས་མེད་པ་དང་། རྣམ་པར་ཐར་པ་དང་། ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་དང་། ཟད་པར་གྱི་སྐྱེ་མཆེད་དང་། བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་དང་། མངོན་པར་ཤེས་པ་དང་། སོ་སོ་ཡང་དག་པར་རིག་པ་དང་། སྨོན་ནས་ཤེས་པ་དང་། ཉོན་མོངས་པ་མེད་པ་ལ་སོགས་པའི་གཏམ་རྒྱུད་རེ་རེ་ནི་ཆོས་ཀྱི་ཕུང་པོའོ༌[^168]ཞེས་ཟེར་རོ། །

[Block 425 [VERSE]]
སྤྱོད་པ་རྣམས་ཀྱི་གཉེན་པོར་ནི། །
ཆོས་ཀྱི་ཕུང་པོ་མཐུན་པར་གསུངས། །

[Block 426]
འདི་སྐད་དུ། སེམས་ཅན་རྣམས་ཀྱི་སྤྱོད་པ་འདོད་ཆགས་དང་། ཞེ་སྡང་དང་། གཏི་མུག་དང་ང་རྒྱལ་ལ་སོགས་པ་སྤྱོད་པ་ཐ་དད་པ་བརྒྱད་ཁྲི་ཡོད་དེ། དེ་དག་གི་གཉེན་པོར་བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་གསུངས་སོ་ཞེས་བརྗོད་དོ། །

[Block 427 [HEADING]]
##### མདོ་གཞན་དག་ལས་གསུངས་པ། ^1-2-8-2-0

[Block 428]
ཇི་ལྟར་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི༌[^169]འདི་ཕུང་པོ་ལྔ་པོ༌[^170]འདི་དག་ཉིད་དུ་བསྡུས་པ།

[Block 429 [VERSE]]
དེ་བཞིན་གཞན་ཡང་ཅི་རིགས་པར། །
ཕུང་པོ་སྐྱེ་མཆེད་ཁམས་རྣམས་ནི། །
རང་གི་མཚན་ཉིད་ལེགས་དཔྱད་དེ། །
ཇི་སྐད་བཤད་པར་བསྡུ་བར་བྱ། །

[Block 430]
མདོ་གཞན་དག་ལས་ཕུང་པོ་དང་སྐྱེ་མཆེད་དང་ཁམས་གཞན་གང་དག་གསུངས་པ་དེ་དག་ཀྱང་བསྟན་བཅོས་འདི་ལས།

[Block 431]
ཇི་སྐད་བཤད་པ་བཞིན་དེ་དག་གི་རང་རང་གི་མཚན་ཉིད་ལེགས་པར་དཔྱད་ནས་ཕུང་པོ་ལ་སོགས་པ་ཇི་སྐད་བཤད་པ་འདི་དག་ཉིད་དུ་བསྡུ་བར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག་ཚུལ་ཁྲིམས་དང་། ཏིང་ངེ་འཛིན་དང་། ཤེས་རབ་དང་། རྣམ་པར་གྲོལ་བ་དང་། རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་མཐོང་བའི་ཕུང་པོ་དག་ལས་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་ནི་གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 432]
ལྷག་མ་རྣམས་ནི་འདུ་བྱེད་ཀྱི༌[^171]ཕུང་པོས་བསྡུས་སོ། །

[Block 433]
ཟད་པར་གྱི་སྐྱེ་མཆེད་བཅུ་པོ་དག་ལས་བརྒྱད་ནི་མ་ཆགས་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཆོས་ཀྱི་སྐྱེ་མཆེད་ཀྱིས༌[^172]བསྡུས་སོ། །

[Block 434]
འཁོར་རྣམས་དང་བཅས་ན་ནི་ཕུང་པོ་ལྔའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཡིད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་དག་གིས་བསྡུས་ཏེ། ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་རྣམས་ཀྱང༌[^173]དེ་དང་འདྲའོ། །

[Block 435]
ཟད་པར་ནམ་མཁའ་དང་རྣམ་ཤེས༌[^174]མཐའ་ཡས་སྐྱེ་མཆེད་དག་དང་། ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ་སོགས་པ་བཞི་པོ་དག་ནི་ཕུང་པོ་བཞིའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཡིད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་དག་གིས་བསྡུས་སོ། །

[Block 436]
རྣམ་པར་གྲོལ་བའི་སྐྱེ་མཆེད་ལྔ་པོ་དག་ནི་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཆོས་ཀྱི་སྐྱེ་མཆེད་ཀྱིས་བསྡུས་སོ། །

[Block 437]
འཁོར་རྣམས་དང་བཅས་ན་ནི་སྒྲ་དང་ཡིད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་རྣམས་ཀྱིས་བསྡུས་སོ། །

[Block 438]
སྐྱེ་མཆེད་གཉིས་ལས་འདུ་ཤེས་མེད་པའི་སེམས་ཅན་ནི་དྲི་དང་རོའི་སྐྱེ་མཆེད་བཅུ་བཞི༌[^175]པོ་རྣམས་ཀྱིས་བསྡུས་སོ། །

[Block 439]
འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་གྱི༌[^176]སྐྱེ་མཆེད་དུ་ཉེ་བར་འགྲོ་བ་ནི་ཡིད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་དག་གིས་བསྡུས་སོ། །

[Block 440]
དེ་བཞིན་དུ་ཁམས་མང་པོ་ལ་ལས་ཁམས་དྲུག་ཅུ་རྩ་གཉིས་བསྟན་པ་དེ་དག་ཀྱང་ཅི་རིགས་པར་བསྡུ་བར་རིག་པར་བྱའོ། །

[Block 441]
དེར་གང་དག་སའི་ཁམས་དང་། ཆུའི་ཁམས་དང་། མེའི་ཁམས་དང་། རླུང་གི་ཁམས་དང་། ནམ་མཁའི་ཁམས་དང་། རྣམ་པར་ཤེས་པའི་ཁམས་དྲུག་བསྟན་པ་ལ། དེ་དག་ལས་གཉིས་ཀྱི་མཚན་ཉིད་མ་བཤད་ན། དེ་ཅི་ནམ་མཁའ་ཉིད་ནམ་མཁའི་ཁམས་ཡིན་ལ། རྣམ་པར་ཤེས་པ་ཐམས་ཅད་ཀྱང་རྣམ་པར་ཤེས་པའི་ཁམས་ཡིན་པར་རིག་པར་བྱ་འམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 442]
འོ་ན་ཅི་ཞེ་ན། སྒོ་དང་སྐར་ཁུང་དང་ཁ་དང་སྣ་ལ་སོགས་པའི་བུ་ག་ནམ་མཁའི་ཁམས་ཞེས་བྱ། བུ་ག་ཞེས་བྱ་བ་ཅི་ཞིག་ཡིན་པར་རིག་པར་བྱ། སྣང་དང་མུན་པ་དག་ཡིན་ལོ། །

[Block 443]
བུ་ག་ནི་སྣང་བ་དང་མུན་པ་དག་ལས་གཞན་དུ་གཟུང་དུ་མེད་དོ། །

[Block 444]
དེ་ལྟ་བས་ན་ནམ་མཁའི་ཁམས་ནི་སྣང་བ་དང་མུན་པའི་རང་བཞིན་ཏེ། མཚན་མོ་དང་ཉིན་མོའི་རང་བཞིན་དུ་ཡིན་པར༌[^177]རིག་པར་བྱའོ་ཞེས་གྲག་གོ། །

[Block 445]
དེ་ཉིད་ཐོགས་པའི་ཉེ་བའི་འཁོར་གྱི་གཟུགས་ཞེས་བྱ་སྟེ། ཐོགས་པ་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་གནོད་པར་བྱར༌[^178]རུང་བའི་ཕྱིར་བསགས་པར་གནས་པའི་གཟུགས་ཏེ། དེ་ནི་དེའི་འཁོར་རོ་ལོ། །

[Block 446]
གཞན་དག་ན་རེ་དེ་ལ་གཞན་མི་ཐོགས་པའི་ཕྱིར་ཏེ། དེ་ནི་ཐོགས་མེད་ཀྱང་ཡིན་ལ་གཟུགས་གཞན་གྱི་ཉེ་འཁོར་ཡང་ཡིན་པས་ཐོགས་མེད་ཉེ་འཁོར་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 447]
ཟག་པ༌[^179]དང་བཅས་པའི༌[^180]རྣམ་ཤེས་ནི། རྣམ་ཤེས་ཁམས་ཡིན། ཅིའི་ཕྱིར་ཟག་པ་མེད་པ་ལ་མི་བྱ་ཞེ་ན། འདི་ལྟར་ཁམས་དྲུག་པོ་འདི་དག་ནི། སྐྱེ་བའི་རྟེན་ཡིན་པར་འདོད་དེ། དེ་དག་ཉིང་མཚམས་སྦྱོར་བའི་སེམས་ནས༌[^181]འཆི་བའི་སེམས་ཀྱི་བར་དུ་སྐྱེ་བའི་གཞིར་གྱུར་པ་སྟེ། ཟག་པ་མེད་པའི་ཆོས་རྣམས་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 448]
དེའི་ཕྱིར་དེ་ལྟར་ན་དེ་དག་ལས་ཁམས་བཞི་ནི་རེག་བྱའི་ཁམས་ཀྱི་ནང་དུ་འདུས་སོ། །

[Block 449]
ལྔ་པ་ནི་གཟུགས་ཀྱི་ཁམས་ཀྱི་ནང་དུ་འདུས་སོ། །

[Block 450]
དྲུག་པ་ནི་རྣམ་པར་ཤེས་པའི་ཁམས་བདུན་པོ་དག་ཏུ་འདུས་སོ། །

[Block 451 [HEADING]]
### ཁམས་རབ་ཏུ་དབྱེ་བ། ^1-3-0

[Block 452 [HEADING]]
#### བསྟན་དུ་ཡོད་པ་དང་བསྟན་དུ་མེད་པ། ^1-3-1-0

[Block 453]
གང་དག་ཁམས་བཅོ་བརྒྱད་བསྟན༌[^182]པ་དེ་དག་ལས་བསྟན་དུ་ཡོད་པ་རྣམས་ནི་དུ། བསྟན་དུ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། བསྟན་ཡོད་འདིར་ནི་གཟུགས་གཅིག་ཏུ།[^183] །དེ་ནི་འདི་ནི་འདི་ནའོ། །

[Block 454]
ཆེ་གེ་མོ་ཞིག་ནའོ༌[^184]ཞེས་བསྟན་པར་ནུས་སོ། །

[Block 455]
ལྷག་མ་རྣམས་ནི་བསྟན་དུ་མེད་པའོ་ཞེས་བཤད་པར་འགྱུར་རོ། །

[Block 456 [HEADING]]
#### ཐོགས་པ་དང་བཅས་པ་དང་ཐོགས་པ་མེད་པ། ^1-3-2-0

[Block 457]
ཐོགས་པ་དང་བཅས་པ་རྣམས་ནི་དུ། ཐོགས་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། ཐོགས་དང་བཅས་པ་གཟུགས་ཅན་བཅུ། །གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་པའི་ཁམས་བཅུ་གང་དག་བཤད་པ་དེ་དག་ནི་ཐོགས་པ་དང་བཅས་པ༌[^185]ཡིན་ཏེ། ཐོགས་པ་ཞེས་བྱ་བ་ནི་རྡུགས་པའོ། །

[Block 458]
དེ་ཡང་རྣམ་པ་གསུམ་སྟེ། སྒྲིབ་པ་དང་ཡུལ་དང་དམིགས་པ་ལ་ཐོགས་པའོ། །

[Block 459 [HEADING]]
##### སྒྲིབ་པ་ལ་ཐོགས་པ། ^1-3-2-1-0

[Block 460]
དེ་ལ་སྒྲིབ་པ་ལ་ཐོགས་པ་ནི་རང་གི་ཡུལ་དུ་གཞན་སྐྱེ་བའི་གེགས་བྱེད་པ་སྟེ། དཔེར་ན་ལག་པ་འམ། རྡོ་བ་ལ་ལག་པ་རྡུགས་ཤིག༌[^186]ཐོགས་པའམ། རྡོ་བ་ཡང་དེ་གཉིས་ལ་ཐོགས་པ་ལྟ་བུའོ། །
--- END BLOCKS ---
