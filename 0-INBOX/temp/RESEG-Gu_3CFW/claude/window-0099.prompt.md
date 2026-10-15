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
[Block 3466]
གཙུག་ལག་ཁང་དུ་གནས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བྱའོ་ཞེས་བྱ་བ་དང་མནོད་པར༌[^3536]བྱའོ་ཞེས་བྱ་བ༌[^3537]དེ་གཉིས་ཀྱིས་གནས་པར་བྱ་བ་མ་བསྡུས་ཏེ། དེ་གཉིས་ཀྱིས་གཞན་གྱི་དོན་དུ་བྱ་བ་དང་། མནོད་པར་བྱ་བ་ཡང་སྲིད་པས་རྩོམ་པ་འདིའོ། །

[Block 3467]
གཞན་དག་དགེ་འདུན་གྱི་གཞིར༌[^3538]དགེ་འདུན་གྱི་ཕྱིར་རམ་གང་ཟག་དགེ་སློང་གི་ཕྱིར་གནས་ཀྱི་གཞི་བྱེད་པ་རྗེས་སུ་གནང་བར་བྱའོ། །

[Block 3468]
གལ་ཏེ་སྦྱིན་བདག་ཡོད་ན་དེས་རྗེས་སུ་གནང་བ་ནའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དགེ་འདུན་གྱི་གཞི་དེ་ལ་སྦྱིན་བདག་ཡོད་ན་དེས་རྗེས་སུ་གནང་ན་དགེ་འདུན་གྱི་ཕྱིར་རམ་གང་ཟག་གི་ཕྱིར། གནས་ཀྱི་གཞི་བྱེད་པ་རྗེས་སུ་གནང་བར་བྱའོ། །

[Block 3469]
གྲོང་ཁྱེར་གྱི་ཕྱི་རོལ་ལམ་ནང་དུ་བསྟི་བའི་གནས་དག་རུང་ངོ་ཞེས་བྱ་བ་ནི་གང་དུ་དགེ་སློང་དག་བསོད་སྙོམས་པའི་དོན་དུ་འཇུག་པ་རྣམས་ཀྱི་ཚ་བ་དང་། ངལ་བ་རྣམས་ལ་སོགས་པ་བསལ་བའི་ཕྱིར་བསྟི་བའི་གནས་མི་འོང་བའི་གནས་ཞེས་བྱ་བ་དེ་བྱེད་དུ་གཞུག་པར་རུང་ངོ་། །འདིར་གཞུང་ནི་གལ་ཏེ་བཅོམ་ལྡན་འདས་ཀྱིས་རྗེས་སུ་གནང་ན་བདག་གྲོང་ཁྱེར་གྱི་སླད་རོལ་དུ་བསྟི་བའི་གནས་བགྱིད་དུ་སྩལ་ཏེ་ཞེས་བྱ་བ་ནས། ཁྱིམ་བདག་རྗེས་སུ་གནང་གིས་རྩིགས༌[^3539]ཤིག་ཅེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3470]
འདིར་གྲོང་ཁྱེར་གྱི་ཕྱི༌[^3540]རོལ་དུ་ཞེས་གསུངས་པ་ནི། བྱུང་བའི་དབང་གིས་སྨོས་པ་ཡིན་གྱི།[^3541] གྲོང་ཁྱེར་གྱི་ནང་དུ་ཡང་འགལ་བ་མེད་པས་འདིར་གཉིས་ཀ་མདོར་བསྡུས་སོ། །

[Block 3471]
རང་གི་ཁྲོན་པ་བར་དུ་བཅད་པའི་ཕྱིར་རྩིག་གུ་བྱས་པས་ཀུན་དུ་ཆགས་པའི་ཤེས་པ་བསལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བར་དུ་བཅད་པའི་ཕྱིར་རྩིག་གུ་བྱ་བ་གང་ཡིན་པ་དེ་བྱེད་པས་བུད་མེད་ཀྱི་ཚོགས་ལ་བལྟ་བར་བྱ་བ་གསལ་བར་བྱ་སྟེ། ཁྲོན་པ་གཞན་ལ་ཆོ་ག་འདི་བྱེད་པ་མ་ཡིན་ཏེ་དེ་བས་ན་རང་གི་ཁྲོན་པའི་ཚིག་གོ། །

[Block 3472]
དེར་བུད་མེད་ཆུ་ཆུར་འོངས་པ་མཐོང་བ་ན་ཀུན་དུ་ཆགས་པའི་རྐྱེན་ཡིན་ཏེ། རྩིག་པས་བར་དུ་ཆོད་པ་མེད་པ་ཉིད་ལ་ནི་མཐོང་བ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་ཆགས་པ་སྐྱེ་བའི་རྐྱེན་དུ༌[^3542]མི་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་དེའི་དེ་ཉིད་མེད་པ་ཉིད་དོ། །

