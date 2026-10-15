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
མིག་དམད་པ་དང་ཁྱིམ་པ་རྣམས་ལ་ཆོས་དང་ལྡན་པའི་གཏམ་བྱའོ་ཞེས་བྱ་བ་ལ། མིག་དམད་པ་ཞེས་བྱ་བ་ནི་ཡུལ་རྣམས་ལས་ཏེ། མིག་སོ་སོར་དམད་པར་བྱས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1262]
ཁྱིམ་པ་རྣམས་ལ་ཆོས་དང་ལྡན་པའི་གཏམ་བྱའོ། །

[Block 1263]
སྦྱིན་པ་དང་དུལ་བ་དང་ཡང་དག་པར་སྡོམ་པ་དང་ཚངས་པར་སྤྱོད་པ་ལ་གནས་པ་དང་གསོ་སྦྱོང་དང་སྐྱབས་སུ་འགྲོ་བ་དང་བསླབ་པའི་གཞི་གཟུང་བ་དག་ལ་དེ་རྣམས་ངེས་པར་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་རྣམས་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་རྣམས་སོ། །

[Block 1264]
དུལ་བ་ནི་དབང་དུ་བྱེད་པ་སྟེ། དབང་པོ་རྣམས་དང་ལུས་དང་ངག་དག་ལ་དབང་དུ་བྱེད་པ་ཉིད་དོ། །

[Block 1265]
ཡང་དག་པར་སྡོམ་པ་ནི་འདི་རྣམས་ལ་འགྲོ་བ་མེད་པ་སྟེ། འདུལ་བ་དང་འདུལ་བ་ཉིད་ལ་གནས་པའོ། །

[Block 1266]
ཚངས་པར་སྤྱོད་པ་ལ་གནས་པ་དང་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བའི་ཚུལ་ཁྲིམས་དང་ཁྱིམ་པ་ཉིད་ལ་ཡང་ཇི་སྲིད་འཚོའི་བར་དུ་གྲོང་བའི་ཆོས་ལས་ཕྱིར་བཟློག་པར་བྱའོ། །

[Block 1267]
[^893]ལྟུང་བའི་སྒོར་གྱུར་པའི་འཇུག་པ་ཐམས་ཅད་ལ་དྲན་པས་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དྲན་པས་ཞེས་བྱ་བ་ནི་ལྟུང་བ་རྣམས་ལ་ཞེས་བྱ་བའི་དོན་གྱིས་གོ་བས་ཁྱིམ་དུ་འཇུག་པ་ལ་སོགས་པ༌[^894]འགྲོ་བ་ལ་སོགས་པ་འཇུག་པ་ལྟུང་བ་ལས་འདའ་བའི་སྒོར༌[^895]གྱུར་པ་གང་ཡིན་པ་དེ་ལ་དེ་ལྟར་དྲན་པ་ཉེ་བར་གནས་པར་བྱས་ནས་ཇི་ལྟར་ཅུང་ཟད་ལྟུང་བར་མི་འགྱུར་རོ། །

[Block 1268]
རྗེས་སུ་འགྲོ་བ་བསླབས་པས༌[^896]མི་བྱའོ་ཞེས་བྱ་བ་ནི་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 1269]
འདི་ནི་རྗེས་སུ་བསྟན་པ་དང་རྗེས་སུ་འབྲེལ་བ་མ་ཡིན་ཏེ། དེ་བས༌[^897]ན་བསྒྲུབ་པར་མི་བྱ་སྟེ། འདིའི་རྗེས་སུ་བསྟན་པ་འདའ་བར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1270]
འོངས་པ་ལ་འོངས་པ་ལེགས་སོ་ཞེས་སྔར་སྙན་པ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། འོངས་པ་ལ་འོངས་པ་ལེགས་སོ་ཞེས་བྱ་བ་ནི་ལེགས་པར་འོངས་པ་སྨྲ་བ་ལས་བསྙེན་པར༌[^898]བརྗོད་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1271]
འོངས་པ་ལ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བའམ་ཁྱིམ་པ་ལའོ། །

[Block 1272]
བཞིན་གྱི༌[^899]མདངས་གསལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ངོམ་ཟུམ་མི་བྱའོ། །

[Block 1273]
འཛུམ་པ་སྔར་བྱའོ་ཞེས་བྱ་བ་ནི་འཛུམ་པ་ཐོག་མར་འགྲོ་བ་སྟེ། མངོན་དུ་ཕྱོགས་པ་སྟེར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1274]
བར་དང་བཅས་པའི་འཇུག་པ་ཡང་འཛུམ་པ་དང་བཅས་པ་ཉིད་དུ་འགྱུར་རོ་ཞེ་ན། དེའི་ཕྱིར་ཁྲོ་གཉེར་མེད་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1275]
གལ་ཏེ་ཁྱིམ་པ་ཞིག་ཡིན་ན་དེ་ལ་ཆོས་དང་ལྡན་པའི་གཏམ་བྱའོ། །

