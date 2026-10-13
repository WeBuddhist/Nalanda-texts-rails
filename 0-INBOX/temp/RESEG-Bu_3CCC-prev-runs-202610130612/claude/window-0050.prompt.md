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
[Block 1751]
གལ་ཏེ་སེམས་ཀྱི་རྒྱུན་འབྲེལ་པ་ལས་འབྲས་བུ་འབྱུང་བ་ཡང་དེ་དང་འདྲ་བར་འགྱུར་ན་ནི། མིའི་སེམས་ལས་ཀྱང་མིའི་རྒྱུན་ཁོ་ན་འབྱུང་ལ། ལྷའི་སེམས་ལས་ཀྱང་ལྷའི་རྒྱུན་ཁོ་ན་འབྱུང་། དུད་འགྲོའི་སེམས་ལས་ཀྱང་དུད་འགྲོའི་རྒྱུན་ཁོ་ན་འབྱུང་བར་འགྱུར་རོ། །

[Block 1752]
དེ་ལྟར་གྱུར་ན་འགྲོ་བ་འཁྲུག་པ༌[^1146]མེད་པས་རྩོམ་པ་ཐམས་ཅད་དོན་མེད་པ་ཉིད་དུ་འགྱུར་ཏེ། དེ་ལ་ཉེས་པའི་སྐྱོན་ཆེན་པོ་མང་དུ་འབྱུང་བར་འགྱུར་བས་དེ་ནི་མི་འདོད་དོ། །

[Block 1753]
དགེ་བ་དང་། མི་དགེ་བ་དང་། བསྒྲིབས་པ་དང་མ་བསྒྲིབས་པའི་ལུང་དུ་མ་བསྟན་པའི་བྱེ་བྲག་ལས་སེམས་སྣ་ཚོགས་ཉིད་དུ་འགྱུར་ཞིང་། སེམས་སྣ་ཚོགས་ཉིད་ལས་རྒྱུན་སྣ་ཚོགས་ཉིད་དུ་འགྱུར། རྒྱུན་སྣ་ཚོགས་ཉིད་ལས་ལས་སྣ་ཚོགས་ཉིད་དང་། ལས་སྣ་ཚོགས་ཉིད་ལས་འགྲོ་བ་དང་རིགས་དང་རུས་དང་ཡུལ་དང་ལུས་དང་དབང་པོ་དང་ཁ་དོག་དང་དབྱིབས་དང་སྟོབས་དང་བློ་ལ་སོགས་པ་ཐ་དད་པར་འགྱུར་བ་ཡིན་ན། དེ་ཡང་རྟག་པ་འདིས་མི་འཐད་པས། དེའི་ཕྱིར་སྐྱོན་ཆེན་པོ་མང་པོ་དུ་མར་ཐལ་བར་འགྱུར་བས་རྟག་པ༌[^1147]དེ་ནི་འདིར་འཐད་པ་མ་ཡིན་ནོ། །

[Block 1754]
འོ་ན་ཇི་ལྟ་བུར་འཐད་ཅེ་ན།

[Block 1755 [VERSE]]
སངས་རྒྱས་རྣམས་དང་རང་རྒྱལ་དང་། །
ཉན་ཐོས་རྣམས་ཀྱིས་གསུངས་པ་ཡི། །
རྟག་པ༌[^1148]གང་ཞིག་འདིར་འཐད་པ། །
དེ་ནི་རབ་ཏུ་བརྗོད་པར་བྱ། །

[Block 1756]
དེ་ཡང་གང་ཞེ་ན།

[Block 1757]
ཇི་ལྟར་བུ་ལོན་དཔང་རྒྱ་ལྟར། །དེ་ལྟར་ལས་དང་ཆུད་མི་ཟ། །

