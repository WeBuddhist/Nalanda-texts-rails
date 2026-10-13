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
[Block 1156]
འབར་བར་བྱེད་པའི་རྒྱུ་མེད་པ་ནི་འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་བ་སྟེ། འབར་བར་བྱེད་པ་མེད་པ་ཁོ་ནར་མེ་འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1157]
རྩོམ་པ་དོན་མེད་པ་ཉིད་དུ་ཡང་འགྱུར་རོ། །

[Block 1158]
དེ་ལྟ་ཡིན་ན་ལས་མེད་པའི་མེར་ཡང་འགྱུར་ཏེ། མེ་ཞེས་བྱ་བ་འདི་ནི་སྲེག་པར་བྱེད་པའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུའི་ལས་བསྟན་དུ་མེད་པར་ཡང་འགྱུར་རོ། །

[Block 1159]
སྨྲས་པ། མེ་འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་བར་འགྱུར་རོ་ཞེས་གང་བཤད་པ་དེ་ཇི་ལྟ་བུ། བཤད་པ།

[Block 1160 [VERSE]]
གཞན་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར། །
འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་། །

[Block 1161]
གང་གི་ཕྱིར་བུད་ཤིང་ལས་མེ་གཞན་ཉིད་ཡིན་པར་གྱུར་ན་བུད་ཤིང་མེད་པར་ཡང་འབྱུང་བར་ཐལ་བར་འགྱུར་བ་དེའི་ཕྱིར་གཞན་ལ་ལྟོས་པ་མེད་པ་ཡིན་ཏེ། འདི་ལྟར་མེ་བུད་ཤིང་ལ་ལྟོས་ན་ནི་གཞན་ལ་ལྟོས་པ་དང་བཅས་པར་གྱུར༌[^707]ན་དེ་ཡང་དེ་ལ་བུད་ཤིང་མེད་པས་གཞན་ལ་ལྟོས་པ་མེད་པ་ཡིན་ལ། གཞན་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར་འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་བར་འགྱུར་རོ། །

[Block 1162]
འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་བར་གྱུར༌[^708]ན་རྟག་ཏུ་འབར་བ་ཉིད་དུ་ཐལ་བར་འགྱུར་ཏེ། འདི་ལྟར་མེ་འབར་བྱེད་ལ་ལྟོས་ན་ནི་འབར་བྱེད་མེད་ན་དེ་འཆི་བར་འགྱུར་བ་ཞིག་ན། དེ་ལ་འབར་བྱེད་དེ་ཡང་མེད་པས་རྟག་ཏུ་འབར་བ་ཉིད་དུ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 1163 [VERSE]]
རྟག་ཏུ་འབར་བ་ཉིད་ཡིན་ན། །
རྩོམ་པ་དོན་མེད་ཉིད་དུ་འགྱུར། །

[Block 1164]
མེ་རྟག་ཏུ་འབར་བ་ཉིད་ཡིན་ན་ནི་བྱུང་བ༌[^709]དང་སྦར་བ༌[^710]ལ་སོགས་པ་རྩོམ་པ་དག་དོན་མེད་པ་ཉིད་དུའང་འགྱུར་རོ། །

[Block 1165]
དེ་ལྟ༌[^711]ན་ལས་མེད་པར་ཡང་ཐལ་བར་འགྱུར་ཞིང་། རྣམ་པ་དེ་ལྟ་བུ་ནི་མི་འཐད་པས༌[^712]མེ་མེད་པ་ཉིད་དུ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 1166 [VERSE]]
དེ་ལ་གལ་ཏེ་འདི་སྙམ་དུ། །
སྲེག་ཤིང་བུད་ཤིང་ཡིན་སེམས་ན། །

