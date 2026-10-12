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
ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་ཡེ་ཤེས་རྡོ་རྗེ་ཀུན་ལས་བཏུས་པ་ཞེས་བྱ་བ་ལས་གསུངས་ཏེ། དེ་ནས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བྱམས་པ་སྟན་ལས་ལངས་ཏེ། བཅོམ་ལྡན་འདས་ཀྱི་ཞབས་ལ་སྤྱི་བོས་ཕྱག་འཚལ་ནས་བཅོམ་ལྡན་འདས་ལ་འདི་སྐད་ཅེས་གསོལ་ཏོ། །

[Block 1122]
ཨེ་མའོ་སྟོན་པ་རྣམ་པར་ཤེས་པ་གསུམ་པོ་རྟོགས་པར་དཀའ་བ་མཆོག་ཏུ་རྟོགས་པར་དཀའ་བ་སྟེ། རྣམ་པར་ཤེས་པ་གསུམ་གྱི་དབྱེ་བ་བསྟན་དུ་གསོལ། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རྣམ་པར་ཤེས་པ་ནི༌[^557]འོད་གསལ་བ་ལས་འབྱུང་ངོ་། །དེ་ནི་སེམས་དང་ཡིད་ཅེས་བྱ་སྟེ་ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བ་དང་དེའི་བདག་ཉིད་ཅན་གྱི་ཆོས་ཐམས་ཅད་ཀྱི་རྩ་བ་ཡིན་ནོ། །

[Block 1123]
དེ་ལས་བདག་དང་གཞན་དུ་རྟོག་པ་འབྱུང་བར་འགྱུར་རོ། །

[Block 1124]
རྣམ་པར་ཤེས་པ་དེ་རླུང་ལ་ཞོན༌[^558]ཏེ་རླུང་ལས་ནི་མེའོ། །

[Block 1125]
མེ་ལས་ནི་ཆུའོ། །

[Block 1126]
ཆུ་ལས་ནི་སའོ། །

[Block 1127]
དེ་དག་ལས་ནི་ཕུང་པོ་ལྔ་དང་། སྐྱེ་མཆེད་དྲུག་དང་། དབང་པོ་ལྔ་རྣམས་ཏེ་དེ་དག་ཐམས་ཅད་ནི་རླུང་དང་འདྲེས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གསུངས་སོ། །

[Block 1128]
དེ་ནས་ཡེ་ཤེས་ཀྱི་ཕུང་པོ་ལྔ་ཡང་ཉེ་བར་ཐོབ་པར་བྱ་བའི་ཕྱིར། འདི་ནི་ཕུང་པོ་ལྔ་རྣམས་སུ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་ཕུང་པོ་ལྔ་ཉིད་ཀྱང་སེམས་ལས་འབྱུང་བར་བསྟན་ཏོ། །

[Block 1129]
དེ་ཡང་གང་ཞེ་ན་གཟུགས་ཚོར་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། གཟུགས་ནི་གཟུགས་ཀྱི་ཕུང་པོ་སྟེ་གཞིག་ཅིང་གཞོམ་དུ་རུང་བ་ལ་སོགས་པའི་ཕྱིར་རོ། །

[Block 1130]
ཚོར་བ་ནི་མྱོང་བའོ། །

[Block 1131]
འདུ་ཤེས་ནི་མཚན་མར་འཛིན་པ་ཉིད་དོ། །

[Block 1132]
འདུ་བྱེད་ནི་མངོན་པར་འདུ་བྱེད་པ་ཉིད་དོ། །

[Block 1133]
རྣམ་པར་ཤེས་པ་ནི་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་སྟེ་དམིགས་པ་སོ་སོར་རྣམ་པར་རིག་པའི་ཕྱིར་རོ། །

