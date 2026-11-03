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
[Block 1891]
མ་བཏུབ་ན་བཅད་དོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་བཤུག་ཏུ་མི་བཏུབ་ན་བུ་གུ་སྒྲུབ་པར༌[^1646]མི་ནུས་ནས། དེའི་ཚེ་ཐག་མ༌[^1647]དེ་གཅད་པར༌[^1648]བྱའོ།[^1649] །གལ་ཏེ་ན་ནི་ཐན་ཀོར༌[^1650]དུ་ལོ་མའི་ཆང་བུ་དག་གཞུག་གོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་བུ་གའི༌[^1651]ཐན་ཀོར༌[^1652]དུ་ཞུགས་ཤིང་བཤང་བ་བྱ་བའི་ཕྱིར་འདུག་པ་ན་རེག་པས་བཤང་བའི་ལམ་གྱི་ཐན་ཀོར༌[^1653]ན་ནི་དེའི་ཚེ་ལོ་མའི་ཆང་བུ་དག་འདིར་གཞུག་པར་བྱའོ། །

[Block 1892]
ས་སྨད་པར་བསྲུང་བར་བྱའོ། །

[Block 1893]
དེའི་ཕྱིར་འོག་གཞིར་གྱོ་མོ་བྱའོ་ཞེས་བྱ་བ་ནི་དེའི་འོག་གཞིར་གྱོ་མོ་གཞུག་པར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1894]
ཧ་ཅང་མི་མཐོ་བ་བཟང་ངོ་ཞེས་བྱ་བ་ནི་གྱོ་མོའོ། །

[Block 1895]
དྲི་ང་བར་མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་དུས་སུ་བཀྲུ་བ་དང་སྐམ་པ་དང་ཡུངས་མར་གྱིས་བསྐུ་བར་བྱའོ། །

[Block 1896]
དེའི་དུས་ཀྱི་ཆེད་དུ་གཞན་བསྒྲུབ་པོ་ཞེས་བྱ་བ་ནི་བཀྲུ་བ་དང་བསྐམ་པ་དང་ཡུངས་མར་གྱིས་བསྐུ་བ་དེའི་དུས་ཀྱི་ཆེད་དུ་གྱོ་མོའི་འཐེབ་གཞན་བསྒྲུབ་པར་བྱའོ།[^1654] །མ་འབྱོར་ན་གཞི་ཉིད་དུ་ལོ་ཆུན་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི། གྱོ་མོ་གཞན་མ་འབྱོར་ན་དེ་ཉིད་ཀྱི་སྟིང༌[^1655]དུ་ལོ་ཆུན་གཞག་པར་བྱའོ།[^1656] །དེའི་སྟེང་དུ་བཤང་བ་བྱའོ། །

[Block 1897]
དེ་ཉིད་དང་ལྷན་ཅིག་དོར་བར་བྱ་ཞིང་དུས་གཞན་གྱི་ཚེ་ན་ཡང་ལོ་ཆུན་གཞན་གཞག་པར་བྱའོ། །

[Block 1898]
གྱོ་མོ་དེ་ཉིད་བཀྲུ་བ་ལ་སོགས་པའི་དོན་འགྲུབ་པར་འགྱུར་རོ། །

[Block 1899]
བཤང་བ་བྱས་ནས་དེ་བྱེད་པའི་བཤང་བའི་ལམ་ཕྱི་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་བྱེད་པའི་ཞེས་བྱ་བ་ནི་བཤང་བ་དེ་བྱེད་པའི་ལམ་མོ། །ཅི་ཞིག་གིས་དེ་ཕྱི་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་རྣོན་པོ་དང་རྩྭའི༌[^1657]ཆང་བུ་མ་ཡིན་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1900]
འོ་ན་ཅི་བཟང་ཞེ་ན། དེའི་ཕྱིར་འདི་ལ་རས་མ་དང་ལོ་ཆུན་དང་ལོ་མའི་ཆང་བུ་དང་། ཤིང་དང་བོང་རྡོག་དག༌[^1658]བཟང་བ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ལ་ཞེས་བྱ་བ་ནི་བཀྲུ་བར་བྱ་བ་ལའོ། །

