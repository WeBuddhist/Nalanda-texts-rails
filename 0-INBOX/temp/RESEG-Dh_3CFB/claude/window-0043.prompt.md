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
འབྲེལ་པ་ནི་ངག་རྣམས་དོན་གཅིག་ཏུ་སྡུག་པ༌[^1117]ལ་ཕན་འདོགས་པར་བྱེད་པའོ། །

[Block 1507]
དེ་ལྟར་མ་ཡིན་ན་སྨྲ་བ་པོ༌[^1118]མི་མཐུན་པ་སྟོན་པར་འགྱུར་ཏེ། སེའུ་བཅུ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ངག་དང་འདྲ་བར་བསྡུར་མེད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1508]
འབྲས་བུ་འདོད་པ་བསྟན་བཅོས་ཐབས་ནུས་པ་མེད་པ་ཅན་གྱི་འབྲས་བུ་ཅན་ལ་དཔྱོད་པར་བྱ་བའི་ཕྱིར་གུས་པར་མི་འགྱུར་ཞིང་། སྐྱེས་བུ་དོན་གྱི་འབྲས་བུ་མེད་པ་ཅན་དག་ལ་ཡང་སྟེ། དུག་ཞི་བར་བྱ་བའི་ཕྱིར་འཇོག་པའི་གཙུག་གི་རིན་པོ་ཆེའི་རྒྱན་གྱི་མན་ངག་ལྟ་བུ་དང་། བྱ་རོག་གི་སོ་ལ་བརྟགས༌[^1119]པ་ལྟ་བུའོ། །

[Block 1509]
དེ་བཟློག་ནས་སྡུད་པ་དང་ལྡན་པ་དང་ཐབས་ནུས་པ་ཅན་དང་། སྐྱེས་བུའི་དོན་རྗོད་པར་བྱེད་པའི་བསྟན་བཅོས་ནི་ཡོངས་སུ་བརྟག་པར་བྱ་བ་ཡིན་ཏེ། གཞན་ལ་གུས་པར་བྱ་བ་ཉིད་ནི་མི་རིགས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1510]
དེ་ནི་གལ་ཏེ་ཡོངས་སུ་བརྟགས་པ་ལ་སླུ་བ་བསྟན་པ༌[^1120]མེད་པ་དེ༌[^1121]ལ་འཇུག་པ་ན་མཛེས་པར་འགྱུར་རོ། །

[Block 1511]
འདིའི་མི་སླུ་བ་གང་ཞེ་ན། །མཐོང་དང་མ་མཐོང་དངོས་པོ་ཡི།[^1122] །

[Block 1512 [VERSE]]
དོན་དེ་དག་ལ་མངོན་སུམ་དང་། །
རྗེས་དཔག་རྣམ་པ་གཉིས་ཀྱིས་ཀྱང་། །
གནོད་མེད་འདི་ནི་མི་སླུ་བའོ། །

[Block 1513]
མངོན་སུམ་དུ་འདོད་པའི་དོན་དག་ལ་དེ་བཞིན་དུ་འགྱུར་བ་ནི་མངོན་སུམ་གྱིས་གནོད་པ་མེད་པ་སྟེ། དཔེར་ན་སྔོན་པོ་ལ་སོགས་པ་དང་བདེ་བ་དང་སྡུག་བསྔལ་བ༌[^1123]དང་རྒྱུ་མཚན་ཉེ་བར་མཚོན་པར་བྱེད་པ་དང་འདོད་ཆགས་ལ་སོགས་པ་དང་བློ་དག་ལྟ་བུའོ། །

[Block 1514]
དེ་ལྟར་མངོན་པར་འདོད་པ་མ་ཡིན་པ་དག་ཀྱང་མངོན་སུམ་ཉིད་མ་ཡིན་ཏེ། དཔེར་ན་སྐྲ་ལ་སོགས་པའི་ངོ་བོ་ཞེན་པ་ཅན་བདེ་བ་ལ་སོགས་པ་དག་དང་། རྫས་དང་ལས་དང་སྤྱི་དང་ལྡན་པ་ལ་སོགས་པ༌[^1124]དག་ལྟ་བུའོ། །

[Block 1515]
དེ་བཞིན་དུ་ལུང་ལ་ལྟོས་པ་མེད་པའི་རྗེས་སུ་དཔག་པའི་ཡུལ་དུ་འདོད་པ་དག་ལ་དེ་བཞིན་དུ་འགྱུར་ཏེ། དཔེར་ན་འཕགས་པའི་བདེན་པ་བཞི་དག་ལྟ་བུའོ། །

