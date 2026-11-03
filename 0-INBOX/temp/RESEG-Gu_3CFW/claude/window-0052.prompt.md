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
[Block 1821]
ལག་པ་བསྙལ་ལ་ལྷུང་བཟེད་བཞག་ནས་ཞེས་གསུངས་པ་བཞིན་དུ་ཤེས་པར་བྱ་སྟེ། ཁའི་ནང་ཡང་བཀྲུས་ནས་ཞེས་བྱ་བ་དེ་ལྟ་བུས་འདིར་ཚིགས་སུ་བཅད་པ་གདོན་པ་ནི་མཛེས་པ་བསྐྱེད་པའོ། །

[Block 1822]
ཐམས་ཅད་ཀྱིས་ཟོས་ཟིན་པ་ཉིད་དུ་ངེས་པར་ཤེས་ནས་སོ་ཞེས་བྱ་བ་ནི་ཡོན་བཤད་པ་དང་ཆོས་བཤད་པ་དག་བྱའོ། །ཇི་ལྟར་ངེས་པར་ཤེས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཀུན་དུ་ལྟ་བས༌[^1576]སོ་ཞེས་བྱ་བ་སྨོས་སོ། །གང་གིས༌[^1577]དེ་དག་བྱ་ཞེ་ན། དེའི་ཕྱིར་དུ་མ་ཉིད་ཡིན་ན་དང་པོས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་དགེ་སློང་དག་དུ་མ་ཉིད་ཡིན་ན་དེའི་ཚེ་དེ་དག་གི་གྲལ་གྱི་དང་པོ་པས་དེ་དག་བྱའོ། །

[Block 1823]
མི་ནུས་ན་ནུས་པ་གཞན་ལ་བཅོལ་ལོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དང་པོས་དེ་དག་མི་ནུས་ན་དུ་མ་ཉིད་ཡོད་པའི་སྟོབས་དང་ལྡན་བ་གཞན་ལ་བཅོལ་བར་བྱའོ། །

[Block 1824]
གལ་ཏེ་མ་བྱས་པར༌[^1578]དགེ་སློང་རྣམས་ལ་འགྲོ་བའི་རྐྱེན་བྱུང་ན་འཁོར་ཐ་ན་བཞི་ཡན་ཆད་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཡོན་བཤད་པ་དང་ཆོས་བཤད༌[^1579]བྱེད་པ་ནའོ། །

[Block 1825]
གལ་ཏེ་འགྲོ་དགོས་པའི་རྐྱེན་བྱུང་ན་དེའི་ཚེ་འཆད་པར༌[^1580]བྱེད་པའི་ཐ་ན་དགེ་སློང་བཞི་ཡན་ཆད་གཞག་སྟེ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1826]
དེ་ལ་རྐྱེན་བྱུང༌[^1581]ན་བྱིན་པ་ལ་ཞུས་ཏེ་བལྟས་ནས་སོ་ཞེས་བྱ་བ་ལ་དེ་ལ་ཞེས་བྱ་བ་ནི་འཁོར་ལའོ། །

[Block 1827]
བལྟས་ནས་སོ་ཞེས་བྱ་བ་ནི་ཆོས་བཤད་པ་དང་། ཆོས་བཤད་པར་བྱེད་པའི་བཤད་པ་པོ་གང་ལ་དེ༌[^1582]འཁོར་དུ་སྦྱིན་པར་འགྱུར་བ་དེ་ལ་བལྟས་ནས་ཞེས༌[^1583]བྱ་བའི་དོན་གྱིས་ཤེས་པར་བྱའོ། །

[Block 1828]
ཡོན་འཆད་པ༌[^1584]ན་དགའ་བོ༌[^1585]དང་ཉེ་དགའ་དག་གི་མིང་སྨོས་པར་བྱའོ་ཞེས་བྱ་བ་ནི། འདིར་རྣམ་པར་འབྱེད་པའི་གཞུང་ཁ་ཅིག་ལས་ཡོན་འཆད་པའི་ཚེ་ན་ཀླུའི་རྒྱལ་པོ་དགའ་བོ་དང་ཉེ་དགའ་བོ་གཉིས་ཀྱི༌[^1586]མིང་ཡང་སྨོས་པར་བྱའོ། །

