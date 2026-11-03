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
[Block 2556]
ཡང་ན་བདག་མེད་པར་ཁོང་དུ་ཆུད་པར་བྱས་ནས༌[^2190]ཉོན་མོངས་པ་ཐམས་ཅད་སྤངས་པའི་ཡེ་ཤེས་ཀྱང་བསྐྱེད༌[^2191]ལ། ཁམས་གསུམ་དུ་སྐྱེ་བར་བྱེད་པའི་རྒྱུ་དགེ་བ་མངོན་པར་འདུ་བྱེད་པ་ཡང་གཏོང་བར་མི་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2557]
མི་སྐྱེ་བ་ཤེས་པ་ཡང་མངོན་པར་བསྒྲུབས༌[^2192]ཏེ། དེ་སེམས་ཅན་ལ་ལྟ་བ་ཡང་སྐྱེད་ཅིང་མི་སྐྱེ་བའི་མཐའ་ཡང་མི་སྤོང་ངོ་ཞེས་བྱ་བ་ནི་ཐོག་མ་ནས་མ་སྐྱེས་པར་ཤེས་པའི་ཡེ་ཤེས་ཐོབ་ཀྱང་ཀུན་རྫོབ་ཏུ་སེམས་ཅན་གྱི་དོན་ལ་ལྟ་བའང་སྐྱེད༌[^2193]དེ། དེ་སྐྱེད་ཀྱང་སྐྱེ་བ་འབའ་ཞིག་ལ་མི་ཕྱོགས་ཀྱི་མི་སྐྱེ་བའི་ཆོས་ཉིད་ཀྱང་མི་གཏོང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2558]
ཆོས་དྲན་པ་ཉེ་བར་གཞག་པའི༌[^2194]དོན་བསྡུ་ཞིང་། ཇི་ལྟར་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ༌[^2195]ཡིན་པར་མདོར་བསྟན་པའི་ཕྱིར། ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཆོས་འོག་ནས་མིང་གིས་སྨོས་པ༌[^2196]ཐམས་ཅད་སྟོང་པ་ཉིད་དུ་རྟོགས་པའི་དྲན་པ་དེ་ལ་གནས་པས་ན་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ༌[^2197]ཞེས་བྱའོ། །

[Block 2559]
དྲན་པའི་དོན་བསྟན་པའི་ཕྱིར། ཕྱི་མའི་མཐའི་བར་དུ་ཡང་དྲན་པ་དེས་མི་བརྗེད་ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སེམས་ཅན་གྱི་མཐའ་དང་། འཁོར་བའི་མཐའ༌[^2198]ཇི་སྲིད་ཡོད་ཀྱི་བར་དུ་རྟོགས་པའི༌[^2199]དྲན་པ་དེ་ཉམས་པར་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2560]
དེ་བས་ན་ཆོས་ཐམས་ཅད་མ་ལུས་པར་ཞེས་ཚིག་ཕྱི་མ་དང་སྦྱར་རོ། །

[Block 2561]
དྲན་པ་ཉེ་བར་གཞག་པ༌[^2200]ཞེས་བྱ་བ་དེ་ནི་ཚད་མེད་པ༌[^2201]ཤིན་ཏུ་བསྟན་པའི་ཚིག་སྟེ་ཞེས་བྱ་བ་ལ། ཆོས་དྲན་པ་ཉེ་བར་གཞག་ཅེས་བྱ་བའི་ཚིག་དེ་ནི་ཚད་མེད་པ་ཤིན་ཏུ་བསྟན་པའི༌[^2202]ཚིག་སྟེ། ཇི་ལྟར་ཚད་མེད་པ་ཤིན་ཏུ་བསྟན་པའི༌[^2203]ཚིག་ཡིན་པ་ནི་ཆོས་ཐམས་ཅད་ལ་དམིགས་སོ་ཞེས་སྔར་ཡང་བཤད་ལ། ཀུན་དུ་སྤྱོད་ཡུལ་ཞེས་བྱ་བ་ལ་སོགས་པ་འོག་ནས་འབྱུང་བའི་ཚིག་གིས་ཀྱང་བསྟན་ཏོ། །

