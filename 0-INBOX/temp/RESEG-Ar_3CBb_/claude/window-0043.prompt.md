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
དེ་ལ་ཆགས་པ་ནི་དེ་ཡང་དག་པར་ངེས་པའི་ཚུལ་དུ་འཛིན་པའོ། །

[Block 1507]
འཁོར་བ་མ་ལུས་པར་འཇོམས་པ་ནི་གང་གིས་འཁོར་བ་མ་ལུས་པའི༌[^798]རྟོག་པ་འཇོམས་པའོ། །

[Block 1508]
གཞན་ཡང་དེ་བཞིན་ནོ། །

[Block 1509]
དོན་ཡོད་པ་གྲུབ་པ་ནི༌[^799]ཅིའི་ཕྱིར་ཞེ་ན་བྱ་བ་གྲུབ་པའི་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^800]བསྟན་ཏོ། །

[Block 1510]
འོད་གསལ་བ་ལ་ཅིའི༌[^801]ཕྱིར་ཞེ་ན་མཚན་མ༌[^802]མེད་པའི་འབྲས་བུ་སྟེར་བ་སྟེ་དེ་ལ་དམིགས་པས་དེ་འགྲུབ་པའི༌[^803]ཕྱིར་རོ། །

[Block 1511]
ཕྲག་དོག་ནི་གཞན་གྱི་ཡོན་ཏན་ལ་སེམས་ཁོང་ནས་འཁྲུགས་པ་སྟེ། གང་གིས༌[^804]དེ་དང་ལྡན་པའི་སེམས་ཅན་འདུལ་བར༌[^805]བྱེད་པ་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1512]
ཁམས་ཕྲ་བ་ནི་ལྟེ་བ་ལ་གནས་པའི་རླུང་སྟེ། དེས་ཐབས༌[^806]ཀྱི་ཡེ་ཤེས་བྱང་ཆུབ་ཀྱི་སེམས་བཀུག་ནས་མཆོག་ཏུ་དགའ་བ་སྐྱེད་པ་སྟེ་དེ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 1513]
རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ནི་རྟོག་པ་དང་དཔྱོད་པ་དང་། ངེས་པར་འབྱེད་པ་སྟེ། རྒྱུ་དེ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 1514]
འཛིན་པ་ནི་དེ་དང་ལྡན་པའོ། །

[Block 1515]
ཟླ་བ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 1516]
རླུང་གིས་འཛིན་པ་ནི་དེ་མི་གཏོང་བའོ། །

[Block 1517]
གདུལ་བྱ༌[^807]ནི་ཁམས་གསུམ་གྱི་སེམས་ཅན་ནོ། །

[Block 1518]
དེའི་མངོན་པར་འདོད་པ་ནི་དེའི་བླང་བར་བྱ་བའོ། །

[Block 1519]
ཟག་པ་མེད་པའི་བདེ་བ་ཆེན་པོ་ནི་ཆོས་ཀྱི་སྐུའོ། །

[Block 1520]
རིགས་འདི་རྣམས་ཞེས་པ་ནི་འོག་ནས་སྟོན་ཏོ། །

[Block 1521]
ཕུང་པོ་འདི་དག༌[^808]ནི་གཟུགས་ལ་སོགས་པ་སྟེ་དེ་ཉིད་དོན་དམ་པར་སངས་རྒྱས་དང་ངོ་བོ་གཅིག་པའི་ཚུལ་གྱིས་སོ། །

[Block 1522]
དེ་ལྟ་བུའི་དབུས༌[^809]སུ་མ་ཡིན་ནམ་སྙམ་པ་ལ། རྫོགས་པའི་བྱང་ཆུབ་རྐྱེན་དུ་བྱུང་། །ཞེས་པ་ནི་འདི་ལ་བརྟེན་ནས་བླ་ན་མེད་པའི་བྱང་ཆུབ་སྒྲུབ་པ་ཉིད་དོ། །

[Block 1523]
དེའི་ཕྱིར་ནི་ཐ་དད་དོ༌[^810]ཞེ་ན། དེ་བཞིན་ཉིད་དུ་གཉིས་མེད་པ། །ཞེས་དོན་དམ་པར་གཉིས་སུ་མེད་ཅིང་དབྱེར་མེད་པའོ། །

