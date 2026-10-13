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
[Block 386]
གང་གི་ཚེ་དེ་ལྟར་སྐྱེས་པ་བསྐྱེད་བྱ་མ་ཡིན་ལ་མ་སྐྱེས་པ་ཡང་བསྐྱེད་བྱ་མ་ཡིན་ཞིང་སྐྱེས་པ་དང་མ་སྐྱེས་པའི་སྐྱེ་བཞིན་པ་ཡང་བསྐྱེད་བྱ་མ་ཡིན་པས། དེའི་ཚེ་བསྐྱེད་བྱ་མེད་པས་འདི་དག་བསྐྱེད་པར་ག་ལ་འགྱུར་ཞེས་པ་དེ་ལྟར་འགྱུར་རོ། །

[Block 387]
གང་གི་ཚེ་བསྐྱེད་པ་ཞེས་བྱ་བ་དེ་ལ་མི་སྲིད་པ་དེའི་ཚེ་སྐྱེ་བ་མེད་དོ་ཞེས་བྱ་བ་གྲུབ་བོ། །

[Block 388]
འདིར་སྨྲས་པ། གལ་ཏེ་བསྐྱེད་བྱ་མི་སྲིད་ཀྱང་དེ་ལྟ་ན་ཡང་འབྲས་བུ་སྐྱེད་བྱེད་ཀྱི་རྒྱུ་རེ་ཞིག་ཡོད་ལ། བསྐྱེད་བྱ་མེད་ན་སྐྱེད་བྱེད་ཀྱང་མི་རུང་ངོ་ཞེས་བྱ་སྟེ། དེས་ན་བསྐྱེད་བྱ་ཡང་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན།[^332] སྨྲས་པ། གལ་ཏེ་སྐྱེད་བྱེད་ཀྱི་རྒྱུ་ཉིད་ཡོད་ན་བསྐྱེད་བྱ་ཡོད་པར་འགྱུར་ལ། ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པས།

[Block 389]
[^333]

[Block 390 [HEADING]]
### ཚིགས་བཅད་དྲུག་པ། ^1-6-0

[Block 391 [VERSE]]
འབྲས་བུ་ཡོད་ན་འབྲས་ལྡན་ལ། །
དེར་མེད་གྱུར་ན་རྒྱུ་མེད་མཚུངས། །
ཡོད་དང་མེད་པ་ན་ཡང་འགལ། །
དུས་གསུམ་དུ་ཡང་འཐད་མ་ཡིན། །

[Block 392]
འདིར་ཡོད་བཞིན་པའི་མཉམ་པའི་ས་བོན་དང་ལྕགས་སྲེག་གི༌[^334]གོང་བུ་ལ་སོགས་པ་ལ། མྱུ་གུའི་རྒྱུར་རྣམ་པར་མི་འཇོག་སྟེ། མི་རུང་བའི་ཕྱིར། ས་བོན་ལ་རྣམ་པར་འཇོག་སྟེ་མྱུ་གུ་ཞེས་བྱ་བའི་འབྲས་བུ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 393]
དེ་ནི་འདི་ལྟར་འབྲས་བུ་དང་འབྲེལ་པ་མེད་པའི་ཕྱིར་རྒྱུ་མ་ཡིན་ལ། ལྡན་པའི་སྒྲ་འདི་ནི་རྒྱུའི་རྗོད་བྱེད་དུ་འཆད་ན། གྱུར་ན་ཞེས་ཁ་བསྐང་ངོ་། །དེས་ན་འབྲས་བུ་ཡོད་ན་འབྲས་བུ་དང་ལྡན་པར་འགྱུར་རོ་ཞེས་བྱ་སྟེ། འབྲས་བུ་ཡོད་ན་རྒྱུར་འགྱུར་རོ་ཞེས་པའི་དོན་ཏོ། །

