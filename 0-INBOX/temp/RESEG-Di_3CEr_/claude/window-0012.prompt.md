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
[Block 421]
རྗེས་སུ་དཔག་པར་བྱ་བ་ནི་ཆོས་ཀྱི༌[^345]ཁྱད་པར་དུ་བྱས་པའི་ཆོས་ཅན་ནོ། །

[Block 422]
དེ་ལ་མངོན་སུམ་མམ་རྗེས་སུ་དཔག་པས་མཐོང་གི༌[^346]རྗེས་ལ་དེའི་རིགས་དང་མཐུན་པ་ལ་ཡང་སྤྱིའི་ཚུལ་གྱིས་ཕྱོགས་ཐམས་ཅད་དམ་ཕྱོགས་གཅིག་ལ་ཡོད་པར་གྲུབ་པའོ། །

[Block 423]
[^347]ཅིའི་ཕྱིར་ཞེ་ན། དེ་དང་མཐུན་པ་ཁོ་ན་ལ་ཡོད་ཅེས་ངེས་པར་གཟུང་བའི་ཕྱིར་རོ། །

[Block 424]
དེ་དང་མཐུན་པ་ལ་ཡོད་པ་ཁོ་ནའོ་ཞེས་ནི་བརྗོད་པར་མི་བྱ་བའི་ཕྱིར་རོ། །

[Block 425]
མེད་པ་ཉིད་ལས་མེད་པ་ཞེས་པས་ནི་སླར་ཡང་དེ་ཉིད་ངེས་པར་བྱ་བའི་དོན་དུ་སྟེ། མེད་པ་ཉིད་ལ་མེད་པ་ཉིད་ཡིན་གྱི་གཞན་ལ་ཡང་མ་ཡིན་ལ་འགལ་བ་ལ་ཡང་མ་ཡིན་ནོ་ཞེས་པའི་དོན་ནོ། །

[Block 426]
བསྒྲུབ་པར་བྱ་བའི་རིགས་དང་མཐུན་པ་ལ་ཡོད་པ་དང་མེད་པ་ལ་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་དེ་དག་གིས་ནི་གང་ཚུལ་གསུམ་པའི་རྟགས་ལས་རྟགས་ཅན་རྟོགས་སོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 427]
ཅི་སྟེ་ཤེས༌[^348]པར་བྱ་བ་ཡིན་ནོ་ཞེ་ན་སྨོས་པར་བྱ་བ་མ་ཡིན་ཏེ་གང་གི་ཕྱིར། འདི་རུ་ཤེས་པའང་ཐོབ་པ་ཉིད། །མ་བརྗོད་པ་དེ་ཇི་ལྟར་ཐོབ༌[^349]ཅེ་ན། ཤེས་བྱེད་སྐབས་ཀྱིས༌[^350]དབང་བྱས་ཕྱིར། །འདིར་གཏན་ཚིགས་ནི་ཤེས་པར་བྱེད་པའི༌[^351]དབང་དུ་བྱས་པའི་ཕྱིར་དེ་ཡང་རྟོག་པ་པོ་རང་གི་བདག་ཉིད་ལ་ལྟོས་ནས་རྟོགས་པར་བྱེད་པའི་རྒྱུ་ཡིན་གྱི། བྱེད་པ་པོ་བཞིན་དུ་ལྟོས་པ་མ་ཡིན་པའི་ཕྱིར་ཚུལ་གསུམ་གྲུབ་ན་རྟགས་སུ་བརྗོད་པ་ཡིན་ནོ། །

[Block 428 [HEADING]]
#### ཚུལ་རེ་རེ་དང་གཉིས་གཉིས་པ། ^2-1-6-0

[Block 429]
ཚུལ་རེ་རེ་དང་གཉིས་གཉིས་པ། །རྟགས་དོན་མིན་པར་དོན་གྱིས་བྱས། །

[Block 430]
དེ་ལ་ཚུལ་རེ་རེ་བ་ནི་གང་རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་ཡོད་དོ།[^352] །

[Block 431]
དེ་དང་མཐུན་པ་ལ་ནི་མེད། །དེ་མེད་པ་ལ་ནི་མེད་པ༌[^353]མ་ཡིན་པ་དང་། དེ་དང་མཐུན་པ་ལ་ཡོད། རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་ནི་མེད། དེ་མེད་པ་ལ་ནི་སེམས༌[^354]མེད་པ་མ་ཡིན་པ་དང་། དེ་མེད་པ་ལ་མེད། རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་ཡང་མེད། དེ་དང་མཐུན་པ་ལ་ཡང་མེད་པའོ། །

