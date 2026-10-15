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
[Block 2101]
ཁྱེར་ཏེ་འོངས་པ་ལ་དྲི་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་གྱིས་གང་ཡང་རུང་བ་ཤོ་གམ་དུ་བྱ་བ་མ་ཡིན་པའི་དངོས་པོ་ལ་ཤོ་གམ་གྱི་གནས་ནས་འདའ་བར་བྱེད་པའི་དོན་དུ་ཁྱེར་ཏེ་འོངས་པ་ལ་ཤོ་གམ་གཞལ་དགོས་པའི་རྫས་ཅུང་ཟད་མེད་དམ་ཞེས་བྱ་བ་འདི་དྲི་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2102]
གཞན་གྱིས་དོར་བ་མི་འགྲུབ་ན་རེག་པ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་བ་ནི་གསེར་ལ་སོགས་པ་རེག་པར་བྱ་བ་མ་ཡིན་པ་ལ་གཞན་གྱིས་དེའི་གཏུར་བུ་ལ་སོགས་པའི་ནང་དུ་བཅུག་པ་ལ་རང་གིས་རིག་པར་མ་བྱས་ན་དོར་བ་དབྱུང་བར་མི་འགྲུབ་ན་དེའི་ཚེ་དབྱུང་བའི་ཆེད་དུ་རང་ཉིད་ཀྱིས་རེག་པ་ཉིད་དུ་བྱས་ཏེ་དེ་ལ་ནི་ལྟུང་བར་བྱེད་པ་འགའ་ཞིག་ཏུ་འགྱུར་བ་བག་ཡོངས་སུ་གནང་ངོ་། །མ་ཕུལ་ཡང་ངེས་པ་སྐྱེས་ན་ཕུལ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མ་ལ་སོགས་པ་རྣམས་ལ་བདག་གིས་འདི་སྦྱིན་པ་ཞེས་བྱ་བ་གང་ཞིག་འདི་རྫས་ངེས་པར་བྱས་ནས་བཟུང་བ་མ་ཕུལ་བའི་རྫས་དེ་ལ་ཡང་ཕུལ་བ་ཉིད་ཁོ་ན་ཤེས་པར་བྱའོ། །

[Block 2103]
གང་ལ་ཕུལ་བ་ཡིན་པ་དེས་མ་བཟུང་བ་ཞེས་བྱ་བ་བྱས་ཏེ།[^1461] གང་གིས༌[^1462]དེའི་ལག་པ་ལ་དེ་དང་འབྲེལ་བ་ཉིད་ཤེས་པར་བྱ་བའི་དོན་དང་དེ་དང་འདྲ་བའི་ཤོ་གམ་གྱི་བྱ་བ་འདའ་བར་བྱེད་པ་ལ་གཞན་གྱི་དོན་དུ་རྐུ་བ་ལ་སྐྱོན་ཏེ་དེ་ལྟུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2104]
དེ་དག་གིས༌[^1463]རྫས་གནང་བར་བྱ་བའི་ཕྱིར་ཕ་མའི་བསྔགས་པ་བརྗོད་དོ་ཞེས་བྱ་བ་ལ། ཕ་མ་ཞེས་བྱ་བ་ནི་ཕ་མ་དག་ལའོ། །

