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
ཚིགས་བཅད་བདུན་གྱིས་ནི་ད་ལྟར་ཡང་དག་པ་ཉིད་དུ་བསྟན་པ་བརྗོད་དེ།[^1334] སྔར་སངས་རྒྱས་ཀྱི་ཐེག་པ་གཅིག་པུ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་བསྟན་པའོ། །

[Block 1507 [HEADING]]
###### **སྔར་ཐེག་པ་གསུམ་ཐབས་ཙམ་དུ་བསྟན་པ།** ^4-2-11-1-1-2-5-3-2-1-0

[Block 1508]
སྔ་མ་ལ་ཡང་རྣམ་པ་བཞི་སྟེ་ཚིགས་བཅད་ཕྱེད་དང་བཞིས་ནི་སྐྱེ་བའི་གནས་སུ་བགེགས་ལས་ཐར་བར་བྱ་བ་བསྟན་ཏོ། །

[Block 1509]
ཚིགས༌[^1335]གསུམ་གྱིས་ནི༌[^1336]གྲོལ་བར་བྱ་བར་མི་ནུས་པ་སེམས་པ་བསྟན་པའོ། །

[Block 1510]
ཚིག་ཕྱེད་དང་བཅུ་གཉིས་ཀྱིས་ནི་ཐབས་ཙམ་དུ་བསྟན་པར་དགོངས་སོ། །

[Block 1511]
ཚིག་ཕྱེད་དང་བཞིས་ནི་ཐེག་པ་གསུམ་སྤྲུལ་པ་བསྟན་ཏོ། །

[Block 1512 [HEADING]]
###### **སྐྱེ་བའི་གནས་སུ་བགེགས་ལས་ཐར་བར་བྱ་བ།** ^4-2-11-1-1-2-5-3-2-1-1-0

[Block 1513]
སྔ་མ་ལ་ཡང་གཉིས་ཏེ་ཚིག་གཅིག༌[^1337]གིས་ནི་དགེ་བ་མེད་པ་བསྟན་ཏོ། །

[Block 1514]
ཚིག་ཕྱེད་དང་གསུམ་གྱིས་ནི་སྡིག་པ་ཡོད་པར་བསྟན་ཏོ། །

[Block 1515 [HEADING]]
###### **དགེ་བ་མེད་པ།** ^4-2-11-1-1-2-5-3-2-1-1-1-0

[Block 1516]
ང་ཡིས་མཐོང་བ་ཞེས་བྱ་བ་ནི་སྤྱན་ལྔའི༌[^1338]ནང་ནས་སངས་རྒྱས་ཀྱི་སྤྱན་གྱིས་གཟིགས་སོ། །ཤེས་རབ་དང་བསོད་ནམས་སྤོང་བ་ནི་འགྲོ་བ་དྲུག་གི་སེམས་ཅན་ཐོག་མ་མེད་པ་ནས་བསོད་ནམས་དང་ཡི་ཤེས་ཀྱི་རྒྱུར་འགྱུར་བ་མི་བྱེད་འཕགས་པའི་ནོར་བདུན་དང་མི་ལྡན་ལྷ་དང་མིའི་ཆོས་ཀྱི་ནོར་བདུན་དང་། ཕ་རོལ་ཏུ༌[^1339]ཕྱིན་པ་དྲུག་དང་ཐབས་མཁས་པ་མེད་པ་ནི་ཤེས་རབ་དང་བསོད་ནམས་སྤངས་པའོ། །

[Block 1517 [HEADING]]
###### **སྡིག་པ་ཡོད་པ།** ^4-2-11-1-1-2-5-3-2-1-1-2-0

[Block 1518]
འདི་མན་ཆད་ཚིགས་བཅད་ཕྱེད་དང་གསུམ་གྱིས་ནི་སྡིག་པ་ཡོད་པར་བསྟན་པ་སྟེ། དེ་ལ་ཚིག༌[^1340]ཕྱེད་དང་གཉིས་ཀྱིས་ནི་ད་ལྟར་གྱི་དུས་ན་འཁོར་བར་ནུབ་ཅིང་སྡུག་བསྔལ་སྐྱེ་བ་བསྟན་ཏོ། །

