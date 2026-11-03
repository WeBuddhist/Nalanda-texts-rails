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
[Block 526]
ཕས་ཀྱི་རྒོལ་བ་ནི་མུ་སྟེགས་ཅན་རྣམས་སོ། །

[Block 527]
ངན་པའི་ཚོགས་ཅན་གྱི་ཚོགས་ནི་བདུད་ཀྱི་འཁོར་སྟོབས་དང་བཅས་པ་འམ། མུ་སྟེགས་ཅན་འཁོར་དང་བཅས་པ་ལ་བྱའོ། །

[Block 528 [HEADING]]
###### ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་སྤོང་བའི་ཡོན་ཏན། ^1-1-3-5-9-0

[Block 529]
ཐེག་པ་དེ་ནི་སངས་རྒྱས་ཀྱི་ཐེག་པ་སྒྲིབ་པ་མེད་པར་གྱུར་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཉོན་མོངས་པ་དང་། ཉེ་བའི་ཉོན་མོངས་པ་སྤོང་བའི་ཡོན་ཏན་བསྟན་ཏེ། སངས་རྒྱས་སུ་འགྲོ་བའི་ཐེག་པ་ནི་སངས་རྒྱས་ཀྱི་ཐེག་པ་སྟེ། སངས་རྒྱས་སུ་འགྲོ་བར་བྱེད་པའི་ཐེག་པ་ཡང་ཡིན་ལ་ཐེག་པ་དེས་ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པའི་སྒྲིབ་པ་ཡང་སེལ་བར་བྱེད་པས་ན། ཐེག་པ་དེ་ནི་སངས་རྒྱས་ཀྱི་ཐེག་པ་སྒྲིབ་པ་མེད་པར་གྱུར་པ་ཞེས་བྱའོ། །

[Block 530]
དེ་ལྟར་སྒྲིབ་པ་མེད་པར་འགྱུར་བས་མཐའ་དང་མཐའ་མེད་པར་ལྟ་བ་ལ་སོགས་པ་ལྟ་བའི་ཉོན་མོངས་པ་རྣམས་སེལ་བར་བྱེད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 531]
ལྟ་བ་ཞེས་བྱ་བའི་སྒྲ་མཐར་ལྟ་བ་དང་། མཐའ་མེད་པར་ལྟ་བ་དང་། རྟག་པར་ལྟ་བ་དང་། ཆད་པར་ལྟ་བ་དང་། འབྱུང་བར་ལྟ་བ་དང་། འཇིག་པར་ལྟ་བ་ཞེས་ཚིག་རེ་རེ་དང་སྦྱར་རོ། །

[Block 532]
དེ་ལ་མཐའ་དང་མཐའ་མེད་པར་ལྟ་བ་ནི་འདི་ལྟར་འདི་ན༌[^473]དགེ་སྦྱོང་ངམ་བྲམ་ཟེ་ཁ་ཅིག་འཇིག་རྟེན་པའི་བསམ་གཏན་ལ་བརྟེན་ནས་འཇིག་རྟེན་གྱི་མཐའ་ཡོད་པར་འདུ་ཤེས་པ་དང་། མཐའ་མེད་པར་འདུ་ཤེས་པ་སྟེ། དེ་ཡང་ཇི་ལྟར་ལྟ་ཞེ་ན། འཇིག་རྟེན་གྱི་མཐའ་ཐ་མར་ཆད་པར་འགྱུར་རམ་མི་འགྱུར་སྙམ་དུ་ཡང་དག་པར་ཚོལ་བར་བྱེད་དེ། གང་གི་ཚེ་འཇིག་པའི་བསྐལ་པ་རྗེས་སུ་དྲན་པ་དེའི་ཚེ་ནི་མཐའ་ཡོད་པར་འདུ་ཤེས་འབྱུང་བས་མཐའ་ཡོད་པར་ལྟ་བའོ། །

