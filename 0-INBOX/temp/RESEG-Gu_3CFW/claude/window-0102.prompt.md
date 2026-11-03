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
[Block 3571]
འདས་པ་ལ༌[^3663]ཕྱག་བྱ་བ་ཡིན་པ་ལ་ཕྱག་མི་བྱ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྔོན་འདས་པའི་དུས་ན་དེ་ཕྱག་བྱ༌[^3664]བ་ཉིད་དུ་འགྱུར་བ་ཡིན་ན། [^3665]ད་ལྟར་ཕྱག་བྱ་བ་ཉིད་མ་ཡིན་དུ་ཟིན་ཀྱང་སྔོན་གྱི་གནས་སྐབས་དེ་ཉིད་མངོན་སུམ་བྱས་ཏེ་ཕྱག་བྱར་རུང་བས་དེའི་ཕྱིར་དེ་ལ་ཕྱག་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 3572]
འདི་ནི་དགེ་སློང་རྒན་པོ་ཁྲོས་པའི་དབང་གིས་སྡོམ་པ་རྒྱུན་ཆད་དེ་སྦྲུལ་དུ་གྱུར་པ་ལ། དགེ་སློང་ཅིག་ཤོས་ཀྱིས་སྔོན་གྱི་རྒྱུད་དེ་མངོན་སུམ་དུ་བྱ་སྟེ༌[^3666]འདུད་པར་བྱའོ་ཞེས་གསུངས་པའི་གླེང་གཞི་ཡིན་ཏེ། ཐམས་ཅད་ལ་བྱེ་བྲག་མེད་པས་བྱར་རུང་བས་འདིར་སྤྱིར་མདོར་བྱས་སོ། །

[Block 3573]
སྦགས་པ་ལ་ཕྱག་མི་བྱའོ། །

[Block 3574]
སྦགས་པས་ཕྱག་མི་བྱའོ། །

[Block 3575]
དེས་བདག་གིར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྦགས་པ་ལ་ཕྱག༌[^3667]མི་བྱ་བ་དང་། སྦགས་པས༌[^3668]གཞན་ལ་ཕྱག་མི་བྱ་བ་དང་། སྦགས་པས་ཕྱག་དེ་བདག་གིར་མི་བྱའོ། །

[Block 3576]
སྦགས་པ་ལས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྦགས་པ་གཞན་ལས་ཕྱག་དེ་བདག་གིར་མི་བྱ་བའོ།[^3669] །འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ནད་པ་བལྟ་བར་བྱའོ་ཞེས་གསུངས་པ་དང་། ནད་པ་བལྟ་བར་བྱ་བའི་དགེ་སློང་རྒན་པོ་དག་དང་གསར་བུ་དག་ཀྱང་དོང་ནས། དེ་ན་གསར་བུ་གང་དག་ཡིན་པ་དེ་དག་ནི་ནད་པ་དེ་ལ་ཕྱག་འཚལ་བར་བྱེད། རྒན་པོ་གང་དག་ཡིན་པ་དེ་དག༌[^3670]ལ་ནི་ནད་པ་དེས༌[^3671]ཕྱག་དག༌[^3672]འཚལ་བར་བྱེད་པ་ན༌[^3673]དེ་སྐྱོ་བར་གྱུར་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྦགས་པ་ལ་ཕྱག་མི་བྱའོ། །

[Block 3577]
སྦགས་པས་ཕྱག་མི་བྱའོ། །

[Block 3578]
སྦགས་པས་ཕྱག་བདག་གིར་མི་བྱའོ། །

[Block 3579]
སྦགས་པ་ལས་ཕྱག་བདག་གིར་མི་བྱའོ། །

