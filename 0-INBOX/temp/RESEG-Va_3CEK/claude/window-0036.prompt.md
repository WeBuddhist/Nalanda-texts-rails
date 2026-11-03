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
བསམས་བཞིན་པ༌[^896]ལས་ཇི་ལྟ་བུ་ཞེ་ན། ཆེད་དུ་བསམས་ནས་བྱས་པ་ཡིན་གྱི་བློ་སྔོན་དུ་མ་བཏང་བ་ཡང་མ་ཡིན་ལ་བབ་ཅོལ་དུ་བྱས་པ་ཡང་མ་ཡིན་པའོ། །

[Block 1262]
རྫོགས་པས་ཇི་ལྟ་བུ་ཞེ་ན། ཁ་ཅིག་ནི་ཉེས་པར་སྤྱད་པ་གཅིག་གིས་ངན་སོང་དུ་འགྲོ་ལ། ཁ་ཅིག་ནི་གསུམ་གྱི་བར་གྱིས་འགྲོ་བ་དང་། ཁ་ཅིག་ནི་ལས་ཀྱི་ལམ་གཅིག་གིས་ངན་སོང་དུ་འགྲོ་ལ། ཁ་ཅིག་ནི་བཅུའི་བར་གྱིས་འགྲོ་བ་དེ༌[^897]གང་ཞིག་གིས་ཇི་ཙམ་གྱིས་དེར་འགྲོ་བར་འགྱུར་བ་རྫོགས་པར་མ་བྱས་ན་ཡང་ལས་དེ་བྱས་པ་ཡིན་གྱི་བསགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1263]
རྫོགས་ན་ནི་བསགས་པ་ཡིན་ནོ། །

[Block 1264]
མི་འགྱོད་པ་དང་། གཉེན་པོ་མེད་པས་ཇི་ལྟ་བུ་ཞེ་ན། ལས་དེ་ལ་ཡིད་ལ་གཅགས་པ་མེད་པ་དང་། གཉེན་པོ་མེད་པ་ཡིན་ནོ། །

[Block 1265]
འཁོར་ལས་ཇི་ལྟ་བུ་ཞེ་ན། མི་དགེ་བ་ལ་འཁོར་ཡང་མི་དགེ་བ་མ༌[^898]ཡིན་ནོ། །

[Block 1266]
རྣམ་པར་སྨིན་པ་ལས་ཇི་ལྟ་བུ་ཞེ་ན། རྣམ་པར་སྨིན་པ་འབྱིན་པར་ངེས་པ་ཡིན་ནོ། །

[Block 1267]
དེ་བཞིན་དུ་དགེ་བ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1268]
དེ་ལས་གཞན་དུ་བྱས་པའི་ལས་ནི་མ་བསགས་པ་ཡིན་ནོ། །

[Block 1269 [HEADING]]
##### མཆོད་རྟེན་ལ་སྦྱིན་པ་བྱིན་པའི་བསོད་ནམས། ^1-71-1-9-0

[Block 1270]
འདོད་ཆགས་དང་བཅས་པས་མཆོད་རྟེན་ལ་སྦྱིན་པ་བྱིན་པ་ནི་བདག་གི་དོན་དུའོ་ཞེས་བཤད་པ། དེ་ལ་ལོངས་སྤྱོད་པར་བྱེད་པ་མེད་ན་ཇི་ལྟར་བསོད་ནམས་སུ་འགྱུར་ཞེ་ན། བསོད་ནམས་ནི་རྣམ་པ་གཉིས་ཏེ། བཏང་བའི་རྒྱུ་ལས་བྱུང་བ་ནི་བཏང་བ་ཁོ་ན་ལས་བྱུང་བ་གང་ཡིན་པའོ། །

[Block 1271]
ཡོངས་སུ་ལོངས་སྤྱོད་པ་ལས་བྱུང་བ་ནི་སྦྱིན་པར་བྱ་བའི་ཆོས་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ལས་བྱུང་བ་གང་ཡིན་པའོ། །

[Block 1272]
དེ་ལ་མཆོད་རྟེན་ལ་བཏང་རྒྱུས་བྱུང་བའི་བསོད་ནམས་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་རྒྱུ་ལས་བྱུང་བ་ནི་མེད་དོ། །

