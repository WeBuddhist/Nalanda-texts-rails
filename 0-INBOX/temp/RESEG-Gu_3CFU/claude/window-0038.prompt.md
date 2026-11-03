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
[Block 1331 [VERSE]]
བྱིན་ལེན་མ་བྱས་བཟའ་མི་བྱ། །
གསོག་འཇོག་བྱས་པ་བཟའ་མི་བྱ། །
རྗེས་སུ་མཐུན་པའི་ཆོས་དྲུག་འདི། །
དགེ་སློབ༌[^957]མ་ལ་སློབ་ཕྱིར་བཤད། །

[Block 1332]
ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་མ་ཐོབ་པར་བསྙེན་པར་རྫོགས་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ལ། འདིར་བསྙེན་པར་རྫོགས་པ་ནི་ཚངས་པར་སྤྱོད་པའོ། །

[Block 1333]
དེ་ལ་ཉེ་བར་གནས་པ་ནི་ཉེ་བར་སྐྱེ་བར༌[^958]བྱེད་པའོ། །

[Block 1334]
ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པར་བྱ་བའི་ཕྱིར༌[^959]སྡོམ་པ་ནི་ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པའོ། །

[Block 1335]
གང་གིས་དེ་མ་ཐོབ་པ་དེ་ནི་ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་མ་ཐོབ་པ་སྟེ་དེ་ལའོ། །

[Block 1336]
བསྙེན་པར་རྫོགས་པར་མི་འགྱུར་བ་ནི་གང་གི་ཕྱིར་འདི་རྣམས་ཀྱི་སྡོམ་པ་ནི་བསྙེན་པར་རྫོགས་པའི་དོན་དུ་སྟེ། ཞིང་ཉིད་དུ་ངེས་པར་བྱེད་པ་དེ་ལས་འདི་མ་ཐོབ་པར་ནི་བསྙེན་པར་རྫོགས་པ་མ་ཡིན་ནོ། །གང་གི་ཚེ་འདི་བླང་ཞེ་ན། དེའི་ཕྱིར་གསང་སྟེ་བསྟན་པའི་འོག་ཏུ་དགེ་འདུན་གྱིས་དེ་སྦྱིན་པར་བྱའོ་ཞེས༌[^960]སྨོས་ཏེ། ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་དེ་སྦྱིན་པར་བྱའོ། །

[Block 1337]
སུས་ཤེ་ན་དེའི་ཕྱིར། དགེ་འདུན་གྱིས་ཞེས་བྱ་བ་སྨོས་ཏེ། སྐབས་ཡིན་པའི་ཕྱིར་དགེ་སློང་མའི་དགེ་འདུན་གྱིས༌[^961]སྦྱིན་པར་ཤེས་པར་བྱའོ། །ཅི་ཞིག་འདི་ཙམ་ཉིད་ཀྱིས་འདི་སྦྱིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་བར་ཆད་དྲིས༌[^962]སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལྟར་ན་འདི་ལ་བར་ཆད་དྲི་བ་ལན་གསུམ་དུ་འགྱུར་ཏེ། གཅིག་ནི་དགེ་སློང་མས་གསང་སྟེ་སྟོན་པས་བཀར་ཏེ་དྲིའོ།[^963] །དགེ་སློང་མའི་དགེ་འདུན་འབའ་ཞིག་གི་དབུས་སུ་ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པ་སྡོམ་པའི་ཡན་ལག་ཏུ་གྱུར་པ་ནི་གཉིས་པའོ། །

[Block 1338]
གཉིས་ཀའི་མདུན་གྱི་དབུས་སུ་བསྙེན་པར་རྫོགས་པར་གསོལ་བ་ལ་བསྙེན་པར་རྫོགས་པའི་ཡན་ལག་ཏུ་གྱུར་པ་ནི་གསུམ་པའོ། །

[Block 1339]
འདིར་གསོལ་བ་ནི་གསོལ་བར་བྱེད་པ་ལའོ། །

[Block 1340]
ལས་སུ་བསྐོ་བ་ཞེས་བྱ་བ་འདི་ལས་ཐོབ་པ་དེ་བས་ན་གསོལ་བ་འདི་ལ་ཡང་བསྐོ་བ་རིག་པའི་ངོ་བོ་ཡིན་ཏེ། དེའི་ཕྱིར་གསོལ་བ་བྱས་ནས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་ཡང་གསོལ་ནས་སྦྱིན་པར་བྱེད་པའི་ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་འདི་མ་གསོལ་བ་ལ་ནི་མི་སྦྱིན་པའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1341]
ཆོས་གོས་དག་ནི་ལྔ་ཉིད་དོ། །ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་ལ་ནི་ཆོས་གོས་གསུམ་ཐུན་མོང་ཡིན་ཏེ། ཤིང་ང་དཔུང་ཆད་དང་རྔུལ་གཟན་ལྷག་པར་རོ། །

