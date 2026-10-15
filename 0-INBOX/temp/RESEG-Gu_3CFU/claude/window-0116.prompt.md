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
[Block 4061]
སྔ་མ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པའི་སྟོད་གཡོགས་དང་སྨད་གཡོགས་མ་ཆོག་པ་རྙེད་པ་ལ་དེའི་ཁ་བསྐང་བ་བསླང་བར་མི་བྱ་བའི་དོན་ཏོ། །

[Block 4062]
ཁྱིམ་པའི་ཆེ་ཚད་ནི་ཁྲུ་བཅུ་གཉིས་པའོ་ཞེས་བྱ་བ་ནི་མཆོག་ཏུ་གྱུར་པ་ལ་ཁྱིམ་པའི་སྟོད་གཡོགས་དང༌[^2771]སྨད་གཡོགས་ཀྱི་ཚད་དུ་གསུངས་སོ། །

[Block 4063]
དེ་བས་ན་འདི་ལས་ཆུང་བ་ཐམས་ཅད་ཉིད་དུ་ཁྱིམ་པའི་སྟོད་གཡོགས་སྨད་གཡོགས་ལ་མེད་པ་མ་ཡིན་ནོ། །

[Block 4064]
སླར་གང་ཞིག་འདིའི་མཐར་ཐུག་པའི་རིགས་པ་ཡིན་ཏེ། རས་ཡུག་ཆེན་ཁྲུ་བཅུ་གཉིས་པ་དང་། རས་ཡུག་ཕྲན་བདུན་པ་དང་། དོ་པ་མན་ཆད་ནས་རས་ཡུག་ཆེན་ཁྲུ་ཕྱེད་དང་གསུམ་པ་དང་། ཇི་སྲིད་དུ་ཕྱེད་པ་དང་ལྔ་པའི་བར་དང་རས་ཡུག་ཕྲན་འཁོར་གསུམ་ཁེབས་པའི་ཚད་ཀྱི་བར་ནི་ཆུང་བའི་མཐའ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 4065]
གང་གི་ཕྱིར་འདིའི་དོན་གྲུབ་པ་ཉིད་ལ་མ་བླངས་པ༌[^2772]ཉིད་ནི་རྒྱུ་ཉིད་འདིར་མཐར་ཐུག་པའི་དོན་མཐར་ཐུག་པའི་ཁྱིམ་པའི་སྟོད་གཡོགས་དང་སྨད་གཡོགས་ཐོབ་པ་ལ་ཁྲུ་བཅུ་གཉིས་པ་ལ་སོགས་པ་ཁ་སྐོང་བར༌[^2773]བྱེད་པ་ལ་འདི་བསླང་བར་མི་བྱ་བ་ཉིད་བསྟན་པའོ། །

[Block 4066]
མཐར༌[^2774]ཐུག་པར་གྱུར་པ་ལས་ཀྱང་མ་ཆོག་པ་རྙེད་པ་ལ་བླངས་པ༌[^2775]ཉིད་ཁོ་ན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4067]
ཆོས་གོས་མ་དྲས་པར་འཆང་བར་འདོད་པ་ལས་ལྷག་མ༌[^2776]གང་ཞིག་ཁྱིམ་པའི་སྟོད་གཡོགས་དང་སྨད་གཡོགས་འདོད་པ་འདི་ལ་མ་ཆོག་པ་ཉིད་ཀྱིས་རྫོགས་པ་ཉིད་ཀྱང་མ་ཡིན་ཞེས་བྱ་བ་མ་ཚང་བ༌[^2777]འདི་ལ་བསླང་བར་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 4068]
ལྷག་པ་སྦྱིན་པར་བྱ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ཙམ་གྱིས་ཡང་མཆོག་ཏུ་གྱུར་པའི་དགེ་སློང་གི་སྟོད་གཡོགས་དང་སྨད་གཡོགས་ཡོངས་སུ་རྫོགས་པ་དེ་ཙམ་ལ་ཡིན་གྱི། འདི་ལས་འོག་ཏུ་མ་ཡིན་ནོ། །

