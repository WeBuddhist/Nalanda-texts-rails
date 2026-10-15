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
སྐྱ་རེངས༌[^825]ཤར་ནས་ནི་ལྟུང་བྱེད་དོ། །

[Block 1332]
བདག་པོས་བསྲུངས་པར་གྱུར་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདི་ཡང་གསུངས་པ་ཡིན་ནོ། །

[Block 1333]
གནས་ཐ་དད་པ་ཉིད་ལ་ནི་བདག་པོས་བསྲུངས་པ་ཉིད་ལ་ལྟུང་བ་མེད་པ་ཡིན་ནོ། །

[Block 1334]
གནས་གཅིག་པ་ཉིད་ལ་ནི་བདག་པོས་བསྲུངས་པ་ཉིད་ལ་ཡང་སྤྱོད་པ་ལས་བྱུང་བའི་ཆ་དང་། ལྷན་ཅིག་ཏུ་བུད་མེད་ལ་སོགས་པ་དང་འདུག་པའི་གེགས་བྱེད་པའི་བུད་མེད་དང་འབྲེལ་པའི་སྲུང༌[^826]མ་ཉིད་ལ་ཡང་ལྟུང་བ་མེད་པ་ཡིན་པས་དེའི་ཕྱིར་འདིར་བདག་པོས་བསྲུངས་པ་ཉིད་ནི་དེ་བཞིན་དུ་འདིར་ལྟུང་བས་གོ་བར་བྱེད་པའི་བློ་ལ་སྐབས་མེད་དོ། །

[Block 1335]
དེ་བས་ན་འདིར་ཡང་གནས་ཐ་དད་པ་ཉིད་ལ་བདག་པོས་བསྲུངས་པ་ཉིད་ལ་ལྟུང་བ་མེད་དོ། །

[Block 1336]
འདིར་བདག་པོས་ཞེས་སྨོས་པ་ནི་དཔེ་ཙམ་དུ་ཟད་དོ། །

[Block 1337]
རིམ་ཁང་གཞན་ལ་ནི་སྐས་སྟེང་དུ་བཏུལ་བ༌[^827]ཉིད་དོ་ཞེས་བྱ་བ་ནི། རིམ་ཁང་གི་ཁྱེར་གཞན་ལ་ནི་སྐས་སྟེང་དུ་བརྟུལ་བ་ཉིད་ཀྱང་ངོ་། །རང་གི༌[^828]ཆར་གཏོགས་པའི་སྒོ་བཅད་པས་བཅད་པ་དང་འདྲ་བར་ལྟུང་བ་འབྱིན་པ་པོ་དགེ་སློང་གིས་བསྲུངས་པ་ཉིད་གཅིག་པུར་མ་ཟད་དེ། ཚོགས་ལ་བསྲུངས་པ་ཉིད་ཀྱང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1338]
གཞན་གནས་མ་ཡིན་པ་ཉིད་ལ་ནི་ན་སྨད་དོ་ཞེས་བྱ་བ་ནི་ཉེ་འཁོར་ལ་སོགས་པ་ལས་གཞན་དུ་གྱུར་པ་གང་ཡིན་པ་འདིར་ཞུགས་པ་ཉིད་ཀྱིས་འདིར་བརྩམས་པ་ནི་གནས་མེད་པ་ཉིད་ལ་འདིར་ན་སྨད་པ་སྟེ། ཁ་ན་མ་ཐོ་བ་མེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1339]
འདིར་གནས་སུ་གྱུར་པ་ཉིད་ལ༌[^829]ནི་ཉེས་བྱས་ཡོངས་སུ་རྫོགས་པ་ཉིད་དོ། །

