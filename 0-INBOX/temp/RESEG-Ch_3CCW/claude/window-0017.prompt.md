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
[Block 596]
ཞེ་སྡང་ནི་གཞན་གྱི་ཕྱོགས་ལ་རྒྱབ་ཀྱིས་བལྟས་པའི་མཚན་ཉིད་དོ། །

[Block 597]
འདོད་ཆགས་དང་ཞེ་སྡང་གང་ལས་འབྱུང་བ་དེ་འདོད་ཆགས་དང་ཞེ་སྡང་འབྱུང་བའོ། །

[Block 598]
རྣམ་པར་སྨིན་པ་ཤིན་ཏུ་མི་བདེ་བ་དང་ཤིན་ཏུ༌[^353]བཟོད་པར་དཀའ་བའི་ཕྱིར་མི་བཟོད་པའོ། །

[Block 599]
སེམས་ཀྱི་རྒྱུད་ལ་གནོད་པ་སྐྱེད་པར་བྱེད་པ་དང་། འདའ་བར་དཀའ་བའི་ཕྱིར་མ་རུངས་པ་སྟེ། དེ་ཡང་གང་ཞེ་ན། ལྟ་བ་ཡོངས་སུ་འཛིན་པའོ། །

[Block 600]
ལྟ་བ་ལ་གནས་པ་འདི་ལྟ་བུ་འདི་ཡང་དངོས་པོར༌[^354]ལེན་པ་ལས་སྐྱེའོ། །

[Block 601]
ལྟ་བ་ཡོངས་སུ་འཛིན་པ་ཡོད་ན་རང་གིས་ཁས་བླངས་པའི་དོན་བསྟན་པར་འདོད་པ་དང་། གཞན་གྱིས་ཁས་བླངས་པ་ཞིག་འདོད་པའི་ཕྱིར་ལྟ་བ་ཁས་ལེན་པ་ལས་བྱུང་བའི་རྩོད་པ་དངོས་པོ༌[^355]ལ་མངོན་པར་ཞེན་པའི་རྩ་བ་ལས་བྱུང་བ་གཞན་དག་ཀྱང་འབྱུང་ངོ་། །གང་གི་ཕྱིར་དེ་དེ་ལྟར་གྱུར་པའི་ཕྱིར།

[Block 602 [HEADING]]
### ཚིགས་བཅད་ཞེ་བདུན་པ། ^1-48-0

[Block 603 [VERSE]]
དེ་ནི་ལྟ་བ་ཀུན་གྱི་རྒྱུ། །
དེ་མེད་ཉོན་མོངས་མི་སྐྱེ་སྟེ། །
དེ་བས་དེ་ནི་ཡོངས་ཤེས་ན། །
ལྟ་དང་ཉོན་མོངས་ཡོངས་སུ་འབྱང་། །

[Block 604]
དངོས་པོར་ཁས་ལེན་པ་ཡོད་ན་དེ་ནི་སྔོན་གྱི་མཐའ་དང་ཕྱི་མའི་མཐའ་དང་དབུས་ཡོངས་སུ་རྟོག་པས༌[^356]དེ་ལ་དམིགས་པ་ལྟ་བར་གྱུར་པ་རྣམས་སུ་ལྟུང་བ་ཡོད་པས་ན་དངོས་པོར་འཛིན་པ་དེ་ལྟ་བར་གྱུར་པ་ཐམས་ཅད་ཀྱི་རྒྱུ་ཡིན་ནོ། །

[Block 605]
ལྟ་བར་གྱུར་པ་ཡོད་ན་རྒྱུ་དེ་ལས་བྱུང་བའི་ཉོན་མོངས་པ་འབྱུང་སྟེ། རང་གི་ལྟ་བ་ལ་འདོད་ཆགས་འབྱུང་བ་དང་། དེས་ང་རྒྱལ་དུ་འགྱུར་བ་དང་། གཞན་གྱི་ལྟ་བ་ལ་ཞེ་སྡང་འབྱུང་བའི་ཕྱིར་དང་། ཐམས་ཅད་དུ་གཏི་མུག་འབྱུང་བས་ལྟ་བར་གྱུར་པ་ལས་ཉོན་མོངས་པ་རྣམས་འབྱུང་ངོ་། །གང་གི་ཕྱིར་དེ་ལྟར་ལྟ་བ་དང་། ཉོན་མོངས་པ་ཐམས་ཅད་དངོས་པོར་དམིགས་པའི་རྒྱུ་ལས་བྱུང་བ་དེའི་ཕྱིར་དངོས་པོ་དེ་ཡོངས་སུ་ཤེས་ཏེ། དངོས་པོའི་རང་གི་ངོ་བོ་ཇི་ལྟ་བ་བཞིན་དུ་ཁོང་དུ་ཆུད་ན་དམིགས་པ་མེད་པས་ལྟ་བ་རྣམས་ལྡོག་གོ། །

