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
[Block 1856 [HEADING]]
###### **ཕྱིའི་ཞིང་རྒྱན་དམ་པ་དང་ལྡན་པ།** ^4-3-4-2-4-2-1-2-0

[Block 1857]
མདོ་ལས་ཤཱ་རིའི་བུ་དེའི་ཚེ་ན་ཞེས་པ་ནས་ལྷ་དང་མི་མང་པོས་རབ་ཏུ་གང་ཞེས་པའི་བར་དུ་ནི་ཕྱིའི་ཞིང་རྒྱན་དམ་པ་དང་ལྡན་པ་སྟེ། [^1547]ཞིང་རྣམ་པར་དག་པའོ། །

[Block 1858]
དེ་ལ་ཡང་དགའ་བ༌[^1548]འབའ་ཞིག་གིས་བསྐྱེད་པའི་ཕྱིར་རྡུལ་མེད་པའི་ཕྱིར༌[^1549]ཞིང་ཞེས་བྱ་སྟེ། དྲི་མའི་སྐྱོན་མེད་པའོ། །

[Block 1859]
ང་རྒྱལ་གྱི་སེམས་སྤངས་པས༌[^1550]མཉམ་ཞིང་མཐོ་དམན་མེད་པ་དང་། སེམས་ཅན་གྱི་སེམས་རྣམ་པར་དག་པ་ཕྱིར་ཞིང་རྣམ་པར་དག་པ་རྒྱན་སྣ་ཚོགས་ཀྱིས་བརྒྱན་པ་དང་། གསོད་པ་དང་འཕྲོག༌[^1551]པའི་སེམས་དང་བྲལ་བའི་ཕྱིར་བདེ་བ་སྐྱིད་པ་ནད་དང་མུ་གེ་མེད་པའི་ཞིང་དང་། སྡིག་པའི་བཤེས་གཉེན་དང་བྲལ་བའི་ཕྱིར་ལྷ་དང་མིས༌[^1552]ཡོངས་སུ་རྒྱས་པའོ། །

[Block 1860]
མདོ་ལས་བཻ་ཌཱུརྱ་ལས་བྱས་པ་ཞེས་བྱ་བ་ནས་མེ་ཏོག་འབྲས་བུར་ལྡན་ནོ་ཞེས་པའི་བར་དུ་ནི་སེམས་ཀྱི་སྐྱོན་དང་བྲལ་བའི་ཕྱིར་ཞིང་བཻ་ཌཱུརྱ་ལྟར་རྣམ་པར་དག་པ་སྟོང་པ་བརྒྱད་ལ་གནས་ཤིང་འཕགས་པའི་ལམ་བརྒྱད་སྒྲུབ༌[^1553]པའི་ཕྱིར་གསེར་གྱི་ཐིག་གིས་ཕྱོགས་བརྒྱད་དུ་རེའུ་མིག་བྲིས༌[^1554]པའོ། །

[Block 1861]
གཟུངས་གཞི་ལ་གནས་པའི་ཕྱིར་སྐྱེད་མོས་ཚལ་དང་ལྡན་པ། བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན་སྤྱོད་པའི་ཕྱིར་རིན་པོ་ཆེའི་ཤིང་མེ་ཏོག་དང་། འབྲས་བུར་ལྡན་པའོ། །

[Block 1862 [HEADING]]
###### **ཆོས་སྟོན་པའི་ལུགས་གཅིག་པ།** ^4-3-4-2-4-2-1-3-0

[Block 1863 [HEADING]]
###### **ལུགས་མཐུན་པ།** ^4-3-4-2-4-2-1-3-1-0

[Block 1864]
མདོ་ལས་ཤཱ་རིའི་བུ་པདྨོའི་འོད་དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནས་ཐེག་པ་གསུམ་ཉིད་བརྩམས་ཏེ་ཆོས་སྟོན་ཞེས་པའི་བར་དུ་ནི་སྔོན་གྱི་དེ་བཞིན་གཤེགས་པ་དང་ཆོས་སྟོན་པའི་ལུགས་མཐུན་པ་བསྟན་པ་སྟེ། དེ་ལ་སྔར་ནི་ལུགས་མཐུན་པ་བསྟན། དེའི་འོག་ཏུ་ནི་དེའི་གཏན་ཚིགས་བསྟན་ཏེ། ཞིང་རྣམ་པར་དག་པ་ཞེས་སྨོས་པ་ཉིད༌[^1555]སྤྲུལ་པའི་ཞིང་དུ་ལྟའོ། །

