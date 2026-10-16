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

[Block 1581]
དེ་བས་ན་ཇི་ལྟར་ཚིག་ནི་སྐྱེས་བུ་ལ་བརྟེན་པ་ཉིད་ཀྱི་ཕྱིར་ལོག་པའི་དོན་ཡིན་པ་དེ་ལྟར་བདེན་པའི་དོན་ཡང་ཡིན་པའི་ཕྱིར། དེ་ལོག་པ་ན་དེ་ཡང་ལོག་པ་དེ་ལྟར་ན་མེད་པའམ་ཕྱིན་ཅི་ལོག་ཏུ་འགྱུར་རོ། །

[Block 1582]
སྒྲ་རྣམས་ནི་ངོ་བོ་ཉིད་ཀྱི༌[^1174]དོན་དང་ལྡན་པ་མ་ཡིན་གྱི་བརྡ་ལས་ཡིན་ཏེ། དེ་ལས་དོན་རྟོགས་པའི་ཕྱིར་ལུས་ཀྱི་བརྡ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 1583]
རྗེས་སུ་མཐུན་པར་རུང་བ་ཉིད་ཡིན་ཏེ། བརྡའི་ཚེ་དེའི་འདོད་པ་བརྡར༌[^1175]བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1584]
ངོ་བོ་ཉིད་ཀྱི༌[^1176]གྲུབ་པ་དག་ལ་ནི་འདོད་པའི་དབང་གིས་བསྟན་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1585]
དེ་དག་དོན་མེད་པ་ཅན་ཡིན་པས་སྐྱེས་བུས་ལེགས་པར་བྱས་པ་ལས་དོན་དང་ལྡན་པར་འགྱུར། དེ་དག་ཀྱང་དེ་དག་གིས་ལེགས་པར་བྱ་བ་ཁོ་ན་སྐྱེས་བུས༌[^1177]བྱས་པ་ཅན་ཁོ་ན་ཉིད་དུ་རིགས་ཀྱི་སྐྱེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1586]
དེ་ཉིད་ལས་དོན་ལ་འཁྲུལ་པའི་ཕྱིར་རོ། །

[Block 1587]
སྐྱེས་པ༌[^1178]ཡང་རྣམ་པ་གཞན་དུ་བརྡར༌[^1179]བྱས་པ༌[^1180]ཡང་དེ་ལས་གཞན་པའི་སྐྱེས་བུའི་ཆོས་དང་འདྲ་བར་འགལ་བ་མེད་པ་ཅན་ཡིན་ནོ། །

[Block 1588]
དེ་བས་ན་འདི་ལོག་པས་རང་གིས་བྱས་པའི་བརྡ་ལས་བྱུང་བ་ཅན་གྱི་དོན་གྱི་བློ་དག་ལོག་པར་འགྱུར་རོ། །

[Block 1589]
དེ་བས་ན་དེ་ལོག་པར་གང་ལས་བདེན་པའི་དོན་ཅན་ཉིད་ཡིན། ཅི་སྟེ་ཡང་སྐྱེས་པ་ཁོ་ན་སྐྱེས་བུས་བྱས༌[^1181]པ་ཉིད་ཡིན་གྱི་བརྡར་བྱས་པ་མ་ཡིན་ན།

[Block 1590 [VERSE]]
དོན་ཤེས་བྱས༌[^1182]པ་དག་གི་རྒྱུ། །
བརྡ་ནི་སྐྱེས་བུ་ལ་བརྟེན་པས། །
ཚིག་རྣམས་སྐྱེས་བུས་བྱས་མིན་ཡང་། །
དེ་ཕྱིར་ལོག་པ་ཉིད་དུ་སྲིད། །

[Block 1591]
འདི་སྐྱེས་བུས་བྱས་པ་མ་ཡིན་པ་ཉིད་ཀྱིས་ཅི་ཞིག་བྱ། བརྡ་གང་ལས་དོན་རྟོགས་པར་འགྱུར་བ་དེ་སྐྱེས་བུས་མ་བྱས་པ་དེ་ནི་ཕྱིན་ཅི་ལོག་ཏུ་ཡང་འགྱུར་རོ། །

[Block 1592]
བརྡ་རྣམ་པ་གཞན་གྱིས་ཚུལ་ཁྲིམས་སྒྲུབ་པར་བྱེད་པ་ཅན་གྱི་མཐོ་རིས་ཀྱི་ཚིག་ཕྱིན་ཅི་ལོག་ཏུ་འགྱུར་རོ། །

