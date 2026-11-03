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
མིག་བགྲད༌[^833]བཞིན་ནི་འཛུམ་པ༌[^834]མཛེས་ཞེས་བྱ་བ་འདིས་ནི་ལུས་ཀྱི་ཁྲོ་གཉེར་དེའི་གཉེན་པོ་དགའ་བའི་མཚན་མ་ཉིད་བསྟན་ཏོ། །

[Block 1472]
ཡིད་འོང་རྣར་སྙན་ཚིག་གིས་དགའ་བར་བྱས་ནས་ནི། །ཞེས་བྱ་བ་ནི་ཚིག་རྩུབ་ཅིང་ཁྲོ་བའི་དངོས་པོ་དེའི་གཉེན་པོའི་ཚིག་ཕུན་སུམ་ཚོགས་པ་ཡང་བསྟན་ཏོ། །

[Block 1473]
དགའ་བས་ཚིམ་པར་གྱུར་ཞེས་བྱ་བ་འདིས་ནི་ཡིད་ཀྱི་རྣམ་པར་གྱུར་པའི་དངོས་པོ་དེའི་གཉེན་པོ་ཡིད་རབ་ཏུ་དགའ་བ་ཡང་བསྟན་ཏོ། །

[Block 1474]
ཡིད་རབ་ཏུ་དགའ་ནས་དེ་བཞིན་དུ་ཞེས་བྱ་བས༌[^835]ནི་ཇི་ལྟར་སྔ་མ་དེ་བཞིན་དུ་དེ་བྱེད་པར་བསྟན་ཏོ། །

[Block 1475]
སྦྱིན་པར༌[^836]འདོད་པའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་སྦྱོར་བ་འདོད་པ་ལ་ཞུམ་པ་མེད་པ་དང་ལྡན་པ་དེ་ཅིའི་ཕྱིར་ཞེ་ན། སྙིང་རྗེ་གོམས་པ་ལས་སྐྱེས་པས་སོ། །

[Block 1476]
འདོད་པ་ཙམ་གྱིས་འགྲུབ་པར་རིག་ནས་ཞེས་བྱ་བ་ལ། འདོད་པ་ཙམ་གྱིས༌[^837]དོན་གྲུབ་པར་རིག་པ་གང་ཡིན་པ་དེ་ནི་འདོད་པ་ཙམ་གྱིས་འགྲུབ་པར་རིག་པའོ། །

[Block 1477]
དོགས་པ་དང་འཇིགས་པ་སྐྱེས་ཏེ་ཞེས་བྱ་བ་འདིས་ནི་སྐྱེས་པའི་དོགས་པ་དང༌[^838]འཇིགས་པ་གང་ཡིན་པ་དེ་ནི་དོགས་པ་དང་འཇིགས་པ་སྐྱེས་པའོ། །

[Block 1478]
འཇིགས་པ་ནི་བདག་གི་དཔལ་འཕྲོག་པར་བྱེད་པས་སོ། །

[Block 1479]
དོགས་པ་ནི་ཅི་ཞིག་བསྟན་ནས་དཀའ་ཐུབ་སྤྱོད་པར་བྱད་པ༌[^839]ཞེས་པའོ། །

[Block 1480]
དེ་གཉི་གའི་རྒྱུ་དེ་དྲི་བར་གཉེན་དང་མཛའ་བཤེས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་སྨོས་ཏེ། འདིའི་དོན་ནི་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པའི་བཟོད་པ་དང་། སྦྱིན་པའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་མངོན་པར་སྤངས་ནས་ཅི་ཞིག་འདོད་པའི་ཕྱིར་དཀའ་ཐུབ་སྤྱོད་པར་བྱེད་ཅེས་བྱ་བའི་དྲི་བའི་སྐབས་འདི་ཡིན་ནོ། །

[Block 1481]
གཞན་བསླུ་བའི་དོགས་པ་ཤེས་ན་དྲི་བའི་ཚིག་གི་རྒྱུ་བསྟན་པའི་ཕྱིར། བདེ་བར་སྦྱོར་བའི་ལོངས་སྤྱོད་ཅེས་བྱ་བའི་ཚིགས་བཅད་འདི་ལྟ༌[^840]སྟེ། ཕྱེད་ཀྱིས་ནི་ཚིགས་བཅད་སྔ་མའི་ཕྱེད་ཉིད་ཀྱི་དོན་རྟོགས་པར་བྱའོ། །

[Block 1482]
ཚིགས་བཅད་འོག་མའི་ཕྱེད་ཀྱིས་ཀྱང་གོང་མའི་ཕྱེད་ཉིད་ཀྱི་དོན་བསྟན་ཏོ། །

