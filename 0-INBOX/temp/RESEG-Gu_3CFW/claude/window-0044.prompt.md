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
[Block 1541]
མཇུག་ཏུ་ཁྲུས་བྱའོ། །

[Block 1542]
གོས་དག་གི་དྲི་ནི་བཀྲུ་བ་དང་། དུ་བ་དག་གིས་བསལ༌[^1331]ལོ། །

[Block 1543]
རུང་བ་ཉིད་དུ་བྱིན་གྱིས་བརླབས་པར་བཙོས་པ་དང་གནས་པ་དག་ནི་ཕྱི་རོལ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་དཔེར་ན་དགེ་སློང་གིས་གནས་ཉེན་ཀོར༌[^1332]འདོམ་གང་དང་བཅས་པ་ནས་ཕྱི་རོལ་དུ་གྱུར་པའི་བཙོས་པ་དང་གནས་པ་དག་གིས་ཟས་ལ་རྟེན་ཉིད་དུ་འགྲོ་ཞིང་མི་རུང་བ་ཉིད་བྱེད་པ་པོ་མ་ཡིན་པའི་ཟས་དེ་ལ་དེ་བཞིན་དུ་རུང་བ་ཉིད་དུ་བྱིན་གྱིས་བརླབ་པའོ། །

[Block 1544]
དེར་ཡང་ཉེས་པ་དེ་དག་མི་འབྱུང༌[^1333]བ་ཉིད་བྱིན་གྱིས་བརླབས་པ༌[^1334]ལས་གསུངས་སོ། །

[Block 1545]
འདི་བྱེད་པར་རིགས་པ་མ་ཡིན་པའམ། འོན་ཏེ་ཡིན་སྙམ་པ་དེ་བསྟན་པའི་ཕྱིར། བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 1546]
ཤིང་དྲུང་དང་གླང་པོ་ཆེའི་ར་བ་དང་། མུ་སྟེགས་ཅན་གྱི་འདུག་གནས་དང་། རྒྱལ་པོའི་ཕོ་བྲང་ས༌[^1335]དང་། དགེ་སློང་མའི་དབྱར་ཁང་དང་། གཙུག་ལག་ཁང་གི་བང་རིམ་དང་། སྒོ་ཁང་དང་། ཁྱམས་དང་། བསྲོ་ཁང་དང་། དཔོང༌[^1336]སའི་ར་བ་དག་ཏུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་པར་བྱ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1547]
གཏུམ་ཕུག༌[^1337]ཅན་དང་བསྙོན་ཐབས་མཁན་དང་། ཟིལ་གྱིས་གནོན་པར་བྱེད་པ་དང་། ཁང་པ་དང་། ཁྱམས་སུ་མི་བྱེད་པ་དང་། དོན་ཉམས་པ་དང་གུས་པ་ཉམས་པ་ཞེས་བྱ་བ་དེ་རྣམས་ཡོངས་སུ་སྤང་བའི་ཕྱིར་དེ་རྣམས་འདིས་དགག༌[^1338]པ་སྟེ་བསྒྲུབ་པ་ལ་སོགས་པ་ལ༌[^1339]ཡང་ངོ་། །ཁ་ཅིག་ལས་བླ་གབ་མེད་པ་དང་། མེ་ཁང་དང་། མཆོད་རྟེན་གྱི་གཞི་དང་། ཁྱིམ་བདག་གི༌[^1340]ས་གཞི་ཡང་ཞེས་བྱ་བ་ནི། གཞུང་ཁ་ཅིག་ལས་འདི་རྣམས་དང་སྔར་སྨོས་པ་དག་ཏུ་རུང་བའི་ཁང་པ་བྱིན་གྱིས་བརླབ་པར༌[^1341]མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་འདོད་པའོ། །

[Block 1548]
དེར་གཡོས་དང་བཙོ་བ༌[^1342]ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ལ་དེར་ཞེས་བྱ་བ་ནི་ཤིང་དྲུང་ལ་སོགས་པ་དང་བླ་གབ་མེད་པ་དེར་རོ། །

