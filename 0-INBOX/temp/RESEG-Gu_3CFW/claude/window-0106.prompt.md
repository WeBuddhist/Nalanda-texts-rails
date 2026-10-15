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
[Block 3711]
མུཉྫ་ལས་བྱས་པ་དང་། བལ་བ་ཛ་ལས་བྱས་པ་དང་། ཤ་ན་ལས་བྱས་པ་དང་། རས་བལ་ལས་བྱས་པའོ༌[^3812]ཞེས་བྱ་བ་ནི་གླེང་གཞི་དག་ལས་དེ་གསུངས་པ་དང་། འདིར་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས་ཀྱང་དྲ་བ་ནི་རྣམ་པ་ལྔ་སྟེ། ལྔ་གང་ཞེ་ན། ཤ་ན་ལས་བྱས་པ་དང་། མུཉྫ་ལས་བྱས་པ་དང་། བལ་བ་ཛ་ལས་བྱས་པ་དང་། ཀ་ཤ་ལས་བྱས་པ་དང་། ཀུ་ཤ་ལས་བྱས་པའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ།[^3813] དེ་དག་ནི་འགལ་བར་ཤེས་པར་མི་བྱ་སྟེ། དེ་ནི་གཉིས་ཀ་ལ་ཡང་དཔེ་ཉིད་དུ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 3712]
བལ་བ་ཛ་སྨོས་པས་ནི་སྔར་གྱི་ཀ་ཤ་ལས་བྱས་པ་དང་། ཀུ་ཤ་ལས་བྱས་པ་དག་ཀྱང་འཕངས་པར་ཤེས་པར་བྱའོ། །

[Block 3713]
ཤ་ན་ལས་བྱས་པ་ཞེས་སྨོས་པས་ནི་ཕྱི་མ་རས༌[^3814]བལ་ལས་བྱས་པ་ཡང་འཕངས་སོ། །

[Block 3714]
གྲུ་བཞི་དག་ཏུ་གཟུངས༌[^3815]གཟེར་གདབ་བོ། །

[Block 3715]
དེ་དག་ལ་ཡང་གདགས་སོ་ཞེས་བྱ་བ་ནི་གཟུངས༌[^3816]གཟེར་དེ་དག་ལ་བྱ་རྒྱ་གདགས་སོ། །

[Block 3716]
ཤིང་གི་ནི་འཆག་པ༌[^3817]དང་འདྲུལ་བས༌[^3818]དེའི་ཕྱིར་ལྕགས་ལས་བྱས་པ་དག་གོ་ཞེས་བྱ་བ་ནི་གཟུངས་གཟེར་གདགས་པའོ། །

[Block 3717]
དེའི་ཕྱོགས་གཅིག་ཏུ་མཐོངས་གདོད་དོ་ཞེས་བྱ་བ་ལ་དེའི་འོ་ཞེས་བྱ་བ་དེ་ནི་བྱ་རྒྱ་དེའི་འོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ཟས་ཟོས་ཟིན་ནས་འཇུག་པའི༌[^3819]ཕྱིར་རོ་ཞེས་སྨོས་ཏེ། ཁྭ་ཏ་ལ་སོགས་པ་རྣམས་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་ཤེས་པའོ། །

[Block 3718]
དེ་དྲོ་ཀར་དགབ་བོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་མཐོངས་དེའོ། །

[Block 3719]
དབྱར་དག་ཁྱམས་སུ་ཆུ་མི་འབྱུང་བར་བྱ་བའི་ཕྱིར་སྤང་ལེབ་དག་གོ་ཞེས་བྱ་བ་ནི་གཞུག་གོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3720]
ཕྱོགས་གང་དུ་ཞེ་ན་དེའི་ཕྱིར་ཀ་བའི་བར་དག་ཏུའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3721]
ཅི་ཐམས་ཅད་དུའམ༌[^3820]ཞེ་ན་དེའི་ཕྱིར་སྣང་བར་བྱ་བའི་ཕྱོགས་མ་གཏོགས་པར་རོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3722]
མེད་ན་སེག་དག་གམ་རེ་ལྡེ་དག་གོ་ཞེས་བྱ་བ་ནི་སྤང་ལེབ་དག་མེད་ན་སེག་དག་གམ་རེ་ལྡེ་དག་གཞུག་པར་བྱའོ། །

