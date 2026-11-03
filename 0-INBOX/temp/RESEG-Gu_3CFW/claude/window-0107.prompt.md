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

[Block 3751]
སྔ་མ་དེ་གཉིས་གཏི་མུག་གིས་ཟ་བར་རོ་ཞེས་བྱ་བ་ལ། སྔ་མ་དེ་གཉིས་ཞེས་བྱ་བ་ནི་འདོད་ཆགས༌[^3855]ཞེ་སྡང་གི་རྣམ་པ་ཕུག་རོན་དང་སྦྲུལ་གཉིས་ཏེ། གཏི་མུག་གི་རྣམ་པ་ཕག་གིས་ཟ་བ་འདྲ་བ་བྲི་བར་བྱའོ། །

[Block 3752]
ཁོ་ར་ཁོར་ཡུག་ཏུ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཡན་ལག་བཅུ་གཉིས་དང་ཐམས་ཅད་མི་རྟག་པར་གཟུང་བར་རོ། །

[Block 3753]
སྟེང་དུ་སངས་རྒྱས་མྱ་ངན་ལས་འདས་པའི་དཀྱིལ་འཁོར་དཀར་པོ་ཉེ་བར་སྟོན་པའོ། །

[Block 3754]
འོག་ཏུ་བརྩམ་པར༌[^3856]བྱ་ཞིང་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་གཉིས་སོ་ཞེས་བྱ་བ་ནི་འདིར་བྲི་བར་བྱ་ཞེས་ཐམས་ཅད་དུ་དགོངས་པའོ། །

[Block 3755]
དེ་སྟོན་པར་བྱེད་པ་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་ལྷགས་པ༌[^3857]རྣམས་ལ་འཁོར་བའི་འཁོར་ལོ་དེ་སྟོན་པར༌[^3858]ནུས་པའི་དགེ་སློང་གཙུག་ལག་ཁང་དེར་གཞག་པར༌[^3859]བྱའོ། །

[Block 3756]
དེའི་ཁོ་ར་ཁོར་ཡུག་ཏུ་ཆོ་འཕྲུལ་ཆེན་པོ་དང་བདུད་འཇོམས་པ་དག་གོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་སྟོན་བྱེད་ནུས་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3757]
ཁྱམས་སུ་སྐྱེས་པའི་རབས་དག་གོ། །

[Block 3758]
དྲི་གཙང་ཁང་གི་སྒོར་གནོད་སྦྱིན་ཕྲེང་ཐོགས་དག་གོ། །

[Block 3759]
དཔོང༌[^3860]སའི་ཁང་པར་གནས་བརྟན་གྱི་གྲལ་དག་གོ། །

[Block 3760]
མཛོད་ཀྱི་སྒོར་ནི་གནོད་སྦྱིན་ལག་ན་དབྱུ༌[^3861]གུ་ཐོགས་པ་དག་གོ། །

[Block 3761]
ཟས་ཀྱི་ཁང་པར་ལག་ན་བཅའ་བ་ཐོགས་པ་དག་གོ། །

[Block 3762]
བསྲོ་ཁང་གི་ཁང་པར་ལག་ན་མྱུ་གུ་དང་བུམ་པ་ཐོགས་པ་དག་གོ། །

[Block 3763]
མེའི་ཁང་པར་གྲུལ་བུམ་མེ་སྦར་བར་བྱེད་པ་དག་དང་། གྲུལ་བུམ་གྱི་བུ་མོ་བྱི་དོར་ལ་སོགས་པ་བྱེད་པ་དང་། མེ་སྦར་བར་བྱེད་པ་དང་། སྦྱིན་བདག་མར་མེ་ཐོགས་པ་དང་ལྷའི་ཕོ་ཉ་དག་གོ། །

[Block 3764]
ཆུའི་ཁང་པར་ཀླུ་ལག་ན་བུམ་པ་ཐོགས་པ་རྒྱན་སྣ་ཚོགས་ཀྱིས་བརྒྱན་པ་དག་དང་ཀླུའི་བུ་མོ་ཆུ་འདྲིམ་པར་བྱེད་པ་དག་གོ། །

[Block 3765]
ནད་པའི་རུང་བའི་ཁང་པར་དེ་བཞིན་གཤེགས་པ་ནད་པའི་རིམ་གྲོ་མཛད་པའོ། །

[Block 3766]
བཤང་བ་དང་གཅི་བའི་སྐྱབས་སུ་དུར་ཁྲོད་དག་གམ་མགོ་བོའི་ཐོད་པ་དག་གོ། །

