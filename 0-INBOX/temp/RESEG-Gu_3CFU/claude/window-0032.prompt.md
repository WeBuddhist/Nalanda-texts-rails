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
[Block 1121]
རྐང་པའི་ཆུ་དང་རྟེན་དང་ཆོལ་ཟངས་དབུལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། རྐང་པའི་ཞེས་བྱ་བའི་སྒྲ་ནི་ཆུ་དང༌[^793]རྟེན་དག་གིས་སོ་སོར་མངོན་པར་འབྲེལ་པ་སྟེ། རྐང་པའི་ཆུ་ལ་སོགས་པ་དབུལ་བར་བྱ་བ་ནི་རྐང་པ་བཀྲུ་བའི་ཆུ་དང་རྟེན་དང་ཆོལ་ཟངས༌[^794]རྣམས་དབུལ་བར་བྱ་བའོ།[^795] །མཆིལ༌[^796]ལྷམ་གཉིས་ཕྱིའོ། །

[Block 1122]
སྒྲུབ་པར་བྱེད་པ་ཉིད་དུ་མ་བསྒོས་པར་ཕྱག་མ༌[^797]ཐོགས་པ་མཐོང་ན་ལས་ཆུང་བར་བྱའོ། །

[Block 1123]
གོས་འཚེམ་པ་ཉིད་དུ་མ་བསྐོས་པར་ཁས༌[^798]ཐོགས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མཐོང་ནས་ལས་ཆུང་བར་བྱའོ་ཞེས་བྱ་བ་རྗེས་སུ་སྦྱར་རོ། །

[Block 1124]
སྒྲུབ་པར་བྱེད་པ་ཉིད་དུ་བསྐོས་པའམ་གོས་འཚེམ་པ་ཉིད་དུ་བསྐོས་པ༌[^799]ལས་ཆུང་བར་མ་བྱས་ཀྱང་སྐྱོན་མེད་དོ། །

[Block 1125]
རུང་བར་བྱ་བ་དང་སྔོ་ཆུང་ངུ༌[^800]བརྔ་བ་དང་མེ་ཏོག་དང་འབྲས་བུ་བཏོགས་པ་དང་། སོ་ཤིང་ཉེ་བར་བསྒྲུབ་པ་ལ་སོགས་པ་ལ་ཡང་དགེ་ཚུལ་བསྐོའོ་ཞེས་བྱ་བ་ནི་གནས་ཀྱི་སླད་དུ་བྱའོ་ཞེས་བྱ་བ་དོན་གྱིས་ཤེས་སོ། །

[Block 1126]
དེའི་ཕྱིར་ཡང་ཞེས་བྱ་བའི་སྒྲས་གནས་པར་བྱ་བ་སྔར་བསྟན་པ་ཐམས་ཅད་དང་གནས་འགའ་ཞིག་ལ་བྱ་བར་མ་ཟད་ཀྱི་དགེ་འདུན་ལ་ཡང་དེ་དག་ཐམས་ཅད་ལ་འདི་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སུ་འབྲེངས་ནས་ཤེས་པར་བྱའོ། །

[Block 1127]
སྒོ་གླེགས་ལ་བརྡབས་པས༌[^801]ནང་ན་གནས་པ་ལ་གོ་བར་བྱའོ་ཞེས་བྱ་བ༌[^802]གནས་དང་གནས་ལའོ། །

[Block 1128]
ཆོ་ག་འདི་ནི་དགེ་སློང་རྣམས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 1129]
དེ་ནི༌[^803]དལ་བུས་དང་ཡུན་མི་རིང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཡང་དང་ཡང་དུ་སྒོ་གླེགས་ལ་བརྡབས་པས༌[^804]ནང་ན་གནས་པ་ལ་གོ་བར་བྱ་བ་སྟེ། །དེ་ནི་དལ་བུ་དང་ཡུན་མི་རིང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཡང་དང་ཡང་དུ་སྒོ་གླེགས་བརྡུང་བར༌[^805]མི་བྱ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1130]
དེ་ནི་གཞན་གྱིས་མི་ཕུལ་ལོ་ཞེས་བྱ་བ་ལ། དེ་ནི་སྒོ་གླེགས་ཏེ་སྒོ་ཞེས་བྱ་བ་གཉིས་པའི་མིང་ཅན་ཤིན་ཏུ་ཤུགས་དང་ལྡན་པས་མི་ཕུལ་ལོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1131]
དལ་བུས་ཤེས་བཞིན་དུ་འཇུག་པ་དང་འབྱུང་བ་དང་སྒོ་སྐྱས༌[^806]ལ་མི་དྲུད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་འདི་དག་ལ་དྲུད་པར༌[^807]མི་འགྱུར་བ་དེ་ལྟར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1132]
དེ་ལ་བཀུར་སྟི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་གནས་སོ། །

