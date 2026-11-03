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
[Block 3186]
དེ་ལ་བྱ་བ་མི་འཕེལ་བའི་དབང་དུ་བྱས་པའི་ཚིགས་བཅད་བདུན་པོ་རྣམས་བསྡུས་པའི་དོན་ནི་འདི་ཡིན་ཏེ། སློབ་དཔོན་བཙུན་པ་གཞན་ལ་ཕན་པའི༌[^2011]དབྱངས་ཀྱིས་མདོ་སྡེ་རྒྱན་གྱི་ནང་དུ་ཆང་འཐུང་བའི་ཉེས་པའི་དབང་དུ་བྱས་ནས་གསུངས་ཏེ། དེ་ནི་ཚིགས་བཅད་འདི་དག་བསྡུས་པའི་དོན་ཡིན་ཏེ། ཇི་སྐད་དུ། གང་ཞིག༌[^2012]འཐུངས་པས་ལུས་རྙོག་དྲན་འཕྲོག༌[^2013]ཚུལ་ལས་འདའ་བ་དང་། ། བློ་རྨོངས་ངོ་ཚའི་ཆོས་གཅོད་འདུ་ཤེས་ཉམས་ཤིང་རིགས་བསླད་འགྱུར། །དགའ་མཆོག་ཉམས་ཤིང༌[^2014]ཞེ་སྡང་སྐྱེད་པར་བྱེད་པ་གང་ཞིག་གིས། །འཐུངས་ན་མྱོས་པར་འགྱུར་ཞིང་དྲན་ཉམས་དེ་ནི་འཆི་བཞིན་གནས། །ཞེས་བཤད་དོ། །

[Block 3187]
དེ་བས་ན་ཚིགས་བཅད་འདིའི་གོ་རིམས་ཀྱིས་མཚོན་པ་འདིས་ནི། གང་ཞིག་འཐུངས་ན་ར་རོ་བློང་ནས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་དག་གི་དོན་བསྟན་པ་ཡིན་ནོ། །

[Block 3188]
ལུས་རྙོག་ཅེས་བྱ་བ་དང་། དྲན་པ་འཕྲོག་པ་དང་། ཚུལ་ལས་འདའ་བ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་འཆི་བར་གྱུར༌[^2015]ན་ཡོན་ཏན་འདི་དག་ཉམས་པ་ཡིན་ཏེ། དེ་བཞིན་དུ་ཆང་འདི་འཐུངས༌[^2016]ན་ཡང་ར་རོ་བློང་ནས་གོམ་པ་དབང་མེད་འདོར་ཞིང་འགྲོ་བ་དང་། ཡུལ་ཕྱོགས་མ་འདྲིས་པར་ཡང་འཁྱམ་ཞིང་རྡེག་འཆོས་ཞེས་བྱ་བ་ཡིན་ཏེ། འདིར་ནི་སྔར་བསྟན་པའི་ལུས་རྙོག་ཅེས༌[^2017]བྱ་བ་དེ་བསྟན་པ་ཡིན་ནོ། །

[Block 3189]
དྲན་པ་ཉམས་པ་ཞེས་བྱ་བ་འདིས་ནི་གོང་དུ་བསྟན་པའི་དྲན་པ་འཕྲོག་ཅིང་ཞེས་བྱ་བ་དེ་ཉིད་སྟོན་ཏོ། །

[Block 3190]
བཟའ་དང་མི་བཟའི༌[^2018]དཔྱད་པ་མེད་པར་དེ་དང་དེ་དག་ཟར་འགྱུར་བ། །ཞེས་བྱ་བ་འདིས་ནི་གང་གོང་དུ་བསྟན་པའི་ཚུལ་ལས་འདའ་བ་ཞེས་བྱ་བ་དེ་སྟོན་ཏོ། །

[Block 3191]
ཚིགས་བཅད་ཀྱི་དོན་གང་སྔར་བསྟན་པའི་ངོ་ཚའི་ཆོས་གཅོད་ཅེས་བྱ་བ་དེའི་དབང་དུ་བྱས་ནས་ཚིགས་བཅད་གཉིས་ཡིན་ཏེ། གང་གིས་བདག་གི་སེམས་ལ་དབང་མེད་ཅེས་བྱ་བ་དང་། འཐུངས་ན་གང་གིས་བདག་གི༌[^2019]ངོ་ཚ་འོས་པའང་འདོར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ཏེ། ངོ་ཚའི་ཆོས་ཞེས་བྱ་བ་ནི་ཁྲེལ་ཡོད་པ་ཡང་འདི་ཡིན་ནོ། །

