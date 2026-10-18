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
[Block 3256]
མདོ་ལས་དགེ་སློང་རྣམས་འདི་ཡིད་ལ་ཇི་སྙམ་དུ་སེམས་ཞེས་པ་ནས་སངས་རྒྱས་བདུན་པོ་དེ་དག་གི་ཐ་མ་ནི་ང་ཡིན་དེ༌[^2757]དག་གི་ཡང་ཆོས་འཆད་པའི་མཆོག་ཏུ་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་ཡོན་ཏན་གྱི་ཁྱད་པར་དེ་དག་ལ་ཡང་དེ་བཞིན་གཤེགས་པའི་བསྟན་པ་འཛིན་པ་དང་། འཁོར་དགའ་ཞིང་ཕན་པ་བསྐྱེད་པ༌[^2758]དང་། དེ་བཞིན་གཤེགས་པའི་ཆོས་སྒྲོགས་པ་ལ་མཁས་པ་དང་། ཚངས་པ་མཚུངས་པར༌[^2759]སྤྱོད་པ་རྣམས་ལ་ཕན་བཏགས་པ༌[^2760]དང་། སྤོབས་པ་ཁྱད་པར་ཅན་དུ་གྱུར་པའོ། །

[Block 3257]
སྟོང་པ་ཉིད་ཀྱིས༌[^2761]འགྲོས་སུ་ཞེས་པ་ནི་དགེ་བའི་བློ་གྲོས་ཀྱི་ས་ལ་གནས་པ་སྟེ། ཐེ་ཚོམ་ཐམས་ཅད་སྤངས་པའོ། །

[Block 3258]
ཡོངས་སུ་སྨིན་པར་བྱས་སོ་ཞེས་པ་ནི་ཆོས་ཀྱི་སྤྲིན་གྱི་ས་ལ་གནས་པས་སེམས་ཅན་མང་པོ་ལ་ཕན་ཐོགས་ཞེས་པའོ། །

[Block 3259]
སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་བྱེད་པ་ནི། ལྷག་མ་མ་ལུས་པའི་མྱ་ངན་ལས་འདའ་བ་རྣམས་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་དེ། ཐེག་པ་ཆེན་པོ་ལ་བཀོད་པས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་བསྒྱུར་ཏོ། །

[Block 3260]
བྱང་ཆུབ་ཏུ་བསྒྱུར་བ་དེ་ཉིད་གཞན་གྱི་དོན་བྱེད་པ་སྟེ། སངས་རྒྱས་ཀྱི༌[^2762]མཛད་པ་དེས་ཞིང་བརྒྱན༌[^2763]ཞེས་པའོ། །

[Block 3261]
མདོ་ལས་དགེ་སློང་རྣམས་བསྐལ་པ་བཟང་པོ་འདི་ལ་ཞེས་པ་ནས་ཡོངས་སུ་སྨིན་པར་བྱེད་དོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པའི་ཆོས་འཛིན་པ་དང་། བྱང་ཆུབ་སེམས་དཔའི༌[^2764]སྤྱོད་པ་བསྟན་པའོ། །

[Block 3262 [HEADING]]
#### ལུང་བསྟན་པ། ^4-8-6-0

[Block 3263]
མདོ་ལས་རྟག་ཏུ་རྒྱུན་མི་གཅོད་དོ་ཞེས་པ་ནས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཏེ་ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་གྱི་དོན་བྱེད་པ་དང་། བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པའི་ལམ་བསྟན་པ་དང་། དངོས༌[^2765]འབྲས་བུ་མཚོན་ཏེ་ལུང་བསྟན་པའོ། །

[Block 3264]
མདོ་ལས་སངས་རྒྱས་ཀྱི་ཞིང་འདིར་ཞེས་པ་ནས་ཡོངས་སུ་གང་བར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པའི་ཞིང་གི་རྒྱན་སྟོན་ཏེ། རྒྱན་དེ་ཡང་རིན་པོ་ཆེ་ལས་བྱས་པ་དང་མཉམ་པ་ཞེས་པར་བསྡུའོ། །

[Block 3265]
མདོ་ལས་ལྷའི་གཞལ་མེད་ཁང་དང་ཞེས་པ་ནས་བུད་མེད་ཀྱང་མེད་དེ་ཞེས་པའི་བར་དུ་ནི་དེ་ན་དགེ་བ་འབའ་ཞིག་ཅེས་པའི་དོན་ཏེ།[^2766] ལྷ་དང་ཉེ་བ་གཅིག་གིས་གཅིག༌[^2767]མཐོང་བ། ངན་སོང་གསུམ་མེད་པ། འདོད་ཆགས་ཀྱི་གཞི་མེད་པས་རྫུས༌[^2768]ཏེ་སྐྱེ་བ་ཤ་སྟག་གོ༌[^2769]བར་སྦྱར་རོ། །

