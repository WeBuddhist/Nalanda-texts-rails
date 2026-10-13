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
དེ་ལ་རྒྱུ་ནི་འདས་པ་དང་ད་ལྟར་དང་མ་འོངས་པ་ཉིད་ཀྱིས་ན་དུས་གསུམ་ལ་འབྲས་བུ་ཡང་དུས་གསུམ་མོ། །

[Block 422]
འབྲས་བུ་རེ་རེ་ལ་ཡང་དུས་གསུམ་དུ་ཡང་རྒྱུ་མི་སྲིད་དོ།[^348] །ཇི་ལྟར་བསྟན་པའི་རིགས་པས་ཞེས་གསུངས་པ། དུས་གསུམ་རྣམས་སུ་འཐད་མ་ཡིན། །ཞེས་བྱའོ། །

[Block 423]
དེ་སྐད་དུ་ཡང་རྩ་བའི་རབ་བྱེད་ཉི་ཤུ་པར།

[Block 424 [VERSE]]
འདས་པའི་འབྲས་བུ་འདས་པ་ཡི། །
རྒྱུ་དང་ལྷན་ཅིག་མ་ཡིན་ལ། །
མ་སྐྱེས་པ་དང་མ་སྐྱེས་པ། །
ནམ་ཡང་ལྷན་ཅིག་ཡོད་མ་ཡིན། །

[Block 425 [VERSE]]
མ་སྐྱེས་པ་ཡི་འབྲས་བུ་དང་། །
མ་སྐྱེས་རྒྱུ་དག་ལྷན་ཅིག་མིན། །
འདས་པ་དང་ནི་མ་སྐྱེས་པ། །
ནམ་ཡང་ལྷན་ཅིག་ཡོད་མ་ཡིན། །

[Block 426 [VERSE]]
མ་སྐྱེས་པ་ཡི་འབྲས་བུ་དང་། །
སྐྱེས་པའི་རྒྱུ་དག་ལྷན་ཅིག་མིན། །
མ་སྐྱེས་པ་དང་མ་འགགས་པ། །
ལྷན་ཅིག་ནམ་ཡང་མ་ཡིན་ནོ། །

[Block 427]
ཞེས་གང་གི་ཆོས་འདི་ལྟར་དཔྱད་ན་རྒྱུ་མི་སྲིད་པ་དེའི་ཚེ་རྒྱུ་མེད་ན། དེས་བསྐྱེད་བྱ་འབྲས་བུ་མེད་ལ། བསྐྱེད་བྱ་འབྲས་བུ་མེད་པས་སྐྱེ་བ་མེད༌[^349]པ་གྲུབ་བོ་ཞེས་བྱའོ། །

[Block 428]
འདིར་སྨྲས་པ། རྒྱུའི་གྲངས་ཉེ་བར་བསྟན་པ་ཡོད་པའི་ཕྱིར་ཡོད་པ་ཉིད་དེ། ཡོད་པ་མ་ཡིན་པའི་རུས་སྦལ་གྱི་སྤུ་ལ་གྲངས་ཉེ་བར་སྟོན་པ་མ་ཡིན་ལ་རྒྱུའི་གྲངས་ཉེ་བར་བསྟན་པའི་ཕྱིར།

[Block 429 [VERSE]]
བྱེད་རྒྱུ་ལྷན་ཅིག་འབྱུང་བ་དང་། །
སྐལ་མཉམ་མཚུངས་པར་ལྡན་པ་དང་། །
ཀུན་དུ་འགྲོ་དང་རྣམ་སྨིན་རྒྱུ། །
རྒྱུ་ནི་རྣམ་པ་དྲུག་ཏུ་འདོད། །

[Block 430]
ཅེས་ཆོས་མངོན་པ་ལས་སོ། །

[Block 431]
མདོ་ལས་ཀྱང་གསུངས་པ། ཆོས་གཅིག་ནི་ཁྱད་པར་གྱི་སྐལ་བ་ཅན་ཏེ། གང་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པའོ། །

[Block 432]
རྒྱུ་དང་རྐྱེན་གཉིས་ཀྱིས་ཡང་དག་པའི་ལྟ་བ་བསྐྱེད་པ་སྟེ། ནང་གི་བདག་ཉིད་ཀྱིས༌[^350]ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་དང་། གཞན་ལས་རྗེས་སུ་མཐུན་པའི་སྒྲའོ། །

[Block 433]
ཆོས་གསུམ་ནི་མང་པོ་བྱེད་པ་སྟེ། སྐྱེས་བུ་དམ་པ་བསྟེན་པ་དང་། དམ་པའི་ཆོས་ཉན་པ་དང་། ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པའོ་ཞེས་སོ། །

