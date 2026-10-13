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
དེ་ལྟར་ཉོན་མོངས་པ་རྣམ་པ་དགུ་པོ་དེ་དག་ཐམས་ཅད་དུ།

[Block 3397 [VERSE]]
འབྲས་གནས་བསྒོམ་སྤང་བྱ་མ་ཟད། །
རེ་ལྟར༌[^1338]ཐོགས་ན་ལན་བདུན་པ། །

[Block 3398]
གང་ཞིག་བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་གཅིག་ཀྱང་མ་སྤངས་པ་དེ་ནི་རྒྱུན་དུ་ཞུགས་པ༌[^1339]ཡིན་ལ། ཚེ་བདུན་གྱི་བར་དུ་སྐྱེ་བ་ན་ལན་བདུན་པའོ། །

[Block 3399]
རེ་ལྟར༌[^1340]ཐོགས་ན་ལན་བདུན་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཀྱི་ཐ་ཤལ་པའོ། །

[Block 3400]
དེ་ནི་དེ་ལས་གཞན་པར་སྐྱེ་བའི་སྲིད་པ་བདུན་དང་། སྲིད་པ་བར་མ་བདུན་དུ་མི་རྣམས་ཀྱི་ནང་དུ་ཉིང་མཚམས་སྦྱོར་བར་བྱེད་ལ། དེ་བཞིན་དུ་ལྷ་རྣམས་ཀྱི་ནང་དུ་ཡང་སྟེ། བདུན་ཚན་དུ༌[^1341]འདྲ་བའི༌[^1342]མཆོག་ཏུ་ཐོགས་ན་ལན་བདུན་པ་ཞེས་གསུངས་སོ། །

[Block 3401]
རེ་ཞིག་བསྒོམ་པས་སྤང་བར་བྱ་བ་མ་ཟད་པ་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3402 [VERSE]]
རྣམ་གསུམ་རྣམ་བཞི་ལས་གྲོལ་བ། །
ཚེ་གཉིས་གསུམ་དུ་རིགས་ནས་རིགས། །

[Block 3403]
རྒྱུན་དུ་ཞུགས་པ་དེ་ཉིད་ཉོན་མོངས་པའི་རྣམ་པ་གསུམ་མམ་བཞི་སྤངས་པའི་ཕྱིར་དང་། ཚེ་གཅིག་གམ་གཉིས་སུ་ལུས་པའི་ཕྱིར་རིགས་ནས་རིགས་སུ་སྐྱེ་བ་ཞེས་བྱའོ། །

[Block 3404 [HEADING]]
##### ལན་ཅིག་ཕྱིར་འོང་བ། ^6-2-2-2-0

[Block 3405 [VERSE]]
རྣམ་པ་ལྔ་ཡི་བར་བཅོམ་པ། །
གཉིས་པ་ལ་ནི་ཞུགས་པའང་ཡིན། །

[Block 3406]
འབྲས་བུ་ལ་གནས་པ་གང་གིས་རྣམ་པ་གཅིག་ནས་ལྔའི་བར་དུ་སྤངས་པ་ཡིན་ན་དེ་ནི་འབྲས་བུ་གཉིས་པ་ལ་ཞུགས་པ་ཡིན་ནོ། །

[Block 3407]
རྣམ་པ་དྲུག་པ་ཟད་གྱུར་པ། །དེ་ནི་ལན་ཅིག་ཕྱིར་འོང་བ་དང་། དེ་ནི་འབྲས་བུ་གཉིས་པ་ཐོབ་པ་ཡིན་ཏེ། ལྷ་དག་གི་ནང་དུ་སོང་ནས་མིའི་འཇིག་རྟེན་དུ་ལན་ཅིག་ཕྱིར་འོང་བའི་ཕྱིར་རོ། །

[Block 3408]
འབྲས་བུ་ལ་གནས་པ་དེ་ཉིད།

[Block 3409 [VERSE]]
ཉེས་ཆ་བདུན་དང་བརྒྱད་ཟད་པ། །
ཚེ་གཅིག་པ༌[^1343]བར་ཆད་གཅིག་པ་དང་།
གསུམ་པ་ལ་ནི་ཞུགས་པའང་ཡིན། །

