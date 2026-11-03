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
འདིར་ཟས་ནི་ལྷག་མར་བྱས་པ་སྟེ། བསྒྱུར་བ་དང་བསྒྲུབ་པ༌[^3223]ལ་འདི་ནི་ཉེས་བྱས༌[^3224]སུ་བརྗོད་པའོ། །

[Block 4727]
འདིར་གཞུང་ནི་འདི་ཡིན་ཏེ། མུ༌[^3225]ཏོ་བ་གཅིག་ལ་བསྔོས་པའི་ཟས་མུ༌[^3226]ཏོ་བ་གཞན་ལ་སྒྱུར་བར་བྱེད་ན་ཉེས་བྱས་སུ་བརྗོད་པ་གང་ཡིན་པ་བཟའ་བར་བྱ་བ་ལ༌[^3227]ཡང་དེའོ་ཞེས་བྱ་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 4728]
དབྲལ་བ་དང་སྦྱར་བ་གཉིས་ཀ་སེམས་ཅན་དུ་བགྲང་བ་མ་ཡིན་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གནས་ཁང་ལ་སོགས་པ་སེམས་ཅན་དུ་བགྲང་བ་ཉིད་མ་ཡིན་པ་གནས་ཁང་ལ་སོགས་པ་གང་ལ་རྙེད་པ་འདི་བསྔོས་པ་འདི་ནི་འདིར་དབྲལ་བར་བྱ་བར་བརྗོད་དོ། །

[Block 4729]
གང་དུ་སྔོ་བར༌[^3228]བྱེད་པ་དེ་ནི་སྦྱོར་བའོ། །

[Block 4730]
འདིར་ཡང་བསྔོ་བ་དང་གྲུབ་པ་ལ་ཉེས་བྱས་ཞེས་བྱ་བ་འདིར་ངག་གི་དོན་ཏོ། །

[Block 4731]
ཕྱོགས་གཅིག་པ་ཉིད་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཐེམ་སྐས་ཀྱི་རིམ་པ་ལ་སོགས་པ་གཅིག་ལ་ལུས་ལ་སོགས་པ་ཉིད་ཀྱིས་ཕྱོགས་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་དབྲལ་བར་བྱ་བ་དང་། སྦྱར་བ་གཉིས་ཀ་གཞན་ལ་བསྔོས་པ་འདི་ནི་སྦྱར་བར་བྱ་བ་མ་ཡིན་པ་དེ་བས་ན་དངོས་གཞིའི་ཉེས་པ་མེད་པར་ཤེས་པར་བྱ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4732]
འདིར་ཡང་བསྔོས་པ་དང་། གྲུབ་པ་ལ་ཉེས་བྱས་ཞེས་བྱ་བའི༌[^3229]དོན་ཏོ། །

[Block 4733]
ལྷག་མ་ཟ་བ་དུད་འགྲོ་ལ་སོགས་པ་བཙལ་ཏེ་མ་རྙེད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། ལྷག་མ་ཟ་བ་དུད་འགྲོ་ལ་སོགས་པ་གང་ལ་བསྔོས་པ་དེ་གལ་ཏེ་བཙལ་ཏེ་མ་རྙེད་ན།[^3230] དེ་ལས་གཞན་པ་ལ་བསྒྱུར་བ་ན་ཡང་ལྟུང་བ་མེད་དོ། །

[Block 4734]
བདེ་བར་གཤེགས་པའི་སྐུ་གཟུགས་གཞན་ལ་ནི་གཡར་པོར་སྦྱིན་དུ་རུང་ངོ་ཞེས་བྱ་བ་ནི། རྒྱན་ལ་སོགས་པ་གང་ཞིག་གཞན་ནི་བཅོམ་ལྡན་འདས་ཀྱིས༌[^3231]སྐུ་གཟུགས་དང་འབྲེལ་པ་གལ་ཏེ་དེ་ལས་གཞན་པའི་བཅོམ་ལྡན་འདས་ཀྱི་སྐུ་གཟུགས་ལ་གཡར་པོ་སྦྱིན་པར་གྱུར་ན་དེ་ལ་ཉེས་པ་མེད་དོ། །

[Block 4735]
བསྔོས་པ་མི་སྦྱིན་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི། ཆེ་གེ་མོ་ཞིག༌[^3232]ལ་སྦྱིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་དེ་ལ་སྦྱིན་པར་མི་བྱེད་ན་དེའི་ཕྱིར་འདི་ལ་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4736]
མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོང་སྟེ་དགེ་འདུན་གྱི་བྱིན༌[^3233]གྱིས་རློབ་པར༌[^3234]བྱེད་ནའོ་ཞེས་བྱ་བ་ནི། དགེ་འདུན་གྱི་རྙེད་པར་བསྔོས་པ་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོང་སྟེ། བྱིན་གྱིས་རློབ་པར་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4737]
མ་ཚོགས་པ་དག་གིས་འགོད་ནའོ་ཞེས་བྱ་བ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4738]
བྱིན་གྱིས་མ་བརླབས་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ཤི་བའི་ཡོ་བྱད་ལ་སོགས་པ་འགོད་ན་ཡང་ཉེས་བྱས་སོ། །

