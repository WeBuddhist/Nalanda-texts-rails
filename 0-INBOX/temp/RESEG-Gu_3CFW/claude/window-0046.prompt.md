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
[Block 1611]
པདྨའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཡང་ནགས་ཀྱི་རུས་པ་ཡིན་ཏེ། སྤངས་ཏེ་ལངས་པས་བཟའ་བར་བྱའོ། །

[Block 1612]
འདིར་ཐམས་ཅད་དུ་ལྷག་མའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྤངས་ཏེ་ལངས་པས་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 1613]
པདྨ་ཞེས་བྱ་བ་དེ་ཅི་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདི་ལྟ་སྟེ་པདྨའི་རྩ་བ་དང་། པདྨའི་རྩ་ལག་དང་བེ་ཊ་དང་། ཨུཏྤ་ལའི་རྩ་བ་དང་པདྨའི་སྙིང་པོ་དག་ནི་དེ་ཞེས་བྱའོ་ཞེས་སྨོས་སོ། །

[Block 1614]
གཞིར་གཏོགས་པའི་སྨན་གྱི་གཞིའོ།། །།

[Block 1615]
དེ་ལ་རེ་ཞིག་འབྲེལ་པ་བསྟན་པར་བྱ་སྟེ། བཀྲེས་པ་དང་སྐོམ་པ་དག་ནི་ནད་དང་འདྲ་བ་མ༌[^1397]ཡིན་ཏེ། དེ་བས་ན་དེ་དག་གི་གཉེན་པོར་གྱུར་པ་འཚོ་བ་ཙམ་སྒྲུབ་པར་བྱེད་པ་བཟའ་བར་བྱ་བ་དང་། བཏུང་བར་བྱ་བ་དུས་སུ་རུང་བའི་སྨན་གྱི་ཆོས་ཁོངས་སུ་གཏོགས་པ༌[^1398]ཉིད་གང་ཡིན་པ་དེ་དག་གི་འདུ་བའི་སྒོ་བསྟན་པའི་ཕྱིར། རྒྱལ་སྲིད་དང་དེའི་ཕྱེད་ནོད༌[^1399]པར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་དེའི་ཞེས་བྱ་བ་ནི་རྒྱལ་སྲིད་དེའོ། །

[Block 1616]
དགེ་འདུན་གྱི་ཆེད་དུ་གྲོང་མནོད་པའོ། །

[Block 1617]
ཞིང༌[^1400]ཡང་ངོ་ཞེས་བྱ་བ་ནི་མནོད་པར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཞིང་ནི་གྲོང་གི་ཕྱོགས་གཅིག་པ་ཡིན་པའི་ཕྱིར་གྲོང་མེད་པའི་ཕྱིར་དགོན་པ་དང་། འབད་རྩོལ་མེད་པའི་གནས་དང་འབྲེལ་པ་ཞེས་བྱ་བ་ལྷག་མས་ཤེས་པར་བྱའོ། །

[Block 1618]
དེ་ཡལ་བར་མི་དོར་རོ་ཞེས་བྱ་བ་ནི་ཞིང་དེའོ། །

[Block 1619]
དེའི་འོག་ཤས༌[^1401]མནོད་དོ། །

[Block 1620]
ཐོག་ཤས་བརྩལ༌[^1402]ལོ། །

[Block 1621]
མནོད་པས༌[^1403]དེ་གཙུག་ལག་ཁང་དུ་དབུལ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ནམ་གྱི་ཚེ་གང་ཞེ་ན། དེའི་ཕྱིར་བདག་ཉིད་ཀྱི་བས་དང་པོར་རོ། །

[Block 1622]
བསྲུང་བའི་ཕྱིར་དགེ་སློང་དག་བསྐོའོ་ཞེས་བྱ་བ་ནི་ཐོག་ཤས་མནོད་པ་ལ་སོགས་པ་ལའོ། །

