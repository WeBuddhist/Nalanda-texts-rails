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
[Block 1121 [VERSE]]
གལ་ཏེ་བློ་དེས་གཟུགས་འཛིན་ན། །
རང་གི་རང་བཞིན་ལ་འཛིན་འགྱུར། །
རྐྱེན་ལས་སྐྱེས་པས་ཡོད་མིན་ལ། །
ཡང་དག་གཟུགས་མེད་ཇི་ལྟར་འཛིན། །

[Block 1122]
འདིར་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་འཛིན་ན་སྔོན་དུ་རང་གི་བདག་ཉིད་མཐོང་སྟེ། འདི་ལྟ་སྟེ། མེའི་དྲོ་བ་ཉིད་ལྟ་བུ་དེ་དང་ལྡན་པ་ལས་ཕ་རོལ་གྱི་བདག་ཉིད་ཀྱང་ཉེ་བར་དམིགས་པར་བྱེད་དོ།[^810] །ཆུ་ལྟ་བུའོ། །

[Block 1123]
དེ་ལྟར་གལ་ཏེ་བློ་ནི་འཛིན་པའི་རང་བཞིན་དུ་འགྱུར་ན། དེ་ནི་འཛིན་པའི་རང་གི་བདག་ཉིད་ཁོ་ན་ལ་རེ་ཞིག་ཉེ་བར་དམིགས་པར་འགྱུར་ལ། དམིགས་པ་ཡང་མ་ཡིན་ཏེ། བདག་ཉིད་ལ་འཇུག་པ་དང་འགལ་བའི་ཕྱིར་དང་། ལས་དང་བྱེད་པ་པོ་དག་གཅིག་ཉིད་དུ་ཐལ་བ་དང་། དམིགས་པ་མེད་པར་དམིགས་པ་པོ་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 1124]
གང་གི་ཚེ་འདི་ལྟར་བློ་རང་གི་བདག་ཉིད་ལ་འཛིན་པར་མི་ནུས་པ་དེའི་ཚེ། འདིར་གཟུགས་ཇི་ལྟར་འཛིན་པར་བྱེད། རིགས་པས་ནི་རང་གི་བདག་ཉིད་མི་འཛིན་པའི་ཕྱིར་གཟུགས་ཀྱང་མི་འཛིན་ཏེ། བོང་བ་ལ་སོགས་པ་བཞིན་ནོ་ཞེས་བྱའོ། །

[Block 1125]
གཞན་ཡང་འདིའི་བློ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཕྱིར་ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་པའོ། །

[Block 1126]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཕྱིར་ཡང་རང་བཞིན་གྱིས་ཡོད་པ་མ་ཡིན་པའི་གཟུགས་ཇི་ལྟར་འཛིན་པར་འགྱུར། དེས་ན་གཟུགས་འཛིན་པ་མེད་དོ།། །།

[Block 1127]
འདི་ལྟར་ཡང་འཛིན་པ་མེད་དེ། གང་གི་ཕྱིར།

[Block 1128 [HEADING]]
### ཚིགས་བཅད་ཞེ་དགུ་པ། ^1-49-0

[Block 1129 [VERSE]]
ཇི་སྐད་སྨོས་པ༌[^811]གཟུགས་སྐྱེས༌[^812]བློས། །
སྐད་ཅིག་སྐད་ཅིག་གིས་མི་འཛིན། །
འདས་དང་མ་འོངས་པ་གཟུགས་ཀྱང་། །
དེ་ཡིས་ཇི་ལྟར་རྟོགས་པར་འགྱུར། །

[Block 1130]
ཇི་སྐད་སྨོས་པའི་གཟུགས་ཞེས་པ་ལ། ཇི་སྐད༌[^813]དུ་བཤད་པའི་གཟུགས་ལ་སྨོས་པ་ཞེས་བརྗོད། འདིར་མིག་གི་ཡུལ་ནི་ཇི་སྐད་སྨོས་པའི་གཟུགས་སུ་ཤེས་པར་བྱ་ལ། བློ་ཡང་མིག་གི་བློས༌[^814]འཛིན་གྱི༌[^815]གཞན་མ་ཡིན་ནོ། །

