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
དེ་ལ་ལན་བརྗོད་པ།

[Block 1507]
ཐ་དད་རྣམས་ཀྱི་རིགས་སྒྲ་མེད། །རྗོད་པར་བྱེད་པ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1508]
རེ་ཞིག་རིགས་ཀྱི་སྒྲ་ཡོད་པ་ལ་སོགས་པ་རྫས་ལ་སོགས་པ་རྣམས་ཀྱི་རྗོད་པར་བྱེད་པ༌[^1154]མ་ཡིན་ཏེ། མཐའ་ཡོད་མིན་ཕྱིར། མཐའ་མེད་ཅེས་བྱ་བ་ནི། ཐ་དད་པ་རྣམས་སྒྲ་དང་འབྲེལ་པར་བྱེད་མི་ནུས་ལ། འབྲེལ་པར་མ་བྱས་པའི་སྒྲས་དོན་བརྗོད་པ་ཡང་རིགས་པ་མ་ཡིན་པས་རང་གི་ངོ་བོ་ཙམ་ཞིག་རྟོགས་པར་བྱེད་པར་ཟད་དོ། །

[Block 1509]
གཞན་ཡང་། འཁྲུལ་པའི་ཕྱིར། ཇི་ལྟར་རྫས་ལ་ཡོད་པའི་སྒྲ་འཇུག་པ་དེ་བཞིན་དུ་ཡོན་ཏན་ལ་སོགས་པ་ལ༌[^1155]ཡང་འཇུག་པས་འཁྲུལ་པའི་ཕྱིར་ཐེ་ཚོམ་དུ་འགྱུར་གྱི། རྗོད་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1510 [HEADING]]
### རིགས་ཀྱི་སྒྲ་ཙམ་མམ་དེ་དང་ལྡན་པ་ཙམ། ^5-3-0

[Block 1511]
འགའ་ཞིག་ནི་འདི་སྙམ་དུ་སེམས་ཏེ། རིགས་ཀྱི་སྒྲ་ཙམ་མམ། དེ་དང་ལྡན་པ་ཙམ་ལ་ནི། འབྲེལ་པར་སླ་བ༌[^1156]ཡིན་པའི་ཕྱིར་དང་། མི་འཁྲུལ་པའི་ཕྱིར་རོ་ཞེའོ། །

[Block 1512]
དེ་དག་ཀྱང་། རིགས་སམ་ལྡན་སྒྲ་ཐ་དད་ཀྱི། །དེ་ལ་སོ་སོར་རྗོད་བྱེད་མིན། དེ་ལྟ༌[^1157]ན་ནི་རྫས་ཡོད་དོ་ཡོན་ཏན་ཡོད་དོ་ལས་ཡོད་དོ༌[^1158]ཞེས་ཐ་དད་པའི་དོན་གྱི་རྫས་ལ་སོགས་པའི་སྒྲས་གཞི་མཐུན་པ་ཉིད་དུ་མི་འགྱུར་ན། དེ་ལྟར་ཡང་མཐོང་བ༌[^1159]ན་ཡོད་པའམ། དེ་དང་ལྡན་པ་ལ་རྫས་སམ་ཡོན་ཏན་ལ་ནི་མི་སྲིད་དོ། །

[Block 1513]
འདི་ལྟར་རྫས་ཀྱིའོ༌[^1160]ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1514]
ཡང་བརྗོད་པ།

[Block 1515 [VERSE]]
ཡོན་ཏན་དང་ནི་ཡོན་ཏན་ཅན། །
བརྗོད་པའི་རྣམ་དབྱེ་ཐ་དད་དུ། །
ངེས་ཕྱིར་གཞི་དང་མཐུན་པ་ཡི། །
རྫས་དང་སྒྲ་དག་རབ་ཏུ་གྲུབ། །

[Block 1516 [VERSE]]
འབྲེལ་པ་ནི་འདིར་འབྲེལ་ཅན་གྱི། །
ཆོས་ཀྱི༌[^1161]འཕངས་པར་བརྗོད་བྱ་སྟེ། །
དེ་ལྟས་ངེས༌[^1162]བྱས་ནས་བརྗོད་ཀྱི། །
དངོས་པོ་གཞན་གྱིས་སྦྱར་མི་བྱ། །

[Block 1517]
འབྲེལ་པ་ནི་གདོན་མི་ཟ་བར་འབྲེལ་པར་འགྱུར་བའི་ངེས་པ་མེད་དེ་ཁ་བསྒྱུར་བ་ལ་སོགས་པ་བཞིན་གཞན་གྱི་གེགས་བྱེད་པ་སྲིད་དོ། །

