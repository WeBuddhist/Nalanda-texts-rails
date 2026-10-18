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
[Block 2381]
ཉེ་བར་ལེན་པ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་ཡོད་པར་རྟོག་པའོ། །

[Block 2382]
དམིགས་པ་ནི་ཕྱིའི་ཡུལ་གཟུགས་ལ་སོགས་པ་ཡོད་པར་དམིགས་པའོ། །

[Block 2383]
ཕྱིན་ཅི་ལོག་ནི་བདག་མེད་པ་ལ་བདག་ཏུ་རྟོག་པ་ལ་སོགས་པ༌[^2077]ཕྱིན་ཅི་ལོག་བཞིའོ། །

[Block 2384]
རྣམ་པར་རྟོག་པ་ནི་བདག་དང་བདག་གི་ཡོད་པར་རྟོག་པའོ། །

[Block 2385]
ལྟ་བ་ནི་བདག་ཏུ་ལྟ་བ་དང་སེམས་ཅན་ལ་སོགས་པ་སྟེ། དེ་དག་གི༌[^2078]བག་ལ་ཉལ་ལམ། ཉོན་མོངས་པ་གཞན་གྱི་བག་ལ་ཉལ་ལོ། །

[Block 2386]
མིག་ཏུ་འདུ་ཤེས་པ་ལ་སོགས་པ་ནི་དབང་པོ་རྣམས་ཡོད་པར་འདུ་ཤེས་པ་སྟེ། དེ་དག་ཀྱང་ཚོར་བ་སྐྱེ་བའི་རྒྱུར་འགྱུར་བས་མིག་ཏུ་འདུ་ཤེས་པའི་ཚོར་བའོ། །

[Block 2387]
ཡང་ན་ཡོངས་སུ་འཛིན་པ་ནི་ཚོར་བའོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་མེད་པ་ལ་དངོས་པོར་འཛིན་པ་ཉིད་ཚོར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2388]
ཉེ་བར་ལེན་པའི་ཚོར་བ་ཞེས་བྱ་བ་ལ། སྡུག་བསྔལ་གྱི་ཕུང་པོ་ལྔ་ལེན་པ་ཉིད་ཚོར་བའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2389]
དམིགས་པ་ནི་ཚོར་བའོ་ཞེས་བྱ་བ་ལ་གཟུགས་ལ་སོགས་པ་ལ་དམིགས་པ་ཉིད་ཚོར་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2390]
ཚོར་བའི་རྣམ་གྲངས་གཞན་ཡང་བསྟན་པའི་ཕྱིར། གཞན་ཡང་རྣམ་གྲངས་སུ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སྟེ།[^2079] འོག་ནས་སྨོས་པའི་རྣམ་གྲངས་རྣམས་ཀྱང་མིང་དུ་ཐ་དད་ཀྱི། དོན་དུ་གཅིག་གོ་ཞེས་བྱ་བར་དགོངས་པའོ། །

[Block 2391]
ཚོར་བ་གཅིག༌[^2080]པུ་ཞེས་བྱ་བ་ནི་གཅིག་ཏུ་ཟད་དེ༌[^2081]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2392]
གང་འདི་སེམས་ཀྱི་རྣམ་པར་རིག་པ་ཞེས་བྱ་བ་ལ། གང་གི༌[^2082]མཚན་ཉིད་རྣམ་པར་རིག་པའི་ངོ་བོ་ཉིད་ཚོར་བ་ཡིན་པ་འམ། སེམས་ཀྱི་རྣམ་པར་རིག་པ་ལས་བྱུང་བའི་ཚོར་བའོ། །

[Block 2393]
ནང་གི་ཉེ་བར་ལེན་པ་ལས་བྱུང་བའི་ཚོར་བ་ནི་ནང་གི་ཚོར་བའོ། །

[Block 2394]
ཕྱིའི་གཟུགས་ལ་སོགས་པ་ལ་དམིགས་པའི་རྒྱུ་ལས་བྱུང་བའི་ཚོར་བ་ནི་ཕྱིའི་ཚོར་བའོ། །

