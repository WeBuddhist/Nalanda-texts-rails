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
[Block 3291]
དེ་འདྲ་བ་ཡི་དམ་པའི་ཞིང་དུ་འགྱུར། །ཞེས་པ་ནས། འདི་ནི་ཅུང་ཟད་ཙམ་ཞིག་བཤད་པ་ཡིན། །ཞེས་པའི་བར་དུ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ས་བརྒྱད་པ༌[^2792]ཡན་ཆད་ནས་རྫོགས་ལོངས་སྤྱོད་པའི་སའི༌[^2793]བར་དུ་ནི་ཡིན་པར་སྦྱར་རོ། །

[Block 3292 [HEADING]]
#### དགེ་སློང་ལྔ་བརྒྱ་ལུང་བསྟན་པ། ^4-8-8-0

[Block 3293]
མདོ་ལས།

[Block 3294 [HEADING]]
##### སེམས་ཀྱི་རེ་བ། ^4-8-8-1-0

[Block 3295]
དེ་ནི་དབང་དུ་གྱུར་པ་ཞེས་པ་ནས་རྨད་དུ་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་དགེ་སློང་ལྔ་བརྒྱ་ལུང་བསྟན་པ་སྟེ། སེམས་ཀྱི་རེ་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་གནང་བ་དང་། མངོན་དུ་ལུང་བསྟན་པ་དང་། རྗེས་སུ་འཛིན་པའོ། །

[Block 3296 [HEADING]]
##### བཅོམ་ལྡན་འདས་ཀྱིས་གནང་བ། ^4-8-8-2-0

[Block 3297]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས། ལུང་བསྟན་ཏོ་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2794]གནང་བ་དང་སྦྱར་རོ། །

[Block 3298 [HEADING]]
##### མངོན་དུ་ལུང་བསྟན་པ། ^4-8-8-3-0

[Block 3299 [HEADING]]
###### ཚིག་རྐྱང་པ། ^4-8-8-3-1-0

[Block 3300]
མདོ་ལས་དེ་ལ་འོད་སྲུངས་ཆེན་པོ་ཞེས་པ་ནས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཏེ་ཞེས་པའི་བར་དུ༌[^2795]མངོན་དུ༌[^2796]བསྟན་པ་སྟེ།[^2797] དེ་ཡང་ཚིག་རྐྱང་པ་དང་ཚིགས་སུ་བཅད་པར་དབྱེའོ། །

[Block 3301]
མདོ་ལས་འོད་སྲུངས་དེ་ནི་ཞེས་པ་ནས་དབང་དུ་གྱུར་པ་ལྔ་བརྒྱའོ་ཞེས་པའི་བར་དུ་ནི་དགེ་སློང་ལྔ་བརྒྱ་ལུང་བསྟན་པ་སྟེ། དེ་ལ་ཁ་ཅིག་ན་རེ་ལྔ་བརྒྱ་པོ་འདི་སྟོང་ཉིས་བརྒྱའི་གྲངས་སུ་གཏོགས་ཞེས་ཀྱང་ཟེར། ལོགས་ཤིག་ཏུ་སྟོན་པ་ཡང་ཡོད་དོ། །

[Block 3302 [HEADING]]
###### ཚིགས་སུ་བཅད་པ། ^4-8-8-3-2-0

[Block 3303]
མདོ་ལས།

[Block 3304]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ། །ཞེས་པ་ནས། བྱང་ཆུབ་དམ་པ་མཆོག༌[^2798]ཀྱང་སྟོན་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་མངོན་དུ༌[^2799]བསྟན་པ་སྟེ། དེ་ལ་དང་པོ༌[^2800]ཚིག་དྲུག་གིས་ནི་འཕགས་པ་ཅང་ཤེས་ཀྱི་ཕྱིར་གླེངས། དེའི་འོག་མས་ནི་གཞན་གླེང་སྟེ། འདི་ནི་དང་པོའི༌[^2801]རང་བཞིན་བསྟན་པའོ། །

[Block 3305]
མདོ་ལས།

[Block 3306]
བྱང་ཆུབ་སེམས་དཔའ་བརྩོན་པ་རྣམས། །ཞེས་པ་ནས། ལྷ་དང་མི་རྣམས་སྡུག་ཅིང་བསམ་པར་འོས།[^2802] །ཞེས་པའི་བར་དུ་ནི་ཞིང་དང་། འཁོར་དང་། ཚེའི་ཚད་བསྟན་པའོ། །

[Block 3307]
མདོ་ལས།

[Block 3308]
རྒྱལ་བ་དེ་དང་མི་མཐུན་འགྱུར་བ་ནི། །ཞེས་པ་ནས། ཇི་ལྟར་འཇིག་རྟེན་ཐམས་ཅད་ངས་བསྟན་བཞིན། །ཞེས་པའི་བར་དུ་ནི་དགེ་སློང་ལྔ་བརྒྱ་ལུང་བསྟན་པའི་རང་བཞིན་དུ༌[^2803]བསྡུས་པ་བསྟན་པའོ། །

