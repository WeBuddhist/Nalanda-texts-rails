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
[Block 3886]
གཏུམ་པོ་ཞེས་བྱ་བ་སྨོས་པས་ནི་དེ་དག་དགོན་པར་བསྒོམ་པར་མི་བྱའོ་ཞེས་བྱ་བར་གསུངས་པ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 3887]
འདིར་སེང་གེ་ལ་སོགས་པ་གཏུམ་པོ་རྣམས་འབྱུང་བར་འགྱུར་བ་དེའི་ཕྱིར་འདི་སྤང་བར་བྱའོ། །

[Block 3888]
གྱ་ཚོམ་ཞེས༌[^2670]སྨོས་པ་ནི་དེ་དག་གྲོང་གི་ཉེ་འཁོར་དུ་དོར་ཏེ༌[^2671]སྒོམ་པར་བྱེད་པ་ན། མ་དད་པའི་གྱ་ཚོམ་བྱེད་པ་དག་འདི་སྐད་དུ་འཕགས་པ་དག་ཅི༌[^2672]ཁྱེད་འགའ་ཞིག་ཤི་བ་དང་ལྡན་པ་ཡིན་ནམ་ཞེས་ཅོ་འདྲི་བར་བྱེད་པ་ནས།[^2673] བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ས་ཕྱོགས་དེར་ཡལ་བར་དོར་བ་རྣམས་དང་། ཀི་ཏ་ཀ་དང་། ཀི་ལེན་ཛ་རྣམས་ཀྱིས་བསྐོར་བར་བྱའོ། །

[Block 3889]
ས་ཕྱོགས་དེ་ཇི་སྲིད་དུ་ཡལ་ག་རྣམས་ཀྱིས་བསྐོར་བར་གྱུར་གྱི་བར་དུ་གྱ་ཚོམ་པ་མ་དད་པ་དག་འདི་སྐད་ཅེས་འཕགས་པ་དག །ཅི་ཁྱེད་འགའ་ཞིག་རས༌[^2674]བལ་གྱི་ལྡུམ་ར༌[^2675]བྱེད་དམ་ཞེས་ཅོ་འདྲི་བར་བྱེད་པའི་སྐབས་དེ༌[^2676]ས་ཕྱོགས་དེར་ཚེར་མ་དང་། ཆུའི་འོབས་དག་གིས་བསྐོར་བར་བྱའོ། །

[Block 3890]
ས་ཕྱོགས་ཚེར་མ་དག་ཆུའི་འོབས་ཀྱིས་བསྐོར་བར་གྱུར་པ་དང་། གྱ་ཚོམ་པ་མ་དད་པ་དག་འདི་སྐད་ཅེས་ས་བོན་གྱིས་བཀང་བའི་ལྡུམ་ར་ཡིན་ནམ། འོན་ཏེ་སེའུ་འབྲུའི་ལྡུམ་ར་ཡིན་ཞེས་བྱ་བ་ནས། སྤོང་ཁང་བརྩིག་པར༌[^2677]བྱའོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ཏེ། མདོ་འདིས་ནི་དེ་དག་བསྡུས་པ་ཡིན་ནོ། །

[Block 3891]
དེའི་ཕྱིར༌[^2678]སྤོང་ཁང་གི་སྐབས་ཡིན་པས་ན། གྲོང་དང་ཉེ་བ་ལ་སོགས་པར་སྤོང་ཁང་བརྩིག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་རྣམ་པ་ཅི་འདྲ་ཞེ༌[^2679]ན། དེའི་ཕྱིར་གནས་ཁང་གཉིས་ཀྱི༌[^2680]བར་དུ་སྲང་གདོད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ངོས་ཡ་གཅིག་ཏུ་ཡང་གནས་ཁང་བརྩིག་ལ། ངོས་གཞན་ལ་ནི་གཞན་བརྩིག་ཅིང་བར་དུ་སྲང་གདོད་པར་བྱ་བ་སྟེ། འདི་ནི་སྤོང་ཁང་ཆུང་ངུའི་རྣམ་པ་ཡིན་ནོ། །

[Block 3892]
བར་དུ་སྲང་གདོད་དོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ངོས་ཡ་གཅིག་ཏུ་ཡང་གནས་ཁང་ལྔ་བརྩིག་ལ། ངོས་གཞན་ལྔ་བརྩིག༌[^2681]ཅིང་བར་དུ་སྲང་གདོད་པར་བྱ་བའམ། ངོས་ཡ་གཅིག་ཏུ་ཡང་དྲུག་བརྩིག་ལ། ངོས་གཞན་ལ་ཡང་དྲུག་བརྩིག་ཅིང་བར་དུ་སྲང་གདོད་པར་བྱ་སྟེ། འདི་ནི་སྤོང་ཁང་ཆེན་པོའི་རྣམ་པ་ཡིན་ནོ། །