[Block 4739]
ཀུན་དབང་བའི་རྙེད་པ་དགེ་འདུན་ལས་གཅིག་གམ། གཉིས་སམ་གསུམ་གྱིས་ལེན་ནའོ་ཞེས་བྱ་བ་ནི། ཉེས་བྱས་སོ་ཞེས་བྱ་བ་འདི་ལ་ཐམས་ཅད་དུ་སྦྱར་བར་བྱའོ། །

[Block 4740]
ཀུན་དབང་བའི་རྙེད་པ་ཞེས་བྱ་བ་ནི་རྙེད་པ་དགེ་འདུན་ལས་ཐོབ་པར་གྱུར་པའོ། །

[Block 4741]
གཅིག་གམ་གཉིས་སམ་གསུམ་ལ་མི་སྟེར་བ་ལ་ཉེས་བྱས་སོ། །

[Block 4742]
གལ་ཏེ་དེ༌[^3235]རྙེད་པ་དེ་རྣམས་ལ་ཡོད་པར་གྱུར་ན་ཅིའི་ཕྱིར་ཉེས་བྱས་སུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེ་ལ་གཞན་དག་གིས༌[^3236]ཤས་ཉིད་མ་བྲལ་ལོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་དག་གིས་རྙེད་པ་བླངས་པ་དེ་ལས་གཞན་པའི་རྙེད་པ་དེ་ལ་འདིར་ཤེས་པར་བྱའོ། །

[Block 4743]
འདིར་ནི་རྒྱུ་བསྟན་པ་སྟེ་རྐུ༌[^3237]སེམས་མེད་པ་ལ་འདི་རྣམ་པར་གཞག་པ་ཡིན་གྱི། རྐུ་སེམས་ཡོད་ན་ལྟུང་བ་ཅིར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རྐུ་སེམས་ཀྱིས་ནི་བརྐུས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ།

[Block 4744]
འདིར་གཞུང་ནི་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 4745]
བྱིན་གྱིས་བརླབ་པ༌[^3238]གསུངས་པའི་འོག་ཏུ་ཇི་སྟེ་འདི་ལྟར་མི་བྱེད་ན་དགེ་སློང་དེ་གཅིག་པུས་གོས་དེ་བདག༌[^3239]ཏུ་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4746]
དགེ་སློང་དག་ཀྱང་སྐལ་བ་མཉམ་པ་སྟེ། དགེ་འདུན་ལ་བསྔོས་པའི་རྙེད་པ་གཅིག་གིས་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོང་སྟེ་བདག་གིར་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4747]
འོན་ཏེ་དེ་རྣམས༌[^3240]རྐུ་སེམས་ཀྱིས་བརྐུ༌[^3241]ཞིང་བདག་གིར་བྱེད་ན་ནི་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ། །

[Block 4748]
གཉིས་དང་རབ་ཏུ་མང་པོ་རྣམས་ཀྱང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། [^3242]གང་ཞིག་དེ་འདིར་འོན་ཏེ་དེ་རྣམས་རྐུ་སེམས་ཀྱིས་ཞེས་བྱ་བ་ནི་ཚིག་ནི་དེ་ལ་རྐུ་བ་ཉིད་དུ་ཤེས་པའོ། །

[Block 4749]
ཡོངས་སུ་རྫོགས་པ་དང་ཡོངས་སུ་མ་རྫོགས་པའི་སྤྲོས་པ་སྤང་བའི་དོན་དུ་འདིར་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་བྱ་བའི་ཚིག་ཡིན་གྱི་ཕམ་པ༌[^3243]མི་སྐྱེད་པ༌[^3244]ནི་མ་ཡིན་ནོ། །

[Block 4750]
གང་ཞིག་འདིར་རབ་ཏུ་མང་པོ་ཞེས་བྱ་བའི་ཚིག་དེ་ལ་དགེ་འདུན་དུ་གྱུར་པ་ཉིད་ལ་ཆོ་ག་འདི་དང་ལྡན་པ་སྟེ། དགེ་འདུན་དུ་མ༌[^3245]གྱུར་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4751]
དེར་གང་ཟག་གི་བྱེད་པར་གྱུར་པ་ཉིད་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བའི་དགོངས་པ་ཉིད་མང་པོའི་ཚིག་ལས་ཤེས་པའོ། །

[Block 4752]
གྱ་ཚོམ་དུ་གཙུག་ལག་ཁང་དོར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཕྲན་ཚེགས་དག་ལས་འདི་ཞེས་བྱ་བ་ལ་སོགས་པ་ཇི་སྲིད་དུ་དོར་བ་ལས་འགྱེད་པ་ཞེས་བྱ་བ་འདི་ལས་སོ། །

