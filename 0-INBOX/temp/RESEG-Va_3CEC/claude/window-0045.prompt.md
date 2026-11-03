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
[Block 1576]
དེ་ཉིད་གང་ཡིན་པ་བསྟན་པའི་ཕྱིར། གང་ཆོས་ཐམས་ཅད་ལ་དོན་དམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། འདུས་བྱས་དང་འདུས་མ་བྱས༌[^1377]ལ་སོགས་པའི་ཆོས་ཐམས་ཅད་འཕྲལ་དུ་སྣང་ཞིང་གྲག་པ༌[^1378]ལྟ་བུ་མ་ཡིན་པར་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱི་སྤྱོད་ཡུལ་ཆོས་ཀྱི་དབྱིངས་ཉིད་དུ་ཤེས་པ་ནི་དོན་སོ་སོ་ཡང་དག་པར་རིག་པར༌[^1379]བྱ་སྟེ། ཚིག་ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 1577]
ཆོས་ཤེས་པ་ནི་འདོད་པའི་ཁམས་ཀྱི་འདུས་བྱས་ཀྱི་དངོས་པོ་རྣམས་ལ་སྡུག་བསྔལ་བ་དང་མི་རྟག་པ་ལ་སོགས་པའི་མཚན་ཉིད་དང་ཆོས་ཉིད་དུ་ཤེས་པའོ། །

[Block 1578]
སོ་སོར་རྟོག་པ༌[^1380]ཤེས་པ་ཞེས་བྱ་བ་ནི་ཁམས་དེ་ཉིད་ཀྱིས༌[^1381]འདུས་བྱས་རྣམས་སྐྱེད་པར་བྱེད་པའི་རྒྱུ་ཀུན་འབྱུང་བ་ལ་རྒྱུ་དང་རྐྱེན་ལ་སོགས་པའི་མཚན་ཉིད་དུ་ཤེས་པའོ། །

[Block 1579]
རྗེས་སུ་འགྲོ་བ་ཤེས་པ་ནི་གཟུགས་ཡོད་པ་དང་གཟུགས་མེད་པའི་འདུས་བྱས་རྣམས་ལ་མི་རྟག་པའི་མཚན་ཉིད་དང་། ཆོས་ཉིད་དུ་ཤེས་པ་སྟེ། འདོད་པའི་ཁམས་ཀྱི་འདུས་བྱས་ཀྱི་ཆོས་ལ་དེ་ལྟར་ཤེས་པའི་འོག་ཏུ་ཕྱིས་ཁམས་གོང་མ་གཉིས་ཀྱིས༌[^1382]འདུས་བྱས་ལ་དེ་ལྟར་ཤེས་པས་རྗེས་སུ་འགྲོ་བ་ཤེས་པ་ཞེས་བྱའོ། །

[Block 1580]
ཡང་ན་སོ་སོར་རྟོག་པ་ཤེས་པ་ནི་ཁམས་གསུམ་གྱི་ཆོས་རྣམས་སྤྱིར་མི་རྟག་པ་ལ་སོགས་པའི་ཆོས་ཉིད་དང་། མཚན་ཉིད་དུ་སོ་སོར་རྟོག་ཅིང་ཤེས་པ་ལ་བྱའོ། །

[Block 1581]
རྒྱུ་ཤེས་པ་ནི་བྱེད་པའི་རྒྱུ་ལ་སོགས་པ་རྒྱུ་དྲུག་རྣམས་ཀྱི་དོན་དང་མཚན་ཉིད་ཤེས་པའོ། །

[Block 1582]
ཚོགས་པ་ཤེས་པ་ནི་རྒྱུ་དང༌[^1383]རྐྱེན་དེ་རྣམས་འདུས་ཤིང་ཚོགས་ན་གདོད་འབྲས་བུ་སྐྱེ་བ༌[^1384]ཤེས་པའོ། །

[Block 1583]
གཉིས་སུ་མེད་པར་ཤེས་པ་ནི་རྟག་ཆད་ལ་སོགས་པའི་མཐའ་གཉིས་དང་བྲལ་བའི་མཚན་ཉིད་ཤེས་པ་འམ། རྒྱུ་དང་རྐྱེན་གཉིས་ཀྱང་དོན་དམ་པ་ནས༌[^1385]ཡོད་པ་མ་ཡིན་པར་ཤེས་པའོ། །

[Block 1584]
ཐ་མར་མི་འགྲོ་བ་ཤེས་པ་ནི་ཐོག་མའི་མཐའ་དང་ཐ་མའི་མཐའ་གཉིས་གང་ནས་ཀྱང་མ་འོངས་གར་ཡང་མི་འགྲོ་བ་ཤེས་པའོ། །

