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
[Block 451]
ཕྱིའི་དྲུག་པོ་དག་ནི་དོན་ཡོངས་སུ་སྤྱོད་པའི་ཉེ་བར་སྤྱོད་པའི་སྐྱེ་བའི་སྒོའི་ཕྱིར་རོ། །

[Block 452]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་ནི།

[Block 453 [VERSE]]
རྒྱུ་དང་འབྲས་བུ་རྩོལ་བ་ལ། །
སྒྲོ་འདོགས་མེད་ཅིང་སྐུར་འདེབས་མེད། །

[Block 454]
རྒྱུ་དང་འབྲས་བུ་དང་བྱེད་པ་རྣམས་ལ་སྒྲོ་འདོགས་པ་མེད་པ་དང་། སྐུར་པ་འདེབས་པ་མེད་པའི་དོན་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་དོན་ཏོ།[^177] །དེ་ལ་རྒྱུ་ལ་སྒྲོ་འདོགས་པ་ནི་འདུ་བྱེད་ལ་སོགས་པའི་མི་མཐུན་པའི་རྒྱུ་ལ་རྟོག་པའི་ཕྱིར་རོ། །

[Block 455]
རྒྱུ་ལ་སྐུར་པ་འདེབས་པ་ནི་རྒྱུ་མེད་པ་ཅན་དུ་རྟོག་པའི་ཕྱིར་རོ། །

[Block 456]
འབྲས་བུ་ལ་སྒྲོ་འདོགས་པ་ནི་བདག་དང་བཅས་པའི་འདུ་བྱེད་ལ་སོགས་པ་ནི་མ་རིག་པ་ལ་སོགས་པའི་རྐྱེན་ལས་འབྱུང་བར་རྟོག་པའི་ཕྱིར་རོ། །

[Block 457]
འབྲས་བུ་ལ་སྐུར་པ་འདེབས་པ་ནི་འདུ་བྱེད་ལ་སོགས་པ་མ་རིག་པ་ལ་སོགས་པའི་རྐྱེན་གྱིས་འབྱུང་བ་མེད་པར་རྟོག་པའི་ཕྱིར་རོ། །

[Block 458]
བྱེད་པ་ལ་སྒྲོ་འདོགས་པ་ནི་འདུ་བྱེད་ལ་སོགས་པ་སྐྱེ་བ་ལ་མ་རིག་པ་ལ་སོགས་པ་ལ་བྱེད་པར་རྟོག་པའི་ཕྱིར་རོ། །

[Block 459]
བྱེད་པ་ལ་སྐུར་པ་འདེབས་པ་ནི་ནུས་པ་མེད་པར་རྟོག་པའི་ཕྱིར་རོ། །

[Block 460]
དེ་མེད་པའི་ཕྱིར་སྒྲོ་འདོགས་པ་མེད་པ་དང་། སྐུར་པ་འདེབས་པ་མེད་པར་རིག་པར་བྱའོ། །

[Block 461 [VERSE]]
མི་འདོད་འདོད་དང་རྣམ་དག་དང་། །
མཉམ་དུ་འབྱུང་དང་དབང་བྱེད་དང་། །
འཐོབ་དང་ཀུན་ཏུ་སྤྱོད་པ་དག །
གཞན་དབང་ཉིད་ཀྱི་དོན་ཏེ་གཞན། །