[Block 3309]
མདོ་ལས།

[Block 3310]
དེ་ལྟར་དེ་དག་འོད་སྲུངས་ཁྱོད་ཀྱིས་དེང་། །ཞེས་པ་ནས། དེ་བཞིན་སྒོའོ༌[^2804]ཞེས་པའི་བར་དུ་ནི་འཁོར་འདིར་མ་འདུས་པ་རྣམས་བརྒྱུད་དེ་ལུང་བསྟན་པའོ། །

[Block 3311 [HEADING]]
##### རྗེས་སུ་འཛིན་པ། ^4-8-8-4-0

[Block 3312]
མདོ་ལས་དེ་ནས་དགྲ་བཅོམ་པ་ལྔ་བརྒྱ་པོ་དེ་དག་ཅེས་པ་ནས་ཉེས་པ་དེ་དག་བདག་ཅག་གིས༌[^2805]བཤགས་སོ་ཞེས་པའི་བར་དུ་ནི་དགའ་བའི་སེམས་ཀྱིས་བཀའ་ཡང་དག་པ་མནོས་པ་དང་སྔར་སེམས་ཞུམ་པ་གནོད་པ་གླེངས་པའོ། །

[Block 3313]
མདོ་ལས་བཅོམ་ལྡན་འདས་འདི༌[^2806]ནི་ཞེས་པ་ནས་ཆུང་ངུས་ཆོག་གོ་སྙམ་ཞེས་པའི་བར་དུ་ནི་སྔར་ནི་མོས་པ་ཆུང་བས་གླེངས། དེའི་འོག་ཏུ་ནི་ཆུང་བ་སྟོན་པའོ། །

[Block 3314 [HEADING]]
###### དྲང་བའི་དོན་གྱི་དཔེ། ^4-8-8-4-1-0

[Block 3315]
མདོ་ལས།

[Block 3316]
དེ་འདི་ལྟ་སྟེ་ཞེས་པ་ནས་གོས་ཀྱི་ཐ་མར་ཕུར༌[^2807]ཏོ་ཞེས་པའི་བར་དུ༌[^2808]འདིས་ནི་དྲང་བའི་དོན་གྱི་དཔེ་བཤད་དོ།[^2809] །དེ་ལ་ཉམ་ང་བ་ལ་དབྲལ་བ་མི་དེ་མྱོས་པར་གྱུར་པ་དང་། ཡུལ་གཞན་དུ་སོང་བ་དང་། དུབ་པ་ལྟ་བར་གྱུར་པ་སྟེ། དེ་ནི་དང་པོ་དང་སྦྱར་རོ། །

[Block 3317]
ཁྱིམ་དུ་ཕྱིན་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོའི་བསྟན༌[^2810]དང་ཕྲད་པའོ། །

[Block 3318]
ར་རོ་ཞེས་པ་ནི་མ་རིག་པ་མ་སྤངས་ཞེས་པའོ། །

[Block 3319]
ཉལ་བ་ནི་འཁོར་བ་ན་གནས་པའོ། །

[Block 3320]
རིན་པོ་ཆེ་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོ་སྟེ། ཇི་ལྟར་ཡིད་བཞིན་གྱི་རིན་པོ་ཆེ་དགོས་པ་སྣ་ཚོགས་འབྱུང་བ་བཞིན་ཐེག་པ་གཅིག་པུ་ལ་ཕྱོགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡིད་བཞིན་དུ་འགྲུབ་ཅེས་པའོ། །

[Block 3321]
གོས་ཀྱི་མཐར་ཕུར༌[^2811]ཞེས་པ་ནི་སྔོན་གྱི་ཐེག་པ་ཆེན་པོ་པའི་བཤེས་གཉེན་དང་ཕྲད་པའི་བག་ཆགས་སོ། །

[Block 3322]
མདོ་ལས།

[Block 3323]
དེ་ནས་བཅོམ་ལྡན་འདས་དེ་སྐྱེས་བུ་ཞེས་པ་ནས་དེ༌[^2812]མགུ་རབ་ཏུ་དགའོ༌[^2813]ཞེས་པའི་བར་དུ་ནི་སེམས་ནུར་བའི་རྣམས་སྤྲུལ་པའི་གྲོང་ཁྱེར་བསྟན་པ་བཞིན་གཞན་དུ་སོང་སྟེ་ཞེས་པ་ནི་སྤྱོད་པ་གཞན་ལ་ཞུགས་པའོ། །

[Block 3324]
ཐེག་པ་ཆེན་པོའི་དོན་དང་ཆོས་ཀྱི་རོས་ཕོངས་པ་ནི་ཁ་ཟས་དང་གོས་ཚོལ་བའོ། །

[Block 3325 [HEADING]]
###### ངེས་པའི་དོན་སྟོན་པའི་དཔེ། ^4-8-8-4-2-0

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
--- END BLOCKS ---
