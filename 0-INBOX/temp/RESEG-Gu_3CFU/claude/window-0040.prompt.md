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
[Block 1401]
འདིར་མཚན་དུག་མའི་གཞུང་ནི། རེ་ཞིག་མཚན་དུག་མ་ཞིག་བཙུན་པ་རྣམས་ཀྱིས་བསྙེན་པར་རྫོགས་པར་བགྱིད་ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱིའམ་བསྙེན་པར་མ་རྫོགས་ཞེས་བགྱི། བཀའ་སྩལ་པ། བསྙེན་པར༌[^996]རྫོགས་ཞེས་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་རྣམས་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1402]
མཚན་དུག་མ་ནི་སྔར་གང་དང་མཉམ་པར་སྦྱོར་བས་སྐྱེས་པ་འཆི་བའོ། །

[Block 1403]
རྒྱུ་ལས་བཟློག་པའི་ཆད་པ་ཁས་མི་ལེན་པ་གནས་ནས་ཕྱུང་བ་ལ་ཡང་མི་སྐྱེའོ་ཞེས་བྱ་བ་ནི་ལྟ་བ་དང་བཅས་པ་དྲི་བ༌[^997]དང་བྲལ་བ་ཞེས་བྱ་བའི་བསམ་པ་ཅན་ལ་སྡོམ་པ་སྐྱེའོ། །

[Block 1404]
དེ་བས་ན་ལྟུང་བ་མ་མཐོང་བ་ལ་སོགས་པའི་རྒྱུ་གང་གིས་གནས་ནས་དབྱུང་བའི་ལས་བྱས་པ་རྒྱུ་དེ་ལས་བཟློག་པ༌[^998]ལ་སོགས་པ་དེ་ཁས་མི་ལེན་པ་ལ་ཡང་སྡོམ་པ་མི་སྐྱེའོ། །

[Block 1405]
འདིར་གནས་ནས་ཕྱུང་བ་སྨོས་པ་ནི་དཔེ་ཙམ་དུ་ཟད་ཀྱི། སྨད་པ་ཐམས་ཅད་ལ་ཡང་ཆོ་ག་འདི་ཡིན་ཏེ། འཐབ་མོ་བྱེད་པ་ལ་སོགས་པའི་བསམ་པ་ཅན་ལ་ཡང་མི་བཟློག་པའི་བསམ་པ་ཅན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1406]
ཚིག༌[^999]སྔ་མ་མེད་པ་ཉིད་ལ་ནི་ཉེས་བྱས་ཙམ་དུ་ཟད་དོ། །

[Block 1407]
དགེ་བསྙེན་ཉིད་མེད་པར་དགེ་ཚུལ་ཉིད་དུ་ཁས་ལེན་པ་དང་དགེ་ཚུལ་ཉིད་མེད་པར་དགེ་སློང་ཉིད་ཁས་ལེན་པར་བྱེད་ན་ཉེས་བྱས་ཙམ་དུ་འགྱུར་གྱི་སྡོམ་པ་མི་སྐྱེ་བར་ནི་མི་འགྱུར་རོ། །

[Block 1408]
འདིར་གཞུང་ནི། ཁྱིམ་པ་རབ་ཏུ་མ་བྱུང་བ་ཞིག་བསྙེན་པར་རྫོགས་པར་བགྱིད་ན། བསྙེན་པར་རྫོགས་ཞེས་བགྱིའམ་བསྙེན་པར་མ་རྫོགས་ཞེས་བགྱི། བཀའ་སྩལ་པ། ཉེ་བ་འཁོར་བསྙེན་པར་རྫོགས་ཞེས་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་པོ་རྣམས་ལ་ནི་ཉེས་བྱས་ཀྱི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1409]
མཁན་པོར༌[^1000]མ་གསོལ་བ་ལ་ཡང་ངོ་། །བར་ཆད་མ་དྲིས་པར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་གཉིས་ཀ་ལ་ཡང་ཉེས་བྱས་ཡིན་ཏེ། སྡོམ་པ་མི་སྐྱེ་བ་ནི་མ་ཡིན་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 1410]
དེ་མེད་པར་ཁས་ལེན་པ་ལ་སྦྱིན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ལ། མེད་པར་ཞེས་བྱ་བ་ནི་ཡོད་པར་གྱུར་པ་མ་ཡིན་པ་ལའོ། །

[Block 1411]
ཡང་དག་པར་ལེན་པ་པོས་བདག་བར་ཆད་ཡོད་དོ་ཞེས་བྱ་བ་ཁས་བླངས་ན་སྡོམ་པ་འབོགས་པ་ལ་ཉེས་བྱས་ཙམ་ཡིན་གྱི་མི་སྐྱེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 1412]
འདིར་གཞུང་ནི་གླེང་གཞི་རྣམས་ལས།

