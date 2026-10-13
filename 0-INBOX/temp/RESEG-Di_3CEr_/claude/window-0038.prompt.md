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
དེ་སྟེ༌[^1030]ཡོད་པའི་དངོས་པོ་ཙམ་ཡིན་ན་ནི་བུམ་པ་མི་རྟག་པ་ཉིད་ཀྱང་རྩོལ་བ་ལས་བྱུང་བ༌[^1031]མེད་ན་མི་འབྱུང་བར༌[^1032]འགྱུར་བས༌[^1033]ན། དེ་ཕྱི་རོལ་གྱི་དོན་ལ་ལྟོས་པ་ཉིད་དུ་སྟོན་ཏོ་ཞེས་ནི་བརྗོད་པར་མི་བྱའོ། །

[Block 1332]
ཁྱབ་པ་ཉིད་ཀྱི་གཏན་ཚིགས་བསྒྲུབ་བྱ་རྗེས་སུ་སྒྲུབ་པོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1333]
འདིའི་གནས་སྐབས་སུ་ནི་དོན་གྱི་ཤུགས་ཁོ་ནས་བསྒྲུབ་བྱ་མེད་པ་ལ་གཏན་ཚིགས་མེད་པར་བརྗོད་པ་ཡིན་པས་ཆོས་མི་མཐུན་པའི་དཔེའི་སྦྱོར་བ་ནི་མི་བྱའོ། །

[Block 1334]
གང་གི་ཚེ་དཔེ་གཉིས་ཀ་སྦྱོར་བར་བྱེད་པ་དེའི་ཚེ་ནི་མི༌[^1034]མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་ཙམ་བསྟན་པ་ཡིན་ལ། ཁྱབ་པ་ནི་བསྒྲུབ་བྱ་མེད་པ་ལ་མེད་པ་བསྟན་པ་ཡིན་པས་འདི་སྐད་དུ་ཡང༌[^1035]བསྒྲུབ་བྱ་སྒྲུབ་པར་བྱེད་པའི་རྟགས་ཆོས་མཐུན་པ་དང་བཅས་པ་སྟོན་ཏོ་ཞེས་བརྗོད་པར་མི་བྱའོ། །

[Block 1335]
དེ་ལྟར་ཡང་གཏན་ཚིགས་ཀྱི༌[^1036]བསྒྲུབ་བྱ་རྗེས་སུ་སྒྲུབ་པའི་འགེགས་པའི་དོན་དུ་འགྱུར་གྱི་དོན་འགོག་པའི་དོན་དུ་ནི་མི་འགྱུར་ཏེ། མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་དང་གཉིས་ཀ་ཞེས་སྨྲས་པའི་ཕྱིར་རོ། །

[Block 1336]
འདིར་ནི་གཏན་ཚིགས་ལྷག་མ་བསྟན་པར་བྱ་སྟེ། ཕྱོགས་ཀྱི་ཆོས་ནི་གཏན་ཚིགས་ཉིད་ཀྱིས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1337]
དོན་ནི་གདོན་མི་ཟ་བར་མཐུན་པའི་ཕྱོགས་ཁོ་ན་ལ་ཡོད་ཅེས་ངེས་པར་གཟུང་བར་བྱའོ་ཞེ་ན། དེ་ལྟ་ན་ནི་མཐུན་པའི་ཕྱོགས་ཁོ་ན་ལ་ཡོད་ཅེས་པས་མི་མཐུན་པའི་ཕྱོགས་ལ་མཐུན་པའི་ཕྱོགས་མེད་པ་ཉིད༌[^1037]བཀག་པ་ཐོབ་པར༌[^1038]འགྱུར་བའི་དོན་དུ་འགྱུར་རོ། །

