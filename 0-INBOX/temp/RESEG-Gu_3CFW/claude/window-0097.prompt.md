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
[Block 3396]
རྩོད་པ་ཐམས་ཅད་ལ་འདི་རུང་བ་ཉིད་ཅེས་བྱ་བ་ཐམས་ཅད་ཀྱི་དབང་དུ་བྱས་ནས་ཉེ་བར་ཞི་བར༌[^3464]སྦྱར་བའོ། །

[Block 3397]
རྩོད་པའི་གཞིའོ།། །།

[Block 3398]
ཞི་བ་ཐམས་ཅད་ནི་བྱ་བའི་ཕྱིར་རྩོད་པར་འཇུག་གོ་ཞེས་བྱ་བ་ནི་རྩོད་པ་ཞི་བར་བྱ་བ་བདུན་པོ་ཐམས་ཅད་ནི་བྱ་བའི་ཕྱིར་རྩོད་པར་འཇུག་གོ། །

[Block 3399]
གསོལ་བ་ལ་སོགས་པའི༌[^3465]ལས་ལ༌[^3466]མཐུན་པ་མི་སྦྱིན་པ་ནི༌[^3467]བྱ་བའི་ཕྱིར་རྩོད་པ་ཡིན་པས་སྤོང་བ་ཉིད་ལ་བརྟེན་ཏེ་མཐུན་པ་མི་སྦྱིན་པ་དང་བཅས་པ་ཉིད་ཀྱང་ངོ་། །རྣམ་པར་ངེས་པར་བྱ་བ་སྤོང་བ་དང་ལྟུང་བ་དང་བཅས་པ་འདི་གཉིས་དང་ལྟ་བ་ངན་པ་ཉིད་ཀྱིས་ཀྱང་རྣམ་པར་ངེས་པར་བྱ་བ་ནི་རྒྱུའི་སྒོ་ནས་ཏེ། རྒྱུ་གང་གིས་རྩོད་པ་ཞི་བར་བྱ་བ་བདུན་པོ་དག་འཇུག་པར་འགྱུར་བའི་རྒྱུ་དེ་ནི་བྱ་བའི་ཕྱིར་རྩོད་པ་ལ་ཡོད་དེ་འདི་ལྟར་སྤོང་བ་ལ་སོགས་པ་ནི་མཐུན་པ་མི་སྦྱིན་པའི་རྒྱུ་ཡིན་པ་དེའི་ཕྱིར་རྩོད་པའི་མཐུན་པ་མི་སྦྱིན་པ་ཞེས་བྱ་བ་གང་ཡིན་པ་དེའི་སྒོ་ནས་འདིར་ཞི་བར་བྱ་བ་ཐམས་ཅད་དུ་འཇུག་གོ། །

[Block 3400]
གསོལ་བ་ལ་སོགས་པའི་ལས་ལ་མཐུན་པ་མི་སྦྱིན་པ་ནི་བྱ་བའི་ཕྱིར་རྩོད་པ་ཡིན་པས་དེ་ལ་ཇི་ལྟར་སྤོང་བ་ཉིད་ལ་བརྟེན་ཏེ་མཐུན་པ་མི་སྦྱིན་པ་དེ་བཞིན་དུ་མི་གདམས་པའི་ཕྱིར་རྩོད་པ་ཞི་བར་བྱ་བའི་དྲན་པ་དང་མ་སྨྱོས་པས༌[^3468]འདུལ་བ་གཉིས་ཀྱང་འདིར་འཇུག་གོ། །

[Block 3401]
ཇི་ལྟར་ལྟུང་བ་དང་བཅས་པ་ཉིད་ཀྱིས་དེ་བཞིན་དུ་ལྟུང་བའི་ཕྱིར་རྩོད་པ་ཞི་བར་བྱེད་པ་ཁས་བླང་བའི་བྱ་བ་དང་། མངོན་སུམ་གྱིས་འདུལ་བ་དག་དང་། རྩྭ༌[^3469]བཀྲམ་པ་ལྟ་བུ་དག་ཀྱང་འཇུག་གོ། །

