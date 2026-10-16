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
དེ་ལྟར་ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། དེའི་འོག་ཏུ་བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། [^392]སངས་རྒྱས་ཀྱི་ཞིང་ཐ་དད་པ་ནས་འདུས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དཔག་ཏུ་མེད་པ་ཐམས་ཅད་ཀྱང་གནས་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 527]
དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་བསྟན་པའི་དགོས་པ་ནི་དེ་དག་ལ་ཁ་ཅིག་བརྙས་པ་བཟློག་པའི་ཕྱིར་ཏེ། ཉན་ཐོས་ཡུན་རིང་དུ་ཚངས་པར་སྤྱད་པ་རྣམས་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའ་དག་ལ་གདུང་བར་བྱའོ་ཞེས་གསུངས་པའི་ཕྱིར་དང་། ཁ་ཅིག་བྱང་ཆུབ་སེམས་དཔའ་དག་ཀྱང་ཡོན་ཏན་དེ་ལྟ་བུ་དང་ལྡན་པ་ཡིན་ན། དེ་བཞིན་གཤེགས་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་སྙམ་དུ་དད་པ་བསྐྱོད་པའི་ཕྱིར་རོ། །

[Block 528 [HEADING]]
###### ཆེན་པོ་རྣམ་པ་གསུམ། ^3-2-3-2-1-0

[Block 529]
དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཕུན་སུམ་ཚོགས་པ་ནི་ཆེན་པོ་རྣམ་པ་གསུམ་གྱིས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཆེན་པོ་བརྗོད་དེ། གྲངས་ཆེན་པོ་དང་། ཡོན་ཏན་ཆེན་པོ་དང་། ལས་ཆེན་པོས་སོ། །

[Block 530 [HEADING]]
###### **གྲངས་ཆེན་པོ།** ^3-2-3-2-1-1-0

[Block 531]
དེ་ལ་གྲངས་ཆེན་པོ་ནི། སངས་རྒྱས་ཀྱི་ཞིང་ཐ་དད་པ་ནས་འདུས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དཔག་ཏུ་མེད་པ་ཞེས་གསུངས་པས༌[^393]བསྟན་ཏོ། །

[Block 532]
དེ་ལ་སངས་རྒྱས་ཀྱི་ཞིང་ཐ་དད་པ་ནས་འདུས་པ་ཞེས་བྱ་བ་གསུངས་པ་ནི་དོན་དུ་མི་གཉེར་བས་ཆོས་ཉན་དུ་མི་འགྲོ་བ་དང་། ལེ་ལོས་ཆོས་ཉན་དུ་མི་འགྲོ་བ་དང་། ང་རྒྱལ་གྱི་དབང་གིས་ཆོས་ཉན་དུ་མི་འགྲོ་བ་དེ་དག་གི་གཉེན་པོར་བསྟན་པའི་ཕྱིར་ཏེ། དེ་ལ་དོན་དུ་མི་གཉེར་བས་ཆོས་ཉན་དུ་མི་འགྲོ་བ༌[^394]དག་གི་གཉེན་པོར་ནི་དེ་དག་ཀྱང་བདག་ཉིད་ཆོས་མཉན་པ༌[^395]དོན་དུ་གཉེར་བས་སངས་རྒྱས་ཀྱི་ཞིང༌[^396]ཐ་དད་པ་གཞན་དང་གཞན་ནས་འོངས་པ་ཡིན་གྱི།[^397] གཞན་གྱི་དྲིང་འཇོག་པས་ནི་མ་ཡིན་པས་གཞན་དག་གིས་ཀྱང་ཅིའི་ཕྱིར་ཆོས་མཉན་པ་དོན་དུ་གཉེར་བར་མི་བྱ་ཞེས་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 533]
ལེ་ལོས་ཆོས་ཉན་དུ་མི་འགྲོ་བ་དག་གི་གཉེན་པོར་ནི་དེ་དག་ཀྱང་སངས་རྒྱས་ཀྱི་ཞིང་ཐ་དད་པ་ཐག་རིང་པོ་དག་ནས་བརྩོན་འགྲུས་ཀྱི་སྟོབས་བསྐྱེད་པ་ཆེན་པོས་ཆོས་མཉན་པའི༌[^398]ཕྱིར་འདིར་འོངས་པ་ཡིན་ན། གཞན་དག་ལེ་ལོས་ཉན་དུ་མི་འགྲོ་བ་དེ་དག་ནི་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 534]
ང་རྒྱལ་གྱི་དབང་གིས་ཆོས་ཉན་དུ་མི་འགྲོ་བ་དག་གི་གཉེན་པོར་ནི་འབྱོར་པ་ཆེན་པོ་དང་ལྡན་པ་དེ་དག་ཀྱང་སངས་རྒྱས་ཀྱི་ཞིང་ཐ་དད་པ་གཞན་དག་ནས་ཆོས་མཉན་པའི་ཕྱིར་འོངས་ན་གཞན་དག་ཅིའི་ཕྱིར་འདོད་པར་མི་བྱ་སྙམ་དུ་སེམས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 535]
བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བའི༌[^399]ཚིག་གི་དོན་ནི་བླ་ན་མེད་པའི་བྱང་ཆུབ་དང་སེམས་ཅན་ཐམས་ཅད་ལ་དམིགས་ཏེ་སེམས་བསྐྱེད་པའོ། །

