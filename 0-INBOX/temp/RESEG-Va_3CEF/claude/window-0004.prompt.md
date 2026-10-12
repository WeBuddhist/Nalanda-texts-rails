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
[Block 301]
བདུན་པ་ལ་ནི་ཐ་དད་པ་མེད་པའི་དོན་དུ་རྟོགས་ཏེ། མཚན་མ་མེད་པས་མདོ་ལ་སོགས་པའི་ཆོས་ཀྱི་མཚན་མ་ཐ་དད་པར་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 302]
བརྒྱད་པ་ལ་ནི་བྲི་བ་མེད་ཅིང་འཕེལ་བ་མེད་པའི་དོན་དུ་རྟོགས་ཏེ། མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པས་ཀུན་ནས་ཉོན་མོངས་པའམ། རྣམ་པར་བྱང་བ་ན་ཡང་བྲི་བའམ་འཕེལ་བ་མི་མཐོང་བའི་ཕྱིར་རོ། །

[Block 303]
དབང་རྣམ་པ་བཞི་ནི་རྣམ་པར་མི་རྟོག་པ་ལ་དབང་བ་དང་། ཞིང་ཡོངས་སུ་དག་པ་ལ་དབང་བ་དང་། ཡེ་ཤེས་ལ་དབང་བ་དང་། ལས་ལ་དབང་བའོ། །

[Block 304]
དེ་ལས༌[^124]

[Block 305]
བརྒྱད་པ་ཉིད་ལ་ཆོས་ཀྱི་དབྱིངས་ལ་དབང་བ་དང་པོ་དང་། [^125]འོག་གི་གནས་ཉིད་དུ་རབ་ཏུ་རྟོགས་སོ། །

[Block 306]
དགུ་པ་ལ་ནི་ཡེ་ཤེས་ལ་དབང་བའི་གནས་ཉིད་དུ་རྟོགས་ཏེ། སོ་སོ་ཡང་དག་པར་རིག་པ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 307]
བཅུ་པ་ལ་ནི་ལས་ལ་དབང་བའི་གནས་ཉིད་དུ་རྟོགས་ཏེ། ཇི་ལྟར་བཞེད་པ་བཞིན་དུ་སྤྲུལ་པ་རྣམས་ཀྱིས་སེམས་ཅན་གྱི་དོན་མཛད་པའི་ཕྱིར་རོ། །

[Block 308]
མདོར་བསྡུ་ན།

[Block 309 [VERSE]]
ཉོན་མོངས་པ་ཡི་སྒྲིབ་པ་དང་། །
ཤེས་བྱའི་སྒྲིབ་པ་ཉིད་དུ་བསྟན། །
དེར་ནི་སྒྲིབ་པ་ཐམས་ཅད་དེ། །
དེ་ཟད་ནས་ནི་གྲོལ་བར་འདོད། །

[Block 310]
སྒྲིབ་པ་རྣམ་པ་གཉིས་པོ་འདི་ཟད་ན་སྒྲིབ་པ་ཐམས་ཅད་ལས་གྲོལ་བར་འདོད་དོ། །

[Block 311]
སྒྲིབ་པ་རྣམས་ཀྱི་དོན་བསྡུས་པ་སྟེ། སྒྲིབ་པ་ཆེན་པོ་ནི་ཁྱབ་པ་གང་ཡིན་པའོ། །

[Block 312]
སྒྲིབ་པ་ཆུང་ངུ་ནི་ཉི་ཚེ་བ་གང་ཡིན་པའོ། །

[Block 313]
སྦྱོར་བའི་སྒྲིབ་པ་ནི་ལྷག་པ་གང་ཡིན་པའོ། །

[Block 314]
ཐོབ་པ་ལ་སྒྲིབ་པ་ནི་མཉམ་པ་གང་ཡིན་པའོ། །

[Block 315]
འཐོབ་པ་ཁྱད་པར་ཅན་ལ་སྒྲིབ་པ་ནི་ལེན་པ་དང་སྤོང་བ་གང་ཡིན་པའོ། །

[Block 316]
ཡང་དག་པར་སྦྱོར་བ་ལ་སྒྲིབ་པ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པ་རྣམ་པ་དགུ་གང་ཡིན་པའོ། །

