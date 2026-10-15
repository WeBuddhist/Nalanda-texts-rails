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
དུས་གཞན་གྱི་ཚེ་ན་འབབ་པ་གཞན་སྦྱིན་པའི་ཕྱིར་དང་འབབ་པ་ལྷགས་པ༌[^990]དང་བྲལ་ན་དབྱར་གྱི་གོས་རས་ཆེན་བཞིན་དུ་ཞེས་བྱ་བ་འདི་ལྟ་བུ་ཆུ་མེད་པའི་ཕྱིར་གཞག་པར་བྱའོ། །

[Block 1157]
ནད༌[^991]གསོ་བའི་དོན་དུ་ནི་འདི་དག་ནི་ཉེ་བར་དགོས་པའོ། །

[Block 1158]
བཅས་པའི་ཁ་ན་མ་ཐོ་བ་ཐམས་ཅད་རྗེས་སུ་གནང་བས་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 1159]
བླ་མའི་དྲུང་དུ་མཆིལ་ལྷམ་བགོ་བ་བསྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་ཉིད་ཀྱི་སྤྱན་སྔར་མཆིལ་ལྷམ་གྱོན་ཞིང་འཆག་པའི༌[^992]དགེ་སློང་སྨད་པ་ན་དགེ་སློང་དག་ལ་ཡང་ཚུལ་དེ་ཉིད་སྨད་པ་ཡིན་པས་དེའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 1160]
སེང་གེ་དང་སྟག་དང་གུང་དང་། གླང་པོ་ཆེ་ཅང་ཤེས་དང་རྟ་ཅང་ཤེས་ཀྱི་ཡན་ལག་ཅུང་ཟད་ཀྱང༌[^993]ལུས་ལ་གདགས་པར་མི་བྱ་བ་ཉིད་དེ༌[^994]ཞེས་བྱ་བ་ལ་ཅུང་ཟད་ཀྱང་ཞེས་བྱ་བ་ཡང་འདིར་གཞུང་ནི། ཕྲན་ཚེགས་དག་ལས་སེང་གེ་དང་དེ་ལས་གཞན་པའི་རི་དྭགས་གཏུམ་པོ་རྣམས་ལ་ཡང་འདིར་བསྙེགས་པའོ། །

[Block 1161]
དེ་དག་གིས༌[^995]གླང་པོ་ཆེ་ཕལ་པ་དང་རྟ་དམུ་རྒོད་དང་། དེ་ལས་གཞན་པའི་གཅན་གཟན༌[^996]དག་ལ་འཕངས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་དག་གིས་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། གླང་པོ་ཆེ་དང་སྟག་དང་གུང་དང་གླང་པོ་ཆེ་ཅང་ཤེས་དང་། སེང་གེ་ལ་སོགས་པ་རྣམས་ཀྱིས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1162]
མཆིལ་ལྷམ་དག་གདབ་པར་མི་བྱའོ། །

[Block 1163]
རས་མ་གཤེར་བ་དག་གིས་དེ་དག་གི་རྡུལ་མེད་པར་བྱ་བའི་ཕྱིར་ཕྱི་བར་བྱའོ་ཞེས་བྱ་བ་ལ།

[Block 1164 [VERSE]]
དེ་དག་ཅེས༌[^997]བྱ་བ་ནི་མཆིལ་ལྷམ་མོ། །
དེ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ།
དེ་ཞེས་བྱ་བ་ནི་ཕྱི་བའི༌[^998]རས་མའོ། །

[Block 1165]
དེ་དག་བརྒྱུ་བར༌[^999]བྱའོ་ཞེས་བྱ་བ་ནི་མཆིལ་ལྷམ་དེ་དག་གོ། །

[Block 1166]
མི་མཛེས་པའི་དངོས་པོ་དབེན་པའི་ཕྱོགས་སུ་བྱའོ་ཞེས་བྱ་བ་ནི། ལྷུང་བཟེད་གླན་པ་ལ་སོགས་པ་མི༌[^1000]མཛེས་པའི་དངོས་པོ་ཐམས་ཅད་དབེན་པའི་ཕྱོགས་སུ་ལས་བྱེད་པ་ཞེས་བྱ་བ་ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བར་བསྒྲུབ་པའོ། །

