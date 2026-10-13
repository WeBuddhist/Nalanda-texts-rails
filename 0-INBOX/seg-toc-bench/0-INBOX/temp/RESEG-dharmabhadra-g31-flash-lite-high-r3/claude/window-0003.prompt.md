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
[Block 106 [HEADING]]
### དང་པོ་བསམ་པའི་ཁྱད་པར་བསྟན་པ། ^3-1-0

[Block 107]
གསུམ་པ་ཕན་ཡོན་བསྟན་པ་ལ་བཞི། བསམ་པའི་ཁྱད་པར་བསྟན་པ། དུས་ཀྱི་ཁྱད་པར་བསྟན་པ། ཕན་ཡོན་དངོས་བསྟན་པ། གྲངས་ཀྱི་སྒོ་ནས་མདོར་བསྡུས་ཏེ་བསྟན་པའོ། །དང་པོ་ནི།

[Block 108 [VERSE]]
རྩ་བའི་སྔགས་ཀྱིས་བསྟོད་པ་འདི་དང་། །
ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག །
ལྷ་མོ་ལ་གུས་ཡང་དག་ལྡན་པའི། །
བློ་ལྡན་གང་གིས་རབ་དང་བརྗོད་པས། །

[Block 109]
ཞེས་པ་སྟེ། ཞི་བ་དང་ཁྲོ་མོའི་རྩ་བའི་སྔགས་གཉིས་དང་སྤེལ་བས་ན་དེའི་སྒོ་ནས་སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ་འདི་ལ་ཚིགས་བཅད་ཉི་ཤུ་རྩ་གཅིག་ཡོད་པ་དང་། ཕྱག་འཚལ་ལོ་ཞེས་པ་ཡང་ནི་ཉི་ཤུ་རྩ་གཅིག་ཡོད་པའི་གཞུང་འདི་ཉིད་ལྷ་མོ་སྒྲོལ་མ་ཉིད་ལ་བཀའ་དྲིན་དྲན་པའི་གུས་པ་ཡང་དག་པ་དང་ལྡན་པའི་གང་ཟག་ལེགས་ཉེས་འབྱེད་པའི་བློ་གྲོས་མཆོག་ཏུ་གྱུར་པ་དང་ལྡན་པ་གང་དང་གང་གིས་ཚིག་དོན་ལྟར་ཡོན་ཏན་དྲན་པའི་རབ་ཏུ་དད་པ་བརྟན་པོས་བརྗོད་པས་འོག་ནས་འབྱུང་བའི་ཕན་ཡོན་རྣམས་འབྱུང་ངོ་ཞེས་བསམ་པ་དང་གུས་ཆེན་པོས་བསྟོད་དགོས་པར་བསྟན་ཏོ། །

[Block 110 [HEADING]]
### གཉིས་པ་དུས་ཀྱི་ཁྱད་པར་བསྟན་པ། ^3-2-0

[Block 111]
གཉིས་པ་དུས་ཀྱི་ཁྱད་པར་བསྟན་པ་ནི།

[Block 112 [VERSE]]
སྲོད་དང་ཐོ་རངས་ལངས་པར་བྱས་ནས། །
དྲན་པས་མི་འཇིགས་ཐམས་ཅད་རབ་སྟེར། །
སྡིག་པ་ཐམས་ཅད་རབ་ཏུ་ཞི་བ། །
ངན་འགྲོ་ཐམས་ཅད་འཇོམས་པ་ཉིད་དོ། །

