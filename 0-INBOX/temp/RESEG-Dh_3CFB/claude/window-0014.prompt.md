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
[Block 491]
ཁྱད་པར་དེ་ཙམ་ཁོ་ན་སྟོན་པར་བྱེད་པ་ན་དེ་ལྟ་བུའི་ཤེས་པར་བྱ་བའི་ཕྱིར་རོ།[^341] །བརྩེད་པ༌[^342]ཉིད་ཅེས་དེ་ལ་ཕན་པས་སྟོན་ཀྱང་རུང་། བརྩེད་པ༌[^343]ཞེས་བྱེད་པ་དང་ལྡན་པས་ཀྱང་རུང་། རང་གིས་བྱས་པའི་གཞུང་ལུགས་གཞན་གྱིས་ཀྱང་རུང་། དེ་སྐད་དུ་བརྗོད་པ་ཙམ་གྱིས་ནི་དེ༌[^344]དོན་གཞན་པ་ཉིད་དུ་འགྱུར་ཏེ། དེ་ལྟ་བུ་ཁོ་ན་ཤེས་པར་བྱ་བའི་ཕྱིར་སྒྲ་བརྡར་བྱས་པའི་ཕྱིར་རོ། །

[Block 492]
བརྩེད་པ༌[^345]ཉིད་ཅེས་བྱ་བ་འབྲེལ་པ་ལ་བྱ་བ་མ༌[^346]ཡིན་ནམ། འཚེད་པ་ཉིད་ནི་མ་ཡིན་ནོ་ཞེ་ན། ཇི་སྐད༌[^347]དུ་བརྗོད་པ་ལྟ་བུར་འཚེད་པ་དང་། འཚེད་པ་པོ་གཞན་འགའ་ཁོ་ན་ཞིག་བརྗོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 493]
འདིའི་བརྗོད་པར་བྱ་བ་གང་ཡིན་པ་དེ་ནི་བསྟན་ཟིན་ཏོ། །

[Block 494]
དེ་ཉིད་འཚེད་པས་ཀྱང་བརྗོད་དོ། །

[Block 495]
གཏིང་མི་ཚུགས་པ་ལོག་པའི་རྣམ་པར་རྟོག་པ་དག་གིས་ཆོག་གོ།[^348] །ཇི་ལྟར་བྱ་བ་དོན་གཞན་དུ་གྱུར་པའམ། དེ་དག་གི་འདུ་བ་མ་ཡིན་པ་དེ་ནི་འོག་ནས་ཤེས་པར་བྱའོ། །

[Block 496]
དེ་ཕྱིར་གཞན་སེལ་ཡུལ་ལ་ནི། །དེ་ལྡན་ཕྱོགས་ལ་བརྗོད་པ་བསལ།[^349] །

[Block 497 [VERSE]]
རིགས་དང་དེ་དང་ལྡན་པ་དག །
ཐ་དད་ཉིད་ན་ཉེས་པར་འགྱུར། །

[Block 498]
སྒྲའི་དོན་གཞན་སེལ་བ་ཅན་ལ་ཡང་དེས་ཁྱད་པར་དུ་བྱས་པ་བརྗོད་པའི་ཕྱིར། དེ་དང་ལྡན་པའི་ཕྱོགས་ལ་བརྗོད་པའི་ཐལ་བ་ཐམས་ཅད་མཚུངས་པར་འགྱུར་རོ། །ཞེས་སྨྲས་པ་གང་ཡིན་པ་དེ་ཡང་འདིས་བསལ་ཏེ། དེ་ལ་ནི་དོན་གཞན་ལ་བརྟེན་ནས་འཇུག་པའི་སྒྲ་རང་དབང་མེད་པ་ལ་སོགས་པའི་ཉེས་པས་གནོད་པར་འགྱུར་རོ། །