[Block 317]
རྒྱུ་ལ་སྒྲིབ་པ་ནི་དགེ་བ་ལ་སོགས་པ་རྣམ་པ་བཅུ་ལ་སྒྲིབ་པ་གང་ཡིན་པ་སྟེ། རྒྱུའི་དོན་གྱི་སྐབས་ཀྱི་ཕྱིར་རོ། །

[Block 318]
དེ་ཁོ་ན་ལ་འཇུག་པ་ལ༌[^126]སྒྲིབ་པ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་རྣམས་ལ་སྒྲིབ་པ་གང་ཡིན་པའོ། །

[Block 319]
དགེ་བ་བླ་ན་མེད་པ་ལ་སྒྲིབ་པ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་ལ་སྒྲིབ་པ་གང་ཡིན་པའོ། །

[Block 320]
དེ་ཁྱད་པར་དུ་འགྲོ་བ་ལ་སྒྲིབ་པ་ནི་ས་རྣམས་ལ་སྒྲིབ་པ་གང་ཡིན་པའོ། །

[Block 321]
བསྡུས་པའི་སྒྲིབ་པ་ནི་མདོར་བསྡུས་པ་རྣམ་པ་གཉིས་པོ་གང་ཡིན་པའོ། །

[Block 322]
བསྟན་བཅོས་དབུས་དང་མཐའ་རྣམ་པར་འབྱེད་པ་ལས་སྒྲིབ་པའི་ལེའུར་བཅད་པ་ཞེས་བྱ་བ་གཉིས་པའི་འགྲེལ་པའོ།། །།

[Block 323 [HEADING]]
## དེ་ཁོ་ན། ^3-0

[Block 324]
དེ་ཁོ་ནའི་དབང་དུ་མཛད་དེ་གསུངས་པ།

[Block 325 [VERSE]]
རྩ་བ་མཚན་ཉིད་དེ་ཁོ་ན། །
ཕྱིན་ཅི་མ་ལོག་མཚན་ཉིད་དང་། །
འབྲས་བུ་རྒྱུ་ཡི་དེ་ཁོ་ན། །
རགས་པ༌[^127]དང་ནི་ཕྲ་བ༌[^128]དང་། །

[Block 326 [VERSE]]
གྲགས་དང་རྣམ་པར་དག་ཡུལ་དང་། །
བསྡུ་དང་དབྱེ་བའི་མཚན་ཉིད་དང་། །
མཁས་དེ་ཁོ་ན་རྣམ༌[^129]བཅུ་ནི། །
བདག་ཏུ་ལྟ་བའི་གཉེན་པོའོ། །

[Block 327]
ཞེས་བྱ་བ་འདི་དག་ནི་དེ་ཁོ་ན་རྣམ་པ་བཅུ་སྟེ། འདི་ལྟ་སྟེ། རྩ་བའི་དེ་ཁོ་ན་དང་། མཚན་ཉིད་ཀྱི་དེ་ཁོ་ན་དང་། ཕྱིན་ཅི་མ་ལོག་པའི་དེ་ཁོ་ན་དང་། འབྲས་བུ་དང་རྒྱུའི་དེ་ཁོ་ན་དང་། རགས་པ་དང་ཕྲ་བའི་དེ་ཁོ་ན་དང་། གྲགས་པའི་དེ་ཁོ་ན་དང་། རྣམ་པར་དག་པའི་སྤྱོད་ཡུལ་གྱི་དེ་ཁོ་ན་དང་། བསྡུ་བའི་དེ་ཁོ་ན་དང་། རབ་ཏུ་དབྱེ་བའི་དེ་ཁོ་ན་དང་། མཁས་པའི་དེ་ཁོ་ན་སྟེ། རྣམ་པ་བཅུ་པོ་དེ་ཡང་བདག་ཏུ་འཛིན་པ་རྣམ༌[^130]པ་བཅུའི་གཉེན་པོར་རིག་པར་བྱའོ། །

