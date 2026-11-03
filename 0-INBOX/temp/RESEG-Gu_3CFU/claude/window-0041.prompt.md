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
མིག་ནེའུ་ལེའི་ལྟ་བུ་ཞེས་བྱ་བ་ནི་གང་གི་མིག་ནེའུ་ལེའི་མིག་ལྟ་བུའོ། །

[Block 1437]
མིག་འུག་པའི་ལྟ་བུ་ཞེས་བྱ་བ་ནི་གང་གི་མིག་འུག་པའི་ལྟ་བུའོ། །

[Block 1438]
ཡང་ན་མིག་སེར་སྐྱ་བ་ལ་ཟླུམ་པའི་ཕྱིར་སྲིན་པོའི་མིག་འདྲ་བའོ། །

[Block 1439]
མིག་ཕྱིན་ཅི་ལོག་ཅེས་བྱ་བ་ནི་གང་གི་གྲྭ་ལོགས་ཀྱི་ཟུར་གང་ཡིན་པ་དེ་ནི་སྣ་ལོགས་ལ་འདུག་ལ་སྣ་ལོགས་ཀྱི་ཟུར་གང་ཡིན་པ་དེ་ནི་གྲྭ་ལོགས་ན་འདུག་པའོ། །

[Block 1440]
མིག་བར་འཛིངས་པ་ནི་གང་གི་སྣ་གོང་གཏན་མེད་ལ་མིག་གཡས་གཡོན་འབྲེལ་བའོ། །

[Block 1441]
མིག་རློ་བ༌[^1027]ཞེས་བྱ་བ་ནི་གང་གི་མིག་དྲ་བ་བཞིན་དུ་ཧ་ཅང་འཕྱང་བའི་མིག་གོ། །

[Block 1442]
མིག་གླེའོ༌[^1028]ཞེས་བྱ་བ་ནི་གང་གི་མིག་གི་རྫི་མའི་སྤུ་མེད་པའི་ཕྱིར་རྫི་མ་སྐྱེ་བའི་མཐར་དཔེར་ན་ཁྲག་འཛག་པའི་ཤ་ལྟར་དམར་བའོ། །

[Block 1443]
མིག་ཟླུམ་པོ་ཞེས་བྱ་བ་ནི་གང་གི་མིག་དག་གི་འབྲས་བུ་ཟླུམ་པོ་དེའི༌[^1029]མིག་དག་གོ། །

[Block 1444]
མིག་པོ་ཆེ་དང་འཛེར་ཅན་དང་ཤུ་བ་ཅན་དང་འབྲུམ་ཅན་ཞེས་བྱ་བ་ནི་ཡང་མིག་ཅེས་བྱ་བའི་སྒྲ་སོ་སོར་སྦྱར་ཏེ། མིག་པོ་ཆེ་དང་། མིག་འཛེར༌[^1030]ཅན་དང་། མིག་ཤུ་ཅན་དང་། མིག་འབྲུམ་ཅན་ནོ། །

[Block 1445]
དེ་ལ་མིག་པོ་ཆེ་དང་། ཞེས་བྱ་བ་ནི་གང་གི་མིག་ཧ་ཅང་ཆེ་བའོ། །

[Block 1446]
རྣ་བ་སེར་བ་དང་དཀར་བ་དང་དམར་བ་དང་སྦུབས་ཅན་ཞེས་བྱ་བ་ནི་ཡང་རྣ་བ་ཞེས་བྱ་བའི་སྒྲ་སོ་སོར་སྦྱར་ཏེ། རྣ་བ་སེར་བ་དང་། རྣ་བ་དཀར་བ་དང་། རྣ་བ་དམར་བ་དང་། རྣ་བ་སྦུབས་ཅན་ནོ། །

[Block 1447]
ཁྱི་རྔོ་གཡའ་བ་དང་འཕུངས་པ་དང་། ཆེ་བ་ཞེས་བྱ་བ་ཡང་ཁྱི་རྔོ་གཡའ་བ་དང་། ཁྱི་རྔོ་འཕུངས་པ་དང་། ཁྱི་རྔོ་ཆེ་བའོ། །

[Block 1448]
རླིག་པའི་ནང་དུ་མཚན་ནུབ་པ་དང་ཞེས་བྱ་བ་ནི་གང་གི་རླིག་པ་གཉིས་ཀྱིས་ཕོ་མཚན་གཡོགས་པའོ། །

