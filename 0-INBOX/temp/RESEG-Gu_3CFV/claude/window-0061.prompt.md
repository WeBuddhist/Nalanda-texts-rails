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
[Block 2136]
མདོ་སྡེ་དང་ལྡན་པ་སྨྲས་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི། མདོ་སྡེ་དང་ལྡན་པའི༌[^1362]བསླབ་པའི་གཞི་སྨྲ་བ༌[^1363]ན་དེ་སྐད་ཟེར་བ་དེ་ལ་ཉེས་བྱས་སོ། །

[Block 2137]
གཞུང་ཁ་ཅིག་ལས་འདིར་གཞུང་ནི་འདུལ་བ་དང་ལྡན་པའི་མདོ་མ་གཏོགས་པ་ལ་འདི་སྐད་ཅེས་འདི་ལྟར་ཆོས་འདི་ཡང་མདོའི་ནང་དུ་གཏོགས་མདོའི་ནང་དུ་འདུས་པ་དང་། ཟླ་བ་ཕྱེད་ཕྱེད་ཅིང་བཏོན་པར་བདག་གིས་ད་གཟོད་ཤེས་སོ་ཞེས་ཟེར་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2138]
ཐུན་མོང་མ་ཡིན་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། མཚན་གཞན་བསྟན་པ་འདི་ནི་བསླབ་པའི་གཞི་ཐུན་མོང་མ་ཡིན་པ་འདོན་པའི་ཚེ་ལྟུང་བ་མེད་པའོ། །

[Block 2139]
སོ་སོར་ཐར་པའི་མདོ་འདོན་པའི་ཚེ་མ་གུས་པར་ཉན་པ་ཉེ་བར་བསྒྲུབ་པ་འགྱོད་དུ་གཞུག་གོ་ཞེས་བྱ་བ་ནི། བདག་གིས་ད་གཟོད་ཤེས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཙམ་ལ་ཡང་སྔར་འདུག་པ་ན་འདོན་པ་ལ་མ་གུས་པར་ཉན་པ་ལ་ཉེ་བར་སྦྱར་བར་རིག་པར་བྱའོ། །

[Block 2140]
དངོས་སུ་ནི་མ་ཡིན་ཏེ། གང་ཞིག་འདི་བསྟན་པ་ཅི་ཁོ་བོ་ཅག་ལ་ལས་འདི་ཉིད་གཅིག་པུ་ཡིན་ནམ། ཁོ་བོ་ཅག་གིས་ཀྱང་འདོད་པའི་རྣམ་པར་རྟོག་པ་ལ་ཡང་རྣམ་པར་རྟོག༌[^1364]དགོས་སོ། །

[Block 2141]
གནོད་སེམས་ཀྱི་རྣམ་པར་རྟོག་པ་དང་། རྣམ་པར་འཚེ་བའི་རྣམ་པར༌[^1365]རྟོག་པ་ལ་ཡང་རྣམ་པར་རྟོག་དགོས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དེ་ཡང་མ་གུས་པར་ཉན་པ་ལ་ཉེ་བར་སྦྱར་བར་རིག་པར་བྱའོ། །

[Block 2142]
འགྱོད་དུ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་འདི་ནི་ལམ་དམ་པའོ་ཞེས་བྱ་བའི་བསླབ་པ་ལ་ཉེ་བར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2143]
འདིར་མང་པོའི་ཚིག་ནི་དུ་མ་ཉེ་བར་གནས་པ་བརྗོད་པ་ལ་ཉན་པ་པོ་རྣམས་ཐམས་ཅད་ཀྱིས་འདིར་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུའོ། །

[Block 2144]
འདིར་འགྱོད་དུ་གཞུག་པ་ནི་ཚེ་དང་ལྡན་པ་ཁྱོད་མ་རྙེད་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 2145]
ཉེས་བྱས་དང་མ་གུས་པར་གསོ་སྦྱོང་ལ་སོགས་པ་ཐོས་པ་ཞེས་བྱ་བའི་ཆོ་ག་འདི་ལས་རྟོགས་པར་རིག་པར་བྱའོ། །

