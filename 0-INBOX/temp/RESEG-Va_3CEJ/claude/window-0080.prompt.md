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
[Block 2801]
ཡང་ན་འབྱུང་བར་འགྱུར་བའི་མིང་གིས་བསྟན་ཏེ། དཔེར་ན་མདོ་ལས་འདུས་བྱས་མངོན་པར་འདུ་བྱེད་དོ་ཞེས་གསུངས་པ་དང་། འཇིག་རྟེན་ན་འབྲས་ཆན་འཚེད་དོ། །

[Block 2802]
ཕྱེ་འཐག་གོ་ཞེས་པ༌[^1538]ལྟ་བུ་སྟེ། དེ་ལྟ་བས་ན་དེ་ནི་ཉེས་པ་མེད་དོ། །

[Block 2803]
ཡང་ཇི་ལྟར་ན་ཤེས་བཞིན་མ་ཡིན་པར་མའི་མངལ་དུ་འཇུག་ཅིང་འབྱུང་བའི་བར་དུ་ཡིན་པའམ། ཇི་ལྟར་ན་ཤེས་བཞིན་དུ་ཡིན་ཞེ་ན། རེ་ཞིག་སེམས་ཅན་དབང་ཐང་ཆུང་བར་གྲགས་པ་མའི་མངལ་དུ་འཇུག་པ་ལ་འདི་སྙམ་དུ་རླུང་ལངས་པའམ། ཆར་པ་འབབ་པ་འམ། གྲང་བའམ། ཡུལ་ངན་ནམ། སྐྱེ་བོ་ཕལ་པོ་ཆེའི་ཚོགས་ཀུ་ཅོ་འདོན་པ་སྙམ་བྱེད་ནས། མ་ལ་རྩྭ་ཐིབས་པོའམ། ནགས་ཐིབས་པོའམ། རྩྭའི་སྤྱིལ་པོའམ། ལོ་མའི་སྤྱིལ་པོར་འཇུག་པའམ། ཤིང་དྲུང་ངམ། རྩིག་པའི་དྲུང་དུ་འགྲོའོ། །

[Block 2804]
གནས་ན་ཡང་འདི་དག་ཏུ་གནས་པར་བྱའོ། །

[Block 2805]
འབྱུང་ན་ཡང་འདི་དག་ནས་འབྱུང་ངོ་སྙམ་དུ་ལོག་པའི་འདུ་ཤེས་དང་མོས་པ་དག་འབྱུང་བར་འགྱུར་རོ། །

[Block 2806]
སེམས་ཅན་དབང་ཐང་ཆེ་བར་གྲགས་པ་ནི་ཀུན་དགའ༌[^1539]ར་བའམ། སྐྱེད་མོས་ཚལ་ལམ། ཁང་བཟངས་སུ་འཇུག་པའམ། ཁང་པ་བརྩེགས་པའམ། ཁྲི་ལ་འཛེག་གོ། །

[Block 2807]
དེ་བཞིན་དུ་གནས་སོ། །

[Block 2808]
འབྱུང་ངོ་སྙམ་དུ་སེམས་སོ། །

[Block 2809]
རེ་ཞིག་ཤེས་བཞིན་མ་ཡིན་པར་འཇུག་པ་ནས་འབྱུང་བའི་བར་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །ཤེས་བཞིན་ཡིན༌[^1540]པ་ནི་མའི་མངལ་ལ༌[^1541]འཇུག་གོ། །

[Block 2810]
དེ་ཉིད་དུ་གནས་སོ། །

[Block 2811]
དེ་ཉིད་ནས་འབྱུང་ངོ་སྙམ་དུ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་བར་དུ༌[^1542]རབ་ཏུ་ཤེས་ཏེ། འདི་ལ་ཕྱིན་ཅི་ལོག་གི་འདུ་ཤེས་དང་མོས་པ་དག་མི་འབྱུང་ངོ་། །ཡང་འདིར་བསྟན་པ་དང་།

[Block 2812 [VERSE]]
[^1543]མངལ་དུ་འཇུག་པ་གསུམ་དག་སྟེ། །
འཁོར་ལོས་སྒྱུར་དང་རང་བྱུང་གཉིས། །

[Block 2813]
འཁོར་ལོས་སྒྱུར་བ་དང་། རང་བྱུང་རང་སངས་རྒྱས་དང་། རྫོགས་པའི་སངས་རྒྱས་དག་སྟེ། འོག་ནས་གོ་རིམས༌[^1544]ཞེས་འཆད་པར་འགྱུར་རོ། །

