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
དེའི་ཕྱིར་རྣམ་པར་རིག་པ་ཙམ་ཡིན་གྱི་དོན་ནི་མེད་དོ།[^412] །ཡང་རྣམ་པ་གཉིས་ཉིད་ནི་རྒྱུ་མཚན་དང་བཅས་པ་དང་། ལྟ་བ་ཅན་གྱི༌[^413]རྣམ་པར་ཤེས་པས་རྣམ་པར་གཞག་པར་འགྱུར་རོ། །

[Block 562]
གལ་ཏེ་རྣམ་པར༌[^414]རིག་པ་ཙམ་གཅིག་པོ་དེའི་ཆ་གཅིག་ནི་རྒྱུ་མཚན་ཡིན་ལ།

[Block 563]
གཉིས་པ་ནི་ལྟ་བར་འགྱུར་ན། དེས་ན་ཡང་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་རྣམས་གཉིས་ཉིད་དེ། སྣ་ཚོགས་ཀྱི་ངོ་བོ་ཉིད་དུ་རྣམ་པར་བཞག་པས་ཡང་རྣམ་པར་རིག་པ་ཙམ་གཅིག་པོ་དེ་ཉིད་ལ་ཇི་ལྟར་རིགས་པ་ཆ་གཅིག་ནི་སྣ་ཚོགས་སུ་འབྱུང་བར་འགྱུར་ལ། གཉིས་པས་ནི་འདི་ལྟར་འཛིན་པར་བྱེད་དོ། །

[Block 564]
ཡང་གང་གི་ཕྱིར་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་འཛིན་པར་བྱེད་པ་དེས་ན་མིག་ལ་སོགས་པའི་རྣམ་པར་རིག་པ་ཆོས་ཀྱི་མཐར་ཐུག་པ་ཐམས་ཅད་ནི༌[^415]རྒྱུ་མཚན་ཡིན་པས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་འདི་ལྟར༌[^416]ལྟ་བ་ཞེས་བྱའོ། །

[Block 565]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དེ་དག༌[^417]ཉིད་ནི་རྒྱུ་ཞེས་བྱ་བར་ཡང་བསྟན་ཏེ་སོ་སོར་ངེས་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 566]
ཡང་གཞན་དག་ནི་ཡུལ་སོ་སོར་ངེས་པ་ཡིན་པའི་ཕྱིར་དང་། རྣམ་པར་རྟོག་པ་མེད་པ་ཉིད་དེ། དེས་ན་གང་རྣམ་པར་རྟོག་པ་ཅན་དེ་ནི་ལྟ་བ་ཞེས་བྱའོ། །

[Block 567]
དེ་ལྟར་ན་འདི་ནི་རྣམ་པར་རིག་པ་ཙམ་དུ་རྣམ་པར་གཞག་པའོ། །

[Block 568]
ཚིགས་སུ་བཅད་པ༌[^418]དེ་ཙམ་སྟེ། དོན་མེད་པ་ལ་འཇུག་པ་ཉིད་དེ། དེ་ཙམ་གཉིས་དང་སྟེ་རྒྱུ་མཚན་དང་བཅས་པ་དང་། ལྟ་བ་ཅན་གྱི་རྣམ་པར་རིག་པ་ཙམ་མོ། །

[Block 569]
སྣ་ཚོགས་ཉིད་འཇུག་པ་སྟེ། གང་སྣ་ཚོགས་ཀྱི་རྣམ་པ་ཅན་ཉིད་དུ་འབྱུང་བའི་རྣམ་པར་ཤེས་པ་དེའིའོ། །

[Block 570]
རྣལ་འབྱོར་པ་རྣམས་རྟོགས་པར་འདོད། །ཅེས་བྱ་བ་ནི་རྣལ་འབྱོར་སྤྱོད་པ་པ་རྣམས་འདི་ལྟར་འདོད་པའོ། །གང་དུ་ཞེ་ན།

[Block 571 [VERSE]]
སེམས་ཙམ་ལ་ནི་ཞུགས་གྱུར་པ། །
དེ་དང་བྲལ་ན་དེ་ཕྱིར་ཡང་། །

[Block 572]
ཞེས་བྱ་བ་སྟེ། འདི་ལྟར་ཡང་སེམས་ཙམ་ལ་ཞུགས་པས་དོན་མེད་པ་བྲལ་བར་ཡང་འགྱུར་རོ། །

