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
[Block 281]
སྲིད་པ་འདི་ལས་གཞན་མི་ཤེས་སོ་ཞེས་ཁོང་དུ་ཆུད་པའི་ཕྱིར་རོ། །

[Block 282 [HEADING]]
###### ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་རྣམ་གྲངས་གཞན། ^1-1-3-3-2-0

[Block 283]
གཞན་ཡང་ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་ནི་ཞེས་བྱ་བས་ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་རྣམ་གྲངས་གཞན་དུ་སྟོན་ཏེ། མཁན་པོ་དང་སློབ་དཔོན་གྱིས་བཤད་པའི་སྒྲ་ལ་བརྟེན༌[^260]ནས་གང་ཟག་ལ་བདག་མེད་པར་དམིགས་པ་ནི་ཉན་ཐོས་ཏེ། ཉན་ཐོས་དེ་དག་གི་ཐེག་པ་ནི་ཉན་ཐོས་ཀྱི་ཐེག་པའོ། །

[Block 284]
དེ་ཡང་རྣམ་པ་གཉིས་སུ་རིག་པར་བྱ་སྟེ། མི་མཐུན་པའི་ཕྱོགས་ལ་སུན་འབྱིན་པ་དང་། གཉེན་པོའི་ས་ལ་ཡོན་ཏན་དུ་ལྟ་བའོ། །

[Block 285 [HEADING]]
###### **མི་མཐུན་པའི་ཕྱོགས་ལ་སུན་འབྱིན་པ།** ^1-1-3-3-2-1-0

[Block 286]
དེ་ལ་མི་མཐུན་པའི་ཕྱོགས་ལ་སུན་འབྱིན་པ་ནི། གང་བསོད་ནམས་དང་བསོད་ནམས་མ་ཡིན་པ༌[^261]ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། སྐྱེ་བའི༌[^262]གནས་ཐམས་ཅད་ལ་མི་སྨོན་ཞེས༌[^263]བྱ་བ་ཡན་ཆད་ཀྱིས༌[^264]བསྟན་ཏོ། །

[Block 287]
གཉེན་པོའི་ས་ལ་ཡོན་ཏན་དུ་ལྟ་བའི༌[^265]མྱ་ངན་ལས་འདས་པ་ལ་གནས་དང་སྐྱབས་སུ་འདུ་ཤེས་པ་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 288]
དེ་བས་ན་གང་གིས་འགྲོ་བ་དང་། གང་དུ་འགྲོ་བའི་ཕྱིར་དེ་གཉིས་ནི་ཉན་ཐོས་ཀྱི་ཐེག་པ་སྟེ། གང་གིས་འགྲོ་བ་ནི་མི་མཐུན་པའི་ཕྱོགས་སུན་འབྱིན་པའི་འདུ་ཤེས༌[^266]ཀྱིས་འགྲོ་བའོ། །

[Block 289]
གོང༌[^267]དུ་འགྲོ་བ་ནི་མྱ་ངན་ལས་འདས་པའི་སར་འགྲོ་བའོ།[^268] །མི་མཐུན་པའི་ཕྱོགས༌[^269]སུན་འབྱིན་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། རྒྱུ་སྤོང་བ་དང་། འབྲས་བུ་སྤོང་བའོ། །

[Block 290 [HEADING]]
###### **རྒྱུ་སྤོང་བ།** ^1-1-3-3-2-1-1-0

[Block 291]
རྒྱུ་སྤོང་བ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ལས་སྤོང་བ་དང་། ཉོན་མོངས་པ་སྤོང་བའོ། །

[Block 292 [HEADING]]
###### **ལས་སྤོང་བ།** ^1-1-3-3-2-1-1-1-0

