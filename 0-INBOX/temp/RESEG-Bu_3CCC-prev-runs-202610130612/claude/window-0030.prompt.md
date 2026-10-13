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
[Block 1051]
དེའི་ཕྱིར་དེ་གཉིས་ནི་ལྟོས་པ་ཅན་དུ་གདགས་པ་ཡིན་གྱི། ངོ་བོ་ཉིད་དུ་གྲུབ་པ་དང་མ་གྲུབ་པ་མེད་དོ། །

[Block 1052]
དེའི་ཕྱིར་དེ་ལྟར་དེ་གཉིས་ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་དུ་ཁས་མ་བླངས་པས་དབུ་མའི་ལམ་དུ་གདགས་པ་ཡིན་ནོ། །

[Block 1053]
གདགས་པ་དེ་མ་གཏོགས་པར་དེ་གཉིས་འགྲུབ་པའི་མཚན་ཉིད་གཞན་མ་མཐོང་ངོ་། །དེ་བཞིན་ཉེར་ལེན་ཤེས་པར་བྱ། །ཉེར་ལེན་ཞེས་བྱ་བ་ནི་དངོས་པོར་ལྟ་སྟེ། གང་ལ་དངོས་པོ་ཡོད་པ་དེ་ལ་བྱེད་པ་པོ་དུ་མ་ཡོད་པས་འདིར་ཉེ་བར་བླངས་པ་དང་ཉེ་བར་ལེན་པ་པོ་གཟུང་བར༌[^662]འདོད་པར་བྱའོ། །

[Block 1054]
དེ་ལ་ཇི་ལྟར་བྱེད་པ་པོ༌[^663]ལ་བརྟེན་ནས་གདགས་པ་དེ་བཞིན་དུ། ཉེ་བར་ལེན་པ་པོ་ཡང་ཉེ་བར་བླང་བ་ལ་བརྟེན་ནས་གདགས་སོ། །

[Block 1055]
ཇི་ལྟར་ལས་བྱེད་པ་པོ་དེ་ཉིད་ལ་བརྟེན་ནས་གདགས་པ་དེ་བཞིན་དུ་ཉེ་བར་བླང་བ་ཡང་ཉེ་བར་ལེན་པ་པོ་དེ་ཉིད་ལ་བརྟེན་ནས་གདགས་ཏེ། དེ་གཉིས་ལ་ཡང་དེ་མ་གཏོགས་པར་འགྲུབ་པའི་མཚན་ཉིད་མ་མཐོང་ངོ་། །དེ་ཡང་། ཇི་ལྟར་ཞེ་ན། ལས་དང་བྱེད་པོ༌[^664]བསལ་ཕྱིར་རོ། །

[Block 1056]
བསལ་ཞེས་བྱ་བ་ནི་བཀག་པའོ། །

[Block 1057]
ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་གཏན་ཚིགས་ཀྱི་དོན་ཏེ། བྱེད་པ་པོ་དང་ལས་དེ་དག་སྔར་རྣམ་པ་དུ་མར་གསལ་བར༌[^665]བྱས་པས་དེ་དག་གསལ་བ༌[^666]ཁོ་ནས་ཉེ་བར་ལེན་པ་པོ་དང་ཉེ་བར་བླང་བ་དག་གིས༌[^667]འགྲུབ་པའི་མཚན་ཉིད་གཞན་ཡང་བསལ་བར་ཤེས་པར་བྱའོ། །

[Block 1058]
དེ་ལ་ཇི་ལྟར་བྱེད་པ་པོ་ཡིན་པར་གྱུར་པ་ལས་ཡིན་པར་གྱུར་པ་མི་བྱེད་ལ། [^668]བྱེད་པ་པོ་མ་ཡིན་པར་གྱུར་པ་ལས་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད། བྱེད་པ་པོ་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ལས་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དེ། སྐྱོན་དུ་མར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་དེ་བཞིན་དུ་ཉེ་བར་ལེན་པ་པོ་ཡང་ཉེ་བར་ལེན་པ་པོ་ཡིན་པར་གྱུར་པ་ཉེ་བར་བླང་བ་ཡིན་པར་གྱུར་པ་ཉེ་བར་ལེན་པར་མི་བྱེད། ཉེ་བར་ལེན་པ་པོ་མ་ཡིན་པར་གྱུར་པ་ཉེ་བར་བླང་བ་མ་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཉེ་བར་ལེན་པར་མི་བྱེད་དེ། སྐྱོན་དུ་མར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1059]
ཕྱོགས་མི་མཐུན་པ་དག་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 1060 [VERSE]]
བྱེད་པ་པོ་དང་ལས་དག་གིས། །
དངོས་པོ་ལྷག་མ་ཤེས་པར་བྱ། །

