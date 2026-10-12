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
དབུ་མ་པ་ཞེས་བྱ་བས་གཟུང་བ་དང་འཛིན་པའི་རྣམ་པར་རྟོག་པ་དང་བྲལ་བ་འབའ་ཞིག་ཏུ་དྲི་མ་མེད་པའི་མཐའ་ཡས་པ་ནམ་མཁའ་དང་མཚུངས་པ། དངོས་པོ་ཐམས་ཅད་ཀྱི་དེ་ཁོ་ན་ཉིད་ཅེས་བྱ་བ་འདོད་དེ་རྣམ་པར་ཐར་པ་གསུམ་གྱིས་རྟོགས་པར༌[^987]བྱ་བའི་ཕྱིར་རོ། །

[Block 1402]
དེ་བས་ན་དངོས་པོ་ཐམས་ཅད་སྟོང་པ་ཉིད་དེ། གཅིག་དང་དུ་མས་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1403]
དབང་ཕྱུག་ལ་སོགས་པའི་རྒྱུ་མཚན་དང་བྲལ་བ་དངོས་པོ་རྣམས་ཡིན་ཏེ་དབང་ཕྱུག་ལ་སོགས་པ་དཔྱོད་པ་ན༌[^988]མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 1404]
དངོས་པོ་ཐམས་ཅད་སྨོན་པ་མེད་པ་ཡིན་ཏེ། སྨོན་པར་བྱ་བ་མ་གྲུབ་པས་སོ། །

[Block 1405]
འདི་ལ་སྦྱོར་བ་ནི་དངོས་པོ་ཐམས་ཅད་སྟོང་པ་ཡིན་ཏེ་གཅིག་དང་དུ་མས་བྲལ་བའི་ཕྱིར་གཟུགས་བརྙན༌[^989]བཞིན་ནོ། །

[Block 1406]
དེ་ལ་གལ་ཏེ། ཆོས་མཐུན་པའི་དཔེས་ངོ་བོ་མེད་པ་ཉིད་དམིགས་ན་དེ་བཞིན་དུ་ཡང་དེ་ཙམ་ལས་གཏན་ཚིགས་ཀྱི་འབྲེལ་པ་ངེས་སོ། །

[Block 1407]
རྗེས་སུ་འགྲོ་བ་ཉེ་བར་ལེན་པའི༌[^990]ལྡོག་པ་དོན་གྱིས་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 1408]
མཁས་པ་རྣམས་ཀྱིས་གཏན་ཚིགས་གཅིག་པུ་ཙམ་གྱིས་ངེས་པ་ཡིན་གྱི་ཡན་ལག་ལྔའམ་ཡན་ལག་གསུམ་གྱི་ཚིག་གི་སྦྱོར་བ༌[^991]བསྟན་མི་དགོས་སོ། །

[Block 1409 [VERSE]]
དེ་དངོས་དང་ནི་རྒྱུ་དངོས་དག །
དཔེ་ཡིས་དེ་ནི་མི་རིགས་ལ། །
སྨྲ་བ་ཡིན་གྱི༌[^992]མཁས་པ་ལ། །
གཏན་ཚིགས་གཅིག་པུ་སྨྲ་བ་ཡིན། །