[Block 1483]
གང་གི་ཡོན་ཏན་ཐོས་ནས་ཞེས་བྱ་བ་ནི་གང་ཐོས་ནས་དེ་སྤངས་པ་སྟེ། ཕུན་སུམ་ཚོགས་པ་དང་འདྲ་བའི་ཕུན་སུམ་ཚོགས་པ་ཚོགས་ཀྱི་ནང་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1484]
རྒུད་པ་ཞེས་བྱ་བ་ལ༌[^841]ལོངས་སྤྱོད་དང་ཤེས་པ་ལ་སོགས་པ་རྒུད་པའོ། །

[Block 1485]
སྐྱེ་བོ་དཀའ་ཐུབ་ཅན་དང་མཐུན་པ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བའི་སྐྱེ་བོ་དང་མཐུན་པ་སྟེ། འདིས་ནི་རབ་ཏུ་བྱུང་བ་རྣམས་ཀྱིས༌[^842]ངེས་པར་ལེགས་པར་སྒྲུབ་པ་དང་རྗེས་སུ་མཐུན་པར་བསྟན་ཏོ། །

[Block 1486]
སྲིད་པའི་བདེ་བ་ལ་མ་ཆགས་པ་དང་ཞེས་བྱ་བ་ནི་འོག་ནས་བསྟན་པའི་ཚིགས་བཅད་གང་གིས་སྦྱིན་པ་ལ་སོགས་པ་དེ་དག་ལ་ཆགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1487]
སློང་བ་ཉིད་སྡུག་བསྔལ་དུ་རིག་ཅིང་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ཆགས་པས་ནི་སློང་བར་གྱུར་ལ། སློང་བས༌[^843]ནི་ཆགས་པར་འགྱུར་རོ། །

[Block 1488]
དེ་བས་ན་སློང་བ་སྤངས་པ་ནི་མཆོག་ཡིན་ནོ། །

[Block 1489]
ཆོག་ཤེས་པ་ལ་གོམས་པ་ཞེས་བྱ་བ་ནི་དཀའ་བས་རྙེད་པས་འཚོ་བ་གནས་པའི༌[^844]སྒྲུབ་པས་ཆོག་ཤེས་པའི་ཕྱིར་རོ། །

[Block 1490]
ཆུང་མ་ཡིད་དུ་འོང་དང་བུ་དང་དབང་བྱེད་དང་། །ཞེས་བྱ་བ་ནི་སེམས་ཅན་དུ་བསྟན་པའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་བསྟན་པའོ། །

[Block 1491]
ནོར་ནི་སྦྱིན་པ་ལས་བྱུང་བའི༌[^845]བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུའོ། །

[Block 1492]
ཉོན་མོངས་པ་དང་བྲལ་བ་ཐོབ་དཀའ་བ་ཉིད་ཅེས་བྱ་བ་ལ་ཉོན་མོངས་པའི་སྒྲ་ནི་ཞེ་སྡང་ཉིད་དེ། ཅིའི་ཕྱིར་དེ་བཟུང༌[^846]ཞེ་ན། ཆགས་པ་ལ་སོགས་པ་སྤྱིར་བསྟན་པ་ཡིན་ཡང་འདི་ནི་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱི་ནང་ན་ཐ་ཆད་ཡིན་ཏེ། བདག་དང་གཞན་གདུང་བར་བྱེད་པས་སོ། །

[Block 1493]
ནོར་ཡང་ཉམས་ཤིང་ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་གྱི་སེམས་ཅན་མ་ཡིན་པ་ལས་སོ། །

[Block 1494]
མདོག་བཟང་ཞེས་བྱ་བ་ནི་ནང་གི་མདོག་རྒུད་པའོ། །

[Block 1495]
གྲགས་པ༌[^847]ནི་སེམས་ཅན་གཞན་གྱི་དད་པ་རྒུད་པའོ། །

[Block 1496]
བདེ་བ་ལས་ཀྱང་ཞེས་བྱ་བ་ནི་བསམ་པ་དང་ཕན་འདོགས་པ་ཉམས་པའོ། །

[Block 1497]
ཕོངས་པར་གྱུར་ལ་ཞེས་བྱ་བྱ་བ་བསྟན་པ་ལ་ཕོངས་པ་དེ་བསྒྲུབ་པའི༌[^848]ཕྱིར་ཕོངས་པའི་གནས་སུ་གྱུར་པའི་ཕྱིར་ཞེས་བྱ་བ་འདིའི་དོན་ནོ། །

