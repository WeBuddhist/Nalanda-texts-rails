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
[Block 3221]
མྱ་ངན་འདས་ཤིང་སེམས་ནི་དགའ་བར་བྱོས། །ཞེས་པ་ནས། དེ་ནས་དེ་དག་ཐམས་ཅད་མཐར་འགྲོ་བ། །ཞེས་པའི་བར་དུ་ནི་དུབ་པ་བསྟི་བའི་དཔེ་བསྟན་ཏོ། །

[Block 3222]
མདོ་ལས།

[Block 3223]
ཐམས་ཅད་ངལ་སོས་པ་ཡི༌[^2727]ཚུལ་རིག་ནས། །ཞེས་པ་ནས། གླིང་དུ་འགྲོ་བའི་ཕྱིར་ནི་བརྩོན་འགྲུས་བསྐྱེད།[^2728] །ཅེས་པའི་བར་དུ་ནི་ངེས་པའི་དོན་སྟོན་པའི་དཔེའོ། །

[Block 3224]
མདོ་ལས།

[Block 3225]
དགེ་སློང་དེ་བཞིན་ང་ཡང་འདྲེན་པ་སྟེ། ཞེས་པ་ནས་ཁྱེད་ཅག་བྱ་བ་བྱས་ཞེས་པའི་བར་དུ་ནི། འདི་མན་ཆད་དཔེ་དང་དོན་དུ་སྦྱར་བ་དང་། བཀྲི་བའི་དོན་དང་། ངེས་པའི་དོན་སྟོན་ཏེ། འདི་ནི་དང་པོའོ། །

[Block 3226]
མདོ་ལས།

[Block 3227]
དུས་སུ་ནམ་ཞིག་གནས་འདིར་འདུག་པ་ཡི། །ཞེས་པ་ནས། ཆོས་འདི་ཇི་བཞིན་ཡང་དག་དོན་བཤད་དོ། ། ཞེས་པའི་བར་དུ་ནི་ཡང་དག་པར་སྟོན་པའི་གླེང་བའོ། །

[Block 3228]
མདོ་ལས།

[Block 3229]
དྲང་སྲོང་ཆེན་པོས༌[^2729]ཐེག་པ་གསུམ་བསྟན་པ། །ཞེས་པ་ནས།

[Block 3230 [VERSE]]
སངས་རྒྱས་གྱུར་ནས་མྱ་ངན་འདས་པ་ཡིན། །
ཞེས་པའི་བར་དུ༌[^2730]ནི་དྲང་བའི་དོན་བོར༌[^2731]ལ།
ངེས་པའི་དོན་ལ་ཞུགས་ཞེས་པར་བསྟན་པའོ། །

[Block 3231]
མདོ་ལས།

[Block 3232]
འདྲེན་པ་རྣམས་ཀྱིས་བསྟན་པ་འདི་འདྲའོ། །ཞེས་པ་ནས། ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱེད། །ཅེས་པའི་བར་དུ་ནི་བསྡུས་པ་བསྟན་ཏོ།། །།

[Block 3233 [HEADING]]
### དགེ་སློང་ལྔ་བརྒྱ་ལུང་བསྟན་པའི་ལེའུ། ^4-8-0

[Block 3234]
འདི་མན་ཆད་དགེ་སློང་ལྔ་བརྒྱ་ལུང་བསྟན་པའི་ལེའུ་སྟེ། གཏན་ཚིགས་དང་། མིང་དང་། དྲིས་པའི་ལན་དང་གསུམ་དུ་དབྱེའོ། །

[Block 3235 [HEADING]]
#### གཏན་ཚིགས། ^4-8-1-0

