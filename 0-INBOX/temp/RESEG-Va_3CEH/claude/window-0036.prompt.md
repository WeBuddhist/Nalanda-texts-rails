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
[Block 1261]
དེ་ལ་སྦྱིན་པ་བྱེད་པ་ནི༌[^804]ལུས་དང་ངག་བསྡམས་ནས་སྦྱིན་པར་བྱེད་པ་ནི་དེའི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་བྱེད་པ་ཡིན་ནོ། །

[Block 1262]
སྦྱིན་པའི་རྒྱུ་དང་འབྲས་བུ་ཤེས་པ་ཉིད་ནི་ཤེས་རབ་ཀྱི་བྱེད་པ་སྟེ། ལྷག་མ་རྣམས་ཀྱི་བྱེད་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1263 [HEADING]]
## དེའི་རྒྱུ་དང་འབྲས་བུའི་སྒོམ་པ་རབ་ཏུ་དབྱེ་བ། ^5-0

[Block 1264]
དེའི་རྒྱུ་དང་འབྲས་བུའི་བྱེ་བྲག་ལས་བརྩམས་པ་ནི་ཤེས་བྱ་ཆོས་ཀྱི་དབྱིངས་རྣམ་པ༌[^805]བཅུ་པོ་ཀུན་ཏུ་འགྲོ་བའི་དོན་དང་། གཟུངས་དང་ཏིང་ངེ་འཛིན་གྱི་སྒོ་ལ་དབང་བའི་དོན་གྱི་བར་དུའོ། །

[Block 1265 [HEADING]]
### ཤེས་བྱ་ཆོས་ཀྱི་དབྱིངས་རྣམ་པ་བཅུ། ^5-1-0

[Block 1266]
དེ་ལ་ཤེས་བྱ་ཆོས་ཀྱི་དབྱིངས་རྣམ་པ་བཅུ་ནི་ལུས༌[^806]དང་ས་ལ་ཤེས་བྱའི་རྣམ་པ་རེ་རེ་སྟེ། དེ་ཡང་མ་རིག་པའི་དབང་གིས་མི་ཤེས་པ་ཡིན་པས་དེའི་ཕྱིར་དེ་ལྟ་བུའི་མ་རིག་པའི་གཉེན་པོར་ས་བཅུ་པའོ།[^807] །ཡང་ན་དེའི་མི་མཐུན་པའི་ཕྱོགས་རྣམ་པ་བཅུ་ལས་ས༌[^808]བཅུར་གཞག་སྟེ། དེའི་མི་མཐུན་པའི་ཕྱོགས་རྣམ་པ་བཅུ་གང་ཞེ་ན། སོ་སོའི་སྐྱེ་བོ་ཉིད་དང་། བདེན་པ་ལ་ལུས་ལ་སོགས་པས་ཕྱིན་ཅི་ལོག་ཏུ་སྒྲུབ་པ་དང་དབུལ་བ༌[^809]ཉིད་དོ། །

[Block 1267]
ཐོས་པ་དང་། བསམས་པ༌[^810]དང་། བསྒོམས་པ་བརྗོད་པ་ཉིད་དོ། །

[Block 1268]
ཉོན་མོངས་པ་ཕྲ་བ་ཀུན་ཏུ་རྒྱུ་བ་སྟེ། ལྷན་ཅིག་སྐྱེས་པའི་འཇིག་ཚོགས་ལ་ལྟ་བ་ལ་སོགས་པས་བསྡུས་པའོ། །

