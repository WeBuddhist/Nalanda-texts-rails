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
[Block 4691]
བསྙེན་པར་མ༌[^3286]རྫོགས་པ་རྣམས་ཀྱི་དགེ་འདུན་ལྷག་མའི་སྐབས་མ་གཏོགས་པ་སྔ་མ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་དབྱུང་བ་མ་གཏོགས་པ་གང་ཞིག་སྔོན་དུ་ཀུན་དགའ་ར་བ་འབུལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་དེ་ཐམས་ཅད་བསྙེན་པར་མ་རྫོགས་པ་རྣམས་ལ་ཡང་རྟོགས་པར་བྱའོ། །

[Block 4692]
ཁྱིམ་པ་དང་ཁྱིམ་པ་མོའི་བཟོད་པ་གསོལ་བ་ནི་ཁ་བསྲང་བའོ་ཞེས་བྱ་བ་ནི་བཟོད་པར་གསོལ་བའི་གནས་ལ་ཁྱིམ་པ་ཕོ་མོའི་ལྷུང་བཟེད་ཁ་ཕུབ་པ༌[^3287]དག་ལ༌[^3288]ཁ༌[^3289]བསྲང་བར་གསོལ་བ་ཡིན་པར་བལྟའོ། །

[Block 4693]
ཟས་དང་སྨན་དང་གཡོག་དག་མེད་ལ་དེ་དག་མེད་པར་འཚོ་མི་ནུས་ན་དེ་ལས་འདའ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དབྱར་གནས་པར་ཁས་བླངས་བ་དེའོ། །

[Block 4694]
ཟས་ལ་སོགས་པ་རྣམས་མེད་ལ་དེ་དག་མེད་པར་འཚོ་མ༌[^3290]ནུས་པར་གྱུར་ན་དེ་ལས་འདའ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་ལྟར་ཟས་མེད་པར་འཚོ་བར་མི་ནུས་ཤེ༌[^3291]ན། གང་གི་ཕྱིར་འདིར་ཡང་བྱེ་བྲག་ཏུ་འདི་རྟེན༌[^3292]ནི་བྱེ་བྲག་ཏུ་འདི་ལ་བརྟེན་པ་ཡོད་པ་སྟེ། ཐམས་ཅད་དུ་མེད་པ་ཁོ་ན་མ་ཡིན་ཏེ། དེ་ལ་མཆོག་མེད་པ་ལ་རྩ་བ་དང་འབྲས་བུ་ལ་སོགས་པ་གཞན་གྱིས་སུ་ཞིག་ལ་ནུས་པ་ཡོད་སྙམ་དུ་སེམས་པ་དེ་བས་ན་འདི་བྱེ་བྲག་ཏུ་བྱས་སོ། །

[Block 4695]
དགེ་སྦྱོང་གི་ཚུལ་དང་སྲོག་དང་ཚངས་པར་སྤྱོད་པའི་བར་ཆད་ཡོད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ལ།[^3293] དེ་ལས་འདའ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ།[^3294] །བུད་མེད་དང་སྐྱེས་པ་དང་མ་ནིང་གི་མཚན་མ་རྣམས་སམ། དེར་གཉེན་འདུན་རྣམས་ཀྱི་བར་ཆད་ཡོད་ན་ཞེས་བྱ་བ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 4696]
དགེ་འདུན་དབྱེ་བའི་ཕྱིར་བརྟུལ་བ་རྗེས་སུ་མི་མཐུན་པའི་སེམས་བསྐྱེད་པ་དང་སྡིག་པ་ཅན་གྱི་ཚིག་བརྗོད་པ་དག་འབྱུང་ནའོ་ཞེས་བྱ་བ་ནི་དབྱེ་བའི་ཕྱིར་རྗེས་སུ་མི་མཐུན་པར་གྱུར་པ་གཉིས་པོ་དེ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་སྨོས་པར་རིག་པར་བྱ་བ་སྟེ། གང་ཞིག་གཞན་འདུལ་བའི་ཕྱིར་སྐྲོད་པ་དེ་ནི་མ་ཡིན་ནོ། །

