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
མདོ་ལས།

[Block 1402 [HEADING]]
###### **མཆོད་རྟེན་བྱས་པ།** ^4-2-11-1-1-2-5-2-1-2-2-2-0

[Block 1403]
གང་གིས་རིང་བསྲེལ༌[^1273]ལ་ནི་མཆོད་བྱེད་པ། །ཞེས་པ་ནས། །དེ་དག་གིས་ཀྱང་བྱང་ཆུབ་ཐོབ་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་ཕྱེད་དང་ལྔས་མཆོད་རྟེན་བྱས་པས་བྱང་ཆུབ་ཐོབ་པ་བསྟན་པ་སྟེ། དེ་ལ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 1404]
ཐོག་མའི་ཚིགས༌[^1274]བཅད་བཞིས་ནི་མཆོད་རྟེན་བྱས་པ་བསྟན་ཏོ། །

[Block 1405]
འོག་མའི་ཚིགས༌[^1275]བཅད་ཕྱེད་ཀྱིས་ནི་མདོར་བསྡུས་པ་བསྟན་ཏོ། །

[Block 1406]
ཐོག་མའི་ཚིགས༌[^1276]བཅད་ལ་རྣམ་པ་གསུམ་སྟེ། ཐོག་མའི་ཚིག་གཉིས་ཀྱིས་ནི་མཆོད་རྟེན་མང་པོ་ལ་རིན་པོ་ཆེས་བརྒྱན་པ་བསྟན་ཏོ། །

[Block 1407]
ཚིག་གཅིག་གིས་ནི་རྣམ་པ་ལས༌[^1277]མཆོད་རྟེན་བྱས་པ་བསྟན་ཏོ། །

[Block 1408]
ཚིག་གཅིག་གིས་ནི་རྩེད་མོའི་ཕྱིར་བྱེ་མ་ལས་མཆོད་རྟེན་བྱས་པ་བསྟན་པ་སྟེ། གང་གིས༌[^1278]མཆོད་རྟེན་བྱས་ན་ཚངས་པའི་རྒྱལ་པོའི་བསོད་ནམས་དང་མཉམ་མོ། །

[Block 1409]
ཚངས་པའི་བསོད་ནམས་ནི་གླིང་བཞི་དང་། འདོད་པའི་ཁམས་དྲུག་གི༌[^1279]ལྷའི་བསོད་ནམས་དང་མཉམ་སྟེ་མཆོད་རྟེན་བྱས་ནས་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1410]
མདོ་ལས།

[Block 1411]
གང་གིས་མཆོད་རྟེན་རྡོ་ཡི་སྙིང་ལས༌[^1280]བྱས། །ཞེས་པ་ནས། རྒྱལ་བའི་མཆོད་རྟེན་དགའ་བཞིན་བྱས་པ་དང་། །ཞེས་པའི་བར་དུ་ཚིག་གཅིག་གིས་ནི་རྣམ་པ་དགུ་ལ་མཆོད་རྟེན་དུ་བྱས་པ་བསྟན་པའོ།[^1281]

[Block 1412]
།མདོ་ལས།

[Block 1413]
དེའི་ཕྱིར་རྡུལ་གྱི་ཕུང་པོ་དག་ལས་ཀྱང་། །ཞེས་པ་ནས། དེ་རྣམས་ཀྱིས་ཀྱང་བྱང་ཆུབ་ཐོབ་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ཚིག་གཅིག་གིས་ནི་རྩེ་བའི་ཕྱིར་དངོས་པོ་རིན་ཆུང་བ་ལ་མཆོད་རྟེན་བྱས་ཀྱང་བྱང་ཆུབ་ཏུ་འགྱུར་རོ་ཞེས་བསྟན་ཏེ། བྱེ་མ་ལས་ཕུང་པོ་བྱས་ཏེ། རྒྱལ་བའི་མཆོད་རྟེན་བྱས་ན་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་བ་ནི་གང་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ། བྱང་ཆུབ་སེམས་དཔའི་སྤྱད་པ་སྤྱོད་པ། དགེ་བའི་རྩ་བ་གང་བྱས་ཀྱང་བྱང་ཆུབ་ཐོབ་པར་བྱེད་པ་ལ་བྱ་བའི་མ་རབས་མ་ངེས་པའི་རིགས་ཅན་ཉན་ཐོས་སམ་བྱང་ཆུབ་ཏུ་སེམས་མ༌[^1282]བསྐྱེད་པ་ནི་ཐོབ་པར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 1414]
དེའི་ཚུལ་དུ་ཆུང་ངུ་ནས༌[^1283]ཐལ་མོ་སྦྱར་ཏེ་བཏུད་པ་ཙམ་ཡང་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་ཞེས་བརྗོད་པ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 1415]
མདོ་ལས།

