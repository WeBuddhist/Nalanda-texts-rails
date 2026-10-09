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
དེ་ལྟར་ཆོས་དམིགས་པ་མེད་དེ་ཡོད་པ་མ་ཡིན་ཞིང་མངོན་པར་མ་གྲུབ་ན་དམིགས་པ་ཡོད་པར་འཐད་པར་ག་ལ་འགྱུར། ཆོས་ཀྱི་དམིགས་པ་ཞེས་བྱ་བ་དེ་ཡང་མངོན་པར་མ་གྲུབ་པ་ཁོ་ནའོ། །

[Block 177]
མངོན་པར་མ་གྲུབ་ཅིང་མེད་པ་དེ་ལ་དམིགས་པ་ཡོད་པར་ག་ལ་འགྱུར། དམིགས་པ་མེད་ན་ཇི་ལྟར་དམིགས་པས་ཆོས་སྒྲུབ་པར་བྱེད། དེའི་ཕྱིར་དམིགས་པ་ཡང་ཡོད་པ་མ་ཡིན་ལ། ཆོས་ཀྱང་དམིགས་པ་དང་བཅས་པ་མ་ཡིན་པ་ཁོ་ནའོ། །

[Block 178]
འདིར་སྨྲས་པ། དངོས་པོ་གཞན་འགགས་མ་ཐག་པ༌[^125]ནི་དངོས་པོ་གཞན་སྐྱེ་བའི་རྐྱེན་ཡིན་ནོ། །

[Block 179]
དེ་ནི་དེ་མ༌[^126]ཐག་པ་ཞེས་བྱ་བ་སྟེ་དེ་ཡོད་དོ། །

[Block 180]
བཤད་པ།

[Block 181 [VERSE]]
ཆོས་རྣམས་སྐྱེས་པ་མ་ཡིན་ན། །
འགག་པ་འཐད་པར་མི་འགྱུར་རོ། །
དེ་ཕྱིར་དེ་མ་ཐག་མི་རིགས། །
འགགས་ན་རྐྱེན་ཡང་གང་ཞིག་ཡིན། །

[Block 182 [VERSE]]
དེ་ལ་རྩ་བ་འོག་མ་གཉིས། །
འགགས་ན་རྐྱེན་ཡང་གང་ཞིག་ཡིན། །
དེ་ཕྱིར་དེ་མ་ཐག་མི་རིགས། །

[Block 183]
ཞེས་བསྣོར་བར་བལྟ་བར་བྱའོ། །

[Block 184]
[^127]ཞེས་བྱ་བའི་སྒྲ་ནི་འདིར་མ་སྐྱེས་པ་ལ་ལྟོས་པར༌[^128]བལྟ་བར༌[^129]བྱའོ། །

[Block 185]
དེ་ཡང་མ་སྐྱེས་པའི་སྒྲ་ལ་ལྟོས༌[^130]ནས།

[Block 186 [VERSE]]
འགགས་ན་རྐྱེན་ཡང་གང་ཞིག་ཡིན། །
མ་སྐྱེས་པའི་རྐྱེན་གང་ཞིག་ཡིན། །

[Block 187]
ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 188]
དེ་གཉིས་ནི་ཚིགས་སུ་བཅད་པ་སྦྱར་བའི་ཕྱིར་གོ་རིམས་བཞིན་མ་བྱས་སོ། །

[Block 189]
དངོས་པོ་གཞན་འགག༌[^131]མ་ཐག་པ་ནི་དངོས་པོ་གཞན་སྐྱེ་བའི་རྐྱེན་ཡིན་ནོ་ཞེས་སྨྲས་པ་གང་ཡིན་པ་དེ་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 190 [VERSE]]
ཆོས་རྣམས་སྐྱེས་པ་མ་ཡིན་ན། །
འགག་པ༌[^132]འཐད་པར་མི་འགྱུར་རོ། །
འགགས་ན་རྐྱེན་ཡང་གང་ཞིག་ཡིན། །

