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
དེ་བཞིན་གཤེགས་པ་རྣམས་བྱུང་ཡང་རུང་མ་བྱུང་ཡང་རུང་ཞེས་བྱ་བ་ལ་སོགས་པས་ཆོས་གནས་པའི་མཚན་ཉིད་གསུངས་པའོ། །

[Block 1472]
མཚན་ཉིད་ཀྱི་དབྱིངས་ནི་མཚན་ཉིད༌[^1026]མེད་པའི་དབྱིངས་ཇི་ལྟ་བ་བཞིན་དུ་གནས་པ་ཉིད་དེ། [^1027]དེ་ནི་དེ་བཞིན་གཤེགས་པས་ཡང་དག་པར་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཞེས་བྱ་བ་ནི་མཚན་ཉིད་ཀྱི་རྣམ་པར་རྟོག་པ་ཐམས་ཅད་མེད་པའི་ཕྱིར་མཚན་ཉིད་མེད་པའི་དབྱིངས་ཞེས་བྱའོ། །

[Block 1473]
དེའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་དེ་བཞིན་གཤེགས་པ༌[^1028]ཞེས་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་དུ་ཐུགས་སུ་ཆུད་པའམ། དེ་བཞིན་ཉིད་ཐུགས་སུ་ཆུད་པ་ལ་ངེས་པའི་ཚིག་གིས་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱའོ། །

[Block 1474]
དེ་བཞིན་གཤེགས་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་དག་པར་རབ་ཏུ་བསྟན་པས་མཚན་ཉིད་ཐམས་ཅད་ཡང་དག་པར་རབ་ཏུ་མཁྱེན་ཞེས༌[^1029]བྱ་བ་ནི། ལྷའི་བུ་དག་སྟོང་པ་ཉིད་ཀྱང༌[^1030]མཚན་ཉིད་དང་མཚན་མ་མེད་པའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར། འདི་ནི་ཟབ་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྔར་སྨོས་པ་སྟོན་ཏོ། །

[Block 1475]
བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་ཀྱང་མཚན་ཉིད་ཐམས་ཅད་རབ་ཏུ་དབྱེ་བ་མཛད་དེ་ཞེས་བྱ་བ་ནི་དོན་དམ་པ་རྣམ་པར་མི་རྟོག་པ་དེ་ལྟ་བུ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་ཀྱང་སེམས་ཅན་རྣམས་ལ་ཕན་གདགས་པའི་ཕྱིར་ཀུན་རྫོབ་ཀྱི་མཚན་ཉིད་རྣམས་བཤད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1476]
གཟུགས་ནི་གཟུགས་སུ་རུང་བའི་མཚན་ཉིད་དེ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཀུན་རྫོབ་ཀྱི་མཚན་ཉིད་རྣམས་སྟོན་ཏོ། །

[Block 1477 [HEADING]]
###### བྱས་པ་གཟོ་ཞིང་བྱས་པ་ཚོར་བ། ^1-2-5-12-6-0

[Block 1478]
འདི་ལ་བྱས་པ་གཟོ་བ་དང་བྱས་པ་ཚོར་བ་ནི་བདག་གིས་འདི་བྱས་སོ། །

[Block 1479]
བདག་གིས་འདི་ཁས་བླངས་སོ་ཞེས་བྱ་བར་བདག་གིས་བྱས་པ་དང་། བསྒྲུབ་པར་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 1480]
མ་བྱས་པ་དང་འགྱུར་བ་མེད་པར༌[^1031]མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཞེས་བྱ་བ་ནི་སུས་ཀྱང་མ་བྱས་པའི་ཆོས་རྣམས་མ་བྱས་པའི་བདག་ཉིད་དུ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པའོ། །

[Block 1481]
འགྱུར་བ་མེད་པ་ནི་མི་འགྱུར་བ་མེད་པར་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཞེས་བྱ་བ་ནི་མི་འགྱུར་བའི་བདག་ཉིད་དུ་མཁྱེན་པའོ། །

[Block 1482]
ལུས་མེད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ལུས་མེད་པ་ཁོག་པ་མེད་པ་གཟུགས་མེད་པ་ཉིད་དོ། །

[Block 1483]
རབ་འབྱོར་དེ་ལྟར་ན་ལུས་མེད་ཅིང་ཁོག་པ༌[^1032]འདི་ནི་དེ་བཞིན་གཤེགས་པས་མ་བྱས་པ་མཁྱེན་པ་དང་། མ་བྱས་པ་རིག་པའོ་ཞེས་བྱ་བ་ནི་འདུས་མ་བྱས་ཀྱི༌[^1033]མཚན་ཉིད་མཁྱེན་པས་མ་བྱས་པ་མཁྱེན་པའོ། །