[Block 4697]
དོན་ནི་འདི་ཡིན་ཏེ། དགེ་འདུན་དབྱེ་བའི་ཕྱིར་བརྟུལ་བ་དག་ཡོད་ལ་གང་ཞིག་རྗེས་སུ་མི་མཐུན་པ་ཚུལ་བཞིན༌[^3295]མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་དང་། མཚུངས་པར་ལྡན་པའི་སེམས་སྟོན་པར༌[^3296]བྱེད་པ། ཨེ་མ་དགེ་འདུན་དབྱེ་བར༌[^3297]བྱའོ་སྙམ་པ་གང་ཡིན་པ་དང་། གང་ཡང་དེ་དང་འབྲལ་བ༌[^3298]དེ་ལྟ་བུ་སྡིག་པ་ཅན་གྱི་ཚིག་བརྗོད་པ་དེ་དག་ལ་འབྱུང་བར་འགྱུར་ན་དབྱར་ཁས་བླངས་པ༌[^3299]ལས་འདའ་བར་བྱ་སྟེ། དེ་རལ་པའི་ལྟུང་བར་མི་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4698]
དེ་ཞི་བར་བྱ་བའི་ཕྱིར་མཐུ་ཡོད་པ་ལྟ༌[^3300]ན་མི་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་དབྱེ་བའི་ཕྱིར་བརྟུལ་བ་དག་ཡོད་ལ་དེ༌[^3301]ཞི་བར་བྱ་བའི་ཕྱིར་གང་ལ་དེ་ནུས་པའི་མཐུ་ཡོད་པ་དེ་ནི་མཐུ་དང་བཅས་པའོ། །

[Block 4699]
སོང་ན་མི་འདའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབས་པའི༌[^3302]དུས་ལས་ཞེས་བྱ་བའི་ཚིག་གི་ལྷག་མའོ། །

[Block 4700]
གལ་ཏེ་དེར་སོང་ནས་ཞག་བདུན་ལས་འདས་སུ་ཟིན་ཀྱང་བྱ་བ་དེ་ཉིད་ཀྱིས་དགེ་སློང་གི་དབྱར་རལ་བའི་ལྟུང་བར་མི་འགྱུར་རོ་ཞེས་གསུངས་པས། ངེས་པར་འདའ་བར༌[^3303]བྱའོ་ཞེས་པ་འདིར་དེ་ལ་གཞོལ་བར་བསྟན་པའི་ཕྱིར༌[^3304]མདོར་བྱས་པའོ། །

[Block 4701]
དམ་བཅས་ན་དབྱར་གནས་པ་དང་གནས་སུ་མི་འབྲེལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་འདིར་དབྱར༌[^3305]གནས་པར་བྱ་བའོ་ཞེས་དབྱར༌[^3306]གནས་པར་སོ་སོར་ཐོས་ན་དབྱར་གནས་པའི་དོན་དུ་དབྱར་གྱི་གནས་སུ་འབྲེལ་བར་བྱ་བའི་དོན་དུ་གདོན་མི་ཟ་བར་བྱས་ཏེ་མི་བྱེད་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4702]
གསོ་སྦྱོང་གཅིག་པ་ཉིད་ཀྱིས༌[^3307]གནས་གཉིས་སུ་དེ་འབྱུང་བ་མེད་དོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་སླར་བསྙེན༌[^3308]ནས་དབྱར་གནས་པ་དང་གནས་སུ་འབྲེལ་བར་མི་བྱེད་པའི་ཉེས་པ་ལའོ། །

