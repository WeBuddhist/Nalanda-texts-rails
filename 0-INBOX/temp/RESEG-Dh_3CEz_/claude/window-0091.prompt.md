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
[Block 3186]
དེ་ནས། དབང་ལྡན་དུ་ནི་ཤ་ར་བྷ། །ཞེས་བྱ་བ་ནས། ཕྱག་མཚན་བརྒྱད་དུ་རབ་ཏུ་གྲགས། །ཞེས་པ་སྟེ་རང་རང་གི་སྔགས་ལ་དེ་ཉིད་གསུམ་སྤེལ་ཞིང་ལྷ་རུ་མོས་པ་དགོད་པར་བྱའོ། །

[Block 3187]
དེ་ནས་བུམ་པ་དགོད་པ་ནི་དེ་ནས་རྣམ་རྒྱལ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་བུམ་པའི་ཡོ་བྱད་ཐམས་ཅད་གསོས་གདབ་སྟེ། སྟ་གོན་གྱི་གནས་ནས༌[^1294]རོལ་མོ་དང་བཅས་པས་སྤྱན་དྲངས་ལ་རྣམ་པར་རྒྱལ་བའི་བུམ་པ་ནི་གཙོ་བོའི་སྤྱན་སྔར་གཞག་པར་བྱའོ། །

[Block 3188]
བུམ་པ་གཞན་རྣམས་ནི་རང་རང་གི་གནས་ལ་ཉེ་བར་གཞག༌[^1295]གོ། །

[Block 3189]
ལས་ཐམས་ཅད་པའི་བུམ་པ་ནི་སྒོའི་གཡས་ཕྱོགས་སུ་དགོད་པར་བྱའོ། །

[Block 3190]
དེ་བཞིན་དུ་མཆོད་པ་ཐམས་ཅད་ཀྱང་ཉེ་བར་བཤམ། བླ་རེ་དང་རྒྱན་དང་གདུགས་དང་བདན་ལ་སོགས་པ་དང་རྟ་བབས༌[^1296]དང་རོལ་མོ་དང་། ན་བཟའི་བྱེ་བྲག་ཐམས་ཅད་ཀྱང་ལྷ་རྣམས་ལ་རས་ཟུང་རེ་རེ་དབུལ་བར་བྱའོ། །

[Block 3191 [VERSE]]
དེ་ནས་དཀྱིལ་འཁོར་བསྒྲུབ་པ་ནི། །
མང་དུ་བརྗོད་པས་ཅི་ཞིག་བྱ། །
ཇི་ལྟར་དེ་ཉིད་བསྡུས་པ་ཡི། །

[Block 3192]
དཀྱིལ་འཁོར་ཆོ་ག་དེ་བཞིན་བྱ།[^1297] །ཞེས་བྱ་བ་ནི་སྤྱིར་དེ་དག་ཐམས་ཅད་མཐུན་པར་ཤེས་པར་བྱའོ། །

[Block 3193]
ཁྱད་པར་ནི་དཀྱིལ་འཁོར་གྱི་ཤར་སྒོ་རུ་སྟན་བདེ་བ་ལ༌[^1298]འདུག་སྟེ། ཡན་ལག་དྲུག་གི་རྣལ་འབྱོར་པ༌[^1299]སྦྱོར་བ་རྣམ་པ་གསུམ་བཟླས་པའི་བར་དུ་བྱ་བ་ནི་བདག་ཉིད་ལྡན་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3194]
དེར་དཀྱིལ་འཁོར་གྱི་ལྷ་རྣམས་ས་བོན་ཕྱག་མཚན་ཙམ་ལས་བསྐྱེད་ལ་ཡེ་ཤེས་ཀྱི༌[^1300]འཁོར་ལོ༌[^1301]དགུག །སྐྱེ་མཆེད་དང་སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབ། མཆོད་བསྟོད་རྒྱས་པར་བྱ། བདུད་རྩི་མྱང་བ་བཟླས་པའི་བར་དུ་བྱའོ། །

[Block 3195]
དེ་ནས་སློབ་མས་མཎྜལ་བྱས་ལ་གསོལ་བ་གདབ་པ་དང་ཆོ་ག་རྣམས་ནི་སྟ་གོན་གྱི་སྐབས་བཞིན་འདིར་བྱའོ། །

