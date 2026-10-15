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
[Block 1681]
མཚན་མ་གདབ་པ་ཅི་ཞིག་གིས་ཤེ་ན། དེའི་ཕྱིར་བསོད་སྙོམས་ཀྱི་བྲམ་ཟེ་ལ་སོགས་པས་སོ་ཞེས་བྱ་བ༌[^1457]སྨོས་སོ། །

[Block 1682]
ཆོས་བཙོངས་པས་འཚོ་བ་སྦྱར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་མ་མོ་ལས་དེ་དག་ཆོས་ཀྱི་སྒོ་ནས་རྙེད་པ་ཡོངས་སུ་འཚོལ་ཞིང་ཆོས་འཚོང་བས་འཚོ་བ་སྦྱོར་བར༌[^1458]བྱེད་པ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཆོས་ཀྱི་སྒོ་ནས་རྙེད་པ་ཡོངས་སུ་བཙལ་བར་མི་བྱ་ཞིང་ཆོས་འཚོང་བས་འཚོ་བ་སྦྱར་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1683]
འདིར་སིལ་བུ་དག་ལས་དེ་བྱེད་པ་ཞེས་བྱ་བ་དང་པོར་བྱས་ཏེ་བཟའ་བར་བྱའོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པར་གསུངས་པ་ཡིན་ནོ། །

[Block 1684]
གླེང་གཞི་རྣམས་ལས་དེ་སྤང་བ༌[^1459]འདུག་པ་ཞེས་བྱ་བ་དང་པོར་བྱས་ནས་དགེ་སློང་མའི་ཞེས་བྱ་བའི་མཐར་ཐུག་པར་གསུངས་པ་ཡིན་ནོ། །

[Block 1685]
ཆུ་མེད་ན་ཞོ་ག༌[^1460]ཆུ་ལ་སོགས་པའི་ཁུ་བས་རྐང་པ་དག་བཀྲུའོ་ཞེས་བྱ་བ་ནི་འདི་ནི་འོག་ནས་ཟས་རྐང་པས་བརྫི་བར༌[^1461]མི་བྱའོ་ཞེས་འབྱུང་བའི་དམིགས་ཀྱིས་བསལ་བ་ཡིན་ནོ། །

[Block 1686]
རྩྭ་བམ༌[^1462]ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྟན་གཞན་མེད་པའོ། །

[Block 1687]
བླ་གབ་མེད་པའི་མཐའ་གཅིག་ཏུ་གཞག་གོ། །

[Block 1688]
སྤུངས་ཏེ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སོ་སོར་གཞག་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི། སྤུངས་ཏེ་གཞག་ཏུ་ཡང་རུང་བའོ། །

[Block 1689]
མཇུག་ཏུ་འདོར༌[^1463]རོ་ཞེས་བྱ་བ་ནི། བྱ་བ་ཟིན་པའི་མཇུག་ཏུ་རྩྭ་བམ་དོར་བར་བྱའོ། །

[Block 1690]
མང་བ་ཉིད་ཡིན་ན་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མང་བ་ཉིད་ཡིན་ནའོ། །

[Block 1691]
གྲལ་གྱི་ཚར་དུ་མ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། ཚར༌[^1464]དུ་དགེ་སློང་མང་བ་ཉིད་ཡིན་ན། གྲལ་གྱི་ཚར་དུ་མ་ཉིད་ཀྱང་བྱར་རུང་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1692]
ཚད་ཇི་ཙམ་ཞེ་ན། དེའི་ཕྱིར་ལྔ་བརྒྱའི་ཚར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གྲལ་ཚར་གཅིག་ལ་དགེ་སློང་ལྔ་བཀོད༌[^1465]པ་མན་ཆད་ཀྱི་ཚར༌[^1466]རིང་པོ་བྱར་རུང་བའོ། །

