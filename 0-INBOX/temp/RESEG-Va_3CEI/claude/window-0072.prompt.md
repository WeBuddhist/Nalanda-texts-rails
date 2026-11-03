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
[Block 2521]
ཕའི་གནས་དེར་ཕྱིན་ཞེས་བྱ་བ་ནི་ལུང་དང་རིགས་པའི་སྒོ་ནས་སྤྱོད་པ་ལ་ཞུགས་ཞེས་པའི་དོན་ཏོ། །

[Block 2522]
གནས་གང་ན་བ་དེར་ཕྱིན་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོའི་ཕྱོགས་ལ་བསྙེན༌[^2114]ཞེས་པའི་དོན་ཏོ། །

[Block 2523]
འགྲོན་བུ་དང་གསེར་དང་། འབྲུ་མཛོད་མང་དུ་ཡོད་ཅེས་པ་ནི་ཐེག་པ་ཆེན་པོ་རིན་པོ་ཆེ་ཐམས་ཅད་ཀྱི་འབྱུང་གནས་སུ་གྱུར་པ་ཉིད་ལ་བྱའོ། །

[Block 2524]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་མི་དབུལ་པོ་དེའི་ཕ༌[^2115]ཞེས་པ་ནས། བརྒྱན་པ༌[^2116]ལ་མཆི་སྟེ་ཞེས་པའི་བར་དུ་ནི་འདིས་ཕ་མཐོང་བ་བསྟན་པ་ལ་ཡང་ཕ་བདེ་བར་འདུག་པ་དང་འཁོར་མང་པོས་བསྐོར་བའོ། །

[Block 2525]
མཐོང་ཞེས་པ་ནི་རྒྱང་མ་ནས་མཐོང་ཞེས་པའི་དོན་ཏེ།[^2117] ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ་ལ་ད་དུང་རིང་ཞེས་པའི་དོན་ཏོ། །

[Block 2526]
ཁྲི་ནི་མི་འཇིགས་པ་བཞིའི་ཁྲི་དང་། བསམ་གཏན་བཞིའི་ཁྲིའོ། །

[Block 2527]
རྒྱན་སྣ་ཚོགས་ཀྱིས་བརྒྱན་ཞེས་པ་ནི་གདུག་པ་གསུམ་དང་བྲལ་བའི་རྒྱན་གྱིས་བརྒྱན་པའོ། །

[Block 2528]
ལྷག་པའི་ཚུལ་ཁྲིམས་ནི་བྲམ་ཟེ་དང་སྦྱར་རོ། །

[Block 2529]
ལྷག་པའི་ཤེས་རབ་ནི་རྒྱལ་རིགས་དང་སྦྱར་རོ། །

[Block 2530]
ལྷག་པའི་བསམ་གཏན་ནི་རྗེའུ་རིགས་དང་སྦྱར་རོ། །

[Block 2531]
མདོ་ལས་འགྲོན་བུ་བྱེ་བ་བརྒྱ་སྟོང་གིས་སྤྱོད་པ་བགྱིད་དེ་ཞེས་པ་ནས་ལོངས་སྤྱོད་ཆེན་པོས་མཆིས་པ་ཞེས་པའི་བར༌[^2118]ནི་རྒྱན་དེ་ལ༌[^2119]ཡང་རྣམ་པ་གཉིས་ཏེ། དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་ཀྱིས༌[^2120]ལུས་བརྒྱན་པ་དང་། སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པས་འཁོར་བྱས་པ་དང་། ཉོན་མོངས་པ་ཐུལ་བ་ཉིད་བྲན་དུ་བྱས་པ་དང་། བསྡུ་བ་རྣམ་བཞིའི་སེམས་རྟག་ཏུ་འཛིན་པ་རྔ་ཡབ་བྱས་པ། ཚད་མེད་བཞིའི་བླ་རེ་བྲེས་པ། རྣམ་པར་དག་པའི་ཡན་ལག་བདུན་གྱི་མེ་ཏོག་དང་། དེ་ལ་སོགས༌[^2121]ཏེ་སྤྱོད་པ་དམ་པ༌[^2122]ཐམས་ཅད་ཀྱིས་བརྒྱན་པའི་གནས་ན་འདུག་ཅེས་པའི་དོན་ཏོ། །

[Block 2532]
བུ་དེས་ཕ་མཐོང་ནས་བྲོས་པ་ནི་རྫོགས་ལོངས་སྤྱོད་པའི་སྐུ་མཐོང་ཞེས་པའི་དོན་ཏོ། །

[Block 2533]
མདོ་ལས་བཅོམ་ལྡན་འདས་མི་དབུལ་པོ་དེས་ཞེས་པ་ནས་འདི་སྙམ༌[^2123]སེམས་སོ་ཞེས་པའི་བར་དུ་མཐོང་ཞེས་པ་ནི་མངོན་དུ་རྟོགས་པ་མ་ཡིན་ཏེ། ཐོས་པ་དང་བསམ་པའི༌[^2124]སྒོ་ནས་དཔོག་པའོ། །

