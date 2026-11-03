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
[Block 3816]
དེས་ན་ངང་པའི་ཚུལ་ཅན་འདི་གཉིས་ངེས་པར་གཞན་ཞེས་བྱ་བར་སྟོན༌[^2475]ཏོ། །

[Block 3817]
ཡོན་ཏན་བསྒྲགས་པ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་ཅན་བསྟན་པ་དང་། ཡོན་ཏན་གསལ་བར་བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏེ། དེ་དང་བྲལ་བ་ད༌[^2476]ནི་ཕྲག་དོག་སྟེ། ཕྲག་དོག་མེད་པས་སོ། །

[Block 3818]
རྒྱས་པར་གྱུར་ཞེས༌[^2477]བྱ་བས༌[^2478]ནི་གཞན་དང༌[^2479]གཞན་དེ་དག་གིས་གྲགས་པ་རྒྱ་ཆེར་བྱས་ཤིང་ཡོན་ཏན་བསྟན་པ་སྟེ། གང་གི་ཕྱིར་གྲགས་པ་རྒྱས་པར་གྱུར་པ་དེ༌[^2480]བས་ན་དད་པ་སྐྱེས་པར་གྱུར་པ་སྟེ། ཡོན་ཏན་དང་ལྡན་པའི་ཚིག་ནི་གཟུང་བར་འོས་པའི་ཕྱིར་རོ། །

[Block 3819]
འདི་དག་ནི་སྔར་བསྟན་པ་རྣམས་ཏེ། གྲུབ་པ་དྲང་སྲོང་ལ་སོགས་པ་དང་། གང་ཡང་གཞན་དག་ལས་དེའི་གྲགས་པ་ཐོབ་པར་གྱུར་པ་དེས་གཅིག་ལ་གཅིག་བརྒྱུད་དེ་རྒྱས་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3820]
སྐྱེས་དང་འདྲ་བར་གྱུར་ཞེས་བྱ་བ་ནི་གང་ལས་ཐོས་པའི་གྲགས་པ་དེ་ཡང་གཞན་དག་ལ་སྟོན་ཏེ། དེས་ཀྱང་གཞན་དག་ལ་བརྟེན་པ༌[^2481]ཡིན་པས་ཉེ་བར་བརྒྱུད་པ་དེས་ན་སྐྱེས་དང་མཉམ་པར་གྱུར་པའོ། །

[Block 3821]
བློན་པོ་དང་བྲམ་ཟེ་རྒན་པོ༌[^2482]སྨོས་པ་ནི་ཚོགས་པའི་ནང་དུ་སྨྲ་བར་འོས་པ་དང་། ཡོན་ཏན་སྒྲོགས་པའི༌[^2483]ཕྱིར་དང་། ཤེས་རབ་བཀུར་བའི་ཕྱིར་རོ། །

[Block 3822]
གཙུག་ལག་དུ་མ་ལ་གོམས་ཤིང་མཁས་པའི་བློ་གང་ལ་ཡོད་པ་དེ་ནི་གཙུག་ལག་དུ་མ་ལ་གོམས་ཤིང་བློ་དང་ལྡན་པ་རྣམས་སོ། །

[Block 3823]
དེ་ལ་འདིས་ནི་ལྷན་ཅིག་སྐྱེས་པའི་དུལ་བ་དང་ཤེས་རབ་དང་ལྡན་པ་ཡིན་ནོ་ཞེས་བཤད་དོ། །

[Block 3824]
བློན་པོ་བཀའ་ལ་གཏོགས་པ་ཞེས་བྱ་བ་ནི་བློ་ལ་གྲོགས་བྱེད་པའོ། །

[Block 3825]
སྤྱན་སྔར་བྲིམ་དུ་རུང་བ་ཞེས་བྱ་བ་ནི་ལྷན་ཅིག་སྨྲ་བ་དང་། རབ་ཏུ་དགའ་བར༌[^2484]བྱ་བའི་གཏམ་བྱར་རུང་བའོ། །

[Block 3826]
བདེ་བའི་རྒྱུ་ནི་བདེ་བར་འགྱུར་བའོ། །

[Block 3827]
བདེ་བའི་རྒྱུ་ཉིད་ཡོན་ཏན་ཡིན་པས་བདེ་བར་འགྱུར་བའི་ཡོན་ཏན་ཏོ། །

[Block 3828]
བདེ་བའི་རྒྱུའམ་ཁྱད་པར་དུ་གྱུར་པའི་བདེ་བ་སྐྱེད་པའི་རྐྱེན་ནི་མཆོག་གོ། །

