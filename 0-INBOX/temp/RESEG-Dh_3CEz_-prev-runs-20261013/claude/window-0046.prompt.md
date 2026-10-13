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

[Block 1616]
མྱ་ངན་ལས་འདས་པ་ལས་ཆེས་ལྷག་པའི་ཆོས་ཅིག༌[^757]ཡོད་ན་ཡང་རྨི་ལམ་ལྟ་བུ་སྒྱུ་མ་ལྟ་བུའོ་ཞེས་གསུངས་སོ། །

[Block 1617]
གཞན་ཡང་། སེང་གེ་ཟླ་བའི་གྲོང་ཁྱེར་བཞིན། །

[Block 1618 [VERSE]]
ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱ་ཆེར་གསུངས་སོ། །
ལེའུ་བཤད་པ་ནི་སྡུད་པར་བྱེད་པས་ཁས་ལེན་པའོ། །
དངོས་པོ་ཐམས་ཅད་ནི་བརྟན་གཡོ་བསྡུས་པའོ། །
དག་པ་ནི་ཐ་མལ་པའི་རང་བཞིན་དང་བྲལ་བའོ། །

[Block 1619]
དེ་བཞིན་ཉིད་ནི་མ་བཅོས་པ་སྟེ་རང་བཞིན་རྣམ་དག་གིས་བསྟན་པའོ། །

[Block 1620]
ཕྱི་ནས་ཞེས་བྱ་བ་ནི་ལེའུ་བརྒྱད་པར་ནི་བསྐྱེད་པའི་སྔོན་དུ་བསྟན་ལ། འདིར་ནི་དེ་ལས་བཟློག་པ་བསྟན་ཏོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དེར་ནི་རྟེན༌[^758]དང་བརྟེན་པའི༌[^759]དབང་དུ་བྱས་ཏེ། རྟེན་སྔོན་དུ་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 1621 [VERSE]]
འདིར་ནི་དེ་ཁོ་ན་ཉིད་ཀྱི་དབང་དུ་བྱས་ཏེ།
རང་བཞིན་རྣམ་པར་དག་པས༌[^760]ཁྱབ་པའི་ཕྱིར་རོ། །

[Block 1622]
རེ་རེའི་དབྱེ་བ་ནི་ཆོས་རེ་རེ་ལ་ཡོད་པའི་ལྷའོ། །

[Block 1623]
ལྷ་རྣམས་ཀྱི་བརྗོད་པ་ནི་རྟེན་དྲི་ཟའི་གྲོང་ཁྱེར་དང་། བརྟེན་པ་རྨི་ལམ་ལྟ་བུ་དང་། ལོངས་སྤྱོད་སྒྱུ་མ་ལྟ་བུ་སྟེ། སྒྱུ་མ་རྣམ་དག་ཏུ་བསྟན་པའོ། །

[Block 1624]
འདི་རྣམས་ཕྱོགས་གཅིག་ཏུ་བསྟན་པ་ནི༌[^761]རྒྱུད་ཟོར་ཡང་བའི་དགོས་པ་དང་། བདག་མེད་པ༌[^762]དང་ཧེ་རུ་ཀ་གཉིས་ཁྱད་པར་མེད་པར་བསྟན་པའི་དོན་ཏོ། །

[Block 1625 [HEADING]]
#### རང་བཞིན་རྣམ་དག་བཤད་པ། ^1-9-1-0

[Block 1626]
ད་ནི་རང་བཞིན་རྣམ་དག༌[^763]བཤད་པ།[^764] གང་ལ་དག་པའི་ཚིག་རྐང་གཉིས་ཀྱིས་བསྟན་པ་སྟེ་གོ་སླའོ། །

[Block 1627]
གང་ལྟར་དག་པ་ནི་གཟུགས་ལ་སོགས་པའི་ཚིག་རྐང་གཉིས་དང་རང་བཞིན་གྱིས༌[^765]དག་པའི་ཚིག་རྐང་གཅིག་སྟེ་གོ་སླའོ། །

[Block 1628 [VERSE]]
གང་དག་པ་ནི་ཉོན་མོངས་ཤེས་བྱའི་སྒྲིབ་པའོ། །
གང་གིས་དག་པ་ནི་དག་བྱེད་གཞན་ལ་མི་ལྟོས༌[^766]པའོ། །

[Block 1629]
དེ་ཅིའི་ཕྱིར་ཞེ་ན། །

[Block 1630 [VERSE]]
དག་པ་གཞན་གྱིས་རྣམ་གྲོལ་མིན། །
ཞེས་པ་ནི་དམ་བཅའ་བའོ། །

