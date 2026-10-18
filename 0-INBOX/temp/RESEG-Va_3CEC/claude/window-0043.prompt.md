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
སྙན་པར་སྨྲ་བ་ནི་སློང་བ་རྣམས་ལ་མི་སྨོད་པའོ་ཞེས་བྱ་བ་ལ། ཟང་ཟིང་སློང་བ་པོ་རྣམས་ལ་རིགས་ངན་འདི། དབུལ་པོ་འདི་ཞེས་བྱ་བ་ལ་སོགས་པ་སེམས་གདུང་བར་འགྱུར་བའི་ཚིག་མི་སྨྲ་བ་ནི་སྙན་པར༌[^1293]སྨྲ་བའོ། །

[Block 1507]
དེ་ལ་དོན་སྤྱོད་པ་ནི་གང་སློང་བ་རྣམས་ཀྱི་དོན་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའོ་ཞེས་བྱ་བ་ལ། སློང་བ་རྣམས་ཚེ་འདིར་ཡང་དབུལ་བ་མེད་པར་བྱ་སྟེ། ལོངས་སྤྱོད་ཀྱི་འབྱོར་པ་དང་ལྡན་པར་བྱས་ནས། མི་དགེ་བ་ལ་མི་འཛུད་ཅིང་དགེ་བ་ལ་འཇོག་པ་ནི་དོན་སྤྱོད་པ་ཞེས་བྱའོ། །

[Block 1508]
དེ་ལ་དོན་མཐུན་པ་ནི་གང་ཐེག་པ་དེ་ཉིད་ལ་ཡང་དག་པར་འཛུད་པའོ་ཞེས་བྱ་བ་ལ། གང་ནི་སློང་བ་པོའི་གང་ཟག་གམ་བྱང་ཆུབ་སེམས་དཔའ་གང་ངོ་། །ཐེག་པ་དེ་ཉིད་ལ་ཡང་དག་པར་འཛུད་ཅེས་བྱ་བ་ནི་གང་ཟག་དེ་ཐེག་པ་གང་ལ་དད་པའི་ཐེག་པ་དེ་ཉིད་ལ་གང་ཟག་དེ་འཛུད་པའམ། བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་གང་ལ་གནས་པའི་ཐེག་པ་དེ་ཉིད་ལ་སློང་བ་པོའི༌[^1294]གང་ཟག་དེ་འཇུད་པ་སྟེ། འདི་ནི་དོན༌[^1295]མཐུན་པ་ཞེས་བྱའོ། །

[Block 1509]
རྣམ་གྲངས་གཞན་བསྟན་པར་བཞེད་ནས། གཞན་ཡང་སྦྱིན་པ་ནི་བསམ་པ་ཐག་པ༌[^1296]ནས་སྟོང་པའོ༌[^1297]ཞེས་བྱ་བ་གསུངས་ཏེ། བཟའ་བ་དང་བགོ་བ་ལ་སོགས་པའི་ཟང་ཟིང་རྣམས་ལ་ཅུང་ཟད་ཀྱང་ཆགས་པའི་སེམས་མེད་པར་སྟོང་པ༌[^1298]ནི་སྦྱིན་པའོ། །

[Block 1510]
སྙན་པར་སྨྲ་བ་ནི་གང་སྦྱོར་བ་ལ་ཡོངས་སུ་ཆད་པ་མེད་པའོ་ཞེས་བྱ་བ་ལ། སློང་བ་པོ་རྣམས་ལ་ཕྱིས་ཀྱང་སྦྱིན་པར་བྱ་ཡིས་རྒྱུན་དུ་ཤོག་ཅིག་ཅེས་སྨྲས་ནས་སྦྱིན་པ་གཏོང་བའི་ལས་རྒྱུན་མི་འཆད་པར༌[^1299]བྱེད་པ་ནི་སྙན་པར་སྨྲ་བའོ། །

[Block 1511]
དོན་སྤྱོད་པ་ནི་གང་ལྷག་པའི་བསམ་པས་སྦྱིན་ཏེ་འགྱོད་པ་མེད་པའོ་ཞེས་བྱ་བ་ལ་རྒྱུན་དུ་དངོས་པོས༌[^1300]བཏང་བར་སེམས་པའི་བསམ་པས་བྱིན་ནས་བྱིན་པ་ཉེས་སོ་སྙམ་དུ་འགྱོད་པ་མེད་པ་ནི་དོན་སྤྱོད་པའོ། །

