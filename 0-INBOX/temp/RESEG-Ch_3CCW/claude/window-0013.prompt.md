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
[Block 456]
ཕུང་པོ་ལ་སོགས་པ་དེ་དག་ཀྱང་ཉེ་བར་བཟུང་སྟེ་དེ་དང་འདིའི་ཡོད་པ་གང་ཡིན་པ་དེ་ཉེ་བར་བཟུང་ནས་རིང་པོ་དང་། ཐུང་ངུ་བཞིན་དུའམ། མར་མེའི་འོད་བཞིན་དུ་བསྟན༌[^293]ཏེ་གྱུར་པ་དེ་ལས་གཞན་དུ་མ་ཡིན་ཏེ། དེ་ལྟར་ན་ཉེ་བར་བཟུང་བའམ་བརྟེན་པར་ཟད་དོ། །

[Block 457]
དོན་རྟོགས་ཞེས་བྱ་བ་ཇི་ལྟ་བུ་ཞེ་ན། འབྲས་བུ་རྣམས་ཀྱི་མཐའ་མེད་པའི་ཕྱིར་དང་། འབྲས་བུ་རེ་རེའི་རྐྱེན་ཀྱང་དུ་མ་ཡོད་པའི་ཕྱིར་དང་། རྐྱེན་རེ་རེ་ལ་ཡང་བརྟགས་ན་ཐོག་མ་མེད་པའི་འཁོར་བ་བཞིན་དུ་རྒྱུའི་ཚོགས་པ་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་མཐའ་མི་མཐོང་བའི་ཕྱིར་འབྲས་བུའི་རྩོམ་པ་ལ་འཇིག༌[^294]པར་ལྟ་བས་རྒྱུའི་ཚོགས་པ་གཅིག༌[^295]བརྒྱུད་པས་བསྒྲུབས་པའི་འབྲས་བུ་རྐྱེན་དུ་མ་ལས་བྱུང་བ་གྲུབ་མ་ཐག་ཏུ་འཇིག་པར་རྟོགས་ཤིང་། སྐྱེ་བ་ནི་ཤིན་ཏུ་འབད་པས་བསྒྲུབ་པར་བྱ་བ་ཡིན་ལ། ཤིན་ཏུ་འབད་པས་བསྒྲུབས་པ་འཇིག་པ་ནི་འབད་པ་མེད་པར་ཡང་འབྱུང་བར་རྟོགས་ནས་འདུས་བྱས་ཀྱི་ཆོས་ཉིད་ལ་སྒྱིད་ལུག་པ། བྱིས་པ་སྐྱེ་བོའི་སྤྱོད་པ་ལ་མངོན་པར་མི་བསྟོད་པ། སྐྱེ་བ་ལ་མངོན་པར་མི་དགའ་བ། འཇིག་པ་ལ་མི་འཕྲོད་པར་འཛིན་པ། འཁོར་བ་རྣམས་ལ་ཆགས་པ་འདོར་བར་འདོད་པ། འཁོར་བ་སྤོང་བར་འདོད་པ། བདག་ལ་ཆགས་པ་ལྷོད་པར་གྱུར་པས་དེ་ལྟར་དོན་ཁོང་དུ་ཆུད་པ་ལ་དེའི་འོག་ཏུ་དབེན་པ་ནི་རིགས་ཀྱི་སྔ་རོལ་དུ༌[^296]ནི་མ་ཡིན་ནོ། །

[Block 458]
དེ་ལྟར་བྱས་ན་སློབ་དཔོན་གྱིས་སྟོང་པ་ཉིད་བསྟན་པ་ཡང་འབྲས་བུ་མེད་པར་མི་འགྱུར། སློབ་མ་རྣམས་ཀྱང་སྤོང་བ་དང་། ཕྱིན་ཅི་ལོག་ཏུ་འཛིན་པས་ལོག་པར་ལྟུང་བར་མི་འགྱུར་རོ། །

