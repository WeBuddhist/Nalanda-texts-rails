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
[Block 4376]
རིན་པོ་ཆེ་ལ་ཡང་ཁས་ལེན་པ་ཉིད་ཐམས་ཅད་དུ་བྱ་བ་བསྒྲུབ་པ་ལ་སྒྲིབ༌[^2993]བྱེད་དུ་གྱུར་པ་གཞི་བྱེད་པ་ལྷག་མ་ལ་ཡང་ཐོབ་པར་བྱེད་པ་པོ་རུང་བ༌[^2994]ལ་སོགས་པ་ཐམས་ཅད་ལ་འདི་རྣམ་པར་གཞག་པས་སོ། །

[Block 4377]
སྙད་གདགས་སུ་མི་རུང་བ་ལ་ནི་ན་སྨད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྙད་གདགས་སུ་མི་རུང་བ་ནི་ཉོ་ཚོང་བྱར་མི་རུང་བ་སྟེ། དེ་ལ་རེག་པ་ལ་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4378]
འོག་མ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི༌[^2995]ཐ་སྙད་རྫོགས་པའི་བསླབ་པའི་གཞི་ལ་ཡང་ན་སྨད་པ་ཉིད་འདི་སྙད་གདགས་སུ་མི་རུང་བ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4379]
སྙད་གདགས་སུ་མི་རུང་བ་ཞེས་བྱ་བ་དེ་ཇི་ལྟ་བུ་ཞིག་ཡིན་པར་རིག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དེ་ནི་གས་པ་དང་ཆག་པ་དང་དུམ་བུ་དང་ཚིག་པ་དང་སྔོན་མ་སྤྱད་པ་དང་མ་བྱས་པ་དང༌[^2996]མཚན་དང་མི་ལྡན་པ་དང་བཅོས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ནི་ཞེས་བྱ་བ་ནི་སྙད་གདགས་སུ་མི་རུང་བའོ། །

[Block 4380]
གས་པ་ཉིད་དང་ཆག་པ་ཉིད་དང་ཞེས་བྱ་བ་ནི་སེར་ག་བྱུང་བ་སྟེ། འབྱར་ཀྱང་རུང་མ་འབྱར་ཀྱང་རུང་བ་དང་བུ་ག་བྱུང་བའོ། །

[Block 4381]
ཚིག་པ་ཞེས་བྱ་བ་ནི་རིན་པོ་ཆེ་དེ་མེ་དང་ཕྲད་ནས་རིན་པོ་ཆེ་མ་ཡིན་པ་ཉིད་དུ་གྱུར་ཏེ། ཉོ་ཚོང་བྱར་མི་རུང་བར་གྱུར་པ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 4382]
པ་ཎ་ནི་མངོན་མཚན་ལྷག་པ༌[^2997]ཡོད་པ་ཉིད་དུ་ཉམས་པ་ཡིན་གྱི་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་ཐལ་བར་གྱུར་པ་ནི་མ་ཡིན་ཏེ། དེ་ལེན་པ་ལ་ཉེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4383]
སྔོན་མ་སྤྱད་པ་ཞེས་བྱ་བ་ནི་ཐ་སྙད་འཇུག་པ་ཤེས་པར་གྱུར་པ་མ་ཡིན་པར་མངོན་མཚན་ཅན་ནོ། །

[Block 4384]
པ་ཎ་ཉིད་ལ་འདི་སྦྱར་བར་བྱའོ། །

[Block 4385]
རིན་པོ་ཆེ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4386]
ཡང་ན་ཚིག་པ་ཞེས་བྱ་བ་ནི་བདར་བ་སྟེ། དང་པོར་དྲི་མ་ཅན་བསྲེགས་པས་ཀྱང་ངོ་། །མཚན་དང་མི་ལྡན་པ་ཞེས་བྱ་བ་ནི་མཚན་ཉིད་དང་བྲལ་བའོ། །

[Block 4387]
མ་བྱས་པ་ཞེས་བྱ་བ་ནི་གང་ལ་མཚན་ཉིད་ཁོ་ན་མ་བྱས་པའོ། །