[Block 293]
ལས་སྤོང་བའི་དབང་དུ་བྱས་ནས་གང༌[^270]བསོད་ནམས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདུ་བྱེད་གསུམ་ནི་ཁམས་གསུམ་དུ་སྐྱེ་བའི་རྒྱུ་བྱེད་པར་མཐོང་ནས་དེ་རྣམས་ལ་རྣམ་པར་སྨོད་པར་བྱེད་དེ། རྣམ་པ་སྣ་ཚོགས་སུ་སྨོད་པ་ནི་རྣམ་པར་སྨོད་པ་སྟེ། སུན་འབྱིན་པར་བྱེད་པའོ། །

[Block 294]
དེ་འང་རྣམ་པ་གཉིས་ཏེ། སྔོན་བྱས་པ་སྤོང་བ་དང་། ཕྱིས་མི་བྱེད་པའོ། །

[Block 295 [HEADING]]
###### **སྔོན་བྱས་པ་སྤོང་བ།** ^1-1-3-3-2-1-1-1-1-0

[Block 296]
དེ་ལ་སྔོན་བྱས་པ་སྤོང་བ་ནི་འདུ་བྱེད་རྣམ་པ་གསུམ་སྔོན་སྤྱད་པའི་བག་ཆགས་ཡོད་པ༌[^271]ལ་འཕགས་པའི་ལམ་གྱིས་སྦྱོང་བའོ། །

[Block 297 [HEADING]]
###### **ཕྱིས་མི་བྱེད་པ།** ^1-1-3-3-2-1-1-1-2-0

[Block 298]
ཕྱིས་མི་བྱེད་པ་ནི་ཕྱིན་ཆད༌[^272]འདུ་བྱེད་རྣམ་པ༌[^273]གསུམ་གྱི༌[^274]ལས་ལ་མི་འཇུག་པའོ། །

[Block 299 [HEADING]]
###### **ཉོན་མོངས་པ་སྤོང་བ།** ^1-1-3-3-2-1-1-2-0

[Block 300]
ཉོན་མོངས་པ་སྤོང་བ་ཡང་རྣམ་པ་གཉིས་ཏེ། དེའི་འབྲས་བུ་སྡུག་བསྔལ་གྱི་བདག་ཉིད་དུ་མཐོང་བ་སོ།[^275] དེ་ལ་མི་དགའ་བ་དང་དེའི་རྒྱུས་སྡུག་བསྔལ་བསྐྱེད་པར༌[^276]མཐོང་བས་སྤོང་བར་འདོད་པའོ། །

[Block 301 [HEADING]]
###### **འབྲས་བུ་སྡུག་བསྔལ་གྱི་བདག་ཉིད་དུ་མཐོང་བས་མི་དགའ་བ།** ^1-1-3-3-2-1-1-2-1-0

[Block 302]
ཁམས་གསུམ་ཐམས་ཅད་ལ་ཡིད་བྱུང་ཞིང་ཞེས་བྱ་བས་དེའི་འབྲས་བུ་སྡུག་བསྔལ་གྱི་བདག་ཉིད་དུ་མཐོང་བས་དེ་ལ་མི་དགའ་བ་བསྟན་ཏེ། ཁམས་གསུམ་ནི་འདོད་པའི་ཁམས་དང་། གཟུགས་ཀྱི་ཁམས་དང་། གཟུགས་མེད་པའི་ཁམས་དག་གོ། །

[Block 303]
དེ་ལ་འདོད་པའི་ཁམས་ནི་གླིང་བཞི༌[^277]དང་། འདོད་པའི་ཁམས་ཀྱི་ལྷ་དྲུག་དང་། སེམས་ཅན་དམྱལ་བ་དང་། དུད་འགྲོ་དང་། ཡི་དྭགས་རྣམས་སོ། །

[Block 304]
གཟུགས་ཀྱི་ཁམས་ནི་ཚངས་རིས་དང་། ཚངས་པ་མདུན་ན་འདོན་དང་། ཚངས་ཆེན་ཞེས་བྱ་བ་ལ་སོགས་པ་གནས་བཅུ་དྲུག་དག་གོ། །

[Block 305]
གཟུགས་མེད་པའི་ཁམས་ནི་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ཅེས་བྱ་བ་ལ་སོགས་པ་བཞིའོ། །

