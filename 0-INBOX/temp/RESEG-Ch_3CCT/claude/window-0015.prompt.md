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
[Block 526]
ཞེས་པ། གང་གིས་བསྐྱེད་པའི་རིམ་པའི་སྔོན་དུ་ནི་དང་པོར་མཚམས་བཅད་པ་དང་། བསོད་ནམས་ཀྱི་ཚོགས་དང་། [^237]ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་ཡན་ལག་བསྒོམ་པར་བྱའོ།[^238] །རྟེན་གྱི་གང་ཟག་ཀྱང་གང་ཡིན་ཞེ་ན།

[Block 527 [VERSE]]
གང་འདི་ཚོགས་དང་སློབ་མ་ཡིས། །
འདི་ནི་བསླབ་པར་བྱ་བ་ཡིན། །

[Block 528]
ཞེས་པ་འདི་ནི་ཐུན་མོང་སྒྲུབ་པའི་དབང་དུ་བྱས་ཏེ་དེ་ཉིད་དོ། །

[Block 529]
གཞན་གྱི་དབང་དུ་བྱས་ཏེ་སློབ་མས་ཀྱང་ངོ་། །གནས་ཀྱང༌[^239]གང་དུ་ཞེ་ན།

[Block 530 [VERSE]]
གནས་ནི་ཡིད་མཐུན་ཉམས་དགའ་བར། །
རྣལ་འབྱོར་པ་ཡིས༌[^240]བསམ་གཏན་བསྒོམ། །

[Block 531]
ཞེས་པ༌[^241]ནི་སྨིན་པར་བྱེད་པའི་སྐབས་སུ་ཤེས་པར་བྱའོ། །

[Block 532]
གྲོགས་ཀྱང་གང་ཡིན་ཞེ་ན།

[Block 533 [VERSE]]
དད་དང་ངོ་ཚ་ཤེས་ལ་སོགས། །
བསྐྱེད་པ་ཡི་ནི་གྲོགས་སུ་འགྱུར། །

[Block 534]
ཞེས་པ་དད་པ་ལ་སོགས་པ་དགེ་བའི་ཆོས་དང་།

[Block 535 [VERSE]]
སྤྱོད་པ་རྣམས་སུ་ཤེས་པར་བྱའོ། །
སེམས་གཟུང་བའང་ཇི་ལྟར་བྱ་ཞེ་ན། །
གང་འཕྲོད་དེ་ལ་དམིགས་ལ་སྦྱོང་། །
འདི་ནི་སེམས་གཟུང་མན་ངག་གོ། །

[Block 536]
ཞེས་པ་གང་གིས་གང་གསལ་བ་དེ་ལ་དམིགས་པ་འདི་ནི་སེམས་གཟུང་བའོ། །

[Block 537]
དེའང་གྲོགས་ཀྱི་མན་ངག་ནི་འདིར་སྦྱར་བར་བྱའོ། །

[Block 538]
འོ་ན་འདིའི་གོམས་པའི་ཚད་ཀྱང་ཇི་ལྟར་ཞེ་ན།

[Block 539 [VERSE]]
གང་ཞིག་འདི་ལ་གོམས་པ་ནི། །
བསྒྱུར༌[^242]བར་ནུས་དང་དམིགས་པ་གསལ། །

[Block 540]
ཞེས་པ་ནི་ལྷའི་སྐུ་ཁ་དོག་དང་། དབྱིབས་ལ་སོགས་པ་གཞན་ལས་གཞན་དུ་བསྒྱུར་ནུས་པ་འདི་ནི་འདིའི༌[^243]གོམས་པའི་ཚད་དོ། །

[Block 541]
མཐར་ཕྱིན་པའི་ཚད་ཀྱང་ཇི་ལྟར་ཞེ་ན།

[Block 542 [VERSE]]
ཇི་ལྟར་སྣང་བ་འདི་ཁོ་ན། །
ལྷ་ལས་གཞན་གྱི་སྦྱོར་བ་མིན། །

