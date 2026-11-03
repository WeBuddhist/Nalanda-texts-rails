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

[Block 2631]
སྐྱེ་གནས་ཐམས་ཅད་ཀྱི་ནང་ན་བཟང་བ༌[^1390]གང་ཡིན་ཞེ་ན། རྫུས་ཏེ་སྐྱེ་བ་ཡིན་ནོ། །

[Block 2632]
འོ་ན་ཅིའི་ཕྱིར་སྲིད་པ་ཐ་མ་པའི་བྱང་ཆུབ་སེམས་དཔའ་སྐྱེ་བ་ལ་དབང་ཐོབ་པ་ཡང་མངལ་ནས་སྐྱེ་བའི་སྐྱེ་གནས་ལ་བརྟེན་ཅེ་ན། དེ་ལྟར་མཛད་ན་དོན་ཆེན་པོ་གཟིགས་པ་ཡིན་ཏེ། ཉེ་དུ་དང་འབྲེལ་པས་ཤཱཀྱའི་རིགས་ཆེན་པོ་ཆོས་ལ་གཟུད་པའི་ཕྱིར་དང་། འདི་ནི་འཁོར་ལོས་སྒྱུར་བའི་རིགས་ཡིན་ནོ་ཞེས་གཞན་དག་རིམ་གྲོ་བསྐྱེད་དུ་གཞུག་པའི་ཕྱིར་དང་། མིར་གྱུར་པ་དག་གིས་ཀྱང་གྲུབ་པ་འདི་ཐོབ་པོ་ཞེས་གདུལ་བྱ་རྣམས་སྤྲོ་བ་བསྐྱེད་པའི༌[^1391]ཕྱིར་རོ། །

[Block 2633]
དེ་ལྟ་མ་ཡིན་ཏེ། རིགས་དང་གདུང་མེད་ན། ཇི་ལྟར་གཞན་མུ་སྟེགས་ཅན་ན་རེ་བསྐལ་པ་བརྒྱར༌[^1392]འདས་ནས་སྒྱུ་མ་མཁན་འདི་ལྟ་བུ་ཞིག་འཇིག་རྟེན་དུ་བྱུང་ནས་སྒྱུ་མས་འཇིག་རྟེན་ཟའོ་ཞེས་ཁ་ཟེར་བ་ལྟར་འདི་སུ་ཞིག་ཡིན། སྒྱུ་མའི་སྐྱེས་བུའམ། འོན་ཏེ་ཤ་ཟ་ཞིག་ཅེས་དེ་སྙམ་དུ་ཡོངས་སུ་རྟོག་པར་འགྱུར་རོ། །

[Block 2634]
གཞན་དག་ན་རེ་གང་དག་ལ་མི་རྣམས་དང་། གཞན་དག་གིས་མཆོད་པ་བྱས་ནས། སྟོང་ཕྲག་གིས་མཐོ་རིས་དང་བྱང་གྲོལ་འཐོབ་པ་རིང་བསྲེལ་སྐུ་གདུང་རྣམས་བཞག་པའི་ཕྱིར་ཏེ། རྫུས་ཏེ་སྐྱེ་བའི་སེམས་ཅན་རྣམས་ལ་ནི་ཕྱིའི་ས་བོན་མེད་པའི་ཕྱིར་ཤི་བ་རྣམས་ཀྱི་ལུས་མི་གནས་ཏེ། ཐོ་རངས༌[^1393]ཀྱི་ཏིལ་མར་གྱི་མར་མེ་ཤི་བར་གྱུར་པ་བཞིན་ནོ་ཞེས་ཟེར་ཏེ། བཅོམ་ལྡན་འདས་ཀྱི་བྱིན་གྱི་རླབས༌[^1394]ལས་བྱུང་བའི་རྫུ་འཕྲུལ་ཡིན་པར་འདོད་པ་རྣམས་ལ་ནི་ལན་དེ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2635]
དྲི་བ་ལས་དྲི་བ་གཞན་འབྱུང་སྟེ། གལ་ཏེ་རྫུས་ཏེ་སྐྱེ་བ་རྣམས་ཀྱི་ལུས་ཞིག་པ་མེད་ན། ཇི་ལྟར་མདོ་ལས་རྫུས་ཏེ་སྐྱེ་བའི་ནམ་མཁའ་ལྡིང་གིས་རྫུས་ཏེ་སྐྱེ་བའི་ཀླུ་བཟའ་བའི་ཕྱིར་འབྱིན༌[^1395]ཏོ་ཞེས་གསུངས་ཤེ༌[^1396]ན། ཟའོ་ཞེས་ནི་མ༌[^1397]གསུངས་པས་མ་ཤེས་ནས་བཟའ་བའི་ཕྱིར་འབྱིན་པས་ཉེས་པ་མེད་དོ། །

[Block 2636]
ཡང་ན་ཇི་སྲིད་མ་ཤིའི་བར་དུ་ཟ་བར་བྱེད་ཀྱི་ཤི་བ་དེའི་ཚིམ་པར་འགྱུར་བ་ནི་མ་ཡིན་ནོ། །