[Block 1516]
རྗེས་སུ་དཔག་པར་བྱ་བ་མ་ཡིན་པ་དེ་དག་ནི་དེ་ལྟར་འགྱུར་ཏེ། དཔེར་ན་བདག་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 1517]
ལུང་ལ་ལྟོས་པའི་རྗེས་སུ་དཔག་པ་ཡང་དཔེར་ན་འདོད་ཆགས་ལ་སོགས་པའི་ངོ་བོ་དང་དེ་ལས་བྱུང་བའི་ཆོས་མ་ཡིན་པར་ཁས་བླངས་ནས་དེ་སྤང་བའི༌[^1125]ཕྱིར་ཁྲུས་དང་མེ་ལ་སྦྱིན་སྲེག་ལ་སོགས་པ༌[^1126]མ་བསྟན་པ་ལྟ་བུའོ། །

[Block 1518]
ཡོངས་སུ་གཅོད་པར་ནུས་པའི་ཡུལ་མ་ལུས་པ་རྣམ་པར་དག་པ་དེ་ནི་མི་སླུ་བ༌[^1127]ཡིན་ནོ། །

[Block 1519 [VERSE]]
ཡིད་ཆེས་ཚིག་ནི་མི་སླུ༌[^1128]བ། །
སྤྱི་ལས་འདི་ཡི་ལྐོག་གྱུར་པའི། །
ཡུལ་ལ་འང་གོ་སྐབས་མེད་བློ་ནི། །
རྗེས་སུ་དཔག་པ་ཉིད་དུ་བརྗོད། །

[Block 1520]
དེ་དང་འདི་དེ་ལྟ་བུར་གྱུར་པའི་ཉེས་པ་ཟད་པའི་ཚིག་མི་སླུ་བར༌[^1129]མཚུངས་པའི་ཕྱིར་མ་མཐོང་བར་འཁྲུལ་པ་མེད་པ་ཅན་མངོན་སུམ་དང་རྗེས་སུ་དཔག་པ་དག་གིས་གོ་བ་མ་ཡིན་པའི་དོན་རྟོགས་པ་ནི་དེ་ལ་བརྟེན་པ་ཉིད་ཀྱི་ཕྱིར་དེ་ལས་གཞན་པའི་རྟོགས་པ་དང་འདྲ་བར་མི་སླུ་བར༌[^1130]རྗེས་སུ་དཔག༌[^1131]པར་བྱ་བ་ཡིན་ནོ། །

[Block 1521]
དེ་བས་ན་སྒྲས་རབ་ཏུ་ཕྱེ་བ་ཡིན་དུ་ཟིན་ཀྱང་སྒྲ་ལས་བྱུང་བ་དང་འདྲ་བར་བསམ་པ་ཉིད་སྟོན་པར་བྱེད་པ་ནི་མ་ཡིན་པ་དེ་ལྟར་ན་དོན་ལ་མི་སླུ་བའི༌[^1132]ཕྱིར་རྗེས་སུ་དཔག་པ་ཡང་ཡིན་ནོ། །

[Block 1522]
ཡང་ན་རྣམ་པ་གཞན་གྱིས་ཉེས་པ་ཟད་པའི་ཚིག་མི་སླུ་བ༌[^1133]ཡིན་པའི་ཕྱིར་རྗེས་སུ་དཔག་པ་ཉིད་དུ་བརྗོད་པར་བྱ་སྟེ།

[Block 1523 [VERSE]]
བླང་དང་དོར་བྱའི་དེ་ཉིད་ནི། །
ཐབས་བཅས་རབ་ཏུ་ངེས་པ་ཡིས། །
གཙོ་བོའི་དོན་ལ་མི་སླུའི༌[^1134]ཕྱིར། །
གཞན་ལའང་རྗེས་སུ་དཔག་པ་ཡིན། །

[Block 1524]
བླང་བར་བྱ་བ་དང༌[^1135]དོར་བར་བྱ་བ་དང་དེའི་ཐབས་དེས་བསྟན་པ་དག་ལ་ཕྱིན་ཅི་ལོག་མེད་པ་ནི་མི་སླུ་བ༌[^1136]ཡིན་ཏེ། དཔེར་ན་འཕགས་པའི་བདེན་པ་བཞི་པོ་འཆད་པར་འགྱུར་བའི་ཚུལ་ལྟ་བུའོ། །

