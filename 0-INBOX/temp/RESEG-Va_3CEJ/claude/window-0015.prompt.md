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
[Block 526 [VERSE]]
གཟུགས་མེད་གཏོགས་པ་ཡིད་དང་ནི། །
ཆོས་དང་ཡིད་ཀྱི་རྣམ་པར༌[^217]ཤེས། །

[Block 527]
ཁམས་གཟུགས་ཀྱི་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་དེར་སྐྱེ་སྟེ། དེའི་ཕྱིར་དེ་ནི་གཟུགས་ཀྱི་རང་བཞིན་གྱི་ཁམས་བཅུ་དང་དེ་དག་ལ་རྟེན་པ༌[^218]དང་དམིགས་པ་རྣམ་པར་ཤེས་པའི་ཁམས་ལྔ་ཡང་མེད་དོ། །

[Block 528 [HEADING]]
#### ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ། ^1-3-5-0

[Block 529]
ཟག་པ་དང་བཅས་པ་རྣམས་ནི་དུ། ཟག་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། ཡིད་དང་ཆོས་དང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་གང་དག་བཤད་པ། དེ་གསུམ་ཟག་བཅས་ཟག་པ་མེད། །གང་དག་ལམ་གྱི་བདེན་པ་དང་འདུས་མ་བྱས་ཀྱིས་བསྡུས་པ་དེ་དག་ནི་ཟག་པ་མེད་པ་ཡིན་ནོ། །

[Block 530]
གཞན་དག་ནི་ཟག་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 531]
ལྷག་མ་རྣམས་ནི་ཟག་བཅས་སོ། །

[Block 532]
ལྷག་མ་ཁམས་བཅོ་ལྔ་པོ་དེ་དག་ནི་གཅིག་ཏུ་ཟག་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 533 [HEADING]]
#### རྟོག་པ་དང་བཅས་དཔྱོད་པ་དང་བཅས་པ་ལ་སོགས་པ། ^1-3-6-0

[Block 534]
རྟོག་པ་དང་བཅས་དཔྱོད་པ་དང་བཅས་པ་རྣམས་ནི་དུ། རྟོག་པ་མེད་ལ་དཔྱོད་པ་ཙམ་དག་ནི་དུ། རྟོག་པ་ཡང་མེད་ལ་དཔྱོད་པ་ཡང་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན།

[Block 535 [VERSE]]
རྟོག་དང་དཔྱོད་དང་བཅས་པ་ནི། །
རྣམ་པར་ཤེས་པའི་ཁམས་ལྔ་ཡིན། །

[Block 536]
འདི་དག་ནི་རྟག་ཏུ་རྟོག་པ་དང་དཔྱོད་པ་དག་དང་མཚུངས་པར་ལྡན་པ་ཡིན་ཏེ། འདི་ལྟར་ཁ་ཕྱི་རོལ་དུ་བལྟས་པའི་ཕྱིར་རྩིང་བ་ཡིན་ནོ། །

[Block 537]
ནི་ཞེས་བྱ་བ་ནི་ངེས་པར་བཟུང་བའི༌[^219]དོན་ཏོ།[^220] །ཐ་མ་གསུམ་ནི་རྣམ་གསུམ་མོ། །

[Block 538]
ཐ་མ་དག་ནི་ཡིད་ཀྱི་ཁམས་དང་། ཆོས་ཀྱི་ཁམས་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་ཏེ། གསུམ་པོ་དེ་དག་ནི་རྣམ་པ་གསུམ་སྟེ། དེ་ལ་ཡིད་ཀྱི་ཁམས་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་། རྟོག་པ་དང་དཔྱོད་པ་དག་ལས་གཞན་པ་ཆོས་ཀྱི་ཁམས་མཚུངས་པར་ལྡན་པ་དག་དང༌[^221]འདོད་པའི་ཁམས་དང་བསམ་གཏན་དང་པོ་ན་ནི་རྟོག་པ་དང་བཅས་དཔྱོད་པ་དང་བཅས་པ་དག་ཡིན་ནོ། །

[Block 539]
བསམ་གཏན་ཁྱད་པར་ཅན༌[^222]ནི་རྟོག་པ་མེད་ཅིང་དཔྱོད་པ་ཙམ་དག་ཡིན་ནོ། །