[Block 4069]
ཕྱི་མ་ཐོབ་ན་ལྷག་མ་སྦྱིན་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་དགེ་སློང་གིས༌[^2778]སྟོད་གཡོགས་དང་སྨད་གཡོགས་དང་བཅས་པ་སློང་བར་བྱེད་པ་ནི་ཚད་ལས་ཆེས་ལྷག་པ་ཞིག་ཐོབ་ན་དེ་ནི་སྦྱིན་བདག་དེ་ཉིད་ལ་སྦྱིན་པར་བྱ་བ་སྟེ་ཡོངས་སུ་རྫོགས་པའི་དོན་ལས་འདི་ལྷག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4070]
ཡོངས་སུ་ལོངས་སྤྱོད་པའི་དོན་དུ་ངོ་བོ་གང་ཞིག་ཚིག་རྐྱང༌[^2779]ལ་སོགས་པ་འདོད་པ་དེས་འདིར་རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །

[Block 4071]
བོར་རླག་བྱུང་བ་ཉིད་ལ་ཉེ་དུ་མ་ཡིན་པའི་དགེ་སློང་མ་ལས་ཆོས་གོས་ལེན་པ་ལ་རྗེས་སུ་གནང་བ་གང་ཡིན་པ་དེའི་སྟོད་གཡོགས་དང་སྨད་གཡོགས་མེད་པ་དེར་གཙོ་བོ་ཉིད་དོ། །

[Block 4072]
འདི་ཙམ་ནི་གཟུང་བར༌[^2780]བྱ་བ་ཉིད་དོ། །

[Block 4073]
ཡོངས་སུ་མ་རྫོགས་པ་འདི་མེད་པ་ལ་རྫོགས་པ་ཙམ་ལ་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པར་བྱའོ། །

[Block 4074]
གང་གི་ཕྱིར་འདི་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་སྔར་བརྗོད་པ་དེ་ཡང་འདི་ལས་སྟོད་གཡོགས་དང༌[^2781]སྨད་གཡོགས་ཙམ་ཉིད་ལ་ཞེས་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 4075]
གང་གི་ཕྱིར་སློང་བ་ལ་ཞུགས་པ་ཉིད་ནི་འདིར་ཕྱི་མ་སོ་སོར་འཛིན་པ་སྤོང་བར་བྱེད་པའི་རྒྱུ་ཡིན་ཏེ། དེ་བས་ན་སློང་བ་ལ་མ་ཞུགས་པ་ཉིད་ལ་ཆོས་གོས་མེད་པ་ཉིད་དང་ཆོས་གོས་ཡོངས་སུ་རྫོགས་པ་ཉིད༌[^2782]ཐོབ་པ་ལ་ཤིན་ཏུ་མང་བ་ཡིན་ན་ཡང་འདི་ལ་འཛིན་པ་སྐྱོང་མེད་པ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 4076]
ཅི་སྟེ་བླངས་པ༌[^2783]གཞན་རྣམས་ལ་དེ་སྔོན་དུ་འགྲོ་བ་ཅན་གྱིས༌[^2784]དོན་བསྒྲུབ་པ་རྣམས་ལ་གཏོགས་པ་གང་ཡིན་པ་དེ་ཙམ་གྱི་ཆོས་གོས་ལ་སྐྱོན་ཡོད་པ་མ་ཡིན་ཏེ། ཆོས་གོས་མ་ཡིན་པ་ལ་དགོས་པ་མེད་པའམ། ལྷག་པ་འཆང་བའི་དགོས་པ་ཅན་ཡོད་པ་ཞེས་བྱའོ། །

[Block 4077]
སློང་བར་རིགས་པ༌[^2785]ཡིན་ནོ་སྙམ་དུ་རྟོགས་པ་འདིས་སློང་བ་ལ་ཞུགས་ན་བྱ་བ་གང་ལ་ལྟུང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བསླང་བར་བྱ་བ་མ་ཡིན་པ་བསླངས་ན་ཉེས་བྱས་སོ། །

[Block 4078]
ཐོབ་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དགེ་སློང་ལ་གོས་དང་ཁ་ཟས་ལ་སོགས་པ་རུང་བ་མ་ཡིན་པ་དེ་སློང་བ་ལས་ཉེས་བྱས་སོ། །

[Block 4079]
བསླངས༌[^2786]ནས་རྙེད་ན་དངོས་གཞིའོ། །

[Block 4080]
མ་རྙེད་ན་ཉེས་བྱས་སོ། །

