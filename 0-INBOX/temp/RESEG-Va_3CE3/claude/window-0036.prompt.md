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
ཆོས་གནས་པ་འདི་ཉིད་མཁྱེན་པས། དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བ་དག་འཇིག་རྟེན་ན་སྣང་སྟེ། འདི་ཉིད་དེ་དག་གི་མངོན་པར་རྟོགས་པ་དང་། འདི་ཉིད་ཆོས་ཀྱི་འཁོར་ལོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1262]
རབ་འབྱོར་འདི་ནི་ཆོས་ཀྱི་འཁོར་ལོ་གཉིས་སུ་བསྐོར་བ་ཡང་མ་ཡིན། གཅིག་ཏུ་བསྐོར་བ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དོན་དམ་པར་ཆོས་ཐམས་ཅད་གྲངས་ལས་འདས་པའི་ཕྱིར་དེ་སྐད་བསྟན་ཏོ། །

[Block 1263]
ཆོས་གང་ཡང་བསྐོར་བའམ་མི་བསྐོར་བར་བྱ་བའི་ཕྱིར་ཉེ་བར་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་རོ་ཞེས་བྱ་བའི་འདུ་ཤེས་སམ། རྣམ་པར་རྟོག་པ་སེལ་བར་བྱེད་པའོ། །

[Block 1264]
དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི༌[^891]ཆོས་ཐམས་ཅད་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱི་མཚན་ཉིད༌[^892]དུ་འཛིན་ཏོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1265 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཆོས་ཐམས་ཅད་ལ་འཇུག་པ། ^1-2-5-6-0

[Block 1266]
ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་ཆེན་མོ༌[^893]སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིག་དགུ་བཅུ་རྩ་ལྔས་གནས་བརྟན་རབ་འབྱོར་གྱིས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ཆོས་ཐམས་ཅད་ལ་འཇུག་པ་རྒྱ་ཆེར་སྟོན་ཏེ།[^894] དེ་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་ཆེན་པོ་ཞེས་བྱ་བ༌[^895]ནི་ཡུལ་ཆེ་བ་དང་། གསང་བ་ཆེན་པོ་ཡུལ་དུ་གྱུར་པ༌[^896]སྟོན་ཏེ། འདི་ལྟར་གསང་བ་ནི་གསུམ་སྟེ་ཆོས་འཇུག་པ་གསང་བ་དང་། མངོན་པར་བྱང་ཆུབ་པ་གསང་བ་དང་། ཆོས་ཉིད༌[^897]ཀྱི་འཁོར་ལོ་བསྐོར་བ་གསང་བའོ། །

[Block 1267 [HEADING]]
###### ཆོས་འཇུག་པ་གསང་བ། ^1-2-5-6-1-0

[Block 1268]
དེ་ལ་ཆོས་རྣམས་ལ་ཀུན་རྫོབ་དང་དོན་དམ་པའི་དབང་གིས་ཆོས་སུ་འདུ་ཤེས་པ་ཡང་འཇུག་ཆོས་མ་ཡིན་པར་འདུ་ཤེས་པ་ཡང་འཇུག་སྟེ། དེ་བས་ན་ཆོས་ཐམས་ཅད་ཀྱང་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་གྱིས་ཡོངས་སུ༌[^898]སྟོང་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1269 [HEADING]]
###### མངོན་པར་བྱང་ཆུབ་པ་གསང་བ། ^1-2-5-6-2-0

[Block 1270]
མངོན་པར་བྱང་ཆུབ་པ་ཡང་སྟོན་ལ་མངོན་པར་བྱང་ཆུབ་པ་མེད་པར་ཡང་མཐོང་སྟེ། དེ་བས་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་ཤིང་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་ཡང་། ཆོས་གང་ཡང་མངོན་པར་རྫོགས་པར་མཚང་རྒྱ་བ་མ་མཆིས་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1271 [HEADING]]
###### ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་གསང་བ། ^1-2-5-6-3-0