[Block 3473]
སྙིམ་པ་བཀང་ཞིང༌[^3543]བླུད་པས་བུད་མེད༌[^3544]རྗེས་སུ་གཟུང་བར༌[^3545]བྱ་ཞིང་ཆུ་རྒྱུན་མ་ཆད་པས་བླུགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བུད་མེད་ཀྱིས་ཆུ་སྙིམ་པ་གང་འཐུངས་ཟིན་ནས་སྙིམ་པ༌[^3546]

[Block 3474]
གཉིས་པ་དགང་ཞིང་བླུད་པར་བྱའི། སྙིམ་པ་ནས་འཐུང་བཞིན་དུ་ཆུའི་རྒྱུན་ཕྱི་མ་ཡང་རྒྱུན་མི་འཆད་པར༌[^3547]བླུགས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3475]
བུད་མེད་གང་ཞིག་དགེ་སློང་གི་མདུན་དུ་སེམས་རབ་ཏུ་གཏད་པ་དེ་ལ་རང་གིས་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ། འདིར་ཁ་ཅིག་བྱེད་པ་དེ་ནི་གཞན་གྱི་སེམས་ཤེས་པར་དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་ཏེ། ཤིན་ཏུ་བྲེལ་བའི༌[^3548]ངོ་བོ་མ་ཡིན་ནོ། །

[Block 3476]
བར་བར་དུ་ཡང་ཆུའི་རྒྱུན་གཅད་པར༌[^3549]བྱའོ་ཞེས་བྱ་བ་ལ། གཞན་དེ་རྣམས་ཆུ་སྟེར་བ་ལ་རྣམ་པར་རྟོག་པ་བྱེད་པ་དེ་ལ་ཡང་ཐོ༌[^3550]འཚམ་པ་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་མི་རིགས་པ་ཉིད་དོ། །

[Block 3477]
དེའི་དུས་ཉིད་ཀྱི༌[^3551]དབྱར་གྱི་ནང་དུ་འོངས་པ་ནི་རྙེད་པ་དབང་ངོ་ཞེས་བྱ་བ་ནི་འདིར༌[^3552]རྙེད་པ་ལ་དེའི་སྒྲ་ལ་ལྟོས་པ་ཉིད་དེ་དུས་གང་ལ་ཡོད་པ་ཞེས་བྱ་བ་དེ་བསྡུས་པའོ། །

[Block 3478]
འདིར་དབྱར་གྱི་རྙེད་པས་དབྱར་གྱི་ནང་དུ་འོངས་ཤིང་ཞེས་བྱ་བ་འདི་ལས་ཤེས་པའོ། །

[Block 3479]
དབྱར་གྱི་དུས་ལ་ཤིན་ཏུ་མང་བ་ཉིད་ནི་དེའི་རྙེད་པའི་དུས་སོ། །

[Block 3480]
གལ་ཏེ་དབྱར་གྱི་ནང་དུ་འོངས་པ་ལ་ཤིན་ཏུ་མང་བར་དབྱར་གནས་ལ་དེར་གནས་པ་གྲུབ་པར་འགྱུར་ན་དེ་འོས་པ་ཡིན་ནོ། །

[Block 3481]
དབྱར་རལ་བ་ལ་ཡང་དབྱར་གྱི་རྙེད་པའི་སྐལ་བ་དབང་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3482]
འདིར་རྙེད་པ་དབང་བའི་རྒྱུ་ནི་གནས་པ་ཡིན་ཏེ། གནས་པར་ཁས་བླངས་པ་ནི་མ་ཡིན་ཏེ། ཇི་ལྟར་ཡང་དེ་ལྟར་ཁས་བླངས་ཀྱང་ཞེས་བྱ་བ་དེ་ལྟར་རྣམ་པར་གཞག་པ་འདིའོ། །

[Block 3483]
ཟ་ཞིང་རྙེད་པ་མ་ཡིན་པ༌[^3553]ལ་ནི་ལས་མི་རིགས་སོ་ཞེས་བྱ་བ་ནི་ཟས་ཙམ་གྱིས་འཚོ་ཞིང་རྙེད་པ་མ་ཡིན་པ༌[^3554]ལ་ནི་དེ་ལ་སུས་ཀྱང་བསྐོ་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3484]
འདིར་གཞུང་ནི༌[^3555]ཁ་ཅིག་ལས་དབྱར་གྱི་ནང་དུ་འོངས་པ་དག་གི་དབང་དུ་བྱས་ཏེ་གསུངས་པ་ཡིན་ནོ། །

