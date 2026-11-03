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
[Block 1471]
གང་དུ་ཅི་ཞིག་བྱས་ན་ལོངས་པ་བཞིར༌[^921]གཏོགས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ༌[^922]ན། དེའི་ཕྱིར་རིན་པོ་ཆེ་རང་གི་མ་ཡིན་པ་དང་། དེར་སྨོས་པ་ལ་རེག་གམ་རེག་ཏུ་བཅུག་ན་བྱེད་པ་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་དུ་ཞེས་བྱ་བའི་དྲི་བ་འདི་ལ་རེག་གམ་རེག་ཏུ་བཅུག་ན་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1472]
ཅི་ཞིག་བྱས་ན་ཞེས་བྱ་བའི་དྲི་བ་འདི་ལ་རིན་པོ་ཆེ་རང་གི་མ་ཡིན་པ་དང་། དེར་སྨོས་པ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1473]
དེར་ཞེས་བྱ་བའི་སྒྲས་ནི་དེར་སྨོས་པ་ལ་རིན་པོ་ཆེར་བཟུང་སྟེ་རིན་པོ་ཆེ་དང་མཉམ་པ་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1474]
དེར་རང་ལ་རང་བཞིན་གྱིས་དངོས་པོ་ཉིད་ཀྱི་ཕྱིར་རང་གི་རིན་པོ་ཆེའི་རང་བཞིན་གྱི་ཆོ་ག་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བའི་ཆོ་ག་འདིར་རང་བཟུང་བ་ཉིད་ཀྱི་ཕྱིར་འདིར་དག་པའི་ལྟུང་བྱེད་ལ་རང་མ་ཡིན་པའི་ཚིག་ཏུ་བྱས་སོ། །

[Block 1475]
དེར་སྨོས་པ་ལ་ཞེས་བྱ་བ་འདི་ལ་རང་མ་ཡིན་པ་ཞེས་བྱ་བ༌[^923]རྟོགས་པར་བྱ་སྟེ། འདིར་གཉིས་ཀ་ཡང་བྱེད་པ་པོར་རིག་པར་བྱའོ། །

[Block 1476]
རང་གི་དང་རང་གི་མ་ཡིན་པ་ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་ནི་ཤིན་ཏུ་རྒྱགས་པའི་གནས་སོ། །

[Block 1477]
གང་གི་ཕྱིར་རང་གི་ཤིན་ཏུ་རྒྱགས་པའི་གནས་ལ་བདག་ཏུ་བྱ་བའི་རིན་པོ་ཆེར་སྨོས་པ་ལ་ཉེས་བྱས་སུ་གཏོགས་པར་རིག་པར་བྱའོ། །

[Block 1478]
རིན་པོ་ཆེར་སྨོས་པ་ཞེས་བྱ་བ་དེ་ཅི་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེ་ནི་གཡུལ་དུ་སྤྱད་པའི་མཚོན་ཆ་དང་རོལ་མོར་སྤྱད་པའི་ལག་ཆའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཡུལ་དུ་དགོས་ཤིང་དེ་འབྲེལ་བའི་མཚོན་ཆ་ནི་གཡུལ་དུ་སྤྱད་པའི་མཚོན་ཆའོ། །

[Block 1479]
དེ་བཞིན་དུ་རོལ་མོར་སྤྱད་པ་ཡང་ངོ་། །དེ་གཉིས་ཇི་ལྟ་བུ་ཞིག་གང་གི་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགོས་པའི་ཕྱིར་རུང་བར་གྱུར་པ་ནི་དངོས་གཞིའོ། །

[Block 1480]
གྱུར་པ་མ་ཡིན་པ་ནི་ཉེས་བྱས་ཀྱིའོ། །

[Block 1481]
གཙུག་ལག་ཁང་དང་ཉེ་འཁོར་ན་འདུག་པ་ལ་བདག་གིར་བྱ་བ་དང༌[^924]མ་འབྲེལ་པར་རྫས་ཆུད་མི་ཟ་བར་བྱ་བའི་སེམས་ཀྱིས་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1482]
དེ་གཉིས་གནས་གང་ལ་ཡང་རུང་བ་ན་འདུག་པ་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་གཙུག་ལག་ཁང་དང་དེའི་ཉེ་འཁོར་ན་འདུག་པ་ནི་མ་གཏོགས་ཏེ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1483]
ཅི་སེམས་གང་ཡང་རུང་བས་འདི་མ་གཏོགས་པར་སེམས་གང་ཡང་རུང་བ་དེ་ལ་འདི་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བདག་གིར་བྱ་བ་དང་མ་འབྲེལ་པར་རྫས་ཆུད་མི་ཟ་བར་བྱ་བའི་སེམས་གང་ལ་ཡོད་པ་དེའི་ཕྱིར་འདིའོ། །

[Block 1484]
གཙུག་ལག་ཁང་དང་དེའི་ཉེ་འཁོར་ན་འདུག་པ་ནི་མ་གཏོགས་ཏེ་ཞེས་བྱ་བ་འདིའི་དོན་ཏོ། །

