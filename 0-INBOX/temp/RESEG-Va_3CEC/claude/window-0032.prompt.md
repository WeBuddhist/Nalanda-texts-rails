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
བཏང་སྙོམས་ནི་གཞན་གྱི་སེམས་སྲུང་བའོ༌[^985]ཞེས་བྱ་བ་ནི་གཞན་གྱི་སེམས་འཁྲུག་པར༌[^986]མི་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1122]
བཏང་སྙོམས་ནི་བདག་ལ་རྟོག་པའོ་ཞེས་བྱ་བ་ནི་གཞན་གྱིས༌[^987]གནོད་པ་བྱས་ཀྱང་བདག་གི་ལས་ལ་རྟོག་གི་གཞན་ལ་ཁོན་དུ་མི་འཛིན་པའོ། །

[Block 1123]
བཏང་སྙོམས་ནི་སེམས་ཅན་གཞན་དག་ལ་གནོད་པ་མེད་པའོ༌[^988]ཞེས་བྱ་བ་ནི་གནོད་པ་ཐམས་ཅད་བདག་གི་ལས་ལས་བྱུང་བར་རྟོགས་པས༌[^989]སེམས་ཅན་གྱིས༌[^990]མ་ཉེས་པར་ཤེས་པའི་ཕྱིར་སེམས་ཅན་གྱིས༌[^991]གནོད་པར་བྱེད་པས་སེམས་ཅན༌[^992]ལ་གནོད་པར༌[^993]མི་བྱེད་པའོ། །

[Block 1124]
བདག་དང་གཞན་བསྲུང་བའི་བཏང་སྙོམས་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། བཏང་སྙོམས་ནི་བྱང་ཆུབ་སེམས་དཔའི་མཉམ་པར་གཞག༌[^994]པའི་གནས༌[^995]སྐབས་ཡིན་ཏེ་ཞེས་བྱ་བ་གསུངས་ཏེ། མཉམ་པར་གཞག་པ་ནི་ཆགས་པ་དང་ཁོང་ཁྲོ་བ་མེད་པར་བྱའོ། །

[Block 1125]
དེ་ལྟར་མཉམ་པར་གཞག་པའི་གནས་སྐབས་ནི་བཏང་སྙོམས་ཡིན་པས་དེ་བས་ན་བཏང་སྙོམས་ནི་མཉམ་པར་གཞག་པའི་གནས་སྐབས་སོ། །

[Block 1126]
ཡང་ན་མཉམ་པར་གཞག་པ་ནི་ཏིང་ངེ་འཛིན་དུ་སེམས་རྩེ་གཅིག་པར་གཞག་པ་སྟེ། དེའི་གནས་སྐབས་ནི་བཏང་སྙོམས་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། གང་ལ་ཡང་ཆགས་པ་དང་ཞེ་སྡང་མེད་ན་འདོད་སེམས་རྩེ་གཅིག་པར་ནུས་པས་སོ། །

[Block 1127 [HEADING]]
##### དུས་དང་དུས་མ་ཡིན་པའི་བཏང་སྙོམས། ^2-4-2-3-0

[Block 1128]
དུས་དང་དུས་མ་ཡིན་པའི་བཏང་སྙོམས་བསྟན་པའི་ཕྱིར། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་དུས་དང་དུས་མ་ཡིན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1129]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་དུ་བཏང་སྙོམས་བྱ་བར་བཀའ་མི་སྩོལ་ཏོ་ཞེས་བྱ་བ་ནི་གོང་དུ་རྣམ་པ་ཐམས་ཅད་དུ་བཏང་སྙོམས་པ་བཤད་པ་སྟེ། སྐབས་ཁ་ཅིག་ཏུ་དེ་ལྟར་བཏང་སྙོམས་སུ་བྱར་མི་རུང་གི །དུས་དང་སྦྱར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1130]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་འདྲི་བའི་ཚིག་སྟེ། དུས་ཐམས་ཅད་དུ་ཅིའི་ཕྱིར་བཏང་སྙོམས་སུ་བཞག་ཏུ་མི་རུང་ཞེ་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1131]
བྱང་ཆུབ་སེམས་དཔའ་རྟག༌[^996]ཏུ་བདག་དང་གཞན་གྱི་དགེ་བའི་ཆོས་བཙལ་བ་ལ་བརྩོན་ཞིང་འབད་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དུས་ཐམས་ཅད་དུ་བདག་དང་གཞན་གྱི་ཆོས་བཙལ་བ་ལ་འབད་པར་བྱ་བ་ཡིན་པས། བྱང་ཆུབ་སེམས་དཔའ་བདག་དང་གཞན་གྱི་དོན་དང་སྦྱར་ཏེ་ཁ་ཅིག་བཏང་སྙོམས་སུའང་འདོར། ཁ་ཅིག་ཏུ་བཙལ་ཞིང་འབད་པར་བྱ་ཞིང༌[^997]བཏང་སྙོམས་སུ་མི་གཞག་གོ་ཞེས་པའི་དོན་ཏོ། །