[Block 1512]
དོན་མཐུན་པ་ནི་གང་ཐེག་པ་ཆེན་པོ་ལ་བསྔོའོ༌[^1301]ཞེས་བྱ་བ་ལ། སློང་བ་པོ་རྣམས་ཟང་ཟིང་གིས་བསྡུས་ནས་ཐེག་པ་ཆེན་པོ་ལ་འཇུག་པ་ནི་དོན་མཐུན་པའོ། །

[Block 1513]
རྣམ་གྲངས་གཞན་ཡང་བསྟན་པའི་ཕྱིར། གཞན་ཡང་སྦྱིན་པ་ནི་གང་བྱམས་པའི་རྗེས་སུ་འབྲང་བའི་སེམས་ཀྱིས་ཡོངས་སུ་གཏོང་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སེམས་ཅན་བདེ་བ་ལ་དགོད་དོ་སྙམ་པའི་བྱམས་པ་དང་ལྡན་པའི་སེམས་ཀྱིས་བྲེལ་བ་དང་། ཕོངས་པ་ལ༌[^1302]ཕྱི་དང་ནང་གི་དངོས་པོ་གཏོང་བ་ནི་སྦྱིན་པའོ། །

[Block 1514]
སྙན་པར་སྨྲ་བ་ནི་གང་དགའ་བ་དང་མཆོག་ཏུ་དགའ་བར་གྱུར་པའི་སེམས་མི་གཏོང་བའོ་ཞེས་བྱ་བ་ལ། དེ་ལྟར་བྲེལ་བ༌[^1303]དང་ཕོངས་པ་རྣམས་ལ་ཕྱི་དང་ནང་གི་དངོས་པོ་བཏང་ཏེ།[^1304] དེ་དག་ལོངས་སྤྱོད་ཀྱི༌[^1305]འབྱོར་པ་དང་ལྡན་པར་མཐོང་ནས་དགའ་བ་དང་མཆོག་ཏུ་དགའ་བའི་སེམས་རྒྱུན་དུ༌[^1306]འབྱུང་བ་ནི་སྙན་པར་སྨྲ་བའོ། །

[Block 1515]
དེ་ལ་ལོངས་སྤྱོད་དང་ལྡན་པ་མཐོང་ནས་སེམས་མོས་པར༌[^1307]སྐྱེ་བ་ནི་དགའ་བའོ། །

[Block 1516]
བྲེལ་བ་དང་ཕོངས་པའི༌[^1308]གང་ཟག་རྣམས་བྲེལ་བ་དང་ཕོངས་པ་མེད་པར་བྱས་ཏེ།[^1309] ལོངས་སྤྱོད་ལ་བཀོད་པའི་དགའ་བ་བས་བྱང་ཆུབ་སེམས་དཔའ་བདག་གི༌[^1310]ལོངས་སྤྱོད་ཡོངས་སུ་བཏང༌[^1311]ནས་གཞན་ལོངས་སྤྱོད་དང་ལྡན་པར་མཐོང་བའི་དགའ་བ་དེ་བས་ཀྱང་ཤས་ཆེ་བའི་མཆོག་ཏུ་ཆེར་དགའ་བ་ཞེས་བྱའོ། །

[Block 1517]
དོན་སྤྱོད་པ་ནི་གང་སྙིང་རྗེ་ཆེན་པོ་ཡོངས་སུ་དག་པའི་སེམས་བསྐྱེད་པས་ཞེས་བྱ་བ་ལ། གང་ལ་ཡང་བྱམས་པ་དང་ཞེ་སྡང་མེད་པར་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྡུག་བསྔལ་བསལ་ལོ་སྙམ་པའི་སྙིང་རྗེ་ཆེན་པོ་ཡོངས་སུ་དག་པའི་སེམས་བསྐྱེད་པས་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྡུག་བསྔལ་སེལ་ཅིང་དེ་དག་གི་ཚེ་འདི་དང་གཞན་གྱི་ལས་སུ་བྱ་བ་ལ་འབད་ཅིང་བརྩོན་པ་ནི་དོན་སྤྱོད་པའོ། །

