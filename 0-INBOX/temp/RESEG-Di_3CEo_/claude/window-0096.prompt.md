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
[Block 3361]
བཟོད་པ་རྣམས་ནི་ཉོན་མོངས་པའི་ཐོབ་པ་རྣམ་པར་གཅོད་པ་ལ་བར་ཆད་བྱ་བར་མི་ནུས་པའི་ཕྱིར་བར་ཆད་མེད་པའི་ལམ་དག་ཡིན་ནོ། །ཤེས་པ་རྣམས་ནི་ཉོན་མོངས་པའི་ཐོབ་པ་ལས་རྣམ་པར་གྲོལ་བའི་ཐོབ་པ་དང་ལྷན་ཅིག་སྐྱེས་པའི་ཕྱིར་རྣམ་པར་གྲོལ་བའི་ལམ་དག་ཡིན་ནོ། །

[Block 3362]
ཅི་སེམས་བཅུ་དྲུག་པོ་ཐམས་ཅད་བདེན་པ་མཐོང་བའི་ལམ་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ། འོན་ཀྱང་དེ་ལས་སྐད་ཅིག་བཅོ་ལྔ་ནི། མ་མཐོང་མཐོང་ཕྱིར་མཐོང་བའི་ལམ། །སེམས་བཅུ་དྲུག་པ་ལ་ནི་སྔོན༌[^1324]མ་མཐོང་བ་བལྟ་བར་བྱ་བ་མེད་ཀྱི། ཇི་ལྟར་མཐོང་བ་གོམས་པར་བྱེད་པའི་ཕྱིར་བསྒོམ་པའི་ལམ་ཁོ་ནའོ། །

[Block 3363]
མཐོང་བའི་ལམ་དང་བསྒོམ་པའི༌[^1325]ལམ་ཇི་ལྟར་སྐྱེ་བ་བཤད་ཟིན་ཏོ། །

[Block 3364 [HEADING]]
### འཕགས་པའི་ལམ་སྐྱེས་པའི་གང་ཟག་རྣམས་རྣམ་པར་གཞག་པ། ^6-2-0

[Block 3365 [HEADING]]
#### ངེས་པར་འཇུག་པའི་གང་ཟག་རྣམ་པར་གཞག་པ། ^6-2-1-0

[Block 3366]
ཇི་ལྟར་ན་འཕགས་པའི་ལམ་སྐྱེས་པའི་གང་ཟག་རྣམས༌[^1326]རྣམ་པར་གཞག་པ་དེ་བཞིན་དུ་བརྗོད་པར་བྱ་སྟེ། མཐོང་བའི་ལམ་གྱི་རང་བཞིན་གྱི་སྐད་ཅིག་མ་བཅོ་ལྔར་བཤད་པ་གང་དག་ཡིན་པ།

[Block 3367 [VERSE]]
དབང་པོ་རྣོ་རྟུལ་དེ་དག་ཏུ། །
དད་དང་ཆོས་ཀྱི་རྗེས་འབྲང་བ། །

[Block 3368]
ཡིན་པར་རིག་པར་བྱ་བ༌[^1327]སྟེ། དབང་པོ་རྟུལ་པོ་ནི་དད་པའི་རྗེས་སུ་འབྲང་བའོ། །

[Block 3369]
དབང་པོ་རྣོན་པོ་ནི་ཆོས་ཀྱི་རྗེས་སུ་འབྲང་བའོ། །

[Block 3370]
དེ་དག་ཀྱང་།

[Block 3371 [VERSE]]
བསྒོམ་པས༌[^1328]སྤང་བྱ་མ་སྤངས་ནས།[^1329] །
འབྲས་བུ་དང་པོ་ལ་ཞུགས་པ། །

[Block 3372]
དད་པ་དང་ཆོས་ཀྱི་རྗེས་སུ་འབྲང་བ་དེ་དག་ཁོ་ན་འཆིང་བ་མཐའ་དག་དང་ལྡན་པ་ཞིག་ཡིན་ན་དེ་གཉིས་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་ཞུགས་པ་ཞེས་བྱའོ། །

[Block 3373]
རྣམ༌[^1330]ལྔའི་བར་བཅོམ། འཇིག་རྟེན་པའི་ལམ་གྱིས་བསྒོམས་ཏེ་སྤང་བར་བྱ་བ་འདོད་པ་ན་སྤྱོད་པ་རྣམས་ལས་རྣམ་པ་ལྔའི་བར་དུ་སྤངས་ནའོ། །

[Block 3374]
གཉིས་པ་ལ།

[Block 3375]
དགུ་པ་ཚུན་ཆད་ཟད་པ་ཡིན། །གང་གི་ཚེ་དེ་གཉིས་ཀྱི་དེ་ཡན་ཆད་རྣམ་པ་དྲུག་གམ་བདུན་ནམ་བརྒྱད་གཅིག༌[^1331]སྔོན་སྤངས་པ་དེའི་ཚེ་ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་ལ་ཞུགས་པ་དག་ཏུ་བརྗོད་དེ།

[Block 3376 [VERSE]]
[^1332]འདོད་པའམ་ཡང་ན་གོང་མ་ལས། །
ཆགས་བྲལ་གསུམ་པ་ལ་ཞུགས་པ། །

[Block 3377]
གལ་ཏེ་འདོད་པའི་ཁམས་སམ་གོང་མ་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ཀྱི༌[^1333]བར་ལས་འདོད་ཆགས་དང་བྲལ་བ་ཞིག་ཡིན་ན་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ལ་ཞུགས་པ་དག་ཡིན་ནོ། །

