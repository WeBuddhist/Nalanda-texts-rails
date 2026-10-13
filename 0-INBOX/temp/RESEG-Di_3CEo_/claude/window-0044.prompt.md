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
[Block 1541 [HEADING]]
#### ཉི་མ་དང་ཟླ་བ། ^3-2-6-0

[Block 1542]
ཉི་མ་དང་ཟླ་བ་འདི་ནས་ཐག་ཇི་སྲིད་ཅེ་ན། ཉི་ཟླ་ལྷུན་པོའི་ཕྱེད་ནའོ། །

[Block 1543]
རི་གཉའ་ཤིང་འཛིན་གྱི་རྩེ་མོ་དང་མཉམ་པར་རྒྱུའོ། །

[Block 1544]
ཚད་ཀྱང་། དཔག་ཚད་ལྔ་བཅུ་གཅིག་དང་བཅས། །རིམ་པ་བཞིན་དུའོ། །

[Block 1545]
གླིང་བཞི་པོ་དག་ཏུ་ཉི་མས་ཅིག་ཅར་བྱ་བ་བྱེད་དམ་ཞེ་ན། མ་ཡིན་ཏེ། འོན་ཀྱང་།

[Block 1546 [VERSE]]
ནམ་ཕྱེད་ཉི་མ་ནུབ་པ་དང་། །
ཉི་མ་ཕྱེད་དང་འཆར་དུས་གཅིག །

[Block 1547]
གང་གི་ཚེ་བྱང༌[^579]སྒྲ་མི་སྙན་དུ་ནམ་ཕྱེད་པ་དེའི་ཚེ་ཤར་ལུས་འཕགས་སུ་ཉི་མ་ནུབ་བོ། །

[Block 1548]
འཛམ་བུའི་གླིང་དུ་ཉི་མ་ཕྱེད་དོ། །

[Block 1549]
བ་ལང་སྤྱོད་དུ་ཉི་མ་ཤར་ཏེ། དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1550]
ཉི་མ་འགྲོ་བའི་བྱེ་བྲག་ལས་ཉིན་མོ་དང་མཚན་མོ་རྣམས་རིང་ཐུང་དུ་འགྱུར་ཏེ། དེ་ལ་ཡང་།

[Block 1551 [VERSE]]
དབྱར་གྱི་ཟླ་བ་གཉིས་པ་ཡི། །
ཐ་མའི་ཚེས་དགུ་ནས་མཚན་རིང་། །

[Block 1552]
དབྱར་ཟླ་ཐ་ཆུངས་ཡར་གྱི་ངོའི་ཚེས་དགུ་ནས་མཚན་མོ་རིང་ངོ་། །དགུན་རྣམས་ཀྱི་ནི་བཞི་པ་ལ། །ཐུང་ངུ་འགྱུར་རོ། །

[Block 1553]
དགུན་ཟླ༌[^580]ཐ་ཆུངས་ཀྱི་ཕྱོགས་གཉིས་པའི་ཚེས་དགུ་ནས་སོ། །

[Block 1554]
ཉིན་མོ་བཟློག །གང་གི་ཚེ་ཉིན་མོ་རིང་བ་དེའི་ཚེ་མཚན་མོ་ཐུང་བར་འགྱུར་རོ། །ཇི་ཙམ་ཞིག་གིས་རིང་བར་འགྱུར་ཞེ་ན།

[Block 1555 [VERSE]]
ཉིན་མཚན་རིང་བ་ཐང་གཅིག་གོ། །
དེ་དག་ཀྱང་གོ་རིམས་བཞིན་དུ།
ཉི་མ་ལྷོ་བྱང་འགྲོ་བའི༌[^581]ཚེའོ། །

[Block 1556]
དཀར་པོའི༌[^582]ཕྱོགས་ཀྱི་དང་པོ་ཟླ་བའི་དཀྱིལ་འཁོར་མ་རངས་པར་སྣང་བ་དེ་ལ་རྒྱུ་ཅི་ཞེ་ན།

[Block 1557 [VERSE]]
ཉི་མ་དང་ནི་ཉེ་བ་ལས། །
རང་གི་གྲིབ་མས་བསྒྲིབས་པར༌[^583]སྣང་། །

[Block 1558]
གང་གི་ཚེ་ཟླ་བའི་གཞལ་མེད་ཁང་ཉི་མའི་གཞལ་མེད་ཁང་དང་ཉེ་བར་རྒྱུ་བ་དེའི་ཚེ་ཉི་མའི་འོད་དེ་གཞལ་མེད་ཁང་ལ་འབབ་སྟེ། དེས་ན་དེའི་ཕ་རོལ་གྱི་ངོས་སུ་གྲིབ་མ་འབབ་པས་ཟླ་བའི་དཀྱིལ་འཁོར་མ་རངས་པར་སྣང་ངོ་ལོ། །

[Block 1559 [HEADING]]
#### ལྷའི་གནས། ^3-2-7-0

[Block 1560]
ཡང་ཉི་མ་དང་ཟླ་བ་དང་སྐར་མ་དག་གི་ལྷ་རྣམས་ལྷའི་རིས་གང་དུ་ཞེ་ན། རྒྱལ་པོ་ཆེན་པོ་རྣམས་སུའོ། །ཅི་དེ་དག་གི་གནས་འདི་ཙམ་ཁོ་ནའམ་ཞེ་ན། མ་ཡིན་ཏེ། འོན་ཀྱང་ལྷུན་པོའི་བང་རིམ་དག་ཀྱང་ངོ་། །

