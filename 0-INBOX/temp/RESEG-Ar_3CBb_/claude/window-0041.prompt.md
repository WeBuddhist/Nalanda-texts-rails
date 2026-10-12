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
དེ་ལྟར་ལྷག་པར་མོས་པས་ཞེས་བྱ་བ་ནི་དྲང་བ་དང་སྤྱིའི་དོན་དུ་བཤད་པ་ཡིན་གྱི་ཐམས་ཅད་ཀྱི༌[^751]ནི་མ་ཡིན་ནོ། །

[Block 1437]
ཡོངས་སུ་དག་པ་དང་ཡོངས་སུ་མ་དག་པ་ནི་སློབ་པ་དང་མི་སློབ་པ་དང་།[^752] ཤེས་བྱའི་སྒྲིབ་པ་མཐའ་དག་སྤངས་པ་དང་མ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 1438]
དེ་ལ་གཙོ་བོ་ནི་ཡོངས་སུ་དག༌[^753]པའོ། །

[Block 1439]
ལྷག་མ་ནི་ཡོངས་སུ་དག་པ་དང་མ་དག་པ་ཉིད་དོ། །

[Block 1440]
ཡི་གེ་གསུམ་ནི་ཨོཾ་ཨཱཿཧཱུཾ་གསུམ་མོ། །

[Block 1441]
དེ་ཉིད་ནི་འདའ་བར་མི་བྱ་བ་ནི་ཡོངས་སུ་བླང་བར་བྱ་བ་ཉིད་དོ། །

[Block 1442]
དེ་ལས་བྱུང་བ་ནི་ཡི་གེ་གསུམ་ལས་བྱུང་བ་སྟེ་རིགས་དྲུག་པའོ། །

[Block 1443]
རྣལ་འབྱོར་བཞི་ནི་རྣལ་འབྱོར་དང་། ལྷག་པའི་རྣལ་འབྱོར་དང་། རྣལ་འབྱོར་ཆེན་པོ་དང་། དེ་ཁོ་ན་ཉིད་ཀྱི་རྣལ་འབྱོར་ཏེ་བཤད་ཟིན་ཏོ། །

[Block 1444]
འདི་དག་གི་དོན་ཡང་ཐོག་མར་སྲུང་བའི༌[^754]འཁོར་ལོ་སྔོན་དུ་འགྲོ་བས་སྟོང་པ་ཉིད་ཀྱི་ངང་ལས་རྟེན་གྱི་དཀྱིལ་འཁོར་གཞལ་ཡས་ཁང་དང་བཅས་པ་གསལ་བར་བྱས་ནས། དེ་ནས་མོས་པས་རང་བཞིན་གྱི༌[^755]དཀྱིལ་འཁོར་གསལ་བར་བྱས་པ་སྟེ༌[^756]སླར་སྟོང་པ་ཉིད་དུ་བྱས་པ་ལས་ཉི་མ་དང་ཟླ་བ་དང་པདྨ་དང་། ཨོཾ་ཨཱཿཧཱུཾ་ཞེས་པ་ནི་གསལ་བར་བསམ་མོ། །

[Block 1445]
དེ་ནས་དེ་དག་ཟླ་བའི་དཀྱིལ་འཁོར་ལ་འདུས་ཏེ་དེ་ལ་དམིགས་པར་བྱའོ། །

[Block 1446]
དེ་ཡོངས་སུ་གྱུར་པ་ལས་དང་པོའི་མགོན་པོ་ཟླ་བ་ལྟ་བུ༌[^757]བསམས་ཏེ། དེར་མི་བསྐྱོད་པ་བཞུགས་པས་ཞལ་གསུམ་པའི་རྡོ་རྗེ་སེམས་དཔའ་བསམས༌[^758]ལ། འོག་ནས་འབྱུང་བའི་རིམ་པས་རྡོ་རྗེ་སེམས་དཔའི་ལུས་ལ་ལྷ་ཐམས་ཅད་ཀྱི་ཡི་གེ་དགོད་པར་བྱའོ། །

