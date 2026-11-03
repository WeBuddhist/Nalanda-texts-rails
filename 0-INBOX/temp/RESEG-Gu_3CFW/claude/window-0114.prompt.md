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
[Block 3991]
ཅི་དེ་དང་རྩེ་གཅིག་པ་ཉིད་ཀྱིས་བཅུ་པའི་བདག་ཉིད་ཀྱིས་བསྐྱང་བར་ཇི་ལྟར་བྱ་ཞེ་ན། དེའི་ཕྱིར། ལག་པ་དག་དང་རྐང་པ་དག་བཀྲུ་བ་དང་སོ་ཤིང་དོར་བ་དང་ལྷུང་བཟེད་བཀྲུ་བ་དང་ཁྲུས་བྱས་པ༌[^4102]ནི་བཅུ་པ་ཡིན་ནོ། །

[Block 3992]
གྲང་བ་སྐྱོབ་པའི་ཕྱིར་ཁང་བུའི་སྦུབས༌[^4103]བྱའོ། །

[Block 3993]
དབུགས་དབྱུང་བའི་ཕྱིར་དེ་ལ་སྐར་ཁུང་གདོད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལ་ཞེས་བྱ་བ་ནི་ཁང་བུའི་སྦུབས་དེ་ལའོ། །

[Block 3994]
གཡོགས་མས་དགབ་བོ་ཞེས་བྱ་བ་ནི་གྲང་བ་བསྐྱབ་པའི༌[^4104]ཕྱིར་ཁོ་ནར་ཁང་བུའི་སྦུབས་དེ་གཡོགས་པར་བྱ་བའོ། །

[Block 3995]
སོ་ག་མི་ཚ་བར་བྱ་བའི་ཕྱིར་བསལ༌[^4105]ལོ་ཞེས་བྱ་བ་ནི་སོ་ག༌[^4106]ཤིང་ལྗོན་པ་དེ་མི་ཚ་བར་བྱ་བའི་ཕྱིར་གཡོགས་མ་དེ་བསལ་བར་བྱ་བའོ། །

[Block 3996]
དབྱར་དག་ནི་མི་འདྲུལ་བར༌[^4107]བྱ་བའི་ཕྱིར་སྔ་མ་ཡང་དེ༌[^4108]ཞེས་བྱ་བ་ལ་སྔ་མ་ཞེས་བྱ་བ་ནི་ཁང་བུའི་སྦུབས་དེ་ཡང་བསལ་བར་བྱའོ།[^4109] །ཆུའི་ཡུར་བ་གདོད་དོ་ཞེས་བྱ་བ་ནི་ཁང་བུའི་སྦུབས༌[^4110]དེ་ལའོ།[^4111] །རྩ་བའི་འོངས་ཡལ་བར་མི་དོར་རོ་ཞེས་བྱ་བ་ལ། རྩ་བའི་འོངས་ཞེས་བྱ་བ་ནི་ཤིང་ལྗོན་པའི་འོངས་སོ། །

[Block 3997]
འདིར་གཞུང་ནི་རྩ་བའི་ཐོག་ཡལ་བར་མི་བྱ་ཞིང་བྱི་དོར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ།[^4112] །འདིར་གཞུང་ནི་གླེང་གཞི་དག་ལས་འདི་དང་པོར་བྱས་ཏེ། དེ་རྣམས་འགྲོ་བ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3998]
འཁོར་རྣམ་པར་དབྱེ་བའི་བྱེ་བྲག་གི་བྱི་དོར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ན། ཅི་དེ་ལ་འཇུག་པས་སམ་ཞེ་ན་དེའི་ཕྱིར། ཁ་ཅིག་ཏུ་སོ་ཤིང་བཟའ་བ་དང་། ཁ་ཅིག་ཏུ་ཁ་བཀྲུ་བ་དང་། ཁ་ཅིག་ཏུ་རྐང་པ་དག་བཀྲུ་བ་དེ་ལྟ་བུས༌[^4113]དེ་ལ་འཇུག་པ་ཉིད་མ་ཡིན་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཀྲུ་བར་བྱ་བ་ནི་བྱི་དོར་གྱི་ལས་ལྷག་མ་རྣམས་ལ་ཡང་ཅི་རིགས་པར་རིག་པར་བྱའོ་ཡང་འདིར་ཅི་ཞིག་བྱི་དོར་བྱ་ཞེ་ན། ཁང་བུའི་སྦུབས་བྱ་བ་ལ་སོགས་པར་རང་གིས་བསྐྱེད་པ་ལ་བྱ་བར་བསྟན་པ་གང་ཡིན་པ་དེ་ལ་བྱའོ་ཞེས་བྱ་བ་དེ་དག་ལ་སྨོས་སོ། །