[Block 3236]
ལེའུ་འདིའི་མིང་གདགས་པའི༌[^2732]གཏན་ཚིགས་ཀྱང་རྣམ་པ་བཞི་སྟེ། དབང་པོའི་རིམ་པ་བཞིན་དུ་ལུང་སྟོན་པས་དབང་པོ་རྣོན་པོ་རྣམས་ལུང་བསྟན་པའི༌[^2733]འོག་ཏུ་ལུང་སྟོན༌[^2734]པ་འདི་འབྱུང་བ་དང་། ལྷག་པའི༌[^2735]ང་རྒྱལ་ཅན་བསམ་གཏན་སྤྱོད་པ་མེད་པ་དག་སེམས་གཡེང་བ་བསྡུས་པའི༌[^2736]དོན་ཐེག་པ་ཆེན་པོའི་དགེ་བའི་རྩ་བ་ཡོད་པར་མི་ཤེས་པའི་དཔེར་ལུས་ལ་རིན་པོ་ཆེ་ཐོགས་པའི་དཔེ་བསྟན་ཏེ། ཏིང་ངེ་འཛིན་དང་ཐེག་པ་ཆེན་པོ་ལ༌[^2737]གཞུག་པའི་ཕྱིར་ལེའུ་འདི་སྟོན་པ་དང་། བླ་ན་མེད་པ་བཅུ་ལས་ཤེས་པར་བྱ་བ་བླ་ན་མེད་པ་བསྟན་པའི་ཕྱིར་ཐེག་པ་ཆེན་པོའི་དགེ་བའི་རྩ་བ་ཡོད་པ་བསྟན་པའི་ཕྱིར་ལེའུ་འདི་བསྟན་པ༌[^2738]དང་། ལུང་སྟོན་པ་རྣམ་པ་དྲུག་ལ་མཉམ༌[^2739]པ་ལས་དགོངས་ཏེ་ལུང་སྟོན་པ་ཉིད་བསྟན་པའི་ཕྱིར་ལེའུ་འདི་བཤད་པའོ། །

[Block 3237 [HEADING]]
#### མིང། ^4-8-2-0

[Block 3238]
ལྔ་བརྒྱ་ནི་གྲངས་སོ། །

[Block 3239]
དགེ་སློང་ཞེས་པ་ནི་དངོས་པོའོ། །

[Block 3240]
ལུང་བསྟན་ཞེས་པ་ནི་དོན་དེ་ལས་མང་དུ་བཏགས་པའོ། །

[Block 3241 [HEADING]]
#### དྲིས་པའི་ལན། ^4-8-3-0

[Block 3242]
ལེའུ་འདིའི་ནང་ནས་རིན་པོ་ཆེ༌[^2740]ལུས་ལ་ཐོགས་པའི་དཔེས་དོན་སྟོན་ན་མིང་དེ་ལས་མི་གདགས་པར་ཅིའི་ཕྱིར་ལུང་བསྟན་པའི༌[^2741]ལེའུ་ཞེས་གདགས་ཞེས་དྲི་བ༌[^2742]དང་དེ་ནི་དབང་པོ་སྨིན་པ་སེམས་སྐྱེས་པ་རྣམས་སྔར་ལུང་བསྟན་ཏེ། དེའི་འོག་ཏུ་དཔེ་སྟོན་པའི་ཕྱིར་མིང་དེར་བཏགས་ཀྱང་ཉེས་པ་མེད་དོ། །

[Block 3243]
ཡང་འཁོར་དེར་དགེ་སློང་སྟོང༌[^2743]ཉིས་བརྒྱ་ལུང་བསྟན་པ་ཐོབ་ན་འདིར་ལྔ་བརྒྱ་ཉི་ཚེར་སྨོས་པ་ཅིའི་ཕྱིར་དྲིས་པ་དང་། དགེ་སློང་དེ་རྣམས་འཁོར་དེ་ཉིད་ན་འདུག་གི་གཞན་དེ་ན་མི་འདུག་པས་མངོན་དུ་གྱུར་པ་རྣམས་ལུང་བསྟན་པ་དང་། སྟོང་ཉིས་བརྒྱ་ནི་སྤྱིར་ལུང་བསྟན་གྱི། འདི་ནི་ཕྱེ་སྟེ་ལུང་བསྟན་པའི་ཕྱིར་ཞེས་ཀྱང་འཆད་དོ། །

[Block 3244 [HEADING]]
#### བཅོམ་ལྡན་འདས་ལ་གུས་པ་བསྟན་པ། ^4-8-4-0

[Block 3245]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་གང་པོ་མཻ་ཏྲིའི་བུ་ཞེས་པ་ནས་འདི་དག་ཐོས་ནས་ཞེས་པའི་བར་དུ༌[^2744]ནི་བཅོམ་ལྡན་འདས་ལ་དང་པོར༌[^2745]གུས་པ་བསྟན་པ་དང་། དེའི་འོག་ཏུ་བཀའ་དམ་པ་མནོས་པ་སྟེ། དེའི་དང་པོ་ལ་ཡང་གུས་པའི་ཚུལ་དང་། མནོས་པའི་དོན་ཏོ། །

