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
[Block 2101 [VERSE]]
གལ་ཏེ་རྒྱུས་ནི་འབྲས་བུ་ལ། །
རྒྱུ་བྱིན་ནས་ནི་འགག་འགྱུར་ན། །
གང་བྱིན་པ་དང་གང་འགགས་པའི། །
རྒྱུ་ཡི་བདག་ཉིད་གཉིས་སུ་འགྱུར། །

[Block 2102]
གལ་ཏེ་རྒྱུས་འབྲས་བུ་ལ་རྒྱུ་བྱིན་ནས་འགག་པར་འགྱུར་ན། དེ་ལྟ་ན་གང་བྱིན་པ༌[^1383]དང་གང་འགགས་པ་དེས་རྒྱུའི་བདག་ཉིད་གཉིས་སུ་འགྱུར་རོ། །

[Block 2103]
རྒྱུའི་བདག་ཉིད་གཉིས་སུ་ནི་མི་འཐད་དེ། འགགས་པ་གང་ཡིན་པ་དེ་ནི་བསྐྱེད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2104]
རྒྱུ་བྱིན་པ༌[^1384]ཡང་མི་འཐད་དེ། འབྲས་བུ་ཡོད་པ་དང་མེད་པ་ལ་རྒྱུ་སྦྱིན་པར་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2105]
འདི་ལྟར་འབྲས་བུ་ཡོད་པ་ལ་ནི་ཡང་རྒྱུ་བྱིན་པས༌[^1385]ཅི་བྱ། མེད་པ་ལ་ནི་སུ་ལ་སྦྱིན་པར་བྱ། སྨྲས་པ། རྒྱུས་འབྲས་བུ་རྒྱུ་བྱིན་ནས་འགག་པ་མ་ཡིན་གྱི། འདི་ལྟར་རྒྱུ་འགགས་མ་ཐག་ཏུ་འབྲས་བུ་སྐྱེའོ། །

[Block 2106]
བཤད་པ།

[Block 2107 [VERSE]]
གལ་ཏེ་རྒྱུས་ནི་འབྲས་བུ་ལ། །
རྒྱུ་མ་བྱིན་པར་འགགས༌[^1386]གྱུར་ན། །
རྒྱུ་འགགས་ནས་ནི་སྐྱེས་པ་ཡི། །
འབྲས་བུ་དེ་ནི་རྒྱུ་མེད་འགྱུར། །

[Block 2108]
གལ་ཏེ་རྒྱུས་འབྲས་བུ་ལ་རྒྱུ་མ་བྱིན་པར་འགགས་པར༌[^1387]གྱུར༌[^1388]ན། རྒྱུ་འགགས་ཤིང་ཞིག་ནས་སྐྱེས་པའི་འབྲས་བུ་དེ་རྒྱུ་མེད་པ་ལས་བྱུང་བར་མི་འགྱུར་རམ། རྒྱུ་མེད་པ་ལས་བྱུང་བར་ནི་མི་འདོད་དེ་སྐྱོན་དུ་མར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2109]
སྨྲས་པ། འབྲས་བུ་ནི་རྒྱུ་དང་ཚོགས་པ་དག་དང་ལྷན་ཅིག་སྐྱེ་སྟེ༌[^1389]མར་མེ་དང་འོད་བཞིན་པ།[^1390] དེའི་ཕྱིར་ཚོགས་པ་དང་འབྲས་བུ་དུས་གཅིག་ཁོ་ནར་འབྱུང་ཞིང་མར་མེ་དང་འོད་བཞིན་པས། དེ་ལ་ཅི་ཚོགས་པ་ཉིད་ལ་འབྲས་བུ་ཡོད་དམ། མེད་ཅེས་བསམ་པ་དེ་མི་འཐད་དོ། །

[Block 2110]
བཤད་པ།

[Block 2111 [VERSE]]
གལ་ཏེ་ཚོགས་དང་ལྷན་ཅིག་ཏུ། །
འབྲས་བུ་ཡང་ནི་སྐྱེ་འགྱུར༌[^1391]ན། །
སྐྱེད༌[^1392]པ་དང་ནི་གང་བསྐྱེད་པ། །
དུས་གཅིག་པར་ནི་ཐལ་བར་འགྱུར། །