[Block 1524]
ཡང་རྣམ་པར་སྣང་མཛད་ཅེས་བྱ་བ་ལ་སོགས་པའི་དོན་ནི། །

[Block 1525]
རྫོགས་སངས་རྒྱས་ནི་ཆགས་པ་བྲལ། །འདོད་ཆགས་ཅན་ལ་དེ་ཉིད་དོ། །ཞེས་པ་ལྟ་བུའོ། །

[Block 1526 [VERSE]]
མཱ་མ་ཀཱི་ནི་འཁྲིག་པ་ཡི། །
རེག་བྱས་མཉེས་པར་བྱེད་པའི་ཕྱིར། །
འདའ་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1527]
ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 1528]
ཞེ་སྡང་ནི་མི་བསྐྱོད་པ་སྟེ་ཞེ་སྡང་ཅན་གྱིས༌[^811]འགྲོ་བ་འདུལ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1529]
དེ༌[^812]དགའ་བ་ནི་དེ་མཉེས་པར་བྱེད་པའི་ཚུལ་གྱིས་སོ། །

[Block 1530]
ཞེ་སྡང་རྣམ་པར་དག་པ་ནི་དེ་བཞིན་ཉིད་དེ་རྒྱུ་དང་ངོ་བོ་ལ་སོགས་པ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1531]
དེ་ལ་དགའ་བ་ནི་དེ་དང་དབྱེར་མེད་པའི་ཚུལ་གྱིས་ཏེ་ཡང་དག་པའི༌[^813]ཡེ་ཤེས་སོ། །

[Block 1532]
བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོ་དེ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པའི་དོན་ནི་དེ་དག་ཀྱང་རྡོ་རྗེ་འཆང་གིས་སེམས་ཅན་གྱི་དོན་དུ་དེ་ལྟར་བསྟན་གྱི་དོན་དམ་པར་ནི་མ་ཡིན་ནོ་ཞེའོ། །

[Block 1533]
གཞན་ལ་ཡང་དེ་ལྟར་ཤེས་པར་བྱའོ། །

[Block 1534]
སྐུ་དང་གསུང་དང་ཐུགས་མི་རྟག་པ༌[^814]ནི་སྐད་ཅིག་གཉིས་པ་ལ་སོགས་པར་མི་གནས་པའོ། །

[Block 1535]
སླུ་བ༌[^815]ནི་རྟག་པར་སེམས་པ་ལའོ། །

[Block 1536]
ཆོས་ཐམས་ཅད་སྟོང་པ་ནི་ཇི་ལྟར་བརྟག་པ༌[^816]དང་བྲལ་བའོ། །

[Block 1537]
སླུ་བ་ནི་ཡོད་པར་འཛིན་པའི་གང་ཟག་ལའོ། །

[Block 1538]
སྣང་བ་གསུམ་ནི་བཤད་ཟིན་ཏོ། །

[Block 1539]
སླར་ཡང་དངོས་པོ་མེད་པར་བྱས་པ་ནི་འོད་གསལ་བའི་ངང་དུ་སྟེ་དེ་ཉིད་ཡོད་པར་འཛིན་པ་ནི་གང་ཟག་ལའོ། །

[Block 1540]
ཕུང་པོ་ལ་སོགས་པ་ནི་སྦྱང་བར་བྱའོ།[^817] །རིལ་པོར་འཛིན་པ་ལ་སོགས་པ་ནི་སྦྱོར་བའི་ཐབས་སོ། །

[Block 1541]
དེ་ཐམས་ཅད་དབྱེ་བ༌[^818]མེད་པར་གྱུར་པ༌[^819]ནི་དེའི་འབྲས་བུའོ། །

[Block 1542]
འདི་ནི་ཐམས་ཅད་རང་གིས་བརྟགས་པས་སླུ༌[^820]བ་སྟེ།

[Block 1543]
བདེན་པར་གྱུར་པའི་དོན་མཐོང་བས། །དམན་ལ་བདེན་པར་གྱུར་པ་སླུ། །ཞེས་འབྱུང་བ་ལྟ་བུའོ། །

[Block 1544]
གཞན་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 1545]
གཤིན་རྗེ་ནི་དམྱལ་བའི་སྲུང་མ་དང་བཅས་པ་སྟེ་དེ་ན་དབང་ཆེ་བར་སྣང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
