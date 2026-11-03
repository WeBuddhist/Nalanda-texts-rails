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
[Block 491]
དབང་པོ་རྣོ་རྟུལ༌[^544]གཉི་ག་ལ་ཕན་པ་དང་སྔ་ཕྱི་རྣམ་གཉིས་ཀྱི་འཁོར་བ༌[^545]ལ་ཕན་གདགས་པ་དང་། དྲང་པོ་དང་དེ་མ་ཡིན་པ་གཉིས་དགའ་བར་བྱ་བ་དང་། དཀའ་སླ་གཉི་གའི་ཆེད་དང་དོན་དམ་པ་དང་ཀུན་རྫོབ་གཉི་གའི་དོན་དང་། བླང་དོར་གཉི་གའི་ཆ་དང་། གསལ་མི་གསལ་དབྱེ་བ་དང་། ཤེས་པ་དང་སྤོབས་པ་དབྱེ་བ་དང་། ཐེ་ཚོམ་དང་འཆིང་བ་དབྱེ་བ་དང་། བཤད་པ་དང་སྤྱོད་པ་བསྟན་པའོ། །

[Block 492]
མདོ་ལས་འཇམ་དཔལ་ཞེས་པ་ནས་ཞལ་གྱི་མཛོད་སྤུ་ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ་འདི་དག་ལ་རྩ་བ་དྲུག་ཅུ་རྩ་གཉིས་ཡོད་དེ། དུམ་བུ་གཉིས་སུ་དབྱེའོ། །

[Block 493]
དང་པོ་རྩ་བ་ལྔ་བཅུ་རྩ་བཞིས་ནི་ལྟས་རྣམས་ཀྱི་དོན་བསྟན། རྩ་བ་བརྒྱད་ཀྱིས་ནི་དོན་འདྲི་བའོ། །

[Block 494 [HEADING]]
###### ལྟས་རྣམས་ཀྱི་དོན་བསྟན་པ། ^4-1-9-2-1-0

[Block 495 [HEADING]]
###### **འོད་ཀྱིས་སྣང་བར་མཛད་པའི་གླེང་གཞི།** ^4-1-9-2-1-1-0

[Block 496]
དང་པོ་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཚིགས༌[^546]བཅད་དང་པོ་གཅིག་གིས་ནི་འོད་ཀྱིས༌[^547]སྣང་བར་མཛད་པའི་གླེང་གཞི་སྟོན་ཏོ། །

[Block 497]
དེའི་འོག་མ་རྩ་བ་གསུམ་གྱིས་ནི་མེ་ཏོག་འབྲུལ་བ་དང་ས་གཡོ་བའི་སྤྱོད་ལམ་བསྟན་ཏོ། །

[Block 498]
དེའི་འོག་གི་རྩ་བ་ལྔ་བཅུས་ནི་ཡུལ་རྣམས་སྣང་བར་མཛད་པའི་གླེང་གཞི་བསྟན་ཏེ་འདི་ནི་དང་པོའོ། །

[Block 499 [HEADING]]
###### **མེ་ཏོག་འབྲུལ་བ་དང་ས་གཡོ་བ།** ^4-1-9-2-1-2-0

[Block 500]
མདོ་ལས།

[Block 501]
མེ་ཏོག་མན་དཱ་ར་བའི་ཆར་ཆེན༌[^548]ཀྱང་། ཞེས་པ་ནས་གང་གིས་དེ་ནི་ཀུན་དུ་མཛེས་པ་ཞེས་པའི་བར་དུ་དེ་ལ་རྩ་བ་གསུམ་གྱིས་ནི་སྤྱོད་ལམ་གསུམ་གྱི༌[^549]དོན་བསྟན། རྩ་བ་ཕྱེད༌[^550]དང་གཉིས་ཀྱིས་ནི་མེ་ཏོག་གི་ཆར་བབ་པ་བསྟན། རྩ་བ་ཕྱེད་ཀྱིས་ནི་ས་གཡོ་བ་བསྟན། རྩ་བ་གཅིག་གིས་ནི་འཁོར་བཞི་རབ་ཏུ་དགའ་བ་བསྟན། འདི་ནི་མེ་ཏོག་གི་ཆར་འབབ་པ་བསྟན་ཏོ། །