[Block 1413]
བཙུན་པ་རེ་ཞིག་བར་ཆད་ཀྱི་ཆོས་རྣམས་དང་ལྡན་ནོ་ཞེས་མཆི་བ་ཞིག་བསྙེན་པར་རྫོགས་པར་བགྱིད་ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱིའམ་མ་རྫོགས་ཞེས་བགྱི། བཀའ་སྩལ་པ། ཉེ་བ་འཁོར་བསྙེན་པར་རྫོགས་ཞེས་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་པོ་རྣམས་ལ་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 1414]
དེ་བས་ན་གང་དུ་བར་ཆོད་མངོན་པར་འདོད་པས་རྣམ་པར་གནས་ཏེ། རྣམ་པ་གང་ཞིག་ལ་བདག་ནི་བསྙེན་པར་རྫོགས་པའོ། །

[Block 1415]
སྐྱེས་པ་འདྲ་བའི་བུད་མེད་ཉིད་དང་། བུད་མེད་འདྲ་བའི་སྐྱེས་པ་ཉིད་མཚན་གྱི་རྣམ་པ་གཞན་མ་ཡིན་པ་ལ་ཡང༌[^1001]ཞེས་བྱ་བ་འདིར་སྡོམ་པ་མི་སྐྱེ་བ་སྟེ་ཞེས་བྱ་བ་དེ་ལ་འདི་རབ་ཏུ་བསྟན་ཏེ་མཚན་རྣམ་པ་གཞན་ཉིད་ཀྱི་ཕྱིར་འདིར་སྐྱེ་བར་མི་འགྱུར་རོ། །

[Block 1416]
དེ་ཡང་འདིར་མི་འགྱུར་ཏེ། དེ་ནི་ལག་རྡུམ་ལ་སོགས་པ་འཕངས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་སྐྱེས་པ་འདི་ལ་བུད་མེད་ཀྱི་རྣམ་པ་གཞན་ལ་ལག་རྡུམ་དང་རྐང་རྡུམ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^1002]འཕངས་པ་ཉིད་ཀྱི་ཕྱིར་ཉེས་བྱས་ཙམ་དུ་ཟད་དོ་ཞེས་བྱ་བ་བརྗོད་པར་ཟད་དོ། །

[Block 1417]
སྡིག་སྡིག་ལྟ་བུའི་མཚན་ཉིད་ཅན་དང་གླིང་གཞན་ནས་སྐྱེས་པའི་ཚུལ་བྱད་མི་འདྲ་བ་གཉིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་འདི་དག་ལ་ཡང་ལག་རྡུམ་ལ་སོགས་པས་འཕངས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1418]
སྡིག་སྡིག་ལྟ་བུའི་མཚན་ཉིད་ཅན་གྱི་གཞུང་ནི། བཙུན་པ་སྡིག་སྡིག་ལྟ་བུའི་མཚན་ཉིད་ཅན་བསྙེན་པར་རྫོགས་པར་བགྱིད་ན་ཞེས་བྱ་བ་ནས་ཇི་སྲིད་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་པོ་དགེ་སློང་རྣམས་ལ་ཉེས་བྱས་ཀྱི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1419]
[^1003]གླིང་གཞན་ནས་སྐྱེས་པའི་གཞུང་ཡང་བཙུན་པ་འཛམ་བུ་གླིང་པའི་དགེ་སློང་རྣམས་ཀྱིས་ཤར་གྱི་ལུས་འཕགས་པོ་ཞིག་བསྙེན་པར་རྫོགས་པར་བགྱིད་ན་བསྙེན་པར་རྫོགས༌[^1004]ཞེས་བགྱིའམ། ཇི་སྲིད་དུ་ཉེ་བ་འཁོར་བསྙེན་པར་རྫོགས་ཞེས་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་པོ་རྣམས་ནི་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་དང་། དེ་བཞིན་དུ་རྒྱས་པར་འཁོར་ལོ་བཞིན་དུ་སྦྱར་བ་གསུམ་པ་ཡིན་ནོ། །

[Block 1420]
དབྱིབས་དང་ཚད་དང་གནས་སྐབས་ཀྱི་དབྱེ་བ་མི་རྣམས་ཀྱི་གླིང་གང་ལ་དེ་ཙམ་གསལ་བའི༌[^1005]གཙོ་བོ་འདིར་གླིང་གི་ཚིག་ཏུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1421]
འདིར་ནི་ཚུལ་བྱད་ཀྱི་ཚིག་གིས་འདི་ཁྱད་པར་དུ་བྱས་ཏེ་གདོང་ལ་སོགས་པའི་དབྱེ་བ་ཡང་འདིར་ཚུལ་བྱད་མི་འདྲ་བ་ལ་མངོན་པར༌[^1006]འདོད་དོ། །

