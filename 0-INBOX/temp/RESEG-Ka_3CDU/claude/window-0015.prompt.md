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
ཆང་མ་འཐུངས་ན་ཡང་མི་འཚོ་བ་ཙམ་དུ་ཐུག༌[^406]ན་བསྐོལ་བ་ཆང་གི་རོ་དང་མྱོས་པའི་མཐུ་མེད་པར་བྱས་ཏེ། ཆང་དང་རོ་ཉམས་པ་དང་ཁ་དོག་དང་འདྲ་བ་ཙམ་བྱའོ། །

[Block 527 [HEADING]]
### གླུ་གར་རོལ་མོ། ^6-2-0

[Block 528]
གླུ་གར་རོལ་མོའི་གླེང་གཞི་ནི་བཅོམ་ལྡན་འདས་རྒྱལ་པོའི་ཁབ་ན་བཞུགས་སོ། །

[Block 529]
རྒྱལ་པོ་གཟུགས་ཅན་སྙིང་པོས་ཀླུའི་རྒྱལ་པོ་རི་བོ་དང་ཡིད་འོང་གི་ཕྱིར་གཙུག་ལག་ཁང་བརྩིགས་ནས་དུས་སྟོན་ཆེན་པོ་བྱས་པའི་ཚེ། ལྷོ་ཕྱོགས་ནས་གར་མཁན་འོངས་ཏེ་དྲུག་སྡེ་ཅི་བྱེད་པའི་ལད་མོ་བཟླས་པ་དང་། དྲུག་སྡེ་ཁྲོས་ནས་དུས་གཞན་ཞིག་ན་དུས་སྟོན་བྱེད་པའི་གར་མཁན་ལ་གནོད་པའི་ཕྱིར་དྲུག་སྡེས་བྲོ་གར་བྱས་པ་དང་། སྐྱེ་བོ་ཀུན་གར་མཁན་ལ་མི་ལྟ་བར་དྲུག་སྡེས་བྲོ་གར་བྱེད་པ་ལ་བལྟས་ནས་རོལ་མོ་མཁན་གྱིས་རྙེད་པ་མ་གྲུབ་སྟེ། འཚོ་བ་ཆད་ནས་རོལ་མོ་མཁན་ཁ་ཟེར་བ་ལ་བཅས། ཡུལ་ནི་རྒྱལ་པོའི་ཁབ། གང་ཟག་ནི་དྲུག་སྡེ།[^407] ཉོན་མོངས་པ་ནི་ཞེ་སྡང་། ཉེས་པ་ནི་གླུ་གར་རོལ་མོའི་སྒྲ་བྱེད་པའོ། །

[Block 530 [VERSE]]
གླུ་གར་དེ་བཞིན་སིལ་སྙན་རྣམས། །
སྡོམ་ལ་གནས་པས་མི་བྱའོ། །

[Block 531]
ཞེས་བྱ་བས་དྲེགས་པའི་ཉེས་པ་སྤང་བ༌[^408]སྟོན་ཏེ། དེ་ལ་གླུ་ནི་ཤར་དང་གན༌[^409]ད་ར་ལ་སོགས་པའོ། །

[Block 532]
གར་ནི་རྐང་ལག་གཡོབ་ཅིང་ལུས་སྒྱུར་བར་བྱེད་པའོ། །

[Block 533]
དེ་གཉིས་སྡོམ་པ་ལ་གནས་པས་བྱས་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 534]
གཞན་བྱེད་དུ་མི་གཞུག་སྟེ་བྱེད་དུ་བཅུག་ན་ཉེས་བྱས་སོ། །

[Block 535]
སིལ་སྙན་ནི་མཆོད་པའི་ཡོ་བྱད་དང་རོལ་མོའི་ཆ་བྱད༌[^410]དོ། །

