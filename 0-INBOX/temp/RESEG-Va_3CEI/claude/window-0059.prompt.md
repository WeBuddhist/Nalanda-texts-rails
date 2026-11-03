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
[Block 2066]
ཐུགས་རྗེས་དགོངས་པ་གཉིས་སུ་མི་མཛད་པའི་ཕྱིར་སྙོམས་པའོ། །

[Block 2067]
མདོ་ལས་བདག་ཀྱང་བང་མཛོད་མང་གི་ཞེས་པ་ནས་བདག་གི་བུ་རྣམས་ལྟ་ཅི་སྨོས་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཐུགས་རྗེ་ཆེན་པོ་དང་ལྡན་པས་འགྲོ་བ་ལྔར་སྐྱེས་པའི༌[^1718]སེམས་ཅན་ཐམས་ཅད་དང་རིགས་མེད་པ་དང་རིགས་ངེས་པ་རྣམས་ལ་ཡང་སྙོམས་པར་སྟོན་ན་ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་དང་རིགས་མ་ངེས་པ་རྣམས་ལ་ལྟ་ཅི་སྨོས་ཞེས་པའི་དོན་ཏོ། །

[Block 2068 [HEADING]]
###### **བུས་པ་རྣམས་ཀྱི་བསམ་པ་དང་འགལ་བ།** ^4-3-5-4-1-1-2-4-0

[Block 2069]
མདོ་ལས་དེའི་ཚེ་བྱིས་པ་དེ་དག་ཀྱང་ཞེས་པ་ནས་དེ་ཇི་སྙམ་དུ་སེམས་ཞེས་པའི་བར་དུ་ནི་བུ་རྣམས་ཀྱིས༌[^1719]སྔར་བསམ་པའི་རེ་བ་ལས་འགལ་བ་བསྟན་ཏེ། སྔར་ཐེག་པ་རྣམ་གསུམ་བསྟན་ལ་ཕྱིས་ཐེག་པ་ཆེན་པོ་འབའ་ཞིག་བསྟན་པས། འགལ་ཞེས་པའི་དོན་ཏོ། །

[Block 2070 [HEADING]]
###### **ཐེ་ཚོམ་དགྲོལ་བའི་དཔེ།** ^4-3-5-4-1-1-3-0

[Block 2071]
མདོ་ལས་སྐྱེས་བུ་དེས་བྱིས་པ་དེ་དག་ལ་ཞེས་པ་ནས། དེ་བརྫུན༌[^1720]དུ་སྨྲས་པར་མི་འགྱུར་རམ་ཞེས་པའི་བར་དུ་ནི་སྔར་ནི་ངེས་པའི་དོན་གྱི་དཔེ་བསྟན་ཕྱིས༌[^1721]ཐེ་ཚོམ་དགྲོལ་བའི་དཔེ་བསྟན༌[^1722]ཏེ་གོང་དུ་བཅོམ་ལྡན་འདས་ནི་བདེན་པར་གསུང་བ་ཡང་དག་པ་ཉིད་དུ་གསུང་པའོ་ཞེས་འབྱུང་བ༌[^1723]ལ་ཐེག་པ་རྣམ་གསུམ་བསྟན་པ་འདིར་ཐེག་པ་ཆེན་པོ་གཅིག་ཏུ་བསྡུས་ན་གསུང་དམ་པར་གྱུར་ཅེས་པའི་དོན་ཏོ། །

[Block 2072]
མདོ་ལས་ཤཱ་རིའི་བུས་གསོལ་པ། བཅོམ་ལྡན་འདས་དེ་ལྟ་མ་ལགས་སོ༌[^1724]ཞེས་པ་ནས་སྲོག་དང་ལྡན་པར་བགྱིས་པའི་སླད་དུའོ་ཞེས་པའི་བར་དུ་ནི་དྲིས་པའི༌[^1725]ལན་བཏབ་པ་སྟེ། སྔར་གླེང་བ་དང་ཕྱིས་དགྲོལ༌[^1726]བའོ། །

[Block 2073]
ཉོན་མོངས་པ་ལས་སྟོན་པ་དང་ངན་འགྲོ་གསུམ་ལས་ཐར་པར་བྱས་པ་ནི་སྲོག་དང་ལྡན་པར་བྱས་པའོ། །

