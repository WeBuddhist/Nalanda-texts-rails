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
[Block 4411]
རྙེད་པ་གྲུབ་ན་ནི་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4412]
ཀུན་དགའ་ར་བ་འམ་དགེ་བསྙེན་དག་ཡོད་ན་བསྒོ་བས་དཀོན་མཆོག་གི་དོན་དུ་བསྐྱེད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཀུན་དགའ་ར་བ་འམ་དགེ་བསྙེན་དག་ཡོད་པར་གྱུར་ན་དེ་གཉིས་འདིར་བསྐོ་བས་དཀོན་མཆོག་གི་དོན་དུ་སྦྱོར་བ་བྱེད་པ་ལ་ངེས་པར་སྦྱར་བར་བྱའི་རང་ཉིད་ཀྱིས་ནི་འཇུག་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 4413]
འདིར་གཞུང་ནི་མ་མོ་ལས་འདི་ལྟ་སྟེ་ཡངས་པ་ཅན་གྱི་ཚོང་པ་རྣམས་ཀྱིས་བཅོམ་ལྡན་འདས་ཀྱི་མཆོད་རྟེན་ཡང་བྱེད་དུ་བཅུག་གཙང་ཁང་བྱུར་བུ་ཡང་བྱེད་དུ་བཅུག་ནས། དགེ་སློང་རྣམས་ལ་མཆོད་རྟེན་དང་གཙང་ཁང་བྱུར་བུ་གང་ཞིག་རལ་དུ་མི་འགྱུར་བའི་ཡོ་བྱད་རྗེས་སུ་གཏོད་པ་ན་དགེ་སློང་དག་འགྱོད་ཅིང་ལེན་པར་མི་བྱེད་ནས་སྐབས་དེ་དགེ་སློང་གིས་བཅོམ་ལྡན་འདས་ལ་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཀུན་དགའ་ར་བ་འམ་དགེ་བསྙེན་དག་གིས་མཆོད་རྟེན་ཞིག་རལ་དུ་མི་འགྱུར་བའི་ཡོ་བྱད་བླང་བར་བྱ་ཞིང་བླངས་ནས་ཀྱང་བསྐྱེད་པར་བྱ་སྟེ། དེ་ལ་རྙེད་པ་ཇི་ཙམ་བྱུང་བ་དེས་མཆོད་རྟེན་ལ་མཆོད་པ་བྱ་བར་ངས་རྗེས་སུ་གནང་ངོ་ཞེས་གསུངས་སོ། །

[Block 4414]
གཏའ་ཉིས་རིར༌[^3020]བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཆུད་མི་གཟན་པར་བྱ་བའི་ཕྱིར་འདི་སྤང་བ་མི་སྐྱེད་པའི༌[^3021]ཡན་ལག་ཅེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །ཇི་ལྟར་འདི་བླངས་ནས་སྦྱར་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དཔང་པོ་དང་ལོ་དང་ཟླ་བ་དང་ཉི་མ་དང་དགེ་འདུན་གྱི་གནས་བརྟན་དང་དགེ་སྐོས་དང་ལེན་པ་པོ་དང་རྫས་དང་སྐྱེད༌[^3022]རྣམས་དཔང་རྒྱར་བྲིས་ནས་སོ། །

[Block 4415]
རྒྱུས་ཤེས་པས་དེ་གཞན་ལ་ཁོང་དུ༌[^3023]ཆུད་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་གང་ལ་འཇུག་པ་འདི་དེས་འདི་ཙམ་ཞིག་འདི་ལས་སྤྱད་པ་དང་དེས་འདི་ཙམ་དུས་དེ་ལ་སྦྱིན་པར་བྱ་བ་ཞེས་བྱ་བའི་རྒྱུས་ཤེས་པར་གྱུར་པ་དེས་གཞན་གྱི་སྟེང་དུ་འདིའི་ལོ་རྒྱུས་ཤེས་པའི་དགེ་སློང་གང་ཞིག་གིས་དེ༌[^3024]ལ་རིམ་པ་ཐོབ་ན་ཁོངས་སུ་ཆུད་པར་བྱ་བ་ནི་བརྗོད་པར་བྱ་ཞེས་བྱ་བའི༌[^3025]དོན་ཏོ། །