[Block 3196]
དེ་དག་ཐུན་མོང་གི་ཆོ་ག་ཐམས་ཅད་ནི་ཇི་ལྟར་དེ་ཉིད་བསྡུས་པ་ལྟར་བྱའོ། །

[Block 3197]
ཁྱད་པར་གྱི་ཆོ་ག་ནི་ལེའུ་བཅུ་པར་བསྟན་པ་བཞིན་ནོ། །

[Block 3198]
འཇུག་པའི་ཆོ་ག་ལ་དམ་ཚིག་བསྒྲགས། མནའ་ཆུ་བླུད། དེ་ནས་ཡེ་ཤེས་དབབ་པ་དང་། མེ་ཏོག་དོར་བ་དང་། དཀྱིལ་འཁོར་ཀྱི་ལྷ་ངོ་བསྟན་ནས་དཀྱིལ་འཁོར་གྱི་དེ་ཁོ་ན༌[^1302]ཉིད་དང་ལྷའི་དེ་ཁོ་ན་ཉིད་བཅས་པ་ནི་འཇུག་པའི་རིམ་པའོ། །

[Block 3199 [HEADING]]
##### དབང་བསྐུར་བ། ^2-5-2-3-0

[Block 3200]
དེ་ནས་དབང་བསྐུར་བ་ལ་ཁྱད་པར་དུ་ཡི་དམ་གྱི་ལྷའི་དབང་བསྐུར་བ་དང་། བུམ་པའི་དབང་བསྐུར་བ་ནས་བརྩམས་ནས་རྗེས་སུ་གནང་བ་ཐུན་མོང་དང་ཁྱད་པར་དང་། དབུགས་དབྱུང་བ་དང་ལུང་བསྟན་པ་རྣམས་མཐུན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 3201 [HEADING]]
###### ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་བསྐུར་བ། ^2-5-2-3-1-0

[Block 3202]
དེ་ནས་ཁྱད་པར་གྱི་དབང་བསྐུར་བ༌[^1303]ནི་གསང་བའི་དབང་སྔོན་དུ་སོང་བས་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་བསྐུར་བ་ལ་གཉིས་ཏེ་ཆགས་ཅན་གྱི་དབང་བསྐུར་བ་དང་ཆགས་བྲལ་གྱི་དབང་བསྐུར་ལུགས་སོ། །

[Block 3203 [HEADING]]
###### **དང་པོ་ཆགས་ཅན་གྱི་དབང་བསྐུར་བ།** ^2-5-2-3-1-1-0

[Block 3204]
དང་པོ་བཤད་པ།

[Block 3205 [VERSE]]
བཅུ་གཉིས་བརྒྱད་གཉིས་ལོན་པ་ཡི། །
རིག་མ་བདེ་ཆེན་བརྒྱད་པོ་ཉིད། །

[Block 3206]
ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་ན་ཚོད་ཀྱི་ཡོན་ཏན་དང་། རིགས་ཀྱི་ཡོན་ཏན་དང་། སྦྱངས་པའི་ཡོན་ཏན་ལ་སོགས་པ་ནི་སྔ་མ་དང་འདྲ་བར་གཞུག་གོ། །

[Block 3207]
མ་དང་སྲིང་མོ་ཉིད་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྒྲ་ཇི་བཞིན་མ་ཡིན་པ་སྟེ་སློབ་དཔོན་གྱི་དབང་ནོད་པ་དང་། རང་དང་ལྷན་ཅིག་དབང་མནོས་པ་དང་། རང་གིས་བུམ་པའི་དབང་བསྐུར་བ་བྱས་པ་དང་། དེ་ལ་སོགས་པ་ཆོས་ཀྱིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 3208]
དམ་དུ་འཁྱུད་དང་འོ་བྱེད་པ། །ལ་སོགས་པ་ནས། དེ་ལ་རྩེད་མོ་རྩེ་བར་བྱ། །ཞེས་བྱ་བའི་བར་དུ་ནི་ཐུན་ཚོད་དང་པོའོ། །