[Block 1273]
དེ་ལ་ལེན་པ་སུ་ཡང་མེད་ན་ཇི་ལྟར་བསོད་ནམས་ཡིན་ཞེ་ན། ལེན་པར་བྱེད་པ་ཡོད་ན་ནི་བསོད་ནམས་སུ་འགྱུར་ལ། མེད་ན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་ཡང་རྒྱུ་ཅི་ཞིག་ཡོད། སུ་ལ་ཡང་ཕན༌[^899]བཏགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1274]
འདི་ནི་རྒྱུ་མ་ཡིན་ཏེ། གལ་ཏེ་ཕན་བཏགས་པ་ཁོ་ནས་བསོད་ནམས་སུ་གྱུར༌[^900]ན་ནི། བྱམས་པ་ལ་སོགས་པ་ཚད་མེད་པ་དང་། ཡང་དག་པའི་ལྟ་བ་བསྒོམས་པ༌[^901]རྣམས་བསོད་ནམས༌[^902]སུ་མི་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་མཆོད་རྟེན་ལ་ཡང་བསོད་ནམས་སུ་འདོད་པར་བྱའོ། །

[Block 1275]
ལེན་མེད་བྱམས་སོགས་བཞིན། ཇི་ལྟར་བྱམས་པ་ལ་སོགས་པ་ལ་ལེན་པར་བྱེད་པའམ། གཞན་ལ་ཕན་འདོགས་པར༌[^903]མེད་ཀྱང་རང་གི་སེམས་ཀྱི་མཐུས་བསོད་ནམས་སུ་འགྱུར་བ་དེ་བཞིན་དུ་ཡོན་ཏན་དང་ལྡན་པ་འདས་ཀྱང་དེ་ལ་དད་པ་བྱས་པ་རང་གི་སེམས་ལས་བསོད་ནམས་སུ་འགྱུར་རོ། །

[Block 1276]
འོ་ན་ནི་སྦྱིན་པ་དང་མཆོད་པར༌[^904]བྱ་བ་དོན་མེད་པར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། ལས་དེ་ཀུན་ནས་སློང་བར་བྱེད་པའི་དད་པ་ནི་ཆེས་མཆོག་ཡིན་པའི་ཕྱིར་ཏེ། ཇི་ལྟར་དགྲ་གསད་པའི་བསམ་པ་ཅན་དེས་ཀུན་ནས་བསླང་བའི་ལུས་དང་ངག་གི་ལས་དེ་ཤི་བཞིན་དུ་དགྲའི་འདུ་ཤེས་ཀྱིས་བྱེད་ན་བསོད་ནམས་མ་ཡིན་པ་ཆེས་མང་དུ་སྐྱེ་བར་འགྱུར་གྱི་བསམས་པ༌[^905]ཙམ་གྱིས་ནི་མ་ཡིན་པ་དེ་བཞིན་དུ། སྟོན་པ་འདས་ཀྱང་དེ་ལ་དད་པས་ཀུན་ནས་བསླང་བའི་སྦྱིན་པ་དང་མཆོད་པའི་བྱ་བ་བྱེད་ན་བསོད་ནམས་ཆེས་མང་དུ་སྐྱེ་བར་འགྱུར་གྱི་དད་པ་ཙམ་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 1277 [HEADING]]
##### ངན་པའི་ཞིང་ལ་འབྲས་བུ་ཡིད་འོང་བ། ^1-71-1-10-0

[Block 1278]
གལ་ཏེ་ཞིང་བཟང་པོ་ལ་སྦྱིན་པར་བྱ་བའི་ས་བོན་འབྲས་བུ་ཡིད་དུ་འོང་བ་ཅན་ཡིན་ནོ། །

[Block 1279]
[^906]འོ་ན་ཞིང་ངན་པ་ལ་བྱིན་ན་འབྲས་བུ་ཡིད་དུ༌[^907]འོང་བར་འགྱུར་རོ་ཞེ་ན།

[Block 1280 [VERSE]]
རྒྱུ་ལས་འབྲས་བུ་མི་འཁྲུལ་ཕྱིར། །
ངན་པའི་ཞིང་ལའང་འབྲས་ཡིད་འོང་། །

[Block 1281]
ཞིང་ངན་པ་ལ་ཡང་ས་བོན་ལས་འབྲས་བུ་མི་འཁྲུལ་བ་མཐོང་སྟེ། རྒུན་འབྲུམ༌[^908]གྱི་ས་བོན་ལས་ནི་རྒུན་འབྲུམ༌[^909]གྱི་འབྲས་བུ་མངར་བ་ཁོ་ན་སྐྱེ་ལ། ནིམ་པའི་ས་བོན་ལས་ནི་ནིམ་པའི་འབྲས་བུ་ཁ་བ༌[^910]ཁོ་ན་སྐྱེའོ། །

[Block 1282]
དེ་བཞིན་དུ་ཞིང་ངན་པ་ལ་ཡང་གཞན་ལ་ཕན་པའི་ལྷག་པའི་བསམ་པ་ལ་ཞུགས་པའི་སྦྱིན་པའི་ས་བོན་གྱི་འབྲས་བུ་ཡང་ཡིད་དུ་འོང་བ་ཁོ་ན་འགྲུབ་ཀྱི་ཡིད་དུ་མི་འོང་བ་ནི་མ་ཡིན་ནོ། །

