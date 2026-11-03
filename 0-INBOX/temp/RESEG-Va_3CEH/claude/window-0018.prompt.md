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
[Block 631]
རྣམ་པར་རྟོག་པ་རྣམས་ཀྱིས་ངག་ཀུན་ནས་སློང་བ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་མངོན་པར་ཞེན་པས་མི༌[^457]གནོད་པ་ཡིན་ན་ཡང་རྣམ་པར་རྟོག་པ་གསུམ་གྱིས་ངག་ཀུན་ནས་འབྱུང་བར་བྱེད་དོ། །

[Block 632]
མཐོང་བ་ལ་སོགས་པ་ཐ་སྙད་བཞི་པོ་དག་གིས་ཐ་སྙད་འདོགས་པ་ཞེས་བྱ་བ་ལ་ནི་ཇི་ལྟར་མཐོང་བ་དང་། ཐོས་པ་དང་། ཤེས་པ་དང་། རྣམ་པར་ཤེས་པའོ་ཞེས་བྱ་བའི་ཐ་སྙད་རྣམ་པ་བཞིས་གཞན་དང་ཐ་སྙད་དུ་བྱེད་པའོ། །

[Block 633]
མེད་པའི་དོན་ལ་ཡོད་པ༌[^458]ཞེས་སྒྲོ་འདོགས་པས་ཞེས་བྱ་བ་ནི་ཐ་སྙད་ཇི་ལྟ་བ་བཞིན་དུ་མེད་པའི་དོན་ལ་དོན་ཡོད་པ་ཉིད་དོ་ཞེས་བཟུང་བའི་ཕྱིར་རོ། །

[Block 634]
ཀུན་ཏུ་རྟོག་པའི་རྒྱུ་མཚན་ཞེས་བྱ་བ་ནི་ཀུན་ཏུ་རྟོག་པ་ཞེས་བྱ་བ་ཡིད་ཀྱི་རྣམ༌[^459]པར་ཤེས་པས༌[^460]ཀུན་ཏུ་བརྟགས་པ་ཞེས་བྱ་བའི་མཚན་མར་བཟུང་ནས་དམིགས་པའི་ངོ་བོ་ཉིད་དུ་སྐྱེའོ། །

[Block 635]
དེས་ཀུན་ནས་བརྟགས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཀུན་ཏུ་རྟོག་པ་ཞེས་བྱ་བ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དེས་ཀུན་ཏུ་བརྟགས་པ༌[^461]ཞེས་བྱ་བ་དམིགས་པར་འགྱུར་བའི༌[^462]མཚན་མས་བཟུང་ནས་ཀུན་ཏུ་རྟོག་པར་བྱེད་པས་དོན་དེས་ན་གཞན་གྱི་དབང་ལ་ཀུན་ཏུ་བརྟགས་པ་ཞེས་བྱའོ། །

[Block 636]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཀུན་ཏུ་རྟོག་པས་ཀུན་ཏུ་བརྟགས་པ་ཉིད་ཀྱིས་ཀུན་ཏུ་བརྟགས་པ་ཇི་ལྟར་ཀུན་ཏུ་བརྟགས་པ་དེ་བཞིན་དུ་དེ་གཏན་མེད་པས་འདི་ལྟར་དོན་དེས་ན་གཞན་གྱི་དབང་དེ་ཉིད་ཡོངས་སུ་གྲུབ་པ་ཞེས་བྱའོ། །

[Block 637 [HEADING]]
### ཡོངས་སུ་མ་གྲུབ་པ་གཞན་གྱི་དབང། ^2-7-0

[Block 638]
ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བའི་ངོ་བོ་ཉིད་ཡོངས་སུ་མ་གྲུབ་པ་གཞན་གྱི་དབང་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་དེ་ལྟ་བུའི་གཞན་གྱི་དབང་དེ་རྣམ་པར་རྟོག་པར་གྱུར་ན་ཀུན་ནས་ཉོན་མོངས་པར་འགྱུར་ལ། རྣམ་པར་མི་རྟོག་པར་གྱུར་ན་རྣམ་པར༌[^463]བྱང་བར་འགྱུར་རོ། །

[Block 639]
དེ་དག་གཉི་གའི་སྒྲ་གཅིག་ཏུ་ཞུགས་པར་གྱུར་པ་ནི་མ་གྲུབ་པ་ཡིན་ནོ། །

[Block 640 [HEADING]]
### ངོ་བོ་ཉིད་དུ་ཀུན་ཏུ་རྟོག་པ་དང་ཁྱད་པར་དུ་ཀུན་ཏུ་རྟོག་པ། ^2-8-0

