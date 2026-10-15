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
[Block 2591]
སྤངས་པ༌[^2417]ལས་ནི་སྤངས་པ་དང་བྲལ་བ་སྔོན་དུ་བཏང་བ་ལས་སོ་ཞེས་བྱ་བ་ནི་ལྟུང་བྱེད་ལས་རྫས་དེ་སྤངས་པ་དང་སྤངས་པ་དག་ཞག་གཅིག༌[^2418]བྲལ་བར་བྱ་བ་དེ་གཉིས་སྔོན་དུ་བཏང་སྟེ། བཤགས་ན་ལྡང་བར་འགྱུར་རོ། །

[Block 2592]
བཏང་བ་ལས་སོ་ཞེས་བྱ་བ་ནི་ནང༌[^2419]མ་བྱས་པ་ལས་སོ། །

[Block 2593]
ཞག་དེ་ལ་ཆོས་གོས་གཞན་བྱིན་གྱིས་མི་རློབ་པར༌[^2420]བྱིན་གྱིས་བརླབ་ཏུ་རུང་བའི་ཆོས་གོས་མེད་པར་གནས་པར་བྱའོ། །

[Block 2594]
དེ་གཉིས་སྔོན་དུ་སོང་བའི་བཤགས་པ་བྱས་ན་སྤང་བའི༌[^2421]ལྟུང་བྱེད་ལས་ལྡང་བར་འགྱུར་རོ། །

[Block 2595]
ཆོས་གོས་གཞན་བྱིན་གྱིས་བརླབས༌[^2422]ན་ནི་བྱིན་གྱིས་བརླབ་ཏུ་རུང་བ་དང་བྲལ་བར་མི་འགྱུར་རོ། །

[Block 2596]
ལྷག་མ་དང་བཅས་པར་གཏོགས་པའི་སྦོམ་པོ་ལྕི་བ་ལས་ནི་དགེ་འདུན་ལྔ་ལ་སོགས་པའི་ཐམས་ཅད་ལའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལྷག་མ་དང་འབྲེལ་བའི་སྦོམ་པོ་ལྕི་བ་ལས་ནི་མཚམས་དེར་གཏོགས་པའི་དགེ་འདུན་ལྔ་ལ་སོགས་པ་ཐམས་ཅད་ལས་བཤགས་པས་ལྡང་བར་འགྱུར་རོ། །

[Block 2597]
ལྷག་མ་མེད་པར་གཏོགས་པའི་སྦོམ་པོ་ལྕི་བ༌[^2423]ལས་ནི་མ་བཅད་པ་ལྷག་པ་ལའོ་ཞེས་བྱ་བ་ལ་ནི༌[^2424]ཕམ་པ་དེར་གཏོགས་པ་དེ་དང་འབྲེལ་བའི་སྦོམ་པོ་ལྕི་བ་ལས་ནི་མ་བཅད་པའི༌[^2425]དེའི་གནས་ཀྱི་གཞི་དེ་ཉེ་བར་སོན་པ་ལས་མཚམས་གཞན་དུ་ཁྱེར་བས༌[^2426]ཐམས་ཅད་དུ་དེའི་མཚམས་ཀྱི་ནང་དུ་གཏོགས་པའི་དགེ་འདུན་ལྔ་ལས་མང་བ་དྲུག་ལ་བཤགས་པས་ལྡང་བར་འགྱུར་རོ། །

[Block 2598]
ཡང་བ་དེ་ལས་བཞི་ལ་སོགས་པ་ལའོ་ཞེས་བྱ་བ་ནི་ལྷག་མ་མེད་པར་གཏོགས་པའི་སྦོམ་པོ་ཡང་བ་དེ་ལས་ནི་མཚམས་དེར་གཏོགས་པའི་དགེ༌[^2427]འདུན་མ་བཅད་པ་བཞི་ལ་སོགས་པ་ཐམས་ཅད་ལ་བཤགས་པས་ལྡང་བར་འགྱུར་རོ། །

