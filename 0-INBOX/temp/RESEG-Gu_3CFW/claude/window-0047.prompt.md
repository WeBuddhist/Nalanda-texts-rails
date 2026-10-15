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
[Block 1646]
འདིར་གཞུང་ནི། བཅོམ་ལྡན་འདས་ལ་འཕྲོག་མ་སྐྱབས་སུ་སོང་ཞིང་བསླབ་པའི་གཞི་དག་ལ་བཞག་ནས། དེས་བུ་དེ་དག་གནོད་སྦྱིན་གདུག༌[^1432]པས་འཇིགས་པ་བསྲུང་བའི་ཕྱིར་དགེ་འདུན་ལ་ཕུལ་བ་ཐོས་ནས། དེ་དག་འདི་སྙམ་དུ་དེས་བསྲུང་བའི་ཕྱིར་དགེ་སློང་རྣམས་ལ་བུ་རེ་ཞིག་འབུལ་བར་བྱེད་ན་བདག་ཅག་གིས་ཀྱང་ཅིའི་ཕྱིར་མི་དབུལ་སྙམ་ནས། དེ་དག་གིས་བུ་དབུལ་བར་བརྩམས་པ་དང་། དགེ་སློང་དག་མི་ལེན་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བླང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1647]
འདིར་ཚུལ་ནི་རྗེས་སུ་འགྲོ་བ་ནི་དགེ་འདུན་གྱིས་བླངས་ཏེ། ཀུན་དགའ་ར་བའི་གཡོག་ཏུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1648]
དེ་ལྟ་བས་ན་བྱེ་བྲག་མེད་པར་བརྟེན་པ་ཡིན་ནོ། །

[Block 1649]
དེ་དག་གི་ཆ་ལུགས་ནི་མགུལ་པར་ཆོས་གོས་བཏགས་པ་ཉིད་དོ། །

[Block 1650]
སྐྱེད་པར༌[^1433]ཡང་རུང་ངོ་ཞེས་བྱ་བ་ལ། དེ་དག་གི་ཆ་ལུགས་ནི་མགུལ་པར་ཆོས་གོས་ཀྱི་ཚལ་བུ་རེ་རེ་བཏགས་པ་ཡིན་ནོ། །

[Block 1651]
ཕན་གདགས་པའི་སེམས་ཀྱིས་སོ་སོར་བསྐྱང་བར་བྱའོ། །

[Block 1652]
དེའི་ཉེ་དུས་ཕུལ་བ་བླང་བར་བྱའོ། །

[Block 1653]
མཇུག་ཏུ་རིན་ཉིད་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། དེའི་ཉེ་དུ་དག་གིས༌[^1434]མཇུག་ཏུ་བྱིས་པ་ཕྱིར་ལེན་པའི་ཚེ་དེའི་དུས་ཕུལ་བ་བླང་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1654]
དེ་ལྟར་ཡང་དེ་རྣམས་ཀྱིས་ཕུལ་བར་གྱུར་པ་ལ་དད་པའི་དབང་དུ་བྱས་པ་ཉིད་ཡིན་པས་འདི་ལ་ལོག་པས་འཚོ་བ་ཉིད་ཡིན་པར་དོགས་པར་མི་བྱ་སྟེ། དེ་བས་ན་དེ༌[^1435]ལ་འདི་བསྟན་པའོ། །

[Block 1655]
དེ་དག་གིས་བྱས་པ་ཤེས་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། བྱིས་པ་དེ་དག་གིས་བྱས་པ་ཤེས་པས་ཕུལ་བ་ཡང་བླང་བར་བྱའོ། །

[Block 1656]
དེའི་རིན་གདབ་པར༌[^1436]མི་བྱའོ་ཞེས་བྱ་བ་ནི། དགེ་སློང་གིས་བྱིས་པ་དེ་དག་ཡོངས་སུ་བསྐྱངས་པའི་རིན་དང་རྔན་པ་བླང་བར་མི་བྱའོ། །

[Block 1657]
ཤིང་ཐོག༌[^1437]གི་རྙེད་པ་བདག་གིར་བྱའོ་ཞེས་བྱ་བ་ལ། [^1438]འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས་ཏེ།

