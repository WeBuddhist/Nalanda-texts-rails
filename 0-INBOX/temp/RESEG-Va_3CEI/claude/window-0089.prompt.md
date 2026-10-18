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
[Block 3116]
སྐྱེ་མཆེད་དྲུག་ནི་རྣམ་པར་སྨིན་པའི་དབང་པོ་དྲུག་ཅན་ནོ། །

[Block 3117]
རེག་པ་ནི་རྣམ་པར་སྨིན་པའི་རེག་པ་མྱོང་བ་ཉིད་རེག་པའོ། །

[Block 3118]
ཚོར་བ་ནི་རྣམ་པ་གསུམ་མྱོང་བའོ། །

[Block 3119]
སྲེད་པ་ནི་ཕྱི་ནང་གི་ཡུལ་ལ་ཆེ་ཆུང་རྣམ་པ་གསུམ་དུ་ཞེན་པའོ། །

[Block 3120]
ལེན་པ་ནི་ཉོན་མོངས་པའི་བདག་ཉིད་ཅན་གཟུང་བ་དང་འཛིན་པའི་ཆོས་ཀྱི་ཉོན་མོངས་པའི་ཕུང་པོ་ལེན་པའོ། །

[Block 3121]
སྲིད་པ་ནི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་འཁོར་བ་ལེན་ཅིང་ཁམས་གསུམ་དུ་འབྱུང་ཞེས་པའི་དོན་ཏོ། །

[Block 3122]
སྐྱེ་བ་ནི་རྒྱུས་འཕགས་ནས་འབྲས་བུ་ལེན་པའོ། །

[Block 3123]
རྒས་པ་ནི་འབྲས་བུའི་མཐར་གྱུར་པའོ། །

[Block 3124]
སློས་པའི་མྱ་ངན་ཞེས་པ་ནི་འཆི་ཁར་ཡིད་ཀྱིས༌[^2624]གདུང་བའོ། །

[Block 3125]
སྨྲེ་སྔགས་འདོན་ཞེས་པ་ནི་ཚིག་ཏུ་འདོན་པའོ། །

[Block 3126]
ཡིད་མི་བདེ་བ་དང་འཁྲུག་པ་ནི་ནང་གི་གདུང་བ་སྟེ། ཞིབ་ཏུ་ཆོས་མངོན་པ་དང་། རྣལ་འབྱོར་སྤྱོད་པ་ལས་འབྱུང་བ་བཞིན་དུ་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བའོ། །

[Block 3127]
མདོ་ལས་དེ་ལྟར་དགེ་སློང་རྣམས་ཞེས་པ་ནས་བསམ་གཏན་བྱེད་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་སོ་སོ་ནས་བདེ་བ་ཐོབ་པ༌[^2625]བསྟན་ཏོ། །

[Block 3128]
ལེན་པ་ཞེས་པ་ནི༌[^2626]ཆགས་པས་ཏེ། ཆོས་རྣམས་ལ་ཆགས་པ་མེད་པ་ཉིད་རྣམ་པར་གྲོལ་བའོ། །

[Block 3129]
མདོ་ལས་དེ་ནས༌[^2627]ཡང་མཐར་གྱིས་ཞེས་པ་ནས་རྣམ་པར་གྲོལ་ལོ་ཞེས་པའི་བར་དུ་ནི་དེའི་འོག་མ་རྣམས་ཀྱང་དེ་བཞིན་དུ་རྣམ་པར་གྲོལ་བ་ཐོབ་པོ་ཞེས་པའོ། །

[Block 3130]
མདོ་ལས་དེའི་འོག་ཏུ་དགེ་སློང་ཕ་རྣམས་ཞེས་པ་ནས་གྲངས་བགྲང་བ༌[^2628]ལས་འདས་པར་གྱུར་པའོ་ཞེས་པའི་བར་དུ་ནི་ཉན་ཐོས་པ་རྣམས་ཀྱི༌[^2629]འཁོར་བསྟན་ཏོ། །