[Block 1342]
གནས་རྣམས་ལ་ཤིང་དྲུང་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ལ། ཤིང་དྲུང་ཉིད་མ་གཏོགས་པ་གནས་གཞན་གསུམ་པོ་ནི་དེའི་གནས་སོ། །

[Block 1343]
ལྟུང་བར་འགྱུར་བ་ཉིད་རྣམས་ལ་བརྒྱད་ཉིད་དོ་ཞེས་བྱ་བ་ནི།

[Block 1344 [VERSE]]
རེག་པ་དང་ནི་ལུས་བཀན་དང་། །
འཆབ་པ་དང་ནི་བཟློག་པའོ། །

[Block 1345]
ཞེས་བྱ་བ་བཞི་པོ་རྣམས་ལྷག་པ་ཡིན་ནོ། །

[Block 1346]
ལྕི་བའི་ཆོས་རྣམས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ལྕི་བའི་ཆོས་བརྒྱད་པོ་རྣམས་བརྗོད་པར་བྱ་སྟེ། དེ་རྣམས་ཀྱང་། དགེ་སློང་རྣམས་ལས་བསྙེན་པར་རྫོགས་པ་དང་།

[Block 1347 [VERSE]]
གཉེན་པོའི་ཚོགས་དང་གདམས་ངག་ཡོངས་ཚོལ་དང་། །
དགེ་སློང་མེད་པར་གནས་པར་བྱེད་པ་དང་། །
གང་དུ་ཡང་ནི་དབྱར་གནས་ཁས་ལེན་དང་། །
རྒུད་པ་རྣམས་ལ་དགེ་སློང་བསྐུལ་བ་དང་། །

[Block 1348 [VERSE]]
ཁྲོ་བ་མེད་དང་གསར་ཞུགས་ལ་ཕྱག་འཚལ། །
གཉིས་ཀའི་ཚོགས་ལས་ཐོབ་བྱ་མིན་པ་དང་། །
དགག་དབྱེ་ཞེས་བྱ་ལྕི་བའི་ཆོས་རྣམས་སོ། །

[Block 1349]
དུས་གང་ལ༌[^964]བརྗོད་པ་ཞེ་ན། དེའི་ཕྱིར་ལྟུང་བར་འགྱུར་བ་དང་། དགེ་སྦྱོང་བྱེད་པའི་བར་སྐབས་སུའོ། །

[Block 1350]
བཀོལ་བ་དྲུག་གོ༌[^965]ཞེས་བྱ་བ་ནི་སྔོན་རབ་ཏུ་བྱུང་བ་ཞེས་བྱ་བ་འདི་ནས་ཇི་སྲིད་དུ་བཀོལ་བ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱི་མིང་ཅན་གང་ཞིག་ཁྱོད་ནི་མ་ཡིན་ནམ་ཞེས་བྱ་བ་རབ་ཏུ་བྱུང་བའི་དོན་དུ་ཉེ་བར་འོངས་པ་ལ་དྲི་བར་བྱ་སྟེ། [^966]བསྙེན་པར་རྫོགས་པར་བྱེད་པ་པོ་རྣམས་ཀྱིས་ཀྱང་རབ་ཏུ་དབྱུང་བར་བྱ་བ་དང་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1351]
དེ་ལ་སྐྱེ་བའི་ཆོས་ཉིད་མེད་པར་ཡང་འདྲའོ་ཞེས་བྱ་བ་ནི་འདིར་ཆོ་ག་དྲུག་པོ་འདི་གཏོགས་པར་བྱའོ། །

[Block 1352]
རྣམ་པ་དེ་ལྟ་བུའི་རྟགས་ཅན་ནི་བསྙིལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ལ་དབང་དུ་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་བརྗོད་པར་བྱ་བ་ཡིན་ཏེ། སླར་འདིར་ཡང་དག་པར༌[^967]རིག་པར་བྱའོ། །

[Block 1353]
དྲུག་པོ་དེ་དག་གང་ཞེ་ན། དེའི་ཕྱིར་མཚན་གཉིས་པའོ། །

[Block 1354]
གླེ་འདམས་པའོ། །

[Block 1355]
རྟག་ཏུ་ཟླ་མཚན་འཛག་པའོ། །

[Block 1356]
ཟླ་མཚན་མི་འཛག་པའོ། །

[Block 1357]
མཚན་མ་ཙམ་ཡོད་པའོ། །

