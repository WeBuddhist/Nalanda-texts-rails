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
[Block 2066]
གྲུབ་པའི་བློ་ཡང་དག་པར་གནས་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 2067]
ཤོ་གམ་གྱི་ས་ལས་འདས་ན་ཞེས་བྱ་བ་སྨོས་པ་དེར་ཤོ་གམ་གྱི་བརྐུས་པ་ཉིད་དུ་བརྗོད་དེ་ཤོ་གམ་གྱི་བྱ་བ་ཉིད་ལ་བརྟེན་པ་སྐྱེ་བ་དང་བཅས་པ་ལྟུང་བ་དང་ལྟུང་བ་མ་ཡིན་པའི་ཚིག་རྣམས་གང་ཡིན་པ་དེ་རྣམས་ནི་རྣམ་པར་འབྱེད་པ་ལས་བསྡུ་བར་བྱ་སྟེ། རྐུ་སེམས་མེད་པ་ལ་ཤོ་གམ་དུ་གཏོགས་པའི་ཉེས་པ་འབྱུང་བར་དོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་སྤང་བ་མ་ཐོབ་པའི་དགེ་སློང་རྣམས་ཀྱིས་ཚོང་པ་རྣམས་ལ་ཤོ་གམ་དུ་གཏོགས་པ་ལས་འདའ་བར༌[^1426]བྱ་བའི་ཕྱིར་སྦྱིན་པ་གང་ཡིན་པ་དེར་ཚོང་པ་རྣམས་འདིར་རྐུ་བར་བྱེད་པ་ཉིད་མ་ཡིན་ཏེ་ཤོ་གམ་པའི་སེམས་བཟུང་བར་བྱས་པའི་ཚོང་པ་དེ་རྣམས་ལས་འདའ་བའི༌[^1427]ཕྱིར་རོ། །

[Block 2068]
གང་གི་ཕྱིར་དགེ་སློང་རྣམས་ལ་བརྐུས་པ་ཉིད་དུ་མི་འགྱུར་བ་དེའི་ཕྱིར་ལྟུང་བ་མེད་པའི་ཚིག་རིགས་པ་ཡིན་ནོ། །

[Block 2069]
གང་ཞིག་ཡོངས་སུ་སྤང་བ་མ་ཐོབ་པའི་དགེ་སློང་གིས་དགེ་སློང་གཞན་ལ་འདའ་བའི་ཕྱིར་སྣོད་སྦྱིན་པ་དེར་ཡང་དགེ་སློང་འདི་ཡིན་ཏེ། འདི་ནི་དེ་ལྟར་འདའ་བར་གྱུར་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་འདི་ལ་རྐུ་བ་ཉིད་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བ་ལྟུང་བ་མ་ཡིན་པའི་རིགས་པར་གྱུར་པ་ཉིད་དེ་ངེས་པར་འདིར་འདིའི་བློ་ཞེས་བྱ་བ་རྐུ་བ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 2070]
གང་ཞིག་སྤོང་བ་ཐོབ་པ་རྣམས་ཚོང་པ་རྣམས་དང་འབྲེལ་པ་ལས་འདའ་བར་བྱེད་པ་དེར་འདི་རྣམས་ལ་གཞན་གྱི་དོན་དུ་བརྐུས་པ་ཉིད་ཡོད་པ་དེར་རང་གི་སྤོང་བ་ཐོབ་པ་འདི་ཞེས་བྱ་བ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 2071]
དེ་ལ་འདི་རྣམས་ལ་གང་ཞིག་ལྟུང་བ་མེད་པར་བརྗོད་པ་དེར་རྐུ་སེམས་མེད་པར་རྒྱུ་རྣམ་པར་གནས་པ་ཡིན་ཏེ། འདི་ལ་འདི་བསྡུས་པའོ། །

