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
[Block 1611]
མཐོང་བ་ཉིད་ཀྱི་དུས་ནི་མཐོང་བའི་ཚེ་ཉེ་བར་གནས་པ་དེའི་དབང་དུ་བྱས་པའོ། །

[Block 1612]
བཟའ་བ་བསླངས་པ་ནི་ཟས་བླངས་པ་བྱས་པའོ། །

[Block 1613]
ཞིམ་པོ་ནི་ཤིན་ཏུ་གཡོས་ལེགས་པ་དང་ཞིམ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1614]
ཁྱེར༌[^910]ཏེ་འོངས་ན་ཡང་ཞེས་བྱ་བ་ནི་གུས་པ་དང་བཅས་པས་མདུན་དུ་འོངས་པའོ། །

[Block 1615]
སྟག་གཟིག༌[^911]རྩྭ་སྔོན་མི་འདོད་པ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་དཔེར་ན་རི་དགས་རྣམས་ལ་རྩྭ་སྔོན་པོ་ཤིན་ཏུ་ཞིམ་པ༌[^912]ཡིན་ཡང་སྟག་ལ་སོགས་པ་མངོན་པར་མི་འདོད་པ་ཡིན་ཏེ། རྒྱལ་པོ་ལ་འོས་པའི་རྩྭ་སྔོན་པོ་ལྟ་བུར་དེ་གནོད་སྦྱིན་རྣམས་ལ་མངོན་པར་མི་འདོད་བའི་ཕྱིར་རོ། །

[Block 1616]
འོ་ན་ཇི་ལྟ་བུ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་མཐུན་པ་སྒྲོགས་ཤིག་པའོ། །

[Block 1617]
བཙལ་ལོ་ཞེས་བྱ་བ་ནི་བཙལ་བར་བྱའོ་ཞེས་སོ། །

[Block 1618]
མི་ཤི་བའི་ཤ་དང་ཁྲག་ཡོངས་སུ་གཟུང་བའི༌[^913]ཕྱིར་ཏེ། གཞན་དུ་ན་ཁ་ཟས་དང་ཁྲག་བཏུང་བ་མེད་དོ། །

[Block 1619]
བརྟུལ་ཞུགས་ཉམས་པ་ཞེས་བྱ་བ་ནི་དམ་བཅའ་བའི་རྗེས་སུ་འགྲོ་བ་སྟེ། ངེས་པར་ཡང་དག་པར་སྦྱིན་དུ་གཞུག༌[^914]པའི་ཕྱིར་རོ། །

[Block 1620]
མཆེ་བ་ཡོངས་སུ་གཙིགས་ཤིང་ཁ་མཆུ་ཡོངས་སུ་བསྐྱོད་པ་གང་ཡིན་པ་དེ་དག་ནི་ཁ་ནས་མཆེ་བ་གཙིགས་པའོ། །

[Block 1621]
མི་སྡུག་ལ་འཇིགས་པ་ཞེས་བྱ་བ་ལ། མི་སྡུག་པ་ནི་མི་རྣམས་ལའོ། །

[Block 1622]
འཇིགས་པ་ནི་འཇིགས་པ་བསྐྱེད༌[^915]པའོ། །ཇི་ལྟར་ཞེ་ན། དེའི་རྣམ་པ་བསྟན་ཏེ། མཆེ་བ་གཙིགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་རྟགས་ཀྱིས་སོ། །

[Block 1623]
འབར་ཞིང་སེར་བ་ཞེས་བྱ་བ་ནི་མདོག་རྣམ་པར་བསྒྱུར་ཞིང་འཇིགས་སུ་རུང་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1624]
སྔོ༌[^916]ཞིང་ཞེས་བྱ་བ་ནི་དབྱིབས༌[^917]རྣམ་པར་གྱུར་པའོ། །

[Block 1625]
སྣ་ལེབ་ཅིང་མི་སྡུག་པ་དང་ཞེས་བྱ་བ་ནི་གང་མཐོང་ན་བལྟ་བར་མི་སྡུག་པ་ལ༌[^918]བ་ལང་གི་སྣ་ལྟ་བུ་གང་ཡིན་པའོ། །

[Block 1626]
སྣ་ལེབ་ཅེས་སྨོས་པས་ནི༌[^919]རྣམ་པར་འགྱུར་བའོ། །

