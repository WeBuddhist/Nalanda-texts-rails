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
[Block 351 [VERSE]]
སྐྱེ་བ་དང་ནི་འཇིག་པའི་ལམ། །
དགོས་པའི་དོན་དུ་བསྟན་པའོ། །

[Block 352]
དེ་བསྟན་པའི་སྒོ་ནས་དགོས་པ་འབའ་ཞིག༌[^249]སྒྲུབ་དགོས་པས་བཅོམ་ལྡན་འདས་ཀྱིས་སྐྱེ་བ་དང་འཇིག་པའི་ལམ་བསྟན་ཏོ། །

[Block 353]
སྐྱེ་བ་དང་འཇིག་པའི་ལམ་གྱིས་བསྟན་པའི་དགོས་པ་གང་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར།

[Block 354 [HEADING]]
### ཚིགས་བཅད་ཉེར་གཉིས་པ། ^1-23-0

[Block 355 [VERSE]]
སྐྱེ་བ་ཤེས་པས་འཇིག་པ་ཤེས། །
འཇིག་པ་ཤེས་པས་མི་རྟག་ཤེས། །
མི་རྟག་ཉིད་ལ་འཇུག་ཤེས་པས། །
དེས་ནི་ཆོས་ཀྱང་རྟོགས་པར་འགྱུར། །

[Block 356]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 357]
འདུ་བྱེད་རྣམས་ལ་ཆགས་པ་ནི་མྱ་ངན་ལས་འདས་པའི་གྲོང་ཁྱེར་དུ་འགྲོ་བའི་ལམ་བསྒྲིབས་ཤིང་འདུག་པས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་གཉེན་པོར་རེ་ཞིག་སྐྱེ་བ་དང་འཇིག་པའི་ལམ་བཤད་དོ། །ཇི་ལྟ་ཞེ་ན། འདི་ལྟར་སྐྱེ་བ་ཤེས་པས་འཇིག་པ་ཤེས་ཞེས་བྱ་བ་སྟེ། སྐྱེ་བ༌[^250]འཇིག་པའི་རྩ་བར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 358]
འཇིག་པ་ཤེས་པ་ལ་འཇིག་པ་དང་མི་རྟག་པ་གཉིས་དོན་གཅིག་ཏུ་ཁོང་དུ་ཆུད་པའོ། །

[Block 359]
ས་གསུམ་གྱི་མི་རྟག་པ་ཉིད་ཀྱི་མེ་རབ་ཏུ་འབར་བའི་ནང་དུ༌[^251]འདུག་པ་ཁྱིམ་རབ་ཏུ་འབར་བར་ཆུད་པ་བཞིན་དུ་གདོན་མི་ཟ་བར་དེ་ལས་འདའ་བར་འདོད་ན་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཆོས་ཉིད་ངེས་པར་འབྱིན་པ་འགྱུར་བ༌[^252]མ་སྐྱེས་པ་མ་འགགས་པ་ཁོང་དུ་ཆུད་ན་དེས་མཆོག་ཏུ་ཟབ་པ་མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བའི་ཆོས་ཁོང་དུ་ཆུད་དོ། །

[Block 360]
དེའི་ཕྱིར་དེ་ལྟར་བློ་མཆོག་དང་ལྡན་པའི༌[^253]རིམ་གྱིས་སྐྱེ་བ་དང་འཇིག་པའི་རྗེས་སུ་འབྲངས༌[^254]ནས།

[Block 361 [HEADING]]
### ཚིགས་བཅད་ཉེར་གསུམ་པ། ^1-24-0

[Block 362 [VERSE]]
གང་དག་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་། །
སྐྱེ་དང་འཇིག་པ་རྣམ་སྤངས་པ། །
ཤེས་པར་གྱུར་པ་དེ་དག་ནི། །
ལྟ་གྱུར་སྲིད་པའི་རྒྱ་མཚོ་རྒལ། །

[Block 363]
སྐྱེ་བ་མེད་པས་དངོས་པོར་ལྟ་བ་མེད། །འཇིག་པ་མེད་པས་ཆད་པར་ལྟ་བ་མེད་དོ། །

[Block 364]
སྐྱེ་བ་དང་འཇིག་པ་མེད་ན་རང་གི་མཚན་ཉིད་མེད་པས༌[^255]རྟག་པར་ལྟ་བ་མི་འབྱུང་ངོ་། །དེ་ལྟར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་སྐྱེ་བ་དང་འཇིག་པ་མི་དམིགས་ན་ལྟ་བར་གྱུར་པའི་སྲིད་པའི་རྒྱ་མཚོ་ལས་རྒལ་བ་ཡིན་ནོ། །

[Block 365]
ལྟ་བར་གྱུར་པ་ཉིད་སྲིད་པའི་རྒྱ་མཚོའོ། །

