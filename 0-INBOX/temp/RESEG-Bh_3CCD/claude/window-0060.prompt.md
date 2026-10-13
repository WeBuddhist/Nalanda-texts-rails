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
[Block 2101]
སྔར་བཤད་པའི་ཀུན་རྫོབ་དང་དོན་དམ་པ་ལ་སོགས་པ་གཉིས་སུ་འཛིན་པའི་རྣམ་པར་རྟོག་པ་གསལ་བའི༌[^1413]མཚན་ཉིད་ཀྱི་རིམ་པ་སོ་སོར་བསྟན་པ་ནི་ཟུང་དུ༌[^1414]འཇུག་གོ། །

[Block 2102]
དེ་དག་ལ་བརྟེན༌[^1415]ཏེ་རྐྱེན་དང་ལྡན་པའི་སྒྲ་ཕྱེ་བས༌[^1416]ལས་ཀྱི་དོན་དུ་འམ་རྒྱུ༌[^1417]

[Block 2103]
ལྔ་པ་ལ༌[^1418]བྱའོ། །

[Block 2104]
རིམ་པ་ལྔའི་བསྡུས་པའི་དོན་ནི་དེ་དག་སྐབས༌[^1419]ཀྱི་རིམ་པའི་རིགས་པས་བསྡུས་པའི་དོན་རྣམས་ཤེས་ནས་ནི་རྟོགས་ནས་སོ། །ཅི་བྱ་ཞེ་ན། མཐའ་དྲུག་ལ་འཇུག་གོ་ཞེས་སྨོས་ཏེ་དོན་དྲུག་སོ་སོར་བསྟན་པའི་འགྲེལ་པ་འདི་ལ་འཇུག་པར་བྱ་སྟེ། དེ་མཉན་པའམ་བཤད་པ་ལ་སྣོད་དུ་རུང་བར་འགྱུར་ཞེས་པའི་དོན་ཏོ། །

[Block 2105]
ཇི་ལྟར་མཐའ་དྲུག་གི་འགྲེལ་པའི་རིམ་པ་ལྔ་བརྗོད་པར་བྱ་བ༌[^1420]དེ་བཞིན་དུ་སྔོན་དུ་བཤད་ཟིན་པ་དང་འཆད་པར་ཡང་འགྱུར་རོ། །

[Block 2106]
ད་ནི་གང་ལ་བརྟེན་ཏེ་འགྲེལ་པ༌[^1421]བྱས་པ་དེ་ཉིད་ཡི་གེ་གསུམ་པོ་སྟོན་པར༌[^1422]བྱེད་པ་དཔལ་གསང་བ་འདུས་པ་ཉིད་བསྔགས་པར་བྱ་བའི་ཕྱིར། ཇི་སྲིད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ་ཡང་། ར་ལ་ཝ་ལ་སོགས་པ་གསལ་བར་བྱ་བ་རྣམས་དང་། གང་མེད་པར་མི་འབྱུང་བ་དབྱངས་ཀྱི་སྡེ་ཇི་སྲིད་ཡོད་པ་དེ་རྣམས། དེ་དེའི་རྩ་བ་ཡི་གེ་གསུམ་ལས་དེ་རྣམས་འབྱུང༌[^1423]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2107]
དགོངས་པ་ནི་འདི་ཡིན་ཏེ་ལྟེ་བའི་ཕྱོགས་ནས་ལངས་པའི་སྲོག་གི་རླུང་གིས་གནས་བརྒྱད་དང་ཕྲད་པ་ལས་དབྱངས་དང་གསལ་བའི་བྱེ་བྲག་གིས་སྡེ་ཚན༌[^1424]བརྒྱད་སྐྱེ་བར་འགྱུར་ཏེ། དེ་དག་ཀྱང་སྡེ་ཚན་གྱི་ཡི་གེ་དང་པོ་རྣམས་ལ་ཐིམ་པར་གྱུར་ནས་སླར་ཡང་བཞི་རུ་གྱུར་ནས་དེ་ཉིད་སྐྱེས་པ་དང་བུད་མེད་དང་མ་ནིང་གི་དབྱེ་བས་ཡི་གེ་གསུམ་དུ་འགྱུར་རོ། །

