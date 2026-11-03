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

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

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
སློང་བ་ཉིད་ནི་སློང་བའོ། །

[Block 2172]
སློང་བ་ཉིད་ཀྱི་ཚིག་ཡིན་པས་སློང་བའི་ཚིག་སྟེ། དོན་དུ་གཉེར་བའི་ཚིག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2173]
མ་ཕྱིན་པ་ནི་མི་ནུས་པ་ཞེས་བྱ་བའི་དོན་ཏེ། སྣང་བ་མེད་པ་དང་། མི་མཉམ་པའི་འཇིག་རྟེན་པའོ། །གང་ལས་ཤེ་ན། མི་མཉམ་པའི་ལམ་ལས་འཇིག་རྟེན་འགྲོ་བ་ཉིད་དུ་སྣང་བའི་ཕྱིར་ཏེ། གཞན་ནི་མི་འགྲོ་བ་ཡིན་ནོ་ཞེས་དོན་གྱིས་རྟོགས་པའོ།[^1360] །དེ་བས་ན་བསྟན་པའི་སྐྱོན་གཉིས་མེད་དེ། མཐོང་བཞིན་དུ་ལམ་མཉམ་པ་ནས་འགྲོ་བར་སྣང་བའི་ཕྱིར་ཁྱོད་ཉིད་ལ་ཕྱིན་པ་ཡིན་ལ། གཞན་པ་མི་སློང༌[^1361]བའི་ཚིག་ཕྱིན་པ་མ་ཡིན་ནོ་ཞེས་སྦྱར༌[^1362]རོ། །

[Block 2174]
དེའི་རྒྱུ་སྐྱོན་གཉིས་དང་བྲལ་བ་མེད་ན་ནི་དེ་ཇི་ལྟར་སློང་བའི་དབང་དུ་བྱས་ནས། སྦྱིན་པ་ལ་དཔའ་བའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 2175]
དེའི་ཕྱིར་ཞེས་བྱ་བ་ནི་གྲགས་པ་ཐོས་པའི་ཕྱིར་རོ། །

[Block 2176]
སྩོལ་ཞེས་བྱ་བ་ནི་སློང༌[^1363]མོ་པ་ཉིད་དུ་ཁས་ལེན་པའི་ཕྱིར་རོ། །

[Block 2177]
ཅིའི་ཕྱིར་ཁྱོད་ལ་སློང་ཞེས་དེ་ལྟར་རྟོག་པ་ལ་གཡོག་ཏུ་ཞེས་པས་བསྟན་ཏོ། །

[Block 2178]
ཚམ༌[^1364]ཚོམ་མེད་པར་སྦྱིན་ཞེས་བྱ་བ་ནི་དཔྱད་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་སྟེ། དེས་ན་སྨྲས་པ། སྦྱིན་པ་ལ་དགའ་བ་གོམས་པར་བྱས་པའི༌[^1365]རབ་ཏུ་སྡུག་པའི་བུ་བས་ཀྱང་སྦྱིན་པ་ལ་དགའ་བ་སྟེ། ཆེས་གཅེས་པའི་ཕྱིར་ཇི་ལྟར་སྦྱིན་པ་ལ་དགའ་བ་གོམས་པར་བྱས་པ་དེ་ལྟ་བུ་ལ་དགའ་བ་ནི་མ་ཡིན་ཏེ། བུ་ལ་དགའ་བ་ནི་རེས་འགའ་བྱས་པའི་ཕྱིར་དང་། སྦྱིན་པ་ལ་དགའ་བ་ནི་རྒྱུན་དུ་གོམས་པའི་ཕྱིར་རོ། །

[Block 2179]
དེ་ཡང་བུ་ནི་མི་རྟག་པ་ལ་གོམས༌[^1366]པར་སོ་སོར་བརྟགས་པ་དེས་ལྷག་པར་དགའ་བ་མེད་ལ། སྦྱིན་པ་ནི་ཡོན་ཏན་ཐམས་ཅད་དང་ལྡན་པར་སྣང་བས་སོ། །

[Block 2180]
ཡང་ན་ཐམས་ཅད་པས་སྦྱིན་པ་ནི་ཆེ་བ་ཉིད་དོ། །

[Block 2181]
སྦྱིན་པ་ལས༌[^1367]དགའ་བས་བུ་གཉིས་ཀྱང་ཚམ་ཚོམ་མེད་པར་སྦྱིན་པ༌[^1368]ཞེས་བྱ་བ་མ་བྱིན༌[^1369]པའི་དངོས་པོ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2182]
བུ་གཉིས་ཀྱང་ཞེས་བྱ་བའི་སྒྲས་གཅིག་ཏུ་དེ་ལྟར་ཅིའི་ཕྱིར་སྨྲས་ཤེ་ན། སླར་བཟློག་པ༌[^1370]ནི་མ་བསླབས་པས་ཞེས་བྱ་བ་སྨོས་ཏེ། སྦྱིན་པའི་བྱ་བ་མ་ཡིན་པས་ཀྱང་བྱ་བ་མ་ཡིན་པ་མཆོག་ཏུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 2183]
སླར་བཟློག་པ༌[^1371]ཞེས་བྱ་བ་འདིས་ནི་དཀའ་བའི་སྦྱིན་པ་ཉིད་དུ་བསྟན་ཏེ། [^1372]སྦྱིན་པ་ཡོན་ཏན་གཉིས་དང་ལྡན་པའོ། །

