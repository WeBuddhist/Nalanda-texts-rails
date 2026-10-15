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
དེ་ལྟར་ཡང་ཤིན་ཏུ་ཚུལ་ཁྲིམས་འཆལ་བ་མཁན་པོ་དང་སློབ་དཔོན་དག་ལ་ཉེ་བར་གནས་པར་བྱ་བ་ཉིད་དུ་གསུངས་སོ། །

[Block 1402]
ཚུལ་ཁྲིམས་འཆལ་བའི་ལྕི་བ་ཉིད་ཡོངས་སུ་སྤོང་བའི་དོན་དུ་སོ་སོར་བསྐོར་བར་བྱའོ། །

[Block 1403]
སྤངས་པའི་རྗེས་སུ་ཕྱོགས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1404]
དེ་དག་ལ་གཞམ་པ༌[^870]དང་ལས་ཀྱིས༌[^871]མི་བསྒོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་འདིས་གང་ཞིག་ལྟ་བ་དང་འབྲེལ་པ་རྣམས་ལ་ཆོ་ག་འདི་བྱ་བ་ཉིད་དུ་བསྟན་པ་དེ་ནི་དགེ་ཚུལ་ཡོད་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་འདི་ལ་གལ་ཏེ་དགེ་སློང་གི་ཁོངས་སུ་སྡུད༌[^872]ན། དེ་ལ་ལས་ཀྱི་མཐའ་ལ་མི་གཏོང་ན་དེའི་ཚེ་ཇི་ལྟར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ལྟོས་ནས་བརྗོད་པར་བྱ་སྟེ། ཚིག་དེ་ཉིད་ལ་ཞུགས་པ་མི་གཏོང་ན། དགེ་ཚུལ་བསྙིལ་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚིག་དེ་ཉིད་ཞུགས་པ་དེ་ལྟར་བདག་གིས༌[^873]ཇི་སྲིད་བར་དུ་གཅོད་པའི་ཕྱིར་ནུས་པ་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གང་ལ་ཡོད་པ་དེ་ནི་ཚིག་དེ་ཉིད་ལ་ཞུགས་པའོ། །

[Block 1405]
དེའི་དངོས་པོ་མི་གཏོང་ན་དགེ་ཚུལ་དེ་བསྙིལ་བར་བྱའོ། །

[Block 1406]
འདིར་འདོད་པ་ཞེས་བྱ་བ་ནི་དཔེ་ཙམ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1407]
དེ་བས་ན་ལྟ་བ་ཐམས་ཅད་ཡོད་པར་བྱེད་པའི་ཚིག་བསྡུས་པ༌[^874]ཡིན་ནོ། །

[Block 1408]
འདི་མ་ཡིན་ཞེས་བྱ་བ་ནི་ཞུགས་པའོ། །

[Block 1409]
བསྟན་པ་ལ་གང་ཞིག་ཚུལ་འདིར་ལེགས་པར་ཞུགས་པ་ལ་ཡང་ལེགས་པར་གནས་པ་དེའི་ཆོས་དང་ལྡན་པ་དག་གིས་སྨད་པར་བྱ་བ་སྟོབས་དང་ལྡན་པ་ལ་གང་དུ་ཡང་མི་འཇུག་པ་དེ་ལས་འདིར་སྨོད་པར་བྱ་བ་རྣམ་པར་གཞག་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1410]
དགེ་འདུན་ལ་ཐ་དད་པར་བྱེད་པ་ནི་གསལ་བའོ། །

[Block 1411]
དགེ་འདུན་ཀུན་ནས་ལྟུང་བ་ལས་འབྱུང་བའོ། །

[Block 1412]
འདི་ལ་ཀུན་ནས་ལྟུང་བ་ཉིད་ཀྱིས་དགེ་འདུན་ལ་ཁོངས་སུ་སྡུད་པ་ཡོད་པ་མ་ཡིན་ཏེ། འདུག་པའི་དབུས་སུ་གནས་པ་ལ་ནི་འཁོར་གྱི་དབུས་ཀྱི་དངོས་པོ་ཉིད་ལ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་བས་ན་བསྙིལ་བར་བྱའོ་ཞེས་བྱ་བ་འདི་ལ་སྤང་བར་བྱ་བའི་ལས་ལ་བརྟགས་པ་ཡིན་ནོ། །

[Block 1413]
གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་རྟོགས་པར་བྱ་བ་གསལ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1414]
སོ་སོའི་དངོས་པོ་ལ་ངེས་པར་ལྡན་པ་ཉིད་ཀྱང་མ་ཡིན་ནོ། །

[Block 1415]
འདིའི་ལས་བྱེད་པ་ལ་རྟོགས་པ་བསྒྲུབ་པ་མ་ཡིན་ནོ། །

[Block 1416]
དེ་བས་ན་འདིར་རྟོགས་པ་བསྒྲུབ་པ་ལ་དེའི་ཆོ་ག་བརྗོད་པར་བྱ་སྟེ། ཁྱོད་ལ་དང་པོར་གསོལ་བ་དང་བཞིའི་ལས་སོ། །

