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
[Block 2416]
ཕྱུགས་སུ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཕྱུགས་དག༌[^1535]མཆོད་སྦྱིན་དུ་བསད་པ་དེ་བཞིན་དུ་ཁྱེད་བདག་ཉིད་གསོད་པར་བྱེད་པའོ། །

[Block 2417]
མཆོད་སྦྱིན་ལ་ནི་ཚུལ་འདི་ཡིན་ཏེ། བདག་ཉིད་གསོད་པའི་ཚུལ་ལོ། །

[Block 2418]
དེ༌[^1536]ཕྱིར་དེ་དག་ཚིག་ནི་སུ་ཞིག་ཉན། །ཞེས་བྱ་བ་ནི་ཇི་སྐད་སྨྲས་པ༌[^1537]དེ་བཞིན་དུ་ནི༌[^1538]མི་བྱེད་ན༌[^1539]ནི་ཚིག་བཙུན་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2419]
དེ་ལྟར་ལྷའི་འཇིག་རྟེན་དུ་སྐྱེ་བ་མི་རིགས་པར་བསྟན་ནས། བསྟན་མ་ཐག་པའི་ཚིགས་བཅད་གཉིས་ཀྱིས་ལྷ་མཉེས་པར་འགྱུར་བ་ཉིད་དུ་མི་རིགས་པར་བསྟན་པའི་ཕྱིར། མཚུངས་མེད་མཐུ་བསུང༌[^1540]ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2420]
བསུང༌[^1541]ཉིད་མཐུ་ཡིན་པས་མཐུ་བསུང༌[^1542]ངོ་། །མཐུ་བསུང༌[^1543]དང་། རོ་དང་། གཟི་ནི༌[^1544]མཚུངས་མེད་མཐུ་བསུང༌[^1545]ལྡན་པའོ། །

[Block 2421]
མཚུངས་པ་མེད་པའི༌[^1546]མཐུ་བསུང༌[^1547]དང་། རོ་དང་། གཟི་ལྡན་པའི་བདུད་རྩི་གང་ཡིན་པ་དེ་ནི་མཚུངས་པ་མེད་པའི་མཐུ་བསུང༌[^1548]དང་། རོ་དང་། གཟི་ལྡན་པའི་བདུད་རྩིའོ། །

[Block 2422]
ཟས་མཆོག་ནི་གཙང་བའོ། །

[Block 2423]
ལྷ་མོས་ཕུལ་བ་ཞེས་བྱ་བ་ནི་ལྷ་མོ་མཆོག་གིས་ཕུལ་བའི་ཡིད་དུ་འོང་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2424]
[^1549]དེ་ལྟར་གསུམ་གྱི༌[^1550]མི་མཐུན་པའི་ཕྱོགས་གསུམ་གྱིས་བསྟན་ཏོ། །

[Block 2425]
མཚུངས་མེད་མཐུ་བསུང༌[^1551]རོ་དང་གཟི་ལྡན་པ། །ཞེས་བྱ་བ་ནི་ཁྱད་པར་མེད་པའོ། །

[Block 2426]
ཕྱུགས་བསད་ཤ་ཁྲག་ཅེས་བྱ་བ་བསྟན་པ་ལ་མཆོད་སྦྱིན་ལ་ཕྱུགས་ཀྱི་ཤས་རུང་བ་མ་ཡིན་ནོ། །

[Block 2427]
སྩོགས་པ་སྨོས་པ་ནི་གང་དེར་སྦྱིན་པ་གཞན་དག་ཀྱང་གཟུང་ངོ་། །དེ་ལྟ་བུའི་རྣམ་པའི་ཟས་འདིའི་གཉེན་པོས༌[^1552]ཕྱུགས་བསད་ཤ་ཁྲག་ཅེས་བྱ་བ་བསྟན་པ་དང་། ལྷ་རྣམས་མགུ་བར་འགྱུར་བ་ཞེས་བྱ་བས་ནི་གང་སྔར་བསྟན་པའི་མཆོད་སྦྱིན་ལེགས་པར་བགྱིས་པས་ལྷ་མཉེས་ན་ཞེས་བྱ་བ་དེ་མི་རིགས་པར་བསྟན་ཏོ། །

