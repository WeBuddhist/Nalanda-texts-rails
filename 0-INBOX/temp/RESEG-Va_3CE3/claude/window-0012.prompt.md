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
བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་སུམ་ཅུ་རྩ་བདུན་དང་སྦྱར་བ་ནི་བཅུ་དགུ་པའོ། །

[Block 422]
འཕགས་པའི་བདེན་པ་ནས་གཟུངས་ཀྱི་སྒོའི་བར་དང་སྦྱར་བ་ནི་ཉི་ཤུ་པའོ། །

[Block 423]
སྟོབས་བཅུ་ནས། མ་འདྲེས་པའི་བར་དང་སྦྱར་བ་ནི་ཉི་ཤུ་གཅིག་པའོ། །

[Block 424]
རིགས་ཀྱི་སའི་ཆོས་ནས་བྱས་པ་རྟོགས་པའི༌[^266]བར་དང་སྦྱར་བ་ནི་ཉི་ཤུ་གཉིས་པའོ། །

[Block 425]
རྒྱུན་དུ་ཞུགས་པ་ནས་དགྲ་བཅོམ་པའི་བར་གྱི་གང་ཟག་དང་སྦྱར་བ་ནི་ཉི་ཤུ་གསུམ་པའོ། །

[Block 426]
རང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་སངས་རྒྱས་དང་སྦྱར་བ་ནི་ཉི་ཤུ་བཞི་པའོ། །

[Block 427]
ཐེག་པ་གསུམ་དང་སྦྱར་བ་ནི་ཉི་ཤུ་ལྔ་པའོ། །

[Block 428]
མྱ་ངན་ལས་འདས་པའི༌[^267]དཔེ་བསྟན་པ་ནི༌[^268]འགྲེས་ཉི་ཤུ་རྩ་དྲུག་པ་སྟེ། དེ་དག་ནི་འགྲེས་ཉི་ཤུ་རྩ༌[^269]དྲུག་གོ། །

[Block 429 [HEADING]]
##### འོང་བའམ་འགྲོ་བ་མི་དམིགས་པ། ^1-1-6-4-0

[Block 430]
ཐེག་པ་འདི་ལ་འོང་བའམ། འགྲོ་བ་ཞེས་བྱ་བ་ཡང་མི་དམིགས་ཤིང་གནས་པ་ཞེས་བྱ་བ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཚིག་བཞི་པ་བསྟན་ཏེ། རབ་འབྱོར་ཆོས་ཐམས་ཅད་ནི་དབྱེ་བ༌[^270]མེད་པ་སྟེ། དེ་དག་གང་དུ་ཡང་འདོར་བ་མེད་དོ། །

[Block 431]
གང་ནས་ཀྱང་འོང་བ་མེད་དོ། །

[Block 432]
གར་ཡང་གནས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་མཐར་ཐུག་པའི་ཐེག་པ་ཆེན་པོའི་གནས་སྐབས་ན་ཆོས་ཐམས་ཅད་དེ་བཞིན་ཉིད་ཙམ་དུ་ཟད་པའི་ཕྱིར། སྐྱེ་བ་དང་། འགག་པ་དང་། གནས་པ་མེད་པས་མི་གཡོ་བར་སྣང་ངོ་། །རང་བཞིན་དང་དེ་བཞིན་ཉིད་དང་ངོ་བོ་ཉིད་དང་ཞེས་བྱ་བ་ནི་མཐར་ཐུག་པའི་ཐེག་པ་ཆེན་པོའི་ས་ལ་ཆོས་ཀྱི་དབྱིངས་དེ་ཉིད་རང་བཞིན་ཉིད་དང་། དེ་བཞིན་ཉིད་དང་། ངོ་བོ་ཉིད་དང་། མཚན་ཉིད་ཁོ་ནར་བཟུང༌[^271]སྟེ། དེ་ཉིད་རང་བཞིན་ཡིན་གྱི་གཞན་མེད་དོ། །

