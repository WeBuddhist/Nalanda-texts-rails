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
འདོད་པ་དང་ལྡན་པ་བཤད་ཟིན་ཏོ། །

[Block 1367]
བསམ་གཏན་ནི། གཉིས་ན༌[^510]བཅུ་གཉིས། ཡིད་མི་བདེ་བའི་ཉེ་བར་རྒྱུ་བ་རྣམས་མ་གཏོགས་སོ། །

[Block 1368]
བཅུ་གཉིས་པོ་དེ་དག་ཀྱང་། འདོད་འགྲོ་རྣམས། འདོད་པའི་ཁམས་ནི་དེ་དག་གི་དམིགས་པའོ། །

[Block 1369]
རང་ལ་དམིགས་བརྒྱད། གཟུགས་ཀྱི་ཁམས་དེ་ཉིད་ནི་དེ་དག་གི་རང་བཞིན་ཡིན་ཏེ། དེ་ནི་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་བརྒྱད་ཀྱི་དམིགས་པ་ཡིན་ཏེ། དྲི་དང་རོ་ལ་ཉེ་བར་རྒྱུ་བ་བཞི་མ་གཏོགས་སོ། །

[Block 1370]
གཟུགས་མེད་པ་གཉིས་ཀྱིའོ། །

[Block 1371]
ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་ངག་གི་དམིགས་པ་ཡིན་ནོ། །

[Block 1372]
བསམ་གཏན་གཉིས་ན་དྲུག །བསམ་གཏན་གསུམ་པ་དང་།

[Block 1373]
བཞི་པ་དག་ན་ན་བཏང་སྙོམས་ཀྱི་ཉེ་བར་རྒྱུ་བ་དྲུག་ཁོ་ན་ཡོད་ཀྱི། གཞན་དག་ནི་མེད་དོ། །

[Block 1374]
དེ་དག །དྲུག་གི་དམིགས་པ་ནི། འདོད་པའོ། །

[Block 1375]
འདོད་པའི་ཁམས་ནི་དྲུག་ཅར་གྱི་ཡང་དམིགས་པ་ཡིན་ནོ། །

[Block 1376]
རང་ནི་བཞིའོ། །

[Block 1377]
གཟུགས་ཀྱི་ཁམས་ནི་བཞིའི་དམིགས་པ་ཡིན་ཏེ། དེ་ན༌[^511]དྲི་དང་རོ་མེད་པའི་ཕྱིར་རོ། །

[Block 1378]
གོང་མ་གཅིག་གི་དམིགས་པ་ཡིན། །གཟུགས་མེད་པའི་ཁམས་ན་ནི་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་གཅིག་ཁོ་ན་དམིགས་པ་ཡིན་ནོ། །

[Block 1379]
གཟུགས་དང་ལྡན་པ་དག་བཤད་ཟིན་ཏོ། །

[Block 1380]
གཟུགས་མེད་ཉེ་བར་བསྡོགས༌[^512]ན་བཞི། །གཟུགས་མེད་པའི་ཉེར་བསྡོགས་ནི། འདིར་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ཀྱི་ཉེར་བསྡོགས་ཡིན་ཏེ། དེ་ན་ནི་གཟུགས་དང་། སྒྲ་དང་། རེག་བྱ་དང་། ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་བཞིའོ། །

[Block 1381]
དེ་དག་ཀྱང་། གཟུགས་འགྲོ། དེ་དག་གི་དམིགས་པ་ནི་བསམ་གཏན་བཞི་པ་ཡིན་ཏེ། གང་དག་གི་ལྟར་ན་དེ་རྣམ་པར་འཆད་པ་ལ་དམིགས་པ་ཡོད་པ་ཡིན་ནོ། །

[Block 1382]
གོང་མར་འགྲོ་བ་གཅིག །དེ་ན་གཟུགས་མེད་པ་ལ་དམིགས་པ་ནི་གཅིག་ཁོ་ན་སྟེ། ཆོས་ལ་ཉེ་བར་རྒྱུ་བའོ། །