[Block 1447]
དེ་ནས་ནམ་མཁའ་ལ་སངས་རྒྱས་ཐམས་ཅད་བལྟས་ཏེ་ལྷ་མོ་སོ་སོས་མཆོད་པ་སྔོན་དུ་འགྲོ་བས་གསོལ་བ་བཏབ་པས་ཇི་སྐད་དུ་འོག་ནས་འབྱུང་བའི་ཆོ་གས་གནས་གསུམ་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 1448]
དེ་ནས་ལེགས་པར་སྦྱངས་པའི་ཤེས་རབ་མ་དང་གཉིས་སུ་མེད་པར་སྙོམས་པར་འཇུག་པ་ཆོ་ག་འདིས་འོག་ནས་སྟོན་པའི་དཀྱིལ་འཁོར་སྤྲོས་ཏེ་སེམས་ཅན་གྱི་དོན་བྱས་ནས་སླར་འདུས་ནས་རང་གི་དཀྱིལ་འཁོར་ལ་དམིགས་ཏེ་བརྟན་པར་བྱའོ། །

[Block 1449]
དེ་ནས། སྣ་ཡི་རྩེ་མོར་ཡུངས་ཀར་བསམ། །ཞེས་བྱ་བ་ལ་སོགས་པའི་རིམ་པ་འདིས༌[^759]ཕྲ་མོའི་ཏིང་ངེ་འཛིན་སྣའི་རྩེ་མོར་བརྟན་པར༌[^760]བྱའོ། །

[Block 1450]
གཞན་ཡང་འོད་དུ་ཞུ་བ་བསླང་བ༌[^761]དང་ཟས་ལ་སོགས་པ་ལེགས་པར་བཟའ་བ་དང་། ལྷའི་འཁོར་ལོ་ལ་བསྟོད་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཡན་ལག་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱའོ། །

[Block 1451]
འོད་གསལ་བ་ནི་སངས་རྒྱས་ཐམས་ཅད་ཀྱིས༌[^762]འདའ་བར་བྱ་བ་མ་ཡིན་པ་སྟེ་ཆོས་ཀྱི་སྐུའོ། །

[Block 1452]
དེ་ལས་བྱུང་བ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་སྟེ། [^763]ཅིའི་ཕྱིར་ཞེ་ན། མཁས་བརྩོན༌[^764]ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། མཁས་པ་ཆེ་བ་དང་། བརྩོན་པ་ཆེ་བ་དང་། རྩོམ་པ༌[^765]ཆེ་བ་ཞེས་པ་སྟེ། འདི་དག་གིས་རང་དང་གཞན་གྱི་དོན༌[^766]ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1453]
གཞན་ནི་གོ་སླའོ། །

[Block 1454]
ཐེ་ཚོམ་སྐྱེ་བར་བྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་རིགས་པ་འདི་བླ་མ་ལས་བྱུང་གི་གཞན་དུ་རྟོག་གེ་པས་ནམ་ཡང་རྙེད་པར་མི་འགྱུར་ཞེས་ངེས་པར་སྟོན་པར་བྱེད་དོ་ཞེའོ། །

[Block 1455]
དེ་རྣམས་འབྱུང་བའི་དམ༌[^767]ཚིག་ནི་དེ་སྐྱེད་པར་བྱེད་པའི་ཞེས་བྱ་བ་ནི་དམ་ལས་མི་འདའ་བ་ཉིད་དོ། །

[Block 1456]
དབང་པོ་གཉིས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གསང་བའི་དབང་བསྐུར་བསྟན་ཏོ། །

[Block 1457]
གདུལ་བྱའི་སྐྱེ་བོ་ནི་སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན༌[^768]པའོ། །

[Block 1458]
སྐུ་རྣམ་པ་གཉིས་ནི་ལོངས་སྤྱོད་རྫོགས༌[^769]དང་སྤྲུལ་པའི་སྐུའོ། །

[Block 1459]
ཡང་དག་པར་སྟོན་པ་ནི་སྐུ་དང་གསུང་གི༌[^770]ཆོས་སྟོན་པ་སྟེ་དེས་སྨིན་པ་དང་གྲོལ་བར་བྱེད་པས་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1460]
ཡེ་ཤེས་ཉིད་ཅེས་པ་ནི་གཞན་དང་ལྡན་པ་རྣམ་པར་གཅོད་པའོ། །

