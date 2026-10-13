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
[Block 141]
དང་པོ་ནི། སྟོང་པ་ཉིད་དང་། མཚན་མ་མེད་པ་དང་། སྨོན་པ་མེད་པའི་དེ་ཁོ་ན་ཉིད་གསུམ་ལ། གདུལ་བྱའི་སེམས་ཉིད་ཡང་དག་པར་བཀོད་པས།

[Block 142]
དེའི་མཐུ་ལས།

[Block 143]
སྒྲིབ་པ་ཐམས་ཅད་སྤངས་ཏེ། ཞི་བ་ལ་འགོད་པ་སྟེ། གདུལ་བྱ་སྨིན་གྲོལ་དུ་བྱེད་པའི་མཐུ་དང་ཡང་དག་པར་ལྡན་མའོ། །

[Block 144]
གདོན་ནི་ནམ་གུའི་གདོན་ལ་སོགས་པ་གདོན་བཅོ་བརྒྱད་རྣམས་སོ། །

[Block 145]
རོ་ལངས་ནི་རོ་ལངས་ཀྱི་ལས་ཏེ་སྤོང་གཏོང་ལ་སོགས་པའི་ངན་སྔགས་རྣམས་སོ། །

[Block 146]
གནོད་སྦྱིན་ནི་མདངས་འཕྲོག་པ་རྣམས་ཀྱི་གནོད་པ་སྟེ། དེ་ལྟ་བུའི་གནོད་པ་ཐམས་ཅད་ཀྱང་། རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་གྱིས་འཇོམས་པ་ཉིད་དུ་བྱེད་ཅིང་། རབ་མཆོག་ཏུ་རེ་ཞེས་པའི་སྔགས་ཀྱི་མཐུ་ལས་ཀྱང་དེ་ལྟར་བྱེད་པ་ཉིད་དོ། །

[Block 147]
ཡང་ན་ཏུ་རེ་ནི་མྱུར་མ་སྟེ། རབ་མཆོག་ལྷ་མོ་ཁྱོད་ཀྱིས་གནོད་པ་ཐམས་ཅད་མྱུར་དུ་འཇོམས་པ་ཉིད་དོ། །ཅེས་པའི་དོན་དུའང་འགྱུར་པས། མྱུར་དུ་འཇོམས་པའི་མཆོག་རབ་ཉིད་མ་ཞེས་བཅོས་ན་བདེའོ། །

[Block 148]
གཉིས་པ་སྤྱིའི་དོན་ནི། སྒྲོལ་མའི་སྐུར་བསྐྱེད་པའི་བསམ་གཏན་ལ། གནས་གསུམ་དུ་ཡི་གེ་འབྲུ་གསུམ་གྱི་དེ་ཉིད་བཀོད་པས། ཞི་བ་སྟེ་བར་ཆད་སྲུང་བའི་མཆོག་ཏུ་འགྱུར་བ་དང་། གདོན་གྱི་གནོད་པ་ལ་སོགས་པ་སྲུང་བའི་མན་ངག་ཀྱང་སྟོན་ནོ། །

[Block 149]
གསུམ་པ་སྦས་དོན་ནི། དེ་ཉིད་གསུམ་སྣང་བ་དང་མཆེད་པ་དང་། ཉེ་བར་ཐོབ་པའོ། །

[Block 150]
དེ་དག་བཀོད་པ་དེ་རིམ་གྱི་ཤར་ནས། ཞི་བ་སྟེ་སྐད་ཅིག་པ་ཞི་བ་ཐམས་ཅད་སྟོང་པ་འོད་གསལ་བ་ཉེ་བར་འགྲོའོ། །

[Block 151]
གདོན་ཏེ་རྩ་དང་། རོ་ལངས་ཏེ་ཐིག་ལེ་དང་།

[Block 152]
གནོད་སྦྱིན་ཏེ་རྣམ་པར་རྟོག་པ་རྣམས་འོད་གསལ་གྱི་དབྱིངས་སུ་བཅོམ་པ་ལས།

