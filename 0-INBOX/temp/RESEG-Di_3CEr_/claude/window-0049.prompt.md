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
[Block 1716]
ཅི་སྟེ་གང་གི་ཕྱིར་ན་མ་མཐོང་ངོ་ཞེས་བྱ། དངོས་པོའི་དོན་ལ་ནི་ཁོ་བོ་ཅག་གི༌[^1336]ང་རྒྱལ་ཙམ་གྱིས་ཆོག་པར༌[^1337]འཛིན་པའི་འཇུག་པ་བཀག་པའི་ཕྱིར་རོ། །

[Block 1717]
དེ་ལྟ་ན་ནི། རང་ཐ་དད་ལ་སྤྱི་སེལ་འགྱུར། །གལ་ཏེ་མ་མཐོང་བ་ལས་སེལ་བར་བྱེད་ན་སྤྱིའི་སྒྲ་ཡང་རང་རང་གི༌[^1338]ཐ་དད་པ་རྣམས་ལ་མ་མཐོང་ངོ་ཞེས་གཞན་སེལ་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 1718]
གཞན་མིན་རིགས་པར་མཐོང་བའི་ཕྱིར། །མཐོང་ཞེས་པ་ནི་སྐབས་ལ་སོགས་པ་སྤྱིའི་སྒྲ་ལས་བྱེ་བྲག་སྤོང་བར་རོ། །

[Block 1719]
དེ་ལྟ་དེ་སྣང་ལ་ཐེ་ཚོམ། །དེ་ལྟར་བྱས་ན་ནི་སྤྱིའི་སྒྲ་དེ་བྱེ་བྲག་གི་སྣང་བ་ལ་ཐེ་ཚོམ་ཟ་བར་རིགས་པ་ཡིན་ནོ། །

[Block 1720]
གལ་ཏེ་དེ་རྣམས་ལ་ཡང་སྔར་དམིགས་པ་ཡིན་ན་ནི་རེ་ཞིག་འགྲེང་བ་ལ་ཡང་། ཐེ་ཚོམ་ཟ་བར་རིགས་ཤེ་ན། འདི་སྙམ་དུ་གལ་ཏེ་སྐབས་ལ་སོགས་པ་དང་དོན་དག་ལྷན་ཅིག་དམིགས་པ་ཡིན་ན་ནི་དེའི་ཕྱིར་ཇི་ལྟར་ན་ཐེ་ཚོམ་ཟ༌[^1339]ཞེ་ན། ངེས་པར་ཡན་གར་བ་ལ༌[^1340]ཞེས་དེ་ལྟར་དུ་བརྗོད་པར་མི་བྱ་སྟེ། དེ་ལ་སོགས་པ་དང་ལྡན་པའི་ཐེ་ཚོམ་ཟ་བ༌[^1341]ནི་དོན་ལ་སོགས་པ་དང་ལྡན་པར་ངེས་པ་ལ་དུས་ཕྱིས་ཡན་གར་བ་ལས༌[^1342]ཐེ་ཚོམ་ཟ་བ་ཡིན་ནོ། །

[Block 1721]
གལ་ཏེ་ཡན་གར་བ༌[^1343]ཐ་དད་པ་མེད་དེ། འདི་ལྟར་སྤྱིའི་སྒྲ་ཁྱད་པར་དུ་བྱས་པ་རྣམས་ལ་ཡན་གར་བ་མ་མཐོང་བ་རྣམས་ནི་ཇི༌[^1344]སྐད་དུ། རིགས་ཀྱི་སྒྲ་ཐ་དད་རྣམས་ཀྱི་རྗོད་བྱེད་མ་ཡིན་ནོ་ཞེས་བརྗོད་པ་བཞིན་ནོ༌[^1345]ཞེ་ན། ཉན་པ་པོ་ལ་ལྟོས་པ་མཐོང་། །ཉན་པ་པོ་གང་དག་སྤྱི་གཞན་བསལ་ནས། ཡན་གར་བ་དོན་དུ་གཉེར་བ་ཡིན་ཏེ། འདི་ལྟར་ཅི་ཤིང་འདི་ས་ལས༌[^1346]བྱུང་བའམ། འོན་ཏེ་འབྱུང་བ་ལྔ་ལས་བྱུང་བ་ཡིན་ཞེས་པ་ལས༌[^1347]ལས་བྱུང་བའོ་ཞེས་བརྗོད་པ་བཞིན་ནོ། །

