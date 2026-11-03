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
ཕྲ་རྒྱས་ལྷག་མ་རྣམས་ནི་འདོད་པའི་ཁམས་ན་མི་དགེ་བ་དག་ཡིན་ནོ། །

[Block 1612 [HEADING]]
### མི་དགེ་བའི་རྩ་བ། ^2-18-0

[Block 1613]
དུ་ནི་མི་དགེ་བའི་རྩ་བ་དག་ཡིན། དུ་ནི་མ་ཡིན་ཞེ་ན།

[Block 1614 [VERSE]]
འདོད་ན་འདོད་ཆགས་ཁོང་ཁྲོ་དང་། །
རྨོངས་རྣམས་མི་དགེའི་རྩ་བ་ཡིན། །

[Block 1615]
འདོད་པའི་ཁམས་ན་འདོད་ཆགས་ཐམས་ཅད་དང་། ཁོང་ཁྲོ་བ་ཐམས་ཅད་དང་། འཇིག་ཚོགས་དང་། མཐར་འཛིན་པར་ལྟ་བ་དང་། མཚུངས་པར་ལྡན་པ་མ་གཏོགས་པའི་རྨོངས་པ་ཐམས་ཅད་ནི་གོ་རིམས་བཞིན་དུ་མི་དགེ་བའི་རྩ་བ་གསུམ་པ༌[^1167]ཆགས་པ་མི་དགེ་བའི་རྩ་བ་དང་། ཞེ་སྡང་མི་དགེ་བའི་རྩ་བ་དང་། གཏི་མུག་མི་དགེ་བའི་རྩ་བ་ཡིན་ཏེ། གང་ཞིག་མི་དགེ་བ་ཡང་ཡིན་ལ་མི་དགེ་བའི་རྩ་བ་ཡང་ཡིན་པ་དེ་ཁོ་ན་མི་དགེ་བའི་རྩ་བ་ཡིན་པར་འདོད་དོ། །

[Block 1616]
ཕྲ་རྒྱས་ལྷག་མ་རྣམས་ནི་མི་དགེ་བའི་རྩ་བ་དག་མ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 1617 [HEADING]]
### ལུང་དུ་མ་བསྟན་པའི་རྩ་བ། ^2-19-0

[Block 1618]
དུ་ནི་ལུང་དུ་མ་བསྟན་པའི་རྩ་བ་དག་ཡིན། དུ་ནི་མ་ཡིན་ཞེ་ན།

[Block 1619 [VERSE]]
ལུང༌[^1168]མ་བསྟན་པའི་རྩ་བ་གསུམ། །
གསུམ་པོ་གང་དག་ཅེ༌[^1169]ན།
དེ་ནི་སྲེད་དང་མ་རིག་བློ། །

[Block 1620]
དེ་ཞེས་བྱ་བ་ནི་ལུང་དུ་མ་བསྟན་པ་ཡིན་པར་སྟོན་ཏེ། ཁ་ཆེ་བ་རྣམས་ན་རེ་སྲེད་པ་དང་མ་རིག་པ་དང་ཤེས་རབ་ཐ་ན་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་ཡང་རུང་སྟེ། གང་ཅུང་ཟད་ལུང་དུ་མ་བསྟན་པ་དེ་ཐམས་ཅད་ནི་ལུང་དུ་མ་བསྟན་པ་དེ༌[^1170]རྩ་བ་དག་ཀྱང༌[^1171]ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1621]
རྣམ་གཉིས་མཐོར་འཇུག༌[^1172]ཕྱིར་དེ་ལས། །

[Block 1622]
གཞན་མིན། ཐེ་ཚོམ་ནི་རྣམ་པ་གཉིས་ཉིད་དུ་འཇུག་པའི་ཕྱིར་རྩ་བར་འོང་བ༌[^1173]མ་ཡིན་ཏེ། གཡོ་བའི་ཕྱིར་རོ། །

[Block 1623]
ང་རྒྱལ་ནི་ཁེངས་པའི་མཚན་ཉིད་ཀྱིས་མཐོན་པོར་འཇུག་པའི་ཕྱིར་མ་ཡིན་ཏེ། རྩ་བ་དང་ཆོས་མི་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1624]
འཇིག་རྟེན་ན་རྩ་བ་རྣམས་ནི་བརྟན་པ་དང་། འོག་ན་གནས་པ་དག་ཡིན་པར་མཐོང་ངོ་ཞེས་གྲག༌[^1174]གོ། །

[Block 1625]
བཞི་ཞེས་ཉི་འོག་པ། ཉི་འོག་པ་རྣམས་ནི་ལུང་དུ་མ་བསྟན་པའི་རྩ་བ་བཞིར་འདོད་དེ། དེ་དག་སྲེད་ལྟ་ང་རྒྱལ་རྨོངས། །དེ་དག་ཅེས་བྱ་བ་ནི་ལུང་དུ་མ་བསྟན་པ་དག་ཅེས་བྱ་བར་སྟོན་ཏེ། ལུང་དུ་མ་བསྟན་པའི་སྲེད་པ་དང་། ལྟ་བ་དང་། ང་རྒྱལ་དང་། མ་རིག་པའོ། །

