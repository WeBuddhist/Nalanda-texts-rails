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
[Block 3466]
ཞིག་པ་དང་མ་སྐྱེས་པ་མི༌[^2424]ཤེས་པ་ནི་འདས་པ་དང་མ་འོངས་པ་མི་ཤེས་པ་སྟེ། ད་ལྟར་གྱི་ཕ་རོལ་གྱི་སེམས་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3467]
གཞན་ཡང་ཆོས་རྗེས་བློ་ཕྱོགས་ཕན་ཚུན༌[^2425]མིན། །ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ཆོས་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པས་ཀྱང་རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པའི་སེམས་མི་ཤེས་ལ། རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པས་ཀྱང་ཆོས་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པའི་སེམས༌[^2426]མི་ཤེས་ཏེ། དེ་གཉིས་ནི་འདོད་པའི་ཁམས་དང་ཁམས་གོང་མའི་གཉེན་པོ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3468]
མཐོང་བའི་ལམ་ལ་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་མེད་དོ། །

[Block 3469]
དེའི་དམིགས་པ་ནི་ཡོད་དེ། དེ་ལ་ཕ་རོལ་གྱི་སེམས་ཤེས་པས་མཐོང་བའི་ལམ་ཤེས་པར་འདོད་པས་སྦྱོར་བ༌[^2427]བྱས་ན། ཉན་ཐོས་མཐོང་བའི་སྐད་ཅིག་གཉིས།[^2428] །

[Block 3470 [VERSE]]
རིག་སྟེ་བསེ་རུ་ལྟ་བུས་གསུམ། །
སངས་རྒྱས་སྦྱོར་བ་མེད་པར་ཀུན། །

[Block 3471]
ཉན་ཐོས་ཀྱིས་ནི་ཕ་རོལ་གྱི༌[^2429]སེམས་ཤེས་པས་མཐོང་བའི་ལམ་ལས་སྐད་ཅིག་མ་གཉིས་ཤེས་ཏེ། སྡུག་བསྔལ་ལ་ཆོས༌[^2430]ཤེས་པའི་བཟོད་པ་དང་། ཆོས་ཤེས་པའོ། །

[Block 3472]
རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པ་ལ་དམིགས་པ་ནི་སྦྱོར་བ་གཞན་གྱིས་བསྒྲུབ་པར༌[^2431]བྱ་བ་ཡིན་པའི་ཕྱིར་དེ་ཇི་སྲིད་ཀྱིས༌[^2432]སྦྱོར་བ་རྩོམ་པ་དེ་སྲིད་ཀྱིས་དེས༌[^2433]སེམས་བཅུ་དྲུག་རྗེས་སུ་འཐོབ་པར་འགྱུར་བས་བར་དུ་ནི་མི་ཤེས་སོ། །

[Block 3473]
རང་སངས་རྒྱས་ཀྱིས་ནི་དང་པོ་གཉིས་དང་བརྒྱད་པ་ཀུན་འབྱུང་ལ་རྗེས་སུ་ཤེས་པ་དང་། གསུམ་ཤེས་ཏེ། སྦྱོར་བ་ཆུང་བའི་ཕྱིར་རོ། །

[Block 3474]
གཞན་དག་ན་རེ་དང་པོ་དང་གཉིས་པ་དང་བཅོ་ལྔ་པ་རྣམས་ཤེས་སོ་ཞེས་ཟེར་རོ། །

[Block 3475]
སངས་རྒྱས་ཀྱིས༌[^2434]ནི་སྦྱོར་བ་མེད་པར་མཐོང་བའི་ལམ་གྱི་སྐད་ཅིག་མ་ཐམས་ཅད་མཁྱེན་ཏོ། །

[Block 3476 [HEADING]]
#### ཟད་པ་ཤེས་པ་དང་མི་སྐྱེ་བ་ཤེས་པའི་ཁྱད་པར། ^4-2-7-0

[Block 3477]
ཡང་ཟད་པ་ཤེས་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་དག་ལ་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན།

