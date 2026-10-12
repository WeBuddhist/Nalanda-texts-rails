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
རྒྱལ་སྲས་ཐམས་ཅད་ཉིད་ཀྱང་ཡིན། །ཞེས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་བདག་པོར་གྱུར་པ་ཡང་ཡིན་ཞེས་པ་སྟེ་ཐ་དད་དུ་མེད་པ་ཡིན་ནོ། །

[Block 1402]
ངེས་པ༌[^738]ནི་མ་ནོར་བའོ། །

[Block 1403]
ད་ནི་དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པའི་དགོས་པ་བཤད་པའི་ཕྱིར། ད་ནི་རྒྱུད་འདི་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སེམས་གཙོ་བོ་ཡིན་པ་ནི་ཏིང་ངེ་འཛིན་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1404]
མི་བསྐྱོད་པ་ནི་ཐུགས་ཀྱི་ངོ་བོའི་ཕྱིར་རོ། །

[Block 1405]
འདི་སྐད་དུ་སྟོན་ཏོ།[^739] །སེམས་སྣང་བ་དང་བཅས་པ་གང་གི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གིས་སྦྱངས་པས་ཐོབ་པ་དེ་ནི་དེའི་རིགས་ཏེ་དེ་བས་ན་དེ༌[^740]གཙོ་བོར་གྱུར་པ་ཉིད་དོ། །

[Block 1406]
དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་དོན་ནི་གང་གིས་ཆོས་ཀྱི་འབྱུང་གནས་ཀྱི་ནང་དུ་བྷྲུཾ་ལ་སོགས་པའི་དེ་བཞིན་གཤེགས་པའི་གཞལ་ཡས་ཁང་ཕྱི་དང་ནང་ཤིན་ཏུ་གསལ་བ་ཇི་ལྟར་སྨོས་པའི་རྒྱན་ཐམས་ཅད་དང་ལྡན་པ་ཤིན་ཏུ་མཛེས་པ་བལྟ་ན་སྡུག་པའི་ངོ་བོ་ཉིད་དོ་ཞེས་བསྟན༌[^741]ཏོ། །

[Block 1407]
དེ་ལྟ་བུའི་གཞལ་ཡས་ཁང་གི་དབུས་སུ་ལྷག་པར་མོས་པ་ལྷ་ལྔའི་རྣམ་པར་བསྒོམས་ཏེ་སླར་རང་ལ་གཞུག་གོ། །

[Block 1408]
ལུང་ལས་ཀྱང་།

[Block 1409]
པདྨ་འདབ་མ་བཞིར་ལྡན་པའི། །རིགས་ལྔ་བསྐྱེད་པ་ཡང་དག་བསྒོམ། །

[Block 1410]
ཞེའོ། །

[Block 1411]
ངེས་པའི་དོན་དུ་བཤད་པ། [^742]རྣམ་པར་ཤེས་པའི་བདག་ཉིད་ཅན། །ཞེས་པ་ནི་དེའི་ངོ་བོ་ཉིད་དག་པས་དེར་གྱུར་པའོ། །

[Block 1412]
གཟུགས་ཀྱི་ཕུང་པོ་ལ་སོགས་པ་རྣམ་པར་ཤེས་པའི་བར་དུ་སྟེ་འདི་ལྟར་ཕུང་པོ་དང་། ཁམས་དང་སྐྱེ་མཆེད་ཐམས་ཅད་རང་གི་ཤེས་པའི་རང་བཞིན་ཏེ། དེ་ཉིད་ཡེ་ནས་སྤྲོས་པ་དང་བྲལ་ཞིང་མ་སྐྱེས་པའི་རང་བཞིན་ཐོགས་པ་མེད་པས་སངས་རྒྱས་ཐམས་ཅད་ཀྱིས་བསྟེན་པར་བྱ་བའི་ཕྱིར་བཙུན་མོའོ། །

[Block 1413]
ཡོངས་སུ་དག༌[^743]ཕྱིར་གསལ་བའོ། །

[Block 1414]
འོད་ཟེར་ཐམས་ཅད་ཀྱི་རང་བཞིན་པས་ན་སྣ་ཚོགས་ཀུན་དུ་རྒྱས་སོ། །

[Block 1415]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རང་བཞིན་པས་ན་དེའི་ངོ་བོ་ཉིད་དོ། །

[Block 1416]
སྣང་བ་ལས་བྱུང་བ་དང་། དེའི་རང་བཞིན་པས་ན༌[^744]གསལ་བ་ལ་སོགས་པ་སྟེ། འདིས་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཀྱི་ཡེ་ཤེས་ཀྱི་སྐུར་བཤད་ནས། དེ་ནས་སེམས་ཅན་ཐམས་ཅད༌[^745]དང་བྱང་ཆུབ་སེམས་དཔའ་ལ་ཇི་སྐད་དུ་བཤད་པའི་སྐུ་ཉིད་གསལ་བར་སྣང་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1417]
ནམ་མཁའ་ཀུན་ནི་དོན་དམ་པའི་དེ་བཞིན་ཉིད་དོ། །

[Block 1418]
དེའི་ངང་ལ་རྡོ་རྗེ་སེམས་དཔའ་རབ་ཏུ་བཞུགས་པ་ནི་ཡང་དག་པའི་ཡེ་ཤེས་ཀྱི་ཡུལ་དང་བྲལ་བའི་ཚུལ་དུ་བྱས་པའོ། །

