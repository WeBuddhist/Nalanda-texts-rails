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
ཆགས་པ་ལ་དགའ་བའི་རྣལ་འབྱོར་པ་གང་ཞིག་གིས་གང་དུ་ཇི་ལྟར་གནས་པར་ཇི་ལྟར་འགྱུར་ཞེ་ན། རྡོ་རྗེ་པདྨོ་མཉམ་སྦྱོར་བས། །ཞེས་བྱ༌[^671]ནི་ཕོ་དང་མོའི་དབང་པོ་གཉིས་སྙོམས་པར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 1262]
ཡེ་ཤེས་གསུམ་གྱི་ཆ་རིག་པ། །ཞེས་བྱ་བ་ནི་རང་བཞིན་མེད་པའི༌[^672]སྐྱེ་བ་དང་འགག་པའི་བྱེ་བྲག་གི་ཡེ་ཤེས་གསུམ་རིག་པའོ། །

[Block 1263 [VERSE]]
བློ་ལ་གོས་དང་མ་གོས་པ། །
[^673]ཞེས་པ་ནི་གཟུང་བ་དང་འཛིན་པའོ། །
དེར་ནི་བདེ་བར་རྟག་ཏུ་གནས། །

[Block 1264]
ཞེས་པ་ནི་བདེ་བ་ཉིད་ལ་གནས་པའོ་ཞེའོ། །

[Block 1265]
འདི་དག་གི་དོན་ཡང་གང་གིས༌[^674]རང་གི་བདག་ཉིད་ཀུན་དུ་གནས་པར་གྱུར་ནས་གང་དུ་གང་དང་འབྲེལ་པར༌[^675]བྱས་ནས་ཀུན་དུ་བདེ་བའི་རྣམ་པ་ཅན་གྱི་སེམས་དང་པོ་ནི་དེའི་སྐུར་པ་ལ༌[^676]གཟུང་ངོ་། །དེར་ནི་དང་པོ་འཕེལ་བར་འགྱུར་རོ། །

[Block 1266]
དེ་ནས་ནི་འགག་པར་འགྱུར་རོ། །

[Block 1267]
ས་པི་ཏིའི་གནས་སུ་ནི་རང་གི་རྣམ་གྲངས༌[^677]ལ་དང་པོ་ནི་འཕེལ་བར་འགྱུར་རོ། །

[Block 1268]
དེ་ནས་ནི་འགག་པར་འགྱུར་རོ། །

[Block 1269]
དེ་ནས་ནི་སྨད་པའི་གནས་སུ་ནི༌[^678]

[Block 1270]
དང་པོ་ནི༌[^679]འཕེལ་བར་འགྱུར་རོ། །

[Block 1271]
དེ་ནས་ནི་འགག་པར་འགྱུར་རོ། །

[Block 1272]
གང་གིས་གང་ནི་ལོག་པའི་དུས་སུ་ཡང་འདི་དག་ནི་སྦྱོར་བ་རབ་ཏུ་གནས་པར་འགྱུར་རོ། །

[Block 1273]
སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ནི་བཤད་ཟིན་ཏོ། །

[Block 1274]
དངོས་བདག་ཀུན་ལ་རྣམ་པར་རོལ། །ཞེས་པ་ནི་སྙོམས་པར་འཇུག་པའོ། །

[Block 1275]
སངས་རྒྱས་མཛད་པ་ནི་འོག་ནས་སྟོན་ཏེ་སྤྱན་མར་འགྱུར་རོ༌[^680]ཞེས་བྱ་བ་ལ་སོགས་པ་དང་དུས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན༌[^681]ཏོ། །

[Block 1276 [VERSE]]
གཏན་ལ་དབབ་པའི་བཞི༌[^682]ལ་གནས། །
ཞེས་པ་ནི་བསམ་གཏན་ལ་གནས་པའོ། །
རྣལ་འབྱོར་ལྷག་པའི་རྣལ་འབྱོར་དང་། །

[Block 1277]
ཞེས་པ༌[^683]ལ་སོགས་པ་ལ་ཏིང་ངེ་འཛིན་གང་གིས་བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པ་རྒྱན་དང་བཅས་པ་ལ་རྩེ་གཅིག་པའོ། །

[Block 1278]
དེས་ཅིར་འགྱུར་ཞེ་ན། རྣལ་འབྱོར་ཆེན་པོར༌[^684]རང་ཉིད་འགྱུར་རོ། །

[Block 1279]
རྡོ་རྗེ༌[^685]ཅན་ནི་གཙོ་བོ་ལ་སོགས་པའོ། །

