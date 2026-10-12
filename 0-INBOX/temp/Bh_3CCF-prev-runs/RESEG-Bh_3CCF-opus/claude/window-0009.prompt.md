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
[Block 316]
སྔགས་ལ་མཆོག་ཏུ་གཞོལ་བ་སྟེ་དེས་ནི་ཞེས་བྱ་བ་ནི་འཕགས་པ་དེ་ཁོ་ན་ཉིད་བསྡུས་པ་ལས༌[^124]གསུངས་པའི་ཚུལ་ཤེས་པས་རྣལ་འབྱོར་ཙམ་བསྐྱེད་པ་ཡིན་ཡང་གསང་བ་འདུས་པ་དང༌[^125]མཚུངས་པར་བྱ་བ་ནི་མ་ཡིན་ནོ།།

[Block 317]
ཡང་དབང་པོ་གཉིས་ཀྱི་སྦྱོར་བ་ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བའི་ཕྱི་རོལ་གྱི་མེ་ལ་ལྷག་མ་ལ་སོགས་པའི་སྲེག་རྫས་རྣམས་ཕྱིའི་སྦྱིན་སྲེག་བྱེད་པ་དེ་བཞིན་དུ་སྙོམས་པར་འཇུག་པའི་སྦྱོར་བས་ཀྱང་ནང་གི་བདག་ཉིད་ཀྱི་སྦྱོར་བས་ནང་གི་སྦྱིན་སྲེག་བྱ༌[^126]སྟེ། དབབ་པའི་རྡོ་རྗེས་ཞེས་བྱ་བ་ནི་འོད་དཔག་མེད་ཀྱི་རང་གི་ངོ་བོས་ཕབ་ལ་གཟུང༌[^127]ངོ་།།འདི་ཡིས་ནི་སྔོན་དུ་བརྗོད་པའི་དབབ་པའི་ཆོ་ག་གསལ་བར་བྱེད་དོ།།

[Block 318]
དབབ་པ་བྱས་ནས་མི་བསྐྱོད་པ་ལ་སོགས་པས་བསྒྲུབ་བྱའི་ལུས་དང་ངག་དང་ཡིད་ལ་བྱིན་གྱིས་བརླབ་པར༌[^128]མཛད་དོ།།

[Block 319]
ཨ་ཁཾ་བི་ར་ཧཱུཾ་ཞེས་བྱ་བ་འདིས་ནི་སློབ་མ་དཀྱིལ་འཁོར་དུ་གཞུག་པར་བྱའོ།།

[Block 320]
སངས་རྒྱས་ཀུན་གྱི་ཞེས་བྱ་བ་ནི་རྡུལ་ཚོན་གྱི་དཀྱིལ་འཁོར་ལ་བསྒྲུབ་པ་བྱས་ནས་ནང་གི་མཆོད་པ་བྱ་བ་སྟོན་ཏོ།།

[Block 321]
ཡུངས་ཀར་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རྗེས་སུ་ཆགས་པ་སྔོན་དུ་འགྲོ་བའི་གསང་བའི་དབང་བསྐུར་བ་བརྗོད་པ་ཡིན་ནོ།།

[Block 322]
ཡང་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ལྷ་མོ་རྣམས་ཀྱིས་དབང་བསྐུར་བ་ནི་སློབ་མ་ལ་བསམ་པར་བྱའོ།།

[Block 323]
སློབ་དཔོན་ཐམས་ཅད་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཐུགས་ཀྱི་དཀྱིལ་འཁོར་ལ་སོགས་པར་དབང་ལྔ་པ་ལ་སོགས་པའི་དབང་བླ་མས་བསྐུར་བར་བྱའོ།།

[Block 324]
དེ་ཡང་དབང་བསྐུར་བ་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་འདོན་ཅིང་སྦྱིན་ནོ།།

[Block 325]
ཤེས་རབ་དང་ལྡན་པ་ནི་མཱ་མ་ཀཱི་ལ་སོགས་པ་དང་སྙོམས་པར་འཇུག་པའི་སྦྱོར་བ་དང་ལྡན་པ་ལའོ།།

[Block 326]
དམ་ཚིག་དང་སྡོམ་པ་འཛིན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྔགས་དང་བསྒོམ་པ་ལ་སོགས་པ་ལ་དངོས་གྲུབ་བསྒྲུབ་པའི་དོན་ཏོ།།

[Block 327]
ཇི་ལྟར་འདོད་པ་སྨྲ་བའི་སློབ་མ་ལ་རྗེས་སུ་གནང་བ༌[^129]སྦྱིན་པར་བྱ་བ་ནི་བསམ་པ་ཤེས་པར་བྱས་ལ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ཡིན་ནོ།།

