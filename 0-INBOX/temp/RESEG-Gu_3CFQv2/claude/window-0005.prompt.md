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
[Block 176]
ཡོན་ཏན་དུ་ལྟ་བ་ཅན་དུ་གྱུར་པ་ཞེས་བྱ་བ་ལ། ཕམ་པའི་གནས་ལྟ་བུའི་ཆོས་དེ་དག་ཉིད་ལ་འདི་དག་ནི་ཡོན་ཏན་ཡིན་ནོ་སྙམ་པའི་ངང་ཚུལ་ཅན་གང་ཡིན་པ་དེ་ནི་ཡོན་ཏན་དུ་ལྟ་བ་ཅན་ནོ། །

[Block 177]
འདི་ལྟ་སྟེ་ཕམ་པའི་ཆོས་རྣམས་བྱས་པས་དགེ་སློང་གིས་སོ་སོར་ཐར་པའི་སྡོམ་པ་གཏང་བར༌[^123]གྱུར་བ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་ཡང་དག་པར་བླངས་པ་གཏོང་བར༌[^124]མི་འགྱུར་རོ། །

[Block 178]
བྱང་ཆུབ་སེམས་དཔས༌[^125]ནི་ཡང་དག་པར་བླངས་པ་ཡོངས་སུ་བཏང་དུ་ཟིན་ཀྱང་ཚེ་འདི་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་ཡང་དག་པར་བླངས་པའི༌[^126]ཕྱིར་ནོད་པའི་སྐལ་བ་ཡོད་དེ་ཞེས་བྱ་བ་ནི་ཁྱད་པར་དེ་གཉིས་ཡོད་པ་ཁོ་ནའི་ཕྱིར་ཕམ་པའི་གནས་ལྟ་བུ་ཞེས་བྱའི༌[^127]དེ་མ་ཡིན་པར་གལ་ཏེ་རྣམ་པ་ཐམས་ཅད་དུ་འདྲ་བར་འདོད་ན་ནི་ཕམ་པའི་ཆོས་རྣམས་ཞེས་བརྗོད་པའི་རིགས་སོ། །

[Block 179]
གཞན་ཡང་ཕམ་པའི་ཆོས་གཞན་དག་ལས་ཁྱད་པར་དུ་གྱུར་པ་གསུམ་བསྟན་པའི་ཕྱིར། ཚེ་བརྗེས་སུ༌[^128]ཟིན་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^129]བརྩམས་སོ། །

[Block 180]
མཆོད་པའི་དམ་པས་ཞེས་བྱ་བ་ནི་སྒྲུབ་པའི་མཆོད་པ་ཡང་བསྡུའོ། །

[Block 181]
ཇི་སྐད་ཡོངས་སུ་བརྗོད་པའི་གཞི་ལས་བྱང་ཆུབ་སེམས་དཔའི་འདུལ་བ་དང་འགལ་བ་ཉེས་བྱས་ཀྱི་ནོངས་པ་བྱུང་སྟེ་ཞེས་བརྗོད་ལ་ལྷག་མ་ནི་དགེ་སློང་ཉེས་བྱས་འཆགས་པ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཉེས་བྱས་ཀྱི་ནོངས་པ་བྱུང་བ་དེ་བདག་གིས་བཙུན་པའི་སྤྱན་སྔར་ནོངས་པ་ལ་ནོངས་པར་མཐོལ་ལོ། །

[Block 182]
བཤགས་སོ། །

[Block 183]
བསྒྲགས་སོ། །