[Block 1525]
སྐྱེས་བུའི་དོན་ལ་ཉེ་བར་མཁོ་བ་ཅན་གོམས་པར་འོས༌[^1137]པ་དེ་དང་འདིའི་མི་སླུ་བའི༌[^1138]ཡུལ་གཞན་ལ་ཡང་དེ་བཞིན་དུ་ཁས་བླང་བར་བྱའི་སླུ་བ༌[^1139]ནི་མ་ཡིན་ཏེ། འགལ་བ་མེད་པའི་ཕྱིར་དང་། འཆད་པ་པོ་དགོས་པ་མེད་པ་ལ་ལོག་པར་སྟོན་པ་ལ་འབྲས་བུ་མེད་པའི་ཕྱིར་རོ། །

[Block 1526]
དེ་དང་དེ་རྣམ་པ་གཉི་གས་ཀྱང་གོ་སྐབས་མེད་པས་ལུང་རྗེས་སུ་དཔག་པ་ཉིད་དུ་བརྗོད་པ་ཡིན་ནོ། །

[Block 1527]
ལུང་ལ་འཇུག་པ་ན་དེ་ལྟར་འཇུག་པར་བྱའོ། །

[Block 1528]
དེ་ལྟར་ན་རྗེས་སུ་དཔག་པ་ཡང་ཉེས་པ་མེད་པ་མ་ཡིན་ཏེ། སྒྲ་དག་ནི་དོན་རྣམས་ལ་མེད་ན་མི་འབྱུང་བ་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །ཞེས་བསྟན་ཟིན་ཏོ། །

[Block 1529 [VERSE]]
སྐྱེས་བུ་ཕུལ་བྱུང་ལ་ལྟོས་པ། །
ཇི་བཞིན་དོན་དུ་གཞན་གྱིས་ཤེས། །

[Block 1530]
དོན་ཇི་ལྟ་བ་བཞིན་དུ་མཐོང་བ་ལ་སོགས་པའི་ཡོན་ཏན་དང་ལྡན་པ་ནི་སྐྱེས་བུ་ཉེས་པ་ཟད་པ་སྟེ། དེས་བྱས་པ་ནི་མི་སླུ་བ༌[^1140]ཞེས་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་དག་གིའོ། །

[Block 1531 [VERSE]]
གལ་ཏེ་ཕུལ་དུ་བྱུང་བ་སྟེ། །
ཤེས་པར་ནུས་ན་དོན་འདི་འདོད། །

[Block 1532]
རྟོག་པ་སྔོན་དུ་གཏོང་བ་འཇུག་པར་འདོད་པ་ཅན་ཐམས་ཅད་ནི་ལུང་ངམ་ལུང་མ་ཡིན་པ་ཚོལ་བར་བྱེད་ཀྱི་ཕོངས་པས་ནི་མ་ཡིན་ནོ། །

[Block 1533]
ཇི་ལྟར་ཡང་འདི་ལས་ནན་ཏན་དུ་བྱས་ཤིང་ཤེས་ནས་འཇུག་པ་ན་དོན་དང་ལྡན་པར་འགྱུར་བ་དེ་ལྟར་མཐོང་བར་ནུས་པ་ཅན་ལ་སླུ་བ༌[^1141]མེད་པའི་རྐྱེན་གྱིས་དེ་གཞན་དག་ལ་ཡང་འཇུག་པར་འགྱུར་ཏེ། འཇིག་རྟེན་གྱི་ཐ་སྙད་ནི་དེ་ལྟར་ཕལ་ཆེ་བ་ཅན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1534]
སྐྱེས་བུ་ཡོངས་སུ་བརྟགས་ནས་འཇུག་པ་ན༌[^1142]མི་འཇུག་པ་ཁོ་ན་ཡིན་ཏེ། དེ་ལྟ་བུར་གྱུར་པ་དེ་ཤེས་པར་མི་ནུས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1535]
མི་འདོད་པའི་ཕྱིར་ནི་མ་ཡིན་ཏེ། དེ་འདྲ་བ་ནི་ཕྱིན་ཅི་མ་ལོག་པ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1536]
འདི་ལྟར།

[Block 1537 [VERSE]]
ཚད་མ་རྣམས་ནི་རྙེད་དགའི་ཕྱིར། །
འདི་ནི་འདི་ལྟའམ་མིན་ནོ་ཞེས། །
གཞན་ཉེས་པ་འམ་ཉེས་མེད་ཀྱང་།
རྟོགས་དཀའ་ཞེས་ནི་གཞན་གྱིས་ཤེས། །

