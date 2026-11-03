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
[Block 2066]
བཅོམ་ལྡན་འདས་ཅི་ལགས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སེམས་དང་པོ་བསྐྱེད་པས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱའམ། འོན་ཏེ་སེམས་སླད་མ་བསྐྱེད་པས་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་ཞེས་བྱ་བ་ནི་ཟབ་མོའི་གནས་ཀྱི་སྐབས༌[^1386]ཞུས་པ་སྟེ། དགེ་བའི་རྩ་བ་བསྩགས་པས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་ན། དེ་ལ་ཇི་ལྟར་དགེ་བའི་རྩ་བ་བསྩགས་པར་འགྱུར། །ཅི་འདི་ལ་བྱང་ཆུབ་སེམས་དཔའ་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱི་སྔོན་རོལ་དུ་གང་ཐོག་མར་སེམས་བསྐྱེད་པ་དེའི་མཐས༌[^1387]མངོན་པར་རྫོགས་པར་འཚང་རྒྱའམ་འོན་ཏེ་གཉིས་པས་སམ། འོན་ཏེ་གསུམ་པས་སམ། འོན་ཏེ་ཅི་གང་བྱང་ཆུབ་ཀྱི་སྙིང་པོར་བཞུགས་པ༌[^1388]ན། ཐམས་ཅད་ཀྱི་ཐ་མར་སེམས་བསྐྱེད་པ་དེའི་མཐུས་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ། དེ་ལ་སེམས་གཅིག་གིས་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་མི་འགྱུར་ཏེ། དེ་ལ་དེ་ལྟ་བུའི་མཐུ་མེད་པ་དང་། བསོད་ནམས་ཀྱི་ཚོགས་ལྷག་མ་རྣམས་དོན་མེད་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2067]
ཐམས་ཅད་ཀྱིས་ཀྱང་མ་ཡིན་ཏེ། དེ་དག་སྐད་ཅིག་རེ་རེ་ལ་འཇིགས་པའི་ངང་ཅན་ཡིན་པས་བསྩགས༌[^1389]སུ་མི་རུང་བའི་ཕྱིར་རོ་ཞེས་བསྟན་པ་སྟེ། དེ་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་མར་མེའི་དཔེ་བསྟན་པ། གང་གི་ཚེ་མར་མེའི་སྙིང་པོ་ཚིག་པ་ནི༌[^1390]སྐད་ཅིག་རེ་རེ་ལ་འཇིགས་པའི༌[^1391]ངང་ཅན་ཡིན་ཡང་། མར་མེའི་སྐད་ཅིག་ཐམས་ཅད་ཀྱི་སྟོབས་ཀྱིས་ཚིག་པར་གྱུར་ཅེས་བྱའོ། །

[Block 2068]
དེ་བཞིན་དུ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་ཡང་སེམས་ཐམས་ཅད་ཀྱི་མཐུས་འགྱུར་བར་བསྟན་པ་སྟེ། སྐད་ཅིག་པ་ཡིན་དུ་ཟིན་ཀྱང་། འདུ་བྱེད་ཀྱི་བག་ཆགས་བསྩགས་པའི་ཚུལ་གྱིས་འགྱུར་རོ༌[^1392]ཞེས་དགོངས་པའོ། །

[Block 2069]
དཀར་པོ་རྣམ་པར་མཐོང་བའི་ས་ནི་ལྷག་མཐོང་གི་ཚེའོ། །

[Block 2070]
རིགས་ཀྱི་ས་ནི་འཇིག་རྟེན་པའི་ཆོས་ཀྱི་མཆོག་གོ། །

[Block 2071]
བརྒྱད་པའི་ས་ནི་རྒྱུན་དུ་ཞུགས་པའི་ལམ་མོ། །

[Block 2072]
དེ་ཉིད་ཀྱི་འབྲས་བུ་ནི་མཐོང་བའི་སའོ། །

[Block 2073]
བསྲབ་པའི༌[^1393]ས་ནི་ལན་ཅིག་ཕྱིར་འོང་བའི་ས་སྟེ། དེས་འདོད་པ་ལ་འདོད་ཆགས་དང་། གནོད་སེམས་བསྲབས་པའི་ཕྱིར་རོ། །

[Block 2074]
འདོད་ཆགས་དང་བྲལ་བའི་ས་ནི་ཕྱིར་མི་འོང་བའི་ས་སྟེ། འདོད་ཆགས་དང་གནོད་སེམས་གཉིས་སྤངས་པའི་ཕྱིར་རོ། །

