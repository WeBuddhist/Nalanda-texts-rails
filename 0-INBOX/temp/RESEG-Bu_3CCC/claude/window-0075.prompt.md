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
[Block 2626]
ཡང་གཞན་ཡང་།

[Block 2627 [VERSE]]
འཕགས་པའི་བདེན་རྣམས་མེད་པའི་ཕྱིར། །
དམ་པའི་ཆོས་ཀྱང་ཡོད་མ་ཡིན། །
ཆོས་དང་དགེ་འདུན་ཡོད་མིན་ན། །
སངས་རྒྱས་ཇི་ལྟར་ཡོད་པར་འགྱུར། །

[Block 2628 [VERSE]]
ཁྱོད་ཀྱིས་སངས་རྒྱས་བྱང་ཆུབ་ལ། །
མ་བརྟེན་པར་ཡང་ཐལ་བར་འགྱུར། །
ཁྱོད་ཀྱིས་བྱང་ཆུབ་སངས་རྒྱས་ལ། །
མ་བརྟེན་པར་ཡང་ཐལ་བར་འགྱུར། །

[Block 2629 [VERSE]]
ཁྱོད༌[^1692]ཀྱི་ངོ་བོ་ཉིད་ཀྱིས་ནི། །
སངས་རྒྱས་མིན་པ་གང་ཡིན་དེས། །
བྱང་ཆུབ་བྱང་ཆུབ་སྤྱོད་པ་ལ། །
བརྩལ་ཀྱང་བྱང་ཆུབ་འཐོབ༌[^1693]མི་འགྱུར། །

[Block 2630 [VERSE]]
འགའ་ཡང་ཆོས་དང་ཆོས་མིན་པ། །
ནམ་ཡང་བྱེད་པར་མི་འགྱུར་ཏེ། །
མི་སྟོང་པ་ལ་ཅི་ཞིག་བྱ། །
ངོ་བོ་ཉིད་ལ་བྱ་བ་མེད། །

[Block 2631 [VERSE]]
ཆོས་དང་ཆོས་མིན་རྒྱུས་བྱུང་བའི། །
འབྲས་བུ་ཁྱོད་ལ་ཡོད་མ་ཡིན། །
ཆོས་དང་ཆོས་མིན་མེད་པར་ཡང་། །
འབྲས་བུ་ཁྱོད་ལ་ཡོད་པར་འགྱུར། །

[Block 2632 [VERSE]]
ཆོས་དང་ཆོས་མིན་རྒྱུས་བྱུང་བའི། །
འབྲས་བུ་གལ་ཏེ་ཁྱོད་ལ་ཡོད། །
ཆོས་དང་ཆོས་མིན་ལས་བྱུང་བའི། །
འབྲས་བུ་ཅི་ཕྱིར་སྟོང་མ་ཡིན། །

[Block 2633 [VERSE]]
འཇིག་རྟེན་པ་ཡི་ཐ་སྙད་ནི། །
ཀུན་ལའང་གནོད་པ་བྱེད་པ་ཡིན། །
རྟེན་ཅིང་འབྲེལ་འབྱུང་གང་ཡིན་པའི། །
སྟོང་པ་ཉིད་ལ་གནོད་པ་བྱེད། །

[Block 2634 [VERSE]]
བྱ་བ་ཅི་ཡང་མེད་འགྱུར་ཞིང་། །
བྱ་བ་རྩོམ་པའང་མེད་པར་འགྱུར། །
སྟོང་པ་ཉིད་ལ་གནོད་བྱེད་ན། །
མི་བྱེད་པ་ཡང༌[^1694]བྱེད་པར༌[^1695]འགྱུར། །

[Block 2635 [VERSE]]
དངོས་ཉིད་ཡོད་ནའང་འགྲོ་བ་རྣམས། །
གནས་སྐབས་སྣ་ཚོགས་བྲལ་འགྱུར་ཞིང་། །
མ་སྐྱེས་པ་དང་མ་འགགས་དང་། །
ཐེར་ཟུག་ཏུ་ཡང་གནས་པར་འགྱུར། །