[Block 433 [VERSE]]
དེ་ཉིད་དེ་བཞིན་ཉིད་ཡིན་གྱི་གཞན་མ་ཡིན་ནོ། །
དེ་ཉིད་ངོ་བོ་ཉིད་ཡིན་གྱི་གཞན་མ་ཡིན་ནོ། །
དེ་ཉིད་མཚན་ཉིད་ཡིན་གྱི་གཞན་མ་ཡིན་ཏེ།
དེ་ལས་ཕྱེ་སྟེ་སྨོས་པ་ཙམ་དུ་ཟད་དོ། །

[Block 434]
དེ་ལ་མི་གཡོ་བའི་འགྲེས་ནི་དང་པོའོ། །

[Block 435]
དེ་ནས་ཕུང་པོ་རྣམས་དང་། སྐྱེ་མཆེད་རྣམས་དང་། རྣམ་པར་ཤེས་པ་རྣམས་དང་། རེག་པ་རྣམས་དང་། ཚོར་བ་རྣམས་དང་། ཁམས་དྲུག་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཡན་ལག་རྣམས་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་དང་། སྟོང་པ་ཉིད་ཐམས་ཅད་དང་། དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་མ་འདྲེས་པའི་མཐར་ཐུག་པ་རྣམས་དང་། དེ་བཞིན་ཉིད་དང་། མ་ནོར་བ་དེ་བཞིན་ཉིད་དང་། གཞན་མ་ཡིན་པ་དེ་བཞིན༌[^272]ཉིད་དང་། ཆོས་ཉིད་དང་། ཆོས་ཀྱི་དབྱིངས་དང་། ཆོས་གནས་པ་ཉིད་དང་། ཆོས་སྐྱོན་མེད་པ་ཉིད་དང་། ཡང་དག་པའི་མཐའ་དང་། བསམ་གྱིས་མི་ཁྱབ་པའི་དབྱིངས་དང་། བྱང་ཆུབ་དང་། སངས་རྒྱས་དང་། འདུས་བྱས་དང་། འདུས་མ་བྱས་རྣམས་ཏེ། དེ་དག་དང་སྦྱར་བར་བྱའོ། །

[Block 436 [HEADING]]
##### དུས་གསུམ་མཉམ་པ་ཉིད་ཀྱི་ཐེག་པ། ^1-1-6-5-0

[Block 437]
དེའི་འོག་ཏུ་ཐེག་པ་དེ་ལ་སྔོན་གྱི་མཐའ་ཡང་མི་དམིགས། ཕྱི་མའི་མཐའ་ཡང་མི་དམིགས། དབུས་ཀྱང་མི་དམིགས་ཏེ། དེ་ནི་དུས་གསུམ་མཉམ་པ་ཉིད་ཀྱི་ཐེག་པ་སྟེ། དེ་བས་ན་ཐེག་པ་ཆེན་པོ་ཞེས་བྱའོ་ཞེས་བྱ་བའི་ཚིག་འདི་ལ། དེ་ནི་དུས་གསུམ་མཉམ་པ་ཉིད་ཀྱི་ཐེག་པ་ཞེས་པ་ཞེས་བྱ་བའི་ཚིག་བཟུང༌[^273]སྟེ། དུས་ཞེས་བྱ་བ་དང་། གསུམ་ཞེས་བྱ་བ་དང་། མཉམ་པ་ཞེས་བྱ་བ་དང་། ཐེག་པ་ཞེས་བྱ་བ་སོ་སོར་སྨོས་ནས། འདས་པའི་དུས་ཀྱང་འདས་པའི་དུས་ཀྱིས་སྟོང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^274]ནི་དུས་སེལ་ལོ།[^275] །དུས་གསུམ་མཉམ་པ་ཉིད་ཀྱང་དུས་གསུམ་མཉམ་པ་ཉིད་ཀྱིས་སྟོང་ངོ་ཞེས་བྱ་བ་ནི་མཉམ་པ་ཞེས་བྱ་བས༌[^276]སེལ་ཏོ། །