[Block 1485]
དེ་བསྐྱང་བའི་ཕྱིར་རེག་པ་དང་རེག་ཏུ་བཅུག་པ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་དེ་ཙམ་བཤད་དོ། །

[Block 1486]
དེ་ལ་འདི་ལྟར་ཡོངས་སུ་བསྐྱང་བར་བྱ་ཞེས་བྱ་བ་མ་བསྟན་པས་དེ་རྗོད་པར༌[^925]བྱེད་པ་ནི། དེ་ཡལ་བར་མི་དོར་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་ན་འདུག་པའམ། གཙུག་ལག་ཁང་གི་ཉེ་འཁོར་ན་འདུག་པ་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 1487]
རིན་པོ་ཆེ་འམ་རིན་པོ་ཆེར་སྨོས་པ་དེ་ཡལ་བར་མི་དོར་ཏེ། དེ་བསྲུང་བའི་ཕྱིར་འདོད་པ་དེ་ཐོབ་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1488]
བདག་པོ་ལས་འཁྱམས་པར་གྱུར་ན་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པའོ། །

[Block 1489]
བསྲུང་བའི་དོན་དུ་འདོད་པ་ཐོབ་པར་བྱ་བ་ཇི་ལྟར་དེ་ཡལ་བར་མི་འདོར་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཞག་བདུན་ནམ་བརྒྱད་དུ་བསྡུ་སྐྱོགས་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འགྲོ་བའི་ལམ་གཡོགས་སུ་འམ་ལོ་མའི་ཚོགས་དག་གིས་གཡོགས་པར་བྱའོ། །

[Block 1490]
བདག་པོ་རྟགས་ཐམས་ཅད་ལ་མ་བབ་པར་ཁོ་བོའི་ཡིན་ནོ་ཞེས༌[^926]ཟེར་བ་ལ་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྫས་དེའི་རྟགས་གང་ཡིན་པ་དེའི་ཐོག་ཏུ་ཕེབས་པར་གྱུར་པའི་དོན་གྱིས་མ་ཕེབས་པར་མུན་སྤྲུལ་ཙམ་དུ་ཁོ་བོའི་ཡིན་ནོ་ཞེས་ཟེར་བ་དེ་ལ་གྱ་ཚོམ་དུ་སྦྱིན་པར་མི་བྱའོ། །

[Block 1491]
འོངས་པར་མ་གྱུར་ན་དེའི་འོག་ཏུ་དགེ་འདུན་གྱི་མཛོད་དུ་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་བདག་པོའི་འོ། །

[Block 1492]
དེའི་འོག་ཏུ་ཞེས་བྱ་བ་ནི་ཞག་བདུན་ནམ་བརྒྱད་རྣམས་ལས་སོ། །

[Block 1493]
འདིར་དུས་ཡུན་ཇི་སྲིད་དུ་གཞུག་ཅིང་བཅང་བར༌[^927]ཞེ་ན། དེའི་ཕྱིར་ཟླ་བ་དྲུག་གི་མཐའ་ཚུན་ཆད་དུ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1494]
དུས་དེ་ལ་ཡང་བདག་པོ་མ་འོངས་ན་དེའི་འོག་ཏུ་གང་ཞིག་བྱ་བ་དེ་སྨོས་པ་ནི། དེའི་ཕྱིར་འོག་ཏུ་མ་འོངས་ན་སངས་རྒྱས་སམ་དགེ་འདུན་གྱི༌[^928]རིས་གང་ནས་རྙེད་པ་དེར༌[^929]སྤྱད་དུ་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ས་རིས་གང་ནས་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་སམ་དགེ་འདུན་གྱི༌[^930]ས་རིས་ཀྱི་ཡུལ་གང་གི༌[^931]ནང་ནས་སོ། །

[Block 1495]
དེས་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་སམ་དགེ་འདུན་གྱིས་སོ། །

[Block 1496]
དགོས་པའི་ཕྱིར་རུང་བ་ཉིད་ལ་དངོས་པོ་དེའི་ཚིག་ཏུ་བརྗོད་པ་མ་ཡིན་པ་སྟེ། མི་རུང་བ་ཉིད་ལ་འདིའི༌[^932]བྱ་བ་གང་ཡིན་པ་དེ་བརྗོད་པར་བྱ་སྟེ། དེ་རུང་བ་ཉིད་མ་ཡིན་ན༌[^933]དེས་རུང་བ་བརྟན་པ༌[^934]ཉོ་བར་བྱའོ། །

[Block 1497]
གལ་ཏེ་དེའི་ཚེ་བདག་པོ་འོངས་པར་གྱུར་ན་རྗེས་སུ་གནང་བ་གསོལ་ཏེ། མི་སྟེར་ན་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་དེའི་ཚེ་ཞེས་བྱ་བ་ནི་ཉོས་པ་ཉིད་དང་མ་ཉོས་པར་སྤྱོད་པའི་གནས་སྐབས་སུ་ཡང་དགོས་པར་གྱུར་པ་ཉིད་ནའོ། །

