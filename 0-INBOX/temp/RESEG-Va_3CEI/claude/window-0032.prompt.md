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

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

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
[Block 1121]
དེ་ལ་གང་། སེམས་ཅན་ལ་གནོད་པར་བྱེད་པ་དགའ་བ་ནི་འཚེ་བ་ཞེས་བྱའོ། །

[Block 1122]
ཁོང་ཁྲོ་བའི་དབང་གིས་ཞེ་ལ་འཛིན་པ་ནི་ཁོན་དུ་འཛིན་པ་ཞེས་བྱའོ། །

[Block 1123]
ཉེས་པས་རྐྱེན་བྱས་ཏེ། སྨྲེ་སྔགས་འདོན་པ་ནི་འཁྲུག་པ་ཞེས་བྱ་སྟེ། འདི་གསུམ་ནི་ཞེ་སྡང་གི་རང་བཞིན་ནོ། །

[Block 1124]
བདག་གི་ཉེས་པ་འཆབ་ཅིང་ཕ་རོལ་པོའི་སྐྱོན་རྟོག་པ༌[^1119]དང་གཞན་གྱི་ཡིད་དང་སྦྱོར་ཏེ་ཚུལ་འཆོས་པ་ནི་གཡོ་ཞེས་བྱའོ། །

[Block 1125]
བཀུར་སྟིའི༌[^1120]ཕྱིར་ཡོན་ཏན་སྒྱུས་སྟོན་པ་ནི་བརྫུན་ཞེས་བྱ་སྟེ་འདི་གཉིས་ནི་འདོད་ཆགས་དང་གཏི་མུག་གི་རང་བཞིན་ནོ། །

[Block 1126]
དར་ཅིང་རྒྱགས་པ་ལ་ཆགས་པར་བྱེད་པ་ནི་ང་རྒྱལ་ཞེས་བྱ་སྟེ་འདོད་ཆགས་ཀྱི་རང་བཞིན་ནོ། །

[Block 1127]
སེམས་ཅན་དག་དྲི་མ་དྲུག་པོ་མང་བའི་ཕྱིར་དགེ་སྦྱོང་དུ་མི་ཤེས། དགེ་བའི་ཆོས་མི་སྤྱོད་པ་ནི་སེམས་ཅན་གྱི་རྙོག་པའོ། །

[Block 1128]
སེར་སྣ་དང་འཇུངས་པ་དང་། ཕྲག་དོག་ནི་ཉོན་མོངས་པའི་རྙོག་པ་སྟེ། ཆོས་དང་ཟང་ཟིང་བདོག་པ་གཏོང་མི་ཕོད་པ་ནི་སེར་སྣ་ཞེས་བྱའོ། །

[Block 1129]
མ་ཐོབ་པའི་ཟང་ཟིང་ལ་ཐོབ་པར་བྱེད་པའི་ཐབས་སྦྱོར་ཏེ་ཆགས་ཤིང་རེ་བ་ནི་བརྐམ་པ༌[^1121]ཞེས་བྱའོ། །

[Block 1130]
དགེ་བའི་རྩ་བ་ཆུང་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་མི་དགེ་བའི་རྩ་བའོ། །

[Block 1131]
དེ་ལྟར་ན་སེམས་ཅན་དགེ་བ་ཆུང་བས་ལྷ་དང་མི་ནི་འགྲིབ།[^1122] ངན་སོང་ནི་འཕེལ་ཞིང་སྐྱེ་སྟེ། སེམས་ཅན་དག་ཐེག་པ་ཆེན་པོ་ལ་ཅིག་ཅར་དགོད་པར་དཀའ་བས་སངས་རྒྱས་རྣམས་ཐབས་མཁས་པས་སངས་རྒྱས་ཀྱི་ཐེག་པ་གཅིག་པོ་དེ་ལས་ཐེག་པ་གསུམ་དུ་བཅད་དེ་བསྟན་ཏོ། །

[Block 1132 [HEADING]]
###### ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པ་ཇི་ལྟར་ཤེས་པ། ^4-2-10-2-2-0

