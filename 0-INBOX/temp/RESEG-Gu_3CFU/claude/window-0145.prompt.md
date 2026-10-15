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
[Block 5076]
འུ་ཤའི་ཁུ་ཚན་ལ་སོགས་པ་དབོ་བ་དང་འཆག་པ་དང་ཡལ་ག་ལ་སོགས་པ་འདྲེན་པ་དང་། དཀྱིལ་འཁོར་དང་སྐྱང་ནུལ་དག་ལ་དེ་དག་གི་བསམ་པ་ཉིད་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་དབོ་བ་ལ་སོགས་པའི་བསམ་པ་ཉིད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5077]
མ་ཉམས་པའི་འདུན་པས་ལྟུང་བ་མེད་པ་ཉིད་དེ་ན་སྨད་པ་ནི་མ་ཡིན་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུ་མདོ་འདི་ཡིན་ནོ། །

[Block 5078]
རྟེན་ཉིད་ཀྱིས༌[^3451]ཡིན་ཏེ་དེ་བས་ན་འདིར་ལྟོས་པས་བསྲེག་པར་བྱ་བ་དང་འཐག་པར་བྱ་བ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིར་ལྟུང་བ་མེད་པར་ཤེས་པའོ། །

[Block 5079]
ཕོངས་པའི་ཚེ་རྩྭ༌[^3452]ཀུ་ཤ་ལ་སོགས་པས་བཅིངས་པ་དེས་མི་ཐར་ན་བཅད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་གི་སྒྲས་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདིའི་རྗེས་སྙེགས༌[^3453]པའི་དོན་དུའོ། །

[Block 5080]
རྩྭ༌[^3454]ཀུ་ཤ་ལ་སོགས་པས་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས་གླེང་གཞིའི་དབང་གིས་རྩྭ༌[^3455]ཀུ་ཤ་རྣམས་ཉིད་ལ་འདི་གསུངས་ཏེ། སེམས་ཅན་གྱི་གྲངས་ལས་གཞན་ཐམས་ཅད་ལ་གཅོད་པར་བྱེད་པ་ལ་རྣམ་པར་གཞག་པ་བྱ་བ་ནི་སོགས་པའི་ཚིག་གོ། །

[Block 5081]
ཕོངས་པའི་ཚེ་ན་ཞེས་བྱ་བ་ནི་ཀུན་ནས་ཉོན་མོངས་པའི་གནས་སྐབས་ཐོབ་པ་ཡོད་པ་ལའོ། །

[Block 5082]
འདིར་གང་གིས༌[^3456]གཅོད་ན༌[^3457]རྗེས་སུ་བསྒྲུབ་པར་གྱུར་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེ་ན། དེའི་ཕྱིར་བཅིངས་པ་ཞེས་བྱ་བ་སྨོས་སོ། །གང་གིས་བཅིངས་པ་ཞེ་ན། དེས༌[^3458]ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་གཅོད་པ་འདི་བཤད་པ་རྫས་གང་ཉིད་ཀྱིས་བཅིངས་པ་རྫས་དེ་ཉིད་བརྗོད་པ་ལ་ལྟུང་བ་འདི་མེད་པ་ཡིན་གྱི་གནས་སྐབས་ཐམས་ཅད་དུ་ནི་མ་ཡིན་ཏེ། འོན་ཀྱང་མི་ཐར་ན་བདག་གམ་གཞན་ལ་འགྲོ་བ་པོ་མེད་པས་སོ། །

