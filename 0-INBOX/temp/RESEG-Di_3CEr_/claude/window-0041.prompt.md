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
[Block 1436]
རེག་པར་བྱ་བ་མ་ཡིན་པ་ཉིད༌[^1106]དང་། མེད་ན་མི་འབྱུང་བ་ཉིད་དུ་བསྟན་པར་ནི་ནུས་པ་མ་ཡིན་ནོ། །

[Block 1437]
གཅིག་པ་ཉིད་ནི་དཔེའི་སྐྱོན་མ་ཡིན་ནོ་ཞེས་བསྟན་ཟིན་ཏོ། །

[Block 1438]
གཅིག་ཉིད་མ་གྲུབ་པའི་དོན་ནི་དཔེའི་ངེས་པ༌[^1107]མ་ཡིན་ནོ་ཞེས་ཁོ་བོས་བསྟན་ཟིན་ཏོ། །

[Block 1439 [HEADING]]
### རིགས་པ་ཅན་གྱི་དཔེ། ^4-5-0

[Block 1440]
རིགས་པ་ཅན་རྣམས་ན་རེ་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་མཐུན་པ་ལས་ཆོས་དེ་རྟོགས་པའི་དཔེ་དཔེར་བརྗོད་པ་དང་། དེ་བཟློག་པ་ལས་དེ་ཕྱིན་ཅི་ལོག་ལས་སོ་ཞེས་ཟེར་རོ། །

[Block 1441]
དེ་ཡང༌[^1108]གལ་ཏེ་གཏན་ཚིགས་ཀྱི་དོན་ལས་དཔེ་ལོགས་ཤིག་པ་ཡིན་ན་ནི་དཔེ་གཏན་ཚིགས་ཀྱི་དོན་དང་རྗེས་སུ་འབྲེལ་པར་བརྗོད་པར་མི་བྱ་བར་འགྱུར་རོ། །

[Block 1442]
དེ་བཞིན་དུ་བྱས་པའི་ཕྱིར་ན་མི་རྟག་པ་སྟེ། ནམ་མཁའ་བཞིན་ནོ་ཞེས་བྱ་བར་ཡང་དཔེར་འགྱུར་རོ། །

[Block 1443]
དེའི་ཕྱིར་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་མི་མཐུན་པ་དང་། ཆོས་དང་མཐུན་པ་ནི་ཡོད་པ་དང་མཉན་བྱ་ཉིད་དག་ལ་སོགས་པ་ལ་ཡང་ཡོད་པ༌[^1109]ཡིན་ནོ། །

[Block 1444]
གཞན་ཡང་གལ་ཏེ་དཔེས་སྔོན་དུ་ཁྱད་པར་དུ་བྱེད་ན་ནི་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་མཐུན་པ་དང་། ཆོས་དང་མི་མཐུན་པར་འཛིན་པ༌[^1110]ཡིན་ཏེ། གོ་བྱེད་དུ་དེ་མཐོང་མ་ཡིན། །ཕྱི་རོལ་གྱི་དོན་གྱི་རྗེས་ཐོགས་སུ་མ་སྨོས་པའི་དཔེས་ནི་བསྒྲུབ་པར་བྱ་བའི་ཆོས་ལ་གོ་བར་བྱ་བ་ཡིན་ནོ་ཞེས་ཆོས་དེ་རྟོགས་པ་ཉིད་དུ་ཡང་མི་འགྲུབ༌[^1111]པོ། །ཇི་སྟེ་ཆོས་དེ་རྟོགས་པ་ཉིད་གཏན་ཚིགས་ལ་སོགས་པ་ལས་ཕྱིས་ཁྱད་པར་དུ་བྱེད་ན་ནི་དེ་ལྟ༌[^1112]ན་ཡང་། གཉིས་ཀ་སྨོས་པ་དོན་མེད་འགྱུར། །གང་འདི་ཆོས་དེ་རྟོགས་པའི་དཔེ་དག་གོ་ཞེས་གཉིས་ཀ་སྨོས་པ་འདི་དོན་མེད་པ་ཉིད་དུ་འཐོབ་པར་འགྱུར་རོ། །

[Block 1445]
ཇི་ལྟར་ན་དོན་མེད་པའོ༌[^1113]ཞེ་ན་ཆོས་དེ་རྟོག་པ༌[^1114]ཉིད་ཀྱིས་ནི་ཆོས་མཐུན་པ་དང་ལྡན་པའི་དོན་གྱིས༌[^1115]བསྒྲུབ་བྱ་དང་དེ་བཟློག་པའི་ཆོས་དང་ལྡན་པ་ཉིད་འཐོབ་སྟེ། དེ་ལས་གཞན་པའི་ཆོས་ཏེ༌[^1116]རྟོགས་པ་ཉིད་ནི་མེད་དོ། །