[Block 4753]
རྗེས་སུ་ཆགས་པ་དང་བཅས་པ་དེར་སྲུང༌[^3246]མར་བཞག་གོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་དེ་ལ་ཆགས་པ་དང་བཅས་པ་གང་ཡིན་པ་དེ་ནི་སྲུང༌[^3247]མའི་ཕྱིར་གཞག་པར་བྱའོ། །

[Block 4754]
དེ་ལ་འོས་པ་རྣམས་ཀྱིས་གཙུག་ལག་ཁང་གཏད་པར་བྱ་ཞེས་བྱ༌[^3248]བའི་དོན་ཏོ། །

[Block 4755]
རྗེས་སུ་ཆགས་པ་དང་བཅས་པའི་ཕྱིར་དཀར་པོ་ཐོབ་ཀྱང་འདི་ཡོངས་སུ་དོར་བར་མི་བྱེད་ཅེས་བྱ་བ་ནི་དགོས་པའོ། །

[Block 4756]
མ་ལྷག་ན་ལོ་བཅུ་འདའ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་གཙུག་ལག་ཁང་བསྲུང་བ་ལ་དགེ་འདུན་མ་ལྷགས་ཤིང་གང་གིས༌[^3249]བསྲུང་བ་དེར་ལོ་བཅུ་འདའ་བར་བྱའོ། །ཇི་ལྟར་འདའ་བར༌[^3250]བྱ་ཞེ་ན། དེའི་ཕྱིར་ལྔ་ནི་བསོད་སྙོམས་ཀྱིས་སོ། །

[Block 4757]
དེར་དུས་སུ་སྦྱིན་བདག་མ་བྱུང་ན་ལོ་གཞན་ལྔ་ནི་ཉེ་འཁོར་གྱི་གཙུག་ལག་ཁང་དང་ལྷན་ཅིག་ཏུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེར་དུས་སུ་ཞེས་བྱ་བ་ནི་ལོ་ལྔ་འདས་པ་རྣམས་ལ་སྦྱིན་བདག་མ་བྱུང་ན་ལོ་གཞན་ལྔ་པོ་རྣམས་ནི་ཉེ་འཁོར་གྱི་གཙུག་ལག་ཁང་དང་ལྷན་ཅིག་འདའ་བར་བྱའོ། །

[Block 4758]
འདིར་གཞུང་ནི་ཁ་ཅིག་ལས་ལྔ་ནི་བསོད་སྙོམས་ཀྱིས་སོ། །

[Block 4759]
ལྔ་ནི་ཉེ་འཁོར་གྱི་གཙུག་ལག་ཁང་ལ་བརྟེན་པ༌[^3251]སྟེ། དེ་ལྟར་ན་ལོ་བཅུར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4760]
འདི་ཉིད་འདི་ལྟར་སྨྲས་པ་ལ་བྱ་བ་དང་བཅས་པའི་ལོ་བཅུའི་ཚིག་བྱས་སོ་ཞེས་བྱ་བ་ཤེས་པ་ཡིན་ནོ། །

[Block 4761]
གསོ་སྦྱོང་ཐ་དད་པ་དང་རྙེད་པ་ཐུན་མོང་བའི་ལས་བྱའོ་ཞེས་བྱ་བ་ལ། ཐ་དད་པར་ཞེས་བྱ་བ་ནི་སོ་སོར་རོ། །

[Block 4762]
ཉེ་འཁོར་གྱི་གཙུག་ལག་ཁང་དང་ལྷན་ཅིག་ཏུ་གཙུག་ལག་ཁང་དེར་གསོ་སྦྱོང་ཐ་དད་པར་རྙེད་པ་གཅིག་པའི་ལས་ཀྱིས་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4763]
འགྲོ་བ་ན་དངོས་པོ་རྣམས་ཉེ་འཁོར་གྱི་གཙུག་ལག་ཁང་རྣམས་སུ་གདམས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་གཏད་པ་ན་གང་གི་ཚེ་འཕོངས་པ་ལ་སོགས་པའི་དབང་གིས་གཙུག་ལག་ཁང་ནས་འགྲོ་བར་འདོད་པ་མལ་སྟན་དང་སྣོད་ལ་སོགས་པའི་དངོས་པོ་རྣམས་ཉེ་འཁོར་གྱི་གཙུག་ལག་ཁང་རྣམས་སུ་གདམས་པར་བྱ་ཞེས་བྱ༌[^3252]བའི་དོན་ཏོ། །

[Block 4764]
གཉུག་མར་གནས་ན་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཏམས་པའི་དངོས་པོ་ལ་གང་དུ་གཏམས་པ་དེར་གཉུག་མར་གནས་པའི་དགེ་སློང་རྣམས་ཀྱིས་སྦྱིན་པར་བྱའོ། །

[Block 4765]
གནས་གཞན་གྱི༌[^3253]རྫས་གནས་གཞན་དུ་མི་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ངེས་པའི་རྙེད་པ་ལ་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བའི་མདོའི་ཕྱོགས་ཀྱི་རྗེས་སུ་བརྗོད་པའོ། །
--- END BLOCKS ---