[Block 1593]
དེ་བས༌[^1183]ན་དོན་ཇི་ལྟ༌[^1184]བ་བཞིན་མ་ཡིན་ཡང་སྟོན་པར་བྱེད་པ་སྲིད་པའི་ཕྱིར་དེ་ཉིད་སྐྱོན་ཡིན་ནོ། །

[Block 1594 [VERSE]]
འབྲེལ་པ་སྐྱེས་བུས་བྱས་མིན་ན། །
བརྡ་རིག་མེད་པར་རྟོགས་པར་འགྱུར། །

[Block 1595]
དེ་ལྟར་ནི་འགྱུར་ན་སྒྲ༌[^1185]འབྲེལ་པ་མ་བྱས་པ་ཅན་དེ་དག་ནི་དོན་རྣམས་ལ་སྐྱེས་བུ་དག་གིས། རྣམ་པ་གཞན་དུ་ཕྱིན་ཅི་ལོག་པར་འགྱུར་བ་མ་ཡིན་པ་དེ་བས་ན་སྐྱོན་ཡོད་པ་མ་ཡིན་ནོ་ཞེ་ན། ད་ནི་བརྡ་ཅི་ཞིག་བྱ་སྟེ། གང་ལས་དོན་རྟོགས་པ་དེ༌[^1186]ནི་འབྲེལ་པ་ཡིན་ནོ། །

[Block 1596]
གལ་ཏེ་དེ་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་ན་འདི་ནི་བརྡ་ལས་ལྟོས་པ་མེད་པ་ཉིད་ཡིན་ནོ། །

[Block 1597]
རྟོགས་པ་ལ་བརྟེན་པ་མ་ཡིན་ན་ཇི་ལྟར་ན་འབྲེལ་པ་ཡིན་ན།

[Block 1598 [VERSE]]
[^1187]བརྡས་དེ་དག་ནི་གསལ་ཡིན་ན། །
རྟོགས་པ༌[^1188]གཞན་དག་དོན་མེད་འགྱུར། །

[Block 1599]
འབྲེལ་པ་ཡོད་ན་ཡང་གསལ་བ་མེད་ན་རྟོགས་པའི་རྒྱུ་མ་ཡིན༌[^1189]ནོ། །

[Block 1600]
བརྡས་ཀྱང་འདི་གསལ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 1601]
འོན་ཏེ༌[^1190]གྲུབ་པ་ལ་ཉེ་བར་གནས་པ་ཅན་རྒྱུ་མ་ཡིན་པས་ཅི་ཞིག་བྱ། འབྲེལ་པའི་བྱ་བ་ནི་གང་དོན་རྟོགས་པ་སྐྱེད་པར་བྱེད་པ་དེ་ཙམ་མ་ཡིན་ནམ། དེ་ནི་བརྡ་ཉིད་ཀྱིས་བྱས་ཟིན་ཏོ། །

[Block 1602]
གལ་ཏེ་རུང་བ་མ་ཡིན་པའི་བརྡས་ནུས་པ་མ་ཡིན་པའི་ཕྱིར་རུང་བ་ཉིད་འབྲེལ་པ་ཡིན་ནོ་ཞེ་ན། དེ་བས་ན་ཅི་སྒྲ་འབྲེལ་པ་ཡིན་པར་བྱ༌[^1191]སྟེ། རྒྱུ་དང་འབྲས་བུའི་རུང་བ་ཉིད་དང་འདྲ་བར་སྒྲའི་ནུས་པའི་ངོ་བོ༌[^1192]རུང་བ་ཉིད་ཡིན་ནོ། །

