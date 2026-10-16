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
[Block 4936 [VERSE]]
འདིས་ནི་ཡོན་ཏན་གྱི་ཞིང་དུ་བསྟན་ཏོ། །
བྱ་བའི་ཁྱད་པར་དག་གིས་བཏང༌[^3192]ན་ནི། །

[Block 4937]
ཞེས་བྱ་བ་ནི་ཕན་འདོགས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4938]
གཉེན་པོ་ཆུང་ན་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དགེ་བའི་ལས་ཡིན་ན་དེའི་གཉེན་པོ་ནི་ཉོན་མོངས་པ་ཡིན་ཏེ་དེ་ཚུང་བའོ། །

[Block 4939]
གལ་ཏེ་མི་དགེ་བའི་ལས་ཡིན་ན་ནི་དེའི་གཉེན་པོ་དགེ་བ་ཡིན་ནོ། །

[Block 4940]
འདིར་གཉེན་པོ་ཞེས་དགོངས་པ་ནི་དགེ་བའི་ལས་ཉམ་ཆུང་བ་ལ་བྱའོ། །

[Block 4941]
དགེ་བ་དང་མི་དགེ་བ་འཕྲལ་དུ་འབྲས་བུ་སྨིན་པ་ཞེས་བྱ་བ་ནི། དེ་ཉིད་དུ་སྨིན་པར་འགྱུར་ཞིང་ལུས་འཇིག་པ༌[^3193]ལ་མི་སྡོད་དེ། དེ་རབ་ཏུ་རྒྱས་པར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4942]
གཉེན་པོ་ཆུང་བས་ན་འབྲས་བུ༌[^3194]དེ་ཙམ་དུ་མྱང༌[^3195]བར་མ༌[^3196]ཟད་དེ། དེ་ནི་མེ་ཏོག་ཙམ་དུ་ཟད་དེ། འབྲས་བུ་གཞན་ཡང་འབྱུང་བར་འགྱུར་རོ། །

[Block 4943]
ཆར་སྤྲིན་འདྲ་བའི་སྔོན་པོ་ནི་ཆར་སྤྲིན་སྔོན་པོ་འདྲ་བའོ། །

[Block 4944]
ལྟོང༌[^3197]དུ་བཅུག་ཅིང་གཞུ་བཀང་བ་ནི་འཕེན་པར་འདོད་པ་སྟེ། ད་ཅུང་འཕངས་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 4945]
དེ་བཟུང༌[^3198]འདོད་པ་ཡིས་ཞེས་བྱ་བ་ནི་རི་དགས་རུ་རུ་དང་ཉེ་བར་གནས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4946]
རེ་ཞིག་གཞེས་ཞེས་བྱ་བ་ནི་ཉེ་བར་བསྙན༌[^3199]ནས་སྨྲས་པ་ཡིན་ཏེ། འདི་གཉི་ག་ཅིའི་ཕྱིར་ཐོབ་པར་འགྱུར་ཅེས་པ་སྟེ། དེ་ཉིད་སྨྲས་པ། ངོ་མཚར་ཆེན་པོ་བསལ་བའི་ཕྱིར་ཏེ།

[Block 4947 [VERSE]]
ཕྱེ༌[^3200]ནས་སྨྲའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
སྐྱེ་བོ་རྒྱུན་ལུགས་མེད་པ་ན། །

[Block 4948]
ཞེས་བྱ་བ་ནི་འདིར་གང་ཡང་འོང་བ་མ་མཐོང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4949]
ནགས་ཚལ་སྟུག་པོ་འདི་ལྟ་བུ། །ཞེས་བྱ་བ་ནི་བདག་ཀྱང་གཞན་དུ་མ་སོང་སྟེ། དེས་ན་ཡང་བདག་མཐོང་བ་མེད་དོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4950]
དེ་ལྟར་རྣམ་པ་གཉི༌[^3201]གས་ཀྱང་མཐོང་བ་མེད་ན་སུ་ཡིས་བདག་མཆིས་པར་གསོལ་བ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདི་ལྟར་སྔར་ཆུའི་རྒྱུན་ལས་བསྒྲལ་བའི་མི་དེས་གསོལ་བ་ཡིན་ནོ་ཞེས་དོགས་པ་སྐྱེས་པ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན་བྱས་པ་གཟོ་བ་མི་སྲིད་པའི་ཚུལ་ཡིན་ཏེ། དེ་བས་ན་སྨྲས་པ། སུ་ཡིས་བདག་མཆིས་གསོལ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4951]
སྔར་རྨི་ལམ་དུ་ཐོས་པ་བས་ཀྱང་ལྷག་པར་དུལ་བར་གྱུར་པ་དེ་བས་ན་རབ་ཏུ་ཞེས་བྱའོ། །

[Block 4952]
ངན་པ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གྱིས་སྨད་པའོ། །

[Block 4953]
བདག་ལ་ཕན་གདགས་པ་དང་། ཁྱོད་ལ་ཕན་པ་དེ་གཉི་ག་ལ་སྟོས་པ༌[^3202]མེད་པའི་དབང་དུ་བྱས་ནས། དེ་ལྟར་འབད་པ་དེ་ཡི་ལན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4954]
དེ་གཉི་ག་ལ་སྟོས་པ༌[^3203]མེད་པ་ཉིད་ནི་ཁྲེལ་མེད་མི་དག་ཅེས་བྱ་བ་བསྒྲུབས་པ་ཡིན་ནོ། །

[Block 4955]
དམིགས་ཀྱིས་མ་ཕྱེ་བའི་དོན་གང་ཡིན་པ་དེ་ནི་དམིགས་ཀྱིས་མ་ཕྱེ་བའི་དོན་ནོ། །

