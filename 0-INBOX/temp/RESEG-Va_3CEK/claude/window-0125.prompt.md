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
[Block 4376]
དེ་ནི་འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བས་འཐོབ་ལ། ཚངས་པའི་འཇིག་རྟེན་ལས་འདོད་ཆགས་དང་བྲལ་བས་འདོར་རོ། །

[Block 4377]
ཚངས་པའི་འཇིག་རྟེན་ལས་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་པ་ལས་འཐོབ་ལ། འདོད་པ་ལ་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་པ་ལས་འདོར་རོ། །

[Block 4378]
གང༌[^3157]ནས་ཚངས་པའི་འཇིག་རྟེན་དུ་སྐྱེ་བ་ན་འཐོབ་ལ། དེས་ན་འདོད་པའི་ཁམས་སུ་སྐྱེ་བ་ན་འདོར་རོ༌[^3158]ཞེས་འབྱུང་ངོ་། །

[Block 4379 [HEADING]]
#### ཟག་མེད་འཐོབ་པ། ^5-2-2-0

[Block 4380 [VERSE]]
ཟག་མེད་འདོད་ཆགས་བྲལ་བ་ཡིས། །
དེ་དང་མི་ལྡན་པ་ལས་འཐོབ། །

[Block 4381]
ཅེས་བྱ་བར་སྦྱོར༌[^3159]རོ། །

[Block 4382]
དེ་དང་ལྡན་པ་ནི་ཟད་པ་ཤེས་པ་ལས་ཀྱང་མི་སློབ་པ་འཐོབ་ལ། དབང་པོ་འཕོ་བ་ལས་ཀྱང་སློབ་པ་དང་མི་སློབ་པ་འཐོབ་བོ། །

[Block 4383]
ངེས་པར་འཇུག་པ་ལས་ཀྱང་དང་པོ་ཉིད་དུ་ཟག་པ་མེད་པ་འཐོབ་པ་མ་ཡིན་ནམ་ཞེ་ན། མཐར་གྱིས་པས་མི་འཐོབ་པའི་ཕྱིར་གདོན་མི་ཟ་བ་ཡིན་ཏེ། ཇི་ལྟར་གདོན་མི་ཟ་བར་འཐོབ་པ་དེ་ལྟར་བཤད་དོ། །

[Block 4384 [HEADING]]
#### ཉོན་མོངས་ཅན་འཐོབ་པ། ^5-2-3-0

[Block 4385]
ཉོན་མོངས་ཅན་ཉམས་སྐྱེ་བ་ཡིས།[^3160] །དེ་དང་མི་ལྡན་པ་ལས་འཐོབ། །ཅེས་བྱ་བ་ཁོ་ནར་སྦྱར་ཏེ། གལ་ཏེ་དེ༌[^3161]ལས་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་ན་ཡོངས་སུ༌[^3162]ཉམས་པ་ལས་འཐོབ་བོ། །

[Block 4386]
གལ་ཏེ་ས་གོང་མ་ལས་ན་ས་འོག་མར་སྐྱེས༌[^3163]ན་སྐྱེ་བས་འཐོབ་བོ། །

[Block 4387 [HEADING]]
### སྙོམས་པར་འཇུག་པའི་རྫས་ཀྱི་མཇུག་ཐོགས་སུ་སྐྱེ་བ། ^5-3-0

[Block 4388]
སྙོམས་པར་འཇུག་པའི་རྫས་གང་གི་མཇུག་ཐོགས་སུ་དུ་ཞིག་སྐྱེ་ཞེ་ན། ཟག་པ་མེད་པའི་བསམ་གཏན་དང་པོའི་མཇུག་ཐོགས་སུ་དྲུག་སྐྱེ་སྟེ། རང་གི་ས་པ་དང་བསམ་གཏན་གཉིས་པ་དང་གསུམ་པའི་ས་པའི་དག་པ་པ་དང་ཟག་པ་མེད་པ་གཞན༌[^3164]དག་གོ། །

[Block 4389]
ཅི་ཡང་མེད་པའི༌[^3165]སྐྱེ་མཆེད་ཀྱི་མཇུག་ཐོགས་སུ་བདུན་ཏེ་རང་གི་ས་པ༌[^3166]དང་རྣམ་ཤེས་དང་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ཀྱི་ས་པའི་དག་པ་པ་དང་ཟག་པ་མེད་པ་དང་། སྲིད་པའི་རྩེ་མོའི༌[^3167]དག་པ༌[^3168]ཁོ་ན་སྟེ། ཟག་པ་མེད་པ་མེད་པའི༌[^3169]ཕྱིར་རོ། །

[Block 4390]
བསམ་གཏན་གཉིས་པའི་མཇུག་ཐོགས་སུ༌[^3170]བརྒྱད་དེ། རང་གི་ས་པ་དང་བསམ་གཏན་གསུམ་པ་དང་།

