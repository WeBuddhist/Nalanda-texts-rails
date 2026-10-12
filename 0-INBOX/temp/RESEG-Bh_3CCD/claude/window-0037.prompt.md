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
[Block 1296]
གཉིས་པ་ལ་མ་ཡིན་ནོ། །

[Block 1297]
དེའི༌[^921]ཕྱིར་མི་རྟོག་པའི་བདག་ཉིད་མངོན་སུམ་གྱི་ནི་དེ་ཡུལ་མ་ཡིན་ནོ། །

[Block 1298]
གང་གི་ཡུལ་ཡིན་པ་དེ་ནི་ཚད་མ་མ་ཡིན་ནོ་ཞེས་ཚངས་པ་ཉིད་ལ་ཡོད་པ་ལ་མངོན་སུམ་མི་འཇུག་གོ། །

[Block 1299]
རྗེས་སུ་དཔག་པ་ཡང་དེ་བཞིན་ཏེ་གང་གི་ཕྱིར་རྗེས་སུ་དཔག་པ་ནི་རྟགས་དང་རྟགས༌[^922]ཅན་གྱི་འབྲེལ་པ་སྔོན་དུ་འགྲོ་བར་འཇུག་པར༌[^923]འགྱུར་ཏེ། དུ་བ་དང་མེ་བཞིན་ནོ། །

[Block 1300]
ཚངས་པ་དེའི་འབྲས་བུར་གྱུར་པའི་རྟགས་གང་ཡང་མ༌[^924]མཐོང་སྟེ། གང་གིས་དེ་མཐོང་བ་མེད་པར་མི་འབྱུང་བས་རྟགས་ཅན་དུ་གྱུར་པ་ཚངས་པ་ཉིད་དཔག་པར་བྱའོ། །

[Block 1301]
དངོས་པོ་ཐམས་ཅད་དེ་ལས་འབྱུང་བ་ཡིན་ཞེས་འབྲས་བུ་མཐོང་བས་དེ་དཔག་པར་བྱ་ཞེ་ན། དེ་ཡང་མི་རིགས་ཏེ། གང་འབྲས་བུ་སྐྱེད་པར་བྱེད་པ་དེ་ནི་རྒྱུ་ཉིད་དེ། འབྲས་བུ་བྱུང་བས་དེ་འཇིག་པར་འགྱུར་བས་རྟག་པ་མ་ཡིན་ནོ། །

[Block 1302]
ཚངས་པ་ཉིད་ཀྱི་ཚུལ་ནི་ཁྱེད་ཅག་གི་ཕྱོགས་སུ་རྟག་པར་འདོད་པ་མ་ཡིན་ནམ། རེ་ཞིག་རྒྱུ་ཉིད་དུ་འདོད་ན་ཡང་། རང་དང་འདྲ་བའི་འབྲས་བུ་ཅིའི་ཕྱིར་མི་སྐྱེད་ཕྱིན་ཅི་ལོག་པར་སྐྱེད་པ་ལ་རིགས་པ་མ༌[^925]མཐོང་ངོ་། །དཔེར་ན་ལྷ་ལ་སོགས་པ་ཁ་ཅིག་བདེ་བར་གྱུར་པ་དང་། ཡི་དགས་ལ་སོགས་པ་ཁ་ཅིག་སྡུག་བསྔལ་ཅན་དུ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1303]
དེའི་སྣ་ཚོགས་པ་ཉིད་དེ༌[^926]ལྟ་བུ་ཡོད་ཅེ་ན། སྨྲས་པ་སྣ་ཚོགས་པ་ཉིད་ནི་དེ་དང་ཐ་དད་པ་ཡིན་ནམ། ཐ་མི་དད་པ་ཡིན། ཐ་དད་པ་ཡིན་ན༌[^927]ཚངས་པ་དེ༌[^928]ཉིད་ཀྱིས་དེར་མི་འགྱུར་རོ། །

