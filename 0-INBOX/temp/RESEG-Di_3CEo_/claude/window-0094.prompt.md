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

[Block 3296]
བཟོད་པ་ནི། ཐམས་ཅད་ཆོས་ཀྱིས་འཕེལ་བར་བྱེད། །ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་ཁོ་ནས་འཕེལ་བར་བྱེད་ཀྱི།

[Block 3297 [VERSE]]
[^1296] གཞན་གྱི་ས་ནི་མ་ཡིན་ནོ། །
ཆེན་པོ་འདོད་གཏོགས་སྡུག་བསྔལ་ཡུལ། །

[Block 3298]
དེ་ནི་ཆོས་ཀྱི་མཆོག་དང་ཉེ་བའི་ཕྱིར་འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་ལ་དམིགས་པ་ཁོ་ནའོ། །

[Block 3299]
དེ་ཉིད་ཀྱི་ཕྱིར་དྲོ་བར་གྱུར་པ་ལ་སོགས་པའི་ངེས་པ་མ་སྨོས་པའི་ཕྱིར་ཁམས་གསུམ་པའི་སྡུག་བསྔལ་ལ་སོགས་པ༌[^1297]ལ་དམིགས་པ་ཉིད་དུ་གྲུབ་པོ། །གང་གི་ཚེ་གཟུགས་དང་། གཟུགས་མེད་པའི་གཉེན་པོ་ལ་སོགས་པ་བདེན་པའི་རྣམ་པ་དམིགས་པ་རེ་རེ་ནས་ཕྲི་ནས་འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་ཁོ་ན་ལ་སྐད་ཅིག་མ་གཉིས་སུ་ཡིད་ལ་བྱེད་པའི་བར་དེ་ཐམས་ཅད་ནི་བཟོད་པ་འབྲིང་ཡིན་ལ། གང་གི་ཚེ་སྐད་ཅིག་མ་གཅིག་ཁོ༌[^1298]ན་གང་ཡིན་པ་དེའི་ཚེ་ནི་ཆེན་པོ་ཡིན་ནོ། །

[Block 3300]
དེ་ནི་སྐད་ཅིག་གཅིག །དེ་ནི་སྐད་ཅིག་མ་གཅིག་ཡིན་གྱི་རྒྱུན་ཆགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 3301 [HEADING]]
##### ཆོས་མཆོག། ^6-1-6-4-0

[Block 3302]
དེ་བཞིན་ཆོས་མཆོག །དེ་དག་ཀྱང་བཟོད་པ་ཆེན་པོའི༌[^1299]ཇི་ལྟ་བ་བཞིན་དུ་འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་ལ་དམིགས་པ་དང་། སྐད་ཅིག་མ་གཅིག་པ་དག་ཡིན་ནོ། །

[Block 3303]
དྲོ་བར་གྱུར་པ་ལ་སོགས་པ་དེ་དག་ནི་དྲན་པ་ཉེ་བར་གཞག་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཤེས་རབ་ཀྱི་བདག་ཉིད་ཅེས་བྱའོ། །

[Block 3304]
ཐམས་ཅད་ཕུང་པོ་ལྔ། འཁོར་དང་བཅས་པ་སྨོས་པའི་ཕྱིར་རོ། །

[Block 3305]
ཐོབ་པ་མ་གཏོགས། ཐོབ་པ་རྣམས་ནི་དྲོ་བར་གྱུར་པ་ལ་སོགས་པས༌[^1300]མ་བསྡུས་ཏེ། འཕགས་པ་ལ་དེ༌[^1301]མངོན༌[^1302]དུ་གྱུར་པས་དྲོ་བར་གྱུར་པས༌[^1303]སོགས་པ་ཡང་མངོན་སུམ་དུ་འགྱུར་དུ་འོང་བས་སོ། །

[Block 3306]
དེ་ལྟར་ནི།[^1304] ངེས་འབྱེད་ཆ་མཐུན་རྣམ་པ་བཞི། །བསྒོམས་བྱུང་ཐོས་པ་དང་། བསམས་པ་ལས་བྱུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 3307]
མི་ལྕོགས་མེད་པ་དང་། ཁྱད་པར་བསམ་གཏན་ས་པའོ། །

[Block 3308]
འདིའི་ས་ནི་མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་བཞི་ཡིན་ཏེ།

[Block 3309 [VERSE]]
དེ་དག་གིས་བསྡུས་པའི་ཕྱིར་རོ། །
གཉིས་ནི་འོག་ན་འང་ཡོད་པའམ། །

[Block 3310]
བཙུན་པ་དབྱངས་སྒྲོགས་ཀྱི་ལྟར་ན།

[Block 3311]
དང་པོ་གཉིས་ནི་ས་བདུན་པ་ཡིན་ཏེ། འདོད་པ་ན་སྤྱོད་པ་ཡང་ཡོད་དོ། །

[Block 3312]
དེ་དག་ཐམས་ཅད་ཀྱང་། འདོད་རྟེན་མི་ཁོ་ན་ལས་སྐྱེད་པར་བྱེད་པའོ།[^1305] །