[Block 1484]
དོན་དམ་པར་འབྱུང་བ༌[^1034]མེད་པའི་མཐུས་ཡེ་ཤེས་བྱས་པ་མེད་པ་ཆོས་ཐམས་ཅད་ལ་ཞུགས་སོ༌[^1035]ཞེས་བྱ་བ་ལ་དོན་དམ་པ་བྱུང་བ་མེད་པའི་མཐུས་ཞེས་བྱ་བ་ནི་དོན་དམ་པ། མ་སྐྱེས་མ་བྱུང་བའི་དབང་གིས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1485]
དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ནི་ཡོངས་སུ་གྲུབ་པའི་ཆོས་ཀྱི་སྐུའི་མཚན་ཉིད་ཡིན་པས་མ་བྱས་པ་སྟེ། དེ་བས་ན་དེ་བཞིན་གཤེགས་པ་ནི་མ་བྱས་པ་མཁྱེན་པའོ་ཞེས་བྱ་བར་སྟོན་ཏོ། །

[Block 1486 [HEADING]]
###### ཆོས་ཐམས་ཅད་ཤེས་པ་པོ་མེད་ཅིང་མཐོང་བ་པོ་མེད་པར་སྟོན་པ། ^1-2-5-12-7-0

[Block 1487]
བཅོམ་ལྡན་འདས་གང་གི་ཚེ་ཆོས་ཐམས་ཅད་སྐྱེད་པ་པོ་མ་མཆིས་ཤིང་མཐོང་བ་པོ་མ་མཆིས་པ་ཞེས་བྱ་བ་ནི་མི་སྐྱེད༌[^1036]པས་ན་སྐྱེད་པ༌[^1037]པོ་མེད་པ་སྟེ། དེ་བས་ན་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྐྱེད་པའོ༌[^1038]ཞེས་བྱ་བ་ནི་མི་མཐོང་ངོ་།[^1039] །མཐོང་བར་མི་བྱེད་པས་མཐོང་བ་པོ་མེད་པ་སྟེ། དེ་བས་ན་འཇིག་རྟེན་སྟོན་པའོ་ཞེས་བྱ་བ་མི་མཐོང་ངོ༌[^1040]ཞེས་སྟོན་ཏོ། །

[Block 1488]
རབ་འབྱོར་དེ་དེ་བཞིན་ནོ༌[^1041]ཞེས་བྱ་བ་ལ་སོགས་པས་ཆོས་ཐམས་ཅད་སྟོང་པ་དང་། གསོ་བ་དང་གསོག་ཡིན་པའི་ཕྱིར་སྐྱེད་པ༌[^1042]པོ་མེད་པ་དང་། མཐོང་བ་པོ་མེད་པ་བདེན་མོད་ཀྱི། [^1043]དོན་འདི་ལྟ་བུ་ཤེས་པ་འཇིག་རྟེན་ན་སུ་ཡང་མེད་དེ། ངས་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ལ་བརྟན༌[^1044]ནས། དོན་ཇི་ལྟ་བ་བཞིན༌[^1045]དུ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཏེ། དེ་ལྟ་བས་ན་དེར༌[^1046]བསྐྱེད་པ་ཡིན་ཞིང་སྟོན་པ་ཡིན་ནོ་ཞེས་དེ་སྐད་སྟོན་ཏེ། འདི་ནི་བསྟོད་པའི་ཚིག་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1489 [HEADING]]
###### མ་མཐོང་བའི་ཆོས་ཐམས་ཅད་སྟོན་པ། ^1-2-5-12-8-0

[Block 1490]
གཟུགས་མཐོང་བ་མེད་པའི་ཕྱིར་སྟོན་པའོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་གཟུགས་ངས་མ་མཐོང་བ་དེའི་ཕྱིར་དེ་སྟོན་པའོ། །

[Block 1491]
གལ་ཏེ་གཟུགས་མཐོང་བར་གྱུར་ན་ནི་རབ་རིབ་ཅན་བཞིན་དུ་ཡང་དག་པ་མ་ཡིན་པའི་དོན་མཐོང་བས་དེ་སྟོན་པར་ཡང་མི་འགྱུར་རོ། །

