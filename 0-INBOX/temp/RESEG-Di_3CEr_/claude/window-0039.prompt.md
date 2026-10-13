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
[Block 1366]
འདི་ལྟར༌[^1056]ཕྱོགས་ཀྱི་ཆོས་ཉིད་བསྟན་པའི་དོན་དུ་གཏན་ཚིགས་ཀྱི་ཚིག་ཡིན་ནོ། །

[Block 1367]
དེ་རྗེས་སུ་དཔག་པར་བྱ་བ་དང་། མེད་ན་མི་འབྱུང་བ་ཉིད་དུ་བསྟན་པའི་དོན་དུ་དཔེའི་ཚིག་ཡིན་ནོ། །

[Block 1368]
རྗེས་སུ་དཔག་པར་བྱ་བ་བསྟན་པའི་དོན་དུ་ཕྱོགས་ཀྱི་ཚིག་བརྗོད་དོ། །

[Block 1369]
འདི་རྗེས་སུ་དཔོག་པར་བྱེད་པའི་ཡན་ལག་གཞན་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1370]
དེས་ན་གཞན་གྱི་ཤེས་པར་འདོད་པ་ལ་སོགས་པའི་ཡན་ལག་ཉེ་བར་སྦྱར་བ་དང་མཇུག་བསྡུ་བ་དག་ནི་འདིར་བསལ་བ་ཡིན་ནོ། །

[Block 1371 [HEADING]]
#### དཔེ་ནི་རྟགས་ལས་ལོག་པ་རུ་བརྗོད་པར་བྱ་བ་མ་ཡིན་པ། ^4-1-4-0

[Block 1372]
དེ་ལྟར་ན་ནི་དཔེའི་ཚིག་ཀྱང་ལོག་པར་ཐོབ་པར༌[^1057]མི་འགྱུར་ཏེ། རྟགས་ཀྱི་དོན་དུ་བསྟན་པ་ཡིན་པའི་ཕྱིར་འདི་ཡང་ཉེ་བར་སྦྱར་བ་བཞིན་དུ་མི་བརྗོད་པར་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། དེ་ལྟར་ཡང་མ་ཡིན་ཏེ།

[Block 1373 [VERSE]]
དཔེ་ནི་རྟགས་ལས་ལོག༌[^1058]པ་རུ། །
བརྗོད་པར་བྱ་བ་མ་ཡིན་ཏེ། །
གཏན་ཚིགས་ཀྱི་དོན་སྟོན་པའི་ཕྱིར། །
ཉེར་འཇལ་བཞིན་དུ་དོན་མེད་མིན། །

[Block 1374]
མཚན་ཉིད་གསུམ་པའི་རྟགས་ལ་བསྒྲུབ་པར་བྱ་བ་ཉིད་དང་། གཏན་ཚིགས་ཀྱི་ཚིག་བརྗོད་པ་དེས་ན་གཏན་ཚིགས་ཀྱི་ལྷག་མ་བསྟན་པར་བྱ་བའི་དོན་དུ་དཔེའི་ཚིག་དོན་དང་བཅས་པ་ཡིན་ནོ། །

[Block 1375]
དེ་ལྟ་ན་ནི།

[Block 1376 [VERSE]]
རྟགས་ཀྱི་འབྲེལ་པ་བསྒྲུབ་པའི༌[^1059]ཕྱིར། །
གལ་ཏེ་དཔེར་བརྗོད་གཉིས་ཡིན་ན། །
དཔེ་ནི་ལོགས་གཅིག་ཉིད་དུ་གྱིས། །

