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
སེམས་ཅན་ཐམས་ཅད་ཀྱིས་ཡོངས་སུ་ཐོབ་པར་བྱ་བ་ནི་གང་རིག་པའི་གནས་དང་། བཟོའི་གནས་དང་། ལོངས་སྤྱོད་ལ་སོགས་པའོ། །

[Block 3187]
གང་འཕགས་པ་ཐམས་ཅད་དང་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་དང་། བྱང་ཆུབ་སེམས་དཔའ་ས་ལ་ཞུགས་པ་དང་། དེ་བཞིན་གཤེགས་པ་དག་གོ། །

[Block 3188]
ཐེག་པ་ལ་གསར་དུ་ཞུགས་པ་ནི་དང་པོ་ཉིད་དུ་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའམ། མོས་པས་སྤྱོད་པའི་ས་ལ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སོ། །

[Block 3189]
ཐོབ་པར་བྱ་བ་ནི་དེ་དག་གིས༌[^2749]ཐོབ་པར་བྱ་བའི་ཡོན་ཏན་དྲན་བ་ཉེ་བར་གཞག་པ་དང་། ཡང་དག་པའི་སྤོང་བ་ལ་སོགས་པ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི༌[^2750]ཆོས་སུམ་ཅུ་རྩ་བདུན་དང་། ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པའོ། །

[Block 3190 [HEADING]]
### བཟོད་པ་ཐོབ་པ། ^11-2-0

[Block 3191]
བཟོད་པ་ཐོབ་པ་ནི་བདག་ཉིད་ཀྱིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་ཡོངས་སུ་སྦྱོང་བར་བྱེད་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། སྦྱིན་པ་ནི་བདག་གི་གྲོགས་མ་ཡིན་གྱི་ཞེས་བྱ་བ་ལ༌[^2751]སོགས་པ་གསུངས་སོ། །

[Block 3192]
དེའི་དོན་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དེ་དག་གིས་བདག༌[^2752]བསྒྲུབ་ཅིང་ལས་སུ་རུང་བར༌[^2753]བྱ་བ་མ་ཡིན་གྱི། བདག་གིས༌[^2754]དེ་དག་བསྒྲུབ་ཅིང་མཐར་དབྱུང་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3193 [HEADING]]
### མཉམ་པ་ཉིད་ལ་གནས་པ། ^11-3-0

[Block 3194]
མཉམ་པ་ཉིད་ལ་གནས་པས༌[^2755]ནི་སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་ཆོས་བསྡུ་བའི་དངོས་པོ་རྣམས་བསྒྲུབས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། བདག་ལ་བསྡུ་བའི་དངོས་པོ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་དག་གི་དོན་ཀྱང་སྔ་མ་བཞིན་དུ་ལྟའོ།[^2756] །

[Block 3195 [HEADING]]
### སྒྲིབ་པ་མེད་པ། ^11-4-0

[Block 3196]
སྒྲིབ་པ་མེད་པ་ནི་བདག་གཅིག་པུས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པའི་བར་དུ་གཅོད་པའི་བགེགས་རྣམས་འཇོམས་པ༌[^2757]སྟེ། དེའི་དབང་དུ་བྱས་ནས། གང་འདི་ལྟ་བུའི་ཆོས་ལ་གྲོགས་མེད་པར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3197]
འདི༌[^2758]ལྟ་བུའི་ཆོས་ནི་གོང་དུ་བཤད་པའི་འཇིག་རྟེན་པའི༌[^2759]ཡོན་ཏན་དང་། འཇིག་རྟེན་ལས་འདས་པའི་ཡོན་ཏན་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། བསྡུ་བའི་དངོས་པོ་ལ་སོགས་པ་དང་འོག་ནས་འབྱུང་བ་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་འཚང་རྒྱ་བའི་ཆོས་རྣམས་སོ། །

[Block 3198]
ཤེས་རབ་ཀྱིས་ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་སོ། །

[Block 3199]
གཅིག་པུ་བགྲོད་པའི་ལམ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 3200 [HEADING]]
## བྱ་བ་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^12-0

[Block 3201]
བྱ་བ་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་རྣམ་པ་བཞི་སྟེ། སྟོན་པ༌[^2760]དང་། འཇུག་པ་དང་། གཅོད་པ་དང་། འདོགས་པར་བྱེད་པའོ། །

[Block 3202]
དེ་ལ་སྟོན་པ་ནི་སེམས་ཅན་རྣམས་ལ་སྐྱེས་བུ་ཆེན་པོ་བཞིན༌[^2761]མོས་ཤིང་སྐྱེས་བུའི༌[^2762]བྱ༌[^2763]བའི་ཐབས་ཤེས་པའོ། །

[Block 3203]
འཇུག་པ་ནི་རྟོགས་པར་ཆུད་པའི་ཐབས་ཤེས་པའོ། །

