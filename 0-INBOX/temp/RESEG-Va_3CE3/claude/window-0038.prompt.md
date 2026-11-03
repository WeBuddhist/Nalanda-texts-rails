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
འདི་ནི་སྟོབས་བཅུའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཆོས་ཐམས་ཅད་ཀྱི་རྣམ་པ་ཐམས་ཅད་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་རྣམ་པ་ཐམས་ཅད་ནི་གནས་དང་གནས་མ་ཡིན་པ་མཁྱེན་པའི་སྟོབས་ལ་སོགས་པ་ཡེ་ཤེས་བཅུའི་སྤྱོད་ཡུལ་ཡིན་ན་དེ་དག་གི་སྤྱོད་ཡུལ་དུ་མ་གྱུར་པ་ནི་རྣམ་པ་ཡོད་པ་མ་ཡིན་ཏེ། འདི་ལྟར་རྣམ་པ་དེ་དག་དོན་དམ་པར་མེད་པས་དེའི་ཕྱིར་སྟོབས་བཅུའི་ཡུལ་དུ་གྱུར་པ་རྣམ་པ་རྣམས་མེད་པར་མཐོང་བའི་ཕྱིར་སྟོབས་བཅུའི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 1332]
ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཞུམ་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ནི་ཆོས་གང༌[^919]ཡང་ཞུམ་པ་མེད་དེ་དེ་བས་ན་ཐམས་ཅད་དུ་ཞུམ་པ་མེད་པའི་རང་བཞིན་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ལ་མི་འཇིགས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 1333]
ཐམས་ཅད་དུ་ཡེ་ཤེས་ཆགས་པ་མེད་ཅིང་ཐོགས་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའི་ཡེ་ཤེས་ནི་ཐམས་ཅད་དུ་ཆགས་པ་མེད་པ་དང་། ཐོགས་པ་མེད་པ་སྟེ། དེ་བས་ན་དེ་སོ་སོ་ཡང་དག་པར་རིག་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 1334]
ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ལས་ཡང་དག་པར་འདས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་འདི་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དེ༌[^920]ཉན་ཐོས་ལ་སོགས་པ་ལ་མེད་པས་དེའི་ཕྱིར་དེ་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་ཞེས་བྱ་བར་བགྲང་ངོ་། །འདི་ནི་དེ་བཞིན་གཤེགས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། སངས་རྒྱས་ཐམས་ཅད༌[^921]ཀྱིས་གསུངས་པ་དེ་བཞིན་གཤེགས་པ་ཉིད་ཡིན་པའི༌[^922]ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ངེས་པའི་ཚིག་གིས་ནི༌[^923]དེ་བཞིན་དུ་གསུང་བའི༌[^924]ཕྱིར་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་སྟེ། སངས་རྒྱས་ཀྱིས་གསུངས་པ་ཐམས་ཅད་ལ་དེ་བཞིན་དུ་དམིགས་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་དེ་བཞིན་གཤེགས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 1335]
འདི་ནི་རང་བྱུང་གི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཆོས་ཐམས་ཅད་ལ་དབང་བསྒྱུར་བའི༌[^925]ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཆོས་ཐམས་ཅད་དེའི་དབང་དུ་འགྱུར་ཏེ།[^926] དེའི་ཕྱིར་རང་གིས་ཆོས་ཐམས་ཅད་ཟིལ་གྱི༌[^927]གནོན་པས་རང་བྱུང་གི༌[^928]ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 1336]
བརྒྱ་བྱིན་གྱིས་བསྔགས་པའི་ཚིག་དང་། གནས་བརྟན་ཤཱ་རིའི་བུའི་ཚིག་དང་། བཅོམ་ལྡན་འདས་རྗེས་སུ་ཡི་རང་བའི་ཚིག་རྣམས་ནི་བརྡ་ཕྲད་པར་སླ་བས་མདོ་ལས་ཇི་སྐད་འབྱུང་བ་བཞིན་ནོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ་གཟུགས་ལ་མི༌[^929]གནས་པ་དེའི་ཚེ་གཟུགས་ལ་བརྩོན༌[^930]པར་བྱེད་པ་ཡིན་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ལམ་གྱི་རྣམ་པ༌[^931]ཤེས་པ་ཉིད་ཀྱི་ཡེ་ཤེས་ནི་ཆོས་གང་ལ་ཡང་མི་གནས་ཏེ། དེ་བས་ན་མི་གནས་པ་ཉིད་དེའི་བརྩོན་པར་བྱེད་པ་ཞེས་བྱའོ། །

[Block 1337]
ཀཽ་ཤི་ཀ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའི༌[^932]གཟུགས་ལ་བརྩོན་པར་མི་བྱེད་དེ་འདི་ལྟར་གཟུགས་ལ་བརྩོན༌[^933]པར་མི་བྱེད་པ་འདི་ལྟ་བུ་ནི་གཟུགས་ལ་བརྩོན༌[^934]པར་བྱེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་འགྲེས་སྔ་མར་ནི་གནས་པ་བཀག་གོ། །