[Block 1901]
ས་གཉིས་ཀྱིས་བཀྲུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བཤང་བའི་ལམ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1902]
སྔར་གཞག་པའི་ས་མ་འདྲེས་པ་དག་གིས་ཕྱིས་བཀྲུ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། སྔར་ཞེས་བྱ་བ་ནི་བཤང་བ་བྱས་པ་ལས་དང་པོ་ཉིད་དུ་འཁྲུ་བ་ཞེས་བྱའོ།[^1659] །འཐོར་འཐུང་གི་རྐང་རྟེན་དག་ཟེར་མ་དག་གིས༌[^1660]མི་ཉམས་པ་ཉིད་དུ་ཁད་ཀྱིས༌[^1661]དལ་བུ་དལ་བུས་སོ་ཞེས་བྱ་བ་དེ༌[^1662]ནི་མ་མོ་ལས་སོ། །

[Block 1903]
བདུན་པ་དག་གིས་གཡོན་པའོ་ཞེས་བྱ་བ་ནི། ལག་པ་གཡོན་པ༌[^1663]བཀྲུ་བའོ། །

[Block 1904]
བདུན་གྱིས་ནི་གཉིས་ཀའོ་ཞེས་བྱ་བ་ནི་ལག་པ་གཉིས་ཀ༌[^1664]བཀྲུ་བར་བྱའོ། །

[Block 1905]
ལག་ངར་གཉིས་ཀྱང་བཀྲུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ལག་པ་གཉིས་བཀྲུས་པ་དེའི་རྗེས་ལའོ། །

[Block 1906]
ཡང་ལག་པ་གཉིས་སོ།[^1665] ། གཞན་གྱིས༌[^1666]རིལ་བ་སྤྱི་བླུགས་སོ་ཞེས་བྱ་བ་ལ། གཞན་གྱིས་ཞེས་བྱ་བ་ནི་སས༌[^1667]སོ། །

[Block 1907]
རྐང་པ་གཉིས་བཀྲུ་བའོ། །

[Block 1908]
ལྟོ་འཛག་པས་ནི་མདུན་དག་ཏུ་ཕྱི་བ་ཙམ་བྱས་ཏེ་འདུག་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ལ། ཐ་མའི་མདུན་དུ་ཞེས་བྱ་བ་འཛག་པའི་ཐ་མ་ལས་མདུན་རོལ་དུ་བྱའོ། །

[Block 1909]
དེ་ལས་གཞན་པས་ནི་ཆུ་ཡོད་ན་འཐོར་འཐུང་མ་བྱས་པར་ཡང་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་ལྟོས༌[^1668]འཛག་པ་ལས་སོ། །

[Block 1910]
འཐོར་འཐུང་མ་བྱས་པས་ཞེས་བྱ་བ་ནི་ཁྲུང་མ༌[^1669]བྱས་པས་ཏེ༌[^1670]དེ་ནི་མ་མོ་ལས་སོ། །

[Block 1911]
སྨན་གྱི་གཞི༌[^1671]ཕྲན་ཚེགས་ལ་སོགས་པའི་སྐབས་སོ། །

[Block 1912]
སྨན་གྱི་གཞི་རྫོགས་སོ།། །།

[Block 1913 [HEADING]]
## ལས་ཀྱི་གཞི། ^5-0

[Block 1914]
ཆོ་ག་ལས་འདས་ན་ལས་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་ཆོ་ག་གང་དག་ལས་གང་ཞིག་བྱེད་པ་ཆོ་ག་ལས་འདས་ན་གཞན་དུ་ན་དེ་མི་བྱེད་པ་ལ་ཕྱི་རོལ་གྱི་དེ་འབད་པ་ཙམ་དེའི་ཆོས་འདུལ་བར་གཏོགས་པའི་ལས་བྱས་པར་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1915]
འདིར་ཆོ་ག་ནི་དགེ་འདུན་ཚང་བ་དང་ལས་བརྗོད་པ་དང་ལས་བྱེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཆོ་གའི་རྣམ་པ་བསྟན་ཏོ། །

[Block 1916]
དགེ་འདུན་ལྷག་མའི་ལྟུང་བ༌[^1672]དབྱུང་བ་ལ་ནི་དགེ་སློང་ཉི་ཤུ་ལ་སོགས་པའོ། །

[Block 1917]
ཡུལ་དབུས་སུ་བསྙེན་པར་རྫོགས་པ་ལ་ནི་བཅུ་ལ་སོགས་པའོ། །

