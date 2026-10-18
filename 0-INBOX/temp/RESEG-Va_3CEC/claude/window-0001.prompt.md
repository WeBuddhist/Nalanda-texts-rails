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
[Block 36]
དེ་ལྟར་ལུགས་དང་མཐུན་པའི་མཚན་ཉིད་བསྟན་ནས། ལུགས་ལས་བཟློག་པའི་མཚན་ཉིད་བསྟན་པའི་ཕྱིར། གཞན་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་མཚན་ཉིད་ལ་མཁས་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའོ། །

[Block 37]
འདི་ལྟ་སྟེ་ཤིང་མེད་ན་མེ་དང་དུ་བ་མི་འབྱུང་བ་དང་། ས་བོན་མེད་ན་མྱུ་གུ་མི་སྐྱེ་བ་བཞིན་དུ་ཉོན་མོངས་པ་འགགས༌[^14]ན་དེ་ལས་སྐྱེས་པའི་འབྲས་བུ་མི་འབྱུང་བའི་ཕྱིར་ཚུལ་བཞིན་མ་ཡིན་པ་འགགས་པས་མ་རིག་པ་འགག་ཅེས་བྱའོ།[^15] །

[Block 38]
ཇི་ལྟར་མ་རིག་པ་ལ་སོགས་པ་འགགས་པ་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བྱ་ཞེ༌[^16]ན། སྨྲས་པ། ཉེས་པ་མེད་དེ། འདི་ལ་གཏན་མེད་པར་དགག་པ་ལ་ནི་མ་རིག་པ་ལ་སོགས་པ་འགག་གོ་ཞེས་མི་བྱའི་དཔེར་ན་མར་མེའི་རྐྱེན་གྱིས་མུན་པ་འགགས་ན་སྣང་བ་ཉིད་སྐྱེ་བ་དང་། སྨན་བཅུད་ཀྱི༌[^17]ལེན་ཟོས་ན་ནད་མེད་པ་ལ་བདེ་བ་སྐྱེ་བ་དེ་བཞིན་དུ་ལམ་བསྒོམས་པའི་མཐུས་མ་རིག་པ་དང་མི་མཐུན་པ་གང་རིག་པ་སྐྱེ་བར་འགྱུར་བ༌[^18]དེ་ནི་མ་རིག་པ་འགགས་པ་ཞེས་བྱ་སྟེ། དེ་ལྟར་གོང་ནས་གོང་དུ་འདུ་བྱེད་ལ་སོགས་པ་དང་མི་མཐུན་པའི་གནས་འབྱུང་བ་ལ་འདུ་བྱེད་ལ་སོགས་པ་འགགས་པར་བལྟའོ། །

[Block 39 [HEADING]]
##### མཐུན་པའི་རྒྱུ་ལས་བྱུང་བ་དང་མི་མཐུན་པའི་རྒྱུ་ལས་མི་འབྱུང་བ། ^1-1-1-3-0

[Block 40 [HEADING]]
###### མཐུན་པའི་རྒྱུ་ལས་བྱུང་བ། ^1-1-1-3-1-0

[Block 41]
གཞན་ཡང་ཆོས་རྣམས་མཐུན་པའི་རྒྱུ་ལས་བྱུང་བ༌[^19]དང་། མི་མཐུན་པའི་རྒྱུ་ལས་མི་འབྱུང་བར་ཤེས་པ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་མཁས་པའོ་ཞེས་བསྟན་པར་བཞེད་ནས། གཞན་ཡང་ཆོས་ཐམས་ཅད་ནི་རྒྱུ་ལ་རག་ལུས་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཆོས་ཐམས་ཅད་ནི་ནང་གི་ཆོས་དང་ཕྱིའི་ཆོས་རྣམས་སོ། །

[Block 42]
དེ་ལ་ནང་གི་ཆོས་ནི་མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད་ལ་སོགས་པའོ། །

[Block 43]
ཕྱིའི་ཆོས་ནི་ས་བོན་དང་། མྱུ་གུ་ལ་སོགས་པའོ། །

[Block 44]
རྒྱུ་ལ་རག་ལུས་པ་ནི་ཆོས་དེ་དག་རྒྱུ་དྲུག་ལ་བརྟེན་ནས་སྐྱེའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 45]
དེ་ལ་རྒྱུ་དྲུག་པོ༌[^20]གང་ཞེ་ན། བྱེད་པའི་རྒྱུ་དང་། ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་དང་། སྐལ་བ་མཉམ་པའི་རྒྱུ་དང་། མཚུངས་པར་ལྡན༌[^21]པའི་རྒྱུ་དང་། ཀུན་དུ་འགྲོ་བའི་རྒྱུ་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུའོ། །

