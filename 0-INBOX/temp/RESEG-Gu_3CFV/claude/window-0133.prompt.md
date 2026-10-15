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

[Block 4661]
དགེ་སློང་མ་ལ་ཡང་མི་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་གནས་མལ་གྱི་ཆོས་ཅན་ལ་དགེ་འདུན་གྱི་གནས་མལ་གཡོགས་པ་དག་མི་གཙང་བ་ལ་སུས་ཀྱང་མི་སྦྱིན་པའོ། །

[Block 4662]
དགེ་སློང་མ་རྣམས་ལ་འབྲེལ་པའི་ཁྲི་སྦྱིན་པར་མི་བྱའོ་ཞེས་འདིར་སྨོས་ཏེ། གནས་མལ་ཡང་ཞེས་བྱ་བ་འདིར་ཡང་ཆོ་ག་འདི་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བའོ། །

[Block 4663]
འདིར་གནས་འབྱོར་ན་དེ་ལ་འདབ་ཏུ་གཙུག་ལག་ཁང་སྦྱིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མའོ། །

[Block 4664]
འདིར་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་ལའོ། །

[Block 4665]
གནས་མལ་ལྷག་པ་བཟང་པོ་མ་ཡིན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ལྷག་ཅེས་བྱ་བ་ནི་དགེ་སློང་རྣམས་ལས་ལྷག་པར་གནས་པ་ལའོ། །

[Block 4666]
ཁྱེད་ཅག་ལ་གང་གིས་ཀྱང་དགེ་འདུན་གྱི་གནས་མལ་ལ་གདིང་བ་མེད་པར་ལོངས་སྤྱད༌[^3247]པར་མི་བྱ། གདིང་བ་རུང་བ་མ་ཡིན་པས་ལོངས་སྤྱད་པར་མི་བྱ། གདིང་བ་དྲི་མ་ཅན་གྱིས་ལོངས་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ལྟུང་བ་ཡིན་ཏེ། བསླབ་པའི་གཞི་ཉིད་ལས་འདིར་ཡོད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4667]
ཟླ་བ་ཕྱེད་ཕྱེད༌[^3248]ཅིང་སོ་སོར་བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་མལ་ལའོ། །

[Block 4668]
དམ་ཚིག་ལས་འདས་ཤིང་སྤྱད་ན་གནས་པ་ནི་གནས་ལ༌[^3249]གཞན་གྱི་ནི་དགེ་འདུན་ལ་བརྗོད་དེ་དབྲོག་པར༌[^3250]བྱའོ་ཞེས་བྱ་བ་ནི་བརྟེན་པ་ལས་གཞན་དགེ་འདུན་ལ་ཞུས་ཏེ༌[^3251]སྤྱད་པར་བྱའོ། །

[Block 4669]
དགེ་འདུན་སོང༌[^3252]སྦྱིན་བདག་ཆེ་གེ་མོ་དང་ཞལ་ཏ་བ་ཆེ་གེ་མོ་དང་། སྤྱོད་ཡུལ་གྱི་གནས་ཆེ་གེ་མོ་དང་ནད་གཡོག་ཆེ་གེ་མོས་གནས་པར་ཞལ་གྱིས་བཞེས་པར་འགྱུར་རོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 4670]
འགྱོད་པ་དང་། གཞན་སྡུག་བསྔལ་བ་དང་། ཡིད་མི་བདེ་བ་མི་སྐྱེད༌[^3253]པ་ཉིད་དང་། སེལ་བ་ཉིད་དག་དང་། བདེ་བ་དང་ཡིད་མི་བདེ་བ་བསྐྱེད་པ་ཉིད་རྗེས་སུ་བསྲུང་བ་ཉིད་དག་དང་། ནད་གཡོག་ཉིད་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་དག་ལས་འབྱུང་བ་སོ་སོར་བརྟགས་པས་གནས་དང་སྤྱོད་ཡུལ་དང་། བསོད་སྙོམས་དང་སྨན་པར༌[^3254]བྱེད་པ་ལ་རྣམ་པར་བལྟས་ཏེ་གནས་པར་ཁས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འགྱོད་པས་ཉེ་བར་གནས་པ་ལའོ། །

