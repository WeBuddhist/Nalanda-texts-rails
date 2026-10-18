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
[Block 4306]
གཞན་དག་ན་རེ་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་དག་ན༌[^2584]ཡང་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་རྣམ་པར༌[^2585]རིག་བྱེད་ནི་ཡོད་ཀྱི་དགེ་བ་ཡང་མེད་ལ། ཉོན་མོངས་པ་ཅན་ཡང་མེད་དོ། །

[Block 4307]
[^2586]ཅིའི་ཕྱིར་ཞེ་ན། དེ་དག་ཏུ་སྐྱེས་པ་ནི་ས་འོག་མ་པའི༌[^2587]སེམས་གང་གིས་ན་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་འགྱུར་བ་དེ་ལྟ་བུ་ནི་མངོན་སུམ་དུ་མི་བྱེད་དེ། དམན་པ་དང་སྤངས་ཟིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་ཏེ་སྔ་མ་ཁོ་ན་བརྗོད་དོ། །

[Block 4308]
ཅིའི་ཕྱིར་ཚངས་པའི་འཇིག་རྟེན་ཡན་ཆད་ན་རྣམ་པར་རིག་བྱེད་མེད་ལ། འདོད་པའི་ཁམས་ན་ཡང་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་མེད་ཅེ་ན། གང་ཕྱིར་ཀུན་སློང་མེད། རྟོག་པ་དང་དཔྱོད་པ་དང་བཅས་པའི་སེམས་ཀྱིས་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་བྱེད་ན། དེ་ཡང་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་དག་ན་མེད་དོ། །

[Block 4309]
བསྒོམ་པས་སྤང་བར་བྱ་བས་སློང་བར་བྱེད་ཀྱི་དེ་ཁ་ནང་དུ་བལྟས་པའི་ཕྱིར་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 4310]
[^2588]བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་སེམས་དེ་ཡང་འདོད་པའི་ཁམས་ན་མེད་དོ། །

[Block 4311 [HEADING]]
###### ཆོས་རྣམས་ཀྱི་དགེ་བ་དང་མི་དགེ་བ་ཉིད། ^4-2-2-1-1-0

[Block 4312]
ཡང་ནི་ཀུན་ནས་སློང་བའི་དབང་པོ༌[^2589]ཁོ་ན་ལས་ཆོས་རྣམས་ཀྱི་དགེ་བ་དང་མི་དགེ་བ་ཉིད་དུ་རིག་པར་བྱ་འམ༌[^2590]ཞེ་ན། སྨས་པ། མ་ཡིན་ནོ། །

[Block 4313]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། རྣམ་པ་བཞིས་ཏེ། དོན་དམ་པ་དང་། ངོ་བོ་ཉིད་དང་། མཚུངས་པར་ལྡན་པ་དང་། ཀུན་ནས་སློང་བས་སོ། །

[Block 4314 [HEADING]]
###### **དགེ་བ།** ^4-2-2-1-1-1-0

[Block 4315 [HEADING]]
###### **དོན་དམ་པར་དགེ་བ།** ^4-2-2-1-1-1-1-0

[Block 4316]
དེ་ལ་རེ་ཞིག །ཐར་པ་དམ་པའི་དོན་དུ་དགེ །མྱ་ངན་ལས་འདས་པ་ནི་སྡུག་བསྔལ་ཐམས་ཅད་ཉེ་བར་ཞི་བ་ཡིན་ཏེ། དེ་བས་ན་མཆོག་ཏུ་བདེ་བའི་ཕྱིར༌[^2591]དོན་དམ་པར་དགེ་བ་སྟེ་ནད་མེད་པ་བཞིན་ནོ། །

[Block 4317 [HEADING]]
###### **ངོ་བོ་ཉིད་ཀྱིས་དགེ་བ།** ^4-2-2-1-1-1-2-0

[Block 4318]
རྩ་བ༌[^2592]ངོ་ཚ་ཁྲེལ་ཡོད་བདག་ཉིད་ཀྱིས། །དགེ་བའི་རྩ་བ་གསུམ་དང་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་ནི་གཞན་མཚུངས་པར་ལྡན་པ་དང་། ཀུན་ནས་སློང་བ་ལ་མི་ལྟོས་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས༌[^2593]དགེ་བ་ཡིན་ཏེ་འཕྲོད་པའི་སྨན་བཞིན་ནོ། །

[Block 4319 [HEADING]]
###### **མཚུངས་པར་ལྡན་པས་དགེ་བ།** ^4-2-2-1-1-1-3-0

