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
[Block 1261]
སེམས་གོང༌[^1066]དུ་ཡང་ཐོགས་པ་མེད་ཅེས་བྱ་བ་ནི་དེའི་སེམས་ཀྱི་དངོས་པོ་ཐམས་ཅད་མ་ལུས་པར་ཤེས་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1262]
བརྩོན་འགྲུས་སྒྲུབ་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་བརྩོན་འགྲུས་ལ་འཇོག་པར་བྱེད་པའོ། །

[Block 1263]
བསམ་གཏན་གྱི་ཡན་ལག་སྟོན་པ་ཞེས་བྱ་བ་ནི་བསམ་གཏན་དང་པོ་དང་གཉིས་པ་ལ་སོགས་པ་སྒོམ་པའི༌[^1067]ཐབས་སྟོན་པའོ། །ཤེས་རབ་ཀྱི་མིག༌[^1068]སྦྱིན་པ་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པའི༌[^1069]ཤེས་རབ་ཀྱི་མིག་སྦྱིན་པའོ། །

[Block 1264]
ལམ་ངན་པ་ལ་ཞུགས་པ་ནི་མུ་སྟེགས་ཅན་རྣམས་སོ། །

[Block 1265]
ལམ་སྟོན་པ་ནི་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་སྟོན་པའོ། །

[Block 1266]
དམན་པ་ལ་མོས་པ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་ལ་ཞུགས་པ་རྣམས་སོ། །

[Block 1267]
སངས་རྒྱས་ཀྱི་ཆོས་རྒྱ་ཆེན་པོ་རྟོག་པར༌[^1070]བྱེད་ཅེས་བྱ་བ་ནི་དེ་དག་ལས་བཅུ་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ༌[^1071]ལ་སོགས་པ་རྟོག་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1268]
ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ལ་འཛུད་ཅེས་བྱ་བ་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་རྣམ་པར་མི་རྟོག་པའི་མཚན་ཉིད་ཐོབ་པ་ལ་འཇོག་པར་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1269]
བྱང་ཆུབ་ཡོངས་སུ་རྫོགས་པར་བྱ་བའི་ཕྱིར༌[^1072]ཞེས་བྱ་བ་ནི་བདག་ཉིད་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པར་བྱ་བའི་ཕྱིར་དེའི་རྒྱུར་གྱུར་པའི་ལྷའི་མིག་མ་ཉམས་པ་ཟིན་ཏེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1270]
ལྷའི་མིག་མངོན་པར་ཤེས་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1271 [HEADING]]
### ཚིག་མངོན་སུམ་པ། ^3-2-0

[Block 1272]
ཚིག་མངོན་སུམ་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ༌[^1073]རྣམས་ཀྱི་ལྷའི་རྣ་བ་མངོན་པར་ཤེས་པ་མི་ཟད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་མི་ཟད་པ་ཡང་རྣ་བ་དེས་དམིགས་པར་བྱ་བའི་སྒྲ་ཟད་མི་ཤེས་པས་དེ་ལ་དམིགས་པར་བྱེད་པའི་ལྷའི་རྣ་བ་ཡང་ཟད་མི་ཤེས་པའི་ཕྱིར་མི་ཟད་པའོ། །

[Block 1273]
ཡང་ན་འོག་ནས་དེའི་རྣ་བའི་ཁམས་དེ་ཆོས་ཀྱི༌[^1074]དབྱིངས་ཤིན་ཏུ་རྣམ་པར་དག་པ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའི་ཚུལ་གྱི་ལྷའི་རྣ་བ་དེའི་རང་བཞིན༌[^1075]ཆོས་ཀྱི་དབྱིངས་ཀྱི་རང་བཞིན་ཡིན་པས་ཆོས་ཀྱི་དབྱིངས་དེ་ལ་ཟད་པ་མེད་པའི་ཕྱིར་ལྷའི་རྣ་བ་ཡང་མི་ཟད་པའོ། །

[Block 1274]
དེ་ཡང་རྣམ་པ་དགུར་རིག་པར་བྱ་སྟེ། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་ཐམས་ཅད་ལས་ཁྱད་པར་དུ་གྱུར་པ་དང་། སྒྲ་ཐམས་ཅད་ལ་དམིགས་པ་དང་། རྒྱུ་གང་ལས་བྱུང་བ་ཤེས་པ་དང་། འབྲས་བུ་གང་ལས་འབྱུང་བ༌[^1076]ཤེས་པ་དང་། རྒྱུ་དང་འབྲས་བུ་མི་མཐུན་པ་ཤེས་པ་དང་། གཉིས་ཀའི་ཆ་ལ་ཉོན་མོངས་པ་མེད་པ་དང་། དུས་གསུམ་མ་འདྲེས་པ༌[^1077]ཤེས་པ་དང་། ལས་དང་རྒྱུའོ། །

[Block 1275 [HEADING]]
#### འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་ཐམས་ཅད་ལས་ཁྱད་པར་དུ་གྱུར་པ། ^3-2-1-0

[Block 1276]
ལྷ་ཐམས་ཅད་ཀྱི་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཆེས་འོད་གསལ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་ལས་ཁྱད་ཞུགས་པ༌[^1078]བསྟན་ཏོ། །

