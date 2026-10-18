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
[Block 1506 [HEADING]]
##### ཕུན་སུམ་ཚོགས་པའི་གང་ཟག་རྣམས་ཀྱི་སྐྱེ་བ་ཞུས་པ། ^1-2-5-14-0

[Block 1507]
དེ་ནས་གནས་བརྟན་རབ་འབྱོར་གྱིས་བཤད་པ་འདི་ལ་མོས་པ་ལ་སོགས་པ་ཕུན་སུམ་ཚོགས་པའི་གང་ཟག་རྣམས་གུས་པ་སྐྱེད་པའི༌[^1059]ཕྱིར་དེ་དག་གི་སྐྱེ་བ་ཞུས་པ། གང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་ཐོས་མ་ཐག་ཏུ་མོས་པར་འགྱུར་བ༌[^1060]དེ་གང་ནས་ཤི་འཕོས་ཏེ་འདིར་སྐྱེས་པར་གྱུར་པ་ལགས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1508 [HEADING]]
###### བྱང་ཆུབ་སེམས་དཔའ་དཀར་པོའི་ཕྱོགས་སུ་གཏོགས་པ་གསུམ། ^1-2-5-14-1-0

[Block 1509]
འདིར་ཡང་བྱང་ཆུབ་སེམས་དཔའ་དཀར་པོའི་ཕྱོགས་སུ་གཏོགས་པ་གསུམ་དང་ནག་པོའི་ཕྱོགས་སུ་གཏོགས་པ་གསུམ་བསྟན་ཏེ་མི་རྣམས་ཉིད་ཀྱི་ནང་ནས་ཤི་འཕོས་ཏེ་མི་རྣམས་ཉིད་ཀྱི༌[^1061]ནང་དུ་སྐྱེས་པ་ནི་དགེ་བ་སྟེ་གཅིག་གོ། །

[Block 1510]
སངས་རྒྱས་ཀྱི་ཞིང་གཞན་དག་ནས་ཤི་འཕོས་ཏེ་མི་རྣམས་ཀྱི་ནང་དུ་སྐྱེས་པ་ཡང་དགེ་བ་སྟེ་གཉིས་པའོ། །

[Block 1511]
དགའ་ལྡན་ནས་ཤི་འཕོས་ཏེ་འདིར་སྐྱེས་པ་ཡང་དགེ་བ་སྟེ་གསུམ་པའོ། །

[Block 1512 [HEADING]]
###### ནག་པོའི་ཕྱོགས་སུ་གཏོགས་པ་གསུམ། ^1-2-5-14-2-0

[Block 1513]
ནག་པོའི་ཕྱོགས་གསུམ༌[^1062]ནི་སྔོན་གྱི༌[^1063]མཐར་མཉན་པ་དང་ཡོངས་སུ་དྲིས་པ་དང་མི་ལྡན་པས་འདིར་སྐྱེས་ན་ཡང་བཤད་པ་ལམ་མོས་པ་ནི་གཅིག་གོ། །

[Block 1514]
སྔོན་གྱི་མཐར་མཉན་པ་ལ་སོགས་པ་དང་མི་ལྡན་པ་འདིར་དད་པ་ཙམ་གྱིས་ཐོས་ན་ཡང་འཕྲོགས་པར༌[^1064]འགྱུར་ཞིང་ལྡམ་ལྡེམ་དུ་འགྱུར་བ་ནི་གཉིས་པའོ། །

[Block 1515]
གང་སྔོན་གྱི་མཐར་བཤད་པ་འདི་དད་པ་ཙམ་གྱིས་དྲིས༌[^1065]ན་ཡང་འཛིན་པ་ལ་སོགས་པ་དང་མི་ལྡན་ན་ཕྱིས་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་དག་ཏུ་ལྷུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་གསུམ་པའོ། །

[Block 1516]
འདིར༌[^1066]ཡང་རྒྱ་མཚོའི་གྲུའི་དཔེ་དང་། བུམ་པའི་དཔེ་དང་། དེ་ནས་ཡང་གྲུའི་དཔེ་དང་མི་རྒད་པོའི་དཔེ་དག་ནི་གཞུང་ཉིད་ལས་བརྡ་ཕྲད་སླའོ། །

