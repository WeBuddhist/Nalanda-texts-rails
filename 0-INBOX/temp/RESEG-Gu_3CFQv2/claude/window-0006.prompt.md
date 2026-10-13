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

[Block 216]
སྐྱེས་བུ་དམ་པའི་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ་ནི་བདག་དང་གཞན་སྒྲུབ་པ་དང་། ཉེས་པ་བྱུང་ན་ཆོས་བཞིན་དུ་ཕྱིར་འཆོས་པའོ།[^150] །དེ་ལ་བདག་དང་གཞན་སྒྲུབ་པ་ནི་ཐོག་མར་བདག༌[^151]གིས་ཚུལ་ཁྲིམས་ཡང་དག་པར་བླངས་པ་ཡང་དག་པར་ལེན་པ་དང་། གཞན་ཡང་དག་པར་ལེན་དུ་འཇུག་པའོ། །

[Block 217]
གཞན་དག་གིས་ཚུལ་ཁྲིམས་ཡང་དག་པར་བླངས་པ་དག་ལ་སྒྲུབ་པ་ནི་གཉིས་ཏེ། ཚུལ་ཁྲིམས་ཀྱི་བསྔགས་པ་བརྗོད་པས་ཚིག་གིས་ཡང་དག་པར་དགའ་བར་བྱེད་པ་དང་། དེ་མཐོང་ན་ཡང་སེམས་ཀྱིས་རབ་ཏུ་དགའ་བར་བྱེད་པའོ། །

[Block 218 [HEADING]]
### ཉེས་པ་བྱུང་ན་ཆོས་བཞིན་དུ་ཕྱིར་འཆོས་པ། ^5-2-0

[Block 219]
བདག་གིས་བསླབ་པའི་གཞི་ཡང་ཡང༌[^152]དག་པར་བླངས་པ་དག་ལས་ཉེས་པ་བྱུང་ན་ཡང་ཆོས་བཞིན་དུ་ཕྱིར༌[^153]འཆོས་པའོ། །

[Block 220 [HEADING]]
## རྣམ་པ་ཐམས་ཅད་ཀྱི་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ། ^6-0

[Block 221 [HEADING]]
### ཡོན་ཏན་དུ་དང་ལྡན་པ། ^6-1-0

[Block 222]
རྣམ་པ་ཐམས་ཅད་ཀྱི་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ་ནི་ཡོན་ཏན་ནི་དུ་དང་ལྡན། རྣམ་པའི་བྱེ་བྲག་ནི་དུ་ཡོད་ཅེ་ན། དེ་ལ་ཡོན་ཏན་དུ་དང་ལྡན་པ༌[^154]ཞེ་ན། ཡོན་ཏན་དྲུག་དང་ལྡན་ཏེ། ཡོན་ཏན་དྲུག་པོ་རྣམས་ཀྱི་དོན་གྱི་མདོ་ནི་རྒྱ་ཆེ་བ་དང་། ཇི་ལྟ་བ་བཞིན་དུ་ཡོད་པ་དང་། རྟག་ཏུ་སྦྱོར་བ་དང་། གུས་པར་སྦྱོར་བ་དང་། རྒྱན་དང་ལྡན་པ་སྟེ། བྱང་ཆུབ་ཆེན་པོར་ཡོངས་སུ་བསྔོས་པའི་ཕྱིར་རྒྱ་ཆེ་བ་དང་། ཁ་ན་མ་ཐོ་བ་མེད་པ་དང་། རབ་ཏུ་དགའ་བའི་གནས་དང་མཐུན་པ་དང་། རྟག་པ་དང་། བརྟན་པ་དང་། ཚུལ་ཁྲིམས་ཀྱི་རྒྱན་དང་ལྡན་པ་དང་དྲུག་གོ་རིམས་བཞིན་ནོ། །

[Block 223]
འདོད་པའི་བསོད་ཉམས༌[^155]ཀྱི་མཐའ་སྤོངས་པའི༌[^156]ཕྱིར་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །

[Block 224]
བདག་ཉིད་དུབ་པར་བྱེད་པའི་མཐའ་སྤངས་པའི་ཕྱིར་རབ་ཏུ་དགའ་བ་ལྟ་བུའོ། །

[Block 225]
རྙེད་པ་དང་བཀུར་སྟི༌[^157]དང་ཕས་ཀྱི་རྒོལ་བ་རྣམས་ཀྱིས་ཟིལ་གྱིས་མི་ནོན་ཅིང་། ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་ཀྱིས་མི་འཕྲོགས་པའི༌[^158]ཕྱིར་བརྟན་པའོ། །

