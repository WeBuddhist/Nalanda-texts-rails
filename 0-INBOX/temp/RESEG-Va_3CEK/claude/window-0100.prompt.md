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

[Block 3506 [HEADING]]
##### སྦྱོར་བ། ^4-2-8-5-0

[Block 3507]
སྦྱོར་བ་ལས་ནི་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་སྟེ། དེས་ནི་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱང་མི་ཤེས་པ་མ་ཡིན་མོད་ཀྱི་སེམས་ཤེས་པར་བྱ་བའི་ཕྱིར་སྦྱོར་བ་བྱས་པ་ལས་གྲུབ་པའི་ཕྱིར་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ཞེས་བཤད་དོ། །

[Block 3508 [HEADING]]
##### བྱ་བ་བྱས་པ། ^4-2-8-6-0

[Block 3509]
བྱ་བ་བྱས་པ་ལས་ནི་ཟད་པ་ཤེས་པ་སྟེ། བྱ་བ་བྱས་པའི་རྒྱུད་ལ་དང༌[^2450]པོ་ཉིད་དུ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 3510 [HEADING]]
##### རྒྱུ་རྒྱས་པ། ^4-2-8-7-0

[Block 3511]
རྒྱུ་རྒྱས་པ་ལས་ནི་མི་སྐྱེ་བ་ཤེས་པ་སྟེ། ཟག་པ་མེད་པའི་ཤེས་པ་ཐམས་ཅད་ཀྱི་རྒྱུ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3512 [HEADING]]
#### ཆོས་ཤེས་པ་ཁམས་གསུམ་གྱི་གཉེན་པོ། ^4-2-9-0

[Block 3513]
ཐམས་ཅད་ཀྱི་གཉེན་པོ་ཐམས་ཅད་ཡིན་པའི་ཕྱིར། [^2451]ཆོས་ཤེས་པ་འདོད་པའི་ཁམས་ཀྱི་གཉེན་པོ་ཞེས་བཤད་པར་ཟད་ཀྱི་གཞན་ཡང་། བསྒོམ་པའི་ལམ་ལ་འགོག་པའམ།

[Block 3514 [VERSE]]
ལམ་ལ་ཆོས་ཤེས་གང་ཡིན་པ། །
ཁམས་གསུམ་གྱི༌[^2452]ནི་གཉེན་པོ་ཡིན། །

[Block 3515]
འགོག་པ་དང་ལམ་ལ་ཆོས་ཤེས་པ་བསྒོམ་པའི་ལམ་གྱིས་བསྡུས་པ་དག་ནི་ཁམས་གསུམ་ཆར་གྱི༌[^2453]གཉེན་པོ་ཡིན་ནོ། །

[Block 3516]
འདོད་པའི་ཁམས་ཀྱི་རྗེས་མ་ཡིན། །འདོད་པའི་ཁམས་ཀྱི༌[^2454]གཉེན་པོ་རྗེས་སུ་ཤེས་པ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་མེད་དོ། །

[Block 3517 [HEADING]]
### ཤེས་པ་བཅུའི་རྣམ་པ། ^4-3-0

[Block 3518 [HEADING]]
#### ཆོས་ཤེས་པ་དང་རྗེས་སུ་ཤེས་པའི་རྣམ་པ། ^4-3-1-0

[Block 3519 [VERSE]]
ཤེས་པ་བཅུ་པོ༌[^2455]དེ་དག་ལས། །
ཆོས་ཤེས་པ་དང་རྗེས་སུ་ཤེས། །

[Block 3520]
རྣམ་པ་བཅུ་དྲུག །དེ་དག་ནི་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 3521 [HEADING]]
#### ཀུན་རྫོབ་ཤེས་པའི་རྣམ་པ། ^4-3-2-0

[Block 3522]
ཀུན་རྫོབ་ནི། དེ་བཞིན་གཞན་དུའང་། ཀུན་རྫོབ་ཤེས་པ་ནི་རྣམ་པ་བཅུ་དྲུག་ཅན་ཡང་ཡིན་ལ་གཞན་གྱི་རྣམ་པ་ཅན་ཡང༌[^2456]ཡིན་ཏེ། ཆོས་ཐམས་ཅད་ཀྱི༌[^2457]རང་དང་སྤྱིའི་མཚན་ཉིད་ལ་སོགས་པ་འཛིན་པའི་ཕྱིར་རོ། །

[Block 3523 [HEADING]]
#### རང་རང་གི་བདེན་པའི་རྣམ་པ། ^4-3-3-0

[Block 3524]
རང་རང་གི༌[^2458]བདེན་པའི་རྣམ་པས་བཞི་ཡིན༌[^2459]ནོ། །

[Block 3525]
སྡུག་བསྔལ་དང་ཀུན་འབྱུང་དང་། འགོག་པ་དང་ལམ་ཤེས་པ་རྣམས་ནི་རང་རང་གི༌[^2460]བདེན་པའི་རྣམ་པ་དག་ཏུ་འཇུག་པས་རེ་རེ་ཞིང་རྣམ་པ་བཞི་བཞི་ཡིན་ནོ། །

[Block 3526 [HEADING]]
#### ཕ་རོལ་གྱི་སེམས་ཤེས་པའི་རྣམ་པ། ^4-3-4-0

