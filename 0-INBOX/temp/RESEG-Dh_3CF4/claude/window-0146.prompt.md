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
[Block 5111]
ཆོས་འཕེལ་བར་བྱས་ན་ནི། བདེ་བ་གཉིས་དང་ལྡན་པར་འགྱུར་ཏེ། གྲགས་པ་འཕེལ་བ་དང་། སྲིད་འཕེལ་བའོ། །

[Block 5112]
འདི་ནི་འདིར་བདེ་བའོ། །

[Block 5113]
ཡང་ན་གཉི་ག་ལ་ཡང་བདེ་བར་འགྱུར་བའོ། །

[Block 5114]
སློབ་དཔོན་དཔའ་བོས༌[^3292]མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་སྤྲེའུའི་རྒྱལ་པོའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 5115 [HEADING]]
## བཟོད་པར་སྨྲ་བའི་སྐྱེས་པའི་རབས། ^30-0

[Block 5116]
བཟོད་པ་ལ་གོམས་པ་ཞེས་བྱ་བ་ནི། སྐུ་ཚེ་སྔ་མ་དག་ཏུ་བཟོད་པའི་རྒྱུ་བསྒོམས་པར་བསྟན་ཏོ། །

[Block 5117]
སྨྲས་པ། སོ་སོར་བརྟགས་ཏེ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོ་སོར་བརྟགས་པའི་རྐྱེན་གྱིས་སོ། །

[Block 5118]
ཡང་ན་བཟོད་པ་ལ་གོམས༌[^3293]པ་ཞེས་བྱ་བ་ན། [^3294]བསྒོམས་པ་ལས་བྱུང་བའི་བཟོད་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་སྨྲས་པའོ། །

[Block 5119]
ཁྱིམ་ན་གནས་པ་ནི་ཉེས་པ་མང་པོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐང་གིས་བསྟན་ཏོ། །

[Block 5120]
ཁྱིམ་ན་གནས་པ་ནི་སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པ༌[^3295]དང་། ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པ་དང་། ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པ་ཉིད་དང་ལྡན་པར་བསྟན་པ་སྟེ། དེ་ལས་ཉེས་པ་མང་པོའི་སྡུག་བསྔལ་དང་ལྡན་ཞེས་བྱ་བ་འདིས་ནི། མཐོང་བའི་ཆོས་ལ་སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5121]
སྲིད་དང་འདོད་པ་ལྷུར་ལེན་པས་ཉེ་བར་མ་ཞི་བ་ཞེས་བྱ་བ་འདིས་ནི། ཡུན་རིང་བོར་ཡང་སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5122]
འདོད་ཆགས་དང་། ཞེ་སྡང་ལ་སོགས་པས་ནི་ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5123]
ཉོན་མོངས་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། མཐོང་བས་སྤང་བར་བྱ་བ་དང་བསྒོམ་པས༌[^3296]སྤང་པར་བྱ་བ་སྟེ། དེས་ཀུན་ནས་ཉོན་མོངས་པ་ཉིད་དུ་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 5124]
བྱ་བ་ངན་པའི་སྐལ་བས་ཆོས་བྱ་བའི་གོ་སྐབས་མེད་པར་ཤེས་པ་ཞེས་བྱ་བ་འདིས་ནི་ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པ༌[^3297]ཉིད་དུ་བསྟན་ཏོ། །

[Block 5125]
ཉེས་པ་དེ་ལྟ་བུ་མེད་པའི་བདེ་བ་ཅན་དུ་ཞེས་བྱ་བ་ནི་ཀུན་ནས་ཉོན་མོངས་པ་དེ་ལྟ་བུ་མེད་པའི་བར་རོ། །

[Block 5126]
ཚུལ་ཁྲིམས་ཞེས་སྨོས་པས་ནི། ལྷག་པའི་ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་བསྟན་ཏོ། །

[Block 5127]
མང་དུ་ཐོས་པ་ཞེས་སྨོས་པས་ནི་ལྷག་པའི་ཤེས་རབ་བསྟན་ཏོ། །

[Block 5128]
རབ་ཏུ་ཞི་བ་སྨོས་པས་ལྷག་པའི་སེམས་སོ། །

