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
དེ་གཉིས་ཀ་ལ་ཡང་ཇི་ལྟར་རིགས་པར༌[^941]སྦྱར་བ་ཞེས་བྱ་བས་གཉིས་ཀ་བསྡུས་པ་ཡིན་ནོ། །

[Block 1507]
མགུལ་རྒྱན་དང་གདུ་བུ་རྒྱན་ཅན་དང༌[^942]དཔུང་རྒྱན་དང་དོ་ཤལ་དང་སེ་མོ་དོར་གནས་པ་ཉིད་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ས་ལེ་སྦྲམ་དང་དངུལ་ལས་བྱས་པ་ཉིད་གང་ཞིག་འདིར་དེ༌[^943]ལ་འདི་ལྟ་བུར་འདུག་པའི་ངོ་བོ་མ་ཡིན་པ་ལ་འདི་དག་ལ་དངོས་གཞིའི་བྱེད་པ་པོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུ་བཟུང་བའོ། །

[Block 1508]
པི་ཝང་དང་གླིང་བུ་དང་བ་ལ་རི་དང་མ་ཧཱ་ཏི་དང་སུ་གྷོ་ཥ་ཀ་རྣམས་ནི་རྒྱུད་དང་བཅས་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་ནི་རུང་བར་གྱུར་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་སྟེ་འདིར་ཐམས་ཅད་དུ་སྦྱར་བར་བྱའོ། །

[Block 1509]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་པི་ཝང་ལེན་ན་རྒྱུད་དང་བཅས་པ་ལེན་ན་ལྟུང་བྱེད་དུ་འགྱུར་ལ་རྒྱུད་མེད་པ་ལེན་ན་ལྟུང་བ་ཉེས་པ་ཅན༌[^944]དུ་འགྱུར་རོ། །

[Block 1510]
པི་ཝང་ཇི་ལྟ་བ་བཞིན་དུ་གླིང་བུ་དང་བ་ལ་རི་དང་མ་ཧཱ་ཏི་དང་སུ་གྷོ་ཥ་ཀ་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1511]
དུང་དང་རྔ་བོ་ཆེ་དང་རྔ་པ་ཊ་ཧ་དང་རྫ་རྔ་རྣམས་ནི་སྒྲ་འབྱིན་ནའོ་ཞེས་བྱ་བ་ནི་རུང་བར་གྱུར་པ་ཡིན་ནོ། །

[Block 1512]
གཞན༌[^945]ནི་རྒྱུད་དང་བཅས་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་ནི་རུང་བར་གྱུར་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བར་འཇུག་གོ། །

[Block 1513]
རལ་གྲི་དང་རལ་གྲི༌[^946]ཁྱོག་པོ་དང་རལ་གྲི་སོ་གཅིག་པ་དང་མདུང་དང་འཕང་མདུང་དང་ལྕགས་ཀྱུ་རྣམས་ནི་དེ་ཉིད་ཡིན་ནའོ་ཞེས་བྱ་བ་ནི་རལ་གྲི་ལ་སོགས་པ་རྣམས་ཀྱི་དེ་དག་ཉིད་ཡིན་ན་རལ་གྲི་ལ་སོགས་པ་རུང་བ༌[^947]ཉིད་ལ་རུང་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1514]
མདའ་དང་ལྕགས་མདའ་དང་མདའ་ཕྱེད་ལྕགས་ལས་བྱས་པ་རྣམས་ནི་མདེའུ་དང་བཅས་པ་ཉིད་ཡིན་ནའོ་ཞེས་བྱ་བ་ནི་རུང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1515]
སྐུ་གཟུགས་ནི་སྐུ་གདུང་དང་བཅས་པ་ཉིད་ཡིན་ནའོ་ཞེས་བྱ་བ་ནི་གང་གིས༌[^948]འདི་འདྲ་བ་དེ་ནི་མཚོན་པར་བྱེད་པ་རྣམས་སོ། །

[Block 1516]
འདིར་སོ་སོར་ཉེ་བར་གནས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1517]
སྐུ་གདུང་དང་བཅས་པ་ཉིད་ཡིན་ན་ཡོངས་སུ་རྫོགས་པ་ཉིད་དེ་ལ་སོ་སོར་ཉེ་བར་གཞག་པ་ཉིད་དོ། །

[Block 1518]
ཉེ་བར་དགོས་པ་ཉིད་ལ་འདིའི་ངོ་བོ་ཉིད་ལྟར་སྐུ་གདུང་དང་བཅས་པའི་སྐུ་གཟུགས་བསྟན་པའོ། །

[Block 1519]
རིན་པོ་ཆེའི་རང་བཞིན་ཉིད་ལ་སྐུ་གདུང་དང་བཅས་པ་ཉིད་ནི་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 1520]
སྐུ་གདུང་དང༌[^949]བཅས་པ་མ་ཡིན་ན་ནི་ཉེས་བྱས་སོ། །

