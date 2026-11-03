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
མདོ་ལས།

[Block 1787]
ཐོག་མར་རྣམ་པར་འདྲེན་གྱི་གསུང་ཐོས་ནས། །ཞེས་པ་ནས། གང་ཚེ་རྒྱུ་དང་གཞི་ཡི་རྣམ་པ་དང་། །ཞེས་པའི་བར་དུ་ནི་ཐེ་ཚོམ་དངོས་སུ་བསལ་བ་བསྟན་ཏེ། དེ་ལ་ཡང་དང་པོའི་ཚིགས་བཅད་འདིས་ནི་ཐེ་ཙོམ་སྐྱེ་བའི་གཏན་ཚིགས་བསྟན། འོག་མ་ཕྱེད་དང་དྲུག་གིས་ནི་ཐེ་ཙོམ་དངོས་སུ་བསལ་བ་བསྟན་ཏོ། །

[Block 1788]
སྔོན་བཅོམ་ལྡན་འདས་ཀྱིས༌[^1492]ཐེག་པ་རྣམ་པ་གསུམ་བཤད་དེ། དེ་སོ་སོའི་འབྲས་བུ་ཡང་ཐོབ་པའི་རྗེས་ལ་ད་ཐེག་པ་གཅིག་གོ་ཞེས་གསུངས་པ་འདི་སྔར་གསུངས་པ་དང་མི་འགལ་བའི་ཕྱིར་གཞུང་ལ་ཐེ་ཚོམ་མེད་ཀྱང་སྨྲ་བའི་ཚིག་འདི་བདུད་ཀྱིས་བཤད་པ་མ་ཡིན་ནམ་ཞེས་ཐེ་ཚོམ་དུ་གྱུར་པའོ། །

[Block 1789 [HEADING]]
###### **དངོས་སུ་ཐེ་ཚོམ་བསལ་བ།** ^4-3-4-1-2-2-4-1-2-3-0

[Block 1790]
མདོ་ལས།

[Block 1791 [HEADING]]
###### **ཐབས་མཁས་པས་དཔེ་དང་དོན་གསལ་བའི་ཕྱིར་ཐེ་ཚོམ་དང་བྲལ་བ།** ^4-3-4-1-2-2-4-1-2-3-1-0

[Block 1792]
དཔེ་རྣམས་བྱེ་བ་ཁྲག་ཁྲིག་སྙེད་ཀྱིས་བསྟན། །ཞེས་པ་ནས། དེ་ནས་བདག་ནི་ཆོས་ཐོས་ཐེ་ཚོམ་བྲལ། །ཞེས་པའི་བར་དུ་ནི་ཐེ་ཚོམ་དང་བྲལ་བ་དང༌[^1493]དངོས་སུ་བསྟན་པ་སྟེ། འདི་མན་ཆད་ཐབས་མཁས་པས་དཔེ་དང་དོན་གསལ་བའི༌[^1494]ཕྱིར་ཐེ་ཚོམ་དང་བྲལ་བ་དང་། དུས་གསུམ་གྱི་དེ་བཞིན་གཤེགས་པ་ཐབས་མཁས་པ་སྟོན་པ་མཐུན་པའི་ཕྱིར་ཐེ་ཚོམ་དང་བྲལ་བ་དང་། དེ་བཞིན་གཤེགས་པའི་གསུང་རབ་དང་། བདུད་ཀྱི་ཚིག་དང་མི་མཐུན་པའི་ཕྱིར་ཐེ་ཚོམ་དང་བྲལ་བ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 1793]
བཅོམ་ལྡན་འདས་ཆོས་སྟོན་པ་ཡང་དཔེའི་སྒོ་ནས་ཆོས་སྟོན་པ་དང་། དོན་དངོས་སུ་བསྟན་པའི་ཕྱིར་ཆོས་སྟོན་པ་ལ་དཔེ་དང་དོན་དུ་སྦྱར་བ་ལ་མི་འགལ་བའི་ཕྱིར་ཐེ་ཚོམ་དང་བྲལ་བའོ། །