[Block 191]
འགག་པ༌[^133]ཞེས་བྱ་བ་ནི་མེད་པ་སྟེ། དེ་ལ་གལ་ཏེ་མྱུ་གུ་སྐྱེ་བའི་སྔོན་རོལ་དུ་ས་བོན་འགག་པར༌[^134]འགྱུར་ན་ནི་ས་བོན་འགགས་ཏེ་མེད་ན་མྱུ་གུ་སྐྱེ་བར་འགྱུར་བ་གང་ཡིན་པ་དེའི་རྐྱེན་ཡང་གང་ཞིག་ཡིན། ཡང་ན་ས་བོན་འགག་པའི་རྐྱེན་ཡང་གང་ཞིག་ཡིན། ས་བོན་འགགས་ཏེ་མེད་པ་ཡང་ཇི་ལྟར་མྱུ་གུ་སྐྱེ་བའི་རྐྱེན་དུ་འགྱུར། མྱུ་གུ་མ་སྐྱེས་པའི་རྐྱེན་དུ་ས་བོན་འགག་པ་ཇི་ལྟར་འགྱུར། དེ་ལྟ་བས་ན་ས་བོན་འགགས་ནས་མྱུ་གུ་སྐྱེ་བར་རྟོག་ན་དེ་གཉི༌[^135]ག་རྒྱུ་མེད་པར་ཐལ་བར་འགྱུར་ཏེ། རྒྱུ་མེད་པར་ནི་མི་འདོད་དོ། །

[Block 192]
སྨྲས་པ། གལ་ཏེ་མྱུ་གུ་སྐྱེས་མ་ཐག་ཏུ་ས་བོན་འགག་པར་འགྱུར་ན། དེ་ལྟ་ན་ཡང་དེ་མ་ཐག་འགྲུབ་སྟེ། འདི་ལྟར་མྱུ་གུ་སྐྱེས་མ་ཐག་ཏུ་ས་བོན་འགག་པའི་རྐྱེན་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 193]
བཤད་པ། དེ་ཡང་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། སྐྱེས་ནའང་རྐྱེན་དུ་ཇི་ལྟར་འགྱུར༌[^136]ཏེ། གལ་ཏེ་མྱུ་གུ་སྐྱེ་ཞིང༌[^137]མྱུ་གུ་སྐྱེ་བའི་བྱ་བ་མཐར་ཐུག་པའི་ཚེ་ས་བོན་འགག་པར་འགྱུར་ན་འགག་པ་དེའི་རྐྱེན་ཡང་གང་ཞིག་ཡིན་པར་འགྱུར། མྱུ་གུ་སྐྱེ་བའི་རྐྱེན་ཡང་གང་ཞིག་ཡིན་པར་འགྱུར་ཏེ། དེའི་ཕྱིར་དེ་ལྟ་ན་ཡང་དེ་གཉི་ག་སྔ་མ་བཞིན་དུ་རྒྱུ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 194]
ཅི་སྟེ་ས་བོན་འགག་བཞིན་པ་ན་མྱུ་གུ་སྐྱེ་བས་དེས་ན་རྒྱུ་མེད་པའི་རྐྱེན་དུ༌[^138]མི་འགྱུར་བར་སེམས་ན། དེ་ཡང་མི་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གང་འགག་པ་དང་གང་སྐྱེ་བ་དེ་གཉི་ག་ཡང་ཡོད་པ་མ་ཡིན་ཏེ། མ་འགག་པའི༌[^139]ཕྱིར་དང་། སྐྱེས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 195]
དངོས་པོ་གཉིས་ཡོད་ན། དེ་མ་ཐག་པའི་རྐྱེན་ཉིད་དུ་ཇི་ལྟར་འགྱུར། སྐྱེ་བ་དང་འགག་པ་གཉིས་དུས་གཅིག་ཏུ་རྟོག་ན་ཡང་དེ་མ་ཐག་པ་མི་འཐད་དེ། དུས་མཉམ་པའི་ཕྱིར་རོ། །

[Block 196]
དེའི་ཕྱིར་དེ་མ་ཐག་མི་རིགས། དེ་ལྟར་གང་གི་ཕྱིར་རྣམ་པ་ཐམས་ཅད་དུ་བརྟགས་ན་དེ་མ་ཐག་པ་མི་འཐད་དེ།[^140] དེའི་ཕྱིར་དེ་མ་ཐག་པའི་རྐྱེན་ཡོད་དོ་ཞེས་སྨྲས་པ་གང་ཡིན་པ་དེ་མི་འཐད་དོ། །