[Block 1358]
མཚན་མ་ཙམ་དུ་གྱུར་པའི་མཚན་ཡོད་པ་ནི་ཞེས་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་མཚན་མ་ཙམ་དུ་གྱུར་པའི་མོ་མཚན་ཡོད་པ་དེ་ནི་མཚན་མ་ཡོད་པ་དེ་ཞེས་བྱ་བ་སྟེ་མིང་དེ་སྐད་གདགས་སོ། །

[Block 1359]
སྔོན་རབ་ཏུ་བྱུང་བའོ་ཞེས་བྱ་བ་ནི་ཁྱོད༌[^968]མཚན་གཉིས་པ་མ་ཡིན་ནམ་ཞེས་བྱ་བ་ནས་ཇི་སྲིད་དུ་ཁྱོད་ནི་སྔོན་རབ་ཏུ་བྱུང་བ་མ་ཡིན་ནམ་ཞེས་བྱ་བའི་བར་ནི་རབ་ཏུ་བྱུང་བའི་དོན་དུ་ཉེ་བར་འོངས་པ་ལ་དྲི་བར༌[^969]བྱའོ། །

[Block 1360]
ཇི་སྲིད་འདི་ལ་སྐྱེ་བའི་ཆོས་ཉིད་མེད་པ་ཞེས་བྱ་བ་འདིར་ཚུལ་འདི་རྟོགས་པར་བྱའོ། །

[Block 1361]
རབ་ཏུ་བྱུང་བའི་གཞི་ཕྲན་ཚེགས་ལ་སོགས་པའི་སྐབས་སོ།། །།

[Block 1362]
མི་མ་ཡིན་པའི་འགྲོ་བ་པ་དང་བྱང་གི་སྒྲ་མི་སྙན་པ་གཉིས་ནི་སྡོམ་པའི་ཞིང་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མིའི་འགྲོ་བ་པ་ལས་གཞན་པའི་འགྲོ་བ་གཞན་ལས་སྐྱེས་པ་དང་། མིའི་འགྲོ་བ་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་བྱང་གི་སྒྲ་མི་སྙན་པ་ནི་སྡོམ་པའི་ཞིང་ཉིད་མ་ཡིན་ཏེ། དེ་གཉིས་ལ་སྡོམ་པ་མི་སྐྱེའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1363]
མཚན་ལན་གསུམ་དུ་གྱུར་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྡོམ་པའི་ཞིང་ཉིད་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 1364]
གང་ཞིག་མཚན་ལན་གསུམ་དུ་གྱུར་པ་དེ་ལ་སྡོམ་པ་མི་སྐྱེའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1365]
དང་པོ་གཉིས་ལ་ནི་མི་ཉམས་སོ་ཞེས་བྱ་བ་ནི་སྡོམ་པ་སྟེ་མཚན་གྱུར་པ་དང་པོ་དང་གཉིས་པ་ལ་ནི་སྡོམ་པ་ཉམས་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1366]
ཕྲན་ཚེགས་ལས་ཆོ་ག་གཉིས་པ་འདི་འདྲ་བ་ནས༌[^970]དྲངས་པའོ། །

[Block 1367]
ལེན་པ་ཉིད་ན་ཡང་སྐྱེའོ་ཞེས་བྱ་བ་ནི་སྡོམ་པ་ཡང་དག་པར་ལེན་པ་ཉིད་ལ་དེའི་ཚེ་ན་མཚན་གྱུར་ན་ཡང་སྡོམ་པ་སྐྱེ་བ་ཉིད་ཡིན་ནོ། །

[Block 1368]
འདིར་གཞུང་ནི་བསྙེན་པར་རྫོགས་པར་འཚལ་བའི་མཚན་གྱུར་ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱི་འམ་བསྙེན་པར་མ་རྫོགས་ཞེས་བགྱི། བཀའ་སྩལ་པ། བསྙེན་པར་རྫོགས་ཞེས་བྱ་སྟེ། དགེ་སློང་མས་ནི་དགེ་སློང་རྣམས་ལས་བསྙེན་པར་རྫོགས་པ་དགེ་སློང་མའི་དངོས་པོ་ཡོངས་སུ་བཙལ་བར་བྱ་བའི་ཕྱིར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1369]
འདི༌[^971]ཕོའི་མཚན་གྱུར་པ་ནི་དཔེ་ཙམ་དུ་ཟད་དོ། །

[Block 1370]
གཞན་དུ་ཆོ་ག་འདི་ལ་ཤིན་ཏུ་དོགས་པ་དང་བྲལ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །
--- END BLOCKS ---
