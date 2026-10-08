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

[Block 1161 [HEADING]]
##### དེ་ཁོ་ན་ཉིད་ལྟར་བཤད་པ། ^1-7-2-4-0

[Block 1162]
དེ་ཁོ་ན་ཉིད་ལྟར་བཤད་པ༌[^560]ནི།

[Block 1163 [VERSE]]
གནས་ནི་རབ་ཏུ་དགའ་བར་བརྗོད། །
ཉེ་གནས་དྲི་མ་མེད་ཅེས་བྱ། །
ཞིང་ནི་འོད་བྱེད་པ་ཡིན་ཏེ། །
ཉེ་བའི་ཞིང་ནི་འོད་འཕྲོ་ཅན། །

[Block 1164 [VERSE]]
ཚནྡོ་ལྔ་པ་སྦྱང་དཀའ་བ། །
ཉེ་བའི་ཚནྡོ་མངོན་དུ་གྱུར། །
དེ་བཞིན་འདུ་བ་རིང་དུ་སོང་། །
ཉེ་བའི་འདུ་བ་མི་གཡོ་བ། །

[Block 1165 [VERSE]]
འཐུང་གཅོད་ལེགས་པའི་བློ་གྲོས་ཏེ། །
ཉེ་བའི་འཐུང་གཅོད་ཆོས་ཀྱི་སྤྲིན། །
དུར་ཁྲོད་ཀུན་དུ་འོད་ཀྱི་ས། །
ཉེ་བའི་འཐུང་གཅོད་བསྒྲུན་དུ་མེད། །

[Block 1166]
འདི་རྣམས་ས་ནི་བཅུ་གཉིས་སོ། །

[Block 1167 [VERSE]]
རྡོ་རྗེ་འཛིན་པའི༌[^561]ས་བཅུ་གསུམ་པ་ནི་མཐར་ཐུག་པ༌[^562]སྟེ།
ཕ་རོལ་ཏུ་ཕྱིན་པ་བས་ནི་མི༌[^563]ཐོབ་བོ། །

[Block 1168]
དེ་ཅིའི་ཕྱིར་ཞེ་ན། རྒྱུའི་ཁྱད་པར་ལས་འབྲས་བུའི་ཁྱད་པར་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1169]
སློབ་དཔོན་ལ་ལ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། གསང་སྔགས་ཀྱི་སྤྱོད་པ་གཉིས་ཀ་ལ་བརྟེན་ནས་ལམ་སོ་སོའི་འབྲས་བུ་སོ༌[^564]སོར་ཐོབ་པར་འདོད་དོ། །

[Block 1170]
སློབ་དཔོན་ལ་ལ་དག་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ནི་ངེས་པར་འབྱུང་བ་ཐོབ་ཀྱི་མཐར་ཐུག་པ་ནི་ཐོབ་པར་མི་འདོད་དོ།[^565] །ལུང་ལས་ཀྱང་རིགས་ཀྱི་བུ་ཁྱོད་ཀྱིས་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས༌[^566]དེ་ཁོ་ན་ཉིད་མ་རྟོགས་པར་དཀའ་བ་རྣམ་པ་སྣ་ཚོགས་པ་སྤྱོད༌[^567]ཅིང་ཇི་ལྟར་ན་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་བྱ་སྙམ་ཞེས་གསུངས་པ་དང་སློབ་དཔོན་ལ་ལ་དག་གིས་ཀྱང་། འདིས་ནི་མཐར་ཐུག་མི་ཐོབ་སྟེ། །ཞེས་གསུངས་པ་དང་། རྡོ་རྗེ་འཛིན་པའི་ས་དགེ་བ།[^568] །བཅུ་གསུམ་པར་ཡང་གསུངས་པ་ཡིན། །ཞེས༌[^569]གསུངས་པ་དང་། མཐར་ཐུག་པ་མི་ཐོབ་པར་བསྟན་པ་དང་།

[Block 1171]
ཡང་ལུང་ལས།

[Block 1172 [VERSE]]
ཐེག་པ་གསུམ་གྱི་ངེས་འབྱུང་ལ། །
ཐེག་པ་གཅིག་གི་འབྲས་བུར་གནས། །

[Block 1173]
ཞེས་གསུངས་སོ། །

[Block 1174]
ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཐེག་པས་ནི་ས་བཅུ་གསུམ་པ་བཤད་པ་མེད་དོ། །

[Block 1175]
རིགས་པ༌[^570]ནི་རྒྱུའི་ཁྱད་པར་ལས་འབྲས་བུའི་ཁྱད་པར་ཡོད་དེ། ཇི་སྲིད་དུ་ཕྱག་རྒྱ་ཆེན་པོ་དོན་རང་གི་མཚན་ཉིད་ཉམས་སུ་མ་མྱོང་བར་དངོས་པོ་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་མི་རྟོགས་ཏེ། དེའི་ཕྱིར་ན་ཡང་མཐར་ཐུག་པ་མི་ཐོབ་བོ། །

[Block 1176]
ཕ་རོལ་ཏུ་ཕྱིན་པར་ནི་རྗེས་སུ་དཔག་པས་གཏན་ལ་འབེབས་པར་བྱེད་པས་ལྟ་བ་ཡང་སྤྱི་ཙམ་གཏན་ལ་འབེབས། སྒོམ་པ་ཡང་ཡིད་ཨུ་ལི་ཀ་སྙམ་དུ་སེམས་པ་སྤྱིའི་སྒོམ་པ་ཙམ་སྟེ། དེའི་ཕྱིར་མཐར་ཐུག་པ་མི་ཐོབ་པའོ། །

