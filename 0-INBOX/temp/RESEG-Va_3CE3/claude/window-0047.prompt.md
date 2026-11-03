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
[Block 1646]
སྒྲ་སྐད་རིང་དུ་འབྱུང་བའི་སྒྲ་ནི་ཆེམ་ཆེམ་མོ། །

[Block 1647]
རྣམ་པར་འཁྲུག་པ་ནི་འཁྲུག་པའོ། །

[Block 1648]
སྒྲ་བེར་བེར་པོ་ནི་འུར་འུར་རོ། །

[Block 1649]
ཡང་ན་ས་ནི་གཡོས་སོ། །

[Block 1650]
ཤིང་ཐམས་ཅད་ནི་འགུལ་ལོ། །

[Block 1651]
རི་ཐམས་ཅད་ནི་ལྡེག་གོ། །

[Block 1652]
ལྷའི་རྔ་བོ་ཆེ་ལ་སོགས་པ་ནི་ཆེམ་ཆེམ་མོ། །

[Block 1653]
རྒྱ་མཚོ་ལ་སོགས་པ་ནི་འཁྲུགས་སོ། །

[Block 1654]
འབྲུག་རྣམས་ནི་འུར་འུར་རོ། །

[Block 1655]
དེ་དག་ཀྱང་དང་པོ་རྩོམ་པའི་ཚེ་ནི་དལ་ཞིང་མི་དྲག་པར་སྣང་ངོ་། །དེའི་འོག་ཏུ་ནི་དེ་བས་དྲག་གོ། །

[Block 1656]
ཐ་མར་དེ་བས་ཀྱང་རབ་ཏུ་དྲག་སྟེ། རྣམ་པ་གསུམ་དུ་ཕྱོ་བས་བཅོ་བརྒྱད་དུ་འགྱུར་ཏེ།[^1166] ཕྱོགས་རྣམས་ཀྱང༌[^1167]ཅིག་ཅར་མཐོ་བ་ལ་སོགས་པར་གྱུར་ན་མུགས་ཤིང་རྣམ་པར་ཞིགས་པ་བཞིན་དུ་རབ་ཏུ་འཁྲུགས་པར་འགྱུར་བའི་ཕྱིར་མཐར་གྱིས་མཐོ་བ་དང་དམའ་བར་གྱུར་ཏོ། །

[Block 1657]
དེ་ལ་གང་གི་ཚེ་ཤར་ཕྱོགས་ཀྱི་ས་དང་། ཤིང་དང་རི་ལ་སོགས་པ་རབ་ཏུ་འཁྲུགས་པར་གྱུར་པ་དེའི་ཚེ་ཤར་ཕྱོགས་མཐོ་བ་འདྲ་བར་སྣང་ངོ་། །

[Block 1658]
གང་གི༌[^1168]ཚེ་ཤར་ཕྱོགས་མཐོ་བར་སྣང་བ་དེའི་ཚེ་ནུབ་ཕྱོགས་རང་བཞིན་དུ་གནས་ཀྱང་དམའ་བ་འདྲ་བར་སྣང་བ་དེའི་ཚེ་ཤར་ཕྱོགས་མཐོ་ན་ནུབ་ཕྱོགས་དམའ་ཞེས་བྱའོ། །

[Block 1659]
གང་གི་ཚེ་ནུབ་ཕྱོགས་ཀྱི་ས་དང་ཤིང་དང་རི་ལ་སོགས་པ་རབ་ཏུ་འཁྲུགས་པར་གྱུར་པ་དེའི་ཚེ་ནུབ་ཕྱོགས་མཐོ་བ་འདྲ་བར་སྣང་ཞིང་ཤར་ཕྱོགས་རང་བཞིན་དུ་གནས་ཀྱང་དམའ་བ་འདྲ་བར་སྣང་ངོ་། །དེ་བཞིན་དུ་ཐམས་ཅད་ལ་སྦྱར་བར་བྱའོ། །

[Block 1660]
གཟུགས་ཀྱི་རྗེས་སུ་མ་སྐྱེས། གཟུགས་ལས་གཞན་གྱི་རྗེས་སུ་མ་སྐྱེས་སོ་ཞེས་བྱ་བ་ནི་གཟུགས་སྐྱེ་བར་འགྱུར་བའི་དངོས་པོ་མེད་པས་གནས་བརྟན་ཡང་དངོས་པོ་མེད་པའི་ཕྱིར་གཟུགས་ཀྱི་རྗེས་སུ་སྐྱེ་བའམ། གཟུགས་ལས་གཞན་པ་གང་དུ་ཡང་སྐྱེ་བར་མི་རིགས་སོ། །

[Block 1661]
དེ་བཞིན་ཉིད་ཀྱང་སྐྱེ་བ་དང་འབྲེལ་པ་མེད་པས་དེ་བཞིན་ཉིད་ཀྱི་རྗེས་སུ་སྐྱེ་བའམ། དེ་བཞིན་ཉིད་ལས་གཞན་པ་གང་དུ་ཡང་མི་རིགས་སོ། །

