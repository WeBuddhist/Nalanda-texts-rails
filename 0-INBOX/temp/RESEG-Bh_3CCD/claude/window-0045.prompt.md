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
གང་གི་ཚེ་རྡོ་རྗེ་བཟླས་པའི་རིམ་གྱིས་སྲོག་དང་རྩོལ་བ་ཤེས་པར་འགྱུར་བ་དེའི་ཚེ་གསུང་གི་རྡོ་རྗེའི་ཏིང་ངེ་འཛིན༌[^1121]གསལ་བར་འགྱུར་རོ། །

[Block 1577]
ངག་རྣམ་པར་དབེན་པ་ལ་གནས་ནས་རང་བཞིན་གྱིས༌[^1122]སྣང་བའི་རིམ་གྱིས་སེམས་ཀྱི་ཏིང་ངེ་འཛིན་ལ་འཇུག་པར་འགྱུར་རོ། །

[Block 1578]
སེམས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པ་ལ་གནས་ནས་སྒྱུ་མའི་དཔེ་བཅུ་གཉིས་ཀྱི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ལ་འཇུག་པར་འགྱུར་རོ། །

[Block 1579]
གང་གི་ཚེ་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལ་འཇུག་པ་དེའི་ཚེ༌[^1123]སངས་རྒྱས་ཀྱི་དབང་བསྐུར་བ་ཐོབ་བོ། །

[Block 1580]
གང་གི་ཚེ་དབང་བསྐུར་བ་ཐོབ་པ་དེའི་ཚེ་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལ་གནས་ནས་སྟོང་པ་ཆེན་པོ་བཅོ་བརྒྱད་ཀྱི་རིམ་པས་དོན་དམ་པའི༌[^1124]བདེན་པ་ལ་འཇུག་གོ། །

[Block 1581]
གང་གི་ཚེ་རིལ་པོར་འཛིན་པ་དང་རྗེས་སུ་འཛིན་པའི་ཏིང་ངེ་འཛིན་གྱིས་ཡང་དག་པའི་མཐའ་ལ་འཇུག་པ་དེའི་ཚེ་ཉོན་མོངས་པ་ཐམས་ཅད་རྣམ་པར་དག་པར་འགྱུར་རོ། །

[Block 1582]
གང་གི་ཚེ་ཡེ་ཤེས་ཀྱི་རིམ་གྱིས་ལྡང་བའི་ཕྱིར་རང་བཞིན་གྱིས་འོད་གསལ་བའི་བདེན་པ་གཉིས་ལ་གཉིས་སུ་མེད་པའི་རྣལ་འབྱོར་པས་བདག་ཉིད་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ་དེའི་ཚེ་རྫོགས་པའི་ཏིང་ངེ་འཛིན་ལ་སློབ་པར་འགྱུར་རོ། །

[Block 1583]
གང་གི་ཚེ་རྫོགས་པའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་འཇུག་པའི་རྣལ་འབྱོར་པས་ནི་ཡང་ཆོས་གང་ལ་ཡང་མི་སློབ་བོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། སྔོན་ལེགས་པར་བསླབས་པའི་ཕྱིར་དེའི༌[^1125]སྔོན་གྱི་འཕེན་ཤུགས་ཀྱི་སྟོབས་ཀྱིས་མངོན་སུམ་དུ་འགྱུར་རོ་ཞེའོ། །

[Block 1584]
དེའི་ཕྱིར་ན་རིམ་གྱིས་ཐོབ་པར་བྱ་བ་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད། རིམ་པ་ལྔ་བསྒོམ་པས༌[^1126]ཐོབ་པ་ཡིན་ཞེས་རྣལ་འབྱོར་པ་གཅིག་གིས་ཐམས་ཅད་བསྒོམ་མོ། །

[Block 1585]
གང་ཡང་རིམ་པ་རེ་རེ་ལ་འོད་གསལ་བ༌[^1127]བཤད་པ་དེ་ནི་དེ༌[^1128]ཁོ་ན་ཉིད་ཀྱིས་ཀུན༌[^1129]ཁྱབ་བོ་ཞེས་བསྟན་པར་བྱ་བའི་ཕྱིར་ཡིན་གྱི། དེ་ཉིད་དུ་ཡོངས་སུ་རྫོགས་པ་མ་ཡིན་ནོ། །

[Block 1586]
བྱ་བ་བྱས་པ་ཉིད་ནི་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ལའོ། །

[Block 1587]
ཇི་སྐད་དུ།

[Block 1588 [VERSE]]
འདི་ནི་རྫོགས་པའི་རྣལ་འབྱོར་ཞེས། །
རྡོ་རྗེ་འཆང་བ་ཆེན་པོ་ཉིད། །
རྣམ་པ་ཐམས་ཅད་མཆོག་ལྡན་པ། །
ཐམས་ཅད་མཁྱེན་པའང་དེ་ནས་འགྱུར། །

[Block 1589]
ཞེས་དང་། དེ་བཞིན་དུ་ཡང་གསུངས་ཏེ། ཟུང་འཇུག་གི་ཏིང་ངེ་འཛིན་ལ་གནས་པས་སླར་ཡང་གང་ལ་མི་བསླབ་པོ་ཞེས་འབྱུང་ངོ་། །