[Block 1865 [HEADING]]
###### **ལུགས་མཐུན་པའི་གཏན་ཚིགས།** ^4-3-4-2-4-2-1-3-2-0

[Block 1866]
མདོ་ལས་གཞན་ཡང་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་སྨོན་ལམ་གྱི་དབང་གིས་ཆོས་སྟོན་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་དེའི་གཏན་ཚིགས་བསྟན་ཏེ། ཤཱཀྱ་ཐུབ་པ་དེ་བཞིན་གཤེགས་པ་ཡང་ཐབས་ལ་མཁས་པའི་སྨོན་ལམ་གྱི་དབང་གིས་འཇིག་རྟེན་རྙོག་པའི་དུས་སུ་བྱུང་ཞིང་ཆོས་སྟོན་པ་བཞིན་པདྨོའི་དེ་བཞིན་གཤེགས་པ་ཡང་སྔོན་གྱི་སྨོན་ལམ་གྱི་མཐུ་བཞིན་དྲང་བ་དང་ངེས་པའི་དོན་གྱི་སེམས་ཅན་རྣམས་ལ་ཆོས་སྟོན་ཏོ། །

[Block 1867 [HEADING]]
###### **བསྐལ་པའི་མིང་མི་མཐུན་པ།** ^4-3-4-2-4-2-1-4-0

[Block 1868]
མདོ་ལས་ཤཱ་རིའི་བུ་བསྐལ་པ་དེའི་མིང་ཞེས་པ༌[^1556]ནས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་རིན་པོ་ཆེ་ཞེས་བྱ་སྟེ་ཞེས་པའི་བར་དུ་ནི་བསྐལ་པ་མི་མཐུན་པ་བསྟན་པའོ། །

[Block 1869 [HEADING]]
###### **འཁོར་བཟང་ངན།** ^4-3-4-2-4-2-1-5-0

[Block 1870]
མདོ་ལས༌[^1557]དེའི་ཚེ་དེའི་དུས༌[^1558]ཞེས་པ་ནས་མང་པོར་བྱུང་སྟེ་ཞེས་པའི་བར་དུ་ནི་འཁོར་གྱི་ཁྱད་པར་བསྟན་ཏེ། དེ་ཡང་སོ་སོར་སྨོས་པ་དང་། སྤྱིར༌[^1559]བསྡུ་བ་ལ། དང་པོ་ལ་རྣམ་པ་བཅུ་སྟེ། འདི་ནི་གྲངས་དཔག་ཏུ་མེད་པ༌[^1560]ཇི་ལྟར་ཙན་དན་གྱི་ཚལ་ཙན་དན་གྱིས་བསྐོར་བ་བཞིན་ནོ། །

[Block 1871]
མདོ་ལས་དེ་བཞིན་གཤེགས་པས་བགྲངས་བ་ནི་ཞེས་པ་ནས་རིན་པོ་ཆེའི་པདྨོའི་སྟེང་ནས་འགྲོ་བ་ཞེས་པའི་བར་དུ་ནི་རིན་པོ་ཆེ་པདྨོའི་སྟེང་ནས་འགྲོ་བ་སྟོན་ཏེ། དེ་ཡང༌[^1561]སེམས་རྣམ་པར་དག་པ་དགུ་ལ་རྟག་ཏུ་གནས་པའི་ཕྱིར་ཏེ་རྣམ་པར་དག་པ་དགུ་ནི་ཚུལ་ཁྲིམས་དང་སེམས་དང༌[^1562]ལྡན་པ་དང་ཐེ་ཚོམ་དང་བྲལ་བ་དང་ལམ་ཤེས་པ་དང་སྤྱོད་པ་ཤེས་པ་དང་སྨོན་ལམ་ཤེས་པ་དང་། མི་དམིགས་པར་འགོག་པ་དང་ཞིང་རྣམ་པར་དག་པ་སྟེ་དགུ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1872]
དགེ་བའི་རྩ་བ་དམན་པ༌[^1563]ཤེ་དག་པ༌[^1564]ལས་ཐོབ་པ༌[^1565]མ་ཡིན་པའོ། །

