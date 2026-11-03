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
[Block 1226]
བཙུན་པ་ཐུན་ཚོད་དུ་རུང་བ་དང་། ཞག་བདུན་པ་དང་། འཚོ་བའི་བར་དུ་བཅང་བར་བྱ་བའི་སྨན་བྱིན་གྱིས་བརླབས་པ་གང་དག་ལགས་པ་དེ་དག་བྲོ་མི་འཚལ་བས་ཡོངས་སུ་སྤྱད་དུ་རུང་ངམ། ཉེ་བ༌[^1052]འཁོར་མི་རུང་ངོ་། །བྱིན་ལེན་བགྱིས་པ་དང་བྱིན་གྱིས་བརླབས་པ་དེ་དག་བྲོ་འཚལ་བས་ཡོངས་སུ་སྤྱད་དུ་རུང་ངམ། ཉེ་བ༌[^1053]འཁོར་རུང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1227]
བཙོ་ཚ༌[^1054]དང་ཆུ་ཤིང་གི་འབྲས་བུ་དང་། རྒྱ་ཤུག༌[^1055]དང་ཨ་ཤྭདྠ་དང་། ཨུ་དུམ་བཱ་ར་དང་རྩུབ་འགྱུར་དང་། རྒུན་ཆུ་དང་། འབྲ་གོའི་བཏུང་བ་རྣམས་ནི་ཐམས་ཅད་དུའོ་ཞེས་བྱ་བ་ལ་ཐམས་ཅད་དུའོ༌[^1056]ཞེས་བྱ་བ་ནི་ན་བ་དང་། མི་ན་བའི་ཕྱིར་བཙོ་ཚ༌[^1057]ལ་སོགས་པའི་བཏུང་བ་བརྒྱད་པོ་འདི་རྣམས་ལ་ཐམས་ཅད་ཉིད་ཀྱི་ཕྱིར་དང་པོ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 1228]
ནད་པ་མ་ཡིན་པའི་ཕྱིར་ཏེ། ནད་པ་ཁོ་ནའི་ཕྱིར་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1229]
བཙོས་པའི་ཚ༌[^1058]དང་། འབྲུའི་ཚ་དང༌[^1059]ཞོ་ག་ཆུ༌[^1060]དང་། དར་བའི་དངས་མ་དང་། རྩབ་མོ་ཆུས་བཏབ་པ་ཚགས་ཀྱིས་བཙགས་པ་ཤིན་ཏུ་སླ་བ༌[^1061]བཞིན་སྣང་བ་འདམ་བུའི་ཉག༌[^1062]མའི་མདོག་ལྟ་བུ༌[^1063]དག་ཀྱང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ལ་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་སྟེ་བཙོ་ཚ༌[^1064]ལ་སོགས་པའི་བཏུང་བའང་དེ་དང་འདྲའོ་ཞེས་སྦྱར་རོ། །

[Block 1230]
འདི་རྣམས་ཀྱང་ཞོ་ག༌[^1065]ཆུའི་བྱེ་བྲག་དང་ལྡན་པ་རྣམས་ལ་ཐམས་ཅད་ཀྱི་ཕྱིར་དང་པོ་མ་ཡིན་པ་དང་བཏུང་བའི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1231]
འདིར་གླེང་གཞི་རྣམས་ལས་མདོ་འདི་གཞུང་ངོ་། །སྤངས་པ་གདོང་མཐོང་བ་ནི་ཞེས་བྱ་བའི་ཚིག་འདིའོ། །

[Block 1232]
ཐུན་ཚོད་དུ་རུང་བ་གཞག་པའི་ཕྱིར། བཏུང་བ་ནི༌[^1066]བྱེད་པའི་ཡན་ལག་ཉིད་ལའོ། །

[Block 1233]
དེ་ལ་སིལ་བུ་རྣམས་ལས་དངས་མ་ཞེས་བྱ་བ་སྟེ། འདིར་རྒྱས་པར་བཤད་པར་བྱ་སྟེ། གདོང་མཐོང་བ་ནི་ཞེས་བྱ་བའོ། །

[Block 1234]
འདིར་གཞུང་ནི།

