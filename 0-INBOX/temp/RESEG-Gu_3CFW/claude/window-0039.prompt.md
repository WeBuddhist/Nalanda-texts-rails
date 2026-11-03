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
[Block 1366]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས།

[Block 1367]
བུ་རམ་གྱི་བཏུང་བའི་སྐབས་ནས། བཙུན་པ་བཏུང་བ་བཙགས་ནས་དགུང་བདུན་པར་བྱིན་གྱིས་བརླབ་ཏུ་རུང་ངམ། ཉེ་བ༌[^1184]འཁོར་མི་རུང་ངོ་། །

[Block 1368]
བཙུན་པ་ཡུན༌[^1185]ཇི་སྲིད་ཅིག་ཏུ་གཞག་པར་འཚལ་བར་བགྱི། ཉེ་བ༌[^1186]འཁོར་ཤིན་ཏུ་སླ་ཞིང་མི་སྐྱུར༌[^1187]ལ་རང་གི་ངོ་བོ་ཉིད་མི་སྤོང་བ་དེ་སྲིད་དུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1369]
འདིར་ཞུ་བ་བྱ་བ་མ་ཡིན་པ་ཉིད་གསུངས་ཏེ། འདི་ལ་གསོག་འཇོག་ལས་གཞན་པའི་བཏུང་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་ལ་རྒྱུ་རྣམ་པར་མི་གནས་པ་དེ་བས་ན་གསོག་འཇོག་ཉིད་དུ་ཤེས་པའོ། །

[Block 1370]
བྱིན་གྱིས་བརླབ་པ་འོག་མ༌[^1188]དང་ལྷན་ཅིག་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་བྱེ་བྲག་ཏུ་བཅད་པས་བྱིན་གྱིས་བརླབས་པ་དང་། གསོག་འཇོག་གི་དུས་ལ་མ་བབ་པ་དང་ལྷན་ཅིག་ཅེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 1371]
འདིར་གཞུང་ནི། མཽད་གལ་གྱི་བུ་ལ་ཐུན་ཚོད་དུ་རུང་བ་གང་ཡིན་པ་དང་། ཞག་བདུན་པ་གང་ཡིན་པ་དང་། འཚོ་བའི་བར་དུ་བཅང་བ་གང་ཡིན་པ་དེ་དུས་སུ་རུང་བ་དང་འདྲེས་ན་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ། །

[Block 1372]
ཞག་བདུན་པ་གང་ཡིན་པ་དང་། འཚོ་བའི་བར་དུ་བཅང་བ་གང་ཡིན་པ་དེ་ཐུན་ཚོད་དུ་རུང་བ་དང་འདྲེས་ན་ཡང་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ། །

[Block 1373]
འཚོ་བའི་བར་དུ་བཅང་བ་གང་ཡིན་པ་དེ་ཞག་བདུན་པ་དང་འདྲེས་ན་ཡང་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1374]
སྨན་གྱི་གོ་རིམས་ནི་དཔེའོ་ཞེས་བྱ་བ་ནི་སྔར་དེ་ནི་རྣམ་པ་བཞིའོ་ཞེས་སྨོས་པས། སྨན་རྣམ་པ་བཞི་སྨོས་པའི་གོ་རིམས་དེ་ནི་དཔེ་ཙམ་དུ་ཟད་དེ། དེ་བས་ན་འདིས་མིག་སྨན་ལ་སོགས་པ་དག་ཀྱང་མ་འཕངས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1375]
དེ་བས་ན་ཅིར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་མིག་སྨན་བསྟེན་པར་བྱའོ། །

[Block 1376]
སྨན་མ་ཡིན་པའི་དོན་དུ་མི་བྱའོ་ཞེས་བྱ་བའི་སྒེག་པའི་དོན་ནི་སྨན་མ་ཡིན་པའི་དོན་ཏེ་དེའི་དོན༌[^1189]དུ་མིག་སྨན་བསྟེན་པར༌[^1190]མི་བྱའོ། །

[Block 1377]
འདི་ནི་དྲིས༌[^1191]བྱུག་པ་དང་ཁ་དོག་འཆང་བའི་ཕྱོགས་ཉིད་དུ་དོགས་པ༌[^1192]དེ་བས་ན་འདི་སྤངས་པའོ། །

