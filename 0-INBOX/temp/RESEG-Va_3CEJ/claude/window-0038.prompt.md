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
[Block 1331 [HEADING]]
###### **གཉིད།** ^2-2-2-2-1-6-0

[Block 1332 [VERSE]]
གཉིད་ནི་ཀུན་ལ་མི་འགལ་ཕྱིར། །
གང་ལ་ཡོད་པ་དེས་བསྣན་ནོ། །

[Block 1333]
གཉིད་ནི་དགེ་བ་དང་། མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་དང་ཡིན་པའི༌[^580]ཕྱིར་ཇི་སྐད་བཤད་པའི་སེམས་ཐམས་ཅད་དང་མི་འགལ་བས། དེའི་ཕྱིར་གང་ལ་དེ་ཡོད་པ་དེ་ལ་དེས་བསྣན་པར་རིག་པར་བྱ་སྟེ། གང་ལ་ཉི་ཤུ་རྩ་གཉིས་འབྱུང་བ་དེ་ལ་ནི་ཉི་ཤུ་རྩ་གསུམ་མོ། །

[Block 1334]
[^581]གང་ལ་ཉི་ཤུ་རྩ་གསུམ་འབྱུང་བ་དེ་ལ་ནི་ཉི་ཤུ་རྩ་བཞིའོ༌[^582]ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 1335 [HEADING]]
###### བསམ་གཏན་དང་པོ་ལ་སོགས་པ། ^2-2-2-2-2-0

[Block 1336]
གང་དེ་ལྟར་འདོད་པའི་ཁམས་ཀྱི་སེམས་ལས་བྱུང་བ་ངེས་པར་བཤད་པ།

[Block 1337 [VERSE]]
དེ་ལས་འགྱོད་གཉིད་མི་དགེ་རྣམས། །
བསམ་གཏན་དང་པོ་དག་ན་མེད། །

[Block 1338]
བསམ་གཏན་དང་པོ་ན་ནི་ཇི་སྐད་བཤད་པ་དེ་ལས་འགྱོད་པ་དང་གཉིད་དང་། གང་ཡང་ཅུང་ཟད་མི་དགེ་བ་འདི་ལྟ་སྟེ། གཡོ་དང་སྒྱུ་དང་རྒྱགས་པ་མ་གཏོགས་པ་ཁྲོ་བ་ལ་སོགས་པ་དང་། ཁོང་ཁྲོ་བ་དང་ངོ་ཚ་མེད་པ་དང་ཁྲེལ་མེད་པ་དག་ཐམས་ཅད་དུ་མེད་དེ། གཞན་ཐམས་ཅད་ནི་དེ་དང་འདྲའོ། །

[Block 1339]
བསམ་གཏན་དང་པོ་ན་མེད་པ་གང་དག་ཡིན་པ་དེ་དག་ཁོ་ན་དང་། རྟོག་པ་འང་བསམ་གཏན་ཁྱད་པར་ཅན་ན་མེད་དེ།

[Block 1340 [VERSE]]
ལྷག་མ་ནི་དེ་དང་འདྲའོ། །
དེ་ཡི་གོང་ན་དཔྱོད་པ༌[^583]ཡང་། །

[Block 1341]
བསམ་གཏན་ཁྱད་པར་ཅན་ལས་གོང་མ་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་དང་། གཟུགས་མེད་པ་དག་ན་ནི་ཇི་སྐད་རྟོག་པ༌[^584]དང་། དཔྱོད་པ་ཡང་མེད་དོ། །

[Block 1342]
ཡང་ཞེས་བྱ་བའི་སྒྲས་ནི་གཡོ་དང་སྒྱུ་ཡང་མེད་དེ། ལྷག་མ་ནི་དེ་དང་འདྲའོ། །

