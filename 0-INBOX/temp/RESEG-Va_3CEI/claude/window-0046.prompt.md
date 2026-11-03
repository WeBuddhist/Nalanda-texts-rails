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
[Block 1611]
མདོ་ལས།

[Block 1612 [HEADING]]
###### **འཛིན་ནུས་པ།** ^4-2-11-1-1-2-5-3-2-2-3-2-0

[Block 1613]
དེ་ལ་ང་ཡང་འཇིགས་མེད་རབ་ཏུ་དགའ། །ཞེས་པ་ནས། འདི་དག་ཐམས་ཅད་འཇིག་རྟེན་སངས་རྒྱས་འགྱུར། །ཞེས་པའི༌[^1394]བར་དུ་འཛིན་ནུས་པ་བསྟན་པ་སྟེ། དགའ་བ་ནི་དགའ་བ་ཚད་མེད་པས་སེམས་ཅན་འཚང་རྒྱ་བ་ལ་ཕྲག་དོག་མེད་པའོ། །

[Block 1614]
འཇིགས་པ་མེད་པ་ནི་གདོན་མི་ཟ་བའི་དོན་ནི༌[^1395]སེང་གེའི་སྒྲ་སྒྲོགས་པ་ལ་གདོན་མི་ཟ་བའོ། །

[Block 1615]
རྣམ་པ༌[^1396]ཀུན་སྤངས་པ་ནི་ཐབས་ཙམ་དུ་གསུམ་དུ་བསྟན་པའོ། །

[Block 1616]
སར་མ་ཕྱིན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་བདག༌[^1397]བྱང་ཆུབ་སེམས་དཔའ་ཐོབ་པར་འཛིན་ཏེ། ཉན་ཐོས་ལ་སྐལ་བ་མེད་པར་འཛིན་པ་དང་། རིགས་མ་ངེས་པ་དག་བདག་ཀྱང་སྐལ་བ་མེད་པར་སེམས་པས་ཆུང་ངུར་ཕྱིར་ནུར་བ་དག་གི༌[^1398]ཕྱིར་ཆོས་འདི་བསྟན་པས་ཐེ་ཚོམ་དང་བྲལ་བ་བསྟན་པའོ། །

[Block 1617]
ཉན་ཐོས་བརྒྱ་ཕྲག་བཅུ་གཉིས་ཀྱང་འཚང་མི་རྒྱ་བར་སེམས་པས་དེ་དག་གི་ཕྱིར་ཡང་ཆོས་བསྟན་ཏོ། །

[Block 1618]
མདོ་ལས།

[Block 1619 [HEADING]]
###### **ཆོས་ཀྱི་དོན།** ^4-2-11-1-1-2-5-3-2-2-4-0

[Block 1620]
འདི་ལྟར་སྔ་མའི་སྐྱོབ་པ་དེ་དག་དང་། །ཞེས་པ་ནས། དེ་ལྟར་ཁྱོད་ལ་དེ་རིང་ངས་བཤད་དོ། །ཞེས་པའི་བར་དུ་ནི་ཆོས་བསྡུས་པ་བསྟན་པ་སྟེ། ཐེག་པ་ཆེན་པོའི་དོན་དམ་པར་ནི་ངོ་བོ་ཉིད་ཀྱི་རྣམ་པར་རྟོག་པ་སྤངས་ཏེ། ཐེག་པ་གསུམ་ལ་ཐ་དད་པ་མེད་པས་ཐམས་ཅད་འཚང་རྒྱ་བར་འགྱུར་རོ་ཞེས་བསྟན་ཏོ། །

[Block 1621]
མདོ་ལས།

[Block 1622 [HEADING]]
###### **མ་ཐོས་པ་ཐོས་པར་བྱ་བ།** ^4-2-11-1-1-2-6-0

