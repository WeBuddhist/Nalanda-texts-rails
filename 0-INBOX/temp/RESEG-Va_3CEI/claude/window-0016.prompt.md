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
མང་དུ་ནགས་གནས༌[^597]དེ་བཞིན་གཞན་དག་ཀྱང་། །ཞེས་པ་ནས། །དེ་དག་རྣམས་ཀྱང་བྱང་ཆུབ་ཕྱིར་དུ་འཇུག །ཅེས་པའི་བར་དུ་འདིས༌[^598]ནི་ཐུགས་རྗེས་འདྲེན་པར་བསྟན་ཏེ། ཐུགས་རྗེའི་འོད་ཀྱིས༌[^599]སེམས་ཅན་དམྱལ་བའི་གནས་རྣམས་ཞི་བར་བྱེད་པའོ། །

[Block 562 [HEADING]]
###### **མོས་པས་སྤྱོད་པ་སྣ་ཚོགས།** ^4-1-9-2-1-3-5-3-0

[Block 563]
རྒྱལ་བའི་སྲས་པོ་ལ་ལ་བརྩོན་འགྲུས་གནས།[^600] །ཞེས་པ་ནས། དེ་དག་བརྩོན་འགྲུས་བྱང་ཆུབ་མཆོག་ལ་ཞུགས། །ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་མོས་པས་སྤྱོད་པའི་ས་ན་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ཚོལ་བར་སྤྱོད་པ་བསྟན་པའི་ཕྱིར་འདི་མན་ཆད་ཚིགས༌[^601]བཅད་རྩ་བ་ཕྱེད༌[^602]དང་བཅུ་བཞིས་བསྟན་ཏོ། །

[Block 564 [HEADING]]
###### **བརྩོན་འགྲུས།** ^4-1-9-2-1-3-5-3-1-0

[Block 565]
དེ་ལ་དང་པོ་འདིས་ནི་བརྩོན་འགྲུས་བསྟན། །དེའི་འོག་མ་གཅིག་གིས་ནི་ཚུལ་ཁྲིམས་བསྟན། ཡང་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་བཟོད་པ་བསྟན། ཡང་གཉིས་ཀྱིས་ནི་བསམ་གཏན་བསྟན། ལྔས་ནི་སྦྱིན་པ་བསྟན། གསུམ་གྱིས་ནི་ཤེས་རབ་བསྟན་ཏེ། འདི་ནི་དང་པོ་བརྩོན་འགྲུས་རྩོམ་པ༌[^603]ཡང་སྡིག་པ་མི་དགེ་བའི་ཆོས་སྐྱེས་པ༌[^604]བསལ་བ༌[^605]དང་། དགེ་བའི་ཆོས་མ་སྐྱེས་པ་བསྐྱེད་པར༌[^606]བྱ་བ་ལ་སོགས་པའོ། །

[Block 566 [HEADING]]
###### **ཚུལ་ཁྲིམས།** ^4-1-9-2-1-3-5-3-2-0

[Block 567]
མདོ་ལས།

[Block 568]
ལ་ལ་སྲུང་བ་རྟག་ཏུ་རྣམ་དག་པ། །ཞེས་པ་ནས། དེ་ལས་སྤྱོད་པ་ཡོངས་སུ་རྫོགས་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་བསླབ་པ་ལ་གནས་ཤིང་སྒོ་གསུམ་ལ་སྤྱོད་པ་སྐྱོན་མེད་པར་གྱུར་པའོ། །

[Block 569]
ཇི་ལྟར་རིན་པོ་ཆེ་ཕྱི་ནང་གསལ་བ་འོད་ཡོད་པ་ཀུན་གྱི༌[^607]ཡིད་དུ་འོང་བ་བཞིན་ཚུལ་ཁྲིམས་མ་ཉམས་པ་སྐྱོན་མེད་པར་གྱུར་པའོ། །

[Block 570 [HEADING]]
###### **བཟོད་པ།** ^4-1-9-2-1-3-5-3-3-0

[Block 571]
རྒྱལ་སྲས་ལ་ལ་བཟོད་པའི་སྟོབས་ཅན་ཏེ། །ཞེས་པ་ནས། བཟོད་པ་དེ་དག་བྱང་ཆུབ་མཆོག་ལ་ཞུགས། །ཞེས་པའི་བར་དུ་ནི་རྡེག་པ་དང་སྤྱོ་བ་དང་སྨད་པ་ལ་སོགས་པས༌[^608]སྨ་དབབ་པ་སྣ་ཚོགས་ཉམས་སུ་ལེན་ཅིང་བཟོད་པའོ། །

