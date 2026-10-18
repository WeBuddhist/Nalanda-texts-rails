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

[Block 1651 [HEADING]]
###### **ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པ།** ^4-2-11-1-2-2-0

[Block 1652]
ང་ཡི་ཐེག་པ་གཅིག་པོ་འདི་ཐོས་པ། །ཞེས་པ་ནས། མདོ་སྡེ་སྐུར་པས་སེམས་ཅན་དམྱལ་བར་འགྲོ། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས་ནི་མ་འོངས་པའི་དུས་ན་སེམས་ཅན་སྡིག་པ་ཅན་ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པ་སེམས་ཅན་དམྱལ་བར་འགྲོ་བར་བསྟན་ཏོ། །

[Block 1653]
མདོ་ལས།

[Block 1654 [HEADING]]
###### **ཇི་ལྟར་སྟོན་པར་འགྱུར་བ།** ^4-2-11-1-2-3-0

[Block 1655]
མཛེས་ཤིང༌[^1410]གཙང་བར་འགྱུར་བའི་སེམས་ཅན་དག །ཞེས་པ༌[^1411]ནས། ཐེག་པ་གཅིག་གིས་བསྔགས་པ་མཐའ་ཡས་སོ། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས་ནི་ཇི་ལྟར་བསྟན་པར་འགྱུར་བ་བསྟན་ཏེ། འཛེམ་པ་ནི་ཁྲེལ་བ་དང་ངོ་ཚ་དང་ལྡན་པའི་དོན་ཏོ། །

[Block 1656]
མདོ་ལས།

[Block 1657 [HEADING]]
##### གཞུང་འོག་མ་དང་མཚམས་སྦྱོར་བ། ^4-2-11-2-0

[Block 1658]
འདྲེན་པ་རྣམས་ཀྱིས་བཤད་པ་དེ་ལྟ་བུ། །ཞེས་པ་ནས། སངས་རྒྱས་འགྱུར་གྱིས་དགའ་བ་རབ་ཏུ་སྐྱེད། །ཅེས་པའི་བར་དུ་ཚིགས་བཅད་འདི་གསུམ་གྱིས༌[^1412]ནི་དགའ་བའི་སེམས་དང་ལྡན་པ་ངེས་པར་འཚང་རྒྱ་བར་བསྟན་པ་སྟེ། ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་སངས་རྒྱས་ཀྱི༌[^1413]ཆོས་རྣམས་མི༌[^1414]མཐུན་ཏེ་མ་བསླབས༌[^1415]ན་མི་རྟོགས་པར༌[^1416]བསྟན་ཏོ། །

[Block 1659]
ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས༌[^1417]ནི་དགའ་བའི་སེམས་བསྐྱེད་པས་འཚང་རྒྱ་བར་འགྱུར་བར༌[^1418]བསྟན་ཏོ།། །།

[Block 1660]
དམ་པའི་ཆོས་པུཎྜ་རཱི་ཀའི་འགྲེལ་པ། [^1419]བམ་པོ་ལྔ་པ།

[Block 1661 [HEADING]]
### དཔེའི་ལེའུ། ^4-3-0

[Block 1662]
འདི་མན་ཆད་དཔེའི་ལེའུ་སྟེ་རྣམ་པ་གསུམ་དུ་དབྱེའོ། །

[Block 1663]
ཅིའི་ཕྱིར་བསྟན་པ་དང་། ལེའུའི་མིང་བསྟན་པ་དང་། དོགས་པ་བསལ་བའོ། །

[Block 1664 [HEADING]]
#### ཅིའི་ཕྱིར་བསྟན་པ། ^4-3-1-0

[Block 1665]
ཅིའི་ཕྱིར་བསྟན་པ་ལ་ཡང་གཉིས་ཏེ། ཤཱ་རིའི་བུ་དབང་པོ་རྣོན་པོས་ཐོས་པ་ཙམ་གྱིས་རྟོགས་པ༌[^1420]དང་། གང་ཟག་བཞི་པོ་དབང་པོ་འབྲིང་པོས་དཔེ་བསྟན་པས་ཤེས་པར་འགྱུར་བ་སྟེ། དབང་པོ་འབྲིང་པོའི་ཕྱིར་དཔེའི་ལེའུ་འདི་བསྟན་ཏོ། །

[Block 1666]
འགྲེལ་པ་ལས་འདི་མན་ཆད་ཉོན་མོངས་པ་དང་བཅས་པའི་སྐྱེ་བོ་བདུན་པོའི་ཕྱིར་དཔེ་རྣམ་པ་བདུན་གྱིས་ང་རྒྱལ་རྣམ་པ་བདུན་དང་ཉོན་མོངས་པ་གསུམ་གྱི་གཉེན་པོར་བསྟན་ཏོ། །

[Block 1667 [HEADING]]
#### ལེའུའི་མིང་བསྟན་པ། ^4-3-2-0

[Block 1668]
དེ་ལེའུའི་མིང་བསྟན་པ་ནི་དཔེའི་ལེའུ་སྟེ། དཔེ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གྱི་མངོན་སུམ་གྱིས༌[^1421]འཇིག་རྟེན་ལས་འདས་པའི་དོན་ཟབ་མོ་རྟོགས་པར་བྱེད་པའི་དོན་ཏོ། །

[Block 1669 [HEADING]]
#### དོགས་པ་བསལ་བ། ^4-3-3-0