[Block 536]
ཡང་གཅིག༌[^400]ཏུ་ན་བྱང་ཆུབ་ཅེས་བྱ་བ་ནི་རྟོགས་པ་དང་ལྡན་པ་ཡིན་ལ། སེམས་དཔའ་ཞེས་བྱ་བ་ནི་སྙིང་སྟོབས་དང་ལྡན་པ་ལ་བྱའོ། །

[Block 537]
དཔག་ཏུ་མེད་པ་ཞེས་བྱ་བ་ནི་བགྲང་བ་ལས་ཡང་དག་པར་འདས་པ་སྟེ། དེ་ཉིད་ཀྱི་གྲངས་ཆེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 538 [HEADING]]
###### **ཡོན་ཏན་ཆེན་པོ།** ^3-2-3-2-1-2-0

[Block 539]
ཡོན་ཏན་ཆེན་པོ་ནི་ཆེན་པོ་རྣམ་པ་དགུས་རིག་པར་བྱ་སྟེ། བརྩོན་འགྲུས་ཆེན་པོ་དང་། རྒྱུ་ཆེན་པོ་དང་། དམིགས་པ་ཆེན་པོ་དང་། དུས་ཆེན་པོ་དང་། འདོད་པ་མེད་པ་ཆེན་པོ་དང་། ཡིད་ལ་བྱེད་པ་ཆེན་པོ་དང་། རྟོགས་པ༌[^401]ཆེན་པོ་དང་། ཡོངས་སུ་དག་པ་ཆེན་པོ་དང་། རྟོགས་པ་ཆེན་པོས་སོ། །

[Block 540 [HEADING]]
###### **བརྩོན་འགྲུས་ཆེན་པོ།** ^3-2-3-2-1-2-1-0

[Block 541]
དེ་ལ་བརྩོན་འགྲུས་ཆེན་པོ་ནི་ཐམས་ཅད་ཀྱང་གནས་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་བསྐྱབ་པའི་ཕྱིར་གནས་ཐམས་ཅད་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 542]
དེ་ལ་གནས་ཆེན་པོ་ཞེས་བྱ་བ་ནི་ཆེན་པོ༌[^402]རྣམས་ཀྱི་གནས་གང་ཡིན་པ་སྟེ། དེ་ཡང་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱི་གནས་དེ་ཐེག་པ་ཆེན་པོ་ཡིན་ནོ། །

[Block 543]
དེའི་དོན་གྱི་ཕྱིར་ཡང་དག་པར་ཞུགས་པ་རྣམས་ནི་བརྩོན་འགྲུས་དང་ལྡན་པས་ན་དེས་ནི་བརྩོན་འགྲུས་ཆེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 544 [HEADING]]
###### **རྒྱུ་ཆེན་པོ།** ^3-2-3-2-1-2-2-0

[Block 545]
རྒྱུ་ཆེན་པོ་ནི་ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱིས་ངེས་པར་འབྱུང་བ་ཞེས་གསུངས་པས་བསྟན་ཏེ། ཐེག་པ་ཆེན་པོ་དང་ཕ་རོལ་ཏུ་ཕྱིན་པས་བསྡུས་པ་ལམ་གྱི་རང་བཞིན་གྱི་ཆོས་ལ་སོགས་པས་ཐོས་པ་དང་། བསམས་པ་དང་། བསྒོམས་པ་ལ་སོགས་པའི་རིམ་གྱིས་ངེས་པར་འབྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 546]
ཐེག་པ་ཆེན་པོའི་ཆོས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ལམ་གྱི་རང་བཞིན་ཡིན་ལ། ལམ་ནི་ངེས་པར་འབྱུང་བའི་རྒྱུ་ཡིན་པས་ན་དེས་ནི་རྒྱུ་ཆེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 547 [HEADING]]
###### **དམིགས་པ་ཆེན་པོ།** ^3-2-3-2-1-2-3-0

[Block 548]
དམིགས་པ་ཆེན་པོ་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་སེམས་མཉམ་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། སེམས་ཅན་ཐམས་ཅད་ལ་བདག་དང་གཞན་དུ་མཉམ་པའི་སེམས་ཐོབ་པས་བྱམས་པ་ཆེན་པོ་ལ་སོགས་པས་མཉམ་པ་ཉིད་དུ་སྦྱོར་བའི་ཕྱིར་ཏེ། སེམས་ཅན་ཐམས་ཅད་ནི་བྱང་ཆུབ་སེམས་དཔའི་དམིགས་པའི་ཡུལ་ཡིན་ལ། དེ་དག་ལ་ཚད་མེད་པའི་སེམས་ཀྱིས༌[^403]མཉམ་པ་ཉིད་དུ་དམིགས་པར་བྱེད་པས་ན་དེས་ནི་དམིགས་པ་ཆེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 549 [HEADING]]
###### **དུས་ཆེན་པོ།** ^3-2-3-2-1-2-4-0

