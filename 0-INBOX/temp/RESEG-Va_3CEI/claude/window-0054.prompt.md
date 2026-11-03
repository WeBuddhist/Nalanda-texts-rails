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

[Block 1896]
སངས་རྒྱས་བྱེ་བ་མང་ལ་བཀུར་སྟི་བྱས། །ཞེས་པ་ནས། བྱང་ཆུབ་དམ་པའི་མཆོག་ཀྱང་ཐོབ་པར་འོང་། །ཞེས་པའི་བར་དུ་ནི་རྒྱུའི་སྒོ་ནས་ལུང༌[^1586]བསྟན་པ་ལ་སྔོན་བཤེས་གཉེན་དམ་པ་ལ་བརྟེན་པ་དང་། བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་རྫོགས་པར་བྱས་པ་བསྟན་ཏོ། །

[Block 1897 [HEADING]]
###### **སངས་རྒྱས་སུ་འགྲུབ་པ།** ^4-3-4-2-4-2-2-2-0

[Block 1898]
མདོ་ལས།

[Block 1899 [HEADING]]
###### **བསྐལ་པའི་མིང།** ^4-3-4-2-4-2-2-2-1-0

[Block 1900]
ཚད་མེད་བསམ་གྱིས་མི་ཁྱབ་བསྐལ་པ་ན། །ཞེས་པ་ནས། །བལྟ་ན་སྡུག་པ་མེ་ཏོག་འབྲས་བུས་བརྒྱན། །ཞེས་པའི་བར་དུ་ནི་སངས་རྒྱས་སུ་འགྲུབ་པ་ཉིད་བསྟན་ཏེ། འདི་མན་ཆད་བསྐལ་པའི་མིང་བསྟན་པ་དང་། ཞིང་གི་རྒྱན༌[^1587]བསྟན་པ་དང་། འཁོར་བཟང་ངན་བསྟན་པ་དང་། སྐུ་ཚེའི་ཚད་བསྟན་པ་ལ་འདི་ནི་དང་པོའི་གཉིས་སོ། །

[Block 1901 [HEADING]]
###### **ཞིང་གི་རྒྱན།** ^4-3-4-2-4-2-2-2-2-0

[Block 1902]
ཕྱིའི་ཞིང་གི་རྒྱན་བསྟན་པ་ཡང་མིང་དང་དག་པའི་མཚན་ཉིད་དང་། ས་གཞི་དང་ལམ་དང་རིན་པོ་ཆེའི་ཤིང་དང་། མེ་ཏོག་དང་འབྲས་བུ་ལ་སོགས་པ་བསྟན་པའོ། །

[Block 1903 [HEADING]]
###### **འཁོར་བཟང་ངན།** ^4-3-4-2-4-2-2-2-3-0

[Block 1904]
མདོ་ལས།

[Block 1905]
དྲན༌[^1588]ལྡན་བྱང་ཆུབ་སེམས་དཔའ་དེ་མ་མང་། །ཞེས་པ་ནས། དེ་དག་སངས་རྒྱས༌[^1589]ཞིང་དེར་སྐྱེ་བར་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་འཁོར་གྱི་ཁྱད་པར་བསྟན་ཏེ་ཕྱིར་མི་ལྡོག་པ་སྤྲུལ་ཏེ་འོང་བ་དགེ་བའི་བཤེས་གཉེན་དང་བསྟེན་པ༌[^1590]རྒྱུ་དམ་པ་བསྐྱེད་པ་ཤ་སྟག་ཅེས་སྦྱར་རོ། །

[Block 1906 [HEADING]]
###### **སྐུ་ཚེའི་ཚད།** ^4-3-4-2-4-2-2-2-4-0

[Block 1907]
མདོ་ལས།

[Block 1908]
རྒྱལ་བ་དེ་ཡི་ཐ་མའི་ལུས་ཀྱི་ཚེ། །ཞེས་པ་ནས། དེ་དག་དེ་ན་ཚེ་ཡི་ཚད་དུ་གྱུར། །ཞེས་པའི་བར་དུ་ནི་སྐུ་ཚེའི་ཚད་དང་འཁོར་རྣམས་ཀྱི་ཚེའི་ཚད་དང་ཡང་དག་པ་དང་གཟུགས་བརྙན་གྱི་བསྟན་པ་ཡུན་ཇི་སྲིད་དུ་གནས་པ་རྣམས་སྟོན་ཏེ། སྐྱེ་བ་ཐམས་ཅད་ཀྱི་ཐ་མ་རྒྱལ་བུར༌[^1591]གྱུར་ཅིང་ཁྱིམ་ནས་བྱུང་བ་ཉིད་བླ་ན་མེད་པའི་བྱང་ཆུབ༌[^1592]འགྲུབ་པའི་དུས་བསྟན་ཏོ། །