[Block 462]
གནས་དང་གནས་མ་ཡིན་པ་ནི་གཞན་གྱི་དབང་ཉིད་རྣམ་པ་བདུན་གྱི་དོན་གྱིས་རིག་པར་བྱ་སྟེ། དེ་ལ་མི་འདོད་པ་གཞན་གྱི་དབང་ཉིད་ནི་ཉེས་པར་སྤྱོད་པས་མི་འདོད་བཞིན་དུ་ཡང་ངན་འགྲོར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 463]
འདོད་པ་གཞན་གྱི༌[^178]དབང་ཉིད་ནི་ལེགས་པར་སྤྱོད་པས་བདེ་འགྲོར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 464]
རྣམ་པར་དག་པ་གཞན་གྱི་དབང་ཉིད་ནི་སྒྲིབ་པ་ལྔ་མ་སྤངས་ལ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན་གྱི་བར་དུ་མ་བསྒོམས་ན་སྡུག་བསྔལ་གྱི་མཐར་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 465]
མཉམ་དུ་འབྱུང་བ་གཞན་གྱི་དབང་ཉིད་ནི། དེ་བཞིན་གཤེགས་པ་དང་། འཁོར་ལོས་སྒྱུར་བ་གཉིས་གཉིས་སྔ་ཕྱི་མེད་པར་འཇིག་རྟེན་གྱི་ཁམས་གཅིག་ཏུ་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 466]
དབང་དུ་བྱེད་པ་གཞན་གྱི༌[^179]དབང་ཉིད་ནི། བུད་མེད་འཁོར་ལོས་སྒྱུར་བ་ལ་སོགས་པ་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 467]
འཐོབ་པ་གཞན་གྱི་དབང་ཉིད་ནི་བུད་མེད་ཀྱིས་རང་བྱང་ཆུབ་དང་། བླ་ན་མེད་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 468]
ཀུན་ཏུ་སྤྱོད་པ་གཞན་གྱི་དབང་ཉིད་ནི། ལྟ་བ་ཕུན་སུམ་ཚོགས་པ་བསོད་པ༌[^180]ལ་སོགས་པ་ཀུན་ཏུ་མི་སྤྱོད་པས་སོ། །

[Block 469]
སོ་སོའི་སྐྱེ་བོ་ནི་ཀུན་ཏུ་སྤྱོད་པའི་ཕྱིར་ཏེ། རྒྱ་ཆེར་ནི་ཁམས་མང་པོ་ཅན་གྱི་མདོ་ལས་འབྱུང་བ་བཞིན་དུ་ཁོང་དུ་ཆུད་པར་བྱའོ།[^181] །དབང་པོ་ནི་རྣམ་པ་ཉི་ཤུ་རྩ་གཉིས་ཏེ།

[Block 470 [VERSE]]
འཛིན་དང་གནས་དང་རྒྱུན་མི་འཆད། །
སྤྱོད་དང་དག་པ་གཉིས་ཀྱི་ཕྱིར། །

[Block 471]
འཛིན་པའི་ཕྱིར་ནས་རྣམ་པར་དག་པ་གཉིས་ཀྱི་བར་དུ་སྟེ། དེ་དག་ལ་དེ་དབང་བྱེད་པའི་ཕྱིར་རོ། །

[Block 472]
གཟུགས་ལ་སོགས་པ་ཡུལ་འཛིན་པ་ལ་ནི་མིག་ལ་སོགས་པ་དྲུག་པོ་དག་དབང་བྱེད་དོ། །

[Block 473]
གནས་པར་བྱ་བ་ལ་ནི་སྲོག་གི་དབང་པོ་དབང་བྱེད་དེ། [^182]དེའི་དབང་གིས་མི་འཆི་བའི་ཕྱིར་རོ། །

[Block 474]
རིགས་འཚོབ་པ༌[^183]ལ་ནི་ཕོ་དང་མོའི་དབང་པོ་གཉིས་དབང་བྱེད་དེ། བུ་འབྱུང་བར་དབང་བྱེད་པའི་ཕྱིར་རོ། །

[Block 475]
ཉེ་བར་སྤྱོད་པ་ལ་ནི་ཚོར་བའི་དབང་པོ་རྣམས་ཏེ། དགེ་བ་དང་མི་དགེ་བའི་ལས་ཀྱི་འབྲས་བུ་ལ་ཉེ་བར་སྤྱོད་པའི་ཕྱིར་རོ། །

