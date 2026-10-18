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
[Block 2836 [VERSE]]
དེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེའོ། །
བཟོའི་ལས་ནི་དྲ་བ་བཙེམ༌[^2480]པ་ལ་སོགས་ཏེ།
[^2481] བཟོ་རིག་པ་རང་གི་མིང་གིས་བསྟན་ཏོ། །

[Block 2837]
རིག་པ་ཞེས་སྨོས་པ་ནི་རིག་པའི་གནས་ལྷག་མ་གསུམ་བསྟན་ཏོ། །

[Block 2838]
སྔགས་ནི་གཞན་གྱི་དམག་གི་སྡེ་མནན་པ་དང་། སྦྲུལ་ལ་སོགས་པའི་དུག་མེད་པར་བྱ་བའི་ཐབས་སོ། །

[Block 2839]
སྟོབས་ནི་མཚོན་ཆ་འཕང་བ༌[^2482]དང་། གླང་པོ་ཆེ་འདེགས་པ་ལ་སོགས་པའི་རྩལ་ལོ། །

[Block 2840]
མངོན་དུ་འགྱུར་བ་ནི་ཤེས་པར་གྱུར་པའོ། །

[Block 2841]
དམ་པ་ཞེས་བྱ་བ་ནི་ལས་སུ་བྱ་བ་དང་། ཤེས་པར་བྱ་བ་གཙོ་བོར་གྱུར་པ་སྟེ། བྱ་དཀའ་བ་ནི་བསྒྲུབ༌[^2483]ཅིང་ཤེས་པར་བྱ༌[^2484]དཀའ་བའོ། །

[Block 2842]
བཟོད་པར་དཀའ་བ་ནི་དེ་དག་སྒྲུབ་པ༌[^2485]ན༌[^2486]སྡུག་བསྔལ་ཉམས་སུ་བླང༌[^2487]དཀའ་བའོ། །

[Block 2843]
ཐོབ་པར་དཀའ་བ་ནི་འབྲས་བུ་ཐོབ་པར་བྱ་དཀའ་བའོ། །

[Block 2844 [HEADING]]
##### འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ལ་མི་ཐུལ་བར་ཤེས་པ། ^8-5-5-2-0

[Block 2845]
འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་གང་དང་གང་དག་གིས༌[^2488]འཇིག་རྟེན་ལས་འདའ་བ༌[^2489]ཞེས་བྱ་བ་ནི་འཕགས་པའི་ལམ་གང་གིས་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་འགྱུར་བའི་ལམ་དེ༌[^2490]དག་ཤེས་སོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2846]
བཅས་པ་ཞེས་བྱ་བའི་སྒྲས་མི་དང་བདུད་ལ་སོགས་པ་ཡང་བསྡུས་པ་ཡིན་ནོ། །

[Block 2847]
མི་བརྫི་བ༌[^2491]ནི་དེ་དག་གི་ཤེས་པས་མི་ཐུབ༌[^2492]པའོ། །

[Block 2848]
སྟོབས་ལྔ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2849 [HEADING]]
### བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན་མི་ཟད་པ། ^8-6-0

[Block 2850]
དྲན་པ་ཤིན་ཏུ་འབྲེལ་པ་དང་། རབ་ཏུ་ཤེས་པ་ཤིན་ཏུ་འབྲེལ་པ་དང་། བརྩོན་འགྲུས་ཤིན་ཏུ་འབྲེལ་པ་དང་། དགའ་བ་ཤིན་ཏུ་འབྲེལ་པ་དང་། བག་ཡངས་ཤིན་ཏུ་འབྲེལ་པ་དང་། ཏིང་ངེ་འཛིན་ཤིན་ཏུ་འབྲེལ་པ་དང་། བཏང་སྙོམས་ཤིན་ཏུ་འབྲེལ་པ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^2493]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^2494]བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཅེས་བྱ་བ་གསུངས་ཏེ། འདི་བསྡུས་པའི་དོན་མཐོང་བའི་ལམ་བསྟན་པར་ཡང་སྦྱར་རོ། །

[Block 2851]
བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཅེས་བྱ་བ་ལ། བྱང་ཆུབ་ནི་ཟད་པ༌[^2495]མི་སྐྱེ་བའི་ཡེ་ཤེས་རྣམ་པར་མི་རྟོག་པའི་རང་བཞིན་ལ་བྱའོ། །