[Block 1758]
འདི་ལ་ལས་ནི་སྐད་ཅིག་མ་སྟེ། ལས་སྐད་ཅིག་མ་དེའི་ཆུད་མི་ཟ་བ་ཞེས་བྱ་བ་སྐད་ཅིག་མ་མ་ཡིན་པའི་ཆོས་སྐྱེ་སྟེ། བུ་ལོན་ཇི་ལྟ་བ་དེ་ལྟར་ནི་ལས་བལྟ་བར་བྱ་ལ། དཔང་རྒྱ་ཇི་ལྟ་བ་དེ་ལྟར་ནི་ཆུད་མི་ཟ་བ་དེ་བལྟ་བར་བྱའོ། །

[Block 1759]
དེ་ལ༌[^1149]དཔེར་ན་བུ་ལོན་གྱི་ནོར་དེ་སྤྱད་ཀྱང་དཔང་རྒྱ་ཡོད་པས་ནོར་བདག་དེའི་ནོར་ཆུད་མི་ཟ་ཞིང་ནོར་སྐྱེད༌[^1150]དང་བཅས་ཏེ་འོང་བར་འགྱུར་བ་དེ་བཞིན་དུ། ལས་སྐད་ཅིག་མ་འགགས་སུ་ཟིན་ཀྱང་། དེའི་རྒྱུ་ལས་བྱུང་བ་ཆུད་མི་ཟའི་ཆོས་སྐྱེ་བ་དེ་ཡོད་པས་བྱེད་པ་པོའི་ལས་ཀྱི་འབྲས་བུ་ཆུད་མི་ཟ་ཞིང་འོང་བར་འགྱུར་རོ། །

[Block 1760]
ཇི་ལྟར་ནོར་བདག་གིས་ནོར་ཕྱིར་བཀུག་སྟེ། འབྲས་བུ་སྤྱད་ཟིན་ན་དཔང་རྒྱ་ཡོད་ཀྱང་ཡང་དང་ཡང་དུ་ནོར་འདའ་བར་མི་ནུས་པ་དེ་ལྟར། བྱེད་པ་པོས་འབྲས་བུ་མྱོང་ཟིན་ན་ཆུད་མི་ཟ་བས་ཀྱང་ཡང་དང་ཡང་འབྲས་བུ་བསྐྱེད་པར་མི༌[^1151]ནུས་ཏེ།[^1152] དེ་ནི་ཁམས་ལས་རྣམ་པ་བཞི། ཆུད་མི་ཟ་བའི་ཆོས་དེ་ནི་ཁམས་ལས་རྣམ་པ་བཞིར་འགྱུར་ཏེ། འདོད་པ༌[^1153]གཏོགས་པ་དང་། གཟུགས་སུ་གཏོགས་པ་དང་། གཟུགས་མེད་པར་གཏོགས་པ་དང་། ཟག་པ་མེད་པའོ། །

[Block 1761]
དེ་ཡང་རང་བཞིན་ལུང་མ་བསྟན། །དེ་ཡང་རང་བཞིན་གྱིས་དགེ་བ་དང་མི་དགེ་བར་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 1762]
སྤོང་བས་སྤང་བ་མ་ཡིན་ནོ།[^1154] །བསྒོམ་པས་སྤང་བ་ཉིད་ཀྱང་ཡིན། །དེ་ནི་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ་དང་འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་སྤོང་བས་སྤང་བ༌[^1155]མ་ཡིན་ཏེ། དེ་ནི་འབྲས་བུ་གཞན་དུ་འཕོ་བ་ན་བསྒོམ་པས་སྤང་བར་བྱ་བ་མ༌[^1156]ཡིན་ནོ། །

[Block 1763 [VERSE]]
དེ་ཕྱིར་ཆུད་མི་ཟ་བ་ཡིས། །
ལས་ཀྱི་འབྲས་བུ་བསྐྱེད་པར་འགྱུར། །

