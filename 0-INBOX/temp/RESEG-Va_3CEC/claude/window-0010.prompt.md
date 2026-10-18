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
[Block 351 [HEADING]]
##### རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་ལ་མཁས་པ། ^1-1-3-4-0

[Block 352]
ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་བསྟན་ནས། རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^341]ཤེས་པར་བྱ་བའི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་ཞེས་བྱ་སྟེ། གང་དག་བསྐལ་པ་གཅིག་གིས༌[^342]ཡེ་ཤེས་ཀྱི་ཚོགས་ཡོངས་སུ་བསྐངས་ཏེ། གཞན་གྱི༌[^343]མན་ངག་མེད་པར་འཕགས་པའི་ལམ་ཐོབ་ནས་ཁམས་གསུམ་པའི་འདོད་ཆགས་དང་བྲལ་བར་ཞུགས་པ་དེ་དག་ནི་སྙིང་རྗེ་ཆེན་པོ་མེད་པས་གཞན་ལ་ལུང་དཔོག་པའི༌[^344]བྱ་བ་མེད་པ་དང་། བདག་གཅིག་པུ་སངས་རྒྱས་པར་བྱེད་པས་རང་སངས་རྒྱས་སོ། །

[Block 353]
རང་སངས་རྒྱས་དེ་དག་རྣམ་པར་གྲོལ་བའི་སར་ཕྱིན་པར་བྱེད་པའི་ཐེག་པ་ནི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་སྟེ། གང་ཞེ་ན་ཞེས་བྱ་བ་ནི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་དྲིས་པའོ། །

[Block 354]
དེ་ཡང་རྣམ་པ་གསུམ་དུ་རིག་པར་བྱ་སྟེ། རྒྱུ་དང་རྐྱེན་དང་འབྲས་བུའོ། །

[Block 355]
དེ་རྣམ་པ་གང་ཞེས་བྱ་བས་རྒྱུ་བསྟན་པ་ཡིན་ཏེ། རྒྱུ་གང་དག་གིས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 356]
རྐྱེན་གང་ཞེས་བྱ་བས་རྐྱེན་བསྟན་པ་ཡིན་ནོ། །

[Block 357]
རང་སངས་རྒྱས་འབྱུང་ཞེས་འབྲས་བུ་བསྟན་པ་ཡིན་ཏེ། ཁམས་གསུམ་ལས་བྱུང་ནས་ཉོན་མོངས་པ་ཐམས་ཅད་སྤངས་ཏེ། མྱ་ངན་ལས་འདས་པར་གྱུར་པ་ནི་རང་སངས་རྒྱས་རྣམས་འབྱུང་བར་འགྱུར་ཞེས་བྱའོ། །

[Block 358]
ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་ཞེས་བྱ་བ་ནི་རྒྱུ་དང་རྐྱེན་དང་འབྲས་བུ་རྣམས་ཕྱིན་ཅི་མ་ལོག་པར་ཁོང་དུ་ཆུད་ཅེས་བྱ་བའི་དོན་ཏེ། དེ་ལྟར་ཁོང་དུ་ཆུད་པ་ནི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 359]
དེ་དག་གང་ཞེ་ན། རྒྱུ་དང་རྐྱེན་དང་འབྲས་བུ་དེ་དག་གང་ཞེ་ན་ཞེས་བྱ་བའི་དོན་ཏེ། དོན༌[^345]གསུམ་བསྟན་པའི་ཕྱིར་འདི་ལྟ་སྟེ་ཞེས་གསུངས་སོ། །

[Block 360]
དེ་ལ་འདུན་པ་དང་བརྩོན་འགྲུས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། རབ་ཏུ་དབེན་པར་གནས་མལ་འཆའ་བ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རྒྱུ་བསྟན་པ་ཡིན་ནོ། །

[Block 361]
བསྙེན་པར༌[^346]དཀའ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ་རང་འབྱུང་གི༌[^347]ཡེ་ཤེས་ཀྱིས་རབ་ཏུ་རྒལ༌[^348]ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རྐྱེན་བསྟན་ཏོ། །

[Block 362]
དམིགས་པ་ལ་གནས་པ་ཐོབ་ཅེས་བྱ་བ་ནས་བརྩམས་ཏེ། དམིགས་པ་གང་ཡང་རུང་བ་ལ་རྐྱེན་གྱིས་ཡེ་ཤེས་རྟོགས་པ༌[^349]ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^350]འབྲས་བུ་བསྟན་ཏོ། །

