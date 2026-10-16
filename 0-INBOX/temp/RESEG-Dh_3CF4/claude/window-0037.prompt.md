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
[Block 1296]
སྔར་བསྟན་པའི་དེ་ལས་སྦྱིན་པ་ཚུལ་ཁྲིམས་ཞེས་བྱ་བའི་ཚིགས་བཅད་དེས་ནི་བསོད་ནམས་ཉི་ཚེ་སྤེལ་བ་ལ་གྲོགས་པོ་བཙུད་པ་ཡིན་ནོ། །

[Block 1297]
སྡུག་བསྔལ་གཞིར་གྱུར༌[^750]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་མི་མཐུན་པའི་ཕྱོགས་སྤང་བ་དང་། གཉེན་པོའི་ཕྱོགས་བསྟེན་པ་ལ་གྲོགས་པོ་དག་ཡང་དག་པར་འཛུད་པ་ཡིན་ནོ། །

[Block 1298]
སྡུག་བསྔལ་གྱི་གཞིར་གྱུར་ཞེས༌[^751]བྱ་བ་ནི༌[^752]འདི་ལ་སྡུག་བསྔལ་གྱི་གནས་ཡིན་པས་སྡུག་བསྔལ་གནས་གཞི་སྟེ། གང་ལ་སྡུག་བསྔལ་གྱི་གནས་ཀྱི་བསོད་ནམས་མ་ཡིན་པའི་ལས་ཡོད་པ་དེ་ནི་སྡུག་བསྔལ་གྱི་གཞིའོ། །

[Block 1299]
དེ་བས་ན་འདིས་ནི་སྡིག་པའི་ལས་ཏེ་ངན་སོང་གི་རྒྱུ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1300]
གང་ལ་གཏམ་ངན་དང་རྗེས་སུ་འབྲེལ་པའི་སྡིག་པའི་ལམ་དེ་ནི་གཏམ་ངན་རྗེས་སུ་འབྲང་བའོ། །

[Block 1301]
དེ་བས་སླར་ལོག་ལ་ཞེས་བྱ་བ་ནི་བསོད་ནམས་མ་ཡིན་པའི་ལམ༌[^753]ལས་ལྡོག་པ་སྟེ། སེར་སྣ་དང་ཚུལ་ཁྲིམས་འཆལ་ཅིང་མི་བཟོད་པ་དེ་ལས་སླར་ལྡོག་པའོ། །

[Block 1302]
དཔལ་ལྡན་པ་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་གྲགས་པ་ལ་སོགས་པའོ། །

[Block 1303]
བདེ་བ་རབ་ཏུ༌[^754]འབྱུང་སྒྲུབ་ལ། ཞེས་བྱ་བ་ནི་བདེ་བ་རབ་ཏུ་འབྱུང་བའོ། །

[Block 1304]
དེའི་སྒྲུབ་པ་ནི། བདེ་བ་རབ་ཏུ་འབྱུང་བ་སྒྲུབ་པ་སྟེ། འདིས་སྒྲུབ་པ་ཡིན་པས་སྒྲུབ་པའོ། །

[Block 1305]
བསོད་ནམས་སྤྱད་པ་ལས༌[^755]ཞེས་བྱ་བ་ནི་བསོད་ནམས་དང་འབྲེལ་པ་ལ་སྟེ། འདིས་ནི་རྟག་ཏུ་བྱེད་པ་ལ་སྦྱོར་བ་ཡིན་ནོ། །

[Block 1306]
དེ་ལྟར་རེ་ཞིག་སྙན་པར་སྨྲ་བའི་མཚན་ཉིད་ཀྱི་བསྡུ་བའི་དངོས་པོས་བསྡུས་ནས་དོན་མཐུན་པའི་བསྡུ་བའི་དངོས་པོས་བསྡུ་བའི་ཕྱིར། བདག་ཉིད་ཆེན་པོ་དེས་བསམས་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞན་དུ་ན་ཇི་སྐད་དུ་སྨྲས་པ་དེ་བཞིན་བྱེད་པ་ཉིད་དུ་སྟོན་པར་མི་འགྱུར་རོ། །

[Block 1307]
འདིར་ཅིའི་ཕྱིར་སྦྱིན་པ་དང་དོན་སྤྱོད་པའི་བསྡུ་བའི་དངོས་པོ་མ་བཤད་ཅེ་ན། དེ་ནི་བཤད་པ་ཉིད་དེ། སྔར་སྦྱིན་པའི་རང་བཞིན་གྱི་བསྡུ་བའི་དངོས་པོ་བསྟན་པ་ནི་ཕན་ཚུན་གཉེན་དུ་འབྲེལ་པ་བཞིན་དུ་གཅིག་ལ་གཅིག་བྱམས་པར་ནི་གྱུར་ཞེས་བྱ་བའི་ཚིག་རྐང་གིས་བསྡུས་པ་ཡིན་ཏེ། ཐབས༌[^756]སྦྱིན་པ་ཡང་བསྡུ་བའི་དངོས་པོར་གྲགས་པ་ཉིད་དེ་ཡང་བརྗོད་པར་མི་བྱའོ། །

