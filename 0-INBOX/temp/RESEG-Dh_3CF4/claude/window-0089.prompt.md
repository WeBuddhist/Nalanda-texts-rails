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
[Block 3116 [HEADING]]
## བྱ་སྲེག་པའི་ཕྲུ་གུའི་སྐྱེས་པའི་རབས། ^17-0

[Block 3117]
བརྩོན་པར་བྱ་བ་ནི་གོམས་པར་བྱའོ།[^1982] །མི་ནུས་པ་ནི་སྤྲོ་བ་མེད་པའོ། །

[Block 3118]
སྒོ་ངའི་སྦུབས་ནས་བྱུང་ནས་ཞག་གྲངས་མང་པོ་མ་ལོན་པ་གང་ཡིན་པ་སྟེ། འདིས་ན་ཚོད་བསྟན་ཏོ། །

[Block 3119]
སྤུ་སར་པ་གདོད་སྐྱེ་བ་གང་ཡིན་པ་དེས་ནི་འགྲོ་བའི་བྱ་བ་མི་ནུས་པ་བསྟན་ཏོ། །

[Block 3120]
རབ་ཏུ་རིད་པས་ཞེས་བྱ་བ་ཡང་འགྲོ་མི་ནུས་པའི་རྒྱུ་ཉིད་དེ། འདབ་གཤོག་རྣམས་ཀྱང་རྒྱས་ཞེས་བྱ་བ་ནི་འཕུར་དུ་རུང་བའི་གཤོག་པ་ཡོད་པས་སོ། །

[Block 3121]
ཐམས་ཅད་ཟ་ཞིང་ཞེས་བྱ་བ་ནི་ཁ་ཟས་ཅི་ཡང་རུང་བ་ཟ་བ་སྟེ། དེས་ན་མི་འཆི་ཞིང་བརྟས་པར་འགྱུར་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་གསུངས་པ།

[Block 3122 [VERSE]]
བརྐམ་ཞིང་བྱ་རོག་ལྟར་དཔའ་བ། །
ངོ་ཚ་མེད་པ་ལེགས་པར་འཚོ། །
བརྣབ་ཅིང་སྤྱི་བརྟོལ་ཆེ་བ་ཡི། །
འཚོ་བ་ཤིན་ཏུ་ཉོན་མོངས་ལྡན། །

[Block 3123]
ཞེས་བྱ་བ་ནི་ཆོས་མ་ཡིན་པ་བྱེད་པའོ། །

[Block 3124 [VERSE]]
རྟག་ཏུ་སྐྱོན་མེད་འཚོལ་བ༌[^1983]དང་། །
ཞུམ་ཞིང་བག་དང་ཆས་པ་དང་། །
འཚོ་བ་སྐྱོན་མེད་ལྟ་བ་དང་། །
ངོ་ཚ་ཤེས་པའི་འཚོ་མི་བདེ། །

[Block 3125]
ཆོས་དང་ལྡན་པས་ཆོས་ཤེས་པའི་ཕྱིར་རོ། །

[Block 3126]
གར་གྱི་ཁྱད་པར་མཛེས་པ་ཡིན་པས་གར་མཛེས་པའོ། །

[Block 3127]
མིང་དོན་མེད་པ་གང་ཡིན་པ་དེ་ནི་མིང་དོན་མེད་པའོ། །

[Block 3128]
མིང་དོན་མེད་པའི་རྐང་པ་གང་ཡིན་པ་དེ་ནི་རྐང་པ་མིང་དོན་མེད་པའོ། །

[Block 3129]
རྐང་པ་ནི་འགྲོ་བར་བྱེད་པས་ན་རྐང་པ་སྟེ། དེའི་ནུས་པ་མེད་པའི་ཕྱིར་མིང་དོན་མེད་པ་ཉིད་དེ། འདིས་ནི་འགྲོ་བར་མི་ནུས་པའོ། །

[Block 3130]
བདག་གི་རྐང་པ་མིང་དོན་མེད་པ་དང་། འདབ་མ་མེད་པ་འདི་གཉིས་ཀྱིས་འགྲོ་བར་མི་ནུས་པར་བསྟན་ཏོ། །

[Block 3131]
ཕ་མ་གཉིས་ཀྱང་ཞེས་བྱ་བ་ནི། ཕ་དང་མ་གཉིས་སོ། །

[Block 3132]
བྱེར་ཞེས་བྱ་བ་ནི་ཡུལ་གཞན་དུ་སོང་བ་སྟེ། འདིས་ནི་བྲལ་བར་སྟོན་ཏོ། །

[Block 3133]
བདག་ཀྱང་རེ་ཞིག་འདི་ལྟ་བུའི་གནས་སུ་གྱུར་པ་སྟེ། ཁྱོད་ལ་མགྲོན༌[^1984]བྱར་རུང་བ་ཅི་ཡང་མེད། །ཅེས་བྱ་བ་འདིས་ནི་ཁྱོད་ཀྱི༌[^1985]འོང་བ་ཡང་རྒྱུ་མེད་པ་ཡིན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 3134]
[^1986]དེ་བས་ན་ཞེས་བྱ་བ་ནི༌[^1987]རྒྱུ་དེ་གཉིས་ནའོ། །

