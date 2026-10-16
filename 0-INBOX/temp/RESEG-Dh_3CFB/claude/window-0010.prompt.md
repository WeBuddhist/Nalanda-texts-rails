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
[Block 351]
བམ་པོ་གཉིས་པ། [^214]

[Block 352 [HEADING]]
## རང་བཞིན་མེད་ན་མི་འབྱུང་བ། ^4-0

[Block 353]
འབྲས་བུ་ནི་དེ་ལས་སྐྱེ་བའི༌[^215]ཕྱིར་རྒྱུ་མེད་ན་མི་འབྱུང་བ་ཡིན་ལ་རག་ན། ད་རང༌[^216]བཞིན་ཇི་ལྟར་མེད་ན་མི་འབྱུང་བ་ཡིན་ནོ༌[^217]ཞེ་ན།

[Block 354 [VERSE]]
རང་བཞིན་ལ་ཡང་མེད་མི་འབྱུང་། །
ཡོད་པ་ཙམ་དང་འབྲེལ་པ་ཡིན། །

[Block 355]
གང་ཞིག་ཡོད་པ་ཙམ་དང་འབྲེལ་པའི་རང་བཞིན་ཡིན་པ་དེ་ལ་ནི་ཡོད་པ་མེད་ན་མི་འབྱུང་བར་འདོད་དེ། དེ་མེད་པར༌[^218]ནི་ཡོད་པ་དག །མེད་འགྱུར་ཐ་དད་མེད་ཕྱིར་རོ།[^219] ། ངོ་བོ་གང་ཁོ་ན་ཡོད་པ་ཙམ་ལ་རག་ལས་པའི་རང་བཞིན་ཡིན་པར་བརྗོད་པ་དེ་ཁོ་ན་རང་གིས་དངོས་སུ་ཡོད་པ་ཡིན་ནོ། །

[Block 356]
དེ་ཡང་བདག་ཉིད་བོར་ནས་ཇི་ལྟར་ཡོད་པར་འགྱུར། འོ་ན་ནི་ཐ་དད་པ་མེད་པའི་ཕྱིར་བྱས་པ་གང་ཡིན་པ་དེ་ཉིད་མི་རྟག་པ་ཡིན་པས་དམ་བཅས་པའི༌[^220]དོན་གྱི་ཕྱོགས་གཅིག་གཏན་ཚིགས་སུ་འགྱུར་རོ་ཞེ་ན།

[Block 357 [HEADING]]
### ཐ་དད་རྣམ་པར་གནས་པ། ^4-1-0

[Block 358 [VERSE]]
དེ་ནི་ཉེས་པ་མེད་དོ། །
[^221]གང་ཕྱིར་དངོས་ཀུན་རང་བཞིན་གྱིས། །
རང་རང་ངོ་བོ་ལ་གནས་ཕྱིར། །
མཐུན་དངོས་གཞན་གྱི་དངོས་དག་ལས། །

[Block 359 [VERSE]]
ལྡོག་པ་ལ་ནི་རྟེན་པ༌[^222]ཅན། །
དེ་ཕྱིར་གང་དང་གང་ལས་དོན། །
ལྡོག་པ་དེ་ཡི་རྒྱུ་ཅན་གྱི། །
རིགས་དབྱེ་དེ་ཡི་ཁྱད་པར་གྱིས། །

[Block 360 [VERSE]]
རྟོགས་འགྱུར་བ་དག་རབ་ཏུ་བྱེད། །
དེ་ཕྱིར་ཁྱད་པར་གང་ཞིག་ཆོས། །
གང་གིས་གོ་བར་འགྱུར་བ་དེ། །
དེ་ལས་གཞན་གྱིས་ནུས་མ་ཡིན། །
དེས་ན་ཐ་དད་རྣམ་པར་གནས། །

[Block 361]
དངོས་པོ་ཐམས་ཅད་ནི་རང་གི་ངོ་བོ་ལ་གནས་པ་ཅན་ཁོ་ན་ཡིན་ནོ། །

[Block 362]
དེ་དག་ནི་རང་དང་གཞན་དུ༌[^223]འདྲེ་བར་མི་བྱེད་དེ། དེ་གཞན་མ་ཡིན་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 363]
གང་ཡང་འདི་དག་གི་རང་བདག་ཉིད་དུ་གྱུར་པའི་ངོ་བོ་ཐ་མི་དད་པ་དེ་ནི་དེ་དག་གི་མ་ཡིན་ཏེ། དེའི་ཚེ་དེ་དག་མེད་པའི་ཕྱིར་རོ། །

