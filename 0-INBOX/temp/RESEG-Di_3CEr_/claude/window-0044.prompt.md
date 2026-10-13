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

[Block 1546]
ཡུལ་གཅིག་པ་རྣམས་ལ་ཡོན་ཏན་གྱི་ཚུལ་ནས་ཉམས་སུ་མྱོང་བར་ཡང་ནུས་པ་མ་ཡིན་ནོ། །

[Block 1547]
ལན་ཅིག་ཏུ་བུམ་པ་ལ་སོགས་པའི་དངོས་པོ་རྟོགས་སོ་ཞེས་པ་དེ་ལ། གཟི་ཡི༌[^1182]ཁྲ་བོ་ཐམས་ཅད་མཐོང་། །ཅི་སྟེ་ཐམས་ཅད་བུམ་པ་ཡིན་པའི་ཕྱིར་ཞེས་པས་ནི་ཅིག་ཅར་དུ་དུས་གཅིག་སོ་སོར་ཕན་འདོགས་པར་བྱེད་པར་འགྱུར་ན་བུམ་པ་ལ་སོགས་པའི་དངོས་པོ་ལ་ནི་གཟུང་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1548]
གཟིའི༌[^1183]ཁྲ་བོ་ཐམས་ཅད་མཐོང་བ་ནི་དངོས་པོ་ཐམས་ཅད་ནི༌[^1184]ཅིག་ཅར་དུ་ཐོབ་པ་ཡིན་ནོ། །

[Block 1549 [VERSE]]
དེ་དག་ཐ་དད་རྣམས་ལ་ཡང་། །
དེ་དང་ལྡན་པའི་སྐྱོན་དེ་མཚུངས། །
རིགས་རང་ངོ་བོའམ་དེ་ལྡན་གྱི། །
ངོ་བོ༌[^1185]གང་ལས་སྦྱོར་མི་བྱ། །

[Block 1550]
ཐ་དད་པའི་ངོ་བོ་ལ་ཡང་གདོན་མི་ཟ་བར་བརྗོད་པ་ཡིན་ཏེ། རིགས་ཀྱི་ངོ་བོ་ཐ་དད་དུ་བརྗོད་པར་བྱ་བ་དང་། དངོས་ཀྱི་རིགས་དག་ལ་ཐ་དད་པ་རྣམས་ལ་ཉེ་བར་བཏགས་པའི་ཞེས་དེ་དང་ལྡན་པ་ལ་བརྗོད་པ་བཞིན་དུ་སྐྱོན་ཐམས་ཅད་བརྗོད་པར་བྱའོ། །

[Block 1551]
བརྗོད་པར་བྱ་བའི་རིགས་དག་ལ་ཡང་སྒྲའི་རང་གི༌[^1186]ངོ་བོ་སྒྲོ་བཏགས་ནས་རྫས་སུ་བརྗོད་པ་ཡིན་ནོ་ཞེས་སྲིད་པས་རིགས་དང་ལྡན་པ་དང་རིགས་ཀྱི་ངོ་བོ་ཡོད་པ་ལ་སོགས་པས་བརྗོད་པ༌[^1187]ཡིན་ནོ། །

[Block 1552]
འདིར་ཡང་སྐྱོན་ཇི་ལྟར་སྲིད་པ་ལྟར་བརྗོད་པར་བྱའོ། །

[Block 1553]
དེ་ལྡན་ཐ་དད་ཉིད་བརྗོད་ན། །དེ་ཡང་སྔར་ཉིད་བསལ་ཟིན་ཏོ། །

[Block 1554]
རིགས་ཀྱི་སྒྲ་རུའོ། །

[Block 1555]
བསལ་ཞེས་པ་ནི། སྔར་ཐ་དད་རྣམས་ཀྱི་རིགས་སྒྲ་མེད་རྗོད༌[^1188]པར་བྱེད་ཅེས་དེ་དང་རིགས་དང་ལྡན་པ་ལ་ཡང་བརྗོད་པ་ཡིན་ནོ། །

[Block 1556 [HEADING]]
### དེ་ལྡན་ཙམ་རྣམ་པར་དཔྱད་པ། ^5-5-0

[Block 1557]
ཅི་སྟེ་ཡང་རིགས་ནི་རིགས༌[^1189]དང་ལྡན་པ་ཙམ་གྱིས་རྗོད་པར་བྱེད་པ་ཡིན་གྱི་ཐ་དད་པའི་ངོ་བོར་ནི་མ་ཡིན་ནོ་ཞེས་བརྗོད་དོ་ཞེ་ན། གལ་ཏེ་དེ་ལྟ་ན།

