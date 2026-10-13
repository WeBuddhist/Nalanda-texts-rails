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
[Block 246]
མཐའ་ཞེས་བྱ་བའི་སྒྲ་ནི་མཆོག་ཏུ་བྱུང༌[^171]བའོ། །

[Block 247]
མཆོག་ཏུ་བྱུང་བ་ཞེས་བྱ་བ་ནི་ཕུལ་དུ་ཕྱིན་པ་ཞེས་བྱ་སྟེ། བྱིས་པའི་སྐྱེ་བོ་རྣམས་ཀྱི་སྤྱོད་ཡུལ་དུ༌[^172]གྱུར་པའི་མཐའི་རང་བཞིན་ནི་གཉི་ག་ཡང་མ་སྐྱེས་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བ་མེད་པས་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་གཉིས་གཅིག་གོ། །

[Block 248]
དེ་བས་ན་མྱ་ངན་ལས་འདས་པ་དང་ཁྱད་པར་མེད་པའི་ཕྱིར་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ལ་ཡང་ཆོས་ཞེས༌[^173]བྱ་སྟེ། དེ་མཐོང་བས་མྱ་ངན་ལས་འདས་པ་ཡང་མཐོང་བས་ན་སུས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་མཐོང་བ་དེས་ཆོས་མཐོང་ངོ་། །ཆོས་ཀྱི་ངོ་བོ་ཉིད་དང་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཐ་མི་དད་པས༌[^174]ན༌[^175]མཐོང་བས་སངས་རྒྱས་མཐོང་བ་ཡིན་ནོ། །

[Block 249]
དེ་ལྟར་ན་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་སྐྱེ་བ་མེད་པ༌[^176]ལ་དམིགས་པའི་ཆོས་ཤེས་པས་རྟེན་བདེན་པ་གསུམ་རྟེན་ཅིང་འབྲེལ༌[^177]བར་འབྱུང་བ་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་ལ། མྱ་ངན་ལས་འདས་པ་ཡང་དེའི་ངོ་བོ་ཉིད་ཡིན་པར་མཐོང་བས་མངོན་པར་རྟོགས་པ་གཅིག་ཏུ་ཟད་དོ། །

[Block 250]
དེ་ལ་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ལ་དམིགས་པའི་ཆོས་ཤེས་པ་སྡུག་བསྔལ་གྱི་སྐྱེ་བ་མེད་པ་དང་འགག་པ་མེད་པ་ཡོངས་སུ་གཅོད་པ་གང་ཡིན་པའི་བདག་ཉིད་དེ་སྡུག་བསྔལ་ཡོངས་སུ་ཤེས་སོ། །

[Block 251]
ལས་དང་ཉོན་མོངས་པའི་སྐྱེ་བ་དང་འགག་པ་མེད་པ་ཡོངས་སུ་གཅོད་པ་གང་ཡིན་པ་དེ་ནི་ཀུན་འབྱུང་བ་ཤེས་པའོ། །

[Block 252]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་སྐྱེ་བ་མེད་པ་དང་འགག་པ་མེད་པ་ཡོངས་སུ་གཅོད་པ་མ༌[^178]ཡིན་པ་འདི་ནི་འགོག་པ་ཤེས་པའོ། །

[Block 253]
ལམ་གྱི་བདེན་པ་ཡང་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཡིན་པས་ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བ་མེད་པ་དང་འགག་པ་མེད་པ་ཡོངས་སུ་གཅོད་པ་གང་ཡིན་པ་དེ་ནི་ལམ་ཤེས་པའོ། །

[Block 254]
དེ་ལྟར་ན་ཆོས་ཤེས་པས་སྐད་ཅིག་གཅིག་ལ་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་མཐོང་བས་སྔོན་མ་མཐོང་བའི་བལྟ་བར༌[^179]བྱ་བ་གཞན་མི་སྲིད་དོ། །