[Block 2075]
བྱས་པ་རྟོགས་པའི་ས་ནི་དགྲ་བཅོམ་པ་ཉིད་དེ། བྱ་བ་བྱས་པའི་ཕྱིར་རོ། །

[Block 2076]
རང་སངས་རྒྱས་ཀྱི་ས་ནི་རང་བྱང་ཆུབ་ཉིད་དོ། །

[Block 2077]
བྱང་ཆུབ་སེམས་དཔའི་ས་ནི་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་དོ། །

[Block 2078]
སངས་རྒྱས་ཀྱི་ས་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་དོ།[^1394] །

[Block 2079 [HEADING]]
##### སེམས་འགགས་པ་སྐྱེ་བར་མི་འགྱུར་བའི་ཟབ་མོའི་གནས། ^1-2-7-5-0

[Block 2080]
གཞན་ཡང་སེམས་གང་འགགས་པ༌[^1395]དེའི་ཕྱིར་སྐྱེ་བར་འགྱུར་རམ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^1396]ཟབ་མོའི་གནས་སྐབས་སྟོན་ཏོ། །

[Block 2081]
གང་འགགས་པ༌[^1397]ནི་སྐྱེ་བར་མི་འགྱུར་རོ། །

[Block 2082]
གང་སྐྱེས་པ༌[^1398]ནི་འགག་པའི་ཆོས་ཅན་ཡིན་ནོ། །

[Block 2083]
གང་འགག་པའི་ཆོས་ཅན༌[^1399]དེ་ནི་འགག་པར་མི་འགྱུར་ཏེ། དེ་བཞིན་ཉིད་ཇི་ལྟ་བ་དེ་བཞིན་ཉིད་དུ༌[^1400]དེ་གནས་པར་ཡང་འགྱུར་ལ། དེ་ཐེར་ཟུག་ཏུ་གནས་པར་ཡང་མི་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ནི༌[^1401]ཟབ་མོའི་གནས་སོ། །

[Block 2084]
གང་འགགས་པ་དེ་ནི་སྐྱེ་བར་མི་འགྱུར་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་ཀྱིས་འགག་པ༌[^1402]སྟེ་འདུས་མ་བྱས་པ་ལ་བྱའོ། །

[Block 2085]
གང་སྐྱེས་པ་དེ་ནི་འགག་པའི་ཆོས་ཅན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདུས་བྱས་ལ་བྱའོ། །

[Block 2086]
གང་འགག་པའི་ཆོས་ཅན་དེ་ནི་འགག་པར་མི་འགྱུར་ཞེས་བྱ་བ་ནི་འགག་པ་གཉིས་པ་མེད་པའི་ཕྱིར་དེ་སྐད་ཅེས་གསུངས་སོ། །

[Block 2087]
དེ་བཞིན་དུ་དེ་གནས་པར་ཡང་འགྱུར་ཞེས་བྱ་བ༌[^1403]ནི་དེ་བཞིན་ཉིད་ལ་བྱའོ། །

[Block 2088]
དེ་ཐེར་ཟུག་ཏུ་གནས་པར་མི་འགྱུར་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་དེ་སྐད་བཤད་དོ། །

[Block 2089]
རབ་འབྱོར་དེ་ཇི་སྙམ་དུ་སེམས། སེམས་དེ་ཡང་དེ་བཞིན་ཉིད་དམ་ཞེས་བྱ་བ་ནི། ཅི་འདུས་བྱས་ཀྱི་སེམས་གང་ཡིན་པ་དེ། དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཡིན་ནམ་ཞེས་དྲིས་པའོ། །

[Block 2090]
བཅོམ་ལྡན་འདས་དེ་ནི་མ་ལགས་སོ་ཞེས་བྱ་བ་ནི། དྲི་མ་དང་བཅས་པའི་ཕྱིར་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་མ་ལགས་སོ་ཞེས་སླར་གསོལ་པའོ། །

[Block 2091]
དེ་བཞིན་ཉིད་ལས་སེམས་དེ་གུད་ན་ཡོད་དམ་ཞེས་བྱ་བ་ནི་འདུས་བྱས་ཀྱི་སེམས་དེ་དེ་བཞིན་ཉིད་ལས་གཞན་ནམ༌[^1404]ཞེས་དྲིས་པའོ། །

[Block 2092]
བཅོམ་ལྡན་འདས་དེ་ནི་མ་ལགས་སོ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པ་ནི་ཡོངས་སུ་གྲུབ་པ་ལས་དེ་ཁོ་ན་ཉིད་དམ་གཞན་དུ་བསྙད་དུ་མི་རུང་བའི་ཕྱིར་སླར་གསོལ་པའོ། །

