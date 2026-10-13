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
[Block 1156]
དཔེར་ན་ལུས་མེད་པས་ཀྱང་ཕྲ་བའི་ལུས་དང་ལྡན་པའི་སེམས་པ༌[^814]ཡོད་པ་ཉིད་དོ། །

[Block 1157]
སེམས་དང་ལྡན་པ་ནི༌[^815]ལུས་ཐམས་ཅད་དུ་མཐོང་ངོ་། །གཟུགས་མེད་པའི་ཁམས་ལ་ཡང་ཏིང་ངེ་འཛིན་གྱི་ལུས་མེད་པར་མི་འབྱུང་བའོ། །

[Block 1158]
གཞི་དང་གཞི་ཅན་གྱི་འབྲེལ་པ་ནི་ལུས་དང་།

[Block 1159 [VERSE]]
སེམས་དག་ལ་འབྲེལ་པ་རིགས་པ་ཉིད་དོ། །
གཞི་འཇིག་པས་གཞི་ཅན་འཇིག་པར༌[^816]མ་མཐོང་སྟེ།
ཤིང་བཅད་པས་བྱ་རོག་བཅད་པ་མ་མཐོང་ངོ་། །

[Block 1160]
གལ་ཏེ་དེ་ལྟ་ཡིན་ན་གསོན་པ་དང་འཆི་བའི་ཐ་སྙད་ཇི་ལྟར་འགྱུར་ཞེ་ན། སྨྲས་པ། ཐོག་མ་མེད་པའི་དུས་ནས་སྲེད་པ་དང་མ་རིག་པའི་བག་ཆགས་ཀུན་འབྱུང་གི་བདེན་པའི་རྣམ་གྲངས་ཅན་གྱི་དབང་གིས་སྲོག་དང་དབང་པོའི་ཚོགས་གཡོ་བར་གྱུར་པས་ཚེ་གནས་པར་བྱེད་པའི་ལས་ཀྱི་དབང་གིས་ཕུང་པོ་ཟ་མ་ཏོག་གི་ནང་དུ་ཇི་སྲིད་རྣམ་པར་ཤེས་པ་གནས་པ་དེ་སྲིད་གསོན་པོ་ཡིན་ཞེས་ཐ་སྙད་འབྱུང་ངོ་། །ཚེ་གནས་པར་བྱེད་པའི་ལས་འགོག་པས་སྲོག་ལ་སོགས་པའི་འཁོར་ལོ་འཛད་པས༌[^817]འཆིའོ་ཞེས་འཇིག་རྟེན་དུ་གྲགས་སོ། །

[Block 1161]
རྣམ་པར་ཤེས་པ་ནི་ཡང་དང་ཡང་དུ་སྐྱེ་ཞིང་འགོག་པར༌[^818]འགྱུར་ཞེས་འབྱུང་བ་ཆེན་པོ་ལས་སེམས་ཐ་དད་པ་ཁོ་ནའོ། །

[Block 1162]
དེའི་ཕྱིར་རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་ནི་ཡོད་དེ་དེ་རྣམས་ཀྱི་ཡང་བདེ་བ་ལ་སོགས་པ་སྒྲུབ་པར་བྱེད་པ་དགེ་བ་དང་མི་དགེ་བ་ཡོད་པས་མཐོ་རིས་དང་དམྱལ་བ་ལ་སོགས་པ་ཡོད་ཅེས་དེ་རྟོགས་པར་བྱ་བའི་ཕྱིར་རྗེས་སུ་དཔག་པ་ཡང་ཡོད་པ་ཁོ་ནའོ་ཞེས་འཇིག་རྟེན་རྒྱང་པན་པ་ལ༌[^819]ལན་ནོ། །

[Block 1163 [HEADING]]
###### **མཆོད་འོས་པ།** ^1-5-3-3-1-4-0

[Block 1164]
མཆོད་འོས་རྣམས་ཀྱིས་ཀྱང་ཡོངས་སུ་འགྱུར་བ་དང་། གང་ཟག་རྟག༌[^820]པ་ཡིན་ཞེས་སྨྲ་བའོ། །

