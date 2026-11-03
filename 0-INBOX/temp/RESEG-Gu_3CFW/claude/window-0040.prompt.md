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
[Block 1401]
དེའི་སྣོད་ནི་རྭའི༌[^1216]སྦུབས་བཟང་ངོ་ཞེས་བྱ་བ་ནི་ལན་ཚྭ་དེའིའོ།[^1217] །རྭ༌[^1218]ཇི་ལྟ་བུ་བཟང་ཞེ་ན། དེའི་ཕྱིར་ལྕི་བས་ཀུན་ནས་བསྐོར་བའོ། །

[Block 1402]
[^1219]དེ་མེད་པའི་ཉེས༌[^1220]པར་མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་ཁ་གབ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་ཁ་གབ་དང་བྲལ་བའི་ཉེས་པ་གང་ཡིན་པ་དེའོ། །ཅི་ལས་བྱས་པ་ཞེ་ན། དེའི་ཕྱིར་དེ་ཉིད་ལས་བྱས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྭ་ལྕི་བས་ཀུན་ནས་བསྐོར་བ༌[^1221]ལས་བྱས་པའི་འགང་གཞུག་པའོ། །

[Block 1403]
དྲིས་བསྒོས་པའི་སའོ་ཞེས་བྱ་བ་ནི་ནད་པས་བཅང་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1404]
ཆུ་སྲོ་བའི་ཕྱིར་ལྕགས་ཀྱི་གར་བུའོ་ཞེས་བྱ་བ་ཡང་ནད་པས་བཅང་ངོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1405]
ཐམས་ཅད་ཀྱིས༌[^1222]སྤྱད་པར་བྱའོ། །ཞེས་བྱ་བ་ནི་ནད་པ་འབའ་ཞག་གིས་སྤྱད་པར་མ་ཟད་ཀྱི་ན་བ་དང་མི་ན་བ་ཐམས་ཅད་ཀྱིས་སྤྱད་དུ་རུང་བའོ། །

[Block 1406]
འདིར་གཞུང་ཁ་ཅིག་ལས་ནི། བཅོམ་ལྡན་འདས་ཀྱིས་བསྲོ་ཁང༌[^1223]བྱའོ་ཞེས་གསུངས་པ་དང་། གནས་པར་བྱ་བའི་དགེ་སློང་དག་ཆུ་དྲོན་བསྐོལ་བས་ངལ་བར་གྱུར་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་བ། ལྕགས་ཀྱི་གར་བུ་བསྲེག་པར་བྱ་ཞིང་ལྕགས་ཐག་གིས་གདགས་པར་བྱའོ་ཞེས་གསུངས་པ་དེ་མདོ་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 1407]
དེ་ལྟ་བུར་གྱུར་པའི་དོགས་པ༌[^1224]དང་། འོས་པ་དགེ་འདུན་གྱིས་འཆང་བ་ལ་མི་རིགས་པ༌[^1225]མེད་དོ། །

[Block 1408]
དེ་ལྟ་བས་ན་དགེ་འདུན་གྱིས་ཀྱང་བཅང་དུ་རུང་པར་རིག་པར་བྱའོ། །

[Block 1409]
བསྲེགས་པ༌[^1226]གདགས་པའི་ཕྱིར་དེ་ལ་ལྕགས་ཐག་གདགས་སོ་ཞེས་བྱ་བ་ལ་དེ་ལ་ཞེས་བྱ་བ་ནི་ལྕགས་ཀྱི༌[^1227]གར་བུ་དེ་ལའོ། །

[Block 1410]
ཚ་བའི་དུས་ནས་གཤེར་བས་དེ་མནན༌[^1228]ནོ་ཞེས་བྱ་བ་ལ། དེ་མནན༌[^1229]ཏོ་ཞེས་བྱ་བ་ནི་ལྕགས་ཐག་དེ་མནན༌[^1230]པའོ། །

[Block 1411]
བསྲེགས་པ་ནི་ཟས་དང་འབགས་པའི་གནས་མེད་དོ་ཞེས་བྱ་བ་ནི། ལྕགས་ཀྱི༌[^1231]གར་བུ་བསྲེགས་པ་ན་དེ་ལ་ཟས་དང་འབགས་པའི་གནས་མེད་པའོ། །