[Block 438]
ཐེག་པ་ཆེན་པོ་ཡང་ཐེག་པ་ཆེན་པོས་སྟོང་ངོ་ཞེས་བྱ་བས་ནི་ཐེག་པ་སེལ་ཏོ། །

[Block 439]
བྱང་ཆུབ་སེམས་དཔའ་ཡང་བྱང་ཆུབ་སེམས་དཔས་སྟོང་ངོ་ཞེས་བྱ་བས་ནི། སྐབས་ནས་སྨོས་པའི་བྱང་ཆུབ་སེམས་དཔས༌[^277]སེལ་ཏོ། །

[Block 440]
རབ་འབྱོར་སྟོང་པ་ཉིད་ལ་གཅིག་ཅེས་བྱ་བ་མེད་དོ། །

[Block 441]
གཉིས་སམ་གསུམ་མམ་ཞེས་བྱ་བ་ནས། བཅུ་ཞེས་བྱ་བའི་བར་དུ་མེད་དོ་ཞེས་བྱ་བས་ནི་གྲངས་ཀྱི་ཚིག་སེལ་ཏོ། །

[Block 442]
དེ་བས་ན་འདི་ནི་དུས་གསུམ་མཉམ་པ་ཉིད་ཀྱི་ཐེག་པའོ་ཞེས་བྱ་བས་མཇུག་བསྡུས་ཏེ་བསྟན་པ་ཅི་ལས་དགོངས་ཤེ་ན། དུས་གསུམ་མཉམ་པ་ཉིད་ཀྱི་ཐེག་པ་ཞེས་བྱ་བ་ནི་མཐར་ཐུག་པའི་ཐེག་པ་ཆེན་པོ་ལ་བྱའོ། །

[Block 443]
ཐེག་པ་ཆེན་པོ་ཡང་ཐ་དད་དུ་བྱ་བ་ཐམས་ཅད་དང་བྲལ་བས། གཅིག་པུའི་བདག་ཉིད་དེ། དེ་ལ་ནི་དུས་ཞེས་བྱ་བ་དང་། དུས་མཉམ་པ་ཉིད་ཅེས་བྱ་བ་དང་། ཐེག་པ་ཆེན་པོ་ཞེས་བྱ་བ་དང་། བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བ་ཐམས་ཅད་སྟོང་པ་ཉིད་ཙམ་དུ་ཟད་པའི་ཐེག་པའོ། །

[Block 444]
སྟོང་པ་ཉིད་ཙམ་དུ་ཟད་པ༌[^278]དེ་ལ་ནི་ཀུན་བརྟགས་པའི་ཆོས་དེ་དག་མེད་པའི་ཕྱིར་ཐམས་ཅད་སེལ་ཏོ། །

[Block 445]
དེ་ལྟར་བསྩལ༌[^279]ནས་ཀྱང་ཐམས་ཅད་གཅིག་གི་བདག་ཉིད་དུ་འགྱུར་བའི༌[^280]ཕྱིར། དེ་བས་ན་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱི༌[^281]དུས་གསུམ་མཉམ་པ་ཉིད་ཀྱི་ཐེག་པ་སྟེ་ཞེས་བྱ་བ་ཐམས་ཅད་ཀྱི་མཇུག་བསྡུས་སོ། །

[Block 446]
དེ་ལྟར་མདོར་བསྡུས་ཏེ་བསྟན་ནས། ཐེག་པ་ཆེན་པོ་འདི་ལ༌[^282]མཉམ་པ་དང་། མི་མཉམ་པ་ནི༌[^283]མི་དམིགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྤྲོས་ཏེ་ཡན་ལག་ཐམས་ཅད་སེལ་ཏོ། །