[Block 2072]
འདི་ནི་བདག་ཅག་ལ་གཞན་གྱི་སྤོང་བའི་ཆ་ཤས་པས༌[^1428]འདི་རྣམས་ལ་རྐུ་སེམས་ཀྱིས༌[^1429]སྐབས་མ་གྱུར་ཅིག་ཅེས་བྱ་བ་འདིར་རིག་པར་བྱའོ། །

[Block 2073]
གང་གིས་བླངས་པ་ཉིད་ཀྱི༌[^1430]སྣོད་ལས་སྦྱིན་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་གིས་བླངས་པ་ནི་གང་གིས༌[^1431]བླངས་པ་སྟེ། དེའི་དངོས་པོ་ནི་གང་གིས་བླངས་པ་ཉིད་དོ། །

[Block 2074]
གང་གིས་དངོས་པོ་བཟུང་བ་ཤོ་གམ་དེ་ལ་སྦྱིན་པ་ཉིད་དོ། །

[Block 2075]
གང་ཞིག་འདིར་འདའ་བར་བྱེད་པ་གཉིས་ནི་སྐྱོན་མེད་པ་དང་ལྡན་པ་གང་གིས་དངོས་པོ་བླངས་པ་དེ་ཤོ་གམ་སྦྱིན་པ་ཉིད་དུ་གྱུར་པ་ལ། འདི་གཉིས་ལ་སྐྱོན་མེད་པ་ཉིད་དུ་རིགས་པ་ཡིན་ཏེ་ཞེས་བྱ་བ་འདི་ཤེས་པའོ། །

[Block 2076]
གནང་བ་ལས་གཞན་གྱིས་བཟླས་ན་མ་བརྐུས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། །གནང་བ་ནི་སྤོང་བ༌[^1432]ཐོབ་པའོ། །

[Block 2077]
དེ་ལ་གཞན་གྱི་ནོར་ལ༌[^1433]དེ་བྱས་པའི་འདའ་བར་བྱེད་པ་གང་ཡིན་པ་འདི་ནི་དེའི་ཆའི་ཕྱིར་མ་བ་རྐུས་པ་ཡིན་ནོ། །

[Block 2078]
གང་ཞིག་འདི་ཤོ་གམ་མ་བྱིན་པ་ཞེས་བྱ་བ་སྤང་བ་སྦྱིན་པ་རང་གི་ཆ་སོ་སོར་ཐོབ་པ་སྟེ་གཞན་གྱི་ནི་མ་ཡིན་ནོ། །

[Block 2079]
དེ་བས་ན་སྐྱོན་འདི་འབྱུང་བ་སྟེ། ཚོང་པ་དང་འབྲེལ་པའི་འདའ་བར་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 2080]
སླར་དགེ་སློང་གིས་ས་ལ་རྙེད་པའི་ཤོ་གམ་འདའ་བར་བྱེད་པ་སྟེ༌[^1434]དགེ་སློང་གིས་ས་ལ་རྙེད་པའི་ཤོ་གམ་འདའ་བར་བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་བརྗོད་པ་ལ་བསྡུ་བ་ནི་འདི་ཡིན་ནོ། །