[Block 3192]
སྔར་བསྟན་པའི་བློ་རྨོངས་པར་བྱེད་ཅེས་བྱ་བ་འདི་ནི་ཁྲེལ་མེད་པའི་དབང་དུ་བྱས་ནས་གསུངས་པ་སྟེ། གང་གིས་བདག་གི་སེམས་ལ་དབང་མེད་བློ་ཉམས་རྣམ་པར་འཁྱམ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 3193]
གང་གི་ཕྱིར་ཤི་ན་ནི་བློ་ལ་ཁྲེལ་ཡོད་པ་མེད་དེ། དེས་ན་བདག་གི་སེམས་ལ་དབང་མེད་བློ་ཉམས་རྣམ་པར་འཁྱམ། །ཞེས་ཏེ། འདི༌[^2020]ནི་གང་སྔར་བསྟན་པའི་བློ་རྨོངས་པར་བྱེད་ཅེས་བྱ་བ་དེ་ཉིད་བསྟན་ཏོ། །

[Block 3194]
ཕྱུགས་དང་འདྲ་བར་བླུན་ཞིང་དགྲ་བོས་འཕྱས་ཀྱང་བྱེད་པར༌[^2021]འགྱུར། །གང་གིས་འདུན་སར་གར་བྱེད་འགྱུར་ཞིང་རང་གི་ཁར་རྔ་བརྡུང་། །ཞེས་བྱ་བའི་ཚིག་འདི་གཉིས་ཀྱིས་ནི་ཁྲེལ་ཡོད་པ་གཅོད་པར་བསྟན་ཏོ། །

[Block 3195]
ངོ་ཚའི་ཆོས་གཅོད་པའི་དབང་དུ་བྱས་ནས་འཐུངས་ན་གང་གིས་བདག་གི་ངོ་ཚ་འདོར་ཞེས༌[^2022]བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། བདག་གི་ངོ་ཚ་བ་ནི་མཛེས་པ༌[^2023]ཡིན་ཏེ། བདག་ཉིད་ལ་ལྟོས༌[^2024]ནས་འཛེམ་པ་ལ་བདག་གི་ངོ་ཚ་བ་ཞེས་བརྗོད་དེ་བདག་གི་དབང་དུ་བྱས་ནས། ཁ་ན་མ་ཐོ་བ་ལ་འཛེམ་པ༌[^2025]ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 3196]
གང་འཐུངས་ན་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་གང་གོང་དུ་བསྟན་པའི་འདུ་ཤེས་ཉམས་པར་འགྱུར་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པ་སྟེ། འདུ་ཤེས་ཉམས་པར་གྱུར་པ་ནི། །དྲན་པ་མེད་པར་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 3197]
གང་ཞིག༌[^2026]འཐུངས་ན་མྱོས་ཏེ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་ནི་གང་གོང་དུ་བཤད་པའི་རིགས་བསླད་ཅེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པ་སྟེ། འདི་ལྟར་བུད་མེད་ལ་འཕྱོས་པར་གྱུར་པས་རིགས་བསླད་པར་འགྱུར་རོ། །

[Block 3198]
གང་ཞིག་འཐུངས་ན་མྱོས་པས་དྲན་བརླག་སྟེ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་དགའ་མཆོག་ཉམས་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པ་སྟེ།

[Block 3199 [VERSE]]
མེ༌[^2027]བྱུང་ནས་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །
གང་ལ་ཆགས་ན་དཔལ་གྱི་གཞིར་གྱུར་རིགས། །

[Block 3200]
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་ཞེ་སྡང་སྐྱེད་པར་བྱེད་པ་དེའི་དབང་དུ་བྱས་པ་སྟེ། གང་གི་ཕྱིར་ཞེ་སྡང་ལས་ནི༌[^2028]རིགས་གཅོད་པར་བྱེད་པས་སོ། །

[Block 3201]
གློ་བུར་དུ་ངུ་ཞིང་ཞེས༌[^2029]བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་དྲུག་གིས་ནི། གང་ཞིག་འཐུངས་ན་བྱ་བ་ཉམས་ཤིང༌[^2030]བག་ཚ་བ་མེད་ཆོས་མི་སྤྱོད། །དོན་མེད་ཕུང་ཁྲོལ་ཤེས་ཤིང་འདུལ་དང་མི་ལྡན་བརྙས་ལ་གནས་མིན་རྡེག །ངུ་ལ་རྨོངས་ཤིང་སྨྲ་དང་འདོན་ཟློས་དགོད༌[^2031]བྱེད་སྨྱོ་འགྱུར་ཡོན་ཏན་དག །མ་ལུས་འཕྲོག་བྱེད་ཡ་རབས་ངོ་ཚ་ཅན་དག་སུ་ཞིག་འཐུང་བར༌[^2032]བྱེད། །ཅེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་བསྡུས་པའི་དོན་ཡིན་ཏེ། དེ་ལས་གློ་བུར་དུ་ངུ༌[^2033]ཞིང་འདུག་ལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་བརྙས་པ་ལ་སོགས་པ༌[^2034]དེའི་དབང་དུ་བྱས་པ་ཡིན་ནོ། །

