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
[Block 246]
སྡུག་བསྔལ་ཀུན་ལས་རབ་ཏུ་གྲོལ།[^142] །

[Block 247 [VERSE]]
ངག་རྣམས་བསྲུངས་ཤིང་ཡིད་ཀྱང་རབ་བསྡམས་ཏེ། །
ལུས་ཀྱིས༌[^143]མི་དགེ་བ་དག་མི་སྤྱོད་ཅིང་། །

[Block 248]
ལས་རྣམས་གསུམ་པོ་འདི་དག་རབ་སྦྱངས་ནས།[^144] །དྲང་སྲོང་གསུང་བའི་ལམ་ནི་ཐོབ་པར་འགྱུར། །ཞེས་གསུངས་པས་སློབ་པར་ཟད་དོ། །

[Block 249]
ལོ་བཅུ་གཉིས་འདས་ནས་བཅོམ་ལྡན་འདས་ཀྱི༌[^145]བསྟན་པ་ལ་སྐྱོན་དང་ཕན༌[^146]འབྱུང་ངོ་། །

[Block 250 [HEADING]]
### སྲོག་གཅོད་པའི་ཕས་ཕམ་པ། ^5-1-0

[Block 251]
དེ་ལ་དང་པོ་སྲོག་གཅོད་པའི་ཕས་ཕམ་པ་བཤད་དེ། དེ་ཡང་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཡུལ་བྲི་ཛིའི༌[^147]ལྗོངས་ཆུ་བོ་དགའ་སྐྱེད༌[^148]ཀྱི་འགྲམ་ཐང་ཤིང་གི་ནགས་སྟུག་བོ༌[^149]ན་བཞུགས་སོ། །

[Block 252]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་གི་དགེ་འདུན་ལ་མི་གཙང་བ་བསྒོམ་དུ་བཅུག་ནས་དགེ་སློང་དག་མི་གཙང་བ་ལ་བརྟེན་ནས་བསྒོམ་པ༌[^150]ལན་མང་དུ་བྱས་ནས་འབྲས་བུ་ཆེ་ཞིང་ལེགས་པ་ཆེན་པོར་འགྱུར་རོ་ཞེས་བསྔགས་པ་བརྗོད་པས། དགེ་སློང་རྣམས་ཀྱིས་མི་གཙང་བ་བསྒོམས་པས་ལུས་རྣག་ཅན་འདིས་ཡིད་བྱུང༌[^151]སྒྱིད་ལུག་སྟེ། རྣམ་པར་སྨོད༌[^152]ཅིང་མཚོན་གྱིས་ཀྱང་འདེབས། དུག་ཀྱང་ཟ། འགེགས་ཀྱང་འགེག །གཡང་དུ་ཡང་མཆོང་།[^153] དགེ་སློང་གིས་ཀྱང་དགེ་སློང་ཡང་གསོད།[^154] དེ་ནས་དགེ་སློང་ཞིག་ལུས་ལ་རྣམ་པར་སྨོད་ཅིང་རི་དགས་དབྱིག་པ༌[^155]ཅན་དགེ་སྦྱོང་སྲུང་བ༌[^156]ལ་འདི་སྐད་ཅེས་སྨྲའོ། །

[Block 253]
བཞིན་བཟངས་ང་སོད༌[^157]ཅིག་དང་ཆོས་གོས་ཀྱང་ཁྱོད་ཀྱིར་འགྱུར་རོ། །

[Block 254]
དེ་ནས་དབྱིག་པ་ཅན་གྱིས་དེའི་སྲོག་བཅད༌[^158]ནས་རལ་གྲི་ཁྲག་ཅན་ཆུ་བོ་དགའ་སྐྱེད༌[^159]ལ་འཁྲུའོ། །

[Block 255]
དེ་ནས་ལྷའི་བུའི་བདུད་ཅིག༌[^160]ཆུ་བོའི་རྒྱུན་ལ་མ་རེག་ཙམ་དུ་འདུག་ནས་དབྱུག་པ་ཅན་ལ་ལེགས་པའི་བསོད་ནམས་མང་དུ་སྤེལ་ལོ། །

