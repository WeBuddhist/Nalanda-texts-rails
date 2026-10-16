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
བདག་གི་སེམས་ནི་རང་གི་སེམས་སོ། །

[Block 422]
དེ་འགྱོད་པའི་མེ་དེས་སེམས་ཀུན་ཏུ་ཚིག་པ་ཡིན་ཏེ། ཇི་ལྟ་བུ་ཞེ་ན། འདི་ལྟར་མེ་ཆེན་པོས་འདམ་བུའམ་རྩྭ་དག་ཚིག་པ་ཡིན་ནོ། །

[Block 423]
དེ་བས་ཞེས་བྱ་བ་ནི་དེའི་ཕྱིར་རོ། །

[Block 424]
བསྲུང་བར་བྱ་བ་ནི་བསྲུང་བའོ། །

[Block 425]
ལུས་ཞེས་བྱ་བ་ལ། ཀ་ཞེས་བྱ་བའི་སྒྲ་ངན་པར་བསྟན་ཏོ། །

[Block 426]
གཡང་སར་ལྷུང་བ་ལ་ཐུག་པ་ཡིན་པས་དེའི་ཕྱིར་གང་གི་སྲོག་ཐུག་པ་ཡོད་པ་སྟེ་ལུས་ཀྱིའོ། །

[Block 427]
ཐུག་པ་ཞེས་བྱ་བ་ནི་ཉེ་བར་འདོད་པའི་སྲོག་དང་ལྡན་པའི་ལུས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 428]
ཕྲུ་གུ༌[^169]བསྲུང་བ༌[^170]ནི་ཕྲུ་གུ༌[^171]གསོད་པ༌[^172]ལས་སོ། །

[Block 429]
གཅན་མོ་ནི་སྟག་མོའོ། །

[Block 430]
དེའི་ཕྲུ་གུ༌[^173]ནི་དེའི་བུའོ། །

[Block 431]
གཞན་ཡང་ཞེས་བྱ་བ་ནི་གཞན་ཡང་ཡོད་པར་བསྟན་པའོ། །

[Block 432]
ཡང་ན་གཞན་ཡང་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཡང་བསྟན་པ་ཡིན་ཏེ། འདི་ལྟར་མདོའི་ཚིག་བསྟན་པ་ནི་ཡང་དག་པར་འཛིན་དུ་འཇུག་པའོ། །

[Block 433]
སྤྲོ་བ་བསྐྱེད་པ་ནི་ཡང་དག་པར་གཟེངས༌[^174]བསྟོད་པའོ། །

[Block 434]
དེ་ལ་བསྟན་པ་ནི་རབ་ཏུ་བཤད་པའོ། །གང་ལ་བཤད་པ་ཡིན་ཞེ་ན། གང་འཇིག་རྟེན་ལ་ཕན་པར་བརྩོན་པ་རྣམས་སོ། །

[Block 435]
འཇིག་རྟེན་ནི༌[^175]སེམས་ཅན་ནོ། །

[Block 436]
ཕན་བརྩོན་ནི་ཕན་འདོགས་པར་བྱེད་པའོ། །

[Block 437]
བརྩོན་འགྲུས་ཞན་པ་ནི་རྨོངས་པ༌[^176]སྟེ། ཕ་རོལ་གནོན་པ་ཞན་པ༌[^177]དང་། སྤྲོ་བ་ཆུང་བ་རྣམས་སོ། །

[Block 438]
དགའ་བ་བསྐྱེད་པ་ནི་ཚིམ་པར་བྱ་བའོ། །སུ་ཞེ་ན། གང་ཞིག་སྦྱིན་པ་གཏོང་ཕོད་པ་སྟེ། དེ་གང་ཡིན་ཞེ་ན། མགོན་མེད་ཟས་སྦྱིན་ལ་སོགས་པའོ། །

[Block 439]
གཏོང་བ་ནི་བཏང་བའོ། །

[Block 440]
ཕོད་པ་ནི་རླབས་ཆེ་བ་ཉིད་དོ། །

[Block 441]
སྐྱེ་བོ་དམ་པ་ཞེས་བྱ་བ་ནི་བག་ཡོད་པ་ལ་གནས་པ་སྟེ།[^178] བྱང་ཆུབ་སེམས་དཔའ་དང་སྐྱེས་བུ་དམ་པ་དག་གོ། །

[Block 442]
ཡིད་དྲང་བ༌[^179]ནི་འདྲེན་པའོ། །

[Block 443]
འདི་སྐད་སྟོན་པ་ཡིན་ཏེ། སྐྱེས་བུ་དམ་པ་རྣམས་ཀྱི་སེམས་འདྲེན་པར་བྱེད་པ་ཡིན་ནོ། །ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 444]
ཡང་ན་བདག་ལས་སྐྱེས་པ་ནི་བུ་བུ་ལས་བསྟན་པ་ནི་རབ་ཏུ་སྟོན་པའོ། །

[Block 445]
བརྩོན་པ་ནི་འབད་པའོ། །

[Block 446]
སྤྲོ་བ་བསྐྱེད་པ་ནི་གཟེངས༌[^180]བསྟོད་པའོ། །

[Block 447]
ཡིད་དྲང་བ༌[^181]ནི་ཡིད་དྲང་བར༌[^182]བྱ་བའོ། །

[Block 448]
བདུད་ནི་འདོད་པའི་ལྷའོ། །

[Block 449]
ཆེན་པོ་ནི་མང་པོ་ཉིད་དོ། །

[Block 450]
སྡེ་ནི་ཚོགས་སོ། །

[Block 451]
སྤ་བཀོང་བ་ནི་སེམས་ཞུམ་པར་བྱ་བའོ།[^183] །ཡང་ན་སྤ་བཀོང་བ་ནི་ཡིད་སྐྱོ་བར་བྱ་བའོ། །

[Block 452]
སངས་རྒྱས་ཀྱི་ཡོན་ཏན་ནི་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་བཅོ་བརྒྱད་དོ། །

[Block 453]
གཞན་ཡང་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་མཐའ་དག་གོ། །

[Block 454]
དགའ་བ་ནི་ཡོན་ཏན་ལ་དགའ་བའོ། །

[Block 455]
དང་བ་ནི་སེམས་དང་བའོ། །

[Block 456]
གང་དེ་དག་ལ་མངོན་པར་དད་པ་དང་མ་དད་པ་རྣམས་ཀྱང་དང་བར་འགྱུར་རོ། །

[Block 457]
བདག་གི་དོན་བརྩོན་ཞེས་བྱ་བ་ནི་བདག་གི་དོན་ལ་གཞོལ་བའོ། །

[Block 458]
ངོ་ཚ་ཞེས་བྱ་བ་ནི་ངོ་ཚའི་གནས་ཀྱིས་སོ། །

[Block 459]
འཇུངས་དང་འདོད་ཆེན་ཞེས་བྱ་བ་ལ། འཇུངས་པ་ནི་ཀུན་ཏུ་བཟུང་བའི་ཡོ་བྱད་ཀྱི་ཚོགས་ཡོངས་སུ་མི་གཏོང་བའི་ངང་ཚུལ་ལོ། །

[Block 460]
འདོད་ཆེན་ཞེས་བྱ་བ་ནི་ཞེན༌[^184]པས་གཟུང་བ༌[^185]སྟེ། བཟུང་བ༌[^186]དང་རྗེས་སུ་འབྲེལ་པའོ། །
--- END BLOCKS ---