[Block 1235]
ཆང་བཏུང་བའི་ལྟུང་བྱེད་ཀྱི་ཞུ་བ་ལས།

[Block 1236]
བཙུན་པ༌[^1067]དུས་མ་ཡིན་པར་བཅོས་པའི་ཚ༌[^1068]བྱར་རུང་ངམ། གལ་ཏེ་དངས་མར་གྱུར་ན་བྱེ་བྲག་ཏུ༌[^1069]གསལ་བ་གང་ལ་བཞིན་སྣང་བའོ། །

[Block 1237]
མྱོས་པ་དང་བྲལ་བ་ཞེས་བྱ་བ་ཐམས་ཅད་དུ་བཏུང་བར་གཏོགས་པ་དངས་མ་དེ་ལའོ། །

[Block 1238]
དེ་ལས་རྗེས་སུ་མཐུན་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1239]
ལྷག་མ་རྣམས་ལ༌[^1070]ཡང་ཚ་ལ༌[^1071]སོགས་པ་འདི་སྨོས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1240]
དེ་ལྟ་བུ་ཉིད་ཀྱི་མདུན་རོལ་དུ་བསྙེན་པར་རྫོགས་པར་མཚན་མཐུན་པས་རེག་ཏུ་མི་རུང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལྟ་བུའི་དངོས་པོ་ནི་དེ་ལྟ་བུ་ཉིད་དོ། །

[Block 1241]
ཞོ་ག༌[^1072]ཆུ་ལ་སོགས་པ་མདུན་རོལ་དུ་བསྙེན་པར་རྫོགས་པ༌[^1073]གཞན་མཚན་མཐུན་པས་དེ་ལ་རེག་ཏུ་མི་རུང་བ་ནི་རིགས་པ་ཡིན་ནོ། །

[Block 1242]
ཇི་ལྟར་དུས་སུ་རུང་བའི་རྫས་ཀྱང་བཏུང་བ་ལ་མདུན་རོལ་དུ་ནི་དུས་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་དང་། བཏུང་བར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1243]
ཨ་རུ་ར་ལ་སོགས་པ་ལྔ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཨ་རུ་ར་དང་སྐྱུ་རུ་ར་དང་། [^1074]བ་རུ་ར་དང་ན་ལེ་ཤམ་དང་པི་པི་ལིང༌[^1075]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1244]
བུ་རམ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་དུ་རུང་བ་སྟེ་དང་པོ་ཉིད་མ་ཡིན་ནོ། །

[Block 1245]
དེ་བྱིན་གྱིས་བརླབས་པ་བཟའ་བ་ལམ་དུ་ཞུགས་པ་དང་། དགེ་སྐོས་དང་ལག་གི་བླ་རྣམས་ནི་ནད་པ་དང་འདྲ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བུ་རམ་དེ་ཞག་བདུན་པ་ལ་སོགས་པར་བྱིན་གྱིས་བརླབས་པ་བཟའ་བ་ལ་ཇི་ལྟར་ནད་པས་དུས་དང་དུས་མ་ཡིན་པར་ཐམས་ཅད་དུ་བཟར་རུང་བ་དེ་བཞིན་དུ་ལམ་དུ་ཞུགས་པ་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1246]
ཟན་ཆད་པས་ཀྱང་དེ་དང་དུས་སུ་རུང་བ་མ་ཡིན་པ་བཟར་རུང་ངོ་ཞེས་བྱ་བ་ལ། དེ་དང་ཞེས་བྱ་བ་ནི་དེ་ལ་བུ་རམ་བྱིན་གྱིས༌[^1076]བརླབས་པ་དེ་ཡང་ནད་པ་དེ་དང་འདྲ་བ་ཉིད་དུ་བཟར་རུང་ལ་ཐམས་ཅད་ཀྱིས་སམ། གཞན་གྱིས་ཀྱང་དུས་སུ་རུང་བ་དང་མར་དང་འབྲུ་མར་ལ་སོགས་པ་ཡང་དུས༌[^1077]མ་ཡིན་པར་བཟར༌[^1078]རུང་ཞིང་ནད་པ་ཉིད་ཀྱིས་སོ། །