[Block 184]
མི་འཆབ་པོ། །མཐོལ་ཞིང་བཤགས་ཏེ་བསྒྲགས་ན་བདག་བདེ་བར་འགྱུར་གྱི་མ་མཐོལ་མ་བཤགས་མ་བསྒྲགས་ན་ནི་དེ་ལྟ་མ་ལགས་སོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 185]
ཉེས་པ་དེ་དག་མཐོང་ངམ། དེས་ཀྱང་མཐོང་ངོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 186]
ཕྱིན་ཆད་སྡོམ་པར་བྱེད་དམ། ལེགས་པར་བསྡམས་པར༌[^130]འཚལ་ལོ་ཞེས་དེ་སྐད་ལན་གཉིས་ལན་གསུམ་དུ་བརྗོད་པར་བྱའོ། །

[Block 187]
བྱང་ཆུབ་སེམས་དཔའི་ཉེས་པ་རྣམས་ནི་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོར་རིག་པར་བྱའོ། །

[Block 188]
འདི་ལྟ་སྟེ་གཞི་བསྡུ་བ་ལས་འབྱུང་བ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་རྣམ་པ་ལྔས་ཉེས་པ་རྣམས་ཆུང་ངུ་དང་། འབྲིང་དང་། ཆེན་པོར་འགྱུར་བར་རིག་པར་བྱ་སྟེ། ལྔ་གང་ཞེ་ན། ངོ་བོ་ཉིད་དང་། བྱེད་པ་དང་། བསམ་པ་དང་། གཞི༌[^131]དང་། བསྩོགས༌[^132]པའོ། །

[Block 189 [VERSE]]
དེ་ལ་ཕམ་པ་ནི༌[^133]ཉེས་པ་ཆེན་པོ་ཡིན་ནོ། །
དགེ་འདུན་ལྷག་མ་ནི་འབྲིང་ངོ་། །
དེ་མ་ཡིན་པ་ནི་ཉེས་པ་ཆུང་ངུའོ། །

[Block 190]
རྣམ་གྲངས་གཞན་ཡང་ཕམ་པ་དང་དགེ་འདུན་ལྷག་མ་རྣམས་ནི་ལྕི་བའོ། །

[Block 191 [VERSE]]
སོ་སོར་བཤགས་པར་བྱ་བ་ནི་འབྲིང་ངོ་། །
ཉེས་བྱས་ནི་ཡང་བར་རིག་པར་བྱའོ། །

[Block 192]
དེ་ལྟར་ན་ངོ་བོ་ཉིད་ཀྱིས༌[^134]ཆུང་ངུ་དང་། འབྲིང་དང་། ཆེན་པོར་འགྱུར་བར་རིག་པར་བྱའོ། །

[Block 193]
དེ་ལ་མི་ཤེས་པས་བྱས་པ་གང་ཡིན་པ་དང་བག་མེད་པས་བྱས་པ་གང་ཡིན་པ་དེ་ནི་ཉེས་པ་ཆུང་ངུ་ཡིན་ནོ། །

[Block 194]
མ་གུས་པས་བྱས་པ་གང་ཡིན་པ་དེ་ནི་ཉེས་པ་འབྲིང་ཡིན་ནོ། །

[Block 195]
ཉོན་མོངས་པ་ཤས་ཆེན་པོས་བྱས་པ་གང་ཡིན་པ་དེ་ནི་ཉེས་པ་ཆེན་པོར་རིག་པར་བྱ་སྟེ། [^135]དེ་ལྟར་ན་བྱེད་པ་ལས་ཆུང་ངུ་དང་། འབྲིང་དང་། ཆེན་པོར་འགྱུར་བར་རིག་པར་བྱའོ། །

[Block 196]
དེ་ལ་འདོད་ཆགས་དང་། ཞེ་སྡང་དང་། གཏི་མུག་གིས་ཀུན་ནས་དཀྲིས་པ་ཆུང་ངུས་བྱས་པ་གང་ཡིན་པ་དེ་ནི་ཆུང་ངུར་རིག་པར་བྱའོ། །

