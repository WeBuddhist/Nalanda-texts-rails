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
ངོ་མཚར་ཆེ་བ་དེས་ན་དེ་ཉིད་ཉམས་སད་པས་འདོད་པ་སྟེ་དེས་སོ། །

[Block 1332]
ཉི་མའི་འོད་རབ་ཏུ་གསལ་བ་གང་ཡིན་པ་དེ་ནི་ཉི་མའི་འོད་ཟེར་རབ་ཏུ་གསལ་བར་གྱུར་པའོ། །

[Block 1333]
འདིར་ཚ་བས་བྱས་པའི་ངལ་བ་དེས་གདུངས་པ་གང་ཡིན་པ་དེ་ནི་ཚ་བས་གདུངས་ཤིང་ངལ་བར་གྱུར་པའོ། །

[Block 1334]
དེ་དག་གིས་ནི་བཀྲེས་པ་དང་སྐོམ་པ་དང་། ངལ་བས་གདུངས་ཤིང་མགྲིན་པ་འགགས་པའོ། །

[Block 1335]
ཡང་ན་བཀྲེས་པ་དང་། སྐོམ་པ་དང་། ངལ་བས་བྱས་པའི་གདུང་བ་དེས་མགྲིན་པ་འགགས་པ་གང་ཡིན་པའོ། །

[Block 1336]
གྲོགས་དང་བྲལ་བས་གཅིག་པུར་གྱུར། །ཞེས༌[^769]བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདིའི་བསྡུས་པའི་དོན་ནི་ལུས་དང་སེམས་སྡུག་བསྔལ་གྱིས་ཉམ་ཐག་པ་བདག་ལ་བསྐྱབ་པའི་རིགས་སོ། །ཞེས་བསྟན་ཏོ། །

[Block 1337]
དེ་ལ་སེམས་ཀྱི་སྡུག་བསྔལ་ནི་འཇིགས་པ་སྟེ། གྲོགས་མེད་པའི་ཕྱིར་རོ། །

[Block 1338]
ནགས་ཚལ་སྟུག་པོའི་ནང་དུ་འདུག་པ་ནི་ལུས་ཀྱི་སྡུག་བསྔལ་ཡིན་ཏེ། དེ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 1339]
ལྷན་ཅིག་སྐྱེས་པའི་སྡུག་བསྔལ་དང་། ལམ་དུ་ཞུགས་པས་དུབ་པའི་སྡུག་བསྔལ་ཏེ། བཀྲེས་པ་དང་ངལ་བ་དེ་གཉིས་ཀྱིས་དུབ་པའི་ལུས་ཞེས་སྨོས་པའི་ཕྱིར་རོ། །

[Block 1340]
སྐོམ་པ་ཡང་ལྷན་ཅིག་སྐྱེས་པའི་སྡུག་བསྔལ་གྱི་རང་བཞིན་ཡིན་པས་མ་སྨོས་སོ། །

[Block 1341]
ཚིགས་བཅད་སྔ་མའི་དོན་ཉིད་བསྟན་པའི་ཕྱིར་ཚིགས་བཅད་གཉིས་པ་ཡང་བརྩམས་ཏེ། བདག་ནི་ལམ་དང་ལམ་མིན་ཞེས་བྱ་བའོ། །

[Block 1342]
ཡང་ན་ཁྱད་པར་དམིགས་པ་ཡིན་ཏེ། ཚིགས་བཅད་དེ་ལས་ནི་སྔ་མར་ནགས་ཚལ་སྟུག་པོའི་ནང་དུ་འདུག་ཅེས་བཤད་པ་ལ། ནགས་ཚལ་གྱི་རྒྱུ་མ་བསྟན་པས་དེའི་རྒྱུ་ལམ་དང་ལམ་མིན་ཞེས་བྱ་བ་འདིས་བསྟན་ཏོ། །

