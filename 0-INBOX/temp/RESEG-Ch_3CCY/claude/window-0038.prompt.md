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
གང་ཡང་འདི་སྙམ་དུ་སེམས་ཏེ། སྒྲའི་མཚན་ཉིད་ལ་མངོན་པར་ཞེན་པ་སྤང་བའི་དོན་དུ་སློབ་དཔོན་གྱི་བསམས་བཞིན༌[^952]དུ་ཟུར་ཆག་པའི་སྒྲའི་སྦྱོར་བ་བྱས་སོ་ཞེས་པ་དེ་མི་འཐད་དེ། །གལ་ཏེ་སྒྲའི་མཚན་ཉིད་བོར་ནས་བརྗོད་པས་དེས་མངོན་པར་ཞེན་པ་དང་བྲལ་ནས་སྒྲའི་མཚན་ཉིད་ལོགས་སུ་བོར་བའི་བརྗོད་པ་ལ༌[^953]མངོན་པར་ཞེན་པ་འབྱུང་བར་འགྱུར་ལ། དེ་ལྟར་ཡང་མ་ཡིན་ནོ། །

[Block 1332]
ཡང་ཇི་ལྟ་དེ་ལྟར་སྒྲའི་སྦྱོར་བ་བྱེད་ན། དེའི་ཚེ་ཚིག་ལྷུག་པ་ལ་ཡང་མངོན་པར་ཞེན་པ་སྤོང་བའི༌[^954]ཕྱིར་སྦྱོར་བ་མཛད་པར༌[^955]འགྱུར་ན། དེ་ཡང་མ་མཛད་ལ། དེའི་ཕྱིར་མཚན་ཉིད་མི་དྲན་པ་ཉིད་སྲིད་ཀྱི་མཚན་ཉིད་ལ་མངོན་པར་ཞེན་པ་སྤོང་བས་ནི་ཡིན་ནོ། །

[Block 1333]
ཐབས་གཞན་གྱིས་དེའི་མངོན་པར་ཞེན་པ་སྤོང་བར་བྱེད་པ་མེད་པ་མ་ཡིན་ལ། དེའི་ཕྱིར་སློབ་དཔོན་ནི་ནམ་ཡང་ཟུར་ཆག་པའི་སྒྲའི་སྦྱོར་བ་མི་མཛད་དོ། །

[Block 1334]
འོ་ན་རེ་ཞིག་འགྲོ་བ༌[^956]མི་འགྲོ་ཞིང་། །ཞེས་པ་ལ་སོགས་པ་ཟུར་ཆག་པའི་སྒྲའི་སྦྱོར་བ་མཐོང་བ་མ་ཡིན་ནམ་ཞེ་ན། འདི་ནི་ཟུར་ཆག་པའི་སྒྲ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་བཟློག་པ་ནི་མང་པོའོ་ཞེས་པས་འདི་ནི། ས་མཐའི༌[^957]རི་མཐའ་ཉེ་བར་གཟུང་བ་རྟགས་དང་སྐྱེས་བུ་དང་། །

[Block 1335 [VERSE]]
ཀ་ལ་ཧལ་དབྱངས་ཡིག་བྱེད་པོ་ཡ་ང་ཉ། །
བསྟན་བཅོས་བྱེད་པས་འདི་དག་བཟློག་པ་སྟེ། །
དེས་ཀྱང་མང་པོ་འགྲུབ་པར་འགྱུར་ཞེས་བྱ། །

[Block 1336]
ཞེས་པ་མ་ངེས་པར་བརྗོད་པ་ལས་ཏེ། བཟློག་པར་སྨྲ་བ་ལ། སྨྲ་བས་བདག་གི་ཚིག་ཏུ་འགྱུར་རོ། །

[Block 1337]
འོ་ན་རིག་བྱེད་ཀྱིའོ་ཞེས་པའི་གཞི་ལས་འདི་ནི་རིག་བྱེད་ཀྱི་བརྗོད་པའོ། །

[Block 1338]
གཞན་ཡང་བཟློག་པ་ནི་སྡེབ་སྦྱོར་གྱི་ཁོ་ནའོ་ཞེ་ན། དེ་དག་ནི་མ་ཡིན་ཏེ། དེར་ནི་ཚིགས་སུ་བཅད་པའི་སྡེབ་སྦྱོར་འཇིག་རྟེན་པས་རིག་བྱེད་ཀྱི་སྒྲས་ཡོངས་སུ་གཟུང་བ་མ་ཡིན་ནོ། །

[Block 1339]
འོན་ཀྱང་སྔགས་དང་བྲམ་ཟེ་རྟོགས་པ༌[^958]རྣམས་ཀྱིའོ། །

