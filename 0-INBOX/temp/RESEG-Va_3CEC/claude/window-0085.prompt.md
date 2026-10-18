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
[Block 2976]
དགའ་བ་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་བསྒོམ་པའི་ལམ་ན་ཚིག་དང་དོན་མི་བརྗེད་པ་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཡང་དག་པའི་དྲན་པ་གང་ཞེ་ན༌[^2608]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2977]
ཤིན་ཏུ་ཉེ་བར་གཞག་པ་ནི་རྟག་ཏུ་རྩེ་གཅིག་ཏུ་གཞག་པའོ། །

[Block 2978]
མི་སྒུལ་བ་ནི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་བསྐྱོད་པར༌[^2609]མི་ནུས་པའོ། །

[Block 2979]
དྲན་པ་ནི༌[^2610]ཡང་དག་པའི༌[^2611]ལྟ་བ་དང་མཐུན་པས་སོ། །

[Block 2980]
གྱ་གྱུ་མེད་པ་ནི་ལོག་པའི་ལྟ་བ་སྤངས་པས་སོ།[^2612] །འཁོར་བའི་སྐྱོན་གྱི༌[^2613]ཉེས་དམིགས་ལ་ལྟ་བ་ནི་ཉོན་མོངས་པ་རྒ་ཤི་ལ་སོགས་པ་ལ་རྟོག་པའོ། །

[Block 2981]
འདྲེན་པ་ནི་མྱ་ངན་ལས་འདས་པའི་ལམ་ལ་འཇུག་པའོ། །

[Block 2982]
དྲན་པ་ནི༌[^2614]བཤད་པའི༌[^2615]ཆོས་ཀྱི་ཚིག་མ་བརྗེད་པའོ། །

[Block 2983]
གཞུངས་པ་ནི་བཤད་པའི་ཚིག་གི༌[^2616]དོན་མ་བརྗེད་པའོ། །

[Block 2984]
འཕགས་པའི་ལམ་ཞེས་བྱ་བ་ནི་བསྒྲུབ་པའི༌[^2617]ཆོས་མ་བརྗེད་པ༌[^2618]བསྟན་པའོ། །

[Block 2985 [HEADING]]
#### མཐུ་ཆེ་བ། ^8-7-8-0

[Block 2986]
མཐུ་ཆེ་བའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་བསྒོམ་པའི་ལམ་ན་བསམས་པའི་དོན་རྫོགས་པར་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས་དེ་ལ་ཡང་དག་པའི་ཏིང་ངེ་འཛིན་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2987]
ཡང་དག་པ་ཉིད་དུ་མཉམ་པ་དང་། ཆོས་ཐམས་ཅད་ཀྱིས་མཉམ་པ་ཞེས་བྱ་བའི༌[^2619]དོན་དམ་པར་ཆོས་ཐམས་ཅད་ལ་ཐ་དད་པ་མེད་དེ། སྟོང་པ་ཉིད་དུ་རོ་གཅིག་ཅིང་མཉམ་པར་སེམས་རྩེ་གཅིག་ཏུ་འཇོག་པ་ནི་ཡང་དག་པའི་ཏིང་ངེ་འཛིན་ཞེས་བྱའོ། །

[Block 2988]
དོན་དེ་ཉིད་བསྟན་པའི་ཕྱིར། ཏིང་ངེ་འཛིན་གང་ལ་གནས་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སེམས་ཅན་ཐམས་ཅད་ཅེས་བྱ་བ་དང་ཉོན་མོངས་པའི་སྒྲིབ་པ་ལས་རབ་ཏུ་ཐར་བར་བྱ་བའི་ཕྱིར། དེ་ཁོ་ན་ཡེ་ནས་དག་པས་མི་འགྱུར་བ་ལ་རྩེ་གཅིག་ཏུ་འཇོག་པ་ནི་ཡང་དག་པའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 2989]
ངེས་པར་གྱུར་བ་ལས་འཇུག་པའི༌[^2620]དོན་དམ་པའི་ཏིང་ངེ་འཛིན་ལ་འཇུག་པའོ། །

