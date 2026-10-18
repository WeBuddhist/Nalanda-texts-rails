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
[Block 3536]
མཆོད་རྟེན་ནམ་མཁའ་ལ་འཕགས་པ་ཡང་དེ་བཞིན་གཤེགས་པའི་ཞིང་རྣམ་པར་དག་པ་ཡང་འཇིག་རྟེན་པའི་དགེ་བའི་རྩ་བ་ལས་ཁྱད་པར་དུ་བསྟན་པའོ། །

[Block 3537]
ལྔ་བརྒྱ་ལ་ཡང་ནམ་མཁའ་ལ་འཕགས་པ་ནི་དེ་བཞིན་གཤེགས་པ་འཁོར་བ་ཐམས་ཅད་ལས་འདས་ཏེ་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ལ་གནས་པ་བསྟན་ཏོ། །

[Block 3538]
ཡང་ན་ཐེག་པ་གཅིག་པོ་འདིར་ཐེག༌[^2968]པ་གཉིས་པ་ལས་ཁྱད་པར་དུ་འཕགས་པ་བསྟན་ཏོ། །

[Block 3539]
ནམ་མཁའ་བར་སྣང་ཞེས་པ་ནི༌[^2969]ཡང་དག་པ་སྟོང་པ་ཉིད་ལ་གནས་པ་བསྟན་ཏོ། །

[Block 3540]
མདོ་ལས་སྣ་ཚོགས་བལྟ༌[^2970]ན་སྡུག་ཅེས་པ་ནས་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་ཁྱབ་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་རྒྱན་གྱི་མཚན་ཉིད་བསྟན་ཏེ། རྒྱན་བརྒྱད་དང་། གདུགས་དང་། བ་དན་ལ་སོགས་པའོ། །

[Block 3541]
མཆོད་རྟེན་རྒྱན་ཐམས་ཅད་ཀྱིས་བརྒྱན་པ་བཞིན་དེ་བཞིན་གཤེགས་པའི་སྐུ་དང་དམ་པའི་ཆོས་འདི་ཡོན་ཏན་ཐམས་ཅད་ཀྱིས་བརྒྱན་པར་སྦྱར་རོ། །

[Block 3542]
རྒྱན་ཐམས་ཅད་ནི་ཡོན་ཏན་སྣ་ཚོགས་ཀྱི་དཔེའོ། །

[Block 3543]
ཁ་རན་ལྔ་སྟོང་ནི་དད་པ༌[^2971]བརྩོན་འགྲུས་དང་དྲན་པ་དང་ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་ཀྱི་དཔེའོ། །

[Block 3544]
རྟ་བབས་སྟོང་ཕྲག་མང་པོ་ཞེས་པ་ནི་བསམ་གཏན་དང་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 3545]
རྒྱལ་མཚན་དང་བ་དན་ཞེས་པ་ནི་ཡེ་ཤེས་དང་གཟུངས་སུ་བལྟའོ། །

[Block 3546]
ཕྲེང་བ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་དང་སྦྱར་རོ།[^2972] །དྲི་དང་སྤོས་དམ་པ་ནི་དེ་བཞིན་གཤེགས་པའི་སྐུ་རྣམས་དང་། ཉོན་མོངས་པ་ཐམས་ཅད་སེལ་བ་ཡང་དག་པ་དེ་བཞིན་ཉིད་དོ། །

[Block 3547]
མདོ་ལས་དེའི་གདུགས་ཀྱི་ཕྲེང་བ་ཞེས་པ་ནས། ཀར་ཀེ་ཏ་ནའོ་ཞེས་པའི་བར་དུ་ནི་རིན་པོ་ཆེ་སྣ་བདུན་འཕགས་པའི་ནོར་བདུན་དང་སྦྱར་རོ། །

[Block 3548]
མདོ་ལས།