[Block 328]
ཁུ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གསང་བའི་དབང་བསྐུར་བ་ལ་སོགས་པ་སྦྱིན་པར་བྱ་བ་ཡིན་པར་སྟོན་ཏོ།།

[Block 329]
གནོད་སྦྱིན་གྱི་གཙོ་བོ་ནི་ཕྱག་ན་རྡོ་རྗེའོ།།

[Block 330]
བསྒྲུབ་བྱར་གྱུར་པའི་གདུག་པ་རྣམས་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་ཀྱི་ལྟ་བ་ཅན་དུ་སུན་འབྱིན་པའི་བློ་ཅན་རྣམས་ལ་ནུས་མཐུ་གསལ་པོར་གྱུར་པའི་རྣལ་འབྱོར་པས་བརྟན་པར་བྱ་བའོ།།

[Block 331]
རྡོ་རྗེ་ཆེན་པོ་བསྒོམ་ཞིང་ཞེས་བྱ་བ་ལ་རྡོ་རྗེ་ནི་རྡོ་རྗེ་སེམས་དཔའོ།།

[Block 332]
བསྒོམ་པ་ནི་དེ་ཞུ་བ་ལས་བྱུང་བའི་ཡི་གེ་ཙུྃ་སྟེ། དེ་ལས་སྐྱེས་པའི་རྡོ་རྗེ་ཆེན་པོ་ནི་སྐུལ་བྱེད་མ་བསམ་པར་བྱ་བ་ཡིན་ནོ།།

[Block 333]
སྐུལ་བྱེད་མ་ཞེས་བྱ་བ་ནི་གདུག་པ་ཅན་གྱི་ལུས་དང་ངག་དང་ཡིད་ལ་འཇོམས་ཤིང་འཇོམས་པར་བྱེད་པ་སྟེ། ལུས་ངག་ཡིད་ཅེས་བྱ་བ་ནི་བཞི་པའི་ཚིག་མང་པོ་བར་བལྟ་བར་བྱའོ།།

[Block 334]
དོན་ནི་འདི་ཡིན་ཏེ་གདུག་པ་ཅན་རྣམས་ཀྱི་ལུས་དང་ངག་དང་ཡིད་རྣམས་འཇོམས་སོ་ཞེས་པའི་དོན་ཏོ།།

[Block 335]
རྡོ་རྗེ་བདུད་རྩི་ཆུ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་རང་བཞིན་དུ་བསམས་ཏེ། སྤྱི་གཙུག་ཏུ་སྦྱིན་པར་བྱའོ།།

[Block 336]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བཅུ་དྲུག་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 337 [HEADING]]
## ལེའུ་བཅུ་བདུན་པ། ^17-0

[Block 338]
ཆོ་འཕྲུལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཤིང་ཨ་མྲ་ལ་སོགས་པར་སྤྲུལ་ནས་མཛད་པ་བསྟན་པ་ཇི་བཞིན་དུ་རང་སངས་རྒྱས་ཀྱང་ལུས་ཉེ་བར་སྤྲུལ་ནས་གདུལ་བྱ་དེ་དག་སེམས་རངས་པར་བྱེད་པར་འདོད་དོ།།

[Block 339]
དེ་ལྟ་བུ་ཉིད་ནི་བཅོམ་ལྡན་འདས་ཀྱི་མཛད་པ་སྟེ། དེ་ཉིད་སྐུ་རྡོ་རྗེ་ལ་གནས་པའི་དམ་ཚིག་ཡིན་ལ། དེ་ཉིད་ཀྱི་རང་སངས་རྒྱས་ཀྱི་རིགས་ཅན་རྣལ་འབྱོར་པས་ཀྱང་དེ་དང་རྗེས་སུ་མཐུན་པའི་ཆོས་བསྟན་པར་བྱའོ།།

[Block 340]
དེ་བཞིན་དུ་ཉན་ཐོས་ལ་སོགས་པའི་དམ་ཚིག་གིས་ཀྱང་དེའི་རིགས་ཅན་ལ་དེ་དང་འཚམ༌[^130]པའི་ཆོས་ཉིད༌[^131]ཉེ་བར་བསྟན་པར་བྱའོ།།

[Block 341]
དེ་བཞིན་དུ་དབང་ཕྱུག་ཆེན་པོའི་གོ་འཕང་ཐོབ་པར་འདོད་པའི་འདོད་ཆགས་ཅན་རྣམས་ལ་འདོད་ཆགས་བསྟེན་པའི་སྒོ་ནས་ཆོས་སྟོན་པར་བྱེད་པ་ནི་དེའི་ཐ་ཚིག་གོ།།