[Block 197]
ཡང་ན་འདི་ནི་དོན་གཞན་ཡིན་ཏེ། འདི་ལ་དངོས་པོ་རྣམས་མ་སྐྱེས་པ་ཞེས་བྱ་བ་དེ་ནི་སྔར་བསྒྲུབས་ཟིན་ཏེ། དེའི་ཕྱིར་དངོས་པོ་རྣམས༌[^141]སྐྱེ་བ་མེད་པ་དེ་གྲུབ་པར་བྱས་ནས། །

[Block 198]
བཤད་པ།

[Block 199 [VERSE]]
ཆོས་རྣམས་སྐྱེས་པ་མ་ཡིན་ན། །
འགག་པ་འཐད་པར་མི་འགྱུར་རོ། །

[Block 200]
དངོས་པོ་རྣམས་སྐྱེས་པ་མ་ཡིན་ཞིང་མེད་ན་འགག་པ་འཐད་པར་མི་འགྱུར་ཏེ། མེད་པ་ལ་ཅི་ཞིག་འགག་པར་འགྱུར། དེ་ཕྱིར་དེ་མ་ཐག་མི་རིགས། །དེ་ལྟར་གང་གི་ཕྱིར་དངོས་པོ་འགག་པ་ཉིད་མི་འཐད་པ་དེའི་ཕྱིར་དེ་མ་ཐག་པ་མི་རིགས་སོ། །

[Block 201]
དེ་ནི༌[^142]འགག་པར་རྟོག་ན་ཡང་དེ་མ་ཐག་པ་མི་རིགས་ཏེ། ཇི་ལྟར་ཞེ་ན། འགགས་ན་རྐྱེན་ཡང་གང་ཞིག་ཡིན། སྐྱེས་ནའང་རྐྱེན་དུ༌[^143]ཇི་ལྟར་འགྱུར་ཏེ། དེའི་དོན་ནི་སྔར་རྣམ་པར་བཤད་ཟིན་ཏོ། །

[Block 202]
འདིར་སྨྲས་པ། བདག་པོ་ཉིད་ནི་ཡོད་དོ། །

[Block 203]
བདག་པོའི་དངོས་པོ་ནི་བདག་པོ་ཉིད་དེ། དེ་ཡང་མདོར་བསྡུ་ན་གང་ཡོད་ན་གང་འབྱུང་བ་དང་། གང་མེད་ན་གང་མི་འབྱུང་བ་དེ་ནི་དེའི་བདག་པོ་ཉིད་དོ། །

[Block 204]
བཤད་པ།

[Block 205 [VERSE]]
དངོས་པོ་རང་བཞིན་མེད་རྣམས་ཀྱི། །
ཡོད་པ་གང་ཕྱིར་ཡོད་མིན་ན། །
འདི་ཡོད་པས་ན་འདི་འབྱུང་ཞེས། །
བྱ་བ་དེ་ནི་འཐད་མ་ཡིན། །

[Block 206]
འདི་ལ་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་མེད་པ་ཉིད་ནི་སྔར་ཡང་ཀུན་ཏུ་བསྟན་ཅིང་ཕྱིས་ཀྱང་རྒྱ་ཆེར་སྟོན་ཏོ། །

[Block 207]
དེའི་ཕྱིར་དེ་རབ་ཏུ་གྲུབ་པར་བྱས་ནས་དངོས་པོ་རང་བཞིན་མེད་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 208]
དེ་ལྟར་གང་གི་ཕྱིར་དངོས་པོ་རང་བཞིན་མེད་པ་རྣམས་ཀྱིས༌[^144]ཡོད་པ་ཞེས་བྱ་བ་ཡོད་པའི་དངོས་པོ་མི་འཐད་པ་དེའི་ཕྱིར་གང་ཡོད་ན་འདི་ཡོད་པས་ཞེས་བརྗོད་པར་ནུས་པའི་དངོས་པོ་དེ་ཉིད་མེད་དོ། །

