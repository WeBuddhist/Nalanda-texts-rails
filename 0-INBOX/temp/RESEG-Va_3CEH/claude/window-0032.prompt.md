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
དེ་ལ་སྦྱིན་པ་ལ་སོགས་པ་ལ༌[^739]ཕ་རོལ་ཏུ་ཕྱིན་པ་གསུམ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་སོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །

[Block 1122]
བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་གཉི་ག་སྟེ། དེའི་དོན་གྱི་ཐབས༌[^740]ཀྱི་བརྩོན་འགྲུས་ནི་ཡེ་ཤེས་སོ། །

[Block 1123]
གང་སེམས་ཅན་གྱི་དོན་གྱི་བརྩོན་འགྲུས་ནི་བསོད་ནམས་ཀྱི་ཚོགས་སོ། །

[Block 1124]
དེ་བཞིན་དུ་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། དེ་ལ་གང་ཡང་ཚད་མེད་པ་རྣམས་ལ་དམིགས་པའི་བསམ་གཏན་གྱི་བསོད་ནམས་སོ། །

[Block 1125]
དེ་ལས་གཞན་པ་དག༌[^741]ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །གང་ཞེ་ན། བྱང་ཆུབ་སེམས་དཔའ་ཉིད་དོ། །

[Block 1126]
ཆོས་ལ་སེམས་པ་ལེགས་པར་རྣམ་ངེས་ཕྱིར། །ཞེས་བྱ་བ་ནི། གང་ཏིང་ངེ་འཛིན་གྱི་རྗེས་ལ་ཆོས་རྣམས་སེམས་པར་བྱེད་པ་དེ་ལགས་པར་རྣམ་པར་ངེས་པ་ཡིན་གྱི་གཞན་ནི༌[^742]མ་ཡིན་ནོ། །

[Block 1127]
དོན་གྱི་རྣམ་པ་བརྗོད་པའི་རྒྱུས་བྱུང་རྟོགས། །ཞེས་བྱ་བ་ལ། དོན་གྱི་རྣམ་པ་བརྗོད་པའི་རྒྱུས་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་ཤེས་པའོ། །

[Block 1128]
དེ་འདྲ་བའི་སེམས་ཙམ་ཉིད་ལ་གནས་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་དེ་ནི་འདི་ལྟར་དོན་དུ་སྣང་བ་འདི་དག་ནི་སེམས་ཙམ་ཉིད་དོ་ཞེས་བྱ་བར་ཤེས་པའོ། །

[Block 1129 [VERSE]]
དེ་བས་གཉིས་ཀྱི་མཚན་ཉིད་བྲལ་བ་ཡི། །
ཆོས་ཀྱི་དབྱིངས་ནི་མངོན་སུམ་ཉིད་དུ་འགྱུར། །

[Block 1130]
ཞེས་བྱ་བ་ནི་གཟུང་བ་དང་འཛིན་པ་དང་བྲལ་བ་ཉིད་ཀྱིས་དེ་ལས་གཞན་པའི་དེ་བཞིན་ཉིད་མངོན་སུམ་ཉིད་དུ་འགྱུར་བའོ། །

[Block 1131]
དེ་ལས་གཞན་པ་ཇི་ལྟར་མངོན་སུམ་ཉིད་དུ་འགྱུར་ཞེ་ན། དེ་བསྟན་པར་བྱ་བའི་ཕྱིར།

[Block 1132 [VERSE]]
སེམས་ལ༌[^743]གཞན་མེད་པར་ནི་བློས་རྟོགས་ནས། །
དེ་ཕྱིར་སེམས་ཀྱང་མེད་པ་ཉིད་དུ་རྟོགས། །

[Block 1133]
ཞེས་བྱ་བ་ལ། སེམས་ལས་གཞན་པའི་དམིགས་པར་བྱ་བའི་དོན་མེད་ལ་དེ་མེད་པས་དམིགས་པར་བྱེད་པའི་སེམས་ཀྱང་མེད་པ་ཉིད་འཐོབ་པ༌[^744]སྟེ། དེ་གཉིས་ཀྱི་མེད་པ་ཉིད་བྱང་ཆུབ་སེམས་དཔས་རྟོགས་ནས། དེ་དང་མི་ལྡན་ཆོས་ཀྱི་དབྱིངས་ལ་གནས། །ཞེས་བྱ་བ་སྟེ། དོན་དེ་དག་དང་སེམས་བྲལ་བར་གྱུར་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1134]
རྟོག་མེད་ཤེས་སྟོབས་ཞེས་བྱ་བ༌[^745]རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱི་སྟོབས་སོ། །