[Block 1269]
དེ་ཡང་ཆུང་བའི་རྣམ་པ་ཉིད་ཀྱི་ཕྱིར་དང་། ཡིད་ལ་བྱེད་པ་དང་བཅས་པའི་དམིགས་པ་ཉིད་ཀྱི་ཕྱིར་དང་། ཀུན་ཏུ་སྤྱོད་པའི༌[^811]རིང་དུ་སོང་བ་ཉིད་ནི་ཕྲ་བ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1270]
ཐེག་པ་དམན་པས་མྱ་ངན་ལས་འདའ་བ་དང་། མཚན་མ་རྒྱ་ཆེན་པོ་ལ་ཀུན་ཏུ་སྤྱོད་པ་དང་། མཚན་མ་ཕྲ་མོ་ལ་ཀུན་ཏུ་སྤྱོད་པ་དང་། མཚན་མ་མེད་པར་མངོན་པར་འདུ་བྱེད་པ་དང་སེམས་ཅན་གྱི་དོན་བྱེད་པ་ལ་མངོན་པར་འདུ་བྱེད་པ་མེད་པ༌[^812]དང་། ཐོབ་པར་བྱ་བའི་ཆོས་ལ་གཙོ་བོར་བྱ་བ་མེད་པའོ། །

[Block 1271]
དེ་ལ་སྔོན་དུ༌[^813]འགྲོ་བའི་དོན་ལས་བརྩམས་པ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀུན་ཏུ་འགྲོ་བ་སྟེ། འདི་ལྟར་ཆོས་གང་ཡང་བདག་མེད་པའི་བདག་ཉིད་མ་ཡིན་པའོ།[^814] །མཆོག་གི་དོན་ཞེས་བྱ་བ་ནི་དེ་ནི་ས་གཉིས་པའི་ཡེ་ཤེས་སོ། །

[Block 1272]
རྒྱུ་མཐུན་པའི་དོན་གྱི་མཆོག་ནི་གོང༌[^815]དུ་ཐེག་པ་ཆེན་པོའི༌[^816]ཆོས་བསྟན་པའི་རྒྱུ་མཐུན་པའོ། །

[Block 1273]
མཆོག་ཅེས་བྱ་བ་ནི་ས་གསུམ་པར་གྱུར་པའི་ཡེ་ཤེས་སོ། །

[Block 1274]
གང་ལ་བདག་ཏུ་འཛིན་པ་ཡོད་པ་དེ་ནི་ཀུན་དུ་འཛིན་པ་ཅན་ཏེ། ཇི་ལྟར་བདག་ཏུ་འཛིན་པ་མེད་པ་ནི་བྱང་གི་སྒྲ་མི་སྙན་ནོ། །

[Block 1275]
དེ་ལ་འདི་ལྟ་བུའི་ཆོས་ཀྱི་དབྱིངས་ཐོབ་པར་གྱུར་པ་ནི་གང་ལ་ཡང་བདག་གིར་འཛིན་པ་འབྱུང་བར་མི་འགྱུར་ཏེ། འདི་ལྟར་དེ་ལྟ་བུའི་ཡེ་ཤེས་ནི་བཞི་པ་ལས༌[^817]འབྱུང་བར་འགྱུར་རོ། །

[Block 1276]
དེ་ཉིད་རྒྱུ༌[^818]ཐ་དད་པ་མེད་པ་སྟེ། ཇི་ལྟར་མིག་ལ་སོགས་པ་སེམས་ཅན་སོ་སོ་ལ་ཡོད་པ་རྣམས་ཉིད་ཐ་དད་པ་མ་ཡིན་པར་ཤེས་པ་དེ་ནི་ལྔ་པའོ། །

[Block 1277]
ཀུན་ནས་ཉོན་མོངས་པ་མ་ཡིན་པ་ནི་རང་བཞིན་གྱིས་ཀུན་ནས་ཉོན་མོངས་པ་མ་ཡིན་པའི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པ་མ་ཡིན་པ་སྟེ་དག་པ་ཉིད་ཀྱི་ཡེ་ཤེས་དེ་ནི་དྲུག་པའོ། །

[Block 1278]
མདོ་སྡེ་ལ་སོགས་པ་སྣ་ཚོགས་ཀྱི་དོན་ཐ་དད་པ་མེད་པ་ཉིད་ཀྱི་ཡེ་ཤེས་ནི་བདུན་པའོ། །

