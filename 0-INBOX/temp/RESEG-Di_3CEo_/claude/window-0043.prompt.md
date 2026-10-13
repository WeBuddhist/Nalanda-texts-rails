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
[Block 1506]
རྒྱར་ནི། ངོས་གསུམ་འདི་དང་འདྲ། །ཇི་ལྟར་འཛམ་བུའི་གླིང་ལ་དཔག་ཚད་སྟོང་ཕྲག་གཉིས་གཉིས་བཞིན་ནོ། །

[Block 1507]
གཅིག་ལ་དཔག་ཚད་སུམ་བརྒྱ་ལྔ་བཅུའོ། །

[Block 1508]
ངོས་བཞི་པ་ལ་ནི་དཔག་ཚད་སུམ་བརྒྱ་ལྔ་བཅུའོ། །

[Block 1509]
བ་ལང་སྤྱོད་གླིང་ཟླུམ་པོ་སྟེ།

[Block 1510 [VERSE]]
སྟོང་ཕྲག་ཕྱེད་དང་བརྒྱད་ཡིན་ནོ། །
དེ་དབུས་སྟོང་ཕྲག་ཕྱེད་དང་གསུམ་མོ། །
སྒྲ་མི་སྙན་བརྒྱད་གྲུ་བཞིར་མཉམ། །

[Block 1511 [HEADING]]
#### བར་གྱི་གླིང་བརྒྱད། ^3-2-4-0

[Block 1512]
ཡང་དེ་དག་གི་བར་བར་ན༌[^567]གླིང་རྣམས་མངོན་པར་གྲུབ་པ་དེ་དག་ནི༌[^568]གང་། དུ་ཞིག་ནི་ཡོད་ཅེ་ན།

[Block 1513 [VERSE]]
དེ་ཡི་བར་གྱི་གླིང་བརྒྱད་ནི། །
ལུས་དང་ལུས་འཕགས་སྒྲ་མི་སྙན། །
སྒྲ་མི་སྙན་གྱི་ཟླ་དང་ནི། །
རྔ་ཡབ་དང་ནི་རྔ་ཡབ་གཞན། །
གཡོ་ལྡན་དང་ནི་ལམ་མཆོག་འགྲོ། །

[Block 1514]
དེ་ལ་ལུས་དང་ལུས་འཕགས་ནི་ཤར་གྱི་ལུས་འཕགས་ཀྱི་འཁོར་ཡིན་ནོ། །

[Block 1515]
སྒྲ་མི་སྙན་དང་སྒྲ་མི་སྙན་གྱི་ཟླ་ནི་བྱང་སྒྲ་མི་སྙན་གྱིའོ། །

[Block 1516]
གཡོ་ལྡན་དང་ལམ་མཆོག་འགྲོ་ནི་ནུབ་ཀྱི་བ་ལང་སྤྱོད་ཀྱིའོ། །

[Block 1517]
རྔ་ཡབ་དང་རྔ་ཡབ་གཞན་ནི་འཛམ་བུའི་གླིང་གིའོ། །

[Block 1518]
འདི་ནས་བྱང་དུ་རི་ནག་པོ་དགུ་འདས་གངས་རིའོ། །

[Block 1519]
འཛམ་བུའི་གླིང་འདི་ནས་བྱང་ཕྱོགས་སུ་རི་ནག་པོ་གསུམ་ཡོད་དོ། །

[Block 1520]
དེ་དག་འདས་ནས་གཞན་གསུམ་ཡོད་དོ། །

[Block 1521]
ཡང་གསུམ་ཡོད་དོ། །

[Block 1522]
དེའི་ཕ་རོལ་ན་གངས་རིའོ། །

[Block 1523]
དེ་ནས་ནི།

[Block 1524 [VERSE]]
སྤོས་ངད་ལྡན་པའི་ཚུ་རོལ་ན། །
ཆུ་ཞེང་ལྔ་བཅུ་ཡོད་པའི་མཚོ། །

[Block 1525]
གངས་རི་དེའི་ཕ་རོལ་རི་སྤོས་ཀྱི་ངད་ལྡང་བའི་ཚུ་རོལ་ན་མཚོ་མ་དྲོས་པ་ཞེས་བྱ་བ་ཞེང་དུ་ཡང༌[^569]དཔག་ཚད་ལྔ་བཅུ་ཡོད་པ། ཆུར་ཡང་དཔག་ཚད་ལྔ་བཅུ་ཡོད་དོ། །

[Block 1526 [HEADING]]
#### དམྱལ་བ། ^3-2-5-0

[Block 1527]
ཡང་དམྱལ་བ་རྣམས་ཕྱོགས་ནི་གང་རོལ་ན་ཚད་ཇི་ཙམ་ཞེ་ན།

[Block 1528 [VERSE]]
འདི་འོག་སྟོང་ཕྲག་ཉི་ཤུ་ན། །
མནར་མེད་པའོ་དེ་ཙམ་མོ། །

[Block 1529]
འཛམ་བུའི་གླིང་འདི་ཉིད་ཀྱི་འོག་དཔག་ཚད་ཉི་ཁྲི་རྔམས་དང་རྒྱར་ནི་དེ་ཙམ་མོ། །

[Block 1530]
སྡུག་བསྔལ་ལ་བར་ཆད་མེད་པས་ན་མནར་མེད་པའོ། །