[Block 1693]
རྒན་པའི་མཐར་རེ་རེར་སྤྱི་བུངས་བྱའོ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་རྣམས་ལ་བསྐོའོ༌[^1467]ཞེས་འབྱུང་བ་དང་སྦྱར་རོ། །གང་དུ་བསྐོ་བ༌[^1468]ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདྲིམ་པ་དག་རྐུ་བ༌[^1469]ཉིད་ན་སྤྱན་པ་དག་བསྐོའོ༌[^1470]ཞེས༌[^1471]སྨོས་སོ། །

[Block 1694]
ཟས་ཀྱི༌[^1472]ལས་བྱེད་པ་དག་གིས་དང་པོར་བཟའ་བར་བྱའོ། །

[Block 1695]
འདུས་པ་ཆེན་པོའི་ཚེ་རྒན་རིམས་སུ་འཁོད་དུ་གཞུག་པའི་ཕྱིར་དང་། འདྲིམ་དུ་གཞུག་པའི་ཕྱིར་དགེ་སློང་དག་བསྐོའོ། །

[Block 1696]
འདི་ལ་དགེ་སློང་མས་ནི་གཉིས་སམ་གསུམ་གཞག་སྟེ་ཅི་དགར་འཁོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འདུས་པ་ཆེན་པོ་འདི་ལ་དགེ་སློང་མས་ནི་རྒན་པ་གཉིས་སམ་གསུམ་སྤངས་ནས་སོ། །

[Block 1697]
སྒྲ་བསྐྱུངས་ཏེ་ཟན་གྱི་ཆེད་དུ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། མ་མོ་ལས་འདི་དང་པོར༌[^1473]བྱས་ནས་གནས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་མཐར་ཐུག་པ་དང་། དྲན་པ་ཉེ་བར་བཞག་ནས་ཞེས་བྱ་བ་དང་པོར་བྱ་སྟེ། མངོན་པར་བསྡུ་བར་བྱའོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་དང་། མཐར་ལངས་པས་གཤེགས་པར་མི་བྱ་བ་དང་པོར་བྱས་ནས་ལྟོ་བ་དང་བློ་རྣམས་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 1698]
ཁྱིམ་པའི་དྲུང་དུ་འོངས་པ་བོད་པ་ལ་དད་པས་སྦྱིན་པ་ལས་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་འདིས་ཀྱང་ངོ་། །ཟས་རྐང་པས་བརྫི་བར་མི་བྱའོ་ཞེས་བྱ་བ་འདི༌[^1474]སྨན་གྱི་གཞི་ལས་སོ། །

[Block 1699]
བཞོན་པས་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་དང་པོར་བྱས་ནས་བཀག་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་དང་། ངེས་པར་མ་བྱས་པ་ཞེས་བྱ་བ་དེ་ཡང་འདུལ་བ་ལ་ཞེས་བྱ་བ་གང་ཞིག་བཅོམ་ལྡན་འདས་ཀྱིས་ལེགས་པར་འོངས་པ༌[^1475]ལྷུང་བཟེད་ལྷག་པ་གཞག་པ་ཞེས་བྱ་བ་རྣམ་པར་འབྱེད་པ་ལས་ཀློག་པ་དང་། སིལ་བུ་རྣམས་ལས་ནི་དེ་ནས་གཅིག་ཏུ་འདོད་པར་བྱ༌[^1476]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1700]
ཤིན་ཏུ་བསྡམས་པ་དང་སྤྱོད་ལམ་མཛེས་པས་སོ། །

[Block 1701]
མཛེས་པས་སོ་ཞེས་བྱ་བ་ཡང་ཟན་གྱི་ཆེད་དུ་འགྲོ་བར་བྱའོ། །

[Block 1702]
དེ་བཞིན་དུ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་དང་། སྒྲ་བསྐྱུངས་པ་དང་། ཤིན་ཏུ་བསྡམས་པ་དང་། སྤྱོད་ལམ་མཛེས་པས་ཟན་གྱི་ཆེད་དུ་འདུག་པར་བྱའོ། །

