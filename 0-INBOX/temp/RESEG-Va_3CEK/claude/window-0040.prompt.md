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
[Block 1401 [HEADING]]
### ཕྲ་རྒྱས་དགུ་བཅུ་རྩ་བརྒྱད། ^2-6-0

[Block 1402]
ཡང་ཆོས་མངོན་པ་ལས་ཕྲ་རྒྱས་བཅུ་པོ་དེ་དག་ལས་འདོད་པ་ན་སྤྱོད་པ་སུམ་ཅུ་རྩ་དྲུག་དང་། གཟུགས་ན་སྤྱོད་པ་སུམ་ཅུ་རྩ་གཅིག་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ་སུམ་ཅུ་རྩ་གཅིག་སྟེ། དགུ་བཅུ་རྩ་བརྒྱད་དུ་ཡང་འཆད་དོ། །ཇི་ལྟར་བྱས་པས་ཤེ་ན། ཕྲ་རྒྱས་དེ་དག་ནི་མདོར་བསྡུ་ན་ཁམས་གསུམ་པའི་མཐོང་བས་སྤང་བར་བྱ་བ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 1403 [HEADING]]
#### འདོད་པ་ན་སྤྱོད་པ། ^2-6-1-0

[Block 1404]
དེ་ལ་རེ་ཞིག་འདོད་པའི་ཁམས་ན་སྤྱོད་པ་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་སུམ་ཅུ་རྩ་གཉིས་སོ། །

[Block 1405]
དེ་དག་གང་ཞེ་ན། དེ་དག་བཅུ་དང་བདུན་བདུན་བརྒྱད། །ལྟ་བ་གསུམ་གཉིས་མ་གཏོགས་པར།[^991] །

[Block 1406 [VERSE]]
འདོད་ན་སྡུག་བསྔལ་ལ་སོགས་པ། །
མཐོང་བས་རིམ་བཞིན་སྤོང་བར་བྱེད། །

[Block 1407]
ཞེས་བྱ་བ༌[^992]སྨོས་ཏེ། ཕྲ་རྒྱས་བཅུར་བཤད་པ་གང་དག་ཡིན་པ་དེ་དག་འདོད་པའི་ཁམས་ན་སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་བཅུ༌[^993]ཡོད་དོ། །

[Block 1408]
དེ་དག་ཉིད་ལ་ཀུན་འབྱུང་འགོག་པ༌[^994]མཐོང་བས་སྤང་བར་བྱ་བ་བདུན་དང་། འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བ་བདུན་ཏེ། འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། མཐར་འཛིན་པར་ལྟ་བ་དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་མ་གཏོགས་སོ། །

[Block 1409]
ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་བརྒྱད་དེ། འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། མཐར་འཛིན་པར་ལྟ་བ་མ་གཏོགས་སོ། །

[Block 1410]
དེ་ལྟར་ན་ཕྲ་རྒྱས་སུམ་ཅུ་རྩ་གཉིས་སོ། །

[Block 1411]
[^995]དེ་དག་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་དག་ཡིན་ཏེ། བདེན་པ་རྣམས་མཐོང་བ་ཙམ་གྱིས་སྤོང་བའི་ཕྱིར་རོ། །

[Block 1412]
བཞི་ནི་བསྒོམ་པས་སྤང་བྱ་ཡིན། །འདི་ལྟ་སྟེ། འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། མ་རིག་པ་དང་། ང་རྒྱལ་དང་། [^996]བདེན་པ་མཐོང་བས་ཕྱིས་ལམ་གོམས་པར་བྱས་པས་སྤོང་བའི་ཕྱིར་རོ། །

[Block 1413]
དེ་ལྟར་ན༌[^997]འཇིག་ཚོགས་ལ་ལྟ་བ་ནི་རྣམ་པ་གཅིག་སྟེ། སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་ལ། མཐར་འཛིན་པར་ལྟ་བ་ཡང་དེ་དང་འདྲའོ། །