[Block 499]
གཞན་ལས་ལྡོག་པ་ནི་ལོག་པ་ལས་དོན་གཞན་པ་ཡང་མ་ཡིན་ཏེ། གཉི་གས་གཅིག་བརྗོད་པའི་ཕྱིར་རོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 500]
ད་ནི་ལོག་པ༌[^350]གཞན་གྱི་རྗེས་སུ་མི་འགྲོ་བའི་ཕྱིར། ཇི་ལྟར་གཞན་ལས་ལྡོག་པ་སྤྱི་ཡིན་ཞེ་ན། དེའི་བློ་ལ་དེ་ལྟར་སྣང་བའི་ཕྱིར་རོ། །

[Block 501]
སྤྱི་ཞེས་བྱ་བ་ནི་འགའ་ཡང་མེད་ཀྱི། སྒྲའི་རྟེན༌[^351]ཅན་གྱི་བློ་ཐོག་མ་མེད་པའི་བག་ཆགས་ཀྱི་མཐུས་ཆོས་མ་འདྲེས་པ་དག་ཀྱང་བསྲེ་ཞིང་སྐྱེའོ། །

[Block 502]
དོན་མེད་བཞིན་དུ་ཡང་དེ་སྣང་བའི་དབང་གིས་སྤྱི་དང་གཞི་མཐུན་པ་ཉིད་དུ་རྣམ་པར་གཞག་སྟེ། དོན་རྣམས་ལ་འབྲེལ་པ་དང་ཐ་དད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 503]
དེ་ཐམས་ཅད་ཀྱི་རྟེན་ནི༌[^352]དེའི་འབྲས་བུ་དང་རྒྱུ་ཅན་ཉིད་ཀྱིས་གཞན་དག་ལས་ཐ་དད་པའི་དོན་རྣམས་ཡིན་ལ། སྒྲས་ཀྱང་མི་འདོད་པ་སྤངས་ཏེ་འཇུག་པར་བྱེད་པ་གཞན་སེལ་བའི་ཡུལ་ཅན་དུ་བཤད་དེ། དེ་ལ་ཕྱི་རོལ་གྱི་དོན་གྱི་དེ་ཁོ་ན་ཉིད་ལ་མི་ལྟོས་པ་བློ་སྣང་བའི་དབང་གིས༌[^353]གཅིག་པུ་དུ་མ་ལས་ལོག་པ༌[^354]སྒྲ་རྣམས་དང་། དེ་ཉམས་སུ་མྱོང་བའི་བག་ཆགས་སད་པ་ལས་སྐྱེ་བ༌[^355]ཅན་གྱི་རྣམ་པར་རྟོག་པ་དེའི་དངོས་པོ་ངེས་པའི་དོན་ཅན་རྣམས་ཀྱི་ཡུལ་དུ་བྱེད་ཅིང་དེ་ཉིད་ལ་ཆོས་དང་ཆོས་ཅན་གྱི་ཐ་སྙད་ཕན་ཚུན་དེ་ཉིད་དང་གཞན་དག་ཏུ་བརྗོད་པར་བྱ་བ་མ་ཡིན་པ་འདི་སྤྲོ་བར་བྱེད་དོ། །

[Block 504]
ཆོས་ནི་ཆོས་ཅན་ལས་གཞན་པ་ཡང་མ་ཡིན་ཏེ། དོན་གཞན་མི་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 505]
དེ་ཉིད་ཀྱང་མ་ཡིན་ཏེ། དེ་བརྗོད་པ་དག་བཞིན་དུ་ཆོས་བརྗོད་པ་རྣམས་ཀྱིས་ཀྱང་རྣམ་པར་གཅོད་པ་གཞན་འཕེན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 506]
དེ་ལྟ་ན་ནི་འདོད་པའི་ཤེས་པར་མི་འགྱུར་བའི་ཕྱིར་བརྡའི་ཁྱད་པར་མི་བྱ་བར་མི་འགྱུར་རོ། །

[Block 507]
ཆོས་དང་ཆོས་ཅན་དག་བརྗོད་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་འདི་ནི་སྒྲའི་དོན་ལ་ཡིན་ནོ། །

