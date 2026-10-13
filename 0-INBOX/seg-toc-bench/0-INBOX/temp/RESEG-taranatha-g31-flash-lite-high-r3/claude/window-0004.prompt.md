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
[Block 141 [HEADING]]
#### སྦས་དོན། ^1-17-2-0

[Block 142]
སྦས་དོན་ནི། རི་རབ་ནི་ཚངས་པའི་རུས་པ། རི་གཞན་གཉིས་ནི་ཡིད་བཟང་མ་དང་དུང་ཅན་མ། གཡོ་བ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་ཡོངས་སུ་གང་བ། འཇིག་རྟེན་གསུམ་ནི་སྟེང་འོག་གི་དབྱེ་བས་རྩ་གསུམ་གསུམ་དྲུག་གོ། །

[Block 143]
ཧཱུྃ་གི་བརྡས་ནི། ཐུགས་རྡོ་རྗེའི་རྩ་ཨ་ཝ་དྷཱུ་ཏི་སྟེ་རྩ་ཐམས་ཅད་ཀྱི་ས་བོན་ནུས་པ་དེར་ཐིམ་པའོ། །

[Block 144 [HEADING]]
### ཕྱག་འཚལ་བཅོ་བརྒྱད་པ། ^1-18-0

[Block 145 [HEADING]]
#### ཚིག་འགྲེལ། ^1-18-1-0

[Block 146]
ཚིགས་བཅད་བཅོ་བརྒྱད་པ་ཕྱག་འཚལ་ལྷའི་སོགས་ལ། ལྷའི་མཚོ་སྟེ། ཡིད་ཀྱི་མཚོའམ་རིང་བུ་དལ་གྱིས་འབབ་པ་དང་འདྲ་བའི་རྣམ་པ་ཅན་ནི། དཀར་ཞིང་ཟླུམ་པའི་རི་དྭགས་རྟགས་ཅན་ཏེ་ཟླ་བ་ཕྱག་ན་བསྣམས་པ་དང་། དེའི་རིག་སྔགས་ཧ་ར་ཞེས་པ་ལན་གཉིས་བརྗོད་ཅིང་། མཐའ་བརྟེན་ཕཊ་ཀྱི་ཡི་གེ་དང་བཅས་པའི་སྔགས་ཀྱིས་བརྟན་པ་དང་གཡོ་བའི་དུག་མ་ལུས་པ་སེལ་བར་བྱེད་དོ། །

[Block 147]
འདིས་ནི་ཟླ་བ་འཛིན་པའི་སྐུ་སྒོམས་ཏེ། སྔགས་ཀྱི་ཁྱད་པར་དེ་བཟླས་པས་སྤྲུལ་ལ་སོགས་པའི་དུག་གསོ་བ་དང་སེལ་བར་བྱེད་དོ། །

[Block 148]
ཧ་ར་ལན་གཉིས་བརྗོད་པའི་སྔགས་ནི། ཨོཾ་ན་མཿཏཱ་རེ་ན་མོ་ཧ་རེ་ཧཱུྃ་ཧ་རེ་སྭཱ་ཧཱ། ཞེས་པ་ཡིན་ལ་དེའི་མཐར་སརྦ་བི་ཛཿ ཤནིཾ་ཀུ་རུ་ཕུཊ་ཅེས་བཏགས་པ་ནི་དུག་སེལ་བ་སྟེ་སྒྲོལ་མ་ཁྲོ་མོའི་ལས་སྔགས་སོ། །ཞེས་པ་ནི་རྗེས་འཇུག་གི་གདོན་ནོ། །

[Block 149 [HEADING]]
#### ངེས་དོན། ^1-18-2-0

[Block 150]
ངེས་པའི་དོན་དུ་ནི། ལྷ་ནི་ལུས་ལས་བྱུང་བ་སྟེ། དེའི་མཚོ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་བདེ་བ་རྟེན་ཀུན་དང་བཅས་པ་ཡིན་ལ། དེ་དང་དབྱེར་མེད་པའི་སྟོང་པ་ཉིད་ཀྱི་ཡེ་ཤེས་ཟླ་བ་ལྟར་དྲི་མ་མེད་པ། གང་ལ་མངའ་བ་ནི་དེའི་ཕྱག་ན་བསྣམས་པའི་དོན་ནོ། །

