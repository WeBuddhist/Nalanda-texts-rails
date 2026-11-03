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
རྒྱུ་དང་སྐྱེ་བ་སྣ་ཚོགས་པ་དག་ལ་ཡང་གཏོང་བ་རྒྱ་ཆེ་བར་བྱེད་པའོ། །

[Block 1367]
དམ་པའི་སྤྱོད་གཞོལ་བ་ཞེས་བྱ་བ་ནི་སྙིང་སྟོབས་རྒྱ་ཆེ་བའོ། །

[Block 1368]
གང་དུ་རྣམ་པར་མཛེས་པ་ནི་ཟླ་བ་སྟེ། གནས་སྐབས་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་རྫོགས་པ༌[^783]སྟེ། ད་ལྟའི་དུས་སུ་ཡང་གཉི་ག་ལ་སྦྱར་བར་བྱའོ། །ཇི་ལྟ་བུ་ཞེ་ན། དངུལ་གྱི་མེ་ལོང༌[^784]བཞིན་དུའོ། །ཇི་ལྟར་མཛེས་པར་སྣང་ཞེ་ན། ཟླ་བའི་གཟུགས་བརྙན་བཞིན་དུ་མདངས་དང་ལྡན་པ་ལྟ་བུར་རོ། །

[Block 1369]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་རི་བོང་གི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 1370 [HEADING]]
## ཨ་ཀ་ཏའི་སྐྱེས་པའི་རབས། ^7-0

[Block 1371]
དཀའ་ཐུབ་ཀྱི་ནགས་ཚལ་ན་གནས་པ་རྣམས་ལ་ཡང་ཞེས་བྱ་བ་ནི་གཞན་ཡོངས་སུ་བཟུང་བ་སྤངས་པའི་ཕྱིར་དཀའ་ཐུབ་ཀྱི་ནགས་ན་ནི་གཏོང་བ་མེད་དེ། གཏོང་བའི་ནུས་པ་མེད་པ་ཡིན་པའི་ཕྱིར་དེ་བས་ན་ཡང་གི་སྒྲ་སྨོས་སོ། །

[Block 1372]
ཁྱིམ་ན་གནས་པ་རྣམས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བ་ནི་དེ་ལས་བཟློག་པའི༌[^785]ཕྱིར་རོ། །

[Block 1373]
འཇིག་རྟེན་ལ་ཕན་པའི་ཕྱིར་འཁོར་བ་ན་གནས་པའི་ཚེ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་འཇིག་རྟེན་ལ་ཕན་པ་ལ་ལྟོས་པ༌[^786]མེད་པར་མཛད་ན་ནི་སྐད་ཅིག་གཅིག་གིས་འཁོར་བའི་ལམ་གྱི་མཐར་གཤེགས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1374]
སྤྱོད་པ༌[^787]དང་ཡོན་ཏན་རྣམ་པར་དག་པས༌[^788]མངོན་པར་མཚོན་པ་ཞེས་བྱ་བ་ལ། སྤྱོད་པ་ནི་ལུས་དང་ངག་གི་མཚན་ཉིད་དོ། །

[Block 1375]
ཡོན་ཏན་ཡང་སྤྱོད་པའི་མཚན་ཉིད་དོ། །

[Block 1376]
ཡང་ན་སྤྱོད་པ་ནི་སྦྱོར་བའོ། །

[Block 1377]
ཡོན་ཏན་ནི་བསམས༌[^789]པའོ། །

[Block 1378]
སྤྱོད་པ་དང་ཡོན་ཏན་དག་ནི་རྣམ་པར་དག་པའི་སྤྱོད་པ་དང་ཡོན་ཏན་རྣམ་པར་དག་པའོ། །

[Block 1379]
དེས་མངོན་པར་མཚོན་པ་ནི་སྤྱོད་པ་དང་ཡོན་ཏན་རྣམ་པར་དག་པས་མཚོན་པའོ། །

