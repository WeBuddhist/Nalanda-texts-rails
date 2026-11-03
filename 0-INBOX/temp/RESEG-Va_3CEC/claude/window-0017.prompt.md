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
[Block 596]
བྱང་ཆུབ་ནི་སྤངས་པ་དང་ཡེ་ཤེས་ཕུན་སུམ་ཚོགས་པས་རབ་ཏུ་ཕྱེ་བ་སྟེ། སྔར་བཤད་པ་བཞིན་ནོ། །

[Block 597]
བྱང་ཆུབ་དེ་ལྟ་བུ་ཐོབ་པར་བྱ་བའི་ཕྱིར་དགེ་བ་མངོན་པར་འདུས་བྱས་པ་རྣམས་བསྔོ་བ༌[^506]དེ་ནི་བྱང་ཆུབ་ཏུ་བསྔོ་བ་ཞེས་བྱ་སྟེ། དེ་ནི་འདུས་བྱས་ལ་མཁས་པའོ། །

[Block 598 [HEADING]]
##### འདུས་མ་བྱས་ལ་མཁས་པ། ^1-1-4-2-0

[Block 599]
གང་ཡང་དགེ་བའི་ལུས་དང་ངག་དང་ཡིད་ཀྱི་འདུ་བྱེད་མངོན་པར་འདུས་བྱས་པ༌[^507]དེ་དག་ཐམས་ཅད་བྱང་ཆུབ་ལ་རྟོག་པས་ཐམས་ཅད་མཁྱེན་པ་ཉིད་དུ་བསྔོ་བ་ཞེས་བྱ་བ་ལ། གོང་དུ་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་བསྔོ་བ་བཤད་པ་ལ་བྱང་ཆུབ་ལ་རྟོག་པ་ཞེས་བྱ་བའི་ཚིག་མ་སྨོས་པས་འདུས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 600]
འདིར་ནི་བྱང་ཆུབ་ལ་རྟོག་པ་ཞེས་སྨོས་པས། ལུས་དང་ངག་དང་ཡིད་ཀྱི་དགེ་བ་ཇི་སྤྱད་པ་ཐམས་ཅད་ཀྱང་བྱང་ཆུབ་ཀྱི་མཚན་ཉིད་དང་དབྱེར་མེད་པར་སྟོང་པ་ཉིད་དུ་བརྟགས་ནས་ཐམས་ཅད་མཁྱེན་པ་ཐོབ་པར་བྱ་བའི་ཕྱིར་བསྔོ་སྟེ། བྱང་ཆུབ་ཀྱང་འདུས་མ་བྱས་ཀྱི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་འདུས་མ་བྱས་ལ་མཁས་པ་ཞེས་བྱའོ། །

[Block 601 [HEADING]]
##### འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་མཁས་པའི་རྣམ་གྲངས་གཞན། ^1-1-4-3-0

[Block 602]
གཞན་ཡང་འདུས་མ་བྱས་པ་ལ་མཁས་པ་ནི་ཞེས་བྱ་བས་འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་མཁས་པའི་རྣམ་གྲངས་གཞན་སྟོན་ཏེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྔ་སྒྲུབ་པ་ནི་འདུས་བྱས་ལ་མཁས་པ་ཞེས་བྱའོ། །

[Block 603]
གང་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་འདུས་མ་བྱས་པ་ལ་མཁས་པར་བསྟན་ཏོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དེ་ཡང་ཅི་འདྲ་བ་ཞིག་ཅེ་ན། དེའི་ཕྱིར་འདུས་མ་བྱས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྔ་པོ་དག་ལ་མི་སྨོད་ཅིང་ཅེས་བྱ་བ་སྨོས་ཏེ། སྟོང་པ་ཉིད་ལ་དམིགས་པའི་ཡེ་ཤེས་ནི་འདུས་མ་བྱས་ཀྱི་ཡེ་ཤེས་ཏེ། དངོས་སུ་ན་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ལ་བྱའོ། །

[Block 604]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྔ་ནི་འཁོར་བར༌[^508]སྐྱེ་བའི་རྒྱུ་ཡིན་པས་སྨད་པ་ཡིན་ཡང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་དེ་ལ་སུན་འབྱིན་པར་མི་བྱེད་པ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྔ་ལ་མི་སྨོད་པ་ཞེས་བྱའོ། །

[Block 605]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ཀྱི་ཚོགས་ནི་སྦྱིན་པ་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གི་ཚོགས་སོ། །

[Block 606]
དགེ་བའི་རྩ་བ་འདོད་མ་ཆགས་པ་ལ་སོགས་པའོ། །