[Block 573]
ཡང་གལ་ཏེ་གཟུང་བའི་དོན་མེད་ན་སེམས་ཀྱིས་གང་ལ༌[^419]འཛིན་པར་འགྱུར་ཞེ་ན། དེ་ཙམ་ཉིད་དང་། གཉིས་ཉིད་དང་། སྣ་ཚོགས་ཉིད་ལ་ཞུགས་པར་གྱུར་ན། རྒྱུ་ཙམ་དུ་བསྟན་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། གཞན་དང་མཚུངས་སོ། །

[Block 574]
བྱང་ཆུབ་སེམས་དཔའ་ཁ་ཅིག་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་གཅིག་པུ་ཉིད་དུ་འདོད་དོ། །

[Block 575]
གང་ཡང་དེའི་རིམ་པ་རྣམ་པར་གཞག་པ་བསྟན་པར་བྱ་སྟེ། དེ་ལ་སེམས་པ་ལ་ལུས་དང་ངག་གི་ལས་ཞེས་བྱ་བ་བཞིན་ནོ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་སེམས་པ་ལུས་ཀྱི་སྒོ་ནས་ཞུགས་པར་གྱུར་པ་ན་ལུས་ཀྱི་ལས་ཞེས་བྱ༌[^420]ལ། ངག་གི་སྒོ་ནས་ནི་ངག་གི་ལས་ཞེས༌[^421]བྱ། ཡིད་ཀྱི༌[^422]ལས་ནི་ཡིད་ཀྱི་ལས་ཞེས་བྱ་བ་ཐོབ་པ་བཞིན་དུ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་གཅིག་པུ་ཡིན་ན་ཡང་མིག་ལ་བརྟེན༌[^423]ནས་འཇུག་པ་ན་དེ་མིག་གི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བའི་མིང་འཐོབ༌[^424]ལ། དེ་བཞིན་དུ་ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བའི་བར་གྱི་མིང་འཐོབ་ཀྱི། ཡང་དེ་ལ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་མ་ཡིན་པ་རྣམ་པར་ཤེས་པ་གཞན་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ལྟ་བུ་ནི་མེད་དོ། །

[Block 576]
དེ་ལྟར་ན་རྟེན་ཐམས་ཅད་དུ་འབྱུང་བ་ན་གང་གི་སྣ་ཚོགས་ཀྱི་རྣམ་པ་གཉིས་སུ་སྣང་བ་བྱུང༌[^425]སྟེ། དེ་དོན་ཙམ་དུ་སྣང་བ་དང་། རྣམ་པར་རྟོག་པར་སྣང་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་འདི་དག་གིས་ཡོངས་སུ་སྤོང་ངོ་། །དེ་ལ་རྟེན་ཐམས་ཅད་དུ་ཞེས་བྱ་བ་ནི་མིག་ལ་སོགས་པའི་རྟེན་ཐམས་ཅད་དུའོ། །

[Block 577]
སྣ་ཚོགས་ཀྱི་རྣམ་པ་གཉིས་སུ་སྣང་བ་ཞེས་བྱ་བ་ནི་དེ་དོན་ཙམ་དུ་སྣང་བ་དང་། རྣམ་པར་རྟོག་པར་སྣང་བའི་ཕྱིར་རོ་ཞེས་བྱ་བའི་ཚིག་གཉིས་ཀྱིས༌[^426]སྟོན་པར་བྱེད་དོ། །

[Block 578]
གང་ཚིག་གཉིས་པོ་འདིས་ནི་རྣམ་པར་ཤེས་པ་གཅིག་པོ་དེ་ཉིད་ཀྱི་ཆ་གཅིག་ནི་དོན་ཙམ་དུ་སྣང་བར་འགྱུར་ལ། ཡང་དེ༌[^427]

[Block 579]
གཉིས་པ་ནི་དོན་གྱི་རྣམ་པར་རྟོག་པའི་རྣམ་པ༌[^428]འབྱུང་སྟེ། དེས༌[^429]ན་སྔར་སྨྲས་པའི་སྐྱོན་མེད་དོ། །