[Block 536]
དེ་གསིལ༌[^411]ཞིང་དཀྲོལ་བ་རྣམ་པ་སྣ་ཚོགས་ཏེ། དེ་དག་སྡོམ་པ་ལ་གནས་པས་མི་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་དག་ནི་རྒྱ་གས་ཤིང་དྲེགས་པར་འགྱུར་བའམ། ཡན་ལག་འཁོར་བར་བྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 537]
མཆོད་པ་བྱ་བའི་ཕྱིར་གླུ་གར་བྱེད་དུ་བཅུག་ན་ཡང་གླུ་གར་བྱེད་དུ་མི་གཞུག །ལྷ་དང་ལྷ་མ་ཡིན་གྱི་དབང་པོས་མཆོད་པ་ལྟར་སངས་རྒྱས་ཀྱི་ཞབས་ཀྱི༌[^412]རྡུལ་ལ་མཆོད་པ་གྱིས་ཤིག་ཅེས་བྱས་ལ་བྱེད་དུ་གཞུག་གོ། །

[Block 538]
ཡང་ན་གནང་བ་ནི་སེམས་ཅན་གཞན་རྣམས་དད་པ་བསྐྱེད་པའི་ཕྱིར། དཀོན་མཆོག་གསུམ་གྱི་ཆེ་བའི་ཡོན་ཏན་བསྟོད་ར་རྣམས་དབྱངས་དང་གླུ་བསྲེས་ཏེ་བྱས་ན་ཉེས་པ་མེད་དོ། །

[Block 539]
གླུ་དབྱངས་དག་མི་ཤེས་ཏེ་སློབ་འདོད་ན་ཡང་ཤེས་པ་ཁྲིད་དེ་གནས༌[^413]དབེན་པར་སློབ་ཏུ་གཞུག་གོ། །

[Block 540]
འདིར་གླུ་གར་ལ་སོགས་པ་དངོས་སུ་མ་བྱས་ཀྱང་ཆུ་ལ་སོགས་པ་ལ་བརྡ་ཐབས་དང་ལག་ཐབས་སུ་བྱེད༌[^414]ན་ཡང་ཉེས་བྱས་སོ། །

[Block 541 [HEADING]]
### ཕྲེང་བ་དང་སྤོས་དང་བྱུག་པ་དང་རྒྱན་འདོགས་པ། ^6-3-0

[Block 542]
ཕྲེང་བ་དང་སྤོས་དང༌[^415]བྱུག་པ་དང་། རྒྱན་འདོགས་པའི་གླེང་གཞི་ནི་བཅོམ་ལྡན་འདས་རྒྱལ་པོའི་ཁབ་འོད་མའི་ཚལ་བྱ་ཀ་ལན་ད༌[^416]ཀ་གནས་པ་ན་བཞུགས་སོ། །

[Block 543]
དེའི་ཚེ་གཙུག་ལག་ཁང་གི་དུས༌[^417]སྟོན་བྱེད་པ་ན་དྲུག་སྡེ་ཁ་དོག་གིས་བརྒྱན་ནས་གར་བྱས་པ་ལ་བཅས་སོ། །

[Block 544]
ཡུལ་ནི་རྒྱལ་པོའི་ཁབ། གང་ཟག་ནི་དྲུག་སྡེ།[^418] ཉོན་མོངས་པ་ནི་ཞེ་སྡང་། ཉེས་པ་ནི་རྒྱན་ཕྲེང་དང་ཁ་དོག་འཆང་བའོ། །

[Block 545]
ལུས་ལ་སྤོས་ཀྱིས་མི་བྱུག༌[^419]སྟེ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཤློ་ཀ༌[^420]ཕྱེད་དང་གསུམ་གྱིས་ཁ་དོག་གི༌[^421]ཉེས་པ་སྟོན་ཏོ། །

[Block 546]
དེ་ལ་ལུས་ལ་སྤོས་ཀྱིས་བྱུག་པ་ནི་ལུས་ཀྱི་མདོག་མཛེས་པ་དང་དྲི་ཞིམ་པར་བྱ་བའི་ཆེད་དུ་ཨ་ཀ་རུ་དང་འབུ་སུག་ལ་སོགས་པ་དྲི་ཞིམ་པོའི་རྣམ་པ་ལྡེ་གུ་དང་ཕྱེ་མར་བྱས་ཏེ་ལུས་ལ་བསྐུ་ཞིང་གདགས་པར་མི་བྱའོ། །