[Block 2428]
ཕན་འདོགས་པ་དང་ལྡན་པར་འགྱུར་རོ་ཞེས་བྱ་བ་གང་གི་ཕྱིར། ཁྱེད་ཅག་གིས༌[^1553]ང་ལ་རྗེས་སུ་བཟུང་བ༌[^1554]དང་ལྡན་པ་སྟེ། དེས་ན༌[^1555]རྗེས་སུ་བཟུང་བ༌[^1556]ཡིན་པས་ཕན་འདོགས་པ་དང་ལྡན་པར་འགྱུར་བའོ། །

[Block 2429]
བག་མེད་པའི་གཉིད་ཀྱིས་ལོག་པ་གང་ཡིན་པ་དེ་ནི་བག་མེད་པའི་གཉིད་ཀྱིས་མ་ལོག་པ་སྟེ། བག་མེད་པའི་གཉིད་ཀྱིས་མ་ལོག་ཅིང་དྲི་མ་མེད་པ་དེས་སོ། །

[Block 2430]
རྟོག་ཆེན་ཉིད་མིག་ཡིན་པས་རྟོག་ཆེན་མིག་གོ། །

[Block 2431]
རང་གི་ཡུལ་ཁོ་ན་ལ་མཐུན་པའི་ཆོས་ཀྱིས་ཐོབ་པའི་རྗེས་སུ་དཔག་པའི་ཚུལ་ལོ། །

[Block 2432]
ག་ལ་བགྱིད་ཅེས་བྱ་བ་ནི་རྗེས་སུ་དཔག་པའི་ཚུལ་འདིའི་དོན་ནི་བདག་གིས་མི་ཤེས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2433]
དམ་པ་རྣམས་ཀྱི་ཚད་མའི་མཆོག་ནི་ལེགས་པའི་ཚད་མའི་ནང་ན་ཚད་མའི་མཆོག་གོ། །

[Block 2434]
སྐྱེ་བོ་མང་པོས་མཐོང་བར་གྱུར་པ་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་ལ་བསྟན་པར་གྱུར་པའོ། །

[Block 2435]
སྡིག་པ་བྱེད་པའི་མི་རྣམས་འཛིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྡིག་པ་བྱེད་པའི་སྐྱེ་པོ་གཟུང་བའི་ཕྱིར་རོ། །

[Block 2436]
བརྟན༌[^1557]ཞིང་གཙང་མ་ཚུལ་ཁྲིམས་ནོར་ལྡན་ཞེས་བྱ་བ་ལ། བརྟན་པའི་ཚུལ་ཁྲིམས་ནི༌[^1558]རྒྱུན་དུ་བསྲུང༌[^1559]བའི་ཕྱིར་རོ། །

[Block 2437]
གཙང་མ་ནི་གུས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2438]
དེ་ཉིད་ནོར་ཡིན་ཏེ། འདོད་པའི་དོན་སྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 2439]
གང་དེ་ལྟ་བུ་དེ་ཉིད་ནི་མི་མཆོག་ཅེས་བརྗོད་དོ། །

[Block 2440]
སྟོང་གིས་ཞེས་བྱ་བ་ནི་སྟོང་ཕྲག་དུ་མའོ། །

[Block 2441]
ཚུལ་མ་ཡིན་པའི་རྗེས་སུ་སྤྱོད་པ་དེ༌[^1560]བརྙེས་པ་ནི་ཚུལ་མིན་རྗེས་སྤྱོད༌[^1561]བརྙེས་པའོ། །

[Block 2442]
དེ་བས་ན་སྡིག་པ་བྱེད་པའི་མི་བཟུང་བའི༌[^1562]ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་བཟུང་བ༌[^1563]མཆོག་ཏུ་བྱེད་པའོ། །

[Block 2443]
ཚུལ་ཁྲིམས་དང་སྡོམ་པ་ཡང་དག་པར་བླང་བ་ལ་ནི་འབད་ཅེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་ཉིད་སྡོམ་པ་ཡིན་པས་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པའོ། །

