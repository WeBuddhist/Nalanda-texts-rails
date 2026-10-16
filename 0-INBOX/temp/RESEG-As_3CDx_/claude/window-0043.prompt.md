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
[Block 1506]
བདག་ཏུ་རྟོག་པར་གྱུར་ན་མི་རུང་ཞེས།[^1375] །ཞེས་བྱ་བ་ནི་ས་བོན་ཐམས་ཅད་པ་དེ་ལ་སྟེ། སྔར་གནས་པའི་དངོས་པོར་གྱུར་པ་དེ་ལ་སེམས་ཅན་རྣམས་བདག་ཏུ་སྦྱོར་བར་བྱེད་པའི་ཕྱིར་ཀུན་གཞི་ཞེས་བྱའོ་ཞེས་བསྟན་པ་ན། དེ་ལ་བདག་ཏུ་རྟོག་པར་གྱུར་ན་གཞན་མུ་སྟེགས་ཅན་ཉིད་དུ་གྱུར་པས་མི་རུང་ངོ་ཞེས་བྱ་བར་དགོངས་པ་ཡིན་ནོ། །

[Block 1507]
བྱིས་པ་རྣམས་ལ་ངས་ནི་དེ་མ་བསྟན་ཞེས་བྱ་བ་ནི་གང་བདག་ཏུ་རྟོག་པར་གྱུར་ན་དེ་དག་ནི་བྱིས་པ་དང་འདྲ་བ་ཡིན་པས་བྱིས་པ་རྣམས་ཞེས་བྱ་སྟེ། དེ་དག་ལ་ངས་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་དེའི་ཡོད་པ་ཉིད་དང་། རབ་ཏུ་དབྱེ་བ་དེ་མ་བསྟན་པས་ན་དེའི་ཕྱིར་དེ་ནི་གསང་སྟེ་བསྟན་ཅིང་རྣམ་པར་གཞག་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1508]
དེའི་ཡོད་པ་ཉིད་དང་རབ་ཏུ་དབྱེ་བ་ནི་སྔར་བསྟན་པ་བཞིན་དུ་རིག་པར་བྱ་སྟེ། དེ་ནི་བརྒལ་བའི་ལན་ལ་ཤིན་ཏུ་རྨོངས་པའི་གཉེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 1509]
[^1376]ལེའུ་ལྔ་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1510 [HEADING]]
#### འཕགས་པ་ཡོན་ཏན་འབྱུང་གནས་ཀྱི་ལེའུ། ^4-2-2-0

[Block 1511]
དེ་ལྟར་སེམས་ཀྱི་མཚན་ཉིད་ཀྱིས༌[^1377]ཀུན་རྫོབ་ཀྱི་བདེན་པའི་མཚན་ཉིད༌[^1378]ཡོངས་སུ་ཤེས་པར་བྱ་བ་བསྟན་ནས། ད་ནི་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ཀྱིས༌[^1379]ཀུན་རྫོབ་ཀྱི་བདེན་པའི་མཚན་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བ་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། དེ་ནས་བཅོམ་ལྡན་འདས་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཡོན་ཏན་འབྱུང་གནས་ཀྱིས་ཞུ་བ་ཞུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་འཕགས་པ་ཡོན་ཏན་འབྱུང་གནས་ཀྱི་ལེའུ་དྲུག་པ་འདི་གསུངས་སོ། །

[Block 1512]
[^1380]དེ་ལ་ལེའུ་དྲུག་པ་འདི་བསྡུས་པའི་དོན་ནི་མདོར་བསྡུ་ན་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 1513]
དེ་ཡང་རྣམ་པར་དབྱེ་ན་རྣམ་པ་གཉིས་ཏེ། ཡོངས་སུ་ཞུས་པ་དང་། རྒྱ་ཆེར་བསྟན་པའོ། །

[Block 1514]
དེ་ལ་ཡོངས་སུ་ཞུས་པ་ནི། བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པ་ཞེས་བྱ་བ་ནས། ཇི་ཙམ་གྱིས་འདོགས་ལགས་ཞེས༌[^1381]གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 1515]
དེ་སྐད་ཅེས་གསོལ་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའ་ཡོན་ཏན་འབྱུང་གནས་ལ་འདི་སྐད་ཅེས་བཀའ་སྩལ་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལེའུ་འདི་ཉིད༌[^1382]ཀྱི་གཞུང་ལྷག་མ་ཐམས་ཅད་ཀྱིས་བསྟན་ཏོ། །