[Block 2112]
གལ་ཏེ་ཚོགས་པ་དང་འབྲས་བུ་ལྷན་ཅིག་ཁོ་ནར་སྐྱེ་བར་འགྱུར༌[^1393]ན། དེ་ལྟ་ན་སྐྱེད་པ༌[^1394]རྒྱུ་གང་ཡིན་པ་དང་བསྐྱེད་པ་དོན་གང་ཡིན་པ་དེ་དག་དུས་གཅིག་ཏུ་འབྱུང་བར་ཐལ་བར་འགྱུར་བས་དེ་ཡང་མི་འཐད་དེ། འདི་ལྟར་ཕ་དང་བུ་དག་དུས་གཅིག་ཏུ་ཇི་ལྟར་སྐྱེ་བར་འགྱུར། ཅི་སྟེ་ཡང་སྐྱེ་བར་འགྱུར་ན་ནི་དེ་ལ་འདི་ནི་འདིའི་རྒྱུའོ། །

[Block 2113]
འདི་ནི་འདིའི་འབྲས་བུའོ་ཞེས་རྣམ་པར་གཞག་པ༌[^1395]འདི་ཇི་ལྟར༌[^1396]ཡོད་པར་འགྱུར། དེ་ལྟ་བས་ན་ཚོགས་པ་ཉིད་དང་འབྲས་བུ་ལྷན་ཅིག་ཏུ་འོང་མ་འཐད་དོ། །

[Block 2114]
སྨྲས་པ། འབྲས་བུ་ནི་ཚོགས་པ་ཉིད་ཀྱི་སྔ་རོལ་ཉིད་ན་ཡང་དེ༌[^1397]དེ་ན༌[^1398]ཕྱིས་ཚོགས་པ་ཉིད་སྐྱེས་པས༌[^1399]གསལ་བར་བྱེད་དེ། མར་མེས་བུམ་པ་བཞིན་ནོ། །

[Block 2115]
བཤད་པ།

[Block 2116 [VERSE]]
གལ་ཏེ་ཚོགས་པའི་སྔ་རོལ་ན། །
འབྲས་བུ་སྐྱེས་པར་གྱུར་ན་ནི། །
རྒྱུ་དང་རྐྱེན་རྣམས་མེད་པ་ཡི། །
འབྲས་བུ་རྒྱུ་མེད་འབྱུང་བར་འགྱུར། །

[Block 2117]
གལ་ཏེ་འབྲས་བུ་སྔ་ན་ཡོད་པ་ཉིད་ཡིན་ལ་ཚོགས་པ་ཕྱིས༌[^1400]འབྱུང་བར་འགྱུར་ན། དེ་ལྟ་ན་རྒྱུ་དང་རྐྱེན་རྣམས་མེད་པ་དང་རྒྱུ་དང་རྐྱེན་རྣམས་མ་གཏོགས་པའི་འབྲས་བུ་རྒྱུ་མེད་པ་ལས་བྱུང་བར་འགྱུར་རོ། །

[Block 2118]
འབྲས་བུ་སྐྱེས་པ་ལ་ཡང་རྒྱུ་དང་རྐྱེན་ཚོགས་པ་ལ་ཡང་སྐྱེ་བར་བརྟགས༌[^1401]པས་ཅི་བྱ། འདི་ལྟར་འབྲས་བུའི་དོན་དུ་རྒྱུ་དང་རྐྱེན་ཚོགས་པར་འདོད་ན། འབྲས་བུ་དེ་ཡང་སྐྱེས་ཟིན་པ་ཉིད་དོ། །

[Block 2119]
དེ་ལྟ་བས་ན་དེ་ཡང་གྱི་ནའོ། །

[Block 2120]
སྨྲས་པ། རྒྱུ་ཡོངས་སུ་འགྱུར་བ་ལས་འབྲས་བུར་འགྲུབ་སྟེ། དེའི་ཕྱིར་གནས་སྐབས་སྔ་མ་འགག་པ་ལས་རྒྱུ་འགགས་ན་འབྲས་བུར་འགྱུར་རོ། །