[Block 1873]
མདོ་ལས་དགེ་བའི་རྩ་བ་ཡུན་རིང་པོ་ནས་སྤྱད་པ་ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པས་ཡོངས་སུ་བསྟོད་པ་ཞེས་པའི་བར་དུ་ནི་དེ་ཡང་ཡོན་ཏན་གཉིས་ཏེ། ཡུན་རིང་པོ་ནས་སྨོན་ལམ་ཆེན་པོ་བཏབ་པའི་དབང་གིས་ཐོས་པ་ཕུན་སུམ་ཚོགས་ཤིང་མང་པོ་ཀུན་གྱིས་ཤེས་པའི་ཕྱིར་སྟོན༌[^1566]པའོ། །

[Block 1874]
མདོ་ལས་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ལ་བརྩོན་པ་ཞེས་པ་ནས་ཞིང་དེ་ཡོངས་སུ་གང་བར་འགྱུར༌[^1567]ཞེས་པའི་བར་དུ་ནི་བླ་ན་མེད་པའི་མོས་པ་དང་ལྡན་པ། སྙིང་རྗེ་ཆེན་པོས་འགྲོ་བ་འདྲེན་པར་སེམས་པ་བསམ་པ་དག་པས་གཡོ་དང་སྒྱུ་མེད་པ། སེམས་སྤྱོད་པ་ཕྱིར་མ་ནུར་པ་ཉོན་མོངས་པ༌[^1568]མི་བསྐྱོད་པའི་ཕྱིར་དྲན་པ་དང་ལྡན་པ་དག་གིས་ཞིང་དེ་ཡོངས་སུ་གང་ཞེས་སྦྱར་རོ། །

[Block 1875 [HEADING]]
###### **ཆོས་གནས་པའི་ཡུན་རིང་ཐུང།** ^4-3-4-2-4-2-1-6-0

[Block 1876]
མདོ་ལས་ཤཱ་རིའི་བུ་འདི་ལྟར་ཡང་ཞེས་པ་ནས་བསྐལ་པ་བརྒྱད་དུ་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་དེའི་བསྟན་པ༌[^1569]གནས་པའི་ཡུན་རིང་ཐུང་ཡོད་པར༌[^1570]བསྟན་ཏེ། དེ་བཞིན་གཤེགས་པའི་སྐུ་ཚེའི་ཚད་དང་སྐྱེ་བ་དང་སངས་རྒྱས་སུ་གྲུབ་པ༌[^1571]ལུང་བསྟན་པ་དང་། བསྟན་པ་ཇི་སྲིད་དུ་གནས་པ་བསྟན་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 1877 [HEADING]]
###### **སྐུ་ཚེའི་ཚད།** ^4-3-4-2-4-2-1-6-1-0

[Block 1878]
བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པ་ནི་སེམས་ཅན་བསོད་ནམས་དང་ཤེས་རབ་ཆུང་བས་བཅོམ་ལྡན་འདས་ཀྱི་སྐུ་ཚེ་ཡང་ཐུང་བར་བསྟན་པདྨོའི་འོད་དེ་བཞིན་གཤེགས་པའི་ཞིང་ན་སེམས་ཅན་བཅོམ་ལྡན་འདས་ཀྱིས་མ་བསྟན་མ་བཤད་ཀྱང་དགེ་བ་ལ་རབ་ཏུ༌[^1572]རྩོལ་ཞིང་བསོད་ནམས་ཤེས་རབ་ཆེ་བ་ཤ་དག༌[^1573]པས་སྐུ་ཚེ་ཡང༌[^1574]རིང་བ་བསྟན་ཏོ། །

[Block 1879 [HEADING]]
###### **སངས་རྒྱས་སུ་གྲུབ་པ་ལུང་བསྟན་པ།** ^4-3-4-2-4-2-1-6-2-0

[Block 1880 [HEADING]]
###### **དུས།** ^4-3-4-2-4-2-1-6-2-1-0

[Block 1881]
མདོ་ལས་ཤཱ་རིའི་བུ་པདྨོའི་འོད་ཅེས་པ་ནས། བྱང་ཆུབ་ཏུ་ལུང་བསྟན་ནས་ཞེས་པའི་བར་དུ་ནི་མ་འོངས་པ་ན༌[^1575]སངས་རྒྱས་སུ་འགྲུབ་པ་བསྟན་པ་སྟེ། དེ་ཡང་དང་པོར་དུས་བསྟན། དེའི་འོག་ཏུ་དངོས་སུ་ལུང་བསྟན། དེའི་འོག་ཏུ་ཞིང་བསྟན་པའོ། །

[Block 1882 [HEADING]]
###### **དངོས་སུ་ལུང་བསྟན་པ།** ^4-3-4-2-4-2-1-6-2-2-0

