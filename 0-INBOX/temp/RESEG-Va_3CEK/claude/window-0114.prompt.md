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
[Block 3991]
གལ་ཏེ་དོན་མྱ་ངན་ལས་འདས་པ་ཡིན་ན་ནི་ཤེས་པ་དྲུག་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། འགོག་པ་དང་ཟད་པ་དང་མི་སྐྱེ་བ་དང་། ཀུན་རྫོབ་ཤེས་པ་རྣམས་སོ། །

[Block 3992]
དོན༌[^2827]ནི་ཀུན་ན། དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་དེ་ནི་ས་ཐམས་ཅད་པ་ཡིན་ནོ། །

[Block 3993]
གཞན་ཀུན་རྫོབ། གཞན་ཆོས་དང་ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་གཉིས་ནི་ཀུན་རྫོབ་ཤེས་པའི་རང་བཞིན་དག་ཡིན་ཏེ། [^2828]མིང་གི་ཚོགས་ལ་སོགས་པ་དང་།

[Block 3994 [VERSE]]
ངག་ལ་དམིགས་པའི་ཕྱིར་རོ། །
ཆོས་རིག་འདོད་དང་བསམ་གཏན་ན། །

[Block 3995]
ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པ་ནི༌[^2829]ས་ལྔ་པོ་འདོད་པའི་ཁམས་དང་། བསམ་གཏན་བཞིས་བསྡུས་པ་ཡིན་ཏེ། ཡན་ཆད་ན་མིང་གི་ཚོགས་མེད་པའི་ཕྱིར་རོ། །

[Block 3996]
ངག་ནི་འདོད་པ༌[^2830]

[Block 3997]
དང་པོ་ན། །ངག་དང་ངེས་པའི་ཚིག་ཅེས་བྱ་བ་ནི་དོན་གཅིག་གོ། །

[Block 3998]
ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་ནི་འདོད་པའི་ཁམས་དང་བསམ་གཏན་དང་པོའི་ས་པ་དག་ཡིན་ཏེ། ཡན་ཆད་ན་རྟོགས་པ༌[^2831]མེད་པའི་ཕྱིར་རོ། །

[Block 3999]
བཏགས་པ༌[^2832]ནི་སོ་སོ་ཡང་དག་པར་རིག་པ་རྣམས་འདི་སྐད་དུ་ཚིག་དང་ཡི་གེ་དང་། དེ་ཉིད་ཀྱི༌[^2833]དོན་དང་། དེ་ཉིད༌[^2834]ཀྱི་གཅིག་དང་གཉིས་དང་མང་པོ་དང་ཕོ་དང་མོ་ལ༌[^2835]སོགས་པའི་ཚིག་བླ་དགས་དང་། དེ་ལ་ཐགས་ཐོགས་མེད་པར་བྱ་བ་ལ་ཐོགས་པ་མེད་པར་ཤེས་པ་ནི་ཆོས་སོ་སོ་ཡང་དག་པར་རིགས་པ༌[^2836]ལ་སོགས་པ་ཡིན་ནོ་ཞེས་སྟོན་ཏེ། དེ་ཉིད་ཀྱིས་འདི་དག་གི་གོ་རིམས་གྲུབ་པ་ཡིན་ནོ། །

[Block 4000]
ཚིག་ངེས་པ་ནི་ངེས་པའི་ཚིག་སྟེ། དཔེར་ན་གཟུགས་སུ་རུང་བས་ནི༌[^2837]དེའི་ཕྱིར། གཟུགས་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 4001]
གཞན་དག་ན་རེ་ལན་དང་ལན་ལ་སྤོབས་པས་ན་སྤོབས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 4002]
སོ་སོ་ཡང་དག་པར་རིག་པ༌[^2838]འདི་དག་གི་སྔོན་གྱི་སྦྱོར་བ་ནི་གོ་རིམས་བཞིན་དུ་རྩིས་དང་། སངས་རྒྱས་ཀྱི་བཀའ་དང་། སྒྲ་རིག་པ་དང་། གཏན་ཚིགས་རིག་པ་དག་ཡིན་ཏེ། འདི་དག་ལ་མཁས་པར་མ་བྱས་པར་དེ་དག་སྐྱེད་པར༌[^2839]མི་ནུས་སོ་ཞེས་གྲག་གོ། །

[Block 4003]
ཐམས་ཅད་ཀྱི་སྦྱོར་བ་སངས་རྒྱས་ཀྱི་བཀའ་ཁོ་ན་ཡིན་ནོ༌[^2840]ཞེས་བརྗོད་དོ། །

