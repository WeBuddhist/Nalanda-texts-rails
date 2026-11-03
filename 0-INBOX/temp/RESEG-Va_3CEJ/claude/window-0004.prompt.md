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
[Block 141]
མ་ཟིན་པའི་འབྱུང་བ་ཆེན་པོའི་རྒྱུ་ལས་བྱུང་བ་ནི་འདི་ལྟ་སྟེ། རླུང་དང་། ནགས་ཚལ་དང་། ཆུའི་སྒྲ་ལྟ་བུའོ། །

[Block 142]
སེམས་ཅན་དུ་སྟོན་པ་ནི༌[^71]ངག་གི་རྣམ་པར་རིག་བྱེད་ཀྱི་སྒྲའོ། །

[Block 143]
གཞན་ནི་སེམས་ཅན་དུ་སྟོན་པ་མ་ཡིན་པའོ། །

[Block 144]
གཞན་དག་ན་རེ་ཟིན་པ་དང་། མ་ཟིན་པའི་འབྱུང་བ་ཆེན་པོའི་རྒྱུ་ལས་བྱུང་བའི་སྒྲ་ཡང་ཡོད་དེ། དཔེར་ན་ལག་པ་དང་རྫ་རྔ་ཕྲད་པ་ལས་སྐྱེས་པ་ལྟ་བུའོ་ཞེས་ཟེར་ཏེ། [^72]དེ་ནི་འདི་ལྟར་ཁ་དོག་གི་རྡུལ་ཕྲ་རབ་གཅིག་ལས་བྱུང་བ་བཞི་ཚན་གཉིས་རྒྱུར་བྱས་པར་མི་འདོད་པ་དེ་བཞིན་དུ་མི་འདོད་པར་བྱའོ། །

[Block 145]
སྒྲ་བཤད་ཟིན་ཏོ། །

[Block 146 [HEADING]]
###### **རོ།** ^1-1-3-1-2-3-0

[Block 147]
རོ་ནི་རྣམ་པ་དྲུག །མངར་བ་དང་། སྐྱུར་བ་དང་། ལན་ཚྭ་དང་། ཚ་བ་དང་། ཁ་བ་དང་། བསྐ་བའི་བྱེ་བྲག་གིས་སོ། །

[Block 148 [HEADING]]
###### **དྲི།** ^1-1-3-1-2-4-0

[Block 149]
དྲི་རྣམ་བཞི། དྲི་ཞིམ་པ་དང་། དྲི་ང་བ་རྣམ་པ་གཉིས། དྲི་མཉམ་པ་དང་། མི་མཉམ་པའི་ཕྱིར་རོ། །

[Block 150]
བསྟན་བཅོས་ལས་ནི་དྲི་ཞིམ་པ་དང་། དྲི་ང་བ་དང་། དྲི་མཉམ་པའོ་ཞེས་རྣམ་པ་གསུམ་འབྱུང་ངོ་། །

[Block 151 [HEADING]]
###### **རེག་བྱ།** ^1-1-3-1-2-5-0

[Block 152]
རེག་བྱ་བཅུ་གཅིག་བདག་ཉིད་དོ། །

[Block 153]
རེག་བྱ༌[^73]རྫས་ཀྱི་རང་བཞིན་ནི་བཅུ་གཅིག་སྟེ། འབྱུང་བ་ཆེན་པོ་བཞི་དག་དང་། འཇམ་པ་ཉིད་དང་། རྩུབ་པ་ཉིད་དང་། ལྕི་བ་ཉིད་དང་། ཡང་བ་ཉིད་དང་། གྲང་བ་དང་། བཀྲེས་པ་དང་། སྐོམ་པའོ། །

[Block 154]
དེ་ལ་འབྱུང་བ་རྣམས་ནི་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 155]
འཇམ་པ་ཉིད་ནི་མཉེན་པའོ། །

[Block 156]
རྩུབ་པ་ཉིད་ནི་རུད་རུད༌[^74]པའོ། །

[Block 157]
ལྕི་བ་ཉིད་ནི་གང་གིས་ན་དངོས་པོ་རྣམས་འཇལ་བར་བྱེད་པའོ། །

[Block 158]
བཟློག་པ་ནི་ཡང་བ་ཉིད་དོ། །

[Block 159]
གྲང་བ་ནི་དྲོ་བར་འདོད་པར་བྱེད་པའོ། །

[Block 160]
བཀྲེས་པ་ནི་ཟད་འདོད་པར་བྱེད་པའོ། །

[Block 161]
སྐོམ་པ་ནི་སྐོམ་འདོད་པར་བྱེད་པའོ། །

[Block 162]
རྒྱུ་ལ༌[^75]འབྲས་བུ་བཏགས་པའི་ཕྱིར་ཏེ་དཔེར་ན།