[Block 2121]
དེ་ལྟ་ན་རྒྱུ་མ་འགགས་པར་ཡང་འབྲས་བུར་མི་འགྱུར་ལ། འབྲས་བུ་དེ༌[^1402]རྒྱུ་མེད་པ་ལས་བྱུང་བར་ཡང་མི་འགྱུར་རོ། །

[Block 2122]
བཤད་པ།

[Block 2123 [VERSE]]
གལ་ཏེ་རྒྱུ་འགགས་འབྲས་བུ་ན། །
རྒྱུ་ནི་ཀུན་ཏུ་འཕོ་བར་འགྱུར། །
སྔོན་སྐྱེས་པ་ཡི་རྒྱུ་ཡང་ནི། །
ཡང་སྐྱེ་བར་ནི་ཐལ་བར་འགྱུར། །

[Block 2124]
གལ་ཏེ་རྒྱུའི་དངོས་པོ་སྔར་འགགས་པ་ན་གནས་སྐབས་གཞན་ཐོབ་པ་འབྲས་བུ་ཞེས་བྱ་ན། དེ་ལྟ་ན་རྒྱུ་ཀུན་ཏུ་འཕོ་བར་འགྱུར་གྱི་སྐྱེ་བ་མ་ཡིན་ཏེ། དཔེར་ན་བྲོ་གར་མཁན་གྱིས་ཆ་ལུགས་གཞན་བོར་ནས་ཆ་ལུགས་གཞན་དུ་ཞུགས་པ་སྐྱེ་བ་མ་ཡིན་པ་བཞིན་ནོ། །

[Block 2125]
ཅི་སྟེ་ཡང་གནས་སྐབས་གཞན་དུ་ཀུན་ཏུ༌[^1403]འཕོ་བ་ཉིད་སྐྱེ་བ་ཡིན་ན་ནི། དེ་ལྟ་ན་ཡང་སྔོན་སྐྱེས་པའི་རྒྱུ་ཉིད་ཀྱང་སྐྱེ་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 2126]
དེ་ལྟ་ན་ཡང་དངོས་པོ་ཡོངས་སུ་འགྱུར་བའི་ཆོས་ཅན་རྣམས་ངེས་པར་མི་གནས་པའི་ཕྱིར་ནམ་ཡང་མི་སྐྱེ་བར་མི་འགྱུར་རོ། །

[Block 2127]
སྨྲས་པ་གང་གི་ཚེ་རྒྱུ་འགགས་པ་ན་འབྲས་བུར་འགྱུར་རོ་ཞེས་བརྗོད་པ་དེའི་ཚེ་ཅིའི་ཕྱིར་ཀུན་ཏུ༌[^1404]འཕོ་བར་འགྱུར་བ་དང་ཡང་སྐྱེ་བར་ཐལ་བར་འགྱུར་རོ་ཞེས་བརྗོད། བཤད་པ། ཅི་ཁྱོད་ལམ་དུ་ཞུགས་བཞིན་དུ་ལམ་འདྲིའམ། ཁྱོད་དངོས་པོ་ཡོངས་སུ་འགྱུར་བ་འབྲས་བུ་ཞེས་བྱའོ་ཞེས་ཟེར་བཞིན་དུ་རང་གི་ཚིག་གི་དོན་ཁོང་དུ་མ་ཆུད་དོ།[^1405] །

[Block 2128]
དེའི་ཕྱིར་ཁྱོད་ཚེགས་ཆེ་བས་ཆོག་གི་འདུག་ཤིག་དང་། ད་ཁོ་བོ་ཉིད་ཀྱིས་ཁྱོད་ཀྱིས་བསྟན་པའི༌[^1406]ལྟ་བ་རྒྱུ་དང་འབྲས་བུར་འབྲེལ་པར་རྣམ་པར་རྟོག་པ་དག་ཏུ་བསྟན་པར་བྱས། ཁྱོད་ཡིད་བསྡུས་ལ་དེ་དག་ཉོན་ཅིག །འདི་ལ་གལ་ཏེ་རྒྱུས་འབྲས་བུ་སྐྱེད་པར༌[^1407]གྱུར་ན་འགགས་པས་སམ་གནས་པས་སྐྱེད་པར་བྱེད་གྲང་། འབྲས་བུ་ཡང་སྐྱེད་པ༌[^1408]ཉིད་དམ་མ་སྐྱེས་པ་སྐྱེད་པར་བྱེད་གྲང་ན། རྣམ་པ་ཐམས་ཅད་ཀྱང་མི་འཐད་དོ། །ཇི་ལྟར་ཞེ་ན། འགགས་པ་ནུབ་པར་གྱུར་པ་ཡིས། །འབྲས་བུ་སྐྱེས་པ་ཇི་ལྟར་སྐྱེད།[^1409] །