[Block 1585]
ཡང་ན་དང་པོར་རྒྱུ་དང་རྐྱེན་ཚོགས་ནས་འབྲས་བུ་སྐྱེས་ཀྱང་རྒྱུ་འབྲས་བུར་མ་འཕོས་པར་ཤེས་པ་ནི་ཐ་མར་མི་འགྲོ་བ་ཤེས་པའོ། །

[Block 1586]
ཡང་ན་དང་པོར་རྒྱུ་དང་རྐྱེན༌[^1386]བར་དུ་མི་འདུག་པར་ཤེས་པ་ནི་སྐད་ཅིག་མའི་རང་བཞིན་ནམ་དངོས་པོ་མེད་པའི་ཕྱིར་མཐའ་གཉིས་ཀྱི་བར་ན་ཡང་མི་གནས་པར་ཤེས་པའོ། །

[Block 1587]
རྐྱེན་ལ་འཇུག་པ་ཤེས་པ་དེ་ལྟར་མ་འོངས་པ་མི་འགྲོ་བ་མི་གནས་ཀྱང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་པའི་ངོ་བོ་ཙམ་དུ་ཡོད་པར་རྟོག༌[^1387]པའོ། །

[Block 1588]
ཆོས་ཀྱི་དབྱིངས་དབྱེར་མེད་པར་ཤེས་པ་ནི་སོ་སོའི་སྐྱེ་བོའི་དུས་ཀྱི་ཆོས་ཀྱི་དབྱིངས་དང་། འཕགས་པའི་དུས་ཀྱི་ཆོས་ཀྱི་དབྱིངས་ལ་ཐ་དད་མེད་པར་ཤེས་པའོ། །

[Block 1589]
དེ་བཞིན་ཉིད་ཀྱི་རྗེས་སུ་འཇུག་པ་ཤེས་པ་ནི་སྟོང་པ་ཉིད་ཀྱི་ཆོས་ཐམས་ཅད་ལ་ཁྱབ་ཅིང་ཆོས་ཐམས་ཅད་རྗེས་སུ་སོང་པར་ཤེས་པའོ། །

[Block 1590]
ཡང་དག་པའི་མཐའ་ལ་གནས་པ་ཤེས་པ་ནི་ཡང་དག་པའི་མཐའ་ནི་སྟོང་པ་ཉིད་དོ། །

[Block 1591]
དེ་ལ་དམིགས་པའི་འཕགས་པའི་ལམ་ནི༌[^1388]ཡང་དག་པའི་མཐའ་ལ་གནས་པ་སྟེ། ཡང་དག་པའི་མཐའ་ལ་དམིགས་པའི་འཕགས་པའི་ལམ་གྱི་མཚན་ཉིད་ཤེས་པའོ། །

[Block 1592]
སྟོང་པ་ཉིད་རྟོག་པའི་ཤེས་པ་ཞེས་བྱ་བ་ལ་སྟོང་པ་ཉིད་ཡེ་ཤེས་གང་གིས་རྟོག་པར༌[^1389]བྱེད་པའི་ཡེ་ཤེས་དེ་ནི་སྟོང་པ་ཉིད་རྟོག་པའི་ཤེས་པ་སྟེ། སྟོང་པ་ཉིད་ནི་གང་དུ་བཤད་པར་ཟད་དོ། །

[Block 1593]
དེ་རྟོག་པར༌[^1390]བྱེད་པའི་ཡེ་ཤེས་ནི་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་སོ། །

[Block 1594]
མཚན་མ་མེད་པ་ལ་སྤྱོད་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་མཚན་མ་མེད་པའི་ཆོས་ཡེ་ཤེས་གང་གིས་དཔྱད་དེ༌[^1391]ཁོང་དུ་ཆུད་པའི་ཡེ་ཤེས་དེ་ནི་མཚན་མ་མེད་པ་ལ་སྤྱོད་པ༌[^1392]ཤེས་པ་སྟེ། དེ་ཡང་མཚན་མ་ཐམས་ཅད་ལ་རྟོག་པ༌[^1393]མེད་པ་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་སོ། །

[Block 1595]
སྨོན་པ་མེད་པ་ལ་སྨོན་ལམ་མེད་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི། འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་གཉིས་ཀ་ཡང་རང་བཞིན་མེད་པས་རང་བཞིན་མེད་པ་དེ་ལ་སྨོན་པར་བྱར་མེད་པར་ཤེས་པ་ནི་སྨོན་ལམ་མེད་པར་ཤེས་པའོ། །

[Block 1596]
མངོན་པར་འདུ་མི་བྱེད་པ་ནི་འདུ་བྱེད་ཀྱི་མཚན་ཉིད་ཐམས་ཅད་དང་བྲལ་བ་སྟོང་པ་ཉིད་དེ་ནི་རྒྱུ་དང་རྐྱེན་གྱིས་བསྐྱེད་པ༌[^1394]མ་ཡིན་པར་ཤེས་པའོ། །

