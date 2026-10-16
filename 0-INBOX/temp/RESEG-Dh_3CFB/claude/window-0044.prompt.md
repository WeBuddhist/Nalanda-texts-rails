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
[Block 1541]
ཟག་པ་ཟད་པ་དེ་ཡང་ཤེས་པར་དཀའ༌[^1147]བ་ཡིན་ནོ། །

[Block 1542]
ཉེས་པ་འདི་ནི་འགྲིབ་པ་དང་ཕུལ་དུ་བྱུང་བའི་ཆོས་ཅན་གྱི༌[^1148]ཡིན་ཏེ། མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་ཟིལ་གྱིས་གནོན་པ་ཁྱད་པར་དུ་བྱེད་པ་དང་མི་བྱེད་པ༌[^1149]མེ་ལ་སོགས་པ་དང་འདྲ་བར་སྒྲུབ་པར་བྱེད་དོ། །

[Block 1543]
དེ་དག་ནི་རྣམ་པར་རྟོག་པ་ལས་འབྱུང་བ་ཅན་དག་ཡིན་ཏེ། ཉེ་བར་ལེན་པ་དག་ཡིན༌[^1150]ན་ཡང་ཡིད་ཀྱི་ཡོན་ཏན་འགའ་ཞིག་གོམས་པ༌[^1151]ལས་ཁྱད་པར་དུ་འགྱུར་བ་མེད་པ་དང་། དེ་གསལ་བ་ན་མེ་ལ་སོགས་པ་དང་འདྲ་བར༌[^1152]རྗེས་སུ་འགྲོ་བ་མེད་པ་ཅན་གྱི་འཇིག་པའི་ཆོས་ཅན་དུ་འགྱུར་རོ། །

[Block 1544]
དེ་བས་ན་མཉེས་པར་མེད་པར་ཡང་འགྱུར་རོ། །

[Block 1545]
ཉེས་པ་མེད་པ་ཞེས་བྱ་བ་ཡང་ཇི་ལྟ་བུ་ཡིན། འདི་ལྟར་ཉེས་པའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་བདག་ཉིད་དུ་འགྱུར་བ་ཉིད་ཡོད་ན་ཡང་རྐྱེན་ཇི་ལྟ་བ་བཞིན་དུ་ཉེས་པ་ཡང་འབྱུང་བ་ཡིན་ཏེ། ཉེས་པའི་བདག་ཉིད་དུ་གྱུར་པའི་མི་མཐུན་པའི་ཕྱོགས་སྐྱེ་བ་དང་འདྲའོ་ཞེ་ན།། །།

[Block 1546]
བམ་པོ་བདུན་པ། ཉེས་པ་འདི་ནི་མེད་དེ་འདི་ལྟར།

[Block 1547 [VERSE]]
འཚེ་བ་མེད་དང་ཡང་དག་དོན། །
ངོ་བོ་ཉིད་ལ་ཕྱིན༌[^1153]ལོག་གིས། །
འབད་དུ་ཟིན་ཀྱང་མི་བཟློག་སྟེ།

[Block 1548]
[^1154] །བློ་ནི་དེ་ཕྱོགས་འཛིན་ཕྱིར་རོ། །

[Block 1549]
རང་བཞིན་དུ༌[^1155]འབད་རྩོལ་མེད་པར་བཟློག་པར་ནུས་པ་མ་ཡིན་ཏེ། གཙང་སྦྲ་ཅན་ལ༌[^1156]ཐོད་པ་ཅན་ལ་འདོད་པ་དང་འདྲའོ། །

[Block 1550]
འབད་རྩོལ་ཡང་ཐོབ་པ་དང་ལྡོག་པའི་རང་བཞིན་དག་ནི་ཡོན་ཏན༌[^1157]སྐྱོན་མཐོང་བས་བྱས་པ་ཡིན་ན། དེ་ཡང་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་བདག་ཉིད་ཅན་དུ་འགྱུར་བའི་སྐྱེས་བུའི་སྐྱོན་དག་ལ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ནི་ཉེ་བར་འཚེ་བ་མེད་པ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1551]
ཉེས་པ་མ་ལུས་པ་སྤངས་པའི་ཕྱིར་དང་། ཀུན་ནས་དཀྲིས་པ་དང་སྐྱེ་བ་ལ་རག་ལུས་པའི་སྡུག་བསྔལ་དང་བྲལ་བའི་ཕྱིར་དང་། རབ་ཏུ་ཞི་བའི་བདེ་བའི་ཕྱིར༌[^1158]དང་། [^1159]སྐྱོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1552]
ཡང་དག་པའི་དོན་ཅན་མ་ཡིན་པ་ཉེ་བར་ལེན་པའི་སྟོབས་ལས༌[^1160]བྱུང་བ་ཅན༌[^1161]ཡང་རྒྱུད་ལས༌[^1162]རྣམ་པར་བཟློག་པ་བཟུང་བའི་ཕྱིར་མི་འགྱུར་རོ། །

