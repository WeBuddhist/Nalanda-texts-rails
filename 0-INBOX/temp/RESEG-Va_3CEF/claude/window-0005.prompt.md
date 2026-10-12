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

[Block 381]
གཞན་གྱི་དབང་ནི་ཡོངས་སུ་ཤེས་པར་བྱ་བ་དང་སྤང་བའོ། །

[Block 382]
ཡོངས་སུ་གྲུབ་པ་ནི་ཡོངས་སུ་ཤེས་པར་བྱ་བ་དང་། ཐོབ་པར་མངོན་སུམ་དུ་བྱའོ། །

[Block 383]
དེ་ལྟར་འདིར་ཡོངས་སུ་ཤེས་པར་བྱ་བ་དང་། སྤང་བར་བྱ༌[^158]བ་དང་། མངོན་སུམ་དུ་བྱས་པས་ལམ་གྱི་བདེན་པ་རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །

[Block 384 [HEADING]]
### རགས་པ་དང་ཕྲ་བའི་དེ་ཁོ་ན། ^3-5-0

[Block 385]
རགས་པ་དང་ཕྲ་བའི་དེ་ཁོ་ན་ནི་ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདེན་པའོ། །

[Block 386]
དེ་རྩ་བའི་དེ་ཁོ་ནར་ཇི་ལྟར་རིག་པར་བྱ་ཞེ་ན།

[Block 387 [VERSE]]
བརྟགས་པ་དང་ནི་ཤེས་པ་དང་། །
དེ་བཞིན་བརྗོད་པ་རགས་པ་ཡིན། །

[Block 388]
ཀུན་རྫོབ་ནི་རྣམ་པ་གསུམ་སྟེ། བརྟགས་པའི་ཀུན་རྫོབ་དང་། ཤེས་པའི་ཀུན་རྫོབ་དང་། བརྗོད་པ་ཡང་དག་པའི་ཀུན་རྫོབ་བོ། །

[Block 389]
དེས་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཉིད་དེ་རྩ་བའི་དེ་ཁོ་ནར་གོ་རིམས་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 390]
དམ་པའི་དོན་ནི་གཅིག་པུའོ། །

[Block 391]
དོན་དམ་པའི་བདེན་པ་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་གཅིག་པུར་རིག་པར་བྱའོ། །

[Block 392]
དེ་ཡང་ཇི་ལྟར་དོན་དམ་པ་ཡིན་ཞེ་ན།

[Block 393 [VERSE]]
དོན་དང་ཐོབ་དང་སྒྲུབ༌[^159]པ་ནི། །
དོན་དམ་རྣམ་པ་གསུམ་དུ་འདོད། །

[Block 394]
དོན་དམ་པ་ནི་དེ་བཞིན་ཉིད་དེ་ཡེ་ཤེས་དམ་པའི་དོན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 395]
ཐོབ་པར་བྱ་བའི་དོན་དམ་པ་ནི་མྱ་ངན་ལས་འདས་པ་སྟེ་དོན་གྱི་དམ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 396]
སྒྲུབ་པ་དོན་དམ་པ་ནི་ལམ་སྟེ་དེའི་དོན་ནི་དམ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 397]
འདུས་མ་བྱས་དང་འདུས་བྱས་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་དུ་ཇི་སྐད་བརྗོད་ཅེ་ན།

[Block 398 [VERSE]]
འགྱུར་མེད་ཕྱིན་ཅི་མ་ལོག་པ། །
ཡོངས་སུ་གྲུབ་པ་རྣམ་པ་གཉིས། །

[Block 399]
འདུས་མ་བྱས་ནི་འགྱུར་བ་མེད་པར་ཡོངས་སུ་གྲུབ་པས་ཡོངས་སུ་གྲུབ་པའོ། །

[Block 400]
འདུས་བྱས་འདི༌[^160]ལམ་གྱིས་བསྡུས་པ་སྟེ། ཕྱིན་ཅི་མ་ལོག་པས་ཡོངས་སུ་གྲུབ་པ་སྟེ། ཤེས་བྱའི་དངོས་པོ་ལ་ཕྱིན་ཅི་ལོག་མེད་པའི་ཕྱིར་རོ། །