[Block 1167]
དེ་ལ་གལ་ཏེ་ལ་ལས་འདི་སྙམ་དུ་གང་གི་ཕྱིར་མེས་ཁྱབ་ཅིང་མེས་བསྲེག༌[^713]བཞིན་པ་བུད་ཤིང་ཡིན་པ་དེའི་ཕྱིར་གཞན་ཉིད་ཡིན་ཡང་མེ་ལ་བུད་ཤིང་མེད་པ་མ་ཡིན་གྱི། བུད་ཤིང་དང་བཅས་པ་ཉིད་ཡིན་པས་དེ་ལ་བུད་ཤིང་མེད་པར་ཐལ་བར་གྱུར་ན་སྐྱོན་གང་དག་བསྟན་པ་དེ་དག་ཏུ་མི་འགྱུར་བར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 1168 [VERSE]]
གང་ཚེ་དེ་ཙམ༌[^714]དེ་ཡིན་ན། །
གང་གིས་བུད་ཤིང་དེ་སྲེག་བྱེད། །

[Block 1169]
གང་གི་ཚེ་བསྲེག༌[^715]བཞིན་པ་དེ་ཙམ་ན་དེ་ཉིད་ཡིན་ཞིང་གཞན་གང་དང་ལྡན་པས་ཀྱང་བསྲེག་བཞིན་པ་མ་ཡིན་ན་བུད་ཤིང་གི་གནས་སྐབས་ཀྱི་སྔ་རོལ་ན་མེ་ཞེས་བྱ་བ་གང་གིས་ཁྱབ་ཅིང་གང་གིས་བསྲེག༌[^716]བཞིན་པ་ན་བུད་ཤིང་ཡིན་པར་འགྱུར་བ་གཞན་དེ་གང་ཡིན། བསྲེག༌[^717]བཞིན་པའི་གནས་སྐབས་ཉིད་ལ་ཡང་ཅི་བུད་ཤིང་གང་ཁོ་ན་ཡིན་པ་དེ་ཉིད་མེ་ཡིན་ནམ། འོན་ཏེ་མེ་ཡང་གཞན་ལ་བུད་ཤིང་ཀྱང་གཞན་ཞེས་བསམ་པ་འདི་འབྱུང་ལ། ཁྱོད་ཀྱིས་ཀྱང་བསྲེག༌[^718]བཞིན་པའི་གནས་སྐབས་ཉིད་ལ་མེས་ཁྱབ་ཅིང་མེས་བསྲེག༌[^719]བཞིན་པ་བུད་ཤིང་ཡིན་ནོ་ཞེས་སྨྲས་པ་དེའི་ཚེ་གང་གི་ཕྱིར་མེས་ཁྱབ་ཅིང་མེས་བསྲེག་བཞིན་པ་བུད་ཤིང་ཡིན་པ་དེའི་ཕྱིར་མེ་ལ་བུད་ཤིང་མེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ཇི་ལྟར་སྨྲ་བ་རིགས་སོ།[^720] ། དེ་ལྟ་བས་ན་གཞན་ཉིད་ཡིན་ན་ཡང་སྐྱོན་དུ་ཐལ་བར་འགྱུར་བ་དེ་དག་སོ་ན་གནས་བཞིན་ནོ། །

[Block 1170]
ཡང་གཞན་ཡང་།

[Block 1171 [VERSE]]
གཞན་ན་མི་ཕྲད་ཕྲད་མེད་ན། །
སྲེག་པར་མི་འགྱུར་མི་སྲེག་ན། །
འཆི་བར་མི་འགྱུར་མི༌[^721]འཆི༌[^722]ན། །
རང་གི་བརྟགས་དང་ལྡན་པར་གནས། །

[Block 1172]
མེ་གཞན་ཡིན་ན་བུད་ཤིང་དང་མི་ཕྲད་པར་འགྱུར་རོ། །

[Block 1173]
ཕྲད་པ་མེད་ན་དེ་སྲེག་པར་མི་འགྱུར་རོ། །

[Block 1174]
ཅི་སྟེ་ཕྲད་པ་མེད་ཀྱང་སྲེག་པར་འགྱུར་ན་ནི། ཕྱོགས་གཅིག་ན་འདུག་པས་འགྲོ་བ་མཐའ་དག་སྲེག་པར་འགྱུར་བས་དེའི་ཕྱིར་ཕྲད་པ་དེ་མི་འཐད་པས་གཞན་ཉིད་ཡིན་ཡང་བསྲེག༌[^723]བཞིན་པ་ན་བུད་ཤིང་ཡིན་ནོ་ཞེས་གང་སྨྲས་པ་དེ་མི་འཐད་དོ། །