[Block 1304]
དབྱེར་མེད་པས་དེའི་བདག་ཉིད་དུ་གྱུར་པའི་ངོ་བོ་གང་ཡིན་པ་དེ་དང་འདྲ་བ་དགའ་བའི་གཟུགས་ཅན་དུ་འགྱུར་ཏེ། ཚངས་པའི་གཟུགས་ནི་དགའ་བ་སྟེ། །ཞེས་བཤད་པས་སོ། །

[Block 1305]
དེ་ལྟར་ཡང་མ་མཐོང་སྟེ་དེའི་ཕྱིར་ན་འབྲས་བུའི་རྗེས་སུ་དཔག་པ་མེད་དོ། །

[Block 1306]
ཡང་ན་སྐྱོན་དེ་བསལ་བར༌[^929]བྱ་བའི་ཕྱིར་རྒྱུའི་རྗེས་སུ་དཔག་པ་རྟོག་པར་བྱེད་ན། དཔེར་ན།

[Block 1307 [VERSE]]
བུང་བ༌[^930]མ་ཧེ་སྦྲུལ་དག་དང་། །
ཏ་མ་ལ་ཡི་འོད་ནག་ཅན། །
སྤྲིན་རྣམས་དེ་དང་འདྲ་བ་ནི། །
ཆར་འབབ་ནམ་ཡང་སླུ་མི་བྱེད། །

[Block 1308]
ཅེས་འབྱུང་བ་དེ་བཞིན་དུ་ཚངས་པ་ཐམས་ཅད་ཀྱི་བདག་ཉིད་གལ་ཏེ་མེད་ན་དེའི་ཚེ་སྣ་ཚོགས་པ་ཉིད་ཀྱང་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 1309]
དེ་ལ་སྨྲས་པ། རྒྱུའི་རྗེས་སུ་དཔག་པ་ནི་སླུ་བ༌[^931]ཡིན་པའི་ཕྱིར་ངེས་པ་མེད་པ་ཉིད་དོ། །

[Block 1310]
དཔེར་ན། ཕྱོགས་བཅུར་ཁྱབ་པའི་ཤིན་ཏུ་ནག་པོའི་མདོག་ཅན་སྤྲིན་རྣམས་ལས༌[^932]ཀྱང་ཆར་རེས་འགའ་མི་འབྱུང་ངོ་། །ཉི་མ་དྲོ་བའི་དུས་སུ་སྤྲིན་ཆུང་ངུ༌[^933]ལས་ཀྱང་ཆར་པ་འབྱུང་བར་མཐོང་བས་རྒྱུའི་རྗེས་སུ་དཔག་པ་ནི་སླུ་བ༌[^934]ཁོ་ནའོ། །

[Block 1311]
དེས་ནི་གྲོག་མོ་འབྱུང་བ་དང་ཉ་འཕར་བ་ལ་སོགས་པ་བཀག་གོ། །

[Block 1312]
སྤྱི་རུ་མཐོང་བའི་རྗེས་སུ་དཔག་པ་ནི་རྟོག་པར༌[^935]བྱེད་པ་ཡིན་ཞེ་ན། དཔེར་ན་ཁང་བཟངས༌[^936]ལ་སོགས་པ་བརྩིགས་པའི་སྔོན་དུ་འགྲོ་བ་འཕེལ་བར་མཐོང་བས་ནགས་ཀྱི་སྨན་ལ་སོགས་པ་རྣམས་ཀྱི་སྐྱེ་བ་སྔོན་དུ་འགྲོ་བའི་འཕེལ་བ་རྗེས་སུ་དཔག་པར་བྱའོ། །

[Block 1313]
དེ་ལྟར་ཚངས་པའི་སྣ་ཚོགས་པ་ཉིད་ཀྱིས་དངོས་པོ་སྣ་ཚོགས་པ་ཉིད་དོ། །