[Block 2105]
ཕ་མ་དག་གི་ཆེད་དུ་བཀུར་བའི་རྫས་ནི་ཕ་མ་དག་ལ་བསྔགས་པ་བརྗོད་པར་བྱ་བ་སྟེ། འདིའི་དོན་དུ་ཤོ་གམ་པ་རྣམས་ཀྱི་དྲུང་དུ་འདི་དག་གི་ཡོན་ཏན་བརྗོད་པ་གང་ཡིན་པ་དེ་ནི་བརྗོད་པ་ཙམ་དོན་དུ་གཉེར་བ་ཞེས་བྱ་བ་ཡོངས་སུ་བརྟགས་ནས་སྐྱོན་དང་ལྡན་པ་ཤེས་པར་བྱ༌[^1464]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2106]
དཀོན་མཆོག་རྣམས་ཀྱི་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་དང་ཆོས་དང་། དགེ་འདུན་རྣམས་ལ་དེ་དག་གིས༌[^1465]རྫས་གནང་བར་བྱ་བའི་ཕྱིར་ཡང་དག་པར་བསྔགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2107]
དོན་དུ་གང་ཡང་རུང་བའི་དཀོར་གང་ཡང་རུང་བ་ལས་སྐྱིན་པོར་བླང་བའི༌[^1466]ཆོས་སུ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་ཡང་རུང་བའི་རྫས་ལས་སྐྱིན་པོ་བླང་བའི་ཆོས་ཀྱིས་སངས་རྒྱས་ལ་སོགས་པ་རྣམས་ལ་གང་ཡང་རུང་བའི་དོན་དུ་ཤོ་གམ་གྱི་བྱ་བ་གང་ཡིན་པ་དེའི་དོན་དུ་དཀོན་མཆོག་གཞན་གྱི་དོན་དུ་ཤོ་གམ་སྦྱིན་པ་སྐྱོན་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2108]
སྐྱིན་པོ་བླང་བའི་ཆོས་ཀྱིས་ཞེས་བྱ་བ་དེ་གང་ལས་བཟུང་བ་སླར་སྦྱིན་པ་ཉིད་དོ། །

[Block 2109]
ཅིའི་ཕྱིར་ཞེ་ན་གང་གི་ཆེད་དུ་བཟུང་བ་དེའི་དོན་གྱིས་ཞེས༌[^1467]བྱ་བའི་དོན་ཏོ། །

[Block 2110]
ཤོ་གམ་གཞལ་དགོས་པ་དང་བཅས་པར་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི༌[^1468]འདིར་རྒྱང་གྲགས་ཀྱི་ལམ་དུ་སོང་བ་ལ་བདག་ཉིད་ཅེས་བྱ་བ་འདི༌[^1469]ལས་རྒྱང་གྲགས་འདི་ལ་དངོས་གཞིར༌[^1470]གྱུར་པའི་ཉེས་བྱས་རྒྱང་གྲགས་ཕྱེད་ཕྱེད་ཅིང་དེའི་སྦྱོར་བར་འགྱུར་བའི་ཞེས་བྱ་བ་འདི་རྟོགས་པར་བྱའོ། །

[Block 2111]
འགྲོ་བ་ནི་འདའ་བར་བྱེད་པ་སྟེ། ཤོ་གམ་པ་དང་ལྷན་ཅིག་ཏུ་ཐ་སྙད་ལ་གླགས་ལྟ་བའི་ཕྱིར་བཏགས་པའོ། །

[Block 2112]
མཐུན་པར་བྱེད་པ་དཀའ་བ་མ་ཡིན་པར་འགྱུར་བ་ཡང་ཤོ་གམ་ལ་བརྟེན་པའི་ཐ་སྙད་དེ་དཀའ་བར་གྱུར་པ་ནི་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཏེ། དེ་མ་ཡིན་པ་ཉིད་ལ་ནི་བ་ལང་གི་ལྕི་བ་བཙིར་བས་ཀྱང་ཁ་བསྒྱུར་བ་དང་། ཁ་ཚར་དང་ཕུན་ཚར་བཅད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་དེ་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་ནི་ཤོ་གམ་གཞལ་དགོས་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 2113]
རེ་རེ་ཉིད་ཀྱིས་ཀྱང་འདི་དག་ལ་བཅད་པ་དང་ཁ་བསྒྱུར་བ་དག་ལ་ཤོ་གམ་གཞལ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 2114]
དེ་བས་ན་སོ་སོ་འདི་དག་ལ་ཤོ་གམ་གཞལ་དགོས་པ་མ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2115]
མ་མཐོང་བ་ལ་བློ་དེ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་འདི་ནི་ཁ་བསྒྱུར་བའམ༌[^1471]ཆད་པ་ཞེས་བྱ་བའི་བློ་ལ་མ་མཐོང་བའི་དངོས་པོ་ལ་དེ་མི་མི༌[^1472]འཆགས་སོ། །

