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
[^947] །ཕ་རོལ༌[^948]ཕྱིན་ལྔའི་རང་བཞིན་ནོ། །

[Block 1507]
དེ་ལ་ལམ་གཉིས་ནི་ཚོགས་ཀྱི་ལམ་དང་། །རྟེན་གྱི་ལམ་མོ། །

[Block 1508 [HEADING]]
#### ཚོགས་ཀྱི་ལམ། ^8-8-1-0

[Block 1509]
དེ་ལ་ཚོགས་ཀྱི་ལམ་ནི་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པ་དང་། བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 1510 [HEADING]]
#### རྟེན་གྱི་ལམ། ^8-8-2-0

[Block 1511]
རྟེན་གྱི་ལམ་ནི་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། གང་གི་ཕྱིར་སྔར་བསྟན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་ཡང་དག་པར་བྱུང་བའི་དགེ་བའི་རྩ་བ༌[^949]དང་། བསམ་གཏན་ལ་བརྟེན་ནས་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་དེ་འབྱུང་བར་འགྱུར་བས་སོ། །

[Block 1512 [HEADING]]
### རྣམ་པར་སྨིན་པ། ^8-9-0

[Block 1513]
སངས་རྒྱས་ཉིད་མ་ཐོབ་ཀྱི་བར་དུ་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་དེས་རྣམ་པར་སྨིན་པ་གང་སྒྲུབ་པར་འགྱུར་ཞེ་ན།

[Block 1514 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས། །
རྣམ་རྟོག་མེད་པའི་རྣམ་སྨིན་ནི།
སངས་རྒྱས་དཀྱིལ་འཁོར་གཉིས་སུ་སྟེ། །

[Block 1515]
སངས་རྒྱས་རྣམས་ཀྱི་དཀྱིལ་འཁོར་གཉིས་ནི་ལོངས་སྤྱོད་རྫོགས་པའི་དཀྱིལ་འཁོར་དང་། སྤྲུལ་པའི་དཀྱིལ་འཁོར་ཏེ། གང་གི་ཚེ་གང་གིས་རྣམ་པར་མི་རྟོག་པའི་སྦྱོར་བ་ལ་ཞུགས་པའི་རྣམ་པར་སྨིན་པ་ནི་སྤྲུལ་པའོ། །

[Block 1516]
རྣམ་པར་མི་རྟོག་པའི་དོན་ཐོབ་པ་དེའི་རྣམ་པར་སྨིན་པ་ནི་ལོངས་སྤྱོད་རྫོགས་པར་འགྱུར་རོ། །

[Block 1517]
དེ་དག་ཉིད་ཀྱི་དོན་བསྟན་པ་ནི། སྦྱོར་བ་དང་ནི་ཐོབ་པས་སོ། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 1518 [HEADING]]
### རྒྱུ་མཐུན་པ། ^8-10-0

[Block 1519]
ཡེ་ཤེས་དེའི་རྒྱུ་མཐུན་པ་གང་ཡིན་ཞེ་ན།

[Block 1520 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས། །
རྣམ་རྟོག་མེད་པའི་རྒྱུ་མཐུན་ནི། །
ཕྱི་མ་ཕྱི་མའི་ཚེ་རྣམས་སུ། །

[Block 1521]
ཞེས་བྱ་བ་སྟེ། བཤད་མ་ཐག་པའི་དཀྱིལ་འཁོར་གཉིས་པོ་དག་ཕྱི་མ་ཕྱི་མའི་ཚེ་ལ་རྣམ་པར་རྟོག་པ་མེད་པའི་རྒྱུ་མཐུན་པས། ཁྱད་པར་དུ་ནི་འགྲོ་བར་འདོད། །ཅེས་བྱ་བ་སྟེ། གང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་བྱེ་བྲག་ཏུ་གྱུར་པ་དེ་ཉིད་དེའི་རྒྱུ་མཐུན་པར་བལྟ་བར་བྱའོ། །

[Block 1522 [HEADING]]
### ངེས་པར་འབྱུང་བ། ^8-11-0

[Block 1523]
དེ་ཇི་ལྟར་ངེས་པར་འབྱུང་བར་འགྱུར་ཞེ་ན། དེ་ལ།

[Block 1524 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས། །
རྣམ་རྟོག་མེད་པའི་ངེས་འབྱུང་ནི། །

[Block 1525]
ཞེས་བྱ་བ་ལ། མཐར་ཐུག་པར་འགྲོ་བ་ནི་ངེས་པར་འབྱུང་བ་སྟེ། མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1526]
ཐོབ་པ་དང་ནི་གྲུབ་ཕྱིར་རོ། །ཞེས་བྱ་བ་ལ། ཡེ་ཤེས་དེ་དང་པོ་ཐོབ་པ་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 1527]
དེ་ནས་བསྐལ་པ་བརྒྱ་སྟོང་དུ་མ་ན་གྲུབ་པ་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 1528]
ས་བཅུ་དག་ཏུ་ཤེས་བྱ་སྟེ། །ཞེས་བྱ་བ་ལ། དང་པོ་ནས་བརྩམས་ནས་རིམ་པ་འདི་ཉིད་ཀྱིས་ས་དང་པོ་ལ་ནི་ཐོབ་པ་ཙམ་དུ་འགྱུར་རོ། །