[Block 1131]
སྐྱེས་པའི་སྒྲ་ནི་འདིར་ད་ལྟར་བའི་རྗོད༌[^816]དུ་ཤེས་པར་བྱའོ། །

[Block 1132]
འདིར་གལ་ཏེ་བློ་ཡིས་གཟུགས་ལ་འཛིན་པར་བྱེད་ན། དེས་ད་ལྟར་བའི་གཟུགས་ལ་འཛིན་ནམ། འདས་པ་དང་མ་འོངས་པ་ལའོ། །

[Block 1133]
དེ་ལ་རེ་ཞིག་ཇི་སྐད་སྨོས་པའི་རྣམ་པས༌[^817]ནི། ད་ལྟར་བའི་གཟུགས་ད་ལྟར་བའི་བློས་མི་འཛིན་ཏེ། གཉི་ག་ཡང་སྐད་ཅིག་མའི་ཕྱིར་སྐྱེས་མ་ཐག་ཏུ་རྣམ་པར་འཇིག་པའི་བློ་ནི་དེ་ལ་སྐད་ཅིག་ཙམ་ཡང་གནས་པ་མེད་ན། གང་ལས་འདིས་ཡུལ་ལ་འཛིན་པ་སྲིད་པར་འགྱུར། བསྐྱེད་པར་བྱ་བ་ལ་འཛིན་ནོ་ཞེ་ན། དེ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། བསྐྱེད་པར་བྱ་བ་ནི་མ་འོངས་པ་ཡིན་ལ། དེ་ཡང་མ་སྐྱེས་པར་གྱུར་པའི་གཟུགས་ཇི་ལྟར་འཛིན་པར་འགྱུར། གཟུགས་ཀྱང་སྐྱེས་མ་ཐག་ཏུ་རྣམ་པར་འཇིག་པས་སྐད་ཅིག་ཙམ་ཡང་གནས་པ་མེད་ན། གང་ལས༌[^818]འཛིན་པར་བྱེད། དེ་ནི་འདི་ལྟར་སྐད་ཅིག་མའི་བློ་ལ་ཇི་སྐད་སྨོས་པའི་གཟུགས་སྐྱེས་པའི་སྐད་ཅིག་མ་ལ་མི་འཛིན་ནོ། །

[Block 1134]
ཡང་ན་འདི་སྙམ་དུ་སེམས་ན། སྐད་ཅིག་མའི་ཕྱིར་ད་ལྟར་བའི་གཟུགས་མི་འཛིན་ལ། དེ་ལྟ་ན་ཡང་འདས་པ་དང་མ་འོངས་པ་ལ་ཇི་ལྟར་འཛིན་པར་མི་འགྱུར་ཞེ་ན། སྨྲས་པ། གང་གི་ཚེ་ད་ལྟར་བའི་དངོས་པོ་ཉིད་སྐད་ཅིག་མའི་ཕྱིར་འཛིན་པར་མི་ནུས་ན། དེའི་ཚེ་ཇི་ལྟར་རྣམ་པ་ཐམས་ཅད་དུ་ཡོད་བཞིན་པ་མ་ཡིན་པའི་ཞིག་པ་དང་མ་སྐྱེས་པ་བློས་འཛིན་པར་ནུས། དེ་ལྟར་རེ་ཞིག་འཛིན་པ་མི་སྲིད་པ་དེས་ན་ཡང་གཟུགས་མེད་དོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1135 [HEADING]]
### ཚིགས་བཅད་ལྔ་བཅུ་པ། ^1-50-0

[Block 1136 [VERSE]]
གང་ཚེ་ནམ་ཡང་ཁ་དོག་དང་། །
དབྱིབས་དག་ཐ་དད་ཉིད་མེད་པས། །
དེ་དག་ཐ་དད་འཛིན་ཡོད་མིན། །
གཅིག་ཏུའང་མ་ཡིན་གྲགས་པའི་གཟུགས། །