[Block 4391]
བཞི་པ་དང་། དང་པོའི་ས་པའི་དག་པ་པ་དང་ཟག་པ་མེད་པ་དག་གོ།[^3171] །རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་ཀྱི་མཇུག་ཐོགས་སུ་དགུ་སྟེ། རང་གི་ས་པ༌[^3172]གཉིས་དང་། ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་དང་བསམ་གཏན་བཞི་པའི་ས་པ་བཞི་དང་། ཅི་ཡང་མེད་པ་དང་སྲིད་པའི་རྩེ་མོའི་ས་པ་གསུམ་མོ། །

[Block 4392]
དེ་བཞིན་དུ་བསམ་གཏན་དང་གཟུགས་མེད་པ་གཞན་གྱི་མཇུག་ཐོགས་སུ་ཡང༌[^3173]རྫས་བཅུ༌[^3174]སྦྱར་བར་བྱའོ། །

[Block 4393]
འདི་ནི་མདོར་བསྡུ་བ་ཡིན་ཏེ། ཟག་པ་མེད་པའི་མཇུག་ཐོགས་སུ། ལྟག་འོག་གསུམ་པའི་བར་དགེ་བ་སྐྱེ་བའོ། །

[Block 4394]
དགེ་བ་སྨོས་པ༌[^3175]ནི་དག་པ་པ་དང་། ཟག་པ་མེད་པ་གཟུང་སྟེ། དགེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4395]
ཟག་པ་མེད་པའི་སྙོམས་པར་འཇུག་པའི་རྫས་ཀྱི་མཇུག་ཐོགས་སུ་རང་གི་ས་པ་དང་ས་གོང་མ་དང་། འོག་མ་ས༌[^3176]གསུམ་པའི་བར་གྱི་དག་པ་པ༌[^3177]དང་ཟག་པ་མེད་པ་སྐྱེ་སྟེ། ཐོད་རྒལ་དུ་སྙོམས་པར་འཇུག་པར་བྱེད་པས་གསུམ་པ་ལས་ཕན་ཆད་དུ་ནི་རྒལ་བར་མི་ནུས་སོ། །

[Block 4396]
རྗེས་སུ་ཤེས་པའི་མཇུག་ཐོགས་སུ་གཟུགས་མེད་པ་ལ་སྙོམས་པར་འཇུག་གི་ཆོས་ཤེས་པའི་མཇུག་ཐོགས་སུ་ནི་མ་ཡིན་ཏེ། དེའི་རྟེན་དང་དམིགས་པ་འོག་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4397]
ཇི་ལྟར་ཟག་པ་མེད་པའི་མཇུག་ཐོགས་སུ་བཤད་པ་ལྟར་དག་པ་ལས་དེ་བཞིན། རིག་པར་བྱ་ལ། རང་གི་ས་པའི་ཉོན་མོངས་ཀྱང་། །དག་པ་པའི་མཇུག་ཐོགས་སུ་ལྷག་པར་རང་གི་ས་པའི་ཉོན་མོངས་པ་ཅན་སྐྱེའོ། །

[Block 4398]
ལྷག་མ་ནི་ཟག་པ་མེད་པ་ལས་བཤད་པ་ཇི་ལྟ༌[^3178]བ་བཞིན་ནོ། །

[Block 4399]
ཟག་པ་མེད་པའི་མཇུག་ཐོགས་སུ་ནི་ཉོན་མོངས་པ་ཅན་སྐྱེ་བ་མེད་དོ། །

[Block 4400]
ཉོན་མོངས་ཅན་ལས་རང་དག་དང་། །ཉོན་མོངས༌[^3179]པ་ཅན་གྱི་སྙོམས་པར་འཇུག་པའི་རྫས་ཀྱི་མཇུག་ཐོགས་སུ་ནི་རང་གི་ས་པའི་དག་པ་པ་དང་ཉོན་མོངས་པ་ཅན་དག་སྐྱེའོ། །

[Block 4401]
འོག་མའི་དག་ཅིག་ཀྱང་། ཉོན་མོངས་པས་གཟིར་བ༌[^3180]ནི་འོག་མའི་སྙོམས་པར་འཇུག་པའི༌[^3181]དག་པ་པ་ལ་ཡང་དགའ་བར་འགྱུར་རོ། །

[Block 4402]
གལ་ཏེ་ཉོན་མོངས་པ་ཅན་ཡོངས་སུ་བཅད་ནས་འོག་མར་འཕོ་ན་ནི་དགེ་བ་ལས་འཕོས་པ་ཡིན་གྱི་ཉོན་མོངས་པ་ཅན་ལས་ནི་མ་ཡིན་ནོ། །