[Block 432]
ཚུལ་གཉིས༌[^355]པ་ནི་འདི་ལྟར་རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་ཡོད། དེ་དང་མཐུན་པ་ལ་ཡང་ཡོད། དེ་མེད་པ་ལ་ཡང་མེད་པ་མ་ཡིན་པ་དང་། རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་ཡོད་དོ།[^356] །

[Block 433]
དེ་མེད་པ་ལ་མེད། དེ་དང་མཐུན་པ་ལ༌[^357]ཡང་ཡོད་པ་མ་ཡིན་པ་དང་། དེ་དང་མཐུན་པ་ལ་ཡོད། དེ་མེད་པ་ལ་མེད། རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་ཡང་མེད་པའོ་ཞེས་བྱ་བ་དེ་དག་གིས་ནི་རྟགས་ལྟར་སྣང་བ་རྣམ་པ་དྲུག་ཏུ་བསྒྲུབས་པར་དོན་གྱིས་གོ་བར་རིག་པར་བྱའོ། །

[Block 434]
དཔེར་ན།

[Block 435 [VERSE]]
སྒྲ་རྟག༌[^358]བྱས་པའི་ཕྱིར་ལུས་ཅན། །
ཕྱིར་དང་གཞལ་བྱ་མིན་ཕྱིར་རོ། །
ལུས་ཅན་མིན་ཕྱིར༌[^359]མཉན་བྱའི་ཕྱིར། །
མིག་གིས་གཟུང་བའི༌[^360]ཕྱིར་མི་རྟག །

[Block 436]
ཅེས་པ་ལྟ་བུའོ། །

[Block 437]
འདི་ལ།

[Block 438 [HEADING]]
#### ཆོས་གཞན་དང་འབྲེལ་པ་དཔག་བྱར་འདོད་པ། ^2-1-7-0

[Block 439 [HEADING]]
##### ཆོས་གཞན་དཔག་བྱར་འདོད་པ། ^2-1-7-1-0

[Block 440]
ཁ་ཅིག་གཏན་ཚིགས་མི་འཁྲུལ་པས། །ཆོས་གཞན་དཔག་པར་བྱ་བར་འདོད། །

[Block 441]
ཁ་ཅིག་ནི་གང་གི་ཕྱིར་མེ་དང་དུད་པ་ནི་ལྷན་ཅིག་རྒྱུ་བ་མཐོང་གི་མེ་དང་ལྷན་ཅིག་པའི་ས་ཕྱོགས་དང་ནི་མ་ཡིན་ནོ། །

[Block 442]
དེའི་ཕྱིར་མེ་ཁོ་ན་དུད་པས་རྗེས་སུ་དཔག་པར་བྱ་བའོ་ཞེས་ཟེར་རོ། །

[Block 443 [HEADING]]
##### འབྲེལ་པ་དཔག་བྱར་འདོད་པ། ^2-1-7-2-0

[Block 444 [VERSE]]
ཆོས་དང་ཆོས་ཅན་དག་གྲུབ་ཕྱིར། །
འབྲེལ་པ་དཔག་བྱར་ཁ་ཅིག་འདོད། །

[Block 445]
གཞན་དག་ན་རེ་གང་གི་ཕྱིར་མེ་དང་ས་ཕྱོགས་དག་ནི་འཇིག་རྟེན་པ་ལ༌[^361]གྲུབ་པ་ཉིད་དེ། དེའི་ཕྱིར་མེ་དང་ས་ཕྱོགས་དག་ནི་མ་ཡིན་གྱི་འབྲེལ་པ་དེ་དུད་པས་རྗེས་སུ་དཔག་པར་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 446 [HEADING]]
##### སྔ་མ་ལ་ལན་བརྗོད་པ། ^2-1-7-3-0

[Block 447]
རེ་ཞིག་དེ་སྔ་མ་ལ་ལན་བརྗོད་པ། །

[Block 448]
ཆོས་ལ་གཏན་ཚིགས༌[^362]གྲུབ་ན་ནི། །དེ་ཡིས་དེ་ལས༌[^363]གཞན་ཅི་དཔག །

[Block 449]
གལ་ཏེ་ཆོས་གཞན་མེ་ལ་གཏན་ཚིགས་དུད་པ་དམིགས་པ་ཉིད་ཡིན་པ་ལྟ་ན་ཡང་དུད་པས་ཅི་ཞིག་རྗེས་སུ་དཔག་པར་བྱ། དོན་གང་མེ་དང་དུད་པ་དག་གིས་འབྲེལ་བ༌[^364]དྲན་པར་བྱེད་དོ་ཞེ་ན།

[Block 450]
དེ་ལྟར་ཆོས་ཅན་དེ་ཉིད་ལ། །དཔག་བྱར༌[^365]ཅི་ཡི་ཕྱིར་མི་འདོད། །