[Block 3723]
དབྱར་གྱི་ཟླ་བ་བཞི་པོ་དག་གི་མཐར༌[^3821]དེ་དབྱུང་ངོ་ཞེས་བྱ་བ་ནི་སྤང་ལེབ་ལ་སོགས་པའོ། །

[Block 3724]
འཁོར་གྱི༌[^3822]ཁྱམས་བྱའོ་ཞེས་བྱ་བ་ལ།[^3823] ཁྱམས་ནི་ཀུན་ནས་ཟླུམ་པ༌[^3824]སྟེ་འཁོར་གང་ལ་ཡོད་པ་དེ་ནི་ཁྱམས་ཟླུམ་པའོ། །

[Block 3725]
གནས་བསིལ་བར༌[^3825]བྱ་བའི་ཕྱིར་ཕྱི་རོལ་རྩིག་པས་བསྐོར་བར་བྱའོ། །

[Block 3726]
ཀ་བའི་ཚར་དག་གཟུགས་སོ་ཞེས་བྱ་བ་ནི་རྩིག་པའི་ཕྱི་རོལ་དུ་གྱུར་པ་ལ་རིག་པར་བྱའོ། །

[Block 3727]
ཀ་བའི་ཚར་དག་གཟུགས་སོ་ཞེས་བྱ་བར༌[^3826]སྦྱར་རོ། །

[Block 3728]
སྐར་ཁུང་གདོད་དོ་ཞེས་བྱ་བ་ནི་དེར་སྐར་ཁུང་མང་པོ་དག་གདོད་པར་བྱའོ་ཞེས་བྱ་བ་སྟེ་མང་པོའི་མཐའ་ཅན་ནོ། །

[Block 3729]
མ་མཐའ་དག་སྟན་གྱི་ཡ་མཐའ་དང་ཐད་ཀར་བབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི། སྟན་ཚད་མ་དག་གི༌[^3827]མཐའ་དང་མཉམ་པའི་མ༌[^3828]མཐའ་དང་ཡ་མཐའ་གང་ལ་ཡོད་པ་ཐད་ཀར་བབ་པར་འགྱུར་བ་དེ་ལྟ་བུར་འཁོར་གྱི་ཁང་པ་དེར་སྐར་ཁུང་དག་གདོད་པར་བྱའོ།[^3829] །དྲ་བ་དང་སྒོ་གླེགས་དག་གཞུག་གོ། །

[Block 3730]
ཟས་དང་མེ་དང་དཔོང༌[^3830]ས་དང་འཆག་པའི༌[^3831]ཁང་པ་དག་བྱའོ་ཞེས་བྱ་བ་ནི་ཟས་ལ་སོགས་པ་རྣམས་ལ་ཁང་པའི་སྒྲ་སོ་སོར་སྦྱར་བར་བྱ་བའོ།[^3832]

[Block 3731]
།མ་མོ་ལས།

[Block 3732]
འདི་དང་བོར་བྱ་སྟེ། རྩིག་ངོས་ཀྱི་ཕྱོགས་ཀྱི༌[^3833]གསལ་བ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3733]
གཡོགས་པའི་རྩིག་ངོས་ཀྱི་ཕྱོགས་སུ་ཀུན་ནས་བསྐོར་བའི་ལྷག་མ་དང་བཅས་པ་ཞེས་བྱ་བ་དེའི༌[^3834]དོན་དུ་མཐོང་བ་ཡིན་ནོ། །