[Block 1631 [VERSE]]
ཡུལ་རྣམ་པར༌[^767]དག་པའི་རང་བཞིན་ནི་དེ་སྒྲུབ་པར༌[^768]བྱེད་པའོ། །
རང་རིག་བདེ་མཆོག་ནི་སྒྲུབ་པའི་ཁྱད་པར་རོ། །
གཟུང་བ་མེད་པའི་ཕྱིར་འཛིན་པ་མེད་དོ། །
དེ་ལྟར་མེད་པས་རང་བཞིན་བདེ་བ་མཆོག་གོ། །

[Block 1632]
ཡང་འདིར་ཁ་ཅིག་དག་པ་དག་པར་བྱེད་དམ། མ་དག་པ་དག་པར༌[^769]བྱེད་ཅེས་རྟོག་པ་ལ། དེ་ཡང་ལེའུ་བརྒྱད་པའི་སྐབས་སུ་བཤད་པ་ལྟར་ཤེས་པར་བྱའོ། །

[Block 1633]
ད༌[^770]ནི་སྡུད་པར་བྱེད་པས་འགྲོ་བ་སངས་རྒྱས་ཀྱི་བདག་ཉིད་རང་བཞིན་གྱིས་དག་པ་ལ་ཐེ་ཚོམ་གྱིས༌[^771]དྲི་བ་དང་ལན་ཚིགས་སུ་བཅད་པ་ཕྱེད༌[^772]དང་བཞིས་སྟོན་ཏེ་གོ་སླའོ། །

[Block 1634]
ད་ནི་ཉམས་སུ་བླང་བའི་ཐབས་བསྟན་པའི་ཕྱིར། དག་པ་ཞེས་པ་ནི་རང་བཞིན་རྣམ་དག་གིས་སོ། །

[Block 1635]
དུག་མེད་བྱས་ནི་ལྟ་བའི་དཔེ་སྟེ་བསྒོམ་པ་ལ་སོགས་པའི་དཔེ་ཡང་ཇི་ལྟར་མེ་ཡིས་ཚིག་པ་ལ་སོགས་ཏེ་བརྟག་པ༌[^773]ཕྱི་མ་ལའོ། །

[Block 1636]
བསྟེན་བྱ་འདི་ནི་དཔེ་དོན་ཏེ་འདོད་པའི་ཡོན་ཏན་ནོ། །

[Block 1637]
བསྟེན་པ་ཉིད་ནི་ཕྱག་རྒྱ་ཆེན་པོ་དང་གར་བྱེད་པའི་ཐབས་སུའོ། །

[Block 1638 [HEADING]]
#### སྒྱུ་མའི་རྣམ་དག་བཤད་པ། ^1-9-2-0

[Block 1639]
ད་ནི་སྒྱུ་མའི་རྣམ་དག་བཤད་པའི་ཕྱིར།

[Block 1640 [VERSE]]
གཟུགས་ལ་སོགས་པའི་ཕུང་པོ་ལྔ་ནི་གོ་སླའོ། །
འདི་དག་རྣམ་དག་ནི་ལྷ་རུ་འགྱུར་བ་ཙམ་མོ། །
འདི་ཉིད་རྣལ་འབྱོར་ནི་སྒྱུ་མ་དག་པའོ། །

[Block 1641 [VERSE]]
འགྲུབ་འགྱུར་ནི་ཕྱག་རྒྱ་ཆེན་པོར་རོ། །
ཕྱི་ནས་རེ་རེའི་དབྱེ་བ་ཡི། །
ལྷ་རྣམས་སུ་ནི་རྗོད་བྱེད་པའི་དོན་ཏོ། །

[Block 1642]
ད་ནི་གནས་ཞར་ལ་འབྱུང་བ་སྟེ་གོ་སླའོ། །

[Block 1643]
བསྐྱེད་པའི་རིམ་པའི་ཕྱོགས་ཞེས་པ་ནི་རང་བཞིན་རྣམ་དག་ཏུ་ཐལ་དུ་དོགས་པའོ། །

[Block 1644]
སྲིད་པ་དང་ཞི་བ་ནི་རེག་དང་ཆོས་ཀྱི་ཁམས་ལ་མ༌[^774]རྟོགས་པ་འདིར་ཡང་ངོ་། །

[Block 1645 [VERSE]]
ལྷ་མོ་འདི་གཉིས་ས་སྤྱོད་མཁའ་སྤྱོད་དོ། །
གནས་ལ་ནི་རང་བཞིན་འགྱུར་བའོ། །

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
--- END BLOCKS ---
