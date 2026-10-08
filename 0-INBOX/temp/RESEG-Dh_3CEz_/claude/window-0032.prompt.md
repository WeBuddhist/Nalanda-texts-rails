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
[Block 1121 [HEADING]]
##### སྔོན་བྱུང། ^1-7-1-1-0

[Block 1122]
འདིའི་དོན་ནི་སྔོན་བྱུང་དང་རྗེས་འཇུག་རྣམ་པ་གཉིས་ཏེ། སྔོན་བྱུང་ནི་རྡོ་རྗེ་འཆང་གི་འཁོར་ན་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་དང་རྡོ་རྗེ་མཁའ་འགྲོ་མ་རྣམས་འདུ་བའི་དུས་སུ་ལུས་ཀྱི་བརྡ་རྣམས་དང༌[^529]འོག་ནས་འབྱུང་བའི་ངག་གི་བརྡ་རྣམས་བརྡ་དང་བརྡའི་ལན་དུ་བསྟན་ཏེ།

[Block 1123 [HEADING]]
##### རྗེས་འཇུག། ^1-7-1-2-0

[Block 1124]
རྡོ་རྗེ་སྙིང་པོ་ལ་སོགས་པ་མ་འོངས་པའི་དུས་སུ༌[^530]བརྡ་དང་ངག་གི་བརྡ་རྣམས་ཀྱིས། རྣལ་འབྱོར་ཕ་དང་རྣལ་འབྱོར་མ་རྣམས་སོ་སོར་འདུ་བའི་བརྡ་དང་མན་ངག་མཚོན་པའི་བརྡ་སྟེ། འཇིག་རྟེན་པ་ལས་བཟློག་པས་ནི༌[^531]དྲི་བ་ཡང་གཡོན་པས་བྱས༌[^532]ལ། ལན་ཀྱང་གཡོན་པས་གདབ་པོ། །སྔར་གྱི་ཚེ་ལ་བརྡ་རྐྱང་པའི་ལན་དུ་ཀུན་ལ་སྦྱར་བར་བྱའོ། །

[Block 1125]
བརྟུལ་ཞུགས་དམ་ཚིག་ཤིན་ཏུ་ནོས། །ཞེས་པ་ནི་སྙོམས་འཇུག་གི་སྤྱོད་པ་ལ་གནས་པའོ། །

[Block 1126]
ད་ནི་དེ་བཞིན་དུ་གཞན་ལ་ཡང་གདམས་པའི་ཕྱིར་རོ། །

[Block 1127 [VERSE]]
ཕྱི་རོལ་དེར་ནི་འདུས་པ་ལ། །
ཞེས་པ་ནི་ཕྱིའམ་ནང་གི་འདུ་བ༌[^533]ཀུན་ལའོ། །

[Block 1128]
བཟང་པོའི་སྤྱོད་ཡུལ་ལ་གནས་ཞེས་པ་ནི་གནས་ས་ལ་སོགས་པ་བཟང་པོར་འདུ་བའོ། །

[Block 1129]
དེ་ཡང་ཕྱིའི་འདུ་བ་ཡིན་ལ་ནང་གི་བཟང་པོ་ནི་རྣལ་འབྱོར་པའོ། །

[Block 1130]
སྤྱོད་ཡུལ་ནི་མའོ། །

[Block 1131]
འདུ་བར་བརྡར་བསྟན་ཞེས༌[^534]པ་ནི་རིགས་པའི༌[^535]བརྟུལ་ཞུགས་ཀྱི་ཐབས་སོ། །

[Block 1132 [VERSE]]
ཡང་བཟང་པོ༌[^536]ནི་ཉིན་མོ་ལ་འཚོག་པའི༌[^537]དུས་སོ། །
སྤྱོད་ཡུལ་ཏེ་མཚན་མོ་ལ་སྤྱོད་པའི་དུས་སོ། །