[Block 1764]
དེ་ལྟར་གང་གི་ཕྱིར་དེ་སྡུག་བསྔལ་ལ་སོགས་པ་མཐོང་བས་སྤང་བར་བྱ་བ་དང༌[^1157]སྤོང་བས་སྤང་བ་མ་ཡིན་པ་དེའི་ཕྱིར་འབྲས་བུ་ཐོབ་ཟིན་ན་ཡང་ཆུད༌[^1158]མི་ཟ་བས་ལས་རྣམས་ཀྱི་འབྲས་བུ་བསྐྱེད་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 1765 [VERSE]]
གལ་ཏེ་སྤོང་བས་སྤང་བ་དང་། །
ལས་འཕོ་བ་དང་མཐུན་གྱུར་ན། །
དེ་ལ་ལས་འཇིག་ལ་སོགས་པའི། །
སྐྱོན་རྣམས་སུ་ནི་ཐལ་བར་འགྱུར། །

[Block 1766]
གལ་ཏེ་དེ་སྡུག་བསྔལ་ལ་སོགས་པ་མཐོང་བས་སྤང་བར་བྱ་བ་སྤོང་བ་དང་ལས་འཕོ་བ་དང་རིས་མཐུན་པ་ཡིན་པར་གྱུར་ན། དེ་ལྟ་ན་སྡུག་བསྔལ་ལ་སོགས་པ་མཐོང་བས་སྤང་བར་བྱ་བ་བཞིན་ནམ༌[^1159]ལས་བཞིན་དུ་དེ་ཡང་སྤོང་བར་འགྱུར་བས། དེ༌[^1160]ལས་འཇིག་པ་ལ་སོགས་པའི་སྐྱོན་རྣམས་སུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1767]
འདི་ལྟར་སོ་སོའི་སྐྱེ་བོས་སྡུག་བསྔལ་ལ་སོགས་པ་མཐོང་བས་སྤང་བར་བྱ་བའི་ཕྲ་རྒྱས་དག་སྤངས་པ་ན་སོ་སོའི་སྐྱེ་བོའི་ལས་གཞན་གང་དག་ཡིན་པ་དེ་དག་ཀྱང་སྤངས་པར་འགྱུར་རོ། །

[Block 1768]
གཞན་དུ་ན་མཐོང་བ༌[^1161]ཐོབ་པ་ཡང་སོ་སོའི་སྐྱེ་བོའི་ལས་དང་ལྡན་པར་འགྱུར་ཏེ། མཐོང་བ་ཐོབ་པ་སོ་སོའི་སྐྱེ་བོའི་ལས་དང་ལྡན་པར་གྱུར་པ༌[^1162]གང་ཡིན་པ་དེ་ནི་མི་འདོད་དེ། དེ་ལ་ད་ནི་ལས་དེ་དག་སྤངས་སུ་ཟིན་ཀྱང་ཆུད་མི་ཟ་བས་ལས་དེ་དག་གི་རྣམ་པར་སྨིན་པ་ཡོངས་སུ་བཟུང་སྟེ་གནས་པས་དེའི་ཕྱིར་མཐོང་བ་ཐོབ་པ་སོ་སོའི་སྐྱེ་བོའི་ལས་དང་ལྡན་པ་ཡང་མ་ཡིན་ལ། ལས་རྣམས་ཆུད་ཟ་བ་དེ༌[^1163]ཉིད་དུ་ཡང་མི་འགྱུར་ཏེ་རྣམ་པར་སྨིན་པར་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1769]
དེ་ལྟ་བས་ན་དེའི་སྡུག་བསྔལ་ལ་སོགས་པ་མཐོང་བས་སྤང་བར་བྱ་བ་སྤོང་བ༌[^1164]ལས་བཞིན་དུ་སྤང་བར་བྱ་བ་མ་ཡིན་ཏེ། འབྲས་བུ་གཞན་དུ་འཕོས་ན་ནི་སྤོང་བར་འགྱུར་རོ། །

[Block 1770]
འདོད་པར་གཏོགས་པའི་ཆུད་མི་ཟ་བ་ནི། འདོད་པའི་ཁམས་ལས་ཡང་དག་པར་འདས་པས་སྤོང་ལ། གཟུགས་དང་གཟུགས་མེད་པར་གཏོགས་པ་དག་ཀྱང་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་ལས་ཡང་དག་པར་འདས་པས་སྤོང་ངོ་། །