[Block 1558 [VERSE]]
དེ་ལྡན་ཙམ་ཡང་འབྲེལ་པའམ། །
ཡོད་པ་ཡིན་ཞེས་རྣམ་པར་དཔྱད། །

[Block 1559]
དེ་ལྡན་ཙམ་ཞེས་པ་ལ་དེ་དང་ལྡན་པ་ཡང་དངོས་པོའི་རྐྱེན་ནམ་འབྲེལ་པའི་ཡོན་ཏན་དུ་འགྱུར་རོ། །

[Block 1560]
ཇི་ལྟར་དུ་བརྗོད་པའི་བསྡུ་བ་དང་། བྱེད་པ་དང་། དེ་ལ་ཕན་པ་རྣམས་ལ་འབྲེལ་པར་མངོན་པར་བརྗོད་དེ། གཞན་ལ་གྲགས་པའི་ཐ་དད་པའི་དངོས་པོ་འཁྲུལ་པ་མེད་པར་འབྲེལ་པ་དག༌[^1190]ལས་སོ། །ཞེས་པ༌[^1191]དེ་ལ་ཡང་།

[Block 1561]
རིགས་སམ་ལྡན་སྒྲས་ཐ་དད་ཀྱི། ། དོན་ལ་སོ༌[^1192]སོར་རྗོད་བྱེད་མིན། །ཞེས་བརྗོད་ཟིན་ཏོ། །

[Block 1562 [VERSE]]
བུམ་པ་སོགས་ཀྱི་དེ་ལྡན་དོན། །
སྣམ་བུ་སོགས་པ་འཇུག་མིན་ན།[^1193] །
སྤྱི་ཡི་དོན་དེ་ཇི་ལྟ་བུ། །

[Block 1563]
དུ་མ་ལ་འཇུག་པའི་སྤྱི་དེ་ཡང་གང་སྤྱི་དང་ལྡན་པའི་བུམ་པ་ལ་སོགས་པ་ལ༌[^1194]སྣམ་བུ་ལ་སོགས་པ༌[^1195]འཇུག་པ་ཡིན་ནམ། དེ་དག་གི་སྤྱི་དེ་ཇི་ལྟ་བུ་ཞིག་ཅེས་སྦྱར་བར་བྱའོ། །ཅི༌[^1196]སྟེ་སྤྱི་དང་ལྡན་པ་བརྗོད་དོ་ཞེ་ན། དེའི༌[^1197]སྤྱི་ཉིད་དུ་སྒྲོ་བཏགས་པའི་དོན་ཅི༌[^1198]ཡིན། འདི་ལྟར་ཡོད་པའི་སྒྲ་ནི་སྤྱི་བརྗོད་པའི་ཚིག་གོ་ཞེས་དམ་བཅའ་བ་ལ་ཡོད་པ་ལ་སོགས་པ་ལ་ཡང་ཡོད་པ་ལ་སོགས་པ་མེད་པའི་ཕྱིར་དེ་ལ་འཇུག་པས་ནི་བརྗོད་པར་མི་བྱའོ། །

[Block 1564]
དེའི་ཕྱིར་གདོན་མི་ཟ་བར་སྤྱིའི་དོན་ཁས་བླང་བར་བྱ་ན། དེ་ཡང་དོན་ལ་ཡོད་པ༌[^1199]མ་ཡིན་པ་དེའི་ཕྱིར། སྒྲ་དོན་འབའ་ཞིག་པ་དང་མཚུངས། །དེ་དང་ལྡན་པའི་བུམ་པ་ལ་སོགས་པ་ནི་ཡོད་པའི་སྒྲས་བརྗོད་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་དེ་དང་ལྡན་པ་ཡོད་པ་དང་སྦྱོར་བ་ནི་སྔར་ཅུང་ཟད་ཀྱང་གྲུབ་པ་མེད་དོ། །

[Block 1565]
དེ་ཡང་རྒྱུ་མཚན་མེད་པར་འདོད། །སྒྲ་ཐ་དད་རྣམས་ལ་ནི་ཐ་མི་དད་ཀྱི་རྒྱུ་མཚན་གཞན་མ་མཐོང་ངོ་། །དེའི་ཕྱིར་དེ་ཡང་སྤྱི་རུ་སྦྱར་བར་མི་བྱའོ། །