[Block 1280 [VERSE]]
མཁའ་འགྲོ་ནི་མཁའ་འགྲོ་མའོ། །
གང་ཡང་རྣལ་འབྱོར་དེ་རང་ཉིད། །

[Block 1281]
ཅེས་པ་ནི་གང་རྡོ་རྗེ་ཅན་ལ་སོགས་པ་ཡང་དེ་ཉིད་དོ་ཞེས་པས་ཐ་དད་པ་མ་ཡིན་པར་བསྟན་ཏོ། །

[Block 1282]
ཀུན་རྫོབ་ཀྱི་བདེན་པ་ལ་གང་ཞིག་གིས་གནས་པས་ཅིར༌[^686]འགྱུར་ཞེ་ན། བཀག་པ་དག་ཀྱང་བྱེད་པས་ན། །ཞེས་པ་ནི་རྟོག་པའི་དྲ་བ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1283]
བྱ་དང་བྱ་མིན་རྣམ་སྤངས་ཏེ། །ཞེས་པ་ནི་ཕུང་པོ་ལ་སོགས་པ་བླང་དོར་གྱི་ཆོས་སྤངས་པའོ། །

[Block 1284]
དེ་ལྟར་ཤེས་པས་ཅིར་འགྱུར་ཞེ་ན།

[Block 1285 [VERSE]]
པདྨ་ལ་ནི་འདམ་གྱིས༌[^687]བཞིན། །
ངོ་བོ་ཉིད་ཤེས་གོས་མི་འགྱུར། །

[Block 1286]
ཞེས་པ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་ཤེས་པས་འཁོར་བའི་ཉེས་པས་མི་གོས་ཞེས་པའོ། །

[Block 1287]
ཡོན་ཏན་བརྒྱད་ནི་དབང་དང་ལྡན་པ་ལ་སོགས་པའོ། །

[Block 1288]
སེམས་ཅན་ཐམས་ཅད་རིགས༌[^688]འགྱུར་ཞིང་། །ཞེས་པ་ནི་དེ་ལྟ་བུའི་ཆོས་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1289 [VERSE]]
འཇིག་རྟེན་ཁམས་རྣམས་མ་ལུས་པར། །
བདག་ཉིད་ཡེ་ཤེས་ལུས་ཀྱིས་སྤྱོད། །

[Block 1290]
ཅེས་པ་ནི་དེ་ལྟ་བུའི་ནུས་པ་དང་ལྡན་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1291]
གཙོ་བོ་གང་དུ་སྤྱོད་འགྱུར་བ། །ཞེས་པ་ནི་གཙོ་བོ་གང་དང་གང་དུ༌[^689]གནས་པའོ། །

[Block 1292]
དེ་ཡི་ཁྱིམ་ནི་ནམ་མཁའ་ཉིད། །ཅེས་པ་ནི་གང་གིས་སྟོང་པ་ཉིད་ཀྱི་ངང་ལ་གནས་པའི་ཕྱིར་རོ། །

[Block 1293]
བདེ་བ་ཆེན་པོའི་ཡུལ་དུ་བྱེད་པ་ནི་བདེ་བ་ཆེན་པོའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 1294]
རྟག་ཏུ་དགྱེས་པ་ནི་རྟག་ཏུ་དགྱེས་པ་སྟེ།

[Block 1295 [VERSE]]
རང་བཞིན་གྱིས་དགའ་ཞེས་པའི་དོན་ཏོ། །
འདི་ལ་སྣང་བ་དབྱེ་བ་ལ། །
ཞེས་པ་ནི་ཐུན་མཚམས་ཉིན་མོ་མཚན་མོ་ཡི། །

[Block 1296]
ཞེས་པ་སྟེ་གང་གི་མཚམས་ལ་སོགས་པར་རང་གི་ཡེ་ཤེས་སྐྱེ་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1297 [VERSE]]
སྣ་ཚོགས་པ་ཡི་ཐ་སྙད་དག །
འཇིག་རྟེན་པས་ནི་ཡོངས་བརྟགས༌[^690]པ། །

[Block 1298]
ཞེས་པ་ནི་བདག་ལ་སོགས་པ་དང་ས་ལ་སོགས་པར༌[^691]བརྟགས་པའོ། །

[Block 1299 [VERSE]]
ལམ་གསུམ་གྱི་ནི་དབྱེ་བ་ཡིས། །
ཡེ་ཤེས་གསུམ་དུ་རབ་ཏུ་འགྱུར། །

[Block 1300]
ཞེས་པ་ནི་གང་གིས་ལམ་གསུམ་ལ་བརྟེན་པས་འགག་པ་དང་སྐྱེ་བར་འགྱུར་ཞེས་པའོ། །
--- END BLOCKS ---