[Block 5129]
རྒྱུ་གསུམ་གྱིས་བཟོད་པ་སྨྲ་བ་ཞེས་བྱ་བར་མིང་དུ་བཏགས་ཏེ། དེ་བཟོད་པར་བྱ་བའི་ཡིད་དམ་མ་ཉམས་ཤིང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཡིད་དམ་བཅས་པ་ཡང་ཚིག་གིས་བཅད་པ༌[^3298]ཡིན་པའི་ཕྱིར་དེ་བས་ན་བཟོད་པ་སྨྲ་བ་ཞེས་བྱའོ། །

[Block 5130]
དེའི་བསྔགས་པ་བརྗོད་པ་དང་། གཞན་དག་ལ་དེ་དང་མཐུན་བའི་ཆོས་འཆད་པ་ཡང་དེ་ཉིད་དེ། བཟོད་པ་སྨྲ་བར་བདག་ཉིད་ཀྱིས་ཁས་བླངས་པ་དང་། བཟོད་པའི་ཡོན་ཏན་བརྗོད་པ་དང་། གཞན་ལ་བཟོད་པ་སྨྲ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5131]
དེ་ལ་དཀའ་ཐུབ་ཕུན་སུམ་ཚོགས། །ཞེས་བྱ་བའི་མིང་ནི་བཟོད་བ་བྱ་བར་ཡིད་དམ་བཅས་པ་མ་ཉམས་པའི་ཕྱིར་རོ། །

[Block 5132]
མཐུ་རྩལ་ཅན་ཞེས་བྱ་བ་ནི་བཟོད་པའི་བསྔགས་པ་བརྗོད་པ་དང་། གཞན་དག་ལ་དེ་དང་མཐུན་པའི་ཆོས་འཆད་པའི་ཕྱིར་རོ། །

[Block 5133]
དེ་ལ་རེ་ཞིག་བདག་ནི་བཟོད་པའི་ཡི༌[^3299]དམ་བཅས་བ་མ་ཉམས་པས་བཟོད་པ་སྨྲ་བ་ཞེས་བྱ་བ་ནི་རིགས་ན། ཅིའི་ཕྱིར་བཟོད་པའི་བསྔགས་པ་རྗོད་པར༌[^3300]བྱེད་པ་དང་། དེ་དང་རྗེས་སུ་མཐུན་པའི་ཆོས་འཆད་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། དེ་ནི་བཟོད་བའི་ཡོན་ཏན་མཐུ་ཤེས་ནས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། དེ་ནི་བཟོད་པའི་ཡོན་ཏན་མཐུ་ཤེས་ནས། །ཞེས་བྱ་བ་ནི་བཟོད་པའི་བསྔགས་པ་བརྗོད་པའི་རྒྱུས་སོ། །

[Block 5134]
དེ་ཡིས་བདག་བཞིན་འཇིག་རྟེན་རབ་ཏུ་བརྒྱན།[^3301] །ཞེས་བྱ་བ་ནི། དེ་དང་རྗེས་སུ་མཐུན་པའི་ཆོས་གོ་རིམས་བཞིན་དུ་འཆད། །ཞེས་བྱ་བའི་རྒྱུས་སོ། །

[Block 5135]
བཟོད་པའི་གཏམ་ཡང་རྒྱུན་དུ་བྱེད་པར་གྱུར། །ཅེས་བྱ་བ་ལ་གཏམ་རྒྱུན་དུ་བྱེད་པ་ནི་རྣམ་པ༌[^3302]གཉིས་སོ། །

[Block 5136]
བཟོད་པ་ཆེན་པོ་རང་གི་ངང་དུ་གྱུར། །ཅེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། སྔར་བསྟན་པའི་དོན་འདིས་བསྡུ་ཞིང་རིག་པར་བསྟན་པའི་ཕྱིར་ཏེ། བཟོད་པ་ཆེན་པོ་རང་གི༌[^3303]ངང་དུ་གྱུར། །ཅེས་བྱ་བ་འདིས་ནི། གང་སྔར་བསྟན་པའི་བཟོད་པར་བྱ་བའི་ཡིད་དམ་མ་ཉམས་པ་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་ཏོ། །