[Block 533]
གང་གི་ཚེ་ཆགས་པའི་བསྐལ་པ་དྲན་པ་དེའི་ཚེ་མཐའ་མེད་པའི་འདུ་ཤེས་འབྱུང་བས་མཐའ་མེད་པར་བལྟའོ།[^474] །རྟག་པར་ལྟ་བ་ནི་དགེ་སྦྱོང་ངམ་བྲམ་ཟེ་ཁ་ཅིག་བདག་དང་འཇིག་རྟེན་ནི་རྟག་པ་སྟེ། བྱས་པ་མ་ཡིན་པ་དང་། བྱས་པས་བྱས་པ་མ་ཡིན་པ་དང་། སྤྲུལ་པ་མ་ཡིན་པ་དང་། སྤྲུལ་པས་བྱས་པ་མ་ཡིན་པ་དང་། གསད་དུ་མེད་པ་དང་། ཐེར་ཟུག་ཏུ་གནས་པ་དང་། སྲོག་ཤིང་ལྟར་བརྟན་པར་གནས་པའོ་སྙམ་དུ་འཛིན་པའོ། །

[Block 534]
ཆད་པར་ལྟ་བ་ནི་དགེ་སྦྱོང་དང་བྲམ་ཟེ་ཁ་ཅིག་འདི་ལྟ་སྟེ། བདག་གཟུགས་ཅན་རགས་པ་འབྱུང་བ་ཆེན་པོ་བཞི་ལས་བྱུང་བ་ཇི་སྲིད་དུ་འདུག་ཅིང་སྡོད་ལ་འཚོ་བ་དེ་སྲིད་དུ་ནད་དང་བཅས་པ། འབྲས་དང་བཅས་པ། ཟུག་རྔུ་དང་བཅས་པ། རིམས་དང་བཅས་པ། ཡོངས་སུ་གདུང་བ་དང་བཅས་པ་ཡིན་ཏེ། ནམ་ཤི་བའི་འོག་ཏུ་བདག་ཆད་དེ་ཞིག་ཅིང་མེད་པར་གྱུར་པ་དེ་ན༌[^475]བདག་གཏན་ཆད་པར་འགྱུར་རོ་ཞེས་སྨྲ་བའོ། །

[Block 535]
འབྱུང་བར་ལྟ་བ་ནི་དངོས་པོ་སྐྱེ་བར་ལྟ་བའོ། །

[Block 536]
འཇིག་པར་ལྟ་བ་ནི་དངོས་པོ་འགག་པར་ལྟ་བའོ། །

[Block 537]
ལྟ་བར་གྱུར་པ་ཐམས་ཅད་ཅེས་སྨོས་པ་ནི་མིང་གིས་སྨོས་པ་ལས་མ་གཏོགས་པ་བདག་ཏུ་ལྟ་བ་ལ་སོགས་པ་ཀུན་བསྡུ་བའོ། །

[Block 538]
ཀུན་ནས་ལྡང་བ་ནི་ཉོན་མོངས་པ་ལ༌[^476]མངོན་སུམ་དུ་འབྱུང་བའོ། །

[Block 539]
སྒྲིབ་པ་ནི་སྒྲིབ་པ་ལྔ་རྣམས་སོ། །

[Block 540]
ཆོད་པ་ནི་དགེ་བའི་བར་དུ་གཅོད་པའི་ཆོས་དག་གོ། །

[Block 541]
ཐེ་ཚོམ་ནི་བདེན་པ་དང་དཀོན་མཆོག་ལ་ཡིད་མི་ཆེས་པའོ། །

[Block 542]
འགྱོད་པ་ནི་དགེ་བ་དང་མི་དགེ་བ་བྱས་ཀྱང་རུང༌[^477]མ་བྱས་ཀྱང་རུང་ཕྱིས་སེམས་ལ་གདུང་བ་སྐྱེ་བའོ། །

[Block 543]
སེལ་བ་ནི་དེ་དག་ཐེག་པ་འདིས་སྤོང་བར་བྱེད་པའོ། །

[Block 544 [HEADING]]
###### བདག་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན། ^1-1-3-5-10-0

[Block 545]
ཐེག་པ་དེ་ནི་ལྷག་པའི་བསམ་པ་དང་སྙིང་རྗེ་ཆེན་པོས་ཕྱེ་བས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་བདག་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན་བསྟན་ཏེ། ལྷག་པའི་བསམ་པ་དང་། སྙིང་རྗེ་ཆེན་པོས་ཕྱེ་བས༌[^478]ཞེས་བྱ་བ་ནི་ལྷག་པའི་བསམ་པ་ཆེན་པོ་དང་། སྙིང་རྗེ་ཆེན་པོའི༌[^479]རྒྱུ་ལས་བྱུང་བ༌[^480]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 546]
དེ་ལ་སེམས་ཅན་རྣམས་བདེ་བ་ལ་གཞག་པར་སེམས་པ་ནི་ལྷག་པའི་བསམ་པ་ཆེན་པོའོ། །

