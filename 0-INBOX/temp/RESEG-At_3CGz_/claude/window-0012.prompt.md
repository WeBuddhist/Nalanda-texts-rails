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
[Block 421 [VERSE]]
རྒྱལ་པོ་མཛོད་དང་ལམ་པོ་ཆེ། །
བཞོན་པ་བཀོད་མའི་ཆུ་དང་ནི། །
སྒྲ་སྙན་ཆུ་བོ་སྤྲིན་རྣམས་ཀྱིས། །
རྣམ་པ་ཉི་ཤུ་རྩ་གཉིས་སོ། །

[Block 422]
ཞེས་གསུངས་སོ། །

[Block 423]
དེ་ལ་གཉིས་ནི་རྒྱུའི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 424]
བཅུ་བདུན་ནི་ལམ་གྱི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 425]
གསུམ༌[^227]ནི་འབྲས་བུའི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 426]
གཉིས་ནི་སྨོན་པའི་སེམས་སོ། །

[Block 427]
ཉི་ཤུ་ནི་འཇུག་པའི་སེམས་སོ། །

[Block 428]
རྣམ་གྲངས་གཞན་ཡང་གསུམ་ནི་རྒྱུའི་དུས་ཀྱི་སེམས་སོ། །

[Block 429]
བཅུ་དྲུག་ནི་ལམ་གྱི་དུས་ཀྱི་སེམས་སོ། །

[Block 430]
ཐ་མ་གསུམ་ནི་འབྲས་བུའི་དུས་ཀྱི་སེམས་སོ། །

[Block 431]
དེ་དག་གི་དོན་རྒྱས་པ་ནི་མངོན་པར་རྟོགས་པའི་རྒྱན་དེ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 432]
དེ་ལྟར་བྱང་ཆུབ་ཀྱི་སེམས་རིན་པོ་ཆེ་དེ་ཁྱད་པར་དུ་སྤེལ་བར་བྱ་བའི་ཕྱིར། ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་ངེས་པར་བླང་བར་བྱའོ་ཞེས་བསྟན་ནས། ད་ནི་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པའི་རྟེན་ཁྱད་པར་ཅན་བསྟན་པར༌[^228]འདོད་ནས།

[Block 433 [VERSE]]
སོ་སོར༌[^229]ཐར་པ་རིས་བདུན་གྱི། །
རྟག་ཏུ་སྡོམ་གཞན་ལྡན་པ་དག །
བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ་ཡི། །
སྐལ་བ་ཡོད་ཀྱི་གཞན་དུ་མིན། །

[Block 434]
ཞེས་སྨྲས་ཏེ། འདིར་སྨྲས་པ། ཁྱོད་ཀྱིས་དང་པོར།

[Block 435 [VERSE]]
དེ་ནི་སྐྱེས་བུ་མཆོག་ཡིན་ནོ། །
སེམས་ཅན་དམ་པ་བྱང་ཆུབ་མཆོག །
འདོད་པར་གྱུར་པ་དེ་དག་ལ། །

[Block 436]
ཞེས་མ་སྨྲས་སམ། ཡང་འདིར་འདི་སྐད་དུ་བརྗོད་པ་དེ་ཇི་ལྟ་བུ་སྨྲས་པ་བདེན་ཏེ། སྔ་མ་ནི་མ་དག་པའི་རྟེན་དུ་བཞག་ལ་འདི་ནི་དག་པའི་རྟེན་དུ་འདོད་པ་ཡིན་ནོ། །

[Block 437]
འདིའི༌[^230]དོན་བླ་མ་རྗེ་བཙུན་དཔལ་བྱང་ཆུབ་བཟང་པོས་སྡོམ་པ་ཉི་ཤུ་པའི་འགྲེལ་པར་གསུངས་ཏེ། འདི་སྐད་དུ་སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་སྡོམ་པའི་ཡན་ལག་ཏུ་གྱུར་པ་ཡིན་ཏེ། ཕྱོགས་གཅིག་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 438]
དེའི་ཕྱིར་སོ་སོར༌[^231]ཐར་པའི་སྡོམ་པ་གཞན་དང་ལྡན་པ་འདིས་བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ་ཡང་དག་པར་ལེན་པའི་སྣོད་དུ་གྱུར་པ་ལ། བསླབ་པའི་ཚིག་འདི་ཡང་སྦྱིན་པར་བྱ་ཞེས་པའི་དོན་ཏོ། །