[Block 1517 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་ཐབས་མཁས་པ་དང་མི་ལྡན་པ། ^1-2-5-15-0

[Block 1518]
དེ་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་ཐབས་མཁས་པ་དང་མི་ལྡན་ན་ཐེག་པ་གཉིས་སུ་ལྟུང༌[^1067]གི་ལྡན་ན་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་བར་བསྟན་པའི་ཕྱིར་གནས་བརྟན་རབ་འབྱོར་གྱིས་ཇི་ལྟར་དེ་གཉིས་དང་མི་ལྡན་པར་འགྱུར་བ་དང་། ཇི་ལྟར་དེ་གཉིས་དང་མི་ལྡན་པར་མི་འགྱུར་བ་ཞུས་པ་དང་། དེའི་ཚེ་བཅོམ་ལྡན་འདས་ཀྱིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་དམིགས་པའི་དབང་དང་ང་རྒྱལ་གྱི་དབང་གིས་མི་ལྡན་པའི་མིང་དུ་འགྱུར་ཏེ། དེ་ནི་ས་གཉིས་ལས་ས་གང་ཡང་རུང་བ་གཅིག་ཏུ་ལྟུང་བར་འགྱུར་རོ། །

[Block 1519]
གང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་དམིགས་པ་དང་། ང་རྒྱལ་མེད་པ་དེ་ནི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཐོབ་པར་བྱེད་དོ་ཞེས་བསྟན་ཏོ། །

[Block 1520]
འདི་ལྟར་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དེ་ནི་ཚུ་རོལ་དུ་ཕྱིན་པའོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ལམ་གྱི་རྣམ་པ༌[^1068]ཤེས་པ་ཉིད་ཀྱི་ཕྱོགས་རྣམ་པར་མི་རྟོག་པ་ལ་ཚུ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 1521]
སངས་རྒྱས་རྣམས་ཀྱི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཕྱོགས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་སྟེ་རྣམ་པར་མི་རྟོག་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 1522]
དེ་བས་ན་ཚུ་རོལ་ཡང་ཤེས་ཕ་རོལ་ཡང་ཤེས་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1523]
དེའི་འོག་ཏུ༌[^1069]ཐབས་མཁས་པའི་འགྲེས་ལ་ཡང་རིམ་པ་དེ་ཉིད་དོ། །

[Block 1524 [HEADING]]
##### ལས་དང་པོ་པའི་བྱང་ཆུབ་སེམས་དཔས་བསླབ་པ། ^1-2-5-16-0

[Block 1525]
དེ་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཐབས་མཁས་པ་དང་མི་ལྡན་པ་དག་ཐེག་པ་གཉིས་སུ་ལྟུང་བར་འགྱུར་བ་ཐོས་ནས་འོ་ན་ཐེག་པ་ལ་གསར་དུ་ཞུགས་པ་ལས་དང་པོ་པ་དག་ཇི་ལྟར་འགྱུར་སྙམ་ནས། བཅོམ་ལྡན་འདས་ལས་དང་པོ་པའི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཇི་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་བསླབ་པར་བགྱི་ཞེས་ཞུས་པ་དང་བཅོམ་ལྡན་འདས་ཀྱིས་ལས་དང་པོ་པ་དག་ལ་དགེ་བའི་བཤེས་གཉེན་ངེས་པར་དགོས༌[^1070]ཏེ། དེ་བས་ན་དགེ་བའི་བཤེས་གཉེན་ལ་བརྟེན་པར༌[^1071]བྱ་ཞེས་བྱ་བ་བསྟན་ཏོ། །

[Block 1526]
མཆོག་ཏུ་འཛིན་པར་མ་བྱེད་ཅིག་ཅེས་བྱ་བ་དང་། འདོད་པ་མ་སྐྱེད་ཅིག་ཅེས་བྱ༌[^1072]བ་ནི་རྣམ་པར་རྟོག་པའི་ལྟ་བ་དང་། དོན་དམ་པ་ལ་ཆགས་པས་སྨོན་པ༌[^1073]མ་བྱེད་ཅིག་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1527 [HEADING]]
##### བྱང་ཆུབ་སེམས་དཔའ་དཀའ་བ་བགྱིད་པ། ^1-2-5-17-0