[Block 328]
འདི་ལྟ་སྟེ། ཕུང་པོ་ལ་མཁས་པ་དང་། ཁམས་ལ་མཁས་པ་དང་། སྐྱེ་མཆེད་ལ་མཁས་པ་དང་། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ལ་མཁས་པ་དང་། གནས༌[^131]དང་གནས་མ་ཡིན་པ་ལ་མཁས་པ་དང་། དབང་པོ་ལ་མཁས་པ་དང་། དུས་ལ་མཁས་པ་དང་། བདེན་པ་ལ་མཁས་པ་དང་། ཐེག་པ་ལ་མཁས་པ་དང་། འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་ལ་མཁས་པའོ། །

[Block 329 [HEADING]]
### རྩ་བའི་དེ་ཁོ་ན། ^3-1-0

[Block 330]
དེ་ལ་རྩ་བའི་དེ་ཁོ་ན་ནི་ངོ་བོ་ཉིད་རྣམ་པ་གསུམ་སྟེ། ཀུན་བརྟགས་པ༌[^132]དང་། གཞན་གྱི་དབང་དང་། ཡོངས་སུ་གྲུབ་པ་སྟེ། དེ་ལ་དེ་ཁོ་ན་གཞན་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 331]
དེ༌[^133]ཅིའི་ཕྱིར་འདིར་ངོ་བོ་ཉིད་གསུམ་ལ་དེ་ཁོ་ན་ཞེས་བྱ་བར་འདོད་ཅེ་ན།

[Block 332 [VERSE]]
ངོ་བོ་ཉིད་གསུམ་རྟག་མེད་དང་། །
ཡོད་ཀྱང་ཁོ་ན་མ་ཡིན་དང་། །
ཡོད་དང་མེད་དེ་ཁོ་ན་སྟེ། །
ངོ་བོ་ཉིད་ནི་གསུམ་དུ་འདོད། །

[Block 333]
ཀུན་ཏུ་བརྟགས་པའི་མཚན་ཉིད་ནི་རྟག་ཏུ་མེད་པའོ། །

[Block 334]
དེ་ནི་ཀུན་ཏུ༌[^134]བརྟགས་པའི་ངོ་བོ་ཉིད་ལ་དེ་ཁོ་ན་ཞེས་བྱ་སྟེ། ཕྱིན་ཅི་མ༌[^135]ལོག་པའི་ཕྱིར་རོ། །

[Block 335]
གཞན་གྱི་དབང་གི་མཚན་ཉིད་ནི་ཡོད་ཀྱང་ཡང་དག་པ་མ་ཡིན་ཏེ་འཁྲུལ་པའི་ཕྱིར་རོ། །

[Block 336]
དེ་ལྟ༌[^136]བས་ན་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ལ་དེ་ཁོ་ན་ཞེས་བྱའོ། །

[Block 337]
ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་ནི་ཡོད་པ་དང་མེད་པའི་དེ་ཁོ་ན་སྟེ། དེ་བས་ན་འདི་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ལ་དེ་ཁོ་ནའོ། །

[Block 338 [HEADING]]
### མཚན་ཉིད་ཀྱི་དེ་ཁོ་ན། ^3-2-0

[Block 339]
མཚན་ཉིད་ཀྱི་དེ་ཁོ་ན་གང་ཞེ་ན།

[Block 340 [VERSE]]
འདི་ལ་ཆོས་དང་གང་ཟག་དང་། །
གཟུང་བ་དག་དང་འཛིན་པ་དང་། །
ཡོད་དང་མེད་པར་སྒྲོ་འདོགས་དང་། །
སྐུར་པ་འདེབས་པར་ལྟ་བ་དག །

[Block 341 [VERSE]]
གང་ཤེས་ནས་ནི་མི་འབྱུང་བ། །
དེ་དེ་ཁོ་ནའི་མཚན་ཉིད་དོ། །

[Block 342]
གང་ཤེས་ནས་གང་ཟག་དང་ཆོས་གཉིས་ལ་སྒྲོ་འདོགས་པ་དང་། སྐུར་པ་འདེབས་པར་ལྟ་བ་མི་འབྱུང་བ་དེ་ནི་ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་ཀྱི༌[^137]དེ་ཁོ་ནའི་མཚན་ཉིད་དོ། །

