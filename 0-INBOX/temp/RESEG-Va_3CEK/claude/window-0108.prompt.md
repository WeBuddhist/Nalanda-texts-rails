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

[Block 3786]
འདོད་ལ་ཆགས་དང་བྲལ་བས་བདུན། །འདོད་ཆགས་དང་བྲལ་བས་ནི་བདུན་པ༌[^2648]ཕ་རོལ་གྱི་སེམས་ཤེས་པ༌[^2649]འཐོབ་བོ། །

[Block 3787 [HEADING]]
#### བསྒོམ་པའི་ལམ། ^4-9-4-0

[Block 3788 [VERSE]]
དེ་ཡི་གོང་མ་ཆགས་བཅས་ཀྱི། །
བསྒོམ་པའི༌[^2650]ལམ་ལ་བདུན་འཐོབ་པོ། །

[Block 3789]
སྐད་ཅིག་མ་བཅུ་དྲུག་གི་གོང་མའི༌[^2651]བསྒོམ་པའི་ལམ་ལ་ནི་ཇི་སྲིད་དུ་འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་མ་ཡིན་པ་དེ་སྲིད་དུ་སྦྱོར་བ་དང་། བར་ཆད་མེད་པ་དང་། རྣམ་པར་གྲོལ་བ་དང་། ཁྱད་པར་ཅན་གྱི་ལམ་ཐམས་ཅད་ལ་ཤེས་པ་བདུན་འཐོབ་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་བ་དང་། འགོག་པ་དང་། ལམ་དང་ཀུན་རྫོབ་ཤེས་པ་རྣམས་སོ། །

[Block 3790]
གལ་ཏེ་བསྒོམ་པའི༌[^2652]ལམ་འཇིག་རྟེན་པ་ཞིག་ཡིན་ན་ནི་ཀུན་རྫོབ་ཤེས་པ་ད་ལྟར་བྱུང་བ་ཡིན་ནོ། །

[Block 3791]
གལ་ཏེ་འཇིག་རྟེན༌[^2653]ལས་འདས་པ་ཞིག་ཡིན་ན་ནི། ཆོས་ཤེས་པ་བཞི་ལས་གང་ཡང་རུང་བ་ཞིག་ད་ལྟར་བྱུང་བ་ཡིན་ནོ། །

[Block 3792 [VERSE]]
ས་བདུན་ལས་རྒྱལ་མངོན་ཤེས་དང་། །
མི་གཡོ་འཐོབ་དང་སྤེལ་བསྒོམས་པའི། །
བར་ཆད་མེད་པའི་ལམ་དག་དང་། །
གོང་མའི་གྲོལ༌[^2654]བའི་ལམ་བརྒྱད་ལའང་། །

[Block 3793]
ཤེས་པ་བདུན་འཐོབ་བོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ས་བདུན་ནི་བསམ་གཏན་བཞི་དང་། གཟུགས་མེད་པ་གསུམ་མོ། །

[Block 3794]
དེ་དག་ལས༌[^2655]རྒྱལ་བ་ནི་འདོད་ཆགས་དང་བྲལ་བ་སྟེ། སློབ་པ་ས༌[^2656]བདུན་པོ་དེ་དག་ལས་འདོད་ཆགས་དང་བྲལ་བ་དང་། མངོན་པར་ཤེས་པ་ལྔ༌[^2657]དང་། མི་གཡོ་བ༌[^2658]རྟོགས་པར་བྱེད་པ་དང་། བསམ་གཏན་སྤེལ་མར་བསྒོམ་པའི་བར་ཆད་མེད་པའི་ལམ་ཇི་སྙེད་པ་དེ་དག༌[^2659]ཐམས་ཅད་ལ་ཤེས་པ་བདུན་འཐོབ༌[^2660]སྟེ། དེ་དག་ཉིད་དོ། །

[Block 3795]
གལ་ཏེ་བསྒོམ་པའི་ལམ་འཇིག་རྟེན་པ་ཞིག་ཡིན་ན་ནི། ཀུན་རྫོབ་ཤེས་པ་ད་ལྟར་བྱུང་བ་ཡིན་ནོ། །

[Block 3796]
འཇིག་རྟེན་ལས་འདས་པ་ཞིག་ཡིན་ན་ནི་རྗེས་སུ་ཤེས་པ་བཞི་དང་ཆོས་ཤེས་པ་གཉིས་ལས་གང་ཡང་རུང་བ་ཞིག་ད་ལྟར་བྱུང་བ་ཡིན་ནོ། །