[Block 366]
ལྟ་བའི་ཆུ་བོ་ཉིད་ལྟ་བར་གྱུར་པའི་སྲིད་པའི་རྒྱ་མཚོ་ཡིན་ནོ། །

[Block 367]
སྟོང་པ་ཉིད་ལ་བརྩོན་པ་དག་ནི་སྟོང་པ་ཉིད་མཐོང་བའི་གྲུ་ཆེན་པོས་གདོན་མི་ཟ་བར་དེ་ལས་རྒལ་བར་འགྱུར་རོ། །

[Block 368]
གང་དག་སྟོང་པ་ཉིད་དུ་ལྟ་བས་འཇིག་པ་དེ་དག་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་སྐྱེ་བ་དང་འཇིག་པའི་མཐའ་གཉིས་སུ་ལྟུང་བ་དང་བྲལ་བར་ཁོང་དུ་ཆུད་པར་མི་ནུས་ཏེ་དེ་དག་གདོན་མི་ཟ་བར།

[Block 369 [HEADING]]
### ཚིགས་བཅད་ཉེར་བཞི་པ། ^1-25-0

[Block 370 [VERSE]]
སོ་སོའི་སྐྱེ་བོ་དངོས་བདག་ཅན། །
ཡོད་དང་མེད་པར་ཕྱིན་ཅི་ལོག །
ཉེས་པས་ཉོན་མོངས་དབང་གྱུར་པ། །
རང་གི་སེམས་ཀྱིས་བསླུས་པར་འགྱུར། །

[Block 371]
ལས་ཇི་ལྟ་བ་དང་ཉོན་མོངས་པ་ཇི་ལྟ་བ་བཞིན་དུ་སོ་སོར་སྐྱེ་བས་སོ་སོའི་སྐྱེ་བོའོ། །

[Block 372]
གང་དངོས་པོ་རྣམས་ལ་བདག་ཉིད་དུ་གནས་པར་འཛིན་པ་དེ་དག་དངོས་བདག་གམ།[^256] དངོས་པོ་ལ་བདག་ཏུ་འཛིན་པ་གང་ཡིན་པ་དེ་དག་དངོས་བདག་ཅན་ཏེ། བདག་ཏུ་འཛིན་པས་དེ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 373]
ཡང་ན་ནི་དངོས་པོ་ལ་མངོན་པར་ཞེན་པས་དངོས་བདག་ཅན་ཏེ། དེ་དག་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ལ་ཕྱིན་ཅི་ལོག་པའི་ཉེས་པ་རང་གིས་ཡོངས་སུ་རྟོག་པས་བསྐྱེད་པས་ཉོན་མོངས་པ་རྣམས་ཀྱི་དབང་དུ་འགྱུར་རོ། །

[Block 374]
དེ་དག་དངོས་པོ་ཡིད་དུ་འོང་བའི་གནས་སུ་གྱུར་པ་ལ་ནི་རྗེས་སུ་ཆགས་པར་འགྱུར། དེ་མེད་པ་ལ་ནི་ཁོང་ཁྲོ་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་སྦྱར་རོ། །

[Block 375]
ཉོན་མོངས་པའི་དབང་དུ་གྱུར་པས་འཇུག་སྟེ། གང་དགེ་བ་དང་མི་དགེ་བའི་ལས་ཉེ་བར་ལེན་པ་ཡོད༌[^257]ན་འཁོར་བས་དེ་ལྟར་སོ་སོའི་སྐྱེ་བོ་དངོས་པོ་ལ་མངོན་པར་ཞེན་པ་རྣམས་རང་གི་སེམས་ཀྱིས་བསླུས་སོ། །

[Block 376]
དངོས་པོ་ལ་མངོན་པར་ཞེན་པ་རང་གི་སེམས་ཀྱིས་ཡོངས་སུ་བརྟགས་པ་དང་། དངོས་པོའི་རང་གི་ངོ་བོ་རང་བཞིན་གྱིས་གྲུབ་པ་མེད་པའི་ཕྱིར་དངོས་པོ་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་མཐོང་བ་བསྒྲིབས་ཏེ་ཕྱིན་ཅི་ལོག་ཏུ་སྒྲོ་བཏགས༌[^258]པས་རང་གི་སེམས་ཀྱིས་བསླུས་ཏེ་བྲིད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 377]
སུ་དག་དགེ་བའི་བཤེས་གཉེན་གྱིས་སྟོང་པ་ཉིད་བསྟན་པ་ལ་གཡང་ས་ལྟ་བུར་མི་སེམས་ཤིང་། འདི་ནི་ཆོས་རྣམས་ཀྱི་དོན་དམ་པ། འདི་ནི་མྱ་ངན་ལས་འདས་པའི་གྲོང་ཁྱེར་དུ་འགྲོ་བ་ཡིན་པར་ཤེས་པ་སླུ་བའི་སེམས་ལ་སླུ་བ་ཉིད་དུ་ཡང་དག་པར་རྟོགས་ནས་སྐད་ཅིག་ཙམ་ཡང་ཡིད་མི་རྟོན་པ་དེ་དག་ནི་ངེས་པར་འཕགས་པར་གྱུར་པར་བལྟ་སྟེ།

