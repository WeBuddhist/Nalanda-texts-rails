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
དེ་ནི་གཟུགས་ལ་གནས་པའོ་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་གནས་ཏེ་སེམས་འཕྲོ་བ་དང་། གཟུགས་བདག་གོ༌[^1005]ཞེས་མངོན་པར་ཞེན་ནས་སྨྲའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1437]
དེ་བཞིན་དུ་དེ་ནི་ཚོར་བ་ལ་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1438]
དེ་བཞིན་དུ་ལྟ་བར་གྱུར་པ་ལས་སེམས་འཕྲོ་བ་ལ་སོགས་པ་ཡང་བསྟན་ནས། ད་ནི་རྣམ་པར་རྟོག་པའི་སྤྲོས་པའི་འཕྲོ་བ་ལ་སོགས་པས་བསྟན་པའི་ཕྱིར་གསུངས་པ། རབ་འབྱོར་གཞན་ཡང་དེ་བཞིན་གཤེགས་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ལ་བརྟེན་ནས༌[^1006]གཟུགས་མཁྱེན་ཏོ། །

[Block 1439 [HEADING]]
###### ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་སྟོན་པ། ^1-2-5-12-4-0

[Block 1440]
གཟུགས་ཇི་ལྟར་མཁྱེན་ཞེ་ན་ཇི་ལྟར་དེ་བཞིན་ཉིད་དུ༌[^1007]འགྱུར་བ་མེད་ཅིང་རྣམ་པར་རྟོག་པ་མེད་ལ། མཚན་མ་མེད་ཅིང་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམ་པ་དྲུག་གིས་ཆོས་ཐམས་ཅད་དེ་བཞིན་ཉིད་དུ༌[^1008]བདག་ཉིད་དུ་མཁྱེན་ཏོ། །

[Block 1441]
དེ་ལ་འགྱུར་བ་མེད་པ་ཞེས་བྱ་བ་ནི་གཞན་མ་ཡིན་པ་དེ་བཞིན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1442]
རྣམ་པར་རྟོག་པ་མེད་ཅེས་བྱ་བ་ནི་མ་ནོར་བ་དེ་བཞིན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1443]
མཚན་མ་མེད་པ་ནི་ཡང་དག་པའི་མཐའི་ཕྱིར་རོ། །

[Block 1444]
ལྷུན་གྱིས་གྲུབ་པ་ནི་གསལ་བར་བྱེད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1445]
སྤྲོས་པ་མེད་པ་ནི་ངོ་བོ་ཉིད་ཀྱིས་དབེན་པའི་ཕྱིར་རོ། །

[Block 1446]
དེ༌[^1009]དམིགས་སུ་མེད་པ་ནི་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1447]
ད་ནི་ཟག་པ་དང་བཅས་པ་དང་། ཟག་པ་མེད་པ་དང་། འཇིག་རྟེན་པ་དང་། འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ཐམས་ཅད་དང་། འཕགས་པའི་གང་ཟག་ཐམས་ཅད་དང་། འཕགས་པའི་ཆོས་ཐམས་ཅད་དང་། དེ་བཞིན་གཤེགས་པ་ཡང་དེ་བཞིན་ཉིད་དུ་ཐ་མི་དད་པའི་ཕྱིར། དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་དུ་ཆོས་ཐམས་ཅད་གཉིས་སུ་མེད་པར་སྟོན་ཏེ།[^1010] རབ་འབྱོར་དེ་ལྟར་ན་སེམས་ཀྱི་གསལ་བ་དང་། བྱིང་བ་དང་། བཀྲམ་པ་དང་། བཙུམས་པའི༌[^1011]དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་ནི་ཕུང་པོ་དང་ཁམས་དང་། སྐྱེ་མཆེད་དང་། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་དེ་བཞིན་ཉིད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 1448 [HEADING]]
###### ཆོས་ཐམས་ཅད་མཚན་ཉིད་མེད་པའི་མཚན་ཉིད་དུ་སྟོན་པ། ^1-2-5-12-5-0

