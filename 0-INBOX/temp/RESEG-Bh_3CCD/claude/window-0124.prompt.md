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
[Block 4341]
ཅེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ། ལས་ལས་འཇིག་རྟེན་སྣ་ཚོགས་སྐྱེ། །[^2651]ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4342 [VERSE]]
ང་རྒྱལ་ལས་ནི་རབ་སྐྱེས་པ། །
བདག་གི་བྱེད་པས་འཕེལ་འགྱུར་ཏེ། །
འགྲོ་ལ༌[^2652]ཕན་པ་ངེས༌[^2653]སྨྲས་པས། །
སྐྱེ་དགུ་མ་ལུས་འདི་དག་གསུངས།[^2654] །

[Block 4343]
ཞེས་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་སྔ་ནས་ཀྱིས་ཀྱང་བསྟན་ཏོ། །

[Block 4344]
དེ་བས་ལྷ་གཞན་མེད་དོ། །

[Block 4345]
དེ་བཞིན་དུ་སྐལ་བ༌[^2655]ཞེས་བྱ་བ་ནི་གང་གི༌[^2656]དབང་གིས་འཇིག་རྟེན་པ་བདེ་བ་དང་ལྡན་པར་འགྱུར་བ་དང་དེ་མེད་པས་སྡུག་བསྔལ་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 4346]
ཚད་མས་གནོད་པར་བྱ་བའི་ཕྱིར་དེ་རྣམས་ནི་མེད་དོ། །

[Block 4347]
གལ་ཏེ་དེ་ལྟ་ཡིན་ན་ཕ་རོལ་གྱི་བསྟན་པས་གྲུབ་པའི་བདག་ལ་སོགས་པ་མེད་དོ། །

[Block 4348]
དེ་རྣམས་ཀྱང་ལས་ཀྱི༌[^2657]རྣམ་གྲངས་ཡིན་པས་དེའི་མཚན་ཉིད་ནི་ལོགས་སུ་མེད་དོ། །

[Block 4349]
དེ་བཞིན་དུ༌[^2658]བསོད་ནམས་ཀྱང་འགག་པར་བྱ་བ་ཡིན་ནོ། །

[Block 4350]
གཤིན་རྗེ་མཐར་བྱེད་དག་ཀྱང་ངེས་པ་བཞིན་དུ་བཤད་པར་བྱའོ། །

[Block 4351]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་རྣམས་ནི་སྔར་བྱས་པའི་རང་གི་སེམས་ཀྱི་ཆོས་ཀྱི་བག་ཆགས་ཀྱི་ངོ་བོའི་ལས་ལ་མིང་གི་རྣམ་གྲངས་ཡིན་ནོ་ཞེས་དོན་གཞན་མེད་དོ། །

[Block 4352]
དེ་ལྟར་གཞན་གྱིས་ཡོངས་སུ་བརྟགས་པའི་བདག་ལ་སོགས་པ་དེ་རྣམས་སྣོད་དུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 4353]
དངོས་པོ་ཐམས་ཅད་བྲལ་བ་དང་། །ཞེས་པ་ནི་ཚད་མས་གནོད་པའི་ཕྱིར་རོ། །

[Block 4354]
རྒྱུ་དང་འབྲས་བུའི་ངོ་བོ་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་གི་བདེན་པ་དག་ཡོད་དེ། སྡུག་བསྔལ་བའི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔའོ། །

[Block 4355]
དེ་ལ་གཟུགས་ཀྱི་ཕུང་པོའི་ཕྱོགས་གཅིག་གིས་བཟུང༌[^2659]བའི་ལུས་ཀྱི་དབང་པོ་འབྱུང་བ་ཆེན་པོ་བཞིའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་ཁམས་བཞི་ནི་མངོན་སུམ་གྱིས༌[^2660]གྲུབ་བོ། །

[Block 4356]
དེ་བཞིན་དུ་གཟུགས་ལ་སོགས་པའི་ཡུལ་རྣམས་ཀྱང་དེའི་ཕྱོགས་གཅིག་ཉིད་ཀྱིས་འགྲུབ་བོ། །

[Block 4357]
དབང་པོ་དང་ཡུལ་ཕྲད་པ་ལས་སྐྱེས་པའི་མིག་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་ཀྱང་མངོན་སུམ་གྱི་སྤྱོད་ཡུལ་ཡིན་ནོ། །

[Block 4358]
རྟེན་དང་བརྟེན་པ་དང་དམིགས་པ་དྲུག་རྣམ་པར་གཞག་པའི༌[^2661]ཕྱིར་ཁམས་བཅོ་བརྒྱད་ནི་མངོན་སུམ་དང་རྗེས་སུ་དཔག་པའི་ཚད་མས་གྲུབ་བོ། །

[Block 4359]
ཀུན་འབྱུང༌[^2662]གི་བདེན་པ་ཡང་མ་རིག་པ་དང་སྲེད་པའི་རང་བཞིན་འབྲས་བུར་གྱུར་པའི་སྡུག་བསྔལ་གྱི་བདེན་པ་མཐོང་བས་རྟོགས༌[^2663]པར་བྱ་སྟེ། དུ་བ་ལས་མེ་བཞིན་ནོ། །

[Block 4360]
དེ་བས་ན་ཕུང་པོ་ལ་སོགས་པ་ཡོད་དེ། དེ་རྣམས་སྤང་བར་བྱ་བའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་འགོག་པ་དང་ལམ་གྱི་བདེན་པ་གཉིས་གསུངས་ཏེ་ཞེས་སྨྲ་བ་ལ་ལན་ནི་རྣམ་པར་ཤེས་པ་འདི་འབའ་ཞིག་ཕྱིའི་ངོ་བོ་སྣང་བ་སྟེ་རང་གསལ་བའི་ཕྱིར་རོ། །

