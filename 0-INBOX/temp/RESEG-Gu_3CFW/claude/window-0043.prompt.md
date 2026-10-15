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

[Block 1511]
ཆང་དང་བཅས་པའི་སྣོད་དུ༌[^1309]སྦྱངས་ཏེ་གཞག་པར་བསྒོ་བར་བྱའོ། །

[Block 1512]
རེག་པ་བསྲུང་ངོ་ཞེས་བྱ་བ་ནི་ཕྱེ་མའི་ཕུར་མ་དེ་ཆང་དང་རེག་པར་མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་བསྲུང་བར་བྱའོ། །

[Block 1513]
དེའི་ཕྱིར་མ་གང་བ༌[^1310]དང་ཤུགས་དང་བྲལ་བ་ཉིད་དུའོ་ཞེས་བྱ་བ་ནི་ཆང་གིས༌[^1311]མ་གང་བའི་སྣོད་དང་བཅས་པ་ལ་ཆང་གི༌[^1312]ཤུགས་དང་བྲལ་བ་ཉིད་ནི་དེའི་སྣོད་དུ་གཏོགས་པའི་ཆང་ལའོ། །

[Block 1514]
གཞན་དུ་ན་གྱེན་དུ་བཏུང་བས་རེག་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1515]
དེ་བཞིན་དུ་རོ་མེད་པར་བྱེད་པ་དང་། དུས་མ་ཡིན་པར་བཏུང་བ་ལ་ཟས་དང་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཕྱེ་མ་ཆང་དང་རག་པ༌[^1313]བསྲུང་བ་དེ་བཞིན་དུ་རོ་མེད་པར་གྱུར་པའི་རྫས་ཀྱིས་ཀྱང་དུས་མ་ཡིན་པར་བཏུང་བར་འདོད་པའི་ཟས་དང་རེག་པ་བསྲུང་བར་བྱའོ། །

[Block 1516]
མཛེས་པ་ཡང་བཟང་ངོ་ཞེས་བྱ་བ་ནི་ཕྱེ་མ་སྐམ་པོ་ཆང་གི་དྲིས་བསྒོས་པ་དང་སྦྱར་བའི་ཆུ་བཟང་བའོ། །

[Block 1517]
གང་གི་ཕྱིར་དེ་ལྟར་བསྲུང་བར་བྱ་བ་ཉིད་མཛེས་པ་ཡིན་ཏེ། དེའི་ཕྱིར་རས་མ་དཀར་པོས་བཙགས་པར་བྱའོ། །

[Block 1518]
ནད་པས་ཆང་ནི་རྩ་མཆོག༌[^1314]གིས་ཀྱང་མི་བཏུང་ངོ་ཞེས་བྱ་བ་འདི་ནི་བཅས་པའི་ཁ་ན་མ་ཐོ་བ་དང༌[^1315]བཅས་པ་ཐམས་ཅད་གནང་བའི་ཡུལ་ལ་རྗེས་སུ་གནང་བ་དེ་ནི་དམིགས་ཀྱིས་བསལ་བ་ཡིན༌[^1316]ཏེ། ཇི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་ཤཱཀྱ་ན་བར་གྱུར་པ་དག་ལ་དེ་ཉིད་མ་གནང་བར་གསུངས་པ་ཡིན་ནོ། །

[Block 1519]
དེ་ལྟར་དགེ་སློང་དག་ང་ལ་སྟོན་པ་ཞེས་ཟེར་བ་ཁྱེད་ཅག་གི་ཚང་རྩྭ༌[^1317]མཆོག་གིས་ཀྱང་མི་བླུད་མི་བཏུང་ངོ་ཞེས་གསུངས་པ་དེ་བས་མདོ་འདི་བྱས་སོ། །

[Block 1520]
དགེ་བསྙེན་ཡན་ཆད་ཀྱིས་མི་བླུད་ཅིང༌[^1318]ཞེས་བྱ་བ་ནི་འདིར་ཡན་ཆད་ཀྱི་སྒྲ་བྲིས་པར་རིག་པར་བྱའོ། །

[Block 1521]
དགེ་བསྙེན་གྱི་མཐའ་ཡན་ཆད་ཆོས་འདི་པ་བསླབ་པ་མ་བླངས་པ་ཐམས་ཅད་ཀྱིས་ཀྱང་ཆང་བླུད་པར་མི་བྱའོ། །

