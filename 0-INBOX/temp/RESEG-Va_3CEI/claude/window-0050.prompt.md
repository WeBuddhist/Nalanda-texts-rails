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

[Block 1756]
ཚིག་ཕྱེད་དང་བཅུ་གསུམ་གྱིས་ནི་ཐེ་ཙོམ་དང་མྱ་ངན་བསལ་བ་བསྟན་ཏོ། །

[Block 1757]
ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས༌[^1481]ཤིན་ཏུ་བདེ་བ་ཐོབ་པ་བསྟན་ཏོ། །

[Block 1758 [HEADING]]
###### **ཐེ་ཙོམ་དང་མྱ་ངན་བསལ་བ།** ^4-3-4-1-2-2-4-1-0

[Block 1759]
སྔ་མ་ལ་གཉིས་ཏེ། ཚིག༌[^1482]ལྔས་ནི་སྔོན་གྱི་མྱ་ངན་ཟད་པ་བསྟན་ཏོ། །

[Block 1760]
ཚིག་ཕྱེད་དང་བརྒྱད་ཀྱིས་ནི་ད་ལྟར་གྱི་ཐེ་ཚོམ་དུ་གྱུར་པ་བསྟན་ཏོ། །

[Block 1761 [HEADING]]
###### **སྔོན་གྱི་མྱ་ངན་ཟད་པ།** ^4-3-4-1-2-2-4-1-1-0

[Block 1762]
སྔ་མ་ལ་ཡང་གཉིས་ཏེ་ཚིག་གཅིག་གིས་ནི་ཅིའི་ཕྱིར་ཐེ་ཚོམ་བསལ་བ་བསྟན་ཏོ། །

[Block 1763]
ཚིག་བཞིས་ནི་ཐེ་ཚོམ་བསལ་བ་དངོས༌[^1483]བསྟན་ཏོ། །

[Block 1764 [HEADING]]
###### **ཅིའི་ཕྱིར་ཐེ་ཚོམ་བསལ་བ།** ^4-3-4-1-2-2-4-1-1-1-0

[Block 1765]
འདིར་ནི་ཆོས་ཐོས་པས༌[^1484]མྱ་ངན་ཟད་པ་བསྟན་ཏོ། །

[Block 1766]
སངས་རྒྱས་ཀྱིས༌[^1485]གསུངས་པ་འདི་ཐོས་པས་ཟག་པ་མེད་པའི་ཡེ་ཤེས་དཔག་དཀའ་བ་བྱང་ཆུབ་ཀྱི་སྙིང་པོར་འགྱུར་བ་ཐོས་པས་མྱ་ངན་དང་བྲལ་ཏེ། མྱ་ངན་དང་བྲལ་བས་ཟག་པ་མེད་པ་ཞེས་བྱའོ། །

[Block 1767 [HEADING]]
###### **ཐེ་ཚོམ་བསལ་བ་དངོས།** ^4-3-4-1-2-2-4-1-1-2-0

[Block 1768]
མདོ་ལས།

[Block 1769]
སྔོན་ཆད་བདག་ནི་ལྟ་ལ་ཆགས་གྱུར་པ། །ཞེས་པ་ནས། བདག་གིས་སྟོང་པ་ཉིད་ཀྱི༌[^1486]ཆོས་ཐོབ་སྟེ། །ཞེས་པའི་བར་འདི་མན་ཆད་ཚིག་བཞིས་མྱ་ངན་བསལ་བ་བསྟན་ཏེ། དེ་ལ་ཡང་གཉིས་སུ་དབྱེའོ། །

[Block 1770]
ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་སྔོན་ངན་པར་ལྟ་བ་ལས་ཕྱིས་ཡང་དག་པར་གྱུར་པ་བསྟན་ཏོ། །

[Block 1771]
ཚིག་ཕྱེད་དང་གསུམ་གྱིས་ནི་ད་ཐེག་པ་ཆུང་ངུར་རྟོགས་ནས་ཐེག་པ་ཆེན་པོ་ལ་འཇུག་པ་བསྟན་ཏོ། །

[Block 1772 [HEADING]]
###### **སྔོན་ངན་པར་ལྟ་བ་ལས་ཕྱིས་ཡང་དག་པར་གྱུར་པ།** ^4-3-4-1-2-2-4-1-1-2-1-0

