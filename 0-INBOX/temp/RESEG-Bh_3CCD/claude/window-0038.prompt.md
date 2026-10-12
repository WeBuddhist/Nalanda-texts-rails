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
[Block 1331]
དཔེར་ན་ལྷ་སྦྱིན་ཆེན་པོ༌[^955]ཉིན་པར་མི་ཟ་ཞེས་བྱ་བས་དོན་གྱི་ཤུགས་ཀྱིས༌[^956]མཚན་མོ་ཟ་ཞེས་ངེས་སོ། །

[Block 1332]
དེ་ལྟར་ཚིག་གི་དོན་རྣམས་ལ་སྣ་ཚོགས་པ་མེད་དོ། །

[Block 1333]
དོན་གྱི་ཤུགས་ཀྱིས་ཚངས་པ་ལ༌[^957]ཡོད་དོ་ཞེས་མི་རིགས་ཏེ། དངོས་པོ་རྣམས་ལ་སྣ་ཚོགས་པ་ཉིད་དམིགས་པའི་ཕྱིར་རོ། །

[Block 1334]
གཅིག་བཀག་པས་ཆོས་གཞན་ངེས་པར་དམིགས་པས་ནི་དོན་གྱི་ཤུགས་སོ། །

[Block 1335]
དེ་ཡང་དངོས་པོ་དང་ཚངས་པ་དག་ལ་མེད་དོ། །

[Block 1336]
དངོས་པོ་མེད་པ་ཡང་ཚད་མ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་དེ་ལ་རྣམ་པ་བཞི་ཡོད་དེ། སྔ་ན་མེད་པ་དང་འཇིག་པས་མེད་པ་དང་ཕན་ཚུན་མེད་པ་དང་ཤིན་ཏུ་མེད་པའོ། །

[Block 1337]
དེ་ལ་སྔ་ན་མེད་པ་ནི་འོ་མ་ཞོར་གྱུར་པའོ། །

[Block 1338]
འཇིག༌[^958]པས་མེད་པ་ནི་བུམ་པ་ཐོ་བ་དང་ཕྲད་པས་འཇིག་པའོ། །

[Block 1339]
ཕན་ཚུན་མེད་པ་ནི་སྣམ་བུ་དང་བུམ་པ་དག་གོ། །

[Block 1340]
ཤིན་ཏུ་མེད་པ་ནི་རི་བོང་གི་རྭ་ལ་སོགས་པའོ། །

[Block 1341]
དངོས་པོ་མེད་པ་ནི་ཡུལ་ལ་དངོས་པོ་མེད་པ་ཚད་མ་ཡིན་གྱི་དངོས་པོ་ཡོད་པའི་ཡུལ་དུ་ནི་མ་ཡིན་ནོ་ཞེས་ཇི་ལྟར་དེས་ནི་དངོས་པོའི་ཆོས་ནི་ཚངས་པའི་སྣ་ཚོགས་པ་ཉིད་སྒྲུབ་པར་བྱེད་དེ། དགག་པ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1342]
ཞོ་ལ་མར་སྲིད་པ་དང་། ཏིལ་འབྲུ་ལ་མར་ཁུ་ཞེས་སྲིད་པ་ནི་ཚད་མ་མ་ཡིན་ཏེ། ས་མི་གཤིན་པ་ལས་སྐྱེས་པའི༌[^959]ཏིལ་འབྲུ་རྣམས་ལ་མར་ཁུ་མི་འབྱུང་བས་སོ།[^960] །

[Block 1343]
ཕལ་ཆེར་ལ་དགོངས་པ་ནི་ངེས་པར་བྱེད་པའི་རྒྱུ་མ་ཡིན་ཏེ་སླུ་བའི༌[^961]ཕྱིར་རོ་སྙམ་པས་ཡོད་པ་ཡང་ཚད་མ་མ་ཡིན་ཏེ། ཤིང་འདི་ལ་གནོད་སྦྱིན་ཡོད་པ་དང་། ཁང་པ་འདི་ལ་ཤ་ཟ་ཡོད་དོ་ཞེས་ངེས་པ་མེད་དོ། །

[Block 1344]
རེས་འགའ༌[^962]དེ་ནས་གཞན་དུ་འགྲོ་བའི་ཕྱིར་དང་སྔགས་ཤེས་པའི་སྐྱེས་བུའི་ནུས་པའི་འབྲེལ་པས་གནོད་སྦྱིན་ལ་སོགས་པ་བསྐྲད་པ༌[^963]རྣམས་དེར་མི་གནས་པའི་ཕྱིར་རོ། །

