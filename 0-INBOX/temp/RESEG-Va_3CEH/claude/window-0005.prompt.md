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
[Block 176]
སྙོམས་པར་འཇུག་པའི་བྱེ་བྲག་དང་སྟེ། གང་ལ་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཡོད་པ་དེ་ནི་འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་སྟེ་དེ་ཡོད་པས་སོ། །

[Block 177]
གཞན་ལ་ནི་དེ་མེད་དེ། དེ་ནི་ཁྱད་པར་ཡིན་ནོ། །

[Block 178]
གཞན་དུ་ན་གཉི་ག་ལ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཀུན་ཏུ་རྒྱུ་བ་མེད་ན་བྱེ་བྲག་མེད་པར་འགྱུར་རོ། །

[Block 179]
ངེས་ཚིག་མེད་པའི་སྐྱོན་དུ་འགྱུར། གང་འདི་སྐད་དུ་ངར་འཛིན་པས་ན་ཡིད་ཅེས་བྱ་བའི་ངེས་པའི་ཚིག་དེ་སྐད་དུ་བརྗོད་པའི་གཞི་གང་ཡིན། རྣམ་པར་ཤེས་པ་དྲུག་པོ་འགགས་མ་ཐག་པའི་རྣམ་པར་ཤེས་པ་ལ་ནི་འདི་ལྟར་མི་བརྗོད་དེ་འགགས་པའི་ཕྱིར་རོ། །

[Block 180]
འདུ་ཤེས་མེད་པའི་སྐྱེ་བའི་རྒྱུན་ཐོབ་པ་ན་ངར་འཛིན་པ་མེད་པའི་སྐྱོན་དུ་འགྱུར་ཏེ། འདི་ལྟར་དེའི་དུས་སྐབས་ན་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་མེད་ན་ངར་འཛིན་པ་མེད་པར་སྐྱེ་བར༌[^117]འགྱུར་རོ། །

[Block 181]
དེ་ལྟ༌[^118]ན་ནི་འཕགས་པས་ཀྱང་སྨད་པར་མི་འགྱུར་ན་དེ་ནི་སྨད་པ་ཉིད་ཡིན་པས་དེས་ན་དེ་ནི་དེ་ན་ཡོད་པ་ཉིད་དུ་རྟོགས་པར་བྱའོ། །

[Block 182]
ངར་འཛིན་པ་དང་ལྡན་པར་ནི་སྟེ། སྦྱིན་པ་ལ་སོགས་པ་སྦྱིན་པ་ལ་ཡང་ངར་འཛིན་པ་དང་ལྡན་པ་ཉིད་དོ། །

[Block 183]
ངར་འཛིན་པ་དང་ལྡན་པ་ཡང་མ་རིག་པ་མེད་པར་མི་རིགས་ལ། མ་རིག་པ་ཡང་རྟེན་མེད་པར་མ་ཡིན་ཞིང་། རྟེན་ཡང་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་མེད་ན་གཞན་མེད་དེ། ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྤངས༌[^119]པའི་ཕྱིར་འབད་པས་དེ་དག་གི་ཕྱིར་བསྟན་ཏོ། །

[Block 184 [HEADING]]
#### ཀུན་གཞི་ལ་ཀུན་ཏུ་དགའ་བ། ^1-3-4-0

[Block 185]
སྐྱེ་དགུ་ཀུན་གཞི་ལ་ཀུན་ཏུ་དགའ་བ་ཞེས་བྱ་བ་ནི་བསྟན་པའི་ཚིག་གོ། །

[Block 186]
ད་ལྟར་དང་འདས་པ་དང་། མ་འོངས་པའི་དུས་གསུམ་གྱི་གོ་རིམས་བཞིན་དུ་ཚིག་ལྷག་མ་རྣམས་ཀྱིས་ནི་བཤད་དོ། །

[Block 187]
དོན་གཞན་ཡང་ཀུན་གཞི་ལ་ཀུན་ཏུ་དགའ་བ་ནི་ད་ལྟར་རོ། །

