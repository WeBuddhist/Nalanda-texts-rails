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
[Block 1436]
དེའི་ཕྱིར་ཆོས་དེ་ནི་མི་གོས་པའི་ཆོས་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1437 [HEADING]]
#### ཏིང་ངེ་འཛིན་རྣམས་ཀྱི་ལས། ^7-6-6-0

[Block 1438]
ལས་ཀྱི༌[^919]རབ་ཏུ་དབྱེ་བ་མ་བསྟན་པས་དེའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཏིང་ངེ་འཛིན་རྣམས་ཀྱི་ལས་གང་ཡིན་པ་བསྟན་པར་བྱའོ། །

[Block 1439]
དེ་ལ་ཏིང་ངེ་འཛིན་ལ་ཡང་དག་པར་བརྟེན་ནས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་སྒོམ་པར་བྱེད་དོ། །

[Block 1440]
དེ་བཞིན་དུ་དེ་ལ་ཡང་དག་པར་བརྟེན་ནས་སེམས་ཅན་རྣམས་ཡོངས་སུ་སྨིན་པར་བྱེད་དོ།[^920] །རྫུ་འཕྲུལ་ལ་སོགས་པ་དག་གིས་འདུན་པར་བྱས་ནས་འཇུག་པར་བྱེད་དོ། །

[Block 1441]
དེ་བཞིན་དུ་དེའི་སྟོབས་ཀྱིས་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་སྦྱོང་བར་བྱེད་དེ། སེམས་ལ་དབང་ཐོབ་པར་གྱུར་ན་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་དེ་གསེར་ལ་སོགས་པའི་རང་བཞིན་དུ་བྱེད་དོ། །

[Block 1442]
དེ་བཞིན་དུ་དེའི་སྟོབས་ཀྱིས་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་སྒྲུབ་པར་བྱེད་དེ། དེའི་ལས་ནི་དེ་དག་ཡིན་ནོ། །

[Block 1443 [HEADING]]
## ལྷག་པའི་ཤེས་རབ། ^8-0

[Block 1444]
ལྷག་པའི་ཤེས་རབ་བརྗོད་པར་བྱ་བའི་དུས་ལ་བབ་པས་དེ་བརྗོད་དོ། །

[Block 1445]
དེ་ལ་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ནི་ལྷག་པའི་ཤེས་རབ་ཏུ་འདོད་དོ། །

[Block 1446]
དེ་ཡང་རྣམ་པ་གསུམ་སྟེ། སྦྱོར་བ་ལས་བྱུང་བའི་རྣམ་པར་མི་རྟོག་པ་སྟེ། ཀུན་ཏུ་ཚོལ་བའི་རྣམ་པར་མི་རྟོག་པ་དང་། དངོས་གཞི་དང་། དེའི་རྗེས་ལས་ཐོབ་པའོ། །

[Block 1447]
དེ་ལ་ཤེས་རབ་ཀྱི་དབང་དུ་བྱས་པ་ནི་ལྷག་པའི་ཤེས་རབ་དང་པོའོ། །

[Block 1448]
ནང་གི་བདག་ཉིད་ཀྱི་ཤེས་རབ་ནི་ལྷག་པའི་ཤེས་རབ་གཉིས་པའོ། །

[Block 1449]
གང་གནས་པའི་ཤེས་རབ་ནི་ལྷག་པའི་ཤེས་རབ་གསུམ་པའོ། །

[Block 1450]
དེ་ལ་རེ་ཞིག་རྣམ་པར་མི་རྟོག་པ་ཉིད་ནི་བསྒྲུབ་པར་བྱ་བ་ཡིན་པས་དེའི་དེ་ཉིད༌[^921]ནི་འབྲས་བུ་ཡིན་ལ། ཀུན་ཏུ་ཚོལ་བ་ནི་རྒྱུར་གྱུར་པ་ཡིན་ནོ། །

[Block 1451]
འབྲས་བུར་གྱུར་པ་དེ་ནི་རྗེས་ལ་ཐོབ་པའི་རྒྱུར་གྱུར་པ་ཡང་ཡིན་པས་དེ་བསྒྲུབས་ན༌[^922]གཉི་ག་ཡང་བསྒྲུབ་པ༌[^923]བྱས་པར་འགྱུར་རོ། །

[Block 1452 [HEADING]]
### རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱི་ངོ་བོ། ^8-1-0

[Block 1453]
དེ་ལ་དང་པོར་རེ་ཞིག་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་བརྗོད་པར་བྱའོ། །

[Block 1454]
འདིར་ངོ་བོ་ཉིད་དེ་ནི་མཚན་ཉིད་ཅེས་བརྗོད་དེ།

