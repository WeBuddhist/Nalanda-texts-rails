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
[Block 4726]
གང་གི་ཕྱིར་སྒྲ་མེད་པ་དེ་ནི་སྒྲ་མི་གྲག་པ་སྟེ། མིའི་རྒྱུན་ལུགས་མེད་པའང་ཡིན་པས་མིའི་རྒྱུན་ལུགས་མེད་ཅིང་སྒྲ་མི་གྲག༌[^3063]པའོ། །

[Block 4727]
རྩྭ་སྟུག་པོའི་ནང་དུ་ཤིང་གི་རྩ་བ་ལྡམ་ལྡུམ་ནུབ་པ་གང་ཡིན་པ་དེ་དག་ནི་ཤིང་གི་རྩ་བ་དང་། ལྡུམ་བུ་མང་པོ་རྩ༌[^3064]སྟུག་པོའི་ནང་དུ་ནུབ་པའོ། །

[Block 4728]
གང་དུ་དེ་མེད་པ༌[^3065]ནི་ཤིང་གི་རྩ་བ་དང་། ལྡུམ་བུ་ནུབ་པ་དེ་ནའོ། །

[Block 4729]
འགྲོན་པོ་རྣམས་དང་། ཤིང་རྟ་དང་། བཞོན་པ་ནི་འགྲོན་པོ་རྣམས་ཀྱི་ཤིང་རྟ་དང་བཞོན་པའོ། །

[Block 4730]
དེ་རྣམས་ཀྱི་རྐང་པ་ནི་འགྲོན་པོ་རྣམས་ཀྱི་ཤིང་རྟ་དང་བཞོན་པའི་རྐང་པ་སྟེ་དེས་སོ། །

[Block 4731]
སྲོལ་གྱི་མཚམས་བཏོད་པ་ནི་སྲོལ་བཏོད་པ་སྟེ། ལམ་སྲོལ་བཏོད་པ་ནི་ལམ་གྱི་སྲོལ་བཏོད་པའོ། །

[Block 4732]
མ་བཏོད་པའི་ལམ་གྱི་སྲོལ་གང་ཡིན་པའི༌[^3066]ས་ཕྱོགས་ནི་ས་ཕྱོགས་དེ་སྟེ། ས་གཞིའི་ཕྱོགས་དེ་ལམ་གྱི་སྲོལ་མ་བཏོད་པ༌[^3067]དེ་ནའོ། །

[Block 4733]
འབབ་ཆུ་འབབ་པ་དང་། གྲོག་མཁར་དང་། གད་ས༌[^3068]རྣམས་ནི་འབབ་ཆུ་དང་། གྲོག་མཁར་དང་། གད་པ་དག་གོ། །

[Block 4734]
དེ་དག་གི་ས་ཕྱོགས་ནི༌[^3069]མི་བདེ་བ་གང་ཡིན་པའི་དགོན་པའི་ཕྱོགས་དེ་ནི་འབབ་ཆུ་འབབ་པ་དང་། གྲོག་མཁར་དང་། གད་པ་དག་གིས་ས་ཕྱོགས་མི་བདེ་བ་ཡོད་པ་དེ་ནའོ། །

[Block 4735]
ལུས་དང་ལྡན་པ་ཞིག་ཏུ་གྱུར་ཏོ་ཞེས་བྱ་བ་ནི་ལུས་དང་བཅས་པར་སྐྱེས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4736]
རི་དགས་གཟུགས་ཅན་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་རི་དགས་ཤར་བྷར་གྱུར་ཏོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4737]
རི་དགས་གཅིག་པུར་གྱུར་པ་མ་ཟད་དེ། དེ་གསལ་བར་བྱ་བའི་ཕྱིར་སྔར་བསྟན་པའི་སེམས་ཅན་རྣམས་ལ་གནོད་པ་མི་བྱེད་ཅེས་བྱ་བ་སྟེ། ཇི་ལྟར་མི་བྱེད་ཅེ་ན། དཀའ་ཐུབ་ཅན་བཞིན་སྲོག༌[^3070]ཆགས་རྣམས་ལ་བརྩེ། །ཞེས་བྱ་བ་ཡིན་ཏེ། གཞན་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 4738]
ཡུལ་དེ་ལ་དབང་བའི་རྒྱལ་པོ་ཞེས་བྱ་བ་ནི། དགོན་པའི་ཕྱོགས་གང་ན་བྱང་ཆུབ་སེམས་དཔའ༌[^3071]གནས་པའི་འོ། །

[Block 4739]
རྟ་དང་། གླང་པོ་ཆེ་དང་། ཤིང་རྟ་དང་། རྐང་ཐང་གི་ཚོགས་རྒྱང་རིང་པོར་ལུས་བཞིན་དུ་ཞེས་བྱ་བ་ནི་གླང་པོ་ཆེ་ལ་སོགས་པ་ཐག་རིང་དུ་བོར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4740]
ཕྱུང་ནས་ཞེས་བྱ་བ་ནི་རལ་ནས་བླངས་པའོ།[^3072] །གང་གིས་མདའ་མདེའུ་རྣོན་པོ་ཅན་དེ་ཕྱུང་བ་ནི་མདའ་མདེའུ་རྣོན་པོ་ཅན་ཕྱུང་བའོ། །

