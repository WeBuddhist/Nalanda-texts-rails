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
[Block 1296]
ཏིང་ངེ་འཛིན་དང་གཟུངས་ཀྱི་སྒོ་རྣམས་ནི་ཆར་གྱི་ཆུ་ལྟ་བུའོ། །

[Block 1297]
དེ་ཡང་ཡེ་ཤེས་དེའི་ཁོང་ན་གནས་པ༌[^839]སྟེ། འདི་ལྟར་ནམ་མཁའ་སྤྲིན་གྱིས་ཁེབས་པར་བྱས་ནས་གནས་པ་ལྟར་འདྲེས་པའི་ཆོས་ལ་དམིགས་པའི་ཡེ་ཤེས་ཀྱིས་ཀྱང་སྒྲིབ་པ་རྒྱ་ཆེན་པོ་རྣམས་མི་མངོན་པར་བྱེད་དོ། །

[Block 1298]
ཆོས་ཀྱི་སྐུ་ཡོངས་སུ་རྫོགས་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྤྲིན་གྱིས༌[^840]ནམ་མཁའ་རྒྱས་པར་འགེངས་པ་ལྟར་ཆོས་ཀྱི་སྐུས་བྱང་ཆུབ་སེམས་དཔའི་རྟེན་ལ་རྒྱས་པར་འགེངས་སོ། །

[Block 1299]
འདིར་འགེངས་པ་ནི་སྤྲོས་པའོ། །

[Block 1300]
འགྲུབ་པས་ཐོབ་པ༌[^841]ནི་ཞེས་བྱ་བ་ནི་གང་གིས་ས་འདི་རྣམས་བསྒོམ་པ༌[^842]ལས་མཐར་ཕྱིན་པར་འགྱུར་བའོ་ཞེས་བལྟ་བར་བྱའོ། །

[Block 1301 [HEADING]]
### ས་འདི་དག་རེ་རེ་ཞིང་བསྒོམ་པ། ^5-3-0

[Block 1302]
ཇི་ལྟར་ས་འདི་དག་རེ་རེ་ཞིང་བསྒོམ་པ་སྒོམ་པར་འགྱུར་བ་དེ་བསྟན་པར་བྱ་བ་ནི་ས༌[^843]རྣམ་པ་ལྔ་སྟེ། ཡང་དེ་ནི་ཞི་གནས་དང་ལྷག་མཐོང་དག་བསྒོམ་པ་ན་དེ་དག་གཉི་ག་ཡང་རྣམ་པ་ལྔས་བསྒོམས་ཏེ། སྐད་ཅིག་རེ་རེ་ལ་གནས་ངན་ལེན་གྱི་གནས་སྐབས་ཐམས་ཅད་འཇིག་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་གནས་ངན་ལེན་ཞེས་བྱ་བ་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པའི་ས་བོན་ཐོག་མ་མེད་པའི་དུས་ཅན་གྱི་བག་ཆགས་ཞེས་བྱ་བ་སྟེ། སྒྲིབ་པ་དེའི་ཚོགས་དེ་ནི་འདྲེས་པའི་ཆོས་ལ་དམིགས་པའི་ཞི་གནས་དང་ལྷག་མཐོང་གི་ཡེ་ཤེས་ཀྱི་སྐད་ཅིག་རེ་རེ་ལ་སྟོབས་ཆུང་བར་བྱེད་པའམ། ཚོགས་འཇིག་པར་བྱེད་པ་ནི༌[^844]འདིར་འཇིག་པར་བྱེད་པར་བཞེད་དོ། །

[Block 1303]
ཡང་སྟོབས་ཆུང་བར་བྱེད་པ་ནི་འཇིག་པར་བྱེད་པའོ། །

[Block 1304]
སྣ་ཚོགས་ཀྱི་འདུ་ཤེས་དང་བྲལ་བ་སྟེ། ཆོས་ཀྱི་ཀུན་དགའ་ལ་དགའ་བ་ཐོབ་པ༌[^845]དང་ཞེས་བྱ་བ་ལ༌[^846]ཕྱོགས་བཅུར་རྣམ་པ་ཡོངས་སུ་མ་ཆད་པའི་ཆོས་ཀྱི་སྣང་བ་རབ་ཏུ་ཤེས་པ་སྟེ། གཞུང་ཁ་ཏོན་ལེགས་པར་བྱང་བ༌[^847]བཞིན་ནོ། །

