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
[Block 1016]
ད་ནི་སྨྱོན་པའི་བརྟུལ་ཞུགས་ཆེན་པོའི་སྤྱོད་པ་དམ་ཚིག་དང་སྡོམ་པས་གཉུག་མའི་དབང་པོ་སྡངས༌[^1127]པར་བྱེད་པའི་ཐབས་དང་ཅུང་ཟད་སྨྱོན་པའི་བརྟུལ་ཞུགས་སྔར་གྱི་ལས་རྣམ་པ་གཞན་གྱིས་དབང་པོ་དང་བར་བྱིན་གྱིས་བརླབ་པའི་ཐབས་བསྟན་པའི་ཕྱིར། །བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ལ་སོགས་པ་བསྟན་ཏེ་གོ་སླའོ། །དེ་ནས་རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པ་ནི་བདག་དྲི་བའི་སྐབས་ཡིན་པ་བཞིན་དུ་རྣལ་འབྱོར་མ་རྣམས་ཀྱང་མ་ཡིན་ཏེ། སྔར་དབང་པོའི་གྲངས་བསྟན་པའི་སྐབས་སུ།གཏི་མུག་རྡོ་རྗེ༌[^1128]ལ་སོགས་ལྡན། །ཞེས་པ་གནང་བ་དེ་ཞུས་པའི༌[^1129]ཕྱིར་རོ། །

[Block 1017]
ཐམས་ཅད་ཡུལ་གྱི་རྣམ་དག་ནི་ལེའུ་དགུ་པར་སྒྱུ་མ་རྣམ་དག་གོ། །དེའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་སོ། །དབང་པོ་དྲུག་ལམ་གསུངས་པའི་བར༌[^1130]ལེའུ་དགུ་པར་མ་བསྟན་ཅིང་། དབང་པོའི་གྲངས་བསྟན་པའི་སྐབས་སུ་གནང་བ་མཛད་དེ་གསོལ་བ་ཞེས་སྔ་མར་འབྲེལ་ལོ། །གཞན་དག་ནི་གོ་སླའོ། །གོ་ཆ་ཞེས་བྱ་བ་ནི་ཐ་མལ་གྱི་དབང་པོ་སྤངས་ནས། ལྷའི༌[^1131]ས་བོན་ལས་མོས་པ་མི་མཐུན་པ་འཇུག་མི་ནུས་པས་ཀ་བ་ཙ་སྟེ་གོ་ཆའམ་ཁྲབ་བོ། །སེམས་དཔའ་ཆེན་པོ་བོས་ནས་དགོས་པ་ཡོད་པར་བསྟན་པའོ། །

[Block 1018]
རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པ་ནི་གླེང་གཞི་དང་སྡོམ་པ་ལ་དགོས་པའི་ཡན་ལག་གི་ཐབས་རྣལ་འབྱོར་མ་ཀུན་ལ་གནང་བ་སྟེ། མ་ལུས་པར་བསམས་ནས་དྲིས་པའོ། །དགོངས་པའི་སྐད་ཅི་ཞེས་པ་ནི་སྔར་གནང་ཡང་ངེས་པར་མ་གསུངས་སོ། །བཅོམ་ལྡན་འདས་ཀྱིས་ངེས་པར་གསུངས་པ་ནི་བཤད་པར་རོ། །