[Block 1338]
དེ་མེད་པ་ལ་མེད་པ་མེད་པ་ཉིད་ལ་མེད་པ་ཡིན་གྱི་མི་མཐུན་པའི་ཕྱོགས་བདག་མེད་པ་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1339]
དེ་བཞིན་དུ་འདིར་ཡང་བསྒྲུབ་པར་བྱ་བ་མེད་པ་ཁོ་ན་མེད་པ་ཡིན་གྱི་གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1340]
མི་མཐུན་པའི་ཕྱོགས་བསྒྲུབ་བྱ་གོ་བར་བྱེད་ན༌[^1039]ནི་རག་ན་གཏན་ཚིགས་དུ་མ༌[^1040]འགལ་བ་དང་མི་འགལ་བ་སྟེ། ཡོད་བཞིན་པའི་འགལ་བ་དང་གཏན་ཚིགས་ཉིད་དུ༌[^1041]འཆད་པ་དེ་དག་ཉིད་གང་འཆད་པར་འགྱུར་བའི་ཆོས་མཐུན་པའི་དཔེ་བརྗོད་པའི་མ་ངེས་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1341]
དེ་ལ་ལུས་ཅན་མ་ཡིན་པ་ཉིད་རྟག་པ་ལ་མེད་པ་ཡང་ཡོད་པའི་དངོས་པོ་ལས་སོ་ཞེས་བསྟན་པར་བྱའི༌[^1042]གཞན་པ་དང་འགལ་བ་ཉིད་མེད་པའི་དངོས་པོ་ལས་སོ་ཞེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1342]
དེ་ལྟར་བྱས་ནས་རྩོལ་བ་ལས་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་རྩོལ་བ་ལས་བྱུང་བ་དང་། མི་རྟག་པ་ཉིད་རྗེས་སུ་འབྲེལ་པའི་ཕྱིར་མི་རྟག་པ་མེད་པས་གཏན་ཚིགས་མེད་པར་བསྟན་པར་བྱའོ། །

[Block 1343]
ཆོས་མི་མཐུན་པའི་དཔེ་ནི་རྟག་པ་ལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1344]
མེད་པ་ཉིད་གཏན་ཚིགས་སུ་བསྟན་གྱི་བཟློག་པ་ནི་མ་ཡིན་ནོ། །

[Block 1345]
མ་བྱས་པའི་ཕྱིར་རྟག་གོ་ཞེས་མ་ཡིན་དུ་ཆུག །འདིར་ནམ་མཁའ་ལ་སོགས་པ་རྟག་པ་ཉིད་དུ་དམ་བཅས་པ་ཉིད་ཀྱིས་མ་བྱས་པ་ཉིད་བསྒྲུབ་པ༌[^1043]ཡིན་ནོ། །

[Block 1346]
དེ་ལྟ་ན་ནི་གཉེན་པོའི་ཕྱོགས་ཀྱི་འགལ་བ་དང་མ་ངེས་པ་གཉིས་ཀ་བརྗོད་པར་བྱ་བའི་ཕྱིར་བརྗོད་པར་མི་བྱའོ། །

[Block 1347]
རེ་རེར་བརྗོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1348]
དེར་ཐལ་བར་འགྱུར་བས་སོ། །

[Block 1349]
དེ་ལྟ་ན་ནི་འཇིག་རྟེན་པའི་སྦྱོར་བ་རྗེས་སུ་བཟུང་ནས་བརྗོད་ཀྱི། བསྒྲུབ་པར་བྱ་བའི་ཆོས་ཇི་ལྟར་བའི་གཏན་ཚིགས་ཀྱི་མཚན་ཉིད་ནི་མ་ཡིན་ཏེ། མ་ངེས་པར་ཐལ་བར་འགྱུར་བས་སོ། །

[Block 1350 [HEADING]]
#### དཔེར་བརྗོད་གཉིས་སུ་བྱ་བ། ^4-1-2-0

[Block 1351]
ཅི་ཡང་རྣམ་པ་གཉིས་ཀྱང་དཔེའི་ཚིག་ཏུ་བསྒྲུབ་པ༌[^1044]ཡིན་ནམ། འོན་ཏེ་གཞན་ཉིད་གཅིག་ཡིན་ཞེ་ན། གཏན་ཚིགས་ཡིན་པའི་ཕྱིར་རྣམ་པ་གཉིས་ཉིད་དོ་ཞེས་བརྗོད་དོ། །

[Block 1352]
དེ་ལྟ་མ་ཡིན་ན།

[Block 1353 [VERSE]]
ཐུན་མོང་དང་ནི་ཁྱད་པར་ཉིད། །
འགལ་བའང་སྒྲུབ་བྱེད་ཉིད་དུ་འགྱུར། །
རེ་རེར་གཉིས་ཀ་མ་བརྗོད་ན།[^1045] །
དེས་ན་དཔེར་བརྗོད་གཉིས་སུ་བྱ། །

[Block 1354]
གལ་ཏེ་ཆོས་མཐུན་པ་ཉིད་རྗོད་པར་བྱེད་ན་དེ་མེད་པ་ལའང་འགྱུར་རོ་ཞེས་ཐུན་མོང་པ་ཉིད་གཏན་ཚིགས་སུ་དོགས་པ་སྐྱེད༌[^1046]དོ། །