[Block 451]
གལ་ཏེ་མེ་དང་འབྲེལ་པའི་ས་ཕྱོགས་སུ་དུད་པ་དམིགས་པ་ལས་མེ༌[^366]རྗེས་སུ་དཔག་པར་བྱ་བ༌[^367]ལྟ་ན་མེ་དང་ལྡན་པའི་ས་ཕྱོགས་དེ་ཉིད་རྗེས་སུ་དཔག་པར་བྱའོ་ཞེས་ཅིའི་ཕྱིར་མི་འདོད། དེར་མེ་ཡོད་པར་མི་རྟོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 452 [HEADING]]
##### འབྲེལ་པ་དཔག་བྱར་ཟེར་བ་ལ་བརྗོད་པ། ^2-1-7-4-0

[Block 453]
གང་དག་འབྲེལ་པ་དཔག་པར་བྱའོ་ཞེས་ཟེར་བ་དེ་ལ་བརྗོད་པ་དང་། [^368]འབྲེལ་པའང༌[^369]གཉིས་ནི་ཡོད་མ་ཡིན། །གང་ན་དུད་པ་ཡོད་པ་དེ་ན༌[^370]མེ་ཡོད་དོ་ཞེས་འདི་ལྟར་ཐ་སྙད་བྱེད༌[^371]ཀྱི་མེའམ་དུད་པའི་འབྲེལ་བ་ལ་སོགས༌[^372]པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 454]
གཞན་ཡང་། དེ་བཞིན་དྲུག་པའི་སྒྲ་རུ་འགྱུར། །འབྲེལ་པ་རྗེས་སུ་དཔག་པར་བྱ་བ༌[^373]བྱེད་པའི་ལྟ་ན་འབྲེལ་པ་ཅན་གྱི་མེས་མེ་འདི་འབྲེལ་པ་ཞེས་དྲུག་པའི་སྒྲ་ཐོབ་པར་འགྱུར་གྱི། འདི་ན་ནི་མེའོ་ཞེས་ནི་མ་ཡིན་ནོ། །

[Block 455]
གང་གི་ཕྱིར་འབྲེལ་པ་ནི་མེ་འདི་ལའོ་ཞེས་དང་པོའི་སྒྲས་བརྗོད་དོ། །

[Block 456]
རང་གི་ཆོས་ཀྱི་འབྲེལ་པར་ནི། །བརྗོད་པར་མི་བྱའོ། །

[Block 457]
གཞན་མ་བརྗོད་པ་ནི་དེ་ལྟར་རྗེས་སུ་དཔག་པར་བྱ་བ་མ་ཡིན་ཏེ། འོན་ཀྱང་། དོན་སྨོས་ཕྱིར། མེ་འདི་ལ་ཞེས་སྨྲས་པའི་དོན་དང་འབྲེལ་པར་བརྗོད་པར་འགྱུར་བའི་ཡིན་ནོ་ཞེ་ན། སྔར་བརྗོད་པའི་འཐད་པས་དེ་ནི་དུད་པས་རྗེས་སུ་དཔག་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར། །གཏན་ཚིགས་འདི་དང་འབྲེལ་པ་མིན། །གང་གི་ཕྱིར་དུད་པ་ལས་མ་གཏོགས་པ༌[^374]མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་ཉིད་ནི་བསྟན་པར་བྱ་བ་མ་ཡིན་ཏེ། འདི་ལྟར་མེ་ཉིད་ལའོ། །

[Block 458]
ཉེས་པ་དེ་དག་ནི་མེད་དེ། གང་གི་ཕྱིར་མེ་དུད་པ་དང་ལྡན་པའི་ས་ཕྱོགས་དང་མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་བསྟན་པར་བྱ་བ་མ་ཡིན་ཡང་དེ་རྗེས་སུ་དཔག་བྱར་བྱེད་པ་དེ་བཞིན་དུ་འབྲེལ་བ་ལ་ཡང་འགྱུར་རོ་ཞེ་ན། རྣམ་གཞག་དེ་ནི་སྤང་བ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 459 [VERSE]]
རྟགས་ཀྱི་འཁྲུལ་བ་མེད་པ་ནི། །
ཆོས་ལས་གཞན་དུ་སྟོན་པར་བྱེད། །
དེར་གྲུབ་དེ་དང་ལྡན་པ་ཡི། །
ཆོས་ཅན་གོ་བར་བྱ་བ་ཡིན། །

[Block 460]
གང་མེ་དང་དུད་པ་མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་དེ་གཞན་དུ་བསྟན་པར་བྱས་ནས་ཡུལ་གཞན་དུ་དུད་པ་དེ་འབའ་ཞིག་ཙམ་མཐོང་ཡང་གང་ན་དུད་པ་ཡོད་པ་དེ་ན་མེ་ཡོད་དོ།[^375] །
--- END BLOCKS ---
