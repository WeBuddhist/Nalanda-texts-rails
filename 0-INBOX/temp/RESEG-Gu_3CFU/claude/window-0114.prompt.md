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
རྒྱ་ཆེ་བ་དང་ཐ་སྙད་ཀྱི་དབང་མ་ཡིན་པ་ཉིད་ནི་གོས་སྦྱིན་པ་ལ་སོགས་པ་ལ་གཙོ་བོ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ཙམ་དུ་རང་གི་ལུས་ཀྱིས་འཇུག་པ་ཉེ་བར་བཀག་པར་གྱུར་པ་ཉིད་ཀྱིས་མ་ཡིན་པ་དེ་ཙམ་དུ་འདིར་རྒྱ་ཆེ་བ་ལ་མངོན་པར་བརྟེན་པར་རིག་པར་བྱའོ། །

[Block 3992]
འདིར་གཉིས་པོ་འདི་ཐམས་ཅད་གཙོ་བོར་རིག་པར་བྱ་བ་སྟེ། ཐ་དད་པ་ནི་མ་ཡིན་ནོ། །

[Block 3993]
བོར་རླག༌[^2734]བྱུང་བ་རྙེད་པ་ལ་འདི་ཙམ་དུ་གཟུང་བ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3994]
རེ་ཞིག་གི་སེམས་ཀྱིས་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། ཉེ་བར་གཡོགས་པ་འམ་བགོས་པའམ་དུས་རེ་ཞིག་པ་སྟེར་བ་ལ་གང་ཞིག་ཡིད་གཅུགས༌[^2735]པས་ལེན་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་མདོ་འདིས༌[^2736]བསྡུས་པ་ཡིན་ནོ། །

[Block 3995]
རིན་སྦྱིན་པ་བརྗེད་པ་ལའོ་ཞེས་བྱ་བ་ནི། ཚེ་དང་ལྡན་པ་སླར་ནོར་མ་སྦྱིན་ཅེས་ཟེར་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདིའི་རྗེས༌[^2737]ལ་དེར་འདི་གསུངས༌[^2738]སོ། །

[Block 3996]
དེ་བཞིན་དུ་གང་ཞིག་མི་དྲན་པ་དེའི་འདི་བསྡུས་པའོ། །

[Block 3997]
ལེན་པའི་སྤང་བ་ཞུ་བའོ། །

[Block 3998]
ལེན་པའི་སྤང་བའོ།། །།

[Block 3999]
སློང་བའི་སྤང་བ་འདི་ལ་ལྟུང་བ་བྱེད་པ་པོ་གང་ཞེ་ན། དེའི་ཕྱིར་མིའི་འགྲོ་བ་པར་གཏོགས་པ་ཁྱིམ་པར་གྱུར་པ་སྲོག་དང་ལྡན་པ་ཉེ་དུ་མ་ཡིན་པ་ནི་ལྟུང་བའི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 4000]
འོག་མ་གསུམ་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདས་མ་ཐག་པའི་བསླབ་པའི་གཞི་འོག་མ་གསུམ་ལ་ཡང་དེ་ཉིད་ལྟུང་བའི་བྱེད་པ་པོ་ཡིན་པའོ། །

[Block 4001]
འདིར་དགེ་སློང་ཇི་ལྟ་བུ་ལ་དེ་ལྟུང་བའི་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གོས་ཕྲོག་པ་དང་། བརླག་པ༌[^2739]དང་། ཚིག་པ་དང་། རླུང་གིས་ཁྱེར་བ་དང་། ཆུས་ཁྱེར་བར་མ་གྱུར་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་དུ་ཇི་ཞིག་ལྷག་པར་སྤྱད༌[^2740]ན་ལྟུང་བ་ཇི་ལྟ་བུར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བླངས་ན་ཉེས་བྱས་ཀྱིའོ། །

[Block 4002]
ཐོབ་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ༌[^2741]སྨོས་ཏེ། བྱེད་པ་པོ་མ་རྙེད་པ་ལ་དེ་ལས་བླངས་ན་དངོས་གཞིའི་སྤང་བའི་ལྟུང་བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་ཞིག་ཐོབ་ན་ཞེ་ན། དེའི་ཕྱིར་ཆོས་གོས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4003]
ཚད་ཇི་ཙམ་ཞིག་ཅེ་ན། དེའི་ཕྱིར་མི་ཆུང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆོས་གོས་གསུམ་གང་ཡང་རུང་བ་ལས་ཚད་དང་ལྡན་པའོ། །ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། དེའི་ཕྱིར་རིན་ཐང་དང་། ཁ་དོག་དང་ཁྲུ་ཚད་ལས་རྣམ་པ་གང་བླངས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྔོན་པོ་དང་། སེར་པོ་དང་། དམར་པོ་དང་། མཐུག་པོ་དང་། ལེ་བརྒན་རྣམས་ནི། འདིར་ཁ་དོག་གི་རྗེས་སུ་འགྲོ་བ་སྟེ། དེ་བས་ན་འདིར་ཁ་དོག་བྱེད་པ་ཅན་ལ་ཁ་དོག་གི་སྒྲའོ། །

