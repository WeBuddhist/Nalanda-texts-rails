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
[Block 3956]
འདིར་གཞུང་ནི་འོན་ཀྱང་ཡུར་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དབྱུག་གུ་གཟུགས་པར་བྱའོ། །

[Block 3957]
དགེ་སློང་དག་གིས་སྨྱིག་མ༌[^2729]བརྩལ་ཏེ་དེས་འཛུག་པ་ལས་རྨ་བྱུང་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བྲེའི་བཅད་འཕྲོ་ལྟ་བུར་བྱའོ། །

[Block 3958]
འོན་ཀྱང་སྣད་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རས་མ་དག་གིས་དཀྲིས་ནས་དལ་བུས་ཁད་ཀྱིས༌[^2730]གཟུགས་པར་བྱའོ༌[^2731]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3959]
ཕོ་ལང་འཕང་བར་བྱའོ། །

[Block 3960]
ཡང་ཕྱིར་འོང་བར་བྱ་བའི་ཕྱིར་ཐ་གུས་གདགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི། ཕོ་ལང་དེ་ཡང་ཕྱིར་དྲང་བར་བྱ་བའི་ཕྱིར་ཐ་གུ་ཕྲ་མོ་རིང་མོས་བཏགས་ཏེ་འཕང་བར༌[^2732]བྱའོ། །

[Block 3961]
དེ་ལྟར་བྱས་ན་ཡང་དང་ཡང་དུ་འཕང་ཞིང་བླང་སླ་བར་འགྱུར་རོ། །

[Block 3962]
འདིར་གཞུང་ནི་འོན་ཀྱང་ཡུར་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཕོ་ལོང་འཕང་བར་བྱའོ། །

[Block 3963]
དགེ་སློང་དག་གིས་མུན་ཁུང་ན་མི་མཐོང་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཐ་གུས༌[^2733]བཏགས་ཏེ་འཕང་བར་བྱ་ཞིང་། དེ་ནས་ཡང་ཕྱིར་དྲན་པར༌[^2734]བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3964]
མདུན་དུ་མར་མེ་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཉིད་བསལ་བའི་དོན་དུ་ཆོ་ག༌[^2735]འདི་ཡིན་ཏེ། འདིར་གཞུང་ནི་འོན་ཀྱང་ཡུར་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། མདུན་དུ་མར་མེ་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3965]
འོན་ཀྱང་གཉིད་མ་སངས་ན༌[^2736]རྐང་པ་དབྱུང་ངོ་། །འོན་ཀྱང་མ་སངས་ན་ཡ་གཅིག༌[^2737]བརྐྱང་ངོ་ཞེས་བྱ་བ་ན། [^2738]རྐང་པ་དབྱུང་ངོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3966]
འདིར་གཞུང་ནི་འོན་ཀྱང་ཡུར་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རྐང་པ་ཡ་གཅིག༌[^2739]བརྐྱང་བར་བྱའོ། །

[Block 3967]
འོན་ཀྱང་ཡུར་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རྐང་པ་ཡ་གཅིག་ཀྱང་བརྐྱང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3968]
མི་འཐོམ་པར་བྱ་བའི་ཕྱིར་ཕྲེང་ཐག་དེ་དག་དེ་ལྟ་བུ་ལ་བཀོད་པའི་བུ་གུའམ། དེ་ལ་བཏགས་པའི་ཐག་པ་ལ་འཇུས༌[^2740]ཏེ་བཅག་པར་བྱའོ་ཞེས་བྱ་བ་ནི། ཕྲེང་ཐག་ཆད་པར་རབ་ཏུ་བརྐྱངས་པ༌[^2741]དེ་ལྟ་བུ་ལ་སྨྱུ་གུའི་སྦུབས༌[^2742]ལ་སོགས་པ་བསྐོན་པ་ལ་འཇུས་ཏེ་བཅག་པར་བྱའོ། །ཅིའི་དོན་དུ་འཇུས་ཤེ་ན། བཀའ་སྩལ་པ། མི་འཐོམ་པའི་དོན་དུ་སྟེ། འདིར་གཞུང་ནི་འོན་ཀྱང་ཡུར་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ལངས་ཏེ་བཅག་པར་བྱའོ། །

[Block 3969]
དགེ་སློང་དག་འཆག་པ་ན་འཐོམས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཕྲེང་ཐག་ལ་འཇུ་བར་བྱའོ། །