[Block 153]
རབ་མཆོག་སྟེ་ལྷའི་སྐུར་མྱུར་དུ་བཞེངས་པའོ། །

[Block 154]
འདི་ལྟ་བུའི་རིགས་ནི།

[Block 155]
སྒྲོན་གསལ་ལས།

[Block 156 [VERSE]]
འོད་གསལ་ནི་རབ་སྟོན་དང་། །
ཟུང་དུ་འཇུག་པ་རབ་རྟོགས་བྱེད། །
རྣམ་པ་གཉིས་སུ་མཐའ་བཤད་དོ། །
མཐའ་ནི་མུར་ཐུག་པ་ཡི་ཚིག །

[Block 157]
ཅེས་གསང་འདུས་འཕགས་སྐོར་བ་རྣམས་ཀྱི་རང་ལུགས་ལ། མཐར་ཐུག་གི་བཤད་པ་འདོད་ཀྱང་། སྤྱིར་ནས་སྦས་དོན་ཡང་ཡོད་པར་ཤེས་པར་བྱའོ། །

[Block 158]
བཞི་པ་མཐར་ཐུག་ནི། སྐུ་དང་གསུང་དང་ཐུགས་རྡོ་རྗེ་འདི་ཉིད་གསུམ་ནི། ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་དུ་གདོད་མ་ནས་བཀོད་པ་ཡིན་ལ། རང་བཞིན་གདོད་མ་ནས་རྣམ་པར་དག་པ་དེའི་ཕྱིར། ལམ་སྒོམས་པས་ཀྱང་ཞི་བ་ཐོབ་པའི་མཐུ་དང་ཡང་དག་པར་ལྡན་པ་དང་། རྡོ་རྗེ་གསུམ་དབྱེར་མེད་པའི་དབྱིངས་དེ་ཉིད་ལ་མཉམ་པར་བཞག་པས། གདོན་གྱི་གནོད་པ་དང་མཚུངས་པའི་སྡུག་བསྔལ་དང་། རོ་ལངས་ཀྱི་ལས་དང་མཚུངས་པའི་ལས་དང་། གནོད་སྦྱིན་དང་མཚུངས་པའི་ཉོན་མོངས་པ་རྣམས་མྱུར་དུ་བཅོམ་ནས། རབ་མཆོག་སྟེ་བདེ་ཆེན་ལྷན་ཅིག་སྐྱེས་པའི་ཡེ་ཤེས་གཅིག་པུར་བྱེད་དོ། ། ཅེས་པའི་དོན་ནོ། །

[Block 159]
དེ་ལྟར་ན་རྒྱས་བཤད་སྒྲ་ཇི་བཞིན་པའི་ཚིག་འདི་རྣམས་ཀྱིས། བཅོམ་ལྡན་འདས་མ་སྤྲུལ་པའི་སྐུ། སངས་རྒྱས་རྣམས་ཀྱི་འཁོར་གྱི་དཀྱིལ་འཁོར་དུ་སྟོན་པར་མཛད་པ། ལྷའི་རྒྱལ་པོ་རྣམས་ཀྱི་གནས་དང་། རི་བོ་ཏ་ལ་ལ་སོགས་པར་མངོན་སུམ་དུ་བཞུགས་པར་གྲགས་པ་འདིའི་དབང་དུ་བྱས་པའི་བསྟོད་པ་ཡིན་ལ། དོན་གྱི་ན་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་དང་ཆོས་ཀྱི་སྐུ་ལ་ཡང་བསྟོད་པའོ། །