[Block 46]
དེ་ལ་བྱེད་པའི་རྒྱུ་ནི་ཆོས་དེ་དག་སྐྱེ་བ་ན༌[^22]གཟུགས་དང་སེམས་ལ་སོགས་པ་མཚན་ཉིད་དེ་དག་བདག་ཉིད་མ་གཏོགས་པར་ཆོས་གཞན་ཐམས་ཅད་ནི་བྱེད་པའི་རྒྱུ་སྟེ། སྐྱེ་བ་ལ་བགེགས༌[^23]མི་བྱེད་པའི་ངོ་བོར་གནས་པའི་ཕྱིར་རོ། །

[Block 47]
ཆོས་གང་དག་གཅིག་ལ་གཅིག་གི་འབྲས་བུར་གྱུར་པ་དེ་ནི་ལྷན་ཅིག་བྱུང་བའི༌[^24]རྒྱུ་སྟེ། འདི་ལྟ་སྟེ། འབྱུང་བ་ཆེན་པོ་བཞི་རྣམས་ལྷན་ཅིག་སྐྱེ་བ་ན་ཕན་ཚུན་སྐྱེད་པར༌[^25]བྱེད་པས་གཅིག་ལ་གཅིག་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུའོ། །

[Block 48]
དེ་བཞིན་དུ་སེམས་དང་སེམས་ལས་བྱུང་བ་དང་། འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བའི་ཆོས་སྔར་སྐྱེས་པ་རྣམས་ཕྱིས༌[^26]སྐྱེས་པ་དང་མ་སྐྱེས་པ་རྣམས་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུའོ། །

[Block 49]
དེ་བཞིན་དུ་དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་རྣམས་དང་ཡང་སྦྱར་རོ། །

[Block 50]
མཚུངས་པར་ལྡན་པའི་རྒྱུ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་གང་དག་སྐད་ཅིག་མ་གང་ལ་བརྟེན་ནས་གནས་པའི་དབང་པོ་རྣམས་སོ། །

[Block 51]
སྔར་སྐྱེད་པའི༌[^27]ཉོན་མོངས་པ་རྣམས་ཕྱིས་སྐྱེས་པ་དང་མ་སྐྱེས་པའི་རང་གི༌[^28]ས་པ་རྣམས་ཀྱིས་ཀུན་དུ་འགྲོ་བའི་རྒྱུ་ཡིན་པའི་ཕྱིར་ཀུན་དུ་འགྲོ་བའི་རྒྱུའོ། །

[Block 52]
མི་དགེ་བ་དང་དགེ་བ་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་ནི་རྣམ་པར་སྨིན་པའི་རྒྱུའོ། །

[Block 53]
རྐྱེན་ལ་རག་ལུས་ཞེས་བྱ་བ་ནི་རྐྱེན་བཞི་ལ་བརྟེན་ནས་སྐྱེ༌[^29]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 54]
རྐྱེན་བཞི་ནི་རྒྱུའི་རྐྱེན་དང་། དམིགས་པའི་རྐྱེན་དང་། མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་དང་། བདག་པོའི་རྐྱེན་ཏོ། །

[Block 55]
དེ་ལ་རྒྱུའི་རྐྱེན་ནི་གང་འབྲས་བུ་སྐྱེད་པ་ལ་རྒྱུའི་དངོས་པོར་གནས་པ་སྟེ། ས་བོན་ལ་སོགས་པ་དང་། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་བག་ཆགས་དང་བཅས་པའོ། །

[Block 56]
གཞན་དག་ནི་གཞན་དུ་འཆད་དེ། བྱེད་པའི་རྒྱུ༌[^30]མ་གཏོགས་པར་རྒྱུ་རྣམ་པ་ལྔ་རྣམས་ནི་རྒྱུའི་རྐྱེན་ཏོ་ཞེའོ། །

[Block 57]
དམིགས་པ་གང་ལ་སེམས་དང་སེམས་ལས༌[^31]བྱུང་བ་གང་དམིགས་ནས་སྐྱེ་བར་འགྱུར་བའི་དམིགས་པ་དེ་དག་ནི་དེའི་དམིགས་པའི་རྐྱེན་ཏེ། དེའང་ཅི་རིགས་པར་ཆོས་ཐམས་ཅད་རྣམ་པར་ཤེས་པ་དྲུག་གི་དམིགས་པའི་རྐྱེན་ཏོ། །

[Block 58]
མྱ་ངན་ལས་འདས་པར་འཇུག་པའི་ཐ་མའི་སེམས་མ་གཏོགས་པར་སེམས་དང་སེམས་ལས་བྱུང་བའི༌[^32]རྒྱུ་རྣམས་ནི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ཏོ། །