[Block 572]
དེ་བཟོད་པ་ཡང་རྣམ་པ་ལྔའི་ཚུལ་གྱིས༌[^609]བཟོད་དེ། ཐོག་མ་མེད་པ་ནས་གཉེན་དུ་གྱུར་པའི་བསམ་པ་དང་། ཆོས་ལ་བསམ་པ་དང་། སྡུག་བསྔལ་ལ་བསམ་པ་དང་། མི་རྟག་པ་ལ་བསམ་པ་དང་། སྡུག་བསྔལ༌[^610]བའི་བསམ་པས་བཟོད་པའོ། །

[Block 573]
མདོ་ལས།

[Block 574 [HEADING]]
###### **བསམ་གཏན།** ^4-1-9-2-1-3-5-3-4-0

[Block 575]
བདག་མཐོང་བྱང་ཆུབ་སེམས་དཔའ་ལ་ལ་ནི། །ཞེས་པ་ནས། དེ་དག༌[^611]བསམ་གཏན་བྱང་ཆུབ་མཆོག་ལ་ཞུགས། །ཞེས་པའི་བར་གྱིས་ནི་བསམ་གཏན་ལ་གནས་པ་བསྟན་ཏེ། གཡེང་བའི་སྐྱོན་འདི་དག་བསྩལ༌[^612]ཏེ་གནས་སོ། །

[Block 576]
རྣམ་པར་རྟོག་པ་དང་རྩེད་མོའི་དགའ་བ་དང་། བྱིས་པ་མ་རབས་སྤང་བ་དང་། བཤེས་གཉེན་ངན་པ་དང་མི་འགྲོགས་ཤིང་སེམས་སྡུད་པའོ། །

[Block 577 [HEADING]]
###### **སྦྱིན་པ།** ^4-1-9-2-1-3-5-3-5-0

[Block 578]
ཡང་མདོ་ལས།

[Block 579]
ལ་ལས་དེ་བཞིན་སྦྱིན་པ་བྱིན་པ་ནི། །ཞེས་པ་ནས། སྦྱིན་པ་དེ་དག་བྱང་ཆུབ་མཆོག་ལ་ཞུགས། །ཞེས་པའི་བར་དུ་སྦྱིན་པ་རྣམ་པ་སྣ་ཚོགས་བསྟན་པའོ། །

[Block 580]
སྦྱིན་པ་དེ་དག་ཀྱང་རྒྱ་ཆེར་སྦྱིན་པ་དང་། མི་སྐྱོ་བར༌[^613]སྦྱིན་པ་དང་། དགའ་བར་སྦྱིན་པ་དང་། ཆགས་པ་མེད་པར་སྦྱིན་པ་དང་། དགེ་བའི་རྒྱུར༌[^614]འགྱུར་བའི་སྦྱིན་པའོ། །

[Block 581]
དེ་ལ་ཁ་ཟས་ཀྱི་སྦྱིན་པ་བྱས་ན་ནི་མུ་གེའི་བསྐལ་པར་མི་སྐྱེ། [^615]སྨན་བྱིན་པས༌[^616]ནི་བླ་ན་མེད་པའི་ཆོས་ཀྱི་སྨན་དང་ལྡན་པར་འགྱུར། [^617]གོས་བྱིན་པས༌[^618]ནི་རིན་པོ་ཆེ་སྣ་བདུན་དང་ལྡན་ཞིང་ཁྲེལ་དང་ངོ་ཚ་ཡོད་པར་འགྱུར། ཁྲི་སྟན་ལ་སོགས་པ༌[^619]བྱིན་པས་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་དང་ལྡན་པར་འགྱུར། ར་བ་དང༌[^620]སྐྱེད་མོས་ཚལ་བྱིན་པས་ནི་གཟུངས་ཀྱི་སྐྱེད་མོས་ཚལ་དང་ལྡན་པར་འགྱུར། མེ་ཏོག་བྱིན་པས་ནི་བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན་དང་ལྡན་པར་འགྱུར། འབྲས་བུ་བྱིན་པས་ནི་འཕགས་པའི་འབྲས་བུ་བཞི་དང་ལྡན་པར་འགྱུར། རྫིང་དང་ཁྲོན་པ་བྱིན་པས་ནི་རྣམ་པར་གྲོལ་བའི་ཆུ་དྲི་མ་མེད་པ་དང་ལྡན་པར་འགྱུར་ཞེས་གསུངས་སོ། །

[Block 582 [HEADING]]
###### **ཤེས་རབ།** ^4-1-9-2-1-3-5-3-6-0

[Block 583]
མདོ་ལས།

[Block 584]
དེ་དག་བྱང་ཆུབ་མཆོག་ཞུགས་ཡེ་ཤེས་ཀྱི། །ཞེས་བྱ་བ་ནས། དེ་དག་ཤེས་རབ་བྱང་ཆུབ་མཆོག་ལ་ཞུགས། །ཞེས་པའི་བར་དུ་ནི་ཤེས་རབ་ཀྱི་མཚན་ཉིད་བསྟན་ཏེ། མཚན་མ་མེད་པ་གཉིས་སུ་མེད་པ་ནམ་མཁའ་དང་མཚུངས་པའོ། །