[Block 459]
དེ་ལྟར་མ་བྱས་ན་ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདེན་པ་གཉིས་རྣམ་པར་གནས་པ་དང་། མི་མཐུན་པར་གྱུར་པའི་ཕྱིར་སྟོང་པ་ཉིད་བསྟན་པས་ལོག་པར་ལྟུང་བར་འགྱུར་རོ། །

[Block 460]
དེ་ལྟར་གྱུར་ན་མི་དགེ་བ་སྤང༌[^297]མི་ནུས་སོ། །

[Block 461]
མི་མཁས་པའི་བློ་ཅན་དག་འགྲོ་བ་འདིའི་སྟོང་པའོ། །

[Block 462]
སྙམ་དུ་འཛིན་ཞིང༌[^298]འདི་ནི་སྟོང་པ་ཉིད་ན་འདིས་ཅི་ཞིག་བྱ་ཞེས་ངེས་པར་བསྒྲུབ་པར་བྱ་བའི་དགེ་བའི་ལས་ལ་མི་སྤྲོ་བར་འགྱུར་ཏེ། དེ་བས་ན་འདི་ཡང་སྒྲོ་གཤོག་མ་སྐྱེས་པའི་བྱ་རང་གི་ཚང་བོར་ནས་འཕུར་བ་བཞིན་དུ་བརླག་པར་འགྱུར་ཏེ། འདི་ལྟར་སོ་སོ་རང་གིས་རྟོགས་པ་དང་བྲལ་བའི་ཕྱིར།

[Block 463 [HEADING]]
### ཚིགས་བཅད་སོ་གཅིག་པ། ^1-32-0

[Block 464 [VERSE]]
རྣམ་པར་དབེན་དོན་མི་ཤེས་ལ། །
ཐོས་པ་ཙམ་ལ་འཇུག་བྱེད་ཅིང་། །
གང་རྣམས་བསོད་ནམས་མི་བྱེད་པ། །
སྐྱེས་བུ་ཐ་ཤལ་དེ་དག་བརླག །

[Block 465]
འཇིག་རྟེན་པ་ཉིད་ཀྱི་དོན་དམ་པ་ལ་གནས་ཏེ་ཕྱིན་ཅི་མ་ལོག་པ་རྣམ་པར་བྱང་བའི་ཕྱོགས་ཕུན་སུམ་ཚོགས་ཤིང་སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་སོ་སོ་རང་གིས་རྟོགས་པ་ན་བསོད་ནམས་དང་བསོད་ནམས་མ་ཡིན་པ་མི་བྱ་བ་ནི་རིགས་སོ། །

[Block 466]
གང་དག་སྟོང་པ་ཉིད་སོ་སོ་རང་གིས་རྟོགས་པ་མེད་པར་སྟོང་པ་ཉིད་ཀྱི་སྒྲ་ཐོས་པ་ཙམ་གྱིས་བྱ་བ་བྱས་པ་རྣམས་ཀྱི་སྤྱོད་པ་ལྟར་རྗེས་སུ་འཆོས་པ་ནི་མི་དགེ་བའི་ལས་ཉིད་ལ་ཞུགས་པ་ཡིན་གྱི། དགེ་བ་ལ་ནི་མ་ཡིན་ཏེ། དེ་དག་གདོན་མི་ཟ་བར་སྒྲོ་གཤོག་རྫོགས་པའི་བྱའི་ཚུལ་བྱིའུ་ཕྲུག་སྒྲོ་གཤོག་མ་སྐྱེས་པས་བྱ་བ་བཞིན་དུ་ཉོན་མོངས་པའི་མཐར་འགྱུར་རོ། །

[Block 467]
ཆུ་ཐོས་པ་ཙམ་གྱིས་སྐོམ་པ་མི་ཕྱེད་ལ། ཟས་ཐོས་པ་ཙམ་གྱིས་ཀྱང་བཀྲེས་པ་མི་ཕྱེད་དེ། དེ་བསྟན༌[^299]ན་དེ་དག་ཕྱེད་པ༌[^300]བཞིན་དུ་འདི་རྟོགས་ནས་སྐྱེས་བུ་ཐ་ཤལ་དེ་དག་བརླག་གོ་ཞེས་བརྗོད་དོ། །

