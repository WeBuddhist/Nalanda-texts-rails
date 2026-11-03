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

[Block 566]
ཀོ་ལྤགས་བཅང་དུ་གནང་བ་ཡང་གཞན་གྱི་གནང་གི་བ་གླང་དང་སྟག་དང་སེང་གེ་དང་དོམ་དང་དྲེད་དང་རྟ་དང་བྱི་ལའི་པགས་པ༌[^440]འདི་བདུན་བཀྲ་མི་ཤིས་ཤིང་། འཇིག་རྟེན་པ་རྣམས་ཀྱིས་སྨད་ཅིང་དཀོན་པ་ཡིན་པ་སྤྱོད་ཅིང་འདུག་ཏུ་མི་གནང་ངོ་། །ནད་ཀྱི་གཞི་ལ་ཕན་ན་ནི་སྨན་པས་བསྒོ་བ་ལ་ཉེས་པ་མེད་དོ། །

[Block 567 [VERSE]]
གླུ་གར་ལ་སོགས་བསྟེན་པ་དང་། །
གང་ལ་དྲེགས་པ་སྐྱེ་མི་འགྱུར། །
དྲེགས་པའི་ཡན་ལག་སྤངས་ནས༌[^441]ནི། །
བརྟུལ་ཞུགས་གནས་ཞེས་བརྗོད་པ་ཡིན། །

[Block 568]
ཞེས་བྱ་བ་ནི་དྲེགས་པའི་ཉེས་པ་སྤངས་པའི་ཕན་ཡོན་ཡིན་ཏེ། འདི་ལྟར་གླུ་དང་གར་ལ་སོགས་པ་དངོས་པོ་གང་བསྟེན་ཅིང་གནས་ན་དྲེགས་པ༌[^442]དང་རྒྱགས་པ་སྐྱེ་བར་འགྱུར་བའི་དྲེགས་པའི་ཡན་ལག་གམ་དངོས་པོ་དེ་ཡང་སྤངས་ན་བརྟུལ་ཞུགས་གནས་པ་སྟེ། སྡོམ་པ་ལ་གནས་པ་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 569 [HEADING]]
### དུས་མ་ཡིན་པས་ཟས་ཟ་བའི་ཉེས་པ། ^6-5-0

[Block 570]
ཉི་མ་ཕྱེད་མཚམས་ཕན་ཆད་ནས། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཤློ་ཀ༌[^443]གསུམ་གྱིས་ནི་དུས་མ་ཡིན་པས༌[^444]ཟས་ཟ་བའི་ཉེས་པ་བསྟན་ཏོ།[^445] །དེ་ལ་དགེ་སྦྱོང་གིས་ཟས་ཟ་བའི༌[^446]དུས་མ་ཡིན་པ་ནི་རང་གི་གནས་འཛམ་བུའི་གླིང་དུ་ཉི་མ་ཕྱེད་མཚམས་ཚུན་ཆད་ནས་བཟུང་སྟེ་སྐྱ་རེངས་མ་ཤར་བར་དུ༌[^447]ཟ་བའི་དུས་མ་ཡིན་པར༌[^448]སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་ཏེ།[^449] དགེ་སྦྱོང་སྡོམ་པ་ལ་གནས་པས་དུས་དེར་ཟས་མི་བཟའ་བར་བྱ་སྟེ། དེ་བས་ན། ཉི་མ་ཕྱེད་མཚམས་ཕན་ཆད་ནས།[^450] །

[Block 571 [VERSE]]
སྐྱ་རེངས༌[^451]མ་ཤར་དུས་མིན་ཏེ། །
དེ་ནི་རྒྱལ་བས་དུས་མིན་གསུངས། །
སྡོམ་ཅན་རྣམས་ཀྱིས་དེར་མི་བཟའ། །

[Block 572]
ཞེས་བྱ་བ་བསྟན་པ་ཡིན་ནོ། །