[Block 3202]
རྒས་པར་གྱུར་ཀྱང་གང་གི༌[^2035]སེམས་ཉམས་ཤིང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་འདུལ་དང་མི་ལྡན་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པའོ། །

[Block 3203]
གང་གི་ཉེས་པས་སྔོན་གྱི་ལྷ་རྣམས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་བྱ་བ་ཉམས་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པ་ཡིན་ནོ།[^2036] །མི་བདེན་པ་ཡང་བདེན་པ་བཞིན་དུ་ངོ་མཐོན་སྨྲ།[^2037] །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་ཆོས་མི་སྤྱོད་ཅེས་བྱ་བ་དང་། ཕུང་ཁྲོལ་དོན་མེད་ཤེས་ཤིང་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པའོ། །

[Block 3204]
དེ་ལ་མི་བདེན་པ་ཡང་བདེན་པ་བཞིན་དུ་ངོ་མཐོན༌[^2038]སྨྲ། །ཞེས་བྱ་བ་དང་། མི་བྱ་བ་ཡང་བྱ་བ་བཞིན་དུ༌[^2039]དགའ་བཞིན་བྱེད། །ཅེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་པོ༌[^2040]འདིས་ནི་ཆོས་མི་སྤྱོད་ཅེས་གང་བསྟན་པ་དེ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 3205]
གང་གི་ལན་གྱིས་ཡོད་མེད་ཕྱིན་ཅི་ལོག་ཏུ་ཤེས། །ཞེས་བྱ་བ་འདིས་ནི་ཕུང་ཁྲོལ་དོན་མེད་ཅེས་བྱ་བ་སྔར་བསྟན་པ་དེ་ཉིད་བསྟན་ཏོ། །

[Block 3206]
མྱོས་གྱུར༌[^2041]རིག་སྔགས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་གང་སྔར་བསྟན་པའི་གནས་མིན་རྡེག་ཅིང་མྱོས་འགྱུར་ཡོན་ཏན་འཕྲོག་བྱེད་ཡ་རབས་སུ་ཞིག་འཐུང་བར་བྱེད། །ཅེས་བྱ་བ༌[^2042]དེ་དག་གི་དབང་དུ་བྱས་པའོ། །

[Block 3207]
གང་གིས་བློ་ནི་རབ་ཏུ་ཉམས་གྱུར་ནས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་བག་ཚ་བ་མེད་ཅེས་བྱ་བ་གང༌[^2043]བསྟན་པ་དེའི་དབང་དུ་བྱས་པའོ། །

[Block 3208]
འདིར་བག་ཚ་བ་མེད་པ་ནི་མི་འཇིགས་པ་སྟེ། མཚམས་མེད་པ་ལྔའི་ལས་ཀྱིས་ངན་འགྲོར་འགྲོ་བས་ཞེས་བྱ་བའི་དོན་ཏེ། ཚིགས་བཅད་འདི་གཉིས་ཀྱི་དོན་མདོ་སྡེ་རྒྱན་ལས་བླངས་པ་ཡིན་ཏེ། གཞུང་རབ་ཏུ་མངས་ཀྱིས་དོགས་པས་སྐབས༌[^2044]མ་ཡིན་པ་མང་པོ་ནི་འདིར་མ་བྲིས༌[^2045]སོ། །

[Block 3209]
འདི་དག་གི་གོ་རིམས་ཀྱི་རྒྱུ་ནི་དང་པོར་ལུས་དང་ཟུངས་ནི་གཞི་ཡིན་པའི་ཕྱིར་ལུས་དྲི་མ་ཅན་དུ་བྱེད་པ་ཞེས་བསྟན་པ་དེ་ཉིད་དོ། །

[Block 3210]
དེའི་འོག་ཏུ་ནི་དྲན་པ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3211]
ལུས་དང་དྲན་པ་ཉམས་པའི་འོག་ཏུ་ནི་ཚུལ་ཁྲིམས་དང་མཐུན་པའི་རིགས༌[^2046]ཞེས་བྱ་བའི་དབང་དུ་བྱས་ནས་སྨྲས་པའོ། །

[Block 3212]
དེའི་འོག་ཏུ་ཁྲེལ་ཡོད་པ་དང་ངོ་ཚ་ཤེས་པ་ནི་འཇིག་རྟེན་བསྲུངས་པའི༌[^2047]ཕྱིར་རོ། །

