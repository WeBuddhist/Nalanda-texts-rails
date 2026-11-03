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
[Block 1296]
སྨན་ཁུ་དང་མིག་སྨན་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་།[^1126] སོས་པ་ཉིད་ན་དེ་དག་ནད་པའི་ཕྱིར་སློང་ན་སྦྱིན་ནོ་ཞེས་བྱ་བ་དང་། དེ་མེད་ན་སྨན་ཁང་དུ་གཞག་གོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1297]
ད་ནི་བཞི་པ་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་འཚོ་བའི་བར་དུ་བཅང་བ་ནི་རྩ་བ་དང་། སྡོང་བུ་དང་འདབ་མ་དང་། མེ་ཏོག་དང་འབྲས་བུ་ཟས་ཀྱི་དོན་དུ་ཁྱབ་པར་བྱེད་པ་མ་ཡིན་པའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1298]
ཁ་ཟས་ཀྱི་དོན་དུ་ཁྱབ་པར་བྱེད་པ་མ་ཡིན་པ་དེ་དག་འཚོ་བའི་བར་དུ་བཅང་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1299]
དེ་ལ་རྩ་བ་དག་གང་ཞེ་ན་འདི་ལྟ་སྟེ་གླ་སྒང་དང་ཤུ་དག་དང་། ཡུང་བ་དང་། སྒེའུ་གཤེར་དང་བོང་ང་དཀར་པོ་དག་གོ། །

[Block 1300]
སྡོང་བུ་དག་གང་ཞེ་ན། ཙན་དན་དང་། སྦྱི་མོ་དང་ཤུག་པ་དང་སྲེ་ཏྲེས༌[^1127]དང་། ཐང་ཤིང་དང་སྐྱེར་པ་དག་གོ། །

[Block 1301]
འདབ་མ་དག་གང་ཞེ་ན། བ་ཤ་ཀ་དང་ཀོ་ཤ་ཏ་ཀི་དང་། པ་ཏོ་ལ་དང་ནི་མ་པ༌[^1128]དང་། སཔྟ་པརྞའི་འདབ་མ་དག་གོ། །

[Block 1302]
མེ་ཏོག་དག་གང་ཞེ་ན། མེ་ཏོག་ནི་བ་ཤ་ཀ་དང་། ནིམ་པ༌[^1129]དང་། ཧ༌[^1130]ད་ཀི་དང་། ཀླུ་ཤིང་དང་པདྨའི་ཟེ་བ་དག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟེ་བ་དེ་དག་ཀྱང་མཚོན་པ་ཙམ་དུ་ཟད་ཀྱི། མེ་ཏོག་ལས་ཕལ་ཆེར་སྨན་ཟས་ཀྱི་དོན་དུ་ཁྱབ་པར་བྱེད་པ་མ་ཡིན་པ་གཞན་དག་ཐ་དད་དུ་བྱས་ནས་བསྡུས་པའོ། །

[Block 1303]
འབྲས་བུ་དག་གང་ཞེ་ན། ཨ་རུ་ར་དང་། སྐྱུ་རུ་ར་དང་། བ་རུ་ར་དང་། ན་ལེ་ཤམ་དང་། པི་པི་ལིང་དག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྩ་བ་དང་སྡོང་བུ་དང་འདབ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་རྣམས་བཤད་ནས། གཞན་འཚོ་བའི་བར་དུ་བཅང་བར་བསྟན་པའི་ཕྱིར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1304]
དེ་ཉིད་བསྟན་པའི་ཕྱིར་སྤྱིལ་བའོ། །

[Block 1305]
འདི་ལྟ་སྟེ་ཤིང་ཤུན་དང་ཕྲ་རྩི༌[^1131]དང་རྒྱ་སྐྱེགས་དང་སྤྲ་ཚིལ་དང་ཤིང་མ་ཞོའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ལྟ་སྟེ་ཞེས་བྱ་བའི་སྒྲས་ནི་འོག་མ་རྣམས་ལ་ཡང་དཔེར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1306]
རྒྱ་སྐྱེགས་ནི་རྒྱ་སྐྱེགས་སོ། །

[Block 1307]
སྤྲ་ཚིལ་ནི་སྤྲ་ཚིལ་ལོ། །

[Block 1308]
ཤིང་མ་ཞོ་ཞེས་བྱ་བ་ནི། རྒྱ་སྐྱེགས་ལས་གཞན་པའི་ཤིང་དག་གི་ཤིང་མ་ཞོ་དག༌[^1132]སྟེ། ཤིང་དག་ལས་འབྱུང་བའོ། །