[Block 573]
འོ་ན་དགེ་སྦྱོང་གི་ཟས་བཟའ་བའི་དུས་གང་ཞེ་ན།

[Block 574 [VERSE]]
སྐྱ་རེངས༌[^452]ཤར་ནས་ཕྱེད་ཀྱི་བར། །
དེ་ཡི་སྐབས་སུ་ཟོས་ན་ནི། །
དེ་ནི་བདག་ཤེས་སྡོམ་པ་སྟེ། །
བཟའ་བ་དུས་སུ་ཟོས་པ་ཡིན། །

[Block 575]
ཞེས་བྱ་བས་བསྟན་ཏེ། འདི་ལྟར་རང་གི་གནས་ནི་འཛམ་བུའི་གླིང་དུ་སྐྱ་རེངས་ཤར་བ་ཉི་མ་ཕྱེད་མ་ཡོལ་གྱི་བར་སྐབས་དེར་བཟའ་བ་ཟོས་པ་ནི་བདག་ཤེས་བཞིན་དང་ལྡན་པ་སྡོམ་པ་ལ་གནས་པ་སྟེ་དགེ་སྦྱོང་གིས༌[^453]གནས་བཟའ་བའི་དུས་སུ་ཟོས་པ་ཡིན་ཏེ་དེ་ནི་དུས་ཡིན་ནོ། །

[Block 576 [VERSE]]
དུས་མིན་དུས་སུ་འདུ་ཤེས་ནས། །
ནམ་ཡང་བཟའ་བར་མི་བྱའོ། །

[Block 577]
ཞེས་བྱ་བ་ནི་ཕྱེད་མཚམས་ཕན་ཆད་དུས་མ་ཡིན་པ་ལས་དུས་ཡིན་ནོ་སྙམ་པའི་འདུ་ཤེས་བཞག་ནས་བཟའ་བ་རྣམས་བཟའ་བར་བྱ་བ་ནི་ནམ་ཡང་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 578]
དུས་མ་ཡིན་པར་བཟར་གནང་བ་ནི།

[Block 579 [VERSE]]
སྨན་པས་ཉོན་མོངས་བསྒོ་ན་ནི། །
ནད་པས་ཉེས་པར་མི་འགྱུར་རོ། །

[Block 580]
ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། སྔ་དྲོ་ཟོས་པས་འཚོ་བར་མི་ནུས་ན་ཕྱི་དྲོ་ཡང་ཟོ་ཅིག་ཅེས་སྨན་པས་བསྒོ་ན་ཉེས་པར་མི་འགྱུར་བ་དང་། ལམ་དུ་ཞུགས་ཏེ་དཔག་ཚད་གཅིག་ཙམ་དུ་འགྲོ་བ་དང་། མུ་གེ་ཆེན་པོ་བྱུང་སྟེ་ཉམ༌[^454]ཐག་པའི་དུས་སུ་ནི་དུས་དང་སྦྱར་བའི་གཏོལ་མེད་པས་ནམ་ཟས་རྙེད་པའི་ཚེ་དུས་མ་ཡིན་པར་བཟར་གནང་ངོ་། །

[Block 581]
དགེ་སློང་བ་ལང་བདག་བཞིན་དུ་ལས་ཀྱི་རྣམ་པར་སྨིན་པས་མིད་པ་གཉིས་ཡོད་པར་གྱུར་ན་སྔ་དྲོ་ནི་མིད་པ་གཅིག་ནས་ནང་དུ་རྒྱུ། ཕྱི་དྲོ་ནི་གཅིག་ནས་ཕྱིར་རྒྱུ་ཞིང་ཟ་བའི་དུས་ཡིན་པས་དེ་ལྟ་བུ་ནི་དང་པོ་ཁམ་གཅིག་གཉིས་ཙམ་གྱིས་ཕྱིར་བོར་ཏེ་སླར་ཁ་བཀྲུ་བར་བྱ། དེའི་ཕྱི་མ་ཕན་ཆད་བཟའ་བར་བྱའོ། །

