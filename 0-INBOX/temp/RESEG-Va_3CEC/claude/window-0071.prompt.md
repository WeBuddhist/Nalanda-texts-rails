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

[Block 2491]
སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ནི་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པའོ། །

[Block 2492]
དེ་དག་ནི༌[^2146]ཡུལ་ནི་སྟོང་པ་ཉིད་དོ། །

[Block 2493]
རྒྱུ་ནི་ཡུལ་ཏེ་མངོན་དུ་བྱེད་པའི་ཆོས་དེ་ཐབས་དང་ཤེས་རབ་བོ། །

[Block 2494]
སྒྲུབ་པ༌[^2147]ནི་ཐབས་དང་ཤེས་རབ་སྒྲུབ་པའོ། །

[Block 2495]
མངོན་པར་ཤེས་པ་ནི་དྲུག་རྣམས་སོ། །

[Block 2496]
སེམས་ཉེ་བར་འདོགས་པ་ནི་རྩེ་གཅིག་ཏུ་འཇོག་པའོ། །

[Block 2497]
སེམས་མི་སྤྱོད་པར་རབ་ཏུ་ཤེས་པའོ། །

[Block 2498]
སེམས་ཅན་རྣམས་ཀྱི་སེམས་ཇི་ལྟ་བུ་ཡིན་པ་དང་། འདོད་ཆགས་ལ་སོགས་པའི་ཉོན་མོངས་པ་གང་ལ་སྤྱོད་པ་ཤེས་པའོ། །

[Block 2499]
དེ་ལྟ་བུའི་རང་བཞིན་གྱིས༌[^2148]ཆོས་སྟོན་པ་ནི་ཉོན་མོངས་པ་གང་ལ་སྤྱོད་པ་དང་དེ་དང་མཐུན་པའི་ཆོས་མི་གཙང་བ་ལ་སོགས་པ་སྟོན་པའོ། །

[Block 2500]
མི་སྐྱོ་བ་ནི་སྙིང་རྗེ་དང་ལྡན་པས་སོ། །

[Block 2501]
སེམས་ཟད་པར་བྱ་བའི་ཕྱིར་སེམས་མི་བསྐྱེད༌[^2149]ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ལྟར་ཞི་བ་ཕྱོགས་གཅིག༌[^2150]པའི་མྱ་ངན་ལས་འདས་པ་ལ་གནས་པ་ནི་མ་ཡིན་གྱི། ཐབས་ཀྱིས༌[^2151]ཡོངས་སུ་ཟིན་པས་འཁོར་བའི་རྒྱུན་ནི་དགེ་བའི་རྩ་བ་མི་གཅོད་དོ༌[^2152]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2502]
ཟད་པ་ནི་ཉོན་མོངས་པ༌[^2153]ཟད་པའི་ཕྱིར་རོ། །

[Block 2503]
འགོག་པ་ནི་ཕུང་པོ་སྤངས་པའི༌[^2154]ཕྱིར་རོ། །

[Block 2504]
སེམས་ཀྱིས༌[^2155]དྲན་པ་ཤེས་པ་དེས་ཞེས་བྱ་བ་ལ་སོགས་པས་གོང་དུ་སྨོས་པ་ལྟ་བུའི་སེམས་དྲན་པ་ཉེ་བར་འཇོག་པ་དེ་ཁོང་དུ་ཆུད་དེ། དེས་མ་བྱུང་བ་དང་མི་སྐྱེ་བ་ལ་སོགས་པའི་མཚན་ཉིད་ལ་གནས་ཀྱང་ཆོས་ཉིད་དེའི་དབང་དུ་མ་གྱུར་པས་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་དག་ལྟར་འཁོར་བ་ཡོངས་སུ་སྤོང་བར་ཡང་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2505]
ནམ་སངས་རྒྱས་ཀྱི་ཆོས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བདག་དང་། སེམས་ཅན་ཐམས་ཅད་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་མ་གྲུབ་ཀྱི་བར་དུ། ཐབས་དང་ཤེས་རབ་ཟུང་དུ་འབྲེལ་པའི་སེམས་ཀྱི་རྒྱུན་མི་གཏོང་བའོ། །