[Block 4081]
དོན་གྱིས་སྔ་མར་གཏོགས༌[^2787]ཏེ་འདི་ནི་ཉེས་བྱས་སོ། །

[Block 4082]
གལ་ཏེ་དངོས་གཞིའི༌[^2788]ལས་སློང་བ་འདི་ནི་འདིའི་བསླང་བར་བྱ་བ་ལས་སྔར་རྙེད་པའོ། །

[Block 4083]
བསླང་བར་བྱ་བ་མ་ཡིན་པ་སློང་བར་བྱེད་པ་སྦྱིན་པར་བྱ་བ་མི་སྦྱིན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ལ་དངོས་གཞིའོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^2789]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 4084]
བསླང་བར་བྱ་བ་མ་ཡིན་པ་བསླངས་པས་མ་ཐོབ་པ་ལ་འདིར་ལྷག་པར༌[^2790]སྦྱིན་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་པས་ཐོབ་པ་ཉིད་ལ་གཞན་ལ་ལྟུང་བ་འགྲུབ་པ་ལ་ཡང་མི་རིགས་པའི་ཕྱིར་སྦྱིན་པར་བྱ་བ་ཉིད་དེ། དེ་བས་ན༌[^2791]འདི་ཉིད་འདིར་མ་སྦྱིན་ན་དངོས་གཞིའི༌[^2792]ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 4085]
སློང་བར་རིགས་པའི་སྤང་བའོ།། །།

[Block 4086]
སྤགས་པ་སློང་བའི་སྤང་བ་ནི་སློང་བའི་རབ་ཏུ་དབྱེ་བར་གྱུར་པ་ཡིན་པས་སྤགས་པ་སློང་བའི་སྤང་བ་དེ་ཉིད་འདིར་ཆོ་ག་ཐོབ་པའི་བསམ་པ་ཙམ་གྱི་བྱེ་བྲག་དེ་ལ་དེའི་ཆོ་ག་ཐོབ་པ་ལ་འདི་ལ་བརྗེད་པར་བསྒྲུབ་པར་འགྱུར་ཏེ། དེའི༌[^2793]ཆོ་ག་ཡོངས་སུ་ཐོབ་པ་བསྒྲུབ་པའི་དོན་དུ་བྱེ་བྲག་འདི་མཚུངས་པ་ཉིད་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་སྤགས་པ༌[^2794]མ་ཕུལ་བ་ཤེས་པ་ནི་མ་སྤགས་པ༌[^2795]དང་འདྲའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཡུལ་གྱི་ཁྱད་པར༌[^2796]ནི་བྱེ་བྲག་གོ་ཞེས་བྱ་བ་འདི་ཙམ་གྱི་མཚུངས་པ་ཉིད་བརྗོད་པས་མ་ཕུལ་བ་ཡོད་པར་གྱུར་པ་ལ། གང་ཞིག་འདི་ལ་ཆོས་གོས་སྟེར་བར་འགྱུར་བ་ཞེས་བྱ་བར་སྤགས་པ་ཇི་ལྟར་ཡང་མ་ཤེས་པ་དེ་ནི་མ་སྤགས་པ༌[^2797]དང་འདྲ་བ་སྟེ། བསླངས་པའི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4087]
དེ་ཉིད་གཞན་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གཞན་གྱིས་མ་ཤེས་པ་སྤགས་པ༌[^2798]ནི་མ་སྤགས་པ༌[^2799]ཉིད་དོ། །

[Block 4088]
འདི་ནི་སློང་བའི་སྤང་བའི་གཞི་ཉིད་ཀྱི༌[^2800]ཁོངས་སུ་གཏོགས་པར་རིག་པར་བྱའོ། །

[Block 4089]
དེའི་བསླབ་པའི་གཞིར་གྱུར་པ་འདི་ལ་འཇུག་པ་ལ་སྐྱེད་པ༌[^2801]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4090]
རང་ཉིད་འདི་ལ་དོན་གྱིས་འཇུག་པ་ཞེས་བྱ་བ་དགོངས་པའི་དབང་གིས་འདིར་འཇུག་པའི་རྣམ་པ་ཉིད་དེ། དེ་བས་ན་མི་བསྐྱེད་པ་ཉིད་དོ། །

[Block 4091]
འདི་མི༌[^2802]ཤེས་པ་ཉིད་ལ་ཞེས་བྱ་བ་འདི་ཤེས་པའོ། །

