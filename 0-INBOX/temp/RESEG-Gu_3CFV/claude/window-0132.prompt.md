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
[Block 4621]
ཕྲན་ཚེགས་དག་ལས།

[Block 4622]
དགེ་སློང་གིས་ཞག་གཅིག་གི་དོན་དུ་གནས་མལ་མནོད་པར༌[^3213]མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4623]
རྙེད་པ་འདོད་པས་གཙུག་ལག་ཁང་མི་མནོད༌[^3214]དོ་ཞེས་བྱ་བ་ནི་གནས་མལ་ལ་ཡང་འཕངས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 4624]
འདིར་གཞུང་ནི། དེ་ནས་དུས་གཞན་ཞིག་ན་དགེ་སློང་རྣམས་ལ༌[^3215]རྒན་རིམས་བཞིན་དུ་གནས་མལ་སྟོབས་པར་བྱེད་ན། བྲམ་ཟེ་ཞིག་གཙུག་ལག་ཁང་དུ་འོངས་ནས་དེས་དེ་མཐོང་བ་དང་། གང་གི་ཕྱིར་འདི་བཞིན་བགོ༌[^3216]བཤའ་བྱེད་པའི་ངང་ཚུལ་ཅན་ཤཱཀྱའི་སྲས་ཀྱི་དགེ་སློང་འདི་དག་ལ༌[^3217]སུ་ཞིག་མངོན་པར་དད་པར་མི་འགྱུར་སྙམ་དུ༌[^3218]དད་པ་སྐྱེས་པར་གྱུར་ནས། དེས་གཙུག་ལག་ཁང་བྱེད་དུ་བཅུག་སྟེ་དགེ་སློང་གི་དགེ་འདུན་ལ་ཕུལ་བ་དང་། དགེ་སློང་རྣམས་ཀྱིས་སྨྲས་པ། ཧ་ཅང་གཤེར་ཆེས་སོ་ཞེས་མི་ལེན་པ་དང་། དེས་ཕྲུས་འདེབས་སུ་བཅུག་སྟེ་ཕུལ་ལོ། །

[Block 4625]
དགེ་སློང་རྣམས་ཀྱིས་སྨྲས་པ། ཧ་ཅང་དགོན་དུང༌[^3219]ཆེས་སོ་ཞེས་མི་ལེན་པ་དང་། བྲམ་ཟེ་དེས་དེ་དག་རྙེད་པ་འདོད་པས་མི་ལེན་པར་རིག་ནས། བྲམ་ཟེ་དེས་ཤཱཀྱའི་སྲས་ཀྱི་དགེ་སློང་དག་གིས༌[^3220]རྙེད་པ་འདོད་པས་གཙུག་ལག་ཁང་ལེན་ཏོ་ཞེས་བྱ་བར་རྩོམ་པ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་རྣམས་ཀྱིས་རྙེད་པ་འདོད་པས་གཙུག་ལག་ཁང་བླང་བར༌[^3221]མི་བྱ་སྟེ། འོན་ཀྱང་སྦྱིན་བདག་རྣམས་ལ་རྗེས་སུ་སྙིང་བརྩེ་བས་གཙུག་ལག་ཁང་རྣམས་བླང་བར་བྱའོ་ཞེས་གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 4626]
[^3222]

[Block 4627]
དེ་ལྟ་བས་ན་འདིར་བརྩེ་བའི་སེམས་ཀྱིས་ཞེས་བྱ་བ་འདི་ནི་མཚོན་པ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཡིན་ཏེ་དེ་བས་ན་འདི་བསྡུ་བར་མ་བྱས་པའོ། །

[Block 4628]
ཐམས་ཅད་ཡོངས་སུ་སྤྱད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་དུ་མ་བླངས་པའོ། །

