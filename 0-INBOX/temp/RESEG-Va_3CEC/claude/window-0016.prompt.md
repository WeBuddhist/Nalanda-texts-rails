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
[Block 561 [HEADING]]
###### **འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་འབྱོར་པ་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-5-10-1-3-0

[Block 562]
ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་རྙེད་པ་ཞེས་བྱ་བས་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་འབྱོར་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ཐེག་པ་དེ་ལ་བརྟེན་ནས༌[^482]འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་བས། ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་རྙེད་པ་ཞེས་བྱའོ། །

[Block 563 [HEADING]]
###### **མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་ལམ་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-5-10-1-4-0

[Block 564]
མི་སླུ་བའི་ལམ་དུ་འགྲོ་བ་ཞེས་བྱ་བས་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་ལམ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། མི་སླུ་བའི་ལམ་ནི་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་ལམ་མོ། །

[Block 565]
ཐེག་པ་འདིས་ཀྱང་ལམ་དེར་འགྲོ་བ་འམ། ལམ་དེ་དང་མཐུན་པའི་ཕྱིར་མི་སླུ་བའི་ལམ་དུ་འགྲོ་བའོ། །

[Block 566 [HEADING]]
###### **གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-5-10-2-0

[Block 567]
སེམས་ཅན་ཐམས་ཅད་ཉེ་བར་འཚོ་བ༌[^483]ཞེས་བྱ་བས་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ཐེག་པ་དེ་ལ་ཞུགས་ན་སེམས་ཅན་ཐམས་ཅད་ཕན་པ་དང་བདེ་བ་ཐོབ་པར་འགྱུར་བའི་ཕྱིར་སེམས་ཅན་ཐམས་ཅད་ཉེ་བར་འཚོ་བ་ཞེས་བྱའོ། །

[Block 568 [HEADING]]
###### འབྲས་བུ་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན། ^1-1-3-5-11-0

[Block 569]
ཐེག་པ་དེ་ནི་ཐམས་ཅད་དུ་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཞེས༌[^484]བྱ་བ་ལ་སོགས་པས་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན་བསྟན་ཏེ། རྣམ་པ་ཐམས་ཅད་དུ་དུས་ཐམས་ཅད་དུ། གནས་ཐམས་ཅད་དུ། ཕྱོགས་ཐམས་ཅད་དུ་ཁ་ན་མ་ཐོ་བ་མེད་པས་ན་ཐེག་པ་དེ་ནི་ཐམས་ཅད་དུ་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཞེས་བྱ་སྟེ། རྣམ་པ་ཐམས་ཅད་ནི་སྡིག་པ་མི་དགེ་བའི་ཆོས་ཐམས་ཅད་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 570]
དུས་ཐམས་ཅད་དུ་ནི་དུས་གསུམ་དུ་ཡང་སྡིག་པ་མི་དགེ་བའི་ཆོས་མི་བྱེད་པས་སོ། །

[Block 571]
གནས་ཐམས་ཅད་ནི་ལྷ་དང་མིའི་གནས་གང་དུ་ཕྱིན་ཀྱང་སྡིག་པ་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 572]
ཕྱོགས་ཐམས་ཅད་ནི་ཕྱོགས་བཅུ་ཀུན་དུ་སྡིག་པ་མི་བྱེད་པས་སོ། །

[Block 573]
ཆོས་འོག་ནས་སྨོས་པ་རྣམས་ཀྱི་རྒྱན་གྱིས་བརྒྱན་པ་ཞེས་བྱ་སྟེ། དེ་དག་ནི་གོང་དུ་བཤད་པར་ཟད་དོ། །

[Block 574 [HEADING]]
##### གོང་དུ་བཤད་པ་རྣམས་མཇུག་བསྡུ་བ། ^1-1-3-6-0

[Block 575]
གོང་དུ་བཤད་པ་རྣམས་མཇུག་བསྡུ་བའི་ཕྱིར། གང་འདི་ལ་མཁས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གང་འདི་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་གོང༌[^485]དུ་བཤད་པ་རྣམས་ལའོ། །

[Block 576 [HEADING]]
#### ཆོས་ཐམས་ཅད་ལ་མཁས་པ། ^1-1-4-0

[Block 577]
ཆོས་ཐམས་ཅད་ལ་མཁས་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཆོས་ཐམས་ཅད་ལ་མཁས་པ་གང་ཞེ་ན་ཞེས་དྲིས་སོ། །

[Block 578]
དྲིས་པའི་ལན་གདབ་པའི་ཕྱིར༌[^486]ཆོས་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་མདོར་ན་འདུས་བྱས་དང་འདུས་མ་བྱས་ཞེས་བྱ་བ་གསུངས་ཏེ། འདུས་བྱས་དང་འདུས་མ་བྱས་སུ་ཆོས་ཐམས་ཅད་འདུས་པས་འདུས་པའི་དོན་གྱིས་དེ་གཉིས་ལ་ཆོས་ཐམས་ཅད་ཅེས་བྱའོ། །

[Block 579]
དེ་ལ་གང་རྒྱུ་དང་རྐྱེན་གྱིས་བསྐྱེད་པའི་ཟག་པ་དང་བཅས་པའི་ཆོས་དང་། ཟག་པ་མེད་པའི་ཆོས་ནི་འདུས་བྱས་སོ། །

[Block 580]
གང་རྒྱུ་དང་རྐྱེན་གྱིས་མ་བསྐྱེད་པ་དེ་བཞིན་ཉིད་དང་ཡང་དག་པའི༌[^487]མཐའ་དང་སྟོང་པ་ཉིད་དང་ཆོས་ཀྱི་དབྱིངས་ནི་འདུས་མ་བྱས་སོ། །

