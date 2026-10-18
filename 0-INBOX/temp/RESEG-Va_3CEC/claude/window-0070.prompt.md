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
[Block 2451]
དེ་ལྟར་སེམས་ཀྱི་རང་བཞིན་སྟོང་ཡང་ཀུན་རྫོབ་ཏུ་རྒྱུ་གང་སྤྱད་པའི་འབྲས་བུ་དེ་བཞིན་དུ་ཐོབ་པར་འགྱུར་ཏེ་ཆུད་མི་ཟ་བར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གཅིག་ཁོ་ནར་ངེས་པར་མི་མངོན་པ་དེ་ནི་བལྟ་དཀའ་བས་ཤིན་ཏུ་ཟབ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2452]
སེམས་ཀྱི་ཆོས་ཉིད་དེ་ལྟ་བུ་ཡིན་དུ་ཟིན་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དོན་དམ་པར་སེམས་དེ་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་དུ་ཟིན་ཀྱང་ཀུན་རྫོབ་ཏུ་རྒྱུ་དང་རྐྱེན་རྣམས་ཚོགས་ན་མེད་པར་མི་འགྱུར་ལ། རྒྱུ་རྐྱེན་ཚོགས་པ་ལས་འབྱུང་བ༌[^2127]དེ་དག་ཀྱང་མུ་སྟེགས་ཅན་གྱི༌[^2128]བྱེད་པ་པོ་ལ་སོགས་པ་མེད་པས་དེ་དག་གིས་ཀྱང་བསྐྱོད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2453]
དེ་དག་ཇི་ལྟར་འདོད་པ་བཞིན་རྣམ་པར་བསྒྲུབ་པ༌[^2129]ཞེས་བྱ་བ་ནི་དེ་ལྟར་བྱེད་པ་པོ་ལ་སོགས་པ་མེད་པར་ཡང་རྒྱུ་རྐྱེན་ཚོགས་པ་ལས་ཀུན་རྫོབ་ཏུ་སྐྱེ་ཞིང་འབྱུང་བས་ན་རྒྱུ་གང་དང་གང་གིས་འབྲས་བུ་གང་དང་གང་སྒྲུབ་པ་དེ་དག་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་གྲུབ་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2454]
བདག་གིས་ཀྱང༌[^2130]རྣམ་པར་བསྒྲུབ་པ་ལ་བརྩོན་པར་བྱ་ཞེས་བྱ་བ་ནི༌[^2131]ཇི་ལྟར་འདོད་པ་བཞིན་འབྲས་བུ་འགྲུབ་པས་བདག་གིས་ཀྱང་བདོག་པ་ཐམས་ཅད་ཡོངས་སུ་གཏང་བ༌[^2132]ལ་སོགས་པའི་འབྲས་བུ་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་བྱ་བའི་ཕྱིར་བསྔོ་བ་ལ་སོགས་པ་ལ་བརྩོན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2455]
སེམས་ཀྱི་ཆོས་ཉིད་འདི་ཡང་མི་སྤོང་ངོ་ཞེས་བྱ་བ་ནི་དེ་དག་ཀུན་རྫོབ་ཏུ་སྒྲུབ་པ༌[^2133]ལ་བརྩོན་པར་བྱེད་ཀྱང་། དོན་དམ་པར་སེམས་ཀྱི་ཆོས་ཉིད་མ་སྐྱེས་པ་ཡང་མི་སྤོང་བ་འམ། དེ་ཡང་ཉམས་པར་མི་བྱེད་པའོ། །

[Block 2456]
སེམས་ནི་སྒྱུ་མ་ལྟ་བུ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དོན་དམ་པར་མི་དམིགས་པ་དང་། ཀུན་རྫོབ་ཏུ་རྒྱུ་དང་འབྲས་བུ་ངེས་པར་ཡོད་པར་བསྟན་པའོ། །