[Block 401 [HEADING]]
### གྲགས་པའི་དེ་ཁོ་ན། ^3-6-0

[Block 402]
གྲགས་པ་དེ་ཁོ་ན་རྩ་བའི་དེ་ཁོ་ན་ལ་བློ་ཇི་ལྟར་རྣམ་པར་གཞག་ཅེ་ན། གྲགས་པའི་དེ་ཁོ་ན་ནི་རྣམ་པ་གཉིས་ཏེ། འཇིག་རྟེན་གྱི་གྲགས་པ་དང་། རིགས་པའི་གྲགས་པའོ། །

[Block 403]
དེ་ལ། གཅིག་གིས་འཇིག་རྟེན་གྲགས་པ་སྟེ། །ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཏེ། འཇིག་རྟེན་པ་ཐམས་ཅད་ཀྱི་བརྡ་ལ་འདྲིས་པའི་རྗེས་སུ་ཞུགས་པའི་བློས་དངོས་པོ་གང་ལ་འདི་ནི་ས་ཡིན་གྱི་མེ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དང་། འདི་ནི་གཟུགས་ཡིན་གྱི་སྒྲ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པར་ལྟ་བ་མཐུན་པ་ཡིན་ནོ། །

[Block 404]
གསུམ་གྱིས་རིགས་པའི་གྲགས་པའོ། །

[Block 405]
གང་ཟག་དམ་པ་རིགས་པའི༌[^161]དོན་ལ་མཁས་པ་རྟོག་གེ་པ་སྤྱོད་ཡུལ་ཅན་དག་ཚད་མ་གསུམ་ལ་བརྟེན་ནས་འཐད་པས་སྒྲུབ་པའི་རིགས་པས་གྲགས་པའི་དངོས་པོའོ། །

[Block 406 [HEADING]]
### རྣམ་པར་དག་པའི་སྤྱོད་ཡུལ་གྱི་དེ་ཁོ་ན། ^3-7-0

[Block 407]
རྣམ་པར་དག་པའི་སྤྱོད་ཡུལ་གྱི་དེ་ཁོ་ན་ཉིད་རྣམ་པ་གཉིས་ཏེ། ཉོན་མོངས་པའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཡེ་ཤེས་ཀྱི་སྤྱོད་ཡུལ་དང་། ཤེས་བྱའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཡེ་ཤེས་ཀྱི་སྤྱོད་ཡུལ་ལོ། །

[Block 408 [VERSE]]
རྣམ་དག་སྤྱོད་ཡུལ་རྣམ་གཉིས་ཏེ། །
གཅིག་པུ་ཁོ་ནར་བརྗོད་པ་ཡིན། །

[Block 409]
ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་དུ་བརྗོད་དེ་ངོ་བོ་ཉིད་གཞན་ནི་རྣམ་པར་དག་པའི་ཡེ་ཤེས་རྣམ་པ་གཉིས་ཀྱི་སྤྱོད་ཡུལ་མ་ཡིན་ནོ། །

[Block 410 [HEADING]]
### བསྡུ་བའི་དེ་ཁོ་ན། ^3-8-0

[Block 411]
བསྡུ་བའི་དེ་ཁོ་ན་རྩ་བའི་དེ་ཁོ་ནར་ཇི་ལྟར་རིག་པར་བྱ་ཞེ་ན། རྒྱུ་དང་རྣམ་པར་རྟོག་པ་དང་། །མིང་ནི་རྣམ་པ་གཉིས་སུ་བསྡུ།[^162] །ཅི་རིགས་སུ་སྦྱར་རོ། །

[Block 412]
དངོས་པོ་ལྔ་ལས་བརྩམས་ཏེ། རྒྱུ་དང་རྣམ་པར་རྟོག་པ་གཉིས་ནི་གཞན་གྱི་དབང་དུ་བསྡུའོ། །