[Block 209]
འདི་ཡོད་པས་ཞེས་བྱ་བ་འདི་ལ་མེད་ན་འདི་འབྱུང་ཞེས་བྱ་བ་དེ་འཐད་པར་ག་ལ་འགྱུར། འདི་ཡོད་པས་འདི་འབྱུང་ཞེས་བྱ་བ་འདི་ལ་མི་འཐད་ན་གང་གི་བདག་པོ་ཉིད་དུ་ཇི་ཞིག་འགྱུར། དེའི་ཕྱིར་བདག་པོ་ཉིད་ཀྱང་མི་འཐད་དོ། །

[Block 210]
འདིར་སྨྲས་པ། རྐྱེན་གྱི་དངོས་པོ་རྣམས་འདི་ལྟར་གྲུབ་པར༌[^145]བྱེད་དོ་ཞེས་བྱ་བ་དེ་སྨྲ་བར་མི་ནུས་མོད་ཀྱི། འོན་ཀྱང་རྐྱེན་རྣམས་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་དག་ལས་འབྲས་བུ་སྐྱེ་བའི་ཕྱིར་ཏེ། འདི་ན་ས་བོན་ལ་སོགས་པ་རྐྱེན་རྣམས་ལས་མྱུ་གུ་ལ་སོགས་པ་འབྲས་བུ་སྐྱེ་བར་མཐོང་སྟེ། དེའི་ཕྱིར་དེ་དག་ལས་འབྲས་བུ་སྐྱེ་བར་མཐོང་ནས་འབྲས་བུའི་རྐྱེན་ནི་འདི་དག་གོ་ཞེས་བྱ་བར་ཤེས་སོ། །

[Block 211]
བཤད་པ།

[Block 212 [VERSE]]
རྐྱེན་རྣམས་སོ་སོ་འདུས་པ་ལས། །
འབྲས་བུ་དེ་ནི་མེད་པ་ཉིད། །
རྐྱེན་རྣམས་ལ་ནི་གང་མེད་པ། །
དེ་ནི་རྐྱེན་ལས་ཇི་ལྟར་སྐྱེ། །

[Block 213]
ཉིད་ཅེས་བྱ་བའི་སྒྲ་ནི་ཁོ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 214]
སོ་སོ་བ་དག་ལ་ཡང་མེད་པ་ཁོ་ན་ཡིན་ལ། འདུས་པ་དག་ལ་ཡང་མེད་པ་ཁོ་ནའོ་ཞེས་བྱའོ། །

[Block 215]
ཁྱོད་ཀྱིས་རྐྱེན་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར་འབྲས་བུ་སྐྱེ་བར་བསྟན་པ་གང་ཡིན་པ་དེ་ཉིད་མི་འཐད་ན། རྐྱེན་འགྲུབ་པར་ག་ལ་འགྱུར་ཇི་ལྟར་ཞེ་ན། གང་གི་ཕྱིར་རྐྱེན་རྣམས་སོ་སོ་བ་དང་འདུས་པ་ལ་འབྲས་བུ་དེ་མེད་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། རྐྱེན་རྣམས་སོ་སོ་བ་དང་འདུས་པ་ལ་མེད་པ་ཉིད་གང་ཡིན་པ་དེ་ཇི་ལྟར་དེ་དག་ལས་སྐྱེ་བར་འགྱུར། འབྲས་བུ་སྐྱེ་བ་མེད་ན་ཁྱོད་ཀྱིས༌[^146]རྐྱེན་འགྲུབ་པར་ག་ལ་འགྱུར། དེ་ལ་འདི་སྙམ་དུ་རྐྱེན་རྣམས་ལས༌[^147]འབྲས་བུ་ཡོད་པ་ཁོ་ནར་སེམས་ན། དེ་ལྟ༌[^148]ན་ཡང་རྐྱེན་འཐད་པ་མ་ཡིན་ཏེ། འདི་ལྟར་ཡོད་པ་ལ་རྐྱེན་གྱིས་བྱ་བ་མེད་དེ་སྐྱེས་ཟིན་པ་ཡང་སྐྱེད༌[^149]མི་དགོས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
