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
[Block 316]
དེ་ལྟར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་སྐྱེ་བ་མི་སྲིད་པ་ཅི་བསྟན་ནས།[^228] ད་ནི་འགག་པ་མི་སྲིད་པར་བསྟན་པར་བཞེད་ནས།

[Block 317 [HEADING]]
### ཚིགས་བཅད་ཉི་ཤུ་པ། ^1-21-0

[Block 318 [VERSE]]
རྒྱུ་ཟད་པ་ཡིས༌[^229]ཞི་བ་ནི། །
ཟད་ཅེས་བྱ་བར་མངོན་པ་སྟེ། །
རང་བཞིན་དུ་ནི་གང་མ་ཟད། །
དེ་ལ་ཟད་ཅེས་ཇི་སྐད་བརྗོད། །

[Block 319]
ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 320]
སྐྱེས་པའི་དངོས་པོ་སྐྱེ་བ་ཡོད་ན་འཇིག་ལ་དངོས་པོའི་གནས་པ་ཡང་རྐྱེན་གྱི་ཁོ་ན་ལས་ཏེ་གནས་པའི་རྐྱེན་མེད་ན་འཇིག་པར་འགྱུར་བས་དེ་ལྟར༌[^230]ན་འཇིག་རྟེན་ན་རྒྱུ་ཟད་ནས་ཞི་བ་དང་མྱ་ངན་ལས་འདས༌[^231]པ་གང་ཡིན་པ་དེ་ཉིད་ཞི་བ་ཞེས་བྱ་བར་དམིགས་ཏེ། གང་ཡང་གནས་པའི་རྐྱེན་མེད་ན་ཟད་པར་འགྱུར་བ་དེ་གནས་པའི་རྐྱེན་མེད་པ་ལ་རག་ལས་པས་རང་གི་ངོ་བོར་གྲུབ་པ་མེད་པར་ཁོང་དུ་ཆུད་ནས།

[Block 321 [VERSE]]
རང་བཞིན་གྱིས་ནི་གང་མ་ཟད། །
དེ་ལ་ཟད་ཅེས་ཇི་སྐད་བརྗོད། །

[Block 322]
ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 323]
གལ་ཏེ་རང་བཞིན་གྱིས་ཟད་པ་ཞིག་ཡོད་ན་ནི་དེ་རྐྱེན་ལ་ལྟོས་པར་མི་འགྱུར་རོ།[^232] །དེ་རྒྱུ་ཡོངས་སུ་ཟད་པ་ལས་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 324]
དེའི་ཕྱིར་ལས་དང་ཉོན་མོངས་པའི་དངོས་པོ་མེད་པར་མ་གྱུར་ཀྱང་མྱ་ངན་ལས་འདས་པར་འགྱུར་ཏེ། དེ་བས་ན་འབད་མི་དགོས་པར་ཐར་བར་འགྱུར་རོ། །

[Block 325]
མར་དང་རས་ཡོངས་སུ་མ་ཟད་པར་མར་མེ་འཆི་བར་འགྱུར་བའི་རིགས་ན་དེ་ཡང་དེ་ལྟ་མ་ཡིན་པས་རང་གི་ངོ་བོར་གྲུབ་པའི་འགག་པ་མེད་དོ། །

[Block 326]
ཅི་སྟེ་མར་དང་རས་ཡོངས་སུ་ཟད་པ་ནི་མར་མེའི་འཆི་བའི་རྒྱུ་མ་ཡིན་ཏེ། ཇི་ལྟ༌[^233]ཞེ་ན། མར་དང་རས་ལྷན་ཅིག་ཏུ་འགགས་ལ་མར་མེའི་སྐད་ཅིག་མ་ཐ་མ་དེའི་རིགས་ཀྱི་མར་མེ་སྐད་ཅིག་མ་མ་འོངས་པའི་ལྷན་ཅིག་བྱེད་པའི་རྒྱུ་མེད་པས་སྐྱེ་བའི་ཡན་ལག་གི་དངོས་པོར་མ་གྱུར་པ་མ་འགགས་སོ། །

