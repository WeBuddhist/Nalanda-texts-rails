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
[Block 1331]
དེ་ལ་བྱ་བའི་ཆ་མ་ཡིན་པར་དོགས་པ༌[^1156]མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1332]
གལ་ཏེ་དུས་མ་ཡིན་པར་ནས་ལས་བྱས་པའི་སྨན་དགོས་པ་ཉིད་ཡིན་ན་དེའི་དོན་དུ་བ་ལང་རྒན་པོའི་ལྕི་བའི་ནས་ཀྱིས་ཆོག་པར་བྱའི་གཞན་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་དོན་དུ་ཞེས་བྱ་བ་ནི་ནས༌[^1157]ལས་བྱས་པའི་སྨན་དེའི་དོན་དུའོ། །

[Block 1333]
གཞན་ཞེས་བྱ་བ་ནི་ནས༌[^1158]གཞན་དག་གོ། །

[Block 1334]
གལ་ཏེ་སྐྱོ་མ་ཚགས་ཀྱིས་བཙགས་ནས་ཏེ་གཞན་ནི༌[^1159]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དུས་མ་ཡིན་པར་ཟ་བར་བྱ་བ་ཉིད་ལ་གང་ཞིག་སྨན་དུ་བྱས་པ་དེའི་དོན་དུ་བྱའི་ནས་ལས་བྱས་པ་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1335]
དེ་རྣམས་ལ་ཡང་བ་ལང་རྒན་པོའི་ལྕི་བའི་ནས་ཀྱིས་ཆོག་པར་བྱའི་གཞན་བཟའ་བར་མི་བྱའོ། །

[Block 1336]
གལ་ཏེ་ཤའི་སྨན་དགོས་པ་ཉིད་ཡིན་ན་མཚའི་རྟུག་པའི༌[^1160]ཤས་སོ་ཞེས་བྱ་བ་དུས༌[^1161]མ་ཡིན་པར་དགོས་པ༌[^1162]ཉིད་ལ་མཚའི་རྟུག་པའི་ནང་ནས་བྱུང་བའི་ཤས་དེའི་དོན་དུ་ཆོག་པར་བྱའི་ཤ་གཞན་ལོངས་སྤྱད་པར་མི་བྱའོ། །

[Block 1337]
གལ་ཏེ་ཁུ་བ་ཚགས་ཀྱིས་བཙགས་ནས་ཏེ། གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དུས་མ་ཡིན་པར་ཤ་ལས་བྱས་པའི་སྨན་དགོས་པ་ཉིད་ཡིན་ནོ།[^1163] །དེའི་དོན་དུ་མཚའི་རྟུག་པའི་ནང་ནས་བྱུང་བའི་ཤས་ཆོག་པར་བྱ་བ་དེ་ཡང་ཤ་དེས་བྱས་པའི་ཁུ་བ་གལ་ཏེ་ཚགས་ཀྱིས་བཙགས་ན་དེས་ཆོག་པར་བྱ་བ་ཡིན་གྱི། དེ་ལས་གཞན་པའི་ཚགས་ཀྱིས་མ་བཙགས་པ་དག་ནི་བཟའ་བར་མི་བྱའོ། །

[Block 1338]
གཞན་དག་བཅས་པ་ལ༌[^1164]དེ་ལྷག་པར་སྤྱོད་པ་ཡོད་དོ། །

[Block 1339]
དེའི་ཕྱིར་དེ་ལས༌[^1165]བཅས་པ་ལ་ཆོ་ག་སྔ་མས་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་གཞན་དང་བཅས་པ་དེ་ལ་ལྷག་པར་སྤྱད་པ་ལྷག་པར་མི་སྤྱོད་པར་འགྱུར་བ་དེ་བས་ན་གང་ཞིག་འདིར་དུས་དང་དུས་མ་ཡིན་པ་ལ་སོགས་པ་ཆོ་ག་སྔ་མ་དེ་དང་དེས་ཕྱི་མ་བཅས་པ་ཉིད་ལ་འཇུག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1340]
ཐུན་ཚོད་དུ་རུང་བ་དང་ཞག་བདུན་པ་དང་། འཚོ་བའི་བར་དུ་བཅང་བ་དང་དུས་སུ་རུང་བ་དང་འདྲེས་བ་གང་དག་ནི་དུས་ཁོ་ནར་ལོངས་སྤྱད་པར་བྱའི། དུས་མ་ཡིན་པར་ལོངས་སྤྱད་པར་མི་བྱའོ། །