[Block 1137]
གལ༌[^819]ཏེ་མིག་གི་ཡུལ་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ཅེས་བྱ་བ་ཅུང་ཟད་ཡོད་ན་དེ་འཛིན་པར་འགྱུར་གྲང་ན། ཡོད་པ་ཡང་མ་ཡིན་ལ། དེ༌[^820]ཡོད་བཞིན་པ་མ་ཡིན་པ་ནི་གང་གི་ཕྱིར་མི་འཛིན་ནོ། །

[Block 1138]
ཇི་ལྟར་ཡང་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ཡོད་བཞིན་པ་མ་ཡིན་ཞེ་ན། སྨྲས་པ། འདིར་ཁ་དོག་དང་དབྱིབས་དག་ལ་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ཅེས་བྱ་བ་ལ། ཁ་དོག་དང་དབྱིབས་འདི་དག་ནི་གཅིག་ཉིད་དུ་གྱུར་པས་སམ། ཐ་དད་པ་ཉིད་དུའོ། །

[Block 1139]
རེ་ཞིག༌[^821]ཁ་དོག་དང་དབྱིབས་དག་ཐ་དད་པ་ཉིད་དུ་མེད་ལ། གལ་ཏེ་ཡོད་ན་ཕན་ཚུན་མ་ལྟོས་པར་འཛིན་པར་འགྱུར་ལ། འདི་དག་ཀྱང་ཁ་དོག་ལས་ཐ་དད་པའི་དབྱིབས་འཛིན་པར་མི་ནུས་ཏེ། བུམ་པ་ལས་སྣམ་བུ་ལྟ་བུ་མ་ཡིན་ལ་དེ་བཞིན་དུ་དབྱིབས་ལས་ཐ་དད་པའི་ཁ་དོག་འཛིན་པར་མི་ནུས་སོ། །

[Block 1140]
གདོན་མི་ཟ་བར་དབྱིབས་གང་ཡང་རུང་བ་ལ་དེའི་ཁ་དོག་འབྱུང་བར་འགྱུར་ལ། གང་ཡང་འདིའི་གནས་ལུགས་ལ་དེའི་དབྱིབས་ཞེས་བྱ་སྟེ། དབྱིབས་ལས་ཐ་དད་པའི་ཁ་དོག་ལོགས་སུ་གྲུབ་པར་མི་སྲིད་དོ་ཞེས་བྱའོ། །

[Block 1141]
དེ་འདི་ལྟར་ཐ་དད་པ་ཉིད་ན། གང་གི་ཚེ་ཁ་དོག་ནམ་ཡང་དབྱིབས་ལ་མི་སྲིད་ལ། དེས་ན་དེ་དག་ཐ་དད་པར་འཛིན་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1142]
ཡང་ན་འདི་སྙམ་དུ་སེམས་ན། གལ་ཏེ་ཐ་དད་དུ་མ་གྲུབ་པའི་ཕྱིར་ཁ་དོག་དང་དབྱིབས་དག་ཐ་དད་དུ་མི་འཛིན་ལ། དེ་ལྟ་ན་ཡང་གཅིག་ཏུ་གྱུར་པ་འདྲེན་མའི་དངོས་པོར་དེ་དག་འཛིན་པར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། སོ་སོ་སོ་སོར་མ་གྲུབ་པ་དག་འདྲེན་མའི་དངོས་པོར་མེད་པས་འདི་དག་གཅིག་ཏུ་ག་ལ་ཞིག །དེའི་ཕྱིར་དེ་དག་གང་གཅིག་ཏུ་འཛིན་པ་མི་སྲིད་དོ། །

[Block 1143]
ཁ་དོག་དང་དབྱིབས་ལས་གཞན་དུ་གཟུགས་མི་དམིགས་ལ། གང་གི་ཕྱིར་དེ་ཡང་ཕ་རོལ་པོས་གཟུགས་ན་ཁ་དོག་དང་དབྱིབས་ཀྱི་བདག་ཉིད་དོ་ཞེས་གྲགས་པ་དེ་དག་ཀྱང་མི་འཛིན་ནོ་ཞེས་བསྒྲུབས་སོ་ཞེས་བྱ་སྟེ། དེས་ན་མི་འཛིན་པའི་ཕྱིར་གཟུགས་མེད་དོ། །

