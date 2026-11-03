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
མདོ་ལས་མཐོང་ཞིང་རྣམ་པ་མང་པོ་དག་ན་ཡང་། །ཞེས་པ་ནས། བརྩོན་འགྲུས་སྣ་ཚོགས་བྱང་ཆུབ་བསྐྱེད་པ་དག །ཅེས་པའི་བར་དུ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་བསྟན་ཏེ། ཚིགས་སུ་བཅད་པ་འདིས༌[^571]ནི་བརྩོན་འགྲུས་སྣ་ཚོགས་བསྟན། རྩ་བ་བདུན་གྱིས་ནི་དངོས་པོ་བསྟན། ཡང་རྩ་བ་ཕྱེད༌[^572]དང་བཅུ་བཞིས་ནི་མོས་པས༌[^573]སྤྱོད་པ་སྣ་ཚོགས་བསྟན་ཏོ། །

[Block 527]
གང༌[^574]གཱ་ཞེས་པ་ནི་ཆུ་བོ་མ་དྲོས་པ་ལས་ཆུ་བོ་བཞི་འབྱུང་བའི་གཅིག་གོ། །

[Block 528]
དེ་བྱེ་མ་མང་བའི་ཕྱིར་མང་བའི་དཔེར་བསྟན་ཏོ། །

[Block 529 [HEADING]]
###### **དངོས་པོ།** ^4-1-9-2-1-3-5-2-0

[Block 530]
མདོ་ལས།

[Block 531]
ལ་ལ་སྦྱིན་པ་སྦྱིན་པའང༌[^575]དེ་བཞིན་ཏེ། །ཞེས་པ་ནས། སྨོན་པ་དེ་བཞིན་གཤེགས་ཀྱི་ཡེ་ཤེས་ལ། །ཞེས་པའི་བར་དུ་འདིས༌[^576]ནི་སྦྱིན་པ་སྣ་ཚོགས་ཀྱི་མཚན་ཉིད་བསྟན་ཏེ། འདི༌[^577]ལའང་རྣམ་པ་གཉིས་སུ་དབྱེའོ། །

[Block 532 [HEADING]]
###### **ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག།** ^4-1-9-2-1-3-5-2-1-0

[Block 533]
དང་པོའི་ཚིགས་བཅད་བཅོ་ལྔས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་བསྟན། ཚིགས་སུ་བཅད་པ༌[^578]གཉིས་ཀྱིས་ནི་རླུང་བརྒྱད་ཀྱིས་མི་བསྐྱོད་པར་བསྟན། ཚིགས་སུ་བཅད་པ༌[^579]དྲུག་གིས་ནི་སྦྱིན་པ་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས་ནི་ཚུལ་ཁྲིམས་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས༌[^580]བཟོད་པ་དང་བརྩོན་འགྲུས་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས་ནི་བསམ་གཏན་བསྟན། དེའི་འོག་མ་གསུམ་གྱིས་ནི་ཤེས་རབ་བསྟན་ཏོ། །

[Block 534 [HEADING]]
###### **སྦྱིན་པ།** ^4-1-9-2-1-3-5-2-1-1-0

[Block 535]
སྦྱིན་པ་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ། རྩ་བ་བཞིས་ནི་ཕྱིའི་ནོར་གྱིས་ཕན་གདགས་པ། དེའི་འོག་མ་གཅིག་གིས་ནི་ནང་གི་ཕན་གདགས་པ། དེའི་འོག་མ་གཅིག་གིས་ནི་ཕྱི་ནང་གཉིས་གའི་ཕན་གདགས་པའོ། །

[Block 536]
དང་པོ་བཞི་ལ་ཡང་རིན་པོ་ཆེ་བདུན་སྦྱིན་པ་དང་དབྱིག་བརྒྱད་སྦྱིན་པ་དང་། ཐེག་པ་སྦྱིན་པ་དང་། རྫས་སྣ་ཚོགས་སྦྱིན་པའོ། །

[Block 537]
རིན་པོ་ཆེ་བདུན་ནི་གསེར་དང་དངུལ་ལ་སོགས་པ་བདུན་ནོ། །

[Block 538]
དབྱིག་བརྒྱད་ནི་བྲན་ཕོ་མོ་དང་། ཤིང་རྟ་དང་། ཁྱོགས་རིན་པོ་ཆེས་སྤྲས་པ་ལ་སོགས་པའོ། །

[Block 539 [HEADING]]
###### **ཚུལ་ཁྲིམས།** ^4-1-9-2-1-3-5-2-1-2-0

[Block 540]
མདོ་ལས།

[Block 541]
འཇམ་དཔལ་བདག་གིས་མཐོང་བ་ལ་ལ་ན། །ཞེས་པ་ནས། ངུར་སྨྲིག་གོས་རྣམས་རབ་ཏུ་གྱོན་པར་བྱེད། །ཅེས་པའི་བར་དུ་འདིས་ནི༌[^581]རབ་ཏུ་འབྱུང་བའི༌[^582]མཚན་ཉིད་བསྟན་ཏེ། གང་རབ་ཏུ་བྱུང་ནས་འདུལ་བ་ལ་གནས་པ་དེ་སྤྱོད་པ་ཐམས་ཅད་ཀྱི་གཞི་ཡིན་པའི་ཕྱིར་རོ། །

