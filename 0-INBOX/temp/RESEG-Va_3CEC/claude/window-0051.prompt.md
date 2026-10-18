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
ངེས་པའི་ཚིག་ནི་གཞན་ལ་ཞེ་གཅོད་པའི་ཚིག་མི་སྨྲ་བའི་ཕྱིར་རོ། །

[Block 1787]
མི་གཡོ་བའི་ཚིག་ནི་མུ་སྟེགས་ཅན་ལ་སོགས་པས་སྤ་བཀོང་བར༌[^1554]མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1788]
ཡང་ན་འདུལ་བ་རྣམས་ཡོངས་སུ་སྨིན་པའི་དུས་ལས་མི་འདའ་བར་སྟོན་པས་ནི་མི་གཡོ་བའོ། །

[Block 1789]
བསྟོད་ཀྱང་འགྱིང་བའི་ཀུན་ནས་ཉོན་མོངས་པ་མི་སྐྱེ་བའི་ཕྱིར་མི་རྒོད་པའོ། །

[Block 1790]
སྨད་ཀྱང་ཞུམ་པའི་ཀུན་ནས་ཉོན་མོངས་པ་མི་སྐྱེ་བའི་ཕྱིར་ཞི་བའོ། །

[Block 1791]
སྐྱེ་བོ་ཐམས་ཅད་ཀྱིས་དེའི་ཚིག་ལ་བཙུན་པར་བྱེད་པའི་ཕྱིར་གཟུང་བའི༌[^1555]ཚིག་གོ། །

[Block 1792]
དེའི་ཚིག་ཐམས་ཅད་ཉན་པའི་ཕྱིར་བཙུན་པའི་ཚིག་གོ། །

[Block 1793]
ཚིག་དང་དོན་དུ་འབྲེལ་པའམ། མདོར་བསྟན་ནས་རྒྱས་པར་འཆད་པ་དང་བཅས་པའི་ཕྱིར་འབྲེལ་པའི་ཚིག་གོ། །

[Block 1794]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་དགེ་བའི་རྩ་བ་འཕེལ་ཞིང་རྒྱས་པར་བྱེད་པའི་ཕྱིར་ཐ་བ་མེད་པའི་ཚིག་གོ། །

[Block 1795]
ཚད་མ་གསུམ་དང་མི་འགལ་བའི་ཕྱིར་ཤིན་ཏུ་རིགས་པའི༌[^1556]ཚིག་གོ། །

[Block 1796]
སེམས་ཅན་དགེ་བའི་རྩ་བ་མ་བསྐྱེད་པ༌[^1557]རྣམས་ནི་སྐྱེད་པར་བྱེད། སྐྱེས་པ་རྣམས་ནི་འཕེལ་བར་བྱེད། འཕེལ་བ་རྣམས་ནི་སྨིན་པར་བྱེད་པས་ན། མ་ཚང་བ་མེད་པའི་ཚིག་གོ། །

[Block 1797]
དོན་བཟང་པོ་སྟོན་པས་ན་སྙན་པའི་ཚིག་གོ། །

[Block 1798]
ཡི་གེ་བཟང་པོ་སྟོན་པས་ན་མཉེན་པའི་ཚིག་གོ། །

[Block 1799]
ཇི་ལྟར་ཁས་བླངས་པ་ལས་གཞན་དུ་འགྱུར་བ་མེད་པས་ན་མ་སྨད་པའི་ཚིག་གོ། །

[Block 1800]
འཁོར་ཐམས་ཅད་ལ་ཕན་འདོགས་ཤིང་འཁོར་རྣམས་སྡུད་པར་བྱེད་པས་ན་ཤིན་ཏུ་སྡུད་པའི་ཚིག་གོ། །

[Block 1801]
ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་བསྟོད་པས་ན་འཕགས་པ་ཐམས་ཅད་ཀྱིས་རབ་ཏུ་བསྔགས་པའོ། །