[Block 1135]
མཉམ་པའི་རྗེས་སོང་བས་ཞེས་བྱ་བ་ནི་ནམ་མཁའ་དང་འདྲ་བར་མདོ་སྡེ་ལ་སོགས་པའི་ཆོས་ཐམས་ཅད་མཉམ་པ་ཉིད་དུ་མཐོང་བའོ། །

[Block 1136]
ཀུན་ནས་ཞེས་བྱ་བ་ནི་ཕྱི་དང་ནང་གི་བདག་ཉིད་དོ། །

[Block 1137]
ཇི་ལྟར་མཐོང་བའི་ཆོས་དེ་དག་ཉིད་དུས་རྟག་ཏུ་མཐོང་བར་ནི་རྟག་པར་ཡང་ངོ་། །དེའི་གནས་ཐིབས་པོ་ཉེས་པ་བསགས་པ་ཞེས་བྱ་བ་ནི་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་དེའི་གནས་ཏེ་རྒྱུའོ། །

[Block 1138]
ཐིབས་པོ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་རྟོགས་པར་དཀའ་བ་ཉིད་དོ། །

[Block 1139]
ཉེས་པ་བསགས་པ་ཞེས་བྱ་བ་ནི་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་རྣམས་ཀྱི་བག་ཆགས་ཀྱི་ངོ་བོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1140 [VERSE]]
ཐུབ་པས་གསུངས་པའི་ལེགས་ཆོས་ལེགས་གཞག་པ། །
རྩ་བ་ཆོས་ཀྱི༌[^746]དབྱིངས་ལ་དེ༌[^747]བློ་བཞག །

[Block 1141]
ཅེས་བྱ་བ་ལ། རྩ་བ་དང་བཅས་པའི་སེམས་ཀྱིས་དམིགས་པ་གང་ལ་བློ་ངེས་པར་བཞག་པ་སྟེ། དེ་བཞིན་ཉིད་དེ་ལའོ། །

[Block 1142]
དེ་ལ་རྩ་བའི་སེམས་ནི་གང་དེ་བཞིན་གཤེགས་པ་མ་ལུས་པའི་སྟོན་པ༌[^748]བསྡུས་པ་ལ་དམིགས་པ་སྟེ། དེ་ཡང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཡིན་པར་བལྟའོ། །

[Block 1143]
དྲན་པའི་རྒྱུད་ནི་རྟོག་པ་ཙམ་ཤེས་ནས། །ཞེས་བྱ་བ་ལ། དེ་ཡང་རྩ་བའི་སེམས་ལ་གནས་པ་སྟེ། བསྟན་པའི་རྗེས་ལ་ཐོབ་པའི་དོན་ཏེ། འདས་པ་དྲན་པ་ནི་དྲན་པའི་རྒྱུད་དེ་གང་རྣམ་པར་རྟོག་པ་ཙམ་དུ་གྱུར་པའོ། །

[Block 1144]
རྣམ་པར་མི་རྟོག་པ་དང་། དེའི་རྗེས་ལ་ཐོབ་པ་དེ་དག་གཉི་གས་ཀྱང་། ཡོན་ཏན་རྒྱ་མཚོའི་ཕ་རོལ་ཏེ་སངས་རྒྱས་ཉིད་དུའོ། །

[Block 1145]
བརྟན་མྱུར་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་ཉིད་དོ། །

[Block 1146]
ཚིགས་སུ་བཅད་པ་དེ་རྣམས་ཀྱི་བསྡུས་པའི་དོན་ནི་དང་པོས་ནི་ཚོགས་ཀྱི་ལམ་མོ། །

[Block 1147]
གཉིས་པའི་ཕྱེད་ཀྱིས༌[^749]ནི་སྦྱོར་བའི་ལམ་མོ། །

