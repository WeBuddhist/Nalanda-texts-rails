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
ཟིན་པ་རྣམས་ནི་དུ། མ་ཟིན་པ་རྣམས་ནི་དུ་ཞེ་ན། མ་ཟིན་དགུ། བརྒྱད་པོ་དེ་དག་རྣམས་དང་སྒྲ། །སེམས་ཀྱི་ཁམས་བདུན་དང་ཆོས་ཀྱི་ཁམས་དང་།

[Block 352 [VERSE]]
སྒྲའི་ཁམས་རྣམས་ནི་མ་ཟིན་པའོ།[^126] །
དགུ་པོ་གཞན་ནི་རྣམ་པ་གཉིས། །

[Block 353]
ཟིན་པ་དག་ཀྱང་ཡིན་མ་ཟིན་པ་དག་ཀྱང་ཡིན་ཏེ། དེ་ལ་མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་ད་ལྟར་བྱུང་བ་རྣམས་ནི་ཟིན་པ་ཡིན་ནོ། །

[Block 354]
འདས་པ་དང་མ་འོངས་པ་རྣམས་ནི་མ་ཟིན་པ་ཡིན་ནོ། །

[Block 355]
གཟུགས་དང་། དྲི་དང་། རོ་དང་། རེག་བྱའི་ཁམས་ད་ལྟར་བྱུང་བ་དབང་པོ་དང་ཐ་མི་དད་པ་རྣམས་ནི་ཟིན་པ་ཡིན་ནོ། །

[Block 356]
གཞན་དག་ནི་མ་ཟིན་པ་རྣམས་སོ། །

[Block 357]
ཟིན་པ་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། ཕན་པ་དང་གནོད་པ་དག་གིས་ཕན་ཚུན་མཐུན་པར་བྱེད་པའི་ཕྱིར་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱི་རྟེན་གྱི་དངོས་པོར་ཉེ་བར་བཟུང་བ་སྟེ། འཇིག་རྟེན་ན་སེམས་པ་དང་བཅས་པ་ཞེས་བརྗོད་པ་གང་ཡིན་པའོ། །

[Block 358 [HEADING]]
#### འབྱུང་བ་ལས་གྱུར་པ། ^1-18-9-0

[Block 359]
འབྱུང་བའི་རང་བཞིན་དུ། འབྱུང་བ་ལས་གྱུར་པ་དུ་ཡིན་ཞེ་ན། རེག་བྱ་རྣམ་པ་གཉིས་ཡིན་ཏེ། འབྱུང་བ་དང་། འབྱུང་བ་ལས་གྱུར་པའོ། །

[Block 360]
དེ་ལ༌[^127]འབྱུང་བ་དག་ནི་བཞིའོ། །

[Block 361]
འབྱུང་བ་ལས་གྱུར་པ་ནི་འཇམ་པ་ཉིད་ལ་སོགས་པ་འབྱུང་བ་དག་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 362]
ལྷག་མ་གཟུགས་ཅན་དགུ་པོ་ནི་འབྱུང་གྱུར༌[^128]ཏེ། དབང་པོ་ལྔའི་ཁམས་དག་དང་ཡུལ་བཞིའོ། །

[Block 363]
ཆོས་ཁམས་ཕྱོགས་གཅིག་ཀྱང་། འབྱུང་བ་ལས་གྱུར་པ་སྟེ། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཞེས་བྱའོ།[^129] །

[Block 364]
ལྷག་མ་རྣམས་ནི་གཉིས་ཀ་མ་ཡིན་པའོ། །

[Block 365 [HEADING]]
#### བསགས་པ། ^1-18-10-0

[Block 366]
བསགས་པ་རྣམས་ནི་དུ། བསགས་པ་མ་ཡིན་པ་རྣམས་ནི་དུ་ཞེ་ན། གཟུགས་ཅན་བཅུ་ནི་བསགས་པའོ། །

[Block 367]
དབང་པོའི་ཁམས་ལྔ་དང་ཡུལ་ལྔ་དག་ནི་རྡུལ་ཕྲ་རབ་འདུས་པ་ཡིན་པའི་ཕྱིར་བསགས་པ་དག་གོ། །

[Block 368 [HEADING]]
#### གཅོད་པར་བྱེད་པ་དང་གཅད་པར་བྱ་བ། ^1-18-11-0

[Block 369]
ཁམས་བཅོ་བརྒྱད་པོ་འདི་དག་ལས་གཅོད་པར་བྱེད་པ་ནི་གང་གཅད་པར༌[^130]བྱ་བ་ནི་གང་། སྲེད་པར་བྱེད་པ་ནི་གང་། བསྲེག་པར་བྱ་བ་ནི་གང་། འཇལ་བར་བྱེད་པ་ནི་གང་། གཞལ་བར་བྱ་བ་ནི་གང་ཞེ་ན།

