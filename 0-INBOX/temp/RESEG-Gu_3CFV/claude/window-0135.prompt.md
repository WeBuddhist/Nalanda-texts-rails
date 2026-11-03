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
འདིར་གཞུང་ནི་དགེ་སློང་དག་གྲུར་དབྱར་གནས་པར་ཁས་ལེན་པར་བགྱིད༌[^3333]ན། དབྱར་རལ་བར་བརྗོད་པར་བགྱིའམ། རལ་བར་བརྗོད་པར་མི་བགྱི། བཀའ་སྩལ་པ། གལ་ཏེ་བརྗོད་ཀྱི་ནང་དུ་འབྱམ་པར་འགྱུར་བ་ཉིད་དུ་ཤེས་ན་དབྱར་རལ་བར་བརྗོད་པར་བྱའོ། །

[Block 4727]
འོན་ཏེ་མི་ཤེས་ན་ནི་དབྱར་རལ་བར་བརྗོད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་དང་།

[Block 4728]
ཁ་ཅིག་ལས།

[Block 4729]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གྲུར་དབྱར་གནས་པར་ཁས་ལེན་ན་དབྱར་གནས་པར་ཁས་བླངས་ཞེས་བགྱིའམ། གལ་ཏེ་ས་ལ་བརྟེན༌[^3334]ཅིང་གནས་པ་ཡིན་ན་དབྱར་གནས་པར་ཁས་བླངས་ཞེས་བྱའོ། །

[Block 4730]
བཙུན་པ་ཕུར་པའམ་ཞུགས་ཤིང་དང་འབྲེལ་པ་ལགས་ན་དབྱར་གནས་པར་ཁས་བླངས་ཞེས་བགྱིའམ། ཉེ་བ༌[^3335]འཁོར་གནས་པར་ཁས་བླངས་ཞེས་བྱའོ་ཞེས༌[^3336]གསུངས་པ་ཡིན་ཏེ། དེ་གཉིས་ཀ་བསྡུས་ནས་དེ་སྨོས་པ་ཡིན་ནོ། །

[Block 4731]
དེའི་ལྟ་བ་ལ་མངོན་པར་ཞེན་ནས་ཆོས་མ་ཡིན་པའི་ཕྱོགས་སུ་སོང་ནས་སྐྱ་རེངས་ཤར་ན་འཇིག་གོ་ཞེས་བྱ་བ་ལ། འཇིག་གོ་ཞེས་བྱ་བ་ཁས་བླངས་པ་དེའོ། །

[Block 4732]
དེ་ལྟ་བ་ལ་ཞེས་བྱ་བ་ནི་ཆོས་མ་ཡིན་པའི་ཕྱོགས་དེའི་ལྟ་བ་ལའོ། །གང་གི་ཚེ་ན་འདི་ཉམས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྐྱ་རེངས་ཤར་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་ཆོས་མ་ཡིན་པའི་ཕྱོགས་ཀྱི་ལྟ་བ་ལ་མངོན་པར་བརྟེན་ནས་ཆོས་མ་ཡིན་པའི་ཕྱོགས་སུ་མངོན་པར་མཆིས༌[^3337]ན། སྐྱ་རེངས་ཤར་བའི་དུས་སུ་ཁས་ལེན་པ་འཇིག་པའོ། །

[Block 4733]
འདིར་གཞུང་ནི། དགེ་སློང་བཞི་དག་ལས་བཙུན་པ་རེ་ཞིག་དབྱར་གྱི་ནང་དུ་དགེ་འདུན་བྱེ་བར༌[^3338]གྱུར་ལ། དེ་ན་གལ་ཏེ་དགེ་སློང་བསམས་བཞིན༌[^3339]དུ་ཆོས་ཀྱི་ཕྱོགས་ནས་ཆོས་མ་ཡིན་པའི་ཕྱོགས་སུ་མཆི་ན་དབྱར་རལ་ཞེས་བགྱིའམ། ཉེ་བ་འཁོར་གལ་ཏེ་དེའི་ལྟ་བ་འདོད་ཅིང་དེར་ཡང་སོང་ན་སྐྱ་རེངས་ཤར་ན་དབྱར་རལ་བར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4734]
ཐེ་ཚོམ་ཟ་བ་ཉིད་ལ་ནི་མི་འཇིག༌[^3340]གོ་ཞེས་བྱ་བ་ནི་བདག་གནས་པར་ཁས་བླངས་སམ་འོན་ཏེ་མ་བླངས་སྙམ་དུ་ཐེ་ཚོམ་ཟ་བ་ཉིད་ལ་ནི་དབྱར་གནས་པར་ཁས་བླངས་པ་མི་འཇིག་པའོ། །