[Block 151]
དེ་འདྲ་བའི་བདེ་སྟོང་གཉིས་སུ་མེད་པ་དེས་ནི། ཧ་ར་ཏེ་འཕྲོག་པ། ལན་གཉིས་བརྗོད་པའི་བརྡས་སྒྲིབ་པ་གཉིས་ཀྱི་ཉེས་སྐྱོན་འཕྲོག་ཅིང་། མ་དག་པའི་ལུས་ཀྱིས་དུག་འཇོམས་པར་བྱེད་དོ། །

[Block 152 [HEADING]]
### ཕྱག་འཚལ་བཅུ་དགུ་པ། ^1-19-0

[Block 153 [HEADING]]
#### ཚིག་འགྲེལ། ^1-19-1-0

[Block 154]
ཚིགས་བཅད་བཅུ་དགུ་པ་ཕྱག་འཚལ་ལྷའི་ཚོགས་རྣམས་སོགས་ལ། ལྷའི་ཚོགས་པ་སྟེ་འདོད་པའི་ཁམས་ཀྱི་ལྷ་རིགས་དྲུག་པོ་རྣམས་ཡིན་ལ། དེ་བཞིན་དུ་རྒྱལ་པོ་ནི་འཇིག་རྟེན་འདི་ན་དབང་བསྒྱུར་པ་པོ་འཁོར་ལོས་སྒྱུར་བ་ལ་སོགས་པའི་རྒྱལ་པོ་རྣམས་སོ། །

[Block 155]
འཇིག་རྟེན་དུ་ཕན་གནོད་བྱེད་པ་རིའི་ལྷ་དང་ཤིང་གི་ལྷ་དང་། མཚོའི་ལྷ་མོ་ལ་སོགས་པ་ནི་ལྷའི་ཁྱད་པར་ཏེ། དེ་རྣམས་དང་མིའམ་ཅི་དབང་ཆེ་བ་རྣམས་ཀྱིས་ཁྱོད་ཀྱི་ཞབས་ཀྱི་པདྨོ་ལ་གུས་པས་བརྟེན་པ་ཡིན་ལ། ལྷ་མོ་ཁྱོད་ཀྱིས་བྱིན་གྱིས་བརླབས་པའི་སྔགས་དང་ཕྱག་རྒྱའི་གོ་ཆ་དགའ་བ་དང་བདེ་བའི་རྒྱུ་དེ་ཀུན་ནས་བཅིངས་པའི་སྒྲུབ་པ་པོས། ལུས་ངག་ཡིད་ཀྱི་གཟི་བརྗིད་ཀྱིས་ཕ་རོལ་པོའི་རྩོད་པ་དང་། རྨི་ལམ་ངན་པ་ལ་སོགས་པ་མི་འཚམ་པ་ཐམས་ཅད་སེལ་བར་བྱེད་མའོ། །

[Block 156]
འདིར་གོ་ཆ་ནི་བསྲུང་བའི་དོན་ནོ། །

[Block 157 [HEADING]]
#### ངེས་དོན། ^1-19-2-0

[Block 158]
ངེས་པའི་དོན་དུ། ལྷ་ནི་དེ་བའི་སྒྲ་ལས་དེ་ཧ་བྷ་བ་སྟེ་ལུས་ལས་བྱུང་བ། ཡེ་ཤེས་ཀྱི་སྐུའོ། །

[Block 159]
ཚོགས་ཞེས་སྨོས་པས་ཡེ་ཤེས་ཀྱི་སྐུ་དེ་ཡང་། ཕུང་ཁམས་བཅུ་ལ་སོགས་པ་རྣམ་དག་དུ་མ་དང་ལྡན་པའི་དོན་ནོ། །