[Block 1722]
དེ་ངེས་པའི་ལྟར་ན་ནི་དེའི་ཤིང་ལས་ལས་བྱུང་བའི་སྒྲ་སྦྱོར་རོ་ཞེས་པའི་ཐེ་ཚོམ་གང་ལས་ཡིན་ཞེས་དེའི་ངེས་པའོ་ཞེས་པ་འདི༌[^1348]འབའ་ཞིག་ལས་ཐེ་ཚོམ་འབྱུང་བ་ཡིན་ནོ། །

[Block 1723]
གངས་ལས་འབྱུང་བ་འབའ་ཞིག་ཐོས་སོ་ཞེས་པ་ཡོད་ན་སྲིད་དོ། །

[Block 1724]
ཡན་གར་བའི༌[^1349]སྦྱོར་བའོ་ཞེས་པའི་ཉེས་པ་ནི་མེད་དོ། །

[Block 1725]
ཇི་ལྟར་དོན་གཞན་སེལ་བ་དེ་བཞིན་དུ་སྤྱི་ཡང་། སྒྲ་གཞན་རྣམ་པར་དཔྱད༌[^1350]ནས་ནི། །སྒྲའི་སྤྱི་རྗོད་པར་བྱེད་པ་ཡིན། ཇི་ལྟར་བྱས་པས་མ་བྱས་པ་རྣམ་པར་བསལ་བའི་སྤྱིའི༌[^1351]མི་རྟག་པ་ལ་སོགས་པ་གོ་བར་བྱེད་པ་བཞིན་དུ་སྒྲ་གཞན་རྣམ་པར་དཔྱད་པའི༌[^1352]སྒྲའི་སྤྱིས་རྗོད་པར་བྱེད་དོ། །

[Block 1726]
དོན་ལ་སྦྱར་བར་བྱ་བ་མ་ཡིན་པ་སྟེ། དེ་ལ་ཡང་། དོན་གང་ལ་གཅིག་ཐེ་ཚོམ་ཟ། །གང་དུ་ཨཀྵ་ལ་སོགས་པའི་སྒྲའི་དོན་ཤིང་རྟའི་གཤོལ་མདའ་ལ་སོགས་པ་ལ་ཐེ་ཚོམ་སྐྱེད་པར༌[^1353]བྱེད་དོ། །

[Block 1727]
དེ་ལ་སྒྲ་གཅིག་ཉིད།[^1354] དུ་མ་ལ་ཐེ་ཚོམ་ན་ཡང་། །དེར་སྒྲ་ལ་སོགས་པ་དག་ལ་སྒྲ་ལ༌[^1355]སོགས་པར་ཐེ་ཚོམ་ཟ༌[^1356]རུ་ཆུག་ན་ཡང་དེ་ལ་ཉན་པ་པོས་སྤྱི་ལ་ཡང་སྒྲའི་བྱེ་བྲག་བལྟ་བར་བྱའོ། །

[Block 1728 [HEADING]]
### སྒྲས་དོན་གཞན་བསལ་ནས་རང་གི་དོན་བརྗོད་པ། ^5-9-0

[Block 1729]
ཡང་ཇི་ལྟར་ན་སྒྲས་དོན་གཞན་བསལ་ནས། རང་གི་དོན་བརྗོད་དེ། སྐྱོན་སྔ་མ་རྣམས་སུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1730]
འདི་ལྟར།

