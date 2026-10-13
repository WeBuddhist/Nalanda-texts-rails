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
[Block 1261 [VERSE]]
དེ་ཚེ་ཤིན་ཏུ༌[^913]ཕྲ་ཞིང་ཟབ། །
དམ་ཆོས་འདི་ནི་གནས་མེད་པ། །
མངོན་སུམ་མིན་པ་ཇི་ལྟར་དུ། །
སེམས་ལ་བདེ་བླག་རྟོགས་པར༌[^914]འགྱུར། །

[Block 1262]
ཞེས་སོ། །

[Block 1263]
དེའི་སེམས་ལ་བདེ་བླག་ཏུ་འཇུག་པའི་ཕྱིར་དཔེ་མང་པོ་བསྟན་པ་ནི་རིགས་པ་ཉིད་དོ་ཞེས་བྱའོ། །

[Block 1264]
གཞན་ཡང་དཔེ་མང་པོ་ཉེ་བར་བཀོད་པས་འགའ་ཞིག་འགའ་ཞིག་ལ་ཤིན་ཏུ་ངེས་པར་འགྱུར་རོ་ཞེས་བྱ་སྟེ། དེ་ལ་དཔེ་དེས༌[^915]དེའི་དོན་བདེ་བླག་ཏུ་བདག་ཉིད་ཀྱིས་ཁོང་དུ་ཆུད་པས་དེས་ན་དཔེ་མང་པོ་ཉེ་བར་བསྡུ་བ་རིགས་པ་ཉིད་དོ། །

[Block 1265]
ཡང་ན་དངོས་པོར་འཛིན་པ་ཐ་དད་པས་དཔེ་ཐ་དད་པའོ། །

[Block 1266]
ཡུལ་དང་དུས་ངེས་པར་འཛིན་པ་ལ། མེད་པ་ལ་ཡུལ་དང་དུས་ངེས་པར་འཛིན་པ་མི་རུང་ཞེས་བྱ་སྟེ། དེ་ལ་ལྟོས་ནས་དྲི་ཟའི་གྲོང་ཁྱེར་དཔེར་བརྗོད་དོ། །

[Block 1267]
གཞན་དབང་དུ་འཛིན་པ་ལ། མེད་པ་ལ་རྒྱུ་གཞན་གྱི་དབང་ལས་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། དེ་ལ་ལྟོས་ནས་སྒྱུ་མ་དཔེར་བརྗོད་དོ། །

[Block 1268]
ལྡོག་པར་འཛིན་པ་ལ། མེད་པ༌[^916]ལྡོག་པ་མེད་དོ་ཞེས་བྱ་སྟེ། དེ་ལ་ལྟོས་ནས་སྨིག་རྒྱུ་དཔེར་བརྗོད་དོ། །

[Block 1269]
དེ་ཡང་བྱེ་བྲག་མེད་པར་ལྡོག་པའོ། །སྙིང་པོ་མེད་པར་འཛིན་པ་ལ། །

[Block 1270]
སྙིང་པོ་མེད་པས་དེ་མེད་དོ་ཞེས་བྱ་སྟེ། དེ་ལ་ལྟོས་ནས་དབུ་བ་དཔེར་བརྗོད་དོ། །

[Block 1271]
གཞན་དང་གཞན་དུ་འཛིན་པ་ལ། མེད་པ་ལ་གཞན་དང་གཞན་འབྱུང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། དེ་ལ་ལྟོས་ནས་ཆུའི་ཆུ་བུར་དཔེར་བརྗོད་དོ། །

[Block 1272]
ཀུན་ནས་སྣང་བར་འཛིན་པ་ལ། །མེད་པ་ལ་ཀུན་ནས་སྣང་བ་མེད་དོ་ཞེས་བྱ་སྟེ། དེ་ལ་ལྟོས་ནས་སྤྲུལ་པ་དཔེར་བརྗོད་དེ། །རྣམ་པ་སྣ་ཚོགས་པར་འཛིན་པ་ལ། མེད་པ་ལ་རྣམ་པ་སྣ་ཚོགས་པ་མེད་དོ་ཞེས་བྱ་སྟེ། དེ་ལ་ལྟོས་ནས་རྨི་ལམ་དཔེར་བརྗོད་དོ། །

[Block 1273]
འཇུག་པར་འཛིན་པ་ལ། མེད་པའི་མྱུ་གུ་ལ་སོགས་པ་ལ་འཇུག་པ་ལ་མི་ལྟོས་སོ་ཞེས་བྱ་སྟེ། དེ་ལ་ལྟོས་ནས་མགལ་མེའི་འཁོར་ལོ་དཔེར་བརྗོད་དོ། །

[Block 1274]
དེའི་འཇུག་པའི་ས་བོན་མགལ་མེ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱའོ། །