[Block 1338]
འདིར་ནི་བསྒྲུབ་པ་བཀག་གོ། །

[Block 1339]
གཟུགས་སྔོན་གྱི་མཐར་མི་དམིགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པས་དུས་གསུམ་ཆར་དུ་ཡང་མི་དམིགས་པར་སྟོན་ཏོ། །

[Block 1340]
ཤཱ་རིའི་བུ་འདི་ལྟར་གཟུགས་ཀྱི་ཟབ་པ་གང་ཡིན་པ་དེ་གཟུགས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཟབ་པ་ཞེས་བྱ་བ་ཀུན་བརྟགས་པ་ཡིན་པའི་ཕྱིར་དོན་དམ་པར་གཟུགས་ཉིད་མེད་པས་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1341]
ཟབ་པའི་འགྲེས་དང་། གཏིང་དཔག་དཀའ་བའི་འགྲེས་དང་། ཚད་མེད་པའི་འགྲེས་དང་། བརྒྱ་བྱིན་གྱི༌[^935]ཚིག་དང་། ལུང་བསྟན་པ་ཐོབ་པ་དང་། འབྲོག་དགོན་པའི་དཔེ་དང་། རྒྱ་མཚོ་ཆེན་པོའི་དཔེ་དང་། དཔྱིད་ཀྱི་དཔེ་དང་། སྦྲུམ་མའི་དཔེ་དང་། རྗེས་སུ་བཟུང་ཞིང་ཡོངས་སུ་བསྟན་པའི༌[^936]ཚིག་འདི་རྣམས་ནི་བརྡ་ཕྲད་པར་སླའོ། །

[Block 1342 [HEADING]]
##### བསྒོམ་པ་ཡོངས་སུ་རྫོགས་པའི་རྟགས། ^1-2-5-7-0

[Block 1343]
ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྒོམ་པ་ཡོངས་སུ་རྫོགས་པའི་རྟགས་རྣམ་པ་གཉིས་ཏེ། ཆོས་ཐམས་ཅད་འཕེལ་བ་དང་། འགྲིབ་པར་མི་མཐོང་བ་དང་། ཆོས་རྣམས་ཀྱི་མཚན་ཉིད༌[^937]མཐོང་བའོ། །

[Block 1344]
བསམ་གྱིས་མི་ཁྱབ་པ་བསྟན་པ་དང་། བསམ་གྱིས་མི་ཁྱབ་པ་ལ་རྣམ་པར་རྟོག་པ་མི་འབྱུང་བ་ཡང་། བསྒོམ་པ་ཡོངས་སུ་རྫོགས་པའི་རྟགས་སོ། །

[Block 1345]
ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སྤྱོད་པའི་རྟགས་ནི་གཟུགས་སུ་མི་རྟོག་རྣམ་པར་མི་རྟོག་གོ། །

[Block 1346]
གཟུགས་ཀྱི་མཚན་མར་མི་རྟོག །རྣམ་པར་མི་རྟོག་གོ། །

[Block 1347]
གཟུགས་ཀྱི་རང་བཞིན་དུ་མི་རྟོག །རྣམ་པར་མི་རྟོག་གོ་ཞེས་བྱ་བ་སྟེ། སྟོང་པ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་གྱིས་ཆོས་རྣམས་སུ་མི་རྟོག་གོ། །

[Block 1348]
མཚན་མ་མེད་པའི་ཏིང་ངེ་འཛིན་གྱིས་མཚན་མར་མི་རྟོག་གོ། །

[Block 1349]
སྨོན་པ་མེད་པའི་ཏིང་ངེ་འཛིན་གྱིས་རང་བཞིན་དུ་མི་རྟོག་གོ། །

[Block 1350]
ཀུན་བརྟགས་པ་ལ་རྣམ་པར་མི་རྟོག་གོ། །

[Block 1351]
གཞན་གྱི་དབང་ལ་རྣམ་པར་མི་རྟོག་གོ། །

[Block 1352]
སྔར་ནི་དེ་བཞིན་ཉིད་ཟབ་པས་ཟབ་པ་ཉིད་དུ་གསུངས་སོ། །

[Block 1353]
ད་ནི་དེ་བཞིན་ཉིད་ཀྱི་མཚན་ཉིད་གཟུགས་ལ་སོགས་པ་ལ་སྒྲོ་བཏགས་ནས་ཟབ་པ་བཤད་པ་ནི་གདུལ་བའི་བསམ་པ་སྣ་ཚོགས་ཀྱི་ཕྱིར་རོ། །