[Block 1449]
གླེན་པ་དང་ལྕེ་མེད་པ་དང་རྐང་ལག་གཅིག་པ་དང་ཞེས་བྱ་བ་ལ། གླེན་པ་ཞེས་བྱ་བའི་སྒྲ་ནི་བསྙེན་པར་རྫོགས་པར་མི་ཤེས་ཞེས་བྱ་བ་འདི་བསྡུས་པ་ཉིད་དོ། །

[Block 1450]
ལྕེ་མེད་པ་ཞེས་བྱ་བ་ནི་ལྕེ་གཏན་མེད་པའོ། །

[Block 1451]
ལྐུགས་པའི་ཚིག་གིས་ནི་ལྕེ་ཡོད་དུ་ཟིན་ཀྱང་སྨྲ་བར་མི་ནུས་པ་ནི་ལྐུགས་པ་སྟེ། གཞན་ནི་ལྕེ་མེད་པ་ཞེས་བྱ་བ་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 1452]
རྐང་ལག་གཅིག་པ་དང་ཞེས་བྱ་བ་ནི། རྐང་ལག་གི་སྒྲ་དག་གིས་སོ་སོར་འབྲེལ་བ་སྟེ་ལག་པ་གཅིག་པ་དང་། རྐང་པ་གཅིག་པ་དང་ལག་པ་མེད་པ་དང་རྐང་པ་མེད་པ་ཞེས་བྱ་བའོ། །

[Block 1453]
སྐྲ་སྔོ༌[^1031]ཞེས་བྱ་བ་ནི་ཡུང་བའི་ཁ་དོག་ལས་གཞན་པའི་ཁ་དོག་ལ་བྱ་སྟེ། དེ་བས་ན་ཡུང་བའི་ཚིག་གིས་སྔོན་པོ་ལ་བརྗོད་པ་ཉིད་དོ། །

[Block 1454]
མགོ་གླང་པོ་ཆེའི་ལྟ་བུ་དང་། རྟའི་ལྟ་བུ་དང་། ཁྱིའི་ལྟ་བུ་དང་། བ་གླང་གི་ལྟ་བུ་དང་། ལུག་གི་ལྟ་བུ་དང་། རི་དགས་ཀྱི་ལྟ་བུ་དང་། ཉའི་ལྟ་བུ་དང་། སྦྲུལ་གྱི་ལྟ་བུ་དང་། རིང་བ་དང་མང་བ་ཞེས་བྱ་བ་ལ། མགོའི་སྐྲ་ནི་སོ་སོར་སྦྱར་ཏེ། མགོ་གླང་པོ་ཆེའི་ལྟ་བུ་དང་། མགོ་རྟའི་ལྟ་བུ་དང་། མགོ་ཁྱིའི་ལྟ་བུ་དང་། མགོ་བ་གླང༌[^1032]གི་ལྟ་བུ་དང་། མགོ་ལུག་གི་ལྟ་བུ་དང་། མགོ་རི་དགས་ཀྱི་ལྟ་བུ་དང་། མགོ་ཉའི་ལྟ་བུ་དང་། མགོ་སྦྲུལ་གྱི་ལྟ་བུ་དང་། མགོ་རིང་བ་དང་། མགོ་མང་པོ་ཞེས་བྱ་བའོ། །

[Block 1455]
ཐམས་ཅད་སྔོ་བ་དང་། ཐམས་ཅད་སེར་བ་དང་། ཐམས་ཅད་དམར་བ་དང་། ཐམས་ཅད་དཀར་བ་ཞེས་བྱ་བ་ལ་གང་ཞིག་འདི་ཡང་འདོན་པ་དེ་རྣམས་ལ་ཡང་ལུས་ཀྱི་ཁ་དོག་བཞི་རྣམས་ཀྱིས་དེ་ལྟར་བརྗོད་པ་ཉིད་དོ། །

[Block 1456]
མགུལ་ཏ་ལ༌[^1033]ལྟ་བུ་དང་། སྐྲངས་པ་དང་། སྐྲངས་པས་དུབ་པ་དང་། སྤྱོད་ལམ་གྱིས༌[^1034]དུབ་པ་ཞེས་བྱ་བའོ། །

[Block 1457]
རྐུན་པོས་ནི་ཕུང་ཀྲོལ་པའོ་ཞེས་བྱ་བ་ནི་འཕངས་པ་ཉིད་དོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 1458]
སྡིག་པ་ལ༌[^1035]འཇུག་པ་མཉམ་པ་ཉིད་ཀྱི་ཐུན་མོང་གིས་སོ། །

