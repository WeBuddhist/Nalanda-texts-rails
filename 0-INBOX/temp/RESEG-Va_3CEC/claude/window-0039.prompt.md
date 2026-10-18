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
[Block 1366]
འོད་གསལ་བ་ནི་རང་བཞིན་གྱིས་དག་པའི༌[^1172]རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1367]
ཁ་ན་མ་ཐོ་བ་མེད་པ་ནི་སྡིག་པའི་ཆོས་དང་མ་འདྲེས་པས་སོ། །

[Block 1368]
མི་བརླང་པ་ནི་ཞེ་སྡང་སྤངས་པའོ།[^1173] །ཉོན་མོངས་པ་མེད་པ་ནི་ཉོན་མོངས་པར་འགྱུར་བའི་ཆོས་གང་གིས་ཀྱང་ཉོན་མོངས༌[^1174]པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1369]
རྙོག་པ་མེད་པ་ནི༌[^1175]སྒྲིབ་པར་འགྱུར་བའི་ཆོས་ཐམས་ཅད་སྤངས་པའི་ཕྱིར་རོ། །

[Block 1370]
ཆོས་ཐམས་ཅད་སྣང་བས༌[^1176]རིག་པ་ནི་ཤེས་པར་བྱ་བའི་དངོས་པོ་ཐམས་ཅད་མངོན་སུམ་དུ་རྟོག་པའི༌[^1177]ཕྱིར་རོ། །

[Block 1371]
སེམས་ཀྱི་སྤྱོད་པ་ལ་ཞུགས་ཞེས་བྱ་བ་ནི་སེམས་ཅན་འདོད་ཆགས་སྤྱོད་པ་ལ་སོགས་པའི་སྤྱོད་པ་མང་པོ་ཁོང་དུ་ཆུད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1372]
སེམས་ཀྱི་རྒྱུན་གཅིག་ཏུ་རིག་ཅེས་བྱ་བ་ནི་དུས་གསུམ་གྱི་སེམས་ཅན་རྣམས་ཀྱི་རྒྱུན་ཇི་ལྟ་བུ་ཡིན་ཇི་འདྲ༌[^1178]བ་རྟོགས་ཞེས༌[^1179]བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1373]
ཕ་རོལ་གྱི་སེམས་ཤེས་པའི་མངོན་པར་ཤེས་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1374 [HEADING]]
### བསམ་པ་མངོན་སུམ་པ། ^3-4-0

[Block 1375]
བསམ་པ་མངོན་སུམ་པ་བསྟན་པའི་ཕྱིར།[^1180] དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པའི་ཤེས་པ་མངོན་སུམ་དུ་བྱེད་པའི་མངོན་པར་ཤེས་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1376]
དེ་མི་ཟད་པ་ཡང་སྔོན་གྱི་དུས་འདི་ཚུན་ཆད་དྲན་ནོ་ཞེས་དྲན་པའི་མཐའ་ཐུག་པ་མེད་པ༌[^1181]ནི་མི་ཟད་པའམ། ཡང་ན་བདག་གི༌[^1182]སྔོན་གནས་དྲན་པ་འབའ་ཞིག་མ་ཡིན་གྱི། སེམས་ཅན་ཐམས་ཅད་ཀྱི༌[^1183]སྔོན་གྱི་གནས་ཀྱང་དྲན་པས་སེམས་ཅན་མི་ཟད་པའི་ཕྱིར་དེ་དག་གི་སྔོན་གྱི་གནས་དྲན་པ་ཡང་མི་ཟད་པའོ། །

[Block 1377]
རྣམ་པ་གཅིག་ཏུ་ན་དྲན་པ་དེ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་གནས་ཀྱིས༌[^1184]བྱིན་གྱིས་བརླབས་པའོ་ཞེས་བྱ་བས་ཀྱང་མི་ཟད་པ་བསྟན་ཏེ། ཆོས་ཀྱི་དབྱིངས་རྣམ་པར་དག་པ་ནི་མཚན་མ་དང་དངོས་པོ་ཐམས་ཅད་ལས་འདས་པས་མི་ཟད་པ་ཡིན་ཏེ། དེས་བྱིན་གྱིས་བརླབས་པ་ཡང་དེ་དང་མཐུན་པའམ། དེའི་རང་བཞིན་རྟོག་པས༌[^1185]དེ་ལྟ་བུའི་དྲན་པ་ཡང་མཐའ་མེད་པའི་ཕྱིར་མི་ཟད་པའོ། །

[Block 1378]
དེ་ཡང་རྣམ་པ༌[^1186]བཞིར་རིག་པར་བྱ་སྟེ། གང་གིས་དྲན་པ་དང་། གང་དྲན་པ་དང་། ཇི་ལྟར་དྲན་པ་དང་། དྲན་ནས་དོན་ཆེན་པོར་འགྱུར་པའོ། །

