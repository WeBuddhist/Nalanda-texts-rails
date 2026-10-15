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
[Block 3641]
གཞན་གདགས་པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རྙིངས་པ་ཕྱིར་བཅོས་པར་བྱ་བའི་ཕྱིར་འབོགས་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་སར་པ་གཞན་གདགས་པའི་ཕྱིར་འབོགས་པ་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །

[Block 3642]
དེའི་དོན་དུ་ཉེ་བར་མ་བཞག་པར་འགོག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་གདགས་པ་དེའི་དོན་དུ་གདུགས་ལ༌[^3738]སོགས་པ་ཉེ་བར་མ་བཞག༌[^3739]པར་སྔ་མ་དབོག༌[^3740]པར་མི་བྱའོ། །

[Block 3643]
འདིར་གཞུང་ནི་གཞན་དག་གིས༌[^3741]གདུགས་དག་ཕོག་པར་གྱུར་ནས་དེ་དག་རབ་ཏུ༌[^3742]དུས་བྱེད་པར་གྱུར་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཇི་སྲིད་དུ་གཞན་དག་ཉེ་བར་མ་བཞག་པ༌[^3743]དེ་སྲིད་དུ་དབོག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3644]
སྐྱེས་པའི་རབས་ལ་སོགས་པའི་རི་མོ་དང་། སངས་རྒྱས་ཀྱི་བཀའི་ཡི་གེ་དག་ཀྱང་ཞེས་བྱ་བ་ནི་དེ་དག་ཀྱང་རྙིངས་པ་བཅོས་པའི་ཕྱིར་ཕྱིས་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །ཅི་ཞིག་གི་ཕྱིར་ཕྱིས་པ་ལ་བྱ་ཞེ་ན། དེའི་ཕྱིར་བྱིད་པའི༌[^3744]བྱེ་བྲག་ཁོ་ན་བྱ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱིད་པའི༌[^3745]བྱེ་བྲག་གང་ཡིན་པ་དེ་ཁོ་ན་བྲི་བའི་ཕྱིར་ཡིན་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 3645]
རྩོམ་པར་བྱེད་པས་མ་བྱས་ན༌[^3746]གཞན་གྱིས༌[^3747]ལྷག་མ་བྱའོ་ཞེས་བྱ་བ་ནི་གང་གིས་མཆོད་རྟེན་དང་གཙུག་ལག་ཁང་དག་རྩོམ་པར་བྱེད་པ་དེ༌[^3748]བརྩམས་ནས་མ༌[^3749]ཟིན་པར་མ་བྱས་ན་གཞན་གྱིས་དེའི་ལྷག་མ་བྱ་བ་ལ་མི་རིགས་པ༌[^3750]མེད་པའོ། །

[Block 3646]
གལ་ཏེ་དགེ་འདུན་གྱི་ཕྱིར་ཕྱེད་བརྩིགས་ན་འཁར་ལེན༌[^3751]སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འདི་ལ་ཚུལ་དང་མི་མཐུན་པ་མེད་པར༌[^3752]ཤེས་པར་བྱའོ། །

[Block 3647]
དེ་བས་ན་དེའི་བརྗོད་པ་འདིའོ། །

[Block 3648]
འདིར་ཕྱེད་ཅེས་བྱ་བའི་སྒྲ་ནི་ཆ་ཤས་ལ་སྙེགས༌[^3753]ཀྱི་ཆ་མཉམ་པའི་ཕྱེད་ཁོ་ན་ནི་མ་ཡིན་ཏེ། ཅུང་ཟད་ཙམ་བརྩིགས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3649]
འདིར༌[^3754]རྣམ་པར་འབྱེད་པ་ལས།

[Block 3650]
[^3755] བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གཞི་མ་ཟིན་པ་ལ་ཞེས་བྱ་བ་ནས་འདི་ལྟར་ལྷན་ཅིག་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3651]
དེས་བསྟང་བའི༌[^3756]དུས་ནི་གལ་ཏེ་དགུན་ཡིན་ན་ཟས་ཀྱི་འོག་རོལ་དུའོ། །

[Block 3652]
གལ་ཏེ་སོ་ག་ཡིན་ན་ཟས་ཀྱི་མདུན་རོལ་དུའོ་ཞེས་བྱ་བ་ལ། དུས་ནི་མཁར་ལེན༌[^3757]གྱིས་བསྟང་བ༌[^3758]དེའི་དུས་སོ། །