[Block 1446]
དཔེ་སྨོས་པ་ཡང་གྲུབ་པའི་ཆོས་དེ་དང་ལྡན་པར་བརྗོད་པ་ནི་དོན་གང་ལ་འཇིག་རྟེན་པས་བཏགས་པའི༌[^1117]བློ་དང་མི་མཐུན་པའི་དཔེ་ཡིན་ནོ། །

[Block 1447]
རེ་ཞིག་ཆོས་དེ་རྟོགས་པ་ཉིད་ནི་རིགས་པ་མ་ཡིན་ཏེ། རྣམ་གྲངས་ཀྱི་ཕྱིར་ཡན་ལག་ཐམས་ཅད་ཀྱི་བསྒྲུབ་པར་བྱ་བའི་ཆོས་རྟོགས་པ་ཉིད་རྣམ་གྲངས་ཡིན་པས་ན་དེ་ཐོབ་པར་ནུས་པ་མ་ཡིན་ནོ། །

[Block 1448]
དེ་ཉིད་ཀྱི་ཕྱིར་ཡང་གཅིག་ཉིད་བརྗོད་པར་བྱ་སྟེ་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་མཐུན་པའམ། ཆོས་དང་མི་མཐུན་པ་ལས་ཀྱང་དེ་ཉིད་གྲུབ་པའི༌[^1118]ཕྱིར་ལ་དེ་ལས་གཞན་པའི་ཆོས་དེ་རྟོགས་པ་ཉིད་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 1449]
ཡང་ན་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་མཐུན་པ་ལས་ཆོས་དེའི་ཞེས་པ་ནི་བསྒྲུབ་བྱའི་ཆོས་ཅན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ་ཞེ་ན། དེ་ལྟ་ན་ཡང་གཉིས་ཀ་ལས་ཆོས་ཅན་ཉིད་དུ་འགྱུར་གྱི་དོན་རྟོགས་པ་སྨོས་པ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 1450]
གལ་ཏེ་ཁྱོད་ཀྱིས་བསྒྲུབ་པར་བྱ་བ་དང་སྒྲུབ་པར་བྱེད་པའི་ཆོས་དང་ལྡན་པའི་དཔེ་ལས་དོན་ཡིན་ན་ནི་གཉིས་ཀའི་ཆོས་དང་ལྡན་པས་ཀྱང་ངག་གི་དོན་མཇུག་བསྡུས་པ་ལས་བསྒྲུབ་པར་བྱ་བའི་དོན་རྟོགས་པར་མི་ནུས་སོ་ཞེས་སྔར་བརྗོད་ཟིན་ཏོ། །

[Block 1451]
འདིར་ཡང་སྒྲུབ་པར་བྱེད་པས་འཇལ་བར་བྱེད་པ་ཉིད་ལ་བསྒྲུབ་པར་བྱ་བའི་ཆོས་ཐུག་པ་མེད་པའོ་ཞེས་བརྗོད་དོ། །

[Block 1452]
དཔེ་སྨོས་པའི་འབྲས་བུ་གྲུབ་པའི་ཆོས་སྒྲུབ་པའི་དོན་དུ་ཡང་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གཞན་ལས་གྲུབ་ཕྱིར་འབྲས་བུ་བསལ༌[^1119]བར་བྱེད་པའི་རྒྱུ་ལས་ཀྱང་དེ་བཞིན་དུ་གྲུབ་པོ། །གཞན་དུ་ན༌[^1120]འདིར་ཆོས་མཐུན་པའི་དཔེར་བརྗོད་ལས་གང་གྲུབ་པ་དེ་འབྲས་བུ་མ་ཡིན་ནོ། །

[Block 1453 [HEADING]]
#### ཆོས་དེ་རྟོགས་པ་ཉིད་དཔེའི་དཔེར་བརྗོད། ^4-5-1-0

[Block 1454]
གཞན་དག་ནི་ཆོས་དེ་རྟོགས་པ་ཉིད་དཔེའི་དཔེར་བརྗོད་པ་ཡིན་ནོ་ཞེས་གླེང་བརྗོད༌[^1121]བྱེད་དོ། །