[Block 394]
གཞན་དུ༌[^335]གལ་ཏེ་འབྲས་ལྡན་གྱི་སྒྲས་ཁྱད་པར་དུ་བྱས་པར་མ་གྱུར་ན། དེའི་ཚེ་འདི་སུའི་ཁྱད་པར་ཡིན་པས༌[^336]གཟུང་བར་མ་གྱུར་པས་སུ་ཞིག་འབྲས་བུ་དང་ལྡན་ཞེས་བྱའོ། །

[Block 395]
དེ་ལས་ཀྱང་དོན་མ་ཚང་བར་འགྱུར་ཏེ། རྒྱུའི་རྗོད་བྱེད་ལ་འབྲས་ལྡན་གྱི་སྒྲའི་དོན་མ་ཚང་བར་འགྱུར་རོ། །

[Block 396]
ཡང་ན་འདི་ནི་རྒྱུ་མེད་མཚུངས། །ཞེས་བརྗོད་པའི་ཤུགས་ལས་དོན་གྱིས་ཐོབ་ན། དེ་ལྟ་ན་ཡང་འགྲོ་བ་པོ་མ་ཡིན་པ་མི་འགྲོའོ་ཞེས་པ་འདིའི་རྒྱུའི་སྒྲས་བརྗོད་པའི་ཤུགས་གང་ཞིག་ལས་དོན་གྱིས་ཐོབ་པར་རིགས་ཀྱི་གཞན༌[^337]མ་ཡིན་ལ། རྒྱུའི་སྒྲའི་རྣམ་གྲངས་ཉེ་བར་ལེན་པར་བརྗོད་ཀྱི་ཤུགས་ཀྱིས་ཐོབ་པར་མ་བཤད་དོ་ཞེས་བྱའོ། །

[Block 397]
དེ་ལྟར་ཡིན་ན་ཡང་དེ་ལྟ་ན་ཡང་སྐྱོན་ཅི་ཡང་མེད་དེ་བཤད་པ་ལས་བྱེ་བྲག་བསྒྲུབ་པར་བྱའོ། །

[Block 398]
དེ་ལ་ལྔ་པོ་ད་ལྟར་བའི་འབྲས་བུ་འཛིན་ཅིང་། གཉིས་ནི་ད་ལྟར་བ་སྐྱེད་པར་བྱེད་ལ་ད་ལྟར་བ་དང་འདས་པ་ལ་ནི་གཉིས་ཀྱིས་སོ། །

[Block 399]
གཅིག་ནི་འདས་པས་བསྐྱེད་དོ་ཞེས་ཆོས་མངོན་པ་ལས་རྣམ་པར་གཞག་པའི་ཕྱིར། ལྷན་ཅིག་འབྱུང་བ་དང་སྐལ་བ་མཉམ་པ་དང་མཚུངས་པར་ལྡན་པ་དང་ཀུན་དུ་འགྲོ་བ་དང་རྣམ་པར་སྨིན་པ་ཞེས་བྱ་བའི་རྒྱུ་ལྔ་ད་ལྟར་བའི་གནས་སྐབས་ཉིད་ན་འབྲས་བུ་འཛིན་ཏེ། འབྲས་བུ་མ་བཟུང་ན་མ་འོངས་པའི་དངོས་པོ་བསྐྱེད༌[^338]མི་ནུས་པའི་ཕྱིར་ན་རྒྱུའི་དངོས་པོ་ལ་གནས་སོ། །

[Block 400]
འབྲས་བུ་ཡང་འགའ་ཞིག་ད་ལྟར་བ་ཉིད་དུ་སྐྱེད་དེ་འདི་ལྟ་སྟེ། ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་དང་སྐལ་བ་མཉམ་པའི་རྒྱུ་དག་གི་སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་བཞིན་ནོ། །

[Block 401]
འགའ་ཞིག་ད་ལྟར་བ་དང་འདས་པ་སྟེ། འདི་ལྟ་སྟེ་སྐལ་བ་མཉམ་པའི་རྒྱུ་དང་ཀུན་དུ་འགྲོ་བའི་རྒྱུ་དག་གི་རྒྱུ་མཐུན་པའི་འབྲས་བུའོ། །