[Block 540]
བསམ་གཏན་གཉིས་པ་ནས་བཟུང་སྟེ། སྲིད་པའི་རྩེ་མོའི་བར་གྱི་དང་། ཆོས་ཀྱི་ཁམས་མཚུངས་པར་ལྡན་པ་མ་ཡིན་པ་ཐམས་ཅད་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་གྱི༌[^223]དཔྱོད་པ་ནི་རྟོག་པ་ཡང་མེད་ལ་དཔྱོད་པ་ཡང་མེད་པ་དག་ཡིན་ནོ། །

[Block 541]
རྟོག་པ་ནི་རྟོག་པ་གཉིས་པ་མེད་པའི་ཕྱིར་དང་། དཔྱོད་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རྟག་ཏུ་རྟོག་པ་མེད་ཅིང་དཔྱོད་པ་ཙམ་ཡིན་ནོ། །

[Block 542]
འདོད་པའི་ཁམས་དང་བསམ་གཏན་དང་པོའི་དཔྱོད་པ་རྣམ་པ་གསུམ་པོ་འདི་དག་གི་ནང་དུ་མི་འདུ་ན་དེ་ཇི་སྐད་དུ་བརྗོད་པར་བྱ་ཞེ་ན། དཔྱོད་པ་གཉིས་པ་མེད་པའི་ཕྱིར་དང་། རྟོག་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་དཔྱོད་པ་མེད་ཅིང་རྟོག་པ་ཙམ་ཡིན་ནོ། །

[Block 543]
དེ་ཉིད་ཀྱི་ཕྱིར་རྟོག་པ་དང་བཅས་དཔྱོད་པ་དང་བཅས་པའི་ས་ན་ཆོས་རྣམ་པ་བཞི་ཡོད་དེ། རྟོག་པ་དང་བཅས་དཔྱོད་པ་དང་བཅས་པ་དག་ནི་རྟོག་པ་དང་དཔྱོད་པ་མ་རྟོགས༌[^224]པ་མཚུངས་པར་ལྡན་པ་རྣམས་སོ། །

[Block 544]
རྟོག་པ་མེད་ཅིང་དཔྱོད་པ་ཙམ་དག་ནི་རྟོག་པའོ། །

[Block 545]
རྟོག་པ་ཡང་མེད་དཔྱོད་པ་ཡང་མེད་པ་དག་ནི་མཚུངས་པར་ལྡན་པ་མ་ཡིན་པ་རྣམས་སོ། །

[Block 546]
དཔྱོད་པ་མེད་ཅིང་རྟོག་པ་ཙམ་ནི་དཔྱོད་པའོ་ཞེས་བྱའོ། །

[Block 547]
ལྷག་མ་རྣམས་ནི་གཉི་ག་སྤངས། །ལྷག་མ་རྣམས་ནི་གཟུགས་ཅན་གྱི་ཁམས་བཅུ་པོ་དག་སྟེ། དེ་དག་ནི་མཚུངས་པར་ལྡན་པ་མ་ཡིན་པའི་ཕྱིར་རྟག་ཏུ་རྟོག་པ་ཡང་མེད་དཔྱོད་པ་ཡང་མེད་པ་དག་ཡིན་ནོ། །

[Block 548 [HEADING]]
#### རྣམ་པར་རྟོག་པ་མེད་པ། ^1-3-7-0

[Block 549]
གལ་ཏེ་རྣམ་པར་ཤེས་པའི་ཚོགས་པ་ལྔ་པོ་རྣམས་རྟོག་པ་དང་དཔྱོད་པ་དང་བཅས་པ་དག་ཡིན་ན། ཇི་ལྟར་ན༌[^225]རྣམ་པར་རྟོག་པ་མེད་པ་དག་ཅེས་བྱ་ཞེ་ན།

[Block 550 [VERSE]]
ངེས་པར་རྟོག་དང་རྗེས༌[^226]དྲན་པའི། །
རྣམ་པར་རྟོག་པ་རྣམས༌[^227]མི་རྟོག །