[Block 547]
དེ་བཞིན་དུ་ཙནྡན་ལ་སོགས་པ་མི་བསྐུའོ། །

[Block 548]
ཡུང༌[^422]དང་གུར་གུམ་ལ་སོགས་པས། ཁ་དོག་རྣམས་སུ་མི་བྲིའོ་སྟེ། མིང་གིས་སྨོས་པ་འདི་རྣམས་ཀྱིས་ཀྱང་ལུས་ཀྱི་མཛེས་ཤིང་སྤ་བ་དང་དྲི་ཞིམ་པར་བྱ་བའི་ཆེད་དུ་ལུས་ལ་གདགས་ཤིང་བསྐུ་བ་དཔྲལ་བ་ལ་རེས་སུ་མི་བྱའོ། །

[Block 549]
སྩོགས་པའི་སྒྲས་ནི་མཚལ་དང་ལི་ཁྲི་དང་། ཁ་དོག་མཛེས་པར་འགྱུར་བའི་རྒྱུ་གཞན་དག་ཀྱང་བསྡུའོ། །

[Block 550 [VERSE]]
མེ་ཏོག་མགོ་རྒྱན་ཕྲེང་བ་དག །
[^423]བརྟུལ་ཞུགས་ཅན་གྱིས་གདགས་མི་བྱ། །

[Block 551]
ཞེས་བྱ་བ་ནི་མེ་ཏོག་བརྒྱུས་པའི་ཆུན་པོས་མགོ་དང་མགུལ་དུ་མི་གདགས་ཤིང་སྤང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 552 [VERSE]]
གསེར་ལ་སོགས་པའི་རྒྱན་རྣམས་ཀྱིས། །
བདག་ལ་བརྒྱན་པར་མི་བྱའོ། །

[Block 553]
ཞེས་བྱ་བ་ལ། དགེ་སྦྱོང་བདག་ཉིད་གསེར་དང་དངུལ་དང་མུ་ཏིག་ལ་སོགས་པ་ནོར་བུ་རིན་པོ་ཆེའི་རྒྱན༌[^424]རྣམས་ཀྱིས་བདག་གི་མགུལ་དང་རྐང་ལག་ལ་སོགས་པ་བརྒྱན་ཅིང་གདགས་པར་མི་བྱའོ། །

[Block 554 [VERSE]]
དུད་པ་ལ་སོགས་མིག་སྨན་རྣམས། །
མིག་མི་ན་བར་མི་བྱུག་གོ། །

[Block 555]
ཞེས་བྱ་བ་ནི་དགེ་སློང༌[^425]བདག་ཉིད་མིག་མི་ན་བར་མཚལ་དང་གུར་གུམ་དང་ག་བུར་དང་དུད་པ་སྦྱར་བ་ལ་སོགས་པས་མིག་ལ་བསྐུ་བར་མི་བྱའོ། །

[Block 556]
ལུས་ཀྱི་མདོག་མཛེས་པ་དང་ཆགས་པ༌[^426]སྐྱེ་བར་བྱ་བའི་ཕྱིར་མེ་ལོང་དང་ཆུ་དང་བ་ལ་བལྟ་བར་མི་བྱ། སེན་མོ་མི་བཅོས། ཆགས་པའི་བསམ་པས་སོ་རྩི་ལ་སོགས་པ་བཟའ་ཞིང་མཆུ་དམར་པོར་མི་བྱའོ། །

[Block 557]
གཡན་པ་དང་འབྲུམ་བུའི༌[^427]ནད་མེད་པར་ལུས་འཇམ་པ་དང་། [^428]མཛེས་པར་བྱ་བའི་ཕྱིར་རྡོ་དང་སོ་ཕག་གིས་མི་བྲུད།[^429] ཁྲུས་ཆུ་ལ་སོགས་པའི་ནང་དུ་དྲི་ཞིམ་པོ་སྣ་ཚོགས་སྦྱར་ལ་མི་བླུགས། ཡོན་བདག་དད་པ་ཅན་འགའ་ཞིག་དྲི་འབུལ་ཏེ་ལུས་ལ་མི་བསྐུར་མི་རུང་ན་ཡང་ཡིད་བསྲུང་བའི་ཕྱིར་སྐད་ཅིག་ཙམ་བསྐུས་ལ་ཡོན་བདག་སོང་མ་ཁད་དུ་མ་ཚོར་བར་དབྱིའོ། །