[Block 1802]
ཞིང་མཐའ་ཡས་པས༌[^1558]འགྲོ་བར་བྱེད་པའི་རྗེས་སུ་སོང་བའི་དབྱངས་ཞེས་བྱ་བ་ནི་སྤོབས་པ་ལས་བྱུང་བའི་ཚིག་དེས་སངས་རྒྱས་ཀྱི་ཞིང་མཐའ་ཡས་པར་ཁྱབ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1803]
ཚངས་པའི་སྒྲ་སྐད་ལ་རྟོག་ཅིང་གོ་བར་བྱེད་པའི་དབྱངས་ཞེས་བྱ་བ་ལ་ཚངས་པ་ནི་མྱ་ངན་ལས༌[^1559]འདས་པ་ལ་བྱ་སྟེ། དེ་སྟོན་པའི༌[^1560]སྒྲ་སྐད་ལ་མཁས་པ་འམ། དེ་སྟོན་པར་བྱེད་པ་ལ་མཁས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1804]
སངས་རྒྱས་ཀྱིས་བཀའ་སྩལ་པ་ཞེས་བྱ་བ༌[^1561]ལ་སོགས་པས། བྱང་ཆུབ་སེམས་དཔའ་དེ་སངས་རྒྱས་རྣམས་ཀྱི་བཤད་པའི་སྤོབས་པ་དང་ལྡན་པས་སེམས་ཅན་རྣམས་ཀྱི༌[^1562]དབང་པོ་མཆོག་དང་མཆོག་མ་ཡིན་པར༌[^1563]ཤེས་པར་བྱས་ནས་དབང་པོ་དང་མཐུན་མཐུན་དུ་ཆོས་སྟོན་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1805]
དེའི་ཆོས་སྟོན་པ་ཡང་དེ་བྱེད་པར་ཡང་དག་པར་སྡུག་བསྔལ་ཟད་པར་བྱ་བའི་ཕྱིར་འབྱུང་བར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ལ་དེ་བྱེད་པ་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་ཟད་པར་བྱེད་པ་ལ་བྱ་སྟེ། བྱང་ཆུབ་སེམས་དཔའི་ཆོས་སྟོན་པའི་ཚིག་དེ་ནི༌[^1564]ཡང་དག་པར་སྡུག་བསྔལ་ཟད་པར་བྱ་བའི་ཕྱིར་འབྱུང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1806]
འདི་ནི་སྤོབས་པ་སོ་སོ་ཡང་དག་པར་རིག་པ་སྟེ། སོ་སོ་ཡང་དག་པར་རིག་པ་བཞི་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1807 [HEADING]]
## སློབ་པར་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^6-0

[Block 1808]
སློབ་པར་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟན་པའི་ཕྱིར༌[^1565]བཙུན་པ་ཤ་ར་དྭ༌[^1566]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སྟོན་པ༌[^1567]བཞི་ཡང་མི་ཟད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་མི༌[^1568]ཟད་པ་ཡང་རྟེན་པར༌[^1569]བྱེད་པའི༌[^1570]དོན་དང་ཡེ་ཤེས་དང་ངེས་པའི་དོན་དང་། ཆོས་ཉིད་མི་ཟད་པའི་ཕྱིར་རོ། །

[Block 1809]
འདིར་ཡང་བསྟན་པ་དང་བཤད་པའི་ཚུལ་རིག་པར་བྱ་སྟེ། བཞི་གང་ཞེ་ན་འདི་ལྟ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་བསྟན་པའི་ཚུལ་ལོ། །

[Block 1810]
ལྷག་མ་རྣམས་ནི་བཤད་པའི་ཚུལ་ལོ། །

[Block 1811]
རྟོན་པ་བཞིའི་དོན་ཤེས་ཏེ། དོན་ལ་སོགས་པ་ལ་རྟོན་པར་གྱུར་ན་གོང་དུ་བསྟན་པ་ལྟ་བུའི་སོ་སོ་ཡང་དག་པར་རིག་པར༌[^1571]འབྱུང་བས། རྟོན་པ་བཞིས་བསྡུས་པའི་དོན་དེའི་ཐབས་ཤེས་པ་བསྟན་པར་སྦྱར་རོ། །

[Block 1812]
སློབ་པར་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམ་པ་བཞི༌[^1572]སྟེ། ཆོས་ཤིན་ཏུ་ཚོལ་བ་དང་། བསམ་པ་ཤིན་ཏུ་ཚོལ་བ་དང་། ནན་ཏན་སྙིང་པོར་བྱེད་པ་དང་། གཞན་གྱི༌[^1573]དྲིང་ལ་མི༌[^1574]འཇོག་པའོ། །

[Block 1813 [HEADING]]
### ཆོས་ཤིན་ཏུ་ཚོལ་བ། ^6-1-0

[Block 1814]
ཆོས་ཤིན་ཏུ་ཚོལ་བའི་དབང་དུ་བྱས་ནས། དེ་ལ་དོན་ནི་གང་། ཚིག་འབྲུ་ནི་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1815]
གང་འཇིག་རྟེན་པའི་ཆོས་དང་བྱ་བ་ལ་འཇུག་པ་བསྟན་པའོ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གྱི་ཆོས་ལས་དང་འབྲས་བུ་ལ་སོགས་པ་ཐ་སྙད་དུ་གདགས་ཤིང་བརྗོད་པར་བྱ་བ་རྣམས་བསྟན་པ་ལ་ཚིག་འབྲུ་ཞེས་བྱའོ། །