[Block 1623]
རས་འགའ་གང་དུ་ཅི་ཡི་འཇིག་རྟེན་དུ། །ཞེས་པ་ནས། གང་གིས༌[^1399]ཆོས་མཆོག་ཐོས་ནས་དད་པའོ། །ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་བདུན་གྱིས་མ་ཐོས་པ་ཐོས་པར་བྱ་བ་བསྟན་པ་སྟེ། འདི་ལ་ཡང་རྣམ་པ་བཞིའོ། །

[Block 1624]
དེ་ལ་ཚིག་གཉིས་ཀྱིས༌[^1400]ཤིན་ཏུ་དཀའ་བ་བཞི་བསྟན་ཏོ། །

[Block 1625]
ཚིགས་བཅད་ཕྱེད་དང་གསུམ་གྱིས་ནི་དཔེ་རྣམ་པ་གཉིས་ཤིན་ཏུ་དཀའ་བ་བསྟན་ཏོ། །

[Block 1626]
ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་དད་པ་བསྐྱེད་པར་བསྐུལ་བ་བསྟན་ཏོ། །

[Block 1627]
ཚིགས་བཅད་གཅིག་གིས་ནི་དོན་བསྡུས་པ་བསྟན་ཏོ། །

[Block 1628 [HEADING]]
###### **ཤིན་ཏུ་དཀའ་བ་བཞི།** ^4-2-11-1-1-2-6-1-0

[Block 1629]
དཀའ་བ་བཞི་ལ་སངས་རྒྱས་འབྱུང་བར་དཀའ་བ་དང་། ཆོས་བཤད་པར་དཀའ་བ་དང་། ཆོས་ཐོས་པར་དཀའ་བ་དང་ཉན་པར་དཀའ་བའོ། །

[Block 1630]
དེ་ལ་སངས་རྒྱས་འབྱུང་བར་དཀའ་བ་ནི་བསྐལ་པ་བཟང་པོའི་སངས་རྒྱས་སྟོང་འབྱུང་བ་ལྟ་བུའོ། །

[Block 1631]
དེ་བཞིན་དུ་བསྐལ་པ་དུ་མས་སངས་རྒྱས་འབྱུང་ཞིང་སངས་རྒྱས་འོད་སྲུངས་ལྟ་བུ་ཞག་བདུན་ལས་མི་བཞུགས་པས་སངས་རྒྱས་འབྱུང་བ་དེ་ལྟར་དཀའ་བའོ། །

[Block 1632]
དེ་ལྟར་སངས་རྒྱས་འབྱུང་བར་དཀའ་བ་མི་ཁོམ་པ་བརྒྱད་ཀྱིས་བསྐལ་ཏེ། སངས་རྒྱས་དང་ཕྲད་པར་དཀའ་བས་ཆོས་ཐོས་པར་དཀའོ། །

[Block 1633]
ཆོས་མི་ཐོས་པས་སྤྱོད་པའང་ཤིན་ཏུ་དཀའོ། །

[Block 1634]
མདོ་ལས།

[Block 1635 [HEADING]]
###### **དཔེ་རྣམ་པ་གཉིས་ཤིན་ཏུ་དཀའ་བ།** ^4-2-11-1-1-2-6-2-0

[Block 1636]
ཨུ་དུམ་བཱ་རའི་མེ་ཏོག་རྙེད་པར་དཀའ་བ༌[^1401]བཞིན། །ཞེས་པ་ནས། སངས་རྒྱས་ཐམས་ཅད་མཆོད་པ་བྱས་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1402]ནི་དཔེ་གཉིས་ཀྱིས་རྙེད་པར་དཀའ་བ་བསྟན་པ་སྟེ། དེ་ལ་ཚིག་གཅིག་གིས་ནི་ཆོས་འབྱུང་བར་དཀའ་བ་བསྟན། ཚིག་ཕྱེད༌[^1403]དང་གཉིས་ཀྱིས་ནི་ཐོས་ནས་བསྟོད་པར་དཀའ་བ་བསྟན་ཏོ།[^1404] །ཆོས་འབྱུང་བ་དང་ཐོས་ནས་བསྟོད་པར་དཀའ་བ་ཡང་ཨུ་དུམ་བཱ་རའི་མེ་ཏོག་དང་འདྲའོ་ཞེས་བསྟན་ཏོ། །

