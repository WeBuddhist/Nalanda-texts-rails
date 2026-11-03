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

[Block 1161]
ཚིག་གསུམ་གྱིས་ནི་མི་དགེ་བའི་རྩ་བ་ཆེ་བ་བསྟན་ཏོ། །

[Block 1162 [HEADING]]
###### **ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པ།** ^4-2-11-1-1-1-1-0

[Block 1163]
ཚིགས་བཅད་འདིས་ནི་ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པ་བསྟན་ཏེ། རབ་ཏུ་བྱུང་བ་ནི་ཚུལ་ལ་གནས་པ་ཡིན་ན་མ་ཐོབ་པ༌[^1141]ཐོབ་ཅེས་སྨྲ་བས་ང་རྒྱལ་ཅན་ནོ། །

[Block 1164]
ཁྱིམ་ན་གནས་པ་དགེ་བསྙེན་པ་ཡང་ང་ཞེས་པ་ལ་ཞེན་པས་ང་རྒྱལ་གྱི་སེམས་སྐྱེས་ཏེ། ང་རྒྱལ་ཅན་དགེ་བསྙེན་མ་ནི་ང་ཞེས་པའི་ལྟོ་མེད་ཀྱང་ཁྱིམ་ཐབ༌[^1142]ཀྱི་རྗེས་སུ་ང་ཞེས་པ་བསྐྱེད༌[^1143]པས་ང་རྒྱལ་ཅན་ཞེས་སྨོས་སོ། །

[Block 1165]
མདོ་ལས།

[Block 1166 [HEADING]]
###### **མི་དགེ་བའི་རྩ་བ་ཆེ་བ།** ^4-2-11-1-1-1-2-0

[Block 1167]
ལྔ་སྟོང་ལས་ནི་མི་ཉུང་བ། །ཞེས་པ་ནས། །དེ་དག་སྙིང་པོ་རབ་ཏུ་གནས། །ཞེས་པའི་བར་དུ་ནི་ཚིག་གསུམ་ནི་མི་དགེ་བའི་རྩ་བ་ཆེ་བ་བསྟན་པ་སྟེ། སྐྱོན་སྦེད་པ་ནི་ཚུལ་ཁྲིམས་ཉམས་ནས་ཉེས་པ་འཆབ་པའོ། །

[Block 1168]
ཉམས་པ་ནི་ཚུལ་ཁྲིམས་ལས་ཤས་ཀྱིས་ཉམས་པའོ། །

[Block 1169]
མ་ཐོབ་པར་ཐོབ་ཅེས་སྨྲ་བ༌[^1144]ནི་ཚུལ་ཁྲིམས་ཀྱི་རྩ་བ་མེད་པ་སྟེ་དེ་ལ་ཚུལ་ཁྲིམས་ཀྱང་མེད་པ་རྣམ་པར་དག་པ་ཡང་མ་ཡིན། ཏིང་ངེ་འཛིན་ཀྱང་མངོན་དུ་མི་འགྱུར་རོ། །

[Block 1170]
སྙིགས་མ་ཞེས་བྱ་བ་ནི་ཅིར་ཡང་དགོས་པ་མེད་པ་སྟེ། བྱིས་པའི་བློ་ཅན་དག་སངས་རྒྱས་ཀྱི་མཐུས་དོང་བ་ཡང་ཅི་སྟེ་དམ་པའི་ཆོས་ཐོས་ན་དེ་ལ་སྐུར་པ་འདེབས་པས་སྡིག་པ་སྐྱེ་བར་འགྱུར་ཏེ། ཕན་པ་མེད་པའི་ཕྱིར་ཕྱིར༌[^1145]དོང་ངོ་། །

[Block 1171]
མདོ་ལས།

[Block 1172 [HEADING]]
###### **ལུང་བསྟན་པ།** ^4-2-11-1-1-2-0

[Block 1173]
འདི་འདྲ་ང་ལ་ཉོན་ཅིག་ཤཱ་རིའི་བུ། །ཞེས་པ་ནས་ཐབས་ལ་མཁས་པ་བརྒྱ་ཕྲག་དུ་མ་ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ནི་ཚིག་བརྒྱ་རྩ་བཅུ་གཅིག་གིས་ལུང་བསྟན་པ་བརྗོད་དེ། སྔར་མདོ་ལས་རྣམ་པ་དྲུག་ཏུ་ཕྱེ་བ་ལྟར་འདིར་ཡང་རྣམ་པ་དྲུག་ཏུ་དབྱེ་སྟེ་ཚིག་དྲུག་གིས་ནི་ཅིའི་ཕྱིར་བཤད་པ་བསྟན་ཏོ། །

