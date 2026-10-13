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
[Block 1576]
བུམ་པ་ལ་སོགས་པའི་དེ་དང་ལྡན་པའི་དོན་ནི་གདོན་མི་ཟ་བར་ཅུང་ཞིག་ཀྱང་འབྲེལ་པ་མ་ཡིན་ནོ། །

[Block 1577]
དོན་གྱིས་འཕངས་པའང༌[^1203]མ་ངེས་པའོ། །

[Block 1578]
དོན་གྱིས་འཕངས་པ་ཞེས་བྱ་བ་ནི། གང་ལ་དོན་གྱི་ཤུགས་ཀྱིས་ངེས་པར་སྐྱེད་པ༌[^1204]སྟེ། དཔེར་ན་ཉིན་པར་མི་ཟའོ་ཞེས་པ་ལས་ནུབ་མོ་ཟ་བར་ངེས་པ་ལྟ་བུའོ། །

[Block 1579]
འདིར་ནི་ཡོད་ཅེས་བརྗོད་པས་བུམ་པ་ལ་སོགས་པ་ལ་མ་ངེས་པའི་ཕྱིར་ཐེ་ཚོམ་ཟ་བ་ཡིན་པས་དོན་གྱིས་འཕངས་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1580]
དེའི་ཕྱིར་རིགས་ཀྱི་སྒྲ་ཐ་དད་འབྲེལ་པའི་སྤྱི་རིགས་དང་ལྡན་པའི་རྗོད་པར་བྱེད་པ༌[^1205]ལན་འགའ་ཡང་སྦྱར་བར་མི་བྱའོ། །

[Block 1581 [HEADING]]
### སྒྲ་ལའང་གཞན་སེལ། ^5-6-0

[Block 1582]
དེས་ན་སྒྲ་ལའང་གཞན་སེལ་བྱས། །དེའི་ཕྱིར་སྔར་བརྗོད་པ་ལྟར་བྱས་པ་ལ་སོགས་པ་བཞིན་དུ་སྒྲ་ཡང་གཞན་སེལ་བའི་སྒོ་ནས་རང་གི་དོན་སྟོན་པར་བྱེད་དོ་ཞེས་གནས་སོ། །

[Block 1583]
ཡང་བརྗོད་པ།

[Block 1584 [VERSE]]
བརྗོད་པར་བྱ་བ་མང་མོད་ཀྱང་། །
སྒྲ་ཡིས་རྣམ་ཀུན་རྟོག༌[^1206]མ་ཡིན། །
རང་དང་རྗེས་སུ་འབྲེལ་པའི༌[^1207]དོན། །
རྣམ་གཅོད་ངག་གི་འབྲས་བུ་ཡིན། །

[Block 1585 [VERSE]]
སྒྲས་ཀྱང་ཆོས་གང་དུ་མ་ཡི། །
དོན་ལ་འཇུག་པ་མ་ཡིན་གྱི། །
སྦྱར་བྱ་དེ་ཉིད་ལ་དེ་སྒྲའི། །
ཡོན་ཏན་ཉིད་སོགས་ཀྱིས་མ་ཡིན། །

[Block 1586]
ཞེས་བྱ་བ་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 1587 [HEADING]]
### གཞི་མཐུན་པ་དང་ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར་དུ་བྱ་བ། ^5-7-0

[Block 1588 [HEADING]]
#### གཞན་སེལ་བའི་སྒྲའི་དོན་ལ་གཞི་མཐུན་པ། ^5-7-1-0

[Block 1589]
གལ་ཏེ་གཞན་སེལ་བ་ཙམ་སྒྲའི་དོན་ཡིན་ན་ཇི་ལྟར་ཨུཏྤལ་སྔོན་པོ་ལ་སོགས་པའི་སྒྲ་ལ་གཞི་མཐུན་པ་དང་། ཁྱད་པར་དུ་བྱེད་པ་དང་། ཁྱད་པར་དུ་བྱ་བའི་དངོས་པོར༌[^1208]ཇི་ལྟར་ན་འགྱུར། ཇི་ལྟར་མི་འགྱུར། ཇི་ལྟར༌[^1209]སྤྱི་ཐ་དད་པ་ནི་ཁྱད་པར་གྱི་སྒྲ་རྣམས་ཀྱི་གཞན་སེལ་བ་ཡིན་པས་ནའོ་ཞེ་ན། [^1210]ཉེས་པ་དེ་དག་ནི་ཡོད་པ་མ་ཡིན་ཏེ།

[Block 1590 [VERSE]]
སེལ་བ་ཐ་དད་དོན་ཕྱེའི་ཕྱིར། །
རང་དོན་ཐ་དད་རྟོགས་ལ་རྨོངས། །
གཅིག་ལ་ཐ་དད་འབྲས་མེད་ཕྱིར། །
ཁྱད་པར་བྱེད་དང་ཁྱད་པར་བྱ། །

