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
[Block 1]
༄༅། །ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་འགྲེལ་བདུད་རྩིའི་དགའ་ཚལ་བཞུགས་སོ། །

[Block 2 [HEADING]]
## མཆོད་བརྗོད། ^I-0

[Block 3]
ཨོཾ་སྭ་སྟི།

[Block 4 [VERSE]]
ཆོས་སྐུ་ཤེས་རབ་ཕ་རོལ་ཕྱིན་མ་ཡུམ། །
ལོངས་སྐུ་དམ་ཚིག་སྒྲོལ་མ་རྣལ་འབྱོར་མ། །
སྒྱུ་འཕྲུལ་དྲྭ་བ་ཉི་ཤུ་རྩ་གཅིག་ལ། །
དད་པའི་དགའ་ཚལ་གཡོ་བས་ཕྱག་འཚལ་ལོ། །

[Block 5 [VERSE]]
གང་གི་བསྟོད་པ་ཕྱི་ནང་གསང་འགྲེལ་སོགས། །
ཉོབ་ན་ཤར་འདོན་ཉམས་ལ་མི་ཕན་པས། །
དངོས་བསྟན་ནང་ནས་གོ་བར་དཀའ་བའི་ཆ། །
སྦྱོར་དངོས་མཇུག་གི་ཚོགས་བཅས་གོ་བདེར་བཤད། །

[Block 6 [HEADING]]
## སྔོན་འགྲོ་ཚོགས་བསགས་ཀྱི་རིམ་པ། ^II-0

[Block 7 [HEADING]]
### ཚོགས་ཞིང་སྤྱན་འདྲེན་པ། ^II-1-0

[Block 8]
དེའང་རྗེ་བཙུན་སྒྲོལ་མའི་ཡོན་ཏན་གྱི་དཔངས་ལ་གོང་ནས་གོང་དུ་བསྟོད་པར་མོས་ན་སྦྱོར་དངོས་མཇུག་གསུམ་ལས། དང་པོ་སྦྱོར་བ་ཚོགས་བསགས་ཀྱི་རིམ་པ་ལ་ཚོགས་ཞིང་སྤྱན་འདྲེན་པ་ནི།

[Block 9 [VERSE]]
པོ་ཊ་ལ་ཡི་གནས་མཆོག་ནས། །
ཏཱཾ་ཡིག་ལྗང་གུ་ལས་འཁྲུངས་ཤིང་། །
ཏཱཾ་ཡིག་འོད་ཀྱིས་འགྲོ་བ་སྒྲོལ། །

[Block 10]
སྒྲོལ་མ་<small>ལྗང་མོ་</small>འཁོར་བཅས་<small>ཉི་ཤུ་རྩ་གཅིག་པོ་</small>གཤེགས་སུ་གསོལ། ། ཞེས་མདུན་མཁར་པདྨ་ཟླ་བའི་གདན་གྱི་ཚལ་དུ་བཞུགས་པར་བསམས་ཏེ།

[Block 11]
ཚོགས་བསགས་དངོས་ལ་ཡན་ལག་བདུན་ལས།

[Block 12 [HEADING]]
### ཕྱག་འཚལ་བ། ^II-2-0

[Block 13]
དང་པོ་ལུས་དཔག་ཏུ་མེད་པར་སྤྲུལ་ནས་ཕྱག་འཚལ་བ་ནི།

[Block 14 [VERSE]]
ལྷ་དང་ལྷ་མིན་ཅོད་པན་གྱིས། །
ཞབས་ཀྱི་པདྨ་ལ་བཏུད་དེ། །
ཕོངས་པ་ཀུན་ལས་སྒྲོལ་མཛད་མ། །
སྒྲོལ་མ་ཡུམ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 15 [VERSE]]
རྗེ་བཙུན་འཕགས་མ་སྒྲོལ་མ་དང་། །
ཕྱོགས་བཅུ་དུས་གསུམ་བཞུགས་པ་ཡི། །
རྒྱལ་བ་སྲས་བཅས་ཐམས་ཅད་ལ། །
ཀུན་ནས་དྭང་བས་ཕྱག་འཚལ་ལོ། །

[Block 16 [HEADING]]
### མཆོད་པ་འབུལ་བ། ^II-3-0

[Block 17]
གཉིས་པ་རྗེ་བཙུན་མ་ལ་མཆོད་པ་འབུལ་བའི་ཡན་ལག་ནི།

[Block 18 [VERSE]]
མེ་ཏོག་བདུག་སྤོས་མར་མེ་དྲི། །
ཞལ་ཟས་རོལ་མོ་ལ་སོགས་པ། །
དངོས་འབྱོར་ཡིད་ཀྱིས་སྤྲུལ་ནས་འབུལ། །
འཕགས་མའི་ཚོགས་ཀྱིས་བཞེས་སུ་གསོལ། །

[Block 19 [HEADING]]
### སྡིག་པ་བཤགས་པ། ^II-4-0