[Block 1412]
དེ་བས་ན་ལྕགས་ཀྱི་བར་དུ་དེ་རུང་བར་བྱ་བའི་ཕྱིར་འབད་པ་ནི་དོན་མེད་དོ། །

[Block 1413]
དེའི་ཕྱིར་དེ་ལ་འདི་བརྗོད་དོ། །

[Block 1414]
རུང་བ་སྔར་བསྲོ་བའོ། །

[Block 1415]
ལོངས་སྤྱད་པ་ཕྱིས་སོ་ཞེས་བྱ་བ་ནི་འདི་གཉིས་ནི་གཙང་སྦྲའི༌[^1232]ཕྱིར་དེ་བསྒྲུབ་བོ། །

[Block 1416]
མདོམས༌[^1233]ཀྱི་གསོ་བ༌[^1234]བསྟེན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་པ་ཞེས་བྱ་བར་དོན་གྱིས་གྱུར་པ་དང་སྦྱར་རོ། །

[Block 1417]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས།

[Block 1418]
མས་བཏང་བར༌[^1235]བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 1419]
གཞན་གྱིས་འཚོ་བར་ནུས་པ་ཉིད་ན་དེ་ལ་སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི་སྨན་གཞན་བྱ་བའི་ཐབས་ཀྱིས་ནད་དེ་ལས་འཚོ་བར་ནུས་པ་ཉིད་ཡིན་ན་མདོམས༌[^1236]ཀྱི་གསོ་བ་བསྟེན་པ་དེ་ལས་ཉེས༌[^1237]པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 1420]
འདིར་གཞུང་ནི་མ་མོ་ལས།

[Block 1421]
དེ་ལས་གཞན་པའི་སྨན་དག་གིས་འཚོ་ན་དགེ་སློང་གིས་མདོམས༌[^1238]ཀྱི་ལས་བྱེད་དུ་མི་གཞུག་གོ། །

[Block 1422]
གང་བྱེད་དུ་འཇུག་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 1423]
མི་འཚོ་བ་ཉིད་ཡིན་ན་བྱེད་དུ་གཞུག་གོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1424]
འདི་ལ་ཟངས་མའམ་ཁར་བའི༌[^1239]སྦུ་གུ་བཟང་གི་ལྕགས་ཀྱི་ནི་མི་རུང་ངོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་མདོམས༌[^1240]ཀྱི་གསོ་བ་འདི་ལའོ། །

[Block 1425]
མཚོན་གྱིས་གསོ་བ་ཡང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ལ། དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་མཚོན་གྱིས་གསོ་བ་བསྟེན་པར་བྱ་བ་ལའོ། །

[Block 1426]
གཞན་གྱིས་འཚོ་བར་ནུས་པ་ཉིད་ན་དེ་སྦོམ་པོའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1427]
འདིར་གཞུང་ནི་མ་མོ་ལས།

[Block 1428]
རྟུལ་བ་གཞན་ཡོད་ན་དགེ་སློང་གིས༌[^1241]མཚོན་གྱི་ལས་བྱེད་དུ་མི་གཞུག་གོ། །

[Block 1429]
གང་བྱེད་དུ་འཇུག་ན་ཉེས་པ་སྦོམ་པོའོ། །

[Block 1430]
རྟུལ་བ་གཞན་མེད་ན་བྱེད་དུ་གཞུག༌[^1242]གོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1431]
གདོང་བུ་རྩའི་རྒྱུན་ལས་གཞན་པར་དེ་མི་བསྟེན་ནོ་ཞེས་བྱ་བ་ནི་གདོང་བུའི་རྩའི༌[^1243]རྒྱུན་ལས་གཞན་པར་མཚོན་གྱིས་འཚོ་བ་དེ་མི་བསྟེན་པའོ། །

[Block 1432]
འདིར་གཞུང་ནི།

[Block 1433]
ཕྲན་ཚེགས་དག་ལས།

[Block 1434]
དགེ་སློང་གི་གདོང་ནི་མེ་ལོང་ལྟ་བུ་ཡིན་པས། དེའི་ཕྱིར་སྨན་པ་གདོང་དུ་མཚོན་གྱི་ལས་བྱེད་དུ་མི་གཞུག་གོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1435]
གཞང་འབྲུམ་བཅད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་མི་བསྟེན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

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
--- END BLOCKS ---