[Block 1132]
སྣོད་མ་ཡིན་པ་དང་མཉན་པར༌[^998]མི་འདོད་པའི་སེམས་ཅན་ལ་བཏང་སྙོམས་ཞེས་བྱ་བ་ནི་དུས་ལ་བབ་པའི་སེམས་ཅན་ཏེ། ཆོས་ཟབ་མོ་བཤད་པའི་སྣོད་མ་ཡིན་པ་དང་། ཆོས་ཉན་པར་མི་འདོད་པ་ལ་མི་འཆད་པར་འཇོག་པ་སྟེ། སྐབས་འདིར་བཏང་སྙོམས་ཞེས་བྱ་བ་ནི་མི་བྱ་བར་གཞག་པ་ལ་བྱའོ། །

[Block 1133]
མ་རྙེད་པ་ལ་སོགས་པའི་དུས་ན་ཡང་མི་དགའ་བའི་སེམས་མི༌[^999]འབྱུང་བ་རྣམས་བཏང་སྙོམས་སུ་གཞག་པའོ། །

[Block 1134]
སེམས་ཅན་ཉན་ཐོས་ཀྱི་ཐེག་པ་ཅན་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཉན་ཐོས་སུ་རིགས་ངེས་པའི་གང་ཟག་དྲོད་དང་སྤྱི་བོ་ལ་སོགས་པ་ངེས་པར་འབྱིན་པའི་ས་ལ་བཞུགས་པའམ། མཐོང་བའི་ལམ་ལ་ཞུགས་པ་རྣམས་ནི་ཐེག་པ་ཆེན་པོ་ལ་སྒྱུར༌[^1000]དུ་མི་བཏུབ་པ༌[^1001]དེ་བཞིན་དུ་བཏང་སྙོམས་སུ་གཞག་པའོ། །

[Block 1135]
སྦྱིན་པའི་དུས་ན་ཚུལ་ཁྲིམས་བཏུལ་བའི་བཏང་སྙོམས་ནི་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་གཉིས་སྤྱད་པའི་སྒོ་ཐ་དད་པས་སྦྱིན་པ་སྤྱད་པའམ། སྦྱིན་པའི་ཡོན་ཏན༌[^1002]བསྔགས་པའི་དུས་སུ་ཚུལ་ཁྲིམས་སྤྱོད༌[^1003]པའམ། ཚུལ་ཁྲིམས་ཀྱི་ཡོན་ཏན་བསྔགས་པ་བཏང་སྙོམས་སུ་གཞག་གོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1136]
དེ་བཞིན་དུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གི་བར་ལ་ཡང་སྦྱར་རོ། །

[Block 1137]
གང་གདོན་མི་ཟ་བར་བྱ་བའི་ཆོས་རྣམས་ལ་མི་འཇུག་པ་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གོང་དུ་མི་བྱ་བའི་ཆོས་རྣམས་ལ་བཏང་སྙོམས་པར་བསྟན་པར་ཟད་ཀྱི་བྱང་ཆུབ་ཆེན་པོའི་རྒྱུ་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ངེས་པར་སྒྲུབ༌[^1004]དགོས་པ་ཀུན་ལ་འཇུག་ཅིང་བཏང་སྙོམས་སུ་མི་བྱ་བར་སྟོན་ཏོ། །

[Block 1138]
སྟོབས་ནི་ལེ་ལོས་ཟིལ་གྱིས༌[^1005]མི་ནོན་པའོ། །

[Block 1139]
མོས་པ་ནི་དགེ་བར་སྤྱད་པ་ལ་དད་པའོ། །

[Block 1140]
མཐུན་པ་ནི་བདུད་ལ་སོགས་པས་མི་ཚུགས་པའོ། །

