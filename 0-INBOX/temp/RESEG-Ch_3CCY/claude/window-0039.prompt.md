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
གང་ཡང་དེ་ལྟར་རང་བཞིན་གྱིས་ཡོད༌[^983]པ་མ་ཡིན་པས། དེ་ཇི་ལྟར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡོད་བཞིན་པར་འགྱུར། དེའི་རང་བཞིན་ཡོད་བཞིན་པ་མ་ཡིན་པ་ཉིད་དོ་ཞེས་དགོངས་པའོ། །

[Block 1367]
དེས་ན་འདི་ལྟར་དཔྱད་ན་རྣལ་འབྱོར་པ་དེ་ཁོ་ན་ཉིད་ངེས་པར་འགྱུར་ཏེ། རང་བཞིན་གྱིས་མ་སྐྱེས་པའི་དངོས་པོའི་དེ་ཁོ་ན་ཉིད་ཡོངས་སུ་ཤེས་པར་འགྱུར་རོ། །

[Block 1368]
དེ་ཁོ་ན་ཉིད་མཐོང་བར་གྱུར་ན་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་མི་དམིགས་པའི་ཕྱིར། ནམ་ཡང་ཆོས་རྣམས་ཀྱི་རང་བཞིན་ཡོངས་སུ་གསལ་བར་མི་བྱེད་དེ། རང་ཉིད་ཀྱིས་མ་དམིགས་པར་གཞན་ལ་བཤད་པ་མི་སྲིད་དོ། །

[Block 1369]
དེས་ན་ཡང་དག་ཉིད་དུ་ནམ་ཡང་ཆོས་བསྟན་པ་མ་ཡིན་ནོ་ཞེས་གྲུབ་བོ། །

[Block 1370]
དེ་ལྟར་ཚིགས་སུ་བཅད༌[^984]པ་གཉིས༌[^985]ཀྱིས་རབ་ཏུ་བྱེད་པ་མ་ལུས་པར་བསྒྲུབ་པའི༌[^986]དོན་བསྡུས་པའི་ཚུལ་གྱིས་ཉེ་བར་བསྟན་ནས། དེ་ལས་གཞན་ལ་ཇི་ལྟར་བསྟན་པའི་ཆོས་རྣམས་ཀྱི་རང་བཞིན་རྣམ་པར་འབྱེད་པས་ངེས་པར་བླ་ན་མེད་པའི་འབྲས་བུའི་དངོས་གྲུབ་མ་ཐོབ་པ་རྣམས། སླར་ཡང་ཐོས་པ་དང་བསམ་པ་དང་བསྒོམ་པ་ལ༌[^987]ཡང་དག་པར་བརྩོན་པ་བསྐྱེད་པའི་ཕྱིར་དང་། མ་ཞུགས་པ་རྣམས༌[^988]ཞུགས་པ་དང་ལྡན་པ་ཡང་སྤྲོ་བ་བསྐྱེད་པའི་དོན་དུ་ཡང་ཚིགས་སུ་བཅད་པ་གཉིས་གསུངས་པ།

[Block 1371 [HEADING]]
### ཚིགས་བཅད་དོན་གཅིག་པ། ^1-70-0

[Block 1372 [VERSE]]
ཚུལ་འདི་ཡང་དག་རྗེས་དཔོག་གང་། །
དད་ལྡན་དེ་ཉིད་ཚོལ་ལ་བརྩོན། །
རྟེན་མེད་ཆོས་འགལ༌[^989]བརྟེན་པ་ཡིས། །
སྲིད་དང་སྲིད་མིན་སྤངས་ནས་ཞི། །

[Block 1373]
ཚུལ་འདི་ནི་དེ་ལྟར་ཇི་སྐད་དུ་སྨོས་པའི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བར་གནས་སོ་ཞེས་པའི་དོན་ཏོ། །

[Block 1374]
ཡང་དག་རྗེས་དཔོག་གང་ནི། རང་གི་རང་བཞིན་ཡོངས་སུ་གཅོད་པའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1375]
ཁོང་དུ་ཆུད་པ་ཡང་གལ་ཏེ་ན་སྐྱོན་རྗེས་སུ་ཚོལ་བ་ལ་བརྩོན་པས་ཁོང་དུ་ཆུད་པའོ་ཞེ༌[^990]ན། གསུངས་པ། དད་པ་དང་ལྡན་ཡང་གལ་ཏེ་རྩོད༌[^991]པའི་བསམ་པས་ཀྱང་འབྱུང་ངོ་ཞེ་ན། གསུངས་པ། དེ་ཉིད་ཚོལ་ལ་བརྩོན་ཞེས་པ་ལ། དད་པ་དང་ལྡན་ན་ཡང་དོན་དམ་པ་ཁོང་དུ་ཆུད་པར་འདོད་པས་དེ་ཁོ་ན་ཉིད་འདི་ཉིད༌[^992]ཚོལ་བའོ། །