[Block 1422]
དེ་ལྟར་ན་ཡང་གླིང་གཅིག་པ་རྣམས་ལ་ཡང་རའི་གདོང་དང་རྣ་བ་འཕྱང་བ་ལ་སོགས་པ་རྣམས་ལ༌[^1007]གསལ་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 1423]
སེན་མོ་གཅིག་པ་དང་ལག་པ་འཇས་ཏེ་ལྟེབས་པ་དང་། གཞོགས༌[^1008]ཕྱེད་འཇས་པ་དང་། མགོ་སྨྱུང་དང་སྐྲ་སྒྲ་སྒྲེ་ཅན་དང་། སྒུར་པོ་དང་དགྱེ་བོ་དང་དགྱེ་སྒུར་གྱུར་པ་དང་སེན་མོ་དྲུག་པ་དང་འབྱར་བ་དང་མེད་པ་དང་། མིག་རྫི་མ་ནང་དུ་ཟུག་པ་དང་ནེའུ་ལེའི་ལྟ་བུ་དང་འུག་པའི་ལྟ་བུ་དང་ཕྱིན་ཅི་ལོག་པ་དང་བར་འཛིངས་པ་དང་རློ་བ༌[^1009]དང་གླེའོ༌[^1010]དང་ཟླུམ་པོ་དང་མིག་པོ་ཆེ་འཛེར༌[^1011]ཅན་དང་ཤུ་བ་ཅན་དང་འབྲུམ་ཅན་དང་། རྣ་བ་སེར་བ་དང་དཀར་བ་དང་དམར་བ་དང་སྦུབས་ཅན་དང་། ཁྱི་རྔོ་གཡའ་བ་དང་། འཕུངས་པ་དང་། ཆེ་བ་དང་རླིག་པའི་ནང་དུ་མཚན་ནུབ་པ་དང་། གླེན་པ་དང་། ལྕེ་མེད་པ་དང་། རྐང་ལག་གཅིག་པ་དང་།[^1012] སྐྲ་སྔོན་དང་མགོ་གླང་པོ་ཆེའི་ལྟ་བུ་དང་། རྟའི་ལྟ་བུ་དང་ཁྱིའི་ལྟ་བུ་དང་བ་གླང༌[^1013]གི་ལྟ་བུ་དང་ལུག་གི་ལྟ་བུ་དང་རི་དགས་ཀྱི་ལྟ་བུ་དང་ཉའི་ལྟ་བུ་དང་སྦྲུལ་གྱི་ལྟ་བུ་དང་། རིང་བ་དང་མང་བ་དང་། མགུལ་ཏ་ལ༌[^1014]ལྟ་བུ་དང་། སྐྲངས་པ་དང་སྤྱོད་ལམ་གྱིས་དུབ་པ་དེ་དག་ལས་མིན་པ་རྣམས་སོ། །

[Block 1424]
གཞན་དག་ནི་ན་བས་སོ་ཞེས་བྱ་བ་ནི་སེན་མོ་གཅིག་པ་ལ་སོགས་པ་རྫོད་པར༌[^1015]བྱེད་པ་རྣམས་ལ་ལག་རྡུམ་ལ་སོགས་པ་དག་གིས་འཕངས་པ་ཉིད་དེ་གཞན་དག་གནོད་པར༌[^1016]བྱེད་པ་རྣམས་ནི་ན་བ་སྟེ། ཁྱོད་ནད་པ༌[^1017]ཡིན་ནམ་ཞེས་བྱ་བ་འདིས་འཕངས་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1425]
སེན་མོ་གཅིག་པ་ནི་གང་ལ་སེན་མོ་གཅིག་པ་ཁོ་ན་ཡོད་པའོ། །

[Block 1426]
ལག་པ་འཇས་ཏེ་ལྟེབས་པ་ནི་གང་གི་ལུས་ཀྱི་ཡན་ལག་རྒྱ་བལྟབས་པ༌[^1018]འདྲ་བའོ། །

[Block 1427]
གཞོགས་ཕྱེད་འཇས་པ་ནི་གང་གི་གཞོགས་ཕྱེད་བསྐམས་པའོ། །

[Block 1428]
མགོ་སྨྱུང་ཞེས་བྱ་བ་ནི་གང་གི་མགོ་མཚན་གྱི་རྣམ་པ་འདྲ་བའོ། །

[Block 1429]
སྐྲ་སྒྲ་སྒྲེ་ཅན་ནི་གང་གི་སྐྲ་སྨྱོན་ཐབས་མཁན་གྱི་ལྟར་བར་བར་དུ་འཛིངས་པར་གནས་པའི་སྐྲའོ། །