[Block 188]
ཀུན་གཞི་ལ་དགའ་བ་ནི་འདས་པའི་དུས་སུ་སྟེ། གང་སྔར་ཀུན་གཞི་ལ་དགའ་བ་ལས་དེ་ལྟར་ཀུན་གཞི་ལས་ཡང་དག་པར་འབྱུང་ངོ་། །གང་ཀུན་གཞི་ལ་དགའ་བ་དང་། ཀུན་གཞི་ལས་ཡང་དག་པར་འབྱུང་བ་ལས་མ་འོངས་པའི་དུས་སུ་ཀུན་གཞི་ལ་མངོན་པར༌[^120]དགའ་བའོ། །

[Block 189]
ཆོས་ཀྱི་རྗེས་སུ་མཐུན་པའི་ཆོས་ནི་མན་ངག་ཇི་ལྟ་བ་བཞིན་དུ་བྱེད་པའོ། །

[Block 190 [HEADING]]
#### རྩ་བའི་རྣམ་པར་ཤེས་པ། ^1-3-5-0

[Block 191]
རྩ་བའི་རྣམ་པར་ཤེས་པ་ཞེས་ཀྱང་འབྱུང་སྟེ། རྣམ་གྲངས་དེས་ཀྱང་དེ་ཉིད་བསྟན་ཏེ། རྩ་བ་ལ་བརྟེན་པའི་ཤིང་ལྗོན་པ་བཞིན་ནོ་ཞེས་བརྗོད་པ་ལ་དེ་ལ་རྩ་བའི་རྣམ་པར་ཤེས་པ་ནི་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་ཀྱི་རྒྱུར་གྱུར་པ་ཉིད་དོ།[^121] །དཔེར་ན་ཤིང་གི་རྩ་བ་ཡལ་ག་ལ་སོགས་པའི་རྒྱུ་ཡིན་ཏེ། རྩ་བ་མེད་ན་ཡལ་ག་ལ་སོགས་པ་མི་འབྱུང་བ་བཞིན་དུ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཡང་རྩ་བའི་རྣམ་པར་ཤེས་པ་ཉིད་དོ། །

[Block 192 [HEADING]]
#### འཁོར་བ་ཇི་སྲིད་པའི་ཕུང་པོ། ^1-3-6-0

[Block 193]
འཁོར་བ་ཇི་སྲིད་པའི་ཕུང་པོ་རྣམས་ཞེས༌[^122]འབྱུང་སྟེ། རྣམ་གྲངས་དེས་ཀྱང་ཞེས་བྱ་བ་ལ་འཁོར་བ་ཇི་སྲིད་པའི་ཕུང་པོ་ཉིད་ཀྱང་དེ་ཉིད་ཡིན་ནོ། །

[Block 194]
གང་གི་ཕྱིར་ལ་ལར་ཏེ་གཟུགས་མེད་པའི་ཁམས་སུ་གཟུགས་སོ། །

[Block 195]
རེས་འགའ་ཞེས་བྱ་བ་ནི་སྙོམས་པར༌[^123]འཇུག་པ་ཁ་ཅིག་གི་གནས་སྐབས་སུ་སྟེ། འདི་ལྟ་སྟེ། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པར་རོ། །

[Block 196]
ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་དེའི་ས་བོན་ནི་རྒྱུན་མི་འཆད་ཅེས་བྱ་བ་ལ། གཟུགས་དང་སེམས་ཀྱི་བག་ཆགས་ཀྱི་རྒྱུ་གང་ལས་ཡང་སྲིད་པའི་གཟུགས་དང་སེམས་དག་འབྱུང་བར་འགྱུར་རོ། །

[Block 197]
ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་ལམ་པོ་ཆེ་གཏོང་བ༌[^124]ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་རྒྱས་པར་བྱས་ཞེས་བྱ་བའི་དོན་ཏེ། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཡོངས་སུ་བཟུང་ནས་རྣམ་པར་འཇོག་པ་དེ་ནི་ཤིན་ཏུ་མཛེས་པ་ཡིན་ནོ། །