[Block 1662 [HEADING]]
##### དེ་བཞིན་ཉིད་ཟབ་པ། ^1-2-5-20-0

[Block 1663]
བཅོམ་ལྡན་འདས་དེ་བཞིན་ཉིད་དང་མ་ནོར་བ་དེ་བཞིན་ཉིད་དང་གཞན་མ་ཡིན་པ་དེ་བཞིན་ཉིད་ཟབ་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དེ་བཞིན་གཤེགས༌[^1169]པའི་དངོས་པོ་ནི་དེ་བཞིན་ཉིད་དོ། །

[Block 1664]
མ་ནོར་བའི་དངོས་པོ་ནི་མ་ནོར་བའི་དེ་བཞིན་ཉིད་དོ། །

[Block 1665]
གཞན་མ་ཡིན་པའི་དངོས་པོ་ནི་གཞན་མ་ཡིན་པ་དེ་བཞིན་ཉིད་དེ། ཆོས་རྣམས་ཀྱི༌[^1170]བརྗོད་དུ་མེད་པའི་མཚན་ཉིད་ཡོངས་སུ་གྲུབ་པ་དོན་དམ་པའི་དབྱིངས་གང་ཡིན་པ་དེ་ནི་དུས་ཐམས་ཅད་དུ་དེ་བཞིན་ཉིད་དུ་འགྱུར་ཞིང་། ནོར་བར་མི་འགྱུར་གཞན་དུ་མི་འགྱུར་བའི་ཕྱིར་དེ་བཞིན་ཉིད་དང་མ་ནོར་བ་དེ་བཞིན་ཉིད་དང་གཞན་མ་ཡིན་པ་དེ་བཞིན་ཉིད་ཅེས་བྱའོ། །

[Block 1666 [HEADING]]
###### ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད། ^1-2-5-20-1-0

[Block 1667]
ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་ནི་རྣམ་པ་གསུམ་སྟེ། མི་འཇིག་པར་ཡོངས་སུ་གྲུབ་པ་དང་། ཕྱིན་ཅི་མ་ལོག་པར་ཡོངས་སུ་གྲུབ་པ་དང་། མི་འགྱུར་བར་ཡོངས་སུ་གྲུབ་པའོ། །

[Block 1668]
དེ་ལ་མི་འཇིག་པར་ཡོངས་སུ་གྲུབ་པའི་ཕྱིར་དེ་བཞིན་ཉིད་དོ། །

[Block 1669]
ཕྱིན་ཅི་མ་ལོག་པར་ཡོངས་སུ་གྲུབ་པའི་ཕྱིར་མ་ནོར་བ་དེ་བཞིན་ཉིད་དོ། །

[Block 1670]
མི་འགྱུར་བར་ཡོངས་སུ་གྲུབ་པའི་ཕྱིར་གཞན་མ་ཡིན་པ་དེ་བཞིན་ཉིད་དོ། །

[Block 1671 [HEADING]]
###### ཆོས་ཉིད་དང་ཆོས་ཀྱི་དབྱིངས་དང་ཆོས་གནས་པ་ཉིད། ^1-2-5-20-2-0

[Block 1672]
ཆོས་ཉིད་དང་ཆོས་ཀྱི་དབྱིངས་དང་ཆོས་གནས་པ་ཉིད་ཅེས་བྱ་བ་ཚིག་གསུམ་གྱིས་མཚན་ཉིད་རྣམ་པ་གསུམ་བསྟན་ཏེ། ཆོས་ཀྱི་མཚན་ཉིད་དང་། འབྱུང་གནས་ཀྱི་མཚན་ཉིད་དང་། གནས་པའི་མཚན་ཉིད་དོ། །

[Block 1673 [HEADING]]
###### **ཆོས་ཀྱི་མཚན་ཉིད།** ^1-2-5-20-2-1-0

[Block 1674]
ཆོས་ཀྱི་དངོས་པོ་ནི་ཆོས་ཉིད་དེ་ཀུན་བརྟགས་པ་དང་། རྣམ་པར་བརྟགས༌[^1171]པའི་ཆོས་ཐམས་ཅད་ལས་གཞན་དུ་གྱུར་པ་ན་དེ་དང་མི་འདྲ་བ་བརྗོད་དུ་མེད་པ་ཆོས་ཀྱི་དངོས་པོར་གནས་པ་གང་ཡིན་པ་དེ་གནས་པའི་ཕྱིར་ཆོས་ཉིད་ཀྱི་སྒྲར་བརྗོད་དོ། །

[Block 1675 [HEADING]]
###### **འབྱུང་གནས་ཀྱི་མཚན་ཉིད།** ^1-2-5-20-2-2-0