[Block 1133]
རྣལ་འབྱོར་མས་སྨྲས་དེ་ནི་བྱ་བ་ཐམས་ཅད་ཅེས་པ་ནི་ཕྲེང་བ་སྟོན་པ་སྟེར་བ་སྟེ། རྡོ་རྗེ་སྙིང་པོ་ལ་གདམས་པ་ལ་དེ་ལྟར་བྱའོ། །

[Block 1134]
ད་ནི་གནས༌[^538]ལ་སོགས་པ་བསྟན་པ་ལ་ཡང་དབང་དང་མན་ངག་གིས་རྣལ་འབྱོར་མ་མཚོན་པ་ཡིན་ལ། བརྟུལ་ཞུགས་འདུ་བའི་གནས་ནི་གང་དག་ཏུ་སྤྱོད་པ་བྱ་ཞེ་ན། དེའི་སླད༌[^539]དུ་དྲིས་པ་དང་ལན་བསྟན་པ་ནི།

[Block 1135 [VERSE]]
གནས་དང་ཉེ་བའི་གནས་དང་ནི། །
ཞིང་དང་ཉེ་བའི་ཞིང་ཉིད་དང་། །
ཚནྡོ་ཉེ་བའི་ཚནྡོ་དང་། །
དེ་བཞིན་འདུ་བ་ཉེ་འདུ་བ། །

[Block 1136 [VERSE]]
འཐུང་གཅོད་ཉེ་བའི་འཐུང་གཅོད་ཉིད། །
དུར་ཁྲོད་ཉེ་བའི་དུར་ཁྲོད་ཉིད། །
འདི་རྣམས་ས་ནི་བཅུ་གཉིས་ཏེ། །
ས་བཅུའི་དབང་ཕྱུག་མགོན་པོ་ཉིད། །

[Block 1137 [VERSE]]
འདིས་ནི་གཞན་གྱི༌[^540]བརྗོད་མིན་བྱ། །
ཞེས་པ་ནི་རྟག་ཏུ་གནས་ཤིང་།
སྤྱོད་པས་ན་གནས་ཞེས་བྱའོ། །

[Block 1138 [VERSE]]
ཡང་རྣལ་འབྱོར་པ་ཞུགས་པས༌[^541]ན་ཡང་གནས་ཞེས་བྱའོ། །
དེ་དང་ཉེ་བས་ན་ཉེ་བའི་གནས་ཞེས་བྱའོ། །
ཡོན་ཏན་སྐྱེད་པར་བྱེད་པས་ན་ཞིང་།
ཡང་ན་རྣལ་འབྱོར་མ༌[^542]གནས་པས་ན་ཞིང་ཞེས་བྱའོ། །

[Block 1139]
དེ་དང་ཉེ་བས་ན་ཉེ་བའི་ཞིང་ངོ་། །

[Block 1140 [VERSE]]
འདོད་ཅིང་འདུན་པ་སྐྱེད་པས༌[^543]ན་ཚནྡོ། །
དེ་དང་ཉེ་བས་ན་ཉེ་བའི་ཚནྡོ། །

[Block 1141]
མ་ག་ངྷ་དང་ཨངྒ་མ་ཏ་ནི་གནས་ཀྱི་གཞི་ཡིན་ཏེ་འདུ་བ༌[^544]ཞེས་བྱའོ། །

[Block 1142]
དེ་དང་ཉེ་བས་ན༌[^545]ཉེ་བའི་འདུ་བའོ། །

[Block 1143]
འདི་ནས་བོས་པས་གནས་གཞན་ཐམས་ཅད་རྒྱས་པར་འཆད་དོ།[^546] །འདི་ཉིད༌[^547]ལ་རྒྱས་པར་བཤད་པ་མེད་དོ། །

[Block 1144]
བར་ཆད་མེད་པས་ན་འཐུང་གཅོད། དེ་དང་ཉེ་བས༌[^548]ཉེ་བའི་འཐུང་གཅོད་དོ།[^549] །རྣམ་པར་རྟོག་པ་མི་འབྱུང་བ་དང་རོ་མང་པོ་གནས་པས་དུར་ཁྲོད་དོ། །

