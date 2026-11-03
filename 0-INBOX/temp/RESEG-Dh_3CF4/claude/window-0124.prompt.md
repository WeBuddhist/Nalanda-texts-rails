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
[Block 4341]
ཁྱོད་ནི་ཇི་ལྟར་བདག་ལ་སེམས་མི་དགའ། །ཞེས༌[^2786]བྱ་བ་ལ། སེམས་མི་དགའ་བ་དེ་ཉིད་བསྟན་པའི་ཕྱིར། གཞན་གྱི་ཉེས་པ༌[^2787]བདག་ལ་ཅི་ཕྱིར༌[^2788]བསྒོ།[^2789] །ཅེས་བྱ་བ་ཡིན་ཏེ། གཞན་གྱི་ཉེས་པ་ནི་དབང་ཕྱུག་གི་ཉེས་པས་སོ། །

[Block 4342]
སྡིག་པ་ཆེན་པོ་མ་ལུས་པ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི། སྤྲེའུ་བསད་པས་ནི་སྡིག་པ་ཉིད་དུ་ཁས་ལེན་པའི་ཕྱོགས་སྔ་མ་དང་འགལ་བའི་ཉེས་བ་ཉིད༌[^2790]བསྟན་ཏོ། །

[Block 4343]
དེ་སྟེ་སྤྲ༌[^2791]ཆེན་དཔའ་བོ་དེ་ཤི་བ། །ཞེས་བྱ་བ་འདིས་ནི་གྲུབ་པའི་མཐའི་སྐྱོན་བསྟན་ཏོ། །

[Block 4344]
ཡང་ན་དེ༌[^2792]གཉིས་གཅིག་ལ་གཅིག་འགལ་བའི་སྐྱོན་བསྟན་ཏོ། །

[Block 4345]
དབང་ཕྱུག་འགྲོ་བ་ཐམས་ཅད་ཀྱི་བྱེད་པ་པོ་ཉིད་ཡིན་ན་ནི༌[^2793]སྐྱེས་བུ་བྱེད་པའི་རྩོལ་བ་ཐམས་ཅད་དོན་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལས་བརྩམས་ཏེ། དབང་ཕྱུག་ལ་ནི་རེ་བ་ཡིས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4346]
ཐམས་ཅད་ཀྱི་བྱེད་པ་པོ་དབང་ཕྱུག་ནི་བྱེད་པའི་རྒྱུ་མ་ཡིན་ཏེ། དབང་ཕྱུག་གིས་བྱེད་པའི་སྐྱོན་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4347]
སྡིག་པ་ཆེན་པོ་མ་ལུས་པ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4348]
སྐྱོན་དེ་ཉིད་ཀྱིས་དབང་ཕྱུག་ཉིད་མེད་པར་ཚིགས་བཅད་འདིས་སྟོན་ཏོ། །

[Block 4349]
ཡང་ན་དེས་ལྟུང་བས་མི་བྱེད་ན་ནི་གྲུབ་པའི༌[^2794]མཐའ་དང་འགལ་བར་བསྟན་པའི་ཕྱིར། སྡིག་པས་འཇིགས་ནས་དེ་དག་ཀུན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4350]
དབང་ཕྱུག་ཆེན་པོ་ཉིད་དུ་འདོད་པ་དེ་ལ། དབང་ཕྱུག་ཆེན་པོ་མེད་པར་བསྟན་པའི་ཕྱིར། དེ་ཡང་དབང་ཕྱུག་འགྱུར་བ་ནི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4351]
དབང་ཕྱུག་ཉིད་དུ་ནི་རྒྱུ་དང་བཅས་པའམ། རྒྱུ་མེད་པ༌[^2795]ཡིན་གྲང་ན་རྒྱུ་དང་བཅས་པ་ནི་ཆོས་ཀྱི་རྒྱུ་ཉིད་དུ་འགྱུར་བའམ་དེ་ལས་རྒྱུ་གཞན་པའི་རྒྱུ་ཉིད་ཡིན་པ༌[^2796]ཞིག་གོ། །

[Block 4352]
དེ་ལ་ཆོས་ཀྱི་རྒྱུ་ཉིད་ཡིན་ན་ནི་ཆོས་ལས་སྔ་རོལ་དུ་དབང་ཕྱུག་མེད་དོ། །

