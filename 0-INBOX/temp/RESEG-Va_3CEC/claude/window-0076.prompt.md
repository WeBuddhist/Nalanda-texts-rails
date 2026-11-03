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
དཔྱོད་པ་ནི་བདག་གི་སེམས་ཀྱི་རྒྱུད་ལ་སྡིག་པ་མི་དགེ་བའི་ཆོས་ཡོད་དམ་མེད་ཅེས་རྣམ་པར་དཔྱོད་པ་ལས་སེམས་རྩེ་གཅིག་པ་ལ་རེག་པར་གྱུར་པའོ། །

[Block 2662 [HEADING]]
#### རྒྱུ། ^8-3-2-0

[Block 2663]
དེ་དག་གི་རྩ་བའི་རྟེན་དང་གནས་ནི་ཞེས་བྱ་བ་ལ་དེ་དག་ནི་འདུན་པ་ལ་སོགས་པ་བཞི༌[^2340]དག་གམ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་དག་སྟེ། དེ་དག་གི་རྩ་བའི་གཞི་འམ། རྟེན་དུ་གྱུར་པ་ནི་ཚད་མེད་པ་བཞི་དག་གོ། །

[Block 2664]
དེ་ལ་རྩ་བའི་སྒྲ་ནི་འདུན་པ་ལ་སོགས་པ་ལ་སྙེགས་ཏེ། དེ་དག་ནི་རྫུ་འཕྲུལ་སྐྱེ་བའི་རྩ་བ་ཡིན་པས་སོ། །

[Block 2665]
འདུན་པ་ལ་སོགས་པའི་རྟེན་དང་གནས་ནི་ཚད་མེད་པ་བཞི་ཡིན་ཏེ། ཚད་མེད་པ་བཞི་དང་ལྡན་པའི་སེམས་ཀྱིས་བསྒོམས༌[^2341]དགོས་པས་སོ། །

[Block 2666]
ཚད་མེད་པ་བཞི་ཇི་ལྟར་ན་རྩ་བའི་རྟེན་དང་གཞིར་འགྱུར་སྙམ་པ་ལ། དེ་ཚད་མེད་པ་བཞི་པོ༌[^2342]འདི་དག་ལ་བརྟེན་ཅིང་བསྒོམས༌[^2343]ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་ཞེས་བྱ་བ་ནི་རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་ལ་བསྒོམ་པར་འདོད་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེས་སོ། །

[Block 2667]
བསྟན་པ༌[^2344]ནི་དང་པོ་ཉིད་དུ་ཚད་མེད་པ་བཞི་བསྒོམ་པ་ལ་བརྟེན༌[^2345]པའོ། །

[Block 2668]
བསྒོམ་པ༌[^2346]ནི་དེའི་འོག་ཏུ་ཡང་ནས་ཡང་དུ་མངོན་སུམ་དུ་བྱེད་པའོ། །

[Block 2669]
མང་དུ་བྱས་པ་ནི་ཚད་མེད་པ་བཞི་མཐར་ཕྱིན་པར་བྱ་བའི་ཕྱིར་བསྒོམ་པ་རྒྱུན་མི་གཅོད་པའོ། །

[Block 2670]
སེམས་ལས་སུ་རུང་བ་ཐོབ་པར་འགྱུར༌[^2347]རོ་ཞེས་བྱ་བ་ནི་སེམས་རྩེ་གཅིག་ཏུ་གནས་སུ་བཏུབ་བ༌[^2348]ཐོབ་བར་འགྱུར་བའོ། །

[Block 2671 [HEADING]]
#### གཞི། ^8-3-3-0

[Block 2672]
བསམ་གཏན་དང་པོ་ལ་མཉམ་པར་གཞོག་པ་ལ་སོགས་པ་སྨོས་པ་ནི་བསམ་གཏན་བཞི་པ་ལ་བརྟེན་ནས་རྫུ་འཕྲུལ་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 2673 [HEADING]]
#### འབྲས་བུ་མངོན་པར་འགྲུབ་པ། ^8-3-4-0

[Block 2674]
ལུས་དང་སེམས་ཡང༌[^2349]བ་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་ནི་ལུས་ཡང་བ་ཐོབ་བ་ནི།[^2350] རང་གི་དོན་སྒྲུབ་པ་ལ་མྱུར་དུ་འཇུག་ཏུ༌[^2351]བཏུབ་ཅིང་གཉིད༌[^2352]དང་རྨུགས་པ་ལ་སོགས་པ་མེད་པ་ཐོབ་པའོ། །