[Block 508]
དངོས་པོ་ལ་ནི་རང་གི་མཚན་ཉིད་ལས་སྤྱིའི་མཚན་ཉིད་བརྗོད་པར་བྱ་བ་མ་ཡིན་ཏེ་མེད་པའི་ཕྱིར་རོ། །

[Block 509]
ཆོས་དང་ཆོས་ཅན་དག་ཐ༌[^356]དད་པ་མ་ཡིན་ན། ཐ་དད་པ་ལ་དྲུག་པ་ལ་སོགས་པར༌[^357]རྣམ་པར་དབྱེ་བ་མཐོང་བ་དང་། ཆོས་མང་བའི་ཕྱིར་དེ་ལ་མང་པོའི་ཚིག་གི་བྱེ་བྲག་མཐོང་བ་ཡང་ཆོས་ཅན་གཅིག་ལ་མི་རུང་བ་མ་ཡིན་ནམ་ཞེ་ན། འདི་ལ་སྒྲ་རྣམས་ལ་རང་དབང་ཅན་ཉིད་ནི་མེད་དོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 510]
གཞན་ཡང་།

[Block 511 [VERSE]]
གང་དག་གི་ཚིག་དངོས་པོའི་དབང་། །
ལྷུར་བརྗོད་འདོད་ལ་མི་བརྟེན་པ། །
དེ་དག་ལ་ནི་དྲུག་པ་དང་། །
ཚིག་དབྱེ་ལ་སོགས་ཀླན་ཀ་རིགས། །

[Block 512]
གལ་ཏེ་སྒྲ་འདི་དག་སྐྱེས་བུ་རྣམས་ཀྱིས་འགའ་ཞིག་ལ་བྱ་བར་འདོད་དུ་ཟིན་ཀྱང་དུ་བ་ལ་སོགས་པ་བཞིན་དུ་དངོས་པོ་དང་འབྲེལ་པའི་ཕྱིར་བྱ་བར་མི་ནུས་ན་དེའི་ཚེ་ཇི་ལྟར་དྲུག་པ་ལ་སོགས་པར་འགྱུར། ཞེས་བྱ་བའི་ཀླན་ཀ་འདིར་འགྱུར་གྱི། གང་གི་ཚེ།

[Block 513 [VERSE]]
ཕྱི་རོལ་དོན་ལ་མི་ལྟོས་པའི། །
ཚིག་གང་སྨྲ་བོས་ཇི་ལྟ་བུར། །
རྗོད་བྱེད་ཉིད་དུ་ངེས་བྱེད་པ། །
དེ་དེ་བཞིན་དུ་རྗོད་བྱེད་ཡིན། །

[Block 514]
ཐ་དད་པ་ལ་ནི་དྲུག་པའོ། །

[Block 515]
མང་པོ་ལ་ནི་བྱེད་པ་པོ་རྣམས་སོ། །ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་ཡང་སྐྱེས་བུའི་འདོད་པ་ལ་མི་ལྟོས་པ་ཉིད་དུ་དངོས་པོ་ཉེ་བ་ཙམ་གྱིས་རང་ཉིད་ཞུགས་པ་ནི་མ་ཡིན་ཏེ། དེ་དག་ནི་དེ་ལ་དེ་ལྟར་སྦྱོར་བས་དེ་ལྟར༌[^358]གོ་བར་འགྱུར་རོ། །

[Block 516]
དེ་བཞིན་དུ་གཞན་ལ༌[^359]ལ་ཡང་དེ་དག་གིས་ཇི་ལྟར་ཡང་རུང་རབ་ཏུ་སྦྱར་བ་དེ་ཁོ་ན་བཞིན་དུ་གོ་བའི་རྒྱུ་དག་ཏུ་འགྱུར་རོ། །