[Block 2506]
སེམས་ཀྱི་སྐད་ཅིག་གཅིག་དང་ལྡན་པའི་ཤེས་རབ་ཅེས་བྱ་བ་ནི་མཐར་མངོན་པར་བྱང་ཆུབ་པ་ལ་འཇུག་པའི་སེམས་ཀྱི་སྐད་ཅིག་མ་གཅིག་དང་ལྡན་པ། བདག་མེད་པ་གཉིས་ཁོང་དུ་ཆུད་པའི་ཤེས་རབ་ཀྱིས་དེ་བཞིན་ཉིད་མངོན་སུམ་དུ་བྱེད་པའོ། །

[Block 2507]
སེམས་དྲན་པ་ཉེ་བར་གཞག་པ་བསྒོམ་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2508 [HEADING]]
#### ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ། ^8-1-4-0

[Block 2509]
རབ་ཏུ་རྣམ་པར་བྱང་བའི་བྱང་ཆུབ་སེམས་དཔའ་གང་ཞེ་ན། གང་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ།[^2156] སྒྲིབ་པ་དང་། ཀུན་ནས་སྦྱོར་བ་དང་། འཆིང་བ་དང་། བག་ལ་ཉལ་བ་དང་། ཉོན་མོངས་བའི་ཀུན་ནས་དཀྲིས་པ་ཐམས་ཅད་ལས་འདས་པ་ཡང་ཐོབ་ལ། ཆོས་ཐམས་ཅད་ལ་དབང་ཐོབ་པ༌[^2157]ཡོངས་སུ་རྫོགས་པར་བྱེད་པའོ། །

[Block 2510]
དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཆོས་རྣམས་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཆོས་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་དང་། ཟག་པ་དང་བཅས་པ་དང་། ཟག་པ་མེད་པའོ། །

[Block 2511]
ཆོས་ཀྱི་རྗེས་སུ་ལྟ་བ་ནི་ཤེས་རབ་ཀྱིས༌[^2158]ཆོས་དེ་དག་ལ་སྟོང་པར་རྟོག་པའོ། །

[Block 2512]
དྲན་པ་ཉེ་བར་གཞག་པ༌[^2159]ནི་ཏིང་ངེ་འཛིན་གྱིས༌[^2160]དེ་ལ་རྩེ་གཅིག་ཏུ་འཇོག་པའོ། །

[Block 2513]
གང་ཞེ་ན་ཞེས་བྱ་བ་ནི་དེ་དག་དངོས་པོ་གང་ཡིན་པ་འདྲི་བའོ། །

[Block 2514]
དེ་དག་བསྟེན་པའི༌[^2161]ཕྱིར། འཕགས་པའི་ཤེས་རབ་ཀྱི་མིག་གིས་མཐོང་བའི་ཆོས་དེ་དག༌[^2162]ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། འཕགས་པ་ཞེས་སྨོས་པ་ནི་ཟག་པ་མེད་པར་སྟོན་ཏོ། །ཤེས་རབ་ཀྱི་མིག་ཅེས་སྨོས་པ༌[^2163]ནི་རྣམ་པར་མི་རྟོག་པའི་མཚན་ཉིད་ཡིན་པར་སྟོན་ཏོ། །

[Block 2515]
མཐོང་བ་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་ཐམས་ཅད་འོག་ནས་འབྱུང་བའི་ཚུལ་དུ་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་མཐོང་བ་སྟེ། དེ་ལྟར་མཐོང་བའི་ཆོས་དེ་དག་ནི་འབྲས་བུ་ལ་གནས་ཀྱི་བར་དུ་ཉམས་པར་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2516]
སྟོང་པ་རྣམ་པར་གྲོལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཆུང་རབ་ཙམ་ཡང་མི་མཐོང་ཞེས་བྱ་བར་སྦྱར་ཏེ། སྟོང་པ་ཉིད་ལ་སོགས་པའི་ནང་དུ་མ་འདུས་པའི་ཆོས་གང་ཡང་མེད་དོ། །

