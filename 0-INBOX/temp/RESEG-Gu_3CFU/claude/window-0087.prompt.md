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
[Block 3046]
བ་གླང༌[^2068]རྫིའམ་ཕྱུགས་རྫི་དག་ལ་གཏང་དེ་ཟན་ལ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དུས་དེ་ཙམ་དུ་བ་གླང༌[^2069]རྫི་དང་ཕྱུགས་རྫི་རྣམས་ཀྱིས་ཁས་བླངས་པ་དང་མི་བསྐྱེད་པ་ལ་རང་གིས་བརྩོན་པར་གྱུར་པ་འམ་མགོན་མེད་པ་སླར་གཏད་པ་དང་། མཚན་མོ་ཡང་འོང་བའི་དོན་དུ་འབད་པར་བྱའོ། །

[Block 3047]
འོང་བ་མ་གྲུབ་པ་དང་མི་ནུས་པ་ཉིད་ཀྱིས༌[^2070]འདི་ལ་བདག་ཉིད་བསྲུང་བ་ལ་དེ་ཉིད་དུ་གནས་པ་ཞེས་བྱ་བའི་དོན་གྱིས་ཤེས་པར་བྱའོ། །

[Block 3048]
འཚོ་འམ་འོན་ཏེ་མ་ཡིན་ཞེས་ཡང་དང་ཡང་དུ་བརྟག་པར༌[^2071]བྱའོ་ཞེས་བྱ་བ་ནི་འཇིག་པ་དང་མི་འཇིག་པའི་དོན་འབད་པས་སོ་སོར་བརྟག་པའོ། །

[Block 3049]
སེམས་དག་པས་སྙིང་བརྩེ་བས་བུད་མེད་དེ༌[^2072]ལ་འཁྱུད་པ་ལ་ཉེས་པ༌[^2073]མེད་དོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་སྨན་གྱི་གཞི་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་བུད་མེད་སྐྲ་གྲོལ་བ་ལ་འཁྱུད་པ་གནང་ངོ་ཞེས་འབྱུང་བ༌[^2074]སྟེ། དེ་མདོ་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 3050]
འདིར་དགེ་བའི་སེམས༌[^2075]ཉིད་ཙམ་ནི་དག་པའི་སེམས་ཉིད་དུ་རིག་པར་བྱའི། འདོད་ཆགས་དག་དང་བྲལ་བའི་སེམས་ཉིད་ཁོ་ན་ནི༌[^2076]མ་ཡིན་ནོ། །

[Block 3051]
དགེ་འདུན་གྱི་ལྷག་པ༌[^2077]གཉིས་པའི་རྣམ་པར་འབྱེད་པའོ།། །།

[Block 3052]
འཇམ་པ་དང་དྲོ་བ་དང་སྙི་བའི་བསམ་པ་ཉིད་ན༌[^2078]སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི༌[^2079]འཇམ་པ་ཡིན་ནམ་འོན་ཏེ་མ་ཡིན་སྙམ་པའི་བསམ་པ་ཉི་ཚེས་བུད་མེད་ལ་ཉམས་སུ་མྱོང་བ་ལ༌[^2080]ཡིན་གྱི། རེག་པ་རྩེ་གཅིག་པ་ཉིད་ཀྱིས༌[^2081]འཁྱུད་པ་དང་སོ་སོ༌[^2082]ཡང་དག་པར་ལྡན་པའི་རོ་མྱང་བའི་བསམ་པ༌[^2083]ཉིད་ཀྱིས་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3053]
འདིར་གཞུང་ནི་བཙུན་པ་རེ་ཞིག་དགེ་འདུན་གྱིས༌[^2084]དྲོ་བའི་བསམ་པ་དང་ལྡན་པས་ལུས་ལ་རེག་པར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར།

[Block 3054 [VERSE]]
ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
དེ་བཞིན་དུ་འཇམ་པའི་བསམ་པ་དང་ལྡན་པ་དང་།
སྙི་བའི་བསམ་པ་དང་ལྡན་པ་ཞེས་བྱ་བའོ། །

[Block 3055]
ཀུན་དུ་འདོད་ཆགས་པ་མེད་པར་བུད་མེད་དག་གི་ལུས་ལ་རེག་པ་རྣམ་པ་ལྔ་གསུངས་ཏེ་དེ་ནི་ཁྱད་པར་ཅན་གྱི་སྤྱོད་པ་དང་། དེ་དང་འདྲ་བ་དང་། དོན་མེད་པར་རེག་པ་ཁོ་ན་ཡིན་པ་དང་། རྒོད་བག་གིས༌[^2085]རེག་པའི་བྱེ་བྲག་ཉམས་སུ་མྱོང་བར་འདོད་པ་དང་། མི་འདོད་པར་སྐྱེ་བོ་མང་པོ༌[^2086]ལྟོས་པའི་དུས་དག་ཏུ་དབང་མེད་པར་རེག་པ་གང་ཡིན་པ་རྣམས་སོ། །