[Block 3209]
དེ་ནས་ཐུན་ཚོད་གཉིས་པ་ལ། །ཞེས་བྱ་བ་ནས། སློབ་དཔོན་ལ་སོགས་རབ་ཕྱེ་ནས།[^1304] །ཞེས་བྱ་བའི་བར་ནི་བྱ་བའི་རིམ་པ་སྟེ་མཆོད་པ་དང་བསྟོད་པ་དང་གསོལ་བ་གདབ་པ་སྔ་མ་བཞིན་དུའོ།[^1305] །དེ་ནས་དབང་བསྐུར་བ་དངོས་ནི་དེ་ཉིད་ལ་བསྟན་པར་བྱ།

[Block 3210 [VERSE]]
དགའ་བྲལ་དང་པོ་མཆོག་མཐའ་ཅན། །
ཐམས་ཅད་རྒྱུད་དུ་སྤྲོས་པ༌[^1306]སྟེ། །
མཐའ་ཡིས་མཐའ་ཡི་ཕྱེ་བ་ཉིད། །

[Block 3211]
ཅེས་བྱ་བ་ནི་རྒྱུད་ཀྱི་རིམ་པ་དང་སྦྱར་ཏེ་བྱ་བའི་རྒྱུད་དང་སྤྱོད་པའི་རྒྱུད་དང་རྣལ་འབྱོར་རྒྱུད་དང་། རྣལ་འབྱོར་བླ་ན་མེད་པའི་རྒྱུད་དེ།

[Block 3212]
དང་པོ་རུ་བལྟ་བ་ཙམ་གྱིས་དགའ་བའི་ཡེ་ཤེས་སྦས་ཏེ་བསྟན་པའོ། །

[Block 3213]
གཉིས་པ་རུ་ལྷ་རྣམས་ཕན་ཚུན་དགོད་པ་ཙམ་གྱིས་མཆོག་དགའི་ཡེ་ཤེས་སྦས་ཏེ་བསྟན་པའོ། །

[Block 3214]
གསུམ་པར་ནི་ལྷ་དམ་ཚིག་སེམས་དཔའ་དང་། །ཡེ་ཤེས་སེམས་དཔའ་ཕྱག་རྒྱ་འཁྱུད་པ་ཙམ་གྱིས་དགའ་བྲལ་གྱི་ཡེ་ཤེས་སྦས་ཏེ་བསྟན་ཏོ། །

[Block 3215]
འདིར་ནི་ཀུན་དུ་རུའི་ལྷན་ཅིག་སྐྱེས་པའི་ཡེ་ཤེས་གཏན་ལ་ཕབ་སྟེ་བསྟན་ཏོ། །

[Block 3216 [VERSE]]
ཡང་དང་པོ་དགའ་བ་ལམ་ནས་ཞུགས་པ་ཡིན་ནོ། །
གཉིས་པ་མཆོག་དགའ་གཉེན་པོ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 3217]
གསུམ་པ་དགའ་བྲལ་གཉེན་པོར་གྱུར་པ་སྟེ་མི་མཐུན་པ་དང་བྲལ་བ་ཡིན་ནོ། །

[Block 3218]
བཞི་པ་ལྷན་ཅིག་སྐྱེས་པ་སྟེ།

[Block 3219]
གཉེན་པོ་འབའ་ཞིག་གི་ངོ་བོ་ཡིན་ནོ། །

[Block 3220 [HEADING]]
###### **ཆགས་བྲལ་གྱི་དབང་བསྐུར་བ།** ^2-5-2-3-1-2-0

[Block 3221]
དེ་ནས་ཆགས་བྲལ་གྱི་དབང་བསྐུར་བ་བསྟན་པ་ནི།

[Block 3222]
རྡོ་རྗེ་མཆོད་པས་ཡང་སྦྱར་ནས། །

[Block 3223 [VERSE]]
ལྷ་དེ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞུས་པའོ། །
བཅོམ་ལྡན་འདས་བཀའ་སྩལ་ཞེས་བྱ་བ་ནི་ལན་ཏེ།

[Block 3224 [HEADING]]
###### **དེར་ནི་ཐོག་མ་ཐ་མ་མེད།** ^2-5-2-3-1-2-1-0

[Block 3225 [VERSE]]
དེར་ནི་ཐོག་མ་ཐ་མ་མེད། །
སྲིད་མེད་མྱ་ངན་འདས་པ་མེད། །
འདི་ནི་མཆོག་ཏུ་བདེ་ཆེན་ཉིད། །
བདག་མེད་གཞན་ཡང་མེད་པ་ཉིད། །
--- END BLOCKS ---