[Block 1519]
ཚིགས་བཅད་གཅིག་གིས་ནི་གྲོལ༌[^1341]བར་འདོད་ཀྱང་ལོག་པར་ལྟ་བ་སྤྱོད་པ་བསྟན་ཏོ། །

[Block 1520 [HEADING]]
###### **འཁོར་བར་ནུབ་ཅིང་སྡུག་བསྔལ་སྐྱེ་བ།** ^4-2-11-1-1-2-5-3-2-1-1-2-1-0

[Block 1521]
འཇིག་རྟེན་ན་གཡག་རྔ་མ་ལ་ཆགས་པ་བཞིན་དུ་སེམས་ཅན་དག་ཀྱང་འདོད་པ་ལྔ་ལ་ཆགས་ནས་སྡུག་བསྔལ༌[^1342]གྱིས་གདུངས་ཏེ་ངན་སོང་དུ་ལྷུང་བར་འགྱུར་རོ།[^1343]

[Block 1522]
།མདོ་ལས།

[Block 1523 [HEADING]]
###### **གྲོལ་བར་འདོད་ཀྱང་ལོག་པར་ལྟ་བ་སྤྱོད་པ།** ^4-2-11-1-1-2-5-3-2-1-1-2-2-0

[Block 1524]
སངས་རྒྱས་མཐུ་ཆེན་རྣམས་ཀྱང་ཡོངས་མི་ཚོལ། །ཞེས་པ་ནས། ང་ཡི་སྙིང་རྗེ་སྟོབས་ཆེན་དེ་དག་ལ། ། ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1344]ནི་གྲོལ་བར་འདོད་ལ་ལོག་པར་ལྟ་བ་སྤྱོད་པ་བསྟན་པ་སྟེ། སངས་རྒྱས་ཀྱི་མཐུ་ཆེན་པོ་དང་ཡེ་ཤེས་ཀྱིས༌[^1345]སྡུག་བསྔལ་གཅོད་པ་ནི་མུ་སྟེགས་ཅན་གྱི་ལྟ་བ་དང་འདྲ་བར་ངན་པ༌[^1346]ལྟ་བར་ལྷུང་སྟེ། ལུས་སྡུག་བསྔལ་བར་བྱས་ནས་འཁོར་བའི་སྡུག་བསྔལ་ལས་གྲོལ་བར་འདོད་པ་ནི་མི་གཤའོ། །

[Block 1525]
ལོ་དྲུག་གི་བར་དུ་ནས་འབྲུ་རེ་ལས་མ་ཟོས་ཀྱང་བྱང་ཆུབ་མ་ཐོབ་ན་ཚེར་ཕུང་གི་སྟེང་ན་ཉལ་བས་བྱང་ཆུབ་ག་ལ་ཞིག་ཐོབ་སྟེ། ཁྱི་རྡོ་ལ་བསྙེགས་པ༌[^1347]དང་འདྲ་བའི་སེང་གེ་ལྟར་མི༌[^1348]བསྙེགས་པ་མ་ཡིན་ནོ། །

[Block 1526 [HEADING]]
###### **གྲོལ་བར་བྱ་མི་ནུས་པ་སེམས་པ།** ^4-2-11-1-1-2-5-3-2-1-2-0

[Block 1527]
འདི་མན་ཆད་ཚིག་གསུམ་གྱིས་གྲོལ་བར་བྱ་མི་ནུས་པ་སེམས་པ་བསྟན་པ་སྟེ། དེ་ལ་ཡང་གསུམ་མོ། །

[Block 1528]
ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་སྔོན་སྤྱོད་པའི་རྒྱུ་སེམས་པ་བསྟན་པ་སྟེ། ཚིག༌[^1349]གཅིག་གིས་ནི༌[^1350]འབྲས་བུ་ཐོབ་ནས་ཀྱང་སེམས་པ་བསྟན་ཏོ། །

[Block 1529]
ཚིག༌[^1351]ཕྱེད་དང་གཉིས་ཀྱིས་ནི་མི་ནུས་པར་སེམས་པ་བསྟན་ཏོ། །

[Block 1530 [HEADING]]
###### **སྔོན་སྤྱོད་པའི་རྒྱུ་སེམས་པ།** ^4-2-11-1-1-2-5-3-2-1-2-1-0