[Block 1144]
ཡང་ན་གལ་ཏེ་ཡང་འཛིན་པ་མེད་པས་གཟུགས་མེད་པར་འགྱུར་ལ། དེ་ལྟ་ན་ཡང་མིག་གི་བློ་རེ་ཞིག་ཡོད་དེ་དེ་མ་བཀག་པའི་ཕྱིར་ལ། དེ་ཡང་གཟུགས་མེད་ན་མི་འབྱུང་ངོ་ཞེས་བྱ་སྟེ། དེའི་ཕྱིར་གཟུགས་ཀྱང་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་མིག་གི་བློ་ཡོད་ན་གཟུགས་ཡོད་པར་འགྱུར་ན། ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བསྒྲུབ་པའི༌[^822]ཕྱིར་གསུངས་པ།

[Block 1145 [HEADING]]
### ཚིགས་བཅད་ང་གཅིག་པ། ^1-51-0

[Block 1146 [VERSE]]
མིག་བློ་མིག་ལ་ཡོད་མ་ཡིན། །
གཟུགས་ལ་ཡོད་མིན་བར་ན་མེད། །
གཟུགས་དང་མིག་ལ་བརྟེན་ནས་སུ། །
ལེགས་སོ་ལོག་པར་ཡོངས་བརྟགས་པ། །

[Block 1147]
འདིར་མིག་གི་བློ་མིག་དང་གཟུགས་ལ་བརྟེན་ནས་སྐྱེའོ༌[^823]ཞེས་རྣམ་པར་འཇོག་པ་ཉིད་རྣམ་པར་དཔྱད་པར་བྱ་སྟེ། ཅི་མིག་གི་བློ་འདི་མིག་ལ་ཡོད་དམ། དེ་ནི་གཟུགས་ཅན་མ་ཡིན་པའི་ཕྱིར་ཡུལ་ན་གནས་པ་མ་ཡིན་པས་དེའི་ཕྱིར་དེ་མིག་ལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1148]
ཇི་ལྟར་མིག་ལ་མེད་པ་དེ་བཞིན་དུ་གཟུགས་ལ་ཡང་མེད་ལ། མིག་དང་གཟུགས་དེ་དག་གི་བར་དུ་ཡང་མི་སྲིད་དེ། ཡུལ་ན་མི་གནས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1149]
གང་ཡང་དེའི་ཚེ་མིག་གི་བློ་མིག་ལ་མ་ཡིན། གཟུགས་ལ་ཡང་མ་ཡིན། བར་ན་ཡང་མ་ཡིན་པས་དེའི་ཚེ་རྣམ་པ་ཐམས་ཅད་དུ་ཡོད་པ་མ་ཡིན་པ་ཉིད་དེ་ཇི་ལྟར་ཡོད་དོ་ཞེས་སྨྲ་བར་རུང་སྟེ། འདི་ནི་མེད་པ་ཉིད་དོ་ཞེས་བྱའོ། །

[Block 1150]
སྨྲས་པ། གལ་ཏེ་ཡང་དེ་མིག་ལ་མེད༌[^824]ཅིང་གཟུགས་དང་བར་ན་ཡང་མེད་ཀྱང་། དེ་ལྟ་ན་ཡང་མིག་དང་གཟུགས་ལ་བརྟེན་ནས་སྐྱེ་བ་ཡོད་པས། དེའི་ཕྱིར་མིག་གི་བློ་ཡང་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། གང་གང་ན་མི་གནས་པ་ཇི་ལྟར་དེ་ལས་སྐྱེ། ཡང་ན་དེ་ལྟར་འགྱུར་ན་ཐམས་ཅད་ལས་ཐམས་ཅད་སྐྱེ་བར་འགྱུར་ན་དེ་དག་ནི་མེད་ལ། མིང་དང་གཟུགས་ལ་བརྟེན་ནས་མིག་གི་བློ་སྐྱེའོ་ཞེས་སྨྲ་ན་ཡང་། དེས་ན་འདི་ནི་ཡང་དག་པར་མི་སྐྱེ་སྟེ། སྐྱེ་བ་རིགས་པ་དང་མི་ལྡན་པའི་ཕྱིར་རོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1151]
མིག་དང་གཟུགས་ལ་བརྟེན་ནས་སུ། །ལེགས་སོ་ལོག་པར་ཡོངས་བརྟགས་པ། །ཞེས་པ་ལ། གང་གི༌[^825]བདག་ཉིད་ཀྱིས་སོ་སོར་སྣང་བ་དེའི་བདག་ཉིད་ལ་བརྟགས་ན་མི་སྲིད་པས་ན་དེ་ཉིད་ཀྱིས་ན།