[Block 3549]
མཆོད་རྟེན་དེ་ལ་ཞེས་པ་ནས་ཐལ་མོ་སྦྱར་ཏེ་འཁོད་དོ་ཞེས་པའི་བར་དུ་ནི་མཐོང༌[^2973]ཞིང་འཕགས་པས་འགྲོ་བ་ལས་ཁྱད་པར་དུ་བསྟན་པ་དང་། ཡ་མཚན་དུ་གྱུར་པས་འཁོར་རྣམས་དད་པ་སྐྱེད་པ་དང་། རྫུ་འཕྲུལ་མཛད་པའི་ཡོན་ཏན་གྱིས་མདོ་སྡེ་འདི་དམ་པ་ཡིན་པར་བསྟན་པ་དང་། མཆོད་རྟེན་ཕྱུང་བས་གུས་པ༌[^2974]བསྐྱེད་པ་དང་། འཁོར་རྣམས་ཀྱི་བསམ་པ་རིག་ནས་ཐེ་ཚོམ་མངོན་པར་གསོལ་བ་སྟེ། དེ་ཡན་ཆད་ཅི༌[^2975]རིགས་པར་སྦྱར་རོ། །

[Block 3550 [HEADING]]
###### དོན་དྲིས་པ། ^4-11-4-1-1-0

[Block 3551]
མདོ་ལས་དེ་ནས་དེའི་ཚེ་སྤོབས་པ་ཆེན་པོ་ཞེས་བྱ་བ་ནས་འདི་ལྟ་བུའི་སྒྲ་འབྱིན་པ་སུ་ཞེས་པའི་བར་དུ་ནི་དོན་དྲིས་པའོ། །

[Block 3552 [HEADING]]
###### བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ^4-11-4-1-2-0

[Block 3553]
མདོ་ལས།

[Block 3554 [HEADING]]
###### **གླེང་པ།** ^4-11-4-1-2-1-0

[Block 3555]
དེ་སྐད་ཅེས་གསོལ་པ་དང་ཞེས་པ་ནས་དེས་སྒྲ༌[^2976]འདི་ཕྱུང་ངོ་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་སྟེ། དང་པོར་གླེང་པ་དང་དངོས་སུ་བསྟན་པ་དང་བསྡུས་པའོ། །

[Block 3556]
འགྲེལ་པ་ལས་སྟུག་པོར་གནས་སོ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་ཆོས་ཀྱི་སྐུ་མངའ་བརྙེས་པ་བཞུགས་པའམ། སྤྲུལ་པའི་སྐུ་གསེར་གྱི་མདོག་ཅན་མངའ་བརྙེས་པར་བཞུགས་ཏེ། མདོ་འདི་ཉིད་དང་སྦྱར་རོ། །

[Block 3557 [HEADING]]
###### **དངོས་སུ་བསྟན་པ།** ^4-11-4-1-2-2-0

[Block 3558 [HEADING]]
###### **དེ་བཞིན་གཤེགས་པའི་སྐུ།** ^4-11-4-1-2-2-1-0

[Block 3559]
མདོ་ལས་སྤོབས་པ་ཆེན་པོ་ཤར་ཕྱོགས་སུ་ཞེས་པ་ནས། སངས་རྒྱས་རིན་ཆེན་མང་ཞེས་བྱ་བ་བྱུང་སྟེ་ཞེས་པའི་བར་དུ་ནི་དེ་ཡང་རྣམ་པ་བཞི་སྟེ། དེ་བཞིན་གཤེགས་པའི་སྐུ་དང་སྔོན་གྱི༌[^2977]སྨོན་ལམ་དང་། ལུང་བསྒོ་བ་དང་། སྨོན་ལམ་བཞིན་མཛད་པའོ། །

[Block 3560]
རིན་ཆེན༌[^2978]ཞེས་པ་དེ་བཞིན་གཤེགས་པ་གཅིག་གམ་མང་དུ་བཞུགས་འགྲེལ་པ་ལས་མདོ་བསྟན་པ་ལ་དེ་བཞིན་གཤེགས་པ་རིན་ཆེན་མང་གི་སྐུ་གཅིག་བསྟན་པའི་ནང་དུ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་འདུས་པས་སྐུ་མཉམ་པར་བསྟན་པ་དང་། ཐེག་པ་གཅིག་པོ་བསྟན་པ་ཡང་ཐེག་པ་ཐམས་ཅད་བསྡུ་བ་དང་། རིན་པོ་ཆེ་མང་ཡང་རིན་པོ་ཆེའི༌[^2979]རང་བཞིན་མཚུངས་པ་བཞིན། སྤྲུལ་པ་དང་རྫོགས་ལོངས་སྤྱོད་པའི་སྐུ་ཡང་སྐུ་མཚུངས་པ་སྟེ། ལུང་དང་གཞུང་རྣམ་པར་དག་པ་ལ་གཉིས་སུ་མེད་ཅེས་པའོ། །

