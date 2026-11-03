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
[Block 3781]
ཆུས་བརླན་པས་ལུས་ཀྱང་བྱུག་གོ་ཞེས་བྱ་བ་ནི་རྫས་ཀྱི་ངོ་བོ༌[^3878]བསྟན་པས་ལག་པ་ལ་སོགས་པ་རྣམས་གང་ཡང་རུང་བ་དེས་ཞེས་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 3782]
སྣུམ་བག་གི་ཉེད་པ༌[^3879]བྱའོ་ཞེས་བྱ་བ་ནི་ཚེས་བརྒྱད་དང༌[^3880]བཅུ་བཞི་དང་བཅོ་ལྔ་ལའོ། །

[Block 3783]
དཀོན་མཆོག་གི་དོན་དུ་ཕྱག་དར་བྱས་པ་དང་ཞལ་ཞལ་བྱས་པ་དང་། དྲི་གཙང་ཁང་དང་སྐུ་གཟུགས་དང་མཆོད་རྟེན་དང་སྲོག་ཤིང་གི་གྲིབ་མ་ལ་གཙུག་ལག་གི་ཚིགས་སུ༌[^3881]བཅད་པ་གདོན་ཅིང་འགོམ་མོ་ཞེས་བྱ་བ་ལ། འདིར་ཞལ་ཞལ་ཞེས་བྱ་བ་ནི་བྱུག་པ་ལ་རིག་པར་བྱའོ། །

[Block 3784]
ཉི་མ་དེ་ཉིད་ལ་གནས་མལ་ལ་སོ་སོར་བརྟགས་ལ༌[^3882]དེས་བཅོས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཚེས་བརྒྱད་དང༌[^3883]བཅུ་བཞིའི་ཉི་མ་དེ་དག༌[^3884]ལའོ། །སུས་དེ་ལ་སོ་སོར་བརྟག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་རྡོལ་བ་ལ་སོགས་པ་དང་ལྡན་པ་དག་གིས་སོ༌[^3885]ཞེས་བྱ་བ་སྨོས་ཏེ་མལ་ཆ་ལ་སོགས་པའོ། །སུས་བཅོས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གནས་པ་དག་གིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དག་ཉིད་ཀྱིས་འདིར་མཁན་པོ་དང་སློབ་དཔོན་དག་གིས༌[^3886]མལ་སྟན་ལ་སོགས་པ་བཅོས་པར་བྱའོ། །

[Block 3785]
གནས་མལ་གྱི་གཞིར༌[^3887]ཆག་ཆག་དང༌[^3888]ཕྱག་དར༌[^3889]དང་། ལྕི་བ་འཇམ་པོའི་བྱུག་པས༌[^3890]བསྐུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མ་མོ་ལས་འདི་དང་པོར་བྱས་ནས་བཀྲུའོ༌[^3891]ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3786]
མལ་ཆ་དྲི་མས་གོས་པ་སྤྲུག་པར་བྱའོ། །

[Block 3787]
གལ་ཏེ་ཧ་ཅང་ན་སྤྲུག་པར༌[^3892]བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཧ་ཅང་དྲི་མ་ཅན་དུ་གྱུར་ན་འགྱུར་བྱེད་ཀྱི་ཆུ་ལ་སོགས་པས་བཀྲུ༌[^3893]བར་བྱའོ། །

[Block 3788]
ཆག་ཆག་གདབ༌[^3894]པའི་འོག་ཏུ༌[^3895]ཕྱག་གོ། །

[Block 3789]
དེའི་འོག་ཏུ་བཤམ་མོ་ཞེས་བྱ་བ་ནི་ཕྱག་དར་བྱས་པའི་འོག་ཏུ་མལ་དང་སྟན་བཤམ་པར་བྱའོ། །

[Block 3790]
གཞི་རྡུལ་དང་བཅས་པ་མ་སྤྲུགས་པ་ལ་མི་བྱའོ་ཞེས་བྱ་བ༌[^3896]མལ་དང་སྟན་གྱི་གཞི་ཁྲི་ལ་སོགས་པ་རྡུལ་དང་བཅས་པ་ཉིད་ཡིན་ན་དེ་མ་སྤྲུགས་པའི་སྟེང་དུ་མལ་དང་སྟན་བཤམ་པར༌[^3897]མི་བྱའོ། །

[Block 3791]
བཤམ་པར་བྱ་བ་དག་ལ་གོས་ཅིག་སྤྲུག༌[^3898]པར་སྤྱད་དོ་ཞེས་བྱ་བ་ནི་མལ་སྟན་བཤམ་པར་བྱ་བ་དེ་དག་གིའོ། །