[Block 363 [HEADING]]
###### རྒྱུ། ^1-1-3-4-1-0

[Block 364]
དེ་ལ་རྒྱུ་རྣམ་པ་གསུམ་སྟེ།[^351] བསྩགས་པའི་རྒྱུ་དང་། སངས་རྒྱས་མཉེས་པར་བྱེད་པའི་རྒྱུ་དང་། རིགས་སོ། །

[Block 365 [HEADING]]
###### **བསགས་པའི་རྒྱུ།** ^1-1-3-4-1-1-0

[Block 366]
དེ་ལ་བསགས་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། གང་གིས་བསགས་པ་དང་། གང་བསགས་པའོ། །

[Block 367 [HEADING]]
###### **གང་གིས་བསགས་པ།** ^1-1-3-4-1-1-1-0

[Block 368]
དེ་ལ་གང་གིས་བསགས་པ་ནི་འདུན་པ་དང་བག་ཡོད་པ་དང་བརྩོན་འགྲུས་ཆེན་པོ་གསུམ་གྱིས་བསྩགས་སོ། །

[Block 369]
གང་བསྩགས་པ་ནི་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་དང་ཐོས་པ་གསུམ་བསྩགས་སོ། །

[Block 370]
གང་གིས་བསྩགས་པ་ཡང་རྣམ་པ་གསུམ་སྟེ། རྒྱུ་དང་རྐྱེན་རྐྱེན༌[^352]དང་། སྒྲུབ་པའོ། །

[Block 371]
དེ་ལ་ཆེན་པོའི་སྒྲ་ནི་འདུན་པ་ལ་སོགས་པའི་ཚིག་གསུམ་པོ་སོ་སོ་དང་ཡང་སྦྱར་ཏེ། འདུན་པ་ཆེན་པོ་དང་། བརྩོན་འགྲུས་ཆེན་པོ་དང་། བག་ཡོད་པ་ཆེན་པོ༌[^353]ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 372]
དེ་ལ་འདུན་པ་ནི་དཀོན་མཆོག་དང་བདེན་པ་དང་ལས་ལ་ཡིད་ཆེས་ནས་འདི་ཁོ་ན་བདེན་གྱི་གཞན་དུ་མ་ཡིན་ནོ༌[^354]ཞེས་འཛིན་པའོ། །

[Block 373]
འདིས་ནི་རྒྱུ་སྨྲས་པ་ཡིན་ཏེ། ཡིད་ཆེས་པར་གྱུར་ན་བརྩོན་འགྲུས་རྩོམ་པས་སོ། །

[Block 374]
བརྩོན་འགྲུས་ཞེས་བྱ་བ་ལ། སྤང་བར་བྱ་བ་མ་ལུས་པར་སྤོང་བ་དང་། ཐོབ་པར་བྱ་བ་ཐོབ་པར་བྱེད་པ་ལ་སེམས་སྤྲོ་བ་ནི་བརྩོན་འགྲུས་ཏེ། འདིས་ནི་རྐྱེན་བསྟན་པ་ཡིན་ཏེ། དགེ་བ་སྒྲུབ་པ་རྣམས་བརྩོན་འགྲུས་ལ་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 375]
བག་ཡོད་པ་ཞེས་བྱ་བ་ལ། གཅིག་པུ་དགོན་པ་ན་གནས་ཤིང་འདུ་འཛི་དང་མི་འདྲེ་བ་ནི་བག་ཡོད་པ་སྟེ། འདིས་ནི་སྒྲུབ་པར་བྱེད་པ་བསྟན་པ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྤང་བར་བྱ་བ་དང་བསྒྲུབ་པར༌[^355]བྱ་བ་གཉིས་ནི་བག་ཡོད་པར༌[^356]བསྒྲུབས་སོ། །

[Block 376 [HEADING]]
###### **གང་བསྩགས་པ།** ^1-1-3-4-1-1-2-0

[Block 377]
གང་བསྩགས་པ་ཡང་རྣམ་པ་གསུམ་སྟེ། ལོངས་སྤྱོད་ཀྱི་རྒྱུ་བསྩགས་པ་དང་། བདེ་འགྲོའི་རྒྱུ་བསྩགས་པ་དང་། རྣམ་པར་གྲོལ་བའི་རྒྱུ་བསྩགས་པའོ། །

