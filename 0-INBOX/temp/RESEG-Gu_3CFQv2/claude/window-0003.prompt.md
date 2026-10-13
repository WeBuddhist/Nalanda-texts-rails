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
[Block 106]
དེ་ལ་དོན་གྱི་མདོ་ལས༌[^69]ནི་བསམ་པ་དང་། རང༌[^70]བཞིན་ཡོངས་སུ་ཤེས་ནས་སེམས་ཅན་གང་དག་གིས༌[^71]ཇི་ལྟར་ལྷན་ཅིག་གནས་པར་བྱ་བ་དེ་ལྟར་དེ་དག་དང་གནས་སོ། །

[Block 107]
སེམས་ཅན་གང་དག་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་བ་དེ་ལྟར་དེ་དག་ལ་སྒྲུབ་པར་བྱེད་དོ་ཞེས་བྱ་བ་དེ་ལ། བསམ་པ་ནི་ད་ལྟར་བྱུང་བའི་རྐྱེན་གྱིས་བསྐྱེད་པའི་སེམས་སོ། །

[Block 108]
རང་བཞིན་ནི་ཚེ་སྔ་མའི་རྒྱུ་ལས་བྱུང་བའི་ངོ་བོ་ཉིད་དོ། །

[Block 109]
ཡང་ན་བསམ་པ་ནི་སེམས་ཅན་རྣམས་ཀྱི༌[^72]སེམས་ཅན་སོ་སོའི་རང་བཞིན་ཐ་དད་པའོ། །

[Block 110]
རང་བཞིན་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་འཇུག་པ་ཐུན་མོང་བ་སྟེ། བསམ་པ་དང་རང་བཞིན་ཤེས་ནས་ལྷན་ཅིག་འགྲོགས་པར་བྱ་ཞིང་། བསམ་པ་དང༌[^73]རང་བཞིན་ཤེས་ནས་སེམས་ཅན་རྣམས་ལ་བསྒྲུབ་པར་བྱའོ།[^74] །དེ་ལ་བསམ་པ་ཤེས་ནས་གནས་པ་དང་། སྒྲུབ་པའི་དབང་དུ་བྱས་ནས་སེམས་ཅན་གང་གིས་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་བརྩམས་སོ། །

[Block 111]
གཞུང་གི་དོན་གྱི་མདོ་ནི།

[Block 112 [VERSE]]
ཕན་མིན་བསླབ་པ་མ་གཏོགས་པར། །
གང་གིས་ཕ་རོལ་སྡུག་བསྔལ་བ། །

[Block 113]
དེ་དང་གཞན་དང་བདག་ལ་ཡང་། དངོས་པོ་དེ་ནི་དེ་མི་སྤྱོད། །ཅེས་བྱའོ། །

[Block 114 [HEADING]]
#### སེམས་ཅན་གང་དག་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་བ། ^1-8-1-0

[Block 115]
སེམས་ཅན་གང་དག་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་བ་ཞེས་བྱ་བ་དེ་ནས་བཟུང་སྟེ། གཞན་ཁྲོ་བའི་ཀུན་ནས་དཀྲིས་པས་ཀུན་ནས་དཀྲིས་པ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་ནི་རང་བཞིན་ཤེས་ནས་སེམས་ཅན་གང་དག་དང་ཇི་ལྟར་ལྷན་ཅིག་གནས་པར་བྱ་བ་དང་སེམས་ཅན་གང་དག་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་བ༌[^75]ཞེས་བྱ་བའི་དབང་དུ་བྱས་པ་ཡིན་ཏེ། གཞུང་འདིའི་དོན་གྱི་མདོ་ནི་ཡིད་ཀྱི་ལས་བསྒྲུབ་པ༌[^76]དང་། ངག་གི་ལས་བསྒྲུབ་པ་དང་། ལུས་ཀྱི་ལས་བསྒྲུབ༌[^77]པའོ། །

[Block 116 [HEADING]]
##### ཡིད་ཀྱི་ལས་སྒྲུབ་པ། ^1-8-1-1-0

[Block 117]
དེ་ལ་ཡིད་ཀྱི་ལས་སྒྲུབ་པའི་དབང་དུ་བྱས་ཏེ་ཁྲོ་བའི་ཀུན་ནས་དཀྲིས་པས་ཀུན་ནས་དཀྲིས༌[^78]པ་ལ་ཞེས་བྱ་བ་ནས། བདག་ཉིད་མཐོང་བར༌[^79]མི་སྟོན་ཏོ་ཞེས་བྱ་བའི་བར་དུ་སྨོས་སོ། །

