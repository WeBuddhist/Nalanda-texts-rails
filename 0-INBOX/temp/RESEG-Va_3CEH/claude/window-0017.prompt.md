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
མིག་ལ་སོགས་པ་རྣམ་པར་རེག་པ༌[^439]ནི་རྒྱུ་མཚན་ནོ། །

[Block 597]
དེ་ནི་ཆོས་ཐམས་ཅད་ཀྱང་ཡིན་ལ་རྣམ་པར་རིག་པ་ཙམ་ཡང་ཡིན་པས་རྣམ་པར་རིག་པ་རྒྱུ་མཚན་དུ་གྱུར་པ་དེ་དག་ཉིད་ཅེས་བྱ་བ་སྟེ། མིག་ལ་སོགས་པ་འབྱུང་བའི་རྒྱུར་གྱུར་པ་ནི་དམིགས་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 598]
དེའི་ལྟ་བ་འབྱུང་བའི༌[^440]རྒྱུ་མཚན་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ལྟ་བ་ཡིན་པ་ནི་དེའི་ལྟ་བའོ། །

[Block 599]
དེ་ལྟ་བ་ཉིད་དུ་སྣང་བར་གྱུར་པ་ན་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ལྟ་བ་རྒྱུན་མི་འཆད་པར་གནས་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རྟེན་གྱི་བྱ་བ་བྱེད་དོ་ཞེས་བརྗོད་དོ། །

[Block 600]
རྣམ་པར་ཤེས་པ་མི་མཐུན་པའི་རྒྱུ་མཚན་ཉིད་ཤེས་པས་ནི་ཞེས་བྱ་བ་ལ། རྣམ་པར་ཤེས་པ་མི་མཐུན་པ་རྣམས་ཀྱི་རྒྱུ་མཚན་ནི་དོན་ཡིན་ནོ། །ཤེས་པར་བྱེད་པས་ན་ཤེས་པའོ། །

[Block 601]
དམིགས་པ་མེད་པའི་རྣམ་པར་རིག་པ་དམིགས་པས་ཞེས་བྱ་བ་ནི་དམིགས་པ་མེད་པར་ཡང་རྣམ་པར་ཤེས་པ་འབྱུང་བ་ནི་ལྟ་བ་སྟེ། དཔེར་ན་འདས་པ་ལ་སོགས་པ་དམིགས་པ་ལྟ་བུའོ། །

[Block 602]
འབད་པ་མེད་པར་ཡང་ཕྱིན་ཅི་ལོག་མེད་པར་ཐལ་བར་འགྱུར་ཏེ་འདི་ལྟར་ཤེས་པའོ། །ཤེས་པ་རྣམ་པ་གསུམ་གྱི་རྗེས་སུ་མཐུན་པར༌[^441]ཤེས་པས་ནི་ཞེས་བྱ་བ་ལ། གང་གི་ཕྱིར་དོན་ནི་འདི་ལྟར་འགྱུར་ཏེ། ཇི་ལྟར་སྣང་བ་དེ་མེད་པར་ཡང་གཉེན་པོ་འབྱུང་བར་འགྱུར་བས་ཕྱིན་ཅི་ལོག་མེད་པར་ཐལ་བར་འགྱུར་ཏེ་འདི་ལྟར་ཤེས་པའོ། །ཤེས་པ་རྣམ་པ༌[^442]གསུམ་གྱི་རྗེས་སུ་མཐུན་པར་ཤེས་པས་ཞེས་བྱ་བ་ནི་དོན་དེ་ཤེས་པས༌[^443]རྣམ་པ་གསུམ་གྱི་རྗེས་སུ་མཐུན་པར་ཤེས་ཞེས་བྱ་བའོ། །

[Block 603]
བསམ་གཏན་པ་ཞེས་བྱ་བ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་ཞེས༌[^444]བྱ་བ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་སོ། །

[Block 604]
སེམས་ལ་དབང་ཐོབ་པས༌[^445]ཞེས་བྱ་བ་ནི་སེམས་ལས་སུ་རུང་བ་ཐོབ་པའོ།[^446] །མོས་པའི་དབང་གིས་དེ་ལྟར་དོན་དེ་དག་སྣང་བ་ཞེས་བྱ་བ་ལ། གལ་ཏེ་སའི་རང་བཞིན་དུ་མོས་ནས༌[^447]ཡང་དེ་བཞིན་དུ་འགྱུར་ལ། དེ་བཞིན་དུ་མེ་ལ་སོགས་པ་ལ་ཡང་དོན་དེ་བཞིན་དུ་བལྟའོ། །