[Block 2074]
མདོ་ལས་དེ་ཅིའི་སླད་དུ་ཞེ་ན་ཞེས་པ་ནས་སྐྱེས་བུ་དེ་ཤོ་བེ་མཆི་བར་མི་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་ཁམས་གསུམ་འབར་བའི་ཁང་པ་དང་འདྲ་བ་ལས་ཐར་བར་བྱས་པའི་ཕྱིར་བརྫུན༌[^1727]དུ་མི་འགྱུར་བ་དང་། སྐྱེས་བུ་དེ་ཐབས་མཁས་པ་དང་ལྡན་པས། ཆེན་པོ་སྦྱིན་པའི་བསམ་པས༌[^1728]ཆུང་ངུར་བརྗོད་དེ་ཆེན་པོ་ཐོབ་པར་བྱས་པས་འགལ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2075]
མདོ་ལས་དེ་ཅིའི་སླད་དུ་ཞེ་ན་བཅོམ་ལྡན་འདས་སྐྱེས་བུ་དེ་ཤོ་བེ་མཆི་བ་མ་ལགས་སོ་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོ་བསྟན་པའི་ཕྱིར་བརྫུན༌[^1729]དུ་མི་འགྱུར་བ་བསྟན་པའོ། །

[Block 2076]
མདོ་ལས་དེ་སྐད་ཅེས་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་ལ་འདི་སྐད་ཅེས་བཀའ་སྩལ་ཏོ། །

[Block 2077]
ཤཱ་རིའི་བུ༌[^1730]ལེགས་སོ་ལེགས་སོ། །

[Block 2078]
དེ་དེ་བཞིན་ཏེ། ཇི་སྐད་སྨྲས་པ༌[^1731]བཞིན་ནོ་ཞེས་པ་ནི་དོན་དེ་ཉིད་ཡིན་པར་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་བསྟན་པར་བྱས་སོ།[^1732] །

[Block 2079 [HEADING]]
###### **དོན།** ^4-3-5-4-1-2-0

[Block 2080]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་བཞིན་དུ་ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་དང་ཞེས་པའི་བར་དུ་ནི་དཔེ་དག་ཀྱང་སྔ་མ་ནི་དྲང་བའི་དོན་གྱི༌[^1733]དཔེ། ཕྱི་མ་ནི་ངེས་པའི་དོན་དང་སྦྱར་བའོ། །

[Block 2081 [HEADING]]
###### **དྲང་བའི་དོན་དང་སྦྱར་བ།** ^4-3-5-4-1-2-1-0

[Block 2082]
དེ་ལ་དེའི་གནས་དང་ཁྱིམ་བདག་དང་། རྒན༌[^1734]དང་འབྱོར་པ་དང་། ཁྱིམ་གྱི་རྟགས་དང་། སྒོ་དང་།[^1735] དྲུག་གཅིག་ཅིག་སྟོན་ཏེ། འཇིག་རྟེན་ཞེས་པ་ནི་གནས་སོ། །

[Block 2083]
ཁྱིམ་བདག་ཅེས་པ་ནི་བདག་པོའོ། །

[Block 2084]
འཇིག་རྟེན་ཡང་སྣོད་དང་བཅུད་དུ་དབྱེའོ། །

[Block 2085]
འཇིགས་པ་ཐམས་ཅད་བསལ་བ་ཞེས་པ་ནི་འབྱོར་པ་བསྟན་ཏེ། འཇིགས་པ་ནི་རྣམ་པ་ལྔ་སྟེ། འཚོ་བ་མི་འབྱོར་བས་འཇིགས་པ་དང་། གཏམ་ངན་གྱིས༌[^1736]འཇིགས་པ་དང་། འཆི་བས་འཇིགས་པ་དང་། ངན་སོང་གིས་འཇིགས་པ་དང་། འཁོར་གྱི་ནང་དུ་སྤ་གོང༌[^1737]བས་འཇིགས་པའོ། །

[Block 2086]
འཆི་བ༌[^1738]དང་འཁྲུག་པ་ཞེས་པ་ནི་མི་བདེ་བའི་སྡུག་བསྔལ་སྣ་ཚོགས་སོ། །

