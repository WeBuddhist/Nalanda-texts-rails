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
[Block 1121]
དམག་ལ་ལྟ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1122]
གང་དུ་དམག་གི་ནང་དུ་གནས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེ་དག་མེད་པར་དེར་ཉིན་མཚན་གཉིས་ལས་ལྷག་པར་འདུག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དག་མེད་པར་ཞེས་བྱ་བ་ནི་རྒྱལ་པོ་ལ་སོགས་པས་བཀུག་པ་དང་བར་ཆད་ཉེ་བར་བྱུང་བའི་དབང་ཉིད་དོ། །

[Block 1123]
དེར་ཞེས་བྱ་བ་ནི་གཡུལ་ལ་མངོན་པར་དགའ་བའི་དམག་ལའོ། །

[Block 1124]
ཉིན་མཚན་གཉིས་ལས་ཞེས་བྱ་བ་ནི་ཉིན་མོ་དང་མཚན་མོ༌[^676]དག་ལའོ། །

[Block 1125]
དེ་ལས་གང༌[^677]དུ་ལྷག་པར་འདུག་ནའོ་ཞེས་བྱ་བ་འདི་ནི་ཉིན་མཚན་དག་གོ། །

[Block 1126]
ཉིན་མཚན་གྱི་མཐར་ཡང་འདུལ་བའི་ཐ་སྙད་དོ། །

[Block 1127]
དེ་བས་ན་འདི་ལ་ཡང་དངོས་གཞིའི་རྣམ་པར་གཞག་པའོ། །

[Block 1128]
འདིར་ཡང་གང་ཞིག་རྣམ་པར་གནས་པ་ལ་སྐད་ཅིག་མའི་རྗེས་སུ་མཐུན་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1129]
དེའི་ཕྱིར་འདིར་སྦྱོར་བ་ཐོབ་པ་འདུན་ནས་རྣམ་པར་གནས་པ་ཡིན་གྱི་ལྟུང་བ་མེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1130]
ཁ་ན་མ་ཐོ་བ་དང་བཅས་པའི་རྗེས་སུ་སྒྲུབ་པ༌[^678]ལ་དུས་ནམ་གྱི་ཚེ་བྱས་པ་ཁ་ན་མ་ཐོ་བ་མེད་པ་མ་ཡིན་ནོ། །

[Block 1131]
ཉིན་མཚན་གཞན་པོ་འདི་ལ་ནི་ཉིན་མཚན་གཞན་ལ་ཞུགས་པ་ཡང་མ་ཡིན་ཏེ། དེ་བས་ན༌[^679]ཉིན་མཚན་སོ་སོར་འདིར་ཁ་ན་མ་ཐོ་བར་རིག་པར་བྱའོ། །

[Block 1132]
དགོས་པ་མེད་ན་སྔ་མ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རིགས་པའི་ཚུལ་གྱིས་དགོས་པ་མེད་ན་སྔ་མ་ཡང་ཉིན་ཞག་གསུམ་པར་འདུག་པ་ལས་གནས་པ་གང་ཡིན་པ་དེ་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1133]
མཐར་ནི་དངོས་གཞི་སྟེ་སྔ་རོལ་དུ་ནི་ཉེས་བྱས་ཞེས་བྱ་བ་འདི་ལ་འདིར་སྔ་མ་བཞིན་དུ་རྟོགས་པར་བྱའོ། །

[Block 1134]
འདིར་གཞུང་ནི་དགེ་སློང་ལ་དེ་འདྲ་བའི་རྐྱེན་ཡོད་པར་གྱུར་ན་རྩོམ་པའི་དམག་ལ་ལྟ་བའི་ཕྱིར་ཉེ་བར་འགྲོ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1135]
ལེགས་པའི་ངོ་བོ་འདོད་པའི་དོན་མེད་པ་ན་དམག་གི་ནང་དུ་སོ་སོར་ཉམས་སུ་མྱོང་བར་བྱ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་གསུངས་པ་དེའི་ཚིག་གི་བརྗོད་པའོ། །

