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
དེའི་ཕྱིར་དེ་དག་ནི་སེམས་ཅན་རྣམས་ཀྱི་གནས་པ༌[^1356]མ་ཡིན་ཏེ་བཙོན་ར་བཞིན་ནོ། །

[Block 2592 [HEADING]]
#### རྣམ་པར་ཤེས་པ་གནས་པ་བཞི། ^3-1-5-0

[Block 2593]
མདོ་གཞན་ལས་ནི་རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་ཞེས་གསུངས་སོ། །

[Block 2594]
གཞན་ལས་ནི་གནས་པ་དག་ནི་ཡང་བཞི་སྟེ། ཞེས་གསུངས་པ། བཞི་གང་ཞེ་ན། རྣམ་པར་ཤེས་པ་གནས་པ་གཟུགས་སུ་ཉེ་བར་འགྲོ་བ་དང་། ཚོར་བར་ཡང༌[^1357]ཉེ་བར་འགྲོ་བ་དང་། འདུ་ཤེས་སུ་ཉེ་བར་འགྲོ་བ་དང་། འདུ་བྱེད་དུ་ཉེ་བར་འགྲོ་བའོ། །

[Block 2595]
དེ་དག་གི་རང་བཞིན་ཅི་ཞེ་ན། དེ་དག་ནི་གོ་རིམས་བཞིན་དུ།

[Block 2596 [VERSE]]
ཟག་དང་བཅས་པའི་ཕུང་པོ་བཞི། །
དེ་དག་ཀྱང་རང་གི་ས་པ་ཉིད།
ས་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 2597]
ཅིའི་ཕྱིར་ཞེ་ན། གནས་པ་ནི༌[^1358]བརྟེན་པ་ཡིན་ན། སྐལ་བ་མི་མཉམ་པའི་ས་པའི་ཕུང་པོ་དག་ལ་ནི་རྣམ་པར་ཤེས་པ་སྲེད་པའི་དབང་གིས་མི་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 2598]
ཅིའི་ཕྱིར་རྣམ་པར་ཤེས་པ་ལ་རྣམ་པར་ཤེས་པ་གནས་པ་ཞེས་མི་བྱ་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་གནས་པ་པོ་ཡོངས་སུ་སྤངས་ནས་གནས་པ་ཞེས་བྱ་བ་མེད་པའི༌[^1359]ཕྱིར་ཏེ། གནས་པ་པོ་ཉིད་ལ་ནི་གནས་པ་ཞེས་མི་བྱ་སྟེ། དཔེར་ན་རྒྱལ་པོ་ཉིད་རྒྱལ་པོའི་བསྟན༌[^1360]མ་ཡིན་པ་བཞིན་ནོ། །

[Block 2599]
ཡང་ན་ཆོས་གང་དག་ལ་རྣམ་པར་ཤེས་པ་གནས་ནས་གྲུ་དང་མཉེན་པའི༌[^1361]ཚུལ་དུ་འགྲོ་བར་བྱེད་པའི་ཆོས་དེ་དག༌[^1362]རྣམ་པར་ཤེས་པ་གནས་པ་དག་ཅེས་བཤད་ན། རྣམ་པར་ཤེས་པ་ཉིད་རྣམ་པར་ཤེས་པ་ལ་གནས་ནས་འགྲོ་བར་བྱེད་པ་ནི་མ་ཡིན་པས་དེའི་ཕྱིར་མ་བཤད་དོ་ཞེས་ཟེར་རོ། །

[Block 2600]
འོ་ན་མདོ་ལས།

[Block 2601]
རྣམ་པར་ཤེས་པའི་ཟས་ལ་དགའ་བ་ཡང་ཡོད། འདོད་ཆགས་ཀྱང་ཡོད་དོ། །