[Block 1343]
ཚངས་པའི་བར་དུ་སྒྱུ་ཡོད་པར་འབྱུང་གི །འཁོར་དང་འབྲེལ་པ་མ་ཡིན་པའི་ཕྱིར་གོང་ན་ནི་མེད་དེ། དེ་ནི་རང་གི་འཁོར་གྱི་ནང་དུ་དགེ་སློང་རྟ་ཐུལ་གྱིས་འབྱུང་བ་ཆེན་པོ་འདི་དག་ཡོངས་སུ་མ་ལུས་པར་གང་དུ་འགག་པར་འགྱུར་ཞེས་དྲི་བ་དྲིས་པ་དང་། མི་ཤེས་པས་ཁོ་བོ་ནི་ཚངས་པའོ། །

[Block 1344]
ཚངས་པ་ཆེན་པོའོ། །

[Block 1345]
དབང་ཕྱུག་གོ། །

[Block 1346]
བྱེད་པ་པོའོ། །

[Block 1347]
སྤྲུལ་པ་པོའོ། །

[Block 1348]
འབྱིན་པར་བྱེད་པ་པོའོ། །

[Block 1349]
འབྱིན་པ་པོའོ། །

[Block 1350]
དངོས་པོ་རྣམས་ཀྱི་ཕ་ལྟ་བུ་ཡིན་ནོ༌[^585]ཞེས་གཏམ་རླུང་ལ་བསྐུར་རོ། །

[Block 1351]
ས་གང་ན་སེམས་གང་ལ་སེམས་ལས་བྱུང་བ་ཇི་སྙེད་ཅིག་འབྱུང་བ་དེ་ནི་བཤད་ཟིན་ཏོ། །

[Block 1352 [HEADING]]
##### སེམས་ལས་བྱུང་བ་ཁ་ཅིག་གི་ཐ་དད་དུ་བྱ་བ། ^2-2-2-3-0

[Block 1353 [HEADING]]
###### ངོ་ཚ་མེད་པ་དང་ཁྲེལ་མེད་པ། ^2-2-2-3-1-0

[Block 1354]
ད་ནི་གཞུང་ལ༌[^586]སེམས་ལས་བྱུང་བ་ཁ་ཅིག་གི་ཐ་དད་དུ་བྱ་བ་འབྱུང་བ་བརྗོད་པར་བྱ་སྟེ། ངོ་ཚ་མེད་པ་དང་ཁྲེལ་མེད་པ་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག་ཡོད་ཅེ་ན། མ་གུས་ངོ་ཚ་མེད། ཡོན་ཏན་རྣམས་དང་ཡོན་ཏན་ཅན་རྣམས་ལ་མ་གུས་པ་ཉིད་དེ། བཀུར་བ་མེད་པ་ཉིད་དང་། འཇིགས་པས་དབང་མི་སྒྱུར་བ༌[^587]ཉིད་ནི་ངོ་ཚ་མེད་པ་ཉིད་དེ་གུས་པའི་མི་མཐུན་པའི་ཕྱོགས༌[^588]སོ། །

[Block 1355]
ཁྲེལ་མེད། ཁ་ན་མ་ཐོ་འཇིགས་མི་ལྟ། །ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བ་ནི་དམ་པ་རྣམས་ཀྱིས་སྨད་པ་སྟེ། དེ་ལ་འཇིགས་པར་མི་ལྟ་བ་ནི་ཁྲེལ་མེད་པའོ། །

[Block 1356]
འདིར་འཇིགས་པ་ནི་མི་འདོད་པའི་འབྲས་བུ་སྟེ། འདི་ལས་འཇིགས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1357]
འདི་ཇི་ལྟར་ཤེས་པར་བྱ། མི་འཇིགས་པར་ལྟ་བ་འཇིགས་པར་མི་ལྟ་བ་ཉིད་ཡིན་ནམ་འོན་ཏེ་འཇིགས་པར་མི་ལྟ༌[^589]བ་ཉིད་ཡིན། དེ་ལས་ཅིར་འགྱུར་ཞེ་ན། [^590]གལ་ཏེ་མི་འཇིགས་པར་ལྟ་བ་ཡིན་ན་ནི་ཤེས་རབ་ཡིན་པར་ཤེས་པར་འགྱུར་རོ། །

[Block 1358]
གལ་ཏེ་འཇིགས་པར་མི་ལྟ་བ་ཡིན་ན་ནི་མ་རིག༌[^591]པར་ཤེས་པར་འགྱུར་རོ། །