[Block 2562]
དེ་ལྟ་མོད་ཀྱི་མདོར་ན་དྲན་པར་བྱ་བའི་ཆོས་རྣམས་ཚད་མེད་དེ་མི་ཟད་པའི་ཕྱིར་རམ། ཕྱི་མའི་མཐའི་བར་དུ་ཡང་དྲན་པ་དེ་མི་བརྗེད༌[^2204]ཅིང་ཉམས་པར་མི་འགྱུར་བའི་ཕྱིར་ཚད་མེད་པའི་དོན་ཏོ། །

[Block 2563]
ཀུན་དུ་སྤྱོད་ཡུལ་ཞེས་བྱ་བ་ནི་ཤེས་བྱ་ཐམས་ཅད་ཀྱང༌[^2205]དྲན་པ་དེའི་སྤྱོད་ཡུལ་དུ་གྱུར་པ་སྟེ། ཐམས་ཅད་དུ་ཁྱབ་པར་དམིགས་ཞེས་བྱ་བའི་དོན་ཏེ།[^2206] ཐམས་ཅད་ཡང་དག་པར་འདུ་བ་ནི་དྲན་པ་དེར་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པའི་སངས་རྒྱས་ཀྱི༌[^2207]ཆོས་ཐམས་ཅད་ཡང་དག་པར་འདུ་བའི་ཕྱིར་རོ། །

[Block 2564]
ཚིམ་པར་བྱེད་པ་ནི་སེམས་ཅན་ལ་ཕན་འདོགས་ཤིང་སེམས་ཅན་དང་བསྐྱེད་པར་བྱེད་པའོ། །

[Block 2565]
ཕམ་པར་བྱེད་པ་ནི་བདུད་ཐམས་ཅད་འཇོམས་པར་བྱེད་པའོ། །

[Block 2566]
རྟོགས་པར་བྱེད་པ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་རང་གིས་རིག་པར་བྱེད་པའོ། །

[Block 2567]
དེ་ལྟར་ཀུན་བྱེད་པའི་ཚིག་དེ་ནི་ཆོས་ལ་ཆོས་ཀྱི་རྗེས་སུ་ལྟ་བའི་དྲན་པ་ཉེ་བར་གཞག་པ་ཞེས་བྱའོ། །

[Block 2568]
འདི་ནི་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་མི་ཟད་པ་བསྒོམ་པ༌[^2208]སྟེ། དྲན་པ་ཉེ་བར་གཞག་པ༌[^2209]བཞི་བསྒོམ་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2569 [HEADING]]
### ཡང་དག་པའི་སྤོང་བ་བཞི་མི་ཟད་པ། ^8-2-0

[Block 2570]
བརྩོན་འགྲུས་ཤིན་ཏུ་གཉེན་པོར་གྱུར་པ་དང་། བརྩོན་འགྲུས་ཤིན་ཏུ་སྦྱངས་པ་དང་། བརྩོན་འགྲུས་ཐོབ་པ་དང་། བརྩོན་འགྲུས་ཤིན་ཏུ་བརྟན་པ༌[^2210]བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^2211]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཡང་དག་པའི་སྤོང་བ་བཞི་ཡང་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2571]
འདིར་ཡང་བསྟན་པ་དང་བཤད་པའི་ཚུལ་དུ་རིག་པར་བྱ་སྟེ། བཞི་གང་ཞེ་ན་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། སེམས་རབ་ཏུ་འཛིན་ཞིང་ཡང་དག་པར་རབ་ཏུ་འཇོག་པ་ཞེས་བྱ་བ་ཡན་ཆད་ནི་བསྟན་པའི་ཚུལ་ལོ། །

[Block 2572]
དེ་མན་ཆད་ལྷག་མ་རྣམས་ནི་བཤད་པའི་ཚུལ་ལོ། །

[Block 2573]
བཞི་པོ་དེ་དག་མི་ཟད་པ་ཡང་སྤང་བར༌[^2212]བྱ་བ་དང་བསྒྲུབ་པར༌[^2213]བྱ་བའི་ཆོས་རྣམས་མི་ཟད་པའི་ཕྱིར་རོ། །