[Block 1343]
ཇི་ལྟར་བསྟན་པའི་དོན་ཉིད་ཚ་བ་དང་། སྐོམ་པ་དང་། ངལ་བའོ་ཞེས་སྔར་བསྟན་པའི་ཁྱད་པར་ཏེ། སྔར་བཤད་པའི་ཚིགས་བཅད་ཀྱི་དོན་ཡང་ལྷན་ཅིག་སྐྱེས་པའི་སྡུག་བསྔལ་སྐོམ་པ་བསྐང་བ་སྟེ། དེའི་རང་བཞིན་བཀྲེས་པའི་སྡུག་བསྔལ་སྨོས་པ་ཡང་རབ་ཏུ་གྲུབ་བོ། །

[Block 1344]
རིངས་རིངས་ལྟར་མགྱོགས་སུ་དོང་སྟེ་ཞེས་བྱ་བ་ནི་རྟབས༌[^770]ཤིང་རིངས་པས་མགྱོགས་པར་འགྲོ་བ་གང་ཡིན་པ་དེ་ནི་རིངས་རིངས་ལྟར་མགྱོགས་སུ་དོང་བའོ། །

[Block 1345]
དགའ་བ་དང་རྟབ་རྟབ་པོ༌[^771]ནི་དགའ་བས་རྟབ་རྟབ་པའོ། །

[Block 1346]
དེ་གཉིས་ཀྱིས་མགྱོགས་པར་འགྲོ་བ་གང་ཡིན་པ་དེ་ནི་དགའ་བས་རྟབ་རྟབ་པོར་གྱུར་ཅིང༌[^772]མགྱོགས་པོར་སོང་བའོ། །

[Block 1347]
ཉ་བ་རྣམས་ཀྱིས༌[^773]བརྗེད་ནས་བོར་བའམ། ཞེས་བྱ་བ་འདིས་ནི་གཞན་གྱིས་བསད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1348]
སྔངས༌[^774]ཏེ་བརྒལ་བས་ཐང་ལ་འགྲེས་པ་དག །ཅེས་བྱ་བ་འདིས་ནི་རང་ཉིད་ཤི་བ་ཉིད་དུ་བསྟན་ཏེ། གཉི་གས་ཀྱང་བདག་གིས་མ་བསད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1349]
དེ་བས་ན་སྦྱིན་པའི་དངོས་པོ་ཉོན་མོངས་པ་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1350]
ལ་ལ་ཞིག་གིས་ཞེས་བྱ་བ་འདིས་ནི་རྐུ་བ་དང་རྔོན་པ་མ་ཡིན་པ་ཉིད་དུ་བསྟན་ཏེ། དེས་ན་ཡང་ཉོན་མོངས་པ་མེད་པ་སྟེ། ལྷག་མ་རྣམས་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 1351]
ཆུང་ངུ་ན་འབྲས་བུ་འདི་སྨོས་པ་ཡིན་ནོ། །

[Block 1352]
རི་བོང་གྲོང་ན་ཉེ་བར་གནས་པ་གཞན་དག་ལ་ནི་ཡོད་དེ། བདག་ནི་ནགས་སུ་སྐྱེས་ནས་མེད་དོ་ཞེས་བསྟན་ཏོ། །

[Block 1353]
[^775]དེས་ན་ཡང་མུད་ག་ལ་སོགས་པ་བཙོས་པའི་ཁྱད་པར་ལས་མ་གཏོགས་པར་ཡང་བཟའ་བར་ནུས་ཏེ། དེས་ན་དེ་དག་ཉིད་སྨོས་སོ། །

[Block 1354]
གང་གི་དོན་སྒྲུབ་ནོར་ཅི་ཡོད་པ་ཞེས་བྱ་བ་འདིས་ནི་རང་དགར་ཡོད་པས་ཉོན་མོངས་པ་མེད་པའི་སྦྱིན་པ་བསྟན་ཏོ། །

[Block 1355]
ལྷག་པའི་ཞེས་བྱ་བ་ནི་ཁྱད་པར་དུ་གྱུར་པའོ། །