[Block 1410]
དེའི་ཕྱིར་ཕྱོགས་དང་དཔེ་ལ་སོགས་པའི་ཚིག་རྒྱས་པ་སྤངས་ཏེ་རྗེས་སུ་འགྲོ་བ་ཙམ་གྱིས་ཁོ་བོ་ཅག་གི་སྟོང་པ་ཉིད་དུ་འགྲུབ་པོ། །གལ་ཏེ་གཅིག་དང་དུ་མས་བྲལ་བ་ཙམ་གྱིས་སྟོང་པ་ཉིད་ངེས་པར་བྱེད་ན། དེ་ཅིའི་ཕྱིར་བྱེ་བྲག་བཅོ་བརྒྱད་པའི་སྟོང་པ་ཉིད་གསུངས་ཤེ་ན། སྨྲས་པ་འདིར་ནི་གདོད་མ་ནས་མ་རིག་པའི་བག་ཆགས་ཀྱི་ཤུགས་ཀྱི་དབང་གིས་ཇི་སྲིད་རྣམ་པར་རྟོག་པ་དེ་དང་དེ༌[^993]དག་གི༌[^994]རྒྱུ་བ་སྤང་བའི་དོན་དུ་འབད་པ་བྱ་བ་ཡིན་ཏེ། ནང་སྟོང་པ་ཉིད་དང་། ཕྱི་སྟོང་པ་ཉིད་དང་། ཕྱི་ནང་སྟོང་པ་ཉིད་དང་། སྟོང་པ་ཉིད་སྟོང་པ་ཉིད་དང་། ཆེན་པོ་སྟོང་པ་ཉིད་དང་། དོན་དམ་པ་སྟོང་པ་ཉིད་དང་། འདུས་བྱས་སྟོང་པ་ཉིད་དང་། འདུས་མ་བྱས་སྟོང་པ་ཉིད་དང་། མཐའ་ལས་འདས་པ་སྟོང་པ་ཉིད་དང་། ཐོག་མ་དང་ཐ་མ་མེད་པ་སྟོང་པ་ཉིད་དང་། དོར་བ་མེད་པ་སྟོང་པ་ཉིད་དང་། རང་བཞིན་མེད་པ་སྟོང་པ༌[^995]ཉིད་དང་། ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་དང་། རང་གི་མཚན་ཉིད་སྟོང་པ་ཉིད་དང་། མི་དམིགས་པ་སྟོང་པ་ཉིད་དང་། ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་དང་། [^996]ངོ་བོ་མེད་པའི་རང་བཞིན་སྟོང་པ་ཉིད་དོ། །

[Block 1411]
ནང་གི་ཆོས་ནི་མིག་ལ་སོགས༌[^997]པ་ཉིད་ཀྱིས་སྟོང་པ་ཡིན་ནོ་ཞེས༌[^998]སྟོང་པ་ཉིད་དོ། །

[Block 1412]
ཕྱིའི་ཆོས་ནི་གཟུགས་ལ་སོགས་པ་སྟེ། དེ་དག་གཟུགས་ལ་སོགས་པ་སྟོང་པ་ཉིད་ཀྱིས་སྟོང་པ་ཞེས་ཕྱི་སྟོང་པ་ཉིད་དོ། །

[Block 1413]
ནང་དང་ཕྱིའི་ཆོས་ནི་ནང་དང་ཕྱིའི་ཆོས་ཉིད་ཀྱིས་སྟོང་པ་སྟེ་ཕྱི་ནང་སྟོང་པ་ཉིད་དོ། །

[Block 1414]
ཆོས་ཐམས་ཅད་ཀྱིས་སྟོང་པ་གང་ཡིན་པ་དེ་ཉིད་ཀྱིས་སྟོང་པ་ཡིན་ནོ་ཞེས་སྟོང་པ་ཉིད་ཀྱི༌[^999]སྟོང་པ་ཉིད་དོ། །

[Block 1415]
ཤར་ལ་སོགས་པའི་ཕྱོགས་རྣམས་ལ་ཤར་ལ་སོགས་པའི་ཕྱོགས་ཉིད་ཀྱིས་སྟོང་པ་ཡིན་ནོ་ཞེས་སྟོང་པ་ཆེན་པོའོ། །

[Block 1416]
དོན་དམ་པ་ནི་མྱ་ངན་ལས་འདས་པ་སྟེ། དེ་ཡང་མྱ་ངན་ལས་འདས་པ་སྟོང་པ་ཉིད་ཀྱིས་སྟོང་པ་ཡིན་ཞེས་དོན་དམ་པའི་སྟོང་པ་ཉིད་དོ། །

