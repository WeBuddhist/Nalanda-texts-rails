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
མདོ་ལས་དེ་ནས་སྤོབས་པ་ཆེན་པོ་ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པའི་སྐུ་མཐོང་ངོ་ཞེས་པའི་བར་དུ་ནི་སྔར་གླེང་བ་དང་མཆོད་རྟེན་དབྱེ་བ་སྟེ། དེ་ལ་ཡང་གསོལ་བ་དང་། ལན་བཏབ་པ་དང་། བཟླས་ཏེ་གསོལ་པ་དང་། དབྱེ་བར་སྣང་བའོ། །

[Block 3572 [HEADING]]
###### ལན་བཏབ་པ། ^4-11-4-2-2-0

[Block 3573]
མདོ་ལས།

[Block 3574]
དེ་སྐད་ཅེས་གསོལ་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་འདིར་དགུག༌[^2982]པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་སྤྲུལ་པའི་སྐུ་སླར་བསྡུ་བ་སྟེ། དེ་འདྲི་བ་ན་རེ་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་ནི་སུམ་སྟོང་ལས་མི་འདའོ་ཞེས་གསུངས་ནས། འདིར༌[^2983]ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་སྐུ་མང་པོས་ཁྱབ་ཅེས་གསུངས་པ་ཅིའི་ཕྱིར་དང་པོ་སྤྲུལ་པ་མཐོང་བ་རྣམས་ལ་གྲངས་བསྟན་པར་ཟད་ཀྱི་ཡོན་ཏན་ཚད་མེད་པའི་ཕྱིར་སྐུ་སྤྲུལ་པ་ཡང་གྲངས་མེད་པ་དང་། སྐུ་ཐ་མི་དད་པའི་ཕྱིར་སྤྲུལ་པ་ཐམས་ཅད་ནི་ངའི་སྐུ་ཞེས་པར་སྦྱར་རོ། །

[Block 3575 [HEADING]]
###### བཟླས་ཏེ་གསོལ་བ། ^4-11-4-2-3-0

[Block 3576]
མདོ་ལས་དེ་ནས་སྤོབས་པ་ཆེན་པོ་ཞེས་པ་ནས། བདག་ཅག་གིས་ཕྱག་བགྱིའོ་ཞེས་པའི་བར་དུ་ནི་བཟླས་ཏེ་གསོལ་བའོ། །

[Block 3577 [HEADING]]
###### དབྱེ་བར་སྣང་བ། ^4-11-4-2-4-0

[Block 3578 [HEADING]]
###### **སྤྲུལ་པའི་སྐུ་རྣམས་བསྡུ་བ།** ^4-11-4-2-4-1-0

[Block 3579]
མདོ་ལས་དེ་ནས་དེའི་ཚེ་བཅོམ་ལྡན་འདས་ཀྱི་ཞལ་གྱི་མཛོད་སྤུ་ནས་ཞེས་པ་ནས། དེ་དག་ཐམས་ཅད་སྣང་ངོ་ཞེས་པའི་བར་དུ་ནི་དབྱེ་བ་སྣང་སྟེ། སྔར་སྤྲུལ་པའི་སྐུ་རྣམས་བསྡུ་བ་དང་། མཆོད་རྟེན་དངོས་སུ་ཕྱེ་བའོ། །

[Block 3580]
དེའི་ཚིག་དང་པོ་ལ་རྣམ་པ་བཞི་སྟེ། འོད་ཀྱིས་སྣང་བར་མཛད་པ་དང་། སྤྲུལ་པའི་སངས་རྒྱས་སླར་གཤེགས་པ་དང་། དེ་བསུ་བ་དང་། མགོན་པོ་དེ་ལ་མེ་ཏོག་འབུལ་བའོ། །

[Block 3581]
སྤྲུལ་པའི་སྐུ་དེ་དག་འཕགས་པ་དགོངས་པ་དག་པ་རྣམས་འོད་ཀྱིས་བསྐུལ་མི་དགོས་པར་བྱོན་པར་འོས་ན་ཅིའི་ཕྱིར་འོད་ཀྱིས་བསྐུལ། དེ་ནི་འཇིག་རྟེན་པ་རྣམས་དེ་བཞིན་གཤེགས་པའི་རྫུ་འཕྲུལ་བསམ་གྱིས་མི་ཁྱབ་པར་བསྟན་པའི་ཕྱིར༌[^2984]འོད་ཀྱིས་སྦྲན་ཏེ་བྱོན་པར་བསྟན་པའོ། །

[Block 3582]
འོད་ཟེར་བཏང་ཞེས་པ་ནི་ཐེག་པ་གཅིག་པོ་བསྟན་པའི་དོན་ཏོ། །

[Block 3583]
སངས་རྒྱས་མང་པོ་སྣང་བར་མཛད་པ་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་མཛད་པ་མཐུན་པ་བསྟན་པའོ། །

