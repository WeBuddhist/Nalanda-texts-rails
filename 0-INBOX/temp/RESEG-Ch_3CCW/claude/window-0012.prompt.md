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
[Block 421]
དེའི་ཕྱིར་འདི་ནི་ཕྱིན་ཅི་མ་ལོག་པ་རྣམས་ཀྱིས༌[^278]སྒྱུ་མ་བཞིན་དུ་གཟིགས་སོ། །

[Block 422]
བྱིས་པ་རྣམས་ཀྱི་རྨོངས་པའི་གྲོང་ཁྱེར་གང་ཡིན་པ་དེ་འཕགས་པ་རྣམས་ཀྱིས་སྒྱུ་མ་བཞིན་དུ་གཟིགས་ཏེ། མ་རིག་པའི་མུན་པ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 423]
འདིའི་ཕྱིར་ཡང་འདི་ལྟར་འགྲོ་བ་དེ་དངོས་པོ་མེད་དེ་འདི་ལྟར།

[Block 424 [HEADING]]
### ཚིགས་བཅད་ཉེར་བརྒྱད་པ། ^1-29-0

[Block 425 [VERSE]]
ཚངས་པ༌[^279]ལ་སོགས༌[^280]འཇིག་རྟེན་འདི། །
བདེན་པར༌[^281]རབ་ཏུ་གང་བརྗོད་པ། །
འཕགས་ལ་དེ་ཡང་བརྫུན་ཞེས་གསུངས། །
དེ་ལས་གཞན་ན༌[^282]ཅི་ཞིག་ལུས། །

[Block 426]
སྒྱུ་མ་ལྟ་བུར་མ་གྱུར་པ་གང་ཡང་ཡོད་དམ་ཞེས་བྱ་བ་ཚིག་གི་ལྷག་མའོ། །

[Block 427]
དབང་པོ་ཡུལ་ལས་འདས་པའི་དོན་ཡོངས་སུ་གཅོད་པ་ནི་འཇིག་རྟེན་ན་ཚངས་པ་ནི་ཚད་མའོ། །

[Block 428]
དེ་ལྟར་ཚད་མར་གྱུར་པ་དེ་ལ་དངོས་པོ་རྣམས་ཀྱི་རང་གི་ངོ་བོ་བདེན་པར་སྣང་བ་གང་ཡིན་པ་དེ་ཡང་འཕགས་པ་རྣམས་ལ་བརྫུན་ནོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་མྱ་ངན་ལས་འདས་པ་ཉིད་བདེན་པ་གཅིག་པུའོ། །ཞེས་བསྟན་པ་ནི་གསུངས་ཏེ། འདུས་བྱས་ནི་བརྫུན་པ་སླུ་བའི་ཆོས་ཅན་ཡིན་ན་གཞན་དག་ལ་སྣང་བ་གང་ཡིན་པ་དེ་བརྫུན་པར་ཅིའི་ཕྱིར་མི་འགྱུར། གང་ལ་བརྫུན་པ་ཉིད་དུ་ཐེ་ཚོམ་མེད་པ་དེ་ལས་གཞན་ཅི་ཞིག་ལུས་ཞེས་བྱ་བ་ནི་སྒྱུ་མ་ལྟ་བུར་མ་གྱུར་པ་གང་ཡང་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 429]
འདི་ནི་གདོན་མི་ཟ་བར་ཁས་བླང་བར་བྱའོ། །

[Block 430]
གཞན་དུ་ན་གལ་ཏེ་ཚངས་པ་ལ་སོགས་པ་དང་། འཕགས་པ་རྣམས་འཇིག་རྟེན་འདི་ལ་ལྟ་བ་མཚུངས་པར་གྱུར་ན་ནི་དེའི་ཚེ་འཕགས་པ་རྣམས་དང་འཕགས་པ་མ་ཡིན་པ་རྣམས་མཚུངས་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 431]
དེ་དག་མཚུངས་པར་མི་སྲིད་པར་བསྟན་པའི་ཕྱིར།

[Block 432 [HEADING]]
### ཚིགས་བཅད་ཉེར་དགུ་པ། ^1-30-0

[Block 433 [VERSE]]
འཇིག་རྟེན་མ་རིག་ལྡོངས་གྱུར་པ། །
སྲིད་པའི་རྒྱུན་གྱི་རྗེས་འབྲང་དང་། །
མཁས་པ་སྲེད་དང་བྲལ་བ་ཡི། །
དགེ་བ་རྣམས་ལྟ་ག་ལ་མཉམ། །

