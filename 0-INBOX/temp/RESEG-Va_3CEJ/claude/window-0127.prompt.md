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

[Block 4451]
གསུམ་པ་ནི་མི་ལྕོགས་པ་མེད་པའི་བར་ཆད་མེད་པའི་ལམ་དགུ༌[^2670]དག་ཏུ་ཟག་པ་དང་བཅས་པའོ། །

[Block 4452]
བཞི་པ་ནི་མི་ལྕོགས་པ་མེད་པའི་བར་ཆད་མེད་པའི་ལམ་མ་གཏོགས་པ་དང༌[^2671]ཟག་པ་མེད་པའི་སྡོམ་པའོ། །

[Block 4453]
དེ་བཞིན་དུ་ཟག་པ་མེད་པའི་སྡོམ་པ་ཡིན་ལ་སྤོང་བའི་སྡོམ་པ་མ་ཡིན་པ་ཡང་ཡོད་ཅེས་བྱ་བ་མུ་བཞིར་ཅི་རིགས་པར་རིག་པར་བྱའོ། །

[Block 4454 [HEADING]]
###### **ཡིད་དང་དབང་པོའི་སྡོམ་པ།** ^4-2-2-2-1-5-0

[Block 4455]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 4456 [VERSE]]
ལུས་ཀྱི་སྡོམ་པ་ལེགས་པ་སྟེ། །
ངག་གི་སྡོམ་པའང༌[^2672]ལེགས་པ་ཡིན། །

[Block 4457]
ཡིད་ཀྱི་སྡོམ་པའང་ལེགས་པ་སྟེ།[^2673] །ཐམས་ཅད་དུ་ནི་སྡོམ་པ་ལེགས། ། ཞེས་གང་གསུངས་པ་དང་། གང་ཡང་མིག་གི་དབང་པོ་འདི༌[^2674]སྡོམ་པས་བསྡམས་ཏེ། གནས་སོ་ཞེས་གསུངས་པ། ཡིད་དང་དབང་པོའི་སྡོམ་པ་འདི་གཉིས་ཀྱི་རང་བཞིན་ཅི་ཞེ་ན། འདི་གཉིས་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་རང་བཞིན་ནི་མ་ཡིན་ནོ། །

[Block 4458]
འོ་ན་ཅི་ཞེ་ན།

[Block 4459 [VERSE]]
ཤེས་བཞིན་དང་ནི་དྲན་དག་གཉིས། །
ཡིད་དང་དབང་པོ༌[^2675]སྡོམ་པ་ཡིན། །

[Block 4460]
གྲངས་བཞིན་དུ་ཤེས་པར་འགྱུར་དུ་འོང་བས་སོ་སོར་གཉིས་ཀྱི་རང་བཞིན་ཡིན་པར་བསྟན་པའི་ཕྱིར་ཡང་གཉིས་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡིད་ཀྱི་སྡོམ་པ་ཡང་དྲན་པ་དང་ཤེས་བཞིན་གྱི་རང་བཞིན་ཡིན་ལ། དབང་པོའི་སྡོམ་པ་ཡང་དྲན་པ་དང་ཤེས་བཞིན་གྱི་རང་བཞིན༌[^2676]ནོ། །

[Block 4461 [HEADING]]
###### རྣམ་པར་རིག་བྱེད་དམ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་ལྡན་པ། ^4-2-2-2-2-0

[Block 4462]
གང་ཞིག་རྣམ་པར་རིག་བྱེད་དམ། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གང་ཞིག་དང་དུས་ཇི་སྲིད་ཅིག་ཏུ་ལྡན་ཞེས་བྱ་བ་འདི་དཔྱད་པར་བྱ་སྟེ། དེ་ལ།

[Block 4463 [HEADING]]
###### **སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པ།** ^4-2-2-2-2-1-0

[Block 4464 [VERSE]]
སོ་སོར་ཐར་གནས༌[^2677]ཇི་སྲིད་དུ། །
མ་བཏང་བར་རྟག་ད་ལྟར་གྱི། །