[Block 1175]
མི་སྲེག་ན་འཆི་བར་མི་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་མེས་བུད་ཤིང་བསྲེགས༌[^724]ན་ནི་བུད་ཤིང་ཟད་པས་འཆི་བར་ཡང་འགྱུར་བ་ཞིག་ན། མི་སྲེག་པ་ལ་འཆི་བ་རྒྱུ་མེད་པ་ལས་བྱུང་བ་ཇི་ལྟར་འབྱུང་བར་འགྱུར། མི་འཆི་ན་ནི་གཞན་ལ་མི་ལྟོས་པ་འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་བ་རྟག་ཏུ་འབར་བ་དང་། གང་གི་རྟགས༌[^725]དང་ལྡན་པ་ཐེར་ཟུག་ཏུ་གནས༌[^726]ཉིད་དུ་གནས་པར་འགྱུར་རོ། །

[Block 1176]
ཡང་ན་ནི་དེ་བུད་ཤིང་ལས་གཞན་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 1177]
སྨྲས་པ། མེ་གཞན་ཡིན་ན་བུད་ཤིང་དང་མི་ཕྲད་པར་འགྱུར་རོ་ཞེས་གང་བཤད་པ་དེ་ལ་སྨྲ་བར་བྱ་སྟེ།

[Block 1178 [VERSE]]
གལ་ཏེ་ཤིང་ལས་མེ་གཞན་ཡང་། །
ཤིང་དང་ཕྲད་དུ་རུང་བར་འགྱུར། །

[Block 1179]
གལ་ཏེ་བུད་ཤིང་ལས་མེ་གཞན་ཡིན་ན་ཡང་བུད་ཤིང་དང་ཕྲད་དུ་རུང་བར་འགྱུར་རོ། །ཇི་ལྟར་ཞེ་ན།

[Block 1180 [VERSE]]
ཇི་ལྟར་བུད་མེད་སྐྱེས་པ་དང་། །
སྐྱེས་པའང་བུད་མེད་ཕྲད་པ་བཞིན། །

[Block 1181]
བཤད་པ།

[Block 1182 [VERSE]]
གལ་ཏེ་མེ་དང་ཤིང་དག་ནི། །
གཅིག་གིས་གཅིག་ནི་བསལ་གྱུར་ན། །
ཤིང་ལས་མེ་གཞན་ཉིད་ཡིན་ཡང་། །
ཤིང་དང་ཕྲད་པར་འདོད་ལ་རག །

[Block 1183]
གལ་ཏེ་མེ་དང་བུད་ཤིང་དག་སྐྱེས་པ་དང་བུད་མེད་དག་བཞིན་དུ་གཅིག་གིས་གཅིག་བསལ་བར༌[^727]གྱུར་ན་ནི་བུད་ཤིང་ལས་མེ་གཞན་ཉིད་ཡིན་ཡང་ཁྱོད་ཀྱི་ཡིད་ལ་བསམས་པ༌[^728]བཞིན་དུ། ཇི་ལྟར་བུད་མེད་སྐྱེས་པ་དང་ཕྲད་པ་དང་། སྐྱེས་པ་བུད་མེད་དང་ཕྲད་པ་བཞིན་དུ་བུད་ཤིང་དང་ཕྲད་པར་ཡང་འདོད་ལ་རག་ན་གང་གི་ཚེ་བསྲེག༌[^729]བཞིན་པའི་གནས་སྐབས་ཉིད་ལ་བསམ་པ་འདི་འབྱུང་བ་དེའི་ཚེ་མེ་དང་བུད་ཤིང་ཕྲད་པར་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་འཐད་པར་ག་ལ་འགྱུར།

[Block 1184]
སྨྲས་པ། འདིར་དེ་གཉིས་གཅིག་པ་ཉིད་ཀྱང་མ་ཡིན་ལ། གཞན་ཉིད་ཀྱང་མ་ཡིན་པ༌[^730]དེ་ཉིད་རིགས་པས་དེ་གཉིས་གཅིག་པ་ཉིད་དམ། གཞན་ཉིད་དུ་མ་གྱུར་ཀྱང་གོ༌[^731]སླ་སྟེ། རེ་ཞིག་མེ་དང་བུད་ཤིང་དག་ནི་རབ་ཏུ་གྲུབ་པ་ཡིན་ནོ། །

