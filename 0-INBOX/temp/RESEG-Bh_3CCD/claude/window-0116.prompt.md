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
[Block 4061]
དོན་དམ་པར་དེ་ནི་ཐོག་མར་འཇིག་པ་ཡིན་ཏེ། སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4062]
དེ་བས་ན་དངོས་པོར་སྨྲ་བ་བརྟན་པ་རྣམས་ཀྱི་འཁྲུལ་པ་བསལ་བར༌[^2507]བྱ་བའི་དོན་དུ་དངོས་པོ་ཉིད་དང་སྐད་ཅིག་མ་ཉིད་ལྡོག་པའི་དབྱེ་བས་བརྟགས་ཏེ་བསྒྲུབ་པར་བྱ་བ་དང་། སྒྲུབ་པར་བྱེད་པའི་འབྲེལ་པ་མཁས་པ་རྣམས་ཀྱིས་བྱས་སོ། །

[Block 4063]
དེ་བས་ན་འཁྲུལ་པ་ཉིད་བསལ་བར༌[^2508]བྱ་བའི་ཕྱིར་རྗེས་སུ་དཔག་པའི་ཚད་མ་བསྟན་ཏོ། །

[Block 4064]
ལྡོག་པ་མ་ལུས་པ་དང་ལྡན་པའི་རང་བཞིན་གྱི་དངོས་པོ་གཟུང་བ་ལ་མཁས་པ་མངོན་སུམ་གྱི་སྐད་ཅིག་མ་ཉིད་གཟུང་བ་ལ་ནུས་པ་མེད་དམ། འོན་ཀྱང་ངེས་པས་གང་ཞིག་ཆ་གཟུང༌[^2509]བ་མི་ནུས་པ་དེ་ལ་དེའི་ཚད་མ་ཡང་བསྟན་ཏོ། །

[Block 4065 [VERSE]]
ཆ་དང་བྲལ་བའི་ཁྱད་པར་ནི། །
མངོན་སུམ་གྱིས་ནི་གཟུང་བས་ཀྱང་། །
གང་ཞིག་ཁྱད་པར་རྟོགས་ངེས་པ། །
དེ་ནི་རྟོགས་པར་གྱུར་པ༌[^2510]ཡིན། །

[Block 4066]
ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4067]
དེ་བཞིན་དུ༌དངོས་པོ་དང་དངོས་པོ་མ་ཡིན་པ་ནི་རང་བཞིན་གཅིག་པར་བརྗོད་པར་མི་རིགས་ཏེ། ཐ་དད་པའི་ཚད་མའི་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4068]
དེ་ལ་དོན་གྱི༌[^2511]བྱ་བ་བྱེད་པའི་དངོས་པོ་ནི་རང་གི་མཚན་ཉིད་དང་མ་བྲལ་བ་འཁྲུལ་པ༌[^2512]མེད་པ་གསལ་བར་སྣང་བ་དབང་པོའི་མངོན་སུམ་གྱིས་ངེས་པར་འགྱུར་རོ། །

[Block 4069]
དངོས་པོ་མ་ཡིན་པ་ཡང་ནུས་པ་ཐམས་ཅད་དང་བྲལ་བའི་མཚན་ཉིད་སྣང་བ་མི༌[^2513]དམིགས་པས་མེད་པའི་ཐ་སྙད་དུ་བྱའོ་ཞེས་བསྒྲུབ་པ་དང་བཀག་པ་སྒྲུབ་པར་བྱེད་པ་མངོན་སུམ་དང་རྗེས་སུ་དཔག་པའི་སྤྱོད༌[^2514]ཡུལ་དངོས་པོ་དང་དངོས་པོ་མ་ཡིན་པ་ཞེས་ཇི་ལྟར་དངོས་པོ་གཅིག་གི་རང་བཞིན་ཡིན། འོ་ན་དངོས་པོ་གཅིག་གཉིས་ཀའི་རང་བཞིན་དེའི་བདག་ཉིད་ཀྱིས་བཀག་པས་ཤེས་པར་བྱ་བ་མ་ཡིན་ནམ། དཔེར་ན་བུམ་པ་འདི་ཤ་ཟ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 4070]
གལ་ཏེ་ཡིན་ན་ཤ་ཟ་ཡང་མཐོང་བར་འགྱུར་རོ། །

[Block 4071]
དེ་བཞིན་དུ་ཡོད་པའི་རང་བཞིན་གྱི་དངོས་པོ་དང༌[^2515]དངོས་པོ་མེད་པའི་ཆ་དང་འདྲེས་པ་ཡིན་ནོ་ཞེ་ན། དེ་ནི་ཡང་དག་པ་མ་ཡིན་ཏེ། དཔེ་མི་འདྲ་བའི་ཕྱིར་རོ། །

