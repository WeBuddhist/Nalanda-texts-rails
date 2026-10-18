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
བརྩོན་འགྲུས་ནི་སེམས་མངོན་པར་སྤྲོ་བའོ། །

[Block 1262]
དགེ་བའི་ས་མང་པོ་པ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 1263]
ས་མང་པོ་ནི་ས་མང་བ་ཡིན་ནོ། །

[Block 1264 [HEADING]]
###### ཉོན་མོངས་པའི་ས་མང་པོ་པ། ^2-2-2-1-3-0

[Block 1265]
འདི་དག་ལ་ཉོན་མོངས་པའི་ས་མང་པོ་ཡོད་པས། འདི་དག་ནི་ཉོན་མོངས་པའི་ས་མང་པོ་པ་དག་ཡིན་ཏེ། ཆོས་གང་དག་ཉོན་མོངས་པ་ཅན་གྱི་སེམས་ལ་རྟག་ཏུ་འབྱུང་བ་ཡིན་ནོ། །

[Block 1266]
ཉོན་མོངས་པ་ཅན་གྱི་སེམས་ལ་རྟག་ཏུ་འབྱུང་བ་དེ་དག་ཀྱང་གང་ཞེ་ན།

[Block 1267 [VERSE]]
རྨོངས་དང་བག་མེད་ལེ་ལོ་དང་། །
མ་དད་པ་དང་རྨུགས་དང་རྒོད། །
ཉོན་མོངས་ཅན་ལ་རྟག་ཏུ་འབྱུང་། །

[Block 1268]
དེ་ལ་རྨོངས་པ་ཞེས་བྱ་བ་ནི་མ་རིག་པ་སྟེ། མི་ཤེས་པ་དང་མི་གསལ་བའོ། །

[Block 1269]
བག་མེད་པ་ནི་དགེ་བའི་ཆོས་རྣམས་མི་བསྒོམ་པ༌[^550]སྟེ། བསྒོམ་པའི་མི་མཐུན་པའི༌[^551]ཕྱོགས་ཀྱི་ཆོས་སོ། །

[Block 1270]
ལེ་ལོ་ནི་སེམས་མངོན་པར་མི་སྤྲོ་བ་སྟེ། བརྩོན་འགྲུས་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་སོ། །

[Block 1271]
མ་དད་པ་ནི་སེམས་མ་དད་པ་སྟེ། དད་པའི་མི་མཐུན་པའི་ཕྱོགས་སོ། །

[Block 1272]
རྨུགས་པ་གང་ཞེ་ན། ལུས་ལྕི་བ་ཉིད་དང་། སེམས་ལྕི་བ་ཉིད་དང་།[^552] ལུས་ལས་སུ་མི་རུང་བ་ཉིད་དང་། སེམས་ལས་སུ་མི་རུང་བ་ཉིད་གང་ཡིན་པའོ། །

[Block 1273]
ཆོས་མངོན་པ་ལས་ལུས་ཀྱི་རྨུགས་པ་དང་། སེམས་ཀྱི་རྨུགས་པ་ཞེས་བཤད་པ་ཇི་ལྟར་ན་སེམས་ལས་བྱུང་བའི་ཆོས་ལུས་ཀྱི་ཞེས་བྱ་ཞེ་ན། ལུས་ཀྱི་ཚོར་བ་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 1274]
རྒོད་པ་ནི་སེམས་རྣམ་པར་མ་ཞི་བ་སྟེ། དེ་ལྟར་ན་དྲུག་པོ་འདི་དག་ནི་ཉོན་མོངས་པའི་ས་མང་པོ་པ་དག་ཡིན་ནོ། །

[Block 1275]
ཆོས་མངོན་པ་ལས།

