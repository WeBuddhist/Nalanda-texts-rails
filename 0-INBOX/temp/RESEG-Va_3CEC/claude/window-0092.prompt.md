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
[Block 3221]
ཤེས་རབ་ཀྱིས་འདུས་མ་བྱས་སྤོང་བ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱིས༌[^2782]འདུས་མ་བྱས་རྟོགས༌[^2783]ཀྱང་། ཐབས་ཀྱིས་ཟིན་པས་འདུས་མ་བྱས་ཀྱི༌[^2784]དབྱིངས་ལ་མི་གནས་ཤིང་འདུས་བྱས་ཀྱི༌[^2785]བྱ་བ་རྣམས་ཀྱང་བྱེད་པའོ། །

[Block 3222]
བྱམས་པས་དཔུང་གཉེན་མེད་པ་རྣམས་ཀྱི་སྐྱབས་ཞེས་བྱ་བ་ནི་ངན་སོང་གི་སྡུག་བསྔལ་མྱོང་བ་དང་རྣམ་པར་གྲོལ་བ་མཐོང་བ་ནི་དཔུང་གཉེན་མེད་པ་སྟེ། དེ་དག་སྐྱེ་འགྲོ༌[^2786]དང་རྣམ་པར་གྲོལ་བའི་བདེ་བ་ཐོབ་པའི་སྐྱབས་བྱེད་པ་ནི་ཐབས་སོ། །

[Block 3223]
སྙིང་རྗེས་འཁོར་བ་ལ་མི་སྨོད་ཅེས་བྱ་བ་ལ། སེམས་ཅན་གྱི་སྡུག་བསྔལ་སེལ་བར་བྱེད་པའི་སྙིང་རྗེས་འཁོར་བ་སྡུག་བསྔལ་གྱི་གནས་ཡིན་ཡང་སྨོད་པར་མི་བྱེད་པ་ནི་ཐབས་སོ། །

[Block 3224]
དགའ་བས་དགའ་བ་དང་མི་དགའ་བ་ལ༌[^2787]མི་འབྱེད་པ་ཞེས་བྱ་བ་ལ། ཆོས་ཀྱི་ཀུན་དགའ་ལ་དགའ་བ་དང་། འཁོར་བའི་རང་བཞིན་སྡུག་བསྔལ་ཞིང་མི་དགའ་བ་ཅན་ཡིན་ཡང་ཐབས་ཀྱི་དབང་གིས་དེ་ལ་ཇི་མི་སྙམ་པ་ནི་ཐབས་སོ། །

[Block 3225]
བཏང་སྙོམས་ཀྱིས༌[^2788]དགེ་བའི་རྩ་བ་དང་། ཚོགས་ཐམས་ཅད་འཕེལ་ཞེས་བྱ་བ་ལ།

[Block 3226]
བཏང་སྙོམས་ཀྱི་རང་བཞིན་ཇི་འང་མི་སྤྱོད་པ་ཡིན་པ་ལས།

[Block 3227]
ཐབས་ཀྱི་དབང་གིས་བཏང་སྙོམས་ཀྱི་དུས་ན་བཏང་སྙོམས་ལས་ཀྱང་མ་ཉམས་ལ། དགེ་བའི་རྩ་བ་དང་། བསོད་ནམས་དང་། ཡེ་ཤེས་ཀྱི་ཚོགས་འཕེལ་བར་བྱེད་པའི་སྤྱོད་པ་ཡང་མི་གཏོང་བའོ། །

[Block 3228]
ལྷའི་མིག་གིས་སངས་རྒྱས་ཀྱི་སྤྱན་ཐོབ་པ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ལྷའི་མིག་གིས་སངས་རྒྱས་ཀྱི་སྤྱན་ཐོབ་པ་ཡང་ཐབས་ཏེ། ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 3229]
ཐབས་ནི་སེམས་ཅན་དག་གི་བསམ་པ་རྣམས་ལ་འཇུག་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གྱི་བསམ་པ་དང་། བག་ལ་ཉལ་ཇི་འདྲ་བར་ཤེས་པ་ནི་ཐབས་སོ། །

[Block 3230]
ཐབས་ནི་སྤྱོད་པའི་མཚན་ཉིད་རབ་ཏུ་ཤེས་པའོ་ཞེས་བྱ་བ་ལ། དེ་ལྟར་སེམས་ཅན་རྣམས་ཀྱི་བསམ་པ༌[^2789]ཤེས་པས་སེམས་ཅན་རྣམས་ཀྱི་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པ་ཆེ་ཆུང་གི་སྤྱོད་པ་རྣམས་ཤེས་པ་ནི་ཐབས་སོ། །