[Block 160]
ངེས་དོན་འདི་རྣམས་ནི། ཟབ་ལམ་མཐར་ཐུག་རྡོ་རྗེའི་རྣལ་འབྱོར་ཡན་ལག་དྲུག་པ་དང་བསྟུན་ནས་བཤད་པ་སྟེ། དེ་ཡང་སྒྲོལ་མ་འབྱུང་བའི་རྒྱུད་ཀྱི་མཚན་ངེས་པའི་སྒོས་ཀྱི་འགྲེལ་པ་རྒྱ་གར་མཁས་པས་སྦྱར་བ་གཉིས་དང་། མར་མེ་མཛད་དཔལ་གྱི་རྒྱུད་འགྲེལ་ཆེན་མོའི་ནང་ནས་འབྱུང་བ་རྣམས་དང་མཐུན་པར་ཕལ་ཆེར་བཤད་པ་ཡིན་ལ། དེ་དག་ལས་རྡོ་རྗེའི་རྣལ་འབྱོར་གྱི་མན་ངག་དག་མི་མཐུན་པ་ཅུང་ཟད་ཡོད་པ་རྣམས་ནི། རྒྱུད་ཀྱི་ཟབ་དོན་མཐར་ཐུག་ལས་བརྩམ་ནས། རྒྱུད་ནི་རྒྱུད་གཞན་གྱིས་རྟོགས་དགོས་པར་གསུངས་པ་ལྟར། བདག་གིས་རྡོ་རྗེའི་རྣལ་འབྱོར་དང་མཐུན་པར་བཀྲལ་ལོ། །

[Block 161]
གཞན་ཡང་ཉེ་བར་མཁོ་བའི་རྣམ་གྲངས་འདི་ལྟ་བུ་དག་ཀྱང་ཡོད་དེ། སྟོན་ཀའི་ཟླ་བ་སོགས་ཀྱིས་ཟླ་བ་དང་ས་བོན་ལས་བསྐྱེད་པ་དང་། ཉི་མ་ཟླ་བ་རྒྱས་པ་སོགས་ཀྱིས་མངོན་བྱང་ལྔ་ལས་བསྐྱེད་པ་དང་། དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར་ཞེས་པས་ལྷ་དབང་བསྐུར་བ་དང་། འཇིག་རྟེན་གསུམ་མགོན་སོགས་ཀྱིས་ཆོ་ག་གསུམ་བསྐྱེད་དང་། དེ་ཉིད་གསུམ་སོགས་ཀྱིས་རྡོ་རྗེ་གསུམ་བྱིན་གྱིས་རློབ་པ་དང་། ཀུན་ནས་གོ་ཆ་སོགས་ཀྱིས་སྐྱེ་མཆེད་རྣམས་བྱིན་གྱིས་རློབ་པ་དང་། ཀུན་ནས་སྐོར་རབ་དགའ་བ་དང་། གཡས་བརྐྱང་གཡོན་བསྐུམ་ཀུན་ནས་སྐོར་དགའི་ཞེས་པས་འཁོར་གྱི་ལྷ་ཚོགས་ཏེ། བསྐྱེད་རིམ་གྱི་ཕྱོགས་དང་། ཉི་མ་ཟླ་བ་རྒྱས་པའི་སོགས་ཀྱིས་ཆོ་ག་དང་། རྡུལ་ཚོན་སོགས་ལ་མིག་གིས་བལྟ་བ་བྱིན་གྱིས་རློབ་པ་དང་། དབུ་རྒྱན་འོད་ཀྱི་ཕྲེང་བ་སྤེལ་མ་ཞེས་པས། ཅོད་པན་གྱི་དབང་བསྐུར་པ་ལ་སོགས་པ་དང་། ཡི་གེ་ཧཱུྃ་གི་ཞེས་པས་སྔགས་ཀྱི་དབང་བསྐུར་བ་དང་། ཟླ་བའི་རྩེ་མོས་དབུ་བརྒྱན་གྱིས་གསང་དབང་དང་། རལ་པའི་ཁྲོད་ལས་འོད་དཔག་མེད་ཀྱིས་ཤེར་དབང་དང་། བདེ་མ་དགེ་མ་སོགས་ཀྱིས་དབང་བཞི་པ་ཡང་བསྟན་ཏེ། དབང་གི་དོན་ནོ། །