[Block 3829]
དེ་བས་ན་སྔར་གྱི་བདེ་བར་འགྱུར་བའི་ཡོན་ཏན་ཉིད་ཁྱད་པར་དུ་གྱུར་པ་དེ་ཐོས་ན་བདེ་བར་འགྱུར་བའི་ཡོན་ཏན་མཆོག་ཐོས་པ་ཡིན་ཏེ། དེ་བས་ན་དེ་གཉིས་མཆི་བ་ལགས་ཏེ། བདེ་བའི༌[^2485]གཞིར་གྱུར་པས་འགུགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3830]
བདེ་བ་ལ་གནས་པར་འདོད་པའི་དབང་གིས་ནི་གང་གི་ཕྱིར། ཚངས་པའི་འཇིག་རྟེན་དུ་སྐྱེས་པ་ལས་ཀྱང་རིགས་པར་མཐོང་བའོ། །

[Block 3831]
བཀའ་མཆིད་གདའ་བ་ཞེས་བྱ་བ་ནི་བདེ་བར་འགྱུར་བའི་ཡོན་ཏན་སྟོན་པ་ཡིན་ནོ། །

[Block 3832]
ཡོན་ཏན་ཁྱད་པར་ཅན་དུ༌[^2486]འཕགས་ཤིང་བཟང་བའི་ཞེས་བྱ་བ་ནི་དེ་ལས་མཆོག་ཏུ་གྱུར་པའོ། །

[Block 3833]
མི་འཇིགས་པ༌[^2487]སྦྱིན་པའི་སྒྲ་བསྒྲགས་པ༌[^2488]ཞེས་བྱ་བ་ཡང་ཅི་ནས་ཀྱང་བྱ་བའི་རིགས་པ་ཡིན་ནོ། །

[Block 3834]
བདེ་བའི་ཡོ་བྱད་ཀྱི་ཡོན་ཏན་ཁྱད་པར་ཅན་ཐོས་ནས་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པ་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 3835]
ལྷ་གཅིག༌[^2489]སེམས་ཅན་ཕལ་ཆེར་ནི། །ཞེས་བྱ་བ་ནི་ཚིགས་བཅད་འདི་ནི་བདེ་བར་འགྱུར་བའི་ཡོན་ཏན་གྱི་མཆོག་ལ་གཅིག་ཏུ་ཆགས་པ་ཡིན་ཡང་བདེ་བའི་རྒྱུས་འགུགས་པ་ཡིན་པར་བསྟན་ཏེ། དེ་ལ༌[^2490]འདྲེན་པའི་ཕྱིར་རོ། །

[Block 3836]
བདག་ཉིད་ཀྱི་བདེ་བའི་རྒྱུར་གྱུར་པའི་ཡིད་བཞིན་གྱི་མཚོ་དེ་ཡོངས་སུ་སྤངས་ནས། ཇི་ལྟར་མཚོ་དེར་འོང་ཞེས་བྱ་བའི་ཚིག་གི་སྐབས་དེའི་ལན་བསྟན་པའི་ཕྱིར། ཡིད་བཞིན་མཚོའི་ཡོན་ཏན་ལ་འགྲན་དུ་རུང་བ་ཞེས་བྱ་བ་ཡིན་ཏེ། ཡོན་ཏན་རྒྱ་ཆེ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3837]
ཡོན་ཏན་རྒྱ་ཆེ་བ་དེ་ཡང་མེ་ཏོག་པདྨ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་བསྟན་པ་ཡིན་ནོ། །

[Block 3838]
ལྗོན་ཤིང་མེ་ཏོག་བཟང་ལྡན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་དགུས་ནི་མཚོ་དེ་ཀུན་ནས་དགའ་བ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3839]
ལྗོན་ཤིང་མེ་ཏོག་བཟང་ལྡན་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་མཚོའི་མཐའ་མ་མཛེས་པའི་དབང་དུ་བྱས་པ་སྟེ། མཐའ་མ་ཡོངས་སུ་བསྐོར་བ་གང༌[^2491]ཡིན་པ་དེ་མཐའ་མ་ཡོངས་སུ་བསྐོར་བའོ། །

[Block 3840]
ཆུའི་རླབས་རྣམས་འཁྲུགས་པ་ནི་ཆུའི་རླབས་འཁྲུགས༌[^2492]པའོ། །

[Block 3841]
དེས་གཡོ་བར་གྱུར་པ༌[^2493]གང་ཡིན་པ་དེ་ནི་ཆུའི་རླབས་འཁྲུགས་པས་གཡོ་བར་འགྱུར་བའོ། །

[Block 3842]
ཟླ་བའི་འོད་ཀྱིས་ཁ་ཕྱེ་བ། །ཞེས་བྱ་བ་ནི་ཟླ་འོད་ཀྱིས༌[^2494]ཁ་ཕྱེ༌[^2495]བའོ། །

