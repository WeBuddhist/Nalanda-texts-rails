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
[Block 2346]
ལུས་ཀྱི༌[^2036]རྗེས་སུ་ལྟ་བ་ནི་གོང་མ་བཞིན་དུ་གཞན་གྱི༌[^2037]ལུས་ལ་དངོས་པོ་མེད་པ་དང་། སྟོང་པར་ལྟ་བའོ། །

[Block 2347]
ཕྱི་རོལ་གྱི༌[^2038]རྗེས་སུ་སོང་བའི་ཉོན་མོངས་པ་དང་། ལྷན་ཅིག་མི་གནས་པ་ནི་གཞན་གྱི༌[^2039]ལུས་ལ་དམིགས་པ་ལས་བྱུང་བའི་འདོད་ཆགས་དང་ཞེ་སྡང་ལ་སོགས་པའི་ཉོན་མོངས་པས་མ༌[^2040]གོས་པའོ། །

[Block 2348]
དེ་ལུས་ཉོན་མོངས་པ༌[^2041]ཅན་མ་ཡིན་པས་ཡོངས་སུ་དག་པའི་ལུས་ཀྱི་ལས་དང་ལྡན་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཉོན་མོངས་པའི་དབང་དུ་མ་གྱུར་པས་སྡིག་པ་མི་དགེ་བའི་ཆོས་མི་སྤྱོད་པའི་ལུས་ཀྱི༌[^2042]ལས་དང་ལྡན་པའོ། །

[Block 2349 [HEADING]]
###### **སྤྲུལ་པའི་སྐུ།** ^8-1-1-5-2-3-0

[Block 2350]
ལྷ་དང་མིའི་ནང་ན་མཚན་གྱིས་ལེགས་པར་བརྒྱན་པའི་ལུས་ཐོབ་ཅེས་བྱ་བ་ནི་དེ་དག་གི་ནང་ན་ཡང་མཚན་ཐམས་ཅད་ཚང་བས་བརྒྱན་པའི་ལུས་སྤྲུལ་པའི་སྐུ་འཐོབ་པའོ། །

[Block 2351]
མངོན་སུམ་དུ་འདོང་བར་འགྱུར་ཞེས་བྱ་བ་ནི་དེའི་གན་དུ་འགྲོ་ཞིང་དེའི་འཁོར་དུ་ཁས་ལེན་པར་འགྱུར་བའོ།[^2043] །དེ་ལྟར༌[^2044]ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་ལྟར་རོ། །

[Block 2352]
ལུས་དྲན་པ་ཉེ་བར་གཞག་པ་སྒོམ་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2353 [HEADING]]
#### ཚོར་བ་དྲན་པ་ཉེ་བར་གཞག་པ། ^8-1-2-0

[Block 2354]
རབ་ཏུ་ཚོར་བ་གང་ཞེ་ན། གང་ཚོར་བ་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་གནས་པ་སྟེ། སྡུག་བསྔལ་གསུམ་ལས་འདས་པ་ཡང་འཐོབ་ལ། ཟག་པ་མེད་པའི་ཚོར་བ་དགེ་བ་ཞི་བ༌[^2045]ཡང་ཚོར་བར་བྱེད་པའོ། །

[Block 2355]
དེའི་དབང་དུ་བྱས་ནས་དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཚོར་བའི་རྗེས་སུ་ལྟ་བ་དྲན་པ་ཉེ་བར་གཞག་པ༌[^2046]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^2047]ཁོང་དུ་ཆུད་ཅིང་བསྒོམ་པར་བྱ་བའི་ཚོར་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ཚོར་བའོ།[^2048] །ཚོར་བ་རྣམས་ནི་བདེ་བ་དང་སྡུག་བསྔལ་ལ་སོགས་པ་སྟེ། གཞན་གྱི་དོན་དུ་བཤད་པ་བཞིན༌[^2049]སྦྱར་རོ། །

[Block 2356]
འདི་ལ་ཞེས་བྱ་བ་ནི་ཚོར་བ་རྣམ་པ་གསུམ་ལའོ། །

[Block 2357]
འདི་སྙམ་དུ་སེམས་ཏེ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་རྟོག་སྟེ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2358]
ཚོར་བ་གང་ཅི་ཡང་རུང་སྟེ་དེ་ཐམས་ཅད་སྡུག་བསྔལ་ཞེས་བྱ་བ་ནི་ཚོར་བ་ཐམས་ཅད་ཀྱང་སྡུག་བསྔལ་བའི་རང་བཞིན་ཏེ། བདེ་བའི་ཚོར་བ་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ་ཡང་མ་ཡིན་པའི་ཚོར་བ་རྣམས་ཀྱང་མཐར་སྡུག་བསྔལ་དུ་འགྱུར་ཞིང་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་གྱིས་ཁྱབ་པའི་ཕྱིར་རོ་སྙམ་ནས་ཞེས་བྱ་བ་ནི་དེ་ལྟར་རྟོགས༌[^2050]ནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2359]
དེས་ཞེས་བྱ་བ་ནི་ཚོར་བ་དྲན་པ་ཉེ་བར་གཞག་པ་ལས༌[^2051]གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེས་སོ། །