[Block 1356]
ནོར་དབྱིག་ཅེས་བྱ་བ་ནི་ནོར་ཐམས་ཅད་དེ་རེ་ཞིག་བདག་ཉིད་ཅེས་བྱ་བ་ལ།

[Block 1357 [VERSE]]
བདག་ཡོངས་སུ་གཏོང་བ༌[^776]ལ་དགོངས་པའོ། །
ཁྱོད་ལ་བརྟེན༌[^777]ནས་བདག་ནི་དོན་ཡོད་གྱུར། །

[Block 1358]
ཞེས་བྱ་བ་ནི་འདི་ལྟར་སྦྱིན་པས་སོ། །

[Block 1359]
གུས་ཤིང་རིམ་གྲོ་སྐྱེད་དེ་ཞེས་བྱ་བ་ལ། གུས་པ་དང་རིམ་གྲོ་མེད་པར་གཞན་དུ་ན་དེ་ཇི་ལྟར་ནུས་པར་གྱུར་པའོ། །

[Block 1360]
དེ་ལ་དེ་སྐད་ཅེས་སྨྲས་ཏེ་ཞེས་བྱ་བ་ནི་སློང་བའི་མགྲོན༌[^778]ལ་དགའ་ཞིང་ཡོན་ཏན་ཆེ་བར་རྟོགས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་ལྟར་མཆོག་ཏུ་དགའ་བ་ཡིན་ཞེ་ན། ནོར་འདོད་པ་དག་གཏེར་ནི་མཐོང་བ་བཞིན། །ཞེས་བྱ་བ་ཡིན་ནོ། །ཇི་ལྟ་བུའི་མེའི་ནང་དུ་ཞུགས་ཤེ་ན། མེ་འབར་དེའི་ནང་དུ་ཞེས་བྱ་བ་དང་། པདྨ་རྒྱས་པའི་ཆུ་ནང་ངང་པ་བཞིན། །ཞེས་བྱ་བའོ། །

[Block 1361]
ཇི་ལྟར་གཏེར་མཐོང་བས་ནི་མཆོག་ཏུ་དགའ་བ་དེ་ལྟ་བུ་མ་ཡིན་ཏེ། དེ་བས་ན་འཕྲལ་ལ་ཞེས་སྨོས་སོ། །ཅི་ཞིག་བཏང་ཞེ་ན། ལུས་སོ། །ཇི་ལྟར་བཏང་ཞེ་ན། ཆགས་པ་མེད་པ་མགྲོན༌[^779]ལ་བྱམས་པའི་ཕྱིར་རོ། །

[Block 1362]
འདི་ལྟར་ཡང་ཆགས་པ་མེད་པ་ནི་མེ་ཏོག་དམན་མ་བཞིན་ནོ། །

[Block 1363]
གཏོང་བ་རྒྱ་ཆེན་ཞེས་བྱ་བ་སྟེ། དེ་བས་ན་ལུས་ལ་ཆགས་པ་མེད་པར་ཡོངས་སུ་གཏོང་བས་སོ། །

[Block 1364]
སེམས་ཀྱང་གསལ་བ་ནི་ཞེས་བྱ་བ་ནི་མགྲོན༌[^780]ལ་བྱམས་པས་གཏོང༌[^781]བའོ། །

[Block 1365]
གཏོང་བ་རྒྱ་ཆེ་བ་དང་སེམས་ཀྱང་གསལ་བའི་རྒྱུ་བསྒྲུབ་པའི་ཕྱིར། །ཨེ་མའོ་ཡོན་ཏན་གོམས་བྱས་པ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། དེ་བས༌[^782]ལུས་ལ་ཆགས་པ་མེད་པར་དུད་འགྲོའི་སྐྱེ་གནས་སུ་གྱུར་པ་ཡང་སེམས་གསལ་བར་བྱེད་པ་དང་། ཡོན་ཏན་ལ་གོམས་པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