[Block 468]
གཅིག་ཏུ་མི་དགེ་བ་ལ་འཇུག་པས་དེ་དག་ནི་སྐྱེས་བུ་ཐ་ཤལ་ལོ། །

[Block 469]
དེ་ལྟར་དེའི་ཉེས་པ་ཡོངས་སུ་སྤང་བར་བཞེད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་ཉན་པ་རྣམས་ལ་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ལས་ཡོངས་སུ་མ་ཉམས་པའི་དོན་རེ་ཞིག་ཐོག་མ་ཉིད་དུ།

[Block 470 [HEADING]]
### ཚིགས་བཅད་སོ་གཉིས་པ། ^1-33-0

[Block 471]
ལུས་ཀྱི་འབྲས་བུ་ཡོད་པ་དང་། །འགྲོ་བ་རྣམས་ཀྱང་ཤིན་ཏུ༌[^301]བརྗོད། །

[Block 472]
སེམས་ཅན་རྣམས་གང་ལ་གནས་ནས་ལས་རྣམས་བྱེད་ཅིང་དེའི་འབྲས་བུ་ཡང་ཟ་བའི་འགྲོ་བ་ལྔ་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་སོ། །

[Block 473]
དེའི་འོག་ཏུ་དེ་དག་གི་འདི་བདེན་ནོ་སྙམ་དུ་མངོན་པར་ཞེན་པ་མཆོག་ཏུ་འཛིན་པ་ལུས་ཀྱི་མདུད་པ་འདིའི་གཉེན་པོར།

[Block 474 [VERSE]]
དེ་ཡི་རང་བཞིན་ཡོངས་ཤེས་དང་། །
སྐྱེ་བ་མེད་པ་དག་ཀྱང་བསྟན། །

[Block 475]
འགྲོ་བ་ལ་སོགས་པ་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡིན་པས་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པའོ། །

[Block 476]
དེའི་རང་བཞིན་ཡོངས་སུ་ཤེས་པ་ལམ་དང་འགྲོ་བ་ལ་སོགས་པ་རྣམས་ཀྱི་སྐྱེ་བ་མེད་པ་ལམ་གྱི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བ་ཡང་བསྟན་ཏོ། །

[Block 477]
དེ་བས་ན་འདི་ལྟར་གཉི་གའི་བདག་ཉིད་བསྟན་པ་རྣམ་པར་གཞག་པ་འདི་ལ་དགོས་པའི་ཆེད་དུ་བསྟན་པ་ནི་གང་དོན་གྱི་ཆེད་དུ་བསྟན་པ་ནི༌[^302]གང་ཞེ་ན། འདི་ལ་དཔྱད་ན་གཏན་ལ་དབབ་ཏུ་རུང་སྟེ།

[Block 478 [HEADING]]
### ཚིགས་བཅད་སོ་གསུམ་པ། ^1-34-0

[Block 479 [VERSE]]
དགོས་པའི་དབང་དུ་རྒྱལ་བ་རྣམས། །
ང་དང་ང་ཡི་ཞེས་གསུངས་ལྟར། །
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་རྣམས། །
དེ་བཞིན་དགོས་པའི་དབང་གིས་གསུངས། །

[Block 480]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་ནི་ང་དང་ང་ཡིར་འཛིན་པ་སྤངས་པ་ཡིན། ཡང་བརྗོད་པར་བཞེད་པའི་དོན་གྱི་སྒོ་ནས་བསྟན་པའི་ཕྱིར་འཇིག་རྟེན་གྱི་ཆེད་དུ་ང་དང་ངའི་ཞེས་གསུངས་པ་དེ་བཞིན་དུ་དགོས་པའི་དབང་གིས་ཕུང་པོ་དང་སྐྱེ་མཆེད་དང་ཁམས་རྣམས་གསུངས་ཏེ། དེའི་རྣམ་པར་དབྱེ་བ་བསྟན་པ་མེད་པར་འཇིག་རྟེན་དེ་ཁོ་ན་ལ་ཞུགས་པའི་ཐབས་མེད་པའི་ཕྱིར་རོ། །

