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
གང་ཞིག་འདིར་ལྐུགས་པ་ལ་མ་ཡིན་ནོ་ཞེས་བྱ་བས་ནི་དེ་ལ་ཡང་གང་ཞིག་ཕུལ་བ་ཉིད་དེ་ནི་ཕུལ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1507]
རྣམ་པ་ཐམས་ཅད་དུ་སྨྲ་བར་མི་ནུས་པ་དེ་ནི། འདིར་ལྐུགས་པར་འདོད་དེ། དེ་ལ་གང་ཞིག་རབ་ཏུ་རིག་པ་དེ་ནི་རབ་ཏུ་རིག་པས་འདི་ཞུགས་པ་མ་ཡིན་ནོ། །

[Block 1508]
མི་མ་ཡིན་པའི་འགྲོ་བ་ལ༌[^1060]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ལྷ་དང་སྤྲུལ་པ་ལ་སོགས་པ་ལའོ། །

[Block 1509]
མ་གོ་བ་ཉིད་ལ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གླེན་པ་དང་འོན་པ་དང་སྙོམས་པར་ཞུགས་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་རྣམས་ཀྱང་བསྡུས་ཏེ། གླེན་པ་དང་འོན་པ་དག་བསྡུས་པ་ཉིད་ཀྱི་ཕྱིར་འདི་རྒྱུ་གཞན་མཐོང་བ་ཡིན་ཏེ། དེ་བས༌[^1061]རྣམ་པ་ཐམས་ཅད་དུ་གོ་བ་དང་ཉན་པའི་ཕྱིར་ཞེས་བྱ་བ་གྲངས་ཇི་ལྟ་བ་བཞིན་དུ་འདིར་མི་ནུས་པ་ནི་གླེན་པ་དང་འོན་པ་དག་ལ་འདོད་པ་རྣམ་པར་གནས་པ་ཡིན་ཏེ། གང་དང་ཉེ་བར་ཕུལ་བ་དེ་ལ་གོ་བ་ཉིད་ལ་ཞེས་བྱ་བ་འདི་འདིར་ཤུགས་ཀྱིས་རྟོགས་པ་ཡིན་ནོ། །

[Block 1510]
དབེན་པར་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་དབེན་པའི་འདུ་ཤེས་ཀྱིས་སམ་དབེན་པ་མ་ཡིན་པའི་འདུ་ཤེས་ཀྱིས་དབུལ་བ་ཉིད་བྱས་ན་ཡང་དེ་ཕུལ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1511]
དེ་བས་ན་ལྟོས་པ་དང་བཅས་པ་ཉིད་ལ་འདིར་དབེན་པའི་འདུ་ཤེས་ཀྱིས་ལྐུགས་པའི་ཡུལ་ལ་ཞུགས་པ་བཞིན་དུ་འགྱུར་ཏེ། ཐམས་ཅད་དུ་བྱེད་པའི་རིམ་པའོ། །

[Block 1512]
དབེན་པར་འདུ་ཤེས་པས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མི་དབེན་པར་དབེན༌[^1062]པའི་འདུ་ཤེས་ཀྱིས་ཕུལ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1513]
འདིར་ཕུལ་བ་ཉིད་ནི་རྒྱུ་ཅིས༌[^1063]མི་འདོད་ཅེ་ན། གང་གི་ཕྱིར་མ་ཉམས་པའི་འདུ་ཤེས་ཀྱིས་ཐ་སྙད་གྱི་ཡུལ་ཐམས་ཅད་དུ་བྱེད་པའི་རིམ་པ་ཐམས་ཅད་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་ཕུལ་བ་ཉིད་དོ། །