[Block 20]
གསུམ་པ་རང་གཞན་གྱི་སྡིག་པ་བཤགས་པའི་ཡན་ལག་ནི།

[Block 21 [VERSE]]
ཐོག་མ་མེད་ནས་ད་ལྟའི་བར། །
མི་དགེ་བཅུ་དང་མཚམས་མེད་ལྔ། །
སེམས་ནི་ཉོན་མོངས་དབང་གྱུར་པའི། །
སྡིག་པ་ཐམས་ཅད་བཤག་པར་བགྱི། །

[Block 22]
གསོད་རྐུ་མི་ཚངས་སྤྱོད་པའི་སྡིག་པ་གསུམ། རྫུན་དང་ཕྲ་མ་ཚིག་རྩུབ་ངག་འཁྱལ་བཞི། བརྣབ་སེམས་གནོད་སེམས་ལོག་པར་ལྟ་བ་གསུམ། བཅས་མི་དགེ་བཅུ་དང་། ། ཕ་མ་དགྲ་བཅོམ་གསོད་དང་དགེ་འདུན་དབྱེན། རྒྱལ་བའི་སྐུ་ལ་ངན་སེམས་ཁྲག་འབྱིན་པ། བཅས་མཚམས་མེད་ལྔ་ལ་སོགས།

[Block 23 [HEADING]]
### རྗེས་སུ་ཡི་རང་བ། ^II-5-0

[Block 24]
བཞི་པ་རང་གཞན་གྱིས་དགེ་བ་བསྒྲུབས་པ་ལ་རྗེས་སུ་ཡི་རང་བའི་ཡན་ལག་ནི།

[Block 25 [VERSE]]
ཉན་ཐོས་རང་རྒྱལ་བྱང་ཆུབ་སེམས། །
སོ་སོ་སྐྱེ་བོ་ལ་སོགས་པས། །
དུས་གསུམ་དགེ་བ་ཅི་བསགས་པའི། །
བསོད་ནམས་ལ་ནི་བདག་ཡི་རང་། །

[Block 26 [HEADING]]
### ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ། ^II-6-0

[Block 27]
ལྔ་པ་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་དུ་གསོལ་བའི་ཡན་ལག་ནི།

[Block 28]
སེམས་ཅན་རྣམས་ཀྱི་བསམ་པ་དང་། ། བློ་ཡི་བྱེ་བྲག་ཇི་ལྟ་བར། །

[Block 29]
<small>ཐེག་པ་</small>ཆེ<small>ན་པོ་བྱང་སེམས་ཀྱི་ཐེག་པ་མདོ་སྔགས་གཉིས་དང་</small>ཆུང་<small>ངུ་ཉན་རང་གཉིས་ཀྱི་ཐེག་པ་གཉིས་དང་</small>ཐུན་མོང་<small>བ་མཐོ་རིས་ལྷ་མི་གཉིས་ཀྱི་</small>ཐེག་པ་ཡི། ། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་དུ་གསོལ། །

[Block 30]
དྲུག་པ་སྐུ་མྱ་ངན་ལས་མི་འདའ་བར་གསོལ་བ་འདེབས་པའི་ཡན་ལག་ནི།

[Block 31 [VERSE]]
འཁོར་བ་ཇི་སྲིད་མ་སྟོངས་བར། །
མྱ་ངན་མི་འདའ་ཐུགས་རྗེ་ཡིས། །
སྡུག་བསྔལ་རྒྱ་མཚོར་བྱིང་བ་ཡི། །
སེམས་ཅན་རྣམས་ལ་གཟིགས་སུ་གསོལ། །

[Block 32 [HEADING]]
### བསྔོ་སྨོན། ^II-8-0