[Block 2093]
དེ་བཞིན་ཉིད་ལ་སེམས་ཡོད་དམ་ཞེས་བྱ་བ་དང་། སེམས་ལ་དེ་བཞིན་ཉིད་ཡོད་དམ་ཞེས༌[^1405]བྱ་བ་ནི། ཅི་ཕན་ཚུན་གནས་དང་བརྟེན་པའི་དངོས་པོར༌[^1406]ཡོད་དམ་ཞེས་དྲིས་པའོ། །

[Block 2094]
བཅོམ་ལྡན་འདས་དེ་ནི་མ་ལགས་སོ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པ་དང་། ཡོངས་སུ་གྲུབ་པ་གཉིས་གནས་དང་བརྟེན་པའི་དངོས་པོར་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་སླར་གསོལ་པའོ། །

[Block 2095]
དེ་བཞིན་ཉིད་ཀྱིས༌[^1407]དེ་བཞིན་ཉིད་ཡང་དག་པར་རྗེས་སུ་མཐོང་ངམ་ཞེས་བྱ་བ་ནི། སེམས་དེས་ཆོས་ཐམས་ཅད་ཡང་དག་པར་རྗེས་སུ་མཐོང་ངོ་སྙམ་དུ་སེམས་པ་ལ་དྲིས་པའོ། །

[Block 2096]
བཅོམ་ལྡན་འདས་དེ་ནི་མ་ལགས་སོ་ཞེས་བྱ་བ་ནི། དེ་བཞིན་ཉིད་ཀྱི་གནས་སྐབས་དེ་ནི།[^1408] དམིགས་པར་བྱ་བ་དང་། དམིགས་པར་བྱེད་པ་མེད་པའི་ཕྱིར་སླར་གསོལ་པའོ། །

[Block 2097]
བཅོམ་ལྡན་འདས་གང་དེ་ལྟར་སྤྱོད༌[^1409]དོ་ཞེས་བྱ་བ་དེ༌[^1410]ནི། ཅི་ལ་ཡང་སྤྱོད༌[^1411]པ་མེད་དོ་ཞེས་བསྟན་པའོ། །

[Block 2098]
བཅོམ་ལྡན་འདས་དེ་ནི་གང་ལ༌[^1412]གཉིས་ཀུན༌[^1413]འབྱུང་བ་མ་མཆིས་པའི་དོན་དམ་པ་ལ་སྤྱོད་དོ་ཞེས་བྱ་བ་ནི། སྤྱོད༌[^1414]དོ་ཞེ་འམ་མེད་དོ་ཞེས་བྱ་བས༌[^1415]དེ་ནི་གཉིས་པའོ།[^1416] །དེས་མཚན་མར་འདུ་ཤེས་པ་རྣམ་པར་བཤིག་པ་ཡིན་ནམ་ཞེས་བྱ་བ་ནི། མཚན་མའི་འདུ་ཤེས་མེད་པར་བྱས་པ་ཡིན་ནམ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2099]
བཅོམ་ལྡན་འདས་དེ་ནི་མ་ལགས་སོ་ཞེས་བྱ་བ་ནི། མཚན་མའི་འདུ་ཤེས་རྣམ་པར་གཞིག་པར་བྱའོ་སྙམ་པ་དེ་ལྟ་བུའི་རྣམ་པར་རྟོག་པ། ཀུན་ཏུ་འབྱུང་བ་མེད་པའི་ཕྱིར་སླར་གསོལ་པ་སྟེ། དེ་ལྟ་བུའི་རྣམ་པར་རྟོག་པ་ཀུན་ཏུ་སྤྱོད་པ་མེད་པར་ཡང་སྟོང་པ་ཉིད་དང་། མཚན་མ་མེད་པ་དང་། སྨོན་པ་མེད་པའི་ཏིང་ངེ་འཛིན་བསྒོམ་པའི༌[^1417]མཐུས་བདག་ཉིད་མཚན་མའི་འདུ་ཤེས་ཀུན་ཏུ་མི་སྤྱོད་པར་འགྱུར་རོ་ཞེས་བསྟན་པའོ། །