[Block 1623]
འདུ་བ་དང་འགོད་པ་དང་གཉིས་ཀ་ལས་གང་ཡང་རུང་བ་མི་མངོན་པས་རྩིས༌[^1404]གདབ་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། འདུ་བ་དང་འགོད་པ་དང་། འདུ་འགོད་གཉིས་ལས་གང་ཡང་རུང་བ་ཞེས་བྱ་བའོ། །

[Block 1624]
འདི་རྣམས་ལས་གཞན་པའི་དག་འདུན་གྱི་གནས་གཅིག་ལས་གདགས་པར་མི་བྱ་སྟེ། དེར་རྩིས༌[^1405]གདབ་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1625]
གཞན་ལ་དྲན་པ་དང་ཤེས་བཞིན་སྔོན་དུ་བཏང་སྟེ་དེ་ལ་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། གཞན་ལ་ཞེས་བྱ་བ་ནི་གང་དུ་གཉིས་ཀ་གདགས་པ༌[^1406]བྱེད་པ་ལ་དེར་རྩིས་བྱེད་པ་ལ་དྲན་པ་དང་། ཤེས་བཞིན་སྔོན་དུ་བཏང་སྟེ་འཇུག་པར་བྱའོ། །

[Block 1626]
དགེ་འདུན་གྱི་ཆེད་དུ་གཡོག་འཁོར་ཉེ་བར༌[^1407]གཞག་གོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་མ་བྱིན་པར་ལེན་པའི་ཕམ་པར་གྱུར་པ་ལས་འདིར་ལས་ཀྱི༌[^1408]མཐར། བཅོམ་ལྡན་འདས་ཀྱིས༌[^1409]བཀའ་སྩལ་པ། དགེ་འདུན་གྱི་ཆེད་དུ་གཡོག་བླང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1627]
གང་ནས་གཙུག་ལག་ཁང་དུ་སྒྲ་མི་འབྱུང་བ་དེར་ལྷ་འབངས་ཀྱི་ཁྱིམ་བྱེད་དུ་གཞུག༌[^1410]གོ། །

[Block 1628]
ཇི་སྙེད༌[^1411]དགོས་པར༌[^1412]འཇུག་པར་བྱའོ། །

[Block 1629]
ཟས་དང་གོས་སྦྱིན་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། གཙོ་བོར་དགེ་འདུན་གྱི༌[^1413]གཡོག་དག་ལའོ། །

[Block 1630]
གལ་ཏེ་གཞན་མེད་ན་དེའི་དོན་དུ་སྦྱིན་པ༌[^1414]ཤུགས་ཀྱིས་རྟོགས་པའོ། །

[Block 1631]
གལ་ཏེ་ལས་བྱེད་པ་ནའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཡོག་དག་ལས་བྱས་ན་དེ་དག་ལ་ཟས་དང་གོས་སྦྱིན་པར་བྱ་བ་ཉིད་དོ། །

[Block 1632]
ན་བ་རྣམས་ལ་གཡོག་བྱའོ་ཞེས་བྱ་བ་ནི་གཡོག་དག་གལ་ཏེ་ན་ན་དེ་རྣམས་ལ་ཡལ་བར་མི་དོར་དེ་སྨན་ལ་སོགས་པས་བསྙེན་བཀུར་བྱའོ། །

[Block 1633]
བ་གླང༌[^1415]དང་མ་ཧེ་དང་ར་དང་ལུག་དང་། གླང་པོ་ཆེ་དང་རྟ་དང་རྔ་མོ་དང་བོང་བུ་དང་། འབྲུ་ཙམ་པ་དང་སྣོད་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་དགེ་འདུན་གྱི་ཆེད་དུ་བླང་བར་བྱའོ། །

[Block 1634]
གླེང་གཞི་རྣམས་ལས་འབྲུ་ཙམ་པ་གནང་བ་རྗེས་སུ་གསུངས་པ་ཡིན་ནོ། །

