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
[Block 4551]
ཁྲིའུ་དང་ཆོལ་ཟངས་ཡན་ཆད་དོ་ཞེས་བྱ་བ་ནི་ཐ་ན་ཁྲིའུ་དང་ཆོལ་ཟངས་ཀྱི་བར་ཡན་ཆད་ཀྱང་དེའི་ཉིན་མོ་བསྡོག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4552]
དེ་སྟོབས་པ་བསྐོ་བར༌[^3166]བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་སྒྲས་ནི་གནས་མལ་སྟོབས་པ་ཡང་བསྡུས་པའོ། །

[Block 4553]
མི་ནུས་ན་དུ་མའོ་ཞེས་བྱ་བ་ནི་གཅིག་གིས་གནས་མལ༌[^3167]སྟོབས་པར་མི་ནུས་པ་ན། གནས་མལ་སྟོབས་པ་དུ་མ་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4554]
བསྐོས་པའི་འོག་ཏུ་དེས་ཅི་ཞིག་བྱ་ཞེ་ན། དེའི་ཕྱིར། དེས་དྲི་དག་གིས་བསྐུས་པའི་ཚུལ་ཤིང་གཟེབ་ཀྱི་སྤྲོག་མར་རས་དཀར་པོ་བཏིང་བས་དཀྲིས་པ་དག་རྒན་རིམས༌[^3168]སུ་བཞག༌[^3169]ནས། ཚེ་དང་ལྡན་པ་དག་གནས་འདི་ན་ཁྲིམས་སུ་བཅས་པ༌[^3170]འདི་དང་འདི་ཡོད་དེ། ཁྱེད་ཅག་ལས་གང་ཁྲིམས་སུ་བྱ་བ་འདི་དང་འདིས་གནས་པར་སྤྲོ་བ་དེས་ནི་ཚུལ་ཤིང་ལོང་ཤིག༌[^3171]ཁྱེད་ཅག་ལས་སུས་ཀྱང་དབྱར་དགེ་འདུན་གྱི་ནང་དུ་འཁྲུག་ལོང་བསྐྱེད་པར་མི་བྱའོ། །

[Block 4555]
ཁྱེད་ཅག་ལས་གང་གིས་འགའ་ཞིག་ལས་ཅུང་ཟད་ཤེས་པ་དེས་ང་སྨྲོས་ཤིག །ཁྱེད་ཅག་ལས་གང་དབྱར་གྱི་ནང་དུ་དགེ་འདུན་ལས་འཁྲུག་ལོང་སྐྱེད་པར༌[^3172]འགྱུར་བ་དེ་ལ་དགེ་འདུན་གྱིས་ཕྱིས་ཉེ་བར་བརྟག་པར་དགོངས་སོ་ཞེས་དགེ་སློང་རྣམས་ལ་གོ་བར་བྱའོ་ཞེས་སྨོས་ཏེ། དེས་ཞེས༌[^3173]བྱ་བ་ནི་གནས་མལ་སྟོབས་པས་སོ། །

[Block 4556]
སྨྲོས་ཤིག་ཅེས་བྱ་བས་ནི་དགོད་པ་པོས་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཕིགས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4557]
གཞན་གྱིས་བླང་བ་དང་ཁས་བླང་བའི༌[^3174]ཕྱིར་དགེ་འདུན་ལ་གསོལ་བ་བྱའོ་ཞེས་བྱ་བ་ནི། །གནས་མལ་སྟོབས་པའི་དགེ་སློང་དེ་ལས་གཞན་པའི་དགེ་སློང་གིས་སོ། །

[Block 4558]
དགེ་སློང་གཞན་གཅིག་གིས་ཚུལ་ཤིང་བླངས་པ་དང་། དབྱར་གནས་ཁས༌[^3175]བླང་བའི་ཕྱིར་གོ་བར་བྱ་ཞེས་བྱ་བའོ།

[Block 4559]
[^3176] །གསོལ་བ་གཅིག་དང་འབྲེལ་བ་ཉིད་ལ་དོན་གཉིས་བརྗོད་པའོ། །

