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
[Block 2626 [HEADING]]
##### ཚིགས་སུ་བཅད་པས་གསོལ་བ། ^4-4-2-2-0

[Block 2627]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་འོད་སྲུངས་ཆེན་པོས་དེའི་ཚེ་ཚིགས་སུ་བཅད་པ་འདི་དག་གསོལ་ཏོ་ཞེས་འཕགས་པ་ཉན་ཐོས་ཆེན་པོ་བཞིས་དོན་འདི་ཆུད་པ་དང་། དྲིས་པར་འདྲ་ན་འདིར་འོད་སྲུངས་གཅིག་པུ་སྨོས་པ་དེ་ཅིའི་ཕྱིར་ཞེ་ན། འོད་སྲུངས་སྐུ་བགྲེས་པའི་ཕྱིར་གཙོར་སྨོས་པས་སོ། །

[Block 2628]
འདི་མན་ཆད་ཚིགས་བཅད་བརྒྱད་ཅུ་རྩ་དྲུག་ཅིག་ཡོད་པ་ལ། བདུན་ཅུ་རྩ་གསུམ་གྱིས་ནི་བཅོམ་ལྡན་འདས་ཀྱི་བཀའ་དྲིན་ཆེན་པོ་ལ་སོགས་པ་བསྟན། ཚིགས་བཅད་བཅུ་གསུམ་གྱིས་ནི་བཅོམ་ལྡན་འདས་ཀྱི་བཀའ༌[^2248]དྲིན་ཟབ་པ་བསྟན་ཏོ། །

[Block 2629 [HEADING]]
###### བཅོམ་ལྡན་འདས་ཀྱི་བཀའ་དྲིན་ཆེན་པོ། ^4-4-2-2-1-0

[Block 2630]
དུམ་བུ་དང་པོ་ལ་ཡང་གསུམ་དུ་དབྱེ་སྟེ།

[Block 2631]
དང་པོ་ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་དོན་བསྟན། དེའི་འོག་གི་ཚིགས་བཅད་བཞི་བཅུ་རྩ་གཅིག་གིས་ནི༌[^2249]དཔེ་བསྟན། དེའི་འོག་མ་ཚིགས་བཅད་སུམ་ཅུ་རྩ་གཅིག་གིས་ནི་དཔེ་དང་དོན་དུ་སྦྱོར་བ༌[^2250]བསྟན་ཏོ།[^2251] །དེ་ཡང་ཐོས་པ༌[^2252]ཉི་ཚེ་སྨོས་ཀྱི་ཚིག་གཞན་མ་སྨོས་སོ། །

[Block 2632 [HEADING]]
###### **དོན་བསྟན་པ།** ^4-4-2-2-1-1-0

[Block 2633]
དེ་ལ་ཡང་ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་དོན་རྣམ་པ་གཉིས་བསྟན། ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་དཔེ་བསྟན།

[Block 2634 [HEADING]]
###### **དཔེ་བསྟན་པ།** ^4-4-2-2-1-2-0

[Block 2635]
མདོ་ལས་ཇི་ལྟར་སྐྱེས༌[^2253]བུ་བུས་པར་གྱུར་པ་ཞིག །འགྲོ་བའི་བྱིས་པ་རྣམས་ཀྱིས་བསླུས་པ་སྟེ་ཞེས་པ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་བཞི་བཅུ་རྩ་གཅིག་གིས་དཔེ་འཆད་དེ།[^2254] དེ་ལ་ཡང་གཉིས་སུ་དབྱེའོ། །

[Block 2636]
ཚིགས་བཅད་སུམ་ཅུ་རྩ་བཞིས་ནི་སྔར་རེ་བ་མེད་པ་བསྟན། ཚིགས་བཅད་བདུན་གྱིས་ནི་འདི་ཐོབ་པ་བསྟན་ཏོ། །

[Block 2637 [HEADING]]
###### **སྔར་རེ་བ་མེད་པ།** ^4-4-2-2-1-2-1-0

[Block 2638 [HEADING]]
###### **སེམས་བསྐྱེད་པའི་དཔེ།** ^4-4-2-2-1-2-1-1-0