[Block 2602]
གང་ལ་དགའ་བ་ཡོད་ཅིང་འདོད་ཆགས་ཡོད་པ་དེ་ལ་རྣམ་པར་ཤེས་པ་བརྟེན༌[^1363]ཅིང་གནས་སོ་ཞེས་གང་གསུངས་པ་དེ་ནི་ཇི་ལྟ་བུ། རྣམ་པར་ཤེས་པ་གནས་པ༌[^1364]བདུན་ཕུང་པོ་ལྔའི་རང་བཞིན་དག་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ཡང་ཇི་ལྟ་བུ། དེ་ལྟ་ན་འོ་ན་ནི་བྱེ་བྲག་མེད་པར་ནི་སྐྱེ་བའི་སྐྱེ༌[^1365]མཆེད་ཀྱིས་བསྡུས་པའི་ཕུང་པོ་དག་ལ་མངོན་པར་དགའ་བ་དང་བཅས་པའི་རྣམ་པར་ཤེས་པ་འཇུག་ན་རྣམ་པར་ཤེས་པ་ལ་རྣམ་པར་ཤེས་པ་གནས་པ་ཞེས་བྱའོ། །

[Block 2603]
སོ་སོར་དབྱེ་བ༌[^1366]ནི་ཇི་ལྟར་གཟུགས་ལ་སོགས་པ་རྣམ་པར་ཤེས་པ་ཀུན་ནས་ཉོན་མོངས་པར་བྱེད་པ་ཡིན་པ་ལྟར་རྣམ་པར་ཤེས་པ་འབའ་ཞིག་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་རྣམ་པར་ཤེས་པ་གནས་པ་བཞི་དག་ཏུ། རྣམ་ཤེས་འབའ་ཞིག་གནས་པར་མ་བཤད་དོ། །

[Block 2604]
གཞན་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་རྣམ་པར་ཤེས་པ་གནས་པ་བཞི་ནི་ཞིང་གི་ངོ་བོར་བསྟན་ལ། ཉེ་བར་ལེན་པ་དང་བཅས་པའི་རྣམ་པར་ཤེས་པ་ཟད་པར་ནི་ས་བོན་གྱི་ངོ་བོ་ཁོ་ནར་བསྟན་གྱི། ས་བོན་ཉིད་ས་བོན་གྱི་ཞིང་གི་ངོ་བོར་རྣམ་པར་གཞག་པར་གྱུར་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་དགོངས་པ་ཡོངས་སུ་བརྟག་གོ། །

[Block 2605]
ཆོས་གང་དག་རྣམ་པར་ཤེས་པ་དང་ལྷན་ཅིག་འབྱུང་བ་དེ་དག་ནི་འདིའི་ཞིང་གི་ངོ་བོར༌[^1367]ཤིན་ཏུ་ལེགས་པ་ཡིན་པས་དེ་དག་ཉིད་འདིའི་གནས་པ་དག་ཅེས་བཤད་དོ། །

[Block 2606]
ཡང་ཅི་རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་གྱིས་བཞི་བསྡུས་སམ། འོན་ཏེ་བཞིས་བདུན་བསྡུས་ཤེ་ན། བདུན་གྱིས༌[^1368]བཞི་ཡང་མ་ཡིན་ལ་བཞིས་ཀྱང་བདུན་མ་ཡིན་གྱི། བསྡུ་ན་མུ་ནི་བཞི་ཡིན་ནོ། །

[Block 2607]
བསྡུ་བ་དཔྱད་ན་བདུན་གྱིས་བསྡུས་ལ་བཞིས་མ་ཡིན་པ་ཡང་ཡོད་དེ་ཞེས་བྱ་བ་དེ༌[^1369]ལྟ་བུ་ལ་སོགས་པ་མུ༌[^1370]བཞིར་རིག་པར་བྱ་སྟེ། མུ་དང་པོ་ནི་བདུན་དག་ཏུ་རྣམ་པར་ཤེས་པ་གང་ཡིན་པའོ། །