[Block 605]
ཞི་གནས་ཐོབ་པ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་ཐོབ་པའོ། །

[Block 606]
ཆོས་ལ་ལྷག་མཐོང་ལ་བརྩོན་པ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་ལ་སོགས་པ་ལ་སྤྱོད་པ༌[^448]ལ་བརྩོན་པ་རྣམས་སོ། །

[Block 607]
ཡིད་ལ་བྱེད་པ་ཙམ་དུ་དོན་སྣང་བ་ཞེས་བྱ་བ་ནི་དོན་གཅིག་ལ་ཡང་ཇི་ལྟ་ཇི་ལྟར་ཡིད་ལ་བྱས་པ་དེ་ལྟ་དེ་ལྟར་རྣམ་པ་མང་པོ་སྣང་བའོ། །

[Block 608]
རྣམ༌[^449]པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཐོབ་པ་ཞེས་བྱ་བ་ལ། དྲུག་པོ་ལ་སྣང་བའི་དོན་ཇི་ལྟ་བ་བཞིན་དུ་ཡོད་པ་ཡིན་ན་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 609]
དེ་ལྟ་ན་ཡང་དེ་ཡོད་པའི་དུས་ན་ཡང་དོན་གྱི་ངོ་བོ་ཉིད་མེད་པ་ནི་ངེས་པར་ཁས་བླང་བར་བྱའོ། །

[Block 610 [HEADING]]
### ཇི་ལྟར་ན་དང་ཅིའི་ཕྱིར་ན། ^2-5-0

[Block 611 [HEADING]]
#### གཞན་གྱི་དབང། ^2-5-1-0

[Block 612]
གལ་ཏེ་རྣམ་པར་རིག་པ་ཙམ་དོན་སྣང་བའི་གནས་ཞེས་བྱ་བ་ནི་དོན་མེད་བཞིན་དུ་ཡང་རྣམ་པར་རིག་པ་ཉིད་དོན་དུ་སྣང་བའི་རྒྱུ་ཡིན་ན་ཞེས་བྱ་བའི་དོན་ཏོ།[^450] །གལ་ཏེ་རྣམ་པར་རིག་པ་ཙམ་གཞན་གྱི་དབང་ཡིན་ན་དེ་ཇི་ལྟར་གཞན་གྱི་དབང་ཡིན་ཞེ་ན། རང་ཉིད་གཟུང་བར༌[^451]བྱ་བ་ཡིན་ཏེ། རྒྱུ་དེས་ན་གཞན་གྱི་དབང་ཡིན་ལ། གཞན་ཞེས་བརྗོད་ན་ནི་རང་གི་རྒྱུ་ལས་བྱུང་ཞིང་བྱུང་བ་ཉིད་ན་གནས་པར་མི་རུང་བ་དང་། རང་ཉིད་ཀྱིས་འཛིན་པས་གཞན་ཞེས་བྱ་བའི་གཞན་དབང་ཡིན་ནོ། །

[Block 613 [HEADING]]
#### ཀུན་ཏུ་བརྟགས་པ། ^2-5-2-0

[Block 614]
དེ་ལ་གནས་པ་ཞེས་བྱ་བ་ནི་བསྟན་པའི་གཞན་གྱི་དབང་རྣམ་པར་རིག་པ་ཙམ་ལ་བརྟེན་པའོ། །

[Block 615]
དོན་མེད་པ་ཞེས་བྱ་བ་ནི་ཡོད་པ་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 616]
སྣང་བ་ཞེས་བྱ་བ་ནི་དོན་དུ་དམིགས་པའོ། །

[Block 617]
དེ་ཇི་ལྟར་ན་ཞེས་བྱ་བ་དང་ཅིའི་ཕྱིར་ཞེས་བྱ་བ་དག་ནི་ཇི་ལྟར་བཤད་མ་ཐག་པ་ལྟ་བུའོ། །