[Block 1355]
གལ་ཏེ་ཆོས་མི་མཐུན་པ་ཉིད་རྗོད་པར་བྱེད་ན་ནི་བསྒྲུབ་པར་བྱ་བའི་རིགས་ལ་ཡང་མེད་པས་ཐུན་མོང་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 1356]
ཅི་སྟེ་གཉིས་ཀ་རྗོད་པར་མི་བྱེད་ན་ནི་དེ་ལ་མཐུན་པའི༌[^1047]ཕྱོགས་ལ་མི་འགྱུར་ལ། རིགས་མི་མཐུན་པའི་ཕྱོགས་ལ་འགྱུར་བའི་ཕྱིར་འགལ་བར་འགྱུར་རོ། །

[Block 1357]
དེའི་ཕྱིར་གདོན་མི་ཟ་བར་གཉེན་པོའི་ཕྱོགས་ཀྱིས་འགལ་བ་དང་མ་ངེས་པ་གཉིས་ཀ་བརྗོད་པར་བྱའོ། །

[Block 1358]
འབའ་ཞིག༌[^1048]ཏུ་ཅུང་ཟད་གྲུབ་པ་ཉིད་དུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 1359]
གང་ཡང་རུང་བ་གཅིག་བརྗོད་པས་ཀྱང་སྒྲུབ་བྱེད་དུ་འགྱུར་ཏེ། སྒྲ་བཞིན་དུ་དོན་གཉིས་རྟོགས་པའི་ཕྱིར་གང་ཡང་རུང་བ་གཅིག་གིས་གཉིས་ཀ་བསྟན་པའི་ཕྱིར་དོན་གྱི་ཤུགས་ཀྱིས་གཉིས་བརྗོད་པ་ཡིན་ནོ། །

[Block 1360]
དོན་རྗེས་སུ་དཔོག་པ་ལ་ཡང་རིགས་པ་དེ་ཉིད་བལྟའོ། །

[Block 1361]
གང་རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་རྟགས་འདི་ངེས་པར་གཟུང་བར་བྱས་ནས་གཞན་ལ་དེའི་རིགས་ཡོད་པ་དྲན་པར་བྱས་ཏེ།[^1049] མེད་པ་ལ་མེད་པ་ཉིད་ཀྱིས༌[^1050]བདག་ཉིད་ཀྱིས༌[^1051]ངེས་པར་སྐྱེད༌[^1052]པར་བྱེད་དོ། །

[Block 1362]
དེ་ཉིད་ཀྱི་ཕྱིར།

[Block 1363]
རང་གི༌[^1053]

[Block 1364 [HEADING]]
#### རྗེས་སུ་དཔོག་པར་བྱེད་པའི་ཡན་ལག། ^4-1-3-0

[Block 1365 [VERSE]]
ངེས་པ་བཞིན་གཞན་ལ། །
ངེས་པ་བསྐྱེད་པར་འདོད་པ་ཡིས། །
ཕྱོགས་ཆོས་ཉིད་དང་འབྲེལ་པ༌[^1054]དང་། །
བསྒྲུབ་བྱ་བརྗོད་བྱ་གཞན་རྣམས་སྤངས།[^1055] །

[Block 1366]
འདི་ལྟར༌[^1056]ཕྱོགས་ཀྱི་ཆོས་ཉིད་བསྟན་པའི་དོན་དུ་གཏན་ཚིགས་ཀྱི་ཚིག་ཡིན་ནོ། །

[Block 1367]
དེ་རྗེས་སུ་དཔག་པར་བྱ་བ་དང་། མེད་ན་མི་འབྱུང་བ་ཉིད་དུ་བསྟན་པའི་དོན་དུ་དཔེའི་ཚིག་ཡིན་ནོ། །

[Block 1368]
རྗེས་སུ་དཔག་པར་བྱ་བ་བསྟན་པའི་དོན་དུ་ཕྱོགས་ཀྱི་ཚིག་བརྗོད་དོ། །

[Block 1369]
འདི་རྗེས་སུ་དཔོག་པར་བྱེད་པའི་ཡན་ལག་གཞན་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1370]
དེས་ན་གཞན་གྱི་ཤེས་པར་འདོད་པ་ལ་སོགས་པའི་ཡན་ལག་ཉེ་བར་སྦྱར་བ་དང་མཇུག་བསྡུ་བ་དག་ནི་འདིར་བསལ་བ་ཡིན་ནོ། །
--- END BLOCKS ---