[Block 606]
དེ་ལོག་ན་ཉོན་མོངས་པ་རྣམས་སྤོང་ངོ་། །གལ་ཏེ་འདི་སྙམ་དུ།

[Block 607 [HEADING]]
### ཚིགས་བཅད་ཞེ་བརྒྱད་པ། ^1-49-0

[Block 608 [VERSE]]
གང་གིས་དེ་ཤེས་འགྱུར་ཞེ་ན། །
རྟེན་ཅིང་འབྱུང་བ་མཐོང་བ་སྟེ། །

[Block 609]
རྟེན་ཅིང་སྐྱེས་པ་མ་སྐྱེས་ཤེས།[^357] །ཡང་དག་མཁྱེན་པ་མཆོག་གིས་གསུངས། །

[Block 610]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་མཐོང་ནས་དངོས་པོ་རྣམས་ལ་ངོ་བོ་ཉིད་དུ་དམིགས་པར་མི་འགྱུར། གང་བརྟེན་ནས་སྐྱེས་པ་དེ་ནི་གཟུགས་བརྙན་བཞིན་དུ་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 611]
བརྟེན་ནས་བྱུང་བ་གང་ཡིན་པ་དེ་ནི་བྱུང་བ་ཉིད་དུ་ངེས་ཏེ། དེ་ལ་མ་བྱུང་ཞེས་བྱ་བའི་སྒྲར་ཇི་སྐད་དུ་གདགས། གལ་ཏེ་མ་སྐྱེས་པ་ཞེས་བྱ་བ་ན༌[^358]ནི་དེ་བརྟེན་ནས་སྐྱེས་པ་ཞེས་བྱར་མི་རུང་སྟེ། དེ་བས་ན་ནང་འགལ་བའི་ཕྱིར་དེ་རིགས་པ༌[^359]མ་ཡིན་ནོ་ཞེས་ཟེར་ན། ཀྱེ་མ་ཀྱི་ཧུད་རྣ་བ་དང་སྙིང་མེད་པས་ཀྱང་བདག་ལ་ཀླན་ཀ་བཙལ་བ་གང་ཡིན་པ་དེ་ནི་བདག་མ་རུངས་པ་ཞེས་བབ་བོ། །

[Block 612]
གང་བརྟེན་ནས་སྐྱེས་པ་དེ་གཟུགས་བརྙན་བཞིན་དུ་ངོ་བོ་ཉིད་ཀྱིས་སྐྱེས་པ་མ་ཡིན་ནོ་ཞེས་ཁོ་བོས་གང་གི་ཚེ་སྨྲས་པ་དེའི་ཚེ་དེ་ལ་ཀླན་ཀ་བཙལ་བའི་སྐབས་ག་ལ་ཡོད། བརྟེན་ནས་འབྱུང་བའི་རྣམ་པ་གང་གི་གཟུགས་བརྙན་དམིགས་པ་དེའི་བརྫུན་པར་གྱུར་པ་དམིགས་པ་ཁོ་བོ་མ་སྐྱེས་པའོ་ཞེས་སྨྲའི། བདག་ཉིད་གང་གིས་དེའི་བྱུང་བ༌[^360]མེད་པ་རྣམ་པར་གཞག་པ་དེ་ཉིད་ཀྱིས་དེའི་སྐྱེ་བ་མེད་པར་བརྗོད་དོ། །

