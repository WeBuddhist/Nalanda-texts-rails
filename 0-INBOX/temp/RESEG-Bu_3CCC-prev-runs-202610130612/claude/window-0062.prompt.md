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
[Block 2171]
འདི་ནི་འབྲས་བུའོ་ཞེས་གཞན་ཉིད་དུ་གྱུར་ན། དེ་ལྟ་ན་ཡང་རྒྱུ་དང་རྒྱུ་མ་ཡིན་པ་དག་མཚུངས་པར་འགྱུར་རོ། །

[Block 2172]
ཇི་ལྟར་ནས་ཀྱི་མྱུ་གུ་ལས་འབྲས་ཀྱི་ས་བོན་གཞན་ཡིན་པ་དེ་བཞིན་དུ་འབྲས་ཀྱི་མྱུ་གུ་ལས་ཀྱང་ནས་ཀྱི་ས་བོན་གཞན་ཡིན་ན། དེ་ལ་ནས་ཀྱི་ས་བོན་ནི་ནས་ཀྱི་མྱུ་གུའི་རྒྱུ་ཡིན་གྱི་འབྲས་ཀྱི་ས་བོན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ཅིའི་ཕྱིར་དེ་ལྟར་འགྱུར། དེ་ལྟ་བས་ན་རྒྱུ་དང་འབྲས་བུ་དག་གཅིག་པ་ཉིད་ཀྱང་མ་ཡིན་ལ་གཞན་ཉིད་དུ་ཡང་མི་འཐད་དོ། །

[Block 2173]
གང་དག་ལ་གཅིག་པ་ཉིད་དང་གཞན་ཉིད་དུ་གྲུབ་པ་ཡོད་པ་མ་ཡིན་པ་དེ་དག་ལ་གྲུབ་པ་མེད་དེ། དེ་དག་ལས་གཞན་དུ་འགྲུབ་ལ༌[^1447]མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2174]
ཡང་གཞན་ཡང་། གལ་ཏེ་རྒྱུས་འབྲས་བུ་སྐྱེད་པར་བྱེད་ན་དེ་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པར་འགྱུར་བ་ཞིག་སྐྱེད་པར་བྱེད་དམ། མེད་པར་གྱུར་པ་ཞིག་སྐྱེད་པར་བྱེད་གྲང་ན། དེ་ལ་ཁོ་བོས་བཤད་པར་བྱ་སྟེ། འབྲས་བུ་ངོ་བོ་ཉིད་ཡོད་ན། །རྒྱུས་ནི་ཅི་ཞིག་སྐྱེད་པར༌[^1448]བྱེད།[^1449] །

[Block 2175 [VERSE]]
འབྲས་བུ་ངོ་བོ་ཉིད་མེད་ན། །
རྒྱུས་ནི་ཅི་ཞིག་བསྐྱེད་པར་འགྱུར། །

[Block 2176]
གལ་ཏེ་འབྲས་བུ༌[^1450]ངོ་བོ་ཉིད་ཀྱིས༌[^1451]ཡོད་པར་གྱུར་ན་མ་བྱས་ཀྱང་རྫོགས་པར་ཡོད་པ་ཉིད་ཡིན་པས་དེ་ཡོད་ན། རྒྱུས་དེ་ལ་གཞན་ཅི་ཞིག་སྐྱེད་པར༌[^1452]འགྱུར། ཅི་སྟེ་དེ་ཉིད་སྐྱེད་པར་བྱེད་དོ་ཞེས་རྟོག་ན་དེ་ནི་མི་རིགས་ཏེ། སྐྱེས་པ་ལ་ཡང་སྐྱེ་བའི་བྱ་བ་མེད་དོ། །

[Block 2177]
ཅི་སྟེ་འབྲས་བུ་དེ་ངོ་བོ་ཉིད་ཀྱིས༌[^1453]མེད་པར་གྱུར་པ་ཡིན་ན་དེ་རྒྱུས་ཇི་ལྟར་སྐྱེད་པར༌[^1454]འགྱུར། ཅི་སྟེ་འབྲས་བུ་ངོ་བོ་ཉིད་ཀྱིས་མེད་ཀྱང་རྒྱུས་བསྐྱེད་པར་འགྱུར་ན་ནི། ཤིང་བ་ཊའི་མེ་ཏོག་གིས་ཀྱང་ཕྲེང་བ་འཆིང་བར༌[^1455]ཐེ་ཚོམ་མེད་དོ། །