[Block 2814]
དེ་ལ་འཁོར་ལོས་སྒྱུར་བ་ནི་དང་པོ་སྟེ། དེ་ནི་འཇུག་པ་ཁོ་ན༌[^1545]ཤེས་བཞིན་ཡིན་གྱི་གནས་པ་ཡང༌[^1546]མ་ཡིན་ལ། འབྱུང་བ་ཡང་མ་ཡིན་ནོ། །

[Block 2815]
རང་སངས་རྒྱས་ནི་གནས་པ་ཡང་ངོ་། །སངས་རྒྱས་ནི་འབྱུང་བ་ཡང་ངོ་། །འདིར་ཡང་འབྱུང་བར་འགྱུར་བའི་མིང་གིས་བསྟན་ཏོ། །

[Block 2816 [VERSE]]
ལས་སམ་ཡེ་ཤེས་སམ་གཉི་ག །
རྒྱ་ཆེའི་ཕྱིར་ན་གོ་རིམས་བཞིན། །

[Block 2817]
ལས་རྒྱ་ཆེན་པོ་བསོད་ནམས་རྒྱ་ཆེན་པོ་བྱེད་པ་རྣམས་ནི་དང་པོ་ཡིན་ནོ། །

[Block 2818]
ཡེ་ཤེས་རྒྱ་ཆེན་པོ་ཐོས་པ་མང་བ་དང་རབ་ཏུ་འབྱེད་པ་བྱས་པ་རྣམས་ནི་གཉིས་པ་ཡིན་ནོ། །

[Block 2819]
བསོད་ནམས་ཀྱི་ལས་དང་ཡེ་ཤེས་རྒྱ་ཆེ་བ་རྣམས་ནི་གསུམ་པ་ཡིན་ཏེ། དེ་ལྟ་བུར་གྱུར་པ་དེ་དག༌[^1547]ནི་རིམ་བཞིན་དུ་འཁོར་ལོས་སྒྱུར་བ་ལ་སོགས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2820]
ལྷག་མ་རྣམས་ནི་བཞི་པ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པོ། །

[Block 2821 [HEADING]]
#### བདག་མེད། ^3-1-8-0

[Block 2822]
ད་ནི་འདིར་ཕྱི་རོལ་པ་རྣམས་གལ་ཏེ་སེམས་ཅན་འཇིག་རྟེན་གཞན་དུ་འཕོའོ་ཞེས་བྱ་བར་དམ་བཅའ་ན་བདག་གྲུབ་པ་ཡིན་ནོ་ཞེས་བདག་ཏུ་སྨྲ་བ་ཡོངས་སུ་བཟུང་ནས་རྒོལ་ཏེ། དེ་དགག་པའི་ཕྱིར། བདག་མེད་ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 2823]
བདག་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། གང་ཕུང་པོ་འདི་དག་འདོར་ཞིང་ཕུང་པོ་གཞན་དག་ཏུ་ཉིང་མཚམས་སྦྱོར་རོ་ཞེས་བྱ་བར་ཡོངས་སུ་རྟོག་པ་ནང་གི་བྱེད་པའི་སྐྱེས་བུ་དེ་ལྟ་བུ་དེ་མེད་དེ་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ། ལས་ནི་ཡོད་དོ། །

[Block 2824]
རྣམ་པར་སྨིན་པ་ནི་ཡོད་དོ། །

[Block 2825]
ཆོས་སུ༌[^1548]བརྡར་བཏགས་པ་མ་གཏོགས་པ་གང་ཕུང་པོ་འདི་དག་འདོར་ཞིང་ཕུང་པོ་གཞན་དག་ཏུ་ཉིང་མཚམས་སྦྱོར་བར་བྱེད་པའི་བྱེད་པ་པོ་ནི་མི་དམིགས་སོ། །

[Block 2826]
དེ་ལ་ཆོས་སུ་བརྡར་བཏགས་པ་ནི་འདི་ཡིན་ཏེ། འདི་ལྟ་སྟེ་འདི་ཡོད་པས་འདི་འབྱུང་བའོ་ཞེས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྒྱས་པར་གསུངས་སོ། །

[Block 2827]
འོ་ན་བདག་ཇི་ལྟ་བུ་ཞིག་མི་དགག་ཅེ་ན། ཕུང་པོ་ཙམ་ཉིད་དོ། །

[Block 2828]
གལ་ཏེ་ཕུང་པོ་ཙམ་ཁོ་ན་ལ་བདག་ཅེས་འདོགས་ན་དེ་ལ་ནི་དགག་པ་མེད་དོ། །

