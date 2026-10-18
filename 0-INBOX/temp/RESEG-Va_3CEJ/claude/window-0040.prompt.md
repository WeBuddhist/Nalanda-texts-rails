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
ད་ནི་ཇི་ལྟར་བསམ་གཏན་དང་པོ་ཡན་ལག་ལྔ་པར་བཤད་ཅེ་ན། ས་ལས་དེ་ཡན་ལག་ལྔ་པར་བཤད་ཀྱི་སྐད་ཅིག་ལས་ནི་མ་ཡིན་ནོ། །

[Block 1402 [HEADING]]
###### ང་རྒྱལ་དང་རྒྱགས་པ། ^2-2-2-3-4-0

[Block 1403]
ང་རྒྱལ་དང་རྒྱགས་པ་དག་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག་ཡོད་ཅེ་ན།

[Block 1404 [VERSE]]
ང་རྒྱལ་ཁེངས་པ་རྒྱགས་པ་ནི། །
རང་གི་ཆོས་ལ་ཆགས་པ་ཡི། །
སེམས་ནི་ཡོངས་སུ་གཏུགས་པའོ། །

[Block 1405]
ཕ་རོལ་པོ་ལས་གང་ཡང་རུང་བའི་ཁྱད་པར་ཞིག་ཡོངས་སུ་བརྟགས་ནས་སེམས་ཁེངས་པ་ནི་ང་རྒྱལ་ལོ། །

[Block 1406]
རྒྱགས་པ་ནི་རང་གི་ཆོས་རྣམས་ཁོ་ན་ལ་ཆགས་པའི་སེམས་ཡོངས་སུ་གཏུགས་པ་གང་ཡིན་པའོ། །

[Block 1407]
གཞན་དག་ན་རེ་ཆང་ལས་སྐྱེས་པ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་རྒྱགས་པ་ཡང་འདོད་ཆགས་ལས་སྐྱེས་པའི་ཀུན་ཏུ་དགའ་བའི་བྱེ་བྲག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1408]
སེམས་ལས་བྱུང་བ་རྣམས་སེམས་དང་བཅས་ཏེ་རྣམ་པ་རེ་རེ་ནས་བཤད་ཟིན་ཏོ། །

[Block 1409 [HEADING]]
##### སེམས་དང་ཡིད་དང་རྣམ་ཤེས་དོན་གཅིག། ^2-2-2-4-0

[Block 1410]
གསུང་རབ་ལས་འདི་དག་གིས་ཐ་སྙད་དུ་འདོགས་པའི་ཕྱིར་དེ་དག་གི་མིང་འདི་དག་བརྗོད་དེ། སེམས་དང་ཡིད་དང་རྣམ་ཤེས་ནི་དོན་གཅིག་འབྱེད་པས་ན་སེམས་སོ། །ཤེས་པས་ན༌[^609]ཡིད་དོ། །

[Block 1411]
རྣམ་པར་ཤེས་པ་ནས་རྣམ་པར་ཤེས་པའོ། །

[Block 1412]
ཁ་ཅིག་ན་རེ་དགེ་བ་དང་མི་དགེ་བའི་ཁམས་དག་གིས་བསགས་པས་ན་སེམས་སོ། །

[Block 1413]
དེ་ཉིད་རྟེན་དུ་གྱུར་པ་ནི་ཡིད༌[^610]དོ། །

[Block 1414]
རྟེན་པར་གྱུར་པ་ནི་རྣམ་པར་ཤེས་པའོ་ཞེས་ཟེར་རོ། །

[Block 1415 [HEADING]]
##### རྟེན་དང་དམིགས་དང་རྣམ་བཅས་དང་མཚུངས་པར་ལྡན་པ། ^2-2-2-5-0

[Block 1416]
ཇི་ལྟར་སེམས་དང་ཡིད་དང་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་དོན་གཅིག་པ་དེ་བཞིན་དུ་སེམས་དང་སེམས་བྱུང་དང་། །རྟེན་དང་དམིགས་དང་རྣམ་བཅས་དང་། མཚུངས་པར་ལྡན་པའང་། དོན་གཅིག་སྟེ། སེམས་དང་སེམས་ལས་བྱུང་བ་དེ་དག་ཉིད་དབང་པོ་ལ་བརྟེན་པའི༌[^611]ཕྱིར་རྟེན་དང་བཅས་པ་དག་ཅེས་བྱའོ། །

[Block 1417]
ཡུལ་ལ་འཛིན་པའི་ཕྱིར་དམིགས་པ་དང་བཅས་པ་དག་གོ། །

[Block 1418]
དམིགས་པ་དེ་ཉིད་ལ་རྣམ་པ་རེ་རེ་ནས་བྱེ་བྲག་ཏུ་གཅོད་པའི་ཕྱིར་རྣམ་པ་དང་བཅས་པ་དག་གོ། །

[Block 1419]
མཉམ་པར་ལྡན་པའི་ཕྱིར་མཚུངས་པར་ལྡན་པ་དག་གོ། །

[Block 1420]
རྣམ་པ་གང་དག་གིས་མཚུངས་པར་ལྡན་ཞེ་ན། རྣམ་པ་ལྔས།[^612] མཚུངས་པ་རྣམ་པ་ལྔ་པོ་རྟེན་དང་དམིགས་པ་དང་རྣམ་པ་དང་དུས་དང་རྫས་མཚུངས་པ་དག་གིས་མཚུངས་པར་ལྡན་ནོ། །

[Block 1421]
རྫས་མཚུངས་པ་གང་ཞེ་ན། ཇི་ལྟར་སེམས་གཅིག་ཁོ་ན་ཡིན་པ་དེ་བཞིན་དུ་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱང་རེ་རེ་ཡིན་པའོ། །

