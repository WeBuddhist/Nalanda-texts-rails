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
འདི་ལྟར་དེ་དག་བསམ་པ་རྫོགས་པ་དང་། །ཞེས་པ་ནས། །ཤིན་ཏུ་རྒྱས་པའི་མདོ་སྡེ་རབ་ཏུ་བཤད། །ཅེས་པའི༌[^1205]བར་དུ་ནི་ཡོན་ཏན་ལྔ་དང་ལྡན་པའི་གང་ཟག་མ་འོངས་པའི་དུས་སུ་འཚང་རྒྱ་བར་འགྱུར་རོ། །

[Block 1262]
དེ་ཡང་སངས་རྒྱས་དྲན་པའི་བསམ་པ་རྫོགས་པ་དང་། རྣམ་པར་དག་པའི་ཚུལ་ཁྲིམས་དང་ལྡན་པའོ། །

[Block 1263]
སངས་རྒྱས་དྲན་པ་ལ་རྣམ་པ་གཉིས་ཏེ་སེམས་ཀྱིས༌[^1206]དྲན་པ་དང་ཚིག་གིས་བརྗོད་པའོ། །

[Block 1264]
ཚུལ་ཁྲིམས་དང་ལྡན་པ་བསླབ་པ་གསུམ་རྫོགས་པ༌[^1207]ལ་ལུང་སྟོན་པར་འགྱུར་ཏེ། དེ་དག་ཐོས་ནས་ཤིན་ཏུ་དགའ་བར་འགྱུར་ཞེས་སྨོས་སོ། །

[Block 1265]
མདོ་ལས།

[Block 1266 [HEADING]]
###### **གནས་པར་བསྐུལ་བ།** ^4-2-11-1-1-2-2-4-0

[Block 1267]
འདི་ལྟར་འདྲེན་པའི་ཉན་ཐོས་དེ་དག་ལས། །ཞེས་པ་ནས། །ཐམས་ཅད་བྱང་ཆུབ་འགྱུར་བར༌[^1208]ཐེ་ཙོམ་མེད། །ཞེས་པའི་བར་དུ་ནི་དད་པ་སྐྱེད་པར་བསྐུལ་བ་སྟེ། ཆོས་འདི་ཐོས་སམ་གཟུང་ཡང་རུང་ཐེག་པ་ཆེན་པོ་ལ་གནས་པར་འགྱུར་བ་བསྟན༌[^1209]པའོ། །

[Block 1268]
མདོ་ལས།

[Block 1269 [HEADING]]
###### **བཅས་པ།** ^4-2-11-1-1-2-3-0

[Block 1270]
ཐེག་པ་གཅིག་སྟེ་གཉིས་སུ་མེད། །ཅེས་པ་ནས། །ཐེག་པ་སྣ་ཚོགས་མངོན་པར་བསྟན། །ཞེས་པའི་བར་དུ་ནི་ཚིག་ཕྱེད་དང་གཉིས་པོ་འདིས་གཉིས་སུ་མེད་པ་བསྟན་པ་སྟེ། གཉིས་སུ་མེད་པ་ནི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་མེད་ཅེས་པའི་དོན་ཏོ། །

[Block 1271]
གསུམ་དུ་མེད་པ་ནི་ཉན་ཐོས་ཀྱི་ཐེག་པ་མེད་པ་སྟེ། སངས་རྒྱས་ཀྱིས༌[^1210]ཐབས་སུ་གསུངས་པ་མ་གཏོགས་པར་ཐེག་པ་ཆེན་པོ་ལས་གཉིས་དང་གསུམ་དུ་མེད་ཅེས་བསྟན་ཏོ། །

[Block 1272]
མདོ་ལས།

[Block 1273 [HEADING]]
###### **དོན་གང་ལ་གནས་པར་བྱ་བ།** ^4-2-11-1-1-2-4-0

[Block 1274]
སངས་རྒྱས་ཡེ་ཤེས་བསྟན་པའི་ཕྱིར། །ཞེས་པ་ནས། །ཐེག་པ་ཆུང་ངུས་མི་འདྲེན་སངས་རྒྱས་ཀྱི།[^1211] །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་ཕྱེད་དང་བཅུ་དགུས་དོན་གང་ལ་གནས་པར་བྱ་བ་བསྟན་པ་སྟེ། དེ་ལ་ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་བྱ་བ་ཆེན་པོ་གཅིག་བསྟན་པའོ། །

