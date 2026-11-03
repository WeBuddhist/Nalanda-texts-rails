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
[Block 4411]
དེ་བས་ན་འདི་དང་མདོ་ཕྱི་མ་དང་ཡང་དག་པར་བསྟན་པའོ། །

[Block 4412]
དབྱངས་ཀྱིས་ཆོས་སྨྲ་བར་བྱའོ། །

[Block 4413]
ལངས་ནས་རྣམ་པར་དབྱེ་བར་བྱའོ། །

[Block 4414]
[^3078]དོན་བསྡུས་ཏེ་བརྗོད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 4415]
ཆོས་ལ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ༌[^3079]ལ་སོགས་པ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 4416]
གལ་གཟུང་བ་དང་གཞུང་གཟུགས་པར་ཡང་ངོ་ཞེས་བྱ་བ་ལ་གང་ཞིག་ཅེ་ན། མདོ་སྡེ་ལ་སོགས་པའི་ཆོས་ཀྱིའོ། །

[Block 4417]
ཡི་གེ་དང་དོན་དེ་ནི་རིགས་པ་མ་ཡིན་ཏེ། དེ་ནི་འདི་ལྟར་བརྗོད་པར་བྱ་སྟེ། དེ་ཡང་གཞི་འདིས་ཆོ་ག་རྟོགས་པར་བྱའོ་ཞེས་བྱ་བ་རྣམ་པར་འབྱེད་པ་ལས་སོ། །

[Block 4418]
གལ་གཟུང་བ་དང་གཞུང་གཟུགས་པ་དེ་ལྟར་ཡི་དམ་བྱེད་པའོ། །

[Block 4419]
[^3080]དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་སྨྱུག་མའི་ཐུར་མ་སྐུད་པ་ལ་བརྒྱུས་པ་སྤོ་བས་ཉི་མ་བགྲང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། གླེང་གཞི་དག་ལས་འདི་དང་པོར་བྱས་པའི་དྲང་བར་བྱའོ་ཞེས་བྱ་བའི་བར༌[^3081]དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 4420]
དགེ་སྐོས་ཀྱིས་དེ་ལ་བརྟགས་ཏེ་དགེ་འདུན་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་གནས་བརྟན་གྱི་ལས་སོ། །

[Block 4421]
བྱེ་བྲག་ཏུ་མ་བྱས་པས་ནི་ཞུ་བར་བྱ་བ་མ་ཡིན་ཏེ། འོན་ཀྱང་བྱེ་བྲག་ཏུ་བྱས་པའི་འོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4422]
གང་གིས་བྱེ་བྲག་ཏུ་བྱས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ངོའི༌[^3082]དབྱེ་བས་སོ་ཞེས་བྱ་བ་སྨོས༌[^3083]ཏེ། ཟླ་བ་ཡར་གྱི་ངོ་དང་མར་གྱི་ངོའི་དབྱེ་བ་དེས་སོ། །

[Block 4423]
གཙུག་ལག་ཁང་གི༌[^3084]བདག་པོ་དང་ལྷའི་ཚིགས་སུ་བཅད་པ་འདོན་པར་དགེ་སློང་རྣམས་ལ་བསྐུལ་བའི་ཚིག་བྱའོ་ཞེས་བྱ་བ་ལ་གང་གི་ཚེ་ན་ཞེ་ན། དེའི་ཕྱིར་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉི་མ་བརྗོད་པའི་ཞེས་བྱ་བ་སྐབས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 4424]
སྡུག་བསྔལ་རིགས་པའི་ངོ་བོ་ཚིག་གིས་མངོན་པར་འདུ་བྱས་པ་ཞེས་བྱ་བ་གང་ཞིག་འདིར་རིགས་པའི་ངོ་བོའི་ཚིག་མངོན་པར་འདོད་པ་དེ་བསྟན་པར་བྱ་སྟེ། དེའི་ཕྱིར་དེང་ནི་ཡར་གྱི་ངོའི་ཚེས་གཅིག་ལགས་ཏེ། གཙུག་ལག་ཁང་གི་བདག་པོ་དང་། གཙུག་ལག་ཁང་གི་ལྷ་རྣམས་ཀྱི་སླད་དུ་ཚིགས་སུ་བཅད་པ་རེ་རེ་བཀླག་ཏུ་གསོལ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཀླག་ཏུ་གསོལ་ཞེས་བྱ་བའི་སྒྲས་ནི་འདི་སྐད་ཅེས་བྱ་བའི་དོན་ཅན་ནོ། །

[Block 4425]
གཙུག་ལག་ཁང་གི་བདག་པོས་སྤྱན་འདྲེན་པའི་ཚིག་ཀྱང་བརྗོད་པར་བྱའོ། ། ཇི་སྐད་དུ་ཞེ་ན། དེའི་ཕྱིར་ཡོན་བདག་མིང་འདི་ཞེས་བགྱིས་པས༌[^3085]སང་དགེ་འདུན་བཤོས་ལ་སྤྱན་འདྲེན་ན། བཙུན་པ་རྣམས་ཀྱིས་དེ་ལ་དགེ་ལེགས་ཀྱི་ཡིད་དག་གིས་སོ་སོ་ནས་ཐུགས་བརྩེ་བར་མཛད་དུ་གསོལ་ཞེས་བྱ་བས་སོ། །

