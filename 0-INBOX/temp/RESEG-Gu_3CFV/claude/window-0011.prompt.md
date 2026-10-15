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
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་སྔར་བཟའ་བ་མ་ལགས་པ་ལ་གཡར་དྲངས་ན། དེ་སླད་ཀྱིས་བཟའ་བ་ལ་གཡར་དྲངས་ཏེ་དེས་དེ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེ་བ་འཁོར་ལྟུང་བ་མེད་དོ། །

[Block 387]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་བཟའ་བ་ལྔ་པོ་རྣམས་མ་གཏོགས་པ་དེ་ལས་གཞན་པའི་བཟའ་བ་དག་ལ་སྔར་གཡར་དྲངས་ནས་དེ་སླད་ཀྱིས༌[^251]བཟའ་བ་ལྔ་པོ་རྣམས་ལ་གཡར་དྲངས་ཏེ་དེས་དེ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེ་བ་འཁོར་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །ཅི་ཐམས་ཅད་ལ་ལྟུང་བ་འདི་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ན་བ་མ་ཡིན་པ་དང་ལས་མ་བྱས་པ་དང་། ལམ་དུ་མ་སོང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ན་བ་ལ་སོགས་པར་གནས་པའི་དུས་དང་ལྡན་པ་རྣམས་ལ་ལྟུང་བ་མེད་དོ། །

[Block 388]
གནས་པ་མ་ཡིན་པའི་དུས་ཐམས་ཅད་ལ་ནི་ཉས་བྱས་སོ་ཞེས་གསུངས་པ་མི་གནས་པའི་དུས་ལ་ཉེས་བྱས་ཞེས་བྱ་སྟེ། དེ་བས་ན་ཉེས་བྱས་སུ་གཏོགས་པར་བྱའོ། །

[Block 389]
རྙེད་པ་གང་ལ་གང་གི་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེ་བླངས་ན༌[^252]ཉེས་བྱས་ཀྱིའོ། །

[Block 390]
ཟོས་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དང་དུ་བླངས་ཡིད་ཀྱི་ཡིན་པའི་ཕྱིར་དེ་ནི་བསྡམ་པར་བྱ་བའི་ཉེས་བྱས་སུ་གསུངས་པར་རིག་པར་བྱའོ། །

[Block 391]
འདིར་ཁར་ཟ་བའི་མདུན་རོལ་དུ་འགྲོ་བ་ལ་སོགས་པ་རྗེས་སུ་བསྒྲུབ་པ་བསྟན་པར་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 392]
འདིར་གོས་ཀྱི་མཐར་གྱུར་པ་ནི་ཁྲུ་གང་གི་ཁྱོན་ནོ་ཞེས་བྱ་བ་ནི་འདི་ལས་ཆུང་བའི་ཆོས་གོས་དང་ལྡན་པ་ལ་བོས་པ་ནི་གོས་མེད་པ་ཉིད་ནི་འདིར་དངོས་གཞི་ཁོ་ན་སྟེ། དེ་བས་འདི་ལ་འདི་བྱེད་པ་ཡིན་ཏེ། ཇི་ཙམ་དུ་སྤང་བའི་བྱེད་པ་པོ་དེ་ཉིད་དེ་ཙམ་ལ་གཞན་དུ་ཡང་ཡན་ལག་ཉིད་དེ་བས་ན་དེ་ལ་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 393]
དེའི་ཕྱིར་གོས་སྦྱིན་པར་བྱ་བ་དང་གོས་བྱ་བ་ལ་སོགས་པ་ལ་ཡང་འདི་ཙམ་ལ་མཐར་ཐུག་པར་འགྱུར་བ་ཉིད་དུ་རྟོགས་པར་བྱའོ། །

[Block 394]
ཆུང་བ་ཉིད་སྦྱིན་པ་དང་བྱེད་པ་ལ་ཉེས་བྱས་སུ་རྣམ་པར་གནས་པ་ཡིན་ཏེ། འདིར་ནི་དངོས་གཞི་ཁོ་ནའོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 395]
ལམ་ནི་དཔག་ཚད་ཕྱེད་དོ་ཞེས་བྱ་བ་ནི་འདིར་ལས༌[^253]འདི་ནི་མཐར་ཐུག་པར་གྱུར་པ་ཉིད་དོ། །

