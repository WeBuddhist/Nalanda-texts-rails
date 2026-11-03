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
ཆོས་སྒྲུབ་པ་དང་རྗེས་སུ་མཐུན་པ་ཞེས་བྱ་བ་ལ་ཆོས་ནི་འདིར་མངོན་པར་མཐོ་བ༌[^807]ལ་དགོངས་སོ། །

[Block 1402]
དེ་སྒྲུབ་པ་ནི་ཆོས་སྒྲུབ་པའོ། །

[Block 1403]
འདིའི་རྗེས་སུ་མཐུན་པ་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལུགས་སུ་འབྱུང་བ་སྟེ། བྱ་བ་ངན་པས་བྲེལ་པའི་གཉེན་པོས་བྱ་བ་བཟང་པོ་སྒྲུབ་པ་དང་རྗེས་སུ་མཐུན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1404]
ཐར་པའི་ཆོས་བརྩམས་པའི་གནས་སུ་གྱུར་པ་ཞེས་བྱ་བ་ལ། འདིར་ཆོས་ནི་ཐར་པ་སྒྲུབ་པའི་ཆོས་ལ་དགོངས་སོ། །

[Block 1405]
ཐར་པའི་ཆོས་བརྩམས་པ་དེའི་རྩོམ་པའི་ལྷག་པའི་ཚུལ་ཁྲིམས་དང་སེམས་དང་། ཤེས་རབ་ཀྱི་མཚན་ཉིད་དེའི་གནས་སུ་གྱུར་པའོ། །

[Block 1406]
ཉོན་མ་མོངས་པར་རྙེད་པ་ཞེས་བྱ་བ་ནི་བསགས་པའི་སྡུག་བསྔལ་མ་ཡིན་པས་རྙེད་པ་སྟེ། སྔ་མ་ཉིད་དུ་ཡན་ཏན་ལ་དགའ་བའི་སྦྱིན་པ་པོ་དག་གིས་མཆོད་ཅིང་ཕུལ་བ་བསླངས་པ་ཞེས་བསྟན་པའི་ཕྱིར་ཏེ། འདིས་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 1407]
འཇིག་རྟེན་གྱི་བཀུར་སྟི་བྱས་པ་ཡིད་དུ་འོང་བ་དག་ཀྱང་ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་བསྟན་ཏེ། བདག་ཉིད་ཀྱི་ཕུན་སུམ་ཚོགས་པ་སྔར་བསྟན་པའི་ཕྱིར་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་ཡང་བསྟན་ཏོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1408]
རབ་ཏུ་བྱུང་བ་དཀའ་ཐུབ་ཅན་གྱི་དུལ་བ་དང་བསྡམས་པ༌[^808]ལ་རབ་ཏུ་འབད་པ་ཞེས་བྱ་བ་ལ་རབ་ཏུ་བྱུང་བའི༌[^809]དཀའ་ཐུབ་ཀྱིས་དུལ་བ་དང་བསྡམས་པ་ནི༌[^810]དཀའ་ཐུབ་ཅན་གྱི་རབ་ཏུ་བྱུང་བ་དུལ་བ་དང་བསྡམས་པའོ། །

[Block 1409]
དེ་རབ་ཏུ་བྱུང་བའི་དུལ་བ་དང༌[^811]བསྡམས་པ་མཆོག་ཏུ་བྱེད་པ་ནི་གཙོ་བོར་བྱེད་པ་སྟེ། དུལ་བ་དང་བསྡམས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1410]
གྲགས་པ་ཆེ་བ་དང་ཞེས་བྱ་བ་ནི་གྲགས་པ་གསལ་བར་གྱུར་པས་སོ། །

[Block 1411]
སྔོན་ཤེས་པ༌[^812]རྗེས་སུ་དྲན་པ་དང་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་འདྲིས་པའི་ཕྱིར་རོ། །

[Block 1412]
སྲིད་པའི་ཡོན་ཏན་དང་། རབ་ཏུ་ཞི་བས་མཚོན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྲིད་པའི་ཡོན་ཏན་ཉེ་བར་ཞི་བ་གང་ཡིན་པ་དེ་ནི་རབ་ཏུ་ཞི་བའོ། །

[Block 1413]
སྲིད་པའི་ཡོན་ཏན་ཉིད་རབ་ཏུ་ཞི་བ་དེས་མངོན་པར་མཚོན་ནས་སྲིད་པའི་ཡོན་ཏན་རབ་ཏུ་ཞི་བས་མངོན་པར་མཚོན་པའོ། །