[Block 607]
ཕྱིར་ཞེས་བྱ་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཚོགས་དང་། དགེ་བའི་རྩ་བའི་ཚོགས་བསྩགས་པར་བྱ་བའི་དོན་དུ་འམ་ཆེད་དུ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 608]
བྱང་ཆུབ་སེམས་དཔའི་རྣམ་པར་གྲོལ་བ་ནི་ཉོན་མོངས་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་པའི་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 609]
བྱང་ཆུབ་སེམས་དཔའི་ཐམས་ཅད་མཁྱེན་པ་ནི་དངོས་པོ་ཐམས་ཅད་ཐུགས་སུ་ཆུད་པ་མེ་ལོང་ལྟ་བུའི་ཡེ་ཤེས་ལ་བྱའོ། །

[Block 610]
བསྔོ་བ༌[^509]ཞེས་བྱ་བ་ནི་མྱ་ངན་ལས་འདས་པ་དང་ཡེ་ཤེས་དེ་ཐོབ་པར་བྱ་བའི་དོན་དུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་བསྒྲུབས་པ༌[^510]བསྔོ་བའོ། །

[Block 611]
དེ་དག་གིས་ནི་འདི་སྐད་བསྟན་པ་ཡིན་ཏེ། གོང་དུ་སྦྱིན་པ་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྔ་རྣམས་ནི་འདུས་མ་བྱས་ཀྱི་ཆོས་རྟོག་པའི༌[^511]རང་རང༌[^512]བཞིན་མ་ཡིན་པས་འདུས་བྱས་ལ་མཁས་པར་བཤད། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་འདུས་མ་བྱས་རྟོག་པའི༌[^513]རང་བཞིན་ཡིན་པས་འདུས་མ་བྱས་ལ་མཁས་པར་བཤད་དོ། །

[Block 612 [HEADING]]
##### འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་མཁས་པའི་རྣམ་གྲངས། ^1-1-4-4-0

[Block 613]
གཞན་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པས་འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་མཁས་པའི་རྣམ་གྲངས་སྟོན་ཏེ། [^514]ཡེ་ཤེས་དང་སྙིང་རྗེས༌[^515]སེམས་ཅན་ཐམས་ཅད་ལ་བལྟས་ནས་ཅི་རིགས་པར་ཕན་འདོགས་པར་བྱེད་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་ཐོགས་པ་མེད་པའི་འོད་ཟེར་མཉམ་པར་གཏོང་བ་ཞེས་བྱའོ། །

[Block 614]
དེ་ལྟར་ཕན་གདགས་པར་བྱ་བའི་ཕྱིར་སྦྱིན་པ་དང་། སྙན་པར་སྨྲ་བ་དང་། དོན་སྤྱོད་པ་དང་། དོན་མཐུན་པར་སྤྱོད་པ་བཞིས་སེམས་ཅན་སྡུད་པར་བྱེད་པ་ནི་འདུས་བྱས་ལ་མཁས་པ་ཞེས་བྱའོ། །

[Block 615]
མི་འཛིན་མི་ལེན་མཆོག་ཏུ་འཛིན་པར་མི་བྱེད་ཅེས་བྱ་བ་ལ་སོགས་པ་ལ་དེ་ལྟ༌[^516]མོད་ཀྱི། དོན་དམ་པར་སྟོང་པ་ཡིན་པས་ཕྱིའི་ཡུལ་ལ་དངོས་པོར་མི་འཛིན། ནང་གི་དངོས་པོ་ལ་བདག་ཏུ་མི་ལེན་ལ། དེ་ལྟར་དངོས་པོ་དང་བདག་ཏུ་མ་གྲུབ་པས་ཕན་བཏགས་སོ་ཞེས་མཆོག་ཏུ་འཛིན་པར་ཡང༌[^517]མི་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 616]
བསྡུ་བའི་དངོས་པོ་ལ་མཁས་པ་དེ་ཡང་འདུས་མ་བྱས་ལ༌[^518]མོས་པ༌[^519]ཞེས་བྱ་བ་ནི་བསྡུ་བའི་དངོས་པོ་རྣམས་ཀྱང་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་དུ་མོས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 617]
ཐམས་ཅད་མཁྱེན་པ་ཉིད་དུ་བསྔོ་བ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་སྟོང་པ་ཉིད་དུ་མོས་པས་བསྡུ་བའི་དངོས་པོ་ལ་མཁས་པ་དེ་དེ་བཞིན་ཉིད་ཐུགས་སུ་ཆུད་པའི་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་བསྔོ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་འདུས་མ་བྱས་ལ་མཁས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 618 [HEADING]]
##### འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་མཁས་པ་རྣམ་གྲངས་གཞན། ^1-1-4-5-0

