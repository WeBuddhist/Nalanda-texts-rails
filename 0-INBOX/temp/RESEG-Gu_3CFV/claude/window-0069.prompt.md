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
ཁམ་ཧ་ཅང་ཆུང་བར༌[^1531]མ་ཡིན་པར་རོ། །

[Block 2417]
ཁམ་ཧ་ཅང་ཆེ་བར་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་ལ། ཁམ་ཞེས་བྱ་བ་ནི་ཁར་ཁམ་ཚད་དུ་གཞུག་ཅིང་མིད་པར་བྱ་བའི་ཕྱིར་ཁམ་ཞེས་བྱ་བ་སྟེ་དེ་བས་ན་ཁམ་རན་པར་རོ། །

[Block 2418]
ཁམ་མ་གཟས༌[^1532]པར་ཁ་མི་གདང་ངོ་། །ཁ་ཁམ་གྱིས་བཀང་སྟེ་མི་སྨྲ་བར་བྱའོ། །

[Block 2419]
ཡང་འདོད་པའི་ཕྱིར་འབྲས་ཆན་གྱིས་ཚོད་མ་མི་དགབ༌[^1533]ཚོད་མས་འབྲས་ཆན༌[^1534]མི་དགབ་པར༌[^1535]རོ། །

[Block 2420]
ཙུག་ཙུག་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཙུག་ཙུག་ཟེར་ཞིང་ཟས་བཟའ་བར་མི་བྱའོ། །

[Block 2421]
དགབ་པ་དང་གདང་བ་ཞེས་བྱ་བ་འདི་དག་ལ་འདི་ལ་ནུས་པ་མེད་པའི་ཕྱིར་འབྲེལ་པ་མེད་པ་ཉིད་དོ།[^1536] །དེ་བས་ན་འདིར་མངོན་པར་འབབ་པའོ། །

[Block 2422]
དེ་ཙམ་གྱིས་འདི་ལ་རྟོགས་པ་ཉིད་ཀྱི་ཕྱིར། རྣམ་པ་འདི་དག་བར་དུ་བཅད་པའི་ཕྱིར་བརྟག་པ་མ་ཡིན་ནོ། །

[Block 2423]
ཅག་ཅག་མི་བྱའོ། །

[Block 2424]
ཧུ་ཧུ་མི་བྱའོ། །

[Block 2425]
ཕུ་ཕུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་སྐད་ཟེར་ཞིང་བསོད་སྙོམས་བཟའ་བར་མི་བྱའོ། །

[Block 2426]
ཁ་ཁམ་གྱིས་བཀང་སྟེ་མི་སྨྲ་བར་བྱའོ། །

[Block 2427]
འབྲུ་ནས་ཐ་དད་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་བྱས་ཏེ་བསོད་སྙོམས་བཟའ་བར་མི་བྱའོ། །

[Block 2428]
འདིར་རིགས་པ་ནི་དེ་མ་ཐག་ཏུ་སྨོས་པ་དེ་ཉིད་ཡིན་ཏེ། དེ་རྣམས་ནི་ཁའི་རྣམ་པར་འགྱུར་བའི་སྒྲའི་བྱེ་བྲག་ཡིན་པས༌[^1537]འདི་ནི་རྣམ་པར་འགྱུར་བ༌[^1538]བྱེད་པའི་ཕྱིར་དགག་པ་ཡིན་གྱི། དེ་བརྟག་པའི༌[^1539]ཕྱིར་དགག་པ་ནི་མ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 2429]
འཕྱས་མི་གདགས་སོ། །

[Block 2430]
མཁུར་བ༌[^1540]མི་སྤོའོ། །

[Block 2431]
ཁམ་འཕྲོར་མི་གཅད༌[^1541]དོ། །

[Block 2432]
ལྕེ་ཕྱུང་སྟེ་ཟས་མི་ཟའོ། །

[Block 2433]
མཆོད་རྟེན་འདྲ་བར་བྱ་སྟེ་མི་གཞོམ་མོ། །

[Block 2434]
ལག་པ་མི་བལྡག༌[^1542]གོ། །

[Block 2435]
ལྷུང་བཟེད་མི་བྱོག་གོ། །

[Block 2436]
ལག་པ་མི་སྤྲུག་གོ། །

[Block 2437]
ལྷུང་བཟེད་མི་བསྐྱམ་མོ། །