[Block 2990]
དེ་ལ་ཡང་དག་པའི་ལྟ་བ་ནི་ཡོངས་སུ་གཅོད་པའི་ཡན་ལག་སྟེ། དེས་ཇི་ལྟར་མྱོང་བའི་དེ་ཁོ་ན་ལ་གཅོད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2991]
ཡང་དག་པའི་རྟོག་པ༌[^2621]ནི་གཞན་གོ་བར་བྱེད་པའི་ཡན་ལག་སྟེ། དེས་ཇི་ལྟར་ཁོང་དུ་ཆུད་པ་སེམས་ལ་བརྟགས་ན༌[^2622]ཚིག་ཏུ་སྨྲ་བའི་ཕྱིར་རོ། །

[Block 2992]
ཡང་དག་པའི་ངག་དང་། ལས་དང་། འཚོ་བ་གསུམ་ནི་གཞན་ཡིད་ཆེས་པར་བྱེད་པའི་ཡན་ལག་སྟེ། དེ་དག་གིས་རིམ་པ་བཞིན་དུ་ལྟ་བ་ལ་སོགས༌[^2623]རྣམ་པར་དག་པ༌[^2624]དེ་ལ་ཡིད་ཆེས་པས་སོ། །

[Block 2993]
དེ་ལ་ཡང་དག་པའི་ངག་གིས་ཇི་ལྟར་ཁོང་དུ་ཆུད་པ་དྲིས་པ་ལ་ལུང་བསྟན་པའི་སྒོ་ནས་འདིའི་ལྟ་བ་རྣམ་པར་དག་གོ་ཞེས་གཞན་ཡིད་ཆེས་པར་འགྱུར་རོ། །

[Block 2994]
ཡང་དག་པའི་ལས་ཀྱི་མཐའ་ནི་མི་བྱ་བ་མི་བྱེད་པ་དང་། འོང་བ་དང་ལྡོག་པ་ལ་སོགས་པ་ལ།[^2625] སྤྱོད་པ་ཕུན་སུམ་ཚོགས་པས༌[^2626]ཚུལ་ཁྲིམས་རྣམ་པར་དག་པར་ཡིད་ཆེས་སོ། །

[Block 2995]
ཡང་དག་པའི་འཚོ་བས་ཆོས་གོས་ལ་སོགས་པ་ཆོས་བཞིན་དུ་ཚོལ་བའི་ཕྱིར། འཚོ་བ་རྣམ་པར་དག་པར་ཡིད་ཆེས་སོ། །

[Block 2996]
ཡང་དག་པའི་རྩོལ་བ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པ་སྦྱོང་བའི༌[^2627]ཡན་ལག་སྟེ། དེས་ཀུན་དུ་སྦྱོར་བ་མ་ལུས་པར༌[^2628]སྤོང་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2997]
ཡང་དག་པའི་དྲན་པ་ནི་ཉེ་བའི་ཉོན་མོངས་པ་སྦྱོང་བའི་ཡན་ལག་སྟེ། དེས་ཞི་གནས་དང་ལྷག་མཐོང་གི་མཚན་མ་མ་བརྗེད་པས་ཞུམ་པ་དང་། རྒོད་པའི་ཉོན་མོངས་པ་སྐྱེ་བའི་སྐབས་མེད་པའི་ཕྱིར་རོ། །

[Block 2998]
ཏིང་ངེ་འཛིན་ནི་ཡོན་ཏན་ཁྱད་པར་ཅན་ཐོབ་པ་ལ་སྒྲིབ་པ་སྦྱོང་བའི་ཡན་ལག་སྟེ། དེས་སྒྲིབ་པ་སྦྱངས་ནས་མངོན་པར་ཤེས༌[^2629]པ་ལ་སོགས་པའི་ཡོན་ཏན་སྒྲུབ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2999]
འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 3000 [HEADING]]
### ཞི་གནས་དང་ལྷག་མཐོང་མི་ཟད་པ། ^8-8-0