[Block 4004]
གཞན་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་རིན་ཐང་གཞན་ནམ་ཁ་དོག་གཞན་ནམ། ཁྲུ་ཚད་གཞན༌[^2742]ཐོབ་པ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 4005]
འདིར་གཞུང་ཁ་ཅིག་ལས་ནི། དགེ་སློང་གིས༌[^2743]ཆོས་གོས་སྔོན་པོ་སློང་བར་བྱེད་ཅིང་སྔོན་པོ་ཉིད་ཐོབ་ནས་དེ་ལ་སློང་བར་བྱེད་ན་ཉེས་བྱས་སོ། །

[Block 4006]
ཐོབ་པ་ན་སྤང་བའི་ལྟུང་བྱེད་དོ། །

[Block 4007]
འོག་མ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4008]
རིན་ཐང་གི་གཞུང་ནི་དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 4009]
དགེ་སློང་མས་ཆོས་གོས་ཀཱར་ཥཱ་པ་ཎ་ལྔ་རི་བ་དེ་ཉིད་སློང་བར་བྱེད་ན་ཉེས་བྱས་སོ། །

[Block 4010]
ཐོབ་པ་ན་སྤང་བའི་ལྟུང་བྱེད་དོ། །

[Block 4011]
འོག་མ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4012]
ཚད་ནི་གཞུང་ཡང་དགེ་སློང་གི་ཆོས་གོས་ཁྲུ་ལྔ་པ་སློང་བར་བྱེད་ཅིང་དེས་གོས་ཁྲུ་ལྔ་པ་ཉིད་ཐོབ་ན་སློང་བ་ལ་ཉེས་བྱས་སོ། །

[Block 4013]
ཐོབ་པ་ན་སྤང་བའི་ལྟུང་བྱེད་དོ། །

[Block 4014]
འོག་མ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4015]
འདིར་འོག་མ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་ཚིག་ནི་ཐ་དད་པར་འགྱུར་བ་ཉིད་ལ་ཡིན་པར་རིག་པར་བྱའི། [^2744]འོག་མ་ཁྲུ་ལྔ་པ་སློང་བ་ལ་ཁྲུ་བཅུ་པ་ཐོབ་པ་ལ་ཆོས་གོས་དེ་ཉིད་ལ་ཁྲུ་ལྔ་པ་རྣམས་ལ་ལྟུང་བ་མེད་དོ། །

[Block 4016]
ལྔ་པོ་རྣམས་ལ་ནི་སྤང་བ་ཞེས་བྱ་བའོ། །

[Block 4017]
སློང་བ་ལ་རྣམ་པར་སྤྱད༌[^2745]པ་ནི་ཐམས་ཅད་སྤང་བའོ། །

[Block 4018]
རས་མ་དང་ཁ་ཚར་དག་སློང་ནའོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4019]
ཁ་ཚར་དག་སློང་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 4020]
ཁ་ཚར་བསླངས་པ་ལས་རས་མ་ཐོབ་པ་ལ་ཡང་ལྟུང་བ་མེད་དོ། །

[Block 4021]
རས་མ་བསླངས་ནས་རས་ཡུག་ཆེན་དང་། རས་ཡུག་ཕྲན་དག་ཐོབ་བོ་སྙམ་ནས་བསླངས་ཤིང་ཐོབ་པ་ན༌[^2746]ཡང་ལྟུང་བ་མེད་པར་རིག་པར་བྱའོ། །

[Block 4022]
གང་ཞིག་སྦྱོར་བ་ལ༌[^2747]ལྟུང་བ་མེད་པར་བརྗོད་པ་དེ་དག་གིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 4023]
རྙེད་པ་ལ་ནི་གང་ཞིག་ལྟུང་བ་མེད་པའི་ཚིག་ཤིན་ཏུ་མང་བ་ལ་ཡང་འདི་ལྟ་བུ་ལ་འདིར་ཉེས་པ་མེད་པར་བརྗོད་པས་དེ་ལ་གྲུབ་པ་ཉིད་དོ། །

[Block 4024]
རྒྱུ་དང་སྤུན་ལ་ནི་ན་སྨད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་ཚད་དང་ལྡན་པ་ལོངས་སྤྱོད་པར་གྱུར་པ་ལ་སོགས་པའི་རྒྱུ༌[^2748]དང་སྤུན་དག་ལ་ན་སྨད་པ་ཉིད་དོ། །

[Block 4025]
ཆོས་གོས་མི་ཆོག་པ་ཉིད་ཞེས༌[^2749]བྱ་བའི་དོན་ཏོ། །

[Block 4026]
ཉེས་བྱས་ཙམ་ལ་ནི་འདི་བྱེད་པ་པོ་དེ། འདིས་ནི་ཞུ་བ་ལས་ཉེ་དུ་མ་ཡིན་པ་ལས་ཆོས་གོས་མི་ཆོག་པ་ཉིད་སློང་ན་ཉེས་བྱས་ཀྱི་ལྟུང་བར་འགྱུར་རོ། །

[Block 4027]
རྒྱུ་སློང་ན་ཡང་ཉེས་བྱས་སོ། །

[Block 4028]
སྤུན་སློང་ན་ཡང་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་དེ་དག་བསྡུས་པ་ཡིན་ནོ། །

[Block 4029]
དེའི་རང་བཞིན་ནི་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི། རྒྱུ་དང་སྤུན་གྱི་སྐུད་པ་དང་འདྲའོ། །

[Block 4030]
འདིས་ནི་ཐ་ག་བའི་ཞུ་བ་ལས།
--- END BLOCKS ---