[Block 4388]
བཅོས་པ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ས་དང་རྩྭ་དང་རྡོ་ལ་སོགས་པ་རྣམས་ལ་ནོར་བུ་དང་དང་ཙེ༌[^2998]དང་མངོན་མཚན་ཅན་དང་རྒྱན་དང་འགྲོན་བུ་ལ་སོགས་པའི་རྣམ་པར་དབྱིབས་སུ་ཉེ་བར་བཀོད་པའོ། །

[Block 4389]
ཁ་མ་བསྒྱུར་བ་ནི་དེ་ལྟ་བུའི་ཚོན་གྱིས༌[^2999]མ་བཅོས་པའོ། །

[Block 4390]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 4391]
དགེ་སློང་གིས་གསེར་གྱི་ཕྲེང་བ་ལ་རེག་ན་སྤང་བའི་ལྟུང་བྱེད་དོ། །

[Block 4392]
དགེ་སློང་གིས་སོག་མའི་ཕྲེང་བ་ལ་རེག་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 4393]
གསེར་དང་དངུལ་ལ་རེག་པའི་སྤང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 4394]
རྙེད་པ་འདོད་པ་ལ་ལྟུང་བ་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་ཁེ་སྤོགས་འདོད་པ་ཉིད་ཀྱིས་འདུན་པ་བརྗོད་པ་དེའི་ཕྱིར་འདིར་ནི་སྐྱེད༌[^3000]ཕྱིན་ན་རྙེད་པ་ཡིན་གྱི་ཐོབ་པ་ཙམ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 4395]
བདག་ཉིད་ཀྱི་དོན་ཉིད་དུ་གཙོ་བོ་དེ་ལ་ཞེས་བྱ་བ་འདི་ལས་རང་གི་དོན་ཉིད་ལ་དངོས་གཞི་སྟེ། སྦྱོར་བ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 4396]
གཞན་གྱི་དོན་ཉིད་ལ་ནི་ཉེས་བྱས་དང་འདིའི་སྦྱོར་བ་ལ་ནི་ན་སྨད་པ་ཉིད་དེ༌[^3001]ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 4397]
ལྟུང་བ་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་དངོས་གཞི་འབའ་ཞིག་ནི་མ་ཡིན་ཏེ་སྦྱོར་བར་གྱུར་པ་ཡང་ངོ་། །ཕ་རོལ་པོ་ཁྱིམ་པ་ཉིད་དང་ཉེ་དུ་མ་ཡིན་པ་ཉིད་ཡིན་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་ནི་ཕ་རོལ་པོ་གང་དང་ལྷན་ཅིག་ཏུ་འདིར་ཐ་སྙད་དུ་བྱེད་པ་དེ་གལ་ཏེ་ཁྱིམ་པ་ཉིད་དང་ཉེ་དུ་མ་ཡིན་པ་ཉིད་ཡིན་ན་དེ་ནས་འདིར་དངོས་གཞིའི་ལྟུང་བར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4398]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་ཉེ་དུ་རྣམས་དང་ལྷན་ཅིག་སྤྱོད་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཉེས་བྱས་སུ་གསུངས་པ་གང་ཡིན་པའོ། །

[Block 4399]
དེ་བས་ན་འདིར་ཉེ་དུའི་ཚིག་འདི་ཡིན་ནོ། །

[Block 4400]
གཞན་ཉེ་དུ་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་ནི༌[^3002]འདིར་འགལ་ཟླའི་ཁྱད་པར་ཡོད་པ་ལ་འདིར་དངོས་གཞི་གང་དུ་ཞེ་ན། དེའི་ཕྱིར་སྐྱེད༌[^3003]ཕྱིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གི་ཚེ་སྐྱེད༌[^3004]ཕྱིན་ན༌[^3005]དེའི་ཚེ་དངོས་གཞིའི༌[^3006]ལྟུང་བར་འགྱུར་རོ། །

