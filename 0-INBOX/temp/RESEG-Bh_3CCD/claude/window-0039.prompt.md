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
ཇི་སྐད་དུ།

[Block 1367 [VERSE]]
དགེ་སློང་ཉིད་དུ་གང་གནས་པ། །
གང་ཡང་རྟོག་གེ་བ་རྣམས་མི། །
རྒན་པོར་གྱུར་པ་གང་རྣམས་དང་། །
དེ་ལ་དེ་ཉིད་བསྟན་མི༌[^969]བྱ། །

[Block 1368]
ཞེས་གསུངས་སོ། །

[Block 1369]
མདོ་སྡེ་པ་ཞེས་བྱ་བས༌[^970]རྗེས་སུ་དཔག་པས་ཕྱིའི་དོན་འདོད་དེ། ཕྱིའི་དོན་ནི་གཅིག་དང་དུ་མས་མ་གྲུབ་པས་མེད་པས་ཀྱང་རྣམ་པར་ཤེས་པའི་སྐྱེ་བ་གཞན་དུ་ན་མི་འགྱུར་བས་རྗེས་སུ་དཔག་པ་ཡིན་ཏེ། མིག་གི་དབང་པོ་བཞིན་ནོ་ཞེས་རྗེས་སུ་དཔོག་པའི་མདོ་སྡེ་པ་ཕྱིའི་དོན་སྨྲ་བ་རྣམས་ཀྱིས་སྔ་མ་བཞིན་དུ་ཐར་པ་ནི་རྣམ་པར་མ་དག་པས་དེ་དག་ཀྱང་སྔགས་ཀྱི་སྣོད་དུ་རུང་བ་མ་ཡིན་ནོ། །

[Block 1370 [HEADING]]
##### རྣལ་འབྱོར་སྤྱོད་པ། ^1-5-4-3-0

[Block 1371]
རྣལ་འབྱོར་སྤྱོད་པ་བ་ནི་རྣམ་པ་གཉིས་ཏེ། རྣམ་པ་དང་བཅས་པ་སྨྲ་བ་དང་། རྣམ་པ་མེད་པ་སྨྲ་བའོ། །

[Block 1372]
དེ་ལ་དངོས་པོ་ཐམས་ཅད་ཕྱི༌[^971]རོལ་དུ་སོ་སོར་སྣང་བ་རྣམས་རང་གི་རྣམ་པ་ཡིན་ཏེ། རང་གི་རྣམ་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 1373]
གང་དང་གང་རང་སྣང་བའི་དངོས་པོ་དེ་དང་དེ་ཡོད་དེ་བློ་བཞིན་ནོ། །

[Block 1374]
གཞན་གྱི་སྣང་བ་བུམ་པ་ལ་སོགས་པར༌[^972]རང་ཉིད་ཀྱིས་ཡོད་པ་མ་ཡིན་ཏེ། གཞན་གང་ཡིན་པ་དེ་རྣམ་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 1375]
དོན་ནི་གཅིག་དང་དུ་མར་མ་གྲུབ་པས་ཞེས་གྲགས་སོ་ཞེས་སྨྲ་བ་དེའི་གཞུང་ནི་མི་བདེན་ཏེ། གལ་ཏེ་དོན་མེད་ན་གང་ལ་ལྟོས་ནས་རྣམ་པར་ཤེས་པ་འབྱུང་། རྣམ་པར་ཤེས་པས་ན་རྣམ་པར་ཤེས་པའོ། །

[Block 1376]
དེ་བས་ན་རྣམ་པར་རིག་པ་སྨྲ་བ་རང་གི་ཚིག་དང་འགལ་བ་འདི་ཡིན་ཏེ། རྣམ་པར་ཤེས་པ་འདོད་པ་དང་དོན་འགོག་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1377]
གལ་ཏེ་གཟུང་བ་དང་འཛིན་པ་རྣམ་པར་རྟོག་པ་འཁྲུལ་པ་ཡིན་ན་དེའི་ཚེ་རྣམ་པར་རིག་པ་ཡང་འཁྲུལ་པར་འགྱུར་རོ། །

[Block 1378]
དེས༌[^973]ཁས་བླངས་ན་ཡང་དེའི་ཐར་པ༌[^974]མ་དག་པར་འགྱུར་རོ། །

