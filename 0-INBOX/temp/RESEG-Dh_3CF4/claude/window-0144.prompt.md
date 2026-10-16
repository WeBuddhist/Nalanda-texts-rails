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
[Block 5041]
གང་གིས༌[^3246]འཇིགས་ཤིང་སྐྲག་པ་དང་། མྱ་ངན་ཡོངས་སུ་སྤངས་པ་དེ་ནི་འཇིགས་ཤིང་སྐྲག་པ་དང་། །མྱ་ངན་ཡོངས་སུ་བཏང་བའོ། །

[Block 5042]
འཇིགས་པ་སྤངས་པ་ནི་བཟློག་པའི་ཐབས་སྒྲུབ་པས་སོ། །

[Block 5043]
མྱ་ངན་སྤངས་པ་དེ་ནི། དེའི་སྐྱབས༌[^3247]སུ་འགྲོ་བར་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 5044]
སྐྲག་པ་སྤངས་པ༌[^3248]ནི་མི་འབྲོས་པའམ། མི་བྱེད་པས་སོ། །

[Block 5045]
ཡང་ན་སྤྲེའུ་འཁོར་དེ་དག་དབུགས་དབྱུང་བའི་ཕྱིར་འཇིགས་པ་མེད་པའོ། །

[Block 5046]
ཡོངས་སུ་བསྐྱབ་པའི་བློ་བསྐྱེད་པའི་ཕྱིར། སྐྲག་པ་དང་། མྱ་ངན་སྤངས་པའོ། །

[Block 5047]
བྱ་འཕུར་བ་བཞིན་དུ་མཆོངས་པ་གཅིག་གིས་ལེགས་པར་མཆོངས་པར་གྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 5048 [VERSE]]
མཆོངས་པའི་མཐུ་རྩལ་ཆེ་བའི་ཕྱིར་རོ། །
དེས༌[^3249]ནི་སྙིང་རྗེ་རྣམ་པར་བསྐྱེད་པ་དང་། །

[Block 5049]
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་མཆོངས་པའི་མཐུ་རྩལ་ཅན་ནོ་ཞེས་བསྟན་པ་དེ་ནི་མཐུ་རྩལ་གྱི་རྒྱུ་བསྟན་པའི་ཕྱིར་ཏེ། སྙིང་རྗེ་དང་། དཔའ་བའི་ཤུགས་ཀྱི་རྩོལ་བ་གང་ཡིན་པའི་རྒྱུས་སོ། །

[Block 5050]
རྩོལ་བ་དྲག་པ༌[^3250]ནི་འབད་པའི་ཁྱད་པར་དེས་ཏེ། དེའི་ཕྱིར་ཡིད་ལ་བསམས་པ་བཞིན་དུ་ཕྱིན་པར་གྱུར་ཏོ། །

[Block 5051]
དེ་གཉིས་ཀྱི་བར་ནི་དེའི་བར་དེ་ཤིང་དང་རི་གཉིས་ཀྱིའོ། །

[Block 5052]
མཐོ་བའི་འགྲམ་ནི་དེའོ། །

[Block 5053]
ས་ཁྱོན་དེའི་བར་བས་ཀྱང་དཀྱུས་རིང་བ་གང་ཡིན་པའི་སྤ་ཐག་དེ་ནི་ས་ཁྱོན་དེ་བས་རིང་བ་སྟེ། དེ་སྨིན་པར་སྐྱེས་ལ་རྩ་བ་བརྟན་ཞིང་ཕྲ་བ་གང་ཡིན་པ་དེའོ། །

[Block 5054]
དེ་གཉིས་ཀྱི༌[^3251]བར་ཐག་རིང་ཞིང་ཞེས་བྱ་བ་ནི་ཤིང་ཆེན་པོ་དེ་དང་། རིའི་རྩེ་མོ་མཐོན་པོ་དེའི་འགྲམ་མོ། །

[Block 5055]
རྐང་པ་གཉིས༌[^3252]བཅིངས་པ་ནི། རྐང་པ་གཉིས་བཅིངས་པ་སྟེ། དེས་ཟོ་མདོག་མི་བདེ་པའི་ཕྱིར་རོ། །

