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
[Block 4341]
གཉིས་པ་ལ་ནི་ནང་རབ་ཏུ་དང་བ་མེད་དེ། ཉོན་མོངས་པས་རྙོག་པའི༌[^3130]ཕྱིར་རོ། །

[Block 4342]
གསུམ་པ་ལ་ནི་དྲན་པ་དང་ཤེས་བཞིན་མེད་དེ། ཉོན་མོངས་པ་ཅན་གྱི་བདེ་བས༌[^3131]ཀུན་དུ་རྨོངས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 4343]
བཞི་པ་ལ་ནི་བཏང་སྙོམས་དང་དྲན་པ་ཡོངས་སུ་དག་པ་མེད་དེ། ཉོན་མོངས་པས་དྲི་མ་ཅན་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 4344]
རེ་ཞིག་ཁ་ཅིག་དེ་སྐད་ཟེར་རོ། །

[Block 4345]
ཁ༌[^3132]ཅིག་ཤིན་ཏུ་སྦྱངས་བཏང་སྙོམས། །ཁ་ཅིག་ན་རེ་ཉོན་མོངས་པ་ཅན་དང་པོ་དང་གཉིས་པ་དག་ན་ནི་ཤིན་ཏུ་སྦྱངས་པ་མེད་ལ་གསུམ་པ་དང་བཞི་པ་དག་ན་ནི་བཏང་སྙོམས་མེད་དེ། །དེ་གཉིས་ནི་དགེ་བའི་ས་མང་པོ་པ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 4346 [HEADING]]
#### སྐྱོན་བརྒྱད་ལས་གྲོལ་བ། ^5-1-8-0

[Block 4347]
བཅོམ་ལྡན་འདས་ཀྱིས་བསམ་གཏན་གསུམ་ནི་སྐྱོན་དང་བཅས་པའི་ཕྱིར་གཡོ་བ་དང་བཅས་པ་དག་ཡིན་ནོ་ཞེས་བཀའ་སྩལ་ཏེ། །[^3133]སྐྱོན་བརྒྱད་ལས་ནི་གྲོལ་བའི་ཕྱིར།

[Block 4348 [VERSE]]
[^3134]བཞི་པ་གཡོ་བ་མེད་པ་ཡིན། །
སྐྱོན་དེ་དག་ཀྱང་གང་ཞེ་ན། །
རྟོག་དང་དཔྱོད་དང་དབུགས་དག་དང་། །
བདེ་བ་ལ་སོགས་བཞི་ཡིན་ནོ། །

[Block 4349]
རྟོག་པ་དང་། དཔྱོད་པ་དང་། བདེ་བ་དང་། སྡུག་བསྔལ་བ་དང་། ཡིད་བདེ་བ་དང་། ཡིད་མི་བདེ་བ་དང་། དབུགས་རྔུབ་པ་དང་དབུགས་འབྱུང་བ་སྟེ། བསམ་གཏན་བཞི་པ་ན་ནི་སྐྱོན་བརྒྱད་པོ་དེ༌[^3135]དག་གཅིག་ཀྱང་མེད་པས་དེའི་ཕྱིར་དེ་ནི་མི༌[^3136]གཡོ་བ་ཞེས་བཤད་དོ། །

[Block 4350]
གཞན་དག་ན་རེ་བཞི་པ་ནི་རྟོག་པ་དང་། དཔྱོད་པ་དང་། དགའ་བ་དང་། བདེ་བ་དག་གིས་གཡོ་བར་མི་འགྱུར་བའི་ཕྱིར་མི་གཡོ་བ་ཡིན་ཏེ། མདོ་ལས་རླུང་མེད་པའི་མར་མེ་དཔེར་མཛད་པའི་ཕྱིར༌[^3137]ཞེས་ཟེར་རོ། །

[Block 4351 [HEADING]]
#### སྐྱེ་བའི་བསམ་གཏན་དག་ན་ཡོད་པའི་ཚོར་བ། ^5-1-9-0

[Block 4352]
བསམ་གཏན་གཉིས་པ༌[^3138]ན་ནི་དགའ་བ་ཞེས་སྨོས་པའི་ཕྱིར་ཡིད་བདེ་བ་ཡོད་པར་བཤད།

[Block 4353]
གསུམ་པ་ན༌[^3139]ནི་བདེ་བ།