[Block 4320]
དེ་དག་དང་ལྡན་མཚུངས་ལྡན་གྱིས། །དགེ་བའི་རྩ་བ་དང་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་དེ་དག་ཉིད་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་ནི་མཚུངས་པར་ལྡན་པས་དགེ་བ་དག་ཡིན་ཏེ།[^2594] དེ་དག་དང༌[^2595]མཚུངས་པར་མི་ལྡན་པ་རྣམས་ལ་དགེ་བ་ཉིད་མེད་པའི་ཕྱིར་སྨན་དང་སྦྱར་བའི་བཏུང་བ་བཞིན་ནོ། །

[Block 4321 [HEADING]]
###### **ཀུན་ནས་སློང་བས་དགེ་བ།** ^4-2-2-1-1-1-4-0

[Block 4322]
བྱ་བ་ལ་སོགས་ཀུན་སློང་བས། །དགེ་བའི་རྩ་བ་ལ་སོགས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་དེ་དག་ཁོ་ནས་ཀུན་ནས་སློང་བའི༌[^2596]ལུས་དང་ངག་གི་ལས་དང་། སྐྱེ་བ་ལ་སོགས་པ་དང་། ཐོབ་པ་དང་། འགོག་པ་དང་། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་རྣམས་ནི་ཀུན་ནས་སློང་བས༌[^2597]དགེ་བ་ཡིན་ཏེ་སྨན་དང་སྦྱར་བའི་བཏུང་བ་ལས་འབྱུང་བའི༌[^2598]འོ་མ་བཞིན་ནོ། །

[Block 4323]
བསྐལ་པ༌[^2599]མི་མཉམ་པའི་སེམས་ཀྱི༌[^2600]ཀུན་ནས་སློང་བའི༌[^2601]ཐོབ་པ་རྣམས་ཇི་ལྟར་དགེ་བ་ཉིད་ཡིན་པ་ནི་བརྗོད་དགོས་སོ། །

[Block 4324 [HEADING]]
###### **མི་དགེ་བ།** ^4-2-2-1-1-2-0

[Block 4325]
དགེ་བ་ཇི་སྐད་དུ་བཤད་པ་དེ་ལས།

[Block 4326 [HEADING]]
###### **དོན་དམ་པར་མི་དགེ་བ།** ^4-2-2-1-1-2-1-0

[Block 4327]
བཟློག་པ་ནི༌[^2602]མི་དགེ །ཇི་ལྟར་བྱས་པས་ཤེ་ན། འཁོར་བའི༌[^2603]སྡུག་བསྔལ་ཐམས་ཅད་འཇུག་པའི་བདག་ཉིད་ཀྱིས༌[^2604]མཆོག་ཏུ་མི་བདེ་བའི་ཕྱིར་དོན་དམ་པར་མི་དགེ་བ་ཡིན་ནོ། །

[Block 4328 [HEADING]]
###### **ངོ་བོ་ཉིད་ཀྱིས་མི་དགེ་བ།** ^4-2-2-1-1-2-2-0

[Block 4329]
མི་དགེ་བའི་རྩ་བ་དང་ངོ་ཚ་མེད་པ་དང་ཁྲེལ་མེད་པ་རྣམས་ནི་ངོ་བོ་ཉིད་ཀྱིས་སོ། །

[Block 4330 [HEADING]]
###### **མཚུངས་པར་ལྡན་པས་མི་དགེ་བ།** ^4-2-2-1-1-2-3-0

[Block 4331]
དེ་དག་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་ནི་མཚུངས་པར་ལྡན་པས་སོ། །

[Block 4332 [HEADING]]
###### **ཀུན་ནས་སློང་བས་མི་དགེ་བ།** ^4-2-2-1-1-2-4-0

[Block 4333]
དེ་དག་གིས་ཀུན་ནས་སློང་བའི༌[^2605]ལུས་དང་ངག་གི་ལས་དང་། སྐྱེ་བ་ལ་སོགས་པ་དང་། ཐོབ་པ་རྣམས་ནི་ཀུན་ནས་སློང་བ༌[^2606]ལས་ཏེ་ནད་དང་མི་འཕྲོད་པའི་སྨན་ལ་སོགས་པས༌[^2607]དཔེར་བྱའོ། །

[Block 4334 [HEADING]]
###### **ལུང་དུ་མ་བསྟན་པ།** ^4-2-2-1-1-3-0

