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
[Block 2626]
བསྐྱེད་པའི༌[^2299]ཕྱིར་བྱ་བ་ནི་མངོན་དུ་བྱ་བའི་ཕྱིར་རོ། །

[Block 2627]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ༌[^2300]ནི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་བསྐྱེད་པའི༌[^2301]ཕྱིར་འདུན་པ་བསྐྱེད་པ་ལ་སོགས་པ་ལ་ཅིའི་ཕྱིར། ཚད་མེད་པའི་ཚིག་ཤིན་ཏུ་བསྟན་པ་ཞེས་བྱ༌[^2302]ཞེ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2628]
དགེ་བའི་ཆོས་ནི་སྦྱིན་པ་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་སོ། །

[Block 2629]
འདུན་པ་ནི་དགེ་བའི་ཆོས་ཐམས་ཅད་ཀྱི༌[^2303]རྩ་བའོ༌[^2304]ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སྒྲུབ་པའི་དགེ་བའི་ཆོས་ནི་ཚད་མེད་དེ། དེ་སྒྲུབ་པར་འདུན་པ་ཡང་ཚད་མེད་པས་དེ་བས་ན། དེ་ནི་ཚད་མེད་པའི་ཚིག་ཤིན་ཏུ་བརྟན༌[^2305]པའོ། །

[Block 2630]
དགེ་བའི་ཆོས་བསྒྲུབ་པར༌[^2306]འདུན་པ་ལས་བསྒྲུབ་པ༌[^2307]འབྱུང་ཞིང་དགེ་བའི་ཆོས་སྐྱེ་བར་འགྱུར་བས་ན། འདུན་པའི་དགེ་བའི་ཆོས་ཐམས་ཅད་ཀྱི་རྩ་བ་ཞེས་བྱའོ། །

[Block 2631]
ཉམས་སུ་ལེན་པར་བྱེད་ཅེས་བྱ་བ་ནི་མཐར་ཕྱིན་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2632]
དགེ་བའི་ཆོས་དེ་དག་ལ་སྤྱོད་ཅིང་རྣམ་པར་འབྱེད་ཅེས་བྱ་བ་ནི་སྨོན་ལམ་གྱི་དགེ་བའི་ཆོས་སྐྱེས་པ་དེ་དང་དེ་དག་ལ་སོ་སོའི་མཚན་ཉིད་ལ་རྟོག་ཅིང་ཕྱིས༌[^2308]ཀྱང་བསྐྱེད་པར་བྱ་བར༌[^2309]སེམས་པའོ། །

[Block 2633 [HEADING]]
#### བརྩོན་འགྲུས་རབ་ཏུ་བརྟན་པ། ^8-2-4-0

[Block 2634]
བརྩོན་འགྲུས་རབ་ཏུ་བརྟན་པའི༌[^2310]བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་ཡང་དག་པའི༌[^2311]སྤོང་བ་བཞི་པ༌[^2312]ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དགེ་བའི་ཆོས་སྐྱེས་པ་རྣམས་བསྟན་པའི༌[^2313]བསྒོམ་པར་བྱ་བ་ལ་སྒོམ་པར༌[^2314]བྱེད་པའོ། །

[Block 2635]
དེའི་དབང་དུ་བྱས་ནས་གང་ཡང་དགེ་བའི་ཆོས་སྐྱེས་པ་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གནས་པ་ནི་སྔར་སྐྱེས་པ༌[^2315]རྣམས་ལས་དེ་ལས་ཆུང་བར་མི་བྱའོ། །

[Block 2636]
བསྒོམ་པ་ནི་སྔར་སྐྱེས་པ་ལས་ཤས་ཆུང་ཟད༌[^2316]སྐྱེད་པའི་ཕྱིར་དེ་དག་ལ་ཡང་ནས་ཡང་དུ་སྒོམ་པར་བྱེད་པའོ། །

[Block 2637]
ཕྱིར་ཞིང་འབྱུང་བ་ནི་དེ་བས་ཀྱང་ཤས་འབྲིང་དུ་བསྐྱེད་པར་བྱ་བའི་ཕྱིར་ཆུང་ངུ་སྐྱེས་པ༌[^2317]ལ་ཡང་ནས་ཡང་དུ་སྒོམ་པར་བྱེད་པའོ། །

[Block 2638]
ཆུད་ཟ་བ༌[^2318]དང་ཉམས་པར༌[^2319]མི་འགྱུར་བ་དོན་གཅིག་སྟེ་སྐྱེས་པ་རྣམས་ཉམས་པར་མི་བྱེད་པའོ། །

[Block 2639]
ཡང་ན་ཆུད་ཟ་བར༌[^2320]མི་འགྱུར་བ་ནི་ཉམས་པར་མི་བྱེད་པའོ། །

[Block 2640]
ཉམས་པར་མི་འགྱུར་བ་ནི་བརྗེད་པར་མི་བྱ་བའོ།[^2321] །ཤིན་ཏུ་རྒྱས་པར༌[^2322]བྱ་བ་ནི་དགེ་བའི་རྩ་བ་ཐམས་ཅད་མཐར་ཐུག་ཅིང་རྫོགས་པར་བྱ་བའོ། །

[Block 2641]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་དགེ་བའི་ཆོས་སྐྱེས་པ་རྣམས་འདུག་པ་ལ་སོགས་པར་བྱེད་པ་ལ། བྱང་ཆུབ་ཏུ་ཡོངས་སུ་བསྔོས་པའི་དགེ་བའི་རྩ་བ་ཞེས་ཅིའི་ཕྱིར་བྱ༌[^2323]ཞེ་ན་ཞེས་བྱ་བའི༌[^2324]དོན་ཏོ། །