[Block 1529]
དུས་ཕྱིས་ནི་ཆེན་པོ་ཉིད་དུ་འགྲུབ་པར་འགྱུར་ཏེ། དེའི་ཕྱིར་འདི་ལྟར་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས་མྱ་ངན་ལས་འདས་པར༌[^950]འགྱུར་ཏེ། འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་དེ་སྲིད་ཀྱིས་རྣམ་པར་མི་རྟོག་པའི་མཐར་ངེས་པར་འབྱུང་བར་འགྱུར་རོ། །

[Block 1530 [HEADING]]
### མཐར་ཐུག་པར་འགྲོ་བ། ^8-12-0

[Block 1531]
མཐར་ཐུག་པར་འགྲོ་བ་གང་ཡིན་ཞེ་ན། འདི་ལྟར་བཤད་མ་ཐག་པའི་རིམ་པ་འདི་ཉིད་ཀྱིས་ཐོབ་པར་གྱུར་པ་ནི་མཐར་ཐུག་པ་སྟེ།

[Block 1532 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས། །
རྣམ་རྟོག་མེད་པའི་མཐར་ཐུག་པ། །
དག་པའི་སྐུ་གསུམ་ཐོབ་ཕྱིར་དང་། །

[Block 1533]
ཞེས་བྱ་བའི་དོན་ཏེ། དག་པ་སྨོས་པ་ནི་འདིར་འདི་ལྟར་སྐུ་གསུམ་པོ་ས༌[^951]

[Block 1534]
དང་པོ་ཉིད་དུ་ཐོབ་པ་ཡིན་ལ།

[Block 1535]
བཅུ་པ་ལ་ནི་ཤིན་ཏུ་རྣམ་པར་དག་པར་འགྱུར་རོ། །

[Block 1536]
དབང་གི་མཆོག་ནི་ཐོབ་ཕྱིར་རོ། །ཞེས་བྱ་བ་ནི་དག་པའི་སྐུ་གསུམ་འབའ་ཞིག་ཐོབ་པས་མཐར་ཐུག་པར་འགྲོ་བ་མ་ཡིན་གྱི། གང་ཡང་ཡེ་ཤེས་རྣམ་པར་མི་རྟོག་པ་དང་། འཆད་པར་འགྱུར་བའི་དབང་བཅུ་པོ་དེ་དག་ཐོབ་པས་ཀྱང་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 1537 [HEADING]]
### ཕན་ཡོན། ^8-13-0

[Block 1538]
རྣམ་པར་མི་རྟོག་པ་དེའི་ཕན་ཡོན་གང་ཡིན་ཞེ་ན། དེ་ལ་རེ་ཞིག་རྣམ་པར་མི་རྟོག་པ་ནི་རྣམ་པ་གསུམ་སྟེ། སྦྱོར་བ་ལས་བྱུང་བའི་རྣམ་པར་མི་རྟོག་པ༌[^952]དང་རྩ་བ་སྟེ། གང་རྣམ་པར་མི་རྟོག་པ་ཉིད་དང་། རྣམ་པར་མི་རྟོག་པའི་རྗེས་ལས་ཐོབ་པའོ། །

[Block 1539 [HEADING]]
#### སྦྱོར་བ་ལས་བྱུང་བའི་ཕན་ཡོན། ^8-13-1-0

[Block 1540]
དེ་ལས་སྦྱོར་བ་ལས་བྱུང་བའི་རྣམ་པར་མི་རྟོག་པ་ཉིད་ནི་གང་བྱང་ཆུབ་སེམས་དཔའ་དེས་དང་པོར་ཕ་རོལ་པོ་ལས་རྣམ་པར་མི་རྟོག་པ་ཐོབ་ལ་དེ་ནས་བདག་ཉིད་ཀྱིས་རིགས་པས་དཔྱད་ནས་ལྷག་པར་མོས་པར་བྱེད་ཅིང་། ལྷག་པར་མོས་པ་དེ་ལ་བརྟེན་ནས་གང་ངེས་པར་ཞུགས་པའི་རྣམ་པར་མི་རྟོག་པ་དེ་ནི། སྦྱོར་བ་ལས་བྱུང་བའི༌[^953]རྣམ་པར་མི་རྟོག་པ་ཞེས་བྱ་བས། དེ་ལྟ་བུ་ཉིད་ནི་རྣམ་པར་མི་རྟོག་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1541]
སྦྱོར་བ་ལས་བྱུང་བ་དེའི་ཕན་ཡོན་གང་ཞེ་ན།

[Block 1542 [VERSE]]
རྣམ་རྟོག་མེད་པའི་ཡེ་ཤེས་དེ། །
གོས་པ་མེད་དེ་ནམ་མཁའ་བཞིན། །

[Block 1543]
གང་གིས་མ་གོས་ཤེ་ན། དེ་བསྟན་པ། སྡིག་པ་སྣ་ཚོགས་དྲག་རྣམས་ཀྱིས་སོ། །

[Block 1544]
རྒྱུ་གང་གིས་མ་གོས་པ་དེ་བསྟན་པ། དད་པ་ཙམ་དང་མོས་པ་ཡིས། །ཞེས་བྱ་བ་ལ། དད་པ་ཙམ་དང་། གང་རྣམ་པར་མི་རྟོག་པ་ལ་ལྷག་པར་མོས་པ་དེ་ནི་དེའི་ཕྱིར་ངན་འགྲོར་འགྲོ་བའི་གཉེན་པོ་ཉིད་ཡིན་ཞིང་། སྒྲིབ་པ་སྤངས་པར་གྱུར་པས་མི་གོས་པའོ། །

[Block 1545 [HEADING]]
#### རྩ་བ་རྣམ་པར་མི་རྟོག་པའི་ཕན་ཡོན། ^8-13-2-0
--- END BLOCKS ---