[Block 364]
དེ་ཁོ་ན་ཡིན་པར་འགྱུར་ཏེ། ཐ་མི་དད་པ་ཡིན་པའི་ཕྱིར་དང་། དེ་ལས་མ་གཏོགས་པ་ཐ་དད་པ་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 365]
དེ་ཉིད་ཐ་དད་པར་ནི་འགལ་བའི་ཕྱིར་རོ། །

[Block 366]
དེ་ཡང་བདག་ཉིད་ལ་རྣམ་པར་གནས་པས་མ་འདྲེས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 367]
དོན་གཞན་ཡང་དུ་མ་དང་འབྲེལ་དུ་ཟིན་ཀྱང་དེ་ནི་དེ་དག་གི་སྤྱི་མ་ཡིན་ཏེ། དེའི་ངོ་བོ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 368]
གཉིས་ཉིད་ལ་སོགས་པ་དང་ལྡན་པ་དང་། འབྲས་བུའི་རྫས་དག་ལ་ཡང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 369]
འབྲེལ་པ་ཅན་གཞན་གྱིས་ཀྱང་གཞན་དག་མཚུངས་པ་ནི་མ་ཡིན་གྱི་དེ་དང་ལྡན་པ་དག་ཏུ་ནི་འགྱུར་ཏེ། འབྱུང་པོའི་མགུལ་ཆིངས་ལྟ་བུའོ། །ཤེས་པ་ཐ་མི་དད་པའི་ཡུལ་ཡང་མ་ཡིན་ཏེ། འབྱུང་པོ་བཞིན་ནོ། །

[Block 370]
[^224]བློ་ནི་དེ་དག་གི་བདག་ཉིད་ཁོ་ན་བསྲེ་ཞིང་སྤྱིའི་ཡུལ་ཅན་དུ་སྣང་གི་གཅིག་དང་འབྲེལ་པ་ཅན་དག་གོ་ཞེས་བྱ་བ་ནི་མ་ཡིན་ཏེ། འབྱུང་པོ་ལྟ་བུའོ། །

[Block 371]
གལ་ཏེ་དེ་ནི་དེ་མཐོང་བའི་འཁྲུལ་པ་ཡིན་ནོ་ཞེ་ན།

[Block 372]
དེ་མཐོང་ངོ་ཞེས་བྱ་བ་གང༌[^225]ལས།

[Block 373]
གལ་ཏེ་འཁྲུལ་པ་ས་བོན་མེད་པ༌[^226]ཅན་མི་རུང་བའི་ཕྱིར་རོ་ཞེ་ན། འབྲས་བུ་དེ་གཅིག་པ་ཅན་དེ་དག་ཁོ་ན་ས་བོན་ཡིན་ནོ། །

[Block 374]
གྲངས་དང་ལྡན་པ་དང་། འབྲས་བུའི་རྗེས༌[^227]ལ་སོགས་པ་དང་ལྡན་པ་དག༌[^228]དང་། འབྱུང་པོ་ལ་སོགས་པ་ལ་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 375]
དེ་བས་ན་དེ་ལྟར་སྤྱིའི་བློ་ལ༌[^229]ཞེན་པ་མེད་པའི་ཕྱིར་སྤྱི་ནི་གཞན་མ་ཡིན་ནོ། །

[Block 376]
ཡོད་དུ་ཆུག་ན་ཡང་དེ་ཡང་རང་གི་བདག་ཉིད་ལ་རྣམ་པར་གནས་པའི་ཕྱིར་གཞན་དང་མ་འདྲེས་པ་ཡིན་ནོ། །

[Block 377]
དེ་ལྟ་བས་ན་དངོས་པོ་འདི་དག་ནི་རིགས་མི༌[^230]མཐུན་པར་འདོད་པ་དང་གཞན་ལས་ལོག་པ་ཡིན་ཏེ། རང་གི་ངོ་བོས་ངོ་བོ་གཅིག་པའི་ཕྱིར་རོ། །

[Block 378]
གང་དང་གང་ལས་ཐ་དད་པ་དེའི་དབྱེ་བ་ཤེས་པར་བྱ་བའི་ཕྱིར། ཐ་སྙད་དུ་བྱས་པའི་སྒྲ་དག་གིས་དེ་དང་དེ་ལས་ཐ་དད་པ་རྒྱུར་བྱས་ནས་ངོ་བོ་ཉིད་ཐ་མི་དད་ཀྱང་ཆོས་དུ་མ་ཤེས་པར་བྱེད་དོ། །

[Block 379]
སྒྲ་དེ་དག་ཀྱང་ཐ་དད་པ་ཐམས་ཅད་མི་འཕེན་ཡང་ཐ་དད་པ་གཅིག་བརྗོད་པས་དེའི་རང་གི་མཚན་ཉིད་དཔྱིས་ཕྱིན་པ་ཁོ་ནར་འགྱུར་ཏེ། དེ་གཅིག་དང་ཡང་དེ་ཐ་དད་པ་ཡང་བས༌[^231]སོ། །