[Block 1518]
དེའི་ཕྱིར་འབྲེལ་པ་ཅན་གྱི་ཆོས་ཀྱིས་འབྲེལ་པ་བརྗོད་པར་བྱ་བ༌[^1163]ཡིན་པའི་ཕྱིར་རང་གི་ཆོས་ཀྱི་ནི་འབྲེལ་པའི་རྗོད་པར་བྱེད་པའི་སྒྲའོ་ཞེས་ཡོད་པ་མ་ཡིན་པར་མཚོན་པས་ན།

[Block 1519]
འདི་ཡི་རིགས་ཀྱི་སྒྲ་ཡིས་ནི། །བརྗོད་པར་བྱ་བ་ཉིད་མི་འཐད། །

[Block 1520 [HEADING]]
### རིགས་དང་ལྡན་པ་ཙམ་བརྗོད་པ། ^5-4-0

[Block 1521]
ལ་ལ་དག་ནི་ཁྱད་པར་གྱི་སྒྲ་རྣམས་དང་གཞི་མཐུན་པ་ཡིན་པའི་ཕྱིར་དང་། འབྲེལ་པར་སླ་བའི༌[^1164]ཕྱིར་དང་། མི་འཁྲུལ་པའི་ཕྱིར་རིགས་དང་ལྡན་པ་ཙམ་བརྗོད་པར་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 1522]
དེ་ལ། རང་དབང་མེད་ཕྱིར་དེ་ལྡན་མིན། །དེ་ལྟ༌[^1165]ན་ཡང་རྫས་ཀྱི་རང་གི་ངོ་བོ་ཙམ་ཡོད་པའི་སྒྲས་ཁྱད་པར་དུ་བྱས་ནས་རྫས་ཞེས་བརྗོད་ཀྱི། དངོས་སུ་ནི་མ་ཡིན་པས་དེས་བུམ་པ་ལ་སོགས་པའི་ཐ་དད་མི་དབེན་པའི༌[^1166]ཕྱིར་དེ་ཉིད་ཐ་དད་པ་ཉིད་ལ་གཞི་མཐུན་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1523]
མེད་པ་དང་མ་བྱས་པ་དག་ལ་ནི་གཞི་མཐུན་པ་ཉིད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1524]
དཔེར་ན་དཀར་པོ་དང་སྒྲ་ལྟ་བུ་རང་གི་ཡོན་ཏན་བརྗོད་པར་བྱ་བ་ལ་རྫས་ཀྱི་ཁྱད་པར་དུ་བྱས་ནས་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 1525]
ཡོད་པས་རྫས་ལ༌[^1167]མངར་བ་ལ་སོགས་པ༌[^1168]ནི་མི་འཕེན་ནོ། །

[Block 1526]
དེ་ལྟ་བས་ན་འདིར་ཡང་དེ་བཞིན་དུ་ཐ་དད་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1527]
གཞན་ཡང་། ཉེ་བར་བརྟགས་ཕྱིར། སྒྲ་ནི་རང་གི་ངོ་བོའམ་རིགས་སུ་བརྗོད་པ་དེ་ལ་འཇུག་ཅིང་དེ་དང་ལྡན་པར༌[^1169]ཉེ་བར་བརྟགས་པ༌[^1170]ཡིན་ནོ། །

[Block 1528]
གང་ཞིག་གང་ལ་ཉེ་བར་བཏགས་པའི༌[^1171]དོན་དེ་ནི་ཡང་དག་པའི་དོན་མ་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 1529]
འདྲ་བ་ཡང་། མི་སྲིད་ཕྱིར། དེ་དང་ལྡན་པ་ཡང་ཡོན་ཏན་གྱིས་འདྲ་བ་ལ་ཡང༌[^1172]ཤེས་པ་འཕོ་བའི་འདྲ་བ་ཡང་མི་སྲིད་ལ། ཡོན་ཏན་གྱིས༌[^1173]ཕན་བཏགས་པའི་འདྲ་བ་ཡང་མི་སྲིད་པའི་ཕྱིར་རོ། །ཇི་ལྟར་ཤས་པ་འཕོ་བ་མི་སྲིད་ཅེ་ན། ཉེ་བར་བཏགས་པ་ནི།

[Block 1530]
འཕངས༌[^1174]ལ་རྒྱལ་པོར་བཏགས་པ་བཞིན། །བློ་ཡི་ཚུལ་ལ་ཐ་དད་ཕྱིར་རོ། །