[Block 580]
གང་གི་ཕྱིར་གཟུགས་ཡོད་ན་ཐམས་ཅད་དུ་རེག་བྱའི་སྣང་བ་འབྱུང་བར་འགྱུར་ཏེ། གང་གི་ཕྱིར་མཉམ་པར་གཞག་པ་ན་རྣམ་པར་ཤེས་པ་ལྔ་ནི་ཉེ་བ་མ་ཡིན་ལ། ནང་གི་ཉམས་སུ་མྱོང་བ་ནི་འབྱུང་བར་འགྱུར་ཏེ་དེ་ལས་གཞན་པའི་དབང་པོ་གཟུགས་ཅན་ལུས་ལ་གནས་པ་བཞིན་དུ་བྱ་བ་སྟེ། དེ་ཇི་ལྟར་ལུས་ལ་གནས་པའི་དབང་པོ་མིག་ལ་སོགས་པ་གཞན་རྣམས་ལུས་དེ་ལ་གནས་པ་ཡིན་པའི་ཕྱིར། དབང་པོའི་རང་གི་གནས་ཉིད་དེ་ལ་དེས་བྱས་པའི་ཕན་འདོགས་པ་དང་གནོད་པ་ཉེ་བར་སྒྲུབ་པར་བྱེད་དོ། །

[Block 581]
དེ་བཞིན་དུ་འདིར་ཡང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་ལུས་ལ་གནས་པ་ཡིན་པའི་ཕྱིར་ལུས་འགྱུར་བར་བྱེད་པར་འདོད་པར་བྱའོ། །

[Block 582]
དོན་གཞན་ཡང་ཇི་ལྟར༌[^430]ལུས་ཀྱི་དབང་པོ་རྣམས་ལུས་ལ་བརྟེན་པ༌[^431]ཉིད་ན་ཕྱི་རོལ་གྱི་རྐྱེན་རེག་པར་བྱ་བ་ཡོད་ན་ལུས་ཀྱི་དབང་པོ་ལ་ཡང་རེག་བྱའི་སྣང་བ་འབྱུང་བར་འགྱུར་ཏེ། དེ་བྱུང་བར་གྱུར་པ་ན་རང་གི་རྟེན་ལུས་ལ་ཕན་འདོགས་པའམ། གནོད་པར་འགྱུར་བར་བྱེད་པར་འགྱུར་རོ། །

[Block 583]
དེ་བཞིན་དུ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཡང་ལུས་ལ་བརྟེན་པ༌[^432]ཡིན་པའི་ཕྱིར་རེག་བྱའི་སྣང་བ༌[^433]བྱུང་ནས་ལུས་ལ་ཕན་འདོགས་པ་དང་། གནོད་པ་སྒྲུབ་པར་བྱེད་དོ། །

[Block 584]
འདི་དག་གི་ལུས་ནི་གལ་ཏེ་མིག་ལ་སོགས་པ་རྣམ་པར་རྟོག་པ་མེད་པ་དེ་ལ་བརྟེན་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་འཇུག་པ་ཡང་རྣམ་པར་རྟོག་པ་མེད་པ་ཉིད་ཐོབ་པར་འགྱུར་ཏེ། ཇི་ལྟར་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཀུན་ནས་ཉོན་མོངས་པ་ལ་བརྟེན་ནས༌[^434]ཉོན་མོངས་པ་ཅན་དུ་འབྱུང་བ་བཞིན་ནོ། །

[Block 585]
དེ་ཡང་བྱང་ཆུབ་སེམས་དཔས་ཚིགས་སུ་བཅད་པས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ་ལ། རིང་དུ་འགྲོ་ཞེས་བྱ་བ་ནི་ཡུལ་ཐམས་ཅད་ལ་དམིགས་པ་ཅན་ཉིད་ཀྱིས་སོ། །

[Block 586]
གཅིག་པུ་རྒྱུ་བ་ནི་གཉིས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 587]
གང་ཞིག་ལུས་མེད་ཅེས་བྱ་བ་ནི་ལུས་དང་བྲལ་བ་ཉིད་དོ། །

[Block 588]
ཕུག་གནས་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ཕུག་གི་ནང་ན་གནས་པ་ཉིད་དོ། །

[Block 589]
སེམས་འདུལ་བྱེད་ཅེས་བྱ་བ་ནི་དབང་དུ་བྱེད་པའོ། །