[Block 1275]
ཚིག་བཅུ་བདུན་གྱིས་ནི་འཛུད་པ་དང་སྟོན་པ་དང་། འཇུག་པ་དང་ཆུད་པར་བྱེད་པ་བསྟན་པའོ། །

[Block 1276 [HEADING]]
###### **བྱ་བ་ཆེན་པོ་གཅིག།** ^4-2-11-1-1-2-4-1-0

[Block 1277]
སངས་རྒྱས་འཇིག་རྟེན་དུ་བྱུང་བ་ནི་བྱ་བ་གཅིག་གི་ཕྱིར་ཏེ། སངས་རྒྱས་ཀྱི་ཐེག་པ་གཅིག་སྟེ་གཉིས་སུ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1278]
མདོ་ལས།

[Block 1279 [HEADING]]
###### **འཛུད་པ་དང་སྟོན་པ་དང་འཇུག་པ་དང་ཆུད་པར་བྱ་བ།** ^4-2-11-1-1-2-4-2-0

[Block 1280]
རང་བྱུང༌[^1212]བདག་ཉིད་གཅིག་ལ་གནས་པ་དང་། །ཞེས་པ་ནས། །དེ་དག་ལ་ཡང་སེམས་ཅན་སོ་སོར་འཇོག །ཅེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་བཅུ་བདུན་གྱིས་འཛུད་པ་དང་སྟོན་པ་དང་། འཇུག་པ་དང་ཆུད་པར་བྱ་བ་བསྟན་པ་སྟེ། ཐོག་མའི་ཚིག་གཅིག་གིས་འཛུད་པ་བསྟན་ཏོ། །

[Block 1281]
ཚིག་ལྔས་ནི་འཇུག་པ་བསྟན་ཏོ། །

[Block 1282]
ཚིག་གཅིག་གིས་ནི་ཆུད་པར་བྱ་བ་བསྟན་ཏོ། །

[Block 1283 [HEADING]]
###### **འཛུད་པ།** ^4-2-11-1-1-2-4-2-1-0

[Block 1284]
ཚིག་བཅུས་ནི་སྟོན་པ་བསྟན་པ་སྟེ། གནས་པ་ནི་བརྟེན་པའི་དོན་ཏེ་མྱ་ངན་ལས་འདའ་བ་དང་། བྱང་ཆུབ་ལ་བདེ་བར་གནས་པའོ། །

[Block 1285]
སྟོབས་དང་བསམ་གཏན་ཚད་མེད་པས་བརྒྱན་ཏེ་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་སུ་འགྱུར་བའི་ཡོན་ཏན་ཐམས་ཅད་ཆོས་འདི་གཉིས་ཀྱི་ནང་དུ་འདུ་སྟེ། སེམས་ཅན་ཐམས་ཅད་དེ་ལ་འཇོག་པས་འཛུད་པ་ཞེས་བྱའོ། །

[Block 1286]
མདོ་ལས།

[Block 1287 [HEADING]]
###### **འཇུག་པ།** ^4-2-11-1-1-2-4-2-2-0

[Block 1288]
སེར་སྣའི་ཉེས་པ་ང་ལ་ཡོད་པར༌[^1213]འགྱུར། །ཞེས་པ་ནས། །སེམས་ཅན་གཅིག་ཀྱང་རུང་སྟེ་ང་མི་དགེ །ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་ལྔས་ནི་འཇུག་པ་བསྟན་པ་སྟེ། དེ་ལ་ཡང༌[^1214]གསུམ་དུ་དབྱེའོ། །

[Block 1289]
ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་མཉམ་པ༌[^1215]བསྟན་ཏོ། །

[Block 1290]
ཚིག་ཕྱེད་དང་གསུམ་གྱིས་ནི་ཡོན་ཏན་གྱི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 1291]
ཚིག་གཅིག་གིས་ནི་འཇུག་པ་ཉིད་བསྟན་ཏེ། བྱང་ཆུབ་མཆོག་རབ་ཅེས་བྱ་བ་ནི་བླ་ན་མེད་པའི་ཐེག་པ་ཆེན་པོ་དོན་དམ་པའོ། །