[Block 2129 [VERSE]]
འབྲས་བུ་དང་ནི་འབྲེལ་པའི་རྒྱུ། །
གནས་པས་ཀྱང་ནི་ཇི་ལྟར་སྐྱེད། །

[Block 2130]
གལ་ཏེ་རེ་ཞིག་རྒྱུ་རྣམ་པ་ཐམས་ཅད་དུ་འགགས་པ་ནུབ་པར་གྱུར་པས་འབྲས་བུ་སྐྱེས་པ་སྐྱེད་པར༌[^1410]བྱེད་པར་རྟོག་ན། དེ་ནི་རིགས་པ་མ་ཡིན་ཏེ། འདི་ལྟར་རྒྱུ་འགགས་པ་ནུབ་པར་གྱུར་པས་འབྲས་བུ་སྐྱེས་པ་ཡོད་པ་ཉིད་ཇི་ལྟར་སྐྱེད་པར་བྱེད། རྒྱུ་མེད་པ་གང་གིས་སྐྱེད་པར་བྱེད་པར་བརྟག་པ་དེ་ཡང་གང་ཡིན། སྐྱེས་པ་ཉིད་ཡང་ཅི་ཞིག་བསྐྱེད་པར་བྱ་དགོས། ཅི་སྟེ་ཡང་འདི་སྙམ་དུ་འབྲས་བུ་དང་འབྲེལ་པའི་རྒྱུ་འབྲས་བུ་དང་ལྡན་པ་གནས་པ་ཉིད་ཀྱིས་འབྲས་བུ་སྐྱེད་པར་བྱེད་པར་སེམས་ན། དེ་ཡང་མི་འཐད་དེ། འདི་ལྟར་རྒྱུ་གནས་པས་འབྲས་བུ་ཡོད་པ་ཉིད་ཇི་ལྟར་སྐྱེད་པར་བྱེད། དེའི་ཕྱིར་གང་གི་ཚེ་འབྲས་བུ་སྐྱེས་པ་ཉིད་དང་རྒྱུར་འབྲེལ་པ་ཡིན་གྱི་མ་སྐྱེས་པ་དང་ནི་མ་ཡིན་ནོ། །

[Block 2131]
སྐྱེས་པ་ལ་ནི་ཡང་སྐྱེས་པའི༌[^1411]རྒྱུས་ཅི་བྱ། དེ་ལྟ་བས་ན་དེའང༌[^1412]མི་འཐད་པའོ།[^1413] །

[Block 2132 [VERSE]]
ཅི་སྟེ་རྒྱུ༌[^1414]འབྲས་མི༌[^1415]འབྲེལ་ན། །
འབྲས་བུ་གང་ཞིག་སྐྱེད་པར་བྱེད། །