[Block 5083]
དུ་མ་ཉིད་ཡིན་ན་དེ་ལས་གཅིག་གིས་སོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་མི་ཐར་ན་ཆོ་ག་འདི་ཡིན་པ་དེ་བས་ན་དུ་མ་ཉིད་དུ་བཅིངས་པ་ལ་དེ་གཅིག་གིས་གཅད་པར༌[^3459]བྱའི་གཞན་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 5084]
ས་བོན་གྱི་ཆོས་མེད་པ་ནི་ཉེས་པ་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མ་སྦས་པ་ཉིད་ཀྱི་ཕྱིར་འདི་ལ་ལྟུང་བར་བྱས་པ་ཉིད་ནི༌[^3460]གང་གིས་སམས་པ༌[^3461]དེའི་དོན་དུ་ས་བོན་གྱི་ཆོས་མེད་པ་ཉིད་འདི་རུང་བ་ལྔ་པོ་རྣམས་གསུངས་པ་གང་ཡིན་པ་དེའི་བསྡུ་བའོ། །

[Block 5085]
བྱིན་ལེན་མ་བྱས་པའི་ཁ་ཟས་ཀྱི་ལྟུང་བ་དང་འབྲེལ་པ༌[^3462]ལས་འདི་དང་པོའི་རུང་བ་ཞེས་བྱ་བ་དོན་འདིར་ཕྲན་ཚེགས་རྣམས་ལས་ས་བོན་མེད་པ་ཉིད་འབྲེལ་པ་ལས་ཞེས་བྱ་བ་ལ་སོགས་པ་བླངས་པ་ཞེས་བྱ་བའི་མཐར་ཐུག་པར་གྲངས་སོ། །

[Block 5086]
སྨན་གྱི་གཞི་ལས་ཡང་དག་པ་ཉིད་དུ་གྲངས་པ་ཞེས༌[^3463]བྱ་བ་ལ་སོགས་པ་སྲིད༌[^3464]པ་ལྡང་བ་ཞེས་བྱ་བའི་མཐར་ཐུག་པར་གྲངས་པ་དང་། སྨན་གྱི་གཞི་ཞུ་བ་ལས་བྱས་པ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་བཟའ་བར་བྱ་ཞེས་བྱ་བའི་མཐར་ཐུག་པར་གྲངས་པ་དང་། ཕྲན་ཚེགས་ལ་སོགས་པ་ལས་ཐ་མི་དད་པ་མ་ཡིན་པ་ཞེས་བྱ་བར༌[^3465]གྲངས་སོ། །

[Block 5087]
མེས་རེག་པ་དང་མཚོན་དང་སེན་མོ་དང་ནེ་ཙོ་དག་གིས་རྨ་ཕྱུང་བ་དང་རྙིངས་པ༌[^3466]དང་ཕྱུང་བ་དང་བཀྲུམ་པ༌[^3467]དང་བཀས་པ་དང་བཅད་པ་ལྟ་བུ་དག་ནི་རུང་བའོ་ཞེས་བྱ་བ་ནི་གཞན་རྣམས་ཀྱིས༌[^3468]རྨ་ཕྱུང་བ་ནི་རྨ་ཕྱུང་བ་མ་ཡིན་པ་མ་ཡིན༌[^3469]ཏེ། དེ་བས་ན་མཚོན་ལ་སོགས་པས་བརྒྱབ་པ༌[^3470]ནི་འདིར་དཔེར་རྟོགས་པར༌[^3471]བྱའོ། །

[Block 5088]
དེ་ལས་གཞན་པ་རྨ་བྱུང་བ་མ་ཡིན་པ་ནི་ཤིང་ཏོག༌[^3472]ལ་སོགས་པ་ལ༌[^3473]སེན་མོ་དང་ནེ་ཙོས་རྨ་ཕྱུང་བ་སྟེ། གྲགས་པ་ཉིད་ཀྱི་ཕྱིར་དང་བརྩལ་བར༌[^3474]བྱ་བ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་དང་གྲགས་པར༌[^3475]བྱ་དཀའ་བ་ཉིད་མ་ཡིན་པའི་ཕྱིར་མ་བྱས་པ་ཇི་ལྟ་བ་བཞིན་དུ་འདི་རྣམས་ལ་དཔེ་ཉིད་ཀྱིས་བསྟན༌[^3476]པའོ། །