[Block 3213]
གཉིས་པོ་དེའི་འོག་ཏུ་ནི་འདུ་ཤེས་ཉམས་པའོ། །

[Block 3214]
དེ་ནས་རིགས་བསླད་པར་གྱུར་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཉེས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3215]
ད་ནི་དགའ་མཆོག་ཉམས་ཞེས་བྱ་བ་དང་། ཞེ་སྡང་སྐྱེད་པ་ཞེས་བྱ་བ་དེ་གཉིས་སྨོས་པ་ཡིན་ཏེ། སྐྱེ་བོ་ཉེ་དུ་དང་ཉེ་དུ་མ་ཡིན་པ་རྣམས་ཀྱང་གཅིག་ལ་གཅིག༌[^2048]རྣམ་པར་འཇིག་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3216]
དེ་ལྟར་རེ་ཞིག་ཚིགས་བཅད་བདུན་གྱི་གོ་རིམས་ཀྱི་རྒྱུ་བསྟན་ནས། ད་ནི་ཚིགས་བཅད་དྲུག་གི་གོ་རིམས་ཀྱི་རྒྱུ་བསྟན་པར་བྱ་སྟེ། གཞན་དག་ལ་བརྙས་པ་ཡིན་པས་ཡོངས་སུ་བརྙས་པ་སྟེ། དེ་བརྙས་པ་བྱུང་བའི༌[^2049]རྒྱུའོ། །

[Block 3217]
དེའི་འོག་ཏུ་འདུལ་དང་མི་ལྡན་པ་ཡིན་ནོ། །

[Block 3218]
དེའི་འོག་ཏུ་ནི་བྱ་བ་ཉམས་པའོ། །

[Block 3219]
དེའི་འོག་ཏུ་ནི་ཆོས་མི་སྤྱོད་པར་རོ། །

[Block 3220]
དེའི་འོག་ཏུ་ནི་ཚུལ་ཁྲིམས་མི་ཤེས་པ་སྟེ། མིའི་འཇིག་རྟེན་དུ་སྐལ་བ་ཉམས་པ་ཡིན་ན་ཡང་ངན་པར་གྱུར་པ་དང་། འཇིག་རྟེན་ཕ་རོལ་ཏུ་ཡང་མཚམས་མེད་པའི་ལས་ཀྱི་རྒྱུ་འདི་འབྱུང་བའོ། །

[Block 3221]
དེ་ལྟར་ཚིགས་བཅད་དྲུག་གི་གོ་རིམས་ཀྱི་རྒྱུ་འདི་དག་གོ། །

[Block 3222]
དེ་ལྟར་ཚིགས་བཅད་བཅུ་གསུམ་པོ་འདི་རྣམས་ཀྱི༌[^2050]དོན་བསྡུས་པའི་ཚིགས་བཅད་གཅིག་སྟེ། མི་ཡི་བདག་པོ་ཆང་འདི་དེ་འདྲ་ཡང་། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 3223]
ད་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཉེས་དམིགས་ཀྱི་དབང་དུ་བྱས་ནས། །གང་ཞིག་བསྟེན༌[^2051]ན་ངན་པ་སྤྱོད་པར་འགྱུར། །ཞེས་བྱ་བ་དང་། ཆང་དེ་ཉུང་ངུ་འཐུངས་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ཏེ། གང་ཞིག་བསྟེན་ན་རབ་ཏུ་འཇིགས་པར་ལྟུང་། །ཞེས་བྱ་བ་ནི་གང༌[^2052]སྔར་བསྟན་མ་ཐག་པའི་གང་ཞིག་བློ་ནི་རབ་ཏུ་ཉམས་གྱུར་ནས། ཞེས་བྱ་བའི་ཚིགས་བཅད་དེའི་མཚམས་མེད་པའི་ལས་ཀྱིས་ངན་སོང་གི་འགྲོ་བར་འཇུག་པ་ཡིན་ཏེ། ལས་དེ་བྱས་ནས་དམྱལ་བ་ལ་སོགས་པའི་ངན་སོང་རྣམ་པ་གསུམ་དུ་འགྲོ་བར༌[^2053]འགྱུར་ཏེ། དེ་ལྟར་འགྲོ་བའི་ལས་ཀྱང་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོའི་དབྱེ་བས་སོ། །

[Block 3224]
བསྟེན་པ་ཞེས་བྱ་བ་ནི་ཆང་བསྟེན་པའོ། །

[Block 3225]
ངན་པ་སྤྱོད་པར་འགྱུར་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ལས་ལ་སོགས་པ་རྣམ་པ་གསུམ་ངན་པར་སྤྱོད་པར་འགྱུར་བའོ། །
--- END BLOCKS ---