[Block 1133]
བར་དུ་གནས་དང་གནས་པ་དབང་དུ་བྱེད་པ་ལ་རྒྱུན་མི་འཆད་པ་ཉིད་ཀྱིས་དེ་ལ་ཞེས་བྱ་བའི་སྒྲ་ནི་གནས་ཡོངས་སུ་བཟུང་བའི་དོན་ལའོ། །

[Block 1134]
བཞར་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ལ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏེ་གནས་པས་གནས་དེ་ལ་བཞར་བར་བྱ་སྟེ། ཐག་མི་རིང་བར་འདུག་པར་བྱ་སྟེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1135]
དེ་དང་ཞེ་འགྲས་པ་ལ་མི་བཞར་རོ་ཞེས་བྱ་བ་ནི་བཞར་བར་བྱའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏེ། གནས་དང་ལྷན་ཅིག་ཞེ་འགྲས་པའི་གང་ཟག་ལ་མི་བཞར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1136]
དེ་ལ་ཁྲེལ་ཡོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་གནས་ལས་སོ། །

[Block 1137]
ཇི་སྲིད་དུ་གནས་པས་གནས་ལ་ངོ་ཚ་ཤེས་པ་དང་བཅས་པས་གནས་པར་བྱའོ་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 1138]
དེའི་བྱ་བ་ལ་གྲིམས་པར་བྱ་ཞེས་བྱ་བ་ནི་ལེ་ལོ་མེད་པའོ། །

[Block 1139]
གུས་པར་བྱས་ཏེ་བྱ་བ་དང་ཞེས་བྱ་བ་ནི་གང་ཞིག་གིས་བྱ་བ་དེ་ནི་གུས་པར་བྱའོ༌[^808]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1140]
མཛེས་པས་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་མཛེས་པ་འདའ་བར་བྱེད་པ་ལ་སོགས་པ་དང་ལྡན་པའོ། །

[Block 1141]
ངོ་ཚ་དང་ལྡན་པ་དང་གུས་པ་དང་བཅས་པ་དང་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཡང་ངོ་ཚ་བའི་བྱེ་བྲག་གུས་པ་ཡིན་ན་དེ་ལྟར་ན་ཡང༌[^809]སྒྲ་འདི་ལས་འདི་ཤེས་པ་མ་ཡིན་པ་དེ་བས་ན་འདི་བཟུང་ངོ་། །ངོ་ཚ་བསྐུམ་པའོ། །

[Block 1142]
རྗེས་དང་བཅས་པའོ་ཞེས་བྱ་བ་ནི་གཞན་ལ་རག་ལས་པའི་རིག་པའི་ངོ་བོ་ཁྲེལ་ཡོད་པའི་བྱེ་བྲག་ནི་རྗེས་དང་བཅས་པའོ། །

[Block 1143]
སེམས་དམའ་བ་ཞེས་བྱ་བ་ནི་ང་རྒྱལ་བཅོམ་པའོ། །ཤེས་བཞིན་གྱིས་ཞེས་བྱ་བ་ནི་རང་གི་དོན་ཏེ་བསམ་གཏན་དང་ཀློག་པ་ལ་སོགས་པའོ། །

[Block 1144]
དགེ་བ་གང་ཡིན་ཞེས་ཚོལ་བ་ཅན་དུ་བྱའོ། །

[Block 1145]
འདི་ལ་བརྟེན་པའི་གནས་བཅའ་བ་དང་ཞུ་བ་དང་འཁོར་སྦྱིན་པ་ལ་སོགས་པ་ལས༌[^810]གཞན་འདི་ལ་གནས་པ་ལ་གང་དགེ་བ་ཚོལ་བས་གནས་པར་བྱའོ། །

[Block 1146]
འཇིག་རྟེན་གྱི་བྱ་བ་ལ་རྩེ་གཅིག་པས་ནི་འདི་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1147]
ཉེས་པ༌[^811]བྱེད་པ༌[^812]འཇུག་ན་བཟློག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གནས་འདི་ཉེས་བྱེད་ཅུང་ཟད་ལ་འཇུག་པ་དེ་ནི་གནས་པས་བཟློག་པར་བྱའོ། །

[Block 1148]
དགེ་བ་མི་འཕེལ་ན་དེ་བྱེད་པ་གནས་པ་གཞན་ལ་གཏད་པར་བྱའོ་ཞེས་བྱ་བ་ལ་གལ་ཏེ་གནས་དེ་ལ་གནས་པའི་དགེ་བ་འཕེལ་བར་མི་འགྱུར་ན། དེ་ནས་དེ་འདི་ལ་དགེ་བ་འཕེལ་བར་བྱེད་པའི་གནས་གཞན་ལ་གཏད་པར་གསོལ་བར་བྱའོ། །