[Block 162]
མེ་འབར་འཁྲུགས་མ་ཞེས་པ་དང་། འབར་བའི་ཕྲེང་བ་ཞེས་པ་དང་། འོད་རབ་འབར་མ་ཞེས་པ་དང་། སྒྲོན་མ་ཉིད་མ་ཞེས་པ་རྣམས་ཀྱིས། ལས་བཞི་དང་དངོས་གྲུབ་སྒྲུབ་པའི་བསྲེག་བླུགས་ཀྱང་བསྟན་ཞིང་། དབང་བསྐུར་བས་ན་རབ་ཏུ་གནས་པའང་བསྟན་པ་ཡིན་ནོ། །

[Block 163]
གཞན་ཡང་སྒྲོན་མ་ཉིན་ཞི་མཚན་ཁྲོར་གྲགས་པའི་སྒྲུབ་ཐབས་ཀྱང་གཞུང་འདིས་ཤིན་ཏུ་གསལ་བར་བསྟན་ཞིང་། སྒྲུབ་ཐབས་ཉེར་གཅིག་དང་ལས་ཚོགས་ཉེར་གཅིག་བསྟན་པ་ཤིན་ཏུ་གྲགས་ཆེ་བ་རྣམས་ཀྱང་ཡིན་ཏེ། ཧ་ཅང་མང་བར་འགྱུར་བས་མ་སྤྲོས་སོ། །

[Block 164 [HEADING]]
## ཕན་ཡོན། ^2-0

[Block 165]
འཇུག་གི་དོན་ལ་དེའི་འོག་ཏུ་བསྟོད་པའི་ཕན་ཡོན་བསྟན་པ་ཡིན་ཏེ།

[Block 166]
དེ་ལ་དང་པོར་རྩ་བའི་སྔགས་ཀྱི་སོགས་ཤྭ་ལོ་ཀ་གཉིས་ལས།

[Block 167]
རྩ་སྔགས་ཀྱི་ཡི་གེ་བཅུ་པའི་སོ་ནས་བསྟོད་པ་དེ་འདི་ཉིད་ཡིན་པ་དང་། ཕྱག་འཚལ་ལོ་ཞེས་པ་ཉི་ཤུ་རྩ་གཅིག་དང་ལྡན་པའི་བསྟོད་པ་ཡང་འདི་ཡིན་ནོ་ཞེས་པ་དེས་ན་དང་ཞེས་པ་སྡུད་པའི་ཚིག་གོ། །

[Block 168]
དེ་ལ་རྩ་བའི་སྔགས་ཀྱི་དོན་ནི། ཨོཾ་ཞེས་བྱ་བ་མཆོག་གི་ཚངས་པ། ཆོས་ཀྱི་དབྱིངས་ཆོས་ཀྱི་སྐུ། ཡོན་ཏན་མཐའ་དག་གི་ནོར་བུ་འཛིན་པ། བདེ་བར་གཤེགས་པའི་སྙིང་པོ་ཆོས་ཀྱི་མཆོག་གོ། །

[Block 169]
ཆོས་ཀྱི་སྐུ་ལས་བྱུང་བའི་ཡེ་ཤེས་ནི་ཏཱ་རེ། གདོད་མའི་ཆོས་ལས་བྱུང་བའི་སྐུ་ནི་ཏུཏྟཱ་རེ། བརྗོད་དུ་མེད་པའི་ཆོས་ལས་བྱུང་བ་སྙིང་རྗེ་ཆེན་པོ་ནི་ཏུ་རེ་སྟེ་སྤྲུལ་པ་དང་མཛད་པའོ། །

[Block 170]
སྭཱ་ནི་རང་བྱིན་གྱིས་བརླབས་པ། ཧཱ་ནི་ཧ་ལས་ཨཱ་ར་ལི་སྟེ། ཨེ་མ་ཧོ་རོལ་པ་སྟེ། སྒྱུ་མ་ལྟ་བུའི་སྐུ་དང་ཞིང་ཁམས་དང་མཛད་པ་མཐའ་ཡས་པའོ། །

