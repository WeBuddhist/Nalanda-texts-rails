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
གཞུང་ཁ་ཅིག་ལས་དགེ་སློང་གིས་ཆོས་གོས་དེ་ཉིད་དགུང་བཅུ༌[^2604]འདས་པ་ཡང་ལགས་ལ་དགུང་གཅིག་བྲལ་བ་ཡང་ལགས་པ་མཆིས་སམ། བཀའ་སྩལ་པ་ཡོད་དེ། ཆོས་གོས་ཞག་བཅུ་འདས་པ་ཡང་ཡིན་ལ་དགེ་སློང་གིས་ཀྱང་དེ་བྱིན་གྱིས་བརླབས་ཏེ་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སྐྱ་རེངས༌[^2605]འཆར་བར་བྱེད་པའོ་ཞེས་གསུངས་ཏེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 3782]
དགེ་སློང་གིས་ཀྱང་དེ་བྱིན་གྱིས་བརླབས་ནས་ཞེས་བྱ་བ་ལ་དེ་བྱིན་གྱིས༌[^2606]བརླབས་ཏེ་ཞེས་བྱ་བའི་ཚིག་ནི་འདིར་འཆད་པ་ཞེས་མཐོང་བ་ཡིན་ནོ། །

[Block 3783]
དགེ་འདུན་གྱི་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབས་པ་མི་འཆགས་པ་མ་ཡིན་ནོ། །

[Block 3784]
རང་ཉིད་ཁོ་ནས་དགེ་སློང་ལ་དགེ་འདུན་གྱི་ཉེ་བར་ལོངས་སྤྱོད་པའི་དུས་ན་རྣམ་པར་གཞག་པ་དེ་བཞིན་དུ་མང་པོ་ཡོངས་སུ་ཐོབ་པ་རེ་རེ་ནས་ཉེ་བར་ལོངས་སྤྱོད་པ་ལ་མང་པོ་དང་འབྲེལ་པའི་དོན་ཉིད་ཀྱི་ཕྱིར་དེ་ལས་འབྲལ་བར་འགྱུར་རོ། །

[Block 3785]
དེ་ལས་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་བྱིན་གྱིས་བརླབས་པ་དེ་ལས་འདིར་བྱིན་གྱིས་བརླབས་པ་བཟུང་བ་ནི་རྒྱུ་ཡིན་ཏེ། ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་བཟུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 3786]
དེ་བས་ན་དགེ་འདུན་གྱིས༌[^2607]བྱིན་གྱིས་བརླབས་པ་ལས་འབྲལ་པར་ཡང་འགྱུར་བ་ཁོ་ནའོ། །

[Block 3787]
གཞན་གནས་པས་གཞན་གྱི་གནས་མི་ཉམས་སོ་ཞེས་བྱ་བ་ལ། གཞན་གྱི་ཞེས་བྱ་བ་ནི་མཚན་ཐ་དད་པ་བསྙེན་པར་རྫོགས་པ་འམ་བསྙེན་པར་རྫོགས་པ༌[^2608]མ་ཡིན་པ་བྱིན་གྱིས་བརླབས་པར་གྱུར་པའི་གནས་ལས་གནས་གཞན་ཉིད་གང་ཡིན་པ་དེར་བྱིན་གྱིས་བརླབས་པས་སམ། གཞན་དུ་ན་བསྙེན་པར་རྫོགས་པ་ཉིད་དེ་ནི༌[^2609]ཉམས་པ་མ་ཡིན་ཏེ་བྲལ་བ་མ་ཡིན་པའོ། །

[Block 3788]
གནས་གཞན་དུ་བྱིན་གྱིས་བརླབས་པ་གཞན་ལ་བྲལ་བ་མ་ཡིན་པ་སྟེ་ཞེས་བྱ་བ་འདི་ཡང་འདིའི་རྗེས་སུ་འབྲངས་ཏེ་རྟོགས་པར་བྱའོ། །

[Block 3789]
འདིར་གཞུང་ནི་ཡི་གེ་ཁ་ཅིག་ལས་དགེ་སློང་ལ་ལ་ཞིག་མུ་སྟེགས་ཅན་གྱི་གནས་སུ་ཆོས་གོས་བཞག་སྟེ། དགེ་འདུན་གྱི་གནས་ཉེན་གོར་གཅིག་པར་གནས་པར་བགྱིས་ན་ལྟུང་བར་མི་འགྱུར་བ་མཆིས་སམ། བཀའ་སྩལ་པ་ཡོད་དེ། གང་ཞིག་མུ་སྟེགས་ཅན་དང་ལྷན་ཅིག་བསྐོས་པར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3790]
དེ་བཞིན་དུ་ཤིང་ལྗོན་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 3791]
དངོས་པོ་གཅིག་ལ་འཇུག་པར༌[^2610]རྣམ་པར་རྟོག་པ༌[^2611]ཙམ་དུ་འདིར་བསྐོས་པར་རིག་པར་བྱའོ། །

