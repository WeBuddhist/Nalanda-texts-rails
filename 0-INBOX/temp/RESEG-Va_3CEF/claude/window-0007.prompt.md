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
[Block 526]
གནས་པ་ནི་འདིར་སེམས་གནས་པ་སྟེ་ཏིང་ངེ་འཛིན་དུ་རིག་པར་བྱའོ། །

[Block 527]
དེའི་ཕྱིར་ཡང་དག་པར་སྤོང་བའི་འོག་ཏུ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་སོ། །

[Block 528]
ལས་སུ་རུང་བ་དེ་ཡང་ཉེས་པ་ལྔ་སྤང་བའི་ཕྱིར་སྤོང་བའི་འདུ་བྱེད་བརྒྱད་བསྒོམ་པའི༌[^209]རྒྱུ་ལས་བྱུང་བར་རིག་པར་བྱའོ། །

[Block 529]
ཉེས་པ་ལྔ་པོ་དེ་དག་གང་ཞེ་ན། གསུངས་པ།

[Block 530 [VERSE]]
ལེ་ལོ་དང་ནི་གདམས་ངག་རྣམས། །
བརྗེད་དང་བྱིང་དང་རྒོད་པ་དང་། །

[Block 531]
འདུ་མི་བྱེད་དང་འདུ་བྱེད་དེ།[^210] །འདི་དག་ཉེས་པ་ལྔར་འདོད་དོ།[^211] །དེ་ལ་བྱིང་བ་དང་རྒོད་པ་ནི་ཉེས་པ་གཅིག་ཏུ་བསྡུའོ། །

[Block 532]
བྱིང་བ་དང་རྒོད་པ་རབ་ཏུ་ཞི་བར་བྱ་བའི་དུས་ན་མངོན་པར་འདུ་མི་བྱེད་ན་ཉེས་པའོ། །

[Block 533]
རབ་ཏུ་ཞི་བའི་ཚེ་ནི་མངོན་པར་འདུ་བྱེད་པའོ། །

[Block 534]
དེ་དག་སྤང་བའི༌[^212]ཕྱིར་སྤོང་བའི་འདུ་བྱེད་བརྒྱད་ཇི་ལྟར་རྣམ་པར་གཞག་ཅེ་ན། ལེ་ལོ་སྤང་བའི་ཕྱིར་བཞི་སྟེ། འདུན་པ་དང་། རྩོལ་བ་དང་། དད་པ་དང་། ཤིན་ཏུ་སྦྱངས་པའོ། །

[Block 535]
དེ་དག་ཀྱང་གོ་རིམས་བཞིན་དུ་རིག་པར་བྱ་སྟེ།

[Block 536 [VERSE]]
གནས་དང་དེ་ལ་གནས་པ་དང་། །
རྒྱུ་དང་འབྲས་བུ་ཉིད་དུའོ། །
རྩོལ་བའི་གནས་ནི་འདུན་པའོ། །

[Block 537]
གནས་པ་ནི་རྩོལ་བའོ། །

[Block 538]
གནས་འདུན་པ་དེའི་རྒྱུ་ནི་དད་པ་སྟེ། ཡིད་ཆེས་པར་གྱུར་ན་མངོན་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 539]
གནས་རྩོལ་བ་དེའི་འབྲས་བུ་ནི་ཤིན་ཏུ་སྦྱངས་པ་སྟེ། བརྩོན་འགྲུས་བརྩམས་པས་ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 540]
སྤོང་བའི་འདུ་བྱེད་ལྷག་མ་བཞི་ནི་དྲན་པ་དང་། ཤེས་བཞིན་དང་། སེམས་པ་དང་། བཏང་སྙོམས་ཏེ་ཉེས་པ་བཞིའི་གཉེན་པོར་གྲངས་བཞིན་ནོ། །

[Block 541]
དེ་དག་ཀྱང་དྲན་པ་ལ་སོགས་པར་རིག་པར་བྱ་སྟེ་གོ་རིམས་བཞིན་ནོ། །

[Block 542 [VERSE]]
དམིགས་པ་བརྗེད་པར་མ་གྱུར་དང་། །
བྱིང་དང་རྒོད་པ་རྟོགས་པ་དང་། །
དེ་སྤོང༌[^213]མངོན་པར་འདུ་བྱེད་དང་། །
ཞི་ཚེ་རྣལ་དུ་འཇུག་པའོ། །