[Block 1416 [HEADING]]
###### **སྐུ་གཟུགས་བྱས་པ།** ^4-2-11-1-1-2-5-2-1-2-2-3-0

[Block 1417]
ལ་ལས་དེ་བཞིན་རིན་ཆེན་གཟུགས་བྱས་པ། །ཞེས་པ་ནས། དེ་དག་ཐམས་ཅད་བྱང་ཆུབ་ཐོབ་པར་འགྱུར།[^1284] །ཞེས་པའི་བར་དུ་ཚིག་དྲུག་གིས༌[^1285]སྐུ་གཟུགས་བྱས་པ་བསྟན་ཏེ། [^1286]དེ་ལ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 1418]
ཚིག་ལྔས་ནི་སྐུ་གཟུགས་བྱས་པ་བསྟན། ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་མདོར་བསྡུས་པ་བསྟན་ཏོ། །

[Block 1419]
སྐུ་གཟུགས་བྱེད་པ་ཡང་གཞོག་པ་དང་རི་མོར༌[^1287]བྲི་བ་ལ་སོགས་པའོ། །

[Block 1420]
མདོ་ལས།

[Block 1421]
ལ་ལས་དེ་ནི་རིན་ཆེན་སྣ་བདུན་དང་། །ཞེས་པ་ནས། དེ་དག་ཐམས་ཅད་བྱང་ཆུབ་ཐོབ་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ཚིག་གཉིས་ཀྱིས་རིན་པོ་ཆེ་ལ་སོགས་པས་སྐུ་གཟུགས་བྱས་པ་བསྟན་པའོ། །

[Block 1422]
མདོ་ལས།

[Block 1423]
གང་གིས་རྩིག་ངོས་སྐུ་གཟུགས་བྲིས་པ་སྟེ། །ཞེས་པ་ནས། དེ་དག་ཐམས་ཅད་བྱང་ཆུབ་ཐོབ་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ཚིགས༌[^1288]བཅད་འདིས༌[^1289]ནི་སྐུ་གཟུགས་རི་མོར་བྲིས་པ་བསྟན་པའོ། །

[Block 1424]
མདོ་ལས།

[Block 1425]
ལ་ལ༌[^1290]དེ་ནི་སློབ་པའི་ཚེ་ནའང་རུང་། །ཞེས་པ་ནས། [^1291]དེ་དག་ཐམས་ཅད་བྱང་ཆུབ་ཐོབ་པ་ཡིན། ། ཞེས་པའི་བར་དུ་ཚིགས༌[^1292]བཅད་འདིས༌[^1293]ནི་རྩེད་མོ་ལས་སྐུ་གཟུགས་བྲིས་པ་བསྟན་པའོ། །

[Block 1426]
མདོ་ལས།

[Block 1427]
དེ་དག་ཐམས་ཅད་སྙིང་རྗེ་ཅན་དུ་འགྱུར། །ཞེས་པ་ནས། བྱང་ཆུབ་སེམས་དཔའ་མང་པོ་རབ་ཏུ་འཛུད། །ཞེས་པའི་བར་དུ་ཚིགས༌[^1294]བཅད་འདིས༌[^1295]ནི་མདོར་བསྡུས་པ་བསྟན་པ་སྟེ། གང་སྙིང་རྗེ་ཆེན་པོའི་སེམས་དང་ལྡན་པ་ནི་དགེ་བ་ཅི་བྱེད་ཀྱང་སྙིང་རྗེའི་སེམས་དང་བཅས་པས་ཕ་རོལ་ཏུ་ཕྱིན་ཅིང་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1428]
མདོ་ལས།