[Block 59]
བྱེད་པའི་རྒྱུ་ཉིད་བདག་པོའི་རྐྱེན་ཏོ། །

[Block 60]
ཚོགས་པ་ལ་རག༌[^33]ལུས་ཞེས་བྱ་བ་ནི་རྒྱུ་དང་རྐྱེན་རྣམས་འདུས་ནས་འབྲས་བུ་བསྐྱེད་ནུས་པའི་མཐུ་དང་ལྡན་པར་གནས་པ་ལ་བརྟེན་ནས། འབྲས་བུ་སྐྱེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 61 [HEADING]]
###### མི་མཐུན་པའི་རྒྱུ་ལས་མི་འབྱུང་བ། ^1-1-1-3-2-0

[Block 62]
མཐུན་པའི་རྒྱུ་ལས་བྱུང་བ༌[^34]བསྟན་ནས་མི་མཐུན་པའི་རྒྱུ་ལས་མི་འབྱུང་བར་བསྟན་པའི་ཕྱིར། ཆོས་གང་རྒྱུ་དང་རྐྱེན་དང་ཚོགས་པ་ལ་རག་ལུས་པ་དེ་དག་ལ་རག་མ་ལུས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གཞན་དག་གིས་བཏགས་པའི་བདག་ལ་སོགས་པ་ལ༌[^35]བརྟེན་ཏེ་མི་སྐྱེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 63]
དེ་འདི་ན་ཞེའམ། སྔ་མ་ཞེ་འམ། གཞན་ཞེས་བགྲང་བ་ཅི་ཡང་མེད་དེ་ཞེས་བྱ་བ་ནི་བདག་ལ་ཇི་ལྟར་རག་མ་ལུས་པ་དང་། སེམས་ཅན་ལ་སོགས་པ་ལ་རག་མ་ལུས་པས་ན་ད་ལྟའི་དུས་སུ་ཡང་འདི་ན་ཞེས་བགྲང་དུ་མེད། འདས་པའི་དུས་སུ་ཡང་འདི་འདྲ་བ་ཞིག་ཅེས་བགྲང་དུ་མེད། མ་འོངས་པའི་དུས་སུ་ཡང་འདི་ལྟར་འགྱུར་ཞེས་བགྲང་དུ་མེད་པའི་དོན་ཏོ། །

[Block 64]
ཡང་ན་ཆོས་ཐམས་ཅད་ནི་རྒྱུ་ལ་རག་ལུས་ཞེས་བྱ་བ་ནི་ཕྱི་དང་ནང་གི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྣམས་རྒྱུ་དང་འབྲེལ་པ་ལ༌[^36]སྐྱེ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དེ་ལ་ཕྱི་རོལ་གྱི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་རྒྱུ་དང་འབྲེལ་པ་གང་ཞེ་ན། འདི་ལྟ་སྟེ། ས་བོན་ལས་མྱུ་གུ། མྱུ་གུ་ལས་འདབ་མ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 65]
དེ་ལ་ནང་གི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྒྱུ་དང་འབྲེལ་པ་གང་ཞེ་ན། མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད། འདུ་བྱེད་ཀྱི་རྐྱེན་གྱིས་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 66]
རྐྱེན་ལ་རག་ལུས་པ༌[^37]ཞེས་བྱ་བ་ནི་ཕྱི་དང་ནང་གི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡང་རྐྱེན་དང་འབྲེལ་པ་ལ་སྐྱེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 67]
ཕྱིའི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་རྐྱེན་གང་ཞེ་ན། འདི་ལྟ་སྟེ། ས་དང་། ཆུ་དང་། མེ་དང་། རླུང་དང་། ནམ་མཁའ་དང་། དུས་ཀྱི་ཁམས་རྣམས་ཞེས་གང་གསུངས་པའོ། །

[Block 68]
ནང་གི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་རྐྱེན་གང་ཞེ་ན། ས་དང་། ཆུ་དང་། མེ་དང་། རླུང་དང་། ནམ་མཁའ་དང་། རྣམ་པར་ཤེས་པའི་ཁམས་རྣམས་ཞེས་གང་གསུངས་པའོ། །