[Block 590]
གདུལ་བར་དཀའ་བ་ཞེས་བྱ་བ་ནི་བཅོས་དཀའ་བའོ། །

[Block 591]
ཡང་ལུང་ནི་འདི་དག་གི་སྤྱོད་ཡུལ་གྱི་ཡུལ་ནི་ཡིད་ཀྱིས་སོ་སོར་ཉམས་སུ་མྱོང་སྟེ་ཞེས་བྱ་བ་ལ། གང་དབང་པོའི་སྤྱོད་ཡུལ་དུ་བསྟན་པའི་ཡུལ་དེ་ནི་ཡིད་ཀྱིས་རེ་རེ་ཞིང་སོ་སོ་སོ་སོར་ཉམས་སུ་མྱོང་བར་འགྱུར་ཏེ། ཆོས་ཐམས་ཅད་ལ་རྣམ་པར་རྟོག་པ་ཅན་ཡིན་པའི་ཕྱིར་སོ་སོར་ཉམས་སུ་མྱོང་བའོ། །

[Block 592]
ཡིད་ནི་འདི་དག་གི་རྟེན་པའོ༌[^435]ཞེས་བྱ་བ་ལ། གང་གི་ཕྱིར་ཡིད་གཡེང་བར༌[^436]གྱུར་ན་དེ་དག་འབྱུང་བར་མི་འགྱུར་བས་དབང་པོ་དེ་དག་འབྱུང་བའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 593]
ཡང་ལུང་གིས་ནི་རྣམ་པར་ངེས་པའི༌[^437]ཚོགས་དྲུག་ནི་ཡིད་ཅེས་བྱ་བའི་སྒྲས་བསྟན་གྱི་རྣམ་པར་ཤེས་པ་གཞན་གྱི་སྒྲས་ནི་མ་ཡིན་ཏེ། རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་ནི་ཡིད་ཀྱི་སྐྱེ་མཆེད་དོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 594]
དེས་ན་ཡིད་འབའ་ཞིག་ནི་ཡོད་དོ་ཞེས་འདི་ལྟར་རྟོགས་པར་བྱའོ། །

[Block 595]
མཚན་མའི་ལྟ་བ་དང་བཅས་པའི་རྣམ་པར་ཤེས་པ་རྣམ་པར་གཞག་པར་བྱ་བ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་སྟེ། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ༌[^438]ཀུན་གཞི་རྣམ་པར་ཤེས་པ་དང་བཅས་པ་ནི་ལྟ་བའོ། །

[Block 596]
མིག་ལ་སོགས་པ་རྣམ་པར་རེག་པ༌[^439]ནི་རྒྱུ་མཚན་ནོ། །

[Block 597]
དེ་ནི་ཆོས་ཐམས་ཅད་ཀྱང་ཡིན་ལ་རྣམ་པར་རིག་པ་ཙམ་ཡང་ཡིན་པས་རྣམ་པར་རིག་པ་རྒྱུ་མཚན་དུ་གྱུར་པ་དེ་དག་ཉིད་ཅེས་བྱ་བ་སྟེ། མིག་ལ་སོགས་པ་འབྱུང་བའི་རྒྱུར་གྱུར་པ་ནི་དམིགས་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 598]
དེའི་ལྟ་བ་འབྱུང་བའི༌[^440]རྒྱུ་མཚན་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ལྟ་བ་ཡིན་པ་ནི་དེའི་ལྟ་བའོ། །

[Block 599]
དེ་ལྟ་བ་ཉིད་དུ་སྣང་བར་གྱུར་པ་ན་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ལྟ་བ་རྒྱུན་མི་འཆད་པར་གནས་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རྟེན་གྱི་བྱ་བ་བྱེད་དོ་ཞེས་བརྗོད་དོ། །

[Block 600]
རྣམ་པར་ཤེས་པ་མི་མཐུན་པའི་རྒྱུ་མཚན་ཉིད་ཤེས་པས་ནི་ཞེས་བྱ་བ་ལ། རྣམ་པར་ཤེས་པ་མི་མཐུན་པ་རྣམས་ཀྱི་རྒྱུ་མཚན་ནི་དོན་ཡིན་ནོ། །ཤེས་པར་བྱེད་པས་ན་ཤེས་པའོ། །
--- END BLOCKS ---