[Block 2675]
སེམས་ཡང་བ་ནི་དེ་བཞིན་དུ་རང་གི་བྱ་བ་མྱུར་དུ་འཇུག་ཏུ་བཏུབ་པའོ། །

[Block 2676]
མངོན་པར་ཤེས་པ་ལ་འཇུག་པ་ལ༌[^2353]མངོན་པར་སྒྲུབ་པོ་ཞེས་བྱ་བ་ནི་རྫུ་འཕྲུལ་མངོན་པར་ཤེས་པ་ཐོབ་པར་འགྱུར་བ་བསྒྲུབ༌[^2354]པའོ། །

[Block 2677]
འདུན་པ་ལས་སམ་བརྩོན་འགྲུས་ལས་སམ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དེ་ལྟར་བསྒྲུབ་པ༌[^2355]དང་ལྡན་པ་དེ༌[^2356]ནི་འདུན་པ་ལ་སོགས་པ་གང་ཡང་རུང་བ་ལ་བརྟེན་ནས་རྫུ་འཕྲུལ་གྱི་རྐང་པ་སྐྱེད་པར་བྱེད་པ་སྟེ། རྫུ་འཕྲུལ་གྱི་རྐང་པ་ཞེས་བྱ་བ་ནི་འདིར་རྫུ་འཕྲུལ་ཉིད་ལ་བྱ་བར་འདོད་དོ། །

[Block 2678]
ཡང་ན་འདུན་པ་ལས་སམ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཆོས་དེ་བཞིས༌[^2357]དེ་དག་གི་འབྲས་བུའི་གནས་ཐོབ་པར་བྱེད་པའི་དོན་ཏོ། །

[Block 2679]
རྐང་པ་ནི་འདིར་འབྲས་བུ་ཐོབ་པའི་གནས་ལྟ་བུ་ལ་བྱའོ། །

[Block 2680 [HEADING]]
##### འདུན་པ་ལ་རབ་ཏུ་གནས་པ། ^8-3-4-1-0

[Block 2681]
དེ་ལ་གང་འདུན་པ་ལ་རབ་ཏུ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་རྫུ་འཕྲུལ་གྱི་རྐང་པ་དང་པོ་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས་དེ་ལ་འདུན་པ་ནི་གང་ཆོས་དེ་དག་ལ་མངོན་དུ་ཕྱོགས་པའོ་ཞེས་བྱ་བ་གསུངས་ཏེ། ཆོས་ཞེས༌[^2358]བྱ༌[^2359]བས་འདུན་པའི་ཏིང་ངེ་འཛིན་ཏམ། སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ལ་བྱ་སྟེ། འདུན་པ་ནི་ཆོས་དེ་རྣམས་ལ་ཕྱོགས་ཤིང་མོས་པ་དང་དད་པ་བྱེད་པའོ། །

[Block 2682 [HEADING]]
##### བརྩོན་འགྲུས་ལ་ཤིན་ཏུ་གནས་པ། ^8-3-4-2-0

[Block 2683]
བརྩོན་འགྲུས་ལ་ཤིན་ཏུ་གནས་པ་ནི་རྫུ་འཕྲུལ་གྱི་རྐང་བ་གཉིས༌[^2360]ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། བརྩོན་འགྲུས་ནི་གང་ཆོས་དེ་དག་སྒྲུབ་པའོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 2684]
ཆོས་དེ་དག་སྒྲུབ་པ་ནི་ཚད་མེད་པ་དང་བསམ་གཏན་དང་རྫུ་འཕྲུལ་གྱི་ཆོས་རྣམས་སྒྲུབ་བའོ། །

[Block 2685 [HEADING]]
##### སེམས་ལ་ཤིན་ཏུ་གནས་པ། ^8-3-4-3-0

[Block 2686]
སེམས་ལ་ཤིན་ཏུ་གནས་པ་ནི་གང་རྫུ་འཕྲུལ་གྱི་རྐང་པ་གསུམ་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས་སེམས་ནི་གང་ཆོས་དེ་དག་ལ་རྟོག་པའོ་ཞེས་གསུངས་སོ། །

[Block 2687]
ཆོས་དེ་དག་ལ་རྟོག་པ༌[^2361]ནི་གང་དུ་བཤད་པའི་ཆོས་རྣམས་ལ་ཡིན་ནམ། མ་ཡིན་ཞེས་འཇོག་པའམ། རྩེ་གཅིག་ཏུ་འཇོག་པའོ། །

