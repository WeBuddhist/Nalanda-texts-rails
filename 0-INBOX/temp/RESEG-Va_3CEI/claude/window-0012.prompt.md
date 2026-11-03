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
[Block 421]
ཡང་མཚན་ཉིད་དྲུག་ཏུ་གཡོ་བ་སྟེ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་འགུལ། རབ་ཏུ་འགུལ་ཞེས་བྱ་བ་ནས་འཁྲུགས་རབ་ཏུ་འཁྲུགས་པའི་བར་དུ་སྟེ། འགུལ་ཞེས་པ་ནི་ཆུང་ངུ་འགུལ་བའོ། །

[Block 422]
རབ་ཏུ་འགུལ་བ་ནི་ཕྱོགས་ཐམས་ཅད་འགུལ་བ་སྟེ། འོག་མའི་རྣམས་ཀྱང་དེ་བཞིན་དུ་སྦྱོར༌[^484]རོ། །

[Block 423]
དེ་བསྒུལ་བ་ཅིར་དགོངས་ཤེ༌[^485]ན། དོན་རྣམ་པ་བདུན་གྱི་ཕྱིར་ཏེ། བདུད་དང་མུ་སྟེགས་ཅན་རྣམས་སྡང་བ་དང་། སེམས་གཡེང་བའི་འཁོར་རྣམས་སེམས་བསྡུ་བ་དང་། ཡང་དྲེགས་པ་ལ་གནས་པ་རྣམས་ཆོས་ལ་གཟུད༌[^486]པའི་ཕྱིར་གཞན༌[^487]གདབ་པ་དང་། ཆོས་ཀྱི་མཚན་ཉིད་ལ་སེམས་སུ་གཞུག་པ༌[^488]དང་། རྟོགས་པའི༌[^489]གནས་བསྟན་པ་དང་། སྨིན་པ༌[^490]རྣམས་གྲོལ་བ་ཐོབ་པར་བྱ་བ་དང་། ཡང་དག་པའི་དོན་འདྲི་བར་བསྐུལ་བའི་ཕྱིར་ས་གཡོ་བ་བསྟན་ཏོ། །

[Block 424 [HEADING]]
##### བཅུད་ཀྱི་འཇིག་རྟེན། ^4-1-7-3-0

[Block 425]
མདོ་ལས་ཡང་དེའི་ཚེ་འཁོར་དེར་གང༌[^491]དགེ་སློང༌[^492]དང་ཞེས་པ་ནས། བཅོམ་ལྡན་འདས་ལ་ལྟ་ཞིང་ངོ་མཚར་དུ་གྱུར་རྨད་དུ་གྱུར་དགའ་བར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི༌[^493]འདི་མན་ཆད་བཅུད་ཀྱི་འཇིག་རྟེན་བསྟན་ཏེ། དེ་ཡང་ཚོགས་བཞིར་བསྡུའོ། །

[Block 426]
འཁོར་བཞི་པ་དང་། འཁོར་བརྒྱད་པ་དང་། རྒྱལ་པོ་གཉིས་དང་མངོན་པར་དགའ་བ་རྣམས་སོ། །

[Block 427 [HEADING]]
#### བཤད་པའི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ། ^4-1-8-0

[Block 428 [HEADING]]
##### འོད་གཏོང་བ། ^4-1-8-1-0

[Block 429]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཀྱི་སྨིན་མཚམས་ཀྱི་བར་གྱི་མཛོད༌[^494]སྤུ་ནས་འོད་ཟེར་གཅིག་བྱུང་ཞེས་པ་ནི་དེ་མན་ཆད་བཤད་པའི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། འགྲེལ་པ་ལས་འགྲོ་བ་ཕལ་པོ་ཆེ་རྣམས་དེ་ལྟ་བུའི་ལྟས་ངོ་མཚར་དུ༌[^495]གྱུར་པ་མཐོང་ན་དེ་བཞིན་གཤེགས་པ་དེ་ཡང་བདག་ཅག་ལ་ཆོས་འཆད་དོ་སྙམ་པའི་སྤྲོ་བའི་སེམས་སྐྱེ་བའི་བཤད་པའི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་སྟེ། འོད་དེ་བཏང་བས་འཇིག་རྟེན་གྱི་ཁམས་ན་དོན་གྱི་རྣམ་པ་ཐམས་ཅད་སྣང་བར་མཛད་དོ། །