[Block 1461]
སེམས་ཅན་རྣམས་ཀྱི་རྒྱུད་ལ་ཞེས་བྱ་བས་ནི་གསལ་བར་བྱ་བའི་ཡུལ་བསྟན་ཏོ། །

[Block 1462]
མི་བསྐྱོད་པ་ནི་གསལ་བར་བྱེད་པའོ། །

[Block 1463]
རྣམ་པར་ཤེས་པ་གསུམ་གྱི་སྣང་བ་ཞེས་པ་ནི་ཤེས་པའི་སྣང་བ་ཉིད་དོ། །

[Block 1464]
དོན་དམ་པའི་བདེན་པ་ནི་ཡང་དག་པའི་ཤེས་པ་དང་ལྡན་པ་ལ་བདེན་པས་སོ། །

[Block 1465]
བརྗོད༌[^771]དུ་མེད་པས་ནི་དེའི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 1466]
རྣམ་པ༌[^772]མ་ལུས་པ་ཟིལ་གྱིས་མནན༌[^773]པས་ནི་དེའི་ལས་བསྟན་ཏོ། །

[Block 1467]
རང་བཞིན་གྱིས༌[^774]འོད་གསལ་བའི་ཏིང་ངེ་འཛིན་ནི་ཆོས་ཀྱི་སྐུ་སྟེ་དེ་ལས་ཆུ་ལས་ཉའི་ཚུལ་དུ་རང་གི་སྐུར་བཞེངས་པའོ། །

[Block 1468]
དེས་ཅི་བྱེད་ཅེ་ན། ཉོན་མོངས་པ་ལྔས་ཁྱབ་པའི་ཞེས་པ་ལ་སོགས་པ་ནི་སྤྱིར་སྙིང་རྗེའི་ཡུལ་དུ་བསྟན་ཏོ། །

[Block 1469]
དེ་ལྟ་ན་ཡང་ཅིའི་ཕྱིར་སྙིང་རྗེ་སྐྱེ་ཞེ་ན། ཉོན་མོངས་པའི་རང་བཞིན་ནི་ཡེ་ནས་རྣམ་པར་དག་པ་སྟེ་དེ་ཡོངས་སུ་ཤེས་པ་ཉིད་ནི་བྱང་ཆུབ་ཡིན་ལ་དེའི་ངོ་བོ་ཉིད་ནི་བདག་ཡིན་ནོ་ཞེས་པ་འདིས༌[^775]ནི་ཉོན་མོངས་པ་དང་རྡོ་རྗེ་འཆང་དང་། དེ་བཞིན་གཤེགས་པ་ནི་གཉིས་སུ་མེད་ཅིང་གཉིས་སུ་དབྱེར་མེད་དོ་ཞེས་དགོངས་པ་ཉིད་དོ། །

[Block 1470]
བྱེ་བྲག་ཏུ་བསྟན་པ། ཉོན་མོངས་པ་ཞེ་སྡང་ནི་སེམས་ཁོང་དུ༌[^776]འཁྲུགས་པ་སྟེ། དེ་དང་གང་ལྡན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1471]
དེ་སྦྱང་བ༌[^777]ནི་ཡོངས་སུ་དག་པར༌[^778]བྱ་བའི་ཕྱིར་རོ། །

[Block 1472]
ཞེ་སྡང་ཞེས་པའི་བཤད་པ་ཐུགས་རྗེ་ཆེན་པོའི་ཐབས་ཀྱི་ཁྲོ་བ༌[^779]ནི་ཐུགས༌[^780]རྗེ་ཆེན་པོས་སྤྲུལ་པའོ། །

[Block 1473]
དེ་ཡང་རབ་ཏུ་ཁྲོས་པའི༌[^781]ཆོས་དང་ལྡན་པས་ནི་ཞེ་སྡང་སྟེ། གང་ལ་ཞེ་སྡང་དང་འདྲ་བའི་ཆོས་ཡོད་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1474]
དེའི་རིགས༌[^782]ནི་དེའི་རིགས་སུ་སྐྱེད་པའོ། །

[Block 1475]
འདོད་པའི་འབྲས་བུ་སྐྱེད་པ་ནི་སྔགས་དང་མཐུན༌[^783]པའི་ལུས་སྐྱེད་པའོ། །
--- END BLOCKS ---