[Block 434]
སྨྲས་པ། གལ་ཏེ་རྒྱུ་ཡོད་ན། དེའི་གྲངས་ཡོད་པ་ཉིད་ལ། ཡོད་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་མེད་པ་དེ་ལྟར་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 435 [HEADING]]
### ཚིགས་བཅད་བདུན་པ། ^1-7-0

[Block 436 [VERSE]]
གཅིག་མེད་པར་ནི་མང་པོ་དང་། །
མང་པོ་མེད་པར་གཅིག་མི་འཇུག །
དེ་ཕྱིར་རྟེན་ཅིང་འབྲེལ་འབྱུང་བའི། །
དངོས་པོ་མཚན་མ་མེད་པ་ཡིན། །

[Block 437]
འདིར་ཐ་དད་པ་རྣམས་སུ་བགྲང་བའི་བརྡ་ལ་འཇིག་རྟེན་དུ་གྲངས་ཞེས་རྣམ་པར་འཇོག་སྟེ། ཐ་དད་པ་འདི་རྣམས་བགྲང་བར་བྱེད་རྩི་བར༌[^351]བྱེད་དོ་ཞེས་བྱས་ནས་གྲངས་དེ་ཡང་གཅིག་དང་གཉིས་དང་མང་པོ་ལ་སོགས་པས་སོ།[^352] །དེ་ལ་གང་འདིའི་གཅིག་གི་གྲངས་ལས་བགྲང་བྱ་གཅིག་ཏུ་རྣམ་པར་འཇོག་ལ། དེ་བཞིན་དུ་གཉིས་ཀྱི་གྲངས་ཀྱིས་གཉིས་ཀྱི་དངོས་པོ་ལ། མང་པོའི་གྲངས་ཀྱིས་མང་པོའི་དངོས་པོའོ། །

[Block 438]
དེ་ལ་གང་ཞིག་གཅིག་མང་པོའི་དངོས་པོ་ལ་མི་ལྟོས་པར་འགའ་ཞིག་གྲུབ་པར་འགྱུར་ན་གཅིག་གི་གྲངས་སུ་འགྱུར་ལ། མང་པོ་ལ་མ་ལྟོས་པར་གཅིག་གི་དངོས་པོའི་རང་གི་ངོ་བོ་གྲུབ་པ་མེད་དོ། །

[Block 439]
དེ་ལ་གང་རེ་ཞིག་བདག་ཉིད་དང་བཅོ་ལྔའི་ཆོས་སྐྱེ་བ་དེ་རྣམས་ཆོས་བཅོ་ལྔ་ལ་མ་ལྟོས་པའི་གཅིག་གི་ཆོས་ནི་མེད་དོ། །

[Block 440]
གཞན་ཡང་གལ་ཏེ་འདིའི་གཟུགས་ཅན་གྱི་དངོས་པོ་གཅིག་འདོད་ན། དེ་འདོད་པའི་ཁམས་སུ་རྫས་བརྒྱད་ཀྱི་བདག་ཉིད་ལ། དབང་པོ་ལས་འདས་པའི་ཕྱིར་ཞེས་པའི་ངེས་པ་ལས་སྒྲའི་རྡུལ་ཕྲ་རབ་ནི་མ་ཡིན་ནོ། །

[Block 441]
རྫས་བདུན་ལ་མ་ལྟོས་པར་རང་གི་ངོ་བོ་གྲུབ་པ་མེད་དོ། །

[Block 442]
ཡང་ན་གལ་ཏེ་གཟུགས་ཁམས་སུ་སེམས་དང་སེམས་ལས་བྱུང་བའི་རང་བཞིན་ལ། [^353]སེམས་དང་སེམས་བྱུང་ངེས་ལྷན་ཅིག །ཞེས་པའི་ངེས་པ་ལས་ཐམས་ཅད་བསྡུས་ན་རྫས་བཅུ་གཅིག་གི་བདག་ཉིད་ལ་ལྟོས་སོ། །

[Block 443]
ཡང་ན་ལྡན་པ་མ་ཡིན་པ་རྣམས་ཀྱི་སྟེ། དེ་ལ་ཡང་།