[Block 1417]
འདུས་བྱས་པ་ནི་ཁམས་གསུམ་སྟེ། འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་སོ། །

[Block 1418]
དེ་དེ་རྣམས་ཀྱིས་སྟོང་པ་ཡིན་ནོ་ཞེས་འདུས་བྱས་སྟོང་པ་ཉིད་དོ། །

[Block 1419]
སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དང་བྲལ་བ་ནི་འདུས་མ་བྱས་པ་སྟེ། དེ་དེ་ཉིད་ཀྱིས་སྟོང་པ༌[^1000]ནི་འདུས་མ་བྱས་ཀྱི་སྟོང་པ་ཉིད་དང་། རྟག་པ་དང་ཆད་པ་དག་ནི་མཐའོ། །

[Block 1420]
དེ་དག་ཉིད་ཀྱིས་སྟོང་པ་ནི་མཐའ་ལས་འདས་པ་སྟོང་པ་ཉིད་དོ། །

[Block 1421]
གང་ཐོག་མ་དང་མ་མེད་པ་དེ་ལ་བདེན་པའི་དངོས་པོ་མེད་དེ། འགྲོ་བ་དང་འོང་བ་མེད་ཅིང་ཐོག་མ་དང་བར༌[^1001]དང་མཐས་སྟོང་པའི་ཕྱིར་ཐོག་མ་དང་ཐ་མ་མེད་པའི་སྟོང་པ་ཉིད་དོ། །

[Block 1422]
དོར་བ་ནི་སྤང་བ༌[^1002]སྟེ་དེ་ལས་ལོག་པ་ནི་དོར་བ་མེད་པ་སྟེ། དེ་ཉིད་ཀྱིས་སྟོང་པས་ན༌[^1003]དོར་བ་མེད་པའི་སྟོང་པ་ཉིད་དོ། །

[Block 1423]
ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་གང་ཡིན་པ་དེ་ནི་སུས་ཀྱང་མ་བྱས་པ་དང་འདུས་མ་བྱས་པ་ཡང་མ་ཡིན་ཏེ། དེ་རང་བཞིན་གྱིས་སྟོང་པས་ན། རང་བཞིན་གྱིས་སྟོང་པའོ། །

[Block 1424]
ཆོས་ཐམས་ཅད་ནི་འདུས་བྱས་པ་དང་འདུས་མ་བྱས་པ་དེ་དག་དེ༌[^1004]ཉིད་ཀྱིས་སྟོང་པས་ན་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་དོ། །

[Block 1425]
ཆོས་ཐམས་ཅད་ནི་རང་རང་གི་གཟུགས་ལ་སོགས་པའི་མཚན་ཉིད་ཀྱིས་སྟོང་པས་ན་རང་གི་མཚན་ཉིད་སྟོང་པ་ཉིད་དོ། །

[Block 1426]
འདས་པ་དང་མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བ་ཉིད་ཀྱིས་སྟོང་པས་ན་མི་དམིགས་པ༌[^1005]སྟོང་པ་ཉིད་དོ། །

[Block 1427]
སྦྱོར་བ་ལས་བྱུང་བའི་ཆོས་ཀྱི་མཚན་ཉིད་མེད་དེ༌[^1006]རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1428]
སྦྱོར་བ་ནི་སྦྱོར་བ་ཉིད་ཀྱིས་སྟོང་པས་ན་ངོ་བོ་ཉིད་དོ། །

[Block 1429]
རང་བཞིན་གྱིས་སྟོང་པས་ན་རང་གི་ངོ་བོ་སྟོང་པ་ཉིད་དོ། །

[Block 1430]
དངོས་པོ་མེད་པའི་རང་བཞིན་དངོས་པོ་དེ་དེ་ཉིད་ཀྱིས་སྟོང་པས་ན་ངོ་བོ་མེད་པའི་རང་བཞིན་སྟོང་པ་ཉིད་དོ། །