[Block 2100]
ཏིང་ངེ་འཛིན་དེ་དག་གིས་སེམས་ཅན་རྣམས་ཡོངས་སུ་སྨིན་པར་བྱེད་དོ་ཞེས་བྱ་བ་ནི་ཐབས་མཁས་པའི་མཐུས། གང་བདག་ཀྱང་སྟོང་པ་ཉིད་ལ་སོགས་པར༌[^1418]མཐོང་བར་འགྱུར་ལ། སེམས་ཅན་རྣམས་ཀྱང་ཡོངས་སུ་སྨིན་པར་བྱེད་པ་སྟེ། དེ་ནི་ཐབས་ལ་མཁས་པའི་མཐུ་ཡིན་ནོ། །

[Block 2101 [HEADING]]
##### རྨི་ལམ་དུ་ཏིང་ངེ་འཛིན་གསུམ་ལ་སྙོམས་པར་ཞུགས་པ། ^1-2-7-6-0

[Block 2102]
[^1419]གང་ལ་ལ་རྨི་ལམ་དུ་སྟོང་པ་ཉིད་དང་། མཚན་མ་མེད་པ་དང་། སྨོན་པ་མེད་པའི་ཏིང་ངེ་འཛིན་གསུམ་ལ་སྙོམས་པར་ཞུགས་ན། དེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་རྣམ་པར་འཕེལ་ལམ་ཞེས་བྱ་བ་ནི། ཟབ་མོའི་གནས་ཀྱི་སྐབས་ཕྱེ་ནས། གནས་བརྟན་གཉིས་ཀྱིས་སྔར་འདས་པའི་ཏིང་ངེ་འཛིན་ཉིད་བསྟན་ཏེ། གལ་ཏེ་ཆོས་ཐམས་ཅད་དམིགས་སུ་མེད་ན། བྱང་ཆུབ་སེམས་དཔའ་གང་རྨི་ལམ་ན་ཏིང་ངེ་འཛིན་གསུམ་ལ་སྙོམས་པར་ཞུགས་པ་དེའི་ཚེ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་རྣམ་པར་འཕེལ་བར་འགྱུར་བའི་རིགས་སོ། །

[Block 2103]
གལ་ཏེ་རྨི་ལམ་ན་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་འཕེལ་བར་མི་འགྱུར་ལ། གཉིད་ཀྱིས་མ་ལོག་པའི་ཚེ་ནི་འགྱུར་ན། དེ་ལྟ་ན་ནི་རྨི་ལམ་དང་། གཉིད་ཀྱིས་མ་ལོག་པ་གཉིས་ལ་ཆོས་རྣམས་ལ༌[^1420]ཡོད་པ་དང་མེད་པའི་བྱེ་བྲག་འབའ་ཞིག་ཡོད་དོ་སྙམ་དུ་དགོངས་ནས་དྲིས་པའོ། །

[Block 2104]
[^1421]ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་གལ་ཏེ་ཉིན་པར་བསྒོམས་པས༌[^1422]རྣམ་པར་འཕེལ་ན། རྨི་ལམ་ན་ཡང་རྣམ་པར་འཕེལ་ལོ་ཞེས་དྲིས་པའོ།[^1423] །དེ་ནས་གནས་བརྟན་རབ་འབྱོར་གྱིས། འདི་ལ་བྱང་ཆུབ་སེམས་དཔའ་ལ་ནི༌[^1424]རྨི་ལམ་དང་། གཉིད་ཀྱིས་མ་ལོག་པའི་ཚེ་ཡང་། ཆོས་རྣམས་དམིགས་སུ་མེད་པར་མཚུངས་ཏེ། དེ་བས་ན་རྨི་ལམ་ཞེས་བྱ་བ་དང་། ཉིན་པར་ཞེས་བྱ་བ་ནི༌[^1425]ཡང་རྣམ་པར་རྟོག་པ་ཙམ་དུ་ཟད་དོ་ཞེས་རྨི་ལམ་དང་གཉིད་ཀྱིས་མ་ལོག་པ་གཉིས་མཚུངས་པར་སྟོན་ཏོ། །

[Block 2105]
དེ་ལྟར་ན་ཉིན་པར་དང་རྨི་ལམ་གཉིས་མཚུངས་ན། གལ་ཏེ་གཉིད་ཀྱིས་མ་ལོག་པའི་ཏིང་ངེ་འཛིན་གྱིས་ཤེས་རབ་རྣམ་པར་འཕེལ་བར་འགྱུར་ན། རྨི་ལམ་གྱི་ཏིང་ངེ་འཛིན་གྱིས་ཀྱང་ཤེས་རབ་རྣམ་པར་འཕེལ་བར་འགྱུར་རོ་ཞེས་བསྟན་པའོ། །
--- END BLOCKS ---