[Block 3266]
མདོ་ལས་རྫུས༌[^2770]ཏེ་སྐྱེ་བ་ཚངས་པར་སྤྱོད་པ་ཞེས་པ་ནས་ལུས་བརྒྱན་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་ལྷ་དང་མིའི་མཚན་ཉིད་ནི་རྫུ་འཕྲུལ་དང་ལྡན་པ། ལུས་འོད་ཅན་ནམ་མཁའ་ལ་འགྲོ་བ། ཡིད་བརྟན་པ། བརྩོན་འགྲུས་དང་ལྡན་པ། ཤེས་རབ་ཅན་མཚན་དང་ལྡན་པ་ཞེས་དབྱེའོ། །

[Block 3267]
མདོ་ལས་དགེ་སློང་རྣམས་ཡང་དེའི་དུས་ན་ཞེས་པ་ནས་བསམ་གཏན་གྱི་དགའ་བའི་ཟས་སོ་ཞེས་པའི་བར་དུ་ནི༌[^2771]ལུས་ཅིས་བཟུང་བའི༌[^2772]དོན་སྟོན་ཏེ། མདོ༌[^2773]ལས་ཟས་རྣམ་པ་བཞི་དང་། དགུ་དག་ཏུ་གསུངས་པ་ལ༌[^2774]སྤྱིར་རྣམ་པ་གཉིས་ཏེ། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཟས་སམ། ཟག་པ་དང་བཅས་པ་དང་། ཟག་པ་མེད་པའི་ཟས་དང་།[^2775] འཇིག་རྟེན་གྱི་ཟས་ནི་ཁམ་གྱི་ཟས་དང་། རེག་པའི་ཟས་དང་། སེམས་པའི་ཟས་དང་། རྣམ་པར་ཤེས་པའི་ཟས་སོ། །

[Block 3268]
འཇིག་རྟེན་ལས་འདས་པའི་ཟས་ནི་བསམ་གཏན་གྱི་ཟས་དང་། སྨོན་ལམ་གྱི་ཟས་དང་། དྲན་པའི་ཟས་དང་། རྣམ་པར་ཐར་པ་བརྒྱད་ཀྱི་ཟས་དང་། དགའ་བའི་ཟས་ཏེ། ཟས་དེ་ལྔ་ལས་གཙོར་སྨོས་པ་འདི་གཉིས་ཀྱི་ཚེ་འདིས་འཛིན་པའི་དོན་ཏོ། །

[Block 3269]
མདོ་ལས།

[Block 3270]
དེའི་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་པ་ནས་བསམ་གཏན་པ་ཤ་སྟག་གོ་ཞེས་པའི་བར་དུ་འདིས༌[^2776]ནི་བྱང་ཆུབ་སེམས་དཔའ་ཉན་ཐོས་རྣམས་ཀྱི་འཁོར་ཏེ། ཡོན་ཏན་གསུམ༌[^2777]དང་ལྡན་པ་ཤ་སྟག་དང་སྦྱར་རོ། །

[Block 3271]
མདོ་ལས་སངས་རྒྱས་ཀྱི་ཞིང་དེ་དེ་ལྟ་བུར་ཚད་མེད་པའི་ཡོན་ཏན་དང་ལྡན་པར་འགྱུར་རོ་ཞེས་པ་ནས་ཇི་ལྟར་བྱང་ཆུབ་སྤྱོད་པ་འདི་སྤྱད་པ་ཞེས་པའི་བར་དུ་ནི་སངས་རྒྱས་ཀྱི་ཞིང་གི་རྒྱན་གྱི་དོན༌[^2778]བསྡུས་པའོ། །

[Block 3272]
བསྐལ་པ་ནི་ཞེས་པ་ནས། ཡང་སྟོན་པ་འདི་སྐད་གསུང་ངོ་ཞེས་པའི་བར་དུ་ནི། བསྐལ་པ་དང་ཞིང་དང་། སྐུ་ཚེའི་ཚད་དང་། མཆོད་རྟེན་བསྟན་པའོ། །

[Block 3273 [HEADING]]
#### ཚིགས་བཅད། ^4-8-7-0

[Block 3274]
མདོ་ལས།

[Block 3275 [HEADING]]
##### དེ་བཞིན་གཤེགས་པས་གླེངས་པ། ^4-8-7-1-0

[Block 3276]
དགེ་སློང་དོན་འདི་ང་ལ་སྟོན། །ཞེས་པ་ནས། བྱང་ཆུབ་སེམས་དཔའ་མང་པོ་སྨིན་པར་བྱེད། །ཅེས་པའི་བར༌[^2779]དུ་ནི་ཚིགས་བཅད་ཉི་ཤུ་རྩ་ཕྱེད་དང་གཉིས་སུ་དབྱེ་སྟེ། དང་པོའི་ཚིག་བཅུ་གཉིས་ཀྱིས་ནི་དེ་བཞིན་གཤེགས་པས་གླེངས་པ། ཚིག་དགུས་ནི་སྔོན་དུ༌[^2780]ལུང་བསྟན་པ། ཚིག་གོང་མ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཚིག་བདུན་གྱིས་ནི་ད་ལྟར་གྱི་ཡོན་ཏན་བསྟན། ཚིག་ལྔས་ནི་ཕྱི་མའི་ཡོན་ཏན་བསྟན་པའོ། །