[Block 3580]
སྦགས་པ་ལ་ཕྱག་འཚལ་ལམ། སྦགས་པས་ཕྱག་འཚལ་ལམ། སྦགས་པས་ཕྱག་བདག་གིར་བྱེད་དམ། སྦགས་པ་ལས་ཕྱག་བདག་གིར་བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3581]
སྦགས་པ༌[^3674]ནི་རྣམ་པ་གཉིས་ཏེ། ཐ་ན་སོ་ཤིང་ཡན་ཆད་ཟ་བས་སམ། ཐ་ན་དེའི་ས་བྱི་དོར་བྱེད་པ་ཡན་ཆད་མི་གཙང་བས་སོ་ཞེས་བྱ་བ་ནི་ཟ་བས་སྦགས་པ་ནི་ཐ་ན༌[^3675]སོ་ཤིང་ཡན་ཆད་ཟ་བས་སྦགས་པ་ཡིན་ནོ། །

[Block 3582]
མི་གཙང་བས་སྦགས་པ་ནི་ཐ་ན་མི་གཙང་བའི་ས་བྱི་དོར་བྱེད་པ་ཡན་ཆད་གྱིས༌[^3676]སྦགས་པ་ཡིན་ནོ། །

[Block 3583]
འདི་ལ་གཅེར་བུ་ཉིད་དང་གོས་གཅིག་པ་ཉིད་ནི་སྦགས་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་འདི་ལ་ཞེས་བྱ་བ་ནི་ཕྱག་བྱ་བ་ལ་སྟེ། དེས་གཅེར་བུ་ལ་ཕྱག་མི་བྱའོ། །

[Block 3584]
གཅེར་བུས་ཕྱག་མི་བྱའོ། །

[Block 3585]
གཅེར་བུས་ཕྱག་བདག་གིར་མི་བྱའོ། །

[Block 3586]
གཅེར་བུ་ལས་ཕྱག་བདག་གིར་མི་བྱའོ། །

[Block 3587]
དེ་བཞིན་དུ་གོས་གཅིག་པ་ལ་ཕྱག་མི་བྱའོ། །

[Block 3588]
གོས་གཅིག་པས་ཕྱག་མི་བྱའོ། །

[Block 3589]
གོས་གཅིག་པས་ཕྱག་བདག་གིར་མི་བྱའོ། །

[Block 3590]
གོས་གཅིག་པ་ལས་ཕྱག་བདག་གིར་མི་བྱའོ། །

[Block 3591]
ཕྱག་ནི༌[^3677]རྣམ་པ་གཉིས་ཏེ། ཡན་ལག་ལྔས་ཕྱག་འཚལ་བ་དང་། སྒྱིད་པ་ལ་འཁྱུད་པས་ཕྱག་འཚལ་བའོ། །

[Block 3592]
སྦྲིད་བ་བྱུང་བ་ལ་སོས་ཞེས་བརྗོད་པར་མི་བྱ་སྟེ། རྒན་ཞུགས་དང་ཁྱིམ་པ་ལ་ནི་མ་གཏོགས་སོ། །

[Block 3593]
གསར་བུ་དེ་ལ༌[^3678]ཨ་རོག་གྱ༌[^3679]ཞེས་བརྗོད་པར་བྱའོ། །

[Block 3594]
རྒན་པོ་ལ་ནི་ཕྱག་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ལ་ཞེས་བྱ༌[^3680]ནི་སྦྲིད་པ་བྱུང་བ་དེ་ལ་ནི་གསར་བུས་ཕྱག་བྱའོ། །

[Block 3595]
སྦྲིད་པ་བྱུང་ན་ཡང༌[^3681]ངོ་ཞེས་བྱ་བ་ནི་གསར་བུ་རང་ལ་སྦྲིད་པ་བྱུང་ན་ཡང་རྒན་པོ་ལ་ཕྱག་བྱའོ། །

[Block 3596]
འདིར་གཞུང་ནི་གསར་བུས་སྦྲིད་པ་བྱུང་ན་ཕྱག་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3597]
དེ་བཞིན་གཤེགས་པ་ལ་ཚེ་དང་ལྡན་པ་དང་མིང་དང་རུས་བརྗོད་པས་ཀུན་དུ་སྤྱད་པར་མི་བྱའོ། །

[Block 3598]
ཉེ་བའི་ཚིག་དང་བྲལ་བར་དེའི་མཚན་ནས་གདུང་སྨོས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འོན་ཀྱང་ཉེ་བའི་ཚིག་དང་བཅས་པར་མཚན་ནས་གདུང་སྨོས་པར༌[^3682]བྱའོ། །