[Block 2599]
དགེ་འདུན་ལྷག་མར་གཏོགས་པའི་སྦོམ་པོ་ལྕི་བ་དང་ཡང་བ་ཇི་ལྟར༌[^2428]ཤེས་པར་བྱ་ཞེ་ན། དེའི་དམིགས་ཀྱིས་བསལ༌[^2429]བ་མེད་པའི་ཕྱིར་དེ་དང་བཅས་པར་བཤགས་པ་ལས་གཅིག་ལ་ཆོ་ག་གཞན་འཇུག་པའོ། །

[Block 2600]
ལྕི་བ་དང་ཡང་བ་ཉིད་ཀྱང་ཁ་ན་མ་ཐོ་བ་མང་བ་དང་ཉུང་བ་ཉིད་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 2601]
དཔེར་ན་འཛག་སྣོད་དུ་ལས་སུ་མི་རུང་བའི་ཡན་ལག་གི་རྣམ་པ་ཉེད་པ་ལ་སོགས་པ་ཡང་བ་ཡིན་ནོ། །

[Block 2602]
བསྟེན་པར༌[^2430]བྱ་བ་མཐུ་མེད་པར་ཡན་ལག་རྩོལ་བ་དང་། རིན་ཐང་མ་ཚང་བའི་རྫས་མང་པོར་རྐུ་བ་ཡང་ལྕི་བའོ། །

[Block 2603]
འདིར་གཞུང་ནི་འདུལ་བྱེད་དག་ལས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་ཚེ་དང་ལྡན་པ་ཉེ་བ༌[^2431]འཁོར་གྱིས་ཞུས་པ། བཙུན་པ་ཉེས་པ་སྦོམ་པོ་ཇི་ལྟར་བཤགས་པར་བགྱི། ཉེ་བ༌[^2432]འཁོར་ཉེས་པ་སྦོམ་པོ་ནི་བཞི་པོ་འདི་དག་ཡིན་ནོ། །

[Block 2604]
ཕམ་པར་འགྱུར་བས་ཀུན་ནས་བསླང་བ་ལྕི་བ་དང་། ཕམ་པར་འགྱུར་བས༌[^2433]ཀུན་ནས་བསླང་བ་ཡང་བ་དང་། དགེ་འདུན་ལྷག་མས་ཀུན་ནས་བསླང་བའི་ལྕི་བ་དང་། དགེ་འདུན་ལྷག་མས་ཀུན་ནས་བསླང་བ་ཡང་བའོ། །

[Block 2605]
ཉེ་བ༌[^2434]འཁོར་དེ་ལ་ཀུན་ནས་བསླང་བ་ཕམ་པར་འགྱུར་བས་ཀུན་ནས་བསླང་བའི་ཉེས་པ་སྦོམ་པོ་ལྕི་བ་གང་ཡིན་པ་དེ་ནི་མཚམས་ཀྱི་ནང་དུ་དགེ་འདུན་དྲུག་ལ་སོགས་པ་ཐམས་ཅད་ཀྱི་མདུན་དུ་བཤགས་པར་བྱའོ། །

[Block 2606]
ཕམ་པར་འགྱུར་བ་ཀུན་ནས་བསླང་བའི་ཉེས་པ་ཡང་བ་གང་ཡིན་པ་དེ་ནི་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་དགེ་སློང་བཞིའི་མདུན་དུ་བཤགས་པར་བྱའོ། །

[Block 2607]
དེ་ལ་དགེ་འདུན་ལྷག་མས་ཀུན་ནས་བསླང་བའི་ཉེས་པ་སྦོམ་པོ་ལྕི་བ་གང་ཡིན་པ་དེ་ནི་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་དགེ་སློང་ལྔའི་མདུན་དུ་བཤགས་པར་བྱའོ། །

[Block 2608]
དགེ་འདུན་ལྷག་མས་ཀུན་ནས་བསླང་བའི་ཉེས་པ་སྦོམ་པོ་ཡང་བ་གང་ཡིན་པ་དེ་ནི་མཚམས་ཀྱི་ནང་དུ་དགེ་སློང་གཅིག་གི་མདུན་དུ་བཤགས་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2609]
མཐར་དེ་ལ་བརྩལ་བའི༌[^2435]རྐྱེན་མ་འབྱོར་བ་ཉིད་ན་ལས་བྱས་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་ཕྱིར་བཅོས་པ་ལའོ། །

