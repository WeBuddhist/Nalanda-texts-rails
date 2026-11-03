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
བྱ་ཀ་ལ་པིང་ཀའི་སྒྲ་དབྱངས་བསྒྲགས་པ་ནི་མྱུར་དུ་འགྱུར་བའི་ངང་ཚུལ་ཅན་གྱི་ཕྱིར་རོ། །

[Block 352]
ཚངས་པའི་སྒྲ་དབྱངས་བསྒྲགས་པ་ནི་རྒྱང་རིང་དུ་གྲགས་པའི་ཕྱིར་རོ། །

[Block 353]
ཤང་ཤང་ཏེའུའི་སྒྲ་དབྱངས་སུ་གྲགས་པ༌[^252]ནི་ཐམས་ཅད་དུ༌[^253]གྲུབ་པ་ཐོག་མར་འགྲོ་བའི་བཀྲ་ཤིས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 354]
ལྷའི་དབང་པོའི་དབྱངས་ལྟར་སྙན་པ་ནི་འགལ་བར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 355]
རྔའི་སྒྲ་ནི་བདུད་ཕྱིར་རྒོལ་བ་ཐམས་ཅད་ཕམ་པར་བྱ་བ་ལ་ཐོག་མར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 356]
མ་ཁེངས་པ་ནི་བསྟོད་པས་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 357]
མི་དམའ་བ་ནི་སྨད་པས་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 358]
སྒྲ་ཐམས་ཅད་ཀྱི་རྗེས་སུ་ཞུགས་པ་ནི་རྣམ་པར་བསྒྲུབ་པ་ཐམས་ཅད་དང་། མཚན་ཉིད་རྣམ་པ་ཐམས་ཅད་ཀྱི་རྗེས་སུ་ཞུགས་པའི་ཕྱིར་རོ། །

[Block 359]
ཚིག་ཟུར་ཆག༌[^254]མེད་པ་ནི་བརྗེད་པར་དེ་མི་འབྱིན་པའི་ཕྱིར་རོ། །

[Block 360]
མ་ཚང་བ་མེད་པ་ནི་འདུལ་བའི་བྱ་བ་ལ་དུས་ཐམས་ཅད་དུ་ཉེ་བར་གནས་པའི་ཕྱིར་རོ། །

[Block 361]
མ་ཞུམ་པ་ནི་རྙེད་པ་དང་བཀུར་སྟི་ལ་མི་རྟག་པའི༌[^255]ཕྱིར་རོ། །

[Block 362]
མི་ཞན་པ་ནི་འཇིགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 363]
རབ་ཏུ་དགའ་བ་ནི་བདེ་བ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 364]
ཁྱབ་པ་ནི་རིག་པའི་གནས་ཐམས་ཅད་ལ་མཁས་པའི་རྗེས་སུ་ཞུགས་པའི་ཕྱིར་རོ། །

[Block 365]
ཆུབ་པ་ནི་སེམས་ཅན་རྣམས་ཀྱི་དོན་མཐའ་དག་སྒྲུབ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 366]
རྒྱུན་ཆགས་པ་ནི་རྒྱུན་མི་འཆད་པའི་ཕྱིར་རོ། །

[Block 367]
འབྲེལ་པ་ནི་རྣམ་པ་སྣ་ཚོགས་སུ་གནས་པའི་ཕྱིར་རོ། །

[Block 368]
སྒྲ་ཐམས་ཅད་རྫོགས་པར་བྱེད་པ་ནི་སྒྲ་གཅིག་ལ་སྒྲའི་རྣམ་པར་རིག་པ་དུ་མ་ཉེ་བར་གནས་པའི་ཕྱིར་རོ། །

[Block 369]
དབང་པོ་ཐམས་ཅད་ཚིམ་པར་བྱེད་པ་ནི་གཅིག་གིས་དོན་དུ་མའི་རྣམ་པར་རིག་པ་ཉེ་བར་གནས་པའི་ཕྱིར་རོ། །

[Block 370]
མ་སྨད་པ་ནི་དམ་བཅས་པ་བཞིན་དུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 371]
མི་འགྱུར་བ་ནི་མ་འོངས་པའི་དུས་ན་རབ་ཏུ་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 372]
མ་བརྟབས་པ་ནི་རྟབ་རྟབ་པོར་མི་སྨྲ་བའི་ཕྱིར་རོ། །

[Block 373]
འཁོར་ཀུན་ཏུ་གྲགས་པ་ནི་འཁོར་ཉེ་རིང་ལ་མཚུངས་པར་གྲགས་པའི་ཕྱིར་རོ། །

[Block 374]
རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པ་ནི་འཇིག་རྟེན༌[^256]དོན་དང་། དཔེའི་ཆོས་ཐམས་ཅད་ཀྱི༌[^257]ཡོངས་སུ་གྲུབ་པའི་ཕྱིར་རོ་ཞེས་སློབ་དཔོན་གྱི་མན་ངག་གོ། །།

[Block 375 [HEADING]]
##### ནམ་མཁའ་དང་མཉམ་པ། ^1-1-6-2-0

[Block 376]
བམ་པོ་བཅུ་དྲུག་པ། ད་ནི་རབ་འབྱོར་གང་ཡང་ཁྱོད་ཀྱིས་འདི་སྐད་དུ་ཐེག་པ་དེ་ནི་ནམ་མཁའ་དང་མཉམ་པའོ་ཞེས་སྨྲས་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་ཚིག་གཉིས་པ་བཟུང་སྟེ་བསྟན་ཏོ། །