[Block 1549]
ཀུན་དུ་སྤྱོད་པ་འདི་ནི་ཁྱིམ་པ་དང་འདྲ་བ་སྟེ། གཡོས་དང་བཙོ་བ༌[^1343]བྱེད་པ༌[^1344]དེའི་ཕྱིར་ཤིན་ཏུ་དབེན་པར་འདི་བྱ་བར་རིགས་པ༌[^1345]ཡིན་ནོ། །

[Block 1550]
འདིར་མ་སྦས་པར་གནས་པས༌[^1346]མི་བྱ་བར༌[^1347]རབ་ཏུ་བྱུང་བའི་ཕམ་པར་གྱུར་པའི་དོན་འདིས་གཞན་རྣམས་ལ་ཡང་འགྱུར་རོ། །

[Block 1551]
ཤིང་དྲུང་ལ་སོགས་པ་རྣམས་ལ་འདི་ཤིན་ཏུ་མ་སྦས་པ་ཉིད་དང་། གུས་པ་ཉམས་པའི་མཐའ་མ་ཅན་གྱི་ཉེས་པ་རྣམས་ལ་འགའ་ཞིག་ཏུ་ཞེས་བྱ་བ་ལས་གཡོས་པ་དང་བཙོ་བ་དག་ལས༌[^1348]འདི་རྣམས་བཀག་པ་དང་། ཚོས་པའི་བྱི་དོར་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ལ། ཚོས་པའི་བྱི་དོར་ནི་ཚོས་པའི་བྱི་དོར་རོ། །

[Block 1552]
དེ་མི་བྱ་བ༌[^1349]སུམ་ཆ་བངས་པ་ན་ཚོས་པ་ཡིན་ཏེ། ཚོས་པ་དེ་དག་དགེ་སློང་རང་གིས་བྱི་དོར་བྱ་བ་ནི་ཤིང་དྲུང་ལ་སོགས་པའི་གནས་དེ་རྣམས་སུ་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1553]
དེ་ནི་ཀློག་པ་མ་ཡིན་ཏེ། ཤིན་ཏུ་སྡིག་པ་བསྲུང་བ་ལ་སོགས་པ་དེ་ལྟ་བས་ན་ཉེ་བར་བསྡུས་པའོ། །

[Block 1554]
འདི་ལ་དུས་བཞི་ཡོད་དོ་ཞེས་བྱ་བ་ནི་འདིར་རུང་བའི་ཁང་པ་བྱིན་གྱིས་བརླབ་པ་འདི་ལ་དུས་བཞི་ཡོད་པའོ། །

[Block 1555]
དེ་དག་ཀྱང་གང་ཞེ་ན།

[Block 1556]
དང་པོ་སོ་ཕག་འགྲེམས༌[^1350]པའོ། །

[Block 1557]
ཕྱིས་ལས་སར་པ་དང་བཅས་པ་ཉིད་དོ་ཞེས་བྱ་བ༌[^1351]ནི་དང་པོ་སོ་ཕག་བཀྲམ་པའི་འོག་ཏུ་རུང་བའི་ཁང་པ་བྱིན་གྱིས་བརླབ་པ་ནི་དུས་གཅིག་གོ། །

[Block 1558]
དང་པོ་སོ་ཕག་བཀྲམ་པའི་འོག་ཏུ་དེང་ཕྱིན་ཆད་ནས་ཇི་སྲིད་དུ་ལས་སར་པ་ཡོད་པ་ཉིད་འདི་ནི་གཞན་ནོ། །

[Block 1559]
གཞན་གྱི་ཚེ་དགེ་སློང་གནས་པ་ཉིད་དང་མ་བྲལ་བའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གནས་པ་ཉིད་དང་མ་བྲལ་བ་འདི་ལ་ཡོད་པས་ན་འདི་ནི་དགེ་སློང་གནས་པ་ཉིད་དང་མ་བྲལ་བའོ། །

[Block 1560]
དེའི་དངོས་པོ་ནི་དེ་ཉིད་དོ། །