[Block 2395]
ཚོར་བ་གསུམ་སྟེ་ཞེས་བྱ་བ་ནི་དུས་གསུམ་གྱི་དངོས་པོ་རྣམ་པར་རིག་པ་ཉིད་ཚོར་བ་འམ། [^2083]དངོས་པོ་རྣམ༌[^2084]པར་རིག་པའི་རྒྱུ་ལས་བྱུང་བའི་ཚོར་བའོ། །

[Block 2396]
ཁམས་བཞི་ནི་ས་ཆུ་མེ་རླུང་བཞི་སྟེ། དེ་དག་རིག་པ༌[^2085]ཉིད་ཚོར་བའམ། དེ་དག་རིག་པའི་རྒྱུ་ལས་བྱུང་བའི་ཚོར་བ་སྟེ། ཡུལ་བཞི་ཡོད་པས་དེ་ལ་དམིགས་པར་བྱེད་པའི་ཚོར་བ་ཡང་རྣམ་པ་བཞིར་གཞག་གོ། །

[Block 2397]
ཕུང་པོ་ལྔ་ཡིད་ལ་བྱེད་ཅེས་བྱ་བ་ནི་ཕུང་པོ་ལྔ་ཡིད་ལ་བྱེད་པ་ཉིད་ཚོར་བ་འམ། དེ་ཡིད་ལ་བྱེད་པའི་རྒྱུ་ལས་བྱུང་བའི་ཚོར་བའོ། །

[Block 2398]
སྐྱེ་མཆེད་དྲུག་ལ་ཡོངས་སུ་རྟོག་པའོ་ཞེས་བྱ་བ་ནི་སྐྱེ་མཆེད་དྲུག་ལ་ཡོངས་སུ་རྟོག་པ་ཉིད་ཚོར་བའམ། ཡོངས་སུ་རྟོག་པའི་རྒྱུ་ལས་བྱུང་བའི་ཚོར་བའོ། །

[Block 2399]
ཚོར་བ་ནི་བདུན་སྟེ།[^2086] གང་འདི་རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་ནོ་ཞེས་བྱ་བ་ལ། རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་ནི་ལུས་སྣ་ཚོགས་པ༌[^2087]དང་། འདུ་ཤེས་སྣ་ཚོགས་པའི་རྣམ་པར་ཤེས་པ་གནས་པ་དང་། ལུས་སྣ་ཚོགས་ལ་འདུ་ཤེས་གཅིག་པའི་རྣམ་པར་ཤེས་པ་གནས་པ་དང་། ལུས་གཅིག་ལ་འདུ་ཤེས་སྣ་ཚོགས་པའི་རྣམ་པར་ཤེས་པ་གནས་པ་དང་། ལུས་གཅིག་ལ་འདུ་ཤེས་ཀྱང་གཅིག་པའི་རྣམ་པར་ཤེས་པ་གནས་པ་དང་། གཟུགས་མེད་པའི་ས་གསུམ་རྣམས་དང་བདུན་ནོ། །

[Block 2400]
དེ་ལ་ལུས་སྣ་ཚོགས་ལ་འདུ་ཤེས་སྣ་ཚོགས་པའི་སེམས་ཅན་རྣམས་ནི་མི་རྣམས་དང་། འདོད་པ་ན་སྤྱོད་པའི༌[^2088]ལྷའི་རིས༌[^2089]དྲུག་དང་། བསམ་གཏན་དང་པོར་སྐྱེས་པ་ཐོག་མ་བྱུང་བ་མ་གཏོགས་པ་རྣམས་ཏེ། སེམས་ཅན་དག་ལུས་ཀྱང་ཆེ་ཕྲ༌[^2090]བཟང་ངན་རྣམ་པ་སྣ་ཚོགས་ཡོད་ལ་འདུ་ཤེས་ཀྱང་རྣམ་པ་སྣ་ཚོགས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2401]
ལུས་སྣ་ཚོགས་ལ་འདུ་ཤེས་གཅིག་པ་ནི་དཔེར་ན་ཚངས་རིས་ཀྱི་ལྷ་དག་དང་པོར་བྱུང་བ་རྣམས་ཏེ། དེ་དག་ལུས་སྣ་ཚོགས་པ་ནི་སྔ་མ་བཞིན་ལ་འདུ་ཤེས་གཅིག་པ་ནི། ཐམས་ཅད་ཚངས་པས་བསྐྱེད་པར་འདུ་ཤེས་གཅིག་པའི་ཕྱིར་རོ། །