[Block 3135]
རྒྱ་མཚོ་ཞེས་བྱ་བ་དང་། བདག་ལ་ཕན་པར་འདོད་པ་ཞེས་བྱ་བ་གཉིས་ཀྱིས་ནི་དཔེ་སྨོས་པ་ཡིན་ཏེ། སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པའི་དཔེ་རྣམ་པ་གཉིས་བསྟན་ཏེ། དེ་དང་རིགས་མི་མཐུན་པ་དཔེར་རབ་ཏུ་གྲགས་པས་ཆོས་མཐུན་པའི་དཔེ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3136]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་བྱ་སྲེག་པའི་ཕྲུ་གུའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 3137 [HEADING]]
## བུམ་པའི་སྐྱེས་པའི་རབས། ^18-0

[Block 3138]
ཉེས་པ་དུ་མ་འབྱུང་བ་ཞེས་བྱ་བ་ནི་ཉེས་པ་དུ་མ་བསྐྱེད་པའི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3139]
ཤིན་ཏུ་མ་རུང་བར་གྱུར་པའི༌[^1988]ཕྱིར་ཞེས་བྱ་བ་ནི་གནོད་པ་སྟེ། གཞན་དག་པས་ཤིན་ཏུ་སྡིག་པར་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3140]
དགེ་བ་རྣམས་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 3141]
སྙིང་རྗེ་ཆེན་པོས་ཡོངས་སུ་བསྒོས་པའི་བློ་ཞེས་བྱ་བ་ནི་སྙིང་རྗེ་ཆེན་པོས་སྦགས་པ་སྟེ། འདིས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 3142]
གཞན་ལ་ཕན་ཞིང་བདེ་བ་བྱེད་པ་ལ་དགའ་བ་ཞེས་བྱ་བ་འདིས་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 3143]
བསོད་ནམས་སྤེལ་བ་ཉམས་སུ་ལེན་པ་ཞེས་བྱ་བ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་སྤེལ་ཞིང་སྒྲོགས་པའོ། །

[Block 3144]
སྦྱིན་པ་དང་དུལ་བ་དང་ཞི་བ་ཞེས་བྱ་བས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གསུམ་བསྟན་ཏེ། [^1989]སྦྱིན་པས་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 3145]
དུལ་བས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 3146]
ཞི་བ་ནི་ཁྲོ་བ་ཉེ་བར་ཞི་བའི་མཚན་ཉིད་དེ། བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 3147]
སོགས་པ་སྨོས་པས་ནི་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏེ། [^1990]བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་གཉི་ག་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3148]
ཕུན་སུམ་ཚོགས་ཀྱང་ཞེས་བྱ་བ་ནི་ལྷའི་དབང་པོའི་གོ་འཕང་ཐོབ་སྟེ་ལོངས་སྤྱོད་ཅི་འདོད་པ་དང་ལྡན་པར་གྱུར་ཀྱང་ངོ་། །སྙིང་རྗེའི་དབང་དུ་གྱུར་པས་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 3149]
འཇིག་རྟེན་གྱི་དོན་ལ་བརྩོན་པ་ལྷོད་པར་མ་གྱུར༌[^1991]ཏོ་ཞེས་བྱ་བ༌[^1992]ནི་སྔར་བསྟན་པའི་སྦྱོར་བ༌[^1993]ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 3150]
དཔལ་དང་ལྡན་པ་ཉིད་ཆང་ཡིན་པས་དཔལ་ལྡན་ཆང་གི༌[^1994]ཞེས་པའོ། །

[Block 3151]
དེས་མྱོས་པ་ནི་དཔལ་ལྡན་ཆང་གིས་མྱོས་བཞིན་ནའོ། །

[Block 3152]
དཔལ་དང་ལྡན་པ་ཆང་གིས་སེམས༌[^1995]ཡོངས་སུ་དཀྲུགས་ཏེ་བདག་གི་དོན་ཡང་འདོར་བ་ནི་བག་མེད་པའོ། །

[Block 3153]
བག་ཡོད་རྣམས་ནི་ཞེས་བྱ་བ་ནི་བག་དང་ལྡན་པ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་དང་གཞན་གྱི་དོན་དུའོ། །

[Block 3154]
བག་ཡོད་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། སྡུག་བསྔལ་མང་པོས་གདུངས་པའི་སེམས་ཅན་ལ། །ཞེས་སྨོས་ཏེ། འདིའི་བསྡུས་པའི་དོན་ནི་སྙིང་རྗེ་དང་། བརྟན་པ་དང་ཤེས་རབ་ཀྱི་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱིར་གཞན་གྱི་དོན་སྤྱོད་པ་ཡོངས་སུ་མི་བརྗོད༌[^1996]པའོ། །

[Block 3155]
སེམས་ཅན་ལ་བརྩེ་ཞིང་རང་གི་བདེ་བ་ལ་མ་ཆགས་པ་དང་། བརྟན་པ་ལ་གནས་པའི་སྤྱོད་པ་དང་། ཤེས་རབ་ཀྱི་རང་བཞིན་ཤེས་པས་སོ། །
--- END BLOCKS ---