[Block 476]
འཇིག་རྟེན་པའི༌[^184]རྣམ་པར་དག་པ་ནི་དད་པ་ལ་སོགས་པའོ། །

[Block 477]
འཇིག་རྟེན་ལས་འདས་པའི་རྣམ་པར་དག་པ་ནི་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ལ་སོགས་པའོ། །

[Block 478 [VERSE]]
འབྲས་བུ་རྒྱུ་རྣམས་སྤྱད་ཟིན་དང་། །
དེ་བཞིན་མ་སྤྱད་གཞན་ཡིན་ནོ། །

[Block 479]
གཞན་གང་ཞེ་ན། དུས་གསུམ་མོ། །

[Block 480]
ཅི་རིགས་སུ་སྦྱར་ཏེ། འབྲས་བུ་དང་རྒྱུ་སྤྱད་ཟིན་པའི་ཕྱིར་འདས་པའི་དུས་སོ། །

[Block 481]
འབྲས་བུ་དང་རྒྱུ་མ་སྤྱད་པའི་ཕྱིར་མ་འོངས་པའི་དུས་སོ། །

[Block 482]
རྒྱུ་སྤྱད་པ་ལ་འབྲས་བུ་མ་སྤྱད་པའི་ཕྱིར་ད་ལྟར་འབྱུང་བའི་དུས་སུ་རིག་པར་བྱའོ། །

[Block 483 [VERSE]]
ཚོར་བ་རྒྱུ་དང་བཅས་པའི་དོན། །
དེ་ཡི་རྒྱུ་ནི་སྒྲུབ་པ་ཡིན། །
དེ་ཞི་བ༌[^185]དང་གཉེན་པོའི་དོན། །
ལྡན་པའི་ཕྱིར་ན་གཞན་དུ་འདོད། །

[Block 484]
བདེན་པ་བཞི་པོ་དེ་ལ་སྡུག་བསྔལ་གྱི་བདེན་པ་ནི་ཚོར་བ་རྒྱུ་དང་བཅས་པའི་དོན་ཏེ། གང་ཅི་ཚོར་ཡང་རུང་དེ་ནི་འདིར་སྡུག་བསྔལ་ལོ་ཞེས་བྱ་བའི་ཕྱིར་རོ། །

[Block 485]
ཚོར་བའི་རྒྱུ་ནི་ཚོར་བའི་གནས་ཀྱི་ཆོས་རྣམས་སུ་རིག་པར་བྱའོ། །

[Block 486 [VERSE]]
དེ་ཡི་རྒྱུ་ནི་སྒྲུབ་པ་ཡིན། །
ཀུན་འབྱུང་བ་ཡི་བདེན་པ་སྟེ། །

[Block 487]
སྡུག་བསྔལ་གྱི་རྒྱུ་ནི་སྒྲུབ་པ་གང་ཡིན་པའོ། །

[Block 488]
དེ་གཉིས་ཞི་བའི་ཕྱིར་འགོག་པའི་བདེན་པའོ། །

[Block 489 [VERSE]]
གཉེན་པོའི་ཕྱིར་ལམ་གྱི་བདེན་པའོ། །
ཡོན་ཏན་སྐྱོན་དང་རྣམ་མི་རྟོག །
ཤེས་པས་གཞན་ལས་བདག་གིས་ནི། །
ངེས་པར་འབྱུང་ཕྱིར་གཞན་ཞེས་བྱ། །

[Block 490]
ཐེག་པ་གསུམ་སྟེ་ཅི་རིགས་སུ་སྦྱར་བར་བྱའོ། །

[Block 491]
དེ་ལ༌[^186]མྱ་ངན་ལས་འདས་པ་དང་། འཁོར་བ་ལ་ཡོན་ཏན༌[^187]སྐྱོན་དུ་ཤེས་ཤིང་གཞན་ལས་ཐོས་ནས་ངེས་པར་འབྱུང་བའི་ཕྱིར་ཉན་ཐོས་ཀྱི་ཐེག་པའོ། །