[Block 118]
ཡིད་ཀྱི་ལས་བསྒྲུབ་པ༌[^80]ཡང་གཉི་ག་དང་ཅི་རིགས་པར་སྦྱར་བར་བྱ་སྟེ། ཇི་ལྟར་བྱ་ཞེ་ན། ཁྲོ་བའི་ཀུན་ནས་དཀྲིས་པ་ཞེས་བྱ་བ་སེམས་སྒྲུབ་པའི་གནས་སྐབས་ཀྱིས་འདུལ་བ་དེ་ལ་རང་གི་སེམས་སྒྲུབ་ཅིང་འཁྲུག་ཀྱང་མི་འཁྲུག་ལ༌[^81]སྨ་ཡང་འབེབས་པར་བྱེད་དེ། དེ་བཞིན་དུ་གཞན་ལ་ཡང་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 119 [HEADING]]
##### ལུས་ཀྱི་ལས་སྒྲུབ་པ། ^1-8-1-2-0

[Block 120]
ལུས་ཀྱི་ལས་སྒྲུབ་པ་ལས་བརྩམས་ཏེ་གཞན་དག་ལ་མི་རྟེན༌[^82]པར་ཡང་མི་བྱེད་ཧ་ཅང་རྟེན་པར༌[^83]ཡང་མི་བྱེད་དོ། །

[Block 121 [HEADING]]
##### ངག་གི་ལས་སྒྲུབ་པ། ^1-8-1-3-0

[Block 122]
ངག་གི་ལས་སྒྲུབ་པ་ལས་བརྩམས་ཏེ་མདུན་དུ་མཛའ་བོ་ལས༌[^84]སྨོད་པར་ཡང༌[^85]མི་བྱེད་ཅེས་བྱ་བ་ནས་ཆོས་དང་མཐུན་པར་བཤད་ཀྱི༌[^86]བྱང་བར་བྱེད་དོ། །

[Block 123 [HEADING]]
### ཡང་དག་པར་ཡོན་ཏན་གྱིས་ཡང་དག་པར་དགའ་བར་བྱེད་པའི་དོན་གྱི་མདོ། ^1-9-0

[Block 124]
ཡང་དག་པར༌[^87]ཡོན་ཏན་གྱིས་ཡང་དག་པར་དགའ་བར་བྱེད་པའི༌[^88]དོན་གྱི་མདོ་ནི་དད་པ་ལ་སོགས་པ་དེ་དག་ཁོ་ནར་ཟད་དེ། དད་པ་ལ་སོགས་པ་ལྔ་པོ་ཁོ་ན་སྡུད་པའི་རྒྱུ་ཡིན་པར་འོག་ནས་སྟོན་ཏོ། །

[Block 125 [HEADING]]
### ཚར་བཅད་པའི་དོན་གྱི་མདོ། ^1-10-0

[Block 126]
ཚར་བཅད་པའི་དོན་གྱི་མདོ་ནི་ཉེས་པ་དང་། འགལ་བ་རྣམ་པ་གསུམ་ཡོད་པ་ལས་ཉེས་པ་ཇི་ལྟ་བ་བཞིན་དུ་སྨ་དབབ་པ་དང་ཆད་པ་རྣམ་པ་གསུམ་མོ། །

[Block 127]
སྤང་བ་ལ་ནི་རྣམ་པ་གཉིས་ཏེ། དེ་དག་ཉིད་ཕྱིར་དགུག་པར་བྱ་བ་དང་། འགྲོགས་པར་མི་བྱ་བའོ། །

[Block 128]
དེ་ལ་ཉེས་པ་ནི་བྱ་བའི་རིགས་པ་མི་བྱེད་པའོ། །

[Block 129]
འགལ་བ་ནི་བྱ་བ་མི་རིགས་པ༌[^89]བྱེད་པའོ། །

[Block 130 [HEADING]]
### རྫུ་འཕྲུལ་གྱི་དོན་གྱི་མདོ། ^1-11-0

[Block 131]
རྫུ་འཕྲུལ་གྱི་དོན་གྱི་མདོ་ནི་སྐྲག་པར་བྱ་བ་དང་། འདུན་པར་བྱ་བའོ། །

