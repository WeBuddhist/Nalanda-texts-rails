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
[Block 1471]
སྲིན་བུ་རྣམས་ཀྱི༌[^1264]ཚིལ་འཚལ་བར་བགྱིའམ། འཚལ་བར་མི་བགྱི། བཀའ་སྩལ་པ་བཟའ་བར་མི་བྱའོ། །

[Block 1472]
ནད་དང་བྲལ་བའི་ཕྱིར་ལུས་བསྐུ་བར་ནི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1473]
གཞན་ངང་སྐྱ་ལ་སོགས་པ་རྣམས་ནི་དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས་སོ། །

[Block 1474]
ལྷག་མ་རྣམས་ནི་སིལ་བུ་དག་ལས་སོ། །

[Block 1475]
ཤའི་བྱིན་ལེན་སྟོབས་པ་ལ་བཅད་པ་ལས་བྱུང་བ་ཉིད་མ་ཡིན་ནམ་ཞེས་དྲི་བར༌[^1265]བྱའོ་ཞེས་བྱ་བ་ནི་མི་ལ་སོགས་པའི་ཤ་བཅད་པ་གང་ཡིན་པ་དེ་བྱུང་བ་ཉིད་མ་ཡིན་ནམ་ཞེས་བྱ་བ་དང་། བཅས་པར་དྲི་བར༌[^1266]བྱའོ། །

[Block 1476]
དེ་མི་ལ་སོགས་པ་མ་ཡིན་ནམ༌[^1267]ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 1477]
དུ་མ་ཉིད་ཡིན་ན་དང་པོས་སོ་ཞེས་བྱ་བ་དང་། ཟ་བ་པོ་དུ་མ་ཉིད་ཡོད་ན་དང་པོས་དྲི་བར་བྱ་བ་སྟེ། དགེ་འདུན་གྱི་གནས་བརྟན་གྱི་ཆོས་ཉིད་ཀྱིས་གསུངས་པ་དེ་འདིར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1478]
དེ་བས་ན་དེ་ལྟར་ཉེ་བར་སྦྱར་བའོ། །

[Block 1479]
ཉམས་ན་འོག་མས་སོ་ཞེས་བྱ་བ་ནི་ཤའི་སྐབས་དྲིའོ༌[^1268]ཞེས་བྱ་བར་སྦྱར་ཏེ། དང་པོས་དྲི་བ་ཉམས་ན་འོག་མས་དྲི་བར་བྱ་ཞེས་བྱ༌[^1269]བའི་དོན་ཏོ། །

[Block 1480]
གླང་པོ་ཆེ་དང་མིའི་འོ་མ་དག་བཏུང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གླང་པོ་ཆེ་ཞེས་བྱ་བ་གཞན་དུ་རིགས༌[^1270]ཙམ་པོའི་གཙོ་བོ་ལ་བརྟེན་ནས་མོའི་རྐྱེན་མ་བསྐྱེད་པ་སྟེ། དེ་ལྟ་བུའི་སྦྱོར་བ་ཡང་མཐོང་སྟེ་རིགས༌[^1271]ཀྱིའོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1481]
ཞུ་བའི་གཞུང་ཁ་ཅིག་ལས།

[Block 1482]
བཙུན་པ་གླང་མོའི་འོ་མ་འམ་ཞོ་ལོངས་སྤྱད་དུ་རུང་ངམ། ཉེ་བ༌[^1272]འཁོར་མི་རུང་ངོ་། །གང་ཞིག་ལོངས་སྤྱོད་པར༌[^1273]བྱེད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1483]
གཞན་དུ་མིའི་བུད་མེད་ཀྱི་འོ་མ་བཏུང་དུ་རུང་ངམ་མི་རུང་། བཀའ་སྩལ་པ། མི་རུང་ངོ་། །འོན་ཀྱང་ལུས་ལ་བསྐུ་བར༌[^1274]བྱའོ་ཞེས་གསུངས་པ་དེ་གཉིས་ཀ་བསྡུས་ནས་སྨོས་པ་ཡིན་ནོ། །