[Block 1309]
འགྱུར་བྱེད་དོ་ཞེས་བྱ་བ་ནི་འདི་ལྟ་སྟེ།[^1133] ཏིལ་གྱི་དང་རྒྱ་སྐྱེགས་ཀྱི་ཤིང་དང་། ས་ཚུར༌[^1134]གྱི་དང་། ནས་ཀྱི་དང་། ནས་ཀྱི་དྲ་མའི་དང་། བ་ཤ་ཀའི༌[^1135]དང་ཐལ་བའི་འགྱུར་བྱེད་དོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1310]
ལན་ཚྭའོ༌[^1136]ཞེས་བྱ་བ་ནི། འདི་ལྟ་སྟེ་རྒྱམ་ཚ༌[^1137]དང་། ཁ་རུ་ཚ༌[^1138]དང་། ཚ་དམར༌[^1139]དང་། རྒྱ་མཚོའི་ཚ༌[^1140]དང་། བ་ཚའོ༌[^1141]ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1311]
སྨན་ཁུའོ་ཞེས་བྱ་བ་ནི། འདི་ལྟ་སྟེ། ཤིང་ཨ་མྲ་དང་ནིམ་པ་དང་ཀོ་ཤམ་པ༌[^1142]དང་ཤི་རི་ཤ་དང་འཛམ་བུ་དག་གོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1312]
ཇི་ཙམ་གྱིས་ཆོག་པ་བསྟན༌[^1143]ནོ། །

[Block 1313]
བཀྲུས་ནས་ཡང༌[^1144]ངོ་ཞེས་བྱ་བ་ནི། ཇི་ཙམ་གྱིས་ཆོག་པ་བསྟེན་ཏོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1314]
མི་མཉེ་བ་ལན་ཅིག་བཀྲུའོ་ཞེས་བྱ་བ་ནི་དེ་ལ་རེག་པ་མེད་པས་ན་རེག་པ་མེད་པའོ། །

[Block 1315]
སྨན་ཁུ་དེ་ལྟར་བསྟན༌[^1145]ནོ་ཞེས་བྱ་བ་ནི་རྣམ་པ་དེ་ལྟར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1316]
སྐམ་སྔོ་ལ་སོགས་པ་ལ༌[^1146]ཡང་དེ་བཞིན་ནོ། །

[Block 1317]
སྨན་སྨོས་པས་དུག་སྨན་མ་བསྡུས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་ཡང་སྨན་ཞེས་བྱ་བས་དུག་སྨན་ཡང་བསྡུས་པར༌[^1147]རིག་པར་བྱའོ། །

[Block 1318]
དེ་ནི་འཚོ་བའི་བར་དུ་བཅང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་དུག་སྨན་དེ༌[^1148]ལའོ། །

[Block 1319]
འདིར༌[^1149]གཞུང་ནི། གང་ཞིག་བུ་རམ་ཤིང་དང་བུ་རམ་གཉིས་བསྲེགས་པའི་ཐལ་བ་ནི་འཚོ་བའི་བར་དུ་བཅང་བའོ་ཞེས་གསུངས་སོ། །

[Block 1320]
སིལ་བུ་རྣམས་ལས་ཀྱང་འདི་གསུངས་སོ། །

[Block 1321]
ནུ་ཞོས་འཚོ་བའི་བེའུ་རྣམས་ཀྱི་ལྕི་བ་དང་། གཅིན་དག་ནི་དེ་ཞེས་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དུག་སྨན་དེ་ལའོ། །

[Block 1322]
འདིར་གཞུང་ནི། གང་ཞིག་དེ་ཞེས་བྱ་བ་ནི་དུག་ལ་ཕན་ནོ་ཞེས་བྱ་བ་ནི། ལྕི་བ་དང་གཅིན་ལ་སོགས་པ་དུག་སྨན་ཞེས་བྱ་བ་ཇི་སྐད་བསྟན་པ་དེ་དག་ནི་དུག་ཟོས་པ་ལ་ཕན་ནོ། །