[Block 197]
འབྲིང་གིས་བྱས་པ་གང་ཡིན་པ་དེ་ནི་འབྲིང་ངོ་། །ཆེན་པོས་བྱས་པ་གང་ཡིན་པ་དེ་ནི་ཉེས་པ་ཆེན་པོར་རིག་པར་བྱ་སྟེ། དེ་ལྟར་ན་བསམ་པ་ལས་ཆུང་ངུ་དང་། འབྲིང་དང་ཆེན་པོར་འབྱུང་བར་རིག་པར་བྱའོ། །

[Block 198]
བསམ་པ་མཚུངས་པས་གཞི་རང་བཞིན་གཅིག་པ་ལ་བྱས་ཀྱང་ཆུང་ངུ་དང་། འབྲིང་དང་ཆེན་པོར་འགྱུར་བ་ཡང་ཡོད་པར་རིག་པར་བྱ་སྟེ། འདི་ལྟ་སྟེ་ཞེ་སྡང་དང་། གཏི་མུག་གིས་ཀུན་ནས་དཀྲིས་པ་མཚུངས་པས་བསམས༌[^136]བཞིན་དུ་དུད་འགྲོའི་སྐྱེ་གནས་སུ་གྱུར་པའི་སྲོག་ཆགས་བསད་པ་དང་། གསོད་དུ་བཅུག་པ་ནི་ལྟུང་བྱེད་དོ། །

[Block 199]
མིའམ་མིར་ཆགས་པ་བསད་པ་དང་གསོད་དུ་བཅུག་པ་ནི་ཕའམ་མ་མ་ཡིན་ན་ཕམ་པར་ནི་འགྱུར་ལ། མཚམས་མེད་པར་ནི་མི་འགྱུར་རོ། །

[Block 200]
ཞེ་སྡང་དང་། གཏི་མུག་གི༌[^137]ཀུན་ནས་དཀྲིས་པས་ཕའམ་མ་བསད་པ་དང་གསོད་དུ་བཅུག་པ་ནི་ཕམ་པར་ཡང་འགྱུར་ལ། མཚམས་མེད་པའི་ཁ་ན་མ་ཐོ་བར་ཡང་འགྱུར་བར་རིག་པར་བྱ་སྟེ། རྣམ་པ་དེ་ལྟ་བུར་གཞི་ལས་ཉེས་པ་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོར་འགྱུར་བར༌[^138]རིག་པར་བྱའོ། །

[Block 201]
དེ་ལ་འཕེལ་བ་ནི་འདི་ལྟར་འདི་ནི༌[^139]ལ་ལ་ཉེས་པ་གཅིག་ནས་གཉིས་དང་གསུམ་དང་ལྔའི་བར་དུ་བྱས་ཀྱང་ཆོས་བཞིན་དུ་ཕྱིར་འཆོས་པར་མི་བྱེད་པ་དེ་ནི་སོགས་པ་ལས་ཉེས་པ་ཆུང་ངུར་འགྱུར་བ་ཡིན་ནོ། །

[Block 202]
དེ་ཡན་ཆད་ཉེས་པ་བཅུའམ། ཉི་ཤུའམ། སུམ་ཅུ་འམ། ཡང་ན་ཤེས་པར་བྱ་ནུས་པའི་བར་དུ་བྱས་ལ་ཆོས་བཞིན་དུ་ཕྱིར་འཆོས་པར་ཡང་མི་བྱེད་པ་དེ་ནི་སོགས་པ་ལས་ཉེས་པ་འབྲིང་དུ་འགྱུར་བར་རིག་པར་བྱའོ། །

[Block 203]
ཉེས་པ་ཚད་མེད་པ་འབྱུང༌[^140]ལ་ཉེས་པ་འདི་ཙམ་ཞིག་འབྱུང་ངོ་ཞེས་ཤེས་པར་མི་ནུས་པ་གང་ཡིན་པ་དེ་ནི་སོགས་པ་ལས་ཉེས་པ་ཆེན་པོར་འགྱུར་བར༌[^141]རིག་པར་བྱའོ། །