[Block 1152]
རྣམ་ཤེས་སྒྱུ་མ་ལྟ་བུ་ཡང་། །ཉི་མའི་གཉེན་གྱིས་གསུངས་པའོ། །ཞེས་མདོ་ལས་གསུངས་སོ་ཞེས་བྱའོ། །

[Block 1153]
དེ་ནི་དེ་ལྟར་མིག་གི་བློ་མི་སྲིད་པའི་ཕྱིར་མི་བཟུང་བས༌[^826]གཟུགས་མེད་དོ། །

[Block 1154]
འདིར་སྨྲས་པ། གཟུགས་འཛིན་པ་ཉིད་དེ། དེ་ལ་འཛིན་པ་པོ་མིག་གི་དབང་པོ་ཡོད་པའི་ཕྱིར་ན་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ཏེ། མིག་གིས་གཟུགས་མཐོང་བས་ཡིད་བདེ་བའི་གནས་ལ་མངོན་པར་ཞེན་ནོ་ཞེས་པ་ལ་སོགས་པའོ། །

[Block 1155]
སྨྲས་པ། གལ་ཏེ་མིག་རང་གི་བདག་ཉིད་མཐོང་ན་གཟུགས་འཛིན་པར་འགྱུར་ལ། མཐོང་བ་ནི་མ་ཡིན་ཏེ།

[Block 1156 [HEADING]]
### ཚིགས་བཅད་ང་གཉིས་པ། ^1-52-0

[Block 1157 [VERSE]]
གལ་ཏེ་མིག་གིས༌[^827]བདག་མཐོང་མིན། །
དེས་གཟུགས་མཐོང་བ༌[^828]ཇི་ལྟར་འགྱུར། །
དེ་ཕྱིར་མིག་དང་གཟུགས་བདག་མེད། །
དེ་བཞིན་སྐྱེ་མཆེད་ལྷག་མ་རྣམས། །

[Block 1158]
གལ་ཏེ་མིག་གིས་བདག་ཉིད་མི་མཐོང་ལ། དེའི་ཚེ་རང་གི༌[^829]བདག་ཉིད་མ་མཐོང་བས་བོང་བ་ལ་སོགས་པ་བཞིན་དུ་གཟུགས་ཀྱང་མི་མཐོང་ལ། དེ་ནི་བོང་བ་ལ་སོགས་པ་བཞིན་པས་མིག་ཉིད་དུ་མི་འགྱུར་རོ་ཞེས་སྒྲུབ་པར་བྱེད་ན་དེ། [^830]དེ་ཕྱིར་མིག་བདག་མེད་ཅེས་པ་ལ། གང་གི་ཕྱིར་མིག་གིས་གཟུགས་མི་མཐོང་བ་དེའི་ཕྱིར་རང་བཞིན་མེད་དོ། །

[Block 1159]
མིག་མེད་ན་མིག་དང་དེ་ལ་བརྟེན་པའི་མིག་གི༌[^831]བློ་མེད་པས་གཟུང་བ་མེད་པའི་ཕྱིར། གཟུགས་ནི་ཤིན་ཏུ་ཡང་རང་བཞིན་མེད་དོ། །

[Block 1160]
ཇི་ལྟར་མིག་དང་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དག་རང་བཞིན་མེད་པ་ཉིད་ལྟར། དེ་བཞིན་སྐྱེ་མཆེད་ལྷག་མ་རྣམས་ནི། སྐྱེ་མཆེད་ཐམས་ཅད་མིག་དང་གཟུགས་བཞིན་དུ་རང་བཞིན་ཡིན་པར༌[^832]ཁོང་དུ་ཆུད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