[Block 3402]
ཁས་ལེན་ཅིང་ཁྱད་དུ་གསོད་པ་ལ་དེའི་ངོ་བོ་ཉིད་ཚོལ་བ་དང་མཐུན་པ་ཡང་ངོ་། །ཇི་ལྟར་རྣམ་པར་ངེས་པར་བྱ་བ་སྤོང་བ་དང་ལྟུང་བ་དང་བཅས་པ༌[^3470]འདི་གཉིས་ཀྱི་མཐུན་པ་མི་སྦྱིན་པ་དེ་བཞིན་དུ་འགྱེད་པའི་ཕྱིར་རྩོད་པ་ཉེ་བར་ཞི་བར་བྱེད་པའི་གང་མང་བ་བསྩལ༌[^3471]བ་དང་མངོན་སུམ་གྱིས་འདུལ་བ་ཡང་འདིར་འཇུག་གོ། །

[Block 3403]
འདིར་གཞུང་ནི་བཙུན་པ་བཅོམ་ལྡན་འདས་ཀྱིས་རྩོད་པ་བཞི་པོ་གང་དག་གསུངས་པ་དང་རྩོད་པ་ཞི་བ་བདུན་པོ་གང་དག་གསུངས་པ་དེ་དག་ལ་བཙུན་པ་དགེ་སློང་གིས༌[^3472]རྩོད་པ་བཞི་པོ་དག་རྩོད་པ་ཞི་བར་བགྱིད་པ་བདུན་པོ་གང་ཡང་རུང་བས་ཉེ་བར་ཞི་བར་བགྱིད་པ་དང་ཉེ་བར་ཞི་བར་བྱར་རུང་ངམ། ཉེ་བ༌[^3473]འཁོར་ཞི་བར་བྱ་བའི་ཕྱིར་རྩོད་པ་མ་གཏོགས་པ་མི་རུང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3404]
ཁ་སྐོང་བར་འོས་པ་མ་ཡིན་པ་ནི་དགེ་འདུན་གྱི་ཐ་སྙད་ལ་ཚོགས་པར་དབྱུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ་རྫོགས་པ་དང་། ཉམས་པ་ལ་སོགས་པ་གང་དགེ་འདུན་གྱི་ཁ་སྐོང་བར་འོས་པ་མ་ཡིན་པ་དེ་ནི་གཟུ་བོ་ལ་སོགས་པ་དགེ་འདུན་གྱི་ཐ་སྙད་ལ་ཡང་ཚོགས་པར་དབྱུང་བ་ཉིད་མ་ཡིན་པའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3405]
གཞན་གྱི་དག་ལ་ནི་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པ་རྣམས་ཀྱི་དབང་དུ་བྱའོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ་རྫོགས་པ་དགེ་འདུན་ལ་སོགས་པ་གཞན་གྱི་རྩོད་པ་དག་ལ་ནི་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པ་རྣམས་ཀྱི་དབང་དུ་བྱ་སྟེ་དེ་དག་གི༌[^3474]དེ་ཉེ་བར་ཞི་བར་བྱའོ། །

[Block 3406]
བུད་མེད་རྣམས་ཀྱི་ནི་སྐྱེས་པས་རིགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བུད་མེད་རྣམས་ཀྱི་རྩོད་པ་གང་ཡིན་པ་དེ་ནི་དེ་ཉིད་དུ་ཉེ་བར་ཞི་བར་བྱ་བའི་རིགས་པ་ཉིད་ཡིན་ནོ། །

[Block 3407]
འདིར་གཞུང་ནི་དགེ་སློང་རྣམས་ཀྱི་རྩོད་པ་གང་ཡིན་པ་དེ་དག་དགེ་སློང་མ་རྣམས་ཀྱིས་སྤང་དུ་རུང་ངམ་ཉེ་བ༌[^3475]འཁོར་མི་རུང་སྟེ། དགེ་སློང་རྣམས་ཀྱི་རྩོད་པ་ནི་དགེ་སློང་རྣམས་ཀྱིས་ཉེ་བར་ཞི་བར་བྱའོ། །

[Block 3408]
དེ་བཞིན་དུ་དགེ་སློང་མ་རྣམས་ཀྱི༌[^3476]རྩོད་པ་ཡང་དགེ་སློང་རྣམས་ཀྱིས་ཉེ་བར་ཞི་བར་བྱའོ། །

