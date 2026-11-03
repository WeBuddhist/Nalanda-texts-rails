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
[Block 456 [HEADING]]
###### **ཏིང་ངེ་འཛིན་ཐོབ་པ།** ^1-1-3-4-3-1-0

[Block 457]
ཏིང་ངེ་འཛིན་ཐོབ་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། མི་གཡོ་བ་ཐོབ་པ་དང་། རྒྱུན་དུ་ཡིད་ལ་བྱེད་པ་ཐོབ་པའོ། །

[Block 458 [HEADING]]
###### **མི་གཡོ་བ་ཐོབ་པ།** ^1-1-3-4-3-1-1-0

[Block 459]
དམིགས་པ་ལ་འཇུག་པ་ཐོབ་པ༌[^415]དང་ཞེས་བྱ་བས་མི་གཡོ་བ་ཐོབ་པ་བསྟན་ཏེ། དམིགས་པ་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ལ་སོགས་པ་ཏིང་ངེ་འཛིན་གྱི་ཡུལ་རྣམས་སོ། །

[Block 460]
འདུག་པ་ཐོབ་པ་ནི་ཡུལ་ལ་དམིགས་པའི་ཚེ་སེམས་རྩེ་གཅིག་པ་ལ་གནས་པ་ཐོབ་པ༌[^416]སྟེ། ཕྱི་རོལ་དུ་མི་གཡེང་བར་ནུས་པའོ། །

[Block 461 [HEADING]]
###### **རྒྱུན་དུ་ཡིད་ལ་བྱེད་པ་ཐོབ་པ།** ^1-1-3-4-3-1-2-0

[Block 462]
བསམ་གཏན་དང་རྣམ་པར་ཐར་པ་དང་ཏིང་ངེ་འཛིན་དང་སྙོམས་པར་འཇུག་པ་རྒྱུན་མི་ཆད་ཅེས་བྱ་བས་རྒྱུན་དུ་ཡིད་ལ་བྱེད་པ་ཐོབ་པ་བསྟན་ཏེ། རྒྱུན་མི་ཆད་པ་ནི་དེ་དག་ལ་རྒྱུན་དུ་ཡིད་ལ་བྱེད་པའོ། །

[Block 463 [HEADING]]
###### **མངོན་པར་བྱང་ཆུབ་པ།** ^1-1-3-4-3-2-0

[Block 464]
མངོན་པར་བྱང་ཆུབ་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། སྟོན་པ་དང་རྗེས་སུ་སྟོན་པར་བྱེད་པར་མངོན་པར་བྱང་ཆུབ་པ་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 465 [HEADING]]
###### **སྟོན་པ་དང་རྗེས་སུ་སྟོན་པ་མེད་པར་མངོན་པར་བྱང་ཆུབ་པ།** ^1-1-3-4-3-2-1-0

[Block 466]
གཞན་གྱི་དྲིང་ལ་མི་འཇོག་པའི་ཡེ་ཤེས་བསྐྱེད་པ༌[^417]དང་ཞེས་བྱ་བས་སྟོན་པ་དང་རྗེས་སུ་སྟོན་པ་མེད་པར་མངོན་པར་བྱང་ཆུབ་པ་བསྟན་ཏེ། མཁན་པོ་དང་སློབ་དཔོན་གྱི་མན་ངག་ལ་མི་རྟེན་པར༌[^418]ཟད་ལ་མི་སྐྱེ་བའི་ཡེ་ཤེས་སྐྱེད་པར༌[^419]བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 467 [HEADING]]
###### **རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མངོན་པར་བྱང་ཆུབ་པ།** ^1-1-3-4-3-2-2-0

[Block 468]
དམིགས་པ༌[^420]གང་ཡང་རུང་བ་ལ་རྐྱེན་གྱི་ཡེ་ཤེས་རྟོགས་པ༌[^421]སྟེ་ཞེས་བྱ་བས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མངོན་པར་བྱང་ཆུབ་པར་བསྟན་ཏེ། དམིགས་པའི་ཡུལ་གང་ཡང་རུང་སྟེ། ཆོས་ཐམས་ཅད་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ངོ་བོ་ཉིད་དུ་ཤེས་ཤིང་ཁོང་དུ་ཆུད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 469]
དེ་ལྟར་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པའི་ཚུལ་ལྟར་རོ། །

[Block 470]
འཆད་པ་ནི་དོན་ཏོ། །

[Block 471]
སྟོན་པ་ནི་ཚིག་གོ། །

[Block 472]
རབ་ཏུ་སྟོན་པ་ནི་དོན་དང་ཚིག་གོ། །

[Block 473]
ཡང་ན་རྒྱུ་སྟོན་པ་ནི་འཆད་པའོ། །