[Block 1279]
དེ་ནི་ཉོན་མོངས་པ་སྤངས་པས་བྲི་བ་མེད་ཅིང་སྤེལ་བས་རྣམ་པར་བྱང་བ་ལ་འཕེལ་བ་མེད་པ་དང་། རྒྱུ་མཚན་ལ་དབང་བའི་གནས་དང་། ཞིང་ལ་དབང་བའི་གནས་ཤེས་པ་དེ་ནི་བརྒྱད་པའོ། །

[Block 1280]
དེ་ལ་རྒྱུ་མཚན་ལ་དབང་བ་ནི་འདི་ལྟར་དེ་འདོད་པར་གྱུར་ན་མཚན་མ་དེ་མངོན་སུམ་དུ་བྱེད་པར་འགྱུར་བའོ། །

[Block 1281]
ཞིང་ལ་དབང་བ་ནི་ཇི་ལྟར་གསེར་གྱི་རང་བཞིན་དུ་སྒྱུར་བར་འདོད་ན་ཡང་དེར་འགྱུར་བ་དེ་ནི་དེ་ལ་དབང་བའོ། །

[Block 1282]
སོ་སོ་ཡང་དག་པར་རིག་པའི་ཡེ་ཤེས་ལ་དབང་བའི་གནས་ནི་དགུ་པའོ། །

[Block 1283]
ལུས་ལ་སོགས་པའི་ལས་ལ་དབང་བའི་གནས་ནི་བཅུ་པའོ། །

[Block 1284]
གཟུངས་དང་ཏིང་ངེ་འཛིན་གྱི་སྒོ་ལ་དབང་བ་ཉིད་ཀྱི་གནས་ཀྱི་དོན་ཀྱང་བཅུ་པ་སྟེ། མ་རིག་པ་འདི་ཡང་ཉན་ཐོས་རྣམས་ཀྱི་ནི་ཉོན་མོངས་པ་ཅན་མ་ཡིན་ཏེ། གང་གི༌[^819]ཕྱིར་དེ་དག་ས་ལ་མི་འཇུག་པས་སོ། །

[Block 1285 [HEADING]]
### ས་རྣམ་པར་གཞག་པ། ^5-2-0

[Block 1286]
དང་པོ་ཉིད་ཀྱིས་ཐམས་ཅད་རབ་ཏུ་རྟོགས་པར་གྱུར༌[^820]ན། ཡང་ཅིའི་ཕྱིར་སོ་སོའི་རིམ་པ་གཞག་པར་བྱེད་ཅེས་རྒོལ་བ༌[^821]ལ་དེས༌[^822]ལན་གདབ་པའི་ཕྱིར་གང་ལ་གནས་པའི༌[^823]གནས་པ་དེའི་དབང་གིས་ས་རྣམ་པར་གཞག་པར་བྱ་སྟེ། ཇི་ལྟར་དང་པོ་ཉིད་ཀྱིས་ཐམས་ཅད་ཡང་དག་པར་སོ་སོར་རྟོགས་ན་ཅིའི་ཕྱིར་དང་པོ་ལ་རབ་ཏུ་དགའ་བ་ཞེས་བྱ་ཞེ་ན། འདི་ལྟར་བདག་དང་གཞན་གྱི་དོན་ཡང་དག་པར་བསྒྲུབ་པའི༌[^824]ནུས་པ་དེའི་ཚེ་དང་པོ་ཐོབ་པ་ཡིན་པས་སོ། །

[Block 1287]
ཡང་ཉན་ཐོས་རྣམས་ཀྱིས་དེ་ཁོ་ན་ཉིད་དུ་མངོན་པར༌[^825]རྟོགས་པའི་དུས་ན་ནི་བདག་གི་དོན་ཡང་དག་པར་བསྒྲུབ་པའི༌[^826]ནུས་པ་ནི་ཐོབ་ཀྱི། དེ་དག་གིས་གཞན་གྱི་དོན་གྱི་ནི་མ་ཡིན་པས། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཇི་ལྟ་བུ་དེ་ལྟ་བུའི་དགའ་བ་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 1288]
ཅིའི་ཕྱིར༌[^827]དྲི་མ་མེད་པ་ཞེས་བྱ་བ་ནི་གང་གིས་དེ་རང་བཞིན་གྱི༌[^828]ཚུལ་ཁྲིམས་ཅན་དུ་གྱུར་པ་ཉིད་ཡིན་གྱི།