[Block 1498]
མི་སྟེར་ན་ཞེས་བྱ་བ་ནི་རྗེས་སུ་གནང་བའོ། །

[Block 1499]
སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་རྫས་དེའོ། །

[Block 1500]
གལ་ཏེ་སྐྱེད༌[^935]སློང་ན་ཁོ་བོ་ཅག་གིས་ཡོངས་སུ་བསྐྱངས་པ་གང་ཡིན་པ་དེ་ཉིད་དྲིན་ཆེ་བར་མི་སེམས་སམ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། སྐྱེད༌[^936]སློང་ན་ཞེས་བྱ་བ་ནི་དགོད་པའི༌[^937]རྒྱུ་མཚན་གྱི་རྙེད་པའོ། །

[Block 1501]
སྔར་རུང་བ་ཉིད་དུ་གྱུར་པ༌[^938]ཞེས་གང་སྨོས་པ་དེ་ལ་གང་ལ་དགོད་པར་བྱ་བ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བརྗོད་པར་བྱ་སྟེ། ནོར་བུ་ལ་སོགས་པ་ནི་བདར་བ་དང་། ཕུག་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ༌[^939]སྨོས་ཏེ། སོགས་པ་ཞེས་བྱ་བའི་སྒྲས་ནི་མུ་ཏིག་དང་བཻ་ཌཱུརྱ་ལ་སོགས་པ་དག་བསྡུས་པའི་དོན་དུའོ། །

[Block 1502]
འདིར་གཞུང་ཁ་ཅིག་ལས་ནི་དགེ་སློང་གིས་ནོར་བུ་ལེན་ན་ནི་ཉེས་བྱས་སུ་འགྱུར་ལ། བདར་བ་ལེན་པར་བྱེད་ན་ལྟུང་བྱེད་དོ། །

[Block 1503]
ནོར་བུ་ཇི་ལྟ་བ་བཞིན་དུ་མུ་ཏིག་དང་བཻ་ཌཱུརྱ་དང་དུང་དང་མན་ཤེལ་དང་བྱི་རུ་དང་དངུལ་དང་ས་ལེ་སྦྲམ་དང་སྤུག་དང་རྡོའི་སྙིང་པོ་དང་། དམར་པོ་དང་གཡས་སུ་འཁྱིལ་པའི་བར་དུ་ཡང་རུང་ངམ༌[^940]ཞེས་པའོ། །

[Block 1504]
གཞན་ལས་ཀྱང་དགེ་སློང་གིས་ནོར་བུ་ལེན་ན་མ་ཕུག་པ་ལེན་ན་ཉེས་བྱས་སུ་འགྱུར་ལ། ཕུག་པ་ལེན་པར་བྱེད་ན་ནི་ལྟུང་བྱེད་དོ། །

[Block 1505]
ནོར་བུ་ཇི་ལྟ་བ་བཞིན་དུ་མུ་ཏིག་དང་བཻ་ཌཱུརྱ་དང་ཇི་སྲིད་གཡས་སུ་འཁྱིལ་བའི་བར་དུ་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1506]
དེ་གཉིས་ཀ་ལ་ཡང་ཇི་ལྟར་རིགས་པར༌[^941]སྦྱར་བ་ཞེས་བྱ་བས་གཉིས་ཀ་བསྡུས་པ་ཡིན་ནོ། །

[Block 1507]
མགུལ་རྒྱན་དང་གདུ་བུ་རྒྱན་ཅན་དང༌[^942]དཔུང་རྒྱན་དང་དོ་ཤལ་དང་སེ་མོ་དོར་གནས་པ་ཉིད་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ས་ལེ་སྦྲམ་དང་དངུལ་ལས་བྱས་པ་ཉིད་གང་ཞིག་འདིར་དེ༌[^943]ལ་འདི་ལྟ་བུར་འདུག་པའི་ངོ་བོ་མ་ཡིན་པ་ལ་འདི་དག་ལ་དངོས་གཞིའི་བྱེད་པ་པོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུ་བཟུང་བའོ། །

[Block 1508]
པི་ཝང་དང་གླིང་བུ་དང་བ་ལ་རི་དང་མ་ཧཱ་ཏི་དང་སུ་གྷོ་ཥ་ཀ་རྣམས་ནི་རྒྱུད་དང་བཅས་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་ནི་རུང་བར་གྱུར་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་སྟེ་འདིར་ཐམས་ཅད་དུ་སྦྱར་བར་བྱའོ། །

[Block 1509]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་པི་ཝང་ལེན་ན་རྒྱུད་དང་བཅས་པ་ལེན་ན་ལྟུང་བྱེད་དུ་འགྱུར་ལ་རྒྱུད་མེད་པ་ལེན་ན་ལྟུང་བ་ཉེས་པ་ཅན༌[^944]དུ་འགྱུར་རོ། །

[Block 1510]
པི་ཝང་ཇི་ལྟ་བ་བཞིན་དུ་གླིང་བུ་དང་བ་ལ་རི་དང་མ་ཧཱ་ཏི་དང་སུ་གྷོ་ཥ་ཀ་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