[Block 1134]
འདི་དག་གིས་ནི་སེམས་ཉིད་གཟུགས་སུ་སྣང་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1135]
གལ་ཏེ་དེ་ལྟ་ན་ནི་གཟུགས་མེད་པ་ལས་ནི་གཟུགས་སུ་སྣང་བས་རྒྱུའི་བྱེད་པ་དང་། འབྲས་བུའི་བྱེད་པ་གཞན་དུ་ཉེ་བར་སྦྱར་བར་འགྱུར་རོ། །

[Block 1136]
འདི་གཉིས་ནི་ངོ་བོ་གཅིག་པ་ཡང་མ་ཡིན་ཏེ། གཟུགས་དང་གཟུགས་མེད་པ་གཅིག་གིས་གཅིག༌[^559]སྤངས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1137]
འབྲེལ་པ་ཡོད་པར་ངེས་པ་མེད་དེ། གང་གིས་གང་གི་དུས་ན་རག་ལས་པར་འགྱུར་བ་དང་མེད་ན་མི་འབྱུང་བ༌[^560]འགྱུར་བའི་ངེས་པ་མེད་དོ་ཞེ་ན་མ་ཡིན་ཏེ། རྣམ་པར་ཤེས་པ་འཕོ་བའི་མདོ་ལས་འདི་ཉིད་རྒྱས་པར་གསུངས་ཏེ། བཟང་སྐྱོང་དཔེར་ན། རླུང་གི་ཁམས་གཟུགས་ཅན་མ་ཡིན་པ༌[^561]ཡང་བསྟན་དུ་ཡོད་ཅིང་གཟུང་དུ་མེད་པ་ལས་གཟུགས་སུ་སྣང་ངོ་། །དེ་ལ་བསྟན་དུ་ཡོད་པ་ནི་ཤིང་འགུལ་ཞིང་གཡོ་བ་དང་སྒྲ་འུར་འུར་པོའི་སྐད་འབྱིན་པ་དང་། གྲང་བ་དང་དྲོ་བའི་རེག་པས་ཚོར་བ་སྐྱེད་པ་ཡིན་ཡང་རྐང་ལག་དང་གདོང་དང་མིག་ལ་སོགས་པར་དམིགས་པར་མི་འགྱུར་ཏེ། སྔོ་བསངས༌[^562]དང་དཀར་བ་དང་། དམར་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཁ་དོག་ཡོངས་སུ་གསལ་བ་མི་དམིགས་སོ། །

[Block 1138]
བཟང་སྐྱོད་དེ་བཞིན་དུ་རྣམ་པར་ཤེས་པའི་ཁམས་འདི་ཡང་གཟུགས་སུ་མི་དམིགས་ཤིང་གཟུགས་སུ་སྣང་བར་མི་འགྱུར་ཏེ་འོན་ཀྱང་གང་ལ་གནས་ཀྱང་འབྱུང་བར་འགྱུར་རོ། །

[Block 1139]
དེ་བས་ན་ཁྱོད་ཀྱི༌[^563]བྱེ་བྲག་དེ་དག་གིས་རྣམ་པར་ཤེས་པའི་ཁམས་རྟོགས་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1140]
དེའི་ཕྱིར་རླུང་དང་རྣམ་པར་ཤེས་པ་གཟུགས་མེད་པས་རྣམ་པ་གསུམ་མར་གྱི་ནང་དུ་མར་བཅུག་པ་དང་འདྲ་བར་འདྲེས་པར་གྱུར་ནས་འཇིག་རྟེན་དང༌[^564]འཇིག་རྟེན་ལས་འདས་པའི་བྱ་བ་ཐམས་ཅད་རྫོགས་པར་བྱེད་དོ། །

[Block 1141]
གཞན་ཡང་།

[Block 1142 [VERSE]]
རང་རིག་ཙམ་གྱི་ཡེ་ཤེས་ནི། །
ནམ་མཁའ་འདྲ་བར་མཚན་ཉིད་མེད། །
འོན་ཀྱང་དེ་ལ་དབྱེ་བ་ཡོད། །
མཚན་མོ་ཉིན་མོ་མཚམས་བདག་ཉིད། །