[Block 2642]
མཐར་ཐུག་གི་བར་དུ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་སྙིང་པོ་མ་ཐོབ་ཀྱི་བར་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2643]
ཆུད་མི་ཟ་ཞེས༌[^2325]བྱ་བ་ནི་མེད་པར་མི་འགྱུར། ཉམས་པར་མི་འགྱུར་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། འཕེལ་བར་འགྱུར་ཞིང་རྒྱ་ཆེར་འགྱུར་རོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2644]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཏུ་བསྔོས་པའི་དགེ་བའི་རྩ་བ་དེ། བྱང་ཆུབ་ཀྱི་སྙིང་པོའི་བར་དུ་མཐར་མ་ཐུག་གི་བར་དུ་བར་མ་དོར་ཅིའི་ཕྱིར་ཆུད་ཟ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2645]
ཁམས་གསུམ་པ་ཐམས་ཅད་ལ་མི༌[^2326]གནས་པ་ཞེས་བྱ་བ་ནི་ཁམས་གསུམ་དུ་སྐྱེས་པའི༌[^2327]རྒྱུ་མི་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2646]
ཡོངས་སུ་ཟད་པར་འགྱུར་ཞེས་བྱ་བ་ནི་ཁམས་གསུམ་དུ་འགྱུར་བའི་ཆོས་དེ་དག་ནི་འབྲས་བུ་རྣས་པར་སྨིན་པ་མྱོང་ནས་ཟད་པར་འགྱུར་བའོ། །

[Block 2647]
ཡང་དག་པའི་སྤོང་བ་བཞི་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2648 [HEADING]]
### རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་མི་ཟད་པ། ^8-3-0

[Block 2649]
འདུན་པ་ལ་ཤིན་ཏུ་གནས་པ་དང་། བརྩོན་འགྲུས་ལ་ཤིན་ཏུ་གནས་པ་དང་། སེམས་ལ་ཤིན་ཏུ་གནས་པ་དང་། དཔྱོད་པ་ལ་ཤིན་ཏུ་གནས་པ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^2328]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^2329]རྫུ་འཕྲུལ་གྱི་རྐང་པ་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2650]
དེ་མི་ཟད་པ་ཡང་འདུན་པར་བྱ་བ་ལ་སོགས་པའི་ཆོས་རྣམས་མི་ཟད་པའི་ཕྱིར་མི་ཟད་པའོ། །

[Block 2651]
དེ་ལ་རྫུ་འཕྲུལ་ནི༌[^2330]གོང་དུ་མངོན་པར་ཤེས་པ་ལྔ་བསྟན་པ་འམ། མངོན་པར་ཤེས་པ་ལྔའི་ནང་ན་རྫུ་འཕྲུལ་མངོན་པར་ཤེས་པ་བཤད་པའོ། །

[Block 2652]
རྐང་པ་ནི་རྫུ་འཕྲུལ་དེ་དག་ཐོབ་པར་བྱེད་པའི་རྒྱུ་འམ་གཞིའོ། །

[Block 2653]
དེ་ཡང་རྣམ་པ་བཞིར༌[^2331]རིག་པར་བྱ་སྟེ། རབ་ཏུ་དབྱེ་བ་དང་། རྒྱུ་དང་། གཞི་དང་འབྲས་བུ་མངོན་པར་འགྲུབ་པའོ། །

[Block 2654]
དེ་ལ་འདི་ལྟ༌[^2332]སྟེ། འདུན་པ་དང་ཞེས་བྱ་བ་ནས། དཔྱོད་པའོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རབ་ཏུ་དབྱེ་བ་བསྟན་ཏོ། །

[Block 2655]
དེ་དག་གི༌[^2333]རྩ་བའི་རྟེན་ཞེས་བྱ་བ་ནས་ལས་སུ་རུང་བ་ཐོབ་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རྒྱུ་བསྟན་ཏོ།[^2334] །དེ་སེམས་ལས་སུ་རུང་བ་ཐོབ་པ༌[^2335]ཞེས་བྱ་བ་ནི་སེམས་ཡང་བ་མ་ཐོབ་པ་ཡན་ཆད་ཀྱིས་གཞི་བསྟན་ཏོ། །

[Block 2656]
དེ་ལུས་དང་སེམས་ཡང་བ་ཞེས་བྱ་བ་ནས། ནམ་མཁའི་མཐར་ཐུག་པ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^2336]འབྲས་བུ་མངོན་པར་འགྲུབ་པ་བསྟན་ཏོ། །

[Block 2657 [HEADING]]
#### རབ་ཏུ་དབྱེ་བ། ^8-3-1-0

[Block 2658]
དེ་ལ་འདུན་པ་ནི་གང་གུས་པར་བྱེད་པ་དང་། དད་པ་ལ་བརྟེན་ཏེ་སེམས་རྩེ་གཅིག་པ་ལ་རེག་པར་བྱེད་པའོ། །

[Block 2659]
བརྩོན་འགྲུས་ནི། གང་རྒྱུན་དུ་སྦྱོར་བ་ལ་བརྟེན༌[^2337]ནས་སེམས་རྩེ་གཅིག་པ་ལ་རེག་པར་བྱེད་པའོ། །

[Block 2660]
སེམས་ནི་གང་ཚེ་རབས་གཞན་དང་གཞན་དུ་ཏིང་ངེ་འཛིན་བསྒོམས་པ༌[^2338]ལ་བརྟེན་ནས། ཚེ་འདིར་སེམས་ནི༌[^2339]སྔོན་གྱི་སེམས་དང་རྗེས་སུ་མཐུན་པར་གྱུར་ཏེ། མྱུར་དུ་སེམས་རྩེ་གཅིག་པ་ལ་རེག་པར་གྱུར་པའོ། །

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
--- END BLOCKS ---