[Block 2081]
དངོས་པོ་ཇི་ལྟར་ལྟུང་བ་ལ་འགལ་ཚབས་ཅན་ཞེས་བྱ་བ༌[^1435]གསུངས་པའི་ཚིག་ཀྱང་གཞི་ཇི་ལྟ་བ་ལས་འབྱུང་བ་ཡིན་གྱི་ཉེས་བྱས་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 2082]
འདི་ཅིའི་ཕྱིར་ཞེ་ན། ཉེ་བ་འཁོར་གྱིས་ཞུས་པ༌[^1436]ལས་འདིར་སྦོམ་པོའི་ལྟུང་བ་ལ་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 2083]
བཙུན་པ་རེ་ཞིག་ཚོང་པ་རྣམས་ཤོ་གམ་གྱི་ཕྱིར་ཤོ་གམ་ལ་ཉེ་བར་བརྟེན་པའི་དངོས་པོ་ནི་ས་ལ་ཡང་དག་པར་རྙེད་པར་འགྱུར་ཏེ། དགེ་སློང་ལ་ཚོང་པས་འདི་སྐད་ཅེས་སྨྲས་ཏེ། འཕགས་པ་བྱིན་ཅིག་ཤོ་གམ་གྱི་ས་ལས་འདའ་བར་བྱས་ནས་དགེ་སློང་གིས་དེ་ལས་འདའ་བར་བྱེད་ན་ཤོ་གམ་འཇོམས་པ་སྟེ། དེ་ལ་མ་ཤ་ཀ་ལྔའི་རིན་ཐང་འབྱུང་བར་འགྱུར་ཏེ། སྦོམ་པོའི་ལྟུང་བ་ལ་ལྟུང་བར་འགྱུར་ཞེས་བྱ་བའོ། །

[Block 2084]
སྤང་བ་ཐོབ་པའི་དགེ་སློང་གི་དབང་དུ་མཛད་ནས་འདི་གསུངས་པ་རྣམ་པར་གནས་པ་ཡིན་ཏེ། གཞན་གྱིས་རིག་པ༌[^1437]ཤོ་གམ་པ༌[^1438]རྣམས་ཀྱིས་འདའ་བར་བྱ་བའི་ཕྱིར་མི་ནུས་པ་ཉིད་ཀྱིས་བརྐུ་བ༌[^1439]ཉིད་ཚོང་པ་རྣམས་ཉིད་ལ་ཤིན་ཏུ་བྱ་སླ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2085]
རང་གི་བྱ་བ་མ་ཡིན་པའི་དབང་དུ་བྱས་ནས་སྦོམ་པོ་འདི་བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 2086]
མ་གནང་བས་གཞན་གྱིས་འདའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཆོ་ག་ཡང་དག་པར་བྱས་པ་གཞན་གྱིས༌[^1440]ཤོ་གམ་རང་གིས༌[^1441]ཤོ་གམ་གྱི་བྱ་བ་ལས་འདའ་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2087]
ཚོང་པ་རྣམས་ཀྱིས་འདའ་བར་བྱེད་པས་ཀྱང་སླར་དགེ་སློང་གི༌[^1442]སར་ཕྱིན་པའི་ཤོ་གམ་འདའ་བར་བྱེད་པ་སྟེ། དགེ་སློང་གི་སར་ཕྱིན་པའི་ཤོ་གམ་འདའ་བར་བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་དེའི་དོན་བསྡུ་བའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 2088]
རྐུ་བ་ལ་གནས་པའི་སྐྱོན་གྱིས་སྐྱོན་དང་བྲལ་བ་ཉིད་དུ་གྱུར་པ་ལ་འདི་ཡིན་ཏེ། དེ་བས་ན་བསླབ་པ་གཞན་ལ་འདི་རབ་ཏུ་བཏགས་པ་ཉིད་དོ། །

[Block 2089]
རབ་ཏུ་བཏགས་པ་འདི་ན་སླར་ཅིའི་ཕྱིར་ཞེ་ན། རྐུ་བའི་རྣམ་པ་ཉིད་ཀྱིས༌[^1443]འདི་འཇིག་རྟེན་ན་ཁ་ཟེར་བར་འགྱུར་བའི་སྐྱོན་ཉིད་ཀྱིས་གཞན་དུ༌[^1444]ཡང་གཞན་གྱིས་འདའ་བར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བ་འདིའི་རྗེས་སུ་འབྲང་བས༌[^1445]རྟོགས་པར་བྱའོ། །