[Block 4353]
དེ་སྟེ་དབང་ཕྱུག་གིས་དབང་ཕྱུག་གཞན་ཉིད་ཕྱུང་ན་ནི་དབང་ཕྱུག་ཀྱང་ཉམས་པ་ཡིན་ཏེ། དེས་ན་དབང་ཕྱུག་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4354]
གཞན་དུ་ན་དབང་ཕྱུག་ཉིད་ཀྱི་རྒྱུ་ཉིད༌[^2797]ཡིན་ན་ནི། བདག་གིས་སྤྲེའུའི་རྒྱལ་པོ་བསད་པ་ལ་སྡིག་པ་ཡིན་ནོ་ཞེས་ཁས་བླངས་པའི་ཕྱོགས་སྔ་མ་དང་འགལ་བའི་ཉེས་པ་མེད་དོ། །

[Block 4355]
གལ་ཏེ་ཐམས་ཅད་སྔོན་གྱི་ལས་ཀྱིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི༌[^2798]སྤྲེའུ་བསད་པ་ལས་སྡིག་པ་ཉིད་དུ་ཁས་ལེན་པའི་ཕྱོགས་སྔ་མ་དང་འགལ་བ་བསྟན་པའི་ཕྱིར། གལ་ཏེ་ཐམས་ཅད་སྔོན་གྱི་ལས་ཀྱིས་བྱས་ན་ནི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། གང་གི་ཕྱིར་བདག་ལ་སྨད་ཅེས་བྱ་བ་ནི་བདག་གི་ཕྱིར་སྡིག་པས་སོ། །

[Block 4356]
དེ་སྟེ༌[^2799]བདག་གིས་སྤྲེའུ་བསད་པའི༌[^2800]སྡིག་ཡོད་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་གྲུབ་པའི་མཐའ་ཉམས་པ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 4357]
ཅི་སྟེ་ལས་དང་ལས་ཀྱི་རྒྱུ་ཉིད་ཡོད་པར་སྟོན་ཏེ། སྔར་བཤད་པའི་ལས་ཀྱིས་བྱས་པ་སྟེ། ལས་གང་གིས་སྤྲེའུ་དེ་བསད་པའི་ལས་བྱས་པ་ཡིན་ནོ་ཞེས་དེ་ལྟར་འདོད་ན་ནི་ཐར་པ་མེད་པའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་རོ་ཞེས་བསྟན་པའི་ཕྱིར། གལ་ཏེ་ལས་དང་ལས་ཀྱི་རྒྱུ་ཡོད་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཡིན་ནོ། །

[Block 4358]
སྤྲེའུ་བསད་པའི་ལས་བྱས་པ་དེ་ཡང་སྤྲེའུ་བསད་པའི་ལས་གཞན་གྱི་རྒྱུས་ཡིན་ནོ། །

[Block 4359]
དེ་ཡང་གཞན་དང་གཞན་གྱི་ཡིན་པས་ཐར་པ་མེད་པར་ཐལ་བར་འགྱུར་ཏེ།

[Block 4360 [VERSE]]
ལས་རྗེས་སུ་མ་སྤྱད་པའི་ཕྱིར་རོ། །
སྔོན་གྱི་ལས་ཀྱིས་བྱས་པ༌[^2801]ངེས་པར་མངོན། །

[Block 4361]
ཞེས་བྱ་བ་ཡིན་ན་ནི། རྒྱུ་དང་རྐྱེན་གཞན་བདེ་བ་དང་སྡུག་བསྔལ་གཉིས་འགོག་པར་འགྱུར་ཏེ། དེ་རྒྱུ་དང་རྐྱེན་གཞན་གྱིས་ཀྱང་། སྡུག་བསྔལ་རྒྱུ་ཡང་གལ་ཏེ་བདེ་བར་འགྱུར། །ཞེས༌[^2802]དང་། བདེ༌[^2803]དང་སྡུག་བསྔལ་དེ་ལྟར་གྱུར་པའང་མེད། །ཅེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། འདིས་ཀྱང་འགོག་པ་ཡིན་ཏེ། ཉེ་བར་གྱུར་པའི་རྐྱེན་དང་ད་ལྟར་བྱུང་བའི་སྐྱེས་བུའི་བྱེད་པ་སྟེ། ཡུལ་ཉེ་བར་གྱུར་པའི་ཡུལ་གྱི་རྐྱེན་དང་། ད་ལྟར་བྱུང་བའི་སྐྱེས་བུའི་བྱེད་པའོ། །