[Block 3734]
དེ་བས་ན་དེ་བྱེད་པ་ནི་གནས་པའི་ཕྱིར་ནི་མ་ཡིན་ཏེ། རྩིག་ངོས་ཀྱི་ཕྱོགས་འཁོར་བར་གློ་འབུར༌[^3835]དག་བྱའོ་ཞེས་བྱ་བ་ནི་རྩིག་ངོས་ཀྱི་བདག་ཉིད་ངོས་གཅིག་ཏུ་ཀུན་ནས་བསྐོར་བ་གྲུབ་པ་ལ་ཉེ་བར་བརྟེན་ཏེ་ཁང་པ་བྱའོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3735]
ས་ཁྱིམ་རུང་ངོ་། །དགྲ་ཁང་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དག༌[^3836]གི་གནས་སུ་རུང་བ་སྟེ། འདིར་དགྲ་ཁང་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་གི་གྲྭ༌[^3837]དག་གི༌[^3838]ཡང་ཐོག༌[^3839]ལ་སོགས་པ་སྟེ། ཕ་རོལ་གྱི་མཚོན་རྡུགས༌[^3840]པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3736]
འདི་ལ་ལན་ཀན་གྱི་སྐབས་ནི་ཁྱམས་དང་འདྲའོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་དགྲ་ཁང་ལའོ། །

[Block 3737]
མི་ལྟུང་བར་བྱ་བའི་ཕྱིར་ལན་ཀན་བྱ་བ་དང་མི་འགུལ་བར་བྱ་བའི་ཕྱིར་ཤར་བ་གཞུག་པ་དང་། དེ་ལྕགས༌[^3841]ཀྱི་གཟེར་བུ་དག་གིས༌[^3842]སྦྱར་བ་ཞེས་བྱ་བ་གཞན་རྣམས་ལ་ཡང་སྦྱར་བའོ། །

[Block 3738]
རབ་ཏུ་བྱུང་བའི་ཀུན་དགའ་ར་བ་རྩིག་པས་བསྐོར་བ༌[^3843]ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་རུང་ངོ་ཞེས་བྱ་བའི་རྗེས་སྙེག༌[^3844]པའི་ཕྱིར་ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3739]
རྩིག་པ་ལ་ཆུ་ཁུང་གདོད་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བའི་ཀུན་དགའ་ར་བ་གང་ཡིན་པ་དེ་ལ་ཆུ་ཁུང་གདོད་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་རུང་བའོ། །

[Block 3740]
རྩང་དང་འོབས་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་རབ་ཏུ་བྱུང་བའི་ཀུན་དགའ་ར་བ་དེ་དག་གིས་བསྐོར་བ་ཉིད་ཀྱང་རུང་བའོ། །

[Block 3741]
གང་ཟག་གི་གཙུག་ལག་ཁང་ཡོ་བྱད་དང་བཅས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་རུང་བའོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ལན་ཀན་དང་དྲ་བ༌[^3845]དང་ཟས་ཀྱི་ཁང་པ་ལ་སོགས་པ་ཡོ་བྱད་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3742]
སྔོན་པོ་ལ་སོགས་པ་ཟད་པར་གྱི་མཚན་མ་མངོན༌[^3846]དུ་བྱ་བའི་ཕྱིར་གནས་ཁང་གི་རྩིག་པ་དག་སྔོན་པོ་ལ་སོགས་པ་རྣམ་པ་བཞིར་བྱའོ་ཞེས་བྱ་བ་ནི་ཟད་པར་སྔོན་པོ་དང་ཟད་པར་སེར་པོ་དང་ཟད་པར་དམར་པོ་དང་ཟད་པར་དཀར་བའི་སྐྱེ་མཆེད་ཀྱི་མཚན་མ་དག་མངོན་དུ་བྱ་བའི་ཕྱིར། གནས་ཁང་གི་རྩིག་པ་དེ་དག་སྔོན་པོ་ལ་སོགས་པ་ཁ་དོག་རྣམ་པ་བཞིར་བྱ་བའོ། །