[Block 1429 [HEADING]]
###### **མཆོད་པ་བྱས་པ།** ^4-2-11-1-1-2-5-2-1-2-2-4-0

[Block 1430]
དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་རིང་བསྲེལ་དང་། །ཞེས་པ་ནས། དེ་ལ་མེ་ཏོག་དང་ནི་སྤོས་གསོལ་ཏེ། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་བདུན་གྱིས་མཆོད་པ་བྱ་བ་བསྟན་ཏེ། དེ་ལ་ཚིགས༌[^1296]བཅད་ཕྱེད་དང་དྲུག་གིས་ནི་མཆོད་པ་བྱ་བ་བསྟན་ཏོ། །

[Block 1431]
ཕྱེད་དང་གཉིས་ཀྱིས་མདོར་བསྡུས་པ་བསྟན་ཏོ། །

[Block 1432 [HEADING]]
###### **དངོས་པོ་བཞིས་མཆོད་པ།** ^4-2-11-1-1-2-5-2-1-2-2-4-1-0

[Block 1433]
དེ་ལ་ཚིགས་བཅད་གཅིག་གིས་ནི་དངོས་པོ་བཞིས་མཆོད་པ་བྱ་བ་བསྟན། ཚིགས་བཅད་གཅིག་གིས་ནི་རོལ་མོས་མཆོད་པ་བྱ་བ་བསྟན། ཚིགས་བཅད་གཅིག་གིས་ནི་དབྱངས་ཀྱིས་མཆོད་པ་བྱ་བ་བསྟན། ཚིགས་བཅད་གཅིག་གིས་ནི་ལུས་ཀྱི་ལས་ཀྱིས༌[^1297]མཆོད་པ་བྱ་བ་བསྟན་ཏོ།[^1298] །མེ་ཏོག་གིས་མཆོད་པས་བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན་གྱི༌[^1299]མེ་ཏོག་འཐོབ་པོ། །སྤོས་ཕུལ་བས་ཆོས་ཀྱི་སྐུའི་གསུང་ཐོབ་པོ། །བ་དན་ཕུལ་བས་གཟུངས་ཐོབ་ཅིང་སྡིག་པ་ལས་བཟློག་པར་འགྱུར་རོ། །

[Block 1434]
གདུགས་ཕུལ་བས་ཚད་མེད་པ་བཞིས་སེམས་ཅན་འགེབས་པར་འགྱུར་རོ། །

[Block 1435]
མདོ་ལས།

[Block 1436 [HEADING]]
###### **རོལ་མོས་མཆོད་པ།** ^4-2-11-1-1-2-5-2-1-2-2-4-2-0

[Block 1437]
དེར་ནི་གང་གིས་སིལ༌[^1300]སྙན་བརྡུང་བཅུག་པ། །ཞེས་པ་ནས། ཆུ་ལ་བརྡབས་དང་ཐལ་མོ་བརྡབས།[^1301] །ཞེས་པའི་བར་དུ་ནི་རོལ་མོས་མཆོད་པ་བྱ་བ་བསྟན་པ་སྟེ། མདོ་ལས་རོལ་མོ་དང་ན་ཆུང་བཟང་མོ་ཕ་རོལ་གྱི་སེམས་འཕྲོག་པས་སྦྱིན་པར་མི་བྱའོ་ཞེས་འབྱུང་སྟེ། སངས་རྒྱས་ལ་མཆོད་ན་འགལ་བ་མེད་དོ། །

[Block 1438]
མདོ་ལས།

[Block 1439 [HEADING]]
###### **དབྱངས་ཀྱིས་མཆོད་པ།** ^4-2-11-1-1-2-5-2-1-2-2-4-3-0

[Block 1440]
བདེ་བར་གཤེགས་པ་དེ་ལ་མཆོད་པའི་ཕྱིར། །ཞེས་པ་ནས། རིང་བསྲེལ་དེ་ལ་རྣམ་པ་མང་པོས་མཆོད། །ཅེས་པའི་བར་དུ་ནི་ཚིགས་བཅད་འདིས་དབྱངས་དང་གླུ་སྙན་པས་མཆོད་པ་བྱས་པ༌[^1302]བསྟན་པ་སྟེ། ཚངས་པའི་དབྱངས་ཐོབ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