[Block 4426]
ཉིན་ཞག་གཅིག་གིས་མི་ཆོག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། གང་གི་ཚེ་ན་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དུས་ཚིགས་རྣམས་ཀྱི་ཟླ་བ་ཕྱེད་ལུས་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོ་སྦྱོང་གསུམ་པ་ལ་འདིས་ནི་ཚེས་བཅུ་བཞི་པ་ཉིད་བྱས་པར་རིག་པར་བྱའོ། །

[Block 4427]
ཟླ་བ་ཤོལ་དོར་བ་ནི་རྒྱལ་པོའི་རྗེས་སུ་འབྲང་བས་སོ། །

[Block 4428]
རྒྱུ་སྐར་ནི་སྐར་མཁན་གྱི་རྗེས་སུ་འབྲང་བས་ཤེས་པར་བྱའོ། །

[Block 4429]
འདི་ལ་དགོས་པ་ནི་ཐ་སྙད་ལ་མཁས་པར་བྱ་བའོ༌[^3086]ཞེས་བྱ་བ་ལ་ཚེས་གྲངས་བརྗོད་པར་བྱ་བ་ལ་སོགས་པ་འདི་ལ་དགོས་པ་ནི་འཇིག་རྟེན་པའི་ཐ་སྙད་ལ་མཁས་པར་བྱ་བ་དང་། ཚེས་འདས་པ་སེམས་ལ་གཞག་པར་བྱ་བ་དང་། གསོ་སྦྱོང་གི་ཉི་མ་ཡོངས་སུ་ཤེས་པར་བྱ་བ་ཡིན་ནོ།[^3087] །མ་བརྟགས་ཤིང་གསོ་སྦྱོང་ལ་མ་བསྡད་པར་འདི་ནི་སྤོང་བ་ཞིག་གོ་སྙམ་ནས་མཚམས་གཅད་པར༌[^3088]མི་བྱའོ་ཞེས་བྱ་བ་ནི། བརྟག་ཅིང་མཚམས་བཅད་དམ་འོན་ཏེ་མ་བཅད༌[^3089]ཅེས་དེ་ལྟར་བརྟག་ཅིང་གསོ་སྦྱོང་གི་ཉི་མ་ལ་མ་བབ་ཀྱི་བར་དུ་བསྡད་དེ་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4430]
བཅད་པ་ཉིད་དུ་ཤེས་པ་ནི་མི་ཆགས་པའི་ཡན་ལག་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། བག་ཡངས་སུ་མ་བྱས་པར་གཅད་པ༌[^3090]གཞན་ནི༌[^3091]མི་འཆགས་པ༌[^3092]ཁོ་ནའོ་ཞེས་གང་བསྟན་པ་དེ་ལ་ཤེས་པ་དེ་ཡན་ལག་མ་ཡིན་ཏེ། འདི་ལྟར་མཚམས་བཅད་ཟིན་པ་ཡོད་ན་བག་ཡངས་སུ་གྲགས་པ་ཞེས་བྱ་བ་མི་ཤེས་པ་ཉིད་ལ་ཡང་དེ་རིག་པར༌[^3093]བྱའོ། །

[Block 4431]
དེ་མེད་པ་ཉིད་ཀྱིས་ཀྱང་བག་ཡངས་སུ་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། ལས་གང་ཞིག་བག་ཡངས་སུ༌[^3094]ཉིད་ཀྱིས་རྩ་བའི་གཞི་ལས་སྨོས་པ། དེ་ལ༌[^3095]ལྟོས་པ་ཀྱང་གི་སྒྲ་འདི་ཡིན་ནོ། །

[Block 4432]
དེའི་སྒྲས་ནི་མཚམས་དགྲོལ་བ་ལ་ལྟོས་པའམ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་དོན་གྱིས་ཉེ་བར་གནས་པ་རྣམས་ཀྱང་ཉེ་བར་བཟུང་བའོ། །

[Block 4433]
གང་དག་གི་མཚམས་དེའི་ནང་ན་གཅིག་ཀྱང་མ་ལུས་པ་ཞེས་བྱ་བ་ནི་མཚམས་དེ་མེད་པའོ། །

[Block 4434]
དེའི་དངོས་པོ་ནི་དེ་ཉིད་མེད་པའོ། །

[Block 4435]
དེ་བས་ཀྱང་མཚམས་ཀྱི་བག་ཡངས་སུ་བྱ་བའོ། །

