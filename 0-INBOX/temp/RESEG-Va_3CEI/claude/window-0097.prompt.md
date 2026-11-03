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
[Block 3396 [HEADING]]
#### དོགས་པ་བསལ་བ། ^4-10-3-0

[Block 3397]
དོགས་པ་བསལ་བ་ནི་ཆོས་སྨྲ་བ་ཞེས་པ་འདི་སངས་རྒྱས་འཇིག་རྟེན་དུ༌[^2868]བཞུགས་པ་དང་། མི་བཞུགས་པ་གང་གི་ཚེ་ན་ཆོས་སྨྲ་བ་ཞེས་གདགས། དེ་གཉི་ག་ཡང་ཆོས་སྨྲ་བ་ཡིན་མོད་ཀྱི་སངས་རྒྱས་འཇིག་རྟེན་ན་བཞུགས་པའི་ཚེ་ནི་སློབ་པ་ལ་གནས་པས་འཁོར་བརྒྱད་པོ་ཞེས་གདགས་ཀྱི། བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་ཆོས་སྟོན་པ་དེ་ཆོས་སྨྲ་བ་ཞེས་གདགས་སོ། །

[Block 3398]
ལེའུ་འདིའི་ནང་ནས་ཀྱང་ལུང༌[^2869]སྟོན་པ་འབྱུང་ན་ལུང་བསྟན་པའི་ལེའུ་ཞེས་ཅིའི་ཕྱིར་མི་གདགས་ཤེ༌[^2870]ན། གཙོ་བོ༌[^2871]ལས་དྲས༌[^2872]པའི་ཕྱིར་མི་གདགས་སོ། །

[Block 3399 [HEADING]]
#### ཚིག་རྐྱང་པ། ^4-10-4-0

[Block 3400]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་བྱང་ཆུབ་ཏུ་ལུང་སྟོན༌[^2873]ཏོ་ཞེས་པའི་བར་དུ་ནི་ལེའུ་འདི་ཡང་ཚིག་རྐྱང་པ་དང་ཚིགས་སུ་བཅད་པ་གཉིས་སུ་དབྱེའོ། །

[Block 3401 [HEADING]]
##### སངས་རྒྱས་འཇིག་རྟེན་ན་བཞུགས་པའི་ཚེ་ཆོས་སྨྲ་བ། ^4-10-4-1-0

[Block 3402]
ཆོས་སྨྲ་བ་ཡང་རྣམ་པ་གཉིས་ཏེ། སངས་རྒྱས་འཇིག་རྟེན་ན་བཞུགས་པའི་ཚེ་ཆོས་སྨྲ་བ་དང་། མི་བཞུགས་པའི་ཚེ་ཆོས་སྨྲ་བ་གཉིས་ལས༌[^2874]འདི་ནི་དང་པོའོ། །

[Block 3403]
སྨན་གྱི་རྒྱལ་པོ་སྔོན་གྱི་དུས་ན་མདོ་སྡེ་འདི་འཛིན་པའི་ཕྱིར། སྨན་གྱི་རྒྱལ་པོ་ཞེས་ཆེད་དུ་བཀར༌[^2875]ཏེ་བཀའ་སྩལ་ཏོ། །

[Block 3404]
ཆོས་སྤྱོད་པ་བཅུ་ལ༌[^2876]རྗེས་སུ་བསྔགས་ཞེས་པ་ནི་རྗེས་སུ་ཡི་རང་བའོ། །

[Block 3405]
རྗེས་སུ་ཡི་རང་བའི་ཚིག༌[^2877]གཅིག་གིས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཆེན་པོའི་གཞིར་གྱུར༌[^2878]ཞེས་པའོ། །

[Block 3406 [HEADING]]
##### མི་བཞུགས་པའི་ཚེ་ཆོས་སྨྲ་བ། ^4-10-4-2-0

[Block 3407 [HEADING]]
###### རྗེས་སུ་ཡི་རང་བ། ^4-10-4-2-1-0

[Block 3408]
མདོ་ལས་སྨན་གྱི་རྒྱལ་པོ་གང་ལ་ལ་ཞེས་པ་ནས་བྱང་ཆུབ་ཏུ་ལུང་བསྟན་ཏོ་ཞེས་པའི་བར་དུ་ནི་སངས་རྒྱས་མངོན༌[^2879]དུ་མི་བཞུགས་པའི་ཆོས་སྨྲ་བའི་ཡོན་ཏན་སྟོན་ཏེ། དེ་ཡང་རྗེས་སུ་ཡི་རང་བ་དང་། མངོན་དུ་སྤྱོད་པ་རྣམ༌[^2880]གཉིས་ལ་འདི་ནི་དང་པོའོ། །