[Block 1459]
འོ་ན་སོ་སོ་ཉིད་དུ་འགྱུར་བར་སྨོས་པ་མ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཕུང་ཀྲོལ་བར་གྱུར་པ་ཡང་རྐུན་པོ་ནི་སྙིང་རྗེ་དང་བཅས་ཤིང་གཞན་ལ་འཕྲོག་པ་ཡིན་ཏེ། ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་གང་གི་ཕྱིར་ཕལ་ཆེར་སྲོག་གཅོད་པ་ལ་འཇུག་པའོ། །

[Block 1460]
ཕུང་ཀྲོལ་བ་ནི་རྐུན་པོ་མ་ཡིན་པར་གྱུར་པ་སྙིང་རྗེ་མེད་པ་གསད་བྱ་གསོད་པར་བྱེད་པ་ལ་སོགས་པ་སྟེ། དེ་བས་ན་འདི་ལ་སོ་སོ་ཉིད་དུའོ། །

[Block 1461]
རྒྱལ་པོ་ཕ་མའི་བསམ་པ་ཅན་ཉིད་ཀྱིས་གནང་བ་ནི་ཕ་མ་དང་འདྲ་བའོ་ཞེས་བྱ་བ་ནི་ཕ་མའི་བསམ་པ་ཅན་ཉིད་ཀྱི༌[^1036]རྒྱལ་པས་གནང་བ་ནི་ཕ་མ་དག་ཉིད་ཀྱིས་གནང་བར་བལྟ་བར་བྱ་སྟེ། རྒྱལ་པོས་གནང་བས་རབ་ཏུ་དབྱུང་བ་ལ་སྐྱོན་མེད་དོ་ཞེས་བྱ་བར་དགོངས་པའོ། །

[Block 1462]
ཡོངས་སུ་འཛིན་པར་བྱེད་པ་གཉིས་ཀྱང་གནང་བ་དང་བསྲེལ་བ་དང་ཞུ་བ་དག་ལ་ཕ་མ་ཉིད་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་སྐྱེད་པར་བྱེད་པ་ཉིད་མེད་པ་ལ་ཡང་ཕ་མས་ཡོངས་སུ་བཟུང་བས་གནས་པ་དག་གིས་གནང་བ་ལ་ཞག་བདུན་བཟུང་བ་དང་། དགེ་འདུན་ལ་ཞུ་བ་བྱེད་པ་ལ་ཕ་མ་ཉིད་ཡིན་གྱི། སྐྱེད་པར་བྱེད་པ་དག་ཁོ་ནས་ཡོངས་སུ་འཛིན་པ་པོ་ཉིད་ཀྱིས་གནས་པ་དག་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1463]
འདིར་གཞུང་ནི། བཙུན་པ་བུ་བཅོས་མ་ཞིག་རེ་ཞིག་བསྙེན་པར་རྫོགས་པར་བགྱིད་ན་སུའི་དྲུང་དུ་བཟོད་པ༌[^1037]གསོལ་བར་བགྱི། བཀའ་སྩལ་པ། བུ་ཉིད་དང་འདྲ་བས༌[^1038]གང་གིས་ཁས་བླངས་པ་དེ་ལའོ། །

[Block 1464]
དེ་བཞིན་དུ་བུ་མོ་བཅོས་མ་ཡང་བུ་མོ་ཉིད་དང་འདྲ་བར་གང་གིས་ཁས་བླངས་པ་དེ་ལའོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 1465]
མི་མ་ཡིན་པའི་འགྲོ་བ་པ་གཉིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཕ་མ་གཉིས་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 1466]
འདིར་གཞུང་ནི། བཙུན་པ་རེ་ཞིག་གང་གི་ཕ་མ་དག་དུས་བྱས་པར་གྱུར་ཏམ། དུད་འགྲོའི་སྐྱེས་གནས༌[^1039]སུ་སོང་བ་ལགས་ན་དེའི་སྐྲ་བྲེག་པའི་ཕྱིར་དགེ་འདུན་ཐམས་ཅད་ལ་ཞུ་བར་བགྱིའམ། ཉེ་བ་འཁོར་འདི་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 1467]
དེ་གཉིས་ལས་མཚམས་མེད་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་ཕ་མ་མིའི་འགྲོ་བ་ནི༌[^1040]མ་ཡིན་པ་སྐྱེད་པར་བྱེད་པ་དག་གིས་ནི་འདི་མཚམས་མེད་པ་མི་སྐྱེད༌[^1041]པའོ། །