[Block 1019]
རྣལ་འབྱོར་མའི་དམ་ཚིག་ཆེན་པོ་ནི་རྡོ་རྗེ་སྙིང་པོས་དྲིས་ཀྱང་རྣལ་འབྱོར་མ་ལ་ཐུགས་སྟོན་པས་མངོན་རྟོགས་སྐྱེས་པའོ། །ཉན་ཐོས་ལ་སོགས་མི་ཤེས་པ། །ཞེས་པ་ནི་རང་རྒྱལ་བ་དང་ཕ་རོལ་ཕྱིན་པས་མི་ཤེས་པའོ། །འོ་ན་བྱ་བའི་རྒྱུད་ལ་སོགས་པ་རྒྱུད་སྡེ་གཞན་གྱིས་ཀྱང་ཤེས་སམ་ཞེ་ན། དབང་གི་ཐབས་ཀྱིས་སྟོན་པའི་གླེང་གཞི་སྡོམ་ཡོད་ཀྱིས་ཀྱང་། དགོངས་པའི་སྐད་མ༌[^1132]བསྒྲགས་ཤིང༌[^1133]བཤད་པས་འདིར་ངེས་པར་བསྟན་པ་གོ་སླའོ། །ད་ནི་ཉམས་སུ་ལེན་པ་སུ་དག་དང་སྨྲ་ཞེ་ན། དེའི་ཕྱག་རྒྱ་ནི་གཡུང་མོ་ལ་སོགས༌[^1134]གོ་སླའོ། །ད་ནི་སྐད་ཀྱིས༌[^1135]མ་སྨྲས་པའི་སྐྱོན་བསྟན་པའི་ཕྱིར་རྡོ་རྗེ་སྙིང་པོ་ལ་སོགས་པའོ། །དགྱེས་པའི་རྡོ་རྗེ་དབང་བསྐུར་ཞེས་པ་ནི་དབང་བསྐུར་བའི་དུས་སུའམ།ཡང་ན་དབང་ཐོབ་ནས་དུས་ཐམས་ཅད་དུའོ། །རང་གི་དམ་ཚིག་རིགས་རྙེད་ནས། །ཞེས་པ་ནི་ཁྱད་པར་གྱི་དུས་ཏེ་ཞིང་སྐྱེས་མ་ལ་སོགས་པ་རྙེད་ནས་སྤྱོད་པའི་ཚེའོ། །ལེའུ་གསུམ་པའོ།། །།

[Block 1020 [HEADING]]
### ལེའུ་བཞི་པ། ^2-4-0

[Block 1021]
དེ་ནས་ནི་རྗེས་ལ་སྟེ་ལེའུ་སྔ་མའིའོ། །རྡོ་རྗེ་སྙིང་པོ་ལ་སོགས་པ་རྡོ་རྗེ་མཁའ་འགྲོ་མ་ཐེ་ཚོམ་དུ་གྱུར་པ་ནི་སྔར་ནི་སོ་སོར་དྲིས་ལ༌[^1136]ད་ནི་སྡོམ་སྟེ་བཅོམ་ལྡན་འདས་ལ་གསོལ་ཏོ། །དེ་དག་གིས་སོ་སོར་དྲིས་པ་ནི་གོ་སླའོ། །བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། །ཞེས་པ་ལན་རིམ་གྱིས་ཏེ་དང་པོར་གླུའོ། །

[Block 1022 [HEADING]]
#### རྡོ་རྗེའི་གླུ། ^2-4-1-0

[Block 1023]
རྡོ་རྗེའི་གླུ་ཡང་བཞིར་གནས་ཏེ་བསྐྱེད་རིམ་གྱི་ང་རྒྱལ་དང་ལྡན་པའི་དཔའ་བོའི་སྟོན་མོ་དང་། ཚོགས་བྱ་བ་དང་། གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་ཀུན་གྱི་ཆགས་པའི་ཆོས་སུ་བསྟན་པ་དང་རང་ལུས་ཐབས་དང་ལྡན་པ་དང་གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 1024 [HEADING]]
##### བསྐྱེད་རིམ། ^2-4-1-1-0

[Block 1025]
བསྐྱེད་རིམ་ལ་གཉིས་ཏེ། དཔའ་བོའི་སྟོན་མོ་དང་ཚོགས་སོ། །

[Block 1026 [HEADING]]
###### དཔའ་བོའི་སྟོན་མོ། ^2-4-1-1-1-0

[Block 1027]
དཔའ་བོའི་སྟོན་མོ་ལ་བཞི་སྟེ། འདུ་བའི་ཁྱད་པར་དང་ལོངས་སྤྱོད་དང་དམ་ཚིག་དང་རྟོག༌[^1137]པའོ། །

[Block 1028 [HEADING]]
###### **འདུ་བའི་ཁྱད་པར།** ^2-4-1-1-1-1-0