[Block 4416]
འདིར་གཞུང་ནི་དགེ་སློང་གཉུག་མར་གནས་པ་རྣམས་ཀྱིས་དགེ་སློང་གློ་བུར་དུ་ལྷགས་པ༌[^3026]རྣམས་ལ་གང་ཟག་ཆེ་གེ་མོ་ཞིག་ལས་ཟླ་བ་རེ་རེ་ཞིང་འདི་ཙམ་ཞིག་མནོད་དོ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4417]
མངོན་མཚན་ཅན་གྱི་སྤྱོད་པའི་སྤང་བའོ།། །།

[Block 4418]
སྔར་བསྟན་མ་ཐག་པའི་བསླབ་པའི་གཞིར་སྐྱེད༌[^3027]ཕྱིན་ན་དངོས་གཞིའོ་ཞེས་སྨས་ན་སྤྱོད་པ་གང་གིས་ཡིན་པ་མ་བསྟན་པས་དེའི་ཕྱིར་གཞན་གྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྤྱོད་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4419]
པ་ཎ་དང་རིན་པོ་ཆེ་དག་གིས་སྔར་བསྟན་པ་དེ་བས་ན་དེ་དག་ལས་གཞན་པ༌[^3028]གཞལ་བར་བྱ་བ་ལ་སོགས་པས་སྤྱོད་པ་ལས་སྐྱེད༌[^3029]ཕྱིན་ན་ལྟུང་བ་འདིར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4420]
རྙེད་པ་གང་ལ་མངོན་སུམ་མམ་བརྒྱུད་པས་སྐྱེད་པ༌[^3030]ཉིད་དང༌[^3031]པ་ཎ་དགོས་པ་ལས་སྐྱེས་པ་ཉིད་དེར་སྔ་མའི་ལྟུང་བའོ། །

[Block 4421]
གང་དུ་ཇི་ལྟར་པ་ཎ་མི་དགོས་པ་ཉིད་དེ་ལ་འདི་ཞེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །

[Block 4422]
གང་དུ་པ་ཎ་གཞན་དང་ལྡན་པ་ལ་དགོས་པ༌[^3032]དེར་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་ཞེ་ན། སྔར་གྱི་ལྟུང་བ་ཞེས་བྱ་བ་པ་ཎས་ཉོས་པ་ཐམས་ཅད་དེ་ལ་པ་ཎ་དགོས་པས་ཡང་དག་པར་རེག་པ་འདིར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 4423]
དགེ་འདུན་གྱི༌[^3033]བཤོས་ཀྱི་ཕྱིར་དགེ་འདུན་གྱི་འབྲས་རིན་གྱིས་ཉོ་བ་ལ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འདོད་པ་མེད་པར་ཉེས་བྱས་ཀྱི་སྤྱོད་པ་ལྷན་ཅིག་སྤྱོད་པ་ལ་དགའ་སྟོན་མ་ཡིན་པ་ལ་ཐོབ་པའོ། །

[Block 4424]
དེ་བས་ན་མི་འཇུག་པར་གྱུར་པ་རྣམས་ཀྱི་སླད་དུ་ཚིག་འདིའོ། །

[Block 4425]
ཆོས་དང་མི་ལྡན་པའི་དོན་ལ་ཐམས་ཅད་ཀྱིས་རང་གི་དོན་ནམ་གཞན་གྱི་དོན་དུ་འདོད་པ་མེད་པར་སྤྱོད་པ་ལྷན་ཅིག་སྤྱོད་པ་མི་བྱེད་པའོ། །

[Block 4426]
ཆོས་དང་ལྡན་པ་རྗེས་སུ་གནང་བ་ཉིད་འདི་ལས་གཞན་ལ་ཞེས་བྱ་བ་འདིར་གནས་པར་བྱའོ། །

