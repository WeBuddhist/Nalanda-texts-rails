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
[Block 1541]
དེའི་འོག་ཏུ་བཤད་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། བཤད་པ་ཞེས་བྱ་བ་ནི་དེ༌[^1395]ལྟར་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་གསུམ་མདོར་བསྟན་པ་དེ་ཉིད་རྒྱས་པར་བཤད་པ་གང་ཡིན་པའོ། །

[Block 1542]
བཤད་པ་འདི་ཡང་རྣམ་པ་གཉིས་ཏེ། དགོས་པ་དྲུག་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པ་དང་། དེ་དག་གི་དངོས་པོ་བསྡུ་བ་བསྟན་པའོ། །

[Block 1543 [HEADING]]
###### **དགོས་པ་དྲུག་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པ།** ^4-2-2-2-2-1-0

[Block 1544]
དེ་ལ་དགོས་པ་དྲུག་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པ་ནི་གཉེན་པོའི་དགོས་པ་དང་། དཔེའི་དགོས་པ་དང་། མངོན་པར་བསྒྲུབ་པའི་དགོས་པ་དང་། ཐབས་ཀྱི་དགོས་པ་དང་། རྟོགས་པའི་དགོས་པ་དང་། ཕན་ཡོན་གྱི་དགོས་པ་དང་ལྡན་པའོ། །

[Block 1545]
དེ་ལ་གཉེན་པོའི་དགོས་པ་དང་ལྡན་པ་ནི་ཡོན་ཏན་འབྱུང་གནས་དེ་ལ་ཆོས་རྣམས་ཀྱི་ཀུན་བརྟགས་པའི་མཚན་ཉིད་གང་ཞེ་ན་ཞེས་བྱ་བ་ནས། བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཀྱི་བར་དུ་ཡང་དག་པར་བསྒྲུབ་པ་གང་ཡིན་པའོ་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 1546]
དཔེའི་དགོས་པ་དང་ལྡན་པ་ནི། ཡོན་ཏན་འབྱུང་གནས་འདི་ལྟ་སྟེ། དཔེར་ན་ཞེས་བྱ་བ་ནས། གསེར་དུ་ལོག་པར་འཛིན་པས་ཀྱང་སེམས་ཅན་རྣམས་རྣམ་པར་རྨོངས་པར་བྱེད་དོ་ཞེས་གསུངས་པའི་ཁྱད་པར་གྱིས་བསྟན་ཏོ། །

[Block 1547]
མངོན་པར་བསྒྲུབ་པའི་དགོས་པ་དང་ལྡན་པ་ནི་ཡོན་ཏན་འབྱུང་གནས་འདི་ལྟ་སྟེ། དཔེར་ན་ཤེལ་ཤིན་ཏུ་གསལ་བ་ཚོན་དང་ཕྲད་པ་དེ་ལྟ་བུ་ནི་ཞེས་བྱ་བ་ནས། ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་བལྟ་བར༌[^1396]བྱའོ་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 1548]
ཐབས་ཀྱི་དགོས་པ་དང་ལྡན་པ་ནི་ཡོན་ཏན་འབྱུང་གནས་དེ་ལ་མཚན་མ་དང་འབྲེལ་པའི་མིང་ལ་བརྟན༌[^1397]ནས་ནི་ཀུན་བརྟགས་པའི་མཚན་ཉིད་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བ་ནས་ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་རབ་ཏུ་ཤེས་སོ་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 1549]
རྟོགས་པའི༌[^1398]དགོས་པ་དང་ལྡན་པ་ནི་ཡོན་ཏན་འབྱུང་གནས་དེ་ལ་བྱང་ཆུབ་སེམས་དཔས་ཆོས་རྣམས་ཀྱི་གཞན་གྱི་དབང་གི་མཚན་ཉིད་ལ་ཀུན་བརྟགས་པའི་མཚན་ཉིད་ཡང་དག་པ༌[^1399]ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་ན་ཞེས་བྱ་བ་ནས། རྣམ་པར་བྱང་བའི་མཚན་ཉིད་ཀྱི་ཆོས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 1550]
ཕན་ཡོན་གྱི་དགོས་པ་དང་ལྡན་པ་ནི། ཡོན་ཏན་འབྱུང་གནས་དེ་ལ་བྱང་ཆུབ་སེམས་དཔས་གཞན་གྱི་དབང་གི་མཚན་ཉིད་ལ་མཚན་ཉིད་མེད་པའི་ཆོས་ཡང་དག་པ༌[^1400]ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་ན་ཞེས་བྱ་བ་ནས། རྣམ་པར་བྱང་བའི་མཚན་ཉིད་ཀྱི་ཆོས་ཐོབ་པར་འགྱུར་ཏེ་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 1551]
དེ་དག་གི་དངོས་པོ་བསྡུ་བ་ནི། ཡོན་ཏན་འབྱུང་གནས་གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔས༌[^1401]དེ་ལྟར་ཆོས་རྣམས་ཀྱི་ཀུན་བརྟགས་པའི་མཚན་ཉིད་ཡང་དག་པ་ཇི་ལྟ་བ༌[^1402]བཞིན་དུ་རབ་ཏུ་ཤེས་ཤིང་ཞེས་བྱ་བ་ནས། ཚིགས་སུ་བཅད་པ་རྫོགས་པའི་བར་གྱི་གཞུང་ལྷག་མ་ཐམས་ཅད་ཀྱིས་བསྟན་ཏོ། །