[Block 1626]
ཅིའི་ཕྱིར་དེ་དག་ཁོ་ན་ལུང་དུ་མ་བསྟན་པའི་རྩ་བ་རྣམས་སུ་འདོད་ཅེ་ན། བསམ་གཏན་པ༌[^1175]གསུམ་མ་རིག་ལས། །

[Block 1627]
འདི་ལྟར་བསམ་གཏན་པ་ནི་གསུམ་སྟེ། སྲེད་པ་དང་། ལྟ་བ་དང་། ང་རྒྱལ་ཤས་ཆེ་བའི་བསམ་གཏན་པ་དག་ཡིན་ལ། དེ་དག་ཀྱང་མ་རིག་པའི་དབང་གིས་འགྱུར་རོ། །

[Block 1628 [HEADING]]
### ལུང་དུ་མ་བསྟན་པའི་དངོས་པོ་བཅུ་བཞི། ^2-20-0

[Block 1629]
མདོ་ལས་ལུང་དུ་མ་བསྟན་པའི་དངོས་པོ་བཅུ་བཞི་གསུངས་པ་ཅི་དེ་དག་ལུང་དུ་མ་བསྟན་པའི་ཕྱིར་ཡིན་ནམ། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 1630]
འོ་ན་ཇི་ལྟ་བུ་ཡིན༌[^1176]ཞེ་ན། གཞག་པར་བྱ་བའི་དྲི་བ༌[^1177]ལ་ལུང་དུ་མ་བསྟན་པ་ཞེས་བཤད་དོ། །

[Block 1631 [HEADING]]
#### འདྲི་བ་རྣམ་པ་བཞི། ^2-20-1-0

[Block 1632]
འདྲི་བ་ནི་རྣམ་པ་བཞི་སྟེ། མགོ་གཅིག་ཏུ་ལུང་བསྟན་པར་བྱ་བ་དང་། རྣམ་པར་ཕྱེ་ནས༌[^1178]ལུང་བསྟན་པར་བྱ་བ་དང་། དྲིས་ནས་ལུང་བསྟན་པར་བྱ་བ་དང་གཞག་པར་བྱ་བའོ། །

[Block 1633]
དེ་ལ་གོ་རིམས་བཞིན་དུ།

[Block 1634 [VERSE]]
མགོ་གཅིག་དང་ནི་རྣམ་ཕྱེ་དང་། །
དྲི་དང་གཞག་པར་ལུང་བསྟན་པ། །
འཆི་དང་སྐྱེ་དང་ཁྱད་པར་འཕགས། །
བདག་གཞན་ལ་སོགས་ལྟ་བུ་ཡིན། །

[Block 1635 [HEADING]]
##### མགོ་གཅིག་ཏུ་ལུང་བསྟན་པར་བྱ་བ། ^2-20-1-1-0

[Block 1636]
བར་རིག་པར་བྱ་སྟེ། ཅི་སེམས་ཅན་ཐམས་ཅད་འཆི་བར་འགྱུར་རམ་ཞེས་འདྲི་ན། འཆི་བར་འགྱུར་རོ་ཞེས་མགོ་གཅིག་ཏུ་ལུང༌[^1179]བསྟན་པར་བྱའོ། །

[Block 1637 [HEADING]]
##### རྣམ་པར་ཕྱེ་ནས་ལུང་བསྟན་པར་བྱ་བ། ^2-20-1-2-0

[Block 1638]
ཅི་སེམས་ཅན་ཐམས་ཅད་སྐྱེ་བར་འགྱུར་རམ་ཞེས་འདྲི་ན། ཉོན་མོངས་པ་དང་བཅས་པ་རྣམས་ནི་སྐྱེ་བར་འགྱུར་གྱི་ཉོན་མོངས་པ་མེད་པ་རྣམས་ནི་མ་ཡིན་ནོ་ཞེས་རྣམ་པར་ཕྱེ་སྟེ་ལུང་བསྟན་པར་བྱའོ། །

[Block 1639 [HEADING]]
##### དྲིས་ནས་ལུང་བསྟན་པར་བྱ་བ། ^2-20-1-3-0

[Block 1640]
ཅི་མི་འདི་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་ནམ་དམན་པ་ཡིན་ཞེས་འདྲི་ན། གང་ལས་ལྟོས་ཏེ་འདྲི་ཞེས་དྲིས་ནས་ལུང་བསྟན་པར་བྱ་སྟེ། གལ་ཏེ་ལྷ་རྣམས་ལ༌[^1180]ལྟོས་ཏེའོ་ཞེས་ཟེར་ན་ནི་དམན་ནོ་ཞེས་ལུང་བསྟན་པར་བྱའོ། །

