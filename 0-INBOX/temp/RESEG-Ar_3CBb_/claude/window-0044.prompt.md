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
[Block 1541]
དེ་ཐམས་ཅད་དབྱེ་བ༌[^818]མེད་པར་གྱུར་པ༌[^819]ནི་དེའི་འབྲས་བུའོ། །

[Block 1542]
འདི་ནི་ཐམས་ཅད་རང་གིས་བརྟགས་པས་སླུ༌[^820]བ་སྟེ།

[Block 1543]
བདེན་པར་གྱུར་པའི་དོན་མཐོང་བས། །དམན་ལ་བདེན་པར་གྱུར་པ་སླུ། །ཞེས་འབྱུང་བ་ལྟ་བུའོ། །

[Block 1544]
གཞན་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 1545]
གཤིན་རྗེ་ནི་དམྱལ་བའི་སྲུང་མ་དང་བཅས་པ་སྟེ་དེ་ན་དབང་ཆེ་བར་སྣང་བའི་ཕྱིར་རོ། །

[Block 1546]
ཁྲོ་བོ་ཆེན་པོ་ནི་དེ་དག་འཇིགས་པར་སྣང་བའོ། །

[Block 1547]
མཐར་ཐུག༌[^821]མཛད་ཅིང་འཇིགས་པ་ནི་གཏུམ་པོའི་ལས་ཀྱི༌[^822]དོན་ཆེན་པོ་དང་ལྡན་པར་བྱེད་པའོ། །

[Block 1548]
རྨོངས་པའི་མུན་པ་ཉིད་མ་རིག་པ༌[^823]སྟེ་དམན་པར་གྱུར་པའི་ཕྱིར་སྡུག་བསྔལ་སྣ་ཚོགས་ཉམས་སུ་མྱོང་བར་བྱེད་པས་གཤིན་རྗེའོ། །

[Block 1549]
དོན་དམ་པའི་བདེན་པས་མཐར་ཐུག༌[^824]པར་མཛད་པ་ནི་རང་བཞིན་གྱིས་བག་ཆགས་དང་བཅས་ཏེ་རྩད་ནས་གདོན་པའི་ཕྱིར་རོ། །

[Block 1550]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་མངོན་པར་བྱང་ཆུབ་པ་ཡང་གང་ཞེ་ན་རིན་ཆེན་འབྱུང་ལྡན་ནོ། །

[Block 1551]
འོད་གསལ་བ་ནི་མངོན་པར་བྱང་ཆུབ་པ་ལས་བྱུང་བ་དང་། དེའི་ངོ་བོ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1552]
དེ་ཉིད་ནི་མི་ཕྱེད་པས་རྡོ་རྗེའོ། །

[Block 1553]
རྣམ་པར་རྟོག་པའི༌[^825]བདག་ཉིད་ཅན་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་མཚུངས་པར༌[^826]ལྡན་པའོ། །

[Block 1554]
དེ་འོད་གསལ་བར་འཇུག་པ་ནི་སྟོང་པ་ཉིད་དུ་བྱས་པའོ། །

[Block 1555]
རྡོ་རྗེའི་དམ་ཚིག་ནི་གང་ཞིག་དེས་གང་བསྙེངས་པར་བྱ་ཞེ་ན་རྡོ་རྗེ་ནི་དེ་བཞིན་གཤེགས་པའི་ཁྲོ་བོའི་ཚུལ་ཅན་ཏེ་དེས་གདུག་པ་ཅན་སློབ་དཔོན་ལ་སྡང་བ་ལ་སོགས་པ་བསྲེགས་པ་ནི་དོན་ཆེན་པོ་དང་ལྡན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1556]
ཡང་བྱེ་བྲག་བསྡུ་བ་སྟེ། རྡོ་རྗེ་དམ་ཚིག་ཉིད་སྲེག༌[^827]པའོ། །