[Block 1165]
དེ་རྣམས་ཀྱི་གཞུང་འདི་ཡིན་ཏེ། དུས་གསུམ་གྱི་དངོས་པོ་རྣམས་ནི་གང་མ་འོངས་པའི་དུས་སུ་གནས་པ་དེ་དག་ད་ལྟར་འབྱུང་བར་འགྱུར་ཏེ། གང་ཡང་ད་ལྟར་བྱུང་བ་དེ་དག་འདས་པའི་དུས་ཉིད་དུ་འགྱུར་ཏེ། འདས་པ་རྣམས་ཀྱང་མ་འོངས་པར་འགྱུར་ཞིང་། མ་འོངས་པ་ཡང་ད་ལྟར་བྱུང་བར་འགྱུར་ཞེས་གང་ཡང་སྐྱེ་བ་དང་འཇིག་པར་མི་འགྱུར་ཏེ་གསེར་བཞིན་ནོ། །

[Block 1166]
དཔེར་ན་རྣ་ཆ༌[^821]འགྱུར་བས༌[^822]གསེར་དང་གསེར་ཡང་འགྱུར་བས་རྣ་ཆ༌[^823]ལྟ་བུར་འགྱུར་ཞེས་གསེར་གྱི་རང་གཟུགས་ཉམས་པར་མི་འགྱུར་རོ། །

[Block 1167]
དེ་ལྟར་ཡིན་པས་ཞོ་ཡང་རྔ་མོར་འགྱུར་བ་དང་རྔ་མོ་ཡང་ཞོར་འགྱུར་རོ། །

[Block 1168]
བདག་རྟག་པ་ལ་ནི་འགྱུར་བས་ཀྱང་སྐྱོན་མེད་དོ། །

[Block 1169]
ཇི་སྐད་དུ།

[Block 1170 [VERSE]]
སྔ་མའི་ཆོས་གཞན་སྤངས་པ་ནི། །
གང་ཚེ་ཆོས་གཞན་ལེན་གྱུར་ན། །
ཆོས་ཅན་དེ་ཉིད་ལས་མ་འཕོས། །
ཡོངས་སུ་གྱུར་པ་དེ་བཤད་དོ། །

[Block 1171]
ཞེས་འབྱུང་ངོ་། །དེ་ལ་སྨྲས་པ། གལ་ཏེ་འགྲོ་བ་དང་མི་འགྲོ་བའི་བདག་ཉིད་འགྲོ་བ་བདག་རྟག་པའི་ངོ་བོ་ཡིན་ན། དེའི་ཚེ་ཅིའི་ཕྱིར་ཡོངས་སུ་འགྱུར་ཏེ་ཡོངས་སུ་འགྱུར་བ་ཞེས་བྱ་བ་ནི་རང་གི་གཟུགས་འཇིག་པའི་བདག་ཉིད་མི་རྟག་པའི་མཚན་ཉིད་ཅན་གྱི་ཆོས་ཀྱི་ཁྱད་པར་རོ། །

[Block 1172]
གང་མི་རྟག་པ་དེ་ཇི་ལྟར་བདག་ཡིན་གལ་ཏེ་གསེར་དང་མདུད་པ་དང་ཁུ་ཚུར་གྱི་རིགས་པས་རང་གི་ངོ་བོ་མི་འཇིག་ཅེས་ཟེར་ན། དེ་ཡང་མི༌[^824]རིགས་ཏེ། གསེར་ལ་ཁྱད་པར་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1173]
དཔེར་ན་གསེར་ལྟར་སྣང་བ་འཇིག་པས་ཀྱང་དེ་ནི་བརྟག་པ་ཤེས་པ་རྣམས་ཀྱིས་སྲ་བ༌[^825]དང་ཁ་དོག་ལ་སོགས་པས་བྱས་པའི་ཁྱད་པར་འགས༌[^826]ངེས་པར་འབྱུང་ངོ་། །གང་ཁྱད་པར་འབྱུང་བ་དེ་ཉིད་མི་རྟག་པ་ཉིད་དོ། །

[Block 1174]
གལ་ཏེ་བདག་ཅེས་བྱ་བ་ཐ་དད་པ་དང་ཐ་མི་དད་པ་ཡང་རུང་སྟེ། དེའི་རང་གི་ངོ་བོ་འཇིག་པར་མི་འགྱུར་ཞེ་ན། དེ་ཡང་བདེན་པ་མ་ཡིན་ཏེ། ཐ་དད་པ་དང་ཐ་མི་དད་པ་ནི་ཕན་ཚུན་འགལ་བའོ། །

