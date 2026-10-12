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
[Block 1051]
དགེ་བ་གང་ཞེ་ན་མ་ཆགས་པ་དང་སྙིང་རྗེ་ལ་སོགས་པ་དང་མཚུངས་པའི་སེམས་ཀྱིས་བསླང་བའི་ལུས་དང༌[^502]ངག་གི་ལས་ཏེ་གང༌[^503]ཉེས་པ་གང་ཞིག་དང་བྲལ་བར་འགྱུར་རོ། །

[Block 1052]
ཚིག་གསལ་བ་གང་ཞེ་ན། ལྕེ་ལ་ཉེས་པ་མེད་ཅིང་ལུས་ཡོངས་སུ་དར་བས་ཆེད་དུ་སྨྲས་པའོ། །

[Block 1053]
བདེན་པ་གང་ཞེ་ན་དངོས་པོ་དང་མཐུན་པའི་ཚིག་ཏུ་བརྗོད་པའོ། །

[Block 1054]
མི་བདེན་པ་གང་ཞེ་ན། དངོས་པོ་དང་མི་མཐུན་པར་སྨྲ་བའོ། །

[Block 1055]
ངེས་པ་གང་ཞེ་ན་སོམ་ཉི་རྣམ་པར་སྤངས་པའི་སེམས་པ་དང༌[^504]དེའི་ལས་སོ། །

[Block 1056]
ཉེ་བར་མི་ལེན་པ་གང་ཞེ་ན། དངོས་པོ་ཐམས་ཅད་བདག་གིར་བྱེད་པར་མི་འདོད་པའོ། །

[Block 1057]
སྦྱིན་པ་པོ་གང་ཞེ་ན་གང་གིས་རང་གི་སྡུག་པ་དང་མི་སྡུག་པ་ཐམས་ཅད་ཡོངས་སུ་གཏོང་ཞིང་འཛིན་པ་མེད་པའོ། །

[Block 1058]
སྐུལ་བ་གང་ཞེ་ན་ལེ་ལོ་ཅན་དག་ལ་ཀུན་དུ་སྤྲོ་བ་སྐྱེད་པའོ། །

[Block 1059]
དཔའ་བ་གང་ཞེ་ན་གང་གིས་གང་ཞིག་ཕམ་པར་བྱེད་པ་དང་དེར་སེམས་པ་འཇིགས་པ་དང་བྲལ་བའོ། །

[Block 1060]
ངོ་ཚ་མེད་པ་གང་ཞེ་ན་རིགས་དང་ཆོས་ཡོངས་སུ་སྤངས་ཏེ་ཚུལ་བཞིན་མ་ཡིན་པའི་ལས་བྱེད་པའོ། །

[Block 1061]
སྒྱུ་གང་ཞེ་ན། གཞན་སླུ༌[^505]བའོ། །

[Block 1062]
གདུག་པ་གང་ཞེ་ན། ཉོན་མོངས་པས་ཉེས་པ་མི་བརྗོད་པའོ། །

[Block 1063]
མི་སྲུན་པ་གང་ཞེ་ན་བཤགས་ཀྱང་མི་ཉན་པའོ། །

[Block 1064]
གྱ་གྱུ་ཆེ་བ་གང་ཞེ་ན་གང་གིས་གཡོ་བྱེད་པའོ། །

[Block 1065]
གཡོ་ཡང་དེའི་གནས་སྐབས་ཉིད་དོ། །

[Block 1066]
གང་འདི་དག་ལ་ཡང་གང༌[^506]གིས་སེམས་པའི་བྱེ་བྲག་དང་ཡུལ་གྱི་བྱེ་བྲག་གིས་དམན་པ་དང་། བར་མ་དང་ཆེན་པོ་ལ་སོགས་པ་གཞག་པར༌[^507]བྱའོ། །

