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
[Block 1471]
གལ་ཏེ་བྱས་པ་ནི་མི་འགེགས་ཀྱི་དེ་དང་ལྷན་ཅིག་ཏུ་རྒྱུ་བའི་རྟག་པ་འགེགས་པའི་དོན་དུ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟར་ཡང་མ་ཡིན་ཏེ། གང་གི་ཕྱིར། གཉེན་པོའི་ཕྱོགས་དང་ལྡན་མ་ཡིན། །གཏན་ཚིགས་ཉིད་དུ་མ་བརྗོད་པའི་བྱས་པའི་སྤྱི་བརྗོད་པ་ཡིན་ཏེ། དང་གི་སྒྲ་སྨོས་པས་བྱས་པ་ཉིད་ཡོད་པས་ན་གཉེན་པོའི་ཕྱོགས་ཀྱི་གོ་སྐབས་ཡོད་པ་མ་ཡིན་ན་གང་དེ་དགག་པར༌[^1134]བྱ་བའི་དོན་དུ་ཆོས་མི་མཐུན་པ་ཉེ་བར་སྦྱོར་བར་བྱེད་དེ་མ་བྱས་པ་དང་ལྷན་ཅིག་ཏུ་རྟག་པ་ཉིད་དགག་པར་བྱ་བའི་དོན་དུ་ཡང་ཉེ་བར་སྦྱོར་བར་མི་བརྗོད་དོ། །

[Block 1472]
དེ་ལྟ་བས་ན་གཉེན་པོའི་ཕྱོགས་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 1473]
ཆོས་མཐུན་པའི་སྒོ་ནས་བྱས་པ་ཉིད་ཀྱིས༌[^1135]མི་རྟག་པ་ཉིད་རྟོགས་པ་ནི༌[^1136]མེད་དོ། །

[Block 1474]
དེའི་གཉེན་པོའི་ཕྱོགས་རྟག་པ་ཉིད་དང་ལྡན་པར་ཡོད་པ་གང་གིས་འགེགས་པར་བྱེད། ཅི་སྟེ་ཡང་མ་གྲུབ་པའི་ཕྱིར་རྟག་པ་ཉིད་ལ་ཆོས་མི་མཐུན་པ་ཙམ་གྱིས་རྟག་པ་ཉིད་འགེགས་སོ་ཞེ་ན། དེ་ལྟ༌[^1137]ན་ཡང་། ཁྱད་པར་སྒོ་ནས་ཀྱང་དེར་འགྱུར། །གལ་ཏེ་ཆོས་མཐུན་པ༌[^1138]མ་བརྗོད་པར་ཁྱད་པར་གྱི་སྒོ་ནས་ཀྱང་སྟེ་དེ་ཆོས་དེའི་གཉེན་པོའི་ཕྱོགས་དང་ལྷན་ཅིག་ཏུ་རྒྱུ་བ་འགེགས་པ་ཡིན་པར་འགྱུར་ཏེ། དཔེར་ན་མཉན་བྱ་ཡིན་པའི་ཕྱིར་སྒྲ་མི་རྟག་གོ་ཞེས་པ་ལྟ་བུའོ། །

[Block 1475]
བུམ་པ་ལ་སོགས་པ་མི་རྟག་པ་ལ་མཉན་པར་བྱ༌[^1139]བ་མ་ཡིན་པ་དང་ལྷན་ཅིག་ཏུ་རྒྱུ་བ་མི་རྟག་པ་ཉིད་བཀག་པའི་ཕྱིར། མི་འདོད་པའི་རྟག་པ་ཉིད་གྲུབ་པར་འགྱུར་རོ། །

[Block 1476]
མི་རྟག་པ་ཉིད་གྲུབ་པར་མཚུངས་པའི་ཕྱིར་འདིར་ཡང་རྟག་པ་ཉིད་དུ་འགྱུར་ཏེ། རྩོལ་བ་ལས་བྱུང་བའི་ཕྱིར་གློག་ལ་སོགས་པ་བཞིན་ནོ་ཞེས་ཆོས༌[^1140]མཐུན་པས་ནི་འདི་ལ་འགའ་ཞིག་ཀྱང་རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་ནམ་མཁའ་བཞིན་མ་བྱས་པ་མ་ཡིན་པ་དེའི་ཕྱིར་དེ་ཉིད་རྟག་པ་མ་ཡིན་པས་ནའོ། །

[Block 1477]
མ་བྱས་པ་ཉིད་ནི་རྟག་པ་ཉིད་ཀྱི་གཏན་ཚིགས་མ་ཡིན་ཏེ། གང་དེ་མེད་པ་ལས་རྟག་པར་མི་འགྱུར་རོ། །