[Block 402]
འདས་པའི་དངོས་པོས་བསྐྱེད་དོ་ཞེས་པ་ནི་གསལ་ལོ། །

[Block 403]
ད་ལྟར༌[^339]བ་ནི་དེ་མ་ཐག་ཏུ་རྫོགས་པའི་ཕྱིར་འབྲས་བུ་བསྐྱེད༌[^340]པའོ། །

[Block 404]
འབྲས་བུ་སྐྱེས་པ་ན་དེ་དག་ཀྱང་འདས་པ༌[^341]འབྲས་བུ་བསྐྱེད་པའི་ཕྱིར་སླར་ཡང་འབྲས་བུ༌[^342]སྐྱེད་པ་མ་ཡིན་ལ། ད་ལྟར་བསྐྱེད་པའི་འབྲས་བུ་སླར་བསྐྱེད་པར་མི་ནུས་སོ། །

[Block 405]
རྣམ་པར་སྨིན་པའི་རྒྱུ་ནི་འདས་པ་ཉིད་ཀྱིས་འབྲས་བུ་འབྱིན་ཏོ།[^343] །གང་གི་ཚེ་དེ་ལྟར་རྒྱུ་རྣམས་འབྲས་བུ་འཛིན་པ་དང་སྐྱེད་པའི་འབྲེལ་པ་བྱས་པས་རྒྱུ་ཉིད་ལ་དེའི་ཚེ་འབྲས་བུ་ཡོད་ན་དེ་དང་འབྲེལ་བའི་རྒྱུ་ནི་རྒྱུ་ཉིད་དུ་འཐད་ཀྱི་མེད་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 406]
གང་ཡང་རྒྱུ་རྣམས་རྒྱུ་ཉིད་དུ་གྲུབ་པའི་དོན་དུ་འབྲས་བུ་ཡོད་པར་ཁས་ལེན་པ་དེའི་ཚེ་འབྲས་བུ་ཡོད་བཞིན་པ་ལ་རྒྱུས་ཅི་ཞིག་བྱ། གང་གི་དོན་དུ་རྒྱུ་ཡོངས་སུ་ཚོལ་བ་དེའི་འབྲས་བུ་ཡོད་པ་ཉིད་ན་རྒྱུས་དགོས་པ་ཅུང་ཟད་ཀྱང་མེད་དོ་ཞེས་བྱའོ། །

[Block 407]
ཡང་ན་འབྲས་བུ་འདིའི་རྒྱུ་འདིའོ་ཞེས་པ་རྣམ་པར་གཞག་པའི་དོན་དུ་འབྲས་བུ་ཡོད་བཞིན་པའི་རྒྱུ་འདོད་པ་དེ་ཡང་མི་འཐད་དེ། ཅིའི་ཕྱིར་ན་འདིར་འབྲས་བུ་ཡོད་པར་ཁས་བླངས་པ་ལ༌[^344]དགོས་པ་མེད་པས་རྒྱུ་མེད་པ་ཉིད་དུ་གྲུབ་པར་འདོད་པ་དང་། རྒྱུ་མེད་ན་འབྲས་བུ་ཡོད་པ་ཉིད་སེལ་བ་དང་ཕན་ཚུན་བརྟེན་པས་བསལ་བར་འགྱུར་བས་རྒྱུ་དང་འབྲས་བུ་འདིའི་རྒྱུ་འདིའོ་ཞེས་མི་འཐད་དོ། །

