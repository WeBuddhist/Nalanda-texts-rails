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
[Block 2766]
དྲན་པའི་དབང་པོས་ནི་དགེ་བའི་ཆོས་རྣམས་ཆུད་མི་ཟ་བ༌[^2408]ལ་དབང་བྱེད་དེ། དེས་མི་བརྗེད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2767]
ཏིང་ངེ་འཛིན་གྱི་དབང་པོས་ནི་གཞན་དུ་མི་གཡེང་བ་ལ་དབང་བྱེད་དེ། དེས་དམིགས་པའི་ཡུལ་ལ་རྩེ་གཅིག་ཏུ་འཇོག་པས༌[^2409]སོ། །

[Block 2768]
ཤེས་རབ་ཀྱི་དབང་པོས༌[^2410]ནི་མཐར་འབྱིན་པ་ལ་དབང་བྱེད་དེ། དེས་དགེ་བའི་ཆོས་ཐམས་ཅད་མཐར་འབྱིན་པར་བྱེད་པས་སོ། །

[Block 2769]
དབང་པོ་ལྔ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2770 [HEADING]]
### སྟོབས་ལྔ་མི་ཟད་པ། ^8-5-0

[Block 2771]
དད་པ་མི་ཚུགས་པ་དང་། བརྩོན་འགྲུས་མི་ཚུགས་པ་དང་། དྲན་པ་མི་ཚུགས་པ་དང་། [^2411]ཏིང་ངེ་འཛིན་མི་ཚུགས་པ་དང་། ཤེས་རབ་མི་ཚུགས་པ་བསྟན་པའི༌[^2412]ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^2413]ཏིའི་བུ་གཞན༌[^2414]ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སྟོབས་ལྔ་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2772]
འདིར་ཡང་བསྟན་པ་དང་བཤད་པའི་ཚུལ་དུ་རིག་པར༌[^2415]བྱ་སྟེ། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སྟོབས་ལྔ་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཤེས་རབ་ཀྱི་སྟོབས་ཞེས༌[^2416]བྱ་བ་ཡན་ཆད་ནི་བསྟན་པའི་ཚུལ་ལོ། །

[Block 2773]
ལྷག་མ་རྣམས་ནི་བཤད་པའི་ཚུལ་ལོ།[^2417] །དད་པ་ལ་སོགས་པ་ལྔ་པོ་འདི་རྣམས་ལ༌[^2418]སྟོབས་ཞེས་བྱ་བ་ཡང་དབང་པོའི་ཚེ་ན་ནི་དད་པར་བྱ་བ་ལ་སོགས་པ་ཆོས་རྣམས་མངོན་དུ་བྱ་བ༌[^2419]དང་། སྒྲུབ་པར་བྱེད་པ་ལ་དབང་བྱེད་པ་ཙམ་དུ་ཟད་ཀྱི། མི་མཐུན་པའི་ཕྱོགས་རྣམས་ཀྱིས༌[^2420]མི་ཚུགས་པ་མ་ཡིན་ནོ། །

[Block 2774]
སྟོབས་ཀྱི་དུས་ན་ནི་དད་པ༌[^2421]ལ་སོགས་པ་དེ་དག་ཉིད་རབ་ཏུ་བསྒོམས་ཤིང་སྦྱངས་ཏེ་མཐུ་དང་ལྡན་པར་གྱུར་པས། མ་དད་པ་ལ་སོགས་པའི་མི་མཐུན་པའི་ཕྱོགས་རྣམས་ཀྱིས་མི་ཚུགས་པ་ལ་སྟོབས་ཞེས་བྱའོ། །

[Block 2775]
དེ་མི་ཟད་པ་ཡང་དེ་དག་གིས་དད་པར་བྱ་བའི་ཆོས་རྣམས་མི་ཟད་པས་དེ་ལ་དད་པར༌[^2422]བྱེད་པ་མི་ཟད་པའམ། མ་དད་པ་ལ་སོགས་པས་མེད་པར་བྱ་ཞིང་ཟད་པར་བྱ་བར་མི་ནུས་པས་ན་མི་ཟད་པའོ། །

[Block 2776 [HEADING]]
#### དད་པ་མི་ཚུགས་པ། ^8-5-1-0

[Block 2777]
དད་པ་མི་ཚུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་དད་པའི་སྟོབས་ཤིན་ཏུ་བསྒོམས་ཤིང་། མ་དད་པ་དང་མ་འདྲེས་པའི་ཆོས་ཅན་ཡིན་ཏེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་དད་པའི་སྟོབས་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2778]
དད་པ༌[^2423]མི་ཚུགས་པ་ལ་ཇི་ལྟ་བ་བཞིན་ཤེས་རབ་མི་ཚུགས་པའི་བར་དུ་ཡང་སྦྱར་རོ། །

[Block 2779]
མོས་པ་ནི་གང་སྒྲུབ་པ༌[^2424]དང་བྱ་བའི་ཆོས་རྣམས་བསྒྲུབ་པར་འདོད་པ་དང་། བྱ་བར་འདོད་པའོ། །

[Block 2780]
དད་པ་ནི་བདེན་པ་དང་དཀོན་མཆོག་ལ་སེམས་དང་ཞིང་ཡིད་ཆེས་པའོ། །

[Block 2781]
མི་བརྫི་བ༌[^2425]ནི་གཞན་གྱིས་མི་ཟློགས་ཤིང་མི་ཚུགས་པ་དང་། དེའི་དད་པའི་སྟོབས་སོ། །

