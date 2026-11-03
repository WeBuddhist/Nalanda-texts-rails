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
ཆོས་མཐུན་པ་ཉིད་ཅན་གྱི་སྦྱོར་བ་ལ་ཡང་དོན་གྱིས་ཆོས་མི་མཐུན་པ་ཉིད་ཅན་རྟོགས་པར་འགྱུར་ཏེ། དེ་མེད་ན་བསྒྲུབ་པར་བྱ་བ་དང་གཏན་ཚིགས་རྗེས་སུ་འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1332]
དེ་བཞིན་དུ་ཆོས་མི་མཐུན་པ་ཉིད་ཅན་གྱི༌[^1027]རྗེས་སུ་འགྲོ་བ༌[^1028]རྟོགས་པར་འགྱུར་ཏེ། དེ་མེད་ན་ནི་བསྒྲུབ་པར་བྱ་བ་མེད་ན་གཏན་ཚིགས་མེད་པར་ཐེ་ཚོམ་དུ་འགྱུར་ཞེས་རྒྱས་པར་འཆད་པར་འགྱུར་རོ། །

[Block 1333]
དཔེར་ན་མི་རྟག་ཉིད་བྱས་པའམ། འཇིག་བྱེད་མ་བྱས་པ་ལྟ་བུའོ། །

[Block 1334]
འདིས་ནི་འདི་གཉིས་ཀྱི་དཔེ་བསྟན་ཏོ། །

[Block 1335]
དེ་ལ་རྗེས་སུ་འགྲོ་བ་ཅན་ནི་གང་ཅུང་ཟད་བྱས་པ་དེ་ཐམས་ཅད་ནི་མི་རྟག་པ་སྟེ། དཔེར་ན་བུམ་པ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 1336]
སྒྲ་ཡང་བྱས་པ་ཡིན་པ་དེ་ལྟ་ན་བྱས་པ་ཉིད་ལ་མི་རྟག་པ་ཉིད་ཀྱིས་ཁྱབ་པ་བསྟན་པས་སྒྲ་ཡང་བྱས་པ་ཉིད་དུ་བརྗོད་པའི་ཤུགས་ལས་སྒྲ་མི་རྟག་ཅེས་བྱ་བར་འགྱུར་བ་དེ་བས་ན་འདིར་གདོན་མི་ཟ་བར་ཕྱོགས་བསྟན་པར་བྱ་བ་མ༌[^1029]ཡིན་ནོ། །

[Block 1337]
འདི་ནི་རྗེས་སུ་འགྲོ་བ་ཅན་གྱི་སྦྱོར་བའོ། །

[Block 1338]
ལྡོག་པ་ཡང་མི་རྟག་པ་ཉིད་མེད་པ་ལ་བྱས་པ་ཉིད་མེད་དེ། སྒྲ་ནི་བྱས་པ་ཡིན་པས་དེའི་རང་བཞིན་ཉིད་དུ་གྲུབ་པ་ཡིན་ཏེ། དེ་མེད་ན་བྱས་པ་ཉིད་མི་འབྱུང་བས་སྒྲ་ལ་ཡོད་པ་ཉིད་དུ་བསྟན་པ་ན། དེའི་བདག་ཉིད་ཡོད་པ་ཉིད༌[^1030]ཀྱི་ངོ་བོ་ཤུགས་ཀྱིས་གྲུབ་པའི་ཕྱིར་སྔ་མ་བཞིན་དུ་དམ་བཅས་པའི་ཚིག་མ་བྱས་པ་ཡིན་ནོ། །

[Block 1339]
རྗེས་སུ་འགྲོ་བ་ནི་དོན་གྱིས་གོ་བས༌[^1031]གྲུབ་པ་ཡིན་ཏེ། དེའི་བདག་ཉིད་ཡིན་པ་ངེས་པ་ནི་དེ་ལོག་པ༌[^1032]ནི༌[^1033]ལྡོག་པ་དེའི་ཕྱིར། ངེས་པ་རབ་ཏུ་བསྒྲུབས་པས་ལྡོག་པ་བརྗོད་པར་བྱའོ། །