[Block 1380]
སའི་སྟེང་ན་རྒྱན་དུ་གྱུར་པ་ཞེས་བྱ་བ་ནི་རིགས་མཐོ་ཞིང་མཐོ་བའི་རྒྱུད་དུ་གྱུར་པ་སྟེ། ཤས་ཆེར་ལྷག་པར་མཛེས་པ་དེས་རྒྱན་དུ་གྱུར།[^790] སྐྱེས་པའི་ལས་ལ་སོགས་པ་བྱ་བ་རྣམས་ནི་བྱས་ཞེས་བྱ་བ་འདིས་ནི་མཆོད་སྦྱིན་བསྟན་ཏོ། །

[Block 1381]
རིག༌[^791]བྱེད་ཡན་ལག་དང་བཅས་པ་ནི་བསླབས་ཞེས་བྱ་བ་འདིས་ནི་འདོན་པ་བསླབས་པའོ། །

[Block 1382]
མཁས་པའི་གྲགས་པས་མིའི་འཇིག་རྟེན་ཁྱབ་པར་བྱས། །ཞེས་བྱ་བ་འདིས་ནི་འདོན་དུ་འཇུག་པ་བསྟན་ཏོ། །

[Block 1383]
ཕུལ་བ་རྣམས་བླངས་པ་ཞེས་བྱ་བ་འདིས་ནི་ལེན་པ་བསྟན་ཏོ། །

[Block 1384]
གཉེན་དང་མཛའ་བཤེས་རྟེན་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྦྱིན་པ་བསྟན་ཏོ། །

[Block 1385]
བྲམ་ཟེ་ལས༌[^792]སུ་བསྟན་པས་ལས་ལྷག་མ་ཅི་ཞིག་ལུས་ཤེ་ན། མཆོད་སྦྱིན་བྱེད་དུ་འཇུག་པ་སྟེ། དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་མི་མཛད་དེ། འགྲོ་བ་ཐམས་ཅད་ལ་འཚེ་བ་མེད་པ་དང་ལྡན་པའི་ཕྱིར་ཏེ། འཚེ་བ་སྤོང་བར་འདོད་པས་སོ། །

[Block 1386]
མཉེན༌[^793]དང་མཛའ་བཤེས་རྟེན་དང་ཞེས་བྱ་བ་ནི་ལས་དང༌[^794]གསོ་དགོས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 1387]
ཕོངས་པ་རྣམས་ཞེས་བྱ་བ་ནི་སྙིང་རྗེའི་ཞིང་གི་དབང་དུ་བྱས་པའོ། །

[Block 1388]
མགྲོན་དང་བཀུར་སྟི་བྱ་བ་རྣམས། །ཞེས་བྱ་བ་ནི་ཡོན་ཏན་གྱི་ཞིང་སྟེ་མགྲོན་ཡང་ཡོན་ཏན་གྱི་ཞིང་དུ་གཟུང་བར༌[^795]བྱ་སྟེ། གང་གི་ཕྱིར་སློང་བ་དག་ནི་བྱང་ཆུབ་སེམས་དཔའི་དགེ་བའི་བཤེས་གཉེན་དུ་གཟུང་བར་བྱའོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1389]
བླ་མ་ཞེས་བྱ་བ་ནི་ཕན་འདོགས་པའི་ཞིང་ངོ་། །ཟླ་བ་ལྟ་བུ་ནི་མཁས་པར་གྲགས་པའོ། །

[Block 1390]
སྟོན་ཀ་ལྟ་བུ་ནི་གཏོང་བ་དང་དཔའ་བའོ། །

[Block 1391]
བྱ་བ་ངན་པས་བྲེལ༌[^796]པའི་ཉེས་པས་གླགས་པ་ཞེས་བྱ་བས༌[^797]ནི་མངོན་པར་མཐོ་བའི་ཕྱོགས་དང་འགལ་བར་བསྟན་ཏོ། །