[Block 4362]
དེ་ལ་ཡུལ་ཉེ་བར་གྱུར་པ་ཉིད་ཀྱི་བདེ་བ་དང་། སྡུག་བསྔལ་གཉིས་བསྟན་པའི་ཕྱིར། སྡུག་བསྔལ་རྒྱུ་ཡང་གལ་ཏེ་བདེ་བར་འགྱུར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4363]
སྡུག་བསྔལ་གྱི་རྒྱུ་ནི་ཡིད་དུ་མི་འོང་བ་སྟེ། དེས་ན་བདེ་བ་དང་སྡུག་བསྔལ་གཉིས་ནི་ཡིད་དུ་འོང་བ་དང་ཡིད་དུ་མི་འོང་བ་ལས་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 4364]
ངེས་པ་ཞེས་བྱ་བ་ནི་གདོན་མི་ཟ་བར་ཞེས་པའི་དོན་ཏོ། །

[Block 4365]
སྔོན་གྱི་ལས༌[^2804]ཀྱིས་བྱས་པ་ཞེས་བྱ༌[^2805]བ་ནི། སྔོན་གྱི་ལས་ཉིད་ཀྱིས་བྱས་པ་གང་ཡིན་པ་སྟེ།

[Block 4366 [VERSE]]
རྒྱུ་གཞན་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །
བདེ༌[^2806]དང་སྡུག་བསྔལ་དེ་ལྟར་གྱུར་པའང་མེད། །

[Block 4367]
ཅེས་བྱ་བ་དང་པོའི་ཕྱེད་ཀྱིས་ནི་བསྟན་མ་ཐག་པའི་དོན་མཇུག༌[^2807]བསྡུ་བའི་ཕྱིར་རོ། །

[Block 4368]
ཚིགས་བཅད་ཕྱེད་འོག་མས་ནི་ད་ལྟར་བྱུང་བའི་སྐྱེས་བུ་བྱེད་པའི་རྐྱེན་གྱིས་དངོས་པོའི་སྐྱོན་བསྟན་པའི་ཕྱིར་ཏེ། དེ་ལྟར་ཞེས་བྱ་བ་ནི་བདེ་བ་དང་སྡུག་བསྔལ་པ་དག་ལ་ཡིད་དུ་འོང་བ་དང་ཡིད་དུ་མི་འོང་བའི་ཡུལ་མངོན་སུམ་དུ་གྱུར་པས་ཡིན་གྱི། སྔོན་གྱི་ལས་ཀྱིས་བདེ་བ་དང་སྡུག་བསྔལ་བྱས་པ་མ་ཡིན་ནོ་ཞེས་བརྒྱ་ལ་དེ་སྨྲ་ན། དེ་ལྟ་མོད་ཀྱི། བདེ་བ་དང་སྡུག་བསྔལ་ཡུལ་གྱི་རྐྱེན་ལས་བྱུང་བ་ཡིན་ནོ་ཞེས་དེ་ལྟར་སྨྲས་པས་ད་ལྟར༌[^2808]བྱུང་བའི་སྐྱེས་བུ་བྱེད་པའི་ལས་བསལ་བ་ཡིན་ཏེ། དེ་མེད་པའི་སྐྱོན་བསྟན་པའི་ཕྱིར་སྨྲས་པ། གསར་དུ་བྱས་པའི་ལས་ཀྱང་ཇི་ལྟར་འགྱུར། །ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4369]
[^2809]གསར་དུ་བྱས་པའི་ལས་མ་གྲུབ་ན་སྐྱོན༌[^2810]ཡོད་ཅེ་ན། དེའི་སྐྱོན་བསྟན་པའི་ཕྱིར་སྨྲས་པ། དེ་མ་གྲུབ་ན་སྔ་མའང་ཇི་ལྟར་འགྲུབ། །ཅེས་བྱ་བ་ཡིན་ཏེ། དེ་མ་གྲུབ་ན་ཞེས་བྱ་བ་ནི་གསར་དུ་བྱས་པའི་ལས་མ་གྲུབ་ནའོ། །

[Block 4370]
ཀུན་ཞེས་བྱ་བ་ནི་སྤྲེའུ་བསད་པ་ལ་སོགས་པའོ། །

[Block 4371]
བདག་གིས་བྱས་པར་ཞེས་བྱ་བ་ནི་སྔོན་གྱི་ལས་ཀྱིས་བྱས་པ་འདི་དག་ལ་བདག་གིས་བྱས་པར་ཡོངས་སུ་བརྟག་པ་ནི་མི་རིགས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4372]
ཕྱོགས་སྔ་མ་སྤྲེའུ་བསད་པ་ལ་སྡིག་པ་ཡོད་དོ་ཞེས་སྨྲས་པ༌[^2811]དང་འགལ་བར་བསྟན་པའི་ཕྱིར་སྨྲས་པ། གལ་ཏེ་ཆད་པར་ལྟ་བ་དེ་ཁོ་ན་ཉིད་ཡིན་པར་སེམས་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4373]
ཅི་ཞིག་སྤང་ཞེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་སྤང་བའོ། །