[Block 1703]
ཟས་རྐང་པས་བརྫི་བར་མི་བྱའོ། །

[Block 1704]
ལྷུང་བཟེད་ཀྱི་གཞི་ལ་རྐང་པས་རེག་པར་མི་བྱའོ། །

[Block 1705]
དྲན་པ་ཉེ་བར་བཞག་སྟེ་བསོད་སྙོམས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་རྩེ་གཅིག་པའོ། །

[Block 1706]
བྱ་བ་གཞན་དང་འབྲེལ་བའི་བསམ་པ་ཡང་སེམས་གཏོད་པའི་རྩེ་གཅིག་པ་ལས་གཞག་པར་ཡོད་པར་འགྱུར་བ་དེ་བཟློག་པའི་ཕྱིར། སེམས་རྣམ་པར་མ་གཡེངས་པས་བསོད་སྙོམས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1707]
མི་འཕྲོགས་པ་དང་འཚོ་བ་ཙམ་དང་། དེ་མ་འདྲེས་པ་དང༌[^1477]མི་དཀྲུག་པ༌[^1478]དང་། ཤིན་ཏུ་དབེན་པ་དང་དུས་ལས་མི་ཡོལ་བར་བསྒྲུབ་པར་བྱའོ། །

[Block 1708]
གང་ལ་མགྲོན་དུ་བོས་པ་དེ་ལས་གཞན་རྙེད་པ་བདག་གིར་བྱེད་པ༌[^1479]མི་རིགས་པ་ཉིད་མེད་དོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་འདྲེག༌[^1480]མཁན་རབ་ཏུ་བྱུང་བས་དགེ་འདུན་ཐུག་པ་ལ་སྤྱན་དྲངས་ནས་རོ་བསོད་པ་སྟ་གོན་བྱས་པ་དང་། དགེ་སློང་དག་ཟས་གཞན་ལ་མགྲོན་དུ་བོས་པས་དེ་ནི་མི་ལེན་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཟས་གཞན་ལ་མགྲོན་དུ་བོས་པས་གཞན་རྙེད་པ་བདག་གིར་བྱེད་པ་ལ་མི་རིགས་པ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1709]
རང་གིས་ཟས་ལས་གཞན་མནོས་པ་ལས་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་རང་གིས་ཟན་ཟ་བའི་ཚེ་གལ་ཏེ་གཞན་གྱིས༌[^1481]སྦྱིན་པར་བྱེད་ན་དེ་མནོས་པ་ལ་ཉེས་པ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1710]
གཞན་གྱིས༌[^1482]མགྲོན་དུ་བོས་ནས་འདུག་པ་ལ་དེས་གནང་ན། གཞན་གྱིས༌[^1483]བྱིན་པ་ན༌[^1484]དེའི་ཁོངས་སུ་གཏོགས་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་གཞན་གྱིས༌[^1485]མགྲོན་དུ་བོས་ན་ནི་འདུག་པ་ལ་སྦྱིན་བདག་དེས་གནང་ན་སྦྱིན་བདག་གཞན་གྱིས་སྦྱིན་པའོ། །

[Block 1711]
འདི་ལྟ་སྟེ་སྡིག་བྱུང་བའི་གྱད་རྣམས་ཀྱིས་མགྲོན་དུ་བོས་པའི་དགེ་སློང་རྣམས་ལ་གྱད་ཀྱི་སྣ་ཆེན་པོ་ལ༌[^1486]གཏོགས་པ་སྣང་བྱེད་ཀྱིས་བཅའ་བ་དང་བཏུང་བ་དག་བྲིམས་པ་སྦྱིན་བདག་གིས་གནང་བ༌[^1487]དེ་ནི་སྦྱིན་བདག་གཞི་བོའི་ཁོངས་སུ་གཏོགས་པ་དང་འདྲའོ། །