[Block 408]
དེས་ཀྱང་འབྲས་བུ་འདིའི་རྒྱུ་འདིའོ་ཞེས་རྣམ་པར་གཞག་པར༌[^345]དོན་དུ་འབྲས་བུ་ཡོད་བཞིན་པའི་རྒྱུ་འདོད་པ་དེ་ནི་མི་རིགས་ཏེ། ཇི་སྲིད་དེའི་འབྲས་བུ་མ་རྫོགས་པ་དེ་སྲིད་དུ་དངོས་པོ་འགའ་ཞིག་རྒྱུའི་རྣམ་པར་གཞག་པ་མེད་པར་འགྱུར་བས་འབྲས་བུ་དོན་དུ་གཉེར་བའི་འཇིག་རྟེན་པ་སུ་ཞིག་ཉེ་བར་ལེན་པ་དང་སྤོང་བ་ལ་འཇུག་པར་འགྱུར། འབྲས་བུ་དོན་དུ་གཉེར་བ་རྣམས་ཀྱིས་སྔར་རྒྱུ་ཉེ་བར་ལེན་ཅིང་རྒྱུ་མ་ཡིན་པ་ཡོངས་སུ་སྤངས་ནས་འཇུག་པར་འགྱུར་རོ་ཞེ་ན། འདི་དག་ནི་ཅུང་ཟད་ཙམ་སྟེ། དེ་ནི་འབྲས་བུ་ཡོད་ན་རྒྱུས་དགོས་པ་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 409]
ཡང་ན་དེའི་རྒྱུས་དགོས་པ་ཡོད་དོ་ཞེ་ན། དེ་ལྟ་ན་ཡང་དེ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། སྐྱེས་པ་སླར་ཡང་མི་སྐྱེ་བས་ཐུག་པ་མེད་པའི་སྐྱོན་དང་། སྐྱེ་བ་དོན་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་སྟེ། སྐྱེ་ལྟར་དེ་བཞིན་དུ་འབྲས་བུ་ཡོད་པ་ནི་རྒྱུ་འཐད་པ་མ་ཡིན་ནོ། །

[Block 410]
ཡང་ན་ཇི་སྐད་སྨོས་པའི་སྐྱོན་བསལ་བའི་དོན་དུ་མེད་པ་འབྲས་བུ་འདོད་ན། དེ་ལྟ་ན་ཡང་། དེར་མེད་ན་ཡང་རྒྱུ་མེད་མཚུངས། ། ཞོ་ཞེས་བྱ་བ་འབྲས་བུ་ཡོད་ན། འོ་མ་ནི་དེའི་རྒྱུ་ལ་ཆུ་ནི་མ་ཡིན་ནོ་ཞེས་རིགས་པར་འགྱུར་ཏེ། འབྲས་བུ་ལྡན་པ་དང་མི་ལྡན་པའི་ཕྱིར་རོ། །

[Block 411]
གང་དུ་དེའི་འབྲས་བུ་ཞོ་ཞེས་བྱ་བ་མེད།[^346] དེའི་ཚེ་ཞོ་ཞེས་བྱ་བ་འོ་མའི་འབྲས་བུ་ལ་ཆུ་ལ་སོགས་པ་ནི་རྒྱུ་མ་ཡིན་པ་དང་འོ་མ་རྒྱུ་ཡིན་པ་དག་ཁྱད་པར་མེད་པའི་ཕྱིར་འོ་མ་ལ་སོགས་པ་ལ་ཞོ་མི་སྐྱེ་བར་འགྱུར་ཏེ། རྒྱུ་མེད་པ་དང་མཚུངས་པའི་ཕྱིར་རོ། །

[Block 412]
དེ་ལྟར་འབྲས་བུ་མེད་ན་དེ་ལ་རྒྱུ་ཡང་མེད་དོ། །

[Block 413]
ཡང་ན་འདི་སྙམ་དུ་ཡོད་པ་དང་མེད་པའི་འབྲས་བུའི་རྒྱུ་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། ཡོད་དང་མེད་པ་ན་ཡང་འགལ་ཏེ། འབྲས་བུ་གཅིག་ལ་ཡོད་པ་དང་མེད་པ་ཕན་ཚུན་འགལ་བའི་ཕྱིར་མི་སྲིད་དོ་ཞེས་བྱ་སྟེ། དེ་ལྟ་བུའི་འབྲས་བུ་ཡོད་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 414]
དེ་མེད་ན་འབྲས་བུ་ཡོད་བཞིན་པ་མ་ཡིན་ལ། འབྲས་བུ་ལ་ལྟོས་པ་མེད་པའི་རྒྱུ་ནམ་ཡང་ག་ལ་ཞིག་ཅེས་པས་ཇི་སྐད་དུ་སྨོས་པའི་རིགས་པས་དུས་གསུམ་དུ་འབྲས་བུའི་རྒྱུ་འཐད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ་རྒྱུ་མེད་དོ། །