[Block 1376]
དེ་ཡང་རང་བཞིན་གྱིས་མི་དམིགས་པའི་ཕྱིར་མི་བརྟེན༌[^993]པའོ། །

[Block 1377]
ཆོས་འགའ་བརྟེན་པས༌[^994]ནི། ཆོས་འགའ་ཞིག་གསལ་བར་བྱེད་པའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1378]
དེ་ལྟར་རྟེན་མེད་ཆོས་འགའ་བརྟེན་པ༌[^995]དེས་ཅི་ཞིག་བྱེད་ཅེ༌[^996]ན། གསུངས་པ། སྲིད་དང་སྲིད་མིན་སྤངས་ནས་ཞི། །ཞེས་པ་ལ། སྲིད་པ་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔའོ། །

[Block 1379]
སྲིད་མིན་ནི་དེ་མེད་པའོ། །

[Block 1380]
དེ་གཉིས་འདིར་སྤངས་ན་ངེས་པར་དངོས་པོ༌[^997]དང་དངོས་པོ་མེད་པ་ཞི་བར་འགྱུར་ཏེ། སྲིད་དང་སྲིད་མིན༌[^998]དག་གི་འཇུག་པ་འགག་པས༌[^999]ཞི་བར་གྱུར་པའོ་ཞེས་པའི་དོན་ཏོ།། །།

[Block 1381]
སླར་ཡང་ཇི་ལྟར།

[Block 1382 [VERSE]]
སྲིད་དང་སྲིད་མིན་རྟག་སྤོང་ཞིང་། །
ཇི་ལྟར་དེ་ཞི་ཞེས་བརྗོད་ན། །
གང་ལས་དེའི་རྣལ་འབྱོར་པ་ནི། །

[Block 1383 [HEADING]]
### ཚིགས་བཅད་དོན་གཉིས་པ། ^1-71-0

[Block 1384]
འདི་དག་རྐྱེན་འདི་ལས་རིག་ན། །

[Block 1385 [VERSE]]
ལྟ་ངན་དྲ་བས་ཟིན་པ་ལྡོག །
དེས་ནི་ཆགས་རྨོངས་ཁྲོ་བ་རྣམས། །
སྤངས་ཕྱིར་མྱ་ངན་འདས་པ་ཐོབ། །

[Block 1386]
འདི་ནི་འདིའི་རྐྱེན་ལའོ་ཞེས་པས། རྐྱེན་འདི་པ་ལ། དེའི་དངོས་པོ་ནི་རྐྱེན་འདི་པའོ། །

[Block 1387]
འདིས་ཇི་སྐད་དུ་བསྟན་པའི་རྐྱེན་འདིས༌[^1000]གསུངས་སོ། །

[Block 1388]
རྣལ་འབྱོར་པ་གང་ཞིག་གིས་ཇི་སྐད་དུ་སྨོས་པའི་རྐྱེན་འདི་པ་ཁོང་དུ་ཆུད་པས་ཆོས་ཀྱི་རང་བཞིན་འགའ་ཡང་མི་དམིགས་པའི་ཕྱིར།[^1001] དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ཏུ་ཡོངས་སུ་མི་རྟོག་པར་གྱུར་པས། འཇིག་རྟེན་པའི་ལྟ་བ་ངན་པའི་དྲ་བའི་ནང་ནས་ལྡོག་ལ། དེ་ལས་ལོག་ནས་ཀྱང་། དངོས་པོ་དང་དངོས་མེད་ཀྱི་ལྟ་བས་བསླང་བ་འདིའི་སྲིད་དང་སྲིད་མིན་གྱི་རང་བཞིན་དུ་ཉེ་བར་དམིགས་པ་སྤངས་པས་སྤོངས་ལ། དེ་སྤངས་ནས་ཀྱང་ལྟ་བའི་རྩ་བ་འདོད་ཆགས་ལ་སོགས་པ་འདིའི་ཉོན་མོངས་པ་ལས་ལྡོག་གོ། །