[Block 2574]
རྒལ་བ༌[^2214]སྡིག་པ་མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ༌[^2215]མི་སྐྱེད་པ་དང་། སྐྱེས་པ་སྤོང་བ་ལ་ནི་ཡང་དག་པའི་སྤོང་བ་ཞེས་བྱ་བར་འོས་ན། དགེ་བའི་ཆོས་མ་སྐྱེས་པ་བསྐྱེད་པ་དང་། སྐྱེས་པ་གནས་པར་བྱ་བ་ལ་ཡང་དག་པའི༌[^2216]སྤོང་བ་ཞེས་ཇི་ལྟར་གདགས་ཤེ་ན། [^2217]དེ་གཉིས་ལ་གདགས་པར་མི་རིགས་པ་འདྲ་མོད་ཀྱི། དགེ་བ༌[^2218]བསྐྱེད་པ་དང་གནས་པར་བྱ་བའི་མི་མཐུན་པའི་ཕྱོགས་སྤངས་པ་དང་། བསྐྱེད་ཅིང་གནས་པར་འགྱུར་བའི་ཕྱིར། མི་མཐུན་པའི་ཕྱོགས་སྤོང་བ་ལ་ཡང་དག་པའི་སྤོང་བ་ཞེས་བྱ་བས་ཉེས་པ་མེད་དོ། །

[Block 2575 [HEADING]]
#### བརྩོན་འགྲུས་ཤིན་ཏུ་གཉེན་པོར་གྱུར་པ། ^8-2-1-0

[Block 2576]
བརྩོན་འགྲུས་ཤིན་ཏུ་གཉེན་པོར་གྱུར་པའི་བྱང་ཆུབ་སེམས་དཔའ་གང་ཞེ་ན། གང་ཡང་དག་པའི༌[^2219]སྤོང་བ་དང་པོ་ལ་ཞུགས་པ་སྟེ། མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་ཀྱི༌[^2220]གཉེན་པོ་བསྒོམ་པར་བྱ་བ་ལ་སྒོམ་པར་བྱེད་པའོ། །

[Block 2577]
དེའི་དབང་དུ་བྱས་ནས། གང་སྡིག་པ་མི་དགེ་བའི་ཆོས་གང་མ་སྐྱེས་པ་རྣམས་མི་སྐྱེད་པའི་ཕྱིར་འདུན་པ་བསྐྱེད༌[^2221]ཅེས་བྱ་བ་ནི༌[^2222]ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པའི་ཚིག་བླ་དགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ།[^2223] །སྡིག་པ་མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་མི་སྐྱེད་པའི་ཕྱིར་འདུན་པ་བསྐྱེད༌[^2224]ཅེས་ཀྱང་བྱ། ཚུལ་བཞིན་དུ༌[^2225]ཡིད་ལ་བྱེད་ཅེས༌[^2226]ཀྱང་བྱ་སྟེ། འདུན་པ་བསྐྱེད༌[^2227]ཅེས་བྱ་བ་ནི། ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པའི་ཚིག་བླ་དགས་སོ། །

[Block 2578]
དེ་ལ་སྡིག་པ་མི་དགེ་བའི་ཆོས་ནི་གང་འདོད་པ་ན༌[^2228]སྤྱོད་པའི་ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་ཉེས་པར༌[^2229]སྤྱོད་པས་ཡོངས་སུ་བསྡུས་པ་དང་། དེ་སྐྱེད་པར་བྱེད་པའི་ཉོན་མོངས་པ་རྣམས་སོ། །

[Block 2579]
མ་སྐྱེས་པ་ན༌[^2230]ཆོས་དེ་མངོན་དུ་མ་གྱུར་ཅིང་ཉེ་བར་མ༌[^2231]གྱུར་པའོ། །

[Block 2580]
མི་སྐྱེད་པ་ནི་མངོན་དུ་མི་འབྱུང་བ་དང་། ཉེ་བར་མི་འགྱུར་བར་བྱའོ། །