[Block 4560]
ཚུལ་ཤིང་བྲིམ་མོ། །

[Block 4561]
དང་པོ༌[^3177]སྟོན་པའི་བླང་ངོ་ཞེས་བྱ་བ་ནི། ཚུལ་ཤིང་བྲིམ་པ༌[^3178]པོས་ཚུལ་ཤིང་བྲིམ་པར༌[^3179]བྱ་བའོ། །

[Block 4562]
གཞན་དག་གིས་ནི་སྟན་ལས་ཕྱེད་འཕགས་པས་སོ་ཞེས་བྱ་བ་ནི། སྟོན་པའི་ཚུལ་ཤིང་ལེན་པ་ལས་གཞན་པས་སོ། །

[Block 4563]
དགེ་ཚུལ་རྣམས་ཀྱི་ནི་སློབ་དཔོན་དང་མཁན་པོ་དག་གིས་སོ། །

[Block 4564]
མཇུག་ཏུ་གཉུག་མར་གནས་པ་རྣམས་ཀྱི་དེ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། འཕྲོག་མ་ལ་སོགས་པ་དག་གིས༌[^3180]ཚུལ་ཤིང་བྲིམ༌[^3181]པའོ། །

[Block 4565]
དེ་ཡང་ཞེས་བྱ་བ་ནི་ཚུལ་ཤིང་ལ་གཏོགས་པའོ། །གང་གི་ཚེ་དེ་རྣམས་ལ་འདི་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མཐར་དལ་བུས་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས༌[^3182]ཏེ། ཚུལ་ཤིང་རྣམས་གཞག་གོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4566]
དེ་ལ་གནས་ཁང་བསྟབས་པ་ཞེས་སྨོས་པས་འདིར་འདི་ཡང་སྨོས་པར་འགྱུར་བ་དེ་ལྟ་བས་ན་མདོ་འདི་བྱས་པ་ཡིན་ནོ། །

[Block 4567]
བགྲངས་ནས་གནས་འདིར་དགེ་སློང་འདི་སྙེད་ཀྱིས་ཚུལ་ཤིང་བླངས་སོ་ཞེས་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ་ཞེས་བྱ་བའི་སྒྲས་ནི་འདི་ལྟར་དགེ་འདུན་ལ་གོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4568]
གནས་ཀྱི་གཞི་བསྟབ་པར་བྱའོ། །

[Block 4569]
དེ་དག་གི་སྒོ་ལྕགས་དང་ལྡེ་མིག་བླངས་པས་མདུན་དུ་འདུག་སྟེ། གནས་བརྟན་གཙུག་ལག་ཁང་ཆེ་གེ་མོ་ནི་རྙེད་པ་དང་བཅས་པ་གོས་ཀྱི་རིན་དང་བཅས་པ་ལགས་ཀྱིས་བཞེས་ཤིག་ཅེས་ཡོན་ཏན་ཇི་ལྟ་བ་བཞིན་དུ་མོས་པ་བསྐྱེད་ཅིང་ལེན་དུ་གཞུག་གོ་ཞེས་བྱ་བ་ལ། བླངས་པས་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་གནས་ཀྱི་གཞི་གང་ལ་བསྟབ་པར༌[^3183]བྱ་བ་དེ་ལའོ། །

[Block 4570]
སྒོ་ལྕགས་དང་ལྡེ་མིག་ཅེས་བྱ་བ་ནི། དེ་གཉིས་གང་གིས་བླངས་པ་ཞེས་བྱ་བའི་བསྡུ་བའོ། །