[Block 256]
སེམས་ཅན་ནོ་ཞེས་བསྟོད་པས་དབྱིག་པ༌[^161]ཅན་ཡང་ཆོས་གོས་དང་ལྷུང་བཟེད་འདོད་པས་བསོད་ནམས་བྱའོ་སྙམ་ནས་རལ་གྲི་རྣོན་པོ་མཆན་དུ་བཅུག་སྟེ། གཙུག་ལག་ཁང་ནས་འཆག་སའི་བར་དུ་གཅིག་ནས་གཅིག་ཏུ་དགེ་སློང་དྲུག་ཅུའི་བར་དུ་སྲོག་བཅད་ནས་དགེ་སློང་རྣམས་ཉུང་ཞིང་འགྲིབས་པར་གྱུར་ཏོ། །

[Block 257]
དེ་ནས་བཅོམ་ལྡན་འདས་གསོ་སྦྱོང་བཅོ་ལྔ་པའི་ཚེ་དགེ་སློང་གི་དགེ་འདུན་ཐམས་ཅད་ལ་གཟིགས་ནས་ཚེ་དང་ལྡན་པ་ཀུན་དགའ་བོ་ལ་བཀའ་སྩལ་པ། རྒྱུ་རྐྱེན་གང་གིས་ད་ལྟ་ངའི་དགེ་སློང་ཉུང་ཞིང་འགྲིབས་པར་གྱུར་ཞེས་སྨྲས་པ་དང་ཇི་ལྟ་བུར་གྱུར་པ་རྒྱས་པར་གསོལ་ཏོ། །

[Block 258]
བཀའ་སྩལ་པ། ཀུན་དགའ་བོ་དགེ་སློང་གསོད་དམ། བཙུན་པ་འགུམས་ལགས་སོ། །

[Block 259]
བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་མ་ཡིན་ཞེས་རྣམ་གྲངས་དུ་མས་སྨད་ནས། ལེགས་པ་བཅུ་གཟིགས་པའི་ཕྱིར་བསླབ་པའི་གནས་བཅས་སོ། །

[Block 260]
གླེང་གཞི་ནི་ཡུལ་བྲི་ཛི། གང་ཟག་ནི་དབྱིག་པ༌[^162]ཅན་དགེ་སྦྱོང་སྲུང་། ཉོན་མོངས་པ་ནི་མི་བཟོད་པ། ཉེས་པ་ནི་གསོད་པ་དང་། དངོས་པོ་ནི་མིར་ཆགས་པའོ། །

[Block 261]
སྲོག་གཅོད་པའི་ཕས་ཕམ་པ་འདི་རྣམ་པ་གསུམ་གྱིས་བསྟན་ཏེ། ཕས་ཕམ་པའི་གནས་བསྟན་པ་དང་། སྦོམ་པོའི་གནས་བསྟན་པ་དང་། ཉེས་བྱས་ཀྱི༌[^163]གནས་བསྟན་པའོ། །

[Block 262 [HEADING]]
#### ཕས་ཕམ་པའི་གནས། ^5-1-1-0

[Block 263]
ཕས་ཕམ་པའི་གནས་བསྟན་པ་ལ་གསུམ་སྟེ། བདག་གིས་བསད་པ༌[^164]དང་། གཞན་གསོད་དུ་བཅུག་པ་དང་། ཐབས་ཀྱིས་བསད་པའོ། །

[Block 264 [HEADING]]
##### བདག་གིས་བསད་པ། ^5-1-1-1-0

[Block 265 [VERSE]]
བརྟུལ་ཞུགས་གནས་སེམས་མ་ཉམས་པས། །
ཆེད་དུ་བསམས་ཏེ་མ་ནོར་བར། །
མི་གཞན་བདག་གམ་གཞན་རྣམས་ཀྱིས། །
བསད༌[^165]ན་བརྟུལ་ཞུགས་ཉམས་པར་འགྱུར། །

[Block 266]
ཞེས་བྱ་བ་བདག་གིས་བསད་པ་དང་། གཞན་གྱིས་བསད་པ་བསྟན་ཏེ། བརྟུལ་ཞུགས་གནས་ཞེས་བྱ་བས་བསླབ་པ་ཉམས་པར་ཡང་མ་བྱས། བསླབ་པ་ཕུལ་ཡང་མ་ཕུལ་བ་ལ་བརྟུལ་ཞུགས་གནས་ཞེས་བྱའོ། །

[Block 267]
འདིར་རྣམ་པ་བཞི་བཞག་གོ།[^166] །བསླབ་པ་ཕུལ་ལ་ཉམས་པར་མ་བྱས་པ་དང་། བསླབ་པ་ཉམས་པར་བྱས་ལ་མ་ཕུལ་བ་དང་། བསླབ་པ་ཉམས་པར་ཡང་བྱས་ལ་ཕུལ་བ་དང་། བསླབ་པ་ཉམས་པར་ཡང་མ་བྱས་ཕུལ་ཡང་མ་ཕུལ་ལོ། །