[Block 1308]
དོན་སྤྱོད་པའི་བསྡུ་བའི་དངོས་པོ་ཡང་བཤད་པ་དེ༌[^757]ཉིད་དེ། གཅིག་ལ་གཅིག་སྤོབས་ཤིང་བཀུར་སྟི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐང་གིས་བསྟན་ཏེ། གང་གི༌[^758]ཕྱིར་སྤོབས་ཤིང་བཀུར་སྟི་ནི་དོན་སྤྱོད་པའི༌[^759]བསྡུ་བའི་དངོས་པོ་སྟེ། དེ་བས་ན་བསྡུ་བའི་དངོས་པོ་བཞི་ཡང་བསྟན་པའི་ཚུལ་ཉིད་ཡིན་ཏེ། ཡང་ཚིག་བསྟན་པ་ནི་བརྗོད་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1309]
མགྲོན་ལ་བསྙེན་བཀུར་བྱེད་པ༌[^760]ཅིའི་ཕྱིར་ནུས་པ་མེད་ཅེ་ན། རྩྭ་ནི་སོས་བཅད་པར་ནུས་པ་ཡིན་ཏེ། དེ་བས་ན་བདག་གི་སོ་རྩེས་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདི༌[^761]སྟེ། སྔར་མ་བྱུང་བ་ཉིད་བསྟན་ཅིང་མགྲོན་ལ་བསྙེན་བཀུར་མི་ནུས་པ་ཉིད་དེ། དེ་ལྟར་གསལ་བ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ཏེ། རྩྭའི་མྱུ་གུ་ཁ་བོ་ནི་ཞེས་བྱ་བ་ནི་རྫས་དང་རོས་མགྲོན་ལ་སྦྱིན་དུ་མི་རུང་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1310]
ཡོང་ཡེ་ཞེས་བྱ་བ་ནི་མདོར་བསྡུ་ན་ནུས་པ་མེད་པ་དང་མཉམ་པའི་སྨད་པ་ནི་ཅུང་ཟད་ཀྱང་མེད་པའི་ཕྱིར་རོ། །

[Block 1311]
དེ་བས་སྦྱིན་པ་མི་ནུས་པ་ཞེས་བྱ་བ་ནི་གཞན་ལ་ཕན་འདོགས་པའི་ནུས་པ་ཉིད་ལ་ཞན་པའོ། །

[Block 1312]
ཡང་ན་ནུས་པ་མེད་པ་དང་ཞན་པ་ནི་ནུས་མེད་ཞན་པ་སྟེ། སློང་བ་རྣམས་ལ་ཕན་འདོགས་པར་མི་ནུས་པའོ། །

[Block 1313]
གསོན་ཡང་ཅི་ལ་ཕན་ཞེས་བྱ་བ་ནི་གསོན་པ་ཞེས་བྱ་བ་འདིས་གཞན་ལ་ཕན་འདོགས་པ་གང་ཡིན་པ་དེ་ནི་ནུས་པ་མེད་པས་དོན་ཅི་ཞིག་ཡོད་ཅེས་སོ། །

[Block 1314]
དགའ་བ་ཞེས་བྱ་བ་ནི་དགའ་བའི་རྒྱུ་སྟེ།

[Block 1315 [VERSE]]
རྒྱུ་ལ་འབྲས་བུ་བཏགས་པའི་ཕྱིར་རོ། །
མྱ་ངན་ཡང་མྱ་ངན་གྱི་རྒྱུ་སྟེ།
བདག་ནི་མགྲོན་བཞིན་འོངས་གྱུར་ན། །

[Block 1316]
ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་ནུས་པ་མེད་པ་དང་ལྡན་པའོ། །

[Block 1317]
འདི་ལྟར་ཞེས་བྱ་བ་ནི་བདག་གི་སོ་རྩེས་ཞེས་བྱ་བའི་ཚིགས་བཅད་དུ་བསྟན་པ་དེའི་རྣམ་པས་མགྲོན་ལ་བསྙེན་བཀུར་བྱ་བར་མི་ནུས་པས་སོ། །

[Block 1318]
མགྲོན་རྣམས་ཀྱི་བསྙེན་བཀུར་ནི་མགྲོན་གྱི་བསྙེན་བཀུར་རོ། །

[Block 1319]
དེ་ལ་མི་རུང་བ་ནི་མགྲོན་གྱི་བསྙེན་བཀུར་བྱ་བར་མི་རུང་བའོ། །

[Block 1320]
དེས་སྙིང་པོ་མེད་པ་ནི་མགྲོན་ལ་བསྙེན་བཀུར་བྱར་མི་རུང་བས་སྙིང་པོ་མེད་པའོ། །

