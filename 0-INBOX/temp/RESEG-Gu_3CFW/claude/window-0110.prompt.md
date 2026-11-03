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

[Block 3856]
དེར་རང་གི་གནས་སུ་བསྐུར་བར་མི་འགྲུབ༌[^3979]ན་གནས་གཞན་དུ་ལོངས་སྤྱད་པས་ཡོངས་སུ་སྤྱད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་གཞན་དུ་ལོངས་སྤྱད་པར་བྱའོ་ཞེས་བྱ་བའི༌[^3980]དོན་ཏོ། །

[Block 3857]
གནས་གཞན་གྱི་ཟས་དང་ཡོ་བྱད་ཀྱི་རྙེད་པ༌[^3981]ནས༌[^3982]གཞན་དུ་ཡོངས་སུ་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་གཞན་གྱི་ཟས་ཀྱི་རྙེད་པ་བཟའ་བ་དང་བཅས་པ་ལ་སོགས་པ་དང་། ཡོ་བྱད་ཀྱི་རྙེད་པ་མར་མེ་དང་འབྲུ་མར་དང་རྐང་པ་བསྐུ་བ་དང་། མཆིལ༌[^3983]ལྷམ་དང་གོས་དང་གདུགས་དང་ཤིང་དང་རྩ་བ་དང་སྡོང་བུ་དང་འདབ་མ་དང་མེ་ཏོག་དང་། འབྲས་བུ་དང་སྨན་ལ་སོགས་པ་དག་གནས་དེར༌[^3984]གནས་པར་མི་བརྟེན་པས༌[^3985]གནས་གཞན་དུ་དྲང༌[^3986]ཞིང་ཡོངས་སུ་སྤྱད་པར་མི་བྱའོ། །

[Block 3858]
དེ་དེ་ལ་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་གཞན་གྱི་ཟས་དང་ཡོ་བྱད་ཀྱི་རྙེད་པ་དེ་གནས་གཞན་དུ་ཟ་བར་བྱེད་པ་དེ་ལ་སྦྱིན་པར་མི་བྱའོ། །

[Block 3859]
ནོད་པ་འབུལ་དུ་གཞུག་པར་བྱའོ༌[^3987]ཞེས་བྱ་བ་ནི་གནས་གཞན་དུ་ཟ་བར་བྱེད་པ་མནོས་པ་སྨོས་པ་གང་ཡིན་པ་དེ་འབུལ་དུ་གཞུག་པར་བྱའོ། །

[Block 3860]
མི་ཁུགས་ན་དབྲོག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ནོད་པ་སྟེ་མ་རྙེད་དམ། མཐུ་དང་ལྡན་པ་ལ་བརྟེན་པའི་ཕྱིར་ནོད་པ་དེ་ལ་དབྲོག་པར༌[^3988]མི་ནུས་ན། གང་གིས་དེ་ལ་སྦྱིན་པ་དེ་ལ་འབུལ་དུ་གཞུག་པར་བྱའོ། །

[Block 3861]
འདིར་སིལ༌[^3989]བུ་དག་ལས།

[Block 3862]
དགེ་སློང་གཞན་དུ་གནས་པས་གཞན་དུ་ཁྱེར་ཏེ་ཅུང་ཟད་ཅི་ཙམ་ཟོས་པ་ཐམས་ཅད་རིན་ཐང་ཚང་བར་བྱ་སྟེ་འབུལ་དུ་གཞུག་པར་བྱའོ་ཞེས་གསུངས་པ་དེ་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 3863]
ཆ་དབང་བ་དག༌[^3990]གིས་དགེ་འདུན་གྱི་རྩྭ་དང་ཤིང་མི་མཁོ་བ་དང་། རང་གི་དང་འདྲ་བར་སྤྱད་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་དོ་ཞེས་བྱ་བ་གང་དག་དེས་འཐོབ་ཅིང་དེའི་ཆ་དབང་བ་དག་གིས་དགེ་འདུན་གྱི་རྩྭ༌[^3991]དང་ཤིང་དགེ་འདུན་གྱི་ས་ཁོ་ནར་སྐྱེ་ཞིང་ཡོངས་སུ་མ་བཟུང་བ་དག་ཡིན་ལ་ཡོངས་སུ་བཟུང་བ་དང་འདིར་མི་མཁོ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 3864]
མ་བསྐོས་པ་འཁོར་ཞིང་སྤྱད་པ་ལ་ཇི་ལྟར་འོངས་པས་ཡིན་གྱི་རྒན་རིམས་ཀྱིས༌[^3992]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མ་བསྐོས་པ་རེས་ཀྱིས་འཁོར་ཞིང་སྤྱད་པ་ཟས་ལ་སོགས་པ་ལ་མར་མེ་བཞིན་དུ་ཅིག་ཅར་སྤྱད་པ་མ་ཡིན་པ་ལ་ནི་ཇི་ལྟར་འོས་པས༌[^3993]སྤྱད་པར་བྱའི་རྒན་རིམས་ཀྱིས༌[^3994]སྤྱད་པར་བྱ་བ་ནི་མ་ཡིན་གྱི། གང་ཞིག་མ་བསྐོས་ན་དང་པོ་སུ་འོངས་པ་དེ་ལ་གཡར་པོར་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3865]
ཅིག་ཅར་བརྙས་ན་ནི་དེའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཅིག་ཅར༌[^3995]བརྙས་པར་གྱུར་ན་ནི་ཅིག་ཅར་བརྙས་པ་དེ༌[^3996]རྒན་རིམས་ཀྱིས༌[^3997]སྤྱད་པར་བྱ་བའོ། །