[Block 1591]
ཨུཏྤལ་སྔོན་པོ་ལ་སོགས་པའི་སྒྲ་ལ་བརྟེན་ན་ཡང་གཞན་སེལ་བའི་དབྱེ་བས་རང་གི་དོན་གྱི་ཁྱད་པར་བསལ་བར་བྱ་བའི་ཕྱིར་འགྲེང་བ་དང་བྱ་བབས་པ་དག་བཞིན་དུ་གཞན་སེལ་བའི་རང་གི་དོན་གཅིག་ལ་བསྡུས་ནས་གཞི་མཐུན་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1592]
དེ་ལྟར་ན་སོ་སོ་བ་དེ་དག་རང་རང་གི་བྱེ་བྲག་ལ་ཐེ་ཚོམ་གྱི་རྒྱུ་ཅན་དུ་འདུག་པ་རྣམས་སྒྲ་གཞན་དང་ལྡན་པས་བསལ་བར༌[^1211]བྱེད་པ་མིན་པའི་ཕྱིར་དང་། དེ་ལྟ་བུ་སྲིད་པའི་ཡང་ཕྱིར་ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར་དུ་བྱ་བར་འགྱུར་བ་ཡིན་ཏེ། འདི་ལྟར་གཞི་གཅིག་ལ་དེ་སྔོན་པོ་ཡང་མ་ཡིན་ལ། ཨུཏྤ་ལ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །ཇི་ལྟར་ན་དེ་སྔོན་པོ་ཡང་ཡིན། ཨུཏྤ་ལ་ཡང་ཡིན་ཞེ་ན། བརྗོད་པར་བྱ་སྟེ། དེ་ནི་སྔོན་པོ་རྐྱང་པ༌[^1212]ཡིན། ཨུཏྤ་ལ་རྐྱང་པའང་མ་ཡིན་ཏེ། བསྡུས་པ་བརྗོད་བྱ་ཡིན་ཕྱིར་རོ། །

[Block 1593]
སྔོན་པོ་དང་ཨུཏྤ་ལའི་སྒྲ་དག་ལས་ནི་དེ༌[^1213]མཐའ་དག་ལ་སྦྱར་བར༌[^1214]བྱ་བའི་ཁ་ཡར་བ་དག་ལ༌[^1215]ནི་མ་ཡིན་ཏེ། ཁ་ཡར་བ་ནི། ཁ་དོག་བཞིན་དུ་དོན་མི༌[^1216]འགྱུར། །ཇི་ལྟར་ནིའི་སྒྲ་དང་། ལའི་སྒྲ་དག་ནི་ཡོད་དུ་ཟིན་ཀྱང་ནི་ལ་བརྗོད་པ་ལ་དོན་མེད་པ་དེ་བཞིན་དུ་འདི་ལ་ཡང་ངོ་། །

[Block 1594]
གལ་ཏེ་ཁ་དོག་བརྗོད་པ་ལ་ནི་དང་ལ་ཡིས་ཅུང་ཞིག་ཀྱང་དོན་གྱི་རྟོག་པ་མི་བསྐྱེད་དོ་ཞེས་པ་ནི་བརྒལ་ཞིང་བརྟག་པ༌[^1217]སྤང་བ༌[^1218]སྟེ།

[Block 1595 [VERSE]]
ཁ་དོག་གི་དོན་ཅུང་ཟད་ཀྱང་། །
མིན་ནའང་ཚིག༌[^1219]གཉིས་ལ་དེ་ཡིས།[^1220] །
བརྗོད་བྱ་རྟོགས་ན་དེ་ལ་ཡང་། །
ཡན་གར་བ་དེ་རྟོགས་པ་ཡིན། །

[Block 1596]
ཇི་ལྟར་ནིའི་སྒྲ་དང་ལའི་སྒྲ་དག་ནི༌[^1221]ལའི་སྒྲས་སྟོང་པ་དེ་བཞིན་དུ་ཨུཏྤ་ལ་དང་སྔོན་པོའི་སྒྲ་དག་ཀྱང་འདུས་པའི་སྒྲས་སྟོང་སྟེ། ཇི་སྐད་དུ་ནི་དང་ལའི༌[^1222]སྒྲ་ཅུང་ཟད་ཀྱང་དོན་གྱི་རྟོག་པ༌[^1223]མི་བསྐྱེད་དོ་ཞེས་པ་བཞིན་ནོ་ཞེ་ན། དེ་ལ་ཡང་རིགས་སྔོན་པོ་ནི་སྒྲའི་བརྗོད་བྱའོ་ཞེས་ཡན་གར་བ་རྟོགས་པར་བྱ་སྟེ། ཡོན་ཏན་དེའི་བརྗོད་བྱ་དང་ལྡན་པ་ཡིན་ན་ནི་རྫས་ལྡན་པའི་ལྡན་པ་ཡང་ཡིན་པས་ཁ་དོག་དོན་གྱིས་སྟོང་པ་ཉིད་བཞིན་དུ་འདུས་པ་ལ༌[^1224]ཡང་ཐ་སྙད་དེ་གོ་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1597]
སྒྲ་ཐ་དད་ཀྱི༌[^1225]བརྗོད་པ་ཡིན་ན་ནི་དོན་གྱི་ཤུགས་ཀྱིས་དོན་ཐ་དད་དོ་ཞེས་བརྗོད་པ་ཡིན་ནོ། །