[Block 1552 [HEADING]]
###### **གཉེན་པོའི་དགོས་པ་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པ།** ^4-2-2-2-2-1-1-0

[Block 1553]
དེ་ལ་དང་པོར་གཉེན་པོའི་དགོས་པ་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། གཉེན་པོའི་དགོས་པ་དང་ལྡན་པའི་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་བསྟན་པ་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་རྨོངས་པ་རྣམ་པ་བཞིའི་གཉེན་པོའི་དགོས་པ་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་གསུམ་བསྟན་པ་གང་ཡིན་པའོ། །

[Block 1554]
དེ་ལ་ཤིན་ཏུ་རྨོངས་པ་རྣམ་པ་བཞི་ནི་མེད་པའི་དོན་ལ་ཤིན་ཏུ་རྨོངས་པ་སྒྲོ་འདོགས་པའི་རྒྱུ་དང་། ཡོད་པའི་དོན་ལ་ཤིན་ཏུ་རྨོངས་པ་སྐུར་པ་འདེབས་པའི་རྒྱུ་དང་། ཀུན་ནས་ཉོན་མོངས་པ་ལ་ཤིན་ཏུ་རྨོངས་པ་དེ་འཇིག་པའི་རྒྱུ་དང་རྣམ་པར་བྱང་བ་ལ་ཤིན་ཏུ་རྨོངས་པ་དེ་འཇིག་པའི་རྒྱུའོ། །

[Block 1555 [HEADING]]
###### **མེད་པའི་དོན་ལ་ཤིན་ཏུ་རྨོངས་པ་སྒྲོ་འདོགས་པའི་རྒྱུའི་གཉེན་པོ།** ^4-2-2-2-2-1-1-1-0

[Block 1556]
དེ་ལ་དང་པོར་མེད་པའི་དོན་ལ་ཤིན་ཏུ་རྨོངས་པའི་སྒྲོ་འདོགས་པའི་རྒྱུའི་གཉེན་པོའི་དགོས་པ་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། དེ་ལ་མེད་པའི་དོན་ཅེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་མཚན་ཉིད་དེ་ནི་ཁམས་གསུམ་པའི་སེམས་དང་སེམས་ལས་བྱུང་བ་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་རྟོག་པས༌[^1403]གཞན་གྱི་དབང་དང་ཡོངས་སུ་གྲུབ་པའི་དངོས་པོ་ལ་ངོ་བོ་ཉིད་དམ་བྱེ་བྲག་ཏུ་ཀུན་བརྟགས་པ་དང་མིང་དང་བརྡར་བཏགས་པ་དང་། ཐ་སྙད་དུ་བརྗོད་པར་ཟད་ཀྱི་གཟུང་བ་དང་འཛིན་པའི་ངོ་བོ་ཉིད་གང་ཡང་མ་ཡིན་ཏེ། ནམ་མཁའི་མེ་ཏོག་དང་འདྲ་བར་མཚན་ཉིད་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཀྱིས་ངོ་བོ་ཉིད་མེད་པ་ཀུན་རྫོབ་དང་། དོན་དམ་པའི་བདེན་པ་གཉི་གར་གཏན་མེད་པས་ན་མེད་པའི་དོན་ཅེས་བྱའོ། །

[Block 1557]
དེ་ལ་ཤིན་ཏུ་རྨོངས་པ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་མཚན་ཉིད་མེད་པའི་དོན་ལ་ཡོད་པར་མངོན་པར་ཞེན་པ་ཡིན་ནོ། །

