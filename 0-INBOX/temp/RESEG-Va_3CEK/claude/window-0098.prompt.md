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
[Block 3431]
གཞན་ཤེས༌[^2405]འཇིག་རྟེན་པའི་ཤེས་རབ་ཐམས་ཅད་ནི་ཤེས་པ་ཁོ་ན༌[^2406]ཡིན་ནོ། །

[Block 3432]
དྲུག་ནི་ལྟ་བའང་ཡིན། །ལྟ་བ་ལྔ་དང་། འཇིག་རྟེན་པའི་ལྟ་བ་ཡང་དག་པའི་ལྟ་བ་སྟེ། འཇིག་རྟེན་པའི་ཤེས་པ་རྣམ་པ༌[^2407]དྲུག་ནི་ལྟ་བ་ཡིན་གྱི༌[^2408]གཞན་ནི་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 3433]
འདི་དག་དང་གཞན་དག་ཀྱང་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 3434 [HEADING]]
### ཤེས་པ་བཅུ། ^4-2-0

[Block 3435]
ཇི་སྙེད་ཅིག་གིས་ཤེས་པ་ཐམས་ཅད་བསྡུས་ཤེ་ན། ཤེས་པ་བཅུས་བསྡུས་སོ། །

[Block 3436]
མདོར་བསྡུ་ན་ནི་གཉིས་ཏེ། [^2409]ཤེས་པ་ཟག་བཅས་ཟག་པ་མེད། །དེ་གཉིས་ལས་ཀྱང་།

[Block 3437 [HEADING]]
#### ཀུན་རྫོབ་ཤེས་པ། ^4-2-1-0

[Block 3438]
དང་པོ་ཀུན་རྫོབ་ཅེས་བྱའོ། །

[Block 3439]
ཟག་པ་དང་བཅས་པ་གང་ཡིན་པ་དེ་ནི་ཕལ་ཆེར་བུམ་པ་དང་སྣམ་བུ་དང་སྐྱེས་པ་དང་བུད་མེད་ལ་སོགས་པ་ཀུན་རྫོབ་འཛིན་པའི་ཕྱིར་ཀུན་རྫོབ་ཤེས་པ་ཡིན་ནོ། །

[Block 3440 [HEADING]]
#### ཆོས་ཤེས་པ་དང་རྗེས་སུ་ཤེས་པ། ^4-2-2-0

[Block 3441]
ཟག་མེད་རྣམ་གཉིས་ཆོས་དང་ནི། རྗེས་སུ་ཤེས་པ་ཁོ་ན་ཡིན། །ཟག་པ་མེད་པའི་ཤེས་པ་ལ་རྣམ་པ་གཉིས་སུ་དབྱེ་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པའོ། །

[Block 3442]
དེ་ལྟར་ན་ཤེས་པ་འདི་གཉིས་ནི་གསུམ་ཡིན་ཏེ། ཀུན་རྫོབ་ཤེས་པ་དང་། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པའོ། །

[Block 3443 [HEADING]]
#### ཤེས་པ་གསུམ་གྱི་སྤྱོད་ཡུལ། ^4-2-3-0

[Block 3444]
དེ་ལ། ཀུན་རྫོབ་ཡུལ་ནི་ཐམས་ཅད་དོ། །

[Block 3445]
ཀུན་རྫོབ་ཤེས་པའི་དམིགས་པ་ནི་ཅི་རིགས་པར་འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཡིན་ནོ། །

[Block 3446]
ཆོས་ཤེས་བྱ་བའི་སྤྱོད་ཡུལ་ནི། །འདོད་པའི༌[^2410]སྡུག་བསྔལ་ལ་སོགས་པ།[^2411] །ཆོས་ཤེས་པའི་དམིགས་པ་ནི་འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་དང་། དེ་ཀུན་འབྱུང་བ་དང་།

[Block 3447 [VERSE]]
འགོག་པ་དང་ལམ་རྣམས་ཡིན་ནོ། །
རྗེས་སུ༌[^2412]ཤེས་པའི་སྤྱོད་ཡུལ་ནི། །

[Block 3448]
[^2413]གོང་མའི་སྡུག་བསྔལ་ལ་སོགས་ཡིན།[^2414] །རྗེས་སུ་ཤེས་པའི་དམིགས་པ་ནི་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་དང་། དེ་ཀུན་འབྱུང་བ་དང་།

[Block 3449]
འགོག་པ་དང་ལམ་རྣམས་སོ། །

[Block 3450 [HEADING]]
#### བདེན་པའི་བྱེ་བྲག་གིས་ཤེས་པ་བཞི། ^4-2-4-0