[Block 2610]
བརྩལ་བའི༌[^2436]རྐྱེན་མ་འབྱོར་བ་ཉིད་ནི་ཞེས་བྱ་བ་ལ་མཐར་ཞེས་བྱ་བ་ནི་འཆི་བ་སྲིད་པའི་གནས་སྐབས་ཀྱི་འཆི་བའི་སྐད་ཅིག་མར་རོ། །

[Block 2611]
དེ་ལ་ཞེས་བྱ་བ་ནི་བཤགས་པ་ལ་སོགས་པ་ཕྱིར་བཅོས་པའི་ཕྱིར་བརྩལ་བ༌[^2437]ནི་ཕྱིར་བཅོས་པའི་ལས་བྱས་པ་དང་འདྲའོ། །

[Block 2612]
འདིར་གཞུང་ནི་དགེ་སློང་དག་དེ་ནི་ལྟུང་བ་དེ་ལས་ལངས་པ་ཡིན་ཏེ། ད་ནི་བསམ་པས་ལྟུང་བ་ལས་ལྡང་བར་སྨྲའི། ཆད་པའི་ལས་ཀྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་ཕྱིར་བཅོས་པར་བྱའོ་སྙམ་པ་ཡུལ་གཞན་དུ་སོང་བའི་སྐབས་སུ་སྲོག་དང་བྲལ་བར་གྱུར་པ་ནས་ཆད་པའི་ལས་ཀྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 2613]
ད་ནི་བསམ་པས་ལྟུང་བ་ལས་ལྡང་བར་སྨྲའི་ཞེས་སྨོས་པ་ནི་ཕྱིར་བཅོས་པ་ཐམས་ཅད་ཀྱི་ལྟུང་བྱེད་ཀྱི་དབང་དུ་བྱ་བའི་དོན་དུའོ། །

[Block 2614]
དགེ་འདུན་ལྷག་མའི་ཕྱིར་བཅོས་པ་ནི་ཐམས་ཅད་དུ་ལྕི་བ་སྟེ། དེ་བས་ན་དེ་ལས་འདི་ལྟར་ལྔ་པ་ཡོད་པ་ལ་སྡང་བ་ཞེས་བྱ་བ་ནི་སྦྱར་བར་བྱའོ། །

[Block 2615]
དེ་བས་ན༌[^2438]ཐམས་ཅད་ལ་དབང་དུ་བྱ་བའི་ཕྱིར་མདོ་འདིའོ། །

[Block 2616]
དུས་གཞན་དུ་ཡང་དེ་ལྟར་བླངས་པ་ཉིད་ལ་བཤགས་པ་ལ་སོགས་པའི་དོན་མེད་པར་ཐལ་བས་དེ་བས་ན་ནང་དུ་དེ་རྣམ་པར་གནས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 2617]
མི་ཟད་པའི་ཡིད་ལས་བྱུང་བ་རྗེས་སུ་སྦྱར་བའི་བསམ་པ་གཅིག་པུ་ལས་བཤགས་པར་བྱེད་པ་རྣམས་ལས་ལྡང་བར་རིགས་པ༌[^2439]ཡིན་ནོ། །

[Block 2618]
དོན་མེད་པ་ལ་ཡང་དེ་ལྟར་དེ། གཞན་དུ་ན་བཤགས་པ༌[^2440]ལ་སོགས་པ་ཐལ་བས་དེ་བས་ན་བརྩོན་པ༌[^2441]དང་བཅས་པ་ཉིད་ན་དེ་རྣམ་པར་གནས་པ་ཡིན་ཏེ། དེ་བས་ན་དེ་ཡང་འདི་བརྟེན་པའོ། །

[Block 2619]
བརྩོན་འགྲུས་དམན་པ་ལ་ཡང་བརྩོན་འགྲུས་དང་བཅས་པ་ཉིད་བསྟན་པའོ། །

