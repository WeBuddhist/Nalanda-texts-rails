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
སྐད་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པའི་སྒྲས་ནི་རང་བཞིན་གྱིས་འོད་གསལ་བ་འབའ་ཞིག་སྟོན་ནོ།།

[Block 142]
སྔགས་པ་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་སེམས་དཔའོ།།

[Block 143]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་དྲུག་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 144 [HEADING]]
## ལེའུ་བདུན་པ། ^7-0

[Block 145]
ཡན་ལག་དྲུག་ཅེས་བྱ་བ་ནི་ཇི་སྐད་དུ་བཤད་པའི་བསྐྱེད་པའི་རིམ་པ་དང་། རྫོགས་པའི་རིམ་པ་དག་གིས་ཇི་ལྟ་བའི་སེམས་ཀྱི་ཡུལ་རྣམས་ལ་གནས་པའོ།།

[Block 146]
འདོད་པ་ནི་འཛིན་པའི་རྣམ་པའོ།།

[Block 147]
མིག་ལ་སོགས་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བུའི་མིག་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པ་རྣམས་ཀྱིས་ཡུལ་རྣམས་བླངས་ནས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་ལྷན་ཅིག་ཏུ་ཡུལ་མཆོག་ཏུ་གྱུར་པ་ལ་སོགས་པ་རྣམས་ལ་བདེ་བ་ཙམ་གྱིས་ཡུལ་དུ་རྣམ་པར་བྱེད་དོ།།

[Block 148]
དེ་བཞིན་དུ་རྣལ་འབྱོར་པས་ཀྱང་ཡོངས་སུ་མི་སྤང་བ་ཉིད་དུ་ལོངས་སྤྱད་པར་བྱའོ།།

[Block 149]
ཡིད་དུ་འོང་བ་ནི་མཆོག་ཏུ་གྱུར་པའོ།།

[Block 150]
ཡིད་དུ་མི་འོང་བ་ནི་རྣམ་པར་དམན་པ་དག་གོ།།

[Block 151]
ལུང་དུ་མ་བསྟན་པ་ནི་གཉི་ག་མ་ཡིན་པའོ།།

[Block 152]
ཁྲོ་བོ་ནི་ཐབས་ཀྱི་ཡེ་ཤེས་སོ་ཞེས༌[^56]བྱ་བ་ནི་ཁམས་ཕྲ་མོ་དང་འདྲེས་པའི་ཡེ་ཤེས་སོ།།

[Block 153]
རླུང་ལ་དགའ་བ་ཞེས་བྱ་བ་ནི་ཡི་གེ་ཧཱུཾ་གིའོ།།

[Block 154]
རྐན་གྱི་པདྨ་དེ་དག་ཀྱང་ལྡན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཡ་རྐན་གྱི་ལྕེའུ་ཆུང་དང་ངོ་།།ཆོས་དང་དོན་དང་སྤོབས་པ་སོ་སོ༌[^57]ཡང་དག་པར་རིག་པ་ཞེས་བྱ་བ་ནི་ཆོས་དང་དོན་ནི་བློས་རྣམ་པར་སྤྲོ་བར་བྱ་བའོ།[^58] །སྤོབས་པ་སོ་སོ༌[^59]ཡང་དག་པར་རིག་པ་ནི་རིགས་ལྔ་ལ་སོགས་པ་སོ་སོའི་རིམ་པར༌[^60]རིགས་བརྒྱ་རྣམས་སུ་ཉེ་བར་མཚོན་ཏེ་སྤྲོ་བར་བྱའོ།།

[Block 155]
རང་བཞིན་བརྒྱད་ཅུ་དང་ལྡན་པ་རྣམས་ཞེས་པ་ནི་སྤྱི་མ་ལུས་པ་རྣམས་སོ།།

[Block 156]
མཐོང་བའི་ཆོས་ལ་ཞེས་བྱ་བ་ནི་ཆོས་རྟོགས་པ་ནའོ།།

[Block 157]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བདུན་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 158 [HEADING]]
## ལེའུ་བརྒྱད་པ། ^8-0

[Block 159]
ལྷ་ཉི་ཤུ་རྩ་ལྔ་པོ་ཞེས་བྱ་བ་ནི་རང་བཞིན་གྱིས་རྣམ་པར་དག་པའི་ལྷ་ཉི་ཤུ་རྩ་ལྔ་པོ་རྣམས་སོ།།

[Block 160]
བདག་པོ་ལས་གཞན་པ་ཞེས་བྱ་བ་ནི་རིགས་གཞན་དུ་སྐྱེས་པ་ཡང་བརྟག་པའོ།།

[Block 161]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བརྒྱད་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 162 [HEADING]]
## ལེའུ་བཅུ་པ། ^10-0

[Block 163]
ནམ་མཁའ་བཞི་ནི་སྟོང་པ་བཞིའི་བདག་ཉིད་དོ།།

[Block 164]
ཡང་ན་འབྱུང་བ་བཞི་དང་།