[Block 1379]
ཡང་ན་ཅིའི་ཕྱིར་རྣམ་པར་མ་དག །བདག་ཅག་རྣམས་ཀྱི༌[^975]ནི་མཚན་ཉིད་གསུམ་སྟེ། ཀུན་བརྟགས་དང་། གཞན་དབང་དང་། ཡོངས་སུ་གྲུབ་པའོ། །

[Block 1380]
དེ་ལ་ཀུན་བརྟགས་ནི༌[^976]ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་དུ་རྟོག་པའི༌[^977]མཚན་ཉིད་དེ། གཟུང་བ་དང་འཛིན་པའི་རྣམ་པར་རྟོག་པའོ། །

[Block 1381]
གཞན་དབང་ཞེས་བྱ་བ་ནི་དེའི་རྣམ་པ་སོ་སོར་སྣང་བའི་འཁྲུལ་པའི༌[^978]གཞིའོ། །

[Block 1382]
ཡོངས་སུ་གྲུབ་པ་ཞེས་བྱ་བ་ནི་གཉིས་ཀྱིས་སྟོང་པའི་མཚན་ཉིད་དོ། །

[Block 1383 [VERSE]]
དངོས་པོ་ཤེས་དོན་དེ་ཡི་རྣམས།[^979] །
དེ་མེད་པ་ཉིད་མཁས་པ་ཡིས། །
ཀུན་བརྟགས་ལ་སོགས་མཚན་ཉིད་ནི། །
གོ་རིམས་བཞིན་དུ་ཤེས་པར་བྱ། །

[Block 1384]
ཞེས་འབྱུང་ངོ་། །དེ་ལ་མཚན་ཉིད་གཉིས་མེད་པས་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ནི་སྤྲོས་པའི་དྲི་མ་ཐམས་ཅད་དང་བྲལ་བ། ཆོས་ཀྱི༌[^980]དབྱིངས་ཀྱི་ཡེ་ཤེས་ཞེས་བྱ་བ་རྣམ་པར་དག་པའི་ཐར་པ་ཡིན་ཞེ་ན། དེ་ཡང་བདེན་པ་མ་ཡིན་ཏེ། རྣམ་པར་དག་པ་ཞེས་བྱ་བ་ནི་མདུད་པ་ཐམས་ཅད་དང༌[^981]བྲལ་བའི་སྟོང་པ་ཉིད་དུ་བཤད་ཀྱི། །རྣམ་པར་རིག་པ་ནི་མ་ཡིན་ནོ། །

[Block 1385]
དེའི་དམིགས་པ་ཇི་སྲིད་བློ་ལ་རྒྱུ་བ་དེའི་བར་དུ་རྣམ་པར་མ་དག་པའོ། །

[Block 1386]
ཇི་སྐད་དུ།

[Block 1387 [VERSE]]
འབྱུང་བ་ཆེ་སོགས་རྣམ༌[^982]ཤེས་ལ། །
བསྟན་པ་དེ་དག་འགོག་པར༌[^983]འགྱུར། །
དེ་ནི་ཡེ་ཤེས་ལ་ཐིམ་ཞིང་། །
ངེས་པར་ཕྱིན་ཅི་ལོག་པ་ཡིན། །

[Block 1388]
ཞེས་འབྱུང་ངོ་། །

[Block 1389 [VERSE]]
ཀམ་པ་ལའི་ཞལ་སྔ་ནས་ཀྱིས། །
རེ་ཞིག་ཐམས་ཅད་བརྫུན་ཡིན་ཏེ། །
ཇི་སྲིད་ཇི་སྲིད་རྣམ་པར་རྟོག །
གང་ཞིག་རྟོག་པར་མི་བྱེད་པ། །

[Block 1390]
དེ་ཡི་བདེན་པ་དེ་ཉིད་ཡིན། །ཞེས་གསུངས་སོ། །

[Block 1391 [VERSE]]
རྣམ་རིག་ཙམ་ཉིད་འདི་དག་ཅེས། །
དེ་ལྟར་ཉེ་བར་དམིགས་གྱུར་པ། །
མདུན་དུ་ཅུང་ཟད་འཇོག་བྱེད་ན། །
དེ་ཙམ་ལ་ཡང་གནས་མི་འགྱུར། །

