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

[Block 1616]
ལ་ལས་ཀྱང་དངོས་པོ་ཐམས་ཅད་ཉེ་བར་སྡུད་ཅིང་གཅིག་དང་དུ་མ་ལ་སོགས་པ་སྤངས་པའི་གཉིས་སུ་མེད་པའི་ཏིང་ངེ་འཛིན་གྱི་རིམ་པས་སོ། །

[Block 1617]
ལ་ལ་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་དམ་རླུང་གི་དེ་ཁོ་ན་ཉིད་བསྒོམ་པས༌[^1149]སོ། །

[Block 1618]
ལ་ལས་ཀྱང་སྔགས་དང་ཕྱག་རྒྱ་ལ་སོགས་པའི་རིམ་པས་སོ། །

[Block 1619]
ཁ་ཅིག་གིས་ཀྱང་དེ་ལས་སྐྱེས་པའི་སྔགས་ཀྱི་སྐུ་དང་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱིས་སོ། །

[Block 1620]
གཞན་དག་གིས་ཀྱང་སྣང་བ་ཐོབ་པ་ལ་སོགས་པའི་རྣལ་འབྱོར་གྱིས་ལྷའི་སྐུར་བསྒོམས་པས༌[^1150]སོ། །

[Block 1621]
ལ་ལས་ཀྱང་ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་བསྒོམ་པའི༌[^1151]རིམ་པས་འོད་གསལ་བ་ལ་འཇུག་པས་སོ། །

[Block 1622]
གཞན་ཡང་སྲིད་པ་དང་མྱ་ངན་ལས་འདས་པ་རོ་གཅིག་པ་གཉིས་སུ་མེད་པ་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གྱི་སྒོ་ནས་དེ་ཁོ་ན་ཉིད་སྒོམ་པར༌[^1152]བྱེད་དོ། །

[Block 1623]
དེ་ཁོ་ན་ཉིད་གཅིག་ཡིན་པའི་ཕྱིར་ལམ་གྱི་བྱེ་བྲག་དུ་མ་ལ་སྐྱོན་མེད་དོ། །

[Block 1624]
གཞིའི་བྱེ་བྲག་གི་དབང་གིས་བྱེ་བྲག་ལྟར་སྣང་བ་སྟེ་ཆར་བཞིན་ནོ། །

[Block 1625]
དཔེར་ན་ཆར་པའི་དུས་སུ་ཆུ་འཛིན་གྱི་ཚོགས་ཀྱི་ནང་ནས་འབྱུང་བའི་ཆར་པ་རྨ་བྱས་འཐུང་བ་ན་བདུད་རྩི་ཉིད་དུ་འགྱུར་རོ། །

[Block 1626]
དེ་ཉིད་སྦྲུལ་གྱིས་འཐུང་བ་ན་དུག་ཏུ་འགྱུར་རོ། །

[Block 1627]
བུ་རམ་གྱི་ཤིང་ལ་སོགས་པ༌[^1153]དེ་ཉིད་མངར་བའི་རོ་རུ་འགྱུར་རོ། །

[Block 1628]
ནིམ་པའི་ཤིང་ལ་དེ་ཉིད་ཁ་བའི་རོ་རུ་འགྱུར་རོ་ཞེས་དེ་ཁོ་ན་ཉིད་ལ་དེ་བཞིན་དུ་བྱེ་བྲག་ཏུ་མེད་དོ། །

[Block 1629]
འདི་ལྟར་དཔྱད་པར་བྱ་སྟེ། གལ་ཏེ་དཔལ་གསང་བ་འདུས་པའི་ཕྱོགས་སུ་རིམ་པ་ལྔ་མ་གཏོགས་པར་གཞན་རྫོགས་པའི༌[^1154]རིམ་པ་མེད་པ་ཡིན་ན་དེ་ཅིའི་ཕྱིར་ཕྲ་མོའི་རྣལ་འབྱོར་ལ་སོགས་པ་ཡན་ལག་དྲུག་པའི་རྣལ་འབྱོར་བཅོམ་ལྡན་འདས་ཀྱིས་དེ་དང་དེ་རུ་གསུངས་ཤེ་ན། སྨྲས་པ། [^1155]དེ་དག་གི་ནང་དུ་སོང་བས་རྫོགས་པའི་རིམ་པ་དེ་ལས་གཞན་མེད་དོ། །

