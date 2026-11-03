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
[Block 3326]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་འདི་སྐད་སྨྲས་སོ་ཞེས་པའི་བར་དུ་ནི་ངེས་པའི་དོན་སྟོན་པའི་དཔེའོ། །

[Block 3327]
མདོ་ལས་སྐྱེས་བུ་ཁྱོད་ཟས་དང་སྐོམ་ཞེས་པ་ནས་ཆོག་པར་འཛིན་ཏམ་ཞེས་པའི་བར་དུ་ནི་ངེས་པའི་དོན་སྟོན་པ་སྟེ། འདོད་པ་ཞེས་པ་ནི་བདེ་བ་སྡུག་པ༌[^2814]རྣམ་པ་ལྔ་སྟེ། རང་བཞིན་བདེ་བ་དང་། རྒྱུ་བདེ་བ་དང་། སྤོང་བ་བདེ་བ་དང་། ཉོན་མོངས་པའི་གཉེན་པོས་བདེ་བ་དང་། གནོད་པ་མེད་པའི་བདེ་བ་སྟེ། དེ་བཞིན་གཤེགས་པའི་ཆོས་ཀྱི་དབྱིངས་རྣམ་པར་དག་པ་དང་། ཡེ་ཤེས་བཞི་དང་ལྔ་ཡང་བསྒྲུབ་པར་བྱ་བའི་བདེ་བ་ཞེས་གདགས་པ་དང་། ཟག་པ་མེད་པའི་ཕུང་པོ་ལྔ་ཡང་བདེ་བར་བྱ་བ་ཉིད་པས་བདེ་བ་ཞེས་གདགས་སོ། །

[Block 3328]
མདོ་ལས་ཀྱི༌[^2815]སྐྱེས་བུ་ཁྱོད་ཅེས་པ་ནས་བྱ་བ་ཐམས་ཅད་བྱོས་ཤིག་ཅེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོ་ལ་ཞུགས་པས་ཡོན་ཏན་ཐམས་ཅད་རྫོགས་ཏེ། ཇི་ལྟར་ཡིད་བཞིན་གྱི་རིན་པོ་ཆེ་བསྒྱུར་བ་བཞིན་ཞེས་པར་སྦྱར་རོ། །

[Block 3329 [HEADING]]
###### དཔེ་དང་ངེས་པའི་དོན་དུ་སྦྱར་བ། ^4-8-8-4-3-0

[Block 3330]
མདོ་ལས་དེ་བཞིན་དུ་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་སེམས་བསྐྱེད་པར་གྱུར་པ་ཞེས་པའི་བར་དུ་ནི་དཔེ་དང་ངེས་པའི་དོན་དུ་སྦྱར་བ་སྟེ། སྦྱོར་བའི་ཡོན་ཏན་དང་སྦྱར་རོ། །

[Block 3331]
མདོ་ལས་དེ་བདག༌[^2816]གིས་མ་རྟོགས་མ་ཆུད་པ་ཞེས་པ་ནི༌[^2817]སེམས་བསྐྱེད་པ་ལས་ལྡོག་པ་བསྟན་ཏོ། །

[Block 3332]
མདོ་ལས་བཅོམ་ལྡན་འདས་དེའི་སླད་དུ་ཞེས་པ་ནས་རྟག་ཏུ་མ་ཉམས་པ་ཞེས་པའི་བར་དུ་ནི་འཕགས་པ་དགྲ་བཅོམ་པ་དེ་སྤྱོད་པ་དཀའ་བའི༌[^2818]རྣམས་ཆུད་ཟོས་པ་དང་ཐེག་པ་ཆེན་པོར་སྨོན་ལམ༌[^2819]བཏབ་པས་ཡེ་ཤེས་ཆུང་ངུས་ཆོག་པར་འཛིན་ཞེས་པའོ། །

[Block 3333]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་བདག་ཞེས༌[^2820]པ་ནས་ཐབས་མཁས་པ་སྟེ་ཞེས་པའི་བར་དུ་ནི་ངེས་པའི་དོན་དང་སྦྱར་བ་མྱ་ངན་ལས་འདས་པའི་མཚན་ཉིད་བསྟན་པའོ། །

[Block 3334 [HEADING]]
###### ཚིགས་སུ་བཅད་པ། ^4-8-8-4-4-0

[Block 3335]
མདོ་ལས་དེ་ལྟར་བཅོམ་ལྡན་འདས་ཏེ་ཞེས་པ་ནས་ཆོག་པར་འཛིན་པ་བདེ་གཤེགས་བསྟན་པ༌[^2821]ཞེས་པའི་བར་དུ་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་བཅུ་གསུམ་གྱིས་ནི་ཉེས་པར་གནོད་བཀུར་བ་དང་། ཤེས་པ་སྐྱེས་པ་བསྟན་ཏོ། །