[Block 1598]
དེའི་ཕྱིར་གཞན་སེལ་བའི་སྒྲའི་དོན་ལ་གཞི་མཐུན་པ་དང་། ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར་དུ་བྱ་བ་དག་འཐད་པ་ཡིན་ནོ། །

[Block 1599 [HEADING]]
#### དོན་གཞན་ལ་ནི་སྒྲའི་དོན་མི་འཐད་པ། ^5-7-2-0

[Block 1600 [HEADING]]
##### ཐ་མི་དད་པའི་ཕྱོགས་ལ་སྐྱོན་བརྗོད་པ། ^5-7-2-1-0

[Block 1601]
དོན་གཞན་ལ་ནི་སྒྲའི་དོན་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་ལ་ནི་ཡན་ལག་དང་ཡན་ལག༌[^1226]ཅན་གྱི་དོན་དག་རྟེན་དེ་ལས་ཐ་དད་པའམ། ཐ་མི་དད་པ་ཞིག་ཏུ་འགྱུར་གྲང་ན། དེ་ལ་རེ་ཞིག་ཐ་མི་དད་པ་ནི༌[^1227]མ་ཡིན་ཏེ། འདི་ལྟར།

[Block 1602]
ཕན་ཚུན་གཅིག་པར་ཐལ་འགྱུར༌[^1228]ཕྱིར། །འདུས་པ་གཅིག་ཉིད་ཡོད་མ་ཡིན། །

[Block 1603]
གལ་ཏེ་འདུས་པ་གཅིག་ཡིན་ན་ནི་དེ་ལྟར་ན་ཨུཏྤ་ལ་དང་སྔོན་པོའི་དོན་དག་གཞན་མ་ཡིན་ནོ། །

[Block 1604]
དོན་གཅིག་ལས་གཞན་མ་ཡིན་པའི་ཕྱིར་དེ་དག་ཀྱང་ཕན་ཚུན་ཐ་མི༌[^1229]དད་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1605]
གཞན་ཡང་། འདུས་པ་དུ་མར་ཐལ་བར་འགྱུར། །འདུས་པ་ནི་དུ་མ་ལས་གཞན་མ་ཡིན་པའི་ཕྱིར་དུ་མ་ཉིད་དུ་ཐལ་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1606]
འདིའི་ཕྱིར་ཡང་ཡོད་པ་མ་ཡིན་ཏེ།[^1230] ཡོད་པ་ཉིད་དུ་ཁས་བླངས་སུ་ཟིན་ཀྱང་འདུས་པ་དང་། ཨུཏྤ་ལ་སྔོན་པོའི་དོན་དག་ལ་གཞི་མཐུན་པ་མི་སྲིད་དེ།[^1231] འདི་ལྟར། གཅིག་ལ་འཇུག་པ་དག་ལ་ནི། །སྒྲ་དག་རང་དོན་སྤོང་མ་ཡིན། གང་ཡན་གར་བ་དག་སྔོན་པོ་དང་། ཨུཏྤ་ལའི་སྒྲ་དག་གི་དོན་ཡིན་ན་ནི་རང་དང་འདུས་པ་དག་ལ་ཡང་དེ་དག་ནི་དེ་ཉིད་དོ་ཞེས་གང་ལས་གཞི་མཐུན་པར་འགྱུར། གལ་ཏེ་ཉེས་པ་དེ༌[^1232]དག་ནི་མེད་དེ། སྤྱིའི་ཁོངས་སུ་བྱེ་བྲག་འདུས་པའི་ཕྱིར་དོན་གྱི་བྱེ་བྲག་དེ་གཉིས་ཀ༌[^1233]ཡང་ངོ་བོ་མཚུངས་པ་དག་ནི་སྤྱིའི་དོན་ལས་ཡིན་པས་དོན་གྱི་བྱེ་བྲག་དང་ལྡན་པ་ཤེས་པར་བྱ་བའི་ཕྱིར་གཉིས་ཀའི་སྒྲའི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 1607]
དེ་ལྟར་ན་གཉིས་ཀ་ཡང་གཞི་མཐུན་པར་འགྱུར་བ་ཡིན་ཏེ། འདུས་པའི་དོན་དང་ལྡན་པ་ཡིན་པའི་ཕྱིར་རོ་ཞེ་ན། འདི་ལ་རེ་ཞིག་སྔོན་པོའི་སྒྲས་ཐ་མི་དད་དུ་བརྗོད་ཀྱི། རིགས་ནི་མ་ཡིན་པས་རྫས་དང་རིགས་སྔོན་པོའི་སྒྲའི་སྤྱིས་བརྗོད་པ་ནི་མ་ཡིན་ན་གང་ལས་བྱེ་བྲག་དང་རྫས་དང་རིགས་ཀྱི་ཁོངས་སུ་འདུས་པར་བརྟག །གལ་ཏེ་རྫས་སྔོན་པོ་བཞིན་དུ་སྤྱིས་བརྗོད་དོ་ཞེ་ན། བྱེ་བྲག་དེ་ནི་ཡོད་དུ་ཆུག་ན་ལ་བ་དང་ཨུཏྤ་ལ་དག་ཀྱང་ཁོངས་སུ་འདུས་པར་འགྱུར་རོ། །