[Block 1389]
ཡང་དག་པ་མ་ཡིན་པའི་ལྟ་བས་ཀུན་ནས་བསླངས་པའི༌[^1002]དངོས་པོ་དང་དངོས་པོ་མེད་པའི་ཡུལ་ཉིད་འཇིག་རྟེན་པས་རྟོགས་ལ། དེ་སྤངས་པར་གྱུར་ན་ཡང་། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་དེ་ལ་མི་སྣང་བའི་ཕྱིར། རྒྱུ་མཚན་མེད་པས་འདོད་ཆགས་ལ་སོགས་པ་འདི་ལ་མི་ལྡན་ལ། དེས་ན་རྣལ་འབྱོར་པ་དེ་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་དང་། གཏི་མུག་སྤངས་པའི་ཕྱིར་དྲི་མ་མེད་པ་སྟེ། ཉོན་མོངས་པ་མེད་པར་འགྱུར་རོ། །

[Block 1390]
ཉོན་མོངས་པ་མེད་ན་ཡང་། སྔར་འཕངས་པའི་དངོས་པོ་འདི་ཡོངས་སུ་ཟད་པ་དང་། སྔོན་མེད་པའི་དངོས་པོ་འཕེན་པ་སྤངས་པས་ངེས་པར་མྱ་ངན་ལས་འདས་པར་འགྲོ་བ་མ་ཡིན་ནམ། དེ་འདི་ལྟར་བླ་ན་མེད་པའི་མྱ་ངན་ལས་འདས་པའི་འབྲས་བུ་དོན་དུ་གཉེར་བའི་ཐུགས་རྗེ་ཆེན་པོ་དང་ལྡན་པ། ཤེས་རབ་ཅན་དང་། དད་པ་ཅན་དང་ལྡན་པས་ཀྱང་། ཇི་སྐད་དུ་སྨོས་པའི་རྐྱེན་འདི་པའི་མཚན་ཉིད། རང་བཞིན་གྱིས་སྟོང་པ་ལ། དེ་བཞིན་དུ་བསྒོམ་པར་བྱ་ཞིང་། ཚུལ་བཞིན་དུ་ཉན་པ་དང་བསམ་པར་བྱ་བ་ཡིན་ལ། གཞན་ཡང་རྣལ་འབྱོར་པས་རྟག་ཏུ་བསྒོམ་པ་ལ་ཤིན་ཏུ་བརྩོན་པ་དང་ལྡན་པར་འགྱུར་བར་རིགས༌[^1003]སོ་ཞེས་བྱའོ། །

[Block 1391 [HEADING]]
## བསྔོ་བ། ^a-0

[Block 1392 [VERSE]]
བསིལ་བའི་ངག་གི་འོད་ཀྱི་ཀུ་མུ་ད་ཅན་ནི། །
བདུན་ཅུ་པ་ནི་ཀུན་ནས་རབ་ཏུ་གསལ་བྱེད་པའི། །
ཟླ་བ་རྣམ་པར་འཕྲོ་བས་གསལ་བྱས་ལམ་རིག་པ། །

[Block 1393]
ཅི་ཡང་མིན་ཞིང་ཅི་ཡང་མིན་མིན་ཆགས་པས་བརྟེན།[^1004] །

[Block 1394 [VERSE]]
གང་ཞིག་དབུ་མར་འཇུག་པར་མ་སྨོས་པ་དག་དང་། །
གང་ཞིག་དབུ་མའི་ཚིགས་སུ་བཅད་པ་མི་གསལ་བ། །
དངོས་པོའི་དེ་ཉིད་མ་ལུས་དེ་དག་བདག་གིས་ནི། །
བདུན་ཅུ་པ་ཡི་རྣམ་པར་བྱེད་པ་འདིར་གསལ་བྱས། །

[Block 1395]
གང་ཞིག་ཐུགས་རྗེའི་བདག་ཉིད་ཐུབ་པའི་དབང་པོ་ཡིས། ། ཡུན་རིངས་དུས་ནས་འབད་པ་ཆེན་པོས་མཛད་པ་ཡི།[^1005] །