[Block 3743]
འདིར་གཞུང་ནི་དགེ་སློང་ཞིག་ཟད་པར་སྔོན་པོའི་སྐྱེ་མཆེད་ཀྱི་སྙོམས་པར་འཇུག་པ་སྒོམ་པར་བྱེད་པའི་དགེ་སློང་དེ་ལ་རེ་ཞིག་མངོན་དུ་མི་འགྱུར་བ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གནས་ཁང་གི་རྩིག་པ་སྔོན་པོ་དང་སེར་པོ་དང་དམར་པོ་དང་དཀར་པོ་རྣམ་པ་བཞི༌[^3847]བྱ་སྟེ།[^3848] དེ་དག་མཐོང་ནས༌[^3849]མངོན་དུ་བྱ་སྟེ། ཟད་པར་སྔོན་པོའི་སྐྱེ་མཆེད་ཀྱི་སྙོམས་པར་འཇུག་པ་བསྒོམ་པར༌[^3850]བྱའོ་ཞེས་གསུངས་སོ། །

[Block 3744]
རབ་ཏུ་བྱུང་བའི་ཀུན་དགའ་ར་བ་ལ་རི་མོ་བྲི་བ་ཉིད་དུ་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་ན། གང་དུ་ཅི་ཞིག་བྲི་བར་བྱ༌[^3851]ཞེ་ན། དེའི་ཕྱིར་སྒོར་གནོད་སྦྱིན་ལག་ན་རྡོ་རྗེ་འཛིན་པ་ལ་སོགས་པ་རྣམས་བྲིའོ། །

[Block 3745]
སྒོ་ཁང་དུ་འཁོར་བའི་འཁོར་ལོའོ་ཞེས་བྱ་བ་ཡང་རི་མོ་བྲི་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །ཅི་འདྲ་བ་ཞེ་ན། དེའི་ཕྱིར་ཆ་ལྔ་པར་སྦྱར་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཆ་ལྔ་པ་ཞེས་བྱ་བའི་སྒྲས་ནི་འགྲོ་བ་ལྔ་པོ་དག༌[^3852]བསྟན་ཏེ། ལྷ་དང་མིའི་ཆ་དག་ཕྱོགས་གང་དུ་བྲི་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དེའི་སྟེང་དུ་ལྷ་དང་མི་རྣམས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ནས་འོག་གི་ཕྱོགས་དག་ཏུ་སེམས་ཅན་དམྱལ་བ་དང་དུད་འགྲོ་དང་ཡི་དགས་ཀྱི་འགྲོ་བ་རྣམས་བྲི་བར་ཞར་ལ༌[^3853]ཤེས་པར་བྱའོ། །

[Block 3746]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 3747]
འདི་དང་པོར་བྱ་སྟེ་གཞག་པར་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3748]
གླིང་བཞི་པོ་དག་གོ་ཞེས་བྱ་བ་ཡང་བྲི་བར་བྱའོ། །

[Block 3749]
རྫུས་ཏེ་སྐྱེ་བའི་སེམས་ཅན་ཟོ་ཆུན་རྒྱུད་མོ་བཞིན་དུ་འཆི་འཕོ་བ་དང་སྐྱེ་བ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་རི་མོར་བྲི་བར་བྱའོ། །

[Block 3750]
དབུས་སུ་འདོད་ཆགས་དང་ཞེ་སྡང་དང༌[^3854]གཏི་མུག་དག་ཕུག་རོན་དང་སྦྲུལ་དང་ཕག་གི་རྣམ་པར་རོ་ཞེས་བྱ་བ་ནི་དེ་དག་གྲངས་ཇི་ལྟ་བ་བཞིན་དུ་རི་མོར་བྲི་བར་བྱའོ། །
--- END BLOCKS ---