[Block 2852]
དྲན་པ་ལ་སོགས་པ་བདུན་པོ་འདི་རྣམས་ནི་བྱང་ཆུབ་དེ་ཐོབ་པར་བྱེད་པའི་རྒྱུ་འམ། གྲོགས་ཡིན་པས་ན་ཡན་ལག་ཅེས་བྱ་སྟེ། ཇི་ལྟར་ཡན་ལག་ཡིན་པར་ནི་ཕྱིས་བཤད་དོ། །

[Block 2853]
དེ་དག་མི་ཟད་པ་ཡང་དྲན་པར་བྱ་བ་ལ་སོགས་པའི་ཆོས་རྣམས་མི་ཟད་པའི་ཕྱིར་མི་ཟད་པའོ། །

[Block 2854 [HEADING]]
#### དྲན་པ་ཤིན་ཏུ་འབྲེལ་པ། ^8-6-1-0

[Block 2855]
དྲན་པ་ཤིན་ཏུ་འབྲེལ་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་ཡང་དག་པའི་ངེས་པ་ཉམས༌[^2496]འོག་ཏུ་ཆུད་ཅིང་། དྲན་པ༌[^2497]ཡང་དག་པའི་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་དྲན་པ་ཡང་དག༌[^2498]བྱང་ཆུབ་ཀྱི་ཡན་ལག་གང་ཞེ་ན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 2856]
དྲན་པ་ཤིན་ཏུ་འབྲེལ་པ་ལ་ཇི་ལྟ་བ་དེ་བཞིན། བཏང་སྙོམས་ཤིན་ཏུ་འབྲེལ་པའི་བར་དུ་ཅི་རིགས་པར་ཤེས་པར་བྱ་སྟེ། འདིར་ཡང་བསྟན་པ་དང་བཤད་པའི་ཚུལ་ནི་གོང་མ་བཞིན་དུ་ལྟའོ། །

[Block 2857]
དྲན་པ་གང་གིས་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་སེམས་ལ་གསལ་ཞིང་མ་བརྗེད་པའི༌[^2499]དྲན་པ་གང་གིས་སོ། །

[Block 2858]
ཆོས་རྣམས་རྟོག་པར༌[^2500]འགྱུར་བ་ཞེས་བྱ་བ་ནི་མདོར་བསྟན་པའི་ཚིག་སྟེ། ལྷག་མ་རྣམས་ནི་བཤད་པའི་ཚིག་གོ། །

[Block 2859]
དྲན་པས་རྟོགས་པའི༌[^2501]ཆོས་རྣམས༌[^2502]ཀྱང་རྣམ་པ་གསུམ་སྟེ། ཆོས་ཀྱི་དབྱིངས་རྟོགས་པ་དང་། དེའི་ལམ་རྟོགས་པ་དང་། ལམ་དེ་སྟོན་པའི་གཞུང་རྟོགས༌[^2503]པའོ། །

[Block 2860 [HEADING]]
##### ཆོས་ཀྱི་དབྱིངས་རྟོགས་པ། ^8-6-1-1-0

[Block 2861]
ཆོས་རྣམས་ལ་སོ་སོར་རྟོག་པ་ཞེས་བྱ་བས༌[^2504]ཆོས་ཀྱི་དབྱིངས་རྟོགས་པ༌[^2505]བསྟན་ཏེ། སོ་སོར་གྱི་སྒྲ་ཕྱིན་ཅི་མ་ལོག་པའི་སྒྲར་འགྲོ་བས་ཆོས་རྣམས་ཀྱི༌[^2506]ཆོས་ཀྱི་དབྱིངས་མངོན་སུམ་དུ་གྱུར་པའོ། །

[Block 2862 [HEADING]]
##### ལམ་རྟོགས་པ། ^8-6-1-2-0

[Block 2863]
ཆོས་རྣམས་ལ་དཔྱོད་པ༌[^2507]དང་ཞེས་བྱ་བས་དེའི་ལམ་རྟོགས་པ༌[^2508]བསྟན་ཏེ། ཆོས་ཀྱི་དབྱིངས་རྟོགས་པར༌[^2509]བྱ་བའི་ལམ་གང་ཡིན་པ་ཁོང་དུ་ཆུད་པའོ། །

[Block 2864 [HEADING]]
##### ལམ་སྟོན་པའི་གཞུང་རྟོགས་པ། ^8-6-1-3-0