[Block 447]
མཉམ་པ་དང་མི་མཉམ་པ་ཉིད་ཐ་དད་པའོ། །

[Block 448]
འདོད་ཆགས་དང་འདོད་ཆགས༌[^284]བྲལ་བ་ཡང་མི་དམིགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ།[^285] འདོད་ཆགས་ནི་མི་མཉམ་པའོ། །

[Block 449]
འདོད་ཆགས་དང་བྲལ་བ་ནི་མཉམ་པའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 450]
དེ་ལྟར་ཆོས་ཐམས་ཅད་གཉིས་ཀྱི་ངོ་བོར་མེད་པར་བསྟན་ནས། རབ་འབྱོར་འདས་པའི་གཟུགས་ནི་འདས་པའི་གཟུགས་ཀྱིས་སྟོང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པས། ཡང་སོ་སོའི་མིང་སྨོས་ཏེ་མེད་པར་བསྟན་ཏོ། །

[Block 451]
སྟོང་པ་ཉིད་ཀྱང་སྟོང་པ་ཉིད་ཀྱིས་སྟོང་པས་དམིགས་སུ་མེད་ན། སྟོང་པ་ཉིད་ལ་འདས་པའི་གཟུགས་དམིགས་པར་ལྟ་ག་ལ་འགྱུར་ཞེས་བྱ་བ་ལ་གཟུགས་སྟོང་པ་ཞེས་བྱ་བ་ནི་གང་གི་ཚེ་གཟུགས་དང་འབྲེལ་བའི་སྟོང་པ་ཉིད་སྨོས་པ་དེའི་ཚེ་སྟོང་པ་དེ་ཉིད་ཀྱང་ཀུན་བརྟགས་པ་ཡིན་པའི་ཕྱིར་ཡོད་པ་མ་ཡིན་ན་སྟོང་པ་ཉིད་དེ་ལ་གཟུགས་ཡོད་པར་གཟུགས་ལ་འགྱུར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 452]
སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པའི་ཆོས་རྣམས་ཀྱང་། དུས་གསུམ་མཉམ་པ་ཉིད་ལ་མི་དམིགས་པར་བསྟན་ནས། མཉམ་པ་ཉིད་ཀྱང་མཉམ་པ་ཉིད་ལ་མི་དམིགས་ན་ཞེས་བྱ་བ་ཅི་ལས༌[^286]དགོངས་ཤེ་ན། མཐར་ཐུག་པའི་ཐེག་པ་ཆེན་པོའི་ས་ལ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་ཆོས་ཐམས་ཅད་རྣམ་པར་སྨིན་པའི་བདག་ཉིད་དུ་གྱུར་ནས། སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཀྱི་རྗེས་སུ་ཞུགས་ཏེ། དེ་བས་ན་དེ་ལ་དུས་གསུམ༌[^287]མཉམ་པ་ཉིད་ཅེས་བྱ་བ་ཡང་མེད་ལ། དུས་གསུམ་དུ་གཏོགས་པའི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་ཡང་མེད་དོ། །