[Block 1289]
དང་པོ་བཞིན་དུ་སོ་སོར་བརྟགས་པའི་ཚུལ་ཁྲིམས་ཅན་ནི་མ་ཡིན་ནོ། །

[Block 1290]
དེས་ན་འདི་ལྟར་འཆལ་བའི་ཚུལ་ཁྲིམས་ཀྱི་དྲི་མ་རིང་དུ་བྱེད་པའི་ཕྱིར། དེ་ནི་རང་བཞིན་གྱི༌[^829]ཚུལ་ཁྲིམས་ཅན་ཉིད་ཡིན་ནོ། །

[Block 1291]
གང་གི་ཕྱིར་ས་གསུམ་པ་ལ་འོད་བྱེད་པའོ༌[^830]ཞེས་བྱ་ཞེ་ན་འདི་ལྟར་དེ་ནི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་པ་དེ་ལས་འབྲལ་བར་མི་འགྱུར་ཏེ། དེ་ལས་ཉམས་པ་མེད་པ་ན་ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱི་སྣང་བ་འབྱུང་བར་འགྱུར་བས་སོ། །གང་གི་ཕྱིར་བཞི་པ་ལ་འོད་འཕྲོ་བ་ཞེས་བྱ་ཞེ་ན། འདི་ལྟར་དེ་ཡིས་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་དེ་དག་ལ་གནས་པར་གྱུར་པ་ན། དེ་ལ་གནས་པར་གྱུར་པ་ཉིད་ཀྱིས་ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་ཐམས་ཅད་སྲེག་པར༌[^831]བྱེད་པས་སོ། །ཅིའི་ཕྱིར་ས་ལྔ་པ་ལ་ཤིན་ཏུ་སྦྱང་དཀའ་བ་ཞེས་བྱ་ཞེ་ན། གང་གིས་དེ་བདེན་པར༌[^832]ཤེས་པའི་རྣམ་པར་མི་རྟོག་པ་དང་། འཇིག་རྟེན་པའི་བཟོ་དང་བསྟན་བཅོས་ལ་སོགས་པ་རྣམ་པར་རྟོག་པ་དང་བཅས་པ་ཀུན་ཏུ་སྒྲུབ་པར་བྱེད་པ་ན་དེ་དག་འགལ་བས་ཤིན་ཏུ་དཀའ་བ་དང་། དེ་གཉིས༌[^833]འགལ་བ་ཡང་མངོན་པར་སྒྲུབ་པར་བྱེད་པ་ན་སྡུག་བསྔལ་བས་ཤིན་ཏུ་སྦྱང་དཀའ་བ་ཞེས་བྱའོ། །

[Block 1292]
ཡང་གང་གི་ཕྱིར་དྲུག་པ་ལ་མངོན་དུ་གྱུར་པ་ཞེས་བྱ་ཞེ་ན། འདི་ལྟར་དེས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཤེས་པ་ལ་གནས་པར་གྱུར་པ་ན། །དེ་ནས་དེ༌[^834]རྣམ་པར་མི་རྟོག་པ་ལ༌[^835]གནས་པའི་ཡེ་ཤེས་ཀྱི་སྟོབས་ཀྱིས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བས་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་མ་ཡིན་རྣམ་པར་དག་པའི་ཆོས་ཀྱང་མ་ཡིན། བདུན་པ༌[^836]མངོན་པར་འདུ་བྱེད་པ་དང་ལྡན་པ་དང་།

