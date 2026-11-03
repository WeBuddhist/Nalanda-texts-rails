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
[Block 1156 [HEADING]]
#### འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་ལས་ཁྱད་ཞུགས་པ། ^3-1-1-0

[Block 1157]
བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལས་ངེས་པར་བྱུང་བ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་བསྔོས་པས་ལྷའི་མིག་དེ་ལྟ་བུ་ཐོབ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1158]
རྒྱ་ཆེན་པོ་ལས་ངེས་པར་འབྱུང་བ༌[^1011]རྣམས་ཀྱིས་ལྷའི་མིག་ནི་ཆེས་མཆོག་གོ་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་རྒྱ་ཆེན་པོ་འམ། ལམ་གྱི་ཡེ་ཤེས་རྒྱ་ཆེན་པོ་སྤྱོད་པ་ལས་ཐོས་པའི༌[^1012]ལྷའི་མིག་ནི་ཆེས་མཆོག་གོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1159]
ཆེས་མཆོག་ཅེས་བྱ་བ་ནི་ལྷ་དང་ཀླུ་ལ་སོགས་པ་འཇིག་རྟེན་པ་འཕགས་པ་མ་ཡིན་པ་རྣམས་ཀྱི་ལྷའི་མིག་པས་ཉན་ཐོས་དང་རང་སངས་རྒྱས་འཕགས་པ་རྣམས་ཀྱི༌[^1013]ལྷའི་མིག་མཆོག་གོ། །

[Block 1160]
འཕགས་པ་དེ་དག་གི་ལྷའི་མིག་བས་ཀྱང་བྱང་ཆུབ་སེམས་དཔའི་ལྷའི་མིག་མཆོག་པས་ན་དེ་ཉིད༌[^1014]ལས་བཟླ་བའི༌[^1015]ཕྱིར་ཆེས་མཆོག་ཅེས་བྱའོ། །ཅིའི་ཕྱིར་ཆེས་མཆོག་ཅེ་ན། འཇིག་རྟེན་པ་རྣམས་ཀྱིས་ཟག་པ་དང་བཅས་པ་དང་། འཕགས་པ་ཉན་ཐོས་ལ་སོགས་པ་འཇིག་རྟེན་ལས་འདས་པ་རྣམས་ཀྱི་མངོན་པར་ཤེས་པ་ཡང་འདས་པ་དང་། མ་འོངས་པ་དང་། དབང་པོས་ལྷག་པ་དང་། ཁམས་ཀྱིས༌[^1016]ལྷག་པ་ལ་སོགས་པ་གོང་མ་རྣམས་ཤེས་པར༌[^1017]མི་ནུས་ལ་ཅུང་ཟད་ཤེས་ཤིང་ཚད་ཡོད་ཀྱི། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་དེ་ལྟ་མ་ཡིན་ཏེ། ཚད་དང་མཐའ་མེད་པའི་ཕྱིར་ཆེས་མཆོག་གོ། །

[Block 1161]
དེ་ལ་མཆོག་ནི་བཀྲ་ཤིས་པའི་ཕྱིར་རོ། །

[Block 1162]
ཆེས༌[^1018]དམ་པ་ནི་གོང་ནས་གོང་དུ་ཁྱད་པར་དུ་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 1163]
ཆེས་རབ་ནི་ཐམས་ཅད་ཀྱི་ཐོག་མར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 1164]
ཆེས་ཕུལ་ནི་གཟུགས་ཐམས་ཅད་ལ་ཁྱབ་པའི་ཕྱིར་རོ། །

[Block 1165]
ཆེས་གསལ་བ་ནི་དྲི་མ་མེད་ཅིང་རབ་ཏུ་དང་བའི་ཕྱིར་རོ། །

[Block 1166]
ཆེས་བཟང་བ་ནི་མ་སྨད་ཅིང་མྱ་ངན་ལས་འདས་པ་དང་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1167]
ཆེས་སྟོབས་དང་ལྡན་པ་ནི་ཐོགས་པ་མེད་པར་གཟུགས་ཀུན་མཐོང་བའི་མཐུ་ཆེན་པོ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1168]
ཆེས་འོད་གསལ་བ་ནི་ཡེ་ཤེས་དྲི་མ་མེད་པའི་མཐུ་མཆོག་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1169]
འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་ལས་ཁྱད་ཞུགས་པ༌[^1019]བཤད་ཟིན་ཏོ།། །།

[Block 1170 [HEADING]]
#### གཟུགས་ཐམས་ཅད་མཐོང་བ། ^3-1-2-0

[Block 1171]
གཟུགས་ཐམས་ཅད་མཐོང་བ་བསྟན་པའི་ཕྱིར། དེ༌[^1020]ལྷའི་མིག་དེས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1172]
ལྷའི་མིག་དེས་ཞེས༌[^1021]བྱ་བའི་གོང་དུ་བཤད་པ་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ལྷའི་མིག་ཐམས་ཅད་ལས་འདས་པར་གྱུར་པའི༌[^1022]ལྷའི་མིག་དེས་ཞེས༌[^1023]བྱ་བའི་དོན་ཏོ། །

