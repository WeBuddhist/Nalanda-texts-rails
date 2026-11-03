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
[Block 631 [HEADING]]
###### **བྱང་ཆུབ་ཆེན་པོའི་རྒྱུ་རྒྱུན་མི་གཅོད་པ།** ^1-1-4-5-1-2-1-0

[Block 632]
བྱང་ཆུབ་སྒྲུབ་པའི་ཀུན་དུ་སྦྱོར་བ་རྣམས་ཀྱི་རྒྱུན་འབྲེལ་བ་ཞེས་བྱ་བས་བྱང་ཆུབ་ཆེན་པོའི་རྒྱུ་རྒྱུན་མི་གཅོད་པ་བསྟན་ཏེ། བྱང་ཆུབ་ཀྱི་དོན་ནི་གོང་དུ་སྨྲས་པར་ཟད་དོ། །

[Block 633]
ཀུན་དུ་སྦྱོར་བ་ནི་ཞི་གནས་དང་ལྷག་མཐོང་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 634]
ཞི་གནས་དང་ལྷག་མཐོང་བསྒོམ་པ༌[^527]གང་གིས་བྱང་ཆུབ་ཐོབ་པར༌[^528]བྱེད་པ་དེ་ནི་བྱང་ཆུབ་སྒྲུབ་པའི་ཀུན་དུ་སྦྱོར་བ་ཞེས་བྱ་སྟེ། དེ་ལྟར་བསྒོམ་པ་རྒྱུན་མི་གཅོད་པ་ནི་ཀུན་དུ་སྦྱོར་བ་རྣམས་ཀྱི་རྒྱུན་འབྲེལ་པའོ། །

[Block 635 [HEADING]]
###### **ཞི་བ་ཕྱོགས་གཅིག་པའི་རྒྱུ་སྒྲུབ་པར་མི་བྱེད་པ།** ^1-1-4-5-1-2-2-0

[Block 636]
ཉི་ཚེ་བའི་ཀུན་དུ་སྦྱོར་བ་རྣམས་མི་སྤྱད་པ༌[^529]ཞེས་བྱ་བས་ཞི་བ་ཕྱོགས་གཅིག་པའི་རྒྱུ་སྒྲུབ་པར་མི་བྱེད་པ༌[^530]བསྟན་ཏེ། ཉི་ཚེའི༌[^531]ཀུན་དུ་སྦྱོར་བ་ནི་ཞི་བ་ཕྱོགས་གཅིག་པའི་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་འགྱུར་བའི་རྒྱུ་ཞི་གནས་དང་ལྷག་མཐོང་སྒོམ་པར༌[^532]བྱེད་པའོ། །

[Block 637]
མི་སྤྱད་པ་ནི་དེ་ལྟ་བུའི་རྒྱུ་ལ་མི་འཇུག་པའོ། །

[Block 638]
ཡང་ན་འཁོར་བའི་རྒྱུན་གྱི་ཉོན་མོངས་པ་རྣམས་གཅོད་ཀྱང་བྱང་ཆུབ་ཆེན་པོ་ཐོབ་པར་བྱེད་པའི་རྒྱུ་རྒྱུན་མི་གཅོད་པས་ན་བྱང་ཆུབ་སྒྲུབ་པའི་ཀུན་དུ་སྦྱོར་བ་རྣམས་ཀྱི་རྒྱུན་འབྲེལ་པ་ཞེས་བྱའོ། །

[Block 639]
འཁོར་བར་སྐྱེ་བའི་དགེ་བའི་རྩ་བ་རྣམས་རྒྱུན་མི་གཅོད་པས་ཞི་བ་ཕྱོགས་གཅིག་པའི་མྱ་ངན་ལས་འདས་པར་མ་ལྷུང་བའི་ཕྱིར་ཉི་ཚེ་བའི་ཀུན་དུ་སྦྱོར་བ་རྣམས་མི་སྤྱད་པ་ཞེས་བྱའོ། །