[Block 1377]
གལ་ཏེ་གཏན་ཚིགས་ཀྱི་ཚིག་གིས༌[^1060]ཕྱོགས་ཉིད་ཙམ་བརྗོད་ནས་གཏན་ཚིགས་ལྷག་མ་གྲུབ་པར་བྱ་བའི་དོན་དུ་དཔེའི་ཡན་ལག་གྱིས་ཤིག །དེ་ལྟ༌[^1061]ཡང་མ་ཡིན་ཏེ། ལོགས་ཡིན་འཇིག་རྟེན་དང་མཚུངས་འགྱུར། །དེ་ལྟ་ན་ནི་འཇིག་རྟེན་པའི་བཞིན་དཔེ་གཏན་ཚིགས་དང་མ་འབྲེལ་བར་འགྱུར་རོ། །

[Block 1378 [VERSE]]
དེ་དག་གིས་ནི་དཔེ་བརྗོད་ལ། །
ཆོས་མཐུན་འབའ་ཞིག་རྗོད་པར་བྱེད། །

[Block 1379]
འཇིག་རྟེན་པས་ནི་སྦྱོར་བའི་དཔེ་བརྗོད་ལ་ཆོས་མཐུན་པ་འབའ་ཞིག་སྟོན་པར་བྱེད་དེ་བྱས་པའི་ཕྱིར་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1380]
བསྒྲུབ་བྱ་སྒྲུབ་བྱེད་ཉིད་སྤངས་ནས། །བསྒྲུབ་བྱ་སྒྲུབ་པའི་གཏན་ཚིགས་སོ། །ཞེས་ཇི་སྐད་དུ་བརྗོད་པ་དེ་སྦྱོར་བ་ལ་མེད་དོ། །

[Block 1381]
དེ་ལྟར་ཉེར་འཇལ་ཙམ་པོར་འགྱུར། །དེ་ལྟར་སྦྱོར་བས་གཏན་ཚིགས་ཀྱི་དོན་དུ་མ་སྨོས་པའི་ཕྱིར་བསྒྲུབ་བྱ་ལ་ཉེ་བར་འཇལ་བ་ཙམ་བསྟན་པ་ཡིན། དེ་བུམ་པ་བཞིན་དུ་བྱས་པའི་ཕྱིར་མི་རྟག་གོ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1382]
ཅི་སྟེ་ཡང་ཆོས་མི་མཐུན་པས་བསྒྲུབ་བྱ་སྒྲུབ་བྱེད་ཉིད་དུ་རྗོད་པར་བྱེད་དོ་ཞེ་ན་དེ་མ་ཡིན་ཏེ་ཆོས་མི་མཐུན་པས་ཀྱང་བསྒྲུབ་བྱ་སྒྲུབ་པའི༌[^1062]གཏན་ཚིགས་ཉིད་བསྟན་པར་མི་ནུས་ཏེ། གང་གི་ཕྱིར་དེ་ལ་ཡང་མི་མཐུན་ཕྱོགས་དག་ལྡན་ཅིག་རྒྱུ། །དེར༌[^1063]ཡང་རྟག་པར་མ་བྱས་པར་མཐོང་ཞེས་འཇིག་རྟེན་པས་མ་བྱས་པ་ཉིད་དང་། རྟག་པ་ཉིད་དག་སྟབས་གཅིག་ཏུ་བསྒྲུབ་པར༌[^1064]སྟོན་པར་བྱེད་པོར༌[^1065]འགྱུར་རོ། །

[Block 1383]
བཟློག་པས་ནི་རྟག་པ་དང་ཉེ་བར་འཇལ་བ༌[^1066]བཟློག་པར་བྱ་བའི་དོན་དུའོ། །

[Block 1384]
དེ་བཞིན་དུ་འདིར་ཡང་གཏན་ཚིགས་ཀྱི་དོན་ལས་ལོགས་ཤིག་ཏུ་དཔེ་རྗོད་པར་བྱེད་ན་ནི་ཉེ་བར་འཇལ་བ་ཙམ་ཞིག་བརྗོད་པར་འགྱུར་ཏེ་འཇིག་རྟེན་པ་བཞིན་ནོ། །