[Block 1392]
བག་མེད་པའི་གནས་སུ་གྱུར་པ་ཞེས་བྱ་བ་འདིས་ནི་ངེས་པར་ལེགས་པ་དང་འགལ་བར་བསྟན་ཏོ། །

[Block 1393]
བག་མེད་པ་གང་ཞེ་ན། དགེ་བའི་ཆོས་རྣམས་མི་སྒོམ་པ་སྟེ། འདིས་ནི་ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1394]
སྔ་མས་ནི་ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1395]
ད་ནི་སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས༌[^798]པ་ཉིད་བསྟན་ཏེ། ཚོལ་བ་ལ་སོགས་པའི་སྐྱོན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1396]
ཉེ་བར་ཞི་བ་དང་འགལ་བ་ཞེས་བྱ་བ་ནི་ཉེ་བར་ལོངས་སྤྱོད་པའོ། །

[Block 1397]
དབེན༌[^799]དུ་གྱུར་པ་ཞེས་བྱ་བ་ནི་འཇིག་པའི་དུས་སུ་མྱ་ངན་དང་། སྨྲེ་སྔགས་འདོན་པ་དང་། སྡུག་བསྔལ་བ་དང་། ཡིད་མི་བདེ་བ་དང་། འཁྲུགས་པ༌[^800]ལ་སོགས་པའི་ཕོངས་པ་བརྒྱའི་དབེན༌[^801]དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1398]
སོ་ཚིས་ཀྱི་ལས་བསྒྲུབ་པ༌[^802]མཐའ་ཡས་པས༌[^803]ཞེས་བྱ་བ་ནི་ནོར་སྒྲུབ་པ་ལ་སོགས་པའི་ཡོངས་སུ་མ་གྲུབ་པ༌[^804]དང་མཐར་མ་ཕྱིན་པས་སོ། །

[Block 1399]
ཆོག་མི་ཤེས་པ་ཞེས༌[^805]བྱ་བ་ནི་ཉེ་བར་ལོངས་སྤྱོད་པས་ངོམས་པ་མེད་པའོ། །

[Block 1400]
དེའི་ཉེས་པ་མེད་ཅིང་བདེ་ལ་ཞེས་བྱ་བ་ནི་ངན་པས་བྲེལ༌[^806]པའི་ཉེས་པས་གླགས་པ་མེད་པའི་བདེ་བའོ། །

[Block 1401]
ཆོས་སྒྲུབ་པ་དང་རྗེས་སུ་མཐུན་པ་ཞེས་བྱ་བ་ལ་ཆོས་ནི་འདིར་མངོན་པར་མཐོ་བ༌[^807]ལ་དགོངས་སོ། །

[Block 1402]
དེ་སྒྲུབ་པ་ནི་ཆོས་སྒྲུབ་པའོ། །

[Block 1403]
འདིའི་རྗེས་སུ་མཐུན་པ་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལུགས་སུ་འབྱུང་བ་སྟེ། བྱ་བ་ངན་པས་བྲེལ་པའི་གཉེན་པོས་བྱ་བ་བཟང་པོ་སྒྲུབ་པ་དང་རྗེས་སུ་མཐུན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1404]
ཐར་པའི་ཆོས་བརྩམས་པའི་གནས་སུ་གྱུར་པ་ཞེས་བྱ་བ་ལ། འདིར་ཆོས་ནི་ཐར་པ་སྒྲུབ་པའི་ཆོས་ལ་དགོངས་སོ། །

[Block 1405]
ཐར་པའི་ཆོས་བརྩམས་པ་དེའི་རྩོམ་པའི་ལྷག་པའི་ཚུལ་ཁྲིམས་དང་སེམས་དང་། ཤེས་རབ་ཀྱི་མཚན་ཉིད་དེའི་གནས་སུ་གྱུར་པའོ། །
--- END BLOCKS ---