[Block 4741]
གྱ་ཚོམ་དུ་རྒོལ་བ་སྤང་བ༌[^3073]གང་ཡིན་པ་དེ་ནི་གྱ་ཚོམ་དུ་རྒོལ་བ་སྤངས་པ་སྟེ། རྒོལ་བ་སྤངས་པ་ནི་བདག་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར། རྒོལ་བ་སྤངས་པའོ། །

[Block 4742]
ལམ་ཀ་ན་ཞེས་བྱ་བ་ནི་ཉེ་བ་ན་ཡོད་པའོ། །

[Block 4743]
ཐོག་ནས་ལྷུང་བ་ནི་བསྐྱུར་བའོ། །ཅིའི་ཕྱིར་རྟ་ལས་ལྷུང་ཞེ་ན། དེ་མ་མཐོང་བ་ཡིན་ཏེ།[^3074] མ་མཐོང་བ་ཡིན་པ་དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། མིག་ནི་རི་དགས་དེ་ལ་ཡེངས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་ཕྱེད་དང་པོས་བསྟན་ཏོ། །

[Block 4744]
ཤིན་ཏུ་བརྟན་པར༌[^3075]རྟ་ལ་ཆགས་ཀྱང་ཅིའི་ཕྱིར་ལྷུང་ཞེ་ན། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། ཚིགས་བཅད་ཕྱེད་འོག་མའོ། །

[Block 4745]
སླར་བལྟས་པ་དང་ཞེས་བྱ་བ་ནི། གདོང་ཕྱིར་བསྒྱུར་ཏེ་བལྟས་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4746]
ངལ་བསོ་བའི་ཆེད༌[^3076]དུ་རྟ་ལས་བབས་ཞེས་བརྟགས་པ་སྟེ། འདིར་ཡང་བབས་པ་བརྟགས་པའི་ཕྱིར། འདི་ན་གབ་ཏུ་རུང་བའི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐང་སྨོས་ཏེ།[^3077] འདི་ན་རྩྭ་སྟུག་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིས་ནི་གཞན་གྱི་དགོས་པས་བབས་སོ། །ཞེས་བྱ་བ་དེའི་དགོས་པ་ཡང་མེད་དེ། མ་མཐོང་བས་སོ། །

[Block 4747]
དེ་ལྟར་ངེས་པར་བྱས་ནས་སྙིང་རྗེ་སྐྱེས་པར་གྱུར་ཏོ། །

[Block 4748]
དེ་ཉིད་རྒྱལ་མཚན་བཟང་པོའི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་བཞིས་ནི་ཕུན་སུམ་ཚོགས་པ་དང་བྲལ་བ་དང་། སྡུག་བསྔལ་དང་ཕྲད་པའི་དབང་དུ་བྱས་པ་སྟེ། དེ་ནས༌[^3078]ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་ཕུན་སུམ་ཚོགས་པ་དང་བྲལ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 4749]
ཕུན་སུམ་ཚོགས་པ་ཡང་བསོད་ནམས་ཀྱི་འབྲས་བུས༌[^3079]དབྱེ་བས་གསུམ་དུ་སྦྱར་ཏེ། བཟོད་པ་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་དང་བྲལ་བའི་དབང་དུ་བྱས་ནས། དེ་ཉིད་རྒྱལ་མཚན་བཟང་པོའི༌[^3080]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ཡིན་ཏེ། ཕྱི་བཞིན་བསྐྱལ་ཞིང་ཞེས་བྱ་བ་འདིས་ནི། གཡོག་འཁོར་ཕུན་སུམ་ཚོགས་པར་གཟུང་ངོ་། །མཛེས་པའི་གདུགས་ཀྱིས་བསྐྱབས༌[^3081]ཞེས་བྱ་བ་དང་། གཡག་རྔའི༌[^3082]བསིལ་ཡབ་གཡོབ་པས་མཛེས་པར་བྱས། ཞེས་བྱ་བས་ནི། སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་ཚོགས་ཀྱི་འབྲས་བུ་དང་བྲལ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 4750]
སྐྱེ་བོ་མང་པོས་བཀུར་བའི་ལྷ་ཡི་དབང་པོ་བཞིན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི། ཚུལ་ཁྲིམས་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི༌[^3083]འབྲས་བུ་དང་བྲལ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 4751]
དེ་རིང་ཁོ་ནར༌[^3084]གཡང་ས་ཆེན་པོར་ལྷུང་། །ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་དང་ཕྲད་པའི་དབང་དུ་བྱས་པའོ། །