[Block 2133]
ཅི་སྟེ་རྒྱུ་དེ་འབྲས་བུ་དང་མ་འབྲེལ་བ་འབྲས་བུ་དང་མི་ལྡན་པས་འབྲས་བུར་སྐྱེད༌[^1416]པར་བྱེད་པར་སེམས་ན། ཁྱོད་ཀྱི་འབྲས་བུ་གང་ཞིག་རྒྱུས་སྐྱེད་པར༌[^1417]བྱེད་པ་དེ་སྨྲོས་ཤིག །གང་གི་ཚེ་འབྲས་བུ་མ་སྐྱེས་པའི་ཕྱིར་མེད་པ་ལ་འབྲས་བུ་ཞེས་བྱ་བ་ཉིད་ཀྱང་མེད་པ་དེའི་ཚེ་རྒྱུས་འབྲས་བུ་སྐྱེད་པར༌[^1418]བྱེད་དོ་ཞེས་བྱ་བ་དེ་ཇི་ལྟར་འཐད་པར་འགྱུར། ཅི་སྟེ་ཡང་མེད་ཀྱང་དེ་ལ་དེ་སྐད་ཅེས༌[^1419]སྐྱེད་པར་བྱེད་པའི་མཐུ་ཉིད་ཡོད་པར་གྱུར་ན་ནི་དེས་རི་བོང་གི་རྭ་ཡང་བསྐྱེད་པར་འགྱུར་བར་ཐེ་ཚོམ་མེད་དོ། །

[Block 2134]
ཡང༌[^1420]གཞན་ཡང་།

[Block 2135 [VERSE]]
རྒྱུས་ནི་མཐོང་དང་མ་མཐོང་བར། །
འབྲས་བུ་སྐྱེད་པར་མི་བྱེད་དོ། །

[Block 2136]
འདི་ལ་གལ་ཏེ་རྒྱུས་འབྲས་བུ་བསྐྱེད་པར་གྱུར་ན་མཐོང་ནས་སམ་མ་མཐོང་བར་སྐྱེད་པར༌[^1421]འགྱུར་གྲང་ན། གཉི་ག་ལྟར་ཡང་མི་འཐད་དོ། །ཇི་ལྟར་ཞེ་ན། གལ་ཏེ་རེ་ཞིག་མཐོང་བས་སྐྱེད༌[^1422]པར་འགྱུར་ན། དེ་ལྟར་ན་སྐྱེས་པ་སྐྱེད་པར་བྱེད་པར་འགྱུར་ཏེ། འདི་ལྟར་མ་སྐྱེས་པ་ནི་མཐོང་བར་མི་འགྱུར་ལ། སྐྱེས་པ་ལ་ནི་ཡང་བསྐྱེད་པར༌[^1423]བྱ་མི་དགོས་སོ། །

[Block 2137]
ཅི་སྟེ་ཡང་རྒྱུས་མ་མཐོང་བར་འབྲས་བུ་སྐྱེད་པར་བྱེད་པར་རྟོག་ན། དེ་ལྟ་ན་ཡང་རྒྱུས་གང་དང་གང་མ་མཐོང་བ་དེ་དང་དེ་སྐྱེད་པར༌[^1424]འགྱུར་བ་ཞིག་ན་སྐྱེད་པར་ཡང་མི་བྱེད་དེ། དེ་ལྟ་བས་ན་རྒྱུས་མ་མཐོང་བར་ཡང་འབྲས་བུ་སྐྱེད་པར་མི་བྱེད་དོ། །

[Block 2138]
ཡང་གཞན་ཡང་། འདི་ལ་གལ་ཏེ་རྒྱུ༌[^1425]འབྲས་བུ་བསྐྱེད་པར་གྱུར་ན། ཕྲད་ནས་སྐྱེད་པར༌[^1426]འགྱུར་གྲང་ན། འབྲས་བུ་དང་རྒྱུ་དག་ཕྲད་པ་ནི་ཇི་ལྟར་ཡང་མི་འཐད་དོ། །ཇི་ལྟར་ཞེ་ན།

[Block 2139 [VERSE]]
འབྲས་བུ་འདས་པ་རྒྱུ་འདས་དང་། །
མ་སྐྱེས་པ་དང་སྐྱེས་པ་དང་། །
ལྷན་ཅིག་ཕྲད་པར་འགྱུར་བ་ནི། །
ནམ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2140]
འབྲས་བུ་འདས་པ་ནི་རྒྱུ་འདས་པ་དང་མ་སྐྱེས་པ་དང་ལྷན་ཅིག་ཕྲད་པར་འགྱུར་བ་ནམ་ཡང་ཡོད་པ་མ་ཡིན་ཏེ། འདས་པ་དང་མ་འོངས་པ་དག་གི་འབྲས་བུ་དང་རྒྱུ་དག་མེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