[Block 1314]
ཚིག་གི་དོན་སྣ་ཚོགས་པ་ཉིད་ཀྱང་ཚངས་པའི་སྣ་ཚོགས་པ་ཉིད་རྗེས་སུ་དཔག་པར་བྱའོ། །

[Block 1315]
དེ་ཡང་མི་རིགས་ཏེ། [^937]གང་གི་ཕྱིར་ཚངས་པ་སྣ་ཚོགས་པ་སྨྲ་བ་པོས་ཚངས་པའི་རང་བཞིན་ཅན་དངོས་པོ་རྣམས་འདོད་དོ།[^938] །

[Block 1316]
སྤྱིར་མཐོང་བའི་རྗེས་སུ་དཔག་པའི་ཕྱོགས་སུ་ཐ་དད་པར་ཐལ་བར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཚིག་གི་དོན་རྣམས་གུད༌[^939]དུ་གྲུབ་པ་ཡིན་པས་ཚངས་པའི་སྣ་ཚོགས་པ་ཉིད་ངེས་པ་དང་ཚངས་པ་ཡང་གུད༌[^940]ན་གྲུབ་པས་ཚིག་གི་དོན་སྣ་ཚོགས་ཐ་དད་པའོ། །

[Block 1317]
དེ་ལས་སླུ་བ༌[^941]ཉིད་ཀྱིས་ཀྱང་ངེས་པ་མེད་དེ། དེ་ཡང་དཔེར་ན་སྤྱིར་མཐོང་བའི་རྗེས་སུ་དཔག་པ་ནི་སླུ་བར༌[^942]མཐོང་སྟེ། ཁང་བཟངས༌[^943]ལ་སོགས་པའི་འཕེལ་བ་སྐྱེ་བ་སྔོན་དུ་འགྲོ་བས་ནགས་ཚལ་ལ་སོགས་པའི་འཕེལ་བ་རྟོགས་པར་མི་བྱེད་དོ། །

[Block 1318]
ནགས་ཚལ་ལ་སོགས་པ་ཁ་ཅིག་ནི༌[^944]ཆུ་འབབ་པས་ཀྱང་འཕེལ་བར་མི་འགྱུར་བ་དང་། ཁ་ཅིག་ཀྱང་མིག་འཕྲུལ་མཁན་གྱིས་སྤྲུལ་པ་ཡང་མཐོང་ངོ་། །དེ་བས་ན་རྗེས་སུ་དཔག་པ་དེས་ངེས་པ་མེད་དོ། །

[Block 1319]
སྒྲ་ལས་བྱུང་བ་ཡང་ཚད་མ་མ་ཡིན་ཏེ། ཚངས་པའི་སྣ་ཚོགས་པ་ཉིད་ལ་སྔོན་དུ༌[^945]བཤད་པའི་རིགས་པས་སྒྲ་དང་དོན་དག་གི་འབྲེལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1320]
དོན་ཙམ་ཡང་སོ་སོར་བསྟན་པར་སྒྲས་མི་ནུས་ན་དེའི་སྣ་ཚོགས་པ་ཉིད་ཇི་ལྟར་བརྗོད། སྤྱིའི་རྣམ་པས་ནུས་ཀྱང་སྒྲའི་རང་གི་མཚན་ཉིད་དང་ལྷན་ཅིག་ཏུ་དོན་གྱི་རང་གི་མཚན་ཉིད་ལ་བརྗོད་པ་དང་རྗོད་པར་བྱེད་པའི་མཚན་ཉིད་མེད་དོ། །