[Block 1345]
དེ་བཞིན་དུ་འདིར་ཚངས་པའི་སྣ་ཚོགས་པ་ཉིད་དངོས་པོ་རྣམས་ལ་མ་ངེས་སོ། །

[Block 1346]
མ་མཐོང་བ་རང་བཞིན་གྱིས་བསྐལ་པ་ཤ་ཟ་ལ་སོགས་པ་ལ་སྙམ་པ་ཞེས་བྱ་བས་ངེས་པར་བྱེད་པར་རིགས་སོ། །

[Block 1347]
སྣ་ཚོགས་པ་ནི་མངོན་སུམ་གྱིས་སྣང་ན་སྙམ་པས་ཇི་ལྟར་ངེས་པར་བྱེད་དོ། །

[Block 1348]
དེ་བས་ན་ཚད་མ་བརྒྱད་ཀྱིས་མ་གྲུབ་པའི་ཚངས་པ་ཉིད་དང་དེའི་སྣ་ཚོགས་པ་ཉིད་དུ་གནས་པ་དད་པ༌[^964]དམ་པ་པ་རྣམས་ཇི་ལྟར་གྲོལ་བར་འགྱུར། །དེས་ནི༌[^965]ཚངས་པ་ཞི་བ་སྨྲ་བའི་ཕྱོགས་ཀྱང་བཀག་གོ །གལ་ཏེ་ཚངས་པ་ཉིད་དངོས་པོའི་སྣ་ཚོགས་མ་སྐྱེས་པ་ཞི་བ་ཡིན་ནོ། །

[Block 1349]
ཇི་ལྟར་དངོས་པོ་འདི་རྣམས་རྣམ་པ་སྣ་ཚོགས་སུ་སྣང་ངོ་། །དེ་རྣམས་ཀྱང་ཞི་བ་ཡིན་ཞེས་འདོད་པ་རིགས་པ་མ་ཡིན་ཏེ། ཚད་མ་དང་འགལ་བའི་ཕྱིར་རོ། །

[Block 1350]
གང་གི་ཕྱིར་མཐོང་བ་ལ་མི་རིགས་པ་ཞེས་བྱ་བ་མེད་དོ། །

[Block 1351]
འཁྲུལ་པ༌[^966]ཁོ་ན་དངོས་པོ་རྣམས་ཀྱི་སྣ་ཚོགས་པ་ཡིན་ཞེ་ན། འཁྲུལ་པ་ནི་ཅི་དེ་ལས་ཐ་དད་པའམ་ཐ་མི་དད་ཅེ་ན། ཐ་དད་པ་ཡིན་ན་འཁྲུལ་པ་དང་ཚངས་པ་ཉིད་གཉིས་ཀ་ཡོད་ཅེས་ཐ་དད་པའོ། །

[Block 1352]
ཚངས་པ་ནི་གཉིས་སུ་མེད་པས་འགལ་ལོ། །

[Block 1353]
ཐ་མི་དད་པ་ནི་ཚངས་པ་ཉིད་འཁྲུལ་པའི་རང་བཞིན་དུ་སོང་བས་དེ་ཁོ་ན་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 1354]
དེ་ནི་འཁྲུལ་པ་མེད་པ་ཡིན་དུ་འཇུག་ན་ཅིའི་ཕྱིར་འཁྲུལ་པ་སྐྱེད་པར་བྱེད་པ་ཡིན་ཏེ། འགྱུར་བ་མེད་པ་ལ་སྤྲོས་པ་མེད་དེ་ནམ་མཁའ་བཞིན་ནོ། །

[Block 1355]
དེ་བས་ན་ཞི་བའི་ཚངས་པ་ཉིད་སྨྲ་བའི་ཕྱོགས་ནི་མི་རིགས་སོ་ཞེས་ཚད་མ་བ་དཔྱོད་པ་པའི་ལན་ནོ། །

[Block 1356]
དེ་རྣམས་བསྟན་པ་དྲུག་ལ་གནས་པ་ཕྱིན་ཅི་ལོག་པའི་བློ་ཅན་དུ་བཤད་དོ། །

[Block 1357 [HEADING]]
#### ངེས་པའི་བློ་ཅན། ^1-5-4-0