[Block 1516 [HEADING]]
##### ཡོངས་སུ་ཞུས་པ། ^4-2-2-1-0

[Block 1517]
དེ་ལ་དང་པོར་ཡོངས་སུ་ཞུས་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། ཡོངས་སུ་ཞུས་པ་ཞེས་བྱ་བའི་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་ཤིན་ཏུ་རྨོངས་པའི་གཉེན་པོར་མཚན་ཉིད་ལ་མཁས་པ་བསྟན་པ་གླེང་བསླང་བའི་ཕྱིར་འདིར་དང་པོར། བཅོམ་ལྡན་འདས་ལ་འཕགས་པ་ཡོན་ཏན་འབྱུང་གནས་ཀྱིས་ཞུ་བ་ཞུས་པ་གང་ཡིན་པའོ། །

[Block 1518]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1519]
དེ་ལ་ཆོས་རྣམས་ཞེས་བྱ་བ་ནི་མཚན་ཉིད་མེད་པའི་ཆོས་དང་། ཀུན་ནས་ཉོན་མོངས་པའི་མཚན་ཉིད་ཀྱི་ཆོས་དང་། རྣམ་པར་བྱང་བའི་མཚན་ཉིད་ཀྱི་ཆོས་ཐམས་ཅད་དོ། །

[Block 1520]
མཚན་ཉིད་ཅེས་བྱ་བ་ནི་མཚན་གཞིའི་ཆོས་དེ་དག་གི་དོན་མཚོན་པར་བྱེད་པ་སྟེ། ཀུན་བརྟགས་པ་དང་། གཞན་གྱི་དབང་དང་། ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་གསུམ་པོ་དེ་དག་ཡིན་ནོ། །

[Block 1521]
མཁས་པ་ཞེས་བྱ་བ་ནི་མཚན་ཉིད་གསུམ་པོ་དེ་དག་ལུང་གི་སྒོ་ནས་སྒྲོ་བཏགས་པ་མེད་པ་དང་། སྐུར་པ་མེད་པར་ཤེས་པའོ། །

[Block 1522]
ལན་གཉིས་སུ་བཟླས་པ་ནི་གྲགས་པའི་དོན་བསྟན་པའི་ཕྱིར་རོ་ཞེས་བགྱི་བ་ནི་མདོ་སྡེ་དེ་དང་དེ་དག་ལས་དེ་སྐད་ཅེས་གསུངས་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1523]
ཇི་ཙམ་གྱིས་ན་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པ་ལགས་ཞེས་བྱ་བ་ནི་ལུང་ཇི་ཙམ་གྱི་སྒོ་ནས་མཁས་ན་མཁས་པ་ལགས་ཞེས་ཞུས་པ་ཡིན་ཏེ། ལུང་ཞེས་བྱ་བས༌[^1383]ནི་མཉན་པའི་རྣམ་པས་ཡོངས་སུ་ཤེས་པའོ། །

[Block 1524]
དེའི་སྒོ་ནས་མཁས་པ་ནི་ཀུན་བརྟགས་པ་ལ་སྒྲོ་འདོགས་པ་དང་། གཞན་གྱི་དབང་དང་། ཡོངས་སུ་གྲུབ་པ་ལ་སྐུར་པ་འདེབས་པ་ཡིན་ནོ། །

[Block 1525]
ཇི་ཙམ་གྱིས༌[^1384]འདོགས་པ་ལགས་ཞེས་བྱ་བ་ནི་རྟོགས་པ་ཇི་ཙམ་གྱི་སྒོ་ནས་མཁས་པར་འདོགས་ལགས་ཞེས་ཞུས་པ་ཡིན་ཏེ། རྟོགས་པ་ཞེས་བྱ་བ་ནི་བསྒོམ་པའི་རྣམ་པ་ཡོངས་སུ་ཤེས་པ་དང་། དེའི་འབྲས་བུ་བྱ་བ་མེད་པའོ། །