[Block 2829]
དེ་ལྟ་ན་འོ་ན་ཕུང་པོ་བདག༌[^1549]ཉིད་འཇིག་རྟེན་གཞན་དུ་འཕོའོ་ཞེས་བྱ་བར་གྱུར་ཏོ་ཞེ་ན། དེ་དག་ནི་མི་འཕོ་བའི༌[^1550]ཕུང་པོ་ཙམ་ནི། ཉོན་མོངས་ལས་ཀྱིས་མངོན་དུ༌[^1551]བྱས། །སྲིད་པ་བར་མའི་རྒྱུན་གྱིས་ན།[^1552] །མར་མེ་བཞིན་དུ་མངལ་དུ་འགྲོ། །ཕུང་པོ་རྣམས་ནི་སྐད་ཅིག་མ་སྟེ། དེ་དག་ལ་ནི་འཕོ་བའི་མཐུ་མེད་ཀྱི་ཉོན་མོངས་པ་རྣམས་དང་། ལས་རྣམས་ཀྱིས་ཡོངས་སུ་བསྒོས་པའི༌[^1553]ཕུང་པོ་ཙམ་གྱིས་སྲིད་པ་བར་མ་ཞེས་བྱ་བའི་རྒྱུན་གྱིས་མའི་མངལ་དུ་འགྲོ་སྟེ། དཔེར་ན་མར་མེ་སྐད་ཅིག་མ་ཡིན་ཡང་རྒྱུན་གྱིས་ཡུལ༌[^1554]གཞན་དུ་འགྲོ་བ་ལྟ་བུ་ཡིན་པས༌[^1555]དེ་ནི་ཉེས་པ་མེད་དོ། །

[Block 2830]
དེ་ལྟ་བས་ན་བདག་མེད་བཞིན་དུ་ཡང་ཉོན་མོངས་པ་དང་། ལས་རྣམས་ཀྱིས་མངོན་པར་འདུས་བྱས་པའི་ཕུང་པོ་རྣམས་ཀྱི༌[^1556]རྒྱུན་མའི་མངལ་དུ་འཇུག་གོ་ཞེས་བྱ་བ་འདི་གྲུབ་བོ། །

[Block 2831]
དེ་ཡང་།

[Block 2832 [HEADING]]
#### ཇི་ལྟར་འཕངས་བཞིན་རིམ་གྱིས་རྒྱུན་སྐྱེ་བ། ^3-1-9-0

[Block 2833 [VERSE]]
ཇི་ལྟར་འཕངས་བཞིན་རིམ་གྱིས༌[^1557]རྒྱུན། །
སྐྱེས་ནས་ལས་དང་ཉོན་མོངས་ཀྱིས། །
འཇིག་རྟེན་ཕ་རོལ་དག་ཏུ་འགྲོ། །

[Block 2834]
ཚེའི་ལས་ཐ་དད་པའི་ཕྱིར་ཕུང་པོའི་རྒྱུན་ཐམས་ཅད་ཀྱི་འཕེན་པ་འདྲ་བ་ནི་མ་ཡིན་ཏེ།[^1558] དེའི་ཕྱིར་གང་ཞིག་ཇི་སྲིད་དུ་འཕངས་པ་དེ་དེ་སྲིད་དུ་རིམ་གྱིས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2835]
རིམ་པ་གང་གིས་ཤེ་ན།

[Block 2836]
གཙུག་ལག་ལས།

[Block 2837 [VERSE]]
དང་པོར་ནུར་ནུར་པོ་ཡིན་ནོ། །
ནུར་ནུར་པོ་ལས་མེར་མེར་སྐྱེ། །
མེར་མེར་པོ་ལས་ནར་ནར་སྐྱེ། །
ནར་ནར་པོ་ལས་མཁྲང་འགྱུར་སྐྱེ། །

[Block 2838]
མཁྲང་ལས་རྐང་ལག་འགྱུས་པ་འདྲ།[^1559] །སྐྲ་སྤུ་སེན་མོ་ལ་སོགས་པ།[^1560] །

[Block 2839 [VERSE]]
དབང་པོ་གཟུགས་ཅན་རྣམས་དང་ནི། །
མཚམས་རྣམས༌[^1561]རིམ་གྱིས་སྐྱེ་བར་འགྱུར། །

[Block 2840]
ཞེས་འབྱུང་ངོ་། །ནུར་ནུར་པོ་དང་། མེར་མེར་པོ་དང་། ནར་ནར་པོ་དང་། མཁྲང་འགྱུར་དང་། རྐང་ལག་འགྱུས་པའི་གནས་སྐབས་དེ་དག་ནི་མངལ་གྱི་གནས་སྐབས་ལྔ་ཡིན་ནོ། །
--- END BLOCKS ---