[Block 1731 [VERSE]]
སྒྲ་ཡིས༌[^1357]དོན་གཞན་མ་མཐོང་ཡང་། །
རང་དོན་ཆ་ཤས་སྟོན་པའི་ཕྱིར། །
སྒྲ་ཡིས༌[^1358]འབྲེལ་བ་ཤིན་ཏུ་སླ། །
འཁྲུལ་པ་ཉིད་ཀྱང་ཡོད༌[^1359]མ་ཡིན། །

[Block 1732]
རྗེས་སུ༌[^1360]འགྲོ་བ་དང་ལྡོག་པ་ནི་སྒྲས་དོན་བརྗོད་པའི་སྒོ་ནས་དེ་དག་དང་འདྲ་བ་དང་། མི་འདྲ་བ་དག་ལ་འཇུག་པ༌[^1361]དང་མི་འཇུག་པའོ། །

[Block 1733]
དེ་ལ་འདྲ་བ་ལ་ནི༌[^1362]གདོན་མི་ཟ་བར་ཐམས་ཅད་ལ་ནི་འཇུག་པར་མ་བརྗོད་དོ། །

[Block 1734]
མཐའ་མེད་བའི་དོན་ཁ་ཅིག་ནི་མི་བརྗོད་པ༌[^1363]སྲིད་པའི་ཕྱིར་རོ། །

[Block 1735]
མི་འདྲ་བ་ལས་ན་དོན་ཡོད་དུ་ཟིན་ཀྱང་མཐའ་མེད་པ་ལ་འཇུག་པར༌[^1364]ནུས་པ་མ་ཡིན་ཏེ། མ་བརྗོད་པ་ནི་མ་མཐོང་བ་ཙམ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1736]
དེ་ཉིད་ཀྱི་ཕྱིར་རང་དང་འབྲེལ་པ་ཅན་དག་ལས་གཞན་ལ་མ་མཐོང་བའི་ཕྱིར་དེ་རྣམ་པར་སྤྱད་པའི༌[^1365]རྗེས་སུ་དཔག་པ་ནི་རང་གི་དོན་རྗོད་པར་བྱེད་པ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1737]
རྗེས་སུ་འགྲོ་བའི་སྒོ་ནས་ཀྱང་དངོས་པོ་གཅིག་རྗེས་སུ་དཔོག་པ་ལ་ཤིང་ཤ་པ་ལ་སོགས་པར་སྣང་བ་ཐེ་ཚོམ་དུ་འགྱུར་བ༌[^1366]ཡིན་ནོ། །

[Block 1738]
ཐེ་ཚོམ་དེ་བཞིན་དུ་ས་ལས་བྱུང་བ་ནི་རྫས་མ་ཡིན་པ་ལ་སོགས་པ་ཉིད་དུ་སྣང་བ་ཐེ་ཚོམ་དུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 1739]
གང་དུ་ཤིང་གི་སྒྲ་ས་ལས་བྱུང་བ་ལ་སོགས་པ་མ་ཡིན་པ་ལ་མ་མཐོང་བ་དེའི་ཕྱིར་ལྡོག་པ་ཉིད་ལས་རྗེས་སུ་དཔག་པའོ། །

[Block 1740]
ཡང་བརྗོད་པ།

[Block 1741 [VERSE]]
ཤིང་དང་ས་ལས་བྱུང་དང་རྫས། །
ཡོད་དང་གཞལ་བྱ་རིམ་བཟློག་པས།[^1367] །
བཞི༌[^1368]གསུམ་གཉིས་གཅིག་ཐེ་ཚོམ་དུ། །
འགྱུར་གཞན་ངེས་པའི་རྒྱུ་མཚན་ཡིན། །