[Block 2090]
མ་ཚོར་བར་འདའ་བར་བྱེད་པ་མི་གྲུབ་པར་བྱ་བའི་ཕྱིར་མི་འབད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདའ་བར་བྱ་བ་གྲུབ་པ་ཉིད་ཀྱིས་འདི༌[^1446]ནི་གཞན་གྱིས་སམ་བདག་ཉིད་རང་ཉིད་ཀྱིས་སམ།[^1447] གཞན་གྱི་ཡང་དག་པར་རིག་པ་ལས༌[^1448]འདའ་བར་བྱེད་པ་སེར་སྣ་ལ་སོགས་པ་ཞེས་བྱ་བ་འདིའི་དོན་དུ་མི་འབད་པར་མི་བྱའོ། །

[Block 2091]
འདི་ལྟར་འདའ་བར་བྱེད་པ་ལ་རྐུ་བའི་རྣམ་པ་ཉིད་དང་། སྐྱོན་ཉིད་ཀྱིས་སྲིད་པའི་སྐབས་ཡོད་པ་ཡིན་ཏེ་ཞེས་བྱ་བ༌[^1449]འདི་རྣམས་ནི་བཏགས་པའོ། །ཇི་ལྟར་ཡང་མི་འབད་པར་མི་བྱ་ཞེ་ན། དེའི་ཕྱིར་སྲུང༌[^1450]མ་དགེ་སློང་དུ་མ་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2092]
སྲུང༌[^1451]མ་ཇི་ལྟ་བུ་ཞེ་ན། དགེ་སློང་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2093]
གྲངས་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་དུ་མ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཉིས་ཡན་ཆད་ནས་བརྩམས༌[^1452]ཏེ་བསྲུངས་པའི༌[^1453]ཕྱིར་ཇི་སྙེད་ཀྱིས་དོན་གྲུབ་པ་དེ་སྙེད་གཞག་གོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2094]
དེའི་ཟན་བསྐྱལ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྲུང་བར་བྱེད་པ་དེའི་ཟན་ནི་དེའི་ཟན་ཏེ་དེའོ།[^1454] །དེའི་བསྐྱལ་བར་བྱ་བ་ཉིད་དེ་འདི་ནི་ངེས་པ་མ་ཡིན་ནོ། །

[Block 2095]
དེས་ན་འདིར་འཇུག་པ་གང་ཡིན་པ་དེ་ལ་རྟོགས་པ༌[^1455]ཉིད་མ་ཡིན་པ་ཤེས་པར་བྱ་ཞེས་བྱ་བའི་དོན་དུ་འདི་བརྗོད་པའོ། །

[Block 2096]
དེས་བཟློག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྲུང་བའི༌[^1456]དགེ་སློང་གཞག་པས་སོ། །

[Block 2097]
བཅུག་པ་ཉིད་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེས་ཞེས༌[^1457]བྱ་བར་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 2098]
གང་རྣམས་ཀྱིས་གཞག་པ་དེ་རྣམས་ལ་ཞེས་བྱ་བ་དོན་གྱིས་གྲུབ་པ་སྟེ་གཞག་པ་ལ་དེའི་དོན་ཉིད་ཀྱིས༌[^1458]ཕྱིར་རོ། །

[Block 2099]
མེད་ན་མཚན་མ་གདབ་པོ་ཞེས་བྱ་བ་ནི་སྲུང༌[^1459]མ་མེད་ན་བསོད་སྙོམས་ལ་སོགས་པ་ལ་ཡང་འགྲོ་བའི་དོན་དུ་འགྲོ་བར་བྱེད་ཅིང་རང་གི་སྣོད་དག་ལ་མཚན་མ་གདབ་པར་བྱའོ། །

