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
[Block 1436]
དེའི་ཕྱིར་གཅིག་ཏུ་གྱུར་པ་ནི་གདོང་དུ་མཚོན་གྱི་ལས་བྱེད་པ་དང་། གཞང་འབྲུམ་གཅོད་པ་ཡིན་ཏེ་འདི་གཉིས་ཡིན་པས་འདི་གཉིས་ལ་ཡང་སྦོམ་པོར་རིག་པར་བྱའོ། །

[Block 1437]
མཚོན་ལས་གཞན་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ་གཞན་གྱིས་ཀྱང་ཞེས་བྱ་བ་ནི་སེན་མོ་ལ་སོགས་པས་ཀྱང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1438]
དེ་གསང་སྔགས་དང་སྨན་དག་གིས་གསོའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་གཞང་འབྲུམ་རྣམས་སོ། །

[Block 1439]
ཞེ༌[^1244]འགྲས་པ་གསོར་མི་གཞུག་གོ་ཞེས་བྱ་བ་ནི་གཞང་འབྲུམ་རྣམས་སོ། །

[Block 1440]
གསོ་བའི་ཕྱིར་ནུབ་མོ་ཟ་བ་ནི་ཚུལ་དང་མི་མཐུན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། སིལ་བུ་དག་ལས་མདོ་འདི་དག༌[^1245]དང་འོག་མ་གཉིས་སོ། །

[Block 1441]
འདི་ལ་བྱིན་ལེན་མ་བྱས་པ༌[^1246]གསོག་འཇོག་བྱས་པ་དག་མི་རུང་བ་ཉིད་དུ་དོགས་པར་མི་བྱའོ་ཞེས༌[^1247]བྱ་བ་ནི་གསོ་བ་འདི་ལའོ། །

[Block 1442]
གསོ་བའི་ཕྱིར་རེང་བུའི་དུ་བས་བདུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཕྲན་ཚེགས་དག་ལས།

[Block 1443]
འདི་དང་པོར་བྱས་ཏེ་འདི་བཟའ་བར་བྱ་བ་མ་ཡིན་པ་མ་ཡིན་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 1444]
དེ་ནི་སྨན་གཅེའུས༌[^1248]འགྲུབ་པའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དུ་བར་བདུག༌[^1249]པ་དེའོ། །

[Block 1445]
ལྕགས་ལས་བྱས་པའོ་ཞེས་བྱ་བ་ནི་སྨན་གཅེའུའོ། །

[Block 1446]
སོར་བཅུ་གཉིས་པ་བཟང་ངོ་། །རྣོ་བ་དང་རྩུབ་པ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྨན་གཅེའུའི་སྦུབས་སོ། །

[Block 1447]
ཞུན་མར་རམ་བུ་རམ་གྱིས་བསྐུས་ཏེ་ཤུབས་སུ་གཞུག་གོ། །

[Block 1448]
དེ་ནི་ཟུང་ངམ་ཆོས་གོས་ཀྱི་གདང་བུ་ལ་གདགས་སོ་ཞེས་བྱ་བ་ནི་ཤུབས་དེའོ། །

[Block 1449]
དྲི་མ་མེད་པར་བྱ་བའི་ཕྱིར་མེར་གཞུག་གོ་ཞེས་བྱ་བ་ནི་སྨན་གཅེའུའོ། །

[Block 1450]
སྣར་བླུགས་པའི༌[^1250]ལས་བྱའོ། །

[Block 1451]
དེ་ནི་སྣར་ལྡུགས་པ༌[^1251]སྤྱད་ཀྱིས་འགྲུབ་པོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་སྣར་ལྡུགས་པའི་ལས་བྱས་པ་དེའོ། །