[Block 1061]
བྱེད་པ་པོ་ལས་དག་དང་དངོས་པོ་ལྷག་མ་རྣམས་མཚུངས་པར་ཤེས་པར་བྱའོ། །

[Block 1062]
ཉེ་བར་ལེན་པ་ལོགས་ཤིག་ཏུ་སྨོས་པ་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་དང་། དོན་འོག་མ་དག་གི་ཕྱིར་ཏེ། དེ་ལ་དངོས་པོ་ལྷག་མ་རྣམས་ནི་རྒྱུ་དང་འབྲས་བུ་དང་ཡན་ལག་དང་ཡན་ལག་ཅན་དང་། མེ་དང་བུད་ཤིང་དང་། ཡོན་ཏན་དང་ཡོན་ཏན་ཅན་དང་། མཚན་ཉིད་དང་། མཚན་ཉིད་ཀྱི་གཞི་དང་། རྣམ་པ་དེ་ལྟ་བུ་དག་གོ། །

[Block 1063]
དེ༌[^669]རྒྱུ་ཡིན་པར་གྱུར་པ་འབྲས་བུ་ཡིན་པར་གྱུར་པ་མི་སྐྱེད། [^670]རྒྱུ་མ་ཡིན་པར་གྱུར་པ་འབྲས་བུ་མ་ཡིན་པར་གྱུར་པ་མི་སྐྱེད།[^671] རྒྱུ་ཡིན་པ་དང་། མ་ཡིན་པར་གྱུར་པ་འབྲས་བུ་ཡིན་པ་དང་། མ་ཡིན་པར་གྱུར་པ་མི་སྐྱེད༌[^672]དེ། ཕྱོགས་ཐམས་ཅད་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱ་ཞིང་། སྐྱོན་དུ་ཐལ་བར་འགྱུར་བ་ཇི་སྐད་སྨོས་པ་དག་ཀྱང་བསྟན་པར་བྱའོ། །

[Block 1064]
རྒྱུ་ཡང་འབྲས་བུ་སྐྱེད་པར༌[^673]བྱེད་པ་ན༌[^674]ཡིན་པར་གྱུར་པ༌[^675]ཞེས་བྱའོ། །

[Block 1065]
དེ་ལས་གཞན་པ་ནི་མ་ཡིན་པར་གྱུར་པའོ། །

[Block 1066]
འབྲས་བུ་ཡང་སྐྱེད་པར་བྱ་བ་ན་ཡིན་པར་གྱུར་པ་ཞེས་བྱའོ། །

[Block 1067]
དེ་ལས་གཞན་པ་ནི་མ་ཡིན་པར་གྱུར་པའོ།[^676] །དེ་བཞིན་དུ་ཡན་ལག་དང་ཡན་ལག་ཅན་དག་ལ་ཡང་བལྟ་བར༌[^677]བྱ་སྟེ། ཡན་ལག་ཡིན་པར་གྱུར་པ་ཡན་ལག་ཅན་ཡིན་པར་གྱུར་པ་དག་ལ་མི་འཇུག །མ་ཡིན་པར་གྱུར་པ་ཡང་མ་ཡིན་པར་གྱུར་པ་དག་ལ་མི་འཇུག །ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཡང་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་དག་ལ་མི་འཇུག་གོ། །

[Block 1068]
མེ་ཡིན་པར་གྱུར་པ༌[^678]ཡང་བུད་ཤིང་ཡིན་པར་གྱུར་པ་མི་སྲེག །མ་ཡིན་པར་གྱུར་པ་ཡང་མ་ཡིན་པར་གྱུར་པ་མི་སྲེག །ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཡང་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་མི་སྲེག་གོ། །