[Block 1590]
དེའི་ཕྱིར་རིམ་པ་ལྔ་ལ་བརྟེན་ནས་རྣལ་འབྱོར་པ་གཅིག་གིས་འབྲས་བུའི་གནས་སྐབས་སུ་དངོས་གྲུབ་ཐོབ་པ་ཡིན་ནོ། །

[Block 1591]
ལེའུ་བཅོ་བརྒྱད་པའི་བརྗོད་པར་བྱ་བའི་རིམ་པ་གཉིས་སྒོམ་པ་པོ་རྣལ་འབྱོར་པ་གཅིག་གིས་ཐོབ་པར་བྱ་བ་རྡོ་རྗེ་འཆང་གི་གོ་འཕང་བཞིན་ནོ། །

[Block 1592]
རྩ་བའི་རྒྱུད་ཀྱི་ལེའུ་བཅོ་བརྒྱད་ལ་རྣལ་འབྱོར་པས་བཅོ་བརྒྱད་སོ་སོར་སྒོམ་པ་པོ༌[^1130]མ་བསྟན་ཏོ། །

[Block 1593]
འོན་ཀྱང་གཅིག་པུ་ཉིད་དོ། །

[Block 1594]
རིམ་པ་གཉིས་མ་གཏོགས་པར་གཞན་མ་གསུངས་སོ།[^1131] །

[Block 1595]
དེ་དག་གི་སྒོམ་པ་པོ་ནི་གཅིག་ཡིན་ཞེས་སྔོན་དུ་བཤད་དོ། །

[Block 1596]
གང་ཟག་གི་དབྱེ་བ་ནི་བཤད་པའི་དབྱེ་བས་བཤད་དུ་རུང་བའོ། །

[Block 1597]
ཐབས་ལ་མཁས་པ་དང་ལྡན་པའི་བཅོམ་ལྡན་འདས་སངས་རྒྱས་རྣམས་ཀྱིས་སེམས་ཅན་གྱི་བསམ་པའི་དབྱེ་བས་སེམས་ཅན་གྱི་རྒྱུད་ཀྱི་ཁྱད་པར་ཤེས་ནས་དེ་དང་རྗེས་སུ་མཐུན་པར༌[^1132]བསྟན་པར་མཛད་དོ། །

[Block 1598]
འབྲས་བུ་ལ་དགོངས་ཏེ་དབྱེ་བ་མ་བསྟན་ཏེ། དེ་གཅིག་གི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1599]
ལམ་ནི་ཐ་དད་པ་ཁོ་ན་སྟེ། ལམ་གྱི་འབྲས་བུར་གྱུར་པའི་དེ་ཁོ་ན་ཉིད་ཀྱི་དབྱེ་བ་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ཏེ། ལམ་དུ་མས་ཐོབ་པར་བྱ་བ་གྲོང་ཁྱེར་ཆེན་པོ་བཞིན་ནོ། །

[Block 1600]
མོས་པའི་བྱེ་བྲག་གི་དེ་ཁོ་ན་ཉིད་གཅིག་པུ་ཡང་ཉན་པ་པོས་བྱེ་བྲག་ཏུ་གཟུང༌[^1133]ངོ་། །དཔེར་ན་ཉན་ཐོས་རྣམས་ཀྱིས་འགོག་པའི་སྙོམས་པར་ཞུགས་པའི་སྒོ་ནས་གཟུང་བར་བྱེད་དེ། མདོ་སྡེ་པ་རྣམས་ཀྱིས་དེ་ཉིད་རྗེས་སུ་དཔག་པའི་ཕྱིའི་དོན་ཡོད་པར་སོ་སོར་སྣང་བའི་སྒོ་ནས་སོ། །

[Block 1601]
རྣམ་པ་དང་བཅས་པའི་རྣམ་རིག་སྨྲ་བ་རྣམས་ཀྱིས༌[^1134]ཤེས་པའི་རྣམ་པ་ཕྱིའི༌[^1135]དོན་ཡོད་པའི་སྒོ་ནས་སོ། །

[Block 1602]
རྣམ་པ་མེད་པའི་རྣམ་རིག་སྨྲ་བ་པོས་ཕྱིའི་དངོས་པོ་ལས་ངེས་པར་གྲོལ་བ་དྲི་མ་མེད་པ་མཐའ་ལས་འདས་པའི་ནམ་མཁའ་གཅིག་པུ་དང་མཚུངས་པའི་རྣམ་པར་རིག་པ་གཅིག་པུ་ཡོད་པའི་སྒོ་ན་གཟུང༌[^1136]ངོ་། །ལ་ལ་ཡང་དབུ་མ་པ་རྣམས་ཀྱིས་གཟུང་བ་དང་འཛིན་པ་ལས་གྲོལ་བ་རབ་ཏུ་ཞི་ཞིང་སྤྲོས་པ་མེད་པ་འབའ་ཞིག་ཏུ་སྟོང་པ་ཉིད་ཀྱིས༌[^1137]ངོ་བོ་ཉིད་དངོས་པོ་སོ་སོར་སྣང་བ་ཙམ་གྱི་སྒོ་ནས་གཟུང་བ་དང་། བྱ་བའི་རྒྱུད་ཀྱི་རྣལ་འབྱོར་པས་ལྷའི་རྣམ་པ་སྒོམ་པ་ཙམ་གྱི་སྒོ་ནས་གཟུང་བ༌[^1138]དང་། སྤྱོད་པའི་རྒྱུད་ཀྱི་རྣལ་འབྱོར་པས་དངོས་གྲུབ་དང་ཏིང་ངེ་འཛིན་དང་ཆོ་འཕྲུལ་དང་ལྡན་པ། སྔགས་ཀྱི་སྐུ་བསྒོམ་པའི༌[^1139]སྒོ་ནས་སོ། །