[Block 1452]
མཆུ་གཉིས་མི་རྣོ་བ་བཟང་ངོ་ཞེས་བྱ་བ་ནི་སྣར་ལྡུགས་པའི་སྤྱད་ནི་ཁ་བྲག་མཆུ་གཉིས་པ་མི་རྣོ་བ་བཟང་ངོ་། །དེ་བྱའོ་ཞེས་བྱ་བ་ནི་སྣར་ལྡུགས་པའི་སྤྱད་དེའོ། །

[Block 1453]
དེ་ནི་བཟའ་བར་བྱ་བ་མ་ཡིན་པ་མ་ཡིན་ཏེ། བྱིན་ལེན་བྱས་ཏེ། སྣར་བླུགས་པའི་ལས་བྱའོ། །

[Block 1454]
གལ་ཏེ་འཚོ་བའི་བར་དུ་བཅང་བ་སྨིན་པར་འགྱུར་ན། དེས་རང་ཉིད་ཀྱིས་བཟུང་སྟེ། སྦྱངས་ཏེ་སྦྱིན་པར་བྱ་ཞེས༌[^1252]སྨོས་ཏེ། དེ་ལ་དྲི་མ་མེད་པའི་རིགས་པའི་གནས་ལ་སོགས་པ་དང་ལྷན་ཅིག་ཏུ་དེ་ལྟ་བུས་བསྡུ་བ་འདིའོ། །

[Block 1455]
སྨན་གྱི་གོ་རིམས་ནི་དཔེའོ་ཞེས་སྨོས་ཏེ་དེས་མཚོན་པ་གཞན་བསྟན་པའི་ཕྱིར། སྨན་གྱི་ཕྱིར་ཤ་རློན་པ་བསྟེན་པར་བྱའོ། །

[Block 1456 [VERSE]]
དེ་ཟ་མི་ནུས་ན་ཐབས་བྱའོ། །
རས་ཀྱིས་མིག་གཉིས་དགབ་པོ། །

[Block 1457]
མི་རྒལ་བར༌[^1253]བྱ་བའི་ཕྱིར་དྲི་ཞིམ་པོས་བསྒོའོ། །

[Block 1458]
ཤ་མེད་པ་ཉིད་ན་མདུན་དུ་བཟའ་བ་དང་བཅའ་བ་ཡིད་དུ་འོང་བ་གཞག་སྟེ་དགྲོལ་ལོ་ཞེས་བྱ་བ་ལ། དགྲོལ་ལོ་ཞེས་བྱ་བ་ནི་མིག་རས་ཀྱིས་གཡོགས་པ་དེའོ། །

[Block 1459]
གཞན་གྱི་དོན་དེར་ན་སྦོམ་པོའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ཤ་རློན་པ་དེ་སྨན་གྱི་དོན་ལས་གཞན་པར་ཟ་བ་ལ་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 1460]
མིའི་ཤ་ནི་ཐམས་ཅད་དུའོ་ཞེས་བྱ་བ་ནི་སྨན་གྱི་དོན་དུ་ཡང་མི་ཤ་ཟོས་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 1461]
སྨན་གྱི་ཕྱིར་ཟ་བ༌[^1254]ཡང་བཅོམ་ལྡན་འདས་ཀྱིས༌[^1255]སྨད་པས་དེ་དགག་པ་དེའི་ཕྱིར་ཐམས་ཅད་དུའོ་ཞེས་མདོར་བསྡུ་བ་བྱས་སོ། །

[Block 1462]
ཤ་བསྔོས་པར་ཤེས་ན་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཟ་བ་པོ་ལ་བརྟེན་ནས་བསྔོས་པར་ཟ་བ་པོས་མཐོང་བ་དང་ཐོས་པ་དང་དོགས་པའི་སྒོ་ནས་ཤེས་ན་དེས་ཤ་ཟ་བར་མི་བྱ་སྟེ། རྣམ་པར་རྟོག་པ་ཡོངས་སུ་སྐྱེས་པས་བཟའ་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་དུ་སྨོས་པ་གང་ཡིན་པ་དེ་འདིས་མ་བསྡུས་པ༌[^1256]ཡིན་ནོ། །