[Block 327]
མ་འོངས་པ་ཡང་སྐྱེ་བའི་རྐྱེན་མེད་པས་མ་སྐྱེས་ཏེ། དེ་ལྟ་བས་ན་མ་འོངས་པའི་རྐྱེན་མེད་པས་འདི་ལ་སྐྱེ་བ་མེད་ཅེས་བྱའོ། །

[Block 328]
སྙམ་དུ་སེམས་ན་ཡང་དེ་ལྟར་མ་འོངས་པའི་རྐྱེན་མེད་པ་མི་སྐྱེ་བའི་རྒྱུར་འགྱུར་ན་ནི་གལ་ཏེ་རྐྱེན་མེད་པར་མ་གྱུར་ན་གདོན་མི་ཟ་བར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 329]
དེ་ལྟར་ན་མི་སྐྱེ་བ་ཡང་རྒྱུ་ཉིད་དུ་ཁས་བླངས་པ་ཡིན་ནོ་དེ་ལྟར་ཁས་ལེན་ན་རྒྱུ་ཟད་ནས་ཞི་བ་གང་ཡིན་པ་དེ་ཟད་པ་ཞེས་བྱ་བར་ཁས་བླངས་བ་ཡིན་ནོ། །

[Block 330]
གང་དག་དངོས་པོ་རྣམས་ཀྱི་འགག་པ་རྒྱུ་མེད་པ༌[^234]ཡིན་པར་འཛིན་པ་དེ་དག་གི་འགག་པ་དེ་དངོས་པོ༌[^235]ལ་བརྟེན་པར་མི་འགྱུར་ཏེ། ནམ་མཁའི་མེ་ཏོག་ལ་སོགས་པ་བཞིན་དུ་རྒྱུ་མེད་པའི་ཕྱིར་རོ། །

[Block 331]
གལ་ཏེ་དངོས་པོ་མེད་པའི་ཕྱིར་རྫ་མ་ལ་སོགས་པ་ཡང་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་མ་ཡིན་ན་དེ་དག་ཀྱང་དངོས་པོ་ལ་བརྟེན་པས་དེ་བས་ན་དེ་དག་གཅིག་ཏུ་ངེས་པ་མེད་དོ་ཞེ་ན་ཡང་། འཇིག་རྟེན་ན་རྒྱུ་དང་བཅས་པ་གྲགས་པས་དེ་དག་ལྟར་མ་ཡིན་ནོ། །

[Block 332]
ཡང་ན་དེ་དག་ཀྱང་འགག་པ་བཞིན་དུ་དངོས་པོ་ལ་བརྟེན་པ་མེད་པའི་སྐྱོན་དུ་འགྱུར་རོ། །

[Block 333]
གལ་ཏེ་མེད་པ་ལ་རྒྱུ་ཞེས་ཇི་སྐད་དུ་བྱ་ཞེ་ན། ཡོད་པ་ལས༌[^236]ཡང་རྒྱུ་ཞེས་ཇི་སྐད་དུ་བྱ། ས་བོན་ཡོད་པའི་དུས་ཉིད་ན། །མྱུ་གུའི་རྒྱུའི་དངོས་པོར་ནི་ཤེས་པར་མི་རུང་སྟེ། མེད་པར་འགྱུར་བའི་ཚེ་རྒྱུར་འགྱུར་རོ། །

[Block 334]
དཔེར་ན་མེད་པར་འགྱུར་བའི་རྣམ་པར་ཤེས་པ་ཉིད་རྣམ་པར་ཤེས་པ་གཞན་གྱི་དེ་མ་ཐག་པའི་རྐྱེན་དུ་ཁས་བླངས་པ༌[^237]ལྟ་བུ་སྟེ། རྣམ་པར་ཤེས་པ་དེ་ཡོད་པའི་དུས་ན་རྣམ་པར་ཤེས་པ་གཞན་གྱི་རྒྱུ་ཡིན་ནོ་ཞེས་ནི་བརྗོད་པར་མི་ནུས་སོ། །