[Block 3131 [HEADING]]
#### རྗེས་སུ་ཆོས་སྟོན་པ། ^4-7-7-0

[Block 3132]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཡང་དེའི་ཚེ་ཞེས་པ་ནས་བྱང་ཆུབ་འདོད་པ་ཞེས་པའི་བར་དུ་ནི་རྗེས་སུ༌[^2630]ཆོས་སྟོན་པ་སྟེ། རྒྱལ་བུ་བཅུ་དྲུག་གི་ཡོན་ཏན་ནི་འཁོར་བའི་དྲ་བ་གཅོད་པས༌[^2631]རབ་ཏུ་བྱུང་བ་ཆོས་ཐོས་བས་དབང་པོ་རྣོ་བ། རང་བཞིན་གསལ་བས་ཤེས་རབ་རྣོ་བ། སྔོན་དེ་བཞིན་གཤེགས་པ་ལ་བསྙེན་བཀུར་བྱས་པས་དགེ་བའི་བཤེས་གཉེན་དང་ཕྲད་པ་དང་། [^2632]ཚུལ་ཁྲིམས་གཙང་མས༌[^2633]འབྲས་བུ་ཆེན་པོ་ལ་རེ་བའོ། །

[Block 3133]
མདོ་ལས་དེ་ནས༌[^2634]དགེ་སློང་རྣམས་དགེ་སྦྱོང་དེ་དག་གི་ཞེས་པ་ནས་བདག་ཅག་གི་བསམ་པ་ཡང་མཁྱེན་ཏེ་ཞེས་པའི་བར་དུ་ནི་སྔར་ཉན་ཐོས་པ་རྣམས་དེ་དང་མཐུན་པའི་ཆོས་བཤད། བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཅན་རྣམས་ལ་ཐེག་པ་ཆེན་པོ་བཤད་དུ་གསོལ་ཞེས་པའོ། །

[Block 3134]
མདོ་ལས་དེ་ནས་དེ་དག་དགེ་སློང་རྣམས་དེའི་ཚེ་ན་ཞེས་པ་ནས་རབ་ཏུ་བྱུང་བར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་དེ་དང་མཐུན་པའི་འཁོར་རྣམས་རབ་ཏུ་བྱུང་བའོ། །

[Block 3135]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཞེས་པ་ནས་དེ་དག་ཐམས་ཅད་ལ་རྒྱས་པར་བཤད་དོ་ཞེས་པའི་བར་དུ་ནི༌[^2635]འདིས་ནི་སེམས་ཅན་གྱི་དབང་པོ་སྨིན་པའི་ཕྱིར་བསྐལ་པ༌[^2636]སྟོང་ཕྲག་ཉི་ཤུའི་འོག་ཏུ་བཤད་པའི་དུས་ལ་བབ་པ་དང་། བཤད་པར་བྱ་བའི་ཆོས་གང་ཡིན་པ་བསྟན་པའོ། །

[Block 3136]
མདོ་ལས་དེ་ནས་ཡང་དགེ་སློང་རྣམས་ཞེས་པ་ནས་ཁོང་དུ་ཆུད་དོ་ཞེས་པའི་བར་དུ་ནི་དགེ་སློང་རྣམས་ཀྱིས་ཆུད་པར༌[^2637]བསྟན་ཏོ།[^2638] །མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཞེས་པ་ནས་ཐེ་ཚོམ་ཟ་བ་ཐོབ་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་འདིས་དབང་པོའི༌[^2639]རིམ་པ་སྟོན་ཏེ། དབང་པོ་རྣོན་པོ་དང་བར་མས་རྣམ་པར་གྲོལ་བ་ཐོབ་པ་དང་། དབང་པོ་ཐ་མ་ཐེ་ཚོམ་དུ་གྱུར་པ་སྟེ། ཆོས་འདི་གོ་དཀའ་བར༌[^2640]སྟོན་ཏོ།[^2641] །མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་གཙུག་ལག་ཁང་དུ་ཞུགས་སོ་ཞེས་པའི་བར་དུ་ནི་སྲས༌[^2642]རྣམས་དབང་པོ་སྨིན་ཅིང་སེམས་ཅན་སྒྲོལ་ནུས་པར་བསྟན་པའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཏིང་ངེ་འཛིན་དུ་ཞུགས་པ་བསྟན་པའོ། །

