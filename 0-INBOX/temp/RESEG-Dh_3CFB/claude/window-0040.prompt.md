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
དེ་ཡང་ཡུལ་འདི་ལ༌[^1065]ཚད་མར་མཚུངས་སོ། །

[Block 1402]
མེད་པར་ངེས་པའི་འབྲས་བུ་ཅན་དེ་ཡང་ཡོད་པ་ཉིད་མ་ཡིན་དུ་ཟིན་ཀྱང་འདི་ཚད་མ་ཉིད་ཡིན་ཏེ། གང་དམིགས་སུ་རུང་བ་རྒྱུ་གཞན་ཚོགས་པ་དག་ཡོད་ན་མི་དམིགས་པ་སྲིད་པ་མ་ཡིན་ནོ། །

[Block 1403]
སྔ་མ་ནི་མེད་པ་ཉིད་སྒྲུབ་པར་བྱེད་པ་ཡང་མ་ཡིན་ཏེ།

[Block 1404 [VERSE]]
བསྟན་བཅོས་སྐབས་དང་འབྲེལ་མེད་དང་། །
དབང་པོ་ལས་འདས་རྟགས་ཅན་མིན། །
དོན་རྣམས་མང་པོ་དེ་དག་ནི། །
ཇི་ལྟར་མི་དམིགས་ཕྱིར་ན་མེད། །

[Block 1405]
དེ་མེད་པ་ཉིད་སྒྲུབ་པར་བྱེད་པ་ནི༌[^1066]མི་དམིགས་པ་ཙམ་གྱིས་དོན་ཐམས་ཅད་ལ་ཚད་མ་གསུམ་ལྡོག་པས་བསྒྲུབ་པར༌[^1067]འགྱུར་གྲང༌[^1068]ན། དེ་ལ་བསྟན་བཅོས་ལྡོག་པ་ནི་མེད་པ་ཉིད་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ནི་སྐབས་འགའ་ཞིག་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 1406]
བསྟན་བཅོས་འཇུག་པར་བྱེད་པ་ནི་སྐྱེས་བུའི་དོན་འགྲུབ་པར་བྱེད་པའི་ཐབས་འགའ་ཞིག་ལ་བརྟེན་ནས་འཇུག་པར་འགྱུར་ཏེ། གཞན་དུ་ན་འབྲེལ་པ་མེད་པའི་བརྗོད་པ་ནི་ཚད་མར་མི་འགྱུར་བའི༌[^1069]ཕྱིར་རོ། །

[Block 1407]
སྐབས་དེ་ལ་ཡང་དོན་མང་པོ་དག་གདོན་མི་ཟ་བར་བསྟན་པར་བྱ་བ་མ་ཡིན་ཏེ། དཔེར་ན་སོ་སོར་ངེས་པའི་བདག་ཉིད་ཀྱིས་སྐྱེས་བུའི་སེམས་འགའ་ཞིག་ངེས་པའི་རྒྱུ་མཚན་འབྱུང་བ་མ་ཡིན་པ་ཅན་འཇུག་པའམ། ཡུལ་དང་དུས་ཀྱིས་ཆོད་པའི་སྐབས་ལ་ཉེ་བར་མཁོ་བ་མེད་པའི་རྫས་ཀྱི་བྱེ་བྲག་ལྟ་བུའོ། །

[Block 1408]
དེ་བསྟན་བཅོས་ཀྱི་ཡུལ་དུ་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1409]
དེ་ལྟར་ན༌[^1070]བསྐལ་པ་དག་ལ་རང་གི་ནུས་པ་ཉེ་བའི་ཕྱིར་ཤེས་པ་བསྐྱེད༌[^1071]ནུས་པ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1410]
དེ་དག་གི༌[^1072]གདོན་མི་ཟ་བར་འབྲས་བུ་དམིགས་པ་ཡང་མེད་ན་གང་གི་རྗེས་སུ་དཔག་པར་བྱེད། དེ་དག་ནི་ཚད་མ་གསུམ་ལོག་ཏུ་ཟིན་ཀྱང་མེད་དོ་ཞེས་ངེས་པར་ནུས་པ་མ་ཡིན་ནོ། །