[Block 163 [VERSE]]
སངས་རྒྱས་རྣམས་ནི་འབྱུང་བ་བདེ། །
ཆོས་བསྟན་པ་ཡང་བདེ་བའོ། །
དགེ་འདུན་མཐུན་པ་བདེ་བ་ཡིན། །
མཐུན་པ་རྣམས་ཀྱི་དཀའ་ཐུབ་བདེ། །

[Block 164]
ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 165]
དེ་ལ་གཟུགས་ཀྱི་ཁམས་ན་ནི་བཀྲེས་པ་དང་སྐོམ་པ་མེད་དོ། །

[Block 166]
ལྷག་མ་ནི་ཡོད་དོ། །

[Block 167]
གལ་ཏེ་དེ་ནི་གོས་རེ་རེ་ནས་མི་འཇལ་ཡང་བསགས་པ་དག་ནི་འཇལ་ལོ། །

[Block 168]
གནོད་པར་བྱེད་པའི་གྲང་བ་མེད་ཀྱི་ཕན་པར་བྱེད་པ་ནི་ཡོད་དོ་ལོ། །

[Block 169 [HEADING]]
###### དེ་དག་ལ་ཇི་ལྟར་འཛིན་པ། ^1-1-3-1-3-0

[Block 170]
གང་འདི་གཟུགས་རྣམ་པ་མང་པོ་བཤད་པ་དེ་ལ་རེས་འགའ་ནི་རྫས་གཅིག་གིས་མིག་གི་རྣམ་པར་ཤེས་པ་སྐྱེད་དེ། གང་གི་ཚེ་དེའི་རྣམ་པ་བྱེ་བྲག་ཏུ་གཅོད་པར་འགྱུར་བ་ནའོ། །

[Block 171]
རེས་འགའ་ནི་མང་པོས་ཏེ། གང་གི་ཚེ་བྱེ་བྲག་ཏུ་མི་གཅོད་པ་ན་སྟེ། དཔེར་ན་ཐག་རིང་པོ་ནས་དམག་བཤམས་པ་འམ། ནོར་བུའི་ཚོགས་ཀྱི་ཁ་དོག་དང་དབྱིབས་དུ་མ་ལ་ལྟ་བ༌[^76]ལྟ་བུའོ། །

[Block 172]
རྣ་བ་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པ་ཡང་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 173]
ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་ཁ་ཅིག་ན་རེ་ཤིན་ཏུ་མང་ན་འབྱུང་བ་ཆེན་པོ་བཞི་དག་དང་། འཇམ་པ་ཉིད་ལ་སོགས་པ་གཅིག་དང་རེག་བྱ་ལྔས་སྐྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 174]
གཞན་དག་ན་རེ་བཅུ་གཅིག་པོ་ཐམས་ཅད་ཀྱིས་ཀྱང་སྐྱེད༌[^77]དོ་ཞེས་ཟེར་རོ། །

[Block 175]
དེ་ལྟ་ན་སྤྱི་ལ་དམིགས་པའི་ཕྱིར་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་པོ་དག་སྤྱིའི་ཡུལ་ཅན་དུ་འགྱུར་གྱི། རང་གི་མཚན་ཉིད་ཀྱི་ཡུལ་ཅན་མ་ཡིན་པ་མ་ཡིན་ནམ༌[^78]ཞེ་ན། འདི་དག་ནི་སྐྱེ་མཆེད་ཀྱི་རང་གི་མཚན་ཉིད་ཀྱི་ཡུལ་ཅན་དུ་འདོད་ཀྱི། རྫས་ཀྱི་རང་གི་མཚན་ཉིད་ཀྱི་ནི་མ་ཡིན་པས་ཉེས་པ་མེད་དོ། །

[Block 176]
འདི་དཔྱད་པར་བྱ་སྟེ། ལུས་དང་ལྕེའི་དབང་པོ་གཉིས་ཅིག་ཅར་དུ་ཡུལ་དང་ཕྲད་ན་རྣམ་པར་ཤེས་པ་གང་སྔར་སྐྱེ་ཞེ་ན། གང་གི་ཡུལ་ཤས༌[^79]ཆེ་བའོ། །

[Block 177]
ཡུལ་མཉམ་པ་དང་ཕྲད་ན་ནི་ལྕེའི་རྣམ་པར་ཤེས་པ་སྔར་སྐྱེ་སྟེ། ཟ་བར་འདོད་པས་རྒྱུད་གཏད་པའི་ཕྱིར་རོ། །

[Block 178]
དབང་པོ་ལྔ་དང་། དོན་ལྔ་དང་། དེ་དག་ལ་ཇི་ལྟར་འཛིན་པ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 179 [HEADING]]
###### རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ། ^1-1-3-1-4-0

[Block 180]
ད་ནི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་བསྙད་པར་བྱ་བ་དེ་བརྗོད་པར་བྱ་སྟེ།
--- END BLOCKS ---