[Block 4401]
སྐྱེད་མེད་ན་ནི་སྦྱོར་བ་ཙམ་དུ་ཟད་དོ་ཞེས་བྱ་བ་ལ༌[^3007]ནོར་འཕེལ་བར་གྱུར་པའི༌[^3008]ནོར་ལ་འདིར་སྤང་བ་ནི་སྦྱིན་པ་པོ་ཉིད་ལ་ཡང་དག་པར་གནས་པ་དགོས་པར༌[^3009]བྱའོ། །

[Block 4402]
རྩ་བ་དང་བཅས་པ་ལ་ལྟུང་བར་རིག་པར་བྱའོ། །

[Block 4403]
སྐྱེད༌[^3010]ཕྱིན་པའི་ནོར་བསྒྲུབ་པ་ལ་སྦྱིན་པ་པོ་ཉིད་ལ་ཞེན་པས་རྣམ་པར་གཞག་ཅིང་དེ་ལས་སྐྱེད༌[^3011]དུ་གྱུར་པ་མངོན་པར་ཞེན་པ་སྦྱིན་པ་པོ་ལ་བྱས་པ་ཉིད་དོ། །

[Block 4404]
འོག་མ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཉོ་ཚོང་གིས་ཀྱང་རྙེད་པར་འདོད་པ་ཉིད་ལ་ལྟུང་བ་སྟེ། ཉེ་དུར་མ་གྱུར་པ་ཉིད་དང་ཁྱིམ་པའི་བདག་ཉིད་ཅན་ཉིད་ལ་སྐྱེད༌[^3012]ཕྱིན་པ་ཉིད་དུ་སྒྲུབ་ན་གཞན་ལ་དངོས་གཞིའོ། །

[Block 4405]
འདིར་ཅིའི་ཕྱིར་སྐྱེད༌[^3013]བསྒྲུབ་པ་ལ་དངོས་གཞི་ཡིན་ཞེ་ན། དེའི་ཕྱིར་པ་ཎ་འམ༌[^3014]རིན་པོ་ཆེས་སྤྱོད་པ་ལས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་རེག་གམ་རེག་དུ་འཇུག་པར་བྱེད་པ་དག་ལ༌[^3015]སོ་སོར་བསྒྲུབ་པ་སྔོན་དུ་འགྲོ་བས་སྤང་བའི་ལྟུང་བྱེད་དུ་རིག་པར་བྱའོ། །

[Block 4406]
ཉོ་བ་ལ་ཡང་རྙེད་པ་གྲུབ་ན་དངོས་གཞི་སྟེ། ཉོ་བ་མ་ཡིན་པ་ལ་ཡང་རྙེད་པ་མ་གྲུབ་པ་ལ་ཉེས་བྱས་སོ། །

[Block 4407]
ཉོ་བ་མ་ཡིན་པ་ལ༌[^3016]སྔོན་དུ་འགྲོ་བའི་རྙེད་པ་ལ་ཡང་དངོས་གཞིའི་བྱས་པ་ཉིད་ཅེས་བྱ་བ་འདིར༌[^3017]རྣམ་པར་གཞག་པ་འདི་རིག་པར་བྱའོ། །

[Block 4408]
སྦྱོར་བ་ལས་ནི་གཅིག་པོ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྐྱེད༌[^3018]གྲུབ་པ་བས་མདུན་རོལ་དུ་ཇི་སྲིད་དུ་འདིར་ཐམས་ཅད་ལ་བསྒྲུབ་པ་དེ་ལ་གཅིག་པ་ཉིད་དེ་ཐ་དད་པ་ནི་འགའ་ཡང་མ་ཡིན་ནོ། །

[Block 4409]
མཐའ་ནས་ཕྱོགས་ཡོངས་སུ་བཙལ་བ་ལ་ཡང་འདི་ལྟ་བུར་གྱུར་པ་གཞན་ཐམས་ཅད་ལ་དེར་སྦྱོར་བའི་ལྟུང་བ་གཅིག་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4410]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་ཇི་སྲིད་དུ་རྙེད་པ་སྒྲུབ་པར༌[^3019]མི་བྱེད་ཀྱི་བར་དུ་ནི་ཉེས་བྱས་སོ། །