[Block 1383]
དངོས་གཞི་ན་གཅིག་གཟུགས་མེད་པའི་དངོས་གཞི་ན་ནི་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་གཅིག་ཁོ་ན་ཡོད་ཀྱི་གཞན་ནི་མེད་དོ། །

[Block 1384]
དེ་ཡང་། རང༌[^513]ཡུལ་ཅན། གཟུགས་མེད་པའི་ཁམས་ཁོ་ན་ལ་དམིགས་པ་ཡིན་ནོ། །

[Block 1385]
དེ་དག་ཀྱང་། བཅོ་བརྒྱད་ཐམས་ཅད་ཟག་དང་བཅས། །དེ་ལྟར་ན་ཚོར་བའི་ཡན་ལག་འདིའི་དབྱེ་བ་ནི་དུ་མ་ཡོད་པར་ཤེས་པར་བྱའོ། །

[Block 1386]
ཡན་ལག་ལྷག་མ་རྣམས་ནི་མི་བརྗོད་དེ། འདི་ལྟར། བཤད་དང་འཆད་པར་འགྱུར་བ་གཞན། །འདིར་ཡན་ལག་ཁ་ཅིག་ནི་བཤད་ཟིན་ལ། ཁ་ཅིག་ནི་འོག་ནས་འཆད་དོ། །

[Block 1387]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་དེ་ཡང་ཉོན་མོངས་པ་དང་ལས་དང་གཞི་རྣམས་སོ་ཞེས་བསྟན་པ།

[Block 1388 [VERSE]]
འདིར་ནི་ཉོན་མོངས་ས་བོན་བཞིན། །
ཀླུ་བཞིན་རྩ་བཞིན་ལྗོན་ཤིང་བཞིན། །
དེ་བཞིན་ཤུན་པ་བཞིན་དུ་འདོད། །

[Block 1389]
དཔེར་ན་ས་བོན་ལས་མྱུ་གུ་དང་སྡོང་བུ་དང་ལོ་མ་ལ་སོགས་པ་སྐྱེ་བར་འགྱུར་བ་དེ་བཞིན་དུ་ཉོན་མོངས་པ་ལས་ཀྱང་ཉོན་མོངས་པ་དང་ལས་དང་གཞི་རྣམས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1390]
དཔེར་ན་ཀླུ་གནས་པའི་མཚོ་ནི་སྐམ་པར་མི་འགྱུར་བ༌[^514]ལྟར། ཉོན་མོངས་པའི་ཀླུ་གནས་པའི་སྐྱེ་བའི༌[^515]མཚོ་ཡང་ངོ་། །དཔེར་ན་ནགས་ཚལ་རྩ་བ་རྣམས་མ་ཕྱུང་བ༌[^516]རྣམས་ནི་བཅད་ཅིང་བཅད་ཀྱང་སླར་སྐྱེ་བར་འགྱུར་བ་ལྟར། ཉོན་མོངས་པ་རྩ་བ་ནས་མ་བཏོན་པའི་འགྲོ་བ་རྣམས་ཀྱང་ངོ་། །དཔེར་ན་ཤིང་ལྗོན་པ་རྣམས་དུས་དུས་སུ་མེ་ཏོག་དང་འབྲས་བུ་རྣམས་སྐྱེད་པར་བྱེད་པ་དེ་བཞིན་དུ་ཉོན་མོངས་པ་རྣམས་ཀྱང་ལན་ཅིག་མ་ཡིན་པར་ཉོན་མོངས་པ་དང་ལས་དང་གཞི་རྣམས་ཀྱི་རྒྱུ་ཡིན་ནོ། །

[Block 1391]
དཔེར་ན་ཤུན་པ་དང་བཅས་པའི་འབྲས་ཐུག་པོ༌[^517]ཆེ་རྣམས་སྐྱེ་བར་ནུས་པ༌[^518]བཞིན་དུ་ཉོན་མོངས་པའི་ཤུན་པ་དང་བཅས་པ་ལ་སྐྱེ་བ་གཞན་དུ་སྐྱེ་བར་ནུས་སོ། །