[Block 165]
ཕྱག་རྒྱ་བཞིའི་བདག་ཉིད་ཀྱིས་སོ། །

[Block 166]
གཞན་དུ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སེམས་ཅན་རྣམས་གདུལ་བའི་དོན་དུ་བྱ་བ་ལས་གཞན་དུ་རང་དགར་སྲོག་གཅོད་པ་ལ་སོགས་པ་བྱེད་ན། དམྱལ་བ་མནར་མེད་པར་ལྟུང་བར་ངེས་སོ།།

[Block 167]
དེ་ནས་སྐད་ཅིག་དེ་ཉིད་ལ་ཞེས་པ་ནི་སྔར་ཕྱེ་བ་དེས་སྣང་བ་གསལ་བར་གྱུར་པ་ནའོ།།

[Block 168]
དུས་ཀྱི་ཚད་ནི་དུས་དེ་དག་ཏུ་བསམ་པ་ཤིན་ཏུ་བསྐྱེད་པའོ།།

[Block 169]
སྤྱན་ལ་སོགས་པ་ཞེས་པ་ནི་བཞི་པོ་ལས་གང་འདོད་པ་ཅིག༌[^61]བཀུག་ལ་རང་གི་རིགས་ཀྱིས་བོན་གྱིས་རྫོགས་པར་བྱས་ཏེ། ཡེ་ཤེས་སེམས་དཔའ་དང་། ཏིང་ངེ་འཛིན་སེམས་དཔའ་དང་ལྡན་པར་བྱ་ཞིང་རིགས་ལྔ་པོ་རྣམས་ཀྱིས༌[^62]གང་བར་བྱས་ནས་དཀྱིལ་འཁོར་བ་རྣམས་གོས་དཀར་མོ་ལ་སོགས་པའི་བུད་མེད་ཀྱི་གཟུགས་ཀྱིས་བཅུག་ལ། སྔོན་དུ་རྗེས་སུ་ཆགས་པར་བྱས་ནས་སྣ་ཚོགས་པའི་དགའ་བས་གདུལ་བྱ་སྣ་ཚོགས༌[^63]པའི་དོན་བྱ་བ་ཡིན་ནོ།།

[Block 170]
སྔགས་ཀྱི་མིང་ནི་ཡི་གེ་གསུམ་ལ་སོགས་པའོ།།

[Block 171]
སྔགས་ཀྱི་དོན་ནི་ཡི་གེ་གསུམ་པོ་རྣམས་ཀྱིས་སྔགས་ཀྱི༌[^64]དོན་བརྗོད་པའོ།།

[Block 172]
སྔགས་སྤེལ་བ་ནི་ཞི་བ་ལ་སོགས་པའི་དོན་དང་སྔགས་སྤེལ་བ༌[^65]སྟེ།།སྭཱ་ཧཱ་ལ་སོགས་པ་དང་རབ་ཏུ་སྦྱར་ཏེ་སྔགས་རྣམས་རབ་ཏུ་བརྗོད་པའོ།།

[Block 173]
རྡོ་རྗེ་ཚིག་སྒྲ་སྤངས་པ་ནི་རྡོ་རྗེ་བཟླས་པའོ།།

[Block 174]
གོ་རིམས༌[^66]ནི་རིམ་པ་ལྔ་པོ་རྣམས་སོ།།

[Block 175]
སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་ནུས་པ་ནི་ཤེས་རབ་དང་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ནོ།།

[Block 176]
[^67]བདག་པོ་ལ་སོགས་པ་སེམས་དཔའ་གསུམ་ཞེས་བྱ་བ་ནི་དམ་ཚིག་སེམས་དཔའ་དང་ཡེ་ཤེས་སེམས་དཔའ་དང་ཏིང་ངེ་འཛིན་སེམས་དཔའི་བདག་ཉིད་ཅན་གྱི་དཀྱིལ་འཁོར་བ་རྣམས་ཀྱིའོ།།

[Block 177]
གནོད་མཛེས་རྒྱལ་པོ་ཞེས་པ་ནི་གནོད་མཛེས་ཀྱི༌[^68]རྒྱལ་པོས་ཀྱང་བཀུག་སྟེ་བསྐུལ་བའོ།།

[Block 178]
འདི་ནི་བདག་གིའོ་ཞེས་པ་ལ་འདི་ནི་ཞེས་པ་ནི་རྣལ་འབྱོར་པའོ།།

[Block 179]
བདག་ཅག་གི་ཞེས་བྱ་བ༌[^69]ནི་སེམས་ཅན་རྣམས་ཀྱིའོ།།

[Block 180]
ཕའོ་ཞེས་བྱ་བ་ནི་རྣལ་འབྱོར་པ་བདག་སྟེ། བདག་ཉིད་ཚོགས་དང་བཅས་པ་ལ་སེམས་ཅན་གྱི་ཚོགས་རྣམ་པ་མང་པོ་རྣམས་གཅེས་པར་འཛིན་པར་མངོན་དུ་བསམ་པར་བྱའོ།།
--- END BLOCKS ---