[Block 1136]
དམག་གི་ནང་ན་གནས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1137]
དཔུང་གི་ཡན་ལག་རྣམས་ནི་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གཡུལ་ལ་མངོན་པར་དགའ་བའི་དམག་གི་དཔུང་གི་ཡན་ལག་གླང་པོ་ཆེ་དང་རྟ་དང་ཤིང་རྟ་དང་རྐང་ཐང་དང་རྒྱལ་མཚན་ལ་སོགས་པ་རྣམས་ཀྱི༌[^680]དམག་ལ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1138]
འདིར་མཚོན་པའི་ནི་བརྩམས་པའི་གཡུལ་ངོ་རྣམས་ཀྱི་ཡན་ལག་ཏུ་རྣམ་པར་གནས་པ་ཡིན་ཞེས་བྱ་བ་ཐམས་ཅད་ཁོངས་སུ་བསྡུ་བའོ། །ཅི་དེ་ཐམས་ཅད་ལ་འདི་རྣམས་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་བར་ཆད་ཀྱི་དབང་གིས་འགྲོ་བ་མ་ཡིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྤངས་ནས་ཞེས་བྱ་བ་བརྗོད་པ་དག་ལ་ལྟུང་བ་མེད་དོ། །

[Block 1139]
རྒྱུ་དག་ལས་གཅིག་ནི་འདིར་རྒྱུ་ཉིད་དེ་བར་ཆད་ཀྱི་དབང་གིས་ལྟུང་བ་ཉིད་དེ། རྒྱལ་པོ་ལ་སོགས་པ་ལས་སྨོས་པ་ལས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1140]
འདིར་གཞུང་ནི་བར་ཆད་བརྒྱད་པོ་དག་ལས་བར་ཆད་གང་ཡང་རུང་བ་ཉེ་བར་གནས་པར་གྱུར་ན་ཉེས་པ་མེད་དོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 1141]
དེ་ཡང་དེ་ཙམ་དུ་ཟད་ཀྱི༌[^681]གནོད་པ་ཐམས་ཅད་ཉེ་བར་ཞི་བར་བྱ་བའི་དོན་དུ་འགྲོ་བ་ལ་ཡང་འདིར་ཉེས་པ་མེད་པ༌[^682]ལ་སྦྱོར་བ་ཞེས་བྱ་བ་ནི་བར་ཆད་ཙམ་ལ་ཡང་དག་པར་བརྟེན་པའོ། །

[Block 1142]
བསྡུས་པ་དང་སོ་སོ༌[^683]དག་གོ་ཞེས་བྱ་བ་ནི་གཡུལ་གྱི་ཡན་ལག་རྣམས་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1143]
དཔུང་གི་ཚོགས་སམ༌[^684]དམག་གི་ཚོགས་ཡང་དག་པར་བསྟན་པ་ཞེས་བྱ་བ་འདི་ལ་ཐམས་ཅད་དུ་བཟུང་ནས་བསྡུས་པའོ། །

[Block 1144]
འདིར་དཔུང་གི་ཚོགས་ནི་དཔུང་གི་ཚོགས་ལ་རིག་པར་བྱ་སྟེ། ཚོགས་དང་འབྲེལ་པ་ཉིད་ཀྱིས་རྣམ་པ་བཞི་པོ་རྣམས་ཀྱི་ཚིག་གོ། །

[Block 1145]
ཚོགས་རྣམས་ནི་བཞི་སྟེ། འབྲུའི་ཁ་ལྟ་བུ་དང་། ཤིང་རྟའི་དབྱིབས་ལྟ་བུ་དང་། ཟླ་ཁམ་གྱི་རྣམ་པ་ལྟ་བུ་དང་། ནམ་མཁའི༌[^685]ལྡིང་གི་འདབ་མ་ལྟ་བུའོ། །

[Block 1146]
བཤམས་པ༌[^686]ལ་ཡང་རྣམ་པ་བཞི་སྟེ། ཟླ་བའི་རྣམ་པ་ལྟ་བུ་དང་། ཤིང་རྟའི་དབྱིབས་ལྟ་བུ་དང་། གཡུལ་ངོ་རྣམ་པ༌[^687]ལྟ་བུ་དང་། ནམ་མཁའ་ལྡིང་གི་འདབ་མ་ལྟ་བུའོ། །

[Block 1147]
ཟླ་བའི་རྣམ་པ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་མདུན་དུ་ཡང་རུ༌[^688]དངར་རྒྱབ་ཏུ་ཡང་རུ༌[^689]དངར་གློར་ཡང་རུ༌[^690]དངར་ལ་དབུས་ན་རྒྱལ་པོ་འདུག་པའོ། །

