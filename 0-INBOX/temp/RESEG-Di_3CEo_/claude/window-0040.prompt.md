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
གཞན་རྣམས༌[^524]གསུམ་མོ། །

[Block 1402]
སྲིད་པ་བར་མ་ལ་སོགས་པ་ནི་དགེ་བ་དང་ཉོན་མོངས་པ་ཅན་དང་ལུང་དུ་མ་བསྟན་པ་རྣམས་སོ། །

[Block 1403]
དེ་ལས་ཀྱང་། གཟུགས་མེད་གསུམ། སྲིད་པ་བར་མ་མ་གཏོགས་སོ། །

[Block 1404]
འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་ན་སྲིད་པ་བཞི་པོ་ཡང་ཡོད་ཅེས་བྱ་བར་སྣང་བར་འགྱུར་རོ། །

[Block 1405 [HEADING]]
#### ཟས་ཀྱིས་གནས་པ། ^3-1-8-0

[Block 1406]
སེམས་ཅན་གྱི་སྐྱེ་བ་ཇི་ལྟ་བ་བཞིན་དུ་བཤད་ཟིན་ནས། གནས་པ་བརྗོད་པ། འགྲོ་བ་ཟས་ཀྱིས༌[^525]གནས་པ་ཡིན། །དེ་དག་ཀྱང་། ཁམ༌[^526]གྱི་ཟས་ལ་སོགས་པ་སྟེ། །དེ་ལ། ཁམ་གྱི་ཟས་ནི་འདོད་པ་ན། །གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ན་ནི་ཡང་མེད་དོ། །

[Block 1407]
དེ་ཡང་། སྐྱེ་མཆེད་གསུམ་གྱི་བདག་ཉིད་དོ། །

[Block 1408]
དྲི་དང་རོ་དང་རེག་བྱའི་སྐྱེ་མཆེད་རྣམས་ནི་ཁམ་གྱི་ཟས་ཁོ་ན་ཡིན་ཏེ།

[Block 1409 [VERSE]]
ཁམ་དུ་བྱས་ནས་མིད་པའི༌[^527]ཕྱིར་རོ། །
གཟུགས་ཀྱི་སྐྱེ་མཆེད་མ་ཡིན་དེས། །
རང་དབང་གྲོལ་ལ་མི་ཕན་ཕྱིར། །

[Block 1410]
གཟུགས་ཀྱི་སྐྱེ་མཆེད་ནི་ཁམ་དུ་བྱས་ནས་མིད་པ་ཡིན་ཡང་ཁམ་གྱི་ཟས་མ་ཡིན་ཏེ། མིད་པའི་ཚེ་རང་གི་དབང་པོ་དང་འབྱུང་བ་ཆེན་པོ་རྣམས་ལ་ཕན་མི་འདོགས་པའི་ཕྱིར་རོ། །

[Block 1411]
གང་གི་ཚེ་མཐོང་བ་ན་བདེ་བ་དང་ཡིད་བདེ་བར་བྱེད་པ་དེའི་ཚེ་ཡང་དེ་ལ་དམིགས་པ་བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པ་ཟས་ཡིན་གྱི་གཟུགས་མ་ཡིན་ནོ། །

[Block 1412]
གྲོལ་བ་ཕྱིར་མི་འོང་བ་དང་། དགྲ་བཅོམ་པ་ཟས་ཤིན་ཏུ་ཡིད་དུ་འོང་བ་མཐོང་བ་རྣམས་ལ་ཡང་ཕན་འདོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1413 [VERSE]]
རེག་དང་སེམས་པ་རྣམ་ཤེས་ནི། །
ཟག་བཅས་ཟས་ཡིན་གསུམ་དག་ན། །

[Block 1414]
རེག་པ་དང་། སེམས་པ་དང་། རྣམ་པར་ཤེས་པ་ཟག་པ་དང་བཅས་པ་དག་ཁོ་ན་ཟས་ཏེ། ཁམས་གསུམ་ཆར་ན་ཡང༌[^528]ཡོད་དོ། །ཅིའི་ཕྱིར་ཟག་པ་མེད་པ་རྣམས་མ་ཡིན་ཞེ་ན། འདི་ལྟར་སྲིད་པ་གསོ་བར་བྱེད་པའི་དོན་ནི་ཟས་ཀྱི་དོན་ཡིན་ན། དེ་དག་ནི་སྲིད་པ་ཟད་པར་བྱ་བའི་ཕྱིར་སྐྱེས་པ་དག་ཡིན་ནོ། །