[Block 1411]
དེ་བས་མི་དམིགས་པ་ཐམས་ཅད་ནི་ལྡོག་པ་ངེས་པར་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1412]
དེ་བས་ན་འདི་ནི།

[Block 1413 [VERSE]]
ཡོད་མེད་ངེས་པའི་འབྲས་ཅན་མིན། །
ཕྱིར་ནའང་ཚད་མ་ཉིད་མིན་འགྱུར། །

[Block 1414]
མི་དམིགས་པ་འདི་ནི་ཚད་མ་ཉིད་མ་ཡིན་ཏེ། ཚད་མ་དག་ནི་ངེས་པའི་འབྲས་བུ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1415]
འདི་འཇུག་པ་འགོག་པ་ཡིན་ཡང་སེམས་ལ་ཐེ་ཚོམ་ཡོངས་སུ་གཅོད་པ་ཅན༌[^1073]མ་ཡིན་ཏེ། ཐེ་ཚོམ་ལས་ཀྱང་འགའ་ཞིག་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 1416]
གལ་ཏེ་ངེས་པ་སྔོན་དུ་འགྲོ་བའི་ཐ་སྙད་དུ་བྱེད་པ་ཅན་ནི་དེ་བཞིན་ཁོ་ན་ལ་དེ་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ནི། མི་འཇུག་འབྲས་བུ་ཅན་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1417 [VERSE]]
རྟགས་ཀྱི་ཕུལ་བྱུང་ཡོད་པ་ཅན། །
ལ་ལ་ཚད་མ་དག་ཏུའང་འགྱུར། །

[Block 1418]
འདིར་མི་དམིགས་པ་ཐམས་ཅད་ནི་ཚད་མ་མ་ཡིན་ལ། རྟགས་ཀྱི་ཁྱད་པར་ལས་ཡོད་པ་ཅན་ལ་ལ་ཚད་མ་ཡང་ཡིན་ཏེ། ཇི་ལྟར་གོང་དུ་དཔེར་བྱས་པ་ལྟ་བུའོ། །

[Block 1419]
གང་ཡང་མི་དམིགས་པ་ནི་ཚད་མ་མ་ཡིན་ནོ་ཞེས་དེ་བཤད་ཅེ་ན།

[Block 1420 [VERSE]]
རང་བཞིན་ཤེས་བྱེད་མི་ཤེས་ལ། །
རིགས་པ་འདི་ནི་བརྗོད་པ་ཡིན། །

[Block 1421]
གང་འགའ་ཞིག་གི༌[^1074]རང་གི་ངོ་བོ་ཡུལ་ལ་སོགས་པས་བསྐལ་པའི་ཕྱིར། མི་དམིགས་པས་དེ་ནི་མི་དམིགས་པ་ཙམ་གྱིས་མེད་པ་ཞེས་བྱ་བ་མ་ཡིན་ཏེ། གོང་དུ་ཇི་སྐད་བཤད་པ་ལྟ་བུའོ། །ཤེས་པར་བྱེད་པ་རྟགས་ལ་མེད་པའི་ཕྱིར། དབང་པོ་ལས་འདས་པའི་དོན་གང་ཡིན་པ་འམ། རང་བཞིན་གྱི་ཁྱད་པར་སྤོང་བར་བྱེད་དེ། དཔེར་ན་སེམས་འདོད་ཆགས་དང་བྲལ་བ་འམ། ལྷ་ཉིད་ཀྱི་ཁྱད་པར་མེད་པ་འམ། སྦྱིན་པ་དང་འཚེ་བ་ལ་སོགས་པ་ལས་ལྡོག་པ་སེམས་ལ་མངོན་པར་མཐོ་བ་དང་། ངེས་པར་ལེགས་པའི་རྒྱུ་ཉིད་མེད་དོ་ཞེས་བྱ་བ་དང་། མངོན་སུམ་གྱི་དོན་ལ་ནི་འབྲས་བུ་དེ་མ་ཐག་པ་མེད་པའི་ཕྱིར། དེའི་འབྲས་བུ་མེད་པ་ཅན་དང་། ཆོས་མཐུན་པའི་ཕྱིར་ཕྱིན་ཅི་ལོག་པས་སྐུར་བར་བྱེད་ན་ཡང་། དེ་ཙམ་གྱིས་ནི་འབྲས་བུ་ཆོད་པ་དག་ཀྱང་རྒྱུ་ལས་སྐྱེ་བ་མཐོང་བའི་ཕྱིར་དེ་མེད་པ་ཉིད་མ་ཡིན་ཏེ། བྱི་བ་དང་ཁྱི་སྨྱོན་པའི་དུག་གི་འགྱུར་བ་བཞིན་ནོ། །

