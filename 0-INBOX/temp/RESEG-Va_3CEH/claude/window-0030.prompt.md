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
[Block 1051]
བམ་པོ་ལྔ་པ། དོན་དུ་སྣང་བ་ཐམས་ཅད་འབྱུང་བའི་སྐབས་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རྣམ་པར་རིག་པ་ཙམ་གྱི་རྣམ་པར་ཡང་མི་འབྱུང་ན་དེ་དོན་གྱི་རྣམ་པར་སྣང་བ་འབྱུང་བ་ལྟ་ཅི་སྨོས་ཏེ། དེའི་ཕྱིར་རྣམ་པར་རིག་པ་ཙམ་ཉིད་དུ་བརྟགས་ན་ཡང་དོན་དུ་འགྱུར་བས། དེའི་ཕྱིར་དེ་ལས་གཞན་པ་དེ་བཞིན་ཉིད་མངོན་སུམ་ཉིད་དུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 1052]
གནས་སྐབས་དེ་ནི་བརྗོད་པར་ནུས་པ་མ་ཡིན་ཏེ། སོ་སོ་རང་གིས་རིག་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1053]
དེའི་ཚེ་བྱང་ཆུབ་སེམས་དཔའ་དེའི་དམིགས་པར་བྱ་བ་དང་དམིགས་པར་བྱེད་པ་མཉམ་པས་མཉམ་པའི་ཡེ་ཤེས་རྣམ་པར་མི་རྟོག་པ་འབྱུང་སྟེ་ཞེས་བྱ་བ་ལ་དམིགས་པར་བྱེད་པ་ནི་ཡེ་ཤེས་དང་དམིགས་པར་བྱ་བ་དེ་ནི་དེ་བཞིན་ཉིད་དེ། དེ་དག་མཉམ་པ་ཉིད་དུ་གྱུར་པ་ནི་ནམ་མཁའ་ཉིད་དུ་གཟུང་བ༌[^704]དང་། འཛིན་པ་མེད་པར་གནས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། གཟུང་བ་དང་འཛིན་པར་རྣམ་པར་རྟོག་པ་མེད་པ་ནི་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 1054]
དེ་ལྟར་ན་ཡོངས་སུ་གྲུབ་པ་ཉིད་ལ་ཞུགས་པ་ཡིན་ནོ། །

[Block 1055 [HEADING]]
#### མིང་གི་བྱེ་བྲག། ^3-2-7-0

[Block 1056]
གང་གི་ཚེ་དོན་ཐམས་ཅད་ལ་རྣམ་པར་མི་རྟོག་པའི་མིང་ལ་གནས་ཤིང་ཞེས་བྱ་བ་ནི་དེའི་མིང་ཅི་རྣམ་པ༌[^705]ཇི་སྙེད་ཅེས་བྱ་བའི་ཐ་ཚིག་ལས༌[^706]དེའི་མིང་གི་བྱེ་བྲག་ཚིགས་སུ་བཅད་པས་བསྟན་ཏོ། །

[Block 1057]
དེ་ལ་ཆོས་ཀྱི་མིང་ནི་གཟུགས་དང་། ཚོར་བ་དང་། མིག་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1058]
གང་ཟག་གི་མིང་ནི༌[^707]སངས་རྒྱས་བཤེས་གཉེན་དང་། དད་པས་རྗེས་སུ་འབྲང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1059]
ཡང་ཆོས་ཀྱི་མིང་ནི་མདོ་སྡེ་ལ་སོགས་པའོ། །

[Block 1060]
དོན་གྱི་མིང་ནི༌[^708]ཆོས་དེ་དག་ལ་བརྟེན་པའི་དོན་ཏོ། །

[Block 1061]
བསྡུས་པའི་མིང་ནི་སེམས་ཅན་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1062]
རྒྱས་པའི་མིང་ནི་དེ་དག་ཉིད་རེ་རེ་ནས་བརྗོད་པ་ལྟ་བུའོ། །