[Block 1029]
དེ་ལ་འདུ་བའི་ཀོ་ལ་ཨི་རེ་ཊྛི་སྟེ་གནས་ལ་སོགས་པའི་རྣལ་འབྱོར་པ་དང་། མུམྨུ་ནི་ཞིང་ལ་སོགས་པའི་རྣལ་འབྱོར་མ་རྣམས་དང་གྷ་ཎེ་སྟེ་ཉེ་བར་འདུས་ནས་ཧ༌[^1138]ལེ་ཀ་ལི་སྟེ་སྐལ་པ་དང་ལྡན་པ་ནི་གཞུག །དུཾ་དུ་ར་སྟེ་སྐལ་བ༌[^1139]དང་མི་ལྡན་པ་ནི་མི་གཞུག་གོ། །ནི་རཾ་ཤུ་རུས་པའི་རྒྱན་བཏགས་པའོ། །ཀྲྀ་པི་ཊ་ཧོ་བཛྲ་ཞེས་པ་ནི་ཅང་ཏེའུའི་སྒྲ་ནི་བརྡུང་བ་དང་བཅས་པའོ། །ཀཱ་རུ་ཎ་ནི་བརྩེ་བ་དང་ལྡན་པའོ། །ཨ་ཨི་ན་རོལ་སྟེ་ཞེ༌[^1140]འགྲས་པ་མེད་པས་སོ། །ཏ༌[^1141]ཧི་ཛཾ་ས་རཱ་བ་སྟེ་རོ་བཙལ་ནས་སོ། །པ་ཎི་ཨ་ཨི་སྟེ་དབུས་སུ་བཅུག་པ་དང་བཅས་པའོ། །

[Block 1030 [HEADING]]
###### **ལོངས་སྤྱོད།** ^2-4-1-1-1-2-0

[Block 1031]
ཀུན་ཀྱང་རྟོག་པ་བསྐྱེད་ཅིང་བསྒོམ་སྟེ། ལོངས་སྤྱོད་ཀྱི་རྣལ་འབྱོར་ཀུན་དང་སྤྱད་པར་བྱ་བའི་རོ་ལ་སོགས་པ་རྫས་ཀུན་ལ་རོ་ནི་ཕྲེཾ་ཁ་ཎ་སྟེ་གང་ནས་ཀྱང་མ་འོངས། ཁ༌[^1142]ཊ་ཀ་རན་ཏེ༌[^1143]གང་དུ་ཡང་འགྲོ་བའི་དགོས་པ་མེད་པའོ། །གཞན་དག་བཟའ་བཏུང་གི་ཆོ་གས༌[^1144]ནི་ཤུདྡྷ་སྟེ་དག་པ་དང་། །ཨ་ཤུདྡྷ་སྟེ་མ་དག་པར་རོ། །མུ་ཎི་ཨ་ཨི་སྟེ་མི་བལྟ་བར་རོ། །གཙང་བ་དང་མི་གཙང་བ་མེད་པའི་ཕྱིར་དག་པ་དང་མ་དག་པར་མི་བལྟ་སྟེ་ལྷར་རྟོགས་པས་བསྒོམ་པ་དང་། ཏ་ཧིཾ་བ་ལ་སྟེ་སྟོབས་བཟའ་བ་དང་། ག་ཌྷེཾ་སྟེ་འབད་པས་ཆང་བཏུང་བ་སྟེ་ལོངས་སྤྱོད་དོ། །

[Block 1032 [HEADING]]
###### **དམ་ཚིག།** ^2-4-1-1-1-3-0

[Block 1033]
དེ་ནས་དམ་ཚིག་ནི་ཙ༌[^1145]ཨུ་མ་སྟེ། བཞི་མཉམ་ལ་སོགས་པའོ། །ཨ་ཨི་བྷ་རུ་ཁཱ་ཨི༌[^1146]སྟེ་དེར་ཁེངས་པར་བཟའ་བཏུང་ངོ་། །

[Block 1034 [HEADING]]
###### **རྟོག་པ།** ^2-4-1-1-1-4-0

[Block 1035]
རྟོགས་པ་ནི་མངོན་རྟོགས་འཁྲུག་སྟེ༌[^1147]ཤེས་པར་བྱའོ། །

[Block 1036 [HEADING]]
###### ཚོགས། ^2-4-1-1-2-0