[Block 481]
ཇི་ལྟར་དགོས་པའི་དབང་དུ་ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་རྣམས་བཤད་ཀྱི་དེ་ཁོ་ནའི་དོན་དུ་ནི་མ་ཡིན་པར་འདི་ཇི་ལྟར་ཤེས་པར་ནུས་པ་འདི་ནི་འཐད་པ་དང་ལུང་གིས་ངེས་པར་རུང་སྟེ། དེ་ལ་རེ་ཞིག་འཐད་པའི་དབང་དུ་བྱས་ནས།

[Block 482 [HEADING]]
### ཚིགས་བཅད་སོ་བཞི་པ། ^1-35-0

[Block 483 [VERSE]]
འབྱུང་བ་ཆེ་ལ་སོགས་བཤད་པ། །
རྣམ་པར་ཤེས་སུ་ཡང་དག་འདུ། །
དེ་ཤེས་པས་ནི་འབྲལ་འགྱུར་ན། །
ལོག་པར་རྣམ་བརྟགས་མ་ཡིན་ནམ། །

[Block 484]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 485]
རྣམ་པར་ཤེས་པས་དམིགས་པ་གང་གི་རྣམ་པ་འཛིན་ཅིང་སྐྱེ་བའི་དམིགས་པ་དེ། རྣམ་པར་ཤེས་པ་ལ་རྣམ་པ་ཉེ་བར་བསྒྲུབས་པའི་རང་གི་དངོས་པོ་ཐོབ་ནས་དངོས་པོའི་དོན་གྱི་ངོ་བོ་ཉིད་ཀྱིས་འབྱུང་བ་ཆེན་པོ་ལ་སོགས་པར་ཡོངས་སུ་བརྟགས་སོ། །

[Block 486]
རྣམ་པར་ཤེས་པ་ལ་འགའ་ཞིག་གི་རྣམ་པར་མ་བཞག་པ་ལ་ནི་འཇིག་རྟེན་གྱིས་ཡོད་པ་ཉིད་དུ་རྣམ་པར་གཞག་མི་ནུས་ཏེ། མོ་གཤམ་གྱི་བུ་ལ་སོགས་པ་ཡང་ཡོད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 487]
དེ་བས་ན་འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ་དང་། སེམས་དང་སེམས་ལས་བྱུང་བ་དང་། སེམས་དང་ལྡན་པ་མ་ཡིན་པ་རྣམས་ནི་རྣམ་པར་ཤེས་པའི་རྣམ་པའི་རྒྱུ་ཅན་ཡིན་པའི་ཕྱིར་འབྱུང་བ་ཆེན་པོ་ལ་སོགས་པ་གང་དང་གང་བཤད་པ་ཅི་ཡང་རུང་བ་དེ་དག་ཐམས་ཅད་ནི་རྣམ་པར་ཤེས་པར་ཡང་དག་པར་འདུ་ཞིང་ཁོངས་སུ་ཆུད་དོ། །