[Block 582]
དེ་ལྟ་བུ་མ་གཏོགས་པ་རྣམས་ནི་སྒྲེགས་པའི་ཁྲོད་ན་ཁ་ཟས་ཀྱི་ཚལ་མ་ཞིག་བྱུང་ན་ཁ་ཟས་དང་བཅས་པར་མི་བྱའི་བརྟགས་པའི་ཆུས་ཁ་དག་པར་བཀྲུ་བར་བྱའོ། །

[Block 583 [HEADING]]
### དབྱིག་འཆང་བའི་ཉེས་པ། ^6-6-0

[Block 584]
ས་ལེ་སྦྲམ་ནི་གསེར་ཡིན་ཏེ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཤློ་ཀ་གསུམ་གྱིས་དབྱིག་འཆང་བའི་ཉེས་པ་སྤང་བ་སྟོན་ཏེ། དགེ་སྦྱོང་གིས་བདག་གི་ཆེད་དུ་གསེར་ས་ལེ་སྦྲམ་དང་། བདོག་པ༌[^455]ལ་སོགས་པ་དང་། དངུལ་ལ་སོགས་པ་སྟེ་རིན་པོ་ཆེ་རྣམས་སྦྱིན་བདག་རྣམས་ཀྱིས་དེ་བྱིན་ན།

[Block 585 [VERSE]]
བདག་ཉིད་ཀྱིས་ཀྱང་མི་བླང་ལ། །
གཞན་ཡང་ལེན་དུ་མི་གཞུག་གོ། །

[Block 586]
གལ་ཏེ་དེ་ལྟར་མ་བྱས་པར་བླངས་ན་ཉེས་བྱས་ཏེ་ལྕི་བར་འགྱུར་རོ། །

[Block 587]
དགེ་སྦྱོང་གིས༌[^456]ཁབ་རལ་དང་གྲི་ཤུབས་ལ་སོགས་པ་རྭ་དང་བ་སོ་དང་རུས་པ་ལས༌[^457]བྱས་པ་དང་། གསེར་དངུལ་ལ་སོགས་པ་ལས་བྱས་པའམ། གསེར་དངུལ་དང་རིན་པོ་ཆེས་སྦྲས་པ༌[^458]ལ་སོགས་པ་གདགས་ཤིང་བཅང་བར་མི་བྱ་སྟེ་བྱས་ན༌[^459]ཉེས་བྱས་སོ། །

[Block 588]
ཚོན་མོ་སྟེང་དང་ཞ་ཉེ་དང་ཁར་བ༌[^460]ལ་སོགས་པ་ལ་རེག་ན་ཉེས་བྱས་སོ། །

[Block 589]
འོ་ན་དགེ་སྦྱོང་གསེར་དངུལ་ལ་སོགས་པ་ལ་ཅི་ནས་ཀྱང་རེག་ཏུ་མི་རུང་ངམ་ཞེ་ན།

[Block 590 [VERSE]]
བདག་གིས་རུང་བ་མ་ཡིན་འདིས། །
རུང་བའི་དངོས་པོ་བཙལ་སྙམ་དུ། །
དེ་ལྟར་མངོན་པར་བསམས་ནས་ནི། །
དེ་ནས་གཞན་ཞིག་ལེན་དུ་གཞུག །

[Block 591]
ཅེས་སྨོས་ཏེ། དགེ་སྦྱོང་གིས་བསམས་པ་འདི་གཞན་ཏེ། བདག་གིས་གསེར་དངུལ་ལ་སོགས་པ་རུང་བའི་དངོས་པོ་མ་ཡིན་པ་འདིས། རུང་བའི་དངོས་པོ་ཆོས་གོས་གསུམ་བཙལ་བའི་ཟོང་དང་། གསེར་དངུལ་ཅུང་ཟད་མ་བཅངས་ན་འཚོ་བ་འཆད་པར་འགྱུར་བས་འཚོ་བའི་ཕྱིར་དང་། སྨན་མེད༌[^461]ནད་ཀྱིས་གཙེས་པར་འགྱུར་བས་སྨན་བཙལ་བའི་ཟོང་གི་ཕྱིར་བཅང་ཞིང་བླང་ངོ་སྙམ་དུ་བསམས་ཏེ་དགེ་བསྙེན་ནམ་ཁྱིམ་བདག་གཞན་ལེན་དུ་གཞུག་གོ། །