[Block 1492]
རབ་འབྱོར་ནམ༌[^1047]གཟུགས་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་མི་འབྱུང་བའི་ཚེ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རབ་རིབ་ཅན་ལ་སྐྲ་ཤད་འཛིངས་པ་ལ་སོགས་པ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་འབྱུང་བ་དེ་ཕྱིས་མི་འབྱུང་བར་གྱུར་པ་དེ་ནས༌[^1048]མཐོང་བ་ཡོངས་སུ་དག་པ་ཞེས་བྱ་བར་འགྱུར་ཏེ། དེ་བཞིན་དུ་འདིར་ཡང་གཟུགས་ལ་སོགས་པ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་རྣམས་མི་འབྱུང་བའི་ཕྱིར་སྟོན་པ་ཞེས་བྱ་བའི་མིང་དུ་འགྱུར་རོ། །

[Block 1493 [HEADING]]
###### འཇིག་རྟེན་འདི་བསམ་གྱིས་མི་ཁྱབ་པར་སྟོན་པ། ^1-2-5-12-9-0

[Block 1494]
བསམ་གྱིས་མི་ཁྱབ་ཅེས་བྱ་བར་སྟོན་ཏོ༌[^1049]ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་རྟོག་གེའི་སྤྱོད་ཡུལ་ལས་ཡང་དག་པར་འདས་པའི་ཕྱིར་རོ། །

[Block 1495]
རབ་འབྱོར་གཟུགས་ནི་བསམ་གྱིས་མི་ཁྱབ། གཞལ་དུ་མེད། དཔག་ཏུ་མེད། གྲངས་མེད་ཅིང་མི་མཉམ་པ་དང་མཉམ་པ་སྟེ་སྣང་བ་མེད་པའོ་ཞེས་བྱ་བ་ནི་གཟུགས་ན༌[^1050]སྣང་བ་མེད་པ་སྟེ་ཅིའི་ཕྱིར་ཞེ་ན་ཀུན་བརྟགས་པའི་གཟུགས་ནི་རི་བོང་གི་རྭ་བཞིན་དུ་མེད་པའི་ཕྱིར་སྣང་བ་མེད་དོ། །

[Block 1496]
ཆོས་ཉིད་ཀྱི་གཟུགས་ནི་རྣམ་པར་ཤེས་པ་གང་གིས་ཀྱང་གཟུང་བར༌[^1051]མི་ནུས་པའི་ཕྱིར་སྣང་བ་མེད་དེ། གང་གི་ཕྱིར་དེ་ལྟར་སྣང་བ་མེད་པ་དེའི་ཕྱིར་བསམ་གྱིས་མི་ཁྱབ་ཅེས་བྱ་གཞལ་དུ་མེད་ཅེས་བྱ། དཔག་ཏུ་མེད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1497]
བསམ་གྱིས་མི་ཁྱབ་པ་ལ་སོགས་པ་བསྟན་པ་ནི་གཞུང་ལས་འབྱུང་བ་བཞིན་དུ་བརྡ་ཕྲད་སླའོ། །

[Block 1498]
དེ་ལ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བའི་ཆོས་རྣམས་ཀྱང་མི་དམིགས་སོ་ཞེས་བྱ་བ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བའི་ཆོས་རྣམས་ཀྱིས་གཟུང་དུ་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དེ་བས་ན་སྣང་བ་མེད་པ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1499 [HEADING]]
##### དོན་ཆེན་པོའི་སླད་དུ་ཉེ་བར་གནས་པ། ^1-2-5-13-0

[Block 1500]
ཅིའི་ཕྱིར་གནས་བརྟན་རབ་འབྱོར་དོན་ཆེན་པོའི་སླད་དུ་ཉེ་བར་གནས་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བཤད་ཟིན་པའི་སྐབས་ཡང་སླར་གླེངས་ཏེ་བསྟན་ཞེ་ན་འཁོར་བསྡུ་བའི་ཕྱིར་འདི་ཉིད་གླེངས་ནས་རྒྱ་ཆེར་སྤྲོ་བར་འདོད་པའི་ཕྱིར་ཡང་བསྟན་ཏེ། སྔར་ནི་སངས་རྒྱས་རྣམས་ཀྱི་སྔོན་གྱི་སྤྱོད་པ་ལ་ཕན་འདོགས་པ་ཡིན་པར་བསྟན་ཏོ། །

[Block 1501]
ད་ནི་སངས་རྒྱས་ཀྱི་བྱ་བ་བྱེད་དོ་ཞེས་བསྟན་པའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་གཟུགས་ལ་ཡོངས་སུ་འཛིན་པ་མེད་པ་དང་། མངོན་པར་ཞེན་པ་མེད་པར་ཉེ་བར་གནས་པའོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མཐོང་བས་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ལ་སྲེད་པས་ཡོངས་སུ་འཛིན་པ་དང་། ལྟ་བས་མངོན་པར་ཞེན་པ་མི་འབྱུང་བ་དེའི་ཕྱིར། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དེ་ཡོངས་སུ་འཛིན་པ་མེད་པ་དང་། མངོན་པར་ཞེན་པ་མེད་པར་ཉེ་བར་གནས་པའོ་ཞེས་བྱ་བའི་མིང་དུ་འགྱུར་ཏེ་དོན་ཆེན་པོ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 1502]
རབ་འབྱོར་ངས་ཀྱང་ཞེས་བྱ་བ་ནི་བདག་ཉིད་དབང་དུ་གྱུར་པར་གསུངས་པའོ། །