[Block 517]
དེ་ལ་ནི་བརྗོད་པར་བྱ་བ་དག༌[^360]སྐྱེས་བུ་ལ་རག་ལས་ཏེ། འཇུག་པའི་སྒྲ་དངོས་པོ་ཡང་དག་པར་མི་སྟོན་པ་ཇི་ལྟར་གོམས་པ་བཞིན་རྣམ་པར་རྟོག་པ༌[^361]སད་པའི་རྒྱུར་གྱུར་པ་རྣམས་འཇུག་པ་སེམས་པ་དང་། དེའི་དབང་གིས་དངོས་པོ་རྣམ་པར་འཇོག་པ་ནི་བླུན་པར་སྟོན་པ་འབའ་ཞིག་ཏུ་ཟད་དོ། །

[Block 518]
ཆོས་དང་ཆོས་ཅན་ལ་སོགས་པ་ལ་སྒྲ་དག་དེ་ལྟར་རྣམ་པར་གཞག་པར་བྱས་ཀྱི། ལྡོག་པ་དང་དངོས་པོ་ཐ་དད་པའི་སྒོ་ནས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ག་ལས་ཤེ༌[^362]ན། དེ་ལྟར་ན༌[^363]ཐ་སྙད་མི་རུང་བའི་ཕྱིར་ཏེ། ཆོས་དང་ཆོས་ཅན་དག་ཐ་དད་པའམ། དེའི་ངོ་བོ་ཡིན་པའམ། སྒྲ་རྣམས་དངོས་པོ་ཇི་ལྟ་བ་བཞིན་དུ་འཇུག་པ་ཡིན་ནོ། །

[Block 519]
སྤྱི་དང་དེ་དག་གི་འབྲེལ་པ་དང་། གཞི་མཐུན་པ་ཉིད་དང་། ཁྱད་པར་དང་ཁྱད་པར་གྱི་གཞིའི་དངོས་པོ་དག༌[^364]མི་རུང་ངོ་ཞེས་འཆད་པར་འགྱུར་རོ། །

[Block 520]
གང་ཡང་སྒྲ་འཇུག་པའི་ཁྱད་པར་འདི་ནི་ཐམས་ཅད་དུ་དངོས་པོས་བྱས་པ་ཁོ་ནར་འདོད་པ་དེའི།

[Block 521 [VERSE]]
བཙུན་མོ་རྣམས་གྲོང་དྲུག་ལ་སོགས། །
ཐ་དད་ཐ་དད་མིན་གཞན༌[^365]པའམ། །
ནམ་མཁའི་རང་བཞིན་ནམ༌[^366]མཁའ་ཉིད། །

[Block 522]
ཅེས་བྱ་བ་འདི་ལ་རྒྱུ་ཅི་ཡོད། གང་གི་ཚེ་བུད་མེད་གཅིག་ལ་ཡང་བཙུན་མོ་རྣམས་ཞེས་བྱ་བ་དང་། བྱེ་མ་གཅིག་ལ་ཡང་བྱེ་མ་རྣམས་ཞེས་ཐ་སྙད་འདོགས་པ་དེ་ལ་གང་གིས་ན་དེ་ལྟ་བུར་འགྱུར་བའི་མང་པོ་ཉིད་ཅི་ཞིག་ཡོད། གལ་ཏེ་ནུས་པ་ཐ་དད་པ་ཡིན་ནོ་ཞེ་ན། དེ་ནི༌[^367]ཐམས་ཅད་དུ་གཅིག་གིས༌[^368]ཚིག་ཉམས་པ་ཡིན་ཏེ། ནུས་པ་གཅིག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 523]
འབད་པ་ཡང་དོན་མེད་དོ། །

[Block 524]
གལ་ཏེ་དངོས་པོ་ཐ་མི༌[^369]དད་པའི་ཕྱིར་གཞན་ལ་གཅིག་གི་ཚིག་ཏུ་འགྱུར་རོ་ཞེ་ན། འདི་ལ་ཡང་འགྱུར་རོ། །

[Block 525]
དེའི་ཕྱིར་ངེས་པ་དངོས་པོ་མ་ཡིན་པ་འདི་བྱེད་པ་ན། སྒྲ་སྦྱོར་བ་ལ་འདོད་པ་རང་དབང་ཅན་དུ་སྟོན་པ་ཡིན་ནོ། །