[Block 3409]
དེ་བཞིན་དུ་དགེ་སློབ་མ་རྣམས་དང་། དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་རྣམས་ཀྱི་རྩོད་པ་ཡང་དགེ་སློང་རྣམས་ཀྱིས་ཉེ་བར་ཞི་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3410]
སྲོག་གམ་བསྙེན་པར་རྫོགས་པ་ལས་ཉམས་ན་ཉེ་བར་ཞི་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྲོག་ལས་ཉམས་སམ་བསྙེན་པར་རྫོགས་པ་ལས་ཉམས་ན་རྩོད་པ་ཉེ་བར་ཞི་བ་ཉིད་ཡིན་པའོ། །

[Block 3411]
སྤང་བ༌[^3477]ཉིད་ནས་གཞན་གྱི་ཕྱོགས་ཉིད་ཀྱི་བར་དུ་གྱུར་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་བར་དུའི་སྒྲ་བྲི་བར་བྱའོ། །

[Block 3412]
སྤང་བར་བྱ་བ་ཉིད་ནས་ཕྱོགས་ནས་ཕྱོགས་མ་ཡིན་པ་ཐ་དད་པར་གནས་པའི་བར་དུ་གྱུར་ན་དེ་དག་ཐམས་ཅད་ལ་ཡང་ལྟུང་བ་དང་རྩོད་པ༌[^3478]ཉེ་བར་ཞི་བ་ཉིད་ཡིན་པའོ། །

[Block 3413]
དགེ་འདུན་དུ་གྱུར་པ་དང་འབྲེལ་པ་དག་ལ་འཁྲུག་ལོང་གི་རྩོད་པ་དག་གིས་རྣམ་པར་གཞག་པའི་ལྟུང་བ་ཉིད་ནི་དགེ་འདུན་དུ་གྱུར་པ་གསལ་བ་ཉིད་དོ། །

[Block 3414]
གཞན་དུ་སོང༌[^3479]ངམ་ནད་ཀྱི་རྣམ་པས་ཡུན་རིང་པོར་བཏབ་ན་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་རྩོད་པ་ཉེ་བར་ཞི་བ་ཉིད་ཡིན་པའོ། །

[Block 3415]
གང་ཞིག་སྲོག་ལས་འདས་པ་ནས་ནད་ཀྱི་རྣམ་པས༌[^3480]ཡུན་རིང་པོར༌[^3481]བཏབ་པའི་བར་དུ་གྱུར་ན་རྩོད་པ་ཉེ་བར་ཞི་བ་ཉིད་ཡིན་ནོ།[^3482] །དེའི་ཕྱིར། དོན་སྦྱིན་པར་བྱེད་པའམ་མངོན་པར་བརྩོན་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་དོན་སྦྱིན་པར་བྱེད་པ་ནི་གླེང་བའོ།[^3483] །འདིར་ཉམས་པ་ལ་སོགས་པའི་གཞུང་ནི་བཙུན་པ་རྩོད་པ་བཞི་པོ་དག་ལས་རྩོད་པ་གང་ཡང་རུང་བ་བྱུང་བ་རྩོད་པ་ཞི་བར་བགྱིད་པའི་ཆོས་བདུན་པོ་དག་ལས་གང་ཡང་རུང་བར༌[^3484]ཉེ་བར་ཞི་བར་མི་འགྱིད་ཅིང་། ཉེ་བར་ཞི་བར་ཡང་བརྗོད་པར་བགྱི་བ་མཆིས་སམ། ཡོད་དེ་སྦྱིན་པར་བྱེད་པའི་དགེ་སློང་དུས་བྱེད་དམ་བྱིན་པའི་དགེ་སློང་དུས་བྱེད་དམ་དགེ་སློང་སྦྱིན་པར་བྱེད་པའི་དགེ་སློང་ཁྱིམ་པ་ཉིད་དུ་དམ་འཆའ་འམ། །དགེ་ཚུལ་ཉིད་དམ་དགེ་སློང་མ་སུན་ཕྱུང་བ་ཉིད་དམ། རྐུ་ཐབས་སུ་གནས་པ་ཉིད་དམ་མ་ནིང་ཉིད་དམ། མུ་སྟེགས་ཅན་ཞུགས་པ་ཉིད་དམ་མ་བསད་པ་ཉིད་དམ། ཕ་བསད་པ་ཉིད་དམ། དགྲ་བཅོམ་པ་བསད་པ་ཉིད་དམ། དགེ་འདུན་གྱི་དབྱེན་བྱས་པ་ཉིད་དམ། དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བ་ཉིད་དམ། གནས་པར་མི་བྱ་བ་ཉིད་དམ། ཐ་དད་དུ་གནས་པ་ཉིད་དུ་དམ་འཆའ་བར་བྱེད་དམ། དེ་བཞིན་དུ་བྱིན་པའི་དགེ་སློང་དེ་དག་ཏུ་དམ་འཆའ་བར་བྱེད་དམ། སྦྱིན་པར་བྱེད་པའི་དགེ་སློང་ནད་ཀྱི༌[^3485]རྣམ་པས་ཡུན་རིང་དུ་ཐེབས་སམ་གཞན་དུ་སོང་ངམ། དེ་བཞིན་དུ་བྱིན་པའི་དགེ་སློང་དེ་ལྟར་གྱུར་ན་རྩོད་པ་དེ་ཉེ་བར་ཞི་བར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3416]
རྩོད་པའི་གཞི་ཞུ་བའི་སྐབས་སོ། །