[Block 2457]
སྒྱུ་མ་ལྟ་བུར་ཞེས་བྱ་བ་ནི་སྒྱུ་མ་བཞིན་དུ་རང་བཞིན་མེད་པ་སྟེ། [^2134]དེ་བས་ན་གང་ཟག་འདི་ལ་བདག་གིས་དངོས་པོ་གཏོང་བར་སྣང་བ་ནི་རང་བཞིན་མེད་པའོ། །

[Block 2458]
བདོག་པ་ཐམས་ཅད་ཡོངས་སུ་བཏང་སྟེ་ཞེས་བྱ་བ་ནི་ཕྱི་དང་ནང་གི་དངོས་པོ་ཐམས་ཅད་ཡོངས་སུ་གཏོང༌[^2135]བའོ། །

[Block 2459]
སངས་རྒྱས་ཀྱི་ཞིང་དག་པ་ནི་བཻ་ཌཱུརྱའི་ཁ་དོག་ལ་སོགས་པའོ། །

[Block 2460]
སེམས་རྨི་ལམ་ལྟ་བུ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་རྨི་ལམ་ན་དངོས་པོ་རྣམ་པ་སྣ་ཚོགས་སྣང་བ༌[^2136]ཡང་རང་བཞིན་སྟོང་པ་དེ་བཞིན་དུ། སེམས་ལ་གཟུང་བ་དང་འཛིན་པ་ལ་སོགས་པ་རྣམ་པ་དུ་མར་སྣང་ཡང་རང་བཞིན་གྱིས་སྟོང་པའོ། །

[Block 2461]
ཡང་དག་པར་བླངས་པ་དང་། ཡང་དག་པར་སློབ་པ་ནི་ཚུལ་ཁྲིམས་སོ། །

[Block 2462]
ཡང་དག་པར་བླང་བར་བྱ་བ་དང་། བསླབ་པར་བྱ་བ་ནི་བསླབ་པའོ། །

[Block 2463]
ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་མཁྱེན་པ་ཐོབ་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2464]
གཟོད་མ་ནས་ཡོངས་སུ་མ་གྲུབ་ཅེས་བྱ་བ་ནི་ཇི་ལྟར་མིག་ཡོར་ཕྱིས་བརྟགས༌[^2137]ཏེ་རང་བཞིན་མེད་པ་ལྟར་དང་པོ་སྣང་བའི་དུས་ན་ཡང༌[^2138]རང་བཞིན་མེད་པ་ཡིན་ནོ། །

[Block 2465]
དེ་དང་འདྲ་བར་སེམས་འདི་ཡང་ཐོག་མ་ནས་རང་བཞིན་མེད་ཅིང་མ་སྐྱེས་པའོ། །

[Block 2466]
བཟོད་པ་ནི་གཞན་གྱིས་གནོད་པ་བྱས་པ་ཉམས་སུ་ལེན་པའོ། །

[Block 2467]
དེས་པ་ནི་སླར་གནོད་པ་མི་བྱེད་པ་སྟེ། དེ་དག་བསྒྲུབས་པ༌[^2139]ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2468]
མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་རྫོགས་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་དང་འགག་པ་མེད་པའི་ཆོས་ལ་སྐྲག་པ་མེད་པ་ཐོབ་པར་བྱ་བའི་ཕྱིར་བསྔོ༌[^2140]བའོ། །

[Block 2469]
ཤིན་ཏུ་དབེན་པ་ཞེས་བྱ་བ་ནི་སྨིག་རྒྱུ་ཆུས་སྟོང་སྟེ། དབེན་པ་བཞིན་དུ་སེམས་ལ་ཡང་གཟུང་བ་དང་འཛིན་པས་སྟོང་སྟེ་དབེན་པའོ། །

[Block 2470]
དགེ་བའི་རྩ་བ་ཐམས་ཅད་ལ་ཞེས་བྱ་བ་ནི་དགེ་བའི་རྩ་བ་ཐམས་ཅད་སྒྲུབ་པ་ལ་ཞེ་འམ། སྒྲུབ་པའི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2471]
སངས་རྒྱས་ཀྱི༌[^2141]ཆོས་ནི་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པའོ། །

