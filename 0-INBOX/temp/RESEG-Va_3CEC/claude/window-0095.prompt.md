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
[Block 3326]
མི་གཡེང་བ་ནི་གཡེང་བ་མེད་པའོ། །

[Block 3327]
གཞན་གྱི་དྲིང༌[^2868]མི་འཇོག་པར་ཤེས་པ་ནི་གཞན་ལ་བརྟེན༌[^2869]མི་དགོས་པར་ཤེས་པའོ། །

[Block 3328]
རབ་ཏུ་རྣམ་པར་འབྱེད་པར༌[^2870]ཤེས་པ་ནི་མི་ཟད་པ་རྣམས་ཀྱི་མཚན་ཉིད་སོ་སོར༌[^2871]མ་འདྲེས་པར་དབྱེ་བ་ཤེས་པའོ། །

[Block 3329]
སངས་རྒྱས་ཀྱི་ཆོས་ནི་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པའོ། །

[Block 3330]
རྒྱ་ཞེས་བྱ་བ་ནི་ས་བཅུར་འདྲེན་པར༌[^2872]བྱེད་པའི་གཞི༌[^2873]དང་རྟེན་ཡིན་ཏེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3331]
རྒྱ་འདི་ལ་ཡང་དག་པར་གཞོལ་བ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་རྣམ་གྲངས་འདི་བསྒྲུབས༌[^2874]ན་ཆོས་ཀྱི་རྣམ་གྲངས་ཐམས་ཅད་སྒྲུབ་པ༌[^2875]ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3332]
ཆོས་ཀྱི༌[^2876]བསྲུང་བ་བགྱི་ཞེས་བྱ་བ་ནི་ཆོས་འཆད་པ་ལ་བར་ཆད་མེད་པར་བསྲུང་བའོ། །

[Block 3333]
སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་བཟུང་བར་འགྱུར་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་བཏགས་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3334]
སྟོབས་ནི་བདུད་ཀྱི་འཁོར་གྱི་གཡོག་རྣམས་སོ། །

[Block 3335]
བསྲུང་བ་དང་བསྐྱབ་པ༌[^2877]དང་སྦ་བ་ནི་མི་དགེ་བའི་ལས་རྣམ་པ་གསུམ་ལས་སོ། །

[Block 3336]
དེ་ལ་མཐོང་བའི་ཆོས་ལ་མྱོང་བའི་ལས་ལས་ནི་བསྲུང་བའོ། །

[Block 3337]
སྐྱེས་ནས་མྱོང་བའི་ལས་ལས༌[^2878]ནི་བསྐྱབ༌[^2879]པའོ། །

[Block 3338]
ཚེ་རབས་གཞན་དུ་མྱོང་བའི་ལས་ལས་ནི་སྦ་བའོ། །

[Block 3339]
ཡང་ན་གནོད་པ་གཉིས༌[^2880]འབྱུང་སྟེ། རང་གི་རྐྱེན་ལས་འབྱུང་བ་དང་། གཞན་གྱི་རྐྱེན་ལས་འབྱུང་བའོ། །

[Block 3340]
གཞན་གྱི་རྐྱེན་ལས་འབྱུང་བ་ཡང་རྣམ་པ་གཉིས་ཏེ། སེམས་ཅན་མ་ཡིན་པའི་གྲངས་ཀྱི་རྐྱེན་ལས་འབྱུང་བ་དང་། སེམས་ཅན་གྱི་གྲངས་ཀྱི་རྐྱེན་ལས་འབྱུང་བའོ། །

[Block 3341]
[^2881]བདག་གི་ལས་ཀྱི་རྐྱེན་ལས་འབྱུང་བ་ལས་ནི་བསྲུང་བའོ། །

[Block 3342]
སེམས་ཅན་མ་ཡིན་པའི་གྲངས་ཀྱི་གནོད་པ་རླུང་དང་ཚ་བ་ལ་སོགས་པ་ལས་ནི་བསྐྱབ་པའོ། །

[Block 3343]
སེམས་ཅན་གྱི་གྲངས༌[^2882]ཀྱི་གནོད་པ་བརྡེག་པ་དང་བཅིང་བ་ལ་སོགས་པ་ལས་ནི་སྦ་བའོ། །