[Block 640 [HEADING]]
###### འདུས་མ་བྱས་ལ་མཁས་པ། ^1-1-4-5-2-0

[Block 641]
གང་ཡང་སྟོང་པ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པས་འདུས་མ་བྱས་ལ་མཁས་པ་བསྟན་ཏེ། དེ་ཡང་ཏིང་ངེ་འཛིན་གསུམ་ལ་དབང་ཐོབ་པ་དང་། [^533]གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་ལ་མི་བརྟེན་པར༌[^534]དེ་བཞིན་ཉིད་ཁོང་དུ་ཆུད་པ་དང་། དེ་བཞིན་ཉིད་ཁོང་དུ་ཆུད་ཀྱང་དེའི་ཕྱོགས་ལ་མི་གནས་པའོ། །

[Block 642 [HEADING]]
###### **ཏིང་ངེ་འཛིན་གསུམ་ལ་དབང་ཐོབ་པ།** ^1-1-4-5-2-1-0

[Block 643]
གང་སྟོང་པ་ཉིད་དང་མཚན་མ་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཏིང་ངེ་འཛིན་གསུམ་ལ་དབང་ཐོབ་པ་བསྟན་ཏེ། སྟོང་པ་ཉིད་ལ་སོགས་པ་ནི་གོང་དུ་བཤད་པར་ཟད་དོ། །

[Block 644]
ཡེ་ཤེས་གང་གིས་ཏིང་ངེ་འཛིན་དེ་གསུམ་ལ་དབང་བྱེད་པར་འགྱུར་བ་དེ་ལ་ནི་འདྲིས་པར་བྱེད་པའི་ཡེ་ཤེས་ཞེས་བྱ་སྟེ། ཡེ་ཤེས་དེ་མངོན་སུམ་དུ་གྱུར་པའམ། ཡེ་ཤེས་དེ་རྟོགས་པ་ནི་རྟོགས་པ་ལ་མཁས་པའོ། །

[Block 645 [HEADING]]
###### **གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་ལ་མི་བརྟེན་པར་དེ་བཞིན་ཉིད་ཁོང་དུ་ཆུད་པ།** ^1-1-4-5-2-2-0

[Block 646]
བྱང་ཆུབ་ཏུ་གཞན་གྱི་དྲིང་ལ་མི་འཇོག་ཅིང་ཞེས་བྱ་བས་གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་ལ་མི་བརྟེན་བར་དེ་བཞིན་ཉིད་ཁོང་དུ་ཆུད་པ་བསྟན་ཏེ། དེ་བཞིན་གཤེགས་པ་དང་མཁན་པོ་དང་སློབ་དཔོན་གྱིས་བསྟན་པའི་མན་ངག་ལ་མི་བརྟེན་པར་སྟོང་པ་གཉིས་སུ་མེད་པའི་མཚན་ཉིད་ཁོང་དུ་ཆུད་པ་ནི་བྱང་ཆུབ་གཞན་གྱི་དྲིང༌[^535]མི་འཇོག་པ་ཞེས་བྱའོ། །

[Block 647 [HEADING]]
###### **དེ་བཞིན་ཉིད་ཁོང་དུ་ཆུད་ཀྱང་དེའི་ཕྱོགས་ལ་མི་གནས་པ།** ^1-1-4-5-2-3-0

[Block 648]
འདུས་མ་བྱས་མངོན་སུམ་དུ་མི་བྱེད་ཅེས་བྱ་བས་དེ་བཞིན་ཉིད་ཁོང་དུ་ཆུད་ཀྱང་དེའི་ཕྱོགས་ལ་མི་གནས་པ་བསྟན་ཏེ། འདུས་མ་བྱས་ནི་མྱ་ངན་ལས་འདས་པའམ་སྟོང་པ་ཉིད་དོ། །

[Block 649]
མངོན་སུམ་དུ་མི་བྱེད་པ་ནི་དེ་དག་ཁོང་དུ་ཆུད་ཅིང་ཐོབ་ཀྱང་དེའི་ཕྱོགས་ལ་མི་གནས་པའོ། །