[Block 4072]
གང་གི་ཕྱིར་བུམ་པ་འདི་ཤ་ཟ་མ་ཡིན་ནོ་ཞེས་བྱ་བས། ཤ་ཟ་ལས་ལྡོག་པ་ཙམ་བསྟན་པ་ཡིན་ཏེ། བུམ་པ་ལས་ལྡོག་པ་དང་ལྡན་པའི་སྣམ་བུ་བཞིན་ནོ། །

[Block 4073]
དངོས་པོའི་ལྡོག་པ་ཇི་སྲིད་ཡོད་པ་དེ་སྲིད༌[^2516]དེ་བརྗོད་པའི་ནུས་པ་ཡོད་དེ། དེ་བས་ན་ཤ་ཟ་ལས་ལྡོག་པའི་རང་བཞིན་བུམ་པ་འབའ་ཞིག་སོ་སོར་སྣང་བས་འདི་ཤ་ཟ་མ་ཡིན་ནོ་ཞེས་དེའི་བདག་ཉིད་ཀྱིས་དགག་པར་རིགས་སོ། །

[Block 4074]
དེ་བཞིན་དུ་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དང་ལྡན་པའི་དངོས་པོ་ནི་མི་རིགས་སོ། །

[Block 4075]
དངོས་པོ་མེད་པ་བཀག་པའི་སྒོ་ནས་དངོས་པོ་རྟོགས་པར༌[^2517]འགྱུར་བ་དང་། དངོས་པོ་དགག་པའི་སྒོ་ནས་ཀྱང་དངོས་པོ་མེད་པ་རྟོགས་པར་འགྱུར་རོ། །

[Block 4076]
དེ་བས་ན་དངོས་པོ་དགག་པས། དངོས་པོ་མེད༌[^2518]པར་བྱ་བ་དང་དངོས་པོ་མེད་པ་བཀག་པས་དངོས་པོ་ངེས་པར་བྱ་བ་ཡིན་ནོ། །

[Block 4077]
དེ་བས་ན་འབའ་ཞིག་དངོས་པོ་ཙམ་དུ༌[^2519]འགྲུབ་པའམ་དངོས་པོ་མེད་པ་ཙམ་འགྲུབ་པ་ཡིན་གྱི་དངོས་པོ་དང་དངོས་པོ་མེད་པའི་བདག་ཉིད་ཅན་གྱི་དངོས་པོ་ནི་གཉིས་ཀའི་རང་བཞིན་མི་རིགས་སོ། །

[Block 4078]
དེ་བས་ན༌[^2520]ཞེས་བྱ་བ་ལ་སོགས་པས་ཉེ་བར་བསྡུས་པ་བཤད་པར་བྱ་སྟེ། བསྒོམ་པར་བྱ་བ་ནི་ཤེས་བྱའོ། །

[Block 4079]
སྒོམ་པ་པོ་ནི་དངོས་པོ༌[^2521]སྒོམ་པར་བྱེད་པ་སྟེ། སྒོམ་པ་གཞལ་བར་བྱེད་པའོ། །

[Block 4080]
བསྒོམ་པ་ནི་བྱ་བའི་བདག་ཉིད་མེད་དེ། ལས་དང་བྱེད་པ་པོ་གཉིས་མེད་པའི་ཕྱིར་རོ། །

[Block 4081]
དེ་བས་ན་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད༌[^2522]ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 4082]
ཡི་གེའི་དོན་ནི་ཁྱབ་པར་བྱ་བ་མི་དམིགས་པས་དངོས་པོ་ཐམས་ཅད་ཀྱི་སྟོང་པ༌[^2523]ཉིད་སོ་སོར་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 4083]
རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་གྱི་རིམ་པས་དངོས་པོ་ཐམས་ཅད་ཀྱི་སྟོང་པ་ཉིད་སོ་སོར་བསྟན་པར་བྱ་བའི་ཕྱིར། སྟེང་འོག་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཆ་དྲུག་དང་ལྡན་པའི་ས་ལ་སོགས་པའི་ཁམས་བཞིའོ། །

[Block 4084]
དེ་རྣམས་གཅིག་དང་དུ་མ་བྲལ་བའི་ཕྱིར་སྟོང་པ་ཡིན་ནོ་ཞེས་སྟོང་པ་ཉིད་ཀྱི༌[^2524]མཚན་ཉིད་ཅན་གྱི་རྣམ་པར་ཐར་པའི་སྒོ་གཅིག་གོ། །

[Block 4085]
འདུས་བྱས་དང་འདུས་མ་བྱས་པ༌[^2525]ནི་འདུས་བྱས་པ་སྟེ་ཕུང་པོ་ལྔའོ། །

[Block 4086]
འདུས་མ་བྱས་པ་ནི་ནམ་མཁའ་ཞེས་པ་ལ་སོགས་པའོ། །