[Block 434]
ཞེས་བྱ་བ་སྨོས་ཏེ་མ་རིག་པའི་ལིང་ཏོག་གིས་ཁེབས་ནས། བློའི་མིག་ལྡོངས་པར་གྱུར་པ་ཚངས་པ་ལ་སོགས་པ་འགྲོ་བ་མ་ལུས་པ་ཡང་དག་པར་མཐོང་བ་དང་བྲལ་བའི་ཕྱིར། རང་དབང་མེད་པར་འགྲོ་བ་ཐོག་མ་མེད་པའི་འཁོར་བས་འཁོར་བར་འཕངས་པས་བྲུབ་པ་ན་ཤུགས་ཀྱིས་ལྦུ་བ་འཁོར་བ་ལྟ་བུའི་འཁོར་བའི་འཁོར་ལོ་ཆུ་ཀླུང་ཆེན་པོར་ཕྱིན་ཅི་ལོག་གི་རླུང་གིས་དཀྲུགས༌[^283]ཏེ། འཁྲུགས་པས་དགེ་བའི་ཕྱོགས་ཀྱི་གྲུ་ཆག་པ༌[^284]དགེ་བའི་ལས་ཀྱི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་མཐར་ཐུག་པའི་ལྟོང༌[^285]ཅན་སྲེད་པའི་རྒྱུན་གྱི་རྗེས་སུ་འགྲོ་བ་སོ་སོའི་སྐྱེ་བོ་དང་། མཁས་པ་ཤེས་རབ་ཀྱིས་དག་པ་བློའི་མིང་ཅན་དམ་པའི་ཆོས་བདུད་རྩིའི་ཁུ་བའི་རྒྱུན་གྱི་བཏུང་བས་ངོམས་པ་གཅིག་ཏུ་ཆོས་ཀྱི་ངང་ཚུལ་ཅན་གྱི་དགེ་བ་རྣམས་དང་། གོང་དུ་སྨོས་པའི་འཇིག་རྟེན་དུ་མཚུངས་པར་བརྟག་ཏུ་ག་ལ་རུང་སྟེ། སྣང་བ་དང་། མུན་པ་དང་། འཁོར་བ་དང་། མྱ་ངན་ལས་འདས་པ་མཚུངས་པར་བརྟག་པ༌[^286]ནི་མི་རིགས་སོ། །

[Block 435]
དེ་བས་ན་ཚངས་པ་ལ་སོགས་པའི་འཇིག་རྟེན་འཁོར་བའི་རྗེས་སུ་མཐུན་པར་འགྲོ་བ་འདི་ནི་བདེན་པ་གང་ཡིན་པ་དེ་ནི་གདོན་མི་ཟ་བར་འཕགས་པ་རྣམས་ལ་བརྫུན་པ་ཡིན་ནོ། །

[Block 436]
གང་གི་ཕྱིར་དེ༌[^287]དེ་ལྟར་འཕགས་པ་རྣམས་ཀྱིས་འདི་སྐད་ཅེས། །

[Block 437 [VERSE]]
རྨོངས་པའི་གྲོང་ཁྱེར་མི་བཟད་པ། །
འགྲོ་བ་སྒྱུ་མ་བཞིན་དུ་སྣང་། །

[Block 438]
ཞེས་སྨོས་པ་གང་ཡིན་པ་དེ་ལ་མཁས་པ་རྣམས་དོགས་པ་སྤངས་ཏེ་མོས་པར་བྱའོ། །

[Block 439]
འདིར་སྨྲས་པ། གལ་ཏེ་འགྲོ་བ་སྒྱུ་མ་བཞིན་དུ་རང་བཞིན་གྱིས་སྟོང་ན་འདི་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་དེ་ཁོ་ན་གང་ཡིན་པ་དེ་མི་བསྟན་པར་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ཡོད་དོ་ཞེས་བསྟན་པ་བདེན་པ་མ་ཡིན་པ་འདིས་ཅི་ཞིག་བྱ། བཤད་པ། བདེན་པ་ཉིད་ནི་བསྟན་གྱི་བརྫུན་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི༌[^288]ག་ལས་འོངས། འཇིག་རྟེན༌[^289]བདེན་ཡང་མི་དགོས་ན་ནི་ཁ་ཅིག་མི་བསྟན་ཏོ། །