[Block 413 [VERSE]]
མིང་ནི་ཀུན་བརྟགས་པར་བསྡུའོ། །
ཡང་དག་ཡེ་ཤེས་རབ་ཁོ་ན། །
གཅིག་པུ་ཁོ་ནས༌[^163]བསྡུས་པ་ཡིན། །

[Block 414]
དེ་བཞིན་ཉིད་དང་ཡང་དག་པའི་མཐའི་ཡེ་ཤེས་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ཀྱིས་བསྡུས་སོ། །

[Block 415 [HEADING]]
### རབ་ཏུ་དབྱེ་བའི་དེ་ཁོ་ན། ^3-9-0

[Block 416]
རབ་ཏུ་དབྱེ་བའི་དེ་ཁོ་ན་རྩ་བའི་དེ་ཁོ་ནར་ཇི་ལྟར་རིག་པར་བྱ་ཞེ་ན། རབ་ཏུ་དབྱེ་བའི་དེ་ཁོ་ན༌[^164]རྣམ་པ་བདུན་ཏེ། འཇུག་པའི་དེ་ཁོ་ན་དང་། མཚན་ཉིད་ཀྱི་དེ་ཁོ་ན་དང་། རྣམ་པར་རིག་པའི་དེ་ཁོ་ན་དང་། [^165]གནས་པའི་དེ་ཁོ་ན་དང་། ལོག་པར་སྒྲུབ་པའི་དེ་ཁོ་ན་དང་། རྣམ་པར་དག་པའི་དེ་ཁོ་ན་དང་། ཡང་དག་པར༌[^166]སྒྲུབ་པའི་དེ་ཁོ་ན་སྟེ།

[Block 417]
དགོངས་པ་ངེས་པར་འགྲེལ་པའི་མདོ་ལས།

[Block 418]
དེ་བཞིན་ཉིད་རྣམ་པ་བདུན་འབྱུང་བ་གང་ཡིན་པ་དེ་དག་ཉིད་དོ། །

[Block 419]
དེ་ལ། འཇུག༌[^167]དེ་ཁོ་ན་རྣམ་པ་གཉིས། །རྩ་བའི་དེ་ཁོ་ན་ཀུན་བརྟགས་པ་དང་། གཞན་གྱི་དབང་གི་མཚན་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 420]
འཇུག་པའི་དེ་ཁོ་ན་ཇི་ལྟ་བ་བཞིན་དུ། གནས་པ་དང་ནི་ངན་པར་ཞུགས། །གནས་པ་དང་ལོག་པར་སྒྲུབ་པའི་དེ་ཁོ་ན་ཡང་དེ་བཞིན་དུ་རྩ་བའི་དེ་ཁོ་ན་རྣམ་པ་གཉིས་སུ་རིག་པར་བྱའོ། །

[Block 421 [VERSE]]
མཚན་ཉིད་རྣམ་པར་རིག་དང་དག །
ཡང་དག་སྒྲུབ་པ་གཅིག་པུའོ། །

[Block 422]
མཚན་ཉིད་ཀྱི་དེ་ཁོ་ན་ལ་སོགས་པ་བཞི་ནི་རྩ་བའི་དེ་ཁོ་ན་གཅིག་སྟེ། ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་དོ། །

[Block 423 [HEADING]]
### མཁས་པའི་དེ་ཁོ་ན། ^3-10-0

[Block 424 [VERSE]]
མཁས་དེ་ཁོ་ན་རྣམ་བཅུ་ནི། །
བདག་ཏུ་ལྟ་བའི་གཉེན་པོའོ། །

[Block 425]
ཞེས་གསུངས་ན་ཕུང་པོ་ལ་སོགས་པ་ལ་བདག་ཏུ་ལྟ་བ་རྣམ་པ་བཅུ་པོ་དེ་དག་ཇི་ལྟ་ཞེ་ན།

[Block 426 [VERSE]]
གཅིག་དང་རྒྱུ་དང་ཟ་བ་དང་། །
བྱེད་པ་དང་ནི་དབང་སྒྱུར་དང་། །
བདག་པོའི་དོན་དང་རྟག་པ་དང་། །
ཉོན་མོངས་པ་དང་དག་པའི་གནས། །