[Block 1185]
བཤད་པ། དེ་ནི་བཞད་གད་ཁོ་ནར་འགྱུར་ཏེ།

[Block 1186 [VERSE]]
གང་དག་དངོས་པོ་གཅིག་པ་དང་། །
དངོས་པོ་གཞན་པ་ཉིད་དུ་ནི། །
གྲུབ་པར་གྱུར་པ་ཡོད་མིན་པ། །
དེ་གཉིས་གྲུབ་པ་ཇི་ལྟར་ཡོད། །

[Block 1187]
སྨྲས་པ། ཕན་ཚུན་ལྟོས་པ་ལས་བུད་ཤིང་ལ་ལྟོས༌[^732]ནས་མེ༌[^733]ཡིན་ལ། མེ་ལ་ལྟོས་ནས་བུད་ཤིང་ཡིན་ནོ། །

[Block 1188]
བཤད་པ།

[Block 1189 [VERSE]]
གལ་ཏེ་ཤིང་ལྟོས་མེ་ཡིན་ལ། །
གལ་ཏེ་མེ་ལྟོས་ཤིང་ཡིན་ན། །
གང་ལ་ལྟོས་པའི་མེ་དང་ཤིང་། །
དང་པོར་གྲུབ་པ་གང་ཞིག་ཡིན། །

[Block 1190]
གལ་ཏེ་བུད་ཤིང་ལ་ལྟོས་ནས་མེ་ཡིན་ལ། མེ་ལ་ལྟོས་ནས་ཀྱང༌[^734]ཤིང་ཡིན་ན། གང་ལ་ལྟོས་ནས་མེ་ཡིན་པར་འགྱུར་བ་འམ། བུད་ཤིང་ཡིན་པར་འགྱུར་བ་དེ་གཉིས་ལས་དང་པོར་གྲུབ་པ་གང་ཡིན། དེ་ལ་འདི་སྙམ་དུ་བུད་ཤིང་དང་པོར་གྲུབ་པ་དེ་ལ་ལྟོས་ནས་མེ་ཡིན་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 1191 [VERSE]]
གལ་ཏེ་ཤིང་ལྟོས་མེ་ཡིན་ན། །
མེ་གྲུབ་པ་ལ་སྒྲུབ་པར་འགྱུར། །

[Block 1192]
གལ་ཏེ་བུད་ཤིང་དང་པོར་གྲུབ་པ་ལ་དེ་ལྟོས་ནས་མེ་ཡིན་པར་འགྱུར་ན་དེ་ལྟར༌[^735]ན་མེ་གྲུབ་ཟིན་པ་ལ་ཡང་སྒྲུབ་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1193]
ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་མེ་གྲུབ་ན་བུད་ཤིང་ལ་ལྟོས་པར་འཐད་ཀྱི། མེ་མ་གྲུབ་ཅིང་མེད་ན་ཇི་ལྟར་བུད་ཤིང་ལ་ལྟོས་པར་བྱེད་དོ།[^736] །དེའི་ཕྱིར་བུད་ཤིང་མེད་པར་ཡང་མེ་རང་གིས་གྲུབ་པ་ལྟོས་པར་ནུས་པ་ལ་ཁྱོད་ཡང་བུད་ཤིང་ལ་ལྟོས་ནས་རབ་ཏུ་འགྲུབ་པར་འགྱུར་བ་དོན་མེད་པ་ཡོད་དམ། ཡང་གཞན་ཡང་།

[Block 1194 [VERSE]]
བུད་པར་བྱ་བའི་ཤིང་ལ་ཡང་། །
མེ་མེད་པར་ནི་འགྱུར་བ་ཡིན། །

[Block 1195]
དེ་ལྟ་ན་བུད་ཤིང་ལ་ཡང་མེ་མེད་པར་འགྱུར་བ་ཡིན་ནོ། །
--- END BLOCKS ---