[Block 1597]
ཚུལ་གཅིག་ལ་འཇུག་པའི་ཤེས་པ་དང་ཞེས་བྱ་བ་ལ་ཆོས་ཐམས་ཅད་མཚན་ཉིད་གཅིག་ཏུ་འཇུག་ཅིང་མཚན་ཉིད་གཅིག་པའི་རང་བཞིན་ཤེས་པའོ། །

[Block 1598]
བདག་མེད་པར་རྟོག་པའི༌[^1395]ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་གང་ཟག་ལ་བདག་མེད་པར་རྟོག་པའི༌[^1396]ཤེས་པ་བསྟན་ཏོ། །

[Block 1599]
གང་ཟག་ལ་བདག་མེད་པར༌[^1397]དོན་དམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་དོན་དམ་པར་ན་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་སོགས་པ་གང་ཟག་གི་དངོས་པོ་མེད་པར་ཤེས་པའོ། །

[Block 1600]
འདས་པའི་དུས་ལ་མ་ཆགས་པའི་ཤེས་པ་ཞེས་བྱ་བ་ནི་ལུས་དང་ལོངས་སྤྱོད་འདས་ཏེ་འགགས་པ༌[^1398]རྣམས་དངོས་པོ་མེད་པར་ཁོང་དུ་ཆུད་པས་དེ་ལ་ཡང་ཕྲད་པར་སྨོན་པ༌[^1399]མི་སྐྱེ་བའམ་འདས་པའི་དངོས་པོ་ཤེས་པར་བྱ་བའི་ཡུལ་རྣམས་ལ་ཐོགས་པ་མེད་པར་ཤེས་པ་ནི་འདས་པའི་དུས་ལ་མ་ཆགས་པའི་ཤེས་པ་ཞེས་བྱའོ། །

[Block 1601]
མ་འོངས་པའི་དུས་ལ་ཐུག་པ་མེད་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་མ་འོངས་པའི་དུས་ཉིད་ལ་མཐའ་ཐུག་ཅིང་ཟད་པ་མེད་པར་ཤེས་པ་འམ། མ་འོངས་པའི་དུས་ཀྱི༌[^1400]དངོས་པོ་ཤེས་པར་བྱ་བ་རྣམས་ལ་ཐོགས་པ་མེད་པར་ཤེས་པའོ། །

[Block 1602]
ད་ལྟར་བྱུང་བའི་དུས་ན་ཐམས་ཅད་དུ་ཁ་ན་མ་ཐོ་བ་མེད་པར་ཤེས་པ་ནི་ད་ལྟར་བྱུང་བའི་དུས་ཀྱི་དངོས་པོ་རྣམས་རང་བཞིན་མེད་པར་ཁོང་དུ་ཆུད་པས་གང་ལ་ཡང་ཁོང་ཁྲོ་བ་དང་ཆགས་པ་མི་སྐྱེ་བའོ། །

[Block 1603]
ཕུང་པོ་རྣམས་ལ་སྒྱུ་མར་ཤེས་པ་ནི་ཇི་ལྟར་སྒྱུ་མ་རྒྱུ་རྐྱེན་གྱིས་སྐྱེད་པས༌[^1401]སྣང་ཡང་རང་བཞིན་མེད་པ་བཞིན་དུ། ཕུང་པོ་ལྔ་རྣམས་ཀྱང་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་སྒྱུ་མ་མཁན་དང་འདྲ་བ་ལ་བག་ཆགས་སྔགས་དང་སྨན་དང་འདྲ་བའི་མཐུ་ལས་སྐྱེས་པ་རང་བཞིན་མེད་པར་ཤེས་པའོ། །

[Block 1604]
ཁམས་རྣམས་ལ་སྦྲུལ་གདུག་པ་ལྟ་བུར་ཤེས་པ་ཞེས་བྱ་བ་ནི། ཇི་ལྟར་སྦྲུལ་གདུག་པས་མྱུར་དུ་གསོད་པར་བྱེད་པ་དེ་བཞིན་དུ་མིག་དང་གཟུགས་ལ་བརྟེན་ཅིང༌[^1402]དམིགས་ནས་མིག་གི༌[^1403]རྣམ་པར་ཤེས་པ་གཟུགས་ལ་ཆགས་པ་དང་ཞེ་སྡང་ལ་སོགས་པ་སྐྱེ་པའི་སྒོ་ནས་དགེ་བའི་རྩ་བ་གསོད་པར་ཤེས་པའོ། །

[Block 1605]
སྐྱེ་མཆེད་རྣམས་ལ་ཡང༌[^1404]སྟོང་པ་ལྟ་བུར་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་གྲོང་སྟོང་པ་ན་སེམས་ཅན་མེད་པ་དེ་བཞིན་དུ་སྐྱེ་མཆེད་རྣམས་ལ་ཡང་བདག༌[^1405]དང་བདག་གིར་མེད་པར་ཤེས་པའོ། །