[Block 1484]
པགས་པ་དང་རྨར༌[^1275]བསྐུ་བ་དང་སྣར་བླུགས་པ༌[^1276]དང་། མིག་སྐུད་ཅིང་བཟའ་བཏུང་མི་བྱེད་པ་ལ་ནི་སྐྱོན་ཆགས་པ༌[^1277]མེད་དོ་ཞེས་བྱ་བ་ནི་དེ་དག་གིས༌[^1278]པགས་པ་སྐུད་པ་དང་། རྨ་སྐུད་པ་དང་། སྣར་བླུགས་པ་དང་མིག་སྐུད་ཅིང་བཟའ་བཏུང་མི་བྱེད་པ༌[^1279]ལ་ནི་སྐྱོན་ཆགས་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1485]
འདིར་གཞུང་ནི།

[Block 1486]
དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 1487]
བཙུན་པ་སྨན་རུང་བ་མ་ལགས་པ་དག་དང་བསྐོལ་བའི་འབྲུ་མར་འཚལ་དུ་རུང་ངམ་ཉེ་བ༌[^1280]འཁོར་མི་རུང་ངོ་། །ལུས་སྐུད་པ་དེ༌[^1281]དང་། རྨའི་བསྐུ་མཉེ་བྱ་བ་དང་། སྣར་ལྡུགས་པའི་ལས་བྱ་བ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1488]
བཙུན་པ་བུད་མེད་ཀྱི་འོ་མ་འཚལ་དུ་རུང་ངམ། ཉེ་བ༌[^1282]འཁོར་མི་རུང་ངོ་། །མིག་ལ་སྐུད་པ་ལ༌[^1283]ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1489]
ལུས་སྐུད་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 1490]
སྔར་ཞུ་བ་ལས་གསུངས་སོ། །

[Block 1491]
ནད་པས་ནི་ཞུན་མར་དང་འབྲུ་མར་ཆང་དང་འདྲེས་པ་བཏུང་བར་བྱ་བ་ཉིད་དོ། །

[Block 1492]
ཆང་མ་ཡིན་པ་ཉིད་ནི་ཉེས་པ་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ།

[Block 1493]
ནད་པ་ཞེས་བྱ་བ་ནི་འདིར་བཏུང་བ་པོའི་ཡུལ་ལ་ཞུ་བ་ལས།

[Block 1494]
འདི་ནི་དང་པོ་སྟེ་བསྐོལ༌[^1284]ན་རུང་ངོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 1495]
ཆང་མ་ཡིན་པ་ཉིད་ན་ཞེས་བྱ་བ་ནི་ཆང༌[^1285]མ་ཡིན་པ་ཉིད་དུ་གྱུར་ན་ཉེས་པ་མེད་དོ། །

[Block 1496]
བཏུང་དུ་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1497]
དེའི་དྲི་དང་རོ་དག་ཀྱང་གང་དུ་བྲལ་བ་ཉིད་དེ་ནི་འདིར་ཆང་མ་ཡིན་པ་ཉིད་དུ་གསུངས་སོ། །

[Block 1498]
དེའི་ཕྱིར་ཆང་གི་དྲི་དང་རོ་མྱང་བ༌[^1286]མྱོས་པར་མི་བྱེད་པ་དག་ཅེས་གསུངས་པ་ལས་ཤེས་པར་བྱའོ། །

[Block 1499]
དེ་ནི་བསྐོལ་བ་ལས་འགྲུབ་པོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ལ༌[^1287]ནི་ཆང་མ་ཡིན་པ་ཉིད་དེ་ནི་བསྐོལ་བ་ལས་ཆང་མ་ཡིན་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1500]
འདིར་གཞུང་ནི། བཙུན་པ་མྱོས་པར་འགྱུར་བའི་བཏུང་བ་ཞུགས་ཀྱིས་བསྐོལ་ནས༌[^1288]འཚལ་དུ་རུང་ངམ་ཉེ་བ༌[^1289]འཁོར་རུང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1501]
གོས་ཀྱི་གཞི་ལས་སྨོས་པའི་ཚ་ཉིད་དུ་སྒྲུབ་པར་བྱེད་པའི་ཆང་གི་ཆོ་ག་བརྗོད་པའི་ཕྱིར། དེ་ནི་ནས་རྔོས་པས༌[^1290]གདབ་ཅིང་སའི་སྟེང་དུ་བཅུག་པ་ཚ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1502]
རྒུན༌[^1291]གྱི་ཁུ་བ་ནི༌[^1292]བསྐོལ་ན་ཆང་ཉིད་དུ་མི་འགྱུར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ་འདིར་གཞུང་ནི། བསྐོལ༌[^1293]ཏེ་གཞག་པར་བྱ་ཞིང་དགེ་འདུན་གྱི༌[^1294]དུས་མ་ཡིན་པའི་བཏུང་བར་འགྱུར་རོ་ཞེས་གསུངས་བའི་དགོངས་པ་ལ་འདི་སྨོས་པ་ཡིན་ནོ། །