[Block 444]
[^354] དེ་དག་སྐྱེ་བའི་སྐྱེ་ལ་སོགས། །དེ་ཆོས་བརྒྱད་དང་གཅིག་ལ་འཇུག །ཅེས་པའི་ངེས་པ་ལས་དེ་དེ་ལྟར་མང་པོ་ལ་ལྟོས་པར་དངོས་པོ་གཅིག་མེད་ལ། གང་གི་ཚེ་འདི་ལྟར་མང་པོ་ལ་མ་ལྟོས་པར་དངོས་པོ་གཅིག་མེད་པ་དེའི་ཚེ། དངོས་པོ་གཅིག་པུ་འགྲུབ་པར་མི་འགྱུར་ན། གཅིག་བསགས་པ་ག་ལ་ཞིག །གཅིག་བསགས་པ་མེད་ན་མང་པོ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། མང་པོ་ཡང་མེད་དོ། །

[Block 445]
ཇི་སྐད་དུ་འཕགས་པ་ལས།

[Block 446 [VERSE]]
[^355] དངོས་པོ་གང་གང་རྣམ་བརྟགས་ན། །
དེ་དང་དེ་ལ་གཅིག་མེད་ལ། །
གང་དུ་གཅིག་ཀྱང་མེད་པ་ན། །
གང༌[^356]དུ་མ་འོངས༌[^357]ཡོད་མ་ཡིན། །

[Block 447]
ཞེས་སོ། །

[Block 448]
གང་གི་ཚེ་དེ་ལྟར་དངོས་པོ་མང་པོ་ལ་མ་ལྟོས་པར་དངོས་པོ་གཅིག་མེད་པ་དེའི་ཚེ། དངོས་པོ་གཅིག་མེད་པ་ལ་མང་པོ་འཐད་པ་མ་ཡིན་ནོ། །

[Block 449]
གང་གི་ཚེ་ཡང་དངོས་པོ་གཅིག་མེད་པར་གྱུར་ན་མང་པོ་མི་འཐད་པ་དེའི་ཚེ་མང་པོ་མེད་པས་དེ་དང་འབྲེལ་པ་ལས་བྱུང་བའི་གཅིག་ཀྱང་མེད་དོ་ཞེས་གསུངས་པ། མང་པོ་མེད་པར་གཅིག་མི་འཇུག །ཅེས་བྱ་བ་ལ། མང་པོ་མེད་ན་གཅིག་མི་སྲིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 450]
གང་དུ་གཅིག་ལ་གཅིག་གམ་མང་པོའི་དངོས་པོ་མེད་པ་དེ་ལ་གཅིག་གི་གྲངས་སམ་མང་པོ་ཉིད་ཀྱི་གྲངས་ག་ལ་འཇུག་བྱ་བ་སྟེ། དེས་ན་གྲངས་མེད་ལ། གྲངས་མེད་ན་ཡང་གྲངས་སྲིད་པའི་རྒྱུ་མཚན་གྱིས་གྲུབ་པའི་རྒྱུ་མི་འགྲུབ་བོ། །

[Block 451]
འདིར་སྨྲས་པ། གལ་ཏེ་གཅིག་མེད་ན་དེ་ལ་གཅིག་གི་ཐ་སྙད་མི་འབྱུང་ན། བུམ་པ་གཅིག་ཅེས་པ་དང་། གལ་ཏེ་མང་པོ་མེད་ན་དེའི་ཚེ་མང་པོའི་ཐ་སྙད་མེད་པར་འགྱུར་ན། བུམ་པ་མང་པོ་ཞེས་སོ། །

[Block 452]
སྨྲས་པ། སུ་ཞིག་དེ་སྐད་སྨྲ། གཅིག་མེད་ཅིང་མང་པོ་མེད་དོ་ཞེས་བྱ་བ། ཁོ་བོས་གཅིག་དང་མང་པོའི་དངོས་པོའི་ངོ་བོ་གྲུབ་པ་བཀག་ལ། གང་ལས་དེ་རྣམས་ཀྱི་རང་གི་ངོ་བོ་གྲུབ་པ་མེད་པ།

[Block 453 [VERSE]]
དེ་ཕྱིར་རྟེན་ཅིང་འབྲེལ་འབྱུང་བའི། །
དངོས་པོ་མཚན་མ་མེད་པ་ཡིན། །

[Block 454]
གང་ཁོ་ན་དེ་རྣམས་ཀྱི་ངོ་བོ་མ་གྲུབ་པ་དེ་ཉིད་ཀྱིས་ན་དངོས་པོ་རྣམས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བར་འགྱུར་རོ། །