[Block 1385]
ཅི་སྟེ་ཡང་གཏན་ཚིགས་མ་སྨོས་ཀྱང་འཇལ་བ་སྨོས་པ་དེ་ལས་ཀྱང་བསྒྲུབ༌[^1067]བྱ་རྗེས་སུ་འཛིན་པར་འགྱུར་རོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། དེ་ལ་ཡང་།

[Block 1386 [VERSE]]
ལྡོག་པ་རྣམ་པར་བརྗོད་པ་ན། །
བསྒྲུབ་བྱ་སྒྲུབ་པའི་གཏན་ཚིགས་སམ། །
དེ་ཡི་ཁྱད་པར་ཡིན་ཡང་རུང་། །
མཚུངས་སྟོན་ཐུག་པ་མེད་པར་འགྱུར། །

[Block 1387]
གལ་ཏེ་དེ་ལྟར་ཉེ་བར་འཇལ་བར་བྱེད་ན་ནི༌[^1068]ཇི་ལྟར་བུམ་པ་བྱས་པའི་ཕྱིར་མི་རྟག་པ་དེ་བཞིན་དུ་སྒྲ་ཡང་ངོ་ཞེས་བྱ་བ༌[^1069]བཞིན་ཡང་བུམ་པ་མི་རྟག་པ་ཉིད་དུ་སྟོན་པ་ཡང་བརྗོད་པར་འགྱུར་རོ། །

[Block 1388]
སྒྲའི་ངེས་པར་བསྟན་པ་མ་གྲུབ་ཡང་ངོ་། །ཅི་སྟེ་བུམ་པ་ལ་སོགས་པ་བཞིན་མི་རྟག་པ་ཡིན་གྱི་ནམ་མཁའ་བཞིན་དུ་རྟག་པའོ་ཞེས་པ་ནི་མ་ཡིན་ནོ་ཞེས་བསྒྲུབ་པར་བྱ་བ་ཙམ་ཉེ་བར་འཇལ་བར་བྱེད་དེ། དེས་ན་ནམ་མཁའ་ལ་སོགས་པ་ལས་བྱས་པ་ཉིད་ལོག་པར་ཉེ་བར་བསྟན་པར་འགྱུར་རོ་ཞེ་ན་མ་ཡིན་ཏེ། ཅི་སྟེ་བསྒྲུབ་བྱའི་བྱེ་བྲག་ཉེ་བར་འཇལ་བར་བྱེད་པའི་ལྟ་ན། མི་རྟག་སྟེ་བུམ་པ་ལ་སོགས་པ་བཞིན་ནོ་ཞེ་ན། [^1070]དེ་ལྟ་ན་ཡང་སྣམ་བུ་ལ་སོགས་པ་ལས་ལོག་པའི་བྱས་པ་ཉིད་བརྗོད་པར་འགྱུར་རོ། །

[Block 1389]
བསྒྲུབ་བྱ་རྣམ་པ་ཐམས་ཅད་དང་ལྡན་པ་ནི་མ་ཡིན་ལ། དམ་བཅས་པའི་དོན་དང་ཡང་འབྲེལ་བ་མ་ཡིན་ཏེ། མི་རྟག་པ་ཉིད་ཙམ་དམ་བཅའ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1390]
དེ་ལྟར་ཉེ་བར་འཇལ་བའི་དོན་རྣམས་ཐམས་ཅད་དུ་མི་རིགས་སོ། །

[Block 1391]
གལ་ཏེ་ཡང་གཏན་ཚིགས་ནི་ཕྱོགས་ཀྱི་ཆོས་ཉིད་ཙམ་ཡིན་པའི་ཕྱིར་དཔེ་ནི་གཏན་ཚིགས་ཀྱི་དོན་ལས་ལོགས་ཤིག་པར་འགྱུར་རོ་ཞེ་ན། དེ་ལྟ་ན་ཡང་།

