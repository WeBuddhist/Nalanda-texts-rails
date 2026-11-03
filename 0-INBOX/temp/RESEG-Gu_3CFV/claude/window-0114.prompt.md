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
དེའི་གནས་ནི་ཁང་སྟེང་ངོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་གཎྜཱི་བརྡུང་བ་དེའི་གནས་དེའོ། །

[Block 3992]
གང་དང་གང་དུ་དེ་དང་དེ་བརྗོད་པ་དེར་འདི་གནས་པར་རྟོགས་པར་བྱ་སྟེ། དེ་བས་ན་འདིས༌[^2758]བྱས་པའོ། །

[Block 3993]
དེའི་ཁང་སྟེང་དུ་སྒྲུབ་པ་ལ་མཆོག །དེ་བས་ན་གཞན་ཁང་སྟེང་གི་རྣམ་པ་མ་ཡིན་ཏེ། འདིར་དེའི་གནས་སུ་གཏོགས་པའི་གནས་དེ་དང་དེར་ཁང་ཐོག་ཏུ་འཛེགས་ནས་བཀླག་པར༌[^2759]བྱའོ་ཞེས་བྱུང་བ་ཡིན་ཏེ། དེ་བས་ན་མདོ་འདིའོ། །

[Block 3994]
དེ་སྒྲུབ་པར་བྱེད་པས༌[^2760]ནི་མ་ཡིན་ཞེས་བྱ་བ་འདོན་པས་མེད་པར་ཤེས་པར་བྱ་བ་སྟེ། དགོངས་པ་མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3995]
དགེ་འདུན་བསྡུ་བའི་ཕྱིར་ནི་རྒྱུད་གསུམ་དང་དེ་སྙེད་ཀྱི་ཏོག༌[^2761]དག་གོ་ཞེས་བྱ་བ་ནི་ལན་གསུམ་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3996]
ལས་བྱ་བའི་དོན་དུ་གཎྜཱི་བརྡུང་བ་ལ་ནི་རྒྱུད་གཅིག་དང་། ཏོག་གསུམ་བརྡུང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3997]
ཁ་ཅིག་ལས་རྒྱུད་གསུམ་དང་ཏོག༌[^2762]གཉིས་སོ་ཞེས་བྱ་བ་ལུགས་གཅིག་ལས།

[Block 3998]
ལས་བྱ་བའི་དོན་དུ་གཎྜཱི་བརྡུང་བ་ལ་ནི། རྒྱུད་གསུམ་དང་ཏོག་གཉིས་ཞེས་ཀྱང་འབྱུང་སྟེ། འདི་ནི་ཏོག་གི་སྒྲས་བརྗོད་པའོ། །

[Block 3999]
ཁ་ཅིག་ཅེས་བྱ་བ་ནི༌[^2763]འདོད་པའོ། །

[Block 4000]
ལས་བྱ་བའི་དོན་དུ༌[^2764]ཁ་ཅིག་གི་འདོད་པ་འདི་ཞེས་བྱ་བའི་དོན་དུའོ། །

[Block 4001]
ཤི་བ་ལ་ཕྲག་པ་དབྱུང་བའི་དོན་དུ་ནི་བྱི་བོའོ༌[^2765]ཞེས་བྱ་བ་ནི། གཎྜཱི་བརྡུང་བ་ནི་བྱི་བོ་སྟེ། བྱི་བོ་ཞེས་བྱ་བ་ནི་རྒྱུད་ཉེ་ཚེ༌[^2766]སྟེ་ཏོག་དང་བྲལ་ལོ། །

[Block 4002]
ཁ་ཅིག་ལས་ནི་རྒྱུད་གཅིག་དང་ཏོག༌[^2767]གཅིག་གོ་ཞེས་བྱ་བ་ནི་ལུགས་ཁ་ཅིག་ལས་ཏེ་འདོད་པ་གཞན་ཉེ་བར་བཀོད་པའོ། །

[Block 4003]
སྤོང་བ་པའི་དོན་དུ་ནི་ཁར་གསིལ༌[^2768]ལོ་ཞེས་བྱ་བ་ནི། དེས་གཎྜཱི་བྱ་བའི་དོན་ཏོ། །

[Block 4004]
ཁ་ཅིག་ལས་གཎྜཱི་ཆུང་ངུ་ཞེའོ་ཞེས་བྱ་བ་ནི། ཀློག་པར་བྱེད་པའི་རྟོགས་པས་མངོན་པར་འབྲེལ་པ་ཕོའི་རྟགས་འདི་བསྟན་ཏོ།[^2769] །འདི་དག་གི་དོན་གཅིག་ཁོ་ན་ཞེས་བྱ་སྟེ། དེ་བས༌[^2770]ན་འདི་བསྟན་པ་ཁར་གསིལ༌[^2771]ཉིད་གཎྜཱི་ཆུང་ངུ་ཞེས་བྱ་བ་བརྗོད་དོ། །