[Block 3485]
འདིར་གཞུང་ནི་དགེ་སློང་དག་གི༌[^3556]རྙེད་པ་མ་ཐོབ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གལ་ཏེ་ལས་སུ་བསྐོས་པ་བྱེད་ན་ནི་རྙེད་པ་ཡང་སྦྱིན་པར་བྱའོ། །

[Block 3486]
ཇི་སྟེ༌[^3557]མི་བྱེད་ན་ནི་ཟན་ལ་བལྟས་པ༌[^3558]ཙམ་གྱིས་གནས་པར་བྱ་སྟེ་ལས་དང་རྙེད་པ་ཡང་ངོ་ཞེས་གསུངས་པ་འདི་ལ་རིགས་པས་བྱེ་བྲག་ཉེ་བར་བསྡུས་ནས་མདོ་འདི་གཉིས༌[^3559]ཀྱིས་འདི་བསྡུས་སོ། །

[Block 3487]
གཞུང་གཞན་ལས་ཀྱང་དགེ་སློང་དག་ཟས་ཀྱི་རྙེད་པ་དེ་ཡང་མི་ནོད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་དག་ལ་ཟས་ཀྱི་རྙེད་པ་དེ་དག་སྦྱིན་པར་བྱའོ་ཞེས་གསུངས་པ་དེ་དག་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 3488]
ལས་སུ་ནི་གཞོན་རིམས་ནས་མཐར་གྱིས་བསྐོའོ་ཞེས་བྱ་བ་ནི་གཞོན་རིམས་ནས་མཐར་གྱིས་བྱའོ། །

[Block 3489]
རྙེད་པ་མི་འཐོབ་པ་ལ་ཟས་སྦྱིན་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་ལ་དབྱར་རམ་དུས་གཞན་ལ་དབྱར་གྱི་དུས་བཞིན་དུ་ངེས་པ་ཉིད་ཀྱི་ཕྱིར། །བྱ་བས་རྙེད་པ་མི་འཐོབ་པ་དེ་ལ་ཟས་ནི་སྦྱིན་པར་བྱ་བ་ཉིད་ཡིན་པའོ། །

[Block 3490]
གཞན་གྱི་རྙེད་པ་ལ་འདུ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དེའི་ཚེ་མ་སྦྱིན་པར་ལེན་པ་སྐྱེད་པ༌[^3560]ནི་འདི་ལྟ་སྟེ། གནས་གཞན་མངོན་སུམ་དུ་རྙེད་པའི་ཕྱིར་ནང་དུ་གཏོགས་པའི་ཁྲོད་དུ་ཞུགས་ནས་ཟོས་ན་ཉེས་པར་འགྱུར་ལ། ཉེས་པ་མེད་པ་དེའི་དོན་ཁོ་ནར༌[^3561]དེར་སོང་བ་མ་ཡིན་པ་གཙུག་ལག༌[^3562]ཁང་གཞན་དུ་སོང་ནས་ཟོས་པ་ལའོ། །

[Block 3491]
གལ་ཏེ་ཟས་ཀྱི་དོན་ཁོ་ནར་དེར་སོང་བ་མ་ཡིན་པ་དེ་ལ་ནི་ཉེས་པ་མེད་པའོ། །

[Block 3492]
མུ་གེའི་ཚེ་རང་གིས་མ་ཁྱེར་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་མུ་གེའི་དུས་ཀྱི༌[^3563]ཚེ་རང་གིས་གཙུག་ལག་ཁང་ནས་བརྒྱགས༌[^3564]མ་ཁྱེར་བར་གཙུག་ལག་ཁང་གཞན་དུ་ཟན་ཟོས་ན་ཉེས་པ་མེད་པའོ། །

[Block 3493]
དགེ་སློང་གི་ཚད་ཉིད༌[^3565]ལས་ལྷག་མ༌[^3566]ཉིད་བླངས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་ན་གནས་ནས་དགེ་སློང་ཇི་སྙེད་པ༌[^3567]འཁོད་པའི་ཟས་ཀྱི་ཚོད་ལས་ལྷག་པའི་ཐོབ་པ་ཡོད་པ༌[^3568]ཉིད་ཡིན་ན་གཙུག་ལག་ཁང༌[^3569]ན་གནས་ནས་ཟས་བླངས་ན་ཉེས་པ་མེད་པའོ། །

[Block 3494]
གཙུག་ལག་ཁང་ཡལ་བར་མི་དོར་རོ་ཞེས་བྱ་བ་ནི་འདི་ནི་སིལ་བུ་དག་ལས་སོ། །

