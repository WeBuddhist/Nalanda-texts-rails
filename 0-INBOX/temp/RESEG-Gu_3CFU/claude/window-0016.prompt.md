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
ཆོམ་རྐུན་པར་གྲགས་པ་ནི་རྒྱལ་མཚན་བཅིངས་པའོ། །

[Block 562]
གང་དུ་གང་ལ་རབ་ཏུ་གྲགས་པར་གྱུར་པ་ཉིད་མ་ཡིན་པ་དེར་དེ་ལ་རྒྱལ་མཚན་བཅིངས་པ་ཉིད་དོ། །

[Block 563]
ཤིང་རྟ་བྱེད་པ་དང་། ལྷམ་མཁན་དང་། གདོལ་པ་དང་། གཡུང་པོ་དང་། དེ་ལྟ་བུ་རབ་ཏུ་དབྱུང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། ཤིང་རྟ་བྱེད་པ་ནི་ལྷམ་མཁན་ནོ། །

[Block 564]
དེ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་ཟན་བཟའ་བར་མི་བྱ་བ་སྟེ། དགེ་ཚུལ་ཉིད་དང་སློབ་པ་ཉིད་ཀྱིས་བསྙེན་པར་རྫོགས་པར་འོས་པ་མ་ཡིན་པ་ཉིད་ཤིང་རྟ་མཁན་ལ་སོགས་པ་རྣམས་ལ་རབ་ཏུ་དབྱུང་བ་མ་ཡིན་པ་ཉིད་ཀྱི་རྒྱུ་མཚན་ནོ། །

[Block 565]
དེ་བས་ན་འདི་རྣམས་ལ་ཡང་མི་བྱ་བ་ཉིད་དུ་སྟོན་པའོ། །

[Block 566]
ལག་རྡུམ་ལ་སོགས་པ་ནི་མཚོན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདིར་རབ་ཏུ་དབྱུང་བའི་གཞི་ལས་ལག་རྡུམ་དང་རྐང་རྡུམ༌[^400]ལ་སོགས་པ་བརྗོད་པ་དེ་ནི་མཚོན་པར་རིག་པར་བྱ་སྟེ། ཡོངས་སུ་བགྲང་བ་ནི་མ་ཡིན་ནོ། །

[Block 567]
ད་ནི་གང་རྣམས་ཀྱིས་འདི་འཚོད་པ༌[^401]དེ་རྣམས་ཉེ་བར་དགོད་པར་བྱེད་དེ།

[Block 568 [VERSE]]
སྐྲ་སེར་དང་ནི་སྐྲ་སེར་སྐྱ། །
དེ་བཞིན་སྐྲ་ནི་ལྗང་གུ༌[^402]ཁ། །
མི་རྣམས་སྐྲ་ནི་དཀར་བ་དང་། །
གླང་ཆེན་སྐྲ་འདྲ་སྐྲ་མེད་དང་། །

[Block 569 [VERSE]]
མགོ་འབར་འབུར་ཅན་གླང་པོ་ཆེ། །
ཧ་ཅང་སྦོམ་དང་ལུས་གླེབས་འདྲ། །
བང་བུ་ཕག་གི་མགོ་ལྟ་བུ། །
མགོ་གཉིས་པ་དང་མགོ༌[^403]ཆུང་དང་། །

[Block 570 [VERSE]]
གླང་ཆེན་རྣ་འདྲ་རྟ་རྣ་འདྲ། །
བ་གླང༌[^404]རྣ་འདྲ་སྤྲེའུ་རྣ་འདྲ། །
བོང་བུའི་རྣ་འདྲ་ཕག་རྣ་འདྲ། །
རྣ་གཅིག་པ་དང༌[^405]རྣ་མེད་དང་། །

[Block 571 [VERSE]]
མིག་དམར་ཧ་ཅང་མིག་ཆེ་དང་། །
མིག༌[^406]ཆུང་མིག་ནི༌[^407]ཧ་ཅང་སེར། །
ཤེལ་མིག་མིག་ནི་ཆུ་བུར་འདྲ། །
མིག་གཅིག་པ་དང་མིག་མེད་དང་། །

[Block 572 [VERSE]]
གླང་ཆེན་སྣ་འདྲ་རྟ་སྣ་འདྲ། །
བ་གླང༌[^408]སྣ་འདྲ་སྤྲེའུ་སྣ་འདྲ། །
བོང་བུའི་སྣ་འདྲ་ཕག་སྣ་འདྲ། །
སྣ་སྦུབས་གཅིག་དང་སྣ་མེད་དང་། །