[Block 370 [VERSE]]
གཅོད་བྱེད་གཅད་པར༌[^131]བྱ་བ་ཉིད། །
ཕྱི་རོལ་གྱི་ནི་ཁམས་བཞི་ཡིན། །

[Block 371]
གཟུགས་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་ཞེས་བྱ་བ་སྟེ། དགྲ་སྟ་དང་། ཤིང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 372]
གཅོད་པ་ཡང་འདུས་པའི་རྒྱུན་འབྲེལ་བར་འབྱུང་བ་ཅན་རྣམ་པར་འབྱེད་པ་སྐྱེད་པའོ། །

[Block 373]
དབང་པོ་རྣམས་ནི་གཅད་པར༌[^132]བྱ་བ་མ་ཡིན་ཏེ། གཉིས་སུ་བྱར་མེད་པའི་ཕྱིར་རོ། །

[Block 374]
གཅོད་པར་བྱེད་པ་ཡང་མ་ཡིན་ཏེ། ནོར་བུའི་འོད་བཞིན་དུ་དང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 375]
ཇི་ལྟར་གཅོད་བྱེད་གཅད་པར་བྱ་བ་ཉིད༌[^133]ཕྱི་རོལ་གྱི་ཁམས་བཞི་ཡིན་པ་ལྟར། དེ་བཞིན་བསྲེག་བྱ་འཇལ་བྱེད་པའོ། །

[Block 376]
དེ་དག་ཉིད་བསྲེག་པར་བྱ་བ་ཡིན་ལ། དེ་དག་ཉིད་འཇལ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 377]
དབང་པོ་རྣམས་ནི་མ་ཡིན་ཏེ། དང་བའི་ཕྱིར་རོ། །

[Block 378]
སྒྲ་ཡང་མ་ཡིན་ཏེ། ཆད་པའི་ཕྱིར་རོ། །

[Block 379]
བསྲེག༌[^134]དང་གཞལ་ལ༌[^135]མི་མཐུན་སྨྲ། །ཁ་ཅིག་ན་རེ་ཁམས་བཞི་པོ་སྲེག་པར་བྱེད་པ་ཡང་ཡིན་ལ་གཞལ་བར་བྱ་བ༌[^136]ཡང་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 380 [HEADING]]
#### རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ། ^1-18-12-0

[Block 381]
རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའི་ཁམས་ནི་དུ། རྒྱས་པ་ལས་བྱུང་བ་རྣམས་ནི་དུ། རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་རྣམས་ནི་དུ། རྫས་དང་ལྡན་པ་རྣམས་ནི་དུ། སྐད་ཅིག་མ་རྣམས་ནི་དུ་ཞེ་ན། སྨྲས་པ།

[Block 382 [VERSE]]
རྣམ་པར༌[^137]སྨིན༌[^138]ལས་སྐྱེས་པ་དང་། །
རྒྱས་ལས་བྱུང་བ་ནང་གི་ལྔ། །

[Block 383]
མིག་ལ་སོགས་པ་ལྔ་པོ་དག་ནི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་ཡང་ཡིན་ལ། རྒྱས་པ་ལས་བྱུང་བ་ཡང་ཡིན་ནོ། །

[Block 384]
རྒྱུ་མཐུན་པར༌[^139]བྱུང་བ་ལས༌[^140]ནི་མེད་དེ། དེ་དག་ལས་མ་གཏོགས་པའི་རྒྱུ་མཐུན་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 385]
དེ་ལ་རྣམ་པར་སྨིན་པའི་རྒྱུ་ལས་སྐྱེས་པ་ནི། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའོ། །

[Block 386]
ཟས་དང་ལེགས་པར་བྱ་བ་དང་། ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་དག་གིས་རྒྱས་པར་བྱས་པ་རྣམས་ནི་རྒྱས་པ་ལས་བྱུང་བ་དག་གོ། །

[Block 387]
སྒྲ་ནི་རྒྱས་པ་ལས་བྱུང་བ་དང་། རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་ཡོད་ཀྱི།

[Block 388 [VERSE]]
[^141]སྒྲ་ནི་རྣམ་སྨིན་ལས་སྐྱེས་མིན། །
རང་གི་འདོད་དགུར་འབྱུང་བའི་ཕྱིར། །
[^142]རྒྱུ་མཐུན༌[^143]ལས་བྱུང༌[^144]རྣམ་སྨིན་སྐྱེས། །

[Block 389]
ཐོགས་པ་མེད་པ༌[^145]བརྒྱད། སེམས་ཀྱི་ཁམས་བདུན་པོ་དག་དང་ཆོས་ཀྱི་ཁམས་ཏེ་སྐལ་པ་མཉམ་པ་དང་། ཀུན་དུ་འགྲོ་བའི་རྒྱུས་བསྐྱེད་པ་རྣམས་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དག་གོ། །

[Block 390]
རྣམ་པར་སྨིན་པའི་རྒྱུས་བསྐྱེད་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དག་གོ། །
--- END BLOCKS ---
