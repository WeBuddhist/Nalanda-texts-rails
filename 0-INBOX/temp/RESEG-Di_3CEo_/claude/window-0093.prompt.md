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
[Block 3256]
འཇུག་པའི་སྒོ་གཉིས་བཤད་ཟིན་ཏོ། །

[Block 3257 [HEADING]]
#### དྲན་པ་ཉེར་གཞག། ^6-1-5-0

[Block 3258]
དེ་གཉིས་ཀྱིས་ཏིང་ངེ་འཛིན་ཐོབ་ནས།

[Block 3259 [VERSE]]
ལྷག་མཐོང་བསྒྲུབ་པར་བྱ་བའི་ཕྱིར། །
ཞི་གནས་གྲུབ་པར་གྱུར་པ་ཡིས། །
དྲན་པ་ཉེར་གཞག་བསྒོམ་པར་བྱ། །

[Block 3260]
ཇི་ལྟར་བྱ་ཞེ་ན།

[Block 3261 [VERSE]]
ལུས་ཚོར་སེམས་དང་ཆོས་རྣམས་ལ། །
མཚན་ཉིད་གཉིས༌[^1280]སུ་ཡོངས་བརྟགས་པས། །

[Block 3262]
ལུས་དང་། ཚོར་བ་དང་། སེམས་དང་། ཆོས་རྣམས་ལ་རང་དང་སྤྱིའི་མཚན་ཉིད། དག་ཏུ་ཡོངས་སུ་བརྟགས་པ༌[^1281]སྟེ། །དེ་དག་གི་རང་གི་མཚན༌[^1282]ཉིད་ནི་རང་གི་ངོ་བོའོ། །

[Block 3263]
སྤྱིའི་མཚན་ཉིད་ནི་འདུས་བྱས་རྣམས་ནི་མི་རྟག་པ་ཉིད་དང་། ཟག་པ་དང་བཅས་པ་རྣམས་སྡུག་བསྔལ་ཉིད་དང་། ཆོས་ཐམས་ཅད་སྟོང་པ་དང་བདག་མེད་པ་ཉིད་དག་གོ། །

[Block 3264]
ལུས་ཀྱི་ངོ་བོ་ནི༌[^1283]འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ་ཉིད་དོ། །

[Block 3265]
གསུམ་ལས་གཞན་བདག་ནི་ཆོས་སོ། །

[Block 3266]
ཡང་དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་ཀྱི་རང་བཞིན་ནི་ཅི་ཞེ་ན། དྲན་པ་ཉེ་བར་གཞག་པ་ནི་རྣམ་པ༌[^1284]གསུམ་སྟེ། རང་བཞིན་དང་། འབྲེལ་པ་དང་།

[Block 3267 [VERSE]]
དམིགས་པའི་དྲན་པ་ཉེ་བར་གཞག་པའོ། །
ཤེས་རབ་ཐོས་སོགས་ལས་བྱུང་བའོ། །
གཞན་ནི་འབྲེལ་དང་དམིགས་པ་ལས། །

[Block 3268]
རང་བཞིན་གྱི་དྲན་པ་ཉེ་བར་གཞག་པ་ནི་ཤེས་རབ་སྟེ། གཞན་དེ་དང་ལྷན་ཅིག་འབྱུང་བའི་ཆོས་རྣམས་འབྲེལ་པའི་དྲན་པ་ཉེ་བར་གཞག་པའོ། །

[Block 3269]
དེ་དག་གི་དམིགས་པ་ནི་དམིགས་པའི་དྲན་པ་ཉེ་བར་གཞག་པའོ། །

[Block 3270 [VERSE]]
རིམ་ནི་ཇི་ལྟར་སྐྱེ་བ་བཞིན། །
ཅིའི་ཕྱིར་དེ་ལྟར་སྐྱེ་ཞེ་ན།
སྔར་རགས་པ༌[^1285]མཐོང་བའི་ཕྱིར་རོ། །
ཕྱིན་ཅི་ལོག་གི་གཉེན་པོར་བཞི། །

[Block 3271]
གཙང་བ་དང་བདེ་བ་དང་། རྟག་པ་དང་། བདག་ཏུ་ཕྱིན་ཅི་ལོག་པ་རྣམ་པ་བཞིའི་གཉེན་པོར་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་གོ་རིམས་བཞིན་དུ་བསྟན་ཏོ། །

[Block 3272]
དེ་ལྟར་ལུས་ལ་སོགས་པ་ལ་དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་གོམས་པར་བྱས་ནས།

[Block 3273 [VERSE]]
དེ་ནི་ཆོས་དྲན་ཉེར་གཞག་པ། །
སྤྱི་ལ་དམིགས་པ་ལ་གནས་ཏེ། །
དེ་དག་ལ་ནི་མི་རྟག་དང་། །
སྡུག་བསྔལ་སྟོང་བདག་མེད་པར་ལྟའོ། །