[Block 650 [HEADING]]
##### འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་མཁས་པའི་རྣམ་པ་གཞན། ^1-1-4-6-0

[Block 651]
འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་མཁས་པའི༌[^536]རྣམ་པ་གཞན་ཡང་བསྟན་པའི་ཕྱིར་གཞན་ཡང་འདུས་བྱས་ལ་མཁས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 652]
ཁམས་གསུམ་ན་ཡང་སྤྱོད་ལ་ཁམས་གསུམ་ན་སྤྱོད་པའི་ཉོན་མོངས་པས་ཀྱང་མི་གོས་ཞེས་བྱ་བས་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་དུ་ཁམས་གསུམ་ན་ཡང་གནས་ལ། པདྨོ་འདམ་ལས་སྐྱེས་ཀྱང་འདམ་གྱི་ཉེས་པས་མི་གོས་པ་བཞིན་དུ་ཁམས་གསུམ་ན་ཡོད་པའི༌[^537]འདོད་ཆགས་ལ་སོགས་པས་མི་གོས་པ་འདི་ནི། འདུས་བྱས་ལ་མཁས་པ་ཞེས་བྱའོ། །

[Block 653]
གང་ཡང་ཁམས་གསུམ་ནས་ངེས་པར་འབྱུང་བའི་ཡེ་ཤེས་རབ་ཏུ་ཤེས་ཀྱང་ཞེས་བྱ་བ་ལ། ཁམས་གསུམ་ནས་ངེས་པར་འབྱུང་བའི་ཡེ་ཤེས་ནི་ཉོན་མོངས་པ་སྤོང་བར་བྱེད་པ་དང་། སྤོངས་པ༌[^538]མངོན་དུ་གྱུར་པ་ཟད་ལ་མི་སྐྱེ་བའི་ཡེ་ཤེས་ལ་བྱའོ། །

[Block 654]
རབ་ཏུ་ཤེས་ཀྱང་ཞེས་བྱ་བ་ནི་དེ་མངོན་སུམ་དུ་གྱུར་ཀྱང་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 655]
ངེས་པར་འབྱུང་བའི་དབྱིངས་སུ་མི་ལྷུང་ཞེས་བྱ་བ་ལ་ངེས་པར་འབྱུང་བའི་དབྱིངས་ནི་མྱ་ངན་ལས་འདས་པ་ལ་བྱ། [^539]མི་ལྟུང་བ་ནི་དེ་འབའ་ཞིག་གི་ཕྱོགས་ལ་མི་གནས་པའོ། །

[Block 656 [HEADING]]
#### མཁས་པ་བརྒྱད་པོ་བསྡུས་ཏེ་བསྟན་པ། ^1-1-5-0

[Block 657 [HEADING]]
##### ངེས་པའི་ཚིག། ^1-1-5-1-0

[Block 658]
མཁས་པ་བརྒྱད་པོ་རྣམས་རྒྱ་ཆེར་བཤད་པའི་ངེས་པའི་ཚིག་དང་རྒྱུ་དང་འབྲས་བུ་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། གང་ཆོས་ཐམས་ཅད་ལ་མཁས་པ་ཞེས་སྨྲས་པ༌[^540]དེ་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཚིག་བླ་དགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཆོས་ཐམས་ཅད་ལ་མཁས་པ་ཞེས་ཀྱང་བྱ། ཐམས་ཅད་མཁྱེན་པ་ཞེས་ཀྱང་བྱ་བས་ཆོས་ཐམས་ཅད་ལ་མཁས་པ་ཞེས་སྨྲས་པ་དེ་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཚིག་བླ་དགས་ཏེ། འདིས་ནི་ངེས་པའི་ཚིག་བསྟན་ཏོ། །

[Block 659 [HEADING]]
##### རྒྱུ། ^1-1-5-2-0