[Block 618]
དཔག་ཏུ་མེད་པའི་རྣམ་པ་ཅན་གྱི་ཞེས་བྱ་བ་ནི་ཡུལ་ཐམས་ཅད་ལ་དམིགས་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའོ། །

[Block 619]
ཀུན་ཏུ་རྟོག་པ་ཞེས་བྱ་བ་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་ཀུན་ཏུ་བརྟགས་པའོ། །

[Block 620]
ཕྱིན་ཅི་ལོག་འབྱུང་བའི་རྒྱུ་མཚན་ཡིན་ཞེས་བྱ་བ་ནི་དམིགས་པའི་ངོ་བོ་ཉིད་ཀྱིས་དོན༌[^452]ཕྱིན་ཅི་ལོག་སྐྱེ་བའི་རྒྱུ་མཚན་དུ་གྱུར་པ་ཉིད་དོ། །

[Block 621]
རང་གི་མཚན་ཉིད་མེད་ཅེས་བྱ་བ་ནི་དེའི་ལུས་མེད་པའོ། །

[Block 622]
ཀུན་ཏུ་རྟོག་པ་ཙམ་དུ་དམིགས་པས་ཞེས་བྱ་བ་ནི་འཁྲུལ་པའི་རྣམ་པར་ཤེས་པ་ཙམ་ལ་དམིགས་པ་ཉིད་དོ། །

[Block 623 [HEADING]]
#### ཡོངས་སུ་གྲུབ་པ། ^2-5-3-0

[Block 624]
དེ་གཏན་མེད་པའི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་མེད་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 625]
དེ་ཇི་ལྟར་ན་ཞེས་བྱ་བ་དང་། ཅིའི་ཕྱིར་ན་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དབང་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 626]
གཞན་དུ་མི་འགྱུར་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སླུ་བ་མེད་པ་ཉིད་དོ།[^453] །སླུ་བ་མེད་པའི་འཁོར་བཞིན་ནོ། །

[Block 627]
རྣམ་པར་དག་པའི་དམིགས་པ་ཡིན་པ་དང་། དགེ་བའི་ཆོས་ཐམས་ཅད་ཀྱི་མཆོག་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་རྣམ་པར་དག་པའི་དམིགས་པའི་ངོ་བོ་ནི་ཡོངས་སུ་གྲུབ་པ་ཡིན་ཏེ། མཆོག་ཡིན་པའི་ཕྱིར་ཡོངས་སུ་རྫོགས་པའི་གནས་བཞིན་ནོ། །

[Block 628 [HEADING]]
### ཀུན་ཏུ་རྟོག་པས་ཇི་ལྟར་ཀུན་དུ་རྟོག། ^2-6-0

[Block 629]
ཀུན་ཏུ་རྟོག་པས་ཇི་ལྟར་ཀུན་དུ་རྟོག་ཅེས་བྱ་བ་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་ཀུན་ཏུ་རྟོག་པ་ཞེས་བྱ་བ་ལ། དེ་ལ༌[^454]ནི་གཞན་གྱི་དབང་ལ་ཀུན་ཏུ་རྟོག་པ་སྟེ། རྣམ་པ་གང་གིས་ཀུན་ཏུ་རྟོག་པ་དེ་སྟོན་པར་བྱེད་པ་དེ་ནི་མིང་གིས་དམིགས་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་ཡིན་ཏེ། གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ལ་དེར་མཚན་མར་འཛིན་པ་དང་ཞེས་བྱ་བ་ལ། གཞན་གྱི་དབང་ཉིད་ལ་མིག་ལ་སོགས་པའི་མིང་གི་མཚན་མར་འཛིན་པས་གང་གི་ཕྱིར་མཚན་མ་བཟུང་ནས་ཀུན་ཏུ་རྟོག་གོ། །

[Block 630]
ལྟ་བས་དེ་ལ་མངོན་པར་ཞེན་པ་དང་ཞེས་བྱ་བ་ནི་འདི་ནི་འདི༌[^455]ལྟ་བུའོ་ཞེས༌[^456]མཚན་མས་མཚན་མ་ཉིད་དུ་བཟུང་ནས་ཞེན་པའོ། །

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
--- END BLOCKS ---
