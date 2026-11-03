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
འདིར་གཞུང་ནི་དགེ་སློང་ཉལ་བར་བྱེད་ན་སོ་སོར་བརྟགས༌[^3933]ཏེ་ཉལ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3817]
དྲན་པ་ཉེ་བར་མ་བཞག༌[^3934]པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་བ་བརྩམས་པ་དང་འབྲེལ་བ་དང་དགེ་བའི་ཕྱོགས་གཞན་དང་འབྲེལ་བ་དང་། དུས་ཇི་ལྟ་བ་བཞིན་དུ་ལྡང་བ་དང་འབྲེལ་བ་དང་ལུས་དང་གོས་མི་འཕྱར་བ་དང་འབྲེལ་བའི་དྲན་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3818]
གཞན་དང་ལྷན་ཅིག་ཁྲིའམ་སྟན་ནམ་གཞན་ལ་ཅིག་ཅར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཉལ་བར་མི་བྱ་བ་སྟེ། གཞན་ལ་ཞེས་སྨོས་པ་ནི་སྟེགས་བུ་ལ་སོགས་པའི་ཁྲི་དག་བསྡུའོ། །

[Block 3819]
ངོ་ཚ་ཤེས་པ༌[^3935]མེད་ན་སྟན་སོ་སོར་བཏིང་སྟེ་གཏུར་བུའམ་ལྷུང་བཟེད་ཀྱི་སྣོད་ལ་སོགས་པས་རབ་ཏུ་བཅད་ནས་དྲན་པ་ཉེ་བར་གཞག་སྟེ་ཉལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་རེག་པའམ་ཀུན་ནས་ཉོན་མོངས་པའི་གཉེན་པོར་གྱུར་པ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་ཤེས་པའོ། །

[Block 3820]
གསུམ་ལས་ལྷག་པ༌[^3936]

[Block 3821]
དང་པོ་དང་ལྷན་ཅིག་ཁྲི་ལ་འཛེགས་པ༌[^3937]བསྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གང་ཟག་གསུམ་ལས་ལྷག་པ་མང་པོ་དང་ལྷན་ཅིག་ཏུ་ཁྲི་གཅིག་གི༌[^3938]སྟེང་དུ་འཛེགས་པ༌[^3939]དང་འདུག་པ་དང་ཉལ་བར་མི་བྱའོ། །

[Block 3822]
གང་ཞིག་ཁྲི་གཅིག་གི་སྟེང་དུ་གང་ཟག་གཉིས་སམ་གསུམ་ནི་འཛེགས་པ༌[^3940]དང་འདུག་པ་དང་ཉལ་བར་བྱའི༌[^3941]བཞི་ཡན་ཆད་ནི་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3823]
ཁྲི་རིང་པོ་ལ༌[^3942]ནི་གཉིས་ལས་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ལྷག་པར་མང་པོ་དང་ལྷན་ཅིག་འཛེག་པ་བསྟེན་པར་མི་བྱ་བའོ།[^3943] །ཁྲིའུ་ལ་གཅིག་མ་ཡིན་པས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཅིག་ཁོ་ན་དེ་ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3824]
དེ་ནི་ཁྲི་ཐུང་ངུའི་དཔེ་ཡིན་པར༌[^3944]རིག་པར་བྱའོ། །

[Block 3825]
ཤིང་གི་ཁྲིའུ་ལ་ཡང་དེ་ལྟ་བུ་ཡིན་ཏེ། དེ་ལྟར་ཁྲིའུ་མེད་པས་དེ་ལ་ཡང་ཁྱབ་པ་ཉིད་ཀྱིས་ཡང༌[^3945]བ་ཉིད་དུ་རྣམ་པར་གཞག་པས་འདིར་དུ་མས་འཛེག་པར་མི་འོས་པ་ཉིད་དོ། །

[Block 3826]
ཤིང་གི་སྤང་ལེབ་ལ་ནི་སྟོབས་ཅི་ཡོད་པ་དང་གོ་ཅི་ཡོད་པ་ལས་ཤེས་པར་བྱའོ། །

