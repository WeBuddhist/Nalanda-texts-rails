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
[Block 1191]
བསམ་པ་དང་སྦྱོར་བ་ནི་དགེ་བ་དང་མི་དགེ་བའི་ལས་སོ། །

[Block 1192]
དེ་ལྟར་བསམ་པ་དང་དཔྱོད་པ༌[^1153]དང་དད་པ་སྣ་ཚོགས་མཁྱེན་པས་གདོན་མི་ཟ་བའི་ཚིག་དང་རྒྱུ་དང་དཔེ་མང་པོ༌[^1154]བསྟན་པས་ཐམས་ཅད་མགུ་བར་གྱུར་ཏོ། །

[Block 1193 [HEADING]]
###### **མདོ་སྡེ་བཅུ་གཉིས།** ^4-2-11-1-1-2-1-1-3-0

[Block 1194]
མདོ་ལས་དེ་བཞིན་མདོ་སྡེ་ཞེས་པ་ནས་གཏན་ལ་ཕབ་ཀྱང་དེ་བཞིན་བཤད་ཅས་པའི་བར་དུ་ནི་སྐབས་འདིར༌[^1155]མདོ་སྡེ་བཅུ་གཉིས་བསྟན་ཏེ། དེ་ལ་ཡང་རྣམ་པ་གསུམ་མོ། །

[Block 1195]
མཚན་ཉིད་བསྟན་པ་དང་། མིང་བསྟན་པ་དང་། ཁྱད་པར་བསྟན་པའོ། །

[Block 1196 [HEADING]]
###### **མཚན་ཉིད་བསྟན་པ།** ^4-2-11-1-1-2-1-1-3-1-0

[Block 1197]
མདོ་སྡེའི་མཚན་ཉིད་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། སྤྱིའི་མཚན་ཉིད་དང་རང་གི་མཚན་ཉིད་དོ། །

[Block 1198 [HEADING]]
###### **སྤྱིའི་མཚན་ཉིད།** ^4-2-11-1-1-2-1-1-3-1-1-0

[Block 1199]
དེ་ལ་སྤྱིའི་མཚན་ཉིད་ནི་འདི་སྐད་བདག་གིས་ཐོས་པ་ནས་མངོན་པར་དགའོ་ཞེས་པའི་བར་དུ་ནི་ཚིག་གི༌[^1156]དོན་གང་བརྗོད་པ་དེ་དག་ཐམས་ཅད་ནི་སྤྱིའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1200 [HEADING]]
###### **རང་གི་མཚན་ཉིད།** ^4-2-11-1-1-2-1-1-3-1-2-0

[Block 1201]
འགྲེལ་པ་དག་ལས་མདོ་སྡེའི་ཚིགས་སུ་བཅད་དེ་གསུངས་པ་མ་གཏོགས་པར༌[^1157]ཚིག་རྐྱང་པ་ལས་ཚིག་གི་དོན་མཚོན་ཏེ༌[^1158]བརྗོད་པ་ནི་རང་གི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1202]
དབྱངས་ཀྱིས་བསྙད་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཕྱིས་འོངས་པ་ལ་ཕན་གདགས་པ་དང་རྐྱང་པ་ལས་དོན་མ་ངེས་པ་ངེས་པར་བསྟན་པའོ། །

[Block 1203]
འགྲེལ་པ་དག་ལས་མདོ་སྡེ་ལ་ལ༌[^1159]སྔ་ཕྱི་མི་མཐུན་ཏེ་རྐྱང་པ་ལས་སྨོས་པའི་འོག་ཏུ་ཚིགས་སུ་བཅད་དེ༌[^1160]བཟླས་པ་ནི་ཕྱིས་འོངས་པ༌[^1161]ལ་ཕན་པའོ། །

[Block 1204]
རྐྱང་པ་ལས་དོན་མ་ངེས་པ་དག་ཚིགས་སུ་བཅད་དེ་བཟླས་པས་དོན་གསལ་བར༌[^1162]བྱ་བའི་ཕྱིར་དོན་མ་ངེས་པ་ངེས་པར་བསྟན་པ་ཞེས་བྱའོ། །

[Block 1205]
ལུང་བསྟན་པ་ལ་རྣམ་པ་གསུམ་སྟེ། ཉེ་གནས་ཀྱི་སྐྱེ་ཤིའི་རྒྱུ་དང་འབྲས་བུ་ལུང་བསྟན་པ་དང་། ངེས་པའི་དོན་ལ་གསལ་བར༌[^1163]ལུང་བསྟན་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་ལ་སངས་རྒྱས་སུ་ལུང་བསྟན་པ༌[^1164]དང་གསུམ་མོ། །