[Block 3409]
རྗེས་སུ་ཡི་རང་བ་ཙམ་གྱིས་ཀྱང་འདི་ལྟ་ན་མངོན་དུ་སྤྱོད་པ་ལྟ་ཅི་སྨོས།

[Block 3410 [HEADING]]
###### མངོན་དུ་སྤྱོད་པ། ^4-10-4-2-2-0

[Block 3411]
མདོ་ལས།

[Block 3412]
སྨན་གྱི་རྒྱལ་པོ་རིགས་ཀྱི་བུའམ། རིགས་ཀྱི་བུ་མོ་ཞེས་པ་ནས་ཐལ་མོ་སྦྱར་བའི་ལས་ཀྱི་མཆོད་ཞེས༌[^2881]པའི་བར་དུ་ནི་འདིས་ཆོས་མངོན་དུ་སྤྱོད་པ་སྟོན་པ་ལ་འདིར་ཆོས༌[^2882]སྤྱོད་པ་རྣམ་པ་དྲུག་སྟོན། དབུས་དང་མཐའ་རྣམ་པར་འབྱེད་པ་ལས་ནི་ཆོས་སྤྱོད་པ་བཅུ་སྟོན་ཏོ།[^2883] །འདིའི་དྲུག་པོ་ལ་འཛིན་པ་དང་། ཀློག་པ་དང་། འདོན་པ་དང་། མོས་པ་དང་། འདྲི་བ་དང་། མཆོད་པའོ། །

[Block 3413]
མཆོད་པ་ནི་ཕྱི་ནང་གི་མཆོད་པའོ། །

[Block 3414]
ཆོས་སྤྱོད་པ་དེ་ལ་ཇི་ལྟར་བཅོམ་ལྡན་འདས་མངོན་དུ་མཐོང་བ་དང་འདྲ་བར་དད་པ་དང་། གུས་པའི་ལས༌[^2884]བསྐྱེད་པའོ། །

[Block 3415]
མདོ་ལས་སྨན་གྱི་རྒྱལ་པོ་རིགས་ཀྱི་བུ་དང་། རིགས་ཀྱི་བུ་མོ་གང་ལ་ལ་ཞེས་པ་ནས། འཇིག་རྟེན་དུ་འབྱུང་ངོ་ཞེས་པའི་བར་དུ་འདི་ནི་ཐུགས་རྗེ་དང་སྨོན་ལམ་གྱི་དབང་གིས་དེར་སྐྱེས་པ་དང་རྒྱུ་དམ་པས་འཇིག་རྟེན་དུ་འབྱུང་བའོ། །

[Block 3416]
མདོ་ལས།

[Block 3417]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ་ནས། ཕྱག་འཚལ་ཞིང་བཏུད་པ་ལྟ་ཅི་སྨོས་ཞེས་པའི་བར་དུ་ནི་སྔར༌[^2885]གང་ཟག་གི་ཡོན་ཏན་བསྟོད་ཅིང་མཆོད་པར་འོས་པ་དང་། ཡོན་ཏན་ཆེ་བས་ཐུགས་རྗེ་དང་སྨོན་ལམ་གྱིས་འདིར་སྐྱེ་ཞིང་ཕན་པ་ཆེན་པོ་བྱེད་པའོ། །

[Block 3418]
མདོ་ལས་སྨན་གྱི་རྒྱལ་པོ་ཞེས་པ་ནས་སྐྱེས་པར་རིག་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་ཡོན་ཏན་ཆེན་པོ་དང་ལྡན་པ་སྟེ། [^2886]ཐུགས་རྗེས༌[^2887]འདིར་སྐྱེ་བར་བསྟན་པ་དང་། ཆོས་འདི་སྟོན་པ་ཡང་འཕགས་པ་ཡིན་པར་བསྟན་པ་དང་། ཐེག་པ་རྣམ་གཉིས་ལས་དགར་བའི་ཕྱིར། བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཞེས་སྨོས་པ་དང་། སངས་རྒྱས་ཀྱི་ཞིང་ཡངས༌[^2888]པར་མི་སྐྱེ་བ་ཡང་ཐུགས་རྗེས་སེམས་ཅན་ལ་ཕན་འདོགས་པའི་ཕྱིར། ལྷ་དང་། ཁམས་བླ་མ་གཉིས་སུ་མི་སྐྱེ་བར་འདིར་སྐྱེ་བ༌[^2889]སྟོན་ཏོ། །

