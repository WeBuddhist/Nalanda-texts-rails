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
གླེང་པ་བསྟན་པ་ལ་ཡང༌[^1459]གཉིས་ཏེ། ཐོག་མའི་ཚིག་གཅིག་གིས་ནི་ཐེ་ཙོམ་མེད་པས་རབ་ཏུ་དགའ་བ༌[^1460]བསྟན་ཏོ། །

[Block 1717]
ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས༌[^1461]ནི་ཐེ་ཙོམ་དང་མྱ་ངན་ཟད་པས་ངོ་མཚར་དུ་གྱུར་པ་བསྟན་ཏོ། །

[Block 1718 [HEADING]]
###### **ཐེ་ཙོམ་དང་མྱ་ངན་ཟད་པས་ངོ་མཚར་དུ་གྱུར་པ།** ^4-3-4-1-2-1-2-0

[Block 1719]
[^1462]བདེ་བར་གཤེགས་པའི་གསུང་དེ་ངོ་མཚར༌[^1463]གྱུར། །ཞེས་པ་ནས། གསུང་ཐོས་པ་ཡིས་ཐམས་ཅད་མེད་པར་གྱུར། །ཞེས་པའི་བར་དུ་ཐེ་ཙོམ་དང་མྱ་ངན་ཟད་པས་ངོ་མཚར་དུ་གྱུར་པ་བསྟན་ཏོ། །

[Block 1720]
སྔོན་ཐེག་པ་ཆེན་པོ་མ་ཐོས་པ༌[^1464]ཐེ་ཚོམ་དང་མྱ་ངན་དུ་འགྱུར་བ༌[^1465]ལས་ད་ཐེག་པ་ཆེན་པོ་ཐོས་པས་ཐེ་ཙོམ་དང་མྱ་ངན་སློས་པ༌[^1466]བསལ་ཞེས་སྨོས་སོ། །

[Block 1721]
མྱ་ངན་སློས་པ༌[^1467]ཞེས་བྱ་བ་ནི་སངས་རྒྱས་སུ་མི་འགྱུར་དུ་དོགས་པའོ། །

[Block 1722 [HEADING]]
###### **བཤད་པ།** ^4-3-4-1-2-2-0

[Block 1723]
མདོ་ལས།

[Block 1724 [HEADING]]
###### **འགྱོད་པ།** ^4-3-4-1-2-2-1-0

[Block 1725]
གདུགས་ལ་སྤྱོད་ཅིང་ཕན་ཚུན་འཆི་བ་དང་། །ཞེས་པ་ནས། ཀྱེ་མ་སྡིག་གི་སེམས་ཀྱིས༌[^1468]བདག་བསླུས་པས། །ཞེས་པའི༌[^1469]བར་དུ་འདི་མན་ཆད་ནི་འགྱོད་པ་བསྟན་པ་སྟེ། ཀྱེ་མ་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་འགྱོད་པའི་ཐ་ཚིག་སྟེ། སྔར་ཐེག་པ་ཆུང་ངུ་ལ་གནས་པས་ཐེག་པ་ཆེན་པོ་ལ་སྐལ་བ་མེད་པ་ཙམ་དུ་འཛིན་པས་སྡིག་པའི་སེམས་ཀྱིས་བསླུས་པ་ཞེས་བྱའོ། །

[Block 1726 [HEADING]]
###### **ཅིས་འགྱོད་པ།** ^4-3-4-1-2-2-2-0

[Block 1727]
མདོ་ལས།

[Block 1728]
ཟག་པ་མེད་པའི་ཆོས་སུ་འདྲ་བ་ལ། །ཞེས་པ་ནས་འཆད་པར་མི་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ཚིག་འདི་ནི་ཅིས་འགྱོད་པ་བསྟན་པ་སྟེ། ཟག་པ་མེད་པའི་ཆོས་ཀྱི་དབྱིངས༌[^1470]ཡང་དག་པ་ཉིད་དེ། ཤེས་པ་མེད་པ་དག་ནི་མ་འོངས་པའི་དུས་སུ་སངས་རྒྱས་སུ་འགྱུར་ཞིང་ཆོས་འཆད་པར་མི་འགྱུར་རོ་ཞེས་བསྟན་ཏོ། །