[Block 1771 [VERSE]]
ཁམས་མཚུངས་ལས་ནི་ཆ་མཚུངས་དང་། །
ཆ་མི་མཚུངས་པ་ཐམས་ཅད་ཀྱི། །
དེ་ནི་ཉིང་མཚམས༌[^1165]སྦྱོར་བའི་ཚེ། །
གཅིག་པུ་ཁོ་ན་སྐྱེ་བར་འགྱུར། །

[Block 1772]
ཁམས་མཚུངས་པའི་ལས་ཆ་མཚུངས་པ་དང་ཆ་མི་མཚུངས་པ༌[^1166]ཐམས་ཅད་ཀྱི་ཆུད་མི་ཟ་བ་དེའི་ཚེ་འདི་ལ་རེ་རེ་ལས་སྐྱེས་པ་དག་ནི་ཉིང་མཚམས་སྦྱོར་བའི་ཚེ་དེ་དག་ཐམས་ཅད་འགག་པ་ན་ཡང་གཅིག་པུ་ཁོ་ན་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1773 [VERSE]]
ཚེ་འདི་ལ་ནི་ལས་དང་ལས། །
རྣམ་པ་གཉིས་པོ་ཐམས་ཅད་ཀྱི། །
དེ་ནི་ཐ་དད་སྐྱེ་འགྱུར་ཞིང་། །
རྣམ་པར་སྨིན་ཀྱང་གནས་པ་ཡིན། །

[Block 1774]
ཚེ་འདི་ལ་ནི་ལས་དང་ལས་སོ་སོ་བ་སེམས་པ་དང་བསམས་པ་དང༌[^1167]དགེ་བ་དང་མི་དགེ་བ་རྣམ་པ་གཉིས་པོ་ཐམས་ཅད་ཀྱི་ཆུད་མི་ཟ་བ་གང་ཡིན་པ་དེ་ནི་ཐ་དད་པར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1775]
རྣམ་པར་སྨིན་ན་ཡང་གནས་པ་ཡིན་ཏེ། དེ་ནི་ལས་རྣམ་པར་སྨིན་པའི་རྒྱུས་འགག་པ་ལྟར་ངེས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1776]
ལས་རྣམ་པར་སྨིན་ཀྱང་བརྒྱ་ལ་ཇི་སྲིད་དུ་འཁྲུགས་པར་མ་གྱུར་པ་དེ་སྲིད་ཀྱི་བར་དུ་གནས་ཏེ། འཁྲུགས་པར་གྱུར་ན་ནི་འགག་གོ་དེ་གནས་སུ་ཟིན་ཀྱང་ཡང་འབྲས་བུ་སྐྱེད་པར༌[^1168]ནི་མི་ནུས་ཏེ་ངེས་པར་སྤྱད་བཞིན་པའི་དཔང་རྒྱ་བཞིན་ནོ། །

[Block 1777 [VERSE]]
དེ་ནི་འབྲས་བུ་འཕོས་པ་དང་། །
ཤི་བར་གྱུར་ན་འགག་པར་འགྱུར། །
དེ་ཡི་རྣམ་དབྱེ་ཟག་མེད་དང་། །
ཟག་དང་བཅས་པར་ཤེས་པར་བྱ། །

[Block 1778]
ལས་དེའི་ཆུད་མི་ཟ་བ་དེའི་འགག་པ་ནི་རྣམ་པ་གཉིས་སུ་ངེས་པ་ཡིན་ཏེ། འབྲས་བུ་འཕོས་པར་གྱུར་པ་དང་། ཤི་བར་གྱུར་པའོ། །