[Block 1630]
དེ་ལ་ཕྲ་མོའི་རྣལ་འབྱོར་དང་ཐིག་ལེའི་རྣལ་འབྱོར་དག་ནི་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་ལ་བསྡུས་སོ། །

[Block 1631]
རྩའི་ཀུན་ཏུ་སྤྱོད་པ་དང་དམ་ཚིག་གི་དཀྱིལ་འཁོར་དང་དེའི་ནང་དུ་གསང་བའི་དབང་སེམས་ལ་དམིགས་པ་ཐོབ་པའི་བདག་ཉིད་དོ། །

[Block 1632]
བྱང་ཆུབ་སེམས་འཛིན་པ་ནི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་ལའོ། །

[Block 1633]
དེ་སྟེང་དུ་བཟློག་པ་ནི་དེ་ཉིད་དུ་འདུས་སོ། །

[Block 1634]
སོ་སོར་སྡུད་པ་དང་བསམ་གཏན་དག་ནི་སེམས་རྣམ་པར་དག་པ་ལའོ། །

[Block 1635]
སྲོག་དང་རྩོལ་བ་དག་གིས་རྡོ་རྗེ་བཟླས་པ་མཚོན་པ་དང་། འཛིན་པ་ནི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པས༌[^1156]མཚོན་ནོ། །

[Block 1636]
རྗེས་སུ་དྲན་པས་ནི་བདག་བྱིན་གྱིས༌[^1157]རློབ་པའི་རིམ་པ་མཚོན་པ་དང་། ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པ་ལ་བསྡུས་སོ་ཞེས་རིམ་པ་ལྔའི་བདག་ཉིད་ཁོ་ན་རྫོགས་པའི་རིམ་པའོ། །

[Block 1637]
དེ་ལ་འདི་ལྟར་དཔྱད་པ་ཡིན་ཏེ། ཅི་རིམ་པ་འདི་དག་བཞིའམ་དྲུག་ལ་སོགས་པར་མི་འགྱུར་ཞིང་ལྔ་ཁོ་ནར་བཤད་ཅེ་ན་ཞེས་གྲངས་ལ་ལོག་པར་རྟོག་པ༌[^1158]བསལ་བར༌[^1159]བྱ་བའི་ཕྱིར་སྨྲས་པ། འདིར་ནི་རྣལ་འབྱོར་པས་ཐ་མལ་པའི་ལུས་དང་ངག་དང་ཡིད་རྣམ་པར༌[^1160]བྱ་བ་ཡིན་ཏེ། དེའི་དོན་དུ་བསྐྱེད་པའི་རིམ་པས་ལུས་རྣམ་པར་དག་པ་དང་། རྫོགས་པའི་རིམ་པའི་དང་པོ་རྡོ་རྗེ་བཟླས་པའི༌[^1161]རིམ་པས་ངག་རྣམ་པར་དག་པ་དང་། ཐམས་ཅད་རྣམ་པར་དག་པས་སེམས་རྣམ་པར་དག་པའོ། །

[Block 1638]
ལུས་དང་ངག་དང་ཡིད་རྣམ་པར་དག་པ༌[^1162]ན་སེམས་ཅན་གྱི་དོན་བྱ་བའི་ཕྱིར་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱིས་རང་བྱིན་གྱིས་རློབ་པའོ། །