[Block 3419]
ཕྱིར་མི་ལྡོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་ལ་མོས་པའི༌[^2890]རྟགས་ནི་ཆོས་ཐོས་པ་ཙམ་གྱིས་སྒྲ༌[^2891]དང་བ་སྤུ་ལྡང་བ་དང༌[^2892]གདུང་བས་མཆི་མ་འབྱུང་བ་དེ་ནི་བྱང་ཆུབ་སེམས་དཔའི་རྟགས་སོ། །

[Block 3420]
མདོ་ལས་སྨན་གྱི་རྒྱལ་པོ་རིགས་ཀྱི་བུའམ་ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པས་སྐྱེ་བར་རིག་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་སྨྲ་བ་རྣམ་པ་དྲུག་ལ་གུས་པ་དང་། བཙུན་པར་བྱ་བ་བསྟན་ཏེ། གུས་པར་བྱ་བ་ལ་འཆད་པ་ནི་སངས་རྒྱས་ཀྱི་ཕོ་ཉ་ལྟ་བུར་བལྟའོ། །

[Block 3421]
སྨོད་པ་ནི་དེ་བཞིན་གཤེགས་པ་ལ་སྐུར་པས་སྡིག་པ་ཆེ་བར་བསྟན་པ་དང་། ཀློག་པ་དང་། འདོན་པ་ནི་དེ་བཞིན་གཤེགས་པ་ལ་རྒྱན་གྱིས་བརྒྱན་པ་བཞིན་བཞུགས་པའི་གནས་ནི་མཆོད་ཅིང་ཕྱག་བྱ་བའི་གནས་སུ་བསྟན་ཏེ། མཆོད་པ་རྣམ་བཞིས་མཆོད་པར་བྱའོ། །

[Block 3422]
ཕོ་ཉ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པའི་དགོངས་པ་དང་མཐུན་པ། སྐྱེ་བ་ཞེས་པ་ནི་གསུང་དང་མཐུན་པ། བྱ་བ་བྱེད་པ་ཞེས་པ་ནི་སྐུའི་ཕྲིན་ལས༌[^2893]དང་མཐུན་པས། དེ་བཞིན་གཤེགས་པའི་མཛད་པ་ཐམས་ཅད་བྱེད་པའོ། །

[Block 3423]
མདོ་ལས་ཡང་སྨན་གྱི་རྒྱལ་པོ་སེམས་ཅན་གང་ལ་ལ་ཞེས་པ་ནས་ཤིན་ཏུ་སྡུག་པར་བཤད་དོ་ཞེས་པའི་བར་དུ་ནི་ཆེས་སྨྲ་བ་ལ་སྨོད་པ་སྡིག༌[^2894]ཆེ་བར་བཤད་པ་སྟེ། དེ་ནི་བཅོམ་ལྡན་འདས་ལ་ངན་སེམས་ཀྱིས་སྨད་པ་ནི་ཕན་པར་སྤྱོད་པ་རྣམ་གཉིས་ཉམས་པར་མི་འགྱུར་བ་ནི་བཅོམ་ལྡན་འདས་ལ་འཁྲུག་པ་མི་མངའ་བའི་ཕྱིར་རོ། །

[Block 3424]
ཆོས་སྨྲ་བ་ལ་སྨད་པས་ནི་ཕན་པར་སྤྱོད་པ་གཉིས་ཉམས་ཤིང་འཁྲུག་པ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 3425]
ཡང་སངས་རྒྱས་ལ་སྨད་པས་ནི་བྱམས་སྡང་གི་ཐུགས་མི་དགོངས་ཏེ༌[^2895]སེམས་ཅན་མི་སྤོང་གི་ཆོས་སྨྲ་བ་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 3426]
སངས་རྒྱས་འཇིག་རྟེན་ན་བཞུགས་པའི་ཚེ། སེམས་ཅན་དབང་པོ་བརྟན་པས༌[^2896]འགའ་ཞིག་སྨོད་པ་ཡོད་ཀྱང་གཞན་གྱི༌[^2897]སེམས་ནུར་བར་མི་འགྱུར་གྱི། དེང་སང་གི་ཆོས་སྨྲ་བ་ལ་སྨད་པས་གཞན་གྱི་སེམས་ལྡོག་པའི་ཕྱིར་བདག་དང་གཉི་ག་ལ་གནོད་དོ། །