[Block 1340]
གཞན་ལ་ནི་ཉེས་བྱས་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1341]
ཅི་ཞིག་བྱས་ན་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་ཉལ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་ཏུ་མཚན་མོ་གསུམ་པ་ལ་ཉལ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འགལ་ཟླ་གཉིད་མ་ལོག་པ་ལ་དེ་དང་ལྷན་ཅིག་ཏུ་ཉལ་བ་བསྒྲུབ་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1342]
དེ་བས་ན་དེ་དང་ལྷན་ཅིག་གཉིད་ལོག་པ་ལ་ནི་གཉིད་ཀྱི་ཁ་ན་མ་ཐོ་བ་ཉིད་དུ་བསྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 1343]
གཅིག་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 1344]
སྤྱོད་ལམ་ནི་གཞན་གྱི༌[^830]འདིར་ལྟུང་བྱེད་དུ་རྟོགས་པར་བྱའོ། །

[Block 1345]
གཉིད་མ་ལོག་པ་ལ་གཅིག་ཏུ་བསྒྲུབ་པ་ཉིད་ཀྱིས་འདི་ལྟ་བུར་གྱུར་པ་གང་ལ་གཞན་དང་འདྲ་བ་ལྷན་ཅིག་ཉལ་བ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1346]
ཁ་ཅིག་ནི་གཞན་དུ་ཡང་དགེ་སློང་གཉིད་ལོག་པ་ཉིད༌[^831]ལ་ལྟུང་བ་མེད་དོ་ཞེས་འདོད་པ་དེ་ནི་མི་རིགས་ཏེ། འདུག་པ་ལ་ནི་སྐྱོན་མེད་པའི་ཕྱིར་དང་ཉམས་པ་མེད་པའི་ཕྱིར་ཏེ། དེ་བས་ན་འདུག་པ་ལ་བསྒྲུབ་པས་སོ། །

[Block 1347]
མཚན་མོའི་དུས་ལ་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་མཐར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྐད་ཅིག་གང་གི༌[^832]མཇུག་ཐོགས་སུ་སྐྱ་རེངས༌[^833]འཆར་བ་དེར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1348]
འདིར་གཞུང་ནི་གནས་བཞི་པོ་དག་ཏུ་སྐྱ་རེངས༌[^834]འཆར་བར་བྱེད་ཅིང་། སྐྱ་རེངས༌[^835]འཆར་ན་ལྟུང་བྱེད་དུ་འགྱུར་བ་ཁོ་ནར་གསུངས་པ་ཡིན་ནོ། །

[Block 1349]
གང་ཞིག་ཇི་ལྟར་མཐར་རོ་ཞེས་བརྗོད་ཅེ་ན། ཉེས་པ་མེད་དེ། དེའི་ཕྱིར༌[^836]སྒོ་ནས་འདི་བསྟན་པར་ནུས་པའི་ཕྱིར་རོ། །

[Block 1350]
མདུན་རོལ་དུ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་མཐའ་མ་ལས་མདུན་རོལ་དུ་གསུམ་དུ་གཏོགས་པའི་གཉིད་ལོག་པ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 1351]
ཉིན་མོ་ཐ་དད་པ་ཉིད་ཀྱང་ངོ་། །དེ་བས་ན་གཞན་དུ་ཞག་གཞན་ལ་ཉེས་བྱས་བསྐྱེད་པ་ཞེས་བྱ་བར༌[^837]རིག་པར་བྱའོ། །

[Block 1352]
ལམ་གྱིས་དུབ་པ་རྨྱ་བ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་མདུན་རོལ་དུ་ནི་གཉིད་ལོག་པ་ལ་ཉེས་པ་མེད་པ་ཉིད་ལ་འདིར་བསྒྲུབ་པའོ།[^838] །གལ་ཏེ་བསྙེན་པར་མ་རྫོགས་པ་མེད་པའི་གནས་རྙེད་པ་མེད་ན་མཐར་ནི་ཉེས་པ་ཁོ་ནར་འགྱུར་ཞེས་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 1353]
མཐར་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཡང་དེས་མདུན་རོལ་དུ་གཉིད་ལོག་པ་ཙམ་བྱས་སུ་ཟིན་ཀྱང་དེས་དུབ་པ་ལ་མཐར་ཡང་གཉིད་ལོག་པ་ལ་ཉེས་པ་མེད་དོ། །