[Block 3653]
འདིར་གཞུང་ནི་དགེ་སློང་དག་སོ་ག་ནི་ཟས་ཀྱི་འོག་རོལ་དུ་ལས་བྱེད་ལ། དགུན་ནི་ཟས་ཀྱི་མདུན་རོལ་དུ་ལས་བྱེད་ནས།[^3759] བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགུན་ནི་ཟས་ཀྱི་འོག་རོལ་དུ་ལས་བྱ༌[^3760]ལ། སོ་གས༌[^3761]ནི་ཟས་ཀྱི་མདུན་རོལ་དུ་ལས་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3654]
ཟས་ཀྱི་བྱ་བའི་དུས་ལུས་པར་རོ་ཞེས་བྱ་བ་ནི་ཇི་སྲིད་དུ་ཟས་ཀྱི་བྱ་བ་ལྷུང་བཟེད་བཀྲུ་བ་ལ་སོགས་པ་དག་གི་དུས་ལས་ཡོལ་བར་གྱུར་པ་དེ་སྲིད་དུ་ལས་མི་བྱའོ།[^3762] །དེའི་ལས༌[^3763]བྱི་དོར་མ་བྱས་པར་འཚོ་བ་ལ་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་བསྟང་བའི༌[^3764]བྱ་བ་ལས་སོ། །

[Block 3655]
འཚོ་བ་ལས་ཞེས་བྱ་བ་ནི་བསོད་སྙོམས་ཀྱི་ཕྱིར་འགྲོ་བ་ལ་སོགས་པའོ། །

[Block 3656]
དེའི་མཐའ་ནི་རྐང་ལག་བཀྲུས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེའི་མཐའ་ཞེས་བྱ་བ་ནི་བྱི་དོར་བྱས་པ་དེའི་མཐའོ། །

[Block 3657]
འདིར་མཐའི་སྒྲ་ནི་འདི་ཐམས་ཅད་ལས་ཆུང་བ་ཉིད་ལ་སྨོས་སོ། །

[Block 3658]
ལག་གི༌[^3765]བླས་ཁྱེའུ་སུས་སྦྱོར་དུ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དགེ་སློང་དག་ཟས་ཀྱི་མདུན་རོལ་དུ་བྱེད་ན་དེའི་ཚེ་ལག་གི༌[^3766]བླས་ཁྱེའུ་སུས་སྦྱོར་དུ་གཞུག་གོ། །

[Block 3659]
ཟས་ཀྱི་འོག་རོལ་དུ་ནི་སྐོམ་དང་རྐང་ལག་བསྐུ་མཉེ་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དགེ་སློང་དག་ཟས་ཀྱི་འོག་རོལ་དུ་ལས་བྱེད་ན་དེའི་ཚེ་ལག་གི་བླས་སྐོམ༌[^3767]ལ་སོགས་པ་སྦྱོར་དུ་གཞུག་པའོ། །

[Block 3660]
གནས་ཁང་དག་གི་སྒོ་གདོད་དོ། །

[Block 3661]
སྒོ་གླེགས༌[^3768]གཞུག་གོ། །

[Block 3662]
ལག་གཟུངས་དང་ཡང་མིག་དང་ཀོ་བའི་དུམ་བུ་དག་གོ་ཞེས་བྱ་བ་ནི་གཞུག་གོ་ཞེས་བྱ་བའི་རྗེས་སུ་སྦྱར་རོ། །

[Block 3663]
སྐར་ཁུང་དག་གདོད་དོ་ཞེས་བྱ་བ་ནི་གནས་ཁང་ལའོ། །

[Block 3664]
ཕྱོགས་གང་དུ་གདོད་པར་བྱ་ཞེ་ན་དེའི་ཕྱིར་དཀྱིལ་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་རྩིག་ངོས་ཀྱིའོ། །

[Block 3665]
དབྱིབས་ཅི་འདྲ་བ་ཞེ་ན། [^3769]ཕྱི་རུབ་ལ་ནང་ཡངས་པ་རྒྱ་མཚོའི་རྣམ་པ་ལྟ་བུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒྱ་མཚོ་ལྟར་བྱིན་གྱིས་ཡངས་པའོ། །

[Block 3666]
དྲ་བ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་སྟེགས༌[^3770]བུའི་རྣམ་པ་འདིར་རིག་པར་བྱ་སྟེ་སྐར་ཁུང་ལ་སྟེ། དྲ་བ་ཞེས་བྱ་བ་གང་ཞིག་བསྟན་པ་དེ་ནི་འདིར་སྟེགས་བུ་དེའོ། །