[Block 3427]
མདོ་དག་ལས་ཀྱང་བྱང་ཆུབ་སེམས་དཔའི་སེམས་དཀྲུགས་པ་ནི་སེམས་ཅན་ཐམས་ཅད༌[^2898]ཆོས་ཀྱི་སྣང་བ༌[^2899]སྒྲིབ་པར་བྱེད་པས་མནར་མེད་པ་ལྔ་བྱས་པ་བས་ཁ་ན་མ་ཐོ་བ་འདི་ཆེ་བར་བཤད་དོ། །

[Block 3428]
བྱང་ཆུབ་ཀྱི་སེམས་དཀྲུགས་ཞེས་པ་ཡང་སངས་རྒྱས་ཀྱི་ཆོས་འཇིག་པའོ། །

[Block 3429]
མདོ་ལས། དེ་ཅིའི་ཕྱིར་ཞེ་ན། སྨན་གྱི་རྒྱལ་པོ་ཞེས་པ་ནས། དེ་བཞིན་གཤེགས་པ་ཕྲག་པ་ལ་ཐོགས་པ་ཡིན་ནོ་ཞེས་པའི་བར་དུ་ནི་དམ་པའི་ཆོས་འདི་འདོན་པ་ཡོན་ཏན་ཐམས་ཅད་ཀྱི་རྒྱན་གྱིས་བརྒྱན་པའི་ཕྱིར་སྡོང་པོས་བརྒྱན་པ་ལས་བྱང་ཆུབ་སེམས་དཔའི་རྒྱན་རྣམ་པ་བཅུས་བརྒྱན་པའམ། དེ་བཞིན་གཤེགས་པའི་རྒྱན་ཐམས་ཅད་ཀྱིས་བརྒྱན་པའོ། །

[Block 3430]
མདོ་ལས་དེ་གང་དུ་འགྲོ་བ་དེར་ཞེས་པ་ནས་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་དམ་པའི་ཆོས་འདི་ཤིན་ཏུ་ཟབ་པའི་ཕྱིར་འཕགས་པ་དགའ་བོ་ལ་མ་གཏད་ཀྱི། བྱང་ཆུབ་སེམས་དཔའ་སྨན་གྱི་རྒྱལ་པོ་ལ་སོགས་པ་ལ་གཏད་པ་ཡང་ཇི་ལྟར་སྨན་པ་ཆེན་པོས༌[^2900]དུག་སྨན་དུ་བསྒྱུར་བ་བཞིན་སྨན་པ་མི་མཁས་པས་མི་ནུས་སོ། །

[Block 3431]
དེ་བཞིན་དུ་ཆོས་འདི་བྱང་ཆུབ་སེམས་དཔའ་ལ་གཏད་པར་འོས་ཀྱི་ཉན་ཐོས་པ་རྣམས་ལ་མ་ཡིན་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་ནི་ཐོས་པ་ཙམ་གྱིས་མཐར་ཕྱིན་པར་འགྱུར་བ་དང་བདག་དང་གཞན་གྱི༌[^2901]དོན་འགྲུབ་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3432 [HEADING]]
#### ཚིགས་སུ་བཅད་པ། ^4-10-5-0

[Block 3433]
མདོ་ལས།

[Block 3434]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2902]དེའི་ཚེ་ཞེས་པ་ནས་འཛིན་པ་ལ་བཀུར་སྟི་བྱ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིག་བཅུ་དྲུག་ལ་རྣམ་པ་གསུམ་དུ་དབྱེ་སྟེ། ཚིག་དང་པོ་གཉིས་ཀྱིས་ནི་ཆོས་སྨྲ་བའི་ཡོན་ཏན་དང་མཆོད་པར་འོས་པ་གླེངས། ཚིག་བཅུ་གསུམ་གྱིས་ནི་ཆོས་སྨྲ་བའི་ཡོན་ཏན་ཉིད་གླེངས། ཚིག་གཅིག་གིས་ནི་ཆོས་ཁྱད་པར་ཅན་བསྡུ་བ༌[^2903]བསྟན་ཏོ། །

[Block 3435 [HEADING]]
##### ཆོས་སྨྲ་བའི་ཡོན་ཏན་དང་མཆོད་པར་འོས་པ། ^4-10-5-1-0
--- END BLOCKS ---