[Block 613]
བདག་ཉིད་གང་གིས་དེའི་སྐྱེ་བ་མེད་པར་རྣམ་པར་གཞག་ཅེ་ན། ཡང་དག་པར་འདོད་པའི་ངོ་བོ་ཉིད་ཀྱིས་འདོད་ཀྱི། བརྫུན་པའི་ངོ་བོས་ནི་མ་ཡིན་ཏེ། དེ་ནི་ངོ་བོ་དེས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཁས་བླངས་པའི་ཕྱིར་རོ། །

[Block 614]
དེའི་ཕྱིར་དེ་ལྟར་སྐྱེ་བ་དང་མི་སྐྱེ་བ་འདི་གཉིས་ཡུལ་མ་ཡིན་པའི་ཕྱིར་གཅིག་གི་ཡུལ་དུ༌[^361]ག་ལ་འགྱུར། གལ་ཏེ་རྟེན་ཅིང༌[^362]འབྲེལ་བར་འབྱུང་བ་ཇི་ལྟར་དམིགས་པ་དེ་ལ་སྐྱེ་བ་མེད་པ་ཞེས་མི་སྟོན་གྱི། ངོ་བོ་ཉིད་ལ་སྐྱེ་བ་མེད་པ་ཞེས་སྟོན་ན་འདི་ལ་ཁྱོད་ཀྱིས་དེ་སྐད་སྨྲས་པ་ལྟ་བུ་སྔོན་མ་ཐོས་པ་ཅི་ཞིག་བསྟན་པར་འགྱུར། ཁོ་བོ་ནི་སྔོན་མ་ཐོས་པ་ཅུང་ཟད་ཀྱང་མི་སྟོན་ཏེ། ངེད་ཀྱི་བསྟན་བཅོས་ནི་ཇི་ལྟར་གནས་པའི་ཆོས་ཉིད་བསྟན་པ་ཆེད་ཆེ་བར་བྱ་བ་ཡིན་ན་ཇི་ལྟར་གནས་པའི་ཆོས་ཉིད་དེ་ལ་ཡང་ཕྱིན་ཅི་ལོག་གི་རྗེས་སུ་འབྲང་བ་འདྲོན་པོ༌[^363]ཕྱོགས་བསླད་པ་ལྟ་བུ་དག་རྣམ་པ་གཞན་དུ་ཡོངས་སུ་རྟོག་གོ། །

[Block 615]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པ་སྟེ། ཕྱིན་ཅི་ལོག་པའི་བདག་ཉིད་དུ་མ་བྱུང་བ་ཡིན་ན་སོ་སོའི་སྐྱེ་བོ་དག་དེ་ལ་ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བར་ཡོངས་སུ་རྟོག་སྟེ། དེ་ལ་མངོན་པར་ཞེན་ནས་ཀུན་ནས་ཉོན་མོངས་སོ། །

[Block 616]
ཀུན་ནས་ཉོན་མོངས༌[^364]དེ་སྤང་བའི་ཕྱིར་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཡང་དག་པར་རིག་པ་རྣམས་ཀྱི་མཆོག་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ། བརྟེན་ནས་སྐྱེས་པ་མ་སྐྱེས་ཤེའོ། །

[Block 617]
སྒྱུ་མ་མཁན་ནི་སྒྱུ་མའི་ན་ཆུང༌[^365]ཡང་དག་པ༌[^366]སྙམ་དུ་མངོན་པར་ཞེན་ནས་ཀུན་ནས་ཉོན་མོངས་པར་མི་འགྱུར་གྱི། ན་ཆུང་ཡང་དག་པ་སྙམ་དུ་མངོན་པའི་ང་རྒྱལ་ཅན་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་དེ་ལ་ནི་ཀུན་ནས་ཉོན་མོངས་པ་འབྱུང་ངོ་། །དེ་བཞིན་དུ་འདི་ལ་ཡང་བརྟེན་ནས་བྱུང་བ་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་སོ་ཞེས་བཅོམ་ལྡན་འདས་གསུངས་པས༌[^367]དངོས་པོ་རྣམས་ལ་ངོ་བོ་ཉིད་དུ་མངོན་པར་ཞེན་པ་བཟློག་པ་ཡིན་ནོ། །

[Block 618]
འདི་ལྟར།