[Block 378]
ཡང་ན་སེར་སྣའི་གཉེན་པོ་བསྩགས་པ་དང་། འདོད་པ་ལ་ཆགས་པའི་གཉེན་པོ་བསྩགས་པ་དང་། ཉོན་མོངས་པའི་གཉེན་པོ་བསྩགས་པའོ། །

[Block 379]
དེ་ལ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་རང་སངས་རྒྱས་ཀྱི་འདུན་པ༌[^357]དང་བརྩོན་འགྲུས་ལ་སོགས་པ་ཉན་ཐོས་དག་པས་ལྷག་པས་ན་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 380]
ཉན་ཐོས་ལྟ་བུ་མ་ཡིན་པའི་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་ཀྱི་བས་ཤས་ཆེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 381]
སྦྱིན་པའི་བསོད་ནམས་ཀྱི་ཚོགས༌[^358]སོགས་པ་ཞེས་བྱ་བས་སེར་སྣའི་གཉེན་པོ་སྤངས་པ་བསྟན་ཏེ། སྦྱིན་བས༌[^359]རྣམ་པར་གྲོལ་བ་ཐོབ་པའི་རྒྱུར་གྱུར་པ་རྣམས་ནི་ཚོགས་བསགས་པ་ཞེས་བྱའོ། །

[Block 382]
ཚུལ་ཁྲིམས་ཀྱིས༌[^360]བསོད་ནམས་ཀྱི་ཚོགས་བསྩགས་པ་ཞེས་བྱ་བས་འདོད་པ་ལ་ཆགས་པའི་གཉེན་པོ་བསྩགས་པ་བསྟན་ཏོ། །

[Block 383]
གང་གིས། གང་། གང་གི་ཕྱིར་ཚུལ་བསྲུངས་བ་ནི་ཚུལ་ཁྲིམས་ཏེ། གང་གིས་བསྲུང་བ༌[^361]ནི་མི་དགེ་བ་བཅུ་ལས་ལྡོག་ཅིང་རྣམ་པར་གྲོལ་བ་འདོད་པའི་སེམས་ཀྱིས་སོ། །

[Block 384]
གང་བསྲུང་བ༌[^362]ནི་ཡན་ལག་དྲུག་པའི་ཚུལ་ཁྲིམས་བསྲུང་བའོ། །

[Block 385]
གང་གི་ཕྱིར་བསྲུང་བ་ནི་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་བྱ་བའི་ཕྱིར་བསྲུང་བའོ། །

[Block 386]
ཐོས་པ་ཉུང་བ་ལ་ཆོས་ཀྱི་ནན་ཏན་བྱེད༌[^363]ཅེས་བྱ་བས་ཉོན་མོངས་པའི་གཉེན་པོ༌[^364]བསྩགས་པ་བསྟན་ཏེ། །ཐོས་པ༌[^365]ལ་མི་དགའ་བས་ཅུང་ཟད་ཐོས་པ་ནི་ཐོས་པ༌[^366]ཉུང་བའོ། །

[Block 387]
ཆོས་ཀྱི་ནན་ཏན་བྱེད་ཅེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་རྣམས་བསྒོམས༌[^367]ཤིང་སྒྲུབ་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 388]
དེ་ནི་འདི་སྐད་དུ་ཉན་ཐོས་ལྟར་ཐོས་པ་མི་མང་བར་ཐོས༌[^368]པ་ཅུང་ཟད་ཅིག་གིས་ཆོས་ཀྱི་ནན་ཏན་བྱེད་དོ་ཞེས་བསྟན་པའོ། །

[Block 389 [HEADING]]
###### **སངས་རྒྱས་མཉེས་པར་བྱེད་པ།** ^1-1-3-4-1-2-0

[Block 390]
སངས་རྒྱས་མཉེས་པར་བྱེད་པ༌[^369]ཡང་རྣམ་པ་གཉིས་ཏེ། ཆོས་ཉིད་ཀྱིས་མཉེས་པར་བྱེད་པ་དང་། ཟང་ཟིང་གིས་མཉེས་པར་བྱེད་པའོ། །
--- END BLOCKS ---