[Block 4005]
གནོད་པ་བྱུང་བ་ལ་ནི་ཇི་ཙམ་གྱིས་ཆོག་པའོ་ཞེས་བྱ་བ་ནི། གནོད་པ་བྱུང་བའི་ཚེ་གཎྜཱི་བརྡུང་བ་ལ་ནི་ཇི་ཙམ་གྱིས་ཆོག་པ་དེ་ཙམ་བརྡུང་བར་བྱ་སྟེ། ནམ་ཞི་བར་གྱུར་གྱི་བར་དུ་བརྡུང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4006]
ཟན་གྱི་ཕྱིར་འདུ་བའི་དོན་དུ་ནི་གཎྜཱི་དང་། གཎྜཱི་ཆུང་ངུ་གཉིས་ཀ་བརྡུང་ངོ་ཞེས་བྱ་བ་ནི།

[Block 4007 [VERSE]]
ཟན་གྱི་ཕྱིར་འདུ་བའི༌[^2772]གང་ཡིན་པ་དེའི་དོན་དུའོ། །
ཅི་རྒྱུན་མ་ཆད་པར་བརྡུང་བར་བྱའམ༌[^2773]ཞེ་ན།
དེའི་ཕྱིར་རབ་ཏུ་གཅད༌[^2774]དེའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4008]
ཅི་ཙམ་གྱིས་བར་དུ་གཅོད་ཅེ་ན། དེའི་ཕྱིར་བརྐྱང་བས་སོ་ཞེས་བྱ་བ༌[^2775]སྨོས་ཏེ། དུས་ཅི་ཙམ་གྱིས་འགྲུབ་པར་འགྱུར་བའི་དུས་དེ་ཙམ་གྱི་བར་དུ་གཎྜཱི་ཆུང་ངུ་བརྐྱང་པས་བརྡུང་བར་བྱའོ། །

[Block 4009]
དེ་བས་ན་ཤིན་ཏུ་ཆུང༌[^2776]བར་འདི་ལས་བསྟན༌[^2777]པར་མི་བྱའོ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 4010]
འདུས་པ་ཆེན་པོའི་ཚེ་གཎྜཱི་བརྡུངས་པས་གོ་བར་མི་འགྱུར་བ་བལྟ་ན་དུང་སྦྲེལ༌[^2778]ཏེ། བུད་པར་བྱའོ། །

[Block 4011]
རྔ་བོ་ཆེ་བརྡུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི། གླེང་གཞི་དག་ལས་དེ་རྣམ༌[^2779]པའི་དོན་དུ་ཟན་གྱི་ཕྱིར་འདུ་བའི་དོན་དུ་ཞེས་བྱ་བ་ནི་དཔེ་ཙམ་དུ་རིག་པར་བྱ་སྟེ། གཞན་དུ་ཡང་འདི་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 4012]
གཎྜཱི་བརྡུངས་པར་མི་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཅི་ཡང་རུང་བ་བླངས་པའོ། །

[Block 4013]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ༌[^2780]པ། རྣམ་པར་འབྱེད་པ་ལ་སོགས་པ་ལ་གཎྜཱིའི་ཕྱིར་མྱུར་བ་ཁོ་ནར་འགྲོ་བར་བྱའོ༌[^2781]ཞེས་བྱ་བའི་ཚིག་གནང་ངོ་། །གཎྜཱི་བརྡུངས་པར་སོ་སོར་ཉེ་བར་གནས་པའི་ཕྱིར་སྦྲན་པ་ཡིན་པས་དེའི་ཕྱིར་དོན༌[^2782]ཅི་ཞིག་བྱུང་ཞེས་ངེས་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་དེར་འགྲོ་བར་བྱའོ། །

[Block 4014]
འདིར་འགྲོ་བ་ནི་བྱ་བ་སྟེ་དོན་སྒྲུབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 4015]
འདི་ལ་དགོས༌[^2783]པའི་དབང་ཉིད་ཀྱི་ཕྱིར་འོས་པ་ལ་ལྟོས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4016]
མི་མྱུར་བར༌[^2784]མི་བྱའོ་ཞེས་བྱ་བ་ནི། གཎྜཱིའི་ཕྱིར་མྱུར་བ་ཁོ་ནར་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་ཏེ་འདི་ནི་མ་མོ་ལས་སོ། །

[Block 4017]
བྱ་བ་འགྲུབ་པའི་དུས་ཀྱི་ལྷག་མ་ལུས་ཙམ་ན་རྒྱུན་ཆགས་གསུམ་པ་གདོན་ཅིང་ཅི་བདེར་བྱའོ་ཞེས་བྱ་བ་ནི། [^2785]རྒྱུན་ཆགས་གསུམ་པ་གདོན་པ་ལ་དུས་ཇི་ཙམ་གྱིས་དགེ་སློང་སྤོང་བ་པ་དག་གིས་མཆོད་རྟེན་ལ་ཕྱག་བྱ་བ་ལ་སོགས་པའི་བྱ་བ་གྲུབ་པའི་དུས་ཀྱི་ལྷག་མ་དེ་ཙམ་ལུས་པ་ནི། རྒྱུན་ཆགས་གསུམ་པ་འདོན་པ་སྤོང་བ་པ་དག་ཅི་བདེར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4018]
དེ་རན་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་རྒྱུན་ཆགས་གསུམ་པའོ། །