[Block 1558]
སྒྲོ་འདོགས་པའི་རྒྱུ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་མེད་པའི་དོན་ལ་ཤིན་ཏུ་རྨོངས་པ་དེ་ཉིད་སྒྲོ་འདོགས་པའི་རྒྱུ་ཡིན་ཏེ། མེད་པའི་དོན་ལ་མེད་པར་མངོན་པར་ཞེན་ཅིང་ཤིན་ཏུ་རྨོངས་པ་དེས་མེད་པའི་དོན་དེ་ལ་ཡོད་པར་སྒྲོ་འདོགས་པའི་ཕྱིར་རོ། །

[Block 1559]
དེའི་གཉེན་པོའི་དགོས་པ་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་སྒྲོ་འདོགས་པའི་རྒྱུ་དེ་རྣམ་པར་སེལ་བའི་གཉེན་པོའི་དོན་དང་ལྡན་པ་ཀུན་བརྟགས་པའི་ཆོས་ཀྱི་མཚན་ཉིད་ནམ་མཁའི་མེ་ཏོག་དང་འདྲ་བ་བདེན་པ་གཉི་གར་གཏན་མེད་པར་བསྟན་པ་གང་ཡིན་པ་དེ། དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཡོན་ཏན་འབྱུང་གནས་དེ་ལ་ཆོས་རྣམས་ཀྱི༌[^1404]ཀུན་བརྟགས་པའི་མཚན་ཉིད་གང་ཞེ་ན། ཇི་ཙམ་དུ་རྗེས་སུ་ཐ་སྙད་གདགས་པའི་ཕྱིར་ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་དམ་བྱེ་བྲག་ཏུ་མིང་དང་བརྡར་རྣམ་པར་གཞག་པ་གང་ཡིན་པའོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1560]
དེ་ལ་ཇི་ཙམ་དུ་རྗེས་སུ་ཐ་སྙད་གདགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྒྲོ་བཏགས་པའི་ཕྱིར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1561]
ཆོས་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དབང་གི་མཚན་ཉིད་ཀྱི་ཆོས་དང་། ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་ཀྱི་ཆོས་རྣམས་ཀྱིའོ། །

[Block 1562]
ངོ་བོ་ཉིད་དམ་བྱེ་བྲག་ཏུ་མིང་དང་བརྡར་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་ཀྱི་མཚན་ཉིད་དུ་མིང་དང་བརྡར་བཏགས་པ་དང་། བྱེ་བྲག་གི་མཚན་ཉིད་དུ་མིང་དང་བརྡར༌[^1405]བཏགས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། ཀུན་བརྟགས༌[^1406]པ་དང་། བཏགས་པ་དང་། བརྗོད་པའི་དོན་ཏོ། །

[Block 1563]
དེ་ལ་ངོ་བོ་ཉིད་ཅེས་བྱ་བ་ནི་འདི་ནི་གཟུགས་སོ། །

[Block 1564]
འདི་ནི་ཚོར་བའོ། །

[Block 1565]
འདི་ནི་འདོད་ཆགས་སོ། །

[Block 1566]
འདི་ནི་དད་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུར་ངོ་བོ་ཉིད་དུ་སྒྲོ་བཏགས་པ་གང་ཡིན་པའོ། །

[Block 1567]
བྱེ་བྲག་ཞེས༌[^1407]བྱ་བ་ནི་གཟུགས་འདི་ནི་ཟག་པ་དང་བཅས་པའོ། །

[Block 1568]
འདི་ནི་ཟག་པ་མེད་པའོ། །

[Block 1569]
ཚོར་བ་འདི་ནི་སྲེད་པས་བརླན་པའོ། །

[Block 1570]
འདི་ནི་སྲེད་པས་མ་བརླན་པའོ། །

[Block 1571]
འདོད་ཆགས་འདི་ནི་མཐོང་བས་སྤོང་བར་བྱ་བའོ།[^1408] །འདི་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བའོ།[^1409] །དད་པ་འདི་ནི་ལས་དང་འབྲས་བུ་ལ་ཡིད་ཆེས༌[^1410]པའོ། །

[Block 1572]
འདི་ནི་དཀོན་མཆོག་དང་བདེན་པ་ལ་སེམས་དང་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུར་བྱེ་བྲག་ཏུ་སྒྲོ་བཏགས་པ་གང་ཡིན་པའོ། །

[Block 1573]
མིང་ཞེས་བྱ་བ་ནི་ཐ་སྙད་གཞན་དུ་མི་འཁྲུལ་པའི་རྒྱུ་སྟེ། གཟུགས་ཤེའམ། ཚོར་བ་ཞེའམ། [^1411]འདོད་ཆགས་ཤེ་འམ། དད་པ་ལ་སོགས་པ་ལྟ་བུར་ཚིག་གིས་གདགས་པ་ཡིན་ནོ། །