[Block 2637]
སྐྱེ་གནས་ཐམས་ཅད་ཀྱི་ནང་ནས་མང་བ་གང་ཡིན་ཞེ་ན། རྫུས་ཏེ་སྐྱེ་བ་ཡིན་ཏེ། དེ་ནི་འགྲོ་བ་གཉིས་དང་གསུམ་གྱི་ཕྱོགས་དང་། སྲིད་པ་བར་མ་ཐམས་ཅད་ཡིན་ནོ། །

[Block 2638 [HEADING]]
#### སྲིད་པ་བར་མ། ^3-1-7-0

[Block 2639]
སྲིད་པ་བར་མ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན། འདིར་གང་འཆི་དང་སྐྱེ་བ་ཡིན།[^1398] །སྲིད་པའི་བར་དུ་འབྱུང་བའོ། །

[Block 2640]
ལུས་གང༌[^1399]ཡུལ་གཞན་དུ་སྐྱེ་བ་ཐོབ་པར་བྱ་བའི་ཕྱིར་འཆི་བའི་སྲིད་པ་དང་སྐྱེ་བའི་སྲིད་པའི་བར་དུ་མངོན་པར་འགྲུབ་པ་དེ་ནི་སྲིད་པ་བར་མ་ཞེས་བྱ༌[^1400]སྟེ། འགྲོ་བའི་བར་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2641]
ཇི་ལྟར་ན་འདི་སྐྱེ་བ་ཡང་ཡིན་ལ་བྱུང་བ་ཡང་མ་ཡིན་ཞེ་ན།

[Block 2642 [VERSE]]
བགྲོད་པའི་ཡུལ་དུ་མ་ཕྱིན༌[^1401]ཕྱིར། །
སྲིད་པ་བར་མ་བྱུང་བ་མིན། །

[Block 2643]
སོན་པ་ནི་བྱུང་བ་ཡིན་ན་སྲིད་པ་བར་མ་འདི་ནི་བགྲོད་པར་བྱ་བའི་ཡུལ་དུ་སོན་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་བྱུང་བ་མ་ཡིན་ནོ། །

[Block 2644]
བགྲོད་པར་བྱ་བའི་ཡུལ་དེ་གང་ཞིག་ཅེ་ན། གང་དུ་རྣམ་པར་སྨིན་པས༌[^1402]འཕངས་པ་མངོན་ཞིང་རྫོགས་པའོ། །

[Block 2645 [HEADING]]
##### སྲིད་པ་བར་མ་ཡོད་པ། ^3-1-7-1-0

[Block 2646]
སྡེ་པ་གཞན་དག་ན་རེ། འཆི་བའི་སྲིད་པ་ཆད་པ་ཁོ་ན་ལས་སྐྱེ་བའི་སྲིད་པ་འབྱུང་ངོ་ཞེས་ཟེར་ཏེ། དེ་ནི་མི་འདོད་དོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། རིགས་པ་དང་ལུང་ལས་ཏེ། རེ་ཞིག་རིགས་པ་ལ་བརྟེན་ནས།

[Block 2647 [HEADING]]
###### རིགས་པ་ལ་བརྟེན་པ། ^3-1-7-1-1-0

[Block 2648 [VERSE]]
འབྲུའི་རྒྱུན་དང་ཆོས་མཐུན་ཕྱིར། །
སྲིད་པ་ཆད་ལས་འབྱུང་བ་མིན། །

[Block 2649]
རྒྱུན་གྱི༌[^1403]འཇུག་པའི་ཆོས་རྣམས་ནི་རྒྱུན་མི་འཆད་པར་ཡུལ་གཞན་དག་ཏུ་འབྱུང་བ་མཐོང་སྟེ། དཔེར་ན་འབྲུའི་རྒྱུན་ལྟ་བུའོ། །

[Block 2650]
དེ་ལྟ་བས་ན་སེམས་ཅན་གྱི་སེམས་ཀྱི་རྒྱུན༌[^1404]འདི་ཡང༌[^1405]མི་འཆད་པར་ཡུལ་གཞན་དུ་འབྱུང་བའི་ཆོས༌[^1406]ཅན་ཡིན་ནོ། །

[Block 2651]
ཆད་ནས་འབྱུང་བ་ཡང་མཐོང་སྟེ། དཔེར་ན་མེ་ལོང་ལ་སོགས་པ་དག་གི་ནང་དུ་གཟུགས་ལས་གཟུགས་བརྙན་ལྟ་བུའོ། །

[Block 2652]
དེ་བཞིན་དུ་འཆི་བའི་སྲིད་པ་ལས་ཀྱང་སྐྱེ་བའི་སྲིད་པ་རུང་ངོ་ཞེ་ན།

[Block 2653 [VERSE]]
གཟུགས་བརྙན་མ་གྲུབ་ཕྱིར་བ་དང་། །
མི་འདྲའི༌[^1407]ཕྱིར་ན་དཔེ་མ་ཡིན། །