[Block 4403]
འོན་ཏེ་ཡོངས་སུ་མ་བཅད་ན་ནི་ཇི་ལྟར་འཕོ་ཞེ་ན། སྔོན་འཕངས་པའི་ཕྱིར་ཏེ། སྔོན་འདི་སྙམ་དུ་འོག་མའི་དག་པ་པ་ནི་བླའི༌[^3182]གོང་མའི་ཉོན་མོངས་པ་ཅན་ནི་མ་ཡིན་ནོ་སྙམ་དུ་འདོད་པར་འགྱུར་ལ། སྔོན་གྱི༌[^3183]བསམ་པ་ཡང་སེམས་ཅན་རྣམས་ཀྱི་རྒྱུན་གྱི་རྗེས་སུ་འབྲངས༌[^3184]ཏེ། བསམས་ནས་གཉིད་ལོག་པར་འདོད་པའི་དུས་སུ་སད་པ་བཞིན་ནོ། །

[Block 4404]
ཟག་པ་མེད་པ་ནི་ཉོན་མོངས་པ་ཅན་གྱི་མཇུག་ཐོགས་སུ་རྣམ་པ་ཐམས་ཅད་དུ་མི་སྐྱེའོ། །

[Block 4405]
སྙོམས་པར་འཇུག་པའི་དུས་ཀྱི་ཕྱིར་དག་པ་པ་དང་། ཉོན་མོངས་པ་ཅན་གྱི་མཇུག༌[^3185]ཐོགས་སུ་རང་གི་ས་པའི་ཉོན་མོངས་པ་ཅན་ཁོ་ན་སྐྱེའི་གཞན་གྱི་ས་པ་ནི་མ་ཡིན་ནོ་ཞེས་དེ་སྐད་དུ་བཤད་ཀྱི། འཆི་འཕོ༌[^3186]དག་ལས་ཉོན་མོངས་ཀུན། །འཆི་འཕོ་བའི་ཚེ་སྐྱེ་བས༌[^3187]ཐོབ་པའི་དག་པ་པའི་མཇུག་ཐོགས་སུ་ས༌[^3188]ཐམས་ཅད་པའི་ཉོན་མོངས་པ་ཅན་སྐྱེའོ། །

[Block 4406]
ཉོན་མོངས་ཅན་ལས་གོང་མ་མིན། །འཆི་འཕོ་བའི་ཚེ་ཉོན་མོངས་པ་ཅན་གྱི་བསམ་གཏན་དང་གཟུགས་མེད་པའི་མཇུག་ཐོགས་སུ་རང་གི་ས་པ་དང་ས༌[^3189]འོག་མ་པའི་ཉོན་མོངས་པ་ཅན་སྐྱེའི་ས་གོང་མ་པ་ནི་མ་ཡིན་ནོ། །

[Block 4407]
དག་པ་པ་ཐམས་ཅད་ལས་ཟག་པ་མེད་པའི་སྙོམས་པར་འཇུག་པའི་རྫས་སྐྱེ་བ་ཡང་མ་ཡིན་ནོ། །

[Block 4408 [HEADING]]
### དག་པ་པ་རྣམ་པ་བཞི། ^5-4-0

[Block 4409]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། དག་པ་ཉམས་པའི་ཆ་མཐུན་སོགས། །རྣམ་བཞི། དག་པ་པ་ནི་ཉམས་པའི་ཆ་དང་མཐུན་པ་དང་། གནས་པའི་ཆ་དང་མཐུན་པ་དང་། ཁྱད་པར་གྱི་ཆ་དང་མཐུན་པ་དང་། ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་དང་། རྣམ་པ་བཞིའོ། །

[Block 4410]
སྲིད་པའི་རྩེ་མོ་ན་ནི་རྣམ་པ་གསུམ་ཡིན་ཏེ། ཁྱད་པར་གྱི་ཆ་དང་མཐུན་པ་མ་གཏོགས་སོ། །

[Block 4411]
འདིའི་མཚན་ཉིད་ཅི་ཞེ་ན། དེ་ནི་གོ་རིམས་བཞིན་དུ།

[Block 4412 [VERSE]]
ཉོན་མོངས་སྐྱེ་དང་རང་ས་དང་། །
གོང་དང་ཟག་མེད་རྗེས་མཐུན་པའོ། །

[Block 4413 [HEADING]]
#### ཉམས་པའི་ཆ་དང་མཐུན་པ། ^5-4-1-0

[Block 4414]
ཉམས་པའི་ཆ་དང་མཐུན་པ་ནི་ཉོན་མོངས་པ་སྐྱེ་བ་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 4415 [HEADING]]
#### གནས་པའི་ཆ་དང་མཐུན་པ། ^5-4-2-0
--- END BLOCKS ---