[Block 1133]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་ལྟར་ཞེས་པ་ནས་སངས་རྒྱས་ཀྱང་མ་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པས་ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པ་ལ་མི་སྟོན་ཏོ་ཞེས་ཐེ་ཚོམ་དུ་གྱུར་པ་འགྲོ་བ་སྟེ་དེ་དག་ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པ་ཇི་ལྟར་ཤེས་ཤེ༌[^1123]ན་དེ་ལ་རྣམ་པ་གསུམ་སྟེ། ཡང་དག་པ་མ་ཡིན་པ་ཐེག་པ་གཉིས་ཀྱི་འཕགས་པའི་མཚན་ཉིད་བསྟན་པ་དང་། ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པའི་མཚན་ཉིད་བསྟན་པ་དང་། ཡང་དག་པའི་འཕགས་པ་བསྡུས་པའི་མཚན་ཉིད་དོ། །

[Block 1134 [HEADING]]
###### **ཡང་དག་པ་མ་ཡིན་པ་ཐེག་པ་གཉིས་ཀྱི་འཕགས་པའི་མཚན་ཉིད།** ^4-2-10-2-2-1-0

[Block 1135]
འདིར་ནི་ཡང་དག་པ་མ་ཡིན་པ་བསྟན་པ་སྟེ། ཉན་ཐོས་དང་རང་སངས་རྒྱས་འཕགས་པ་ཡང་དག་པར༌[^1124]རབ་ཏུ་ཞི་བ་ལ་ཞུགས་པ་ནི། སངས་རྒྱས་དང་ཕྲད་ཀྱང་ཕལ་ཆེར་ཐེག་པ་ཆེན་པོའི་ཆོས་དང་མི་ཕྲད་དོ། །

[Block 1136]
གང་རིགས་མ་ངེས་ཤིང་སེམས་བསྐྱེད་པ་ནི་ཐོས་མ་ཐག་ཏུ་ཉན་པ་དང་། འཇུག་པ་དང་། ཁོང་དུ་ཆུད་པར་གྱུར་ཏེ།[^1125] དེ་ནི་འཕགས་པ་ཡང་དག་པའོ། །

[Block 1137]
གང་དེ་ལྟར་མི་ཤེས་པ་དེ་ནི་སངས་རྒྱས་ཀྱི་ཉེ་གནས་མ་ཡིན་ཏེ། འཕགས་པ་ཡང་དག་པ་མ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1138 [HEADING]]
###### **ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པའི་མཚན་ཉིད།** ^4-2-10-2-2-2-0

[Block 1139]
མདོ་ལས་འདི་ལྟར་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་ང་རྒྱལ་ཅན་དུ་ཤེས་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པའི་མཚན་ཉིད་བསྟན་པ་སྟེ། མ་རབས་བསམ་གཏན་བཞི་པ་ཐོབ་པ་འབྲས་བུ་གསུམ་གྱི་ཉོན་མོངས་པ་མ་ཟད་པ་དགྲ་བཅོམ་པའི་འབྲས་བུ་ཕུང་པོ་ནང་གི་ཐ་མ་མྱ་ངན་ལས་འདའ་བ་ཐོབ་སྙམ་སྟེ། སངས་རྒྱས་མི་འདོད་པ་ནི་ང་རྒྱལ་ཅན་ཞེས་བྱའོ། །

[Block 1140 [HEADING]]
###### **ཡང་དག་པའི་འཕགས་པ་བསྡུས་པའི་མཚན་ཉིད།** ^4-2-10-2-2-3-0

[Block 1141]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེས་པ་ནས་གནས༌[^1126]མ་ཡིན་ནོ་ཞེས་པའི་བར་དུ་ནི་ཡང་དག་པའི་འཕགས་པ་བསྡུས་པའི་མཚན་ཉིད་བསྟན་པ་སྟེ། འཕགས་པ་ཡང་དག་པ་དང་ཕྲད་པ་རབ་ཏུ་ཞི་བ་ལ་ཞུགས་པ་ན༌[^1127]ཕལ་ཆེར་ཆོས་དང་ཕྲད་དོ་དེ་དག་སྤྱོད་མི་ནུས་ཀྱང་དད་ཅིང་ཡིད་ཆེས་པར་བྱེད་དོ། །