[Block 1173]
གཟུགས་སུ་སྣང་བ་ཞེས་བྱ་བ་ནི་གཟུགས་སུ་གཏོགས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1174]
རགས་པའམ་ཞེས་བྱ་བ་ནི་ཆེན་པོར་གཏོགས་པ་ཐམས་ཅད་བསྡུས་པ་སྟེ། གངས༌[^1024]རི་དང་རི་རབ་ལ་སོགས་པའོ། །

[Block 1175]
ཕྲ་མོ་ཞེས་བྱ་བས་ཆུང་ངུར་གཏོགས་པ་ཐམས་ཅད་བསྡུས་པ་སྟེ། རྡུལ་དང་རྡུལ་ཕྲན་ལ་སོགས་པའོ། །

[Block 1176]
བཟང་པོ་འམ་ཞེས་བྱ་བས་བཟང་པོ་ཐམས་ཅད་བསྡུས་པ་སྟེ། གང་འཕགས་པ་སློབ་པ་དང་མི་སློབ་པ་ལ་སོགས་པའི་གཟུགས་སོ། །

[Block 1177]
ངན་པའམ་ཞེས་བྱ་བས་ངན་པ་ཐམས་ཅད་བསྡུས་པ་སྟེ། གང་སོ་སོའི་སྐྱེ་བོའི་གཟུགས་རྣམས་སོ། །

[Block 1178]
རྒྱང་རིང་པོ་འམ་ཞེས་བྱ་བས་རྒྱང་རིང་པོར་གཏོགས་པ་ཐམས་ཅད་བསྡུས་པ་སྟེ། གང་འཇིག་རྟེན་གྱི་ཁམས་བརྒྱ་སྟོང་དུ་མའི་ཕ་རོལ་ན་གནས་པའོ། །

[Block 1179]
ཐག་ཉེ་བ༌[^1025]གང་ཅི་ཡང་རུང་ཞེས་བྱ་བས་ཉེ་བ་ཐམས་ཅད་བསྡུས་པ་སྟེ། གང་ཐག་ཉེ་བ་ན་འདུག་པའི་གཟུགས་ཐམས་ཅད་དོ། །

[Block 1180]
ཡང་ན་རགས་པ་ནི་འབྱུང་བ་ཆེན་པོ་བཞི་རྣམས་སོ། །

[Block 1181]
ཕྲ་བ་ནི་འབྱུང་བ་ཆེན་པོ་བཞི་ལས་གྱུར་པའི་གཟུགས་རྣམས་སོ། །

[Block 1182]
ཡང་ན་རགས་པ་ནི་འཇིག་རྟེན་པའི་གཟུགས་རྣམས་སོ། །

[Block 1183]
ཕྲ་བ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་གཟུགས་རྣམས་སོ། །

[Block 1184]
ཡང་ན་རགས་པ་ནི་འདོད་པའི་ཁམས་སུ་གཏོགས་པའི་གཟུགས༌[^1026]སོ། །

[Block 1185]
ཕྲ་བ་ནི་གཟུགས་ཀྱི་ཁམས་སུ་གཏོགས་པའི་གཟུགས་སོ། །

[Block 1186]
བཟང་པོ་ནི་བདེ་འགྲོ་རྣམས་ཀྱི་གཟུགས་སོ། །

[Block 1187]
ངན་པ་ནི་ངན་སོང་བ༌[^1027]རྣམས་ཀྱི་གཟུགས་སོ། །

[Block 1188]
ཡང་ན་བཟང་པོ་ནི་དབྱིབས་དང་ཁ་དོག་ཏུ་ལྡན་པའོ། །

[Block 1189]
ངན་པ་ནི་དབྱིབས་དང་ཁ་དོག་ཏུ་མི་ལྡན་པའོ། །

[Block 1190]
རྒྱང་རིང་པོ་ནི་འདས་པ་དང་མ་འོངས་པའི་གཟུགས་སོ། །

[Block 1191]
ཐག་ཉེ་བ་ནི་ད་ལྟར་གྱི་གཟུགས༌[^1028]སོ། །

[Block 1192]
ཡང་ན་རྒྱང་རིང་པོ་ནི་གཞན་གྱི་རྒྱུད་དུ་གཏོགས་པའི་གཟུགས་སོ། །

[Block 1193]
ཐག་ཉེ་བ་ནི་བདག་གི་རྒྱུད་དུ་གཏོགས་པའི་གཟུགས་སོ། །

[Block 1194]
དེ་དག་ཐམས་ཅད་ནི་གོང་དུ་བཤད་པའི་གཟུགས་དེ་དག་ཐམས་ཅད་དོ། །

[Block 1195]
དེ་དག་གི་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་གི་ལྷའི་མིག་གིས་སོ། །
--- END BLOCKS ---
