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
[Block 1786]
ཇི་ལྟར་ཞེ་ན་དེའི་ཕྱིར་འབྱུང་བ་དང་འདྲ་བ་དང་འགྱུར་བ་དང་ཕྱིར་རྒོལ་བ་ཉིད་དང་རྒྱུ་མཐུན་པ་དང་བརྟེན་པ་དང༌[^1552]རྣམ་པ་དང་བཙལ་བ་དང་། གཞན་ལ་རག༌[^1553]ལས༌[^1554]པ་ཉིད་དང་། སོ་སོར་འགྲོ་བ་དག་གི༌[^1555]མི་མཐུན་པ་ཉིད་དུ་གཞག་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འབྱུང་བ་ལ་སོགས་པ་རྣམ་པ་བཅུ་པོ་དེ་དག་གི་ཟས་ལས་མི་མཐུན་པའི་དྲན་པ་ཉེ་བར་གཞག་སྟེ། བཟའ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1787]
དེ་ལ་འབྱུང་བ་ཞེས་བྱ་བ་ནི་ཟས་ནི་མི་གཙང་བ་དང་། ལུད་པ་ལ་སོགས་པ་དག་ལས་འབྱུང་བའོ། །

[Block 1788]
འདྲ་བ་ཞེས་བྱ་བ་ནི་འདི་ལྟ་སྟེ། འབྲས་ཆན་ནི་སྲིན་བུ་དང་འདྲ་ལ། ཕྱེ་དག་ནི་རུས་ཕྱེ་དང་འདྲ་བ་ལ་སོགས་པའོ། །

[Block 1789]
འགྱུར་བ་ཞེས་བྱ་བ་ནི་ཟས་ཟོས་ན་བད་ཀན་དང་སྣབས་དང་རྣག་དང་ཁྲག་ལ་སོགས་པར་འགྱུར་བའོ། །

[Block 1790]
ཕྱིར་ཞེས་བྱ་བ་ནི་ཟས་ཀྱི༌[^1556]ཕྱིར་རྒོལ་བ་རྣམས་དང་རྗེས་སུ་འབྲེལ་བ་སྟེ།

[Block 1791]
ཟས་ཀྱི༌[^1557]རྒྱུ་ལས།

[Block 1792]
མ་ནི་བུ་དང་ལྷན་ཅིག་འཐབ་པར་བྱེད། བུ་ནི་མ་དང་ལྷན་ཅིག་འཐབ་པར་བྱེད་པ་ལ་སོགས་པའོ། །

[Block 1793]
རྒྱུ་མཐུན་པ་ཞེས་བྱ་བ་ནི་ཟས་ནི་བཤང་དང་གཅི༌[^1558]ལ་སོགས་པ་ཤིན་ཏུ་སྨད་པ་དག་དང་རྒྱུ་མཐུན་པ་ཡིན་ནོ། །

[Block 1794]
རྟེན་པའི་རྣམ་པ་ཞེས་བྱ་བ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྟེ། ཟས་འདི་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྟེ། ཞིང་ལ་སོགས་པ་ལ་བརྟེན༌[^1559]ཏེ་འབྱུང་བ་དང་། དེ་དག་ལ་བརྟེན༌[^1560]ནས་སྲེད་པ་ལ་སོགས་པའི་ནད་མང་པོ་དུ་མ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1795]
བཙལ་བ་ཞེས་བྱ་བ་ནི་དེ་ཚེགས་ཆེན་པོས་བསྒྲུབ་དགོས་པའོ། །

[Block 1796]
གཞན་ལ་རག་ལས་པ་ཉིད་ཅེས་བྱ་བ་ནི་ཚེགས་ཆེན་པོས་འབྲུ་ལ་སོགས་པ་གྲུབ་ཀྱང་དེ་གཡོ་བ་ལ་སོགས་པ་མེད་ན་མི་ལྡན་པའི་ཕྱིར་གཞན་ལ་རག་ལས་པ་ཉིད་དུ་འགྱུར་བའོ། ནད་དང་བཅས་པ་ཉིད་ཅེས་བྱ་བ་ནི་ཟས་ལོག་པར་ཞུ་བས་རིམས་ལ་སོགས་པའི་ནད་མང་པོ་དུ་མ་དག་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1797]
སོ་སོར་འགྲོ་བ་ཉིད་ཅེས་བྱ་བ་ནི། ཟས་འདི་རྣམ་བཞིར་འགྲོ་བ་སྟེ། དེའི་ཆ་གཅིག་ནི་ལུས་ཀྱི་མེས་སྲེག་པར་བྱེད་པ་དང་།

[Block 1798]
གཉིས་པ་ནི་བཤང་བ་དང་གཅི་བར་གྱུར་པ་དང་།

[Block 1799]
གསུམ་པ་ནི་སྲིན་བུ་དག་གིས་བཟའ་བར་འགྱུར་བ་དང་།

[Block 1800]
བཞི་པ་ནི་ལུས་བརྟས་པར༌[^1561]བྱེད་པའོ། །