[Block 4671]
འདིར་སྡུག་བསྔལ་ནི་ཤིན་ཏུ་ཆེ་བ་སྟེ། ཡིད་མི་བདེ་བ་དང་ཡིད་བདེ་བ་ནི་བདེ་བ་ཤིན་ཏུ་ཆེ་བ་སྟེ་ལུས་ཀྱི་ཡང་ངོ་། །དེའི་ལུས་ཅན་གྱི་ཡུལ་བསྡུས་པ་དང་། དེའི་རིགས་ཅན་བཟའ་བར་བྱ་བ་སྦྱིན་པ་ནི་དེ་དག་གིས༌[^3255]བསྐྱེད་པའི་སྡུག་བསྔལ་སེལ་བ་ནི་གསོ་བར་བྱེད་པའོ། །

[Block 4672]
བདེ་བ་རྗེས་སུ་སྲུང་བ་ནི་དེའི་ཚོགས་པ་རྣམས་ལ་ཇི་ལྟར་མི་འབྲལ་བ༌[^3256]དེ་ནི་དེ་ལྟར་ཀུན་ཐུབ༌[^3257]པའོ། །

[Block 4673]
སྦྱིན་པར་བྱེད་པ་ལ་ཞེས་བྱ་བ་ནི་སྤྱོད་ཡུལ་དེ་ལ་འབྱོར་པ་སོ་སོར་བརྟགས་པས་སོ། །གང་དུ་གནས་པར་ཁས་བླང་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གཡོགས་པར་དགེ་སློང་གི་མདུན༌[^3258]དུའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4674]
གཙུག་ལག་ཁང་དུ་མར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། གཙུག་ལག་ཁང་དུ་མར་མཚམས་སུ་རྫས་གཅིག་གིས་མནན་ཏེ། དུ་མས་ཁས་ལེན་པ་གང་ཡིན་པ་དེར་ཡང་འདི་དག་བཀག་པ་ཡིན་ནོ། །

[Block 4675]
འདིར་གཞུང་ནི་དགེ་སློང་གིས༌[^3259]གཙུག་ལག་ཁང་གཉིས་སུ་དབྱར་གནས་པར་ཁས་བླང་བར༌[^3260]མི་བྱའོ། །

[Block 4676]
ཁས་ལེན་པར་བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ༌[^3261]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4677]
གང་ལ་དགེ་སློང་མེད་པ་ཉིད་དང་སྒོ་གླེགས་མེད་པ་ཉིད་དང་བཅས་པར་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ལ། གང་ལ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་ལའོ། །

[Block 4678]
གཙུག་ལག་ཁང་གང་ན་འདི་གཉི་ག་མཉམ་པར་སྦྱོར་བ་དེ་ཡང་གནས་པར་ཁས་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4679]
སྦྱིན་བདག་དང་ཞལ་ཏ་བ་དང་སྤྱོད་ཡུལ་གྱི་གྲོང༌[^3262]དང་ནད་གཡོག་དག༌[^3263]ཡོད་པ་ཉིད་ཡིན་ན་བརྗོད་པར་བྱའོ༌[^3264]ཞེས་བྱ་བ་ནི་གལ་ཏེ་དེ་ན་དེ་དག་ཡོད་པ་ཉིད་ན་ཁས༌[^3265]ལེན་པའི་སྔགས་བརྗོད་པའི་ཚེ་ཡང་དེ་སྐད་བརྗོད་པར་བྱ་སྟེ། ཞུ་བ་ལས་ཀྱང་བརྗོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ།[^3266] །བྱིན་གྱིས་མ་བརླབས་པར༌[^3267]མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སྐྱ་རེངས་འཆར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྐྱ་རེངས་ལས་དུས་སྔར་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་འདའ་བར་བྱེད་པ་ལ་ནི་ཉེས་པ་མེད་དོ།[^3268] །དེ་ལྟ་ཡང་གལ་ཏེ་འགྲོ་ན་དེ་ཡང་གནས་པར་མི་བྱའོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4680]
ཆོས་དང་ལྡན་པའི་དོན་དུ་ཞག་བདུན་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཆོས་ལས་མི་འདའ་བའི་དོན་ལའོ། །