[Block 1143 [VERSE]]
སྣང་བ་དང་ནི་སྣང་བ་མཆེད། །
དེ་བཞིན་སྣང་བ་ཐོབ་པ་དེ། །
སེམས་ནི་རྣམ་པ་གསུམ་དུ་བཤད། །
དེ་ཡི་གཞི་ནི་བཤད་པར་བྱ། །

[Block 1144]
ཕྲ་བའི་གཟུགས་ཅན་རླུང་དང་ནི། །ཡེ་ཤེས་དག་ནི་འདྲེས་འགྱུར་པ།[^565] །

[Block 1145 [VERSE]]
དབང་པོའི་ལམ་ནས་བྱུང་ནས་ནི། །
ཡུལ་རྣམས་ལ་ནི་དམིགས་པར་བྱེད། །
གང་ཚེ་སྣང་བ་ལྡན་གྱུར་པ། །
རླུང་ནི་བཞོན་པར་གྱུར་པ་ཡིན། །

[Block 1146 [VERSE]]
དེ་ཚེ་རང་བཞིན་དེ་ཐམས་ཅད། །
མ་ལུས་ལུས་པ་མེད་པར་འབྱུང་། །
རླུང་ནི་གང་དང་གང་དུ་གནས། །
དེ་དང་དེ་ནི་རང་བཞིན་འབྱུང་། །

[Block 1147]
ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱ་ཆེར་གསུངས་སོ། །

[Block 1148]
གཞུང་གཞན་དག་ལས་ཀྱང་རྣམ་པར་ཤེས་པ་འདིས་ནི་ཇི་སྲིད་དུ་ལུས་སྐྱེ་བར་བྱེད། འཆི་བར་བྱེད་ཅིང༌[^566]ཉིང་མཚམས་སྦྱོར་བར་བྱེད་ཀྱི།[^567] །རྣམ་པར་ཤེས་པ་ལ་ནི་སྐྱེ་བ་དང་འཆི་བ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱ་ཆེར་གསུངས་སོ། །

[Block 1149]
དེ་ནས་ཡེ་ཤེས་ལྔའི་མཚན་ཉིད་རྒྱས་པར་བཤད་པར་བྱ་སྟེ་དེའི་ཕྱིར། མཉམ་ཉིད་སོ་སོར་རྟོག་པ་དང་། །ཞེས་བྱ་བ་ལ་སོགས་པ༌[^568]གསུངས་ཏེ། དེ་ལ་མཉམ་པ་ཉིད་ཅེས་བྱ་བ་ནི་རྐང་མེད་དང་། རྐང་གཉིས་དང་རྐང་བཞི་དང་། རྐང་མངས་དང་། འཇིག་རྟེན་གྱི་ཆོས་བརྒྱད་ལ་སོགས་པ་རང་བཞིན་གྱི་སེམས་ཙམ་དང་རང་བཞིན་མེད་པར་གཅིག་པར་རྟོགས་པས་ནི་མཉམ་པ་ཉིད་དོ། །

[Block 1150]
གང་གིས་གང་གི་དེ་ཉིད་ཡོངས་སུ་ཤེས་པར་གྱུར་པ་དེ་ནི་དེའི་ཡེ་ཤེས་ཡིན་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1151]
གང་གི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དང་། ཕྱི་དང་ནང་གི་ཆོས་ཐམས་ཅད་སོ་སོར་རྣམ་པར་ཕྱེ་སྟེ་རྣམ་པར་བརྟགས༌[^569]ན་ཐམས་ཅད་སངས་རྒྱས་ཀྱི་རང་བཞིན་ནོ། །