[Block 171]
དོན་དེ་རྣམས་ཀྱིས་སྒོ་ནས་བསྟོད་པའི་ཕྱིར་རྩ་བའི་སྔགས་ཀྱིས་བསྟོད་པའོ། །

[Block 172]
ལས་སུ་བྱ་བ་བསྟོད་པའི་ཡུལ་ལྷ་མོ་སྟེ་བཅོམ་ལྡན་འདས་མ་ལའོ། །

[Block 173]
བྱེད་པ་ནི་གུས་པ་ཡང་དག་པར་ལྡན་པས་སོ། །

[Block 174]
བྱེད་པ་པོ་བློ་ལྡན་གང་གིས་སོ། །

[Block 175]
ཚུལ་ཇི་ལྟར་ན། འདིར་རབ་ཏུ་དང་ཞིང་བརྩོན་འགུས་དང་ལྡན་པས་ཏེ། བསྟོད་པ་འདི་བརྗོད་པ་དང་། སྲོད་དང་ཐོ་རངས་ལངས་པ་སྟེ་ལྡང་བ་ཡང་བར་བྱས་ནས། ཕྱག་འཚལ་བ་དང་མཆོད་པ་སྔོན་དུ་འགྲོ་བས། འཕགས་མའི་ཡོན་ཏན་ཡིད་ལ་དྲན་པས་སོ། །

[Block 176]
དེའི་ཕན་ཡོན་ནི་མི་འཇིགས་པ་ཐམས་ཅད་རབ་ཏུ་སྟེར་བ་སྟེ། འཇིགས་པ་ཆེན་པོ་བརྒྱད་དང་བཅུ་དྲུག་ལ་སོགས་པ་འཇིགས་པ་ཐམས་ཅད་ལས་སྐྱོབ་པ་དང་། མི་འཇིགས་པའི་གནས་དབང་ཕྱུག་ཕུན་སུམ་ཚོགས་པ་སྩོལ་བར་མཛད་པའོ། །

[Block 177]
འདིར་རབ་དང་བརྗོད་ཅིང་ཞེས་པ་ལ། རྒྱ་སྐད་དུ་བ་ཞེས་པ་ཡོད་བས་བརྩོན་པས་ཀློག་ཅིང་ཞེས་བརྗོད་ན་བདེའོ། །

[Block 178]
དེ་བས་ན་བློ་ལྡན་གང་གིས་སྲོང་སོགས་ཐུན་དྲུག་ཏུ་ལྷ་མོ་ལ་གུས་ཤིང་ཡོན་ཏན་དྲན་པའི་སྒོ་ནས། བརྩོན་པས་བསྟོད་པ་འདི་བཀླགས་ན། ཕན་ཡོན་འདི་དག་ཡོད་དོ་ཞེས་པ་སྟེ་གོང་འོག་ཐམས་ཅད་དུ་དེ་ལྟར་གོ་བར་བྱའོ། །

[Block 179]
སྡིག་པ་ནི་སྡིག་པའི་འབྲས་བུ་སྟེ། ནད་དང་གདོན་དང་། བྱུར་ཆགས་སྐལ་བ་ངན་པ་སྔར་ཡོད་རྣམས་ཐམས་ཅད་རབ་ཏུ་ཞི་ཞིང་སླར་འབྱུང་བར་འགྱུར་བ་རྣམས་བཟློག་པའོ། །

[Block 180]
དེ་བཞིན་དུ་སྔར་སྡིག་པའི་ལས་ཀྱི་མཐུས། ངན་འགྲོར་སྐྱེ་ངེས་པའི་ལས་ཅན་ཡིན་ཡང་། བསྟོད་པ་བཀླགས་པའི་གཟི་བརྗིད་ཀྱིས་སྡིག་ལས་ཟང་དེ་ངན་འགྲོའི་སྐྱེ་བ་ཐམས་ཅད་འཇོམས་པའི་གནས་སྐབས་ཐོབ་པ་ཉིད་དེ། ངན་འགྲོར་སྐྱེ་བར་མི་འགྱུར་རོ། །
--- END BLOCKS ---