[Block 3417]
རྩོད་པའི་གཞི་རྫོགས་སོ།། །།

[Block 3418 [HEADING]]
## གནས་མལ་གྱི་གཞི། ^12-0

[Block 3419]
སོ་སོར་ཐར་པའི་སྡོམ་པས་མཆོག་ལ་རབ་ཏུ་བྱུང་བས་ཕྱག་བྱའོ་ཞེས་བྱ་བ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པས་མཆོག་ཏུ་གྱུར་པ་དགེ་སློང་གང་ཡིན་པ་དེ་ལ་རབ་ཏུ་བྱུང་བས་ཕྱག་བྱའོ། །

[Block 3420]
དགེ་ཚུལ་གྱིས་དགེ་སློང་ལ་ཕྱག་བྱའོ། །

[Block 3421]
དགེ་ཚུལ་མས་དགེ་སློབ༌[^3486]མ་ལ་ཕྱག་བྱའོ། །

[Block 3422]
དགེ་སློབ་མས་དགེ་སློང་མ་ལ་ཕྱག་བྱའོ་ཞེས་བྱ་བ་དེ་ལ་དེ་བྱེད་པའོ། །

[Block 3423]
མཉམ་ན་རྒན་པ་ལའོ་ཞེས་བྱ་བ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པས་མཉམ་པ་ཉིད་ན་སོ་སོར་ཐར་པའི་སྡོམ་པ་དེས་རྒན་པ་དེ་ལ་གཞོན་པས་ཕྱག་བྱའི་ན་ཚོད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 3424]
བསྙེན་པར་རྫོགས་པའི་སྡོམ་པ་སྔར་བླངས་པ་ལ་ཕྱིས༌[^3487]བླངས་པས་ཕྱག་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3425]
དང་པོར་བསྙེན་པར་རྫོགས་ཟིན་པ་ལ་བསྙེན་པར་རྫོགས་པས་ཕྱག་བྱའོ། །

[Block 3426]
དགེ་སློང་གིས་དགེ་སློང་ལ་ཕྱག་བྱའོ། །

[Block 3427]
དགེ་སློང་མས་དགེ་སློང་མ་ལ་ཕྱག་བྱའོ། །

[Block 3428]
དང་པོར་དགེ་སློང་མའི་སྡོམ་པ་དང་ལྡན་ཟིན་པ་ལ་དགེ་སློང་མས་ཕྱག་བྱའོ། །

[Block 3429]
དང་པོར་རབ་ཏུ་བྱུང་བའི་སྡོམ་པ་དང༌[^3488]ལྡན༌[^3489]ཟིན་པ་ལ་དགེ་སློང་མས་ཕྱག་བྱའོ། །

[Block 3430]
དང་པོར་རབ་ཏུ་བྱུང་བའི་སྡོམ་པ་དང་ལྡན་པར་གྱུར་ཟིན་པའི་དགེ་སློང༌[^3490]ལ་དགེ་ཚུལ་གྱིས༌[^3491]ཕྱག་བྱའོ། །