[Block 619]
འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་མཁས་པ་རྣམ་གྲངས་གཞན་ཡང་བསྟན་པར་བཞེད་ནས། གཞན་ཡང་འདུས་བྱས་ལ་མཁས་པ་ནི་གང་འཁོར་བའི་རྒྱུན་གྱི་ཉོན་མོངས་པ་རྣམས་གཅོད་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 620 [HEADING]]
###### འདུས་བྱས་ལ་མཁས་པ། ^1-1-4-5-1-0

[Block 621]
དེ་ལ་འདུས་བྱས་ལ་མཁས་པ་རྣམ་པ༌[^520]གཉིས་ཏེ། འཇིག་རྟེན་པའི་རྒྱུ་ལ་མཁས་པ་དང་། འཇིག་རྟེན་ལས་འདས་པའི་རྒྱུ་ལ་མཁས་པའོ། །

[Block 622 [HEADING]]
###### **འཇིག་རྟེན་པའི་རྒྱུ་ལ་མཁས་པ།** ^1-1-4-5-1-1-0

[Block 623]
འཇིག་རྟེན་པའི་རྒྱུ་ལ་མཁས་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། སྡུག་བསྔལ་གྱི་རྒྱུ་སྤོང་བ་ལ་མཁས་པ་དང་། བདེ་བའི་རྒྱུ་བསྐྱེད་པ༌[^521]ལ་མཁས་པའོ། །

[Block 624 [HEADING]]
###### **སྡུག་བསྔལ་གྱི་རྒྱུ་སྤོང་བ་ལ་མཁས་པ།** ^1-1-4-5-1-1-1-0

[Block 625]
གང་འཁོར་བའི་རྒྱུན་གྱི་ཉོན་མོངས་པ་རྣམས་གཅོད་པ་དང་ཞེས་བྱ་བས་སྡུག་བསྔལ་གྱི་རྒྱུ་ཡོངས་སུ་སྤོང་བ་ལ་མཁས་པ་བསྟན་ཏེ། འཁོར་བར་རྒྱུན་དུ་སྐྱེ་བར་བྱེད་པའི༌[^522]རྒྱུ་འདོད་ཆགས་ལ་སོགས་པ་ཀུན་དུ་སྦྱོར་བའི་ཚོགས་ནི་འཁོར་བའི་རྒྱུན་གྱི་ཉོན་མོངས་པ་ཞེས་བྱའོ། །

[Block 626]
དེ་རྣམས་སྤོང་བར་བྱེད་པ་ནི་ཉོན་མོངས་པ་རྣམས་གཅོད་པ་ཞེས་བྱའོ། །

[Block 627 [HEADING]]
###### **བདེ་བའི་རྒྱུ་བསྐྱེད་པ་ལ་མཁས་པ།** ^1-1-4-5-1-1-2-0

[Block 628]
འཁོར་བའི༌[^523]རྒྱུན་གྱི་དགེ་བའི་རྩ་བ་རྣམས་མི་གཅོད་པ་དང་ཞེས་བྱ་བས་བདེ་བའི་རྒྱུ་བསྐྱེད་པ་ལ་མཁས་པ་བསྟན་ཏེ། གང་འཁོར་བ་ལ༌[^524]རྒྱུན་དུ་ལྷ་དང་མིར་སྐྱེ་བར་བྱེད་པའི་རྒྱུ་དགེ་བ་བཅུ་དང་། འདོད་མ་ཆགས་པ་དང་། ཞེ་མི་སྡང་བ་ལ་སོགས་པའི་དགེ་བའི་རྩ་བ་རྣམ་པ༌[^525]གཅིག་ནས་གཅིག་ཏུ་རྒྱུན་མི་འཆད་པར་བྱེད་པས་ནི།[^526] འཁོར་བའི་རྒྱུན་མི་དགེ་བའི་རྩ་བ་མི་གཅོད་པ་ཞེས་བྱའོ། །

[Block 629 [HEADING]]
###### **འཇིག་རྟེན་ལས་འདས་པའི་རྒྱུ་ལ་མཁས་པ།** ^1-1-4-5-1-2-0

[Block 630]
འཇིག་རྟེན་ལས་འདས་པའི་རྒྱུ་ལ་མཁས་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། བྱང་ཆུབ་ཆེན་པོའི་རྒྱུ་རྒྱུན་མི་གཅོད་པ་དང་། ཞི་བ་ཕྱོགས་གཅིག་པའི་རྒྱུ་སྒྲུབ་པར་མི་བྱེད་པའོ། །

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
--- END BLOCKS ---