[Block 132 [HEADING]]
## ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་རྣམ་པ་གསུམ། ^2-0

[Block 133]
ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་རྣམ་པ་གསུམ་ཞེས་བྱ་བ་འདིས་ནི་ཚུལ་ཁྲིམས་མང་བར་བསྟན་ཏོ། །

[Block 134]
བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་ལ་ཞེས་བྱ་བ་འདིས་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་གང་ལ་སློབ་པ་དེ་བསྟན་ཏོ། །

[Block 135]
གང་གིས༌[^90]རྣམ་པར་རིག་བྱེད་ཀྱི་དོན་འཛིན་པ་དང་། གོ་བར་ནུས་པ་ལ་ཐུགས་བརྩེ་བའི་སླད་དུ་ཅུང་ཟད་ཅིག་གསན་ཅིང་ཐུགས་བརྩེ་བའི་སླད་དུ་སྩལ་བའི་རིགས་སོ་ཞེས༌[^91]སྦྱར་བར་བྱའོ། །

[Block 136]
ཡེ་ཤེས་དང་མཐུ་ཆེན་པོ་ཐོབ་པ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་ཟབ་པ་དང་རྒྱ་ཆེ་བ་དང་ལྡན་པར་བསྟན་ཏོ། །

[Block 137]
མཆོད་པ་བྱས་པ་ནི་མེ་ཏོག་དང་། བདུག་པ་དང་སྤོས་ལ་སོགས་པ་དང་། བསྟོད་པ་བརྗོད་པ་དང་། ཕྱག་བྱ་བ་ལ་སོགས་པས་མཆོད་པའོ། །

[Block 138]
ཅི་ནུས་པ་དང་རྒྱུའི་སྟོབས་ཅི་ཡོད་པས་ཞེས་བྱ་བ་ནི་སེམས༌[^92]བསྐྱེད་པ་དེ་ད་ལྟར་བྱུང་བའི་སྐྱེས་བུའི་རྩལ་དང་། འདས་པའི་ཚེ་རབས་ན་བྱས་པའི་རྒྱུའི་འབྲས་བུར་བསྟན་པའོ། །

[Block 139]
གལ་ཏེ་འབོགས་པ༌[^93]ནི་ཆོས་མཚུངས་པ་ཁྱིམ་པ་ཞིག་ཡིན་ན་ནི་རིགས་ཀྱི་བུ་ཞེས་བྱ་བའོ། །

[Block 140]
ཡང་ན་རབ་ཏུ་བྱུང་བ༌[^94]ན་ཡང་གལ་ཏེ༌[^95]གཞོན་ནུ་ཞིག་ཡིན་ན་ཚེ་དང་ལྡན་པ་ཞེས་བྱ་བའོ།

[Block 141]
[^96] །ཅི་སྟེ་རྒན་པ་ཞིག་ཡིན༌[^97]ན་ནི་བཙུན་པ་ཞེས་བྱ་སྟེ། འདིས་ཅི༌[^98]བསྟན་ཞེ་ན། རབ་ཏུ་བྱུང་བ་འབའ་ཞིག་དང་། རྒན་པ་ཉི་ཚེ་ལས་གནོད་པར་བྱ་བར་ངེས་པ་མེད་པར་བསྟན་པའི་དོན་ཏོ། །

[Block 142]
བསླབ་པའི་གཞི་གང་ཡིན་པ་རྣམས་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་རྣམ་པ་གསུམ་པོ་རེ་རེ་ལ་བསླབ་པའི་གཞི་སོ་སོ་བ་གང་དག་ཡོད་པ་དེ་དག་གོ། །

[Block 143]
ཚུལ་ཁྲིམས་གང་ཡིན་པ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་རྣམ་པ་གསུམ་མོ། །

[Block 144]
ཡེ་ཤེས་གཟིགས་པ་ཞེས་བྱ་བ་ལ།

[Block 145 [VERSE]]
ཡེ་ཤེས་ནི་ལྐོག་ཏུ་གྱུར་པ་འཛིན་པའོ། །
གཟིགས་པ་ནི་དངོས་པོ་མངོན་སུམ༌[^99]དུ་གྱུར་པ་འཛིན་པའོ། །
--- END BLOCKS ---