[Block 4703]
འདི་སྐད་བསྟན་ཏེ། གསོ་སྦྱོང་གཅིག་པའི་གནས་གཉིས་ལ་གཅིག་ཏུ་དབྱར་གནས་པར་དམ༌[^3309]བཅས་ནས། གཞན་དུ་དབྱར་གནས་པར་ཁས་ལེན་པར་བྱེད་དུ་ཟིན་ཀྱང་དེ་ལ་ཉེས་པ་མེད་དེ། གང་གི་ཕྱིར་གསོ་སྦྱོང་གཅིག་ཡིན་པས་ཐ་དད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4704]
གནས་གཞན་དུ་སོང་བ་ལའོ། །

[Block 4705]
དེར་མ་ཚང་བར་བྱས་པའི་གནས་ཁང་དུ་མ་བཟུང་བ་དང་འདྲ་བར་མ་འབྲེལ་བ༌[^3310]འདི་ལ་མི་གནས་པར་གྱུར་པ་ནི་མ་ཡིན་ནོ། །

[Block 4706]
དེ་ལ་གནས་གཅིག་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར། གནས་དེ་དག་ལ་དེ་བས་ན་ཉེས་པ་མི་སྐྱེད༌[^3311]པའོ། །

[Block 4707]
རྙེད་པར༌[^3312]གཅིག་པ་ཉིད་ལ་ནི་ཡོད་དོ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་ཐ་དད་པ་ཉིད་ལ་རྙེད་པ་ནི་གཅིག་པ་ཉིད་ཡིན་ན་གནས་དག་ལ་ཐ་དད་པར་ཉལ་བ་འདི་ལ་བསྐྱེད་པ་ཡོད་པ་ཉིད་དོ། །

[Block 4708]
གནས་པའི་ལོངས་སྤྱོད་ཐ་དད་པས་གནས་ཀྱི་བྱེད་པ་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 4709]
དོན་ལེན་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4710]
རྙེད་པ་ཞེས་སྨོས་པས་ཡོན་བདག་གམ་རྙེད་པའི་ཚད་ལས་ཐ་དད་པའི་ཕྱིར་རོ།[^3313] །འདིར་གཞུང་ནི་འདི་ལྟར། དགེ་སློང་གིས་གནས་འདིར་དབྱར་སྔ་མ་ཟླ་བ་གསུམ་གནས་པར་བྱའོ་ཞེས་དམ་བཅས་ནས་གནས་དེ་གཉིས་རྙེད་པ་ནི། གཅིག་ལ་གསོ་སྦྱོང་ནི་ཐ་དད་པར་གྱུར་ནས་དེ་འདི་སྙམ་དུ་འདིར་གནས་ན་ཡང་རྙེད་པ་གཅིག་ཏུ་ཟད་ལ། ཕ་གིར་གནས་ན་ཡང་རྙེད་པ་གཅིག་ཏུ་ཟད་དོ་སྙམ་ནས་དེ་དམ་བཅས་ནས་མི་འགྲོ་ཞིང་དགེ་སློང་དེ་ལ་དེར་དབྱར་སྔ་མ་ཟླ་བ་གསུམ་ཡང་མི་སྣང་ཕྱི་མ་ཡང་མི་སྣང་ལ་དམ་ནི་བཅས་ནས་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4711]
གཞིར་གཏོགས་པའི་དབྱར་གྱི་གཞིའོ།། །།

[Block 4712]
སྡེ་པ་ལྔ་ཆར་གྱིས་ཀྱང་གནས་པར་ཁས་བླང་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དང་དགེ་སློང་མ་འབའ་ཞིག་གིས་གནས་པར་ཁས་བླང་བར་བྱ་བ་ཉིད་དུ་མ་ཟད་ཀྱི། འདི་ལྟར་དགེ་སློང་མ་དང་དགེ་ཚུལ་མ་དག་གིས་ཀྱང་གནས་པར་ཁས་བླང་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4713]
དགེ་ཚུལ་འབའ་ཞིག་གིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཁས་བླང་བར་བྱ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4714]
ལོ་མ་ཚང་བ་དག་གིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་འབའ་ཞིག་གནས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 4715]
དེ་དག་ལས་ཁས༌[^3314]བླང་བ་མི་འཆགས་པ༌[^3315]ཉིད་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་དག་ལ་ཞེས་བྱ་བ་ནི་དབྱར་གནས་པར་བྱ་བ་མ་ཡིན་པ་དང་། སྔ་མ་དེ་རྣམས་འབའ་ཞིག་ཁས་ལེན་པ་ལའོ། །