[Block 2360]
ཚོར་བ་ཤིན་ཏུ་རྟོགས་པ༌[^2052]དང་ཞེས་བྱ་བ་ནི་ཚོར་བ་དངོས་པོ་མེད་པ་འམ། ཚོར་བ་ཐམས་ཅད་སྡུག་བསྔལ་བ་ཡིན་པར་ཕྱིན་ཅི་མ་ལོག་ཅིང་ལེགས་པར་རྟོགས༌[^2053]པའོ། །

[Block 2361]
ཡེ་ཤེས་ཀྱིས་རྟོགས༌[^2054]པ་ནི་དེ་ལྟ་བུར་འཕགས་པའི་ཡེ་ཤེས་ཟག་པ༌[^2055]མེད་པས་ཁོང་དུ་ཆུད་པའོ། །ཤེས་རབ་ཀྱིས་རྟོགས་པ༌[^2056]ནི་ཟག་པ་མེད་པའི་ཤེས་རབ་ཀྱིས་རྟོགས༌[^2057]པའོ། །

[Block 2362]
ཉེ་བར་ཞི་བས་རྟོགས་པ༌[^2058]ནི་ཉོན་མོངས་པ་ཞི་བའི་ཤེས་པས་རྟོགས་པའོ།[^2059] །བདེ་བའི་ཚོར་བ་ཡང་བདེ་བར་བྱེད་ཅེས་བྱ་བ་ནི་ཟག་པ་མེད་པའི་བདེ་བའི་ཚོར་བ་ཚོར་བར་བྱེད་པའམ། བདེ་འགྲོའི་ཚོར་བ་ཉིད་མྱོང་བར་བྱེད་པའོ། །

[Block 2363]
དེ་འདོད་ཆགས་ཀྱི་བག་ལ་ཉལ་ཡང་བག་ལ་ཉལ་བར་མི་འགྱུར་ཞེས་བྱ་བ་ལ་ཚོར་བ་ཐམས་ཅད་སྟོང་པར་ཁོང་དུ་ཆུད་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེས་གོང་དུ་བཤད་པ་ལྟར་བདེ་བའི་ཚོར་བ༌[^2060]ཡང་དངོས་པོ་མེད་པར་ཁོང་དུ་ཆུད་པས་བདེ་བའི་ཚོར་བས་ཀྱང་འདོད་ཆགས་མི་སྐྱེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2364]
སྡུག་བསྔལ་གྱི་ཚོར་བས་རེག་པ་ན་ཡང་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་གྱི་ཚོར་བ་མྱོང་བར་གྱུར་པ་ན་ཡང་ཤིན་ཏུ་བཟོད་པར་དཀའ་བའི་ངོ་བོ་ཡིན་པར་རིག་ནས་ངན་སོང་ལ་སོགས་པ་སྡུག་བསྔལ་གྱི་ཚོར་བ་དང་ལྡན་པ་རྣམས་ལ་སྙིང་རྗེ་ཆེན་པོ་བསྐྱེད་ཅིང་སྡུག་བསྔལ་གྱི་ཚོར་བ་ཉིད་ཀྱང༌[^2061]རང་བཞིན་མེད་པར་རྟོགས་པས་དེའི་རྒྱུ་ལས་ཁོང་ཁྲོ་བ་ཡང་མི་སྐྱེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2365]
བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ༌[^2062]ཡང་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ༌[^2063]བཏང་སྙོམས་ཀྱི་ཚོར་བ་ཡང་མྱོང་བ་དེ་དག་རང་བཞིན་མེད་པར་ཁོང་དུ་ཆུད་པས་དེའི་རྒྱུས་གཏི་མུག་ཀྱང་སྐྱེ་བར་མི་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2366]
དེ་ཚོར་བ་དང་ལྡན་པའི་དྲན་པས་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་དེས༌[^2064]ཚོར་བ་གསུམ་བསྒོམ་པ༌[^2065]དང་ལྡན་པའི་ཤེས་རབ་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2367]
ཚོར་བ་དེ་དག་ཐམས་ཅད་ལས་བྱུང་བའི་ཡེ་ཤེས་མཐོང་བ་བསྒོམ་མོ་ཞེས་བྱ་བ་ནི་གོང་དུ་སྨོས་པའི་ཚོར་བ་དེ་དག་དང་བྲལ་བ་ཡེ་ཤེས་དེ་རྟོགས་པར་བསྒོམ༌[^2066]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2368]
དེ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཚོར་བ་ཞེས་བྱ་བ་ནི་ཚོར་བ༌[^2067]བདག་གི་ཚོར་བ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཚོར་བའི་རང་བཞིན་ཁོང་དུ་ཆུད་པར་བྱ་བའི་ཕྱིར་བརྩོན་འགྲུས་རྩོམ་པར་བྱེད་པའོ། །