[Block 1521]
རིན་པོ་ཆེའི་རང་བཞིན་མ་ཡིན་པ་ཉིད་ལ་སྐུ་གདུང་དང་བཅས་པ་ཉིད་ན་ནི་ཉེས་བྱས་སོ། །

[Block 1522]
སྐུ་གདུང་མེད་པ་ཉིད་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1523]
འདིར་ལྕི་བ་ཡོངས་སུ་སྤང་བའི༌[^950]དོན་དུ་དྲན་པ་ཉེ་བར་གཞག་པ་ཞེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་པར༌[^951]རིག་པར་བྱའོ། །

[Block 1524]
མཆོད་རྟེན་རིན་པོ་ཆེ་ལས་བྱས་པ་ལ་ནི་དགོས་པ་ཉིད་མེད་པ་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་འདིར་ཡང་རིན་པོ་ཆེའི་རང་བཞིན་དང་སྐུ་གདུང་དང་བཅས་པ་ཉིད་དག་ལ་ལྟུང་བྱེད་དོ། །

[Block 1525]
གང་ཡང་རུང་བ་གཅིག༌[^952]མ་ཚང་ན་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 1526]
ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་དང་སྐུ་གདུང་དང་བཅས་པ་ཉིད་ལ་ནི་དེ་དག་གི་སྐུ་གདུང་དང་བཅས་པ་ཡང་རུང་། སངས་རྒྱས་ཀྱི་སྐུ་གདུང་དང་བཅས་པ་ཡང་རུང་སྟེ། ཉེས་བྱས་སུ་འགྱུར་བ་ཉིད་དུ་རྟོགས་པར་བྱའོ། །

[Block 1527]
སྲེད་མེད་ཀྱི་བུ་ལ་སོགས་པའི་གཟུགས་རིན་པོ་ཆེ་ལས་བྱས་པ་ཉིད་མ་ཡིན་པ་སྐུ་གདུང་དང་བཅས་པ་ཉིད་ནི་དེ་དག་གི་རུས་པ་དང་བཅས་པ་ཡང་རུང་སངས་རྒྱས་ཀྱི་སྐུ་གདུང་དང་བཅས་པ་ཡང་རུང་སྟེ་ཉེས་པ་མེད་དོ། །

[Block 1528]
རིན་པོ་ཆེ་ལས་བྱས་པ་ཉིད་ཡིན་ན་ནི་རྫས་ཙམ་གྱི་དབང་ལས་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 1529]
དེ་ལ་སྟོན་པའི་འདུ་ཤེས་ཉེ་བར་གཞག་ན་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་སྐུ་གཟུགས་དེ་དག་ལ་སྟོན་པའི་འདུ་ཤེས༌[^953]ཉེ་བར་བཞག༌[^954]སྟེ། རེག་གམ་རེག་ཏུ་བཅུག་པ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1530]
ནོར་བུ་མཆིང་བུ་དང་སོག་མའི་ཕྲེང་བ་དང་མཆུ༌[^955]སྒྲེང་དང་རྫ་རྔ་ཁ་ཅིག༌[^956]པ་དང་གཞུ་དང་མདའ་ལྟར་བཅོས་པ་རྣམས་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ལ། མདའ་ལྟར་བཅོས་པ་ཞེས་བྱ་བ་ནི་ལྟོང་ལ་སོགས་པ་དང་སྦྱར་བས་མདའི་རྣམ་པ་ཉིད་དུ་ཉེ་བར་གྱུར་པ་སྟེ། ཤིང་བུ་ལ་སོགས་པ་དག་ལས་ལྟོང་ཙམ་བཏོད་ཅིང་འོལ༌[^957]བྱི་ཙམ་མདའ་འདྲ་བ་བྱས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1531]
འདིར་མཆིང་བུ་ལ་སོགས་པའི་ཚིག་ནི་དཔེ་ཙམ་དུ་ཟད་དེ། ས་ལས་བྱས་པའི་ནོར་བུ་དག་ཀྱང་ཕྱེད་ཉིད་དེ་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 1532]
གསེར་གྱི་སྟེགས་བུ་ནི་མི་རུང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། རྣམ་པ་འདི་ལྟ་བུ་ཉིད་ནི་མཁོ་བའི་ཡོ་བྱད་དུ་གྱུར་པ་ཉིད་མ་ཡིན་ཏེ། གང་ཞིག་འདི་ལ་སྟེགས་བུ་ལ་སོགས་པ་ཉེ་བར་མཁོ་བའོ། །

[Block 1533]
མི་རུང་བ་ཉིད་ལ་གྲུབ་པས་ཐམས་ཅད་དུ་གྱུར་པའི་ཡོངས་སུ་གྲུབ་པའི་དོན་ལའོ། །