[Block 2108]
དེའི་ཕྱིར་འདི་ལ་གྲུབ་པའི་མཐའ་འདི་ཡིན་ཏེ། ཡི་གེ་ཧཱུཾ་ལས་ཀ་ལ་སོགས་པ་ནས་མའི་བར་དུ་སྐྱེས་པ་དང་། ཡི་གེ་ཨོཾ་ལས་བར་ན་གནས་པ་ཡ་ལ་སོགས་པ་དང་། ཡི་གེ་ཨ་ལ་སོགས་པ་དབྱངས་ཡི་གེ་བཅུ་དྲུག་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2109]
དབྱངས་ཡིག་མེད་པས་གསལ་བྱ་རྣམས་བརྗོད་པར་མི་ནུས་ཏེ། ཀེ་ཁེ་གྷེ་དེ་ཞེས་བྱ་བ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 2110]
དེའི་ཕྱིར་ཡ་ལ་སོགས་པ་གཟུང་བས༌[^1425]དབྱངས་ཡིག་རྣམས་ཀྱང་འདུས་སོ། །

[Block 2111]
དེ་ལྟར༌[^1426]ན་ཀ་ལ་སོགས་པ་དང་པོ་བརྗོད་པར་རིགས་པ་ཡིན་ན་ཇི་ལྟར་ཡ་ལ་སོགས་པ་བརྗོད་དེ། གོ་རིམས༌[^1427]འདོར་བའི་རྒྱུ་མེད་པའི་ཕྱིར་རོ། །

[Block 2112]
སྨྲས་པ་ཡ་ལ་སོགས་པའི་རྒྱུད་ཡོད་དེ་ལས་ཀྱི་རབ་འབྱམས་གཙོ་བོ་ཡིན་པས་ན་གོང་དུ་གསུངས་སོ། །

[Block 2113]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་།

[Block 2114 [VERSE]]
ཡ་ཡི༌[^1428]དོན་གྱིས༌[^1429]ཅི་ཡང་རུང་། །
དངོས་གྲུབ་འདོད་པས་བྱ་བ་ནི། །
ར་ལ་སོགས་པ་གསུམ་གྱིས་ནི། །
འགྲོ་བའི་བྱ་བ་རབ་ཏུ་འཇུག །

[Block 2115]
ཞེའོ། །

[Block 2116]
གཞན་དག་ན་རེ་དཔལ་གསང་བ་འདུས་པ་རྣལ་འབྱོར་གྱི་རྒྱུད་ཆེན་པོའི་ཡན་ལག་གི་ཡི་གེ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་གྲངས་ཀྱིས་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་སུམ་ཅུ་རྩ་གཉིས་ཡོད་དེ། དེ་རྣམས་ཀྱང་ཀ་ལ་སོགས་པའི་གསལ་བྱའི༌[^1430]མཐའ་ཅན་ནོ། །

[Block 2117]
འདི་ལྟ་སྟེ། ཛྙཱ་ན་བཛྲ་ས་མུཉྫ་ཡ་ནི་ཡའི་མཐའ་ཅན་ནོ། །

[Block 2118]
བཛྲ་དྷ་ར་རྒྱུད་ནི་རའི་མཐའ་ཅན་ནོ། །

[Block 2119]
བཛྲ་མ་ལ་རྒྱུད་ནི་ལའི་མཐའ་ཅན་ནོ། །

[Block 2120]
བཛྲ༌[^1431]གྲ་ཧ་རྒྱུད་ནི་ཧའི་མཐའ་ཅན་ནོ། །