[Block 3970]
དེ་དག་ལག་པས་འཆང་བ་རྒྱུད་བྱེད་དམ། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྦུ་གུ་བསྐྱོན༌[^2743]ནས་སྐུད་པས་བཏགས་པ་ལ་འཇུས་ཏེ། བཅག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3971]
འདིར་སྦུ་གུ་ལ་འཇུས་པ་ནི་སྦྱོར་བ་སྟེ། གཞུང་ལས་ཀྱང་འཐོགས་པ་སྲིད་པ་དེ་བས༌[^2744]ན་དེ་ལྟར་ཉེ་བར་འབྲེལ་པའོ། །

[Block 3972]
མཆི་ལ་ལྷམ་ཅན་གྱིས་བཅག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྤོང་བ་ཉི༌[^2745]ཚེར་མ་ཟད་ཀྱི་འོ་ན་གང་ཞེ་ན། མཚོན་པའི་ཕྱིར་སྤོང་བ་པའི་ཞེས་སྨོས་པས་རིག་པར་བྱའོ། །

[Block 3973]
རྐང་པ་གཉིས་ལ་རྡུལ་མི་འགོ་བར་བྱ་བའི་ཕྱིར་པར་ཐང་འདིང༌[^2746]བར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་པར་ཐང་ཞེས་སྨོས་པ་ནི།

[Block 3974 [VERSE]]
འཇམ་པོ་དང་སྟན་གཞན༌[^2747]དག་གི་དཔེ་ཡིན་ནོ། །
མི་འགོ་བར༌[^2748]བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི།
རྡུལ་གྱིས་མི་འགོ་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3975]
འདི་ནི་དཔེ་ཙམ་ཡིན་གྱི༌[^2749]ལུས་ཡིད་དུ་འོང་བ་ལ་དེ་བས་གཞན་གྱིས་ཀྱང་ལུས་ཀྱི་གོས་དང་སྟན་རྣམས་ཀྱིས་ཉམས་པ་བས་ལ་བའི་ཕྱིར། རྐང་པ་ཕྱི་བ་དང་། བསྡུ་བ་དང་། རྐང་པ་རྡུལ་ཅན་གྱིས་སྐྱིལ་མོ་ཀྲུང༌[^2750]འཆའ་བའི་རྒྱུ་མཚན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3976]
སྤོང་བ་པས་ཞག་གསུམ་ཞིང་རྐང་པ་གཉིས་བསྐུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། ཞག་གསུམ་གསུམ་ཞིང་རྐང་པ་གཉིས་བསྐུ་བར་བྱ་སྟེ། དེ་ལས་ལྷག་པར་ནི་མ་ཡིན་ཏེ་ཞེས་དེ་ལྟར་འདི་ནི་གཙོ་བོ་ཡིན་ནོ། །

[Block 3977]
མ་ནུས་ན་དེར་ཡང་ཉལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། གཉིད་བྲོ་བས་བསད་པར་མ་ནུས་ན། རྣལ་འབྱོར་གྱི་གནས་དེར་ཡང་ཉལ་བ་ཉེས་པ་མེད་པ་སྟེ། རྣལ་འབྱོར་གྱི་གནས་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3978]
དེ་ལ་འདི་ནི་རྣལ་འབྱོར་དང་བཅས་པ་ཉིད་ཀྱིས་དེར་ཞུགས་པ་སྲིད་པའི་ཕྱིར་གཞན་དུ་སོང་སྟེ། འདི་བྱེད་པ་རིགས་པ་ཞེས་བྱ་བ་དེའི་འདོད་པ་བསལ་བའི་དོན་དུའོ། །

[Block 3979]
སྒོ་བཅད་པར་རོ་ཞེས་བྱ་བ༌[^2751]ལ་འདི་ནི་གཞན་དག་མ་དད་པར་འགྱུར་བ་དང་། ཐོ་འཚམས༌[^2752]པར་འགྱུར་བའི༌[^2753]སྤང་བའི་ཕྱིར། སྒོ་གླེགས་ལ་སོགས་པས་སྒོ་བཅད་པ༌[^2754]དེར་ཉལ་བ་ལ་ཉེས་པ་མེད་དོ། །

[Block 3980]
གློས་ཀྱང་ཕབ་སྟེའོ་ཞེས་བྱ་བ་ནི། ཉལ་དུ་རུང་ངོ་ཞེས་བྱ་བའི་དོན་དུའོ། །

[Block 3981]
དེ་ཡང་སྟན་ལ་ཉལ་བ་འདིར་རུང་བ་མ་ཡིན་གྱི་གཞན་ནི་མ་ཡིན་ཞེས་བྱ་བ་འདོད་པ་བསལ་བའི་དོན་དུའོ། །