[Block 2184]
ད་འདི་ན་མཆིས་ཏེ་ཅི་ཞིག་བགྱི་ཞེས་བྱ་བ་ནི༌[^1373]གལ་ཏེ་བྱིན་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2185]
བྱིན་པའི་གཏམ་ཐོས་ནས་མི་དགའ་བ་སྐྱེས་པའི་མིག་རིག་རིག་པོ་གང་ཡིན་པ་དེ་ནི་སྦྱིན་པའི་གཏམ་ཐོས་ནས་སྐྲག་པའི་མིག་རིག་རིག་པོར་གྱུར་པ་དེའོ། །

[Block 2186]
དེ་གཉིས་ཀྱི༌[^1374]སྙིང་གདུངས་པར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་སྙིང་གདུངས་པར་གྱུར་པའོ། །

[Block 2187]
འདི་ནི་ཞེས་བྱ་བ་དེས་སྨྲས་པ་དེའི་ལན་ནི། ཁྱོད༌[^1375]འདི་གཉིས་ངས་བྱིན་ན་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 2188]
ད་ནི་མཆིས་ཏེ་ཅི་བགྱི་ཞེས་བྱ་བ་འདིའི་ལན་ནི། འདི་གཉིས་མ་ནི་སོང་ཞེས་བྱ་བའོ། །

[Block 2189]
གང་དུ་ཅིའི་ཕྱིར་སོང་ཞེས་བྱ་བ་འབྲི་བའི༌[^1376]ཚིག་གི༌[^1377]སྐབས་རྟོགས་པ༌[^1378]ལ་ནགས་ཚལ་དུ་རྩ་བ་འབྲས་བུ་ཚོལ༌[^1379]དུ་སོང་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 2190]
དེ་ཡང་དེ་རིང་འདིར་འོང་གིས། ། ཞེས་བྱ་བ་འདིས་ནི་རིང་པོ་མི་ཐོགས་པར་འོང་བར་བསྟན་ཏོ། །

[Block 2191]
དེ་འོངས་ནས་ཅི་ཞིག་བྱེད་པ་ཡིན་ཞེས་རྟོགས་པ༌[^1380]ལ་དེ་དང་ཕྲད་ནས་འོ་བྱས་ཞེས་བྱ་བ་སྟེ། འདིས་ནི་མད་དྲི་ལ་ཕན་འདོགས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2192 [VERSE]]
རྒྱན་གྱིས་བརྒྱན་ཅིང་ཕྲེང་བ་ཅན། །
ཞེས་བྱ་བ་ནི་གཞོན་ནུ་གཉིས་སོ། །
འདིར་ནི་ཞག་གཅིག་ངལ་སོ་ལ། །

[Block 2193]
ཞེས་བྱ་བ་འདི་ནི་བྲམ་ཟེ་དེ་ལ་ཕན་འདོགས་པ་བསྟན་ཏེ། ལམ་གྱིས༌[^1381]དུབ་པ་སེལ་བར་སྣང་བའི་ཕྱིར་རོ། །

[Block 2194]
བུད་མེད་རྣམས་ནི་མི་དྲང་བས་ཞེས་བྱ་བ་འདིས་ནི་མ་ནི་བུ་སྦྱིན་པ་དེ་ལ་འགྱོད་པར་འགྱུར་བ་རྗེས་སུ་ཤེས་ཏེ། དེ་བས་ན་ཁྱོད་ཀྱི་སྦྱིན་པ་ལ་གེགས་བྱས་པར་འགྱུར་བས་ཆོས་མ་ཡིན་པ་དང་ལྡན་པར་འགྱུར་བ་ཡིན་པས་ཞག་གཅིག་འདུག་པའི་སྐྱོན་བསྟན་པའོ། །

[Block 2195]
ཁྱོད་ཀྱི་སྦྱིན་པ༌[^1382]ལ་གེགས་བྱེད་ཀྱིས་ཞེས་བྱ་བ་འདིས་ཀྱང་བྱང་ཆུབ་སེམས་དཔའི་སྐྱོན་བསྟན་ཏོ། །

[Block 2196]
བདག་ཉིད་ཀྱིས༌[^1383]ནི་མ་བསྟན་ཀྱང་གྲུབ་པའི་ཕྱིར་ཏེ། སྦྱིན་པ་མ་བྱིན་པའི་ཉེས་དམིགས་བསྟན་པས་གང་རྙེད་པའི་བར་ཆད་ཀྱི་མཚན་ཉིད་དོ། །

