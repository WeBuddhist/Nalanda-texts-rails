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
[Block 561]
ཞེས་པ་ནི་རྡོ་རྗེ་བཟླས་པ་ནས་ཟུང་དུ་འཇུག་པའི་བར་དུའོ། །

[Block 562]
དེ་ལ་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་ཞེས་བྱ་བའང་དུ་ཞེ་ན། དེའི་ཕྱིར་བཤད་པ།

[Block 563 [VERSE]]
ངོ་བོ་དང་ནི་རྣམ་དབྱེ་དང་། །
ངེས་པའི་ཚིག་དང་རྣམ་གྲངས་དང་། །
ཆོས་རྣམས་གང་དང༌[^246]ལྡན་པ་དང་། །
གཞན་སེལ་བ་དང་རྒྱུད་དང་དུས། །

[Block 564 [VERSE]]
མཚན་ཉིད་དང་ནི་དམིགས་པ་དང་། །
གྲོགས་དང་གནས་དང་སྔོན་འགྲོ་དང་། །
རྟེན་དང་མི་མཐུན་གཉེན་པོ་དང་། །
ས་དང་སྤོང་བའི་ཁྱད་པར་དང་། །

[Block 565 [VERSE]]
རང་བཞིན་དངོས་གྲུབ་སྤྱོད་པ་དང་། །
ས་མཚམས་དང་ནི་གོམས་ཚད་དང་། །
མཐར་ཕྱིན་ཚད་དང་ངོས་བཟུང་དང་། །

[Block 566]
ཁྱད་པར་དང་ནི་འབྲས་བུའོ།[^247] །དེ་ལ་ངོ་བོ་ཞེས་བྱ་བའང༌[^248]གང་ཞིག་ཡིན། དེ་ཉིད་མི་ཤེས་སོ་ཞེ་ན།

[Block 567 [VERSE]]
འབྱུང་འཇུག་ཡུལ་ཅན་ཏིང་འཛིན་ནི། །
གང་དུ་དང་པོའི་ངོ་བོར་འདོད། །

[Block 568]
ཅེས་པ་འབྱུང་བ་དང་། འཇུག་པ་དང་གནས་པ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་འདི་ནི་དེའི་ངོ་བོར་བསམ་པའོ། །

[Block 569]
གཞན་ཤེས་རབ་ལ་སོགས་པ་དང་། ཐིག་ལེ་གཅིག་པ་དང་འོད་གསལ་བ་ལ་སོགས་པ་ནི་འདིར་ཤུགས་ཀྱིས༌[^249]གསལ་ལོ། །

[Block 570]
དབྱེ་བའང་དུ་ཞིག་ཅེ་ན། སྟེང་དང་འོག་དང་བར་གྱི་དབང་དུ་གསུམ་སྟེ། འདི་ལྟར་སྟེང་ལ་དམིགས་པ་ནི་སྟེང་གི་རྡོ་རྗེ་བཟླས་པའོ། །

[Block 571]
འོག་ལ་དམིགས་པ་ནི་འོག་གི་རྡོ་རྗེ་བཟླས་པའོ། །

[Block 572]
སྙིང་ག་ལ་དམིགས་པ་ནི་བར་གྱི་རྡོ་རྗེ་བཟླས་པའོ། །

[Block 573]
དེ་ལ་སྟེང་གི་རྡོ་རྗེ་བཟླས་པའང་གང་ཡིན་དུ་ཞིག་ཅེ་ན་དང་པོ་ནི་བཤད་ཟིན་ཏོ། །

[Block 574]
འོག་མའི་དབང་དུ་བཤད་པ།

[Block 575 [VERSE]]
དབུགས་དང་དབང་པོ་འགྱུར་བའི་དབང་། །
འདི་ནི་གཉིས་སུ་ཤེས་པར་བྱ། །

[Block 576]
ཞེས་པ་ལ་གང་གིས་དབུགས་ལ་སློབ་པ་དང་། དེ་བཞིན་དུ་མིག་ལ་སོགས་པ་གཞན་ལ་ཡང་སློབ་པ་འདི་ནི་གཉིས་པའོ། །

[Block 577]
དབང་པོའང༌[^250]དུ་ཞིག་ཅེ་ན།

[Block 578 [VERSE]]
མིག་ལ་སོགས་པའི་སྦྱོར་བ་ལ། །
ཡི་གེ་ཐིག་ལེ་མེད་པར་བྱ། །

[Block 579]
ཞེས་པ་མིག་གི་དབང་པོ་དང་། རྣ་བའི་དབང་པོ་དང་། སྣའི་དབང་པོ་དང་། ལྕེའི་དབང་པོ་དང་། ལུས་ཀྱི་དབང་པོ༌[^251]དང་། དེ་ལ་སོགས་པ་ལ་སློབ་པ་སྟེ། དེ་རེ་རེ་ལའང་སྐུ་དང་། ཕྱག་མཚན་དང་། ཐིག་ལེ་དང་། ཡི་གེ་ལ་སོགས་པ་ལ་སློབ་པའོ། །

[Block 580]
དེའི་རྟེན་ཡང་གང་ཡིན་ཞེ་ན། མིག་ལ་སོགས་པ་ལ་གནས་པའི་ཁ་དོག་དཀར་པོའམ། དེ་ལས་གཞན་པ་དང་། ལྡན་པའི་རྩ་པདྨ་ཁ་བྱེ་བའི་ཚུལ་ཅན་ལ་བརྟེན་པར༌[^252]བྱེད་པ་སྟེ།