[Block 1392]
ཞེས་ཁྱེད་ཅག་རྣམས་ཀྱི་རང་གི༌[^984]ཚིག་དང་འགལ་བའོ། །

[Block 1393]
འོ་ན་ཇི་ལྟར་འགལ་བ་ཡིན་ཞེས་འདོད་ན། སྨྲས་པ།

[Block 1394 [VERSE]]
གང་ཚེ་ཤེས་པའི་དམིགས་པ་ནི། །
དམིགས་པ་ཉིད་དུ་མི་འགྱུར་ན། །
དེ་ཚེ་རྣམ་རིག་ལ་གནས་ཤིང་། །
གཟུང་བ་མེད་པས་དེ་མི་འཛིན། །

[Block 1395]
ཞེ་ན། དེ་ཡང༌[^985]བདེན་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་དེ་ལྟ་བུས་ཀྱང་སྟོང་པ་ཉིད་ནི་མངོན་པར་རྟོགས་པ་མ་ཡིན་ཏེ། རྣམ་པར་རིག་པར༌[^986]འཇིག་པར་བྱས་པའི་ཕྱིར་དེ་ཡང་སྔོན་དུ་བཀག་ཟིན་ཏོ། །

[Block 1396]
ཇི་སྐད་དུ།

[Block 1397 [VERSE]]
གལ་ཏེ་ཤེས་པ་ཤེས་བྱའི་སྔོན། །
ཅི་ལ་དམིགས་ཏེ་དེ་བྱུང་སྟེ། །
ཤེས་བྱ་ཞིག་པས་ཤེས་འབྱུང་ན། །
ཅི་ལ་དམིགས་ཏེ་དེ་འབྱུང་འགྱུར། །

[Block 1398]
ཞེས་འབྱུང་བས་ཤེས་པ་དང་ཤེས་བྱ་དག་ལ་འབྲེལ་པ་མེད་པས་རྣམ་པར་ཤེས་པའི་སྣང་བ་མེད་དོ། །

[Block 1399]
དེའི་ཕྱིར་དེ་ལྟ་བུའི་ལྟ་བ་ཅན་སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོ་ལ་མི་འཇུག་པས་རྗེས་སུ་གཟུང་བར་བྱའོ་ཞེས་རྣམ་པར་རིག་པ་སྨྲ་བ་པོ་རྣམས་ལ་ལན་ནོ། །

[Block 1400 [HEADING]]
##### དབུ་མ། ^1-5-4-4-0

[Block 1401]
དབུ་མ་པ་ཞེས་བྱ་བས་གཟུང་བ་དང་འཛིན་པའི་རྣམ་པར་རྟོག་པ་དང་བྲལ་བ་འབའ་ཞིག་ཏུ་དྲི་མ་མེད་པའི་མཐའ་ཡས་པ་ནམ་མཁའ་དང་མཚུངས་པ། དངོས་པོ་ཐམས་ཅད་ཀྱི་དེ་ཁོ་ན་ཉིད་ཅེས་བྱ་བ་འདོད་དེ་རྣམ་པར་ཐར་པ་གསུམ་གྱིས་རྟོགས་པར༌[^987]བྱ་བའི་ཕྱིར་རོ། །

[Block 1402]
དེ་བས་ན་དངོས་པོ་ཐམས་ཅད་སྟོང་པ་ཉིད་དེ། གཅིག་དང་དུ་མས་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1403]
དབང་ཕྱུག་ལ་སོགས་པའི་རྒྱུ་མཚན་དང་བྲལ་བ་དངོས་པོ་རྣམས་ཡིན་ཏེ་དབང་ཕྱུག་ལ་སོགས་པ་དཔྱོད་པ་ན༌[^988]མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 1404]
དངོས་པོ་ཐམས་ཅད་སྨོན་པ་མེད་པ་ཡིན་ཏེ། སྨོན་པར་བྱ་བ་མ་གྲུབ་པས་སོ། །

[Block 1405]
འདི་ལ་སྦྱོར་བ་ནི་དངོས་པོ་ཐམས་ཅད་སྟོང་པ་ཡིན་ཏེ་གཅིག་དང་དུ་མས་བྲལ་བའི་ཕྱིར་གཟུགས་བརྙན༌[^989]བཞིན་ནོ། །
--- END BLOCKS ---