[Block 2654]
གཟུགས་བརྙན་ཞེས་བྱ་བ་ཁ་དོག་གི་ཁྱད་པར་གཞན་ཁོ་ན་ཞིག་འབྱུང་ངོ་ཞེས་བྱ་བ་དེ་ནི་མ་གྲུབ་བོ། །

[Block 2655]
གྲུབ་ཏུ་ཟིན་ཀྱང་མི་འདྲ་བའི་ཕྱིར་དཔེ༌[^1408]མ་ཡིན་ནོ། །

[Block 2656]
རེ་ཞིག་ཇི་ལྟར་མ་གྲུབ་ཅེ་ན། གཅིག་ན་ལྷན་ཅིག་གཉིས་མེད་ཕྱིར། །ཡུལ་དེ་ཉིད་ན་མེ་ལོང་གི་གཟུགས་ཀྱང་སྣང་། གཟུགས་བརྙན་ཡང་སྣང་སྟེ། རྟེན་གྱི་འབྱུང་བ༌[^1409]ཐ་དད་པའི་ཕྱིར་ཡུལ་གཅིག་ཏུ་གཟུགས༌[^1410]གཉིས་ལྷན་ཅིག་འབྱུང་བ་ནི༌[^1411]མེད་དོ། །

[Block 2657]
དེ་བཞིན་དུ་ཕྱོགས་ཐ་དད་པ་ན༌[^1412]གནས་པ་རྣམས་ཀྱི༌[^1413]མཚེའུའི་ཆུ༌[^1414]ཡུལ་གཅིག་ན་རང་གི་མདུན་རོལ་གྱི་ཡུལ་ན་གནས་པའི་གཟུགས་རྣམས་ཀྱི་གཟུགས་བརྙན་ཕན་ཚུན་དམིགས་ཏེ། གཟུགས་གཅིག་ལ་ལྟ་བ་པོ་གཉིས་ཀྱིས་ལྷན་ཅིག་མི༌[^1415]མཐོང་བ་ནི་མ་ཡིན་པས་དེར་གཟུགས་གཞན་ཞིག༌[^1416]འབྱུང་བར་རིགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2658]
གྲིབ་མ་དང་ཉི་མ་གཉིས་ཀྱང་ལྷན་ཅིག་འབྱུང་བ་མ་མཐོང་བ༌[^1417]ན་གྲིབ་མ་ན་འདུག་པའི་མེ་ལོང་གི་ནང་ན་ཉི་མའི་གཟུགས་བརྙན་ཡང་དམིགས་པས་དེར་དེ་འབྱུང་བར༌[^1418]རིགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2659]
ཡང་ན། གཅིག་ན་ལྷན་ཅིག་གཉིས་མེད་ཕྱིར། །ཞེས་བྱ་བ་གཉིས་གང་ཞེ་ན། མེ་ལོང་གི་ངོས་དང་ཟླ་བའི་གཟུགས་བརྙན་ཏེ། མེ་ལོང་གི་ངོས་ཀྱང་གཞན་ཁོ་ན་ལ༌[^1419]ཡོད་ལ། ཟླ་བའི་གཟུགས་བརྙན་ནང་དུ་སོང་བ་ཡང་ཁྲོན་པའི་ཆུ་བཞིན་དུ་གཞན་ཁོ་ན་ན་སྣང་ངོ་། །དེ་ཡང་དེའི༌[^1420]ནང་དུ་འབྱུང་ན་ནི་གཞན་ན་དམིགས་པར་མི་འགྱུར་རོ། །

[Block 2660]
དེ་ལྟ་བས་ན་དེ་ནི་ཅུང་ཟད་ཀྱང་མེད་ཀྱི་གང་ཕྱིར༌[^1421]དེ་ལྟར་སྣང་བ་དེ་ནི་ཚོགས་ལ༌[^1422]དེའི་མཐུ་དེ་འདྲ་བ་ཡིན་ཏེ། ཆོས་རྣམས་ཀྱི་མཐུའི་བྱེ་བྲག་ནི་བསམ་གྱིས་མི་ཁྱབ་པོ། །རེ་ཞིག་མ་གྲུབ་པའི་ཕྱིར་ནི༌[^1423]དེ་ལྟ་བུ༌[^1424]ཡིན་ནོ། །ཇི་ལྟར་ན་མི་འདྲ་བའི་ཕྱིར་དཔེ་མ་ཡིན་ཞེ་ན། རྒྱུན་མིན་ཕྱིར། ཇི་ལྟར་འཆི་བའི་སྲིད་པ་སྐྱེ་བའི་སྲིད་པ་ལྟ་བུར་གཟུགས་བརྙན་ནི་གཟུགས་ཀྱི་རྒྱུན་དུ་གྱུར་པ་མ་ཡིན་ཏེ། མེ་ལོང་གི་རྒྱུད་དང་འབྲེལ་པའི་ཕྱིར་དང་། ལྷན་ཅིག་འབྱུང་བའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