[Block 3767]
གཙུག་ལག་ཁང་བླ་ཁབ༌[^3862]མེད་པ་མ་ཡིན་པར་མེ་དུ་བ་ཅན་དང་བཅས་པ་བུད་པར་ཡང་མི་བྱ། བཅང་བར་ཡང་མི་བྱའོ། །

[Block 3768]
སྤྱིལ་བུར༌[^3863]ནི་ཐམས་ཅད་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མེ་དུ་བ་ཅན་དང༌[^3864]དུ་བ་མེད་པ་ཐམས་ཅད་བུད་པར་མི་བྱ་བཅང་བར་ཡང་མི་བྱའོ་ཞེས་བྱ་བར༌[^3865]སྦྱར་རོ། །

[Block 3769]
དེའི་དོན་དུ་ཞུགས་ལིང་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་དོན་ཞེས་བྱ་བ་ནི༌[^3866]མེ་འབུད་པ་དང་བཅང་བ་དེའི་དོན་དུ་ཞུགས་ལིང་བཅང་བར་བྱའོ། །

[Block 3770]
འདིར་གཞུང་ནི་སིལ༌[^3867]བུ་དག་ལས།

[Block 3771]
དགེ་སློང་དག་དགུན་སྨད་ཀྱི་དུས་སུ་ལྷགས་པས་ཉེན་ནས་སྤྱིལ་བུར་མེ་བུད་པར༌[^3868]བྱེད་པ་ན་སྤྱིལ་བུ་མ་རུང་བར་གྱུར་ནས།[^3869] བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྤྱིལ་བུར་མེ་བུད་པར་མི་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3772]
མཉམ་པར་བཅེར༌[^3870]བའི་ཕྱིར་ལྕགས་ཀྱི་ཕྲ་སྐམ་མོ་ཞེས་བྱ་བ་ནི་བཅང་བར་བྱའོ་ཞེས་བྱ་བར༌[^3871]སྦྱར་ཏེ།[^3872] མེའི་ཕྱོགས་ཕན་ཚུན་ནས་བསྐུལ་བ་ནི་མཉམ་པར་བཅེར་བ༌[^3873]ཞེས་བྱའོ། །

[Block 3773]
ལྕགས་ཀྱི་ཕྲ་སྐམ་ཞེས་བྱ་བ་ནི་ལྕགས་ཀྱི༌[^3874]ཐལ་ཕྱགས་སོ། །

[Block 3774]
ཤིང་གི་ཡོག་པས་ཀྱང་ལས་དེ་འགྲུབ་པོ་ཞེས་བྱ་བ་ནི་ཕྲ་སྐམ་གྱི་ལས་དེ་འགྲུབ་བོ། །

[Block 3775]
ཁང་སྐྱོང་གིས་གཙུག་ལག་ཁང་དེ་ཉི་མ་རེ་རེ་ཞིང་ཕྱག་དར་བྱའོ། །

[Block 3776]
མི་ནུས་ན་མཁོ་བའི༌[^3875]ཕྱོགས་སོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་མཐའ་དག་ཕྱག་དར་བྱེད་མི་ནུས་ན་གཙུག་ལག་ཁང་གི་ཕྱོགས་གང་མཁོ་བ་དེ་ཕྱག་དར་བྱའོ། །

[Block 3777]
ལྷག་མ་ནི་ཚེས་བརྒྱད་དམ་བཅུ་བཞི་ལ་གཎྜཱི་བརྡུངས་ཏེ་དགེ་འདུན་ཐམས་ཅད་ཀྱིས་ཆོས་དང་ལྡན་པའི་གཏམ་གྱིས་སམ། འཕགས་པའི་མི་སྨྲ་བ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་མཁོ་བའི་ཕྱོགས་ཀྱི་ལྷག་མ་ཕྱག་དར་མ་བྱས་པ་གང་ཡིན་པ་དེ་དག་དུས་དེར་དགེ་འདུན་ཐམས་ཅད་ཀྱིས་རིམ་པ་འདིས་ཕྱག་དར་བྱའོ། །

[Block 3778]
ཆོས་ཀྱི་མདུན་སར་ཆག་ཆག༌[^3876]དང་ལྕི་བ་འཇམ་པོའི་བྱུག་པས་བྱུག་གོ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་དང་དགག་དབྱེ་ལ་སོགས་པ་ཆོས་ཀྱི་འདུན་སའི༌[^3877]གནས་དེར་རོ། །

[Block 3779]
མཇུག་ཏུ་ཁྲུས་བྱའོ་ཞེས་བྱ་བ་ནི་ཕྱག་དར་ལ་སོགས་པ་ཟིན་པའི་མཇུག་ཏུའོ། །

[Block 3780]
ཡང་ན་རྐང་ལག་བཀྲུའོ། །

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
--- END BLOCKS ---
