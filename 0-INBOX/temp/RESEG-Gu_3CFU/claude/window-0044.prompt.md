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
དགེ་ཚུལ་ལམ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པ་ཉིད་དགེ་ཚུལ་ལ་བརྟེན་པ་ཞེས་བྱ་བ་ཡོད་པ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་དགེ་ཚུལ་ལ་བརྟེན་པ་ཉིད་ཤེས་པ་ལ་བསྙེན་པར་རྫོགས་པ་འབུལ་བ་ལའོ། །

[Block 1542]
ཟ་མའམ་མ་ནིང་ངམ་ཞེས་བྱ་བ་ནི་ཞིང་མ་ཡིན་པ་ལ་སྡོམ་པའི་དངོས་པོ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཟ་མའམ་མ་ནིང་ཉིད་དུ་དམ་བཅས་པ་ལ་སྡོམ་པ་ཐམས་ཅད་འབུལ་བ་ལའོ། །

[Block 1543]
དགེ་སློང་མ་སུན་ཕྱུང་བའམ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་སུན་ཕྱུང་བ་ཉིད་ནི་ཞིང་མ་ཡིན་པ་ཉིད་ཀྱི་རྟོག་པས་གལ་ཏེ་དམ་བཅས་ན་དེ་ལྟ་བུ་ཉིད་འདི་ལ་གོ་བ་ཉིད་དེ་ཕམ་པ་ཉིད་ཀྱི་བསམ་པས་གལ་ཏེ་འཕོ་བ་ཉིད་འདིར་རབ་ཏུ་བྱུང་བའི་ཕྱིར་ཞེས་བྱ་བའི་བློ་གང་ཡིན་པ་དེའི་དབང་གིས་སོ། །

[Block 1544]
རྐུ་ཐབས་སུ་གནས་པའམ་ཞེས་བྱ་བ་ནི་དམ་བཅས་པ་ལ་ཞིང་མ་ཡིན་པ་ཉིད་ཀྱི་བསམ་པ་ཉིད་ལ་ཟ་མ་དང་མ་ནིང་ཉིད་དུ་དམ་བཅས་པ་བཞིན་གོ་བར་བྱེད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1545]
སྡོམ་པ་མ་བླངས་པའི་བསམ་པ་ཉིད་ལ་ཁྱིམ་ན་གནས་པ་དམ་བཅས་པ་བཞིན་དུའོ། །

[Block 1546]
ཐ་དད་པར་གནས་པའམ་ཞེས་བྱ་བ་ལ། ཐ་དད་པར་གནས་པ་ཞེས་བྱ་བ་ནི་དམ་བཅས་པ་ལ་སྨོན་པའི༌[^1083]ཕྱོགས་ཀྱི་ནང་ན་གནས་པ་ཉིད་ཀྱི་བསམ་པ་ལ་འབུལ་བ་ལ་གོ་བར་བྱེད་པ་ཉིད་ནི་ཡོད་པ་མ་ཡིན་པ་སྟེ། རབ་ཏུ་བྱུང་བ་ཀུན་ལས་འདི་ཐ་དད་པ་ཉིད་ཅེས་བྱ་བ་མངོན་པར་འདོད་པ་ལ་ཁྱིམ་པ་ཉིད་དུ་དམ་བཅས་པ་བཞིན་དུའོ། །

[Block 1547]
བསྙེན་པར་རྫོགས་པ་ཐམས་ཅད་ལས་འདི་ཐ་དད་པ་གནས་པ་ཞེས་བྱ་བ་འདི་དགེ་ཚུལ་ཉིད་དུ་དམ་བཅས་པ་བཞིན་དུའོ། །

[Block 1548]
གནས་པར་མི་བྱ་བའམ་ཞེས་བྱ་བ་ལ། གནས་པར་མི་བྱ་བ་ནི་དམ་བཅས་པ་འདི་ཕམ་པ་ཉིད་དེ་ཞེས་བྱ་བ་ཕྱོགས་འདི་ལ་དགེ་སློང་མ་སུན་འབྱིན་པར་བྱེད་པ་ལ་དམ་བཅས་པ་བཞིན་དུའོ། །