[Block 4752]
ཡན་ལག་གྲུགས་པར་གྱུར་ཅེས་བྱ་བ་ནི། ཡན་ལག་གྲུགས་པ་དེ་མེད་ཀྱང་བརྒྱལ་བར་གྱུར་པའམ། དེ་མེད་ཀྱང་མྱ་ངན་བྱེད་པ་སྟེ། དེ་བས་ན་གཡང་ས་འདི་ལས་བདག་ཉིད་ཀྱིས་ཐར་བར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 4753]
མྱ་ངན་བྱེད་དོ་ཞེས་བསྟན་པ་ལ། ཇི་ལྟར་དེ་མྱ་ངན་བྱེད་པར་འགྱུར་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར། སྡུག་བསྔལ་མ་མྱོང་རབ་ཏུ་གཞོན་ཤ་ཅན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4754]
མ་རབས་རྣམས་ལ་རྨ་རྙིང་སོས་འདྲ་བར། །ཞེས་བྱ་བས་ནི་སྡུག་བསྔལ་སྐྱེས་པ༌[^3085]ཡིན་ནོ། །

[Block 4755]
སྲོག་གི་ལྷག་མ་ཙམ་ཞིག་ལུས་སུ་ཟིན་ཀྱང་ཞེས་བྱ་བ་ནི་ངེས་པར་འཆི་བ་ཉིད་དེ། གཡང་ས་ཟབ་པའི་ཕྱིར་རོ། །

[Block 4756]
སྙིང་རྗེས་སེམས་དྲངས་ནས་ཞེས་བྱ་བ་ནི་ཕུན་སུམ་ཚོགས་པ་དང་བྲལ་བ་དང་། སྡུག་བསྔལ་གྱི་རྒྱུས༌[^3086]སྙིང་རྗེ་བའོ། །

[Block 4757]
དེ་ནི་འཐབ་བེར་ནི་རྡུལ་གྱིས་གཡོགས༌[^3087]ཐོད་བཅིངས་པ་ནི་ཞིག་ཅེས་བྱ་བ་འདིས་ནི། ལུས་ལ་གྱོན་པའི་གོས་དག་འགྱུར་བར་སྟོན༌[^3088]ཏོ། །

[Block 4758]
གཡང་ས་ནས་ལྷུང་སྟེ་སྣད་པའི་ཚོར་བ་མྱོང་བ་ནི་སེམས་ལ༌[^3089]ཁྱབ་པར་གྱུར་ཅེས་བྱ་བ་འདིས་ནི་ལུས་ཀྱི་སྡུག་བསྔལ་དེས་བྱས་པའི་སེམས་ཀྱི་སྡུག་བསྔལ་ལོ། །

[Block 4759]
འདུག་པ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་གྱུར་པས་འགྲོ་བའི་སྐབས་མེད་དོ། །ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4760 [VERSE]]
འགྲོ་བ་ནི་འགྱུར་ལྡོག་ཉེ་བར་བྱེད་པའོ། །
དེའི་སྡུག་བསྔལ་ཡིན་པས་དེའི་སྡུག་བསྔལ་ཏེ།
རྒྱལ་པོ་དེའི་སྡུག་བསྔལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4761]
དེའི་སྡུག་བསྔལ་ཐུན་མོང་ཉིད་དུ་གྱུར་པ་ནི། དེའི་སྡུག་བསྔལ་གྱི་རྒྱུས་ཐུན་མོང་དུ་གྱུར་པའོ། །

[Block 4762]
ཡ་རབས་ཀྱི་ཚུལ་བཞིན་དུ་སྐྱེ་བོ་དགེ་བའི་རང་བཞིན་སྟོན་པར་བྱེད་པའི་ཚིག་དེ་བསྒྲུབ་པའི༌[^3090]ཕྱིར། རྒྱལ་པོ་ཆེན་པོ་སྣད་པར་མ༌[^3091]གྱུར་ཏམ། །ཞེས་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4763]
དེ་ལ་ཡ་རབས་ཚུལ་བཞིན་ཞེས་བྱ་བ་ཉིད་ནི་རྒྱལ་པོ་ཆེན་པོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 4764]
སྐྱེ་བོ་དགེ་བའི་རང་བཞིན་སྟོན་བྱེད་ཅིང་། །ཞེས་བྱ་བའི་ཚིག་གིས་ནི་སྣད་པར་མ་གྱུར་ཏམ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་སོ། །

[Block 4765]
འདི་ནི་སྐྱེ་བོ་དགེ་བའི་རང་བཞིན་ཏེ། གཞན་སྡུག་བསྔལ་བ་ལ་རང་བཞིན་གྱིས་བརྩེ་བ་ཡིན་ཏེ། སྣད་པར་མ་གྱུར་ཏམ་ཞེས་བྱ་བ་ནི། ལུས་སྣད་པར་མ་གྱུར་ཏམ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པའོ། །
--- END BLOCKS ---