[Block 2581]
འདུན་པ་བསྐྱེད་པ་ནི་དེའི་གཉེན་པོར་གྱུར་པ་ཞི་གནས་ལ་སོགས་པའི་མཚན་མ་ཡིད་ལ་བྱེད་པ་ལ་མི་བརྟེན་པར་མི་གཙང་བ་ལ་སོགས་པའི་གཉེན་པོ་ཉི་ཚེ་སྒོམ་པར༌[^2232]བྱེད་པ་སྟེ། དེ་བས་ན་འདུན་པ་བསྐྱེད་པ༌[^2233]ནི་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པའི་ཚིག་བླ་དགས་སོ། །

[Block 2582]
འབད་པས༌[^2234]བརྩོན་འགྲུས་རྩོམ་ཞེས་བྱ་བ་དེ་ནི་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་མི་འདོར་བའི་ཚིག་བླ་དགས་སོ་ཞེས་བྱ་བ་ལ། འདིར་ཡང་སྡིག་པ་མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འབད་པས༌[^2235]བརྩོན་འགྲུས་རྩོམ་ཞེས་ཀྱང་བྱ། ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་མི་འདོར་མི་གཏོང་ཞེས་ཀྱང་བྱ་སྟེ། དེ་བས་ན་འབད་པས་བརྩོན་འགྲུས་རྩོམ་ཞེས་བྱ་བ་ནི་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་མི་འདོར་བའི་ཚིག་བླ་དགས་སོ། །

[Block 2583]
དེ་ལ་སྡིག་པ་མི་དགེ་བའི་ཆོས་དེ་དག་ཀྱང་འདས་པའི་དངོས་པོ་ལ་དམིགས་པ་དང་། མ་འོངས་པའི་དངོས་པོ་ལ་དམིགས་པ་དང་། ད་ལྟར་གྱི་ཡུལ་ལ་དམིགས་ནས་སྐྱེའོ། །

[Block 2584]
དེ་ལྟར་ན་དེ་དག་ནི་ལྐོག་ཏུ་གྱུར་པའི་ཡུལ་ལ༌[^2236]དམིགས་པ་དང་། མངོན་སུམ་དུ་གྱུར་པའི་ཡུལ་ལ༌[^2237]དམིགས་པ་སྟེ། གང་འདས་པ་དང་མ་འོངས་པའི་དངོས་པོ་ལ་དམིགས་པ་ནི་ལྐོག་ཏུ་གྱུར་པའི་ཡུལ་ལ་དམིགས་པའོ། །

[Block 2585]
ད་ལྟར་གྱི་ཡུལ་ལ་དམིགས་པ་ནི་མངོན་སུམ་གྱི༌[^2238]ཡུལ་ལ་དམིགས་པའོ། །

[Block 2586]
དེ་ལ་ལྐོག་ཏུ་གྱུར་པའི་ཡུལ་ལ་དམིགས་པའི་སྡིག་པ་མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་མི་སྐྱེད་པ༌[^2239]ནི་འབད་དོ། །

[Block 2587]
མངོན་སུམ་དུ་གྱུར་པའི་ཡུལ་ལ་དམིགས་པའི་སྡིག་པ་མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་མི་སྐྱེད་པའི་ཕྱིར་ནི་བརྩོན་འགྲུས་རྩོམ་མོ། །

[Block 2588]
སེམས་རབ་ཏུ་འཛིན་ཞིང་ཡང་དག་པར་རབ་ཏུ་འཇོག་ཅེས་བྱ་བ་དེ་ནི་ཚུལ་བཞིན་དུ་རྟོགས་པའི༌[^2240]ཚིག་བླ་དགས་སོ་ཞེས་བྱ་བ་ལ། འདིར་ཡང་སྡིག་པ་མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་ཞེས་བྱ་བར་སྦྱར་ཏེ། སེམས་རབ་ཏུ་འཛིན་ཞིང་ཡང་དག་པར་རབ་ཏུ་འཇོག་ཅེས་ཀྱང་བྱ། ཚུལ་བཞིན་དུ་རྟོགས་པ༌[^2241]ཞེས་ཀྱང་བྱ་སྟེ། སེམས་རབ་ཏུ་འཛིན་ཞིང་ཡང་དག་པར་རབ་ཏུ་འཇོག་པ་ནི་ཚུལ་བཞིན་དུ་རྟོགས་པའི༌[^2242]ཚིག་བླ་དགས་སོ། །