[Block 1276]
ཉོན་མོངས་པའི་ས་མང་པོ་པ་བཅུ་པོ་འདི་དག༌[^553]མ་ཡིན་ནམ། དེ་ལས་རྨུགས་པ་མི་འབྱུང་སྟེ། མ་དད་པ་དང་། ལེ་ལོ་དང་། བརྗེད་ངས་པ་དང་། སེམས་རྣམ་པར་གཡེང་བ་དང་། མ་རིག་པ་དང་། ཤེས་བཞིན་མ་ཡིན་པ་དང་། ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་དང་། ལོག་པར་མོས་པ་དང་། རྒོད་པ་དང་། བག་མེད་པའོ་ཞེས་འབྱུང་ངོ་ཞེ་ན། འགྱུར་བ་ཤེས་པ་ནི་ལྷ་རྣམས་དགའ་བ་ཡིན་གྱི། འདོད་པ་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1277]
འདི་ལ་འདོད་པ་གང་ཡིན་ཞེ་ན། བརྗེད་ངས་པ་དང་། རྣམ་པར་གཡེང་བ་དང་། ཤེས་བཞིན་མ་ཡིན་པ་དང་། ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་དང་། ལོག་པར་མོས་པ་རྣམས་ནི་ས་མང་པོ་པ་ཡིན་པའི་ཕྱིར། དཔེར་ན་གཏི་མུག་མེད་པ་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་དེ་དགེ་བའི་ས་མང་པོ་པར་ངེས་པར་མ་བཟུང་བ༌[^554]ལྟར་ཉོན་མོངས་པའི་ས་མང་པོ་པ་དག་ཁོ་ན་ཡིན་པར་ངེས་པར་མི་བཟུང༌[^555]སྟེ། དྲན་པ་ཉོན་མོངས་པ་ཅན་ཁོ་ན་བརྗེད་ངས་པ་ཡིན་ལ། ཏིང་ངེ་འཛིན་ཉོན་མོངས་པ་ཅན་ཁོ་ན་རྣམ་པར་གཡེང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 1278]
དེ་ཉིད་ཀྱི་ཕྱིར་གང་དག་ས་མང་པོ་པ་ཡིན་པ་དེ་དག་ཉོན་མོངས་པའི་ས་མང་པོ་པ་ཡང་ཡིན་ནམ་ཞེ་ན། མུ་བཞི་སྟེ། མུ་དང་པོ་ནི་ཚོར་བ་དང་། འདུ་ཤེས་དང་། སེམས་པ་དང་། འདུན་པ་དང་། རེག་པའོ། །

[Block 1279]
གཉིས་པ་ནི་མ་དད་པ་དང་། ལེ་ལོ་དང་། མ་རིག་པ་དང་། རྒོད་པ་དང་། བག་མེད་པའོ། །

[Block 1280]
གསུམ་པ་ནི་དྲན་པ་ལ་སོགས་པ་ཉོན་མོངས་པ་ཅན་ལྔ་ཇི་སྐད་བཤད་པ་རྣམས་སོ། །

[Block 1281]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ་ཞེས་འབྱུང་ངོ་། །

[Block 1282]
ཁ་ཅིག་ནི་སེམས་རྣམ་པར་གཡེང་བ་ལོག་པའི་ཏིང་ངེ༌[^556]འཛིན་ལས་གཞན་དུ་འདོད་དེ། དེ་དག་གི་མུ་བཞི་པ༌[^557]ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 1283]
རྨུགས་པ་ནི་ཉོན་མོངས་པ་ཐམས་ཅད་དང་མཚུངས་པར་ལྡན་པར་འདོད་པ་དེ་ཉོན་མོངས་པའི་ས་མང་པོ་པ་དག་ཏུ་མ་བཏོན་པ་སུ་ཞིག་གིས་ཉེས། འདི་སྐད་དུ་གདོན་པར་བྱ་བ་ནི་ཡིན་མོད་ཀྱི་ཏིང་ངེ་འཛིན་དང་མཐུན་པའི་ཕྱིར་མ་བཏོན་ཏེ།[^558] རྨུགས་པ་སྤྱོད་པ༌[^559]ནི་ཏིང་ངེ་འཛིན་ཤིན་ཏུ་མྱུར་དུ་སྐྱེད་པར་འགྱུར་གྱི་རྒོད་པ་སྤྱོད་པ་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 1284]
གང་ཞིག་རྒོད་པ་མི་སྤྱོད་ལ་རྨུགས་པ་སྤྱོད་པ་ཡང་སུ་ཞིག་ཡོད། ཡང་ན་གང་ཞིག་རྨུགས་པ་མི་སྤྱོད་ལ་རྒོད་པ་སྤྱོད་པ་ཡང་སུ་ཞིག་ཡོད་དེ། འདི་དག་ནི་ནམ་དུ་ཡང་ལྷན་ཅིག་སྤྱོད་པ་ཉིད་འདོར་བར་མི་འགྱུར་མོད་ཀྱི། འོན་ཀྱང་གང་ཞིག༌[^560]གང་ལ་ཤས་ཆེ་བ་དེ་ནི་སྤྱོད་པར་ཤེས་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཉོན་མོངས་པའི་ས་ཆེན་པོ་པ་ནི་དྲུག་པོ་ཁོ་ནར་འགྲུབ་བོ། །

