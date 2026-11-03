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

[Block 1161]
དེ་ཡང་མེད་ན་མཁན་པོས་སོ། །

[Block 1162]
དེ་ཡང་མེད་ན་སློབ་དཔོན་གྱིས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1163]
མཁན་པོ་ལ་ལྕི་བ་ཉིད་ཀྱི༌[^825]ཕྱིར་དེའི་སྔོན་དུ་གང་ཞིག་དང་པོར་འོས་པ་ཉིད་སློབ་དཔོན་ལ་མཐར་གནས་པ་ལ་གཙུག་ལག་ཁང་དང་ལྷན་ཅིག་ཉེ་གནས་པས་སོ། །

[Block 1164]
དེ་བས་ན་ཤིན་ཏུ་ཉེ་བར་གནས་པ༌[^826]ཉིད་ཀྱི༌[^827]ཕྱིར་ལྷག་མ་སྔ་མ་ལ་དང་པོ་འོས་པ་ཉིད་དོ། །

[Block 1165]
འདིར་ཀློག་པའི་སློབ་དཔོན་ཡང་བཟུང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སློབ་དཔོན་བཟུང་བས་སོ། །

[Block 1166]
ཅིག་ཅར་མི་ནུས་ན་གནས་པ་གང་དང་འཇུག་པའིའོ༌[^828]ཞེས་བྱ་བ་ལ། ཅིག་ཅར་ཞེས་པ་ནི་ནད་པ་ལ་ཉེ་བར་གནས་དུ་མ་ལའོ། །

[Block 1167]
མི་ནུས་པ་ལ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཅིག་ལས་ཡང་ཉེ་བར་གནས་པ་མི་ནུས་ན་གནས་པ་ཉེ་བར་གནས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1168]
གནས་པ་སུ་ཞིག་ཅེ་ན། གང་དང་འཇུག་པའིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་ལ་ཞུ་བ་བྱས་ནས་བྱ་བ་བྱེད་པ་གང་གི་ཚེ་གང་ལ་གང་གིས་གལ་ཆེ་བ་དེའི་དེ་ལ་འཇུག་པའོ། །

[Block 1169]
ཤིན་ཏུ་གནོད་པར་བྱེད་པའི་ཕོངས་པ་ལ་ཐམས་ཅད་དོར་ནས་ཞེས་བྱ་བ་དོན་གྱིས་གོ་བར་བྱའོ། །

[Block 1170]
འདིར་དེའི་རྟགས་ཙམ་པ་ཡང་རབ་ཏུ་བྱུང་བ་དང་འདྲའོ་ཞེས་བྱ་བ་ལ། འདིར་ཞེས་བྱ་བ་ནི་ནད་གཡོག་བྱ་བའི་ཡུལ་ལ་གང་ཞིག་རབ་ཏུ་བྱུང་བའི་དོན་དུ་སྐྲ་བྲེགས་པ༌[^829]ལ་སོགས་པའི་རྟགས་ཙམ་གྱིས་སྦྱར་ཅིང་ད་ལྟར་ཡང་རབ་ཏུ་འབྱུང་དུ་མ་བཅུག་པ་དེ་ནི་རབ་ཏུ་བྱུང་བ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 1171]
ཇི་ལྟར་རབ་ཏུ་བྱུང་བ་ལ་ཉེ་བར་གནས་པ་དེ་ལྟར་ནད་པ་དེ་ལ་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1172]
ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་ན་བ་ཡལ་བར་མི་དོར་རོ། །

[Block 1173]
དེ་ལ་ནད་གཡོག་མེད་ན་མཐར་ཐུག་པ༌[^830]མན་ཆད་ལས༌[^831]བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། མེད་ན་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་ལ་སོགས་པ་དང་ལྷན་ཅིག་ཏུའོ། །

[Block 1174]
གང་མན་ཆད་ལས་བསྐོ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་མཐར་ཐུག་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་གཅིག་བྱིན་ནས་ཀྱང་ཉེར༌[^832]གནས་མེད་པར་གྱུར་ནས། དེས་འབྲས་བུ་བསྒྲུབ་པའི་ནུས་པ་མེད་པའི་ཕྱིར་གཞན་བསྐོ་བར་བྱའོ། །