[Block 1566]
དེ་ལྟ་བས་ན་ཁྱད་པར་དུ་བྱ་བ་དག་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1567]
ཅི་སྟེ་ཡོད་པའི་སྒྲ་ལས་ཡོན་ཏན་ཡོད་པ་ལས་གཞན་མ་ཡིན་པའི་རྫས་ལ་འཇུག་པ་ནི་ཤིན་ཏུ་སྔོ་བ་ལ་སོགས་པ་བཞིན་དུ་བུམ་པ་ལ་སོགས་པ་ལ་ཡང་འདོད་པ་ཡིན་ལ་ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར་དུ་བྱ་བར་འགྱུར་རོ་ཞེ་ན།

[Block 1568]
གལ་ཏེ་གཅིག་ལའང་སྔོ་སོགས་བཞིན། །འབྲེལ་པའི་ཡོན་ཏན་དུ་འགྱུར་རོ། །

[Block 1569]
དེ་ལྟའང་མ་ཡིན། སྔོན་པོའི་སྒྲ་ནི་ཤིན་ཏུ་སྔོ་བ་ལ་སོགས་པ་མེད་པར་གཞན་གྱིས་དེ་དང་ལྡན་པར་འཐད་པ་མ་ཡིན་ནོ། །

[Block 1570]
སྔོན་པོ་ཉིད་དང་འབྲེལ་པ་ནི་སྒྲའི་དོན་མ་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 1571]
གཞན་ཡང་སྤྱི༌[^1200]དེ་ཁས་བླངས་ཀྱང་། །རིགས་ལ་རིགས་མེད་པས་དེ་མིན། །

[Block 1572]
ཁས་བླངས་སུ་ཟིན་ཡང་སྔོན་པོ་ལ་སོགས་པ་ལ་སྔོན་པོའི་སྤྱི༌[^1201]ཇི་ལྟར་རྣམ་པ་གསུམ་དུ་ཕྱེ་བའི་སྔོན་པོའི་ཡོན་ཏན་དག་ལ་རིགས་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1573]
གང་བུམ་པ་ཉིད་ལ་སོགས་པའི་རིགས་དང་ལྡན་པ་དེའི་ཁྱད་པར་ཉེ་བར་བླངས་པའི༌[^1202]ཕྱིར་རྫས་ལ་འཇུག་པའི་བུམ་པ་ཉིད་ལ་སོགས་པའི་ཁྱད་པར་འདོད་པ་ཡིན་ནོ། །

[Block 1574]
དེའི་ཕྱིར་འདི་ཡང་བརྟག་པར་མི་བྱའོ། །

[Block 1575]
དེ་ལྟ་ན་ནི་སྒྲར་བརྗོད་པར་བྱ་བ་མ་ཡིན་ཡང་དོན་གྱིས་འཕངས་པའི་བུམ་པ་ལ་སོགས་པ་ལ་ཁྱད་པར་འདོད་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1576]
བུམ་པ་ལ་སོགས་པའི་དེ་དང་ལྡན་པའི་དོན་ནི་གདོན་མི་ཟ་བར་ཅུང་ཞིག་ཀྱང་འབྲེལ་པ་མ་ཡིན་ནོ། །

[Block 1577]
དོན་གྱིས་འཕངས་པའང༌[^1203]མ་ངེས་པའོ། །

[Block 1578]
དོན་གྱིས་འཕངས་པ་ཞེས་བྱ་བ་ནི། གང་ལ་དོན་གྱི་ཤུགས་ཀྱིས་ངེས་པར་སྐྱེད་པ༌[^1204]སྟེ། དཔེར་ན་ཉིན་པར་མི་ཟའོ་ཞེས་པ་ལས་ནུབ་མོ་ཟ་བར་ངེས་པ་ལྟ་བུའོ། །

[Block 1579]
འདིར་ནི་ཡོད་ཅེས་བརྗོད་པས་བུམ་པ་ལ་སོགས་པ་ལ་མ་ངེས་པའི་ཕྱིར་ཐེ་ཚོམ་ཟ་བ་ཡིན་པས་དོན་གྱིས་འཕངས་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1580]
དེའི་ཕྱིར་རིགས་ཀྱི་སྒྲ་ཐ་དད་འབྲེལ་པའི་སྤྱི་རིགས་དང་ལྡན་པའི་རྗོད་པར་བྱེད་པ༌[^1205]ལན་འགའ་ཡང་སྦྱར་བར་མི་བྱའོ། །
--- END BLOCKS ---
