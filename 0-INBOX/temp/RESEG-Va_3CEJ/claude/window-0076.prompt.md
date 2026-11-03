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
[Block 2661]
རྒྱུན་ལ༌[^1425]མི་འཆད་པར་ཡུལ་གཞན་དག་ཏུ་འབྱུང་བར་བརྗོད་ཀྱི་རྒྱུན་མ་ཡིན་པ་ལ་ནི་མ་ཡིན་པས་དཔེ་མི་འདྲ་བ་ཡིན་ནོ། །

[Block 2662]
གཟུགས་བརྙན་ནི། གཉིས་ལས་འབྱུང་ཕྱིར། གཟུགས་བརྙན་ནི་གཟུགས་དང་མེ་ལོང་དང་རྒྱུ་གཉིས་ལས་འབྱུང་བར་འགྱུར་ཏེ། གཙོ་བོའི་རྒྱུ་གང་ཡིན་པ་དེ་ལ་བརྟེན་ནས་འབྱུང་ན། སྐྱེ་བའི་སྲིད་པ་ཡང་དེ་ལྟར་འཆི་བའི་སྲིད་པ་དང་། གཙོ་བོའི་རྒྱུ་གང་ཡང་རུང་བ་ཞིག་དང་རྒྱུ་གཉིས་ལས་འབྱུང་བ་ནི་མེད་དོ། །

[Block 2663]
[^1426]དེའི་ཕྱིར་ཡང་དེའི་འདི་ནི་མི་འདྲ་བ་ཡིན་ནོ། །

[Block 2664]
ཕྱིའི་ཁུ་ཆུ་དང་ཁྲག་ལ་སོགས་པ་སེམས་པ༌[^1427]མེད་པ་གཙོ་བོའི་རྒྱུ་ཡིན་པ༌[^1428]ཡང་རིགས་པ་མ་ཡིན་ཏེ། གང་དུ་རྫུས་ཏེ་སྐྱེ་བ་རྣམས་ནམ་མཁའ་ཁོ་ན་ལ་འབྱུང་བ་དེར་ཅི་ཞིག་ཡོངས་སུ་བརྟག །དེ་ལྟར་རེ་ཞིག་རིགས་པ་ལས་འཆི་བའི་སྲིད་པ༌[^1429]འབྱུང་བར་མི་འདོད་དོ། །

[Block 2665]
དེ་ལྟ་བས་ན་སྲིད་པ་བར་མ་ནི་ཡོད་པ་ཉིད་དོ། །

[Block 2666 [HEADING]]
###### ལུང་ལས་གྲུབ་པ། ^3-1-7-1-2-0

[Block 2667]
མགུར་ནས་གསུངས་ཕྱིར་ཡོད།

[Block 2668]
མདོ་ལས།

[Block 2669]
སྲིད་པ་ནི་བདུན་ཏེ། དམྱལ་བའི་སྲིད་པ་དང་། དུད་འགྲོའི་སྲིད་པ་དང་། ཡི་དགས་ཀྱི་སྲིད་པ་དང་། ལྷའི་སྲིད་པ་དང་། མིའི་སྲིད་པ་དང་། ལས་ཀྱི་སྲིད་པ་དང་། སྲིད་པ་བར་མའོ་ཞེས་གསུངས་སོ། །

[Block 2670]
མདོ་འདི་ནི་དེ་དག་མི་འདོན་ཏོ་ཞེ་ན། འོ་ན། དྲི་ཟ་ཞེས་བྱ་བ་འདི་ལས་ཏེ། གནས་གསུམ་མངོན་དུ་གྱུར་པས་མའི་མངལ་དུ་བུ་ཆགས་པར་གྱུར་ཏེ། མ་རུང་ཞིང་ཟླ་མཚན་དང་ལྡན་པ་དང་། ཕ་མ་ཆགས་པར་གྱུར་ཅིང་ཕྲད་པ་དང་། དྲི་ཟ་ཡང་ཉེ་བར་གནས་པར་གྱུར་ནའོ་ཞེས་གསུངས་པ། སྲིད་པ་བར་མ་མ་གཏོགས་པར༌[^1430]དྲི་ཟ་གཞན་གང་ཞིག་ཡིན། འདི་ཡང་དེ་དག་འདི་སྐད་དུ་མི་འདོན་ཏོ། །

[Block 2671]
འོ་ན་ཇི་ལྟར་ཞེ་ན། ཕུང་པོ་ཞིག་པ་ཉེ་བར་གནས་པར་གྱུར་ནའོ་ཞེས་འདོན་ཏོ། །