[Block 255]
གལ་ཏེ་དེ་ལྟར་ན་མཐོང་བའི་ལམ་སྐད་ཅིག་མ་བཅོ་ལྔར་ཇི་ལྟར་གཞག །སྡེ་པ་ཁ་ཅིག་ནི་མཐོང་བའི་ལམ་སྐད་ཅིག་མ་བཅོ་ལྔར་མི་འདོད་ཀྱི། མངོན་པར་རྟོགས་པ་གཅིག་ཏུ་ཟད་པར་འདོད་དོ། །

[Block 256]
དེ་དག་གི་འདོད་པ་དང་བཤད་པ༌[^180]འདི༌[^181]མི་འགལ་ལོ། །

[Block 257]
གང་དག་སྐད་ཅིག་མ་བཅོ་ལྔར་འདོད་པ་དེ་དག་གི་ལྟར༌[^182]ཡང་དེ་ལྟ་བུས་གདུལ་བའི་སྐྱེ་བོ་ལ་དེ་བསྟན་པས་ཕན་གདགས་པའི་ཕྱིར་ཤེས་པ་ངོ་བོ་གཅིག་ལ༌[^183]ཆར་ཕྱེ་སྟེ། ཆ་བཅོ་ལྔར་རྣམ་པར་གཞག་གོ། །

[Block 258]
གལ་ཏེ་དེ་ལྟར་ན་ལམ་སྒོམ་པ་རྣམ་པ་བཅུ་དྲུག་པ་དེ་ཅི་ལྟ་བུར་ཐར་པར༌[^184]འདོད་པ་རྣམས་ལམ་རྣམ་པ་གཞན་དག་གིས་དེ་ཁོ་ན་ཤེས་པ་ལ་འཇུག་པ་གོམས་པར་བྱ་བའི་ཕྱིར་འདི་ཡང་ཡོངས་སུ་བརྟགས་ནས་རྣམ་པར་གཞག་པ་ཉིད་དེ། དེ་ཁོ་ན་ནི་ངོ་བོ་གཅིག་པུར་ཟད་དོ། །

[Block 259]
ཅི་སྟེ་ཁྱད་པར་དུ་དབྱེ་བའི་རྣམ་པ་དངོས་པོ་གཞན་ཤེས་པ་གཞན་གྱིས༌[^185]གཟུང་བ་ཞིག་ཡོད་ན་ནི། དེའི་ཚེ་རྣམ་པ་ཡོངས་སུ་མ་བཅད་པ༌[^186]ཡོངས་སུ་བཅད་དགོས་པར་འགྱུར་ཏེ། ཆོས་ཤེས་པ་དེའི་འོག་ཏུ་བྱེ་བྲག་ཏུ་ཡོངས་སུ་གཅད་པར་བྱ་བ་བྱེ་བྲག་དབྱེ་བ་ཞིག་ཡོད་ན་ནི་དེའི་དམིགས་པ་གཞན་དུ་བརྟགས་པས་དེས་དེའི་ངོ་བོ་བྱེ་བྲག་ཏུ་ཡོངས་སུ་གཅད༌[^187]དགོས་པས་མི་མཁས་པ་སུས་དངོས་པོ་ཤིན་ཏུ་ཕྲ་བ་ལ་རང་གི་ངོ་བོར་སྐྱེ་བར་རྣམ་པར་བརྟགས་པས་ཀྱང་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་དོན་ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བ་མེད་ཅིང་རོ་གཅིག་པའི་དོན་མི་ཤེས་པ་ཡིན་ན་རགས་པ༌[^188]ས་ལ་སོགས་པ་ལྟ་ཅི་སྨོས། དེ་ལྟར༌[^189]རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་དོན་དེ་མཚན་ཉིད་གཅིག་ཏུ་མཐོང་སྟེ། རིམ་གྱིས་གོམས་པར་བྱས་ནས་མ་རིག་པ་མ་ལུས་པར་འགགས་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ངོ་བོ་ཉིད་ལ་དམིགས་པའི་ཤེས་པ་ལ་གནས་པ་ནི་མཐོང་བའི་ཆོས་ལ་མྱ་ངན་ལས་འདས་པ་དང་བྱ་བ་བྱས་པ་ཞེས་བྱ་བར་རྣམ་པར་གཞག་སྟེ་གཞན་དུ་མ་ཡིན་ནོ། །