[Block 2369]
ཚོར་བ་ལས་ངེས་པར་འབྱུང་བ་ནི་ཚོར་བ་ལས་ཐར་བར་བྱེད་པའི་ཐབས་ཚོལ་བ་ཐམས་ཅད་སྟོང་པ༌[^2068]ཡིན་པར་ཤེས་པའོ། །

[Block 2370]
བདག་ནི་ཤེས་རབ་དང་ཡེ་ཤེས་ཡོངས་སུ་ལྡན་པའི་ཚོར་བས་ཞེས་བྱ་བ་ལ། [^2069]ཟག་པ་མེད་པའི་ཡེ་ཤེས་དང་ལྡན་པའི་ཚོར་བ་དང་། ཟག་པ་མེད་པའི་ཡེ་ཤེས་དང་ལྡན་པའི༌[^2070]ཚོར་བས་ཚོར་བ་ཀུན་ཏུ༌[^2071]སྟོང་པ་ཉིད་དུ་རིག་པ༌[^2072]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2371]
ཚོར་བ་ཐམས་ཅད་རྒྱུན་ཆད་པའི་ཐབས་མཁས་པ་ཞེས་བྱ་བ་ནི་ཚོར་བ་ཐམས་ཅད་སྟོང་པར་ཁོང་དུ་ཆུད་པས་བདེ་བའི་ཚོར་བ་ལ་སོགས་པ་མྱོང་ཡང་འདོད་ཆགས་དང་ཞེ་སྡང་མི་སྐྱེ་བའི་ཐབས་མཁས་པས༌[^2073]སོ། །

[Block 2372]
སྙིང་རྗེ་ཆེན་པོས་ཟིན་པས་ཞེས་བྱ་བ་ལ། སྙིང་རྗེ་ཆེན་པོ་དང་ལྡན་པ་ལས་བྱུང་བའི་དགེ་བའི་རྩ་བའོ། །

[Block 2373]
ཚོར་བ་དྲན་པ་ཉེ་བར་གཞག་པ་རྣམ་གྲངས་གཞན་ཡང་བསྟན་པའི་ཕྱིར་ཡང་ཅིའི་ཕྱིར་ཚོར་བ་ཞེས་བྱ་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2374]
མ་རྟོགས་པའི་ཚོར་བ་ནི་སྡུག་བསྔལ་དུ་འགྱུར་ཞེས་བྱ་བ་ནི་ཚོར་བ་མྱོང་བ༌[^2074]དངོས་པོ་མེད་པར་མ་རྟོགས་པའི་ཚོར་བ་ནི་སྡུག་བསྔལ་སྐྱེ་བའི་རྒྱུར་འགྱུར་བའོ། །

[Block 2375]
ཡེ་ཤེས་ཀྱིས༌[^2075]རྟོགས་པའི་ཚོར་བ་ཞེས་བྱ་བ་ནི་ཚོར་བ་མྱོང་ལ། ཡེ་ཤེས་ཀྱིས་སྟོང་པར་རྟོགས་པའི་ཚོར་བ་ནི་ཟག་པ་མེད་པའི་བདེ་བ་སྐྱེ་བའི་རྒྱུར་འགྱུར་བའོ། །

[Block 2376]
གང་གིས་ཀྱང་ཚོར་བར་འགྱུར་བ་མེད་ཀྱི་ཞེས་བྱ་བ་ནི་ཚོར་བ་མྱོང་བར་བྱེད་པའི་བདག་དང་སེམས་ཅན་ལ་སོགས་པ་གོང་དུ་སྨོས་པ་རྣམས་ནི་མེད་ཀྱི། ཕྱིན་ཅི་ལོག་ཏུ་རྟོག་ཅིང་མངོན་པར་ཞེན་པ་ཉིད་ཚོར་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2377]
དེ་བས་ན་མངོན་པར་ཞེན་པ་ནི་ཞེས་བྱ་བ་དངོས་སུ་གསུངས་སོ། །

[Block 2378]
ཡང་ན་མངོན་པར་ཞེན་པ་ལ་སོགས་པ་ནི་ཚོར་བ་སྐྱེ་བའི་རྒྱུ་ཡིན་པས་དེ་དག་ལ་ཚོར་བ་ཞེས་གསུངས་སོ། །

[Block 2379]
མངོན་པར་ཞེན་པ་ནི་བདག་ཡོད་པར་མངོན་པར་ཆགས་པའོ། །

[Block 2380]
ཡོངས་སུ་འཛིན་པ་ནི་བདག་གིར༌[^2076]འཛིན་པའོ། །

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
--- END BLOCKS ---