[Block 377]
ཀུན་བརྟགས་པའི་དངོས་པོ་རྣམས་ནི་རྣམ་པ་ཉི་ཤུ་རྩ་གཅིག་གིས་རྣམ་པར་གཞག་པ་ཡིན་ཏེ། ཐེག་པ་ཆེན་པོ་འདི་ལ་ནི་རྣམ་པར་གཞག་པ་དེ་དག་མེད་པའི་ཕྱིར་ནམ་མཁའ་དང་མཚུངས་པར་རིག་པར་བྱའོ། །

[Block 378]
རྣམ་པ་ཉི་ཤུ་རྩ་གཅིག་ནི་ཕྱོགས་རྣམ་པར་གཞག་པ་དང་། དབྱིབས་དང་། ཁ་དོག་དང་། དུས་དང་། འགྲིབ་ཅིང་འཕེལ་བ་ལ་སོགས་པ་དང་། ཀུན་ནས་ཉོན་མོངས་ཤིང་རྣམ་པར་བྱང་བ་དང་། སྐྱེ་ཞིང་འགག་པ་དང་། དགེ་བ་ལ་སོགས་པ་དང་། མཐོང་ཞིང་ཐོས་པ་ལ་སོགས་པ་དང་། ཤེས་པར་བྱ་བ་ལ་སོགས་པ་དང་། རྣམ་པར་སྨིན་ཅིང་རྣམ་པར་སྨིན་པའི་ཆོས་ཅན་དང་། འདོད་ཆགས་ལ་སོགས་པ་དང་། ཁམས་དང་། རབ་ཏུ་དགའ་བ་ལ་སོགས་པ་བྱང་ཆུབ་སེམས་དཔའི་ས་བཅུ་དང་། དཀར་པོ་རྣམ་པར་མཐོང་བ་དང་། རིགས་ཀྱི་ས་ལ་སོགས་པ་ས་བཅུ་དང་། འཕགས་པའི་གང་ཟག་གི་ས་དང་། གཉིས་དང་། ཆོས་ཀྱི་མདོ་དང་། རྣམ་པར་ཐར་པའི་སྒོ་དང་། གསང་བ་དང་། མི་གསང་བ་ལ་སོགས་པ་དང་། རྙེད་པ་ལ་སོགས་པ་དང་། རབ་ཏུ་བརྗོད་པ་ལ་སོགས་པའོ། །

[Block 379]
དེ་ལ་འགྲིབ་པ་དང་འཕེལ་བ་ནི་རིམ་གྱིས་སོ། །

[Block 380]
འབྲི་བ་ནི་ཆད་པའོ། །

[Block 381]
སྐྱེ་བ་ཞེས་བྱ་བ་ནི་དངོས་པོ་རྣམས་ཐོག་མ་སྐྱེ་བའོ།[^258] །འགག་པ་ནི་སྐད་ཅིག་གཅིག་ལ་འཇིག་པའོ། །

[Block 382]
གནས་པ་ནི་དེ་ལྟར་སྐྱེ་ཞིང་འགག་པའི་ཆོས་རྣམས་ཀྱི་རྒྱུན་མ་ཆད་པའོ། །

[Block 383]
མཐར་ཐུག་པ་ནི་དེའི་རྒྱུན་ཆད་ཅིང་བལྟར་མི་སྣང་བའོ། །

[Block 384]
གནས་པ་ལས་གཞན་དུ་འགྱུར་བ་ཞེས་བྱ་བ་ནི་དེའི་རྒྱུན་སྔ་མ་དང་། ཕྱི་མ་བྱེ་བྲག་ཅན་དུ་གྱུར་པ་དེ་མི་འདྲ་བར་གྱུར་པའོ། ། ཤེས་པར་བྱ་བ་ཡང་མ་ཡིན་པ་ནི་གཟུགས་ལ་སོགས་པ་ལྟར་ཤེས་པས་རབ་ཏུ་རྟོགས་པར་བྱ་བའི་དངོས་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 385]
ཀུན་བརྟགས་པའི་ཆོས་ནི་ཤེས་པས་རྟོགས་པར་འགྱུར་བ་མ་ཡིན་ཏེ། དེའི་ཚེ་ན་མེད་པའི་ཕྱིར་རོ། །ཤེས་པར་མི་བྱ་བ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ནི་རི་བོང་གི་རྭ་ལྟར་ཤིན་ཏུ་མེད་པ་ཡང་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 386]
ཡོངས་སུ་ཤེས་པར་བྱ་བ་ལ་སོགས་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ནི་བདེན་པར་རྟོགས་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 387]
འབྲས་བུ་གང་ཡིན་པ་ནི་རྣམ་པར་སྨིན་པའོ། །

[Block 388]
རྣམ་པར་སྨིན་པར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་རྣམ་པར་སྨིན་པའི་ཆོས་ཅན་ནོ། །

[Block 389]
རབ་ཏུ་དགའ་བ་ལ་སོགས་པ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་སེམས་ཀྱི་ངོ་བོ་ཉིད་དུའོ། །

[Block 390]
འཐོབ་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་རྙེད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