[Block 2116]
མཐོང་བ་མེད་པར་འདིར་ལྟུང་བ་དང་རྟོགས་པའི་ངེས་པ་མེད་པའི་ཕྱོགས་པའོ། །

[Block 2117]
དེའི་དབང་གིས༌[^1473]ཤོ་གམ་གཞལ་དགོས་པ་དང་བཅས་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 2118]
མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་མི་ལྡང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2119]
འདིར་གཞུང་ནི་རང་གི༌[^1474]མིག་གིས་བལྟ་བར་བྱའོ། །

[Block 2120]
མ་བལྟས་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2121]
གཞན་གྱི་སྤྱོད་པ་བརྟོལ་བར༌[^1475]མི་བྱའོ་ཞེས་བྱ་བ་ནི། རང་གི་འམ་གཞན་གྱི་ཤོ་གམ་གཞལ་དགོས་པའི་རྫས་རང་ངམ་གཞན་གྱིས༌[^1476]ཤོ་གམ་གྱི་གནས་ནས་འདའ་བར་བྱེད་པ་གང་ཡིན་པ་དེ་དགག་པར་མཛད་པ་ཉིད་ཀྱི་ཕྱིར་གཞན་གྱི་སྤྱོད་པ་བརྟོལ་བར་བྱེད་པ་འདི་ཡང་བཀག་པར་རིག་པར་བྱའོ། །

[Block 2122]
ཡིད་གཅུགས་པ༌[^1477]མ་ཡིན་པ་ལ་གཅུགས་པ༌[^1478]ཉིད་དུ་མི་བྱའོ། །

[Block 2123]
འདི་ལ་གསུམ་ཉིད་དོ། །

[Block 2124]
དེ་ཉིད་ནི་འོག་མ་ལ་གོང་མའོ་ཞེས་བྱ་བ་ལ། དེ་ཉིད་ཅེས་བྱ་བ་ནི་ཡིད་གཅུགས་པ༌[^1479]ཉིད་དོ། །

[Block 2125]
འོག་མ་ལ་ཞེས་བྱ་བ་ནི་ཡིད་གཅུགས༌[^1480]པའོ། །

[Block 2126]
གོང་མའོ་ཞེས་བྱ་བ་ནི་ཡིད་གཅུགས་པ༌[^1481]ཉིད་ལའོ། །

[Block 2127]
ཆུང་ངུ་དང་། འབྲིང་དང་། ཆེན་པོ་ཉིད་ཀྱིས་གོང་མ་དང་། འོག་མ་ཉིད་འདི་ཞེས་བྱ་བའི་རྣམ་པ་འདིས་སྦྱར་བ་ཉིད་ཀྱི་ཕྱིར་རྟོགས་པར་བྱའོ། །

[Block 2128]
ཡིད་གཅུགས་པ༌[^1482]མ་ཡིན་པ་ལ་ཡིད་གཅུགས་པ༌[^1483]ཉིད་དུ་བརྟེན་པར་མི་བྱའོ། །

[Block 2129]
འདི་སྐད་བསྟན་པ་མཛའ་བཤེས་ཐ་མ་ལ་ཡིད་གཅུགས་པ༌[^1484]འབྲིང་དང་ཆེན་པོ་མི་བྱའོ། །

