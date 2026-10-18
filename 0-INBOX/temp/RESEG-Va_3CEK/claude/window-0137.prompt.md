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
[Block 4796]
འདི་ལ་ནི༌[^3402]འདི་ལྟར་ཚེ་དང་ལྡན་པ་དེའི་མིང་ནི་འདི་ཞེས་བྱ། རིགས་ནི་འདི་ཞེས་བྱ། རུས་ནི་འདི་ཞེས་བྱ། ཁ་ཟས༌[^3403]ནི་འདི་ལྟ་བུ་ཞིག་ཟ་ཟ། བདེ་བ་དང་སྡུག་བསྔལ་ནི་འདི་ལྟ་བུ་ཞིག་མྱོང་། ཚེ་ནི་འདི་ཙམ་ཞིག་ཐུབ། ཡུན་ནི་ཇི་སྲིད་ཅིག་གནས། ཚེའི་མཐའ་ནི་འདི་ཙམ་ཞིག་གོ་ཞེས་བྱ་བ་འདི་ནི་ཐ་སྙད་ཡིན་ནོ། །

[Block 4797]
དགེ་སློང་དག་དེ་ལྟར་ན་འདི་དག་ནི་མིང་ཙམ། འདི་དག་ཁས་འཆེ་བ་ཙམ། འདི་དག་ནི་ཐ་སྙད་ཙམ་སྟེ། ཆོས་འདི་དག༌[^3404]ཐམས་ཅད་ནི་མི་རྟག་པ། འདུས་བྱས་པ། སེམས་པས་འཕངས་པ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དག་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 4798]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ངེས་པའི་དོན་གྱི་མདོ་ལ་བརྟེན་པར་གསུངས་ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་ཡང་དང་ཡང་དུ་བརྟག་པར་བྱ་བ་ཡིན་ནོ། །

[Block 4799]
དེ་བཞིན་དུ་བྲམ་ཟེ་ཐམས་ཅད་ཡོད་དོ་ཞེས་བྱ་བ་ནི་འདི་ལྟ་སྟེ། སྐྱེ་མཆེད་བཅུ་གཉིས་དག་ཏུ་ཟད་དོ་ཞེས་ཀྱང་གསུངས་སོ། །

[Block 4800]
གལ་ཏེ་གང་ཟག་འདི་སྐྱེ་མཆེད་མ་ཡིན་ན་ནི་དེ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 4801]
འོན་ཏེ་སྐྱེ་མཆེད་ཡིན་ནོ་ཞེ་ན། འོ་ན་ནི་བརྗོད་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 4802]
དེ་དག་གི་ལྟར་ན་ཡང་འདི་སྐད་དུ་དགེ་སློང་མི་ཇི་སྙེད་པ་དང་། གཟུགས་ཇི་སྙེད་པ་ཞེས་བྱ་བ་རྒྱས་པར་གསུངས་ནས། དགེ་སློང་འདི་ཇི༌[^3405]སྙེད་ཅིག་ནི་དེ་བཞིན་གཤེགས་པ༌[^3406]ཐམས་ཅད་འདོགས་པར་མཛད་དོ། །

[Block 4803]
ཐམས་ཅད་བརྟགས༌[^3407]སོ་ཞེས་གསུངས་སོ་ཞེས་འདོན་ཏོ། །

[Block 4804]
གཟུགས་ཅན་སྙིང་པོའི་མདོ་ལས་ཀྱང་། དགེ་སློང་དག་བདག་དང་བདག་གི་ཞེས་བྱ་བ་ནི་བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་ཐོས་པ་དང་མི་ལྡན་པས་བརྟགས་པ་ལ་ལྷུང་བར་ཟད་དེ། འདི་ལ་བདག་གམ་བདག་གི་ནི་མེད་ཀྱི་སྡུག་བསྔལ་འདི་སྐྱེ་བ་ན་སྐྱེ་བར་ཟད་དོ་ཞེས་བྱ་བ་རྒྱས་པར་གསུངས་སོ། །

[Block 4805]
དགྲ་བཅོམ་པ་དྲུག་གིས་ཀྱང་བདུད་ལས་བརྩམས་ནས།

[Block 4806 [VERSE]]
སེམས་ཅན་ཞེས་བྱ་བདུད་ཅི་སེམས། །
ཁྱོད་ནི་ལྟ་བར་གྱུར་པ་ཡིན། །
འདུ་བྱེད་ཕུང་པོ་འདི་སྟོང་སྟེ། །
འདི་ལ་སེམས་ཅན་ཡོད་མ་ཡིན། །

[Block 4807 [VERSE]]
ཇི་ལྟར་ཡན་ལག་ཚོགས་རྣམས་ལ། །
ཤིང་རྟའི་མིང་དུ་བཤད་པ་ལྟར། །
དེ་བཞིན་ཕུང་པོ་རྣམས་བརྟེན་ནས།
ཀུན་རྫོབ་སེམས་ཅན་ཞེས་བྱའོ། །

[Block 4808]
ཞེས་བཤད་དོ། །

