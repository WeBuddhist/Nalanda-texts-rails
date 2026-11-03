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
[Block 1681]
གང་གི་ཕྱིར་འདི་དག་ཀུན་དུ་འདོད་ཆགས་མ་སྐྱེས་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1682]
ཅི་བྱེད་པ་ཞེས་བྱ་བ་འདི་འདིར་མདོར་བྱས་པ་མ་ཡིན་ཏེ། དེར་རྩོལ་བ་མ་ཡིན་པར་འགྱུར་བ་ལྷག་མ་ཉིད་གང་ཡིན་པ་དེར་ཀུན་དུ་འདོད་ཆགས་སྐྱེས་པ་ལ་ཡང་ལྟུང་བ་སྦོམ་པོ་ཞེས་བྱ་བ་ཀུན་དུ་འདོད་ཆགས་མ་སྐྱེས་པས་ཞེས་བྱ་བའི་རྒྱུའི་ཚིག༌[^1162]ལས་རྩོལ་བ་ཞེས་རྟོགས་པར་བྱའོ། །

[Block 1683]
རྩོལ་བ་འདི་ཉམས་སུ་མ་མྱོང་ན་ཞེས་བྱ་བ་བྱས་ནས་སོ། །

[Block 1684]
ཡན་ལག་གི་རྣམ་པ་རྡོལ་བའི་ཕྱིར་རོ་མ་མྱོང་ནའོ་ཞེས་བྱ་བ་ནི་འཁྲིག་པའི་རོ་ཉམས་སུ་མ་མྱོང་ན་སྦོམ་པོ་སྟེ། འདིར་ཡང་རྩོལ་བ་ཉིད་ན་འདིའོ། །

[Block 1685]
ལས་སུ་མི་རུང་བ་བཅུག་ནའོ་ཞེས་བྱ་བ་ནི་སྦོམ་པོའི་ལྟུང་བ་ཤེས་པའོ། །

[Block 1686]
ལག་པས་ལག་པ་དང་རྐང་པས་རྐང་པ་དང་ཚིགས་ཀྱིས་ཚིགས་སུ་དང་མདོམས༌[^1163]ཀྱིས་མདོམས༌[^1164]སུ་ལྟ་བུར་མི་རུང་ནའོ་ཞེས་བྱ་བ་ནི་ཕྲད་པར་མ་གྱུར་ན་སྦོམ་པོའོ༌[^1165]ཞེས་བྱ་བ་འཇུག་པ་ཡིན་ནོ། །

[Block 1687]
འདིར་ཐམས་ཅད་དུ་རོ་ཉམས་སུ་མ༌[^1166]མྱོང་བ་ལ་རྒྱུ༌[^1167]རིག་པར་བྱའོ། །

[Block 1688]
འདིར་མ་ཕྲད་པ་ནི་ལག་པ་ལ་སོགས་པ་རྣམས་ལ་གཟུང་དུ་མི་རུང་བ་ཉིད་དོ། །

[Block 1689]
ཕྲད་པའི་གཡོ་བ་ཉིད་ཙམ་ལའོ་ཞེས་བྱ་བ་ནི་སྟོབས་ཀྱིས་བརྩལ༌[^1168]བར་འགྱུར་བ་ལ་རྩོལ་བའི་བསྟེན་པར་བྱ་བ་ལ་སྟེན་པར༌[^1169]བྱེད་པ་དང་ཡང་དག་པར་ལྡན་པས་མཐའ་མེད་པར་གནས་པར་བྱེད་ཅིང་འཁྲིག་པའི་རོ་ཉམས་སུ་མྱོང་བ༌[^1170]སྤྲད་པའི་གཡོ་བ་ཉིད་ལ་ནི༌[^1171]དེར་སྦོམ་པོའོ། །

[Block 1690]
ཤིང་དང་བ་སོ་དང་རྡོ་བ་དང་གོས་ལས་བུ་མོའི་གཟུགས་བྱས་པ་ལ་རྩོལ་བ་ན་གལ་ཏེ་དབང་པོ་ཙམ་དོད་ནའོ་ཞེས་བྱ་བ་ལ། འདིར་ཤིང་དང་རྡོ་ལ་སོགས་པའི་མཚན་ཉིད༌[^1172]ནི་དཔེ་ཡིན་ཏེ། གཞན་གྱི་བདག་ཉིད་བུ་མོ་ལ་བརྩལ་བ་ན་ཡང་དབང་པོ་ཙམ་དོད་པ་ལ་སྦོམ་པོ་ཉིད་དོ། །