[Block 2865]
ཆོས་རྣམས་ལ་ཀུན་དུ་འགྲོ་བ་ཞེས་བྱ་བས་ལམ་དེ་སྟོན་པའི༌[^2510]གཞུང་རྟོགས་པ་བསྟན་ཏེ། ལམ་དེ་སྟོན་པའི་གསུང་རབ་ཀྱི་ཆོས་རྣམས་གང་དང་གང་གི༌[^2511]ཕྱོགས་སུ་རྟོགས་པ་སེམས་ལ་རྟོགས་ཤིང་གཞན་ལ་སྟོན་པ་ལ་ཡང་ནོར་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2866]
དེ་ཡང་བསམ་པ༌[^2512]དང་བསྒོམ་པའི༌[^2513]ཤེས་རབ་ཀྱིས་དེ།[^2514] ཆོས་རྣམས་ལ་བསམ་པ༌[^2515]དང་ཞེས་བྱ་བས་བསམ་པའི༌[^2516]ཤེས་རབ་བསྟན་ཏེ། ཆོས་རྣམས་ཀྱི་དོན་ཁོང་དུ་ཆུད་པའི་ཕྱིར་རོ། །

[Block 2867]
ཆོས་རྣམས་ལ་རྗེས་སུ་རྟོགས་པ༌[^2517]ཞེས་བྱ་བས་བསྒོམ་པའི༌[^2518]ཤེས་རབ་བསྟན་ཏེ། བསམ་པས༌[^2519]རྙེད་པའི་ཆོས་ལ་ཡང་ནས་ཡང་དུ་བསྒོམ་པའི་ཕྱིར་ཏེ༌[^2520]དེ་ནི་དྲན་པའོ།[^2521] །

[Block 2868 [HEADING]]
#### རབ་ཏུ་ཤེས་པ་ཤིན་ཏུ་འབྲེལ་པ། ^8-6-2-0

[Block 2869]
རབ་ཏུ་ཤེས་པ་ཤིན་ཏུ་འབྲེལ་པ་ནི་གང་ཆོས་རྣམ་པར་འབྱེད་པ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ལ་ཤིན་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། ཆོས་རྣམ་པར་འབྱེད་པ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་གང་ཞེ་ན་ཞེས་བྱ་བ༌[^2522]ལ་སོགས་པ་གསུངས་སོ། །

[Block 2870]
རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ཤེས་པ་ནི། རྣམ་པར་འབྱེད་པ་ཤེས་པའོ། །

[Block 2871]
དེ་ཉིད་ཀྱི་དོན་གང་ཡིན་པ་བསྟན་པའི་ཕྱིར་གང་དང་གང་། ཇི་ལྟ་ཇི་ལྟ་བུར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཆོས་གང་དང་གང་། གང་གི་ཆ་དང་ཕྱོགས་སུ་གཏོགས་པ་ཇི་ལྟ་ཇི་ལྟ་བུར་དེའི་ཟླ་དང་ཕྱོགས་སུ་བསླན་ཞིང་། དབྱེ་བར་བྱ་བའི་ཆོས་དེ༌[^2523]དང་དེ་དག་ལ་འདི་ནི་འདིའི༌[^2524]ཕྱོགས་སུ་གཏོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་། [^2525]གང་དང་གང་གི་ཟླ་ལ་གཏོགས་པ་ཤེས་ཤིང་། ཆ་ཆར་སོ་སོར་རྣམ་པར་འབྱེད་པ་ཤེས་པའོ། །

[Block 2872]
བརྡ་དང་རྣམ་པར་ངེས་པ་ནི་ཐ་སྙད་དང་གཏན་ལ་ཕབ་པའི་དོན་ལ་བྱ་སྟེ། ངེས་པའི་དོན་ནས་རྣམ་པར་ངེས་པའི་བར་གྱི་ཆོས་གང་དང་གང་གསུངས་པ་དེ་དག་ཀྱང་དེ་དག་སོ་སོའི་སྡེ་ཚན་དུ་གཏོགས་པར་ཤེས་པའོ།[^2526] །

[Block 2873 [HEADING]]
#### བརྩོན་འགྲུས་ཤིན་ཏུ་འབྲེལ་པ། ^8-6-3-0

[Block 2874]
བརྩོན་འགྲུས་ཤིན་ཏུ་འབྲེལ་པ་ནི་བརྩོན་འགྲུས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ལ་རབ་ཏུ་ཞུགས་ཏེ། དེ་བསྟན་པའི་དབང་དུ་བྱས་ནས། དེ་ལ་བརྩོན་འགྲུས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་གང་ཞེ་ན༌[^2527]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2875]
འདི་ཞེས་བྱ་བའི་ཚིག་གོང་དུ་བསྟན་པ་ཆོས་རྣམ་པར་འབྱེད་པ་ལ་སོགས་པ་སྙེགས༌[^2528]སོ། །
--- END BLOCKS ---