[Block 430]
ཡང་བཅོམ་ལྡན་འདས་ཆོས་སྟོན་པ་ནི་འགྲོ་བ་མང་པོ་ལ་ཕན་པའི་ཆེད་པས་ཉན་པ་རྣམས་སྤྲོ་ཞིང་ཐོས་པར་དཀའ་བའི་སེམས་སྐྱེ་བའི་ཕྱིར་བཤད་པའི་རྒྱུ་ཞེས་བྱ་བས་དེའི་ཕྱིར་འོད་ཀྱིས༌[^496]རྒྱང་རིང་པོ་ཚུན་ཆད་སྣང་བར་མཛད་དོ། །

[Block 431]
རྣམ་པ་གཉིས་སུ་རྣམ་པ་དྲུག་ཏུ་གཡོ་བར་བསྟན་ནས། དེའི་འོག་ཏུ་ཆོས་བསྟན་པར་མཛད་པ་ནི། ཆོས་ཟབ་མོ་རང་གི་རིག་པའི་དོན་ཡིན་པས་སྔར་ཆོ་འཕྲུལ་བསྟན་ཏེ་གཟོད༌[^497]ཆོས་འདི་སྟོན་པར་མཛད་པས་དེའི་ཕྱིར་ཆོས་བཤད་པའི་རྒྱུ་ཞེས་བྱའོ། །

[Block 432]
སྔར་ལྷའི་མེ་ཏོག་འབྲུལ་བ༌[^498]དང་ས་རྣམ་པར་གཡོ་བ་བསྟན་པ་ཡང་ངོ་མཚར་དུ་བྱ་བ་ཡིན་མོད་ཀྱི་འོད་ཀྱིས་སྣང་བར་མཛད་པ་འདི་ཉིད་ཆོས་ཟབ་མོ་རང་གི༌[^499]རིག་པ་བསྟན་པའི་ལྟས་བསམ་གྱིས་མི་ཁྱབ་པར་ཀུན་གྱིས་མཐོང་བས་བཤད་པའི་རྒྱུ་ཞེས་བྱའོ། །

[Block 433]
འོད་གཏོང་བ་དང་ཡུལ་སྣང༌[^500]བར་མཛད་པ་མཐོང་བར་བྱེད་པ་སྟེ། འདི་ནི་དང་པོ་སྨིན་མ་བཞིན་གྱི༌[^501]རྒྱན༌[^502]ཡིན་པ་བཞིན་ཐེག་པ་ཆེན་པོའི་གཞུང་དེ་ཡང་གཙོར་ཡིན་པར་བསྟན་པ་དང་། མཚམས་ཞེས་བསྟན་པས་དབུ་མའི་དོན་མཚོན་པ་དང་། དཀར་པོ་ཞེས་སྨོས་པས་ཁ་དོག་ཐམས་ཅད་ཀྱི་གཞི་ཡིན་ཏེ། དེ་བཞིན་དུ་མདོ་སྡེ་འདི་ཡང་ཐེག་པ་རྣམ་གསུམ་གྱི་གཞི་ཡིན་པར་བསྟན་པའོ། །

[Block 434]
མཛོད་སྤུ་དེ་ཡང་ཤིན་ཏུ་དཀར་པ་བརྐྱང་ན་རིང་པ། བསྐུམ་ན་ཐུང་བའོ། །