[Block 1816]
དོན་ཞེས་བྱ་བ་ནི་གང་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་རྟོགས་པའོ་ཞེས་བྱ་བ་ལས་དང་འབྲས་བུ་ལ་སོགས་པ་འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་གདགས་པའི་ཆོས་རྣམས་ལས་འདས་ཏེ་དེ་དག་གི༌[^1575]མཚན་མ་རྣམས་དང་བྲལ་བ་སྟོང་པའི་དོན་རྟོགས་པ་ལ་དོན་ཞེས་བྱའོ། །

[Block 1817]
དེ་བཞིན་དུ་འོག་མ་རྣམས་ལ་ཡང་གར་རིགས༌[^1576]པར་སྦྱར་ཏེ་མདོར་ན་ཇི་ཙམ་དུ་ཀུན་རྫོབ་ཀྱི་ཆོས་རྣམས་བཤད་ཅིང་འབྲེལ་པ༌[^1577]ལ་ནི་ཚིག་འབྲུ་ཞེས་བྱའོ། །

[Block 1818]
དེ་ལས་བཟློག་སྟེ་བཤད་པ་དང་བརྗོད་པ་ལ་སོགས་པ་ལས་འདས་ཤིང་དོན་དམ་པའི་དབྱིངས་ཉིད་དུ་རྟོགས་པ་ལ་དོན་ཞེས་བྱའོ། །

[Block 1819]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་སྦྱིན་པ༌[^1578]དང་དུལ་བ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཕྱི་དང་ནང་གི་དངོས་པོ་སྦྱིན་པ་བསྟན་ཅིང་བཤད་པ་དང་། མིག་ལ་སོགས་པའི་དབང་པོ་རྣམས་ཡུལ་ལ་མི་འཇུག་པར་དུལ་བ་བསྟན་པ་དང་། ལུས་དང་ངག་དང་ཡིད་ཀྱི་སྒོ་ནས་སྡིག་པ་མི་བྱེད་པར་སྡོམ་པ་བསྟན་པ་དང་། གཞན་ལ་གནོད་པ་མི་བྱེད་པར་ངེས་པ་བསྟན་ཅིང་བཤད་པ་ནི་ཚིག་འབྲུ་ཞེས་བྱའོ། །

[Block 1820]
མཉམ་པ་ཉིད་ཤེས་པའོ་ཞེས་བྱ་བ་ནི་ཆོས་དེ་དག་རང་བཞིན་མེད་པར་ཤེས་པའམ། ཆོས་དེ་དག་གིས༌[^1579]སྟོང་པ་ཉིད་ཤེས་པ་ནི་དོན་ཞེས་བྱའོ། །

[Block 1821]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་འཁོར་བའི་སྐྱོན་བསྒྲགས་ཤིང་བརྗོད་པའོ་ཞེས་བྱ་བ་ལ་ཕུང་པོ་གཅིག་ནས་གཅིག་ཏུ་ཚེའི་ཉིང་མཚམས་སྦྱོར་ཞིང་སྐྱེ་བ་ནི་འཁོར་བའོ། །

[Block 1822]
འཁོར་བའི་སྐྱོན་ནི་འཁོར་བའི་ཉེས་པ་སྟེ། རྒ་བ་དང་འཆི་བ་ལ་སོགས་པའི་སྡུག་བསྔལ་མང་པོ་དང་ལྡན་པ་སྟེ། དེ་ལྟར་འཁོར་བའི་སྐྱོན་བསྒྲགས་ཤིང་འཆད་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1823]
དོན་ཞེས་བྱ་བ་ནི༌[^1580]འཁོར་བ་ལ་མི་དམིགས་པར་རྟོགས་པའོ༌[^1581]ཞེས་བྱ་བ་ལ་ཉེས་པ་དུ་མའི་གནས་སུ་གྱུར་པའི་འཁོར་བ་དེ་ཡང་རང་བཞིན་གྱིས་སྟོང་ཞིང་མེད་པར་ཁོང་དུ་ཆུད་པ་ནི་དོན་ཞེས་བྱའོ། །

[Block 1824]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་མྱ་ངན་ལས་འདས་པའི་ཡོན་ཏན་དང་ཕན་ཡོན་བརྗོད་ཅེས་བྱ་བ་ལ། ཉོན་མོངས་པ་མ་ལུས་པར་སྤངས་ནས་ཚེ་གཅིག་ནས་གཅིག་ཏུ་ཉིང་མཚམས༌[^1582]སྦྱོར་བའི་རྒྱུན་ཆད་པ༌[^1583]ནི་མྱ་ངན་ལས༌[^1584]འདས་པའོ། །

[Block 1825]
མྱ་ངན་ལས་འདས་པའི་ཡོན་ཏན་ནི་ཞི་བ་དང་གྱ་ནོམ་པ་དང་། ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