[Block 1396 [VERSE]]
དེ་ཡང་ངོ་བོ་ཉིད་ཀྱི༌[^1006]སྟོང་པ་ཞེས་བྱ་འདི། །
ལམ་ཆེན་རྒྱལ་བ་ཐམས་ཅད་རྗེས་སུ་གཤེགས་པ་སྟེ། །
དེ་ལ༌[^1007]འཇུག་ཕྱིར་སྟོང་ཉིད་བདུན་ཅུ་ཞེས་བྱ་བའི། །
བསྟན་བཅོས་གང་ཞིག་འཕགས་པ་ཀླུ་སྒྲུབ་ཅེས་བྱ་བས། །

[Block 1397]
གསུངས་པ་དེ་ནི་བདག་གིས་རྣམ་པར་ཕྱེ་བ་ཡི།[^1008] །དགེ་བ་གང་གིས་སྐྱེ་བོས༌[^1009]སངས་རྒྱས་ཉིད་གྱུར་ཅིག །

[Block 1398 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 1399 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 1400]
སྟོང་ཉིད་བདུན་ཅུ་པའི་རྒྱ་ཆེར་འགྲེལ་པ་སློབ་དཔོན་ཟླ་བ་གྲགས་པས་མཛད་པ།[^1010] །།

[Block 1401 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 1402 [VERSE]]
སྟོང་ཉིད་བདུན་ཅུའི་འགྲེལ་པ་ནི། །
དགེ་སློང་དྷརྨ་གྲགས་ཀྱིས་བསྒྱུར། །
གཞུང་གྲངས་སྟོང་ཕྲག་གཉིས་དང་ནི། །
བརྒྱ་ཕྲག་གཅིག་གིས་ལྷག་པ་ཡིན། །

[Block 1403]
དཔལ་ན༌[^1011]ལེན་དྲའི་གཙུག་ལག་ཁང་དུ་པཎྜི་ཏ་ཨ་བྷ་ཡཱ་ཀཱ་ར་དང་། སྣུར་ལོ་ཙཱ་བ་དྷརྨ་གྲགས་ཀྱིས་བསྒྱུར་བའོ།། །།