[Block 2100]
བསོད་སྙོམས་ཀྱི་ཕྱིར་ཞུགས་པ་ལ་ཤོ་གམ་གཞལ་དགོས་པ་ལ་ལས་མི་ཕྱུང་བ་མི་བཅུག་པར་བྱ༌[^1460]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2101]
ཁྱེར་ཏེ་འོངས་པ་ལ་དྲི་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་གྱིས་གང་ཡང་རུང་བ་ཤོ་གམ་དུ་བྱ་བ་མ་ཡིན་པའི་དངོས་པོ་ལ་ཤོ་གམ་གྱི་གནས་ནས་འདའ་བར་བྱེད་པའི་དོན་དུ་ཁྱེར་ཏེ་འོངས་པ་ལ་ཤོ་གམ་གཞལ་དགོས་པའི་རྫས་ཅུང་ཟད་མེད་དམ་ཞེས་བྱ་བ་འདི་དྲི་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2102]
གཞན་གྱིས་དོར་བ་མི་འགྲུབ་ན་རེག་པ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་བ་ནི་གསེར་ལ་སོགས་པ་རེག་པར་བྱ་བ་མ་ཡིན་པ་ལ་གཞན་གྱིས་དེའི་གཏུར་བུ་ལ་སོགས་པའི་ནང་དུ་བཅུག་པ་ལ་རང་གིས་རིག་པར་མ་བྱས་ན་དོར་བ་དབྱུང་བར་མི་འགྲུབ་ན་དེའི་ཚེ་དབྱུང་བའི་ཆེད་དུ་རང་ཉིད་ཀྱིས་རེག་པ་ཉིད་དུ་བྱས་ཏེ་དེ་ལ་ནི་ལྟུང་བར་བྱེད་པ་འགའ་ཞིག་ཏུ་འགྱུར་བ་བག་ཡོངས་སུ་གནང་ངོ་། །མ་ཕུལ་ཡང་ངེས་པ་སྐྱེས་ན་ཕུལ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མ་ལ་སོགས་པ་རྣམས་ལ་བདག་གིས་འདི་སྦྱིན་པ་ཞེས་བྱ་བ་གང་ཞིག་འདི་རྫས་ངེས་པར་བྱས་ནས་བཟུང་བ་མ་ཕུལ་བའི་རྫས་དེ་ལ་ཡང་ཕུལ་བ་ཉིད་ཁོ་ན་ཤེས་པར་བྱའོ། །

[Block 2103]
གང་ལ་ཕུལ་བ་ཡིན་པ་དེས་མ་བཟུང་བ་ཞེས་བྱ་བ་བྱས་ཏེ།[^1461] གང་གིས༌[^1462]དེའི་ལག་པ་ལ་དེ་དང་འབྲེལ་བ་ཉིད་ཤེས་པར་བྱ་བའི་དོན་དང་དེ་དང་འདྲ་བའི་ཤོ་གམ་གྱི་བྱ་བ་འདའ་བར་བྱེད་པ་ལ་གཞན་གྱི་དོན་དུ་རྐུ་བ་ལ་སྐྱོན་ཏེ་དེ་ལྟུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2104]
དེ་དག་གིས༌[^1463]རྫས་གནང་བར་བྱ་བའི་ཕྱིར་ཕ་མའི་བསྔགས་པ་བརྗོད་དོ་ཞེས་བྱ་བ་ལ། ཕ་མ་ཞེས་བྱ་བ་ནི་ཕ་མ་དག་ལའོ། །

[Block 2105]
ཕ་མ་དག་གི་ཆེད་དུ་བཀུར་བའི་རྫས་ནི་ཕ་མ་དག་ལ་བསྔགས་པ་བརྗོད་པར་བྱ་བ་སྟེ། འདིའི་དོན་དུ་ཤོ་གམ་པ་རྣམས་ཀྱི་དྲུང་དུ་འདི་དག་གི་ཡོན་ཏན་བརྗོད་པ་གང་ཡིན་པ་དེ་ནི་བརྗོད་པ་ཙམ་དོན་དུ་གཉེར་བ་ཞེས་བྱ་བ་ཡོངས་སུ་བརྟགས་ནས་སྐྱོན་དང་ལྡན་པ་ཤེས་པར་བྱ༌[^1464]ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