[Block 5089]
ཕྱུང་བ་ཞེས་བྱ་བ་ནི་ཕྱུང་བ་སྟེ། འདིར་དེ་ནི་བརྟགས་པ༌[^3477]གཞན་གྱིས་རུང་བར་བྱ་བ་ལ་ལྟོས་མི་དགོས་ཏེ། ཕྱུང་བ་ཉིད་ཁོ་ན་འདིར་རུང་བར་བྱས་པས་ཉིད་ཅེས་བྱ་བ་འདིར་རྟོགས་པར་བྱའོ། །

[Block 5090]
འདི་བཀྲུམ་པར་བྱེད་པ་ནི་བཀྲུམ༌[^3478]པའི་ཚིག་གིས་བཟུང་ངོ་། །བཀས་པ་སྟེ་ཞེས་བྱ་བ་ནི་གས་པར་གྱུར་པ་སྟེ། རང་གས་པ་ཉིད་གང་ཡིན་པ་དེ་ནི་རུང་བ་ཉིད་མ་ཡིན་ཏེ། རྣམ་པར་མི་འགྱུར་བར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 5091]
བཅད་པ་ཞེས་བྱ་བ་ནི་བརྔས་པ་སྟེ། གནས་ལས་བསལ་བའི་དོན་དུ་གཅོད་པ་གང་ཡིན་པ་འདི་ནི་དེའི་དོན་ཏོ།[^3479] །བཟའ་བའི་དོན་དུ་འཐད་པ་བྱས་པ་ཉིད་ལ་རྨ་བྱུང་བ་ནི་འདི་ཡིན་ཏེ། དེ་ནི་སྔར་བཟུང་བ་སྟེ། དེ་ལྟ་བུར་གྱུར་པ་མ་ཡིན་པ་ཞེས་བྱ་བར་གང་གིས་བསམ་པ་དེའི་དོན་དུ་ཚིག་འདིའོ། །

[Block 5092]
རུང་བར་བྱེད་པ་ན་ས་བོན་མ་ཡིན་པ་ཉིད་དུ་གྱུར་གྱི་བར་དུ་ལྟོས་པར་བྱ་བ་མི་དགོས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རུང་བར་བྱེད་པ་ན༌[^3480]ཇི་སྲིད་དུ་ས་བོན་མ་ཡིན་པ་ཉིད་དུ་གྱུར་གྱི་བར་དེ་སྲིད་དུ་འདི་ལ་ལྟོས་པ་འདི་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5093]
དེ་རེག་པའི་མེ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསལ་བའི་དོན་ཉིད་ཤེས་པ་ཡིན་ཏེ་དེ་བས་ན་མདོ་འདི་བྱས་སོ། །

[Block 5094]
འདི་ལ་རླངས་པ་ནི་མེ་མ་ཡིན༌[^3481]ནོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་རུང་བ་ལའོ། །

[Block 5095]
རླངས་པ་ནི་མེ་ཁོ་ན་ཉིད་དེ་རླངས་པས་ཀྱང་མེས་རེག་པ་ལ་རུང་བ་ཉིད་སྐྱེས་པ་ཞེས་བྱ་བ་དེའི་འདི་བྱེད་པའོ། །

[Block 5096]
འདིར་མདོ་དེ་གཉིས་ཀྱི་གཞུང་ནི་དགེ་སློང་དག་ས་བོན་གྱི་རིགས་མ་ཚོས་པ་ཞེས་བྱ་བ་ཡོད་པས་དེའི་ཕྱིར་རླངས་པས་བརླན་པ་དེ་བཟའ་བར་རྗེས་སུ་གནང་གིས༌[^3482]འདི་ལ་འགྱོད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5097]
འབྲས་བུ་དག་མེས་རུང་བར་བྱ་བ་ལ་སྤྱིའི་ཚོམས་ནི་གཙོ་ཆེར༌[^3483]བྱ་བ་ཡང་དག་པའི་གྲངས་ཉིད་དོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་དགེ་སློང་དག་རྒུན་འབྲུམ་མེས་སྤྱིར་རེ་རེ་ནས་རུང་བར་བྱེད་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 5098]
འདིར་སྤྱིའི་ངོ་བོ་གཙོ་བོར༌[^3484]བྱེད་པའི་ཡང་དག་པ་ཉིད་ཀྱི་གྲངས་དང་ལྡན་པ་སྟེ་སྤྱི་ལ་རུང་བ༌[^3485]ཉིད་ཡིན་པར་སྣང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5099]
ཕྱོགས་གཅིག་ནས་ནི་ཕྱིའི༌[^3486]རུང་བར༌[^3487]མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་རུང་བ་དག་བྱས་པ་ཞེས་བྱ་བ་རུང་བ་འདི་ལའོ། །

