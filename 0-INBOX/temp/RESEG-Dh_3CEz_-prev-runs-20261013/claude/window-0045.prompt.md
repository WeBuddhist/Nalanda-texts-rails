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

[Block 1581]
འོན་ཀྱང་བླ་མའི་རྒྱུད་ལས་ཀྱང་ཇི་ལྟར་ཁྱད་པར་དུ་འགྱུར་ཞེ་ན། དེ་དག་གིས་ནི་དོན་དམ་པ་བྱང་ཆུབ་སེམས་ཀྱི་ཆེ་བའི་བདག་ཉིད་ཙམ༌[^737]སྟོན་ལ། འདིས་ནི་བསྐྱེད་པའི་རིམ་པ་ཉུང་ལྡན་ཆགས་པ་དང་མ་རུངས་པ་རྗེས་སུ་གཟུང་པ༌[^738]དང་། །ཚར་གཅད་པ༌[^739]ལ་བརྟེན་ནས་ཕྱག་རྒྱ་ཆེན་པོའི་མན་ངག་ལྷན་ཅིག་སྐྱེས་པ་རང༌[^740]འབར་བའི་ཐབས་ཉེ་བའི་ཕྱིར་རོ། །

[Block 1582]
དེའི་ཕྱིར་ཆུ་བོའི་རྒྱུན་ནི་མཉམ་པར་གཞག་པ༌[^741]དང་། མཉམ་པར་གཞག་པ༌[^742]ལས་ལངས་པའི་རྣལ་འབྱོར་རྒྱུན་མི་འཆད་པའོ། །

[Block 1583]
མར་མེ་འབར་བ་ནི་ལྷའི་རྣམ་པ་དང་ང་རྒྱལ་ལོ། །

[Block 1584]
རྟག་ཏུ་ནི་རྒྱུན་དུའོ། །

[Block 1585 [VERSE]]
འདི་ཉིད་ནི་ཧེ་རུ་ཀའམ་བདག་མེད་མའོ། །
རྣལ་འབྱོར་ནི་སྙོམས་པར་འཇུག་པ་དང་ལྡན་པའོ། །

[Block 1586]
ཉིན་དང་མཚན་དུ་བཞག་པ་ནི་དེ་དག་ཏུ་གདམས་པ་སྟེ། ཉིན་མཚན་གཅིག་ལ་སྒོམ་པ་ཐུན་བཞིར་མི་སྒོམ་པ་ཐུན་བཞིར་མཉམ་གཞག༌[^743]དང་སྤྱོད་ལམ་དུ་ཤེས་པར་བྱའོ། །

[Block 1587]
ཡང་ཆུའི་རྒྱུན་ནི་ཟླ་བ་བྱང་ཆུབ་སེམས་སོ། །

[Block 1588]
མར་མེ་འབར་བ༌[^744]ནི་སྙོམས་པར་འཇུག་པས་འདོད་ཆགས་ཆེན་པོའི་མེའོ། །

[Block 1589]
རྟག་ཏུ་དེ་ཉིད་ནི་ཞུ་བ་སྔོན་དུ་སོང་བའི་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1590]
རྣལ་འབྱོར་ནི་ཐ་མལ་གྱི་རྣམ་པར་རྟོག་པ་བསྒྱུར་ནས་ཐབས་དང་ཤེས་རབ་ཀྱི་ལྷར་གསལ༌[^745]བའོ། །

[Block 1591 [VERSE]]
ཉིན་མོ་འཆར་བ་སྟེ་དགའ་དང་མཆོག་དགའོ། །
མཚན་མོ་ནི་ནུབ་པ་སྟེ་དགའ་བྲལ་གྱི་དགའ་བའོ། །
རྣམ་པར་གཞག་པ༌[^746]ནི་ལྷན་ཅིག་སྐྱེས་པའི་རང་བཞིན་དུའོ། །

[Block 1592]
དེ་ཡང་དང་པོ་ཆུ་ཚོད་དང་ཐུན་ཕྱེད་དང་ཐུན་གཅིག༌[^747]དང་ཉི་མ་ཕྱེད་དང་མཚན་མོ་དང་ཇེ་ཆེ་ཇེ་ཆེ་ལ་བསླབ་པའོ།[^748] །ཡང་ཆུ་བོའི་རྒྱུན་ནི་ཧཾ་ལས་རྡོ་རྗེ་འཛིན་པ་གསོ་བའོ། །

[Block 1593]
མར་མེ་འབར་བ་ནི་དེ་བཞིན་གཤེགས་པ་བསད༌[^749]པ་སྟེ་གཏུམ་མོ་སྦར་བའོ། །

[Block 1594]
རྟག་ཏུ་དེ་ཉིད་ནི་དེ་གཉིས་རྒྱུན་མི་འཆད་པའོ། །

[Block 1595]
རྣལ་འབྱོར་ནི་སྦྱོར་བ་སྟེ་ཉིན་མཚན་ནི་སྟེང་འོག་གི་གཡས་གཡོན་ནོ། །

[Block 1596]
རྣམ་པར་གཞག་པ༌[^750]ནི་སྟེང་འོག་གི་ཐིག་ལེ་གཞག་པའམ། །

