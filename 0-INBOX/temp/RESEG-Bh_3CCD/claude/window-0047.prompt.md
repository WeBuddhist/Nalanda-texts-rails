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

[Block 1651]
རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་ལ་ནི་སྔགས་དང་། རླུང་གི་དེ་ཁོ་ན་ཉིད་ཡིད་ལ་བྱེད་པ་ཇི་སྲིད་མ་བྱས་པ་དེ་སྲིད་རྣམ་པ༌[^1174]བཅུ་གཅིག་གིས་རྡོ་རྗེ་བཟླས་པ་ཇི་ལྟར་བསྒོམ། སེམས་ལ་དམིགས་པ་ཐོབ་པ་ལ་ནི་ཡི་གེ་གསུམ་གྱི་བདག་ཉིད་སྔགས་ཆོས་འབྱུང་བའི་འཁོར་ལོའི་ནང་དུ་ཐིག་ལེ་དང་ཚེག་དྲག་གི་ནང་དུ་འཇུག་པ་དང་། ཕྱག་རྒྱ་དང་ལྷན་ཅིག་ཏུ་སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་རྟོགས་པར་བྱེད་དོ། །

[Block 1652]
སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལ་ཡང་སྒྱུ་མའི་དཔེ་བཅུ་གཉིས་ཀྱི་རྣམ་པར་རྟོག་པ་སྐྱེའོ། །

[Block 1653]
མངོན་པར་བྱང་ཆུབ་པའི༌[^1175]རིམ་པ་ལ་ཕྱག་རྒྱ་དང་རྡོ་རྗེ་དང་པདྨ་སྙོམས་པར་ཞུགས་པའི་ཡིད་ལ་བྱེད་པ་དང་། ཆགས་པ་དང་ཆགས་པ་དང་བྲལ་བ༌[^1176]དང་། ཆགས་པ་བར་མའི་རྣམ་པར་རྟོག་པ༌[^1177]ཡིད་ལ་བྱེད་པ་འབྱུང་ངོ་། །ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ལ་ཡང་བདེན་པ་གཉིས་གཉིས་སུ་མེད་པའི་རྟོག་པ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1654]
དེ་ལྟར་རིམ་པ་གཉིས་བསྒོམ་པ་ནི་རྟོག་པ་དང་བཅས་པའི་ཕྱིར་མངོན་སུམ་དུ༌[^1178]མི་སྲིད་དོ། །

[Block 1655]
ངེས་པའི་ཤེས་པས་འགྲུབ་པོ་ཞེ་ན་མ་ཡིན་ཏེ། ངེས་པའི་ཤེས་པ་ནི་རྟོག་པ་མེད་པའི་མངོན་སུམ་ལས་ཕྱིས༌[^1179]འབྱུང་བ་ཡིན་གྱི་དང་པོ་ནི་མ་ཡིན་ནོ། །

[Block 1656]
རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་ནི་རྣམ་པར་རྟོག་པ་ལ་རྟོག་པ་མེད་པའི་མངོན་སུམ་འཇུག་པར་མི་འགྱུར་ཞེས་ཅི་ལ་བརྟེན་ཏེ། ངེས་པའི་ཤེས་པ་འབྱུང་བར་འགྱུར། །རྒྱུན་དུ་གནས་པའི་ཤེས་པ་རྣམས་ཀྱིས༌[^1180]ཚད་མ་ཉིད་མེད་དེ། དོན་གྱི་ཡུལ་ཅན་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1657]
རང་དབང་གི་རྟོག་པ༌[^1181]ཡང་ངེས་པ་མེད་དེ། དེ་ཚད་མ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1658]
ཚད་མ་མེད་པ་ནི་བདེན་པའི་དངོས་པོ་ལ་བརྟེན་ཏེ་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1659]
སློབ་དཔོན་གྱིས་བསྟན་པའི་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པ་རྣམས་རྣ་བའི་དབང་གིས་གཟུང་བར་བྱ་བ་ཡིན་པས་དབང་པོའི་མངོན་སུམ་ངེས་པའི་ཤེས་པ་དང་བཅས་པས་ངེས་པར་འགྱུར༌[^1182]ཞེ་ན། བདེན་མོད་ཀྱི་འོན་ཀྱང་ཉེ་བར་སྟོན་པའི་དུས་སུ་དེ་ཚད་མ་ཉིད་དུ་ངེས་ན་དེ་ཕྱིས་ཀྱི་དུས་སུ་ཇི་ལྟར་ངེས། རྣམ་པར་རྟོག་པས་ཤེ༌[^1183]ན། བདེན་ཏེ་དོན་ལ་བརྟེན་པ་མ་ཡིན་པས་རྟོག་པ་ནི་ཚད་མ་མ་ཡིན་ནོ། །

