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
དེའི་ཕྱིར་མེད་པའི་དོན་ནི་མི་རྟག་པའི་དོན་ཞེས་བྱའོ། །

[Block 527]
དེ་ལྟར་གཟུགས་ལ་སོགས་པ་ཀུན་བརྟགས་པའི་ཆོས་ཐམས་ཅད་མི་རྟག་པ་སྟེ། མེད་པའི་ཕྱིར་ཡོད་པ་ལས་གྱུར་པ་གང་ཡང་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 528]
ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་འདི་ལྟར་མི་རྟག་པ་གང་ཡིན་པ་དེ་ནི་དངོས་པོ་མེད་པ་དང་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ལ་མི་རྟག་པ་ཞེས་བྱ་བའི་སྒྲ་ནི་མེད་པ་དང་། དངོས་པོ་མ་ཡིན་པ་སྟེ། སྟོང་པ་ཉིད་ལ་བྱའོ། །

[Block 529]
ཟད་ཅེས་བྱ་བའི་སྒྲ་ནི་ཀུན་བརྟགས་པའི་ཆོས་རྣམས་ལ་བྱའོ། །

[Block 530]
དེ་ལྟར་ནི༌[^325]མི་རྟག་པ་གང་ཡིན་པ་དེ༌[^326]སྟོང་པ་ཉིད་དང་། ཀུན་བརྟགས་པའི་ཆོས་ཟད་པ་དངོས་པོ་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 531]
དེ་ལྟར་ཆོས་ཐམས་ཅད་ནི་མི་རྟག་གོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་དངོས་པོ་མེད་པའོ་ཞེས་བྱ་བ་ཉིད་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 532]
དེ་བས་ན་ཆོས་ཐམས་ཅད་ཀྱི་ཡོངས་སུ་གྲུབ་པ་དེ་བཞིན་ཉིད་ཀྱི་མཚན་ཉིད་བསྟན་པ་ཡིན་ཏེ། ཆོས་ཐམས་ཅད་ནི་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 533]
དེ་བཞིན་དུ་ཆོས་ཐམས་ཅད་ནི་སྡུག་བསྔལ་བ་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་སོགས་པ་ཀུན་བརྟགས་པའི་ཆོས་ཐམས་ཅད་ལ་དངོས་པོའི་རྣམ་པར་མངོན་པར་ཞེན་ནས་ཉེ་བར་ལེན་ན་སྡུག་བསྔལ་གསུམ་གྱི་རྒྱུར་འགྱུར་བས་སྡུག་བསྔལ་ཞེས་བརྗོད་དོ། །

[Block 534]
གང་གི་ཚེ་ཀུན་བརྟགས་པའི་རྣམ་པ་དངོས་པོ་མེད་པའི་བདག་ཉིད་དུ་ཡོངས་སུ་ཤེས་ནས་མངོན་པར་མི་ཞེན་ཅིང་སྤོང་བ་དེའི་ཚེ། སྡུག་བསྔལ་མེད་པའི་རྒྱུར་གྱུར་པས་བདེ་བ་ཡིན་ནོ། །

[Block 535]
དེ་བས་ན། སྡུག་བསྔལ་ནི་ཀུན་བརྟགས་པའི་ཆོས་ཞེས་བྱའོ། །

[Block 536]
ཆོས་ཐམས་ཅད་ནི་སྡུག་བསྔལ་བ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པ་རྣམས་དངོས་པོ་མེད་པའི་མཚན་ཉིད་ཁོ་ནར་བསྟན་པ་ཡིན་ཏེ། དངོས་པོ་མེད་པའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་ཆོས་ཐམས་ཅད་ནི་སྡུག་བསྔལ་བའོ། །