[Block 1561]
དེ་ལས་སར་པ་ཉིད་ཀྱི་ཕྱིར་དུས་གཞན་གྱི་ཚེ་ན་གལ་ཏེ་དགེ་སློང་རྣམས་ཀྱིས་ལྷག་པར་གནས་པ་དང་མི་འབྲལ་བར་འགྱུར་ན། དེ་ནས་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ཉིད་ཅེས་བྱ་བ་འདི་ནི་དུས་གསུམ་པའོ། །

[Block 1562]
དེ་དག་མེད་པ་ན༌[^1352]གནས་པའི་ཕྱིར་དགེ་སློང་དག་ཕྱིན་པ་ན་ཞེས་བྱ་བ་ནི། དེ་ན་དགེ་སློང་སྔར་གནས་པ་གནས་ཁང་ན་མེད་པ་དེ་ནི་དེ་མ་ཡིན་པ་དེ་གང་ཡིན་པ་དེ་ལ་དགེ་སློང་གནས་པ་མེད༌[^1353]པར་གྱུར་པ་ལ་ལྷག་པར་གནས་པའི་ཕྱིར། དགེ་སློང་རྣམས་ཀྱིས་ཕྱིན་པ་གང་ཡིན་པ་དེ་ནི་བྱིན་གྱིས་བརླབ་པའི་དུས་བཞི་པའོ། །

[Block 1563]
ཕྱིན་པའི་དུས་དེ་ཉིད་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 1564]
བྱ་བ་གཞན་བརྩམས་པ་དང་ངལ་བསོ་བ་མ་བྱས་པ་ཚུན་ཆད་ནི་དེ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཇི་སྲིད་དུ་དེ་རྣམས་ཕྱིན་པ་བྱ་བ་གཞན་བརྩམས་པ་མ་བྱས་པ་ཚུན་ཆད་ཞི་བར་མི་འགྱུར་རོ། །

[Block 1565]
འདུག་པ་ལ་སོགས་པ་གནས་པར་གྱུར་པ་རེ་ཞིག་བརྟག་པར༌[^1354]མི་བྱ་སྟེ། དེ་ཉིད་ནི་ཕྱིན་པ་ཉིད་དོ། །

[Block 1566]
ཕྱིན་པའི་གནས་སྐབས་སུ་རིག་པར་བྱ༌[^1355]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1567]
ཐམས་ཅད་ལ་དགེ་འདུན་གྱི་ལས་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་དུས་བཞི་པོ་དེ་རྣམས་ལ་དགེ་འདུན་གྱི་ལས་ཀྱིས་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 1568]
དང་པོ་གཉིས་ལ་ནི་གང་ཟག་གིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དང་པོ་སོ་ཕག་འགྲེམས་པར་གྱུར་པ་དང་། ཕྱིས་ལས་སར་པ་དང་བཅས་པར་གྱུར་པ༌[^1356]ཉིད་ནི་གང་ཟག་གིས་ཀྱང་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 1569]
གང་ཟག་ཇི་ལྟ་བུས་ཤེ་ན། དེའི་ཕྱིར་ལག་གི་བླས་སོ། །

[Block 1570]
དང་པོ་ཤོས་ལ་ནི་འབའ་ཞིག་གིས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དང་པོའི་དུས་ལ་དང་པོའི༌[^1357]སོ་ཕག་འགྲེམས་པ་ཉིད་ན་ལག་གི་བླ་འབའ་ཞིག་གིས་ཀྱང་བྱིན་གྱིས༌[^1358]བརླབ་ཏུ་རུང་བའོ། །