[Block 1514]
གཉིད་ལོག་པ་ན་བླ་བར་འགྱུར་བ་ཉིད་ཀྱིས་འདུ་ཤེས་མ་ཉམས་པ་ཉིད་ལ་ལ༌[^1064]ཀུན་ནས་སྤྱོད་པ་ཉིད་ལ་གནས་སྐབས་དེ་དང་ལྡན་པས་ཕུལ་བ་ཉིད་མ་ཡིན་ཏེ། རང་བཞིན་ཉམས་པ་དང་ལྐུགས་པ་དང་མ་གོ་བ་ཉིད་དང་དབེན་པར་ཐམས་ཅད་དུ་བྱེད་པ་མེད་པའི་ཕྱིར་རོ།[^1065] །གང་གི་ཕྱིར་ཐམས་ཅད་དུ་བྱེད་པ་མ་ཡིན་པ་ལ་འདི་ལྟར་བདག་ནི་ཐ་སྙད་ལ་གནས་ཞེས་བྱ་བའི་བསམ་པ་རྫོགས་པ་མ་ཡིན་ནོ། །

[Block 1515]
མི་མ་ཡིན་པའི་འགྲོ་བ་པ་ལ་ཐ་སྙད་དུ་བྱ་བ་མེད་པའི་ཕྱིར་དང་དབེན་པའི་འདུ་ཤེས་ཀྱིས་ཐམས་ཅད་དུ་བྱེད་པ་རྩོམ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1516]
ཐམས་ཅད་དུ་བྱེད་པ་རྩོམ་པ་ཉིད་མེད་པ་བདག་འདི་ལྟར་ཐ་སྙད་ལ་གནས་ཞེས་བྱ་བ་བསམ་པ་རྫོགས་པ་མ་ཡིན་ནོ། །

[Block 1517]
དེ་བས་ན་ལྟོས་པ་དང་བཅས་པ་ཉིད་རང་གི་འདོད་པས་རབ་ཏུ་གྲོལ་ཞིང་སེམས་རབ་ཏུ་བཟུང་བར་འགྱུར་རོ། །

[Block 1518]
དེ་བས་ན་འདིར་ཕུལ་བ་ཉིད་འདོད་པ་མ་ཡིན་ནོ། །

[Block 1519]
བསླབ་པའམ། སངས་རྒྱས་སམ་ཆོས་སམ་དགེ་འདུན་ནམ་མདོ་སྡེའམ་འདུལ་བའམ་མ་མོའམ། སློབ་དཔོན་ནམ་མཁན་པོ༌[^1066]འབུལ་ལོ། །

[Block 1520]
བདག་ཁྱིམ་པའམ། དགེ་ཚུལ་ལམ། ཟ་མའམ། མ་ནིང་ངམ། དགེ་སློང་མ་སུན་ཕྱུང་བའམ། རྐུ་ཐབས་སུ་གནས་པའམ། ཐ་དད་པར་གནས་པའམ། གནས་པར་མི་བྱ་བའམ། མུ་སྟེགས་ཅན་ནམ། མུ་སྟེགས་ཅན་ཞུགས་པའམ། མ་བསད་པའམ། ཕ་བསད་པའམ། དགྲ་བཅོམ་པ་བསད་པའམ། དགེ་འདུན་གྱི་དབྱེན་བྱས་པའམ། དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བར་གཟུང་དུ་གསོལ། །བདག་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་ཁྱེད་ཅག་དང་ལྷན་ཅིག་གནས་པའམ་ལོངས་སྤྱོད་པས་ཆོག་གོ་ཞེས་བྱ་བ་ལྟ་བུ་ནི་འབུལ་བའི་ཚིག་དག་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ལྟ་བུ་ཞེས་བྱ་བའི་སྒྲ་ནི་རྣམ་པ་གསུམ་བསྟན་པའི་ཕྱིར་ཏེ། རྣམ་པ་དེ་ལྟ་བུ་དང་ཆོ་ག་དེ་ལྟ་བུ་དང་། རིགས་དེ་ལྟ་བུ་རྣམས་ནི་འབུལ་བའི་ཚིག་རྣམས་རྩོམ་པའོ། །