[Block 1455]
དེ་ལ་ཡང་། བསྒྲུབ་བྱའི་ཆོས་དང་སྦྱར་མི་བྱ། །རང༌[^1122]གི་སྒྲས་ནི་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་མཐུན་པ་དང་། ཆོས་དང་མི་མཐུན་པ་ཡང་སྟེ། དེ་གོ་བར་བྱེད་པ་ཉིད་དུ་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1456]
གང་ལ་གང་གིས་གང་གི་གང་ཞིག་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་སྦྱར་བར་མི་བྱ་ཞེ་ན། གང་ཆོས་མཐུན་པའི་དཔེར་བརྗོད་པ་ལས་ཞེས་བྱ་བ་འདི་ལ། དཔེར༌[^1123]བརྗོད་ཀྱིས་བསྒྲུབ་པར་བྱ་བའི་བྱས་པ་ཉིད་ལ་སོགས་པས་ཆོས་དང་མཐུན་པར་སྦྱར་བར་མི་བྱའོ། །

[Block 1457]
བུམ་པས་ནི་བསྒྲུབ་བྱའི་བྱས་པ་ལ་སོགས་པ༌[^1124]ཆོས་དང་མཐུན་པ་བུམ་པའི་བསྒྲུབ་པར་བྱ་བའི་ཆོས་རྟོགས་པ་ཉིད་ཀྱི་བྱ་བ་དང་བྱེད་པ་པོའི་འབྲལ་པ༌[^1125]ལས་ཡིན་གྱི། ཆོས་གཞན་ཡོད་པ་ལ་སོགས་པས་བསྒྲུབ་བྱའི་ཆོས་དང་མཐུན་པ་ནི་མ་ཡིན་ནོ། །

[Block 1458]
ཚིག་གཉིས་པོ་ཡང་དོན་གྱི་དཔེ་བརྗོད་དུ་བསྟན་པའི་ཕྱིར་ངག་གི་ཆ་ཤས་ཉིད་ཉམས་པ་ཡིན་པས་དཔེར༌[^1126]བརྗོད་ཀྱང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1459 [HEADING]]
#### ཉེ་བར་སྦྱོར་བ། ^4-5-2-0

[Block 1460 [VERSE]]
དཔེ་བརྗོད་པ་ལ༌[^1127]ལྟོས་ནས་ནི། །
དེ་བཞིན་ནོ་ཞེས་ཉེར་སྦྱོར་བ། །
བསྒྲུབ་བྱ་ལ་ཡང་དེ་བཞིན་ཞེས། །
ཉེ་བར་སྦྱོར་བ་རིགས་མ་ཡིན། །

[Block 1461]
འདི་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས༌[^1128]བྱས་པའི་སྤྱིའི་ཉེ་བར་སྦྱོར་བའམ་དེའི་བྱེ་བྲག་ཡིན་ཡང་རུང་སྟེ། རིགས་པ་མ་ཡིན་ནོ། །

[Block 1462]
ཐམས་ཅད་ཀྱི་སྤྱི་ནི་དེ་བཞིན་ནོ་ཞེས་བསྟན་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1463]
གལ་ཏེ་དེ་ལྟ་ན་ཡང་དེ་ལ་རེ་ཞིག་བྱས་པ་ནི་བུམ་པ་ལྟ་བུའོ་ཞེས་སྦྱོར་གྱི། ནམ་མཁའ་ལ་སོགས་པ་ལྟ་བུར་མ་བྱས་པའོ།[^1129] །

[Block 1464]
མི་སྦྱོར་རོ་ཞེ་ན། དེ་ནི། སྤྱི་ཉིད་གཏན་ཚིགས་ཉིད་དུ་བརྗོད། །སྤྱི་ནི་བྱས་པའི་ཕྱིར་ཞེས་བྱ་བ་འདི་ཉིད་ཀྱིས་བརྗོད་པ་ཡིན་ཏེ། སྒྲའིའོ་ཞེས་འབྲེལ་པའི་ཕྱིར་རོ། །

[Block 1465]
དཔེ་དང་བསྒྲུབ་པར་བྱ་བའི་དོན་གཅིག་པ་ཉིད་ནི་མ་ཡིན་ཏེ། དེ་བཞིན་དུ་མི་རྟག་པ་ཉིད་གྲུབ་པ་ཞེས་ཕྱི་རོལ་གྱི་དོན་ཉེ་བར་མི་སྦྱོར་རོ། །

[Block 1466]
དེ་ལྟ་མ་ཡིན་ན་ཁྱད་པར་མེད་པའི་སྤྱི་ཉིད་ལན་དུ་འགྱུར་རོ། །