[Block 3599]
འདིར་གཞུང་ནི་འདི་ལྟར་ཉེ་བའི་ཚིག་དང་བཅས་ཏེ་སྟོན་པའི་མཚན་སྨོས་པར་བྱ་སྟེ། བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3600]
རྒན་པའི་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཉེ་བའི་ཚིག་དང་བྲལ་བར་མིང་དང་རུས་སྨོས་པར་མི༌[^3683]བྱའོ། །

[Block 3601]
འདི་ལ་གནས་བརྟན་དང་ཚེ་དང་ལྡན་པ་ནི་ཉེ་བའི་ཚིག་ཉིད་ཀྱི་ཚུལ་དང་མཐུན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་རྒན་པ་ལའོ། །

[Block 3602]
སྔ་མ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པ་ལ་སྟེ། སྟོན་པ་ལ་ནི་གནས་བརྟན་དང་ཚེ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་ཉེ་བའི་ཚིག་ཉིད་ཀྱི་ཚུལ་དང་མཐུན་པ་མ༌[^3684]ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3603]
ལག་གི༌[^3685]བླས་འགྲོ་བ་དང་འོང་བ་དང་ལྡན་པའི་གཞིར་གཙུག་ལག་ཁང་རབ་ཏུ་གནས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་འགྲོར་ཡང་ནུས་ལ་འོང་ཡང་ནུས་པའི་གཞིར་རོ། །

[Block 3604]
འདིར་གཞུང་ནི་མ་མོ་ལས།

[Block 3605]
ཕྱོགས་གང་དུ་དང་པོ་གཙུག་ལག་ཁང་རབ་ཏུ་གནས་པར་བྱེད་པ་དེ་དགེ་སློང་ལག་གི་བླས་དང་པོ་ཁོ་ནར་གཙུག་ལག་ཁང་གི་གཞི་བརྟག་པར༌[^3686]བྱ་སྟེ། འོང་བ་དང་ལྡན་པ་དང་འགྲོ་བ་དང་ལྡན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3606]
ཤིང་ལྗོན་པ་དང་རྫིང་བུ་དང་འཆག་ས་དག་དང་ངོ་ཞེས་བྱ་བ་ཡང་ལྡན་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཤིང་ལྗོན་པ་དང་ལྡན་པ་དང་རྫིང་བུ་དང་ལྡན་པ་དང་འཆག་ས་དང་ལྡན་པའི་གཞིར་གཙུག་ལག་ཁང་རབ་ཏུ་གནས་པར་བྱའོ། །

[Block 3607]
ཉེན་ཀོར༌[^3687]དང་ངོ་ཞེས་བྱ་བ་ནི་ཉེན་ཀོར༌[^3688]དང་ལྡན་པའི་གཙུག་ལག་ཁང་རབ་ཏུ་གནས་པར་བྱའོ། །

[Block 3608]
རྒྱུན་ལུགས་དང་ཀླག་ཅོར་དང་སྒྲ་དང་ཏུག༌[^3689]རིང་ཆུང་བར་རོ་ཞེས་བྱ་བ་ནི་རྒྱུན་ལུགས་ཉུང་བ་དང་ཀླག་ཅོར་ཆུང་བ་དང་སྒྲ་ཆུང་བ་དང་ཏུག༌[^3690]རིང་ཆུང་བར་གཙུག་ལག་ཁང་རབ་ཏུ་གནས་པར་བྱའོ། །

[Block 3609]
བྲམ་ཟེའི་ཀློག་པ་དང་འདུན་སའི་ཐ་སྙད་དང་གླང་པོ་ཆེ་དང་རྟ་ལ་སོགས་པའི་སྒྲ་ནི་སྒྲའོ། །

[Block 3610]
རྫ་རྔ་ལ་སོགས་པའི་སྒྲ་ནི་ཏུག༌[^3691]རིང་སྟེ་དེ་དག་ཆུང་བར་བྱའོ། །
--- END BLOCKS ---