[Block 1909]
མདོ་ལས།

[Block 1910]
རྒྱལ་བ་དེ་ནི་མྱ་ངན་འདས་ནས་ཀྱང་། །ཞེས་པ་ནས། ཟིལ་གྱིས་མི་ནོན་རྐང་གཉིས་གཙོ་བོ་སྟེ། །ཞེས་པའི་བར་དུ་ནི་དམ་པའི་ཆོས་དང་གཟུགས་བརྙན་གྱི་བསྟན་པ་ཇི་སྲིད་དུ་གནས་པ་དང་། བསྡུས་པ་བསྟན་ཏོ། །

[Block 1911 [HEADING]]
###### ལྷ་དང་མིས་མཆོད་ཅིང་བསྟོད་པ། ^4-3-4-2-5-0

[Block 1912]
མདོ་ལས་དེ་ནས་འཁོར་བཞིའི་དགེ་སློང་དང་ཞེས་པ་ནས་རང་རང་གི་གོས་བཅོམ་ལྡན་འདས་ལ་མངོན་དུ་གསོལ་ཏོ་ཞེས་པའི་བར་དུ་ནི་ལུང་བསྟན་པའི་ཚེ་ལྷ་རྣམས་ཀྱིས༌[^1593]མཆོད་པ་དང་བསྟོད་པ༌[^1594]བསྟན་ཏོ། །

[Block 1913 [HEADING]]
###### **འཁོར་བཞི་དང་བརྒྱད་ཀྱིས་མཆོད་པ།** ^4-3-4-2-5-1-0

[Block 1914]
སྔར་ནི་འཁོར་བཞི་དང་བརྒྱད་ཀྱིས༌[^1595]མཆོད། དེའི་འོག་ཏུ་ནི་ལྷ་རྣམས་ཀྱིས༌[^1596]མཆོད་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 1915]
གོས་ནི་འགེབས་པའི་དོན་ཏེ་བླ་ན་མེད་པའི་འབྲས་བུ་ཆེན་པོ་བརྙེས་པ༌[^1597]འགྲོ་བ་མང་པོ་ལ་ཐུགས་རྗེས་འགེབས་པའི་དོན་ཏམ། དམ་པའི་ཆོས་འདི་འཛིན་པ་དེ་བཞིན་གཤེགས་པའི་ན་བཟས་གཡོགས་པའོ༌[^1598]ཞེས་འབྱུང་བ༌[^1599]ཉིད་དང་ཡང་སྦྱར་རོ། །

[Block 1916 [HEADING]]
###### **ལྷ་རྣམས་ཀྱིས་མཆོད་པ།** ^4-3-4-2-5-2-0

[Block 1917]
མདོ་ལས་ལྷའི་དབང་པོ་བརྒྱ་བྱིན་དང་ཞེས་པ་ནས་འཕྲུལ་གྱི་གོས་མངོན༌[^1600]དུ་གསོལ་ཏོ་ཞེས་པའི་བར་དུ་ནི་ལྷ་རྣམས་ཀྱིས་མཆོད་པ་དང་བསྟོད་པ་བསྟན་ཏེ་མེ་ཏོག་མང་པོར་འཐོར་བ༌[^1601]ནི་དམ་པའི་ཆོས་འདི་དོན་རྟོགས་པར༌[^1602]སྟོན་པའོ། །

[Block 1918]
མདོ་ལས་འཕྲུལ་གྱི་མེ་ཏོག་དང་ཞེས་པ་ནས་བར་སྣང་ལ་བུན་ལོང་དུ་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་ངོ་མཚར་དུ་གྱུར་པ་བསྟན་ཏེ་བར་སྣང་ལ་གནས་པས་ཆོས་འདི་ཐོས་པས་འགྲོ་བ་རྣམ་བཞི་ལས་ཁྱད་པར་དུ༌[^1603]གྱུར་པ་བསྟན་ཏོ། །