[Block 492]
གཞན་ལས་མ་ཐོས་པར་དེ་ཉིད་ཀྱིས་བདག་གིས་ངེས་པར་འབྱུང་བའི་ཕྱིར། རང་སངས་རྒྱས་ཀྱི་ཐེག་པའོ། །

[Block 493]
བདག་གིས་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱིས་ངེས་པར་འབྱུང་བའི་ཕྱིར་ཐེག་པ་ཆེན་པོར་རིག་པར་བྱའོ། །

[Block 494 [VERSE]]
བཏགས༌[^188]བཅས་རྒྱུར་བཅས་རྒྱུ་མཚན་དང་། །
རབ་ཏུ་ཞི་བའི་དོན་བཅས་ནི། །
ཐ་མ་ཉིད་དུ་བཤད་པ་ཡིན། །
འདུས་བྱས་དང་འདུས་མ་བྱས་སོ། །

[Block 495]
དེ་ལ་བཏགས་པ་ནི་མིང་གི་ཚོགས་ལ་སོགས་པའོ། །

[Block 496]
རྒྱུ་ནི་ས་བོན་དུ་བསྡུས་པའི་ཀུན་གཞི་རྣམ་པར་ཤེས་པའོ། །

[Block 497]
རྒྱུ་མཚན་ནི་གནས་དང་ལུས་དང༌[^189]ལོངས་སྤྱོད་དུ་བསྡུས་པ་དང་། འཇུག་པའི་རྣམ་པར་ཤེས་པར་བསྡུས་པ་ཡིད་དང་། འཛིན་པ་དང་། རྣམ་པར་རྟོག་པ་སྟེ། བཏགས་པ༌[^190]དང་བཅས་ཤིང་རྒྱུ་དང་བཅས་པའི་རྒྱུ་མཚན་མཚུངས་པར་ལྡན་པ་དང་བཅས་པ་འདི་ནི་འདུས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 498]
དེ་ལ་ཡིད་ནི་གང་རྟག་ཏུ་རློམ་སེམས་པ་ནི་རྣམ་པའོ། །

[Block 499]
འཛིན་པ་ནི་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔའོ། །

[Block 500]
རྣམ་པར་རྟོག་པ་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་སྟེ། དེ་ནི་རྣམ་པར་རྟོག་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 501]
འདུས་མ་བྱས་ནི་རབ་ཏུ་ཞི་བ་འགོག་པ་དང་། རབ་ཏུ་ཞི་བའི་དོན་དེ་བཞིན་ཉིད་དེ་ལམ་གྱི་དམིགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 502]
ལམ་ཡང་རབ་ཏུ་ཞི་བ་ཉིད་དོ། །

[Block 503]
དེས་རབ་ཏུ་ཞི་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 504]
དེ་ལྟར་དོན༌[^191]འདིས་ཕུང་པོ་ལ་སོགས་པ་ཤེས་པ་ནི་ཕུང་པོ་ལ་སོགས་པ་ལ་མཁས་པར་རིག་པར་བྱའོ། །

[Block 505]
དེ༌[^192]ཁོ་ནའི་དོན་བསྡུས་པ་ནི་མདོར་བསྡུ་ན་དེ་ཁོ་ན་རྣམ་པ་གཉིས་ཏེ། མེ་ལོང་ལྟ་བུའི་དེ་ཁོ་ན་དང་། སྣང་བའི་དེ་ཁོ་ནའོ། །

[Block 506]
དེ་ལ་མེ་ལོང་ལྟ་བུའི་དེ་ཁོ་ན་ནི་རྩ་བའི་དེ་ཁོ་ན་སྟེ། ལྷག་མ་རྣམས་དེར་སྣང་བའི་ཕྱིར་རོ། །