[Block 1175]
གལ་ཏེ་ཐ་དད་ན༌[^827]ཅིའི་ཕྱིར་ཐ་མི་དད། ཐ་མི་དད་པ་ལ་ཐ་དད་པ་ཡང་མི་རིགས་ཏེ། ཐ་མི་དད་པ་ཡང་ཡིན་ལ་ཐ་དད་པ་ཡང་ཡིན་ཞེས་འགལ་བའི་ཆོས་བརྟགས་པའི་དབང་གིས་བདག་ཇི་ལྟར་བརྟག་པར་འགྱུར་རོ། །

[Block 1176]
[^828]དེའི་ཕྱིར་ན་གང་ཟག་གི་ཐ་སྙད་ནི་བརྟགས་པ་ཡིན་ནོ་ཞེས་མཆོད་འོས་པ༌[^829]ལ་ལན་ནོ། །

[Block 1177 [HEADING]]
###### **ཞི་བ་པ།** ^1-5-3-3-1-5-0

[Block 1178]
ཞི་བ་པ་ན་རེ་རྟག་ཅིང་ཐམས་ཅད་བྱེད་པ་ཀུན་ཤེས་པ་འདོད་པ་དང་བྱ་བ་དང་ཡེ་ཤེས་ཀྱི་ནུས་པ་གསུམ་གྱི་མཐུས་སྐྱེ་བ་དང་གནས་པ་དང་། འཇིག་པར་བྱེད་པ་འཇིག་རྟེན་གསུམ་གྱི་དབང་ཕྱུག་ཁོ་ན་རྒྱུ་ཡིན་ཞེས་དེ་ཉིད་ལས་ཐམས་ཅད་འབྱུང་ཞིང་ཐིམ་པར་འགྱུར་རོ། །

[Block 1179]
བརྟན་པ་དང་གཡོ་བའི་དབྱེ་བས་དབྱེ༌[^830]བར་འགྱུར་བའི་འབྲས་བུའི་དངོས་པོ་གང་ཡིན་པ་དེ་དག་ཐམས་ཅད་འཇིག་པའི་ཆོས་ཅན་དེ་ལས་འབྱུང་ཞིང་། རང་ཉིད་ནི་མི་འཇིག་གོ། །

[Block 1180]
ཇི་སྐད་དུ།

[Block 1181 [VERSE]]
འདིར་ནི་གནས་སྐབས་གཉིས་ཡིན་ཏེ། །
བྱ་བ་བྱེད་པ་ཉིད་དུ་གྲགས། །
བྱ་བ་ཉིད་ནི་ཟད་གྱུར་པ། །
བྱེད་པ་ཉིད་ནི་ཟད་མེད་དོ། །

[Block 1182]
ཞེས་འབྱུང་ངོ་། །སྦྱོར་བ་ནི་གང་དང་གང་རྒྱུ་རྟག་པ་ལས་བྱུང་བ་དེ་དག་ནི་འཇིག་པའི་ཆོས་ཅན་དུ་མཐོང་སྟེ། དུག་གི་ཤིང་གི་མྱུ་གུ་དང་འདབ་མ་དང་འབྲས་བུ་དང་ཡལ་ག་བཞིན་ནོ། །

[Block 1183]
རྟག་པའི་དབང་ཕྱུག་ལས་འབྱུང་བ་ཐམས་ཅད་འཇིག་པའི་ཆོས་ཅན་ཡིན་གྱི་རྩ་བར་གྱུར་པའི་དབང་ཕྱུག་ལ་འཇིག་པ་མེད་དེ་ནམ་མཁའ་བཞིན་ཞེས་རང་བཞིན་གྱི་གཏན་ཚིགས་སོ། །

[Block 1184]
སྨྲས་པ། གལ་ཏེ་དེས་ཁམས་གསུམ་སྐྱེད་པར་བྱེད་ན་དེའི་ཚེ་ཇི་ལྟར་རྟག་པ་ཡིན་ཏེ། བྱེད་པ་དང་རྟག་པ་ཉིད་ཕན་ཚུན་འགལ་བའི་ཕྱིར་རོ། །