[Block 1549]
མུ་སྟེགས་ཅན་ཞེས་བྱ་བ་ལ། མུ་སྟེགས་ཅན་ནི་ཞིང་མ་ཡིན་པ་ཉིད་ཀྱིས་བསམ་པ་ཉིད་ལ་མུ་སྟེགས་ཅན་ཞུགས་པ་ལ་རིགས་པ་ཡིན་ཏེ། དེ་ལ་ཟ་མ་དང་མ་ནིང་ཉིད་དུ་དམ་བཅས་པ་བཞིན་དུའོ། །

[Block 1550]
དགེ་འདུན་གྱི་དབྱེན་བྱས་པའམ། དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བར་གཟུང་དུ་གསོལ་ཞེས་བྱ་བ་ལ། དགེ་འདུན་གྱི་དབྱེན་བྱས་པ་དང་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བ་ཞེས་བྱ་བ་ནི་འདི་ཉིད་རིགས་པ་ཡིན་ཏེ། དེ་དག་ལ་ཡང་དེ་བཞིན་དུའོ། །

[Block 1551]
མཚམས་མེད་པ་ལྷག་མ་རྣམས་བྱེད་པ་ལ་ཞིང་མ་ཡིན་པ་ཉིད་ཀྱིས་བསམ་པ་ལ་ཡང་སྦྱར་བ་དང་ཕམ་པ་ཉིད་ནི་བསམ་པ་ཡང་སྦྱར་བའོ། །

[Block 1552]
ཞིང་མ་ཡིན་པ་ཉིད་དུ་རྟོགས་པ་ལ་འདི་རྣམས་ཀྱང་དམ་བཅས་པ་ལ་དེ་ལྟ་བུ་ཉིད་དུ་ཕམ་པར་འགྱུར་བའི་བསམ་པ་ཅན་ལ་གནས་པར་མི་བྱ་བ་ཉིད་དུ་དམ་བཅས་པ་བཞིན་དུའོ། །

[Block 1553]
བདག་ལ་ཆོག་གོ་ཞེས་བྱ་བ་ནི་ཐ་དད་པའི་དངོས་པོའི་ཚིག་ནི་འདི་ལ་ཐ་དད་པར་གནས་པ་ཉིད་དུ་དམ་བཅས་པ་བཞིན་དུའོ། །

[Block 1554]
འབུལ་བའི་ཆོ་གའོ།། །།

[Block 1555]
སོ་སོར་བཤགས་པར་བྱ་བའི་མཐའ་ཅན་གྱི་ལྟུང་བ་རྣམས་ནི་མདོ་འདི་རྣམས་ལ་མ་བརྗོད་པ་ལྟུང་བ་རྒྱས་པར་བཤད་པ་སོ་སོར་ཐར་པའི་མདོ་ལ་གནས་པ་ལ་ལྟོས་ནས་ལྟུང་བ་འདི་གང་ཡིན་ཞེས་བྱ་བའི་མཚན་ཉིད་སྟོན་པར་རིག་པར་བྱ་སྟེ། དེ་ལ་མི་ཚངས་པར་སྤྱོད་པའི་ཕམ་པར་གྱུར་པ་གང་ཞེ་ན། དེའི་ཕྱིར་བཅུག་རེག་ཉམས་སུ་མྱོང་བར་བྱས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཅུག་པའི་རེག་པ་ཉམས་སུ་མྱོང་བར་བྱས་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1556]
བཅུག་པ༌[^1084]དང་འབྲེལ་བ་དང་ཡང་ཚིག་གིས་ནི་བཅུག་པ་མེད་པར་ལྟུང་བ་སྐྱེད་པ༌[^1085]མ་ཡིན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 1557]
གང་དུ་བཅུག་པ་འདི་དེ་ལ་བཅུག་པའི་ཆ་དང་ཡང་དག་པར་ལྡན་པའི་ཕྱོགས་ཀྱིས་རེག་པ་གང་ཞིག་དེ་ལ་ཉམས་སུ་མྱོང་བར་བྱས་པ་ལ་དགེ་སློང་མ་ཕམ་པར་བྱེད་པ༌[^1086]ལ་མཚན་ཉིད་འདིའོ། །