[Block 1478]
མི་རྟག་པ་ཉིད་ཀྱི་གཏན་ཚིགས་ལུས་ཅན་མ་ཡིན་པ་ལ་སོགས་པ་ཡང་མེད་པའི་ཕྱིར་མི་རྟག་པ་ཉིད་འགེགས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1479]
ནམ་མཁའ་ནི་ངག་གི་དོན་ལ་ལྟོས་ནས་ཉེ་བར་སྦྱར་བར་རིགས་ཏེ་གང་གི་ཕྱིར་མ་བྱས་པ་ལས་ཕྱི་རོལ་དུ་གྱུར་པའི་རྟག་པ་ནི་ཅུང་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། ནམ་མཁའ་བཞིན་ནོ། །

[Block 1480]
མི་རྟག་པ་ལ་ཡང་བུམ་པ་བཞིན་ནོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 1481]
དེའི་ཕྱིར་མི་རྟག་པའོ་ཞེས་བྱ་བ་ཉིད་ཀྱིས་ཉེ་བར་སྦྱར་བར་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1482 [HEADING]]
#### མཇུག་བསྡུ་བ། ^4-5-3-0

[Block 1483]
མཇུག་བསྡུ་བ་ལ་ནི་སླར་གྱི་ཚིག་མི་བརྗོད་པ་ཉིད་དེ་དེ་ལ་ཡན་ལག་མ་ཡིན་ནོ་ཞེས་འཆད་པར་མི་བྱའོ། །

[Block 1484 [HEADING]]
### གཉིས་ཀ་རབ་ཏུ་གྲུབ་པ་དཔེ། ^4-6-0

[Block 1485]
བྱེ་བྲག་པ་རྣམས་ནི་གཉིས་ཀ་རབ་ཏུ་གྲུབ་པ་དཔེའོ་ཞེས་ཟེར་རོ། །

[Block 1486]
དེ་ལ་ཡང་།

[Block 1487]
མཁའ་དཔེར་བརྗོད་པའི་སྦྱོར་བའམ། །ངག་གི་ཕྱོགས་གཅིག་ཉིད་ཀྱང་མིན། །

[Block 1488]
གཉིས་རབ༌[^1141]གྲུབ་པ་ཞེས་བྱ་བ༌[^1142]ལ་གལ་ཏེ་དམ་བཅའ་དང་གཏན་ཚིགས་དག༌[^1143]ནམ་མཁའ་ལ་གྲུབ་པ་དེའི་ཡོན་ཏན་ཡིན་པའི་ཕྱིར་ཞེ་ན་ནི་ཐམས་ཅད༌[^1144]ནམ་མཁའ་དཔེར་འགྱུར་རོ། །

[Block 1489]
ཅི་སྟེ་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དེ་གང་ལ༌[^1145]གྲུབ་པ་དེ་ཉིད་དོ་ཞེ་ན་ནི། དེ་ལྟ་ན་ཡང་དག་གི་ཆ་ཤས་ཉིད་མི་འཐད་དེ།

[Block 1490 [VERSE]]
[^1146]རྗེས་འགྲོ་རྗོད་པར༌[^1147]མི་བྱེད་པ། །
དེ་ནི་དཔེ་ཡི་གཟུགས་བརྙན་ཡིན། །

[Block 1491]
གང་དུ་གཏན་ཚིགས་དང་བསྒྲུབ་བྱའི་རྗེས་སུ་འགྲོ་བ་མི་སྟོན་པ་དེ་ནི་དཔེ་ལྟར་སྣང་བའོ། །

[Block 1492]
གཉིས་ཀའི་དཔེ་ནི་སྔ་མ་བཞིན་ནོ་ཞེས་སྦྱར་བར་བྱའོ། །

[Block 1493]
སྒྲུབ་བྱེད་ཉེ་བར་སྦྱར་དོན་ནི། །རང་རྒྱུད་ཡིན༌[^1148]ཡང་དོན་མེད་འགྱུར། །

[Block 1494]
གལ་ཏེ་དཔེ་རང་གི་རྒྱུད་ཀྱི༌[^1149]ཡིན་ན་ནི་གཏན་ཚིགས་ཀྱི་དོན་གྱི་ཕྱོགས་གཅིག་མ་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 1495]
དེ་ལྟ་བས་ན་སྒྲུབ་པར་བྱེད་པ་ཉིད་མི་སྲིད་པ་ཉེ་བར་སྦྱར་བའི་དོན་ཡང་མ་ཡིན་ཏེ། སྔར་ཇི་སྐད་བཤད་པ་བཞིན་ནོ། །

