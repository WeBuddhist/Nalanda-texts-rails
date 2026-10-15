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
ཁ་བསྐང་བ་ལ་རེ་བ་མེད་ན་ཆུང་བ་ཁྲུ་གང་ཡན་ཆད་ཀྱང་ཆོག་པ་དང་འདྲའོ་ཞེས་བྱ་བ༌[^2626]ནི་འཁོར་གསུམ་ཁེབས་པའི་མཐའི་ཚད་བཞིན་དུ་འཛིན་པ་དང་། བསླབ་པའི་གཞི་ལས་འདི་ཞུགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3817]
མེད་ན་ཞེས་བྱ་བ་ནི་གནས་མ༌[^2627]ཟིན་པ་ལ་འདིར༌[^2628]ཇི་ལྟར་རྣམ་པ་གང་གིས་ཀྱང་བསྒྲུབ་པ་ཡིན་ཏེ། ཕྱིར༌[^2629]འོང་བ་ལ་སྡོད་པ་ནི་རེ་བ་དང་བཅས་པར་རིག་པར་བྱའོ། །

[Block 3818]
འདིར༌[^2630]ཆད་ནི་རེ་བ་ཀུན་ནས་ཆད་པའོ། །

[Block 3819]
འདིར་གཞུང་ནི་དེ་ཆོས་གོས་ལ་རེ་བ་གང་ཡིན་པ་དེ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་རྒྱུན་ཆད་པར་གྱུར་ན་དགེ་སློང་དེས༌[^2631]གོས་དེ་ཉི་མ་བཅུ་པ་དེ་ཉིད་ཀྱི་ནང་རོལ་དུ་གཏང་བར༌[^2632]བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཆོག་པ་ཞེས་བྱ་བ་གང་ཞིག༌[^2633]དེར་ཁ་བསྐང་བར་གསུངས་པ་འཁོར་གསུམ་ཁེབས་པའི་མཐའི་ཚད་དུ་འདི་ཆོག་པར་སྔ་མ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་ཁྲུ་གང་ཡན་ཆད༌[^2634]ཁ་བསྐང་བ་པོ་ལ་རེ་བ་མེད་པར་གྱུར་ན་ཁྲུ་གང་ཡན་ཆད་དུ་ཆོག་པ་དེ་ཞག་བཅུའི་མཐར་ཐུག་པར་བཙང་བར་བྱའོ། །

[Block 3820]
ཡོད་ན་ནི་ཁྲུ་གང་ཡན་ཆད་ཉེ་བར་བསྐུལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་རྣམ་པར་གཞག་པ་འདིའོ། །

[Block 3821]
བྱིན་གྱིས་བརླབ་པར༌[^2635]བྱ་བ་ཡོད་པ་ཉིད་ཡིན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཁ་བསྐང་བ་བཞིན་དུ་རྫོགས་པར་གྱུར་པ་ལ་ཁྲུ་གང་ལས་ཆོག་པ་དང་འདྲ་བར་བལྟ་བར་བྱའོ། །

[Block 3822]
འདིར་གཞུང་ནི་མདོའི་ཚིག་ལས་ཆུང་ན་ཁ་བསྐང་བར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 3823]
བྱིན་གྱིས་བརླབ་པར༌[^2636]བྱ་བ་ལ་འདི་འདིར་ཁ་བསྐང་བ་ཉིད་དུ་མངོན་པར་འདོད་པ་དེ་གང་གི་ཕྱིར་འདིར་དེའི་རྣམ་པར་འབྱེད་པ་ནི་འདི་ཡིན་ཏེ་མ་ཆོག་པ་ཁ་བསྐང་བའི་དོན་དུ་འམ་ཞེས་བྱ་བ་ནི་སྣམ་སྦྱར་གྱི་འམ་མཐང་གོས་ཀྱིའོ་ཞེས་བྱ་བས་འདིར་འམ་གྱི་སྒྲ་ནི་ཉམས་པ་མཐོང་བ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3824]
ཕྲན་ཚེགས་ཀྱི་ཞུ་བ༌[^2637]པའི༌[^2638]ནང་ནས་ཀྱང་གཞུང་འདི་ཡིན་ཏེ་ཟླ་བ་གཅིག་གི་མཐར་ཐུག་པའི་ཆོས་གོས་ནི་འདི་ཡིན་ཏེ་གང་ལ་ཆོས་གོས་གསུམ་ཚང་བར་ཡོད་པ་དེས་དེ་གཞག་པར་མི་བྱའོ། །

[Block 3825]
ཅི་སྟེ་འཇོག་ན་སྤང་བའི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །གང་ལ་འཇོག་པའི་སྤང་བ་འབྱུང་ཞེ་ན། དེའི་ཕྱིར་གཞན་དུ་ན་དེ་ནི་ཞག་སུམ་ཅུ་འདས་ནའོ་ཞེས་བྱ་བ་ནི་ཁ་སྐོང་བ་པོ་ལ་རེ་བ་ལ༌[^2639]ཡོད་པ་དང་བྱིན་གྱིས་བརླབ་པར༌[^2640]བྱ་བ་མེད་པ་ཉིད་ནའོ། །