[Block 543]
དྲན་པ་ནི་དམིགས་པ་མ་བརྗེད་པའོ། །ཤེས་བཞིན་ནི་དྲན་པ་མ་བརྗེད་པར་གྱུར་ན་བྱིང་བ་དང་རྒོད་པ་རྟོགས་པའོ། །

[Block 544]
རྟོགས་ནས་དེ་དང་འབྲལ་བའི་ཕྱིར་མངོན་པར་འདུ་བྱེད་པ་ནི་སེམས་པའོ། །

[Block 545]
བྱིང་བ་དང་རྒོད་པ་དེ་ཉེ་བར་ཞི་བར་གྱུར་པ་ན་རྣལ་དུ་འཇུག་པ་ནི་སེམས་བཏང་སྙོམས་སུ་བྱེད་པའོ། །

[Block 546]
རྫུ་འཕྲུལ་གྱི་རྐང་པའི་འོག་ཏུ་དབང་པོ་རྣམས་ཏེ་དད་པ་ལ་སོགས་པའོ། །

[Block 547]
དེ་དག་ལས་ཇི་ལྟར་རྣམ་པར་གཞག་ཅེ་ན། ཐར་པའི་ཆ་དང་མཐུན་བསྐྱེད་ནས། །འདུན་དང་སྦྱོར་བ་དབང་བྱེད་དང་།[^214] །

[Block 548 [VERSE]]
དམིགས་པ་བརྗེད་པར་མ་གྱུར་དང་། །
མི་འཕྲོ་རྣམ་པར་འབྱེད་ཀྱང་ངོ་། །
དབང་བྱེད་པ་ཞེས་བྱ་བར་སྙེགས༌[^215]སོ། །

[Block 549]
རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་ཀྱི་སེམས་ལས་སུ་རུང་བ་དང་། ཐར་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་བསྐྱེད་ནས། འདུན་པ་ནི་དབང་བྱེད་པ། སྦྱོར་བ་ནི་དབང་བྱེད་པ། དམིགས་པ་མ་བརྗེད་པ་ནི་དབང་བྱེད་པ། མི་འཕྲོ་བ་ནི་དབང་བྱེད་པ། །རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ནི་དབང་བྱེད་པ་སྟེ། དད་པ་ལ་སོགས་པ་དབང་པོ་ལྔ་དག་དང་གོ་རིམས་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 550]
དད་པ་ལ་སོགས་པ་དེ་དག་ཉིད་སྟོབས་དང་ལྡན་པར་འགྱུར་བ་ལ་སྟོབས་རྣམས་ཞེས་བྱ་སྟེ། དེ་དག་མི་མཐུན་ཕྱོགས་ནི་སྲབ་པའི༌[^216]ཕྱིར། [^217]སྟོབས་ལྡན་གང་གི་ཚེ་དེ་དག་ཉིད་མ་དད་པ་ལ་སོགས་པ་མི་མཐུན་པའི་ཕྱོགས་དང་མི་འདྲེ་བ་ནའོ། །ཅིའི་ཕྱིར་དད་པ་ལ་སོགས་པ༌[^218]སྔ་ཕྱིར་བསྟན་ཞེ་ན། འདི་ལྟར་སྔ་མའི་འབྲས་བུ་ཕྱི་མ་ཡིན། རྒྱུ་དང་འབྲས་བུ་ལ་དད༌[^219]པར་གྱུར་པའི་རྒྱུས༌[^220]འབྲས་བུ་ལ་བརྩོན་འགྲུས་རྩོམ་མོ། །

[Block 551]
བརྩོན་འགྲུས་བརྩམས་པས༌[^221]ནི་དྲན་པ་ཉེ་བར་གནས་སོ། །

[Block 552]
དྲན་པ་ཉེ་བར་གནས་པས༌[^222]ནི་སེམས་མཉམ་པར་འཇོག་གོ། །

[Block 553]
སེམས་མཉམ་པར་གཞག་པས༌[^223]ནི་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ། །

[Block 554]
ཐར་པའི་ཆ་དང་མཐུན་པ་བསྐྱེད་ཟིན་ནས་དབང་པོ་རྣམས་བསྟན་ན། ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་ཅི་དབང་པོའི་དུས་ལ་རིག་པར་བྱའམ། འོན་ཏེ་སྟོབས་ཀྱི་དུས་ལ་རིག་པར་བྱ་ཞེ་ན།