[Block 1340]
གལ་ཏེ་དེ་གྲུབ་པ་ན་དེའི་བདག་ཉིད་དུ་ངེས་པ་དོན་གྱིས་འཕངས་པའི་ཕྱིར་རྗེས་སུ་འགྲོ་བ་གྲུབ་པ་ཡིན་ནོ། །

[Block 1341]
ད་ནི་ཇི་ལྟར་བྱས་པ་ནི་གདོན་མི་ཟ་བར་མི་རྟག་པ་ཡིན་ནོ་ཞེས་གང་གིས་དེ་སྐད་དུ་བརྗོད་པར་བྱ་ཞེ་ན། འདི་ལྟར།

[Block 1342]
རང་བཞིན་ཡིན་ཕྱིར་རྗེས་འབྲེལ་ཉིད། །འཇིག་པ་ཡི་ནི་རྒྱུ་མིན་ཕྱིར། །

[Block 1343]
དངོས་པོ་འཇིག་པའི་ངང་ཚུལ་ཅན་དེའི་ངོ་བོ་ནི་རྒྱུ་ལ་ལྟོས་པ་མ་ཡིན་ཏེ། རང་གི་རྒྱུ་ཉིད་ལས་འཇིག་པའི་ངང་ཚུལ་ཅན་དུ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1344]
དེ་བས་ན་གང་ཅུང་ཟད་བྱས་པ་དེ་ནི་རང་བཞིན་གྱིས་འཇིག་པའི་ངང་ཚུལ་ཅན་ཡིན་ནོ། །

[Block 1345 [VERSE]]
[^1034]དངོས་པོ་ལྟོས་དང་བཅས་རྣམས་ནི། །
ངེས་པར་འབྱུང་བ་ཅན་མི་མཐོང་། །

[Block 1346]
དངོས་པོ་འཇིག་པ་ཡང་ལྟོས་པ་མེད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1347]
ལྟོས་པ་དང་བཅས་པ་ཉིད་ཡིན་ན་ནི་བུམ་པ་ལ་སོགས་པ་འགའ་ཞིག་རྟག་པ་ཉིད་དུ་ཡང་འགྱུར་རོ། །

[Block 1348]
གང་གིས།

[Block 1349 [VERSE]]
དེ་རྒྱུ་མང་པོ་ཡོད་ན་ཡང་། །
འགའ་ཞིག་ཏུ་ཡང་མི་སྲིད་འགྱུར། །

[Block 1350]
གལ་ཏེ་འཇིག་པའི་རྒྱུ་མང་པོ་ཡོད་ན་དེ་དག་གི་ཡང་རང་གི་རྐྱེན་དག་ལ་ལྟོས་པ་ཐག་ཉེ་བ༌[^1035]ཅན་ཉིད་ཡིན་པའི་ཕྱིར། གདོན་མི་ཟ་བར་ཐག་ཉེ་བ་མ་ཡིན་པས་འགའ་ཞིག་ཀྱང་ཞིག་པར་མི་འགྱུར་རོ། །

[Block 1351]
རྒྱུ་དག་ནི་གདོན་མི་ཟ་བར་འབྲས་བུ་དང་ལྡན་པ་མ་ཡིན་ཏེ། མ་ཚང་བ་དང་གགས་བྱེད་པ་སྲིད་པའི་ཕྱིར་རོ། །

[Block 1352]
དེ་བས༌[^1036]ན་འབྲས་གཞན་མེད་པའི་ཕྱིར།

[Block 1353 [VERSE]]
[^1037]འཇིག་པ་རྒྱུ་ལྡན་སྨྲ་རྣམས་ཀྱི། །
འཇིག་པའི་རྒྱུ་ནི་ཐམས་ཅད་དག །
འཁྲུལ་བ་ཉིད་དུ་བཤད་པ་ཡིན། །