[Block 160]
དེ་ཉིད་རིག་པ་འཛིན་པའི་རྒྱལ་པོ་ཡང་ཡིན་ལ། འཇིག་རྟེན་གསུམ་གྱི་མཆོད་འོས་ཡིན་པའི་ཕྱིར། ལྷ་དང་མིའམ་ཅི་ལ་སོགས་པས་བསྟེན་པའོ། །

[Block 161]
དེའི་རྒྱུ་ནི་ཐིག་ལེའི་ཚོགས་པ་འཕོ་མེད་དུ་བཅིངས་བའི་གོ་ཆའི་གཟི་བརྗིད་ཀྱིས། འགྱུར་བའི་ཆགས་བྲལ་རྩོད་པ་དང་། ཐ་མལ་གྱི་སྣང་བ་རྨི་ལམ་ངན་པ་བཅོམ་པའོ། །

[Block 162 [HEADING]]
### ཕྱག་འཚལ་ཉི་ཤུ་པ། ^1-20-0

[Block 163 [HEADING]]
#### ཚིག་འགྲེལ། ^1-20-1-0

[Block 164]
ཚིགས་བཅད་ཉི་ཤུ་པ་ཕྱག་འཚལ་ཉི་མ་སོགས་ལ། ཉི་མ་དང་ཟླ་བ་འོད་ཟེར་རབ་ཏུ་རྒྱས་པ་ལྟ་བུའི་སྤྱན་གཉིས་པོ་ལ་འོད་ཟེར་འབར་བ་རབ་ཏུ་གསལ་བའི་གཟིགས་པས་འགྲོ་བ་རྣམས་ལ་ཡོངས་སུ་གཟིགས་པ་ན། ངན་འགྲོ་ལ་སོགས་པ་སྡུག་བསྔལ་ཅན་གྱི་འགྲོ་བ་མཐའ་དག་བདེ་བ་ལ་འགོད་པར་མཛད་པ་སྟེ། ཧཱ་རའི་སྔགས་ལན་གཉིས་སུ་བརྗོད་པ། ཏུཏྟཱ་རེའི་སྔགས་དང་བཅས་པ་བཟླས་པ་ཡིས་ཤིན་ཏུ་དྲག་པོ་སྟེ་གསོ་བར་དཀའ་བའི་རིམས་ནད་མ་ལུས་པ་ཡང་སེལ་བར་མཛད་པའོ། །

[Block 165]
གནས་སྐབས་སུ་ཡི་གེ་བཅུ་པའི་སྔགས་ཀྱི་རིམས་ནད་ཞི་བ་དང་། ནད་ཡམས་གཅོད་པ་དང་། ནད་འགོ་བ་རྣམས་བསྲུང་བར་སྟོན་ལ། དོན་གི་གཙོ་བོ་ནི་ཡི་གེ་བཅུ་ལ་བཟླས་པས། དྲག་པོའི་རིམས་ནད་དང་འདྲ་བའི་ཉོན་མོངས་པ་མ་ལུས་པ་ཞི་བར་བྱེད་པའོ། །

[Block 166]
སྐབས་འདིར་སྤྱན་གཉིས་ཉི་ཟླ་འདྲ་བར་སྦྱར་བ་ནི། སྤྱན་གཡས་པའི་འོད་ཀྱི་ཉེ་བར་འཚེ་བ་རྣམས་སྐྲག་པར་བྱེད་ཅིང་། སྡིག་པ་དང་སྡུག་བསྔལ་བསྲེག་པར་བྱེད་པས་ཉི་མ་ལྟ་བུའི་འོད་དང་། གཡོན་པའི་འོད་ཟེར་གྱིས་ཚེ་དང་ལོངས་སྤྱོད་དང་བདེ་བ་སྩོལ་བའི་ཕྱིར། བདུད་རྩི་སྤྲོ་བར་བྱེད་པའི་ཟླ་བའི་འོད་དོ། །