[Block 1691]
ཡན་ལག་ཐམས་ཅད་དུ་རེག་པ་སྟེར་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་ནི་ཤིང་ལ་སོགས་པའི་རང་བཞིན་གྱི་བུ་མོའི་གཟུགས་ལ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 1692]
བསྟན་པའི༌[^1173]དོན་དུ་བརྩལ་བའི་ཡན་ལག་གི་རྣམ་པར་རྐང་པ་འཇུག་ནའོ་ཞེས་བྱ་བ་བསྟེན་པའི་དོན་དུ་བརྩལ་བས་ཡན་ལག་གི་རྣམ་པར་རྐང་པ་འཛུད༌[^1174]ན་སྦོམ་པོའོ། །

[Block 1693]
བསྟེན་པར་བྱ་བ་ལ་ཡན་ལག་གི་རྣམ་པས་དེ་ཙམ་ལ་གཞོལ་བས་ཕྱི་རོལ་དུ་རེག་ནའོ་ཞེས་བྱ་བ་ནི་བསྟེན་པར་བྱ་བ་མོའི་དབང་པོ་ལ་སོགས་པ་ཡན་ལག་གི་རྣམ་པས༌[^1175]ཕྱི་རོལ་དུ་རེག་པ་ལ་སྦོམ་པོའོ། །

[Block 1694]
དེ་ཙམ་ལ་གཞོལ་བས་ཞེས་བྱ་བ་ནི་རིག་པ་ཙམ་ལ་གཞོལ་བས་རྩོལ་བའི་འདུན་པ་མེད་པས་འདིར་ཉེས་བྱས་སུ་རིགས་ཀྱི་སྦོམ་པོ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་རྣམ་པར་རྟོག་པ༌[^1176]བསལ་བའི༌[^1177]དོན་དུ་འདི་ཡིན་ནོ། །

[Block 1695]
འདི་ལྟ་བུའི་ཆོ་གས་རེག་པ་ལ་སྦོམ་པོ་མེད་ཅེས་བྱ་བ་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1696]
འདིར་གཞུང་ནི། བུད་མེད་སྒྲེན་མོ་ཡོལ་བའི་ཕག༌[^1178]ན་སྣང་བ༌[^1179]ཆུ་ལྡུགས་པ་དེའི་ཡན་ལག་གི་རྣམ་པ་དགེ་སློང་གིས་ཡོལ་བའི་རྒྱབ་ནས་མཐོང་ངོ་། །དེས་མཐོང་ནས་ཀུན་ནས་ཆགས་པས་དེའི་ཡན་ལག་གི་རྣམ་པ་དང་ཡན་ལག་གི་རྣམ་པ་སྤྲད་དོ། །

[Block 1697]
དེ་འགྱོད་པ་སྐྱེས་ནས། ཇི་སྲིད་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 1698]
བསྟན་པའི༌[^1180]ཕྱིར་གཞན་ལ་བསྒོ་ནའོ་ཞེས་བྱ་བ་ནི་འཁྲིག་པའི༌[^1181]དོན་དུ་གཞན་ལ་བསྒོ་ན་སྦོམ་པོའོ། །

[Block 1699]
རང་བཞིན་གྱིས་ལས་སུ་རུང་བ་ཉིད་ལེན༌[^1182]ན་སྨད་པར་བྱ་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་གང་རང་བཞིན་གྱིས་ཏེ། ངོ་བོ་ཉིད་ཁོ་ནས་དུས་ཐམས་ཅད་དུ་དབང་པོ་ལས་སུ་རུང་བ་དེ་ལ་བཅུག་ནན་སྨད་པ་དང་བཅས་པ་ནི་མ་ཡིན་ཏེ། འོན་ཀྱང་དངོས་གཞི་ཉིད་ཅེས༌[^1183]བྱ་བའི་དོན་ཏོ། །

