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
[Block 3746]
གང་ཞིག་ཤེས་པ་དུ་དང་ལྡན། །ཞེས་བྱ་བ་འདི་བརྗོད་པར་བྱ་སྟེ། རེ་ཞིག་སོ་སོའི་སྐྱེ་བོ་ནི་ཀུན་རྫོབ་ཤེས་པ་གཅིག་པུ་དང་ལྡན་ནོ། །

[Block 3747]
འདོད་ཆགས་དང་བྲལ་བ་ཞིག་ཡིན་ན་ནི་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང་ཡང་ལྡན་ནོ། །

[Block 3748]
འཕགས་པ་ནི།

[Block 3749 [VERSE]]
ཟག་མེད་སྐད་ཅིག་དང་པོ་ལ། །
ཆགས་ཅན་ཤེས་པ་གཅིག་དང་ལྡན། །

[Block 3750]
འདོད་པ་ལས་འདོད་ཆགས་དང་མ་བྲལ་བ་ཞིག་ཡིན་ན། སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་ལ་ཀུན་རྫོབ་ཤེས་པ་གཅིག་ཁོ་ན་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 3751]
གཉིས་པ་ལ་གསུམ། སྡུག་བསྔལ་ལ༌[^2601]ཆོས་ཤེས་པ་ལ་ནི་ཀུན་རྫོབ་ཤེས་པ་དང་། ཆོས་ཤེས་པ་དང་། སྡུག་བསྔལ་ཤེས་པ་སྟེ། གསུམ་དང་ལྡན་ནོ། །

[Block 3752]
ཡན་ཆད་ནི། བཞི་ལ་རེ་རེ་འཕེལ་དང་ལྡན། །དེ་ཡན་ཆད་ཀྱི་སྐད་ཅིག་མ་བཞི་ལ་ནི། དེ་ལ་ཤེས༌[^2602]པ་རེ་རེ། འཕེལ་བར་ཤེས་པར་བྱ་སྟེ། སྡུག་བསྔལ་ལ་རྗེས་སུ་ཤེས་པ་ལ་ནི་རྗེས་སུ་ཤེས་པ་འཕེལ་ལ། ཀུན་འབྱུང་དང་། འགོག་པ་དང་། ལམ་ལ་ཆོས་ཤེས་པ་རྣམས༌[^2603]ལ་ནི་ཀུན་འབྱུང་དང་། འགོག་པ་དང་། ལམ་ཤེས་པ་རྣམས་འཕེལ་བས་ལམ་ལ་ཆོས་ཤེས་པ་ལ་ཤེས་པ་བདུན་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 3753]
འདོད་ཆགས་དང་བྲལ་བ་ཞིག་ཡིན་ན་ནི་ཐམས་ཅད་དུ་གཞན་གྱི་སེམས་ཤེས་པ་ལྷག་པར་ལྡན་པར་རིག་པར་བྱའོ། །

[Block 3754 [HEADING]]
### གནས་སྐབས་གང་དུ་ཤེས་པ་དུ་དག་འཐོབ་པ། ^4-9-0

[Block 3755]
ཡང་ན༌[^2604]གནས་སྐབས་གང་དུ་ཤེས་པ་དུ་དག་ཅིག་འཐོབ༌[^2605]ཅེ་ན།

[Block 3756 [HEADING]]
#### མཐོང་བའི་ལམ། ^4-9-1-0

[Block 3757 [VERSE]]
མཐོང་བའི་ལམ་ལ་བཟོད་པ་དང་། །
ཤེས་པ་ཇི་ལྟར་སྐྱེས་པ་རྣམས། །

[Block 3758]
མ་འོངས་པ་འཐོབ། མཐོང་བའི་ལམ་ལ་བཟོད་པའམ། ཤེས་པ་གང་དང་གང་སྐྱེས་པ་དེ་དང་འདྲ་བ་མ་འོངས་པ་དེའི་རྣམ་པ་བཞི་ཁོ་ན་འཐོབ་པར་འགྱུར་རོ། །

[Block 3759]
ཅིའི་ཕྱིར། མཐོང་བའི་ལམ་ལ་ཤེས་པ་དང་། །རྣམ་པ་འདྲ་བ་ཁོ་ན་འཐོབ་ཅེ་ན། རིགས་རྣམས་མ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3760]
དེ་ཉིད་ལས།

[Block 3761 [HEADING]]
#### མངོན་པར་རྟོགས་པའི་མཐའ་ལས་བྱུང་བ། ^4-9-2-0

[Block 3762]
རྗེས་གསུམ་ལ་ནི་ཀུན་རྫོབ་ཀྱང་།[^2606] ། མཐོང་བའི་ལམ་དེ་ཉིད་ལ་སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་དང་། འགོག་པ་ལ་རྗེས་སུ་ཤེས་པ་གསུམ་ལ་ཀུན་རྫོབ་ཤེས་པ་ཡང་འཐོབ་བོ། །