[Block 1503]
ཐ་དད་པ་མ་ཡིན་པ་ཉིད་ལ་ནི་ཡོད་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཐ་དད་པ་མ་ཡིན་པ་དེ་ནི་ཐ་མི་དད་པར་གྱུར་པའོ། །

[Block 1504]
དཔེར་ན་ཏིལ་རྣམས་ལ་ཏིལ་མར་དང་། བུ་རམ་ཤིང་ལ་ཁུ་བ་དང་། དེ་ལ་ཡང་བུ་རམ་ཡོད་པ་ཉིད་མ་ཡིན་པ༌[^1295]ལྟ་བུའོ། །

[Block 1505]
དེ་ལྟ་བས་ན་ཏིལ་ལ༌[^1296]བྱིན་ལེན་བྱས་པས་ཏིལ་མར་ལ་བྱིན་ལེན་བྱས་པར་མི་འགྱུར་ལ། བུ་རམ་ཤིང་ལ་བྱིན་ལེན་བྱས་པས་བུ་རམ་བྱིན་ལེན་བྱས་པར་མི་འགྱུར་བར་ཤེས་པར་བྱའོ། །

[Block 1506]
བག་ཆགས་སུ་གྱུར་པ་ཉིད་ནི་ཡོད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། འདིར་གཞུང་ནི། ཞག་རུང་བ་མ་ལགས་པ་དག་བསྐོལ་བའི་དཔོན་ཚ༌[^1297]འཚལ་དུ་རུང་ངམ་མི་རུང་བཀའ་སྩལ་པ། ནད་པས་ནི་བཟར༌[^1298]རུང་ལ་མིན་པས༌[^1299]ནི་མི་རུང་ངོ་། །ཤ་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་གང་ཞིག་ཞུས་པ་ལས་རྫས་རུང་བ་མ་ཡིན་པ་དང་འབགས་པ་བཟའ་བར་བྱ་བ་ཉིད༌[^1300]མ་ཡིན་ཞེས་གསུངས་པ་དེ་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 1507]
ཆང་གི་སྲིད་པ༌[^1301]དང་བྲལ་བར་བྱ་བའི་ཕྱིར་རྩ་བ་དང་། སྡོང་བུ་དང་། འདབ་མ་དང་། མེ་ཏོག་དང་། འབྲས་བུའི་སྨན་སྐམ་པོའི་ཕྱེ་མ་ཆང་གི་དྲིས་བསྒོས་པ༌[^1302]ཆུ་དང་སྦྱར་བ་བཏུང་ངོ་ཞེས་བྱ་བ་ནི་ཆང་གི༌[^1303]དྲིས་བསྒོས་པའི་རྩ་བ་ལ་སོགས་པའི་སྨན་རྣམས་ལ་སྐམ་པོའི༌[^1304]ཕྱེ་མ་དང་སྦྱར་བའི་ཆུས་སོ། །

[Block 1508]
འདིར་གཞུང་ནི།

[Block 1509]
སིལ་བུ་དག་ལས།

[Block 1510]
དེ་ལྟ་བས་ན་ཆང་དུ་རུང་བའི་རྩ་བ༌[^1305]དང་སྡོང་བུ་ལ་སོགས་པའི་རྫས་སྐམ་པོ་གང་དག་ཡིན་པ་དེ་དག༌[^1306]ཕྱེ་མར་བྱས་ཏེ། རས་མ་དཀར་པོས་ཕུལ༌[^1307]ཏེ་ཆང་གི༌[^1308]ཤུགས་དང་བྲལ་བའི་སྣོད་མ་གང་བར་བཅང་བར་བྱ་ཞིང་དེ་ནས་ཕྱུང་སྟེ། བྱི་དོར་བྱས་ནས་ཟས་དང་མ་འབགས་པའི་ཆུ་དང་ལྷན་ཅིག་སྦྱར་ཞིང་བཙགས་ཏེ་བཏུང་བར་རྗེས་སུ་གནང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