[Block 1635]
ཕྲན་ཚེགས་དག་ལས་ནི་སྣོད་རྣམས་ལའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1636]
འདི་ཡང༌[^1416]འདིར༌[^1417]གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས༌[^1418]ལོངས་སྤྱོད་དང་། ལོངས་སྤྱོད་མཆོག༌[^1419]བླང་དུ་རུང་ངམ་ཀ་ཏ་ཡ༌[^1420]ན་དགེ་འདུན་གྱི་ཆེད་དུ་བླང་དུ་རུང་ངོ་། །དེ་ལ་ལོངས་སྤྱོད་ནི༌[^1421]གྲོང་དང་ཞིང་དག་གོ། །

[Block 1637]
ལོངས་སྤྱོད་མཆོག་ནི་བ་ལང་དང་ར་དང་ལུག་དང་མ་ཧེའོ། །

[Block 1638]
ཡོ་བྱད་མ་ཡིན་པ་དག་གང་ཞེ་ན་གླང་པོ་ཆེ་དང་རྟ་དང་རྔ་མོ་དང་བ་ལང་དང་། བོང་བུ་དང་ར་དང་ལུག་དང་མ་ཧེ་བཅོམ་ལྡན་འདས་ཀྱིས་རྗེས་སུ་གནང་བ་མཆོད་རྟེན་གྱི་ཡང་རུང་བ་དག་གོ་ཞེས་བྱ་བ་ནི། མ་མོ་ལས་དེ་བསྡུས་ནས་གསུངས་པ་ཡིན་ནོ། །

[Block 1639]
གང་ཞིག་ཕུལ་ནས་ཁྱིམ་པ་ཤི་ན་གླང་པོ་ཆེ་ལ་སོགས་པ་རྣམས་རྒྱལ་པོ་ལ་དབུལ་ལོ་ཞེས་གསུངས་སོ། །

[Block 1640]
རྫས་འདི་ཉིད་རྙེད་པ༌[^1422]ལ་ཡང་ཁྱིམ་པས་རྒྱལ་པོ་དབང་བ་ཉིད་ཅེས་བྱ་བ་དེའི་དགོངས་པ་ནི༌[^1423]འདི་ཡིན་གྱི།[^1424] དེ་བདག་ཏུ་བྱེད་པ་ལ་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་རྟེན་རྟོགས་པར་བྱའོ། །

[Block 1641]
དེ་དག་མཆོད་རྟེན་གྱིར༌[^1425]ཡང་མི་རུང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གྲོང་ལ་སོགས་པ་དགེ་འདུན་གྱི་ཆེད་དུ་བླང༌[^1426]དུ་རུང་བ་དེ་དག་མཆོད་རྟེན་གྱི་ཆེད་དུ་ཡང་རུང་། དགེ་འདུན་གྱི་ཆེད་དུ་ཡང་རུང་བ་དེ་དག་གོ་ཞེས་བྱ་བ་མ་མོར་གཏོགས་པ་དེ་བས་ན་མདོ་འདིའོ། །

[Block 1642]
དེའི་རྗེས་སུ་འབྲངས༌[^1427]ནས་འདིར་ལྷག་མ་བསྡུས་པའོ། །

[Block 1643]
ཁ་གཟར་དང་ཚྭ༌[^1428]ཁུག་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་གཉིས་ཞེས་བྱ་བ་ནི་ཁ་གཟར་དང་ཚྭ༌[^1429]ཁུག་དག་གོ། །

[Block 1644]
དེ་གཉིས་དང་ཕུལ་བའི་བཏུང་ཕོར་ལས་གཞན་བའི་ཁར་བའི༌[^1430]སྣོད་གང་ཟག་གིས་བཅང་བར་མི་བྱའོ། །

[Block 1645]
ཀུན་དགའ་ར་བ་པ༌[^1431]ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་མ་མོ་ལས་དགེ་འདུན་གང་གིས་ཀྱང་ངོ་། །བསྲུང་བའི་ཕྱིར་བྱིས་པ་མཚན་མཐུན་པ་འབུལ་བ་དག་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ནམ་གང་ཟག་གིས་ཀྱང་བླང་བར་བྱའོ། །

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
--- END BLOCKS ---