[Block 3137]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་དགེ་སྦྱོང་དེ་དག་གི་ཞེས་པ་ནས་རྒྱས་པར་བཤད་དོ་ཞེས་པའི་བར་དུ་ནི་སྲས་རྣམས་ཆོས་སྟོན་པས་འགྲོ་བ་རྣམས་ཀྱི་བདེ་བ་རྙེད་པ་བསྟན་པའོ། །

[Block 3138]
མདོ་ལས་བྱང་ཆུབ་སེམས་དཔའ་རེ་རེས་ཀྱང་ཞེས་པ་ནས་ཡོངས་སུ་སྨིན་པར་བྱས་སོ་ཞེས་པའི་བར་དུ་ནི། བདེན་པ་དངོས༌[^2643]བསྟན་པ་དང་། མོས་པ་རྙེད་པ་རྣམས་སྤྲོ་བར་བྱས་པ་དང་། ཉམས་ཀྱིས༌[^2644]དོགས་པ་རྣམས་གཟེངས་བསྟོད༌[^2645]དེ་དགའ་བར་བྱས་པ་དང་། འབད་པ་རྣམས་བསྟོད་ཅིང་བྱེད་དུ་གཞུག་པ༌[^2646]ཞེས་པའོ། །

[Block 3139]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཞེས་པ་ནས་བརྒྱ༌[^2647]སྟོང་མང་པོ་ལ་ཆོས་སྟོན་ཏོ་ཞེས་པའི་བར་དུ་ནི་དགེ་སྦྱོང༌[^2648]དྲུག་ཅུ༌[^2649]པོ་དེ་དག་ལ་བསྟོད་པ་དང་ལུང་བསྟན་པ༌[^2650]སྟེ། བསྟོད་པ་ཡང་ངོ་མཚར་དུ་གྱུར་པ་དང་། དབང་པོ་རྣོ་བ་དང་། རིག་པ་དང་ལྡན་པ་དང་། འཕགས་པ་རྣམས་ལ་བསྙེན་བཀུར་བྱས་པ་དང་། དཀའ་བ་སྤྱོད་པ་དང་། དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་འཛིན་པ་དང་། སེམས་ཅན་རྣམས་ལ་ཆོས་སྟོན་པའོ། །

[Block 3140]
མདོ་ལས་འདི་ལྟ་སྟེ་དགེ་སློང་རྣམས་ཞེས་པ་ནས་སངས་རྒྱས་སོ་ཞེས་པའི་བར་དུ་ནི་སངས་རྒྱས་དེ་དག་ནི་ཉོན་མོངས་པས་མི་བསྒུལ་བ་དང་། ཡོན་ཏན་འཕགས་པ་དང་། སེང་གེ་བཞིན་སྒྲ་མི་འཇིགས་པ་སྒྲོགས་པ་དང་། བདུད་ཀྱི་དཔུང༌[^2651]འཇོམས་པ་ལ་བཏགས་སོ། །

[Block 3141]
མདོ་ལས་ལྷོ་ཕྱོགས་ན་ཞེས་པ་ནས། སངས་རྒྱས་སོ་ཞེས་པའི་བར་དུ༌[^2652]སངས་རྒྱས་ཀྱི་མཚན་དེ༌[^2653]དག་ཉོན་མོངས་པ་འཇོམས་པ་དང་། ཡོན་ཏན་གྱི་མཚན་ཉིད་ལ་གནས་པ་དང་། བདག་དང་གཞན་གྱི་དོན་མཛད་པ་ལས་བཏགས་པ་ལས་ཞེས༌[^2654]པར་བྱའོ། །