[Block 1292 [HEADING]]
###### **མཉམ་པ།** ^4-2-11-1-1-2-4-2-2-1-0

[Block 1293]
སངས་རྒྱས་ཀྱི་བླ་ན་མེད་པའི་ཐེག་པ་མཉམ་པ་བརྙེས་ན་དེ་ལ་བདག་གམ་ཕ་རོལ་ཞེས་ཐ་དད་པར་ག་ལ་ཞིག་འབྱེད་དེ། ནང་གི་ཡེ་ཤེས་མི་མཉམ་ན་བདག་འབའ་ཞིག་ཐེག་པ་ཆེན་པོ་ལ་འཇུག་པར་བྱེད་ཕྱི་རོལ་གྱི་ཡེ་ཤེས་མི་མཉམ་ན་ཕ་རོལ་པོ་ཐེག་པ་ཆུང་ངུ་ལ་འཇོག་པར་འགྱུར། སྒྲིབ༌[^1216]དང་མ་བྲལ་ན་བླ་ན་མེད་པའི་ཐེག་པ་ཆེན་པོར་ག་ལ་རུང་སྟེ། དེ་བས་ན་སེར་སྣའི་ཉེས་པ་ང་ལ་ཡོད་ན་མི་དགེ་ཞེས་སྨོས་པ་ཡིན་ནོ། །

[Block 1294]
མདོ་ལས།

[Block 1295 [HEADING]]
###### **ཡོན་ཏན་གྱི་ཁྱད་པར།** ^4-2-11-1-1-2-4-2-2-2-0

[Block 1296]
ང་ལ་སེར་སྣ་དག་ནི་ཆུང་ཟད༌[^1217]མེད། །ཞེས་པ་ནས། །འགྲོ་བ་ཀུན་རིག་དེ་བས་ང་སངས་རྒྱས། །ཞེས་པའི་བར་དུ་ནི་ཡོན་ཏན་གྱི་ཁྱད་པར་བསྟན་པ་སྟེ། དེ་ལ་ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ང་འདོད་ཆགས་དང་བྲལ་བས་འཇིགས་པ་མེད་པའི་ཡོན་ཏན་བསྟན་ཏོ། །

[Block 1297]
ཚིག་འོག་མ་གཅིག་གིས་ནི་ཕྱི་རོལ་གྱི་རྒྱན་དང་ཡང་དག་པའི་ཆོས་ཀྱི་ཡོན་ཏན་བསྟན་ཏེ། སེར་སྣ་མེད་ཅེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོ་བཅབས་ཏེ། ཐེག་པ་ཆུང་ངུ་སྟོན་ཅིང་སེམས་ཅན་བསླུ་བའམ། སྔར་ཐེག་པ་ཆེན་པོ་སྦྱིན་པར་བྱ་བ་ལས་ཕྱིས་མ་སྦྱིན་པ༌[^1218]མ་ཡིན་པས་སེར་སྣ་མེད་དོ། །

[Block 1298]
སེམས་ཅན་གྱིས་ཐེག་པ་ཆེན་པོ་རིག་ཅིང་ཆུད་ཀྱིས༌[^1219]དོགས་པའི་ཐུགས་མི་མངའ་བས་ཕྲག་དོག་མེད་དོ། །

[Block 1299]
སྡིག་པའི་ཆོས་ནི་གང་ཉོན་མོངས་པའི་ལས་དང་བཅས་པ་སྡུག་བསྔལ་བ་འཁོར་བའི་ཆོས་ཡོངས་སུ་བཅད་པས་ཉེས་པའི་སྐྱོན་གང་ཡང་མེད་དེ། ཡང་དག་པའི་ཡེ་ཤེས་རྫོགས་ནས་ཕྱོགས་བཅུར་སེང་གེའི་སྒྲ་བསྒྲགས་ཏེ་འཇིགས་པ་མི་མངའ་བས། འགྲོ་བ་ཀུན་རིག་ང་སངས་རྒྱས། །ཞེས་བྱའོ། །

[Block 1300]
མདོ་ལས།
--- END BLOCKS ---