[Block 4571]
ཡོན་ཏན་ཇི་ལྟ་བ་བཞིན་དུ་ཞེས་བྱ་བ་ནི། གནས་ཀྱི་གཞི་དེའི་ཡོན་ཏན་གང་ཡིན་པས་དེ་མོས་པ་བསྐྱེད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4572]
བླང་བ་ལ་སོགས་པ་ནི་ལྷུང་བཟེད་དང་འདྲའོ་ཞེས་བྱ་བ་ལ། དགོས་པ་བླང་བ་དང་བླངས་པ་མ་ཡིན་པ་སྟེ། བར་ཆོད་པས་ཚིག་གཉིས་པ་ལ་མི་སྦྱིན་ཞིང་ཕྱི་མ་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བ་འདི་ནི་གཞན་ལ་ཡང་འགྲེ༌[^3184]བའོ། །

[Block 4573]
མཆོད་རྟེན་དང་དགེ་འདུན་གྱི་དོན་མ་ཡིན་པར་སོང་བར་ཤེས་པ་ལ་ནི་འཐེབ་ཉིད་ལས་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། མཆོད་རྟེན་དང་དགེ་འདུན་གྱི་དོན་ལ་མ་སོང་བ་ལ་ཇི་ལྟར་རྒན་རིམས་ཉིད་ཀྱི་དགེ་འདུན་གྱི་གནས་བརྟན་ཡོད་པ་ལ་བཙུན་པ་ཉེ༌[^3185]དགས་རྒན་པ་གཞན་འོངས་པ་ལ་བདག་ཉིད་དང་ལྷན་ཅིག་དགེ་འདུན་གནས་བརྟན་དུ་གྱུར་ནས་གནས་བརྟན༌[^3186]གཉིས་པས་གནས་པར་བྱ་སྙོམ་པའི༌[^3187]བློས་གཙུག་ལག་ཁང་གཞན་དུ་སོང་བ་ན། དེར་དགེ་འདུན་གྱི་གནས་བརྟན་གྱི་རྙེད་པ་དང་། རྙེད་པ་སྔ་མ་གནས་བརྟན་གཉིས་པའི་རྙེད་པ་དང་། མཉམ་པར་ཤེས་ནས་དགོས་པ་མེད་པར་ཅིའི་ཕྱིར་དགེ་འདུན་གྱི་གནས་བརྟན་ཉིད་བདག་གིས་བྱའོ་སྙམ་པའི་བློ་སྔོན་དུ་བཏང་ནས། གཙུག་ལག་ཁང་དུ་ཕྱིན་པ་དང་སྔར་བསྟན་པའི་གནས་མལ་ལ་ཇི་ལྟར་འཕེལ་བ་ཉིད་ཀྱིས་མལ་སྟན་སློང་བར༌[^3188]བྱེད་པ་ཞེས་བྱ་བ། བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་བའི་ལུང་ལས་འབྱུང་བ་ཡིན་ནོ། །

[Block 4574]
དགེ་འདུན་གྱིའམ་མཆོད་རྟེན་གྱི༌[^3189]བྱ་བ་ལ་སོང་བར་གྱུར་པ་གང་ཡིན་པ་དེ་ལ་ཇི་ལྟར་རྒན་རིམས་ཀྱིས༌[^3190]གནས་མལ་བསྟབ་པར་བྱའོ། །

[Block 4575]
གཞན་ལ་ནི་ཇི་ལྟར་འཐེབ་ཉིད་ལས་བསྐོ་བར་བྱའོ་ཞེས་སྨོས་པ་སྟེ། དེ་བས་ན་མདོ་འདི་སྟེ་ཇི་ལྟར་བསྐོ་བ་ལས་གཞན་པས་བསྐོ་བར་བྱའོ། །

[Block 4576]
འདི་ཇི་ལྟར་འཐེབ་ཀྱི་དོན་འདིའོ། །

[Block 4577]
གནས་མལ་གྱི་གཞི་ལས་འདི་དང་པོར་བྱ་སྟེ། སྔར་རྟོག་པའི༌[^3191]དགེ་སྐོས་ཀྱིས་ཞེས་བྱ་བ་དེ་བས་ན་འདིར་གྲགས་པ་ཡིན་ནོ། །