[Block 1247]
དེ་ནི་རྣམ་པ་བཞི་པོ་དག་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཐུན་ཚོད་དུ་རུང་བའི་ནི་བཏུང་བ་དག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི། ཐུན་ཚོད་དུ་རུང་བ་ནི་ཁྱིམ་པའམ་དགེ་ཚུལ་གྱིས་སྦྱར་བ་ཚགས་ཀྱིས་བཙགས་པ་དག་ནི་ཐུན་ཚོད་དུ་རུང་བའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1248]
ཁ་ཅིག་ནི་ཐུན་ཚོད་དུ་རུང་བའི་བཏུང་བ་བརྒྱད་པོ་ཞེས་ཀྱང་ཟེར་རོ། །

[Block 1249]
འདིར་གཞུང་དུ་བྱེད་དེ་བཙོ་ཚའི༌[^1079]བཏུང་བ་དང་། ཆུ་ཤིང་གི་འབྲས་བུའི་བཏུང་བ་དང་། རྒྱ་ཤུག་གི་བཏུང་བའམ། ཨ་ཤྭདྠའི་བཏུང་བའམ། ཨུ་དུམ་བཱ་རའི་བཏུང་བའམ། རྩུབ་འགྱུར་གྱི་བཏུང་བའམ། རྒུན་ཆུའི་བཏུང་བའམ། འབྲ་གོའི་བཏུང་བ་རྣམས་ནི་ཐམས་ཅད་དུ་བྱའི་ཞེས་ཟེར་བ་དེ་ནི་མི་རིགས་ཏེ། ནད་པ་མ་ཡིན་པ་ལ་ཡང་དེ་རྣམས་འོས་པའི་ཕྱིར་ཞེས་བྱ་བའོ། །

[Block 1250]
འབྲས་བུ་བརྒྱད་པོ་འདི་རྣམས་ཁྱིམ་པ་དང་དགེ་ཚུལ་གྱིས༌[^1080]སྦྱར་བ། ཚགས་ཀྱིས་བཙགས་པ་འདི་དག་ནི་དུས་སམ་དུས་མ་ཡིན་པར༌[^1081]ཡང་ན་བའམ་ན་བ་མ་ཡིན་པས༌[^1082]ཀྱང་བཏུང་བར་བྱ་བ་དག་ཡིན་ཏེ། འདི་ལ་འགྱོད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1251]
དངས་མ་ཞེས་བྱ་བ་ནི་སྐ་བ༌[^1083]ཉིད་བསལ་བའོ། །

[Block 1252]
ཤིན་ཏུ་སླ་བའོ་ཞེས་བྱ་བ་ནི་ཐུན་ཚོད་དུ་རུང་བའི་བཏུང་བ་དག་གོ། །

[Block 1253]
དེའི་རྫས་དེ་ཉིད་མ་ཡིན་པ་དེའི་ཕྱིར་གལ་ཏེ་དུས་སུ་རུང་བ་ཉིད་ཡིན་ན་བསྙེན་པར་མ་རྫོགས་པས་སྦྱར་ཞིང་ཚགས་ཀྱིས་ཀྱང་བཙགས་པར༌[^1084]བྱའོ་ཞེས་བྱ་བ་དང་། དེའི་རྫས་དེ་ཉིད་མ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་བཏུང་བ་ཉིད་མ་ཡིན་པའི༌[^1085]ཕྱིར་རོ། །

[Block 1254]
དེའི་རྫས་ཞེས་བྱ་བ་ནི་བཏུང་བར་བྱ་བའི་རྫས་དེའོ། །

[Block 1255]
གལ་ཏེ་དུས་སུ་རུང་བ་ཡིན་ན་ཞེས་བྱ་བ་ནི་རྫས་དེའོ། །

[Block 1256]
བསྙེན་པར་མ་རྫོགས་པས་སྦྱར་ཞིང་ཞེས་བྱ་བ་ནི་དུས་མ་ཡིན་པར་རུང་བ་ཉིད་ཡིན་ན། བསྙེན་པར་རྫོགས་པས་སྦྱར་ཞིང་བཙགས་པ་ལ་ཡང་ཉེས་པ་མེད་དོ། །

