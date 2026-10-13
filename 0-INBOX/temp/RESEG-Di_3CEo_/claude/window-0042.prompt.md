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
[Block 1471]
ཁོར་ཡུག་ཏུ་ནི་སུམ་འགྱུར་རོ།[^553] །

[Block 1472]
ཁོ་ར་ཁོར་ཡུག་ཏུ་བརྩི་བ༌[^554]ནི་སུམ་འགྱུར་རོ། །

[Block 1473 [HEADING]]
#### རི་ཆེན་པོ་བརྒྱད། ^3-2-2-0

[Block 1474 [VERSE]]
དེ་ལ་ལྷུན་པོ་གཉའ་ཤིང་འཛིན། །
གཤོལ་མདའ་འཛིན་དང་སེང་ལྡེང་ཅན། །
དེ་བཞིན་བལྟ་ན་སྡུག་རི་དང་། །
རྟ་རྣ་དང་ནི་རྣམ་འདུད་དང་། །
མུ་ཁྱུད་འཛིན་རིའོ། །

[Block 1475]
འདི་ལྟར་རི་ཆེན་པོ་བརྒྱད༌[^555]ནི་གསེར་གྱི་དཀྱིལ་འཁོར་ལ་བརྟེན་པ་ཡིན་ཏེ། རི་རབ་ནི་དབུས་ནའོ། །

[Block 1476]
ལྷག་མ་རྣམས་ཀྱིས་ནི་རི་རབ་ལ་བསྐོར་ཏེ་གནས་སོ། །

[Block 1477]
གང་ཕྱིར་རི་མུ་ཁྱུད་འཛིན། དེ་ནས་ནི་གླིང་རྣམས་ཡིན་ནོ། །

[Block 1478]
དེའི་ཕྱི་རོལ་ན་ནི་གླིང་བཞིའོ། །

[Block 1479]
དེ་དག་གི་ཡང་། ཕྱི་རོལ༌[^556]ན་ནི་ཁོར་ཡུག་སྟེ། །དེས་ནི་གླིང་བཞི་ཁོར་ཡུག་ཏུ་བསྐོར་བའོ། །

[Block 1480]
དེ་དག་ལས།

[Block 1481]
བདུན་ནི་གསེར་ཡིན་དེ༌[^557]ལྕགས་སོ། །

[Block 1482]
གཉའ་ཤིང་འཛིན་ལ་སོགས་པའི་རི་བདུན་ནི་གསེར་གྱིའོ། །

[Block 1483]
ཁོར་ཡུག་ནི་ལྕགས་སོ། །

[Block 1484]
ལྷུན་པོ་རིན་ཆེན་བཞི་ཡི༌[^558]རང་བཞིན་ཅན། །གསེར་དང་། དངུལ་དང་། བཻ་ཌཱུཪྻ་དང་། ཤེལ་གྱི་རང་བཞིན་ནོ། །

[Block 1485]
རི་དེ་དག་ཀྱང་། ཆུ་ཡི་ནང་དུ་བརྒྱད་ཁྲི་དག་ནུབ་བོ། །

[Block 1486]
གསེར་གྱི་ས་གཞིའི་སྟེང་དུ་ཆུ་དཔག་ཚད་བརྒྱད་ཁྲི་ཡོད་པ་དེར་ནུབ་བོ། །

[Block 1487]
ཆུའི་སྟེང་དུ་ཡང་། དཔག་ཚད་དག་ནི་བརྒྱད་ཁྲིའོ། །

[Block 1488]
དེ་ལྟར་ན་རི་རབ་ནི་འཕང་དུ་དཔག་ཚད་འབུམ་དྲུག་ཁྲིའོ། །

[Block 1489]
བརྒྱད་པོའི་འཕང་དུ་ཕྱེད་ཕྱེད་དབྲི། །རི་རབ་ཆུའི་སྟེང་དུ་ཇི་ཙམ་འཕགས་པ་དེའི་ཕྱེད་ནི་གཉའ་ཤིང་འཛིན་ཡིན་ཏེ།

[Block 1490 [VERSE]]
དེ་བཞིན་དུ་ལྷག༌[^559]མ་རྣམས་སོ། །
དེ་དག་རྔམས་སུའང་འཕང་དང་མཉམ། །

[Block 1491]
ད་དག་ཆུ་ལས་གྱེན་དུ་འཕགས་པ་རྔམས་སུ་ཡང་དེ་ཙམ་སྟེ། རྒྱ་ཆེར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1492]
དེ་དག་བར་བདུན་རོལ་མཚོ་ཡིན། མུ་ཁྱུད༌[^560]འཛིན་ལ་ཐུག༌[^561]པའི་རི་དེ་དག་གི་བར༌[^562]བདུན་ནི་རོལ་མཚོ་བདུན་ཞེས་བྱའོ། །