[Block 1063]
རིགས་ཀྱི་མིང་ནི་ཡི་གེའི་ཕྱི་མོ་རྣམས་སོ། །

[Block 1064]
མ་དག་པའི་མིང་ནི་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱིའོ། །

[Block 1065]
དག་པའི་མིང་ནི་སློབ་པ་རྣམས་ཀྱིའོ། །

[Block 1066]
མཐར་ཐུག་པ་རྣམས་ཀྱི་མིང་ནི་གང་འདྲེས་པའི་ཆོས་ལ་དམིགས་པ་སྟེ། ས་བཅུ་པ་ལྟ་བུའོ། །

[Block 1067]
དེ་ལ་དོན་ཐམས་ཅད་ནི་འདྲེས་པའི་ཆོས་ལ་དམིགས་པའི་ཡེ་ཤེས་ཀྱི་དམིགས་པའོ། །

[Block 1068]
དེ་ལྟ་བུའི་རྣམ་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་མིང་གི་ཡུལ་ཡིན་ནོ། །

[Block 1069]
དེ་བཞིན་གཤེགས་པའི་རིགས་སུ་སྐྱེས་པ་ཡིན་ཞེས་བྱ་བ་ནི་གང་གིས་སངས་རྒྱས་ཀྱི་གདུང་རྒྱུན༌[^709]མི་གཅོད་པར་གྱུར་པའོ། །

[Block 1070]
སེམས་ཅན་ཐམས་ཅད་ལ་སེམས་མཉམ་པ་ཡིན་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་བདག་ཇི་ལྟ་བ་བཞིན་དུ་སེམས་ཅན་ཐམས་ཅད་མྱ་ངན་ལས་བཟླའོ་ཞེས་སེམས་པའོ།[^710] །བྱང་ཆུབ་སེམས་དཔའ༌[^711]ཐམས་ཅད་དང་སེམས་མཉམ་པ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་དེ་དག་དང་སེམས་མཉམ་པ་ཉིད་ཐོབ་པའོ། །

[Block 1071]
སངས་རྒྱས་ཐམས་ཅད་དང་སེམས་མཉམ་པ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་སངས་རྒྱས་རྣམས་ཀྱི་ཆོས་ཀྱི་སྐུའི་གནས་སྐབས་དེས་ཐོབ་པར་གྱུར་པ་སྟེ། དེ་ཐོབ་པས་སངས་རྒྱས་ཐམས་ཅད་དང་སེམས་མཉམ་པ་ཐོབ་པར་གྱུར་པའོ། །

[Block 1072 [HEADING]]
#### ཞི་གནས་དང་ལྷག་མཐོང་གི་ཤེས་པ། ^3-2-8-0

[Block 1073]
ཞི་གནས་དང་ལྷག་མཐོང་གི་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཞི་གནས་དང་ལྷག་མཐོང་ཞེས་བརྗོད་པའི་ཤེས་པའོ། །

[Block 1074]
ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་ས་བོན་རྒྱུ་མཚན་དང་བཅས་པའི་རྒྱུ་མཚན་སྤངས་ནས་ཞེས་བྱ་བ་ལ་རྒྱུ་མཚན་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་རྒྱུ་མཚན་དང་བཅས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། གང་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་རྣམས་ཀྱི་ས་བོན་ཅན་ནོ། །

[Block 1075]
ཡང་རྒྱུ་མཚན་སྨོས་པ་ནི་དེའི་ས་བོན་དེ་དག་གི་དམིགས་པའི་རྒྱུ་མཚན་བསྟན་པའི་དོན་ཏོ། །

[Block 1076]
དེ་ལྟར་བྱས་ནས༌[^712]ས་བོན་དེ་དག་རྒྱུ་དང་འབྲས་བུ་དང་བཅས་པར་སྤངས་པ་བསྟན་པར་འགྱུར་རོ། །