[Block 1526]
དེའི་སྒོ་ནས་མཁས་པར་འདོགས་པ་ནི་མཚན་ཉིད་མེད་པའི་ཆོས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་རབ་ཏུ་ཤེས་ནས་ཀུན་ནས་ཉོན་མོངས་པའི་མཚན་ཉིད་ཀྱི་ཆོས་རབ་ཏུ་སྤངས་ནས། རྣམ་པར་བྱང་བའི་མཚན་ཉིད་ཀྱིས་ཆོས་ཐོབ་པར་འགྱུར་བ་དེ་ཙམ་གྱིས་ན་མཁས་པར་འདོགས་པ་ཡིན་ནོ། །

[Block 1527]
ཡོངས་སུ་ཞུས་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1528 [HEADING]]
##### རྒྱ་ཆེར་བསྟན་པ། ^4-2-2-2-0

[Block 1529]
དེའི་འོག་ཏུ་རྒྱ་ཆེར་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། རྒྱ་ཆེར་བསྟན་པ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཡོངས་སུ་ཞུས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པ་རྒྱ་ཆེར་བསྟན་པ་གང་ཡིན་པའོ། །

[Block 1530]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཡོན་ཏན་འབྱུང་གནས་ཁྱོད་དེ་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1531 [HEADING]]
###### ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་གསུམ་མདོར་བསྟན་པ། ^4-2-2-2-1-0

[Block 1532]
དེ་ལ་རྒྱ་ཆེར་བསྟན་པ་འདིས་ནི་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པ་བསྟན་པ་དང་། བཤད་པ་རྣམ་པ་གཉིས་བསྟན་ཏེ། དེ་ལ་བསྟན་པ་ནི་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལུང་དང་རྟོགས་པའི་སྒོ་ནས་མེད་པའི་མཚན་ཉིད་ཀྱང་མེད་པར་ཤེས་པར་བྱ་དགོས་པས།[^1385] མཚན་ཉིད་གསུམ་མདོར་བསྟན་པ་གང་ཡིན་པ་སྟེ། དེའི་ཕྱིར༌[^1386]དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཡོན་ཏན་འབྱུང་གནས་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་གསུམ་པོ་འདི་དག་ཡིན་ཏེ། གསུམ་གང་ཞེ་ན། ཀུན་བརྟགས་པའི་མཚན་ཉིད་དང་། གཞན་གྱི་དབང་གི་མཚན་ཉིད་དང་། ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་དོ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ལ་ཀུན་བརྟགས་པའི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་ཁམས་གསུམ་པའི་སེམས་དང་སེམས་ལས་བྱུང་བའི་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་དུ་རྟོག་པ་གཞན་གྱི་དབང་དང་། ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་དམ། བྱེ་བྲག་ཏུ་ཀུན་བརྟགས་པ་དང་། མིང་དང་བརྡར་བཏགས་པ་དང་། ཐ་སྙད་དུ་བརྗོད་པ༌[^1387]གང་ཡིན་པའོ། །

[Block 1533]
དེ་ནི་ཁམས་གསུམ་པའི་སེམས་དང་སེམས་ལས་བྱུང་བའི་ཡང་དག་པ་མ་ཡིན་པ༌[^1388]ཀུན་དུ་རྟོག་པས་ངོ་བོ་ཉིད་དམ། བྱེ་བྲག་ཏུ་ཀུན་བརྟགས་པ་ཙམ་དུ་ཟད་ཀྱི་གཟུང་བའི་ངོ་བོ་ཉིད་ཀྱང་མ་ཡིན། འཛིན་པའི་ངོ་བོ་ཉིད་ཀྱང་མ་ཡིན་པས་ན་ཀུན་བརྟགས་པའི་མཚན་ཉིད་ཅེས་བྱ་སྟེ། ནམ་མཁའི་མེ་ཏོག་དང་འདྲ་བར་མཚན་ཉིད་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཀྱིས་ངོ་བོ་ཉིད་མེད་པ་ཀུན་རྫོབ་དང༌[^1389]དོན་དམ་པའི་བདེན་པ་གཉི་གར་གཏན་མེད་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1534]
གཞན་གྱི་དབང་གི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་ཕྱི་ནང་གི་དངོས་པོའི་ངོ་བོ་ཉིད་རྐྱེན་གཞན་གྱི་དབང་གིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གང་ཡིན་པའོ། །