[Block 1321]
སྤྱིའི༌[^946]ཡང་གོང་དུ་བཀག་པས་ཇི༌[^947]ལྟར་དེ་ཁོ་བོས༌[^948]ཚད་མར་གཟུང་། སྐད་ཅིག་མ་ཡིན་པས་ཀྱང་ངེས་པ་མེད་དེ། གང་གི་ཕྱིར་སྒྲ་ནི་གནས་དང་བྱེད་པ་དང་སྐྱེས་བུའི་རྩོལ་བ་ལས་འབྱུང་བས་བརྗོད་མ་ཐག་ཏུ་འཇིག་པར་འགྱུར་བ་དེ་རང་གཟུགས་སུ་ཡོད་པར་མི་འགྱུར་བས་ཇི་ལྟར་དོན་རྟོགས་པར་བྱེད་དེ། [^949]ག་དང་ཨུ་དང་ཚེག་དྲག་རྣམས་རེ་རེ་ལྷན་ཅིག་ཏུ་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 1322]
རྣ་བའི་དབང་པོས་གཟུང་བར་བྱ་བ་དབྱངས་ཙམ་ནི་རྟོགས་པར་བྱེད་པ་ཡིན་ཏེ། དྲིལ་བུའི་སྒྲ་བཞིན་ནོ་ཞེ་ན། སྨྲས་པ་ཡི་གེ་དང་ཚིག་དང་ངག་རྣམས་ཀྱིས༌[^950]རང་གི་ངོ་བོ་དོར་ནས་དོན་གཞན་གྱི་དབྱངས་ཙམ་མི་དམིགས་སོ། །

[Block 1323]
དེ་རྣམས༌[^951]ཞིག་ནས་དབྱངས་ནི་མི་འཇིག་པར་ཇི་ལྟར་འགྱུར། དེའི་ཕྱིར་ན་དབྱངས་ཙམ་གྱི་ཐ་སྙད་ནི་བཏགས་པ་ཡིན་གྱི་ངེས་པའི་རྒྱུར་ནི་མ་ཡིན་ནོ། །

[Block 1324]
དཔེ་ཡང་ཚད་མ་མ་ཡིན་ཏེ་གང་གི་ཕྱིར་དེ་ནི་ཆོས་གསུམ་དང་ལྡན་པ་ཡིན་ཏེ། དཔེ་དང་དཔེ་ལས་བྱུང་བ་དང་ཐུན་མོང་གི་ཆོས་ཀྱིས་སོ། །

[Block 1325]
དཔེར་ན་བ་དང་འདྲ་བ་ནི་བ་མེན་ནོ། །

[Block 1326]
དེ་ལ་བ་མེན་མཐོང་བའི་སྐྱེས་བུས་བ་ལ་གནས་པའི་ལྐོག་ཤལ་ལ་སོགས་པའི་ཆོས་མཐུན་པའི་ཕྱིར་བ་མེན་མ་མཐོང་བའི་སྐྱེས་བུ་ཁ་ཅིག་རྟོགས་པར་བྱེད་དེ། བ་དང་འདྲ་བ་ནི་བ་མེན་ནོ་ཞེས་པས་སོ། །

[Block 1327]
དེས་ནི་དེའི་བ་མེན་ཡིན་ཞེས་ཁོང་དུ་ཆུད་དོ། །

[Block 1328]
དེ་བཞིན་དུ་འདིར་ཚངས་པའི་སྣ་ཚོགས་པ་ཉིད་དངོས་པོ་སྣ་ཚོགས་པ་ཉིད་ཀྱིས་དཔེ་མ་ཡིན་པ་དང་། དེ་ལ་སོགས་པས་ཀྱང་མ་ཡིན་ཏེ་དེ༌[^952]དང་མཐུན་པའི་ཆོས་མེད་པའི་ཕྱིར་རོ། །

[Block 1329]
ཚངས་པ་ནི་གཟུགས་མེད་པ་དང་། དངོས་པོ་རྣམས་གཟུགས་ཅན་ཡིན་པས་གང༌[^953]གིས་དཔེར་བྱའོ། །

[Block 1330]
[^954]དོན་གྱི་ཤུགས་ཀྱིས་ཀྱང་ངེས་པ་མེད་དོ། །

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
--- END BLOCKS ---