[Block 268]
དེ་ལ་བསླབ་པ་ཕུལ་ལ་ཉམས་པར་མ་བྱས་པ་ནི་འདི་ལྟར་དགེ་སྦྱོང་ཆགས་པར་གྱུར་ཏམ་མི་དགའ་འམ། སླར་འབབ༌[^167]འདོད་དམ། དགེ་སྦྱོང་དོན་དུ་མི་གཉེར་བས་དགེ་སྦྱོང་གི་གན་དུ་སོང་ནས། ཚེ་དང་ལྡན་པ་དགོངས་ཤིག༌[^168]བདག་མིང་འདི་ཞེས་བགྱི་བ་བསླབ་པ་འབུལ་ལོ་ཞེས་ཟེར་བ་དང་། སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་འབུལ་བའམ། མཁན་པོ་དང་སློབ་དཔོན་འབུལ་ལོ་ཞེས་ཟེར་ན་བསླབ་པ་ཕུལ་ལོ་ཞེས་བྱའོ། །

[Block 269]
བདག་ཁྱིམ་པ་ཡིན་ནོ་ཞེ་འམ། དགེ་བསྙེན་ཡིན་ནོ་ཞེ་འམ། མཚམས་མེད་པ་ལྔ་བྱས་པའམ། མུ་སྟེགས་ཅན་ནམ། ཚངས་པ༌[^169]མཚུངས་པར་སྤྱོད་པ་ཁྱེད་དང་ལྷན་ཅིག་འགྲོགས་སུ་མ་དགོངས་སོ་ཞེས་ཟེར་ན་བསླབ་པ་ཕུལ་བ་ཡིན་ཏེ། བསླབ་པ་ཉམས་པར་བྱས་པ་མ་ཡིན་ནོ། །

[Block 270]
ཇི་ལྟར་བསླབ་པ་ཉམས་པར་ནི་བྱས་ལ་བསླབ་པ་ཕུལ་བ་མ་ཡིན་ཞེ་ན། འདི་ལྟར་དགེ་སྦྱོང་ཆགས་ཤིང་མི་དགའ་སྟེ་འབབ༌[^170]པར་འདོད་ནས་མཁྱེན་པར་མཛོད་ཅིག་ཚངས་པར་སྤྱད་པས༌[^171]རབ་ཏུ་དབེན་པ་དང་། དགོན་པ་ནི་སྤྱད་དཀའོ། །

[Block 271]
ཕ་མ་བུ་སྲིང་ཕུ་ནུ་མཁན་པོ་དྲན་ནོ། །

[Block 272]
བདག་བཟོ་སློབ་བོ། །

[Block 273]
བདག་དགའ་བའི་རིགས་རྣམས་ལ་གཏོད་ཅིག །བབས་པའི་རྟགས་སྨྲས་ཀྱང་བསླབ་པ་འབུལ་ཞེས་མ་སྨྲས་ན་བསླབ་པ་ཉམས་པར་བྱས་ཀྱི་ཕུལ་བ་མ་ཡིན་ནོ། །ཇི་ལྟར་བསླབ་པ་ཉམས་པར་ཡང་བྱས་ཕུལ་བ་ཡང་ཡིན་ཞེ་ན། དགེ་སྦྱོང་ཆགས་ཤིང་འབབ༌[^172]པར་འདོད་པས་ཚངས་པར་སྤྱོད་པ་དང་དགོན་པ་ནི་དཀའོ། །

[Block 274]
ཕ་དང་མ་དང་མཁན་པོ་ལ་སོགས་པ་དྲན་ན་བདག་དགའ་བའི༌[^173]རིགས་ལ་གཏོད་ཅིག་ཅེས་སྨྲ་ཞིང་ཚིག་གིས་གོ་བར་བསླབ་པ་འབུལ་ཞེས་ཟེར་ན་བསླབ་པ་ཉམས་པར་ཡང་བྱས་ལ་བསླབ་པ་ཕུལ་བ་ཡང་ཡིན་ནོ། །

[Block 275]
ཇི་ལྟར་བསླབ་པ་ཉམས་པར་ཡང་མ་བྱས་ལ་ཕུལ་བ་ཡང་མ་ཡིན་ཞེ་ན། ཉམས་པའི་ཚིག་ཀྱང་མ་སྨྲས་འབུལ་བའི་ཚིག་ཀྱང་མ་སྨྲས་པའོ། །