[Block 507]
སྣང་བའི་དེ་ཁོ་ན་ནི་རྣམ་པ་དགུ་སྟེ། ང་རྒྱལ་མེད་པའི་སྣང་བའི་དེ་ཁོ་ན་དང་། ཕྱིན་ཅི་ལོག་གི་གཉེན་པོའི་སྣང་བའི༌[^193]དེ་ཁོ་ན་དང་། ཉན་ཐོས་ཀྱི་ཐེག་པས༌[^194]ངེས་པར་འབྱུང་བ་སྣང་བའི་དེ་ཁོ་ན་དང་། རགས་པས་ཡོངས་སུ་སྨིན་པར་བྱེད་ཅིང་ཕྲ་བས་རྣམ་པར་གྲོལ་བར་བྱེད་པའི་ཕྱིར་ཐེག་པ་ཆེན་པོས་ངེས་པར་འབྱུང་བ་སྣང་བའི་དེ་ཁོ་ན་དང་། དཔེ་ལ་བརྟེན་ཏེ་རིགས་པས་ཚར་གཅོད་པའི་ཕྱིར་ཕས་ཀྱི༌[^195]རྒོལ་བ་ཚར་གཅོད་པ་སྣང་བའི་དེ་ཁོ་ན་དང་། ཐེག་པ་ཆེན་པོ་མངོན་པར་བརྗོད་པ༌[^196]སྣང་བའི་དེ་ཁོ་ན་དང་། ཤེས་བྱའི་རྣམ་པ་ཐམས་ཅད་ལ་འཇུག་པ་སྣང་བའི་དེ་ཁོ་ན་དང་། མ་ནོར་བའི་དེ་བཞིན་ཉིད་མངོན་པར་བརྗོད་པ་སྣང་བའི་དེ་ཁོ་ན་དང་། བདག་ཏུ་འཛིན་པའི་གཞི་ལ་དགོངས་པ་ཐམས་ཅད་རྟོགས་པ་སྣང་བའི་དེ་ཁོ་ནའོ། །

[Block 508]
བསྟན་བཅོས་དབུས་དང་མཐའ་རྣམ་པར་འབྱེད་པ་ལས་དེ་ཁོ་ན་ཞེས་བྱ་བའི་ལེའུར་བཅད་པ་གསུམ་པའི་འགྲེལ་པའོ།། །།

[Block 509]
བསྟན་བཅོས་དབུས་དང་མཐའ་རྣམ་པར་འབྱེད་པའི་འགྲེལ་པ། བམ་པོ་གཉིས་པ་སྟེ་ཐ་མ།[^197] །

[Block 510 [HEADING]]
## གཉེན་པོ་བསྒོམ་པ། ^4-0

[Block 511]
གཉེན་པོ་བསྒོམ་པ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་བསྒོམ་པ་སྟེ། དེ་ད་བརྗོད་པར་བྱའོ། །

[Block 512]
དེ་ལ་རེ་ཞིག་དང་པོར།

[Block 513 [VERSE]]
གནས་ངན་ལེན་ཕྱིར་སྲེད༌[^198]རྒྱུའི་ཕྱིར། །
གཞི་ཡི་ཕྱིར་དང་མ་རྨོངས་ཕྱིར། །
བདེན་པ་བཞི་ལ་འཇུག་བྱ་བས། །
དྲན་པ་ཉེ་བར་གཞག་པ་བསྒོམ། །

[Block 514]
ལུས་ཀྱིས་ནི་གནས་ངན་ལེན་རབ་ཏུ་སྟོན་ཏེ། དེ་ཡང་ཡོངས་སུ་བརྟགས་པས་སྡུག་བསྔལ་གྱི་བདེན་པ་ལ་འཇུག་གོ། །