[Block 1321]
ལུས་ཉིད་ནོར་ཡིན་ཏེ། ནོར་ནི་འདོད་པའི་དོན་སྒྲུབ་པ་ཉིད་ཀྱིས་ཏེ། སེམས་ནི༌[^762]ཁྱོད་དེ་བས་ན་རྟོགས་པ་དེ་ལས་མི་དགའ་བ་མ་བྱེད་ཅིག་པའོ། །

[Block 1322]
ཡོངས་སུ་རྫོགས་པར་ཡོད་པ་འདིས་མགྲོན་གྱི་སྐྱེ་བོ་སྤོབས་པར་སློང་བ་ལ་མགྲོན་བྱའོ་ཞེས་སོ། །

[Block 1323]
མཐུ་དང་རབ་ཏུ་དང་བ་དག་རབ་ཏུ་བསྟན་པ་སྟེ། ལྷ་རྣམས་བྱང་ཆུབ་སེམས་དཔའི་མཐུ་སྟོན་པར་བྱེད་ཅིང་།

[Block 1324 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའི་གཏམ་ལྷ་རྣམས་སྒྲོགས་པར༌[^763]བྱེད་དོ། །
མཐུ་དང་དང་བ་ལྷ་རྣམས་ལ་ནི་བསྟན་པར་གྱུར། །

[Block 1325]
ཞེས་བྱ་བ་དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། དེ་ནས་ས་གཞི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་སྟེ། ཚིགས་བཅད་འདི་གསུམ་གྱི་བསྡུས༌[^764]པའི་དོན་ནི་ས་འགུལ་བའི་མཚན་མ་དང་། མཆོད་པའི་དབང་དུ་བྱས་པ་སྟེ། མཁའ་ལས་ལྷའི་རྔ་སྒྲ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་མཆོད་པའི་དོན་ཏོ། །

[Block 1326]
ཕན་ཚུན་བསྡོས༌[^765]པས་མེ་ཏོག་གི་རྡུལ་རྣམས་ལྷགས་པར༌[^766]གྱུར་པ་གང་ཡིན་པ་དེ་ནི་ཕན་ཚུན་བསྡོས༌[^767]པའི་རྡུལ་རྣམས་ལྷགས་པའི་མེ་ཏོག་གོ། །

[Block 1327]
རབ་ཏུ་འཁྲིགས་པ་སྲབ་མོའི་ཞེས་བྱ་བ་ནི་རབ་ཏུ་འཁྲིགས་པ་གང་ཡིན་པའི་སྲབ་མོའི་གོས་ཡིན་གྱི། གཞན་རབ་ཏུ་འཁྲིགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1328]
དེ་ལས་ཐོས་པ་ནི་ས་འགུལ་བ་ལ་སོགས་པའོ། །

[Block 1329]
རབ་ཏུ་དགའ་ཞིང་ངོ་མཚར་སྐྱེས་པ་ནི་སྔར་དང་བ་ཐོབ་པའོ། །

[Block 1330]
ཡིད་ལ་ཡ་མཚན་དང་ངོ་མཚར་ཆེ་བ་ཞེས་བྱ་བ་ནི་ངོ་མཚར༌[^768]ཡ་མཚན་ཆེ་བ་གཉིས་ཀྱིས་དྲངས་པ་སྟེ། དེས་ངོ་མཚར་དུ་གྱུར་ནས་རྣམ་པར་རྟོག་པ་རྨད་དུ་བྱུང་བར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1331]
ངོ་མཚར་ཆེ་བ་དེས་ན་དེ་ཉིད་ཉམས་སད་པས་འདོད་པ་སྟེ་དེས་སོ། །

[Block 1332]
ཉི་མའི་འོད་རབ་ཏུ་གསལ་བ་གང་ཡིན་པ་དེ་ནི་ཉི་མའི་འོད་ཟེར་རབ་ཏུ་གསལ་བར་གྱུར་པའོ། །

[Block 1333]
འདིར་ཚ་བས་བྱས་པའི་ངལ་བ་དེས་གདུངས་པ་གང་ཡིན་པ་དེ་ནི་ཚ་བས་གདུངས་ཤིང་ངལ་བར་གྱུར་པའོ། །

[Block 1334]
དེ་དག་གིས་ནི་བཀྲེས་པ་དང་སྐོམ་པ་དང་། ངལ་བས་གདུངས་ཤིང་མགྲིན་པ་འགགས་པའོ། །

[Block 1335]
ཡང་ན་བཀྲེས་པ་དང་། སྐོམ་པ་དང་། ངལ་བས་བྱས་པའི་གདུང་བ་དེས་མགྲིན་པ་འགགས་པ་གང་ཡིན་པའོ། །
--- END BLOCKS ---
