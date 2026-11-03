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
[Block 1436 [HEADING]]
#### རྒྱུ་རྣམ་པར་དག་པས་བྱུང་བ། ^3-5-1-0

[Block 1437]
གང་འདུན་པ་དང་། བརྩོན་འགྲུས་དང་། སེམས་དང་དཔྱོད་པས་ཟིན་པའི་ཆོས་རྣམས་བསྒྲུབ་པ༌[^1238]དང་ཞེས་བྱ་བ་ལ། འདུན་པ་ལ་སོགས་པ་བཞི་པོ་མིང་གིས་སྨོས་པ་འདི་དག་ནི་རྫུ་འཕྲུལ་གྱི་རྐང་པ་ཞེས་བྱ་སྟེ། རྫུ་འཕྲུལ་བ༌[^1239]སྐྱེད་པའི་རྒྱུའོ། །

[Block 1438]
རྫུ་འཕྲུལ་ནི་འོག་ནས་འབྱུང་བའི་གཟུགས་དང་། སྟོབས་དང་བྱིན་གྱི་རླབས༌[^1240]ལ་སོགས་པ་ལྟ་བུར་སྤྲུལ་ཅིང་འབྱོར་པ་ནུས་པ་ལ་བྱའོ། །

[Block 1439]
དེ་སྤྲུལ་ཅིང་འབྱོར་པ་ནུས་པའི་རྒྱུ་འམ་གཞི་འམ། དེ་ལྟ་བུའི་གནས་སུ་ཕྱིན་པར་བྱེད་པ་ནི་འདུན་པ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་བཞི་པོ་འདི་རྣམས་ཡིན་པས་འདུན་པ་ལ་སོགས་པ༌[^1241]བཞི་པོ་འདི་རྣམས་ལ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་ཞེས་བྱའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། འདུན་པས་ནི་ཐོག་མ༌[^1242]ཉིད་དུ་རྫུ་འཕྲུལ་ལ་མངོན་དུ་ཕྱོགས་པའམ་དད་པར་བྱེད། བརྩོན་འགྲུས་ནི་དེ་སྒྲུབ་པར་བྱེད། །སེམས་ཀྱིས་ནི་བསྒྲུབ་པ༌[^1243]རྣམས་ཆུད་མ༌[^1244]ཟོས་པར་བཟུང་བའི་ཆོས་གཏན་ལ་ཕབ་ནས་རྟོག་པར༌[^1245]བྱེད་དེ། དེ་ལྟ་བུ་ལ་རྫུ་འཕྲུལ་འབྱུང་བའི་ཕྱིར་དེ་རྣམས་ནི་རྫུ་འཕྲུལ་གྱི་རྐང་པའོ། །

[Block 1440]
རབ་ཏུ་ཟིན་པའི་ཆོས་རྣམས་ཞེས་བྱ་བ་ལ། འདུན་པ་དང་བརྩོན་འགྲུས་དང་། སེམས་དང་དཔྱོད་པ་རྣམས་ཀྱིས་བསྒྲུབ༌[^1246]པའམ། དེ་དག་ལྡན་པའི་གཟུགས་དང་བྱིན་གྱི་རླབས༌[^1247]འོག་ནས་འབྱུང་བ་རྣམས་སྒྲུབ་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1441]
སྒྲུབ་པ་ནི་མ་ཐོབ་པ་ལས་ཐོབ༌[^1248]པར་བྱེད་པའོ། །

[Block 1442]
ལས་སུ་རུང་བ་ནི་ཐོབ་པ་ནས་སྤྱོད་ནུས་པའོ། །

[Block 1443]
དབང་བྱེད་པ་ནི་སྤྱོད་ནུས་པ་ལས་ཀྱང་རབ་ཏུ་བྱང་ནས་ཅིར་དགར༌[^1249]བསྒྱུར་ནུས་པའོ། །

[Block 1444]
དེས་རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་པོ་འདི་དག་ཤིན་ཏུ་བསྒོམ་པའི༌[^1250]ཕྱིར། མངོན་པར་འདུ་བྱེད་པ་མེད་པའི་རྫུ་འཕྲུལ་མངོན་དུ་ཐོབ་པར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ནི་འདུན་པ་ལ་སོགས་པ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་གོང་དུ་སྨོས་པ་བཞི་པོ་རབ་ཏུ་བསྒོམས་ཏེ་བྱང་བར་གྱུར་པའི་མཐུས་གཟུགས་དང་སྟོབས་དང་། བྱིན་གྱི་རླབས༌[^1251]ཀྱིས་རྫུ་འཕྲུལ་འོག་ནས་འབྱུང་བ་རྣམས་གསལ༌[^1252]ཞིང་འབད་མི་དགོས་པར་ལན༌[^1253]གྱིས་གྲུབ་པ་ཉིད་དུ་ཐོབ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1445]
དེ་རྫུ་འཕྲུལ་གྱི་ཆོ་འཕྲུལ་རྣམ་པ་དུ་མ་མྱོང་བ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ལྷུན་གྱིས་གྲུབ་པ༌[^1254]ལས།