[Block 2146]
བསླབ་པའི་གཞིའི་དངོས་པོ་ལ་ཁྱད་དུ་གསོད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 2147]
གང་ལ་ཁབ་རལ་འཆོས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བ་སོ་དང་རུས་པ་དང་རྭའི་ཁབ་རལ་བྱེད་དམ་བྱེད་དུ་བཅུག་པ་ལ་ཞེས་བྱ་བ་སྨོས་ཏེ། བ་སོའམ་རུས་པའམ་རྭའི་ཁབ་རལ་བྱེད་དམ་བྱེད་དུ་བཅུག་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2148]
འདི་མན་ཆད་ཤིང་བལ་གྱིས་གོས་པར་བྱས་པ་མ་གཏོགས་པའི་ལྟུང་བྱེད་རྣམས་ལ་བྱེད་དུ་འཇུག་པ་འབའ་ཞིག་གསུངས་མོད་ཀྱི། རང་བྱེད་པ་ལ་ཆེས་ལྕི་བས་ཞེས་བྱ་བ་དེ་ཡང་འདི་རྣམས་ཀྱི་ཁོངས་སུ་བསྡུས་སོ། །

[Block 2149]
ཤིན་ཏུ་ཡང་བ་བརྗོད་པ་ན་ལྕི་བ་མ་བརྗོད་ཀྱང་གྲུབ་པ་ཉིད་ཅེས་བྱ་བ་འདི་དེ་ཙམ་ཞིག་སྨོས་སོ། །

[Block 2150]
ཁབ་རལ་དང་ཁྲིའི་རྐང་པ་འཆོས་པ་ལས་ཀྱང་དགེ་སློང་གིས་བཅག་པ་ནའོ། །

[Block 2151]
བ༌[^1366]སོ༌[^1367]ལ་སོགས་པ་ཡང་རིན་ཆེ་བའི་ཕྱིར་བཀག་པའོ། །

[Block 2152]
དེ་ལྟ་བས་ན་གང་ལ་ཆེས་རིན་ཆེ་བའི་ཕྱིར་དེ་ཡང་འདིར་བཀག༌[^1368]པར་རིག་པར་བྱ་སྟེ། ཐ་ན་མཚོན་ཆ་ལ་སོགས་པ་ཡང་ངོ་། །དེ་ལ་ཡང་དེ་འདི་བྱས་པ་ཉིད་དོ། །

[Block 2153]
རིན་པོ་ཆེ་ལས་བྱས་པ་ནི་རུང་བ་མ་ཡིན་པའི་ཕྱིར་ཉེས་བྱས་བྱེད་པ་ཉིད་ཡིན་ནོ། །

[Block 2154]
དེ་ལྟར༌[^1369]ཡང་འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 2155]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་རིན་པོ་ཆེ་ལས་བགྱིས་པའི་ཁབ་རལ་བགྱིད་དུ་སྩོལ༌[^1370]ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2156]
བྱས་ཟིན་པ་རྙེད་པ་དང་བྱས་ཟིན་པ་སྤྱོད་པ་དག་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། རས་ལ་སོགས་པ་རྙེད་པ་དེ་ལས་བྱས་པ་དང་བྱེད་དུ་བཅུག་པ༌[^1371]ལ་ལྟུང་བ་མེད་པ་དང་ན་སྨད་པ་ཡང་མེད་དེ། [^1372]བྱས་པ་འདི་ཉིད་ལས་བཀག་པའི་ཕྱིར་རོ། །

[Block 2157]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 2158]
བྱས་པ་རྙེད་པ་དང་བྱས་པ་ལ་སྤྱོད་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2159]
བཅག་པ་ཉིད་མ་དྲིས་པར་འཆགས་པ་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གང་གི༌[^1373]མདུན་དུ་ལྟུང་བ་འཆགས་པ་དེས་ཁབ་རལ་དེ་ཁྱོད་ཀྱིས་བཅག་གམ་ཞེས་དྲི་བར་བྱ་སྟེ། དེ་སྐད་མ་དྲིས་པར་ལྟུང་བ་འཆགས་པ་བླང་བར་མི་བྱའོ། །

[Block 2160]
གལ་ཏེ་མ་བཅགས༌[^1374]ན་མ་བཤགས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་མ་བཅགས་པར༌[^1375]ལྟུང་བ་འཆགས་པར་བྱེད་ན་དེའི་ལྟུང་བ་དེ་མ་བཤགས་པ་ཉིད་ཡིན་ནོ། །

[Block 2161]
འོག་མ་ལྔ་པོ་དག་ལ་ཡང་དེ་དག་དང་བཅས་པ་དང་ལྡན་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསླབ་པའི་གཞི་འདིའི་འོག་མ་བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཀྱི་ཚད་ལས་གྱུར་པའི་གོང་མ་རྣམས་དེ་མ་ཐག་པར་རྟོགས་པར་བྱའོ། །