[Block 1558]
དགེ་སློང་མ༌[^1087]བརྟེན་པ་ཉིད་ཀྱིས་ཉེ་བར་མཁོ་བ༌[^1088]ལ་རེག་པར་བྱ་བ་ལ་རེག་པ་གཅིག་གང་ཞིག་དེ་དང་ཡང་དག་པར་ལྡན་པས་འདི་བརྗོད་པས་ཉམས་སུ་མྱོང་བར་བྱས་ན་ཞེས་བྱ་བའི་ཚུལ་རྟོགས་པར་བྱའོ། །

[Block 1559]
འདིར་ཡང་སྙོམས་པར་འཇུག་པ་གཉིས་ལས་སྒྲ་གཅིག་ལ་འཇུག་པ་ཡང་དག་པར་འབྱུང་བ་ཡོད་པ་ཡིན་ཏེ། དེ་བས་ན་མདོ་འདི་ལ་ཡང་བལྟབས་པར༌[^1089]རྟོགས་པར་བྱའོ། །ཅི་ཞིག་བཅུག་པ་ཞེ་ན། དེའི་ཕྱིར། ཟག་བྱེད་དོ་ཞེས་སྨོས་ཏེ། སྐྱེས་པ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 1560]
འདོད་ཆགས་དང་བྲལ་བ་རྗེས་སུ་མཐུན་པ་ཉིད་ཀྱི་ཕྱིར་སྒྲ་འདིས་གང་དུ་བསྟན་ཞེ་ན། དེའི་ཕྱིར་དེར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟག་བྱེད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1561]
འདིར་ཟག་བྱེད་ནི་མོའི་དབང་པོའོ། །

[Block 1562]
དེ་ཇི་ལྟ་བུ་ལས་ཤེ་ན། དེའི་ཕྱིར་མ་ཉམས་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མིའི་བུད་མེད་གསོན་པ་མ་ཉམས་པ་ལའོ་ཞེས་བྱ་བས་མ་ལུས་པ་ལ་བརྟེན་པ་ལ་འདིར་རབ་ཏུ་སྦྱར་རོ། །

[Block 1563]
དེར་དགོས་པ་མེད་པར་མོའི་དབང་པོ་དང་ཁའི་ནང་དུ༌[^1090]བརྩེགས་པ་ལ་བརྟེན་པའི་ཉམས་པ་ཉིད་ལས་དོན་གཞན་ལ་ཉམས་པ་ཉིད་ཅེས་བྱ་བར་རྣམ་པར་ཤེས་ནས་མོའི་དབང་པོ་དང་ཁའི་རྟེན་ཉེ་བར་བརྟགས་པ་ནི་ཁའམ་བཤང་བའི་ལམ་དུའོ་ཞེས་བྱ་བ་སྟེ། ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བ་ཐམས་ཅད་དུ་རང་གི་དང་གཞན་གྱི་དང་མོའི་དང་དུད་འགྲོའི་སྐྱེ་གནས་ལ་སོགས་པ་དང་འབྲེལ་བའི་བུད་མེད་ཀྱི་ཚོགས་ལ་དང་སྐྱེས་པའི་དང་མ་ནིང་ན་ཡང་མ་ཉམས་པ་ཞེས་བྱ་བ་འཇུག་པ་ཡིན་ནོ། །

[Block 1564]
ཉམས་པ་དག་ལ་ནི་སྦོམ་པོར་རོ༌[^1091]ཞེས་བྱ་བ་ནི་ཁ་དང་བཤང་བའི་ལམ་དང༌[^1092]མོའི་དབང་པོ་ཉམས་པ་དག་ཏུ་བཅུག་པ་ལ་ནི་ཁ་ན་མ་ཐོ་བ་སྦོམ་པོར་འགྱུར༌[^1093]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1565]
མི་རུང་བ་ཉིད་ནི་ན་སྨད་དོ་ཞེས་བྱ་བ་ནི་ཡན་ལག་ཐམས་ཅད་ལ་རུང་བ་ཉིད་དེ་གཟུང་བ་དང་འགྲོ་བ་དང་བསྟེན་པ་ལ་རུང་བ་ཉིད་ཅེས་བྱ་བ་ངེས་པ་རྣམས་ལ་འཆད་པར་འགྱུར་བའོ། །