[Block 4411]
རྙེད་པ་གྲུབ་ན་ནི་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4412]
ཀུན་དགའ་ར་བ་འམ་དགེ་བསྙེན་དག་ཡོད་ན་བསྒོ་བས་དཀོན་མཆོག་གི་དོན་དུ་བསྐྱེད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཀུན་དགའ་ར་བ་འམ་དགེ་བསྙེན་དག་ཡོད་པར་གྱུར་ན་དེ་གཉིས་འདིར་བསྐོ་བས་དཀོན་མཆོག་གི་དོན་དུ་སྦྱོར་བ་བྱེད་པ་ལ་ངེས་པར་སྦྱར་བར་བྱའི་རང་ཉིད་ཀྱིས་ནི་འཇུག་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 4413]
འདིར་གཞུང་ནི་མ་མོ་ལས་འདི་ལྟ་སྟེ་ཡངས་པ་ཅན་གྱི་ཚོང་པ་རྣམས་ཀྱིས་བཅོམ་ལྡན་འདས་ཀྱི་མཆོད་རྟེན་ཡང་བྱེད་དུ་བཅུག་གཙང་ཁང་བྱུར་བུ་ཡང་བྱེད་དུ་བཅུག་ནས། དགེ་སློང་རྣམས་ལ་མཆོད་རྟེན་དང་གཙང་ཁང་བྱུར་བུ་གང་ཞིག་རལ་དུ་མི་འགྱུར་བའི་ཡོ་བྱད་རྗེས་སུ་གཏོད་པ་ན་དགེ་སློང་དག་འགྱོད་ཅིང་ལེན་པར་མི་བྱེད་ནས་སྐབས་དེ་དགེ་སློང་གིས་བཅོམ་ལྡན་འདས་ལ་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཀུན་དགའ་ར་བ་འམ་དགེ་བསྙེན་དག་གིས་མཆོད་རྟེན་ཞིག་རལ་དུ་མི་འགྱུར་བའི་ཡོ་བྱད་བླང་བར་བྱ་ཞིང་བླངས་ནས་ཀྱང་བསྐྱེད་པར་བྱ་སྟེ། དེ་ལ་རྙེད་པ་ཇི་ཙམ་བྱུང་བ་དེས་མཆོད་རྟེན་ལ་མཆོད་པ་བྱ་བར་ངས་རྗེས་སུ་གནང་ངོ་ཞེས་གསུངས་སོ། །

[Block 4414]
གཏའ་ཉིས་རིར༌[^3020]བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཆུད་མི་གཟན་པར་བྱ་བའི་ཕྱིར་འདི་སྤང་བ་མི་སྐྱེད་པའི༌[^3021]ཡན་ལག་ཅེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །ཇི་ལྟར་འདི་བླངས་ནས་སྦྱར་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དཔང་པོ་དང་ལོ་དང་ཟླ་བ་དང་ཉི་མ་དང་དགེ་འདུན་གྱི་གནས་བརྟན་དང་དགེ་སྐོས་དང་ལེན་པ་པོ་དང་རྫས་དང་སྐྱེད༌[^3022]རྣམས་དཔང་རྒྱར་བྲིས་ནས་སོ། །

[Block 4415]
རྒྱུས་ཤེས་པས་དེ་གཞན་ལ་ཁོང་དུ༌[^3023]ཆུད་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་གང་ལ་འཇུག་པ་འདི་དེས་འདི་ཙམ་ཞིག་འདི་ལས་སྤྱད་པ་དང་དེས་འདི་ཙམ་དུས་དེ་ལ་སྦྱིན་པར་བྱ་བ་ཞེས་བྱ་བའི་རྒྱུས་ཤེས་པར་གྱུར་པ་དེས་གཞན་གྱི་སྟེང་དུ་འདིའི་ལོ་རྒྱུས་ཤེས་པའི་དགེ་སློང་གང་ཞིག་གིས་དེ༌[^3024]ལ་རིམ་པ་ཐོབ་ན་ཁོངས་སུ་ཆུད་པར་བྱ་བ་ནི་བརྗོད་པར་བྱ་ཞེས་བྱ་བའི༌[^3025]དོན་ཏོ། །
--- END BLOCKS ---
