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
[Block 3396 [VERSE]]
དམར་ཞིང་སེར་བའི་བུད་མེད་གང་། །
པདྨའི་འདབ་ལྟར་དཀྱུས་རིང་མིག །
རྟག་ཏུ་གོས་དཀར་ལ་དགའ་ཞིང་། །
ཙནྡན་སར་པའི་དྲི་དང་ལྡན། །

[Block 3397 [VERSE]]
བདེ་གཤེགས་འདུས་པ་ཉིད་ལ་དགའ། །
ཞེན་པར་ལྟ་བའི་རྗེས་སུ་འགྲོ། །
ཁྱིམ་དུ་པདྨ་བྲི་བར་བྱེད། །
པདྨ་གར་དབང་རིགས་འབྱུང་ཡིན། །

[Block 3398]
ཞེས་གསུངས་སོ། །

[Block 3399]
འདིས་ནི་སེམས་ཅན་གྱི་དུས་ན་དེ་དང་དེའི་རིགས་སུ་ཤེས་པས་རང་ང་རྒྱལ་མི་བཅག་པ་དང་། གཞན་ལ་མཐོ་མི་བཙམ་པ་དང་བརྙས་པར་མི་བྱ་བའོ། །

[Block 3400]
སངས་རྒྱས་པའི་དུས་སུ་རིགས་དེ་དང་དེ་རུ་སངས་རྒྱས་པར་འགྱུར་རོ། །

[Block 3401]
བྷ་ག་ལིང་གར་འོ་མཛད་ནས། །ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ལུས་ཀྱི་འཁྲུལ་འཁོར་བསྟན་ཏེ་བླ་མ་ལས་ཤེས་པར་བྱའོ། །

[Block 3402]
ལེའུ་འདིས་ནི་སྤྱོད་པ་དང་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་དང་། ལས་ཀྱི་ཕྱག་རྒྱ་ལ་བརྟེན་ཏེ་བསྒོམ་པའི་ཡན་ལག་བསྟན་ཏོ། །

[Block 3403]
ལེའུ་བཅུ་གཅིག་པའོ།། །།

[Block 3404 [HEADING]]
### ལེའུ་ཐ་མ། ^2-11-0

[Block 3405]
དེ་ནས་རྡོ་རྗེ་ཅན་གྱི་དབང་བཞིའི་དོན་ནི་བཀའ་སྩལ་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལེའུ་ཐ་མ་འདིར་དབང་བཞིའི་ཚིགས་སུ་བཅད་པ་དང་། །རྡོ་རྗེ་དང་པདྨ་བྱིན་གྱིས་བརླབ་པ་སྟོན་ཏོ། །

[Block 3406 [HEADING]]
#### དབང་བཞིའི་ཚིགས་སུ་བཅད་པ། ^2-11-1-0

[Block 3407 [VERSE]]
རྡོ་རྗེ་རབ་གནས་རྡོ་རྗེ་ཉིད། །
ཆེ་དང་ཆེན་པོ་དྲིལ་བུ་ཟུང་། །

[Block 3408]
ཞེས་བྱ་བ་ནི་བུམ་པའི་དབང་ནས་བརྩམས་ཏེ།[^1361] །བརྟུལ་ཞུགས་ཀྱི་དབང་ཁྱད་པར་རྡོ་རྗེ་སློབ་དཔོན་གྱི་བརྟུལ་ཞུགས་བསྟན་ནོ། །

[Block 3409 [VERSE]]
དེ་རིང་རྡོ་རྗེ་སློབ་དཔོན་གྱུར། །
སློབ་མ་བསྡུ་བ་ཉིད་དུ་གྱིས། །

[Block 3410]
ཞེས་པ་ནི་ལུང་བསྟན་པ་དང་རྗེས་སུ་གནང་བ་དང་། དབུགས་དབྱུང་བ་དང་སློབ་དཔོན་གྱི་ལས་ལ་སོགས་པ་ཐམས་ཅད་བསྟན་ཏོ། །