[Block 1359]
ལྟ་བ་ཡང་ལྟ་བ་ཉིད་མ་ཡིན་ལ་མི་ལྟ་བ་ཡང་མི་ལྟ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1360]
འོ་ན་ཅི་ཞེ་ན། དེ་གཉིས་ཀྱི་རྒྱུ་མཚན་ཉེ་བའི་ཉོན་མོངས་པ་གང་ཡིན་པ་སྟེ། དེ་ནི༌[^592]ཁྲེལ་མེད་པ་ཞེས་བྱའོ། །

[Block 1361]
གཞན་དག་ན་རེ་ནི་བདག་ལ་ལྟོས་ནས་ཉེས་པ་རྣམས་ཀྱིས་མི་འཛེམ་པ་ནི་ངོ་ཚ་མེད་པ་ཡིན་ཏེ།[^593] གཞན་ལ་ལྟོས་ནས་ནི་ཁྲེལ་མེད་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1362]
དེ་ལྟ༌[^594]ན་ཡང་ལྟོས་པ་གཉིས་ཅིག་ཅར་ཇི་ལྟར་འགྲུབ་པར་འགྱུར་ཞེ་ན། བདག་དང་གཞན་ལ་ལྟོས་པ་ཅིག་ཅར་རོ་ཞེས་ནི་མི་ཟེར་རོ། །

[Block 1363]
འོན་ཀྱང་མི་འཛེམ་པ་ཁ་ཅིག་བདག་ལ་ལྟོས་ནས་ཀྱང་འཇུག་པ་ཡོད་པ་གང་ཡིན་པ་དེ་ནི་ངོ་ཚ་མེད་པ་ཡིན་ནོ། །

[Block 1364]
གཞན་ལ་ལྟོས་ནས་འཇུག་པ་ཡོད་པ་གང་ཡིན་པ་དེ་ནི་ཁྲེལ་མེད་པ་ཡིན་ནོ། །

[Block 1365]
བཟློག་པ་ནི་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། རེ་ཞིག་རྟོག་པ་དང་པོ་ལྟར་ན་གུས་པ་དང་བཅས་པ་ཉིད་དེ། བཀུར་བ་དང་བཅས་པ་ཉིད་དང་། འཇིགས་པས་དབང་སྒྱུར་བ་དང་བཅས་པ་ཉིད་ནི་ངོ་ཚ་ཤེས་པ་ཡིན་ལ། ཁ་ན་མ་ཐོ་བ་དག་ལ་འཇིགས་པར་ལྟ་བ་ཉིད་ནི་ཁྲེལ་ཡོད་པ་ཡིན་ནོ། །

[Block 1366]
རྟོག་པ་གཉིས་པ་ལྟར་ན་ནི་བདག་དང་གཞན་ལ་ལྟོས་པ་དག་ལས་འཛེམ་པ་དག་ཡིན་ནོ། །

[Block 1367 [HEADING]]
###### དགའ་བ་དང་གུས་པ། ^2-2-2-3-2-0

[Block 1368]
དགའ་བ་དང་གུས་པ་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག་ཡོད་ཅེ་ན། དགའ་དང་ཞེས་བྱ་བ་སྨོས་ཏེ། དགའ་བ་ནི་རྣམ་པ་གཉིས་ཏེ། ཉོན་མོངས་པ་ཅན་དང་། ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའོ། །

[Block 1369]
དེ་ལ་ཉོན་མོངས་པ་ཅན༌[^595]ནི་སྲིད་པ༌[^596]སྟེ། དཔེར་ན་བུ་དང་ཆུང་མ་ལ་སོགས་པ་དག་ལ་དགའ་བ་ལྟ་བུའོ། །

[Block 1370]
ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ནི་དད་པ་སྟེ། དཔེར་ན་སྟོན་པ་དང་བླ་མ་དང་ཡོན་ཏན་ཅན་རྣམས་ལ་དགའ་བ་ལྟ་བུའོ། །
--- END BLOCKS ---