[Block 1185]
བྱེད་པ་པོ་ཡིན་ན་ཅིའི་ཕྱིར་སྔོན་དུ་མི་བྱེད། ལྷན་ཅིག་བྱེད་པ་ལ་ལྟོས་པ་ཅི་དགོས་ཏེ། ལྟོས་པ་དང་བཅས་པ་ནི་ནུས་པ༌[^831]མེད་པའི་ཕྱིར་རོ། །

[Block 1186]
ཡང་ན་ལྟོས་པ་མི་དགོས་ན་དེའི་ཚེ་ཅི་སྟེ་བྱེད་དེ་ནམ་མཁའ་བཞིན་ནོ། །

[Block 1187]
དེའི་ཕྱིར་བྱ་བའི་དུས་དང་བྱ་བ་མེད་པའི་དུས་དག་ཡོད་པས་བྱེད་པ་དང་མི་བྱེད་པས༌[^832]ཕན་ཚུན་འགལ་བ་ཡིན་པས་མི་རྟག་པ་ཁོ་ནའོ། །

[Block 1188]
ཡང་ན་གལ་ཏེ་དབང་ཕྱུག་དེས་རང་དབང་དུ་བྱེད་པ༌[^833]ཡིན་ན་དེའི་ཚེ་སྔོན་དུ་བཤད་པའི་ནུས་པ་གསུམ་ལ་ལྟོས་པ་མི་རིགས་སོ། །

[Block 1189]
ཡང་ན་དབང་ཕྱུག་ལས་ནུས་པ་ཐ་མི་དད་པ་ཞེ་ན། དེའི་ཚེ་ནུས་པ་ཁོ་ན་བྱེད་པ་ཡིན་གྱི་དབང་ཕྱུག་ནི་མ་ཡིན་ནོ། །

[Block 1190]
ཡང་ན་དབང་ཕྱུག་བྱེད་པ་པོ་ཡིན་ན་ནུས་པས་ཅི་ཞིག་བྱ། །ཡང་ན་དབང་ཕྱུག་གི་ནུས་པས་ཞེས་འབྲེལ་པ་གང་ཞིག་ཡིན།[^834] །དེའི་བདག་ཉིད་ལ་སྔོན་དུ་བཤད་པའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1191]
རྒྱུ་འབྲས་ཀྱི་འབྲེལ་པས་ཀྱང་དབང་ཕྱུག་ལ་ནུས་པ་སྐྱེས་པས་དབང་ཕྱུག་འགོག་པར༌[^835]འགྱུར་རོ། །

[Block 1192]
དེ་ཡང་འདོད་པ་མ་ཡིན་ཏེ། དེ་རྟག༌[^836]པའི་ཕྱིར་རོ། །

[Block 1193]
རྒྱུ་རྣམས་ནི་ངེས་པར་འབྲས་བུ་དང་ལྡན་པར་མི་འགྱུར་ཞེས་ནུས་པ་ཁོ་ན་རྒྱུ་རུ་འགལ་བ་མེད་དོ། །

[Block 1194]
དེ་བས་ན་དབང་ཕྱུག་བྱེད་པ་པོར་མི་འགྱུར་རོ། །

[Block 1195]
འདུ་བའི་འབྲེལ་པས་དེའི་བདག་ཉིད་དུ་འཐད་ཅེ་ན། འདུ་བ་ཞེས་བྱ་བ་ཅི་ཡིན་ན་སྣམ་བུ་དང་སྣལ་མ་ཐ་དད་པ་དག་ལ་ཡང་འདིར་སྣལ་མ་ལ་སྣམ་བུ་ཞེས་ཐ་སྙད་ཡིན་ཞེ་ན། འོ་ན་ནི་སྣལ་མ་ལས༌[^837]མ་གཏོགས་པའི་སྣམ་བུ་གང་ཞིག་ཡོད། གང་ལ་ལྟོས་པས་དེ་དག་གི་འདུ་བའི་འབྲེལ་པར་འགྱུར། ཆུ༌[^838]དང་ཞེང་གི་བདག་ཉིད་ཁེབས་པ་ལ་སོགས་པའི་བྱ་བ་བྱེད་པ་སྣམ་བུ་ཡིན་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། དེའི་ཚེ་དེ་དག་སྣལ་མ་མ་ཡིན་གྱི་སྣམ་བུ་གཅིག་པུ་ཁོ་ན་དོན་གྱི་བྱ་བ་བྱེད་པས་སོ། །
--- END BLOCKS ---