[Block 543]
ཞེས་པ་ཇི་ལྟར་སྣང་ཞིང་སྲིད་པས་བསྡུས་པ་ཐམས་ཅད་ལྷ་དང་། གཞལ་ཡས་ཁང་དང་། དེ་ལས་གཞན་པའི་རྣམ་པ་དང་བྲལ་བའོ། །

[Block 544]
འདིའི་དངོས་གྲུབ་གང་དང་འབྲེལ་བ་ཡིན་ཞེ་ན།

[Block 545 [VERSE]]
ཐུན་མོང་དངོས་གྲུབ་ཐམས་ཅད་ཀུན། །
བསྐྱེད་པའི་རིམ་དང་འབྲེལ་པ་ཡིན། །

[Block 546]
ཞེས་པ་ས་འོག་དང་། རི་ལུ་དང་། རྐང་མགྱོགས་དང་། མིག་རྣོན་ལ་སོགས་པ་འདི་ནི་བསྐྱེད་པའི་རིམ་པ་དང་འབྲེལ་བའོ། །

[Block 547]
འདི་དག་གིས༌[^244]ནི་དང་པོའི་སྦྱོར་བ་བསྟན་ཏེ། འདིས་རྟོག་པའང་གང་སྤོང་ཞེ་ན།

[Block 548 [VERSE]]
གང་དུ་རགས་པའི་རྟོག་པ་རྣམས། །
བསྐྱེད་པ་ཡིས་ནི་སྤོང་བར་བྱེད། །

[Block 549]
ཅེས་པ་བསྐྱེད་པའི་རིམ་པས་ནི་རགས་པའི་རྟོག་པའམ། ཉོན་མོངས་པ་མངོན་དུ་གྱུར་པ་སྤོང་བར་བྱེད་དོ། །

[Block 550]
འདིས་ཀྱང་ས་བོན་གང་ལ་ཕན་ཞེ་ན།

[Block 551 [VERSE]]
ལོངས་སྤྱོད་རྫོགས་དང་སྤྲུལ་སྐུ་ཡི། །
ས་བོན་ཁྱད་པར་ཅན་དུ་བྱེད། །

[Block 552]
ཅེས་པ་བསྐྱེད་པའི་རིམ་པ་བསྒོམས་པས་ལོངས་སྤྱོད་རྫོགས་པ་དང་། སྤྲུལ་པའི་སྐུ་ཐོབ་པའི་ས་བོན་གསོས་པ༌[^245]འདེབས་པར་བྱེད་དོ།།

[Block 553]
དེ་ལྟར་བསྐྱེད་པའི་རིམ་པ་རྒྱས་པར་བསྟན་ནས། ད་ནི་རྫོགས་པའི་རིམ་པའི་སྦྱོར་བའང་དུ་ཞིག་ཅེ་ན།

[Block 554 [VERSE]]
རྫོགས་པའི་རིམ་པའི་སྦྱོར་བ་ནི། །
རྣམ་པ་ལྔ་རུ་ཤེས་པར་བྱ། །

[Block 555]
ཞེས་པ་ལ། འདི་རྫོགས་པའི་རིམ་པའང་ཡིན་ལ། རྣམ་པ་ལྔའང་ཡིན་པས་འདི་ནི་རིམ་པ་ལྔའོ། །

[Block 556]
དེའང་གང་ཞེ་ན།

[Block 557 [VERSE]]
རྡོ་རྗེ་བཟླས་དང་སེམས་ལ་དམིགས། །
སྒྱུ་མ་འོད་གསལ་ཟུང་དུ་འཇུག །

[Block 558]
ཅེས་པ་འོད་གསལ་ལ་སོགས་པ་འོག་ནས་བསྟན་ཏོ། །

[Block 559]
རྣལ་འབྱོར་པ་གང་ཞིག་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་དུ་ཡོད་པའང་མི་ཤེས་ནས་དྲིས་པ་རྫོགས་པའི་རིམ་པའང་གང་ཡིན་དུ་ཞེ་ན།

[Block 560 [VERSE]]
རྡོ་རྗེ་བཟླས་ལ་སོགས་པའང་། །
རྣམ་པ་ལྔ་རུ་ཤེས་པར་བྱ། །

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
--- END BLOCKS ---