[Block 1574]
བརྡ་ཞེས་བྱ་བ་ནི་ཐ་སྙད་གོ་བར་བྱེད་པའི་རྒྱུ་སྟེ། འདིར་འདུག་ཤིག༌[^1412]པའམ། ཕར་སོང་ཤིག༌[^1413]པའམ། བྱོས་ཤིག་པའམ། མ་བྱེད་ཅིག་པ་ལ་སོགས་པ་ལྟ་བུའི་ཐ་སྙད་ཚིག་གམ། ལག་བརྡའམ། མིག་ཟུར་ལ་སོགས་པས་གོ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 1575]
རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་ནི་ཁམས་གསུམ་པའི་སེམས་དང་སེམས་ལས་བྱུང་བ་ཡང་དག་པ༌[^1414]མ་ཡིན་པ་ཀུན་རྟོག་པས༌[^1415]གཞན་གྱི་དབང་དང་། ཡོངས་སུ་གྲུབ་པའི་དངོས་པོའི་ངོ་བོ་ཉིད་དང་བྱེ་བྲག་ཏུ་ཀུན་བརྟགས་པ་དང་། མིང་དང་བརྡར་བཏགས་པ་དང་། ཐ་སྙད་དུ་བརྗོད་པ་རྣམ་པར་གཞག་པ་སྟེ། དེ་ནི་དངོས་པོ་ལ་གློ་བུར་བ་ཡིན་ནོ། །

[Block 1576]
དེ་ལྟར་ན་ཀུན་བརྟགས་པའི་མཚན་ཉིད་ནི་ཀུན་བརྟགས་པ་ཙམ་དུ་ཟད་ཀྱི། གཟུང་བ་དང་འཛིན་པའི་ངོ་བོ་ཉིད་མ་ཡིན་པས་དེ་ལྟར་ཤེས་ན་མེད་པའི་དོན་ལ་ཤིན་ཏུ་རྨོངས་ཤིང་ཡོད་པ་སྒྲོ་འདོགས་པའི་ཕྱིར་དེ་ནི་མེད་པའི་དོན་ལ་ཤིན་ཏུ་རྨོངས་པ་སྒྲོ་འདོགས་པའི༌[^1416]རྒྱུའི་གཉེན་པོར་དགོས་པ་དང་ལྡན་པར་ཀུན་བརྟགས་པའི་མཚན་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 1577 [HEADING]]
###### **ཡོད་པའི་དོན་ལ་ཤིན་ཏུ་རྨོངས་པ་སྐུར་པ་འདེབས་པའི་རྒྱུའི་གཉེན་པོ།** ^4-2-2-2-2-1-1-2-0

[Block 1578]
དེའི་འོག་ཏུ་ཡོད་པའི་དོན་ལ་ཤིན་ཏུ་རྨོངས་པ་སྐུར་པ་འདེབས་པའི་རྒྱུའི་གཉེན་པོའི་དགོས་པ་དང་ལྡན་པའི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། དེ་ལ་ཡོད་པའི་དོན་ཅེས་བྱ་བ་ནི་གཞན་གྱི་དབང་གི་མཚན་ཉིད་དེ། དེ་ནི་ཕྱི་ནང་གི་དངོས་པོའི་ངོ་བོ་ཉིད་རྐྱེན་གཞན་གྱི་དབང་གིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྟེ། སྒྱུ་མ་བྱས་པ་དང་འདྲ་བར་སྐྱེ་བ་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཀྱིས་ངོ་བོ་ཉིད་མེད་པ་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཉིད་དུ་ཡོད་པའི་ཕྱིར་ཡོད་པའི་དོན་ཅེས་བྱའོ། །

[Block 1579]
དེ་ལ་ཤིན་ཏུ་རྨོངས་པ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དབང་གི་མཚན་ཉིད་ཡོད་པའི་དོན་ལ་མེད་པར་མངོན་པར་ཞེན་པ་ཡིན་ནོ། །

[Block 1580]
སྐུར་པ་འདེབས་པའི་རྒྱུ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཡོད་པའི་དོན་ལ་ཤིན་ཏུ་རྨོངས་པ་དེ་ཉིད་སྐུར་པ་འདེབས་པའི་རྒྱུ་ཡིན་ཏེ། ཡོད་པའི་དོན་ལ་མེད་པར་མངོན་པར་ཞེན་ཅིང་ཤིན་ཏུ་རྨོངས་པ་དེས་ཡོད་པའི་དོན་ལ་མེད་པར་སྐུར་པ་འདེབས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