[Block 167]
ཏ་ར་གཉིས་བརྗོད་ཅེས་པ་འདིས་ནི་ཏཱ་རེ་གཉིས་དང་ཏུཏྟཱ་རེ་སྟེ་གོང་དུ་ཡི་གེ་བཅུ་པའི་ངག་ཅེས་གསུངས་པ་དེ་ཉིད་ངོས་འཛིན་པའོ། །

[Block 168]
དེས་ན་ཨོཾ་ཏཱ་རེ་ཏུཏྟཱ་རེ་ཏུ་རེ་སྭཱ་ཧཱ་ཞེས་ཡོངས་སུ་གགས་པ་སྟེ། སྒྲོལ་མ་ཞི་བའི་བསྙེན་སྒྲུབ་ལས་གསུམ་ཀའི་སྔགས་སོ། །

[Block 169 [HEADING]]
#### སྦས་དོན། ^1-20-2-0

[Block 170]
སྦས་དོན་ནི། ཉི་ཟླའི་བརྡས་ནང་གི་ཁུ་རྡུལ་གཉིས་ཡིན་ལ། དེ་ཡིས་ཡོངས་སུ་གང་བའི་སྤྱན་ནི་དབུ་མའི་སྟེང་འོག་གི་སྔགས་གཉིས་ཡིན་ཞིང་།

[Block 171 [VERSE]]
དེ་ལས་ཡེ་ཤེས་འབྱུང་བའི་ཕྱིར་འོད་གསལ་བའོ། །
ཧཱ་ར་གཉིས་ནི་སྒྲོལ་བ་ཞེས་པ་སྟེ།
བདེ་སྟོང་གིས་སྲིད་ཞི་གཉིས་ཀྱི་མཐའ་ལས་སྒྲོལ་བའོ། །

[Block 172]
ཏུཏྟཱ་རེ་ནི་གདུང་བ་སྟེ་དཀའ་ཐུབ་ཡིན་ལ། ཉི་མ་ཐུར་དུ་གནོན་པ་དང་ཟླ་བ་གཙུག་ཏོར་དུ་རེངས་ཏེ་འགྱུར་མེད་ཀྱི་དཀའ་ཐུབ་འདིས་ནི་ཐིག་ལེ་འཕོ་བའི་རིམས་ནད་སེལ་བའོ། །

[Block 173 [HEADING]]
### ཕྱག་འཚལ་ཉེར་གཅིག་པ། ^1-21-0

[Block 174]
ཚིགས་བཅད་ཉེར་གཅིག་པ་ཕྱག་འཚལ་དེ་ཉིད་གསུམ་རྣམས་སོགས་ལ། ཡི་གེའི་དོན་དང་། སྤྱིའི་དོན་དང་། སྦས་དོན་དང་། མཐར་ཐུག་གི་དོན་ཏེ་བཞིའོ། །

[Block 175 [HEADING]]
#### ཡི་གེའི་དོན། ^1-21-1-0

[Block 176]
དང་པོ་ནི། སྟོང་པ་ཉིད་དང་། མཚན་མ་མེད་པ་དང་། སྨོན་པ་མེད་པའི་དེ་ཁོ་ན་ཉིད་གསུམ་ལ། གདུལ་བྱའི་སེམས་ཉིད་ཡང་དག་པར་བཀོད་པས།

[Block 177]
དེའི་མཐུ་ལས།

[Block 178]
སྒྲིབ་པ་ཐམས་ཅད་སྤངས་ཏེ། ཞི་བ་ལ་འགོད་པ་སྟེ། གདུལ་བྱ་སྨིན་གྲོལ་དུ་བྱེད་པའི་མཐུ་དང་ཡང་དག་པར་ལྡན་མའོ། །

[Block 179]
གདོན་ནི་ནམ་གུའི་གདོན་ལ་སོགས་པ་གདོན་བཅོ་བརྒྱད་རྣམས་སོ། །

[Block 180]
རོ་ལངས་ནི་རོ་ལངས་ཀྱི་ལས་ཏེ་སྤོང་གཏོང་ལ་སོགས་པའི་ངན་སྔགས་རྣམས་སོ། །
--- END BLOCKS ---