[Block 3142]
མི་མཇེད་ཅེས་པ་ནི་འཇིག་རྟེན་གྱི་ཁམས་དེ་སྡུག་བསྔལ་སྣ་ཚོགས་སྤྱོད་པ་ལ་ཇི་མི་སྙམ་པའི་ཕྱིར་མི་མཇེད་པ་དང་།[^2655] ཤཱཀྱ་ཐུབ་པའི་སངས་རྒྱས་ཀྱི་ཞིང་ངོ་། །མདོ་ལས་དགེ་སློང་རྣམས་ཞེས་པ་ནས་ཡེ་ཤེས་དེ་ལ་མོས་པར་དཀའོ་ཞེས་པའི་བར་དུ་ནི་མདོ་སྡེ་འདི་ལ་འཇུག་པར་དཀའ་བའི་ཕྱིར་སྔར་དྲང་པའི་དོན་བསྟན། ཕྱིས་ངེས་པའི་དོན་བསྟན་ཅིང་མོས་པ་སྐྱེས་པའོ། །

[Block 3143]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ་ནས་དགེ་སློང་རྣམས་ང༌[^2656]བྱང་ཆུབ་སེམས་དཔར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་བསྡུས་པའོ། །

[Block 3144 [HEADING]]
#### དོགས་པ་བསལ་བ། ^4-7-8-0

[Block 3145 [HEADING]]
##### གླེང་བ། ^4-7-8-1-0

[Block 3146]
མདོ་ལས་ང་མྱ་ངན་ལས་འདས་ནས་ཞེས་པ་ནས་མྱ་ངན་ལས༌[^2657]འདའ་བར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་འཕགས་པ་ཉན་ཐོས་པ་རྣམས་མཐར་བླ་ན་མེད་པའི་སངས་རྒྱས་སུ་གྲུབ་པར༌[^2658]འགྱུར་རོ་ཞེས་པ་ནི༌[^2659]སངས་རྒྱས་བཞུགས་ཏེ། དགེ་བའི་བཤེས་གཉེན་གྱིས༌[^2660]བླ་ན་མེད་པའི་གནས་སུ་བསྒྱུར་བ༌[^2661]བཞུགས་ན་ནི་དེ་ལྟར་ཡང་རུང་ན་སངས་རྒྱས་མི་བཞུགས་པའི་ཁམས་སུ་ཉན་ཐོས་ལ་སོགས་པའི་རིགས་སུ་སེམས་བསྐྱེད་པ་རྣམས་བྱང་ཆུབ་སེམས་དཔའ༌[^2662]སྤྱོད་པ་རྒྱ་ཆེན་པོ་མ་ཐོས་པའི་རྣམས་ཐལ་བྱུང་ཉན་ཐོས་པའི་རིགས་སུ་ལྟུང་ཞིང་ལྷག་མ་མ་ལུས་པའི་མྱ་ངན་ལས་འདས་པར་མི་འཇུག་གམ་ཞེས་པའི་དོགས་པ་བསལ་བའི་ཕྱིར་འདི་སྨྲས་པ་སྟེ། དེ་ལ་ཡང་དང་པོ་གླེང་བ་དང་། དེ་ཡང་སངས་རྒྱས་སུ་གྲུབ་པ་དང་། དེ་གྲུབ་པའི་གཏན་ཚིགས་ཏེ། འདི་ནི་དང་པོའོ། །

[Block 3147 [HEADING]]
##### སངས་རྒྱས་སུ་གྲུབ་པ། ^4-7-8-2-0