[Block 1449]
ལྷའི་བུ་དག་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་ནི་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་དེ་ཞེས་བྱ་བ་ནི་བྱིས་པའི་སྤྱོད་ཡུལ་དུ་གྱུར་པ་ཀུན་བརྟགས་པའི་ཆོས་རྣམས་དང་། བྲལ་བ་ཉིད་ལ་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད༌[^1012]ཅེས་བྱའོ།[^1013] །རྟོག་པ༌[^1014]དང་རྣམ་པར་རྟོག་པའི་སྤྲོས་པ་ཐམས་ཅད་ཀྱི་མཚན་མ་མེད་ཅིང་ཤིན་ཏུ་ཞི་བའི་ཕྱིར་མཚན་མ་མེད་པའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1450]
རྣམ་པར་རྟོག་པའི་སྨོན་པ་ཐམས་ཅད་ཡོངས་སུ་བཏང་བའི་ཕྱིར་ཕྱིས་སྨོན་པའི་མཚམས་མི་སྦྱོར་བ་ནི་སྨོན་པ་མེད་པའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1451]
རྒྱུ་དང་རྐྱེན་དང་འབྲས་བུར་རྣམ་པར་རྟོག་པའི་སྤྲོས་པ་ཐམས་ཅད་རྒྱུན་ཆད་ཅིང་སྐྱེ་བ་ལ་སོགས་པ་དང་བྲལ་བའི་ཕྱིར་འདུས་མ་བྱས་པའི་གནས་སྐབས་ནི་སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1452]
གྱུར་པ་རྣམ་པ་བཞིས་གནས་གྱུར་ཅིང་ཤིན་ཏུ་ཡོངས་སུ་དག་པ་ཉིད་ལ་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་དང་། རྣམ་པར་བྱང་བ་མེད་པའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1453]
སྒྱུ་མ་དང་རྨི་ལམ་དང་མིག་ཡོར་ལ་སོགས་པ་བཞིན་དུ་ཡོངས་སུ་མ་གྲུབ་ཅིང་དངོས་པོ་མེད་པའི༌[^1015]ངོ་བོ་ཉིད་ཀྱི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1454]
ཡོངས་སུ་རྟོག་པ་དང་རྣམ་པར་རྟོག་པ་ཐམས་ཅད་དང་བྲལ་ཞིང་དོན་དམ་པར༌[^1016]བརྗོད་དུ་མེད་པས་ནམ་མཁའ་བཞིན་དུ་གང་དུ་ཡང་གནས་པ་མེད་པ་ལ་མི་གནས་པའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1455]
སྔོན་གྱི་མཐའ་དང་ཕྱི་མའི་མཐའ་དང་། དབུས་ཀྱི་མཐའ་རྣམ་པར་སྤངས་པའི་ཕྱིར་ཡོད་པ་དང་མེད་པའི་དངོས་པོ་དང་བྲལ་བ་རང་བཞིན་གྱིས་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་ཉིད་ལ་ཆད་པ་མེད་པ་དང་། རྣམ་པར་རྟག༌[^1017]པ་མེད་པའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1456]
ཐ་དད་པའི་རྣམ་པར་རྟོག་པ་ཐམས་ཅད་སྤངས་པས་གཉིས་སུ་མེད་པ་ཐ་དད་པ་དང་གཅིག་པ་དང་བྲལ་བ་ཉིད་ནི་དོན་གཅིག་པ་མ་ཡིན་པ་དང་། དོན་ཐ་དད་པ་མ་ཡིན་པའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1457]
རྩོལ་བ་ཐམས་ཅད་སྤངས་པས་གསལ་བར་བྱེད་པ་མེད་པ༌[^1018]ལ་བྱེད་པ་མེད་པའི་ཕྱིར། འགྲོ་བ་དང་འོང་བ་དང་བྲལ་བ་ཉིད་ནི་འོང་བ་མེད་པ་དང་འགྲོ་བ་མེད་པའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1458]
རྣམ་པ་ཐམས་ཅད་དུ་ཐམས་ཅད་རང་གི་མཚན་ཉིད་ཐམས་ཅད་དང་བྲལ་བས་མཚན་ཉིད་མེད་པའི་བདག་ཉིད་དུ་གནས་པ་ནི་ནམ་མཁའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1459]
དེ་ཡང་དེ་བཞིན་གཤེགས་པས་འཇིག་རྟེན་གྱི་བརྡར་བཀའ་སྩལ་ཏེ་དོན་དམ་པར་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བརྗོད་དུ་མེད་པའི་མཚན་ཉིད་དུ་གསུངས་པའོ། །