[Block 1379]
དེ་དྲན་པ་དེས་སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་ཏེ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ཀྱིས་ཚོགས་བསགས་པའོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་གང་གིས་དྲན་པ་བསྟན་ཏོ། །

[Block 1380]
དེ་དྲན་པ་དེས་སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་ཏེ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བསྐལ་པ་བརྒྱ་སྟོང་ཕྲག་དུ་མ་ཡང་དྲན་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་གང་དྲན་པ་བསྟན་ཏོ། །

[Block 1381]
སེམས་ཅན་མིང༌[^1187]ཆེ་གེ་མོ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། དེས་བདག་དང་སེམས་ཅན་གཞན་གྱི་སྔོན་གྱི་མཐའ་ནས་བཟུང་སྟེ། སྔོན་གྱི་གནས༌[^1188]རྗེས་སུ་དྲན་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱི༌[^1189]ཇི་ལྟར་དྲན་པ་བསྟན་ཏོ། །

[Block 1382]
དེ་དག༌[^1190]གི་དགེ་བའི་རྩ་བ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཐམས་ཅད་མཁྱེན་པའི་ཕྱིར་བསྔོ་སྟེ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་དོན་ཆེན་པོར་འགྱུར་བ་བསྟན་ཏོ། །

[Block 1383 [HEADING]]
#### གང་གིས་དྲན་པ། ^3-4-1-0

[Block 1384]
དེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ༌[^1191]དེ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1385]
དེས༌[^1192]ཞེས་པ་ནི༌[^1193]སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་དེས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1386]
དྲན་པ་དེ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་གནས་ཀྱིས་བྱིན་གྱིས་བརླབ་པའོ་ཞེས་བྱ་བ་ལ་གཟུང་བ༌[^1194]དང་འཛིན་པ་ཐམས་ཅད་ལས་འདས་པའི་ཆོས་ཀྱི་དབྱིངས་ཉིད་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་སྐྱེ་བའི་རྒྱུ་ཡིན་པས་ཆོས་ཀྱི་དབྱིངས་ཀྱི་གནས་ཏེ། དྲན་པ་དེའི༌[^1195]ཆོས་ཀྱི་གནས་དེའི་རྒྱུ་ལས་སྐྱེས་པ་འམ། ཆོས་ཀྱི་དབྱིངས་དང་རང་བཞིན་མཐུན་པའི་ཕྱིར་བྱིན་གྱིས་བརླབས་པ་ཞེས་བྱའོ། །

[Block 1387]
རབ་ཏུ་རིག་པས་ན། མི་གཡོ་བའོ་ཞེས་བྱ་བ་ནི་དྲན་པ་དེས་ཆོས་ཐམས་ཅད་ཕྱིན་ཅི་མ་ལོག་པ༌[^1196]ཤིན་ཏུ་རྟོག་པ༌[^1197]ན་འཁྲུལ་པ་འམ་འགྱུར་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1388]
ཡེ་ཤེས་ཤིན་ཏུ་སྦྱང་བ་བྱས་པས་ན་མི་རྒོད་པའོ་ཞེས་བྱ་བ་ནི་ཤེས་ཤིང་དྲན་པར་བྱས་པའི་དངོས་པོ༌[^1198]ལ་རབ་ཏུ་བྱང་བར་གྱུར་པས་ན་འཕྱར་བ་དང་རྒོད་པ་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1389]
ཞི་གནས་ལ་རབ་ཏུ་གནས་པས་གཙེ་བ༌[^1199]མེད་ཅེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་སེམས་རྩེ་གཅིག་པའི་མཚན་ཉིད་ལ་ལེགས་པར་འདུག་པས་ཏིང་ངེ་འཛིན་དང་མི་མཐུན་པའི་ཕྱོགས་ཕྱིན་ཅི་ལོག་ཏུ་རྟོག་ཅིང་དཔྱོད་པ་ལ་སོགས་པའི་སྐྱོན་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1390]
ལྷག་མཐོང་གིས་ཤིན་ཏུ་ཟིན་པས་ན། ནོར་བ་མེད་ཅེས་བྱ་བ་ལ། ལྷག་མཐོང་ནི་ཤེས་རབ་ལ་བྱ་སྟེ། དྲན་པར་བྱ་བའི་དངོས་པོ་རྣམས་ཤེས་རབ་ཀྱིས་མ་ནོར་བར་ཟིན་ཅིང་རྟོག་པས་ན་མ་འཁྲུལ་བའོ། །

[Block 1391]
དྲན་ཞིང་མི་བརྗེད་པའི་ཆོས་ཅན་པས་ན་ཞེས་བྱ་བ་ལ་སྔོན་ཐོས་པའི་ཆོས་དང་དོན་རྣམས་མ་བརྗེད་པ༌[^1200]ནི་དྲན་པའོ། །