[Block 555 [VERSE]]
དབང་པོ་རྣམས་དང་སྟོབས་རྣམས་ལ། །
ངེས་འབྱེད་ཆ་མཐུན་གཉིས་གཉིས་སོ། །

[Block 556]
དྲོ་བར་གྱུར་པ་རྣམས་དང་རྩེ་མོ་དག་གི་ཚེ༌[^224]ནི་དབང་པོ་རྣམས་སོ། །

[Block 557]
བཟོད་པ་དག་དང་འཇིག་རྟེན་པའི་ཆོས་ཀྱི་མཆོག་རྣམས་ཀྱི་ཚེ་ནི་སྟོབས་རྣམས་སོ། །

[Block 558]
སྟོབས་ཀྱི་འོག་ཏུ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་རྣམས་ཏེ། དེ་དག་ཇི་ལྟར་རྣམ་པར་གཞག་ཅེ་ན།

[Block 559 [VERSE]]
རང་བཞིན་ཡན་ལག་གནས་ཡན་ལག །
གསུམ་པ་ངེས་འབྱུང་ཡན་ལག་སྟེ། །
བཞི་པ་ཕན་ཡོན་ཡན་ལག་ཡིན། །
རྣམ་གསུམ་ཉོན་མོངས་མེད་ཡན་ལག །

[Block 560]
མཐོང་བའི་ལམ་ལ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཏུ༌[^225]གྱུར་པ་དག་ནི་བྱང་ཆུབ་ཀྱི་ཡན་ལག་རྣམས་སོ། །

[Block 561]
དེ་ལ་དྲན་པ་ནི་བྱང་ཆུབ་ཀྱི་གནས་ཀྱི་ཡན་ལག་གོ། །

[Block 562]
ཆོས་རྣམ་པར་འབྱེད་པ་ནི་རང་བཞིན་གྱི་ཡན་ལག་གོ།[^226] །བརྩོན་འགྲུས་ནི་ངེས་པར་འབྱུང་བའི་ཡན་ལག་གོ། །

[Block 563]
དགའ་བ་ནི་ཕན་ཡོན་གྱི་ཡན་ལག་གོ། །

[Block 564]
རྣམ་པ་གསུམ་ནི་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པའི་ཡན་ལག་སྟེ། ཤིན་ཏུ་སྦྱངས་པ་དང་། ཏིང་ངེ་འཛིན་དང་། བཏང་སྙོམས་སོ། །

[Block 565]
ཅིའི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པའི་ཡན་ལག་རྣམ་པ་གསུམ་དུ་བསྟན་ཞེ་ན།

[Block 566 [VERSE]]
འདི་ལ་གཞི་དང་གནས་དང་ནི། །
ངོ་བོ་ཉིད་དུ་བསྟན་པ་ཡིན། །

[Block 567]
ཀུན་ནས་ཉོན་མོངས་པ་ནི་གནས་ངན་ལེན་གྱི་རྒྱུ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 568]
ཤིན་ཏུ་སྦྱངས་པ་ནི་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པའི་གཞི་སྟེ། དེ་ནི་དེའི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 569]
ཏིང་ངེ་འཛིན་ནི་གནས་སོ། །

[Block 570]
བཏང་སྙོམས་ནི་ངོ་བོ་ཉིད་དོ། །

[Block 571]
བྱང་ཆུབ་ཀྱི་ཡན་ལག་གི་འོག་ཏུ་ལམ་གྱི་ཡན་ལག་རྣམས་ཏེ། དེ་དག་ཇི་ལྟར་རྣམ་པར་གཞག་ཅེ་ན།

[Block 572 [VERSE]]
ཡོངས་སུ་གཅོད་དང་གོ་བྱེད་དང་། །
རྣམ་གསུམ་གཞན་ཡིད་ཆེས་པར་བྱེད། །
མི་མཐུན་ཕྱོགས་ཀྱི་གཉེན་པོར་ནི། །
ལམ་གྱི་ཡན་ལག་དེ་བརྒྱད་དོ། །

[Block 573]
ཡང་དག་པའི་ལྟ་བ་ནི་བསྒོམ་པའི་ལམ་གྱི་ཚེ་མཐོང་བའི་ལམ་ལ་ཡོངས་སུ་གཅོད་པའི་ཡན་ལག་སྟེ། འཇིག་རྟེན་ལས་འདས་པའི་རྗེས་ལས་ཐོབ་པ་འཇིག་རྟེན་པ་དེས་རང་གི་རྟོགས་པ་ཡོངས་སུ་གཅོད་དོ། །