[Block 1829]
སྨོས་པར་མི་བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1830]
མིད་པ་གཉིས་པས་དུས་མ་ཡིན་པའི་སྒྲེགས་པ༌[^1587]དག་བྱུང་ན། དང་པོར་གཉིས་སམ་གསུམ་བོར་ཏེ་ཁ་བཀྲུས་ནས་མིད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། ཁ་ཆུ་ལ་སོགས་པ་གནོད་པ༌[^1588]ཉིད་སྒྲེགས་པ༌[^1589]དག་བོར་བའི་རྒྱུས་སྒྲེགས་པ༌[^1590]བོར་བའི་ལྷག་མ་བསལ་བའི༌[^1591]ཕྱིར་བཀྲུས་ནས་བོར་ད༌[^1592]གསུམ་པོ་འདི་དག༌[^1593]ལ་རྣམ་པར་གཞག་པ་དེ་བས་ན་འདི་ལ་མི་རུང་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 1831]
དེ་ནི་ཟས་མ་ཡིན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་སྒྲེགས་པ༌[^1594]བྱུང༌[^1595]བའོ། །

[Block 1832]
དེའི་ཕྱིར་གཞན་གྱིས་དུས་མ་ཡིན་པ་དང་སྤངས་པའི་ཚེ་སྒྲེགས་པ༌[^1596]བྱུང་ན་ཁ་བཀྲུ་བར་བྱའོ་ཞེས་བྱ་བ༌[^1597]ལ། གཞན་གྱིས་ཞེས་བྱ་བ༌[^1598]ནི་རྩེ་གཅིག་པ་སྒྲེགས༌[^1599]པའོ། །

[Block 1833]
འདི་མན་ཆད་ནི་རྒྱུ་མཐུན་པ་དག་གང་ཡིན་པ་དེ་དག་བརྗོད་པར་བྱ་སྟེ། དེའི་བྱིར༌[^1600]མ་བཤམས་པའི༌[^1601]ཕྱོགས་སུ་མཆིལ་མ་དོར་བར་མི་བྱའོ། །

[Block 1834]
བྱི་དོར་བྱས་པར་ཡང་མི་བྱའོ༌[^1602]ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་ཕྱོགས་མ་ཡིན་པ་ཡང་རུང་སྟེ་ཞེས་བྱ་བ༌[^1603]རྩོམ་པའི་ཤུགས་ཀྱིས༌[^1604]ཤེས་པར་བྱའོ། །

[Block 1835]
མ་མོ་ལས།

[Block 1836]
དེའི་སྐབས་ཞེས་བྱ་བའི༌[^1605]མཐར་ཐུག་པ་ཅན་ནོ། །

[Block 1837]
སོས་ལྕེ་བཙིར་ཏེ་ཡང་མི་བྱའོ་ཞེས་བྱ་བ༌[^1606]ནི་སོས་ལྕེ་བཙིར་ཏེ་མཆིལ་མ་བརླན་དེ་ལ༌[^1607]སྒྲ་ཙིད་ཅེས་ཀྱང་ཕྱོགས་དེར་དོར་བར་མི་བྱའོ། །

[Block 1838]
དེ་དང་དེའི་སྒྲ་གནས་བརྟན་གྱི༌[^1608]མདུན་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་མཆིལ་མ་དོར་བའོ། །

[Block 1839]
དེའི་སྒྲ་ཞེས་བྱ་བ་ནི་མཆིལ་མ་དོར་བ༌[^1609]དེའི་སྒྲའོ། །

[Block 1840]
ཟ་བའི་དྲུང་དུ་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་དང་དེའི་སྒྲ་མི་བྱའོ། །

[Block 1841]
ལྷག་མའི་དྲུང་དུ་ཡང་དང་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་བརྟན་དང་ཟ་བའི་ལྷག་མ་དེའོ། །

[Block 1842]
མི་ནུས་ན་གཞན་དུ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མཆིལ་མ་དོར་བ་དེ་མི་ནུས་ན་ཕྱོགས་གཞན་དུ་འགྲོ་བར་བྱའོ། །

[Block 1843]
གཞན་ལ་མི་བདེ་བ་མི་བྱའོ། །

[Block 1844]
སྔུར་སྒྲ་ཅན་གྱིས༌[^1610]ཉལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལྷག་མ་རྣམས་ཀྱི་མདུན་དུ་ཡང་ཉལ་བར་མི་བྱའོ། །

[Block 1845]
དེས་སྔུར་སྒྲ་སྤང་བའི༌[^1611]ཕྱིར་ཇི་ལྟ་ཞེ་ན། དེའི་ཕྱིར་ད་བཅག་པའམ་གཞན་དུ་འགྲོ་བར་བྱའོ། །

[Block 1846]
དེའི་སྣོད་གླང་པོ་ཆེའི་རྨིག་མཐིལ་ལྟ་བུའམ་བརྩེགས༌[^1612]མའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་མཆིལ་མ་དེའོ།[^1613] །དེ་མེད་ན་ཕྱི་མ་ཤོས་སོ། །