[Block 1145]
དེ་དང་ཉེ་བས་ན༌[^550]ཉེ་བའི་དུར་ཁྲོད་དོ། །

[Block 1146]
འདི་རྣམས་ནི་ས་བཅུ་གཉིས་ཏེ་ཞེས་པ་ནི་རབ་ཏུ་དགའ་བ་ནས་བཅུ་གཉིས་དཔེས༌[^551]བསྐྲུན་དུ་མེད་པའི་བར་དུའོ། །

[Block 1147]
ས་བཅུའི༌[^552]དབང་ཕྱུག་ཅེས་པ་ནི་རྣལ་འབྱོར་གྱི་དབང་ཕྱུག་དང་། རྣལ་འབྱོར་མ་རྣམས་སོ། །

[Block 1148]
དེ་དག་ནི་བགྲོད་པའི་སའོ། །

[Block 1149]
མགོན་པོ་ཉིད་ཅེས་པ་ན།[^553] བུདྡྷའི་ས་གསུམ་སྟེ། བཅུ་གཅིག་ཀུན་དུ་འོད་ཀྱི་ས་དང་། བཅུ་གཉིས་པ་དཔེས༌[^554]བསྐྲུན་དུ་མེད་པའི་ས་དང་བཅུ་གསུམ་པ་རྡོ་རྗེ་འཛིན་པའི་ས་སྟེ་མགོན་པོའི་ས་གསུམ་མོ། །

[Block 1150]
འདིས་ནི་གཞན་གྱི་བརྗོད་མིན་ཞེས་པ་ནི། རབ་ཏུ་དགའ་བ་ལ་སོགས་པའི་མིང་གིས་མི་གདགས་ཀྱི༌[^555]གནས་ལ་སོགས་པའི་མིང་གིས་བཏགས་པའོ། །

[Block 1151]
བྱང་ཆུབ་སེམས་དཔའི་མིང་གིས་མི་གདགས་ཀྱི་རྣལ་འབྱོར་གྱི་དབང་ཕྱུག་གི་མིང་གིས༌[^556]བཏགས་སོ། །

[Block 1152 [HEADING]]
#### བཤད་ཚུལ་རྣམ་པར་སྦྱར་བ། ^1-7-2-0

[Block 1153 [HEADING]]
##### ཕྱི་ལྟར་བཤད་པ། ^1-7-2-1-0

[Block 1154]
འདི་ཡང་བཤད་ཚུལ་རྣམ་པར་སྦྱར་ཏེ། ཕྱི་ལྟར་བཤད་པ་ནི་གང༌[^557]གི་བཅུ་གཉིས་པོ་དེ་འཛམ་བུའི་གླིང་གི་ཡུལ་སུམ་ཅུ་རྩ་གཉིས་སུ་འོག་ནས༌[^558]རྒྱས་པར་འཆད་དོ། །

[Block 1155 [HEADING]]
##### ནང་ལྟར་བཤད་པ། ^1-7-2-2-0

[Block 1156]
ནང་ལྟར་བཤད་པ༌[^559]ལུས་ཀྱི་གནས་ཉི་ཤུ་རྩ་བཞི་ལ་སྦྱར་བ་དང་རྩ་སུམ་ཅུ་རྩ་གཉིས་སུ་སྦྱར་ཏེ་གནས་དང་ལས་དང་བྱ་བ་རྣམས་བྱེད་དོ། །

[Block 1157]
དེ་སྐད་དུ།

[Block 1158 [VERSE]]
སྤྱི་གཙུག་ཛཱ་ལནྡྷ་རར་བཤད། །
ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1159 [HEADING]]
##### གསང་བ་ལྟར་བཤད་པ། ^1-7-2-3-0

[Block 1160]
གསང་བ་ལྟར་བཤད་པ་ནི་གསང་བའི་གནས་ཀྱི་ཁྱད་པར་ཏེ། རྩ་གནས་བརྒྱ་པའི་བྱེ་བྲག་ལ་ཅི་རིགས་པར་སྦྱར་རོ། །
--- END BLOCKS ---