[Block 574]
ཡང་དག་པའི་རྟོག་པ་དང་། ཡང་དག་པའི་ངག་ནི་གཞན་གོ་བར་བྱེད་པའི་ཡན་ལག་སྟེ། ཀུན་སློང་བ་དང་བཅས་པས་ངག་གི༌[^227]དེ་གོ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 575]
གཞན་ཡིད་ཆེས་པར་བྱེད་པའི་ཡན་ལག་ནི་རྣམ་པ་གསུམ་སྟེ། ཡང་དག་པའི་ངག་དང་། ལས་ཀྱི་མཐའ་དང་། འཚོ་བའོ། །

[Block 576]
དེ་དག་ཀྱང་གོ་རིམས་བཞིན་དུ།

[Block 577 [VERSE]]
ལྟ་དང་ཚུལ་ཁྲིམས་ཡོ་བྱད་བསྙུངས། །
གཞན་ལ་རྣམ་པར་རིག་བྱེད་འདོད། །

[Block 578]
ཡང་དག་པའི་ངག་གིས་བསྙད་པ་དང་། འབྲེལ་པའི་གཏམ་རྣམ་པར་ངེས་པས་ཤེས་རབ་ལ་ཡིད་ཆེས་པར་འགྱུར་རོ། །

[Block 579]
ཡང་དག་པའི་ལས་ཀྱི་མཐའ་ནི་ཚུལ་ཁྲིམས་ལ་སྟེ། བྱ་བ་མ་ཡིན་པ་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 580]
ཡང་དག་པའི་འཚོ་བས་ནི་ཡོ་བྱད་བསྙུངས་པ་ལ་སྟེ། ཆོས་ཀྱིས་གས༌[^228]ལ་སོགས་པ་ཚོད་ཟིན་པར་ཚོལ་བའི་ཕྱིར་རོ། །

[Block 581]
མི་མཐུན་པའི་ཕྱོགས་ཀྱི་གཉེན་པོའི་ཡན་ལག་ནི་རྣམ་པ་གསུམ་སྟེ། ཡང་དག་པའི་རྩོལ་བ་དང་། དྲན་པ་དང་། ཏིང་ངེ་འཛིན་ཏོ། །

[Block 582]
དེ་དག་ནི་གོ་རིམས་བཞིན་དུ། ཉོན་མོངས་ཉེ་བའི་ཉོན་མོངས་དབང་། །མི་མཐུན་ཕྱོགས་ཀྱི་གཉེན་པོའོ།[^229] །མི་མཐུན་ཕྱོགས་ནི་རྣམ་པ་གསུམ་སྟེ། བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་དང་། ཉེ་བའི་ཉོན་མོངས་པ་བྱིང་བ་དང་། རྒོད་པའི་དབང་གིས༌[^230]མི་མཐུན་པའི་ཕྱོགས་ཏེ། ཡོན་ཏན་ཁྱད་པར་ཅན་མངོན་པར་སྒྲུབ་པའི་གེགས་སུ་གྱུར་པའོ། །

[Block 583]
དེ་ལ་དང་པོའི་གཉེན་པོ་ནི་ཡང་དག་པའི་རྩོལ་བ་སྟེ། དེས་ལམ་བསྒོམ་པའི་ཕྱིར་རོ། །

[Block 584]
གཉིས་པ་ནི་ཡང་དག་པའི་དྲན་པ་སྟེ། ཞི་གནས་ལ་སོགས་པའི་རྒྱུ་རྣམས་ལ་དྲན་པ་ཤིན་ཏུ་ཉེ་བར་གནས་པས་བྱིང་བ་དང་རྒོད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 585]
གསུམ་པ་ནི་ཡང་དག་པའི་ཏིང་ངེ་འཛིན་ཏེ། བསམ་གཏན་ལ་གནས་ནས་མངོན་པར་ཤེས་པ་ལ་སོགས་པ་ཡོན་ཏན་མངོན་པར་བསྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 586]
གཉེན་པོ་བསྒོམ་པ་དེ་མདོར་བསྡུ༌[^231]ན་རྣམ་པ་གསུམ་དུ་རིག་པར་བྱ་སྟེ།

[Block 587 [VERSE]]
རྗེས་སུ་མཐུན་ལ་ཕྱིན་ཅི་ལོག །
རྗེས་སུ་འབྲེལ་བཅས་བཟློག་པ་དང་། །
ཕྱིན་ཅི་མ་ལོག་ཕྱིན་ཅི་ལོག །
རྗེས་སུ་འབྲེལ་མེད་བསྒོམ་པའོ། །