[Block 3999]
མེ་ཏོག་དང་འབྲས་བུ་བསྲུང་བའི་ཕྱིར་དགེ་སློང་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མེ་ཏོག་དང་འབྲས་བུ་ལ་སོགས་པ་བསྲུང་བའི་ཕྱིར་རོ། །

[Block 4000]
ཟས་ཀྱི༌[^4114]ཆེད་དུ་གཞན་དག་གོ། །

[Block 4001]
དེ་དག་གིས་ཆེས་དང་པོར་ཟན་ཟོས་ཏེ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཟན་གྱི་དུས་ཀྱི༌[^4115]ཆེད་དུ་བསྐོས་པ༌[^4116]དག་གིས་སོ། །

[Block 4002]
གནས་ཀྱི་ཚུལ་བཤད་ཟིན་ཏོ།། །།

[Block 4003]
ད་ནི་བྱ་བའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། ཀློག་ཏུ་འཛུད་པ༌[^4117]བསྙེན་བཀུར་ཆེས་མང་བ་བྱེད་པ་དང་། མི་ནུས་པ་ལ་ལོགས་ཤིག་ཏུ་བྱ་བས་ཀྱང་རྗེས་སུ་བརྩེ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཀློག་ཏུ་འཛུད་པ༌[^4118]ཞེས་བྱ་བ་ཀློག་པའི་སློབ་དཔོན་གྱི༌[^4119]བསྙེན་བཀུར་ཆེས་མང་དུ་བྱེད་པ་ཞེས་བྱ་བ་རང་གི་དྲུང་ན་འདུག་པའི་སློབ་མ་དང་ཉེ་གནས་ལ་སློབ་དཔོན་དག་གིས་སོ། །

[Block 4004]
དེའི་འདུལ་བ༌[^4120]བཟུང་སྟེ་དེའི་ལུང་དབོག་པ་དང་ཁ་དོན༌[^4121]བྱ་བ་དང་དམིགས་ཀྱིས༌[^4122]དྲི་བ་སྦྱིན་པ་དག་གིས་དགེ་སློང་མ་ལ་རྗེས་སུ་བརྩེ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་འདུལ་བ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མའི་འདུལ་བ་དེའོ། །

[Block 4005]
དེའི་ལུང་དབོག་པ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མའི་འདུལ་བ་དེ་ལའོ། །

[Block 4006]
ཡི་གེ་བྲི་བར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^4123]འདི་ལ་ཚུལ་དང་མི་མཐུན་པ་མེད་པར་ཤེས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4007]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 4008]
བཅོམ་ལྡན་འདས་ཀྱིས་རང་ཉིད་ཀྱི་ཡབ་ལ་སྤྲིང་ཡིག་བསྐུར་བ་དང་། སྐྱེ་དགུའི༌[^4124]བདག་མོ༌[^4125]ཆེན་མོས་ཨུཏྤ་ལའི་མདོག་གི་ཕྱིར་དང་རང་ཉིད་ཀྱི༌[^4126]ཡི་གེ་སྤྲིང་ངོ་ཞེས་གསུངས་པ་དེའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 4009]
དྲན་པ་དང་འཛིན་པར་མི་ནུས་པས་འདུལ་བའོ། །

[Block 4010]
དེ་མི་བྲི་བར༌[^4127]བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདུལ་བ་དེ་དྲན་པར་བྱ་བའི་དོན་ལས་གཞན་དུ་ཡི་གེ་མི་བྲི་བ༌[^4128]ཉིད་ཡིན་པའོ། །

[Block 4011]
གླེང་གཞི་རྣམས་ལས་འདི༌[^4129]དང་པོར་བྱ་སྟེ་མཚན་མ་མེད་པ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 4012]
འདིར་གཞུང་ནི་བཙུན་པ་བཅོམ་ལྡན་འདས་ཀྱིས་མ་འོངས་པའི་དུས་ན་བརྗེད་ངས་པ་རྒྱུད་ཉམ༌[^4130]ཆུང་བ་དག་འབྱུང་བར་འགྱུར་ཏེ། དེ་དག་གིས༌[^4131]གླེང་གཞི་ཡང་ཐོན་པར་མི་འགྱུར་རོ་ཞེས་གསུངས་པ་ལ། བཅོམ་ལྡན་འདས་ཀྱིས་ལྔ་པོ་དག་ནི་ཡི་གེར་མི་བྲི་སྟེ། ལྔ་གང་ཞེ་ན། སོ་སོར་ཐར་པ་ཐམས་ཅད་དང་། སོ་སོར་ཐར་པ་དང་ལྡན་པ་ཐམས་ཅད་དང་འདུལ་བ་ཐམས་ཅད་དང་། འདུལ་བ་དང་ལྡན་པ་ཐམས་ཅད་དང་། གང་ཟག་སོ་སོའོ༌[^4132]ཞེས་བཀའ་སྩལ་ན་དེ་དག་གིས་ཇི་ལྟར་བསྒྲུབ་པར་བགྱི། ཉེ་བར་འཁོར་དེ་དག་གིས་གླེགས་བུ་ལ་ཡི་གེར་བྲིས་ཏེ་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4013]
འདིར་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས།