[Block 1658]
འོག་མ་གསུམ་གྱིས་ཡང་ངོ་། །འདིར་སིལ་བུ་དག་ལས།

[Block 1659]
བཟའ་བར་བྱ་བ་ཉིད་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 1660]
ཞུན་མར་དང་འབྲུ་མར་དང་སྦྲང་རྩི་དང་བུ་རམ་གྱི་ལྦུ༌[^1439]བའི་བུམ་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ཞུན་མར་ལ་སོགས་པས་གང་བའི་བུམ་པ་ནི་བླང་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1661]
འདིར་གཞུང་ནི། ཞུན་མར་དང་འབྲུ་མར་དང་སྦྲང་རྩི་དང་བུ་རམ་གྱི། ལྦུ༌[^1440]བའི་བུམ་པ་དགེ་འདུན་ལ་ཕུལ་ན་བུམ་པའི་ཚད་ཙམ་པོ་དེ་རྣམས་ཞེས་བྱ་བ་ནས། ཇི་སྲིད་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བླང་བར་བྱ་ཞིང་བླངས་པས་དགེ་སློང་དག་གམ་ཁྱིམ་བདག་གིས་བྲིམ་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1662]
དགེ་འདུན་དུ་གཏོགས་པའི་ཚིག་ནི་འདི་ཡིན་ཏེ། འདིར་དགེ་འདུན་ནམ་གང་ཟག་གིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་རྣམ་པར་དཔྱད་པ་ལ་མ་བྱས་ཏེ། འདི་ནི་གང་ཟག་ལ་མི་རིགས་པའི་ངོ་བོ་མ་མཐོང་ངོ་། །དེ་བས་ན་སྐབས་ཀྱི་དབང་གིས་ཚིག་འདིར་བླངས་སོ་སྙམ་དུ་རྣམ་པར་ངེས་ནས་བྱེ་བྲག་ཏུ་མ་སྨོས་སོ། །

[Block 1663]
དེ་དག་གི་སྣོད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། ཞུན་མར་ལ་སོགས་པ་དེ་དག་གི་སྣོད་དེ་བུམ་པ་ནི་བུམ་པའོ། །

[Block 1664]
དེ་དག་གཞག༌[^1441]པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཞུན་མར་ལ་སོགས་པའི་སྣོད་བུམ་པ་དག་གོ། །

[Block 1665]
ཞུན་མར་ལ་སོགས་པས་གང་བའི་བུམ་པ་ཞེས་བྱ་བ་འདིར་ཤུགས་ཀྱིས་ཞུན་མར་གྱི་བུམ་པ་ལ་སོགས་པའི་དོན་ཤེས་པའོ། ། གང་དུ་གཞག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གཞི་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1666]
བཤང་བ་དང་གཅི་བ་དང་ཆང་གི་བུམ་པ་དག་ནི་མི་མཁོ་བ་ཉིད་དོ། །

[Block 1667]
དགེ་འདུན་གྱི་ཕྱིར་ཡང་གཡོས་དང་འཚེད་པ་གང་ཡིན་པ་དག་གི་ཞལ་ཏ་བྱའོ་ཞེས་བྱ་བ༌[^1442]ནི། བྱེད་དུ་འཇུག་པ་ཞལ་ཏ་བྱེད་པ་སྟེ། རང་གིས༌[^1443]བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 1668]
འདིར་གཞུང་ནི་སྨན་གྱི་གཞི་ལས།

[Block 1669]
འདིར༌[^1444]དང་པོར་བྱས་ནས་ལྷུང་བཟེད་ཀྱི་ཁ་གཡོགས་བཅང་བར་བྱའོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་གསུངས་སོ། །

[Block 1670]
ལྷུང་བཟེད་དུ་བསོད་སྙོམས་མ་བླུགས་པའི་མདུན་རོལ་དུ་མ་བཟུང་བ་ཉིད་ཀྱིས་བསོད་སྙོམས་ལ་འཇུག་པར་བསྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། མ་བླུགས་པའི་མདུན་རོལ་དུ་ཞེས་བྱ་བ་ནི། མདུན་རོལ་དུ་ལྷུང་བཟེད་བློས་མ་བཟུང་བའི་ཕྱིར་རོ། །