[Block 1285]
དེ་དག་ཀྱང་རྟག་ཏུ་ཉོན་མོངས་པ་ཅན་གྱི༌[^561]སེམས་ཁོ་ན་ལ་འབྱུང་གི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1286 [HEADING]]
###### མི་དགེ་བའི་ས་མང་པོ་པ། ^2-2-2-1-4-0

[Block 1287]
མི་དགེ་ལ་ནི་ཁྲེལ་མེད་དང་། །ངོ་ཚ་མེད་པའོ། །

[Block 1288]
ངོ་ཚ་མེད་པ་དང་ཁྲེལ་མེད་པ་ནི༌[^562]མི་དགེ་བའི་སེམས་ལ་རྟག་ཏུ་འབྱུང་བས་ཆོས་འདི་ཉིད༌[^563]ནི་མི་དགེ་བའི་ས་ཆེན་པོ་པ་དག་ཅེས་བྱའོ། །

[Block 1289]
དེ་གཉིས་ཀྱི་མཚན་ཉིད་ནི་འོག་ནས་འཆད་དོ། །

[Block 1290 [HEADING]]
###### ཉོན་མོངས་པ་ཆུང་ངུའི་ས་པ། ^2-2-2-1-5-0

[Block 1291]
ཁྲོ་བ་དང་།

[Block 1292 [VERSE]]
ཁོན་དུ་འཛིན་དང་གཡོ་དང་ནི། །
ཕྲག་དོག་འཚིག་འཆབ་སེར་སྣ་དང་། །
སྒྱུ་དང་རྒྱགས་དང་རྣམ་འཚེ་ནི། །
ཉོན་མོངས་ཆུང་ངུའི་ས་པ་རྣམས། །

[Block 1293]
[^564]འདི་དག་ལ་ཉོན་མོངས་པ་ཆུང་ངུའི་ས་ཡོད་པས་འདི་ནི་ཉོན་མོངས་པ་ཆུང་ངུའི་ས་པ་རྣམས་ཏེ། མ་རིག་པ་ཙམ་དང་བསྒོམས་པས་སྤང་བར་བྱ་བ་དང་། ཡིད་ཀྱི་ས་པ་ཁོ་ན་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1294]
འདི་དག་ནི་ཉེ་བའི་ཉོན་མོངས་པ་དག་གི་ནང་ནས་སྟོན་པར་འགྱུར་རོ། །

[Block 1295]
སེམས་ལས་བྱུང་བ་རྣམ་པ་ལྔ་པོ་དེ་དག་བཤད་ཟིན་ཏོ། །

[Block 1296 [HEADING]]
##### ས་གང་ན་སེམས་གང་ལ་སེམས་ལས་བྱུང་བ་ཇི་སྙེད་ཅིག་འབྱུང་བ། ^2-2-2-2-0

[Block 1297 [HEADING]]
###### འདོད་པ་ན་སྤྱོད་པའི་སེམས། ^2-2-2-2-1-0

[Block 1298]
རྟོག་པ་དང་དཔྱོད་པ༌[^565]དང་འགྱོད་པ་དང་གཉིད་ལ་སོགས་པ་མ་ངེས་པ་གཞན་དག་ཀྱང་ཡོད་པས། དེ་ལ་སེམས་གང་ཞིག་ལ་སེམས་ལས་བྱུང་བ་དུ་ཞིག་གདོན་མི་ཟ་བར་འབྱུང་བ་བརྗོད་པར་བྱ་སྟེ། རེ་ཞིག་འདོད་པ་ན་སྤྱོད་པའི་སེམས་ནི་རྣམ་པ་ལྔ་སྟེ། དགེ་བ་དང་མི་དགེ་བ་རྣམ་པ་གཉིས་ཏེ། མ་འདྲེས་པ་དང་། ཉོན་མོངས་པ་གཞན་དང་མཚུངས་པར་ལྡན་པ་དང་། ལུང་དུ་མ་བསྟན་པ་རྣམ་པ་གཉིས་ཏེ། བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དང་། མ་བསྒྲིབས་པ༌[^566]ལ་ལུང་དུ་མ་བསྟན་པའོ། །

[Block 1299]
དེ་ལ་རེ་ཞིག་འདོད་པ་ན་སྤྱོད་པའི་སེམས་ནི་ངེས་པར་རྟོག་པ་དང་དཔྱོད་པ་དང་བཅས་པ་ཡིན་པས་དེའི་ཕྱིར་འདི་ལ།

[Block 1300 [HEADING]]
###### **དགེ་བ།** ^2-2-2-2-1-1-0
--- END BLOCKS ---