[Block 3827]
ལོ་གསུམ་ལས་ལྷག་པས་བར་དུ་ཆོད་པ་དང་ལྷན་ཅིག་སྟན་ལ་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི༌[^3946]ལོ་གསུམ་ལས་ལྷག་པའི་དུས་བསྙེན་པར་རྫོགས་པའི་བར་དུ་གྱུར་པས་བསྙེན་པར་རྫོགས་པའི་དུས་གཞན་གྱིས༌[^3947]བར་དུ་ཆོད་པ་ཉིད་དེ་དང་ལྷན་ཅིག་སྟན་ཐམས་ཅད་ལ་འཛེག་པ་ཉིད་བསྟེན་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 3828]
ཁྱིམ་གཞན་དུ་མེད་ན་མཁན་པོ་དང་ཡང་དྲན་པ་ཉེ་བར་གཞག་སྟེ་སྟན་གཅིག་ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པའི་ཁྱིམ་མམ༌[^3948]གཞན་འགའ་ཞིག་ཏུ་ནི་མ་ཡིན་ནོ། །

[Block 3829]
ཁྱིམ་པ་དང་གང་དུ་ཡང་མི་བྱའོ་ཞེས་བྱ་བ༌[^3949]ནི་ཁྱིམ་པ་དང་ཁྱིམ་གཞན་ཡང་རུང་གཙུག་ལག་ཁང་ཡང་རུང་བ་སྟེ། གང་ཡང་རུང་བར་སྟན་གཅིག་ལ་འདུག་པར་མི་བྱའོ། །

[Block 3830]
བསྙེན་པར་མ་རྫོགས་པ་དང་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ་རྫོགས་པ་དང་གང་དུ་ཡང་སྟན་གཅིག་ལ་འདུག་པར་མི་བྱའོ། །

[Block 3831]
ཟ་མ་དང་མ་ནིང་དང་མ་བསད་པ་ལ་སོགས་པ་དང༌[^3950]མུ་སྟེགས་ཅན་ཞུགས་པ་དང་། རྐུ་ཐབས་སུ་གནས་པ་དང་། ཐ་དད་པར་གནས་པ་དང་། གནས་པར་མི་བྱ་བ་དག་དང་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མ་མོ་ལས་འདི་ལ་སོགས་པ་གསུངས་ཏེ། དེ་དག་གང་དང་གང་དུ་ཡང་རུང་སྟན་གཅིག་ལ་འདུག་པ་བསྟེན་པར་མི་བྱའོ། །

[Block 3832]
བསླབ་པ་བྱིན་པ་དང་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གང་དུ་ཡང་སྟན་གཅིག༌[^3951]ལ་འདུག་པ་བསྟེན་པར་མི་བྱའོ། །

[Block 3833]
ཨར་མོ་ནིག༌[^3952]ནི་བསྙེན་པར༌[^3953]རྫོགས་པ་དང་བཅས་པའི་དགེ་འདུན་འདུས་པ་ལས་གཞན་པར་སྟན་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཨར་མོ་ནིག༌[^3954]ནི་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པའི་དགེ་འདུན་འདུས་པ་ལས་གཞན་པའི་གནས་སུ་སྟན་ཉིད་ཡིན་པའོ། །

[Block 3834]
གང་གི༌[^3955]ཕྱིར་དེ་ལྟ་ཡིན་པ་དེའི་ཕྱིར་དགེ་འདུན་འདུས་པ་ལས་གཞན་པར་ཡང་ཨར་མོ་ནིག་ནི༌[^3956]དེ་ལ་ལོ་གསུམ་ལས༌[^3957]ལྷག་པའི་བར་དུ་ཆོད་པ་དང་ལྷན་ཅིག་འདུག་པ་བསྟེན༌[^3958]པར་མི་བྱའོ། །

[Block 3835]
འདིར་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པ་ཞེས་སྨོས་པ་ནི་བསྙེན་པར་མ་རྫོགས་པ་དག་དང་ལྷན་ཅིག་དགེ་འདུན་ཚོགས་ན་ཡང་འདུག་པར་མི་བྱའོ་ཞེས་བསྟན་པའི་ཕྱིར་སྨོས་སོ། །