[Block 4436]
ལས་རྣམ་པ་ལྔས་དེ་མེད་པ་ཉིད་ཀྱིས་ཀྱང་བག་ཡངས་སུ་སྒྲུབ་པ་བྱེད་པ་གཅིག་པུར་མ་ཟད་ཀྱི། དགེ་འདུན་ཐམས་ཅད་དོང་བ་ཐམས་ཅད་མཚན་པ་དང་ཞིང་མ་ཡིན་པ་ཉིད་ལྟུང་བ་ཐོབ་པ་དང་རྣམ་པར་འཁྲུགས་པར་གྱུར་པ་དང་ཤི་བས་སོ། །

[Block 4437]
གནས་སུ་གཞག་སྟེ་སེམས་ཀྱིས་དཀྱིལ་འཁོར་པ་གང་གིས་བྱིན་གྱིས་བརླབ་པ་དེ་བས་ན། གནས་ཁང་དེར་དེ་མེད་པ་ཉིད་ཀྱིས་ཀྱང་འདི་ལ་དེ་མེད་པ་དེར༌[^3096]རང་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 4438]
རུང་པའི་ཁང་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་མེད་པ་ཉིད་ཀྱིས་ཀྱང་བག་ཡངས་སུ་འགྱུར་རོ་ཞེས་བྱ་བ་སྟེ། མདོ་སྔ་མ་ལས་ཉེ་བར་གཞག་པ་ལ་ཀྱང་གི༌[^3097]སྒྲས་ནི་འདིར་བསྡུས་པ༌[^3098]ལ་རིག་པར་བྱའོ། །

[Block 4439]
ལས་དང་དེ་མེད་པ་ཉིད་འདིས་ཀྱང་ཞེས་བྱ་བའོ། །

[Block 4440]
མཚམས་སུ་མཚམས་ཀྱིས་བསྐོར་དུ་མི་རུང་ངོ་ཞེས་བྱ་བ་ནི། མ་གྲགས་པའི་ཚིག་འདི༌[^3099]ལས་བྱས་སུ་ཟིན་ཀྱང་མ་བྱས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 4441]
དཀྱིལ་འཁོར་བ་དང་དགེ་སློང་མའི་དབྱར་ཁོང༌[^3100]དག་དང་ཁྲོན་པ་དག་ལ་ནི་རུང་ངོ་ཞེས་བྱ་བ་ལ། འདི་དག་ནི་ཡུལ་གྱི་བདུན་པའོ། །

[Block 4442]
ཡུལ་འདི་ལ་མཚམས་གང་ཞིག་དེ་ལ་གང་ཞིག་བསྐོར༌[^3101]དུ་རུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4443]
ཤིང་ལྗོན་པ་གཅིག་ལ་མཚམས་བཞི་མན་ཆད་ཀྱིས་མུ་ཐུག་དུ་མ་རྣམ་པར་གནས་སོ་ཞེས་བྱ་བ་ལ། མཚམས་བཞི་མན་ཆད་ཀྱི་ཞེས་བྱ་བ་ནི་གསལ་བ་ཉིད་དུ་ཁས་བླངས་ནས་འདི་སྨོས་སོ། །

[Block 4444]
རྣམ་པ་བཞི༌[^3102]ཤིང་ལྗོན་པའི་རྣམ་པར་དབྱེ་བ་ཤིན་ཏུ་ཡང་གསལ་བ་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་ཡང་མང་པོའི་མཚམས་རྣམས་ལ་རྣམ་པར་གནས་པ་ཉིད་ཡོད་པའོ། །

[Block 4445]
འདི་ལ་ཐ་སྙད་དུ་རུང་བ་མཚན་མ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་མཚམས་ལའོ། །

[Block 4446]
རྫུ་འཕྲུལ་དང་སྒྱུ་མ་བྱས་པ་དག་ཀྱང་དེ་ལྟར་གྱུར་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། ཐ་སྙད་མ་ཡིན་པ་ཉིད་དུ་བྱས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4447]
ཟླ་བ་དང་། ཉི་མ་དང་། སྐར་མའི་འོད་དང་དབའ་ཀློང་གི་རླབས་དག་ཀྱང་མི་བརྟན་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། བརྟན་པ་ཞེས་བྱ་བ་འདི་ཉིད་ཀྱིས་འདི་རྣམས༌[^3103]མ་ཡིན་པར༌[^3104]དགག་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4448]
མཚམས་དང་མ་འབྱར་བ་ལ་དེའི་མཚན་མ་ཉིད་མ་ཡིན་ནོ། །

[Block 4449]
དེ་ལྟ་བས་ན་འདིར་འོད་ཟེར་རྣམས་མངོན་པར་བརྟེན་པ་ཟླ་བ་ལ་སོགས་པ་ལ༌[^3105]ཡང་མ་ཡིན་ཏེ། འདིར་དོགས་པའི་སྐབས་མེད་པའི་ཕྱིར་རོ། །

[Block 4450]
འདིར་དེའི་ཁྱད་པར་གྱི་ངོ་བོས་ཟླ་བ་ལ་སོགས་པ་ཉེ་བར་བཟུང་བའོ། །
--- END BLOCKS ---