[Block 1518]
དོན་མཐུན་པ་ནི་གང་བཏང་སྙོམས་དང་ལྡན་པའི་སེམས་མཐོན་དམན་མེད་ཅིང་ཞེས་བྱ་བ་ལ། སེམས་ཅན་འདི་ལ་ནི་ཕན་བཏགས། འདི་ལ་ནི་ཕན་མི་གདགས་སོ་ཞེས་བྱ་བ་ནི་མཐོན་དམན་གྱི་སེམས་ཏེ། དེ་ལྟ་བུ་མེད་པར་བཏང་སྙོམས་དང་ལྡན་པའི་སེམས་ཀྱིས་སེམས་ཅན་ཐམས་ཅད་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ལ་དགོད་དོ་སྙམ་དུ་སེམས་པ་ནི་དོན་མཐུན་པའོ། །

[Block 1519]
རྣམ་གྲངས་གཞན་ཡང་བསྟན་པར་བཞེད་ནས། གཞན་ཡང་སྦྱིན་པ་ནི་གང་ཆོས་སྦྱིན་པ་བརྩལ་བ༌[^1312]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1520]
བབ་ཅོལ་དང་ཆོས་བཞིན་མ་ཡིན་པ་སྤངས་ཏེ། དགེ་བ་བཅུ་དང་མི་འགལ་བར་བརྩལ་བའི༌[^1313]ལོངས་སྤྱོད་དེ། ལོངས་སྤྱོད་དེ་རྣམས་གཞན་ལ་གཏོང་བ་ནི་སྦྱིན་པའོ། །

[Block 1521]
སྙན་པར་སྨྲ་བ་ནི༌[^1314]གང་དག་ལ་སྦྱིན་པ་སྦྱིན་པ་དེ༌[^1315]དག་ཆོས་ལ་རབ་ཏུ་འཛུད་པའོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་ཅན་གང་ལ་སྦྱིན་པ་སྦྱིན་པའི༌[^1316]སེམས་ཅན་དེ་དང་དེ་དགེ་བ་བཅུ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སོགས་པ་ལ་སྤྱོད་ཅིག་ཅེས་སྨྲས་ནས་ཆོས་དེ་དག་བྱེད་དུ་བཙུད་པ་ནི་སྙན་པར་སྨྲ་བའོ། །

[Block 1522]
དོན་སྤྱོད་པ་ནི་གང་བདག་གི༌[^1317]དོན་དང་གཞན་གྱི་དོན་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའོ་ཞེས་བྱ་བ་ནི་བདག་དང་གཞན་གྱི་དོན༌[^1318]མཐར་ཕྱིན་པའི་དོན་ལ་དགོད་པ༌[^1319]ནི་དོན་སྤྱོད་པའོ། །

[Block 1523]
དེ་ལ་བདག་དང་གཞན་གྱི་དོན་ཀྱང་སྤངས་པ་དང་ཡེ་ཤེས་ཀྱིས་བསྡུས་པར་རིག་པར་བྱའོ།[^1320] །དེ་ལ་སྤངས་པ་ནི་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་པའོ། །

[Block 1524]
ཡེ་ཤེས་ནི་ཤེས་བྱ་ཐམས་ཅད་ལ་གཉིས་སུ་མེད་པར་ཁོང་དུ་ཆུད་པའི་མཚན་ཉིད་དོ། །

[Block 1525]
དོན་མཐུན་པ་ནི་གང་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་གྱི་ཕྱིར་ཞེས་བྱ་བ་ལ་སེམས་ཅན་ཐམས་ཅད་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་གཞག་པའི་ཕྱིར་བདག་ཉིད་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་ནི་དོན་མཐུན་པའོ། །

[Block 1526]
རྣམ་གྲངས་གཞན་ཡང་བསྟན་པར་བཞེད་ནས། གཞན་ཡང་སྦྱིན་པ་ནི་གང་ནང་དང་ཕྱིའི་དངོས་པོ་རྣམས་ཡོངས་སུ་གཏོང་བ་ཞེས་བྱ་བ་གསུངས་ཏེ། ནང་དང་ཕྱིའི་དངོས་པོ་གཏོང་བ་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྐབས་སུ་ནང་གི་དངོས་པོ་བརྒྱད་དང་། ཕྱིའི་དངོས་པོ་ཉི་ཤུ་རྩ་ལྔ་གཏོང་བར་བཤད་པའོ། །