[Block 343]
གང་ཤེས་ནས་གཟུང་བ་དང་། འཛིན་པ་གཉིས་ལ་སྒྲོ་འདོགས་པ་དང་། སྐུར་པ་འདེབས་པར་ལྟ་བ་མི་འབྱུང་བ་དེ་ནི་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ཀྱི་དེ་ཁོ་ནའི་མཚན་ཉིད་དོ། །

[Block 344]
གང་ཤེས་ནས་དངོས་པོ་དང་དངོས་པོ་མེད་པར་སྒྲོ་འདོགས་པ་དང་། སྐུར་པ་འདེབས་པར་ལྟ་བ་མི་འབྱུང་བ་དེ་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ཀྱི་དེ་ཁོ་ནའི་མཚན་ཉིད་དོ། །

[Block 345]
རྩ་བའི་དེ་ཁོ་ན་ལ་མཚན་ཉིད་ཀྱི་དེ་ཁོ་ན་ཕྱིན་ཅི་མ་ལོག་པ་འདི་ནི་མཚན་ཉིད་ཀྱི་དེ་ཁོ་ན་ཞེས་བྱའོ། །

[Block 346 [HEADING]]
### ཕྱིན་ཅི་མ་ལོག་པའི་དེ་ཁོ་ན། ^3-3-0

[Block 347]
ཕྱིན་ཅི་མ་ལོག་པའི་དེ་ཁོ་ན་ནི་རྟག་པ་ལ་སོགས་པར་ཕྱིན་ཅི་ལོག་པའི་གཉེན་པོར་མི་རྟག་པ་དང་། སྡུག་བསྔལ་བ་དང་། སྟོང་པ་དང་། བདག་མེད་པ་ཉིད་དོ། །

[Block 348]
རྩ་བའི་དེ་ཁོ་ན་དེར༌[^138]ཇི་ལྟར་ན་མི་རྟག་པ་ལ་སོགས་པ་ཉིད་རིག་པར་བྱ༌[^139]ཞེ་ན།

[Block 349 [VERSE]]
མི་རྟག་དོན་ནི་མེད་དོན་དང་། །
སྐྱེ་ཞིང་འཇིག་པའི་མཚན་ཉིད་དང་། །
དྲི༌[^140]བཅས་དྲི་མ་མེད་དོན་ཏེ། །
རྩ་བའི་ཁོ་ནར་གོ་རིམས་བཞིན། །

[Block 350]
མི་རྟག་པའི་དོན་ནི་རྣམ་པ་གསུམ་སྟེ། མེད་པའི་དོན་དང་། སྐྱེ་ཞིང་འཇིག་པའི་དོན་དང་། དྲི་མ་དང་བཅས་ཤིང་དྲི་མ༌[^141]མེད་པ་ཉིད་ཀྱི་དོན་ནི་རྩ་བའི་དེ་ཁོ་ནར་ངོ་བོ་ཉིད་གསུམ་པོ་དག་དང་གོ་རིམས་བཞིན་ནོ། །

[Block 351 [VERSE]]
སྡུག་བསྔལ་ལེན་དང་མཚན་ཉིད་དང་། །
འབྲེལ་པ་གཞན་དུ་འདོད་པ་ཡིན། །

[Block 352]
གང་ཟག་དང་ཆོས་ལ་མངོན་པར་ཞེན་པ་ཉེ་བར་ལེན་པའི་ཕྱིར། ཉེ་བར་ལེན་པའི་སྡུག་བསྔལ་བ་དང་། སྡུག་བསྔལ་བ་ཉིད་གསུམ་གྱི་མཚན་ཉིད་ཡིན་པས་མཚན་ཉིད་དང་། སྡུག་བསྔལ་དང་འབྲེལ་པའི་ཕྱིར་འབྲེལ་པ་ཡང་སྟེ། རྩ་བའི་དེ་ཁོ་ན་ཉིད་ཀྱི་ནང་དུ་གོ་རིམས་བཞིན་ནོ། །

[Block 353 [VERSE]]
དངོས་མེད་དེ༌[^142]དངོས་མ་ཡིན་དང་། །
རང་བཞིན་གྱིས་ནི་སྟོང་པར་འདོད། །