[Block 2444]
ཚུལ་ཁྲིམས་ཡོད་པའི་ཕྱིར་ཚུལ་ཁྲིམས་ལྡན་པ་སྟེ། འགྱོད་པ་ལ་སོགས་པ་སེམས་ཀྱི་གདུང་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2445]
ཚུལ་ཁྲིམས་ཁོ་ན་སྡོམ་པ་སྟེ། མི་དགེ་བའི་ལས་སྤངས་པའི་མཚན་ཉིད་ཡིན་པས་སོ། །

[Block 2446]
ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་ཡང་དག་པར་བླང་བ་ནི་ཚུལ་ཁྲིམས་དང་སྡོམ་པ་ཡང་དག་པར་བླང་བའོ། །

[Block 2447]
དེ་ལ་འབད་ཅིང་མཆོག་ཏུ་བྱེད་པ་དེ་དག་ནི་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་ཡང་དག་པར་བླང་བ་ལ་འབད་པ་སྟེ། དེ་ལྟར་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་ལ་ཡང་དག་པར་འབད་པའི་ཕྱིར་རོ། །

[Block 2448]
ཚུལ་མ་ཡིན་པ་ལ་བྱེད་པར་དགའ་བ་ནི་བཏང་ཞེས་བསྟན་པ་ཡིན་ཏེ། འདིས་ནི་དགེ་བའི་ལས་ཀྱི་ལམ་བདུན་པོ་ལུས་དང་ངག་གི་མཚན་ཉིད་ཀྱི་ལྡོག་པ་བསྟན་ཏོ། །

[Block 2449]
དགྲར་འཛིན་པ་ལས་ནི་ཕྱིར་ཕྱོགས༌[^1564]ཞེས་བྱ་བ་ནི་ཡིད་ཀྱིས་ཞེ་འགྲས་པ༌[^1565]ལས་ལྡོག་པ་བསྟན་ཏོ། །

[Block 2450]
གཅིག་ལ་གཅིག་དགའ་བ་དང་གུས་པར་ནི༌[^1566]བྱེད་ཅེས་བྱ་བ་འདིས་ནི་ཞེ་སྡང་གི་མི་མཐུན་པའི་ཕྱོགས་ཡོན་ཏན་ཡང་དག་པར་བསྟེན་པ་བསྟན་ཏོ། །

[Block 2451]
འཐབ་པ་དང་རྩོད་པ་ཞེས་བྱ་བ་འདིས་ནི་མི་དགེ་བའི་ལམ་དག་གིས་བསྡུས་པ་ལས་ལྡོག་པ་བསྟན་ཏོ། །

[Block 2452]
བླ་མའི་ངག་ཉན་ཞིང་རྗེས་སུ་མཐུན་པར་ནི་བྱེད་ཅེས་བྱ་བ་འདིས་ནི་གང་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་བླངས་ཤིང་སྤོང་བ་ལས་སྐྱེས་པའི་དབང་དུ་བྱས་པ་སྟེ། བླ་མས་ནི་མི་དགེ་བ་ལས་ལྡོག་པ་དང་། དགེ་བ༌[^1567]ལ་འཇུག་པ་བསྟན་ཏོ། །

[Block 2453]
བགོ་བཤའ་བྱེད་པ་ལ་ནི། བག་ཚ་བ་མེད་ཅེས་བྱ་བ་ནི་ནང་གི༌[^1568]ཕ་མ་ལ་སོགས་བའོ། །

[Block 2454]
གློ་བུར་དུ་འོངས་པ་ལ་ནི་དགའ་ཞེས་བྱ་བ་ནི་མགྲོན་ལ་མཉེས༌[^1569]གཤིན་པའོ། །

[Block 2455]
དུལ་བ་དང་གུས་པར་བྱ་བ་ལ་ནི་འབད་པར་གྱུར་ཞེས་བྱ་བ་ལ། དུལ་བ་ནི་ཉོན་མོངས་པ་ཉེ་བར་ཞི་བའོ། །
--- END BLOCKS ---