[Block 4578]
གང་དུ་གཞུང་འཆད་པར་འགྱུར་བ་འདི་དང་གཞན་དེ་སྤངས་ནས་དུ་མ་ཉིད་མ་ཡིན་པ་གཙུག་ལག་ཁང་དུ་ཞེས་བྱ་བ་འདི་ཡང་དྲངས་པ་ཡིན་ནོ། །

[Block 4579]
ཤིང་ལྗོན་པའི་དྲུང་དང་ནེའུ་གསིང་གི་གཞི་དག་ལ་ཡང་རྒན་རིམས་སུ་བསྐོ་བར་བྱའོ། །

[Block 4580]
གནས་ཁང་གིས་མི་ཆོག་ན་གཉིས་ལ་སོགས་པ་དག་ན་ཐ་ན་དེའི་ས་གཞི་གདིང་བའི་ཚད་ཙམ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། མི་ཆོག་ན་ཞེས་བྱ་བ་ནི། གལ་ཏེ་དགེ་སློང་ཐམས་ཅད་ལ་རེ་རེ་ལ༌[^3192]བསྐོར་མི་ཆོག་ན་འདི་རྣམས་ཐམས་ཅད་ཀྱིས་གནས་ཀྱི་གཞི་ཐོབ་པའི་མཐར་ཐུག་པ་མ་ཡིན་པ་སྟེ། སོགས་པའི་སྒྲས་གྲངས་པར་བསྟན་པའི་ཕྱིར་ཐ་ན་ཞེས་སྨོས་སོ། །

[Block 4581]
དེའི་ས་ཞེས་བྱ་བ་ནི་གནས་ཁང་གིས་གཞིར་བཏིང་བའི་ཚད་ཙམ་ཡང་བསྐོ་བ་ཞེས་བྱ་བའི༌[^3193]དོན་ཏོ། །

[Block 4582]
ལྷུང་བཟེད་དང་བྱ་མ་བུམ་དང་འདག་རྫས་དང་། སོ་ཤིང་དང་། སྨན་གྱི་གནས་ལ་ལྟོས་པར་བྱའོ་ཞེས་བྱ་བ་ལ་ལྟོས་པར་བྱའོ་ཞེས་བྱ་བ་ནི། གདིང་བའི་ཚད་ཙམ་དུ་བསྐོ་བར༌[^3194]བྱའོ། །

[Block 4583]
དེ་དོར་ནས་ནི་མ་ཡིན་ཏེ་དེ་ལྟར་མ་ཡིན་ནོ། །

[Block 4584]
ཇི་ལྟར་དེ་འབྱུང་བར་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4585]
ཁ་ཅིག་ནི་འདིར་སྨན་གྱི་ཚིག་ཏུ་ཡང་བྱེད་དོ། །

[Block 4586]
དེ་ནི་མི་རིགས་ཏེ་ནད་པས་བསྟེན་པར་བྱའི་གཞན་གྱིས་ནི་བཟའ་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4587]
སྒོ་ཁང་དང་ཐེམ་སྐས་ཀྱི་ལྐོག་དང་། ཁྱམས་དང་དཔོང༌[^3195]ས་དང་བཀད་ས་དང་བསྲོ་ཁང་གི་ར་བ་དག་ནི་བསྐོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ནི་མི་ཆོག་པ་ལ་བསྐོ་བར་བྱ། ཤེས་པར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4588]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 4589]
དགེ་སློང་དག་གནས་དྲུག་པོ་འདི་དག་ནི་བསྒོ་བར༌[^3196]མི་བྱ་བ་དག་སྟེ། སྒོ་ཁང་ཐམས་ཅད་དང་། ཐེམ་སྐས་ཀྱི་ལྐོག་དང་ཁྱམས་དང་དཔོང༌[^3197]སའི་ར་བ་དང་བཀད་སའི་ར་བ་དང་བསྲོ་ཁང༌[^3198]གི་ར་བ་དག་སྟེ། སྐོ་བར༌[^3199]བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4590]
མཚན་མོ་གནས་མལ་མི་བསྐོའོ་ཞེས་བྱ་བ་ནི་བསྐོ་བར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །
--- END BLOCKS ---