[Block 3148]
མདོ་ལས་ཡང་དགེ་སློང་རྣམས་འཇིག་རྟེན་གྱི་ཁམས་གཞན་དུ་ཞེས༌[^2663]པ་ནས་ཡེ་ཤེས་ཚོལ་ཞིང་སྐྱེའོ་ཞེས་པའི་བར་དུ་ནི་དེ་སངས་རྒྱས་སུ་གྲུབ་པ༌[^2664]བསྟན་ཏེ། བཅོམ་ལྡན་འདས་ཁམས་འདིར་མྱ་ངན་ལས་འདས་པ་སྟོན་ཀྱང་ཡུལ་ཁམས་གཞན་དུ་སེམས་ཅན་གྱི་དོན་མཛད་པར་ཉན་ཐོས་རྣམས་ཀྱང་དེར་སྐྱེ་བ་དང་། དེར་སྐྱེ་བ་ཡང་ཉན་ཐོས་ཀྱི་བསྐལ་པ་སྨིན་པ་དང་། དེ་བཞིན་གཤེགས་པའི་ཐུགས་རྗེས་ཀྱང་སྐྱབས༌[^2665]ཏེ། དེར་སྐྱེ་བས་སངས་རྒྱས་སུ་ལུང་སྟོན་ཏོ། །

[Block 3149 [HEADING]]
##### གྲུབ་པའི་གཏན་ཚིགས། ^4-7-8-3-0

[Block 3150]
མདོ་ལས་དེ་ནས་ཡང་དེ་བཞིན་གཤེགས་པའི་ཞེས་པ༌[^2666]ནས་ཡིན་པར་རིག་པར༌[^2667]བྱ་བ༌[^2668]ཞེས་པའི་བར་དུ་ནི་དེ་གྲུབ་པའི༌[^2669]གཏན་ཚིགས་བསྟན་ཏེ། ཐེག་པ་དེ་གཉིས་ཀྱང་མཐར་ཐེག་པ་ཆེན་པོར་འདུ་སྟེ། མྱ་ངན་ལས་འདས་པར་འགྱུར་གྱིས་ལོགས་ཤིག་ན་མྱ་ངན་ལས་འདས་པ་མེད་དེ། གཉིས་དང་གསུམ་བསྟན་པ་ཡང་སེམས་ཅན་གྱི་དབང་པོ་མི་མཐུན་པ་ལས་ཐབས་ཀྱིས་བཤད་པར་ཟད་ཀྱི༌[^2670]ངེས་པར་གཉིས་དང་གསུམ་དུ་མེད་དོ། །

[Block 3151]
མྱ་ངན་ལས་འདས་པ་ཆེན་པོའི་མདོ་ལས་ཀྱང་། མྱ་ངན་ལས་འདས་པ་ནི་ཇི་ལྟ་བུ། མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ནི་ཇི་ལྟ་བུ་ཞེས་དྲིས་པ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་བསྐལ་པ་བརྒྱད་ཁྲིའམ། དྲུག་ཁྲིའམ། བཞི་ཁྲིའམ། ཉི་ཁྲིའམ། ཁྲི་གཅིག་གི་བར་དུ་བཞུགས་པའི་གནས་དེ་ནི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 3152]
འཕགས་པ་ཆོས་ཀྱི་རྒྱལ་པོའི་གནས་དེ་ནི་མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ཞེས་གསུངས་སོ།། །།

[Block 3153]
དམ་པའི་ཆོས་པུཎྜ་རཱི་ཀའི་འགྲེལ་པ། [^2671]བམ་པོ་བརྒྱད་པ་སྟེ་ཐ་མ།[^2672]

[Block 3154 [HEADING]]
#### དོན། ^4-7-9-0

[Block 3155]
མདོ་ལས་དགེ་སློང་རྣམས་གང་གི་ཚེ་ན་ཞེས་པ་ནས་བསམ་གཏན་ཆེན་པོ་དང་ལྡན་པ་གཟིགས་ན་ཞེས་པའི་བར་དུ་ནི་རྣམ་པ་གསུམ་དུ་དབྱེ་སྟེ། དོན་དང་། དཔེ་དང་། བསྡུ་བའོ། །
--- END BLOCKS ---