[Block 3411 [VERSE]]
ཇི་ལྟར་འདས་པའི་སངས་རྒྱས་ཀྱིས། །
བྱང་ཆུབ་སྲས་རྣམས་དབང་བསྐུར་བ། །
བདག་གི་གསང་བའི་དབང་གིས་ནི། །
སེམས་ཀྱི་རྒྱུན༌[^1362]གྱི་དབང་བསྐུར་ཏོ། །

[Block 3412]
ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་སྦྱིན་པའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 3413]
ལྷ་མོ་དགའ་སྦྱིན་གནས་སྦྱིན་མ། །ཞེས་བྱ་བ་ཤློ་ཀ་གཅིག་གིས་ནི་རིག་མ་སྦྱིན་པའོ། །

[Block 3414]
ཡེ་ཤེས་འདི་ནི་ཆེས་ཕྲ་ཞིང་། །ཞེས་པ་ནི་གསུམ་པས་གོ་ཕྱེ་བའི་བཞི་པའི་དོན་ཏེ། །རྡོ་རྗེ་ནམ་མཁའི་དཀྱིལ་ལྟ་བུ་ནི་རྟོག་པས་སྟོང་པའི་དཔེས་བསྟན་ཏོ། །

[Block 3415]
རྡུལ་བྲལ་ཐར་པ་ཞི་བ་ཉིད་ནི་ཉོན་མོངས་པ་དང་གློ་བུར་བ་ཐམས་ཅད་ཞི་བའོ། །

[Block 3416]
ཁྱོད་རང་ཡང་ནི་དེ་ཡི་ཕ། །ཞེས་པ་ནི་རང་གི་སེམས་ཏེ་དེའི་བདེ་བ་ལྷན་ཅིག་སྐྱེས་པའི་ཡེ་ཤེས་སོ། །

[Block 3417 [HEADING]]
#### རྡོ་རྗེ་དང་པདྨ་བྱིན་གྱིས་བརླབ་པ། ^2-11-2-0

[Block 3418]
ད་ནི་རྡོ་རྗེ་དང་པདྨ་བྱིན་གྱིས་བརླབ་སྟེ།[^1363] ཨོཾ་པདྨ་སུ་ཁ་ངྷ་ར་ལ་སོགས་པས་བསྟན་ཏེ་རྡོ་རྗེ་འཆང་བསྐྱེད་པའི༌[^1364]རྗེས་ལ་འཁོར་བསྐྱེད་པའི་དོན་དུ་བྱིན་གྱིས་བརླབ་པ༌[^1365]དང་ཐ་མལ་པ་སྤངས་པའི་དགོངས་པའོ། །

[Block 3419]
ཡང་སྤྱོད་པ་དང་ལས་ཀྱི་ཕྱག་རྒྱ་བསྒོམ་པའི་སྔོན་དུ་ཡང་འགྲོ་བའོ། །

[Block 3420]
སྤྱི་བོར་ཨོཾ་གྱི་རྣམ་པ། སྙིང་གར་ཧཱུཾ་གི་རྣམ་པ། ཟེའུ་འབྲུ་ལ་ནི་ཨའི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་སྐུ་གསུང་ཐུགས་ཀྱི་བྱིན་གྱིས་བརླབ་པའི་ས་བོན་ནོ། །

[Block 3421]
གང་ཟེའུ་འབྲུ་ནི་སའི་རྣམ་པའོ་ཞེས་པ་རྡོ་རྗེ་པདྨ་བྱིན་གྱིས་རློབ་པ་ཡང་གཟུང་སྟེ། ཧཱུཾ་ལས་རྡོ་རྗེ། ཨོཾ་གྱིས་ནོར་བུ་ཕཊ་ཀྱིས་བུག་སྒོ་དགག །ཨོཾ་གྱིས་པདྨ་ཨས་ཟེའུ་འབྲུ་ཕཊ་ཀྱིས་བུག་སྒོ་དགག་པའོ། །