[Block 1354]
ཞེས་བྱ་བ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 1355]
དེ་བས་ན་ངོ་བོ་འདི་དེའི་ངོ་བོ་ལྟོས་པ་མེད་པ་ཅན་ནི་དེའི་ངོ་བོ་ལ་ངེས་པ་ཡིན་ཏེ། རྒྱུ་མ་ལུས་པ༌[^1038]ཚོགས་པས་འབྲས་བུ་བསྐྱེད་པ་ན་གགས་བྱེད་པ་ཅན་མི་སྲིད་པ་བཞིན་ནོ། །

[Block 1356]
འགའ་ཞིག་འགའ་ཞིག་ལ་ལྟོས་པ་མེད་དུ་ཟིན་ཀྱང་གདོན་མི་ཟ་བར་དེའི་ངོ་བོ་མེད་པ་མ་ཡིན་ནམ། ས་དང་ས་བོན་དང་ཆུ་དག་གི་ཚོགས་པ་དག་ཀྱང་འགའ་ཞིག་ཏུ་མྱུ་གུ་མི་བསྐྱེད་པའི་ཕྱིར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ལ་ཡང་རྒྱུན༌[^1039]འགྱུར་བ་ལ་ལྟོས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1357]
འདི་ལྟར་ངོ་བོ་ནི་འགའ་ཞིག་ལ་ཡང་ལྟོས་པ་མེད་པ་ཡིན་ནོ། །

[Block 1358]
དེ་ལ་ཡང་རྒྱུའི་ཚོགས་པ་ཐ་མ་འབྲས་བུ་བསྐྱེད་པའི་ཕྱིར། བར་ཆད་མེད་པ་གང་ཡིན་པ་དེ་ནི་འབྲས་བུ་དང་ལྡན་པ་ཁོ་ན་ཡིན་ཏེ། དེ་ཉིད་ཀྱང་དེའི་ནང་ནས་མྱུ་གུའི་རྒྱུ་ཡིན་ན། གཞན་སྔར་གྱུར་པའི་དེའི་དོན་ཉིད་ཡིན་ནོ། །

[Block 1359]
དེར་དེ་ལ་འགའ་ཞིག་གགས་བྱེད་པར་ནུས་པ་མ་ཡིན་ཏེ། ངོ་བོ་གཅིག་ལ་མི་འགྱུར་བར་མི་བསྐྱེད་པའི་ཕྱིར་དང་། བསྐྱེད་ན་གཅིག་པ་ཉིད་ཉམས་པའི་ཕྱིར་རོ། །

[Block 1360]
དེའི་བདག་ཉིད་ལས་རྒྱུ་འཕོ་བ་མེད་པ་ནི་དེ་སྐྱེད་པར་བྱེད་པ་ལ་གགས་བྱེད་པའི་རྒྱུ་མི་མཐུན་པ་མི་བྱེད་པ་ནི་གགས་བྱེད༌[^1040]པ་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1361]
ནས་ཀྱི་ས་བོན་ལ་སོགས་པ་དག་ཀྱང་སཱ་ལུའི་མྱུ་གུ་བསྐྱེད་པ་ལ་ལྟོས་པ་དང་བཅས་པ་མེད་པ་མ་ཡིན་ནམ། དེ་སྐྱེད་པར་བྱེད་པའི་རྐྱེན་དག་ནི་འགའ་ཞིག་ཏུ་དེ་ལ་ཡང་ཉེ་བའི་ཕྱིར་རོ་ཞེ་ན། ཇི་ལྟར་ལྟོས་པ་མེད་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་དེ་དག་ལ་སཱ་ལུའི་ས་བོན་གང་ཡིན་པ་དེ་ཉིད་སྐྱེད་པར་བྱེད་པའི་རང་བཞིན་ཏེ། དེ་མེད་པའི་ཕྱིར་དེའི་རང༌[^1041]ལ་ལྟོས་པ་ཡིན་ནོ། །

[Block 1362]
འོན་ཏེ་དེ་ལྟ་ཡིན་ན་འགའ་ཞིག་བྱས་པ་འམ་ཡོད་པ་ཉིད་ལ་ཡང་འཇིག་པའི་རང་བཞིན་གང་ཡིན་པ་དེ་ཉིད་ཡོད་པ་མ་ཡིན་པ་དེ་བས་ན། དེའི་རང་བཞིན་ལ་ལྟོས་པ་ཉིད་ཀྱི་ཕྱིར་འཇིག་པ་དག་མ་ཡིན་ནོ། །