[Block 2438]
རྐན་མི་གཏོག་གོ་ཞེས་བྱ་བ་ལ་འདི༌[^1543]ནི་གཟུང་བའི་ཚིག་ཡིན་ཏེ་ལག་པ་མི་བལྡག་པ་དང་ལྷུང་བཟེད་མི་བྱོག་པ་དང་། ལག་པ་མི་སྤྲུག་པ་དང་། ལྷུང་བཟེད་མི་བསྐྱམ་པ་དང་། རྐན་མི་གཏོག་པ་ཞེས་བྱ་བ་ནི་འདིར་དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས་སོ། །

[Block 2439]
ལྷུང་བཟེད་ཀྱི་འདུ་ཤེས་ཅན་ཁ་ཟས་ཡང་དག་པར་ཤེས་ཤིང་ལྷུང་བཟེད་དང་འབྲེལ་པའི་མིག་གིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2440]
འདིར་མིག་ནི༌[^1544]ཡིད་ཡིན་ཏེ། དེ་བས་ན་དེ་དང་འབྲེལ་པའི་ཡིད་ཅེས༌[^1545]བྱ་བ་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 2441]
ལྷུང་བཟེད་ཀྱི་དགོས་པ་ལ་བསྟན་པར་རིགས་པ་མ་ཡིན་ཏེ། དེ་བས་ན་དེའི་དབང་གིས་འདིར་ལྟ་བའི་རྣམ་པར་རྟོག་པར་བྱེད་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2442]
དྲུང་ན་འདུག་པའི་དགེ་སློང་གི་ལྷུང་བཟེད་ལ་འཕྱས་གདགས་པའི་བདག་ཉིད་ཅན་གྱི་དོན་ལ་རྗེས་སུ་བསྒྲུབ་པ་མཐོང་ཞིང་བལྟ་བའོ། །

[Block 2443]
ལག་པ་ཟས་དང་འབགས་པས༌[^1546]ཆུ་སྣོད་ལ་མི་བཟུང་ངོ་། །དྲུང་ན་འདུག་པའི་དགེ་སློང་ལ་ཟས་དང་འབགས་པའི་ཆུས་མི་གཏོར་རོ། །

[Block 2444]
ཁྱིམ་པ་འདུག་པ་ལ་མ་དྲིས་པར༌[^1547]དེའི་ཁྱིམ་དུ་མི་དབོའོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་ཟས་དང་འབགས་པའི་ཆུའོ། །

[Block 2445]
ལྷུང་བཟེད་ཀྱི་ནང་དུ་ཟས་ཀྱི་ལྷག་མ་བླུགས་ཏེ་མི་དོར་བའོ།[^1548] །ལྷུང་བཟེད་ལེན་གསུམ་བཀྲུས་ཏེ་གཙུག་ལག་ཁང་གི་ཚིགས་སུ་བཅད་པ་དག་གིས་བཟླས་བརྗོད་བྱས་པའི་ལྷུང་བཟེད་ཀྱི་ཆུ་སྦྱིན་པར་བྱའོ། །

[Block 2446]
འོག་གཞི་མེད་པའི་ས་ཕྱོགས་སུ་ལྷུང་བཟེད་མི་གཞག་པར་རོ། །

[Block 2447]
འགྲེང་སྟེ་ལྷུང་བཟེད་མི་བཀྲུ་བར་རོ། །

[Block 2448]
དེ་གཉིས་དེ་གསུམ་དུ་མི་བྱ་བར་རོ་ཞེས་བྱ་བ་ལ་གཉིས་པོ༌[^1549]ནི་བཀྲུ་བ་དང་གཞག་པའོ། །

[Block 2449]
གད༌[^1550]ཀ་མ་ཡིན་པར་རོ། །

[Block 2450]
གཡང་ས་མ་ཡིན་པར་རོ། །

[Block 2451]
དཀན་གཟར་པོ་མ་ཡིན་པར་རོ། །

[Block 2452]
ལམ་གྱི་བཞི་མདོར་མི་བྱའོ། །

[Block 2453]
དེས་འབབ་ཆུ་དྲག་པོའི༌[^1551]རྒྱུན་ལས་བཟློག་སྟེ་ཆུ་མི་བཅུ་བར་རོ། །

[Block 2454]
བཤང་གཅི་ཡན་ཆད་ནི་མི་ན་བ་ལའོ། །

[Block 2455]
ལངས་ཏེ་བཤང་གཅི་མི་བྱའོ་ཞེས་བྱ་བ་འདིའི་གོང་རོལ་དུ་དེ་དག་ལ་ནི་མིན་བའོ་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །
--- END BLOCKS ---