[Block 306]
ཡིད་བྱུང་བ་ནི་ཁམས་གསུམ་ལ་སྐྱོ་བའོ། །

[Block 307 [HEADING]]
###### **རྒྱུས་སྡུག་བསྔལ་བསྐྱེད་པར་མཐོང་བས་སྤོང་བར་འདོད་པ།** ^1-1-3-3-2-1-1-2-2-0

[Block 308]
འདོད་ཆགས་དང་བྲལ་བ༌[^278]ཞེས་བྱ་བས་དེའི་རྒྱུས་སྡུག་བསྔལ་བ་སྐྱེད་པར་མཐོང་བས་སྤོང་བར་འདོད་པ་བསྟན་ཏེ། ཁམས་གསུམ་ནི་ཉོན་མོངས་པ་སྤངས་པ་ནི་འདོད་ཆགས་དང་བྲལ་བའོ། །

[Block 309 [HEADING]]
###### **འབྲས་བུ་སྤོང་བ།** ^1-1-3-3-2-1-2-0

[Block 310]
འབྲས་བུ་སྤོང་བའི་དབང་དུ་བྱས་ནས། འདུ་བྱེད་ཐམས་ཅད་ལ་མི་རྟག༌[^279]ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 311]
ཐམས་ཅད་ཀྱི་སྒྲ༌[^280]རྟོག་པའི་སྒྲ་གཉི་ག་དང་སྦྱར་ཏེ། འདུ་བྱེད་ཐམས་ཅད་ལ་མི་རྟག་པར་རྟོག་པ་དང་། འདུ་བྱེད་ཐམས་ཅད་ལ་སྡུག་བསྔལ་བར་རྟོག་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 312]
རྒྱུ་དང་རྐྱེན་གྱིས་བསྐྱེད་པའི་ཕུང་པོ་དང་ཁམས་དང་། སྐྱེ་མཆེད་ལ་སོགས་པའི་ཆོས་རྣམས་ནི་འདུ་བྱེད་ཐམས་ཅད་དེ། དེ་དག་མི་རྟག་པ་རྣམ་པ་གཉིས་ཀྱིས་འཇིག་པར་བྱེད་པ་ནི་འདུ་བྱེད་ཐམས་ཅད་ལ་མི་རྟག་པར་རྟོག་པ་ཞེས་བྱའོ། །

[Block 313]
དེ་ལ་མི་རྟག་པ་རྣམ་པ་གཉིས་ནི་འཇིག་པས་མི་རྟག་པ་དང་། སྐད་ཅིག་མས་འཇོམས་པས་མི་རྟག་པའོ། །

[Block 314]
དེ་ལ་འཇིག་པས་མི་རྟག་པ་ནི་མཐར་འཆི་བར་འགྱུར་བ༌[^281]སྟེ། མནར་མེད་པ་ནས་བརྩམས་ནས་སྲིད་པའི་རྩེ་མོའི་བར་དུ་དེ་ན་གནས་པའི་སེམས་ཅན་རྣམས་རང་གི་གནས་ནས་འཕོས་པས་སོ། །

[Block 315]
སྐད་ཅིག་མས་འཇོམས་པས་མི་རྟག་པ་ནི་སྐད་ཅིག་མ་རེ་རེ་ལ་ཡང་འཇིག་ཅིང་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 316]
འདུ་བྱེད་ཐམས་ཅད་སྡུག་བསྔལ་རྣམ་པ་བརྒྱད་དང་ལྡན་པར་ཤེས་པ་ནི་སྡུག་བསྔལ་བར་རྟོག་པ་ཞེས་བྱ་སྟེ། སྡུག་བསྔལ་རྣམ་པ་བརྒྱད་ནི་སྐྱེ་བའི་སྡུག་བསྔལ་དང་། རྒ་བའི་སྡུག་བསྔལ་དང་། ན་བའི་སྡུག་བསྔལ་དང་། ཤི་བའི་སྡུག་བསྔལ་དང་། མི་སྡུག་པ་དང་ཕྲད་པའི་སྡུག་བསྔལ་དང་། སྡུག་པ་དང་བྲལ་བའི་སྡུག་བསྔལ་དང་། གང་འདོད་པ་དེ་བཙལ་ཏེ་མི་རྙེད་པའི་སྡུག་བསྔལ་དང་། མདོར་ན་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་སྡུག་བསྔལ་བའོ། །