[Block 1272]
ཆོས་ཀྱི་འཁོར་ལོ་ཡང་བསྐོར་ལ་ཆོས་གང་ཡང་བསྐོར་བའམ་མི་བསྐོར་བར་བགྱིད་པ་ཡང༌[^899]མ་མཆིས་ཏེ་ཞེས་བྱ་བས་ནི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་གསང་བ་བསྟན་ཏོ། །

[Block 1273]
དེའི་འོག་ཏུ་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་རྣམ་པ་བརྒྱད་ཀྱིས་འགྲེལ་ཏེ། ཆོས་མེད་པ་དང་འཁོར་ལོ་མེད་པ་དང་། བསྐོར་བ༌[^900]མེད་པ་དང་བཤད་པའི་ངོ་བོ་ཉིད་མེད་པ་དང་། འཆད་པ་པོ་མེད་པ་དང་ཉན་པ་པོ༌[^901]མེད་པ་དང་རྟོག་པ་མེད་པ་དང་། འཕགས་པའི་གང་ཟག་མེད་པའོ། །

[Block 1274 [HEADING]]
###### **ཆོས་མེད་པ།** ^1-2-5-6-3-1-0

[Block 1275]
དེ་ལ་ཆོས་མེད་པ་ནི་ཆོས༌[^902]གང་ཡང་ཡོངས་སུ་མཐོང་བ་ཡང་མ་མཆིས་ལ་ཆོས་གང་ཡང་ཡོངས་སུ་མ་མཐོང་བ་ཡང་མ་མཆིས་པ་ལགས༌[^903]སོ་ཞེས་བྱ་བ་གསུངས་པའོ། །

[Block 1276 [HEADING]]
###### **འཁོར་ལོ་མེད་པ།** ^1-2-5-6-3-2-0

[Block 1277]
འཁོར་ལོ་མེད་པ་ནི་འདི་ལྟར་གང་བསྐོར་བར་བགྱིའམ་མི་བསྐོར་བར༌[^904]བགྱི་བའི་ཆོས་དེ་ལྟ་བུ་དམིགས་པ་མ་མཆིས་ཏེ་ཞེས་བྱ་བ་གསུངས་པའོ། །

[Block 1278 [HEADING]]
###### **བསྐོར་བ་མེད་པ།** ^1-2-5-6-3-3-0

[Block 1279]
བསྐོར་བ་མེད་པ་ནི་སྟོང་པ་ཉིད་ནི་བསྐོར་བར་བགྱིད་པའམ་མི་བསྐོར་བར་བགྱིད་པ་མ་ལགས་སོ། །

[Block 1280]
མཚན་མ་མ་མཆིས་པ་དང་སྨོན་པ་མ་མཆིས་པ་ནི་བསྐོར་བར་བགྱིད་པ་འམ་མི་བསྐོར་བར་བགྱིད་པ་མ་ལགས་སོ་ཞེས་བྱ་བ་གསུངས་པའོ། །

[Block 1281 [HEADING]]
###### **བཤད་པའི་ངོ་བོ་ཉིད་མེད་པ།** ^1-2-5-6-3-4-0

[Block 1282]
བཤད་པ་མེད་པ་ནི་དེ་ལྟར་ན་གང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པ་དང་། རབ་ཏུ་བསྟན་པ་དང་ཞེས་བྱ་བ་ནས་འདི་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པ་ཡོངས་སུ་དག་པའོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པའོ། །

[Block 1283 [HEADING]]
###### **འཆད་པ་པོ་མེད་པ།** ^1-2-5-6-3-5-0

[Block 1284]
འཆད་པ་མེད་པ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པ་དེ་ཡང་སུས་ཀྱང་མ་བསྟན་ཞེས་བྱ་བ་གསུངས་པའོ། །

[Block 1285 [HEADING]]
###### **ཉན་པ་པོ་མེད་པ།** ^1-2-5-6-3-6-0

[Block 1286]
ཉན་པ་མེད་པ་ནི་སུས་ཀྱང་མ་བཟུང་ངོ་ཞེས་བྱ་བ་གསུངས་པའོ། །