[Block 204]
ཀུན་ནས་ཉོན་མོངས་པ་དང་། ཡང་འབྱུང་བ་པ་དང་། རིམས་ནད་དང་བཅས་པ་དང་། རྣམ་པར་སྨིན་པ་སྡུག་བསྔལ་བ་དང་། ཕྱི་མ་ལ་སྐྱེ་བ་དང་རྒ་ཤིར་འགྱུར་བའི་སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་དང་། མ་འདྲེས་པ་ཞེས་བྱ་བ་ནི༌[^142]དེ་ལ་ཚེ་འདི་ལ་ཀུན་ནས་ཉོན་མོངས་པ་ཕྱི་མ་ཕྱི་མ་གྲུབ་པའི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པ་རྣམས་སོ། །

[Block 205]
ཚེ་ཕྱི་མ་ལ་ཡང་སྲིད་པ་འགྲུབ་པའི་ཕྱིར་ཡང་འབྱུང་བ་རྣམས་སོ། །

[Block 206]
ཀུན་ནས་ཉོན་མོངས་པ་རྣམས་ཡོད་པས་ན༌[^143]རིམས་ནད་དང་བཅས་པའོ། །

[Block 207]
ཡང་འབྱུང་བ་རྣམས་ཡོད་པས་ན་རྣམ་པར་སྨིན་པ་སྡུག་བསྔལ་བའི་ཉེས་དམིགས་སུ་འགྱུར་ཏེ། ཚེ་འདི་ལ་ཉོན་མོངས་པའི་ཡོངས་སུ་གདུང་བ་རྣམས་ཀྱིས་ལུས་དང་སེམས་ཡོངས་སུ་གདུང་བ་དང་། ཚེ་ཕྱི་མ་ལ་ངན་འགྲོར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 208]
ཡང་འབྱུང་བ་པ་རྣམས་ཡོད་པས་ན་ཕྱི་མ་ལ་སྐྱེ་བ་དང་རྒ་བ་དང་འཆི་བའི་ཉེས་དམིགས་སུ་འགྱུར་ཏེ། ཡུན་རིང་པོར་རྒ་ཤི་སྐྱེད་པའི༌[^144]ཕྱིར་རོ། །

[Block 209 [HEADING]]
## དཀའ་བའི་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ། ^3-0

[Block 210]
དཀའ་བའི་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ་ནི་ཐོག་མ་ལེན་པ་དང་བསྲུང་བའི༌[^145]ཕྱིར་དཀའ་བར་བསྟན་ཏོ། །

[Block 211]
དེ་ལ་སྲུང་བ༌[^146]ནི་ཉམས་ཐག་པར་གྱུར་ཀྱང་སྲུང་བ་དང་གཏན་དུ་སྲུང་བའོ། །

[Block 212 [HEADING]]
## ཐམས་ཅད་ཀྱི་སྒོ་ནས་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ། ^4-0

[Block 213]
ཐམས་ཅད་ཀྱི་སྒོ་ནས་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ་ནི་ཚེ་འདིའི་སྦྱོར་བ་དང་། ཐོག་མ་མེད་པའི་དུས་ཀྱི་ས་བོན་དང་། འདས་པའི་ཚེ་རབས་དག་ཏུ་ཐོག་མ་མེད་པའི་དུས་ཀྱི་ས་བོན་ཡང་དག་པར་སྒྲུབ་པ་དང་། ཚུལ་ཁྲིམས་དེ་ཡང་དག་པར༌[^147]བརྟེན་ནས་འབྱུང་བ༌[^148]སྟེ། དེ༌[^149]ཕྱིར་ཐམས་ཅད་ཀྱི་སྒོར་བསྟན་ཏོ། །

[Block 214 [HEADING]]
## སྐྱེས་བུ་དམ་པའི་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ། ^5-0

[Block 215 [HEADING]]
### བདག་དང་གཞན་སྒྲུབ་པ། ^5-1-0
--- END BLOCKS ---