[Block 342]
དེ་བཞིན་དུ༌[^132]ཁྱབ་འཇུག་གི་གོ་འཕང་འཐོབ་པར་འདོད་པ་ལ་ཡང་ཐམས་ཅད་སྟོང་པ་ཉི༌[^133]ཚེ་བ་ཞེས་བྱ་བའི་ཆོས་སྟོན་པ་སྟེ་དེ་དག་ནི༌[^134]སྐུ་རྡོ་རྗེ་ལ་སོགས་པའི་རང་བཞིན་ནོ།།

[Block 343]
གནོད་སྦྱིན་མོ་ལ་སོགས་པའི་དམ་ཚིག་ནི་ཤ་ལ་སོགས་པ་བཟའ་བ༌[^135]དང་སེམས་ཁྲོ་བ་ལ་སོགས་པ་དང་ལྡན་པར་བྱས་པས་གནོད་སྦྱིན་མོ་ལ་སོགས་པ་བསྒྲུབས་པས༌[^136]གཞན་དག་དང་དེ་དག་ཉིད་དུ་བཅས་པ་ཡང་དག་པའི་ལམ་ལ་གཟུད་དོ།[^137] །གནས་ཀྱི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་རང་རང་གི་ཕྱག་རྒྱ་དང་སྔགས་ཀྱི་གཟུང་མ༌[^138]འཁྱུད་དེ་གསད་པ༌[^139]ལ་སོགས་པའི་ལས་རྣམས་བྱའོ།།

[Block 344]
རྡོ་རྗེ་ལས་བྱུང་བ་ནི་འོད་གསལ་བའོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་རྣམས་འོད་གསལ་བའི་རང་བཞིན་འོད་གསལ་བར་བསྐྱེད་པར་བྱའོ།།

[Block 345 [VERSE]]
ཆོས་ནི་མི་དགེ་བ་བཅུ་སྤངས་པའོ། །
ཆོས་མ་ཡིན་པ་ནི་མི་དགེ་བ་བཅུ་པོའོ། །

[Block 346]
བླང་དོར་ལ་ལྟོས་པ་མེད་པར་ཉམས་སུ་ལེན་པ༌[^140]ནི་འོད་གསལ་བའོ།།

[Block 347]
དེ་ཉམས་སུ་བླངས་པས་རྣལ་འབྱོར་པ་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པར་འགྱུར་རོ།།

[Block 348]
དགོས་པའི་དབང་གིས་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ལ་སོགས་པ་ལ་ལུས་དང་ངག་ཙམ་གྱིས་ཕྱག་འཚལ་ཞིང་ལུས་ངག་ཙམ་གྱིས་ཕྱག་བྱ་བ་ཡིན་ནོ།།

[Block 349]
ཕྱི་རོལ་གྱི༌[^141]བཅུད་ཀྱིས༌[^142]ལེན་གང་ཡིན་པ་དེ་ལ་ལྟོས་པ་མེད་པ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་གྱིས་ལུས་བསྟན་པར་བྱེད་པའི་ཆོ་ག་སྟོན་ཏོ།།

[Block 350]
བདུད་རྩི་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་སེམས་དཔའ་ལས་བདུད་རྩི་འཛག་པའི་རང་བཞིན་དབུ་རྒྱན་གྱིས༌[^143]གནས་ཏེ། སྤྱི་གཙུག་ཏུ་གནས་པར༌[^144]བསམ་པར་བྱའོ།།

[Block 351]
རྡོ་རྗེ་ཕྲ་མོ་ནི་ལྕེ་སྟེ་ལྕེ་དེའི་རྩེ་མོ་ཁ་ལ་རེག་པ་ལས་སེམས་མཉམ་པར་གཞག་པར༌[^145]འགྱུར་རོ།།

[Block 352]
རྣལ་འབྱོར་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདག་ཉིད་ཅན་གྱི་རྡོ་རྗེ་འཛིན་པ་སྟེ། བདག་དང་ཁམས་གསུམ་པོ་དེར་མཉམ་པར་ལོངས་སྤྱོད་པར་བྱའོ།།

[Block 353]
ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ནི་མངོན་སུམ་དུ་བྱེད་པའི་ཐབས་ཀྱི་སྦྱོར་བ་རིགས༌[^146]པའོ།།

[Block 354]
སོམ་ཉིར་གྱུར་པ་ནི་དེའི་ཤེས་རབ་ཡིད་གཉིས་ཟོས་ནས་ཕན་ཚུན་དུ་གྲོས་སུ་འགྲོ་བར་བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ།།

[Block 355]
སྐུ་རྡོ་རྗེའི་རྒྱུར་གྱུར་པ་ཞེས་བྱ་བ་ནི་ཕྱག་རྒྱ་ཆེན་པོའི་རྒྱུར་གྱུར་པ་ལ་བྱའོ།།
--- END BLOCKS ---