[Block 581]
དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་འདུས་བྱས་དང་། འདུས་མ་བྱས་ལ་མཁས་པར་བྱ་སྟེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ཁོང་དུ་ཆུད་པར་བྱ་སྟེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 582 [HEADING]]
##### འདུས་བྱས་ལ་མཁས་པ། ^1-1-4-1-0

[Block 583]
གང་དེ་དག་ལུས་ཀྱི༌[^488]འདུ་བྱེད་དགེ་བ་དང་། ངག་གི་འདུ་བྱེད་དགེ་བ༌[^489]དང་། ཡིད་ཀྱི་འདུ་བྱེད་དགེ་བ་ཞེས་བྱ་བ་ལ། སྲོག་མི་གཅོད་པ་དང་། མ་བྱིན་པར་མི་ལེན་པ་དང་། འདོད་པས་ལོག་པར་མི་གཡེམ་པ་ནི་ལུས་ཀྱི༌[^490]འདུ་བྱེད་དགེ་བའོ། །

[Block 584]
བརྫུན་དང་ཕྲ་མ་དང་ངག་རྩུབ་པོ་དང་ཚིག་ཀྱལ་པའི་ཚིག་མི་སྨྲ་བ་ནི་ངག་གི་འདུ་བྱེད་དགེ་བའོ། །

[Block 585]
བརྣབ༌[^491]སེམས་དང་གནོད་སེམས་དང་ལོག་པར་ལྟ་བ་སྤངས་པ་ནི་ཡིད་ཀྱི་འདུ་བྱེད་དགེ་བ་ཞེས་བྱའོ། །

[Block 586]
དེ་དག་ཐམས་ཅད་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་བསྔོ་བ༌[^492]ཞེས་བྱ་བ་ལ། དེ་དག་ཅེས་བྱ་བ་ནི་གོང་དུ་སྨོས་མ་ཐག་པའི་འདུ་བྱེད་རྣམ༌[^493]གསུམ་མངོན་པར་འདུས་བྱས་པའོ། །

[Block 587]
བླ་ན་མེད་པ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་དེ་སྤོང་བ་དང་། ཡེ་ཤེས་དང་སྒྲུབ་པ་དང་དུས་དང་ཐོབ་པ༌[^494]དང་ལྡན་པ་དང་སྤྱོད་པ་ལ་སོགས་པས༌[^495]ཉན་ཐོས་ཀྱི་བྱང་ཆུབ་ལས་ཁྱད་ཞུགས་པའི་ཕྱིར་བླ་ན་མེད་པ་ཞེས་བྱའོ། །

[Block 588]
དེ་ལ་སྤོང་པ་ཁྱད་ཞུགས་པ་ནི་ཉན་ཐོས་ཀྱི་བྱང་ཆུབ་ཀྱིས་ཉོན་མོངས་པའི་སྒྲིབ་པ་ཙམ་སྤོང་བར་ཟད་ཀྱི། འདིས་ནི་ཉོན་མོངས་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པ་གཉིས་སྤངས་པས༌[^496]སྤོང་བ་ཁྱད་ཞུགས་སོ། །

[Block 589]
ཡེ་ཤེས་ནི་གང་ཟག་ལ་བདག་མེད་པ་ཙམ་ཁོང་དུ་ཆུད་པར་ཟད་ཀྱི། འདིས་ནི་གང་ཟག་དང་ཆོས་ལ་བདག་མེད་པའི་ཡེ་ཤེས་ཁོང་དུ་ཆུད་པས་སོ། །

[Block 590]
སྒྲུབ་པ་ནི་ཉན་ཐོས་ལ་སོགས་པས༌[^497]བདག་གི་དོན་བསྒྲུབ་པ་ཙམ་དུ་ཟད་ཀྱིས༌[^498]འདིས་ནི་བདག་དང་གཞན་གྱི་དོན་སྒྲུབ༌[^499]པར་བྱེད་པས་ན་སྒྲུབ་པ་ཁྱད་ཞུགས་སོ། །

[Block 591]
དུས་ནི་ཉན་ཐོས་ལ་སོགས་པ༌[^500]ཚེ་གསུམ་མམ་བདུན་གྱི་བར་དུ་སྦྱོར་བ་ཙམ་དུ་ཟད་ཀྱི་འདི་ནི་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱི་བར་དུ་སྦྱོར་བས་ན་དུས་ཁྱད་ཞུགས་སོ། །

[Block 592]
ཐོབ་པ་ནི་ཉན་ཐོས་ཀྱིས་དགྲ་བཅོམ་པའི་འབྲས་བུ་ཐོབ་པར་ཟད་ཀྱི། འདིས་ནི་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་འབྲས་བུ་ཐོབ་པས་ན་ཐོབ་པ་ལ༌[^501]ཁྱད་ཞུགས་སོ། །

[Block 593]
ལྡན་པ་ནི་ཉན་ཐོས་དག་ཟད་པར་གྱི༌[^502]སྐྱེ་མཆེད་དང༌[^503]ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་ལ་སོགས་པའི༌[^504]ཡོན་ཏན་དང་ལྡན་པར་ཟད་ཀྱི། འདི་ནི་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པ༌[^505]ཡོན་ཏན་དང་ལྡན་པས་ན་ལྡན་པ་ཁྱད་ཞུགས་སོ། །

[Block 594]
སྤྱོད་པ་ནི་ཉན་ཐོས་ལ་སོགས་པས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་མི་སྤྱོད་ཀྱི། འདིས་ནི་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པས་ན་སྤྱོད་པ་ཁྱད་ཞུགས་སོ། །

[Block 595]
ཡང་དག་པར་རྫོགས་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཕྱིན་ཅི་མ་ལོག་པར་ཐུགས་སུ་ཆུད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

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
--- END BLOCKS ---