[Block 1341]
ཞག་བདུན་པ་དང་། འཚོ་བའི་བར་དུ་བཅང་བ་ཐུན་ཚོད་དུ་རུང་བ་དང་། འདྲེས་པ་དག་གིས༌[^1166]ཐུན་ཚོད་དུ་ཁོ་ནར་ཡོངས་སུ་ལོངས་སྤྱད་པར་བྱའི། ཐུན་ཚོད་ཀྱི་མཐའ་ལས་ཡོལ་བར་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ། །

[Block 1342]
འཚོ་བའི་བར་དུ་བཅང་བ་དང་ཞག་བདུན་པ་དང་། འདྲེས་པ་ནི་ཞག་བདུན་པ་ཁོ་ནར་ཡོངས་སུ་ལོངས་སྤྱད་པར་བྱའི། འཚོ་བའི་བར༌[^1167]བཅང་བར་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་དེ་ལ་མདོ་འདི་བྱས་པའོ། །

[Block 1343]
རང་བཞིན་གཞན་དུ་མ་གྱུར་པ་ནི་སྔོན་གྱི་རང་བཞིན་མ་ཡིན་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1344]
དེའི་ཕྱིར་གཞན་དང་མ་འདྲེས་པ་ལ་ནི༌[^1168]རང་གི་ཆོ་གས་རུང་བར་བྱ་བ་མི་འགྲུབ་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། རང་བཞིན་གཞན་དུ་མ་གྱུར་པ་ནི་གང་གང་མ༌[^1169]འདྲེས་པ་དེའི་བག་ཆགས་སུ་འགྱུར་བའི་ངོ་བོ་ཉིད༌[^1170]གཞན་ནོ། །

[Block 1345]
སྔོན་གྱི་རང་བཞིན་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་གང་གི་སྔོན་དུ་རང་གི་རིགས་ཙམ་དུ་གྱུར་པ་ངོ་བོ་ཡོད་པར་གྱུར་པ་དེ་ལས་རྣམ་པ་གཞན་ཉིད་ནི་སྔོན་གྱི་རང་བཞིན་མ་ཡིན་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1346]
གང་གི་ཕྱིར་རང་བཞིན་གཞན་དུ་མ་གྱུར་པ་ནི་སྔོན་གྱི་རང་བཞིན་མ་ཡིན་པ༌[^1171]ཉིད་མ་ཡིན་པ་དེའི་ཕྱིར། གཞན་དང་མ་འདྲེས་པའི་ཞེས་བྱ་བ་ནི། གང་གིས་འདི་དང་འདྲེས་པ་ཡང་དག་པར་འབྱུང་བར་འགྱུར་བ་དེ་ལས་ཐ་དད་པར་གྱུར་པ་ལ་རང་གི༌[^1172]ཆོ་གས་རུང་བས༌[^1173]བྱ་བ་མི་འགྲུབ་པ་མ་ཡིན་པ་དེ་འགྲུབ་པ་ཁོ་ན༌[^1174]ཡིན་ནོ། །