[Block 1174]
ཚིག་ཕྱེད་དང་བརྒྱད་ཀྱིས་ནི་གནས་པ་བསྟན་ཏོ། །

[Block 1175]
ཚིག་ཕྱེད༌[^1146]དང་གཉིས་ཀྱིས༌[^1147]ནི་བཅས་པ་བསྟན་ཏོ། །

[Block 1176]
ཚིག་ཕྱེད་དང་དགུས་ནི་དོན་གང་ལ་བརྟེན་པ་བསྟན་ཏོ། །

[Block 1177]
ཚིག་བདུན་ཅུ་རྩ་གཅིག་གིས་ཆོས་བསྡུ་བ་བསྟན་ཏོ། །

[Block 1178]
ཚིག་བདུན་གྱིས་ནི་མ་ཐོས་པ་ཐོས་པར་བྱ་བ་བསྟན་ཏེ། མདོ་ལས༌[^1148]འགྲེལ་པ་ལས་བཤད་པ་དང་ལྟག་འོག་ནི་མི་མཐུན་ནོ། །

[Block 1179 [HEADING]]
###### **ཅིའི་ཕྱིར་བཤད་པ།** ^4-2-11-1-1-2-1-0

[Block 1180]
ཚིག་དྲུག་གིས་ཅིའི་ཕྱིར་བཤད་པ་ལས་ཡང་རྣམ་པ་གཉིས་སུ་དབྱེ༌[^1149]སྟེ། ཚིག་ཕྱེད་དང་ལྔས་ནི་ཅིའི་ཕྱིར་བྱ་བ་བསྟན་ཏོ།[^1150] །ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་དབང་པོ་ཇི་བཞིན་དུ་བཤད་པ་བསྟན་ཏོ། །

[Block 1181 [HEADING]]
###### **ཅིའི་ཕྱིར་བྱ་བ།** ^4-2-11-1-1-2-1-1-0

[Block 1182]
དེ་ལ་ཚིགས་བཅད་གཅིག་གིས་རྒྱུ་སྣ་ཚོགས་བསྟན་ཏོ། །

[Block 1183]
ཚིག་གཉིས་ཀྱིས་ནི་གདོན་མི་ཟ་བའི་ཚིག༌[^1151]དང་རྒྱུ་དང་དཔེ་སྣ་ཚོགས་བསྟན་ཏོ། །

[Block 1184 [HEADING]]
###### **རྒྱུ་སྣ་ཚོགས།** ^4-2-11-1-1-2-1-1-1-0

[Block 1185]
ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་ཆོས་སྣ་ཚོགས་བསྟན་པ་སྟེ། ཚིགས་བཅད་འདིས༌[^1152]ནི་དབང་པོ་ཇི་བཞིན་དུ་རྒྱུ་སྣ་ཚོགས་བསྟན་པའོ། །

[Block 1186]
མདོ་ལས།

[Block 1187 [HEADING]]
###### **གདོན་མི་ཟ་བའི་ཚིག་དང་རྒྱུ་དང་དཔེ་སྣ་ཚོགས།** ^4-2-11-1-1-2-1-1-2-0

[Block 1188]
དེ་ཡི་བསམ་པ་སྤྱོད་པ་ཇི་འདྲ་མཁྱེན། །ཞེས་པ་ནས། །ཅི་ནས་སེམས་ཅན་ཐམས་ཅད་མགུ་བར་བྱས། །ཞེས་པའི་བར་དུ་ནི་གདོན་མི་ཟ་བའི་ཚིག་དང་རྒྱུ་དང་དཔེ་རྣམ་པ་སྣ་ཚོགས་བསྟན་པའོ། །

[Block 1189]
ཁོང་དུ་ཆུད་པ་ནི་བྱང་ཆུབ་རྟོགས་པའོ། །

[Block 1190]
དད་པ་སྣ་ཚོགས་ནི་མོས་པའི་མཆོག་ཅེས་བྱ་བའི་དོན་ཏོ། །

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
--- END BLOCKS ---