[Block 1712]
དེ་ལ༌[^1488]ནི་དམ་བཅའ་བ་ལས་འདས་པ་དང་ཡང་ཡང་ཟ་བའི་ཉེས་པར་མི་འགྱུར་རོ། །

[Block 1713]
བསམས་པའི་དོན་གྱིས་སྒྲའི་སྦྱོར་བར་རྣམ་པར་གཞག་གི་གྲགས་པས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཚུར་ཤོག་ཅེས་བྱ་བ་ལ་སོགས་པས་འབོད་ཅིང་ཅིའང་རུང་བ་སྦྱིན་པར་བྱེད་པ་ན། སྨྲ་བ་པོའི་བསམས་པའི་དོན་གྱིས་དེ་རྣམ་པར་གཞག་གི༌[^1489]གྲགས་པ་ནི་མ་ཡིན་ཏེ། གལ་ཏེ་དེ་སྐད་དུ་འབོད་པ་དེ་སངས་རྒྱས་ཉིད་དུ་བསམས་པ་ཡིན་ན་ནི་དེ་ཉིད་ལ་དེ་ཕུལ་བར་འགྱུར་རོ། །

[Block 1714]
ཇི་སྟེ་གྲགས་པ་ཉིད་དུ་བསམས་པ་ཡིན་ན་ནི་གྲགས་པ་ཉིད་ལ་ཕུལ་བ་ཡིན་ནོ། །

[Block 1715]
བླངས་བ་སྤང་བར༌[^1490]མི་བྱའོ་ཞེས་བྱ་བ་ལ། བླངས་པ་ནི་བྱིན་ལེན་བྱས་པ་སྟེ་སླར་སྦྱིན་པར་མི་བྱའོ། །

[Block 1716]
འདི་ལྟར་བསོད་སྙོམས་ལ་དེ་སྐད་གསུངས་པ་ཡིན་མོད་ཀྱི་གཞན་ལ་ཡང་དེ་རུང་བར་གནང་བས་དེ་རིགས་པར༌[^1491]བྱའོ། །

[Block 1717]
ལྟ་བ་དང་ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་དག་ལས་བླངས་པ་གཞན་གོ་རིམས་བཞིན་ལ་སྦྱིན་པ་དང་། འཚོ་བར་བྱེད་པ་ལྷག་མ་ཁམ་གཅིག་ཡན་ཆད་ལེན་པ་དང་ཟ་བ་ནི་དད་པས་སྦྱིན་པར་བྱ་བ་ཆུད་གསོན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གོ་རིམས་བཞིན་ལ་ཞེས་བྱ་བ་ནི༌[^1492]ལྟ་བ་ཕུན་སུམ་ཚོགས་པ་ལས་བླངས་པ་ལྟ་བ་ཉམས་པ་ལ་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་ལས་བླངས་པ་ཚུལ་ཁྲིམས་འཆལ་པ་ལ་སྦྱིན་པ་ལ་ནི་དཔེ་ཙམ་དུ་ཟད་དེ། མཆོག་ལས་བླངས་པ་མཆོག་མ་ཡིན་པ་ལ་ཡང་སྦྱིན་པ་ཞེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པར་རེག་པར༌[^1493]བྱའོ། །

[Block 1718]
མཆོག་དང་མཆོག་མ་ཡིན་པ༌[^1494]ནི་འདི་ལྟར་ཤེས་པར་བྱ་སྟེ། ཏིང་ངེ་འཛིན་ཐོབ་པ་ནི་མ་ཐོབ་པ་བས་མཆོག་གོ། །

[Block 1719]
འཕགས་པ་ནི་མ་འཕགས་པ་མ༌[^1495]ཡིན་པས་སོ། །

[Block 1720]
ཆོས་ཀྱི་ཚོགས་རབ་ཏུ་འཕེལ་བའི་བྱང་ཆུབ་སེམས་དཔའི༌[^1496]སོ་སོའི་ཡང༌[^1497]ཉན་ཐོས་ལས་སོ། །
--- END BLOCKS ---
