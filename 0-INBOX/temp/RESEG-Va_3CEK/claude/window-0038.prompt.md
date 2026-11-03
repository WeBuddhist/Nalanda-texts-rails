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
[Block 1331 [VERSE]]
བསོད་ནམས་མྱ་ངན་འདས་པ་དང་། །
ངེས་འབྱེད་ཆ་མཐུན་དགེ་རྣམས༌[^937]གསུམ། །

[Block 1332 [HEADING]]
#### བསོད་ནམས་ཀྱི་ཆ་དང་མཐུན་པ། ^1-72-1-0

[Block 1333]
བསོད་ནམས་ཀྱི་ཆ་དང་མཐུན་པ་ནི་རྣམ་པར་སྨིན་པ་ཡིད་དུ་འོང་བ་ཅན་གང་ཡིན་པའོ། །

[Block 1334 [HEADING]]
#### ཐར་པའི་ཆ་དང་མཐུན་པ། ^1-72-2-0

[Block 1335]
ཐར་པའི་ཆ་དང་མཐུན་པ་ནི་གང་སྐྱེས་ན་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཆོས་སུ་ནམ༌[^938]འགྱུར་བ་སྟེ། གང་ལ་འཁོར་བའི་ཉེས་དམིགས་དང་། བདག་མེད་པ་དང་། དམྱལ་བ༌[^939]ལས་འདས་པའི་ཡོན་ཏན་བརྗོད་པའི་གཏམ་ཐོས་ནས་སྤུ་ཟིང་ཞེས་བྱེད་པ་དང་། མཆི་མ་འཁྲུག་ཅེས་བྱེད་པ་དེ་ལ་ནི་ཐར་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་ཡོད་པར་ཤེས་པར་བྱ་སྟེ། དབྱར་མྱུ་གུ་སྐྱེ་བ་ལས་ན་གཡུལ་གྱི་གསེབ་ན་ས་བོན་ཡོད་པར་ཤེས་པ་བཞིན་ནོ། །

[Block 1336 [HEADING]]
#### ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ། ^1-72-3-0

[Block 1337]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ནི་དྲོ་བར་གྱུར་པ་ལ་སོགས་པ་རྣམ་པ་བཞི་ཡིན་ཏེ། འོག་ནས་བཤད་པར་བྱའོ། །

[Block 1338 [HEADING]]
### ཡིག་འབྲུ་དང་རྒྱ་ལ་སོགས་པའི་རང་བཞིན། ^1-73-0

[Block 1339]
འཇིག་རྟེན་ན་ཡིག་འབྲུ་དང་། རྒྱ་དང་། བགྲང་བ་དང་། སྙན་ངག་དང་། གྲངས་ཞེས་བྱ་བ་གང་ཡིན་པ་འདི་དག་གི་རང་བཞིན་ཅི་ཞེ་ན།

[Block 1340 [VERSE]]
རིགས་པའི༌[^940]རབ་ཏུ་བཅུག་པའི་ལས། །
རྣམ་གསུམ་ཀུན་སློང་བཅས་པ་ནི། །
ཡིག་འབྲུ་རྒྱ་དང་གྲངས་བཅས་པའི། །
སྙན་ངག་གྲངས་ཏེ་གོ་རིམས་བཞིན། །

[Block 1341]
རིགས་པས་བཅུག་པ་ཞེས་བྱ་བ་ནི་ཐབས་ཀྱི་བྱེ་བྲག་གིས་བཅུག་པའོ། །

[Block 1342]
ལས་རྣམ་པ༌[^941]གསུམ་ཞེས་བྱ་བ་ནི་ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་སོ། །

[Block 1343]
དེ་ལ་རེ་ཞིག༌[^942]ཡིག་འབྲུ་དང་རྒྱ་ནི་ལུས་ཀྱི་ལས་རིགས་པས་རབ་ཏུ་བཅུག་པ་ཀུན་ནས་སློང་བ༌[^943]དང་བཅས་པ་ཡིན་ནོ། །

[Block 1344]
བགྲང་བ་དང་། སྙན་ངག་ནི༌[^944]ངག་གི་ལས་ཏེ། དེ་ལྟར་ན་དེ་དག་ནི་ཕུང་པོ་ལྔའི་རང་བཞིན་ཡིན་ནོ། །

[Block 1345]
གྲངས་ནི་ཡིད་ཀྱི་ལས་ཏེ། ཡིད་ཀྱི༌[^945]ཆོས་རྣམས་སྡོམ་པར་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 1346 [HEADING]]
### རྣམ་གྲངས་ཁ་ཅིག། ^1-74-0

[Block 1347]
ད་ནི་རྣམ་གྲངས་ཁ་ཅིག་བརྗོད་པར་བྱ་སྟེ། སྒྲིབ༌[^946]ངན་ཁ་ན་མ་ཐོ་བཅས། །ཉོན་མོངས་ཅན༌[^947]ཆོས། ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་དང་། བསྒྲིབས་པ་དང་། ངན་པ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཆོས་རྣམས་ཀྱི་རྣམ་གྲངས་དག་ཡིན་ནོ། །

[Block 1348]
དྲི་མེད་དགེ། གྱ་ནོམ། གྱ་ནོམ་པ་ཞེས་བྱ་བ་ནི་དགེ་བ་ཟག་པ་མེད་པ༌[^948]རྣམས་ཀྱི་རྣམ་གྲངས་ཡིན་ནོ། །