[Block 427 [VERSE]]
རྣལ་འབྱོར་ཅན་དང་མ་གྲོལ་གྲོལ། །
འདི་དག་ལ་ནི་བདག་ཏུ་ལྟ། །

[Block 428]
བདག་མེད་པ་ལ་འཛིན་པ་རྣམ་པ་འདི་བཅུ་ནི། ཕུང་པོ་ལ་སོགས་པ་ལ་འཇུག་སྟེ། དེའི་གཉེན་པོར་མཁས་པ་རྣམ་པ་བཅུའོ། །

[Block 429]
འདི་ལྟ་སྟེ། གཅིག་པུར་འཛིན་པ་དང་། རྒྱུར་འཛིན་པ་དང་། ཟ་བར་འཛིན་པ་དང་། བྱེད་པར་འཛིན་པ་དང་། རང་དབང་དུ་འཛིན་པ་དང་། བདག་པོར་འཛིན་པ་དང་། རྟག་པར་འཛིན་པ་དང་། ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བར་འཛིན་པ་དང་། རྣལ་འབྱོར་ཅན་དུ་འཛིན་པ་དང་། མ་གྲོལ་བ་དང་གྲོལ་བར་འཛིན་པའོ། །

[Block 430]
མཁས་པའི་དེ་ཁོ་ན་རྣམ་པ་བཅུ་པོ་འདི་དག་རྩ་བའི་དེ་ཁོ་ནར་ཇི་ལྟར་འདུས་ཤེ་ན། འདི་ལྟར་ངོ་བོ་ཉིད་གསུམ་དུ་ཕུང་པོ་ལ་སོགས་པ་དེ་དག་འདུས༌[^168]སོ། །ཇི་ལྟར་འདུས་ཤེ་ན།

[Block 431 [VERSE]]
ཀུན་དུ་རྟོག་དང་རྣམ་རྟོག་དོན། །
ཆོས་ཉིད་དོན་གྱིས་དེ་དག་དེར། །

[Block 432]
ཞེས་བྱའོ།[^169] །གཟུགས་ལ་སོགས་པ༌[^170]རྣམ་པ་གསུམ་སྟེ། ཀུན་བརྟགས་པའི་གཟུགས་ནི་གང་གཟུགས་ཀྱི་ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 433]
རྣམ་པར་བརྟགས༌[^171]པའི་གཟུགས་ནི་གང་གཟུགས་ཀྱི་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་དེ།[^172] དེ་ལ་གཟུགས་སུ་རྣམ་པར་རྟོག་པར་བྱེད་དོ། །

[Block 434]
ཆོས་ཉིད་ཀྱི་གཟུགས་ནི་གང་གཟུགས་ཀྱི༌[^173]ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 435]
གཟུགས་ལ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་ཚོར་བ་ལ་སོགས་པའི་ཕུང་པོ་རྣམས་དང་། ཁམས་དང་། སྐྱེ་མཆེད་ལ་སོགས་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 436]
དེ་ལྟར་ན༌[^174]ངོ་བོ་ཉིད་གསུམ་དུ་ཕུང་པོ་ལ་སོགས་པ་འདུས་པའི་ཕྱིར་མཁས་པའི་དེ་ཁོ་ན་རྣམ་པ་བཅུ་ནི་རྩ་བའི་དེ་ཁོ་ན་ཉིད་དུ་བལྟའོ། །

[Block 437]
ཇི་ལྟར་བདག་ཏུ་ལྟ་བ་རྣམ་པ་བཅུའི་གཉེན་པོར་ཕུང་པོ་ལ་སོགས་པ་ལ་མཁས་པ་འདི་བཤད་ན། ཕུང་པོ་ལ་སོགས་པའི་དོན་མ་བཤད་པས་དེ་ད་བརྗོད་པར་བྱ་སྟེ།

[Block 438 [VERSE]]
ཐོག་མ་དུ་མ་ཉིད་དང་ནི། །
བསྡུས་དང་ཡོངས་སུ་ཕྱེ་བའི་དོན། །