[Block 5056]
བརྒྱངས༌[^3253]ཞེས་བྱ་བ་ནི་དྲངས་པའོ། །

[Block 5057]
བདག་གི་ལུས་ཀྱི་ཤ་དང་བྲལ་བ་ཅིའི་ཕྱིར་ཞེ་ན། སྤྲེའུའི་ཚོགས་དེ་དག་འཇིགས་པས་ལུས་བརྫིས་པའི་ཕྱིར་རོ། །

[Block 5058]
དེ་ལྟར༌[^3254]ན་ཡང་བརྟན་པ་ཉིད་ནི་མ་ཉམས་པར་སྟོན་ཏོ། །

[Block 5059]
འདི་ལྟར་དཔའ་བ་ཕུན་སུམ་ཚོགས་པས་ནི་སྔར་བསྟན་པའི་འབད་བའི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 5060]
བློ་ཕུན་སུམ་ཚོགས་པ་ནི་རྐང་པ་གཉིས་སྤ་ཐག་གིས༌[^3255]བཅིངས་པའི་ཕྱིར་རོ། །

[Block 5061]
བདག་ལའང་མི་ལྟ་ཞེས་བྱ་བ་ནི་སྤྲེའུའི་ཚོགས་རྣམས་འདི་ལས་མྱུར་དུ་དེང་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 5062]
གཞན་ལ་སྙིང་བརྩེ་ཞེས་བྱ་བ་ནི་བདག་གིས༌[^3256]སྐད་ཀྱིས་སྤྲན་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 5063]
སྤྲེའུའི་བདག་པོ་འདི་སྤྲེའུ་མང་པོ་འཇིགས་ཏེ་བྲོས་པའི་རྐང་ལག་གིས་སྣད་པའི་ལུས་གང་ཡིན་པ་དེ་ནི་སྤྲེའུའི་བདག་པོ་འདི་སྤྲེའུ་མང་པོ་འཇིགས་ཏེ་བྲོས་པའི་རྐང་ལག་གིས་སྣད་པའི་ལུས་སོ། །

[Block 5064]
རྨས་བྱས་པའི་སྡུག་བསྔལ་དང་། སེམས་མི་དྲན་པ་ནི་ལུས་ཀྱི་རྨའི་སྡུག་བསྔལ་གྱིས་བརྒྱལ་བར་གྱུར་ཏེ་སེམས་མི་དྲན་བའོ། །

[Block 5065]
དེ་གཉིས་ལས་བྱུང་བ་ནི་རྨ་བྱུང་བའི་སྡུག་བསྔལ་གྱིས་བརྒྱལ་བར་གྱུར་ཏེ་སེམས་མི་དྲན་པ་ཉིད་དོ། །

[Block 5066]
རྨའི་སྡུག་བསྔལ་དེ་ཡང་སྤྲེའུ་མང་པོ་འཇིགས་ཏེ་བྲོས་པའི་རྐང་ལག་གིས་བརྫིས་པས་ལུས་སྣད་པའི་ཕྱིར་རོ། །

[Block 5067]
དུབ་པ་ཡང་སྤྲེའུའི་ཚོགས་ཀྱིས་རྐང་པས་བརྫིས་པའི་ཕྱིར་ཏེ། གནས་སྐབས་དེ་ལྟ་བུར་ཡུན་རིང་དུ་དུབ་པས་སོ། །

[Block 5068]
ཡ་མཚན་ཆེ་བ་ཞེས་བྱ་བ་ནི་ལྟད་མོར་ཆེ་བའི་ཕྱིར་རོ། །

[Block 5069]
ཁྱོད་ཀྱི་ཅིར་འོང་ཁྱོད་ཀྱང་ཁོང་གི་ཅི། །ཞེས་དྲིས་པ་ཡིན་ཏེ། ངོ་མཚར་ཆེ་བ་ནི་རང་གི་སྲོག་གཏོང་བ་དང་། སྙིང་རྗེ་དང་། གུས་པས་སྤྲེའུའི་ཚོགས་བསྒྲལ་བའི་ཕྱིར་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར། དེ་གཙོ་བོ་ཡིན་པས་ཡ་མཚན་ཆེ་བ་དང་པོར་བརྗོད་པ་ཡིན་ནོ། །