[Block 2087]
དེ་དག་ནི་འཁོར་བའི་འཇིགས་པ་དང་སྦྱར་རོ། །

[Block 2088]
ཡིད་མི་བདེ་བ་དང་། མ་རིག༌[^1739]པ་ལ་སོགས་པ་ནི་ཉོན་མོངས་པའི་རྩ་བ་གཏི་མུག་སྟེ་སྡུག་བསྔལ་གྱི་རྒྱུ་ཡིན་པས་དུག་གསུམ༌[^1740]དང་སྦྱར་རོ། །

[Block 2089]
ཡང་ན་དཀོན་མཆོག་གསུམ་མ་རིག་པ་ཡང་སྦྱར་རོ། །

[Block 2090]
ཉོན་མོངས་པ་དེ་དག་མ་ལུས་པ་སྤངས་པས་ཡོན་ཏན་ཐམས་ཅད་དང་ལྡན་པའི་དེ་བཞིན་གཤེགས་པ་ཉིད་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཕ་ཡིན་པར༌[^1741]སྦྱར་རོ། །

[Block 2091]
མདོ་ལས་སྟོབས་དང་མི༌[^1742]འཇིགས་པ་ཞེས་པ་ནས་ཡེ་ཤེས་དམ་པའི་མཆོག་ཐོབ་པ་ཞེས་པའི་བར་དུ་ནི་འབྱོར་པ་བསྟན་ཏོ། །

[Block 2092]
སྟོབས་དང་མི་འཇིགས་པ་དང་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་ལ་སོགས་པ་ནང་གི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པའི་ཕྱིར་ཕྱུག་ཅིང་ནོར་མང་བ་ལྟ་བུར་བསྟན་ཏོ། །

[Block 2093]
རྫུ་འཕྲུལ་ནི་བྲན་གཡོག༌[^1743]འཁོལ་བ་དང་འདྲ་བར་དེས་དབང་དང་སེམས་ཅན་གྱི་དོན་བྱེད་པའོ། །

[Block 2094]
མདོ་ལས་སྙིང་རྗེ་ཆེན་པོ་མི་སྐྱོ་བའི་ཡིད་ཀྱིས་ཕན་པར་འདོད་པ་ཞེས་པ་ནས་ཞིག་པའི་ཁང་པ་དང་འདྲ་བར་སེམས་ཅན་ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་ལ་ཕན་འདོགས་པ་ལ་ཐུགས་རྗེ་ཆེན་པོ་སྐྱོ་མི་མཁྱེན་པར་བསྟན་པ་སྟོན་ཏེ། སྤོང་པ་ཕུན་སུམ་ཚོགས་པ་དང་། ཡེ་ཤེས་ཕུན་སུམ་ཚོགས་པས༌[^1744]བདག་དང་གཞན་གྱི་དོན་རྫོགས་པར་མཛད་པ་དང་། ཁང་པ་མེ་འབར་བ་དང༌[^1745]འདྲ་བར༌[^1746]ཁམས་གསུམ་གྱི་སེམས་ཅན་འགྲོ་བ་ལྔར་སྐྱེ་བ་རྣམས་ལ་ཕན་འདོགས་ཤིང་འཇིག་རྟེན་དུ་གཤེགས་ཏེ།[^1747] དེ་ལས་བྱུང་བ་བསྟན་པས་ཐེག་པ་རྣམས་གཅིག་གི༌[^1748]དོན་སྤྱོད་པ་ལ་གཟུད་པར་ཐབས་མཁས་པ་ཆེན་པོས་ཕན་འདོགས་པ་བསྟན་པའོ། །

[Block 2095]
མདོ་ལས་སྐྱེ་བ་དང་རྒ་བ་དང་། ན་བ་དང་། འཆི་བ་ཞེས་པ་ནས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་གཟུད་པའི་ཕྱིར་འབྱུང་སྟེ་ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་འགྲོ་བ་ལྔར་སྐྱེས་པ་རྣམས་འཁོར་བ༌[^1749]གཡང་ཟ་བ་ན་གནས་པའི་དཔེ་སྟེ། དེ་ཡང་དེ་ན་རབ་ཏུ་མང་བར་གནས་པ་དང་། ཁང་ཁྱིམ་ཞིག་པ་དང་། ཕྱོགས་ཐམས་ཅད་ནས་མེ་འབར་བ༌[^1750]བུས་པ་རྣམས་དེ་ན་གནས་པར་སྟོན་པ་ལ་རབ་ཏུ་མང་བ་གནས་པའི་སེམས་ཅན་མང་པོ་ཞེས་པའི་དོན་ཏོ། །