[Block 1037]
ཚོགས་ལ་གཉིས་ཏེ་ཡུལ་མཉམ་པ་དང་སྦྱོར་བ་མཉམ་པའོ། །དེ༌[^1148]ཡང་ཚིག་གི་གོ་རིམས་བཟློག་པའོ། །

[Block 1038 [HEADING]]
###### **ཡུལ་མཉམ་པ།** ^2-4-1-1-2-1-0

[Block 1039]
དེ་ཡུལ་མཉམ་པ་ནི་ཌི་མ་སྟེ་གཡུང་མོ་ཉེ་བར་མཚོན་པ་སྟེ་བྲམ་ཟེ་མོའི་བར་དུ་མི་སྤང་བར་སྤྱད་དོ། །ཀྱེ་ཧ་ཧི་ནི་བྷ་ཛའི་སྟེ་མི་སྤང༌[^1149]བར་བཤད་དོ། །

[Block 1040 [HEADING]]
###### **སྦྱོར་བ་མཉམ་པ།** ^2-4-1-1-2-2-0

[Block 1041]
སྦྱོར་བ་མཉམ་པ་ནི་མ་ལཱ་ཛེ་སྟེ་ཡབ་ཡུམ་ལུས་ཆ་མཉམ་པ་དང་ཀུན་དུ་རུ་བྷ་ཏ་ཧི༌[^1150]སྙོམས་འཇུག་ལས་བྱུང་བའི་ཞུ་བ་དེ་མཉམ་པར་མི་སྤང་བའོ། །

[Block 1042 [HEADING]]
##### གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ། ^2-4-1-2-0

[Block 1043]
ད་ནི་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་ལ་རྗེས་སུ་ཆགས་པའི་ཆོས་སུ་བསྟན་པའི་ཕྱིར་ལ་ཚིག་བཞི་བཞི༌[^1151]ལ་རྐང་པ་གཉིས་སུ་སྦྱར་ཏེ་བླང་ངོ་། །དེ་ཡང་བཞི་སྟེ། སྙོམས་པར་འཇུག་པའི་སྦྱོར་བ་དང་ལྡན་པ་དང་། ཡོན་ཏན་སྤོང་བའི་ཁྱད་པར་དང༌[^1152]ལྡན་པའི་སྦྱོར་བ་དང་། ཡོན་ཏན་ཐོབ་པའི་ཁྱད་པར་དང་ལྡན་པའོ། །སྦྱོར་བ་དང་དབྱེར་མེད་བསྒོམ་པའི་ཁྱད་པར་ལྡན་པའི་སྦྱོར་བའོ། །

[Block 1044 [HEADING]]
###### སྙོམས་པར་འཇུག་པའི་སྦྱོར་བ། ^2-4-1-2-1-0

[Block 1045]
དེ་ལ་སྙོམས་པར་འཇུག་པའི་སྦྱོར་བའི་ཆོས་ནི་ཀོལླ༌[^1153]ཨི་རི་སྟེ་རྣལ་འབྱོར་པའི་ལུས་དང་པོ་ལ་སྟེ་གསང་བའི་ལུས་སོ། །མུམྨུ་སྟེ་རྣལ་འབྱོར་མའི་ལུས་དང་ཀ་ཀྐོ་ལ་སྟེ་གསང་བའི་གནས་སོ། །གྷ་ཎ་སྟེ་ཕྲད་ཅིང་ཞུགས་པའོ། །ཀྲྀ་པི་ཊ་ཧོ་བཛྲ་ཨི་གདུངས་ཤིང་བརྩེ་བའི་ངག་སྟོན་པས་སོ། །ཀཱ་རུ་ཎི་ཀ་ཨ་ཨི་ཎ་རོལ་ཏེ་ཆགས་ཤིང་གདུངས༌[^1154]པའི་སེམས་ཤིན་ཏུ་འཕེལ་བའོ། །དེ་ནས་ཌི་ཎྜི་མ་ཏ་ཧིནྣ་བཱཛྫི་ཨ་ཨི་སྟེ། དེས་གཡུང་མོ་ལ་སོགས་པ་ཡང་མི་སྤོང་བར༌[^1155]རོ། །མ་ལ་ས་ཛ་འདུས་པ་ལུས་མཉམ་པར་སྦྱོར་བ་ཞུ་བདེ་ཆ་མཉམ་པའོ། །