[Block 573 [VERSE]]
གླང་ཆེན་ཀོས་འདྲ་རྟ་ཀོས་འདྲ། །
བ་གླང༌[^409]ཀོས་འདྲ་སྤྲེའུ་ཀོས་འདྲ། །
བོང་བུའི་ཀོས་འདྲ་ཕག་ཀོས་འདྲ། །
ཀོས་སྨྱུང་དང་ནི་ཀོས་མེད་དང་། །

[Block 574 [VERSE]]
གླང་ཆེན་སོ་འདྲ་རྟ་སོ་འདྲ། །
བ་གླང༌[^410]སོ་འདྲ་སྤྲེའུ་སོ་འདྲ། །
བོང་བུའི་སོ་འདྲ་ཕག་སོ་འདྲ། །
སོ་གཅིག་པ་དང་སོ་མེད་དང་། །

[Block 575 [VERSE]]
མགུལ་རིངས་ཆེས་དང་མཇིང་ནུབ་དང་། །
ཕྲག་མིག་དང་ནི་ཆེས་སྒུར་དང་། །
ཕོ་མཚན་ཆད་དང་རླིག་རླུགས་དང་། །
རླིག་གཅིག་པ་དང་རླིག་མེད་དང་། །

[Block 576 [VERSE]]
ཧ་ཅང་རིང་དང་ཧ་ཅང་ཐུང་། །
སྐེམ་པོ་མ་འོས་ངལ་སྐྱེན་དང་། །
ཤ་མདོག་ཁ་དོག་རྣམ་བཞི་དང་། །
དེ་བཞིན་གྱོལ་པོ་ལུས་ཉམས་པའོ། །

[Block 577]
རྣམ་པ་དེ་ལྟ་བུ་དག་གི་དགག་པ་དེ་ཡང་རབ་ཏུ་གཟུང་བར་བྱའོ། །

[Block 578]
དེ་ཞེས་བྱ་བ་ནི་ལག་རྡུམ་དང་རྐང་རྡུམ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 579]
རྣམ་པ་དེ་དང་དེ་ལྟ་བུ་རྣམས་ཀྱི་དགག་པ་དེ་ཡང་རབ་ཏུ་གཟུང་ཞེས་བྱ་བ་ནི་གཟུང་བར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 580]
གང་རྣམས་ཀྱི་སྐྲ་ཡུང་བས་བཙོས་པ་ལྟ་བུ་དེ་དག་ནི་སྐྲ་སེར་ཅན་ནོ། །

[Block 581]
སྐྲ་སེང་གེའི་ལྟ་བུ་རྣམས་ནི་སྐྲ་སེར་སྐྱ་ཅན་ནོ། །

[Block 582]
གང་རྣམས་ཀྱི་སྐྲ་རམས་ཀྱིས་ཁ་བསྒྱུར་བ་ལྟ་བུ་དེ་རྣམས་ནི་སྐྲ་ལྗང་གུའོ། །

[Block 583]
[^411]གང་རྣམས་ཀྱི་སྐྲ་སྐྱེས་པ་ཉིད་ཀྱིས་དཀར་བ་དེ་རྣམས་ནི་དཀར་བའི་སྐྲ་ཅན་ཏེ། རྒས་པར་གྱུར་པ་ནི་མ་གཏོགས་སོ། །

[Block 584]
གང་རྣམས་ཀྱི་སྐྲ་གླང་པོ་ཆེའི་ལྟ་བུ་རྣམས་ནི་གླང་པོ་ཆེའི་སྐྲ་སྟེ་གླང་པོ་ཆེའི་སྤུ་འདྲ་བ་རྣམས་ཡིན་ནོ། །

[Block 585]
གང་རྣམས་ཀྱི་མགོ་སྐྲ་མེད་ཅིང་ཟངས་མའི་སྣོད་ལྟར་འཇམ་པ་དེ་རྣམས་ནི་སྐྲ་མེད་པའོ། །

[Block 586]
གང་གི་མགོ་སུལ་གསུམ་མམ༌[^412]

[Block 587]
བཞི་པ་དག༌[^413]རྣམས་ཀྱི་མཐོན་དམན་དུ་སྣང་བ་དེ་ནི་མགོ་འབར་འབུར༌[^414]ཅན་ནོ། །

[Block 588]
གང་རྣམས་ཀྱི་ལུས་གླེབས་པ་འདྲ་བར་རྒྱ་ཆེ་བ་ཉིད་ཀྱིས་སོ་སོ་དང་། འདྲ་བར་བསྡུས་པ་དེ་རྣམས་ནི་ལུས༌[^415]གླེབས་པ་ཅན་ནོ། །

[Block 589]
གང་གི་མིག་དག་ཧ་ཅང་ཆུང་ཞིང་ཟླུམ་པ་དེ་ནི་མིག་ཆུང་བའོ། །