[Block 3204]
གཅོད་པ་ནི་དྲང་བའི་ཐབས་ཤེས་པའོ།[^2764] །འདོགས་པར་བྱེད་པ་ནི་བསྟན་པའི་ཚུལ་གྱིས་ཡོངས་སུ་སྨིན་པའི་ཐབས་ཤེས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། བཙུན་པ་ཤ་ར་དྭ༌[^2765]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཐབས་མི་ཟད་པ་སྟེ། ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། འདིས་བསྡུས་པའི་དོན་ཆོས་ཀྱི་འཁོར་ལོ་རབ་ཏུ་བསྐོར་བ་བསྟན་ཏོ། །

[Block 3205]
ཐབས་མི་ཟད་པ་ཡང་ཐབས་ཀྱིས་བསྒྲུབ་པར་བྱ་བའི་ཆོས་རྣམས་མི་ཟད་པའི་ཕྱིར། དེ་སྒྲུབ་པར་བྱེད་པའི་ཐབས་ཀྱང་མི་ཟད་པའོ། །

[Block 3206]
ཐབས་གང་གིས་བྱང་ཆུབ་སེམས་དཔའ་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་རྣམ་པར་སྒྲུབ་ཅིང་སློང་བ་སྟེ༌[^2766]དེ་ཞེས་བྱ་བ་ལ། སངས་རྒྱས་ཀྱི་ཆོས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། བྱང་ཆུབ་ཀྱི་ཕྱོགས་ལ་སོགས་པའོ། །

[Block 3207]
རྣམ་པར་སྒྲུབ་པ༌[^2767]ནི་མ་གྲུབ་པའམ། མ་སྐྱེས་པ་ལ་སྒྲུབ༌[^2768]པའམ། སྐྱེད་པར་བྱེད་པའོ། །

[Block 3208]
སློང་བ་ནི་སྐྱེས་པ་རྣམས་གོང་དུ་འཕེལ་བར་བྱེད་པ་སྟེ།[^2769] དེས་ན་ཐབས་སོ། །

[Block 3209]
ཚིག་འདི་ནི་མདོར་བསྟན་པ་སྟེ། ལྷག་མ་རྣམས་ནི་ཇི་ལྟར༌[^2770]སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་སྒྲུབ༌[^2771]ཅིང་སློང་བར་བྱེད་པའི་བཤད་པའོ། །

[Block 3210]
ཐབས་ནི་བྱང་ཆུབ་སེམས་དཔའི་དགེ་བའི་ཆོས་ཐམས་ཅད་ཉེ་བར་གཞོག་པ་ཞེས་བྱ་བ་ནི་ཐབས་ནི་ལྷ་དང་མིར་སྐྱེ་བའི་དགེ་བའི་ཆོས་རྣམས་ལ་གནས་པའམ། དེ་ལ་གོམས་པར་བྱེད་པའི་དོན་ཏོ། །

[Block 3211]
བསམ་པ་ངེས་པར་སེམས་ཞེས་བྱ་བ་ནི་སེམས་ཀྱིས༌[^2772]ཆོས་རྣམས་ལ་རྟོག་ཅིང་གཏན་ལ་འབེབས་པའི་དོན་ཏོ། །

[Block 3212]
སྦྱོར་བ་རྒྱུན་མི་འཆད་ཅེས་བྱ་བ་ནི་ལུས་དང་ངག་གིས༌[^2773]དགེ་བའི་ཆོས་ལ་རྒྱུན་མི་འཆད་པར་སྤྱོད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3213]
ལྷག་པའི་བསམ་པས་བྱེ་བྲག་ཏུ་འཕགས་པའི་ཆོས་འདོད་ཅེས་བྱ་བའི་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་ཀྱི་ཆོས་ལས་བྱེ་བྲག་ཏུ་འཕགས་པ་ཐེག་པ་ཆེན་པོའི་ཆོས་ལ༌[^2774]སེམས་ཐག་པ་ནས་དད་པའི་དོན་ཏོ། །

[Block 3214]
ཐབས་ནི་སྦྱིན་པས་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་ཅེས་བྱ་བ་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཅིག་པུས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་ནི་ཐབས་ཏེ། དེ་ལ་ཟང་ཟིང་གི་སྦྱིན་པས༌[^2775]ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའོ།[^2776] །མི་འཇིགས་པའི་སྦྱིན་པས་ནི་ཚུལ་ཁྲིམས་དང་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྫོགས་པར་བྱེད་དོ། །

[Block 3215]
ཆོས་སྦྱིན་པས་ནི་བརྩོན་འགྲུས་དང་། བསམ་གཏན་དང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་དེ། །ཚུལ་ཁྲིམས་ཀྱིས་སྐྱེ་བ་ཐམས་ཅད་འཛིན་པ་ནི་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པའི་རྣམ་པར་སྨིན་པ་མཐོ་རིས་སུ་ངེས་ཀྱང་ཐབས་ཀྱི་དབང་གིས༌[^2777]སེམས་ཅན་གྱི་དོན་སྤྱད་པའི་ཕྱིར་མཐོ་རིས་འབའ་ཞིག་ཏུ་སྐྱེ་བར་མ་ཟད་ཀྱི་སྐྱེ་བ་ཐམས་ཅད་དུ་འབྱུང་བའོ། །