[Block 1883]
མདོ་ལས་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ཏེ་ཞེས་པ་ནས་འཇིག་རྟེན་དུ་འབྱུང་ངོ་ཞེས་པའི་བར་དུ་དངོས་སུ་ལུང་བསྟན་ཏེ། དམ་པའི་ཆོས་འདི་ཐོས་པས་མངོན་པར་བྱང་ཆུབ་པའི་ཕྱིར་སྟོབས༌[^1576]བརྗིད་པ་པདྨ་འདོར་བ་ཉིད་དུ༌[^1577]ཁྱུ་མཆོག་གི་འགྲོས་ལྟ་བུར༌[^1578]དེ་བཞིན་གཤེགས་པར་འགྱུར་རོ། །

[Block 1884 [HEADING]]
###### **ཞིང།** ^4-3-4-2-4-2-1-6-2-3-0

[Block 1885]
མདོ་ལས་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་དེ་དག་འདྲ་བ་ཉིད་དུ་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པ་དེའི་ཞིང་པདྨོའི་དེ་བཞིན་གཤེགས་པའི་ཞིང་དང་འདྲ་བར་རྒྱུ་དམ་པ་ཉིད་ཀྱིས་བསྐྱེད་པའོ། །

[Block 1886 [HEADING]]
###### **བསྟན་པ་ཇི་སྲིད་དུ་གནས་པ།** ^4-3-4-2-4-2-1-6-3-0

[Block 1887]
མདོ་ལས་ཡང་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་གཟུགས་བརྙན་གནས་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདས་ནས་དེའི་བསྟན་པ་ཡུན་ཇི་སྲིད་དུ་གནས་པ་སྟོན་ཏེ། ཡང་དག་པའི་བསྟན་པ་ནི་ལུང་དང་སྤྱོད་པ་དང་མངོན་པར་གྲུབ་པ༌[^1579]དང་བཅས་པའོ། །

[Block 1888]
ཆོས་ཀྱི་གཟུགས་བརྙན་ནི་མངོན་པར་གྲུབ་པ༌[^1580]མེད་དེ། ལུང་དང་སྤྱོད་པ་ཙམ་དུ་ཟད་པ་ལ་བསྟན་པ་དེ་ཡང་མེད་པར་གྱུར་པའི་དུས་ན་ལུང་ཉི་ཚེ་བཞུགས་སོ། །

[Block 1889]
བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པའི་བསྟན་པ་ཡང་དག་པ་ནི་ཡུན་ཐུང་། ཆོས་ཀྱི་གཟུགས་བརྙན་རིང་སྟེ།[^1581] བུད་མེད་རབ་ཏུ་བྱུང་བ་ལས་ཡང་དག་པའི་བསྟན་པ་ལོ་ལྔ་བརྒྱས་ཐུང་བར་འགྱུར་རོ། །

[Block 1890]
པདྨོའི་འོད་དེ་བཞིན་གཤེགས་པའི་ཡང་དག་པའི་བསྟན་པ་དང་། ཆོས་ཀྱི་གཟུགས་བརྙན་དུས་མཉམ་པར་གནས་སོ། །

[Block 1891 [HEADING]]
###### **ཚིགས་སུ་བཅད་པ།** ^4-3-4-2-4-2-2-0

[Block 1892]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^1582]ཞེས་པ་ནས་སྲོག་ཆགས་བྱེ་བ་ཕྲག་སྟོང་རྣམ་པར་འདུལ་ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་ཕྱེད༌[^1583]དང་བཅུ་གཅིག་ལ་ཚིགས་བཅད་བཅུས་ནི་གོང་དུ་ལུང་བསྟན་པ་ལ་བཟླས༌[^1584]ཚིག་གཅིག་གིས༌[^1585]ནི་བསྡུས་ཏེ་དབྱེ་བའི་ཚུལ་གོང་མ་དག་དང་འདྲ་བར་སྦྱར་རོ། །

[Block 1893]
ཀུན་དུ་སྤྱན་ཞེས་པ་ནི་ཐམས་ཅད་མཁྱེན་པ་དང་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་གཉིས་དང་ལྡན་པའོ། །

[Block 1894 [HEADING]]
###### **རྒྱུའི་སྒོ་ནས་ལུང་བསྟན་པ།** ^4-3-4-2-4-2-2-1-0

[Block 1895]
མདོ་ལས།
--- END BLOCKS ---