[Block 1498]
བྱིས་པ་ཐ་མ་ཡིན་པར་འདོད་ཅེས་བྱ་བ་ནི་ཕོངས་པ་ཐམས་ཅད་ཀྱི་ནང་ན་ཁྱད་པར་དུ་སྙིང་རྗེའི་གནས་སུ་གྱུར་པ་ཞེས་བྱ་བ་ཡིན་ཏེ། བྱིས་པ་ནི་ཕོངས་པ་ཐམས་ཅད་ཀྱི་གནས་སུ་གྱུར་པའི་ཕྱིར་ཁྱད་པར་དུ་སྙིང་རྗེའི་གནས་སུ་གྱུར་པ་ཡིན་ནོ། །

[Block 1499]
མཐོང་བ་ཙམ༌[^849]དུའང་མི་འདོད་པ་ཉིད་ནི་ལྷན་ཅིག་གནས་པ་དང་ཕེབས་པར་སྨྲ་བ་ལྟ་ཅི་སྨོས་ཞེས་པའོ། །

[Block 1500]
འདི་དག་ཚུལ་མིན་པ་ཡང་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས༌[^850]པའི་དན་ནི་བདག་ལ་ཕན་པའི་ཁྱད་པར་མི་བྱེད་ཅིང་གཞན་གྱི་ཁ་ན་མ་ཐོ་བ་དང་སླུ་བར་བྱེད་པ་ཡང་བསྟན་ཏོ། །

[Block 1501]
བདག་ཉིད་ཀྱང་ཕན་པ་མ་ཡིན་པ་དང་། ལུགས་མ་ཡིན་པ་སྒྲུབ་པར་བྱེད་ལ། དེ་ལ་སྨས་པའི་ཕྱིར་གཞན་ཡང་རབ་ཏུ་སྦྱོར་བར་འདོད་དེ། ཁྱད་པར་སྒྲུབ་པར་མི་བྱེད་པ་དང་ཕན་པ་སྒྲུབ་པར་མི་བྱེད་པ་ཉིད་དོ། །

[Block 1502]
མཁས་པའི་ང་རྒྱལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་འདི་དག་ཚུལ་མིན་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྒྲུབ་པ་ཡིན་ཏེ། མཁས་པའི་ང་རྒྱལ་དང་གཏི་མུག་ནི་མཁས་པའི་ང་རྒྱལ་གཏི་མུག་དག་གོ། །

[Block 1503]
ཡང་ན་མཁས་པའི་ང་རྒྱལ་ཉིད་གཏི་མུག་སྟེ་མཁས་པའི་ང་རྒྱལ་གཏི་མུག་གོ། །

[Block 1504]
བདག་གི་རང་བཞིན་ང་རྒྱལ་གྱི་གཏི་མུག་གིས་བསྒྲིབས་པ་ཡིན་ཏེ། དེས་ཚུལ་མ་ཡིན་པ་ལ་ཚུལ་བཞིན་དུ་སྒྲུབ་པར་བྱེད་ལ། གཞན་ཡང་འདི་ལ་རབ་ཏུ་སྦྱོར་བར་འདོད་དོ། །

[Block 1505]
འདིར༌[^851]ཕན་པར་སྨྲ་ལའང་ཁྲོ་བས་རྩུབ་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་དག་ནི་ཕན་པ་ཡིན་ན་ཡང་ཕན་པ་མ་ཡིན༌[^852]བཞིན་དུ་རབ་ཏུ་ཁྲོ་བར་བྱེད་དོ། །

[Block 1506]
དྲང་པོའི་རིམ་པ༌[^853]མི་མཐུན་བ་ཞེས་བྱ་བ་ཅིའི་ཕྱིར་ཞེ་ན། གཟུ་ལུམས་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1507]
འདུལ་བ་དང་མི་མཐུན་པ༌[^854]ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1508 [VERSE]]
འདུལ་བ་ལ་བརྩོན་འགྲུས་ཆུང་ཞེས་པའི་ཕྱིར་རོ། །
མཁས་པའི་ང་རྒྱལ་གཏི་མུག་མེས་བསྲེགས་ཤིང་། །

[Block 1509]
ཞེས་བྱ་བ་ནི་བདག་ཉིད་གཞན༌[^855]གྱི་ཐད་དུ་སོང་ནས་ཕན་པའི་དྲི་བའི་ཚིག་སྒྲུབ་པ་མེད་པའི་ཕྱིར་ཏེ། དེས་ན་དེ་ཉིད་ཀྱིས་བདག་ཀྱང་ལོག་པར་སྒྲུབ་པར་བྱེད་ལ། གཞན་ཡང་དེ་ལ་སྦྱོར་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 1510]
བརྟན་པ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །
--- END BLOCKS ---