[Block 113]
ཞེས་པ་སྟེ། ཚེ་འདིར་ནད་གདོན་དགྲ་རྐུན་སོགས་ཀྱིས་འཇིགས་ནས་གསོལ་བ་འདེབས་ན། སྲོད་ཀྱི་དུས་སུ་ཁྲོ་མོའི་སྐུ་སོགས་གཙོ་བོར་དྲན་ནས་བསྟོད་པ་དང་། ཕྱི་མར་ངན་འགྲོའི་སྡུག་བསྔལ་གྱིས་འཇིགས་ནས་གསོལ་བ་འདེབས་ན། ཐོ་རངས་ཀྱི་དུས་སུ་མལ་ནས་ལངས་པར་བྱས་ནས་ཞི་བའི་སྐུ་སོགས་གཙོ་བོར་དྲན་ནས་བསྟོད་པས། ཕྱི་ནང་གི་འཇིགས་པ་ཆེན་པོ་བརྒྱད་འཇོམས་པས་ན། མི་འཇིགས་པ་ཐམས་ཅད་རབ་ཏུ་སྟེར་ཞིང་། ངན་འགྲོའི་རྒྱུ་མི་དགེ་བ་བཅུ་སོགས་སྡིག་པ་ཐམས་ཅད་རབ་ཏུ་ཞི་བར་བྱེད་པས་ན། འབྲས་བུ་དམྱལ་བ་སོགས་ངན་འགྲོ་ཐམས་ཅད་ཀྱང་འཇོམས་པ་ཉིད་ཀྱི་ཕན་ཡོན་ཡོད་དོ། །ཞེས་དུས་ཀྱི་ཁྱད་པར་དང་བསྟུན་དགོས་པར་བསྟན་ཏོ། །

[Block 114 [HEADING]]
### གསུམ་པ་ཕན་ཡོན་དངོས་བསྟན་པ། ^3-3-0

[Block 115 [HEADING]]
#### དང་པོ་སྒྲུབ་པ་པོ་རང་ལ་འབྱུང་བའི་ཕན་ཡོན། ^3-3-1-0

[Block 116 [HEADING]]
##### དང་པོ་ཡོན་ཏན་འཐོབ་པའི་ཕན་ཡོན། ^3-3-1-1-0

[Block 117]
གསུམ་པ་ཕན་ཡོན་དངོས་བསྟན་པ་ལ་གཉིས། སྒྲུབ་པ་པོ་རང་ལ་འབྱུང་བའི་ཕན་ཡོན་དང་། སྒྲུབ་བྱ་གཞན་ལ་འབྱུང་བའི་ཕན་ཡོན་ནོ། །དང་པོ་ལ་གཉིས། ཡོན་ཏན་འཐོབ་པའི་ཕན་ཡོན་དང་། སྐྱོན་ལྡོག་པའི་ཕན་ཡོན་ནོ། །དང་པོ་ནི།

[Block 118 [VERSE]]
རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས། །
མྱུར་དུ་དབང་ནི་བསྐུར་བར་འགྱུར་ལ། །
འདི་ལས་ཆེ་བ་ཉིད་ནི་ཐོབ་ཅིང་། །
སངས་རྒྱས་གོ་འཕང་མཐར་ཐུག་དེར་འགྲོ། །

[Block 119]
ཞེས་པ་སྟེ། བཅོམ་ལྡན་འདས་མ་ཉིད་དང་ལྷན་ཅིག་ཏུ་བཞུགས་པའི་རྒྱལ་བ་སྤྲུལ་པའི་སྐུ་གྲངས་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས་མྱུར་དུ་སྟེ་ཚེ་འདི་ཉིད་ལ་འོད་ཟེར་རམ་བདུད་རྩིའི་རྒྱུན་གྱིས་དབང་ནི་བསྒྱུར་བར་འགྱུར་ལ། དེའི་མཐུས་གནས་སྐབས་སུ་ད་ལྟའི་གནས་སྐབས་འདི་ལས་ཆེ་ཞིང་མཆོག་ཏུ་གྱུར་པའི་གནས་ལུས་ལོངས་སྤྱོད་འཁོར་རྣམས་ཕུན་སུམ་ཚོགས་པ་ཉིད་ནི་ཐོབ་ཅིང་། མཐར་ཐུག་གི་འབྲས་བུ་ལམ་མྱུར་དུ་བགྲོད་ནས་སངས་རྒྱས་ཀྱི་གོ་འཕང་དེར་འགྲོ་བར་འགྱུར་རོ། །ཞེས་པ་སྟེ་ཚིག་རྐང་བཞི་པ་ལ་འགྱུར་ཁ་ཅིག་ཏུ། མཐར་ཐུག་སངས་རྒྱས་གོ་འཕང་དེར་འགྲོ། ཞེས་པ་ལྟར་བཤད་དོ། །