[Block 335]
རྣམ་པར་ཤེས་པ་གཉིས་ཅིག་ཅར་དུ་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 336]
ཡོད་པ་དང་མེད་པ་གཉིས་ཀྱི་གནས་པ༌[^238]རྟོགས་པའི་རྣམ་པར་ཤེས་པ་གཞན་ནི༌[^239]མི་སྲིད་དོ། །

[Block 337]
ལ་ལ་རྒྱུ་འགགས་མ་ཐག་པ་ནི་འབྲས་བུ་སྐྱེ་བའི་རྐྱེན་ཡིན་ནོ་ཞེས་བྱ་བར༌[^240]མི་རིགས་སོ་ཟེར་བ་ཡང་ཡོད། དེ་བས་ན་མེད་པ་ཡང་རྒྱུར་སྲིད་པས་མེད་པ་རྒྱུར་མི་རུང་ངོ་ཞེས་བྱ་བར་མི་རིགས་སོ། །

[Block 338]
གལ་ཏེ་རིགས་པས་རྣམ་པར་དཔྱད་ན་རྒྱུར་མི་སྲིད་དོ་ཞེ་ན་ཡང་དེ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། འཇིག་རྟེན་གྱི་དངོས་པོ་རྣམས་ནི་རྣམ་པར་བརྟག་ཅིང་ཁས་བླང་བར་མི་བྱ་སྟེ། འཇིག་རྟེན་ཇི་ལྟ་བ་བཞིན་དུའོ། །

[Block 339]
འཇིག་རྟེན་ན་ཡང་མེད་པ་ལ་རྒྱུ་ཞེས་བྱ་བར༌[^241]ཡོད་དེ། འདི་ལྟར་ཆུ་མེད་པས་འབྲུ་མ་རུང་བར་འགྱུར་རོ།[^242] །ཟན་མེད་པས་ངའི་བུ་ཤིའོ། །ཞེས་དེ་སྐད་དུ་ཆུ་དང་ཟན་མེད་པས་འབྲུ་དང་བུ་མ་རུང་བར༌[^243]བྱས་སོ་ཞེས་ཟེར་རོ། །

[Block 340]
འཇིག་རྟེན་པའི་ཐ་སྙད་ཐམས་ཅད་ལ་འཐད་པ་མེད་པས། འཇིག་རྟེན་ན་གྲགས་པའི་དོན་རྣམས་ཀྱང་འཇིག་རྟེན་ན་གྲགས་པས་རྣམ་པར་གཞག་པར་བྱ་སྟེ། འཐད་པས་ནི་མ་ཡིན་ནོ། །

[Block 341]
ཆུ་ལ་སོགས་པ་མེད་པ་ནི་འཇིག་པའི་རྒྱུ་ཞེས་བྱ་བ་ཡོད་དེ། དེ་བས་ན། རྒྱུ་ཟད་པ་ཡིས༌[^244]ཞི་བ་ནི། ཟེད་ཅེས་བྱ་བར་མངོན་པ་སྟེ། །ཞེས་བྱ་བ་གྲུབ་པོ། །རྒྱུ་ཟད་པ་ཉིད་ཉེ་བར་བཟུང་ནས་ཟད་པ་ཞེས་བྱ་བར་རྣམ་པར་གཞག་སྟེ། ཟད་པ་དེ་ནི་རྒྱུ་ཟད་པའི་སྔ་རོལ་གྱི་གནས་ན་མི་སྲིད་ལ་ཟད་ནས་ཡོད་པས་རང་གིས་གྲུབ་པའི་ངོ་བོ་ཉིད་མེད་དོ། །

[Block 342]
གང་རང་བཞིན་གྱིས་མ་ཟད་དེ༌[^245]རྒྱུ་ལ་མི་ལྟོས་པར་ངོ་བོ་ཉིད་ཀྱིས་ཟད་པ་ཡང་མ་ཡིན་པ་དེ་དག་གཞན་གྱི་ངོ་བོ་གང་གིས་ཟད་ཅེས་བྱ་བར་རྣམ་པར་གཞག །ཟད་པ་མ་ཡིན་པའི་ངོ་བོའི་ཆོས་ནི་ཟད་པའི་ངོ་བོ་ཉིད༌[^246]མི་མཐུན་པས་ཟད་པའི་ངོ་བོར་རྣམ་པར་གཞག་པར་མི་ནུས་སོ། །