[Block 4716]
གནས་མལ་མི་མནོད་པར༌[^3316]བྱ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་གནས་པར་ཁས་བླངས་པ་རྣམས་ལའོ། །

[Block 4717]
སྟོབས་པ་མེད་པས་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ༌[^3317]གནས་མལ་སྟོབས་པ་མེད་པས་ན་གནས་མལ་མི་མནོད་པ་མ་ཡིན་ཏེ། མནོད་པར་བྱ་བ་ཁོ་ན་ཡིན་པའོ།[^3318] །མ་བསྐོས་པར་བསྟབ་པར༌[^3319]མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་མལ་སྟོབས་པར་མ་བསྐོས་པའི་གང་ཟག་གིས་བསྙེན་པར་རྫོགས་པ་དང་། བསྙེན་པར་མ་རྫོགས་ཤིང་རབ་ཏུ་བྱུང་བ་སུ༌[^3320]ཡང་བཟུང་བ༌[^3321]དང་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བའི༌[^3322]དོན་ཏོ། །

[Block 4718]
འགྱོད་པ་ལ་སོགས་པས་སྡེ་སྣོད་འཛིན་པ་དང་། འཐབ་ཀྲོལ་བྱེད་པ་ཡོད་པ་དང་མེད་པ་དག་མ་བསྡུས་པ་ན་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མི་སྐྱེད་པ༌[^3323]ཉིད་དང་སེལ་བ་ཉིད་དག་ལ་འགྱོད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་མདོ་དེས་སྡེ་སྣོད་འཛིན་པ་ཡོད་པ་དང་། འཐབ་ཀྲོལ་བྱེད་པ་མེད་པ་འདི་གཉིས་ཀྱང་མ་བསྡུས་པ་ཉིད་མ༌[^3324]ཡིན་པའོ། །ཇི་ལྟར་བསྡུས་ཤེ་ན། འདི་ལྟར་འགྱོད་པ་བསལ་བའི་སྒྲས་ནི་དེ་ལ་སྡེ་སྣོད་འཛིན་པ་ཙམ་བསྡུས་པ་ཡིན་ནོ། །

[Block 4719]
འགྱོད་པ་དང་དེ་ལས་གཞན་པའི་སྡུག་བསྔལ་དང་ཡིད་མི་བདེ་བ་མི་སྐྱེད་པ༌[^3325]ཉིད་ཅེས་སྨོས་པས་ནི་འཐབ་ཀྲོལ་བྱེད་པ་མེད་པ་འདི་གཉིས་ཀྱང་མ་བསྡུས་པ་མ༌[^3326]ཡིན་ནོ། །

[Block 4720]
གནས་པར༌[^3327]ཁས་མ་བླངས་པས་གནས་མི་གཏོང་ན་གནས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ཁ་ཅིག་ལས་ནི། དགེ་སློང་དབྱར་གནས་པར་ཁས་མི་ལེན་པ་དག་ལ་དབྱར་རལ་བར་བརྗོད་པར་བགྱིའམ། གལ་ཏེ་དབྱར་གྱི་ནང་དུ་གནས་མི་གཏོང་ན་དབྱར་རལ་བར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 4721]
འདིས་ནི་གནས་པར་ཁས་མ་བླངས་སུ་ཟིན་ཀྱང་དབྱར་གྱི་ནང་དུ་གནས་མི་གཏོང་ན་ཕྱི་རོལ་དུ་འགྲོ་བའི་ཕྱིར་བྱིན་གྱིས་བརླབ་པར་བྱ་དགོས་སོ་ཞེས་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 4722]
ནམ་མཁའ་ལ་གནས་པར་ཁས་བླངས་པ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་གནས་འདིར་དེ་ལྟ་བས་ན་རྟེན༌[^3328]འདི་ལ་འདིར་བླང་བའོ། །