[Block 1422]
དེ་འབྱུང་བ་ལ་འགལ་བ་མེད་པའི་ཕྱིར་འདི་ལ་མི་དམིགས་པ་ཙམ་ནི་ཚད་མ་མ་ཡིན་ནོ། །

[Block 1423]
གལ་ཏེ་ཡོད་པ་ལ་གང་ཚད་མ་ཡིན་ཞེ་ན། དེ་ཉིད་ཀྱི་ཕྱིར་ཐེ་ཚོམ་ཟ་བ་ཡིན་ཡང་བླ་སྟེ། ཚད་མ་ཡང་སྲིད་པའི་ཕྱིར་མི༌[^1075]སྤོང་ངོ་། །དེ་བས་ན་འདིར་དོན་ནམ༌[^1076]རང་གི་ངོ་བོ་འགའ་ཞིག་ལ་མཐོང་བ་གསལ་བ་མེད་པའི་ཕྱིར་དང་། རྒྱུ་རྣམས་ནི་འབྲས་བུ་བསྐྱེད་པར་ངེས་པ་མེད་པའི་ཕྱིར། ཤེས་པར་བྱེད་པ་མ་འགྲུབ་པའི༌[^1077]འགྱུར་རོ། །

[Block 1424]
འདི་ཙམ་གྱིས་ནི་དེ་མེད་པ་མ་ཡིན་ཏེ། ཡང་ཚུལ་གཞན་དུ་འགའ་ཞིག་མངོན་པར་གསལ་བའི་ཕྱིར་རོ། །

[Block 1425 [VERSE]]
རྒྱུ་མི་ཤེས་པ་འབྲས་བུ་ཡིས། །
མེད་པ་ཉིད་ཀྱིས༌[^1078]སྒྲུབ་བྱེད་དང་། །

[Block 1426]
རང་གི་ངོ་བོ་མེད་པར་བསྒྲུབ་པར་བྱ་བ་ལ། དེ་མི་དམིགས་པ་ཉིད་ནི་ཚད་མར་མི་བརྗོད་ཀྱི་རྒྱུ་མི་དམིགས་པ་ཚད་མ་ཁོ་ན་ཡིན་ནོ། །

[Block 1427]
གང་རྒྱུ་མེད་པ་ལ་འབྲས་བུ་འགྱུར་བ་སྲིད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1428]
ལ་ལར་རྒྱུ་ཞིག་ན་ཡང་འབྲས་བུ་གནས་པར་མཐོང་བ་མ་ཡིན་ནམ། རྒྱུ་གནས་པའི་དུས་ན་འབྲས་བུ་ཡོད་དོ་ཞེས་ནི་མི་སྨྲའོ། །