[Block 354]
ཀུན་བརྟགས་པའི་མཚན་ཉིད་ནི་རྣམ་པ་གང་གིས་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། དངོས་པོ་མེད་པ་ཉིད་པས་དེའི་སྟོང་པ་ཉིད་དོ། །

[Block 355]
གཞན་གྱི་དབང་གི་མཚན་ཉིད་ནི་ཇི་ལྟར་ཀུན་བརྟགས་པ་དེ་ལྟར་མེད་ཀྱི། ཡེ་ཤེས༌[^143]མེད་པ་ས་ནི་མ་ཡིན་ཏེ། དེ་མ༌[^144]ཡིན་པས་དེའི་སྟོང་པ་ཉིད་དོ། །

[Block 356]
ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་ནི། སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཁོ་ན་ཡིན་པས་རང་བཞིན༌[^145]ཁོ་ནས་དེའི་སྟོང་པ་ཉིད་དོ། །

[Block 357 [VERSE]]
མཚན་ཉིད་མེད་པས་བདག་མེད་དང་། །
དེ་དང་མི་མཐུན་མཚན་ཉིད་དང་། །
རང་གི་མཚན་ཉིད་བསྟན་པ་ཡིན། །

[Block 358]
ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་ནི་མཚན་ཉིད་ཀྱིས་མེད་པའི་ཕྱིར་རོ། །

[Block 359]
མཚན་ཉིད་དེའི་བདག་མེད་པ་ཉིད་དོ། །

[Block 360]
གཞན་གྱི་དབང་གི༌[^146]མཚན་ཉིད་ནི་ཡོད་ཀྱང་ཇི་ལྟར་ཀུན་ཏུ་བརྟགས་པ་བཞིན་དུ་མེད་པས་དེ་དང་མི་མཐུན་པའི་མཚན་ཉིད་ཀྱིས་དེའི་བདག་མེད་པའོ། །

[Block 361]
ཡོངས་སུ་གྲུབ་པ་ནི་ངོ་བོ་ཉིད་ཀྱིས་བདག་མེད་པ་ཉིད་པས་རང་གི་མཚན་ཉིད་ཀྱིས༌[^147]དེའི་བདག་མེད་པའོ། །

[Block 362]
རྩ་བ་དེ་ཁོ་ན་རྣམ་པ་གསུམ་ལ་མི་རྟག་པ་ཉིད་རྣམ་པ་གསུམ་ཡོངས་སུ་བསྟན་ཏེ། མེད་པའི་དོན་མི་རྟག་པ་ཉིད་དང་། སྐྱེ་ཞིང་འཇིག་པ་མི་རྟག་པ་ཉིད་དང་། དྲི་མ་དང་བཅས་ཤིང་དྲི་མ་མེད་པ་མི་རྟག་པ་ཉིད་དོ། །

[Block 363]
སྡུག་བསྔལ་ཉིད་རྣམ་པ་གསུམ་སྟེ། ཉེ་བར་ལེན་པས་སྡུག་བསྔལ་ཉིད་དང་། མཚན་ཉིད་ཀྱིས༌[^148]སྡུག་བསྔལ་ཉིད་དང་། འབྲེལ་པས་སྡུག་བསྔལ་ཉིད་དོ། །

[Block 364]
སྟོང་པ་ཉིད་རྣམ་པ་གསུམ་སྟེ། དངོས་པོ་མེད་པས་སྟོང་པ་ཉིད་དང་། དེ་མ་ཡིན་པས་སྟོང་པ་ཉིད་དང་། ངོ་བོ་ཉིད་ཀྱིས་སྟོང་པ་ཉིད་དོ། །

[Block 365]
བདག་མེད་པ་རྣམ་པ་གསུམ་སྟེ། མཚན་ཉིད་མེད་པས་བདག་མེད་པ་དང་། མི་མཐུན་པའི་མཚན་ཉིད་ཀྱིས་བདག་མེད་པ་དང་། རང་གི་མཚན་ཉིད་ཀྱིས་བདག་མེད་པའོ། །

[Block 366 [HEADING]]
### འབྲས་བུ་དང་རྒྱུའི་དེ་ཁོ་ན། ^3-4-0

