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
དུད་འགྲོའི་རང་བཞིན་ལ་ནི་མི་ཕྱོགས་ཞེས་བྱ་བ་ནི་སྲོག་གཅོད་པ་ལས་ལྡོག་པའོ། །

[Block 1262]
བདེ་བ་དང་མཐུན་ཞིང་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིའི་ལུས་ནི་ཕན་པ་ཡིན་བདེ་བ་མ་ཡིན་པ་དང་། བདེ་བ་ཡང་མ་ཡིན་ཕན་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམ་པ་བཞི་ལས་དེ་ལ་ཕན་པ་མེད་པ་ནི་གཅིག་ཏུ་མི་བྱ་བ་ཡིན་ནོ། །

[Block 1263]
གང་དུ་ཕན་པ་ཡོད་པ་དེ་ནི་གཅིག་ཏུ་བྱ་བ་སྟེ། དེ་ལ་ཕན་ལ་བདེ་བ་མ་ཡིན་པ་དང་། ཕན་ལ་བདེ་བ་དེ་ནི་བྱ་བ་ཡིན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 1264]
བདེ་དང་མཐུན་ཞིང་ཡོན་ཏན་མི་མཐུན་ཚུལ། །ཞེས་བྱ་བ་ནི་གང་དུ་ཕན་པ་དང་བདེ་བ་ཡོད་པ་དེ་བསྟན་ཏོ། །

[Block 1265]
ཡོན་ཏན་མཐུན་ཞིང་བདེ་དང་མི་མཐུན་ཚུལ། །ཞེས་བྱ་བ་ནི་ཕན་པ་དེ་ཉིད་བདེ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1266]
ཡོན་ཏན་ཕྱོགས་ལ་བརྟེན་ན་ནི་ཞེས་བྱ་བ་ནི་གང་ལ་ཕན་པ་ཡོད་པ་དེ་ལ་བརྟེན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1267]
གཞན་ལ་སྙིང་རྗེ་དང་སྒྲུབ་པ་ནི་སྙིང་རྗེ་དང་སྒྲུབ་པའོ། །

[Block 1268]
དེ་གཉིས་ཀྱིས་བླ་མར་གྱུར་པ་ནི་གཞན་ལ་སྙིང་རྗེ་སྒྲུབ་པའི་བླ་མ་སྟེ། བསམ་པ་དང་སྦྱོར་བ་གཉིས་ཆེ་བའོ། །

[Block 1269]
ཡང་ན་བདག་དང་གཞན་ལ་ཕན་པ༌[^726]སྒྲུབ་པའོ། །

[Block 1270]
ཡང་ན་གཞན་ལ་སྙིང་རྗེ་བ་ཉིད་སྒྲུབ་པ་ཡིན་པས་གཞན་ལ་སྙིང་རྗེ་ཆེ་བའི་བླ་མར་གྱུར་པ་སྟེ། གཞན་ལ་ཕན་པར་སྒྲུབ་པ་ཡིན་པས་བླ་མ་ཞེས་བརྗོད་པ་ཡིན་ནོ། །

[Block 1271]
ཡོན་ཏན་རྗེས༌[^727]འགྲོ་རང་བཞིན་ཕུན་སུམ་ཚོགས། །ཞེས་བྱ་བ་ལ་སློབ་མ་རྣམས་ཀྱི་རང་བཞིན་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1272]
སློབ་མ་དང་བླ་མའི་ཕུན་སུམ་ཚོགས་པ་གཉིས་ཀྱི་གྲགས་པ་ལྷ་ཡུལ་དུ་ཡང་གྲགས་པར་གྱུར་པའོ། །

[Block 1273]
དཀྱིལ་འཁོར་ཡོངས་སུ་རྫོགས་པ་ཉེ་བ་ཅུང་ཟད་མ་རྫོགས་པ་བཟང་པོ་ནི་ཡོངས་སུ་མ་གང་བའི་མཛེས་པའོ། །

[Block 1274]
འདུ་བ་གང་ཡོད་མཐའ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་དྲུག་སྨོས་པ་ལ། དེ་ལ་འདུ་བ་གང་ཡོད་དོ། །

[Block 1275]
ཞེས༌[^728]བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་གཡོག་འཁོར་དང་ལོངས་སྤྱོད་ཆེན་པོའི་བདག་ཉིད་སྲིད་པའི་ཕུན་སུམ་ཚོགས་པ་མཐར༌[^729]རྒུད་པ་ཉིད་དུ་བསྟན་ཏེ། འདུ་བ་གང་ཡོད་མཐའ་ནི་འབྲལ་བར་འགྱུར། །ཞེས་བྱ་བ་ནི་མཐར་འབྱེ་བ༌[^730]ཡིན་ཏེ། འདིས་ནི་བསོད་ནམས་ཀྱི༌[^731]ཚོགས་ཀྱི་འབྲས་བུ་གཡོག་འཁོར་ཆེན་པོ་དང་བྲལ་ཞིང་མཐར་རྒུད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1276]
དར་བ་ཡོད་ན་ངན་པ་རྒུད་པའི་མཐའ། །ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ལོངས་སྤྱོད་ཆེན་པོ་ལས་མཐར༌[^732]རྒུད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1277]
ཚེ་ཡང་གློག་བཞིན་འགྱུ་ཞིང་མི་བརྟན༌[^733]ནོ། །ཞེས་བྱ་བ་འདིས་ནི་ཚུལ་ཁྲིམས་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་བདག་གི༌[^734]ཕུན་སུམ་ཚོགས་པ་འཆི་བ་ཉིད་ཀྱིས་རྒུད་པར་བསྟན་ཏོ། །