[Block 1534]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་དགེ་སློང་གསེར་གྱི་སྟེགས་བུ་ལ་འདུག་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1535]
འཇིགས་པར་གྱུར་ན་རང་གི་ལ་མི་གནོད་ན་དགེ་འདུན་གྱི་དང་མཆོད་རྟེན་གྱི་དབྱིག་དང་གསེར་སྦས་སམ་ཁྱེར་ཏེ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞུང་ཁ་ཅིག་ལས་འདིར་སྦས་ནས་ཁྱེར་ཏེ་འགྲོ་བར་བྱའོ་ཞེས་འབྱུང་ངོ་། །གཞན་དུ་ནི་དགེ་སློང་གིས་དགེ་འདུན་གྱི༌[^958]མི་ཟད་པའི་གཏེར་ཁྱེར་ཏེ། ཁྱིམ་པ་དང་དགེ་ཚུལ་དག་ལ་བྱིན་པ་དང་དེ་དག་གིས་ཁྱེར་སྟེ་བྲོས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཁྱིམ་པ་ཡིད་ཆེས་པ་མ་ཡིན་པ་ལ་ཁྱིམ་པའམ། དགེ་ཚུལ་ལ་དགེ་འདུན་གྱི་མི་ཟད་པའི་གཏེར་རྣམས་ལག་ཏུ་སྦྱིན་པར་མི་བྱའོ། །

[Block 1536]
གལ་ཏེ་ཡིད་ཆེས་པར་གྱུར་ན་ནི་སྦྱིན་པར་བྱའོ། །

[Block 1537]
འོན་ཏེ་ཡིད་ཆེས་པར་མ་གྱུར་ན་དགེ་སློང་རང་གིས་ཁྱེར་ཏེ་འགྲོ་བར་བྱ་ཞིང་གང་གི་ཚེ་གཙུག་ལག་ཁང་དེ་ཉིད་ན་གནས་པ་ཡིན་ན་དེའི་ཚེ་དེ་ཉིད་དུ་སྦྱིན་པར་བྱའོ། །

[Block 1538]
འོན་ཏེ་གཙུག་ལག་ཁང་པ༌[^959]ཞིག་ན་གནས་པ་མ་ཡིན་ན་གཙུག་ལག་ཁང་དེ་ཉིད་དུ་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1539]
དེར་གཉིས་ཀ་ལྟར་ཡང་ཇི་ལྟར་ཉེ་བར་དགོས་པར་གྱུར་པ་རྟོགས་པ་ཕྱིར་འཐད་པ་ཡིན་ནོ། །

[Block 1540]
དེ་བས་ན་དེ་གཉིས་ཀ་ཡང་འདིས༌[^960]བསྡུས་པ་ཡིན་ནོ། །

[Block 1541]
རང་གི་ལ་མི་གནོད་ན་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དགེ་འདུན་ནམ་མཆོད་རྟེན་གྱི་སྦ་བར་བྱ་བ་ལ་བདག་ཉིད་ཀྱི་དོན་ལ་མི་སྦ་བར་ཁྱེར་བ་དང་མ་ཁྱེར་བར་གནོད་པར་གྱུར་ན་ནི་དེ་ལྟ་བུ་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1542]
རང་གི་ལ་ཞེས་བྱ་བ་ནི་ཆོས་དང་ལྡན་པ་དེའི་འོ། །

[Block 1543]
གང་ཞིག་མེད་པར་ལུས་གནས་པའམ་ཆོས་སྒྲུབ་པ༌[^961]ལ་གནོད་པར་འགྱུར་བ་རྨོངས་པའི་ཡོ་བྱད་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 1544]
དགེ་འདུན་གྱིས་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་དེར་དགེ་སློང་རྣམས་ཀྱིས་དགེ་འདུན་གྱི༌[^962]མི་ཟད་པའི་གཏེར་རྣམས་ཁྱེར་བ་དང་། དེ་དག་གི་ལྷུང་བཟེད་དང་ཆོས་གོས་དང་འཁྱམས་ནས་སྐབས་དེ་དགེ་སློང་དག་གིས་བཅོམ་ལྡན་འདས་ལ་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་ལྟར་མི་བྱ་སྟེ་གང་ཟག་ནི་ཕོངས་པར་འགྱུར་གྱི་དགེ་འདུན་ནི་མི་འགྱུར་བས་དེའི་ཕྱིར་དགེ་སློང་གིས་དང་པོར་རང་གི་ལྷུང་བཟེད་དང་ཆོས་གོས་བསྐུར་བར༌[^963]བྱ་ཞིང་གལ་ཏེ་བསྲུང་བར་ནུས་ན་ཕྱིས་དགེ་འདུན་གྱི་ལ་ཡང་འབད་པར་བྱའོ། །

[Block 1545]
མཆོད་རྟེན་གྱི་ལ་ཡང་ཞེས་བྱ་བ་ནི་དེ་ཡང་གང་དུ་སྦས་ནས་འགྲོ་བ་ཀློག་པ་ལས་དེར་གསུངས་པ་རིང་བ་ཉིད་ཀྱི་ཕྱིར་འདིར་མ་བརྟགས་སོ། །
--- END BLOCKS ---