[Block 1463]
གལ་ཏེ་རྣམ་པར་རྟོག་པ་དེ་ངེས་ན་ནི་ཤེས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1464]
གལ་ཏེ་ཡིད་གཉིས་སུ་གྱུར་ན་འདུ་ཤེས་པ་ལྟར་ཡིད་གཉིས་སོ༌[^1257]སྙམ་དུ་ངེས་པའི་ཕྱིར་དེས་འདི་བསྡུས་པའོ། །

[Block 1465]
སྟག་གི་གོད་མའི་ཤ་མི་བཟའོ་ཞེས་བྱ་བ་ནི། ཤར་ཤེས་ན་ཟ་བར་མི་བྱའོ། །

[Block 1466]
འདི་ནི༌[^1258]ཕྲན་ཚེགས་དག་ལས་དགེ་སློང་དག་སྟག་ནི་རུལ་སྦེད་པ་ཡིན་པས་དེའི་ཕྱིར་དགེ་སློང་གིས་སྟག་གི་གོད་མའི་ཤ་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བར༌[^1259]སྦྱར་རོ། །

[Block 1467]
གླང་པོ་ཆེ་དང་། རྟ་དང་། ཀླུ་རྣམས་ཀྱི་མི་བཟའོ། །

[Block 1468]
མིག་གཅིག་པ་དང་། ཝ་དང་། སྤྲེའུ་དང་། ཤིང་རྟ་མོ་དང་། བྱ་རོག་དང་། བྱ་རྒོད་དང་། ཆུ་སྐྱར་དང་། ཁྱི་དང་། བྱ་ཁྲ་དང་། འུག་པ་དང་། དེ་དག་ལས་གཞན་པའི་བྱ་མི་རོ་ཟ་བ་དག་དང་། བྱ་གར༌[^1260]དང་། ཕ་བང༌[^1261]དང་། སྐྱིན་གོར༌[^1262]དང་། དྲེའུ་སྲིན་དང་། སྲིན་བུ་རྣམས་ཀྱི་ཡང་མི་བཟའོ་ཞེས་བྱ་བ་ནི། དེ་དག་གི་ཤ་ཡང་ཤེས་ན་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1469]
དེ་ལས་གཞན་པའི་ཞེས་བྱ་བ་ནི་གང་དུ་མི་རོ་ཟ་བའི་བྱ་སྔར་བསྟན་པ་དེ་དག་ལས་གཞན་པའི་ལའོ།[^1263] །

[Block 1470]
ཞུ་བའི་གཞུང་ཁ་ཅིག་ལས།

[Block 1471]
སྲིན་བུ་རྣམས་ཀྱི༌[^1264]ཚིལ་འཚལ་བར་བགྱིའམ། འཚལ་བར་མི་བགྱི། བཀའ་སྩལ་པ་བཟའ་བར་མི་བྱའོ། །

[Block 1472]
ནད་དང་བྲལ་བའི་ཕྱིར་ལུས་བསྐུ་བར་ནི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1473]
གཞན་ངང་སྐྱ་ལ་སོགས་པ་རྣམས་ནི་དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས་སོ། །

[Block 1474]
ལྷག་མ་རྣམས་ནི་སིལ་བུ་དག་ལས་སོ། །

[Block 1475]
ཤའི་བྱིན་ལེན་སྟོབས་པ་ལ་བཅད་པ་ལས་བྱུང་བ་ཉིད་མ་ཡིན་ནམ་ཞེས་དྲི་བར༌[^1265]བྱའོ་ཞེས་བྱ་བ་ནི་མི་ལ་སོགས་པའི་ཤ་བཅད་པ་གང་ཡིན་པ་དེ་བྱུང་བ་ཉིད་མ་ཡིན་ནམ་ཞེས་བྱ་བ་དང་། བཅས་པར་དྲི་བར༌[^1266]བྱའོ། །
--- END BLOCKS ---