[Block 1527]
སྙན་པར་སྨྲ་བ་ནི་གང་ཆོས་ཐམས་ཅད་ཀྱི་ཡོན་ཏན་ཤེས་པ་ཞེས་བྱ་བ་ལ། བཤད་པར་བྱ་བ་དང་། བསྒྲུབ་པར་བྱ་བ་དང་། ཐོབ་པར་བྱ་བའི་ཆོས་རྣམས་ཀྱི་ཡོན་ཏན་ཤེས་པའི་གང་ཟག་ལ་སློབ་དཔོན་གྱི༌[^1321]དཔེ་མཁྱུད་མེད་པ༌[^1322]ཆོས་ཐམས་ཅད་འཆད་པ་ནི་སྙན་པར་སྨྲ་བའོ། །

[Block 1528]
དོན་སྤྱོད་པ་ནི་གང་བདག་གི་དོན་བཏང་སྟེ་ཞེས་བྱ་བ་ལ། བདག་གི་དོན་བཞག༌[^1323]ནས་གཞན་གྱི་དོན་བྱེད་པ་ནི་དོན་སྤྱོད་པ་སྟེ། གཞན་གྱི་དོན་ཀྱང་སྤངས་པ་དང་། ཡེ་ཤེས་ཀྱིས་བསྡུས་པ་གོང་དུ་བཤད་པ་བཞིན་སྦྱར་རོ། །

[Block 1529]
བསྡུས་ཏེ་ཞེས་བྱ་བ་ནི་བསྒྲུབས་ཏེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1530]
ལག་ཏུ་ཐོབ་པ་ཞེས་བྱ་བ་ནི་བདག་གི་དབང་དུ་གྱུར་པ་ཡང་བྱ་བའི་དོན་ཏོ། །

[Block 1531]
སྦྱིན་པ་རྣམ་པ་གསུམ་ལས་བསྡུས་པའི༌[^1324]དངོས་པོ་བཞི་ཆོས་སྦྱིན་པ་འབའ་ཞིག་དང་སྦྱར་ཏེ་བསྟན་པའི་ཕྱིར། དེ་ལ་ཆོས་སྦྱིན་པ་གང་ཞེ་ན། གང་ཇི་སྐད་ཐོས་པའི་ཆོས་རྣམས་སྟོན་པའོ་ཞེས་བྱ་བ་གསུངས་ཏེ། གང་བདག་གི་མཁན་པོ་དང་སློབ་དཔོན་ལས་ཇི་ལྟར་ཐོས་པའི་ཆོས་རྣམས་སྟོན་པ་ནི་ཆོས་སྦྱིན་པའོ། །

[Block 1532]
སྙན་པར་སྨྲ་བ་ནི་ཟང་ཟིང་མེད་པའི་སེམས་ཀྱིས་ཞེས་བྱ་བ་ལ། ཆོས་བསྟན་པ་འདིས་ཟང་ཟིང་འདི་སྒྲུབ་པོ་ཞེས་ཁེ་དང་བཀུར་སྟི་ལ་མ་ཆགས་པའི་སེམས་ཀྱིས༌[^1325]ཆོས་ཕྱིན་ཅི་མ་ལོག་པར་སྨྲ་བ་ནི་སྙན་པར་སྨྲ་བའོ། །

[Block 1533]
དེ་སྤྱད་པ་ནི་གང་གཞན་ལ་ལུང་འབོགས་པ༌[^1326]ཞེས་བྱ་བ་ལ་གང་སེམས་ཅན་གཞན་ལ་ལུང་འབོགས་པ༌[^1327]དང་། ཁ་ཏོན་བྱེད་དུ་འཇུག་པའི་དོན༌[^1328]ལ་མི་སྐྱོ་བ་ནི་དོན་སྤྱོད་པའོ། །

[Block 1534]
དེ་ལ་ལུང་འབོགས་པ་ནི་བསམ་གཏན་གྱི་མན་ངག་སྟོན་པའོ། །

[Block 1535]
ཁ་ཏོན་བྱེད་པ་ནི་གཞུང་གི་ཆོས་ཁ་ཏོན་བྱེད་དུ་གཞུག་པའོ། །