[Block 4335]
དེ་ལྟ་ན་འོ་ན་ནི་འཁོར་བའི་ཁོངས་སུ་གཏོགས་པའི་ཕྱིར་ཟག་པ་དང་བཅས་པ་ཅུང་ཟད་ཀྱང་ལུང་དུ་མ་བསྟན་པའམ། དགེ་བར་མི་འགྱུར་རོ་ཞེ་ན། དོན་དམ་པར་དེ་སྐད་དུ་བཤད་ཀྱི་ཟག་པ་དང་བཅས་པ་གང་ཞིག་རྣམ་པར་སྨིན་པའི་ཕྱིར་ལུང་དུ་མ་བསྟན་པ༌[^2608]ཞེས་བྱ་ལ། རྣམ་པར་སྨིན་པ་ཡིད་དུ་འོང་བ་ཅན་ནི་དགེ་བ༌[^2609]ཞེས་བྱའོ། །

[Block 4336]
གལ་ཏེ་དོན་དམ་པར༌[^2610]ལུང་དུ་མ་བསྟན་པ་བཙལ་ན་ནི་དེ་ལ། དོན་དམ་པར་ལུང་མ་བསྟན་པ་དག །འདུས་མ་བྱས་གཉིས་པོ་ནམ་མཁའ་དང་སོ་སོར་མ་བརྟགས་པས་འགོག་པ་ནི་རྣམ་གྲངས་མེད་པར་ལུང་དུ་མ་བསྟན་པ་དག་ཡིན་ནོ། །

[Block 4337 [HEADING]]
###### ཀུན་ནས་སློང་བ་རྣམ་པ་གཉིས། ^4-2-2-1-2-0

[Block 4338]
ད་ནི་འདི་དཔྱད་པར་བྱ་སྟེ། གལ་ཏེ་ཀུན་ནས་སློང་བའི་དབང་གིས་ལུས་དང་ངག་གི་ལས་དག་དགེ་བ་དང་མི་དགེ་བ་ཉིད་ཡིན་ན། ཅི་སྟེ་འབྱུང་བ་ཆེན་པོ་རྣམས་མ་ཡིན་ཞེ་ན། བྱེད་པ་པོ་ནི་ལས་ལ་སེམས་པ་ཡིན་གྱི་འབྱུང་བ་རྣམས་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4339]
མཉམ་པར༌[^2611]བཞག་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ལ་ནི་བསམ་པ་མེད་དོ། །

[Block 4340]
མཉམ་པར་མ་བཞག་པའི་སེམས་ནི་སྐལ་བ་མི་མཉམ་པའི་ཕྱིར་དེ་ཀུན་ནས་སློང་བར་བྱེད་པ་མ་ཡིན་ན་ཇི་ལྟར་དེ་དགེ་བ་ཉིད་ཡིན་ནོ། །

[Block 4341]
ཡང་ན་ལྷའི་མིག་དང་རྣ་བ་དག་ཀྱང་དགེ་བ་ཉིད་དུ་ཐལ་བར་འགྱུར་བས་འདི་ལ་འབད་པར་བྱའོ།[^2612] །མཐོང་ནས༌[^2613]སྤང་བར་བྱ་བའི་སེམས་ནི་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་གང་བཤད་པ། འོ་ན་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ལོག་པར་ལྟ་བ་དེ་ལས་ནི་ལོག་པར་རྟོག་པ་དང་ལོག་པའི་ངག་དང་ལོག་པའི་ལས་ཀྱི་མཐའ་འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་གསུངས་ཤེ་ན། འདི་ནི་འགལ་བ་མེད་དེ། འདི་ལྟར།

[Block 4342 [VERSE]]
ཀུན་སློང་རྣམ་གཉིས་རྒྱུ་དང་ནི། །
དེ་ཡི་དུས་ཀྱིས་སློང་ཞེས་བྱ། །

[Block 4343]
ཀུན་ནས་སློང་བ་ནི༌[^2614]རྣམ་པ་གཉིས་ཏེ། རྒྱུའི་ཀུན་ནས་སློང་བ་དང་། དེའི་དུས་ཀྱིས༌[^2615]ཀུན་ནས་སློང་བ་སྟེ། དེའི་དུས་ཁོ་ན་ན་དེ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 4344 [VERSE]]
གཉིས་ལས་དང་པོ་རབ་འཇུག་བྱེད། །
གཉིས་པ་རྗེས་སུ་འཇུག་བྱེད་ཡིན། །

[Block 4345]
རྒྱུའི་ཀུན་ནས་སློང་བ་ནི་འཕེན་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡིན་ནོ། །
--- END BLOCKS ---