[Block 1597 [VERSE]]
གཡས་གཡོན་ཨ་ཝ་དྷཱུ་ཏཱིར་རོ། །
དེ་ནི་རང་ལུས་ཐབས་དང་ལྡན་པའོ། །
ཡང་ཆུ་བོའི་རྒྱུན་ནི་སྣང་བའོ། །

[Block 1598]
མར་མེའི་རྩེ་མོ་ནི་སྟོང་པ་ཤེས་རབ་པོ། །རྟག་ཏུ་དེ་ཉིད་རྣལ་འབྱོར་ནི་སྣང་བ་སྟོང་པ་དབྱེར་མེད་དུ་བསྒོམ་པའོ། །

[Block 1599]
ཉིན་དང་མཚན་མོ་ནི༌[^751]བརྡ་ཡིས་མཚོན་པ་སྟེ། ཉིན་མོ་སྣང་བ་མཚན་མོ་ཤེས།[^752] །དེ་གཉིས༌[^753]མཚམས་དབྱེར་མེད་བསྒོམ་པའོ། །

[Block 1600 [VERSE]]
ཡང་ན་ཆུ་བོའི་རྒྱུན་ནི་ཕྱག་རྒྱ་ཆེན་པོའོ། །
རབ་འབར་ནི་ཀུན་རྫོབ་ལྷན་སྐྱེས་སོ། །

[Block 1601]
མར་མེ་འབར་བ་ནི་དོན་དམ་ལྷན་སྐྱེས་ཏེ་ཡེ་ཤེས་རང་འབར་བའོ། །

[Block 1602]
རྟག་ཏུ་དེ་ཉིད་རྣལ་འབྱོར་ནི་དབང་པོ་རང་སྣང་ངོ་། །ཉིན་དང་མཚན་དུ་ནི་སྤྱོད་ལམ་དང་བསྲེ་བའོ། །

[Block 1603]
རྣམ་པར་གཞག་པ༌[^754]ནི་འབྲས་བུ་ཆེ་བ་ཁམས་གསུམ་རོ་གཅིག་ཏུ་འབྱུང་བའི་བདག་ཉིད་དོ། །

[Block 1604]
དེ་དག་གི་སྔོན་དུ་འགྲོ་བའི་ཆོ་ག་དང་མཇུག་གི་རིམ་པ་ནི་སྔ་མ་བཞིན་དུ་སྦྱར་རོ། །

[Block 1605]
ལེའུ་བརྒྱད་པའོ།། །།

[Block 1606 [HEADING]]
### དགུ་པ་རིམ་པ་གཉིས་དག་པའི་ཚུལ། ^1-9-0

[Block 1607]
དེ་ནས་ཞེས་བྱ་བ་ནི་རིམ་པ་གཉིས་ཀྱི་དོན་བསྟན་པའི་རྗེས་ལའོ། །

[Block 1608]
རྣམ་པར་དག་པ་ནི་གཉིས་ཏེ། རང་བཞིན་རྣམ་པར་དག་པ་དང་། སྒྱུ་མ་ཡོངས་སུ་དག་པའོ། །

[Block 1609]
རང་བཞིན་རྣམ་པར་དག་པ་ནི་རྣམ་པར་དག་པ་དང་མཆོག་ཏུ་རྣམ་པར་དག་པ་སྟེ། རྣམ་པར་དག་པ་ནི་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པར་སྤྲོས་པ་དང་བྲལ་བའོ། །

[Block 1610]
མཆོག་ཏུ་དག་པ་ནི་བདེ་བ་ཆེན་པོའི་ཐུན་མོང་མ་ཡིན་པ་དག་པའོ། །

[Block 1611]
སྒྱུ་མ་ཡོངས་སུ་དག་པ་ནི་ཆོས་ཐམས་ཅད་རྨི་ལམ་མམ་སྒྱུ་མ་ལྟ་བུའོ། །

[Block 1612]
སྒྱུ་མ༌[^755]མཆོག་ཏུ་ཡོངས་སུ་དག་པ་ནི་ལྷའི་རྣལ་འབྱོར་སྒྱུ་མ་དང་རྨི་ལམ་ལ་སོགས་པར་ཤེས་པའོ། །

[Block 1613]
དེ་སྐད་དུ་ཡང་། གཟུགས་ཀྱི་དེ་བཞིན་ཉིད་ཤེས་ན་ཆོས་ཐམས་ཅད་ཀྱི་མདོ་དང་རྒྱས་པ་ཤེས་པར་འགྱུར་རོ་ཞེས་གསུངས་པ་དང་། གཟུགས་ཁམས་ཞེས༌[^756]བྱ་སྟོང་པ་སྟེ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྔར་གསུངས་པ་དང་མཚུངས་སོ། །

[Block 1614]
ཡང་གཟུགས་ཀྱང་རྨི་ལམ་ལྟ་བུ་སྒྱུ་མ་ལྟ་བུའོ། །

[Block 1615]
མྱ་ངན་ལས་འདས་པ་ཡང་རྨི་ལམ་ལྟ་བུ་སྒྱུ་མ་ལྟ་བུའོ། །
--- END BLOCKS ---