[Block 1538]
སྐྱེས་བུ་དག་སེམས་ལས་བྱུང་བའི་ཡོན་ཏན་དང་སྐྱོན་དག་ལས་ཡང་དག་པ་དང་ལྡོག་པར༌[^1143]འཇུག་པ་ཅན་ཡིན་ན་དེ་ཡང་དབང་པོ་ལས་འདས་པ་དག་ཡིན་ཏེ། རང་ལས་བྱུང་བའི་ལུས་དང་ངག་གི་བྱ་བ་དང་སྨྲ་བས་རྗེས་སུ་དཔག་པར་བྱ་བ་དག་ཡིན་ན། ཐ་སྙད་ཀྱང་ཕལ་ཆེར་བློ་སྔོན་དུ་གཏོང་བས་རྣམ་པ་གཞན་དུ་ཡང་བྱ་བར་ནུས་ཏེ། སྐྱེས་བུའི་འདོད་པའི༌[^1144]འཇུག་པ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་དང་། དེ་དག་ཀྱང་བསམ་པ་སྣ་ཚོགས་པ༌[^1145]ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1539]
དེ་བས་ན་འདི་ནི་གཏན་ཚིགས་ཚོལ་བའི་ཕྱིར་ངེས་པ་མེད་པ་ཡིན་ན་ཇི་ལྟར་རྟོགས་པར་འགྱུར། ཅི་སྟེ་གང་ཉེས་པ་མེད་པ་དེ་འདྲ་བའི་སྐྱེས་བུ་ཅི་ཡོད་པ་མ་ཡིན་ནམ་ཞེ་ན།

[Block 1540 [VERSE]]
འགྲིབ་དང་ཕུལ་བྱུང་བརྟེན་པ་ཀུན། །
མི་མཐུན་ཕྱོགས་དང་བཅས་ཉིད་ཕྱིར། །
དེ་གོམས་པ་ལས་བདག་གྱུར་པས། །
ལ་ལར༌[^1146]ཟག་པ་ཟད་པར་འགྱུར། །

[Block 1541]
ཟག་པ་ཟད་པ་དེ་ཡང་ཤེས་པར་དཀའ༌[^1147]བ་ཡིན་ནོ། །

[Block 1542]
ཉེས་པ་འདི་ནི་འགྲིབ་པ་དང་ཕུལ་དུ་བྱུང་བའི་ཆོས་ཅན་གྱི༌[^1148]ཡིན་ཏེ། མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་ཟིལ་གྱིས་གནོན་པ་ཁྱད་པར་དུ་བྱེད་པ་དང་མི་བྱེད་པ༌[^1149]མེ་ལ་སོགས་པ་དང་འདྲ་བར་སྒྲུབ་པར་བྱེད་དོ། །

[Block 1543]
དེ་དག་ནི་རྣམ་པར་རྟོག་པ་ལས་འབྱུང་བ་ཅན་དག་ཡིན་ཏེ། ཉེ་བར་ལེན་པ་དག་ཡིན༌[^1150]ན་ཡང་ཡིད་ཀྱི་ཡོན་ཏན་འགའ་ཞིག་གོམས་པ༌[^1151]ལས་ཁྱད་པར་དུ་འགྱུར་བ་མེད་པ་དང་། དེ་གསལ་བ་ན་མེ་ལ་སོགས་པ་དང་འདྲ་བར༌[^1152]རྗེས་སུ་འགྲོ་བ་མེད་པ་ཅན་གྱི་འཇིག་པའི་ཆོས་ཅན་དུ་འགྱུར་རོ། །

[Block 1544]
དེ་བས་ན་མཉེས་པར་མེད་པར་ཡང་འགྱུར་རོ། །

[Block 1545]
ཉེས་པ་མེད་པ་ཞེས་བྱ་བ་ཡང་ཇི་ལྟ་བུ་ཡིན། འདི་ལྟར་ཉེས་པའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་བདག་ཉིད་དུ་འགྱུར་བ་ཉིད་ཡོད་ན་ཡང་རྐྱེན་ཇི་ལྟ་བ་བཞིན་དུ་ཉེས་པ་ཡང་འབྱུང་བ་ཡིན་ཏེ། ཉེས་པའི་བདག་ཉིད་དུ་གྱུར་པའི་མི་མཐུན་པའི་ཕྱོགས་སྐྱེ་བ་དང་འདྲའོ་ཞེ་ན།། །།
--- END BLOCKS ---