[Block 1729 [HEADING]]
###### **ཆོས་ཆེན་པོ་ལས་ཉམས་པས་འགྱོད་པ།** ^4-3-4-1-2-2-3-0

[Block 1730]
མདོ་ལས།

[Block 1731]
བདག་ནི་སུམ་ཅུ་རྩ་གཉིས་མཚན་ལས་ཉམས། །ཞེས་པ་ནས་བདག་རྨོངས་སོ་ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད༌[^1471]ཕྱེད་དང་དྲུག་གིས་ཆོས་ཆེན་པོ་ལས་ཉམས་པས་འགྱོད་པ་བསྟན་པ་སྟེ༌[^1472]འདི་ལ་ཡང་རྣམ་པ་གཉིས་སུ་དབྱེའོ། །

[Block 1732]
དེ་ལ་ཡང༌[^1473]ཚིག་ཕྱེད་དང་བཞིས་ནི་ཆོས་ཆེན་པོ་གང་ཉམས་པ་བསྟན་ཏེ། ཚིགས་བཅད༌[^1474]གཉིས་ཀྱིས་ནི་བདག་འགྱོད་པ་བསྟན་ཏོ། །

[Block 1733 [HEADING]]
###### **ཆོས་ཆེན་པོ་གང་ཉམས་པ།** ^4-3-4-1-2-2-3-1-0

[Block 1734]
ཆོས་གང་ཉམས་པ་བསྟན་པ་ལ་ཡང་རྣམ་པ༌[^1475]གཉིས་སུ་དབྱེ་སྟེ། ཐོག་མའི་ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་ཕྱི་ནང་གི་མཚན་གྱིས་བརྒྱན་པའི་ཡོན་ཏན་བསྟན་ཏོ། །

[Block 1735]
ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་གྲགས་པ་དང་རྙེད་པའི་ཡོན་ཏན་བསྟན་ཏོ། །

[Block 1736 [HEADING]]
###### **ཕྱི་ནང་གི་མཚན་གྱིས་བརྒྱན་པའི་ཡོན་ཏན།** ^4-3-4-1-2-2-3-1-1-0

[Block 1737]
མཚན་གྱིས་བརྒྱན་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཚིགས་བཅད་གཅིག་གིས་ནི་མཚན་རྫོགས་པས་བདུད་བཏུལ་བའི་ཡོན་ཏན་བསྟན་ཏོ། །

[Block 1738 [HEADING]]
###### **མཚན་རྫོགས་པས་བདུད་བཏུལ་བའི་ཡོན་ཏན།** ^4-3-4-1-2-2-3-1-1-1-0

[Block 1739]
ཚིགས་བཅད་གཅིག་གིས་ནི་དཔེ་བྱད་རྫོགས་པས་མ་འདྲེས་པའི་ཡོན་ཏན་བསྟན་པ་སྟེ། འདིར་ནི་མཚན་རྫོགས་པའི་ཡོན་ཏན་ནོ། །

[Block 1740]
མཚན་སུམ་ཅུ་རྩ་གཉིས་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཆེན་པོ་ལས་རྒྱས་པར་བཤད་པ་བཞིན་ནོ། །

[Block 1741 [HEADING]]
###### **དཔེ་བྱད་རྫོགས་པས་མ་འདྲེས་པའི་ཡོན་ཏན།** ^4-3-4-1-2-2-3-1-1-2-0

[Block 1742]
མདོ་ལས།