[Block 5070]
ཚིགས་བཅད་འོག་མ་སྨོས་པ་ཡང་དེའི་ཁྱད་པར་དེ་འདིས་འབྲེལ་པ་ཡིན་པས་རྒྱུ་འབྲེལ་ལོ། །

[Block 5071]
རབ་ཏུ་འབྲེལ་པའི་རྒྱུ་འབྲེལ་ཆུང་གང་ཡིན་པ་དེ་ནི་རབ་ཏུ་མཛའ་བའི་རྒྱུ་འབྲེལ་ཆུང་ངུའོ། །

[Block 5072]
ཁུར་དེ་བསྐུར་བ༌[^3257]ཞེས་བྱ་བ་ནི་བདག་པོ་ཉིད་ཀྱི་དངོས་པོའོ། །

[Block 5073]
ཉེ་དུ་ཡིན་པས་གཉེན་ནོ། །

[Block 5074]
དེ་དང་འདྲ་བ་ཡིན་པས། གཉེན་དང་འདྲ་བར་གྱུར་པའོ།[^3258] །བློན་པོ་ལ་སོགས་པ་གང་ཡིན་པ་དེ་དག་ནི་བློན་པོ་ལ་སོགས་པའོ། །

[Block 5075]
གཉེན་དང་མཛའ་བོ་ཞེས་བྱ་བ་འདིས་ནི་བྱམས་པ་བསྟན་ཏོ། །

[Block 5076]
ཉམས་ཉེས༌[^3259]རབ་ཏུ་ཆེ་བ་དང་། །ཕོངས་ནས་མྱ་ངན་བྱེད་པ་ཞེས་བྱ་བ་ལ་ཉམས་ཉེས༌[^3260]པ༌[^3261]རབ་ཏུ་ཆེ་བ་ནི་རྒྱལ་པོའི་དཔུང་གི་ཚོགས་ཀྱིས་ཟིལ་གྱིས་མནན་པས་སོ། །

[Block 5077]
དེས་བྱས་པའི་ཕོངས་པ་ནི་ཉམས་ཉེས༌[^3262]རབ་ཏུ་ཆེར་བྱུང་བས་ཕོངས་པའོ། །

[Block 5078]
ཉམས་ཉེས༌[^3263]རབ་ཏུ་ཆེར་བྱུང་ཞིང་ཕོངས་པས་བྱས་པའི་མྱ་ངན་ནི་ཉམས་ཉེས༌[^3264]རབ་ཏུ་ཆེར་བྱུང་ཞིང་། ཕོངས་ནས་མྱ་ངན་བྱེད་པའོ། །

[Block 5079]
ཉམས་ཉེས༌[^3265]རབ་ཏུ་ཆེར་བྱུང་ཞིང་ཕོངས༌[^3266]ནས་མྱ་ངན་བྱེད་པ་དེ་ཉིད་ཀྱི་རྒྱུ་བསྟན་པའི་ཕྱིར། དེ་བས་གཞུ་རྣམས་བཀང་ནས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། དེ་བས་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར། སྡུག་བསྔལ་རབ་ཏུ་བྱུང་བ་ཉིད་དེ། དེའི་ཕྱིར། མདེའུ་རྩེ་མོ་རྣོན་པོ་དག་འཕེན་པ་རྣམས་ཀྱིས་འཇིགས་པ་གང་ཡིན་པ་དེ་དག་ལས་འཇིགས་པའི་སྒྲ་གང་ཡིན་པ་དེ་ནི་སྒྲ་འཇིགས་པའོ། །

[Block 5080]
སྒྲ༌[^3267]འཇིགས་པའི་གཞུ་རྒྱུད་གང་ཡིན་པ་དེ་ནི། གཞུ་རྒྱུད་སྒྲ་འཇིགས་སོ། །
--- END BLOCKS ---