[Block 2620]
ཡོད་པ་གང་ལ་ཡང་རྐྱེན་གཞན་མ་ཚང་བས་ཕྱིར་བཅོས་པ་མ་གྲུབ་པ་དེ་ལ་འདིར་ཡན་ལག་འདི་ཉིད་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2621]
དེ་བས་ན་རྐྱེན་མ་གྲུབ་པའི་ཕྱིར་སྨོས་པའོ། །

[Block 2622]
སྨྱོས་པས་བྱས་པ་དེའི་ཕྱིར༌[^2442]སངས་པ་ནི་ཉེས་བྱེད་དང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རང་བཞིན་ལས་ཉམས་པས་བྱས་པ་ཐམས་ཅད་ཉིད་ལ་ལྷག་པར་སྤྱད་པ་སངས་པ་རང་བཞིན་ཐོབ་པ་ཡོད་པ་ལ་བྱེད་པ་པོ་དེས་འདུ་ཤེས་པ་ནི་ཉེས་བྱེད་དང་འདྲ་བ་ཉིད་དོ། །

[Block 2623]
གཅིག་གི་མདུན་དུ་ཕྱིས་བཤགས་པ་ཉིད་དང་འདྲའོ། །

[Block 2624]
མི་བདེན་པ་བསལ་བའི་དོན་དུ་བཤགས་པ་དེ་རྣམ་པར་གནས་པ་ཡིན་གྱི་ཕྱིར་བཅོས་པ་ཉིད་ཀྱི་ཕྱིར་ལྟུང་བ་མི་ལྡང་བ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2625]
མིང་དང་རིགས་དང་ལྡན་པར་བརྗོད་ན་ལྟུང་བ་ལས་སོ་ཞེས་བྱ་བ་ནི་ལྡང་ངོ་ཞེས་བྱ་བར་དབང་དུ་བྱེད་པ་ལས་ཤེས་པར་བྱའོ། །

[Block 2626]
མིང་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་ཉེས་པ་སྦོམ་པོ་དང་། དགེ་འདུན་ལྷག་མ་དང་། སྤང་བའི་ལྟུང་བྱེད་དང་། ལྟུང་བྱེད་འབའ་ཞིག་པ་དང་། སོ་སོར་བཤགས་པར་བྱ་བ་དང་། ཉེས་བྱས་ཞེས་བྱ་བ་རྣམས་སོ། །

[Block 2627]
རིགས་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་མི་ཚངས་པར་སྤྱོད་པས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། བསམས་བཞིན༌[^2443]དུ་ཁུ་བ་འབྱིན་པས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། རེག་པས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། འཁྲིག་པ་སྨྲ་བས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། བསྙེན་བཀུར་བསྔགས་པས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། ཚིག་རྩུབ་པ༌[^2444]སྨྲ་བས་ཀུན་ནས་བསླང་བའི་བར་དང་། ཞག་བཅུ་ལས་འདའ་བས་ཀུན་ནས་བསླང་བ་དང་། བརྫུན་དུ་སྨྲ་བས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། དགེ་སློང་མའི་བསོད་སྙོམས་བྱིན་ལེན་བྱེད་པས་ཀུན་ནས་བསླང་བ་དང་། ཤམ་ཐབས་ཟླུམ་པོར་མ་བགོས་པས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དག་སྟེ། དེ་ལྟར་མིང༌[^2445]དང་རིགས་དང་ལྡན་པར་བརྗོད་པས་ལྟུང་བ་བཤགས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2628]
འདིར་བདག་ལས་བརྗོད་པ་ནི་སྔགས་ལས་ཤེས་པར་བྱ་སྟེ།

[Block 2629]
བདག་དགེ་སློང་མིང་འདི་ཞེས་བགྱི་བ་ལ་ལྟུང་བྱེད་ཀྱི་སྡེ་ཚན་ལས།

[Block 2630]
བརྫུན་དུ་སྨྲ་བས་ཀུན་ནས་བསླང་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་ལྟར་དེ་བརྗོད་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