[Block 474]
རྐྱེན་འཆད་པ་ནི་སྟོན་པའོ། །

[Block 475]
འབྲས་བུ་འཆད་པ་ནི་རབ་ཏུ་སྟོན་པའོ། །

[Block 476 [HEADING]]
##### བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་ཆེན་པོ་ལ་མཁས་པ། ^1-1-3-5-0

[Block 477]
བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་ལ་མཁས་པ༌[^422]བསྟན་པའི་ཕྱིར། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་ཆེན་པོ༌[^423]ལ་མཁས་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 478]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཁོང་དུ་ཆུད་པར་བྱ་བའི་ཐེག་པ་འམ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་མི་གནས་པའི་མྱ་ངན་ལས༌[^424]འདའ་བར་ཕྱིན་པར༌[^425]བྱེད་པའི་ཐེག་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་སྟེ། འདིས་འགྲོ་བས་ཐེག་པ་འམ། འདིར་འགྲོ་བས་ཐེག་པའོ།[^426] །དེ་ལ་འདིས་འགྲོ་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ས་རྣམས་ཀྱིས༌[^427]འགྲོ་བས་ན་དེ་དག་ལ་ཐེག་པ་ཞེས་བྱའོ། །

[Block 479]
འདིར་འགྲོ་བ་ནི་སངས་རྒྱས་ཀྱི་སར་འགྲོ་བ་སྟེ། དེ་ལ་ཐེག་པ་ཞེས་བྱའོ། །

[Block 480]
ཐེག་པ་ཡང་ཡིན་ལ་ཆེན་པོ་ཡང་ཡིན་པས་ཐེག་པ་ཆེན་པོ་སྟེ། ཆེན་པོ་རྣམ་པ་བདུན་པ༌[^428]དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 481]
ཆེན་པོ་རྣམ་པ་བདུན་ནི་ཆོས་ཆེ་བ་དང་། སེམས་བསྐྱེད་པ༌[^429]ཆེ་བ་དང་། བསམ་པ་ཆེ་བ་དང་། མོས་པ་ཆེ་བ་དང་། ཚོགས་ཆེ་བ་དང་། དུས་ཆེ་བ་དང་། ཐོབ་པ་ཆེ་བའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟོང་ཕྲག་བརྒྱ་པ་ལ་སོགས་པ་མདོ་སྡེ་ཚད་མེད་པའི་ཕྱིར་ཆོས་ཆེ་བའོ།[^430] །སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་དུ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ༌[^431]སེམས་བསྐྱེད་པས༌[^432]སེམས་བསྐྱེད་པ་ཆེ་བའོ། །

[Block 482]
ཟབ་ཅིང་རྒྱ་ཆེ་བའི་མདོ་སྡེ་ལ་མོས་པའི་ཕྱིར་མོས་པ་ཆེ་བའོ།[^433] །བདག་དང་གཞན་མཉམ་པ་ཉིད་ཀྱི་བསམ་པ་ཐོབ་པས་ན་བསམ་པ་ཆེ་བའོ། །

[Block 483]
སྐད་ཅིག་མ་རེ་རེ་ལ་ཡང་བསོད་ནམས་ཀྱི་ཚོགས་དཔག་ཏུ་མེད་པ༌[^434]སོགས་པས་ན་ཚོགས་ཆེ་བའོ། །

[Block 484]
བསྐལ་པ་ཆེན་པོ་གྲངས་མེད་པ་གསུམ་གྱི་བར་དུ་རྒྱུན་དུ་སྦྱར་བས༌[^435]ན་དུས་ཆེ་བའོ། །

[Block 485]
བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་འབྲས་བུ་ཐོབ་པས་ན་ཐོབ་པ་ཆེ་བའོ། །

[Block 486]
ཐེག་པ་དེའི་རང་བཞིན་དང་། རྒྱུ་དང་འབྲས་བུ་ལ་སོགས་པ་རྟོགས་པ་ནི་ཐེག་པ་ཆེན་པོ་ལ་མཁས་པའོ། །

[Block 487]
གང་ཞེ་ན་ཞེས་བྱ་བ་ནི་དྲིས་པའོ། །

[Block 488]
བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་ཆེན་པོ་ལ་མཁས་པ་ནི་དཔག་ཏུ་མེད་དེ་ཞེས་བྱ་བ་ལ། ཐེག་པ་ནི་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་ཕྱིན་པར་བྱེད་པ་སྟེ། ཐེག་པ་དེ་ལས་འདས་པ་དང་མ་འོངས་པ་དང་ད་ལྟར་གྱི་དུས་ཀྱི་སེམས་ཅན་གྲངས་མེད༌[^436]ཚད་མེད་པ་རྣམས་འཚང་རྒྱ་བའི་ཕྱིར་ཐེག་པ་དེ་ཚད་མེད་དོ། །