[Block 453]
དེའི་ཕྱིར། མཉམ་པ་ཉིད་ལ་འདས་པ་དང་། མ་འོངས་པ་དང་། ད་ལྟར་བྱུང་བའི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དམིགས་པར་ག་ལ་འགྱུར་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 454]
དེ་བཞིན་དུ་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 455]
འགྲེས་ནི་དུས་གསུམ་མཉམ་པ་ཉིད་བསྩལ་བའི༌[^288]འགྲེས་དང་། ཆོས་ཐམས་ཅད་གཉིས་ཀྱི་སྒོ་ནས་བསྩལ་བའི་འགྲེས་དང་། ཕུང་པོ་ལྔའི་ཆོས་རྣམས་ལ་དུས་གསུམ་བསྩལ་བའི་འགྲེས་དང་། སྟོང་པ་ཉིད་ལ་དུས་གསུམ་དུ་གཏོགས་པའི་ཕུང་པོ་ལྔའི་ཆོས་རྣམས་བསྩལ་བའི་འགྲེས་དང་། དུས་གསུམ་མཉམ་པ་ཉིད་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་བསྩལ་བའི་འགྲེས་དང་། དེ་དག་ལ་སྟོང་པ་ཉིད་བསྩལ་བའི་འགྲེས་དང་། དེ་དག་ཉིད་ལ་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་མ་འདྲེས་པའི་མཐར་ཐུག་པའི་བར་དག་བསྩལ་བའི་འགྲེས་དང་། སོ་སོ༌[^289]སྐྱེ་བོ་བསྩལ་བའི་འགྲེས་དང་། ཉན་ཐོས་དང་། རང་སངས་རྒྱས་དང་། བྱང་ཆུབ་སེམས་དཔའ་དང་། དེ་བཞིན་གཤེགས་པ་བསྩལ་བའི་འགྲེས་རྣམས་སུ་ཤེས་པར་བྱའོ། །

[Block 456]
དེ་བས་ན་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱི་ཐེག་པ་ཆེན་པོ་ཞེས་བྱའོ་ཞེས་བྱ་བ་ནི་ཆེན་པོ་རྣམས་ཀྱི་ཐེག་པ་ཡིན་པས་ཐེག་པ་ཆེན་པོ་ཞེས་བྱ་བར་ངེས་པའི་ཚིག་གིས་བསྟན་ཏོ། །

[Block 457 [HEADING]]
#### གཏན་ལ་དབབ་པའི་ཚིག་བཅུ་གཉིས། ^1-1-7-0

[Block 458]
བཅོམ་ལྡན་འདས་གནས་བརྟན་རབ་འབྱོར་འདི་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སླད་དུ་བསྒོ་བ་མཛད་པས་འདི་ནི་ཐེག་པ་ཆེན་པོ་བསྟན་པར་སེམས་སོ་ཞེས་བྱ་བ་ནི་གནས་བརྟན་གང་པོས་འོག་ནས་བཤད་པའི་སྐབས་དབྱེ་བའི་ཕྱིར་གསོལ་པའོ། །

[Block 459]
སྔར་གདམས་པ་དང་། རྗེས་སུ་བསྟན་པ་བཤད་པ་རྩོམ་པ༌[^290]ལས་བཅོམ་ལྡན་འདས་ཀྱིས་རབ་འབྱོར་ཁྱོད་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་བརྩམས༌[^291]ཏེ། ཅི་ནས་ཀྱང༌[^292]བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ངེས་པར་འབྱུང་བར་འགྱུར་བར་སྤོབས་པར་གྱིས་ཤིག་ཅེས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཕྱིར་བསྐོས་ལ། ད་ལྟར་ནི༌[^293]ཐེག་པ་ཆེན་པོ་བཤད་པ་བྱས་པ་ལས་ཞུས་པ་ནི་དེའི་སྒོ་ནས་འོག་ནས་བཤད་པའི་ལམ་འདོད་དོ། །

[Block 460]
བཅོམ་ལྡན་འདས་བདག་གིས༌[^294]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་འགལ་བར་ཐེག་པ་ཆེན་པོ་བསྟན་པའམ་གཅིག་ཏུ་མ་གྱུར་ལགས་གྲང་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཐེག་པ་ཆེན་པོ་གཉིས་ཐ་མི་དད་པའི་ཕྱིར། ཐེག་པ་ཆེན་པོ་བསྟན་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་བསྟན་པ་ཡིན་པར་དགོངས་པ་སྟེ། ཐེག་པ་ཆེན་པོ་བསྟན་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པར་འགྱུར་རོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པས་ཐེག་པ་ཆེན་པོ་བསྟན་པར་འགྱུར་རོ་ཞེས་ཐ་མའི༌[^295]ཚིག༌[^296]བསྟན་ཏོ། །
--- END BLOCKS ---