[Block 435]
འོད་དེ་ཡང་རྣམ་པ་བདུན་ཏེ། མི་ཆེན་པོའི་ཆ་ཡིན་པས་འགྲོ་བ་དད་པ་སྐྱེ་བར༌[^503]འགྱུར་བ་དང་། མུན་པ་སེལ་བས་མ་རིག་པའི་ས་འཇོམས་པ་དང་། སྣང་བ་དེས་མཚོན་པས་འཇིག་རྟེན་ནས་འདྲེན་པ་དང་ནང་གི༌[^504]བསྟན་པ་ཡེ་ཤེས་ཀྱི༌[^505]འོད་ཡིན་པར་མཚོན་པ་དང་། འོད་ཀྱིས༌[^506]རེག་པ་རྣམས་སྡུག་བསྔལ་ཞི་བར་བྱེད་པ་དང་། འོད་ཀྱིས་རེག་པ་རྣམས་ཆོས་ཉན་པར་བསྐུལ་བ་དང་། ཡུལ་ལ་ཆགས་པ་རྣམས་སྐྱོ་བ་བསྐྱེད་པའི་ཕྱིར་ཏེ་བདུན་ནོ། །

[Block 436]
གཅིག་ཏུ་རྫུ་འཕྲུལ་བཤད་པའི་སྐབས་སུ་བསྟན་ཏོ། །

[Block 437 [HEADING]]
##### ཡུལ་སྣང་བར་མཛད་པ། ^4-1-8-2-0

[Block 438]
མདོ་ལས་དེ་ཤར་ཕྱོགས་སུ་སངས་རྒྱས་ཀྱི་ཞིང་སྟོང་ཕྲག་བཅོ་བརྒྱད་ཅེས་པ༌[^507]ནས་འོད་ཀྱིས༌[^508]ཤིན་ཏུ་ཁྱབ་པར་སྣང་ངོ་ཞེས་པའི་བར་དུ་ནི་ཡུལ་སྣང་བར་མཛད་པ་བསྟན་པ་སྟེ། ཞིང་ནི་སྟོང་ཕྲག་བཅོ་བརྒྱད་པའོ། །

[Block 439]
ཤར་ཕྱོགས་ཞེས་སྨོས་པ་ནི་ཕྱོགས་ཀྱི་གཙོ་བོ་ཡིན་པ་བཞིན༌[^509]བསྟན་པ་འདི་ཐེག་པའི་གཙོ་བོ་ཡིན་པའོ། །

[Block 440]
དང་པོ་དེར་འཆར་བ་ཡང་དཔེར་ཉི་མ་རི་མཐོ་མཐོ་ལ་དང་པོར་འཆར་བ་བཞིན་མདོ་སྡེ་འདི་ཡང་དང་པོར་དབང་པོ་སྨིན་པ་རྣམས་ལ་སྣང་བར་མཛད་དོ། །

[Block 441]
སེམས་ཅན་དམྱལ་བ་སྣང་བར་མཛད་པ་ནི་སྡུག་བསྔལ་ཞི་བར་མཛད་པ། ལྷའི་ཁམས་སྣང་བར་མཛད་པ་ནི་ཐེག་པ་ཆེན་པོ་ཉན་པར་བསྐུལ་བ་སྟེ། ཐུགས་རྗེས་ཁྱབ་པར་མཛད་ཅེས་པའི་དོན་ཏོ། །

[Block 442]
སེམས་ཅན་དམྱལ་བ་བསྟིར་མེད་པ་ཞེས་པ་ནི་སྡུག་བསྔལ་མྱོང་བ་མནར༌[^510]བའི་སྐབས་མེད་པའི་ཕྱིར་རོ། །

[Block 443 [HEADING]]
##### སྣང་བར་བྱ་བའི་ཡུལ། ^4-1-8-3-0

[Block 444]
མདོ་ལས་སངས་རྒྱས་ཀྱི་ཞིང་དེ་དག་གི་འགྲོ་བ་དྲུག་ན་སེམས་ཅན་གང་ཡོད་པ་དེ་དག་ཐམས་ཅད་མ་ལུས་པར་སྣང་ངོ་ཞེས་པ་ནི་འདི་སྣང་བར་བྱ་བའི་ཡུལ་བསྟན་ཏེ། དེ་ཡང་རྣམ་པ་བདུན་ནོ། །