[Block 3001]
བསྡུས་པའི་རྣལ་འབྱོར་སྤྱོད་པ་དང་། སྤྲོས་པའི་རྣལ་འབྱོར༌[^2630]སྤྱོད་པ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^2631]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཞི་གནས་དང་ལྷག་མཐོང་ཡང་མི་ཟད་པ་ཡིན་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3002]
དེ་གཉིས་མི་ཟད་པ་ཡང་དེ་གཉིས་རྩེ་གཅིག་ཏུ་གཞག་པའི་ཆོས་དང་། རྟོགས་པར༌[^2632]བྱ་བའི་ཆོས་མི་ཟད་པས་ན། དེ་ལ་རྩེ་གཅིག་ཏུ་འཇོག་པར་བྱེད་པ་དང་། རྟོགས་པར༌[^2633]བྱེད་པ་ཡང་མི་ཟད་པའོ། །

[Block 3003 [HEADING]]
#### བསྡུས་པའི་རྣལ་འབྱོར་ལ་ཞུགས་པ། ^8-8-1-0

[Block 3004]
བསྡུས་པའི་རྣལ་འབྱོར་ལ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་སྦྱོར་བ་དང་མཐོང་བ་དང་། བསྒོམ་པའི་ལམ་ན་ཞི་གནས་ལ་རབ་ཏུ་སྦྱོར་བ་སྟེ།[^2634] དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཞི་གནས་མི་ཟད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3005]
ཞི་གནས་མི་ཟད་པ་ཡང་ཞི་གནས་ཀྱི་ཚོགས་མི་ཟད་པ་དང་། ཞི་གནས་ཉིད་མི་ཟད་པ་སྟེ། རྣམ་པ་གཉིས་སུ་རིག་པར་བྱའོ། །

[Block 3006]
དེ་ལ་གང་སེམས་ཞི་བ་དང་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བཏང་སྙོམས་སྒོམ༌[^2635]ཞེས་བྱ་བ་ཡན་ཆད་ནི་ཞི་གནས་ཀྱི་ཚོགས་སོ། །

[Block 3007]
བསམ་གཏན་དང་པོ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ་དགུ་པོ་འདི་དག་ནི་ཞི་གནས་ཞེས་བྱའོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་ཞི་གནས་ཉིད་བསྟན་ཏོ། །

[Block 3008 [HEADING]]
##### ཞི་གནས་ཀྱི་ཚོགས། ^8-8-1-1-0

[Block 3009]
ཞི་གནས་ཀྱི་ཚོགས་ལ་རྣམ་པ་གཉིས་ཏེ། གཙོ་བོར་གྱུར་པ་མ་ཡིན་པའི་ཚོགས་དང་། གཙོ་བོའི༌[^2636]ཚོགས་སོ། །

[Block 3010 [HEADING]]
###### གཙོ་བོར་གྱུར་པ་མ་ཡིན་པའི་ཚོགས། ^8-8-1-1-1-0

[Block 3011]
གཙོ་བོར་གྱུར་པ་མ་ཡིན་པའི་ཚོགས་ཀྱི་དབང་དུ་བྱས་ནས། སེམས་ཞི་བ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3012]
ནང་དུ་སེམས་རྣམ་པར་རྟོག་པ་མི་མང་བ་ནི་སེམས་ཞི་བའོ། །

[Block 3013]
ཕྱི་རོལ་གྱི་ཡུལ་རྣམས་ལ་རྟོག་པར་མི་དགའ་བ་ནི་རབ་ཏུ་ཞི་བའོ། །

[Block 3014]
ཕྱི་ནང་གཉིས་ལ་རྟོག་པ་མེད་པའམ། གཉིད་དང་རྨུགས་པ་མེད་པ་ནི་ཉེ་བར་ཞི་བའོ། །

[Block 3015]
ནང་དུ་སེམས་རྣམ་པར་རྟོག་པ་མི་མང་བ་སྟེ་ཞི་བས་ན། རྣམ་པར་མི་གཡེང་བའོ།[^2637] །ཕྱི་རོལ་དུ་རྟོག་པ༌[^2638]མེད་དེ་རབ་ཏུ་ཞི་བས་ན། དབང་པོ་ལེགས་པར་བསྡོམས༌[^2639]པའོ། །
--- END BLOCKS ---