[Block 367]
འབྲས་བུ་དང་རྒྱུའི་དེ་ཁོ་ན་ནི་རྩ་བའི་དེ་ཁོ་ན་ཉིད་ལ་སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་བ༌[^149]དང་། འགོག་པ་དང་། ལམ་གྱི་བདེན་པ་ཉིད་དོ། །

[Block 368]
ཇི་ལྟར༌[^150]རྩ་བའི་དེ་ཁོ་ན་རྣམ་པ་གསུམ་ལས་སྡུག་བསྔལ་ལ་སོགས་པའི་བདེན་པ་ཞེས་བྱ་ཞེ་ན། འདི་ལྟར་དེ་མི་རྟག་པ་ལ་སོགས་པའི་མཚན་ཉིད་ཀྱིས་ཏེ། དེའི་ཕྱིར་སྡུག་བསྔལ་བདེན་པར་འདོད། །ཀུན་འབྱུང་བའི་དོན་རྣམ་པ་གསུམ་གྱིས་ཀུན་འབྱུང་བའི་བདེན་པ་སྟེ། ཀུན་འབྱུང་བའི་དོན་རྣམ་པ་གསུམ་ནི།

[Block 369 [VERSE]]
བག་ཆགས་དང་ནི་ཀུན་ནས་འབྱུང་། །
མ་བྲལ་བ་ཡང་དེ་བཞིན་ནོ། །

[Block 370]
བག་ཆགས་ཀྱི༌[^151]ཀུན་འབྱུང་བ་ནི། ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་ལ་མངོན་པར་ཞེན་པའི་བག་ཆགས་སོ། །

[Block 371]
ཀུན་ནས་འབྱུང་བའི་ཀུན་འབྱུང་བ་ནི་ལས་དང་ཉོན་མོངས་པ་རྣམས་སོ། །

[Block 372]
མ་བྲལ་བའི་ཀུན་འབྱུང་ནི་དེ་བཞིན་ཉིད་སྒྲིབ་པ་དང་མ་བྲལ་བའོ། །

[Block 373]
འགོག་པ་རྣམ་པ་གསུམ་གྱིས༌[^152]འགོག་པའི་བདེན་པ་སྟེ་འགོག་པ་རྣམ་པ་གསུམ་མོ། །

[Block 374]
[^153]འགོག་པ་རྣམ་པ་གསུམ་ནི།

[Block 375 [VERSE]]
ངོ་བོ་ཉིད་དང་གཉིས་མི་སྐྱེ། །
དྲི་མ་ཞི་བ་གཉིས་སུ་འདོད། །

[Block 376]
ངོ་བོ་ཉིད་ཀྱིས་མི་སྐྱེ་བ་དང་། གཟུང་བ་དང་འཛིན་པ་གཉིས་མི་སྐྱེ་བ་དང་། དྲི་མ་ཞི་བ་གཉིས་ཀྱང་སྟེ། སོ་སོར་བརྟགས་པའི་འགོག་པ་དང་། དེ་བཞིན་ཉིད་ཅེས་བྱའོ། །

[Block 377]
འདི་ནི་འགོག་པ་རྣམ༌[^154]གསུམ་སྟེ། །འདི་ལྟ་སྟེ། ངོ་བོ་ཉིད་ཀྱིས༌[^155]འགོག་པ་དང་། གཉིས་པོ་འགོག་པ་དང་། རང་བཞིན་གྱིས་འགོག་པའོ། །

[Block 378]
ལམ་གྱི༌[^156]བདེན་པ་རྩ་བའི་དེ་ཁོ་ན་རྣམ་པ་གསུམ་དུ་ཇི་ལྟར་གཞག་ཅེ་ན།

[Block 379 [VERSE]]
[^157] ཡོངས་སུ་ཤེས་དང་སྤང་བ་དང་། །
ཐོབ་པར་མངོན་སུམ་བྱ་བས་ནི། །
ལམ་གྱི་བདེན་པ་ཡང་དག་བཤད། །

[Block 380]
ཀུན་བརྟགས་པ་ནི་ཡོངས་སུ་ཤེས་པར་བྱའོ། །
--- END BLOCKS ---