[Block 3763]
ཆོས་ཤེས་པ་ལ་ནི་མ་ཡིན་ཏེ། བདེན་པ་ཟད་པར་མངོན་པར་མ་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 3764]
དེ་ཉིད་ཀྱི་ཕྱིར༌[^2607]མངོན་རྟོགས་མཐའ་ཞེས་བྱ། དེ་ཉིད་ཀྱི་ཕྱིར་ཀུན་རྫོབ་ཤེས་པ་དེ་ནི་མངོན་པར་རྟོགས་པའི་མཐའ་ལས་བྱུང་བ༌[^2608]ཞེས་བྱ་སྟེ། བདེན་པ་རེ་རེ་མངོན་པར་རྟོགས་པའི་རྗེས་ལ་འཐོབ་པའི་ཕྱིར་རོ། །

[Block 3765]
ཅིའི་ཕྱིར་ལམ་ལ་རྗེས་སུ་ཤེས་པ་ན་འཐོབ་པར་མི་འགྱུར་ཞེ་ན། ལམ་གྱི་བདེན་པ་ནི་སྔོན་འཇིག་རྟེན་པའི་ལམ་གྱིས༌[^2609]མངོན་པར་མ་རྟོགས་པའི་ཕྱིར་དང་།[^2610] ཟད་པར་མངོན་པར་མ་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 3766]
སྡུག་བསྔལ་ཟད་པར་ཡོངས་སུ་ཤེས་པར་བྱ་བ་དང་། ཀུན་འབྱུང་སྤང་བར་བྱ་བ་དང་། འགོག་པ་མངོན་དུ༌[^2611]བྱ་བར་ནི༌[^2612]ནུས་ཀྱི། ལམ་ནི་ཟད་པར་བསྒོམ་པར༌[^2613]མི་ནུས་པས་མངོན་པར་རྟོགས་པའི་མཐའ་མེད༌[^2614]པའི་ཕྱིར། དེ་ནི༌[^2615]མངོན་པར་རྟོགས་པའི་མཐའ་ལས་བྱུང་བ་མི༌[^2616]འཐོབ་བོ། །

[Block 3767]
དེའི་ཚེ༌[^2617]ཀུན་འབྱུང་བ་ལ༌[^2618]ཡང་ཐམས་ཅད་སྤངས་པ༌[^2619]མ་ཡིན་པས་མངོན་པར་རྟོགས་པའི་མཐའ་ལས་བྱུང་བར་མི་འགྱུར་རོ་ཞེ་ན། དེའི་བདེན་པ་མཐོང་བས་སྤང་བར་བྱ་བ་ཐམས་ཅད་སྤངས་པ་ཡིན་ནོ། །

[Block 3768]
ལམ་ནི་རིགས་མང་བའི་ཕྱིར། མཐོང་བས་སྤང༌[^2620]བའི་གཉེན་པོར༌[^2621]ཐམས་ཅད་བསྒོམ་པར་མི་ནུས་པས་ཁྱད་པར་ཆེར་ཡོད་དོ། །

[Block 3769]
གཞན་དག་ན་རེ་མཐོང་བའི་ལམ་གྱི༌[^2622]འཁོར་ཡིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ།[^2623] །འདི་ནི་བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་ཤེས་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 3770]
ཅི་ཀུན་རྫོབ་ཤེས་པ་མངོན་པར་རྟོགས་པའི་མཐའ་ལས་བྱུང་བ་དེ་རེས་འགའ་མངོན་སུམ་དུ་བྱེད་དམ་ཞེ་ན། ནམ་ཡང་མི་བྱེད་དེ། གཅིག་ཁོ་ནར་དེ་ནི་མི་སྐྱེ་བའི་ཆོས་ཅན་ཡིན། ཇི་ལྟར་ན་དེ་ཐོབ་པ༌[^2624]ཡིན་ཏེ། མ་རྙེད་པ་ལས་རྙེད་པའི་ཕྱིར་རོ། །

[Block 3771]
ད༌[^2625]ནི་གལ་ཏེ་དེ་མངོན་སུམ་དུ་བྱ་བ་མི་ནུས་པ་ཁོ་ན་ཡིན་ན་ཇི་ལྟར་ན་དེ་རྙེད་པ་ཡིན། ཐོབ་པའི་སྒོ་ནས་སོ། །

[Block 3772]
གང་གི་ཕྱིར་རྙེད་པ་དེའི་ཕྱིར་རྙེད་དོ་ཞེས་སྟོན་པ་འདི་ནི་སྔོན་མ་བྱུང་བའི་རྣམ་པ་ཡིན་ནོ། །

[Block 3773]
དེ་ལྟ་བས་ན་དེ་ལྟ་ན༌[^2626]ནི་ཐོབ་པ་མི་འགྲུབ་པ༌[^2627]ཉིད་ཀྱིས་སྔོན༌[^2628]གྱི་སློབ་དཔོན་དག་ཇི་སྐད་ཟེར་བ་དེ་ལྟ་ན་འགྲུབ་པར་འགྱུར་རོ། །