[Block 1378]
འདིར་གཞུང་ནི་མ་མོ་དག་ལས་མིག་ཐུར་བཅང་བར་བྱ་སྟེ། ཇི་སྙེད༌[^1193]དུ་རང་འཁྲུངས་དག་གོ་ཞེས་བྱ་བའོ། །

[Block 1379]
དེའི་སྣོད་རིགས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གི་སྣོད་ཅི་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མིག་སྨན་སྐྱེར་ཁཎྜའི་ནི་ཟ་མ་ཏོག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཅང་བར་བྱ་བ་ཉིད་ཀྱང་དེ་ལ་སོགས་པ་དང་སྐྱེར་ཁཎྜ་ལ་སོགས་པར་དོན་གྱིས༌[^1194]རིག༌[^1195]པར་བྱའོ། །

[Block 1380]
མིག་སྨན་རི་ལུའི་ནི་སྒེའུ་འོ། །

[Block 1381]
མིག་སྨན་དུ་བ་དང་སྦྲུས་པ་དང་། ཕྱེ་མ་རྣམས་ཀྱི་ནི་དོང་བུའི༌[^1196]ཐུར་མ་བཅང་བར་བྱའོ། །

[Block 1382]
ཟངས་མ་དང་ལྕགས་དག་གི་བཟང་ངོ་། །ཅི་མིག་ཐུར་ཐམས་ཅད་རུང་ངམ་ཞེ་ན། དེའི་ཕྱིར་རང་འཁྲུངས་དག་གོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1383]
ནད་པས་སྨན་གཞུག་པའི་ཕྱིར་མཆན་ཁུག་བཅང་བར་བྱའོ། །

[Block 1384]
དེར་མ་ཤོང་བ་ཉིད་ཡིན་ན་བྲུབས༌[^1197]སམ་ཐུམ་པོ་བྱས་ཏེ་བཅེར་རོ་ཤེས༌[^1198]བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་མཚན་ཁུག་དེར་བྲུབས་སམ་ཐུམ་པོ་བྱས་ཏེ་བཅེར་རོ། །

[Block 1385]
བཅུག་པ་མི་འདྲུལ་བར་བྱ་བའི་ཕྱིར་དུས་སུ་སྐམ༌[^1199]མོ་ཞེས་བྱ་བ་ལ་གང་དུ་བསྐམ་པར་བྱ་ཞེ་ན། [^1200]དེའི་ཕྱིར་ཉི་གྲིབ་ལའོ། །

[Block 1386]
བསྐམས༌[^1201]ན་མཐུ་འབྲིའོ་ཞེས་བྱ་བ་ནི་སྐབས་འདིར་བསྒྲུབ་པ༌[^1202]འདི་བསྡུས་པ་ཡིན་ནོ། །

[Block 1387]
གོས་ལ་སོགས་པ་བསྐམ་པ་ལ་ཡང་ཆོ་ག་འདི་ཡིན་གྱི་དེ་ཉིད་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བ་བསྟན་པའི་དོན་དུའོ། །

[Block 1388]
[^1203]མ་རུང་བར་འགྱུར་བའི༌[^1204]རྒྱུ་བྱུང་ན་རང་གིས་བྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི། རླུང་དང་ཆར་པ་ལ་སོགས་པས་སྨན་མ་རུང་བར༌[^1205]གྱུར་པའི་རྒྱུ་བྱུང་ན་དེ་བསྐམས་པའི་གནས་ནས་རང་གིས་བསྡུ་ཞིང་བྲུབ་པར༌[^1206]བྱའོ། །ཅི་གནས༌[^1207]སྐབས་ཐམས་ཅད་དུའམ་ཞེ་ན། དེའི་ཕྱིར་བསྙེན་པར༌[^1208]རྫོགས་པ་མེད་ནའོ། །

[Block 1389]
སྨན་ཕོར་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་པས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1390]
ཕྲན་ཚེགས་དག་ལས།

[Block 1391]
འདིར་དང་པོར་བྱས་ཏེ་ཕྱིས་ལོངས་སྤྱད་པ་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 1392]
སྨན་གྱི་ནལ་ཟེ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་། ནད་པས་བཅང་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1393]
འགྲོར་མི་བཏུབ་པས་ཕུལ་བའི་བཏུང་ཕོར་རོ་ཞེས་བྱ་བ་ཡང་བཅང་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1394]
འགྲོར་མི་བཏུབ་པས་ཞེས་བྱ་བ་ལ་འགྲོ་བ་ཞེས་བྱ་བ་ནི་མིད་པའི་ཚེ་ནང་དུ་འགྲོ་བའོ། །