[Block 4354]
བཞི་པ་ན་ནི་བཏང་སྙོམས་ཡོད་པར་བཤད་ན། དེ་ཅི།[^3140] སྙོམས་པར་འཇུག་པའི་བསམ་གཏན་དག་ན་ཡོད་པའི་ཚོར་བ་གང་དག་ཡིན་པ་དེ་དག་ཉིད་སྐྱེ་བའི་བསམ་གཏན་དག་ན༌[^3141]ཡོད་དམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 4355]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 4356 [VERSE]]
སྐྱེ་བའི་བསམ་གཏན་དག་ན་ནི། །
ཡིད་བདེ་བ༌[^3142]དང་བཏང་སྙོམས་དང་། །
བཏང་སྙོམས་ཡིད་བདེ་བདེ་བ་དང་། །
བཏང་སྙོམས་བཏང་སྙོམས་ཚོར་བ་ཡོད། །

[Block 4357]
སྐྱེ་བའི་བསམ་གཏན་དང་པོ་ན་ནི། ཚོར་བ་གསུམ་ཡོད་དེ། རྣམ་པར་ཤེས་པའི་ཚོགས་གསུམ་པའི་བདེ་བ་དང་། ཡིད་ཀྱི་ས་པའི་ཡིད་བདེ་བ་དང་། རྣམ་པར་ཤེས་པའི་ཚོགས་བཞི་པའི་བཏང་སྙོམས་སོ། །

[Block 4358]
སྐྱེ་བའི་བསམ་གཏན་གཉིས་པ་ན་ནི་ཚོར་བ་གཉིས་ཏེ། ཡིད་ཀྱི་ས་པའི་ཡིད་བདེ་བ་དང་བཏང་སྙོམས་སོ། །

[Block 4359]
རྣམ་པར་ཤེས་པའི་ཚོགས་གཞན་མེད་པའི་ཕྱིར་བདེ་བ་དང་། ཡིད་ཀྱི་ས་པའི་ཡིད་བདེ་བ་དང་། རྣམ་པར་ཤེས་པའི་ཚོགས་བཞི་པའི་བཏང་སྙོམས་སོ། །

[Block 4360]
སྐྱེ་བའི་བསམ་གཏན་གཉིས་པ་ན་ནི་ཚོར་བ་གཉིས་ཏེ། ཡིད་ཀྱི་ས་པའི་ཡིད་བདེ་བ་དང་བཏང་སྙོམས་སོ། །

[Block 4361]
རྣམ་པར་ཤེས་པའི་ཚོགས་གཞན་མེད་པའི་ཕྱིར་བདེ་བ༌[^3143]མེད་དོ། །

[Block 4362]
སྐྱེ་བའི་བསམ་གཏན་གསུམ་པ་ན་ནི་ཚོར་བ་གཉིས་ཏེ། ཡིད་ཀྱི་ས་པའི་བདེ་བ་དང་། བཏང་སྙོམས༌[^3144]སྐྱེ་བའི་བསམ་གཏན་བཞི་པ་ན་ནི་བཏང་སྙོམས་ཁོ་ན་ཡོད་དོ། །

[Block 4363 [HEADING]]
#### གཉིས་པ་སོགས་ན་ལུས་མིག་རྣ་བའི་རྣམ་ཤེས། ^5-1-10-0

[Block 4364]
གལ་ཏེ་བསམ་གཏན་གསུམ་པ་ལ་སོགས་པ་དག་ན་རྣམ་པར་ཤེས་པའི་ཚོགས་གསུམ་མེད་པ་ལ་རྟོག་པ་དང༌[^3145]དཔྱོད་པ་དག་ཀྱང་མེད་ན་ཇི་ལྟར་ན་དེ་དག་གིས་མཐོང་བ་ནས་རེག་པའི་བར་དུ་འགྱུར། ཇི་ལྟར་ན་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་བྱེད་ཅེ་ན། དེ་དག་ཏུ་སྐྱེས་པ་རྣམས་ལ་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་མེད་པ་ཉིད་ཀྱང་མ་ཡིན་ལ་རང་གི་ས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 4365]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 4366 [VERSE]]
གཉིས་པ་སོགས་ན་ལུས་མིག་དང་། །
རྣ་བའི་རྣམ་ཤེས་རྣམ་རིག་སློང་། །
གང་ཡིན་དེ་ནི་དང་པོར་གཏོགས། །