[Block 4809]
ལུང་ཕྲན་ཚེགས་ལས་ཀྱང་། བྲམ་ཟེ་རྒྱ་ཤུག་གི་བུའི་དབང་དུ་བྱས་ནས།

[Block 4810 [VERSE]]
ཇི་ལྟར་སེམས་ནི་ཀུན་ཉོན་མོངས། །
ཇི་ལྟར་སེམས་ནི་རྣམ་བྱང་དང་། །
མདུད་པ་ཐམས་ཅད་འཇིག་བྱེད་པའི། །
ཆོས་ནི་རྒྱ་ཤུག་བུ་ཁྱོད་ཉོན། །

[Block 4811 [VERSE]]
བདག་ཉིད་ཀྱིས་ནི༌[^3408]བདག་མེད་དེ། །
ཕྱིན་ཅི་ལོག་གིས་རྟོགས་པར༌[^3409]བྱེད། །
འདི་ལ་བདག་གམ་སེམས་ཅན་མེད། །
ཆོས་འདི་དག་ནི་རྒྱུ་དང་བཅས། །

[Block 4812 [VERSE]]
སྲིད་པའི་ཡན་ལག་བཅུ་གཉིས་དང་། །
ཕུང་པོ་སྐྱེ་མཆེད་ཁམས་རྣམས་ཏེ། །
རྣམ་པར་བསམས་ན་འདི་ཀུན་ལ། །
གང་ཟག་དམིགས་པ་མ་ཡིན་ནོ། །

[Block 4813 [VERSE]]
ནང་གི་སྟོང་པ་ཡིན་པར་ལྟོས། །
ཕྱི་རོལ་གནས་པ་སྟོང་པར་ལྟོས། །
རང་བཞིན༌[^3410]སྟོང་པ་ཉིད་བསྒོམ༌[^3411]པ། །
དེ་ཡང་འགའ་ཡང་མི་དམིགས་སོ། །

[Block 4814]
ཞེས་གསུངས་སོ། །

[Block 4815]
དེ་བཞིན་དུ་བདག་ཏུ་དམིགས་པ་ལ་ཉེས་དམིགས་ལྔ་ཡོད་དོ། །

[Block 4816]
[^3412]བདག་ཏུ་ལྟ་བ་དང་སེམས་ཅན་དུ་ལྟ་བ་དང་། སྲོག་ཏུ་ལྟ་བར་འགྱུར། མུ་སྟེགས་ཅན་རྣམས་དང་ཁྱད་པར་མེད་པར་འགྱུར། །ལམ་གོལ་བར་ཞུགས་པར་འགྱུར། འདིའི་སེམས་སྟོང་པ་ཉིད་ལ་མི་འཇུག་ཅིང་རབ་ཏུ་དང་བར་མི་འགྱུར་ལ་ཡང་དག་པར་མི་གནས་པས་རྣམ་པར་གྲོལ་བར་མི་འགྱུར། འདིའི་འཕགས་པའི་ཆོས་རྣམས་རྣམ་པར་བྱང་བར་མི་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 4817 [HEADING]]
#### གཞུང་འདི་ཚད་མར་མི་བྱེད་པ། ^6-2-6-0

[Block 4818]
དེ་དག་ནི་གཞུང་འདི་ཚད་མར་མི་བྱེད་པ་ཉིད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ཁོ་བོ་ཅག་གི༌[^3413]སྡེ་པ་མི་འདོན་ཏོ་ཞེས་ཟེར་རོ། །

[Block 4819]
ཅི་དེ་དག་ལ་སྡེ་པ་ཁོ་ན་ཚད་མ་ཡིན་ནམ། འོན་ཏེ་སངས་རྒྱས་ཀྱི་བཀའ་ཚད་མ་ཡིན།[^3414] གལ་ཏེ་སྡེ་པ་ཁོ་ན་ཚད་མ་ཡིན་ན་འོ་ན་ནི་དེ་དག་གི་སྟོན་པ༌[^3415]ཡང་སངས་རྒྱས་མ་ཡིན་ལ། ཤཱཀྱའི་བུ་ཡང་མ་ཡིན་པར་འགྱུར། [^3416]འོན་ཏེ་སངས་རྒྱས་ཀྱི་བཀའ་ཚད་མ་ཡིན་ནོ་ཞེ་ན་ནི་གཞུང་འདི་ཅིའི་ཕྱིར་ཚད་མ་མ་ཡིན། འདི་ནི་སངས་རྒྱས་ཀྱི་བཀའ་མ་ཡིན་ནོ། །

[Block 4820]
དེ༌[^3417]ཅིའི་ཅིའི་ཕྱིར་ཞེ་ན་ནི། [^3418]ཁོ་བོ་ཅག་གི་སྡེ་པ་མི་འདོན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 4821]
འདི་ནི་མི་རིགས་པར་ཞུགས་པ་ཡིན་ནོ། །