[Block 3231]
རྒལ༌[^2790]ནས་འཇུག་པ་ནི་བསམ་གཏན་ལ་སོགས་པས་གོང་མ་རྣམས་སུ་ཕྱིན་ཀྱང་ཐབས་ཀྱི་དབང་གིས་དེ་ནས་སླར་ལྡོག་ཅིང་ས་འོག་མ་དག་ཏུ་འཇོག༌[^2791]ཅིང་སྤྱོད་པའོ། །

[Block 3232]
ཉོན་མོངས་པ་མེད་པས་ཀུན་ནས་ཉོན་མོངས་པ་ཞེས་བྱ་བ་ནི་ཤེས་བྱ་དང་། ཉོན་མོངས་པའི་སྒྲིབ་པ་སྤངས་ཏེ། ཉོན་མོངས་པ་མེད་པར༌[^2792]གྱུར་ཀྱང་། སེམས་ཅན་གྱི་དོན་དུ་འཁོར་བ་ན་སྤྱོད་ཅིང་ཉོན་མོངས་པའོ། །

[Block 3233]
ཁུར་བོར་བས་ཁུར༌[^2793]ཁྱེར་བ་ནི་ཕུང་པོ་ལྔའི་ཁུར་བོར་ཏེ། ཟག་པ་མེད་པར་གྱུར་ཀྱང་ཐབས་ཀྱི་དབང་གིས༌[^2794]སེམས་ཅན་གྱི་དོན་སྤྱོད་ཅིང་ཕུང་པོའི་ཁུར་ལེན་པའོ། །

[Block 3234]
ཚད་ཡོད་པར་ཚད་མེད་པར་སྟོན་པ་ནི་ཆོས་ཀྱི་མདོ་བཞི་ལྟ་བུ་ལ་སོགས་པ་ཚད་ཡོད་པ༌[^2795]དག་ལས་སེམས་ཀྱི་སྤྱོད་པ་དང་སྦྱར་ཏེ། ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ལ་སོགས་པ་ཚད་མེད་པར་སྟོན་ཅིང་འཆད་པའོ། །

[Block 3235]
ཚད་མེད་པ་ཚད་ཡོད་པར་སྟོན་པ་ནི་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ལ་སོགས་པ་ཡང་། ཆོས་ཀྱི་མདོ་བཞིར་ཉུང་ངུར་བསྡུས་ནས་འཆད་པའོ། །

[Block 3236]
དབང་པོ་ཞན་པ་རྣམས་ལ་གསལ་བར་བྱེད་པ་ནི་དབང་པོ་རྟུལ་པོ་རྣམས་ལ་ཡང་སྟོན། མཁས་པའི་ཐབས་ཀྱིས༌[^2796]དོན་དཀའ་བ་རྣམས་གསལ་བར་གོ་བར་བྱེད་པའམ། དབང་པོ་རྣོ་བར་བྱེད་པའོ། །

[Block 3237]
དུས་དང་དུས་མ་ཡིན་པ་ཤེས་པ་ནི་བྱ་བ་དང་མི་བྱ་བའི་དུས་ལ་མཁས་པའོ། །

[Block 3238]
ལམ་ནས་ལམ་ངན་པར་འགྲོ་བ་ནི། འཕགས་པའི་ལམ་ལ་གནས་ཀྱང་འཁོར་བའི་ལམ་དུ་ཡང་འགྲོ་བའོ། །

[Block 3239]
མྱུར་དུ་ལས་མང་པོ་བྱེད་པ་ནི་སྦྱིན་པ་ལ་སོགས་པའི་དངོས་པོ་ཆུང་ངུ་ཡང་བསམ་པ་དག་པས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་བསྔོ་བས་མང་པོ་དང་འབྲས་བུ་ཆེན་པོ་ཐོབ་པར་བྱེད་པའོ། །

[Block 3240]
མང་པོ་ལས་ཚད་མེད་པར་བྱེད་པ་ནི་སྦྱིན་པ་ལ་སོགས་པ་དངོས་པོ་ཆེན་པོ་བསྔོ་བ་ཡོངས་སུ་དག་པས་ཚད་མེད་པར་བྱེད་པའོ། །

[Block 3241]
བྱེ་བའི༌[^2797]སེམས་ཅན་རྣམས་འདུམ་པར་བྱེད་པ་ནི་སེམས་ཅན་ཕན་ཚུན་བྱེ་བ་དང་། དགེ་བའི་རྩ་བ་དང་བྲལ་བར་གྱུར་པ་རྣམས་འདུམ་པར་བྱེད་ཅིང་དགེ་བའི་རྩ་བ་ལ་འཇོག་པར་བྱེད་པའོ། །

[Block 3242]
ཐ་མ་དང་འབྲིང་དང་རབ་ལ༌[^2798]གནས་པ་ནི་སེམས་ཅན་རབ་འབྲིང་གསུམ་དང་མཐུན་པར་སྤྱོད་ཅིང་སྟོན་པའོ། །