[Block 440]
བརྫུན་ཡང་དགོས་པ་ཡོད་ན་ནི་ལ་ལ་བསྟན་དགོས་ཏེ་འདི་ལ་ནི་དོན་དམ་པ་ལ་འཇུག་པའི་ཐབས་སུ་དགོས་པ་ཡོད་པས་ཕུང་པོ་དང་ཁམས་ལ་སོགས་པ་བདེན་པ་མ་ཡིན་ཡང་ཡོད་དོ། །ཞེས་ཐོག་མ་ཉིད་དུ་བསྟན་པའི་དབང་དུ་བྱས་ཀྱི། དེ་ཁོ་ན་ཡང་དག་པ་སྟོང་པ་ཉིད་ནི་མ་ཡིན་ཏེ། དེ་ལ་ཐོག་མར་བསྟན་ན་དོན་མེད་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 441]
མཐའ་གཉིས་ཀྱི་གཡང་ས་མེད་པའི་ཆོས་འདི་སྐྱེ་བོ་བློ་གྲོས་མ་བྱང་བ་ལ་ཐོག་མ་ཉིད་དུ་བསྟན་མི་བཟོད་དེ། དེ་བས་འགྲོ་བའི་དོན་སྒྲུབ་པ་ལ་མཁས་པ་ཐབས་ལ་ཁོང་བཟོ་བས།

[Block 442 [HEADING]]
### ཚིགས་བཅད་སུམ་ཅུ་པ། ^1-31-0

[Block 443 [VERSE]]
དེ་ཉིད་ཚུལ༌[^290]ལ་ཐོག་མར་ནི། །
ཐམས་ཅད་ཡོད་ཅེས་བརྗོད་པར་བྱ། །
དོན་རྣམས་རྟོགས་ཤིང་ཆགས་པ༌[^291]ནས། །
དེ་ཡི་འོག་ཏུ་དབེན་པའོ། །

[Block 444]
སྐྱེ་བོ་བློ་གྲོས་མ་བྱང་བ་དག་ཐོག་མ་ཁོ་ནར་སྟོང་པ་ཉིད་དུ་ལྟ་བ་ལ་བཙུད་ན་ཤིན་ཏུ་མགོ་རྨོངས་པར་འགྱུར་ཏེ། དེ་བས་ན་འཕགས་པ་རྣམས་སྟོང་པ་ཉིད་ཐོག་མ་ཁོ་ནར་མི་སྟོན་ཏེ། དངོས་པོ་ལ་ཆགས་པ་དང་ལྡན་པ་དངོས་པོའི་ངོ་བོ་ཉིད་རབ་ཏུ་དབྱེ་བ་ལ་དགའ་བ་རྣམས་ཀྱི་འདོད་པའི་དོན་ཡང་དག་པར་བརྗོད་པས་བདག་ལ་གཅེས་པར་འཛིན་པར་བྱ་བའི་ཕྱིར་དེ་ཁོ་ན་ཚོལ་བ་ལ་ཐོག་མར་ཐམས་ཅད་ཡོད་དོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 445]
དེའི་དངོས་པོ་ནི་དེ་ཉིད་དོ། །

[Block 446]
བརྗོད་པར་འདོད་པའི་དོན་སྤྱིའི་དངོས་པོ་དང་འབྲེལ་པ་ཅན་དེའི་ཞེས་བྱ་བ་འདི་དང་སྦྱར་རོ། །

[Block 447]
དངོས་པོ་ནི་རང་གི་ངོ་བོ་སྟེ། གང་གི་རང་གི་ངོ་བོ་གང་ཡིན་པ་དེ་ནི་དེའི་དངོས་པོ་སྟེ། དེ་ཁོ་ནའོ། །

[Block 448]
རང་གི་ངོ་བོའོ། །

[Block 449]
ངོ་བོ་ཉིད་དོ། །

[Block 450]
དེ་བཞིན་ཉིད་དོ། །

[Block 451]
གཞན་མ་ཡིན་པ་ཉིད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 452]
དེ་ཁོ་ན་ཚོལ་བའི་ངང་ཚུལ་ཅན་ཡིན་པས་ན་དེ་ཁོ་ན་ཚོལ་བའོ། །

[Block 453]
དེ་ཁོ་ན་ཚོལ་བར་འདོད་པ་དེ་ལ་བླ་མ་ཕན་པར་འདོད་པས་ཇི་སྐད་བརྗོད་པར་བྱ་ཞེ་ན། ཐམས་ཅད་ཡོད་དོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 454]
བྲམ་ཟེ་ཐམས་ཅད༌[^292]ཅེས་བྱ་བ་ནི་ཕུང་པོ་ལྔ་དང་། སྐྱེ་མཆེད་བཅུ་གཉིས་དང་། ཁམས་བཅོ་བརྒྱད་ཀྱི་བར་དག་གོ་ཞེས་གསུངས་སོ། །