[Block 2096]
སྐྱེ་བ་དང་རྒ་བ་དང་ན་བ་དང་འཆི་བ་ལ་སོགས་པ་ནི་ཁང་པ་རྙིང་པ་དང་འདྲ་བར༌[^1751]སྦྱར་རོ། །

[Block 2097]
མ་རིག་པའི་མུན་པ་ཞེས་པ་ལ་སོགས་པ་ནི་གདུག་པ་གསུམ་གྱི་མེ་ཕྱོགས་བཞི་ནས་འབར་བ་བསྟན་ཏོ། །

[Block 2098]
བྱང་ཆུབ་ལ་གཟུད༌[^1752]ཅེས་པ་ནི་བུ་རྣམས་ལ་ཐུགས་རྗེ་སྐྱེ་ཞིང་ཉོན་མོངས་པའི་གནས་ནས་འདོན་ཞེས་པའོ། །

[Block 2099]
ཕུང་པོ་བཞི་ལ་མི་རྟག་པ་ལ་སོགས་པས་འཇོམས་པ་དང་། སྐྱེ་རྒ་ན་འཆིས་རྙིངས་པར་བྱེད་པ་ནི་ཁང་པ་རྙིངས་པ་ལྟ་བུའོ། །

[Block 2100]
མདོ་ལས་དེ་བྱུང་མ་ཐག་ཏུ་སེམས་ཅན་རྣམས་ཞེས་པ་ནས་སྡུག་བསྔལ་རྣམ་པ་མང་པོ་རབ་ཏུ་མྱོང་བ་ཞེས་པའི་བར་དུ་ནི་དེ་ཡང་བཅོམ་ལྡན་འདས་ཐུགས་རྗེ་སྐྱེ་བ་སྟོན་པ་ལ་ཐུགས་རྗེ་སྐྱེ་བ་དང་། ཐུགས་རྗེ་སྐྱེ་བའི་དངོས་པོ་རྣམ་གཉིས་སྟོན་ཏེ། སེམས་ཅན་རྣམས་ཞེས་པ་ནི་ཐུགས་རྗེ་སྐྱེའོ། །

[Block 2101]
སྐྱེ་རྒ༌[^1753]ན་འཆི་བ༌[^1754]ལ་སོགས་པ་ནི་ཐུགས་རྗེ་སྐྱེ་བའི་དངོས་པོའོ། །

[Block 2102]
དེ་འདྲ་བའི་སྡུག་བསྔལ་སྣ་ཚོགས་པ༌[^1755]ལ་སེམས་ཅན་འདི་དག་གནས་སོ་ཞེས་བཅོམ་ལྡན་འདས་ཐུགས་རྗེ་སྐྱེ་བའོ། །

[Block 2103]
དེ་ཡང་སྔར་ནི་འདོད་པའི་ཁམས་ཀྱི་སྡུག་བསྔལ་བདུན་བསྟན། སྡུག་བསྔལ་རྣམ་པ་མང་པོ་ཞེས་པ་ནི་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་ཀྱི་སྡུག་བསྔལ་བསྟན་ཏོ། །

[Block 2104]
འདོད་པའི་ཁམས་ཀྱི་སྡུག་བསྔལ་ཡང་འདུ་བྱེད་ཀྱི་མཚན་ཉིད་བཞིས་འཇོམས་པ་དང་། འདོད་པ་རྣམ་ལྔས་བསྲེགས་པ༌[^1756]དང་རྒྱུད་རྣམས་སུ་འཁོར་བའོ། །

[Block 2105]
དེ་ཡང་སྔ་མ་གསུམ་ནི་ཚེ་འདིའི་སྡུག་བསྔལ་ལོ། །
--- END BLOCKS ---