[Block 1794 [HEADING]]
###### **དུས་གསུམ་གྱི་དེ་བཞིན་གཤེགས་པ་ཐབས་མཁས་པ་སྟོན་པ་མཐུན་པའི་ཕྱིར་ཐེ་ཚོམ་དང་བྲལ་བ།** ^4-3-4-1-2-2-4-1-2-3-2-0

[Block 1795]
མདོ་ལས།

[Block 1796]
དེ་ལྟར་བདག་ལ་སངས་རྒྱས་བྱེ་བ་སྟོང་། །ཞེས་པ་ནས། ཤིན་ཏུ་སྟོན་པར་འགྱུར་ཞིང་ད་ལྟར༌[^1495]འཆད། །ཞེས་པའི༌[^1496]བར་དུ་ནི་འདིས་དུས་གསུམ་གྱི་དེ་བཞིན་གཤེགས་པ་ཐབས་མཁས་པས་ཆོས་སྟོན་པ་ལ་ལུགས་མཐུན་པ་སྟོན་ཏེ། ཚིག་དང་པོ་ནི་འདས་པ་དང་སྦྱར། དེའི་འོག་མ་ནི་མ་འོངས་པ་དང་ད་ལྟར་གྱི་དང་སྦྱར་ཏེ། དུས་གསུམ་གྱི་དེ་བཞིན་གཤེགས་པ་ཆོས་སྟོན་པ་ལ་དྲང་བ་དང་ངེས་པའི་དོན༌[^1497]སྟོན་པ་གཞུང་ལུགས་མཐུན་པའི་ཕྱིར་ཐེ་ཚོམ་དང་བྲལ་བའོ། །

[Block 1797]
མདོ་ལས།

[Block 1798]
དེ་ལྟར་ཁྱོད་ནི་སྤྱོད་པ་ཅི་འདྲ་བ། །ཞེས་པ༌[^1498]ནས། ཆོས་ཀྱི་འཁོར་ལོ་ཅི་འདྲ་ཁྱོད་ཀྱིས་མཁྱེན། །ཞེས་པའི་བར་དུ་ནི་དུས་གསུམ་གྱི་སངས་རྒྱས་ཀྱང་མཚུངས་པའི་སྒོ་ནས་ཐེ་ཚོམ་བྲལ་བ་སྟོན་ཏེ།

[Block 1799]
དང་པོ་བལྟམས་པ་དང་ཁབ་ནས་བྱུང་བའི་བར་དུ་ནི་སྐུའི་སྤྱོད་པ་བསྟན་ཏོ། །

[Block 1800]
འཕགས་པའི་ལམ་བརྙེས་པས་ནི་ཐུགས་ཀྱི་སྤྱོད་པ་བསྟན་ཏོ། །

[Block 1801]
ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བས་ནི་གསུང་གི་སྤྱོད་པ་བསྟན་ཏོ། །

[Block 1802]
དེ་ལྟར་སྟོན་པ་ལ་འཁྲུལ་པ་དང་འགལ་བ་མེད་པའི་ཕྱིར་ཐེ་ཚོམ་བསལ་ཏོ། །

[Block 1803 [HEADING]]
###### **དེ་བཞིན་གཤེགས་པའི་གསུང་རབ་དང་བདུད་ཀྱི་ཚིག་དང་མི་མཐུན་པའི་ཕྱིར་ཐེ་ཚོམ་དང་བྲལ་བ།** ^4-3-4-1-2-2-4-1-2-3-3-0

[Block 1804]
མདོ་ལས།

[Block 1805]
ཇི་ལྟར་ཁྱོད་ཀྱིས༌[^1499]ཆོས་བཤད་གནས་པ་ལས། །ཞེས་པ་ནས། བདག་ཉིད་དེ་ལྟར་སེམས་ལ་ཐེ་ཚོམ་སྐྱེས། །ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པའི་གསུང་རབ་དང་། བདུད་ཀྱི་ཚིག་མི་འདུ་བ༌[^1500]ལས་ཐེ་ཚོམ་དང་བྲལ་བ༌[^1501]བསྟན་ཏོ། །

[Block 1806 [HEADING]]
###### **ཤིན་ཏུ་བདེ་བ་ཐོབ་པ།** ^4-3-4-1-2-2-4-2-0

[Block 1807]
མདོ་ལས།