[Block 4956]
དམིགས་ཀྱིས་མ་ཕྱེ་བའི་དོན་ཡང་ཡིན་ལ་ཟབ་པ་ཡང་ཡིན་པས་དམིགས་ཀྱིས་མ་ཕྱེ་བའི་དོན་ཟབ་བའོ། །

[Block 4957]
སྨད་པ་ཞེས་བྱ་བ་ནི་བཤུད་པའོ། །

[Block 4958]
མི་མ་ཡིན་ཞེས་བྱ་བ་ནི་ཤ་ཟ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4959]
མི་འམ་འོན་ཏེ་མི་མ་ཡིན། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་ནི་དེ་དག་དེ་ན་ཡོད་པའི་ཕྱིར་རོ། །

[Block 4960]
འདི་ནི་གཞན་ལ་སྨད་པ་ལགས།[^3204] །ཞེས་བྱ་བ་ནི་དགོས་པ་མེད་པར་སྨད་པ་མ་ཡིན་ཏེ། འོན་ཀྱང་དགོས་པ་དང་བཅས་པ་མ་ཡིན་ནོ། །

[Block 4961]
དགོས་པ་དེ་གང་ཡིན་ཞེ་ན། སྨྲས་པ། ལས་འདི་སྨད་པར༌[^3205]འོས་པའི༌[^3206]ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ལས་འདི་སྨད་པར་འོས་པའི་རྒྱུ་ཉིད་དོ། །

[Block 4962]
འཁྱམས་པ་ལ་ཚིག་རྩུབ་པོ་ཞེས་བྱ་བ་དེའི་དཔེའི་དབང་དུ་བྱས་ནས། སྨད་པའི་རྨ་ལ་སུ་ཞིག་ཞིགས་པར་བགྱིས། །ཞེས༌[^3207]བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4963]
འདིའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་གོ་རིམས་བཞིན་དུ་འདི༌[^3208]ནི་གཞན་ལ་སྨད་པ་མ་ལགས་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། འཁྱམས་པ་དག་ལ་ཚིག་རྩུབ་པོས༌[^3209]བྱ་བ་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 4964]
ཚིག་དེའི་དགོས་པ་ཡོད་པའི་ཕྱིར་དཔེའི་དབང་དུ་བྱས་ནས། སྡུག་པའི་བུ་ལ་སྨན་དཔྱད་ལ་འཇུག་པ་བཞིན་དུའོ། །

[Block 4965]
འབབ་ཆུ་དྲག་པོས་ཁྱེར་ཏེ་སོང་བ་ཞེས་བྱ་བ་ནི། སྙིང་རྗེའི་གནས་ཀྱི༌[^3210]དབང་དུ་བྱས་པའོ། །

[Block 4966]
སྙིང་རྗེའི་དབང་གིས་ཞེས་བྱ་བ་ནི་བསམ་པ་དག་པའི་དབང་དུ་བྱས་པའོ། །

[Block 4967]
དབང་གིས་ཕྱུང་བ་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་ལ་འཇུག་པའི་རྒྱུ་ཡིན་གྱི། གཞན་གྱི་རྒྱུ་མ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 4968]
མི་དེ་འཇིགས་ཤིང་སྐྲག་ལ་རྔུལ་གྱིས་མདོག་ཉམས་ཤིང་གཅོམ་བསྐྱུངས༌[^3211]ཏེ་ཞེས་བྱ་བ་ནི། དེ་ལྟར་བྱ་བ་མ་ཡིན་པ་བྱས་པའི་མཚན་མའོ། །

[Block 4969]
མཚུངས་པའི་ནང་ཞེས་བྱ་བ་ནི། དམ་པ་མི༌[^3212]རྣམས་དང་འདྲ་བའི་དོན་ཏོ། །

[Block 4970]
དེ་གཉིས་ཀྱི་བར་ཞེས་བྱ་བ་ནི་མི་དང་མཚམས་སུའོ། །

[Block 4971]
མཐོང་བའི་ཆོས་ལ་ཇི་ལྟར་བསོད་ནམས་ཟད་པ་ཡིན་ཞེ་ན། བསོད་ནམས་ཟད་པའི་ཉེས་པ་བསྟན་པའི་ཕྱིར། །སྡུག་བསྔལ་བཟོད་པར་དཀའ་བས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4972]
འདི་ལྟ་བུར་ནི་བརླག་པར་འགྱུར། །ཞེས་བྱ་བ་ནི་བྱ་བ་མ་ཡིན་པ་བྱེད་པས་ལྟུང་བ་སྟེ། བྱ་བ་མ་ཡིན་པ་བྱས་པས་བརླག་པ་ནི་ངན་སོང་གི་སྡུག་བསྔལ་ཡིན་ཏེ། བརླག་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4973]
འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་འདོད་པས་བསླུས། །ཞེས་བྱ་བ་ནི། ངན་འགྲོར་འགྲོ་བའི་ལས་དེ༌[^3213]འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་འདོད་པ་ལ་བསླུས་པའི་ཕྱིར་རོ། །

[Block 4974]
ཕྱེ་མ་ལེབ་བྲིད་པ་དང་འདྲ་བ་ནི༌[^3214]ངན་འགྲོར་འགྲོ་ཞིང་བརླག་པའི་རྒྱུར་གྱུར་པའི་ལས་ཀྱི་ལྟུང་བའོ། །

[Block 4975]
དེ་བས་སྙིང་རྗེ་ཞེས་བྱ་བ་ལ་འདིར་དེ་བས་ཞེས་བྱ་བ་ནི། འཇིག་རྟེན་གཉིག་ལ་ཕན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