[Block 4014]
བྲི་བ་དོར་ནས་དེ་དག་ལྡན་པ་ཉིད་དོ་ཞེས་གསུངས་སོ། །

[Block 4015]
འདི་ལ་སོ་སོར་ཐར་པ་ནི་དེ་དང་འདྲའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4016]
ཡི་གེར་བྲི་བ་དང་ཡི་གེར་མི་བྲི་བ༌[^4133]ཉིད་འདི་ལ་སོ་སོ༌[^4134]ཐར་པ་ནི་འདུལ་བ་དང་འདྲ་སྟེ། དྲན་པ་དང་འཛིན་པར་མི་ནུས་པས་ནི་སོ་སོར་ཐར་པ་ཡི་གེར་བྲི་བར་བྱའོ། །

[Block 4017]
དེ་དང་ལྡན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདུལ་བ་དེ་དང་ལྡན་པ་དང་སོ་སོར་ཐར་པ་དེ་དང་ལྡན་པ་ཡང་ཡི་གེར་བྲི་བ་དང་། ཡི་གེར་མི་བྲི་བ་ཉིད་འདི་ལ་འདུལ་བ་དང་འདྲ་བར་ཤེས་པར་བྱའོ། །

[Block 4018]
འདིར་གཞི་དག་ནི་འདུལ་བ་ཉིད་ཀྱིས་བསྟན་ཏོ། །

[Block 4019]
མདོ་ཙམ་ནི་སོ་སོར་ཐར་པ་ཉིད་ཀྱིས་བསྟན་ཏོ། །

[Block 4020]
སོ་སོར་ཐར་པ་རྣམ་པར་འབྱེད་པ་དང་། དེར་གཏོགས་པའི་ཕྲན་ཚེགས་དང་། གླེང་གཞི་དང་སིལ་བུ༌[^4135]དང་ཞུ་བ་ལ་སོགས་པའི་སོ་སོར་ཐར་པ་དང་ལྡན་པ་ཉིད་ཀྱིས་བསྟན་ཏོ། །

[Block 4021]
གཞིར་གཏོགས་པའི་ཕྲན་ཚེགས་དང་། གླེང་གཞི་དང་སིལ་བུ་དང་ཞུ་བ་ལ་སོགས་པ་ནི་འདུལ་བ་དང་ལྡན་པ་ཉིད་ཀྱིས་བསྟན་ཏོ། །

[Block 4022]
གང་ཟག་གི་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་མི་བྲི་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས་པའི༌[^4136]ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 4023]
མཚན་མ་བྱ་བ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར་ལྷུང་བཟེད་ལ་སོགས་པ་ལ་མཚན་མ་མེད་པ་གང་ཡིན་པ་དེ་ནི་ཡིན༌[^4137]པར་རིག་པར་བྱའོ། །

[Block 4024]
འདིར་གཞུང་ནི་མཚན་མ་མེད་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4025]
དགེ་འདུན་གྱི་གནས་མལ་ལ་མིང་ཡི་གེར་བྲིའོ་ཞེས་བྱ་བ་སྨོས་ན་ཇི་ལྟར་ཞེ་ན། དེའི་ཕྱིར། འདི་ཆེ་གེ་མོའི་གཙུག་ལག་ཁང་མིང་འདི་ཞེས་བྱ་བ་ནི༌[^4138]སྦྱིན་པར་བྱ་བའི་ཆོས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4026]
དེ་ནི་འདིར་སིལ༌[^4139]བུའི་གཞུང་ལས།

[Block 4027]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། མལ་ཆ་དེ་ལས་འདི་ནི་རྒྱལ་པོ་གཟུགས་ཅན་སྙིང་པོའི་སྦྱིན་པར་བྱ་བའི་ཆོས་སོ་ཞེས་ཡི་གེར་བྲི་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4028]
གོས་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་གནས་མལ་གྱི་ལྟུང་བྱེད་ཞུ་བ་ལས།

[Block 4029]
དགེ་འདུན་གྱི་གོས་དག་ལ་ཡང་འདི་ནི་ཆེ་གེ་མོའི་གཙུག་ལག་ཁང་མིང་འདི་ཞེས་བྱ་བའི་སྦྱིན་པར་བྱ་བའི་ཆོས་ཞེས་ཡི་གེར་བྲི་བར་བྱ་བ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4030]
རྣམ་པ་དེ་ལྟར་གཞན་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ།
--- END BLOCKS ---