[Block 581 [VERSE]]
པདྨ་ཁ་བྱེའི་ཚུལ་ཅན་ལ། །
བརྟེན་ནས་དེ་ཡི་རྣམ་པ་བསམ། །

[Block 582]
ཞེས་པས་བསྟན་ཏོ། །

[Block 583]
ཅིའི་ཕྱིར་དེའི༌[^253]དབང་པོའི་རྒྱུ་བ་འགོག་པ་ཡིན་སྙམ་པ་ལ།

[Block 584 [VERSE]]
གང་གིས་མིག་ལ་སོགས་པ་རྣམས། །
གཟུགས་ལ་སོགས་པའི་རྣམ་པ་ལ། །
མིག་ལས་རྒྱུ་བར་མི་བྱེད་པ། །
དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་བྱ། །

[Block 585]
ཞེས་པ་མིག་ནས་ལུས་ཀྱི་བར་དུ་ཡུལ་གྱི་རྣམ་པ་ལ་དམིགས་པའི་ཞེན་པ་འགོག་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 586]
དེ་ཡང་ཇི་ལྟར་བྱེད་སྙམ་པ་ལ།

[Block 587 [VERSE]]
དེ་ལ་དམིགས་ནས་འབྱུང་བ་དང་། །
འཇུག་དང་གནས་པར་བྱེད་པ་ཡིན། །

[Block 588]
ཞེས་པ། དབང་པོ་ལྔ་ལ་ཐིག་ལེ་ལ་སོགས་པ་དམིགས་ནས། དེ་ལ་སེམས་གཏད་དེ། འབྱུང་བ་དང་འཇུག་པ་དང་གནས་པ་གཉིས་ལ་བསླབ་པར་བྱའོ། །

[Block 589]
གནས་པ་གཉིས་ཞེས་བྱ་བ་འདི་ཡང་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 590 [VERSE]]
འབྱུང་དང་འཇུག་པའི་ཆ་ལ་གནས། །
རྩ་བ་དང་ནི་རྩེ་མོ༌[^254]གཉིས། །

[Block 591]
ཞེས་པ་གང་འབྱུང་བའི་ཆ་ལ་བརྟེན་པ་དེ་ཉིད་རྩེ་མོར་གནས་པ་ནི་དང་པོར་རྩ་བའི་ས་བོན་ལ་དམིགས་ནས་དེ་ལས་དབུགས་འབྱུང་བའི་སྟོབས་ཀྱིས། བ་ཐག་གམ་ཕྲེང་བའམ་འོད་ཀྱི་ཚུལ་དུ་རྩེ་མོ་ལ་བསྟིམས་ཏེ། འབྱུང་བ་རྒྱུན༌[^255]ཆད་པ་དང་། ཇི་སྲིད་དུ་དེ་ཉིད་ཀྱི་རྣམ་པ་ལ་དམིགས་པ་ནི་འབྱུང་བའི་ཆ་ལ་བརྟེན་པའི་གནས་པའོ། །

[Block 592]
དེ་ལས་གང་གི༌[^256]ཚུལ་དུ་འདུས༌[^257]ནས་རང་གི་སར་བསྟན་པ་ནི་འཇུག་པའི་ས་ལ་བརྟེན་པའི་གནས་པའོ། །

[Block 593 [VERSE]]
མིག་དང་རྣ་བ༌[^258]དང་ནི༌[^259]ལྕེ། །
ལུས་ཀྱི་སྤྱི་བོ་ལ་སོགས་མཐར། །
གང་ཞིག་དབང་པོ་ཁ་བྱེ་བའི། །
རྩ་ནི་དད་པའི་ཁ་དོག་ཅན། །

[Block 594]
རྩེ་མོར་སོ་སོའི་རིགས་མཐུན་པའི། །རྡོ་རྗེ་རིན་ཆེན་པདྨ་གྲི།[^260] །

[Block 595 [VERSE]]
རྒྱ་གྲམ་འཁོར་ལོའི་རྣམ་པའམ། །
ཨོཾ་ཨཱཿཧཱུཾ་དང་སྭཱ་ཧཱ་ཧཾ། །
རྩེ་མོ་ལ་ནི་ལེགས་གནས་པའོ། །
ཡང་ནི་ཕྲེང་བའི་ཐིག་ལེར་བཅས། །

[Block 596]
ཞེས་པ་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 597]
གཞན་ཡང་དབུགས་ཀྱི་རྒྱུ་བ་འགོག་པ་ཞེས་བྱ་བ་འདི་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 598 [VERSE]]
གང་གི་རྣ་བའི་བུ་ག་ནས། །
དབུགས་རྣམས་རབ་ཏུ་རྒྱུ་འགྱུར་བ། །
དེ་ལ་དམིགས་ཕྱིར་དེ་སྐད་དོ། །

[Block 599]
ཞེས་པ་གང་གིས་སྣའི་རྩེ་མོ༌[^261]ལ་དམིགས་ཏེ་ལུས་ཀྱི་གནས་ནས་རླུང་ཐམས་ཅད་འདུས་ནས། སྣའི་རྩེ་མོ་ལ་འཛིན་པ་འདི་ནི་དབུགས་ཀྱི་འགོག་པའོ། །

[Block 600]
འོ་ན་དབུགས་ཀྱང་ཇི་ལྟ་བུ་དམིགས་ཤེ་ན།
--- END BLOCKS ---