[Block 537]
འདིར་ཡང༌[^327]སྡུག་བསྔལ༌[^328]ནི་གང་དང་ཡང་བྲལ་བས་མ་ཡིན་ཞེས་བྱ་བར་སྦྱར་ཏེ། སྡུག་བསྔལ་ནི་བདེ་བའི་རྣམ་པ་ཡོད་པ་གང་དང་ཡང་བྲལ་བས་ནི་མ་ཡིན་གྱི་དངོས་པོ་མེད་པའི་ཕྱིར་སྡུག་བསྔལ་བའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 538]
དེ་བཞིན་དུ། སྡུག་བསྔལ་བ༌[^329]གང་ཡིན་པ་དེ་ནི་མེད་པ་དང་ཟད་པ་ཞེས་བྱ་སྟེ། ཀུན་བརྟགས་པའི་ཆོས་ཟད་པར་གྱུར་པ་རྣམས་དངོས་པོ་མ་ཡིན་པ་དང་། མེད་པ་ལ་ཕྱིན་ཅི་ལོག་ཏུ་མངོན་པར་ཞེན་པར་གྱུར་པ་ལ་སྡུག་བསྔལ་ཞེས་བྱ་བའོ༌[^330]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 539]
བདག་མེད་པ་ཡང་གང་དང་ཡང་བྲལ་བས་མ་ཡིན་ཏེ། བདག་མེད་པ་དང་ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 540]
བདག་མེད་པ་གང་ཡིན་པ་དེ་ནི་དངོས་པོ་མེད་པ་དང་། ཟད་པ་སྟེ་ཞེས་བྱ་བ་ནི་ཟད་པའི་ཆོས་རྣམས་ཀྱི་དངོས་པོ་མེད་པ་གང་ཡིན་པ་དེ་ཉིད་བདག་མེད་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 541]
དེ་བཞིན་དུ་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 542]
ཆོས་ཐམས་ཅད་ནི་ཐེར་ཟུག་ཏུ་གནས་པ་མ་ཡིན་འཇིག་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ཡང་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 543]
གལ་ཏེ་ཀུན་བརྟགས་པ༌[^331]རྣམས་ལ་ངོ་བོ་ཉིད་འགའ་ཞིག་ཡོད་ན་ནི་དེ་ཐེར་ཟུག་ཏུ་གནས་པ་རྟག་པའམ། འཇིག་པ་མི་རྟག་པ་ཞིག་ཏུ་འགྱུར་གྲང་ན། དེ་ལྟར༌[^332]དེ་ནི་སྒྱུ་མའི་གཟུགས་བཞིན་དུ་ངོ་བོ་ཉིད་མེད་པས། རྟག་པ་ཡང་མ་ཡིན་མི་རྟག་པ་ཡང་མ་ཡིན་ཏེ། སྒྱུ་མའི་གཟུགས་ལ་རྟག་ཅེས་བྱ་བའམ། མི་རྟག་ཅེས་བྱ་བར་བརྗོད་པར་མི་ནུས་པ་དེའི་ཕྱིར་ཆོས་ཐམས་ཅད་ནི་ཐེར་ཟུག་ཏུ་གནས་པ་མ་ཡིན། འཇིག་པ༌[^333]མ་ཡིན་ནོ། །

[Block 544 [HEADING]]
###### གཟུགས་མངོན་པར་འདུས་མ་བྱས་པ། ^1-1-7-2-8-0

[Block 545]
ཚིག་བརྒྱད་པ་ལ་གཟུགས་མངོན་པར་འདུས་མ་བྱས་པ་ཞེས་བྱ་བ་ནི་མངོན་པར་འདུ་བྱེད་པ་པོ་གང་ཡང་མེད་པའི་ཕྱིར་གཟུགས་ལ་སོགས་པ་མངོན་པར་འདུས་མ་བྱས་པའོ། །

[Block 546]
དེ་བས་ན། མངོན་པར་མ་གྲུབ་པ་ཞེས་བྱའོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 547 [HEADING]]
###### གཟུགས་ནི་རང་བཞིན་གྱིས་སྟོང་པ། ^1-1-7-2-9-0

[Block 548]
ཚིག་དགུ་པ་ལ། གཟུགས་ནི་རང་བཞིན་གྱིས་སྟོང་སྟེ། རང་བཞིན་གྱིས་སྟོང་པ་གང་ཡིན་པ་དེ་ལ་སྐྱེ་བ་མེད་ཅིང་འཇིག་པ་མེད་དེ། སྐྱེ་བ་མེད་ཅིང་འཇིག་པ་མེད་པ་གང་ཡིན་པ་དེ་ལ་གཞན་དུ་འགྱུར་བ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ལ་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ཀྱི་རང་བཞིན་ནི་ངོ་བོ་ཉིད་དེ་སྟོང་པ་ཉིད་དོ། །

[Block 549]
སྟོང་པ༌[^334]ཉིད་ནི་ཆོས་ཐམས་ཅད༌[^335]ཀྱི་ངོ་བོ་ཉིད་དོ། །

[Block 550]
རང་བཞིན་གྱིས་སྟོང་པ་གང་ཡིན་པ་དེ་ལ། སྐྱེ་བ་མེད་ཅིང་འཇིག་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་སྟོང་པའི་བདག་ཉིད་ཅན་གྱི་ཆོས༌[^336]ཡོངས་སུ་གྲུབ་པ་རྣམས་ལ་སྐྱེ་བ་དང་། འགག་པ་གཉིས༌[^337]མེད་དོ། །

[Block 551]
དེ་གཉིས་མེད་པས་གཞན་དུ་འགྱུར་བ་རྒ་བ་ཡང་མེད་དོ། །