[Block 1557]
འོད་དཔག་ཏུ་མེད་པ་ནི་ཆོས་རིན་པོ་ཆེ་སྟེ་ཆོས་ཐམས་ཅད་ཀྱི་འབྱུང་གནས་སུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1558]
རྟ་མགྲིན་ཡང་འོད་དཔག་ཏུ་མེད་པ་སྟེ་དེའི་རིགས་སུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1559]
འོད་གསལ་བ་ནི་ཆོས་རིན་པོ་ཆེ་སྟེ་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1560]
རྟ་མགྲིན་ཡང་དེ་ལས་བྱུང་བའི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1561]
ཉོན་མོངས་པ་རྣམས་ཀྱིས་མ་གོས་པ་ནི་དེའི་རང་བཞིན༌[^828]ཡིན་པའི་ཕྱིར་རོ། །

[Block 1562]
དེ་ཉིད་འཇིགས་པར༌[^829]མཛད་པ་ནི་དེ་དང་ལྷན་ཅིག་པར་འགལ་བའི་ཕྱིར་རོ། །

[Block 1563]
པདྨ་ནི་སྐྱེ་གནས་སོ་ཞེས་པ་ལ་སོགས་པའི་དོན་ནི་རྡོ་རྗེ་པདྨ་སྙོམས་པར་ཞུགས་པས་བྱང་ཆུབ་སེམས་ཕབ་སྟེ་དེས་བདེ་བ་དང་བདེ་བ་དམ་པ་སྐྱེ་བར་འགྱུར་རོ་ཞེས་པའི་དོན་ཏོ། །

[Block 1564]
རྣམ་པར་དག་པའི་གནས་ནི་རྣམ་པར་དག་པར་བྱེད་པའི་རྟེན་ཏེ་གང་ཡིན་ཞེ་ན་འོད་གསལ་བའོ། །

[Block 1565]
བགེགས་ནི་བི་ནཱ་ཡ་ག་ལ་སོགས་པ་སྟེ་དེ་མཐར་བྱེད་པ་ནི་ཐབས་གང༌[^830]གི་སྒོ་ནས་དོན་ཆེན་པོ་ལྡན་པར་བྱེད་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1566]
དེས་པའི་དོན་དུ་བགེགས་ཞེས་བྱ་བ་གང་ཞིག་ཅེ་ན། བགེགས་ནི་ཁམས་བཞི་པོ་སྟེ། ས་དང་ཆུ་དང་མེ་དང་རླུང་རང་གི་ལུས་ཀྱིས་བསྡུས་པའོ། །

[Block 1567]
དེ་ལ་ཡང་ཅིའི་ཕྱིར་ཞེ་ན། དེ་དག་འཕེལ་བ་དང་འགྲིབ་པས་ལུས་གཟིར་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1568]
ཐབས་ཀྱི༌[^831]ཡེ་ཤེས་ཤར་བས་རྣམ་པར་འཇིག་པ་ནི་གང་གིས་ལུས་ཀྱི་རྒྱུན་ལས་བྱང་ཆུབ་སེམས་ཕབ་སྟེ་དེའི་ཉེས་པ་དང་བྲལ་བར་བྱས་པ་ཉིད་དོ། །

[Block 1569]
འདི་ལ་ཁ་ཅིག་གིས༌[^832]འདི་སྐད་ཅེས་དེ་བཞིན་གཤེགས་པའི་གཙོ་བོ་དང་འཁོར་གྱི་རྣམ་པར་སྣང་བ་འདི༌[^833]ཐ་དད་པའམ་གཅིག་པའམ་དེ་ལས་གཞན་དུ་འགྱུར་ཞེས་རྟོག་དྲང༌[^834]ན། རེ་ཞིག་དང་པོར་ཐ་དད་པ་ནི་མ་ཡིན་ཏེ་སོ་སོར་མ་འདྲེས་པར་རྣམ་པར་སྣང་བའི་ཕྱིར་དང་གང་གིས་རག་ལས་དེའི་དབང་གིས་འགྱུར་རོ་ཞེས་བྱ་བར་ཡང་མི་ནུས་ཏེ། དུང་དང་དཀར་པོ་ལྟ་བུའོ། །