[Block 1671]
ལྷུང་བཟེད་ཀྱི་ཁ་གཡོགས་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི། ལྷུང་བཟེད་ཀྱི་ནང་དུ་བསོད་སྙོམས་བླུགས་པ་གང་གིས༌[^1445]གཡོགས་པར་བྱེད་པ་དེ་ནི་ལྷུང་བཟེད་ཀྱི་ཁ་གཡོགས༌[^1446]ཞེས་བྱའོ།[^1447] །འདི་དང་འཁར་བའི་སྣོད་བཅང༌[^1448]བ་ལ་ཐུན་མོང་མ་ཡིན་པ་ཉིད་དུ་དོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ལྷུང་བཟེད་ཀྱི་ཁ་གཡོགས༌[^1449]བཅང་བར་བྱའོ་ཞེས་བྱ་བ་འདི་དང་འཁར་བའི་སྣོད་བཅང་བ་དག་ལས་དེ་ལ་ཕུལ་བའི་བཏུང་ཕོར་ལས་གཞན་པའི་འཁར་བའི་སྣོད་གང་ཟག་གིས་བཅང་བར་མི་བྱའོ་ཞེས་བྱ་བ༌[^1450]ཐུན་མོང་མ་ཡིན་པ་ཉིད་དུ་དོགས་པར་མི་བྱ་སྟེ། གཉིས་པོ་དེ་དགེ་སློང་མ་ལ་མ་ཡིན་སྙམ་དུ་རྟོག་པར༌[^1451]མི་བྱའོ་ཞེས་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1672]
ནད་པས་ཞྭ་བཅང་བ་ལ་ནི་མི་རུང་བ་ཉིད་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་དོགས་པར་མི་བྱའོ་ཞེས༌[^1452]སྦྱར་བར་བྱའོ། །

[Block 1673]
ཉེ་བ༌[^1453]འཁོར་རང་བཞིན་གྱི་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་མ་གཏོགས་པ་ཞེས་བྱ་བ་གསུངས་པས། ནད་པ་ལ་ཞྭ་བཅང་བར༌[^1454]རྗེས་སུ་གནང་བ་གང་ཡིན་པ་དེ་དགེ་སློང་མ་ལ་མི་རུང་བ་ཉིད་དུ་དོགས་པར་མི་བྱའོ། །

[Block 1674]
འདིར་གཞུང་ནི་སྐྱེ་དགུའི་བདག་མོ་ཆེན་མོ་གླད་པ༌[^1455]ན་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཞྭ་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1675]
དོན་འདི་ལ་བུད་མེད་ཀྱིས་ཀྱང་ཞྭ་བཅང་དུ་རུང་ངོ་ཞེས་བྱ་བ་འདིས་བསྟན་པར་འགྱུར་རོ། །

[Block 1676]
དེ་ལྟ་བས༌[^1456]ཆུ་ལ་ཆབ་རོམ་ཆགས་པའི་ཡུལ་དུ་ཡང་དེ་རྗེས་སུ་གནང་བར་ཤེས་པར་བྱ་སྟེ། དེའི་ཕྱིར་མདོ་འདི་ནི་དཔེ་ཙམ་དུ་རིག་པར་བྱའོ། །

[Block 1677]
སིལ་བྱེད་ཀྱི་སྒྲ་མ་ཕྱུང་བར་བསོད་སྙོམས་ལ་ཁྱིམ་དུ་འཇུག་པར་མི་བྱའོ། །

[Block 1678]
དེ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་སིལ་བྱེད་དེའོ། །

[Block 1679]
འབྱུང་བ་དང་འཇུག་པ་ལ་མཁས་པར་འབད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསོད་སྙོམས་པས་སོ། །

[Block 1680]
ཇི་ལྟར་ཞེ་ན་དེའི་ཕྱིར་མཚན་མར་བྱས་པས་སོ། །

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
--- END BLOCKS ---