[Block 3792]
གོས་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན་དེའི་ཕྱིར། ངན་པའོ་ཞེས་བྱ་བ༌[^3899]སྨོས་ཏེ་ཐམས་ཅད་ཀྱི་ཐ་མའོ། །

[Block 3793]
དེ་བཅོས་སོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ཕྱིར་བཅོས་པ་དེའོ། །

[Block 3794]
སྤྲུག་པའི་དོན་དུ༌[^3900]སྤྱད་པའི་དོན་གོས་ངན་པ་དེའོ། །

[Block 3795]
མི་ནུས་པ་ཉིད་ན་རས་མར་བྱས་ཏེ་ཤིང་བུའི་རྩེ་མོ་ལ་བཏགས་ནས་སྤྲུག་གོ་ཞེས་བྱ་བ་ནི་དེས༌[^3901]ཁྲི་ལ་སོགས་པ་དག་སྤྲུག་གོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3796]
དེ་ལྟར་ཡང་མི་རུང་བ་ཉིད་མ༌[^3902]ཡིན་ན། སྦྱིན་པ་པོའི་བསོད་ནམས་མངོན་པར་སྤེལ་བ་དང་ཡུན་རིང་བ་ཉིད་དུ་བྱ་བའི་ཕྱིར་ལྕི་བ་དང་ས༌[^3903]བསྲེས་ཏེ་ཀ་བ་དང་རྩིག་པའི་སེར་ཀར༌[^3904]གླན་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལྟར་ཡང་ཞེས་བྱ་བ་ནི་དེ་ལྟར་བྱས་ཀྱང་མི་རུང་བ་ཉིད་ཡིན༌[^3905]ནའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3797]
སྒོ་ཁང་དང་ཁྱམས་སུ་མལ་བཅའ་བ་དང་བཅས་ན་ཡང་གཟུང་བར༌[^3906]མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་དག་ཏུ་མལ་བཅའ་བར་ཡང་མི་བྱ་གཞན་གྱིས༌[^3907]བཅས་ན་ཡང་རང་གིས་གཟུང་བར༌[^3908]མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3798]
འདིར་བརྟགས་པ་ནི་སྐྱོན་ཡིན་ཏེ་གཟུང་བས༌[^3909]ཀྱང་ངོ་། །

[Block 3799]
གཞན་གྱིས་བཅས་ན་ཡང་གནས་ཁང་ཡོངས་སུ་གྱུར་པ་ལ་སོགས་པ་རང་ལ་རག་ལས་པ་ཉིད་ཐོབ་པ་ལ་ཉེས་པ༌[^3910]སྤང་བར་བྱའོ། །

[Block 3800]
སྦྱིན་པ་པོས༌[^3911]མྱ་ངན་བསང་བའི་ཕྱིར་ཕུལ་བ་དེས་མཐོང་བར་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རྒྱལ་པོ་གསལ་རྒྱལ་གྱིས་རང་གི་མ་ཤི་བའི་མྱ་ངན་བསང་བའི་ཕྱིར། མའི་མལ་ཁྲི་དགེ་འདུན་ལ་ཕུལ་བ་དགེ་སློང་གིས་སྒོ་ཁང་དང་ཁྱམས་སུ་བཤམས་པ༌[^3912]རྒྱལ་པོས་མཐོང་ནས། ཡང་མྱ་ངན་ལངས་པ་བྱུང་བའི་མཐའ་ལས་བཅས་པ་ཡིན་ཏེ། དེ་ལྟ་བུའི་རྫས་སྦྱིན་བདག་གིས་མཐོང་བར་མི་བྱའོ། །

[Block 3801]
སྒྲ་མི་སྙན་པའི་གཉེན་པོའི་ཕྱིར་ཚེས་བརྒྱད་དང༌[^3913]བཅུ་བཞི་དག་ལ་ཁྱམས་སུ་བཤམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་རྣམས་ཀྱིས་མལ་ཁྲི་དེ་བཀྲུས༌[^3914]སོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲ་མི་སྙན་པའོ། །

[Block 3802]
དེ་བསལ་བའི་གཉེན་པོའི་ཕྱིར་བཤམ་ཞིང་གཞན་གྱིས༌[^3915]མཐོང་བར་བྱ་བའོ། །

[Block 3803]
ཁྲི་དང་ཁྲིའུ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མ་སྨོས་པའི་ཕྱིར་གང་ཟག་གིས་ཀྱང༌[^3916]ངོ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 3804]
མ་མོ་ལས་འདི་ནི་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3805]
སྤྱིལ་བ་མི་ཉམས་པར༌[^3917]བྱ་བའི་ཕྱིར་ཁྲི་རྐང་གི་མཐིལ་མཉམ་པར་སྤྱད་པར་བྱའོ། །