[Block 4681]
དེ་འདིར་རྒྱས་པར་བཤད་པའི་ཕྱིར། འདི་ལྟ་སྟེ། དགེ་སློང་གི་ཀུན་དགའ་ར་བ་འབུལ་བ་དང་། གཙུག་ལག་ཁང་ཞལ་བསྲོ་བ་དང་། གནས་མལ་འབུལ་བ་དང་། བསླབ་པ་བརྟན་པོ་བཅའ་བ་དང་། མཆོད་རྟེན་ཞལ་བསྲོ་བ་དང་། མཆོད་སྡོང་གཟུགས་པ་དང་། རྒྱལ་མཚན་བསྒྲེང་བ་དང་། མཆོད་པ་བྱ་བ་དང་། ཚོན་དང་། ཙན་དན་གུར༌[^3269]ཀུམ་བྱུག་པ་སྐུད་པ༌[^3270]དང་། བཀླག་པ་དང་། འགྱོད་པ་བསལ་བ༌[^3271]དང་། ལྟ་བའི་རྣམ་པ་སྤང་བ་དང་། ཕྱོགས་དང་མཐུན་པ་བསྒྲུབ་པ་དང་། བཟོད་པ་གསོལ་བ་དང་། ཡོངས་སུ་གནས་པ་ལ་སོགས་པ༌[^3272]བཞི་བྱ་བ་དང་། དབྱུང་བ་དང་ནད་པ་དབུགས་དབྱུང་བ༌[^3273]དག་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཆོད་སྡོང་གཟུགས་པ་དང་རྒྱལ་མཚན་བསྒྲེང་བ་ཞེས་བྱ་བ་ལ། མཆོད་སྡོང་གི་སྒྲས་ནི་གཟུགས་པ་དང་འབྲེལ་བའོ། །

[Block 4682]
བཀླག་པ༌[^3274]ཞེས་བྱ་བ་ནི་མདོ་སྡེའི་མཚན་བཀླག་པ༌[^3275]དང་། སྟོན་པ་ན་རྙེད་པ་འགྲུབ་པ་ཡོད་པས་ལོངས་སྤྱད༌[^3276]པའི་དོན་དུ་ཞེས་བྱ་བ་འདིར་སྨོས་ཏེ། ཀློག་པ༌[^3277]དེ་ཙམ་གྱི་ཕྱིར་ཡང་རིགས་པ་ཡིན་ཏེ། བཟོད་པ་གསོལ་བ་ཞེས་བྱ་བ་ཡང་བསྡུ་བའི་ཕྱིར་བཀླག་པ༌[^3278]ཞེས་བྱ་བའི་སྒྲས༌[^3279]སྨོས་སོ། །

[Block 4683]
ཕྱོགས་དང་མཐུན་པ་ཞེས་བྱ་བ་ནི་སྨོན་ལམ་གྱི་ལམ༌[^3280]བྱ་བ་དང་། གཞི་འགའ་ཞིག་སོ་སོར་གནས་པ་ལའོ། །

[Block 4684]
ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་བཞི་བྱ་བ་ནི་སྤོ་བ་དང་། གཞི་ནས་ཡོངས་སུ་སྤོ་བ༌[^3281]དང་། མགུ་བར་བྱ་བ་དང་། གཞི་ནས་མགུ་བར་བྱ་བའོ། །

[Block 4685]
གཞི་ནས་མགུ་བར་བྱ་བ་ལས༌[^3282]ཐ་མི་དད་དོ། །

[Block 4686]
དགེ་སློང་གིས་ཞེས་བྱ་བ་ནི་ཆོས་ལས་མི་འདའ་བའི་དོན་ལ་ཞེས་བྱ་བ་དེ་དང་འབྲེལ་བའོ། །

[Block 4687]
དགེ་སློང་མའི་ལྕི་བའི་ཆོས་ཀྱི་མགུ་བར་བྱ་བ་དབུལ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། སྔ་མ་རྣམས་བསྡུ་བའི་དོན་དུ་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་སྨོས་སོ། །

[Block 4688]
དགེ་སློང༌[^3283]མའི་ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་དང་བསྙེན་པར་རྫོགས་པར་བྱ་བ་ལ་ཡང་ངོ་། །དགེ་ཚུལ་གྱི་དེ་ལའོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པར་བྱ་བ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4689]
དགེ་ཚུལ་མའི་བསླབ་པའི་སྡོམ་པ་སྦྱིན་པ་ལའོ། །