[Block 5100]
དེ་བས་ན་སྤྱི་ལ་ངོས་ཐམས་ཅད་ལ་མེས་རེག་པར་རིགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5101]
ཕྱོགས་གཉིས་སམ་གསུམ་རྣམས་སུ་རེག་པར་བྱའོ་ཞེས་གསུངས་པ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 5102]
དགེ་སློང་གིས༌[^3488]རུང་བ་དག་བྱས་པ་ཉིད་ནི་བྱས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་བཙུན་པ་རེ་ཞིག་དེ་དག་གིས་ཞུགས་ཀྱིས་ས་མ་སེན་མོས་སམ་མཚོན་གྱིས༌[^3489]ས་བོན་གྱི་རིགས༌[^3490]ལྔ་པོ་དག་རུང་བར་བགྱིད་ན་རུང་བར་བགྱིས་པ་ཞེས་བགྱི་འམ། ཉེ་བ་འཁོར་རུང་བར་བྱས་པ་ཞེས་བྱ་སྟེ། ཉེ་བ་འཁོར་མེས་རུང་བར་བྱས་པ་མ་གཏོགས་པ་ལྷག་མ་རྣམས་ནི་བཟར་རུང་སྟེ་བཟའ་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 5103]
གང་རུང་བར་བྱེད་ན་ས་བོན་གྱི་ཚོགས་འཇོམས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5104]
ཉམས་པར་གྱུར་པའི་རུང་བའི་དབང་དུ་བྱས་ནས་གང་རུང་བར་བྱེད་ན་ཞེས་བྱ་བའི་ཚིག་རིག་པར་བྱའོ། །

[Block 5105]
གང་འདིར་ཉེ་བ་འཁོར་མེས་རུང་བར་བྱས་པ་མ་གཏོགས་པ་ཞེས་གསུངས་པ་དེས་ནི་མེར༌[^3491]རུང་བར་བྱ་བ་མ་གསུངས་པ་ཡིན་ཏེ། འཚེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་མདོ་འདིས༌[^3492]རིག་པར་བྱའོ། །

[Block 5106]
དགེ་སློང་གིས་བཙོས་པའི་དབང་དུ་བྱས་པ་འདིར་བཟའ་བར་བྱ་བ་ཉིད་ལ་རྒྱུ་རྣམ་པར་གནས་པ་ཡིན་ཏེ། གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དོན་འདི་མདོར་བྱས་པའོ། །

[Block 5107]
ས་རུང་བ་མ་ཡིན་པར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རུང་བ་རྣམས་ཀྱིས་བྱས་པ་ཉིད་ནི་བྱས་པ་ཉིད་དོ། །

[Block 5108]
ཞག་བདུན་པ་དང་འཚོ་བའི་བར་བཅང་བ་ཆུ་གྲང་མོས༌[^3493]མ་གཏོར་བར་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། དེར་རུང་བར་བྱ་བ་དང་འབྲེལ་པ་ཡིན་པས༌[^3494]འདིའི་ཚིག་བྱས་པའོ། །