[Block 502]
མེ་ཏོག་དེ་དག་ཙན་དན་གྱི་དྲི་བསུང་དང་ལྡན་ཞིང༌[^551]ཡིད་དུ་འོང་བས་ཞིང་དེ་མཛེས་པར་བྱེད༌[^552]པའོ། །

[Block 503]
མདོ་ལས།

[Block 504 [VERSE]]
འཁོར་བཞི་དེ་དག༌[^553]ཤིན་ཏུ་དགའ་བ་འཐོབ། །
ཞིང་འདི་ཐམས་ཅད་ཀུན་ནས་རབ་ཏུ་གཡོས། །

[Block 505]
ཞེས་པ་ནི་ས་གཡོ་བས་འཁོར་འདི་རྣམས་དགའ་བ་བསྟན་ཏོ། །

[Block 506 [HEADING]]
###### **ཡུལ་རྣམས་སྣང་བར་མཛད་པ།** ^4-1-9-2-1-3-0

[Block 507]
མདོ་ལས།

[Block 508]
འོད་ཟེར་དེ་ཡིས་ཤར་གྱི༌[^554]ཕྱོགས་ལོགས་སུ། །ཞེས་པ་ནས། བསྟིར་མེད་ཡན་ཆད་སྲིད་པའི་ཐོག་མའི་བར། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པའི་རྩ་བ་བཅོ་ལྔས་ཡུལ་རྣམས་སྣང་བར་མཛད་པ་བསྟན་ཏེ། དེ་ལ་རྩ་བ་ཕྱེད་ཀྱིས་ནི་སྣང་བའི་ཡུལ༌[^555]བསྟན། གཞན་གྱིས་ནི་ལྟ༌[^556]བ་བསྟན་ཏེ། འདིས་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་སྣང་བར་བྱེད་པ༌[^557]བསྟན་ཏོ། །

[Block 509]
གསེར་གྱི་ཁ་དོག་དུ་སྣང་ཞེས་པ་ནི་ཐེག་པ་གཅིག་པོ་འདི་རིན་ཆེ་བར་བསྟན་པའོ། །

[Block 510 [HEADING]]
###### **འགྲོ་བ་དྲུག།** ^4-1-9-2-1-3-1-0

[Block 511]
མདོ་ལས།

[Block 512]
དེ་དག་ཞིང་གི་ཇི་སྙེད་སེམས་ཅན་དག །ཅེས་པ་ནས། འགྲོ་བ་བདེ་དང་མི་བདེ་རྣམས་ཀྱང་སྣང་།[^558] །ཞེས་པའི་བར་དུ་ནི་སྣང་བར་བྱ་བ་རྣམས་བསྟན་ཏེ། །དུམ་བུ་དྲུག་ཏུ་དབྱེའོ། །

[Block 513]
ཚིགས༌[^559]བཅད་རྩ་བ་ཕྱེད༌[^560]དང་གཉིས་ཀྱིས་ནི་འགྲོ་བ་དྲུག་པོ་རྣམས་བསྟན། རྩ་བ་ཕྱེད་ཀྱིས་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་བསྟན། དེའི་འོག་ཏུ་རྩ་བ་ཕྱེད༌[^561]དང་བདུན་གྱིས་ནི་ཆོས་ཐོས་པ་བསྟན། ཡང་ཕྱེད༌[^562]དང་གཉིས་ཀྱིས་ནི་འཁོར་བཞི་བསྟན། དེའི་འོག་ཏུ་རྩ་བ་སུམ་ཅུ་རྩ་གཅིག་གིས་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་བསྟན། རྩ་བ་བདུན་གྱིས་ནི་མྱ་ངན་ལས༌[^563]འདས་པ་དང་མཆོད་རྟེན་བསྟན་ཏེ། འདིས་ནི་དང་པོ་ལས་དགེ་བ༌[^564]དང་མི་དགེ་བས་བསྐྱེད་པའི་འགྲོ་བ་དྲུག་པོ་རྣམས་ལས་དང་ཉོན་མོངས་པས་བདེ་བ་དང་མི་བདེ་བ་རྣམ་པར་སྨིན་པ་མྱོང་བར་བྱེད་པ་རྣམས་སྣང་བར་མཛད་པའོ། །

[Block 514 [HEADING]]
###### **སངས་རྒྱས།** ^4-1-9-2-1-3-2-0

[Block 515]
ཡང་མདོ་ལས།