[Block 3797]
མི་གཡོ་བ༌[^2661]རྟོགས་པར་བྱེད་པ་ལ་ནི་ཀུན་རྫོབ་ཤེས་པ་མི་འཐོབ་སྟེ། སྲིད་པའི་རྩེ་མོའི་གཉེན་པོ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3798]
དེར་ནི་ཟད་པ་ཤེས་པ་བདུན་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3799]
ས་བདུན་ལས་འདོད་ཆགས་དང་བྲལ་བའི་ཡང་གོང་མ་སྲིད་པའི་རྩེ་མོ་ལས་འདོད་ཆགས་དང་བྲལ་བའི་རྣམ་པར་གྲོལ་བའི་ལམ་བརྒྱད་ལ༌[^2662]ཡང་ཤེས་པ་བདུན་ཁོ་ན་འཐོབ་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་དང་། འགོག་པ་དང་། ལམ་དང་། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་རྣམས་སོ། །

[Block 3800]
ཀུན་རྫོབ་ཤེས་པ་ནི་མི་འཐོབ་སྟེ། སྲིད་པའི་རྩེ་མོའི་གཉེན་པོ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3801]
རྗེས་སུ་ཤེས་པ་རྣམ་པ༌[^2663]བཞི་དང་། ཆོས་ཤེས་པ་རྣམ་པ༌[^2664]གཉིས་ལས་གང་ཡང་རུང་བ་ཞིག་ད་ལྟར་བྱུང་བ་ཡིན་ནོ། །

[Block 3802 [VERSE]]
སློབ་པ་སྦྱོང་བའི་གྲོལ་བ་ལ། །
ཤེས་པ༌[^2665]དྲུག་དང་བདུན་འཐོབ་བམ། །

[Block 3803]
སློབ་པ་འདོད་ཆགས་དང་བཅས་པས་ནི་དབང་པོ་སྦྱོང་བའི་རྣམ་པར་གྲོལ་བའི་ལམ་ལ་དྲུག་འཐོབ་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། སྡུག་བསྔལ་བ༌[^2666]དང་། ཀུན་འབྱུང་བ་དང་། འགོག་པ་དང་། ལམ་ཤེས་པ་རྣམས་སོ། །

[Block 3804]
འདོད་ཆགས་དང་བྲལ་བས་ནི་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་བསྣན་ཏེ། བདུན་འཐོབ༌[^2667]བོ། །

[Block 3805]
འམ་ཞེས་བྱ་བའི་སྒྲ་ནི་ཁ་ཅིག་ན་རེ༌[^2668]གཉི་གས་ཀུན་རྫོབ་ཤེས་པ་ཡང་འཐོབ་བོ་ཞེས་ཟེར་བའི་ལུགས་ཐ་དད་པ་ཤེས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3806]
སྦྱོར་བའི་ལམ་ལ་ནི་དེ་གཉིས༌[^2669]ཀྱིས་ཀུན་རྫོབ་ཤེས་པ་ཡང་འཐོབ་བོ། །

[Block 3807]
བར་ཆད་མེད་པའི་ལམ་ལ་དྲུག །སློབ་པ་འདོད་ཆགས་དང་བྲལ་བ་ཡང་རུང་། འདོད་ཆགས་དང་མ་བྲལ་བ་ཡང་རུང་། དབང་པོ་སྦྱོར་བའི༌[^2670]བར་ཆད་མེད་པའི་ལམ་ལ་དྲུག་འཐོབ་སྟེ། སྔ་མ་བཞིན་ནོ། །

[Block 3808]
ཀུན་རྫོབ་ཤེས་པ་ནི་མ་ཡིན་ཏེ། མཐོང་བའི་ལམ་དང་འདྲ་བའི་ཕྱིར། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ཡང་མ་ཡིན་ཏེ། བར་ཆད་མེད་པའི་ལམ་ཐམས་ཅད་ལ་བཀག་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་བཀག་པ་ཅི་ཞེ༌[^2671]ན། གཉེན་པོ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3809]
དེ་བཞིན་སྲིད་རྩེའི་རྣམ་རྒྱལ་ལ།[^2672] །སྲིད་པའི་རྩེ་མོ་ལས་འདོད་ཆགས་དང་བྲལ་བའི་བར་ཆད་མེད་པའི་ལམ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་དྲུག་འཐོབ་བོ། །

[Block 3810]
ཟད་པ་ཤེས་པ་ལ་དགུའོ། །

[Block 3811]
སྲིད་པའི་རྩེ་མོ་ལས༌[^2673]འདོད་ཆགས་དང་བྲལ་བ་ལ༌[^2674]རྣམ་པར་གྲོལ་བའི༌[^2675]ལམ་དགུ་པ་ནི་ཟད་པ་ཤེས་པ་ཡིན་ཏེ། དེ་ལ་མི་སྐྱེ་བ་ཤེས་པ་མ་གཏོགས་པ་ཤེས་པ་དགུ་འཐོབ་པོ། །མི་གཡོ་བས་ནི་བཅུ་འཐོབ་བོ། །