[Block 3774]
སྔོན་གྱི་སློབ་དཔོན་དག་ཇི་སྐད་ཟེར་ཞེ་ན། འཇིག་རྟེན་ལས་འདས་པའི་ལམ་གྱི༌[^2629]མཐུས་དེ་ལས་ལངས་ནས་འཇིག་རྟེན་པའི་ཤེས་པ་ཆེས་ཁྱད་པར་དུ་འཕགས་པ་བདེན་པ་ལ་དམིགས་པ༌[^2630]མངོན་སུམ་དུ་བྱེད་པར་འགྱུར་བ༌[^2631]ཀུན་རྫོབ་ཤེས་པ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3775]
དེ་མངོན་སུམ་དུ་འགྱུར་བར་ནུས་པའི་རྟེན་རྙེད་པ་གང་ཡིན་པ་དེ་ཉིད་རྙེད་པ་ཡིན་ཏེ། རིགས་རྙེད་ན་རིགས་ལས་བྱུང་བ་ཡང་རྙེད་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3776]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་འདི་མི་འདོད་དོ། །

[Block 3777]
ས་དུ་པའི་ཀུན་རྫོབ་ཤེས་པ་དེ་འཐོབ་ཅེ་ན།[^2632] མཐོང་བའི་ལམ་གྱིས་ནི། རང་དང་འགོག་པ༌[^2633]མཐོང་བའི་ལམ་ལས་ས་གང་པ༌[^2634]ཡིན་པ་ས་དེ་པ་དང་། ས་འོག་མ་པའི་ཀུན་རྫོབ་ཤེས་པ་འཐོབ༌[^2635]པ་སྟེ། གལ་ཏེ་མཐོང་བའི་ལམ༌[^2636]མི་ལྕོགས་པ་མེད་པའི་ས་པ་ཞིག་ཡིན་ན་ནི། མི་ལྕོགས་པ་མེད་པའི་ས་པ་དང་། འདོད་པ་ན་སྤྱོད་པ་དང་། ས་གཉིས་པ༌[^2637]ཐོབ་ལ། དེ་བཞིན་དུ་མཐོང་བའི་ལམ། བསམ་གཏན་བཞི་པའི་ས་པ་ཡིན་ན་ས་བདུན་པའི་ཀུན་རྫོབ་ཤེས་པ་ཐོབ་པའི་བར་དུའོ། །

[Block 3778]
དེ་ཡང་དྲན་པ་ཉེ་བར་གཞག་པ་དུ་དག་ཅིག་ཡིན་ཞེ་ན། འགོག་པའི་མཐའ། འགོག་པའི༌[^2638]མངོན་པར་རྟོགས་པའི་ཀུན་རྫོབ་ཤེས་པ་གང་ཡིན་པ་དེ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་ཐ་མ་སྟེ། ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་ཡིན་ནོ། །

[Block 3779]
གཅིག་གྲངས༌[^2639]བཅད་པས་ལྷག་མ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ཆར་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པ་ཡིན་ནོ། །

[Block 3780]
ཀུན་རྫོབ་ཤེས་པ་མངོན་པར་རྟོགས་པའི་མཐའ་ལས་བྱུང་བ་དེ་ནི་རང་བདེན་རྣམས༌[^2640]ཅན། བདེན་པ་གང་ཞིག་མངོན་པར་རྟོགས་པའི་འཐོབ་པ་བདེན་པ་དེའི་རྣམ་པ་ཅན་ཁོ་ན་ཡིན་ནོ། །

[Block 3781]
དེའི་རྣམ་པ་ཅན་ཡིན་ནོ། །ཞེས་སྨོས་པས་འདིའི་དམིགས་པ་ཡང་བདེན་པ་དེ་ཉིད་ཡིན་ནོ་ཞེས་བཤད་པ་ཡིན་ནོ། །

[Block 3782]
དེ་ནི༌[^2641]མཐོང་བའི་ལམ་གྱིས་འཐོབ༌[^2642]པར་བྱ་བ་ཡིན་པའི་ཕྱིར་འབད་ལས་བྱུང་བ་སྦྱོར་བ་ལས་བྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3783]
འཁོར་དང་བཅས་པ་ལ་སོགས་པ་སྨོས་པའི་ཕྱིར། འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པ༌[^2643]ནི་ཕུང་པོ་བཞི་དང་ལྔའི་རང་བཞིན་ཡིན་ནོ། །

[Block 3784 [HEADING]]
#### བཅུ་དྲུག་པ་ལམ་ལ་རྗེས་སུ་ཤེས་པ། ^4-9-3-0

[Block 3785]
ཆགས་བཅས་བཅུ་དྲུག་པ་ལ་དྲུག །འཐོབ་ཅེས་བྱ་བར་སྦྱར་ཏེ། འདོད་ཆགས་དང་མ༌[^2644]བྲལ་བ་ནི་བཅུ་དྲུག་པ་ལམ་ལ་རྗེས་སུ་ཤེས་པ་ལས་ཤེས་པ༌[^2645]གཉིས་ད་ལྟར༌[^2646]བྱུང་བ་ཡིན་ལ། མ་འོངས་པ་དྲུག་འཐོབ༌[^2647]སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། སྡུག་བསྔལ་དང་ཀུན་འབྱུང་དང་འགོག་པ་དང་། ལམ་ཤེས་པ་རྣམས་སོ། །
--- END BLOCKS ---