[Block 1536]
དོན་མཐུན་པ་ནི་གང་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་སེམས་དང་མ་བྲལ་བས་ཞེས་བྱ་བ་ལ། བདག་ཉིད་བྱང་ཆུབ་ཀྱི་སེམས་དང་མ་བྲལ་བས་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པའི་ཆོས་རྙེད་པ་དང་། གཞན་ཡང་བྱང་ཆུབ་ཀྱི་སེམས་ལ་བཙུད་ནས་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པའི་ཆོས་རྙེད་པར་བྱས་པས་ནི་དོན་མཐུན་པའོ། །

[Block 1537]
ཆོས་སྦྱིན་པ་དང་བསྡུ་བའི་དངོས་པོ་བཞིར་སྦྱར་བ་རྣམ་གྲངས་གཞན་ཡང་བསྟན་པའི་ཕྱིར། གཞན་ཡང་ཆོས་ཀྱི་སྦྱིན་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཆོས་ཉན་པར་འོངས་ཞེས་བྱ་བ་ནི་ཆོས་ཉན་པའི་སེམས་ཅན་རྣམས་ཐག༌[^1329]ཉེ་བ་ནས་འོངས་པའོ། །

[Block 1538]
ལྷག་པ༌[^1330]ནི་ཆོས་ཉན་པའི་ཕྱིར་ཐག་རིང་པོ་ནས་ལྷགས་པའོ། །

[Block 1539]
མི་སྐྱོ་བ་ནི་གང་ཟག་དེ་དག་ལ་ཁ་ཅིག་འཆད༌[^1331]པ་མ་ཡིན་གྱི་མ་ལུས་པར་འཆད་པའོ། །

[Block 1540]
མི་གཡེང་བ༌[^1332]ནི་འཕྲལ་གྱི་བྱ་བ་གཞན་རྣམས་བཏང་ནས་ཆོས་འཆད་པ་འབའ་ཞིག་ལྷུར་བྱེད་པའོ། །

[Block 1541]
སྙན་པར་སྨྲ་བ་ནི་ངག་ཇི་སྲིད་དུ་རྒྱང་རིང་པོར་སོང་སྟེ་ཞེས་བྱ་བ་ལ། བདག་ཉིད་དཔག་ཚད་གཅིག་གམ་དཔག་ཚད་གཉིས་སམ། ཡུལ་གཅིག་གམ་ཡུལ་གཉིས་སམ། འཛམ་བུའི་གླིང་གཅིག་གམ་འཛམ་བུའི་གླིང་གཉིས་སམ་ཞེས་བྱ་བ་ནས། སྟོང་གསུམ་གྱི་སྟོང་ཆེན་པོའི་འཇིག་རྟེན་གྱི་ཁམས་གྲངས་མེད་པའི་ཕ་རོལ་དུ་ཡང་སོང་སྟེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1542]
ལྷག་པའི་བསམ་པར་སོང་བའི་སེམས་ཀྱི་རྒྱུད་ཀྱིས་ཞེས་བྱ་བ་ནི་ཡོ་བྱད་ཀྱི༌[^1333]གཡེན་སྤྱོ་བ་རྣམས་ཀྱིས༌[^1334]གཡེན་སྤྱོ་བ་མེད་པར་བྱས་ནས་ཆོས་ལ་དགོད་དོ་སྙམ་པའི་བསམ་པས་ཤེས་པར་བྱ་བའི་དོན་ཏོ། །

[Block 1543]
འཛུད་ཅིང་ཡོངས་སུ་བསྔོ༌[^1335]པའོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་རྒྱུ་སྒྲུབ་ཏུ༌[^1336]འཛུད་ཅིང་བྱང་ཆུབ་ཉིད་ལ་འཇོག་པར་བྱེད་པའོ། །

[Block 1544]
ཆོས་སྦྱིན་པ་དང་བསྡུ༌[^1337]བའི་དངོས་པོ༌[^1338]སྦྱར་བ་རྣམ་གྲངས་གཞན་ཡང་བསྟན་པའི་ཕྱིར། གཞན་ཡང་ཆོས་ཀྱི༌[^1339]སྦྱིན་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1545]
སྦྱིན་པ་ཐམས་ཅད་ཀྱི་མཆོག་ཆོས་སྦྱིན་པ་ཡིན་པར་རིག་ནས་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་རྣམ་པ་གསུམ་སྟེ། ཟང་ཟིང་སྦྱིན་པ་དང་། མི་འཇིགས་པ་སྦྱིན་པ་དང་། ཆོས་སྦྱིན་པའོ། །
--- END BLOCKS ---