[Block 1340]
དེའི་ཕྱིར་འདི་དག་མཚན་ཉིད་ཀྱི༌[^959]རྗེས་སུ་འགྲོ་བ་མ་ཡིན་ནོ་ཞེ་ན། སྨྲས་པ། དེ་ལྟར་འགྱུར་དུ་ཆུག་ན་ཡང་། དེ་ལྟ་ན་ཡང་རིག་བྱེད་བཞིན་དུ་སྙན་ངག་མཁན་གྱིས་སྦྱོར་ཏེ། དེ་སྐད་དུ་ཡང་།

[Block 1341 [VERSE]]
རིག་བྱེད་འཇིག་རྟེན་པར་མཐོང་ལ། །
འཇིག་རྟེན་པ་ཡང་རིག་བྱེད་ལ། །
སྒྲ་ནི་ཁྱད་འཕགས་སྦྱོར་བའི་ཕྱིར། །
ནམ་ཡང་ཐ་དད་མ་ཡིན་ནོ། །

[Block 1342]
ཞེས་སོ། །

[Block 1343]
ཁྱད་པར་འཕགས་པ་ཡང་སློབ་དཔོན་འདིའོ་ཞེས་བྱ་སྟེ། དེས་ན་འདིར་ཟུར་ཆག་པའི་སྒྲའི་སྦྱོར་བ་མི་སྲིད་ལ། མཚན་ཉིད་བྱེད་པས་མཚན་ཉིད་མ་ཚང་བ་ཡང་སྲིད་དོ།[^960] །མཚན་ཉིད་ནི་མཚོན་བྱ་མ་ལུས་པ་ལ་ཁྱབ་པར་འགྱུར་བས་སོ། །

[Block 1344]
མཚོན་ཆ་ཡང་ཁྱད་པར་འཕགས་པས་སྦྱར་བ་བྱས་པའི་སྒྲའོ། །

[Block 1345]
དེ་རྣམས་མཚན་ཉིད་ཀྱིས་མ་བསྡུས༌[^961]པའི་ཕྱིར་འདི་ནི་མཚན་ཉིད་བྱེད་པའི་སྐྱོན་ཡིན་གྱི་སློབ་དཔོན་གྱི་ནི་མ་ཡིན་ནོ། །

[Block 1346]
དེའི་དུས་ན་རབ་ཏུ་གྲགས་པའི་སྒྲ་མང་པོ་སློབ་དཔོན་གྱིས་གཟིགས་པ་རྣམས་ཀྱང་། དེང་སང་གི་པཱ་ཎི་ནི་ལ་མཚན་ཉིད་ལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1347]
དེང་སང་དུས་ན་དེས་མཚན་ཉིད་བྱས་པ་ཡང་མ་ལུས་པའི་སྒྲའི་རྗེས་སུ་འབྲངས་ནས་མཚན་ཉིད་བརྗོད༌[^962]ཀྱང་། གལ་ཏེ་ན་ཡང་། དེ་བསམས་པ༌[^963]དང་དྲན་པ་ཉམས་པ་དག་གིས་མཚོན་བྱ་མ་ལུས་པ་ལ་ཁྱབ་པའི་མཚན་ཉིད་བརྗོད་པར་མ་ལུས་པས༌[^964]ན། དེའི་ཚེ་དེ་སུའི་སྐྱོན་ཡིན། འདི་ལྟར་ཀཱ་ཏྱཱ་ཡ་ནས་འདིར་ཡང་ཤིན་ཏུ་ཆེས་མ་ཚང་བའི་མཚན་ཉིད་སྨོས་པ་ནི། ཇི་ལྟར་པཱ་ཎི་ནི་དྲན་པ་དང་བསམས་པ༌[^965]ཉམས་པས་མཚན་ཉིད་མ་ཚང་བ་ལྟར་དེ་བཞིན་དུ་དུས་དེང་སང༌[^966]ན་སྐྱེས་པའི་ཀཱ་ཏྱཱ་ཡ་ན་ལ་སོགས་པའི༌[^967]ལ་སྲིད་ལ། གལ་ཏེ་ན་ཡང་རིག་པའི་སྒྲས་སྔགས་དང་བྲམ་ཟེ་དང་རྟོག་པ་གཟུང་ཡང་རུང་། ཚིགས་སུ་བཅད་པའི་སྡེབ་སྦྱོར་གྱི་མདོ་རུ་གཟུང་ཡང་རུང་སྟེ། དེ་ལྟར་པཱ་ཎི་ནིའི་སྒྲ་ཡང་སྐྱོན་ཅན་དུ་མི་འགྱུར་ལ། སྡེར་སྦྱོར༌[^968]གྱི་མཚན་ཉིད་སྟོན་པ་པོ་རྣམས་ལ་ཡང་འདི་དག་འཐད་པར་འགྱུར་རོ། །