[Block 3561 [HEADING]]
###### **སྔོན་གྱི་སྨོན་ལམ།** ^4-11-4-1-2-2-2-0

[Block 3562]
མདོ་ལས་བཅོམ་ལྡན་འདས་དེའི་སྨོན་ལམ་འདི་ལྟ་བུ་ཞེས་པ་ནས་ཡོངས་སུ་རྫོགས་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་སྔོན་གྱི་སྨོན་ལམ་བསྟན་པའོ། །

[Block 3563 [HEADING]]
###### **ལུང་བསྒོ་བ།** ^4-11-4-1-2-2-3-0

[Block 3564]
མདོ་ལས་ཡང་སྤོབས་པ་ཆེན་པོ་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་མཆོད་རྟེན་ཆེན་པོ་གཅིག་བྱོས་ཤིག་ཅེས་པའི་བར་དུ་ནི་ལུང་བསྒོ་བའོ། །

[Block 3565 [HEADING]]
###### **སྨོན་ལམ་བཞིན་མཛད་པ།** ^4-11-4-1-2-2-4-0

[Block 3566]
མདོ་ལས་མཆོད་རྟེན་གཞན་ནི་ངའི་ཕྱིར་བྱའོ་ཞེས་པ་ནས་དགེའོ་ཞེས་བྱ་བ་བྱིན༌[^2980]ནོ་ཞེས་པའི་བར་དུ་ནི་སྨོན་ལམ་བཞིན་གྲུབ་པར་མཛད་པའོ། །

[Block 3567 [HEADING]]
###### **བསྡུས་པ།** ^4-11-4-1-2-3-0

[Block 3568]
མདོ་ལས༌[^2981]སྤོབས་པ་ཆེན་པོ་དེ་ལྟ་བས་ན་ཞེས་པ་ནས་དགེའོ་ཞེས་བྱ་བ་བྱིན་ནོ་ཞེས་པའི་བར་དུ་ནི་མདོར་བསྡུས་ཏེ་བསྒོ་བའོ། །

[Block 3569 [HEADING]]
##### གླེང་བ་དང་མཆོད་རྟེན་དབྱེ་བ། ^4-11-4-2-0

[Block 3570 [HEADING]]
###### གསོལ་བ། ^4-11-4-2-1-0

[Block 3571]
མདོ་ལས་དེ་ནས་སྤོབས་པ་ཆེན་པོ་ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པའི་སྐུ་མཐོང་ངོ་ཞེས་པའི་བར་དུ་ནི་སྔར་གླེང་བ་དང་མཆོད་རྟེན་དབྱེ་བ་སྟེ། དེ་ལ་ཡང་གསོལ་བ་དང་། ལན་བཏབ་པ་དང་། བཟླས་ཏེ་གསོལ་པ་དང་། དབྱེ་བར་སྣང་བའོ། །

[Block 3572 [HEADING]]
###### ལན་བཏབ་པ། ^4-11-4-2-2-0

[Block 3573]
མདོ་ལས།

[Block 3574]
དེ་སྐད་ཅེས་གསོལ་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་འདིར་དགུག༌[^2982]པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་སྤྲུལ་པའི་སྐུ་སླར་བསྡུ་བ་སྟེ། དེ་འདྲི་བ་ན་རེ་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་ནི་སུམ་སྟོང་ལས་མི་འདའོ་ཞེས་གསུངས་ནས། འདིར༌[^2983]ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་སྐུ་མང་པོས་ཁྱབ་ཅེས་གསུངས་པ་ཅིའི་ཕྱིར་དང་པོ་སྤྲུལ་པ་མཐོང་བ་རྣམས་ལ་གྲངས་བསྟན་པར་ཟད་ཀྱི་ཡོན་ཏན་ཚད་མེད་པའི་ཕྱིར་སྐུ་སྤྲུལ་པ་ཡང་གྲངས་མེད་པ་དང་། སྐུ་ཐ་མི་དད་པའི་ཕྱིར་སྤྲུལ་པ་ཐམས་ཅད་ནི་ངའི་སྐུ་ཞེས་པར་སྦྱར་རོ། །

[Block 3575 [HEADING]]
###### བཟླས་ཏེ་གསོལ་བ། ^4-11-4-2-3-0
--- END BLOCKS ---