[Block 3431]
དགེ་ཚུལ་མས་ཀྱང་དགེ་ཚུལ་མ་ལ་ཕྱག་བྱའོ་ཞེས༌[^3492]གསུངས་པ་དེ་བས་ན་དེ་ལ་དེ༌[^3493]བྱེད་པའོ། །

[Block 3432]
མདོ་སྔ་མས་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པས་མཆོག་ལ་རབ་ཏུ་བྱུང་བས༌[^3494]ཕྱག་བྱའོ་ཞེས་བསྟན་པ་ལ་དགེ་ཚུལ་ཕས་དགེ་སློབ་མ་དང་དགེ་སློང་མ་ལ་ཕྱག༌[^3495]བྱ་བར་ཐལ་བར་འགྱུར་བ་དང་། མདོ་འདིས་ནི་མཉམ་ན་རྒན་པ་ལའོ་ཞེས་བྱ་སྟན༌[^3496]པས་དགེ་སློང་དང་དགེ་སློང་མ་ཡང་སོ་སོར་ཐར་པའི་སྡོམ་པས་མཉམ་པ་ཡིན་པས། དགེ་སློང་མ་ལ་དགེ་སློང་གིས་ཕྱག་བྱ་བར་ཐལ་བར་འགྱུར་བ་དང་། དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་ཡང་སོ་སོར་ཐར་པའི་སྡོམ་པས་མཉམ་པ་ཡིན་པས་དགེ་ཚུལ་མ་རྒན་པ་ལ་དགེ་ཚུལ་གྱིས་ཕྱག་བྱ་བར༌[^3497]ཐལ་བར་འགྱུར་བས༌[^3498]དེ་བསལ་བའི་ཕྱིར་མདོ་དེ་གཉིས་ཀྱི་བྱེ་བྲག་བསྟན་པར་བྱ་སྟེ། དེའི་ཕྱིར། མཚན་ཐ་མི་དད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཚན་མཐུན་པ་དག་ལ་ཆོ་ག་འདི་ཡིན་གྱི་མཚན་མི་མཐུན་པ་དག་གི་ནི་མ་ཡིན་ནོ། །

[Block 3433]
ཇི་ལྟར་སྐྱེས་པས་བུད་མེད་ལ་ཕྱག་མི་བྱ་བ་དེ་བཞིན་དུ་བུད་མེད་ཀྱིས་ཀྱང་སྐྱེས་པ་ལ་ཕྱག་མི་བྱ་བར་ཐར་བར་འགྱུར་བ་དེ་དམིགས་ཀྱིས་བསལ་བའི་ཕྱིར། སྐྱེས་པ་མི་དམན་པ་ལ་བུད་མེད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་སོ་སོར་ཐར་པའི་སྡོམ་པས་བུད་མེད་པས་མི་དམན་ན་གསར་བུ་ལ་ཡང་བུད་མེད་ཀྱིས་ཕྱག་བྱ་ན་དུས་མཉམ་པའམ་རྒན་པ་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3434]
ཆོ་ག་དེ་དག་ཐམས་ཅད་ཀྱི་དམིགས་ཀྱིས་བསལ་བའི༌[^3499]ཕྱིར། ས་གཞན་ན་གནས་པ་དང་ཉམས་པ་དང་དགེ་སློང་མ༌[^3500]སུན་ཕྱུང་བ་དང་། ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་དང་། ཐ་དད་པར་གནས་པ་དང་། མཚམས་མེད་པ༌[^3501]བྱས་པ་དང་། ཉལ་བ་དང་སྙོམས་པར་ཞུགས་པ་དང་བྲེལ་བ༌[^3502]དང་སེམས་གཞན་དུ་སོང་བ་དང་རྒྱབ་ཀྱིས༌[^3503]ཕྱོགས་པ་དང་ཁྱིམ་གཞན་ན་འདུག་པ་དང་ཟས་ཀྱི་གྲལ༌[^3504]ན་འདུག་པ་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ས་གཞན་ན་གནས་པ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་བསླབ་པ་བྱིན་པ་དང་། དེའི་ངོ་བོ་ཉིད་ཚོལ་བ་དང་མཐུན་པ་སྦྱིན་པ་ལ་སོགས་པའོ། །

[Block 3435]
ཉམས་པ་ཞེས་བྱ་བ་ནི་གནས་པར་མི་བྱ་བའོ། །
--- END BLOCKS ---