[Block 515]
དེའི་མཚན་ཉིད་ནི་གནས་ངན་ལེན་དང་བཅས་པའི་འདུ་བྱེད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 516]
གནས་ངན་ལེན་ནི་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་ཉིད་དེ་དེས་ཟག་པ་དང་བཅས་པའི་དངོས་པོ་ཐམས་ཅད་འཕགས་པས་སྡུག་བསྔལ་དུ་གཟིགས་སོ། །

[Block 517]
སྲེད་པའི་རྒྱུ་ནི༌[^199]ཚོར་བ་སྟེ། དེ་ལ་ཡོངས་སུ་བརྟགས་པས་ཀུན་འབྱུང་གི་བདེན་པ་ལ་འཇུག་གོ། །

[Block 518]
བདག་ཏུ་མངོན་པར་ཞེན་པའི་གཞི་ནི་སེམས་ཏེ། དེ་ལ་ཡོངས་སུ་བརྟགས་པས་འགོག་པའི་བདེན་པ་ལ་འཇུག་སྟེ། བདག་ཆད་པར་དོགས་པའི་འཇིགས་པ༌[^200]མེད་པའི་ཕྱིར་རོ། །

[Block 519]
ཆོས་ལ་ཡོངས་སུ་བརྟགས་པས་ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བའི་ཆོས་ལ་རྨོངས་པ་མེད་པའི་ཕྱིར་ལམ་གྱི་བདེན་པ་ལ་འཇུག་གོ། །

[Block 520]
དེ་བས་ན་བདེན་པ་བཞི་ལ་འཇུག་པར་བྱ་བའི་ཕྱིར་ཐོག་མར་དྲན་པ་ཉེ་བར་གཞག་པ་བསྒོམ་པ་རྣམ་པར་གཞག་གོ། །

[Block 521]
དེའི་འོག་ཏུ་ཡང་དག་པར་སྤོང་བ་བསྒོམ་པ་སྟེ། འདི་ལྟར། མི་མཐུན་ཕྱོགས་དང་གཉེན་པོ་རྣམས། །རྣམ་པ་ཐམས་ཅད་ཡོངས་ཤེས་ན།[^201] །

[Block 522 [VERSE]]
དེ་དག་སྤང་ཕྱིར་བརྩོན་འགྲུས་ནི། །
རྣམ་པ་བཞི་དག་རབ་ཏུ་འབྱུང་། །

[Block 523]
དྲན་པ་ཉེ་བར་གཞག་པ་བསྒོམས་པས་མི་མཐུན་པའི་ཕྱོགས་དང་གཉེན་པོ་རྣམ་པ༌[^202]ཐམས་ཅད་དུ་ཡོངས་སུ་ཤེས་ན།[^203] མི་མཐུན་པའི་ཕྱོགས་གསལ༌[^204]ཞིང་གཉེན་པོ་བསྐྱེད་པའི་ཕྱིར་བརྩོན་འགྲུས་རྣམ་པ་བཞི་རབ་ཏུ་འབྱུང་སྟེ། སྡིག་པ་མི་དགེ་བའི་ཆོས་སྐྱེས་པ༌[^205]རྣམས་སྤང་བའི་ཕྱིར་ཞེས་རྒྱ་ཆེར་འབྱུང་བའོ། །

[Block 524 [VERSE]]
དེར༌[^206]གནས་ལས་སུ་རུང་བ་ཉིད། །
དོན་རྣམས་ཐམས་ཅད་འབྱོར་པར་འགྱུར། །
ཉེས་པ་ལྔ་སྤོང་འདུ་བྱེད་བརྒྱད། །
བརྟེན་པའི་རྒྱུ་ལས༌[^207]བྱུང་བའོ། །

[Block 525]
དེ་སྤང་བའི༌[^208]ཕྱིར་བརྩོན་འགྲུས་རྩོམ་པ་དེ་ལ་སེམས་གནས་པའི་ལས་སུ་རུང་བ་ཉིད་ནི་རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་པོ་དག་སྟེ། དོན་ཐམས་ཅད་འབྱོར་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