[Block 120 [HEADING]]
##### གཉིས་པ་སྐྱོན་ལྡོག་པའི་ཕན་ཡོན། ^3-3-1-2-0

[Block 121 [HEADING]]
###### དང་པོ་སྡུག་བསྔལ་གྱི་རྒྱུ་ལྡོག་པའི་ཕན་ཡོན། ^3-3-1-2-1-0

[Block 122]
གཉིས་པ་སྐྱོན་ལྡོག་པའི་ཕན་ཡོན་ལ་གཉིས། སྡུག་བསྔལ་གྱི་རྒྱུ་ལྡོག་པའི་ཕན་ཡོན་དང་། འབྲས་བུ་སྡུག་བསྔལ་ལ་ལྡོག་པའི་ཕན་ཡོན་ནོ། །དང་པོ་ནི།

[Block 123 [VERSE]]
དེ་ཡི་དུག་ནི་དྲག་པོ་ཆེན་པོ། །
བརྟན་གནས་པའམ་གཞན་ཡང་འགྲོ་བ། །
ཟོས་པ་དང་ནི་འཐུངས་པ་ཉིད་ཀྱང་། །
དྲན་པས་རབ་ཏུ་སེལ་བ་ཉིད་ཐོབ། །

[Block 124]
ཅེས་པ་སྟེ། གནས་སྐབས་དང་མཐར་ཐུག་གི་ཕན་ཡོན་དེ་ཐོབ་པ་ལ་བར་དུ་གཅོད་ཅིང་སྡུག་བསྔལ་ཚབས་ཆེན་བསྐྱེད་པར་བྱེད་པའི་དུག་ཆགས་སོགས་ཉོན་མོངས་ནི། མངོན་མཐོ་དང་ངེས་ལེགས་ཀྱི་སྲོག་འཕྲོག་པས་ན་དྲག་པོ་དང་། འཁོར་བ་དང་ངན་སོང་གི་སྡུག་བསྔལ་བསྐྱེད་པས་ན་ཆེན་པོ་ཡིན་པས་དེ་དང་། བཙན་དུག་སོགས་བརྟན་པར་གནས་པ་སྣོད་ཀྱི་འཇིག་རྟེན་ལ་ཡོད་པའམ། གཞན་ཡང་སྦྲུལ་དུག་སོགས་གཡོ་ཞིང་འཕྲོས་བཅུད་ཀྱི་སེམས་ཅན་ལ་ཡོད་པའི་དུག་རྣམས་ཁར་ཟོས་པ་དང་ནི་འཐུངས་པ་དང་རེག་པ་ལ་སོགས་པ་ཉིད་ཀྱང་། ལྷ་མོའི་སྐུ་སོགས་དྲན་ནས་བསྟོད་པ་བརྗོད་པ་ཙམ་གྱིས་རབ་ཏུ་སེལ་བ་ཉིད་ཐོབ་པར་འགྱུར་རོ། །

[Block 125 [HEADING]]
###### གཉིས་པ་འབྲས་བུ་སྡུག་བསྔལ་ལྡོག་པའི་ཕན་ཡོན། ^3-3-1-2-2-0

[Block 126]
གཉིས་པ་འབྲས་བུ་སྡུག་བསྔལ་ལྡོག་པའི་ཕན་ཡོན་ནི།

[Block 127 [VERSE]]
གདོན་དང་རིམས་དང་དུག་གིས་གཟིར་བའི། །
སྡུག་བསྔལ་ཚོགས་ནི་རྣམ་པར་སྤོང་སྟེ།