[Block 1414]
འདིས་ནི་ཐོས་པ་སྟེ། འགྲོགས་པས་ནི་མ་ཡིན་ནོ། །

[Block 1415]
དེ་ལྟར་ན་མཐོང་བ་ཙམ་གྱིས་དེ་བཞིན་དུ་འོང་བར་འགྱུར་རོ་ཞེས་སྨོས་ཏེ། སྔོན་ཁྱིམ་པའི་གནས་སྐབས་བཞིན་རབ་ཏུ་བྱུང་ནས་ཀྱང་རབ་ཏུ་དབེན་པའི་བདེ་བ་མེད་པར་བྱེད་པ་འཁྲུག་པ་དང་ཞེས་བྱ་བ་ནི་བསམ་གཏན་གྱི་བདེ་བ་བཅོམ་པའོ། །

[Block 1416]
ཡང་ན་རབ་ཏུ་བྱུང་བའི་བདེ་བ་བཅོམ་པའོ། །ཅི་ལྟ་ཞེ་ན། གཡེང་བ་དང་བར་ཆད་དུ་གྱུར་པ་དེ་ལ་ཞེས་བྱ་བ་ནི་གཡེང་བ་དང་བར་ཆད་དུ་གྱུར་པའི་ཁྱིམ་པའི་འདུ་འཛི་སྟེ། དབེན་པའི་འདུ་འཛིས་བར་དུ་གཅོད་པར་བྱེད་པས་འདྲེས་པའོ། །

[Block 1417]
དེ་ལ་མི་དགའ་ནས་ཞེས་བྱ་བ་ནི་གཞན་གྱིས་ནི་དབེན་པའི་རོ་མི་ཤེས་ཤིང་འདུ་འཛི་ལ་དགའ་བ་སྟེ། དེ་བས་ན་མངོན་པར་འཇུག་པ་ལ་དགའ་བ་ཞེས་བསྟན་ཏོ། །

[Block 1418]
རབ་ཏུ་དབེན་པ་ལ་དགའ་བའི་ཕྱིར་ཞེས་བྱ་བ་ལ་དགའ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ལུས་དང་སེམས་དབེན་པ་ལ་དགའ་བའི་ཕྱིར་ཏེ། ལུས་དབེན་པ་ནི་གཉིས་སུ་མེད་པར་གནས་པའོ། །

[Block 1419]
སེམས་དབེན་པ་ནི་ཉོན་མོངས་པས་ཀུན་ཏུ་བཅོམ་པའི་སེམས་སྤངས་ཤིང་སེམས་ཀྱི་རྒྱུད་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 1420]
ཨནྡ་རྙིལ་གྱི་བཅག་འཕྲོ་ལྟར་མངོན་པར་སྔོ་བའི་ཆོས་གསལ་བ་གང་ཡིན་པའི་རླབས་ཀྱི༌[^813]ཕྲེང་བ་འདི་ནི་ཨནྡ་རྙིལ་ལྟར་མདོག་སྔོ་བའོ། །

[Block 1421]
དེ་འཐོར་བས་མཐའ་མར་གཏོར་བ་དེ་ནི་འཐོར་བས་མཐའ་གཏོར་བའོ། །

[Block 1422]
འདི་དག་གིས་ནི་སྐྱེ་བོ་གཞན་གྱིས་བགྲོད་པར་མི་ནུས་པར་བསྟན་ཏོ། །

[Block 1423]
ས་གཞི་བྱེ་མ་སྐྱ་བོས་ཁེབས་པ༌[^814]ཞེས་བྱ་བ་ནི་ཉམས་དགའ་བ་དང་། རྐང་པ་དོར་བ་ན་རེག་ན་བདེ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1424]
མེ་ཏོག་དང་འབྲས་བུ་དང་འདབ༌[^815]མས་བརྒྱན་པ་ཞེས་བྱ་བ་ནི་ཉམས་དགའ་བ་དང་། འཚོ་བ་སྒྲུབ་ཏུ་རུང་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1425]
ཤིང་རྣམ་པ་སྣ་ཚོགས་ཀྱིས་མཛེས་པར་བྱས་པ་ཞེས་བྱ་བ་ནི་འཚོ་བ་ཡོད་པ་སྒྲུབ་པ་དང་རྟག་ཏུ་མི་འབྲལ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1426]
ཆུ་གཙང་མ་བཏུང་དུ་རུང་བ་ཡོད་པ་ཞེས་བྱ་བ་ནི་བཏུང་བ་དང་། ཁྲུས་དང་། གཙང་སྦྲའི་ཡོ་བྱད་ཉིད་བསྟན་ཏོ། །