[Block 1167]
དེའི་ཆེད་དུ་སྨྱུང་བུ་དང་ཀོ་བ་བཅང་བར་བྱ་སྟེ། དྲ༌[^1001]གྲི་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེའི་ཆེད་དུ་ཞེས་བྱ་བ་ནི་མཆིལ་ལྷམ་དེ་བརྒྱུ་བའི་དོན་དུའོ། །

[Block 1168]
འདིར་གཞུང་ནི། སྨྱུང་བུ་དང་ཀོ་བ་བཅང་བར་བྱའི་དྲ༌[^1002]གྲི་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1169]
ཁྱིམ་གཞན་དང་ཆབ་ཁུངས་ལས་གཞན་པར་ཤིང་གི་མཆིལ་ལྷམ་བགོ་བར་མི་བྱ་བའོ།[^1003] །

[Block 1170]
སྨྱུག་མའི་གླེགས་བུ་མུན་ཛ་དང་། སི་རི༌[^1004]དང་དར་བ་དག་གིས་ཡང་མི་བྱའོ། །

[Block 1171]
ཐ་གུའི་ཡང་ངོ་། །རླུང་དྲག་ཅན་མ་ཡིན་པས་སོ་ཞེས་བྱ་བ་ནི་གང་ཟག་རླུང་དྲག་ཅན་མ་ཡིན་པས་ཐ་གུའི་མཆིལ་ལྷམ་བགོ་བར་མི་བྱའོ། །

[Block 1172]
རླུང་དྲག་ཅན་གྱི་ནད་པས་ནི་མི་འདྲུལ་བར་བྱ་བའི་ཕྱིར་ཆག་ཆག་གདབ་པ་ལ་འདིར་དེའི་རྗེས་སུ་མཐུན་པར་བྱའོ། །

[Block 1173]
འདི་ནི་གཙོ་བོར་དོན་མཉམས་པར་ཡིན་གྱི་ནད་གསོ་བ༌[^1005]ནི་མ་ཡིན་ནོ། །

[Block 1174]
དེ་ལྟ་བས་ན་བཅས་པའི་ཁ་ན་མ་ཐོ་བ་འདི་མ་གྲུབ་པ་ནི་མ་ཡིན་ཏེ། ནད་པ་ལ་རྗེས་སུ་གནང་བས་འདིར་སྨྱུག་མའི་གླེགས་བུ་ལ་སོགས་པ་ལ་ཕལ་ཆེར་དབུལ་བར་བྱེད་པ་ཉིད་དང་ཤིན་ཏུ་མི་མཐུན་པར་བྱེད་པ་ཉིད་དང་ཤིང་གི་ལྷམ་ནི་ཤིན་ཏུ་སྐྱོན་དང་ལྡན་པ་ཉིད་དོ། །

[Block 1175]
དེ་བས་ན་འདིར་དེའི་ཐ་ཚིག་གོ། །

[Block 1176]
ཁྱིམ་གཞན་དུ་གཞན་མེད་ན་ཀོ་ལྤགས་ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། གཞན་ཞེས་བྱ་བ་ནི་སྟན་གཞན་ན་མེད་ནའོ། །

[Block 1177]
དེར་ཡང་རྐྱེན་དེ་ལྟ་བུ་དག་མེད་ན་ཉལ་བར་མི་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེར་ཡང་ཞེས་བྱ་བ་ནི་ཁྱིམ་གྱི་ནང་དུའོ། །

[Block 1178]
དེ་ལྟ་བུ་དག་ནའོ་ཞེས་བྱ་བ་ནི་ཀོ་ལྤགས་སོ། །

[Block 1179]
འདི་ནི་མ་མོ་ལས།

[Block 1180]
མཆིལ་ལྷམ་དུ་གྱུར་པའི་ཀོ་ལྤགས་ལ་ཀོ་ལྤགས་ཉིད་མ་ཡིན་ཏེ། དེའི་ཕྱིར་ཕྲེང་ཐག་གི་ཆོ་ག་ལ་ཡུལ་མ་ཡིན་པར་ཤེས་པར་མི་བྱའོ། །

[Block 1181]
མིག་ལ་ཕན་པར་བྱ་བའི་ཕྱིར་དོམ་ལྤགས་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། དོམ་གྱི་པགས་པ་བླང་བར༌[^1006]རྗེས་སུ་གནང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1182]
རྐང་པའི་གནས་སུ་གདིང་བར་བྱ་བའོ་ཞེས་བྱ་བ་ནི་དོམ་ལྤགས་བླངས་པ་དེའོ། །