[Block 1206]
འཕགས་པའི་ཉེ་གནས་དག་ལ་ཁྱོད་འདས་པའི་དུས༌[^1165]ལེགས་པ་དང་ཉེས་པ་འདི་ལྟ་བུ་ཞིག་བྱས་ཏེ༌[^1166]སྐྱེ་བའི་གནས་ཀྱི་ཁྱད་པར་ལུང་བསྟན་པ་ནི་སྐྱེ་ཤིང༌[^1167]རྒྱུ་དང་འབྲས་བུ་ལུང་བསྟན་པའོ། །

[Block 1207]
མདོ་སྡེ་མ་ངེས་པ་ངེས་པའི་དོན་དུ་ལུང་བསྟན་པ་ནི། ངེས་པའི་དོན་ཟབ་མོར་ལུང་བསྟན་པའོ། །

[Block 1208]
མ་ཕམ་པ་ཁྱོད་མ་འོངས་པའི་དུས༌[^1168]རྒྱལ་པོ་དུང་ཞེས་བྱ་བ་དེའི་ཚེ་བྱམས་པ་ཞེས་བྱ་བའི་སངས་རྒྱས་སུ་འགྱུར་རོ༌[^1169]ཞེས་ལུང་བསྟན་པ་ནི་སངས་རྒྱས་སུ་ལུང་བསྟན་པའོ། །

[Block 1209]
ཚིགས་སུ་བཅད་པ་ནི་མདོ་སྡེ་དག་ལ་ཚིག་རྐྱང་པ་ལས་མི་སྨོས་པར་ཚིགས་སུ་བཅད་པ་གཉིས་སམ་གསུམ་མམ་བཞིའམ་ལྔའམ་དྲུག་ལ་སོགས་པ་དོན་གང་བརྗོད་པ་ཚིགས་སུ་བཅད་དེ་གསུངས་པ་ནི་ཚིགས་སུ་བཅད་པའི་སྡེ་ཞེས་བྱའོ། །

[Block 1210]
ཆེད་དུ་བརྗོད་པ་ནི་མདོ་སྡེ་ལས་གསོལ་བ་མ་བཏབ་པར་ཡང་དག་པའི་ཆོས་དང་བསྟན་པ་དང་ཡུན་དུ་གནས་པར་བྱ་བའི་ཕྱིར་གསོལ་བ་གདབ་མི་དགོས་པར་གསུངས་པ་ནི་ཆེད་དུ་བརྗོད་པའི་སྡེ་ཞེས་བྱའོ། །

[Block 1211]
གླེང་གཞི་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ་གསོལ་བ་བཏབ་ནས་བསྟན་པ་དང་ཉམས་པ་ལས༌[^1170]ཚུལ་ཁྲིམས་བཅས་པ་བསྟན་པ་དང་། གླེང་བ་ཡོད་པས་ཆོས་བསྟན་པ་དང་གསུམ་མོ། །

[Block 1212]
འགྲེལ་པ་དག་ལས་གླེངས་ནས་བསྟན་པ་ནི་གསོལ་བ་བཏབ་ནས་བཤད་པའོ། །

[Block 1213]
བསླབ་ཚིག་བཅས་པ་ནི་བཅས་པའོ། །

[Block 1214]
མདོ་སྡེ་དག་ལས་ཕ་རོལ་པོས་གླེངས་ཏེ་དཔེར་ན་མཉན་དུ་ཡོད་པ་ན་མི་ཞིག་གིས་བྱ་ཞིག་བཟུང་ནས་ཕྱིར་ཡང་བཏང་བ་ལས་གླེངས་ཏེ་བཅོམ་ལྡན་འདས་ཀྱིས༌[^1171]སྔོན་གྱི་རྒྱུ་ཡང་གླེངས་ནས་བསྟན་པ་ནི་གླེངས་ནས་བསྟན་པ་ཞེས་བྱའོ། །

[Block 1215]
དཔེ་ནི་མདོ་སྡེ་དག་ལས་དཔེ་རྣམ་པ་མང་པོས་ཆོས་བསྟན༌[^1172]པའོ། །

[Block 1216]
ད་ལྟར༌[^1173]འདས་པའི་སྡེ་ནི་སྐྱེས་པའི་རབས་མ་གཏོགས་པར༌[^1174]སྔོན་འདས་པའི་གང་ཟག་དང་ཆོས་ཀྱི་རྒྱུས་བསྟན་པའོ། །