[Block 3584]
མདོ་ལས་སངས་རྒྱས་ཀྱི་ཞིང་དེ་དག་ནི་ཤེལ་ལས་བྱས་པ་ཞེས་པ་ནས་གསེར་གྱི་དྲ་བས་གཡོགས་པར་སྣང༌[^2985]ངོ་ཞེས་པའི་བར༌[^2986]ནི་འདིའི་ནང་དུ་དོན་རྣམ་པ་གསུམ་སྟོན་ཏེ། ཞིང་གི་མཚན་ཉིད་དང་། འཁོར་དང་། བླ་རེ་ཆེན་པོ་ཅིའི་ཕྱིར༌[^2987]ཞིང་རྣམ་པར་དག་པའི་ཚུལ་དུ་སྟོན་ཞེ་ན། བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཡང་དག་པའི་སྤྱོད་ཡུལ་དུ་རིན་པོ་ཆེ༌[^2988]རྒྱན་སྣ་ཚོགས་སྣང་བར་བསྟན་པ་དང་། ཐེག་པ་གཅིག་པོའི༌[^2989]ནང་དུ་ཡོན་ཏན་ཐམས་ཅད་བསྡུ་བར་བསྟན་པའོ། །

[Block 3585]
མདོ་ལས་དེ་དག་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་ཡོངས་སུ་གང་བར་སྣང་ངོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་སྟོན་པའོ། །

[Block 3586]
མདོ་ལས།

[Block 3587]
དེ་བཞིན་དུ་ཤར་དང་ལྷོ་ཕྱོགས་ཞེས་པ་ནས་གཤིན་རྗེའི་འཇིག་རྟེན་ཡང་མེད་ཅེས་པའི་བར་དུ་ནི་ཕྱོགས་གཞན་དུ་ཕྱིན་པ་དང་དེ་བཞིན་གཤེགས་པ་གཞན་ཡང་དེར་བྱོན་པ་དང་། བསུ་སྟེ་གཤེགས་པ་བསྟན་ཏོ། །

[Block 3588]
འཇིག་རྟེན་གྱི་ཁམས་སྤོ་བ་དང་། དེ་བཞིན་གཤེགས་པ་བཞུགས་པ་དང་། དེར་བཞུགས་ནས་ཀྱང་རྫུ་འཕྲུལ་ཆེན་པོ་བསྟན་པའོ། །

[Block 3589]
འཇིག་རྟེན་གྱི་ཁམས་སྤོ་བ་ཡང་རྣམ་པར་དག་པའི་ཞིང་དུ་བསྟན་ཏེ། རི་དང་། ཆུ་དང་། ནགས་ལ་སོགས་པ་གསལ་བར༌[^2990]བསྟན་པ་འདིས༌[^2991]ནི་ཞིང་རྣམ་པར་དག་པ་མཉམ་པ་ཉིད་བསྟན་ཏོ། །

[Block 3590]
དང་པོ་རིན་ཆེན་མང་གི་མཆོད་རྟེན་ཞིང་མ་དག་པ་ན་བཞུགས་པ་བསྟན་པ་ནི། ཐེག་པ་རྣམ་པ༌[^2992]གཉིས་དྲང་བའི་དོན་ཏོ། །

[Block 3591]
སྤྲུལ་པའི་སྐུ་འདུས་ནས་ཞིང་རྣམ་པར་དག་པར་གྱུར་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་དོན་དུ་བསྟན་པའོ། །

[Block 3592]
ཡང་ན་དང་པོ་ཞིང་མ་དག་པ་ནི་མ་རབས་ཀྱི་ས་བསྟན་ཏོ། །

[Block 3593]
དེའི་འོག་ཏུ་སྟོང་ཆེན་པོ་གཅིག་གིས༌[^2993]བསྒྱུར་བ་ནི་འཕགས་པ་ཉན་ཐོས་པའི་དཔེའོ། །

[Block 3594]
དེའི་འོག་ཏུ་བསྒྱུར་བ་ནི་འཕགས་པ་རང་སངས་རྒྱས་པ་རྣམས་ཀྱི་དཔེའོ། །

[Block 3595]
ཡང་དེའི་འོག་ཏུ་བསྒྱུར་བ་ནི་ཐེག་པ་ཆེན་པོ་ཡོངས་སུ་རྒྱས་པའི་དཔེའོ། །

[Block 3596]
མདོ་ལས།

[Block 3597]
དེའི་ཚེ༌[^2994]མི་མཇེད་ཀྱི་ཁམས་ན་ཞེས་པ་ནས་དེ་ལྟར་དེ་བཞིན་གཤེགས་པ་དེ་དག་ཐམས་ཅད་ཀྱི་རང་རང་གི་ཞམ་འབྲིང་བ་བཀྱེའོ༌[^2995]ཞེས་པའི་བར་དུ་ནི་རྒྱས་པར་བསྒྱུར་ཞིང་སྤོ་བ་སྟེ། དེ་ཡང་གཅིག་གིས་བསྒྲེ་ཞིང་བསྒྱུར་བ་དང་། བརྒྱར་བསྒྲེ་ཞིང་བསྒྱུར་བ་ནི་དེ་བཞིན་གཤེགས་པ་ཐ་དད་པས་སོ། །