[Block 396]
གཞན་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡང་ཡང་ཟ་བ་ལས་གཞན་པའི་བསླབ་པའི་གཞི་དག་ལ་འདུས་ཤིང་ཟ་བ་ལ་སོགས་པའི་དོན་དུ་འདི་ཡིན་ནོ། །

[Block 397]
འདིར་རམ་གྲུར་འགྲོ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། འདིར་ཞེས་བྱ་བ་ནི་ལམ་ལ་སྟེ། ཐང་གི་ལམ་ཉིད་ཀྱི་ཡུལ་ལ་འདིའི་མཐར་ཐུག་པར་གྱུར་པའི་ལམ་གྱི་ཚད་མ་ཡིན་ནོ། །

[Block 398]
འོན་ཀྱང་གྲུར་འགྲོ་བ་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 399]
ལས་ཀྱི་ངོ་བོ་ཅི་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ལས་ནི་ཕྱག་དར་རེ་ལྡེ་ཙམ་མམ། དཀྱིལ་འཁོར་བ་མལ་ཙམ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ནི་ལས་ཀྱི་མཐར་གྱུར་པའི་ཚད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 400]
གཞན་ལ་ཡང་ངོ་ཞེས་བྱ་བ་འདི་སྦྱར་བར་བྱའོ། །

[Block 401]
དེ་ཡང་དགེ་འདུན་ཉིད་དམ་མཆོད་རྟེན་ཉིད་ནའོ་ཞེས་བྱ་བ་ནི། ལས་འདིའི་རབ་ཏུ་དབྱེ་བ་འདི་དག་རིག་པར་བྱའོ། །

[Block 402]
དེ་ལྟ་བུར་གྱུར་པའི་ཡན་ལག་འདི་བརྗོད་པ་ཤེས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 403]
ན་བ་ཉིད་ཀྱི་ཚད་ནི་མི་ནུས་པའོ་ཞེས་བྱ་བ་ནི་གཞན་ལ་ཡང་ངོ་ཞེས་བྱ་བ་འདིར་ཡང་སྦྱར་བར་བྱའོ། །

[Block 404]
བཤམས་པ་ནི་མགྲོན་དུ་བོས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གང་ཞིག་གཏན་དུ་བའམ་བར་མ་ལས་བྱུང་བ་བཤམས་པར་གྱུར་པ་དེ་ནི་བོས་པར་རྟོགས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 405]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས།

[Block 406]
མངོན་པར་ལྷག་པ་ཟོས་ན་ལྟུང་བ་མེད་དོ། །

[Block 407]
མངོན་པར་ལྷག་པ་ཞེས་བྱ་བ་ནི་དགེ་སློང་ལ་བཤམས་པའི་བསོད་ནམས་ཀྱི་ཕུང་པོ་ལ་བརྗོད་པ་ཡིན་ཏེ། དེ་ཟོས་པ་ན་ལྟུང་བ་མེད་ཅེས་བྱ་བའོ། །

[Block 408]
དགེ་སློང་གི་ཕྱིར་བཤམས་པ་ནི་དགེ་སློང་ལ་བཤམས་པའོ། །

[Block 409]
ཀུན་དུ་ལྟ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡང་མགྲོན་དུ་བོས་པ་ཉིད་མ་ཡིན་པ་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་ངམ་བཤེས་པའི་དབང་གིས་འབོད་པ་ཉིད་ནི་ཀུན་དུ་ལྟ་བའོ། །

[Block 410]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་སྤྱན་གཟིགས་སམ་གསོལ་ལ་གདུགས་ཚོད་ཙམ་གཞན་དུ་གསོལ་ཅིག་ཅེས་ཟེར་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 411]
འདི་ཉིད་དུ་དགེ་སློང་གསོལ་ཞིང་གཞན་འཚོལ་བར་བྱེད་ན་ལྟུང་བ་མེད་དོ། །

[Block 412]
འདི་ཉིད་དུ་དགེ་སློང་བསོད་སྙོམས་ཙམ་པོ༌[^254]འཚོལ་ཞིང་ལྷག་མ་གཞན་ནས་ཚོལ་བར་བྱེད་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 413]
ཡང་ཡང་ཟ་བ་ལ་ནི་ཉེས་པ་མེད་པའི་ཚིག་འདི་ཡིན་གྱི་ཐམས་ཅད་དུ་ནི་མ་ཡིན་ནོ། །