[Block 128]
ཞེས་པ་སྟེ། གཞན་ཡང་ནམ་གྲུ་ལ་སོགས་པའི་གདོན་དང་། ཉིན་གཅིག་པ་ལ་སོགས་པའི་རིམས་དང་། ཕྱི་ནང་གི་དུག་གིས་གཟིར་བ་སྟེ་བསྐྱེད་པའི་སྡུག་བསྔལ་དང་ཉེར་འཚེའི་ཚོགས་ནི་རྣམ་པར་སྤོང་ནུས་པ་ཡིན་ཏེ། དེ་དག་གི་རྒྱུ་རྣམས་བདེ་བླག་ཏུ་སེལ་ནུས་པའི་ཕྱིར་རོ། །

[Block 129 [HEADING]]
#### གཉིས་པ་བསྒྲུབ་བྱ་གཞན་ལ་འབྱུང་བའི་ཕན་ཡོན། ^3-3-2-0

[Block 130]
གཉིས་པ་བསྒྲུབ་བྱ་གཞན་ལ་འབྱུང་བའི་ཕན་ཡོན་ནི། སེམས་ཅན་གཞན་པ་རྣམས་ལ་ཡང་ངོ། ། ཞེས་པ་སྟེ། སྒྲུབ་པ་པོ་རང་ཉིད་ལ་ཕན་ཡོན་འབྱུང་བར་མ་ཟད། ངེས་སྦྱིན་བདག་སོགས་སེམས་ཅན་གཞན་པ་རྣམས་ཀྱི་ཆེད་དུ་དམིགས་ནས་བསྟོད་ཚིག་བརྗོད་ཀྱང་གོང་འོག་ཏུ་བཤད་པའི་ཕན་ཡོན་རྣམས་ཇི་ལྟ་བ་བཞིན་དུ་འབྱུང་ངོ་། །ཞེས་པའོ། །

[Block 131 [HEADING]]
### བཞི་པ་གྲངས་ཀྱི་སྒོ་ནས་མདོར་བསྡུས་བསྟན་པ། ^3-4-0

[Block 132]
བཞི་པ་གྲངས་ཀྱི་སྒོ་ནས་མདོར་བསྡུས་བསྟན་པ་ནི།

[Block 133 [VERSE]]
གཉིས་གསུམ་བདུན་དུ་མངོན་པར་བརྗོད་ན། །
བུ་འདོད་པས་ནི་བུ་ཐོབ་འགྱུར་ཞིང་། །
ནོར་འདོད་པས་ནི་ནོར་རྣམས་ཉིད་ཐོབ། །
འདོད་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་ཏེ། །
བགེགས་རྣམས་མེད་ཅིང་སོ་སོར་འཇོམས་འགྱུར། །

[Block 134]
ཞེས་པ་སྟེ། ཉིན་མཚན་གྱི་ཆ་གཉིས་པོ་རེ་རེ་ལ་ཐུན་གསུམ་གསུམ་དུ་བྱས་ཏེ། ཐུན་རེ་རེ་ལ་བསྟོད་ཚིག་ལན་བདུན་བདུན་དུ་མངོན་པར་བརྗོད་ན། རིགས་དང་ཆོས་བརྒྱུད་འཛིན་པའི་བུ་འདོད་པ་རྣམས་ཀྱིས་ནི་བུ་དང་སློབ་མ་ཐོབ་པར་འགྱུར་ཞིང་། འདི་ཕྱིའི་བདེ་བ་སྒྲུབ་པའི་ནོར་འདོད་པ་རྣམས་ཀྱིས་ནི་ནོར་དང་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པ་རྣམས་བདེ་བླག་ཉིད་དུ་ཐོབ་པ་སོགས། །མདོར་ན་མཐུན་ཕྱོགས་གནས་སྐབས་དང་མཐར་ཐུག་གི་འདོད་པ་ཇི་སྙེད་ཡོད་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་ཏེ། དེ་ལ་མི་མཐུན་ཕྱོགས་ཀྱི་བགེགས་དང་བར་དུ་གཅོད་པ་རྣམས་གསར་དུ་འབྱུང་བ་མེད་ཅིང་། སྔར་བྱུང་ཟིན་པ་རྣམས་ཀྱང་། རྗེ་བཙུན་མ་སྐབས་གང་ཡིན་གྱི་ནུས་པས་སོ་སོར་ལྷག་མེད་དུ་འཇོམས་པར་འགྱུར་རོ། །ཞེས་པའོ། །