[Block 343]
གང་གི་ཕྱིར་དེ་ལྟར་སྐྱེ་བ་དང་འགག་པ་འདི་རང་གི་དངོས་པོས་ཀྱང་སྲིད་པ་མ་ཡིན་ལ། གཞན་གྱི་དངོས་པོས་ཀྱང་མ་ཡིན་པ་དེའི་ཕྱིར་རྣལ་འབྱོར་པས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཇི་ལྟ་བ་བཞིན་དུ་མཐོང་སྟེ་འཐད་པས་རྣམ་པར་དཔྱད་ན།

[Block 344 [HEADING]]
### ཚིགས་བཅད་ཉེར་གཅིག་པ། ^1-22-0

[Block 345 [VERSE]]
དེ་ལྟར་གང་ཡང་སྐྱེ་བ་མེད། །
གང་ཡང་འགག་པར་མི་འགྱུར་རོ།། །།

[Block 346]
བམ་པོ་གཉིས་པའོ། །

[Block 347]
གལ་ཏེ་དེ་ལྟར་སྐྱེ་བ་དང་འཇིག་པ་གཉིས་མི་སྲིད་ན་བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 348 [VERSE]]
ཀྱེ་མ་འདུ་བྱེད་རྟག་པ༌[^247]མེད། །
སྐྱེ་ཞིང་འཇིག་པའི་ཆོས་ཅན་ཡིན། །
སྐྱེས་ནས་འགག་པར་འགྱུར་བ་སྟེ། །
དེ་དག་ཉེ་བར་ཞི་བ་བདེ། །

[Block 349]
ཞེས་དེ་སྐད་གསུངས་པ་ཇི་ལྟ་བུ། གལ་ཏེ་སྐྱེ་བ་དང་འཇིག་པ་གཉིས་མེད་དུ་ཟིན་ན་དེའི་ཚེ་སྐྱེ་བ་དང་འཇིག་པའི་ལམ་མྱ་ངན་ལས་འདས་པར་འགྲོ་བའི་མན་ངག་བསྟན་པར་མི་འགྱུར་བ་ཞིག་ན། བསྟན་པས་དེ་བས་ན། སྐྱེ་བ་དང་འཇིག་པ་གཉིས་ཡོད་དོ་ཞེ་ན་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་དེ་སྐད་གསུངས་མོད་ཀྱི། དེ་གཉིས་རང་གི་ངོ་བོར་གྲུབ་པ་ལ་ལྟོས་ནས་གསུངས་པ༌[^248]ནི་མ་ཡིན་ནོ། །

[Block 350]
དེ་མེད་ཀྱང་འཇིག་རྟེན་འདི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བས་སྦྱོར་བ་མཛད་དེ།

[Block 351 [VERSE]]
སྐྱེ་བ་དང་ནི་འཇིག་པའི་ལམ། །
དགོས་པའི་དོན་དུ་བསྟན་པའོ། །

[Block 352]
དེ་བསྟན་པའི་སྒོ་ནས་དགོས་པ་འབའ་ཞིག༌[^249]སྒྲུབ་དགོས་པས་བཅོམ་ལྡན་འདས་ཀྱིས་སྐྱེ་བ་དང་འཇིག་པའི་ལམ་བསྟན་ཏོ། །

[Block 353]
སྐྱེ་བ་དང་འཇིག་པའི་ལམ་གྱིས་བསྟན་པའི་དགོས་པ་གང་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར།

[Block 354 [HEADING]]
### ཚིགས་བཅད་ཉེར་གཉིས་པ། ^1-23-0

[Block 355 [VERSE]]
སྐྱེ་བ་ཤེས་པས་འཇིག་པ་ཤེས། །
འཇིག་པ་ཤེས་པས་མི་རྟག་ཤེས། །
མི་རྟག་ཉིད་ལ་འཇུག་ཤེས་པས། །
དེས་ནི་ཆོས་ཀྱང་རྟོགས་པར་འགྱུར། །
--- END BLOCKS ---