[Block 1275]
དེ་ལྟར་དེ་དག་འདས་མ་ཐག་པའི་ཚིགས་སུ་བཅད་པ་དྲུག་ཅུ་རྩ་བཞིས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཇི་ལྟ་བར་གནས་པའི་རང་བཞིན་བསྒྲུབས་ནས། དེ་ལས་གཞན་པའི་ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་དོན་འདི་ཉིད་དེ་བཞིན་གཤེགས་པས་གསུངས་པའི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཕྱིན་ཅི་མ་ལོག་པར་བཤད་པས། དེས་ན་ཤིན་ཏུ་ཡང་དེ་དང་འབྲེལ་པར་བསྒྲུབ་པར་བྱའོ། །

[Block 1276]
དེ་ལྟར་གྱུར་ན་ལེགས་པར་ཉན་པ་རྣམས་དོན་འདི་ལ་ཤིན་ཏུ་ངེས་པ་སྐྱེ་བར་འགྱུར་ཏེ།

[Block 1277 [HEADING]]
### ཚིགས་བཅད་རེ་བདུན་པ། ^1-66-0

[Block 1278 [VERSE]]
དངོས་ཀུན་རང་བཞིན་སྟོང་པས་ན། །
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་འདི། །
དེ་བཞིན་གཤེགས་པ་མཚུངས་མེད་ཀྱིས། །
དངོས་པོ་རྣམས་ནི་ཉེ་བར་བསྟན། །

[Block 1279]
དྲི་ཟའི་གྲོང་ཁྱེར་ལ་སོགས་པ་དང་འདྲ་བར་འདུ་བྱེད་རྣམས་ངོ་བོ་ཉིད་ཀྱིས་མ་གྲུབ་བོ་ཞེས་ཉེ་བར་བསྟན་པའི་དོན་དུ་འདི་དག་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའོ་ཞེས་གསུངས་སོ། །

[Block 1280]
མཚུངས་མེད་ཀྱིས་ཞེས༌[^917]པ། འཇིག་རྟེན་གྱི་ཁམས་གཅིག་ཏུ༌[^918]བརྩམས་ནས་འཇིག་རྟེན་གྱི་ཁམས་གཞན་ན་ཡང་དེ་བཞིན་གཤེགས་པ་འདྲ་བའི་དེ་བཞིན་གཤེགས་པ་ཡོད་པ༌[^919]མ་ཡིན་ནོ། །

[Block 1281]
ཡང་ན་ཤཱཀྱ་ཐུབ་པ་གཽ་ཏ་མའོ་ཞེས་སྨྲ་ན་བརྩད་པ་འདི་དག་ཏུ་འགྱུར་ཏེ། དེ་བཞིན་གཤེགས་པའི་སྒྲ་འདི་ནི་ཡང་དག་པ་ཇི་ལྟ་བར་སྟོན་པའི་ཡོན་ཏན་ལ་བརྟེན་ནས་འཇུག་ལ། དེ་ཡང་སངས་རྒྱས་ཐམས་ཅད་ལ་ཐུན་མོང་དུ་གྲུབ་བོ་ཞེས་བྱ་སྟེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་མཚུངས་མེད་ཅེས་བྱའོ། །

[Block 1282]
ལྷག་མ་བཤད་ཟིན་ཏོ། །

[Block 1283]
དེ་ནི༌[^920]དྲི་ཟའི་གྲོང་ཁྱེར་ལ་སོགས་པ་འདི་དག་གི་རང་བཞིན་མེད་པའི་དོན་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་ནི༌[^921]དམ་པ་ཉིད་དུ་ཉེ་བར་མཚོན་པར་གསུངས་པ།

[Block 1284 [HEADING]]
### ཚིགས་བཅད་རེ་བརྒྱད་པ། ^1-67-0

[Block 1285]
འདི་ཙམ་རེ་ཞིག་དོན་དམ་སྟེ། །ཞེས་པ་ལ་དངོས་པོར་རྟོག་པ་ཐམས་ཅད་ཇི་ལྟ་བའི་དོན་མ་ཡིན་པའི་ཕྱིར། འདི་ནི་རེ་ཞིག་ཅེས་པ་ངེས་པར་གཟུང་བ་སྟེ། ཉེ་བར་བསྒྲུབས་པའི༌[^922]ཆོས་ཐམས་ཅད་རང་བཞིན་མེད་པ་ཉིད་དོ། །

[Block 1286]
སྟོང་པ་ཉིད་དེ་ལ་ཇི་སྲིད་དུ་དངོས་པོར་མངོན་པར་ཞེན༌[^923]པ་ཐམས་ཅད་འདིར་ཕྱིན་ཅི་ལོག་པས་འཁྲུལ་པ་སྟེ། འཁྲུལ་པ་ཡང་དོན་དམ་པ་ཡིན་པར༌[^924]ནི་མི་རིགས་སོ། །