[Block 226]
དགེ་སྦྱོང་གི་རྒྱན་ནི་འདི་དག་ཡིན་ཏེ།

[Block 227 [VERSE]]
དགེ་སྦྱོང་དག་གི་རྒྱན་རྣམས་ནི། །
དད་པ་དང་ནི་གཡོ་མེད་དང་། །
དེ་བཞིན་གནོད་པ་ཆུང་བ་དང་། །
བརྩོན་འགྲུས་བརྩམས་དང་ཤེས་རབ་དང་། །

[Block 228 [VERSE]]
འདོད་པ་ཆུང་དང་ཆོག་ཤེས་དང་། །
གསོ་སླ་བ་དང་དགང་སླ་སྟེ། །
ཡོན་ཏན་དེ་དག་ལྡན་པ་ཡིན། །
དང་བ་ཉིད་དང་ཚོད་ཤེས་དང་། །

[Block 229 [VERSE]]
སྐྱེས་བུ་དམ་པའི་ཆོས་རྣམས་དང་། །
མཁས་པའི་རྟགས་དང་ལྡན་པ་དང་། །
བཟོད་དང་ལྡན་ཞིང་ངེས་པ་དང་། །
དེ་ལ་ཡངས་པ་ཉིད་དང་ལྡན། །

[Block 230 [HEADING]]
### རྣམ་པ་དུ་ཡོད། ^6-2-0

[Block 231]
དེ་ལ་རྣམ་པ་དུ་ཡོད་ཅེ་ན། །རྣམ་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ངོ་བོ་ཉིད་རབ་ཏུ་དབྱེ་བ་དང་། འབྲས་བུ་རབ་ཏུ་དབྱེ་བའོ། །

[Block 232 [HEADING]]
#### ངོ་བོ་ཉིད་རབ་ཏུ་དབྱེ་བ། ^6-2-1-0

[Block 233]
དེ་ལ་ངོ་བོ་ཉིད་རབ་ཏུ་དབྱེ་བ་ནི། །ལྡོག་པའི་ཚུལ་ཁྲིམས་དང་འཇུག་པའི་ཚུལ་ཁྲིམས་དང་གཉི་ག་རྗེས་སུ་སྲུང་བའི་ཚུལ་ཁྲིམས་ཏེ། ངོ་བོ་ཉིད་རབ་ཏུ་དབྱེ་བའོ། །

[Block 234 [HEADING]]
#### འབྲས་བུ་རབ་ཏུ་དབྱེ་བ། ^6-2-2-0

[Block 235]
སྐྱེས་བུ་ཆེན་པོའི་མཚན་རྣམ་པར་སྨིན་པར་བྱེད་པ་ལ་སོགས་པ་ནི་འབྲས་བུ་རབ་ཏུ་དབྱེ་བ་སྟེ། སྐྱེས་བུ་ཆེན་པོའི་མཚན་རྣམ་པར་སྨིན་པར་བྱེད་པ་ནི་དགེ་བ་སྡུད་པའི་ཚུལ་ཁྲིམས་སོ། །

[Block 236]
ལྷག་པའི་སེམས་རྣམ་པར་སྨིན་པར་བྱེད་པ་དང་། སྡུག་པའི་འགྲོ་བ་རྣམ་པར་སྨིན་པར་བྱེད་པ་ནི་སྡོམ་པའི་ཚུལ་ཁྲིམས་སོ། །

[Block 237]
སེམས་ཅན་གྱི་དོན་རྣམ་པར་སྨིན་པར་བྱེད་པ་ནི་སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་སོ། །

[Block 238 [HEADING]]
## ཕོངས་ཤིང་འདོད་པའི་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ། ^7-0

[Block 239]
ཕོངས༌[^159]ཤིང་འདོད་པའི་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ༌[^160]ནི་བདག་གི༌[^161]ཉམས་ལས་དཔག༌[^162]ནས་གཞན་དག་ལ། སྲོག་གཅོད་པ་ལ་སོགས་པ་ལུས་དང་ངག་གི་མི་དགེ་བའི་ལས་ཀྱི་ལམ་བདུན་པོ་དག་དང་། མི་དགེ་བའི་ལུས་ཀྱི་ལས་ཀྱི་ལམ༌[^163]དུ་གཏོགས་པ་དང༌[^164]ལག་པ་དང་བོང་པས་བསྣུན་པ་མི་སྡུག་པའི་རྣམ་པར་འཚེ་བའི་འདུས་ཏེ་རེག་པ་དག་ལས་ལྡོག་པའོ། །