[Block 4004]
གང་ལ་གཅིག་ཡོད་པ་དེ་ལ་གདོན་མི་ཟ་བར་སོ་སོ་ཡང་དག་པར་རིག་པ་བཞི་ཆར་ཡོད་དོ། །

[Block 4005]
[^2841]མ་ཚང་བར་ནི་དེ་ཐོབ་མེད། །དེ་དག་མ་ཚང་བར་ནི་སོ་སོ་ཡང་དག་པར་རིག་པ་འཐོབ་པ་མ་ཡིན་ནོ། །

[Block 4006 [HEADING]]
#### རབ་ཀྱི་མཐའ་པའི་བསམ་གཏན། ^4-13-4-0

[Block 4007]
ཉོན་མོངས་པ་མེད་པ་ལ་སོགས་པའི་ཡོན་ཏན་བསྟན་པ་གང་དག་ཡིན་པ། དྲུག་པོ་དེ་དག་རབ་མཐའ་པས། །དེ་དག་ནི་རབ་ཀྱི་མཐའ་པའི་བསམ་གཏན་གྱི་སྟོབས་ཀྱིས་འཐོབ་པོ། །དེ་ནི་རྣམ་དྲུག །བསམ་གཏན་བཞི་པ་རབ་ཀྱི༌[^2842]མཐའ་པ་དེ་ཡང༌[^2843]ཉོན་མོངས་པ་མེད་པ་དང་། སྨོན་ནས་ཤེས་པ་དང་། སོ་སོ་ཡང་དག་པར་རིག་པ་གསུམ་དང་། རབ་ཀྱི་མཐའ་པ་དེ་ཉིད་དང་དྲུག་གི་བདག་ཉིད་ཡིན་ནོ། །

[Block 4008]
ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་ནི་དེའི་སྟོབས་ཀྱིས༌[^2844]འཐོབ་པ་ཡིན་གྱི་དེ་བསམ་གཏན་བཞི་པའི་ས་པ་ནི་མ་ཡིན་ནོ། །

[Block 4009]
རབ་ཀྱི་མཐའ་པ་ཞེས་བྱ་བ་ནི༌[^2845]ཅི་ཞེ་ན། བསམ་གཏན་མཐའ། བསམ་གཏན་བཞི་པ་ཡིན་ནོ། །

[Block 4010]
དེ་ནི་ས་ཀུན་གྱིས༌[^2846]མཐུན་པས།[^2847] །འཕེལ་བའི་རབ་ཏུ་ཕྱིན་པ་ཡིན། །ཇི་ལྟར་ན་ས་ཐམས་ཅད་ཀྱིས་མཐུན་པར་བྱས་པ་ཡིན་ཞེ་ན། འདོད་པ་ན་སྤྱོད་པའི་སེམས་ལས་བསམ་གཏན་དང་པོ་ལ་སྙོམས་པར་འཇུག་ལ། དེ་ལས་ནི་བསམ་གཏན་གཉིས་པ་སྟེ། དེ་བཞིན་དུ་རིམ་གྱིས་འདུ་ཤེས་མེད༌[^2848]འདུ་ཤེས་མེད་མིན་གྱི་སྐྱེ་མཆེད་ཀྱི་བར་ལ་སྙོམས་པར་འཇུག་གོ། །

[Block 4011]
མི་མཐུན་པ་ནི་ཡང་འདོད་པ་ན་སྤྱོད་པའི་སེམས་ཀྱི་བར་ལའོ། །

[Block 4012]
དེ་ལས་ཡང་བསམ་གཏན་བཞི་པའི་བར་དུ་མཐུན་པ༌[^2849]ཡིན་ཏེ། དེ་ལྟར་ན་ས་ཐམས་ཅད་ཀྱིས་མཐུན་པར་བྱས་པ་ཡིན་ནོ། །

[Block 4013]
ཇི་ལྟར་ན་འཕེལ་བའི་རབ་ཏུ་ཕྱིན་པའི་བར་དུ་ཡིན༌[^2850]ཞེ་ན། དེ་ལྟར་བསྒོམས་པ༌[^2851]ཆུང་ངུ་ལས་འབྲིང་། འབྲིང་ལས་ཆེན་པོ་ལ༌[^2852]སྙོམས་པར་འཇུག་པ་སྟེ། འཕེལ་བའི་མཆོག་ནི་འཕེལ་བའི་རབ་ཡིན་ནོ། །

[Block 4014]
བསམ་གཏན་འདི་ལྟ་བུ་འདི་ནི་རབ་ཀྱི་མཐའ་པ་ཡིན་ཏེ། འདི་ལ་མཐར༌[^2853]རབ་ཏུ་ཕྱིན་པ་ཡོད་པའི༌[^2854]ཕྱིར་རོ། །

