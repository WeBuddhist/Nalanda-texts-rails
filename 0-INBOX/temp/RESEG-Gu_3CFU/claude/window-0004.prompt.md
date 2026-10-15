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
[Block 141]
འོ་ན་འདི་ནི་སྡོམ་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་འདི་ལ་སྐྱབས་སུ་འགྲོ་བར་རྩོམ་པ་ཉིད་ཀྱི་དོན་ཅི་ཞིག་ཡིན་ཞེས་བྱ་བ་ཁ་ཅིག་སྨྲ་ན་དེ་ནི་ཡང་དག་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་རབ་ཏུ་བྱུང་བ་ཉིད་ཅེས་བྱ་བ་ནི་ངེས་པར་ཞུགས་པ་ཉིད་ཡོངས་སུ་དོར་བ་སྟེ། ཟག་པ་དང་བཅས་པའི་དངོས་པོ་ཐམས་ཅད་ལ་མངོན་པར་མི་དགའ་བ་དེ་ལ་ངེས་པར་ཞུགས་པའོ། །

[Block 142]
དེ་བས་ན་འཁོར་བ་ལ་རྒྱབ་ཏུ་ཕྱོགས་པ་ནི་ངེས་པར་ཞུགས་པ་ཡོངས་སུ་དོར་བ་མ་ལུས་པའོ། །

[Block 143]
མྱ་ངན་ལས་འདས་པ་ལ་བརྟེན་པ་མེད་པར་འཁོར་བ་ལ་རྒྱབ་ཀྱིས་ཕྱོགས་པ་གྲུབ་པ་མ་ཡིན་ཏེ། དེ་བས་ན་སྡོམ་པ་བཞིན་དུ་འདིར་ཡང་མྱ་ངན་ལས་འདས་པའི་བསམ་པ་རབ་ཏུ་བསྒྲུབ་པར་བྱའོ། །

[Block 144]
དེ་བས་ན་འདིར་ཡང་སྐྱབས་སུ་འགྲོ་བ་རྩོམ་པ་ཉིད་དོ། །

[Block 145]
ཁ་ཅིག་ནི་རབ་ཏུ་བྱུང་བ་ཉིད་ཉེ་བར་བླང་བའི་སྔགས་ལ་རབ་ཏུ་བྱུང་བ་ཉིད་ཀྱི་རྟགས་ཡང་དག་པར་བླང་བར་བགྱི་ཞེས་བྱ་བ་འདིའི་མདུན་དུ་བདག་ནི་དགེ་ཚུལ་དུ་མཁན་པོས་གཟུང་དུ་གསོལ་ཞེས་བྱ་བ་འདོན་པ་ཡིན་ནོ་ཞེ་ན། དེ་ནི་རིགས་པ་མ་ཡིན་ཏེ། རབ་ཏུ་སྐྱེས་པ་ལ་སླར་རབ་ཏུ་སྐྱེས་པ༌[^115]མེད་པ་ཉིད་ཀྱི་ཕྱིར་དང་། ཡང་དག་པར་བླངས་པ་ལ་ཡང་དག་པར་བླང་བ༌[^116]མི་འཐད་པའི་ཕྱིར་དང་། སློབ་དཔོན་གྱིས་སྔགས་ལ་ཡང་གདོན་པར་བྱ་བ་ཉིད་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 146]
དགེ་ཚུལ་ཉིད་དུ་སྒྲུབ་པར་བྱེད་པའི་སྔགས་ལ་རབ་ཏུ་བྱུང་བ་ཉིད་དུ་ཁས་བླངས་པ་ལ་ཡང་བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པ་དེ་ལ་ཇི་སྲིད་དུ་རབ་ཏུ་བྱུང་བ་ཉིད་ཀྱི་རྟགས་ཡང་དག་པར་ལེན་ཏོ། །

[Block 147]
དོན་གྱི་སླད་དུ་མཚན་ནས་བརྗོད་དེ་མཁན་པོ་འདི་ཞེས་བྱ་བས་མཁན་པོའི་མིང་གཟུང་ངོ་། །བདག་དགེ་ཚུལ་ཉིད་དུ་སློབ་དཔོན་གྱིས་གཟུང་དུ་གསོལ་ཞེས་པ་ནི་དེ་རྣམས་ཀྱི་འདོན་པ་ཡིན་ནོ། །

[Block 148]
དེ་ཡང་ཡང་དག་པར་བླངས་པ་མི་འཐད་པས་དེ་ཉིད་ཀྱི་ཕྱིར་མི་རིགས་སོ། །

[Block 149]
གསོལ་བའི་འོག་ཏུ་ཡང་རུང་ངོ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བ་ཉིད་ཉེ་བར་སྒྲུབ་པ་ཞེས་བྱ་བ་ལ་འཇུག་པའོ།[^117] །རུང་ངོའི་སྒྲ་ནི་འདོད་པ་རྣམས་རྣམ་པར་བརྟག་པའི༌[^118]དོན་དུའོ། །