[Block 276]
དེ་ལ་བསླབ་པ་མ་ཕུལ་ཡང་ཉམས་པར་བྱས་པས་ཀྱང་བསླབ་པ་ཉམས་པ་དང་ཕུལ་བར་འགྱུར་རོ། །

[Block 277]
བསླབ་པ་མ་ཕུལ་བ་ལས་ཉམས་པར་བྱས་པ་དང་། བསླབ་པ་ཕུལ་ཡང་མ་ཕུལ་ལ་ཉམས་པར་ཡང་མ་བྱས་པས་ནི་ཕུལ་བར་མི་འགྱུར་རོ། །

[Block 278]
སེམས་ཉམས་པས་ཞེས་བྱ་བ་ལ་སེམས་ཉམས་པ་ནི་སྨྱོས་ཏེ་མི་དྲན་པ་ལ་བྱ་སྟེ། བདག་སྨྱོས་ཀྱང་མ་སྨྱོས་ཏེ་དྲན་བཞིན་དུ་བསད་ན་ཕས་ཕམ་པར་འགྱུར་རོ། །

[Block 279]
སྨྱོས་ཏེ་མི་དྲན་པར་གྱུར་ནས་བསད་ན་ནི་ཕས་ཕམ་པར་མི་འགྱུར་རོ། །

[Block 280]
ཆེད་དུ་བསམས་ཏེ་ཞེས་བྱ་བ་ལ་བསད་པར་ནི་མ་བསམས་ཀྱི་རྩེད་མོ་ལ་སོགས་པ་བྱེད་བྱེད་དེ་ཤི་ནས་ཕས་ཕམ་པར་མི་འགྱུར་གྱི། ཆེད་དུ་གསད་པར༌[^174]བསམས་ཏེ་ཤི་ནས་ཕམ་པར་འགྱུར་རོ། །

[Block 281]
མ་ནོར་བ་ཞེས་བྱ་བ་ལ་ཡང་མི་རྣམ་པ་གསུམ་བསད་ན་ཕས་ཕམ་པར་འགྱུར་བ་ལས།

[Block 282]
བདག་ཀྱང་མིའི་རྒྱུད་དུ་གཏོགས་པ་ཡིན་ཏེ། བདག་གིས་བདག་བསད་པ་ན་ཕས་ཕམ་པར་མི་འགྱུར་གྱི་བདག་གིས་གཞན་བསད་ན་ཕས་ཕམ་པར་འགྱུར་རོ། །

[Block 283]
བདག་གིས་གཞན་བསད་ན་བརྟུལ་ཞུགས་ཉམས་པར་འགྱུར་ཞེས་བྱ་བར་སྦྱར་ཏེ། བདག་ཉིད་ཀྱིས་ལག་དར་ཏེ༌[^175]མི་རྣམ་པ་གསུམ་བསད་ན་བརྟུལ་ཞུགས་ཉམས་པར་འགྱུར་ཏེ་ཕས་ཕམ་པ་འབྱུང༌[^176]བས་དགེ་སྦྱོང་དུ་མི་རུང་ཞིང་འཕགས་པའི་བདེན་པ་མཐོང་བ་དང་མྱ་ངན་ལས་འདས་པ་ཐོབ་པའི་སྐལ་བ་མེད་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 284 [HEADING]]
###### ཟིན་པའི་ལུས་སུ་གཏོགས་པ། ^5-1-1-1-1-0

[Block 285]
དེ་ལ་བདག་གིས་བསད་པ་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཟིན་པའི་ལུས་སུ་གཏོགས་པ་དང་། ཕྱི༌[^177]རོལ་གྱིས༌[^178]འཕངས་པ་དང་། གཉིས་ཀ་དང༌[^179]ཡང་ལྡན་པའོ། །ཇི་ལྟར་ཟིན་པའི་ལུས་སུ་གཏོགས་པས་ཤེ་ན། དགེ་སྦྱོང་གིས་གསད༌[^180]སེམས་ཀྱིས་སྐྱེས་པ་དང་། བུད་མེད་དམ༌[^181]མ་ནིང་ཁུ་ཚུར་རམ་རྡོ་འམ་ཐ་ན་སོར་མོ་གཅིག་བསྣུན་ཏེ། ཤི་བར་གྱུར་ཅིག་སྙམ་པ་ལས་དེ་ཉིད་ཀྱི་ཚེའམ་ཕྱིས་ཤི་བར་གྱུར་ན་ནི་ཕས་ཕམ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