[Block 380]
དེ་ལྟ་བས་ན༌[^232]དངོས་པོ་གཅིག་ལ་གཞན་གྱི་ངོ་བོ་ཇི་སྙེད་པ་དེ་ལ་ལྟོས་ནས་ལྡོག་པ་དེ་སྙེད་ཡོད་དེ། དེ་ལ་མེད་པའི་རྒྱུ་དང་འབྲས་བུ༌[^233]ཅན་ནི་དེ་ལས་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 381]
ལྡོག་པ་ཇི་སྙེད་པ་དེའི་རྒྱུ་དང་འབྲས་བུ་ཅན་མ་ཡིན་པ་ཡོངས་སུ་སྤང་བར༌[^234]ཐ་སྙད་ཀྱི་དོན་ཅན་གྱི་སྒྲ་དག་ཀྱང་དེ་སྙེད་དེ། དཔེར་ན་སྒྲ་ནི་སྩལ༌[^235]མ་ཐག་ཏུ་འབྱུང་བ་ཅན་དང་ཉན་པ་ཅན་ཡིན་ནོ་ཞེས་བྱ་བ་དེའི་རྒྱུ་དང་འབྲས་བུ་ཅན་མ་ཡིན་པ་ཡོངས་སུ་སྤང་བའི༌[^236]དོན་ཡིན་པ་ལྟ་བུའོ། །

[Block 382]
དེའི་ཕྱིར་ངོ་བོ་ཉིད་ཐ་མི་དད་ཀྱིས་ཀྱང་ཁྱད་པར་གྱི་བྱེ་བྲག་གང་ཞིག་མིང་གི་ཆོས་གང་གིས་གོ་བར་འགྱུར་བ་དེ་ནི་གཞན་གྱིས་གོ་བར་མི་ནུས་པས་སྒྲ་ཐམས་ཅད་ནི་དོན་གཅིག་པ་མ་ཡིན་ནོ། །

[Block 383]
དེ་བས་ན་དམ་བཅས་པའི༌[^237]དོན་གྱི་ཕྱོགས་གཅིག་གཏན་ཚིགས་མ་ཡིན་ནོ། །

[Block 384]
ཡང་སྒྲ་དང་རྟགས་དག་གིས་རྣམ་པར་བཅད་པ་རྟོགས་པར་བྱེད་ཀྱི། བསྒྲུབས་པས༌[^238]དངོས་པོའི་རང་གི་ངོ་བོ་ཁོ་ན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཇི་ལྟར་ཤེས་ཤེ་ན། ཚད་མ་གཞན་དང་སྒྲ་གཞན༌[^239]འཇུག་པའི་ཕྱིར་ཏེ། འདི་ལྟར།

[Block 385 [VERSE]]
དོན་གྱི་རང་གི་ངོ་བོ་གཅིག །
བདག་ཉིད་མངོན་སུམ་ཡིན་པ་ལ། །
ཚད་མ་རྣམས་ཀྱིས་བརྟག་བྱ་གང་། །
མ་མཐོང་ཆ་གཞན་ཅི་ཞིག་ཡོད། །

[Block 386]
དོན་གྱི་བདག་ཉིད་གཅིག་པ་དེ་ནི་མངོན་སུམ་པ་ཡིན་ཏེ། ཆོས་ཅན་མ་གྲུབ་ན་སྒྲུབ་པ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 387]
དཔེར་ན་མི་རྟག་པ་བསྒྲུབ་པར་བྱ་བ་ལ་སྒྲ་ལྟ་བུ་སྟེ། དེའི་མངོན་སུམ་ཁོ་ནས་གྲུབ་པས་རྣམ་པ་ཐམས་ཅད་འགྲུབ་སྟེ། དེ་ལས་གཞན་པ་མ་གྲུབ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 388]
འོན་ཏེ་ཡོད་ན་ནི་དེའི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ། །

[Block 389]
གང་ཞིག་གང་དང་གྲུབ་པ་དང་བདེ་བ་གཅིག་པ་ཅན་མ་ཡིན་པ་དེ་ནི་དེའི་ངོ་བོ་ཉིད་ཡིན་པར་རིགས་པ་མ་ཡིན་ཏེ། ཐ་དད་པའི་ཐ་སྙད་ཀྱི་རྒྱུ་ནི་དེ་ཙམ་དུ་ཟད་པའི་ཕྱིར་རོ། །

[Block 390]
དེ་ལྟ་མ་ཡིན་ན་མེད་པར་ཐལ་བར་འགྱུར་རོ་ཞེས་བཤད་ཟིན་ཏོ། །
--- END BLOCKS ---