[Block 33]
བདུན་པ་བསྔོ་སྨོན་ཡན་ལག་ནི། དེའང་ཡན་ལག་དང་པོ་གཉིས་ཀྱི་སྒོ་ནས་ཚོགས་བསགས། གསུམ་པས་སྡིག་སྒྲིབ་སྦྱངས། ལྷག་མ་གསུམ་གྱིས་གོང་དུ་སྤེལ་བ་བཅས་བསགས་སྦྱངས་སྤེལ་གསུམ་གྱི་དགེ་བ་ཐམས་ཅད་མཐར་ཐུག་རྗེ་བཙུན་མ་དང་ཐུགས་ཡིད་གཅིག་ཏུ་འདྲེས་པའི་བྱང་ཆུབ་ཐོབ་ནས། གནས་སྐབས་ཁྱེད་དང་ལྷན་ཅིག་ཏུ་གཞན་དོན་འགྲུབ་པའི་སྨོན་ལམ་ནི། བདག་གིས་བསོད་ནམས་ཅི་བསགས་པ། ། ཐམས་ཅད་<small>རྗེ་བཙུན་མ་དང་ཐུགས་ཡིད་གཅིག་ཏུ་འདྲེས་པའི་</small>བྱང་ཆུབ་རྒྱུར་གྱུར་ནས། ། རིང་པོར་མི་ཐོགས་འགྲོ་བ་ཡི། ། འདྲེན་པའི་དཔལ་དུ་<small>རྗེ་བཙུན་མ་ཁྱེད་དང་ལྷན་ཅིག་ཏུ་</small>བདག་གྱུར་ཅིག ། དེ་ལྟར་ཕྱག་གཅིག་འཚལ་ན་རང་ལུས་ཀྱི་ཁ་འོག་ཏུ་ཆུད་པའི་དབང་ཆེན་གསེར་གྱི་ས་གཞི་ཡན་ཆད་ཀྱི་རྡུལ་ཕྲན་ཇི་སྙེད་ཡོད་པ་དེ་སྙེད་འཁོར་ལོས་བསྒྱུར་བའི་རྒྱལ་སྲིད་ཐོབ་པའི་ཕན་ཡོན་ཡོད་པར་མདོ་ལས་གསུངས་ཤིང་ཡན་ལག་ལྷག་མ་རྣམས་ཀྱང་གོང་ནས་གོང་དུ་བརྒྱ་འགྱུར་གྱིས་ཕན་ཡོན་ཆེ་བར་བཤད་པས་ཚོགས་མྱུར་དུ་རྫོགས་ཐབས་ལ་ཡན་ལག་བདུན་པ་འདི་གལ་ཆེའོ། །ཞེས་སྔོན་འགྲོ་ཚོགས་བསགས་ཀྱི་རིམ་པ་སོང༌།

[Block 34 [HEADING]]
## བསྟོད་པ་དངོས། ^1-0

[Block 35]
གཉིས་པ་སྒྲོལ་མའི་རྒྱུད་ལས་ཁོལ་དུ་ཕྱུང་བའི་བསྟོད་པའི་ཚིག་བྱིན་རླབས་ཀྱི་སྤྲིན་ཆར་གཡོ་བས་བསྟོད་པ་དངོས་ཀྱི་ཚིག་དོན་དྲན་བཞིན་དུ་དད་གུས་མིག་ནས་ཟིལ་པ་འཁྲུགས་ལུས་ནས་བ་སྤུ་གཡོ་བའི་ཀློང་ནས་དཔག་མེད་བཞི་ལྡན་གྱི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 36]
དང་པོ་མཚན་རྒྱ་གར་སཾ་སྐྲྀ་ཏའི་སྐད་དུ་སྨོས་ན། ན་མཿཏཱ་ར་ཨེ་ཀ་བིམ་ཤ་ཏི་སྟོ་ཏྲ་གུ་ཎ་ཧི་ཏ་ས་ཀ

[Block 37]
གཉིས་པ་བོད་སྐད་དུ་སྨོས་ན། སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ་ཕན་ཡོན་དང་བཅས་པ།

[Block 38]
གསུམ་པ་སྐད་གཉིས་ཤན་སྦྱར་དུ་སྨོས་ན། ན་མཿནི་ཕྱག་འཚལ། ཏཱ་ར་ནི་སྒྲོལ་མ། ཨེ་ཀ་བིཾ་ཤ་ཏི་ནི་ཉི་ཤུ་རྩ་གཅིག་གིས། སྟོ་ཏྲ་ནི་བསྟོད་པ། གུ་ཎ་ཧི་ཏ་ས་ཀ་ནི་ཕན་ཡོན་དང་བཅས་པའོ། །

[Block 39]
བཞི་པ་མཚན་དོན་དངོས་བསྟན་ལྟར་གོ་སླའོ། །

[Block 40]
ཨོཾ་ནི་མགོ་འདྲེན། རྒྱལ་བ་ཀུན་གྱི་ཡུམ་མཆོག་ཏུ་གྱུར་པས་རྗེ་བཙུན་མ་སོ་སོའི་སྐྱེ་བོའི་ས་ལས་འཕགས་པས་ན་འཕགས་མ་དད་པ་ཅན་འཁོར་བ་དང་ངན་སོང་དང་འཇིགས་པ་ལས་སྒྲོལ་བས་སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ལོ། །ཞེས་ལོ་ཙཱ་བའི་འགྱུར་ཕྱག་ཡིན། ཕྱག་གང་ལ་འཚལ་ན་ཏཱ་རེ་ནི་སྒྲོལ་མ། སྐད་ཅིག་དང་ཉི་མ་གཅིག་གིས་ཀྱང་འགྲུབ་པས་ལྷ་གཞན་ལས་ཕྲིན་ལས་མྱུར་མ་བར་ཆད་མྱུར་དུ་ཟློག་པས་དཔའ་མོ། ཏུཏྟཱ་རེ་ཡིས་འཇིགས་པ་སེལ་མ། ཏུ་རེས་རང་དོན་གཞན་དོན་གཏན་དོན་ཀུན་སྦྱིན་པའི་སྒྲོལ་མ། སྭཱ་ཧུའི་ཡི་གེ་ནི་ཁྱོད་ལ་འདུད་དོ། །
--- END BLOCKS ---