[Block 3826]
དེ་ནི་ཞེས་བྱ་བ་ནི་ཆུང་བ་ཁྲུ་གང་ཡན་ཆད་པའོ། །

[Block 3827]
ཞག་སུམ་ཅུ་འདས་ནའོ་ཞེས་བྱ་བ་ནི་ཞག་སུམ་ཅུ་རྩ་གཅིག་གི་སྐྱ་རེངས༌[^2641]དང་པོ༌[^2642]ཤར་ནའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3828]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་ཆོས༌[^2643]གོས་སྔོན་པོ་རྙེད་ལ་བྱེད་དུ་མི་འཇུག་ཅེས་བྱ་བ་ལ་སོགས་པ་དང་། ཞུ་བ་ལས་ཀྱང་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2644]དགེ་སློང་དེས་ཟླ་བ་གཅིག་གི་མཐར་ཐུག་པར་ཆོས་གོས་གཞག་པར་བྱའོ། །

[Block 3829]
ཆོས་གོས་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། འཁོར་གསུམ་མི་ཁེབས་པ་གང་ཡིན་པའོ་ཞེས་གསུངས་པ་གང་ཡིན་པའོ། །

[Block 3830]
ཁ་དོག་ལ་སོགས་པ་ལས་རིགས་མི་མཐུན་པ་ནི་ཆོག་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདི་ལ་འགྲུབ་པ་ཉིད་དུ་རྩོམ་པ༌[^2645]ཉིད་འདིར་གང་ཞིག་རེ་བ་གང་ཡིན་པས་ནི་རེ་བ་དང་བཅས་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3831]
འདིར་གཞུང་ནི་འདི་ལྟར་གང་གི་ཚེ་དེ་དང་འདྲ་བ་རྙེད་པར་གྱུར་ནའོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 3832]
སོགས་པ་ཞེས་བྱ་བའི་སྒྲས་ནི་རིགས་མི་མཐུན་པ་ཐ་དད་པ་བལ་གོས་དང་རས་གོས་ལ་སོགས་པ་ལྟ་བུ་ཐམས་ཅད་བསྡུའོ། །

[Block 3833]
ཁ་དོག་ཅེས་བྱ་བའི་སྒྲས་ནི་འདིར་སྔོན་པོ་དང་སེར་པོ་དང་དམར་པོ་དང་དེ་དག་གི་བྱེ་བྲག་ལས་བྱས་པ་དག་ཀྱང་བསྡུའོ། །

[Block 3834]
དཀར་པོ་ཉིད་ནི་ཁ་དོག་ཐམས་ཅད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ་ཁ་དོག་ཐམས་ཅད་པ་ནི་ཁ་དོག་ཐམས་ཅད་པའོ། །

[Block 3835]
དེའི་དངོས་པོ་ནི་དཀར་པོ་ཉིད་དོ། །

[Block 3836]
སྔོན་པོ་ལ་སོགས་པ་ལ་དཀར་པོའི་རྫོགས་པ་ཉིད་མ་ཡིན་ཏེ། སྔོན་པོ་ལ་སོགས་པ་བཞག་པ་ལ་དཀར་པོ་རྙེད་པ་གང་ཡིན་པ་དེ་ནི་གཞན་རྙེད་པ་ཉིད་མ་ཡིན་ཞེས་བྱ་བ་འདི་ལ་འདི་བྱེད་པའོ། །

[Block 3837]
འདིར་ལུང་ནི་སྔོན་པོ་ལ་སོགས་པའི་ནང་དུ་དཀར་པོ་མ་སྨོས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3838]
དེ་རྙེད་ན་ཞག་བཅུ་པ་དེའི་དང་པོ་ལ་བག་ལ་གློན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཉེ་བར་གཞག་པ་དེ་ཞེས་བྱ་བ་ནི་དེའི་རིགས་ཀྱི་ཁ་དོག་ལ་སོགས་པ་དེ་དང་རིགས་མཐུན་པ་བསྒྲུབ་པ༌[^2646]ལ་གང་ཞིག་དེའི་ཚེ་ན་གཞག་པའི་དུས་ན་ཞག་བཅུ་པ་དང་པོ་འམ་གཉིས་པ་ལ་སོགས་པ་དེའི་དང་པོ་ལ་བག་ལ་གློན་པ་ཉིད་དོ། །

[Block 3839]
ཚད་རྫོགས་པ་ཉིད་གལ་ཏེ་དེའི་ཚད་ཀྱིས་ཆོག༌[^2647]ལ་ཞག་བཅུ་ལས་འབྱུང་བ་ཉིད་དེ་དག་གཅིག་པ་ཉིད་ཀྱི་རྣམ་པར་ལྟོས་པར་བྱ་བ་ཉིད་དོ། །

[Block 3840]
དེའི་ཞག་བཅུ་ལ་སོགས་པ་ཉིད་ནི་འཆང་བ་ལ་སོགས་པའོ། །