[Block 2162]
དེ་དག་ཅེས་བྱ་བ་ནི་མ་དྲིས་པར་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2163]
བཅད་པ་དང་ལྡན་པ་ཉིད་དུ་རྟོགས་པར་བྱ་སྟེ། བཅད་པ་ཉིད་མ་དྲིས་པར་འཆགས་པར་བླང་བར་མི་བྱའོ། །

[Block 2164]
གལ་ཏེ་མ་བཅད་པ་ན་ཆགས་པ་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2165]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 2166]
གང་གི་མདུན་དུ་འཆགས་པར་བྱེད་པ་དེས་ཁྱེད་ཀྱིས་དངོས་པོ་དེ་བཅད་དམ་ཞེས་དྲི་བར་བྱའོ། །

[Block 2167]
མ་དྲིས་པར་བཤགས་ན་ལྟུང་བ་དེ་དག་བཤགས་པ་མ་ཡིན་ལ། དགེ་སློང་དེ་ལ་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2168]
བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཀྱི་ཚད་ལས་གྱུར་པའི་ལྟུང་བྱེད་ལ་བཅད་ནས་ལྟུང་བྱེད་དུ་ནི་མ་གསུངས་སོ། །

[Block 2169]
འདིར་རྣམ་པར་འབྱེད་པ་ལས་བཅད་ནས་ཞེས་བྱ་བ་འདི་ལ་དོན་བསྟན་པར་གྱུར་པ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཀྱི་ཚད་ལས་གྱུར་པ་ལས་གཞན་དག་ལ་བཅད་པ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 2170]
ཅི་བཅགས་པ༌[^1376]དང་བཅད་པ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་རང་བཞིན་གྱི་དོན་འདི་ཉིད་ཀྱིས་དེ་ལྟར་ཉིད་དུ་གནས་སྤྱིར་བཏང་བར་བྱས་ནས་དམིགས་ཀྱིས་བསལ་བ་བསྟན་པའི་ཕྱིར། དེའི་ཕྱིར་བཅད་པ་དང་ལྡན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་ལྔ་པོ་དག་ལ་ཡང་བཅད་པ་དང་ལྡན་པ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་གཉིས་པ་ལ་ནི་བསྡུས་པ་དང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཤིང་བལ་གྱིས་གོས་པར་བྱས་པ་ཞེས་བྱ་བ་བསླབ་པའི་གཞི་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2171]
ཁབ་རལ་འཆོས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 2172]
རྐང་པ༌[^1377]དམའ་བ་དང་ལྡན་པའི་ཁྲི་ལ་ཉལ་བར་མི་བྱ་བའོ༌[^1378]ཞེས་བྱ་བ་ནི། གང་ཞིག་འབྱུང་བར་འགྱུར༌[^1379]བའི་མགོ་བོ་ལ་ཉེས༌[^1380]པར་འགྱུར་བ་དེ་ལྟ་བུའི་ས་དང་གང་ལ་འཁྱིལ་བ་མ་བཅགས་པར༌[^1381]སྦྲུལ་གྱིས་སོས༌[^1382]བཏབ་པ་བསྒྲུབ་པ་མི་འབྱུང་བ་དེ་ལྟ་བུའི༌[^1383]ས་ལ་ཞེས་བྱ་བ་གླེང་གཞི་ལས་རྟོགས་པར་བྱའོ། །

[Block 2173]
མལ་དང་འབྲེལ་པའི་ཁྲིའི་ཉེ་འཁོར་གྱི་ཕྱོགས་སུ་རྐང་པ་བཀྲུ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཉལ་བའི་གནས་དང་འབྲེལ་པའི་ཁྲིའི་ཉེན་ཀོར༌[^1384]དང་འབྲེལ་པའི་ཕྱོགས་སུ་རྐང་པ་བཀྲུ་བར་མི་བྱའོ། །

[Block 2174]
ཁྱིམ་པའི་གནས་མལ་གྱི་གནས་གཞན་དང་འབྲེལ་པ་ཉིད་ལ་འདི་དང་མི་མཐུན་པ་སྟེ། དེ་བས་ན་དེ་ལས་ཡང་ཉེས་པ་འདིའོ། །

[Block 2175]
ཁྱིམ་པའི་གནས་མལ༌[^1385]ཉིད་ལ་འདི་ནི་ཤིན་ཏུ་ན་སྨད་པར་རིག་པར་བྱའོ། །ཅི་ཐམས་ཅད་ཀྱིས་བཀྲུ་བར་མི་བྱའམ་ཞེ་ན། དེའི་ཕྱིར་ལྷམ་ཡོད་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །
--- END BLOCKS ---