[Block 439]
ཐོག་མ་ཁོ་ནར་ཕུང་པོ་དེ་དག་དོན་རྣམ་པ་གསུམ་དུ་རིག་པར་བྱ་སྟེ། དུ་མའི་དོན་ནི༌[^175]གཟུགས་གང་ཅི༌[^176]ཡང་རུང་སྟེ། འདས་པ་དང་མ་འོངས་པ་ཞེས་རྒྱ་ཆེར་འབྱུང་བའོ། །

[Block 440]
བསྡུས་པའི་དོན་ནི་དེ་དག་ཐམས་ཅད་གཅིག་ཏུ་བསྡུས་ཏེ་ཞེས་འབྱུང་བའོ། །

[Block 441]
ཡོངས་སུ་ཕྱེ་བའི་དོན་ནི་གཟུགས་ལ་སོགས་པའི་མཚན་ཉིད་ཐ་དད་དུ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 442]
ཕུང་པོའི་དོན་ནི་སྤུངས་པའི་དོན་ཏེ། དེ་ལྟར་འཇིག་རྟེན་ན་སྤུངས་པའི་དོན་མཐོང་ངོ་། །

[Block 443 [VERSE]]
འཛིན་དང་གཟུང་དང་དེ་འཛིན་པ། །
ས་བོན་དོན་ཏེ་གཞན་དུ་འདོད། །

[Block 444]
གཞན་གང་ཞེ་ན། ཁམས་སོ། །

[Block 445]
དེ་ལ་འཛིན་པའི་ས་བོན་གྱི་དོན་ནི་མིག་གི་ཁམས་ལ་སོགས་པའོ། །

[Block 446]
གཟུང་བའི་ས་བོན་གྱི་དོན་ནི་གཟུགས་ཀྱི་ཁམས་ལ་སོགས་པའོ། །

[Block 447]
དེ་འཛིན་པའི་ས་བོན་གྱི་དོན་ནི་མིག་གི་རྣམ་པར་ཤེས་པའི་ཁམས་ལ་སོགས་པའོ། །

[Block 448 [VERSE]]
ཚོར་དང་དོན་རྣམས་ཡོངས་གཅོད་ཀྱི། །
ཉེར་སྤྱོད་འབྱུང་སྒོ་གཞན་ཡིན་ནོ། །

[Block 449]
གཞན་གང་ཡིན་ཞེ་ན། སྐྱེ་མཆེད་དོ། །

[Block 450]
དེ་ལ་ནང་གི་སྐྱེ་མཆེད་དྲུག་པོ་དག་ནི་ཚོར་བ་ཉེ་བར་སྤྱོད་པའི་སྐྱེ་བའི་སྒོའི་ཕྱིར་རོ། །

[Block 451]
ཕྱིའི་དྲུག་པོ་དག་ནི་དོན་ཡོངས་སུ་སྤྱོད་པའི་ཉེ་བར་སྤྱོད་པའི་སྐྱེ་བའི་སྒོའི་ཕྱིར་རོ། །

[Block 452]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་ནི།

[Block 453 [VERSE]]
རྒྱུ་དང་འབྲས་བུ་རྩོལ་བ་ལ། །
སྒྲོ་འདོགས་མེད་ཅིང་སྐུར་འདེབས་མེད། །

[Block 454]
རྒྱུ་དང་འབྲས་བུ་དང་བྱེད་པ་རྣམས་ལ་སྒྲོ་འདོགས་པ་མེད་པ་དང་། སྐུར་པ་འདེབས་པ་མེད་པའི་དོན་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་དོན་ཏོ།[^177] །དེ་ལ་རྒྱུ་ལ་སྒྲོ་འདོགས་པ་ནི་འདུ་བྱེད་ལ་སོགས་པའི་མི་མཐུན་པའི་རྒྱུ་ལ་རྟོག་པའི་ཕྱིར་རོ། །

[Block 455]
རྒྱུ་ལ་སྐུར་པ་འདེབས་པ་ནི་རྒྱུ་མེད་པ་ཅན་དུ་རྟོག་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