[Block 547]
སེམས་ཅན་རྣམས་ཀྱི་སྡུག་བསྔལ་མེད་པར་བྱེད་པར་སེམས་པ་ནི་སྙིང་རྗེ་ཆེན་པོའོ། །

[Block 548 [HEADING]]
###### **བདག་གི་དོན་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-5-10-1-0

[Block 549]
རྒྱུ་དེ་གཉིས་ལས་བྱུང་བས་ན་བདག་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པར་འགྱུར་ཏེ། བདག་གི་དོན༌[^481]ཕུན་སུམ་ཚོགས་པའང་རྣམ་པ་བཞིའོ། །

[Block 550]
གང་ཞེ་ན་ཆོས་ཕུན་སུམ་ཚོགས་པ་དང་། ཐེག་པ་ཕུན་སུམ་ཚོགས་པ་དང་། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་འབྱོར་པ་ཕུན་སུམ་ཚོགས་པ་དང་། མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་ལམ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 551 [HEADING]]
###### **ཆོས་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-5-10-1-1-0

[Block 552]
དེ་ལ་ཆོས་ཐམས་ཅད་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བས་ཆོས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ཆོས་ཀྱང་རྣམ་པ་གསུམ་མོ། །གང་ཞེ་ན། ཤེས་པར་བྱ་བའི་ཆོས་དང་། བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་། ཐོབ་པར་བྱ་བའི་ཆོས་སོ། །

[Block 553 [HEADING]]
###### **ཤེས་པར་བྱ་བའི་ཆོས།** ^1-1-3-5-10-1-1-1-0

[Block 554]
དེ་ལ་ཤེས་པར་བྱ་བའི་ཆོས་ནི་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་སོ། །

[Block 555 [HEADING]]
###### **བསྒྲུབ་པར་བྱ་བའི་ཆོས།** ^1-1-3-5-10-1-1-2-0

[Block 556]
བསྒྲུབ་པར་བྱ་བའི་ཆོས་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་སུམ་ཅུ་རྩ་བདུན་ནོ། །

[Block 557 [HEADING]]
###### **ཐོབ་པར་བྱ་བའི་ཆོས།** ^1-1-3-5-10-1-1-3-0

[Block 558]
ཐོབ་པར་བྱ་བའི་ཆོས་ནི་མྱ་ངན་ལས་འདས་པ་སྟེ། དེ་དག་དང་ལྡན་པས་ན་ཆོས་ཐམས་ཅད་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱའོ། །

[Block 559 [HEADING]]
###### **ཐེག་པ་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-5-10-1-2-0

[Block 560]
རིན་པོ་ཆེ་ཐམས་ཅད་དང་ལྡན་པ་ཞེས་བྱ་བས་ཐེག་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ཐེག་པ་དེར་སངས་རྒྱས་ལ་སོགས་པ་དཀོན་མཆོག་གསུམ་དང་། ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་སོགས་པ་ཐམས་ཅད་འདུས་པས་ན་རིན་པོ་ཆེ་ཐམས་ཅད་དང་ལྡན་པ་ཞེས་བྱའོ། །

[Block 561 [HEADING]]
###### **འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་འབྱོར་པ་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-5-10-1-3-0

[Block 562]
ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་རྙེད་པ་ཞེས་བྱ་བས་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་འབྱོར་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ཐེག་པ་དེ་ལ་བརྟེན་ནས༌[^482]འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་བས། ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་རྙེད་པ་ཞེས་བྱའོ། །

[Block 563 [HEADING]]
###### **མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་ལམ་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-5-10-1-4-0

[Block 564]
མི་སླུ་བའི་ལམ་དུ་འགྲོ་བ་ཞེས་བྱ་བས་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་ལམ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། མི་སླུ་བའི་ལམ་ནི་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་ལམ་མོ། །

[Block 565]
ཐེག་པ་འདིས་ཀྱང་ལམ་དེར་འགྲོ་བ་འམ། ལམ་དེ་དང་མཐུན་པའི་ཕྱིར་མི་སླུ་བའི་ལམ་དུ་འགྲོ་བའོ། །
--- END BLOCKS ---