[Block 317]
དེ་ལ་སྐྱེ་བ༌[^282]ནི་མི་དང་ལྷ་ལ་སོགས་པའི་འགྲོ་བ་དེ་དང་དེ་དག་ཏུ་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་མངོན་པར་འགྲུབ་པའོ། །ཅིའི་ཕྱིར་སྐྱེ་བ་སྡུག་བསྔལ་བ་ཞེས་བྱ་ཞེ་ན། རྣམ་པ་གཉིས་ཀྱི་ཕྱིར་ཏེ། རང་བཞིན་གྱིས་སྡུག་བསྔལ་བ་དང་། སྡུག་བསྔལ་གཞན་གྱི༌[^283]རྟེན་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 318]
དེ་ལ་རྒས་པ་ནི་ཕུང་པོ་གཞན་དུ་གྱུར་པ་སྟེ། ལང་ཚོ༌[^284]བཅོམ་པ་དང་། ན་ཚོད་ཉམས་པ་ལ་སོགས་པ་ལའོ། །ཅིའི་ཕྱིར་རྒ་བ་སྡུག་བསྔལ་བ་ཞེས་བྱ་ཞེ་ན། ཉེ་དུ་འཁོར་རྣམས་ཀྱིས་ཤིན་ཏུ་བྱམས་ཤིང་ཡིད་དུ་འོང་བར་བྱ་བ་དང་། འགྲོ་བ་བཟང་མོའི་མིག་དང་། ཡིད་ཀྱིས་རྗེས་སུ་མཐུན་པར་བྱེད་པའི་ཁ་དོག་དང་དབྱིབས་ཤིན་ཏུ་མཛེས་པ་དེ་རྒ་བའི་སེར་བས་ཕོག་ནས་མི་མཛེས་པ་དང་། འཁུམས་པ༌[^285]དང་། ཞིགས་པར་སྣང་བས་ཉེ་དུའི་ཕྱོགས་རྣམས་ཀྱང་ཤིན་ཏུ་མི་དགའ་བར་བྱེད་ཀྱི། འགྲོ་བ་བཟང་མོས་ཀྱང་སྤོང་བར་བྱེད་པས་རྒ་བ་སྡུག་བསྔལ་བའོ། །

[Block 319]
དེ་ལ་ཁམས་མི་མཐུན་པ་འཕེལ་བར་གྱུར་པ་ནི་ན་བ་སྟེ་ས་ལ་སོགས་པའི་ཁམས་ཤས་ཆེ་ཆུང་དུ་གྱུར་པའོ། །ཅིའི་ཕྱིར་ན་སྡུག་བསྔལ་བ་ཞེས་བྱ་ཞེ་ན། རབ་ཏུ་མི་བཟད༌[^286]པའི་ནད་ཀྱི་ཁྱད་པར་གྱིས༌[^287]ཐེབས་ནས༌[^288]ནགས་ཆེན་པོ་མེས་ཚིག་པའི་ནང་དུ་ཆུད་པ་རབ་ཏུ་ཚ་བའི་མེ་ལྕེས་རེག་པ་སྐད་ཆེན་པོ་འབྱིན་པ་བཞིན་སྡུག་བསྔལ་བའི་མེས་རེག་པ་ན་མི་བཟད༌[^289]པའི་སྐད་ཆེར་འབྱིན་པས་ན་སྡུག་བསྔལ་བ་ཞེས་བྱའོ། །

[Block 320]
དེ་ལ་འཆི་བ་ནི་དབང་པོ་རྣམས་ཉམས་པ་ལས་དེའི་རྒྱུས་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་མི་རྒྱུ་བའོ། །
--- END BLOCKS ---