[Block 3344]
སྙིང་ལས་ཆུང་ངུར་གྱིས་ཤིག་ཅེས་བྱ་བ་ནི་རྒྱས་པར་རྣམ་པར་དབྱེ་བའི་སྒོ་ནས་ཁྱོད་འབད་མི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3345]
དམ་པའི་ཆོས་བཟུང་བ༌[^2883]འཇིག་རྟེན་དུ་རིང་དུ༌[^2884]གནས་ཤིང་མི་ནུབ་པར༌[^2885]བྱའོ། །

[Block 3346]
སླད་མའི་དུས་ལྔ་བརྒྱ་ཐ་མ་ལ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་ཆོས་འཕེལ་བ་དང་། འགྲིབ་པའི་ཚུལ་བསྟན་པའི་ཕྱིར་དུས་ཀྱི་ཁྱད་པར་བརྗོད་པའོ། །

[Block 3347]
དེ་ཡང་དཔེར་ན་མིའི་ཚེ་ལོ་བརྒྱ་ཐུབ་པ་ལ་ལོ་ལྔ་བཅུའི་བར་དུ་ནི་འཕེལ་བའི་དུས་ཏེ། ལུས་དང་། ཤེས་རབ་དང་། རྩལ་ལ་སོགས་པ་འཕེལ་ཞིང་སྐྱེ་བའོ། །

[Block 3348]
དེ་ལྟར་ལོ་ལྔ་བཅུ་འདས་ནས་དེའི་ཕྱི་མའི་ལྔ་བཅུ་ནི་འགྲིབ་པའི་དུས་ཏེ། ལུས་དང་། ཤེས་རབ་དང་། རྩལ་ལ་སོགས་པ༌[^2886]ཤིན་ཏུ་ཉམས་ཤིང་བྲི་ནས་ཐ་མར་རྒ་ཤི་ལ་ཐུག་སྟེ་ཟད་པར་འགྱུར་རོ། །

[Block 3349]
དེ་བཞིན་དུ་སངས་རྒྱས་ཤཱཀྱ་ཐུབ་པའི་བསྟན་པ་ལ༌[^2887]འབྲས་བུ་ཐོབ་པ་དང་། ཤིན་ཏུ་རྒྱས་པའི་དུས་ནི་ལོ་སྟོང་ཤིག་འཛམ་བུའི་གླིང་ན་གནས་སོ། །

[Block 3350]
དེའི་ཕྱེད་དུ་བགོས་ཏེ་ལྔ་བརྒྱ་སྔ་མ་ནི་འཕེལ་བའི་དུས་སུ་གཞག་ལ། ལྔ་བརྒྱ་ཕྱི་མ་ནི་འགྲིབ་པའི་དུས་སུ་གཞག་གོ། །

[Block 3351]
འཕེལ་བ་ནི་ལོ་བརྒྱད་ཅུའི་བར་དུ་ཤཱཀྱ་ཐུབ་པ་མྱ་ངན་ལས་མ་འདས་ཏེ།[^2888] དེའི་དུས་སུ་བྱང་ཆུབ་སེམས་དཔའ་དང་། ཉན་ཐོས་ལ་སོགས་པ་འཕགས་པ་ཕྱོགས་བཅུ་ནས་དགེ་བའི་རྩ་བ་སྨིན་ཏེ་ལྷག་མ་རྣམས་ཀྱང་ཤིན་ཏུ་ལྷག་པར་རྣམ་པར་གྲོལ། གཞན་ལྷ་དང་མི་ལ་སོགས་པ་ཡང་དེ་བཞིན་གཤེགས་པ་ཉིད་ཀྱིས་བཀའ༌[^2889]བསྟན་ཅིང་མངོན་སུམ་དུ༌[^2890]ཡོངས་སུ་སྨིན་ཏེ། ཡོངས་སུ་བཀྲོལ་བས་ལྷག་པར་འབྲས་བུ་འཐོབ་པོ། །དེ་ནས་སངས་རྒྱས་མྱ་ངན་ལས་འདས་ནས་ཀྱང༌[^2891]ལོ་ལྔ་བརྒྱ་སྔ་མ༌[^2892]འདས་ཀྱི་བར་དུ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དང་། ཉན་ཐོས་ཆེན་པོ་དག་སངས་རྒྱས་ཀྱི་བསྟན་པ་རྣམས་ཤིན་ཏུ་འཛིན་ཅིང་འཛམ་བུའི་གླིང་ན་ཁྱབ་པར་གྲངས་མང་དུ་གནས་ཏེ། དེ་དག་གིས་ཀྱང་ལྷ་དང་མི་ལ་སོགས་པ་ཤིན་ཏུ་ཚད་མེད་པ་ཡོངས་སུ་སྨིན་པ་དང་། ཡོངས་སུ་གྲོལ་བར་བྱས་ཏེ་འབྲས་བུ་ཐོབ་པར་གྱུར་ཏོ། །