[Block 1847]
དེ་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་མཆིལ་མའི་སྣོད་དེའོ། །

[Block 1848]
དེར་སོ་ཕག་གི་ཕྱེ་མའམ༌[^1614]ཐལ་བ་དག་གི་གཅལ་བླུགས་སོ་ཞེས་བྱ་བ་ནི་མཆིལ་མའི་སྣོད་དེར་རོ། །

[Block 1849]
དེར་སྦྲང་བུ་འདུ་བའི་གཉེན་པོ་གང་ཞེ་ན། དེའི་ཕྱིར་སྦྲང་བུ་བསྐྲད་པ་གཉེན་པོ་ཡིན་ནོ་ཞེས་བྱ་བ༌[^1615]སྨོས་ཏེ། སའམ་ལོ་མ་ལ་སོགས་པས༌[^1616]དགབ་པས་སོ། །

[Block 1850]
དྲི་ང་བར་མི་འགྱུར་བ་དང་། སྲོག་ཆགས་འབྱུང་བར་མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་དུས་དུས་སུ་བཀྲུ་བ་དང་བསྐམ་པར་བྱ་བའོ༌[^1617]ཞེས་བྱ་བ་ནི་དྲི་ང་བར་མི་འགྱུར་བའི་ཕྱིར་དང་སྲོག་ཆགས་འབྱུང་བར་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1851]
དེའི་དུས་ཀྱི་ཆེད༌[^1618]དུ་གཞན་ཉེ་བར་གཞག་གོ་ཞེས་བྱ་བ་ནི་བཀྲུ་བ་དང་བསྐམ་པ༌[^1619]དེའི་དུས་ཀྱི་ཆེད་དུ་མཆིལ་མའི་སྣོད་འཐེབ༌[^1620]ཉེ་བར་གཞག་པར་བྱའོ། །

[Block 1852]
མི་བྲེལ་བར༌[^1621]བྱ་བའི་ཕྱིར་གཙུག་ལག་ཁང་གི་གྲྭའི་ཀ་བ་བཞི་པོ་དག་གི་ངོས་སུ་ཡང་མཆིལ་མའི་སྣོད་དག་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། བཞི་པོ་དག་གི༌[^1622]ཞེས་བྱ་བ་ནི་གྲྭའི་ཀ་བ་བཞི་པོ་དག་གི་ངོས་ལའོ། །

[Block 1853]
རླུང༌[^1623]ལས་སྒྲ་དང་བཅས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ནི་མ་མོ་ལས་གསུངས་པ་ཡིན་ནོ། །

[Block 1854]
དཀོན་མཆོག་དང་བླ་མའི་མདུན་དུ་མི་གཏོང༌[^1624]ངོ་། །གཞན་གྱི་དྲུང་དུ་ཡང་དང་ཡང་དུ་མི་གཏོང༌[^1625]ངོ་། །ཤིང་ལྗོན་པའི་དྲུང་དུ་བཤང་བ་དང་གཅི་བ་དག་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1855]
དགོན་པར་དེ་དག་གི་སྐབས་མེད་པ་ཉིད་ཡིན་ན་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི༌[^1626]ཚེར་མ་ཅན་གྱི་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ཤིང་ཚེར་མ་ཅན་གྱི་དྲུང་ཡང་མ་གཏོགས་ཏེ། དེར་སྐྱེ་བོ་དག་མི་སྡུག་པའི་ཕྱིར་རོ། །

[Block 1856]
བཤང་བའི་སྐྱབས་བྱའོ། །

[Block 1857]
གལ་ཏེ་གཙུག་ལག་ཁང་དུ་ན་ནུབ་བམ་བྱང་གི་ཕྱོགས་སུའོ་ཞེས་བྱ་བ་ནི། སྒོ་ཤར་ཕྱོགས་ཉིད་དང་ངེས་པ་ལ་སྨོས་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1858]
འདིར་ནུབ་དང་བྱང་ཞེས་བྱ་བ་ནི་ཉི་མ་ཤར་ནུབ་ཀྱི་འགྲོས་ཀྱི་ཕྱོགས་ལ༌[^1627]ལྟོས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1859]
ཕྱོགས་སུའོ་ཞེས་བྱ་བ་ནི། དཔུང་པ་གཅིག་གམ་གཞན་གྱི༌[^1628]མཚམས་ལ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1860]
གསོང་ལྡོང་ངམ་ཕུག་རྡུགས་སོ་ཞེས་བྱ་བ་ནི་མི་གཙང་བའི་ལས་ཤོད་དམ་ཁང་སྟེང་ཉིད་དུ་བྱའོ། །
--- END BLOCKS ---