[Block 1670]
དེ་ལ་དོགས་པ་བསལ་བ་ནི་དྲིས་པ་ལས་འདིར་ནི་དཔེས་དོན་བསྟན་པས་ལེའུ་ཡང་དཔེའི་ལེའུ་ཞེས་གདགས་སུ་རུང་ན་ལེའུ་སྔ་མ་ལས་ཆོས་འབའ་ཞིག་སྟོན་ན་དེ་ལ་ཆོས་ཀྱི་ལེའུ་ཞེས་གདགས་སམ།[^1422] ལན་བཏབ་པ་སྔ་ཕྱི་འབྲེལ་བས༌[^1423]གཞུང་གིས་དེ་ལྟ་བུ་ཡིན་ཡང་མིང༌[^1424]གདགས་པ་ལ་སོ་སོ་སྟེ། ཐབས་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་ཏུ་དབྱེའོ། །

[Block 1671]
དཔེ་ནི་སྤྱིར་སྙེགས༌[^1425]ཏེ་ཐ་དད་པ་མེད་དོ། །

[Block 1672 [HEADING]]
#### ཤཱ་རིའི་བུ་ཆོས་ཐོས་ནས་དགའ་རངས་ཏེ་ལུང་བསྟན་པ་ཐོབ་པ། ^4-3-4-0

[Block 1673]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་དགའ་བ་ཐོབ་ཞེས༌[^1426]པའི་བར་དུ་འདི་མན་ཆད་ལེའུ་འདི་ལ་སྤྱིར་རྣམ་པ་གཉིས་དབྱེ་སྟེ། ཤཱ་རིའི་བུ་ཆོས་ཐོས་ནས་དགའ་རངས་ཏེ་ལུང་བསྟན་པ་ཐོབ་པ་དང་དཔེས་དབང་པོ་འབྲིང་པོ་ལ་ཆོས་བསྟན་པའོ། །

[Block 1674 [HEADING]]
##### ཆོས་ཐོས་ནས་དགའ་རངས་པ། ^4-3-4-1-0

[Block 1675 [HEADING]]
###### ཚིག་རྐྱང་པ་ལ་སྨོས་པ། ^4-3-4-1-1-0

[Block 1676]
འདི་མན་ཆད་ཤཱ་རིའི་བུ་ཆོས་ཐོས་ནས་དགའ་རངས་པ་ལ་རྣམ་པ་གཉིས་ཏེ། ཚིག་རྐྱང་པ་ལ་སྨོས་པ་དང་། ཚིགས་སུ་བཅད་དེ་བཟླས་པའོ། །

[Block 1677 [HEADING]]
###### **དགའ་བ་ཐོབ་པ།** ^4-3-4-1-1-1-0

[Block 1678]
ཇི་ལྟར་རེ་བ་བཞིན་དུ་ཡིད་དང་མི་འགལ་བ་ཐོས་པས་དགའ་བ་དང་སྤྲོ་བའོ། །

[Block 1679]
བཤད་པར་གསོལ་པ་གདབ་པས༌[^1427]ཐལ་མོ་སྦྱར་རོ། །

[Block 1680]
བཤད་པའི་ལན་འདོད་པས༌[^1428]བཅོམ་ལྡན་འདས་ལ་བལྟའོ།[^1429] །འདི་ལྟ་བུའི་སྒྲ་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོའི་གསུང་རབ་པོ། །སྔོན་མ་ཐོས་པ་ཐོས་པས་ངོ་མཚར་རྨད་དུ་གྱུར་ཏོ། །

[Block 1681]
གཞན་ཡང་དོན་རྣམ་པ་གསུམ་གྱིས་དགའ་བ་ཐོབ་པོ། །སངས་རྒྱས་ལས་ཐོས་ནས་སེམས་རབ་ཏུ་བདེ་ཞིང་བདུད་མ་ཡིན་པར་རྟོགས་པ༌[^1430]དགའ་བ་དང་། ཡང་དག་པ་གཅིག་ཐོབ་པས༌[^1431]སྔ་མ་གསུམ་པོ་ཐབས་ཙམ་དུ་བསྟན་པར་ཤེས་པས་དགའ་བ་དང་། སངས་རྒྱས་ཀྱིས༌[^1432]དགྲ་བཅོམ་པ་བརྒྱ་ཕྲག་ཕྱེད་དང་བཅུ་གསུམ་ཡང་སངས་རྒྱས་སུ་ལུང་བསྟན་པ་ཐོས་པས་དགའ་བ་ཐོབ་པས།[^1433]

[Block 1682 [HEADING]]
###### **ཅིའི་ཕྱིར་དགའ་བ།** ^4-3-4-1-1-2-0

[Block 1683]
མདོ་ལས་དེ་ཅིའི་སླད་དུ་ཞེས་པ་ནས་ཡོངས་སུ་གདུང་བར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ནི་ཅིའི་ཕྱིར་དགའ་བ་བསྟན་ཏེ། དེ་ལ་ཡང་རྣམ་པ་བཞིའོ། །

[Block 1684]
ཆོས་ཆེན་པོ་ལས་ཉམས་པས་གདུང་བར་གྱུར་པ་དང་། ཐེག་པ་ཆུང་ངུས་བཏོན་པས༌[^1434]འགྱོད་པ་དང་། ཐོས་པས༌[^1435]མྱ་ངན་ཟད་པས་དགའ་བ་དང་སངས་རྒྱས་ཀྱི་སྲས་རྣམས་བྱང་ཆུབ་ཐོབ་པར་རྟོགས་པའོ། །

[Block 1685 [HEADING]]
###### **ཆོས་ཆེན་པོ་ཉམས་པས་གདུང་བར་གྱུར་པ།** ^4-3-4-1-1-2-1-0
--- END BLOCKS ---