[Block 3478 [VERSE]]
ཟད་པ་ཤེས་པ་བདེན་རྣམས་ལ། །
ཡོངས༌[^2435]ཤེས་ལ་སོགས་ངེས་པའོ། །
ཡོངས་ཤེས་བྱར་མེད་ཅེས་ལ་སོགས། །
མི་སྐྱེ་བ་ཡི་བློར་འདོད་དོ། །

[Block 3479]
བསྟན་བཅོས་ལས།

[Block 3480]
ཟད་པ་ཤེས་པ་གང་ཞེ་ན། བདག་གིས༌[^2436]སྡུག་བསྔལ་ཡོངས་སུ་ཤེས་སོ་ཞེས་བྱ་བར་ཤེས་པ་དང་། ཀུན་འབྱུང་སྤངས་སོ། །

[Block 3481]
འགོག་པ་མངོན་དུ་བྱས་སོ། །

[Block 3482]
ལམ་བསྒོམས་སོ་ཞེས་བྱ་བར་ཤེས་པའི༌[^2437]རྒྱུ་ལས་བྱུང་བའི་ཤེས་པ་དང་མཐོང་བ་དང་རིག་པ༌[^2438]དང་བློ་དང་རྟོགས་པ་དང་ཤེས་རབ་དང་སྣང་བ་དང་མངོན་པར་རྟོགས་པ་གང་ཡིན་པ་འདི་ནི་ཟད་པ་ཤེས༌[^2439]པ་ཞེས་བྱའོ། །

[Block 3483]
མི་སྐྱེ་བ་ཤེས་པ་གང་ཞེ་ན། བདག་གིས་སྡུག་བསྔལ་ཡོངས་སུ་ཤེས་ཏེ། ཡང་ཡོངས་སུ་ཤེས་པར་བྱར་མེད་དོ་ཞེས་བྱ་བར་ཤེས་པ་ནས་བདག་གིས་ལམ་བསྒོམས་ཏེ་ཡང་བསྒོམ་དུ་མེད་དོ་ཞེས་བྱ་བའི་བར་དུ་ཤེས་པ་དེའི་རྒྱུ་ལས་བྱུང་བའི་ཞེས་བྱ་བ༌[^2440]རྒྱས་པར་འབྱུང་ངོ་། །ཇི་ལྟར་ན་ཟག་པ་མེད་པའི་ཤེས་པས་དེ་ལྟར་ཤེས་ཤེ་ན།

[Block 3484]
ཁ་ཆེ་བ་རྣམས་ན་རེ་བསྟན་བཅོས་ལས།

[Block 3485]
དེའི་རྗེས་ལ་ལངས་པས་དེ་ལྟར་ཤེས་ཏེ། དེའི་ཕྱིར་དེའི་བྱེ་བྲག་གིས་དེ་གཉིས་ཀྱི་བྱེ་བྲག་བསྟན་ཏོ་ཞེས་ཟེར་རོ། །

[Block 3486]
གཞན་དག་ན་རེ་ཟག་པ་མེད་པས་ཀྱང༌[^2441]དེ་ལྟར་ཤེས་ཏེ། མཐོང་བ་སྨོས་པ་ནི་བཤད་པ་འཕངས་པའི་ཕྱིར་རམ། ཡང་ན་མངོན༌[^2442]སུམ་དུ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3487]
[^2443]དེ་ཉིད་ཀྱི་ཕྱིར་རེ་ཞིག་ཤེས་པ་གང་ཡིན་པ་དེ་ནི་མཐོང་བ་ཡང་ཡིན་ནོ་ཞེས་འབྱུང་ངོ་ཞེས་ཟེར་རོ། །

[Block 3488]
དེ་ལྟར་ན་དེ་དག་ནི་ཤེས་པ་བཅུ་ཡིན་ཏེ། འདི་ལྟ་སྟེ་ཆོས་ཤེས་པ་དང་རྗེས་སུ་ཤེས་པ་དང་། ཀུན་རྫོབ་ཤེས་པ་དང་། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང་། སྡུག་བསྔལ་ཤེས་པ་དང་། ཀུན་འབྱུང་ཤེས་པ་དང་། འགོག་པ་ཤེས་པ་དང་། ལམ་ཤེས་པ་དང་། ཟད་པ་ཤེས་པ་དང་། མི་སྐྱེ་བ༌[^2444]ཤེས་པའོ། །