[Block 1468]
དེ་ནི་སྐྱེད་པར་བྱེད་པ་གཉིས་ལས་ཏེ་མཚན་གྱུར་པ༌[^1042]གཉིས་ལས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་མ་སྐྱེས་པ་ཉིད་དུ་གྱུར་ཏམ། ཕ་བུད་མེད་ཉིད་དུ་གྱུར་ན་ཡང་མཚམས་མེད་པ་འབྱུང་བར་འགྱུར་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 1469]
མ་བསད་པ་ལ་སོགས་པ་དེ་བྱས་པ་ཉིད་གཙོ་བོར༌[^1043]ཞེས་བྱ་བ་ལ། དེ་བྱས་པ་ཉིད་ནི་མཚམས་མེད་པ་བྱས་པ་ཉིད་དེ་གང་ཞིག་མ་གསོད་པ༌[^1044]ལ་སོགས་པ་རྣམས་ལ་རབ་ཏུ་དབྱུང་བའི་ཕྱིར་བཀག་པ་གང་ཡིན་པ་དེ་བྱས་པ་ཉིད་དེ་མཚམས་མེད་པ་དེ་བྱས་པ་ཉིད་དུ་རྟོགས་པར་བྱའོ། །

[Block 1470]
དེའི་ཕྱིར་མཚམས་མེད་པ་བྱེད་པ་པོ་ནི་རབ་ཏུ་དབྱུང་བར་མི་བྱ་ཞེས་བྱ་བ་ཐམས་ཅད་དུ་ཡིན་ཏེ། མ་བསད་པ་རབ་ཏུ་དབྱུང་བར་མི་བྱའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུའི་གཙོ་བོ་ཅན་དེ་མ་ཡིན་ནོ། །

[Block 1471]
དེ་ལྟར་ན་ཡང་དུད་འགྲོའི་སྐྱེ་གནས་སུ་གཏོགས་པའི་མ་གསོད་པར༌[^1045]བྱེད་པ་ལ་རབ་ཏུ་དབྱུང་བ་བཀག་པར་འགྱུར་རོ། །

[Block 1472]
སྐྱེས་པས་དགེ་སློང་མ་ལ་ཇི་ཞིག་བྱས་ན་དགེ་སློང་མ་སུན་ཕྱུང་བར་འགྱུར་ཞིང་བུད་མེད་ཀྱིས་ཀྱང་དགེ་སློང་ལ་ཇི་ཞིག་བྱས་ན་སུན་ཕྱུང་བར་འགྱུར་ཅིའི་ཕྱིར་དེ་གཉིས་སུ་བསྟན་ཞེ་ན། དེའི་ཕྱིར་ཕམ་པར་གྱུར་པ་མ་བྱུང་བ་ཉིད་ལ་མི་ཚངས་པར་སྤྱོད་པས་ཉམས་སུ་མྱོང་བ་དག་སུན་ཕྱུང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1473]
འདིར་གཞུང་ནི་བཙུན་པ་ཇི་ཙམ་གྱིས་ན་དགེ་སློང་མ་སུན་ཕྱུང་བ་ཞེས་བགྱི། ཉེ་བ་འཁོར་གང་གིས་མི་ཚངས་པར་སྤྱད་པས་དགེ་སློང་མ་སུན་ཕྱུང་བར་གྱུར་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1474]
ཅི་སེམས་གང་ཡང་རུང་བའི་སེམས་དག་ལ་འདི་འབྱུང་བར་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་ཉམས་སུ་མྱོང་བ་དག་ལ་ཞེས་བྱ་བ་སྨོས་ཏེ། བགྲོད་པར་བྱ་བ་ཡང་སུན་ཕྱུང་བར་འགྱུར་ལ་བགྲོད་པ༌[^1046]པོ་ལ་ཡང་སུན་ཕྱུང་བར་འགྱུར་བ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུ་འདིར་གཉིས་པའི་ཚིག་གོ། །

[Block 1475]
བརྗོད་པ་དང་བཅས་པའི་ཟླས་ཉམས་སུ་མྱོང་བས་སུན་ཕྱུང་བ༌[^1047]ཉིད་མི་འགྱུར་བ་ཞེས་བྱ་བ་འདི་ལ་འདིར་ཟླས་ཉམས་སུ་མྱོང་བ་ཡན་ལག་མ་ཡིན་པ་ཉིད་དེ་གང་གི་ཕྱིར་གཞན་གྱི་ཉེས་པས་གཞན་ལ་མི་གོས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