[Block 1217]
སྐྱེས་པའི་རབས་ཀྱི་སྡེ་ནི་བཅོམ་ལྡན་འདས་སྔོན་འདས་པའི་དུས་ན་ཆེ་གེ་མོ་ཞིག་ན་སྐྱེ་བ་དང་འཆི་འཕོ་བ་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་དཀའ་བ་སྤྱོད་པ་དང་། མདོ་སྡེ་དག་ལ་འདས་པའི་དུས་ན་ཤ་བ་དང་དྲེད་མོ་དང་། རི་བོང་དང་བྱ་ནམ་མཁའ་ལྡིང་ལ་སོགས་པའི་ལུས་བྱས་པ་བསྟན་པ་ནི་སྐྱེས་པའི་རབས་ཞེས་བྱའོ། །

[Block 1218]
ཤིན་ཏུ་རྒྱས་པ་ལ་རྣམ་པ་གཉིས་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་ལམ་ལ་སྟོན་པ་དང་། རྒྱ་ཆེ་ལ་དུས༌[^1175]ཡུན་རིང་བའོ། །

[Block 1219]
ཉན་ཐོས་ལའང་ཤིན་ཏུ་རྒྱས་པ་ཡོད་དེ། འདིར་ནི་གཉི་ག་ལ་ཤིན་ཏུ་རྒྱས་པ་ཞེས་བྱའོ། །

[Block 1220]
རྨད་དུ་བྱུང་བ་ནི་མདོ་སྡེ་དག་ལས་སངས་རྒྱས་དང་ཉེ་གནས་འཕགས་པ་འཁོར་བརྒྱད་ཀྱི་ཡོན་ཏན་ཐུན་མོང་དང་ཐུན་མོང་མ་ཡིན་པ་ཡ་མཚན་ངོ་མཚར་དུ་གྱུར་པ་བསྟན་པ་ནི་རྨད་དུ་བྱུང་བ་ཞེས་བྱའོ། །

[Block 1221]
གཞན་ཡང་མདོ་སྡེ་ལས་སངས་རྒྱས་བཙས་མ་ཐག་ཏུ་གོམ་པ་བདུན་བདུན་གཤེགས་པ་དང་། འོད་ཟེར་ཆེན་པོས་ཕྱོགས་བཅུ་སྣང་བར་བྱས་པ་དང་། སྤྲེའུས་སྦྲང་རྩི་ཕུལ་བ་དང་། ཁྱི་དཀར་པོས་ཆོས་ཉན་པ་ལ་སོགས་ཏེ། ངོ་མཚར་རྨད་དུ་བྱུང་བའི་ཆོས་རྣམས་ནི་རྨད་དུ་བྱུང་བ་ཞེས་བྱའོ། །

[Block 1222]
གཏན་ལ་ཕབ་པར༌[^1176]བསྟན་པ་ཞེས་བྱ་བ་ལ་རྣམ་པ་གཉིས་ཏེ། སངས་རྒྱས་ཉིད་ཀྱིས༌[^1177]བསྟན་པ་དང་། འཕགས་པ་ཉེ་གནས་ཀྱིས༌[^1178]བསྟན་པའོ། །

[Block 1223]
འགྲེལ་པ་དག་ལས་མདོ་སྡེ་གང་ལྟག་འོག་གཏན་ལ་ཕབ་པ་ནི་གཏན༌[^1179]ལ་ཕབ་པར༌[^1180]བསྟན་པ་ཞེས་བྱའོ། །

[Block 1224]
གང་མདོ་སྡེ་ངེས་པར་བསྟན་པ་ལ་ཡང་གཏན་ལ་ཕབ་པ༌[^1181]ཞེས་བྱའོ། །

[Block 1225 [HEADING]]
###### **མིང་བསྟན་པ།** ^4-2-11-1-1-2-1-1-3-2-0

[Block 1226]
དེ་ལ་མིང་བསྟན་པ་ནི༌[^1182]མདོ་སྡེ་བཅུ་གཉིས་ཀྱི་མིང་བསྟན་པའོ། །

[Block 1227 [HEADING]]
###### **ཁྱད་པར་བསྟན་པ།** ^4-2-11-1-1-2-1-1-3-3-0

[Block 1228]
དེ་ལ་ཁྱད་པར་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ་རང་བཞིན་གྱི་ཁྱད་པར་དང་། བསྟན་པའི་ཁྱད་པར་རོ། །

[Block 1229 [HEADING]]
###### **རང་བཞིན་གྱི་ཁྱད་པར།** ^4-2-11-1-1-2-1-1-3-3-1-0

[Block 1230]
རང་བཞིན་གྱི་ཁྱད་པར་ནི་དབྱངས་ཀྱིས་བསྙད་པའི་ནང་ན་ཚིགས་སུ་བཅད་པ་མེད་ལ། ཚིགས་སུ་བཅད་པའི་ནང་ན་དབྱངས་ཀྱིས་བསྙད་པ་མེད་དེ་སྔ་ཕྱི་དང་། རྐྱང་པ་དང་བཟླས་པ་ཐ་དད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