[Block 1395]
མི་བཏུབ་པ་ཞེས་བྱ་བ་ནི་མིད་པའི་ཚེ་ནང་དུ་འགྲོར་མི་བཏུབ་ཅིང་མགུལ་བར་ཐོགས་ཤིང་སྣང་བ་སྟེ། གང་གིས་དེར་འགྲོར་མི་བཏུབ་པ་དེ་ནི་འདིར་མགུལ་པའི་ནད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1396]
ཕུལ་བའི་བཏུང་ཕོར་ཞེས་བྱ་བ་ནི་གང་ཟས་ཟོས་ན་མགུལ་པར་ཐོགས་པ་དེ་འཕུལ་བར་བྱེད་པའི་ཕྱིར། ཕྱི་ནས་སྐོམ་འཐུང་བར་བྱེད་པའི་སྣོད་ཆུང་ངུ་མ་ལ་བྱའོ།[^1209] །འདིར་གཞུང་ནི། གནས་བརྟན་ཁྱོད་ཅི་བསྲུང་། ཚེ་དང་ལྡན་པ་འགྲོར་མི་བཏུབ་པའོ། །

[Block 1397]
ཁྱོད་ཀྱིས༌[^1210]སྔོན་ཅི་བགྱིས་ཕུལ་བའི་བཏུང་པོར་བཅངས་སོ། །

[Block 1398]
དེ་ཅིའི༌[^1211]ཕྱིར་མི་བཅང་། [^1212]བཅོམ་ལྡན་འདས་ཀྱིས་མ་གནང་ངོ་ཞེས་ཟེར་བའི་སྐབས་དེ་ནས་ཇི་སྲིད་དུ་བཀའ་སྩལ་པ། དེ་ལྟ་བས་ན་ཕུལ་བའི་བཏུང་ཕོར༌[^1213]བཅང་བར་རྗེས་སུ་གནང་ངོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 1399]
འདིར་དེ་ལ་ལྟོས་པའི་གླེང་གཞིའི་དབང་གིས་རྗེས་སུ་གནང་བ་དེ་རིགས་པ་ཡིན་ཏེ། [^1214]དེའི་ཕྱིར་འདིར་མདོར་བསྡུས་པ་བྱས་སོ། །

[Block 1400]
ནད་པས་ལན་ཚྭ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འགྲོར་མི་བཏུབ་པས་ཞེས་བྱ་བ་བསལ་བའི༌[^1215]ཕྱིར་འདིར་ནད་པ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1401]
དེའི་སྣོད་ནི་རྭའི༌[^1216]སྦུབས་བཟང་ངོ་ཞེས་བྱ་བ་ནི་ལན་ཚྭ་དེའིའོ།[^1217] །རྭ༌[^1218]ཇི་ལྟ་བུ་བཟང་ཞེ་ན། དེའི་ཕྱིར་ལྕི་བས་ཀུན་ནས་བསྐོར་བའོ། །

[Block 1402]
[^1219]དེ་མེད་པའི་ཉེས༌[^1220]པར་མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་ཁ་གབ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་ཁ་གབ་དང་བྲལ་བའི་ཉེས་པ་གང་ཡིན་པ་དེའོ། །ཅི་ལས་བྱས་པ་ཞེ་ན། དེའི་ཕྱིར་དེ་ཉིད་ལས་བྱས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྭ་ལྕི་བས་ཀུན་ནས་བསྐོར་བ༌[^1221]ལས་བྱས་པའི་འགང་གཞུག་པའོ། །

[Block 1403]
དྲིས་བསྒོས་པའི་སའོ་ཞེས་བྱ་བ་ནི་ནད་པས་བཅང་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1404]
ཆུ་སྲོ་བའི་ཕྱིར་ལྕགས་ཀྱི་གར་བུའོ་ཞེས་བྱ་བ་ཡང་ནད་པས་བཅང་ངོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1405]
ཐམས་ཅད་ཀྱིས༌[^1222]སྤྱད་པར་བྱའོ། །ཞེས་བྱ་བ་ནི་ནད་པ་འབའ་ཞག་གིས་སྤྱད་པར་མ་ཟད་ཀྱི་ན་བ་དང་མི་ན་བ་ཐམས་ཅད་ཀྱིས་སྤྱད་དུ་རུང་བའོ། །
--- END BLOCKS ---