[Block 260 [HEADING]]
### ཚིགས་བཅད་བཅུ་གསུམ་པ། ^1-14-0

[Block 261]
ཅི་སྟེ་ཁྱོད་ཀྱི་གཞུང་ལྟར་ན། ཉོན་མོངས་ཟད་པའི་དགེ་སློང་གི །

[Block 262]
འཁོར་བ་གལ་ཏེ་རྣམ་བཟློག༌[^190]ན། །རྫོགས་པའི་སངས་རྒྱས་རྣམས་ཀྱིས་ཀྱང་། །

[Block 263]
ཅི་ཕྱིར་དེ་ཡི་རྩོམ་མི་བཟད།[^191] །གལ་ཏེ་ཡེ་ཤེས་ཀྱིས་ཉོན་མོངས་པ་བཟློག་ན་ལས་ལྡོག་སྟེ། རྒྱུ་དང་རྐྱེན་དུ་མི་ལྡན་པའི་ཕྱིར་ཐོག་མ་མེད་པ་ནས་འཁོར་བར་འཇུག་པ་དང་སྐྱེ་བ་དང་འཆི་བ་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པ་རང་གི་མཚན་ཉིད་ཀྱིས་གྲུབ་པའི་ངོ་བོ་གཟུགས་ལ་སོགས་པའི་རྒྱུན་ལྡོག་ན་དེ་ལྟ་ན་ནི་དེ་རྩོམ་པ་རྫོགས་པའི་སངས་རྒྱས་རྣམས་ཀྱིས་མ་གསུངས་པ་ནི་གཏན་ཚིགས་འདི་ལྟ་བུ་ཞིག་གིས་བཅོམ་ལྡན་འདས་ཀྱིས་རྩོམ་པ་མ་གསུངས་སོ། །ཞེས་འདི་ལ་ཁྱོད་ཀྱི་ཕུང་པོའི་རྒྱུན་དེའི་རྩོམ་པ་ཐ་མ་བཞིན་དུ་བརྗོད་དགོས་པར་འགྱུར་རོ། །

[Block 264]
མི་མཁྱེན་ཏེ་མ་གསུངས་སམ་གཞན་ཞིག་གི་ཕྱིར་མ་གསུངས་ཞེས་བྱ། འདི་ལ་བཅོམ་ལྡན་འདས་ནི་ཐམས་ཅད་མཁྱེན་པར༌[^192]ཁས་ལེན་པའི་ཕྱིར་མི་མཁྱེན་ནི་མི་སྲིད་དོ། །

[Block 265]
གཞན་ཞིག་གི་ཕྱིར་མ་གསུངས་ཞེས་བྱར་ནི་དེ་ཡང་མི་རིགས་སོ། །

[Block 266]
ཟོ་ཆུན་བརྒྱུད་མོའི་འཁྲུལ་འཁོར་ལྟར་ཐོག༌[^193]མ་མེད་པའི་ཕྱིར་མ་གསུངས་ཞེས་བྱར་ནི་གལ་ཏེ་དེ་ལྟར་ན་ཟོ་ཆུན་བརྒྱུད་མོའི་འཁྲུལ་འཁོར་ལྟར་ཐོག་མ་མེད་པ་དེ་བཞིན་དུ་དེའི་ཐ་མ་ཡང་མེད་པར་འགྱུར་ཏེ། འཁོར་ལོ་ལ་སོགས་པའི་དཔེ་ལ་ཡང་དེ་སྐད་ཅེས་བརྗོད་པར་བྱའོ། །

[Block 267]
ཟད་པར་འགྱུར་རོ་ཞེས་བཤད་པས་ཐ་མ་ཡོད་པ་སྐད་བྱ་ན་ནི་དེའི་ཕྱིར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་མི་མཁྱེན་པ་ཡོད་པར་འགྱུར་ཏེ། མི་མཁྱེན་མི་སྲིད་པས་རྩོམ་པ་ཡང་བསྟན་དགོས་སོ། །