[Block 1363]
སཱ་ལུའི་ས་བོན་ལ་སོགས་པ་དག་གི་རང་བཞིན་དེ་ནི༌[^1042]རང་གི་རྒྱུ་ཡིན་པའི་ཕྱིར། དེའི་རྒྱུ་མ་ཡིན་པ་གང་ཡིན་པ་དེ་ནི་དེའི་རང་བཞིན་དུ་མི་འགྱུར་རོ། །

[Block 1364]
རྒྱུ་དེའི་ནུས་པ་ངེས་པ༌[^1043]ཡང་རང་རང་གི་ངོ་བོས་ཁོང་དུ་ཆུད་པ་ཉིད་ཡིན་ནོ། །

[Block 1365]
རང་བཞིན་ངེས་པ་ཡང་དོན་རྣམས་ལ་གློ་བུར་དུ་རིགས་པ་མ་ཡིན་ཏེ། ལྟོས་པ་མེད་པ་ནི་ཡུལ་དང་དུས་དང་རྫས་ངེས་པ་ལ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1366]
དེ་ལྟར་འདི་ལ་ཡང་ངེས་པའི་རྒྱུ་བརྗོད་པར་བྱ་བ་སྟེ། གང་གི་ཕྱིར་འགའ་ཞིག་འདི་ནི་འཇིག་པའི་བདག་ཉིད་ཅན་དུ་འབྱུང་བ༌[^1044]དག་ཡིན་ལ། འདིར་འགའ་ཞིག་ངེས་པར་བྱེད་པའི་རང་བཞིན་ནི་ཡོད་པ་མ་ཡིན་ཏེ། སྐྱེ་བ་དང་ལྡན་པ་ཐམས་ཅད་ནི་མི་རྟག་པ་ཉིད་དུ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1367]
གལ་ཏེ་སྐྱེ་བ་དང་ལྡན་པའི་རང་བཞིན་ནི་འཇིག་པ་ཅན་ཡིན་ནོ་ཞེ་ན། སྐྱེ་བ་ནི་འཇིག་པ་ཅན་གྱི༌[^1045]རང་བཞིན་གྱི་རྒྱུ་མ་ཡིན་ལ། རྒྱུ་མེད་པ་ཅན་གྱི་རང་བཞིན་ལ་ངེས་པ་མེད་པ་དེ་བས་ན། འདིར་རྒྱུ་ལས་རང་གི་ངོ་བོའི་རྣམ་པར་དབྱེ་བ་འགའ་ཞིག་ཀྱང་མེད་དེ། དེ་མེད་པའི་ཕྱིར་འབྲས་བུ་ལ་ཡང་ཡོད་པ་མ་ཡིན་པས་ན་མཚུངས་པ་མ་ཡིན་ནོ། །

[Block 1368]
འཇིག་པ་ལ་ལྟོས་པ་མེད་པའི་དེ་འདིས་འགའ་ཞིག་ལ་འགའ་ཞིག་གི་ཚེ་ཡོད་པ་འགལ་བ་ཅན་དེ་མེད་པའི་རང་བཞིན་དུ་སྒྲུབ་པར་བྱེད་དོ། །

[Block 1369]
གང་གི་ཕྱིར་རང་བཞིན་ལྟོས་པ་མེད་པ་དེ་ནི་གལ་ཏེ་འགའ་ཞིག་གི་ཚེའམ་འགའ་ཞིག་ལ་འགྱུར་ན་དུས་དང་རྫས་དེ་ལ་ལྟོས་པ་ཅན་ཡིན་པའི་ཕྱིར། ལྟོས་པ་མེད་པ་ཉིད་དུ་མི་འགྱུར་རོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1370]
འོན་ཏེ་འཇིག་པའི་རང་བཞིན་དེ་ལྟོས་པ་མེད་པའི་ཕྱིར། རྒྱུ་མེད་པ་ཅན་དུ་འགྱུར་རོ། །
--- END BLOCKS ---