[Block 1521]
སླར་མདོ་འདི་ལ་དེ་ལྟར་ན་བསླབ་པ༌[^1067]འབུལ་བ་ནི་ཚིག་ཏུ་སྨྲ་བ་དེ་ཁོ་ན་ལས་བསླབ་པ་འབུལ་བར་མ་ཟད་ཀྱི། ཚིག་ཏུ་མ་སྨྲས་པར་རྣམ་པ་གང་ཡང་རུང་བས་གཏོང་བའི་མཚན་མ་ལས་ཀྱང་ཕུལ་བར་འགྱུར་ཏེ། དེས་ན་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་ལས་ཀྱང་འདིར་ཕུལ་བར་འགྱུར་ལ། ངག་གི་རྣམ་པར་རིག་བྱེད་ལས་ཀྱང་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 1522]
འདིར་སླར་རིགས་པ་ནི་འཕོ་བ་བསྟན་པས་འདིར་དགོས་པ་ཡིན་གྱི༌[^1068]ཚིག་གི༌[^1069]ཁྱད་པར་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 1523]
དོན་གཞན་སྟོན་པའི་སྒྲ་ལས་དོན་གཞན་ཁོང་དུ་ཆུད་པ་ཞེས་བྱ་བ་འགྲུབ་པ་ཡིན་ནོ། །

[Block 1524]
དེ་བཞིན་དུ་འཕོ་བ་ལ་དགོས་པས། ཚིག་ཏུ་སྨྲས་པ་དང་། ཚིག་ཏུ་མ་སྨྲས་པར་ཤེས་པ་དང་། རྟོགས་པ་གཞན་གྱིས་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་ཀྱིས༌[^1070]ཉམས་པ་འདི་ལ་སྒྲུབ་པར་བྱེད་པ་ཡིན་གྱི༌[^1071]གཞན་དུ་ནི་མ་ཡིན་ཞེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་གོ། །

[Block 1525]
གཞན་གྱིས་གོ་བར་བྱས་པ་ལ་འདིར་དོན་ཡིན་པའི་ཕྱིར་གང་དུ་སུ༌[^1072]ཞིག་གིས་རྣམ་པ་གང་ཡང་རུང་བས་བསླབ་པ་འདིས་ཡོངས་སུ་བཏང༌[^1073]ངོ་ཞེས་བྱ་བ་གཞན་གྱིས་རྟོགས་པར་གྱུར་ན་ཕུལ་བ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1526]
ལྟ་བུ་ནི་དབུལ་བའི་ཚིག་རྣམས་ཡིན་ནོ་ཞེས་བྱ་བས་ངག་གི་རྣམ་པར་རིག་བྱེད་ཉིད་ལས་ཡོངས་སུ་བཟུང་བ་ཡིན་ནོ། །

[Block 1527]
འབུལ་བའི་བྱ་བ༌[^1074]ལ་འདི་ལྟ་བུའི་ཚིག་རྣམས་ཞེས་བྱ་བ་འདིའི་དོན་ཡིན་ཏེ། ཚིག་ཉིད་ནི་འབུལ་བར་བྱེད་པ་ཞེས་བྱ་བ་འདི་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1528]
ཚེ་དང་ལྡན་པ་དགོངས་སུ་གསོལ་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་ཞིག་འདིར་འདོན་པ་དེ་ནི་མི་གཡེང་བ་ཉིད་སྦྱིན་དུ་བཅུག་པས་དགེ་སློང་གི་ཚིག་གིས༌[^1075]འདོན་པ་ཡིན་ནོ། །

[Block 1529]
འདི་ནི་སྔགས་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་འདིར་སྔགས་ཀྱི་དགོས་པ་མ་ཡིན་ཏེ། དོར་བ་ཙམ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་འདི་ནི་སོང་བ་ཙམ་དུ་ཟད་དོ། །