[Block 3806]
ཡང་དེའི་འོག་ཏུ་ཕུབ་མའི་ཕུང་པོ་གཞག་པའམ་དེ་རས་མས་དཀྲི་བར་བྱའོ་ཞེས་བྱ་བ་ལས།

[Block 3807]
[^3918] དེའི་ཞེས་བྱ་བ་ནི་ཁྲིའུའི༌[^3919]རྐང་པ་དེའི་འོག་ཏུའོ། །

[Block 3808]
དགེ་འདུན་མ་ཡིན་པས་རྐང་པ་དཀྲིས་པའི༌[^3920]ཁྲིའུ་བསྟེན་པ་བདག་གིར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སིལ༌[^3921]བུ་དག་ལས་སྒྲོན་མའི་ཤིང་ཤེས༌[^3922]པར་བྱ་བའི་བར་དུ་ཡང་ངོ་། །སྟན་བཟང་པོ་དང་རྒྱབ་རྟེན་དང་བཅས་པའི་སྟན་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ཡང་དགེ་འདུན་མ་ཡིན་པས་བདག་གིར་བྱ་བ་བསྟེན་པར་མི་བྱ་བའོ།[^3923] །མར་མེའི་སྡོང་བུ༌[^3924]ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ནི༌[^3925]ཤིང་ལྗོན་པའི་རྣམ་པ་འདྲ་བའི་མར་མེའི༌[^3926]སྡོང་བུ་ཡང་དགེ་འདུན་མ་ཡིན་པས་བདག་གིར་བྱ་བ་བསྟེན་པར་མི་བྱ་བའོ། །

[Block 3809]
འདིར་གཞུང་ནི། དགེ་འདུན་ལ་ནི་ཡལ་ག་གཅིག་པའི་མར་མེའི་སྡོང་པོ་རྙེད་ན་ཡང་རྗེས་སུ་གནང་ངོ་། །གང་ཟག་ལ་ནི་རྗེས་སུ་མ་གནང་ངོ་། །ཡལ་ག་གཉིས་པ་དང་མང་པོ་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3810]
ཁ་ཅིག༌[^3927]ལས་ནི་ཡལ་ག་དུ་མ་པ་ཞེས་སོ་ཞེས༌[^3928]བྱ་བ་ནི་ལུགས་ཁ་ཅིག་ལས་ནི་ཡལ་ག་དུ་མ་དང་ལྡན་པའི་མར་མེའི་སྡོང་པོ་དགེ་འདུན་མ་ཡིན་པས་བདག་གིར་བྱ་བ་བསྟེན་པར་མི་བྱའོ། །

[Block 3811]
ཡལ་ག་གཅིག་དང་ལྡན་པ་བདག་གིར་བྱས་པ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་འབྱུང༌[^3929]ངོ་། །སྟན་ནང་ཚངས་ཅན་གྲུ་བཞི་དང་སྔས་ནང་ཚངས་ཅན་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མ་གཏོགས་པའི་ཕྱིར་ཐམས་ཅད་ཀྱིས་བཅང་བར་རྟོགས་པར་བྱའོ། །

[Block 3812]
སྟན་ནང་ཚངས་ཅན་ཞེས་བྱ་བ་ནི་ཤིང་བལ་ཅན་ནོ། །

[Block 3813]
འདིར་གཞུང་ནི་མ་མོ་ལས་སྟན་ནང་ཚངས་ཅན་གྲུ་བཞི་དང་སྔས་ནང་ཚངས་ཅན་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3814]
སྔས་ནང་ཚངས་ཅན་གྱི་ངོ་བོ་བསྟན་པའི་ཕྱིར་ཁྲུ་བཞི་པ་དང་དོ་པ་ཉིས་བལྟབ་ཏུ་བྱ་སྟེ། བཙེམ་མོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྲིད་དུ་ནི་ཁྲུ་བཞི་པ་ཉིས་བལྟབ་དང་ཞེང་དུ་ནི་ཁྲུ་དོ༌[^3930]པ་ཉིས་བལྟབ་ཏུ་བྱས་ཏེ་བཙེམ༌[^3931]མོ། །

[Block 3815]
ཤིང་བལ་གྱིས་བརྫང་ངོ་། །སོ་སོར་བརྟག་པ་མ༌[^3932]བྱས་པར་ཉལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མལ་དང་སྟན་འདི་ལ་སོ་སོར་བརྟག་པ་མ་བྱས་ན་སོ་སོར་བརྟག་པ་མ་བྱས་པ་ཞེས་བྱ་བ་འདིས་བསྡུས་པའོ། །

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
--- END BLOCKS ---