[Block 4374]
ཅི་ཞིག་འབད་དུ་ཡོད་ཅེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་འབད་དུ་ཡོད་པའོ། །

[Block 4375]
ཡང་ན་ཅི་ཞིག་ཅེས་བྱ་བའི་སྒྲ་ནི་དྲི་བའི་ཚིག་གོ། །

[Block 4376]
རང་དགར་ཅི་བདེར་སྤྱོད་པར་རིགས་པ༌[^2812]གང་ཡིན་པ་དེ་ནི་རང་དགར་ཅི་བདེར་སྤྱད་པར་རིགས་ཏེ། སྡིག་པ་དང་དགེ་བ་དག་ལ་སྤང་བ་དང་། བསྟེན་པའི་ཉེས་པ་དང་ཡོན་ཏན་མེད་པས་སོ། །

[Block 4377]
དེ་ལྟ་མོད་ཀྱི་འཇིག་རྟེན་པ་རྣམས་ཀྱི་ཁ་ན་མ་ཐོ་བས་འཇིགས་པར༌[^2813]བྱེད་དོ་ཞེས་དེ་ལྟར་རྟོག་ན་ཡང་སྨྲས་པ། འགྲོ་བས༌[^2814]འཕྱ་བ་དག་གིས་འཇིགས་ནས་སུ། །ཞེས་བྱ་བ་སྨོས་ཏེ། འཇིག་རྟེན་གྱིས༌[^2815]མི་སྨན་པར༌[^2816]སྨྲ་བས་འཇིགས་པའོ།[^2817] །བདག་གི་ཚིག་དང་མི་མཐུན་སྤྱོད་པ་ཡིན། །ཞེས་བྱ་བ་ནི་སྡིག་པ་བསྟེན་པ་དང་། དགེ་བ་སྒྲུབ་པ་ལ་སྐྱོན་དང་ཡོན་ཏན་མེད་དོ་ཞེས་སྨྲ་ན་སྡིག་པ་བསྟེན་པ་དང་། དགེ་བ་བསྟེན་པར་བྱེད་པ་ཡིན་པས་ན་བདག་གི་ཚིག་དང་མི་མཐུན་པར་སྤྱོད་པ་ཡིན་ཏེ། འགྲོ་བས༌[^2818]འཕྱ་བའི་ཉེས་པས་འཇིགས་པས་ནི༌[^2819]རང་གི་ཚིག་དང་མི་འགལ་བར་སྤྱོད་པའོ། །

[Block 4378]
དེ་ཡོད་ན་ནི་དེ་དག་ཀྱང་ཡོད་ཀྱི་ཆད་པར་སྨྲ་བ་འདི་ལ་ནི་འགྲོ་བས༌[^2820]འཕྱ་བའི་ཉེས་པ་མེད་དོ། །

[Block 4379]
འགྲོ་བས༌[^2821]འཕྱ་བའི་སྐྱོན་གཅིག་པུར༌[^2822]མ་ཟད་དེ། འདི་ལྟར་རང་གི་གྲུབ་པའི་མཐའི༌[^2823]ལས་བསྟན་པའི་བདེ་བའང་མི་འཐོབ་པ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར། འཇིག་རྟེན་ཚུལ་ལ་གནས་པར་གྱུར་ན་ནི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། རང་གི་གཞུང་ལུགས་ཞེས་བྱ་བ་ནི་རང་གི་གྲུབ་པའི་མཐའོ། །

[Block 4380]
རང་གི་གྲུབ་པའི་མཐའ་སྨྲ་བ་འཁྲུལ་པས་དོན་མེད་པར་འགྱུར་བ་ནི་བདེ་བ་འཐོབ་པ་སྟེ། དེ་བས་ན་འགྲོ་བས༌[^2824]འཕྱ་བར༌[^2825]འཇིགས་ན་རང་གི་གྲུབ་པའི་མཐའི་འབྲས་བུ་མི་ཐོབ་པས་སྨྲ་བ་དོན་མེད་པ་ནི་འཁྲུལ་པ་ཡིན་པས་སྨྲ་བ་འཁྲུལ་པའོ། །
--- END BLOCKS ---