[Block 1148]
ཤིང་རྟའི་དབྱིབས་ལྟ་བུ་ཞེས་བྱ་བ་ནི་མདུན་དུ་ཡང་རུ༌[^691]དངར་གློར་ཡང་རུ་དངར་ལ༌[^692]རྒྱབ་ན་རྒྱལ་པོ་འདུག་པའོ། །

[Block 1149]
གཡུལ་ངོའི་རྣམ་པ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་མདུན་དུ་ཡང་རུ༌[^693]དངར་རྒྱབ་དུ་ཡང་རུ༌[^694]དངར་ལ་དབུས་ན་རྒྱལ་པོ་འདུག་པའོ། །

[Block 1150]
ནམ་མཁའ་ལྡིང་གི་འདབ་མ་ཞེས་བྱ་བ་ནི༌[^695]གློར་ཡང་རུ༌[^696]དངར་ལ་མདུན་ན་རྒྱལ་པོ་འདུག་པའོ། །

[Block 1151]
ཚོགས་དང་དམག་ཚོགས་ཀྱི་སྒྲ་དག་ལ་རྣམ་གྲངས་ཉིད་ཀྱི་ཕྱིར་དོན་གཅིག་པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 1152]
དེ་ལྟ་བས་ན་འདི་ལྟ་སྟེ། དམག་གི་ཚོགས་སོ་སོ་ཉམས་སུ་མྱོང་བར་བྱ་ཞེས་བྱ་བ་འདིའི་བཤད་པ་ནི། ཚོགས་ལ་ལྟ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བར་བྱ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1153]
རྣམ་པ་ཅི་འདྲ་བ་འདི་རྣམས་ལ་ཁ་ན་མ་ཐོ་བ་གང་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྟ་གོན་བྱས་པ་རྣམས་ཀྱིའོ། །

[Block 1154]
དངོས་ལ་དངོས་གཞིའོ། །

[Block 1155]
སྦྱོར་བ་ལ་ནི་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟ་གོན༌[^697]མ་བྱས་པ་དེ་ལ་ནི་གཉིས་ཀ་ལ་ཡང་ཉེས་བྱས་ཁོ་ནའི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 1156]
གླང་པོ་ཆེ་ལ་སོགས་པ་རྣམས་ལ་གོ་བསྐོན་པ་ཉིད་ནི་སྟ་གོན་བྱས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 1157]
ཤིང་རྟ་བཤམས་པ༌[^698]དང་རྒྱལ་མཚན་བསྒྲེང་བ་དང་། གཞུ་བདུངས་པ༌[^699]དང་། མདའ་མདའུ་ཅན་བདར་བ་དང་རལ་གྲི་ཕྱུང་བ་ཉིད་ལ་སོགས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1158]
གཉི་ག་ལ་ཡང་ཞེས་བྱ་བ་ནི་དངོས་གཞི་དང་སྦྱོར་བ་ལའོ། །

[Block 1159]
ཅི་འདིར་དངོས་གཞི་ལ་ཞེས་བྱ་བ་བདུན་ལྟུང་བའི་མཚན་མ་ཉིད་ཀྱིས་དངོས་གཞི་བརྗོད་པ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་རེག་པ་དང་བཤམ་པ་དཀྲུག་པ་དང་ལྟ་བའི༌[^700]ཕྱིར་འཕགས་ཤིང་ཉེ་འཁོར་གྱི་མཐའ་ལས་འདས་ཏེ་མཐོང་བ་ལྟ་བུ་ནི་དངོས་གཞི་དག་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རིན་པོ་ཆེ་སྨོས་པ་ཞེས་བྱ་བས་མཚོན་ཆ་ལ་རེག་པའི་ལྟུང་བ་གང་ཡིན་པ་དེ་ནི་འཆད་པར་འགྱུར་ཏེ། དེ་ལས་ཡུལ་གཞན་ཡིན་པ་དེ་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པར་བྱའོ། །

[Block 1160]
འདིར་བཤམས་པ༌[^701]ནི་གནས་ནས་འཕོ་བར་རྣམ་པར་གནས་པ༌[^702]ཡིན་ནོ། །
--- END BLOCKS ---