[Block 1069]
ཡོན་ཏན་ཡིན་པར་གྱུར་པ་ཡང་ཡོན་ཏན་ཅན་ཡིན་པར་གྱུར་པ་ལ་མི་འཇུག །མ་ཡིན་པར་གྱུར་པ་ཡང་མ་ཡིན་པར་གྱུར་པ་ལ་མི་འཇུག །ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཡང་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ལ་མི་འཇུག་གོ། །

[Block 1070]
མཚན་ཉིད་ཡིན་པར་གྱུར་པ་ཡང་མཚན་ཉིད་ཀྱི་གཞི་ཡིན་པར་གྱུར་པ་མཚོན་པར་མི་བྱེད། མ་ཡིན་པར་གྱུར་པ་ཡང་མ་ཡིན་པར་གྱུར་པ་མཚོན་པར་མི་བྱེད། ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཡང་ཡིན་པ་དང་། མ་ཡིན་པར་གྱུར་པ་མཚོན་པར་མི་བྱེད་དོ། །

[Block 1071]
ཇི་ལྟར་བྱེད་པ་པོ་ལས་ལ་བརྟེན་ནས་གདགས་ལ། ལས་ཀྱང་བྱེད་པ་པོ་ཉིད་ལ་བརྟེན་ནས་གདགས་པ་དེ་བཞིན་དུ་འབྲས་བུ་ཡང་རྒྱུ་ལ་བརྟེན་ནས་གདགས་ལ། རྒྱུ་ཡང་འབྲས་བུ་དེ་ཉིད་ལ་བརྟེན་ནས་གདགས་སོ། །

[Block 1072]
ཡན་ལག་ཅན་ཡང་ཡན་ལག་ལ་བརྟེན་ནས་གདགས་ལ། ཡན་ལག་ཀྱང་ཡན་ལག་ཅན་དེ་ཉིད་ལ་བརྟེན་ནས་གདགས་སོ། །

[Block 1073]
མེ་ཡང་བུད་ཤིང་ལ་བརྟེན་ནས་གདགས་ལ། །བུད་ཤིང་ཡང་མེ་དེ་ཉིད་ལ་བརྟེན་ནས་གདགས་སོ། །

[Block 1074]
ཡོན་ཏན་ཅན་ཡང་ཡོན་ཏན་ལ་བརྟེན་ནས་གདགས་ལ། ཡོན་ཏན་ཡང་ཡོན་ཏན་ཅན་དེ་ཉིད་ལ་བརྟེན་ནས་གདགས་སོ། །

[Block 1075]
མཚན་ཉིད་ཀྱི་གཞི་ཡང་མཚན་ཉིད་ལ་བརྟེན་ནས་གདགས་ལ། མཚན་ཉིད་ཀྱང་མཚན་ཉིད་ཀྱི་གཞི་དེ་ཉིད་ལ་བརྟེན་ནས་གདགས་སོ། །

[Block 1076]
དེ་ལྟར་དེ་དག་ལ་ལྟོས་ཏེ་གདགས་པ་མ་གཏོགས་པར་རྣམ་པ་གཞན་གང་གིས་ཀྱང་དེ་དག་འགྲུབ་པར་མི་འཐད་དོ། །

[Block 1077]
བྱེད་པ་པོ་དང་ལས་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་བརྒྱད་པའོ།། །།

[Block 1078 [HEADING]]
## ཉེ་བར་ལེན་པ་པོ་དང་ཉེ་བར་བླང་བ་བརྟག་པ། ^9-0

[Block 1079]
དབུ་མ་རྩ་བའི་འགྲེལ་པ་བུད་དྷ་པཱ་ལི་ཏ། བམ་པོ་བཞི་པ། སྨྲས་པ། དེ་བཞིན་ཉེར་ལེན་ཤེས་པར་བྱ། །ཞེས་གང་བཤད་པ་དེ་ལ་སྨྲ་བར་བྱ་སྟེ།

[Block 1080 [VERSE]]
ལྟ་དང་ཉན་ལ་སོགས་པ་དང་། །
ཚོར་སོགས་དང་ཡང་དབང་བྱས་པ། །
གང་གི་ཡིན་པ་དེ་དག་གི། །
སྔ་རོལ་དེ་ཡོད་ཁ་ཅིག་སྨྲ། །