[Block 585]
མཚན་མ་ཡོད་པ་དང་མཚན་མ་མེད་པ་ནི་གཞན་གྱི་དོན་དེ༌[^621]དང་བདག་གི་དོན་ལ༌[^622]སྤྱོད་པའི་ཡེ་ཤེས་སོ། །

[Block 586 [HEADING]]
###### **མྱ་ངན་ལས་འདས་པ་དང་མཆོད་རྟེན།** ^4-1-9-2-1-3-6-0

[Block 587]
མདོ་ལས།

[Block 588]
གང་གིས༌[^623]གཞན་ཡང་མཐོང་བ་འཇམ་པའི་དབྱངས། །ཞེས་པ་ནས། རྒྱལ་བའི་རིང་བསྲེལ་དག་ལ་རིམ་གྲོ་བྱེད། །ཅེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་དུམ་བུ་དྲུག་སྟེ། ཚིགས་བཅད་རྩ་བ་བདུན་གྱིས་མཆོད༌[^624]རྟེན་སློང་བ་བསྟན། དེ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། རིང་བསྲེལ་མཆོད་པ་དང་མཆོད་རྟེན་ལ་མཆོད་པའོ། །

[Block 589]
ཡང་བྱང་ཆུབ་སེམས་དཔའ་ལ་མཆོད་པ་དང་འཁོར་བརྒྱད་ལ་མཆོད་པའོ། །

[Block 590]
མདོ་ལས།

[Block 591]
མཆོད་རྟེན་བྱེ་བ་སྟོང་ཕྲག་མི་ཉུང་བ། །ཞེས་བྱ་བ་ནས། །དྲིལ་དང་དྲིལ་བུ་གཡེར་ཁ་རྟག་ཏུ་འཁྲོལ། །ཞེས་པའི་བར་འདིས་ནི་མཆོད་རྟེན་སློང་བ་བསྟན་ཏེ། བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་རིང་བསྲེལ་གྱི་མཆོད་རྟེན་ལ་མཆོད་པ་དང་རིམ་གྲོ་བྱས་ན་བསྐལ་པ་དུ་མར་ངན་སོང་དུ་མི་ལྷུང༌[^625]བྱང་ཆུབ་ཆེན་པོའི་ཚོགས་ཀྱང་རྫོགས་པར་འགྱུར་ཞེས་བསྟན་ཏོ། །

[Block 592]
དཔག་ཚད་ཅེས་པ་ནི་གཞུ་འདམ་ལྔ་བརྒྱ་ལ་རྒྱང་གྲགས་གཅིག །རྒྱང་གྲགས་བརྒྱད་ལ་དཔག་ཚད་གཅིག་གོ། །

[Block 593]
མདོ་ལས།

[Block 594]
མེ་ཏོག་དྲི་དང་དེ་བཞིན་སིལ་སྙན་གྱི། །ཞེས་པ་ནས། འདི་འདྲའི་མཆོད་རྟེན་རྒྱལ་བའི་རིང་བསྲེལ་ལ། །ཞེས་པའི་བར་དུ་ནི་འཁོར་བརྒྱད་ཀྱིས༌[^626]མཆོད་པ་བསྟན་ཏོ། །

[Block 595]
མདོ་ལས།

[Block 596]
གང་གིས༌[^627]ཕྱོགས་བཅུའི་དེ་དག་བརྒྱན་པ་ནི། །ཞེས་བྱ་བ་ནས། ལྷ་དང་བཅས་པའི་འཇིག་རྟེན་རྒྱས་པ་འདི།[^628] །ཞེས་པའི་བར་དུ་ནི་མཆོད་རྟེན་དེ་བྱས་པས་འཇིག་རྟེན་ཐམས་ཅད་ལ་མཛེས་པ་ནི་དཔེར་ན་ལྷའི་མེ་ཏོག་པ་རི་ཡ་ཏ་རྒྱས་པ་བཞིན་དུ་མཛེས་པ་བསྟན་ཏོ། །

[Block 597 [HEADING]]
###### དོན་འདྲི་བ། ^4-1-9-2-2-0

[Block 598]
མདོ་ལས།

[Block 599]
རྒྱལ་བས་འོད་ཟེར་གཅིག་པུ་འདི་བཏང༌[^629]བས། །ཞེས་པ་ནས། སྟོང་ཕྲག་མང་པོའི་ཞིང་རྣམས་སྟོན་པའོ། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་རྩ་བ་བརྒྱད་ཀྱིས་ནི་གསོལ་བའི་དོན་བསྟན་ཏེ། རྩ་བ་བཞིས་ནི་ལན་བཏབ་པའོ། །

[Block 600]
མདོ་ལས།
--- END BLOCKS ---