[Block 4822]
འདིར་མི་རིགས་པ་གང་ཞིག་ཡིན་ཞེ་ན། གཞུང་གང་ཞིག་སྡེ་པ་གཞན་ཐམས་ཅད་ལས་འབྱུང༌[^3419]ལ་མདོ་དང་། ཆོས་ཉིད་དང་ཡང་མི་འགལ་བ་དེ་ཁོ་བོ་ཅག་མི་འདོན་པའི་ཕྱིར་སངས་རྒྱས་ཀྱི་བཀའ་མ་ཡིན་ནོ་ཞེས༌[^3420]སྨྲ་བ་སྟེ། གཟུ་ལུམས༌[^3421]ཙམ་འབའ་ཞིག་ཏུ་ཟད་དོ། །

[Block 4823]
གཞན་ཡང་དེ་དག་ལ་ཆོས་ཐམས་ཅད་ནི་བདག་མེད་པའོ་ཞེས་བྱ་བའི་མདོ་འདི་ཡང་མེད་དམ། གང་ཟག་ནི་ཆོས་ཞེས་ཀྱང་མི་བྱ་ལ་ཆོས་ལས་གཞན་ཞེས་ཀྱང་མི་བྱའོ་ཞེས་བྱ་བར་འདོད་པར་གྱུར་ན། དེ་ལྟ་ན་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པར་བྱ་བར༌[^3422]མི་འགྲུབ་སྟེ། གཉིས་ལ་བརྟེན་ནས་རྣམ་པར་ཤེས་པ་སྐྱེའོ་ཞེས་ངེས་པར་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4824]
བདག་མེད་པ་ལ་བདག་གོ་སྙམ་དུ་འདུ་ཤེས་ཕྱིན་ཅི་ལོག་པ་དང་། སེམས་ཕྱིན་ཅི་ལོག་པ་དང་། ལྟ་བ་ཕྱིན་ཅི་ལོག་པ་ཞེས་བྱ་བ་འདི་ཁོ་ན་ལ༌[^3423]ཡང་ཇི་ལྟར་རྟོག །བདག་མེད་པ་ལ་བདག་གོ་སྙམ་པ་ཕྱིན་ཅི་ལོག་ཡིན་གྱི་བདག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4825]
བདག་མེད་པ་ཡང་གང་ཞིག་ཡིན། ཕུང་པོ་དང་སྐྱེ་མཆེད་དང་། ཁམས་རྣམས་ཡིན་ནོ། །

[Block 4826]
རེ་ཞིག་སྔར་གཟུགས་རྣམས་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱའོ། །

[Block 4827]
[^3424]གཟུགས་རྣམས་མ༌[^3425]ཡིན་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱའོ་ཞེས་སྨྲས་པ་གང་ཡིན་པ་ནི་བསལ་ཏོ། །

[Block 4828]
མདོ་གཞན་ལས།

[Block 4829]
དགེ་སློང་དག་དགེ་སྦྱོང་ངམ་བྲམ་ཟེ་གང་ལ་ལ་བདག་གོ་སྙམ་དུ་རྗེས་སུ་ལྟ་བ་དེ་དག་ཐམས་ཅད་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་འདི་དག་ཁོ་ན་ལ་ཞེས་གསུངས་ཏེ། དེ་ལྟ་བས་ན་བདག་ཏུ་འཛིན་པ་ཐམས་ཅད་ནི་བདག་མེད་པ་ཁོ་ན་ལ་ཡིན་ནོ། །

[Block 4830]
དེ་བཞིན་དུ་གང་ལ་སྔོན་གྱི་གནས་རྣམ་པ་དུ་མ་རྗེས་སུ་དྲན༌[^3426]པར་གྱུར་ཏམ། རྗེས་སུ་དྲན་ནམ། རྗེས་སུ་དྲན་པར་འགྱུར་བ་དེ་དག་ཐམས་ཅད་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་འདི་དག་ཁོ་ན་ལ་ཞེས་གསུངས་སོ། །

[Block 4831]
གལ་ཏེ་དེ་ལྟ་ན་ནི་ཅིའི་ཕྱིར་བདག་ནི་འདས་པའི་དུས་ན་གཟུགས་འདི་ལྟ་བུ་དང་ལྡན་པར་གྱུར་ཏོ་ཞེས་གསུངས།

[Block 4832]
གང་དག་དེ་ལྟར་རྣམ་པ་དུ་མ་རྗེས་སུ་དྲན་པ་ཞེས་བྱ་བ༌[^3427]རབ་ཏུ་སྟོན་པར་བྱེད་དོ། །

[Block 4833]
གལ་ཏེ་གང་ཟག་གཟུགས་དང་ལྡན་པར་ལྟ་བར་གྱུར་ན་འཇིག་ཚོགས་ལ་ལྟ་བར་ཐལ་བར་འགྱུར་བས་འདི་ལ་ནི་མ་བཏོན༌[^3428]པ་ཁོ་ན་སྐྱབས་ཡིན་ནོ། །

[Block 4834]
དེ་ལྟ་བས་ན་གང་ཟག་ནི་བཏགས་པའི་ཡོད་པ་ཡིན་ཏེ། ཕུང་པོ་དང་རྒྱུན་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 4835 [HEADING]]
#### སངས་རྒྱས་ཐམས་ཅད་མཁྱེན་པ། ^6-2-7-0
--- END BLOCKS ---