[Block 1392]
དེ་ལྟར་རེ་ཞིག་ཉོན་མོངས་པ་ས་བོན་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 1393 [VERSE]]
ལས་ནི་ཤུན་བཅས་འབྲས་དང་འདྲ། །
དེ་བཞིན་སྨན་དང་མེ་ཏོག་བཞིན། །

[Block 1394]
ཤུན་པ་ལྟ་བུའི་ཉོན་མོངས་པ་བཤད་ཟིན་ཏོ། །

[Block 1395]
ད་ནི་ཤུན་པ་དང་བཅས་པའི་འབྲས་བུའི་ལས་བརྗོད་པར་བྱའོ། །

[Block 1396]
དཔེར་ན་འབྲུ་དང་སྨན་དག་འབྲས་བུ་སྨིན་ན་མཐར་ཕྱིན་པ་དེ་བཞིན་དུ་ལས་ཀྱང་ངོ་། །དཔེར་ན་མེ་ཏོག་འབྲས་བུ་བསྐྱེད༌[^519]པར་བྱ་བ་ལ་ཉེ་བའི་རྒྱུ་ཡིན་པ་ལྟར་ལས་རྣམས་ཀྱང་རྣམ་པར་སྨིན་པ་བསྐྱེད་པར་བྱ་བ་ལ་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 1397]
གཞི་ནི་བཟའ་བཏུང་གྲུབ་པ་བཞིན། །དཔེར་ན་བཟའ་བཏུང་དུ་གྲུབ་པ་ཡོངས་སུ་ལོངས་སྤྱོད་པར་བྱ་བ་འབའ་ཞིག་ཡིན་གྱིས་ཡང་བསྐྱེད་པར་བྱ་བ་མ་ཡིན་པ་ལྟར་རྣམ་པར་སྨིན་པ་ཞེས་བྱ་བའི་གཞི་ཡང་དེ་བཞིན་ནོ། །

[Block 1398]
ཡང་ཕུང་པོ་སྐྱེ་བའི་རྒྱུན་དེ་སྲེད༌[^520]པ་བཞི་ལས་མི་འདའོ། །

[Block 1399 [VERSE]]
སྲིད་པ་བཞི་པོ་དེ་དག་ལས། །
སྐྱེ་བའི་སྲིད་པ་ཉོན་མོངས་ཅན། །
ཉོན་མོངས་པ་གང་གིས་ཤེ༌[^521]ན།
རང་གི་ས་པའི་ཉོན་མོངས་ཀུན། །

[Block 1400]
ཉོན་མོངས་པ་རྣམས་ཁོ་ནས་ཡིན་གྱི་ཀུན་ནས་དཀྲིས་པ་ཆིག་རྐྱ༌[^522]ཐུབ་པ་རྣམས་ཀྱིས༌[^523]ནི་མ་ཡིན་ནོ། །

[Block 1401]
གཞན་རྣམས༌[^524]གསུམ་མོ། །

[Block 1402]
སྲིད་པ་བར་མ་ལ་སོགས་པ་ནི་དགེ་བ་དང་ཉོན་མོངས་པ་ཅན་དང་ལུང་དུ་མ་བསྟན་པ་རྣམས་སོ། །

[Block 1403]
དེ་ལས་ཀྱང་། གཟུགས་མེད་གསུམ། སྲིད་པ་བར་མ་མ་གཏོགས་སོ། །

[Block 1404]
འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་ན་སྲིད་པ་བཞི་པོ་ཡང་ཡོད་ཅེས་བྱ་བར་སྣང་བར་འགྱུར་རོ། །

[Block 1405 [HEADING]]
#### ཟས་ཀྱིས་གནས་པ། ^3-1-8-0
--- END BLOCKS ---