[Block 1431]
དེའི་ཕྱིར་སྟོང་པ་ཉིད་བཅོ་བརྒྱད་བསྟན་ཏོ། །

[Block 1432]
དེ་བས་ན་རྣམ་པར༌[^1007]ཐར་པ་གསུམ་ཐོབ་པས་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་རྗེས་ཐོགས་ལ་ས་བཅུ་གཉིས་པ་ཀུན་ཏུ་འོད་ཀྱི་ས་ལ་བྱང་ཆུབ་སེམས་དཔས་བྱང་ཆུབ་ཐོབ་བོ་ཞེས་དེ་ཉིད་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཉིད་དོ། །

[Block 1433]
ཕྱོགས་དེར་ཉན་ཐོས་ལ་སོགས་པའི་འདོད་པའི་དངོས་པོའི་མངོན་པར་ཞེན་པ་མེད་དེ། དེ་རྣམས་ཀྱི་སྟོང་པ་ཉིད་མངོན་དུ་གྱུར་པ་ལ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 1434]
ཇི་སྐད་དུ།

[Block 1435 [VERSE]]
དངོས་པོ་གོས་དང་འདྲ་བ་རྣམས། །
རྣམ་པ་དུ་མས་ཐ་དད་པ། །
སྟོང་པ་ཉིད་ཀྱི་མེས་ཚིག་ན། །
ཐལ་བའི་དབྱེ་བ་གང་ཡང་མེད། །

[Block 1436 [VERSE]]
སྣོད་དང་སེམས་ཅན་ཞེས་བྱ་བའི། །
འཇིག་རྟེན་གཉིས་པོ་འདི་བསྲེགས་ནས། །
དེ་ཡང་རང་ཉིད་དེ་ཉིད་དུ། །
མེ་སྒྲོན་བཞིན་དུ་ཞི་བར་འགྱུར། །

[Block 1437]
ཞེས་འབྱུང་ངོ་། །སྔོན་གྱི་སྨོན་ལམ་དང་སྙིང་རྗེ་ཆེན་པོས༌[^1008]བསྐུལ་བས་སེམས་ཅན་གྱི་དོན་འགྲུབ་པ་ཡིན་པས་ཆད་པའི་ཕྱོགས་མེད་དོ། །

[Block 1438]
སྤྲོས་པ་ཐམས་ཅད་དང་བྲལ་བའི་ཏིང་ངེ་འཛིན་ལ་རྟག་ཏུ་གཞོལ་བས་རྟག་པ་ཡང་མེད་དོ་ཞེས་སྟོང་པ་ཉིད་སྨྲ་བ་ཐེག་པ་ཆེན་པོ་པ༌[^1009]བདག་ཅག་རྣམས་ཀྱི་ཞི་གནས་དང་ལྷག་མཐོང་གི་བདག་ཉིད་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གྱི༌[^1010]ཕྱོགས་སོ། །

[Block 1439]
འོ་ན་མངོན་པར་འདུས་མ་བྱས་པའི་རྣམ་པར་ཐར་པ་ཡང་ཡོད་དེ་དེ་ཅིའི་ཕྱིར་མ་བསྟན༌[^1011]ཞེ་ན། དེ་ནི་ཡོད་པ་བདེན་ཏེ། འོན་ཀྱང་གསུམ་པ་ལ་གོམས་པས་འབད་པ་མེད་པར་ལྷུན་གྱིས་གྲུབ་པ་ཡིན་ཏེ་ཆུ་ཐིགས་བཞིན་ནོ། །

[Block 1440]
དེ་བས་དེ་ནི་བྱང་ཆུབ་ཀྱི་རྒྱུ་ཡིན་ཡང་ཤིན་ཏུ་ཉེ་བའི་ཕྱིར་འབྲས་བུ་ཡང་ཡིན་པ་ལ་སྐྱོན་གང་ཡང་མེད་དོ། །
--- END BLOCKS ---