[Block 2688 [HEADING]]
##### དཔྱོད་པ་ལ་ཤིན་ཏུ་གནས་པ། ^8-3-4-4-0

[Block 2689]
དཔྱོད་པ་ལ་ཤིན་ཏུ་གནས་པ་ནི་གང་རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས་དཔྱོད་པ་ནི་གང་ཆོས་དེ་དག་ལ་མཁས་པ་ཞེས་གསུངས་སོ། །

[Block 2690]
དཔྱོད་ན་ཤེས་རབ་སྟེ། དེ་ནི་གོང་དུ་བཤད་པའི་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པའོ། །

[Block 2691]
དེ་ལྟར༌[^2362]ཏིང་ངེ་འཛིན་བཞི་བསྒོམ་པ་ལ་སྤོང་བའི་འདུ་བྱེད་བརྒྱད་འབྱུང་བར་འགྱུར་ཏེ། འདུན་པ་ནི་ནམ་ཞིག་ན་བདག་གི་ཏིང་ངེ་འཛིན་ཡོངས་སུ་རྫོགས་ཤིང་། སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་ཀྱི༌[^2363]བག་ལ་ཉལ་སྤོང་བར་འགྱུར་ཞིག་གྲུ༌[^2364]སྙམ་དུ་སེམས་པའོ། །

[Block 2692]
རྩོལ་བ་ནི་གཉེན་པོ་བསྒོམ་པ་ལ་སྦྱོར་བ་མི་གཏོང་བའོ། །

[Block 2693]
དད་པ་ནི་སྦྱོར་བ་མ་བཏང་བའི་གོང་དུ་རྟོགས་པར་བྱ་བ་ལ་ཡིད་ཆེས་པའོ། །

[Block 2694]
ཤིན་ཏུ་སྦྱངས་པ་ནི་དད་པ་སྔོན་དུ་བཏང་བའི་དགའ་བ་སྟེ། ཡིད་དགའ་བར་གྱུར་པའི་རིམ་གྱིས༌[^2365]སྡིག་པ་མི་དགེ་བའི་ཆོས་ཀྱི་གནས་ངན་ལེན་སྦྱངས་པའོ། །

[Block 2695]
དྲན་པ་ནི་ཞི་གནས་ཀྱི་སེམས་ཟིན༌[^2366]པའོ། །ཤེས་བཞིན་ནི་ལྷག་མཐོང་ངོ་། །སེམས་པ་ནི་སྤངས་པ་དང་། མ་སྤངས་པ་ལ་སྤྱོད་པ༌[^2367]དང་། ཞི་གནས་དང་ལྷག་མཐོང་དང་། མཐུན་པའི་ལུས་དང་ངག་གི་ལུས་ཀུན་ནས་སློང་བའོ། །

[Block 2696]
[^2368]བཏང་སྙོམས་ནི་སྡིག་པ་མི་དགེ་བའི་ཆོས་དང་མཐུན་པ་དག་ལ་སྤྱོད་པའི་སེམས་ཀུན་ནས་ཉོན་མོངས་པ་མེད་ཅིང༌[^2369]མཉམ་པ་ཉིད་དུ་བྱེད་པའོ། །

[Block 2697]
དེ་ལ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་མངོན་པར་སྒྲུབ་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་དེ་ལ་འདུན་པ་ལ་སོགས་པ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་སྒྲུབ་པ་རྣམས་ཀྱིས༌[^2370]རྫུ་འཕྲུལ་ཡང་དག་པར་སྒྲུབ་པར་བྱེད་དེ། དེ་བས་ན་འདུན་པ་ལ་སོགས་པ་ལ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་ཞེས་བྱའོ། །

[Block 2698]
དེ་ལ་འདུན་པ་དང་རྫུ་འཕྲུལ་གྱི་རྐང་པས་ནི་རྫུ་འཕྲུལ་སྒྲུབ༌[^2371]པའོ། །

[Block 2699]
བརྩོན་འགྲུས་རྫུ་འཕྲུལ་གྱི༌[^2372]རྐང་པས་ནི་རྫུ་འཕྲུལ་མཐར་འབྱིན་པར་བྱེད་དོ། །

[Block 2700]
སེམས་རྫུ་འཕྲུལ་གྱི་རྐང་པས་ནི་མཐར་དབྱུང་བའི་རྫུ་འཕྲུལ་རྣམས་མི་ཉམས་པར་བྱེད་དོ། །
--- END BLOCKS ---