[Block 2589]
དེ་ལ་སེམས་རབ་ཏུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་གང་གི༌[^2243]ཚེ་ཞུམ་པའི་ཉེ་བའི་ཉོན་མོངས་པ་སྐྱེས་པར་གྱུར་པ་དེའི་ཚེ། དེ་བསལ་བར་བྱ་བའི་ཕྱིར་རབ་ཏུ་དང་བར་འགྱུར་བ་ལ་སོགས་པའི་ཡིད་ལ་བྱེད་པ་སེམས་གཟུང་བ༌[^2244]སྟེ། གཟུང་ཞེས་བྱ་བ་ནི་དེའི་གཉེན་པོ་འཕགས་པའི་ལམ་དང་། དེ་བཞིན་གཤེགས་པའི་ཡོན་ཏན་རྣམས་བསམས༌[^2245]ནས་སེམས་གཟེངས་བསྟོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2590]
ཡང་དག་པར་འཇོག་རབ་ཏུ་འཇོག་ཅེས་བྱ་བ་ནི་རྒོད་པའི་ཉེ་བའི་ཉོན་མོངས་པ་སྐྱེས་པ་ན་སེམས་ནང་དུ་བསྡུ་བའི་ཚུལ་གྱིས་རྩེ་གཅིག་ཏུ་གཞག་པ་སྟེ། དམིགས་པ་དེ་ཉིད་ལ་ཡང་དང༌[^2246]ཡང་དུ་གཞག་ཅིང་འཁོར་བའི་ཉེས་པ་ལ་སོགས་པ་ཡིད་ལ་བྱེད་པས་སྐྱོ་བ་བསྐྱེད༌[^2247]པའོ། །

[Block 2591]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་འདྲི་བ༌[^2248]སྟེ། འདུན་པ་སྐྱེད་པ་དང་། འབད་དེ་བརྩོན་འགྲུས་རྩོམ་པ་དང་། སེམས་རབ་ཏུ་འཛིན་ཞིང་ཡང་དག་པར་རབ་ཏུ་འཇོག་པ་དེ་དག་ལ་ཅིའི་ཕྱིར་ཚུལ་བཞིན་ཞེས་བྱ་ཞེ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2592]
ལན་དུ་ཚུལ་བཞིན་རབ་ཏུ་སྦྱོར་བ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་ཀྱི་གཉེན་པོ་དང་། ཞུམ་པ་དང་རྒོད་པའི་གཉེན་པོ་བསྒོམ་པ་རྣམས་ནི་དེ་དང་མི༌[^2249]མཐུན་པ་སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་ལ་མི་འཇུག་སྟེ། དེ་བས་ན་དེ་དག་ནི་ཚུལ་བཞིན་གྱི་ཚིག་བླ་དགས་སོ། །

[Block 2593]
དེ་ལ་སྡིག་པ་མི་དགེ་བའི་ཆོས་གང་ཞེ་ན། གང་བསླབ་པ་གསུམ་མཐར་དབྱུང་བར་བྱ་བ་དང་མི་མཐུན་པའི་ཆོས་རྣམས་སོ། །

[Block 2594]
དེ་དག་དངོས་པོ་གང་ཡིན་པ་བསྟན་པའི་ཕྱིར། ཚུལ་ཁྲིམས་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2595]
ཚུལ་ཁྲིམས་ཉམས་པ་དང་ཞེས་བྱ་བ་ནི་གང་ཡན་ལག་དྲུག་པའི་ཚུལ་ཁྲིམས་ཉམས་པ་ཉིད་སྡིག་པ་མི་དགེ་བའི་ཆོས་སོ། །
--- END BLOCKS ---