[Block 2639]
དེ་ལ་ཡང་དང་པོའི༌[^2255]ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི༌[^2256]སེམས་བསྐྱེད་པའི་དཔེ་བསྟན། དེའི་འོག་མ་གཅིག་གིས་ནི་འཁོར་བར་ལྡོག་པའི་དཔེ་བསྟན། དེའི་འོག་མ་བདུན་གྱིས་ནི་སངས་རྒྱས་མཐོང་བའི་དཔེ་བསྟན། དེའི་འོག་མ་བཅུ་བཞིས་ནི་ཆེན་པོ་སྒྲུབ༌[^2257]ཏུ་མི་བཏུབ་པའི་དཔེ་བསྟན། དེའི་འོག་མ་ཕྱེད་དང་བཅུས་ནི་ཐེག་པ་རྣམ་གཉིས་དྲང་བའི་དཔེ་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས་ནི་ཆེན་པོ་ལ་རེ་བ་མེད་པའི་དཔེ་བསྟན་ཏེ་འདི་ནི་དང་པོའོ། །

[Block 2640 [HEADING]]
###### **འཁོར་བར་ལྡོག་པའི་དཔེ།** ^4-4-2-2-1-2-1-2-0

[Block 2641]
མདོ་ལས།

[Block 2642]
ཕ་ཡི་གནས་ནས༌[^2258]གལ་ཏེ་སོང་བ་ནི། །ཞེས་པ་ནས། ལོ་ནི་ལྔ་བཅུ་ལས་ཀྱང་མི་ཉུང་བར་ཞེས་པའི་བར་དུ་ནི་འཁོར་བར་ལོག་པའི་དཔེ་བསྟན། ལྔ་བཅུ་ནི་འགྲོ་བ་རྣམ་ལྔའི་དཔེ་སྟེ། གཞན་དུ་འཁྱམས་ཞེས་པའི་དོན་ཏོ། །

[Block 2643 [HEADING]]
###### **སངས་རྒྱས་མཐོང་བའི་དཔེ།** ^4-4-2-2-1-2-1-3-0

[Block 2644]
མདོ་ལས།

[Block 2645]
དེས་ནི་དེ་ལྟ་བུ་དེ་ཚོལ་བ༌[^2259]ན། །ཞེས་པ་ནས། དེ་བཞིན་ཕྱུགས་དང་བ་ལང་ལུག་རྣམས་ཏེ། །ཞེས་པའི་བར་དུ་འདིས་ནི་སངས་རྒྱས་མཐོང་བ་དང་། དེ་བཞིན་གཤེགས་པའི་ཐུགས་རྗེ་སྐྱེ་བའི་དཔེ་བསྟན་ཏེ། ཕྱོགས་དང་ཕྱོགས་མཚམས་སུ་ཕྱིན་ཞེས་པ་ནི་འཁོར་བར་འཁྱམས་ཞེས་པའི་དོན་ཏེ། གྲོང་ཁྱེར་ཆེན་པོར་ཕྲད་ཅེས་པ་ནི་ཐེག་པ་ཆེན་པོའི་གནས་སུ་སོན་པའི་དོན། ཁྱིམ་བརྩིགས༌[^2260]ཞེས་པ་ནི་ཐུགས་རྗེ་ཆེན་པོས་བསྐྱབ༌[^2261]ཞེས་པའི་དོན། འདོད་པ་རྣམ་ལྔ་ལ་སོགས་པ་ལོངས་སྤྱོད་པ་ནི་ཆོས་རྣམ་པར་དག་པའི་དབྱིངས་ལ་ལོངས་སྤྱོད་པ་ཤིང་རྟ་དང་བཞོན་པ༌[^2262]རྣམས་ནི་ཐེག་པའི་དོན་ཏོ། །

[Block 2646]
མདོ་ལས།

[Block 2647]
འཕེལ་ཞིང་འདུ་བ་དང་ནི་དེ་བཞིན་ཞིང་། །ཞེས་པ་ནས། འདི་ལྟར་བདག་ལ་མཛོད་ནི་མང་དུ་ཡོད། །ཅེས༌[^2263]པའི་བར་དུ་ནི་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་དུ་དགེ་བ་སྣ་ཚོགས་ཀྱིས་སེམས་ཅན་སྡུད་པ་སྟེ། བསྡུ་བ༌[^2264]དང་འཕེལ་བའི་ཁེ་འཚོལ༌[^2265]བའོ། །

[Block 2648]
ཀུན་གྱིས་གུས་པར་བྱ་ཞིང་བཀུར་བས་སེམས་ཅན་དོན་བྱེད་པ་བསྟན་པའོ། །

[Block 2649]
རྒས་ལ་ཞོམ་ཞིང་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོའི་ཆོས་ལ་གནས་ཤིང་ཞེས༌[^2266]པའི་རྒྱས༌[^2267]རྒན་པ་ཐུགས་རྗེ་ཆེན་པོས་ཉིན་མཚན་གཅིག་ལ་ལན་དྲུག་དྲུག་སེམས་ཅན་གྱི་ཁམས་སུ་གཟིགས་པས་གདུང་བར་གྱུར་པའོ། །