[Block 3982]
དེ་ཡང་སྟན་ལ་ཉལ་བ་འདིར་རུང་བ་ཡིན་གྱི་གཞན་ནི་མ་ཡིན་ཞེས་བྱ་བ་འདོད་པའི་དོན་དུའོ། །

[Block 3983]
སྤོང་བ་པའི་ཕྱིར་ཞལ་ཏ་པ་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། ཇི་ལྟར་འོས་པ་དེ་དགེ་འདུན་གྱིས་གསོལ་བ་དང་གཉིས་ཀྱིས་བསྐོ་བར་བྱའོ། །

[Block 3984]
དེའི་བྱ་བ་ནི་ལངས་མ་ཐག་ཁོ་ནར་ཆག་ཆག་གདབ་པ་དང་། ཕྱག་དར་བྱ་བ་དང་། ལྕི་བསར་པའི་བྱུག་པས་བསྐུ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། སྤོང་བ་པའི་ཞལ་ཏ་བ་དེས་ལས་སུ་བྱ་བ་སྟེ། དེས་བྱ་བའི་ལས་འོག་ནས་འབྱུང་བ་ཐམས་ཅད་ལ་སྤྱིར་སྦྱར་རོ། །

[Block 3985]
ལངས་མ་ཐག་ཁོ་ནར་ཞེས་བྱ་བ་ནི། ནམ་ལངས་མ་ཐག་ཁོ་ནར་ལངས་ནས་སོ། །

[Block 3986]
སྟན་བཤམ་པར་བྱའོ། །

[Block 3987]
མི་གཙང་བའི་སྐྱབས་གཉིས་ཀྱིས༌[^2755]བྱི་དོར་བྱའོ་ཞེས་བྱ་བ་ནི་བཤང་བ་དང་གཅི་བའི༌[^2756]ས་གཉིས་བྱི་དོར་བྱའོ། །

[Block 3988]
ཆག་ཆག་ལ་སོགས་པས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲས་ནི་ཕྱག་དར་བྱ་བ་དང་། ལྕི་བ་སར་པའི་བྱུག་པས་བསྐུ་བ་དག་བསྡུས་སོ། །

[Block 3989]
བོང་རྡོག་དང་། ས་དང་ཆུ་དག་གཞག༌[^2757]པར་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་དག་པར་བྱ་བའི་ཕྱིར་དུས་དང་མཐུན་པའི་ཆུ་ཞེས་བྱ་བ་ཕྲན་ཚེགས་དག་གི་རྗེས་སུ་འབྲངས་ནས་ཤེས་པར་བྱའོ། །

[Block 3990]
བསྡུ་བའི་ཕྱིར་གཎྜཱི་བརྡུང་ངོ་ཞེས་བྱ་བ་ནི། སྤོང་བ་པ་རྣམས་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 3991]
དེའི་གནས་ནི་ཁང་སྟེང་ངོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་གཎྜཱི་བརྡུང་བ་དེའི་གནས་དེའོ། །

[Block 3992]
གང་དང་གང་དུ་དེ་དང་དེ་བརྗོད་པ་དེར་འདི་གནས་པར་རྟོགས་པར་བྱ་སྟེ། དེ་བས་ན་འདིས༌[^2758]བྱས་པའོ། །

[Block 3993]
དེའི་ཁང་སྟེང་དུ་སྒྲུབ་པ་ལ་མཆོག །དེ་བས་ན་གཞན་ཁང་སྟེང་གི་རྣམ་པ་མ་ཡིན་ཏེ། འདིར་དེའི་གནས་སུ་གཏོགས་པའི་གནས་དེ་དང་དེར་ཁང་ཐོག་ཏུ་འཛེགས་ནས་བཀླག་པར༌[^2759]བྱའོ་ཞེས་བྱུང་བ་ཡིན་ཏེ། དེ་བས་ན་མདོ་འདིའོ། །

[Block 3994]
དེ་སྒྲུབ་པར་བྱེད་པས༌[^2760]ནི་མ་ཡིན་ཞེས་བྱ་བ་འདོན་པས་མེད་པར་ཤེས་པར་བྱ་བ་སྟེ། དགོངས་པ་མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3995]
དགེ་འདུན་བསྡུ་བའི་ཕྱིར་ནི་རྒྱུད་གསུམ་དང་དེ་སྙེད་ཀྱི་ཏོག༌[^2761]དག་གོ་ཞེས་བྱ་བ་ནི་ལན་གསུམ་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