[Block 1493]
ཡང་དེ་དག་ལས། དང་པོ་སྟོང་ཕྲག་བརྒྱད་ཅུའོ། །

[Block 1494]
རྒྱར་རོ་དེ་ནི་ནང་གི་རྒྱ་མཚོ་ཡིན། །དེ་ཡི་ངོས་ལ་སུམ་འགྱུར་རོ། །

[Block 1495]
གཉའ་ཤིང་འཛིན་གྱི་འགྲམ་གཅིག་ནས་བརྩིས་ན་དཔག་ཚད་ཉིས་འབུམ་བཞི་ཁྲིའོ། །

[Block 1496]
རོལ་མཚོ་གཞན་ནི་ཕྱེད་ཕྱེད་དབྲི། །དཔག་ཚད་སྟོང་ཉིས་བརྒྱ་ལྔ་བཅུའོ་ཞེས་བྱ་བའི་བར་དུ་རོལ་མཚོ་བདུན་ནོ། །

[Block 1497]
དེ་དག་གི་སྲིད་དུ་ནི་ཧ་ཅང་འབྱམ་ཀླས་པའི་ཕྱིར་མ་བགྲངས་སོ། །

[Block 1498]
ལྷག་མ་ཕྱི་ཡི་མཚོ་ཆེན་ཡིན། །མུ་ཁྱུད༌[^563]འཛིན་ནས་ཁོར་ཡུག་གི་བར་ལྷག་མ་དེ་ནི་ཕྱིའི་རྒྱ་མཚོ་ཆེན་པོའོ། །

[Block 1499]
ཁ་ཆོན་དུ་དཔག་ཚད་འབུམ་ཕྲག་གསུམ་དང་སྟོང་ཕྲག་ནི། ཉི་ཤུ་གཉིས་སོ། །

[Block 1500 [HEADING]]
#### གླིང་བཞི། ^3-2-3-0

[Block 1501]
དེ༌[^564]རི་རབ་ཀྱི་ངོས་བཞིར་གླིང་བཞི་སྟེ། དེ་ལ་ནི།

[Block 1502 [VERSE]]
འཛམ་བུའི་གླིང་སྟེ་ངོས་གསུམ་ལ། །
སྟོང་ཕྲག་གཉིས་པོ༌[^565]ཤིང་རྟའི་དབྱིབས། །

[Block 1503]
དེའི་ངོས་གསུམ་ནི་དཔག་ཚད་ཉིས་སྟོང་ཉིས་སྟོང་ཡོད་ལ་དབྱིབས་ནི་ཤིང་རྟ་དང་འདྲའོ། །

[Block 1504]
གཅིག་ལ་དཔག་ཚད་ཕྱེད་དང་བཞི། །དེའི་ངོས་གཅིག་ལ་དཔག་ཚད་ཕྱེད་དང་བཞིའོ། །

[Block 1505]
ཤར་གྱི་ལུས་འཕགས་ཟླ་ཁམ༌[^566]འདྲ། །ཤར་གྱི་ལུས་འཕགས་ཀྱི་གླིང་ནི་ཟླ་ཁམ་གྱི་དབྱིབས་སོ། །

[Block 1506]
རྒྱར་ནི། ངོས་གསུམ་འདི་དང་འདྲ། །ཇི་ལྟར་འཛམ་བུའི་གླིང་ལ་དཔག་ཚད་སྟོང་ཕྲག་གཉིས་གཉིས་བཞིན་ནོ། །

[Block 1507]
གཅིག་ལ་དཔག་ཚད་སུམ་བརྒྱ་ལྔ་བཅུའོ། །

[Block 1508]
ངོས་བཞི་པ་ལ་ནི་དཔག་ཚད་སུམ་བརྒྱ་ལྔ་བཅུའོ། །

[Block 1509]
བ་ལང་སྤྱོད་གླིང་ཟླུམ་པོ་སྟེ།

[Block 1510 [VERSE]]
སྟོང་ཕྲག་ཕྱེད་དང་བརྒྱད་ཡིན་ནོ། །
དེ་དབུས་སྟོང་ཕྲག་ཕྱེད་དང་གསུམ་མོ། །
སྒྲ་མི་སྙན་བརྒྱད་གྲུ་བཞིར་མཉམ། །
--- END BLOCKS ---