[Block 3378 [VERSE]]
གང་ཞིག་གང་ལ་ཞུགས་པ་ནི། །
བཅུ་དྲུག་པ་ལ་དེ་འབྲས་གནས། །

[Block 3379]
སེམས་བཅུ་དྲུག་པ༌[^1334]སྐྱེས་ན་འབྲས་བུ་གང་ལ་ཞུགས་པར་གྱུར་པ་དེ་ནི་དེའི་ཚེ་འབྲས་བུ་དེ་ལ་གནས་པ་ཡིན་ནོ། །

[Block 3380 [VERSE]]
དེ་ཚེ་དབང་པོ་རྣོ་རྟུལ་དག །
དད་པས་མོས་དང་མཐོང་བས་ཐོབ། །

[Block 3381]
དེའི་ཚེ༌[^1335]དབང་པོ་རྟུལ་པོ་ནི་དད་པས་མོས་པའོ། །

[Block 3382]
དབང་པོ་རྣོན་པོ་གང་ཡིན་པ་དེ་ནི་མཐོང་བས་ཐོབ་པའོ། །

[Block 3383]
ཅིའི་ཕྱིར་རྣམ་པ་ལྔ་སྤངས་ཀྱང་སེམས་བཅུ་དྲུག་པ་ལ་རྒྱུན་དུ་ཞུགས་པ་ཁོ་ན་ཞེས་བྱ་ལ། ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་ལ་ཞུགས་པ་ཞེས་མི་བྱ་ཞེ་ན། གང་གི་ཕྱིར།

[Block 3384 [VERSE]]
འབྲས་ཐོབ་འབྲས་བུ་ཁྱད་པར་གྱི། །
ལམ་ཐོབ་མེད་པ་དེ་ཡི་ཕྱིར། །
འབྲས་གནས་ཁྱད་པར་བྱ་བའི་ཕྱིར། །
མི་བརྩོན་པ་ནི་ཞུགས་མ་ཡིན། །

[Block 3385]
འབྲས་བུ་ཐོབ་ན་འབྲས་བུ་ཁྱད་པར་ཅན་གྱི་ལམ་མི་ཐོབ༌[^1336]སྟེ། དེ་ལྟ་བས་ན་འབྲས་བུ་ལ་གནས་པ་ཇི་སྲིད་དུ་ཁྱད་པར་དུ་བྱ་བའི་ཕྱིར་མི་བརྩོན་པ་དེ་སྲིད་དུ་ཞུགས་པ་ཞེས་མི་བྱའོ། །

[Block 3386]
རེ་ཞིག་ཕལ་ཆེར་ལས་དང་། འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཀྱི་ངེས་པར་འཇུག་པའི་གང་ཟག་རྣམ་པར་གཞག་པ་དེ༌[^1337]ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3387 [HEADING]]
#### མཐར་གྱིས་འཇུག་པ། ^6-2-2-0

[Block 3388]
མཐར་གྱིས་འཇུག་པ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་རེ་ཞིག་འདི་ལྟར་རྣམ་པར་གཞག་པར་བྱའོ། །

[Block 3389]
ཇི་ལྟར་འདོད་པའི་ཁམས་ཀྱི་ཉོན་མོངས་པ་རྣམ་པ་དགུ་བསྟན་པ་དེ་བཞིན་དུ།

[Block 3390 [VERSE]]
ས་དང་ས་ན་ཉེས་རྣམ་དགུ། །
སྲིད་པའི་རྩེ་མོའི་བར་དུའོ། །

[Block 3391]
ཉེས་པ་རྣམས་ཇི་ལྟར། དེ་བཞིན་དུ་ནི་ཡོན་ཏན་རྣམས། །ས་དང་ས་ན་དེའི་གཉེན་པོ་བར་ཆད་མེད་པ་དང་། རྣམ་པར་གྲོལ་བའི་ལམ་ཞེས་བྱ་བ་ཡོན་ཏན་ཡང་རྣམ་པ་དགུ་དགུ་ཁོ་ན་ཡོད་དོ། །ཇི་ལྟར་བྱས་ནས་ཤེ་ན།

[Block 3392 [VERSE]]
ཆུང་དང་འབྲིང་དང་ཆེ་རྣམས་ཀྱི། །
ཆུང་ངུ་ལ་སོགས་ཐ་དད་ཕྱིར། །

[Block 3393]
འདི་ལྟ་སྟེ། ཆུང་ངུའི་ཆུང་ངུ་དང་། ཆུང་ངུའི་འབྲིང་དང་། ཆུང་ངུའི་ཆེན་པོ་སྟེ། དེ་བཞིན་དུ་འབྲིང་དང་། ཆེན་པོ་དག་གི་དབྱེ་བ་ཡང་གསུམ་གསུམ་མོ། །

[Block 3394]
དེ་ལ་ལམ་ཆུང་ངུའི་ཆུང་ངུས་ནི་ཉོན་མོངས་པ་ཆེན་པོའི་ཆེན་པོ་སྤོང་ལ། དེ་བཞིན་དུ་ཆེན་པོའི་ཆེན་པོས་ནི་ཆུང་ངུའི་ཆུང་ངུའི་བར་རོ། །

[Block 3395 [HEADING]]
##### རྒྱུན་དུ་ཞུགས་པ། ^6-2-2-1-0

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
--- END BLOCKS ---