[Block 4735]
མཐའི་ཞག་དྲུག་ལ་བྱིན་གྱིས་བརླབ་པ༌[^3341]མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་གནས་པར་ཁས་བླངས་ནས་ཟླ་བ་གསུམ་གྱི་མཐའི་ཞག་དྲུག་ལུས་པའི་ཚེ། ཕྱི་རོལ་དུ་འགྲོ་བའི་ཕྱིར་བྱིན་གྱིས་བརླབ་པ༌[^3342]མི་འཆགས་པ་སྟེ། དུས་ཧ་ཅང་ཡུན་ཐུང་ངུ་ལས་འདའ་བའི་ཕྱིར་རོ། །

[Block 4736]
ཧ་ཅང་ཐུང་ངུ་ཉིད་ལ་མ་རྫོགས་པ་རིགས་པ༌[^3343]ཡིན་ཏེ། གང་གི་ཕྱིར་སྐྱེས་པ་ངན་པ་ཉིད་དེ་ཞེས་བྱ་བ་ནི་ཞུ་བ་ལས་འབྱུང་བས་དགོངས་པ་མཐོང་བ་དེ་ལྟ་བས་ན་མདོ་འདི་ཡིན་ནོ། །

[Block 4737]
བྱ་བ་མེད་པར་ཤེས་ནས་ཕྱིར་མི་ལྡོག་པ་དང་གནས་པ་དག་ལ་ནི་འཇིག་གོ་ཞེས་བྱ་བ་ནི། འབྲས་བུ་མེད་པ་ཉིད་གང་གིས་ཤེས་པ་དེ་ནི་འབྲས་བུ་ཤེས་པ་ཉིད་ཤེས་པའོ། །

[Block 4738]
བྱིན་གྱིས་བརླབས་ཏེ་འགྲོ་བཞིན་པ་ལ་བསྒྲུབ་པ་མི་དགོས་པའི་སྐབས་རྙེད་ཅིང་ཕྱིར་མི་ལྡོག་པར་འགྲོ་བ་ལ་དབྱར་གནས་པར་ཁས་བླངས་པ་དེ་འཇིག་གོ། །

[Block 4739]
བྱིན་གྱིས་བརླབས་ནས་འགྲོ་བ་ལ་དེ་སྨོས་ཏེ། འདིར་གཞུང་ནི་གལ་ཏེ་ཤུལ་གྱི་དབུས་ཁོ་ནར་དོན་དེ་བག་ཡངས་སུ་གྱུར་ན་དེ་མཆི་བར་བགྱིའམ། ཉེ་བ་འཁོར་མི་བྱ་སྟེ། གལ་ཏེ་འགྲོ་ན་དབྱར་རལ་བའི་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4740]
འདྲ་བ་ཉིད་ཀྱིས་འདྲ་བ་ཡང་ཤེས་པའོ། །

[Block 4741]
འདི་ལ་མཐར་ཐུག་པའི་མཐའ་ནི་ཞག་བདུན་ཉིད་དོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་པ་ལའོ། །

[Block 4742]
ཞག་གཅིག་ལ་སོགས་པ་རྣམས་ལ་ཡང་བྱིན་གྱིས་བརླབ་ཏུ་རུང་བ་ཉིད་དུ༌[^3344]དེ་བསྟན་པའོ། །

[Block 4743]
གནང་བ་མ་ཐོབ་པའི་མཐའ་ནི་དེ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མཐའ་ཞག་བདུན་ཡིན་ནོ། །

[Block 4744]
གཞན་གྱི་ནི་ཞག་བཞི་བཅུའོ་ཞེས་བྱ་བ་ལ། གཞན་གྱི་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་པ་གནང་བ་ཐོབ་པ་དག་གི༌[^3345]མཐའ་ནི་ཞག་བཞི་བཅུའི་མཐར་ཐུག་པའོ། །

[Block 4745]
གནང་བ་ཐོབ་པས་དགེ་སློང་གི་མདུན་དུ་སྔགས་ཀྱིས་བྱིན་གྱིས་བརླབས་ཏེ་འགྲོ་བར་བྱའོ། །

[Block 4746]
གནང་བ་སྦྱིན་པ་ནི་བྱིན་གྱིས་བརླབ་པ་གནང་བ་སྦྱིན་པའོ། །

[Block 4747]
བྱིན་གྱིས་བརླབས་པ་མ་ཡིན་པ་བསྒྲུབ་པ་མ་ཡིན་ཞེས་བྱ་བ་འདིས་བྱས་པ་རིག་པར་བྱའོ། །

[Block 4748]
ཁྱེད༌[^3346]ལ་ཁོ་བོ་ཅག་གིས་བྱིན་གྱིས་བརླབ་པ་འདི་རུང་བར་བྱིན་གྱིས་བརླབ་པ་ཞེས་བྱ་བ་འདིར་གནང་བ་སྦྱིན་པའི་དུས་ལ་མངོན་པར་བརྟེན་ནས་དེ་རྩེ་གཅིག་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4749]
དེ་ལྟ་བས་ན་དུས་མ་ཚང་བ་ལ་བྱིན་གྱིས་བརླབ་པ་འཆགས་པ་མ་ཡིན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4750]
དེ་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་པའི་གནང་བ་དེའོ། །