[Block 4361]
ཕུང་པོ་ལ་སོགས་པ་གཞན་རྣམས་ནི་མེད་དེ། གཞན་གྱི་སྣང་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4362]
རང་སྣང་བ་གང་ཡིན་པ་དེ་ནི་རྣམ་པར་ཤེས་པ་ཡིན་ཏེ་གཞན་མ་ཡིན་པས། གཟུགས་ལ་སོགས་པ་མེད་དོ། །

[Block 4363]
དེའི་རྣམ་པ་ཅན་དེ་རྣམས་ནི་ཕྱི་རོལ་གྱི་ངོ་བོར་འཁྲུལ་པའི་དབང་གིས་སྣང་སྟེ་དོན་དམ་པར་མ་ཡིན་ནོ། །

[Block 4364]
དཔེར་ན་རྒྱ་མཚོ་དང་དབའ་རླབས་བཞིན་ནོ། །

[Block 4365]
ཇི་སྐད་དུ།

[Block 4366 [VERSE]]
དབའ་རླབས་གཡོ་བ་དེ་དང་དེས། །
ཆུས་ནི་རང་བཞིན་ཐ་དད་པ། །
སྣང་བར་བྱས་ཏེ་སྐད་ཅིག་གིས། །
སླར་ཡང་གཡོ་མེད་ཉལ་བཞིན་འགྱུར། །

[Block 4367 [VERSE]]
གང་ཞིག་དེ་ནི་གཉིས་སྣང་བ། །
དེ་ལ་རིགས་པའི་སྤྱོད་ཡུལ་མིན། །
གློ་བུར་དུ་ནི་བརྗོད་པ་ཡི། །
བྲག་ཅ་ཡི་ནི་སྒྲ་བཞིན་ནོ། །

[Block 4368]
ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4369]
དེ་བས་ན་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ཅན་ནི་མེད་དེ། རྣམ་པར་ཤེས་པ་ཉིད་དེའི་རྣམ་པ་ཉིད་དུ་སྣང་བའི་ཕྱིར་རོ། །

[Block 4370]
དེས་ནི་མདོ་སྡེ་པ་ཡང་བཀག་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་དེའི་རྣམ་པར་ཤེས་པའི་རྣམ་པ་དངོས་པོ་ཡིན་ན་ཡང་མངོན་སུམ་གྱི་ཡུལ་མ་ཡིན་ནོ། །

[Block 4371]
འོན་ཀྱང་མིག་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པའི་བསྐྱེད་པ་མེད་པར༌[^2664]མི་འབྱུང་བའི་ཕྱིར། ཕྱི་རོལ་གྱི་དོན་ནི་རྗེས་སུ་དཔག་པས་རྣམ་པར་གཞག༌[^2665]གོ། །

[Block 4372]
དེ་བས་ན་མངོན་སུམ་མམ་རྗེས་སུ་དཔག་པར་བྱ་བའི་དངོས་པོ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་མེད་དེ། །རྣམ་པར་ཤེས་པ་ཁོ་ན་མངོན་སུམ་དང་རྗེས་སུ་དཔག་པའི་ཚད་མ་གཉིས་ཀྱི་ངོ་བོར༌[^2666]སྣང་བའི་ཕྱིར་རོ། །

[Block 4373]
དེས་ནི་ཉན་ཐོས་པ་དང་མདོ་སྡེ་པའི་ཕྱོགས་བཀག་པ་ཡིན་ནོ། །

[Block 4374]
རྣམ་རིག་སྨྲ་བས་ནི་རྣམ་པར་རིག་པ་ཙམ་འབའ་ཞིག་ཏུ་དོན་ལ་མི་ལྟོས་པ་ཡོད་དེ། །གང་གིས་སེམས་ཅན་སྣོད་དུ་གྱུར་པའི་ཁམས་གསུམ་པ་འདི་སྣང་བ་ཡོད་པ་ཡིན་ནོ། །

[Block 4375 [VERSE]]
ཉི་མ་ཟླ་བ་ནམ་མཁའ་དང་། །
རྒྱུ་སྐར་ཚོགས་དང་ས་གཞི་དང་། །
ཆུ་བོ་རྒྱ་མཚོ་ཕྱོགས་རི་རྣམས། །
དེ་དག་སེམས་ཀྱི་སྤྲུལ་པ་ཡིན། །

[Block 4376 [VERSE]]
ཇི་སྲིད་པ་ཡི༌[^2667]རྩེ་མོའི་བར། །
ཁམས་གསུམ་པ་རྣམས་འདི་དག་ནི། །
གང་ཞིག་ཐམས་ཅད་འདི་ལྟར་སྣང་། །
སེམས་ཉིད་ལས་ནི་ངེས་པར་བྱུང་། །

[Block 4377]
ཞེས་བཤད་པའི་ཕྱིར་རོ།[^2668] །

[Block 4378]
དེ་བཞིན་དུ་དབྱིག་གཉེན་གྱི་ཞལ་སྔ་ནས་ཀྱང་། །

[Block 4379 [VERSE]]
རྣམ་རིག་ཙམ་ནི་དོན་མེད་དེ། །
མེད་པའི་དོན་ནི་སྣང་བའི་ཕྱིར། །
ཇི་ལྟར་རབ་རིབ་ཅན་གྱིས་ནི། །
མེད་པའི་སྒྲ་ཟླ་སོགས་མཐོང་བཞིན། །

[Block 4380]
ཞེས་བཤད་དོ། །
--- END BLOCKS ---