[Block 1641]
འོན་ཏེ་ངན་སོང་རྣམས་ལས་ལྟོས་ཏེའོ་ཞེས་ཟེར་ན་ནི་ཁྱད་པར་དུ་འཕགས་སོ་ཞེས་ལུང་བསྟན་པར་བྱའོ། །

[Block 1642 [HEADING]]
##### གཞག་པར་བྱ་བ། ^2-20-1-4-0

[Block 1643]
ཅི་ཕུང་པོ་རྣམས་ལས་སེམས་ཅན་གཞན་ནམ་གཞན་མ་ཡིན་ཞེས་འདྲི་ན། སེམས་ཅན་གྱི་རྫས་མེད་པའི་ཕྱིར་གཞག་པར་བྱ་སྟེ། མོ་གཤམ་གྱི་བུ་སྔོ་བསངས་སམ་དཀར་ཤམ༌[^1181]ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1644]
འདི་ཇི་ལྟར་ན་ལུང་མ༌[^1182]བསྟན་པ་ཡིན་ཞེ་ན། དེ་ནི་ལུང་མ་བསྟན་ནོ་ཞེས་དེ་ལྟ་བུར་ལུང་དུ༌[^1183]བསྟན་པའི་ཕྱིར་རོ། །

[Block 1645]
གཞན་དག་ན་རེ་ཐམས་ཅད་སྐྱེ་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ཡང་མགོ་གཅིག་ཏུ་ལུང་བསྟན་པར་བྱ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1646]
གང་ཞིག་ཅི་གང་དག་འཆི་བར་འགྱུར་བ་དེ་དག་སྐྱེ་བར་འགྱུར་རམ་ཞེས་འདྲི་བ་དེ་ལ་ནི་རྣམ་པར་ཕྱེ་སྟེ་ལུང་བསྟན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1647]
མི་ལ་ཡང་དམན་པ་དང་ཁྱད་པར་དུ་འཕགས་པ་གཉི་ག་ཡོད་དེ། ལྟོས་པ་ཡིན་པས་མགོ་གཅིག་ཏུ་གཉིས་ཀར་ལུང་བསྟན་པར་བྱ་དགོས་ཏེ། དཔེར་ན་རྣམ་པར་ཤེས་པ་ནི་རྒྱུ་ཡང་ཡིན་ལ་འབྲས་བུ་ཡང་ཡིན་པ་བཞིན་ནོ། །

[Block 1648]
གཅིག་ཏུ་འདྲི་བ་ལ་གཅིག་ཏུ་ལུང་བསྟན་དུ་མི་རུང་བས་རྣམ་པར་ཕྱེ་སྟེ་ལུང་བསྟན་པར་རིགས་སོ། །

[Block 1649]
ཕུང་པོ་དག་ལས་སེམས་ཅན་གཞན་ནམ་ཞེས་འདྲི་བ་འདི་ནི༌[^1184]ལུང་དུ་མ་བསྟན་པ་ཁོ་ན༌[^1185]ཡིན་ཏེ། ལུང་དུ་མ་བསྟན་པ་ཁོ་ན་ནི་ལུང༌[^1186]བསྟན་པར་མི་རུང་བའོ།[^1187] །གཞག་པར་བྱ་བའི་འདྲི་བ་གང་ཡིན་པ་གཞག་པར་བྱ་བ་ཉིད་དུ་ལུང་སྟོན་པ་དེ་ཇི་ལྟར་ན་ལུང་དུ༌[^1188]མ་བསྟན་པ་ཡིན། ཆོས་མངོན་པ༌[^1189]རྣམས་ན་རེ་བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་དང་། དེའི་ལེགས་པར་བཤད་པའི་ཆོས་དང་། ཉན་ཐོས་ཀྱི་དགེ་འདུན་ལེགས་པར་ཞུགས་པ་དང་། གཟུགས་མི་རྟག་པ་ནས་རྣམ་པར་ཤེས་པའི་བར་མི་རྟག་པ་དང་། སྡུག་བསྔལ་གདགས་པ་ནས་ལམ་གདགས་པའི་བར་ནི༌[^1190]དོན་དང་ལྡན་པ་ཡིན་པའི་ཕྱིར། མགོ་གཅིག་ཏུ་ལུང་བསྟན་པར་བྱའོ། །

[Block 1650]
རྣམ་པར་ཕྱེ་སྟེ་ལུང་བསྟན་པ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་འགའ་ཞིག་ཆོས་དག་སྨྲོས་ཤིག་ཅེས་ཟེར་ན། དེ་ལ་འདས་པ་དག་དང་། མ་འོངས་པ་དག་དང་། ད་ལྟར་བྱུང་བ་དག་དང་། ཆོས་མང་པོ༌[^1191]ཞིག་ཡོད་ན་གང་དག་སྨྲ་བར་བྱ་ཞེས་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