[Block 1081]
ལྟ་དང་ཉན་ལ་སོགས་པ་དང་། །ཞེས་བྱ་བ་ནི་ལྟ་བ་དང་ཉན་པ་ལ་སོགས་པའོ། །

[Block 1082]
ལྟ་བ་དང་ཉན་པ་ལ་སོགས་པ་དང་། ཚོར་བ་ལ་སོགས་པ་དག་གང་གི་ཉེ་བར་བླང་པ་ཡིན་པའི་དངོས་པོ་དེ་ལྟ་བ་དང་ཉན་པ་ལ་སོགས་པ་དང་། ཚོར་བ་ལ་སོགས་པ་དེ་དག་གི་སྔ་རོལ་ན་ཡོད་དོ་ཞེས་ཁ་ཅིག་དེ་སྐད་ཅེས་སྨྲའོ། །

[Block 1083]
དེ་ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1084 [VERSE]]
དངོས་པོ་ཡོད་པ་མ་ཡིན་ན། །
ལྟ་ལ་སོགས་པ་ཇི་ལྟར་འགྱུར། །
དེ་ཕྱིར་དེ་དག་སྔ་རོལ་ན། །
དངོས་པོ་གནས་པ་དེ་ཡོད་དེ། །

[Block 1085]
དངོས་པོ་ཡོད་པ་མ་ཡིན་ན། །ལྟ་བ་ལ་སོགས་པ་དག་ཇི་ལྟར་ཉེ་བར་བླང་བ་ཡིན་པར་འགྱུར། དེའི་ཕྱིར་མི་འཐད་པས་ལྟ་བ་ལ་སོགས་པ་དེ༌[^679]དག་གི་སྔ་རོལ་ན་ལྟ་བ་ལ་སོགས་པ་དག་གང་གི་ཉེ་བར་བླང་བ་ཡིན་པའི་དངོས་པོ་གནས་པ་དེ་ཡོད་དོ། །

[Block 1086]
ཉེ་བར་ལེན་པ་པོ་དེ་ཡོད་ན་ཉེ་བར་བླང་བ་ཡང་ལྟོས་པས་གདགས་སུ་ཡོད་པ་ཡིན་ན་དེ་ལ་ཁྱོད་ཅི་ཟེར། བཤད་པ།

[Block 1087 [VERSE]]
ལྟ་དང་ཉན་ལ་སོགས་པ་དང་། །
ཚོར་བ་ལ་སོགས་ཉིད་ཀྱི་ནི། །
སྔ་རོལ་དངོས་པོ་གང་གནས་པ། །
དེ་ནི་གང་གིས་གདགས་པར་བྱ། །

[Block 1088]
འདི་ལ་ལྟ་བ་དང་ཉན་པ་ལ་སོགས་པ་དང་། ཚོར་བ་ལ་སོགས་པ་དག་གིས་ལྟ་བ་པོ་དང་། ཉན་པ་པོ་དང་། ཚོར་བ་པོ་ཞེས་དངོས་པོ་གདགས་པར་བྱ་བ་ཡིན་ན་ལྟ་བ་ལ་སོགས་པ་དང་། ཚོར་བ་ལ་སོགས་པ་དག་གི་སྔ་རོལ་ན་ལྟ་བ་ལ་སོགས་པ་དག་གང་གི་ཉེ་བར་བླང་བ་ཞེས་བརྗོད་པའི་དངོས་པོ་ཡོད་དོ། །ཞེས་བརྟག་པའི་དངོས་པོ་དེ་འདི་ལྟར་གནས་ཏེ། ཡོད་དོ་ཞེས་གང་གིས་གདགས་པར་བྱ།

[Block 1089]
སྨྲས་པ། དེ་ནི་ལྟ་བ་ལ་སོགས་པ་དག་མེད་པར་ཡང་རང་ཉིད་ཀྱིས་རབ་ཏུ་གྲུབ་པར་ཡོད་དོ། །

[Block 1090]
བཤད་པ།
--- END BLOCKS ---