[Block 240 [HEADING]]
## འདི་དང་གཞན་དུ་བདེ་བར་འགྱུར་བའི་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ། ^8-0

[Block 241]
འདི་དང་གཞན་དུ་བདེ་བར་འགྱུར་བའི་ཚུལ་ཁྲིམས་ཀྱི་དོན་གྱི་མདོ་ནི་འདི་དང་གཞན་དུ་སེམས་ཅན་རྣམས་ཀྱི་སྡུག་བསྔལ་གྱི་རྒྱུ་ལ་འཇུག་པ་དགག་པ་དང་། བདེ་བའི་རྒྱུ་ལ་འཇུག་པ་གནང་བ་དང་། དེ་ལ་ཡང་དག་པར་ཞུགས་པའི་སེམས་ཅན་བསྡུ་བ་དང་། དེ་ལ་ལོག་པར་ཞུགས་པའི་སེམས་ཅན་ཚར་བཅད་པ་དང་། སེམས་ཅན་རྣམས་དང་བདག་ལ་འདི་དང་གཞན་དུ་བདེ་བ་སྟེ། སེམས་ཅན་རྣམས་དེ་ལ་འཛུད་པའི་ཕྱིར་རོ། །

[Block 242]
སྦྱིན་པ་ལ་སོགས་པ་དང་ལྡན་པའི་ཚུལ་ཁྲིམས་ནི་བདག་ཉིད་དང་གཞན་དེས་བསྡུས་པ་རྣམས་ལ་འདི་དང་གཞན་དུ་བདེ་བར་འགྱུར་བ་ཉིད་དོ། །

[Block 243 [HEADING]]
## རྣམ་པར་དག་པའི་ཚུལ་ཁྲིམས་རྣམ་པ་བཅུའི་དོན་གྱི་མདོ། ^9-0

[Block 244]
རྣམ་པར་དག་པའི་ཚུལ་ཁྲིམས་རྣམ་པ་བཅུའི་དོན་གྱི་མདོ་ནི་ཉེས་པ་དྲུག་རྣམ་པར་སྤངས་པས་དེའི་གཉེན་པོའི་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱིར་རྣམ་པར་དག་པའོ། །

[Block 245]
ཉེས་པ་དྲུག་པོ་དག་གང་ཞེ་ན། བསམ་པའི་ཉེས་པ་དང་། སྦྱོར་བའི་ཉེས་པ་དང་། སྨོན་པའི་ཉེས་པ་དང་། གཞན་མ་དད་པའི་ཉེས་པ་དང་། བདག་ལ་ཕན་མི་འདོགས་པའི་ཉེས་པ་དང་། འདོད་པའི་དོན་མི་འཐོབ་པའི་ཉེས་པའོ། །

[Block 246]
དེ་ལ་བསམ་པའི་ཉེས་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ལེན་པའི་དུས་ན་ཉེས་པར་བླངས་པ་དང་། སྲུང་བའི་དུས་ན་ཧ་ཅང་ཞུམ་པ་དང་། ཧ་ཅང་ཐལ་བའི་ཕྱིར་རོ། །

[Block 247]
སྦྱོར་བའི་དུས་ན་དེ་ལ་སྦྱོར་བ་མི་བྱེད་པ་དང་། བྱ་བ་ངན་པ་གཞན་ལ་ཆགས་པས་ནི་སྦྱོར་བའི་ཉེས་པར་འགྱུར་རོ། །

[Block 248]
ཚེ་འདི་ལ་ཚེ་ཕྱི་མར་ལོག་པར་སྨོན་པའི་ཉེས་པ་ནི་སྨོན་པའི་ཉེས་པའོ། །

[Block 249]
དགེ་བའི་ཕྱོགས་ལ་སོགས་པ་ལ་སྦྱོར་བ་དང་། འཚོ་བའི་ཡོ་བྱད་ཡོངས་སུ་ཚོལ་བའི་དུས་ན་གཞན་མ་དད་པར་འགྱུར་བའི་ཉེས་པ་ནི་གཞན་དག་གིས་སྨད་པའི་ཕྱིར་རོ། །

[Block 250]
བདག་སྡུག་བསྔལ་བ་ལ་གནས་པའི་ཕྱིར་བདག་ལ་ཕན་མི་འདོགས༌[^165]པའི་ཉེས་པའོ། །
--- END BLOCKS ---