[Block 1149]
དེའི་ཕྱིར་དེས་ཀྱང་དེ་ལ་དྲི་བ་ལ་སོགས་པས་གནས་ཀྱི༌[^813]འོས་ངེས་པར་ཤེས་པར་བྱས་ནས་གཏད་པར་བྱའོ། །

[Block 1150]
གནས་དེས་ཀྱང་གནས་པ་དེ་ལ་འདི་ལ་ཡང་བྱ་བ་སྟེ། སྡིག་པའི་གྲོགས་པོ་ལས་བཟློག་པར་བྱའོ། །

[Block 1151]
དགེ་བ་ལ་སྦྱར་བར་བྱའོ། །

[Block 1152]
དེ་ཉེ་བར་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་བ་ལ་ཉེ་བར་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1153]
ལྟུང་བ་ལས་བསླང་བ་དང་རྗེས་སུ་མཐུན་པའི་འཚོ་བའི་ཡོ་བྱད་བསྒྲུབ་པ་ལ་བརྩོན་པར་བྱའོ་ཞེས་བྱ་བ༌[^814]ནི། ཇི་ལྟར་གནས་པ་ལ་འདི་གཉིས་བསྒྲུབ་པ་དེ་ལྟར་གནས་ཀྱིས་བརྩོན་པར་བྱའོ། །

[Block 1154]
དེས་ཀྱང་དེ་ལ་དེ་བྱའོ་ཞེས་བྱ་བའི་མདོ་འདའ་བ་ལ༌[^815]གནས་པས་ཀྱང་གནས་ལ་འདི་གཉིས་བསྒྲུབ་པ་ལ་བརྩོན་པར་བྱའོ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 1155]
ལྷན་ཅིག་གནས་པ་དང་ཉེ་གནས་དང་མཁན་པོ་དང་སློབ་དཔོན་དང་མཁན་པོ་གཅིག་པ་དང་སློབ་དཔོན་གཅིག་པ་དང་གཏམ་འདྲེས་པ་དང་ཕེབས་པར་སྨྲ་བ་དང་སྨོས་འདྲིན་དང་འགྲོགས་བཤེས༌[^816]རྣམས་ཀྱིས་ནད་གཡོག༌[^817]བྱའོ་ཞེས་བྱ་བ་ལ། གཏམ་འདྲེས་པ་ཞེས་བྱ་བ་ནི་གཏམ་དྲི་བ་ལ་སོགས་པ་དང་དགའ་བ་སྤྱོད་པ་ཉིད་ཀྱིས་དགའ་བ་ཉིད་དུ་བཀྲི་བའོ། །

[Block 1156]
ཕེབས་པར་སྨྲ་བ་ནི་གང་དང་ལྷན་ཅིག་ཏུ་བག་ཕེབས་པར༌[^818]གྱུར་ཅིང་དེ་ལ་དུས་དུས་སུ་ཀུན་དུ་སྨྲ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 1157]
སྨོས་འདྲིན༌[^819]ཞེས་བྱ་བ་ནི་གང་དང་ལྷན་ཅིག་ཏུ་གནས་གཅིག་ན་འདུག་པ་དང་ལྷན་ཅིག་ཏུ་འགྲོ་བ་ལ་སོགས་པས་འདྲིས་པ་ཁས་བླངས་པས་ཡན་ལག་དང་ཡན་ལག་ཅན་གྱི་དངོས་པོ་སྐྱེས་པའོ། །

[Block 1158]
འགྲོགས་བཤེས༌[^820]ཞེས་བྱ༌[^821]ནི་གང་གིས་གང་མཐོང་ངམ་ཐོས༌[^822]མ་ཐག་ཁོ་ནར་ཡན་ལག་ཅན་གྱི་དངོས་པོ་སྐྱེས་པ་ནས༌[^823]དགའ་བ་ཙམ་སྐྱེས་པའོ། །

[Block 1159]
བྱེད་པ་དང་པོ་མེད་ན་འོག་མས་སོ་ཞེས་བྱ་བ་གཙུག་ལག་ཁང་གི་ཉེ་གནས་ལ་སོགས་པ་རྣམས་དང་ལྷན་ཅིག་ཏུ་སྔ་མས་ཉེ་གནས་བྱེད་པ་མེད་པ་ལ་ཕྱི་མ་ཕྱི་མས་ཉེ་གནས་བྱའོ། །

[Block 1160]
གཙུག་ལག་ཁང་དང་ལྷན་ཅིག་ཏུ་ཉེ་གནས་བྱེད་པ་མེད་པ་ལ༌[^824]མཐར་གནས་པས་ཉེ་གནས་བྱའོ། །
--- END BLOCKS ---