[Block 1067]
གང་གིས་དེ་དང་ལྡན་པ་དེས་ཀྱང་དེར་འགྱུར་བ་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1068]
དེའི་མིང་ནི་ཐབས་ཞེས་བྱ་བ་སྟེ་གང་ཞིག་གང་ལ་ལྟོས་པ༌[^508]དེ་དང་གང་ཞིག་མཐུན་པར་སྣང་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1069]
སྣང་བ་མཆེད་པ་ཞེས་བྱ་བ་ཡང་རང་བཞིན་གྱིས་ཡོངས་སུ་མཆེད་པར་འགྱུར་བ་སྟེ། གང་ཞིག་གང་ལ་གང་དང་ལྷན་ཅིག་ཏུ་གནས་པར་འགྱུར་བ་ཉིད་དོ། །

[Block 1070]
ཡང་ན་རང་བཞིན་འཁྲུལ་པ་རགས་པར་སྣང་བ་སྟེ། གང་ཞིག་ཀུན་དུ་གང་ལ་གང་དུ་འབྱུང་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1071]
ཡང་ན་རླུང་གིས་ཀུན་དུ་བསྐྱོད་པ་ཉིད་དེ། གང་ཞིག་གང་གི་རླུང་གིས་གང་ལ་གང་ཀུན་དུ་མཆེད་པར་འགྱུར་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1072]
[^509]དེ་ནས་སྣང་བ་ཐོབ་པའི་དོན་བཤད་པ། །རིག་ཆེན་རང་ཉིད་རྩ་བ་སྟེ། །ཞེས་པ་གང་གིས་གང་ཞིག་ཡོངས་སུ་རིག་པར་འགྱུར་བ་སྟེ་དེ་ལས་བཟློག་པ་ནི་མ་རིག་པའོ། །

[Block 1073]
གང་ཞིག་གང་དང་མཐུན་པར་འགྱུར་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1074]
བདག་ཉིད་གང་ལ་གང་དུ༌[^510]གནས་པར་འགྱུར་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1075]
སྣང་བ་ནི་ཁོལ་བུར་གཡོའོ། །

[Block 1076]
སྣང་བ་མཆེད་པ་ནི་ཀུན་དུ་རྒྱས་སོ། །

[Block 1077]
ཐོབ་པ་ནི་ལོག་པ་ཉིད་དོ། །མ་རིག་པ་ལས་འདི་འབྱུང་འགྱུར། །ཞེས་པ་ནི་ཆགས་པ་བར་མ་དང་བརྗེད་ངས་པ་དང་། འཁྲུལ་པ་དང་། མི་སྨྲ་བ་དང་། སྐྱོ་བ་དང་། ལེ་ལོ་དང་། ཐེ་ཚོམ་དག༌[^511]སྟེ་གང་ཞིག་འདི་ལས་བྱུང་བ་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1078]
དེ་ལ་ཆགས་པ་བར་མ་གང་ཞེ་ན། །གང་གིས༌[^512]ཆགས་པ་མེད་པ་ཡང་མ་ཡིན་ལ་ཆགས་པ་ཆེན་པོ་ཡང་མ་ཡིན་པ་ཉིད་དེ་དམན་པའི་ཆགས་པའོ། །

[Block 1079]
བརྗེད༌[^513]ངས་པ་གང་ཞེ་ན་སེམས་ཀུན་དུ་འཁྲུགས་པས་དོན་དུ་མི་གཉེར་བ་ཉིད་དང་། ཀུན་དུ་གང་གིས་དྲན་པ་ཉམས་པར་གྱུར་པ་ཉིད་དེ༌[^514]མ་འདྲིས་པ་དང་། རབ་ཏུ་སུན་པ༌[^515]ལས་བྱུང་བ་ཉིད་དོ། །

[Block 1080]
འཁྲུལ་པ་གང་ཞེ་ན་གང་གིས་སེམས་རྣམ་པ་གཞན་ལ་གཞན་དུ་འདི༌[^516]འཛིན་པ་ལ་སོགས་པ་སྟེ་གང་གིས་གང་དང་མི་མཐུན་པར་འཛིན་པ་སྟེ། གང་གིས་དོགས་པ་དང་བཅས་པ་ལ་སོགས་པ་ལས་བྱུང་བའོ། །

