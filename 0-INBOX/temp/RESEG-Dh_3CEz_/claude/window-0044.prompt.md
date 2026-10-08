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
[Block 1541]
བཅོམ་ལྡན་ནི་ཧེ་རུ་ཀ་སྟེ་ལོངས་སྐུའོ། །

[Block 1542]
བདེ་བ་ནི་དོན་དམ་མོ། །

[Block 1543]
གདོད་མ་ནི་བདག་མེད་མ་སྟེ་ཆོས་སྐུའོ། །

[Block 1544 [HEADING]]
##### མཇུག་བསྡུ་བ། ^1-8-6-13-0

[Block 1545]
དེ་དག་མཇུག་བསྡུ་བའི་ཕྱིར་གཅིག་དང་དུ་མ་བྲལ་བ་ནི་ཡིད་ཀྱི་རྒྱུ་བ་ཉོན་མོངས་པའི་བདེ་བ་བྲལ་བ་སྟེ་མི་རྟོག་པའོ། །

[Block 1546]
སྐད་ཅིག་གཅིག་ནི་སྐད་ཅིག་དང་བྲལ་བའི་མི་འགྱུར་བ་གཅིག་པ་སྟེ། ཕྱག་རྒྱ་ཆེན་པོ་རང་འབྱུང་བའོ། །

[Block 1547]
མཆོག་དགའ་ནི་འབའ་ཞིག་ཏུ་དགའ་བ་སྟེ་བདེ་བའོ། །

[Block 1548]
རང་རིག་པ་ནི་སེམས་སོ། །

[Block 1549 [VERSE]]
ཡེ་ཤེས་འདི་ནི་འདི་ཉིད་བདེ་བ་དང་།
མི་རྟོག་པ་དབྱེར་མེད་པའི་ཡེ་ཤེས་སོ། །

[Block 1550 [HEADING]]
##### འདི་ཤེས་པའི་འབྲས་བུ། ^1-8-6-14-0

[Block 1551 [VERSE]]
ཡང་འདི་ཤེས་པ་ནི་འབྲས་བུ་ཡང་བསྟན་པའི་ཕྱིར།
ངག་གི་ལམ་འདས་ནི་རྟོག་པ་དང་བརྗོད་པའོ། །

[Block 1552]
སྤྱོད་ཡུལ་ནི་གཉུག་མའི་དབང་པོའོ། །

[Block 1553 [VERSE]]
བྱིན་བརླབས༌[^723]རིམ་པ་ནི་རང་བྱིན་གྱིས་བརླབ་པའི༌[^724]རིམ་པའོ། །
ཀུན་མཁྱེན་ཡེ་ཤེས་ནི་ས་བཅུ་གསུམ་དང་མཚུངས་པའོ། །

[Block 1554 [HEADING]]
##### བརྟག་པས་མི་གནོད་པ། ^1-8-6-15-0

[Block 1555]
དེ་ཡང་སངས་རྒྱས་དང་མཉམ་ནས་ལ༌[^725]སོགས་པས་མི་གནོད་དམ་ཞེ་ན། དེ་ཡིས༌[^726]བརྟག་པས། མི་གནོད་པར་བསྟན་པའི་ཕྱིར། ས་དང་ཆུ་དང་མེ་དང་རླུང་དང་ནམ་མཁའ་རྟག་པ༌[^727]སྨིན་པའོ། །

[Block 1556]
རང་གཞན་རིག་པའི་ཚོར་བའམ་དབྱེ་བ་ནི༌[^728]རྟོག་པའོ། །

[Block 1557 [VERSE]]
ཀུན་ནི་རྟོག་པས་བརྟགས་པ༌[^729]ཀུན་ནོ། །
སྐད་ཅིག་ནི་ཡེ་ཤེས་ཉིད་དོ། །

[Block 1558]
མི་གནོད་པའམ་མི་འཆིང་བ་དེས་མི་གནོད་པས་ན༌[^730]སངས་རྒྱས་དང་འདྲའོ། །

[Block 1559]
ཡང་སྤྲུལ་ཞིང་བསྒྱུར་བར་ནུས་སམ་ཞེ་ན། མཐོ་རིས་མི་ཡུལ་རྐང་འོག་ཏུ། །

[Block 1560 [VERSE]]
ཞེས་བྱ་བ་ནི་ས་བླ་ས་འོག་ས་སྟེངས༌[^731]གསུམ་མོ། །
སྐད་ཅིག་ནི་འདོད་ན་དེ་མ་ཐག་གོ། །
གཟུགས་གཅིག་གམ་ནི་གང་ཡང་རུང་བར་རོ། །