[Block 526]
གྲོང་ཁྱེར་དྲུག་ཅེས་བྱ་བ་ཡང་ཇི་ལྟར་མང་པོ་དག་ལ་གཅིག་གི་ཚིག་ཏུ་འགྱུར། གྲོང་ཁྱེར་ཉིད་ཀྱང་ཅུང་ཟད་ཀྱང་མེད་ན། དེ་རྣམས་ལ་སྡུད་པ་ལྟ༌[^370]ག་ལ་ཡོད། ཁང་བཟངས་དང་སྐྱེས་བུ་ལ་སོགས་པ་རིགས་མི་མཐུན་པ་རྣམས་ཀྱིས་མི་རྩོམ་པའི་ཕྱིར། དེ་རྣམས་ཀྱི་སྤྱི་ལྟ་ཞིག་རྫས་གང་ལ༌[^371]ཡིན་ཏེ། ལྡན་པ་མེད་པའི་ཡང་ཕྱིར་རོ། །

[Block 527]
ལྡན་པ་ནི་མ་ཡིན་ཏེ། ཁང་བཟངས་རང་ཉིད་ལྡན་པའི་བདག་ཉིད་ཡིན་པ་གཞན་དང་མི་ལྡན་པའི་ཡང་ཕྱིར་རོ། །

[Block 528]
དེ་ཉིད་ཀྱི་ཕྱིར་གྲངས་ཀྱང་མེད་དེ། གལ་ཏེ་གྲོང་ཁྱེར་ནི་ལྡན་པ་དེ་དང་སྐྱེས་བུས་ཁྱད་པར་དུ་བྱས་པའི་ཡོད་པ་ཡིན་ནོ་ཞེ་ན། བོགས་དབྱུང་དུ་མེད་པ་འདི་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད། ཡོད་པ་ཡང་གཅིག་ཡིན་པའི་ཕྱིར། གྲོང་ཁྱེར་མང་པོ་ཉིད་ལ་ཡང་གྲོང་ཁྱེར་རྣམས་ཞེས་མང་པོའི་ཚིག་ཏུ་མི་འགྱུར་རོ།[^372] ། གལ་ཏེ་གཉིས་ཕན་ཚུན་གྲོགས་བྱེད་པ་ཉིད་ཡིན་ནོ་ཞེ་ན། ཕན་པར་བྱ་བ་དང་ཕན་པར་བྱེད་པ་པོ་མ་ཡིན་པ་དག་ལ་གྲོགས་བྱེད་པའི་དངོས་པོ་ཅི་ཞིག་ཡོད། སྐྱེས་བུ་དང་ལྡན་པ་དང་། ཡོད་པ་རྣམས་ཀྱང་མང་བའི་ཕྱིར། ཇི་ལྟར་གྲོང་ཁྱེར་ཞེས་གཅིག་གི་ཚིག་ཏུ་འགྱུར། གལ་ཏེ་དེ་ལྟ་བུ་རྣམས་དོན་འགའ་ཞིག་ལ་ནུས་པ་ཐ་མི་དད་པ་ཡོད་པས་དེ་རྒྱུ་མཚན་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། ནུས་པ་ནི་དངོས་པོའི་ངོ་བོ་ལས་ཐ་མི་དད་པའི་ཕྱིར་རོ།། །།

[Block 529]
བམ་པོ་གསུམ་པ། འོན་ཏེ་ཐ་དད་ན་ནི་ཕན་པར་བྱ་བ་མ་ཡིན་པ་ལ་གཞན་གྱི་དབང་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 530]
འོན་ཏེ་ཕན་ན་ནི་ནུས་པ་ལ་ཕན་འདོགས་པའི་ནུས༌[^373]པས་ཐུག་པ་མེད་པའི་ཕྱིར་རྟོགས་པ་མེད་དོ། །
--- END BLOCKS ---