[Block 558]
རིམས་ནད་དང་གཡན་པའི་ནད་ལ་ཕན་པའི་ཕྱིར་ཙནྡན་དང་གུར་ཀུམ༌[^430]གྱིས་ལུས་ལ་བསྐུ་དགོས་ན་འཇིག་རྟེན་པས་མི་འཕྱ་བར་བསྐུའོ། །

[Block 559 [HEADING]]
### མཐོན་པོ་ན་འདུག་པའི་ཉེས་པ། ^6-4-0

[Block 560]
ཤིང་ཁྲི་ཁྲུ༌[^431]གང་མཐོ་བ་དང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཤློ་ཀ་གཅིག་གིས་མཐོན་པོ་ན་འདུག་པའི་ཉེས་པ༌[^432]བསྟན་ཏེ། ཤིང་ཁྲི་ཁྲུ༌[^433]གང་ལས་མཐོ་བ་ཞེས་བྱ་བ་སྟེ་དེ་ལ་ཉལ་བར་མི་བྱའོ། །

[Block 561 [VERSE]]
བ་སོ་ལ་སོགས་བརྒྱན་པའི་ཁྲི། །
དམའ་ཡང་ཉལ་ཁྲི་བཟང་པོ་ལ། །
ཉལ་ལ་སོགས་པ་མི་བྱའོ། །

[Block 562]
ཞེས་བྱ་བ་ནི་ཁྲུ་གང་སྙེད་དུ་མི་མཐོ་ཟིན་ཀྱང་བ་སོ་དང་དུང་དང་རྭ༌[^434]ལས་བྱས་པའི་ཁྲིའམ། དེ་དག་གིས་བརྒྱན་པའི་ཁྲི་བཟང་པོ༌[^435]དམའ་ཡང་ཉལ་བར་མི་བྱའོ། །ཅིའི་ཕྱིར་ཞེ༌[^436]ན། མལ་སྟན་མཐོན་པོ་དང་བཟང་པོ་དང་ཆེན་པོ་ལ་ཉལ་ན་མལ་གྱི་བདེ་བ་ལ་ཆགས་ཤིང་རློམ་སེམས་འབྱུང་བའི་ཕྱིར་དང་། གཞན་དུ་ན་བཀྲ་མི་ཤིས་པར་ཡང་འཆད་པས་ཉལ་བར་མི་བྱའོ། །

[Block 563]
གནང་བ་ནི་དེ་བཞིན་གཤེགས་པའི་གསུང་རབ་ཁ་དོན༌[^437]དུ་འདོན་ཅིང་འཆད་པའི་ཚེ་ནི་རིན་པོ་ཆེ་སྣ་ཚོགས་ཀྱིས་བརྒྱན་པའི་ཁྲི་ལ་འདུག་ཏུ་གནང་ངོ་། །དེ་ལ༌[^438]འདུག་པའི་ཚེ་ཡང་ཆགས་ཤིང་བདེ་བའི་བསམ་པས་ནི་འདུག་པར་མི་བྱའོ། །

[Block 564]
འདུ་བྱེད་ཐམས་ཅད་སྐད་ཅིག་མི་རྟག་པའི་རང་བཞིན་ཡིན་པར་བསམས་ཏེ་འདུག་པར་བྱའོ། །

[Block 565]
གདིང་བ༌[^439]ཀོ་ལྤགས་འཆང་བ་གནང་བ་ནི་ཡུལ་མཐའ་འཁོབ་དང་ལྷགས་པ་ཆེ་བ་དག་ཏུ་ནི་མལ་གོས་དང་སྟན་གཉིས་ཀ་ཀོ་ལྤགས་ལས་བྱེད་དུ་གནང་གི་ཡུལ་དབུས་མ་ག་དྷཱའི་ཕྱོགས་སུ་ནི་མི་གནང་ངོ་། །
--- END BLOCKS ---