[Block 1660]
ཡང་ན་སྐྱོན་དེ་བསལ་བར་བྱ་བའི་ཕྱིར་སློབ་དཔོན་གྱིས་བསྟན་པའི་ཕྱིས་ཀྱི་དུས་སུ་དེ་ཉིད་འདི་ཡིན་ནོ་ཞེས༌[^1184]ངོ་ཤེས་པས་ཤེས་པར་བྱེད་དེ༌[^1185]དཔེར་ན་མ་ག་དྷཱའི་འབྲུ་གང་ཡིན་པ་དེ་ཉིད་ཡུལ་འདིའི་ཡིན་ནོ་ཞེས་པ་དང་། གང་མ་ག་དྷཱ་རུ་མཐོང་བ་དེ་འདི་ཉིད་ཡིན་ཞེ་ན། དེ་ལ་སྨྲས་པ། ངོ་ཤེས་པས་ནི་ཚད་མ་མ་ཡིན་ཏེ་སྒྲ་དང་དོན་འགལ་བའི་ཕྱིར་རོ། །

[Block 1661]
དེ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཀྱི་མིང་གི་སྒྲས༌[^1186]འདས་པའི་དུས་སུ༌[^1187]སོ་སོར་རྟོགས་པའོ། །

[Block 1662]
འདི་ཞེས་བྱ་བ་ནི་མངོན་སུམ་གྱི་དངོས་པོ་རྟོགས་པར་བྱེད་པ་ཐམས་ཅད་ཀྱི་མིང་གི་སྒྲའོ། །

[Block 1663]
འདས་པ་དང་ད་ལྟར་བྱུང་བ་དུས་སོ་སོར་བསྟན་པའི་སྒྲ་གཉིས་ཀྱི་གཞི་མཐུན་པ་མེད་པའི་ཕྱིར༌[^1188]ཁྱད་པར་ཅན་གྱི་མཚན་ཉིད་མི་རིགས་སོ། །

[Block 1664]
ཇི་ལྟར་མི་རིགས་ཏེ། རྫས་ཐ་དད་པ་སྟོན་པར་བྱེད་པའི་སྒྲ་དག་གི་དོན་གཅིག་ལ་འཇུག་པ་ནི་གཞི་མཐུན་པའོ། །

[Block 1665]
དེ་ཞེས་བྱ་བའི་སྒྲ་ནི་འདས་པའི་དུས་ཀྱི་ཡུལ་གྱི་རྫས་སྟོན་པར་བྱེད་པ་དང་། འདི་ཞེས་བྱ་བའི་སྒྲས་ཀྱང་ད་ལྟར་བྱུང་བའི་ཡུལ་གྱི་རྫས་སོ་སོར་སྟོན་ཞེས་པ༌[^1189]འདིར་ནི་འདི་དང་དེ་གཉིས་ཀྱི་དེ་ཉིད་འདི་ཡིན་ཞེས་གཞི་མཐུན་པར་རིགས་པ་ཡིན་ནོ་ཞེ་ན། དེ་ལ་སྨྲས་པ། གཞི་མཐུན་པའི་ཐ་སྙད་འདི་བརྟགས་པ་པ་ཡིན་གྱི། དངོས་པོའི་ཡུལ་ཅན་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་གང་འདས་པ་དེའི་འཇིག༌[^1190]པས་དེའི་རྫས་ཇི་ལྟར་རྟོགས། གང་དེ་ལྟར་བྱུང་བ་དེ་ཡང་སྐད་ཅིག་མས་མི་གནས་པའམ་ཆོས་ཅན་ཞེས་འདིའི༌[^1191]སྒྲས་ཇི་ལྟར་བརྗོད་ནུས། བརྗོད་མ་ཐག་ཏུ་འཇིག་པའི་སྒྲ་རྣམས་རང་གི་བདག་ཉིད་ཀྱི་ནུས་པ་ཟད་པའི་ཕྱིར་རོ། །

[Block 1666]
ཇི་ལྟར་དོན་གཅིག་ལ་འདི་ཡིན་ཞེས་ཇི་ལྟར་འཇུག༌[^1192]ཅེས་སྒྲ་འགལ་བའོ། །

[Block 1667]
སྒྲ་དང་དོན་དག་གི་འགལ་བ་ནི་འབྲེལ་པ་མེད་པའི་སྒོ་ནས་སོ་སོར་བསྟན་ཏོ། །

[Block 1668]
བུམ་པ་ལ་སོགས་པའི་སྒྲ་གཅིག་གིས་ཀྱང་གཙོར་འཇུག་པའི་སྒོ་ནས་དངོས་པོ་སོ་སོར་བསྟན་པ་མ་མཐོང་ངོ་། །འདས་པ་དང་མངོན་སུམ་གྱི་དུས་ཀྱི་ཡུལ་ཅན༌[^1193]དག་གི་སྒྲ་གཉིས་ཀྱིས་སོ་སོར་བསྟན་པ་ཅི་མཐོང་ངམ་གཞན་ཡང་དེ་ཉིད་ལ་འདི་ཡིན་ཞེས་འཁྲུལ་པ་ཁོ་ན་ཡིན་གྱི་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 1669]
གང་གི༌[^1194]ཕྱིར་གང་མ་ག་དྷཱ་ལ་སོགས་པའི་ཡུལ་དུ་བ་ལང་དང་། འབྲུ་ལ་སོགས་པ་མཐོང་བ་དང་མྱོང་བ་གང་ཡིན་པ་དེ་དག་གི་གཟུགས་ཀྱི་བྱེ་བྲག་དང་རོ་མཆོག་ལ་སོགས་པ་གཞན་ཡིན་ལ་འདི་དག་གི༌[^1195]ཡང་གཞན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1670]
ཇི་སྐད་དུ།