[Block 1358]
ངེས་པའི་བློ་ཅན་ནི་རྣམ་པ་བཞི་སྟེ། ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་རྣལ་འབྱོར་སྤྱོད་པ་དང་དབུ་མའི་དབྱེ་བས་སོ། །

[Block 1359 [HEADING]]
##### ཉན་ཐོས། ^1-5-4-1-0

[Block 1360]
དེ་ལ་ཉན་ཐོས་པའི་གཞུང་ནི་བདེན་པ་བཞི་སྟེ། སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་བ་དང་། འགོག་པ་དང་། ལམ་མོ། །

[Block 1361]
དེ་ལ་བདེན་པ་གཉིས་ནི་རྒྱུ་དང་འབྲས་བུའི་དབྱེ་བས་གནས་པ་ནི་འཁོར་བའོ། །

[Block 1362]
བདེན་པ་ཡང་གཉིས་ནི་རྒྱུ་དང་འབྲས་བུའི་བྱེ་བྲག་གི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 1363]
དེ་ལ་འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པའི་དབྱེ་བས་ཉོན་མོངས་པ་དགུ་བཅུ་རྩ་བརྒྱད་མཐོང་བ་དང་། བསྒོམ་པའི་ལམ་གྱིས་སྤངས་ཏེ། འགོག་པའི་སྙོམས་པར་ཞུགས་པ་གཙོར༌[^967]གྱུར་པ་རང་གི་དོན་ཙམ་དང་ལྡན་པ་ཉན་ཐོས་ཀྱི་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1364]
དེ་རྣམས་ཀྱི་རེ་བ་ནི་གཞན་གྱི་དོན་གྱིས་ཅི་ཞིག་བྱ། བདག་གི་དོན་ནི་བསྒྲུབ་བྱ་ཡིན། །ཞེས་བྱ་བ་ལ་སོགས་པ་འབྱུང་ངོ་། །དེ་རྣམས་གང་ཟག་ལ་བདག་མེད་པར་འདོད་ཅིང་། ཕུང་པོ་ལ་སོགས་པ་ཆོས་རྣམས་ལ་བདག་ཡོད་པར་འདོད་ཅིང་གཟུང་བ་དང་། འཛིན་པ་ལ༌[^968]ཞེན་པའོ། །

[Block 1365]
དེའི་ཕྱིར་དེ་རྣམས་ཀྱི་གྲོལ་བ་རྣམ་པར་དག་པ་མ་ཡིན་པས་སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོར་སྣོད་མ་ཡིན་པར་བཤད་དོ། །

[Block 1366]
ཇི་སྐད་དུ།

[Block 1367 [VERSE]]
དགེ་སློང་ཉིད་དུ་གང་གནས་པ། །
གང་ཡང་རྟོག་གེ་བ་རྣམས་མི། །
རྒན་པོར་གྱུར་པ་གང་རྣམས་དང་། །
དེ་ལ་དེ་ཉིད་བསྟན་མི༌[^969]བྱ། །

[Block 1368]
ཞེས་གསུངས་སོ། །

[Block 1369]
མདོ་སྡེ་པ་ཞེས་བྱ་བས༌[^970]རྗེས་སུ་དཔག་པས་ཕྱིའི་དོན་འདོད་དེ། ཕྱིའི་དོན་ནི་གཅིག་དང་དུ་མས་མ་གྲུབ་པས་མེད་པས་ཀྱང་རྣམ་པར་ཤེས་པའི་སྐྱེ་བ་གཞན་དུ་ན་མི་འགྱུར་བས་རྗེས་སུ་དཔག་པ་ཡིན་ཏེ། མིག་གི་དབང་པོ་བཞིན་ནོ་ཞེས་རྗེས་སུ་དཔོག་པའི་མདོ་སྡེ་པ་ཕྱིའི་དོན་སྨྲ་བ་རྣམས་ཀྱིས་སྔ་མ་བཞིན་དུ་ཐར་པ་ནི་རྣམ་པར་མ་དག་པས་དེ་དག་ཀྱང་སྔགས་ཀྱི་སྣོད་དུ་རུང་བ་མ་ཡིན་ནོ། །

[Block 1370 [HEADING]]
##### རྣལ་འབྱོར་སྤྱོད་པ། ^1-5-4-3-0
--- END BLOCKS ---