[Block 550]
དུས་ཆེན་པོ་ནི། བསྐལ་པ་དང་བསྐལ་པ་མ་ཡིན་པའི་ཡོངས་སུ་རྟོག་པ་ཐམས་ཅད་དང་བྲལ་བ་ཞེས་བྱ་བས་བསྟན་ཏེ། བླ་ན་མེད་པའི་བྱང་ཆུབ་དང་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བསྒྲུབ་པའི༌[^404]ཕྱིར་ཕྱི་མའི་མཐའི་མུར་ཐུག་པའི་དུས་ཐམས་ཅད་ལ་སྐད་ཅིག་གཅིག་དང་འདྲ་བར་འཇུག་གོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདི་ནི་བསྐལ་པ་ཡིན་ཏེ། བསྐལ་པ་གཅིག་གི་ཡུད་ཙམ་ཞིག་ཏུ་སྤྱད་པར་བྱའོ་ཞེས་སྙམ་པའམ་འདི་ནི་བསྐལ་པ་མ་ཡིན་ཏེ། བསྐལ་པ་བས་ཐུང་བའམ། བསྐལ་པ་ལས་ལྷག་པ་ཡིན་པས་དེ་དག་གི་ཡུད་ཙམ་ཞིག་ཏུ་སྤྱད་པར་བྱའོ་སྙམ་དུ་དུས་ལས་ཡོངས་སུ་རྟོག་པ་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར་གྲུབ་པའི༌[^405]མཐར་ཐུག་པའི་བར་དུ་བདག་ཉིད་ཀྱི༌[^406]སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་སྨིན་པར་བྱེད་པ་དང་། དུས་ཀྱི་མཐར་ཐུག་པའི་བར་དུ་ཕྱི་རོལ་གྱི་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པས༌[^407]ན་དེས་ནི་དུས་ཆེན་པོ་བསྟན་པ་ཡིན་ནོ། །

[Block 551]
ཡང་རྣམ༌[^408]གྲངས་གཞན་དུ་ཚིག་གི་དོན་ནི་རྟོག་པ་དང་རྣམ་པར་རྟོག་པ་དང་། ཡོངས་སུ་རྟོག་པ་ཐམས་ཅད་དང་བྲལ་བ་ཞེས་བྱ་བར་ཡང་འདྲེན་ཏེ། དེའི་ཚིག་གི་དོན་དུ་ན༌[^409]རྟོག་པ་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་དུ་རྟོག་པ་སྟེ། འདི་ནི་གཟུགས་སོ། །

[Block 552]
འདི་ནི་ཚོར་བའོ། །

[Block 553]
འདི་ནི་འདོད་ཆགས་སོ། །

[Block 554]
འདི་ནི་དད་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུར་ངོ་བོ༌[^410]ཉིད་དུ་རྟོག་པའོ། །

[Block 555]
རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་ཏུ་རྣམ་པར་རྟོག་པ་སྟེ། གཟུགས་འདི་ནི་ཟག་པ་དང་བཅས་པའོ། །

[Block 556]
[^411]འདི་ནི་ཟག་པ་མེད་པའོ། །

[Block 557]
ཚོར་བ་འདི་ནི་སྲེད་པས་བརླན་པའོ། །

[Block 558]
འདི་ནི་སྲེད་པས་མ་བརླན༌[^412]པའོ། །

[Block 559]
འདོད་ཆགས་འདི་ནི་མཐོང་བས་སྤང་བར་བྱའོ། །

[Block 560]
འདི་ནི་བསྒོམ་པས་སྤང་བར་བྱའོ། །

[Block 561]
དད་པ་འདི་ནི་ལས་དང་འབྲས་བུ་ལ་ཡིད་ཆེས་པའོ། །

[Block 562]
འདི་ནི་དཀོན་མཆོག་དང་བདེན་པ་ལ་སེམས་དད་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུར་བྱེ་བྲག་ཏུ་རྣམ་པར་རྟོག་པའོ། །

[Block 563]
ཡོངས་སུ་རྟོག་པ་ཞེས་བྱ་བ་ནི༌[^413]ངོ་བོ་ཉིད་དང་བྱེ་བྲག་ཏུ་ཡོངས་སུ་རྟོག་པ་སྟེ། འདི་ནི་གཟུགས་ཏེ། གཟུགས་འདི་ནི་ཟག་པ་དང་བཅས་པའོ། །

[Block 564]
འདི་ནི་ཟག་པ་མེད་པའོ། །

[Block 565]
འདི་ནི་ཚོར་བ་སྟེ། ཚོར་བ་འདི་ནི་སྲེད་པས་བརླན་པའོ།[^414] །འདི་ནི་སྲེད་པས་མ་བརླན་པའོ། །
--- END BLOCKS ---