[Block 1808]
གང་ཚེ་འཇམ་ཞིང་ཟབ་མོ་སྙན་པ་ཡི། །ཞེས་པ་ནས། ཐེ་ཚོམ་དང་བྲལ་ཡེ་ཤེས་གནས། །ཞེས་པའི་བར་དུ་ནི་འདིས་ཉོན་མོངས་པ་ཟད་པས་དགའ་བ་སྐྱེ་བ་བསྟན་ཏེ། ཐུགས་རྗེས་འདྲེན་པའི་གསུང་ནི་འཇམ་པའོ། །

[Block 1809]
འབྲུག་སྒྲ་ལྟ་བུས་རྒྱང་དུ་ཐོས་པར་བྱེད་པ་ནི་ཟབ་པའོ། །

[Block 1810]
ཀ་ལ་པིང་ཀའི་སྒྲ་ལྟ་བུ་ཡིད་དུ་འོང་བ༌[^1502]ནི་སྙན་པའོ། །

[Block 1811]
དྲང་བའི་དོན་བསལ་ཏེ་ངེས་པའི་དོན་ལ་གནས་པ་ནི་ཡེ་ཤེས་ལ་གནས་པའོ། །

[Block 1812]
མདོ་ལས།

[Block 1813]
དེ་བཞིན་གཤེགས་པར་བདག་འགྱུར་ཐེ་ཚོམ་མེད། །ཞེས་པ༌[^1503]ནས། བྱང་ཆུབ་སེམས་དཔའ་མང་པོ་ཡང་དག་འཛུད། །ཞེས་པའི༌[^1504]བར་དུ་ཐེག་པ་ཆེན་པོ་ལ་ཕྱོགས་པའི་རྒྱུ་ཆེན་པོ་བསྐྱེད་པས་སངས་རྒྱས་སུ་འགྲུབ་ཅིང་ལྷ་དང་མི་ལ་སོགས་པས༌[^1505]མཆོད་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་མང་པོ་བླ་ན་མེད་པའི་གནས་སུ་འཇོག་པར་འགྱུར་བ་བསྟན་པའོ། །

[Block 1814 [HEADING]]
##### ལུང་བསྟན་པ་ཐོབ་པ། ^4-3-4-2-0

[Block 1815]
མདོ་ལས་དེ་སྐད་ཅེས་གསོལ་པ་དང་བཅོམ་ལྡན་འདས་ཀྱིས་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་ལ་འདི་སྐད་ཅེས༌[^1506]བཀའ་སྩལ་ཏོ་ཞེས་པ་ནས་ངའི་རྗེས་སུ་སློབ་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་འདི་མན་ཆད་འཕགས་པ་ཤཱ་རིའི་བུའི་སྔོན་གྱི་སྤྱོད་པ་བསྟན་པ་དང་ད་ལྟར་དེ་བཞིན་གཤེགས་པ་དང་ཕྲད་པ་དང་། ཕྱིས་ཀྱང་ཡང་དག་པ་ཉིད་ལ་གནས་པར་འགྱུར་བ་སྟོན་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 1816 [HEADING]]
###### སྔོན་གྱི་སྤྱོད་པ། ^4-3-4-2-1-0

[Block 1817]
ཤཱ་རིའི་བུ་སྔོན་སངས་རྒྱས་བྱེ་བ་ཁྲག་ཁྲིག་མང་པོའི་ཐད་དུ་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་སྤྱད་པ་ལས་བྲམ་ཟེས་མིག་བསླངས་ཏེ། མིག་བྱིན་པ་དང་། མིག་ས་ལ་བརྫིས་ཏེ༌[^1507]དོན་མེད་པར་བྱས་པ་དང་། སེམས་ཆེན་པོ་ལས་ནུར་ཏེ་ཐེག་པ་ཆུང་ངུ་ལ་ཞུགས་པ་སྔོན་གྱི་སྤྱོད་པ་བསྟན་པའོ། །

[Block 1818 [HEADING]]
###### ད་ལྟར་སངས་རྒྱས་དང་ཕྲད་པ། ^4-3-4-2-2-0