[Block 2197]
སྦྱིན་པའི་གེགས་སུ་འགྱུར་དུ་མ་དོགས་ཤིག་ཅེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱི་སྦྱིན་པའི་གེགས༌[^1384]མེད་པའོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ༌[^1385]ངའི་ཆོས་སྤྱོད་པའི་གྲོགས་ཡིན་མོད་ཀྱི་ཞེས་པ༌[^1386]སྨོས་ཏེ། གང་སྔར་བསྟན་པའི་མིང་ནི་གཡོན་ཅན་ཞེས་སུ་བཏགས་ཞེས་བྱ་བ་དེའི་ལན་བཏབ་པ་ཡིན་ནོ། །

[Block 2198]
ད༌[^1387]ནི་ངའི་ཆོས་སྤྱོད་པའི༌[^1388]གྲོགས་ཡིན་མོད་ཅེས་བྱ་བ་ནི་ཇི་ལྟར་ང་སྦྱིན་པ་ལ་དགའ་བ་དེ་ལྟར་དེ་ཡང་དགའ་བ་ཡིན་ཏེ།

[Block 2199 [VERSE]]
ཆོས་སྤྱོད་པའི་གྲོགས་ཡིན་པའི་ཕྱིར་རོ། །
འོན་ཀྱང་འདི་ལ་ཁྱོད་ཅི་དགར་ཟད་མོད། །

[Block 2200]
ཅེས༌[^1389]བྱ་བ་ནི་གལ་ཏེ་ཁྱོད་ཁྱེར་བར༌[^1390]འདོད་ན་དེ་རིང་ཁྱོད་ཁྱེར་ཅིག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2201]
རབ་ཏུ་གཞོན་ཞིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་དོན་གྱི་ཡོན་ཏན་རྣམ་པ་གསུམ་དང་ལྡན་ན་ནི་བྲན་གྱི་ལས་སུ་འོས་པ་ཡིན་ཏེ། ལས་ཅི་འདོད་པ་བསྒྲུབས་པས་བདག་པོ་དགའ་བ་སྐྱེད་པ་དང་། སྡུག་བསྔལ་བཟོད་ཅིང་ལས་བྱེད་པར༌[^1391]ནུས་པ་དང་མཁས་པའོ། །

[Block 2202]
གསུམ་པོ་དེ་དག་ལས་གང་ཞིག་དང་ཡང་མི་ལྡན་པ་མེད་ན་ནི་ཇོ་བོ་ལས་བྱེད༌[^1392]པས་དགའ་བ་བསྐྱེད་པ༌[^1393]ཡིན་ལ།[^1394] ཚིགས་སུ་བཅད་པ་འདིས་ནི་ཡོན་ཏན་དེ་དག་དང་མི་ལྡན་པར་བསྟན་ཏོ། །

[Block 2203]
དེ་ལ་ཉེས་པ་བསྟན་པ་དང་། བཏང་བའི་ཡོན་ཏན་བསྟན་པའི་ཕྱིར་ཤི་བི་པའི་རྒྱལ་པོ་ངའི་ཡབ་ཅེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཉིས་སོ། །

[Block 2204]
འདི་ལྟར་གྱུར་པ་ནི་བྲན་ཉིད་ཀྱི་དངོས་པོར་གྱུར་པའོ། །

[Block 2205]
ངེས་པར༌[^1395]ནི་གདོན་མི་ཟ་བར་རོ།[^1396] །དེའི་ཡུལ་ནི་ཞེས་བྱ་བ་ནི་ཤི་བི་པའི་རྒྱལ་པོའི་ཡུལ་ལོ། །

[Block 2206]
དེ་ལྟར་བྱས་ན་ནོར་ཆེན་དང་། །ཞེས་བྱ་བ་ནི་བུའི་གླུད༌[^1397]ཀྱི་ཕྱིར་ཐོབ་པར་འགྱུར་བའོ། །

[Block 2207]
ཆོས་རྣམས་དང་ཡང་ལྡན་པར་འགྱུར། །ཞེས་བྱ་བ་ནི་ནོར་ཆེན་པོ་དེ་ཉིད་ཀྱིས་ཆོས་བྱེད་ནུས་པའི་ཕྱིར་དང་། བྱིས་པའི་ཉོན་མོངས་པ་མེད་པའི་ཡང་ཕྱིར་རོ། །

[Block 2208]
སྦྲུལ་གདུག་པ་དང་འདྲ་བའི་དྲུང་དུ་ཞེས་བྱ་བ་ནི་སྦྲུལ་གདུག་པ་ལྟ་བུར་བསྙེན་པར་དཀའ་བས་སོ། །

[Block 2209]
མི་དགའ་བ་ཉིད་ཀྱི་སྐྱེས་པ་ཡིན་པས་མི་དགའ་བའི་སྐྱེས་སོ། །

[Block 2210]
དེ་ལྟ་བུའི་མཚན་ཉིད་དང་ལྡན་པའི་རྒྱལ་པོའི་དྲུང་དུ་འགྲོ་བའི་ཉེས་དམིགས་བསྟན་པའི་ཕྱིར་རྒྱལ་པོས་བདག་ལ་འདི་གཉིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །
--- END BLOCKS ---