[Block 3410]
རྣམ་པ་བདུན་ནམ་བརྒྱད་པ་སྤངས་པའི་ཕྱིར་དང་། ཚེ་གཅིག་ལུས་པའི་ཕྱིར་བར་ཆད་གཅིག་པ་ཞེས་བྱའོ། །

[Block 3411 [HEADING]]
##### ཕྱིར་མི་འོང་བ། ^6-2-2-3-0

[Block 3412]
དེ་དགུ་ཟད་པས་ཕྱིར་མི་འོང་། །འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བ་འདོད་པའི་ཁམས་སུ་ཕྱིར་མི་འོང་བའི་ཕྱིར་ཕྱིར་མི་འོང་བ་ཞེས་བྱའོ། །

[Block 3413 [VERSE]]
དེ་ནི་བར་སྐྱེས་འདུ་བྱེད་དང་། །
འདུ་བྱེད་མེད་ཡོངས་མྱ་ངན་འདའ། །
གོང་དུ་འཕོ་བ་རྣམས།

[Block 3414]
བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ༌[^1344]ནི་གང་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའོ། །

[Block 3415]
སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་སྐྱེས་པ་ཙམ་ལས་མི་འཆི་བར་ཕུང་པོ་ལྷག་མ་དང་བཅས་པའི་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་སྟེ། མངོན་པར་བརྩོན་པ་དང་། ལམ་ངང་གིས་འབྱུང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3416]
མངོན་པར་འདུ་བྱེད་པ་དང་བཅས་པས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་སྐྱེས་ནས་སྦྱོར་བ་མ་བཏང་ཞིང་མངོན་པར་འདུ་བྱེད་པ་དང་བཅས་པས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་གང་ཡིན་པ་སྟེ། མངོན་པར་བརྩོན་པ་དང་། ལམ་ངང་གིས་འབྱུང་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3417]
མངོན་པར་འདུ་བྱ་བ་མེད་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་མངོན་པར་འདུ་བྱེད་པ་མེད་པར་ཏེ། མངོན་པར་བརྩོན་པ་མེད་པར་ལམ་ངང་གིས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3418]
གོང་དུ་འཕོ་བ་ནི་གང་དུ་སྐྱེས་པ་དེ་ཉིད་དུ་ཡོངས་སུ་མྱ་ངན་ལས་མི་འདའ་བར་གོང་དུ་འགྲོ་བའོ། །

[Block 3419]
དེ་ནི། བསམ་གཏན་སྤེལ་ནས་འོག་མིན་འགྲོ། །དེ་ལ་གང་གིས་བསམ་གཏན་སྤེལ་བ་དེ་ནི་འོག་མིན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའོ། །

[Block 3420]
དེ་འཕར་ཕྱེད་འཕར་ཐམས་ཅད་དུ། །འཆི་འཕོ། །གང༌[^1345]དུ་འཕོ་བ་འོག་མིན་གྱི་མཐར་ཐུག་པ་དེ་ཡང་འཕར་བ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་རྣམ་པ་གསུམ་སྟེ། དེ་ལ་འཕར་བ་ཞེས་བྱ་བ་ནི་འདིར་བསམ་གཏན་རྣམས༌[^1346]སྤེལ་ནས། བསམ་གཏན་དང་པོའི་རོ་མྱངས་ཏེ་བསམ་གཏན་གསུམ་པ་ལས་ཡོངས་སུ་ཉམས་པ་ལས༌[^1347]ཚངས་རིས་པ་དག་གི་ནང་དུ་སྐྱེས་ནས་སྔོན་གྱི་གོམས་པའི་དབང་གིས་བསམ་གཏན་བཞི་པ་སྤེལ་ཏེ། དེ་ནས་ཤི་འཕོས་ནས་འོག་མིན་པ་དག་གི་ནང་དུ་སྐྱེས་པ་གང་ཡིན་པ་སྟེ། དེ་ནི་བར་དུ་མི་འགྲོ་བས་ན་འཕར་བ་ཞེས་བྱའོ། །

[Block 3421]
ཕྱེད་དུ་འཕར་བ་ཞེས་བྱ་བ་ནི་དེ་ནས་གནས་གཙང་མ་རྣམས་སུ་སྐྱེལ་བར་ནས་གནས་གཞན་འགའ་ཙམ་ཡང་རྒལ༌[^1348]ཏེ་འོག་མིན་དུ་འཇུག་པ་གང་ཡིན་པའོ། །