[Block 1531]
དེ་ཡི་སྟེང་ན་དམྱལ་བ་བདུན། །རབ་ཏུ་ཚ་བ་དང་། ཚ་བ་དང་། ངུ་འབོད་ཆེན་པོ་དང་། ངུ་འབོད་དང་། བསྡུས་འཇོམས་དང་། ཐིག་ནག་དང་། ཡང་སོས་དག་གོ། །

[Block 1532]
དེ་དག་ཀྱང་།

[Block 1533 [VERSE]]
བརྒྱད་པོ་ཀུན་ལ་ལྷག་བཅུ་དྲུག །
ལྷག་པ་བཅུ་དྲུག་གང་ཞེ་ན། །
དེ་དག་གི་ནི་ངོས་བཞི་ན། །
མེ་མ༌[^570]མུར་དང་རོ་མྱགས༌[^571]དང་། །

[Block 1534]
སྤུ་གྲིའི༌[^572]ལམ་སོགས་ཆུ་བོ་བཞི།[^573] །དེ་དག་གི་སྒོ་རེ་རེ་ན་ལྷག་པ་བཞི་བཞི་ཡོད་དོ། །

[Block 1535]
མེ་མ༌[^574]མུར་པུས༌[^575]མོ་ནུབ་ཙམ་གང་དུ་སེམས་ཅན་དེ་དག་གི་རྐང་པ་བཞག་ན་ནི་པགས་པ་དང་ཤ༌[^576]ཁྲག་ཞིག་པར་འགྱུར་ལ། རྐང་པ་བཏེག་ན་ནི་དེ་དག་སླར་སྐྱེ་བ་དང་། རོ་མྱགས་མི་གཙང་བའི་འདམ་རྫབ་གང་དུ་འབུ་མཆུ་རྣོན་ཞེས་བྱ་བ་ལུས་ཐམས་ཅད་དཀར་ཞིང་མགོ་གནག༌[^577]པ་རུས་པའི་བར་དུ་འབིགས་པར་བྱེད་པ་དང་། སྤུ་གྲི་ལམ་སོགས་ནི་སྤུ་གྲི་གཏམས་པའི་ལམ་ཆེན་པོ་དང་། རལ་གྲི་ལོ་མའི་ནགས་ཚལ་དང་། །ཁྱི་སྲེ་བོ་དང་། ལྕགས་ཀྱི་ཤལ་མ་ལིའི་ནགས་ཚལ་དང་། ཁྭ་ལྕགས་ཀྱི་མཆུ་ཅན་རྣམས་སོ། །

[Block 1536]
སྤུ་གྲིའི་ལམ་ལ་སོགས་པ་དེ་དག་ནི་མཚོན་ཆ་མངོན་པར་འདྲ་བའི་ཕྱིར་གཅིག་ཏུ་དྲིལ་ནས་གསུངས་སོ། །

[Block 1537]
ལྷག་པ་བཞི་པ་ནི་ཆུ་བོ་རབ་མེད་ཐལ་ཆུ་ཁོལ་མས་གང་བ་སྟེ། གནོད་པ་ལྷག་པའི་གནས་ཡིན་པའི་ཕྱིར་བཞི་པོ་དེ་དག་ལྷག་པ་སྟེ། སྒོའི་དབྱེ་བས་བཅུ་དྲུག་ཏུ་འགྱུར་རོ། །

[Block 1538]
རེ་ཞིག་དེ་དག་ནི་ཚ་བའི་དམྱལ་བ་བརྒྱད་ཡིན་ནོ། །

[Block 1539]
ཆུ་བུར་ཅན་སོགས་གྲང་བརྒྱད་གཞན། །འདི་ལྟ་སྟེ། ཆུ་བུར་ཅན་དང་། ཆུ་བུར་རྡོལ་བ་དང་། སོ་ཐམ་ཐམ་པ་དང་། ཨ་ཆུ་དང་། ཀྱི་ཧུད༌[^578]དང་། ཨུཏྤལ་ལྟར་གས་པ་དང་། པདྨ་ལྟར་གས་པ་དང་། པདྨ་ལྟར་ཆེར་གས་པའོ། །

[Block 1540]
མིང་འདི་རྣམས་ནི་སེམས་ཅན་གྲང་བ་མི་བཟད་པས་ཉེན་པ་དེ་དག་གི་ལུས་དང་སྒྲ་འགྱུར་བ་དང་མཐུན་པ་དག་ཡིན་ནོ། །

[Block 1541 [HEADING]]
#### ཉི་མ་དང་ཟླ་བ། ^3-2-6-0

[Block 1542]
ཉི་མ་དང་ཟླ་བ་འདི་ནས་ཐག་ཇི་སྲིད་ཅེ་ན། ཉི་ཟླ་ལྷུན་པོའི་ཕྱེད་ནའོ། །

[Block 1543]
རི་གཉའ་ཤིང་འཛིན་གྱི་རྩེ་མོ་དང་མཉམ་པར་རྒྱུའོ། །

[Block 1544]
ཚད་ཀྱང་། དཔག་ཚད་ལྔ་བཅུ་གཅིག་དང་བཅས། །རིམ་པ་བཞིན་དུའོ། །

[Block 1545]
གླིང་བཞི་པོ་དག་ཏུ་ཉི་མས་ཅིག་ཅར་བྱ་བ་བྱེད་དམ་ཞེ་ན། མ་ཡིན་ཏེ། འོན་ཀྱང་།
--- END BLOCKS ---