[Block 1639]
དེ་ལ་མངོན་པར་ཞེན་པ་ཡོངས་སུ་སྤོང་བའི་ཕྱིར་དོན་དམ་པའི་བདེན་པའི་ངོ་བོ་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 1640]
དེ་ལྟར་ན་ཆད་པར་ཐལ་བར་འགྱུར་བས་དེ་ཡོངས་སུ་སྤོང་པའི་ཕྱིར་བདེན་པ་གཉིས་གཉིས་སུ་བྱར་མེད་པའི་མཚན་ཉིད་རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པ་རྡོ་རྗེའི་སྐུ་ཞེས་བྱ་བའི་རྣམ་གྲངས་ཅན་རིན་པོ་ཆེ་སྣ་ཚོགས་ཀྱི་རང་བཞིན་གཞལ་ཡས་ཁང་པའི་ནང་དུ་གནས་པའི་དཀྱིལ་འཁོར་གྱི་བདག་པོ་ཉིད་དུ་བཞུགས་པ། སར་ཞིང་སར་པའི་དཀྱིལ་འཁོར་གྱི༌[^1163]འཁོར་ལོ་སྤྲོས་པས༌[^1164]ནམ་མཁའི་གཏོས་མ་ལུས་པར་ཁྱབ་པ་དུས་ཐམས་ཅད༌[^1165]དུ་སེམས་ཅན་མ་ལུས་པ་སྒྲོལ་བ༌[^1166]ལ་བརྩོན་པ། ཁྱབ་འཇུག་དང་ལྷ་ཆེན་པོ་དང་ཚངས་པ་དང་བརྒྱ་བྱིན་ལ་སོགས་པ་ལྷའི་མཆོག་རྣམས་ཀྱིས༌[^1167]ཞབས་ཀྱི་པདྨ་ལ་ཕྱག་བྱས་པ། ཡིད་བཞིན་ནོར་བུ་དང་དཔག་བསམ་ཤིང་དང་། བུམ་པ་བཟང་པོ་ལྟར་རེ་བ་ཐམས་ཅད་སྐོང་བར་བྱེད་པ་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ལ་དམིགས་ནས་རྣལ་འབྱོར་པས་གནས་པར་བྱའོ། །

[Block 1641]
དེ་བས་ན་ཀུན་ཏུ་འོད་ཀྱི༌[^1168]ས་བཅུ་གཉིས་པ་ལ་གནས་པར་འགྱུར་རོ། །

[Block 1642]
དེའི་འོག་ཏུ་བསླབ་པར་བྱ་བ་མེད་པས་དེ་ཉིད་ས་བཅུ་གསུམ་པར་བཤད་དོ། །

[Block 1643]
ཇི་སྐད་དུ།

[Block 1644 [VERSE]]
ཟུང་འཇུག་ཏིང་འཛིན་ལ་གནས་ནས། །
སླར་ཞིང་གང་ལའང་མི་སློབ་བོ། །

[Block 1645]
ཞེས་འབྱུང་ངོ་། །དེ་ལྟར་རིམ་པ་དེ་དག་གི་རྣལ་འབྱོར་པས་གལ་ཏེ་གང་ལ་ཡང་མི་སློབ་པའི་དབང་གིས་བྱ་བ་བྱས༌[^1169]པ་བྱེད་པ༌[^1170]རྫོགས་པས་རིམ་པ་དྲུག་པ༌[^1171]གང་ཡང་མེད་དོ། །ཞེས་གྲངས་ལྷག་པ་བསལ་ཏོ། །

[Block 1646]
ཉུང་བ་ཡང་མ་ཡིན་ཏེ། ལྔ་མེད་པས་གཞན་དང་རང་གི་དོན་མེད་པའི་ཕྱིར་ཞེས་གྲངས་ལ་ལོག་པར་རྟོག་པ༌[^1172]ཅན་གྱི་ལན་ནོ། །

[Block 1647]
[^1173]

[Block 1648]
འདིར་ཡང་འདི་ལྟར་དཔྱད་པར་བྱ་སྟེ། ཏིང་ངེ་འཛིན་དེ་རྣམས་ཀྱི་ཚད་མ་མངོན་སུམ་མམ་རྗེས་སུ་དཔག་པ་ཡོད་ཅེ་ན། དེ་ལ་རེ་ཞིག་མངོན་སུམ་ནི་མི་འཐད་དེ། རྟོག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1649]
མངོན་སུམ་རྟོག་པ་དང་བྲལ་ཞིང་མ་འཁྲུལ་པ་ཡིན་ཞེས་བཤད་པས་སོ། །

[Block 1650]
རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་བསྒོམ་པའི་རིམ་པས་དེ་ཁོ་ན་ཉིད་ཀྱི་རྣམ་པར་རྟོག་པ་འབྱུང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