[Block 1414]
ལོག་པར་ལྟ་བ་ནི་རྣམ་པ་བཞི་སྟེ། སྡུག་བསྔལ་བ༌[^998]དང་། ཀུན་འབྱུང་བ༌[^999]དང་། འགོག་པ་དང་། ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་ལ། ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་དང་། ཐེ་ཚོམ་ཡང་དེ་དང་འདྲའོ། །

[Block 1415]
ཚུལ་ཁྲིམས་དང་། བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ནི་རྣམ་པ་གཉིས་ཏེ། སྡུག་བསྔལ་དང་། ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1416]
འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་རྣམས་ནི་རྣམ་པ་ལྔ་སྟེ། བདེན་པ་བཞི་མཐོང་བས་སྤང་བར་བྱ་བ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1417]
སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་དེ་དག་ནི་ཅི་ལྟ་བུ་ཡིན། བསྒོམ་པས་སྤང་བར་བྱ་བའི༌[^1000]བར་དུ་ནི་ཇི་ལྟ་བུ་ཡིན༌[^1001]ཞེ་ན། གང་དག་གང་ཞིག་མཐོང་བས་སྤང་བར་བྱ་བའི་དམིགས་པ་ཅན་དེ་དག་ནི་དེ༌[^1002]མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་ལ་ལྷག་མ་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 1418]
དེ་དག་ལ་ལྟ་བ་ནི་བཅུ་གཉིས་ཡིན་ནོ། །

[Block 1419]
ཐེ་ཚོམ་ནི་བཞི་ཡིན་ནོ། །

[Block 1420]
འདོད་ཆགས་ནི་ལྔ་ཡིན་ནོ། །

[Block 1421]
ཁོང་ཁྲོ་བ་ནི་ལྔ་ཡིན་ནོ། །

[Block 1422]
ང་རྒྱལ་ནི་ལྔ་ཡིན༌[^1003]ནོ། །

[Block 1423]
མ་རིག་པ་རྣམས༌[^1004]ནི་ལྔ་ཡིན་ཏེ། དེ་ལྟར་ན་ཕྲ་རྒྱས་སུམ་ཅུ་རྩ་དྲུག་པོ་དེ་དག་ནི་འདོད་པ་ན་སྤྱོད་པ་ཡིན་ནོ། །

[Block 1424 [HEADING]]
#### གཟུགས་ན་སྤྱོད་པ། ^2-6-2-0

[Block 1425]
ཁོང་ཁྲོ་མ་གཏོགས་དེ་དག་ཉིད། །གཟུགས་ཁམས། ཁོང་ཁྲོ་བ་ལྔ་བོར་ནས་གཟུགས་ན་སྤྱོད་པའི་ཕྲ་རྒྱས་སུམ་ཅུ་རྩ་གཅིག་པོ་དེ་དག་ཉིད་ཡིན་ནོ། །

[Block 1426 [HEADING]]
#### གཟུགས་མེད་པ་ན་སྤྱོད་པ། ^2-6-3-0

[Block 1427]
གཟུགས་ཀྱི༌[^1005]ཁམས་ན་ཇི་ལྟ་བར་གཟུགས་མེད་པ་ཡང༌[^1006]དེ་དང་འདྲ།

[Block 1428 [VERSE]]
ཕྲ་རྒྱས་སུམ་ཅུ་རྩ་གཅིག་སྟེ། །
[^1007]དེ་ལྟར་དགུ་བཅུ་རྩ་བརྒྱད༌[^1008]འདོད། །

[Block 1429]
དེ་ལྟར་ན་ཆོས་མངོན་པ༌[^1009]དག་ན་རེ་ཕྲ་རྒྱས་དྲུག་པོ་དེ་དག་རྣམ་པ་དང་། བྱེ་བྲག་དང་ཁམས་ཀྱི་དབྱེ་བས་དགུ་བཅུ་རྩ་བརྒྱད་དུ་འདོད་དོ། །

[Block 1430 [HEADING]]
### མཐོང་བ་ཁོ་ནས་སྤོང་བ། ^2-7-0