[Block 2178]
དེ་ལྟ་བས་ན་འབྲས་བུ་ཡོད་པར་འགྱུར་བ་དང་འབྲས་བུ་མེད་པར་འགྱུར་བ༌[^1456]ཡང་རྒྱུས་བསྐྱེད་པར་མི་འཐད་དོ། །

[Block 2179 [VERSE]]
སྐྱེད་པར་བྱེད༌[^1457]པ་མ་ཡིན་ན། །
རྒྱུ་ཉིད་འཐད་པར་མི་འགྱུར་རོ། །

[Block 2180]
རྒྱུ་གང་གིས་ཀྱང་འབྲས་བུ་སྐྱེད་པར་མི་བྱེད་ན། དེ་རྒྱུ་ཉིད་དུ་འཐད་པར་མི་འགྱུར་རོ། །

[Block 2181]
འདི་ལྟར་སྐྱེད་པར་བྱེད་པའི༌[^1458]རྒྱུ་ཞེས་བྱ་བ༌[^1459]ན་ཅི་སྟེ་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་ཡང་རྒྱུར་འགྱུར་ན་ནི། དེ་ལྟ་ན་འགར་ཡང༌[^1460]རྒྱུ་མ་ཡིན་པར་མི་འགྱུར་བས་ཐམས་ཅད་རྒྱུ་ཉིད་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་གང་ཡིན་པ་དེ་ཡང་མི་འདོད་དོ། །

[Block 2182]
དེ་ལྟ་བས་ན་རྒྱུ་ཉིད་འཐད་པར་མི་འགྱུར་རོ། །

[Block 2183 [VERSE]]
རྒྱུ་ཉིད་འཐད་པ་ཡོད་མིན་ན། །
འབྲས་བུ་གང་གི་ཡིན་པར་འགྱུར། །

[Block 2184]
གལ་ཏེ་འབྲས་བུ་བསྐྱེད་པའི་རྒྱུ་ཉིད་ཡོད་པ་མ་ཡིན་ན། རྒྱུ་མེད་ན་འབྲས་བུ་དེ་གང་གི་ཡིན་པར་འགྱུར། འདི་ལྟར་རྒྱུའི་འབྲས་བུ༌[^1461]ཡིན་པར་འདོད་ན་དེ་ཡང་མེད་དེ། [^1462]དེ་མེད་ན་འབྲས་བུ་ཞེས་བྱ་བར་མི་འཐད་དོ། །

[Block 2185]
ཅི་སྟེ་འཐད་ན་ནི་ཕ་མེད་པར་ཡང་བུ་ཡོད་པར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དོ། །

[Block 2186]
དེ་ལྟ་བས་ན། རྒྱུ་ཡོད་པ་མ་ཡིན་ན་འབྲས་བུ་ཡོད་པ་ཡང༌[^1463]མ་ཡིན་ནོ། །

[Block 2187]
རྒྱུ་རྣམས་དང་ནི་རྐྱེན་དག་གི །

[Block 2188 [VERSE]]
[^1464]ཚོགས་པ་གང་ཡིན་དེ་ཡིས་ནི། །
བདག་གིས་བདག་ཉིད་མི་སྐྱེད༌[^1465]ན། །
འབྲས་བུ་ཇི་ལྟར་སྐྱེད་པར་བྱེད། །

[Block 2189]
རྒྱུ་དང་རྐྱེན་རྣམས་ཀྱི་ཚོགས་པ་འབྲས་བུ་སྐྱེད་པར་བྱེད་པ་ཞེས་བྱ་བར་བརྟག་པ་གང་ཡིན་པ་དེས་རེ་ཞིག་བདག་གིས་བདག་ཉིད་སྐྱེད་པར་མི་བྱེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། ཚོགས་པ་ནི་དུ་མ་ཡིན་པར་ཤེས་པའི་ཕྱིར་ཏེ། སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 2190 [VERSE]]
ཚོགས་པ་གཅིག་པུ་མ་ཡིན་ཏེ། །
དེ་བཞིན་དངོས་པོ་འགའ་ཡང་མེད། །
གལ་ཏེ་དེ་ཡང་དེ་ལས་གཞན། །
དེ་ཡང་གཅིག་པུ་འགའ་ཞིག་ཡོད། །

[Block 2191]
ཅེས་གསུངས་སོ། །