[Block 1293]
བརྒྱད་པ་མངོན་པར་འདུ་བྱེད་པ་མེད་པ་ལ་མངོན་དུ་ཕྱོགས་པར་གྱུར་པས་སོ། །ཅིའི་ཕྱིར་ས་བདུན་པ་ལ་རིང་དུ་སོང་བ་ཞེས་བྱ་ཞེ་ན། འདི་ནི་སྦྱོར་བ་ལས་བྱུང་བའི་སྤྱོད་པ་དེའི་མཐར་འགྲོ་བར་འགྱུར་བ༌[^837]ཡིན་པ་དང་། གང་གི་ཕྱིར་མཚན་མ་ཐམས་ཅད་ཀྱིས་མི་བསྐྱོད་པས་མངོན་པར་འདུ་བྱེད་པ་དང་བཅས་པར་གྱུར་པས་སོ། །ཅིའི་ཕྱིར་ས་བརྒྱད་པ་ལ་མི་གཡོ་བ་ཞེས་བྱ་ཞེ་ན། མཚན་མ་མེད་པ༌[^838]དང་། མངོན་པར་འདུ་བྱེད་པ་ཐམས་ཅད་ཀྱིས་བསྐྱོད་པར་མི་ནུས་པ་སྟེ། རང་གི་ངང་གིས་འཇུག་པའི་ཕྱིར་དང་། རྣམ་པར་རྟོག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1294]
ཅིའི་ཕྱིར་ས་དགུ་པ་ལ་ལེགས་པའི་བློ་གྲོས་ཞེས་བྱ་ཞེ་ན། ལེགས་པའི་བློ་ནི་ལེགས་པའི་བློ་གྲོས་ཏེ། འདིར་སོ་སོ་ཡང་དག་པར་རིག་པ་ནི་འདིར་བློ་གྲོས་ཀྱི་སྒྲས་བསྟན་ཏེ། ཡེ་ཤེས་དེ་ནི་འདིར་ལེགས་པའི་བློ་གྲོས་ཞེས་བྱའོ། །ཅིའི་ཕྱིར་ས་བཅུ་པ་ལ་ཆོས་ཀྱི་སྤྲིན་ཞེས་བྱ་ཞེ་ན། གང་གིས་ཆོས་ཐམས་ཅད་བསྡུས་པ་ལ་དམིགས་པའོ། །

[Block 1295]
འདི་ལྟར་དེ་ལ་ཡེ་ཤེས་ནི་སྤྲིན་ལྟ་བུའོ། །

[Block 1296]
ཏིང་ངེ་འཛིན་དང་གཟུངས་ཀྱི་སྒོ་རྣམས་ནི་ཆར་གྱི་ཆུ་ལྟ་བུའོ། །

[Block 1297]
དེ་ཡང་ཡེ་ཤེས་དེའི་ཁོང་ན་གནས་པ༌[^839]སྟེ། འདི་ལྟར་ནམ་མཁའ་སྤྲིན་གྱིས་ཁེབས་པར་བྱས་ནས་གནས་པ་ལྟར་འདྲེས་པའི་ཆོས་ལ་དམིགས་པའི་ཡེ་ཤེས་ཀྱིས་ཀྱང་སྒྲིབ་པ་རྒྱ་ཆེན་པོ་རྣམས་མི་མངོན་པར་བྱེད་དོ། །

[Block 1298]
ཆོས་ཀྱི་སྐུ་ཡོངས་སུ་རྫོགས་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྤྲིན་གྱིས༌[^840]ནམ་མཁའ་རྒྱས་པར་འགེངས་པ་ལྟར་ཆོས་ཀྱི་སྐུས་བྱང་ཆུབ་སེམས་དཔའི་རྟེན་ལ་རྒྱས་པར་འགེངས་སོ། །

[Block 1299]
འདིར་འགེངས་པ་ནི་སྤྲོས་པའོ། །

[Block 1300]
འགྲུབ་པས་ཐོབ་པ༌[^841]ནི་ཞེས་བྱ་བ་ནི་གང་གིས་ས་འདི་རྣམས་བསྒོམ་པ༌[^842]ལས་མཐར་ཕྱིན་པར་འགྱུར་བའོ་ཞེས་བལྟ་བར་བྱའོ། །
--- END BLOCKS ---