[Block 2782]
དེ་ཉིད་ཀྱི་དོན་གསལ་བར་བསྟན་པའི་ཕྱིར།[^2426] གལ་ཏེ་བདུད་སྡིག་ཅན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2783]
སངས་རྒྱས་ཀྱི་གཟུགས་ཀྱིས༌[^2427]ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་གཟུགས་སུ་བསྒྱུར་ཏེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2784]
ཆོས་ལ་ངེས་པར་སེམས་པའི་མོས་པ་ཞེས་བྱ་བ་ནི་ཆོས་གང་ལ་སེམས་པའི་མོས་པ་དང་དད་པའོ། །

[Block 2785]
འབྲལ་བར་བྱེད་ཅེས་བྱ་བ་ནི་གཏོང་དུ་འཇུག་པའོ། །

[Block 2786]
འདུན་པ་ཟློག༌[^2428]ཅེས་བྱ་བ་ནི་ཐབས་སྣ་ཚོགས་ཀྱིས༌[^2429]ལྟ་བ་གཞན་ལ་འཇུད་པར་བྱེད་པའོ། །

[Block 2787]
བསྐྱོད་པ་ལ་སོགས་པའི་ཚིག་ནི་མོས་པ་ལས་བཟློག་བར་མི་ནུས་པའི་རྣམ་གྲངས་སོ། །

[Block 2788]
ཡང་ན་ཉན་པའི་དུས་ན་མོས་པ་བཟློག་པར༌[^2430]མི་ནུས་པ་ནི་བསྐྱོད་པར་མི་ནུས་པའོ། །

[Block 2789]
སེམས་པའི་དུས་ན་དད་པ་བཟློག་པར་མི་ནུས་པ་ནི་བསྒུལ་བར་མི་ནུས་པའོ། །

[Block 2790]
བསྒོམ་པའི་དུས་ན་དད་པ་བཟློག་པར་མི་ནུས་པ་ནི་བསླང་བར་མི་ནུས་པའོ། །

[Block 2791 [HEADING]]
#### བརྩོན་འགྲུས་མི་ཚུགས་པ། ^8-5-2-0

[Block 2792]
བརྩོན་འགྲུས་མི་ཚུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་བརྩོན་འགྲུས་ཀྱི་སྟོབས་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་བརྩོན་འགྲུས་ཀྱི་སྟོབས་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2793]
བརྩོན་འགྲུས་བརྩམས་པ༌[^2431]གང་དང་གང་རྩོམ་པ་ཞེས་བྱ་བ་ནི་བརྩོན་འགྲུས་བརྒྱད་པོ་སྔར་བསྟན་པ་གང་དང༌[^2432]གང་གིས་དགེ་བ་གང་ལ་རྩོམ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2794]
དགེ་བའི་ཆོས་གང་དང་གང་ལ་སྦྱོར་བ་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་ལ་སོགས་པའི་དགེ་བའི་ཆོས་གང་དང་གང་བྱེད་པ་སྟེ། །རྩོམ་པ་ནི་དང་པོ་ཉིད་དུ་དགེ་བའི་ཆོས་རྩོམ་པར་བྱེད་པའོ། །

[Block 2795]
སྦྱོར་བ་ནི་དེ་ཕན་ཆད་རྒྱུན་དུ་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 2796]
དེ་དང་དེ་ལ་ཞེས་བྱ་བ་ནི་དགེ་བའི་ཆོས་བརྩམས་ཤིང་སྦྱར་བ༌[^2433]དེ་དང་དེ་ལའོ། །

[Block 2797]
སྟོབས་སྐྱེད་པ་ཞེས་བྱ་བ་ནི་བརྩོན་འགྲུས་ཀྱི་མཐུ༌[^2434]སྐྱེད་པའོ། །

[Block 2798]
སྲ་བ་འཐོབ་སྟེ་ཞེས་བྱ་བ་ནི་བརྩོན་འགྲུས་བརྟེན༌[^2435]ཞིང་མི་ཟློགས་པ་ཐོབ༌[^2436]ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2799]
སྟོབས་སྐྱེད་པ༌[^2437]དེ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་བརྩོན་འགྲུས་ཀྱི་མཐུ་སྐྱེད་པ༌[^2438]དེ་དེ་དང་ལྡན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2800]
གནས་དེ་ལས་མ་བརྒལ་གྱི་བར་དུ་ཞེས་བྱ་བ་ནི་གང་བསྒྲུབ་པར༌[^2439]བྱ་བའི་གནས་དེ་མཐར་ཕྱིན་གྱི་བར་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2801]
ལྷར་བཅས་པའི་འཇིག་རྟེན་ཞེས་བྱ་བ་ནི་ལྷ་དང་ལྷ་ལས་གཞན་པའི་འཇིག་རྟེན་གྱིས་ཀྱང་རུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2802 [HEADING]]
#### དྲན་པ་མི་ཚུགས་པ། ^8-5-3-0

[Block 2803]
དྲན་པ་མི་ཚུགས་པ་ནི་གང་དྲན་པའི་སྟོབས་ལ༌[^2440]རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་དྲན་པའི་སྟོབས་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2804]
དེ་ཞེས་བྱ་བ་ནི་དྲན་པའི་སྟོབས་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེའོ། །

[Block 2805]
ཆོས་ནི་ཕུང་པོ་དང་ཁམས་ལ་སོགས་པ་གང་ཡང་རུང་པའོ། །
--- END BLOCKS ---