[Block 4092]
གང་ལ་མི༌[^2803]ཤེས་པ་ཉིད་ལ་སློང་བ་ལ་འཇུག་པ་ཤེས་པ་ཉིད་ལ་ཡང་ལེན་པ་ལ་དེ་དངོས་གཞི་འདི་ཡིན་ནམ། འོན་ཏེ་དེ་དང་འབྲེལ་བའི་ཉེས་བྱས་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པར་བྱའོ། །

[Block 4093]
སྤགས་པ་སློང་བའི་སྤང་བའོ།། །།

[Block 4094]
སྦྱིན་པ་པོ་འདི་དག་ལས་སྤུངས་ཆེ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་རབ་ཏུ་གཏོང་བ་ཉིད་དང་ཚམ་ཚོམ་མེད་པ་ཉིད་ལ་དོན་གྱིས་འཇུག་པ་འདི་ཞེས་བྱ་བ་བྱེ་བྲག་འདིས་སོ་སོར་སྤགས་པ་དག་ལ་སློང་བ་དང་དེ་སྔོན་དུ་འགྲོ་བ་ཅན་གྱི་སློང་བ་ལ་འཇུག་པ་འདི་གཞན་ཡིན་ཏེ་སྔ་མ་ནི༌[^2804]མ་ཡིན་ནོ་ཞེས་བྱ་བའི་བློའོ། །

[Block 4095]
གང་གི་ཕྱིར་འདིར་འཇུག་པ་ཡང་ཉེས་པ་མེད་པའི་བློས༌[^2805]སྔར་བསླབ་པའི་གཞི་ཡོད་པ་ལ་ཡོད་པར་གྱུར་པའི༌[^2806]བསླབ་པའི་གཞི་གཞན་ཡོད་པར་འགྱུར་བ་དེ་ལ་བཏགས་པའོ། །

[Block 4096]
འདི་ནི་ལྟུང་བ་དང་ལྡན་པ་མ་ཡིན་ཏེ། སྔར་ཉིད་དུ་མི་འཇུག་པ་བྱ་བ་སྲིད་པ་ཡིན་ནོ། །

[Block 4097]
དེ་ལ་འདི་ལ་ཡང་དེའི་ཆོ་ག་ཡོངས་སུ་ཐོབ་པས་ཉེ་བར་བརྗོད་པ་མི་སླུ་བར་བྱེད་ཅིང་། དེའི་ཆོ་ག་ཡོངས་སུ་ཐོབ་པ་ལ༌[^2807]བསྒྲུབ་པའི་དོན་དུ་ཡུལ་འདི་ལ་མཚུངས་པ་ཉིད་དུ་བྱེ་བྲག་ལ་བརྗོད་པར་བྱ་སྟེ། སྦྱིན་པར་བྱེད་པ་སྤུངས་ཆེ༌[^2808]བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སྤགས་པ་མ་ཕུལ་བ་ཞེས་བྱ་བ་ནི་མ་སྤགས་པ་དང་འདྲའོ་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 4098]
སྦྱོར་བ་གཅིག་པའི་ཕྱིར་ཐོབ་ན་གཅིག་ཉིད་དོ་ཞེས་བྱ་བ་ནི། སྦྱོར་བ་གཅིག་པའི་ཕྱིར་ཐོབ་ན་རྫས་ཐ་དད་པ་ཅན་ལ་ཡང་རྙེད་པ་ལ་གཅིག་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4099]
ལེན་པ་ལ་སོགས་པ་ལ་དུ་མ་ཉིད་ལ་ཡང༌[^2809]ཡོངས་སུ་རྫོགས་པའི་གོས་སྦྱིན་པ་དགེ་སློང་མ་ལ་ལྷུང་བཟེད་དང་དབྱར་གྱི་རས་ཆེན་ཐོབ་པ་ལ་ཡང་སྦྱོར་བ་གཅིག་པ་ཉིད་ཡིན་ན་ལྟུང་བ་གཅིག་ཅེས་བྱ་བ་དེ་འདིའི་བྱེད་པའོ། །

[Block 4100]
སོ་སོ་ནས་སྤགས་པ་སློང་བའི་སྤང་བའོ།། །།
--- END BLOCKS ---