[Block 1347]
དུས་སུ་རུང་བའི་ནང་ན་འདུག་པའི་འཚོ་བའི་བར་དུ་བཅང་བ་ལ་དུས་སུ་རུང་བ་ཉིད་དང་། རང་བཞིན་གཞན་དུ་མ་གྱུར་པ་དང་། གཞན་དང་མ་འདྲེས་པ་ལ་ནི་དུས་སུ་རུང་བ་དེ་ལས་འཚོ་བའི་བར་དུ་བཅང་བས་རུང་བ་བྱ་བ་མི་འགྲུབ་པ་མ་ཡིན་ཏེ། རང་རང་གི་ཆོ་ག་འདི་ལ་འཇུག་པར་བྱར་རུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1348]
བུ་རམ་བསྒོང་བའི་ཕྱིར་འབྲས་ཕྱེའི་ནང་དུ་གཞག་པ་ནི་བཀྲུ་བས་རང་ཁོ་ནའི་གྲངས་ཉིད་དུ་འགྲུབ་པོ་ཞེས་བྱ་བ་ནི་ཞག་བདུན་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1349]
འགོར་གྱི་ཟུངས་ནི་བུ་རམ་ཉིད་དུ་ཤེས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བུ་རམ་བསྐོལ་བའི་དུས་སུ་འགོར་དང་ལིངས་ཉིད་དུ་བྱ་བའི་ཕྱིར་འབྲས་ཀྱི་བག་ཕྱེ་ལ་སོགས་པ་བླུགས་པ༌[^1175]དེ་ནི་བུ་རམ་ཉིད་ཡིན་པས། དེ་ལ་དུས་སུ་རུང་བ་ཉིད་ནི་མ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1350]
དེའི་ཕྱིར་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 1351]
བྱིན་གྱིས༌[^1176]བརླབས་པ་ལ་ནི་གསོག༌[^1177]འཇོག་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི། བཙུན་པ་བྲོ་འཚལ་བས་བྱིན་ལེན་བགྱིས་པ་དང་། བྱིན་གྱིས་བརླབས་པ་ཡོངས་སུ་ལོངས་སྤྱོད་དུ་རུང་ངམ། ཉེ་བ༌[^1178]འཁོར་རུང་ངོ་ཞེས་གང་ཞིག་གསུངས་པ་དེ་བས་ན་མདོ་འདི་བྱས་སོ། །

[Block 1352]
བྲོ་འཚལ་བ་ཞེས་བྱ་བ་ནི་ན་བ་ལ་རུང་བ་ཉིད་དུ་བསྟན་པ་ཉིད་ཡིན་ནོ། །

[Block 1353]
ནད་པའི་ཆེད་དུ་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་ཕྱིར་རང་གི་དུས་ཀྱི་མཐའི་བར་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དུས་སུ་རུང་བའི་ནི་དེའི་ཡུལ་མ་ཡིན་ཏེ། བྱིན་གྱིས་བརླབས་པ་དོན་མེད་པའི་ཕྱིར་རོ། །

[Block 1354]
ཐུན་ཚོད་དུ་རུང་བ་དང་། ཞག་བདུན་པ་དང་འཚོ་བའི་བར་དུ་བཅང་བ་དག་རང་རང་གི་དུས་ཀྱི་མཐའ་ཚུན་ཆད་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 1355]
དུས་གང་གི་ཚེ་བྱིན་གྱིས་བརླབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཟས་སྔ་མའི་ཚེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཆོ་གའི་གཞིར་གྱུར་པ་ཞེས་བྱ་བ་ཡིན་པས། དུས་སུ་བཟའ་བར་བྱ་བ་ལ་བརྟེན་པའོ། །

[Block 1356]
བཟའ་བར་བྱ་བའི་དུས་འདི་ལ་གཞིར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བས་དེ་ཤེས་པའོ། །

[Block 1357]
ཐུན་ཚོད་ཀྱི་དོན་ལས་ཀྱང་འདིའི་ངེས་པ་རྣམ་པར་གནས་པ་བྱིན་གྱིས་བརླབ་པ་མེད་པར་ཕྱིས་ཟས་བྱིན་ལེན་བྱས་པ་ལ་ཐུན་གཅིག་གི་མཐར༌[^1179]ཇི་སྲིད་དུ་རུང་བ་ཉིད་ཅེས་བྱ་བ་དེ་ཉིད་དུ་འདི་ལ་དོན་དང་བཅས་པ་ཉིད་དོ། །ཇི་ལྟར་ཞེ་ན། དེའི་ཕྱིར་བྱིན་ལེན་བྱས་ཏེའོ། །