[Block 1779]
དེ་ལ་འབྲས་བུ་འཕོས་པར་གྱུར་པ་ནི་བསྒོམ་པས་སྤང་བ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 1780]
ཤི་བར་གྱུར་པ་ནི་འགག་པ་དག་ན་ཉིང་མཚམས་སྦྱོར་བའི་ཚེ་གཅིག་པུ་ཁོ་ན་སྐྱེ་བར་འགྱུར་རོ། །ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 1781]
དེའི་དེ་ཡང་རྣམ་པར་དབྱེ་ན་རྣམ་པ་གཉིས་སུ་ཤེས་པར་བྱ་སྟེ། ཟག་པ་མེད་པ་དང་ཟག་པ་དང་བཅས་པའི་ལས་ཀྱི་བྱེ་བྲག་གིས་སོ། །

[Block 1782]
དེའི་ཕྱིར་དེ་ལྟར་ལས་རྣམས་སྐད་ཅིག་མ་ཉིད་ཡིན་ཡང་ཆུད་མི་ཟ་བའི་ཆོས་ཀྱིས་ཡོངས་སུ་འཛིན་པས༌[^1169]འབྲས་བུ་དང་འབྲེལ་པར༌[^1170]འགྱུར་རོ། །

[Block 1783]
འབྲས་བུ་དང་འབྲེལ་བ་དེ་ཡང་ལས་ཀྱི་བྱེ་བྲག་ལས་འགྲོ་བ་དང་རིགས་དང་། རུས་དང་ཡུལ་དང་དུས་ཐ་དད་པ་དག་ཏུ་ལུས་དང་དབང་པོ་དང་ཁ་དོག་དང་དབྱིབས་དང་སྟོབས་དང་བློ་ལ་སོགས་པ་ཐ་དད་རྣམས་ཀྱིས་ཡུལ་སྣ་ཚོགས་ཀྱི་བདེ་བ་དང་། སྡུག་བསྔལ་ཉམས་སུ་མྱོང་བར་འགྱུར་རོ། །

[Block 1784]
དེའི་ཕྱིར།

[Block 1785 [VERSE]]
སྟོང་པ་ཉིད་དང་ཆད་མིན་དང་། །
འཁོར་བ་དང་ནི་རྟག་པ་མིན། །
ལས་རྣམས་ཆུད་མི་ཟ་བའི་ཆོས། །
སངས་རྒྱས་ཀྱིས་ནི་བསྟན་པ་ཡིན། །

[Block 1786]
དེ་ལྟར་གང་གི་ཕྱིར་ལས་དང་འབྲས་བུར༌[^1171]འབྲེལ་པ་དེ་ཡོད་པ༌[^1172]ལ་སོགས་པ་ཐ་དད་པས་གནས་སྐབས་སྣ་ཚོགས་ཡིན་ལ། གནས་སྐབས་སྣ་ཚོགས་ཡིན་ཡང་དེ་ཉིད་དང་གཞན་ཉིད་དུ་བརྗོད་པར་བྱ་བ་མ༌[^1173]ཡིན་པ་དེའི་ཕྱིར་ངོ་བོ་ཉིད་ངེས་པར་མི་གནས་པ་དང་བརྗོད་པར་བྱ་བ་མ་ཡིན་པས། སྟོང་པ་ཉིད་ཀྱང་འཐད་པ་ཡིན་ནོ། །

[Block 1787]
སྟོང་པ་ཉིད་ཡིན་ཡང་ཆད་པའི་སྐྱོན་དུ་ཡང་ཐལ་བར་མི་འགྱུར་རོ། །

[Block 1788]
འཁོར་བ་ཡང་འཐད་པ་ཡིན་ནོ། །

[Block 1789]
འཁོར་བ་ཡོད་ཀྱང་རྟག་པའི་སྐྱོན་དུ་ཡང་ཐལ་བར་མི་འགྱུར་རོ། །

[Block 1790]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་སེམས་ཅན་རྣམས་ཀྱི༌[^1174]ལས་དང་རྣམ་པར་སྨིན་པ་མངོན་སུམ་དུ་གྱུར་པ༌[^1175]ལས་རྣམས་ཀྱི་ཆུད་མི་ཟ་བའི་ཆོས་བསྟན་པ་གང་ཡིན་པ་དེ་ཡང་འཐད་པ་ཡིན་ནོ། །
--- END BLOCKS ---