[Block 1637]
མདོ་ལས།

[Block 1638 [HEADING]]
###### **དད་པ་བསྐྱེད་པར་བསྐུལ་བ།** ^4-2-11-1-1-2-6-3-0

[Block 1639]
འདི་ལྟར་ཐེ་ཚོམ་སོམ་ཉི་རྣམ་པར་སྤོངས། །ཞེས་པ་ནས། འདི་ནང་ལ་ཉན་ཐོས་གང་ཡང་མེད། །ཞེས་པའི༌[^1405]བར་དུ་ནི་དད་པ་བསྐྱེད་པར༌[^1406]བསྐུལ་ཏེ། ཐེ་ཚོམ་སྤོངས་ཤིག་པར་བསྟན་པའོ། །

[Block 1640]
མདོ་ལས།

[Block 1641 [HEADING]]
###### **དོན་བསྡུས་པ།** ^4-2-11-1-1-2-6-4-0

[Block 1642]
ཤཱ་རིའི་བུ་ཁྱོད་འདི་ཡང་གསང་བར་གྱིས། །ཞེས་པ་ནས། ང་ཡི་གསང་བ་འདི་རྣམས་ཐུབ་པར་གྱིས། །ཞེས་པའི་བར་དུ་ནི་སངས་རྒྱས་རྣམས་ཀྱི་གསང་བར་བསྔགས་པ་བསྟན་པའོ། །

[Block 1643]
མདོ་ལས།

[Block 1644 [HEADING]]
###### ཐེ་ཚོམ་བཞི་བསལ་བ། ^4-2-11-1-2-0

[Block 1645]
ཇི་ལྟ་ཞེ་ན་རྙོག་པ་ལྔ་ཡི་ཚེ། །ཞེས་པ་ནས། དེ་དག་རྣམས་ཀྱང་བྱང་ཆུབ་སེམས་མི་སྐྱེ། །ཞེས་པའི་བར་དུ་འདི་མན་ཆད་སྤྱིར་ཚིགས་བཅད་གསུམ་གྱིས་ཐེ་ཚོམ་བཞི་བསལ་བ༌[^1407]བསྟན་ཏེ། དེ་ལ་ཡང་རྣམ་པ་གསུམ་མོ། །

[Block 1646 [HEADING]]
###### **སངས་རྒྱས་རྙོག་པ་ལྔའི་ཚེ་འབྱུང་བ།** ^4-2-11-1-2-1-0

[Block 1647]
ཐོག་མ་ཚིགས་བཅད་གཅིག་གིས་སངས་རྒྱས་ནས་འཇིག་རྟེན་དུ་འབྱུང་ཞིང་ཐེག་པ་གསུམ་གྱིས༌[^1408]རྙོག་པ་ལྔའི་ཚེ་འབྱུང་བར༌[^1409]འགྱུར་བ་བསྟན་ཏོ། །

[Block 1648]
ཚིགས་བཅད་གཅིག་གིས་ནི་ཇི་ལྟར་ན་ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པ་དགྲ་བཅོམ་པའོ་ཞེས་བརྗོད་ཅིང་ཆོས་འདི་ལ་ཡིད་ཆེས་པའི་ཆོས་མེད་པར་བསྟན་ཏོ། །

[Block 1649]
ཚིགས་བཅད་གཅིག་གིས་ནི་ཇི་ལྟར་སྟོན་པར་འགྱུར་སྙམ་པ་སྟོན་ཏོ། །

[Block 1650]
མདོ་ལས། །
--- END BLOCKS ---