[Block 1287 [HEADING]]
###### **རྟོག་པ་མེད་པ།** ^1-2-5-6-3-7-0

[Block 1288]
རྟོགས་པ་མེད་པ་དེ་ནི་སུས་ཀྱང་མངོན་སུམ་དུ་མ་བགྱིས་སོ་ཞེས་བྱ་བ་གསུངས་པའོ། །

[Block 1289 [HEADING]]
###### **འཕགས་པའི་གང་ཟག་མེད་པ།** ^1-2-5-6-3-8-0

[Block 1290]
འཕགས་པའི་གང་ཟག་མེད་པ་ནི་དེ་ལ་ནི་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་སུ་ཡང་མ་མཆིས་ཏེ། ཆོས་བསྟན་པ་འདི་ལ་སུ་འང་སྦྱིན་གནས་སུ་འགྱུར་བ་མ་མཆིས་སོ་ཞེས་བྱ་བ་གསུངས་པའོ། །

[Block 1291]
རབ་འབྱོར་ནམ་མཁའ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ནམ་མཁའ་ལྟར་དམིགས་པའི་བདག་ཉིད་དུ་མེད་པ་ཡིན་གྱི། དམིགས་པ་མེད་པའི་བདག་ཉིད་དུ་མེད་པ་མ་ཡིན་ནོ། །

[Block 1292]
ཆོས་ཐམས་ཅད་དམིགས་པ་མེད་པར་མཉམ་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ནི༌[^905]ཀུན་བརྟགས་པ་སྟེ་དམིགས་སུ་མེད་པའི་བདག་ཉིད་དུ་མཉམ་པའོ། །

[Block 1293]
མིང་མེད་པ་དང་ལུས་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་གཟུགས་མེད་པའི་ཆོས་དང་། གཟུགས་ཀྱི་ཆོས་རྣམས་ཚིག་ཏུ་གྱུར་པ་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1294]
དབུགས་ཕྱི་ནང་དུ་རྒྱུ་བ་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ལུས་སྟོང་པ་ནམ་མཁའ་ལྟ་བུ་ལ་དབུགས་ཕྱི་ནང་དུ་རྒྱུ་བ་ཡང་མེད་དོ་ཞེས་སོ་སོར་རྟོག་པའི་ཕྱིར་རོ། །

[Block 1295]
རྣམ་པར་རྟོག་པ༌[^906]དང་རྣམ་པར་དཔྱོད་པ་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་རྣམ་པར་རྟོག་པ་དང་རྣམ་པར་དཔྱོད་པ་གཉིས་ཚིག་མངོན་པར་འདུ་བྱེད་པ་ཡིན་པའི་ཕྱིར་དེ་སྐད་གསུངས་ཏེ་སྔར་རྣམ་པར་བརྟགས་རྣམ་པར་དཔྱད་ནས་ཕྱིས་ཚིག་འབྱིན་ཏོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1296]
ཚོར་བ་དང་འདུ་ཤེས་དང་འདུ་བྱེད་དང་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་དེ་དག་གཟུགས་མེད་པས་མིང་གི་ཚོགས་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1297]
ཆོས་ཐམས་ཅད་འགྲོ་བ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་འགྲོ་བ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1298]
ཆོས་ཐམས་ཅད་གཟུང་དུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ་ཆོས་རྣམས་ནི་ཆོས་རྣམས་མི་འཛིན་ཏེ། དེ་བས་ན་མི་འཕྲོགས་པའོ། །

[Block 1299]
ཆོས་ཐམས་ཅད་ཤིན་ཏུ་བྱང་ཞིང་ཟད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཤིན་ཏུ་བྱང་བས་སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པའི་བདག་ཉིད་ཀྱིས་ཟད་པར་སྣང་བའོ། །

[Block 1300]
ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པ་དང་འགག་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་སྟོང་པ་སྟེ་སྐྱེ་བ་ཡང་མེད་འགག་པ་ཡང་མེད་པར་སྣང་བའོ། །
--- END BLOCKS ---