[Block 4629]
འདི་ལ་ཇི་ལྟར་ཐམས་ཅད་ཀུན་ནས་སྤྱད་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ལ་ལར་ཀློག་པ་དང་། ཁ་ཏོན་དང་། འདུག་པ་དང་། བཅག་པ༌[^3223]ལས་གང་ཡང་རུང་བ་བྱ། ལ་ལར་ལྷུང་བཟེད་དང་ཆོས་གོས་གཞག་པར་བྱའོ། །

[Block 4630]
ལ་ལར་མཚན་མོ་ཉལ་བ་དང་། ལ་ལར་སྔ་དྲོ་དང་། གུང་ཚིགས་དང་། ཕྱི་དྲོ་འདུག་པས་དེ་ལ་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཡོངས་སུ་སྤྱད་པར་བྱ་བ་དེ་ལའོ། །

[Block 4631]
དེ་ལ་གཞུང་ཁ་ཅིག་ལས་ནི། ལ་ལར་བཀླག་པར་བྱ། ཁ་དོན༌[^3224]བྱ། ལ་ལར་ལྷུང་བཟེད་དང་ཆོས་གོས་གཞག་པར་བྱ། ལ་ལར་འཆག་པར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 4632]
གཞུང་ཁ་ཅིག་ལས་ནི། ལ་ལར་སྔ་དྲོ་འདུག་པར་བྱ། ལ་ལར་གུང་ཚིགས་ལ་འདུག་པར་བྱ། ལ་ལར་ཕྱི་དྲོ་འདུག་པར་བྱ། ལ་ལར་མཚན་མོ་འདུག་པར་བྱའོ་ཞེས་གསུངས་པས། དེའི་ཕྱིར་གཉིས་ཀ་བསྡུ་བའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 4633]
གནས་པར་ཁས་བླངས་པས་གནས་ཀྱི་གཞི་རལ་བ་དང་འདྲུམས་པ་བཅོས་པར་བྱའོ་ཞེས་བྱ་བ་ལ། རལ་བ་ཞེས་བྱ་བ་ནི་ཕྱོགས་གཅིག་ཆད་པའོ། །

[Block 4634]
འདྲུམས་པ་ཞེས་བྱ་བ་ནི་གས༌[^3225]པའོ། །

[Block 4635]
དགེ་སློང་མ་དབྱར་གནས་པ་རྣམས་ཀྱིས་དབྱར་ཁང་བཅོས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་དུ་གཅིག་ཏུ་གྱུར་ནས་ཐམས་ཅད་སྤྱིས་བཅོས་པར་བྱ་བ་ཡིན་གྱི། གནས་ཁང་གང་ན་གང་གནས་པ་དེས་དེ་ཉི་ཚེས༌[^3226]བཅོས་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ལྟར་ཆོ་ག་འདིའོ། །

[Block 4636]
དེ་བས་ན་མ་བྱས་པ་ཉིད་དེ་ལ་རལ་བ་དང་འདྲུམས་པ་ཞེས་བྱ་བ་འདིས་རུང་བ་འཇུག་པ་སྒྲུབ་པའི་དོན་དུའོ། །

[Block 4637]
འཐབ་ཀྲོལ་ཅན་གྱིས་གནས་མི་ཐོབ་པར་བྱ་བའི་ཕྱིར་དགུན་མནོད་པ་དང་དཔྱིད་མནོད༌[^3227]པའི་གནས་མལ་ཡང་བསྟབ་པར༌[^3228]བྱའོ་ཞེས་བྱ་བ་ནི་གང་ཡང་རུང་བ་དེ་ལ་དགུན་དང་སོ་གའི་དུས་ཀྱི་ཆ་དག་ལ་ཟླ་བ་བཞི་དང་ལྡན་པ་ཉིད་ལ་མངོན་པར་བརྟེན་ནས་ཚིག་དེ་སྨོས་སོ། །

[Block 4638]
རིལ་གྱིས་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་མལ་རིལ་གྱིས་བསྐོ་བར་བྱའོ། །

