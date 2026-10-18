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

[Block 1476]
ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། གང་གཞན་གྱིས་བསྟན་པ་ཐོས་པ་ལ༌[^933]བག་ཆགས་སོ། །

[Block 1477]
གང་བག་ཆགས་ཀྱི་རྒྱུ་ལས་ནི་ཡིད་ཀྱི་བརྗོད་པ་ཡིད་ལ་བྱེད་པ་སྟེ། དེ་ནི་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་ཞེས་བྱའོ། །

[Block 1478 [HEADING]]
### དམིགས་པ། ^8-4-0

[Block 1479]
ཡང་ཡེ་ཤེས་དེའི་དམིགས་པ་གང་ཡིན་པ་དེ་དེ་ལས་གཞན་པའི་ཚིགས་སུ་བཅད་པས་བསྟན་པ་ལ།

[Block 1480 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས། །
རྣམ་རྟོག་མེད་པའི་དམིགས་པ་ནི། །

[Block 1481]
ཞེས་བྱ་བ་ལ། དེ་ལ་གང་ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ཉིད་ཀྱི་ཆོས་ཐམས་ཅད་ནི་བརྗོད་པར་བྱ་བ་མེད་པ་ཡིན་པས་ན་ཆོས་རྣམས་བརྗོད་དུ་མེད་པ་ཉིད་དོ། །

[Block 1482]
ཡང་དེའི་བརྗོད་དུ་མེད་པ་ཉིད་གང་ཡིན་ཞེ་ན། བདག་མེད་དེ་བཞིན་ཉིད་ཀྱང་དེ། །ད་ནི་གང་ཟག་དང་ཆོས་ཀྱི་བདག་མེད་པ་སྟེ། ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ཉིད་ཀྱི་བདག་མེད་པའོ། །

[Block 1483]
དེའི་ངོ་བོ་ནི་དེ་ཉིད་དེ། དེ་བཞིན་ཉིད་དོ། །

[Block 1484]
དེས་ན་ཆད་པར་ལྟ་བར་མ་གྱུར་ཅིག་པའོ། །

[Block 1485 [HEADING]]
### རྣམ་པ། ^8-5-0

[Block 1486]
ཡང་དེ་ལ་དམིགས་པར་བྱེད་པའི་རྣམ་པ་གང་ཡིན་ཞེ་ན། དེ་སྟོན་པའི་ཚིགས་སུ་བཅད་པ།

[Block 1487 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས། །
རྣམ་པར་མི་རྟོག་རྣམ་པ་ནི། །
ཤེས་བྱ་དམིགས་པ་དེ་ཉིད་ལ། །
མཚན་མ་མེད་པ་གང་ཡིན་པའོ། །

[Block 1488]
ཞེས་བྱ་བ་ལ། ཡེ་ཤེས་དེ་ནི་དེ་བཞིན་ཉིད་དེ་ལ་མཉམ་པས་མཉམ་པར་འབྱུང་བས་མཚན་མ་མེད་པ་ཐ་མི་དད་པའི་རྣམ་པ་སྟེ། འདི་ནི་རྣམ་པའོ། །

[Block 1489]
ཇི་ལྟར་མིག་གིས་གཟུགས་རྣམས་འཛིན་པ་ན་དེ་ལ་སྔོན་པོ་ལ་སོགས་པ་མཐོང་བ་ཉིད་ཀྱི་རྣམ་པ་དང་། གཟུགས་སྔོན་པོ་ལ་སོགས་པ་ཉིད་གཞན་མ་ཡིན་པ་དེ་བཞིན་དུ། འདིར་ཡང་ཡེ་ཤེས་དང་དེ་བཞིན་ཉིད་དག་གཞན་མ་ཡིན་པ་ནི་རྣམ་པའོ། །

[Block 1490 [HEADING]]
### བརྒལ་བའི་ལན། ^8-6-0

[Block 1491]
ཡང་གལ་ཏེ་ཆོས་ཐམས་ཅད་བརྗོད་དུ་མེད་པ་ཡིན་ན་དེ་ལྟ་ན་གང་ལ་རྣམ་པར་རྟོག་པར་བྱེད་ཅེ་ན། སྦྱོར་བ༌[^934]ལས་བྱུང་བའི་རང་བཞིན་ཏེ། དོན་དུ། རྣམ་བརྟགས་དེ་ལས་གཞན་དུ་མིན། །དེ་བས་ན་དེ་ལས་གཞན་དུ་མ་ཡིན་ནོ། །

[Block 1492]
ཡང་ཇི་ལྟར་བྱས་ནས་ཤེ་ན། དེ་བསྒྲུབ་པར༌[^935]བྱ་སྟེ། ཡི་གེ་ཕན་ཚུན་སྦྱོར་བས་ན། དོན་དེ་སྦྱོར་ལས་བྱུང་བ་ཡིན་ཏེ། ཡི་གེ་གཞན་དང་གཞན་དག་ལྷན་ཅིག་ཏུ་བརྗོད་པའི་དོན་ནི་སྦྱོར་བ་ལས་བྱུང་བའི་དོན་ཡིན་ཏེ། ཇི་ལྟར་མིག་ཅེས་བྱ་བ་ལྟ་བུའི་ཡི་གེ་རྣམ་པར་མ་ཆད་པར་བརྗོད་པའི་དོན་ནི་འདི་ལྟར་སྦྱོར་བ༌[^936]སྟེ། རྣམ་པར་བརྟག་པར༌[^937]བྱ་བ་ནི༌[^938]དེ་ཡིན་ནོ། །

[Block 1493]
ཆོས་ཐམས་ཅད་བརྗོད་པར་བྱ་བ་མེད་པ་ཡིན་ནོ་ཞེས་བསྟན་པ་དེ་གང་གིས་གྲུབ་པ་ཡིན་ཞེ་ན། འདི་ལྟར།

[Block 1494 [VERSE]]
བརྗོད་པ་མེད་པར་བརྗོད་ཅེས༌[^939]ལ། །
ཤེས་པ་འཇུག་པ་མ་ཡིན་ནོ། །

[Block 1495]
རྗོད་པར་བྱེད་པ་ལ་མ་བྱང་བའི་ཕྱིར་བརྗོད་པར་བྱ་བ་ཡོད་ན་ཡང་དེའི་བློར་མི་འགྱུར་རོ། །

[Block 1496]
ཡང་གལ་ཏེ་རྗོད་པར༌[^940]བྱེད་པ་ནི་བརྗོད་པར་བྱ་བའི་བློར་འགྱུར་རོ་ཞེ་ན། འགལ་བའི་ཕྱིར་ན་བརྗོད་ལ་མིན་ཏེ། རྗོད་པར་བྱེད་པ་དང་། བརྗོད་པར་བྱ་བ་མཚན་ཉིད་གཞན་ཡིན་པའི་ཕྱིར་འགལ་བ་ཉིད་དོ། །

[Block 1497]
རྗོད་པར་བྱེད་པ་དང་། བརྗོད་པར༌[^941]བྱ་བ་དག །དེ་ཕྱིར་ཐམས་ཅད་བརྗོད་དུ་མེད། །ཅེས་བྱ་བ་སྟེ། རྗོད་པར་བྱེད་པ་དང་། བརྗོད་པར་བྱ་བ་དག་རྒྱུ་དེའི༌[^942]ཕྱིར་བརྗོད་དུ་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1498 [HEADING]]
### རྟེན། ^8-7-0

[Block 1499]
ཡང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་དེ་གང་གི་རྟེན་ཡིན་ཞེ་ན།

[Block 1500 [VERSE]]
རྣམ་པར་མི་རྟོག་ཡེ་ཤེས་དེ། །
བྱང་ཆུབ་སེམས་དཔའི་དེ་རྗེས་ལ། །
ཐོབ་པར་བྱ་བའི༌[^943]རྟེན་ཡིན་ཏེ། །

[Block 1501]
གང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱི་རྗེས་ལ་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ཐོབ་པར་འགྱུར་བས་དེའི་ཕྱིར་ཡེ་ཤེས་དེའི་རྟེན་དུ་འགྱུར་རོ། །

[Block 1502]
དེ་ནི་འཕེལ་བར་འགྱུར༌[^944]རོ་ཞེས་བྱ་བ་སྟེ། དེའི་ཕྱིར་དེ་ལྟ་བུའི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་འཕེལ་བར་འགྱུར་བའི་ཕྱིར་ཡང་རྣམ་པར་མི་རྟོག་པའི༌[^945]ཡེ་ཤེས་ནི་རྟེན་དུ་འགྱུར་རོ། །

[Block 1503 [HEADING]]
### གྲོགས། ^8-8-0

[Block 1504]
ཡང་དེའི་གྲོགས་གང་ཡིན་ཞེ་ན།

[Block 1505 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ༌[^946]རྣམས་ཀྱི་ཤེས། །
རྣམ་པར་རྟོག་པ་མེད་པའི་གྲོགས། །
ལམ་གཉིས་སུ་ནི་བརྗོད་པ་དེ།

[Block 1506]
[^947] །ཕ་རོལ༌[^948]ཕྱིན་ལྔའི་རང་བཞིན་ནོ། །

[Block 1507]
དེ་ལ་ལམ་གཉིས་ནི་ཚོགས་ཀྱི་ལམ་དང་། །རྟེན་གྱི་ལམ་མོ། །

[Block 1508 [HEADING]]
#### ཚོགས་ཀྱི་ལམ། ^8-8-1-0

[Block 1509]
དེ་ལ་ཚོགས་ཀྱི་ལམ་ནི་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པ་དང་། བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 1510 [HEADING]]
#### རྟེན་གྱི་ལམ། ^8-8-2-0
--- END BLOCKS ---