[Block 1354]
དགེ་སློང་གིས་བྱར་མི་རུང་བ་ཡོད་ན་དེ་སྒྲུབ་པར་བྱེད་པ་དང་ལྷན་ཅིག་པའི་ནད་གཡོག་ལ་ཡང་ཞེས་བྱ་བ་ནི། དགེ་སློང་གིས་བྱར་མི་རུང་བ་བྱིན་པ་ལ་སོགས་པ་གང་ཡིན་པ་དེ་སྒྲུབ་པར་བྱེད་པའི་ཕྱིར་གང་ཞིག་དེར་འཛིན་པར་བྱེད་པར་གྱུར་པ་དེ༌[^839]ཡང་ལྷན་ཅིག་ཏུ་ཉལ་བ་ལ་མདུན་རོལ་དང་མཐར་ཡང་ཉེས་པ་མེད་དོ། །

[Block 1355]
དེར་ནད་པ་དང་ནད་གཡོག་ལ་ཉེས་པ་མེད་པ༌[^840]ཁོ་ན༌[^841]ཡིན་གྱི༌[^842]གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1356]
དགེ་ཚུལ་དང་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་ཚུལ་དང་ལྷན་ཅིག་ཉལ་བ་ལ་མདུན་རོལ་དུ་མཐར་ཡང་ཉེས་པ་མེད་དོ། །གང་ལ་ཞེ་ན། དེའི་ཕྱིར་དེ་དང་ལྡན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་ཚུལ་དང་ལྡན་པ་ལའོ། །

[Block 1357]
གནས་སྐབས་གང་གི་ཚེ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་སྡིག་ཅན་ཉེ་བར་གྱུར་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་དེ་དང་ལྡན་པ་ཐམས་ཅད་ལའམ་ཞེ་ན། དེའི་ཕྱིར་དེ་སྤྱུག་པ༌[^843]ལ་འབད་པ་བྱས་སམ་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གིས་དགེ་སློང་སྡིག་ཅན་དེ་སྤྱུག་པའི་ཕྱིར་འབད་པ་སྔར་བྱས་པའམ་བྱེད་ཅིང་དེ་ལས་ཏེ། གཞན་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1358]
བརྩོན་འགྲུས་ཇི་སྙེད་པ་བྱེད་པའི་ཕྱིར་ནུས་པ་ཉིད་དེ་སྙེད་པའི༌[^844]འབད་པ་ལ་དེར་བརྩོན་པའོ། །

[Block 1359]
དེས་མངོན་པར་འདུ་བྱས་པའི་སེམས་ཀྱིས་འཇིགས་པ་དག་ལས་བརྩམས་ཏེ། ལུས་སམ་ངག་གིས་ལྡོག་པ་ཉིད་ལ་འདིར་འབད་པ་མ་བྱས་པ་ཉིད་ནི་མ་ཡིན་ནོ། །ཅི་དུས་གང་ཡང་རུང་བ་ལ་ཉེས་པ་མེད་པ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་གནས་པར་ཁས་བླངས་ན་དུས་ཕྱི་མ་དང་སྔ་མའི་གཉིས་པ་དག་ལ་བབ་པ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕྱི་མར་ཁས་བླངས་པའི་དུས་སུ་གྱུར་པ་སྔ་མའི་གཉིས་པོ་དག་ནི་དབྱར་ཟླ་ཐ་ཆུངས༌[^845]ཉ་ནས་སྟོན་ཟླ་ར་བའི་ཉའི་བར་དུ་ཁས་བླངས་པ༌[^846]སྔ་མ་དང་ཕྱི་མ་ལ་གནས་པར་གྱུར་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1360]
དེས་ལྷག་པར་གནས་པར་མི་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ་ནི་དབྱར་གནས་པར་ཁས་བླངས་པ་ལ་ཟླ་བ་གཉིས་ལས་ལྷག་པར་གནས་པར་མི་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 1361]
ཕྱི་མར་ཁས་བླངས་པ་ལ་ད་ལྟར་བྱུང་བའི་ཕྱིར་འདིའོ། །