[Block 1566]
བགྲོད་པར་བྱ་བ་ཕོ་དང་མོ་དང་མ་ནིང་ནི་མི་རུང་བ་ཉིད་ལ་ན་སྨད་པ་སྟེ། རུང་བ་ཉིད་གང་ལ་རྩ་བ་དང་དེར་འདི་ལ་སྦོམ་པོའོ། །

[Block 1567]
གང་དུ་སྦོམ་པོ་དེར་ཉེས་བྱས་ཏེ། གང་དུ་ཉེས་བྱས་དེར་ཕྲ་མོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1568]
མི་མ་ཡིན་པའི་འགྲོ་བ་ཉིད་དང་སྐྱེས་པ་ཉིད་དང་མ་ནིང་ཉིད་དང་སྟེན་པར༌[^1094]བྱེད་པ་དང་། བསྟེན་པར་བྱ་བ་གཡོགས་མ་ཅན་དང་རོ་ཉིད་དག་ལ་ན་སྨད་པ་མེད་དོ། །

[Block 1569]
མ་ཚོར་བ་དང་རང་བཞིན་ཉམས་པའི་གནས་སྐབས་དང་མི་འདོད་བཞིན་དུ་བཅུག་པ་ཉིད་ནའོ། །

[Block 1570]
རང་གིས༌[^1095]བསྟེན་པར་བྱ་བར་རོ། །

[Block 1571]
སྔར་ཕྱི་རོལ་དུ་དྲུག་པ༌[^1096]ཉིད་ལའོ། །

[Block 1572]
ནང་དུ་མི་དབོ་བར་ཕྱི་རོལ་ཉིད་དུའོ་ཞེས་བྱ་བ་ལ། ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་མེད་པའི་དོན་མི་ཟད་པའི་དངོས་པོ་བསྡུ་བ་འདི་ཡིན་ནོ། །

[Block 1573]
མི་མ་ཡིན་པའི་འགྲོ་བ་པ་ཉིད་ལ་བགྲོད་པར་བྱ་བ་དང་། སྐྱེས་པ་ཉིད་ལ་སྐྱེས་པའི་དངོས་པོ་སྐྱེད་པ༌[^1097]ཉིད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1574]
མ་ནིང་ཉིད་ལ་བགྲོད་པར་བྱ་བ་དང་།

[Block 1575 [VERSE]]
སྟེན་པར༌[^1098]བྱེད་པ་ཕོའི་དབང་པོའོ། །
བསྟེན་པར་བྱ་བ་མོའི་དབང་པོ་དང་།
ཁ་དང་བཤང་བའི་ལམ་རྣམས་ལའོ། །

[Block 1576]
གཡོགས་མ༌[^1099]ཅན་ཉིད་ལ་ཞེས་བྱ་བ་ནི་གཡོགས་པ་ཉིད་ལའོ། །

[Block 1577]
རོ་ཉིད་དག་ལ་ཞེས་བྱ་བ་ནི་བགྲོད་པར་བྱ་བ་ལའོ།[^1100] །མ་ཚོར་བ་དང་ཞེས་བྱ་བ་ནི་གཉིད་ལོག་པ་ལ་སོགས་པ་ལ་བཅུག་པ་ཉིད་ལའོ། །

[Block 1578]
རང་བཞིན་ཉམས་པའི་གནས་སྐབས་དང་མི་འདོད་བཞིན་དུ་བཅུག་པ་ཉིད་ནའོ་ཞེས་བྱ་བའི་ཡུལ་གྱི་བདག་གི་བ་མེད་པ་ཉིད་ལའོ། །

[Block 1579]
སྔར་ཕྱི་རོལ་དུ་དྲུད་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་ནི་ཁ་དང་བཤང་བའི་ལམ་དག་ལ་ཕྱི་རོལ་ཏུ་དྲུད་པ་སྔོན་དུ་འགྲོ་བ་ཉིད་ཀྱིས་བཅུག་པ་ཉིད་ནའོ། །

[Block 1580]
ནང་དུ་མི་དབོ་བར་ཕྱི་རོལ་ཉིད་དུའོ་ཞེས་བྱ་བ་ལ། ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