[Block 1257]
དེ་དག་ལས༌[^1086]གཞན་བལ་པོ་སེའུ་དང་མ་དུ་ལུང་ག་ལ༌[^1087]སོགས་པའི་རྫས་ཀྱི་ཞེས་བྱ་བ་ནི་བཙོ་ཚ༌[^1088]ལ་སོགས་པའི་བཏུང་བ་དག་ལས་གཞན་པ་ཐུན༌[^1089]ཚོད་དུ་རུང་བའི་བཏུང་བ་ལས།

[Block 1258]
བལ་པོ་སེའུ་དང་མ་དུ་ལུང་ག་ལ༌[^1090]སོགས་པའི་རྫས་གང་ཞིག་རྩ་བ་དང་སྡོང་བུ་དང་། འདབ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་ཟས་ཀྱི་དོན་དུ་ཁྱབ་པར་བྱེད་པ་གང་ཡིན་པ་དེ་དག་ཀྱང་བསྡུ་བའི་ཕྱིར་སྙེགས་པར༌[^1091]རིག་པར་བྱའོ། །

[Block 1259]
འདིར་གཞུང་ནི།

[Block 1260]
སིལ་བུ་དག་ལས།

[Block 1261]
འདི་དང་པོ་བྱས་ཏེ་སིངས་པོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1262]
དེ༌[^1092]དུས་སུ་རུང་བ་ཉིད་ཡིན་ན་ཐུན་ཚོད་ཀྱི་མཐའ་ཡིན་ནོ༌[^1093]ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་བཏུང་བའི་རྫས་དེའོ། །

[Block 1263]
གཞན་ཉིད་ཡིན་ན་དེའི་གང་ཡིན་པའོ་ཞེས་བྱ་བ་ནི་བཏུང་བའི་རྫས་དེ་དུས་སུ་རུང་བ་ལས་གཞན་པ་དུས་མ་ཡིན་པར་རུང་བ་ཉིད་ཡིན་ན་གང་ཞིག་རྫས་དེའི་མཐར་ཐུག་པ་བཏུང་བ་དེ་ལ་ཐུན་ཚོད་ཀྱི་མཐའ་གཞན་བཟའ་བར་བྱ་བ་ལ་དུས་གང་གི་ཚེ་བཟའ་བར་བྱ་བ་ཉིད་སྐྱེས་པར་འགྱུར་བ་དེའི་ཚེ༌[^1094]བཟའ་བའི་ཕྱིར་དུས་མ་ཡིན་པར་བཏུང་བའི་རྫས་ལ་དུས་ཐམས་ཅད་པ་ཉིད་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1264]
བྱིན་གྱིས་བརླབས་པའི་ཕྱིར་ནི་ཐུན་ཚོད་དུ་རུང་བ་ཉིད་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1265]
ཁ་ཅིག་ན་རེ་མ་གྱུར༌[^1095]ན་དེ་ཡིན་གྱི་གྱུར་ན་གང་ཚུན་ཆད་དེ་ཡིན་པའོ་ཞེས་ཟེར་རོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་བཏུང་བའི་རྫས་ཀྱི་མཐའ་ཡིན་པ་དེ་ཉིད་བཏུང་བ་ལ་ཞེས་གང་སྨོས་པ་དེ་གཅིག་ཏུ་ངེས་པར་རྣམ་པར་གནས་པ་མ་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། འདི་ལྟར་ངོ་བོ་ཉིད་མ་གྱུར་ན་དེ་ལྟུང་བའི༌[^1096]མཐའ་ཡིན་གྱི། གྱུར་ན་སྐད་ཅིག་གང་ཚུན་ཆད་ཀྱི་འོག་ཏུ་ངོ་བོ་ཉིད་དུ་གྱུར་པའི་སྐད་ཅིག་དེ་ཉིད་བཏུང་བའི་མཐའ་ཡིན་པར་ཤེས་པར་བྱའོ་ཞེས་ཟེར་རོ། །
--- END BLOCKS ---