[Block 1773]
འདིར་ནི་ངན་པར་ལྟ་བ་ལས་ཡང་དག་པར་ལྟ་བ་བསྟན་པ་སྟེ། སྔོན་མུ་སྟེགས་ཅན་གྱིས་སྟོན་པ་ལས་འཁོར་བརྒྱ་དང་བཅས་ཏེ་སངས་རྒྱས་ཀྱི་བསྟན་པ་ལ་རབ་ཏུ་བྱུང་ནས་གང་ཟག་ལ་བདག་མེད་པར༌[^1487]ཆུད་དེ་དགྲ་བཅོམ་པར་གྱུར་པས་སྟོང་པ་ཉིད་ཀྱི༌[^1488]ཆོས་ཐོབ་ཅེས་བྱའོ། །

[Block 1774 [HEADING]]
###### **ཐེག་པ་ཆུང་ངུར་རྟོགས་ནས་ཐེག་པ་ཆེན་པོ་ལ་འཇུག་པ།** ^4-3-4-1-2-2-4-1-1-2-2-0

[Block 1775]
མདོ་ལས།

[Block 1776 [VERSE]]
དེ་ཕྱིར་བདག་ནི་མྱ་ངན་འདས་སྙམ་བགྱིད། །
མྱ་ངན་འདས་ཞེས་བྱ་བ་དེ་མ་ལགས། །

[Block 1777]
ཞེས་བྱ་བ༌[^1489]ནི་ཐེག་པ་ཆུང་ངུར་རྟོགས་ནས་ཐེག་པ་ཆེན་པོ་ལ་འཇུག་པ་བསྟན་པ་སྟེ། དེ་ལ་ཡང་གཉིས་སོ། །

[Block 1778]
ཚིག་གཅིག་ནི་ཐེག་པ་ཆུང་ངུར་རྟོགས་པ་དང་ཚིག་གཅིག་ནི་ཆེན་པོ་ལས་ཉམས་པ་ཞེས་བྱའོ། །

[Block 1779]
མདོ་ལས།

[Block 1780]
ནམ་ཞིག་སངས་རྒྱས་སེམས་ཅན་གཙོར་གྱུར་ཏེ། །ཞེས་པ་ནས། གསུང་ཐོས་དེ་རིང་བདག་ནི་མྱ་ངན་འདས། །ཞེས་པའི་བར་དུ་ནི་ཡང་དག་པའི་འགོག་པ་རྟོགས་ཤིང་མངོན་པར་བྱང་ཆུབ་པ་བསྟན་ཏེ།

[Block 1781]
མཚན་དམ་པས་སྐུ་བརྒྱན་པས་སེམས་ཅན་མང་པོ་འདུ་བའི་གནས་སུ་གྱུར་པ་ཉིད་སྐྱེ་བ་རྣམ་པ་གཉིས་སྤངས་ཤིང་ཟག་པ་མེད་པ་བརྙེས་པའི་ཕྱིར་ཐེག་པ་ཆེན་པོ་མྱ་ངན་ལས་འདས་པ་ཐོབ་པོ། །མདོ་ལས།

[Block 1782 [HEADING]]
###### **བག་ཚ་བའི་ཐེ་ཚོམ་བསལ་བ།** ^4-3-4-1-2-2-4-1-2-0

[Block 1783 [HEADING]]
###### **ཐེ་ཚོམ་གྱི་གཞི་གླེང་པ།** ^4-3-4-1-2-2-4-1-2-1-0

[Block 1784]
གང་ཚེ་བདག་ནི་བྱང་ཆུབ་མཆོག་ལུང་བསྟན། །ཞེས་པ་ནས། བདག་ནི་བག་ཚ་བ་ཡི་མཐུ་སྐྱེས་པ། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་བརྒྱད་ལ་བག་ཚ་བའི་ཐེ་ཚོམ་བསལ་བ་བསྟན་ཏེ། སྔར་ཚིགས་བཅད་གཅིག་གིས༌[^1490]ཐེ་ཚོམ་གྱི་གཞི་གླེང་པ་བསྟན། དེའི་འོག་མས་ནི་ཐེ་ཚོམ་བསལ་བའི་གཏན༌[^1491]ཚིགས་བསྟན། དེའི་འོག་མ་གཞན་གྱིས་ནི་དངོས་སུ་ཐེ་ཙོམ་བསལ་བ་བསྟན་ཏེ་འདི་ནི་དང་པོའོ། །

[Block 1785 [HEADING]]
###### **ཐེ་ཚོམ་བསལ་བའི་གཏན་ཚིགས།** ^4-3-4-1-2-2-4-1-2-2-0

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
--- END BLOCKS ---