[Block 439]
འདི་ལ་སྲོག་གཅོད་པ་ལ་སོགས་པ་ལས་ལྡོག་པའི་ཆོ་ག་གཞན་པ་ཉིད་མ་ཡིན་ཞིང་དེ་རྣམས་ལས་ཀྱང་ལྡོག་པ་ཡིན་པ་ལ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ་ལེན་པའི་སྣོད་དུ་གྱུར་པ་ཡང་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 440]
རེ་ཞིག་ཐེག་པ་ཆེན་པོའི་བག་ཆགས་མེད་པ་དེའི་རིགས་མེད་པ་སོ་སོར༌[^232]ཐར་པའི་གཏན་གྱི་བར་ཆད་ཅན་ནམ། བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ་མེད་པའི་གོང་དུ་དེ་ལ་ཕམ་པ་བྱུང་བའམ་བསླབ་པ་ཕུལ་བའམ་དགེ་བའི་རྩ་བ་ཆད་པའམ། སྡོམ་པ་དེ་མ་བླངས་པ་ནི་སོ་སོར༌[^233]ཐར་པའི་སྡོམ་པ་ཡང་མེད་ན། ཅིག་ཤོས་ལྟ་ག་ལ་ཡོད་དུ་རུང་། འདིར་སྨྲས་པ། སྲོག་གཅོད་པ་ལ་སོགས་པ་ལས་མ་ལོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡོད་པར་འགྱུར་རམ། སྨྲས་པ་དེ་ནི་མེད་དེ་དེ་དག་ནི་བྱང་ཆུབ་སེམས་དཔའ་ལ་རྩ་བའི་ལྟུང་བ་ཡིན་པར་མདོ་ལས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 441]
དེ་ལྟ་བས་ན༌[^234]སོ་སོར་ཐར༌[^235]པའི་སྡོམ་པ་དེ་དང་པོར་དགོས་ཤིང་སྔོན་དུ་འགྲོ་བ་ཉིད་དོ། །

[Block 442]
ཡང་ན་རིགས་ལ་གནས་པ་དང་སྐྱེ་བ་གཞན་དུ་ཐེག་པ་ཆེན་པོ་ལ་གོམས་པར་བྱས་པ༌[^236]ནི་དེ་རང་བཞིན་གྱིས་སྡིག་པ་མི་སྤྱོད་པས་བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ་དེ་ཉིད་དང་པོ་ཉིད་དུ་བླངས་ཀྱང་ཉེས་པ་མེད་དོ། །

[Block 443]
ཡང་ན་ཐེག་པ་ཆེན་པོ་དབུ་མ་ཆེན་པོའི་གྲུབ་མཐའ་བརྩན་པར༌[^237]བྱས་ན་ནི། འདི་ལྟར་ཐེག་པ་ཆེན་པོའི་སྣོད་དུ་མ་གྱུར་པ་འགའ་ཡང་མེད་དོ། །

[Block 444]
སེམས་ཅན་ཐམས་ཅད་རིགས་གཅིག་ཉིད་ཡིན་ཏེ། དེ་བཞིན་གཤེགས་པའི་སྙིང་པོ་ཅན་ནོ༌[^238]ཞེས་བྱ་བ་དང་།

[Block 445 [VERSE]]
ས་སྟེངས༌[^239]སྐལ་མེད་ཡོད་མིན་ཏེ། །
ཐམས་ཅད་སངས་རྒྱས་འགྱུར་བ་ཡིན། །
དེའི་ཕྱིར་རྫོགས་སངས་སྒྲུབ་པ་ལ། །
སྒྱིད་ལུག་པར་ནི་མི་བྱའོ། །

[Block 446]
ཞེས་གསུངས་པའོ། །

[Block 447]
དེ་ཁོ་ན་ཉིད་བསྡུས་པའི་རྒྱུད་ཆེན་པོ་ལས་ཀྱང་། ཀྱེ་བཅོམ་ལྡན་འདས་ཀྱི་དཀྱིལ་འཁོར་ཆེན་པོ་འདིར་འཇུག་པ་ལ་སྣོད་དང་སྣོད་མ་ཡིན་པ་བརྟག་མི་འཚལ་ལོ། །

[Block 448]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 449]
སློབ་དཔོན་འཕགས་པ་ལྷའི་ཞལ་ནས།

[Block 450 [VERSE]]
དང་པོར་གང་དང་གང་འདོད་པ། །
དེ་ལ་དེ་དང་དེ་ཉིད་སྦྱིན། །
དམ་པའི་ཆོས་ལ་སྣོད༌[^240]མིན་པ། །
འགའ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 451]
ཞེས་གསུངས་སོ། །

[Block 452]
དེ་བས་སེམས་ཅན་ཐམས་ཅད་རིགས་གཅིག་ཉིད་ཡིན་པས། མགོན་པོ་མི་ཕམ་པའི་ཞལ་ནས།

[Block 453]
ཆོས་ཀྱི་དབྱིངས་ལ་དབྱེར་མེད་ཕྱིར། །རིགས་ནི་ཐ་དད་རུང་མ་ཡིན། །ཞེས་གསུངས་པ་དང་། འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་ནས་ཀྱང་།