[Block 3843]
ཁ་བྱེ་བ་ནི་བསྐུལ་བ་ལྟ་བུ་ཡིན་ཏེ། ཇི་ལྟར་གང་གིས་གཉིད་ཀྱིས་ལོག་པ་ལ། །བསྐུལ་བར་འགྱུར་བ་དེ་བཞིན་དུ་ཀུ་མུ་ཏ་དག་ཀྱང་ཁ་འབྱེད་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར། ཁ་འབྱེད་པ་ཞེས་བརྗོད་དེ། ཟླ་བའི་འོད་ཀྱིས་ཁ་ཕྱེ་བ་ནི་ཇི་ལྟར་གཉིད་ལོག་པ་ལས་བསླང་བ་ལྟ་བུ་ཡིན་ཏེ། རབ་ཏུ་སད་པར་བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3844]
པདྨ་རྣམས་ནི་དགོད་པ་བཞིན། །ཞེས་བྱ་བ་དང་། ཁ་ཅིག་ན་ནི་ཟླ་འོད་ཀྱིས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་ཆུའི་ནང་དུ་མེ་ཏོག་ལ་སོགས་པས་མཚོ་མཛེས་པར་བསྟན་པའོ། །

[Block 3845]
[^2496]པདྨ་ཨུཏྤལ་ཕྱེ་བ་རྣམས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་མཚོའི་མཐའ་མར་གྱུར་པ་མཛེས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 3846]
རླབས་ཉིད་སོར་མོ་ཡིན་པ་སྟེ། དེས་བྲིས་པ་ནི་བཀོད་པའི་ཞེས་བྱ་བའི་དོན་ཏེ། རླབས་ཀྱི་སོར་མོས་བྲིས་པའོ། །

[Block 3847]
ཐམས་ཅད་དུ་ཁྱད་པར་མཛེས་པའི་དབང་དུ་བྱས་ནས། པདྨ་ཨུཏྤ་ལ་འདབ་མ་དག །ཅེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3848]
ཆུའི་ནང་ཉིད༌[^2497]དུ་མཛེས་པའི་དབང་དུ་བྱས་ནས། ཆུ་ནི་རབ་གསལ་མི་གཡོ་བས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 3849]
མཚོའི་ལྷན་ཅིག་སྐྱེས་པའི་མི་ཟད་པས་མཛེས་པའི་དབང་དུ་བྱས་ནས། ལ་ལར་མུ་ཏིག་ཕྲེང་ཆད་བཞིན། །ཞེས་བྱ་བ་དང་། རིག་འཛིན་ན་ཆུང་ཞེས་བྱ་བ་དང་། ཟླ་བའི་ཆུང་མ་སྐར་མ༌[^2498]རྣམས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གསུམ་ཡིན་ཏེ། དེས་ན་གནས་སུ་རུང་ཞིང་མཛེས་པར་བྱས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 3850]
ཟླ་བའི་ཆུང་མ༌[^2499]སྐར་མ་རྣམས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་ཕྱེད་ཀྱིས་ནི་མཐོ་རིས་སུ་སྐྱེས་པའི་སེམས་ཅན་གྱི་ཡང་ཉེ་བར་ལོངས་སྤྱད་དུ་རུང་བ་ལྟ་བུར་ཡོངས་སུ་བརྟགས་ཤིང་རྗེས་སུ་མཐུན་པའོ། །

[Block 3851]
བདེ་བའི་ཡོ་བྱད་དགག་པ་མེད་པ་ཞེས་བྱ་བ་ལ། དགག་པ་མེད་པ་ནི་བྱ་བ་ཐམས་ཅད་ཀྱི་ཐུན་མོང་དུ་གྱུར་པའི་ཕྱིར་ཏེ།[^2500] བདེ་བའི་ཡོ་བྱད་དང་།

[Block 3852 [VERSE]]
མི་འཇིགས་པ་བྱིན་པས་སོ། །
རྒྱལ་པོས་བྱ་རྣམས་ཀུན་ལ་བྱིན། །

[Block 3853]
ཞེས་བྱ་བ་འདིས་ནི་དགག་པ་མེད་པ་ཉིད་བསྟན་ཏོ། །

[Block 3854]
མི་འཇིགས་ཡོན་དང་བཅས་པའི་ཡིད་བཞིན་གྱི་མཚོ་གང་ཡིན་པ་དེ་ནི་མི་འཇིགས་ཡོན་དང་བཅས་པ་སྟེ། འདིས་ནི་བདེ་བའི་ཡོ་བྱད་ཉིད་བསྟན་ཏོ། །

[Block 3855]
སྤྲིན་གྱིས་བྱས་པའི་མུན་པ་ནི་སྤྲིན་གྱི་མུན་པའོ། །
--- END BLOCKS ---