[Block 3527 [HEADING]]
##### ཟག་པ་མེད་པ། ^4-3-4-1-0

[Block 3528]
ཕ་རོལ་ཡིད་ཤེས་དྲི་མེད་ཀྱང་། དེ་བཞིན་ཕ་རོལ་གྱི༌[^2461]སེམས་ཤེས་པ་ཟག་པ་མེད་པ་ཡང་དེ་བཞིན་ཁོ་ནར་རང་གི༌[^2462]བདེན་པའི་རྣམ་པ་ཅན་ཡིན་པའི་ཕྱིར༌[^2463]རྣམ་པ་བཞི་ཅན་ཡིན་ཏེ། ལམ་ཤེས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3529 [HEADING]]
##### ཟག་པ་དང་བཅས་པ། ^4-3-4-2-0

[Block 3530]
དྲི་མ་དང་བཅས་ནི། ཤེས་བྱའི་རང་གི་མཚན་ཉིད་རྣམས། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ཟག་པ་དང་བཅས་པ་ནི་ཤེས་བྱ༌[^2464]སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱི་རང་གི་མཚན་ཉིད་གང་ཡིན་པ་དེའི་རྣམ་པ་འཛིན་ཏེ། རང་གི་མཚན་ཉིད་འཛིན་པར༌[^2465]བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3531]
གཉི་ག་ཡང་། རྫས་རེ་རེ་ཞིག་སྤྱོད་ཡུལ་ལོ། །

[Block 3532]
གང་གི་ཚེ་སེམས་འཛིན་པ་དེའི་ཚེ་སེམས་ལས་བྱུང་བ༌[^2466]རྣམས་མི་འཛིན་ལ། གང་གི་ཚེ་ཚོར་བ་འཛིན་པ་དེའི་ཚེ༌[^2467]འདུ་ཤེས་མི་འཛིན་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 3533 [HEADING]]
##### འདོད་ཆགས་དང་བཅས་པའི་སེམས། ^4-3-4-3-0

[Block 3534]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་འདོད་ཆགས་དང་བཅས་པའི་སེམས་ལ་ཡང་འདོད་ཆགས་དང་བཅས་པའི་སེམས་ཞེས་བྱ་བར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་གང༌[^2468]གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། དེ་གཉིས་ཅིག་ཅར་དུ་འཛིན་པ་ནི་མ་ཡིན་ཏེ། གོས་དང་དྲི་མ་ཅིག་ཅར་དུ་མི་འཛིན་པ་བཞིན་ནོ། །

[Block 3535]
འདོད་ཆགས་དང་བཅས་པའི་སེམས་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་དང་བཅས་པ་ཉིད༌[^2469]རྣམ་པ་གཉིས་ཏེ། འདྲེས་པའི་འདོད་ཆགས་དང༌[^2470]བཅས་པ་ཉིད་དང་། ལྡན་པའི་འདོད་ཆགས་དང་བཅས་པ་ཉིད་དོ། །

[Block 3536]
དེ་ལ་འདོད་ཆགས་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ནི་གཉིས་ཀྱིས༌[^2471]འདོད་ཆགས་དང་བཅས་པ་ཡིན་ནོ། །

[Block 3537]
དེ་ལས་གཞན་པ་ཟག་པ་དང་བཅས་པ་ནི་ལྡན་པའི་འདོད་ཆགས་དང་བཅས་པས་ན་འདོད་ཆགས་དང༌[^2472]བཅས་པ་ཡིན་ནོ། །

[Block 3538]
ཁ་ཅིག་ན་རེ་མདོ་འདིར་ནི་འདོད་ཆགས་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ནི་འདོད་ཆགས་དང་བཅས་པ་ཡིན་ལ། འདོད་ཆགས་ཀྱི༌[^2473]གཉེན་པོར་ནི་འདོད་ཆགས་དང་བྲལ་བར་བཤད་པ་ཡིན་ཏེ། གལ་ཏེ་འདོད་ཆགས་དང་མཚུངས་པར་མི་ལྡན་པ་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་ན་ནི་ཉོན་མོངས་པ་གཞན་དང་མཚུངས་པར་ལྡན་པ་ཡང་ཡིན་པར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 3539]
གཞན་དག་ན་རེ་དེ་ལྟ་ན་ནི་འོ་ན་དེའི་གཉེན་པོ་མ་ཡིན་པའི་སེམས་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་འདོད་ཆགས་དང་བཅས་པ་ཡང་མ་ཡིན་ལ། འདོད་ཆགས་དང་བྲལ་བ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པར་འགྱུར་བས།[^2474] དེ་ལྟ་བས་ན༌[^2475]མདོ་འདིར་འདོད་ཆགས་དང་ལྡན་པས་ཀྱང་འདོད་ཆགས་དང་བཅས་པའི་སེམས་སུ་འདོད་པར་བྱ་སྟེ། གཏི་མུག་དང་བཅས་པ་དང་གཏི་མུག་དང་བྲལ་བའི་བར་དུ་ཡང་དེ་དང་འདྲ་བར་ཤེས་པར་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 3540]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས༌[^2476]ན་རེ་ཀུན་དུ་བསྡུས་པ་ནི་དམིགས་པ་ལ་མངོན་པར་སྡུད་པའི་ཕྱིར་དགེ་བ་ཡིན་ནོ། །
--- END BLOCKS ---