[Block 4639]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། འདི་ལྟ་སྟེ། གཙུག་ལག་ཁང་དང་ཁང་ཁྱིམ་དག་གི་ཉེན་ཀོར༌[^3229]ཡང་ངོ་། །ཁྱམས་ཀྱི་དེ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཉེན་ཀོར༌[^3230]དང་བཅས་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4640]
དེ་དག་དོང་བ་ཉིད་ཀྱི་འོག་ཏུ་དེ་དག་མི་གཏོང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་དག་ཅེས་བྱ་བ་ནི་ཁྱམས་ཀྱི་ཉན་ཀོར༌[^3231]དང་དེའི་ཉན་ཀོར༌[^3232]དུས་མ་ངེས་པ་ཉིད་ཀྱིས་དགུན་དང༌[^3233]དཔྱིད་མནོད་པའི་གནས་མལ་གཉིས་ཀྱང་བསྟབ་པར་བྱའོ། །

[Block 4641]
རང་བཞིན་དུ་གནས་པའི་ཕྱིར་སྒྱུ་ཐབས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རང་བཞིན་དུ་གནས་པས་འཐབ་ཀྲོལ་མི་བྱེད་པའི་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཉིད་ཀྱིས་ཏེ། འདི་ནི་བསྐོ་བའི་དུས་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་ཞེས་བྱ་བ་ནི་ཁྱད་པར་མེད་པར་རྟོགས་པའོ། །

[Block 4642]
གང་ཞིག་མཐའ་འཁོབ་ཀྱི་རི་ལ་རང་བཞིན་དུ་གནས་པའི་དོན་དུ་ཆོ་ག་དེ་ལ་བྱས་པས་དེའི་དོན་དུ་དེ་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་པ་དེ་ནི་འདིའོ། །

[Block 4643]
འབྱུང་བའི་དོན་དུ་ནི་མི་བསྐོའོ་ཞེས་བྱ་བ་ནི་ཕྱིས་འབྱུང་བར་འགྱུར་བའི་དོན་དུ་དགོས་པ༌[^3234]ཉེ་བར་མི་གནས་པས་དེ་ཉིད་བསྟན་པའི་ཕྱིར། འདི་ནི་དུས་ཚིགས་དང་། ཉིན་མཚན་དང་དེའི་ཡན་ལག་ཆེ་གེ་མོ་ཞིག་འབྱུང་བའིའོ། །

[Block 4644]
འདི་ནི་མཁན་པོ་དང་སློབ་དཔོན་ཆེ་གེ་མོ་ཞིག་འབྱུང་བའིའོ། །

[Block 4645]
འདི་ནི་ལྷན་ཅིག་གནས་པ་དང་ཉེ་གནས་ཆེ་གེ་མོ་ཞིག་འབྱུང་བའིའོ། །

[Block 4646]
འདི་ནི་གཏམ་འདྲེས་པ་དང་ཕེབས་པར་སྨྲ་བ་དང་། འགྲོགས་བཤེས་དང་སྨོས་འདྲིན་པ༌[^3235]ལ་སོགས་པ་ཆེ་གེ་མོ་ཞིག་འབྱུང་བའིའོ་ཞེས་གཙུག་ལག་ཁང་དག་བསྐོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཡན་ལག་ཅེས་བྱ་བ་ནི་ཉིན་མཚན་གྱི༌[^3236]ཡན་ལག་སྔ་དྲོ་ལ་སོགས་པའོ། །

[Block 4647]
མནོད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གཞན་གྱིས་བསྐོས་ཀྱང་མནོད་པར་མི་བྱའོ། །

[Block 4648]
འདིར་གཞུང་ནི་འབྱུང་བའི་དོན་དུ་གཙུག་ལག་ཁང་བསྐོ་བར་མི་བྱ། བསྐོར་གཞུག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེ་ལ་མདོ་སྔ་མས་ནི་བསྐོ་བར་མི་བྱའོ་ཞེས་གསུངས་པ་བསྡུས་སོ། །