[Block 1608]
དེ་ལྟར་དུ་འགྱུར་བར༌[^1234]ནི་རིགས་པ་མ་ཡིན་ཏེ། [^1235]ཅིའི་ཕྱིར་ཞེ་ན། སྔར་བརྗོད་ཕྱིར། དེང༌[^1236]ལྡན་པར་བརྗོད་པ་ལ་ནི་སྔར༌[^1237]ཉིད་དུ། །རང་དབང་མེད་ཕྱིར་དེ་ལྡན་མིན། །ཞེས་བྱ་བ་ལ་སོགས་པས་མ་གྲུབ་པར་བརྗོད་དོ། །

[Block 1609]
གང་ཇི་སྐད་དུ། སྤྱིའི་ཁོངས་སུ་བྱེ་བྲག་འདུས་པའི་ཕྱིར་རོ་ཞེས་བརྗོད་པ་དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། གང་ལས་ཤེ་ན། ཐེ་ཚོམ་ཟ་ཕྱིར། སྤྱིའི་སྒྲ་ལས་བྱེ་བྲག་གི་སྒྲ་རྣམས་ལ་ཐེ་ཚོམ་ཟ་བར་མཐོང་ན་ནི་གང་ལས་ཐེ་ཚོམ་ཟ་བ་དེས་བརྗོད་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1610]
འགྱུར་དུ་ཆུག་ན་ཡང་དོན་གྱི་བྱེ་བྲག་གི་སྒྲ་ལས་ཡིན་ཏེ། སྤྱི་རྟོགས་པ་ལ་ནི༌[^1238]འཁྲུལ་བའི་ཕྱིར་གང་ཡང་འདི་སྐད་དུ་བྱེ་བྲག་གི་ཁོངས་སུ་སྤྱི་འདུས་པའི་ཞེས་བརྗོད་པར་བྱ་གྲང་ན་དེ་ལྟར་བརྗོད་པར་བྱ་བ་ལས་བརྗོད་པར་བྱ་བ་ཡང་མ་ཡིན་ནོ། །

[Block 1611]
འདི་ལྟར། གཞན་སེལ་མིན། འདི་ལྟར་སྔོན་པོའི་སྒྲ་དང་མེ་ཏོག་ཀུནྡ་ལ་སོགས་པ་བཞིན་སྔོན་པོ་ལ་སོགས་པ༌[^1239]གཞན་སེལ་བ་མ་ཡིན་ནོ། །

[Block 1612]
དེའི་ཕྱིར་ཁོངས་སུ་འདུས་པ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1613]
ཁས་བླངས་ཀྱང་བརྗོད་པར་བྱ་བ་ཉིད་ཀྱི་ཁོངས་སུ༌[^1240]འདུས་པ་ཡིན་ནོ། །

[Block 1614]
གལ་ཏེ་གཉིས་ཀ་ཡང་བྱེ་བྲག་གི་དོན་དུ་ཡིན་ན་ནི་རྣམ་གྲངས་པའི་སྒྲར་འགྱུར་ཏེ། གཅིག་ལས་རྣམ་གྲངས་སུ་འགྱུར་བས༌[^1241]མཐོང་བ་ཡིན་ནོ། །

[Block 1615]
རྣམ་གྲངས་ཀྱི་སྒྲ་ནི་མ་རྟོགས་པ་དང་། དོན་དུ་མ་ལ༌[^1242]ཡིན་གྱི་སྔར་གྱི་དོན་དེ་ཉིད་རྟོགས་པར་བྱ་བའི་ཕྱིར༌[^1243]རྣམ་གྲངས་གཞན་སྦྱོར་བ་ཡིན་ནོ། །
--- END BLOCKS ---