[Block 619 [HEADING]]
### ཚིགས་བཅད་ཞེ་དགུ་པ། ^1-50-0

[Block 620 [VERSE]]
ལོག་པའི་ཤེས་པས་ཟིལ་གནོན༌[^368]པ། །
བདེན་པ་མིན་ལ་བདེན་འཛིན་པའི། །
ཡོངས་སུ་འཛིན་དང་རྩོད་སོགས་ཀྱི། །
རིམ་པ་ཆགས་ལས་ཤིན་ཏུ་བྱུང་། །

[Block 621]
དེ་ལྟ་བས་ན་དངོས་པོ་བདེན་པ་མ་ཡིན་པ༌[^369]བདེན་པར་འདུ་ཤེས་པ་དེ་བཟློག་པའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་བསྟན་ཏོ། །

[Block 622]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ནི་སླུ་བའི༌[^370]ཕྱིར་བདེན་པ་མ་ཡིན་ནོ། །

[Block 623]
དེ་བདེན་པ་མ་ཡིན་པར་རྟོགས་ན་དངོས་པོ་ལ་ཆགས་པ་ལྡོག་གོ། །

[Block 624]
དངོས་པོ་ལ་ཆགས་པ་ལོག་ན་དངོས་པོ་ཡོངས་སུ་འཛིན་པ་ལྡོག་གོ། །

[Block 625]
ཡོངས་སུ་འཛིན་པ་ནི་བདག་གིར་བྱེད་པ་སྟེ། དེ་ནི་དེ་ལྟར་ལྡོག་གོ། །

[Block 626]
དེ་ལོག་ལ༌[^371]འདོད་པ་ལ་ཆགས་པར་གྱུར་པ་དང་། ལྟ་བ་ལ་ཆགས་པར་འགྱུར་བའི་རྩོད་པ་ཡང་ལྡོག་གོ། །

[Block 627]
རྩོད་པ་ལོག་ན་འཐབ་པ་ལ་སོགས་པ་ཡང་ལྡོག་གོ། །

[Block 628]
དེ་བས་ན་དངོས་པོ་བརྟེན་ནས་གྲུབ་པ་གང་ཡང་མི་དམིགས་ན་གདོན་མི་ཟ་བར།

[Block 629 [HEADING]]
### ཚིགས་བཅད་ལྔ་བཅུ་པ། ^1-51-0

[Block 630]
རྩོད་མེད་ཆེ་བའི་བདག་ཉིད་ཅན། །དེ་དག་ལ་ནི་ཕྱོགས་མེད་དོ། །

[Block 631]
རང་གི་ཕྱོགས་ཁས་ལེན་པ་ཡོད་ན་ནི་དེའི་ཚེ་དེ་གཟུགས་པའི་ཕྱིར་གཞན་རྣམས་དང་རྩོད་པར་གྱུར་ན་དེ་དག་ལ་ནི་དེ་ལྟ་བུ་ཡང་མེད་པས་དེ་བས་ན་རྩོད་མེད་ཆེ་བའི་བདག་ཉིད་ཅན་ནོ། །

[Block 632]
གལ་ཏེ་དེ་དག་ལ་རང་གི་ཕྱོགས་མེད་དུ་ཟིན་ཀྱང་གཞན་གྱི་ཕྱོགས་གཞིག་པ་མེད་མི་སྲིད་དེ།

[Block 633]
དེ་བས་ན་གཞན་གྱི་ཕྱོགས་ཡོད་དང་། །བདག་གི་ཕྱོགས་ཀྱང་མེད་དུ་མི་རུང་ངོ་། །

[Block 634]
ཕྱོགས་ཤིག་ཡོད་ན་ནི་བདག་གི༌[^372]ཕྱོགས་སམ་གཞན་གྱི་ཕྱོགས་མེད་པར༌[^373]ཡང་འགྱུར་ན། གང་གི་ཚེ་ཕྱོགས་ཡེ་མེད༌[^374]དེའི་ཚེ།

[Block 635 [VERSE]]
གང་རྣམས་ལ་ནི་ཕྱོགས་མེད་པ། །
དེ་ལ་གཞན་ཕྱོགས་ག་ལ་ཡོད། །
--- END BLOCKS ---