[Block 2636]
ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་ན་འགྲོ་བ་མ་ལུས་པ་རྣམས་གནས་སྐབས་སྣ་ཚོགས་དང་བྲལ་བར་འགྱུར་ཞིང་མ་སྐྱེས་པ་དང་མ་འགགས་པ་དང་ཐེར་ཟུག་ཏུ་གནས་པར་ཡང་འགྱུར་རོ། །

[Block 2637]
དེ་ལྟ་བས་ནས་དེ་ལྟར་ངོ་བོ་ཉིད་དུ་སྨྲ་བ་ཡོངས་སུ་འཛིན་ན༌[^1696]ཇི་སྐད་བསྟན་པའི་སྐྱོན་དེ་དག་ཐམས་ཅད་དུ་ཡང༌[^1697]ཐལ་བར་འགྱུར་རོ། །

[Block 2638]
ཡང་གཞན་ཡང་།

[Block 2639 [VERSE]]
གལ་ཏེ་སྟོང་པ་ཡོད་མིན་ན། །
མ་ཐོབ་ཐོབ་པར་བྱ་བ་དང་། །
སྡུག་བསྔལ་མཐར་བྱེད་ལས་དང་ནི། །
ཉོན་མོངས་ཐམས་ཅད་སྤོང་བའང་མེད། །

[Block 2640]
གལ་ཏེ་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་པ་ཉིད་མ་ཡིན་ན། དེའི་ཕྱིར་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཁྱད་པར་མ་ཐོབ་པ་ཐོབ་པར་བྱ་བ་གང་དག་ཇི་སྙེད་ཡོད་པ་དེ་དག་ཐམས་ཅད་ཐོབ་པར་བྱ་བ་ཡང་མེད་པར་འགྱུར་ལ། སྡུག་བསྔལ་མཐར་བྱེད་པའི་ལས་ཀྱང་མེད་པར་འགྱུར་ཞིང་། ཉོན་མོངས་པ་ཐམས་ཅད་སྤོང་བའང་མེད་པར་འགྱུར་རོ། །

[Block 2641 [VERSE]]
གང་གིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་། །
མཐོང་བ་དེས་ནི་སྡུག་བསྔལ་དང་། །
ཀུན་འབྱུང་དང་ནི་འགོག་པ་དང་། །
ལམ་ཉིད་དེ་དག་མཐོང་བ་ཡིན། །

[Block 2642]
གང་གིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མཐོང་བ་དེས་ཆོས་བཞི་པོ་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་དང་འགོག་པ་དང་། ལམ་ཉིད་ཅེས་བྱ་བ་དེ་དག་མཐོང་བ་ཡིན་ནོ། །

[Block 2643]
འཕགས་པའི་བདེན་པ་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་ཉི་ཤུ་བཞི་པའོ།། །།

[Block 2644 [HEADING]]
## མྱ་ངན་ལས་འདས་པ་བརྟག་པ། ^25-0

[Block 2645]
འདིར་སྨྲས་པ།

[Block 2646 [VERSE]]
གལ་ཏེ་འདི་དག་ཀུན་སྟོང་ན། །
འབྱུང་བ་མེད་ཅིང་འཇིག་པ་མེད། །
གང་ཞིག་སྤོང༌[^1698]དང་འགག་པ་ལས། །
མྱ་ངན་འདའ་བར་འགྱུར་བར་འདོད། །

[Block 2647]
གལ་ཏེ་འགྲོ་བ་འདི་དག་ཀུན་སྟོང་ན་དེ་ལྟ་ན་འབྱུང་བ་མེད་ཅིང་འཇིག་པ་མེད་དོ། །