[Block 1606]
ནང་ཉེ་བར་ཞི་བར་ཤེས་པ་ཞེས་བྱ་བ་ནི་ནང་གི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལ་བདག་དང་བདག་གི་མེད་པར་ཤེས་པའམ། ནང་དུ་ཏིང་ངེ་འཛིན་བྱེད་པས༌[^1406]ན་གཉིད་དང་རྨུགས་པས་སེམས་མི་ནོན་པའི་ཐབས་ཤེས་པའོ། །

[Block 1607]
ཕྱི་རོལ་གྱི་རྒྱུ་བ་མེད་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་གྱི་ཆོས་རྣམས་དངོས་པོ་མེད་པར་ཤེས་པ་འམ། ཕྱི་རོལ་གྱི་ཆོས་རྣམས་ལ་སེམས་འཕྲོ་བར་མི་འགྱུར་བའི་ཐབས་ཤེས་པའོ། །

[Block 1608]
ཡུལ་རྣམས་ལ་སྒྱུ་མ་དང་བྱེ་བྲག་མེད་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྒྱུ་མ་མེད་ཀྱང་འགྲོ་བ་དེའི་རང་བཞིན་ལ་མི་མཁས་པ་རྣམས་ལ་ཉོན་མོངས་པ་སྐྱེ་ཞིང་སླུ་བར་བྱེད་པ་བཞིན་དུ། གཟུགས་ལ་སོགས་པའི་ཡུལ་རྣམས་ཀྱང་དངོས་པོ་མེད་མོད་ཀྱི་བྱིས་པ་དེའི་རང་བཞིན་ལ་མི་མཁས་པ་རྣམས་ལ་ཡོད་པ་འདྲ་བར་སྣང་ཞིང་ཉོན་མོངས་པ་སྐྱེད་པར་བྱེད་པ་ཡིན་པར་ཤེས་པའོ། །

[Block 1609]
དྲན་པ་ལ་གནས་པའི་ཤེས་པ་ནི་མི་བརྗེད་པའི་གཟུངས་ཀྱི་དྲན་པ་བསྟན་ཞིང་མི་ཉམས་པར་བྱ་བའི༌[^1407]ཐབས་ཤེས་པའོ། །

[Block 1610]
བཟོད་པའི་རྗེས་སུ་འགྲོ་བའི་ཤེས་པ་ཞེས་བྱ་བ་ནི་མ་སྐྱེས་པའི་ཆོས་ལ་བཟོད་པ་དང་། སྡུག་བསྔལ་བ་ལ་ཇི་མི་སྙམ་པའི་བཟོད་པ་དང་། རྗེས་སུ་མཐུན་པའི་ཆོས་གང་ཡིན་པ་ཤེས་པའོ། །

[Block 1611]
བློ་གྲོས་ཀྱིས་སོ་སོར་རྟོག་པའི༌[^1408]ཤེས་པ་ནི་ཤེས་རབ་ཀྱི་རང་བཞིན་གྱི་བློས་ཆོས་རྣམས་ལ་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པའོ། །

[Block 1612]
བདག་ལ་རྟོགས་པའི་ཤེས་པ་ནི་བདག་གི་ངོ་བོ་ཉིད་ཇི་ལྟ་བུ༌[^1409]ཡིན་པ་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པའོ། །

[Block 1613]
བདེན་པ་རྣམས་ལ་རབ་ཏུ་རྟོགས་པར༌[^1410]ཤེས་པ་ནི་འཕགས་པའི་བདེན་པ་བཞིའི་མཚན་ཉིད་མ་ནོར་བར་ཤེས་པའོ། །

[Block 1614]
དེ་དག་ཇི་ལྟར་མ་ནོར་བར་ཤེས་ཤེ་ན། དེའི་ཕྱིར་སྡུག་བསྔལ་ལ་མི་འབྱུང་བར་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སྡུག་བསྔལ་གྱི་ཕུང་པོ་ཉིད་ངོ་བོ་མེད་པས༌[^1411]མ་བྱུང་མ་སྐྱེས་པར་ཤེས་པའོ། །

[Block 1615]
ཀུན་འབྱུང་བ་ལ་མངོན་པར་འདུ་མི༌[^1412]བྱེད་པར་ཤེས་པ་ནི་ཀུན་འབྱུང་བའི་ངོ་བོ་ཉིད་མེད་པར་ཤེས་པས་སྡུག་བསྔལ་གྱི་ཕུང་པོ་སྐྱེད་པའི༌[^1413]བྱ་བ་མི་བྱེད་པར་ཤེས་པའོ། །
--- END BLOCKS ---