[Block 1553]
ཡང་དག་པའི་དོན་ཅན་ནི་མ་ཡིན་ཏེ། དངོས་པོའི་སྟོབས་ཀྱིས་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1554]
ཉེས་པའི་ཡང་དག་པའི་དོན་མ་ཡིན་པ་ཅན་གཉེན་པོའི་ཕྱོགས་ཀྱི་བདག་ཉིད་ཅན་དུ་གྱུར་པ་ལ་གནོད་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1555]
དེ་བས་ན་ཉེས་པ་སྐྱེ་བ་མ་ཡིན་ཏེ། འབད་རྩོལ་ཡོད་ན་ཡང་རྟོག་པ་དང་ལྡན་པའི་བློ་དང་ཁྱད་པར་དུ་སྐྱོན་མེད་པའི་བདག་ཉིད་ཅན་ནི་ཡོན་ཏན་གྱི་ཕྱོགས་སུ་གྱུར་པས་གཉེན་པོའི་ཕྱོགས་ཉིད་ལ་རྩོལ་བ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1556]
ཉེས་པ་དེ་དག་སྐྱེད་པར་བྱེད་པ༌[^1163]གང་གི་གཉེན་པོའི་ཕྱོགས་གོམས་པ་ལས་སྤོང་བར་འགྱུར་བ་ཡང་གང་ཞེ་ན།

[Block 1557 [VERSE]]
ཉེས་པར༌[^1164]རྣམ་པ་ཐམས་ཅད་དག །
འཇིག༌[^1165]ཚོགས་ལྟ་ལས་སྐྱེ་བ་ཡིན། །
དེ་མི་རིགས༌[^1166]དེ་དེར་ཆགས་པ། །
དེ་ལས་ཞེ་སྡང་ལ་སོགས་འབྱུང་། །

[Block 1558]
ང་མ་ཡིན་ངའི་མ་ཡིན་ཞེས་ལྟ་བའི་ཡོངས་སུ་འཛིན་པ་མེད་པར་འགའ་ཞིག་ལ་ཡང་ཆགས་པ་མེད་ཅིང་། རྗེས་སུ་ཆགས་པ་མེད་པར་འགའ་ཞིག་ལ་ཞེ་སྡང་མེད་དེ། བདག་མེད་པ་བདག་གི་ལ་ཉེ་བར་གནོད་པ་མེད་པ་ཅན་དང་། ཉེ་བར་གནོད་པ་འཇོམས་པར་བྱེད་པ་ལ་དེ་མེད་པའི་ཕྱིར་རོ། །

[Block 1559]
དེ་བས་ན་རིགས་མཚུངས་པ་གོམས་པ་ལས་སྐྱེ་བའི་བདག་ཏུ་ལྟ་བས༌[^1167]བདག་གིར་འཛིན་པ་སྐྱེ་བར༌[^1168]བྱེད་དོ། །

[Block 1560]
དེ་དག་གིས་ཀྱང་དེ་ལ་ཆགས་པ༌[^1169]དང་ཞེ་སྡང་ལ་སོགས་པ་སྐྱེད་པར་བྱེད་པའི་ཕྱིར། ཉེས་པ་ཐམས་ཅད་ནི་འཇིག་ཚོགས་སུ་ལྟ་བ་ལས་སྐྱེ་བ་ཡིན་ནོ། །

[Block 1561]
དེ་ཉིད་ཀྱང་མི་ཤེས་པས་མ་རིག་པ་ཞེས་བྱ་སྟེ།

[Block 1562 [VERSE]]
དེ་ཉིད་ཕྱིར་ན་ཉེས་རྣམས་ཀྱི། །
རྒྱུ་ནི་གཏི་མུག་ཡིན་པར་གསུངས། །
གཞན་ཡང་འཇིག་ཚོགས་ལྟ་བ་སྟེ།

[Block 1563]
[^1170] །དེ་སྤངས་པ་ན་སྤངས་ཕྱིར་རོ། །

[Block 1564]
གཏི་མུག་ནི་ཉེས་པའི་རྒྱུ་ཡིན་པར་གསུངས་ཏེ། རྨོངས་པ་མེད་པ་ལ་ཉེས་པ་དག་མི་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1565]
གཞན་དག་ཏུ་ནི་འཇིག་ཚོགས་སུ་ལྟ་བ་ཡང་ཡིན་ནོ། །