[Block 1530]
སངས་རྒྱས་སམ། ཆོས་སམ་དགེ་འདུན་ནམ་ཞེས་བྱ་བ་ནི་དཀོན་མཆོག་འདུལ་བ་ལ་ཡང་དག་པར་བརྟགས་པའི་དོན་དུ་འདི་ནི་འདི་ལྟ་བུ་མ་ཡིན་པ་དང་། འདི་ལྟ་བུ་ཅུང་ཟད་ཡོད་པ་མ་ཡིན་པ་དང་། འདི་ནི་འདི་ལྟ་བུ་ཡོད་དམ་འོན་ཏེ་མ་ཡིན་སྙམ་པ༌[^1076]འདིས་བདག་ལ་རེ་ཞིག་དགོས་པ་མེད་ཅེས་བྱ་བ་རྟོགས་པ་གསུམ་མོ། །

[Block 1531]
མདོ་སྡེའམ་འདུལ་བའམ་མ་མོའམ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་དུ་སྡེ་སྣོད་འབུལ་བ་ལ། འདི་ནི་གཏོང་བའི་ཆོ་ག༌[^1077]ཡིན་པ་དང་། འདི་ལྟ་བུ་གཏོང་བའི་ཆོ་ག་ཡོད་པ་མ་ཡིན་པ་དང་། གཏོང་བའི་ཆོ་ག་འདི་ནི་ཡོད་དམ། འོན་ཏེ་མ་ཡིན་སྙམ་དུ་འདིས་བདག་ལ་རེ་ཞིག་དགོས་པ་མེད་ཅེས་བྱ་བ་ལ། དང་པོ་བདག་གི་འདོད་པ་བརྟགས་པ༌[^1078]ནི།

[Block 1532 [VERSE]]
མེད་ན་བདེན་པར་བརྟེན་འདོད་ལ། །
གཏོང་བའི་ཆོ་ག་བདེན་པར་འདོད། །

[Block 1533]
ཅེས་བྱ་བས་འབུལ་བར་བྱ་བ་མ་ཡིན་པ༌[^1079]འབུལ་བ་ཉིད་དོ། །

[Block 1534]
གཞན་ལ་བརྟེན་པའི་གཏོང་བའི་ཆོ་ག་འདི་ཡོད་དམ། དོན་གཞན་ལ་བརྟེན་པའི་གཏོང་བའི་ཆོ་ག་འདི་ཡོད་པ་མ་ཡིན་ཞེ་ན། འདུལ་བ་ཡོད་པ་མ་ཡིན་པ་དང་། འདི་ལྟ་བུ་ནི་ཅུང་ཟད་ཡོད་པ་མ་ཡིན། འདི་ལྟ་བུར་ཡོད་དམ་འོན་ཏེ་མ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདིས་རེ་ཞིག་བདག་ལ་དགོས་པ་མེད་དོ། །

[Block 1535]
གཏོང་བའི་ཆོ་ག་འདི་ལྟ་བུ་ཡོད་པ་མ་ཡིན་པ་དང་། འདི་ནི་ཡོད་དམ་འོན་ཏེ་མ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རེ་ཞིག་འདིས་བདག་ལ་དགོས་པ་མེད་ཅེས་བྱ་བ་རྣམས་ཀྱིས་རྣམ་རྟོག༌[^1080]མེད་པར་འབུལ་བའོ། །

[Block 1536]
འདི་ནི་སྡོམ་པའི་རྟེན་ཡིན་ཏེ། གང་ཞིག་གསུམ་པོ་འདི་དེ་བས་ན་འདི་འབུལ་བས་བསླབ་པ་འབུལ་བ་ལ་ཡིད་ཆེས་པའོ། །

[Block 1537]
སློབ་དཔོན་ནམ་མཁན་པོ་འབུལ་ལོ་ཞེས་བྱ་བ་ནི་སྡོམ་པའི་མཚན་མར་འདི་འབྲེལ་པ་ཡིན་ཏེ། གང་ཞིག་སློབ་དཔོན་ཉིད་དང་མཁན་པོ་ཉིད་འདི་དག་འབུལ་བ་ལ་ཡིད་ཆེས་པའོ། །