[Block 551]
[^228]རྣམ་པར་རྟོག་པ་ནི་རྣམ་པ་གསུམ་མོ་ཞེས་གྲག་སྟེ། ངོ་བོ་ཉིད་དང་། ངེས་པར་རྟོག་པ་དང་། རྗེས་སུ་དྲན་པའི་རྣམ་པར་རྟོག་པའོ། །

[Block 552]
དེ་བས་ན་དེ་དག་ལ་ངོ་བོ་ཉིད་ཀྱི་རྟོག་པ་ཡོད་ཀྱི་གཞན་དག༌[^229]ཡིན་ཏེ། དེ་ལྟ་བས་ན༌[^230]རྣམ་པར་རྟོག་པ་མེད་པ་དག་ཅེས་བྱ་སྟེ། དཔེར་ན་རྟ་རྐང་གཅིག་པ་ལ་རྐང་མེད་ཅེས་བྱ་བ་བཞིན་ནོ། །

[Block 553 [HEADING]]
##### ངོ་བོ་ཉིད་ཀྱི་རྣམ་པར་རྟོག་པ། ^1-3-7-1-0

[Block 554]
དེ་ལ་ངོ་བོ་ཉིད་ཀྱི་རྣམ་པར་རྟོག་པ་ནི་རྟོག་པ་ཡིན་ཏེ། དེ་ནི་འོག་ནས་སེམས་ལས་བྱུང་བ་དག་གི་ནང་ནས་སྟོན་ཏོ། །

[Block 555 [HEADING]]
##### ངེས་པར་རྟོག་པའི་རྣམ་པར་རྟོག་པ། ^1-3-7-2-0

[Block 556]
གཞན་དག་གི་རང་བཞིན་ཅི་ཞེ་ན། རིམ་བཞིན་དུ།

[Block 557 [VERSE]]
དེ་དག་ཡིད་ཀྱི་ཤེས་རབ་གཡེང་། །
ཡིད་ཀྱི་དྲན་པ་ཐམས་ཅད་ཉིད། །

[Block 558]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཤེས་རབ་ནི་ཡིད་ཀྱི་ཞེས་བྱའོ། །

[Block 559]
མཉམ་པར་གཞག་པ་མ་ཡིན་པ་ནི་གཡེང་བ་ཞེས་བྱ་སྟེ། དེ་ནི་ངེས་པར་རྟོག་པའི་རྣམ་པར་རྟོག་པའོ། །

[Block 560 [HEADING]]
##### རྗེས་སུ་དྲན་པའི་རྣམ་པར་རྟོག་པ། ^1-3-7-3-0

[Block 561]
ཡིད་ཀྱི་དྲན་པ་ཉིད་མཉམ་པར་གཞག་པ་དང་མཉམ་པར་གཞག་པ༌[^231]མ་ཡིན་པ་ཐམས་ཅད་ནི་རྗེས་སུ་དྲན་པའི་རྣམ་པར་རྟོག་པ་ཡིན་ནོ། །

[Block 562 [HEADING]]
#### དམིགས་པ་དང་བཅས་པ་དང་དམིགས་པ་མེད་པ། ^1-3-8-0

[Block 563]
དམིགས་པ་དང་བཅས་པ་རྣམས་ནི་དུ། དམིགས་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། དམིགས་བཅས་སེམས་ཀྱི་ཁམས་བདུན་ནོ། །

[Block 564]
མིག་དང་། རྣ་བ་དང་། སྣ་དང་ལྕེ་དང་། ལུས་དང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་རྣམས་དང་། ཡིད་ཀྱི་ཁམས་ཏེ། སེམས་ཀྱི་ཁམས་བདུན་པོ་དེ་དག་ནི་ཡུལ་འཛིན་པའི་ཕྱིར་དམིགས་པ་དང་བཅས་པ་དག་གོ། །

[Block 565]
ཆོས་ཀྱི་སྐྱེ་མཆེད༌[^232]ཀྱང་། དམིགས་པ་དང་བཅས་པ་ཡིན་ཏེ། སེམས་ལས་བྱུང་བའི་རང་བཞིན་གང་ཡིན་པའོ། །
--- END BLOCKS ---