[Block 1603]
གལ་ཏེ་དོན་གཞན་ཡིན་ན་སྒྲའི༌[^1193]ཞེས་བྱ་བའི་འབྲེལ་པ་བརྗོད་པས་ཅི་ཞིག་བྱ། གལ་ཏེ་རུང་བ་ཉིད་ལ་ཕན་འདོགས་པར་བྱེད་པ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ་རྟག་པ་ཉིད་ནི་ཕུལ་དུ་དབྱུང་དུ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1604]
དེ་ལ་ཡང་ཤིན་ཏུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར། ཕན་འདོགས་པ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1605]
རུང་བ་ཉིད་ཀྱང་དོན་ལ་ངོ་བོ་ཉིད་ཀྱིས་རུང་བ་ཉིད་དུ་ཅིའི་ཕྱིར་མི་འདོད། འོན་ཏེ་བརྡ་ནི་ཇི་ལྟར་སྒྲ་དང་དོན་དག་གི་འབྲེལ་པ་ཡིན་ཏེ། སྐྱེས་བུ་རྣམས་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 1606]
མ་འདྲེས་པ་རྣམས་དང་གྲུབ་པ་རྣམས་ལ་ནི་འབྲེལ་པ་གང་ཡང་ཡོད་པ་མ་ཡིན་ཏེ། ཐ་དད་པ་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དང་ལྟོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1607]
དོན་གྱི་ཁྱད་པར་བརྗོད་པར་འདོད་པ་འཕངས་པའི་ཚིག་གིས་འདི་ལས་འདི་ཞེས་ཤེས་པའི་རང་གི་རྒྱུ་ལ་སྣང་བའི་དོན་རྟེན་པར༌[^1194]བྱེད་པའི་ཕྱིར། བློའི་ངོ་བོ་དང་ངག་གི་རྣམ་པར་རིག་བྱེད་དག་ནི་བསྐྱེད་པར་བྱ་བ་དང་སྐྱེད་པར་བྱེད་པའི་ངོ་བོའི་འབྲེལ་པ་ཡིན་པ་དེ་བས་ན་སྒྲ་ལས་རྟོགས་པ་ནི་མེད་ན་མི་འབྱུང་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1608]
དེ༌[^1195]གསལ་བར་བྱེད་པ་ནི་བརྡ་ཡིན་ཏེ། དེ་ལས་ཤེས་པར་བྱེད་པའི་འབྲེལ་པ་གྲུབ་པའི་ཕྱིར་དང་། འབྲེལ་པ་གསལ་བར་བྱེད་པའི་ཕྱིར། དེ་ཉིད་ནི་འབྲེལ་པ་མ་ཡིན་ནོ། །

[Block 1609]
གཞན་ཉིད་འབྲེལ་པ་རྟག་པ་ཡིན་པར་ནི་བླ་སྟེ། དེས་ན།

[Block 1610 [VERSE]]
ཚིག་རྣམས་དོན་གཅིག་ལ་ངེས་ན། །
དོན་གཞན་རྟོགས་པར་མི་འགྱུར་རོ། །

[Block 1611]
འབྲེལ་པ་དེས་འབྲེལ་པ་མེད་པའི་དོན་རྟོགས་པར་རིགས་པ་མ་ཡིན་ཏེ། དེ་ནི་དོན་མེད་པ་ཅན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1612]
འདོད་པའི་དབང་གིས་བརྡར་བྱས་པ་ཅན་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་གསལ་བར་བྱེད་པ་ཡང་མཐོང་ངོ་། །

[Block 1613 [VERSE]]
དོན་དུ་མ་དང་མངོན་འབྲེལ་ན། །
འགལ་བ་གསལ་བར་བྱེད་པ་སྲིད། །

[Block 1614]
ཅི་སྟེ་མཐོང་བ་འགལ་བར་མ་གྱུར་ཅིག་སྙམ་པས་ཐམས་ཅད་ཐམས་ཅད་ཀྱི་རྗོད་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1615]
དེ༌[^1196]ལྟར་ན་ཐམས་ཅད་ཐམས་ཅད་ཀྱི་སྒྲུབ་པར་ནི་མ་ཡིན་ཏེ། རྒྱུ་དང་འབྲས་བུ་དག་ནི་འཆོལ་བ་མེད་པའི་ཕྱིར་རོ།[^1197] ། དེ་ལས་སོ་སོར་ངེས་པར་བྱེད་པ་སྒྲུབ་པ་ཅན་གྱི་མངོན་པར་འདོད་པའི་དོན་ལ་བསྒྲུབ་པར་བྱ་བ་དང་། སྒྲུབ་པར་བྱེད༌[^1198]པ་ཐམས་ཅད་ཀྱི་ཐུན་མོང་གི་སྒྲ་ནི་འདོད་པའི་དོན་གསལ་བར་བྱེད༌[^1199]པས་བྱས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་གང་ལས་ཡིན། དེ་མ་ངེས་པ་ངེས་པ་སྐྱེས་བུ༌[^1200]ལས་མཐོང་བར་འགྱུར་བ་དེའི་ཚེ། སྐྱེས་བུས་མ་བྱས་པ་ཉིད་ཀྱི་ཀུན་ཏུ་རྟོག་པའང་དོན་མེད་འགྱུར། ཇི་ལྟར་ཡང་དོན་མ་འཆོལ་བ་རྟོགས་པའི་ཕྱིར་སྐྱེས་བུ་རྒྱུར་འཆོལ་བ་གསལ་བ་ཡིན་ནོ། །
--- END BLOCKS ---