[Block 1522]
དགེ་བསྙེན་གྱིས་མི་བྱ་བའི་ལས་དྲུག་སྟེ། སེམས་ཅན་འཚོང་བ་དང་། ཆང་འཚོང་བ་དང་། མཚོན་ཆ་འཚོང་བ་དང་། དུག་འཚོང་བ་དང་། རྒྱ་སྐྱེགས་ཀྱི་ལས་དང་། ཏིལ་འཚོང་བའི༌[^1319]ལས་སོ་ཞེས་བྱ་བ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 1523]
རང་བཞིན་གྱི་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་ལས་གཞན་པ་ཐམས་ཅད་ལ་གསོ་བའི་དོན་ཉིད་མ་གཏོགས་སོ་ཞེས་བྱ་བའི་ལྷག་མའོ་ཞེས་བྱ་བ་ནི་བཅས་པའི་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་བཟའ་བ་ཐམས་ཅད་བཀག་པ་ལས་གཞན་དུ་ཡང་དགག་པའི་ཕྱིར་གང་ཡིན་པ་དེ་ཐམས་ཅད་ལ་གསོལ་བའི་དོན་ཉིད་དུ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བའི་ལྷག་མ་འདི་ཤེས་པར་བྱའོ། །

[Block 1524]
ཕྲན་ཚེགས་དག་ལས་འདི་དང་པོར་བྱས་ཏེ་གཙང་བར་བྱས་པ་དང་སྤོས་ཀྱིས༌[^1320]བསྒོ་བར་བྱའོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 1525]
སྒོག་སྐྱ་དང་ཀུན་དོང༌[^1321]ཀེའུ་བཟའ་བར་མི་བྱའོ། །

[Block 1526]
ནད་པས་ནི་དབེན་པའི་ཕྱོགས་སུའོ་ཞེས་བྱ་བ་ནི་བཟའ་བར་བྱ་བའོ།[^1322] །ཟོས་ནས་སྒོག༌[^1323]སྐྱ་ནི་ཞག་བདུན། ཀུན་དོང་ནི་ཞག་གསུམ། ཀེའུ་ནི་ཞག་གཅིག་མ་ལོན་པར་གཙུག་ལག་ཁང་དུ་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཟོས་ནས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1527]
སྒོག་སྐྱ་ཟོས་ནས་ནི་ཞག་བདུན་ནོ། །

[Block 1528]
དེ་བཞིན་དུ་ཀུན་དོང་ཟོས་ནས་ནི་ཞག་གསུམ་མོ། །

[Block 1529]
ཀེའུ་ཟོས་ནས་ནི་ཞག་གཅིག་གོ། །

[Block 1530]
གནས་མལ་ལ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལོངས་སྤྱད༌[^1324]པར་མི་བྱའོ། །

[Block 1531]
བཤང་བའི་སར་འཇུག་པར་མི་བྱའོ། །

[Block 1532]
གཅི་བའི་སར་མི་བྱའོ། །

[Block 1533]
དགེ་འདུན་གྱི་ནང་དུ་འགྲོ་བར་མི་བྱའོ། །

[Block 1534]
མཆོད་རྟེན་གྱི་ཉེན་ཀོར༌[^1325]དུ་མི་བྱའོ། །

[Block 1535]
དེའི་ཐག་ནི་འདོམ་གང་ངོ་ཞེས༌[^1326]བྱ་བ་ནི་མཆོད་རྟེན་གྱི་ཉེན་ཀོར༌[^1327]དེའི་འོ། །

[Block 1536]
འདིར་གཞུང་ནི། མཆོད་རྟེན་གྱི་ཉེན་ཀོར༌[^1328]འདོམ་གང་སྤང་བར་བྱ་སྟེ། དགེ་སློང་དག་མཆོད་རྟེན་ནི་ལྷ་མངོན་པར་དད་པ་ཅན་དག་གིས་ཀུན་ནས་གང་བ་ཡིན་ལ། ལྷ་རྣམས་ནི་གཙང་སྦྲ་འདོད་པ་ཡིན་པས་དྲི་དེ་ནི་དེ་དག་དང་མི་མཐུན་པའི་ཕྱིར་མཆོད་རྟེན་ལ་ཕྱག་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1537]
འདི་ནི་མི་རིགས་པར་གྱུར་པ་སྟེ།[^1329] གང་གི་ཕྱིར་དེ་ལྟ་བུར་གྱུར་པའི་གནས་སྐབས་རྣམས་ལ༌[^1330]མཆོད་རྟེན་ལ་ཕྱག་བྱ་བར་མི་རིགས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1538]
ཁྱིམ་བདག་དག་ལ་ཆོས་བསྟན་པར་མི་བྱའོ། །

[Block 1539]
ཁྱིམ་དག་ཏུ་འགྲོ་བར་མི་བྱའོ། །

[Block 1540]
སྐྱེ་བོས་གང་བའི་ས་ཕྱོགས་སུ་མི་བྱའོ། །

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
--- END BLOCKS ---