[Block 1278]
དེ༌[^735]ཕྱིར་ཞེས་བྱ་བ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་གསུམ་པོ་དེ་ཉིད་ཀྱི་ཕྱིར་བག་ཡོད་པར་བྱ་བ་སྟེ། ཕྱིས་ཀྱང་དེའི་རྒྱུ་འཕེལ་བ་ལ་བག་ཡོད་པར་བྱའོ། །

[Block 1279]
ཡང་ན་འདིའི་བསྡུས་པའི་དོན་གཞན་ནི་དགེ་བའི་བཤེས་གཉེན་དང་། ལུས་དང་སྲོག་དང་བྲལ་བ་དང་། རྒུད་པ་དང་། འཇིག་པ༌[^736]ཞེས་བྱ་བ་སྟེ། དེ་བས་ན༌[^737]མཐར་རྒུད་པས་འཇིགས་པ་མེད་པ་ལས་རྒྱུ་གསུམ་གྱིས༌[^738]བག་ཡོད་པར་འགྱུར་ཏེ། ཚིགས་བཅད་འདིས་གོ་རིམས་བཞིན་དུ་སྦྱར་རོ། །

[Block 1280]
བག་ཡོད་པར་བྱའོ་ཞེས་བསྟན་པ་ལ། ཇི་ལྟར་བག་ཡོད་པར་བྱ་བ་དང་། དེའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར། དེ་བས་སྦྱིན་པ་ཚུལ་ཁྲིམས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 1281]
སྦྱིན་པ་ཞེས་བྱ་བས༌[^739]ནི་སྦྱིན་པའི་བསོད་ནམས་ཀྱི་ཚོགས་བསྟན་ཏོ། །

[Block 1282]
ཚུལ་ཁྲིམས་བརྒྱན་པ་ཞེས་བྱ་བས་ནི་ཚུལ་ཁྲིམས་དང་། བཟོད་པའི་བསོད་ནམས་ཀྱི་ཚོགས་བསྟན་ཏོ། །

[Block 1283]
ཚུལ་ཁྲིམས་ལས་ཐ་དད་པ་དེ་ཡང་གང་ཞེ་ན། གནོད་པར་བྱེད་པ་ལ་ལན་དུ་གནོད་པ་བྱེད་པའི་མཚན་ཉིད་ཀྱི་བཟོད་པ་མེད་པའོ། །

[Block 1284]
ཚུལ་ཁྲིམས་མེད་ན་ནི་གནོད་པ་མི་བྱེད་པ་ལ་ཡང་གནོད་པ་བྱེད་པ་སྟེ། དེས་ན༌[^740]གནོད་པ་བྱེད་པ་ལས་ལྡོག་པའོ། །

[Block 1285]
དེ་བས་ན་སྤྱིར་གཉི་ག་ལ་སྦྱར་བ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་སྨོས་པས་བཟོད་པ་མ་སྨོས་ཀྱང་གྲུབ་པ་ཡིན་ནོ། །

[Block 1286]
སྐྱེ་བའི་ངན་འགྲོའི་ནང་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་ཕྱེད་འོག་མས་ནི་བསོད་ནམས་ཀྱི་ཚོགས་དང་འབྲེལ༌[^741]པའི་ཕན་ཡོན་ནོ། །

[Block 1287]
རྟེན་ནི་གནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1288]
སྐར་མ་རྣམས་ཀྱི༌[^742]དཔལ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་སྨོས་པ་ནི་བསོད་ནམས་ཀྱི་གནས་སུ༌[^743]སྨོས་པའི་ཕྱིར་རོ། །

[Block 1289]
དེ་ལ་སྐར་མ་རྣམས་ཀྱི་དཔལ་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་ཚུལ་ཁྲིམས་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་བསྒྲུབ་པའི༌[^744]ཕྱིར་ཏེ། ཚུལ་ཁྲིམས་ནི་བདག་གི་ཕུན་སུམ་ཚོགས་པའི་འབྲས་བུ་སྟེ། དེ་ཡང་རིས་འདྲ་བ་ལས༌[^745]ཚུལ་ཁྲིམས་དེ་ཁྱད་པར་དུ་གྱུར་པའི་འབྲས་བུ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1290]
སྐར་མ་རྣམས་དང་བསིལ་བར་རིགས་འདྲ་ཞིང་ཆོས་མཐུན་པ་དེ་ལས་ཁྱད་པར་དུ་གྱུར་པའི་ཡོན་ཏན་གྱིས་ཟླ་བ་མཛེས་པ་ཡིན་ཏེ། མཛེས་ཤིང་ཁྱད་པར་དུ་གྱུར་པ་ཡིན་ནོ། །