[Block 2672]
གལ་ཏེ་དེ་ལྟ་ན་ལྔ༌[^1431]ལེན་གྱི་བུའི་མདོ། ཁྱོད་ཀྱི༌[^1432]དྲི་ཟ་ཉེ་བར་གནས་པ་གང་ཡིན་པ་འདི་རྒྱལ་རིགས་སམ། བྲམ་ཟེ་འམ། རྗེའུ་རིགས་སམ། དམངས་རིགས་སམ། འོན་ཏེ་ཤར་ཕྱོགས་ནས་འོངས་པ་ཞིག་གམ། འོན་ཏེ་ལྷོ་དང་ནུབ་དང་། བྱང་ནས་འོངས་པ་ཞིག་ཤེས་སམ་ཞེས་བྱ་བ་ཇི་ལྟར་དྲང་། ཕུང་པོ་ཞིག་པ་ནི་འོང་བར་རུང་བ་མ་ཡིན་ནོ། །

[Block 2673]
འོན་ཏེ་འདི་ཡང་མི་འདོན་ཏོ་ཞེ་ན། འོ་ན།

[Block 2674]
སྔར་གསུངས། ཞེས་བྱ་བ་འདི་ལས་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་ཕྱིར་མི་འོང་བ་ནི་ལྔ་སྟེ། བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ༌[^1433]དང་། སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་དང་། མངོན་པར་འདུ་བྱེད་པ་མེད་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ༌[^1434]དང་། མངོན་པར་འདུ་བྱེད་པ་དང་བཅས་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ༌[^1435]དང་། གོང་དུ་འཕོ་བའོ་ཞེས་གསུངས་པ་སྲིད་པ་བར་མ་མེད་ན་ཇི་ལྟར་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ཞེས་བྱ་བར་འགྱུར། ཁ་ཅིག་ན་རེ་བར་མ་དོར་ཞེས་བྱ་བའི་ལྷ་དག་ཅིག་ཡོད་དོ་ཞེས་ཟེར་རོ། །

[Block 2675]
དེ་ལྟ་ན་སྐྱེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡང་ལྷ་དག་ཅིག༌[^1436]ཡིན་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 2676]
དེ་ལྟ་བས་ན་རྟོག་པ་འདི་ནི་བཟང་པོ་མ་ཡིན་ནོ། །

[Block 2677]
འགྲོ་མདོ་ཞེས་བྱ་བ་འདི་ལས་ཀྱང་འགྲུབ་སྟེ། སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་བདུན་ཞེས་བྱ་བའི་མདོ་ལས་ཀྱང་དུས་དང་ཡུལ་གྱི་ཁྱད་པར་གྱི་བྱེ་བྲག་གིས་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས༌[^1437]འདའ་བ་གསུམ་དུ་བཤད་དེ། དཔེར་ན་ཞོག་མའི༌[^1438]མེ་ཆུང་ངུ་མངོན་པར་འགྲུབ་བཞིན་དུ་འཆི་བར་འགྱུར་བ་དེ་ལྟ་བུ་ནི་དང་པོ་ཡིན་ནོ། །

[Block 2678]
དཔེར་ན་ལྕགས་ཀྱི་ཚ་ཚ་གནམ་དུ་ཡར་བ༌[^1439]བཞིན་དུ་འཆི་བར་འགྱུར་བ་དེ་ལྟ་བུ་ནི་གཉིས་པའོ། །

[Block 2679]
དཔེར་ན་ལྕགས་ཀྱི་ཚ་ཚ་གནམ་དུ་ཡར་ནས་ས་ལ་མ་ལྷུང་བ་ཉིད་དུ་འཆི་བར་འགྱུར་བ་དེ་ལྟ་བུ་ནི་གསུམ་པའོ་ཞེས་གསུངས་ལ། བར་མ་དོ་ཞེས་བྱ་བའི་ལྷ་ནི་ཡུལ་དང་དུས་ཀྱི་ཁྱད་པར་གྱི༌[^1440]ཐ་དད་པ་རྣམ་པ་གསུམ་པ༌[^1441]དེ་ལྟ་བུ་མེད་པས་འདི་ནི་རྟོག་པ་འབའ་ཞིག་ཏུ་ཟད་དོ། །

[Block 2680]
གཞན་དག་ན་རེ་གང་ཞིག་ཚེའི་ཚད་ཀྱི་བར་དུའམ། ལྷ་དང་ཉེ་བའི་བར་དུ་ཉོན་མོངས་པ་རྣམས༌[^1442]སྤོང་བར་བྱེད་པ་གང་ཡིན་པ་དེར༌[^1443]ནི་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ཡིན་ཏེ། དེ་ཡང་ཁམས་ཀྱི་གནས་སྐབས་པའམ། འདུ་ཤེས་ཀྱི་གནས་སྐབས་པའམ། རྣམ་པར་རྟོག་པའི་གནས་སྐབས་པ་ཞིག་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་སྟེ། དེས་ན་རྣམ་པ་གསུམ་ཡིན་ནོ། །