[Block 3841]
དེ་ཡང་གལ་ཏེ་དེའི་ཚེ་བག་ལ་གློན་པ་ཉིད་དེ་ཚད་དུ་ཆོག་པ་ཉིད་ཡིན་ན་དེའི་ཚེ་ལྟུང་བ་མེད་པ་ཉིད་དོ། །

[Block 3842]
སྔ་མ་ལ་ཟླ་བ་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་དེ་ཉིད་དུ་ཕྱི་མ་ལ་ཞུགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་འདི་ལ་འདི་བྱེད་པའོ། །

[Block 3843]
བཞག་པ་དང་བག་ལ་གློན་པའི་དབང་གིས་འདིར་རྣམ་པར་བཞག་པ༌[^2648]འདི་རིག་པར་བྱའོ། །

[Block 3844]
འདིར་གཞུང་ནི་དགེ་སློང་དེས་ཞག་བཅུ་པ་དེ་ཉིད་ཀྱི་ནང་རོལ་དུ་ཞེས་འདི་ཙམ་ལྟ་བུར་གྱུར་པ་ལ་བྱིན་གྱིས་བརླབས་པ་ཉིད་བསྐྱེད་པ་སྤང་བའི་ལྟུང་བྱེད་བྱས་པ་ཉིད་གཞན་ལ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 3845]
དེ་བསྒྲུབ་པའི་ཚུལ་བརྗོད་པར་བྱ་སྟེ་སར་པ་ལས་སྣམ་སྦྱར་གྱི་མཐའ་ནི་ཉིས་རིམ་མོ་ཞེས་བྱ་བ་སར་པ་ལས་ཞེས་བྱ་བ་ནི་དུས་གསུམ་དུ་གང་ཡང་རུང་བ་གཅིག་དུས་ལས་ལོངས་མ་སྤྱད་པ་ལའོ། །

[Block 3846]
གདིང་བའི་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སར་པ་ལས་བྱེད་ན་དེའི་རིམ་པའི་ཚད་ཀྱི་མཐའ་ཉིས་རིམ་མོ། །

[Block 3847]
བླ་གོས་དང་མཐང་གོས་གཉིས་ནི་ཆིག་རྐྱང་ངོ་ཞེས་བྱ་བ་ནི་བླ་གོས་དང་མཐང་གོས་གལ་ཏེ་སར་པ་ལས་བྱེད་ན་དེ་གཉིས་ཀྱི་རིམ་པའི་ཚད་ཀྱི་མཐའ་ནི་ཆིག་རྐྱང་ངོ་། །འདིར་གཞུང་ནི་གལ་ཏེ་དགེ་སློང་དེས་བཅག་པ་དང་ཁ་བསྒྱུར་བ་དང་རྩོམ་པར་ནུས་ན་དགེ་སློང་དེས་གོས་དེ་ལས་སྣམ་སྦྱར་དང་གདིང་བ་ནི་ཉིས་རིམ་དུ་བྱའོ། །

[Block 3848]
བླ་གོས་དང་མཐང་གོས་ནི་ཆིག་རྐྱང་དུ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3849]
དུས་ཚིགས་སུ་སྤྱད་པ་ལས་ནི་ཉིས་འགྱུར་དུའོ་ཞེས་བྱ་བ་ནི་མདོ་སྔ་མ་དག་ལས་ཉིས་རིམ་དང་ཆིག་རྐྱང་ཞེས་སྨོས་པ་དེ་དག་ལ༌[^2649]ལྟོས་ཏེ། གལ་ཏེ་གོས་ཚིགས་གཅིག་ཏུ་སྤྱད་པ་ལས་དེ་དག་བྱེད་ན་ཉིས་འགྱུར་དུ་བྱའོ། །

[Block 3850]
སྣམ་སྦྱར་དང་གདིང་བ་གཉིས་ནི༌[^2650]བཞི་རིམ་དུ་བྱའོ། །

[Block 3851]
བླ་གོས་དང་མཐང་གོས་གཉིས་ནི་ཉིས་རིམ་དུ་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3852]
དུས་ཚིགས་སུ་སྤྱད་པའི་གོས་ནི་བགོ་ཟས་ཆུང་བ་ཉིད་དེ་ཞེས་བྱ་བ་འདི་གྲུབ་པའོ། །

[Block 3853]
གང་ཞིག་དུས་ཚིགས་གསུམ་པོ་དག་ལས་དུས་ཚིགས་གང་ཡང་རུང་བའི་དུས་ཚིགས་སུ་སྤྱད་པ་གང་ཡིན་པའོ་ཞེས་དུས་ཟད་པའི་ངོ་བོ་བརྗོད་པའོ། །

[Block 3854]
འདིར་ཟླ་བ་བཞི་པོ་ནི་དུས་སུ་རིག་པར་བྱའོ། །

[Block 3855]
ཕྱག་དར་ཁྲོད་ལས་བྱས་པ་དག་ལ་ནི་ངེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་རིམ་པ་རྣམས་ཤིན་ཏུ་མང་བ་ཉིད་ལ་ཡང་ངེས་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