[Block 5137]
དེ་ཡི་དོན་དང་མཐུན་པའི་གཏམ་དག་གིས། །ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་བཟོད་པའི་བསྔགས་པ་རྗོད་པར༌[^3304]བྱེད་ལ། དེ་ལ་མཐུན་པའི་ཆོས་ཀྱང་རྒྱུན་དུ་འཆད། །ཅེས་བྱ་བ་དེ་སྟོན་ཏོ། །

[Block 5138]
རབ་ཏུ་དབེན་པ་དང་། ཉམས་དགའ་བ་ནི་རབ་ཏུ་དབེན་ཞིང་ཉམས་དགའ་བའོ། །

[Block 5139]
དུས་ཐམས་ཅད་དུ་རྙེད་པར་སླ་བའི་མེ་ཏོག་དང་། འབྲས་བུ་གང་ན་ཡོད་པ་དེ་ནི། མེ་ཏོག་དང་། འབྲས་བུ་དུས་ཐམས་ཅད་དུ་རྙེད་སླ༌[^3305]བའོ། །

[Block 5140]
སྐྱེད་མོས་ཚལ་ཉིད་དགའ་ཞིང་མཛེས་པ་གང་ཡིན་པ་དེ་ནི་སྐྱེད་མོས་ཚལ་ཉམས་དགའ་བ་ཤིན་ཏུ་མཛེས་པ་དེའོ། །

[Block 5141]
བཀྲ་ཤིས་པ་ནི་ཐོས་པའི་ཆོས་ལ་འདོད་པའི་འབྲས་བུ་སྟེར་བའི་ཕྱིར་རོ། །

[Block 5142]
ཡིད་དུ་འོང་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཡིད་ཀྱི་དྲི་མ་སེལ་བའི་ཕྱིར་རོ། །

[Block 5143]
རྟེན་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་མི་འདོད་པའི་འབྲས་བུ་སྨིན་པར་བྱེད་པའི་སྡིག་པ་འཁྲུ་བའི་ཕྱིར་རོ། །

[Block 5144]
དཀའ་ཐུབ་ཀྱི་ཚལ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཡིད་དུ་འོང་བའི་འབྲས་བུའི་རྒྱུ་དགེ་བ་སྐྱེ་བའི༌[^3306]གཞི་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5145]
སྐྱེད་མོས་ཚལ་གྱི༌[^3307]ཡོན་ཏན་པས་ཁྱད་པར་དུ་གྱུར་པ་ནི། སྐྱེད་མོས་ཚལ་གྱི་ཡོན་ཏན་བས་ལྷག་བའོ། །

[Block 5146]
དེའི་གནས་སུ་གྱུར་པ་ནི་སྐྱེད་མོས་ཚལ༌[^3308]གྱི་ཡོན་ཏན་བས་ཀྱང་ལྷག་པའི་གནས་སུ་གྱུར་པའོ། །

[Block 5147]
འཁྲིད་ཤིང༌[^3309]འཁྱིལ༌[^3310]པས་གཏིབས་པ་ཞེས་བྱ་བ་ནི། གྲང་ཕ་སེལ་བར་བྱེད་པ་སྟེ། ལྡིང་ཁང་ནི་བསིལ་བའོ། །

[Block 5148 [VERSE]]
མེ་ཏོག་རྒྱས་པའི་ལྗོན་ཤིང་དགོད་པ་བཞིན། །
པདྨ་རབ་ཏུ་རྒྱས་པའི་མཚོ་འགྲམ་ན། །
ཞེས་བྱ་བས་ནི་ཚ་བ་བཙལ་བས༌[^3311]སོ། །
གཞལ་མེད་ཁང་ལ་ལྟ་བས་ཆགས་གྱུར་བ། །

[Block 5149]
ཞེས་བྱ་བ་ནི་དུས་དྲོ་བའི་ཕྱིར་དང་། གཞལ་མེད་ཁང་རབ་ཏུ་མཛེས་པའི་ཕྱིར་རོ། །

[Block 5150]
པདྨའི་མཚོ་ཞེས་བྱ་བ་ལ་པདྨའི་མཚོ་ནི་གྲང་པའི་ཕྱིར་ཏེ། དུས་ནི་དྲོ་བ་ཉིད་ཀྱིས་བུང་བ་དང་རད་པ་བཞིན་དུ་མེ་ཏོག་ཤིང་ལ་ཞེས་པ༌[^3312]ནི་མེ་ཏོག་ལ་ལྷག་པར་ཆགས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