[Block 1417]
དེའི་འོག་ཏུ་བསྙིལ་བ་རྩོམ་མོ་ཞེས་བྱ་བ་དང་། གསོལ་བ་བྱས་སོ། །

[Block 1418]
ལས་བརྗོད་པ་དང་པོ་དང་གཉིས་པ་ཡང་བྱས་ཟིན་གྱི་སྡིག་པ་ཅན་གྱི་ལྟ་བར་གྱུར་པ་འདི་ལྟ་བུ་འདི་ཐོང་ཤིག་ཅེས་མཐར་དགེ་སློང་གིས༌[^875]དེ་ལ་བསྒྲགས་པར༌[^876]བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དང་པོར་ཞིས་བྱ་བ་ནི་གསོལ་བ་ལའོ། །

[Block 1419]
དེའི་འོག་ཏུ་ཞེས་བྱ་བ་ནི་བསྙིལ་བའི་ལས་ལའོ། །

[Block 1420]
བསྙིལ་བའོ་ཞེས་བྱ་བ་ནི་ལས་ལ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1421]
རྩོམ་པ་ཞེས་བྱ་བ་ནི་རྩོམ་པ་སྟེ་འདི་ནི་དང་པོའི་ཆའོ། །

[Block 1422]
རྩོམ་པ་དེ་ཡང་གང་ཞེ་ན། དེའི་ཕྱིར་གསོལ་བ་བྱས་ཟིན་གྱི་སྡིག་པ་ཅན་གྱི་ལྟ་བར་གྱུར་པ་འདི་ལྟ་བུ་འདི་ཐོང་ཤིག་ཅེས་བྱ་བ་སྨོས་ཏེ། འདི་ནི་གཅིག་སྟེ་གཞན༌[^877]བཤད་པ་ནི་ལས༌[^878]བརྗོད་པ་དང་པོ་ཡང་བྱས་ཟིན་གྱི༌[^879]སྡིག་པ་ཅན་གྱི་ལྟ་བར་གྱུར་པ་འདི་ལྟ་བུ་འདི་ཞེས་བྱ་བས་སོ། །

[Block 1423]
དེའི་འོག་ཏུ་ལས་བརྗོད་པ་གཉིས་པ་ཡང་བྱས་ཟིན་གྱི་སྡིག་པ་ཅན་གྱི་ལྟ་བར་གྱུར་པ་འདི་ལྟ་བུ་འདི་ཐོང་ཤིག་ཅེས་བྱ་བས་སོ། །

[Block 1424]
རེ་རེའི་མཐར་ཞེས་བྱ་བ་ནི་གསོལ་བ་དང་ལས་བརྗོད་པ་དང་པོ་དག་སོ་སོ་རེ་རེའི་མཐའ་ནས་བརྩམས་ཏེ་མཐར་མི་འགྲོ་བར་ལྡོག་པ་ནི་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདོད་པ་དགག་པའི་དོན་དུ་བརྗོད་པར་བྱའོ། །

[Block 1425]
བཏང་ན་ཕྱི་མ་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྔ་མ་ཉིད་ཀྱིས་སོ་སོར་ལྡོག་པ་ཡོད་པ་ལ་ཕྱི་མ་མི་བྱའོ། །

[Block 1426]
བརྡའི་བྱེད་པ་ཡང་ཆོ་ག་འདིས་རྟོགས་པར་བྱའོ། །

[Block 1427]
ཐམས་ཅད་དུ་འབྲེལ་པ་བྱེད་པ་ལ་སོགས་པའི་དོན་གྱི་ལས་ལ་མི་བསྒོ་བ་དང་སྨད་པར་བྱ་བ་དང་སྤང་བ་དང་བསྙིལ་བ་རྣམས་ཉིད་ལ་སྔར་བཤད་པའི་ཆོ་གའི་དངོས་པོ་ལ་ལྟོས་ནས་ཆོ་ག་རིག་པར་བྱའོ། །

[Block 1428]
བསྙིལ་བ་སྡུད་པའི་ལྟུང་བ་བྱེད་པ་པོ་ཉིད་ནི་གང་ཡིན་ཅི་ཞིག་སྤྱད་ན་ཞེས་བྱ་བ་འདི་ལ་སྔར་བཤད་པ་ལ་མངོན་པར་བརྟེན་ནས་དེ་སྐད་སྨྲ་བ་པ་འབྱུང་བ་ལ་སླར་བྱས་པས༌[^880]དགེ་སློང་ལ་ཞེས་བྱ་བ་འདིའི་གནས་སུ་གང་དུ་འདུ་ཤེས་བྱ་བ་ལ་སྨོས་པ་ནི་དགེ་ཚུལ་བསྙིལ་བ་ཉིད་དུ་གྱུར་པའི་གནས་སྐབས་ལ་སྟེ། བསྙེན་པར་མ་རྫོགས་པ་ལ་འདི་ལྟ་བུ༌[^881]ཉིད་ཡིན་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1429]
ཉེས་བྱས་འདི་ཡོད༌[^882]ལ་དོར་བ་རྣམ་པར་གཞག་པའོ། །