[Block 3352]
དཔེར་ན་དུས་དེའི་ཚེ་ན་གཏམ་དུ་བརྗོད་པ། འཕགས་པ་ཉན་ཐོས་ཨུ་པ་གུཔྟ་ཞེས་བྱ་བ་ཞིག་གིས་ཀྱང་སངས་རྒྱས་ཀྱི་བསྟན་པ་བཟུང་ནས་སེམས་ཅན་གྲངས་མེད་པ་བསྒྲལ་ཏེ། ཇི་སྙེད་ཅིག༌[^2893]བསྒྲལ་བ་དེ་དག་བྱང་བུ་ལ་བྲིས་ཏེ༌[^2894]བསགས་པས་རང་གི་ཁང་པ་གང་ངོ་ཞེས་བྱ་བ་དང་། དགེ་སློང་དེས་བདུད་ཀྱང་བཏུལ་ཏེ་དེ༌[^2895]དགེ་སློང་དེ༌[^2896]དུས་གཞན་ཞིག་ན། བསམ་གཏན་བྱེད་པའི་ཚེ་དེའི་ཐད་དུ་བདུད་ཅིག་འོངས་པས་མ་ཚོར་བར་མགོ་ལ་མེ་ཏོག་གི་ཕྲེང་བ་གཞག་གོ། །

[Block 3353]
དེ་ནས་དགེ་སློང་དེས་ཀྱང་ཚོར་ཏེ་བདུད་དེ་ལ་གདུལ་བའི་སྐབས་སྣང་ངོ་སྙམ་ནས། ཁྱི་རོ་འབུ་ཅན་ཞིག་ཏུ་སྤྲུལ་ཏེ་བདུད་ཀྱི་ལུས་ལ་སེ་མོ་དོར་བཏགས༌[^2897]ནས། བདུད་ཀྱིས་དོར་དུ་མི་ནུས་པར་བྱིན་གྱིས་བརླབས་སོ། །

[Block 3354]
དེ་ནས་བདུད་དེ་རང་གིས༌[^2898]དོར་མ༌[^2899]ནུས་ནས། བརྒྱ་བྱིན་གྱི་ཐད་དུ་ཕྱིན་ཏེ་གསོལ་བ་བཏབ་ན་དེས་ཀྱང་གྲོགས་མ་བྱས་སོ། །

[Block 3355]
དེ་ཚངས་པའི་ཐད་དུ་ཕྱིན་ཏེ། གསོལ་བ་བཏབ་ན་ཡང་ཚངས་པས་ཀྱང་མ་བཀྲོལ་ཏེ། ཐ་མ་དགེ་སློང་གི་མགོ་ལ་མེ་ཏོག་བཞག་པས་ཉེས་སོ་ཞེས་དགེ་སློང་གི་ཐོག་ཏུ༌[^2900]བཏང་ངོ་། །དེ་ནས་དགེ་སློང་ལ་ཕྱག་འཚལ་ཏེ་གསོལ་བ་བཏབ་ནས་དགེ་སློང་ཨུ་པ་གུཔྟ་སྔོན་སངས་རྒྱས་མ་མཐོང་བ་དེ་བདུད་ཀྱིས་སངས་རྒྱས་མཚན་དང་ལྡན་པ་ཉན་ཐོས་ཀྱི་འཁོར་དང་བཅས་པ་ཅིག་སྤྲུལ་ཏེ་བསྟན་ན་ཁྱི་རོ་དགྲོལ་བར་དམ་བཅས་ཏེ་ཁྱི་རོ་བཀྲོལ་ནས་སངས་རྒྱས་འཁོར་དང་བཅས་པར་སྤྲུལ་ནས་བསྟན་ཏོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 3356]
དེ་བས་ན་ལྔ་བརྒྱ་སྔ་མ་ནི་དུས་བཟང་པོ་སྟེ་དུས་དེ་ལ་ལྟོས༌[^2901]ནས་ཁྱད་པར༌[^2902]སྨྲས་པ་ནི་ལྔ་བརྒྱ་ཕྱི་མ་ཞེས་བྱའོ། །