[Block 1283]
ཞིང་གི་སྐྱོན་གྱིས་ནི་ས་བོན་དེའི་འབྲས་བུ་ཆུང་བའམ། འབྲས་བུ་མེད་པར་འགྱུར་རོ། །

[Block 1284]
སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་གཞི་ཞར་ལ་འོངས་པ་དང་བཅས་ཏེ་རྫོགས་སོ།། །།

[Block 1285 [HEADING]]
#### ཚུལ་ཁྲིམས་ལས་བྱུང་བ། ^1-71-2-0

[Block 1286 [HEADING]]
##### ཚུལ་ཁྲིམས་མདོར་བཤད་པ། ^1-71-2-1-0

[Block 1287]
ཚུལ་ཁྲིམས་ལས་བྱུང་བ་བརྗོད་པར་བྱ་སྟེ། དེས༌[^911]སྨྲས་པ། འཆལ་པའི་ཚུལ་ཁྲིམས་མི་དགེའི་གཟུགས། །དེ་སྤང་ཚུལ་ཁྲིམས། གཟུགས་མི་དགེ་བ་ནི་འཆལ་པའི་ཚུལ་ཁྲིམས་ཞེས་བྱའོ། །

[Block 1288]
དེ་སྤོང་བ་ནི་ཚུལ་ཁྲིམས་ཡིན་ནོ། །

[Block 1289]
སྤོང་བ་དེ་ཡང་རྣམ་པ༌[^912]གཉིས་སོ། །

[Block 1290]
རྣམ་པར་རིག་བྱེད་གང་གིས་སྤོང་བར་བྱེད་པ་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྤོང་བ་གང་ཡིན་པའོ། །

[Block 1291]
ཚུལ་ཁྲིམས་ནི༌[^913]འཆལ་པའི་ཚུལ་ཁྲིམས་ལས་སྤོང་བ་འབའ་ཞིག་ཀྱང་མ་ཡིན་ནོ། །

[Block 1292]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། སངས་རྒྱས་ཀྱིས་ནི་བཅད་པ་ཡང་། །རང་བཞིན་གྱིས་འཆལ་པའི་ཚུལ་ཁྲིམས་མ་ཡིན་ཡང་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་བཅད་པ་དུས་མ་ཡིན་པའི་ཟས་ལ་སོགས་པ་གང་དག་ཡིན་པ་དེ་དག་སྤོང་བ་རྣམ་པ་གཉིས་ཀྱང་ཚུལ་ཁྲིམས་ཡིན་ཏེ། སླབ་པ༌[^914]མནོས་པས་དེ་དག་སྤྱད་ན་འཆལ་པའི་ཚུལ་ཁྲིམས་སུ་འགྱུར་རོ། །

[Block 1293]
ཚུལ་ཁྲིམས་མདོར་བཤད་ཟིན་ཏོ། །

[Block 1294 [HEADING]]
##### རྣམ་པར་དག་པའི་ཚུལ་ཁྲིམས། ^1-71-2-2-0

[Block 1295]
རྣམ་དག་ཡོན་ཏན་བཞི་ལྡན་ནོ། །

[Block 1296]
ཡོན་ཏན་བཞི་དང་ལྡན་པའི་ཚུལ་ཁྲིམས་དེ་ནི་རྣམ་པར་དག་པ་ཡིན་ནོ། །

[Block 1297]
བཟློག་པ་ནི་རྣམ་པར་མ་དག་པ་ཡིན་ནོ། །ཇི་ལྟར་ན་ཡོན་ཏན་བཞི་དང་ལྡན་པ་ཡིན་ཞེ་ན། ཚུལ༌[^915]ཁྲིམས་དེ་རྒྱུས་འཕེན་མ་བྱུང་།[^916] །དེ་ཡི་གཉེན་པོ་ཞི་ལ་བརྟེན།[^917] །རེ་ཞིག་འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱིས་འཕེན་མ་བྱུང་བ་ནི་ཇི་སྐད་དུ་བཤད་པས་འཕེན་མ་བྱུང་བ་ཡིན་ནོ། །

[Block 1298]
འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱི་རྒྱུས་འཕེན་མ་བྱུང་བ་ནི་ཆགས་པ་ལ་སོགས་པ་ཉོན་མོངས་པ་དང་། ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་ཀྱིས་འཕེན་མ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 1299]
འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱི་གཉེན་པོ་ལ་བརྟེན་པ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་བརྟེན་པའི༌[^918]ཕྱིར་རོ། །

[Block 1300]
ཞི་བ་ལ་བརྟེན་པ༌[^919]ནི་སྐྱེ་བའི་ཁྱད་པར་ལ་མི་བརྟེན་གྱི་མྱ་ངན་ལས་འདས་པར་ཡོངས་སུ་བསྔོས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