[Block 1446]
རྫུ་འཕྲུལ་མངོན་པར་ཤེས་པ་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེ་རྫུ་འཕྲུལ་རྣམ་པ་མང་པོ་སྤྱོད་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1447 [HEADING]]
#### རྣམ་པ་སྣ་ཚོགས་སུ་སྟོན་པ། ^3-5-2-0

[Block 1448]
གཟུགས་སོ༌[^1255]ཞེས་བྱ་བ་ནི་གཟུགས་བཟང་ངན་གང་གིས༌[^1256]འདུལ་བའི་གཟུགས་དེ་སྟོན་པའོ། །

[Block 1449 [VERSE]]
སྟོབས་ནི་ལུས་ཀྱི་མཐུ་དང་རྩལ་ལོ། །
བྱིན་གྱིས་བརླབས་པ་ཆུར་སྒྱུར་བ་དང་།
ཆུ་མེར་སྒྱུར་བ༌[^1257]ལ་སོགས་པའོ། །

[Block 1450]
མོས་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཆོས་སྟོན་ཏོ་ཞེས་བྱ་བ་ནི་རྫུ་འཕྲུལ་གྱི༌[^1258]ཆོ་འཕྲུལ་གྱིས༌[^1259]བཏུལ་ནས་ཆོས་གང་ལ་དད་པའི་ཆོས་དེ་སྟོན་པའོ། །

[Block 1451 [HEADING]]
#### དབང་དུ་བྱ་བ། ^3-5-3-0

[Block 1452]
སྟོབས་དེ༌[^1260]དང་དེ་ཉིད་སྟོན་ཞེས་བྱ་བ་ནི་སེམས་ཅན་དེ་དག་པས་སྟོབས་ཆེ་བའི་སེམས་ཅན་དེ་དང་དེ་དག་གི་སྟོབས་ཉེ་བར་སྟོན་པའོ། །

[Block 1453]
དེ་བཞིན་དུ་ཐ་མ་དང་འབྲིང་དང་རབ་ཅེས་བྱ་བ་ལ་ཐ་མ་རབ་ཏུ་གྱུར་ཅིག་ཅེས་བྱིན་གྱིས་བརླབས་ན་དེ་དེ་བཞིན་དུ་འགྱུར་བ་ལ་སོགས་པ་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 1454 [HEADING]]
#### ཐམས་ཅད་གཟུགས་སུ་འཛུད་པ། ^3-5-4-0

[Block 1455]
འཇིག་རྟེན་དུ་ཆོས་དང་མཐུན་པས༌[^1261]སུས་ཀྱང་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ན་བདག་དང་འདྲ་བར་གྱུར་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1456 [HEADING]]
#### གཞན་དུ་བྱ་བ། ^3-5-5-0

[Block 1457]
བྱིན་གྱི་རླབས༌[^1262]ནི་རྫུ་འཕྲུལ་གྱི༌[^1263]བྱིན་གྱི་རླབས༌[^1264]སོ། །

[Block 1458 [HEADING]]
#### གཞན་གྱི་རྫུ་འཕྲུལ་ཟིལ་གྱིས་གནོན་པ། ^3-5-6-0

[Block 1459]
ཡེ་ཤེས་ཀྱི༌[^1265]སྟོབས་སྐྱེད༌[^1266]ཅེས་བྱ་བ་ནི་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ཀྱི་མཐུ་བསྐྱེད་པས་སོ། །

[Block 1460]
བརྗོད་པ་སྣ་ཚོགས་དང་དགའ་བ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་བཤད་པ་སྣ་ཚོགས་ལ་དགའ་བའོ། །

