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
[Block 1506]
ཡང་ན་རིམ་པ་ལྔ་སྟེ་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་ནི་ངག་རྣམ་པར་དག་པའི་ཕྱིར་རོ། །

[Block 1507]
སེམས་རྣམ་པར་དག་པ་ནི་སེམས་ལ་དམིགས་པའི་རིམ་པས་སོ། །

[Block 1508]
ཀུན་རྫོབ་ཀྱི་བདེན་པ་རྣམ་པར་དག་པ་ནི་རང་བྱིན་གྱིས་རློབ་པས་སོ། །

[Block 1509]
དོན་དམ་པའི་བདེན་པ་རྣམ་པར་དག་པ་ནི་མངོན་པར་བྱང་ཆུབ་པས་སོ། །

[Block 1510]
མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་སུ་འཇུག་པ་ནི༌[^1068]ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གྱི་རིམ་པས་སོ། །

[Block 1511]
སེམས་དཔའ་གཉིས་ནི་ཡེ་ཤེས་སེམས་དཔའི་ས་བོན་གྱི་ཐིག་ལེར་འཇུག་པར་བྱ་སྟེ། དེ་ཙམ་གྱི་ང་རྒྱལ་ལ་གནས་པའི་རིམ་པས་སོ། །

[Block 1512]
རིལ་པོར་འཛིན་པ་དང་རྗེས་སུ་གཞིག་པའི་ཏིང་ངེ་འཛིན་གྱིས་རང་བཞིན་དང་གཞན་གྱི་རྒྱུད་ལ་གནས་པའི་ལུས་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ་བཀག་པའི་སྒོ་ནས་སོ། །

[Block 1513]
དེ་དང་འདྲ་བ་གཞན་ཡང་རྫོགས་པའི་རིམ་པའི་ཏིང་ངེ་འཛིན་འོག་ནས་འཆད་པར་འགྱུར་བ་དང་། རྩ་ཡང་དག་པར་རྒྱུ་བ༌[^1069]ལ་སོགས་པ་གང་ཡིན་པ་དང་། དེ་དག་ཐམས་ཅད་རིམ་པ་ལྔ་པོར་འདུས་པར་རིག་པར་བྱའོ། །

[Block 1514]
རྣལ་འབྱོར་ཆེན་པོའི་ཕྱོགས་འདི་གང་ཟག་ལྔ་འདུལ་བའི་ཡུལ་ཅན་གང་ཡིན་པ་དེའི་དབྱེ་བས༌[^1070]འོག་ནས་ཀྱང༌[^1071]འཆད་པར་འགྱུར་རོ། །

[Block 1515]
[^1072]

[Block 1516]
ད་ནི་འདི་ལྟར་དཔྱད་པར་བྱ་སྟེ། བཅོམ་ལྡན་འདས་ཀྱིས་གང་གསུངས་པ་དེ་དག་ལས་བསྐྱེད་པའི་རིམ་པ་སྒོམ་པ༌[^1073]པོའི་གང་ཟག་གང་ཞེ་ན། སྨྲས་པ། དབང་པོ་དམན་པ་དང་བར་མ༌[^1074]དང་། རབ་ནི་ཙནྡན་ལ་སོགས་པའོ། །

[Block 1517]
དེའི་ཕྱིར་དེ་དག་ཚོགས་ལ་བཤད་པ་ལ་སྣོད་ཡིན་ནོ། །

[Block 1518]
བསྐྱེད་པའི་རིམ་པ་ཞེས་བྱ་བ་ནི་རྟོག་པའི་རྣལ་འབྱོར་རོ། །

[Block 1519]
ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ཐ་མལ་པ་སྤངས་ཏེ།[^1075] དེ་བཞིན་ཉིད་དང་ཕྱག་མཚན་དང་ས་བོན་ལས་སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པས་ཕྱག་རྒྱ་བསྒོམ་པ་ཡིན་ནོ། །

[Block 1520]
དེ་བས་ན་སྤྲོས་པས་བསྒྲུབ་པའི་ཕྱིར་རྣལ་འབྱོར་པ་ས་བརྒྱད་པ་ལ་གནས་པར་གྱུར་ནས་དེའི་འོག་ཏུ་དད་པ་ལ་སོགས་པའི་ཆོས་ལ་མཐར་ཕྱིན་པས་དེ་རྣམས་ཁོ་ན་དབང་པོ་རྣོ་བར་འགྲོ་བས་ན༌[^1076]རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཟག་ཏུ་འགྱུར་རོ། །

[Block 1521]
ལ་ལ་ན་རེ་གསེར་ཁུང་ལྟ་བུའི་ཐ་དད་པའི་རིགས་ཙནྡན་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 1522]
དེའི་ཕྱིར་གང་བསྐྱེད་པའི་རིམ་པ་སྒོམ་པ་པོ་དེ་དག་དེའི་རིགས་ཅན་ཁོ་ནའོ། །