[Block 69]
ཚོགས་པ་ལ་རག་ལུས་པ་ཞེས་བྱ་བ་ནི་རྒྱུ་དང་རྐྱེན་མ་ཚང་བར་མ་གྱུར་པ་ལ་རྟེན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 70]
དེ་བས་ན་སཱ་ལུ་ལྗང་པའི་མདོ་ལས་ཀྱང་། རྒྱུའི་སྐབས་སུ་ས་བོན་མེད་ན་མྱུ་གུ་མི་འབྱུང་སྟེ། མེ་ཏོག་མེད་ན་འབྲས་བུའི་བར་དུ་ཡང་མི་འབྱུང་ངོ༌[^38]ཞེས་གསུངས་པ་དང་། རྐྱེན་གྱི༌[^39]སྐབས་སུ་རྐྱེན་འདི་རྣམས་མེད་པར་ས་བོན་ལས་མྱུ་གུ་སྐྱེ་བར་མི་འགྱུར་གྱི། ནམ་ཕྱི་རོལ་གྱི་སའི་ཁམས་མ་ཚང་བ༌[^40]མེད་པར་གྱུར་པ༌[^41]ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 71]
ནང་གི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་ཡང་རྒྱུའི་སྐབས་སུ་གལ་ཏེ་མ་རིག་པ་མ་བྱུང་ན་འདུ་བྱེད་ཀྱང་མི་འབྱུང་བ་ཞིག་ན། དེ་བཞིན་དུ་སྐྱེ་བ་མ་བྱུང་དུ་ཟིན་ན་རྒ་ཤིའི་བར་དུ་ཡང་མི་མངོན་པ་ཞིག་ན། འདི་ལྟར་མ་རིག་པ་ཡོད་པ་ལས་འདུ་བྱེད་རྣམས་སྐྱེ་ཞིང་འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་དང་། རྐྱེན་གྱི་སྐབས་སུ་ཡང་རྐྱེན་འདི་དག་མེད་པར་ལུས་སྐྱེ་བར་མི་འགྱུར་གྱི། ནམ་སའི༌[^42]ཁམས་ཚང་ཞིང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའོ། །

[Block 72]
ཆོས་གང་རྒྱུ་དང་རྐྱེན༌[^43]ཚོགས་པ་ལ་རག་ལུས་པ་དེ་ཞེས་བྱ་བ་ནི་ཕྱི་དང་ནང༌[^44]གི་ཆོས་གང་རྒྱུ་དང་རྐྱེན་དང་། རྒྱུ་རྐྱེན་འབྲེལ་པ་ལས་སྐྱེས་པའི་ཆོས་དེ་དག་ནི་བདག་ལས་མི་སྐྱེ། སེམས་ཅན་ལས་མི༌[^45]སྐྱེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 73]
དེ་བས་ན་མདོ་སྡེ་དེ་ཉིད་ལས་ཕྱིའི་རྟེན་ཅིང་འབྲེལ་པར༌[^46]འབྱུང་བའི་སྐབས་སུ་དེ་ལ་སའི་ཁམས་ཀྱང་འདི་ལྟར་བདག་གི་ས་བོན་རྟེན་པའི་བྱ་བ་བྱའོ་སྙམ་དུ་མི་སེམས་སོ་ཞེས་བྱ་བ་ནས་མྱུ་གུ་དེ་ཡང་བདག་གིས་མ་བྱས། ཕ་རོལ་གྱིས༌[^47]མ་བྱས། གཉིས་ཀས་མ་བྱས། དབང་པོས་མ་སྤྲུལ། དུས་ཀྱི༌[^48]མ་བསྒྱུར། རང་བཞིན་ལས་མ་བྱུང་། རྒྱུ་མེད་པ་ལས་ཀྱང་མ་སྐྱེས་ཏེ་ཞེས་གསུངས་པ་དང་། ནང་གི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་སྐབས་སུ་ཡང་མ་རིག་པ་ཡང་འདི་ལྟར་བདག་གིས་འདུ་བྱེད་སྐྱེད་དོ་སྙམ་དུ་མི་སེམས་སོ་ཞེས་བྱ་བ་ནས་བདག་མ་ཡིན་ནོ། །

[Block 74]
སེམས་ཅན་མ་ཡིན། སྲོག་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 75]
དེ་ན་འདི་ན་ཞེ་འམ། སྔ་མ་ན་ཞེ་འམ། གཞན་ན་ཞེས་བགྲང་བ་ཅི་ཡང་མེད་དེ་ཞེས་བྱ་བ་ནི་ཆོས་གང་རྒྱུ་དང་རྐྱེན་དང་ཚོགས་པ་ལ་རག་ལུས་པས་བདག་དང་སེམས་ཅན་ལ་རག་མ་ལུས་པའི་ཆོས་དེ་ནི་ད་ལྟར༌[^49]ཅི་ཡིན་ཞེས་བརྟག༌[^50]ཏུ་མེད་པ་དང་། སྔོན་གྱི་དུས་ན་ཅི༌[^51]འདྲ་ཞེས་བརྟག༌[^52]ཏུ་མེད་པ་དང་། མ་འོངས་པའི་དུས་ན་ཅི་ལྟ༌[^53]བུར་འགྱུར་ཞེས་བརྟག༌[^54]ཏུ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