[Block 588]
ཕྱིན་ཅི་མ་ལོག་པའི་རྗེས་སུ་མཐུན་ལ་ཕྱིན་ཅི་ལོག་པ་དང་། ཕྱིན་ཅི་ལོག་མེད་ལ་ཕྱིན་ཅི་ལོག་རྗེས་སུ་འབྲེལ་པ་དང་། ཕྱིན་ཅི་ལོག་ཀྱང་མེད་ལ་ཕྱིན་ཅི་ལོག་རྗེས་སུ་འབྲེལ་བ་ཡང་མེད་པ་སྟེ། སོ་སོའི༌[^232]སྐྱེ་བོ་དང་། སློབ་པ་དང་། མི་སློབ་པ་དང་། གོ་རིམས་བཞིན་ནོ། །

[Block 589]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ནི།[^233] །དམིགས༌[^234]དང་ཡིད་ལ་བྱེད་པ་དང་། །ཐོབ་པས་དེ་ནི༌[^235]ཁྱད་པར༌[^236]འཕགས་ཏེ། ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་ནི་རང་གི་རྒྱུད་དུ་གཏོགས་པའི་ལུས་ལ་སོགས་པ་ལ་དམིགས་སོ། །

[Block 590]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་བདག་དང་གཞན་གྱི་རྒྱུད་དུ་གཏོགས་པ་རྣམས་སོ། །

[Block 591]
ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་ནི་ལུས་ལ་སོགས་པ་མི་རྟག་པ་ལ་སོགས་པའི་རྣམ་པར་ཡིད་ལ་བྱེད་དོ། །

[Block 592]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་མི་དམིགས་པའི་ཚུལ་རྣམ་པར་ཡིད་ལ་བྱེད་དོ། །

[Block 593]
ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་ནི་ཅི་ནས་ཀྱང་ལུས་ལ་སོགས་པ་དང་བྲལ་བར་བྱ་བའི་ཕྱིར་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་བསྒོམ་མོ། །

[Block 594]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་འབྲལ་བར་བྱ་བའི་ཕྱིར་ཡང་མ་ཡིན། མི་འབྲལ་བར་བྱ་བའི་ཕྱིར་ཡང་མ་ཡིན་གྱི། [^237]ཅི་ནས་ཀྱང་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་ཕྱིར་བསྒོམ་མོ། །

[Block 595]
གཉེན་པོ་བསྒོམ་པ་བཤད་ཟིན་ཏོ། །

[Block 596 [HEADING]]
## གཉེན་པོ་བསྒོམ་པ་དེ་ཉིད་ཀྱི་གནས། ^5-0

[Block 597]
དེའི་གནས་གང་ཞེ་ན།

[Block 598 [VERSE]]
རྒྱུ་ཡི་གནས་དང་ཞུགས་པ་དང་། །
སྦྱོར་དང་འབྲས་བུ༌[^238]བརྗོད་པ་དང་། །
བྱ་དང་བྱ་མེད་ཁྱད་པར་དང་། །
དེ་ནི་བླ་མ་བླ་ན་མེད། །

[Block 599 [VERSE]]
མོས་པ་དང་ནི་འཇུག་པ་དང་། །
ངེས་པར་འབྱུང་དང་ལུང་བསྟན་དང་། །
བརྗོད་པ་དང་ནི་དབང་བསྐུར་དང་། །
ཕྱིན་པ་དང་ནི་ཕན་ཡོན་དང་། །

[Block 600]
བྱ་བ་བསྒྲུབ་པ༌[^239]བསྟན་པའོ། །

[Block 601]
དེ་ལ་རྒྱུའི་གནས་ནི་གང་རིགས་ལ་གནས་པའི་གང་ཟག་གོ། །

[Block 602]
ཞུགས་པའི་གནས་ནི་སེམས་བསྐྱེད་པའོ། །

[Block 603]
སྦྱོར་བའི་གནས་ནི་སེམས་བསྐྱེད་ནས་འབྲས་བུ་མ་ཐོབ་ཚུན་ཆད་དོ། །

[Block 604]
འབྲས་བུའི་གནས་ནི་ཐོབ༌[^240]པའོ། །

[Block 605]
བྱ་བ་བཅས་པའི་གནས་ནི་སློབ་པའོ། །
--- END BLOCKS ---