[Block 2650]
མདོ་ལས།

[Block 2651]
བདག་ནི་འཆི་བའི་དུས་ལ་ཉེ་བར་གྱུར། །ཞེས་པ་ནས། ལ་ལ་སྐྱེད་དང་སྦོགས་ཀྱང་རབ་ཏུ་གཏོང་། །ཞེས་པའི་བར་དུ་ནི་ཆོས་ཀྱི་ཟས་ཀྱིས༌[^2268]རབ་ཏུ་ཕོངས་པའི༌[^2269]ཕྱིར་བཀྲེས་པའོ། །

[Block 2652]
སྤྱོད་པ་དམ་པ་མ་རྫོགས་པའི་ཕྱིར་རིད་པའོ། །

[Block 2653]
ལྟ་བ་ངན་པས་བསྒྲིབས༌[^2270]པའི་ཕྱིར་གཡན་པ་བྱུང་བ་ལྟ་བུའོ། །

[Block 2654]
ལྷག་པའི་སྡོམ་པས་མ་བསྡམས་པའི་ཕྱིར་སྐམ༌[^2271]པོས་གཡོགས་པ་ལྟ་བུའོ། །

[Block 2655]
མཐར་གྱིས་རྒྱུ་ཞེས་པ་ནི་ཡང་དག་པའི་དོན་ཚོལ་བའོ། །

[Block 2656]
ཕའི་ཁྱིམ་དུ་ཕྱིན་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོ་དབུ་མའི་ལམ་དུ་ཞུགས་པ་ཞེས་པའི་དོན་ཏོ། །

[Block 2657]
སྒོ་ན་འདུག་ཅེས་པ་ནི་འབྲས་བུའི་སྒོ་ནི་རྒྱུ་ཡིན། དོན་དང་བསྟན་པ་ནི་ཕུགས་དང་སྒོ་ལྟ་བུར་བལྟའོ། །

[Block 2658]
བགྲང་བ་ནི་འཕགས་པའི་ནོར་རྣམས་སེམས་པའོ། །

[Block 2659]
སྐྱེད་དང་སྤོགས་གཏོང་ཞེས་པ་ནི་ཕྱི་ནང་གི་སྤྱོད་པས་ཕན་འདོགས་པའོ། །

[Block 2660 [HEADING]]
###### **ཆེན་པོ་སྒྲུབ་ཏུ་མི་བཏུབ་པའི་དཔེ།** ^4-4-2-2-1-2-1-4-0

[Block 2661]
མདོ་ལས།

[Block 2662]
དེ་ནས༌[^2272]དབུལ་པོ་དེས་ནི་དེ༌[^2273]མཐོང་བ། ། ཞེས་པ་ནས། ཁྱོད་ནི་གླ༌[^2274]ཡང་ཉིས་འགྱུར་སྦྱིན་པར་བྱས། །ཞེས་པ། འདིར་ནི་ཉེས་པར་གྱུར་ན་མི་རུང་སྟེ། །ཞེས་པ་ཡང་སྔོན་གྱི་སྤྱོད་པ་དང་བྲལ་ཏེ་ཆེན་པོ་སྤྱོད་དུ་མ་བཅུག་གམ་ཞེས་དོགས་པ་སྐྱེའོ།[^2275] །ཞར་བ་འཐེང༌[^2276]གྲུམ་ཅན་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་ཀྱི་བདེན་པ་སྟོན་པ་གཞུང་མ་རྫོགས་པའི་དཔེའོ། །

[Block 2663 [HEADING]]
###### **ཐེག་པ་རྣམ་གཉིས་དྲང་བའི་དཔེ།** ^4-4-2-2-1-2-1-5-0

[Block 2664]
མདོ་ལས།

[Block 2665]
མི་དེས་འདི་ལྟ་བུ་ཡི་སྒྲ་ཐོས་ནས། །ཞེས་པ་ནས། ང་ཡི་བུ་ཡིན་ཡང་དག་གདོན་མི་ཟ། །ཞེས་པའི་བར་དུ་ནི་ཉོན་མོངས་པའི་ཕྱག་དར་བྱས་ཤིང་ཕུང་པོ་ལྔའི་ཁང་པ་གཙང་མར་བྱས་པ་དང་། རྐང་པ་བསྐུ་ཞེས་པ། རྐང་པ་ནི་རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞིའོ། །
--- END BLOCKS ---