[Block 3451]
དེ་དག་ཉིད་བདེན༌[^2415]བྱེ་བྲག་གིས། །

[Block 3452]
བཞི་སྟེ། ཆོས་ཤེས་པ་དང་རྗེས་སུ་ཤེས་པ་དེ་དག་ཉིད་བདེན་པའི་བྱེ་བྲག་གིས༌[^2416]སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་བ་དང་། འགོག་པ་དང་། ལམ༌[^2417]ཤེས་པ་རྣམས་དང་ཤེས་པ་བཞི་ཡིན་ཏེ། དེ་དག་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3453 [HEADING]]
#### ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ། ^4-2-5-0

[Block 3454]
རྣམ་བཞི་དེ་དག་ནི། མི་སྐྱེ་བ་དང་ཟད་པ་ཤེས། །ཆོས་དང་རྗེས་སུ་ཤེས་པ་ལྟ་བའི་རང་བཞིན་མ་ཡིན་པ་རྣམ་པ་བཞི་པོ་དེ་དག་ཁོ་ནར་ཟད་པ་ཤེས་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་ཞེས་བྱའོ། །

[Block 3455 [VERSE]]
དེ་གཉིས་དང་པོ་སྐྱེས་པ་ནི། །
སྡུག་བསྔལ་རྒྱུ་རྗེས་ཤེས་པ་ཡིན། །

[Block 3456]
ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་དང་པོ་སྐྱེས་པ་ནི་སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་ལ་རྗེས་སུ་ཤེས་པ་ཡིན་ཏེ། [^2418]སྲིད་པའི་རྩེ་མོའི༌[^2419]ཕུང་པོ་ལ་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་ལ་རྗེས་སུ་ཤེས་པའི་རྣམ་པར་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3457]
ཡང་ཅི་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ཀྱང་དེ་གཉིས་དང་དམིགས་པ་གཅིག་པ་ཞིག་ཡིན་ནམ་ཞེ་ན། གལ་ཏེ་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་ལ་དམིགས་ན་ནི་ཡིན་ནོ། །

[Block 3458]
འོན་ཏེ་འགོག་པ་དང་ལམ་ལ་དམིགས་པ་ཞིག་ཡིན༌[^2420]ན་ནི་དམིགས་པ་གཅིག་པ་མ་ཡིན་ནོ། །

[Block 3459 [HEADING]]
#### ཕ་རོལ་གྱི་སེམས་ཤེས་པ། ^4-2-6-0

[Block 3460]
བཞི་ལས་ཕ་རོལ་སེམས་རིག་པ། །རིག་པར་བྱེད་པས་ན་རིག་པ་སྟེ་ཤེས་པའོ། །

[Block 3461]
ཕ་རོལ་གྱི༌[^2421]སེམས་ཤེས་པ་ནི་ཤེས་པ་བཞི་ལས་སྐྱེ་བར་བལྟ་བར༌[^2422]བྱ་སྟེ། ཆོས་ཤེས་པ་དང་རྗེས་སུ་ཤེས་པ་དང་ལམ་ཤེས་པ་དང་།

[Block 3462 [VERSE]]
ཀུན་རྫོབ་ཤེས་པ་རྣམས་ལས་སོ། །
དེའི་ངེས་པ་ནི་འདི་ཡིན་ཏེ། །
དེས་ནི་ས་དབང་གང་ཟག་འདས། །
ཞིག་དང་མ་སྐྱེས་མི་རིག་གོ། །

[Block 3463]
ས་འདས་པ་མི་ཤེས་པ་ནི་བསམ་གཏན་འོག་མའི་ས་པས་བསམ་གཏན་གོང་མའི་ས་པ་མི་ཤེས་པའོ། །

[Block 3464]
དབང་པོ་འདས་པ་མི་ཤེས་པ༌[^2423]ནི་དད་པས་མོས་པ་དང་དུས་ཀྱིས་རྣམ་པར་གྲོལ་བའི་ལམ་གྱིས་མཐོང་བས་ཐོབ་པ་དང་དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བའི་ལམ་མི་ཤེས་པའོ། །

[Block 3465]
གང་ཟག་འདས་པ་མི་ཤེས་པ་ནི་ཕྱིར་མི་འོང་བ་དང་དགྲ་བཅོམ་པ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་སངས་རྒྱས་ཀྱི་ལམ་རྣམས་འོག་མས་གོང་མ་མི་ཤེས་པའོ། །

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
--- END BLOCKS ---