[Block 3812]
མི་གཡོ་བའི་ཆོས་ཅན་གང་ཡིན་པ་དེས་ནི་བཅུ་འཐོབ་སྟེ།

[Block 3813 [VERSE]]
མི་སྐྱེ་བ་ཤེས་པ་འཐོབ་པའི་ཕྱིར་རོ། །
དེར་འཕོ་བའི་གྲོལ་བ་ཐ་མ་ལའང་། །

[Block 3814]
གང་ཞིག་མི་གཡོ་བ་ཉིད་དུ་འཕོ་བ་དེའི་རྣམ་པར་གྲོལ་བའི་ལམ་ཐ་མ་ལ་ཡང་བཅུ་འཐོབ་བོ། །

[Block 3815]
བཤད་པའི་ལྷག་མ་ལ༌[^2676]བརྒྱད་འཐོབ་བོ། །

[Block 3816]
ལྷག་མ་ཡང་གང་ཞིག་ཅེ་ན། འདོད་པའི་ཁམས་ལས་འདོད་ཆགས་དང་བྲལ་བའི་རྣམ་པར་གྲོལ་བའི་ལམ་དགུ་པ་དང་། ས་བདུན་ལས་འདོད་ཆགས་དང་བྲལ་བ་དང་། མངོན་པར་ཤེས་པ་དང༌[^2677]སྤེལ་མར་བསྒོམ་པ༌[^2678]དག་གིས༌[^2679]རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་དང་། མི་གཡོ་བ་རྟོགས་པར་བྱེད་པའི་རྣམ་པར་གྲོལ་བའི་ལམ་བརྒྱད་དང་། འདོད་ཆགས་དང༌[^2680]བྲལ་བའི་སྦྱོར་བ་དང་། ཁྱད་པར་ཅན་གྱི་ལམ་ཐམས་ཅད་དེ། དེ་དག་ཐམས་ཅད་ལ་ནི་ཟད་པ་དང་། མི་སྐྱེ་བ་ཤེས་པ་མ་གཏོགས་པ༌[^2681]ཤེས་པ་བརྒྱད་མ་འོངས་པ་འཐོབ་པས་འཐོབ་པ༌[^2682]སྟེ། སློབ་པ་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3817 [HEADING]]
#### མི་སློབ་པ། ^4-9-5-0

[Block 3818]
མི་སློབ་པའི་མངོན་པ༌[^2683]ཤེས་པ་ལ་སོགས་པའི་སྦྱོར་བ་དང་། རྣམ་པར་གྲོལ་བ་དང་། ཁྱད་པར་ཅན་གྱི་ལམ་རྣམས་ལ་ཤེས་པ་དགུའམ་བཅུ་འཐོབ་པོ། །མངོན་པར་ཤེས་པ་དང་སྤེལ་མར་བསྒོམ་པའི་བར་ཆད་མེད་པའི་ལམ་རྣམས་ལ་ནི་བརྒྱད་དམ་དགུ་འཐོབ་པོ། །མངོན་པར་ཤེས་པའི་རྣམ་པར་གྲོལ་བའི་ལམ་གཉིས་ནི་ལུང་དུ་མ་བསྟན་པའི་ཕྱིར་མ་འོངས་པ་ཅུང་ཟད་ཀྱང་མི་འཐོབ་བོ། །

[Block 3819 [HEADING]]
#### སོ་སོའི་སྐྱེ་བོ། ^4-9-6-0

[Block 3820]
སོ་སོའི་སྐྱེ་བོ༌[^2684]ནི་འདོད་པ་དང་། བསམ་གཏན་གསུམ་ལས་འདོད་ཆགས་དང་བྲལ་བའི་རྣམ་པར་གྲོལ་བའི་ལམ་ཐ་མ་རྣམས་དང་། བསམ་གཏན་གྱི་ས་པ་དག་གི་སྦྱོར་བ་རྣམས་དང་། མངོན་པར་ཤེས་པ་གསུམ་གྱི་རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་དང་། ཚད་མེད་པ་ལ་སོགས་པའི་ཡོན་ཏན་མངོན་པར་སྒྲུབ་པ༌[^2685]རྣམས་ལ༌[^2686]ཀུན་རྫོབ་ཤེས་པ་མ་འོངས་པ་དང་། ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་དག་གི་སྦྱོར་བ་རྣམས་དང་། མངོན་པར་ཤེས་པ་གསུམ་གྱི༌[^2687]རྣམ་པར་གྲོལ་བ་མ་གཏོགས་པ་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ཡང་འཐོབ་བོ། །
--- END BLOCKS ---