[Block 1430]
བསྙིལ་བ་སྡུད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1431]
ཅི་ཞིག་བྱས་ན་ཁ་མ་བསྒྱུར་བའི་གོས་གྱོན་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྔོན་པོའམ་དམར་པོའམ་ངུར་སྨྲིག་གིས་ཁ་མ་བསྒྱུར་བ་རང་གི་གོས་ཐ་ན་ལྷུང་བཟེད་ཀྱི་ཁ་གཡོགས་དང་། སྣོད་དང་རྐང་པའི་འབོབ་དང་སྐེ་རགས༌[^883]དག་གི༌[^884]བགོ་བ་ལ་སོགས་པ་ཡོངས་སུ་ལོངས་སྤྱོད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚོན་ཆེན་པོ་བརྒྱད་པོ་རྣམས་སྤངས་ནས་གཞན་གང་ཡང༌[^885]རུང་བ་འགའ་ཞིག་ལས་གོས་ཁ་བསྒྱུར་བར་བྱའོ་ཞེས་བྱ་བ་ཕྲན་ཚེགས་དག་ལས་སྨོས་སོ། །

[Block 1432]
འདིར་ཡང་འདག་པ་ཞེས་བྱ་བ་ལས་གང་ཞིག་འདི་ལ་དམར་པོས་ཞེས་བྱ་བ་རྣམ་པར་འབྱེད་པ༌[^886]ཀློག་པ་ཁ་ཅིག་ལས་འདིར་ཡང་འདོན་པ་ཡིན་ཏེ། ཚོན་ཆེན་པོ་རྣམ་པ་བརྒྱད་ཀྱིས་ཁ་སྒྱུར་བར༌[^887]བྱེད་ལ་ལི་ཁྲི་དང་། མཐིང་ཤུན་དང་རྒྱ་སྐྱེགས་དང་། མཚལ་དང་། གུར་གུམ་དང་། བཙོད༌[^888]དང་། རྨ་ཤིང་དང་། ལེ་བརྒན་རྩིས་ཁ་སྒྱུར་བར༌[^889]བྱེད་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཁ་དོག་ཆེན་པོ་བརྒྱད་མ་གཏོགས་པ་གཞན་གང་ཡང་རུང་བ་འགའ་ཞིག་གིས་གོས་ཁ་བསྒྱུར་བར་བྱ་ཞེས༌[^890]གསུངས་པ་ཡིན་ནོ། །

[Block 1433]
དེ་བས་ན་འདིར་སྔོན་པོ་ལ་སོགས་པ་ནི་དཔེ་ཙམ་དུ་རྟོགས་པར་བྱ་བའོ།[^891] །དེ་ལ་སྔོན་པོས་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་ཕུན་སུམ་ཚོགས་པའི་ཚོན་ལ་དཔེར༌[^892]རིག་པར་བྱའོ། །

[Block 1434]
དམར་པོས་ཞེས་བྱ་བ་ནི་ས་ལས་འབྱུང་བའི་ཁམས་ལའོ། །

[Block 1435]
རྨ་ཤིང་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་ཕུན་སུམ་ཚོགས་པའི་མེ་ཏོག་དང་འབྲས་བུ་ལ་སོགས་པའི་ཚོན་ལས་བསྐྱེད་པའོ། །

[Block 1436]
ཁ་མ་བསྒྱུར་བ་ཞེས་བྱ་བ་ནི་ཚོན་གྱིས༌[^893]སོ། །

[Block 1437]
དེ་བས་ན་གང་ཡང་རུང་བས་ཁ་མ་བསྒྱུར་བའི་རང་གི་གོས་ལ་ཞེས་བྱ་བ་ནི་གཞན་གྱི༌[^894]གོས་ཉེ་བར་ལོངས་སྤྱོད་པ་ལ་ན་སྨད་པ་ཉིད་དེ་ཁ་ན་མ་ཐོ་བ་སྟོབས་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར། བདག་ཏུ་བྱས་པ་དང་དཀྲིས་པར་མངོན་པར་བརྟེན་པ་ཉིད་ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1438]
དེ་ལྟར་ཡང་སོ་སོར་ཁྱིམ་པའི་གོས་བགོ་བ་བཀག་པའི་ཚུལ་གྱིས་ཏེ་གཞན༌[^895]དུ་ནི་མ་ཡིན་ནོ། །

[Block 1439]
དེ་ལྟ་བུའི་ལྟུང་བྱེད་ལ་འབྱུང་བ་སྲིད་པ་མ་ཡིན་ནོ། །

[Block 1440]
གོས་སར་པ་སོ་སོར་རྙེད་པས་ཞེས་བྱ་བ་ལ། གང་ཞིག་སོ་སོར་རྙེད་པའི་ཚིག་བྱས་ཞེས་བྱ་བ་འདིའི་རྗེས་ལ་ཡང་རང་གི་ཚིག་སྨོས་པ་དེ་ལས་སོ། །
--- END BLOCKS ---