[Block 150]
མཁན་པོ་ལ་སོགས་པའི༌[^119]རྗེས་ཉིད་ལ་སྐྲ་དང་ཁ་སྤུ་བྲེགས་པ་རབ་ཏུ་དབྱུང་བར་བྱ་ཞེས་བྱ་བ་ནི་ཁ་ཅིག་རྣམས་འདོན་ནོ། །

[Block 151]
དེ་རྣམས་ཀྱི་དགོངས་པ་ནི་འདི་ཡིན་ཏེ། ཇི་ལྟར་དགེ་ཚུལ་ཉིད་དེ་བཞིན་དུ་སྐྲ་བྲེགས་པ༌[^120]ལ་སོགས་པ་ཡང་རབ་ཏུ་བྱུང་བ་ཉིད་ཀྱི་ལུགས་ཏེ། དེ་བས་ན་དེ་འདོན་པའི་རྣམ་པར་རྟོག་པ་ཉེ་བར་འབྲེལ་པའོ། །

[Block 152]
དེ་བཞིན་དུ་མཁན་པོས་དེ་དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་སྒྲུབ་པར་བྱེད་པའི་དགེ་སློང་ལ་གཏད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་ལས༌[^121]དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་སྒྲུབ་པར་བྱེད་པ་དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་བསྒྲུབ་པའི་ཕྱིར་ངང་ཚུལ་འདི་ལ་ཡོད་པས་ན༌[^122]དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་བསྒྲུབ་པའོ། །

[Block 153]
གང་ཞིག་འདི་ལ་དགེ་ཚུལ་གྱི་སྡོམ་པ་ཉེ་བར་སྒྲུབ་པ་ལ་མངོན་པར་ཤེས་པའི་སླད་དུའོ། །

[Block 154]
སེམས་ཀྱིས༌[^123]རབ་ཏུ་ཕྱེ་བ་ཉིད་འདིར་དེའི་ངང་ཚུལ་ཉིད་ཀྱིས་བརྟེན་པར་རིག་པར་བྱའོ། །

[Block 155]
གང་ལ་ཉེ་བར་བསྒྲུབ་པའི་དོན་དུ་འདི་གཏད་པར་བྱའོ།[^124] །ཅི་ཡོངས་སུ་དག་གམ་ཞེས་དྲིས་ནས་དག་ན་ཉེ་བར་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་སྟེ། དེ་ནི་སློབ་དཔོན་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་བསྒྲུབ་པ༌[^125]དེ་ནི་སློབ་དཔོན་དུ་བལྟ་བར་བྱའོ། །

[Block 156]
གསང་སྟེ་སྟོན་པ་དང་། ལས་བྱེད་པ་དང་། གནས་སྦྱིན་པ་དང་། ཀློག་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སློབ་དཔོན་རྣམས་ཞེས་བྱ་བའི་བསྡུས་པའི་དོན་ནི་ཡང་གི་སྒྲའོ། །

[Block 157]
ཅི་ཙམ་གྱིས་སློབ་དཔོན་ཉིད་འདི་རྣམས་ལ་ཤེས་པ་ཉིད་ཅེ་ན། དོན་གྲུབ་ན་གྱུར་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨྲས་ཏེ། དོན་གང་ཞིག་གིས་སྔགས་ལ་རྣམ་པར་གཞག་པ་འདི་ལྟ་སྟེ། དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་བསྒྲུབ་པའི་དོན་གྱིས་དགེ་ཚུལ་ཉིད་ཀྱི་སློབ་དཔོན་ཉིད་ལའོ། །

[Block 158]
དེ་གྲུབ་པ་ནི་དོན་ངེས་པ་ལ་སློབ་དཔོན་ཉིད་ལ་སོགས་པར༌[^126]གྱུར་པ་དེ་ལའོ། །

[Block 159]
གྲུབ་པ་ཉིད་ནི་སྐྱེ་བ་ཉིད་དོ། །

[Block 160]
དེ་བས་ན་ཉེ་བར་སྒྲུབ་པ་ལ་སོགས༌[^127]པ་གྲུབ་པ་རྣམས་ལ་སློབ་དཔོན་ཉིད་འདི་རྣམས་ལ་སྐྱེ་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 161]
དོན་གང་ཞིག་གིས་འདི་མཁན་པོ་ཡིན་པ་མཁན་པོ་ཉིད་ལ་ཡང་དེ་ངེས་པའི་དོན་ལ་ཅི་ཞིག་སྐྱེས་པ་ཉིད་ཅེས་བྱ་བ་མཁན་པོར་གསོལ་བ་ཁས་བླངས་པ་ནི༌[^128]དེར་གྱུར་ཏོ་ཞེས་བྱ་བ་སྨྲས་ཏེ། གསོལ་བའི་དུས་མཁན་པོར༌[^129]ཁས་བླངས་པ་གང་ཞིག་དེ་ལ་མཁན་པོ་ཉིད་དུ་གྱུར་ཏོ། །