[Block 4465]
རྣམ་རིག་མི༌[^2678]ལྡན། སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་གནས་པས་བཤད་པའི་གང་ཟག་གང་ཡིན་པ་དེ་ནི་ཇི་སྲིད་དུ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དེ་མི་གཏོང་བ་དེ་སྲིད་དུ་རྟག་ཏུ་ད་ལྟར་གྱི་དེ་དང་ལྡན་ནོ། །

[Block 4466]
སྐད་ཅིག་མ།

[Block 4467]
དང་པོ་ཕྱིན་ཆད་འདས་པ་དང་། །སྐད་ཅིག་མ་དང་པོ་ཕྱིན་ཆད་ནི་འདས་པ་དང་ཡང་ལྡན་ཏེ། ཐམས་ཅད་དུ་ཡང་ཇི་སྲིད་དུ་མ་བཏང་བར་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པར་རིག་པར་བྱའོ། །

[Block 4468]
སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་གནས་པ༌[^2679]ཇི་སྐད་དུ་བཤད་པ། སྡོམ་མིན་གནས་པའང་དེ་དང་འདྲ། །སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པ་ཡང་ཇི་སྲིད་དུ་སྡོམ་པ་མ་ཡིན་པ་མི་གཏོང་བ་དེ་སྲིད་དུ་རྟག་ཏུ་ད་ལྟར་གྱི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་ལྡན་ནོ། །

[Block 4469]
སྐད་ཅིག་མ་གཅིག་ཕྱིན་ཆད༌[^2680]ནི་འདས་པ་དང་ཡང་ལྡན་ནོ། །

[Block 4470 [VERSE]]
བསམ་གཏན་སྡོམ་དང་ལྡན་པ་ནི། །
རྟག་ཏུ་འདས་དང་མ་འོངས་དང་། །

[Block 4471]
བསམ་གཏན་གྱི་སྡོམ་པ་ཐོབ་པ་ནི་ཇི་སྲིད་དུ་མ་བཏང་གི་བར་དུ་རྟག་ཏུ་འདས་པ་དང་མ་འོངས་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་ལྡན་ཏེ། དེས་ནི་སྐད་ཅིག་མ་དང་པོ་ལ་ཡང་ཚེ་རབས་གཞན་དག་ཏུ་བཏང་བའི་བསམ་གཏན་གྱི་སྡོམ་པ་འདས་པ་ཐོབ་བོ། །

[Block 4472]
འཕགས་ནི་དང་པོ་འདས་དང་མིན། །འཕགས་པའི་གང་ཟག་ཀྱང་ཟག་པ་མེད་པ་དང་དེ་བཞིན་དུ་ལྡན་ལ། འདི་ནི་ཁྱད་པར་ཡིན་ཏེ། ལམ་སྔོན་མ་བསྐྱེད་པའི༌[^2681]ཕྱིར་དེ༌[^2682]སྐད་ཅིག་མ་དང་པོ་ལ་འདས་པ་དང་མི་ལྡན་ནོ། །

[Block 4473 [VERSE]]
མཉམ་གཞག་འཕགས་ལམ་གནས་དེ་གཉིས། །
ད་ལྟར་དང་ལྡན་བསམ་གཏན་དང་། །
ཟག་པ་མེད་པའི་སྡོམ་པ་དང་། །
ལྡན་པ་མཉམ་པར་གཞག་པ་དང་། །

[Block 4474]
འཕགས་པའི་ལམ་ལ་སྙོམས་པར་ཞུགས་པ་དེ་དག་ནི་གོ་རིམས་བཞིན་དུ་ད་ལྟར་གྱི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་ལྡན་གྱི་ལངས་པ་དག་ནི་མ་ཡིན་ནོ། །

[Block 4475]
རེ་ཞིག་སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པ་རྣམས་ཀྱི་གཏམ་ནི་དེ་ལྟ་བུའོ།[^2683] །

[Block 4476 [HEADING]]
###### **བར་མ་ལ་གནས་པ།** ^4-2-2-2-2-2-0