[Block 2681]
ཡང་ན་དང་པོ་ནི་གཟུགས་ཀྱི་ཁམས་སུ་རིས་མཐུན་པ་ཡོངས་སུ་བླངས་ནས་མྱ་ངན་ལས་འདའ་བ་ཡིན་ནོ། །

[Block 2682]
གཉིས་པ་ནི་ལྷ་རྣམས་ཀྱི་འབྱོར་པ་ཉམས་སུ་མྱོང་ནས་སོ། །

[Block 2683]
གསུམ་པ་ནི་ལྷ་རྣམས་ཀྱི་ཆོས་ཡང་དག་པར་འགྲོ་བའི་ནང་དུ་ཞུགས་ནས་སོ། །

[Block 2684]
སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་ཡང་དག་པར་འགྲོ་བ་མཆོག་ཏུ་ལྡན་པའི་ནང་དུ་ཞུགས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའམ། སྐྱེས་པ་ཙམ་ཁོ་ནར་མ་ཡིན་གྱི་ཚེ་ཕལ་ཆེར་བཅོམ་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའོ་ཞེས་ཟེར་ཏེ། དེ་དག་ཐམས་ཅད་ཀྱང་ཡུལ་དུ་འགྲོ་བའི་བྱེ་བྲག་མེད་པའི་ཕྱིར་ཞོག་མ༌[^1444]ལ་སོགས་པའི་དཔེ༌[^1445]དག་དང་། མི་འབྱོར་རོ། །

[Block 2685]
ཚེའི་ཚད༌[^1446]ཀྱི་བར་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་གཟུགས་མེད་པ་དག་ཏུ་ཡང་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་གསུངས་པར་འགྱུར་བ་ཞིག་ན།

[Block 2686 [VERSE]]
བསམ་གཏན་དག་གི༌[^1447]བཅུ་ཚན་བཞི། །
གཟུགས་མེད་དག་གི༌[^1448]བདུན་ཚན་གསུམ། །
འདུ་ཤེས་ཀྱི༌[^1449]ནི་དྲུག་ཚན་དུ། །

[Block 2687]
མཛད་ནས་ཚོམས་སུ་ཡང་དག་བསྡེབ།[^1450] །ཞེས་གསུངས་པའི་སྡོམ་གྱི་ཚིགས་སུ་བཅད་པ་འདི་ལས་ཀྱང་མི་འབྱུང་ངོ་། །དེ་ལྟ་བས་ན་དེ་དག་ཐམས་ཅད་ཀྱང་རྟོག་པ་ཙམ་དུ་ཟད་དོ། །

[Block 2688]
འོན་ཏེ་དེ་དག་ནི་མདོ་དེ་དག་ཀྱང་མི་འདོན་ཏོ་ཞེ་ན། སྟོན་པ་གང་ཡིན་པ་ནི་ཡོངས་སུ་མྱ་ངན་ལས་འདས། བསྟན་པ་འདིའི་འདྲེན་པ་ནི་མེད། རྣམ་པ་མང་པོ་ནི་ཐ་དད་ཀྱི་སྟེང་དུ་ད་དུང་ཡང་ཚིག་དང་དོན་ལ་དགའ་དགུར༌[^1451]བྱེད་ན་གོ། །

[Block 2689]
ང༌[^1452]ཅི་ཞིག་བྱར་ཡོད་དེ་རེ་ཞིག་གང་དག་ལ་ལུང་འདི་ཚད་མ་ཡིན་པ་དེ་དག་ལ་ནི་ལུང་ལས་ཀྱང་སྲིད་པ་བར་མ་གྲུབ་བོ། །

[Block 2690]
འོ་ན་མདོ་ལས།

[Block 2691]
དེ་ནས་བདུད་སུན་འབྱིན་བྱེད་རང་གི་ལུས་ཁོ་ནས་མནར་མེད་པའི་དམྱལ་བ་ཆེན་པོར་ལྷུང་ངོ་ཞེས་གང་གསུངས་པ་ཇི་ལྟར་དྲང་འདིར་དགོས་པ༌[^1453]ནི་དེ་གསོན་པོ་ཁོ་ནར་དམྱལ་བའི་མེ་དག་གིས་བསྐོར་ཏེ་ཤི་ནས་སྲིད་པ་བར་མས་མནར་མེད་པར་སོང་ངོ་སྙམ་དུ་དགོངས་པ་ཡིན་ནོ། །