[Block 1455 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས། །
རྣམ་རྟོག་མེད་པའི་ངོ་བོ་ཉིད། །
རྣམ་པ་ལྔ་ནི་རྣམ་སྤངས་ཤིང་། །
ཡང་དག་དོན་ལ་བཀྲར་འཛིན་མེད། །

[Block 1456]
ཅེས་བྱ་བར་སྦྱོར༌[^924]རོ། །

[Block 1457]
རྣམ་པ་ལྔ་ནི་ཡིད་ལ་བྱེད་པ་མེད་པ་ཙམ་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཉིད་ཡིན་ན་གཉིད་ལོག་པ་དང་། ར་རོ་བ་དང་། བག་མེད་པ་ལ་སོགས་པ་ཡང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་སུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1458]
ཡང་རྣམ་པར་རྟོག་པ་དང་བཅས་རྣམ་པར་དཔྱོད་པ་དང་བཅས་པའི་ས་ལས་འདས་པ་རྣམ་པར་མི་རྟོག་པར་འདོད་ན། དེའི་ཕྱིར་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་ཐམས་ཅད་ཀྱང་རྣམ་པར་མི་རྟོག་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1459]
དེ་ལྟ་ཡིན་ན་ནི་འཇིག་རྟེན་པས་ཀྱང་རྣམ་པར་མི་རྟོག་པ་ཐོབ་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1460]
ཡང་ན་གང་དུ་སེམས་དང་སེམས་ལས་བྱུང་བ་མི་འཇུག་པ་འདུ་ཤེས་དང་ཚོར་བ་འགོག་པ་ལ་སོགས་པ་དེའི་གནས་སྐབས་རྣམ་པར་མི་རྟོག་པར་འདོད་ན་དེ་ནི་ཡེ་ཤེས་ཉིད་དུ་མི་འགྱུར་ཏེ། འགོག་པའི་སྙོམས༌[^925]པར་འཇུག་པ་ལ་སོགས་པའི་དུས་ན་སེམས་མེད་པའི་ཕྱིར་རོ། །

[Block 1461]
ཡང་ན་གཟུགས་ཀྱི་ངོ་བོ་བཞིན་དུ་རྣམ་པར་ཤེས་པ་འདོད་ན་ཡང་དེའི་ཕྱིར་ཇི་ལྟར་གཟུགས་བེམས་པོ༌[^926]ཡིན་པ་བཞིན་དུ་རྣམ་པར་ཤེས་པ་ཡང་བེམས་པོ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1462]
ཡང་ན་གང་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་ལ་བཀྲ་བར་འཛིན་པར་ཞུགས་པ་དེ་རྣམ་པར་མི་རྟོག་པ་ཡིན་ན། དེ་ཉིད་ནི་རྣམ་པར་རྟོག་པར་འགྱུར་ཏེ། འདི་ནི་དེ་ཁོ་ན་ཉིད་དོ་ཞེས་རྟོགས་པའི༌[^927]ཕྱིར་རོ། །

[Block 1463]
དེ་ལྟ་བུའི་རྣམ་པ་འདི་ལྔ་ཡོངས་སུ་སྤངས་པའི་ཡེ་ཤེས་ཀྱིས་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་ལ་གལ་ཏེ་ཞུགས་པར་གྱུར་ན་ནི་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་ནི་འདིའོ་ཞེས་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་ལ་བཀྲ་བར་འཛིན་པར་མི་འགྱུར་རོ། །

[Block 1464]
དེ་ལྟ་བུ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱི་མཚན་ཉིད་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་ལ་དམིགས་པ་མ༌[^928]ཡིན་ཏེ། མིག་གི་རྣམ་པར་ཤེས་པ་བཞིན་དུ་སྣ་ཚོགས་ཀྱི་རང་བཞིན་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1465]
དོན་འདི་དག་ཉིད་ཀྱིས་ཚིགས་སུ་བཅད་པ་དང་པོ་ཡང་བསྟན་པར་གྱུར་པ་ཡིན་ནོ། །

[Block 1466 [HEADING]]
### གནས། ^8-2-0

[Block 1467]
དེ་ལྟར་ངོ་བོ་ཉིད་བསྟན་ནས་གནས་གང་ལ༌[^929]འབྱུང་བར་འགྱུར་བ་བསྟན་པར་བྱ་སྟེ། དེ་ལྟར༌[^930]བསྟན་པའི་ཡེ་ཤེས་དེའི་གནས་ནི་སེམས་ཡིན་ནོ། །

[Block 1468]
གལ་ཏེ་དེའི་གནས་སེམས་ཡིན་ན་སེམས་ནི་སེམས་པར་བྱེད་པས་ན་སེམས་ཞེས་བྱ་བ་ཡིན་པས་སེམས་ཀྱི་གནས་ལ་འཇུག་པར་འགྱུར་བ་ནི་རྣམ་པར་མི་རྟོག་པ་ཞེས་བྱ་བར་མི་རིགས་སོ། །

[Block 1469]
ཡང་སེམས་མེད༌[^931]པ་ཡིན་ན་ནི་དེ་ནི་ཤེས་པ་མ་ཡིན་པ་ཐོབ་པར་འགྱུར་རོ་ཞེ་ན། སྐྱོན་གཉི་ག་སྤང་བར་བྱ་བའི་ཕྱིར་ཚིགས་སུ་བཅད་པ།

[Block 1470 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས། །
རྣམ་པར་རྟོག་པ་མེད་པའི་གནས། །

[Block 1471]
ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེའི་གནས་ནི་སེམས་ནི་མ་ཡིན་ཏེ། དོན་ལ་མི་སེམས་པའི་ཕྱིར་རོ། །

[Block 1472]
སེམས་མེད་པ་ཡང་མ་ཡིན་ཏེ། གང་དེའི་གནས་སེམས་ཀྱི་འཕེན་པའི་གནས་སྐབས་ལས་དེ་འབྱུང་བར༌[^932]གྱུར་པས་ན་དེ་སེམས་ཀྱི་རྒྱུ་ལས་བྱུང་བའི་ཕྱིར་ཏེ། དེའི་ཕྱིར་སེམས་ཁོ་ན་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1473 [HEADING]]
### གཞི། ^8-3-0

[Block 1474]
རྒྱུ་གང་ལས་འབྱུང་བར་འགྱུར་བ་དེ་ཚིགས་སུ་བཅད་པས་བསྟན་པ་ནི།

[Block 1475 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས། །
རྣམ་པར་རྟོག་པ་མེད་པའི་གཞི། །
ཐོས་པའི་བག་ཆགས་བརྗོད་བཅས་པའི། །
--- END BLOCKS ---