[Block 4690]
ཁྱིམ་བདག་དང་ཁྱིམ་པ་མོའི་མགོ་དཀྲི་བ་དང་། བང་བསང་བ་དང་། སྐྲ་བསྐྱེད་པ་དང་། སྐྲ་བྲེག་པ༌[^3284]དང་། གདུབ་ཀོར་བསྐྱེད་པ་དག་ལའོ་ཞེས་བྱ་བ་ནི་ཆོས་ལས་མི་འདའ་བའི་དོན་ལ༌[^3285]ཞག་བདུན་མན་ཆད་བྱིན་གྱིས་བརླབ་པོ་ཞེས་བྱ་བའི་དགོངས་པ་འདིར་ཐམས་ཅད་དུ་རིག་པར་བྱའོ། །

[Block 4691]
བསྙེན་པར་མ༌[^3286]རྫོགས་པ་རྣམས་ཀྱི་དགེ་འདུན་ལྷག་མའི་སྐབས་མ་གཏོགས་པ་སྔ་མ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་དབྱུང་བ་མ་གཏོགས་པ་གང་ཞིག་སྔོན་དུ་ཀུན་དགའ་ར་བ་འབུལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་དེ་ཐམས་ཅད་བསྙེན་པར་མ་རྫོགས་པ་རྣམས་ལ་ཡང་རྟོགས་པར་བྱའོ། །

[Block 4692]
ཁྱིམ་པ་དང་ཁྱིམ་པ་མོའི་བཟོད་པ་གསོལ་བ་ནི་ཁ་བསྲང་བའོ་ཞེས་བྱ་བ་ནི་བཟོད་པར་གསོལ་བའི་གནས་ལ་ཁྱིམ་པ་ཕོ་མོའི་ལྷུང་བཟེད་ཁ་ཕུབ་པ༌[^3287]དག་ལ༌[^3288]ཁ༌[^3289]བསྲང་བར་གསོལ་བ་ཡིན་པར་བལྟའོ། །

[Block 4693]
ཟས་དང་སྨན་དང་གཡོག་དག་མེད་ལ་དེ་དག་མེད་པར་འཚོ་མི་ནུས་ན་དེ་ལས་འདའ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དབྱར་གནས་པར་ཁས་བླངས་བ་དེའོ། །

[Block 4694]
ཟས་ལ་སོགས་པ་རྣམས་མེད་ལ་དེ་དག་མེད་པར་འཚོ་མ༌[^3290]ནུས་པར་གྱུར་ན་དེ་ལས་འདའ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་ལྟར་ཟས་མེད་པར་འཚོ་བར་མི་ནུས་ཤེ༌[^3291]ན། གང་གི་ཕྱིར་འདིར་ཡང་བྱེ་བྲག་ཏུ་འདི་རྟེན༌[^3292]ནི་བྱེ་བྲག་ཏུ་འདི་ལ་བརྟེན་པ་ཡོད་པ་སྟེ། ཐམས་ཅད་དུ་མེད་པ་ཁོ་ན་མ་ཡིན་ཏེ། དེ་ལ་མཆོག་མེད་པ་ལ་རྩ་བ་དང་འབྲས་བུ་ལ་སོགས་པ་གཞན་གྱིས་སུ་ཞིག་ལ་ནུས་པ་ཡོད་སྙམ་དུ་སེམས་པ་དེ་བས་ན་འདི་བྱེ་བྲག་ཏུ་བྱས་སོ། །

[Block 4695]
དགེ་སྦྱོང་གི་ཚུལ་དང་སྲོག་དང་ཚངས་པར་སྤྱོད་པའི་བར་ཆད་ཡོད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ལ།[^3293] དེ་ལས་འདའ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ།[^3294] །བུད་མེད་དང་སྐྱེས་པ་དང་མ་ནིང་གི་མཚན་མ་རྣམས་སམ། དེར་གཉེན་འདུན་རྣམས་ཀྱི་བར་ཆད་ཡོད་ན་ཞེས་བྱ་བ་དེ་བསྡུས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