[Block 1422]
སེམས་དང་སེམས་ལས་བྱུང་བ་རྒྱས་པ་དང་། རབ་ཏུ་དབྱེ་བ་དང་བཅས་པ་དག་བསྟན་ཟིན་ཏོ། །

[Block 1423 [HEADING]]
### ལྡན་པ་མ་ཡིན་པའི་འདུ་བྱེད། ^2-3-0

[Block 1424 [VERSE]]
མི་ལྡན་པ་ཡི་འདུ་བྱེད་རྣམས། །
ཐོབ་དང་མ་ཐོབ་སྐལ་མཉམ་དང་། །
འདུ་ཤེས་མེད་སྙོམས་འཇུག་དག་དང་། །
སྲོག་དང་མཚན་ཉིད་རྣམས་དང་ནི། །

[Block 1425]
མིང་གི་ཚོགས་ལ་སོགས་པ་ཡང་། །འདུ་བྱེད་འདི་དག་ནི་སེམས་དང་མཚུངས་པར་ལྡན་པ་ཡང་མ་ཡིན་ལ་གཟུགས་ཀྱི་རང་བཞིན་ཡང་མ་ཡིན་པས་སེམས་དང་ལྡན་པ་མ་ཡིན་པ་དག་ཅེས་བྱའོ། །

[Block 1426 [HEADING]]
#### ཐོབ་པ། ^2-3-1-0

[Block 1427]
དེ་ལ་རེ་ཞིག་ཐོབ་པ་རྙེད་དང་ལྡན་པའོ། །

[Block 1428]
ཐོབ་པ་ནི་རྣམ་པ་གཉིས་ཏེ། མ་ཐོབ་པ་དང་རྣམ་པར་ཉམས་པ་ལས་རྙེད་པ་དང་། ཐོབ་ནས་ལྡན་པའོ། །

[Block 1429]
བཟློག་པ་ནི་མ་ཐོབ་པ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 1430]
ཐོབ་པ་དང་མ་ཐོབ་པ་འདི་དག་གང་གི་ཡིན་ཞེ་ན། ཐོབ་དང་མ་ཐོབ་རང་རྒྱུད་དུ། །གཏོགས་པ་རྣམས་ཀྱིའོ། །

[Block 1431]
གཞན་གྱི་རྒྱུད་དུ་གཏོགས་པ་རྣམས་ཀྱི་ནི་མ་ཡིན་ཏེ། གཞན་གྱི་དག་དང༌[^613]ནི་འགལ་ཡང༌[^614]ལྡན་པ་མེད་དོ། །

[Block 1432]
རྒྱུད་དུ་མ་གཏོགས་པ་རྣམས་ཀྱི་ཡང་མ་ཡིན་ཏེ། སེམས་ཅན་དུ་མི་བགྲང་བ་དག་དང་ནི་འགའ་ཡང་ལྡན་པ་མེད་དོ། །

[Block 1433]
འདི་ནི༌[^615]རེ་ཞིག་འདུས་མ༌[^616]བྱས་དག་གི་ངེས་པ་ཡིན་ནོ། །

[Block 1434]
འདུས་མ་བྱས་རྣམས་ཀྱི་ཐོབ་པ་དང་མ་ཐོབ་པ་དག་ནི། འགོག་གཉིས་ཀྱི། སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་དང་ནི་སེམས་ཅན་ཐམས་ཅད་དང༌[^617]ལྡན་ནོ། །

[Block 1435]
དེ་ཉིད་ཀྱི་ཕྱིར་ཆོས་མངོན་པ་ལས།

[Block 1436]
ཟག་པ་མེད་པའི་ཆོས་རྣམས་དང་སུ་ཞིག་ལྡན་ཞེ་ན། སྨྲས་པ། སེམས་ཅན་ཐམས་ཅད་དོ་ཞེས་འབྱུང་ངོ་ཞེས་གྲག་གོ། །

[Block 1437]
སོ་སོར་བརྟགས་པས་འགོག་པ་དང་ནི་འཆིང་བ་མཐའ་དག་དང་ལྡན་པ་སྐད་ཅིག་མ་དང་པོ་ལ་གནས་པ་མ་གཏོགས་པ་འཕགས་པ་ཐམས་ཅད་དང་། སོ་སོའི་སྐྱེ་བོ་ཁ་ཅིག་ཀྱང་ཡིན་ནོ། །

[Block 1438]
ནམ་མཁའ་དང་ནི་འགའ་ཡང་ལྡན་པ་མེད་དེ། དེ་བས་ན་འདི་ལ་ཐོབ་པ་མེད་དེ། གང་ལ་ཐོབ་པ་མེད་པ་དེ་ལ་ནི་མ་ཐོབ་པ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་གྲུབ་པའི་མཐའ་ཡིན་ནོ། །

[Block 1439]
ཐོབ་པ་ཞེས་བྱ་བ་རྫས་གཞན་ཅུང་ཟད་ཅིག་ཡོད་དོ་ཞེས་བྱ་བ་འདི་གང༌[^618]ལས།

[Block 1440]
སྨྲས་པ་མདོ་ལས་ཏེ། མདོ་ལས་དེ་མི་སློབ་པའི་ཆོས་བཅུ་པོ་འདི་དག་བསྐྱེད་ཅིང་སོ་སོར་ཐོབ་པ་ལས༌[^619]ཀུན་ཏུ་ལྡན་པས་ན་ཡན་ལག་ལྔ་རྣམ་པར་སྤངས་པའི་འཕགས་པར་འགྱུར་རོ་ཞེས་རྒྱས་པར་གསུངས་སོ། །
--- END BLOCKS ---