[Block 1419]
དོན་འདི་ཉིད་ནི་བསྐྱེད་པའི་རིམ་པ་ཉིད་དོ། །

[Block 1420]
དེ་གསལ་བར་བྱ་བ་ནི་བསྟན་པ་དང་བཤད་པའི་རིམ་པས་སོ། །

[Block 1421]
འདས་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་བཤད་པའི་དོན་ནི་གང་གིས་དུས་གསུམ་གྱི་སངས་རྒྱས་ཐམས་ཅད་འདུས་པའི་བདག་ཉིད་ཅན་རྡོ་རྗེ་སེམས་དཔའ་ས་བོན་ལ་སོགས་པའི་གཟུགས་ཀྱིས་སྐྱེ་བ་དང་སྡུད་པའི་ཚུལ་བསྟན་པ་ཉིད་དོ། །

[Block 1422]
རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིས་ནི་དེའི་དགོས་པ་བསྟན་ཏོ། །

[Block 1423]
མ་འོངས་པའི་གང་ཟག་གིས་བསྐྱེད་པའི་རིམ་པ་བསྒོམས་ན་ཞེས་བྱ་བ་ཉིད་དོ། །

[Block 1424]
རྡོ་རྗེ་སེམས་དཔའ་དང་འདྲ་བར་འགྱུར་བར་དགོངས་སོ། །

[Block 1425]
ཕུང་པོ་ལ་སོགས་པ་ནི་ཡུལ་དང་དབང་པོ་ཐམས་ཅད་དོ། །

[Block 1426]
ཀུན་རྫོབ་བྱང་ཆུབ་སེམས་ནི་ཁུ་བ་སྟེ༌[^746]ཟག་པ་མེད་པའི་བདེ་བ་སྐྱེད་པའི༌[^747]ཕྱིར་རོ། །

[Block 1427]
གཅིག་ཏུ་མཛད་པ་ནི་དེས་མི་རྟོག་པའི་ཡེ་ཤེས་སྐྱེད་པའི་ཕྱིར་རོ། །

[Block 1428]
དེ་ཉིད་བཤད་པ། ནམ་མཁའི་དབྱིངས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། རྩ་ཕྲན་སྟོང་ཕྲག༌[^748]བདུན་ཅུ་རྩ་གཉིས་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ས་བོན་གནས་པའི་རྩ་སྟེ། དེ༌[^749]རླུང་ལ་སོགས་པའི་རིམ་པས་བྱང་ཆུབ་ཀྱི་སེམས་ཕབ་པས་ཟག་པ་མེད་པའི་བདེ་བ་ཡོངས་སུ་རྒྱས་པར་འགྱུར་རོ། །

[Block 1429]
དབང་པོ་གཉིས་ནི་རྡོ་རྗེ་དང་པདྨ་སྟེ་སྐྱེ་བ་ལ་དབང་བའི་ཕྱིར་རོ། །

[Block 1430]
དེས༌[^750]ཅིར་འགྱུར་ཞེ་ན། འདོད་ཆགས་ཆེན་པོའི་མེ་སྟེ་གང་ལ་སེམས་ཆེན་པོ་དང་ཏིང་ངེ་འཛིན་དུ་ལྡན་པ་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1431]
མཆོག་ཏུ་དགའ་བ་ནི་ཉོན་མོངས་པ་དང་བྲལ་བའི་དགའ་བའོ། །

[Block 1432]
འདི་ནི་དབང་པོ་གཉིས་སྦྱོར་བའི་སྣང་བ་གསུམ་མོ། །

[Block 1433]
དོན་དམ་པའི་བདེན་པས་གཅིག་ཏུ་མཛད་པ་ནི་སྤྲོས་པ་ཐམས་ཅད་དང་བྲལ་བའི་ཡེ་ཤེས་ཀྱི་རང་བཞིན་མེད་པར་གྱུར་པའོ། །

[Block 1434]
སྟོང་པ་ཉིད་གསུམ་ནི་གོང་དུ་བཤད་པའོ། །

[Block 1435]
ཐམས་ཅད་སྟོང་པ་ནི་མཐར་ཐུག་པ་ཉིད་དོ། །

[Block 1436]
དེ་ལྟར་ལྷག་པར་མོས་པས་ཞེས་བྱ་བ་ནི་དྲང་བ་དང་སྤྱིའི་དོན་དུ་བཤད་པ་ཡིན་གྱི་ཐམས་ཅད་ཀྱི༌[^751]ནི་མ་ཡིན་ནོ། །

[Block 1437]
ཡོངས་སུ་དག་པ་དང་ཡོངས་སུ་མ་དག་པ་ནི་སློབ་པ་དང་མི་སློབ་པ་དང་།[^752] ཤེས་བྱའི་སྒྲིབ་པ་མཐའ་དག་སྤངས་པ་དང་མ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 1438]
དེ་ལ་གཙོ་བོ་ནི་ཡོངས་སུ་དག༌[^753]པའོ། །

[Block 1439]
ལྷག་མ་ནི་ཡོངས་སུ་དག་པ་དང་མ་དག་པ་ཉིད་དོ། །

[Block 1440]
ཡི་གེ་གསུམ་ནི་ཨོཾ་ཨཱཿཧཱུཾ་གསུམ་མོ། །
--- END BLOCKS ---