[Block 4751]
དེ་ལས་ལྷག་པར་ཕྱི་རོལ་དུ་གནས་པར་མི་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། །དེ་ལས་ཞེས་བྱ་བ་ནི་ཞག་བཞི་བཅུ་པོ་དེ་ལས་སོ། །

[Block 4752]
ལྷག་པར་ཅུང་ཟད་བྱིན་གྱིས་བརླབས་ཀྱང་རུང་བ་ཡང་འགྲོ་བ་ལ་ཅིག་ཅར་བྱིན་གྱིས་བརླབས་ཀྱང་རུང་སྟེ། དེ་ལས་ལྷག་པར་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་འདུག་པར་མི་བྱའོ། །

[Block 4753]
འདིར་གཞུང་ནི་ཉེ་བ༌[^3347]འཁོར་མཚམས་དེར་ཆེས་མང་དུ་འདའ་བར་བྱའོ་ཞེས་གསུངས་པ་དེ་མདོ་ཡིན་ནོ། །

[Block 4754]
དེ་ནི་སྡེ་པ་ལྔ་པོ་དག་གི༌[^3348]ཡང་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། བྱིན་གྱིས་བརླབས་པ༌[^3349]དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4755]
དེ་ནི་མཚམས་ཀྱི་ནང་དུ་འཆགས་སོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི། གང་ཞིག་ཕྱི་རོལ་དུ་འགྲོ་བ་བྱིན་གྱིས་བརླབ་པ་དེ་ནི་སྡེ་པ་ལྔ་པོ་དག་ལ་བྱའོ་ཞེས་སྨོས་སོ། །

[Block 4756]
དགེ་སློང་གི་མདུན་དུ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གི་མདུན་དུ་བྱིན་གྱིས་བརླབས་ན་འཆགས་སོ་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 4757]
འདིར་དགེ་སློང་གི་མདུན་དུ་ཞེས་སྨོས་པ་ནི་གང་ཞིག་དགེ་སློང་མ་རྣམས་ཀྱི་གཞན་དུ་གསུངས་པ་དེ་བས་ན་འདིར་རྟགས་བརྗོད་པར་འདོད་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 4758]
བྱ་བ་ཐམས་ཅད་ལ་དགེ་སློང༌[^3350]མ་ལ་སོགས་པ་རྣམས་ལ་བསྙེན་པར་རྫོགས་པའི་དྲུང་དུ་དེ་གཙོ་བོ་ཉིད་ཀྱི་ཕྱིར་བྱ་བ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4759]
དེ་ལྟ་བས་ན་འདིར་དེ་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་མི་རིགས་པར་ཤེས་པར་མི་བྱའོ། །

[Block 4760]
མུ་སྟེགས་ཅན་གྱི་ལྟ་བ་དང་དབྲལ་བའི་ཕྱིར་དང་ཉེ་དུ༌[^3351]བྱ་བ་དང་། བདག་ཉིད་ཀྱི་ལུང་དང་རྟོགས་པ་ལ་ནེམ་ནུར་ཟ་བ་བསལ་བའི་ཕྱིར་འགྲོ་བ་ལ་དེ་བྱ་བ་མ་བསྡུས་པ་ཉིད་དུ་དོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་བྱ་བ་མ་བསྡུས་པ་ཉིད་དུ་དོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྔར་ཆོས་དང་ལྡན་པའི་དོན་དུ་ཞེས་སྨོས་པའི་མདོ་དེས་སོ། །

[Block 4761]
དེ་བྱ་བ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་པ་དེ་བྱ་བ་ལའོ། །

[Block 4762]
གནས་པར་ཁས་བླང་བ་ཉིད་ལ་གནས་པ་སྤང་བར་མི་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཁས་བླངས་པ་ཉིད་ལ་གནས་པའི་དགེ་སློང་སྤང༌[^3352]བར་མི་བྱ་བ་ཉིད་དོ། །

[Block 4763]
རྣམ་པར་གཞག་པ་འདི་སོ་སོར་བརྟེན་པར་གྱུར་པས་ན་དེ་ཤེས་པའོ། །

[Block 4764]
འདིར་གཞུང་ནི་དགེ་སློང་གནས་པར་ཁས་བླངས་པ༌[^3353]སྤང་བར་བགྱི་བ་དེ་དང་ལྷན་ཅིག་གནས་པར་བགྱིའམ། བཀའ་སྩལ་པ། དེ་དང་ལྷན་ཅིག་གནས་པར་བྱའོ། །

[Block 4765]
དགག་དབྱེ་བྱས་ནས་ནི་གནས་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