[Block 414]
དགག་དབྱེ་ཉིད་ཡོད་པར་གྱུར་པ་ལ་སྟན༌[^255]གཅིག་ལ་ཟ་བ་ལས་འདའ་བར་བྱེད་པའི་ལྟུང་བ་ལས་ལྡང་བ་ཡོད་པ་ཡིན་ནོ། །

[Block 415]
མགྲོན་དུ་བོས་པ་གཞན་ཡོད་ན་ཟན་བླང་བ༌[^256]ལ་སྤང་བ༌[^257]བསྲུང་ཞིང་འཇུག་པར་བྱའོ། །

[Block 416]
ཐོ་འཚམས༌[^258]པས་བྱས་པ་ནི་མ་ཡིན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མགྲོན་དུ་བོས་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 417]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་སྔར་ཐོ་འཚམས༌[^259]པའི་རྟོག་པ་ཅན་གྱིས་གཡར་དྲངས་པར་གྱུར་ནས་སླད་ཀྱི་ཐ་མལ་པའི་གནས་སྐབས་སུ་གཡར་དྲངས་པ་གཞན་རྙེད་ཅིང་དེ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེ་བ་འཁོར་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 418]
ཐོ་འཚམས༌[^260]པའི་རྟོག་པ་ཞེས་བྱ་བ་ནི་ཐོ་འཚམས༌[^261]པའི་རྟོག་པ་སྟེ་གཞན་ལ་ཞེས་བྱ་བ་འདི་ཉམས་པའོ། །

[Block 419]
མི་རུང་བ་ཞེས་བྱ་བ་ནི་བྱས་པ་ལ་མེད་པ་ཉིད་དོ། །

[Block 420]
དེ་བས་ན་བོས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བཟའ་བར་བྱ་བ་མི་རུང་བ་ཉིད་ཀྱི་ཕྱིར་སྐྱེས་པར་རིག་པར་བྱའོ། །

[Block 421]
དེའི་ཕྱིར་མ་ཡིན་པར་དགེ་འདུན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལ་བརྟེན་ནས་དགེ་འདུན་སྤྱན་དྲངས་པ་དེའི་མེད་པ་ཉིད་ན་དེའི་ཕྱིར་རྣམ་པར་གཅད་པར༌[^262]བྱ་བ་ལ་མངོན་པར་བརྟེན་པ་ཉིད་ཀྱི་ཕྱིར་གཞན་ལ་ནི་མེད་པ་ཉིད་དོ། །

[Block 422]
འདིར་ཁུངས་ནི་གང་གི་ཕྱིར་འཕགས་པ་ལེགས་འོངས་ཀྱི་ཕྱིར་ཏེ། གང་དེ་ལ་བརྟེན་ན་ཆུ་སྲིན་བྱིས་པ་གསོད་ཀྱི་རི་པ་རྣམས་ཀྱིས༌[^263]དགེ་འདུན་སྤྱན་འདྲེན་པ་ལ་བྲམ་ཟེ་སྤྱན་དྲངས་པར་གྱུར་པས་བྲམ་ཟེ་རྣམས་འོངས་ནས་བྱིས་པ་གསོད་པའི་རི་པའི་བྲམ་ཟེ་དང་ཁྱིམ་བདག་རྣམས་ཀྱིས༌[^264]སངས་རྒྱས་ལ་སོགས་པ་དགེ་སློང་གི་དགེ་འདུན་ཞག་བདུན་བཤོས་ལ་སྤྱན་དྲངས་པས་དེའི་ཚེ་ངས་དང་དུ་མ་བླངས་སོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 423]
དགག་དབྱེ་སོ་སོར་རྗེས་སུ་གནང་བ་དང་སྦྱར་བར་བྱའོ། །

[Block 424]
གཞན་དུ་ལྔ་པོ་འཇོག་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མགྲོན་དུ་བོས་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 425]
སིལ་བུ་དག་ལས་དང་པོ་ལྔ་པོ་ཞེས་བྱ་བ་འདི་བརྗོད་པ་ཡིན་ཏེ། དེ་བས་ན་གཞུང་ནི་ཡི་གེ་གཞན་ལས་དགེ་སློང་བཅའ་བ་དང་བཟའ་བའི་ཟན་གཉིས་དང་མགྲོན་དུ་བོས་པས་གཅིག་དགེ་སློང་ལ་རྣམ་པར་རྟོག་པར་བྱེད་ན་ལྟུང་བ་མེད་དོ། །
--- END BLOCKS ---