[Block 378 [HEADING]]
### ཚིགས་བཅད་ཉེར་ལྔ་པ། ^1-26-0

[Block 379]
དངོས་ལ་མཁས་པ་རྣམས་ཀྱིས་ནི།

[Block 380 [VERSE]]
དངོས་པོ་མི་རྟག་སླུ་བའི་ཆོས། །
གསོག་དང་སྟོང་པ་བདག་མེད་པ། །
རྣམ་པར་དབེན་པར་རབ་ཏུ་མཐོང་། །
བྱུང་བས་དངོས་པོ་ཞེས་བྱ་སྟེ། །

[Block 381]
དངོས་པོ་ཞེས་བྱ་བའི་སྒྲ་ནི་འདུས་པ༌[^259]ལ་བྱའོ། །

[Block 382]
དངོས་པོ་དེ་ཡང་སྐད་ཅིག་རེ་རེ་ལ་འཇིག་པའི་ངང་ཅན་ཡིན་པས་མི་རྟག་པའོ། །

[Block 383]
དངོས་པོའི་རང་བཞིན་ནི་ངོ་བོ་ཉིད་མེད་པ་ཡིན་ན་གང་གི༌[^260]ཕྱིར་བྱིས་པ་རྣམས་ལ་ངོ་བོ་ཉིད་ཡོད་པར་སྣང་བ་དེའི་ཕྱིར་སྒྱུ་མ་ལ་སོགས་པ་བཞིན་དུ་སླུ་བས་ན་དངོས་པོ་དེ་ཉིད་སླུ་བའི་ཆོས་སོ། །

[Block 384]
རིང་དུ་གནས་པའི་མཐུ་མེད་ལ༌[^261]རང་བཞིན་གྱིས་ཉམ༌[^262]ཆུང་བས་གསོག༌[^263]གོ། །

[Block 385]
ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་སྟོང་པའོ། །

[Block 386]
བདག་གིས་སྟོང་པའི་ཕྱིར་བདག་མེད་པ་སྟེ། མི་རྟག་པ་ལ་སོགས་པས་དངོས་པོའི་རང༌[^264]གི་ངོ་བོ་བསྙད་དོ། །

[Block 387]
དེ་བས་ན་དངོས་པོ་འདི་དེ་ལྟར་མཐོང་བས་མཁས་པ་དེ་དག་གིས་དབེན་པར་མཐོང་ངོ་། །དབེན་ཞེས་བྱ་བ་ནི་སྟོང་པའོ། །

[Block 388]
དེ་ལྟར་ན་དབེན་པ༌[^265]མཐུན་པའི་ཕྱིར་སྐྱེ་བ་མེད་པའི་དགོན་པ་རྣམས་ལ་དབེན་པ་ཞེས་བྱ་སྟེ། དེ་བཞིན་དུ་འདིར་ཡང་རྣལ་འབྱོར་པས་དངོས་པོ་དབེན་པར་མཐོང་ཞེས་བྱ་བ་ནི་སྟོང་པར་མཐོང་བའི་བར་ལ་བྱའོ། །

[Block 389]
དེ་དག་དངོས་པོ་ཉིད་སྐུར་ཏེ་དབེན་པར་མཐོང་བ༌[^266]མ་ཡིན་གྱི། དངོས་པོ་སྟོང་པར་གྱུར་པ་ལ་སྟོང་པར་མཐོང་ངོ་། །སྟོང་པ་ཉིད་བསྟན་པའི་ཕྱིར་མི་རྟག་པ་ལ་སོགས་པ་བྱེ་བྲག་རྣམས་སྨོས་སོ། །

[Block 390]
ཡང་ན་དབེན་པ་ནི་དྲི་མ་མེད་པ་ཡིན་ན་འདི་ལྟར་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པའི་དངོས་པོ་ཡང་རང་གི་རྟོག་པའི་དྲི་མས་སྦགས་པའི་ཕྱིར་ཕྱིན་ཅི་ལོག་ཏུ་ཁོང་དུ་ཆུད་ཀྱི་འཕགས་པ་རྣམས་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། དེ་དག་ནི་མེད་པ་ལ་སྒྲོ་མི་འདོགས་པར་དབེན་པར་དྲི་མ་མེད་པ་ཉིད་དུ་གཟིགས་སོ། །
--- END BLOCKS ---