[Block 1627]
[^920]མི་སྡུག་པ་ནི་འཇིགས་སུ་རུང་བའོ། །

[Block 1628]
མེ་འབར་བ་ལྟ་བུའི་སེར་བའི་སྐྲ་དང་ཁ་སྤུ་གང་ཡིན་པ་ནི་དེའོ། །

[Block 1629]
མདོག་མུན་པ་ལྟར་གནག་པ་དེ་ནི་ཆར་སྤྲིན་ལྟར་གནག༌[^921]པའོ། །

[Block 1630]
འབའ་ཞིག་སེམས་ཞེས་བྱ་བ་ནི་དེ་དག་འཆི་བར་འགྱུར་རོ་སྙམ་དུ་སེམས་པས་སློང་བ་ལས་གཞན་ཡིད་ལ་མི་བྱེད་བར་དེ་འབའ་ཞིག་སེམས་པའི་ཕྱིར་རོ། །

[Block 1631]
སྙིང་རྗེ་ཅན་ལ་འདི་ལྟ་བུ། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་སྟེ། གསུམ་པོ་འདིའི༌[^922]བསྡུས་པའི་དོན་ནི་བཀྲེས་པའི་སྡུག་བསྔལ་གསོ་བའི་ཁ་ཟས་རྙེད་དཀའ་བ་དེས་གནོད་པའི་སྡུག་བསྔལ་དང་། ཡང་ན་བཀྲེས་པའི་སྡུག་བསྔལ་བཟློག་པའི་ཁ་ཟས་རྙེད་ཀྱང་མི་དགེ་བ་བསགས་པའི་རྒྱུས༌[^923]སྡུག་བསྔལ་བ་སྟེ། རྣམ་པ་ཐམས་ཅད་དུ་སྡུག་བསྔལ་ཞིང་དེའི་འབྲས་བུ་ཡང་སྡུག་བསྔལ་བའི་དབང་དུ་བྱས་ནས་བསམ་པ་དག་པས་དེ་དག་ལ་སྙིང་རྗེ་དེ་བས་ཆེར་ཡང་གྱུར་ཞེས་བྱ་བ་བསྟན་ཏོ། །

[Block 1632]
འོན་ཏེ་སྙིང་རྗེ་དང་ལྡན་ཞིང་ནུས་པ་དང་ལྡན་པ་དེ་མེད་པའམ་ནུས་པ་མེད་པ་འདི་གཉིས་ཀྱིས་ནི་རེ་ཞིག་རྣམ་པ་ཐམས་ཅད་དུ་རྙེད་དཀའོ། །

[Block 1633]
ཉིན་རེ་བཞིན་ཡང་དེ་བཙལ་བས། །ཞེས་བྱ་བ་ནི་དུས་གཅིག་གི་ཚེ་རྙེད་ནས་བྱ་བ་བྱས་པར་གྱུར་པ་དེ་ལྟ་བུ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1634]
འདོད་པའི་དོན་ནི་མེད་པར་འགྱུར། །ཞེས་བྱ་བ་ནི་བཀྲེས་པའི་སྡུག་བསྔལ་གསོ་བའི་ཁ་ཟས་རྙེད་པའོ། །

[Block 1635]
དེ་ལྟ་བུའི་ཁ་ཟས་ཟ་བ་རྣམས་ཞེས་བྱ་བ་ནི་སྙིང་རྗེ་ཅན་ལ་དེ་ལྟ་བུའི་ཁ་ཟས་ཟ་བ་རྣམས༌[^924]ཀྱི་ཟས་ནི་རྙེད་པར་དཀའ་བའོ། །

[Block 1636]
སྙིང་རྗེ་མེད་ཅིང་ཡིད་ནི་མ་ཞི་བ། །ཞེས་བྱ་བ་ནི་སྙིང་རྗེས་སྟོང་པའི་ཕྱིར་མ་ཞི་ཞིང་མི་དགེ་བའི་ཡིད་གང་ཡིན་པ་དེ་དག་སྟེ། འདིས་ནི་མི་ནུས་ཀྱང་རྟག་ཏུ་དེའི་ཁ་ཟས་ཀྱི་རྣམ་པ་ལ་གནས་པའོ། །