[Block 3056]
འདིར་ཁྱད་པར་ཅན་གྱི་སྤྱོད་པ་ནི་རྣམ་པ་གསུམ་སྟེ། སྙིང་བརྩེ་བ་དང་ཉེ་དུ་བཤེས་པ་མཐོང་བ་དང་། སྔོན་སྤྱད་པ་ལ་ཀུན་དགའ་བ་ཉམས་སུ་མྱོང་བའོ། །

[Block 3057]
ཁྱད་པར་ཅན་གྱི་སྤྱོད་པ་དང་འདྲ་བ་ནི་གནས་མ་ཡིན་པ་ལ་སྙིང་བརྩེ་བ༌[^2087]ལ་སོགས་པ་རྣམས་ལ་དེའི་ངོ་བོས་མི་འཇུག་པའོ། །

[Block 3058]
དཔེར་ན་འགྱེལ་བ་རང་ཉིད་སྔངས་པར་ནུས་པ་སློང་བར་བྱེད་པའོ། །

[Block 3059]
རྣམ་པ་ལྔ་པོ་འདི་རྣམས་ལ་ཞུ་བ༌[^2088]འདི་རྣམས་ཏེ། གང་ཞིག་འདུལ་བྱེད་དག་ལས་ལྟུང་བ་དང་ལྟུང་བ་མེད་པ༌[^2089]རྣམས་བསྟེན་པའི༌[^2090]ཕྱིར་བརྗོད་དོ། །

[Block 3060]
སྙིང་བརྩེ་བས༌[^2091]སྡུག་བསྔལ་ལས་ཐར་པར་བྱ་བ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་མེ་དང་གཡང་ས་དང་མཚོན༌[^2092]དང་གག་མིག་དང་། དུག་ཟ་བ་དང་སྦྲུལ་གྱིས་སོས༌[^2093]བཏབ་པ་དང་སྟག་དང་འདབ་ཆགས་དང་མི་མ་ཡིན་པ་ལ་སོགས་པའི་རྒུད་པའི༌[^2094]རྒྱུ་མཚན་གྱི་སྡུག་བསྔལ་ལས་གྲོལ་བ་ལ་རེག་པ་གང་ཡིན་པ་དེ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3061]
མ་དང་བུ་མོ་དང་སྲིང་མོ་རྣམས་ལ་དེ་དག་ཏུ་འདུ་ཤེས་པའོ་ཞེས་བྱ་བ་ནི་མ་ལ་སོགས་པའི་འདུ་ཤེས་དེ་རྣམས་ཡོད་པར་གྱུར་པ་ལས་མ་ལ་སོགས་པ་ལ་རེག་པས་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3062]
སྔོན་སྤྱད་པ་ཉིད་ལ་ཀུན་དགའ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཀུན་དགའ་བའི་མཚན་ཅན་གྱི་རེག་པ་ལ་ལྟུང་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3063]
དགེ་འདུན་ལྷག་མ་གཉིས་པའི་ཞུ་བའི་སྐབས་སོ།། །།

[Block 3064]
ཟས་དང་ས་དང་བོང་བ་ལ་སོགས་པ་མོའི་དབང་པོར་འཇུག་ན་སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི་འདི་ནི་རྣམ་པར་འགྱུར་བར་གྱུར་པ་མི་ཚངས་པར་སྤྱོད་པའི་ལམ་གྱི་རྣམ་པར་ངེས་པར་འདིར་རྒོད་བག་ཅེས་བྱ་བ་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་ཉིད་དོ། །

[Block 3065]
རྐང་པ་དང་ཕྲག་པ་ལ་སོགས་པས་བུད་མེད་ལ་ཕུལ༌[^2095]ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ལ་འདི་ནི་ཤིན་ཏུ་མ་ཁྱབ་པ་སྟེ། ཇི་ལྟར་སྔར་བསྟན་པ་ཞེས་བྱ་བ་འདི་ཤེས་པའོ། །

[Block 3066]
པུས་མོ་དང་རྗེ༌[^2096]ངར་དང་བརླ་དང་རྐེད་པ༌[^2097]དང་ལག་པ་དང་དཔུང་པ་དང་མགོ་བོ་ལ་སོགས་པ་གཅིག་པུ༌[^2098]རྣམས་ཁོ་ནར་མ་ཟད་ཀྱི༌[^2099]སེན་མོ་ལ་སོགས་པ་རྣམས༌[^2100]ཡང་འདི་སྙེགས་པར་རིག་པར་བྱའོ། །

[Block 3067]
དེའི་སྟན་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བུད་མེད་དང་བཅས་པ་འམ། བུད་མེད་མེད་པའི་བུད་མེད་ཀྱི་སྟན་ལ་རྐང་པའི་ཆུ་ལ་སོགས་པས་འཕུལ་ན་ཉེས་བྱས་སོ། །