[Block 1152]
ཆོས་ཐམས་ཅད་ཀྱི་ཆ་ཤས་ནི་འདི་དག་གོ་ཞེས་པདྨའི་འདབ་མ་ལྟར་སོ་སོར་རྟོག་པ་སྟེ་གང་ལ་གང་གིས་ཆོས་ཡོད་པར་གྱུར་པ་གང་དང་གང་ཡིན་པ་དེ་དང་དེའི༌[^570]ཇི་ལྟར་གྱུར་པ་ཤེས་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1153]
བྱ་བ་གྲུབ་པས་ན་བྱ་བ་གྲུབ་པ་ཉིད་དེ། བདག་དང་གཞན་གྱི་བྱ་བ༌[^571]ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་ཡོངས་སུ་རྫོགས་པར་གྱུར་པ་ཉིད་གང་ལ་གང་གིས་ཇི་ལྟར་ཡོངས་སུ་བྱེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1154]
མེ་ལོང་ནི་མེ་ལོང་ལྟ་བུའི་ཡེ་ཤེས་ཏེ། ཕྱི་དང་ནང་གི༌[^572]ཆོས་ཐམས་ཅད་མེ་ལོང་གི༌[^573]གཟུགས་བརྙན་སྣང་བ་བཞིན་དུ་སྣང་བ་སྟེ། ཆོས་གང་ཞིག་གང་གིས་ཇི་ལྟར་ཡོངས་སུ་ཤེས་པར་གྱུར་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1155]
ཆོས་ཀྱི་དབྱིངས་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཏེ་ལུས་དང་ངག་དང་ཡིད་ཀྱི་སྒྲིབ་པ་དག་ཅིང་ལས་དང་ཉོན་མོངས་པ་ལས་གྲོལ་ཏེ། དགེ་བ་དང་མི་དགེ་བའི་བག་ཆགས་ཕྲ་རྒྱས་མ་ལུས་པ་ཐམས་ཅད་སྤངས་ནས་གནས་པ་ནི་ཆོས་ཀྱི་དབྱིངས་སྤྲོས་པ་ཐམས་ཅད་དང་བྲལ་བའི་ཡེ་ཤེས་ཏེ། འདི་དག་གི་དོན་ནི༌[^574]སེམས་ཉིད་ཐོག་མ་ལ་སོགས་པ་དང་བྲལ་ཡང་ཡེ་ཤེས་སུ་ཡང་འགྱུར་བ་སྟེ་གོང་དུ་བརྗོད་པའི་ལུང་ཉིད་བཞིན་ནོ། །

[Block 1156]
དེ་ནས་སེམས་དེ་ཉིད་སྐྱེ་མཆེད་ཀྱི་ངོ་བོར་ཡང་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པའི་ཕྱིར། ཡིད་ཀྱི་སྐྱེ་མཆེད་ཉིད་དང་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་ཆོས་ལ་དམིགས་པ་དང་། བདག་དང་གཞན་གྱི་ཡུལ་རིག་པ༌[^575]དང་། སྤྱི་དང་བྱེ་བྲག་ལ་སོགས་པ་རིག་པར་བྱེད་པ་ནི་ཡིད་ཀྱི་སྐྱེ་མཆེད་དེ་དུས་གཅིག་པ་ཉིད་དོ། །

[Block 1157]
མིག་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཡུལ་གཅིག་པ་ཉིད་དེ་རང་གི་ཡུལ་ལ་དམིགས་པ་དང་། རང་གི་མཚན་ཉིད་རིག་པ་ལ་སོགས་པའོ། །

[Block 1158]
དེའི་སེམས་ལ་དམིགས་པ་ནི་གནས་པའི་རླུང་ལ་དབང་ཐོབ་ནས་འབྱུང་ངོ་། །གང་གིས་གནས་པ་ནི་གང་ཞིག་གང་དུ་བྱས་པ་དེ་ལ་རག་ལས་པར་འགྱུར་རོ་ཞེས་བསྟན་པའི་ཕྱིར།

[Block 1159 [VERSE]]
གང་ཡང་ཁམས་གསུམ་སེམས་ཅན་རྣམས། །
ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ།
ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་ནོ། །

[Block 1160]
སྲོག་དང་རྩོལ་བ་ནི་སྲོག་དང་རྩོལ་བ༌[^576]སྟེ་རྩ་བ་དང་ཡན་ལག་གི་རླུང་ངོ་། །
--- END BLOCKS ---