[Block 3243]
མྱ་ངན་ལས་འདས་པའི་རིག་པ༌[^2799]ལས་འཁོར་བའི་རིགས་པར་ལྟུང་བ་ནི་མྱ་ངན་ལས་འདའ་བར༌[^2800]སྦྱོར་བ་འམ། སྤྱོད་པས་མྱ་ངན་ལས་འདའ་བ༌[^2801]ཐོབ་ཀྱང་། དེ་ནི༌[^2802]མི་གནས་པར་འཁོར་བ༌[^2803]ཡང་སྤྱོད་ཅིང་འཇུག་པའོ།[^2804] །རིགས་པ་ཞེས་བྱ་བ་ནི་སྐབས་འདིར་སྦྱོར་བ་འམ་སྤྱོད་པ་ལ་བྱའོ། །

[Block 3244]
ཐར་པ་ལས་བཅིངས་པ་ཚོལ་བ་ནི་ཉོན་མོངས་པ་ལ་སོགས་པའི་བཅིངས་པ༌[^2805]ལས་ཐར་ཀྱང་སེམས་ཅན་གྱི་དོན་སྤྱོད་པ་ལ་ཐབས་ཀྱིས༌[^2806]ཉོན་མོངས་པ་དང་བཅས་པར༌[^2807]སྟོན་པའོ། །ཤེས་བྱ་ཟད་པར་བྱེད་དེ། ཤེས་བྱ་ཟད་པར་ཡང་མི་ལྟུང་ཞེས་བྱ་བ་ནི་འདུས་བྱས་དང་། འདུས་མ་བྱས་ཀྱི་ཆོས་ཤེས་པར་བྱ་བ་རྣམས་ཟད་ཅིང་སྟོང་པར་ཆུད་ཀྱང་ཐབས་ཀྱིས་ཀུན་དུ་སྤྱད་པ་མི་གཏོང་བའི༌[^2808]ཕྱིར་སྟོང་པའི་མཐར་ཡང་མི་ལྟུང་བའོ། །

[Block 3245]
སྤྱོད་ལམ་ཐམས་ཅད་འཁྲུག་པར་བྱེད་པ་ལ་སྤྱོད་ལམ་རྣམས་ལས་ཀྱང་མི་ཉམས་སོ་ཞེས་བྱ་བ་ནི། ཐབས་ཀྱིས་སེམས་ཅན་གྱི༌[^2809]དོན་སྤྱོད་པའི་ཚེ་བསམ་གཏན་དང་ཏིང་ངེ་འཛིན་ལ་སོགས་པའི་སྤྱོད་པ་ལས་ལངས་ཀྱང་བསམ་གཏན་དང་། ཏིང་ངེ་འཛིན་གྱི་དོན་ལས་ཉམས་པར་ཡང་མི་འགྱུར་བའོ། །

[Block 3246]
སེམས་ཅན་ལ༌[^2810]ལྟ་བའི་ཚུལ་ཁྲིམས་ལ་མ་ཡིན་པ་ནི་འཕགས་པ་ཉན་ཐོས་ལ་སོགས་པ་ལྟར་ཐབས་མེད་པ་ནི་མ་ཡིན་གྱི། སེམས་ཅན་གྱི་དོན་དུ་སྤྱོད་པ་ཉིད་བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་ཡིན་པས་སེམས་ཅན་གྱི་དོན་མཐོང་ན། སོ་སོར༌[^2811]ཐར་པའི་སྡོམ་པ་ལ་མི་ལྟའོ།[^2812] །བསྡུ་བས་ལྟ་བ་ལ་བརྟེན་ཅིང་རྩོད་པས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་བསྡུ་ཞིང་དྲང་བའི་ཕྱིར་དོན་མཐུན་པར་སྤྱད་པ་ལ་སོགས་པའི་སྒོ་ནས་འདུལ་ཞིང་དྲང་བར་བྱ་བའི་སེམས་ཅན་དེ་དག་གི་ལྟ་བ་ཡང་ཕྱོགས་ཤིང་རྟེན་གྱི་མུ་སྟེགས་ཅན་ལ་སོགས་པ་ལྟར་ལྟ་བ་དེས་མཆོག་ཏུ་འཛིན་ཅིང་རྩོད་པ༌[^2813]ནི་མ་ཡིན་པའོ། །

[Block 3247]
སྒྲ་འབྱིན་པའོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་བརྗོད་དུ་མེད་པར་རྟོགས་ཀྱང་། སེམས་ཅན་གྱི་དོན་དུ་ཐབས་ཀྱིས༌[^2814]སྒྲ་དང་ཚིག་གི་སྒོ་ནས་ཆོས་སྟོན་པའོ། །