[Block 1415]
གཞན་ཡང་མདོ་ལས།

[Block 1416]
སེམས་ཅན་བྱུང་བ་རྣམས་གནས་པར་བྱེད་པ་དང་། འཚོ་བར་བྱེད་པ་དང་། སྲིད་པ་ཚོལ་བར་བྱེད་པ་རྣམས་ལ་ཕན་པར་བྱེད་པ་ཡིན་ནོ་ཞེས་གསུངས་ན་ཟག་པ་མེད་པའི་སེམས་རྣམས་ནི་དེ་ལྟ་མ་ཡིན་པས་ཟས་མ་ཡིན་ནོ། །

[Block 1417]
རེ་ཞིག་བྱུང་བ་ནི་སེམས་ཅན་སྐྱེས་པ་རྣམས་ལ་བྱ་བར་ཡང་ཤེས༌[^529]ན། སྲིད་པ་ཚོལ་བ༌[^530]རྣམས་གང་ཞེ་ན།

[Block 1418 [VERSE]]
ཡིད་ལས༌[^531]བྱུང་དང་སྲིད་ཚོལ༌[^532]དང་། །
དྲི་ཟ་སྲིད་པ་བར་མ་དང་། །

[Block 1419]
འགྲུབ་པའོ། །

[Block 1420]
བཅོམ་ལྡན་འདས་ཀྱིས་སྲིད་པ་བར་མ་ནི་བརྗོད་པ་འདི་དག་གིས་གསུངས་སོ། །

[Block 1421]
ཡིད་ལས་བྱུང་བ་ནི་ཡིད་ཙམ་ལས་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 1422]
སྲིད་པ་ཚོལ་བའི༌[^533]ངང་ཚུལ་ཅན་ཡིན་པའི་ཕྱིར་སྲིད་པ་ཚོལ༌[^534]བའོ། །

[Block 1423]
དྲི་ཟ་བའི་ཕྱིར་ན་དྲི་ཟའོ། །

[Block 1424]
སྐྱེ་བ་ལ་མངོན་དུ་ཕྱོགས་པའི་ཕྱིར་མངོན་པར་འགྲུབ་པའོ། །

[Block 1425]
ཡང་ཅིའི་ཕྱིར་ཟས་བཞི་ཁོ་ན་ཡིན། ཟག་པ་དང་བཅས་པའི་ཆོས་ཐམས་ཅད་སྲིད་པ་རྣམས་གསོ་བར་བྱེད་པ་དག་མ་ཡིན་ནམ་ཞེ་ན། དེ་ནི་དེ་ལྟ་ཡིན་མོད་ཀྱི། འོན་ཀྱང་གཙོ་བོར་བཤད་དེ། འདི་ལ་གནས་དང་ནི།

[Block 1426 [VERSE]]
བརྟེན་པ་རྒྱས་པའི་དོན་དུ་གཉིས། །
སྲིད་གཞན་འཕེན་དང་འགྲུབ་པ་ཡི། །
དོན་དུ་གཉིས་ཏེ་གོ་རིམས་བཞིན། །

[Block 1427]
གནས་ནི་དབང་པོ་དང་བཅས་པའི་ལུས་སོ། །

[Block 1428]
དེ་རྒྱས་པར་བྱེད་པ་ནི་ཁམ་གྱི་ཟས་སོ། །

[Block 1429]
བརྟེན་པ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་སོ། །

[Block 1430]
དེ་རྒྱས་པར་བྱེད་པ་ནི་རེག་པ་སྟེ། རེ་ཞིག་འདི་གཉིས་ནི་འདིར་སྐྱེས་པའི་སྲིད་པ་གསོ་བར་བྱ་བ་ལ་གཙོ་བོ་ཡིན་ནོ། །