[Block 1561]
འགྱུར་བར༌[^732]ནི་སྤྲུལ་ཞིང་བསྒྱུར་བའོ། །

[Block 1562]
དེ་དག་གིས་ནི་བརྟག་པས༌[^733]མི་གནོད་ཅིང་སྤྲུལ་པར་བསྟན་ནས།

[Block 1563 [HEADING]]
##### རྟོག་པས་ཀྱང་མི་གནོད་པ། ^1-8-6-16-0

[Block 1564]
ད་ནི་རྟོག་པས་ཀྱང་མི་གནོད་པ་སྟོན་ཏེ། རང་གཞན་ཆའི་རྣམ་རྟོག་གིས་ཞེས་པ་ནི་གཟུང༌[^734]འཛིན་ནམ་རང་གཞན་གྱི་རྣམ་པར་རྟོག་པའོ། །

[Block 1565]
མི་གནོད་པའམ་མི་འཆིང་བ་ནི་མ་སྐྱེས་པའི་ཕྱིར་བཅུ་གསུམ་པ་དང་མཚུངས་སོ། །

[Block 1566 [HEADING]]
##### ལམ་གཉིས་གསང་བ་ཐུན་མོང་མ་ཡིན་པ། ^1-8-6-17-0

[Block 1567]
ད་ནི་ལམ༌[^735]གཉིས་གསང་བ་ཐུན་མོང་མ་ཡིན་པར་བསྟན་པའི་ཕྱིར། ཐམས་ཅད་རིག་བྱེད་ནི་བྲམ་ཟེ་ལ་སོགས་པའི་འཇིག་རྟེན་པའོ། །

[Block 1568]
གྲུབ་མཐའ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་ཕ་རོལ་ཕྱིན་པའོ། །

[Block 1569]
ལས་རྒྱས་ལ་སོགས་པས་ནི་བྱ་བ་དང་སྤྱོད་པ་དང་རྣལ་འབྱོར་གྱི་རྒྱུད་དོ། །

[Block 1570]
དག་པའི་དངོས་གྲུབ་མི་གྲུབ་པ་ནི་དེ་དག་ལ་ཕྱག་རྒྱ་ཆེན་པོའི་དངོས་གྲུབ་མི་སྐྱེ་བས་སོ། །

[Block 1571]
རང་རང་གི་འབྲས་བུའི་དངོས་གྲུབ་ཡོད་དོ་ཞེ་ན། ཕྱག་རྒྱ་ཆེན་པོ་བསྐྱེད་རིམ་ཉུང་ལྡན་ལ་བརྟེན་ནས། གཉུག་མའི་དབང་པོར་མ་སྐྱེས་བར་དུ་ཡིད་ཀྱིས་བརྟགས་པའི་འབྲས་བུ་ཐོབ་ཀྱང་ཡང་ནི་སྲིད་པར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1572 [VERSE]]
དེའི་ཕྱིར་འཇིག་རྟེན་འདི་ནི་ཚེ་འདིའོ། །
ཕ་རོལ་ནི་སྐྱེ་བ་གཞན་དུའོ། །
དེ་མེད་པས་ནི་ལམ་གཉིས་སོ། །

[Block 1573]
དངོས་གྲུབ་མེད་ནི་ཐབས་དང་ཤེས་རབ་དབྱེར་མེད་དོ། །

[Block 1574]
ད་ནི་རྣལ་འབྱོར་བླ་མའི་རྒྱུད་དག་ལས་ཀྱང་བླ་ན་མེད་པའི་རྒྱུད་ཁྱད་པར་དུ་བསྟན་པའི་ཕྱིར། གང་གིས་མི་ཤེས་པ་ནི་བླ་མའི་རྒྱུད་ཤེས་པས་ཀྱང་ངོ་། །ཀྱེའི་རྡོ་རྗེ་ནི་ལྷན་སྐྱེས་སྟོན་པའི་རྒྱུད་དོ། །

[Block 1575]
དེ་ནི་དེ་རྣམས་སོ། །

[Block 1576]
ངལ་བ་ནི་བླ་མའི་རྒྱུད་ཤེས་པའོ། །

[Block 1577]
དོན་མེད་ནི་རྣལ་འབྱོར་རྒྱུད་ལ་སོགས་པ་གཞན་དག་གོ། །

[Block 1578]
ཡང་ན༌[^736]ངལ་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་གྲུབ་མཐའ་རྣམས་སོ། །

[Block 1579]
དོན་མེད་པ་ནི་མུ་སྟེགས་པའོ། །

[Block 1580]
མི་ཤེས་པ་ནི་བྱ་བའི་རྒྱུད་ནས་བླ་མའི་རྒྱུད་མན་ཆད་དོ། །
--- END BLOCKS ---