[Block 1277 [HEADING]]
#### སྒྲ་ཐམས་ཅད་ལ་དམིགས་པ། ^3-2-2-0

[Block 1278]
ལྷའི་རྣ་བ་དེས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། སྒྲ་དེ་དག་ཐམས་ཅད་ཀྱང་ཐོས་སོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་སྒྲ་ཐམས་ཅད་ལ༌[^1079]དམིགས་པ་བསྟན་ཏོ། །

[Block 1279]
སེམས་ཀྱི་དམིགས་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ལས་འབྱུང་བ་ཐམས་ཅད་ཀྱང་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^1080]རྒྱུ་གང་ལས་འབྱུང་བ༌[^1081]ཤེས་པ་བསྟན་ཏོ། །

[Block 1280]
ངག༌[^1082]གི་ལས་དགེ་བའི་རྒྱུ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ལུང་དུ་མི་སྟོན་པའི་རྒྱུ་ཡོངས་སུ་འཛིན་པ་དེ་དག་ཐམས་ཅད་ཀྱང་ཡང་དག་པ༌[^1083]ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་འབྲས་བུ་གང་འབྱུང་བ་ཤེས་པ་བསྟན་ཏོ། །

[Block 1281]
འདོད་ཆགས་བག་ལ་ཉལ་ཞེས་བྱ་བ་ནས༌[^1084]བརྩམས་ཏེ། ལྷའི་རྣ་བའི་མངོན་པར་ཤེས་པའི་ཡེ་ཤེས་ཐོགས་པ་མེད་པ༌[^1085]དེས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་ཞེས༌[^1086]བྱ་བ་ཡན་ཆད་ཀྱིས་རྒྱུ་དང་འབྲས་བུའི་མི་མཐུན་པ་ཤེས་པ་བསྟན་ཏོ།[^1087] །དེ་དག་གི༌[^1088]ལྷའི་རྣ་བའི་མངོན་པར་ཤེས་པའི་ཡེ་ཤེས་དེས་འཕགས་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། འཕགས་པ་མ་ཡིན་པའི་སྒྲ་ལ་སྙིང་རྗེ་ཆེན་པོ་འཐོབ་བོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་གཉི་གའི་ཆ་ལ་ཉོན་མོངས་པ་མེད་པ་བསྟན་ཏོ། །

[Block 1282]
སྒྲ་ཐམས་ཅད་ལ་ཡང་སྔོན་གྱི་མཐའ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་དུས་སུ་མ་འདྲེས་པ་ཤེས་པ་བསྟན་ཏོ། །

[Block 1283]
དེ་དག་ལྷའི་རྣ་བའི་མངོན་པར་ཤེས་པའི་ཡེ་ཤེས་དེས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། སེམས་ཅན་གང་དག་ཆོས་ཤེས་པར་བྱེད་པ་མ་ཡིན་པ་དེ་དག་ནི་མི་ཐོས་སོ་ཞེས་བྱ་བ༌[^1089]ཡན་ཆད་ཀྱིས་ལས་བསྟན་ཏོ། །

[Block 1284]
དེ་དག་གི་རྣ་བའི་ཁམས་དེ་ཆོས་ཀྱི་དབྱིངས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ལྷའི་སྙན་དུ་བསྔོས་པ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^1090]རྒྱུ་བསྟན་ཏོ། །

[Block 1285]
གོང་དུ་ལྷའི་མིག་གི་སྐབས་སུ་བཤད་པ་དང་དོན་མཐུན་པའི་ཚིག་རྣམས་འདིར་མ་བཤད་དོ། །

[Block 1286 [HEADING]]
#### རྒྱུ་གང་ལས་བྱུང་བ་ཤེས་པ། ^3-2-3-0

[Block 1287]
སེམས་ཀྱི༌[^1091]དམིགས་པ་དགེ་བ་དང་མི་དགེ་བ་དང་། ལུང་དུ་མི་སྟོན་པ་གང་དག་གིས་སེམས་ཅན་དེ་དག་གི་ངག་གི༌[^1092]ལས་འབྱུང་བ༌[^1093]ཐམས་ཅད་ཀྱང་ཡང་དག་པ༌[^1094]ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་དེ་དག་གི་ཚིག་རབ་ཏུ་སྨྲ་བ་དེའི་རྒྱུ་ནི་སེམས་ཀྱི་དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མི་སྟོན་པའི་ཆོས་ལ་དམིགས་པ་ཡིན་ཏེ། དེ་དག་གི་སེམས་ཀྱི་ཆོས་གང་ལ་དམིགས་ནས་ངག༌[^1095]གི་ལས་ཚིག་ཏུ་སྨྲ་བ་ནི་སྒྲ་གང་བྱུང་བའི་རྒྱུ་རྣམས་ཀྱང་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1288]
རྒྱུ་གང་ལས་བྱུང་བ་ཤེས་པ་བཤད་ཟིན་ཏོ། །

[Block 1289 [HEADING]]
#### འབྲས་བུ་གང་ལས་འབྱུང་བ་ཤེས་པ། ^3-2-4-0