[Block 1460]
ལྷའི་བུ་དག་མཚན་ཉིད་དེ་དག་ནི་ལྷ་དང་མི་དང་ལྷ་མ་ཡིན་དུ་བཅས་པའི་འཇིག་རྟེན་གྱིས་གཞན་དུ་བྱ་བར་མི་ནུས་སོ་ཞེས་བྱ་བ་ནི་མི་འགྱུར་བར་ཡོངས་སུ་གྲུབ་པ་དང་། ཕྱིན་ཅི་མ་ལོག་པར་ཡོངས་སུ་གྲུབ་པས༌[^1019]ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་དུ་གསུངས་པའོ།[^1020] །ལྷའི་བུ་དག་མཚན་ཉིད་ནི་མཚན་ཉིད་གཞན་དུ་མི་བྱེད་དོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ཀྱིས་དེ་བཞིན་ཉིད་རྣམ་པར་འཁྲུག་པར་མི་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1461]
མཚན་ཉིད་ནི་མཚན་ཉིད་མི་ཤེས་སོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ཀྱིས་དེ་བཞིན་ཉིད་མི་ཤེས་ཏེ་ཇི་ལྟར་ནམ་མཁས་ནམ་མཁའ་མི་ཤེས་པ་བཞིན་ནོ། །

[Block 1462]
མཚན་ཉིད་ནི་མཚན་ཉིད་མེད་པ་མི་ཤེས་སོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ཀྱིས་ཀུན་བརྟགས་པ་མི་ཤེས་ཏེ། ཇི་ལྟར་ནམ་མཁའ༌[^1021]རི་བོང་གི་རྭ་མི་ཤེས་པ་བཞིན་ནོ། །

[Block 1463]
མཚན་ཉིད་མེད་པ་ནི་མཚན་ཉིད་མི་ཤེས་སོ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པས་དེ་བཞིན་ཉིད་མི་ཤེས་ཏེ། ཇི་ལྟར་རི་བོང་གི་རྭས་ནམ་མཁའ་མི་ཤེས་པ་བཞིན་ནོ། །

[Block 1464]
མཚན་ཉིད་མེད་པས་མཚན་ཉིད༌[^1022]མི་ཤེས་སོ་ཞེས་བྱ་བ་ཀུན་བརྟགས་པས་ཀུན་བརྟགས་པ་མི་ཤེས་ཏེ། ཇི་ལྟར་རི་བོང་གི༌[^1023]རྭས་རི་བོང་གི་རྭ་མི་ཤེས་པ་བཞིན་ནོ། །

[Block 1465]
མཚན་ཉིད་གང་ཡིན་པ་དང་མཚན་ཉིད་མེད་པ་གང་ཡིན་པ༌[^1024]གཉིས་ཀ་ལ་ཡང་གང་གིས་ཤེས་པར་བྱེད་པའི་ངོ་བོ་ཉིད་མེད་དོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་རྣམ་པར་མི་རྟོག་པ་དང་ལྷུན་གྱིས་གྲུབ་པ་ཉིད་དང་སྤྱོད་པ་མེད་པའི་ཕྱིར་རབ་ཏུ་ཤེས་པའི་ངོ་བོ་ཉིད་མེད་དེ་ཀུན་བརྟགས་པ་རྣམས་མེད་པའི་ཕྱིར་རོ། །