[Block 1528]
དེ་ནས་གནས་བརྟན་རབ་འབྱོར་གྱིས་དེ་ལྟར་ཆོས་ཐམས་ཅད་རང་གི་མཚན་ཉིད་ཀྱིས༌[^1074]སྟོང་པ་ལ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཚོལ་བའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་དཀའ་བ་བགྱིད་པའོ་ཞེས་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་སྐབས་དེར༌[^1075]འཇིག་རྟེན་ལ་ཕན་པ་དང་། བདེ་བ་དང་མགོན་དང་སྐྱབས་དང་གནས་དང་དཔུང་གཉེན་དང་གླིང་དང་། ཡོངས་སུ་འདྲེན་པ་དང་། རྟེན་དུ་འགྱུར་བར་བྱའོ་ཞེས་བྱ་བ་ཚིག་དགུས༌[^1076]བསྟན་ནས་དེ་ནས་ཡང་ཚིག་དེ་དག་རེ་རེ་ནས་སྨོས་ཏེ། རྒྱ་ཆེར་བཤད་པ་མཛད་དོ། །

[Block 1529 [HEADING]]
###### ཕན་པ། ^1-2-5-17-1-0

[Block 1530]
འགྲོ་བ་རྣམས་ལས་ཡོངས་སུ་ཐར་བར་བྱས་ལ། འཇིག་པ་མེད་པའི་གནས་སུ་དགོད་པའི་བསམ་པ་ནི་ཕན་པའོ། །

[Block 1531 [HEADING]]
###### བདེ་བ། ^1-2-5-17-2-0

[Block 1532]
སྡུག་བསྔལ་རྣམས་ལས་ཡོངས་སུ་ཐར་བར་བྱས་ལ། བདེ་བ༌[^1077]ལ་དགོད་པའི་བསམ་པ་ནི་བདེ་བའོ། །

[Block 1533 [HEADING]]
###### མགོན། ^1-2-5-17-3-0

[Block 1534]
སྡུག་བསྔལ་རྣམས༌[^1078]ལས་ཡོངས་སུ་བསྲུང་བའི་ཕྱིར་ཆོས་བཤད་པའི་བསམ་པ་ནི་མགོན་ནོ། །

[Block 1535 [HEADING]]
###### སྐྱབས། ^1-2-5-17-4-0

[Block 1536]
སྡུག་བསྔལ་གྱིས༌[^1079]ཉམ་ཐག་པ་རྣམས་སྡུག་བསྔལ༌[^1080]ལས་ཡོངས་སུ་ཐར་བར་བྱས་ལ། ཕུང་པོ་མེད་པའི་མྱ་ངན་ལས་འདས་པར་དགོད་པའི་བསམ་པ་ནི་སྐྱབས་སོ། །

[Block 1537 [HEADING]]
###### གནས། ^1-2-5-17-5-0

[Block 1538]
ཆགས་པ་མེད་པར་བྱ་བའི་ཕྱིར། ཆོས་འཆད་པའི་བསམ་པ་ནི་གནས་སོ། །

[Block 1539 [HEADING]]
###### དཔུང་གཉེན། ^1-2-5-17-6-0

[Block 1540]
གཟུགས་ལ་སོགས་པའི་ཆོས་ཐམས་ཅད་ཀྱིས་ཕ་རོལ་གྱི་ཆོས་འཆད་པའི་བསམ་པ་ནི་དཔུང་གཉེན་ནོ། །

[Block 1541 [HEADING]]
###### གླིང། ^1-2-5-17-7-0

[Block 1542]
གླིང་བཞིན་དུ་ཁོ་ར་ཁོར་ཡུག་ཏུ་ཡོངས་སུ་ཆད་པའི་རྣམ་པར་ཆོས་འཆད་པའི་བསམ་པ་ནི་གླིང་ངོ་། །

[Block 1543 [HEADING]]
###### ཡོངས་སུ་འདྲེན་པ། ^1-2-5-17-8-0

[Block 1544]
སེམས་ཅན་རྣམས་ལ་སྙིང་རྗེ་ཆེན་པོས་མྱ་ངན་ལས་འདས་པར་འདྲེན་པའི་ཆོས་འཆད་པའི་བསམ་པ་ནི་ཡོངས་སུ་འདྲེན་པའོ། །

[Block 1545 [HEADING]]
###### རྟེན། ^1-2-5-17-9-0
--- END BLOCKS ---