[Block 2608]
གཉིས་པ་ནི་ངན་སོང་རྣམས་དང་། བསམ་གཏན་བཞི་པ་དང་། སྲིད་པའི་རྩེ་མོ་ན་རྣམ་པར་ཤེས་པ་མ་གཏོགས་པའི་ཕུང་པོ་རྣམས་སོ། །

[Block 2609]
གསུམ་པ་དག་ནི་བདུན་དག་ཏུ་ཕུང་པོ་བཞི་རྣམས་སོ། །

[Block 2610]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 2611 [HEADING]]
#### སེམས་ཅན་སྐྱེ་གནས་བཞི། ^3-1-6-0

[Block 2612]
འགྲོ་བ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་ཐ་དད་པའི་ཁམས་གསུམ་བཤད་པ་གང༌[^1371]ཡིན་པ།

[Block 2613 [VERSE]]
དེར་ནི་སྒོ་ང་ལས་སྐྱེས་སོགས། །
སེམས་ཅན་སྐྱེ་གནས་བཞི་དག་ཏུ། །

[Block 2614]
རིག་པར་བྱ་སྟེ། སྒོ་ང་ལས་སྐྱེས་པའི་སྐྱེ་གནས་དང་། མངལ་ནས་སྐྱེས་པའི་སྐྱེ་གནས་དང་། དྲོད་གཤེར་ལས་སྐྱེས་པའི་སྐྱེ༌[^1372]གནས་དང་། རྫུས་ཏེ་སྐྱེས་པའི་སྐྱེ༌[^1373]གནས་སོ། །

[Block 2615]
སྐྱེ་གནས་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་ཡིན་ཏེ། འདིར་སེམས་ཅན་རྣམས་འཆོལ་བར་འགྱུར་ཞིང་སྐྱེ་བ་ཐུན་མོང༌[^1374]པའི་ཕྱིར་འདྲ་བར༌[^1375]འགྱུར་བས་སྐྱེ༌[^1376]གནས་སོ། །

[Block 2616]
སྒོ་ང་ལས་སྐྱེས་པའི་སྐྱེ་གནས་གང་ཞེ་ན། སེམས་ཅན་གང་དག་སྒོ་ང་ལས་སྐྱེས་པ་རྣམས་ཏེ། འདི་ལྟ་སྟེ། ངང་པ་དང་། ཁྲུང་ཁྲུང་དང་། རྨ་བྱ་དང་། ནེ་ཙོ་དང་། རི་སྐེགས་ལ་སོགས་པ་ལྟ་བུའོ།[^1377] །མངལ་ནས་སྐྱེས་པའི་སྐྱེ༌[^1378]གནས་གང་ཞེ་ན། སེམས་ཅན་གང་དག་མངལ་ལས་སྐྱེས་པ་རྣམས་ཏེ། འདི་ལྟ་སྟེ། གླང་པོ་ཆེ་དང་། རྟ་དང་། བ་ལང་དང་། མ་ཧེ་དང་། བོང་བུ་དང་། ཕག་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2617]
དྲོད་གཤེར་ལས་སྐྱེས་པའི་སྐྱེ་གནས་གང་ཞེ་ན། སེམས་ཅན་གང་དག་འབྱུང་བའི་དྲོད་གཤེར་ལས་སྐྱེ་བ་རྣམས་ཏེ། འདི་ལྟ་སྟེ་སྲིན་བུ་དང་། སྦུར་པ་དང་། ཕྱེ་མ་ལེབ་དང་། སྦྲང་བུ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2618]
རྫུས་ཏེ་འབྱུང་བའི༌[^1379]སྐྱེ་གནས་གང་ཞེ་ན། སེམས་ཅན་གང་དག་དབང་པོ་མ་ཚང་བ་མ་ཡིན་ཞིང་དམན་པ་མ་ཡིན་ལ། ཡན་ལག་དང་ཉིང་ལག་ཐམས་ཅད་དང་ལྡན་པར་ཅིག་ཅར་དུ་སྐྱེ་བ་རྣམས་སོ། །