[Block 3495]
རང་གིས་ཞེས་བྱ་བ་དེ་ཡང་ངོ་། །སྦྱིན་པའི་བདག་པོ་ཞེས་བྱ་བ་དེ་ནི་འདིར་ཡང་ངོ་། །ཕྱིར་བཅོས་པའི་ཕྱིར་སྦྱིན་བདག་སྤྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་ཏུ་མ་སྨོས་པས་གནས་པའི་གཞི་ཉི་ཚེར་མ་ཟད་ཀྱི་དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་ཐམས་ཅད་ཀྱང་དགེ་འདུན་གྱི་ཡིན་གྱི་གཞན་གྱི་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིའི་འོག་ནས་སྟོན་པ་ལས་ཤེས་པར་བྱའོ། །

[Block 3496]
མ་གྲུབ་ན་དགེ་འདུན་གྱི་ལས་ཇི་ཙམ་གྱིས་ནུས་པ་ངེས་པར་སྦྱར་རོ་ཞེས་བྱ་བ་ནི་སྦྱིན་བདག་མ་གྲུབ་ན་ཕྱིར་བཅོས་པའི་ཕྱིར་དགེ་འདུན་གྱི་རྫས་ལས་ཇི་ཙམ་གྱིས་ཆོག་པར་ཕྱིར་བཅོས་པར་བྱའོ། །

[Block 3497]
རང་གིས་ཀྱང་ཕྱིར་བཅོས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ལག་གི་ལས་ཀྱི་ཚུལ་གྱིས་ཅི་ནུས་པས་ཀྱང་ངོ་། །རྙེད་པ་མནོད་པས་གཙུག་ལག་ཁང་གི་བྱི་དོར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ནས་གང་རྙེད་པ་ནོད་པ་དེས་ལས་དེ་བྱའོ།[^3570] །དད་པའི་རྙེད་པ་ནི་གཙུག་ལག་ཁང་ཉིད་ཀྱིས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དད་པའི་རྒྱུ་ལས་བྱུང་བའི་རྙེད་པ་གང་ཡིན་པ་སྦྱིན་བདག་དད་པས་དུས༌[^3571]ངེས་པ་མེད་པར་གང་ཟག་འགའ་ཞིག་ལ་འབུལ་བར་བྱེད་པ་དེ་ནི་གཙུག་ལག་ཁང་ཉིད་ལ་རྙེད་པ་མ་ཡིན་ནོ། །

[Block 3498]
གཙུག་ལག་ཁང་ནས་སྒོ་བཅད་དེ་འགྲོ་བར་བྱའོ། །

[Block 3499]
སྲུང༌[^3572]མ་ཡང་གཞག་སྟེའོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་གི་ཞེས་བྱ་བའི་ལྷག་མའོ། །

[Block 3500]
དེ་ལ་ཟན་མེད་ན་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་གི་སྲུང༌[^3573]མ་དེ་ལ་ཟན་མེད་ན་སྦྱིན་པར་བྱའོ། །

[Block 3501]
དེས་ཆོམ་རྐུན་པའི་རང་དབང་ཉིད་མེད་པར་མི་ཤེས་པར་སྒོ་དབྱེ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་གི་སྲུང༌[^3574]མ་དེས་གཞན་དག་གཙུག་ལག་ཁང་གི་སྒོ་ཕྱེ་ཤིག་ཅེས་ཟེར་ན། ཆོམ་རྐུན་པའི་རང་དབང་ཉིད་མེད་པ་ངེས་པར་མི་ཤེས་པར་སྒོ་དབྱེ་བར་མི་བྱའོ། །

[Block 3502]
འདིར་ངེས་པར་ཤེས་པར་བྱ་བའི་ཐབས་གང་ཞེ་ན། དེའི་ཕྱིར་ཁང་སྟེང་དུ་འཛེགས་ལ་བལྟ༌[^3575]སྟེ། ཁྱོད་རིམས་ཀྱིས༌[^3576]མ་བཏབ་བམ་ཞེས་བརྗོད་པ་ནི་འདིར་ཐབས་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱོད་རིམས་ཀྱིས༌[^3577]མ་བཏབ་བམ་ཞེས་བརྡ་སྐད་བརྗོད་པ་ནི་སྨྲར་གཞུག་པའོ། །

[Block 3503]
གནས་དང་མིང་དང་ཕ་མ་ལ་སོགས་པ་སོ་སོར་ཤེས་པར་བྱེད་དུ་གཞུག་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་བརྗོད་པ་ནི་ཐབས་ཡིན་ནོ། །

[Block 3504]
འདི་རྗོད་པར་བྱེད་དུ་གཞུག་པའོ། །

[Block 3505]
ཡིད་མ་ཆེས་ཤིང་འཇིགས་པ་དང་བཅས་པ་ཉིད་ལ་སྒོ་དབྱེ་བར་མི་བྱའོ། །
--- END BLOCKS ---