[Block 3336]
མདོ་ལས་ཇི་ལྟ་བུར་ན༌[^2822]སྐྱེས་བུ་ལ་ལ་ཞིག་ཞེས༌[^2823]པ་ནས་འདོད་པའི་ཡོན་ཏན་ལྔ་དང་ཤིན་ཏུ་ལྡན༌[^2824]ཞེས་པའི་བར་དུ་ནི་དཔེ་དེ་ཡང༌[^2825]

[Block 3337]
དང་པོ་སེམས་བསྐྱེད་པའི་དཔེ་དང་། བར་དུ་སེམས་ནུར་བའི་དཔེའོ། །

[Block 3338]
སྟོང་པ་ཉིད་བསྟན་པ་དང་། སྟོང་པ་དེ་ཆུད་པས་བླ་ན་མེད་པའི་བདེ་བ་ཆེན་པོ་དང་ལྡན་པའི་དཔེ་བསྟན་ཏོ། །

[Block 3339]
མདོ་ལས།

[Block 3340]
དེ་བཞིན་བཅོམ་ལྡན༌[^2826]བདག་ཅག་འདི་ལྟ་བུར། །ཞེས་པ་ནས། བདག་ཅག་མྱ་ངན༌[^2827]འདས་ཙམ་མཆོག་ཏུ་གཟུང་། །ཞེས་པའི་བར་དུ་ནི་སྔར་ནི་དྲང་བའི་དོན་བསྟན་པ་ལ་ཡང་སྤོང་བའི་ཡོན་ཏན་དང་། བར་དུ་ལྡོག་པའི་དཔེ་བསྟན་པའོ། །

[Block 3341]
མདོ་ལས།

[Block 3342]
བླ་མེད་དེ་ནི་མི་འདོད་མི་ཚོལ་ལོ། །ཞེས་པ་ནས། མགོན་པོ་གཅིག་ལ་གཅིག་ལུང་བསྟན་པའི་ཕྱིར། །ཞེས་པའི་བར་དུ་ནི་དྲང་བ་དང་ངེས་པའི་དོན་བསྡུས་པ་སྟེ་ཅི་རིགས་པར་ཆུད་པར་བྱའོ།། །།

[Block 3343 [HEADING]]
### དགེ་སློང་ཉིས་སྟོང་ལུང་སྟོན་པའི་ལེའུ། ^4-9-0

[Block 3344]
འདི་མན་ཆད་དགེ་སློང་ཉིས་སྟོང་ལུང་སྟོན་པའི་ལེའུ་འཆད་དེ[^2828]། དེ་ཡང་རྣམ་པ་གཉིས་སུ་དབྱེའོ། །

[Block 3345]
ལེའུ་འདི་ཅི་ལས་བཏགས་པའི་གཏན་ཚིགས་དང་། ལེའུ་འདིའི་མིང་བཤད་པའོ། །

[Block 3346 [HEADING]]
#### གཏན་ཚིགས། ^4-9-1-0

[Block 3347]
དེའི་གཏན་ཚིགས་ཀྱང་རྣམ་པ་གཉིས་ཏེ། དབང་པོ་རྣོན་པོ་རྣམས་སྔར་ལུང་བསྟན་པའི་རྗེས་ལ་འདི་དག་ལུང་སྟོན་པར་འོས་པ་དང་། ལུང་བསྟན་པ་རྣམ་པ་བཞི་ལས་ལུང་བསྟན་པ་ཐ་མ་དང་སྦྱར་བའི་ཕྱིར་ལེའུ་འདི་བསྟན་ཏོ། །

[Block 3348 [HEADING]]
#### མིང་བཤད་པ། ^4-9-2-0

[Block 3349]
མིང་བཤད་པ་ནི་སློབ་པ་དང་མི་སློབ་པ༌[^2829]རྣམས་འདིའི་ནང་དུ་ལུང་སྟོན་པའི་ཕྱིར་དགེ་སློང་གཞན་ཉིས་སྟོང་ལུང་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3350 [HEADING]]
#### འཁོར་རེ་བའི་སེམས་སྐྱེས་པ། ^4-9-3-0

[Block 3351]
མདོ་ལས།

[Block 3352]
དེ་ནས་ཚེ་དང་ལྡན་པ་དགའ་བོ༌[^2830]ཞེས་པ་ནས་རྣམ་པར་སེམས་ཏེ་སྨོན༌[^2831]ཞེས་པའི་བར་དུ་ནི་རྣམ་པ་གཉིས་ཏེ། འཁོར་རེ་བའི་སེམས་སྐྱེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་རེ་བ་སྐོང༌[^2832]བའོ། །

[Block 3353]
འཁོར་རེ་བ་ཡང་སྔར་ནི་སྐྱེས་བུ་གཉིས་ཀྱིས་གསོལ། དེའི་འོག་ཏུ་ནི་འཁོར་ཉིས་སྟོང་གིས༌[^2833]གསོལ་བ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 3354]
མདོ་ལས་སྟན་ལས་ལངས་ཏེ་ཞེས་པ་ནས་སྐབས་དབྱེར་གསོལ་ཞེས་པའི་བར་དུ་ནི་སྐྱེས་བུ་དེ་གཉིས་ཀྱིས༌[^2834]ལུང་བསྟན་པར་གསོལ་བའོ། །