[Block 1503]
དད་པས་རྗེས་སུ་འབྲང་བ་དང་ཆོས་ཀྱི་རྗེས་སུ་འབྲང་བ་དང་། དགྲ་བཅོམ་པ་དང་རང་སངས་རྒྱས་ཀྱི་བར་གྱི་ཤེས་པ་དང་། སྤྲོས་པ༌[^1052]གང་ཡིན་པ་དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པའི་བཟོད་པའོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ཤེས་རབ་ནི་ཆེ་བར༌[^1053]བསྟན་ཏེ། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་དགྲ་བཅོམ་པའི་ལམ་གྱི་འབྲས་བུའི་ཤེས་པ་རྣམས་དང་ཉོན་མོངས་པ་ཐམས་ཅད་སྤངས་པ༌[^1054]རྣམས་ནི་ས་བརྒྱད་པ་ལ་ཞུགས་པའི༌[^1055]མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པ༌[^1056]ཙམ་ཉིད་ཀྱིས་མཐར་གཏུགས་པར་འགྱུར་ཏེ། དེ་དག་གི༌[^1057]ཤེས་པ་དང་སྤང་བ་ནི་བཟོད་པ་དེ་ལས་ལྷག་པ་མེད་དོ། །

[Block 1504]
དེ་ཕན་ཆད་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་རྣམ་པ་ཐམས་ཅད་དུ་ཉོན་མོངས་པ་མེད་པའོ། །

[Block 1505]
དེ་དག་ཤིན་ཏུ་ཡང་མི་རིང་བ་ཞིག་ཏུ་ཕྱིན་ནས་མི་སྣང་བར་གྱུར་ཏེ་ཞེས་བྱ་བ་ནི་བཤད་པ་འདིས་དེ་དག་གི༌[^1058]བྱ་བ་ཡོངས་སུ་རྫོགས་པར་བསྟན་ཏོ། །

[Block 1506 [HEADING]]
##### ཕུན་སུམ་ཚོགས་པའི་གང་ཟག་རྣམས་ཀྱི་སྐྱེ་བ་ཞུས་པ། ^1-2-5-14-0

[Block 1507]
དེ་ནས་གནས་བརྟན་རབ་འབྱོར་གྱིས་བཤད་པ་འདི་ལ་མོས་པ་ལ་སོགས་པ་ཕུན་སུམ་ཚོགས་པའི་གང་ཟག་རྣམས་གུས་པ་སྐྱེད་པའི༌[^1059]ཕྱིར་དེ་དག་གི་སྐྱེ་བ་ཞུས་པ། གང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་ཐོས་མ་ཐག་ཏུ་མོས་པར་འགྱུར་བ༌[^1060]དེ་གང་ནས་ཤི་འཕོས་ཏེ་འདིར་སྐྱེས་པར་གྱུར་པ་ལགས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1508 [HEADING]]
###### བྱང་ཆུབ་སེམས་དཔའ་དཀར་པོའི་ཕྱོགས་སུ་གཏོགས་པ་གསུམ། ^1-2-5-14-1-0

[Block 1509]
འདིར་ཡང་བྱང་ཆུབ་སེམས་དཔའ་དཀར་པོའི་ཕྱོགས་སུ་གཏོགས་པ་གསུམ་དང་ནག་པོའི་ཕྱོགས་སུ་གཏོགས་པ་གསུམ་བསྟན་ཏེ་མི་རྣམས་ཉིད་ཀྱི་ནང་ནས་ཤི་འཕོས་ཏེ་མི་རྣམས་ཉིད་ཀྱི༌[^1061]ནང་དུ་སྐྱེས་པ་ནི་དགེ་བ་སྟེ་གཅིག་གོ། །

[Block 1510]
སངས་རྒྱས་ཀྱི་ཞིང་གཞན་དག་ནས་ཤི་འཕོས་ཏེ་མི་རྣམས་ཀྱི་ནང་དུ་སྐྱེས་པ་ཡང་དགེ་བ་སྟེ་གཉིས་པའོ། །
--- END BLOCKS ---