[Block 3274]
དྲན་པ་ཉེ་བར་གཞག་པ་འདྲེས་པ་ལ་དམིགས་པ་ལ་གནས་ཏེ། ལུས་ལ་སོགས་པ་དེ་དག་ཐམས་ཅད་སྤྱིར་བསྡུས་ཏེ་རྣམ་པ༌[^1286]བཞིར་ལྟའོ། །

[Block 3275 [HEADING]]
#### ངེས་འབྱེད་ཆ་མཐུན་རྣམ་པ་བཞི། ^6-1-6-0

[Block 3276 [HEADING]]
##### དྲོ་བ། ^6-1-6-1-0

[Block 3277]
དེ་ལས་དྲོ་བར༌[^1287]གྱུར་པ་འབྱུང་།[^1288] །དྲན་པ་ཉེ་བར་གཞག་པ་དེ་ལྟར་གོམས་པ་ལས་རིམ་གྱིས་དགེ་བའི་རྩ་བ་དྲོ་བར་གྱུར་པ་ཞེས་བྱ་བ་སྐྱེའོ། །

[Block 3278]
དེ་ནི་བདེན་བཞིའི་སྤྱོད་ཡུལ༌[^1289]ཅན། །དྲོ་བར་གྱུར་པ་དེ་ནི་རྒྱུན་ཆགས་པ་ཡིན་པའི་ཕྱིར་བདེན་པ་བཞི་ལ་དམིགས་པ་ཡིན་ནོ། །

[Block 3279]
རྣམ་པ་བཅུ་དྲུག་སྡུག་བསྔལ་ལ་སོགས་པ་རེ་རེ་ལ་ཡང་རྣམ་པ་བཞི་བཞི་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 3280]
དྲོ་བ་ལས།

[Block 3281]
[^1290] རྩེ་མོ། །

[Block 3282 [HEADING]]
##### རྩེ་མོ། ^6-1-6-2-0

[Block 3283]
དྲོ་བ་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོའི་རིམ་གྱིས་མངོན་པར་འཕེལ་བ་ལ་རྩེ་མོ་དག་སྐྱེ་སྟེ། དེ་ཡང་དེ་དང་འདྲ། ཇི་ལྟར་དྲོ་བར་གྱུར་པ་རྣམས་བདེན་པ་བཞི་ལ་དམིགས་པ་དང་། རྣམ་པ་བཅུ་དྲུག་ཡིན་པ་བཞིན་ཏེ། ཆོས་མཆོག་ཏུ་གྱུར་པའི་ཕྱིར་ན་མིང་གཞན་དུ་བཏགས༌[^1291]སོ། །

[Block 3284]
གཉིས་ཀ་ཆོས་ཀྱིས་རྣམ་པ་གཏོད། །དྲོ་བར་གྱུར་པ་དང་། རྩེ་མོ་དང་། འདི་གཉིས་ཀ་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པས་ཉེ་བར་གཏོད་པར་བྱེད་པ་ནི།

[Block 3285]
དང་པོ་ཉིད་དུ་བདེན་པ་རྣམས་ལ་རྣམ་པ་དག་འགོད་པའོ། །

[Block 3286]
གཞན་དག་གིས་ཀྱང་འཕེལ་བར་བྱེད་དོ། །

[Block 3287]
དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ཆར་གྱིས་ཀྱང་དེ་དག་འཕེལ་བར་བྱེད་དོ། །

[Block 3288]
རྣམ་པར་འཕེལ་བར་བྱེད་པ་ན་སྔོན་ཐོབ་པ་རྣམས་མངོན་སུམ་དུ་མི་བྱེད་དེ། དགའ་བ་ཆེན་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 3289]
ཆུང་ངུ་དང་འབྲིང་དང་།

[Block 3290]
ཆེན་པོའི་རིམ་གྱིས་འཕེལ་བ༌[^1292]དག་ལས།

[Block 3291 [HEADING]]
##### བཟོད་པ། ^6-1-6-3-0

[Block 3292]
དེ་ལས་བཟོད་པ་ཡང་སྐྱེ་སྟེ། ཡོངས་སུ་མི་ཉམས་པའི་སྒོ་ནས་བདེན་པ་ལ༌[^1293]ཆེར་བཟོད་པའི་ཕྱིར་རོ། །

[Block 3293]
དེ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཆུང་ངུ་དང་། འབྲིང་དང་། ཆེན་པོའོ། །

[Block 3294]
དེ་ལ་རྣམ་པ་གཉིས་དེ་བཞིན། །རྩེ་མོ་རྣམས་ཇི་སྐད་བཤད་པ་ལྟར་བཟོད་པ་ཆུང་ངུ་དང་། འབྲིང་དག་ཀྱང་དེ་དང་འདྲ་སྟེ། དེ་ཁོ་ན་བཞིན་དུ་རྣམ་པ་གཏོད་པའི་ཕྱིར་རོ། །

[Block 3295]
རྣམ་པར་འཕེལ་བ་ལ་ནི་ཁང་པར༌[^1294]འདི་ཡོད་དོ།[^1295] །
--- END BLOCKS ---