[Block 1431]
ཅི་མཐོང་སྟེ་སྤང་བར་བྱ་བའི་ཆོས༌[^1010]ཕྲ་རྒྱས་སུ་བཤད་པ་གང་དག་ཡིན་པ་དེ་དག་ངེས་པར་མཐོང་བ་ཁོ་ནས་སྤོང་ངམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 1432]
འོ་ན་ཅི་ལྟ་བུ༌[^1011]ཞེ་ན།

[Block 1433 [VERSE]]
སྲིད་རྩེ་ལས་སྐྱེས་བཟོད་པ་ཡིས། །
གཞོམ་བྱ་མཐོང་བས་སྤང་བྱ་ཉིད། །

[Block 1434]
སྲིད་པའི་རྩེ་མོའི་ས༌[^1012]ལས་སྐྱེས་པའི་ཕྲ་རྒྱས་གང་དག་རྗེས་སུ་ཤེས་པའི་བཟོད་པས་གཞོམ་པར་བྱ་བ་དེ་དག་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་ཁོ་ན་ཡིན་གྱི་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ནི་མ་ཡིན་ནོ། །

[Block 1435]
ལྷག་སྐྱེས་མཐོང་དང་བསྒོམ་གཉིས་ཀྱིས། །བཟོད་པས་གཞོམ་པར་བྱ་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ས་ལྷག་མ་དག་ན་ཆོས་དང་རྗེས་སུ་ཤེས་པའི་བཟོད་པ༌[^1013]སྤང་བར་བྱ་བའི་ཕྲ་རྒྱས་ཡོད་པ་རྣམས་ནི་ཅི་རིགས་པར་འཕགས་པ་རྣམས་ཀྱིས་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་ལ། སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱིས་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 1436]
བཟོད་པས་གཞོམ་མིན་བསྒོམ་ཁོ་ནས། །ས་ཐམས་ཅད་ན་ཕྲ་རྒྱས་གང་དག་ཤེས་པས་གཞོམ་པར༌[^1014]བྱ་བ་ཡོད་པ་དེ་དག་ནི་གཉི་གའི་ཡང་རྟག་ཏུ་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1437]
གཞན་དག་ན་རེ་ཕྱི་རོལ་པ་རྣམས་ཀྱིས་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ནི༌[^1015]སྤོང་བ་ཁོ་ན་སྟེ། འདི་ལྟར་ལས་རྣམ་པར་འབྱེད་པ་ཆེན་པོའི༌[^1016]མདོ་དང་སྔོན་གྱི་མཐའ་ལས༌[^1017]རྟོག་པ་སྤོང་བ༌[^1018]རྣམས་ལས་རྟག་པར་སྨྲ་བ་རྣམས་དང་། ལ་ལ་རྟག་པར་སྨྲ་བ་རྣམས་དང་། རྒྱུ་མེད་པ་ལས་ཀུན་དུ་འབྱུང་བར་སྨྲ་བ་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ལ༌[^1019]འདོད་པའི་ཁམས་ལས་དམིགས་པའི་ལྟ་བ་ཀུན་དུ༌[^1020]འབྱུང་བར་གསུངས་ཏེ། གཟུགས་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་རྣམས་འདོད་པའི་ཁམས་ལ་དམིགས་པ་ནི་མ་ཡིན་ཏེ། འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1438]
དེ་ལྟ་བས་ན་འདོད་པ་དང་ལྡན་པ་དེ་དག་ཁོ་ན་མ་སྤངས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1439]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་དེ་དག་ཀྱང༌[^1021]ལྟ་བ་བསྐྱེད་པ༌[^1022]དང་དུས་མཉམ་དུ་ཡོངས་སུ་ཉམས་པའི་ཕྱིར་ཏེ། ལྷ་སྦྱིན་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1440 [HEADING]]
### ལྟ་བ་ལྔའི་རང་གི་ངོ་བོ། ^2-8-0
--- END BLOCKS ---