[Block 1141]
བརྩོན་པ་མི་འདོར་བ་ནི་བརྩོན་འགྲུས་རྒྱུན་དུ་སྤྱོད་པ་མི་གཏོང་བའོ། །

[Block 1142]
བཏང་སྙོམས་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1143 [HEADING]]
## མངོན་སུམ་གྱུར་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^3-0

[Block 1144]
མངོན་སུམ་གྱུར་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^1006]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་མངོན་པར་ཤེས་པ་ལྔ་ཡང་མི་ཟད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། མངོན་པར་ཤེས་པ་ལ་གནས་པ་རྣམས་ནི་མངོན་དུ་གྱུར་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱའོ། །

[Block 1145]
དེ་མི་ཟད་པ་ཡང་ཤེས་པར་བྱ་བའི་དངོས་པོ་སེམས་ཅན་དང་ཆོས་རྣམས་ལ་མཐའ་མེད་དེ་མི་ཟད་པས་ལྷའི་མིག་ལ་སོགས་པ་ཤེས་པར་བྱེད་པ་རྣམས་ཀྱང་མི་ཟད་དོ། །

[Block 1146]
འདིར་ཡང་བསྟན་པ་དང་བཤད་པའི་ཚུལ་དུ་བལྟ་སྟེ། ལྔ་གང་ཞེ་ན་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། རྫུ་འཕྲུལ་བྱ་བ་ཤེས་པ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་བསྟན་པའི་ཚུལ་བསྟན་ཏོ། །

[Block 1147]
དེ་མན་ཆད་ལྷག་མ་ཐམས་ཅད་ཀྱིས་བཤད་པའི་ཚུལ་བསྟན་ཏོ། །

[Block 1148]
མངོན་སུམ་དུ་གྱུར་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡང་རྣམ་པ་དྲུག་སྟེ། གཟུགས་མངོན་སུམ་པ་དང་ཚིག་མངོན་སུམ་པ་དང་། སེམས་མངོན་སུམ་པ་དང་། བསགས་པ༌[^1007]མངོན་སུམ་པ་དང་། མཉམ་པ་ཉིད་མངོན་སུམ་པ་དང་། འབྱུང་བ་མངོན་སུམ་པར་གྱུར་པའོ། །

[Block 1149 [HEADING]]
### གཟུགས་མངོན་སུམ་པ། ^3-1-0

[Block 1150]
དེ་ལ་གཟུགས་མངོན་སུམ་བསྟན་པའི་ཕྱིར། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^1008]ལྷའི་མིག་གང་ཞེ་ན་ཞེས་བྱ་བ༌[^1009]ལ་སོགས་པ་གསུངས་སོ། །

[Block 1151]
གཟུགས་མངོན་སུམ་པ་དེ་ཡང་རྣམ་པ་བཞིར་རིག་པར་བྱ་སྟེ། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་ལས་ཁྱད་ཞུགས་པ་དང་། གཟུགས་ཐམས་ཅད་མཐོང་བ་དང་། མི་མཐུན་པའི་དྲི་མས་མ་གོས་པ་དང་། རྒྱུ་རྣམ་པར་དག་པའོ། །

[Block 1152]
དེ་ལ་གང་ལྷ་ཐམས་ཅད་ཀྱི་ལྷའི་མིག་ཅེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཆོས་འོད་གསལ་ཏེ་བྱ་བ་ཡན་ཆད་ཀྱིས་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་ཐམས་ཅད་ལས་ཁྱད་ཞུགས་པ་བསྟན་ཏོ། །

[Block 1153]
ལྷའི་མིག་དེས་ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། དེ་དག་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་དོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་གཟུགས་ཐམས་ཅད་མཐོང་བ་བསྟན་ཏོ། །

[Block 1154]
དེ་དག་གི་མིག་དེ་ནི་གཟུགས་ཐམས་ཅད༌[^1010]མཐོང་བས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ལམ་ལ་མ་ཆགས་པར་སྤྱོད་པའོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་མི་མཐུན་པའི་དྲི་མས་མ་གོས་པར་བསྟན་ཏོ། །

[Block 1155]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། མངོན་པར་ཤེས་པ་མ་ཉམས་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རྒྱུ་རྣམ་པར་དག་པ་བསྟན་ཏོ། །

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
--- END BLOCKS ---