[Block 1323]
ཐལ་བའོ་ཞེས་བྱ་བ་ནི་ཤིང་ཀ་ཙ༌[^1150]ན་དང་། ཀ་བི་ཀ་ལ་དང་། ཨ་ཤྭདྠ་དང་། ཨུ་དུམ་བཱ་ར་དང་། ནྱ་གྲོ་དྷ་རྣམས་ཀྱི་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའོ་ཞེས་བྱ་བ་ནི་དུག་ལ་སྨན་པའོ། །

[Block 1324]
ས་ནི་སོར་བཞིའི་འོག་གི༌[^1151]བཟང་ངོ་ཞེས་བྱ་བ་ནི་རླུང་དང་ཉི་མ་ལ་སོགས་པ་རྣམས་ཀྱིས་སྟེང་གི༌[^1152]ལ་གནོད་པའི་ཕྱིར་རོ། །

[Block 1325]
འདིར་གཞུང་ནི། དགེ་སློང་དག་དུག་སྨན་ཞེས་བྱ་བ་ནི་ལྕི་བ་དང་གཅིན་དང་ཐལ་བ་དང་ས་སྟེ། དེ་ལ་ལྕི་བ་ནི་བེའུ་འབྲངས༌[^1153]ནས་རིང་པོ་མ་ལོན་པ་མའི་ནུ་ཞོས་འཚོ་བ་གང་དག་ཡིན་པ་རྣམས་ཏེ་གཅིན་ཡང་དེ་དག་ཉིད་ཀྱིའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 1326]
དེ་དགེ་བསྙེན་དད་པ་ཅན་ལས་བླང་ངོ་ཞེས་བྱ་བ་ལ་དེ་ནི༌[^1154]ཞེས་བྱ་བ་ནི་དུག་སྨན་དེའོ། །

[Block 1327]
འདི་ནི་སིལ་བུ་དག་ལས་དེས་བྱིན་ལེན་ཡང་ངོ་། །དེས་བྱིན་ལེན་བསྟབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བྱིན་ལེན་ཡང་དགེ་བསྙེན་དད་པ་ཅན་དེས་བསྟབ་པར་བྱའོ། །

[Block 1328]
ཤའི་བདག་ཉིད་ཀྱི་སྨན་དེ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་། ཤའི་བདག་ཉིད་ཀྱི་སྨན་དེ་ལ་དེས་བྱིན་ལེན་བསྟབ་པར་བྱའོ། །

[Block 1329]
ཐམས་ཅད་ཤན་པའི་གནས་ནས་བླང་ངོ་ཞེས་བྱ་བ་ནི་ཤ་རློན་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་ཤའི་སྨན་ཐམས་ཅད་དགེ་བསྙེན་དད་པ་ཅན་གྱིས་ཤན་པའི་གནས་ནས་བླང་བའོ། །

[Block 1330]
དེ་ནི་བྱ་བ་ཉིད༌[^1155]ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཤའི་སྨན་བླང་བ་དེ་ནི་ཤན་པའི་གནས་ནས་བླང་བ་ཉིད་དོ། །

[Block 1331]
དེ་ལ་བྱ་བའི་ཆ་མ་ཡིན་པར་དོགས་པ༌[^1156]མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1332]
གལ་ཏེ་དུས་མ་ཡིན་པར་ནས་ལས་བྱས་པའི་སྨན་དགོས་པ་ཉིད་ཡིན་ན་དེའི་དོན་དུ་བ་ལང་རྒན་པོའི་ལྕི་བའི་ནས་ཀྱིས་ཆོག་པར་བྱའི་གཞན་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་དོན་དུ་ཞེས་བྱ་བ་ནི་ནས༌[^1157]ལས་བྱས་པའི་སྨན་དེའི་དོན་དུའོ། །

[Block 1333]
གཞན་ཞེས་བྱ་བ་ནི་ནས༌[^1158]གཞན་དག་གོ། །

[Block 1334]
གལ་ཏེ་སྐྱོ་མ་ཚགས་ཀྱིས་བཙགས་ནས་ཏེ་གཞན་ནི༌[^1159]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དུས་མ་ཡིན་པར་ཟ་བར་བྱ་བ་ཉིད་ལ་གང་ཞིག་སྨན་དུ་བྱས་པ་དེའི་དོན་དུ་བྱའི་ནས་ལས་བྱས་པ་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1335]
དེ་རྣམས་ལ་ཡང་བ་ལང་རྒན་པོའི་ལྕི་བའི་ནས་ཀྱིས་ཆོག་པར་བྱའི་གཞན་བཟའ་བར་མི་བྱའོ། །
--- END BLOCKS ---