[Block 455]
དེའི་ཤེས་པ་དང་སྦྱར་ཏེ་ཕུང་པོ་ལ་སོགས་པ་དེ་དང་འདི་ཡོད་པར་བརྗོད་པར་བྱའོ། །

[Block 456]
ཕུང་པོ་ལ་སོགས་པ་དེ་དག་ཀྱང་ཉེ་བར་བཟུང་སྟེ་དེ་དང་འདིའི་ཡོད་པ་གང་ཡིན་པ་དེ་ཉེ་བར་བཟུང་ནས་རིང་པོ་དང་། ཐུང་ངུ་བཞིན་དུའམ། མར་མེའི་འོད་བཞིན་དུ་བསྟན༌[^293]ཏེ་གྱུར་པ་དེ་ལས་གཞན་དུ་མ་ཡིན་ཏེ། དེ་ལྟར་ན་ཉེ་བར་བཟུང་བའམ་བརྟེན་པར་ཟད་དོ། །

[Block 457]
དོན་རྟོགས་ཞེས་བྱ་བ་ཇི་ལྟ་བུ་ཞེ་ན། འབྲས་བུ་རྣམས་ཀྱི་མཐའ་མེད་པའི་ཕྱིར་དང་། འབྲས་བུ་རེ་རེའི་རྐྱེན་ཀྱང་དུ་མ་ཡོད་པའི་ཕྱིར་དང་། རྐྱེན་རེ་རེ་ལ་ཡང་བརྟགས་ན་ཐོག་མ་མེད་པའི་འཁོར་བ་བཞིན་དུ་རྒྱུའི་ཚོགས་པ་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་མཐའ་མི་མཐོང་བའི་ཕྱིར་འབྲས་བུའི་རྩོམ་པ་ལ་འཇིག༌[^294]པར་ལྟ་བས་རྒྱུའི་ཚོགས་པ་གཅིག༌[^295]བརྒྱུད་པས་བསྒྲུབས་པའི་འབྲས་བུ་རྐྱེན་དུ་མ་ལས་བྱུང་བ་གྲུབ་མ་ཐག་ཏུ་འཇིག་པར་རྟོགས་ཤིང་། སྐྱེ་བ་ནི་ཤིན་ཏུ་འབད་པས་བསྒྲུབ་པར་བྱ་བ་ཡིན་ལ། ཤིན་ཏུ་འབད་པས་བསྒྲུབས་པ་འཇིག་པ་ནི་འབད་པ་མེད་པར་ཡང་འབྱུང་བར་རྟོགས་ནས་འདུས་བྱས་ཀྱི་ཆོས་ཉིད་ལ་སྒྱིད་ལུག་པ། བྱིས་པ་སྐྱེ་བོའི་སྤྱོད་པ་ལ་མངོན་པར་མི་བསྟོད་པ། སྐྱེ་བ་ལ་མངོན་པར་མི་དགའ་བ། འཇིག་པ་ལ་མི་འཕྲོད་པར་འཛིན་པ། འཁོར་བ་རྣམས་ལ་ཆགས་པ་འདོར་བར་འདོད་པ། འཁོར་བ་སྤོང་བར་འདོད་པ། བདག་ལ་ཆགས་པ་ལྷོད་པར་གྱུར་པས་དེ་ལྟར་དོན་ཁོང་དུ་ཆུད་པ་ལ་དེའི་འོག་ཏུ་དབེན་པ་ནི་རིགས་ཀྱི་སྔ་རོལ་དུ༌[^296]ནི་མ་ཡིན་ནོ། །

[Block 458]
དེ་ལྟར་བྱས་ན་སློབ་དཔོན་གྱིས་སྟོང་པ་ཉིད་བསྟན་པ་ཡང་འབྲས་བུ་མེད་པར་མི་འགྱུར། སློབ་མ་རྣམས་ཀྱང་སྤོང་བ་དང་། ཕྱིན་ཅི་ལོག་ཏུ་འཛིན་པས་ལོག་པར་ལྟུང་བར་མི་འགྱུར་རོ། །

[Block 459]
དེ་ལྟར་མ་བྱས་ན་ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདེན་པ་གཉིས་རྣམ་པར་གནས་པ་དང་། མི་མཐུན་པར་གྱུར་པའི་ཕྱིར་སྟོང་པ་ཉིད་བསྟན་པས་ལོག་པར་ལྟུང་བར་འགྱུར་རོ། །

[Block 460]
དེ་ལྟར་གྱུར་ན་མི་དགེ་བ་སྤང༌[^297]མི་ནུས་སོ། །
--- END BLOCKS ---