[Block 2192]
ད་ཚོགས་པ་གང་ཡིན་པ་བདག་ཉིད་མ་སྐྱེས་པ་བདག་ཉིད་རབ་ཏུ་མ་གྲུབ་པ་དེས་འབྲས་བུ་ཇི་ལྟར་སྐྱེད་པར་བརྟག །ཅི་སྟེ་ཚོགས་པ་བདག་ཉིད་མ་སྐྱེས་པས་ཀྱང་འབྲས་བུ་སྐྱེད་པར་བྱེད་ན་ནི་མ་མ་སྐྱེས་པས་ཀྱང་བུ་སྐྱེད༌[^1466]པར་མངོན་པར་འགྱུར་རོ། །

[Block 2193 [VERSE]]
དེ༌[^1467]ཕྱིར་ཚོགས་པས་བྱས་པ་དང་། །
ཚོགས་མིན་བྱས་པའི་འབྲས་བུ་མེད། །
འབྲས་བུ་ཡོད་པ་མ་ཡིན་ན། །
རྐྱེན་གྱི་ཚོགས་པ་ག་ལ་ཡོད། །

[Block 2194]
དེ་ལྟར་གང་གི་ཕྱིར་ཚོགས་པ་དེ་བདག་ཉིད་མ་སྐྱེས་ཤིང་རབ་ཏུ་མ་གྲུབ་པ་དེའི་ཕྱིར་ཚོགས་པས་བྱས་པའི་འབྲས་བུ་མེད་དོ། །

[Block 2195]
དེ་ལ་འདི་སྙམ་དུ་ཚོགས་པ་མ་ཡིན་པས་བྱས་པའི་འབྲས་བུ་ཡོད་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ། ཚོགས་མིན་བྱས་པའི་འབྲས་བུ་མེད། །གང་གི་ཚེ་ཚོགས་པས་བྱས་པའི་འབྲས་བུ་ཉིད་མི་འཐད་པ་དེའི་ཚོགས་པ་མ་ཡིན་པས་བྱས་པའི་འབྲས་བུ་རྒྱུ་མེད་པ་ལས་བྱུང་བ་ཇི་ལྟར་འཐད་པར་འགྱུར། ཅི་སྟེ་འགྱུར་ན་ནི་ཕ་དང་མ་དག་མེད་པར་ཡང་བུ་སྐྱེ་བར༌[^1468]འགྱུར་བ་ཞིག་ན་སྐྱེ་བར་ཡང་མི་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་ཚོགས་པ་མ་ཡིན་པས་བྱས་པའི་འབྲས་བུ་ཡང་མེད་དོ། །

[Block 2196]
སྨྲས་པ། འཇིག་རྟེན་པ་དང་འགལ་བ་ཤིན་ཏུ་མང་པོ་ཞིག་བཤད་པ་འདིས་ཅི་བྱ། ཡོད་ན༌[^1469]རེ་ཞིག་རྒྱུ་དང་རྐྱེན་རྣམས་ཀྱི་ཚོགས་པ་ཡོད་དེ་དེ་ཡོད༌[^1470]པས་འབྲས་བུ་ཡང་ཡོད་པར་འགྱུར་རོ། །

[Block 2197]
བཤད་པ། ཅི་ཁྱོད་གྲོང་སྟོད་དུ་མཁར་ལྡན་འབེབས་སམ། ཁྱོད་འབྲས་བུ་ཡོད་པ་མ་ཡིན་ན་ཚོགས་པ་ཡོད་པར་འདོད་ཀོ །འབྲས་བུ་སྐྱེད་པ༌[^1471]ཉིད་ཚོགས་པ་ཞེས་བྱ་ན་འབྲས་བུ་དེ་ཉིད་ཀྱང་གང་གི་ཚེ་ཇི་ལྟར་ཡང་མི་འཐད་པ་དེའི་ཚེ་འབྲས་བུ་ཡོད་པ་མ་ཡིན་ན་རྐྱེན་གྱི༌[^1472]ཚོགས་པ་ཡོད་པར་ག་ལ་འགྱུར། སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 2198 [VERSE]]
གང་ཕྱིར་འཇིག་རྟེན་ཇི་སྙེད་མིང་། །
ཚོགས་པ་ཉིད་ལ་སྣང་འགྱུར་བ། །
དེ་ཕྱིར་དངོས་པོ་ཡོད་མིན་ཏེ། །
དངོས་མེད་ཚོགས་པའང་ཡོད་མ་ཡིན། །

[Block 2199]
ཞེས་གསུངས་སོ། །