[Block 3068]
བུད་མེད་དང་བཅས་པ་ཉིད་ཀྱིས་འདི་རྣམས་ལ་བུད་མེད་ཀྱི་སྟན་བསྟེན་པ༌[^2101]འདོན་པ་ཡིན་ཏེ། འདིར་གཞུང་ནི་དགེ་སློང་གིས་བུད་མེད་དང་བཅས་པ་འམ། བུད་མེད་མེད་པའི་སྟན་ལ་རྐང་པས་བསྒུལ་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3069]
བུད་མེད་དང་བཅས་པ་ཉིད་ལ་ནི་འདིར་ཉེས་བྱས་ཡིན་ཏེ། འོན་ཀྱང་བུད་མེད་ལ་དགའ་བས་འདི་ཕུལ་བ་གཅིག་པུ་ཉིད་ལ་ཡང་ཉེས་བྱས་དང་སྦྱོར་བ་ཞེས་བྱ་བ་འདི་ལྟར་མདོ་བྱས་སོ། །

[Block 3070]
འདྲེད་པས་འགྱེལ་བའི་བུད་མེད་སློང་བའོ་ཞེས་བྱ་བ་ནི་འདྲེད་པས་འགྱེལ་བའི་བུད་མེད་སློང་ན་ཉེས་བྱས་སོ། །

[Block 3071]
འདི་ནི་ཉམ༌[^2102]ང་བར་གྱུར་པས་འགྱེལ་བ་མ་ཡིན་ནོ།[^2103] །དེ་བས་ན་ལེགས་པར་མ་བྱས་པ༌[^2104]ཉིད་ཀྱིས་འཇུག་པ་འདི་ཡིད་ལ་ངེས་པར་འབྲེལ་བ་ཡིན་གྱི་སྙིང་རྗེའི་དངོས་པོ་རྒྱུ་མཐུན་པ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 3072]
དེ་བས་ན་འདིར་ལྟུང་བ་རྣམ་པར་གཞག་པའོ། །

[Block 3073]
ཉེས་བྱས་ལ་སྙིང་བརྩེ་བའི་ངོ་བོ་ཉིད་ཀྱི་ཕྱིར་སྦོམ་པོའི་ལྟུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 3074]
བུད་མེད་ཀྱིས་དེ་གསུམ་བྱེད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་རྐང་པའི་ཆ་ལ་སོགས་པས་དགེ་སློང་འཕུལ་བ་དང་། དགེ་སློང་གི་སྟན་ལ་འཕུལ་བ་དང་། འདྲེད་པས་འགྱེལ་བ་སློང་བ་ཞེས་བྱ་བ་གསུམ་པོ་འདི་བུད་མེད་ཀྱིས་བྱས་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 3075]
མི་འདོད་བཞིན་དུ་འབྱུང་བ༌[^2105]ཉིད་ཀྱི་ཕྱིར་འདི་དང་འཆད་པར་འགྱུར་བ་ལ་སྐྱོན་མེད་པ་ཉིད་དོ། །

[Block 3076]
བཟུང་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མི་འདོད་བཞིན་དུ་བུད་མེད་ཀྱིས་བཟུང་བ་ལ་ཡང་ལྟུང་བ་མེད་དོ། །

[Block 3077]
མས་འཁྱུད་པ་ལ་ཡང་ངོ་། །བང་པར་བུ༌[^2106]མོ་འདུག་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བར་སྦྱོར༌[^2107]རོ། །

[Block 3078]
བུད་མེད་འཁྲུལ་བ་སྟེང་དུ་འགྱེལ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3079]
དགེ་འདུན་ལྷག་མ་གཉིས་པའི་འདུལ་བྱེད་ཀྱི་སྐབས་སོ།། །།

[Block 3080]
ལུས་ཀྱིས་རེག་པའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 3081]
གང་ཞིག་སྨྲས་ན་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འཁྲིག་པ་སྨྲས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུད་མེད་མཐུ་ཡོད་པ་ལ་ཀུན་ནས་ཆགས་པས་ཞེས་བྱ་བ་འདི་སྔར་བརྗོད་པ་རྟོགས་པར་བྱའོ། །

[Block 3082]
སླར་ཡང་འཁྲིག་པ་ནི་གཉིས་ཀྱིས་གཉིས་སྤྲོད་པ་སྟེ་དེ་སྨྲས་ནའོ། །

[Block 3083]
སྒྲ་ཇི་ལྟ་བུས་དེ་བརྗོད་པ་གང༌[^2108]ཞེ་ན། དེའི་ཕྱིར་རྒྱ་ལ་སོགས་པའི་དོན་གྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར༌[^2109]རྒྱ་ལ་སོགས་པའི་སྒྲ་ནི་ཡ་ཡིག་དང་བྷ་ཡིག་གི་རང་བཞིན་ཞེས་བྱ་བ་བརྗོད་པའོ། །

[Block 3084]
དེའི་དོན་ཅན་རྒྱ་ལ་སོགས་པ་རྣམ་པ་གཞན་གྱིས་འཁྲིག་པ་བརྗོད་པ་གང་ཡིན་པར་སྟོན་པ་དེ་ནི་རྒྱ་ལ་སོགས་པ་ཞེས་བྱ་བ་གྲགས་པ་ཉེ་བར་སོང་བའོ། །

[Block 3085]
རྒྱའི་དོན་ནི་མཐོང་བར་རིག་པར་བྱ་བ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