[Block 1392]
ཕྱིས་བརྗེད་པར་མི་འགྱུར་བ་ནི་མི་བརྗེད་པ་སྟེ། དེ་ལྟ་བུའི་ཆོས་དང་ལྡན་པས་སྔོན་གྱི་གནས་དྲན་པའི་མངོན་པར་ཤེས་པ་དེ་དྲན་པར་བྱའོ། །

[Block 1393]
ཐེག་པ་ཆེན་པོ་རབ་ཏུ་ཤེས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་དྲན་པ་དེས་ཐེག་པ་ཆེན་པོའི་ཆོས་ཁོང་དུ་ཆུད་པའི་ཕྱིར་ཁོང་དུ་ཆུད་པའི་རྒྱུ་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་དང་ལྡན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1394]
གཞན་ལ་རག་མ་ལུས་པས་ན་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་པའོ་ཞེས་བྱ་བ་ནི་བསམ་གཏན་འཁོར་གསུམ་ཡོངས་སུ་དག་པ་གཞན་གྱི་དྲིང་ལ་མི་འཇོག་པས་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་པའོ། །

[Block 1395]
ཐམས་ཅད་ཀྱི་ཕ་རོལ་ཏུ་འགྲོ་བའི་ཕྱིར་ཞེས་བྱ་བ་ལ་ཕ་རོལ་ཅེས་བྱ་བ་ནི་མཐར་ཕྱིན་པའམ་མཆོག་ཏུ་ཕྱིན་པ་ལ་བྱ་སྟེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ཀྱི་མཆོག་གམ་མཐར་ཕྱིན་པའི་ཕྱིར་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ཀྱི་ཚོགས་བསགས་པའོ། །

[Block 1396 [HEADING]]
#### གང་དྲན་པ། ^3-4-2-0

[Block 1397]
ཚེ་རབས་གཅིག་ཀྱང་དྲན་ནོ་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་གཅིག་ཀྱང་དྲན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1398]
གཞན་ནི་གོ་སླ་བསམ་བཤད་དེ། གང་དྲན་པ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 1399 [HEADING]]
#### ཇི་ལྟར་དྲན་པ། ^3-4-3-0

[Block 1400]
བདག་གི་མིང་ནི་འདི་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཚེ་རབས་གང་དུ་སྐྱེས་པའི་ཚེ་རེ་རེའི༌[^1201]མིང་ཡང་དྲན་པ་སྟེ། དཔེར་ན་ཚེ་འདིའི་ཚེ་ན་ནི་མང༌[^1202]ཡང་འདི་ཞེས་བྱ་ཚེ་འདིའི་ཚེ་ན་ནི་མིང་འདི་ཞེས་བྱ་བ་དྲན་པའོ། །

[Block 1401]
རིགས་འདི་ཞེས་བྱ་བ་ནི་ཚེ་རབས་དེ་དག་ཏུ་སྐྱེས་པས་ན་བདག་རིགས་བཞི་ལས་གང་དང་གང་དུ་སྐྱེས་པ་དྲན་པའོ། །

[Block 1402]
རུས་ཞེས་བྱ་བ་ནི་རིགས་བཞི་ལས་ཀྱང་མཐོན་དམན་དུ་ཕྱེ་བ་ཤེས་པས་ཏེ།[^1203] ཚེ་རབས་དེ་དག་ན་བདག༌[^1204]གི་ཕའི་རུས་ནི་འདི་ཞེས་བྱ། མའི་རུས་ནི་འདི་ཞེས་བྱ་ཞེས་བྱ༌[^1205]བ་ལ་སོགས་པའོ། །

[Block 1403]
ཁ་དོག་ནི་འདི་འདྲ་ཞེས་བྱ་བ་ནི་ཁ་དོག་ཡིད་དུ་འོང་བ་དང་། ཡིད་དུ་མི་འོང་བ་དང་། མཛེས་པ་དང་མི་མཛེས་པ་ཅི་འདྲ་བར་གྱུར་པ་དང་དྲན་པའོ། །

[Block 1404]
ཁ་ཟས་འདི་ལྟ་བུ་ཞིག་ཟ་ཟ་ཞེས་བྱ་བ་ནི་སྟོན་པ་དྲན་པ་སྟེ། ཚེ་རབས་དེ་དང་དེ་དག་ཏུ་ཁ་ཟས་ཅི་དང་ཇི་ལྟ་བུ་ཟོས་པ་དྲན་པའོ། །

[Block 1405]
ཚེའི་ཚད་ནི་འདི་ཙམ་ཞིག་ཐུབ་ཅེས་བྱ་བ་ནི༌[^1206]ཚེའི་འདུ་བྱེད་དྲན་པ་སྟེ།
--- END BLOCKS ---