[Block 1046 [HEADING]]
###### ཡོན་ཏན་སྤོང་བའི་ཁྱད་པར། ^2-4-1-2-2-0

[Block 1047]
དེ་ནས་ཡོན་ཏན་སྤོང་བའི་ཁྱད་པར་བ་ལ་ཁཱ་ཛྫ་ཨི་སྟེ་བདེ་བ་རྟོག་པ་སྤངས་ནས་མི་རྟོག་པ་ལ་འཇུག་པའོ། །ག་ཌྷེཾ་མ་སྟེ་འབད་པས་ཞུ་བ་དང་མི་འབྲལ་ཞིང་། །འཐུངས་པས་དམ་ཚིག་ཏུ་ལུས་རྒུད་པ་མེད་པར་སྟོབས་ཅན་དུ་འབྱུང་ངོ་། །ཧ་ལེ་ཀཱ་ལི་སྟེ་ལྷན་ཅིག་སྐྱེས་པའི་སྐལ་བ་དང་ལྡན་པས་སོ། །དུཾ་དུ་ར་ནི་སྐལ་མེད་སྤོང་བ་སྟེ་ཆགས་པ་ལ་སོགས་པའི་སྐལ་མེད་སྤོང་བའོ། །དེ་ནས་ཚིག་རྐང་གཉིས་ཀྱིས་སྦྱོར་བ་སྔ་མ་བཞིན་ནོ། །

[Block 1048 [HEADING]]
###### ཡོན་ཏན་ཐོབ་པའི་ཁྱད་པར། ^2-4-1-2-3-0

[Block 1049]
ད་ནི་ཡོན་ཏན་ཐོབ་པའི་ཁྱད་པར་ནི་རྣལ་འབྱོར་མ་ལ་ཙ་ཨུ་ས་མ་ལ་སོགས་པ་ཕུང་པོ་ལྔའི་བདག་ཉིད་ཀྱི་རོ་བསྡུས་པ་ཞུ་བ་ཀུནྡ་ལྟ་བུར་ཨ་ཨི་བྷ་རུ་སྟེ། ལུས་གང་བས་འཇོག་གི་གཉུག་མའི་ཡེ་ཤེས་ཐོབ་པའོ། །རྣལ་འབྱོར་མས་ནི་ཙ་ཨུ་ས་མ་ལ་སོགས་པ་འབྱུང་བ་ལྔའི་རོའི་བདག་ཉིད་འདུས་པ་ཉི་མའི་རྣམ་པ་ཅན་ཀུན་འདུས་ལུས་བཀང་བས་གཉུག་མའི་ལུས་ཐོབ་པའོ། །ཚིག་རྐང་གཉིས་ཀྱིས་སྦྱོར་བ་ནི་འདིར་ཡང་སྔ་མ་བཞིན་ནོ། །

[Block 1050 [HEADING]]
###### དབྱེར་མེད་སྒོམ་པའི་ཁྱད་པར། ^2-4-1-2-4-0

[Block 1051]
ད་ནི་དབྱེར་མེད་སྒོམ་པའི་ཁྱད་པར་ནི་ཀུན་རྫོབ་བྱང་ཆུབ་སེམས་ཏེ་མན་ངག་གི་ཚུལ་དུ་གཟུང་བ་དང་དམ་ཚིག་ཏུ་བཟའ་བའོ། །མན་ངག་གི༌[^1156]སྒྲུབ་པ་ནི་ས་འོག་ས་སྟེངས་ས་བླ་མ་ཡིན་པ་ནམ་མཁའི་དཀྱིལ་དུ་ཕྲེཾ་ཁ་ཎ་སྟེ། འགྲོ་འོང་གི་དོགས་པ་མེད་བར་མི་གཡོ་བར་གཟུང་བའོ། །