[Block 1392]
ཕྱོགས་ཀྱི་ཆོས་ཉིད་ཙམ་གཏན་ཚིགས། །ཡིན་ན་འཁྲུལ་པ་ཅན་ཡང་འགྱུར། །

[Block 1393]
གཏན་ཚིགས་ལྟར་སྣང་བ་ཡང་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 1394]
གཉིས་ཀ་བརྗོད་ལ་མི་འགྱུར་ཞེས། །འདི་སྙམ་དུ་ཡང༌[^1071]ཆོས་མཐུན་པ་འབའ་ཞིག་གི་དཔེ་རྗོད་པར༌[^1072]བྱེད་པ་དེ་ལས༌[^1073]འཁྲུལ་པ་ཅན་གྱི༌[^1074]གོ་སྐབས་ཡོད་དེ་མི་མཐུན་པའི་ཕྱོགས་ལ་ཡང་སྲིད་པའི་ཕྱིར་རོ། །

[Block 1395]
གང་ཆོས་མི་མཐུན་པ་འབའ་ཞིག་རྗོད་པར་བྱེད་པ་དེ་ལ་ནི་ཐུན་མོང་མ་ཡིན་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1396]
གང་ཞིག་གཉིས་ཀ་བརྗོད་པ༌[^1075]དེ་ལ་ནི་གང་ཡང་མི་སྲིད་དོ་ཞེ་ན། དེ་ལ་ཡང་ཡོད་པ་ཉིད་དེ། དགུ་ཡི་ནང་ནས་གཉིས་སྲིད་དོ། །

[Block 1397]
ཕྱོགས་ཀྱི་ཆོས་དགུ་ལས་དང་པོ་དང་ཐ་མ་གསུམ་པ་གཡས་ཕྱོགས་ན་མོའི་དཔེ་གཉིས་ཀ་བརྗོད་ཀྱང་འཁྲུལ་པ་ཅན་དུ་ཡོད་པར་སྲིད་པ་ཡིན་ནོ། །

[Block 1398]
དཔེ་བསྟན་ཏོ། །

[Block 1399 [HEADING]]
### དཔེ་ལྟར་སྣང་བ། ^4-2-0

[Block 1400 [VERSE]]
གཏན་ཚིགས་བསྒྲུབ་བྱ་གཉིས་ཀ་མེད། །
མི་མཐུན་ཕྱོགས་ལས༌[^1076]མེད༌[^1077]མ་བྱས། །
རྗེས་འགྲོ་ཕྱིན༌[^1078]ལོག་རྣམ༌[^1079]པ་གཉིས། །
ལྟར་སྣང་རྗེས་འགྲོ་མེད་པའང་ཡིན། །

[Block 1401]
དེ་ལ་གཏན་ཚིགས་མེད་པ༌[^1080]སྒྲ་རྟག་སྟེ། རེག་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རྡུལ་ཕྲ་རབ་བཞིན་ནོ༌[^1081]ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1402]
བསྒྲུབ་བྱ་མེད་པ་ནི་ལས་བཞིན་ནོ། །

[Block 1403]
གཉིས་ཀ་མེད་པ་ནི་བུམ་པ་བཞིན་ནོ། །

[Block 1404]
མི་མཐུན་པའི་ཕྱོགས་ལ་ཞུགས་པ་ནི་དཔེར་ན་གང་མི་རྟག་པ་དེ་རེག་པར་བྱ་བ་མ་ཡིན་ཏེ། མཐོང་བའི་ལས་བཞིན་རྡུལ་ཕྲ་རབ་བཞིན་ནམ་མཁའ་བཞིན་ཞེས་པ་ལྟ་བུའོ། །

[Block 1405]
དེ་དག་གིས་ནི་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་ནི༌[^1082]འབྲེལ་ན་དེའི་ཆོས་སུ་གྲུབ་པ༌[^1083]སོ་སོར་བརྗོད་དོ། །
--- END BLOCKS ---