[Block 3248]
ཁམས་གསུམ་པ་སྤྱོད་ཡུལ་པ་ནི་ཁམས་གསུམ་གྱི་འདོད་ཆགས་དང་བྲལ་ཏེ་ཁམས་གསུམ་ལས་འདས་ཀྱང་སེམས་ཅན་གྱི་དོན་དུ་ཁམས་གསུམ་ན་སྤྱོད་པའོ། །

[Block 3249]
རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་ཐོབ་པའི་མཚན་ཉིད་སྤྱོད་ཡུལ་བ་ནི་སྟོང་པ་ཉིད་ལ་སོགས་པ་རྣམ་པར་ཐར་པའི་མཚན་ཉིད་ལ་སྤྱོད་པའོ། །

[Block 3250]
འཕགས་པ་མ་ཡིན་པའི་སྐྱེ་བོ་དང་འདྲེས་ཀྱི་འཕགས་པའི་སྐྱེ་བོ་དང་མ་འདྲེས་པ་ནི། བདག་ཉིད་འཕགས་པར་གྱུར་ཀྱང་འཕགས་པའི་ས་ན༌[^2815]མི་གནས་པར་སོ་སོའི་སྐྱེ་བོའི་ས་ན༌[^2816]གནས་ཤིང་སྤྱོད་པའོ། །

[Block 3251]
མྱ་ངན་ལས་འདས་པའི་ས༌[^2817]ལ་རྒྱབ་ཀྱིས་ཕྱོགས༌[^2818]ཤིང་འཁོར་བ་ལ་མངོན་དུ་ཕྱོགས་པ་ནི། །མྱ་ངན་ལས་འདས་པ་ཐོབ་ཀྱང་དེ་ལ་མི་ཕྱོགས་མི་གནས་པར་སེམས་ཅན་གྱི་དོན་དུ་འཁོར་བ་ལ་ཕྱོགས་ཤིང་སྤྱོད་པའོ། །

[Block 3252]
བདུད་ཀྱི༌[^2819]སྤྱོད་ཡུལ་ན་ཉོན་མོངས་པ་མེད་པར་སྣང་བ་ནི། འདོད་པའི་ཁམས་བདུད་ཀྱི་སྤྱོད་ཡུལ་ན་འདུག་ཀྱང་འདོད་པ་དང་། བདུད་ཀྱི་དབང་དུ་མི་འགྱུར་བའོ། །

[Block 3253]
ཐམས་ཅད་ནས་ཐམས་ཅད་དེ་ཐམས་ཅད་ནས་ཐམས་ཅད་པ་ཡང་མ་ཡིན་པ་ནི་ཐབས་མཁས་པས། ཀུན་རྫོབ་ཏུ་དངོས་པོ་ཐམས་ཅད་ལས་དངོས་པོ་ཐམས་ཅད་སྐྱེ་བར་ཤེས་ཤིང་འབྱུང་བར་ཡང་ནུས་ལ། དོན་དམ་པར་དངོས་པོ་ཐམས་ཅད་གང་ལས་ཀྱང་གཅིག་ཀྱང་མི་སྐྱེ་བར་རྟོགས་པའོ། །

[Block 3254]
ཐབས་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 3255 [HEADING]]
## དབང་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^13-0

[Block 3256]
དབང་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་རྣམ་པ་བཞི་སྟེ། སྐྱེས་བུ་ཆེན་པོར་གྱུར་པ་དང་། སེང་གེའི་སྒྲ་ཆེན་པོ་ཅན་དང་། ཤིན་ཏུ་དམ་བཅས་པ་ཅན་དང་། མི་བརྗེད་པའི་ཆོས་ཅན་ནོ། །

[Block 3257 [HEADING]]
### སྐྱེས་བུ་ཆེན་པོར་གྱུར་པ། ^13-1-0

[Block 3258]
སེམས་ཅན་གྱི་མཆོག་དམ་པ་སྐྱེས་བུ་ཆེན་པོ་ཞེས་བྱ་བ་ནི། གང་མཚན་དང་དཔེ་བྱད་རྣམས་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 3259 [HEADING]]
### སེང་གེའི་སྒྲ་ཆེན་པོ་ཅན། ^13-2-0

[Block 3260]
སེང་གེའི༌[^2820]སྒྲ་ཆེན་པོ་ཅན་ནི་གང་སྟོབས་བཅུ་ཐོབ་པ་སྟེ། ཉོན་མོངས་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པ་ཐམས་ཅད་སྤོབས་པ༌[^2821]དང་། ཁྱུ་མཆོག་གི་གནས་ཆེན་པོ་རབ་ཏུ་ཤེས་ཤིང་ཚངས་པའི་འཁོར་ལོ་རབ་ཏུ་བསྐོར་བ་དང་། འཁོར་དུ་སེང་གེའི་སྒྲ་ཡང་དག་པར་སྒྲོག༌[^2822]པར་བྱེད་པའོ། །
--- END BLOCKS ---