[Block 3792]
ཆོས་འདི་པ་དང་གཞན་པ་དག་ནི་ལྟ་བ་ལས་ཤེས་པས་མ་འཕངས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་འཛིན་པ་པོ་རྣམས་རྣམ་པར་འབྱེད་པ་ལ་ལྟ་བ་ལས་དབྱེ་བ་ཞེས་བྱ་བ་འདིས་ཆོས་གཞན་པ་དང་འདི་པ་དག་མ་འཕངས་པ་མ་ཡིན་ནོ། །

[Block 3793]
ཐུན་མོང་བ་དག་གི་སྒོ་གང་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་གནས་དུ་མ་ཉིད་ཀྱི་ཕྱིར་སྒོ་ལ་སོགས་པ་ནི་ཐུན་མོང་བར་བརྗོད་དོ། །

[Block 3794]
དེས་ནི་སྒོ་གང་ཡང་མ་བསྡུས་པ་མ་ཡིན་ཏེ་བསྡུས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 3795]
མདོ་འདི་གཉིས་ཀྱི་གཞུང་ནི་འདི་ཡིན་ཏེ་དགེ་འདུན་གྱི་གནས་དང་མུ་སྟེགས་ཅན་གྱི་གནས་ཉེན་ཀོར་གཅིག་པར་གནས་པར་བྱེད་ན་སྒོ་ཁང་དུ་གནས་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་གྲགས་པར་གྱུར་པ་དེ་བས་ན་འདི་དང་ཐ་མི་དད་པ་ཉིད་དོ། །

[Block 3796]
ནོར་ལས་ཞེས་བྱ་བས་ཕ་དང་བུ་དག་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཉེ་བར་འཛིན་པ་པོ་རྣམས་ཐ་དད་པ་ནི་ནོར་ལས་གནས་ཀྱི་དབྱེ་བ་ཞེས་བྱ་བ་འདིས་ཕ་དང་བུ་དག་ཀྱང་འཕངས་པ་ཁོ་ནའོ། །

[Block 3797]
སྤངས་པ་ཉིད་ཀྱང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་རྣམ་པར་འབྱེད་པ་ཉིད་ལ་ཐ་དད་པ་ཉིད་དང་། ནོར་གྱིས་རྣམ་པར་འབྱེད་པ་ཉིད་མ་ཡིན་པ་ལ་ནོར་གྱིས་ཐ་དད་པ་ཉིད་མ་ཡིན་པ་ཞེས་བྱ་བ་འདི་གང་ཞིག༌[^2612]འདིར་ལྷུང་བཟེད་ཁ་སྦུབ་པས་སམ་ཁྲིམས་སུ་བྱས་པས་སྤངས་པ་ཉིད་ཀྱང་དེ་དང་འདྲ་བར་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3798]
ཟས་དང་བཅས་པ་ཉིད་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རྣམ་པར་འབྱེད་པ་ཉིད་ལ་ཐ་དད་པ་ཉིད་དང་ནོར་གྱིས་ཀྱང་རྣམ་པར་འབྱེད་པ་ཉིད་མ་ཡིན་པ་ཉིད་ལ་ཐ་མི་དད་པ་ཉིད་དོ། །

[Block 3799]
ཐ་མི་དད་པ་ཉིད་ཅེས་བྱ་བ་འདི་ཁ་ཟས་དང་བཅས་པ་ཉིད་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3800]
ཁང་པ་གཅིག་པ་ཉིད་དང་ཤིང་ཆེ་བ་གཅིག་པ་ཉིད་དང་གཅིག་པར་གྱུར་པ་ཉིད་ལ་གཞན་སུ་དག་རྣམས་ལ་ཆོ་ག་འདི་སྦྱར་བའོ། །

[Block 3801]
ཉལ་པོ་བྱེད་པར་ཤོམ་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་འདིར་འདུག་ནས་གནས་པ་བརྟག་པར་བྱེད་ཅིང་འཁྲིག་པའི་ཚད་དང་ལྡན་པ་ལྟུང་བྱེད་རྣམས་ལ་ཞེས་བྱ་བ་འདི་ལ་འདི་བསྟན་པའོ། །