[Block 3277]
མདོ་ལས་འདི་སྐད་སྨྲས་པ་བདག་ཅག་ཉན་ཐོས་ཞེས་པ་ནས་སེམས་ཅན་ལྟ་བ༌[^2781]ལ་ཆགས་པ་རིག་པས་ན་ཞེས་པའི་བར་དུ་ནི་ཉན་ཐོས་པའི་གནས་དེ་བཞིན་གཤེགས་པའི་ས་ལས་རིང་བ་དང་། སེམས་ཅན་གྱི་དོན་བྱེད་པ་ཆུང་བ་དང་། གནས་དང་ཞིང་ཆུང་ངུ་ན་དག་པར་སྟོན་པའོ།[^2782]

[Block 3278]
།མདོ་ལས།

[Block 3279]
དེ་ཡི་བསྟན་པ༌[^2783]རྣམས་ལ་ཉེ་བར་གནས། །ཞེས་པ་ནས། མི་མཁས་མི་རྣམས་ཤིན་ཏུ་མྱོས་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་བསྡུས་པའོ། །

[Block 3280]
མདོ་ལས།

[Block 3281]
དེ་ཡི་སྤྱོད་པ་ཐམས་ཅད་རབ་བསྟན་པ། །ཞེས་པ་ནས། མང་དུ་ཐོས་ཤིང་འཇིགས་མེད་སྣ་ཚོགས་འཆད། །ཅེས་པའི་བར་དུ་འདི་ནི་འདས་པའི་དུས་ཀྱི་ཡོན་ཏན་བཅུ་སྨོས་པ་ལ་ཚིག་ལྷུག་པ་ལས་མ་བྱུང་བ་ཆོས་སྨྲ་བ་ཁྱད་པར་དུ་འཕགས་པ། མང་དུ་ཐོས་པ། ཤེས་རབ་དང་ལྡན་པ་འདིར་སྨོས་སོ། །

[Block 3282]
མདོ་ལས།

[Block 3283]
རྟག་ཏུ་མི་སྐྱོ༌[^2784]ཡང་དགའ་རབ་ཏུ༌[^2785]བྱེད། །ཅེས་པ་ནས། བདག་གི་ཞིང་མཆོག་རྣམ་པར་དག་པར་བྱེད། །ཅེས་པའི་བར་དུ་འདིས་དོན་རྣམ་པ་བདུན༌[^2786]ཞིག་སྟོན་ཏེ། སྟོན་མཁས་པ་མངོན་པར་ཤེས་པ་དང་ལྡན་པ། ཡང་དག་པར་རིག་པ་བརྙེས་པ། དབང་པོ་རིག་པ། ཆོས་ཀྱི་མཆོག་སྟོན་པ། ཕན་པ་ཆེན་པོ་བྱེད་པ། སངས་རྒྱས་ཀྱི་ཞིང་དག་པར་བྱེད་པའོ། །

[Block 3284 [HEADING]]
##### སྔོན་དུ་ལུང་བསྟན་པ། ^4-8-7-2-0

[Block 3285 [HEADING]]
###### རྒྱུ། ^4-8-7-2-1-0

[Block 3286]
མདོ་ལས་མ་འོངས་པའི་དུས་ན་དེ་བཞིན་དུ་ཞེས་པ་ནས། རྟག་ཏུ་འཛིན་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་འདིས་ལུང་སྟོན༌[^2787]པ་སྟེ། སྔར་ཚིག༌[^2788]གཉིས་ཀྱིས་ནི་རྒྱུ་བསྟན། ཚིག་བདུན་གྱིས་ནི་འབྲས་བུ་བསྟན་ཏེ། སངས་རྒྱས་རྣམས་ལ་མཆོད་པ་དང་། ཆོས་སྟོན་པ་དང་། སངས་རྒྱས་ཀྱི་ཞིང་དག་པར་བྱེད་པ་དང་། སེམས་ཅན་ལ་ཕན་འདོགས་པའོ། །

[Block 3287 [HEADING]]
###### འབྲས་བུ། ^4-8-7-2-2-0

[Block 3288]
མདོ་ལས།

[Block 3289]
འཇིག་རྟེན་དུ་ནི་རང་བྱུང༌[^2789]སངས་རྒྱས་གྱུར། །ཞེས་པ་ནས། ངན་སོང་དང་ནི་ངན་འགྲོའི༌[^2790]འཇིགས་པ་མེད། །ཅེས་པའི་བར་དུ་ནི་འབྲས་བུ་བསྟན་ཏེ་དེ་ཡང་དེའི་རང་བཞིན་དང་། དེའི་ཞིང་དང་དེའི་བསྐལ་པའི༌[^2791]མིང་དང་། ཞིང་གི་རྒྱན་དང་། བྱང་ཆུབ་སེམས་དཔའི་འཁོར་རྣམས་ཏེ། གོང་དུ་བཤད་པ་རྣམས་དང་འདྲ་བར་སྦྱར་རོ། །

[Block 3290]
མདོ་ལས།

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
--- END BLOCKS ---
