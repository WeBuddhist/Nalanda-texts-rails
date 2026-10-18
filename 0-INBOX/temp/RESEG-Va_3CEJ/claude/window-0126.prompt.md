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
[Block 4411 [VERSE]]
ཚུལ་ཁྲིམས་དང་ནི་ལེགས་སྤྱད་དང་། །
ལས་དང་སྡོམ་པ་ཞེས་བྱའོ། །

[Block 4412]
ལས་མི་མཉམ་པ་ཅན་རྣམས་ཡང་དག་པར་འཇོག་པར་བྱེད་པས་ན༌[^2651]ཚུལ་ཁྲིམས་སོ། །

[Block 4413]
ངེས་པའི་ཚིག་ཏུ་ན་བསིལ་བའི་ཕྱིར་ཏེ།

[Block 4414]
ཚིགས་སུ་བཅད་པ་ལས།

[Block 4415 [VERSE]]
ལུས་ལས་ཡོངས་སུ་གདུང་མེད་པས། །
ཚུལ་ཁྲིམས་ཡང་དག་བླངས་པ་བདེ། །

[Block 4416]
ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 4417]
མཁས་པ་རྣམས་ཀྱིས་བསྔགས་པའི༌[^2652]ཕྱིར་ལེགས་པར་སྤྱད་པའོ། །

[Block 4418]
བྱ་བའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ལས་སོ། །

[Block 4419]
རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་བྱ་བ་མ་ཡིན་པའོ༌[^2653]ཞེས་མི་བྱའམ༌[^2654]དེ་ཇི་ལྟར་ན་བྱ་བ་ཡིན་ཞེ་ན། ངོ་ཚ་ཤེས་པ་རྣམས་ཡང་དག་པར་བླངས་པ་དེས་སྡིག་པ་མི་བྱེད་པས་ན་བྱ་བ་མ་ཡིན་པ་ཞེས་བྱ་ལ། དེ་ཡང་རྣམ་པར་རིག་བྱེད་དང་སེམས༌[^2655]དག་གིས་བྱེད་པས་ན་བྱ་བ་ཡིན་ནོ། །

[Block 4420]
གཞན་དག་ན་རེ་བྱ་བའི་རྒྱུ་ཡིན་པ་དང་། བྱ་བའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 4421]
ལུས་དང་ངག་སྡོམ་པའི་ཕྱིར་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཞེས་ཀྱང་བྱའོ། །

[Block 4422]
དེ་ལྟར་རེ་ཞིག་བྱེ་བྲག་མེད་པར་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཡང་དག་པར་བསྟན་ཏོ། །

[Block 4423]
ཡང་།

[Block 4424 [VERSE]]
དང་པོའི་རྣམ་རིག་རྣམ༌[^2656]རིག་མིན། །
སོ་སོར་ཐར་དང་བྱ་བའི་ལམ། །

[Block 4425]
སྡོམ་པ་ཡང་དག་པར་བླང་བའི༌[^2657]རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་པོ་དག་ནི་སོ་སོར་ཐར་པ་ཞེས་བྱ་སྟེ། དེས་སྡིག་པ་ལས་སོ་སོར་ཐར་པའི་ཕྱིར་ཏེ། སྤང་བའི༌[^2658]ཕྱིར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4426]
སོ་སོར་ཐར་པའི་སྡོམ་པ་ཞེས་ཀྱང་བྱ་སྟེ། ལུས་དང་ངག་སྡོམ་པའི་ཕྱིར་རོ། །

[Block 4427]
ལས་ཀྱི་ལམ་ཞེས་ཀྱང་བྱའོ། །

[Block 4428]
སྐད་ཅིག་མ་གཉིས་པ་ལ་སོགས་པ་ལ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཁོ་ན་ཡིན་གྱི་སོ་སོར་ཐར་པ་ནི་མ་ཡིན་ནོ། །

[Block 4429]
མཇུག་ཡིན་གྱི་ལས་ཀྱི་ལམ་དངོས་ནི་མ་ཡིན་ནོ། །

[Block 4430 [HEADING]]
###### **སྡོམ་པ་གང་ཞིག་གང་དང་ལྡན་པ།** ^4-2-2-2-1-2-0

[Block 4431 [HEADING]]
###### **སོ་སོར་ཐར་པའི་སྡོམ་པ་དང་ལྡན་པ།** ^4-2-2-2-1-2-1-0

[Block 4432]
ཡང་སྡོམ་པ་འདི་རྣམས་ལས་གང་ཞིག་གང་དང་ལྡན་ཞེ་ན། སོ་སོར་ཐར་དང་ལྡན་པ་བརྒྱད། །སོ་སོར་ཐར་པའི་སྡོམ་པ་དང་ནི་རིས་བརྒྱད་པོ་དགེ་སློང་དང་དགེ་སློང་མ་དང༌[^2659]

[Block 4433]
བརྒྱད་པ་བསྙེན་གནས་པའི་བར་དང་ལྡན་ནོ། །

[Block 4434]
ཡང་ཅི་ཕྱི་རོལ་པ་རྣམས་ལ་ཡང་དག་པར་བླངས་པའི་ཚུལ་ཁྲིམས་མེད་དམ་ཞེ་ན། ཡོད་མོད་ཀྱི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་སྲིད་པ་ལ་བརྟེན་པའི༌[^2660]ཕྱིར་གཏན་དུ་སྡིག་པ་ལས་སོ་སོར་ཐར་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 4435 [HEADING]]
###### **བསམ་གཏན་གྱི་སྡོམ་པ་དང་ལྡན་པ།** ^4-2-2-2-1-2-2-0