[Block 1358]
བྱིན་ལེན་མ་བྱས་པ་དང་གསོག་འཇོག་དང་འདྲེས་པ་བསྲུང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1359]
དེའི་ཕྱིར་ལག་པ་གཉིས་ཀ་བསྙལ་ནས་སོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ལག་པ་གཉིས་མ་བསྙལ་བ་ལ་བྱིན་ལེན་མ་བྱས་པ་དང་། གསོག་འཇོག་དང་འདྲེས་པ་བསྲུང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1360]
ལག་ཉར་བླངས་པ་དང་གསོག་འཇོག་བྱས་པ་དང་། བྱིན་ལེན་མ་བྱས་པ་དང་། ནང་དུ་ཞག་ལོན་པ་དང་། ནང་དུ་བཙོས་པ་དང་དགེ་སློང་གིས་བཙོས་པ་དག་ལ་བྱིན་གྱིས་བརླབས་པ༌[^1180]མི་འཆགས་སོ་ཞེས་བྱ་བ་ལ་བཙོས་པའི་སྒྲས་ཀྱང་ནང་དུའི་སྒྲ་དང་འབྲེལ་པའོ། །

[Block 1361]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 1362]
ནང་དུ་བཙོས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 1363]
རོ་དང་སླ་བ་ཉིད་ཡོངས་སུ་གྱུར་ན་ནི་གསོག་འཇོག་བྱས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རོ་མི་སྣང་བ་ཉིད་དུ་ཡོངས་སུ་གྱུར་པ་ནི༌[^1181]དེའི་ཚེ་གསོག་འཇོག་བྱས་པ་ཉིད་ཡིན་ནོ། །

[Block 1364]
འདིར་ནི༌[^1182]འདི་གཉིས་ཀྱི་ནི་ངོ་བོ་ཉིད་གྱུར་པར་བསྟན་ཏེ། དེ་བས་ན་དེ་གཉིས་སྨོས་པ་ཡིན་ནོ། །

[Block 1365]
དེ་ལྟ་བས་ན༌[^1183]གཅིག་ལ་ཡང་དེ་ལས་ཡོངས་སུ་གྱུར་ན་གསོག་འཇོག་ཉིད་དོ། །

[Block 1366]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས།

[Block 1367]
བུ་རམ་གྱི་བཏུང་བའི་སྐབས་ནས། བཙུན་པ་བཏུང་བ་བཙགས་ནས་དགུང་བདུན་པར་བྱིན་གྱིས་བརླབ་ཏུ་རུང་ངམ། ཉེ་བ༌[^1184]འཁོར་མི་རུང་ངོ་། །

[Block 1368]
བཙུན་པ་ཡུན༌[^1185]ཇི་སྲིད་ཅིག་ཏུ་གཞག་པར་འཚལ་བར་བགྱི། ཉེ་བ༌[^1186]འཁོར་ཤིན་ཏུ་སླ་ཞིང་མི་སྐྱུར༌[^1187]ལ་རང་གི་ངོ་བོ་ཉིད་མི་སྤོང་བ་དེ་སྲིད་དུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1369]
འདིར་ཞུ་བ་བྱ་བ་མ་ཡིན་པ་ཉིད་གསུངས་ཏེ། འདི་ལ་གསོག་འཇོག་ལས་གཞན་པའི་བཏུང་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་ལ་རྒྱུ་རྣམ་པར་མི་གནས་པ་དེ་བས་ན་གསོག་འཇོག་ཉིད་དུ་ཤེས་པའོ། །

[Block 1370]
བྱིན་གྱིས་བརླབ་པ་འོག་མ༌[^1188]དང་ལྷན་ཅིག་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་བྱེ་བྲག་ཏུ་བཅད་པས་བྱིན་གྱིས་བརླབས་པ་དང་། གསོག་འཇོག་གི་དུས་ལ་མ་བབ་པ་དང་ལྷན་ཅིག་ཅེས་བྱ་བར་ཤེས་པར་བྱའོ། །
--- END BLOCKS ---