[Block 454 [VERSE]]
ཆོས་ཀྱི་དབྱིངས་ལ་དབྱེར་མེད་ཕྱིར། །
གཙོ་བོ་ཐེག་དབྱེར་མ་མཆིས་ན། །
ཁྱོད་ཀྱིས༌[^241]ཐེག་པ་གསུམ་བསྟན་པ། །
སེམས་ཅན་འཇུག་པར་བྱ་ཕྱིར་ཡིན། །

[Block 455]
ཞེས་གསུངས་སོ། །

[Block 456]
འོ་ན་མདོ་ལས་ཀྱང༌[^242]སེམས་ཅན་གྱི་ཚོགས་གསུམ་དུ་གསུངས་ཤིང་། རྡོའི་རིགས་ལ་དཔེར་མཛད་པ་དེ་ཇི་ལྟ་བུ། སེམས་ཅན་གྱི་རིགས་ཀྱང་རྣམ་པ་ལྔར་བཤད་པ་དེ་ཇི་ལྟ་བུ། སྨྲས་པ་དེ་ནི་རེ་ཞིག་པ་ལ་དགོངས་པ་ཡིན་ཏེ། རྗེ་བཙུན་གསེར་གླིང་པའི་ཞལ་སྔ་ནས། རིགས་ནི་རྣམ་པ་གཉིས་ཏེ། ཆོས་ཉིད་ཀྱི་རིགས་ཅན་དང་། སྒྲུབ་པའི་རིགས་ཅན་ནོ་ཞེས་གསུངས་པས༌[^243]སྒྲུབ་པའི་རིགས་ཅན་ལ་ནི་རེ་ཞིག་དེ་ལྟར་གནས་སོ། །

[Block 457]
ཆོས་ཉིད་ཀྱི་རིགས་ཅན་གྱི་དབང་དུ་བྱས་ན་ནི་དབྱེ་བ་གང་ཡང་མེད་དོ། །

[Block 458]
འདི་ལྟར་མཁས་པ་དག་གིས་ནི་སོ་སོ་ཐར་པའི་སྡོམ་པ་དེ་ངེས་པར་གཙོ་བོར༌[^244]བྱ་དགོས་པ་ཡིན་ཏེ། དེ་ཡང་འདི་ལྟར་ཆོས་ཀྱི་སྐུ་ནི་དུས་ཐམས་ཅད་དང་། དངོས་པོ་ཐམས་ཅད་ལ་ཁྱབ་པ་ཡིན་པ་དང་། ཡང་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་དེ་ཡང་འཁོར་ལོར༌[^245]བཞུགས་ལ། དེ་ཡང་ས་བཅུའི་དབང་ཕྱུག་ཆེན་པོ་རྣམས་ཁོ་ནའི་སྤྱོད་ཡུལ་ཡིན་ཞིང་དེ་ཡང་ཐེག་པ་ཆེན་པོའི་ཆོས་ཟབ་པ་དང་། རྒྱ་ཆེ་བ་འབའ་ཞིག་གསུངས་པ་ཡིན་ནོ། །

[Block 459]
སྤྲུལ་པའི་སྐུ་ནི་འདི་ལྟར་ཨུ་དུམ་བཱ་རའི་མེ་ཏོག་དང་འདྲ་བས་དུས་རེས་འགའ༌[^246]བ་ཡིན་ཏེ། མདོ་ལས་བསྐལ་པ་དེའི་རྗེས་ལ་སངས་རྒྱས་མི་འབྱུང་བའི་བསྐལ་པ་དྲུག་ཅུ་འབྱུང་བར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 460]
དེ་བས་ན་དེས་གསུངས་པའི་སོ་སོར༌[^247]ཐར་པའི་སྡོམ་པ་འདི་ཡང་དུས་རེས་འགའ་བ་ཡིན་པས་དཀོན་པའི་ཕྱིར་དང་། བདེ་འགྲོར་བགྲོད་པའི་རྒྱུའི་གཙོ་བོ་ཡིན་པ་དང་། སངས་རྒྱས་ཀྱི་བསྟན་པ་ནི་སྲོག་གཅོད་པ་ལ་སོགས་པ་སྡིག་པ་ལས་ལོག་པ་ཡིན་པ་དང་། སངས་རྒྱས་ཀྱི་བསྟན་པ་ནི་ཇི་སྲིད་སོ་སོར་ཐར་པའི་སྡོམ་པ་གནས་པ་དེ༌[^248]སྲིད་དུ་གནས་ཤིང་དེ་ལ་རག་ལུས་པ་ཡིན་པས་སོ་སོར་ཐར་པའི་སྡོམ་པ་དེ་དང་པོ་ཁོ་ནར་བསྟན་ཏོ། །
--- END BLOCKS ---