[Block 198 [HEADING]]
#### ཀུན་གཞི་རྣམ་པར་ཤེས་པ་རྣམ་པར་གཞག་པ། ^1-3-7-0

[Block 199]
དེ་ལ་མ་རྨོངས་པ་རྣམས་ཀྱིས་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་ལ། དེ་ལ༌[^125]མ་རྨོངས་པའི་བྱང་ཆུབ་སེམས་དཔའ་གང་ཡིན་པ་དག་ལ་དེ་བསྟན་པའོ། །

[Block 200]
དེ་ལ་ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་རྣམ་པར་གཞག་པ་ནི་དེ་བས་ན་ཤིན་ཏུ་འཐད་པ་ཞེས་བྱ་བ་ནས༌[^126]བརྩམས་ཏེ། དེ་བས་ན་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཀུན་གཞི་ཉིད་དུ་ཆེས་ལེགས་པར་རྣམ་པར་གཞག་པ་གྲུབ་པོ༌[^127]ཞེས་བྱ་བའི་བར་གྱིས་སོ། །

[Block 201]
དེ་ལ་ངན་འགྲོ་ཞེས་བྱ་བ་ནི་ཡི་དྭགས་དང་དུད་འགྲོ་དང་། དམྱལ་བ་ནི་ངན་འགྲོའོ། །

[Block 202]
ཤིན་ཏུ་སྡུག་བསྔལ་བ་ཞེས་བྱ་བ་ནི་ལས་ཀྱི་འབྲས་བུ་ཤིན་ཏུ་མི་འདོད་པ་ཅན་གྱི་ངན་འགྲོ་རྣམས་ཏེ། གང་ཡང་དེར་རེས་འགའ་བདེ་བའི་ཚོར་བ་འབྱུང་བ་དེ་ནི་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ཡིན་གྱི་རྣམ་པར་སྨིན་པ་ཉིད་ནི་དེར་སྐྱེས་པ་རྣམས་ཀྱི་སྡུག་བསྔལ་ཁོ་ནའོ། །

[Block 203]
བདེ་བའི་ཚོར་བ་འདོད་ཆགས་དང་བཅས་པ་ཡང་བསམ་གཏན་བཞི་པ་ཡན་ཆད་གོང་མ་ལ་མེད་དེ། དེ་དང་ལྡན་པའི་སེམས་ཅན་རྣམས་དང་མི་མཐུན་པ་ཡིན་པས། བསམ་གཏན་བཞི་པ་ཡན་ཆད་གོང་མ་སྟེ། བསམ་གཏན་བཞི་པ་དང་གོང་མ་ལ་ཡང་ངོ་། །དེ་དང་ལྡན་པས༌[^128]ཞེས་བྱ་བ་ནི་དེར་སྐྱེས་པ་ཞེས༌[^129]པ་རྣམས་སོ། །

[Block 204]
ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་ནང་གི༌[^130]དངོས་པོར་ཁས་བླངས་པ་ཞེས་བྱ་བ༌[^131]ནས་བརྩམས་ནས་དེ་རྣམ་པར་ཞིག༌[^132]པར་འདོད་པ་ནི་ནམ་ཡང་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་བར་ལ། དེ་ལ་ནང་གི་བདག་གི་དངོས་པོར་ཁས་བླངས་པ་སྨོས་པ་ནི་ནང་གི་བདག་ཉིད་ཁས་བླངས་པའོ། །

[Block 205]
སྡུག་བསྔལ་གྱི་ཕུང་པོ་རྣམ་པར་གཞིག་པར་འདོད་པ་ནི་ཚོར་བ་སྡུག་བསྔལ་དང་བྲལ་བར་གསོལ་བ་འདེབས་སོ། །

[Block 206]
ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་བདག་ཏུ་ཆགས་པས་བཅིངས་པ་ཞེས་བྱ་བ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་བདག་གོ་ཞེས་ཁས་བླངས་ནས་སྲེད་པས་བཅིངས་པའོ། །

[Block 207]
དེ་ལྟར་རེ་ཞིག་རྣམ་གྲངས་རྣམ་པར་གཞག་པ་བསྟན་ཏོ། །