[Block 1287]
འདི་ཉིད་ཡོད་པ་དང་མེད་པས་མ་བསྡུས་པས་སྐྱོན་གྱིས་རྣམ་པར་དབེན་པ། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་གསུངས་པ་ལས་དབུ་མ་ཁོང་དུ་ཆུད་པ་ནི་དོན་དམ་པ་ཉིད་དོ་ཞེས་གསུངས་པ།

[Block 1288 [VERSE]]
འདི་ཙམ་རེ་ཞིག་དོན་དམ་སྟེ། །
འཇིག་རྟེན་ཐ་སྙད་ལ་བརྟེན་ནས། །
སྣ་ཚོགས་ཐམས་ཅད་བཅོམ་ལྡན་འདས། །
སངས་རྒྱས་བདེན་པར་གདགས་པ་མཛད། །

[Block 1289]
ཅེས་པ་ལ་ཇི་ལྟར་རྨི་ལམ་མཐོང་བ་འགའ་ཞིག་གི༌[^925]རྨི་ལམ་རྨིས་པའི་སེམས་འགའ་ཞིག་རྣམ་པར་ཤེས་ནས་དེ་ནི་བདེན་པར་སྨྲའོ་ཞེས་བརྗོད་ཅིང་། དེ་རིང་རྨི་ལམ་དུ་མས༌[^926]མགོ་ལའོ་བྱས་ཤིང་ཕས༌[^927]སོ་སོར་བསྔགས་པ་བརྗོད། སྐྱེད༌[^928]མོས་ཚལ་བཙོངས་ནས་སྟོང་ཕྲག་གཅིག་བྲམ་ཟེ་ལ་བྱིན་པ་དང་། བསྐོར་བ་བྱེད་པ་མཐོང་ཞེས་སོ། །

[Block 1290]
དེ་བཞིན་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་བྱིན་པས༌[^929]མངོན་པར་ཞེན་པ་ལྟར་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་ལ་སོགས་པའི་དབྱེ་བ་ཐ་དད་དང༌[^930]དངོས་པོ་ཐམས་ཅད་མེད་པར་ཐ་སྙད་ཀྱིས་གསུངས་པར་འགྱུར་རོ། །

[Block 1291]
དེ་ལ་རྨི་ལམ་དུ་མཐོང་བའི་མ་ལ་སོགས་པ་ཉིད་ལ་བདེན་པར་མངོན་པར་འདོད་པ་དེའི་ངོ་བོ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1292]
དེ་བཞིན་དུ་བྱིས་པ༌[^931]ཕྱིན་ཅི་ལོག་པ་རྣམས་ཀྱིས་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་ལ་སོགས་པ་མངོན་པར་བརྗོད་ཀྱི་སངས་རྒྱས་རྣམས་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1293]
ལྷག་མ་བཤད་ཟིན་ཏོ། །

[Block 1294]
མྱ་ངན་ལས་འདས་པ་དང་མཚུངས་པར་ཆོས་ཐམས་ཅད་རང་བཞིན་མེད་པ་ལ་གནས་པའི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་སོ་ཞེས་བྱ་སྟེ། སྤྲོས་པ་ག་ལ་ཞིག

[Block 1295]
།ཇི་སྐད་དུ་མདོ་ལས།

[Block 1296]
ཚེ་དང་ལྡན་པ་ཀུན་དགའ་བོ་རེག་པའི་སྐྱེ་མཆེད་དྲུག་པོ་ཟད་པ་དང་། འདོད་ཆགས་དང་བྲལ་བ་དང་། འགགས་པ་དང་། ཉེ་བར་ཞི་བ་དང་། ནུབ་པར་གྱུར་པ་འདི་ལས་གཞན་པའི་སྤྲོས་པས་སྤྲོས་པར་བྱེད་པ་ཡོད་དམ་ཞེས་པ་དང་། ཡོད་པ་དང་མེད་པ་ཞེས་པའི་སྤྲོས་པས་སྤྲོས་པར་བྱེད་དམ་ཞེས་པ་ནས། ཚེ་དང་ལྡན་པ་ཀུན་དགའ་བོ་སྐྱེ་མཆེད་དྲུག་ནི་སྤྲོས་པའོ། །

[Block 1297]
སྐྱེ་མཆེད་དྲུག་འགག་པ༌[^932]ལས་སྤྲོས་པ་མེད་པའོ་ཞེས་པའི་བར་དུ་མྱ་ངན་ལས་འདས་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་སོ། །

[Block 1298]
དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཀྱི་དབང་གིས་ན་དོན་དམ་པའོ། །

[Block 1299]
འཇིག་རྟེན་པའི་ཤེས་པའི་དབང་གིས་ཀྱང་ཀུན་རྫོབ་བོ་ཞེས་གནས་སོ། །

[Block 1300]
དེ་ཉིད་ཀྱིས་ན།
--- END BLOCKS ---