[Block 1523]
གང་རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཟག་གང་ཡིན་པ་དེ་རྣམས་ཐ་དད་པ་སྟེ། རྫོགས་པའི་རིམ་པའི་སྒོམ་པ་པོ་ཁོ་ནའོ། །

[Block 1524]
དེ་བས་ན་དེ་རྣམས་ཀྱིས༌[^1077]བསྐྱེད་པའི་རིམ་པ་མ་བསྒོམས་པས་ཀྱང་རྫོགས་པའི་རིམ་པ་གཅིག་པུ་སྒོམ་པ༌[^1078]ལ་དབང་བ་སྟེ། བསྐྱེད་པའི་རིམ་པ་ཚེ་སྔ་མ་ལ་གོམས་པའི་ཕྱིར་ཞེས་སྐྱོན་མེད་དོ། །

[Block 1525]
ཇི་སྐད་དུ།

[Block 1526 [VERSE]]
བསྐྱེད་པའི་རིམ་ལ་ལེགས་གནས་ཤིང་། །
རྫོགས་པའི་རིམ་པ་འདོད་རྣམས་ལ། །
ཐབས་འདི་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས། །
སྐས་ཀྱི་རིམ་པ་ལྟ་བུར་གསུངས།[^1079] །

[Block 1527]
ཞེས༌[^1080]གསུངས་པའོ། །

[Block 1528]
དེ་ལ་གལ་ཏེ་བཅོམ་ལྡན་འདས་ཀྱི་གསུང་གི༌[^1081]ངོ་བོ་མི་བཟོད་ནས་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་ཕྱག་རྒྱ་ལ་དམིགས་ཏེ་རིམ་པ་ལ་བསླབ་པར༌[^1082]བྱའོ། །

[Block 1529]
ཡང་ན་མེད་ན་དེའི་ཚེ་སྔ་མ་བཞིན་དུ་རྫོགས་པའི་རིམ་པ་ཉིད་བསྒོམ་པར་བྱའོ། །

[Block 1530]
གོམས་པའི་རིམ་པས་ཅི་ཞིག་བྱ་ཞེས་གང་གསུངས་པ་དེ་ནི་རྫོགས་པའི་རིམ་པའི་གོ་རིམས་ལ་སློབ་པའི་ཕྱིར་ཡིན་གྱི། བསྐྱེད་པའི་རིམ་པ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་སྐྱོན་གང་ཡང་མེད་དེ། [^1083]དེ་ལ་འདི་ལྟར་དཔྱད་པར༌[^1084]བྱ་སྟེ། རྫོགས་པའི་རིམ་པ་གཙོར་གྱུར་པ་རིམ་པ་ལྔ་པོ་ཡིན་ན་དེའི་ཚེ་རིམ་པའི་གྲངས་ཀྱིས་རྣལ་འབྱོར་པའི་རིམ་པ་ལྔ་པོ་ཡིན་ནམ་གཅིག་ཡིན་ཞེ་ན། གལ་ཏེ་གཅིག་ཡིན་ན་དེའི་ཚེ་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་ཉིད་ཀྱིས་བྱ་བ་བྱས་པའི་ཕྱིར་རིམ་པ་གཞན་གྱིས་ཅི་ཞིག་བྱ། དེ་ལ་ཡང་མ་ནིང་གི་བཟླས་པ༌[^1085]ལ་སོགས་པའི་སྐབས་སུ་འོད་གསལ་བ་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1531]
ལྔ་ཡིན་ན་ནི་དེའི་ཚེ་རེ་རེ་དག་ལ་ངག་རྣམ༌[^1086]པར་དབེན་པ་ལ་སོགས་པ་ཡིན་གྱི་སེམས་རྣམ་པར་དག་པ་ལ་སོགས་པ་མ་ཡིན་ནོ། །

[Block 1532]
དེ་བཞིན་དུ་གཞན་དག་གིའོ། །

[Block 1533]
སྨྲས་པ། རྣལ་འབྱོར་པ་གཅིག་པ་ཡིན་གྱི་ལྔ་ནི་མ་ཡིན་ནོ། །

[Block 1534]
གང་གི་ཕྱིར་བསྐྱེད་པའི་རིམ་པས་ཏིང་ངེ་འཛིན་གསུམ་པོ་དེ་ཉིད་ལ་དམིགས་ཏེ། རིགས་བརྒྱའི་དབྱེ་བས་ལུས་རྣམ་པར་དབེན་པ་ལ་འཇུག་གོ། །

[Block 1535]
དེའི་རྗེས་སུ་ཡི་གེ་གསུམ་འཇུག་པ་ལ་སོགས་པའི་རིམ་གྱིས་རྡོ་རྗེའི་བཟླས་པ་ལ་གོམས་པས་ངག་རྣམ་པར་དབེན་པ་ལ་འཇུག་གོ། །

[Block 1536]
དེའི་འོག་ཏུ་སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་གསུམ་རྣམ་པར་དག་པས་དེ་རྫོགས་པ་ན་སེམས་རྣམ་པར་དབེན་པ་ལ་འཇུག་གོ། །

