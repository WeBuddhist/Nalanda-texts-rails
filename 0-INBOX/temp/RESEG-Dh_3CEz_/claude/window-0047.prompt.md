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
[Block 1646]
ཡང་གཟུགས་དང་སྒྲ་ལ་སོགས་པ་ནི་ཡུལ་དག་པ་སྟེ་གོ་སླའོ། །

[Block 1647]
རྟག་ཏུ་འདི་དག་རྣམ་དག་ནི་ལྷ་རུ་འགྱུར་བ་ཙམ་མོ། །

[Block 1648 [VERSE]]
འདི་ཉིད་རྣལ་འབྱོར་ནི་སྒྱུ་མར་དག་པའོ། །
འགྲུབ་འགྱུར་འདིར་ཡང་ཕྱག་རྒྱ་ཆེན་པོའི་རྟེན་ནོ། །

[Block 1649]
ད་ནི་ཞར་ལས་བྱུང་བ་སྟོན་ཏེ༌[^775]དེ་ཡང་རང་བཞིན་དང་། སྒྱུ་མ་རྣམ་དག་གིས་རྫོགས་པ་དང་། བསྐྱེད་པའི་རིམ་པ་སྟོན་ཏེ། ཕྱག་གི་དག་པ་སྟོང་པ་ཉིད། །ཅེས་པ་ནི་སྟོང་པ་བཅུ་དྲུག་སྟེ་ནང་སྟོང་པ་ཉིད་ལ་སོགས་པ་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་དང་། དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ནི་སྤྱིར་བསྡུས་ཏེ། བཅུ་དྲུག་པའོ། །

[Block 1650]
བདུད་དག་པ་ལ་ཞབས་རྣམས་ཉིད། །ཅེས་པ་ནི་ལྷའི་བུའི་བདུད་ཚངས་པ་སེར་པོ། འཆི་བདག་གི་བདུད་དེ་གཤིན་རྗེ་ནག་པོ། ཉོན་མོངས་པའི་བདུད་དེ། ཆུ་བདག་དཀར་པོ། ཕུང་པོའི་བདུད་དེ་གནོད་སྦྱིན་སྔོན་པོ།[^776] ཞབས་རྣམས་ནི་སྦྱིན་པ་དང་སྙན་པར་སྨྲ་བ་དང་།

[Block 1651 [VERSE]]
དོན་མཐུན་པ་དང་དོན་སྤྱོད༌[^777]པའོ། །
རྣམ་ཐར་བརྒྱད་ཀྱི་ཞལ་རྣམས་ཉིད། །

[Block 1652]
ཅེས་པ་ནི་ནང་གཟུགས་མེད་པ་ལ་ཕྱི་རོལ་གྱི་གཟུགས་སུ་ལྟ་བ༌[^778]ནི་དང་པོའོ། །

[Block 1653]
ཕྱི་རོལ་གྱི་གཟུགས་མེད་པ་ལ་ནང་གི་གཟུགས་སུ་ལྟ་བ༌[^779]ནི་གཉིས་པའོ། །

[Block 1654]
བཟང་བར་མོས་པ་འདི་ནི་གསུམ་པའོ། །

[Block 1655]
ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་དང་། རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་དང་། ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་དང་། ཡོད་མིན་མེད་མིན་སྐྱེ་མཆེད་ལ༌[^780]སྙོམས་པར་འཇུག་པ་དང་འགོག་པ་ལ་སྙོམས་པར་འཇུག་པ་སྟེ་བརྒྱད་དོ། །

[Block 1656]
རྡོ་རྗེ་གསུམ་གྱིས༌[^781]དག་པའི་སྤྱན་ནི་སྐུ་རྡོ་རྗེ་གསུང་རྡོ་རྗེ་ཐུགས་རྡོ་རྗེའོ། །

[Block 1657]
དེ་དག་མ་ཡིན་ལྷག་པར་མོས་པ་ནི་དག་པའི་རང་བཞིན་རྣམ་དག་དང་མཐུན་པ་ནི་དེ་ཉིད་དག་པ་ཡིན། སྒྱུ་མ་རྣམ་དག་མཐུན་པ་ནི་ཤ་དང་ཁྲག་རུས་པ་ལ་སོགས་པ་ལྷར་མོས་པའོ། །

[Block 1658]
འོ་ན་དེ་ཉིད་དག་པ་ཇི་ལྟ་བུ་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར་བརྟག་པ་ཕྱི་མའི་ལྷའི་དག་པ་བསྟན་ཏེ་གོ་སླའོ། །

[Block 1659]
པུཀྐ་སཱི་ལ་སོགས་པའི་གནས་བཤད་ནས་དག་པ་ཇི་ལྟ་བུ་ཞེ་ན་ས་ལ་སོགས་པ་དེ་གོ་སླའོ། །

[Block 1660]
ཡང་རྡོ་རྗེ་མ་ལ་སོགས་པ་ཆོས་ཅན་དག་པ་ཉོན་མོངས་པ་ལྔ་སྟེ་གོ་སླ་བའོ།[^782] །བསྐྱེད་པའི་རིམ་པའི་ཕྱོགས་ཞེས་པ་ནི་དེའི་ལུགས་ཀྱིས་སོ། །