[Block 1362]
གནས་པར་ཁས་བླངས་པ་སྔ་མ་ཤོས་མི་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དེས་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 1363]
སྔ་མ་མི་བསྲུང་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཟླ་བ་གཉིས་པོ༌[^847]དག་གི་སྔ་རོལ་དུ་ཁས་བླངས་པ་སྔ་མ་ཤོས་མི་བསྲུང་བར་བྱ་བ་ཉིད་དོ། །

[Block 1364]
དེ་དགེ་ཚུལ་ཉེ་བར་མ་བཞག་པ་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས༌[^848]བྱ་བ་ནི་དགེ་སློང་སྡིག་ཅན་གནས་པར་གྱུར་པའི་གནས་ལ་གནས་པར་གྱུར་པའོ། །

[Block 1365]
ལམ་དུ་དགེ་ཚུལ་གཉིད་བྲོ་བས་རྨྱ་བར་གྱུར་ན་མདུན་དུ་བཏང་སྟེ་འགྲོ་བར་བྱའོ། །

[Block 1366]
གལ་ཏེ་བྲུ་བ་ཚ་བར་གྱུར་ན། དེ་ལ་ནང་པར་གྱི་དུས་སུ་ཁ་ཟས་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ལ༌[^849]ཁ་ཟས་ནང་པར་ཁྱེའུ་སུས་ཀྱི་དུས་སུ་སྦྱིན་པར་བྱའོ། །

[Block 1367]
གལ་ཏེ་དྲོ་ཀར་ཡང་ན་དེའི་ཚེ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་དྲོ་ཀར་ཡང་བཀྲེས་པར་གྱུར་ན། དེའི་ཚེ་ཡང་དེ་ལ༌[^850]དྲོ་ཟན་སྦྱིན་པར་བྱའོ། །

[Block 1368]
བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་ཉལ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1369]
བཟློག་པའི་ངོ་བོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེའི་ཐ་མར་ཞེས་བྱ་བའི་མཐར་ཇི་ལྟར་རིགས་པར་བཀའ་བསྒོ་བ་ཉེ་བར་བརྩམས་པའི་བསླབ་པའི་གཞིར་གཏོགས་པ་སྤྱིའི་ཆོ་ག་ལ་ཉེ་བར་གནས་པ་ལ་ལྟོས་ན་གང་ལ་ལྟ་བར་གྱུར་པ་མི་འདོར་བའི་ལྟུང་བྱེད་ཅེས་བྱ་བ་འདིའི་བྱེ་བྲག་བརྗོད་པ༌[^851]ཡིན་ཏེ། དེའི་ཕྱིར་ཇི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་བར་དུ་གཅོད༌[^852]པའི་ཆོས་སུ་གསུངས་པ་གང་ཡིན་པ་དེ་དག་བསྟེན་ཀྱང་བར་དུ་གཅོད་པར་མི་འགྱུར་ཏེ། དེ་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས༌[^853]བསྟན་པ་བདག་གིས་ཤེས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པར་འཇུག་པའི་ཚིག་མི་གཏོང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་ཞིག་གསུངས་པ་འཇུག་པའི་ཚིག་ཉིད་མི༌[^854]གཏོང་བ་ཞེས་བྱ་བའི༌[^855]དོན་ཏོ། །

[Block 1370]
བར་དུ་གཅོད་པའི་ཆོས་རྣམས་ནི་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་སུ་རིག་པར་བྱའོ། །
--- END BLOCKS ---