[Block 1461]
རྫུ་འཕྲུལ་གྱི་རྐང་པ་དེ་དག་ཀྱང་མངོན་པར་འཕགས་སོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་རྫུ་འཕྲུལ་གྱི་རྐང་པ་དེ་འཇིག་རྟེན་པ་དང་དྲང་སྲོང་ལ་སོགས་པའི་རྫུ་འཕྲུལ་གྱི་རྐང་པ་དང་། འཇིག་རྟེན་ལས་འདས་པ་ཉན་ཐོས༌[^1267]ལ་སོགས་པ་ལས་ཀྱང༌[^1268]ཁྱད་ཞུགས་པའི་ཕྱིར་རོ། །

[Block 1462]
བདུད་དང་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱི་ཡུལ་ལས་འདས་པ་ཞེས་བྱ་བ་ནི་བདུད་དང་ཉོན་མོངས་པ་ཐམས་ཅད་དེས༌[^1269]སྤངས་ལ་བདུད་དང་ཉོན་མོངས་པ་དང་ལྡན་པ་རྣམས་ཀྱིས་ཐོབ་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1463]
སངས་རྒྱས་ཀྱི་ཡུལ་ལ་འཇུག་པ་ཞེས་བྱ་བ་ནི་རྫུ་འཕྲུལ་དེས་ཆོས་ཀྱི་དབྱིངས་རྟོགས་པར༌[^1270]བྱེད་པའི་ཕྱིར་རོ། །

[Block 1464]
སེམས་ཅན་ལ་མི་གནོད་ཅེས་བྱ་བ་ནི་རྫུ་འཕྲུལ་དེས་སེམས་ཅན་རྣམས་ལ་ཕན་འདོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1465]
དགེ་བའི་རྩ་བ་དང་ཚོགས་ཐམས་ཅད་བསྩགས་པ་ཞེས་བྱ་བ་ནི་རྫུ་འཕྲུལ༌[^1271]བརྩམས་པ་ཐམས་ཅད་ཀྱང་དགེ་བའི་རྩ་བ་དཔག་ཏུ་མེད་པ་ལ་སོགས་པའི་རྒྱུར་འགྱུར་བས་སོ། །

[Block 1466]
འདོད་པའི་ཁམས་ཀྱི་དབང་ཕྱུག་ཆེན་པོ་ཐོབ་པའི་ལྷའི་བུ་ནི་བདུད་དོ། །

[Block 1467]
བདུད་དེའི་འཁོར་དང་གཡོག་ཏུ་གཏོགས་པའི་ལྷ་རྣམས་ནི་བདུད་ཀྱི་རིགས་ཀྱི་ལྷའོ། །

[Block 1468]
མི་འཕྲོགས་པ་ནི་དེ་དག་གིས༌[^1272]བྱང་ཆུབ་སེམས་དཔའི་རྫུ་འཕྲུལ་མེད་པར་བྱ་ཞིང་ཟིལ་གྱིས༌[^1273]གནོན་པར་མི་ནུས་པའོ། །

[Block 1469]
འདི་ནི་རྫུ་འཕྲུལ་བྱ་བ་མངོན་པར་ཤེས་པ་ལྔ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1470 [HEADING]]
### འབྱུང་བ་མངོན་སུམ་དུ་གྱུར་པ། ^3-6-0

[Block 1471]
འབྱུང་བ་མངོན་སུམ་དུ་གྱུར་པ་ནི་ཟག་པ་ཟད་པ་མངོན་སུམ་དུ་བྱས་པ་སྟེ། སློབ་དཔོན་ཐོགས་མེད་ཀྱིས་མངོན་སུམ་དུ་གྱུར་པ་དྲུག་ཡོད་པའི་ཕྱིར་བསྡུས་པའི་དོན་གྱི་ནང་དུ་སྨོས་མོད་ཀྱིས།[^1274] དེ་བཞིན་གཤེགས་པ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^1275]ཟག་པ་ཟད་པ་མངོན་སུམ་དུ་མ་བྱས་པས་ན་མདོ་ལས་ནི་མ་གསུངས་སོ། །

[Block 1472]
[^1276]

[Block 1473 [HEADING]]
## ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^4-0

[Block 1474]
ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^1277]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་བསྡུ་བའི་དངོས་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བསྡུ་བའི་དངོས་པོ་ནི་དགའ་བའི་དངོས་པོ་འམ། ཕན་པར་བྱེད་པའི་དངོས་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1475]
དེ་མི་ཟད་པ་ཡང་དེས་བསྡུ་བར་བྱ་བའི་སེམས་ཅན་མི་ཟད་པས་སྡུད་པར་བྱེད་པའི་དངོས་པོ་ཡང་མི་ཟད་པའོ། །
--- END BLOCKS ---