[Block 3802]
འདིར་གཞུང་ནི་ཕྲན་ཚེགས་ཀྱི་ཞུ་བ་ལྷུང་བཟེད་ཁ་སྦུབ་པ་ལས།

[Block 3803]
ཁྱིམ་བདག་ལ་ཁྱིམ་ཞིག་ཡོད་ལ༌[^2613]དེ་ལ་དུ༌[^2614]རབ་ཏུ་མང་པོ་དག་བདོག་ཅིང་དེ་ཡང་ནོར་ཐ་དད་པའི་ཁྱིམ་མ་ཡིན་པ་ལ་ཁྱིམ་བདག་རྣམས་ཀྱང་ལྷན་ཅིག་གནས་པ་ཡིན་ན་ཁྱིམ་གཅིག༌[^2615]ཡིན་པར་བརྗོད་པར་བྱ་སྟེ། འདིར་ཕྱིས་གནོན་མ་བྱས་ཤིང་ཡོངས་སུ་གཅོད་པར་མི་འགྱུར་ནའོ། །

[Block 3804]
གལ་ཏེ་དེས་སླར་ནོར་བགོས་པར་གྱུར་ན་ཁྱིམ་ཐ་དད་པ་བརྗོད་པར་བྱ་སྟེ། བུ་དེ་རྣམས༌[^2616]ཇི་སྙེད་པ་དག་དང༌[^2617]འབྲེལ་པ་ཇི་སྙེད་པ་ཡོད་པ་རྣམས་དང་མནའ་མ་ཇི་སྙེད་པ་དེ་རྣམས་འཁོད་པ་ཐམས་ཅད་ལ་ཕྱིས་གནོན་བྱས་ཤིང་འདུག་པའམ། [^2618]སྐྱབས་ཡོད་པ་ན་འགྲེང་བའི་ལྟུང་བྱེད་རེ་རེར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3805]
དེ་ལྟར་ཁྱིམ་བདག་རྣམས་ཀྱང་ལྷན་ཅིག་གནས་པ་ཡིན་ལ༌[^2619]ཞེས་བྱ་བ་ནི་ཁྱིམ་གཅིག་ཏུ་གྱུར་པ་ཉིད་བསྟན་ཏོ། །

[Block 3806]
ཕྱིས་གནོན་མ་བྱས་ཤིང་འདུག་པར་གྱུར་པ༌[^2620]ཞེས་བྱ་བ་འདི་ལ་ཕྱིས་གནོན་མ་བྱས་ཤིང་འདུག་པར་ཡང་འགྱུར་ཏེ། འདིའི་མཚན་མ་ཅན་ཁ་ན་མ་ཐོ་བ་གཉིས་ལ་འདིའི་མཚན་མ་ཙམ་ཉིད་ཀྱིས་སོ་སོར་ཉེ་བར་གནས་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3807]
ཐམས་ཅད་ལ་ཕྱིས་གནོན་མ་བྱས་ཤིང་འདུག་ལ་ཞེས་བྱ་བ་འདི་ལ་ཐམས་ཅད་ཕྱིས་གནོན་མ་བྱས་པར་འདུག་པར་ཡང་འགྱུར་ཏེ། སོ་སོར་ཉེ་བར་འདུག་པའི་མཚན་མ་འདི་གཉིས་ནི་གནས་ཀྱིས་ཞེས་བྱ་བའོ། །

[Block 3808]
གྲོང་ལ་དེ་ཡོད་པ་ནི་གཙུག་ལག་ཁང་གི་ཉེན་ཀོར་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གྲོང་ལ་དེ༌[^2621]ཞེས་བྱ་བ་ནི་ཉེ་བར་སྤྱོད་པའོ། །

[Block 3809]
ཡོད་པ་ཞེས་བྱ་བ་ནི་བདོག་པ་སྟེ། གཙུག་ལག་ཁང་གི་ཉེན་ཀོར་ཉིད་མ་ཡིན་ནོ། །

[Block 3810]
གྲོང་གི་ཉེན་ཀོར་གྱི་དོན་གང་ཡིན་པ་དེ་ནི་གཙུག་ལག་ཁང་གི་ཉེན་ཀོར་ཉིད་མ་ཡིན་ནོ། །