[Block 516]
བཟང་པོ་ངན་པ་དེ་བཞིན་བར་མ་ཡང་། །ཞེས་པ་ནས། སངས་རྒྱས་ཆོས་འདི་རབ་ཏུ་སྟོན་པ་ནི། །ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་སྣང་བ་བསྟན་ཏེ། བཅོམ་ལྡན་འདས་ཉིད་སེངྒེ་བཞིན་བག་ཚ་བ་མི་མངའ་བར་ཆོས་སྟོན་པ་ལ་མངའ་བརྙེས་པའོ། །

[Block 517 [HEADING]]
###### **ཆོས་ཐོས་པ།** ^4-1-9-2-1-3-3-0

[Block 518]
སངས་རྒྱས་ཆོས་ནི༌[^565]རབ་ཏུ་སྟོན་པ་ནི། [^566]ཞེས་པ་ནི། ཆོས་ཐོས་པ་བསྟན་ཏེ། སྤོབས་བ་སོ་སོ་ཡང་དག་པར་རིག་པས་དཔེ་དང་དོན་གསལ་བར་སྟོན༌[^567]པའོ། །

[Block 519]
མདོ་ལས།

[Block 520]
སེམས་ཅན་གང་དག་སྡུག་བསྔལ་གཟིར་བ་རྣམས། ཞེས་པ་ནས། དེ་དག་ལ་ནི་བྱང་ཆུབ་ཕྱིར་བསྔགས་གསུང་། །ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེ་ཆུང་གསུམ་གྱི་རིམ་པ་བསྟན་ཏེ། མདོ་ལས་འབྱུང་བ་བཞིན་དུ་ཆུད་པར་བྱའོ། །

[Block 521]
མདོ་ལས།

[Block 522 [HEADING]]
###### **འཁོར་བཞི།** ^4-1-9-2-1-3-4-0

[Block 523]
ཤིན་ཏུ་མཐོང་ཞིང༌[^568]ཐོས་སོ་འཇམ་པའི་དབྱངས། །ཞེས་པ༌[^569]ལས་ནི་ཆ་ཙམ་སྨོས་པར་བྱ་ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ་འདིས་ནི་འཁོར་རྣམ་བཞི་སྣང་བར་བསྟན་ཏེ། འཁོར་དེ་དག་གིས༌[^570]ལམ་བསྒྲུབས་པ་དང་འབྲས་བུ་ཐོབ་པའང་སྣང་ཞེས་པའི་དོན་ཏེ། ཚིག་གོང་མས་ནི་ཉན་ཐོས་ཚིག་འོག་མས་ནི་བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་བསྟན་ཏོ། །

[Block 524 [HEADING]]
###### **བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ།** ^4-1-9-2-1-3-5-0

[Block 525 [HEADING]]
###### **བརྩོན་འགྲུས་སྣ་ཚོགས།** ^4-1-9-2-1-3-5-1-0

[Block 526]
མདོ་ལས་མཐོང་ཞིང་རྣམ་པ་མང་པོ་དག་ན་ཡང་། །ཞེས་པ་ནས། བརྩོན་འགྲུས་སྣ་ཚོགས་བྱང་ཆུབ་བསྐྱེད་པ་དག །ཅེས་པའི་བར་དུ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་བསྟན་ཏེ། ཚིགས་སུ་བཅད་པ་འདིས༌[^571]ནི་བརྩོན་འགྲུས་སྣ་ཚོགས་བསྟན། རྩ་བ་བདུན་གྱིས་ནི་དངོས་པོ་བསྟན། ཡང་རྩ་བ་ཕྱེད༌[^572]དང་བཅུ་བཞིས་ནི་མོས་པས༌[^573]སྤྱོད་པ་སྣ་ཚོགས་བསྟན་ཏོ། །

[Block 527]
གང༌[^574]གཱ་ཞེས་པ་ནི་ཆུ་བོ་མ་དྲོས་པ་ལས་ཆུ་བོ་བཞི་འབྱུང་བའི་གཅིག་གོ། །

[Block 528]
དེ་བྱེ་མ་མང་བའི་ཕྱིར་མང་བའི་དཔེར་བསྟན་ཏོ། །

[Block 529 [HEADING]]
###### **དངོས་པོ།** ^4-1-9-2-1-3-5-2-0

[Block 530]
མདོ་ལས།
--- END BLOCKS ---