[Block 3836]
སྟེགས་བུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྟེགས་བུ་ནི་སར་གྱུར་པ་ཉིད་ཡིན་པས་སྟན་མ་ཡིན་ནོ། །

[Block 3837]
དོགས་པའི་གནོད་པར་གྱུར་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདིར་འདུས་པའི་སྐབས་ཀྱི༌[^3959]བསླབ་པའི་གཞི་དེ་དག་ཐམས་ཅད་ལ་འདི་དམིགས་ཀྱིས་བསལ་བ་ཡིན་ནོ། །

[Block 3838]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་ཁྱིམ་པ་དང་ལྷན་ཅིག་སྟན་ནང་ཚངས་ཅན་གཅིག་ལ་མཆིས་སུ་རུང་ངམ། ཉེ་བ༌[^3960]འཁོར་མི་རུང་སྟེ། རྐྱེན་དེ་ལྟ་བུ་དག་ཡོད་ན་རུང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3839]
གནས་མལ་སྦེད་པ༌[^3961]ན་གལ་ཏེ་གཉིས་ཡོད་ན་གཅིག་གིས་ཁྲིའམ་ཁྲིའུ་བསྐུར་ཞིང་ཅིག་ཤོས་ཀྱིས་སྟན་ནང་ཚངས་ཅན་ལ་སོགས་པའོ་ཞེས་བྱ་བ༌[^3962]ནི་གལ་ཏེ་གང་ཟག་གཉིས་ཡོད་ན་དེ་ལྟར་བསྐུར་བར་བྱའོ། །

[Block 3840]
འདིར་བྱེ་བྲག་ཏུ་མ་སྨོས་པས་དགེ་འདུན་གྱི༌[^3963]འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི༌[^3964]གང་ཟག་གི་ཡང་རུང༌[^3965]ངོ་། །དགེ་འདུན་གྱི་དེ་སྙིང་མི་བརྩེ་བར་མདུན་ནས་དྲང་བ་དང་། གཡས་གཡོན་ནས་དྲང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་གནས་མལ་དེའོ། །

[Block 3841]
ཅི་ནས་ཀྱང་དེ་དུ་བ་དང་རྡུལ་དང་དྲི་མ་དག་གིས་གོས་པར་འགྱུར་བ་དེ་ལྟར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་དེའོ། །

[Block 3842]
དེ་མི་གཙང་བའི་སྐྱབས་དང་ཉེ་བར་བསྟེན་པར་མི་བྱའོ། །

[Block 3843]
ཉམས་པ་དོར་བར་མི་བྱའོ། །

[Block 3844]
བསྲད་པ་དང་སྐམ་པ་དང་སྤྲུག་པ་དང་བུ་གུ་གླན་པར་བྱའོ། །

[Block 3845]
རལ་བ་ན༌[^3966]ལྷན་རིངས་སོ། །

[Block 3846]
དབུས་ཟེགས་ན་མཐའ་གཉིས་དབུས་སུ་བྱའོ། །

[Block 3847]
དེར་འོས་པ་ཁ་བསྒྱུར་རོ། །

[Block 3848]
ཕྱིར་བཅོས་མི༌[^3967]ནུས་ན༌[^3968]དཀོན་མཆོག་ལ་ཕུལ་བའི་མར་མེ་གང་ཟག་སྦྱིན་བདག་ཡིན་པ་གང༌[^3969]ཡང་རུང་བ་དག་གི་སྙིང་པོ་ཉིད་དུ་སྤྱད་དོ་ཞེས་བྱ་བ་ནི་དཀོན་མཆོག་ལ་ཕུལ་བའི་མར་མེ་གང་ཟག་སྦྱིན་བདག་མིན་པ་ཡང་རུང་བ་དག་གིས་སྤྱད་པར་བྱ་སྟེ། དགེ་འདུན་སྦྱིན་བདག་ཡིན་པའི་ཡང་རྣམ་པར་སྦྱར་བར༌[^3970]བྱའོ། །