[Block 660]
ཅིའི་ཕྱིར་ཞེས་བྱ་བ་ནི་རྒྱུ་འདྲི་བ་སྟེ། ཆོས་ཐམས་ཅད་ལ་མཁས་པ་དེ་ཅིའི་ཕྱིར་ཐམས་ཅད་མཁྱེན་པ་ཞེས་བྱ༌[^541]ཞེ་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 661]
རྒྱུ་བསྟན་པའི་ཕྱིར། རྟག་ཏུ་དྲན་པ་དང་བློ་གྲོས་དང་ཤེས་རབ་ལ་མཁས་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། ཆོས་ཐམས་ཅད་ལ་མཁས་པ་དེ་ནི་རྟག་ཏུ་དྲན་པ་ལ་མཁས་པ་དང་། རྟག་ཏུ་བློ་གྲོས་ལ་མཁས་པ་དང་། རྟག་ཏུ་ཤེས་རབ་ལ་མཁས་པས་དེ་ལ་ཐམས་ཅད་མཁྱེན་པ་ཞེས་བྱའོ། །

[Block 662]
དེ་གསུམ་གྱིས་ཆོས་ཐམས་ཅད་ལ་རྟོགས་པས༌[^542]ན་མཁས་པ་སྟེ། དྲན་པ་ལ་མཁས་པ་ནི་ཆོས་རྣམས་ཀྱི་དོན་དང་ཚིག་མི་བརྗེད་པར༌[^543]བྱེད་དོ། །

[Block 663]
བློ་གྲོས་ལ་མཁས་པ་ནི་ཆོས་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་རྟོག་པར་བྱེད་དོ། །ཤེས་རབ་ལ་མཁས་པ་ནི་ཆོས་རྣམས་ཀྱི་རང་དང་སྤྱིའི་མཚན་ཉིད་རྟོག་པར་བྱེད་དོ། །

[Block 664 [HEADING]]
##### འབྲས་བུ། ^1-1-5-3-0

[Block 665]
འབྲས་བུ་བསྟན་པའི་ཕྱིར་སྨྲས་པ། ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཚད་མེད་ཅིང་མི་ཆགས་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། ཤེས་བྱ་ཐམས་ཅད་ལ་དམིགས་པས་ན༌[^544]ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཚད་མེད་པ་ཞེས་བྱ་སྟེ། ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ནི་མེ་ལོང་ལྟ་བུའི་ཡེ་ཤེས་ལ་བྱ་བར་འདོད་དོ། །

[Block 666]
ཡེ་ཤེས་དེ་ལ་ཉོན་མོངས་པའི་སྒྲིབ་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་མ་ལུས་པར་སྤངས་པས་ན་མི་ཆགས་པའོ། །

[Block 667]
ཡོངས་སུ་རྫོགས་པར་བྱེད་ཅེས་བྱ་བ་ནི་དྲན་པ་ལ་སོགས་པ་གསུམ་གྱིས་ཡེ་ཤེས་དེ་འཐོབ་ཅིང་མཐར་ཕྱིན་པར་བྱེད་པའི་ཕྱིར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 668]
དེའི་ཕྱིར་ཆོས་ཐམས་ཅད་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་གང་གི༌[^545]ཕྱིར་གོང་དུ་བཤད་པ་ལྟར་ན་ཆོས་ཐམས་ཅད༌[^546]རྟོགས་ཤིང་ཁོང་དུ་ཆུད་པ་དེའི་ཕྱིར་ཆོས་ཐམས་ཅད་ལ་མཁས་པ་ཞེས་བྱའོ། །

[Block 669]
མཁས་པ་བརྒྱད་པོ་དེ་དག་གིས་ཟིན་པ་ཞེས་བྱ་བ་ནི་མཁས་པ་བརྒྱད་པོ་འདི་དག་དང་ལྡན་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 670 [HEADING]]
### ཤེས་རབ་ཀྱི་ལས། ^1-2-0
--- END BLOCKS ---