[Block 1571]
དགེ་སློང་རབ་ཏུ་མང་པོ་རྣམས་ཀྱིས་སེམས་བསྡུ་བ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་འདིའི་སྔགས་ནི། ཚེ་དང་ལྡན་པ་དག་སེམས་སྡུས༌[^1359]ཤིག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1572]
དང་པོར་འབའ་ཞིག་ལ་འདིས་ཇི་ལྟར་བྱིན་གྱིས་བརླབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་བརྗོད་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1573]
ཇི་ལྟར་ཡང་དེ་དགེ་སློང་ལག་གི༌[^1360]བླས་རྡོ་བརྟེག་པ༌[^1361]ན། དེའི་ཕྱིར༌[^1362]དང་པོར་གཞི་འདི་ནི་དགེ་འདུན་གྱི་རུང་བའི་ཁང་པར་འགྱུར་བའོ་སྙམ་དུ་སེམས་བསྐྱེད་པར་བྱ་ཞིང་ཚིག་ཏུ་ཡང་བརྗོད་པར་བྱ་སྟེ། གཞི་འདི་ནི་དགེ་འདུན་གྱི་རུང་བའི་ཁང་པ་འབྱུང་བར་འགྱུར་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1574]
གཉིས་པ་ལ་ནི་དགེ་སློང་རབ་ཏུ་མང་པོ་དག་གིས་སེམས་བསྡུས་པས་སོ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབས་པའི་དུས་གཉིས་པ་སྟེ། ཕྱིས་ལས་སར་པ་དང་བཅས་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དུས་དེར་ནི་དགེ་སློང་རབ་ཏུ་མང་པོ་དག་གིས་རུང་བའི་ཁང་པར་སེམས་བསྡུས་པར་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་སྟེ། [^1363]དེའི་ཚེ་ན་ཡང་གཙུག་ལག་ཁང་བྱེད་པ་སྲིད་པའི་ཕྱིར་རོ། །

[Block 1575]
གསུམ་པ་ལ་ནི་ལས་ཁོ་ནས་སོ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་པའི་དུས་གསུམ་པ་སྟེ། གཞན་གྱི་ཚེ་དགེ་སློང་གནས་པ་ཉིད་དང་མ་བྲལ་བའོ་ཞེས་བྱ་བའི་དུས་ཀྱི༌[^1364]དེའི་ཚེ་ན་དགེ་འདུན་གྱིས་གསོལ་བ་དང་། གཉིས་ཀྱི༌[^1365]ལས་ཀྱིས་བྱིན་གྱིས་བརླབ་པ་ཁོ་ནར་བྱས་པའོ། །

[Block 1576]
དུས་གསུམ་པར་བྱིན་གྱིས་བརླབ་པའི་རུང་བའི་ཁང་པ་འདིའི་མིང་ནི་ལས་ཀྱི༌[^1366]མཐའ་ལས་བྱུང་བའི་ཞེས་བྱ་བའོ། །

[Block 1577]
བཞི་པ༌[^1367]ལ་ནི་ཇི་སྙེད་ཕྱིན་པ་དེ་སྙེད་ཀྱིས་རུང་བའི་ཁང་པ་ཉིད་དུ་བསྒྲག༌[^1368]པའི་ཚིག་ཅིག་ཅར་བརྗོད་པས་སོ་ཞེས་བྱ་བ་ལ། ཇི་སྙེད་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མ་ཐོབ་པ་རྣམས་ལ་མང་པོ་ཉིད་དུ་འཇུག་པར་འགྱུར་བས། མཉམ་པ་སྲིད་པ་ལ་བྱིན་གྱིས་བརླབ་པར༌[^1369]འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1578]
བཞི་པ་ལ་ནི་ཞེས་བྱ་བ་ནི་དུས་ལའོ། །

[Block 1579]
དེ་མ་ཡིན་པ་ལ་ལྷག་པར་གནས་པའི་ཕྱིར་དགེ་སློང་རྣམས་ཕྱིན་པ་ཞེས་བྱ་བ་དེ་ལའོ། །

[Block 1580]
ཅིག་ཅར་ཞེས་བྱ་བ་ལ་དགེ་སློང་ཕྱིན་པ་ཐམས་ཅད་ཀྱིས་གཞི་འདི་ནི་དགེ་འདུན་གྱི་རུང་བའི་ཁང་པར་འགྱུར་རོ་ཞེས་ཚིག་མཐུན་པར་ཅིག་ཅར་བར༌[^1370]བརྗོད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