[Block 1427]
དཀའ་ཐུབ་ཀྱི་གནས་དཔལ་དང་ལྡན་པར་བྱས་སོ་ཞེས་བྱ་བ་ནི་དཀའ་ཐུབ་ལ་དཀའ་ཐུབ་ཅན་དག་གིས་ལྷག་པར་བསྟེན་པའི་ཕྱོགས་ནི་དཀའ་ཐུབ་ཀྱི་གནས་ཞེས་བརྗོད་དོ། །

[Block 1428]
ལུས་བཟང་ཞེས་བྱ་བ་ནི་ཁྱད་པར་དུ་གྱུར་པའི་ལུས་ཤིན་ཏུ་བཟང་བའོ། །

[Block 1429]
རིད་པར་གྱུར་པ་ནི་ལུས་ཤིན་ཏུ་བཟང་པོ་དེ་ལོ་མ་དང་། འབྲས་བུ་དང་། རྩ་བ་ལ་སོགས་པ་ཟ་བའི་ཕྱིར་རོ། །

[Block 1430]
དེ་ན་ཞེས་བྱ་བ་ནི་ཀ་རའི་གླིང་ནའོ། །

[Block 1431]
དཀའ་ཐུབ་ཅན་ཞེས་བྱ་བ་ནི་དུལ་བ་དང་སྡོམ་པ་ལ་སོགས་པའི་མཚན་ཉིད་ཀྱི་དཀའ་ཐུབ་ཅན་གྱིས་མཛེས་པ་ལྟ་བུ་གང་ཡིན་པ་ནི་དཀའ་ཐུབ་པའོ།[^816] །ཟླ་བ་ཆོས་པ་ལྟ་བུ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 1432]
སྤྱོད་པ་དང་དབང་པོ་རབ་ཏུ་ཞི་ཞིང་དུལ་བ་གང་ཡིན་པ་དེ་ནི་སྤྱོད་པ་དང་དབང་པོ་རབ་ཏུ་ཞི་ཞིང་དུལ་བའོ། །

[Block 1433]
རབ་ཏུ་ཞི་བ་དང་། དུལ་བ་དང་སྤྱོད་པ་ལ༌[^817]ལྟ་ཞིང་རྣམ་པར་ལྟ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། རབ་ཏུ་ཞི་ཞིང་དུལ་བའི་དབང་པོ་ནི་དབང་པོའི་སྒོ་བསྲུངས་པ་ཉིད་དོ། །

[Block 1434]
བརྟུལ་ཞུགས་བསྡམས་ལ་ངེས་བྱས་ཞེས་བྱ་བ་ལ་བརྟུལ་ཞུགས་དང་བསྡམས་པ་ནི་བརྟུལ་ཞུགས་དང་བསྡམས་པའོ། །

[Block 1435]
དེ་གཉིས་ལ་རྩེ་གཅིག་པ་གང་ཡིན་པ་དེ་ནི་བརྟུལ་ཞུགས་བསྡམས་ལ་ངེས་བྱས་སོ། །

[Block 1436]
བརྟུལ་ཞུགས་ཀྱིས་ནི༌[^818]བསྡམས་པ་ཡང་སྨོས་པ་ཡིན་ནོ། །

[Block 1437]
མི་འཚེ་བ་དང་། བདེན་པའི་ཚིག་དང་། མི་རྐུ་བ་དང་། རྟོག་པ་མེད་པ་ཉིད་དང་ཚངས་པར་སྤྱོད་པ་སྟེ། ལྔ་པོ་འདི་དག་ནི་བརྟུལ་ཞུགས་སོ། །

[Block 1438]
བསྡམས་པ་ནི་མི་ཁྲོ་བ་དང་། བླ་མ་ལ་སྲི་ཞུ་ཆེ་བ་དང་། གཙང་སྦྲ་དང་། སྤྱོད་པ་ཡང་བ་དང་། བག་ཡོད་པ་སྟེ་ལྔ་པོ་འདི་དག་ནི་བསྡམས་བ་ཞེས་བསྒྲགས་སོ། །

[Block 1439]
བྱ་དང་རི་དྭགས་རྣམས་ཀྱང་དེ་ལ་འཁོར་ཏེ། དེ་བས་ན་ཐུབ་པ་ཞེས་བྱ་བ༌[^819]སྟེ། རྒྱུ་འདིའི་ཕྱིར་རོ། །

[Block 1440]
འདིས་ནི་དེ་ལ་ཕན་པ་དེས་དཀའ་ཐུབ་ཅན་ཁྱད་པར་དུ༌[^820]གྱུར་པ་བསྟན་ཏོ། །
--- END BLOCKS ---