[Block 1404]
[^1]: ཏི་ ༼སྣར། པེ།༽ ཏི་ཊཱི་
[^2]: བདུན་ཅུ་པར། ༼སྣར།༽ བདུན་ཅུ་པ།
[^3]: ཐོབ་པ་ ༼སྣར། པེ།༽ ཐོས་པ་
[^4]: འཇིགས་པ་ ༼སྣར། པེ།༽ འཇིག་པ་
[^5]: ཁྱད་པར་ ༼སྣར། པེ།༽ ཁྱད་
[^6]: འཕགས་པ་ ༼སྣར། པེ།༽ འཕགས་པའི་
[^7]: གོམས་པའི་ཕྱིར་ ༼སྣར། པེ།༽ གོམས་པའི་
[^8]: ཁོན་ ༼སྣར། པེ།༽ འཁོན་
[^9]: སྐྱེ་བའི་སྐྱེ་ ༼སྣར། པེ།༽ སྐྱེ་
[^10]: དེས་ ༼སྣར། པེ།༽ དེ་
[^11]: གྱུར་པའི་ ༼སྣར། པེ།༽ འགྱུར་བའི་
[^12]: མགུ་ ༼སྣར། པེ།༽ འགུ་
[^13]: དེ་བཞིན་ ༼སྣར། པེ།༽ དེ་བཞིན་དུ་
[^14]: ལ་ལྟོས་ ༼སྣར། པེ།༽ ལ་མ་བལྟོས་
[^15]: ཕྱུང་ལ་ ༼སྣར། པེ།༽ ཕྱུང་ནས་
[^16]: གང་གི་ ༼སྣར། པེ།༽ གང་གིས་
[^17]: ལོག་ ༼པེ།༽ ལོགས་
[^18]: ལུས་པ་ ༼སྣར། པེ།༽ ལུས་པ་དང་
[^19]: གསུངས་པ་ནི་ ༼པེ།༽ གསུངས་པ་
[^20]: གནས་པའི་ ༼སྣར། པེ།༽ གནས་པའམ་
[^21]: དབང་ ༼པེ།༽ དབང་འཇིག་རྟེན་སྙད་དབང་
[^22]: གསུངས་ཀྱི་ ༼སྣར། པེ།༽ གསུང་གི་
[^23]: མཛད་ལ། ༼པེ།༽ མཛད་པ།
[^24]: གཉིས་ ༼པེ།༽ གཉིས་ཀྱིས་
[^25]: སྙད་ ༼སྣར།༽ སྙད་ཀྱི་
[^26]: རིགས་པར་ ༼སྣར། པེ།༽ རིག་པར་
[^27]: སྣང་བ་མ་ ༼པེ།༽ སྣང་བ་
[^28]: ཁོ་ནའོ་ ༼སྣར། པེ།༽ ཁོ་ནའི་
[^29]: འཇིག་རྟེན་པ་ ༼སྣར། པེ།༽ འཇིག་རྟེན་པ་ལ་
[^30]: ཉིད་ཀྱིས་ ༼སྣར། པེ།༽ ཉིད་ཀྱི་
[^31]: སྟོབས་ཀྱིས་ ༼སྣར།༽ སྟོབས་ཀྱི་
[^32]: གསུངས་པར་ ༼སྣར། པེ།༽ གསུང་བར་
[^33]: ཐ་སྙད་ཅེས་ ༼སྣར། པེ།༽ ཐ་སྙད་ཆེས་
[^34]: ཉིད་ཀྱིས་ ༼སྣར། པེ།༽ ཉིད་ཀྱི་
[^35]: ཉམས་པ་ ༼སྣར། པེ།༽ ཉམས་པར་
[^36]: རྟོག་པ་ ༼སྣར། པེ།༽ རྟོགས་པ་
[^37]: བརྗོད་བྱ་རྗོད་བྱེད་ཀྱི་ ༼སྣར།༽ བྱེད་ཀྱིས་ ༼པེ།༽ བརྗོད་བྱ་རྗོད་བྱེད་ཀྱིས་
[^38]: འཆད་པའི་ ༼སྣར། པེ།༽ ཆད་པའི་
[^39]: ལ་འདི་ལྟར་ ༼སྣར། པེ།༽ ལ་འདིར་
[^40]: འཇིག་རྟེན་ ༼སྣར། པེ།༽ འཇིག་
[^41]: གཞག་ ༼སྣར། པེ།༽ བཞག་
[^42]: ཡིན་པས་ ༼སྣར། པེ།༽ ཡིན་པ་
[^43]: འགའ་ཞིག་འགའ་ཞིག་ ༼སྣར། པེ།༽ འགའ་ཞིག་
[^44]: བརྗོད་ ༼སྣར། པེ།༽ རྗོད་
[^45]: ཞོག་ཤིག་ ༼སྣར། པེ།༽ ཞོག་ཅིག་
[^46]: ནི་ ༼སྣར། པེ།༽ ནི་བདེན་པ་
[^47]: སྒྲོ་ ༼སྣར། པེ།༽ དོན་སྒྲོ་མ་
[^48]: པར་བསྟན་ ༼སྣར། པེ།༽ པར་
[^49]: པའི་ ༼སྣར།༽ འདི་
[^50]: ཀྱི་མཐུས་ ༼སྣར།༽ ཀྱིས་ཐུས་
[^51]: བསྟན། ༼སྣར། པེ།༽ བསྟན་གྱི་
[^52]: མེད་པ་ ༼སྣར། པེ།༽ མེད་པས་
[^53]: གནས་ ༼སྣར། པེ།༽ གནས་པ་
[^54]: བྱེད་པ་ ༼སྣར། པེ།༽ བྱེད་པ་ལ་
[^55]: ལུང་གིས་ ༼སྣར། པེ།༽ ལུང་གི་
[^56]: གྲུབ་ ༼སྣར། པེ།༽ གྲུབ་པས་མ་གྲུབ་
[^57]: ལུང་དུ་ ༼སྣར། པེ།༽ ལུང་
[^58]: འཇུག་པས་ ༼སྣར། པེ།༽ འཇུག་པས་སྟོན་པར་
[^59]: ལོག་རྟོགས་ ༼སྣར། པེ།༽ ལོག་རྟོག་
[^60]: འགའ་ཞིག་ ༼སྣར། པེ།༽ འགའ་ཞིག་གིས་འགའ་ཞིག་
[^61]: སྐད་ ༼སྣར། པེ།༽ སྐད་དང་
[^62]: སྒྲུབ་པར་ ༼སྣར། པེ།༽ བསྒྲུབ་པར་
[^63]: ལུང་བཞི། ༼སྣར། པེ།༽ ལུང་གཞི།
[^64]: དྲུག་པ། ༼སྣར། པེ།༽

[Block 1405]
དྲུག་པ་ལས།
--- END BLOCKS ---