[Block 1354]
བཅོམ་ལྡན་འདས་ཆོས་ཐམས་ཅད་ཀྱི་དག་པའི་ཕུང་པོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་ཕུང་པོ་དག་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1355]
བཅོམ་ལྡན་འདས་བར་ཆད་མང་དུ་མི་འབྱུང་བ་ནི་ངོ་མཚར་ཆེའོ་ཞེས་བྱ་བ་ནི་ལེགས་པར་འགྱུར་བ་ལ་བགེགས་མང་ངོ་སྙམ་དུ་བསམས་ནས་གསུངས་པའོ། །

[Block 1356 [HEADING]]
##### དམ་པའི་ཆོས་ཀློག་པའི་བསོད་ནམས། ^1-2-5-8-0

[Block 1357]
དེའི་འོག་ཏུ་དམ་པའི་ཆོས་ཀློག་པའི་བསོད་ནམས་བསྟན་པ་ནི་བརྡ་ཕྲད་སླའོ། །

[Block 1358]
ལྔ་བརྒྱ༌[^938]ཐ་མ་ཞེས་བྱ་བ་ནི་བརྒྱ་ཕྲག་ལྔ་བསྡུས་པ་ལ་ལྔ་བརྒྱ་ཞེས་བྱའོ། །

[Block 1359]
དེ་བཞིན་གཤེགས་པའི་དམ་པའི་ཆོས་གནས་པའི་དུས་ནི་ལོ་ལྔ་སྟོང་ངོ་ཞེས་གསུངས་སོ། །

[Block 1360]
ལོ་ལྔ་སྟོང་ལ༌[^939]ལོ་ལྔ་བརྒྱ་ལྔ་བརྒྱའི་དབང་དུ་བྱས་ལ་ཕྱེད་ཕྱེད་དུ་བཅད་ན༌[^940]ལྔ་བརྒྱ་ཕྲག་བཅུར་འགྱུར་རོ། །

[Block 1361]
དེ་ལ་ལེའུ་བཅུ་སྟེ་ཐོག་མར་ཁོང་དུ་ཆུད་པའི་ལེའུ་དང་། སྒྲུབ་པའི་ལེའུ་དང་། ལུང་གི་ལེའུ་སྟེ། ལེའུ་གསུམ་མོ། །

[Block 1362]
དེ་ལ་ཁོང་དུ་ཆུད་པའི་ལེའུ་ལ་ཡང་རྣམ་པ་གསུམ་དུ་དབྱེ་སྟེ། དགྲ་བཅོམ་པའི་ལེའུ་དང་། ཕྱིར་མི་འོང་བའི་ལེའུ་དང་། རྒྱུན་དུ་ཞུགས་པའི་ལེའུའོ། །

[Block 1363]
བསྒྲུབ་པའི་ལེའུ་ལ་ཡང་རྣམ་པ་གསུམ་དུ་དབྱེ་སྟེ། ལྷག་མཐོང་གི་ལེའུ་དང་། ཏིང་ངེ་འཛིན་གྱི་ལེའུ་དང་། ཚུལ་ཁྲིམས་ཀྱི་ལེའུའོ། །

[Block 1364]
ལུང་གི་ལེའུ༌[^941]ཡང་རྣམ་པ་གསུམ་དུ་དབྱེ་སྟེ། ཆོས་མངོན་པའི་སྡེ་སྣོད་དང་། མདོ་སྡེའི་སྡེ་སྣོད་དང་། འདུལ་བའི་སྡེ་སྣོད་དེ་ལེའུ་དགུ༌[^942]དང་། རྟགས་ཙམ་འཇིགས་པའི༌[^943]ལེའུ་དང་བཅུར་འགྱུར་རོ། །

[Block 1365]
དེ་ལ་ལེའུ་རེ་རེ་ལ་ཡང་ལོ་ལྔ་བརྒྱ་ལྔ་བརྒྱ་ཐོགས་ཏེ། དེ་ལྟར་ལེའུ་བཅུ་པོ་དག་གིས༌[^944]ལྔ་བརྒྱ་ཕྲག་བཅུ་ལ་ལོ་ལྔ་སྟོང་དུ་འགྱུར་རོ། །

[Block 1366]
དེ་ལ་ལྔ་བརྒྱ་ཐམས་ཅད་ཀྱི་དང་པོ་ལ་དགྲ་བཅོམ་པ། ལྔ་བརྒྱ་གཉིས་པ་ལ་ཕྱིར་མི་འོང་བ། ལྔ་བརྒྱ་གསུམ་པ་ལ་རྒྱུན་ཏུ་ཞུགས་པ། ལྔ་བརྒྱ་བཞི་པ་ལ་ལྷག་མཐོང་།

[Block 1367]
ལྔ་པ་ལ་ཏིང་ངེ་འཛིན།

[Block 1368]
དྲུག་པ་ལ་ཚུལ་ཁྲིམས།

[Block 1369]
བདུན་པ་ལ་ཆོས་མངོན་པ།

[Block 1370]
བརྒྱད་པ་ལ་མདོ་སྡེ།
--- END BLOCKS ---