[Block 1276]
གྲོང་མཐའ་བས་ནི་དེར་མི་འོང་ན་ཀུན་དགའ་བར་འགྱུར་བ་ཅི་ནུས་པས་ལྷུག་པར༌[^900]བྱའོ། །

[Block 1277]
མི་འོང་ན་ཞེས་བྱ་བ་ལ་མི་འོང་ན་ནི་ཁྱིམ་པའོ། །

[Block 1278]
གྲོང་མཐའ་བས་ནི་དགེ་སློང་ངོ་། །ཀུན་དགའ༌[^901]བར་འགྱུར་བ་ནི་བཟའ་བ་ལ་སོགས་པའོ། །

[Block 1279]
ཅི་ནུས་པས་ལྷུག་པར༌[^902]བྱའོ། །

[Block 1280]
ཆུ་དང་སྟན་བསྟབས༌[^903]པར་བྱའོ་ཞེས་བྱ་བ་ལ། དགོན་པ་བས་ཀྱང་ཆུ་དང་སྟན་དང་ཞེས་བྱ་བར་བསྡུ་བའོ། །

[Block 1281]
ཕྱག་དར་དང་མལ་དང་སྟན་བཤམ་པ་དང་ཆུ་གཞག་པ་དང་བྲིམ་པ༌[^904]དང་ཟན་དྲང་བ་ནི་གསར་བུས་བྱའོ་ཞེས་བྱ་བ་ནི་གང་དེ་ཡང་དག་པར་འོངས་པ་ལ་འདི་ཐམས་ཅད་གསར་དུ༌[^905]ཞུགས་པ་དེས་བྱའོ། །

[Block 1282]
གཡོག་འཁོར་གྱི་བྱ་བ་མི་མཐུན་པ་གལ་ཏེ་རང་དང་གཞན་ལ་གནོད་པར་མི་འགྱུར་བ་ནི་ཅི་བདེར་གཞག་གོ་ཞེས་བྱ་བ་ལ། ཅི་བདེར་གཞག་གོ་ཞེས་བྱ་བ་ནི་བཏང་སྙོམས་སུ་གཞག་པར་བྱ་བའོ།[^906] །གལ་ཏེ་ཁས་བླངས་པར་གྱུར་པ་ཡིན་ན་རང་དང་གཞན་རྣམས་ལ་གནོད་པར་མི་འགྱུར་རོ། །

[Block 1283]
གལ་ཏེ་དེ་ལྟ་ཡིན་ན་ཞེས་བྱ་བ་ནི་གལ་ཏེ་འཁོར་གྱི་བྱ་བ་དེ་གནོད་པའི་ཕྱིར་ཡིན་ལ་ནུས་པ་ཡོད་ན་དེ་རྒྱུན་བཅད་ལ་ཞེས་བྱ་བ་ནི་མི་མཐུན་པའི་བྱ་བ་གཞན་ནོ། །

[Block 1284]
ཆོས་དང་ལྡན་པ་ནི་བྱ་བའོ། །

[Block 1285]
བསྐྱེད་ནས་དེ་གཡོག་འཁོར་ལ་གྲོས་གདབ་པར་བྱའོ། །

[Block 1286]
དེའི་གཞི་ལས་གཡོག་འཁོར་མི་དགའ་ཞིང་འཕོ་བ་ལྟ་ན་ཕྱིར་བསྡུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཆོས་དང་ལྡན་པའི་བྱ་བ་སྐྱེད་པར་འགྱུར་བ༌[^907]ལ་གཡོག་འཁོར་དེ་ལ་གལ་ཏེ་སེམས་མི་དགའ་ཞིང་ཡིད་མི་བདེ་བར་གྱུར་ཏམ། ནད་མེད་པའམ་གཞན་གྱིས་འགྲོ་བར་བྱ་ཞིང་དེ་ལ་སོ་སོར་འདུ་བྱེད་པའོ། །

[Block 1287]
དེ་བཞིན་དུ་སྦྱིན་པ་ལ་སོགས་པས་སོ་སོར་བསྡུ་བར་བྱའོ། །

[Block 1288]
གཡོག་འཁོར་ཇི་ལྟ་བ་འདི་ལ་གཉིས་སུ་ཡང་མི་འགྱུར་བར་ཞེས་བྱ་བའོ།