[Block 1570]
རང་གི་བློ་དང༌[^835]འགྱུར་བ་ཡང་མ་ཡིན་ཏེ་བརྟགས་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1571]
གལ་ཏེ་ཡིན་ནོ་ཞེ་ན་ཡང་བླང་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 1572]
ཕྱོགས་ངེས་པར༌[^836]འགྲུབ་པར་མི་འགྱུར་ཏེ་དེ་ཉིད་ཀྱི་ཕྱིར་ཐ་དད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1573]
གལ་ཏེ་གཅིག་པ་ཉིད་དོ་ཞེ་ན་ཡང་ཤིན་ཏུ་རིགས་པ་མ་ཡིན་ཏེ། ཁ་དོག་དང་གནས་ལ་སོགས་པ་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 1574]
གལ་ཏེ་གནས་གཅིག་པས་གཅིག་པ་ཉིད་དོ་ཞེ་ན་ཡང་རིགས་པ་མ་ཡིན་ཏེ། ཐམས་ཅད་སའི་དཀྱིལ་འཁོར་གཅིག་ལ་བརྟེན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1575]
གལ་ཏེ་ལུས་འདྲ་བས་གཅིག་པ་ཉིད་དོ༌[^837]ཞེ་ན་ཡང་མ་ཡིན་ཏེ་གང་གིས་མི་རྣམས་ཀྱི༌[^838]ལུས་འདྲ་བས་གཅིག་པ་མ་གྲུབ་པ་བཞིན་ནོ། །

[Block 1576]
གལ་ཏེ་ཡེ་ཤེས་གཅིག་པ་ཉིད་ཀྱིས་གཅིག་པ་ཉིད་དོ་ཞེ་ན་ཡང་མ་ཡིན་ཏེ་མི་རྟག་པ་དང་མི་རྟག་པ་ཅན་ཡང་ཤིན་ཏུ་གཅིག་པར་འགྱུར་རོ། །

[Block 1577]
གལ་ཏེ་རིག་པ་ཙམ་དུ་འདོད་པའོ་ཞེ་ན་ཡང་མ་ཡིན་ཏེ་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་སོ་སོའི་སྐྱེ་བོའི་བར་ལ་སོགས་པ་ཟག་པ་མེད་པའི་ས་བོན་དང་བཅས་པས་བསྡུས་པའི་ཕྱིར་ཐམས་ཅད་ཀྱང་ངོ་། །གལ་ཏེ་ཤེས་པ་ཐ་དད་དུ་གྱུར་པས་ཡིན་ནོ་ཞེ་ན་སོ་སོ་རང་གི་རིག་པས་བརྟགས་ན་དབྱེར་མེད་པའི་ཕྱིར་རོ། །

[Block 1578]
[^839]ཡང་སྔ་མའི་ས༌[^840]ན་འདུག་པ་ཉིད་དོ་ཞེ་ན་ཡང་མ་ཡིན་ཏེ། རང་གི་གདུལ་བྱའི་དབང་གིས་སྣ་ཚོགས་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 1579]
དེ་བས་ན་འདིར་ཡང་སངས་རྒྱས་ཐམས་ཅད་དབྱེར་མེད་ཀྱང་རང་གི་གདུལ་བྱའི་དབང་གིས༌[^841]སྣ་ཚོགས་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 1580]
གལ་ཏེ་དེ་ལྟ་ན། གཅིག་པར་འགྱུར་རོ་ཞེ་ན་དེ་ནི་འདོད་པ་སྟེ། དེའི་རང་བཞིན་གྱི་ཕྱིར་དུས་ཐམས་ཅད་དུ་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །
--- END BLOCKS ---