[Block 1819]
མདོ་ལས་ཤཱ་རིའི་བུ་ཁྱོད་བྱང་ཆུབ་སེམས་དཔའི་མན་ངག་དང་ཞེས་པ་ནས་ངའི་གསུང་རབ་འདི་ལས༌[^1508]སྐྱེས་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་ད་ལྟར་གྱི་དུས་ནས་སངས་རྒྱས་དང་ཕྲད་པ་བསྟན་ཏེ། སྔོན་སྤྱོད་པ་ཆེན་པོ་ལས་ཉམས་པ་དང་ཐབས་ཀྱིས་བསྒྱུར་ཏེ་སྟོང་པ་ཟག་པ་མེད་པའི་ཡེ་ཤེས་རྟོགས་ཤིང་ཐེག༌[^1509]པ་ཆེན་པོའི་ཆོས་ལ་གནས་པར་གྱུར་པ་འདི་ཉིད་དེ་བཞིན་གཤེགས་པའི་གསུང་ལས༌[^1510]སྐྱེས་པའོ། །

[Block 1820 [HEADING]]
###### ཕྱིས་ཡང་དག་པ་ཉིད་ལ་གནས་པར་འགྱུར་བ། ^4-3-4-2-3-0

[Block 1821]
མདོ་ལས་ཤཱ་རིའི་བུ་ཁྱོད་འདི་ལྟར་ཞེས་པ་ནས་མྱ་ངན་ལས་འདས་སོ་སྙམ་དུ་སེམས་ཏེ་ཞེས་པའི་བར་དུ་ནི་ཕྱིས་ཡང་དག་པ་ཉིད་ལ་གནས་པར་འགྱུར་བ་བསྟན་ཏེ། མི་དྲན་ནས་ཞེས་པ་ནི་དྲང་བའི་དོན་ལ་བརྟེན༌[^1511]ཅིང་ངེས་པའི་དོན་བརྗོད་པའོ། །

[Block 1822]
འཕགས་པ་ཉན་ཐོས་པའི་ཡེ་ཤེས་དང་མྱ་ངན་ལས་འདས་པ༌[^1512]ཉིད་མཐར་ཕྱིན་པའི་གནས་ཙམ་དུ་གནས༌[^1513]ཤིང་ཐེག་པ་ཆེན་པོའི་ཡེ་ཤེས་དང༌[^1514]མྱ་ངན་ལས་འདས་པ་མི་འགྲུབ་པའོ། །

[Block 1823]
མདོ་ལས་ཤཱ་རིའི་བུ་ངས་ཁྱོད་ཀྱི་སྤྱོད་པ༌[^1515]དང་ཞེས་པ་ནས་ཉན་ཐོས་པ་རྣམས་ལ་ཡང་དག་པར་བསྟན་ཏོ་ཞེས་པའི་བར་དུ་སྔོན་ཐེག་པ་ཆེན་པོ་སྤྱོད་པའི་སེམས་དྲན་པ་དང་བསྐུལ་བ་སྟེ། དམ་པའི་ཆོས་དང་བསམ་གྱིས་མི་ཁྱབ་པ་བྱང་ཆུབ་སེམས་དཔའ་ལ་གདམས་པ་དང་། སངས་རྒྱས་ཀྱིས༌[^1516]ཡོངས་སུ་གཟུང་བ༌[^1517]ནི་མདོ་སྡེ་འདི་ཉིད་ཀྱི་རྣམ་གྲངས་ཏེ། འདི་ཐེག་པ་ཆེན་པོ་ལ་འཇུག་པའི་ཐབས་དང་སྤྱོད་པ་ཐོབ་པར་འགྱུར་བ་བསྟན་ཏོ། །

[Block 1824 [HEADING]]
###### ལུང་བསྟན་པ། ^4-3-4-2-4-0

[Block 1825]
མདོ་ལས་ཤཱ་རིའི་བུ་ཁྱོད་ནི་འདི་ལྟར་མ་འོངས་པའི་དུས་ཞེས་པ་ནས་འདི་དག་ཡོངས་སུ་རྫོགས་པར་བྱས་ནས་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་དུམ་བུ་བཞིར་དབྱེ་སྟེ། སྔར་ལུང་བསྟན་པ་དང་། ལྷ་དང་མིས་མཆོད་ཅིང་བསྟོད་པའོ། །
--- END BLOCKS ---