[Block 1305]
རྣམ་པར་དག་པའི་ཆ་དང་མཐུན་པའི་མཚན་མ་རྣམ་པར་བརྟགས་པ་མ་ཡིན་པ་རྣམས་དེ་ལ་ཀུན་ཏུ་འབྱུང་བ་ཞེས་བྱ་བ་ལ་དགོས་པ་ཡོངས་སུ་གྲུབ་པ་དང་རབ་ཏུ་ལྡན་པ་ནི་འདིའི་རྣམ་པར་དག་པའི་ཆ་དང་མཐུན་པའི་མཚན་མ་རྣམ་པར་བརྟགས་པ་མ་ཡིན་པ་རྣམས་དེ་ལ་ཀུན་ཏུ་འབྱུང་བ་སྟེ། འདིར་སངས་རྒྱས་ཉིད་ནི་དགོངས་པ་ཡོངས་སུ་རྫོགས་པའོ་ཞེས་འདོད་དོ། །

[Block 1306]
ཆོས་ཀྱི་སྐུ་ཡོངས་སུ་རྫོགས་པ་དང་ཡོངས་སུ་གྲུབ་པར་བྱ་བའི་ཕྱིར་གོང་མ་བས་ཆེས་གོང་མའི་རྒྱུ་ཡོངས་སུ་འཛིན་པར་བྱེད་ཅེས་བྱ་བ་ནི་དེ་ལ་ཡོངས་སུ་རྫོགས་པ་ནི་ས་བཅུ་པའོ།[^848] །ཡོངས་སུ་གྲུབ་པ་ནི་བཅུ་གཅིག་པ་སངས་རྒྱས་ཀྱི་ས་ལ་ཆོས་ཀྱི་སྐུ་ཡོངས་སུ་གྲུབ༌[^849]པའོ། །

[Block 1307]
གོང་མ་བས་ཆེས་གོང་མའི་རྒྱུ་ཡོངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་རྒྱུ་དེ་ལས་ཀྱང་སངས་རྒྱས་ཀྱི་སའི་བར་དུ་འཇུག་པར་འགྱུར་བའོ། །

[Block 1308 [HEADING]]
### ས་བཅུ་དག་ཏུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་སྒོམ་པ། ^5-4-0

[Block 1309]
གཙོར་ནི་ས་བཅུ་དག་ཏུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་སྒོམ་པར༌[^850]འགྱུར་ཏེ་ཞེས་བྱ་བ་ལ། འདི་ལྟར་ས་བཅུ་པ་ལས་འབྱུང་བ་བཞིན་དུ་སྟེ།

[Block 1310]
དང་པོ་ལ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྷག་པར་འཇུག་པ༌[^851]ནས་ཇི་སྲིད་བཅུ་པ་ལ་ཡེ་ཤེས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་བར་གཙོ་བོར༌[^852]འཇུག་པས་ན་བཅུ་པོ་དག་ཏུ་བཅུ་བསྟན་པ་ཡིན་ལ། འདི་ལྟར་ཡང་ས་ཐམས་ཅད་ལ་ཐམས་ཅད་ཀྱང་བསྒོམ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1311]
དྲུག་ཏུ་ནི་དྲུག་ཅེས་བྱ་བ་ནི་གོ་རིམས་བཞིན་བསྟན་པ་ཡིན་ཏེ། འདི་ལྟར་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཕྱི་ནས་བསྟན་ལ། ཡེ་ཤེས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྔོན་དུ་བསྟན་པ་ལྟ་བུ་ནི་མ་ཡིན་ནོ། །

[Block 1312]
ཕྱི་མ་བཞི༌[^853]ནི་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་བསྟན་པར་བྱ་བ་བཞི་པའོ། །

[Block 1313]
གོང༌[^854]དུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་བསྟན་པ་དེར་ཐབས་ལ་མཁས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་བཞི་པོ་དག་ཀྱང་འདུས་པར་འགྱུར་བ་ཉིད་ཡིན་ནོ། །