[Block 1052]
དམ་ཚིག་གི་ཚུལ་ནི་ལག་པ་དང་སྣོད་མ་ཡིན་པར་དག་པ་དང་མ་དག་པར་གཙང་བ་དང་མི་གཙང་བ་མེད་པར་ལྕེས་བླང་ངོ་། །དེ་ཡང་མན་ངག་དག་གིས་གཟུང་བ་ནི་ནི་རཾ་ཤུ་སྟེ། ལུས་ཐམས་ཅད་རུས་པ་དང་འདྲ་བར་བརྒྱན་པ་གཉུག་མའི་བདེ་བ་ལ་འཇུག་གོ། །དེ་ཡང་དམ་ཚིག་ཏུ་ཟོས་པས༌[^1157]ཏ་ཧིཾ་ཛ་ས་ར་ཝའི་རོ་དང་འདྲ་བར་རྟོག་པ་མེད་པར་འཇུག་གོ། །གཡུང་མོ་མི་སྤོང་བ༌[^1158]དང་ཀུན་དུ་རུ་ནི་སྔ་མ་ལྟར་གཞན་དག་ལ་སྦྱར་རོ། །

[Block 1053 [HEADING]]
##### རང་ལུས་ཐབས་དང་ལྡན་པ། ^2-4-1-3-0

[Block 1054]
རང་ལུས་ཐབས་དང་ལྡན་པ་ནི། ཀོ་ལ་ཨི་རི་ཊྛི་སྟེ་མགོ་བོའི་གནས་སོ། །བོ་ལ་སྟེ་ཧཾ་ངོ་། །མུམྨུ་སྟེ་ལྟེ་བའོ། །ཀཀྐོ་ལ་སྟེ་ཨཾ་ངོ་། །གྷ་ཎ་སྟེ་བྱང་ཆུབ་ཀྱི་སེམས་རྒྱུན་སྟེང་འོག་ཏུ་འདུས་པའོ། །ཀྲྀ་པི་ཊ་སྟེ་ནཱ་དའི་སྒྲ་སྐྲའི་རྩེ་མོ་དབབ་པས་ཕྲ་བའོ། །ཀཱ་རུ་ཎི་སྟེ་ཆགས་པས་ནང་དུ་བལྟས་པའོ། །ཨ་ཨི་ན་སྟེ་ཕྱི་རོལ་དུ་མི་གཡེངས༌[^1159]པས་སོ། །བ༌[^1160]ལ་ཁཱཛྫ་སྟེ་ཕྱི་རོལ་གྱི་རྟོག་པ་སྤངས་པའོ། །གཌྷེཾ་སྟེ་ནང་གི་རོ་མྱང་བའོ། །ཧ་ལེ་ཀཱ་ལི་སྟེ་རླུང་སྐལ་བ་དང་ལྡན་པར་ནང་དུ་བཅུག་པས་སོ། །

[Block 1055]
དུཾ་དུ༌[^1161]ར་སྟེ་ཕྱི་རོལ་གྱི་རྟོག་པ་གཟུང་བའི་ཡུལ་སྤང་ངོ་། །ཙ་ཨུ་ས་མ་ལ་སོགས་ཉོན་མོངས་པ་ལྔའོ། །ག་ཎ་བཟའ་སྟེ་དེ་དག་རང་རིག་འོད་གསལ་དུ་མི་རྟོག་པའོ། །ཕྲེཾ་ཁ་ཎ་སྟེ་སྟེང་ནས་བྱང་ཆུབ་ཀྱི་སེམས་རྒྱུ་བ་དང་འོག་ནས་རླུང་དང་འོད་ཟེར་རྒྱུ་བ་སྟེ་དེ་གཉིས་ལ་ཤུདྡྷ་ཨ་ཤུདྡྷ་སྟེ། བཟང་ངན་དུ་མི་རྟོག་གོ། །ནི་རཾ་ཤུ་སྟེ་ཞུ་བ་འདུས་པ་སྟེ་ཡང་སར་པ་སྟེ་རོ་དང་འདྲ་བའི་བདེ་བ་ལ་མི་རྟོག་པ་སྐྱེ་བའོ། །དེ་ལྟར་དེ་ཉིད་གཡུང་མོ་ལ་སོགས་པ་ལྟོས་པ་མེད་ཅིང་སྤང་བླང་མེད་པར་ནང་གི་ཀུན་དུ་རུའི་སྦྱོར་བའོ། །
--- END BLOCKS ---