[Block 542]
དེ་རབ་ཏུ་བྱུང་བའི་ཡོན་ཏན་ཡང་རྣམ་པ་ལྔ་སྟེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས༌[^583]སྐྱོབ་པ་དང་། འཆི་ཀར་དགའ་བ་བསྐྱེད་པ་དང་། ཚུལ་ཁྲིམས་བསྲུངས་པས༌[^584]བཤེས་གཉེན་བཟང་བ་དང་། ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་དང་། སྐྱེ་བ་ཐམས་ཅད་དུ་རབ་ཏུ་བྱུང་བའི་རྒྱུ་ལ་སོགས་པའོ། །

[Block 543]
མདོ་ལས།

[Block 544 [HEADING]]
###### **བཟོད་པ་དང་བརྩོན་འགྲུས།** ^4-1-9-2-1-3-5-2-1-3-0

[Block 545]
བདག་མཐོང་བྱང་ཆུབ་སེམས་དཔའ་ལ་ལ་དག །ཅེས་པ་ནས། ལ་ལ་ལུང་ནོད་ཁ་ཏོན་བྱེད༌[^585]ལ་དགའ། །ཞེས་པའི་བར་དུ་འདིས་ནི་མདོ་སྡེ་དཀའ་བ་འདོན་ཅིང་མདོ་ཟབ་མོ་ལ་སེམས་པའི༌[^586]བཟོད་པ་དང་ལྡན་པས་བཟོད་པ་དང་ལྡན་པ་བསྟན་ཏོ། །

[Block 546]
ཡང་མདོ་ལས།

[Block 547]
བདག་མཐོང་བྱང་ཆུབ་སེམས་དཔའ་ལ་ལ་དག །ཅེས་པ་ནས། ཡོངས་སུ་བསམས་པས་ཉེ་བར་རྟོགས་པར༌[^587]གྱུར། །ཅེས་པའི་བར༌[^588]དུ་འདིས༌[^589]ནི་གོ་ཆ་བགོས་པ་དང་དགེ་བ་སྡུད་པའི་བརྩོན་འགྲུས་བསྟན་ཏེ། བརྩོན་འགྲུས་རྣམ་པ་ལྔ་དང་ལྡན་ཞེས་པའི་དོན་ཏོ། །

[Block 548 [HEADING]]
###### **བསམ་གཏན།** ^4-1-9-2-1-3-5-2-1-4-0

[Block 549]
ཡང་མདོ་ལས།

[Block 550]
ཁ་ཅིག་གིས་ནི་འདོད་པ་མ་ལུས་སྤངས། །ཞེས་པ་ནས། །ཚིགས་བཅད་སྟོང་གིས་རྒྱལ་བ་རྒྱལ་པོ་ལའོ། །ཞེས་པའི་བར་དུ་འདི་གཉིས་ཀྱིས་ནི་བསམ་གཏན་ལ་གནས་པ་བསྟན་ཏོ།[^590] །བསམ་གཏན་གྱི་མངོན་པར་ཤེས་པ་ལ་སོགས་པ་བསྐྱེད་པས་དེ་བཞིན་གཤེགས་པ་མང་པོ་ལ་བསྟོད་པའི་སྤོབས་པ་སྐྱེ་བའོ། །

[Block 551 [HEADING]]
###### **ཤེས་རབ།** ^4-1-9-2-1-3-5-2-1-5-0

[Block 552]
མདོ་ལས།

[Block 553]
དྲན་དང་ལྡན་ཞིང་དུལ་བ་མི་འཇིགས་པ། །ཞེས་པ་ནས། །ཐོས་ནས་དེ་དག་ཆོས་རྣམས་འཛིན་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྤྱོད་པ་ཟབ་མོ་དང་ལྡན་ཞིང་ཐོས་པ་འཛིན་པར་གྱུར་པའོ། །

[Block 554]
མདོ་ལས།

[Block 555]
ཡོངས་སུ་སྒོམ་པ༌[^591]བདག་ཉིད་རྒྱལ་དབང་སྲས་པོ་རྣམས། །ཞེས་པ་ནས། །ཆོས་ཀྱི་རྔ་ནི༌[^592]ཤིན་ཏུ་རྡུང་བར་བྱེད། །ཅེས་པའི་བར་དུ་ནི་ཤེས་རབ་དང་ཏིང་ངེ་འཛིན་དང་ལྡན་པར་གྱུར་པའོ། །

[Block 556]
ཆོས་སྟོན་པ་ནི་རྣམ་པ་བཞི་སྟེ། དགའ་བས་ཕན་འདོགས་པའི་ཕྱིར་སྟོན་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^593]ཆེད་དུ་སྟོན་པ་དང་། བདུད་རྣམས་སྡང་བར་བྱེད་པ་དང་། བཀྲི་བ་དང་ངེས་པའི་དོན་གྱིས༌[^594]བརྡུང་བའོ། །

[Block 557 [HEADING]]
###### **རླུང་བརྒྱད་ཀྱིས་མི་བསྐྱོད་པ།** ^4-1-9-2-1-3-5-2-2-0

[Block 558]
མདོ་ལས།

[Block 559]
མངོན་པ༌[^595]ལ་ལས་བདེ་གཤེགས་བསྟན་པ་ལ། །ཞེས་པ་ནས། །བསྙེམས༌[^596]མེད་ཞི་ཞིང་རབ་ཏུ་ཞི་བར་སྤྱོད། །ཅེས་པའི་བར་དུ་ནི་འཇིག་རྟེན་གྱི་རླུང་བརྒྱད་ཀྱིས་མི་བསྐྱོད་པའི་དོན་ཏེ། འཇིག་རྟེན་གྱི་ཆོས་བརྒྱད་ནི་བསྟོད་པ་དང་སྨད་པ་ལ་སོགས་པའོ། །

[Block 560]
མདོ་ལས།

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
--- END BLOCKS ---