[Block 2402]
འདུ་ཤེས་སྣ་ཚོགས་ལ་ལུས་གཅིག་པ་ནི་འོད་གསལ་གྱི་ལྷའི་རིས་སྔ་ཕྱིར་སྐྱེས་པ་སྟེ། དེ་དག་ཐམས་ཅད་ཀྱི་ལུས་ཆེ་ཕྲ་བཟང་ངན་འདྲ་ཞིང་འོད་སྣང་བ་ཅན་དུ་གཅིག་ལ། མེའི་བསྐལ་པ་བསམ་གཏན་དང་པོར་བྱུང་བའི་ཚེ་ཁ་ཅིག་འཇིག །ཁ་ཅིག་མི་འཇིག་པའི་ཕྱིར་འདུ་ཤེས་ཐ་དད་དོ། །

[Block 2403]
ལུས་གཅིག་ལ་འདུ་ཤེས་གཅིག་པ་ནི་བསམ་གཏན་གསུམ་པ་ཡན་ཆད་དུ་སྐྱེས་པ་སྟེ། བསམ་གཏན་གསུམ་པའི་སེམས་ཅན་རྣམས་དེ་དག་དགེ་བའི་ཚོར་བ་ལ་རྟོག་པའི༌[^2091]འདུ་ཤེས་གཅིག་གོ། །

[Block 2404]
ལུས་གཅིག་པ་ནི་བསམ་གཏན་གཉིས་པ་བཞིན་ནོ། །

[Block 2405]
གཟུགས་མེད་པ་གསུམ་ནི་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་དང་། རྣམ༌[^2092]ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་དང་། ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་དེ། མི་དང་ལྷའི་རིས་མིང་གིས་སྨོས་པ་དེ་དག་གི༌[^2093]རྣམ་པར་ཤེས་པའི་རྒྱུ་བརྟན༌[^2094]པར་གནས་པའི་ཕྱིར་རྣམ་པར་ཤེས་པ་གནས་པ་ཞེས་བྱའོ། །

[Block 2406]
ངན་སོང་རྒྱུད་གསུམ་ནི་སྡུག་བསྔལ་སྣ་ཚོགས་ཀྱིས་གཡེན་སྤྱོ་བས་རྣམ་པར་ཤེས་པ་བརྟན་པར་མི་གནས་པས་དེར་མི་བགྲང་ངོ་། །འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས་ནི་དེ་ན་གཅིག་ཏུ་ངེས་པར་རྣམ་པར་ཤས་པ་ཀུན་དུ་འབྱུང་བ་མེད་པའི་ཕྱིར་མ་ཡིན་གྱི། གཟུགས་མེད་པའི་ཁམས་ཀྱི་འདུ་ཤེས་མེད་མིན་སྐྱེ་མཆེད་ཀྱང་འདུ་ཤེས་དང་། རྣམ་པར་ཤེས་པ་ཡོད་པ་ཡང་མ་ཡིན་མེད་པ་ཡང་མ་ཡིན་པས་བརྟན་པར་མི་གནས་སོ། །

[Block 2407]
ཚོར་བ་བརྒྱད་པོ་ཞེས་བྱ་བ་ནི་ཚོར་བ་བརྒྱད་ནི་བདག་ཏུ་ལྟ་བ་དང་། སེམས་ཅན་དུ་ལྟ་བ་དང་། གང་ཟག་ཏུ་ལྟ་བ་དང་། སྲོག་ཏུ་ལྟ་བ་དང་། ཐེར་ཟུག་ཏུ་ལྟ་བ་དང་། ནད་པར་ལྟ་བ་དང་། སྲིད་པར་ལྟ་བ་དང་། [^2095]སྲིད་པ་མེད་པར་ལྟ་བའོ། །

[Block 2408]
ཡང་ན་ལོག་པ་བརྒྱད་ནི་མི་ཁོམ་པ་བརྒྱད་དེ། དེ་དག་གི་ཚོར་བ་ལ་བྱའོ། །