[Block 1661]
ཞེ་སྡང་ལ་སོགས་པ་སྤྱོད་པ་ནི་བཤད་མ་ཐག་པའོ། །

[Block 1662]
འདིས་ནི་ཕུང་པོ་སྦྱང་བ་ནི་རྣམ་གྲངས་གཞན་དུ་བསྟན་པ༌[^783]སྔར་བཞིན་ནོ། །

[Block 1663]
ད་ནི་མཇུག་བསྡུ་བའི་ཕྱིར་གང་དང་གང་གིས་བྱ་བ་ནི་ཕུང་པོ་དང་ཉོན་མོངས་པ་ལ་སོགས་པ་དེ་ཉིད་དོ། །

[Block 1664]
འཇིག་རྟེན་ནི་རྫོགས་པའི་རིམ་པའི་དེ་ཁོ་ན་ཉིད་མི་ཤེས་པའོ། །

[Block 1665]
བཅིང་བ་ནི་འཁོར་བའོ། །

[Block 1666]
དེ་དང་དེས་ནི་ཕུང་པོ་ལ་སོགས་པ་དེ་ཉིད་དོ། །

[Block 1667 [VERSE]]
གྲོལ་བ་ནི་རྫོགས་པའི་རིམ་པ་རྟོགས་པའོ། །
དེ་ཉིད་མི་ཤེས་ནི་རྫོགས་པའི་རིམ་པའོ། །

[Block 1668]
འཇིག་རྟེན་མི་གྲོལ་བ་ནི་གྲུབ་པའི་མཐའ་ལ་མ་ཞུགས་པའོ། །

[Block 1669]
དེ་ཉིད་རྣམ་སྤངས་ནི་གྲུབ་པའི་མཐའ་ངན་པས་བསྒྱུར་བའོ། །

[Block 1670]
དངོས་གྲུབ་མི་རྙེད་པ་ནི་བསྐལ་པ་དུ་མས་ཕྱག་རྒྱ་ཆེན་པོའི་དངོས་གྲུབ་མི་འགྲུབ་པའོ། །

[Block 1671]
དེའི་ཕྱིར་དེ་དག་ལས༌[^784]བཟློག་སྟེ། དྲི་མེད་སྒྲ་མེད་ལ་སོགས་པ་རྫོགས་པའི་རིམ་པའི་དེ་ཁོ་ན་ཉིད་སྤྲོས་པ་དང་བྲལ་བའོ། །

[Block 1672]
ཐ་མལ་པ་དང་གྲུབ་མཐའ་ངན་པས་བསྒྱུར་བ་མེད་པའོ། །

[Block 1673]
ཐམས་ཅད་རྣམ་པར་དག་པ་ནི་རང་བཞིན་རྣམ་པར་དག་ཏུའོ། །

[Block 1674]
རང་བཞིན་དག་པས་གྲོལ་བ་གྲོལ་བར་ཤེས་ཞེས༌[^785]སོ། །

[Block 1675]
ཡང་གང༌[^786]དང་གང་གིས་ཞེས་བྱ་བ་ནི་སྔ་མ་དང་འདྲ་བའོ། །

[Block 1676]
དེ་དང་དེས་ནི་བཅིང་བ་ནི་བཏགས་པའི༌[^787]དངོས་པོའོ། །

[Block 1677]
དེས་ངན་སོང་དུ་འགྲོ་བའོ། །

[Block 1678 [VERSE]]
གྲོལ་བ་ནི་ལྷའི་རྣལ་འབྱོར་དུ་བྱས་པ་སྟེ།
དེ་ཉིད་མི་ཤེས་འཇིག་རྟེན་ནི་སྔ་མ་བཞིན་ནོ། །
མི་གྲོལ་བ་ནི་ལྷའི་རྣལ་འབྱོར་མི་ཤེས་པའོ། །

[Block 1679]
དེ་ཉིད་རྣམ་སྤངས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་གྲུབ་མཐའ་ལ་སོགས་པའོ། །

[Block 1680]
དངོས་གྲུབ་མི་རྙེད་ནི་ཐུན་མོང་གི་དངོས་གྲུབ་རྣམས་སོ། །

[Block 1681]
དེའི་ཕྱིར་དྲི་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྦྱར་ཏེ། ལྷའི་རྣམ་པར་མོས་པའོ། །

[Block 1682]
ཐམས་ཅད་རྣམ་པར་དག་ཅེས་པ་ནི་སྒྱུ་མ་ཡོངས་སུ་དག་པ་སྟེ། དེ་ཡོངས་སུ་ཤེས་པས་འགྲོ་བ་གྲོལ་བར་ཤེས་པའོ། །

[Block 1683]
ལེའུ་དགུ་པའོ།། །།

[Block 1684 [HEADING]]
### བཅུ་པ་རིམ་པ་གཉིས་དབང་ལམ་དུ་བྱེད་པས་རྒྱུད་ལ་སྐྱེ་བ། ^1-10-0

[Block 1685]
དེ་ནས་ནི་བདག་དོན་དག་པ་དང་ལྡན་པའི་རྗེས་ལ། གཞན་དོན་བསྟན་པའི་ཕྱིར་ཇི་ལྟར་དཀྱིལ་འཁོར་ཞེས་པ་ནི་རྡུལ་ཚོན༌[^788]ནོ། །
--- END BLOCKS ---