[Block 4477]
ཡང་ད་ནི་བར་མ་ལ་གནས་པ་བརྗོད་པར་བྱ་སྟེ། བར་གནས་ལ། ཡོད་ན་དང་པོ་བར་གྱི་དང་། །གང་སྡོམ་པ་ཡང་མ་ཡིན་སྡོམ་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་པ་ལ་གནས་པ་དེ་ནི་བར་མ་ལ་གནས་པ་སྟེ། དེ་ལ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གདོན་མི་ཟ་བར་ཡོད་པ་ནི་མ་ཡིན་གྱི་གང་ལ་འཆལ་པའི་ཚུལ་ཁྲིམས་དང་ཚུལ་ཁྲིམས་ཀྱི་ཡན་ལག་ལ་སོགས་པས་བསྡུས་པ་ཡོད་པ་དེ་ནི་དང་པོ་བར་གྱི་དང་ལྡན་ནོ། །

[Block 4478]
ད་ལྟར་གྱི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་འདས་པ་དང་མ་འོངས་པ་གཉིས་ཀྱི་བར་མ་ཡིན་ནོ། །

[Block 4479]
ཕྱིན་ཆད་དུས་ནི་གཉིས་དང་ངོ་། །སྐད་ཅིག་མ་དང་པོ་ཕྱིན་ཆད་ནི་འདས་པ་དང་ཡང་ལྡན། ད་ལྟར་གྱི་དང་ཡང་ལྡན་ཏེ། མ་བཏང་གི་བར་དུ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4480 [HEADING]]
###### **སྡོམ་མིན་གནས་པ་དགེ་བ་དང་སྡོམ་ལ་གནས་པ་མི་དགེ་བ།** ^4-2-2-2-2-3-0

[Block 4481]
ཅི་རེས་འགའ་སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པ་དགེ་བའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་ལྡན་པར་འགྱུར་བའམ། སྡོམ་པ་ལ་གནས་པ་མི་དགེ་བའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ལ་གནས་པར་འགྱུར་རམ་ཞེ་ན། འགྱུར་རོ། །

[Block 4482]
ནམ་ཞིག་དུས༌[^2684]ཇི་སྲིད་ཅིག་ཏུ་འགྱུར་ཞེ་ན། སྨྲས་པ།

[Block 4483 [VERSE]]
སྡོམ་མིན་གནས་པ་དགེ་བ་དང་། །
སྡོམ་ལ་གནས་པ་མི་དགེ་བའི། །
རྣམ་རིག་མི་ལྡན་ཇི་སྲིད་དུ། །
རབ་དང་ཉོན་མོངས་ཤུགས་ལྡན་པར། །

[Block 4484]
སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པ་ནི་རབ་ཏུ་དང་བའི་ཤུགས་གང་གིས་མཆོད་རྟེན་ལ་ཕྱག་འཚལ་བ་ལ་སོགས་པའི་བྱ་བ་བྱེད་པ་ན་དགེ་བའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྐྱེ་ལ། སྡོམ་པ་ལ་གནས་པ་ནི་ཉོན་མོངས་པའི་ཤུགས་གང་གིས་གསོད་པ་དང་། འཆིང་བ་དང་བརྡེག་པ་ལ་སོགས་པའི་བྱ་བ་བྱེད་པ་ནི་མི་དགེ་བའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྐྱེ་སྟེ། དེ་གཉིས་ཇི་སྲིད་དུ་རྗེས་སུ་འབྲང་བ་དེ་སྲིད་དུ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཡང་རྗེས་སུ་འབྲང་ངོ་། །དེ་ཡང་སྐད་ཅིག་མ་དང་པོ་ལ་ནི་ད་ལྟར་གྱི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཁོ་ན་དང་ལྡན་པར་འགྱུར་ལ། གཞན་དག་ཏུ་ནི་འདས་པ་དང་ཡང་ལྡན་ནོ། །

[Block 4485]
རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་སྐབས་རྫོགས་སོ།། །།
--- END BLOCKS ---