[Block 3893]
སྤོང་ཁང་གཉིས་པོ་འདི་དག་ནི་ཆུང་ངུ་དང་ཆེན་པོ་སྟེ། ཆུང་ངུ་ནི་གནས་ཁང་གཉིས་པ་སྟེ་བར་དུ་སྲང་གདོད་པར་བྱའོ། །

[Block 3894]
འདིར་ཆེན་པོ་ནི་གནས་ཁང་བཅུ་པའམ། གནས་ཁང་བཅུ་གཉིས་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3895]
བར་མ་ནི་རྣམ་པར་གཞག་པ་སྟེ། འདི་མི་རིགས་པ་མ་ཡིན་ཏེ། བརྗོད་པ་ལ་དཔེ་གཉིས་ཀྱི་ཕྱིར་ཞེས་བྱའོ། །

[Block 3896]
སྒོ་གླེགས་སྒྲ་མི་འབྱུང་བ་དང་དྲང་བའི་ཐབས་ཀྱང་ཞེས་བྱ་བ་ནི་བརྩིག་པར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འོག་ནས་སྒོ་ཁང་བྱའོ་ཞེས་འབྱུང་བ་ཡན་ཆད་ཀུན་ལ་འདི་རྗེས་སུ་སྦྱར་རོ། །

[Block 3897]
དེའི་དང་པོ་བྱས་ནས་བརྩིག་པར་བྱའོ་ཞེས་བྱ་བའི་སྒྲས་བཤད་པ་འདི་བྱས་པ་ཞེས་བྱ་བ་དེ་ཙམ་ཞིག་འདིར་བརྗོད་པའོ། །

[Block 3898]
འདིར་འདོད་པས་འཇུག་པ་ན། གལ་ཏེ་ཕོངས་པ་མ་ཡིན་པའི་དོན་ལ་འཇུག་ན་གལ་ཏེ་མ་ཡིན་ན་ཇི་ལྟར་མངོན་པར་འདོད་པས་འཇུག་པར་བྱའོ། །

[Block 3899]
འདིས་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྒོ་གདོད་པར་བྱའོ། །

[Block 3900]
དགེ་སློང་དག་སྒོ་གླེགས་མི་འཇུད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྒོ་གླེགས་གཞུག་པར་བྱའོ། །

[Block 3901]
བཅད་དཀའ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། འཕགས་པ་དག་ལག་གཟུངས་གདབ་པར་བྱའོ། །

[Block 3902]
སྒྲ་འཁྲོལ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། འོག་ཏུ་ཀོ་བའི་དུམ་བུ་གཞུག་པར་བྱའོ། །

[Block 3903]
དབྱེ་དཀའ་ན༌[^2682]བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། འཕགས་པ་དག་ལག་གཟུངས་གདབ་པར་བྱའོ། །

[Block 3904]
དབྱེ་བ༌[^2683]ན་སྒྲ་ཁྲིག༌[^2684]ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རས་མས་དཀྲི་བར་བྱའོ་ཞེས་བྱ་བ་གསུངས་པ་དེ་རྣམས་བསྡུས་པ་ཡིན་ནོ། །

[Block 3905]
དེ་ལ་སྒྲ་མི་འབྱུང་བའི་ཐབས་ཞེས་བྱ་བ་ནི་འོག་ཏུ་ཀོ་བའི་དུམ་བུ་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་དང་། རས་མས་དཀྲི་བར་བྱའོ་ཞེས་གསུངས་པ་དེ་རྣམས་བསྡུས་པ་ཡིན་ནོ། །

[Block 3906]
དྲང་བའི་ཐབས་ཞེས་བྱ་བ་ནི་ཕྱི་ནང་གཉིས་ནས་ལག་གཟུངས་གདབ་པར༌[^2685]བྱའོ་ཞེས་གསུངས་པ་བསྡུས་པ་ཡིན་ནོ། །

[Block 3907]
གོང་དུ་སུམ་ཆ་བོར་བར་སྐར་ཁུང་ཕྱི་རུབ་ལ་ནང་ཡངས་པ་ཡང་བཟང་ངོ་ཞེས་བྱ་བ་ལ། གོང་དུ་ཞེས་བྱ་བ་ནི་རྩིག་ངོས་ཀྱི་གོང་གི་སུམ་ཆ་བོར་ཞིང་སུམ་གཉིས་ལུས་པའི་ཕྱོགས་གང་ཡང་རུང་བ་དེར་སྐར་ཁུང་བཏོད༌[^2686]ན་བཟང་སྟེ། དམས་ན་ནི་ཆོམ་རྐུན་པ་དང་། གཡོན་ཅན་དང་སེང་གེ་ལ་སོགས་པས་འཛུལ་བའི་ཕྱིར་རོ། །