[Block 4427]
ཁྱིམ་པ་ཉོར་གཞུག་གོ། །

[Block 4428]
མེད་ན་ལན་གསུམ་གྱི་བར་དུ་ཚིག་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་འདི་ལ་ཆོ་ག་འདིས་ཉོ་བ་འམ། འཚོང་བ༌[^3034]འདི་འདིར་བྱ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 4429]
གལ་ཏེ་དེ་ཉིད་ཀྱི་ན་འཐེབ་དང་བཅས་པར་རོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དགེ་འདུན་དབང་བའི༌[^3035]འབྲས་ཀྱི་སོ་བ་གང་ཡིན་པ་ལས།

[Block 4430]
གལ་ཏེ་དེ་ཉིད་ཀྱི་དགེ་འདུན་གྱི་བཤོས་ཀྱི་ཕྱིར་ཉོ་བར་བྱེད་ན་དེ་ནས་དེས་དེ་ལ་འཐེབ་དང་བཅས་པར་བསྐྱེད་དེ་སྦྱིན་པར་བྱའི༌[^3036]རིན་ཐང་མཉམ་ཏེ༌[^3037]སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4431]
ཟད་ན་དགེ་འདུན་གྱིས་ཉོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འབྲས་སོ་མ༌[^3038]ཟད་ན་སྐབས་ཉིད་ཀྱི་ཕྱིར་ཉོ་བར་བྱའོ། །

[Block 4432]
སར་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱིས་ཉོ་བར་བྱའོ། །

[Block 4433]
གལ་ཏེ་སྲོག་ཆགས་མེད་ན་རྙིང་པ་བཙོང་བར་བྱའོ། །

[Block 4434]
རིན་ཐང་མི་གདབ་པོ་ཞེས་བྱ་བ་ནི་འདིའི་རིན་ཐང་འདིའོ་ཞེས་ཉོ་བར་མི་འདོད་པ་འམ་ཉོ་བར་འདོད་པ་རང་ཉིད་ཀྱིས་མི་བྱ་བའི་དོན་ཏོ། །

[Block 4435]
པ་ཎ་ལ་སོགས་པ་དང་འབྲེལ་པའི་སྤྱོད་པ་འདི་ལ་སོགས་པ་སྔར་དང་འབྲེལ་པར་རིག་པར་བྱའོ། །

[Block 4436]
གཞན་ནི་འདི་དང་འབྲེལ་པའོ། །

[Block 4437]
ཁྱིམ་པའི་ཉོ་ཚོང་དག་ཏུ་ལག་གཞུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་པ་ཎ་ལ་སོགས་པ་སྤྱོད་པས་ཁྱིམ་པ་མ་ཡིན་པ་རྣམས་ཀྱི་ཉོ་བ་ལ་སོགས་པ་རྣམས་ལ་ཡང་ལག་གཞུག་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4438]
འོ་ན་རིན་ཐང་ཡོད་པ་ལ་དགེ་སློང་གིས་ཆོས་གོས་ལ་སོགས་པ་དག་ཇི་ལྟར་ཉོ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་པ་ཉོར་གཞུག་གོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4439]
ཁྱིམ་པ་མེད་ན་དེའི་ཚེ་སུས་ཉོ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་མེད་ན་ལན་གསུམ་གྱི་བར་དུ་ཚིག་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་ཁྱིམ་པ་མེད་ན་དེའི་རིན་ཐང་ངེས་པར་གཅད་པར༌[^3039]བྱ་ཞིང་དེ་ནས་ལན་གསུམ་གྱི་བར་དུ་དྲི་བའི་ཚིག་བརྗོད་པར་བྱ་སྟེ། རིན་འདི་ཙམ་གྱིས་བྱིན་ཅིག་ཅེས་ལན་གསུམ་གྱི་བར་དུ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4440]
ཟོང་ལ་རྩེག་པ་ནི་གཞན་གྱི་དོན་དུ་ཡང་མི་བྱ་སྟེ། དཀོན་མཆོག་གསུམ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ལ། ཟོང་ཞེས་བྱ་བ་ནི་ཀ་ཀ་ནི་དང་བ་ར་ཏ་ཀ་ལ༌[^3040]སོགས་པའོ། །