[Block 5109]
རུང་བ་ལ་ནི་འདིར་མ་གཏོར་བ་ཉིད་ཇི་ལྟར་མེ་ལ་སོགས་པས་དེ་བཞིན་དུ་འདི་ལ་ཡང་གང་གི་ཚེ་དེའི༌[^3495]ཉེས་བྱས་ཉིད་ལ་རུང་བ་ཉིད་དེ་བཟའ་བའི་དུས་ཉིད༌[^3496]ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 5110]
འདིར་གཞུང་ནི་བཙུན་པ་གང་ཞིག་ལྟུང་བ་བརྒྱད་པོ༌[^3497]འདི་རྣམས་ཙོ་ཙའི་འབྲས་བུ་ལས་བྱུང་བ་དང་ཆུ་ཤིང་གི་འབྲས་བུ་ལས་བྱུང་བ་དང་རྒྱ་ཤུག་གི་ལས་བྱུང་བ་དང་འབྲ་གོ་ལས་བྱུང་བ་དང་རྩུབ་འགྱུར་ལས་བྱུང་བ་དང་། རྒུན་དང་ཨུ་དུམ་བཱ་ར་ལས་བྱུང་བ་དང་ནྱ་གྲོ་དྷ་ལས་བྱུང་བ་དང་ཁྱབ་གནས་ལས་བྱུང་བ་གང་དག་ལགས་པ་དེ་རྣམས་རྩ་བའི་ཁུ་བ་འམ་སྡོང་བུའི་ཁུ་བ༌[^3498]འམ་འདབ་མའི་ཁུ་བ་འམ་མེ་ཏོག་གི་ཁུ་བ་དང་བསྲེས་ཤིང་འཚལ་ཞིང་སྦྱར་ན་རུང་ངམ། གལ་ཏེ་སྐྱུར་བ༌[^3499]དང་། མྱོས་པར་མི་འགྱུར་བ་དང་། མི་བསྐ་བ་དག་ཡིན་ན་བཏུང༌[^3500]དུ་རུང་ངོ་། །དེ་ལས་ལྷག་པར་ཆུས་བཏབ་པ༌[^3501]དག་ནི་ཞག་བདུན་པ༌[^3502]འམ་འཚོ་བའི་བར་དུ་བཅང་བ་དག་ཡིན་ནོ་ཞེས་གསུངས་པའི་ཚིག་གིས་སོ། །

[Block 5111]
ཐུན་ཚོད་དུ་རུང་བ་ཡང་དེ་མ་ཐག་པའི༌[^3503]མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ་ནི་ཆུ་གྲང་མོས་སོ། །

[Block 5112]
འདི་ལ་གཞན་གྱི་དུས་མ་ཡིན་པ་ལས་མ༌[^3504]བྱས་པ་ལ༌[^3505]བྱས་པ་ཉིད་དོ། །

[Block 5113]
མར་བསྲུབ་པའི་ཚེ་དང་འབྲི་མར་འཚིར་བའི་ཚེ་ན་ཡང་ཆུ་གྲང་མོས་གདབ་དགོས་མོད་གྱི། འོན་ཀྱང་མར་དང་མར་ནག་པོ་དག་གིས༌[^3506]རུང་བར་བྱས་པ་ཉིད་དོ། །

[Block 5114]
ཀུན་སློང་ལ་འདི་དགོས་པས་འདི་དག་གྲུབ་པ་ལ་རུང་བ་འདི་ལ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་བུ་རམ་ཡང་མེས་བསྐོལ་བ་ན་ཆུ་གྲང་མོས་གདབ་པར༌[^3507]བྱ་བ་ཡིན༌[^3508]མོད་ཀྱི། དེའི་ཚེ་ན་ཆུས༌[^3509]བཏབ་པ་དེས༌[^3510]རུང་བར་བྱས་པ་ཉིད་དུ་མི་ཆུད་དོ། །

[Block 5115]
ཞག་བདུན་པ་ལ་མེས་རུང་བར༌[^3511]བྱ་བ་མི་སྲིད་དེ་འདིར་གཞུང་ནི་དེ་ལ་ཉམས་སུ་
--- END BLOCKS ---