[Block 2692]
ལས་ཤིན་ཏུ་དྲག་པོ་ཡོངས་སུ་རྫོགས་པ་རྣམས་ནི་ལུས་འདོར་བ་ལ་མི་སྡོད་པས་དེའི་ཕྱིར་འདིའི་མཐོང་བའི་ཆོས་ལ་མྱང་བར༌[^1454]འགྱུར་བའི་ལས་ནི་དང་པོར་སྨིན་ལ། སྐྱེས་ནས་མྱོང་བར་འགྱུར་བའི་ལས་ནི་ཕྱིས་སྨིན་ཏེ། [^1455]ད་ནི་མཚམས་མེད་པ་ལྔའི་ལས་གང་དག་བྱས་ཤིང་བསགས་ནས་དེ་མ་ཐག་ཏུ་དམྱལ་བ་དག་ཏུ་སྐྱེའོ་ཞེས་གསུངས་པ་འདི་ཇི་ལྟར་དྲང་། དགོངས་པ་ནི་འགྲོ་བ་གཞན་དུ་མི་འགྲོ་བར་ཞེས་བྱ་བ་ཡིན་ཏེ། དེར་ནི་སྐྱེས་ནས་མྱོང་བར་འགྱུར་བའི་ལས་སུ་གསུངས་སོ། །

[Block 2693]
འོན་ཏེ་སྒྲ་ཇི་བཞིན་དུ་བརྟགས༌[^1456]ན་ནི་ལྔ་ཁོ་ན་བྱས་ནས་ཡིན་གྱི་གཅིག་ཅེས་བྱ་བར་ཡང་མི་འགྱུར་ལ། བྱས་མ་ཐག་ཏུ་ཡིན་གྱི་དུས་གཞན་གྱི་བར་དུ་གསོན་པོར་འདུག་ནས་ཀྱང་མ་ཡིན་ནོ། །

[Block 2694]
སྲིད་པ་བར་མ་སྐྱེ་བ་ཉིད་ཡིན་པར་གོ་སུ་ཞིག་མི་འདོད་དེ། འདི་འཆི་བའི་སྲིད་པའི་མཇུག་ཐོགས་སུ་སྐྱེ་བ་ལ་མངོན་དུ་ཕྱོགས་པའི་ཕྱིར་སྲིད་པ་བར་མ་ཁོ་ནས་དམྱལ་བ་དག་ཏུ་སྐྱེ་བ༌[^1457]ཡིན་གྱི་སྐྱེས་པ་ཡིན་ནོ་ཞེས་ནི་མི་སྨྲའོ། །

[Block 2695]
འོ་ན།

[Block 2696 [VERSE]]
བྲམ་ཟེ་ན་ཚོད་ཁྱེར་ཟིན་རྒ་བ་དང་། །
ན་བ་ཡིན་ཏེ་གཤིན་རྗེའི་དྲུང་དུ་ཕྱིན། །
བར་ན་ཁྱོད་ཀྱི་གནས་ཀྱང་ཡོད་མིན་ཞིང་། །
ཁྱོད་ཀྱི་ལམ་བརྒྱགས༌[^1458]ཀྱང་ནི་ཡོད་མ་ཡིན། །

[Block 2697]
ཞེས་གསུངས་པའི་ཚིགས་སུ་བཅད་པ་འདི་ཇི་ལྟར་དྲང་། འདིར་ཡང་དགོངས་པ་ནི་མི་དག་གི་ནང་ན་གནས་སུ་མེད་དོ་སྙམ་པ་ཡིན་ནོ། །

[Block 2698]
ཡང་ན་སྐྱེ་བའི་ཡུལ་དུ་ཕྱིན་པར་བྱ་བའི་ཕྱིར་དང༌[^1459]འགྲོ་བ་ལ་བགེགས་བྱེད༌[^1460]པ་མེད་པའི་ཕྱིར་སྲིད་པ་བར་མ་ན་ཡང་འདི་གནས་པ་མེད་དོ་སྙམ་པ་ཡིན་ནོ། །

[Block 2699]
འདི་ལ་འདི་ནི་དགོངས་པ་ཡིན་གྱི་འདི་ནི་དགོངས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ག་ལས་བརྟགས་པ༌[^1461]འདི་ནི་ཁྱོད་ལ་ཡང་མཚུངས་ཏེ། དེ་ལྟ་བས་ན་གཉི་གའི་ཕྱོགས་ལ་ཡང་ཇི་སྐད་གསུངས་པའི་མདོ་མི་འགལ་བའི་ཕྱིར་འདི་ནི་སྲིད་པ་བར་མ་མེད་པའི་ཁུངས་མ་ཡིན་ནོ། །

[Block 2700]
ཁུངས་ཞེས་བྱ་བ༌[^1462]ནི་ཤེས་པར་བྱེད་པ་གཞན་དུ་ཤེས་པར་མི་བྱེད་པ་ཡིན་ནོ། །
--- END BLOCKS ---