[Block 1467]
ཅི་སྟེ་བྱས་པ་ཉིད་དུ་གྲུབ་པ་ལ༌[^1130]བྱས་པ་འདི་བུམ་པ་ལྟ་བུ་ཡིན་གྱི་སྣམ་བུ་ལ་སོགས་པ་ལྟ་བུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱེ་བྲག་ཉེ་བར་སྦྱར་བ་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ་གང་གི་ཕྱིར། བྱེ་བྲག་རང་ལ་བརྟེན༌[^1131]རྗེས་འབྲང་། །རང་ལ་བརྟེན་པར་ངེས་པ་ནི་བྱེ་བྲག་ཡིན་པས་བུམ་པ་ལ་སོགས་པ་ལྟ་བུ་ནི་མ་ཡིན་ཏེ། བྱས་པ་སྒྲ་མ་ཡིན་པ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 1468]
དེ་ལྟ་ན་ཡང་ཉེ་བར་སྦྱར་བ་མེད་དོ། །

[Block 1469]
ཆོས་མི་མཐུན་པའི༌[^1132]ཉེ་བར་སྦྱར་བ་ནི་ནམ་མཁའ་བཞིན་དུ་མ་བྱས་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1470]
དེ་ལ་གལ་ཏེ་དགག་པ༌[^1133]གཉིས་ཀས་བྱས་པ་ཉིད་འགེགས་པ་ཙམ་དུ་བརྗོད་པ་ཡིན་ན་ནི། གཏན་ཚིགས་དེའི་དོན་དུ་མི་འགྱུར་རོ། །

[Block 1471]
གལ་ཏེ་བྱས་པ་ནི་མི་འགེགས་ཀྱི་དེ་དང་ལྷན་ཅིག་ཏུ་རྒྱུ་བའི་རྟག་པ་འགེགས་པའི་དོན་དུ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟར་ཡང་མ་ཡིན་ཏེ། གང་གི་ཕྱིར། གཉེན་པོའི་ཕྱོགས་དང་ལྡན་མ་ཡིན། །གཏན་ཚིགས་ཉིད་དུ་མ་བརྗོད་པའི་བྱས་པའི་སྤྱི་བརྗོད་པ་ཡིན་ཏེ། དང་གི་སྒྲ་སྨོས་པས་བྱས་པ་ཉིད་ཡོད་པས་ན་གཉེན་པོའི་ཕྱོགས་ཀྱི་གོ་སྐབས་ཡོད་པ་མ་ཡིན་ན་གང་དེ་དགག་པར༌[^1134]བྱ་བའི་དོན་དུ་ཆོས་མི་མཐུན་པ་ཉེ་བར་སྦྱོར་བར་བྱེད་དེ་མ་བྱས་པ་དང་ལྷན་ཅིག་ཏུ་རྟག་པ་ཉིད་དགག་པར་བྱ་བའི་དོན་དུ་ཡང་ཉེ་བར་སྦྱོར་བར་མི་བརྗོད་དོ། །

[Block 1472]
དེ་ལྟ་བས་ན་གཉེན་པོའི་ཕྱོགས་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 1473]
ཆོས་མཐུན་པའི་སྒོ་ནས་བྱས་པ་ཉིད་ཀྱིས༌[^1135]མི་རྟག་པ་ཉིད་རྟོགས་པ་ནི༌[^1136]མེད་དོ། །

[Block 1474]
དེའི་གཉེན་པོའི་ཕྱོགས་རྟག་པ་ཉིད་དང་ལྡན་པར་ཡོད་པ་གང་གིས་འགེགས་པར་བྱེད། ཅི་སྟེ་ཡང་མ་གྲུབ་པའི་ཕྱིར་རྟག་པ་ཉིད་ལ་ཆོས་མི་མཐུན་པ་ཙམ་གྱིས་རྟག་པ་ཉིད་འགེགས་སོ་ཞེ་ན། དེ་ལྟ༌[^1137]ན་ཡང་། ཁྱད་པར་སྒོ་ནས་ཀྱང་དེར་འགྱུར། །གལ་ཏེ་ཆོས་མཐུན་པ༌[^1138]མ་བརྗོད་པར་ཁྱད་པར་གྱི་སྒོ་ནས་ཀྱང་སྟེ་དེ་ཆོས་དེའི་གཉེན་པོའི་ཕྱོགས་དང་ལྷན་ཅིག་ཏུ་རྒྱུ་བ་འགེགས་པ་ཡིན་པར་འགྱུར་ཏེ། དཔེར་ན་མཉན་བྱ་ཡིན་པའི་ཕྱིར་སྒྲ་མི་རྟག་གོ་ཞེས་པ་ལྟ་བུའོ། །

[Block 1475]
བུམ་པ་ལ་སོགས་པ་མི་རྟག་པ་ལ་མཉན་པར་བྱ༌[^1139]བ་མ་ཡིན་པ་དང་ལྷན་ཅིག་ཏུ་རྒྱུ་བ་མི་རྟག་པ་ཉིད་བཀག་པའི་ཕྱིར། མི་འདོད་པའི་རྟག་པ་ཉིད་གྲུབ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