[Block 3908]
མཐོས་ན་ནི་སྣང་བ་གསལ་བར་མི་འགྱུར་རོ། །

[Block 3909]
གོང་དུ་སུམ་ཆ་བོར་བ་ལ་སོགས་པའི་དོན་དུ་འདི་བྱས་སོ། །

[Block 3910]
དེ་ཉིད་ནི་འཇིག་རྟེན་པ་ལ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 3911]
དྲ་བ་དང་། སྒོ་གླེགས་དང་། འཕྲེད་གཏན་དང་། གནམ་གཟེར་དང་། འཁོར་གཏན་དང་། དབྱུག་གུ་སྐམ་ཁ་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས༌[^2687]བྱ་བར་སྦྱར་རོ། །

[Block 3912]
འདིས་ནི་ཁྲ་དང་། མཆིལ་པ་དང་། ཕོ་རོག་དག་འཇུག་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྐར་ཁུང་དྲ་བ་ཅན་དུའོ།[^2688] །

[Block 3913]
སྦྲང་བུ་ཏྲྱཻ་མ་བུ་ག་དང་། ཏྲྱེ༌[^2689]ལ་ཀ་དག་འཇུག་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྒོ་གླེགས་གཞུག་པར་བྱའོ། །

[Block 3914]
རླུང་གིས༌[^2690]ཕྱེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། འཕྲེད༌[^2691]གཏན་གཞུག་པར་བྱའོ། །

[Block 3915]
བཅད་དཀའ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གནམ༌[^2692]གཟེར་དང་འཁོར་གཏན་གཞུག་པར་བྱའོ། །

[Block 3916]
དབྱེ་དཀའ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དབྱུ་གུ་སྐམ་ཁ་ཉེ་བར་གཞག་པར་བྱའོ༌[^2693]ཞེས་གསུངས་པ་དེ་འདིར་བསྡུས་པ་ཡིན་ནོ།[^2694] །དྲ་བ་དང་ཞེས་བྱ་བ་ནི་བུ་ག་པ༌[^2695]ཕྲ་མོ་བསྟན་པའི་དོན་དུ་ཅན་གྱི་སྒྲ་སྦྱར་རོ། །

[Block 3917]
མི་ཤོང་ན་སྟེང་དུ་ཁང་མོ་ཆེ་བྱའོ།[^2696]

[Block 3918]
།ཡང་ན་ཡང་ཐོག་གོ་ཞེས་བྱ་བ་ལས།

[Block 3919]
ཁང་མོ་ཆེ་ཞེས་བྱ་བ་ནི། སྤོང་ཁང་རྣམས་ཀྱི༌[^2697]སྟེང་དུའོ། །

[Block 3920]
གལ་ཏེ་སྤོང་ཁང་ལ་སྤོང་ཁང་རྣམས་ཀྱི་ཚད༌[^2698]དུ་མི་འགྱུར་ན་སྟེང་དུ་ཁང་པ་མི་བྱ་སྟེ། ཁང་པ་གཞན་ལས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3921]
གཞུང་ཁ་ཅིག་ལས་དེ་དག་དེར་མི་ཤོང་ནས་སྟེང་དུ་རིམ་ཁང་གཉིས་པ་བྱའོ་ཞེས་གསུངས་པ་དང་། དེ་གཉིས་ཀ་ཡང་འགལ་བ་མེད་པས་མདོ་འདིར་བསྡུས་པའོ། །

[Block 3922]
འཛེག་པའི་ཕྱིར་ཐེམ༌[^2699]སྐས་སོ་ཞེས་བྱ་བ་ནི། བྱའོ་ཞེས་བྱ་བར༌[^2700]སྦྱར་ཏེ་འཛེག་པའི་ཕྱིར་དེར་ཐེམ༌[^2701]སྐས་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3923]
མི་ལྟུང་བར་བྱ་བའི་ཕྱིར་ཁ་ཁྱེར་གྱིས་བསྐོར་བར་བྱའོ། །

[Block 3924]
དེ་མི་འགུལ་བར་བྱ་བའི་ཕྱིར་ལྕགས་ཀྱི་གཟེར་བུ་དག་གིས་གདབ་བོ་ཞེས་བྱ་བ་ནི། དེ་རྣམས་ཀྱིས་ནི་ཁ་ཁྱེར་དེ་དག་ལ༌[^2702]འཛེག་དཀའ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཐེམ༌[^2703]སྐས་བྱའོ། །

[Block 3925]
ལྟུང་བར་གྱུར་ནས། [^2704]ཁ་ཁྱེར་གྱིས༌[^2705]བསྐོར་བར་བྱའོ། །
--- END BLOCKS ---