[Block 1348]
གཞན་ཡང་མོན་སྲན་གྲེའུར་བྱས་པའི༌[^969]སྡེབ་སྦྱོར་ཉམས་པར་མི་བྱའོ་ཞེས་སོ། །

[Block 1349]
དེ་བཞིན་དུ་ཡང་ཁྱད་པར་འཕགས་པའི་སྦྱོར་བའི་རྗེས་སུ་འབྲངས་ནས། ཡངས་ཤིང་ཆེ་བ་ལ་སོགས་པ་དང་། རྨ་བྱ་རོལ་པ་ལ་སོགས་པ་དང་། སྦྱོར་བ་རྣམ་པར་ཕྱེ་བ་ལ་སོགས་པ་ཡང་དོན་ཆེན་པོར་འཐད་དེ། མཚན་ཉིད་བྱེད་པས་མ་ཚང་བ༌[^970]མ་ཡིན་ལ། ཁྱད་པར་འཕགས་པས་སྦྱར་བའི༌[^971]སྒྲ་རྣམས་ཀྱང་ཟུར་ཆག་པའི་སྒྲ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། སྤྲོས་པ་དེ་ཙམ་གྱིས་ཆོག་གོ། །

[Block 1350]
སྐབས་སུ་བབ་པ་ཉིད་བཤད་པར་བྱ་སྟེ།

[Block 1351]
ཡང་ནི་ཇི་སྐད་སྨོས་པ་དེ་ལས།

[Block 1352 [VERSE]]
འཇིག་རྟེན་པ་ཡི་ཆོས་བསྟན་མི་ཉམས་ཤིང་། །
ཡང་དག་ཉིད་དུ་ནམ་ཡང་ཆོས་བསྟན་མེད། །

[Block 1353]
ཅེས་པ་ལ། སླར་ཡང་འདིར་ཇི་ལྟར་ན།

[Block 1354 [VERSE]]
འཇིག་རྟེན་པ་ལ་ཆོས་བསྟན་ཅིང་། །
ཇི་ལྟར་ཡང་འདིར་མི་འཇིགས༌[^972]ལ། །

[Block 1355]
གཞན་ཡང་ནམ་ཡང་དེ་ཁོ་ན་ཉིད་ལ་གང་དུ་གང༌[^973]ཆོས་བསྟན་པ་མེད་ཅེས་པ་དེ་དག་འདིར་སྟོན་པར༌[^974]འདོད་པས་གསུངས་པ།

[Block 1356 [HEADING]]
### ཚིགས་བཅད་བདུན་ཅུ་པ། ^1-69-0

[Block 1357 [VERSE]]
འདི་ལ་བརྟེན་ནས་འདི་འབྱུང་ཞེས། །
འཇིག་རྟེན་ཚུལ་འདི་མི་འགོག་ཅིང་། །
གང་རྟེན་རང་བཞིན་མེད་པས་དེ། །
ཇི་ལྟར་ཡོད་འགྱུར་དེ་ཉིད་དེས། །

[Block 1358]
འདིར་སེམས་ཅན་དང་སྣོད་ཀྱི་འཇིག་རྟེན་དུ་བརྡར༌[^975]བཏགས་པ་འདི་དག་མ་རིག་པ་དང་རླུང་གི་དཀྱིལ་འཁོར་ལ་སོགས་པའི་རིམ་པས༌[^976]འཇུག་པ་ནང་གི་བདག་ཉིད་དང་ཕྱིའི་དབྱེ་བས་ཐ་དད་པ་རྣམས། རང་དང་གཞན་དང་གཉི་གའི་རྒྱུ་དང་ཡོད་པ་དང་མེད་པ་དང་གཉི་ག་དང་གཉི་ག་མ་ཡིན་པ་ལས་སྐྱེ་བར་བརྟགས་པ་རྣམས་རྐྱེན་འདི་པ་ཙམ་ལས་སྐྱེ་བར་བརྟགས་པ་ལས་སྐྱེ༌[^977]བར་སྐྱེ་བ་ཉེ་བར་བསྟན་པ༌[^978]ནི་འཇིག་རྟེན་པའི་ཆོས་བསྟན་པ་ཞེས་བརྗོད་དོ། །