[Block 488]
གང་གི་ཚེ་རྣལ་འབྱོར་པས་ཡོད་པ་མེད་པ་ཡིན་པའི་དོན་སྒྲོ་འདོགས་པའི་རྣམ་པར་ཤེས་པའི་ཚངས་པ་དེ་བརྫུན་པ་སླུ་བའི༌[^303]ཆོས་ཅན་དུ་མཐོང་ཞིང་རང་བཞིན་གྱིས་སྐྱེ་བ་མེད་པར་མཐོང་བ་དེའི་ཚེ་ངེས་པར་དེ་ཤེས་ཏེ། ཇི་ལྟར་གནས་པའི་སེམས་རང་གི་ངོ་བོས་སྐྱེ་བ་མེད་པར་ཤེས་པས་དེས་བསྐྱེད་པ་འབྱུང་བ་ཆེན་པོ་ལ་སོགས་པ་མ་ལུས་པ་དག་ཀྱང་གཟུགས་འགགས༌[^304]ན་གཟུགས་བརྙན་འགགས་པ༌[^305]བཞིན་དུ་འབྲལ་བར་འགྱུར་ན། དེ་ལྟ་བུ་གང་ཡིན་པ་དེ་གཟུགས་བརྙན་བཞིན་དུ་ལོག་པར་རྣམ་པར་བརྟགས་པ་ཉིད་མ་ཡིན་ནམ། དེའི་ཕྱིར་དེ་ལྟར་ཕུང་པོ་ལ་སོགས་པ་དེ་དག་ནི་རྣམ་པར་ཤེས་པའི་རྒྱུས་ཡོད་པ་ཉིད་དེ༌[^306]མེད་ན་ཡོད༌[^307]པས་ངོ་བོ་ཉིད་དུ་གྲུབ་པ་མེད་པ་ཁོ་ན་ཡིན་པ་ལ་ངར་འཛིན་པ་དང་ང་ཡིར་འཛིན་པའི་མངོན་པའི་ང་རྒྱལ་ཅན་གྱི་དབང་དུ་བསྟན་པར་ངེས་སོ། །

[Block 489]
རེ་ཞིག་དེ་ལྟར་རིགས་པས་ཕུང་པོ་ལ་སོགས་པ་དགོས་པའི་དབང་དུ་བསྟན་པར་ཤེས་པར་བྱས་ནས། ད་ནི་ལུང་གིས་ཕུང་པོ་ལ་སོགས་པ་བརྫུན་པ་ཉིད་དུ་བསྟན་པས་དགོས་པའི་ཆེད་དུ་བརྗོད་པར་བསྟན་པའི་ཕྱིར།

[Block 490 [HEADING]]
### ཚིགས་བཅད་སོ་ལྔ་པ། ^1-36-0

[Block 491 [VERSE]]
མྱ་ངན་འདས་པ་བདེན་གཅིག་པུ། །
རྒྱལ་བ་རྣམས་ཀྱིས་རྣམས༌[^308]གསུངས་པ། །
དེའི་ཚེ་ལྷག་མ་ལོག་པ་ཞེས། །
མཁས་པ་སུ་ཞིག་རྟོགས་མི་བྱེད། །

[Block 492]
ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 493]
བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་དག་འདི་ལྟ་སྟེ། མི་སླུ་བའི༌[^309]ཆོས་ཅན་མྱ་ངན་ལས་འདས་པ་འདི་ནི་བདེན་པའི་མཆོག་གཅིག་ཏུའོ༌[^310]ཞེས་གསུངས་ཏེ་ལུང་འདིས༌[^311]དོན་གྱིས་ན་ཤེས་རབ་ཅན་སུ་ཞིག་ཕུང་པོ་ལ་སོགས་པ་བརྫུན་པའི་དོན་ཁོང་དུ་ཆུད་པར་མི་འགྱུར། གང་གི་ཕྱིར་ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་དེ་དག་རྣམ་པ་དེ་ལྟར་རིགས་པ༌[^312]དང་། ལུང་གིས་རྣམ་པར་དཔྱད་ན་ངོ་བོ་ཉིད་ཀྱིས༌[^313]གྲུབ་པ་མེད་པ་དེའི་ཕྱིར་ངེས་པར།

[Block 494 [HEADING]]
### ཚིགས་བཅད་སོ་དྲུག་པ། ^1-37-0

[Block 495 [VERSE]]
ཇི་སྲིད་ཡིད་ཀྱིས༌[^314]རྣམ་གཡོ་བ། །
དེ་སྲིད་བདུད་ཀྱི་སྤྱོད་ཡུལ་ཏེ། །
--- END BLOCKS ---