[Block 2648]
དེ་དག་མེད་པའི་ཕྱིར་གང་ཞིག་སྤོང་བ༌[^1699]དང་འགག་པ་ལས་མྱ་ངན་ལས་འདས་པར༌[^1700]འགྱུར་བར་འདོད་དེ། སྤོང་བ༌[^1701]དང་འགག་པ༌[^1702]མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2649]
དེའི་ཕྱིར་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 2650]
སྟོང་པ་མ་ཡིན་ན་ནི་ཉོན་མོངས་པ་སྤོང་བ༌[^1703]དང་ཕུང་པོ་འགག་པ་ལས་མྱ་ངན་ལས་འདས་པ༌[^1704]ཐོབ་པར་ཡང་འགྱུར་རོ། །

[Block 2651]
འདིར་བཤད་པ།

[Block 2652 [VERSE]]
གལ་ཏེ་འདི་ཀུན་མི་སྟོང་ན། །
འབྱུང་བ་མེད་ཅིང་འཇིག་པ་མེད། །
གང་ཞིག་སྤོང༌[^1705]དང་འགག་པ་ལས། །
མྱ་ངན་འདའ་བར་འགྱུར་བར་འདོད། །

[Block 2653]
གལ་ཏེ་འགྲོ་བ་འདི་དག་ཀུན་མི་སྟོང་ན། དེ་ལྟ་ན་འབྱུང་བ་མེད་ཅིང་འཇིག་པ་མེད་དོ། །

[Block 2654]
དེ་དག་མེད་པའི་ཕྱིར་གང་ཞིག་སྤོང་བ༌[^1706]དང་འགག་པ༌[^1707]ལས་མྱ་ངན་ལས་འདའ་བར་འགྱུར་བར་འདོད་དེ། སྤོང་བ༌[^1708]དང་འགག་པ་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2655]
དེ་ལྟ་བས་ན་རིམ་པ་འདིས་མྱ་ངན་ལས་འདས་པ་མི་འཐད་པར་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 2656]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 2657 [VERSE]]
སྤངས་པ་མེད་པ་ཐོབ་མེད་པ། །
ཆད་པ་མེད་པ་རྟག་མེད་པ། །
འགག་པ་མེད་པ་སྐྱེ༌[^1709]མེད་པ། །
དེ་ནི་མྱ་ངན་འདས་པར་འདོད། །

[Block 2658]
དེའི་ཕྱིར་མྱ་ངན་ལས་འདས་པའི་མཚན་ཉིད་ནི་དེ་ལྟ་བུ་ཡིན་པར་གདགས་སོ། །

[Block 2659]
ཡང་གཞན་ཡང་།

[Block 2660 [VERSE]]
མྱ་ངན་འདས་པ་དངོས་པོ་མིན། །
རྒ་ཤིའི་མཚན་ཉིད་ཐལ་བར་འགྱུར། །
རྒ་ཤི་འཆི་བ་མེད་པ་ཡི། །
དངོས་པོ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2661]
རེ་ཞིག་མྱ་ངན་ལས་འདས་པ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་ཡང་དངོས་པོ་མ་ཡིན་ནོ།[^1710] །གལ་ཏེ་དངོས་པོ་ཡིན་པར་གྱུར་ན། རྒ་ཤིའི་མཚན་ཉིད་ཅན་ཡིན་པར་ཐལ་བར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། རྒ་ཤི་མེད་པའི་དངོས་པོ་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2662]
ཡང་གཞན་ཡང་།

[Block 2663 [VERSE]]
གལ་ཏེ་མྱ་ངན་འདས་དངོས་ན། །
མྱ་ངན་འདས་པ་འདུས་བྱས་འགྱུར། །
དངོས་པོ་འདུས་བྱས་མ་ཡིན་པ། །
འགའ་ཡང་ཇི་ལྟར་ཡོད་མ་ཡིན། །

[Block 2664]
གལ་ཏེ་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་ཡིན་ན་དེའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་འདུས་བྱས་སུ་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་འདུས་བྱས་མ་ཡིན་པ་ནི་འགའ་ཡང་ཇི་ལྟར་ཡང་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2665]
ཡང་གཞན་ཡང་།
--- END BLOCKS ---