[Block 3667]
སྒོ་གླེགས་སོ་ཞེས་བྱ་བ་ནི་སྐར་ཁུང་ལ་གཞུག་པར་བྱའོ། །

[Block 3668]
འཁོར་གཏན་དང་གནམ་གཟེར་དང་འཕྲེད༌[^3771]གཏན་དག་གོ་ཞེས་བྱ་བ་ནི་སྒོ་གླེགས་དེ་ལ་གཞུག་པར་བྱ། [^3772]དབྱུག་གུ་སྐམ་ཁ་བཅང་ངོ་། །གསོར་གྱིས་བཙུགས༌[^3773]པས་རྒྱུའོ༌[^3774]ཞེས་བྱ་བ་ནི་ཐག་མ༌[^3775]རྒྱུ་བ་ཐམས་ཅད་ནི་གསོར་གྱིས་བཙུགས་པའི་ཐབས་ཀྱིས་བྱ་བའོ། །

[Block 3669]
གནས་ཁང་གི་མདུན་དུ་ཁྱམས་བྱའོ་ཞེས་བྱ་བ་སྨོས་ན། ཕྱོགས་གང་དུ་བྱ་ཞེ་ན་དེའི་ཕྱིར་གནས་ཁང་གི་མདུན་དུའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3670]
རིམ་པ་གང་གིས༌[^3776]འདི་བྱ་ཞེ་ན་དེའི་ཕྱིར། སོ་ཕག་གི་གཅལ་བདུན་ནམ་བརྒྱད་གཞུག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་ཁང་གི་རྩིག་པའི་འོག་གཞིའི་གཅལ་དུ་སོ་ཕག་རིམ་པ་བདུན་ནམ་བརྒྱད་གཞུག་པར་བྱ་བའོ། །

[Block 3671]
དེའི་སྟེང་དུ་ཀ་ཏན༌[^3777]གྱི་སྤང་ལེབ་བོ་ཞེས་བྱ་བ་སྨོས་པས་ཀ་ཏན་གྱི༌[^3778]སྤང་ལེབ་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སོ་ཕག་གི་གཅལ་དེའི་སྟེང་དུ་ཀ་ཏན༌[^3779]གྱི་སྤང་ལེབ་གཞུག་པར་བྱའོ། །

[Block 3672]
དེའི་སྟེང་དུ་ཀ་བའི་ཚར་དག་གོ་ཞེས་བྱ་བ་ནི་ཀ་ཏན༌[^3780]གྱི་སྤང་ལེབ་དེའི་སྟེང་དུ་ཀ་བའི་ཚར་དག་གཟུགས་པའོ། །

[Block 3673]
དེ་དག་གི་སྟེང་དུ་ཀ་ཞུའི༌[^3781]འདབ་མ་དག་གོ་ཞེས་བྱ་བ་ལ། དེ་དག་གི་ཞེས་བྱ་བ་ནི་ཀ་བའི་ཚར་དེ་དག་གི་སྟེང་དུ་ཀ་ཞུའི༌[^3782]འདབ་མ་དག་གཞུག་པའོ། །

[Block 3674]
དེ་དག་གི་སྟེང་དུ་གདུང་མ་དག་གོ། །

[Block 3675]
དེ་དག་གི་སྟེང་དུ་ཕྱམ་དག་གོ། །

[Block 3676]
དེ་དག་གི་སྟེང་དུ་སྤང་ལེབ་དག་གོ། །

[Block 3677]
དེ་དག་གི་སྟེང་དུ་སོ་ཕག་དགྲམ་མོ། །

[Block 3678]
དེ་དག་གི་སྟེང་དུ་སོ་ཕག་གི་ཕྱེ་མའི་འཇིམ་པའོ་ཞེས་བྱ་བ་ནི་དེ་དག་གི་སྟེང་དུ་སོ་ཕག་གི་ཕྱེ་མའི་འཇིམ་པ་གླན་པར་བྱ་བའོ།[^3783] །མི་ལྟུང་བར་བྱ་བའི་ཕྱིར་ལན་ཀན་བྱའོ། །

[Block 3679]
མི་འགུལ་བར་བྱ་བའི་ཕྱིར་ཤར་བ་གཞུག་གོ། །

[Block 3680]
དེ་ལྕགས་ཀྱི་གཟེར་བུ་དག་གིས་སྦྱར་རོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་དེ༌[^3784]ཤར་བ་དེའོ། །
--- END BLOCKS ---