[Block 1183]
སངས་རྒྱས་ཀྱི་ནི་དྲི་གཙང་ཁང་གི་སྒོར་རོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་དབང་བའི་དོམ་ལྤགས་དགེ་སློང་ངམ་གཞན་གྱི་དྲི་གཙང་ཁང་གི་སྒོར་གདིང་བར་བཅས་པའོ། །

[Block 1184]
མཆིལ་ལྷམ་དག་ཏུ་བགོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མིག་ལ་ཕན་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1185]
རླུང་ནད་ཅན་གྱི་ནི་འདུག་པ་དང་ཉལ་བར་ཡང་བྱའོ་ཞེས་བྱ་བ་ནི་དོམ་གྱི་པགས་པ་དེའི་སྟེང་དུའོ། །

[Block 1186]
གཞང་འབྲུམ་ཅན་ཐམས་ཅད༌[^1007]ཀྱིས་ཀྱང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་རྐང་པའི་གནས་སུ་གདིང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིར་དེ་རྣམས་ལ་རླུང་ནད་ཅན་དང་། ལྷན་ཅིག་ཏུ་འདུག་པ་དང་ཉལ་བར་ཡང་བྱ་བ་སྨོས་སོ། །

[Block 1187]
འདིར་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས།

[Block 1188]
མཆིལ་ལྷམ་གདིང་བར་བྱའོ། །

[Block 1189]
དེ་བས་ན་དགེ་སློང་གཞང་འབྲུམ་ན་བས་དོམ་ལྤགས་ཀྱི་མཆིལ་ལྷམ་དག་བཅང་བར་རྗེས་སུ་གནང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ༌[^1008]ཞེས་བྱ་བའི་རྗེས་སུ་འབྲངས་པས་རྐང་པའི་གནས་སུ་ཡང་བཅས་པའོ། །

[Block 1190]
འདིར་ཡོ་བྱད་ཅེས་གསུངས་སོ། །

[Block 1191]
དེ་ལ་དེ་ལྟར་སྦྱར་བར༌[^1009]བྱའོ་ཞེས་བྱ་བ༌[^1010]ནི་དོམ་གྱི་པགས་པ་དེ་ལའོ། །

[Block 1192]
སྤུ་ལ་རེག་པས༌[^1011]ཕན་པར་བྱེད་པ་ཉིད་དུ་རེག༌[^1012]གོ་ཞེས་བྱ་བ་ནི་དོམ་ལྤགས་ཀྱི་སྤུ་ལས་སོ། །

[Block 1193]
དགེ་སློང་དག་དོམ་ལྤགས་ཀྱི་སྤུ་དག་འོག་ཏུ་སྟོན་པར༌[^1013]བྱེད་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྤུ་དག་གྱེན་དུ་བསྟན་པར་བྱའོ་ཞེས་གསུངས་པ་དེ༌[^1014]འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 1194]
མཆིལ་ལྷམ་དག་རིམ་པ་མང་པོ་ཉིད་ཀྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་ཕན་པ་བྱེད་པ་ཉིད་དུ་རིག་གོ་ཞེས་བྱ་བར༌[^1015]སྦྱར་ཏེ། རིམ་པ་གཅིག་པ་ཡང་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་དུ་ཕན་པར་བྱེད་པ་ཉིད་ཡིན་པས། དེ་བས་ན་རབ་ཀྱི་དགོངས་པ༌[^1016]ཅན་ཏེ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 1195]
དུ་མའི་སྟེང་དུ་གཅིག་གཞག་པས་ཀྱང་ངོ༌[^1017]ཞེས་བྱ་བ་ནི་ཀོ་ལྤགས་བཞིན་རིམ་པ་དུ་མའི་སྟེང་དུ་དོམ་ལྤགས་གཅིག་གཞག་པས་ཀྱང་ཕན་པར་བྱེད་པ་ཉིད་དུ་རིག་གོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། སྔ་མའི་རྣམ་པ་མེད་པ་ལ༌[^1018]གང་བསྟེན་པ༌[^1019]ཉིད་དུ་རིག་པར༌[^1020]བྱའོ། །
--- END BLOCKS ---