[Block 3866]
མ་ཟིན་ན་དེ་ལས་དབྲལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ལས་ཞེས་བྱ་བ་ནི་མ་བསྐོས་པ་དེ་ལ་སྦྱར་ཞིང་སྤྱད་པ་ལས་སོ། །

[Block 3867]
དེ་བཀྲུ་བར་ཆུས་རྐང་པ་འབགས་པ་ཉིད་ན་དེ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་མ་ཟིན་པ་ཉིད་དོ། །

[Block 3868]
དེ་བཀྲུ་བར་ཞེས་བྱ་བ་ནི་རྐང་པ་དེ་བཀྲུ་བ་ལའོ། །

[Block 3869]
ཆབ་ཁུང་ས་དེར་ཞུགས་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་ཆབ་ཁུང་ལའོ། །

[Block 3870]
ཞུགས་པ་ཉིད་ན༌[^3998]ཞེས་བྱ་བ་ནི་མ་ཟིན་ནའོ། །

[Block 3871]
སྒོམ་པའི་ཕྱིར་འདུག་པ་བསློང་བར༌[^3999]མི་བྱའོ་ཞེས་བྱ་བ་ལ་འདུག་པ་ཞེས་བྱ་བ་ནི་སྒོམ་པའོ། །

[Block 3872]
དེ་ལ་རྒན་རིམས་སུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདུག་པ་དེ་ལ་རྒན་རིམས་སུ་མི་བྱའོ། །

[Block 3873]
འོན་ཀྱང་འདི་ལྟར་འོངས་པས་བྱ་བ་སྟེ། འདུག་པ་ལ་ཉེ་བར་མཁོ་བའི་སྟན་ལ་སོགས་པ་རྣམས་ལ༌[^4000]ཇི་ལྟར་འོངས་པ་ཉིད་ཀྱིས་ལོངས་སྤྱད་པ་སྟེ། ཇི་ལྟར་རྒན་རིམས་སུ་ལོངས་སྤྱད་པར་བྱ་བ་མ་ཡིན་ཏེ་དེ་བས་ན་དེའི་འདི་བྱ་བའོ། །

[Block 3874]
འདིར་གཞུང་ནི་དགེ་སློང་དག་སྤོང་བའི་ཁང་པ་ན་འཁོད་ཅིང་དགེ་བའི་ཕྱོགས་དག་བྱེད་པ་ན། དྲུག་སྡེ་དག་འོངས་ཏེ་ངེད་ཅག་རྒན་ནོ་ཞེས་བྱ་བས༌[^4001]སློང་བར་བྱེད་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། འདི་ལ་རྒན་རིམས་སུ་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3875]
དགེ་སློང་ལས་དང་ཟས་ཀྱིས༌[^4002]འབགས་པ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལས་དང་ཟས་བརྩམས་པས་འབགས་པ་བསླང་བར་མི་བྱའོ། །

[Block 3876]
བྱུག་རིས་མ་ཡིན་པར་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རང་གི་གོ༌[^4003]མ་ཡིན་པ་ནི་བྱུག་རིས་མ་ཡིན་པ་སྟེ་དེར་འདུག་པར་མི་བྱའོ། །

[Block 3877]
བྱ་བ་བྱས་ནས་འཁོར་ཞིང་སྤྱད་པ་འདོད་པ་ཡོད་ན་བཅང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འཁོར་ཞིང་སྤྱད་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་འོས་པའི༌[^4004]སྤྱོད་པ་ལ་སྤྱད་པར་བྱ་བའོ། །