[Block 1314]
གང་ཡང་བཅུར་བསྟན་པ་དེར་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཉིད་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 1315]
དེའི་རྗེས་ལ་ཐོབ་པས་བསྡུས་པ་ཉིད་པས༌[^855]ནི་དེ་ལས་གཞན་པའི་ཐབས་ལ་མཁས་པ་ལ་སོགས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པར་འགྱུར་རོ། །

[Block 1316]
དེས་ན་ཕྱི་མ་རྣམས་ལ་འདི་དག་སྒོམ་པར༌[^856]འགྱུར་བ་ཡིན་ནོ། །

[Block 1317 [HEADING]]
#### ཐབས་ལ་མཁས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ། ^5-4-1-0

[Block 1318]
ཐབས་ལ་མཁས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཞེས་བྱ་བ་དེ་སྟོན་པར་བྱེད་པ་ན༌[^857]སེམས་ཅན་ཐམས་ཅད་དང་ཐུན་མོང་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དེ་ལ་ཐུན་མོང་ཉིད་ནི་དགེ་བའི་རྩ་བ་བསགས་པ་རྣམས་སེམས་ཅན་རྣམས་ལ་ཇི་ལྟ་བ་བཞིན་དུ་འབྱུང་བར་བྱེད་པའོ། །

[Block 1319]
དེ་ཡང་བསྟན་པར་བྱ་སྟེ། གང་ཡང་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཐོབ་པར་འདོད་པས་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་ནས་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུའི་བསམ་པ་དང་མཐུན༌[^858]པའོ། །

[Block 1320]
དེས་ན་གང་སུ་དག་དེ་ལྟ་བུའི་སེམས་དང་། དེ་ལྟ་བུའི་དགེ་བའི་རྩ་བ་ཡོངས་སུ་བསྔོ་བས་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱའོ་ཞེས་བྱ་བ་དེས་ནི་སེམས་ཅན་ཐམས་ཅད་དང་ཐུན་མོང་དུ་ཐབས་ལ་མཁས་པའི་ཤེས་རབ་དང་སྙིང་རྗེ་དག་བསྟན་ཏེ། འདི་ལྟར་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གིས་དགེ་བའི་རྩ་བ་བསགས་པ་རྣམས་སྙིང་རྗེས་ནི་སེམས་ཅན་ཐམས་ཅད་དང་ཐུན་མོང་དུ་བྱེད་དོ། །ཤེས་རབ་ཀྱིས༌[^859]ནི་བརྒྱ་བྱིན་ལ་སོགས་པ་ཉིད་དུ་ཡང་ཡོངས་སུ་སྔོ་བར༌[^860]མི་བྱེད་དོ། །

[Block 1321]
དེས་ན་ཉོན་མོངས་པ་འབྱུང་བར་ཡང་མི་འགྱུར་ཏེ། ཡོངས་སུ་ཤེས་པའི་ཕྱིར་རོ། །

[Block 1322]
འཁོར་བ་ཡང་ཡོངས་སུ་མི་གཏོང་ལ། དེར་ཡང་ཀུན་ནས་ཉོན་མོངས་པ་འབྱུང་བར་མི་འགྱུར་བ་ནི་ཐབས་ལ་མཁས་པར་འགྱུར་བ་ཡིན་ཏེ། འདི་ནི་ཐབས་ལ་མཁས་པའོ། །

[Block 1323 [HEADING]]
#### སྨོན་ལམ་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ། ^5-4-2-0

[Block 1324]
གང་སྨོན་ལམ་སྣ་ཚོགས་ཀྱི་རྒྱུའི་དབང་གིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྣ་ཚོགས་ཀྱི་རྐྱེན་སྡུད་པ་དེ་ལྟ་བུ་ནི་སྨོན་ལམ་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལས་ཡིན་ཏེ། སྨོན་ལམ་ཉིད་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་སྨོན་ལམ་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 1325]
ཕྱི་མ་ལ་ཞེས་བྱ་བ་ལ་ཕྱི་མའི་རྒྱུ་མཚན་ནི་ཕྱི་མ་སྟེ་འདི་ནི་རྒྱུ་མཚན་བདུན་པ་ཡིན་ཏེ། དེའི་ཚེ་སྨོན་ལམ་སྣ་ཚོགས་བསྒོམ་པས༌[^861]དེས་ནི་ཕྱི་མ་ལ་འདི་དག་རྣམས་སྒོམ་པར༌[^862]འགྱུར་བ་ཡིན་ཏེ། དེའི་དབང་གིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྣ་ཚོགས་ཀྱི་རྐྱེན་སྡུད་པ་འཐོབ་བོ། །