[Block 1531]
དཔེར་ན་གང་མི་དེ་ནི་ང་རང་ངོ་ཞེས་བྲན་ལ་རང་གི་སྒྲར་བརྗོད་པ་ནི་རྒྱལ་པོ་དང་བྲན་པོ༌[^1175]ལ་བློ་མཚུངས་པར་སྐྱེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 1532]
རིགས་ཀྱི་སྒྲ་དེ་དང་ལྡན་པ་ལ་ཉེ་བར་བཏགས་པ་ཡང་།

[Block 1533 [VERSE]]
རིམ་གྱིས་རྗོད༌[^1176]པར་བྱེད་པ་ནི། །
ཀུན་ད་དུང་སོགས་དཀར་པོ་བཞིན། །

[Block 1534]
གང་ལ་ཤེས་པ་མཚུངས་པ་ཉིད་ལ་ནི་རིམ་གྱིས་བརྗོད་པར་མཐོང་སྟེ། དཔེར་ན་མེ་ཏོག་ཀུན་ད་དང་མེ་ཏོག་ཀུ་མུ་ཏ་དང་། དུང་གི་དཀར་པོའོ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1535]
ཅིག་ཅར་བ་ཡང༌[^1177]རིགས་དེ་དང་ལྡན་པའི་ལྟ་བུ་སྟེ། ཤེས་པ་འཕོ་བའི་དྲན་པ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1536]
ཡོན་ཏན་གྱིས་ཕན་བཏགས་དངོས་ལ། །བློ་མེད་པར་ཡང་འཇུག་པར་འགྱུར། །

[Block 1537]
གལ་ཏེ་ཤེས་བཞིན་དུ་ཡོན་ཏན་གྱིས་ཕན་བཏགས་པ་ལས་ཡོན་ཏན་གྱི་དངོས་པོ་དེ་དང་ལྡན་པར་འགྱུར་བ་ཉིད་ཡིན་ན་ནི་རྫས་ལ་འཇུག་པའི་བློ་ཡོན་ཏན་ལ་འཇུག་པའི་བློ༌[^1178]ལ་མི་ལྟོས་པར་འགྱུར་རོ། །

[Block 1538]
ཤེལ་དམར་པོའི་བློའི་དངོས་པོ་ནི་རྟེན་ལ་ལྟོས་པ་མ་ཡིན་ཏེ། རྣམ་པར་མ་སྦྱངས་པ་རྣམས་ལ་ཐ་དད་པའི་བློ་མེད་པའི་ཕྱིར་རོ། །

[Block 1539]
གཞན་ཡང་།

[Block 1540 [VERSE]]
འདྲེས་པའི་ཚུལ་ནས་ཐམས་ཅད་དུ། །
ལོག་པའི་ཤེས་པར་ཐལ་བར་འགྱུར། །

[Block 1541]
སྒྲ་དང་ཤེས་པ་ཐམས་ཅད་དོན་དང་འདྲེས་པའི་ཚུལ་ནས་ནི་རྣམ་པར་བསླད་པ་སྟེ། དེའི་ཕྱིར་ཤེལ་བཞིན༌[^1179]དུ་ཤེས་པ་ཐམས་ཅད་དོན་ཇི་ལྟ་བ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 1542]
གཞན་ཡང་།

[Block 1543 [VERSE]]
སྤྱི་སོགས་མང་པོ་ཉིད་དང་ནི། །
ཅིག་ཅར་འཛིན་པ་རྣམས་ལ་ཡང་། །
ཕན་འདོགས་པ་ནི་འགལ་བར་འགྱུར། །

[Block 1544]
གང་ཡང་མང་པོ་འཛིན་པར་འགྱུར་བ་ནི་དཀར་པོ་ལ་སོགས་པ་ནི་ཡོན་ཏན་ལྟ་བུ་སྟེ། དཔེར་ན་བུམ་པ་དང་། ས་ལས་བྱུང་བ་དང་། རྫས་དང་། ཁ་བ་དང་། མངར་བ་དང་། དྲི་ཞིམ་པ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^1180]དེའི་ཚེ་ཡོན་ཏན་གྱིས་ཕན་འདོགས་པ་འགལ་བར༌[^1181]འགྱུར་རོ། །

[Block 1545]
དེའི་ཚེ་ཡོན་ཏན་གྱི་ཚུལ་ནས་རྫས་དང་གཅིག་འགྱུར་བར་ནི་ནུས་པ་མ་ཡིན་ཏེ། ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