[Block 2130]
འབྲིང་ལ་ནི་ཆེན་པོ་བརྟེན༌[^1485]བཞིན་པ་ཡིད་གཅུགས༌[^1486]པར་མི་བྱ་བ་བརྟེན་པར༌[^1487]འགྱུར་གྱི་ཡིད་གཅུགས༌[^1488]པར་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 2131]
གང་ཞིག་གང་ལ་ཡིད་གཅུགས༌[^1489]ནས་སྣོད་ཡིན་པ་དེ་ནི་དེའི་དོན་ཡིད་གཅུགས༌[^1490]པར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བ་བྱས་ཏེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2132]
སླར་སུ་ཞིག་ལ་ཡིད་གཅུགས༌[^1491]པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དེ་ནི་སྡུག་པ་དང་། ཡིད་དུ་འཐད་པ་དང་། བླ་མ་དང་། བསྒྲུབ་པར་འོས་པ་དང་། མཆོད་པར་འོས་པ་དང་། བསྟོད་པར་འོས་པ་དང་། བླངས་ན་དགའ་བའོ་ཞེས་བྱ་བ་ལ། འདིར་ནི་མཉེས་གཤིན་པ་དང་བཅས་པ་ནི་དགའ་བར་བརྗོད་དོ། །

[Block 2133]
བསྟོད་པར་འོས་པ་ནི་ཡིད་དུ་འོང་བའོ། །

[Block 2134]
བླ་མ་ཞེས་བྱ་བ་ནི་སློབ་དཔོན་དང་མཁན་པོའོ། །

[Block 2135]
རྗེས་སུ་བྱེད་པ་སྒྲུབ་པའི་དོན་དུ་དགེ་བའི་བཤེས་གཉེན་ཉིད་ཀྱིས༌[^1492]གང་ཞིག་ཉེ་བར་བསྟེན༌[^1493]ལ་གནས་པ་དེ་ནི་བསྒྲུབ་པར༌[^1494]འོས་པའོ། །

[Block 2136]
མཆོད་པར་འོས་པ་ཞེས་བྱ་བ་ནི་གང་སྦྱིན་པ་དང་བསྙེན་བཀུར་བ་ལ་སོགས་པའི་མཆོད་པས་གང་ཞིག་ལ་དུས་དུས་སུ་བསྙེན་བཀུར་བར་བྱ་བ་དེ་ནི་མཆོད་པར་བྱ་བའོ། །

[Block 2137]
བསྟོད་པར་འོས་པ་ཞེས་བྱ་བ་ནི་གང་གང་ལ་དུས་དུས་སུ་ཉེ་བར་གནས་ནས་ཚུལ་ཁྲིམས་དང་ཐོས་པ་དང་གཏོང་བ་ལ་སོགས་པའི་ཡིད་བཟུང་བ་ཉིད་ཀྱིས་ཡང་དག་པར་མཐོང་བ་དེ་ནི་བསྟོད་པར་བྱ་བའོ། །

[Block 2138]
བླངས་ན་དགའ་བ་ཞེས་བྱ་བ་ནི་བདག་གིས་བཟུང་བ་ལ་དགའ་བའི་ཕྱིར་གང་དུ་ཡིད་ཆེས་པ་འདི་སྐྱེས་པའོ། །

[Block 2139]
ལག་སྤོད༌[^1495]ཀྱི་ལས་ཀྱིས་ལས་བྱ༌[^1496]ཞིང་བསོད་ནམས་ཀྱི་བློས་ཀྱང་སྟེ་གླ་རྔན་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 2140]
ཡུལ་གྱི་ངེས་པའི་ཚིག་ནི་འདྲིད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཡང་རྣམ་པར་འབྱེད་པ་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་མའི་གནས་སུ་ཁྱོད་ཀྱིས་ཅི་ཞིག་བྱས་ཞེས་བྱ༌[^1497]བ་གང་བརྗོད་པ་ཅིའི་ཐ་ཚིག་ཅེས་སྨྲས་པ་དང་། གསོལ་བ་བཙུན་པ་འཇིག་རྟེན་ན་ལྟུང་ངོ་ཞེས་བྱ་བ་གང་ལགས་པའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