[Block 2409]
སེམས་ཅན་གྱི༌[^2096]གནས་དགུ་ནི་གོང་མའི་རྣམ་པར་ཤེས་པ་གནས་བདུན་གྱི་སྟེང་དུ་འདུ་ཤེས་མེད་པ་དང་། སྲིད་པའི་རྩེ་མོ་གཉིས་བསྣན་པའོ། །

[Block 2410]
མི་དགེ་བ་བཅུ་ཞེས་བྱ་བ་ནི་རྒྱུ་བཅུ་ཡོད་པས༌[^2097]དེའི་རྒྱུ་ལས་བྱུང་བའི་སྡུག་བསྔལ་འབྲས་བུ་ཚོར་བ་ཡང་བཅུར་གཞག་གོ། །

[Block 2411]
འདི་ནི་ཚོར་བ་ཀུན་གྱི་ཚུལ་ཏེ་ཞེས་བྱ་བ་ནི་ཚོར་བ་འམ།[^2098] ཚོར་བའི་དངོས་པོ་ནི་མེད་ཀྱི། ཀུན་རྫོབ་ཏུ་ཚོར་བ་ཐ་དད་དུ་གདགས་ཤིང་རྣམ་གྲངས་སུ་བྱ་བ་གོང་དུ་བཤད་པའི་རིམ་པ་འདི་ལྟ་བུ་དག་གོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2412]
དམིགས་པ་ཇི་སྙེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཚོར་བ་མི་ཟད་པ་བསྟན་ཏེ། གཟུགས་ལ་སོགས་པ་དམིགས་པའི་ཡུལ་ཇི་སྙེད་པ་དེ་ལ་དམིགས་ཤིང་ཡིད་ལ་བྱེད་པ༌[^2099]དེ་སྙེད་དོ། །

[Block 2413]
ཡིད་ལ་བྱེད་པ་ཇི་སྙེད་པ་སེམས་ཡོངས་སུ་རྟོག་པ་ཡང་དེ་སྙེད་དོ། །

[Block 2414]
ཡོངས་སུ་རྟོག་པ་ཇི་སྙེད་པ་ཚོར་བ་ཡང་དེ་སྙེད་དེ།[^2100] དེ་བས་ན་ཚོར་བ་ཚད་མེད་ཅིང་མི་ཟད་པར་ཤེས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2415]
དེས་ཞེས་བྱ་བ་ནི་ཚོར་བ་ཚད་མེད་པའོ། །

[Block 2416]
རྗེས་སུ་ལྟ་ཞིང་གནས་པས་ཞེས་བྱ་བ་ནི་ཤེས་རབ་དང་ཏིང་ངེ་འཛིན་གྱིས་སོ། །ཤེས་པ་བསྐྱེད༌[^2101]ཅེས་བྱ་བ་ནི་སྐྱེ་བ་ལ་སྐྱེ་བར་ཤེས་པ་དང་། འཇིག་པ་ལ་འཇིག་པར་ཤེས་པ་དང་། གནས་པ་ལ་གནས་པར་ཤེས་པ་བསྐྱེད་པར་བྱའོ། །

[Block 2417]
ཚོར་བ་ལ་ཚོར་བའི་རྗེས་སུ་ལྟ་ཞིང་དྲན་པ་ཉེ་བར་གཞག་པ་མདོར་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། གང་སེམས་ཅན་ཐམས་ཅད་ཀྱི༌[^2102]ཚོར་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཤེས་པའི་ཚིག་སྐྱེ་བ་ལ་སོགས་པ་ཀུན་དང་སྦྱར་རོ། །

[Block 2418]
དགེ་བའི་རྒྱུ་ལས་བྱུང་བའི་ཚོར་བ་གང་ཡིན་པ་ཤེས་པ་དང་། མི་དགེ་བའི་རྒྱུ་ལས་བྱུང་བའི་ཚོར་བ་གང་ཡིན་པ་ཤེས་པའོ། །

[Block 2419]
ཚོར་བ་དྲན་པ་ཉེ་བར་གཞག་པ༌[^2103]བསྒོམ་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2420 [HEADING]]
#### སེམས་དྲན་པ་ཉེ་བར་གཞག་པ། ^8-1-3-0
--- END BLOCKS ---