[Block 1700]
མདུན་མ་དང་ཕྱི་མ་གཉིས་གང་དུ་བརྩམས་པ་དེ་ལས་གཞན་དུ་གཏུགས་པ་ལ་མེད་དོ་ཞེས་བྱ་བ་ནི་མདུན་ནས་ལས་བྱས་ཏེ། རྒྱབ་ནས་གྲོལ་བ་དང་། རྒྱབ་ནས་ལས་བྱས་ཏེ་མདུན་ནས་གྲོལ་བ་ནི་ན་སྨད་པར་བྱ་བ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1701]
འདིར་གཞུང་ནི། བཙུན་པ་མདུན་ན་མོར་བསྙུགས༌[^1184]པའི་ལས་བྱས་ཤིང་རྒྱབ་ན་མོར་འདུག་པ༌[^1185]དེ་ལ་ནི་ཁོ་མོ་མི་ཚངས་པར་སྤྱད་ཀྱང་ཡིན་པར་མི་འཛིན་ཏེ་ཞེས་ཟེར་ལ། དེས་མདུན་ན་མོར་བསྙུགས་པའི་ལས་བྱས་ཤིང་། རྒྱབ་ན༌[^1186]མོར་འདུག༌[^1187]གོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1702]
དེ་ལ་འདྲ་བ་ཉིད་ཀྱི་བཟློག་པ་ལ་རྒྱུད་མེད་པ་དང་སྔགས་ཀྱི་ཁྱད་པར་ནི་གཞན་ཉིད་ཙམ་དེར་ཞེས་བྱ་བ་འདི་ལྟར་ཉེ་བར་འབྲེལ་པའོ། །

[Block 1703]
ལམ་ལྷག་མ་རྣམས་སུ་བརྩལ་བར་བྱའོ་སྙམ་པ་ལ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་ཟག་བྱེད་དང་ཁ་དང་བཤང་བའི་ལམ་རྣམས་གཅིག་ཏུ་དང་པོར་མི་ཚངས་པར་སྤྱོད་པ་བརྩམས་པ་ལ༌[^1188]ལམ་ལྷག་མ་རྣམས་སུ་བསྩལ་བར༌[^1189]བྱའོ་སྙམ་པའི་བསམ་པ་སྟེ། ན་སྨད་པའི་རྒྱུ་མཚན་དུ་ནི་མ༌[^1190]ཡིན་ནོ། །

[Block 1704]
བདག་ནི་ཉམས་པའོ་སྙམ་པའི་བསམ་པ་ཅན་ལ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་བདག་ནི་ཉམས་པ་སྟེ་དགེ་སློང་གི་ཚུལ་ཞིག་པའོ་སྙམ་པའི་བསམ་པ་ཅན་གྱིས་བཅུག་པ་ལ་ཡང་ན་སྨད་པར་བྱ་བ་མེད་པའོ། །

[Block 1705]
ནད་དང་བྲལ་བར་བྱ་བའི་དོན་ཉིད་ལ་ཡང་མེད་དོ། །

[Block 1706]
ལམ་ལ་གཞན་ཉིད༌[^1191]དུ་འདུ་ཤེས་པ་དང་ཡིད་གཉིས་ཟ་བ་ལ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་མོའི་དབང་པོ་ལ་སོགས་པ་ལ་ལམ་མ་ཡིན་པ་ཉིད་དུ་ཡང་དག་པར་ཤེས་པ་གང་ཡིན་པ་དང་། གང་ལམ་ལ་ཡིད་གཉིས་ཟ་བ་ཅི་འདི་ཟག་བྱེད་ལ་སོགས་པའི་ལམ་མ་ཡིན་ནམ་འོན་ཏེ་ཡིན་སྙམ་དུ་ཡིད་གཉིས་ཟ་བས་བཅུག་ན་དེ་གཉིས་ཀ་ལ་ཡང་ན་སྨད་པར་བྱ་བ་མེད་དོ། །

[Block 1707]
ལམ་མ་ཡིན་པ་ནི་དེ་གཉིས་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལམ་མ་ཡིན་པ་ལ་ལམ་དུ་འདུ་ཤེས་པ་ཉིད་དང་། ལམ་མ་ཡིན་པ་ལ་ཡིད་གཉིས་ཟ་བས་བཅུག་པ་ལ་སྦོམ་པོའོ།[^1192] །འདིར་གཞུང་ནི་ལམ་ལ་ལམ་མ་ཡིན་པ་ཉིད་དུ་འདུ་ཤེས་པ་ལ་ནི་ཕམ་པར་འགྱུར་བའི་ལྟུང་བའོ། །