[Block 268]
མ་བསྟན་ན་ཡང་རིགས་པ་འདི་དང་སྦྱར་ན་མེད་དུ་མི་རུང་སྟེ་དེ་བས་ན།

[Block 269 [HEADING]]
### ཚིགས་བཅད་བཅུ་བཞི་པ། ^1-15-0

[Block 270]
རྩོམ་པ་ཡོད་ན་ངེས་པར་ཡོང་།[^194] །

[Block 271 [VERSE]]
ལྟ་བར་གྱུར་པ་ཡོངས་སུ་འཛིན། །
རྩོམ་པ་ཡོད་པར་བརྟགས་ན་ནི། །
འཁོར་བ་ཐོག་མ་ཅན་དུ་འགྱུར་རོ། །

[Block 272]
ཐོག་མ་ཡོད་པ་ཅན་དུ་གྱུར་ན་ནི་རྒྱུ་མེད་པར་སྨྲ་བ་ཁས་བླངས་པས་ལོག་པར་ལྟ་བ་ཉིད་དུ་འགྱུར་རོ། །

[Block 273]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་སྨྲ་བ་ལ་ནི་ཉེས་པ་འདི་མེད་དོ། །

[Block 274]
སུ་དངོས་པོ་རྣམས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་འདོད་པ་དེ་ནི་དེ་དག་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པར་འདོད་པས་དེ་དག་གི་ཐོག་མའམ་ཐ་མ་མེད་པས་ཡོངས་སུ་བརྟག་པ་མི་ནུས་པར་བསྟན་པའི་ཕྱིར།

[Block 275 [VERSE]]
རྟེན་ཅིང་འབྲེལ་པར་གང་འབྱུང་བ། །
དེ་ལ་སྔོན་དང་ཐ་མ་ཅི། །

[Block 276]
ཞེས་བྱ་བ་སྨོས་ཏེ་གདོན་མི་ཟ་བར་འདི་ཉིད་ཁས་བླངས་དགོས་སོ། །

[Block 277]
གཞན་དུ་ན་ནི་འཁོར་བ་ཐོག་མ་ཅན་དུ་འགྱུར་བར་ཡང་མ་ཟད་དེ། ངོ་བོ་ཉིད་ཀྱིས་སྐྱེས་པ་ན༌[^195]གཞན་དུ་འགྱུར་མི་སྲིད་པས་རྟག་པ་ཁོ་ནར་གྱུར་པར༌[^196]བསྟན་པའི་ཕྱིར།

[Block 278 [HEADING]]
### ཚིགས་བཅད་བཅོ་ལྔ་པ། ^1-16-0

[Block 279 [VERSE]]
སྔོན་སྐྱེས་པ་ནི་ཇི་ལྟ་བུར། །
ཕྱི་ནས་རབ་ཏུ་ལྡོག་པར་འགྱུར། །

[Block 280]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 281]
ངོ་བོ་ཉིད་མི་འགྱུར་བས་རྟག་གོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 282]
དངོས་པོ་སྐྱེ་བ་དེའི་རང་བཞིན་མེད་པ་ལས་འབྱུང་བ་ཁས་ལེན་ན་ནི།

[Block 283 [VERSE]]
རྩོམ་པ་ཡོད་ན་ངེས་པར་ཡང་། །
ལྟ་བར་གྱུར་པ་ཡོངས་སུ་འཛིན། །

[Block 284]
མེད་པ་ལས་དངོས་པོ་རྣམས་རྐྱེན་མི༌[^197]རྒྱུ་མེད་པ་ཁོ་ན་ལས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 285]
དེ་བས་ན་རྒྱུ་མེད་པར་ལྟ་བ་དེ་ཡང་དེ་བཞིན་དུ་ཡོད་ལ་དེ་ཡང་འབྲེལ་ན་ནི་ཆད་པར་ལྟ་བའི་སྐྱོན་དུ་ཡང་འགྱུར་རོ། །
--- END BLOCKS ---