[Block 2517]
དེར་མ་འདུས་པའི་ཆོས་གང་ཡང་མི་མཐོང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2518]
ཆོས་གང་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ལས་རྣམ་པར་གྲོལ་བ་ཆུང་རབ་ཙམ་ཡང་མི༌[^2164]མཐོང་ངོ་ཞེས་བྱ་བ་ནི་དོན་དམ་པར་ཆོས༌[^2165]རྣམས་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་ཡིན་ཡང་། ཀུན་རྫོབ་ཏུ་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མ་ཡིན་པའི་ཆོས་གཅིག་ཀྱང་མི་མཐོང་སྟེ། དེར་མ་གཏོགས་པའི་ཆོས་གཅིག་ཀྱང་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2519]
ཆོས་ཁོ་ན་མཐོང་གི༌[^2166]ཆོས་མ་ཡིན་པ་མི་མཐོང་ངོ་ཞེས་བྱ་བ་ལ། བདག་མེད་པ་ལ་སོགས་པ༌[^2167]ཕྱིན་ཅི་མ་ལོག་པ་ཡང་དག་པ་ཡིན་པས་ན་ཆོས་ཁོ་ན་ཞེས་བྱ་སྟེ། དེ་མཐོང་བའོ། །

[Block 2520]
བདག་ཏུ་ལྟ་བ་ལ་སོགས་པ་སྨོས་པ་ནི་ཡང་དག་པ་མ་ཡིན་པ་ཕྱིན་ཅི་ལོག་པས་ཆོས་མ་ཡིན་པ་སྟེ་དེ་མི་མཐོང་བའོ། །

[Block 2521]
ཆོས་ཐམས་ཅད་ནི་ཆོས་སོ་ཞེས་བྱ་བ་ལ་ཆོས་ཀྱི་སྒྲ་ནི་སྟོང་པ་ཉིད་ལ་སོགས་པ་ལ་བྱ་སྟེ། དེ་ཆོས་ཐམས་ཅད་ལ་ཡོད་པས་ན་ཆོས་ཐམས་ཅད་ནི་ཆོས་སོ། །

[Block 2522]
ཆོས་ཐམས་ཅད་ནི་ཆོས་མ་ཡིན་ཞེས་བྱ་བ་ནི་ཆོས་དེ་དག་ཉིད་ལ་བདག་དང་བདག་གིར་འཛིན་པ་ཡང་སྐྱེ་བས་ན་ཆོས་ཐམས་ཅད་ཆོས་མ་ཡིན་པས་ཏེ༌[^2168]བདག་ཏུ་འཛིན་པ་ལ་སོགས་པ་ལ་ཆོས་མ་ཡིན་པ་ཞེས་བྱའོ། །

[Block 2523]
སོ་སོར་རྟོག་པས་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཤེས་པས་སམ། སྟོང་པས་ཁྱབ་པས་སོ།[^2169] །མངོན་པར་ཞེ་ན་པ༌[^2170]ཞེས་བྱ་བ་ནི་ཆོས་དེ་དག་ཉིད་བདག་དང་བདག་གིར་ཆགས་པའི་རྒྱུ་ཡིན་པས་སོ། །

[Block 2524]
སངས་རྒྱས་ཀྱི་ཆོས་མེད་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཆོས་རྣམས་སྟོང་པར་ཁོང་དུ་ཆུད་པ་ལས་ཐར་བ་དང་མྱ་ངན་ལས་འདས་པར་འགྱུར་ཏེ། དེ་བས་ན་ཆོས་གང་ལ༌[^2171]བརྟེན་ཏེ་སངས་རྒྱས་ཀྱི་ཆོས་སུ་མི་འགྱུར་བའི་ཆོས་དེ་དག་ཡང་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2525]
སངས་རྒྱས་ཀྱི་ཆོས་ནི་ལུང༌[^2172]དང་ཁོང་དུ་ཆུད་པར་བྱ་བའི་ཆོས་ཏེ། དེའི་རང་བཞིན་དུ་མ་གྱུར་པའི་ཆོས་གང་ཡང་མེད་དོ་ཞེས་བྱ་བར་དགོངས་སོ། །
--- END BLOCKS ---