[Block 4723]
གྲུ་ལ་ནང་དུ་འབྱམ་པ༌[^3329]ཉིད་དུ་ཤེས་ན་མི་འཆགས་སོ། །

[Block 4724]
ས་ལ་ཕྱིན་པ་དང་། ས་ལ་གནས་པ༌[^3330]བརྟན་པོ་དང་འབྲེལ་པ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་གྲུ་ས་ལ་ཕྱིན་པར་གྱུར་ནས་ས་ལ་གནས་པ་བརྟན་པོ་དང་འབྲེལ་བར་གྱུར་ན་ཉེ་བར་འགྲོ་བ་པོས་ཤེས་པར་མ་གྱུར་ལ། དེ་དབྱར་གྱི་ནང་དུ་འབྱམ་པར་གྱུར་པ་ཉིད་དུ་མི་ཤེས་ན་དེ་ལྟར་ན་དབྱར་གནས་པར་ཁས་བླངས་པ་འཆགས་ཀྱི༌[^3331]གཞན་དུ་ནི་མི་འཆགས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4725]
དེ་ལྟར་ལོ་ཉི་ཤུ་མ་ལོན་པ་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དེ་མི་ཤེས༌[^3332]ལ་མ་ལོན་པར་གྲགས། དེ་ལྟར་མ་ལོན་པའི་ཆོས་ཅན་ཉིད་དུ་མི་ཤེས་པ་ལ་ནི་ཁས་ལེན་པ་ལ་རིག་པར་བྱའོ། །

[Block 4726]
འདིར་གཞུང་ནི་དགེ་སློང་དག་གྲུར་དབྱར་གནས་པར་ཁས་ལེན་པར་བགྱིད༌[^3333]ན། དབྱར་རལ་བར་བརྗོད་པར་བགྱིའམ། རལ་བར་བརྗོད་པར་མི་བགྱི། བཀའ་སྩལ་པ། གལ་ཏེ་བརྗོད་ཀྱི་ནང་དུ་འབྱམ་པར་འགྱུར་བ་ཉིད་དུ་ཤེས་ན་དབྱར་རལ་བར་བརྗོད་པར་བྱའོ། །

[Block 4727]
འོན་ཏེ་མི་ཤེས་ན་ནི་དབྱར་རལ་བར་བརྗོད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་དང་།

[Block 4728]
ཁ་ཅིག་ལས།

[Block 4729]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གྲུར་དབྱར་གནས་པར་ཁས་ལེན་ན་དབྱར་གནས་པར་ཁས་བླངས་ཞེས་བགྱིའམ། གལ་ཏེ་ས་ལ་བརྟེན༌[^3334]ཅིང་གནས་པ་ཡིན་ན་དབྱར་གནས་པར་ཁས་བླངས་ཞེས་བྱའོ། །

[Block 4730]
བཙུན་པ་ཕུར་པའམ་ཞུགས་ཤིང་དང་འབྲེལ་པ་ལགས་ན་དབྱར་གནས་པར་ཁས་བླངས་ཞེས་བགྱིའམ། ཉེ་བ༌[^3335]འཁོར་གནས་པར་ཁས་བླངས་ཞེས་བྱའོ་ཞེས༌[^3336]གསུངས་པ་ཡིན་ཏེ། དེ་གཉིས་ཀ་བསྡུས་ནས་དེ་སྨོས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