[Block 1742]
ཞེས་བྱ་བ་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 1743]
འབྲེལ་པ་ཅན་གྱི་ཕྱོགས་གཞན་ནས་སྒྲའམ་རྟགས་ཀྱི་རང་བཞིན༌[^1369]དོན་བརྗོད་པའི་ཆ་ཡོད་པ༌[^1370]མ་ཡིན་ཏེ། དེའི་དོན་དུ་མ་ཉིད༌[^1371]ལ་རྣམ་པ་ཐམས་ཅད་དུ་རབ་ཏུ་སྦྱོར་བ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 1744]
རང་གི་དོན་ལ་འཁྲུལ་པ་ཡང་མ་ཡིན་ཏེ། ཐ་དད་པར་རྗོད་པར༌[^1372]བྱེད་པའི་ཕྱིར་རོ། །

[Block 1745]
དེ་ལྟར་ན་རེ་ཞིག༌[^1373]ཉེས་པ་སྔ་མ་མེད་དོ། །

[Block 1746]
ཡོད་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་ཞེ་ན་འདི་ལྟར།

[Block 1747]
གཞན་ལ་ཁྱབ་པ་བཀག་པའི་ཕྱིར། །ཐ་དད་དོན་ནི་ཐ་དད་མིན།[^1374] །

[Block 1748]
སྤྱིའི་སྒྲས་ནི་གང་དོན་གཞན་རྣམ་པར་གསལ་བར་བྱས་པ་རང་གི་བྱེ་བྲག་དེ་མི་འཕེན་པས་ན་ཐ་དད་པའི་སྒྲ་དང་གཞི་མཐུན་པ་དང་ལྷན་ཅིག་པར་འཐད་དོ། །

[Block 1749]
དེས་ན་འདིའི་ཐ་དད་པའི་དོན་དང་སྒྲ་ཐ་དད་པའི་ཉེས་པ་མེད་དོ། །

[Block 1750]
དེ་ནི་མཐུན་པའི་སྒྲ་དང་དོན་གཞན་སེལ་བའི་དོན་གཉིས་ཀ་སྒྲའི་བརྗོད་བྱའོ། །

[Block 1751]
དེ་ལྟ་ན་རང་གི་དོན་ལ་མི་འཁྲུལ་བ་སྟེ། ཡན་གར་བ་ནི་གཞན་ལ་འཇུག་པ་མ་ཡིན་ནོ། །

[Block 1752]
ཉེས་པ་ཕྱི་མ་ཡང་ཡོད་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་ཞེ་ན། དངོས་འཇུག་ཐ་དད་མིན་ཕྱིར་ཡང་། །དོན་གཞན་ཉེ་བར་ལེན་པའི་སྒྲས་རང་རང་གིས༌[^1375]ཐ་དད་པ་རྣམས་ལ་འཇུག་པ་ནི་མེད་དོ། །

[Block 1753]
དེའི་ཕྱིར་དང་གཞན༌[^1376]གྱི་དབང་གིས་རང་གི་ངང་གིས༌[^1377]ཐ་དད་པ་མི་འཕེན་པའི་ཉེས་པ་མེད་དོ། །

[Block 1754]
ཐ་དད་ཐུག་པ་མེད་ཕྱིར་དང་། །ཁྱབ་པར་བྱེད་པ༌[^1378]མ་ཡིན་པའི་ཕྱིར་རྗོད་པར་བྱེད་པ་མ་ཡིན་པས་སྤྱིའི་ཉེས་པ་ཡང་མེད་དོ། །

[Block 1755]
དོན་གཞན་སེལ་བ་ཙམ་ནི་ཐ་དད་པ་མ་ཡིན་པའི་ཕྱིར་དང་། རྫས་མ་ཡིན་པའི་ཕྱིར་ཡང་ངོ་། །དེ་ཉིད་ཀྱི་ཕྱིར་འདིར་སྤྱིའི་བྱེ་བྲག་གཞན་དང་ལྡན་པ་བཙལ་བར༌[^1379]མི་བྱ་སྟེ། དངོས་སུ་དོན་གཞན་འགེགས་པ་ཡིན་པའི་ཕྱིར་ནའོ། །
--- END BLOCKS ---