[Block 1496]
ཚད་མ་ཀུན་ལས་བཏུས་པ་ལས་དཔེ་དང་དཔེ་ལྟར་སྣང་བ་བརྟགས༌[^1150]པའི་ལེའུ་སྟེ་བཞི་པའོ།། །།

[Block 1497 [HEADING]]
## གཞན་སེལ་བ་བརྟག་པའི་ལེའུ། ^5-0

[Block 1498 [HEADING]]
### སྒྲ་ལས་བྱུང་བ་རྗེས་དཔག་ལས་ཚད་མ་གཞན་མིན་པ། ^5-1-0

[Block 1499]
ཚད་མ་གཉིས་སུ་བརྗོད་པ་ལ་ཁ་ཅིག་སྒྲ་ལས་བྱུང་བ་ཡང་ཚད་མ༌[^1151]ཉིད་དུ་འདོད་དོ། །

[Block 1500]
དེ་ལ།

[Block 1501 [VERSE]]
སྒྲ་ལས་བྱུང་བ་རྗེས་དཔག་ལས།[^1152] །
ཚད་མ་གཞན་མིན་འདི་ལྟར་ཏེ། །
རང་གི་དོན་ལ་བྱ༌[^1153]སོགས་བཞིན། །
གཞན་སེལ་སྒོ་ནས་སྟོན་པར་བྱེད། །

[Block 1502]
སྒྲ་ནི་ཡུལ་གང་ལ་མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་ཉིད་རབ་ཏུ་སྦྱོར་བར་བྱེད་པ་དེའི་ཆ་ནས་དེའི་བྱས་པ་ལ་སོགས་པ་བཞིན་དུ་དོན་གཞན་རྣམ་པར་བཅད་ནས་སྟོན་པར་བྱེད་དོ། །

[Block 1503]
དེའི་ཕྱིར་རྗེས་སུ་དཔག་པ་ལས་ཐ་དད་པ་མ་ཡིན་ནོ། །

[Block 1504 [HEADING]]
### ཐ་དད་རྣམས་ཀྱི་རིགས་སྒྲ་མེད་པ། ^5-2-0

[Block 1505]
གང་ལ་ལ་དག་ནི་ཐམས་ཅད་དུ་རིགས་ཀྱི་སྒྲ་རང་རང་གི་ཐ་དད་པ་ལས་ཡིན་ཏེ། སྨྲས་པ་རྣམས་ལ་ནི་ངེས་པའི་དོན་དུ་ཁྱད་པར་གྱི་སྒྲ་ཡིན་ནོ་ཞེས་འཛེར་ཏོ། །

[Block 1506]
དེ་ལ་ལན་བརྗོད་པ།

[Block 1507]
ཐ་དད་རྣམས་ཀྱི་རིགས་སྒྲ་མེད། །རྗོད་པར་བྱེད་པ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1508]
རེ་ཞིག་རིགས་ཀྱི་སྒྲ་ཡོད་པ་ལ་སོགས་པ་རྫས་ལ་སོགས་པ་རྣམས་ཀྱི་རྗོད་པར་བྱེད་པ༌[^1154]མ་ཡིན་ཏེ། མཐའ་ཡོད་མིན་ཕྱིར། མཐའ་མེད་ཅེས་བྱ་བ་ནི། ཐ་དད་པ་རྣམས་སྒྲ་དང་འབྲེལ་པར་བྱེད་མི་ནུས་ལ། འབྲེལ་པར་མ་བྱས་པའི་སྒྲས་དོན་བརྗོད་པ་ཡང་རིགས་པ་མ་ཡིན་པས་རང་གི་ངོ་བོ་ཙམ་ཞིག་རྟོགས་པར་བྱེད་པར་ཟད་དོ། །

[Block 1509]
གཞན་ཡང་། འཁྲུལ་པའི་ཕྱིར། ཇི་ལྟར་རྫས་ལ་ཡོད་པའི་སྒྲ་འཇུག་པ་དེ་བཞིན་དུ་ཡོན་ཏན་ལ་སོགས་པ་ལ༌[^1155]ཡང་འཇུག་པས་འཁྲུལ་པའི་ཕྱིར་ཐེ་ཚོམ་དུ་འགྱུར་གྱི། རྗོད་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1510 [HEADING]]
### རིགས་ཀྱི་སྒྲ་ཙམ་མམ་དེ་དང་ལྡན་པ་ཙམ། ^5-3-0
--- END BLOCKS ---