[Block 4436]
བསམ་གཏན་སྐྱེས་དང་དེ༌[^2661]ལྡན་པ། །བསམ་གཏན་ལས་བསམ་གཏན་གྱིས་བསྐྱེད་པས་ན་བསམ་གཏན་སྐྱེས་ཏེ། གང་བསམ་གཏན་དང་ལྡན་པ་དེ་གདོན་མི་ཟ་བར་བསམ་གཏན་གྱི་སྡོམ་པ་དང་ལྡན་ནོ། །

[Block 4437]
འདིར་ནི་ཉེར་བསྡོགས་ཀྱང་བསམ་གཏན་དུ་བརྗོད་ནས་བསྟན་ཏེ། དཔེར་ན་གྲོང་འདི་ན་སཱ་ལུའི་ཞིང་ཡོད་དོ། །

[Block 4438]
འབྲུའི་ཞིང་ཡོད་དོ་ཞེས༌[^2662]གྲོང་གི་ཉེ་འཁོར་ལ་ཡང་གྲོང་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 4439 [HEADING]]
###### **ཟག་པ་མེད་པའི་སྡོམ་པ་དང་ལྡན་པ།** ^4-2-2-2-1-2-3-0

[Block 4440]
ཟག་མེད་འཕགས་པའི་སེམས་ཅན་དང་། །ཟག་པ་མེད་པའི་སྡོམ་པ་དང་།[^2663] །འཕགས་པའི་གང་ཟག་རྣམས་ལྡན་ཏེ། །དེ་དག་ཀྱང་སློབ་པ་དང་མི་སློབ་པ་རྣམས་སོ། །

[Block 4441 [HEADING]]
###### **སེམས་ཀྱི་རྗེས་སུ་འབྲང་བའི་སྡོམ་པ་གཉིས།** ^4-2-2-2-1-3-0

[Block 4442]
ལྷན་ཅིག་འབྱུང་བའི་རྐྱེན་བཤད་པར་སེམས་ཀྱི་རྗེས་སུ་འབྲང་བའི་སྡོམ་པ་གཉིས་ཞེས་གང་བཤད་པ་དེ་གཉིས་གང་ཡིན་ཞེ་ན་གསུམ་པོ་འདི་དག་ཉིད་ལས།

[Block 4443 [VERSE]]
ཐ་མ་གཉིས་ནི་སེམས་རྗེས་འབྲང་། །
བསམ་གཏན་གྱི་སྡོམ་པ་དང་།
ཟག་པ་མེད་པའི་སྡོམ་པའོ། །

[Block 4444]
སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། སེམས༌[^2664]གཞན་དང་ལྡན་པ་དང་། སེམས་མེད་པ་ལ་ཡང་རྗེས་སུ༌[^2665]འཇུག་པའི་ཕྱིར་རོ། །

[Block 4445 [HEADING]]
###### **སྤོང་བའི་སྡོམ་པ།** ^4-2-2-2-1-4-0

[Block 4446]
[^2666]བསམ་གཏན་གྱི་སྡོམ་པ་དང་། ཟག་པ་མེད་པའི་སྡོམ་པ་དེ་དག་ཉིད༌[^2667]སྤོང་བའི་སྡོམ་པ་ཞེས་བྱ་བའི་མིང་འཐོབ་བོ། །གང་གི་གནས་སྐབས་སུ་ཞེ་ན། སྨྲས་པ།

[Block 4447 [VERSE]]
[^2668]བར་ཆད་མེད་ལམ་སྐྱེས་དེ་གཉིས། །
མི་ལྕོགས་མེད་ལ་སྤོང་ཞེས་བྱ། །

[Block 4448]
མི་ལྕོགས་པ་མེད་པ་ལ་བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པ་དེ་གཉིས་བར་ཆད་མེད་པའི་ལམ་དགུ་དག་ཏུ་སྤོང་བའི་སྡོམ་པ་ཞེས་བྱ་སྟེ། དེ་གཉིས་ཀྱིས་འཆལ་པའི་ཚུལ་ཁྲིམས་དང་། དེ་ཀུན་ནས་སློང་བར་བྱེད་པའི་ཉོན་མོངས་པ་རྣམས་སྤོང་བའི་ཕྱིར་རོ། །

[Block 4449]
དེ་ཉིད༌[^2669]ཀྱི་ཕྱིར་བསམ་གཏན་གྱི་སྡོམ་པ་ཡིན་ལ། སྤོང་བའི་སྡོམ་པ་མ་ཡིན་པ་ཡང་ཡོད་ཅེས་བྱ་བ་མུ་བཞིར་བྱ་སྟེ། མུ་དང་པོ་ནི་མི་ལྕོགས་པ་མེད་པའི་བར་ཆད་མེད་པའི་ལམ་མ་གཏོགས་པ་ཟག་པ་དང་བཅས་པའི་བསམ་གཏན་གྱི་སྡོམ་པའོ། །

[Block 4450]
གཉིས་པ་ནི་མི་ལྕོགས་པ་མེད་པའི་བར་ཆད་མེད་པའི་ལམ་དགུ་དག་ཏུ་ཟག་པ་མེད་པའོ། །
--- END BLOCKS ---