[Block 1637]
ཚེ་འདི་དང་ནི༌[^925]ཕ་རོལ་རང༌[^926]དོན་སྲེག །ཅེས་བྱ་བ་ནི་སྙིང་རྗེའི་སྡུག་བསྔལ་བ་སྟེ། མཐོང་བའི་ཆོས་དང་འཇིག་རྟེན་ཕ་རོལ་གྱི་སྡུག་བསྔལ་ལོ། །

[Block 1638]
ཡང་ན་ཚིགས་བཅད་གསུམ་པས་ནི་སྔར་བཤད་པའི་རྣམ་པ་བཞིའི་དབང་དུ་བྱས་པ་སྟེ། སྙིང་རྗེ་དང་ལྡན་ཞིང་ནུས་པ་དང་། མི་ནུས་པའི་སྙིང་རྗེ་དང་ལྡན་པ་དང་། མི་ནུས་ཤིང་སྙིང་རྗེ་དང་བྲལ་བ་དང་། སྙིང་རྗེ་དང་མི་ལྡན་ཞིང་ནུས་པ་སྟེ་བཞི་པོ་དེ་དག་གི་དབང་དུ་བྱས་པའོ། །

[Block 1639]
དེ་ལྟ་བུའི་ཁ་ཟས་ཟ་བ་རྣམས་ཞེས་བྱ་བ་ནི་སྙིང་རྗེ་དང་ལྡན་ཞིང་མི་ནུས་པ་དང༌[^927]ནུས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 1640]
སྙིང་རྗེ་མེད་ཅིང་ཡིད་ནི་མ་ཞི་བ། །ཞེས་བྱ་བ་ནི་སྙིང་རྗེ་མེད་ཅིང་ནུས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 1641]
ཚེ་འདི་དང་ནི་ཕ་རོལ་རང་དོན་སྲེག །ཅེས་བྱ་བ་ནི་སྙིང་རྗེ་དང་བྲལ་ཞིང་མི་ནུས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 1642]
འདི་དག་སྡུག་བསྔལ་ནམ་ཞིག་མེད་པར༌[^928]འགྱུར། །ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་སམ་ཕྱི་མ་ལའོ། །

[Block 1643]
གཞན་གསོད་པ་ལ་ཞུགས་པ་འདི་ལས་ཇི་ལྟར་བཟློག་པར་བྱ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་སྲོག་གཅོད་པར་བྱེད་པ་ལས་བཟློག་པའོ། །

[Block 1644]
རེ་བ༌[^929]བཟློག་པ་ངོ་འཛུམ་གནག་གྱུར་པ། །ཞེས་བྱ་བ་ནི་རེ་བ་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་ཅིང་གཞན་དུ༌[^930]སྟེ། འདོད་པའི་གགས༌[^931]སུ་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1645]
རེ་བ་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པས་བཞིན་གྱི་མདོག་ཉམས་པར་བྱས་པ་གང་ཡིན་པ་དེ་ནི་རེ་བ་བཟློག་པས༌[^932]ངོ་འཛུམ་གནག་པར་གྱུར་པའོ། །

[Block 1646]
བུ་ཡུག་གིས་ཀུན་ཏུ་འདྲེས་པའི་རླུང་ནི་བུ་ཡུག་རླུང་ངོ་། །བུ་ཡུག་རླུང་གིས་རྙིས་པར་བྱས་པ་ནི་བུ་ཡུག་རླུང་གིས་རྙིས་པ༌[^933]སྟེ། དེ་ལྟ་བུའི་པདྨ་ནི་བུ་ཡུག་རླུང་གིས་རྙིས་པའི༌[^934]པདྨའོ། །

[Block 1647]
བརྟན་ཞིང་རྒྱས་པ་ཞེས་བྱ་བ་ལ་བརྟན་པ་དང་རྒྱས་པ་ནི་བརྟན་ཞིང་རྒྱས་པའོ། །

[Block 1648]
བརྟན་པའི་ཁྱད་པར་ནི་རྒྱས་པ་སྟེ་རྣམ་པ་གཉིས་སོ། །

[Block 1649]
ནད་ལ་སོགས་པས་རྒྱས་པར་གྱུར་པ་ནི་དེ་ལྟ་བུ་མ་ཡིན་ནོ། །

[Block 1650]
བདག་རང་ཤི་བ་ཞེས་བྱ་བ་ནི་མངོན་པར་འདོད་པའི་སྦྱིན་པ་མ་ཡིན་པའོ། །
--- END BLOCKS ---