[Block 2121]
དེ་ལྟར་གསལ་བྱའི་མཐའ་ཅན་རྒྱུད་གཞན་རྣམས་ཀྱང་ཤེས་པར་བྱའོ། །

[Block 2122]
དེ་རྣམས་ཀྱི་ཡི་གེ་གསུམ་པོ་རྗོད༌[^1432]པར་བྱེད་པ་དཔལ་གསང་བ་འདུས་པ་ཁོ་ན་རྩ་བའོ། །

[Block 2123]
དེ་ཡང་རྣལ་འབྱོར་གྱི་རྒྱུད་རྣམས་ཀྱི༌[^1433]རྩ་བ་གཅིག་པུར་མ་ཟད་ཀྱི་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་ཀྱི་ཡང་རྩ་བར་འགྱུར་ཞེས་བསྟན་པར་བྱ་བའི་ཕྱིར། ཐུབ་པ་ཆེན་པོའི་ཆོས་ཀྱི་ཕུང་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ། ཐུབ་པ་ཆེན་པོ་ནི་ཤཱཀྱ་སེང་གེའི་འོ། །

[Block 2124]
ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ཡོད་དེ་དེ་དག་ཐམས་ཅད་ཀྱི་དཔལ་གསང་བ་འདུས་པ་སྣོད་ཡིན་ཏེ། དེ་ཁོ་ན་ཉིད་ཀྱི་རིན་པོ་ཆེའི་ཟ་མ་ཏོག་གོ། །

[Block 2125]
དེ་ལ་གནས་པའམ་དེ་ཉིད་ལས་འབྱུང་ངོ་ཞེས་ཚིག་གི་ལྷག་མའོ། །

[Block 2126]
དེ་བས་འདི་ནི་རྒྱུད་ཀྱི་རྩེ། །ཞེས་བྱ་བ་ནི་དེ་ཉིད་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་རྣམས་ཀྱི་གཙུག་ཕུད་ཡིན་ནོ། །

[Block 2127]
དགོངས་པ་འདི་ཡིན་ཏེ་ལུས་དང་ངག་དང་ཡིད་དག་པར་བྱ་བའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱི༌[^1434]གསུང་རབ་གསུངས་པ་དེ་ཉིད་རྒྱུད་འདི་རུ་མདོར་བསྡུས་ཤིང་ཐབས་བདེ་བས་བསྟན་ཏོ། །

[Block 2128]
ཡང་ན་ཡི་གེ་གསུམ་པོ་ཁོ་ན་ལས་སྔགས་ཀྱི་སྡེ་ཐམས་ཅད་དང་ལུས་ལ་སོགས་པའི་བྱ་བ་ཡང་འབྱུང་ངོ་ཞེས་དེ་ལ་ལྟོས་པས་དཔལ་གསང་བ་འདུས་པ་ཁོ་ན་རྒྱུད་ཀྱི་རྩེ་མོ་ཡིན་ཏེ། [^1435]ཆོས་ཀྱི་ཕུང་པོའི་ཚད་ནི་གྲོ་ག་རིམ་པ་གཅིག་པ་དང་ཤིང་ཏ་ལའི་འདབ་མ་རྣམས་སུ་ཕག་ཟེའི་རྩེ་མོས་བྲིས་པའི་ཚོད་ཀྱི་ཡི་གེ་རྣམས་ཀྱིས་གང་བར་བྱས་ཏེ་གང་བར་བྱས་པའི་གྲོ་གའི་ཁུར་ཇི་སྲིད་གླང་རྒོད་ཀྱིས་ཐེག་པ་དེ་ནི་ཆོས་ཀྱི་ཕུང་པོ་གཅིག་གོ། །

[Block 2129]
དེའི་གྲངས་ཀྱིས༌[^1436]བརྒྱད་ཁྲི་བཞི་སྟོང་ངོ་། །དེ་ནི་ཉེ་བར་མཚོན་པ༌[^1437]ཡིན་ཏེ། ཉན་ཐོས་ཀྱི་སྡེ་སྣོད་ནི་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ཡིན་ནོ། །