[Block 1431]
ཡིད་ལ་སེམས་པས་ནི་ཡང་སྲིད་པ་འཕེན་པར་བྱེད་དོ། །

[Block 1432]
འཕངས་ཟིན་པ་ལས་ཀྱིས་ཡོངས་སུ་བསྒོས་པའི༌[^535]རྣམ་པར་ཤེས་པའི་ས་བོན་ལས་མངོན་པར་འགྲུབ་པས་འདི་གཉིས་ནི་མ་སྐྱེས་པའི་སྲིད་པ་སྐྱེད་པ་ལ་གཙོ་བོ་ཡིན་ཏེ། དེའི་ཕྱིར༌[^536]བཞིར་གསུངས་སོ། །

[Block 1433 [HEADING]]
#### འཆི་འཕོ་དང་སྐྱེ་བ། ^3-1-9-0

[Block 1434]
ད་ནི་རྣམ་པར་ཤེས་པ་གང་ལ་གནས་ཏེ་འཆི་འཕོ་བ་དང་། སྐྱེ་བར་འགྱུར་བ་འདི་བརྗོད་པར་བྱ་སྟེ།

[Block 1435 [VERSE]]
ཆད་དང་མཚམས་སྦྱོར་འདོད་ཆགས་བྲལ། །
ཉམས་དང་འཆི་འཕོ་སྐྱེ་བ་རྣམས། །
ཡིད་ཀྱི་རྣམ་ཤེས་ཁོ་ནར་འདོད། །

[Block 1436]
ཅེས་བྱ་བ་སྨོས་ཏེ། དགེ་བའི་རྩ་བ་ཡང་དག་པར་ཆད་པ་དང་། དེའི་ཉིང་མཚམས་སྦྱོར་བ་དང་། ཁམས་དང་ས་ལས༌[^537]འདོད་ཆགས་དང་བྲལ་བ་དང་། ཡོངས་སུ་ཉམས་པ་དང་། འཆི་འཕོ་བ་དང་། སྐྱེ་བ་དང་། ཆོས་དྲུག་པོ་འདི་དག་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཁོ་ན་ཡིན་པར་འདོད་དོ། །

[Block 1437]
ཚོར་བ་ལས་ཀྱང་། འཆི་འཕོ་སྐྱེ་བ་བཏང་སྙོམས་ལ། །འཆི་འཕོ་བ་དང་སྐྱེ་བ་ནི་བཏང་སྙོམས་ལས་འབྱུང༌[^538]ངོ་། །ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དེ་ལ་ཡང་། རྩེ་གཅིག་སེམས་མེད་དེ་ལ་མེད། །སྐལ་བ་མི་མཉམ་པའི་ས་པ་ཡིན་པའི་ཕྱིར་དང་། མངོན་པར་འདུ་བྱེད་པ་ལས་བྱུང་བ་ཉིད་ཡིན་པའི་ཕྱིར་སེམས་རྩེ་གཅིག་པ་ལ་འཆི་འཕོ་བའམ་སྐྱེ་བ་མེད་དོ། །

[Block 1438]
སེམས་མེད་པ་ལ་ཡང་མེད་དེ། སེམས་མེད་པ་ལ་གནོད་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1439]
འཆི་བའི་སྲིད་པ་རྣམ་པ་གསུམ་དུ་བཤད་པ་ལ༌[^539]དགྲ་བཅོམ་པ་ནི། མྱ་ངན་འདས་ལུང་བསྟན་མིན་གཉིས། །སྤྱོད་ལམ་པའམ། རྣམ་པར་སྨིན་པའི་སེམས་ལས་ཏེ། །སེམས་འཆད་པའི་རྗེས་སུ་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1440]
ཡང་འཆི་བ་ན་ལུས་ཀྱི་ཕྱོགས་གང་དུ་རྣམ་པར་ཤེས་པ་འགག་ཅེ་ན། ཅིག་ཅར་འཆི་ན་ནི་ཡིད་དང་བཅས་པའི་ལུས་ཀྱི་དབང་པོ་མོད་ལ་འགག་པར་འགྱུར་རོ། །
--- END BLOCKS ---