[Block 4015]
འདིར་མཐའ་ནི་འཕེལ་བའམ་རྣམ་པ་ཡིན་ཏེ། མུ་བཞི་པ་བཞིན༌[^2855]ནོ། །

[Block 4016 [VERSE]]
ཡོན་ཏན་དྲུག་པོ་དེ་དག་ཀྱང་། །
སངས་རྒྱས་ལས་གཞན་སྦྱོར་ལས༌[^2856]སྐྱེས། །

[Block 4017]
སངས་རྒྱས་ལས་གཞན་པ༌[^2857]ནི་སྦྱོར་བ་ལས་བྱུང་བ་ཡིན་གྱི་འདོད་ཆགས་དང་བྲལ་བས་ཐོབ་པ་ནི༌[^2858]མ་ཡིན་ནོ། །

[Block 4018]
སངས་རྒྱས་ཀྱི་ནི་སྦྱོར་བ་ལས་བྱུང་བ་ཅུང་ཟད་ཀྱང་མེད་དེ། འདོད་ཆགས་ཅན་གྱི༌[^2859]དབང་ཕྱུག་ཡིན་པའི་ཕྱིར། [^2860]དེའི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ༌[^2861]ཐམས་ཅད་མངོན་དུ༌[^2862]གྱུར་པ་ནི༌[^2863]བཞེད་པ་ཙམ་ལ་རག་ལས་པ་ཡིན་ནོ། །

[Block 4019]
རེ་ཞིག་དེ་དག་ནི་ཉན་ཐོས་དང་། ཐུན་མོང་པའི་ཡོན་ཏན་དག་ཡིན་ནོ། །

[Block 4020 [HEADING]]
### མངོན་པར་ཤེས་པ། ^4-14-0

[Block 4021]
མངོན་པར་ཤེས་པ་ལ་སོགས་པ་ནི་སོ་སོའི་སྐྱེ་བོ་དག་དང་ཡང་ཐུན་མོང༌[^2864]ཡིན་ནོ། །

[Block 4022]
མངོན་པར་ཤེས་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན།

[Block 4023 [VERSE]]
རྫུ་འཕྲུལ་རྣ་བ་ཡིད་དང་ནི། །
སྔོན་ཚེ་འཆི་འཕོ་སྐྱེ་བ་དང་། །
ཟད་ཤེས་མངོན་དུ་བྱ་བ་ཡི། །

[Block 4024]
མངོན་ཤེས་རྣམ་པ༌[^2865]དྲུག །རྫུ་འཕྲུལ་གྱི་ཡུལ་ཤེས་པ་མངོན་དུ་བྱ་བའི་མངོན་པར་ཤེས༌[^2866]དང་། ལྷའི་རྣ་བ་དང་། སེམས་ཀྱི་རྣམ་གྲངས་དང་། སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་དང་། འཆི་འཕོ་དང་། སྐྱེ་བ་དང་། ཟག་པ་ཟད་པ་ཤེས་པ་མངོན་སུམ༌[^2867]དུ་བྱ་བའི་མངོན་པར་ཤེས་པ་སྟེ། དེ་དག་ནི་མངོན་པར་ཤེས་པ་དྲུག༌[^2868]ཡིན་ནོ། །

[Block 4025]
དེ་དག་ལས་ལྔ་ནི་སོ་སོའི་སྐྱེ་བོ་རྣམས་དང༌[^2869]ཐུན་མོང་བ་ཡིན་ནོ། །

[Block 4026]
དེ་དག་ཐམས་ཅད་ནི། རྣམ་གྲོལ་བློ། །དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་བཞིན་དུ། རྣམ་པར་གྲོལ་བའི་ལམ་གྱི་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་ནོ། །

[Block 4027]
བཞི་ནི་ཀུན་རྫོབ་ཤེས་པ་སྟེ། །སེམས་ཀྱི་རྣམ་གྲངས་དང་། ཟག་པ་ཟད་པ་ཤེས་པའི༌[^2870]མངོན་པར་ཤེས་པ་མ་གཏོགས་སོ། །

[Block 4028]
སེམས་ལ་ཤེས་པ་ལྔ་ཡིན་ནོ། །

[Block 4029]
སེམས་ཀྱི་རྣམ་གྲངས་མངོན་པར་ཤེས་པ་ནི༌[^2871]ལྔ་ཡིན་ཏེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། ལམ་དང་ཀུན་རྫོབ་དང་། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་རྣམས་སོ། །

[Block 4030]
ཟག་པ༌[^2872]མངོན་ཤེས་སྟོབས་བཞིན་ནོ། །
--- END BLOCKS ---