[Block 1177]
དེ་དག་གི་གཞུང་གིས་ཀྱང་ཐབས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་ནུས་པའི་མཐུ་ནི་དགག་པར་མི་ནུས་ལ་མངོན་སུམ་དང་རྗེས་སུ་དཔག་པར་ནི་ཐུན་མོང་དུ་མཚུངས་པས་རྒྱུའི་ཁམས་ཀྱི་ཁྱད་པར་ནི་དེ་ཙམ་མོ། །

[Block 1178]
རིགས་པ་མང་དུ་ཡོད་ཀྱང་འདིར་མ་སྤྲོས་སོ། །

[Block 1179]
གོང་གི་ཕྱིའི་གནས་རྒྱས་པར་བཤད་པར་འདོད་ནས། ཀྱེ་བཅོམ་ལྡན་འདས་གནས་ལ་སོགས་པ་གང་ལགས་ཞེས་བྱ་སྟེ། རྡོ་རྗེ་སྙིང་པོས་གསོལ་བ་ཞེས་པ་ཁ་སྐོང་ངོ་། །བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ཞེས་པ་ལ་སོགས་པ༌[^571]ཡུལ་སུམ་ཅུ་རྩ་གཉིས་ལ་སོགས་པ་གོ་སླའོ། །

[Block 1180]
ཡང་དུས་བསྟན་པའི་ཕྱིར་ཅུང་ཟད་གོ་རིམས་བཟློག་སྟེ། ཀྱེ་བཅོམ་ལྡན་འདས་ཉི་མ་གང་ལགས་ཞེས་དྲིས་པའོ། །

[Block 1181]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ཞེས་པ་ནི་ལན་སྟོན་མཁན་སྡུད་པ་པོས་བརྗོད་པའོ། །

[Block 1182]
སེམས་ཅན་གྱི་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་ནི་ཞལ་གྱིས་བཞེས་པ་སྟེ། ཀྱང་ཞེས་པ་ནི་ཉིན་མོ་འཚོག་ཅིང་འཇུག་པའི་དུས་སོ། །

[Block 1183]
མཚན་མོ༌[^572]སྤྱོད་པའི་དུས་ཀྱང་མཚོན་ནོ། །

[Block 1184]
དུས་དེ་ཉིད་ནི་ཡི་དགས་ཟླ་ཕྱེད་དེ་ཚིག་རྐང་གཉིས་སོ། །

[Block 1185]
ཡི་དགས་ཟླ་ཕྱེད་ནི་མར་ངོའོ། །

[Block 1186]
བཅུ་བཞི་ནི་ཉི་ཤུ་དགུའོ།[^573] །

[Block 1187]
བརྒྱད་པ་ནི་ཉི་ཤུ་གསུམ་མོ། །

[Block 1188 [HEADING]]
#### སྤྱོད་པའམ་ཚོགས་ཀྱི་རྫས་བསྟན་པ། ^1-7-3-0

[Block 1189]
ད་ནི་སྤྱོད་པའམ་ཚོགས་ཀྱི་རྫས་བསྟན་པའི་ཕྱིར། རྒྱལ་མཚན་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་བསྟན་ཏེ། དེ་ཡང་རྫས་སུ་བཤད་པའི་ཚེ་ནི་ཟས་སུ་ཉེ་བར་ལོངས་སྤྱོད་པ་ནི་གཉུག་མ་དང་སྒྲུབ་པའི་རྫས་དེ་རྒྱལ་མཚན་ནི་དཔྱངས་ཏེ་ཤི་བའོ། །

[Block 1190]
མཚོན་བསྣུན་པ་ནི་དཔའ་བོ་གཡུལ་ངོར་ཤི་བའི་ཤའོ། །

[Block 1191]
ལན་བདུན་པ་ནི་སྐྱེ་བ་བདུན་པའི་ཤ་སྟེ་འོག་ནས་དེ་ཉིད་བརྟགས༌[^574]པའི་ཐབས་འཆད་དོ། །

[Block 1192]
བསྒྲུབ་པ༌[^575]ནི་ཡུལ་དང་བསམ་པ་སྦྱོར་བས་གནང་བ་སྟེ། དེ་བསད་པའི་ཤ་སྟེ་བརྟག་པ་ཕྱི་མར་འཆད་དོ། །

[Block 1193]
ལྷན་ཅིག་སྐྱེས་པ་གྲུབ་པ་དེའི་ཚེ་རྒྱལ་མཚན་ནི་ཁམས་དང་བཅས་པ་སྟེ་བྱ་རོག་གི་གདོང་ཅན་ནོ། །

[Block 1194]
མཚོན་བསྣུན་ནི་རིན་ཆེན་ཟེ་འབྲུ་དང་བྱ་རོག་གི་གདོང་ཕྲད་པའོ། །

[Block 1195]
ལན་བདུན་པ་ཡང་བཟའ་བར་བྱ། །ཞེས་པ་ནི་ཟླ་བ་དང་མི་འབྲལ་བར་ཉི་མ་དང༌[^576]ལོངས་སྤྱོད་པའོ། །
--- END BLOCKS ---