[Block 455]
རང་བཞིན་ཡོད་པ་རྣམས་སྐྱེ་བ་དོན་མེད་པའི་ཕྱིར། རང་བཞིན་མ་གྲུབ་པའི་གཟུགས་བརྙན་ལ་སོགས་པ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཉེ་བར་ཐོབ་ལ། དེ་ཉིད་ཀྱིས་ན་ཆོས་ཐམས་ཅད་མཚན་མ་མེད་པ་དང་ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་སྟོང་པར་གྲུབ་པའམ།[^358] རང་བཞིན་མེད་པས་ཕན་ཚུན་དུ་བྱེ་བྲག་ཡོངས་སུ་མ་བརྟགས་པས་མཚན་མ་མེད་པ་སྟེ། དངོས་པོ་ཐམས་ཅད་བྱེ་བྲག་མེད་པས༌[^359]གཅིག་གི་རང་བཞིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 456]
རྣམ་པར་ཤེས་པའི་ཡུལ་མ་ཡིན་པའི་ཕྱིར་ཡང་མཚན་མ་མེད་པ་སྟེ། རྣམ་པར་ཤེས་པ་ནི་མཚན་མ་ལ་དམིགས་པའི་ཕྱིར་ན། རྣམ་པར་ཤེས་པའི་དམིགས་པ་གཞན་ལས་ཁྱད་པར་འགའ་ཞིག་གིས་ཁྱད་པར་དུ་གྱུར་པའི་རང་གི་དམིགས་པ་ལ༌[^360]འཇུག་བཞིན་པས་འཇུག་པར་འགྱུར༌[^361]གྲང་ན། དེ་ཡང་ཁྱད་པར་གྱི་དམིགས་པའི་རང་བཞིན་མེད་པས་མེད་དོ་ཞེས་བྱ་སྟེ། འདི་ཉིད་ཀྱིས་ན་རྣམ་པར་ཤེས་པའི་ཡུལ་མ་ཡིན་པས་དངོས་པོ་མཚན་མ་མེད་པའོ་ཞེས་བྱའོ། །

[Block 457]
གཞན་དག་ནི་གཞན་དུའང་སྨྲ་སྟེ། འདིར་ངེས་པར་ཐ་སྙད་ཀྱི་དོན་དུ་དོན་ལ་མིང༌[^362]དག་འཇུག་ལ། དེ་རྣམས་ཀྱང་ཕན་ཚུན་དུ་རང་ལས་གཞན་པའི་མིང༌[^363]རྣམ་པར་གཅད་པའི༌[^364]སྒོ་ནས་རང་གིས༌[^365]རྟོགས་པར་བྱེད་ལ། མང་པོ་ཡོད་ཀྱང་དེ་དག་རྣམ་པར་གཅད་པའི༌[^366]དོན་དུ་གཅིག་ཅེས་བྱ་བའི་ཚིག་འཐད་ལ། དེ་ཡང་གཞན་མེད་ན་འདིས་ཅི་ཞིག་རྣམ་པར་གཅད་པར༌[^367]བྱ་ཞེས་བྱ་སྟེ། སྦྱོར་བར༌[^368]མི་བྱེད་པར་ཐལ་ལོ། །

[Block 458]
མིང་གི་རང་བཞིན་ལས་གཞན་པའི་གཅིག་གི་གྲངས་འགའ་ཞིག་ཡོད་པ་མ་ཡིན་ཏེ། དགྲ་དེ་ལས་མ་གྲོལ་ལོ་ཞེས་བྱ་བ་ལྟ་བུ་ལ་སོགས་པ་ཡུལ་གཞན་དུ་བརྗོད་པའི་ཐ་སྙད་ལས་དེ་དག་འདི་ལྟར་མང་པོ་དང༌[^369]འབྲེལ་པ་དང་མང་པོའི༌[^370]རྒྱུ་མཚན་གྱིས་མང་པོ་ལས་གཞན་དུ༌[^371]གཅིག་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ༌[^372]ལ། གཞན་ལ་རག་ལས་པས་རང་བརྒྱུད༌[^373]པ་མ་ཡིན་ལ། རང་བརྒྱུད༌[^374]པ་མ་ཡིན་པའི་ཕྱིར་ཡོངས་སུ་མ་གྲུབ་པའོ། །

[Block 459]
དེ་བཞིན་དུ་གྲངས་ཅིག་ཤོས་ཀྱང་ཤེས་པར་བྱའོ། །

[Block 460]
གལ་ཏེ་དེ་ལྟར་གྲངས་མི་འཐད་ན་གཅིག་དང་གཉིས་དང་མང་པོ་ལ་སོགས་པའི་ཐ་སྙད་ཇི་ལྟར་འདོགས་ཤེ་ན།
--- END BLOCKS ---