[Block 552]
དེ་ལྟར་ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བ་དང་། འགག་པ་དང་། གཞན་དུ་འགྱུར་བ་རྣམས་མེད་པའི་ཕྱིར་སྐྱེ་བ་དང་། འགག་པ་དང་། གཞན་དུ་འགྱུར་བ་དང་ལྡན་པར་ཀུན་བརྟགས་ཤིང་མངོན་པར་གྲུབ་པའི༌[^338]མཚན་ཉིད་ཅན་གྱི་གཟུགས་ལ་སོགས་པ་གང་ཡིན་པ་དེ་དག་དོན་དམ་པར་མངོན་པར་མ་གྲུབ་པས་མེད་པའི་ཕྱིར་གང་མངོན་པར་མ་གྲུབ་པ་དེ་གཟུགས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནས། གང་མངོན་པར་མ་གྲུབ་པ་དེ་རྣམ་པར་ཤེས་པའི་བར་དུ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 553 [HEADING]]
###### མངོན་པར་མ་གྲུབ་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ། ^1-1-7-2-10-0

[Block 554]
ཚིག་བཅུ་པ་ལ། མངོན་པར་མ་གྲུབ་པ་གང་ཡིན་པ་དེ་ནི༌[^339]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་ཡིན་པ་དེ་ནི་མངོན་པར་མ་གྲུབ་པའོ་ཞེས་བྱ་བ་ལ་མངོན་པར་མ་གྲུབ་པ་ཞེས་བྱ༌[^340]བའི་སྒྲ་ནི་དེ་བཞིན་ཉིད་དེ། སྟོང་པ་ཉིད་ལ་བྱའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བའི་སྒྲ་ཡང་དེ་བཞིན་ཉིད་ལ་བྱའོ། །

[Block 555]
དེ་བས་ན་མངོན་པར་མ་གྲུབ་པ་དང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཉིས༌[^341]ལ་ཐ་དད་པ་མེད་དོ། །

[Block 556]
དེའི་ཕྱིར་ཅི༌[^342]མ་གྲུབ་པའི་ངོ་བོ་ཉིད་དོན་དམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་མངོན་པར་མ་གྲུབ་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ཇི་ལྟར་གདམས་ཤིང་རྗེས་སུ་གདམས་པར་བགྱི་ཞེས་བྱ་བ་གསུངས་ཏེ། སྟོང་པ་ཉིད་ལ་སྟོང་པ་ཉིད་ཇི་ལྟར་གདམས་པར་བྱ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 557 [HEADING]]
###### མངོན་པར་མ་གྲུབ་པ་དང་གཟུགས་གཉིས་སུ་མེད་པ། ^1-1-7-2-11-0

[Block 558]
ཚིག་བཅུ་གཅིག་པ་ལ། མངོན་པར་མ་གྲུབ་པ་ཡང་གཞན་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཡང་གཞན་ཞེས་བྱ་བ༌[^343]ཡིན་པར་ཡང་དག་པར་རྗེས་སུ་མ་མཐོང་ངོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པར་བསྟན་པའོ། །

[Block 559]
མངོན་པར་མ་གྲུབ་པ་དང་། གཟུགས་ལ་གཉིས་སུ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་བཟུང་ནས་བསྟན་པའོ། །

[Block 560 [HEADING]]
###### བྱིང་བའམ་སྐྲག་པར་མི་འགྱུར་བ། ^1-1-7-2-12-0

[Block 561]
ཚིག་བཅུ་གཉིས་པ་ལ། ཆོས་ཐམས་ཅད་སྒྱུ་མ་དང་། སྨིག་རྒྱུ་ལ་སོགས་པ་དང་མཚུངས་པར་སོ་སོར་བརྟགས་ན་གང་ལ་བྱིང་བ་འམ་སྐྲག་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ།། །།

[Block 562 [HEADING]]
##### རྣམ་པར་མི་རྟོག་པ་ཡིད་ལ་བྱེད་པའི་འབྲས་བུ། ^1-1-7-3-0

[Block 563]
བམ་པོ་བཅུ་བདུན་པ། དེ་ལྟར་རེ་ཞིག་རྣམ་པར་མི་རྟོག་པ་ཡིད་ལ་བྱེད་པ་བསྟན་ནས། དེའི་འོག་ཏུ་ཡིད་ལ་བྱེད་པ་དེ་དག་གི་འབྲས་བུ་སྟོན་ཏེ། དེའི་ཚེ་འདི་ནི་གཟུགས་ཞེས་བགྱི་བར་གཟུགས་ལ་མི༌[^344]འཛིན་ཅིང་མི་ལེན་མི་གནས་ཏེ། མངོན་པར་ཞེན་པར་མི་བགྱིད་ལ། འདོགས་པར་མི་བགྱིད་དོ་ཞེས་བྱ་བ་ནི་འཛིན་པའི་རིགས་པ༌[^345]བསྟན་པའི་ཕྱིར་ཚིག་ལྔ་སྨོས་ཏེ། ཐོག་མར་འདུ་ཤེས་ཀྱིས་མི་འཛིན་ཏོ། །

[Block 564]
དེའི་འོག་ཏུ་ཡིད་ཀྱིས་མི་ལེན་ཏོ། །

[Block 565]
དེའི་འོག་ཏུ་ཤེས་རབ་ཀྱིས་གནས་པར་མི་བྱེད་དོ། །
--- END BLOCKS ---