[Block 641]
ངོ་བོ་ཉིད་དུ་ཀུན་ཏུ་རྟོག་པ་དང་། ཁྱད་པར་དུ་ཀུན་ཏུ་རྟོག་པ་ཞེས་བྱ་བ་དེ་ལ། ངོ་བོ་ཉིད་དུ་ཀུན་ཏུ་རྟོག་པ་ནི་ཇི་ལྟར་མིག་ལ་སོགས་པ་རྣམས་ལ་མིག་གི་ངོ་བོ་ལ་སོགས་པ་ཀུན་ཏུ་རྟོག་པའོ། །

[Block 642]
ཁྱད་པར་དུ་ཀུན་ཏུ་རྟོག་པ་ནི་འདི་ལྟ་སྟེ། དེ་དག་ཉིད་ཀྱི་ངོ་བོ་མི་རྟག་པ༌[^464]ལ་སོགས་པའི་བྱེ་བྲག་གིས་ཀུན་ཏུ་རྟོག་པར་བྱེད་པའོ། །

[Block 643 [HEADING]]
### རང་བཞིན་གྱིས་ཡོངས་སུ་གྲུབ་པ་དང་རྣམ་པར་དག་པ་ཡོངས་སུ་གྲུབ་པ། ^2-9-0

[Block 644]
རང་བཞིན་གྱིས་ཡོངས་སུ་གྲུབ་པ་དང་། རྣམ་པར་དག་པ་ཡོངས་སུ་གྲུབ་པ་ཞེས་བྱ་བ་དེ་ལ། རང་བཞིན་གྱིས་ཡོངས་སུ་གྲུབ་པ་ནི་དྲི་མ་དང་བཅས་པའི་དེ་བཞིན་ཉིད་དོ། །

[Block 645]
རྣམ་པར་དག་པས་ཡོངས་སུ་གྲུབ་པ་ནི་དྲི་མ་མེད་པའི་དེ་བཞིན་ཉིད་དོ། །

[Block 646 [HEADING]]
### ཐ་སྙད་ལ་མཁས་པ་དང་མི་མཁས་པ། ^2-10-0

[Block 647]
བྱང་བ་ནི་ཐ་སྙད་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་ཐ་སྙད་ཤེས་པའོ། །

[Block 648]
ཐ་སྙད་ལ་མི་མཁས་པ་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི་བ་ལང་ལ་སོགས་པ་དག་གིས་ཏེ། གང་གི༌[^465]ཕྱིར་དེ་དག་ལ་རྣམ་པར་རྟོག་པ་ཡོད་ན་ཡང་ཡི་གེར་བརྗོད་པར༌[^466]མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 649 [HEADING]]
### རྣམ་པར་རྟོག་པ་རྣམ་པ་བཅུ། ^2-11-0

[Block 650 [HEADING]]
#### རྩ་བའི་རྣམ་པར་རྟོག་པ། ^2-11-1-0

[Block 651]
རྣམ་པར་རྟོག་པ་ཐམས་ཅད་བསྡུས་ནས་རྣམ་པར་རྟོག་པ་རྣམ་པ་བཅུར་བསྟན་ཏེ། དེ་ལ་རྩ་བའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ནི་ཀུན་ཏུ་བརྟག་པར་བྱ་བས་ན་རྣམ་པར་རྟོག་པའི་རྩ་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དེ་ཡང་ཀུན་གཞི་རྣམ་པར་ཤེས་པའོ། །

[Block 652 [HEADING]]
#### མཚན་མའི་རྣམ་པར་རྟོག་པ། ^2-11-2-0

[Block 653]
མཚན་མའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ནི་རྒྱུ་མཚན་ཅན་གྱི་རང་བཞིན་གྱིས༌[^467]རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དེ་ཡང་གཟུགས་ལ་སོགས་པའི་རྣམ་པར་རིག་པའོ། །

[Block 654 [HEADING]]
#### མཚན་མར་སྣང་བའི་རྣམ་པར་རྟོག་པ། ^2-11-3-0

[Block 655]
མཚན་མར་སྣང་བའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ནི་གང་མཚན་མའི་རྣམ་པ་ཅན་གྱི་རྣམ་པར་རྟོག་པ་སྐྱེ་བ་སྟེ། རྣམ་པར་བརྟག་པར༌[^468]བྱ་བའམ། རྣམ་པར་རྟོག་པ་ཞེས་དབྱེ་བ་བྱས་ཏེ། དེ་ཡང་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་རྣམ་པར་རིག་པ་རྟེན་དང་བཅས་པའོ། །