[Block 1676]
ཆོས་ཀྱི་དབྱིངས་ཞེས་བྱ་བ་ནི་འབྱུང་གནས་ཀྱི་མཚན་ཉིད་གསུངས་པ་སྟེ། ཆོས་ནི་སྟོབས་བཅུ་དང་། མི་འཇིགས་པ་དང་། མ་འདྲེས་པ་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་སོ། །

[Block 1677]
དབྱིངས་ཀྱི་སྒྲ་ནི་རྒྱུའི་དོན་ཏེ་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཀྱི་འབྱུང་གནས་ཡིན་པའི་ཕྱིར་ཆོས་ཀྱི་དབྱིངས་ཞེས་བྱ་སྟེ་ཆོས་ཀྱི་སྐུ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1678 [HEADING]]
###### **གནས་པའི་མཚན་ཉིད།** ^1-2-5-20-2-3-0

[Block 1679]
ཆོས་གནས་པ་ཉིད་ཅེས་བྱ་བ་ནི་གནས་པའི་མཚན་ཉིད་གསུངས་པ་སྟེ། དེ་བཞིན་གཤེགས་པ་རྣམས་བྱུང་ཡང་རུང་མ་བྱུང་ཡང་རུང་ཆོས་ཉིད་དང་། ཆོས་གནས་པ་ཉིད་འདི་ནི་འདུག་པ་ཉིད་དོ་ཞེས་ཇི་སྐད་དུ་གསུངས་པ་ལྟ་བུ་སྟེ་དོན་དམ་པ་བརྗོད་དུ་མེད་པས་ཡོངས་སུ་གྲུབ་པའི་ཆོས་ནི་སྔོན་དྲི་མ་དང་བཅས་པའི་གནས་སྐབས་དང་ཕྱིས་དྲི་མ་མེད་པའི་གནས་སྐབས་ན་ཡང་དུས་ཐམས་ཅད་དུ་ཡོད་པ་ནི་ཆོས་གནས་པ་ཉིད་དོ། །

[Block 1680 [HEADING]]
###### ངེས་པའི་མཚན་ཉིད། ^1-2-5-20-3-0

[Block 1681 [HEADING]]
###### **ཆོས་སྐྱོན་མེད་པ་ཉིད།** ^1-2-5-20-3-1-0

[Block 1682]
ཆོས་སྐྱོན་མེད་པ་ཉིད་དང་། ཡང་དག་པའི་མཐའ་དང་། བསམ་གྱིས་མི་ཁྱབ་པའི་དབྱིངས་ཞེས་བྱ་བ་ཚིག་གསུམ་གྱིས་ངེས་པའི་མཚན་ཉིད་གསུངས་ཏེ། དེ་ལ་ཆོས་སྐྱོན་མེད་པ་ཉིད་ཅེས་བྱ་བ་ལ་ཆོས་ནི་འདིར་ལོག་པའི་ཆོས་ལས༌[^1172]བཟློག་པ། ཡང་དག་པ་ཉིད་ཀྱི་ཆོས་ཏེ་དེ་དག་ལ་ངེས་པ་ཉིད་དང་། གཅིག་ཏུ་ཆད་པ་ཉིད་ནི་སྐྱོན་མེད་པ་ཉིད་དེས་རབ་ཏུ་དགའ་བའི་ཡེ་ཤེས་ཀྱིས་དང་པོ་ཉིད་དུ་དེ་བཞིན་ཉིད་རབ་ཏུ་རྟོགས་པས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ངེས་པར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1683]
དེ་བས་ན་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་སངས་རྒྱས་བྱེད་པ་ཡང་དག་པ་ཉིད་ཀྱི་ཆོས་རྣམས་ཀྱི་ངེས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་ཆོས་སྐྱོན་མེད་པ་ཉིད་ཅེས་བྱ་སྟེ་འདི་སྐད་དུ་ཡང་དག་པ༌[^1173]ཉིད་སྐྱོན་མེད་པ་ལ་ཞུགས་པ་ཡིན་ནོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 1684]
ཡང་ན་སྐྱོན་ཞེས་བྱ་བ་ནི་ཆོས་ལ་སྲེད་པ་སྟེ། སྐྱོན་གྱི་དངོས་པོ་མེད་པ་ནི་སྐྱོན་མེད་པ་ཉིད་དོ་ཞེས་སྔར་ཇི་སྐད་དུ་བསྟན་པ་ལྟ་བུའོ། །

[Block 1685]
ཆོས་རྣམས་ལ༌[^1174]སྐྱོན་མེད་པ་ཉིད་ནི་ཆོས་སྐྱོན་མེད་པ་ཉིད་དེ། ཆོས་གང་རབ་ཏུ་རྟོགས་པས་སྐྱོན་གྱི་ཆོས་རྣམས་རྒྱུན་བཅད་པ་དེ་ལ་ཆོས་སྐྱོན་མེད་པ་ཉིད་ཅེས་བྱའོ། །
--- END BLOCKS ---