[Block 3878]
བར་དུ་དོན་གྱི་ཆེད་ཉིད་དུ་ཁྲིའུ་ལས་ལངས་པ་ནི་བྱ་བ་བྱས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བར་མ་བྱ་བ་ཉིད་ཀྱི༌[^4005]དབང་གིས༌[^4006]ཐ་མ་བྱས་པ་ཉིད་ལ་ད་དུང༌[^4007]ལས་སྔ་མ་བརྩམས་པ་གང་ཡིན་པ་དང་། ཁྲིའུ་ལས་བབས་པ་གང་ཡིན་པ་དེ་ལ་འདི་བྱ་བ་བྱས་པ་ཉིད་དུ་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 3879]
དེའི་དུས་ན་དེ་ལ་ཆོས་གོས་སམ་པུས་འཁྱུད་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ལ་ཞེས་བྱ་བ་ནི་ཁྲིའུའོ། །

[Block 3880]
དེའི་དུས་ན་ཞེས་བྱ་བ་ནི་བར་མ་བྱས་པ་ཉིད་ཀྱི༌[^4008]དབང་གིས་དུས་ལ༌[^4009]བཏང་བའི་དུས་ལའོ། །

[Block 3881]
འདོད་པ་ཡོད་ལ་གནས་ཡོད་ན་དགེ་འདུན་གྱི་སྦགས་པ་ཉིད་བརྟེན་པར༌[^4010]མི་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དོན་དུ་གཉེར་བ་གཞན་དག་ཡོད་ན་འགྲོ་བ་ཡང་ཡོད་ན་དེས་དགེ་འདུན་གྱི་ཡོ་བྱད་སྦགས་པ་ཉིད་བསྟེན་པར་མི་བྱའོ། །

[Block 3882]
དོན་ཡོད་ན་རྣམས་པ་དེ་ལྟ་བུ་ལས་བྲལ་བར་བྱས་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་དོན་ཡོད་པ་ཉིད་དང་འདོད་པའི་གང་ཟག་གཞན་ཡོད་པ་ལ་གང་ལ་སྦགས་པ་ཡོད་པ་ཉིད༌[^4011]བསྟེན་པའོ། །

[Block 3883]
དེ་ལྟ་བུར་གྱུར་པ་ལས་ཡོ་བྱད་དེ་ལས་བྲལ་བར་བྱ་སྟེ་ཁྱེར་བ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །ཅི་དགོས་པ་མེད་ཀྱང་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར། དོན་ཡོད་ན་ཞེས་བྱ་བ་སྨོས་ཏེ། དགོས་པ་ཡོད་པ་ལ་ཡིན་གྱི་མེད་ན་ནི་མ་ཡིན་ནོ། །

[Block 3884]
དགེ་འདུན་གྱི༌[^4012]མཆིག་དང་མཆིག་གུ་བཅང་བར་བྱའོ། །

[Block 3885]
འདྲེག་མཁན་གྱི་ལག་ཆ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་བཅང་བར་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས་པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་ཏེ། དགེ་སློང་གི་དགེ་འདུན་གྱི་ཕྱིར་བཅང་བའོ། །

[Block 3886]
སྣོད་དུ་བཅུག་སྟེ་རྩིག་པ་ལ་གཞག་གོ་ཞེས་བྱ་བ་ནི་འདྲེག་མཁན་གྱི་ལག་ཆའོ། །

[Block 3887]
འདིར་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས།

[Block 3888]
དགེ་སློང་གིས༌[^4013]དགེ་འདུན་གྱི་ཕྱིར་འདྲེག་མཁན་གྱི་ལག་ཆ་བཅང་བར་བྱ་ཞིང་སྣོད་དུ་བཅུག་སྟེ་རྩིག་པ་ལ་གཞག་པར་བྱའོ་ཞེས༌[^4014]གསུངས་པ་ཡིན་ནོ། །

[Block 3889]
སྟེའུ་དང་སྟ་རེ་དང་གཟོང་ལ་སོགས་པ་དང་དེ་དག་གི་སྣོད་དང་བཅས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་དགེ་འདུན་གྱིས་བཅང་བར་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^4015]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་ཏེ། དེ་དག་གི་སྣོད་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་སྟེའུ་དང་སྟ་རེ་དང་གཟོང་ལ་སོགས་པ་དེ་དག་གི་སྣོད་དོ། །

[Block 3890]
འདིར་གཞུང་ནི་ཤིང་དག་གཤགས༌[^4016]པར་མི་ནུས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་འདུན་གྱི་ཕྱིར་སྟེའུ་དང་སྟ་རེ་དང་གཟོང་བཅང་བར་བྱའོ། །
--- END BLOCKS ---