[Block 135 [HEADING]]
## བསྔོ་བ། ^a-0

[Block 136]
སྨྲས་པ།

[Block 137 [VERSE]]
རྒྱལ་ཀུན་འཕྲིན་ལས་གཅིག་བསྡུས་སྒྲོལ་མ་ལ། །
རྒྱལ་བ་ཀུན་གྱིས་མགྲིན་གཅིག་བསྟོད་པའི་དོན། །
རྒྱལ་བ་དགེ་འདུན་གྲུབ་ཀྱི་ཊཱི་ཀྐ་དང་། །
རྒྱལ་བའི་དགོངས་པ་ཇི་བཞིན་བདག་གིས་བཤད། །

[Block 138 [VERSE]]
ཡང་དག་ལྟར་སྣད་དབྱེ་བ་མི་ཕྱེད་ཅིང་། །
ཕྲག་དོག་ཟུག་རྡུས་མནར་བའི་དེང་དུས་འགྲོར། །
ཕན་པའི་རེ་བ་བདག་ལ་མ་མཆིས་ཀྱང་། །
རང་བློ་འཕེལ་ཕྱིར་བསྐྲུན་པའི་ལེགས་སྤྱད་མཐུས། །

[Block 139 [VERSE]]
རྒྱལ་ཡུམ་སྒྲོལ་མས་འབྲལ་མེད་རྗེས་འཛིན་ཅིང་། །
རྒྱལ་བའི་འཕྲིན་ལས་སྲིད་མཐར་སྤེལ་བ་ལ། །
རྒྱལ་སྲས་གཞན་ལས་སྙིང་སྟོབས་རྨད་བྱུང་བ། །
རྒྱལ་བ་གཉིས་པ་ལྟ་བུར་བདག་གྱུར་ཅིག །

[Block 140 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 141 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 142]
ཅེས་སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་རྣམ་བཤད་ཡིད་འཕྲོག་ཨུཏྤ་ལའི་ཆུན་པོ་ཞེས་བྱ་བ་འདི་ནི། པཎ་ཆེན་དགེ་འདུན་གྲུབ་ཀྱི་ཊཱི་ཀ་ལ་གཞི་བྱས། རྗེ་བཙུན་གྲགས་པ་རྒྱལ་མཚན། ཐམས་ཅད་མཁྱེན་པ་དགེ་འདུན་རྒྱ་མཚོ། རྗེ་ཏཱ་ར་ནཱ་ཐ་རྣམས་ཀྱི་འགྲེལ་པ་ནས་ལེགས་ཆ་བསྡུས། དཔལ་ལྷ་གཅིག་དཱི་པཾ་ཀ་ར་དང་། པཎ་ཆེན་ཉི་མ་སྦས་པའི་བཞེད་སྲོལ་དང་ཡང་གུང་ཆུང་ཟད་བསྒྲིགས་ནས་ཤཱཀྱའི་དགེ་སློང་དྷརྨ་བྷ་དྲས་འབུ་མང་གི་ལོའི་དབོ་ཟླ་བའི་ཡར་ཚེས་བཟང་པོ་ལ་བཞད་དངུལ་ཆུའི་རི་སྦུག་ཏུ་སྦྱར་བའོ། །

[Block 143]
འདས་ཀྱང་བསྟན་འགྲོ་ལ་ཕན་ཐོགས་པར་གྱུར་ཅིག ། མངྒ་ལཾ༎ ༎
--- END BLOCKS ---