[Block 1801]
དྲན་པ་ཉེ་བར་གནས་པས་སོ་ཞེས་བྱ་བ་ནི་ཟས་ལ༌[^1562]སེམས་གཏད་པས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1802]
སེམས་རྣམ་པར་མ་གཡེངས་པས་སོ་ཞེས་བྱ་བ་ནི་སེམས་ཐམས་ཅད་ཀྱིས་ཟས་ལ་རྩེ་གཅིག་པས་གཏད་པ་སྟེ། ཆ་ཤས་ཀྱིས་ནི་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཤེས་བཞིན་གྱིས༌[^1563]སྒྲ་བསྐྱུང་ཞིང་ངོ་། །དེ་མི་སྦྱར་བར་རོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་སྒྲ་མི་བྱ་བ༌[^1564]དེའོ། །

[Block 1803]
མི་འབྱུང་བར་ཐུག་པ་དག་གོ་ཞེས་བྱ་བ་ནི་སྒྲ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1804]
ཁྲུམ་ཁྲུམ་མི་བྱ་བར་རོ་ཞེས་བྱ་བ་ནི་སྒྲ་ཁྲུམ་ཁྲུམ་མི་བྱ་བར་རོ། །

[Block 1805]
སྒྲ་འབྱུང་བ་དག་ཆུ་ལ་སོགས་པས་སྙེ་བར༌[^1565]བྱའོ་ཞེས་བྱ་བ་ནི་བཟའ་བར་བྱ་བ་རྣམས་ལའོ། །

[Block 1806]
བཟའ་བ་དེའི་དོན་དུ་རོལ་མོ་བྱེད་དུ་མི་གཞུག་གོ་ཞེས་བྱ་བ་ནི། ཟས་ཟ་བ་དེའི་དོན་དུ་གླུ་གླིང་དང་། སིལ་སྙན་ལ་སོགས་པའི་རོལ་མོ་བྱེད་དུ་གཞུག་ཅིང་བཟའ་བར་མི་བྱའོ། །

[Block 1807]
འདིར་གཞུང་ནི་ཨ་མྲ་སྐྱོངས༌[^1566]ཀྱིས་རང་གི༌[^1567]མགྲོན་དུ་བོས་པའི་དགེ་འདུན་ཟ་བ་ན་རོལ་མོ་བྱ་བར་བརྩམས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་གིས༌[^1568]རོལ་མོ་བྱེད་དུ་གཞུག་བཞིན་དུ་བཟའ་བར་མི་བྱའོ། །

[Block 1808]
ཟ་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ། །

[Block 1809]
ཁང་པའི་དུས་སྟོན་དང་མཆོད་རྟེན་ལ་རོལ་མོ་བྱས་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1810]
ཁ་ནས་རོལ་མོ་བྱེད་པ་ལ་ནི༌[^1569]ཡོངས་སུ་མ་རྫོགས་པ་ཉིད་ཀྱི་ཕྱིར་དེ་ལ་བྱས་པ་ལ་ནི་ཤིན་ཏུ་ན་སྨད་པའི་ཕྱིར་ཉེས་བྱས་ཕྲ་མོར་འགྱུར་རོ། །

[Block 1811]
བཤད་པ་བྱེད་པ་ཉིད་ན་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཆོས་བཤད་པ་དང་ཡོན་བཤད་པ་ལས་འདིར་ཀློག་པ་ཡིན་ཏེ། ཆོས་བཤད་པ་ལ་ཡང་འདི་ནི་མི་རིགས་པ་ཞེས་གསུངས་པ་དེའི་ཕྱིར་འདིར་བྱེ་བྲག་མི་སྐྱེད༌[^1570]པའོ། །

[Block 1812]
དེ་སོ་སོར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཡོན་བཤད་པ་ལའོ། །

[Block 1813]
འདིར་གཞུང་ནི་དགེ་སློང་རྣམས་ཀྱིས་ཡོན་བཤད་པར༌[^1571]བྱེད་པར་གྱུར་པ༌[^1572]དེ་ན་བཟའ་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1814]
དུས་ཡོལ་བར་འགྱུར་ན་ཚིགས་སུ་བཅད་པ་གཉིས་སམ་གསུམ་དུ་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་བཤད་པ་བྱེད་དུ་བཅུག་སྟེ། བཟའ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1815]
གལ་ཏེ་དྲོའི་དུས་ཡོལ་བར་དོགས་པ༌[^1573]ཡོད་ན། དེའི་ཚེ་ཚིགས་སུ་བཅད་པ་གཉིས་སམ་གསུམ་བཤད་པ་བྱེད་ཀྱི་བར་དུ་བཟའ་བར་མི་བྱའོ། །

[Block 1816]
རྐྱང་པ་འཆད༌[^1574]ན་ཚིག་གཉིས་སམ་གསུམ་འཆད༌[^1575]ཀྱི་བར་དུ་བཟའ་བར་མི་བྱ་བ་ཡང་འདིའི་རྗེས་སུ་འབྲངས་པས་ཤེས་པར་བྱའོ། །

[Block 1817]
གཞན་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1818]
ཟོས་ན་གཙུག་ལག་གི་ཚིགས་སུ་བཅད་པ་གདོན་ཏོ། །

[Block 1819]
ཟོས་ནས་མགྲོན་དུ་འབོད་པ་ལ་ཡོན་བཤད་པ་དང་ཆོས་བཤད་པ་དག་བྱའོ་ཞེས་བྱ་བ་ནི།

[Block 1820]
མདོ་སྡེའི་གཞུང་ལས།

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
--- END BLOCKS ---