[Block 1359]
དེ་ཡང་རྐྱེན་འདི་པ་ཙམ་དུ་ཁས་བླངས་པར་གྱུར་པས་མི་ཉམས་ལ། དེ་ལས་གཞན་དུ་ན་བརྟགས་ནས་ཁས་བླངས་པར་འགྱུར་ན། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མི་སྲིད་པར་འགྱུར་ལ། གཞན་དུ་བརྟགས་པ་ཡང་འཇིག་རྟེན་པའི་མ་ཡིན་ཏེ། དེ་ནི་འཇིག་རྟེན་ལས་དེ་བཞིན་དུ་ཁས་མ་བླངས་པའི་ཕྱིར། འཇིག་རྟེན་པ་མ་ཡིན་པ་ཐར་པ་འདོད་པ་ཁ་ཅིག་གིས༌[^979]ཕྱིན་ཅི་ལོག་གིས༌[^980]འདིར་བརྟགས་པའི་ཕྱིར་རོ། །

[Block 1360]
ཇི་སྐད་དུ།

[Block 1361]
བསྟན་བཅོས་ལས།

[Block 1362 [VERSE]]
[^981] བྱེད་པོ་ལས་ཀྱི་རྟེན་འབྱུང་ནི། །
དེ་ལ་བརྟེན་ནས་བྱེད་པོ་དང་། །
ལས་འཇུག་གཞན་པ་འགྲུབ་པ་ཡི། །
རྒྱུ་མཚན་ཅི་ཡང་མ་མཐོང་ངོ་། །

[Block 1363]
ཞེས་སོ། །

[Block 1364]
དེ་འདི་ལྟར་འདི་ལ་བརྟེན་ནས༌[^982]འབྱུང་ངོ་ཞེས་པའི་འཇིག་རྟེན་པའི་ཚུལ་འདི་ནི་མི་འགོག་པས། འཇིག་རྟེན་པའི་ཆོས་བསྟན་མི་ཉམས་སོ་ཞེས་གནས་སོ། །

[Block 1365]
གང་ལ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དེ་ནི་ངོ་བོ་ཉིད་ཀྱིས་མེད་པ་སྟེ། ཡོད་བཞིན་པ་ལ་བརྟེན་ནས་འབྱུང་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1366]
གང་ཡང་དེ་ལྟར་རང་བཞིན་གྱིས་ཡོད༌[^983]པ་མ་ཡིན་པས། དེ་ཇི་ལྟར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡོད་བཞིན་པར་འགྱུར། དེའི་རང་བཞིན་ཡོད་བཞིན་པ་མ་ཡིན་པ་ཉིད་དོ་ཞེས་དགོངས་པའོ། །

[Block 1367]
དེས་ན་འདི་ལྟར་དཔྱད་ན་རྣལ་འབྱོར་པ་དེ་ཁོ་ན་ཉིད་ངེས་པར་འགྱུར་ཏེ། རང་བཞིན་གྱིས་མ་སྐྱེས་པའི་དངོས་པོའི་དེ་ཁོ་ན་ཉིད་ཡོངས་སུ་ཤེས་པར་འགྱུར་རོ། །

[Block 1368]
དེ་ཁོ་ན་ཉིད་མཐོང་བར་གྱུར་ན་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་མི་དམིགས་པའི་ཕྱིར། ནམ་ཡང་ཆོས་རྣམས་ཀྱི་རང་བཞིན་ཡོངས་སུ་གསལ་བར་མི་བྱེད་དེ། རང་ཉིད་ཀྱིས་མ་དམིགས་པར་གཞན་ལ་བཤད་པ་མི་སྲིད་དོ། །

[Block 1369]
དེས་ན་ཡང་དག་ཉིད་དུ་ནམ་ཡང་ཆོས་བསྟན་པ་མ་ཡིན་ནོ་ཞེས་གྲུབ་བོ། །

[Block 1370]
དེ་ལྟར་ཚིགས་སུ་བཅད༌[^984]པ་གཉིས༌[^985]ཀྱིས་རབ་ཏུ་བྱེད་པ་མ་ལུས་པར་བསྒྲུབ་པའི༌[^986]དོན་བསྡུས་པའི་ཚུལ་གྱིས་ཉེ་བར་བསྟན་ནས། དེ་ལས་གཞན་ལ་ཇི་ལྟར་བསྟན་པའི་ཆོས་རྣམས་ཀྱི་རང་བཞིན་རྣམ་པར་འབྱེད་པས་ངེས་པར་བླ་ན་མེད་པའི་འབྲས་བུའི་དངོས་གྲུབ་མ་ཐོབ་པ་རྣམས། སླར་ཡང་ཐོས་པ་དང་བསམ་པ་དང་བསྒོམ་པ་ལ༌[^987]ཡང་དག་པར་བརྩོན་པ་བསྐྱེད་པའི་ཕྱིར་དང་། མ་ཞུགས་པ་རྣམས༌[^988]ཞུགས་པ་དང་ལྡན་པ་ཡང་སྤྲོ་བ་བསྐྱེད་པའི་དོན་དུ་ཡང་ཚིགས་སུ་བཅད་པ་གཉིས་གསུངས་པ།
--- END BLOCKS ---