[Block 3811]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་གྲོང་དང་གཙུག་ལག་ཁང་གི་ཉེན་ཀོར་འབྲེལ་བར༌[^2622]གྱུར་ན་ཆོས་གོས་དང་མི་འབྲལ་བར་ཇི་ལྟར་འཚལ་བར་བགྱི། ཉེ་བ་འཁོར་གྲོང་གི་ཉེན་ཀོར་མ་གཏོགས་པ་ལྷག་མ་ལས་ཆོས༌[^2623]དང་མི་འབྲལ་བར་ཤེས་པར་བྱ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3812]
འདིར་མཚམས་ལ་ཇི་ལྟར་མི་ལྡང་བ་དང་བྱིན་གྱིས་བརླབས་པ་དོན་དུ་གཉེར་བ་ལ༌[^2624]ཤེས་པར་བྱ་བ་གནས་པ་ཉིད་ཀྱིས་སོ་སོར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་དེ་བཞིན་དུ་འདི་ལ་གང་ཞིག་གཙུག་ལག་ཁང་ལ་ཅུང་ཟད་ལྷག་པར་གནས་པའི་དགེ་སློང༌[^2625]ཁྱིམ་ན་གནས་པས་གནས་ཁང་དུ་ལྷག་པར་གནས་ན་སོ་སོར་གནས་པ་ཉིད་དེ་ལ་ཞེས་བྱ་བ་འདི་ཡང་འདིས་བྱས་པར་རིག་པར་བྱའོ། །

[Block 3813]
དེ་བས་ན་གནས་ཁང་དང་འབྲེལ་བའི་རྣམ་པར་གཞག་པས་འདི་ཐོབ་པར་རིག་པར་བྱའོ། །

[Block 3814]
གང་ཞིག་འགྲོ་བ་པོས་མཚན་མོ་གཅིག་ལ་ཡང་མཚམས་ཀྱི་ས་ཕྱོགས་འབའ་ཞིག་ན་ལྷག་པར་གནས་པ་དེ་ལ་དེའི་སོ་སོར་གནས་པ་ཉིད་ཅེས་བྱའོ། །

[Block 3815]
འབྲལ་བའི་སྤང་བ་ཞུ་བའི་སྐབས་སོ།། །།

[Block 3816]
ཁ་བསྐང་བ་ལ་རེ་བ་མེད་ན་ཆུང་བ་ཁྲུ་གང་ཡན་ཆད་ཀྱང་ཆོག་པ་དང་འདྲའོ་ཞེས་བྱ་བ༌[^2626]ནི་འཁོར་གསུམ་ཁེབས་པའི་མཐའི་ཚད་བཞིན་དུ་འཛིན་པ་དང་། བསླབ་པའི་གཞི་ལས་འདི་ཞུགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3817]
མེད་ན་ཞེས་བྱ་བ་ནི་གནས་མ༌[^2627]ཟིན་པ་ལ་འདིར༌[^2628]ཇི་ལྟར་རྣམ་པ་གང་གིས་ཀྱང་བསྒྲུབ་པ་ཡིན་ཏེ། ཕྱིར༌[^2629]འོང་བ་ལ་སྡོད་པ་ནི་རེ་བ་དང་བཅས་པར་རིག་པར་བྱའོ། །

[Block 3818]
འདིར༌[^2630]ཆད་ནི་རེ་བ་ཀུན་ནས་ཆད་པའོ། །

[Block 3819]
འདིར་གཞུང་ནི་དེ་ཆོས་གོས་ལ་རེ་བ་གང་ཡིན་པ་དེ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་རྒྱུན་ཆད་པར་གྱུར་ན་དགེ་སློང་དེས༌[^2631]གོས་དེ་ཉི་མ་བཅུ་པ་དེ་ཉིད་ཀྱི་ནང་རོལ་དུ་གཏང་བར༌[^2632]བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཆོག་པ་ཞེས་བྱ་བ་གང་ཞིག༌[^2633]དེར་ཁ་བསྐང་བར་གསུངས་པ་འཁོར་གསུམ་ཁེབས་པའི་མཐའི་ཚད་དུ་འདི་ཆོག་པར་སྔ་མ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་ཁྲུ་གང་ཡན་ཆད༌[^2634]ཁ་བསྐང་བ་པོ་ལ་རེ་བ་མེད་པར་གྱུར་ན་ཁྲུ་གང་ཡན་ཆད་དུ་ཆོག་པ་དེ་ཞག་བཅུའི་མཐར་ཐུག་པར་བཙང་བར་བྱའོ། །

[Block 3820]
ཡོད་ན་ནི་ཁྲུ་གང་ཡན་ཆད་ཉེ་བར་བསྐུལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་རྣམ་པར་གཞག་པ་འདིའོ། །
--- END BLOCKS ---