[Block 4087]
དེ་དག་ཐམས་ཅད་སྔར་བཤད་པའི་རིགས་པས་སྟོང་པ་སྟེ། དངོས་པོ༌[^2526]མེད་པ༌[^2527]ཞེས་བྱ་བ་ནི། ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྣལ་འབྱོར་པ་རྣམས་ཀྱི་སྒོམ་པ་གང་ཡིན་པ་དེ་ནི་སྒོམ་པ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། སྟོང་པ་ཉིད་ལ་མངོན་པར་ཞེན་པར་ལྟ་བ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་པ་ལ། ཆོས་ཐམས་ཅད་སྟོང་པ་ཡིན་ཞེས་མངོན་པར་ཞེན་པའི་བདག་ཉིད་ཀྱི་ལྟ་བ་གང་ཡིན་པ་རྒྱུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4088]
སྟོང་པ་ཉིད་ལ་མངོན་པར་ཞེན༌[^2528]པའི་ལྟ་བས་འདུས་བྱས་པ་དང་འདུས་མ་བྱས་པའི་དངོས་པོའི་ཡུལ་ཅན་གྱི་བསྒོམ་པ་ནི་མི་རིགས་ཏེ། དེ་ནི་རྟེན༌[^2529]མེད་པའི་ཕྱིར་རོ། །

[Block 4089]
སྟོང་པ་ཉིད་ལ་མངོན་པར་ཞེན་པ་ཁོ་ན་བསྒོམ་པའི༌[^2530]རྟེན་ཡིན་ནོ་ཞེས་པས་ཇི་ལྟར་སྒོམ་པ༌[^2531]དགག་ཅེ་ན་སྨྲས་པ། སྟོང་པ་ཉིད་ཅེས་བྱ་བ་མ་ཡིན་པར་དགག་པའི་མཚན་ཉིད་ཅན་གྱི་དོན་རྟོགས་པ་མ་ཡིན་གྱི། འོན་ཀྱང་མེད་པར་དགག་པའི་མཚན་ཉིད་དོ། །

[Block 4090]
དེ་ལ་དངོས་པོ་འདྲ་བ་ཡོངས་སུ་འཛིན་པར་བྱེད་པ་དེ་མ་ཡིན་པར་དགག་པ་སྟེ། དཔེར་ན་བྲམ་ཟེ་མ་ཡིན་པ་ལ་ཁྱེར་ཤོག་ཅེས་བྱ་བས་བྲམ་ཟེ་དང་འདྲ་བའི་རྒྱལ་རིགས་ལ་སོགས་པ་ཁྱེར་བ་ནི་རྟོགས་པའོ། །

[Block 4091]
མེད་པར་དགག་པ་ནི་དངོས་པོ་མེད་པ་ཉིད་སྟོན་པར་བྱེད་པའོ། །

[Block 4092]
དེ་བཞིན་དུ་སྟོང་པ་ཉིད་ཀྱི་དངོས་པོ་བཀག་ནས་གང་ཡང་རུང་བའི་ཅིག་ཤོས་བརྗོད་པ་མ་ཡིན་ཏེ། གང་གིས་མངོན་པར་ཞེན་པ་ཙམ་ཡང་གཞག་པར༌[^2532]བྱ། འོན་ཀྱང་དངོས་པོའི༌[^2533]ཆ་ཐམས་ཅད་དགག་པ་སྟོང་པ༌[^2534]ཡིན་ནོ། །

[Block 4093 [VERSE]]
རྣམ་པ་དུ་མས་ཐ་དད་པའི། །
དངོས་པོ་རྣམས་ནི་གོས་དང་འདྲ། །
སྟོང་པ་ཉིད་མེས་ཚིག་གྱུར་ན། །
ཐལ་བའི་དབྱེ་བ་གང་ཡང་མེད། །

[Block 4094 [VERSE]]
སེམས་ཅན་དང་ནི་སྣོད་ཅེས་བྱ། །
འཇིག་རྟེན་གཉིས་པོ་འདིར་བསྲེགས་ནས། །
རང་བདག་ཀྱང་ནི་དེ་ཉིད་དོ། །
མེ་སྒྲོན་བཞིན་དུ་ཞི་བར་འགྱུར། །

[Block 4095]
ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4096]
དེ་ཉིད་ཀྱི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2535]ཆ་དང་ཆ་ཙམ་གྱི༌[^2536]རྣམ་པར་རྟོག་པ༌[^2537]ཡང་སྤོང་བའི་ཕྱིར་སྟོང་པ་ཉིད་ནི་རྣམ་པ་བཅོ་བརྒྱད་དུ༌[^2538]གསུངས་ཏེ།

[Block 4097 [VERSE]]
ལྟ་བས་བྱས་པའི་སྐྱོན་ཀུན་ནི། །
སྤོང་ཕྱིར་སྟོང་པ་ཉིད་གསུངས་སོ། །

[Block 4098]
ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4099]
གལ་ཏེ་ནུས་པ་ཐམས་ཅད་དང་བྲལ་བའི་མཚན་ཉིད་ཅན་སྟོང་པ་ཉིད་ཡིན་ན།

[Block 4100]
དེའི་ཚེ་བཅོམ་ལྡན་འདས་ཀྱིས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས།
--- END BLOCKS ---