[Block 590]
མགོ་བོ་ནང་དུ་ཞུགས་པ་ཉིད་ཀྱི་ཕྱིར༌[^416]ཕྲག་པའི་སྐབས་སུ་གང་ལ་མིག་དག་ཡོད་པ་དེ་ནི་ཕྲག་མིག་ཅན་ནོ། །

[Block 591]
ཕོ་མཚན་ནི་གཅི་བ་འབྱུང་བ་སྟེ། གང་གི་ཆད་པ་དེ་ནི་ཕོ་མཚན་ཆད་པའོ། །

[Block 592]
གང་རྣམས་ཀྱི་བྱ་བ་ཆུང་བས་ཀྱང་ཁྱད་པར་ཅན་གྱི༌[^417]ངལ་བ་བསྐྱེད་པ་དེ་རྣམས་ནི་ངལ་བ་སྐྱེན་པའོ། །

[Block 593]
རང་གི་ཤ་མདོག་བཞི་རྣམས་ཀྱིས། །ཞེས་བྱ་བ་ནི་སྔོ་བ་དང་། སེར་བ་དང་། དམར་བ་དང་། དཀར་བ་རྣམས་ཀྱིས་ཏེ། འདིས་ནི་རུས༌[^418]སྦལ་བརྗོད་པའོ། །

[Block 594]
གང་ཞིག་དེ་ལྟ་བུའི་རྣམ་པ་ཅན་ཁ་དོག་གི་བྱེ་བྲག་རྣམས་ལ་སྨད་པའི་ངོ་བོ་དེ༌[^419]རྣམས་ལ་འདི་བཀག་པ་སྟེ། གང་ཞིག་ལྷ་རྣམས་ཀྱི་དང་འདྲ་བར་ཤིས་པའི་ངོ་བོ་ཅན་དེ་རྣམས་ནི་མ་ཡིན་ནོ། །

[Block 595]
དེ་ལྟར་རེ་ཞིག་འདི་ལྟ་བུ་རྣམས་ལ་རབ་ཏུ་བྱུང་བ་ལ་སོགས་པ་བཀག་ཟིན་ཏོ། །

[Block 596]
རབ་ཏུ་བྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་འདི་རྣམས་ལ་ཡང་བསྡུ་བར་མི་བྱ་ཞེས་བྱ་བ་ཉེ་བར་སྟོན་པར་བྱེད་ཅིང་རིགས་དང་ལུས་ལ་སྐྱོན་ཆགས་པ་རབ་ཏུ་བྱུང་བ་ནི་ཉེ་བར་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རིགས་ལ་སྐྱོན་ཆགས་པ་ཤིང་རྟ་མཁན་པོ་ལ་སོགས་པ་ཟན་བཟའ་བར་མི་བྱ་བ་རྣམས་སོ། །

[Block 597]
ལུས་ལ་སྐྱོན་ཆགས་པ་ནི་དབྱིབས་དང་ཁ་དོག་ལས་ཏེ་ལག་རྡུམ་ལ་སོགས་པའོ། །

[Block 598]
ཉེ་བར་གཞག་པར་མི་བྱ་བ་ནི་གནས་སྦྱིན་པ་གཅིག་པུར་མ་ཟད་ཀྱི༌[^420]གནས་ཁང་གི་ཡང་ནང་དུ་མི་སྦྱིན་པ་དང་རྗེས་སུ་འབྲང་བའི་འཁོར་ཉིད་ཀྱིས་སོ། །

[Block 599]
དེ་ལྟར་ཡང་དགེ་སློང་གིས༌[^421]འཁོར་སུན་འབྱིན་པའི་འཁོར་ཉེ་བར་གཞག་པར་མི་བྱ་སྟེ། ཉེ་བར་འཇོག་པར་འགྱུར༌[^422]ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་ན། ཇི་ཙམ་གྱིས་ན་འཁོར་སུན་འབྱིན་པའི་འཁོར་ཡིན་པར་བརྗོད་པར་བྱ་ཞེ་ན། རིགས་ལས་དང་ཁ་དོག་ལས་དང་དབྱིབས་ལས་ཏེ། ཇི་ལྟར་རིགས་ལས་ཤེ༌[^423]ན་ཤིང་རྟ་མཁན་དང་གདོལ་པ་དང་གཡུང་པོའི་རིགས་ལས་སོ། །

[Block 600]
ཇི་ལྟར་རིགས་དང་དབྱིབས་ལས་ཤེ༌[^424]ན་སྐྲ་སེར་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིར་སྨོས་སོ། །
--- END BLOCKS ---