[Block 3246]
མནོས་པའི་དོན་ཡང་ངེས་པའི་དོན་དང་། དྲང་བའི་དོན་ཏོ། །

[Block 3247]
བཅོམ་ལྡན་འདས་ཀྱི་ཆེ་བ་ཉིད་ཅེས་པ་ནི། ཆོས་སྟོན་པར་དགོངས་པའི་ལྟས་འོད་ཀྱིས་ཁྱབ་པར་མཛད་པ་དང་། ས་གཡོ་བ་དང་མེ་ཏོག་འབྲུལ་བས༌[^2746]འཁོར་གྱི་རྣམ་པ༌[^2747]བསྐུལ་བ་དང་གཟེངས༌[^2748]བསྟོད་པ་ལ་སོགས་པ་མཛད་པའོ། །

[Block 3248]
མདོ་ལས་ངོ་མཚར་དུ་གྱུར༌[^2749]པ་ནས་ཞབས་ལ་ཕྱག་འཚལ་ནས་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ལ་གུས་པའི་ཚུལ་བསྟན་ཏོ། །

[Block 3249]
མདོ་ལས་ངོ་མཚར་ཏོ༌[^2750]བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་མིག་མི་འཛུམས་པར་བལྟའོ་ཞེས་པའི་བར་དུ་ནི་འདིས་སེམས་ཅན༌[^2751]གྱི་བསམ་པ་མཁྱེན་པ་བསྟན་ཏོ།[^2752] །སྔར་ནི་དེ་བཞིན་གཤེགས་པའི་ཡོན་ཏན་བསམ་གྱིས་མི་ཁྱབ་པ་བསྟན། དེའི་འོག་ཏུ་ནི་སེམས་ཀྱི་རྣམ་པ་ཅི་དང་ཅིར་དགྲོལ་བ་མཁྱེན་གཟིགས་པ་སྟོན་པ་དེ་ཡང་སངས་རྒྱས་ཉག་ཅིག་གིས་མཁྱེན་གྱི། གཞན་གྱིས་ནི་མི་ནུས་སོ་ཞེས་པར་སྦྱར་རོ། །

[Block 3250]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་མཻ་ཏྲིའི་བུ་ལྟོས་ཤིག་ཅེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་དྲིས་པ་བསྟན་ཏེ། མངོན་དུ་གྱུར་པ་འདི་ལྟོས་ཤིག་ཅེས་པ༌[^2753]བསྟན་ཏོ། །

[Block 3251 [HEADING]]
#### ད་ལྟར་གྱི་ཡོན་ཏན། ^4-8-5-0

[Block 3252 [HEADING]]
##### ཡོན་ཏན་གྱི་སྤྱི། ^4-8-5-1-0

[Block 3253]
མདོ་ལས་འདི་ནི་ངས་དགེ་སློང་གི་ཞེས་པ་ནས་མང་པོས་བསྟོད་དོ༌[^2754]ཞེས་པའི་བར་དུ་ནི་ད་ལྟར་གྱི་ཡོན་ཏན་སྟོན་ཏེ། ཡོན་ཏན་དེ་ཡང་སྔར་ནི་ཡོན་ཏན་གྱི་སྤྱི་བསྟན། དེའི་འོག་ཏུ་ནི་ཡོན་ཏན་གྱི་ཁྱད་པར་བསྟན༌[^2755]ཏོ། །

[Block 3254 [HEADING]]
##### ཡོན་ཏན་གྱི་ཁྱད་པར། ^4-8-5-2-0

[Block 3255]
མདོ་ལས་རྣམ་པ་མང་པོས་ངའི་བསྟན་པ་འདི་ལ་ཞེས་པ་ནས་གཞན་གྱི༌[^2756]མཐར་ཕྱིན་པར་མི་ནུས་སོ་ཞེས་པའི་བར་དུ་འདིས་ནི་ཡོན་ཏན་གྱི་ཁྱད་པར་བསྟན་ཏོ། །

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
--- END BLOCKS ---