[Block 2534]
ལོངས་སྤྱོད་ཆེ་ཞེས་པ་ནི་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པའི་མཐུ་ཆེ་བས་ལོངས་པའོ། །

[Block 2535]
དེ་འདྲ་བའི་ལོངས་སྤྱོད་ཆེན་པོ་བདག་གིས་མ་བསྒྲུབས་ན་མི་འཐོབ་པས་སྐྲག་ཅེས་པའི་དོན་ཏོ། །

[Block 2536]
མདོ་ལས་རྒྱལ་པོའི་བློན་པོ་འདི་དང་ཞེས་པ་ནས་ཕྲད་པར་འགྱུར༌[^2125]དུ་མི་འོང་ངམ་སྙམ་ཞེས་པའི་བར་དུ། རྒྱལ་པོ་ཞེས་པ་ནི་ཆོས་ཀྱི་སྐུའོ། །

[Block 2537]
བློན་པོ༌[^2126]ཞེས་པ་ནི་རྫོགས་ལོངས་སྤྱོད་པའི་སྐུའོ། །

[Block 2538]
དབུལ་པོའི་གནས་སུ་འགྲོ་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་ཀྱི་སྤྱོད་པ་ལ་འཇུག་པའོ། །

[Block 2539]
ཟས་དང་གོས་ཀྱིས༌[^2127]ཉོན་མི་མོངས་ཞེས་པ་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་དེར་ཡང་བསྒྲགས་སུ༌[^2128]ཡོད་ཅེས་པའི་དོན་ཏོ། །

[Block 2540]
ཚམས༌[^2129]ཟུངས་སུ་ཟུན་པར་མི་འགྱུར་རམ་ཞེས་པ་ནི༌[^2130]ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ༌[^2131]ལ་དབང་མེད་པར་ཞུགས་པར་མི་འགྱུར་རམ་ཞེས་པའི་དོན་ཏོ། །

[Block 2541]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་མི་དབུལ་པོ་དེ་ཞེས་པ་ནས། བརྒྱལ་ཏེ་ས་ལ་འགྱེལ་ནས་མྱོས་པར་གྱུར༌[^2132]ལ་ཞེས་པའི་བར་དུ་ནི་མྱུར་དུ་བྲོས་ཞེས་པ་ནི་རང་གི་ཉམས་ལས༌[^2133]སྤྱོད་པ་ཆེན་པོ་ལ་འཇུག་པར་མི་ནུས་ནས་ལྡོག་ཅེས་པའི་དོན་ཏོ། །

[Block 2542]
ཕས་མྱུར་དུ་འཛིན་དུ་བཅུག་པ་ནི་ཐེག་པ་ཆེན་པོ་ལ་འཇུག་པའི་རྒྱུ་སྨིན་པར་གཟིགས་ནས་དགྱེས་པ་སྐྱེས་ཤིང་འཛིན་དུ་བཅུག་པའོ། །

[Block 2543]
སྲེད༌[^2134]པས་གདུངས་ཞེས་པ་ནི་ཐུགས་རྗེ་ཆེན་པོས་འགྲོ་བ་མང་པོ་ལ་འདྲེན་པར་དགོངས་པ་ཇི་ལྟར་སྲེད་པས་གདུངས་པ་བཞིན་ནོ། །

[Block 2544]
འདི་དག་འཛིན་དུ་བཅུག་ཅེས་པ་ནི་ཚིག་གི་དོན་མཚོན་པ༌[^2135]བསྙེམས་པ་མ་ཡིན་པའི་ཕྱིར་མི་དག༌[^2136]འཛིན་དུ༌[^2137]བཅུག་ཅེས་པའི་དོན་ཏོ། །

[Block 2545]
སྤྱོད་པ་ཆེན་པོ་ལ་འཛེམ་པས་འཇིགས་ཤིང་སྐྲག་པ་དང་། སྤྱོད་པ་དེ་ལ་ཡིད་ཀྱིས་འཇུག་པར་མི་འདོད་པ་ནི་དངངས་པའི་སྒྲ་དྲག་པོས་ཀུ་ཅོ་འདོན་པ་དང་། ཐེག་པ་ཆེན་པོ་ལ་དབང་མེད་པར་བཅུག་པ་ནི་མི་རུང་བར་བྱས་པར་སེམས་པའོ། །

[Block 2546]
རིངས་པར་མྱུར་དུ་ཞེས་པ་ནི་ཐུགས་རྗེའི་སེམས་གསོལ༌[^2138]པའོ། །

[Block 2547]
གཟུད་དེ༌[^2139]ཞེས་པ་ནི་ཆུང་ངུ་ལས་ཆེན་པོར་བསྐྱུར་བའོ། །

[Block 2548]
མ༌[^2140]རུང་བར་བྱ་ཞེས་པ༌[^2141]ཡང་བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་དཀའ་བ་ལ་བཙུད་པའོ། །