[Block 2472]
གཟུགས་ཅན་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་ཐོགས་པ་དང་བཅས་པའི་གཟུགས་ཀྱི་ངོ་བོ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2473]
བསྟན་དུ་མེད་པ་ཞེས་བྱ་བ་ནི་སྔོན་པོ་ལ་སོགས་པ་བཞིན་དུ་གཞན༌[^2142]ལ་བསྟན་པར་མི་ནུས་པའོ། །

[Block 2474]
ཐོགས་པ་མེད་པ་ནི་ནམ་མཁའ་བཞིན་དུ་ཀུན་དུ་སོང་བའི་ཕྱིར་རོ། །

[Block 2475]
རྣམ་པར་རིག་པ་མེད་པ་ནི་རིག་པར་བྱ་བ་དང་། རིག་པར་བྱེད་པ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 2476]
སངས་རྒྱས་ཀྱི་ཏིང་ངེ་འཛིན་ནི་རྣམ་པར་མི་རྟོག་པའི་ཏིང་ངེ་འཛིན་ནོ། །

[Block 2477]
གཟུང་བ་མེད་པ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བའི་གཟུང་བར༌[^2143]སྣང་བ་དངོས་པོར་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2478]
མཚན་མ་མེད་པ་ནི་གཟུགས་ལ་སོགས་པའི་ངོ་བོ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2479]
བསྟན་དུ་མེད་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 2480]
གནས་མེད་པ་ནི་གཟུགས་དང་དབང་པོ་ལ་མི་གནས་པའི་ཕྱིར་རོ། །

[Block 2481]
དྲིས་པའི་ཚིག་ནི་ཕུང་པོ་དང་ཁམས་ལ་སོགས་པ་གཞན་གྱིས་དྲིས་པའོ། །

[Block 2482]
དབྱེ་བ་བསྟན་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཐོས་པའི་ཆོས་རྣམས་སོ་སོར་ཕྱེ་སྟེ་བཤད་པའི་གནས་ཤེས་རབ་བོ། །

[Block 2483]
སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ནི་མེ་ལོང་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 2484]
སེམས་ནི་དམིགས་པ་མེད་པར་མི་སྐྱེ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཀུན་རྫོབ་ཀྱི་སེམས་ཀྱིས༌[^2144]དམིགས་པའི་རྒྱུ་དང་རྐྱེན་ལ་སོགས་པ་ཡོད་པར་བསྟན་པ་ལས།

[Block 2485]
སྒྲུབ་པ་ཡང་ཡོད་པར་བསྟན་པ་སྟེ། དམིགས་པར་བྱ་བའི་ཡུལ་མེད་པར་སེམས་མི་སྐྱེའོ། །

[Block 2486]
ཡུལ་ལ་དམིགས་ནས་སྐྱེ་བ་ནི་སེམས་ཀྱི་ཆོས་ཉིད་དོ། །

[Block 2487]
གང་དགེ་བའི་རྩ་བ་ཐམས་ཅད་ལ་དམིགས་པ་ཞེས་བྱ་བ་ནི་སེམས་ཡུལ་ལ་དམིགས་ནས་སྐྱེ་བ་ཡིན་པས། དམིགས་ནས་ཡང་དགེ་བའི་རྩ་བ་སྐྱེ་བར་འགྱུར་བའི་དམིགས་པ་ཐམས་ཅད་ལ་སེམས་དམིགས་པའོ། །

[Block 2488]
རྒྱུ་མེད་པར་མི་སྐྱེ་བ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་བག་ཆགས་མེད་པར་སེམས་མི་སྐྱེ་བའོ། །

[Block 2489]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཞེས་བྱ་བ་ནི་སེམས་སྐྱེ་བའི་རྒྱུ་བསྐྱེད་ཅིང་འཇོག་ན་ཡང་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་སྐྱེ་བའི་རྒྱུ་བསྐྱེད༌[^2145]པའོ། །

[Block 2490]
ཡུལ་དྲུག་ལ་ཞེས་བྱ་བ་ནི་ཡུལ་དྲུག་ལ་མ་བརྟེན་པར་སེམས་མི་སྐྱེ་པའོ། །
--- END BLOCKS ---