[Block 3849]
དེར་མི་མཁོ་བ་ཉིད་ཡིན་ན་འཇིམ་པ༌[^3971]དང་བསྲེས་ཏེ་དཀོན་མཆོག་དག་གི་རྩིག་པ་དང་། ཀ་བ་དང་སྒོ་གླེགས་ཀྱི་སེར་ཀ་དག་བྱུག་པའི་ཕྱིར་དེ་ལ་ནན་ཏན་བྱའོ་ཞེས་བྱ་བ་ལ། དེར་མི་མཁོ་བ༌[^3972]ཉིད་ཡིན་ན་ཞེས་བྱ་བ་ནི་མར་མེའི་སྙིང་པོ་དེར་རོ། །

[Block 3850]
དཀོན་མཆོག་དག་གི་ཞེས་བྱ་བ་ནི་དཀོན་མཆོག་དང་འབྲེལ་པ་རྣམས་ལའོ། །

[Block 3851]
དེ་ལ་ནན་ཏན་བྱའོ་ཞེས་བྱ་བ་ནི་བསྲད་པ་ལ་སོགས་པ་དེ་རྣམས་ལ་ནན་ཏན་བྱ་བའོ། །

[Block 3852]
གནས་མལ་ཇི་ལྟ༌[^3973]བུར་གྱུར་པ་སུས་བསྲད་པ་ལ་སོགས་པའི་ནན་ཏན་བྱ་ཞེ་ན། དེའི་ཕྱིར་བསྐོས་པ་ནི་མནོས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྐོས་པ་གང་ཡིན་པ་དེས་སུ་ཞིག་ལ་སྦྱིན་པ་སྟེ། བསྐོས་པ་མནོས་པས་བསྲད་པ་ལ་སོགས་པ་རྗེས་སུ་བསྒྲུབ་པར་བྱའོ། །

[Block 3853]
ལྷག་མ་ནི་དགེ་འདུན་གཎྜཱི་བརྡུངས་པས་བསྡུས་ཏེའོ་ཞེས་བྱ་བ་ལ། ལྷག་མ་བསྐོས་པ་ནི་དགེ་འདུན་གྱིས་བསྲད་པ་ལ་སོགས་པ་དེ་དག་བསྡུས་ཏེ་བསྒྲུབ་པར་བྱ་ཇི་ལྟར་བསྡུས་ཏེ་བསྒྲུབ༌[^3974]པར་བྱའོ༌[^3975]ཞེ་ན། དེའི་ཕྱིར་གཎྜཱི་བརྡུངས་པས་བསྡུས་ཏེའོ་ཞེས་བྱ་བ་སྨོས་ཏེའོ།[^3976] །དགེ་འདུན་གྱི་རྐུ་འཕྲོག་བྱེད་པ་མཐོང་ལ་ནུས་ན་མི་བཟློག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། རྐུ་འཕྲོག་ནི་དཔེ་ཙམ་དུ་ཟད་དེ། ཆུད་ཟ་བར་འགྱུར་བ་དག་ལ་ཡང་ཆོ་ག་དེ་བཞིན་དུ་བསྒྲུབ་པར་བྱའོ། །

[Block 3854]
བསྐྲད་པ་ན་དགེ་འདུན་གྱིས་ཡལ་བར་མི་དོར་རོ། །

[Block 3855]
གནས་སུ་མ་སོན་གྱི་བར་དུ་ཁྱེར་བར་བྱེད་པས་ལོངས་སྤྱོད་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསྐྲད་པ་ནི༌[^3977]དགེ་འདུན་གྱི་དངོས་པོ་ཡལ་བར་དོར་ཏེ་བླངས་པ་གང་ཡིན་པ་དེ་ནི་དགེ་སློང་གི་གནས་སུ་མ་སོན་གྱི་བར་དུ་གང་གིས་ཁྱེར་བར་བྱེད་པའི་གང་ཟག་དེ་ཉིད་ཀྱིས་ལོངས་སྤྱད༌[^3978]པར་བྱ་བ་ཉིད་ཡིན་པའོ། །
--- END BLOCKS ---