[Block 3355]
མདོ་ལས་བཅོམ་ལྡན་འདས་བདག་གི༌[^2835]ཞེས་པ་ནས་བཅོམ་ལྡན་འདས་ལ་བལྟ་ཞིང་འདུག་སྟེ་ཞེས་པའི་བར་དུ་ནི་ལུང་བསྟན་པར་གསོལ་པའི་རིགས་པ༌[^2836]དང་ཚུལ་གསོལ་བའོ། །

[Block 3356 [HEADING]]
#### བཅོམ་ལྡན་འདས་ཀྱིས་རེ་བ་སྐོང་བ། ^4-9-4-0

[Block 3357 [HEADING]]
##### དགའ་པོ་ལུང་བསྟན་པ། ^4-9-4-1-0

[Block 3358]
མདོ་ལས་འདི་ཉིད་སེམས་ཤིང་རྣམ་པར་སེམས་ཞེས་པ་ནས་འཇིག་རྟེན་དུ་བྱུང་སྟེ་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2837]དངོས་སུ་ལུང་བསྟན་པ་སྟེ། དེ་ཡང་སྔར་ནི་དགའ་པོ་ལུང་བསྟན། དེའི་འོག་ཏུ་ནི་སྒྲ་གཅན་འཛིན་ལུང་བསྟན། དེའི་འོག་ཏུ་ནི་དགེ་སློང་ཉིས་སྟོང་ལུང་བསྟན་དང་པོ་ལ་ཡང་རྣམ་པ་བརྒྱད་དུ་དབྱེ་སྟེ། སངས་རྒྱས་ཀྱི་མཚན་དང་། སྔོན་གྱི་སྤྱོད་པ་བསྟན་པ་དང་། སེམས་ཅན་ལ་ཕན་འདོགས་པ་དང་ཡུལ་གྱི་མིང་དང་། ཞིང་གི་རྒྱན་དང་། བསྐལ་པའི་མིང་དང་། ཚེའི་ཚད་དང་། མངོན་པར་བསྟོད་པའོ། །

[Block 3359]
མདོ་ལས་སངས་རྒྱས་བྱེ་བ་ཕྲག་ཞེས༌[^2838]པ་ནས། ཁྲག་ཁྲིག་བརྒྱ་སྟོང་གི་བསྔགས་པ་བརྗོད་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་གོང་དུ་སྨོས་པའི༌[^2839]བརྒྱད་པོ་དང་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 3360]
མདོ་ལས་དེའི་དུས་ན་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2840]ཞེས་པ་ནས་མ་འོངས་པའི༌[^2841]དུས་ཀྱི་ཚེ་ལ་རྒྱལ་བར་འགྱུར་ཞེས་པའི་བར་དུ་འདིས༌[^2842]རྒྱུ་ལས་དགོངས་ཏེ་ལུང་བསྟན་པའོ། །

[Block 3361]
མདོ་ལས།

[Block 3362]
བདེ་གཤེགས་བྱེ་བ་བརྒྱད་ཅུ་མཆོད་བྱས་ན།[^2843] །ཞེས་པ་ནས། སངས་རྒྱས་བྱང་ཆུབ་འདི་ལ་རྒྱུ་ཡང་སྐྱེད།[^2844] །ཅེས་པའི་བར་དུ༌[^2845]འབྲས་བུ་ལས་དགོངས་ཏེ་ལུང་བསྟན་པ་ལ་མཚན་དང་། ཞིང་གི་རྒྱན་དང་། ཡུལ་གྱི་མིང་དང་། ཕན་འདོགས་པ་དང་། རྗེས་སུ་བསྔགས་པ་དང་། སྐུ་ཚེའི་ཚད་དང་། སེམས་ཅན་ལ་ཕན་འདོགས་པ་དང་། དེ་བཞིན་གཤེགས་པའི་སྤྱོད་པའི་རྒྱུ་སྒྲུབ་པ་སྟེ། འདི་ནི་ཚིག་དང་པོ་དང་སྦྱར་རོ། །

[Block 3363]
མདོ་ལས་དེ་ནས་འཁོར་དེ་ན་ཞེས་པ་ནས་ཅིའི་རྐྱེན་དུ་འགྱུར་ཞེས་པའི་བར་དུ་ནི་འཁོར་གྱི་ཐེ་ཚོམ་མོ། །

[Block 3364]
མདོ་ལས།

[Block 3365]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་དེ་ཞེས་པའི་བར་དུ༌[^2846]ནི་སྔོན་གྱི༌[^2847]རྒྱུ་བསྟན་པ་དང་། དེའི་འོག་ཏུ་འཕྲལ་གྱི་སྤྱོད་པ་བསྟན་པ་དང་། བསྡུ་སྟེ༌[^2848]ལུང་སྟོན་པ་ལ༌[^2849]འདི་ནི་དང་པོའོ། །
--- END BLOCKS ---