[Block 162]
རབ་ཏུ་བྱུང་བ་ཉིད་ཉེ་བར་བསྒྲུབ་པའམ། བསྙེན་པར་རྫོགས་པའི་མཚན་ཉིད་ཅན་གྱི་དོན་དུ་བསྒྲུབ་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 163]
དོན་གང་ཞིག་གྲུབ་པས་སློབ་དཔོན་ཉིད་དང་མཁན་པོ་ཉིད༌[^130]སྐྱེ་བའི༌[^131]དོན་དུ༌[^132]དེ་ལ་གང་གི་ཚེ་གྲུབ་པ་ཉིད་ཅེས་བྱ་བ་བརྗོད་པ་ཐ་མ་གང་ཡིན་པའི་ཆ་གསུམ་པ་ལ་གྲུབ་པ༌[^133]ཉིད་དུ་ཞེས་བྱ་བ་སྨྲས་ཏེ། བརྗོད་པ་གང་ཞིག་ལ་དོན་དེ་གང་ཡིན་པའི་ཆ་སློབ་དཔོན་ཉིད་ལ་སོགས་པ་རྣམས་གྲུབ་པ་ཉིད་དུ་དེ་ནི་བརྗོད་པ་སྟེ། དེའི་ཆ་ལ་དོན་གྲུབ་པ་ཉིད་དེ་བརྗོད་པ་དེ་རྣམས་ཀྱང་གསུམ་ཡིན་ཏེ། དེ་ལ་བརྗོད་པ་གང་ཚིག་ལས༌[^134]བརྗོད་པའི་ཆ་ཇི་ཙམ༌[^135]པ་ལས༌[^136]ཞེས་བྱ་བ་ཤེས་པ་མ་ཡིན་ཏེ། དེ་ལ་འདི་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་ཐ་མ་ཡིན་ཏེ་ཕྱི་མ་ལའོ། །

[Block 164]
དེའི་བརྗོད་པ་ཡིན་པ་དེའི་ཆ་གསུམ་པ་གང་ཞིག་དེ་ལ་གྲུབ་པ་ཉིད་དོན་དེ་ལ་ཤེས་པར་བྱའོ། །

[Block 165]
དཔེ་ཉིད་ཀྱིས་དོན་དེ་རབ་ཏུ་གྲུབ་པར་བྱེད་པ་དཔེར་ན་གཞན་བརྗོད་པའི་དུས་ན་དགེ་ཚུལ་ཉིད་བཞིན་ནོ་ཞེས་བྱ་བ་སྟེ། གཞན་ནི་ཉེ་བར་སྒྲུབ་པ༌[^137]པོའི་བརྗོད་པའི་དུས་ནའོ། །

[Block 166]
བདག་དགེ་ཚུལ་འདི་ཞེས་བྱ་བ་འདི་ལས་ཕ་རོལ་དུ་སློབ་དཔོན་ཞེས་བྱ་བ་གང་ཞིག་གཞན་བརྗོད་པ་དེར་དགེ་ཚུལ་འདི་བྱེད་པ་པོ་ཉེ་བར་བསྒྲུབ་པ་པོའི་དོན་གང་ཞིག་དགེ་ཚུལ་གྱི་སྡོམ་པ་ཞེས་བྱ་བ་དེའི་གྲུབ་པ་ཉིད་ཤེས་པར་བྱའོ། །

[Block 167]
སློབ་དཔོན་གྱིས༌[^138]གཟུང་དུ་གསོལ་ཞེས་བྱ་བ་འདིར་ཤེས་པར་བྱའི།[^139] བཙུན་པས་གཟུང་དུ་གསོལ་ཞེས་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 168]
འདིར་ཐ་མ་ལ་མཁན་པོའི་དོན་ཏོ་ཞེས་བྱ་བ་ནི་གྲུབ་པ་ཉིད་ཅེས་བྱ་བ་འཇུག་པ་ཡིན་ནོ། །

[Block 169]
འདིར་ཞེས་བྱ་བ་ནི་གཞན་གྱིས་བརྗོད་པའི་དུས་ནའོ། །

[Block 170]
མཁན་པོ་ལ་གསོལ་བ་གདབ་པ་ལ་དགོངས་སུ་གསོལ་ཞེས་བྱ་བའི་སྒྲ་ལས་དགེ་སློང་དང་འབྲེལ་པ་བརྗོད་པས་ཕྱི་མ་མང་པོ་མཁན་པོས་བརྗོད་པ་རྣམས་སོ། །