[Block 489]
ཐེག་པ་ཚད་མེད་པས་དེ་ལ་མཁས་པའི་ཤེས་རབ་ཀྱང་ཚད་མེད་པའི་ཕྱིར་ཐེག་པ་ཆེན་པོ་ལ་མཁས་པ་ནི་དཔག་ཏུ་མེད་དོ་ཞེས་གསུངས་སོ། །

[Block 490]
དེ་ལྟར་ཐེག་པ་ཆེན་པོ་ཚད་མེད་པས་ན་ཐམས་ཅད་བསྟན་པར་མི་ནུས་ཏེ། དེ་བས་ན་དེ་ལ༌[^437]ཕྱོགས་ཙམ་ཞིག་བསྟན་ཏོ་ཞེས་གསུངས་ཏེ། མདོ་ཙམ་ཞིག་བསྟན་ཏོ་ཞེས་བྱ་བའི་དོན་ཏོ།[^438] །ཚད་མེད་པ་དེ་ཡང་ཡོན་ཏན་བཅུ་གཅིག་ཏུ་རིག་པར་བྱ་སྟེ། སེམས་བསྐྱེད་པའི་ཡོན་ཏན་དང་། ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་ཏེ། ཤེས་པ་ཁོང་དུ་ཆུད་པའི་ཡོན་ཏན་དང་རྒྱུ་བསྩགས་པའི་ཡོན་ཏན་དང་། སྤྱོད་པ་དག་པའི་ཡོན་ཏན་དང་། མངོན་པར་བྱང་ཆུབ་པའི་ཡོན་ཏན་དང་། མཉན་པར༌[^439]ཕན་འདོགས་པའི་ཡོན་ཏན་དང་། ཉན་ཐོས་དང་སོ་སོའི་སྐྱེ་བོའི་ལམ་ལས་རྒལ་བའི༌[^440]ཡོན་ཏན་དང་། བགེགས་བཅོམ་པའི་ཡོན་ཏན་དང་། ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་སྤངས་པའི༌[^441]ཡོན་ཏན་དང་། བདག་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན་དང་། འབྲས་བུ་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན་ནོ། །

[Block 491 [HEADING]]
###### སེམས་བསྐྱེད་པའི་ཡོན་ཏན། ^1-1-3-5-1-0

[Block 492]
ཐེག་པ་དེ་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་གོ་སྐབས་འབྱེད་པས་ན་དཔག་ཏུ་མེད་པའོ་ཞེས་བྱ་བས་སེམས་བསྐྱེད་པའི་ཡོན་ཏན་བསྟན་ཏེ། སེམས་ཅན་ཚད་མེད་པ་རྣམས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་གདོན་ཞིང༌[^442]མངོན་པར་འཚང་རྒྱ་བའི་སྐབས་འབྱེད་པས་ན་གོ་སྐབས་འབྱེད་པ་ཞེས་བྱ་སྟེ། ཐེག་པ་དེ་ཡང་དེའི་རྒྱུར་གྱུར་པའི་ཕྱིར།[^443] སེམས་ཅན་དཔག་ཏུ་མེད་པས་དེ་ཡང་དཔག་ཏུ་མེད་པའོ། །

[Block 493]
རྣམ་པ་གཉིས་ཀྱིས༌[^444]དཔག་ཏུ་མེད་པ་སྟེ། རྒྱ་ཆེ་བ་དང་། ཚད་མེད་པའོ། །

[Block 494]
ཅི་ཙམ་དུ་བསྒྲུབ་པར་བྱ་བའི་དགེ་བའི་རྩ་བ་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་ཐམས་ཅད་སྒྲུབ་པར་བྱེད་པས་རྒྱ་ཆེ་བས་སོ།[^445] །དགེ་བའི་རྩ་བ་དེ་དག་ཐམས་ཅད་ཀྱང་སེམས་ཅན་གྱི་དོན་དུ་སྒྲུབ་པར་བྱ་བའི༌[^446]ཕྱིར་ཚད་མེད་པའོ། །

[Block 495]
ཡང་ན་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི་ཚེ་སེམས་ཅན་འགའ་ཡང་མ་བཀོལ་བར༌[^447]སེམས་ཅན་ཚད་མེད་པ་ཐམས་ཅད་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་བསྒྲལ་ལོ་ཞེས་སེམས་བསྐྱེད་པས་ན། སེམས་ཅན་ཐམས་ཅད་ཀྱི་གོ་སྐབས་འབྱེད་པ་ཞེས་བྱ་སྟེ། སེམས་ཅན་དཔག་ཏུ་མེད་པའི་ཕྱིར་ཐེག་པ་དེ་ཡང་དཔག་ཏུ་མེད་པའོ། །
--- END BLOCKS ---