[Block 4441]
རྩེག་པ་ཞེས་བྱ་བ་ནི་ཉོ་བའི་ཚེ་ན་ཅུང་ཟད་ཅུང་ཟད་བསྐྱེད་པ་དང་། འཚོང་བར་བྱེད་པའི་དུས་ན་ཅུང་ཟད་འབྲིད་པ་སྟེ། དེ་ནི་གཞན་གྱི་དོན་དུ་ཡང་མི་བྱ་ན་རང་གི་དོན་དུ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། འདི་ནི་འགའ་ཞིག་ཏུ་དཀོན་མཆོག་གསུམ་སྤངས་ནས་བསྐྱེད་པར་བྱ་ཞེས་བྱ་བའོ། །

[Block 4442]
དཀོན་མཆོག་གསུམ་གྱི་དོན་དུ་ནི། དེ་བྱེད་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4443]
གཏའ་གཞུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གཏའ་མ་ཉིད་ནི་གཏའ་མ་སྟེ། གལ་ཏེ་དེ་ཁོ་ན་ཉིད་མ་ཡིན་ན། བདག་གིས་འདི་སྦྱིན་པར་བྱ་སྟེ། འདི་གཏའ་ཞེས་བྱ་བ་རྫས་སྦྱིན་པ་ནི་འདིའི་བྱེད་པའོ། །

[Block 4444]
འདིར་གཞུང་ནི་དྲུག་སྡེ་རྣམས་ཡལ་ཟུག་འཁྲ་ཞིང་ལྷུང་བཟེད་ལ་སོགས་གཏར་འཇུད་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་གི་ཡལ་ཟུག་འཁྲ་ཞིང་གཏའ་གཞུག་པར་མི་བྱའོ། །

[Block 4445]
གལ་ཏེ་དགེ་སློང་ཡལ་ཟུག་འཁྲ་ཞིང་གཏའ་འཇུག་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4446]
དགེ་འདུན་གྱི་རྫས་དེ་སྤོགས་པ་ལ་དགེ་འདུན་གྱི་ལས་བྱེད་པ་ལ་གཏད་དོ་ཞེས་བྱ་བ་ལ་རྫས་དེ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་རྫས་སོ། །

[Block 4447]
སྤོགས་པ་ལ་ཞེས་བྱ་བ་ནི་ཉོ་བ་ལ་སོགས་པའི་སྤྱོད་པས་དགེ་འདུན་ལ་རྙེད་པ་བསྒྲུབ་བྱ་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་ཡིན་པ་དེ་ལ་དབྱིག་གཏད་པར་བྱའོ། །

[Block 4448]
ཅི་རང་གི་དེ་གཏད་པར་བྱ་འམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་དགེ་འདུན་གྱི་ལས་བྱེད་པ་ལ་གཏད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དམ་གཞག་པ༌[^3041]ལ་སོགས་པ་ལ་དེ་གཏད་པ་རྗེས་སུ་བསྒྲུབ་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4449]
འདི་བརྗོད་པར་བྱ་སྟེ། རྒན་རབས་རྒན་རབས་ལ་མ་ཞུས་པར་དགེ་འདུན་གྱི་དོན་དུ་བརྩོན་པར་མི་བྱའོ། །

[Block 4450]
དེའི་ཚིག་ཡི་གེར་བྲི་བའི་དམ་གཞག་ལ་ནན་ཏན་བྱའོ་ཞེས་བྱ་བ་ནི་དུས་ག་གེ་མོ་ཞིག་གི༌[^3042]ཚེ་འདི་ཙམ་ཞིག་གཏད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ། གང་དུ་ཡི་གེར་བྲི་བའི་དམ་གཞག་གཏད་པ་འདི་ལ་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