[Block 208 [HEADING]]
### མཚན་ཉིད་རྣམ་པར་གཞག་པ། ^1-4-0

[Block 209 [HEADING]]
#### རང་གི་མཚན་ཉིད། ^1-4-1-0

[Block 210]
ཡང་རྣམ་གྲངས་བསྟན་པ་ཙམ་གྱིས་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བའི་ངོ་བོ་ཉིད་དང་། རྒྱུ་ཉིད་དང་འབྲས་བུ་ཉིད་གང་ཡིན་པ་དེ༌[^133]ནི་ངེས་པར་གཟུང་བར༌[^134]མི་ནུས་པས་དེའི་རང་གི་མཚན་ཉིད་ནི་གང་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་ཐམས་ཅད་ཀྱི་བག་ཆགས་ལ་བརྟེན་ནས་དེ་སྐྱེད་པའི་ནུས་པའི་ཁྱད་པར་ཅན་གྱི་རྣམ་པར་ཤེས་པ་གང་ཡིན་པ་ནི་རང་གི་ངོ་བོ་ཉིད་དང་།[^135] དེ་ཉིད་ཀྱི་ནུས་པ་སྟོན་པ་ནི་ས་བོན་ཡོངས་སུ་འཛིན་པ་དང༌[^136]ཞེས་བྱ་བ་ལ། དེ་ལ་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་རྣམས་ཐམས་ཅད་ཀྱི་བག་ཆགས་ལ་བརྟེན་ནས་ཆོས་དེ་རྣམས་ཉིད་སྐྱེད་པའི་རྒྱུ་མཚན་གྱིས༌[^137]ས་བོན་ཡོངས་སུ་འཛིན་པ་ཞེས་བྱ་སྟེ། ནུས་པའི་བྱེ་བྲག་གོམས་པ་དང་ལྡན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 211]
འདི་དག་ནི་དེའི་རང་གི་མཚན་ཉིད་དོ། །

[Block 212 [HEADING]]
#### རྒྱུ་ཉིད་ཀྱི་མཚན་ཉིད། ^1-4-2-0

[Block 213]
དེས་ན༌[^138]རྒྱུ་ཉིད་ཀྱི་མཚན་ཉིད་ནི་ཀུན་ནས་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱི་བག་ཆགས་ལ་བརྟེན་ནས་དེ་སྐྱེས་པའི༌[^139]རྒྱུ་མཚན་གྱི་ས་བོན་ཡོངས་སུ་ལྡན་པ་སྟེ། རྣམ་པར་ཤེས་པ་གང་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་ཀྱིས་བསྒོ༌[^140]ཞིང་ནུས་པ༌[^141]ཁྱད་པར་ཅན་དུ་ཀུན་ཏུ་བསྒྲུབས་པ་གང་དེ་དག་ཉིད་སྐྱེད་པའི་རྒྱུ་མཚན་དེ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་རྒྱུ་ཉིད་ཀྱི་མཚན་ཉིད་དོ། །

[Block 214 [HEADING]]
#### འབྲས་བུ་ཉིད་དུ་རྣམ་པར་གཞག་པ། ^1-4-3-0

[Block 215]
དེ་ལ་འབྲས་བུ་ཉིད་དུ་རྣམ་པར་གཞག་པ་ནས་བརྩམས་ནས། ཐོག་མ་མེད་པའི་དུས་ཀྱི་བག་ཆགས་ལ་བརྟེན་ནས་བྱུང་བའོ་ཞེས་བྱ་བའི་བར་ལ། ཆོས་དེ་དག་རྣམས་ཀྱི་བག་ཆགས་ལ་བརྟེན་ནས་མངོན་པར་གྲུབ་པའི༌[^142]ཐོག་མ་མེད་པའི་དུས་ནས་བག་ཆགས་ཡོངས་སུ་བཟུང་བས་ཆོས་དེ་དག་དང་ལྷན་ཅིག་སྐྱེ་བ་དང་། འགག་པ་ལ་བརྟེན་ནས་གང་སྐྱེ་བའི་རྒྱུ་མཚན་འདི་ནི་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