[Block 1142]
གང་རིགས་མ་ངེས་པ་ནི་ཐོས་ནས་ཀྱང་འཇུག་ཅིང་སྤྱོད་པར་བྱེད་དེ་དེ་བས་ན་དེ་བཞིན་གཤེགས་པ་དང་མངོན་སུམ་དུ་གྱུར་ཏེ་ཆོས་འདི་ཐོས་ནས་དད་པར་མི་འགྱུར་བའི་སྐབས་མེད་དེ་གནས་མ༌[^1128]ཡིན་ནོ་ཞེས་སྨོས་སོ། །

[Block 1143 [HEADING]]
###### བསྟན་པའི་སྣོད་དུ་ཇི་ལྟར་འགྱུར་བ། ^4-2-10-2-3-0

[Block 1144]
མདོ་ལས་དེ་བཞིན་གཤེགས་པ་མྱ་ངན་ལས་འདས་པ་ནི་མ་གཏོགས་སོ་ཞེས་པ་ནི་སྐབས་འདིར་ཇི་ལྟར་ཆོས་ཀྱི་སྣོད་དུ་འགྱུར་ཞེས་བའི་ཐེ་ཚོམ་བསྟན་པ་སྟེ། ལ་ལ་ནི་སངས་རྒྱས་ལས་ཆོས་ཐོས་ནས་སྐུར་བའི་སེམས་སྐྱེ་སྟེ། ཅིའི་ཕྱིར་ན་དེ་བཞིན་གཤེགས་པས་ཁ་ཅིག་ལ༌[^1129]སངས་རྒྱས་སུ་མི་འགྱུར་པ་དང་ཆོས་ཀྱི་སྣོད་དུ་མི་འགྱུར་བ་ཞེས་བསྟན་པ་ཐེ་ཚོམ་སྐྱེས་ཏེ། དེ་ལྟར་སྣོད༌[^1130]དུ་མ་གྱུར་པའི་སེམས་ཅན་ལ་ཆོས་སྟོན་པ་མི་མཛད་ན་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཞེས་བྱ་བར་རུང་ངམ་ཞེས་པའི་དོགས་པ་བསལ་བའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་མྱ་ངན་ལས་འདས་པ་ནི་མ་གཏོགས་སོ་ཞེས་སྨོས་སོ། །

[Block 1145]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེས་པ་ནས་མི་འབྱུང་ཞེས་པའི་བར་དུ་ནི༌[^1131]མྱ་ངན་ལས་འདས་ནས་ཐབས་མི་མཁས་པ་རབ་ཏུ་ཞི་བ་ལ་ཞུགས་པ་ཆོས་འདི་དང་ཕྲད་ཀྱང་མདོ་སྡེ་འདི་ལྟ་བུ་འཛིན་པའམ་འཆད་པ་མི་འབྱུང་ངོ་ཞེས་སྨོས་སོ། །

[Block 1146]
མདོ་ལས་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་ཐེ་ཚོམ་མེད་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་གང་ཆོས་དང་ཕྲད་པ་ནི་ང་མྱ་ངན་ལས་འདས་ཀྱང་སངས་རྒྱས་གཞན་དང་ཕྲད་དེ་ཐབས་མཁས་པས་བསྟན་ན་ཆོས་འདི་ལ་ཐེ་ཚོམ་མེད་པར་འགྱུར་རོ་ཞེས་སྨོས་སོ། །

[Block 1147 [HEADING]]
###### ཇི་ལྟར་ན་བརྫུན་དུ་མི་འགྱུར་བ། ^4-2-10-2-4-0

[Block 1148]
མདོ་ལས་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་སངས་རྒྱས་ཀྱི་ཐེག་པའོ་ཞེས་པའི་བར་དུ་ནི་སྔར་ཐེག་པ་གསུམ་བསྟན་པ་ལས།