[Block 1918]
མཐའ་འཁོབ་ཏུ་ནི་གཞན་མེད་ན་འདུལ་བ་འཛིན་པ་དང་ལྔ་ལ་སོགས་པའོ། །

[Block 1919]
དགེ་སློང་མ་དགེ་འདུན་ལྷག་མ་ལས་དབྱུང་བ་ལ༌[^1673]ནི་མཚམས་ཀྱི་དགེ་འདུན་གཉིས་ཀ་ཚོགས་པའོ། །

[Block 1920]
དགེ་སློང་མའི་སྡོམ་པ་སྦྱིན་པ་དང་། ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་སྦྱིན་པ་དང་། འཁོར་ཉེ་བར་འཇོག་པ་དང་། འཁོར་མང་པོ་ཉེ་བར་འཇོག་པའི་གནང་བ་སྦྱིན་པ་ལ་ནི་ཡུལ་དབུས་སུ་དགེ་སློང་མ་བཅུ་གཉིས་ལ་སོགས་པའོ། །

[Block 1921]
བསྙེན་པར་རྫོགས་པ་ལ་ནི་དགེ་སློང་བཅུ་དང་དགེ་སློང་མ་བཅུ་གཉིས་ལ་སོགས་པའོ། །

[Block 1922]
ལས་གཞན་ཐམས་ཅད་ལ་ནི་བཞི་ལ་སོགས་པའོ་ཞེས་གསུངས་པའི་གྲངས་དེ་བཞིན་ཚང་བའོ། །

[Block 1923]
ལས་བརྗོད་པ་ཞེས་བྱ་བ་ནི༌[^1674]གསོལ་བ་འབའ་ཞིག་གི༌[^1675]ལས་དང་གསོལ་བ་དང་། གཉིས་ཀྱི༌[^1676]ལས་དང་། གསོལ་བ་དང་བཞིའི་ལས་བརྗོད་པ་དག་ལས་གང་ལ་གང་བྱ་བར་གསུངས་པ༌[^1677]དེ་ལས་མ་ཆད་པ་སྟེ། ལྷག་མ་ལ་ནི་ཉེས་པ་མེད་དོ། །

[Block 1924]
ལས་བྱེད་པ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པའི༌[^1678]ལས་བྱས་པ་ལ་སོགས་པའོ། །

[Block 1925]
ལས་ནི་གསོལ་བ་དང་བརྗོད་པ་དང་སོ་སོར་ཐར་པ་འདོན་པ་དང་། དགག་དབྱེའོ་ཞེས་བྱ་བ་ནི་ལས་བརྗོད་པའོ། །

[Block 1926]
སོ་སོར་ཐར་པ་འདོན་པ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་ངོ་། །དགག་དབྱེ་ཞེས་བྱ་བ་ནི་ལས་བརྗོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1927]
ཐོས་པར་བྱ་བ་མ་ཡིན་པས་ཐོས་པ་ནི་མི་འཆགས་པར༌[^1679]མི་འགྱུར་རོ་ཞེས་བྱ་བ༌[^1680]ནི། གང་ཞིག་དེ་མ་ཡིན་པ་ལ་སོགས་པའི་དབང་དུ་བྱ་སྟེ། སྨོས་པ་དེ་ནི་དེ་དག་གིས་དེ༌[^1681]ཐོས་པར་བྱ་བ་མ་ཡིན་པས་དེ་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བ་ཙམ་དུ་འགྱུར་གྱི་མི་འཆགས་པར༌[^1682]མི་འགྱུར་རོ། །

[Block 1928]
དེ་ལྟར་ཡང་ཀུན་དགའ་བོ་ཁྱོད་ཀྱིས་རྒྱལ་པོ་གསོ་སྦྱོང་གི་ཕྱིར། སོ་སོར་ཐར་པ་འདོན་པ་ཉན་དུ་མ་བཅུག་པ་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1929]
མི་འཆགས་པ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལས་གང་འདི་ལ་འཆགས་པ༌[^1683]མེད་པ་དེ་ནི་མི་འཆགས་པ་སྟེ་ལས་དེ༌[^1684]མི་བྱའོ། །

[Block 1930]
གང་ཞིག་ཆོས་མ་ཡིན་པའི་ལས་རྣམས་ལ་དེས་ནི་དགེ་འདུན་ལ་ཡང་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་འདོད་པ་བས་ན༌[^1685]མདོ་འདིའོ། །
--- END BLOCKS ---