[Block 3422]
གནས་ཐམས་ཅད་དུ་འཆི་འཕོ་བ་ནི་གནས་གཞན་ཐམས་ཅད་དུ་འཕོས་ནས་འོག་མིན་དུ་འཇུག་པ་གང་ཡིན་པའོ། །

[Block 3423]
དེ་ལས།

[Block 3424]
གཞན་སྲིད་རྩེ་མོར་འགྲོ། །གོང་དུ་འཕོ་པ་བསམ་གཏན་མ་སྤེལ་བ་ནི་སྲིད་པའི་རྩེ་མོར་མཐར་ཐུག་པ་ཡིན་ནོ། །

[Block 3425]
དེ་ནི་སྙོམས་པར་འཇུག་པ་རྣམས་རོ་མྱང་བར་བྱེད་ཅིང་གནས་གཞན་ཐམས་ཅད་དུ་སྐྱེ་ལ། གནས་གཙང་མ་རྣམས་སུ་མི་འཇུག་པ་ཁོ་ནར་གཟུགས་མེད་པར་སྐྱེ་བའི་རིམ་གྱིས་སྲིད་པའི་རྩེ་མོར་སོང་སྟེ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའོ། །

[Block 3426]
རེ་ཞིག་དེ་དག་ནི་གཟུགས་སུ་ཉེ་བར་འགྲོ་བའི་ཕྱིར་མི་འོང་བ་ལྔ་ཡིན་ནོ། །

[Block 3427]
གཞན་ནི་གཟུགས་མེད་འགྲོ་རྣམ་བཞི། །བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་མ་གཏོགས་པ་གཟུགས་མེད་པར་འགྲོ་བའི་ཕྱིར་མི་འོང་བ་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 3428]
གཞན་ནི་འདི་ལ་མྱ་ངན་འདའ། །མྱ་ངན་ལས་འདའ་བའོ། །

[Block 3429]
གསུམ་ལ་ཡང་རྣམ༌[^1349]གསུམ་ཕྱེ་ནས། གཟུགས་སུ་ཉེར་འགྲོ་དགུར་བཤད་དོ། །

[Block 3430]
བར་མ་དོ་དང་། སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་དག་དང་། གོང་དུ་འཕོ་བ་གསུམ་རྣམ་པ་གསུམ་དུ་བྱས་པ་འདི་ལྟ་སྟེ་རེ་ཞིག་བར་མ་དོར་མྱ་ངན་ལས་འདའ་བ་རྣམས་ནི་དཔེ་གསུམ་གྱིས་མྱུར་བ་དང་། མྱུར་བ་མ་ཡིན་པ་དང་། ཡུན་རིང་མོ་ཞིག་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་རོ། །

[Block 3431]
སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་སྐྱེས་ནས་དང་། མངོན་པར་འདུ་བྱེད་པ་དང་། མངོན་པར་འདུ་བྱེད་པ་མེད་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་རོ། །

[Block 3432]
གོང་དུ་འཕོ་བ་ནི་འཕར་བ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་སོ། །

[Block 3433]
དེ་དག༌[^1350]ནི་ཁྱད་པར་རྣམས། ལས་དབང་ཉོན་མོངས་བྱེ་བྲག་ལས། །

[Block 3434]
གསུམ་དང་དགུ་པོ་དེ་དག་གི་ཁྱད་པར་ནི་ལས་དང་། ཉོན་མོངས་པ་དང་། དབང་པོའི་བྱེ་བྲག་ལས་ཏེ། རེ་ཞིག་གསུམ་པོ་ནི་མངོན་པར་འགྲུབ་པ་དང་། སྐྱེས་པ་དང་། ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བའི་ལས་བསགས་པའི་ཕྱིར་དང་། ཉོན་མོངས་པ་ཀུན་དུ་སྤྱོད་པ་ཆུང་བ་དང་། འབྲིང་དང་། ཆེན་པོའི་ཕྱིར་དང་། དབང་པོ་ཆེན་པོ་དང་། འབྲིང་དང་། ཆུང་ངུའི་ཕྱིར་རོ། །

[Block 3435]
དགུ་པོ་དེ་དག་སོ་སོར་ཁྱད་པར་དེ་ཉིད་ཀྱི་ཕྱིར་ཅི་རིགས་པར་གསུམ་ཚན༌[^1351]
--- END BLOCKS ---