[Block 1291]
འོད་ཟེར་ཅན་ནི་འོད་དང་ལྡན་པ་སྟེ། ཆོས་མཐུན་པའི་འོད་དང་ལྡན་པ༌[^746]གཞན་པ་བ་སངས་ལ་སོགས་པའི་འོད་ཟེར་ཅན་འོད་དང་ལྡན་པའོ། །

[Block 1292]
ཉི་མས་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་ཀྱི་རང་བཞིན་གྱི་བསོད་ནམས་ཀྱི་ཡོན་ཏན་ལ་སོགས་པའོ། །

[Block 1293]
སའི་དབང་ཕྱུག་ཅེས་བྱ་བ་ལ་སོགས་པའི༌[^747]ཚིགས་བཅད་ནི་བཟོད་པའི་རང་བཞིན་གྱི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་སྟེ། ངེས་པར་འབྱུང་བ་སྟེ་ད་ལྟར་བྱུང་བའི་སྐྱེས་བུའི་བྱེད་པ་དགོན་པའི་རི་དགས་ཀྱང་ཅི་ཡང་མི་བྱེད་དོ་ཞེས་སྟོན་ཏོ། །

[Block 1294]
དེ་ལྟར་བསོད་ནམས་མ་ཡིན་པ་རྗེས་སུ་འབྲང་བ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་རྗེས་སུ་འབྲང་བ་ཡིན་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར། བསོད་ནམས་ཆེ་བས་ཞེས་བྱ་བ་འདིའི་དོན་ཡིན་ཏེ། བསྐྲད་པ་ཉིད་ཡིན་པས་བསྐྲད་པ་སྟེ། ཇི་ལྟར་གང་སུ་དག་གིས་བསྐྲད་ཅིང་དེ༌[^748]རྗེས་སུ་འགྲོ་བ་བཟློག་སྟེ་དེ་དང་མི་མཐུན་པའི་ཕྱོགས་ལ་བརྟེན་པ་དེ་བཞིན་དུ། བསོད་ནམས་ཆེ་བས་སྐྲག་པ་བཞིན་དུ་དེ་ཉེ་བར་འགྲོ་བའི་གླགས་སྐབས་ཐོབ་པས་དེའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་བསོད་ནམས་རབ་ཏུ་ཉམས་པས་དེའི་མི་མཐུན་པའི་ཕྱོགས་སོ། །

[Block 1295]
ཁྲོས་བཞིན་ཞེས་བྱ་བ༌[^749]གང་ལ་ཁྲོས་བཞིན་ཞེ་ན། བསོད་ནམས་ཆེ་བ་ལ་ཁྲོས་པ་བཞིན་དུ་དྲུང་དུ་འགྲོའོ། །

[Block 1296]
སྔར་བསྟན་པའི་དེ་ལས་སྦྱིན་པ་ཚུལ་ཁྲིམས་ཞེས་བྱ་བའི་ཚིགས་བཅད་དེས་ནི་བསོད་ནམས་ཉི་ཚེ་སྤེལ་བ་ལ་གྲོགས་པོ་བཙུད་པ་ཡིན་ནོ། །

[Block 1297]
སྡུག་བསྔལ་གཞིར་གྱུར༌[^750]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་མི་མཐུན་པའི་ཕྱོགས་སྤང་བ་དང་། གཉེན་པོའི་ཕྱོགས་བསྟེན་པ་ལ་གྲོགས་པོ་དག་ཡང་དག་པར་འཛུད་པ་ཡིན་ནོ། །

[Block 1298]
སྡུག་བསྔལ་གྱི་གཞིར་གྱུར་ཞེས༌[^751]བྱ་བ་ནི༌[^752]འདི་ལ་སྡུག་བསྔལ་གྱི་གནས་ཡིན་པས་སྡུག་བསྔལ་གནས་གཞི་སྟེ། གང་ལ་སྡུག་བསྔལ་གྱི་གནས་ཀྱི་བསོད་ནམས་མ་ཡིན་པའི་ལས་ཡོད་པ་དེ་ནི་སྡུག་བསྔལ་གྱི་གཞིའོ། །

[Block 1299]
དེ་བས་ན་འདིས་ནི་སྡིག་པའི་ལས་ཏེ་ངན་སོང་གི་རྒྱུ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1300]
གང་ལ་གཏམ་ངན་དང་རྗེས་སུ་འབྲེལ་པའི་སྡིག་པའི་ལམ་དེ་ནི་གཏམ་ངན་རྗེས་སུ་འབྲང་བའོ། །
--- END BLOCKS ---