[Block 3357]
དེ་ལྟ་མོད་ཀྱི་ལྔ་བརྒྱ་ཕྱི་མའི་དུས་དེ་ན་ཡང་ལོ་ལྔ་བརྒྱའི་བར་དུ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དང་ཉན་ཐོས་ལ་སོགས་པ་འཕགས་པ་གྲངས་མང་དུ༌[^2903]འཛམ་བུའི་གླིང་ན་གནས་ཏེ། དེ་དག་གིས་ཀྱང་ལྷ་དང་མི་ལ་སོགས་པ་ཤིན་ཏུ་ཚད་མེད་པ་ཡོངས་སུ་སྨིན་པ་དང་། ཡོངས་སུ་བཀྲོལ༌[^2904]ཏེ་འབྲས་བུ་ཐོབ་པར་བྱས་སོ། །

[Block 3358]
དེ་ལྟར་འབྲས་བུ་ཐོབ་པ་ལ་སོགས་པར་གྱུར་ཀྱང་། ལྔ་བརྒྱ་སྔ་མ་དང་སྦྱར་ན་དེའི་དུས་ངན་པའི་ཕྱིར་ལྔ་བརྒྱ་ཕྱི་མ་ཞེས་སྨོས་ཏེ། ལྔ་བརྒྱ་ཕྱི་མའི་མགོ་ནས་སངས་རྒྱས་ཀྱི་ཆོས་ནམ་འཛམ་བུའི་གླིང་ན་མེད་པར་མ་གྱུར་གྱི་བར་དུ་ལྔ་བརྒྱ་ཕྱི་མ་ཞེས་བྱ་བའི་དུས་སུ་བསྡུའོ། །

[Block 3359]
ལྔ་བརྒྱ་ཕྱི་མའི་དང་པོ་ཚུན་ཆད༌[^2905]དུས་ངན་པར་གཞག་མོད་ཀྱི། འོན་ཀྱང་ལོ་ལྔ་བརྒྱའི་བར་དུ་ནི་དུས་ངན་པའི་ནང་ནས་ཀྱང་འབྲས་བུ་ཐོབ་པ་ནི༌[^2906]ཤིན་ཏུ་མི་དཀའ་བའི་ཕྱིར། དུས་ངན་པའི་ཡང་ངན་པ་ཁྱད་པར་དུ་སྨོས་པའོ། །

[Block 3360]
ལྔ་བརྒྱ་ཕྱི་མའི་ལོ་འདས་ཕྱིན་ཆད་ནས་ཆོས་མེད་ཀྱི་བར་དུ་དུས་ངན་པའི་ཡང་ངན་པར་གཞག་མོད་ཀྱི། དེའི་ཚེ་ན་ཡང་བརྩོན་འགྲུས་དང་ནན་ཏན་བྱས་ནས་འབྲས་བུ་མི་ཐོབ་པ༌[^2907]ཡང་མ་ཡིན། བྱང་ཆུབ་སེམས་དཔའ་དང་། ཉན་ཐོས་འགའ་ཙམ་འཇིག་རྟེན་དུ་མི་འབྱུང་བ་ཡང་མ་ཡིན་ནོ། །

[Block 3361]
བདག་བློ་ཞན་པས་ཞེས་བྱ་བ་ནི་བདག་གི་ཤེས་རབ་དང་ཡེ་ཤེས་ཆུང་བས༌[^2908]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3362]
འགོག་པ་ལ་ཡང་འཁྲུལ་པ་མེད་ཅེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་དུ་སྟོན་པ་ལ་ཡང་འཁྲུལ་བ་མེད་པའོ། །

[Block 3363]
རྟོགས་པ་ཁོང་དུ་ཆུད་ཅིང་ཞེས༌[^2909]བྱ་བ་ནི་ཕྱིན་ཅི་མ་ལོག་པར་ཁོང་དུ་ཆུད་པའོ། །

[Block 3364]
ཡང་དག་པའི་དོན་རྣམ་པར་ངེས་པ་ཐོབ་པ་ཡིན་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཕྱིན་ཅི་མ་ལོག་པ་དང་། གཏན་ལ་ཕབ་པར་ཁོང་དུ་ཆུད་ཅིང་སྟོན་ནུས་པ་ཐོབ་པ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3365]
དམ་པ་ནི་ཉན་ཐོས་ལ་སོགས་པ་སོ་སོ་ཡང་དག་པར་རིག་པ་ལས༌[^2910]ཁྱད་པར་དུ་འཕགས་པའོ། །
--- END BLOCKS ---