[Block 656 [HEADING]]
#### མཚན་མར་འགྱུར་བའི་རྣམ་པར་རྟོག་པ། ^2-11-4-0

[Block 657]
མཚན་མར་འགྱུར་བའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ནི་གང་མཚན་མའི་འགྱུར་བ་ལ་མཚན་མར་འགྱུར་བའི་བདག་ཉིད་ཅན༌[^469]རྣམ་པར་རྟོག་པ་ཞེས་བྱས་ནས་ཏེ། རྒ་བ་ལ་སོགས་པ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་འབྱུང་བ་ཆེན་པོ་རྣམས་ཀྱི་རང་བཞིན་དེངས་ཤིང་དོན་གཞན་དུ་གྱུར་པ་སྟེ། དེར་རྣམ་པར་རྟོག་པ་ནི་མཚན་མར་འགྱུར་བའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱའོ། །

[Block 658]
སྩོགས་པ༌[^470]སྨོས་པས༌[^471]ནི་ནད་དང་། འཆི་བ་དག་བསྡུའོ། །

[Block 659]
བདེ་བའི་ཚོར་བ་ལ་སོགས་པ་ཡང་དེ་བཞིན་ཏེ། ལུས་གཞན་དུ་འགྱུར་བའོ། །

[Block 660]
སྩོགས་པ༌[^472]སྨོས་པས་ནི་སྡུག་བསྔལ་དང་། སྡུག་བསྔལ་ཡང་མ་ཡིན་བདེ་བ་ཡང་མ་ཡིན་པ་བསྡུའོ། །

[Block 661]
འདོད་ཆགས་ལ་སོགས་པ་ལ་ཡང་དེ་བཞིན་ཏེ། སྩོགས་པ༌[^473]སྨོས་པས་ནི་ཞེ་སྡང་དང་གཏི་མུག་བསྡུའོ། །

[Block 662]
གནོད་པ་དང་དུས་ཀྱི་ཡོངས་སུ་འགྱུར་བ་ལ་སོགས་པ་ཞེས་བྱ་བ་ལ། དེ་བཞིན་དུ་ལུས་གཞན་དུ་འགྱུར་བ་སྟེ། གང་རྣམ་པར་རྟོག་པ་དེ་ལ་དམིགས་ནས་འབྱུང་བའོ། །

[Block 663]
གནོད་པ་དང༌[^474]ཞེས་བྱ་བ་ནི་རྡེག་པ་དང་། འཆིང་བ་ལ་སོགས་པའོ། །

[Block 664]
དུས་ཀྱི་ཡོངས་སུ་འགྱུར་བ་ཞེས་བྱ་བ་ནི་གྲང་བ་ལ་སོགས་པའི་དུས་ན་གཞན་དུ་ཡོངས་སུ་འགྱུར་བའོ། །

[Block 665]
དམྱལ་བ་བའི་འགྲོ་བ་ཞེས་བྱ་བ༌[^475]ལ་སོགས་པ་ཡང་དེ་བཞིན་ཏེ། སྩོགས༌[^476]པས་ནི་དུད་འགྲོ་དང་། ཡི་དྭགས་བསྡུའོ། །

[Block 666]
འདོད་པའི་ཁམས་ལ་སོགས་པ་ཞེས་བྱ་བ་སྔ་མ་བཞིན་ཏེ། སྩོགས་པ༌[^477]སྨོས་པས༌[^478]ནི་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་བསྡུའོ། །

[Block 667 [HEADING]]
#### མཚན་མར་སྣང་བར་འགྱུར་བའི་རྣམ་པར་རྟོག་པ། ^2-11-5-0

[Block 668]
མཚན་མར་སྣང་བར་འགྱུར་བའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ལ། མིག་ལ་སོགས་པའི་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་དེའི་མཚན་མར་སྣང་བར་གང་འགྱུར་བ་སྟེ། མཚན་མར་སྣང་བར་འགྱུར་བའི་བདག་ཉིད་ཀྱི་རྣམ་པར་རྟོག་པའོ། །

[Block 669]
དེ་ལྟ་བས་ན་འདི་དག་གི་ཡང་དག་པ༌[^479]ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པའི་རྒ་བ་ལ་སོགས་པ་གང་གིས་དེ་དང་དེའི་གནས་སྐབས་སུ་འགྱུར་བ་སྐྱེད་པར་བྱེད་པའོ། །

[Block 670 [HEADING]]
#### གཞན་གྱིས་བསྟན་པའི་རྣམ་པར་རྟོག་པ། ^2-11-6-0
--- END BLOCKS ---