[Block 1708]
ལམ་ལ་ཡིད་གཉིས་ཟ་བ་ལ་ཡང་ཕམ་པར་འགྱུར་བའི་ལྟུང་བའོ། །

[Block 1709]
ལམ་མ་ཡིན་པ་ལ་ལམ་དུ་འདུ་ཤེས་པ་ལ་ནི་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 1710]
ལམ་མ་ཡིན་པ་ལ་ཡིད་གཉིས་ཟ་བ་ལ་ལང༌[^1193]ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1711]
འདིར༌[^1194]ནི་ལམ་གསུམ་ཡིན་ཏེ། བཤང་བའི་ལམ་དང་། ཁའི་ལམ་དང་། ཟག་བྱེད་དོ༌[^1195]ཞེས་བྱ་བའོ། །

[Block 1712]
བརྡོས༌[^1196]པས་བུད་མེད་ཀྱི་སྟེང་དུ་འགྱེལ་བ་ལ༌[^1197]ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་བ་གླང༌[^1198]ལ་སོགས་པས་བརྡོས༌[^1199]པའི་དགེ་སློང་བུད་མེད་ཀྱི་སྟེང་དུ་འགྱེལ་བ་ལ་རྒྱུ་དེས་རེག་པ་ལ་སྐྱོན་མེད་དོ་ཞེས་བྱ་བ་འདི་ཙམ་འདིར་བརྗོད་པ་ཡིན་ཏེ། །དེ་བས་ན་མ་བསྡུས༌[^1200]པས་གང་ཞིག་རེག་པ་ཉམས་སུ་མྱོང་བར་བྱ་བ་མི་བྱེད་ན་དེ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་ཤེས་པར་བྱའོ། །

[Block 1713]
ཉམ༌[^1201]ཐག་པས་མགུལ་ནས་མི་འདོད་བཞིན་དུ་འཁྱུད་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བླངས་པ་མེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1714]
མཆུར་མཆུས་རེག་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མི་འདོད་པ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 1715]
ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ཡང་མི་འདོད་བཞིན་དུ་རག་པ་ཡིན་གྱི། འདིར་ཆགས་པ་སྐྱེས་པ་ལ་མངོན་པར་ཚར་གཅོད་པ་ལ་སེམས་ལ་འབད་པ་མི་བྱེད་ཅིང་རོ་མྱོང་བ་སྒྲུབ་པ༌[^1202]ལ་གལ་ཏེ་སྐབས་སུ་གཡོ་བ་དང་སྤྲད་པ་ནི་དགེ་འདུན་ལྷག་མར་གཏོགས་པའི་ལྟུང་བ་སྦོམ་པོ་དེར་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 1716]
ཁྱིའི་མདུན་དུ་གཅི་བར་མི་བྱའོ། །

[Block 1717]
གང་དུ་སྲོག་གི་བར་ཆད་འབྱུང་བའི་དགོན་པ་དེར་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། མིའམ་ཅི་མོའི་དབང་བའི༌[^1203]གླེང་གཞིར་གྱུར་པའི་བསླབ་པའི་གཞི་ལ་དེ་བསྡུ་བ་ཡིན་ནོ། །

[Block 1718]
འདིར་གཞུང་ནི། ཡང་དགེ་སློང་གིས་གང་ན་ཉེས་དམིགས་དེ་ལྟ་བུ་ཡོད་པའི་དགོན་པ་དེ་ལྟ་བུར་ལྷག་པར་གནས་པར་མི་བྱ་སྟེ། གང་ན་འདི་ལྟ་བུའི་འཇིགས་པའི་ངོ་བོ་ཡོད་པར་གྱུར་པའི་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1719]
གང་ན་ཡན་ལག་གི་རྣམ་པ་འཛིན་པའི་འཇིགས་པ་ཡོད་པའི་ཆུ་ཀླུང་དེར་སྒྲེན་མོར་རྒལ་བར༌[^1204]མི་བྱའོ། །

[Block 1720]
དེར་ཤེས་བཞིན་དུ་གྲུ་རྒལ་བར༌[^1205]བྱའོ་ཞེས་བྱ་བ་ནི་བུད་མེད་ལ་རེག་པ་ཡོངས་སུ་སྤང་བའི་ཕྱིར་ཤེས་བཞིན་དུ་འགྲོ་བར༌[^1206]བྱ་བ་ཡིན་པར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