[Block 1919]
མདོ་ལས་ལྷ་རྫས་ཀྱི་སིལ་སྙན་བརྒྱ་སྟོང་དང་ཞེས་པ་ནས་མངོན་པར་ཕབ་ནས་ཞེས་པའི་བར་དུ་ནི་ལྷའི་རོལ་མོས་མཆོད་པ་བསྟན་ཏེ་ཆོས་ཀྱི་སྒྲ་ཐོས་པས་དོན་རྟོགས་པའི་ཕྱིར་རོལ་མོ་སིལ་སྙན་གྱི༌[^1604]མཆོད་པ་བསྟན་ཏོ། །

[Block 1920 [HEADING]]
###### **མངོན་པར་བསྟོད་པ།** ^4-3-4-2-5-2-1-0

[Block 1921 [HEADING]]
###### **ཚིག་རྐྱང་པ།** ^4-3-4-2-5-2-1-1-0

[Block 1922]
མདོ་ལས་འདི་སྐད་སྨྲའོ་ཞེས་པ་ནས་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་ཏོ་ཞེས་པའི་བར་དུ་ནི་མངོན་པར་བསྟོད་པ་ཡང་ཚིག་རྐྱང་པ་དང་ཚིགས་སུ་བཅད་པ་དབྱེ༌[^1605]སྟེ་བསྟན་པ་གཞན༌[^1606]དག་ལ་ལྟོས་ནས༌[^1607]དྲང་བ་དང་ངེས་པའི་དོན་དུ་ལྡན་པའི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་འདི་ཉིད་བླ་ན་མེད་པའོ། །

[Block 1923 [HEADING]]
###### **ཚིགས་སུ་བཅད་པ།** ^4-3-4-2-5-2-1-2-0

[Block 1924]
མདོ་ལས།

[Block 1925 [HEADING]]
###### **སྔོན་བཤད་པའི་དོན་ཆུང་ད་འདིར་བཤད་པ་དོན་ཆེ་བ།** ^4-3-4-2-5-2-1-2-1-0

[Block 1926]
ལྷ་ཡི་སྲས་པོ་དེ་རྣམས་ཀྱི། །ཞེས་པ་ནས། འདི་ལ་གཞན་གྱིས་དད་པར་དཀའ། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་བདུན་ལ་བཞིར་དབྱེ་སྟེ་ཚིགས་བཅད་དང་པོ་གཉིས་ཀྱིས༌[^1608]སྔོན་བཤད་པའི་དོན་ཆུང་། ད་འདིར་བཤད་པ་ནི་དོན་ཆེ་བར་བསྟན་པ་དང་། དེའི་འོག་ཏུ་ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་དོན་དམ་པའི་ཆོས་ལ་རྗེས་སུ་ཡི་རང་བར་བསྟོད་པ་དང་། ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་གཞན་རྟོགས་པ་བསྐྱེད་པས་བདག་ཉིད་ཀྱང་སངས་རྒྱས་སུ་འགྲུབ་པར་བསྟན་པ་དང་། ཚིགས་བཅད་གཅིག་གིས་ནི་བསྔོ་བ་སྟོན་ཏེ་འདི་ནི་དང་པོའོ། །

[Block 1927]
ཕུང་པོ་ལྔའི་སྐྱེ་བ་དང་འཇིག་པ་སྨོས་པས་བདེན་པ་བཞིའི་དོན་སྟོན་ཏེ། དྲང་བའི་དོན་སྤང་ཞིང་ངེས་པའི་དོན་ལ་འཇུག་པ་བསྟན་པའོ། །

[Block 1928 [HEADING]]
###### **དོན་དམ་པའི་ཆོས་ལ་རྗེས་སུ་ཡི་རང་བར་བསྟོད་པ།** ^4-3-4-2-5-2-1-2-2-0

[Block 1929]
མདོ་ལས།

[Block 1930]
རྣམ་པར་འདྲེན་པས་དེང་བཤད་དོ། །ཞེས་པ་ནས། དཔའ་བོ་བདག་ཅག་རྗེས༌[^1609]ཡི་རང་། །ཞེས་པའི་བར་དུ༌[^1610]ནི་ཆོས་དམ་པ་ལ་རྗེས་སུ་ཡི་རང་ཞིང་སྤྱོད་པ་ཆེན་པོ་ལ་གཞོལ་བ་བསྟན་ཏོ། །
--- END BLOCKS ---