[Block 1538]
ཀློག་པའི་སློབ་དཔོན་ལ་ནི་ཆོ་ག་འདི་ཉིད་བདག་གིས་བརྗོད་པ་ཡིན་ཏེ། གང་ཞིག་པའི་དོན་དུ་དང་གཞན་འདི་ལྟ་བུ་ལ་སློབ་དཔོན་ཉིད་དེ་བདག་ལ་སླར་འདིའམ། གཞན་སློབ་དཔོན་འདི་ལྟ་བུ་གང་ལ་སྟེ་ཞེས་བྱ་བའི་ཆོ་ག་གཏོང་བའི་བརྟགས༌[^1081]པས་འབུལ་ལོ། །

[Block 1539]
གནས་ཀྱི་སློབ་དཔོན་ལ་ཡང་དེ་ལྟ་བུ་ཉིད་དུ་གཏོང་བའི་ཆོ་གས་སོ། །

[Block 1540]
གལ་ཏེ་མཁན་པོ་ཉིད་ལ་སླར་རྣམ་པར་བཅད་ནས་འབུལ་བ་ཉིད་བསྙེན་པར་རྫོགས་པའི་མཁན་པོ་ལ་འབུལ་བ་ཞེས་བྱ་བ་བསྙེན་པར་རྫོགས་པ་ལ་འབུལ་བ་རྣམ་པར་གཅད༌[^1082]ནས་དགེ་ཚུལ་ཉིད་ལ་ཡང་ངོ་། །བདག་ཁྱིམ་པའམ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་ཉིད་དུ་དམ་བཅས་པ་ལ་རབ་ཏུ་བྱུང་བའི་སྡོམ་པ་ཡོད་པའི་དངོས་པོ་མེད་དེ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་ཉིད་སོ་སོར་ཤེས་པ་ལ་བསླབ་པ་འབུལ་བ་ཉིད་གོ་བར་བྱེད་པའོ། །

[Block 1541]
དགེ་ཚུལ་ལམ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པ་ཉིད་དགེ་ཚུལ་ལ་བརྟེན་པ་ཞེས་བྱ་བ་ཡོད་པ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་དགེ་ཚུལ་ལ་བརྟེན་པ་ཉིད་ཤེས་པ་ལ་བསྙེན་པར་རྫོགས་པ་འབུལ་བ་ལའོ། །

[Block 1542]
ཟ་མའམ་མ་ནིང་ངམ་ཞེས་བྱ་བ་ནི་ཞིང་མ་ཡིན་པ་ལ་སྡོམ་པའི་དངོས་པོ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཟ་མའམ་མ་ནིང་ཉིད་དུ་དམ་བཅས་པ་ལ་སྡོམ་པ་ཐམས་ཅད་འབུལ་བ་ལའོ། །

[Block 1543]
དགེ་སློང་མ་སུན་ཕྱུང་བའམ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་སུན་ཕྱུང་བ་ཉིད་ནི་ཞིང་མ་ཡིན་པ་ཉིད་ཀྱི་རྟོག་པས་གལ་ཏེ་དམ་བཅས་ན་དེ་ལྟ་བུ་ཉིད་འདི་ལ་གོ་བ་ཉིད་དེ་ཕམ་པ་ཉིད་ཀྱི་བསམ་པས་གལ་ཏེ་འཕོ་བ་ཉིད་འདིར་རབ་ཏུ་བྱུང་བའི་ཕྱིར་ཞེས་བྱ་བའི་བློ་གང་ཡིན་པ་དེའི་དབང་གིས་སོ། །

[Block 1544]
རྐུ་ཐབས་སུ་གནས་པའམ་ཞེས་བྱ་བ་ནི་དམ་བཅས་པ་ལ་ཞིང་མ་ཡིན་པ་ཉིད་ཀྱི་བསམ་པ་ཉིད་ལ་ཟ་མ་དང་མ་ནིང་ཉིད་དུ་དམ་བཅས་པ་བཞིན་གོ་བར་བྱེད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1545]
སྡོམ་པ་མ་བླངས་པའི་བསམ་པ་ཉིད་ལ་ཁྱིམ་ན་གནས་པ་དམ་བཅས་པ་བཞིན་དུའོ། །
--- END BLOCKS ---