[Block 1561]
འདི་ལ་བང་རིམ་ནི་དུ་ཞིག །ཐག༌[^584]སྲིད་ཅེ་ན། འདི་ལ་བང་རིམ་བཞི་ཡོད་དེ།

[Block 1562 [VERSE]]
བར་གྱི་ཐག་ནི་སྟོང་ཕྲག་བཅུ། །
དཔག་ཚད་ཁྲིའི་ལྷག་ན་གཅིག་ཡོད་དེ།[^585] །
བཞི༌[^586]པོའི་བར་དུ་ཡང་དེ་དང་འདྲའོ། །

[Block 1563]
དེ་དག་ཀྱང་དེ་ལས་གྲངས་བཞིན་དུ་སྟེ།

[Block 1564 [VERSE]]
སྟོང་ཕྲག་དག་ནི་བཅུ་དྲུག་དང་། །
བརྒྱད་དང་བཞི་དང་གཉིས་འཕགས་སོ། །

[Block 1565]
དང་པོ་ནི་རི་རབ་ལས་དཔག་ཚད་སྟོང་ཕྲག་བཅུ་དྲུག་འཕགས་སོ། །

[Block 1566]
གཉིས་པ་ནི་བརྒྱད་དོ། །

[Block 1567]
གསུམ་པ་ནི་བཞིའོ། །

[Block 1568]
བཞི་པ་ནི་གཉིས་སོ། །

[Block 1569 [VERSE]]
དེ་ལ་ལག་ན་གཞོང་ཐོགས་དང་། །
ཕྲེང་ཐོགས་དང་ནི་རྟག་མྱོས་དང་། །
རྒྱལ་ཆེན་བཞི་པའི༌[^587]ལྷ་རྣམས་གནས། །

[Block 1570]
འདི་དག་ལ་གྲངས་བཞིན་དུ་གཞོང་ཐོགས་ལ་སོགས་པ་རྣམས་གནས་ཏེ། རི་ནི་བདུན་པོ་དག་ལ་ཡང་། །གཉའ་ཤིང་འཛིན་ལ་སོགས་པར་ཡང་དེ་དག་གི་གྲོང་དང་གྲོང་རྡལ་དག་གོ། །

[Block 1571]
ལྷུན་པོའི་རྩེ་ན་སུམ་ཅུ་གསུམ། །ཡང་ལྷུན་པོའི་རྩེ་མོ་ཇི་ཙམ་ཞེ་ན། དེ་ཡི་ངོས་ལ་བརྒྱད་ཁྲིའོ། །

[Block 1572 [VERSE]]
ངོས་རེ་རེ་ལ་བརྒྱད་ཁྲི་བརྒྱད་ཁྲིའོ། །
ཕྱོགས་མཚམས་བརྩེགས་པ་བཞི་ལ་ནི། །
ལག་ན་རྡོ་རྗེ་གནས།

[Block 1573]
རི་རབ་ཀྱི་རྩེ་མོའི་མཚམས་ནི་གྲྭ་བཞི་སྟེ། དེ་དག་ལས་དཔག་ཚད་ལྔ་བརྒྱའི་ཚད་ཙམ་གྱིས་བརྩེགས་པ་བཞི་ལ་གྱེན་དུ་འཕགས་ཏེ། དེ་དག་ལ་གནོད་སྦྱིན་ལག་ན་རྡོ་རྗེ་ཞེས་བྱ་བ་གནས་སོ། །

[Block 1574]
རི་རབ་དེའི་སྟེང་གི་དབུས་ན། གྲོང་ཁྱེར་བལྟ་ན་སྡུག་ཅེས་པ།

[Block 1575 [VERSE]]
ངོས་ལ་ཉིས་སྟོང་ལྔ་བརྒྱ་པ། །
དཔག་ཚད་ཕྱེད་དང་གཉིས་གསེར་གྱི།[^588] །
རང་བཞིན་བཞི༌[^589]བཀྲ་མཉེན་པ༌[^590]ཡོད། །

[Block 1576]
ངོས་རེ་རེ་ཞིང་དཔག་ཚད་ཉིས་སྟོང་ལྔ་བརྒྱ་པ། འཕང་དུ་དཔག་ཚད་ཕྱེད་དང་གཉིས་པ་དེ་ནི་རྒྱལ་པོའི་ཕོ་བྲང་ངོ་། །

[Block 1577 [VERSE]]
དེ་ནི་རྣམ་པར་རྒྱལ་བྱེད་དེ། །
ངོས་ལ་ཉིས་བརྒྱ་ལྔ་བཅུའོ། །

[Block 1578]
གྲོང་ཁྱེར་གྱི་དབུས་ན་རྣམ་པར་རྒྱལ་བྱེད་ཅེས་བྱ་བའི་ཁང་བཟངས་ངོས་དང་ངོས་ཀྱི་སྲིད་དུ་དཔག་ཚད་ཉིས་བརྒྱ་ལྔ་བཅུ་པ་ཞིག༌[^591]ཡོད་དོ། །

[Block 1579]
རེ་ཞིག་འདི་ནི་གྲོང་གི་མངོན་པར་དགའ་བ་ཡིན་ནོ། །

[Block 1580 [VERSE]]
ཕྱི་རོལ་ཤིང་རྟ་སྣ་ཚོགས་དང་། །
རྩུབ་འགྱུར་འདྲེས་ཚལ་དགའ་བས་བརྒྱན། །
ངོས་བཞིའི་ཚལ་བཞི་ནི་ལྷ་རྣམས་ཀྱིའོ། །
དེ་དག་གི་ནི་ཕྱོགས་བཞི་ན། །
--- END BLOCKS ---