[Block 1537]
རང་བྱིན་གྱིས་རློབ་པའི་རིམ་པས་ཀུན་རྫོབ་ཀྱི་བདེན་པ་མཐོང་བ་ལ་འཇུག་གོ། །

[Block 1538]
མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པས་འོད་གསལ་བ་ལ་འཇུག་གོ། །

[Block 1539]
ཟུང༌[^1087]དུ་འཇུག་པའི་རིམ་པས་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་སུ་འཇུག་གོ། །

[Block 1540]
དེའི་ཕྱིར་སངས་རྒྱས་ཉིད་རིམ་གྱིས་རྙེད་པ་ཡིན་པས༌[^1088]རྣལ་འབྱོར་པ་གཅིག་རྡོ་རྗེའི་བཟླས་པ་གཅིག་པུའམ་གང་ཡང་རུང་སྟེ་གཅིག་གིས་མི་འགྲུབ་པོ། །དེའི་ཕྱིར་ཙནྡན་ལ་སོགས་པ་ལྟ་བུའམ་རིན་པོ་ཆེ་ལྟ་བུའི་རྣལ་འབྱོར་པས་རིམ་པ་ལྔ་ཆར༌[^1089]བསྒོམ་པར་བྱའོ། །

[Block 1541]
དེ་ལྟ་ན་པདྨ་ལྟ་བུ་ལ་སོགས་པའི༌[^1090]བསྐྱེད་པའི་རིམ་པ་གཅིག་པུའི་སྣོད་ཡིན་པས་རྫོགས་པའི་རིམ་པ་ལྔ་པོའི༌[^1091]ཕྱིར་སྒོམ་པར་བྱེད་ཅེ་ན། སྨྲས་པ། དྲང་བའི་དོན་དུ་ཡང་རྫོགས་པའི་རིམ་པ་གསུངས་པས་ཀུན་གྱིས༌[^1092]བསྒོམ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1542]
དེ་བས་ན་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་གཞན་དུ་གསུངས་ཏེ།

[Block 1543]
དེ་སྐད་དུ་སྤྱོད་པ་བསྡུས་པའི་སྒྲོན་མ་ལས།

[Block 1544]
རྡོ་རྗེ་སློབ་མས་གསོལ་བ། བདག་ཅག་ལྟ་བུའི་སོ་སོའི་སྐྱེ་བོ་ཐོག་མ་མེད་པ་ནས་ཕྱི་རོལ་གྱི་དངོས་པོ་རྣམ་པ་སྣ་ཚོགས་པ་ལ་མངོན་པར་ཞེན་པས་ཡོད་པ་དང་མེད་པ་དང་གཅིག་པ་དང་དུ་མ་དང་། གཉིས་དང་གཉིས་མ་ཡིན་པ་དང་། ཡོད་པ་མ་ཡིན༌[^1093]མེད་པའང་མ་ཡིན་པ་རྟག་པ༌[^1094]དང་མི་རྟག་པ་ལ་སོགས་པའི་རང་བཞིན་གྱི་བག་ཆགས་ཀྱི་རྒྱུས་རྣམ་པར་རྟོག་པ་ལ་མངོན་པར་ཞེན་པ་ལ་མ༌[^1095]ཞུགས་པ་རྣམས་ཀྱིས་རྫོགས་པའི་རིམ་པའི་གོ་རིམས་ཀྱི༌[^1096]ཏིང་ངེ་འཛིན་ལ་སློབ་པ་ན། གོ་རིམས༌[^1097]ཇི་ལྟ་བ་བཞིན་དུ་བསླབ་པར་བགྱི་བའམ་ཡང་ན་བླ་མའི་མན་ངག་ཙམ་གྱིས་དེ་དག་སྐད་ཅིག་ཙམ་གྱིས་སོ་སོར་སྣང་བར་བགྱི། རྡོ་རྗེ་སློབ་དཔོན་གྱིས་སྨྲས་པ། རིམ་གྱིས་འཇུག་པ་ལ་སློབ་པར༌[^1098]བྱའི་ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །

[Block 1545]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ལང་ཀར་གཤེགས་པའི་མདོ་ལས་གསུངས་ཏེ། དེ་ནས་བཅོམ་ལྡན་འདས་ལ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བློ་གྲོས་ཆེན་པོས་རང་གི་སེམས་སྣང་བའི་རྒྱུད་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ཡང་གསོལ་བ་བཏབ་པ། བཅོམ་ལྡན་འདས་རང་གི་སེམས་སྣང་བའི་རྒྱུད་ཅིག་ཅར་རམ་རིམ་གྱིས་འཇུག་པས་སམ། ཇི་ལྟར་རྣམ་པར་དག་པར་གྱུར། [^1099]བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བློ་གྲོས་ཆེན་པོ་རང་གི་སེམས་སྣང་བའི་རྒྱུད་ནི་རིམ་གྱིས་འཇུག་པས་རྣམ་པར་དག་སྟེ་ཅིག་ཅར་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