[Block 1175]
དེ་བཞིན་དུ་ཇི་སྲིད་དུ་དགེ་འདུན་གྱི་མཐར་ཐུག་པ་མན་ཆད་ལས་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1176]
འདིར་གཞུང་ནི་ཐམས་ཅད་མེད་ན་དགེ་འདུན་གྱི་ནད་པའི་གནས་སྐབས་ཡོངས་སུ་ཤེས་པར་བྱ་སྟེ། ནད་གཡོག་གཅིག་གམ་གཉིས་སམ་རབ་ཏུ་མང་པོ༌[^833]བསྐོར་བར་བྱ་ཞིང་ཐ་ན་དགེ་འདུན་ཐམས་ཅད་ཀྱིས་ནད་གཡོག་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1177]
སྨན་བརྟག་པར་བྱ་བའི་ཕྱིར་དགེ་འདུན་ལས་བྱུང་བའི་སྨན་ནི་ནད་པ་འབའ་ཞིག་གིས་སྤྱད་དུ་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱིམ་བདག་སྒྲེ་བོའི༌[^834]རྫས་ལས་སྨན་གང་ཡིན་པ་དགེ་འདུན་གྱི་སྨན་ཁང་དུ་གཞུག་པར་བྱ་ཞིང་དགེ་སློང་ནད་པ་རྣམས་ཀྱིས་ལོངས་སྤྱད༌[^835]པར་བྱའོ་ཞེས་གསུངས་པ༌[^836]དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 1178]
མེད་པ་ཉིད་ཡིན་ན་དེ་ནད་གཡོག་གིས་ཚོལ་དུ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་མེད་པར་གྱུར་ན་སྨན་འདི་ནད་གཡོག་གིས་ཚོལ་དུ་གཞུག་པར་བྱའོ། །

[Block 1179]
མ་འབྱོར་ན་དགེ་འདུན་གྱིས་ལས་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཚོལ་དུ་བཅུག༌[^837]ཀྱང་མ་འབྱོར་བར་གྱུར་ན་དེ་ནས་དགེ་འདུན་གྱིས་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1180]
མེད་ན་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱིའོ། །

[Block 1181]
སངས་རྒྱས་ཀྱི་སྐུ་ལ་གསོལ་བ་མན་ཆད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་སྐུ་གཟུགས་དང་མཆོད་རྟེན་དང་རྒྱན་ལ་སོགས་པ་བཏགས་པ་གང་ཡིན་པ་དེ་དག་གི་བར་ཡང་སྦྱིན་པར་བྱ་ན་གཞན་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1182]
དེའི་ཕྱིར་དགེ་འདུན་གྱི་ལས་བཏུང་བ་དང་གདུགས་གདགས་པ་ལ་སོགས་པའི་མཆོད་པ་བྱའོ་ཞེས་བྱ་བ་ནི་མ་འབྱོར་ན་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 1183]
རང་ལ་མེད་ན་དགེ་འདུན་ལས་འདི་ལ་བྱའོ། །

[Block 1184]
དགེ་འདུན་ལ་འདི་མེད་ན་སངས་རྒྱས་ཀྱི་ལས་སོ། །

[Block 1185]
དེ་གཉིས་ཀྱིས་བླངས་པ་དེ་མ་ཤི་ལ་འབྱོར་པ་ཡོད་ན་བསམ་པ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་གཉིས་ཀྱི༌[^838]ཞེས་བྱ་བ་ནི་དགེ་འདུན་དང་སངས་རྒྱས་གཉིས་དག་གིའོ། །

[Block 1186]
སྦྱིན་དུ་མེད་ན་སྐྱོན་མེད་དོ། །

[Block 1187]
ནད་གཡོག་གིས་དེ་ལ་བསྙེན་བཀུར་མི་བྱ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་ནད་པ་ལའོ། །

[Block 1188]
དེའི་ཚིག་དོན་དང་ལྡན་པ་དང་ཆོས་དང་ལྡན་པ་བཅག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དོན་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་འཚོ་བ་ལ་ཕན་པ་དང་སོ་སོར་ཡང་དག་པར་འབྲེལ་བའོ། །

[Block 1189]
དེའི་ཞེས་བྱ་བ་ནི་ནད་པའོ། །

[Block 1190]
ཆོས་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་བསོད་ནམས་ལ་ཕན་པ་དང་འབྲེལ་པའོ། །

[Block 1191]
ལྷག་པར་ཆགས་པའི་དངོས་པོ་འགུགས་ན་དགག༌[^839]པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་ལྷག་པར་ཆགས་པའི་དངོས་པོ་ནི་ལྷུང་བཟེད་ལ་སོགས་པ་གང་ལ་ནད་པའི་སྲེད༌[^840]པའོ། །

[Block 1192]
འགུགས་ན་ཞེས་བྱ་བ་ནི་ནད་པས་ནད་གཡོག་ལའོ། །

[Block 1193]
མི་གདམས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་གཡོག་གིས་ནད་པ་ལའོ། །

[Block 1194]
དེ་ནད་པས་བཟླ་བར་ཤིན་ཏུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་གཡོག་གིས་གདམས་ངག་བྱས་པ་ལས་ནད་པ་འདའ་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1195]
ནད་གཡོག་དེས་དེ་འཆི་བར་དོགས་ན་དེ་དགེ་འདུན་གྱི་མལ་སྟན་ལ་བསླང་སྟེ་གང་ཟག་གི་ལ་གཞག་པར་བྱའོ། །
--- END BLOCKS ---