[Block 1148]
ཕྱེད་ཕྱི་མ་དང་གསུམ་པས་ནི་མཐོང་བའི་ལམ་མོ། །

[Block 1149]
བཞི་པས་ནི༌[^750]བསྒོམ་པའི་ལམ་མོ། །

[Block 1150]
ལྔ་པས་ནི་མཐར་ཕྱིན་པའི་ལམ་མོ། །

[Block 1151 [HEADING]]
## འཇུག་པ་དེའི་རྒྱུ་དང་འབྲས་བུ། ^4-0

[Block 1152]
གང་གི་ཚེ་ཞུགས་པ་དེའི་ཚེ་ལྷག་པའི་བསམ་པ་རྣམ་པར་དག་པ་ཡིན་པའི་ཕྱིར་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་ཀུན་ཏུ་སྤྱོད་པའི་སྦྱོར་བ་ཞེས་བྱ་བ་ནི་ཀུན་ཏུ་སྤྱོད་པ༌[^751]སྦྱོར་བ༌[^752]ཐམས་ཅད་དུ་སྦྱོར་བའོ། །

[Block 1153]
བསྟན་པ་ལ་མོས་པ་ཞེས་བྱ་བ་ནི་གང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དང་རབ་ཏུ་ལྡན་པའི་ཤིན་ཏུ་ཟབ་པ་དེ་དག་ལ་ཡང་ངོ་། །རོ་མྱང་བ་ཡིད་ལ་བྱེད་པ་སྟེ། དེ་དག་གི་ཡོན་ཏན་མཐོང་བར༌[^753]རོ་མྱང་བའོ། །

[Block 1154]
མངོན་པར་དགའ་བ་ཡིད་ལ་བྱེད་པ་ནི་ཇི་ལྟ་བུའི་ལྷག་པའི་བསམ་པས་མཆོག་ཏུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐོབ་པ་ངེས་པ་དེ་ལྟ་བུ་བདག་དང་སེམས་ཅན་ཐམས་ཅད་ཀྱིས་ཐོབ་པར་གྱུར་ཅིག་ཅེས་དེ་ལྟ་བུ་མངོན་པར་དགའ་བའོ། །

[Block 1155 [HEADING]]
### ལྷག་པའི་བསམ་པ་དག་པའི་མཚན་ཉིད། ^4-1-0

[Block 1156]
རེ་ཞིག༌[^754]ལྷག་པའི་བསམ་པ་དག་པ་དེ་དག༌[^755]ཉིད་ཀྱི་མཚན་ཉིད་གང་ཡིན། གང་གིས་དེ་དག་ཡོངས་སུ་བཟུང་བ་ཡིན་ཞེ་ན། གང་གི་རྗེས་ཐོགས་སུ་ཚིགས་སུ་བཅད་པ་དག་གིས་དེའི་མཚན་ཉིད་སྟོན་པར་བྱེད་དེ། དེ་ལ་རེ་ཞིག་མོས་པས་སྤྱོད་པའི་ས་ལ་ཚོགས་ལེགས་པར་བསགས་པ་དང་། དཀར་པོའི་ཆོས་རྣམས་ཀུན་རྫོགས་པ༌[^756]ཉིད་དོ། །

[Block 1157]
བཟོད༌[^757]རྣོན་ཐོབ་དང་ཞེས་བྱ་བ་ནི་ཆུང་ངུ་ལ་སོགས་པ་བཟོད་པ༌[^758]རྣམ་པ་གསུམ་ལས་བཟོད་པའི་མཆོག་ལ་གནས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1158 [HEADING]]
#### དམིགས་པ། ^4-1-1-0

[Block 1159]
གང་ལ་དམིགས་ནས་དག་པར་འགྱུར་བ་དེ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཐེག་ཆེན་ལ་ཞེས་བྱ་བ་སྟེ། གང་དུ་ཞེ་ན། ཟབ་ཅིང་རྒྱ་ཆེ་བསྟན་པ་ལའོ། །

[Block 1160]
དེ་ཉིད་ནི་རང་གི་ཐེག་པ་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིའོ། །
--- END BLOCKS ---