[Block 4649]
མདོ་འདིས་ནི་བསྐོར་གཞུག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་བསྡུས་སོ། །

[Block 4650]
ཕྲན་ཚེགས་དག་ལས་ཀྱང་དགེ་འདུན་གྱི་འབྲེལ་པ་ཞེས་བྱ་བ་དང་པོར་བྱས་ཏེ་མནོད་པ༌[^3237]ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 4651]
ཚང་གཞིག་པའི་ཕྱིར་དབྱུ་གུ་ཐོགས་པ་བསྐོ་བར་བྱའོ། །

[Block 4652]
སྒོ་ང་མེད་པ་རྣམས་ནི་གདོན་པར་བྱའོ། །

[Block 4653]
ཕྲ་མོ་རྣམས་ཀྱི་ནི་མི་འཕེལ་བར་བྱ་བའི་ཕྱིར་སྐུད་པས༌[^3238]དཀྲིའོ་ཞེས་བྱ་བ་ནི། ཁྭ་ཏ་དང་མཆིལ་པ་དང་ཕུག་རོན་རྣམས་ལ་ནི་མ་ཡིན་ཏེ། འོན་ཏེ་འོན་ཀྱང་ཕྲ༌[^3239]མོ་ཆུང་བ༌[^3240]སྦྲང་བུ་ཏྲཻ་མ་བུ་ག་དང་ཏྲཻ་ལ་ཏ་ལ་སོགས་པ་དག་གི་ཚང་གང་ཡིན་པ་དེ་རྣམས་སྐུད་པས་དཀྲི་བར་བྱའོ། །

[Block 4654]
འདིར་གཞུང་ནི་མི་འབྲེལ་བར༌[^3241]བྱ་བའི་ཕྱིར་སྐུད་པས༌[^3242]དཀྲིའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དཀྲིས་པ་དེ་ལ་འདི་རྣམས་ཀྱང་བརྗོད་པ༌[^3243]ཡིན་ཏེ། ཉེ་བར་བསགས་པར་བྱ་ཞེས་བྱ་བ་དོན་འདི་ཤེས་པའོ། །

[Block 4655]
གནས་མལ་ལ་སོགས་པ་སྦྱིན་ནོ་ཞེས་བྱ་བ༌[^3244]གོས་ལ་སོགས་པ་ཡང་བསྡུ་བའི་ཕྱིར་སོགས་པ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 4656]
ཡོད་པ་ཉིད་ན་དུ་མ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཉིས་པ་ཁྲིའུའི་རིམ་པ་ཡོད་པར་གྱུར་ན་ཁྲིའུ་ལ་སོགས་པ་གསུམ་ལ་སོགས་པ་ཡང་རུང་སྟེ། དེ་ཡང་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4657]
རིམ་པ་ཡོངས་སུ་མ་རྫོགས་ན་རྒན་རིམས་ནས་བརྩམས་ཏེ་ཇི་ཙམ་ཁྱེད་པ༌[^3245]ཡན་ཆད་ལ་དེ་སྙེད་པ་རྣམས་ལ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དོན་གྱིས་ཤེས་པར་བྱའོ། །

[Block 4658]
ཁྲི་ཆེན་པོ་དག་ཀྱང་བསྐོ་བར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 4659]
སྟན་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་གླེང་གཞི་དག་ལས་དེའོ། །

[Block 4660]
དགེ་འདུན་གྱི༌[^3246]གནས་མལ་གཡོགས་པ་དགེ་ཚུལ་མི་གཙང་བས་ཉམས་པར་བྱེད་པའི་ཆོས་ཅན་ལ་སུས་ཀྱང་མི་སྦྱིན་ནོ་ཞེས་བྱ་བ་ལ། སུས་ཀྱང་ཞེས་བྱ་བའི་སྒྲས་ནི་གནས་མལ་སྟོབས་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་གཞན་དག་གིས་ཀྱང་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