[Block 1081]
མི་སྨྲ་བ་གང་ཞེ་ན། ངག་གི་ལས་སྤངས་པ་སྟེ་ཐ་སྙད་རྣམས་རབ་ཏུ་སྤངས་པ་ཉིད་དོ། །

[Block 1082]
སྐྱོ་བ་གང་ཞེ་ན་གང་གིས་གང་ལ་ཀུན་དུ་འཁྱུད་པ་ལ་སོགས་པ་སྟེ། སྐྱོ་བ་ཉིད་སྐྱོ་བས་དེ་དག་གིས༌[^517]ཆོས་དང་བྲལ་བ་ཉིད་དོ། །

[Block 1083]
ལེ་ལོ་གང་ཞེ་ན་གང་གིས་དོན་མེད་པའི་ལས་སྔོན་དུ་སོང་བས་གང་ལ་གང་དུ་གནས་པར་འགྱུར་བ་ལ་སོགས་པ་མི་བྱེད་པ་སྟེ་གོ་ཆ་མེད་པ་དང་། སྦྱོར་བ་དང་བྲལ་བ་དང་། ཀུན་དུ་འགོད་པ་དང་མི་འཇུག་པ་དང་ལྡོག་པ་ལ་སོགས་པའི་ཆོས་དང་བྲལ་བའོ། །

[Block 1084]
ཐེ་ཚོམ་གང་ཞེ་ན། ལམ་དང་འབྲས་བུ་ལ་སོགས་པ་ལ་གང་ཡིད་གཉིས་ཟ་བ་སྟེ༌[^518]གྲུབ་པ་མེད་པ་དང་སྤངས་པ་མེད་པ་དང་ཐོབ་པ་མེད་པ་དང་། མྱུར་དུ་བླ་ན༌[^519]མེད་པའི་གང་ཟག་ལ་བརྟེན་ནས་ཡིན་ནམ་མ་ཡིན་དུ་སྙམ་སེམས་པ་ལ་སོགས་པའི་སེམས་གཉིས་སུ་གྱུར་པ་ཉིད་དོ། །

[Block 1085]
འདི་དག་ཡོངས་སུ་འཕེལ་བ་དང་འགྲིབ་པར་བྱེད་པའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། གང་གིས་དེ་དག་འཕེལ་བ་དང་འགྲིབ་པར་ནུས་པ་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1086]
[^520]དེ་ནས་སྣང་བ་གསུམ་གྱི་གོ་རིམས༌[^521]གཏན་ལ་དབབ་པར་བྱ་བའི་ཕྱིར། གང་ཡང་རྣམ་ཤེས་གསུམ་དང་པོ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རྣམ་པར་ཤེས་པ་གསུམ་གྱི་དང་པོ་ནི་དེའི་མིང་ཅན་སྣང་བའོ། །

[Block 1087]
གཉིས་པ་སྣང་བ་མཆེད་པ༌[^522]སྟེ། །ཞེས་བྱ་བ་ནི་སྣང་བ་མཆེད་པ༌[^523]ནི་སྣང་བ་ལ་ལྟོས༌[^524]ནས་གཉིས་པའོ། །

[Block 1088]
དེ་ནི་སྟོང་པ་ཆེར་འགྲོ་ལ། །ཞེས་པ་ནི་སྣང་བ་ཐོབ་པ་ཉིད་དོ། །

[Block 1089]
གཉིས་སྔོན་དུ་འགྲོ་བའོ། །

[Block 1090]
དེ་ཡང་འོད་གསལ་བར་འགྲོའོ། །ཞེས་པ་ནི་དེས་ཐམས་ཅད་སྟོང་པ་འོད་གསལ་བ་ཐོབ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