[Block 445]
འགྲོ་བ་དྲུག་དང་སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་དང་། བྱང་ཆུབ་སེམས་དཔའ་དང་མྱ་ངན་ལས་འདས་པ་རྣམས་དང་། མཆོད་རྟེན་རྣམས་སོ། །

[Block 446]
དེ་ཡང་དུམ་བུ་གསུམ་དུ་དབྱེ་སྟེ། འཁོར་བར་འཁོར་པའི་སེམས་ཅན་རྣམས་སྣང་བར་བྱས་པ་དང་། དཀོན་མཆོག་གསུམ་སྣང་བར་བྱས་པ་དང་། མྱ་ངན་ལས་འདས་པའི་སྤྱོད་པ་བསྟན་པའོ། །

[Block 447 [HEADING]]
###### འཁོར་བར་འཁོར་བའི་སེམས་ཅན་རྣམས་སྣང་བར་བྱས་པ། ^4-1-8-3-1-0

[Block 448]
འགྲོ་བ་དྲུག་ལ་ཡང་དྲུག་ཏུ་དབྱེ༌[^511]སྟེ། དེའི་མིང་བསྟན་པ་དང་། བསྐྱེད་པའི་རྒྱུ་དང་། དབྱེ་བ་དང་བསྡུ་བ་བསྟན་པ་དང་། གནས་བསྟན་པ་དང་། ཚེའི་ཚད༌[^512]བསྟན་པ་དང་། རྒྱུ་དང་འབྲས་བུའི་མཚན་ཉིད་བསྟན་པའོ། །

[Block 449]
མིང་བསྟན་པ་ནི་དྲུག་ཅེས་པ་ནི་གྲངས་སོ། །

[Block 450]
འགྲོ་བ་ཞེས་པ་ནི་ཉོན་མོངས་པ་དང་། ལས་ཀྱིས༌[^513]བསྐྱེད་པའི་ཕུང་པོ་ལྔ་ལ་གནས་པ་འགྲོ་བ་སྣ་ཚོགས་སུ་འགྲོ་ཞེས་པའི་དོན་ཏོ། །

[Block 451]
རང་གིས༌[^514]བྱས་པའི་ལས་ལ་སྤྱོད་པའི་ཕྱིར་ལྷའོ། །

[Block 452]
ཡང་ན་འདོད་པ༌[^515]དང་རྫུ་འཕྲུལ་དུ་ལྡན་པ་ནི་ལྷའོ། །

[Block 453]
སེམས་པ་མང་བ་ནི་མིའོ། །

[Block 454]
བཀྲེས་པའི་སྡུག་བསྔལ་གྱིས་མནར་བ་ནི་ཡི་དགས་སོ། །

[Block 455]
དུད་དེ་འགྲོ་བས་དུད་འགྲོའོ། །

[Block 456]
གཏུབ་པ༌[^516]དང་གཤེགས་པ་ལ་སོགས་པའི་གཞིར་གྱུར་པའི་ཕྱིར་དམྱལ་བའོ། །

[Block 457]
ལྷ་མ་ཡིན་ནི་སྔར་བསྟན་པ་ཡིན་ནོ། །

[Block 458]
སྐྱེད་པའི་རྒྱུ་ནི་འགྲོ་བ་དྲུག་པོ་ཀུན་ཀྱང་རྣམ་པར་སྨིན་པའི་རྣམ་པར་ཤེས་པས་བསྐྱེད་པའི༌[^517]རང་བཞིན་ཅན་མ་བསྒྲིབས་ལ་ལུང་དུ༌[^518]མ་བསྟན་པའོ། །

[Block 459]
བསྡུ་བ་དང་དབྱེ་བ་ལ།

[Block 460 [VERSE]]
འགྲོ་བ་དྲུག་ཅེས་པ་ནི་བསྡུ་བའོ། །
དེ་ཡང་དགེ་བ༌[^519]བསྐྱེད་པ་དང་།
མི་དགེ་བ༌[^520]བསྐྱེད་པ་ནི་དབྱེ་བའོ། །
--- END BLOCKS ---