[Block 592]
ཡང་ཉེས་པར་མི་འགྱུར་བ་ནི།

[Block 593 [VERSE]]
དཀོན་མཆོག་གསུམ་གྱི་ཆེད་ཀ་དང་། །
ཚངས་པ་མཚུངས་པར་སྤྱོད་རྣམས་ཀྱི། །
གསེར་དང་དངུལ་ལ་རེག་གྱུར་ཀྱང་། །
ཉེས་པར་གྱུར་པ་མ་ཡིན་ནོ། །

[Block 594]
ཞེས་པ་སྟེ། འདི་ལྟར་དཀོན་མཆོག་གསུམ་གྱི་ཆེད་དུ་སྟེ་དེའི་དཀོར་དུ་གཏོགས་པ་དང་། ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་མཁན་པོ་དང་སློབ་དཔོན་གཅིག་པའི་དགེ་སྦྱོང་གི་ཡོ་བྱད་ལྟ་བུ་དང་། མཁན་པོ་དང་སློབ་དཔོན་གྱི་ཡོ་བྱད་དུ་གཏོགས་པའི་གསེར་དངུལ་ལ་དགེ་སྦྱོང་བདག་གིས་རེག་ཀྱང་ཉེས་པར་མི་འགྱུར་རོ། །

[Block 595]
ཡང་།

[Block 596 [VERSE]]
བདག་གིས་རུང་བ་མ་ཡིན་འདིས། །
རུང་བའི་དངོས་པོ་བཙལ་སྙམ་དུ། །

[Block 597]
ཞེས་བྱ་བ་ནི་གསེར་དངུལ་འདིས་དེ་བཞིན་གཤེགས་པའི་སྐུ་གཟུགས་ལུགས་སུ་བླུགས་ཤིང་རིས་སུ་བྲིས་པ་དང་། དྷརྨ་བྲིས་ཤིང་གླེགས་བམ་དུ་བྱས་པ་དང་། དགེ་འདུན་སྤྱི་ལ་འབུལ་བའི་བསམས་པས༌[^462]བླངས་ན་ཉེས་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 598]
དགེ་སྦྱོང་གིས༌[^463]ཁེ་སྤོགས་འདོད་པའི་ཕྱིར་བདག་གི་ནོར་གཞན་ལ་འཚོང་དུ་བཅོལ་ཏམ། གཞན་གྱི་ནོར་བདག་གིས༌[^464]བླངས་ཏེ་ཚོང་བྱས་ན་ཉེས་བྱས་སོ། །

[Block 599]
དཀོན་མཆོག་གསུམ་གྱི་ཕྱིར་རམ། དེ་ལྟར་མ་བྱས་ན་སྨན༌[^465]ཟོང་ཙམ་ཡང་མེད་ལ་འཚོ་བ་ཡང་འཆད་པར་འགྱུར་བ་ཞིག་གམ། བསོད་ནམས་བྱ་བ་ཞིག་ཏུ་བསམས་ཏེ་ཚོང་གི་ཁེ་སྤོགས་བྱ་དགོས་ན་ཡང་བདག་ཉིད་ཀྱིས་མི་བྱའི། ཁྱིམ་པ་གཞན་ལ་བཅོལ་བར་བྱའོ། །

[Block 600]
དེ་ལྟར་བཅོལ་བའི་འོས་མེད་ན་ཡང་བདག་ཉིད་ཚོང་བྱེད་པའི་ཚེ་བདག་གིས༌[^466]ནན་དང་མཐུས་མི་བྱའོ། །
--- END BLOCKS ---