[Block 1466]
གང་གིས་ཤེས་པར་བྱེད་ཅེས་བྱ་བ་ནི་ཤེས་པ་ལ་སོགས་པས་སོ། །

[Block 1467]
གང་ཤེས་པར་བྱེད་ཅེས་བྱ་བ་ནི་གང་ཟག་གམ་ཆོས་སོ། །

[Block 1468]
གང་ལ་ཤེས་པར་བྱེད་ཅེས་བྱ་བ་ནི་གང་ཟག་གམ་ཆོས་གཞན་ལའོ། །

[Block 1469]
ལྷའི་བུ་དག་མཚན་ཉིད་འདི་དག་ནི་གཟུགས་ཀྱིས་མངོན་པར་འདུས་བྱས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་མངོན་པར་འདུ་བྱེད་པ་མེད་པའི་མཚན་ཉིད་སྟོན་ཏོ། །

[Block 1470]
མཚན་ཉིད་ཐམས་ཅད་ནི་མཚན་ཉིད་མེད་པའི་ཕྱིར༌[^1025]ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་དང་། མཚན་མ་མེད་པ་ལ་སོགས་པ་སྔར་སྨོས་པ་རྣམས་དང་། འདུས་བྱས་དང་། འདུས་མ་བྱས་པ་ཐམས་ཅད་དང་ཀུན་བརྟགས་པའི་མཚན་ཉིད་ཀྱིས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1471]
དེ་བཞིན་གཤེགས་པ་རྣམས་བྱུང་ཡང་རུང་མ་བྱུང་ཡང་རུང་ཞེས་བྱ་བ་ལ་སོགས་པས་ཆོས་གནས་པའི་མཚན་ཉིད་གསུངས་པའོ། །

[Block 1472]
མཚན་ཉིད་ཀྱི་དབྱིངས་ནི་མཚན་ཉིད༌[^1026]མེད་པའི་དབྱིངས་ཇི་ལྟ་བ་བཞིན་དུ་གནས་པ་ཉིད་དེ། [^1027]དེ་ནི་དེ་བཞིན་གཤེགས་པས་ཡང་དག་པར་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཞེས་བྱ་བ་ནི་མཚན་ཉིད་ཀྱི་རྣམ་པར་རྟོག་པ་ཐམས་ཅད་མེད་པའི་ཕྱིར་མཚན་ཉིད་མེད་པའི་དབྱིངས་ཞེས་བྱའོ། །

[Block 1473]
དེའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་དེ་བཞིན་གཤེགས་པ༌[^1028]ཞེས་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་དུ་ཐུགས་སུ་ཆུད་པའམ། དེ་བཞིན་ཉིད་ཐུགས་སུ་ཆུད་པ་ལ་ངེས་པའི་ཚིག་གིས་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱའོ། །

[Block 1474]
དེ་བཞིན་གཤེགས་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་དག་པར་རབ་ཏུ་བསྟན་པས་མཚན་ཉིད་ཐམས་ཅད་ཡང་དག་པར་རབ་ཏུ་མཁྱེན་ཞེས༌[^1029]བྱ་བ་ནི། ལྷའི་བུ་དག་སྟོང་པ་ཉིད་ཀྱང༌[^1030]མཚན་ཉིད་དང་མཚན་མ་མེད་པའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར། འདི་ནི་ཟབ་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྔར་སྨོས་པ་སྟོན་ཏོ། །

[Block 1475]
བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་ཀྱང་མཚན་ཉིད་ཐམས་ཅད་རབ་ཏུ་དབྱེ་བ་མཛད་དེ་ཞེས་བྱ་བ་ནི་དོན་དམ་པ་རྣམ་པར་མི་རྟོག་པ་དེ་ལྟ་བུ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་ཀྱང་སེམས་ཅན་རྣམས་ལ་ཕན་གདགས་པའི་ཕྱིར་ཀུན་རྫོབ་ཀྱི་མཚན་ཉིད་རྣམས་བཤད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