[Block 1077]
དེའི་རྗེས་ལས་ཐོབ་པ་ལ་དགོས་པ་ཅི་ཡོད། གལ་ཏེ་རྣམ་པར་མི་རྟོག་པས་སྒྲིབ་པ་ཐམས་ཅད་སྤངས་པ་དང་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཀུན་ཏུ་བསྒྲུབ་པར༌[^713]འགྱུར་རོ་ཞེ་ན། རྒྱུ་དང་བཅས་པའི་འབྲས་བུའི་ཆོས་རྣམས་དེས་བསྟན་པར་མི་ནུས་ཏེ། དེ་ནི་མི་རྟོག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1078]
དེའི་ཕྱིར་རྗེས་ལ་ཐོབ་པས་རྒྱུ་དང་འབྲས་བུའི་ཆོས་རྣམས་སྟོན་པར་བྱེད་དེ། རྟོག་པ་ཡིན་པ་དང་། སྒྱུ་མ་མཁན་གྱིས་སྒྱུ་མ་བྱས་པ་བཞིན་དུ་ཕྱིན་ཅི་མ་ལོག་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1079]
ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལས་ཐམས་ཅད་རབ་ཏུ་སྐྱེ་བ་ཞེས་བྱ་བ་ནི་གང་ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་རྒྱུ་ལས་བྱུང་བ་རྣམས་སོ། །

[Block 1080]
རྣམ་པར་རིག་པའི་མཚན་མ་ཐམས་ཅད་དེ། རྣམ་པར་རིག་པའི༌[^714]རྒྱུར་གྱུར་པ་ལས་སྒྱུ་མ་བྱས་པ་བཞིན་དུ་རྗེས་ལས་ཐོབ་པའི་ཕྱིན་ཅི་ལོག་མེད་པར་འབྱུང་བས་ཡང་དུས་ཐམས་ཅད་དུ་སྟོན་པར་བྱེད་དོ། །

[Block 1081 [HEADING]]
#### ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ། ^3-2-9-0

[Block 1082]
ཐམས་ཅད་དུ་དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པ་ནི་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ལས་ཡིན་པས་དེའི་ཕྱིར་འདིར་ཡང་དེ་བསྟན་པར་བྱའོ། །

[Block 1083]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ལ་ཡང་དག་པར་བརྟེན་པ་ཞེས་བྱ་བ་ནི་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ལ་བརྟེན་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1084]
མངོན་པར་རྟོགས་པ་དང་ཉེ་བ༌[^715]ཞེས་བྱ་བ་ནི་མངོན་པར་རྟོགས་པའི་དུས་སུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1085]
ཇི་ལྟར་རྣམ་པར་གནས་པ་བསྟན་པ་ཞེས་བྱ་བ་ནི་གང་སྒྱུ༌[^716]ཇི་ལྟར་རྣམ་པར་གནས་པ་ས་བཅུ་པར་སའི་རྣམ་པར་གནས་པ་བསྟན་པའོ། །

[Block 1086]
འདྲེས་པ་ལ་དམིགས་པ་ཞེས་བྱ་བ་ནི་མཁས་པས་དམིགས་པའི་གནས་ལ་དམིགས་པའོ། །

[Block 1087]
འཇིག་རྟེན་ལས་འདས་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 1088]
དེའི་རྗེས་ལ་ཐོབ་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་གཞག་པ་སྟེ། དེ་ནི་འཇིག་རྟེན་པ་ཞེས་བརྗོད་པར་བྱ་སྟེ། འདི་ལྟར་འཇིག་རྟེན་པ་དང་རྗེས་སུ་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1089]
གང་གི་ཕྱིར་འཇིག་རྟེན་ལས་འདས་པ་འབའ་ཞིག་ནི་འཇིག་རྟེན་པ་ལ་རེག་པ༌[^717]མ་ཡིན་པས་སོ། །

[Block 1090]
དེ་བས་ན་གཅིག་ཏུ་ཞུགས་པར་མི་བརྗོད་དོ། །
--- END BLOCKS ---