[Block 1671 [VERSE]]
ཡུལ་ལ་སོགས་པའི་བྱེ་བྲག་གིས། །
རྫས་ཀྱི་ནུས་པ་ཐ་དད་ཡིན། །
དེ་ལ་གཅིག་ནི་མཐོང་བ་ཡིས། །
གཞན་དུ་དེ་དངོས་མཐོང་ངེས་མེད། །

[Block 1672]
ཅེས་འབྱུང་ངོ་། །དཔེར་ན་ལྷོའི་ཕྱོགས་ཀྱི་ཨ་རུ་ར་བདམ་པར༌[^1196]བྱེད་པ་ཡིན་ཏེ། གཞན་དུ་ཁྲུས༌[^1197]སྨན་དུ་འགྱུར་རོ། །

[Block 1673]
ཡུལ་གྱི་བྱེ་བྲག་རེ་ཞིག་འཇོག་ན་དངོས་པོ་ཐམས་ཅད་རང་རང་གི་གཟུགས་སུ་ཡོད་པ་མ་ཡིན་ཏེ་ཞེས་གང་གང་གིས༌[^1198]བརྗོད་ཅིང་འབྲེལ་ལོ། །

[Block 1674]
[^1199]ཇི་སྐད་དུ།

[Block 1675 [VERSE]]
འདུ་བྱེད་ཐམས་ཅད་སྐད་ཅིག་མ། །
མི་གནས་བྱ་བ་ག་ལ་ཡོད། །
གང་ཡོད་དེ༌[^1200]ཉིད་བྱ་བ་སྟེ། །
བྱེད་པ་པོ་ཡང་དེ་ཉིད་བཤད། །

[Block 1676]
ཅེས་འབྱུང་ངོ་། །དེའི་ཕྱིར་དྲན་པའི་ཤེས་པ་ལྟར་ངོ་ཤེས་པ་ཡང་དོན་གྱི་ཡུལ་ཅན་མ་ཡིན་པས་ཚད་མ་མ་ཡིན་ནོ། །

[Block 1677]
རྗེས་སུ་དཔག་པས་ཀྱང་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་རྣམས་ཀྱི་ངེས་པ་མེད་དེ། དེ་ནི་རྟགས་དང་རྟགས་ཅན་གྱི་དངོས་པོའི་འབྲེལ་པའི་སྒོ་ནས་རྟོགས་པ་སྟེ། མེ་དང་དུ་བ་བཞིན་ནོ། །

[Block 1678]
དེ་ལྟ་བུའི་རྟགས་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་རྣམས་ལ་མེད་དོ། །

[Block 1679]
རླུང་གི་དེ་ཁོ་ན་ཉིད་དང་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་མེད་པར་མི་འབྱུང་བའི་རྡོ་རྗེ་བཟླས་པའི་ཤེས་པ་ནི་རང་བཞིན་གྱི་གཏན་ཚིགས་ཀྱིས་ངེས་པར་འཛིན་ཅེ་ན། དེ་ནི་མ་ཡིན་ཏེ། བྱེ་བྲག་ཏུ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 1680]
རླུང་གི་དེ་ཁོ་ན་ཉིད་ནི་ཐིག་ལེ་ཕྲ་མོའི་རྣལ་འབྱོར་རོ། །

[Block 1681]
སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་ཀྱི་ཡི་གེ་གསུམ་མམ་ཡི་གེ་ཨའོ། །

[Block 1682]
རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་ཡང་འཇུག་པ་ལ་སོགས་པའི་བྱ་བའི་གཞི་སྲོག་དང་རྩོལ་བ་དང་མེ་དང་མཉམ་པའི་ངོ་བོ་ཡིན་ཞེས་བྱེ་བྲག་གོ། །

[Block 1683]
དེའི་བདག་ཉིད་ཀྱི་འབྲེལ་པས་ནི་བྱས་པ་དང་། མི་རྟག་པ༌[^1201]དང་ཤིང་དང་ཤ་བ་བཞིན་དབྱེར་མེད་པར་ངེས་པར་བྱེད་པའོ། །

[Block 1684]
མི་དམིགས་པའི་གཏན་ཚིགས་ཀྱིས་ཀྱང་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་ཡང་ངེས་པར་མི་ནུས་ཏེ། དངོས་པོ་མེད་པའི་ཐ་སྙད་དེའི་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1685]
འདིར་ཆོས་ཅན་ཐམས་ཅད་ཀྱི་ཆོས་ཉིད་ཀྱི་ངོ་བོ་དེ་ཁོ་ན་ཉིད་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་གིས་བརྗོད་དུ་མེད་པར་གྲགས་སོ། །
--- END BLOCKS ---