[Block 4367]
བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་དག་ན་ནི་སྤྲུལ་པའི་སེམས་བཞིན་དུ་གང་གིས་ན་དེ་དག་གིས་མཐོང་བས་ན༌[^3146]རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་བྱེད་པའི་བར་བསམ་གཏན་དང་པོའི་ས་པའི་མིག་དང་། རྣ་བ་དང་། ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་དང་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་པར་བྱེད་པ༌[^3147]མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 4368]
དེ་ལུང་མ་བསྟན་ཉོན་མོངས་མིན།[^3148] །དེ་དག་མངོན་སུམ་དུ་བྱེད་པ་བསམ་གཏན་དང་པོའི་ས་པའི་རྣམ་པར་ཤེས་པ་གང་ཡིན་པ་དེ་ནི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཡིན་གྱི། འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་ཉོན་མོངས་པ་ཅན་ཡང་མ་ཡིན་ལ། དམན་པའི་ཕྱིར་དགེ་བ་ཡང་མ་ཡིན་ནོ། །

[Block 4369]
བསམ་གཏན་གྱི་བྱ་བ་རྫོགས་སོ།། །།

[Block 4370 [HEADING]]
### བསམ་གཏན་དང་གཟུགས་མེད་པ་འཐོབ་པ། ^5-2-0

[Block 4371]
ཡང་དག་པ་ས༌[^3149]ལ་སོགས་པའི་བསམ་གཏན་དང་གཟུགས༌[^3150]མེད་པ་རྣམས་ཇི་ལྟར་འཐོབ་ཅེ་ན།

[Block 4372 [HEADING]]
#### དག་པ་པ་འཐོབ་པ། ^5-2-1-0

[Block 4373 [VERSE]]
དེ་དང་མི་ལྡན་འདོད་ཆགས་བྲལ། །
སྐྱེ་བ་ལས་ནི་དག་པ་འཐོབ། །

[Block 4374]
དེ་དང་མི་ལྡན་པ་ནི་བསམ་གཏན་ནམ་གཟུགས་མེད་པ་དག་ས༌[^3151]འོག་མ་ལས་འདོད་ཆགས་དང་བྲལ་བའམ། སྲིད་པའི་རྩེ་མོ་མ་གཏོགས་པས་འོག་མར་སྐྱེ་བ་ལས་འཐོབ་སྟེ། དེ་ནི་སྐྱེ་བས་འཐོབ་པ་མེད་དོ། །ཅིའི་ཕྱིར་དེ་དང་མི་ལྡན་པ་ཞེས་བརྗོད་ཅེ་ན། དག་པ་པ་དང་ལྡན་པ་ནི་སྦྱོར་བ་ལས་ཀྱང་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པའི་དག་པ་པ༌[^3152]འཐོབ་ལ། ཡོངས་སུ་ཉམས་པ་ལས་ཀྱང་ཉམས་པའི་ཆ་དང་མཐུན་པ་འཐོབ་བོ། །

[Block 4375]
དེ་ཉིད་ཀྱི་ཕྱིར་བསམ་གཏན་དག་པ་པ་འདོད་ཆགས་དང་བྲལ་བས་འཐོབ་པར་འགྱུར་ལ་འདོད་ཆགས་དང་བྲལ་བས་འདོར་བར༌[^3153]འགྱུར་བ་དང་དེ་བཞིན་དུ་ཡོངས་སུ་ཉམས་པ་དང་སྐྱེ་བས༌[^3154]འཐོབ་པ་དང་། འདོར་བར༌[^3155]འགྱུར་བ་ཡོད་དམ་ཞེ་ན་ཡོད་དེ། བསམ་གཏན་དང་པོ་ཉམས་པའི༌[^3156]ཆ་དང་མཐུན་པར་རོ། །

[Block 4376]
དེ་ནི་འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བས་འཐོབ་ལ། ཚངས་པའི་འཇིག་རྟེན་ལས་འདོད་ཆགས་དང་བྲལ་བས་འདོར་རོ། །

[Block 4377]
ཚངས་པའི་འཇིག་རྟེན་ལས་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་པ་ལས་འཐོབ་ལ། འདོད་པ་ལ་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་པ་ལས་འདོར་རོ། །

[Block 4378]
གང༌[^3157]ནས་ཚངས་པའི་འཇིག་རྟེན་དུ་སྐྱེ་བ་ན་འཐོབ་ལ། དེས་ན་འདོད་པའི་ཁམས་སུ་སྐྱེ་བ་ན་འདོར་རོ༌[^3158]ཞེས་འབྱུང་ངོ་། །

[Block 4379 [HEADING]]
#### ཟག་མེད་འཐོབ་པ། ^5-2-2-0

[Block 4380 [VERSE]]
ཟག་མེད་འདོད་ཆགས་བྲལ་བ་ཡིས། །
དེ་དང་མི་ལྡན་པ་ལས་འཐོབ། །
--- END BLOCKS ---