[Block 1566]
དེ་དང་དེ་ནི་གཙོ་བོ་བསྟན་པ་ཡིན་ན་འགྱུར་ཏེ། དུ་མ་ལས་སྐྱེ་བ་ཅན་གྱི་ཉེས་པ་དག་ནི་གཅིག་ལས་སྐྱེ་བ་འགལ་བའི་ཕྱིར་རོ། །

[Block 1567]
གཉི་ག་གཙོ་བོ་ཡིན་ན་ནི་རེ་རེ་བསྟན་པས་མཛེས་པ་ལ་བརྟེན་པ༌[^1171]མ་ཡིན་ནོ། །

[Block 1568]
རྣམ་པ་གཉི་ག་ཡང་གཅིག་ཏུ་བསྟན་པ་ན་འགལ་བ་མེད་དོ། །

[Block 1569]
གཙོ་བོ་ཡང་དེ༌[^1172]དག་གི་ཉེ་བར་ལེན་པ་ཉིད་ཀྱིས་ཡིན་ཏེ། དེ་སྤངས་པ་ན་ཉེས་པ་དག་སྤངས་པའི་ཕྱིར་རོ། །

[Block 1570]
དེ་བས་ན་འཇིག་ཚོགས་སུ་ལྟ་བ་ལས་སྐྱེ་བ་ཅན་གྱི་ཉེས་པ་རྣམས་ནི་དེའི་གཉེན་པོའི་ཕྱོགས་བདག་མེད་པ་མཐོང་བ་གོམས་པ་ལས་སྤངས་པ་ཡོད་པར་འགྱུར་རོ། །

[Block 1571]
ཉེས་པ་ཟད་པ་ཅན་རྟོགས་དཀའ་བ་དེ་ཡང་གང་གིས་བསྟན་པ་ལས་འདིས་རྟོགས་པར་འགྱུར་རོ། །

[Block 1572 [HEADING]]
## སྐྱེས་བུས་མ་བྱས་པའི་ཚིག། ^7-0

[Block 1573 [HEADING]]
### སྐྱེས་བུས་མ་བྱས་བདེན་དོན་ཅན། ^7-1-0

[Block 1574]
སྐྱེས་བུ་ལ་བརྟེན་པ་ཅན་གྱི་ཚིག་ནི་ལུང་མ་ཡིན་ཏེ། བྱེད་པ་པོ་རྟོགས་དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1575 [VERSE]]
ཚིག་རྣམས་ལོག་པ་ཉིད་ཀྱི་རྒྱུ། །
ཉེས་རྣམས་སྐྱེས་བུ་ལ་བརྟེན་ཕྱིར། །
སྐྱེས་བུས་མ་བྱས་བདེན་དོན་ཅན། །
ཞེས་ནི་ལ་ལ་རྗོད་པར་བྱེད། །

[Block 1576]
ལུང་ཐམས་ཅད་ནི་འཁྲུལ་པར་སྲིད་པ་མ་ཡིན་ཏེ། འཁྲུལ་པའི་རྒྱུ་ཉེས་པ་རྣམས་ནི་སྐྱེས་བུ་ལ་བརྟེན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1577]
སྐྱེས་བུས་མ་བྱས་བདེན་དོན་ཅན། །ཞེས་བྱ་བ་ནི་གཞན་དག་གི་ཡིན་ཏེ། རྒྱུ་མེད་པས་ནི་འབྲས་བུ་མེད་པ་གྲུབ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1578]
དེ་སྐད་དུ་སྨྲ་བ་དེ་ཉིད་ལ།

[Block 1579 [VERSE]]
ཚིག་རྣམས་བདེན་པ་ཉིད་ཀྱི་རྒྱུ། །
ཡོན་ཏན་སྐྱེས་བུ་ལ་བརྟེན་ཕྱིར། །
སྐྱེས་བུས༌[^1173]མ་བྱས་ལོག་པའི་དོན། །
ཅི་མིན་ཞེས་ནི་གཞན་དག་བརྗོད། །

[Block 1580]
ཇི་ལྟར་འདོད་ཆགས་ལ་སོགས་པ་དང་ལྡན་པའི་སྐྱེས་བུ་བརྫུན་དུ་སྨྲ་བ་མཐོང་བ་དེ་ལྟར། བརྩེ་བའི་ཆོས་ཉིད་ལ་སོགས་པ་དང་ལྡན་པ་བདེན་པར་སྨྲ་བ་ཡིན་ནོ། །
--- END BLOCKS ---