[Block 2549]
བརྒྱལ༌[^2142]ཏེ་ས་ལ་འགྱེལ་ཞེས་པ་ནི་འཁོར་བ་ལ་སྦྱོར་བར་སེམས་པའོ། །

[Block 2550]
མདོ་ལས་དེའི་ཕ་དེ་ཡང་ཉེ་བ་ཞིག་ན་མཆིས་ནས་ཞེས་པ་ནས་གཞན་མི་འཆི༌[^2143]སྟེ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཐེག་པ་རྣམ་གཉིས་དྲང་ཞིང་གཟུད་པ༌[^2144]ལ་དང་པོར་སེམས་བསྐྱེད་པ་དང་། མི་དབུལ་པོ་དགའ་བར་བྱ་བ་དང་། རིན་པོ་ཆེ་བླངས་པ་དང་། དགེ་བའི་རྩ་བ་ལ་གཟུད་པ་དབུལ་པོའི་མིང་བཏགས་པ་དང་། ཐབས་བསྟན་པའོ། །

[Block 2551]
མ་གཟུད་པར༌[^2145]ཞེས་པ་ནི་ཐབས་ཀྱིས་དྲང་བ་ལ་གཟུད༌[^2146]ཅིང་ཕྱིས་ཆེན་པོ་བསྟན་པའི་དོན་ཏོ། །

[Block 2552]
གདོང་དུ་ཆུས་གཏོར་ཞེས་པ་ནི་སྒྲིབ་པ་དང་རྨོངས་པ་བསལ་བའི་དོན་ཏོ། །

[Block 2553]
མདོ་ལས་ཅིའི་སླད་དུ་ཞེ་ན་ཞེས་པ་ནས་འདི་བདག་གི་བུ་ཡིན་ཞེས་སུ་ལ་ཡང་མི་སྨྲ་སྟེ་ཞེས་པའི་བར་དུ་ནི་ཉན་ཐོས་པ་རྣམས་ཐེག་པ་ཆེན་པོ་ལ་དད་པ་སྐྱེ་བའི་སྐལ་བ་ཆུང་བ་ལ་ཐབས་མཁས་པས་ཁད་ཀྱིས་དྲངས་ནས་དེ་བཞིན་གཤེགས་པའི་རིགས་སུ་འགྱུར་བས་དེའི་བུ་ཡིན་ཡང་སུ་ལ་ཡང་མ་སྨྲ༌[^2147]ཞེས་པའི་དོན་ཏོ། །

[Block 2554]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཁྱིམ་བདག་དེས་ཞེས་པ་ནས། གར་དགའ་བར་འགྲོ་ལ་རག་གོ་ཞེས་བགྱིས་པ་ནས། འཚལ་མ་དང་རང་པ་འཚོལ་པའི་སླད་དུ་མཆིས་ཏེ༌[^2148]ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆུང་ངུ་དེ་དག་སོ་སོའི་དབང་པོ་དང་སྦྱར་ནས་ཐེག་པ་ཆེན་པོ་ལ་གཟུད༌[^2149]པའི་དུས་ལ་མ་བབ་སྟེ་ཐབས་ཀྱིས་དྲང་བའི་ཕྱིར་སླར་བཏང་ཞེས་པའོ། །

[Block 2555]
ངོ་མཚར་རྨད་དུ་གྱུར་ཞེས་པ་ནི་དང་པོ་སེམས་བསྐྱེད་ནས་ཐེག་པ་རྣམ་པ༌[^2150]གཉིས་ལ་ཞུགས་པའོ། །

[Block 2556]
དབུལ་པོའི་གནས་སུ་སོང་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་ཀྱི་ཡོན་ཏན་ཆུང་ངུ་ལ་ཞུགས་པའོ། །

[Block 2557]
ཟས་ཚོལ་ཞེས་པ་ནི་ཟག་པ་མེད་པའི་ཆོས་ལ་ཞུགས་པའོ། །

[Block 2558]
མདོ་ལས་དེ་ནས་ཁྱིམ་བདག་དེས་མི་དབུལ་པོ་དེ་དགུག་པའི་སླད་དུ་ཞེས་པ་ནས་ལས་བྱེད་དུ་ཆུག་ཅེས་པའི་བར་དུ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་བསྒོམ་དུ་གཞུག་ཅིང་རྣམ་པར་གྲོལ་བ་ཐོབ་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2559]
མི་གཉིས་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་ཀྱི་བསྟན་པ་ལ་གཟུད༌[^2151]པའོ། །

[Block 2560]
ཐེག་པ་རྣམ་གཉིས་ཀྱི་བསྟན་པ་རྒྱ་ཆུང་ཞིང་ངེས་པའི་དོན་མ་ཡིན་པས་མདོག་མི་སྡུག་ལ་མདངས་ངན་ཞེས་སྦྱར་རོ། །
--- END BLOCKS ---