[Block 3216]
ཐབས་ནི་བཟོད་པས་བྱང་ཆུབ་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་ལ། བཟོད་པ་དང་ལྡན་པས། ལུས་བཟང་བ་དང་། ངག་སྙན་པ་དང་། སེམས་དང་བར༌[^2778]འགྱུར་ཏེ། ལུས་དང་ངག་ཡིད་དང་བ་དེ་སེམས་ཅན་གཞན་གྱིས་མཐོང་ཞིང་ཐོས་ན་དད་ཅིང་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པར༌[^2779]འགྱུར་བས་ཀྱང་བྱང་ཆུབ་ཀྱི་ཕྱིར། །ལུས་དང་ངག་དང་སེམས་ཀྱི་རྒྱུན་ཅེས་བྱའོ། །

[Block 3217]
བརྩོན་འགྲུས་ཀྱི་འཇུག་པ་དང་། གནས་པ་ལ་བརྩོན་པ་ཞེས་བྱ་བ་ལ། འཇུག་པ་ལ་བརྩོན་པ་དང་། གནས་པ༌[^2780]ལ་བརྩོན་པ་ཞེས་བརྩོན་པའི་ཚིག་གཉི་ག་དང་སྦྱར་རོ། །

[Block 3218]
དེ་ལ་འཇུག་པ་ལ་བརྩོན་པ་ནི་བྱང་ཆུབ་ཀྱི་རྒྱུའི་དགེ་བའི་རྩ་བ་དང་པོ་རྩོམ་པའོ། །

[Block 3219]
གནས་པ་ལ་བརྩོན་པ་ནི་དགེ་བའི་རྩ་བ་བརྩམས་པ་མཐར་ཕྱིན་པའོ། །

[Block 3220]
བསམ་གཏན་གྱིས་བསམ་གཏན་ལས་ཕྱིར་ལྡོག་པ་ཤེས་པ་ནི་བསམ་གཏན་གྱི༌[^2781]ཁམས་གོང་མ་དག་ཏུ་སྐྱེས་ཀྱང་། ཐབས་ཀྱི་དབང་གིས་འདོད་པའི་ཁམས་སུ་སྐྱེ་བ་ལེན་པར་བྱེད་པའོ། །

[Block 3221]
ཤེས་རབ་ཀྱིས་འདུས་མ་བྱས་སྤོང་བ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱིས༌[^2782]འདུས་མ་བྱས་རྟོགས༌[^2783]ཀྱང་། ཐབས་ཀྱིས་ཟིན་པས་འདུས་མ་བྱས་ཀྱི༌[^2784]དབྱིངས་ལ་མི་གནས་ཤིང་འདུས་བྱས་ཀྱི༌[^2785]བྱ་བ་རྣམས་ཀྱང་བྱེད་པའོ། །

[Block 3222]
བྱམས་པས་དཔུང་གཉེན་མེད་པ་རྣམས་ཀྱི་སྐྱབས་ཞེས་བྱ་བ་ནི་ངན་སོང་གི་སྡུག་བསྔལ་མྱོང་བ་དང་རྣམ་པར་གྲོལ་བ་མཐོང་བ་ནི་དཔུང་གཉེན་མེད་པ་སྟེ། དེ་དག་སྐྱེ་འགྲོ༌[^2786]དང་རྣམ་པར་གྲོལ་བའི་བདེ་བ་ཐོབ་པའི་སྐྱབས་བྱེད་པ་ནི་ཐབས་སོ། །

[Block 3223]
སྙིང་རྗེས་འཁོར་བ་ལ་མི་སྨོད་ཅེས་བྱ་བ་ལ། སེམས་ཅན་གྱི་སྡུག་བསྔལ་སེལ་བར་བྱེད་པའི་སྙིང་རྗེས་འཁོར་བ་སྡུག་བསྔལ་གྱི་གནས་ཡིན་ཡང་སྨོད་པར་མི་བྱེད་པ་ནི་ཐབས་སོ། །

[Block 3224]
དགའ་བས་དགའ་བ་དང་མི་དགའ་བ་ལ༌[^2787]མི་འབྱེད་པ་ཞེས་བྱ་བ་ལ། ཆོས་ཀྱི་ཀུན་དགའ་ལ་དགའ་བ་དང་། འཁོར་བའི་རང་བཞིན་སྡུག་བསྔལ་ཞིང་མི་དགའ་བ་ཅན་ཡིན་ཡང་ཐབས་ཀྱི་དབང་གིས་དེ་ལ་ཇི་མི་སྙམ་པ་ནི་ཐབས་སོ། །

[Block 3225]
བཏང་སྙོམས་ཀྱིས༌[^2788]དགེ་བའི་རྩ་བ་དང་། ཚོགས་ཐམས་ཅད་འཕེལ་ཞེས་བྱ་བ་ལ།
--- END BLOCKS ---