[Block 2619]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་དག་སྐྱེ་བ་ལ་མཛེས་པར་བྱེད་པའི་ཕྱིར་རྫུས་ཏེ་འབྱུང༌[^1380]བ་རྣམས་ཞེས་བྱ་སྟེ། འདི་ལྟ་སྟེ། ལྷ་དང་། དམྱལ་བ་དང་། སྲིད་པ་བར་མ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2620]
ཡང་འགྲོ་བ་གང་ན་སྐྱེ༌[^1381]གནས་དུ་ཞིག་ཡོད་ཅེ་ན། སྨྲས་པ། མི་དང་དུད་འགྲོ་རྣམ་པ་བཞི།[^1382] །མི་རྣམས༌[^1383]ནི་རྣམ་པ༌[^1384]བཞི་སྟེ། རེ་ཞིག་སྒོ་ང་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། ཁྲུང་ཁྲུང་མོ་ལས་སྐྱེས་པ་བྲག་དང་ཉེ་བྲག་དང་རི་དྭགས་འཛིན་གྱི་མའི་བུ༌[^1385]སུམ་ཅུ་རྩ་གཉིས་དང་། རྒྱལ་པོ་ལྔ་ལེན་གྱི་བུ་ལྔ་བརྒྱ་རྣམས་སོ། །

[Block 2621]
མངལ་ན༌[^1386]སྐྱེས་པ་ནི་ཇི་ལྟར་ད་ལྟར་གྱི་ལྟ་བུའོ། །

[Block 2622]
དྲོད་གཤེར་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། ང་ལས་ནུ་བ༌[^1387]དང་། མཛེས་པ་དང་། ཉེ་མཛེས་དང་། ཐི་བའི་ཕྲེང་བ་ཅན་དང་། ཨ་མྲ་སྐྱོང་མ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2623]
རྫུས་ཏེ་སྐྱེ་བ་ནི་བསྐལ་པ་དང་པོ་པ་རྣམས་ཁོ་ནའོ། །

[Block 2624]
དུད་འགྲོ་ཡང་རྣམ་པ་བཞི་སྟེ། རྣམ་པ་གསུམ་ནི་སྣང་བ་ཁོ་ནར་ཟད་དོ། །

[Block 2625]
རྫུས་ཏེ་སྐྱེ་བ་རྣམས་ནི་ཀླུ་དང་།

[Block 2626 [VERSE]]
འདབ་བཟངས་ལ་སོགས་པ་ལྟ་བུའོ། །
དམྱལ་བ་རྣམས་དང་ལྷ་རྣམས་དང་། །
སྲིད་པ་བར་མ་རྫུས་ཏེ་སྐྱེ། །

[Block 2627]
དམྱལ་བ་དང་། སྲིད་པ་བར་མ་པ༌[^1388]དང་། ལྷ་ཐམས་ཅད་ནི་རྫུས་ཏེ་སྐྱེ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 2628]
ཡི་དྭགས་མངལ་ནས་སྐྱེ་བ་ཡང་ཡིན། འདི༌[^1389]ཞེས་བྱ་བའི་སྒྲས་ནི་རྫུས་ཏེ་སྐྱེ་བ་དག་ཡིན་ནོ་ཞེས་བྱ་སྟེ། ཚེ་དང་ལྡན་པ་མཽད་གལ་གྱི་བུ་ཆེན་པོ་ལ་ཡི་དྭགས་མོ་ཞིག་ན་རེ།

[Block 2629 [VERSE]]
བདག་གིས་མཚན་མོ་བུ་ལྔ་དང་། །
དེ་བཞིན་ཉིན་མོ་གཞན་ལྔ་དག །
བསྐྱེད་ནས་དེ་དག་ཟ་མོད་ཀྱི། །
འོན་ཀྱང་བདག་ནི་ཚིམ་པ་མེད། །

[Block 2630]
ཅེས་སྨྲས་པའོ། །
--- END BLOCKS ---