[Block 1430]
སྒུར་པོ་དང་དགྱེ་བོ༌[^1019]དང་དགྱེ་སྒུར་གྱུར་པ༌[^1020]ཞེས་བྱ་བ་ནི་དགྱེ་སྒུའི་སྒྲ་གསུམ་ཆར་ལ་སོ་སོར་ཁྱབ་ཅིང་རྫོགས་པའོ། །

[Block 1431]
ནང་དུ་སྒུར་བ་དང་ཕྱིར་དགྱེ་བ་དང་། མདུན་རྒྱབ་ཏུ་སྒུར་བ་ཞེས་བྱ་བ་ནི་དེ་གཞན་དུ་གསུངས་ཏེ། ཞར་བ་སོར་གདུབ་སྒུར་མིའུ་ཐུང་། །ཞེས་སྨོས་སྟེ། འདིའི་རབ་ཏུ་དབྱེ་བ་བསྟན་པའི་དོན་དུའོ། །

[Block 1432]
སོར་མོ་དྲུག་པ་དང་འབྱར་བ་དང་མེད་པ་ཞེས་བྱ་བ་ནི། སོར་མོ་ཞེས་བྱ་བའི་སྒྲ་ནི་སོ་སོར་ཡོངས་སུ་རྫོགས་པ་སྟེ། སོར་མོ་དྲུག་པ་དང་། སོར་མོ་འབྱར་བ་དང་། སོར་མོ་མེད་པ་ཞེས་བྱ་བའོ། །

[Block 1433]
སོར་མོ་དྲུག་པ་ཉིད་དང་། སོར་མོ་འབྱར་བ་ཉིད་དང་། སོར་མོ་མེད་པར་གྱུར་པ་ཉིད་ཙམ་སོར་མོའི་གདེངས་ཀའི་ལག་པ་ཅན་ཏེ། འདིར་སོར་མོ་འབྱར་བ་ཉིད་ཀྱི༌[^1021]ཁོངས་སུ་བསྡུ་བའོ། །

[Block 1434]
མིག་གི་རྫི་མ་ནང་དུ་ཟུག་པ་དང་ནེའུ་ལེ་ལྟ་བུ་དང་འུག་པའི་ལྟ་བུ་དང་། ཕྱིན་ཅི་ལོག་པ་དང་བར་འཛིངས་པ་ཅན་དང་། རློ་བ༌[^1022]དང་གླེའོ་དང་ཟླུམ་པོ་ཞེས་བྱ་བ་ནི་ཡང་མིག་ཅེས་པའི་སྒྲ་སོ་སོར་སྦྱར་ཏེ། མིག་རྫི་མ་ནང་དུ་ཟུག་པ་དང་། མིག་ནེའུ་ལེ་ལྟ་བུ་དང་། མིག་འུག་པའི་ལྟ་བུ་དང་། མིག་ཕྱིན་ཅི་ལོག་པ་དང་། མིག་བར་འཛིངས་པ་དང་། མིག་རློ་བ༌[^1023]དང་། མིག་གླེའོ༌[^1024]དང་། མིག་ཟླུམ་པོའོ། །

[Block 1435]
མིག་གི་རྫི་མ་ནང་དུ་འཛུག་པ༌[^1025]ཞེས་བྱ་བ་ནི་གང་གི༌[^1026]མིག་གི་ནང་གི་པགས་པའི་རིམ་པ་ལ་རྫི་མ་ཡོད་པའོ། །

[Block 1436]
མིག་ནེའུ་ལེའི་ལྟ་བུ་ཞེས་བྱ་བ་ནི་གང་གི་མིག་ནེའུ་ལེའི་མིག་ལྟ་བུའོ། །

[Block 1437]
མིག་འུག་པའི་ལྟ་བུ་ཞེས་བྱ་བ་ནི་གང་གི་མིག་འུག་པའི་ལྟ་བུའོ། །

[Block 1438]
ཡང་ན་མིག་སེར་སྐྱ་བ་ལ་ཟླུམ་པའི་ཕྱིར་སྲིན་པོའི་མིག་འདྲ་བའོ། །

[Block 1439]
མིག་ཕྱིན་ཅི་ལོག་ཅེས་བྱ་བ་ནི་གང་གི་གྲྭ་ལོགས་ཀྱི་ཟུར་གང་ཡིན་པ་དེ་ནི་སྣ་ལོགས་ལ་འདུག་ལ་སྣ་ལོགས་ཀྱི་ཟུར་གང་ཡིན་པ་དེ་ནི་གྲྭ་ལོགས་ན་འདུག་པའོ། །

[Block 1440]
མིག་བར་འཛིངས་པ་ནི་གང་གི་སྣ་གོང་གཏན་མེད་ལ་མིག་གཡས་གཡོན་འབྲེལ་བའོ། །
--- END BLOCKS ---