[Block 1535]
དེ་ནི༌[^1390]གཟུང་བ་དང་འཛིན་པའི་དངོས་པོའི་ངོ་བོ་ཉིད་རྒྱུ་དང་རྐྱེན་གཞན་གྱི་དབང་གིས༌[^1391]བྱུང་བ་ཡིན་པས་ན་གཞན་གྱི་དབང་གི་མཚན་ཉིད་ཅེས་བྱ་སྟེ། སྒྱུ་མ་བྱས༌[^1392]པ་དང་འདྲ་བར་སྐྱེ་བ་ངོ་བོ་ཉིད་མེད་པ་ཉིད་དང་། དོན་དམ་པའི་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཀྱིས༌[^1393]ངོ་བོ་ཉིད་མེད་པ་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཉིད་དུ་ཡོད་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1536]
ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་གནས་གྱུར་པ་དང་། དངོས་པོའི་དེ་བཞིན་ཉིད་ཀྱིས་རབ་ཏུ་ཕྱེ་བ་ཡང་དག་པའི་ཤེས་པ་དང་། དེ་བཞིན་ཉིད་གང་ཡིན་པའོ། །

[Block 1537]
དེ་ནི་གཞན་གྱི་དབང་གི་མཚན་ཉིད་ལ་ཀུན་བརྟགས་པའི་མཚན་ཉིད་དུ་མངོན་པར་ཞེན་པ་མེད་པ་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་དུ་རྟོག་པ་གནས་གྱུར་པ་ཡང་དག་པའི་ཤེས་པ་དང་། དེའི་ཡུལ་གཞན་གྱི་དབང་གི་དངོས་པོའི་དེ་བཞིན་ཉིད་རྣམ་པར་དག་པའི་དམིགས་པ་ཡོངས་སུ་གྲུབ་པ་ཡིན་པས་ན་ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་ཅེས་བྱ་སྟེ། ནམ་མཁའ་དང་འདྲ་བར་དོན་དམ་པ་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཀྱིས༌[^1394]ངོ་བོ་ཉིད་མེད་ལ་དོན་དམ་པའི་བདེན་པ་ཉིད་དུ་ཡོད་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1538]
དེ་ལྟར་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་གསུམ་མདོར་བསྟན་པ་གང་ཡིན་པ་དེ་ནི་བསྟན་པ་ཡིན་ནོ། །

[Block 1539]
བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1540 [HEADING]]
###### རྒྱས་པར་བཤད་པ། ^4-2-2-2-2-0

[Block 1541]
དེའི་འོག་ཏུ་བཤད་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། བཤད་པ་ཞེས་བྱ་བ་ནི་དེ༌[^1395]ལྟར་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་གསུམ་མདོར་བསྟན་པ་དེ་ཉིད་རྒྱས་པར་བཤད་པ་གང་ཡིན་པའོ། །

[Block 1542]
བཤད་པ་འདི་ཡང་རྣམ་པ་གཉིས་ཏེ། དགོས་པ་དྲུག་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པ་དང་། དེ་དག་གི་དངོས་པོ་བསྡུ་བ་བསྟན་པའོ། །

[Block 1543 [HEADING]]
###### **དགོས་པ་དྲུག་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པ།** ^4-2-2-2-2-1-0

[Block 1544]
དེ་ལ་དགོས་པ་དྲུག་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པ་ནི་གཉེན་པོའི་དགོས་པ་དང་། དཔེའི་དགོས་པ་དང་། མངོན་པར་བསྒྲུབ་པའི་དགོས་པ་དང་། ཐབས་ཀྱི་དགོས་པ་དང་། རྟོགས་པའི་དགོས་པ་དང་། ཕན་ཡོན་གྱི་དགོས་པ་དང་ལྡན་པའོ། །

[Block 1545]
དེ་ལ་གཉེན་པོའི་དགོས་པ་དང་ལྡན་པ་ནི་ཡོན་ཏན་འབྱུང་གནས་དེ་ལ་ཆོས་རྣམས་ཀྱི་ཀུན་བརྟགས་པའི་མཚན་ཉིད་གང་ཞེ་ན་ཞེས་བྱ་བ་ནས། བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཀྱི་བར་དུ་ཡང་དག་པར་བསྒྲུབ་པ་གང་ཡིན་པའོ་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །
--- END BLOCKS ---