[Block 1743]
ཐུབ་པ་ཆེན་པོའི་དཔེ་བྱད་བཟང་པོ་གང་། །ཞེས་པ་ནས། དེ་ལས༌[^1476]བདག་ཅག་ཉམས་ཤིང་ཆེས་བསླུས་སོ། །ཞེས་པའི་བར་དུ་ནི་དཔེ་བྱད་བཟང་པོ་རྫོགས་པས་མ་འདྲེས་པའི་ཡོན་ཏན་བསྟན་པ་སྟེ། དཔེ་བྱད་བཟང་པོ་བརྒྱད་ཅུ་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཆེན་པོ་ལས་རྒྱས་པར་བཤད་པ་བཞིན་ནོ། །

[Block 1744]
སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་བཅོ་བརྒྱད་ཀྱང་འགྲེལ་པ་ལས་རྒྱས་པར་བཤད་པ་བཞིན་ཏེ། ཐེག་པ་ཆུང་ངུ་གཉིས་ལ་མེད་པས་མ་འདྲེས་པ་ཞེས་བྱའོ། །

[Block 1745 [HEADING]]
###### **གྲགས་པ་དང་རྙེད་པའི་ཡོན་ཏན།** ^4-3-4-1-2-2-3-1-2-0

[Block 1746]
མདོ་ལས།

[Block 1747]
འཇིག་རྟེན་ཕན་པ་ཐུགས་བརྩེ་ཁྱོད་མཐོང་ནས། །ཞེས་པ་ནས། ཀྱེ་མ་བདག་ནི་བསླུས་ཞེས་རྣམ་པར་སེམས། །ཞེས་པའི་བར་དུ་ནི་གྲགས་པ་དང་རྙེད་པའི་ཡོན་ཏན་བསྟན་ཏོ། །

[Block 1748]
དེ་ལྟར་བདག་བསླུས༌[^1477]པས་སངས་རྒྱས་ཀྱི་ཡོན་ཏན་ལས་ཉམས་ཏེ་ཆུང་ངུས་ཆོག་པར་འཛིན་ཏོ། །

[Block 1749 [HEADING]]
###### **བདག་འགྱོད་པ།** ^4-3-4-1-2-2-3-2-0

[Block 1750]
མདོ་ལས།

[Block 1751]
མ་ཆགས་ཡེ་ཤེས་བསམ་གྱིས་མི་ཁྱབ་ལས། །ཞེས་པ་ནས། །རྣམ་པར་འདྲེས་པས༌[^1478]བསྟན་པའོ། །ཞེས་པའི་བར་དུ་ནི་བདག་འགྱོད་པ་བསྟན་པ་སྟེ། དེ་ལ་ཚིགས་བཅད་གཅིག་གིས་ནི་ཐེག་པ་ཆེན་པོ་ལས་ཉམས་མ་ཉམས་ཞེས་དྲིས་པའོ། །

[Block 1752]
ཚིགས་བཅད་གཅིག་གིས་ནི་བདག་རྟག་ཏུ་སངས་རྒྱས་མཐོང་ཡང་བྱང་ཆུབ་སེམས་དཔའ་ལ་ནི་བསྔགས་ཤིང་བསྟོད་ཀྱི་བདག་ཅག་ལ་མ་བསྟོད་དོ་སྙམ་སེམས་པའོ། །

[Block 1753 [HEADING]]
###### **ཐོས་ནས་དགའ་བས་མྱ་ངན་ཟད་པ།** ^4-3-4-1-2-2-4-0

[Block 1754]
མདོ་ལས།

[Block 1755]
སངས་རྒྱས་གསུང༌[^1479]འདི་བདག་གིས་ཐོས་པ་ནི། །ཞེས་པ་ནས། བྱང་ཆུབ་སྙིང་པོར་གསུང༌[^1480]ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་བཅུ་བཞིས་ནི་ཐོས་ནས་དགའ་བས་མྱ་ངན་ཟད་པ་བསྟན་ཏེ། དེ་ལ་གཉིས་སུ་དབྱེའོ། །
--- END BLOCKS ---