[Block 1603]
རྣལ་འབྱོར་གྱི་རྒྱུད་གཙོར་གྱུར་པའི་རྣལ་འབྱོར་པས་སྔགས་དང་ཕྱག་རྒྱ་ལ་སོགས་པ་གཙོར་གྱུར་པའི་རྣལ་འབྱོར་པས་རྡོ་རྗེ་དབྱིངས་ཀྱི་དཀྱིལ་འཁོར་ཆེན་པོ་ལ་སོགས་པའི་བསྒོམ་པའི༌[^1140]རིམ་པས་སོ། །

[Block 1604]
རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ཀྱི་རྣལ་འབྱོར་པས་རིམ་པ་གཉིས་ཀྱིས་སོ། །

[Block 1605]
དེ་ལ་བསྐྱེད་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་ཏིང་ངེ་འཛིན་གསུམ་གྱི་སྒོ་ནས་དེ་ཁོ་ན་ཉིད་གཟུང༌[^1141]བའོ། །

[Block 1606]
རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་ཕྲ་མོའི་རྣལ་འབྱོར་གཟུང་བའི་སྒོ་ནས་དེ་ཁོ་ན་ཉིད་གཟུང༌[^1142]བའོ། །

[Block 1607]
ལ་ལས་ཀྱང་ཐིག་ལེའི་རྣལ་འབྱོར་བསྒོམ་པའི༌[^1143]རིམ་པས་འདོད་དོ། །

[Block 1608]
ལ་ལས་ཀྱང་རྩ་ཀུན་ཏུ་རྒྱུ་བའི༌[^1144]རྩའི་བསྒོམ་པས༌[^1145]སོ། །

[Block 1609]
ལ་ལས་ཀྱང་དམ་ཚིག་གི་དཀྱིལ་འཁོར་གྱི་སྒོ་ནས་གཟུང་ངོ་། །ལ་ལས་ཀྱང་དེའི་ནང་དུ་གསང་བའི་དཀྱིལ་འཁོར་ལ་གསང་བའི་དབང་གིས༌[^1146]སོ། །

[Block 1610]
གཞན་དག་གིས་ཀྱང་བྱང་ཆུབ་ཀྱི་སེམས་གཟུང་བ་གཅིག་པུས་སོ། །

[Block 1611]
གཞན་ཡང་དེ་ཉིད་སྟེང་དུ་བཟློག་པའི་སྒོ་ནས་སོ། །

[Block 1612]
ལ་ལས་ཀྱང་ཡུལ་དང་དབང་པོའི་ལོངས་སྤྱོད་ཅིང་སོ་སོར་སྡུད་པའི་བསྒོམ་པའི༌[^1147]རིམ་པས་སོ། །

[Block 1613]
གཞན་དག་གིས་ཀྱང་དེའི་རྣམ་པར་དག་པའི་ངོ་བོ་ཉིད་དེ་བཞིན་གཤེགས་པ་ལྔའི་རང་བཞིན་རྟོག་པ་དང་དཔྱོད་པ༌[^1148]ལ་སོགས་པ་རྣམ་པ་ལྔའི་བསམ་གཏན་གྱི་རིམ་པས་སོ། །

[Block 1614]
ཁ་ཅིག་གིས་ཀྱང་སྟེང་དང་འོག་ཏུ་རྒྱུ་བའི་རླུང་གསུམ་གྱི་བདག་ཉིད་སྲོག་དང་རྩོལ་བའི་རླུང་གི་སྒོ་ནས་དེ་ཁོ་ན་ཉིད་ངེས་པར་གཟུང་ངོ་། །དེ་བཞིན་དུ་གཞན་རྣམས་ཀྱིས་ཀྱང་སྣ་གསུམ་གྱི་རྩེ་མོར་འཛིན་པར་གྱུར་པ་རླུང་དང་སྔགས་དང་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེ་འཛིན་པས་སོ། །

[Block 1615]
ཁ་ཅིག་གིས་ཀྱང་སྤྲུལ་པ་མཐའ་ཡས་པ་སྤྲོ་བས་ནམ་མཁའི་དབྱིངས་ཡོངས་སུ་བཀང་ཞིང་རྗེས་སུ་དྲན་པའི་ཡན་ལག་བསྒོམ་པས་སོ། །
--- END BLOCKS ---