[Block 171]
དེ་ལ་གང་ཞིག་གསུམ་པ་བརྗོད་པ་མཁན་པོས་རབ་ཏུ་དབྱུང་བར་བགྱི་བ་འམ། བསྙེན་པར་རྫོགས་པར་བགྱི་ཞེས་བྱ་བ་འདི་ལས་སྔོན་དུ་གང་ཞིག་དེའི་དུས་ལ་མཁན་པོའི་དོན་དེ་ཁས་ལེན་པའི་བདག་ཉིད་ལ་གྲུབ་པ་ཉིད་དོ། །

[Block 172]
དུས་ཉིད་དུ་རབ་ཏུ་བྱུང་བ་ལ་མཁན་པོས་ཞེས་བྱ་བ་བརྗོད་པར་བྱའོ། །

[Block 173]
བསྙེན་པར་རྫོགས་པ་ལ་ནི་གལ་ཏེ་དང་པོ་ཉིད་དུ་སློབ་དཔོན་མེད་པ་ཡིན་ན་སློབ་དཔོན་གྱིས་ནི་མ་ཡིན་པ་འམ། བཙུན་པ་ཞེས་བྱ་བ་བར་དུ་གཅོད་པ་མེད་པ་ཉིད་ཀྱིས་འདིར་ཆ་གསུམ་པར་རིག་པར༌[^140]བྱའོ། །

[Block 174]
ཡི་གེའི་ཚད་ཀྱིས་ནི་མ་ཡིན་ཏེ། དེ་ལྟར་ན་མཁན་པོར་གསོལ་བ་གདབ་པ་ལ་བར་དུ་གཅོད་པ་གསུམ་འབྱུང་བ་ཡིན་ཏེ། བདག་མིང་འདི་ཞེས་བགྱི་བ་བཙུན་པ་ལ་མཁན་པོར་གསོལ་བར་བགྱིའོ། །

[Block 175]
བཙུན་པ་བདག་གིས༌[^141]མཁན་པོ་མཛོད་ཅིག་བཙུན་པ་མཁན་པོས་རབ་ཏུ་བྱུང་བའམ་བསྙེན་པར་རྫོགས་པར་འགྱུར་བར་བགྱིའོ་ཞེས་བྱ་བའོ། །

[Block 176]
དགེ་ཚུལ་ཉིད་དུ་ཁས་བླངས་པ་ལ་རྒྱུན་དང་རབ་ཏུ་ཆད་པ་དག་སྐྱབས་སུ་འགྲོ་བ་དང༌[^142]དགེ་ཚུལ་ཉིད་དུ་ཁས་ལེན་པའོ། །

[Block 177]
དེ་ལ་ཐ་མ་རབ་ཏུ་ཆད་པ་ནི་དོན་གཞན་ལ་རྗེས་སུ་འགྲོ་བ་སྟེ། བདག་དགེ་ཚུལ་ཞེས་བྱ་བར་སློབ་དཔོན་གྱིས་གཟུང་དུ་གསོལ་ཞེས་བྱ་བ་རྣམ་པ་གཉིས་སུ་བྱས་ཏེ། [^143]གསུམ་ཉིད་དུ་ངེས་པ་ཡིན་ནོ། །

[Block 178]
བརྗོད་པ་མ་རྫོགས་པ་ཉིད་ལ་ཅིའི་ཕྱིར་ཆ་གསུམ་པ་ལ་འདི་ལ་འཇུག་པ་ལ་གྲུབ་པ་ཉིད་འབྱུང་བ་ཡིན་ཏེ། གང་ཞིག་སླར་བྱས་སོ་ཞེས་བྱ་བ་སྟེ། མཚམས་གཅད་པ༌[^144]ལ་སོགས་པ་ཐམས་ཅད་ལ་ཆོ་ག་འདི་བལྟ་བར་བྱའོ། །

[Block 179]
དེ་ལྟར་ན་གསང་སྟེ་སྟོན་པ་ལས༌[^145]གསང་སྟེ་བསྟན་པ་མ་རྫོགས་པ་ལ་སློབ་དཔོན་ཉིད་དང་། དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་སྒྲུབ་པའི་དུས་འདི་ལ་ལས་བྱེད་པ་འདི་ལྟ་བུ་ཞེས་བྱ་བས་སོ། །

[Block 180]
གནས་སྦྱིན་པ་དང་ཀློག་པ་པོ་དག་ལ་དུས་གང་གི་ཚེ་ན་ཞེས་བྱ་བ་ཤེས་པ་མ་ཡིན་ཏེ། གནས་སྦྱིན་པ་དང་ཀློག་པ་པོ་དག་གི་ཚད་ལ་མི་གནས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །
--- END BLOCKS ---