[Block 1429]
དངོས་པོ་དེ་ལྟར་གནས་པ་ཅན་ནི་དེའི་རྒྱུ་ཅན་ནི་མ་ཡིན་གྱི་བརྒྱུད་པས་རྒྱུན་ལ་ཕན་འདོགས་པར་བྱེད་པའི་ཕྱིར། དེའི་འབྲས་བུ་བསྟན་ཅིང་རྒྱུ་མེད་པར་དངོས་པོ་སྐྱེ་བ་ནི་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 1430]
གལ་ཏེ་འདི་རྣམ་པ་འགའ་ཞིག་གིས་མེད་པ་གྲུབ་པར་འགྱུར་ན་དེའི་འབྲས་བུ་མེད་དོ་ཞེས་ངེས་པར་འགྱུར་རོ། །

[Block 1431 [VERSE]]
དོན་གྱི་རང་བཞིན་རྟགས་ཅན་ལ། །
རང་བཞིན་མི་དམིགས་པ་ཡང་མིན། །

[Block 1432]
རང་བཞིན་ཉིད་ཀྱི་རྟགས་ཅན་ལ་རང་བཞིན་མི་དམིགས་པ་འགའ་ཞིག་ཀྱང་ཚད་མ་ཁོ་ན་ཡིན་ནོ། །

[Block 1433]
གལ་ཏེ་ཁྱབ་པར་བྱེད་པ་མི་དམིགས་པ་ནི་འདིའི་རང་བཞིན་གྲུབ་པར་འགྱུར་ཏེ། དཔེར་ན་ཤིང་ཤ་པ་ལ་ཤིང་ཉིད་ལྟ་བུའོ། །

[Block 1434 [VERSE]]
གལ་ཏེ་གཏན་ཚིགས་འགའ་ཞིག་གིས། །
དེ་མེད་པར་ནི་རྟོགས་པར་འགྱུར། །

[Block 1435]
གལ་ཏེ་རྒྱུ་འམ་ཁྱབ་པར་བྱེད་པའི་རང་བཞིན་འདི་གོ་བར་བྱེད་པ་གཏན་ཚིགས་གང་ཞིག་ལས་མེད་པར་འགྲུབ་པར༌[^1079]འགྱུར་བ་དེ་མེད་པ་ཉིད་ཀྱིས་རང་གི་འབྲས་བུ་འམ་ཁྱབ་པར་བྱ་བ་ལྡོག་པར་བྱེད་དེ། དེ་མེད་པར་མ་གྲུབ་ན་ནི་ལྡོག་པ་ལ་ཡང་ཐེ་ཚོམ་ཟ་བའི་ཕྱིར་རོ། །

[Block 1436]
ཇི་ལྟར་ན་དངོས་པོའི་བདག་ཉིད་མི་དམིགས་པ་ལས་མེད་པ་གྲུབ་ཅེ་ན། མཐོང་བ་མེད་པ་དག་གི་རྒྱུ། །མི་སྲིད་པར་ནི་གྱུར་པ་ནི།[^1080] །

[Block 1437 [VERSE]]
སྣང་བའི་དངོས་པོ་མི་དམིགས་པའི། །
དངོས་པོ་མེད་པ་རྟོགས་པར་འགྱུར། །

[Block 1438]
གལ་ཏེ་དངོས་པོར་འགྱུར་ན་བདག་ཉིད་ཇི་ལྟ་བུ་འཛིན་པ་པོའི་བྱེད་པས་དམིགས་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1439]
དེ་མཐོང་བའི་གེགས་བྱེད་པ་ཅན་བར་ཆད་ལ་སོགས་པ་དག་མེད་ན་དམིགས་པ་ཁོ་ནར་འགྱུར༌[^1081]ལ། མི་དམིགས་ན་ནི་མེད་པ་ངེས་པར་འགྱུར་ཏེ། དེ་འདྲ་བར་འགྱུར་བ༌[^1082]དམིགས་པ་ལ་འཁྲུལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1440]
གཏན་ཚིགས་འདི་ཉིད་ནི་རྒྱུ་དང་ཁྱབ་པར་བྱེད་པ་དག་མེད་པ་ལ་རིག་པར་བྱའོ། །
--- END BLOCKS ---