[Block 3598]
དེ༌[^2996]བསྒྱུར་བ་ཡང་དང་པོ་ནི་ཞིང་བསྒྱུར། དེའི་འོག་ཏུ་ནི༌[^2997]སེམས་ཅན་བསྒྱུར་བ་དང་། དག་པའི་མཚན་ཉིད་བསྒྱུར་བ་དང་། མ་དག་པ་བསལ་བ༌[^2998]དང་། རྒྱན་གྱིས་བརྒྱན༌[^2999]པའོ། །

[Block 3599]
འོད་ཀྱིས་སྣང་བར་མཛད་པ་ནི་ཕྱོགས་བཅུའི་དེ་བཞིན་གཤེགས་པ་བསྐུལ་བའོ། །

[Block 3600]
སེམས་ཅན་དམྱལ་བ་མེད་ཅེས་པ་ནི་སེམས་ཅན་བསྒྱུར་བའོ། །

[Block 3601]
རི་དང་མཚོ་ལ་སོགས་པ་མེད་པར་བྱས་པ་ནི་ཞིང་བསྒྱུར་བའོ། །

[Block 3602]
འདི་བཞག་སྟེ་ཞེས་པ་ནི་འཁོར་འདི་དག་ཆོས་ཀྱི་སྣོད་དུ་གྱུར་པ་བསྟན་པའོ། །

[Block 3603]
སངས་རྒྱས་ཀྱི་ཞིང་གཅིག་ཏུ་བྱས་ཞེས་པ་ནི་རྒྱན་གྱིས༌[^3000]བརྒྱན་པ་བསྟན་ཏོ།[^3001] །

[Block 3604 [HEADING]]
###### **མཆོད་རྟེན་དངོས་སུ་ཕྱེ་བ།** ^4-11-4-2-4-2-0

[Block 3605 [HEADING]]
###### **ནམ་མཁའ་ལ་བཞུགས་པ།** ^4-11-4-2-4-2-1-0

[Block 3606]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པས་ཞེས་པ་ནས་ནམ་མཁའ་བར་སྣང་ལ་བཞུགས་སོ་ཞེས་པའི་བར་དུ་ནི་མཆོད་རྟེན་དབྱེ་བར་དགོངས་པ་སྟེ། དེ་ཡང་དོན་གྲུབ༌[^3002]ནས་ནམ་མཁའ་ལ་བཞུགས་པ་དང་། འཁོར་བཞི་པོ་ལངས་ནས་ཞལ་དུ་བལྟ་བ༌[^3003]དང་། མཆོད་རྟེན་མངོན་པར་ཕྱེ་བའོ། །

[Block 3607 [HEADING]]
###### **འཁོར་བཞི་པོ་ལངས་ནས་ཞལ་དུ་བལྟ་བ།** ^4-11-4-2-4-2-2-0

[Block 3608]
མདོ་ལས་འཁོར་བཞི་པོ་དེ་དག་སྟན་ལས་ལངས་ནས་ཐལ་མོ་སྦྱར་ཏེ། བཅོམ་ལྡན་འདས་ལགས་སུ་བལྟ་ཞིང་འཁོད་དོ་ཞེས་པ་ནི༌[^3004]འཁོར་ལངས་པ་བསྟན་པའོ། །

[Block 3609 [HEADING]]
###### **མཆོད་རྟེན་མངོན་པར་ཕྱེ་བ།** ^4-11-4-2-4-2-3-0

[Block 3610]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱི༌[^3005]ཞེས་པ་ནས། ས་ལེར་བྱས་སོ་ཞེས་པའི་བར་དུ་ཕྱག་གཡས་པ་ཞེས་པ་ནི་བཀྲ་ཤིས་པར་བྱ་བའོ།[^3006] །མདོ་ལས་དེ་བཞིན་གཤེགས་པའི་ཞེས་པ་ནས་ཁོ་བོ་འདིར་འོངས་སོ་ཞེས་པའི་བར་དུ་ནི་མཆོད་རྟེན་ཕྱེ་བས་འཆད་པ་དང་། ཉན་པ་རྣམས་སྤྲོ་བར་བྱ་བའི་གཏན་ཚིགས་བསྟན་ཏེ། སྐུ་མངོན་པར་སྟོན་ཅིང་གསུང་སྨྲ་བ་དང་། མེ་ཏོག་འཐོར་བ༌[^3007]གཉིས་ལས༌[^3008]འདི་ནི་དང་པོའོ། །
--- END BLOCKS ---