[Block 1289]
[^908] །མི་ནུས་པ་ཉིད་ཡིན་ན་ཡང་གཞན་དུ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་རྒྱུན་གཅད་པར༌[^909]མི་ནུས་པ་ཉིད་ལ་གཞན་དུ་འགྲོ་བར་བྱའོ། །

[Block 1290]
དེའི་རྐྱེན་གྱིས་རྩོད་ཅིང་སྨྲ་བར་མི་བྱའོ། །

[Block 1291]
དགེ་འདུན་གྱི་ཀུན་དགའ་ར་བར་གནོད་པ་བྱེད་ན་ཅི་ནས་ཀྱང་དེ་ཉིད་འཛིན་དུ་གཞུག་པའི་ཕྱིར་འཛིན་པ་གཏང་བ༌[^910]དེ་ལྟར་བྱའོ། །

[Block 1292]
མི་འགྲོ་ན་བབ་ཅོལ་དུ་སུ་ལ་ཡང་མི་བརྗོད་པར་གཞོན་ནུ་དང་མཛའ་བཤེས་དང་ཞང་བློན་དང་ཞབས་འབྲིང་དག་ལ་སྐད་སྦྱར་ཏེ། འཁོར་དག་པར་འཛིན་དུ་བཅུག་ནས་ཐུལ་འོག་ཏུ་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། འཛིན་དུ་བཅུག་ནས་ཞེས་བྱ་བ་ནི་གོ་བར་བྱས་ནས་སོ། །

[Block 1293]
འཁོར་དག་པ་ནི་གང་དུ་འདི་ལ་ཆད་པ་མི་དབབ་པ་དེར་འཇུག་པར་བྱ་བ་ནི་ཕམ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1294]
གཞོན་ནུ་ལ་སོགས་པ་རྣམས་ལ་གང་ཞིག་སྔར་གོ་བར་བྱེད་པ་དེ་ནི་འདིའི་དོན་དུ་སྟེ། ཕམ་པར་གྱུར་པ་དེ་ལ་བརྟན༌[^911]ནས་གཅོད་པར༌[^912]མ་གྱུར་ཅིག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1295]
རབ་ཏུ་བྱུང་བའི་གཞི་ལས།

[Block 1296]
དགེ་སློང་དང་འབྲེལ་བའི་སྐབས་བཤད་ཟིན་ཏོ།། །།

[Block 1297]
ད་ནི་དགེ་སློང་མ་ལ་བརྟེན་པ་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་སྐྱེས་པ་རབ་ཏུ་འབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་ལ་བརྗོད་པ་གང་ཞིག་དེ་ཉིད་བུད་མེད་ལ་ཡང་ཞེས་བྱ་བ་ཁས་བླང་ངོ་། །བྱེ་བྲག་ཏུ་ནི་འདི་བརྗོད་པར་བྱ་སྟེ། དགེ་སློང་གི༌[^913]གནས་སུ་དགེ་སློང་མའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་ཕྱོགས་གཅིག༌[^914]ཏུ་གྱུར་པའམ་གཅིག་པོར་གྱུར་པའི་མཁན་པོ་དང་ཞུ་བ་པོ་ལ་སོགས་པ་གང་དུ་དགེ་སློང་སྨོས་པ་དེར་དགེ་སློང་མ་བལྟ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1298]
ཅི་དགེ་སློང་ཐམས་ཅད་ཀྱི་གནས་སུ་ཡིན་ནམ་འོན་ཏེ་འགའ་ཞིག་ལ་ཞེ་ན། དེའི་ཕྱིར་རབ་ཏུ་བྱུང་བ་ཐམས་ཅད་ཀྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་བྱུང་བའི་ཡུལ་ལ་མཁན་པོ་ལ་སོགས་པའི་དགེ་སློང་ཐམས་ཅད་ཀྱི་གནས་སུ་དགེ་སློང་མ་ཤེས་པར་བྱའོ། །

[Block 1299]
མཁན་པོ་ཉིད་ཀྱི་དོན་དུ་ཞུ་བ་བྱེད་པ་དང་དགེ་ཚུལ་མའི་སྡོམ་པ་སྦྱིན་པ་ཞེས་བྱ་བ་འདི་ཐམས་ཅད་དགེ་སློང་མ་རྣམས་ཀྱིས་བསྒྲུབ་པར་བྱའོ། །

[Block 1300]
འདིར་དགེ་སློང་ལ་དབང་དུ་བྱ་བ་མེད་དོ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུའོ། །
--- END BLOCKS ---