[Block 3313]
གསུམ་ནི་སྐྱེས་པ་དང་བུད་མེད་ཀྱིས་གཉིས་ཀའི་རྟེན་ཅན་དག་འཐོབ་པོ། །ཆོས་མཆོག་བུད་མེད་ཀྱིས། གཉིས་ཀའི་རྟེན་ཅན་འཐོབ་པར༌[^1306]འགྱུར། །ཆོས་ཀྱི་མཆོག་ནི་བུད་མེད་ཀྱིས་གཉིས་ཀའི་རྟེན་ཅན་འཐོབ་ལ། སྐྱེས་པས་ནི་སྐྱེས་པའི་རྟེན་འབའ་ཞིག་འཐོབ་སྟེ། བུད་མེད་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 3314]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་ཇི་ལྟར་གཏོང་ཞེ་ན། འཕགས་པས་དེ་དག་ས་བོར་ནས། །གཏོང་ངོ་། །འཕགས་པ་ནི་ས་གང་ཐོབ་པར་གྱུར་པའི་ས་དེ་དག་འདོར་བ་ན། དེ་དག་ཀྱང་གཏོང་ངོ་། །ས་འདོར་བ་ནི་ས་འཕོས་པ་ལས་སོ། །

[Block 3315]
འཕགས་མིན་འཆི་འཕོ་བས་སོ། །

[Block 3316]
སོ་སོའི་སྐྱེ་བོ་ནི་འཆི་བ་ཁོ་ནས་གཏོང་ངོ་། །

[Block 3317]
དང་པོ་གཉིས༌[^1307]ཡོངས་ཉམས་པས་ཀྱང་། །འཆི་བས་ཀྱང་གཏོང་སྟེ།

[Block 3318 [VERSE]]
སོ་སོའི་སྐྱེ་བོ་ཁོ་ནའོ། །
དངོས་གཞིའི༌[^1308]དེ་ཉིད་ལ་བདེན་མཐོང་། །

[Block 3319]
གང་ཞིག་བསམ་གཏན་དངོས་གཞིའི་ས་པའི་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་སྐྱེད་པར་བྱེད་པ་དེས་ནི་ཚེ་དེ་ཉིད་ལ་གདོན་མི་ཟ་བར་བདེན་པ་རྣམས་མཐོང་བར་འགྱུར་ཏེ།

[Block 3320]
ཡིད་འབྱུང་ཤས་ཆེ་བའི་ཕྱིར་རོ། །རྣམ་པར་ཉམས་ན་སྔོན༌[^1309]མེད་འཐོབ། །

[Block 3321]
གང་གི་ཚེ་རྣམ་པར་ཉམས་པ་དག་ཀྱང་སུ༌[^1310]ཐོབ་པ་དེའི་ཚེ་སྔོན་མེད་པ་དག་ཁོ་ན་འཐོབ་ཀྱི་སྔོན་བཏང་བ་དག་ནི་མ་ཡིན་ནོ། །

[Block 3322]
རྣམ་པར་ཉམས་པ་དང་། ཡོངས་སུ་ཉམས་པ་འདི་དག་གི་རང་བཞིན་ཅི་ཞེ་ན། ཉམས་པ་གཉིས་ནི་མི་ལྡན་པ། ཉམས་པ་དེ་གཉིས་ཀ་ཡང་མི་ལྡན་པའི་རང་བཞིན་ཡིན་ནོ། །

[Block 3323]
རྩེ་མོ་ཐོབ་པ༌[^1311]རྩ་མི་འཆད། །རྩེ་མོ་ཐོབ་པ་ནི་ཡོངས་སུ་ཉམས་ཀྱང་དགེ་བའི་རྩ་བ་ཀུན་དུ་མི་འཆད་དོ། །

[Block 3324]
བཟོད་ཐོབ༌[^1312]ངན་སོང་མི་འགྲོའོ།[^1313] །

[Block 3325]
བཟོད་པ་ལས་ནི་རྣམ་པར་ཉམས་ཀྱང་ངན་སོང་དུ་མི་འགྲོ་སྟེ། དེར་འགྲོ་བའི་ལས་དང་ཉོན་མོངས་པ་ཐག་བསྲིངས་པའི་ཕྱིར་རོ། །

[Block 3326]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་དེ་དག་ཀྱང་རིགས་གསུམ་ཡིན་ཏེ། །དེ་ལ། གཉིས་སློབ་རིགས་ལས་བཟློག་ནས་ནི། །སངས་རྒྱས་སུ་འགྱུར། དྲོ་བར་གྱུར་པ་དང་། རྩེ་མོ་སྐྱེས་པ་ཉན་ཐོས་ཀྱི་རིགས་ལས་བཟློག་ནས་ཡང་སངས་རྒྱས་སུ་འགྱུར་བ་ནི་སྲིད་དོ། །

[Block 3327]
གཞན་གསུམ་ཡང་། གསུམ་ཡང༌[^1314]ཉན་ཐོས་ཀྱི་རིགས་ལས་བཟློག་ནས་སངས་རྒྱས་ལས་གཞན་དུ་འགྱུར་རོ། །

[Block 3328]
རང་སངས་རྒྱས་ཀྱི་རིགས་རྣམས་ནི་བཟློག་པར་མི་ནུས་ཏེ། འདི་ལྟར།

[Block 3329 [VERSE]]
སྟོན་དང་བསེ་རུ་བྱང་ཆུབ་པར། །
བསམ་གཏན་མཐའ་རྟེན་གཅིག་ལ་ཀུན། །

[Block 3330]
སངས་རྒྱས་དང་། རང་སངས་རྒྱས་དག་ནི་བསམ་གཏན་བཞི་པ་ཁོ་ན་ལ་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་ལས༌[^1315]བཟུང་སྟེ། བྱང་ཆུབ་ཀྱི་བར་དུ་སྐྱེད་པར་བྱེད་དོ། །
--- END BLOCKS ---