[Block 2200]
དེ་ལྟ་བས་ན་འབྲས་བུ་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་ཚོགས་པ་ཡང་ཡོད་པ་མ་ཡིན་པས། དེ་ལ་དུས་དང་ཚོགས་པ་ཉིད་ཀྱི་འབྲས་བུ་འགྲུབ་པའི་ཕྱིར་དུས་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ནོ་ཞེས་གང་སྨྲས་པ། དེ་མི་འཐད་དོ། །

[Block 2201]
སྨྲས་པ། གལ་ཏེ་དུས་ཀྱང་མེད་རྒྱུ་དང་འབྲས་བུ་དང་ཚོགས་པ་ཡང་མེད་ན་གཞན་ཅི་ཞིག་ཡོད་དེ། དེ་ལྟ་བས་ན་དེ་ནི་མེད་པར་སྨྲ་བ་ཉིད་ཡིན་ནོ། །

[Block 2202]
བཤད་པ། མ་ཡིན་ཏེ་ཇི་ལྟར་ཁྱོད་དུས་ལ་སོགས་པ་དག་ངོ་བོ་ཉིད་ལས་ཡོད་པར་ཡོངས་སུ་རྟོག་པར་བྱེད་པ་དེ་ལྟར་མི་འཐད་པར་ཟད་ཀྱི། དེ་དག་བརྟེན་ནས་གདགས་པར་ནི་འགྲུབ་བོ། །

[Block 2203]
རྒྱུ་དང་འབྲས་བུ་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་ཉི་ཤུ་པའོ།། །།

[Block 2204 [HEADING]]
## འབྱུང་བ་དང་འཇིག་པ་བརྟག་པ། ^21-0

[Block 2205]
སྨྲས་པ། དུས་ལ་སོགས་པ་དག་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གང་གི་ཚེ་གང་ན་འགའ་ཞིག་འབྱུང་བ་དང་། འཇིག་པ་དག་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2206]
འདི་ལྟར་གལ་ཏེ་དུས་ལ་སོགས་པ་དག་མེད་པར་འགྱུར༌[^1473]ན། འོ་ན་དེ་ལྟ་ན་ཁྱད་པར་མེད་པས་དུས་ཐམས་ཅད་དུ་ཐམས་ཅད་ནས་ཐམས་ཅད་ཀྱང་། འབྱུང་བ་དང་འཇིག་པ་དག་ཏུ་འགྱུར་བ་ཞིག་ན་དེ་ལྟར་ཡང་མི་འགྱུར་བས། དེའི་ཕྱིར་དུས་ལ་སོགས་པ་དག་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2207]
བཤད་པ། གལ་ཏེ་འགའ་ཞིག་ལ་འབྱུང་བ་དང་འཇིག་པ་དག་ཉིད་ཡོད་པར་གྱུར་ན་ནི། དུས་ལ་སོགས་པ་དག་ཀྱང་ཡོད་པར་འགྱུར་བ་ཞིག་ན། གང་གི་ཚེ།

[Block 2208 [VERSE]]
འཇིག་པ་འབྱུང་བ་མེད་པར་རམ། །
ལྷན་ཅིག་ཡོད་པ་ཉིད་མ་ཡིན། །
འབྱུང་བ་འཇིག་པ་མེད་པར་རམ། །
ལྷན་ཅིག་ཡོད་པ་ཉིད་མ་ཡིན། །

[Block 2209]
དེའི་ཚེ་གལ་ཏེ་འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པར་གྱུར་ན། ཕན་ཚུན་མེད་པར་རམ་ལྷན་ཅིག་ཏུ་འགྱུར་གྲང་ན། གང་གི་ཚེ་གཉི་ག་ལྟར་ཡང་མི་འཐད་པ་དེའི་ཚེ་དེ་དག་གི་རྒྱུ་ཅན་གྱི་དུས་ལ་སོགས་པ་དག་ཇི་ལྟར་ཡོད་པར་གྱུར།[^1474] དེ་ཇི་ལྟར་ཞེ་ན། མི་འཐད་པའི་ཕྱིར་ཏེ།

[Block 2210 [VERSE]]
འཇིག་པ་འབྱུང་བ་མེད་པར་ནི། །
ཇི་ལྟ༌[^1475]བུར་ན་ཡོད་པར་འགྱུར། །
འཆི་བ་སྐྱེ་བ་མེད་པ་ལྟར། །
འཇིག་པ་འབྱུང་བ་མེད་པར་མེད། །
--- END BLOCKS ---