[Block 1149]
ད་ཐེག་པ་གཅིག་བསྟན་ཞེས་པའི་ཐེ་ཚོམ་བཅད་པ་སྟེ། སྔར་བསྟན་པ་དང་ཕྱིས་གསུངས་པ་མི་མཐུན༌[^1132]ཡང་བརྫུན༌[^1133]དུ་མི་འགྱུར་བ་ནི་ང་འབའ་ཞིག་གིས་མཁྱེན་གྱི་ཁྱེད་མི་ཤེས་པས་དད་པར་གྱིས་ཤིག །ཡིད་ཆེས་པར་གྱིས་ཤིག །ཁྱེད་ཐོག་མ་སེམས་བསྐྱེད་པས་རྟོགས་པར་གྱིས་ཤིག །དགྲ་བཅོམ་པའི་སེམས་བསྐྱེད་ནས་བསྐལ་པ་སྟོང་ཕྲག་ཉི་ཤུ་འདས་ན་གདོད་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་དུ་སྤྱོད་པའི་དད་པའི་སེམས་དང་འདྲ་བས་ཁྱེད་ཐེ་ཚོམ་མ་བྱེད་པར་ཡིད་ཆེས་པར་གྱིས་ཤིག་དང་ངས་གསུངས་པ་ལ་བརྫུན་མེད་དོ༌[^1134]ཐེག་པ་གཅིག་ཏུ་ཟད་དོ་ཞེས་སྨོས་པ་ཡིན་ནོ། །

[Block 1150 [HEADING]]
#### ཚིགས་བཅད་ཚིག་བརྒྱ་ཉི་ཤུ་རྩ་གཅིག། ^4-2-11-0

[Block 1151]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་དགེ་བསྙེན་མ་རྣམས་ལ༌[^1135]དད་དོ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་ཚིག་བརྒྱ་ཉི་ཤུ་རྩ་གཅིག་ལ་གཉིས་སུ་དབྱེ་སྟེ། ཚིག་བརྒྱ་རྩ་བཅོ་བརྒྱད་ནི་རྐྱང་པ་བཟླས༌[^1136]སོ། །

[Block 1152]
ཚིག་གསུམ་ནི་གཞུང་འོག་མ་དང་མཚམས་སྦྱོར་བའོ། །

[Block 1153 [HEADING]]
##### རྐྱང་པ་བཟླས་པ། ^4-2-11-1-0

[Block 1154]
སྔ་མ་ལ་ཡང་རྣམ་པ་གཉིས་སུ་དབྱེ་སྟེ་ཚིག་བརྒྱ་རྩ་བཅོ་ལྔས་ནི་སྔར་ལུང་བསྟན་པ་རྣམ་པ་གཉིས་པོ་སྟོན་ཏོ། །

[Block 1155 [HEADING]]
###### ལུང་བསྟན་པ་རྣམ་པ་གཉིས། ^4-2-11-1-1-0

[Block 1156]
ཚིག་གསུམ་གྱིས་ནི་ཐེ་ཚོམ་བཞི་བསལ་བ་བསྟན་པ་སྟེ༌[^1137]སྔ་མ་ལ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 1157 [HEADING]]
###### **ལུང་བསྟན་པ་ལས་ངན་པ་སྐྱོན་ཅན་ཕྱིར་དོང་བ།** ^4-2-11-1-1-1-0

[Block 1158]
སྔ་མའི་ཚིག་བཞིས་ནི་ལུང་བསྟན་པ་ལས་ངན་པ་སྐྱོན་ཅན༌[^1138]ཕྱིར་དོང་བ་བསྟན་ཏོ། །

[Block 1159]
ཚིག་བརྒྱད་ཅུ་རྩ༌[^1139]གཅིག་གིས་ནི་ལུང་བསྟན་པ་བསྟན་ཏོ། །

[Block 1160]
ཚིག་སྔ་མ་བཞི་པོ་ལས་ཚིག༌[^1140]སྔར་སྨོས་པ་གཅིག་གིས་ནི་ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པ་བསྟན་ཏོ། །
--- END BLOCKS ---