[Block 1326 [HEADING]]
#### སྟོབས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ། ^5-4-3-0

[Block 1327]
མདོ་གཞན་ལས་སྟོབས་གཉིས་བསྟན་པ་ནི་སོ་སོར་རྟོག་པའི༌[^863]སྟོབས་དང་། བསྒོམ་པའི་སྟོབས་སོ། །

[Block 1328]
ཡང་གལ་ཏེ་བསྒོམ་པའི་སྟོབས་མེད་པ་ནི་སོ་སོར་རྟོག་པའི༌[^864]སྟོབས་ཀྱིས་འཇུག་པར་འགྱུར་ཏེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་གིས་ཕ་རོལ་ཏུ་ཕྱིན་པའི༌[^865]མི་མཐུན་པའི་ཕྱོགས་ཟིལ་གྱིས་མནན་ནས་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྒྱུན་མི་འཆད་པར་འབྱུང་བར་འགྱུར་ཏེ། འདི་དག་ནི་སྟོབས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 1329 [HEADING]]
#### ཡེ་ཤེས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ། ^5-4-4-0

[Block 1330]
ཡེ་ཤེས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལས་གང་ཡིན་པ་དེ་བསྟན་པར་བྱ་སྟེ། ཡེ་ཤེས་དེས་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ངོ་བོ་རྣམ་པར་མི་རྟོག་པའི༌[^866]ཡེ་ཤེས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་ཡིན་པ་རྣམ་པར་འཇོག་པ་སྟེ། གང་གིས་ཆོས་ལ༌[^867]ལོངས་སྤྱོད་པ་མྱོང་བ་དང་། ལྷན་ཅིག་ཏུ་ཆོས་དང་ལྡན་པའི་དོན་དང་། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་དོན་ཡང་ཡེ་ཤེས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 1331]
ཆོས་ཀྱི་རྣམ་གྲངས་དེ་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྡེ་སྣོད་ཀྱིས་བསྡུས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྡེ་སྣོད་ནི་ཐེག་པ་ཆེན་པོའི་ཆོས་ཐམས་ཅད་དོ། །

[Block 1332]
ས་བཅུ་པའི་ཆོས་ཀྱི་རྣམ་གྲངས་འདི་ཡང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྡེ་སྣོད་ཉིད་ཡིན་གྱི་ཉན་ཐོས་ཀྱི་ནི་མ་ཡིན་ནོ། །

[Block 1333]
དེ་བསྡུས་པ་ཉིད་ཀྱི་ཡང༌[^868]ཕྱིར་ན་ཡང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་བསྒོམ་པ༌[^869]ནི་ས་ཐམས་ཅད་ལ་འབྱུང་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1334]
སངས་རྒྱས་ཀྱི་ཞིང་རབ་འབྱམས་ཐམས་ཅད་དུ་སངས་རྒྱས་བྱུང་བ་ཐམས་ཅད་ཀྱིས་ཀྱང་རབ་ཏུ་བསྒོམས་པ་ཡིན་པའི༌[^870]ཕྱིར་ས་འདི་རྣམས་ནི་ཤིན་ཏུ་མཆོག་ཏུ་གྱུར་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཆོས་ཀྱི་རྣམ་གྲངས་དེ་ནི་ཡུལ་གྱི་མཆོག་ཉིད་དུ་བསྟན་ལ་དང་པོར་བསྟན་པ་ཡང་ཡིན་ནོ། །

[Block 1335]
ཡང་ཡུལ་དེ་ནི་ཤིན་ཏུ་གནས་པར༌[^871]གྱུར་པ་ཡིན་པ་དང་། ཉེ་བ་ན་གནས་པའི་ཡུལ་གཞན་གྱི་གཙོ་བོར་གྱུར་པ་ཉིད་ཀྱིས་དེ་ནི་མཆོག་ཡིན་ནོ། །
--- END BLOCKS ---