[Block 3489]
དེ་ལ་ཀུན་རྫོབ་ཤེས་པ་ནི་ཤེས་པ་གཅིག་ཡིན་ལ་གཅིག་གི་ཆ་ཡང་ཡིན་ནོ། །

[Block 3490]
ཆོས་ཤེས་པ་ནི་ཤེས་པ་གཅིག་ཡིན་ལ་བདུན་གྱི་ཆ་ཡང་ཡིན་ཏེ། རྗེས་སུ་ཤེས་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 3491]
སྡུག་བསྔལ་ཤེས་པ་ནི་ཤེས་པ་གཅིག་ཡིན་ལ་བཞིའི་ཆ༌[^2445]ཡང་ཡིན་ཏེ། ཀུན་འབྱུང་བ་དང་འགོག་པ་ཤེས་པ༌[^2446]དེ་དང་འདྲའོ། །

[Block 3492]
ལམ་ཤེས་པ་ནི་ཤེས་པ་གཅིག་ཡིན་ལ་ལྔའི་ཆ་ཡང་ཡིན་ནོ། །

[Block 3493]
ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ནི་ཤེས་པ་གཅིག་ཡིན་ལ་བཞིའི་ཆ་ཡང་ཡིན་ནོ། །

[Block 3494]
ཟད༌[^2447]པ་ནི་ཤེས་པ་གཅིག་ཡིན་ལ། དྲུག་གི་ཆ་ཡང་ཡིན་ཏེ། མི་སྐྱེ་བ་ཤེས་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 3495 [HEADING]]
#### ཤེས་པ་བཅུར་རྣམ་པར་གཞག་པའི་རྒྱུ་བདུན། ^4-2-8-0

[Block 3496]
ཅིའི་ཕྱིར་དེ་དག་གསུམ་ཡོད་ལ་བཅུར་རྣམ་པར་གཞག་ཅེ་ན།

[Block 3497 [VERSE]]
རང་བཞིན་དང་ནི་གཉེན་པོ་དང་། །
རྣམ་པ་རྣམ་པ༌[^2448]སྤྱོད་ཡུལ་དང་། །
སྦྱོར་དང་བྱ་བ་བྱས་ཉིད་དང་། །
རྒྱུ་རྒྱས་པ་ལས་བཅུ་ཡིན་ནོ། །

[Block 3498 [HEADING]]
##### རང་བཞིན། ^4-2-8-1-0

[Block 3499]
རྒྱུ་བདུན་གྱིས་ཤེས་པ་བཅུར་རྣམ་པར་གཞག་གོ་ཞེས་གྲག་སྟེ། [^2449]རང་བཞིན་ལས་ནི་ཀུན་རྫོབ་ཤེས་པ་སྟེ། དོན་དམ་པ་མི་ཤེས་པའི་ཕྱིར་རོ། །

[Block 3500 [HEADING]]
##### གཉེན་པོ། ^4-2-8-2-0

[Block 3501]
གཉེན་པོ་ལས་ནི་ཆོས་དང་རྗེས་སུ་ཤེས་པ་དག་སྟེ། འདོད་པའི་ཁམས་དང་ཁམས་གོང་མའི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3502 [HEADING]]
##### རྣམ་པ། ^4-2-8-3-0

[Block 3503]
རྣམ་པ་ལས་ནི་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ་ཤེས་པ་དག་སྟེ། དམིགས་པ་ཐ་མི་དད་པའི་ཕྱིར་རོ། །

[Block 3504 [HEADING]]
##### རྣམ་པ་དང་དམིགས་པ། ^4-2-8-4-0

[Block 3505]
རྣམ་པ་དང་དམིགས་པ་ལས་ནི་འགོག་པ་དང་། ལམ་ཤེས་པ་དག་སྟེ། རྣམ་པ་དང་དམིགས་པ་ཐ་དད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