[Block 415]
དེ་ཉིད་ཀྱིས་ན་གསུངས་པ། དུས་གསུམ་དུ་ཡང་འཐད་མ་ཡིན། །ཞེས་བྱའོ། །

[Block 416]
དེ་ལ་འབྲས་བུ་ཡོད་པའི་རྒྱུ་འདོད་ན་སྔར་འབྲས་བུ་ལ་ཕྱིས་ནི་རྒྱུའོ་ཞེས་ཐོབ་པར་འགྱུར་ཏེ། སློབ་མ་དང་སློབ་དཔོན་བཞིན་ནོ། །

[Block 417]
འབྲས་བུ་མེད་ན་སྔར་ནི་རྒྱུ་ལ་ཕྱིས་ནི་འབྲས་བུའོ་ཞེས་ཐོབ་པར་འགྱུར་ཏེ་ཞོ་དང་འོ་མ་བཞིན་ནོ། །

[Block 418]
ཡོད་པ་དང་མེད་པའོ་ཞེ་ན། ད་ལྟ་བ་ལ་རྒྱུ་དང་འབྲས་བུ་དག་འཐོབ་པར་འགྱུར་ཏེ། སྐྱེ་བཞིན་པ་ནི་ཡོད་པ་དང་མེད་པའི་ངོ་བོའི་ཕྱིར་རོ། །

[Block 419]
དེ་ནི་འདི་ལྟར་རྣམ་པ་ཐམས་ཅད༌[^347]རྒྱུ་མི་འཐད་པར་གཟིགས་ནས་གསུངས་པ། དུས་གསུམ་དུ་ཡང་འཐད་མ་ཡིན། །ཞེས་སོ། །

[Block 420]
ཡང་ན་དུས་གསུམ་དུ་ཡང་འཐད་མ་ཡིན། །ཞེས་པའི་ཡང་གི་སྒྲ་ནི་ཕྱི་བར་བལྟའོ། །

[Block 421]
དེ་ལ་རྒྱུ་ནི་འདས་པ་དང་ད་ལྟར་དང་མ་འོངས་པ་ཉིད་ཀྱིས་ན་དུས་གསུམ་ལ་འབྲས་བུ་ཡང་དུས་གསུམ་མོ། །

[Block 422]
འབྲས་བུ་རེ་རེ་ལ་ཡང་དུས་གསུམ་དུ་ཡང་རྒྱུ་མི་སྲིད་དོ།[^348] །ཇི་ལྟར་བསྟན་པའི་རིགས་པས་ཞེས་གསུངས་པ། དུས་གསུམ་རྣམས་སུ་འཐད་མ་ཡིན། །ཞེས་བྱའོ། །

[Block 423]
དེ་སྐད་དུ་ཡང་རྩ་བའི་རབ་བྱེད་ཉི་ཤུ་པར།

[Block 424 [VERSE]]
འདས་པའི་འབྲས་བུ་འདས་པ་ཡི། །
རྒྱུ་དང་ལྷན་ཅིག་མ་ཡིན་ལ། །
མ་སྐྱེས་པ་དང་མ་སྐྱེས་པ། །
ནམ་ཡང་ལྷན་ཅིག་ཡོད་མ་ཡིན། །

[Block 425 [VERSE]]
མ་སྐྱེས་པ་ཡི་འབྲས་བུ་དང་། །
མ་སྐྱེས་རྒྱུ་དག་ལྷན་ཅིག་མིན། །
འདས་པ་དང་ནི་མ་སྐྱེས་པ། །
ནམ་ཡང་ལྷན་ཅིག་ཡོད་མ་ཡིན། །
--- END BLOCKS ---