[Block 3422]
གོང་དུ་ཡང་། ཧཱུཾ་ཕཊ་རྣམ་པ་འདོད་མི་བྱ། །

[Block 3423 [VERSE]]
ཞེས་གསུངས་པ་ནི་བདག་མེད་མ་ལ་བཀག་པའོ། །
དགྱེས་པའི་རྡོ་རྗེ་ལ་ནི་འདོད་པ་ཁོ་ནའོ།། །།

[Block 3424]
རྒྱུད་ཀྱི་རྒྱལ་པོ་ཆེན་པོ་སྒྱུ་མའི༌[^1366]བརྟག་པ་ཞེས་བྱ་བ་ནི་ཕྱག་རྒྱ་ཆེན་པོ་སྟེ་སྒྱུ་མ་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 3425]
བརྟག་པ་ནི་ཆོ་ག་ཞིབ་མོའོ། །

[Block 3426]
བརྟག་པ་སུམ་ཅུ་རྩ་གཉིས་ལས་ཕྱུང་བ་ཞེས་བྱ་བ་ནི་མི་བསྐྱོད་དགྱེས་པའི་རྡོ་རྗེ་ལ་བསྡུ་བྱ་བརྟག་པ་སུམ་ཅུ། སྡུད་བྱེད་གཉིས་ཏེ་དེ་ཡང་བསྡུ་བྱ་སྡུད་བྱེད་དུ་བྱས་པ་སུམ་ཅུ་རྩ་གཉིས། བརྟག་པ་གཉིས་ཀྱི་བདག་ཉིད་བསྟན་པ་དང་བཤད་པར་གནས་པའོ། །

[Block 3427]
ཀྱེའི་རྡོ་རྗེ་མཁའ་འགྲོ་མ་དྲ་བའི་སྡོམ་པ་ནི་རྡོ་རྗེ་བདག་མེད་མ་ལ་སོགས་པ་ཞུ་བ་པོའི་གཙོ་མོའོ། །

[Block 3428]
དེ་ཡང་དྲ་བ་ནི་ཐབས་དང་ཤེས་རབ་བོ། །

[Block 3429]
སྡོམ་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོར་སྡོམ་པའམ་རྒྱུད་འདིར་སྡོམ་ཞེས་བྱའོ། །

[Block 3430]
རྒྱུད་ཀྱི་རྒྱལ་པོ་ཆེན་པོ་རྫོགས་སོ།། །།

[Block 3431 [HEADING]]
## བསྔོ་བ། ^a-0

[Block 3432]
བླ་མ་དམ་པས་རྐྱེན་བྱས་སོ་སོར་རྟོག་པའི་ཉེར་ལེན་གྱིས། །སློབ་མ་དམ་པ་འགའ་ཡིས་ཡང་དང་ཡང་དུ་གསོལ་བཏབ་ནས། །རྒྱུད་ཀྱི་འགྲེལ་པ་དཀའ་དོན་སྤྱན་འབྱེད་བདག་གིས་བྱས། །འདི་ལས་བསོད་ནམས་ཀྱིས་ནི་རྗེས་སུ་འབྲང་དང་སེམས་ཅན་རྡོ་རྗེ་འཛིན་ཐོབ་ཤོག །

[Block 3433 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 3434 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 3435]
རྒྱུད་ཀྱི་རྒྱལ་པོ་ཆེན་པོ་དཔལ་དགྱེས་པ་རྡོ་རྗེའི་དཀའ་འགྲེལ་སྤྱན་འབྱེད་ཅེས་བྱ་བ་སློབ་དཔོན་ཆེན་པོ་མཁས་པ་དྷརྨྨཱ་ཀཱིརྟིས་མཛད་པ་རྫོགས་སོ།། །།
--- END BLOCKS ---