[Block 4019]
ཡོན་བཤད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། རྒྱུན་ཆགས་གསུམ་བཏོན་པའི་འོག་ཏུ་སྦྱིན་པའི་ཕན་ཡོན་བཤད་པར་བྱའོ། །

[Block 4020]
དེ་ཡང་ཇི་ལྟར་བྱ་ཞེ་ན། དེའི་ཕྱིར་རན་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕྱི་དྲོ་མཚན་མོའི་མཇུག་ཏུ་རང༌[^2786]གི་གནས་སུ་འགྲོ་བར་མངོན་པར་ཕྱོགས་པ་རྣམས་ལ་དེ་རིགས་པར་གྱུར་པ་མཐོང་བ་ཡིན་ནོ། །

[Block 4021]
སྤོང་བ་པའི་ཞལ་ཏ་པས་སྔར་འདུ་ཞིང་མཇུག་ཏུ་འགྱེད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། སྤོང་བའི་ཞལ་ཏ་བྱེད་པས་གང་དེ་རྣམས་ཀྱིས་སོ། །

[Block 4022]
གལ་ཏེ་རྐྱེན་དེ་ལྟ་བུ༌[^2787]བྱུང་ན་ལྡེ་མིག་སྦས་པ་བསྟན་པར་བྱའོ་ཞེས་བྱ་བ་ལ། གལ་ཏེ་དེ་ལྟ་བུ་ཞེས་བྱ་བ་ནི། དོན་གལ་པོ་ཆེའི་དབང་གིས་མ་གྲུབ་པས་ལྡེ་མིག་གང་དུ་སྦས་པ་དེ་བསྟན་པར་བྱའོ་ཞེས་བྱ་བ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 4023]
གལ་ཏེ་སྔར་ལྡེ་མིག་འགའ་ཞིག་གི་ལག་ཏུ་གཞག་གམ། ཕྱོགས་འགའ་ཞིག་ཏུ་སྦས་ནས། སྔར་འགྲོ༌[^2788]མི་ཁོམ་པ་དེ་ལྟ་བུའི་རྐྱེན་དག་བྱུང་ན། སྦེད་པ་པོ་འགྲོ་བའི་ཕྱིར་གནས་སྐབས་བདེ་བླག་ཏུ་བྱེད་པར་མི་ནུས་ན། དེའི་ཕྱིར་གལ་ཏེ་དེ་ལས་སྤོང་བ་པ༌[^2789]གཞན་དག་མི༌[^2790]སྣང་ན་སྨྲ་བར་བྱ་བའི་དོན་ཏོ། །

[Block 4024]
འདིར་གཞུང་ཐམས་ཅད་ཀྱི་སྔོན་དུ་འོང་བར་བྱའོ། །

[Block 4025]
གལ་ཏེ་དེ་ལྟ་བུའི་རྐྱེན་དག་བྱུང་ན་ལྡེ་མིག་སྦ་བར་བྱ་བ་བརྗོད་པར་བྱ་སྟེ་བསྟན་པར་བྱའོ། །

[Block 4026]
ཚེ་དང་ལྡན་པས་ཕྱོགས་འདི་ན་ལྡེ་མིག་སྦས་པ་བལྟས་ནས་དབྱུང་བར་བྱའོ། །

[Block 4027]
གསོ་སྦྱོང་གི་གཞི་ལས་ཞི་གནས་ཀྱི་གསོ་སྦྱོང་གི་སྐབས་སོ། །

[Block 4028]
གསོ་སྦྱོང་གི་གནས་ལ་བློ་མཐུན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ནས། གནས་ཇི་ལྟ་བུར༌[^2791]བློ་མཐུན་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གནས་ཐམས་ཅད་གྲུབ་པའམ། བྱས་པའམ་ཟིན་པ་ལའོ་ཞེས་བྱ་བ༌[^2792]སྨོས་ཏེ། གནས་གང་ལ་ཐམས་ཅད་གྲུབ་པའམ། ཐམས་ཅད་བྱས༌[^2793]པའམ། ཐམས་ཅད་ཟིན་པ་ཡོད་པ་དེ་ནི་གང་ལ་ཞེས་བྱ་བ་འདིས་བསྡུས་པའོ། །

[Block 4029]
དེ་ལ་གྲུབ་པ་ཞེས་བྱ་བ་ནི་འཆགས་པའི་བསྐལ་པ༌[^2794]ཚེ་རང་གྲུབ་པའམ། གཏིབ་ཆད་པ་ལ་སོགས་པས་རང་གྲུབ་པ་སྟེ། དཔེར་ན་རིའི་བྱ་སྐྱིབས་ལ་སོགས་པ་ལྟ་བུ་གཞན་གྱིས་བྱས་པ་ལ་མི་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 4030]
བྱས་པ་ཞེས་བྱ་བ་ནི་འབད་པ་ལ་བརྟེན་ནས། བསྒྲུབ་པ་གང་ཡིན་པའོ། །
--- END BLOCKS ---