[Block 1349]
ངན་པ་དང་གྱ་ནོམ་པ་དག་ལས་གཞན་པ་ནི་བར་མ་ཞེས་བྱ་བར་གྲུབ་པ་ཡིན་ནོ། །

[Block 1350]
འདུས་བྱས་དགེ་བསྟེན་བྱ། བསྟེན་པར་བྱ་ཞེས་བྱ་བ་ནི་འདུས་བྱས་ཀྱི་ཆོས་དགེ་བ་རྣམས་ཀྱི་རྣམ་གྲངས་ཡིན་ནོ། །

[Block 1351]
ལྷག་མ་རྣམས་ནི་བསྟེན་པར༌[^949]བྱ་བ་མ་ཡིན་ནོ༌[^950]ཞེས་བྱ་བར་གྲུབ་པ་ཡིན་ནོ། །

[Block 1352]
ཅིའི་ཕྱིར་འདུས་མ་བྱས་བསྟེན་པར༌[^951]བྱ་བ་མ་ཡིན་ཞེ་ན། གོམས་པར་བྱར་མི་རུང་བའི་ཕྱིར་དང་། འབྲས་བུའི་དོན་དུ་བསྟེན་པར་བྱ་བ་ཡིན་ན་འབྲས་བུ་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 1353]
ཆོས་གཞན་ཐམས་ཅད་ནི་བླ་མ་དང་བཅས་པ་ཡིན་གྱི། ཐར་པ་བླ་ན་མེད་པ་ཡིན། །མྱ་ངན་ལས་འདས་པ་ལས་ཆེས་ཁྱད་པར་དུ་འཕགས་པ་ནི་མེད་ཀྱི། དེ་ནི་དགེ་བ་དང་རྟག་པ་ཡིན་པའི་ཕྱིར་ཐམས་ཅད་པས་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་ནོ། །

[Block 1354]
ཆོས་མངོན་པའི་མཛོད་ཀྱི་བཤད་པ་ལས་ལས་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་བཞི་པའོ།། །།

[Block 1355 [HEADING]]
## ཕྲ་རྒྱས་བསྟན་པ། ^2-0

[Block 1356]
ལས་ལས་འཇིག་རྟེན་སྣ་ཚོགས་སྐྱེས། །ཞེས་བཤད་པ། ལས་དེ་དག་ཀྱང་ཕྲ་རྒྱས་ཀྱི་དབང་གིས་བསགས་པར་འགྱུར་གྱི། ཕྲ་རྒྱས་མེད་པར་ནི་སྲིད་པ་མངོན་པར་འགྲུབ་པར་མི་ནུས་པ་དེའི་ཕྱིར། སྲིད་པའི་རྩ་བ་ཕྲ་རྒྱས་ཡིན་པར་རིག་པར་བྱ་སྟེ། ཉོན་མོངས་པ་འཇུག་པ་ན་བྱ་བ་བཅུ་བྱེད་དེ། རྩ་བ་བརྟན་པར་བྱེད་དོ། །

[Block 1357]
རྒྱུད་གནས་པར་བྱེད་དོ། །

[Block 1358]
ཞིང་དུ་སྒྲུབ་པར་བྱེད་དོ། །

[Block 1359]
རྒྱུ་མཐུན་པར༌[^952]སྒྲུབ་པར་བྱེད་དོ། །

[Block 1360]
ལས་ཀྱི་སྲིད་པ་མངོན་པར་སྒྲུབ་པར་བྱེད་དོ། །

[Block 1361]
རང་གི་ཚོགས་ཡོངས་སུ་འཛིན་པར་བྱེད་དོ། །

[Block 1362]
དམིགས་པ་ལ་ཀུན་དུ་རྨོངས་པར་བྱེད་དོ། །

[Block 1363]
རྣམ་པར་ཤེས་པའི་རྒྱུན་འཁྲིད་པར་བྱེད་དོ། །

[Block 1364]
དགེ་བའི་ཕྱོགས་ལས་གཡོ་བར་བྱེད་དོ། །

[Block 1365]
ཁམས་ལས་མི་འདའ་བའི་ཚུལ་གྱིས་འཆིང་བའི་དོན་དུ་ཁྱབ་པར་བྱེད་དོ། །

[Block 1366 [HEADING]]
### ཕྲ་རྒྱས་དྲུག། ^2-1-0

[Block 1367]
ཕྲ་རྒྱས་དེ་དག་ཀྱང་དུ་ཞིག་ཅེ་ན། མདོར་བསྡུས༌[^953]ན། དྲུག་དྲུག་གང་ཞེ་ན།

[Block 1368 [VERSE]]
འདོད་ཆགས་དེ་བཞིན་ཁོང་ཁྲོ་དང་། །
ང་རྒྱལ་མ་རིག་ལྟ་བ་དང་། །

[Block 1369]
ཐེ་ཚོམ་ཡིན་ཏེ། དེ་བཞིན་ཞེས་སྨོས་པ༌[^954]ནི་འདོད་ཆགས་ཀྱི་དབང་གིས་གཞན་དག་དམིགས་པ་ལས༌[^955]རྒྱས་པར་གྱུར་པ་ཉིད༌[^956]ཤེས་པར་བྱ་བའི་ཕྱིར་ཏེ། དེ་ནི་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 1370 [HEADING]]
### ཕྲ་རྒྱས་བདུན། ^2-2-0
--- END BLOCKS ---