[Block 2130]
ཐེག་པ་ཆེན་པོ་ལ་དགུ་ཁྲིའོ། །

[Block 2131]
སྔགས་ཀྱི་ཐེག་པ་ལ་སྟོང་ཕྲག་བརྒྱ་ཡིན་ནོ། །

[Block 2132]
ད་ནི་དོན་ཟབ་པ་ཡིན་པའི་ཕྱིར་ཉན་པ་པོས་རྒྱུད་འདི་རྟོགས་པར་དཀའ་བ་ཉིད་དུ་བསྟན་པར་བྱ་བའི་ཕྱིར། གཞུང་ཉུང་བ་ལ་དོན་མང་བ་ཞེས་བྱ་བ་སྨོས་ཏེ། རིམ་པ་གཉིས་ཡོངས་སུ་རྫོགས་པར་སྟོན་པར་བྱེད་པའོ། །

[Block 2133]
རྒྱུད༌[^1438]འདི་གཞུང་ཉུང་བ་ཡིན་པས་མདོར་བསྡུས་པའི་བློ་ཅན་གྱི་ཉན་པ་པོ་ལ་ཕན་པའོ། །

[Block 2134]
དེ་ལྟ་ཡིན་ན་རྗོད་པར་བྱེད་པའི༌[^1439]ཉུང་བས་བརྗོད་པར་བྱ་བ་ཡང་ཉུང་བས་བླང་བར་བྱ་བར་མི་འགྱུར་ཞེ་ན། དོན་མང་བ་ཞེས་བྱ་བ་སྨོས་ཏེ། རིམ་པ་གཉིས་ཡོངས་སུ་རྫོགས་པར་སྟོན་པར་བྱེད་པའོ། །

[Block 2135]
དགོངས་པ་འདི་ཡིན་ཏེ་བྱ་བའི་རྒྱུད་ལ་སོགས་པ་མ་ལུས་པ་དང་། ཆོས་ཀྱི་ཕུང་པོ་མ་ལུས་པའི་དོན་གང་ཡིན་པ་དེ་དག་ཐམས་ཅད་འདིར་མེ་ལོང་ལ་ཞུགས་པའི་གཟུགས༌[^1440]བརྙན་གྱི་རིགས་པས་ནང་དུ་འདུས་པ་ཞེས་དགོངས་པའོ། །

[Block 2136]
འདུས་པའི་རྒྱུད་ནི་རྙེད་དཀའ་ཞིང་། །ཞེས་བྱ་བ་ལས།

[Block 2137]
སྔོན་དུ་བཤད་པའི་རྒྱུད་རྣམས་ཀྱི་ནང་ནས་རྙེད་པར་དཀའ་བ་སྟེ། རྟོགས་པར༌[^1441]དཀའ་བའོ། །

[Block 2138]
ཐམས་ཅད་དུ་ནི་དུས་ཐམས་ཅད་དུའོ། །

[Block 2139]
རྣམ་པར༌[^1442]འཁོར་བ་ནི་ཉན་པ་པོ་རྨོངས་ཤིང་གོ་བར་མི་འགྱུར་རོ་ཞེས་པའི༌[^1443]ཐ་ཚིག་གོ། །ཅིའི་ཕྱིར་ཞེ་ན། རྒྱན་བདུན་རྟོགས་པར་དཀའ་བས་ན། །ཞེས་སྨོས་ཏེ། རྒྱན་རྣམས་དཀའ་བས་ཡོངས་སུ་མི་ཤེས་པའི་ཕྱིར་རོ། །

[Block 2140]
སྦྱོར་བ་ནི་འདུས་པ་ཞེས་ཆོས་ཅན་ནོ། །
--- END BLOCKS ---