[Block 1531]
འདི་ནི་དང་པོ་སྟེ་སེམས་ཅན་དག༌[^1352]རྒྱུ་འདི་གཉིས་དང་ལྡན་པས་ངའི་སྙིང་རྗེ་སྟོབས་ཆེ་དེ༌[^1353]དག་ལའོ་ཞེས་བསྟན་ཏོ། །

[Block 1532]
མདོ་ལས།

[Block 1533 [HEADING]]
###### **འབྲས་བུ་ཐོབ་ནས་སེམས་པ།** ^4-2-11-1-1-2-5-3-2-1-2-2-0

[Block 1534]
དེ་དག་ངས་བསམས་བྱང་ཆུབ་སྙིང་པོ་དེར། །ཞེས་པ་ནས། དེ་ཡི་དྲུང་ན་ཕན་ཚུན་འཆག་ཅིང་གནས།[^1354] ཞེས་པའི་བར་དུ་ཚིགས་བཅད་འདིས༌[^1355]འབྲས་བུ་ཐོབ་ནས་དགོངས་པ་བསྟན་པ་སྟེ། མངོན་པར་སངས་རྒྱས་ནས་ཤིང་རྒྱལ་གྱི་དྲུང་དུ་ཕན་ཚུན་འཆག་ཅིང་སེམས་ཅན་གྱི་དོན་ཇི་ལྟར་བྱ་བ་དགོངས་པའོ། །

[Block 1535]
གཞན་ཡང་སྡོང་པོ༌[^1356]བརྟག་པ་ནི་དོན་ལ་ཐུགས་བཞག་པ་བསྟན་ཏོ། །

[Block 1536]
འཆག་པ་ནི་སེམས་ཅན་གྱི་དོན་མཛད་པའོ། །

[Block 1537]
སྡོང་པོ་ལ་བརྟག་པ་ནི་སྐྱེ་བ་རྣམ་བཞིའི་སྐྱབས་མཛད་པར་དགོངས་པའོ། །

[Block 1538]
འཆག་པ་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་སྦྱིན་པར་དགོངས་པའོ། །

[Block 1539]
མདོ་ལས།

[Block 1540 [HEADING]]
###### **མི་ནུས་པར་སེམས་པ།** ^4-2-11-1-1-2-5-3-2-1-2-3-0

[Block 1541]
ཡེ་ཤེས་འདི་ནི་དམ་པ་ངོ་མཚར་ཆེ། སེམས་ཅན་འདི་དག་མི་མཁས་གཏི་མུག་ལྡོངས། །ཞེས་བྱ་བ༌[^1357]ནི་ཐར་བར་བྱར་མི་རུང་བར་དགོངས་པ་སྟེ་རྒྱུ་རྣམ་བཞིའི་ཕྱིར་རོ། །

[Block 1542]
ཆོས་ཟབ་པས་ཤེས་པར་དཀའ་བ་དང་། དབང་པོ་རྟུལ་བས་ཤེས་པར་དཀའ་བ་དང་། འདོད་པ་ལ་ཆགས་པས་གཏོང་མི་ཕོད་པ་དང་། གཏི་མུག་གིས་ལྡོངས་པས་ཐར་བར་བྱར་མི་རུང་ངོ་སྙམ་དུ༌[^1358]དགོངས་སོ། །

[Block 1543]
མདོ་ལས།

[Block 1544 [HEADING]]
###### **ཐབས་ཙམ་དུ་བསྟན་པར་དགོངས་པ།** ^4-2-11-1-1-2-5-3-2-1-3-0

[Block 1545]
དེ་ཚེ་ང་ལ་གསོལ་བ་ཚངས་པ་དང་། །ཞེས་པ་ནས། ཐམས་ཅད་ཐལ་མོ་སྦྱར་ནས་གུས་པར་འཁོད། །ཅེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས་བཅད་ཕྱེད་དང་བཅུ་གཉིས་ཐབས་ཙམ་དུ་བསྟན་པར་དགོངས་པ་བསྟན་པ་སྟེ། དེ་ལ་ཡང་རྣམ་པ་བཞིའོ། །
--- END BLOCKS ---