[Block 1290]
ངག་གི་ལས་གང་དགེ་བའི་རྒྱུ་ཡོངས་སུ་འཛིན་པ་ལ་སོགས་པ་ནི་སེམས་ཅན་དེ་དག་གིས་ཚིག་ཏུ་སྨྲ་བ་དེ་དག་ཐོས་ནས་ཚིག་དེ་དག་སྨྲས་པའི་རྒྱུས་འབྲས་བུ་ཅི་དང་ཅིར་འགྱུར་བ་ཕྱིན་ཅི་མ་ལོག་པར་ཤེས་པའི་དོན་ཏོ། །

[Block 1291]
འབྲས་བུ་གང་བྱུང་བ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 1292 [HEADING]]
#### རྒྱུ་དང་འབྲས་བུ་མི་མཐུན་པ་ཤེས་པ། ^3-2-5-0

[Block 1293]
འདོད་ཆགས་བག་ལ་ཉལ་བའི་ངག་གི་ལས་གང་སྡང་བ་དང༌[^1096]འབྱིན་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་གསུམ་ལས་གཅིག་ནི་ཚིག་མངོན་པར་སྨྲ་བའི་རྒྱུའི་གཙོ་བོ་ཡིན་པར་སྟོན། གཅིག་ནི་གྲོགས་ཡིན་པར་སྟོན་ཏེ། དེ་ལ་འདོད༌[^1097]ཆགས་བག་ལ་ཉལ་ལ་སྡང་བས་འབྱིན་པ་ནི་ཚིག་འབྱུང་བའི་གཞི་འདོད་ཆགས་ལས་བླངས་ལ། འདོད་ཆགས་དངོས་སུ་མ་བྱུང་བར་བག་ལ་ཉལ་ཏེ་ཞེ་སྡང་དངོས་སུ་བྱུང་བས་ཚིག་ཏུ་སྨྲས་པས་ཤེས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1294]
དེ་བཞིན་དུ༌[^1098]ལྷག་མ་རྣམས་ལ་ཡང་སྦྱར་རོ། །

[Block 1295]
ངག་གི་ལས་གང་བསམ་པ་དག་ལ་སྦྱོར་བ་ཉམས་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། བསམ་པ་མ་ནོར་ལ་ཚིག་ཏུ་སྨྲ་བའི་སྦྱོར་བ་འཁྲུལ་ཞིང་ནོར་བ་དང་། ཚིག་ཏུ་སྨྲ་བའི་སྦྱོར་བ་མ་ནོར་མ་འཁྲུལ་ལ། བསམ་པ་འཁྲུལ་པ་ལ་སོགས་པ་ཕྱིན་ཅི་མ་ལོག་པར་ཤེས་པ་ལ་བྱའོ། །

[Block 1296]
རྒྱུ་དང་འབྲས་བུ་མི་མཐུན་པར་ཤེས་པ་བཤད་ཟིན་ཏོ། །

[Block 1297 [HEADING]]
#### གཉིས་ཀའི་ཆ་ལ་ཉོན་མོངས་པ་མེད་པ། ^3-2-6-0

[Block 1298]
འཕགས་པའི་སྒྲ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་། དེ་བཞིན་གཤེགས་པ་རྣམས་གསུངས་པ་དང་། ཆོས་འཆད་པའི་སྒྲའོ། །

[Block 1299]
འཕགས་པ་མ་ཡིན་པའི་སྒྲ་ནི་སོ་སོའི་སྐྱེ་བོ་རྣམས་འོང་བ༌[^1099]དང་འགྲོ་བ་ལ་སོགས་པ་ཐ་སྙད་སྣ་ཚོགས་ཀྱི་སྒྲ་འབྱིན་པའོ།[^1100] །འཕགས་པའི་སྒྲ་ལ་བྱམས་པ་ཆེན་པོ་འཐོབ་ཅིང་ཞེས་བྱ་བ་ནི་འཕགས་པ་རྣམས་ཀྱི་སྒྲ་ཐོས་ནས་ཆོས་བཤད་པའི་སྒྲ་འདིས་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་བཏགས་སོ་ཞེས་སྒྲ་དེ་ལ་བདག་ཉིད་བྱམས་པ་ཆེན་པོའི་སེམས་བསྐྱེད༌[^1101]པའོ། །

[Block 1300]
འཕགས་པ་མ་ཡིན་པའི་སྒྲ་ལ་སྙིང་རྗེ་ཆེན་པོ་འཐོབ་ཅེས་བྱ་བ་ནི་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱི་སྨྲ་བའི༌[^1102]སྒྲ་ནི་འདོད་ཆགས་དང་ཞེ་སྡང་ལ་སོགས་པའི་རྒྱུ་ལས་བྱུང་བས་ན་སྡུག་བསྔལ་སྣ་ཚོགས་བསྐྱེད༌[^1103]པའི་རྒྱུ༌[^1104]ཡིན་ནོ་ཞེས་སྙིང་རྗེ་ཆེན་པོའི་སེམས་སྐྱེའོ། །
--- END BLOCKS ---
