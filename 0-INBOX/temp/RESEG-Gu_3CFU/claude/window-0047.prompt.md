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
འབྲེལ་པ་ཙམ་ལ་འདིར་ཕམ་པ་ཞེས་བྱ་བ་སྦུབས་ཀྱི་སྒྲས་ཤེས་པར་བྱའོ། །

[Block 1647]
ཀློག་པ་འབའ་ཞིག་ཏུ་འདི་བརྗོད་དེ་མ་ནིང་ལ་རྩོལ་བར་བྱེད་དེ་གང་དུ་གླགས་མེད་པ་ལ་ལྟུང་བར་འགྱུར་བ་མཆིས་སམ། སྦོམ་པོའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་བསྡུས༌[^1133]པའོ། །

[Block 1648]
མཆུ་གཉིས་ལའོ་ཞེས་བྱ་བ་ནི་མཆུ་གཉིས་ལ་སྦྱར་བ་ཙམ་ལ་ཡང་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་དེ། [^1134]སོའི་མཐའ་ཚུན་ཆད་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་ཇི་སྲིད་དུ་བསྩལ་བ༌[^1135]ཞེས་བྱ་བ་སྔོན་གྱི་རྗེས་སུ་འབྲང་བས་རྟོགས་པར་བྱའོ། །

[Block 1649]
ཕྱི་རོལ་གྱི་མཚམས་ལ་ཐུག་པར་རོ་ཞེས་བྱ་བ་ཁའི་དང་པོ་ནི་སོ་ཕན་ཆད་དོ་ཞེས་བསྟན་པ་ལ་ཕྱི་རོལ་དུ་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་དོ། །

[Block 1650]
འདིར་གཞུང་ནི། སོའི་ཕྱི་རོལ་དུ་ཉམས་པར་བྱེད་ན་ཉེས་པ་སྦོམ་པོའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1651]
སྣོད་དུའོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་ཡོངས་སུ་མ༌[^1136]ཟིན་པའི་ཕྱིར་གང་ཞིག་སྣོད་དེའི་རང་བཞིན་དུ་འཇུག་པ་ན་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་དོ། །

[Block 1652]
བལྟབས་པ༌[^1137]དང་མི་རིག་པར་འཇུག་པ་གཉིས་སོ་ཞེས་བྱ་བ་ནི་ཕོའི་དབང་པོ་རྐེད་བལྟབ་ཏུ་བྱས་ཏེ་རྨའི་སྒོ་རྣམས་སུ་འཇུག་པ་གང་ཡིན་པ་དང་། གང་ཡང་མི་རེག་པར་གྱུར་པའི་རྨའི་སྒོ་དེ་དགེ་སློང་ལ་ཡང་ལྟུང་བར་འགྱུར་བ་བཞིན་དུ་དགེ་སློང་མ་ལ་ཡང་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་ཡིན་ནོ། །

[Block 1653]
གལ་ཏེ་མི་རེག་པར་འཇུག་པ་ལ་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་ཡིན་ན་གང་ཞིག་འདི་དག་བསྟེན་པར་བྱ་བ་གཡོགས་མ་ཅན་ཉིད་དག་ལས་ནི་ན་སྨད་པ་མེད་པར་བརྗོད་དོ། །

[Block 1654]
གཡོགས་མས་བར་དུ་མ་ཆོད་པ་ཞེས་བྱ་བ་དེ་ཇི་ལྟར་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མཐའ་ཉིད་བརྗོད་པའི་གཡོགས་པ་དེ་ནི་བསྒྲིབས་པ་སྟེ། དེས་གཡོགས་པ་ལ་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་དུ་རེག་པར་མི་འགྱུར་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཐ་མ་ན་ཡོད་པའི་ཕམ་པར་འགྱུར་བ་ལ་ན་སྨད་པ་མེད་པའི་ཚིག་གིས་བརྗོད་པ་ལ་འདི་ལྟ་བུའི་གཡོགས་པ་ནི་གཡོགས་པ་དང་བཅས་པ་དེ་ནི་བསྒྲིབས་པ་ནི་འདོད་པའོ། །

[Block 1655]
གང་ཞིག་བར་དུ་ཆད་པས་གཡོགས་མས་བསྒྲིབས་པ་དེ་ལ་ནི་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་དུ་རེག་པར་མི་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 1656]
འོ་ན་ཅི་ཞེ་ན། དེ་ལ་རེག་པ་ཡོད་པ་ཁོ་ནའོ། །

[Block 1657]
གཞན་གྱིས་གཡོགས་པ་ཉིད་ནི་མི་རེག་པར༌[^1138]འཇུག་པས་རྣམ་པར་བགད་པ༌[^1139]ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གཞན་གྱིས་ཞེས་བྱ་བ་ནི་གང་གིས༌[^1140]གཡོགས་པ་དེ་ལ་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་དུ་རེག་པར་མི་འགྱུར་བ་ནི་པགས་པ་མཐུག་པའམ། འཇམ་པོས་སམ་གོས་ཀྱིས་རེག་པས༌[^1141]འཇུག་པ་ལ་དེ་རྣམ་པར་བཤད་པ་ཡིན་ཏེ། འདི་ལས་ལྷག་པ་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ།[^1142] །ཕམ་པར་འགྱུར་བ་དང་པོ་ཞུ་བའི་སྐབས་སོ་ཞེས་བྱ་བ་མི་ཚངས་པར་སྤྱོད་པའི་ཕམ་པར་འགྱུར་བ་ཞུ་བའི་སྐབས་རྫོགས་སོ།། །།

[Block 1658]
དགེ་སློང་གི་དངོས་པོར་མི་ཤེས་པ་ནི་རང་བཞིན་གྱིས་ཉམས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རང་བཞིན་གྱིས་ཉམས་པ་ཞེས་བྱ་བའི་སྒྲ་དེའི་དོན་རྒྱས་པར་གྱུར་པས་ཐ་སྙད་ཉམས་པ་ཞེས་བྱ་བའི་སྒྲ་རང་བཞིན་ཉམས་པ་སྨྱོན་པ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་ཀྱིས་བརྗོད་པ་ལ་ལྟུང་བ་མ་བླངས་པས༌[^1143]ཡོངས་སུ་མ་བཅད་པ་ལ་ངོ་བོ་འདི་ཡིན་ནོ་ཞེས་བྱ་བ་རབ་ཏུ་བསྟན་པའི་དོན་དུ་མདོ་འདི་ཡིན་ནོ། །

[Block 1659]
འདིར་གཞུང་ནི། གལ་ཏེ་དགེ་སློང་གི་དངོས་པོར་ཡང་དག་པར་ཤེས་ན་ནི་གཞི་ཇི་ལྟ་བ་བཞིན་དུ་ལྟུང་བར་འགྱུར་རོ། །

[Block 1660]
གལ་ཏེ་དགེ་སློང་གི་དངོས་པོར༌[^1144]མི་ཤེས་པ་སྨྱོན་པ་ལ་ནི་ལྟུང་བར་མི་འགྱུར་ཏེ། སེམས་འཁྲུགས་པ་དང་ཚོར་བས་ཉེན་པ་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1661]
ཉམས་པ་ཉིད་ནི་གཉིས་ཏེ། ནང་དང་ཕྱི་རོལ་ལོ་ཞེས་བྱ་བ་ནི་འདིར་ནང་གི་རིམ་པ་རྟོགས་པ་ཉམས་པ་ཉིད་ལ་དོན་དང་ལྡན་པ་ཉིད་དེ། དེ་བས་ན་ནང་གི་རིམ་པ་ནས་བརྩམས་ཏེ། ཇི་སྲིད་དུ་ཕྱི་རོལ་ཉམས་པའི་བར་དེ་ནི་འདིར༌[^1145]ཕྱི་རོལ་ཉམས་པ་ཉིད་ཡིན་གྱི་ཕྱི་རོལ་ཉམས་པ་འབའ་ཞིག་ནི་ཉམས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1662]
བསྟན་པའི་ཕྱིར་གཞན༌[^1146]ལ་ཁས་བླངས་པ་ན་བསླབ་པ༌[^1147]འཁྲུགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དགེ་སློབ༌[^1148]མ་གང་གི་མིང་དེ་ནི་བསླབ་པར་འདོད་པའོ། །

[Block 1663]
དེ་ལྟར་ན་དགེ་སློབ༌[^1149]མ་ལ་གནས་པའི་ཆོ་ག་འདིར་རྟོགས་པར་བྱའོ། །

[Block 1664]
དགེ་སློབ་མ་གང་ཞིག་བསྟེན་པའི་ཕྱིར་གཞན་སྐྱེས་པ་འདོད་པ་བསྟེན་ནུས་པ་ལ་འདི་ལྟར་ཞེས་བྱ་བར་ཁས་ལེན་པར་བྱེད་པ་དེ་ལ་དགེ་སློབ་མ་དེའི་བསླབ༌[^1150]པའི་གཞི་རྣམས་འཁྲུགས་པ་ཉིད་དེ་མེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1665]
འདིར་གཞུང་ནི། དགོན་པ་པ་སྡིག་ཅན་གྱིས་དགེ་སློབ་མ་ལ་ཁྱོད་བསྙེན་པར་མ་རྫོགས་ཀྱིས་མི་ཚངས་པར་སྤྱོད་ཀྱང་ལྟུང་བར་མི་འགྱུར་རོ་ཞེས་ཅོ་འདྲི་སྟེ་དེས་དེ་བསྟེན་པ་དང་བསྟེན་པ་དེ་ལ་འགྱོད་པ་སྐྱེས་སོ། །

[Block 1666]
དེས་དེ་མི་འདོད་བཞིན་དུ་བརྩལ་བ་དང་། དེ་བདག་དགེ་སློབ་མར་མ་རུང་བར་མ་གྱུར་ཏམ་སྙམ་དུ་འགྱོད་པ་སྐྱེས་སོ། །

[Block 1667]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བསླབ་པ་འཁྲུགས་པས་ཡང་དཔོག་པར་བྱ་སྟེ། ཉེས་བྱས་གྱི༌[^1151]ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1668]
ཕྱིར་བླང་བ་མ་ཡིན་པ་ཉིད་ལ་བརྩལ་བ་ལ་ངེས་པར་མི་འདོད༌[^1152]པའོ། །

[Block 1669]
འདི་ནི་སྐྱོན་མེད་པར་ཤེས་ནས་ཁས་བླངས་ནས་ཆོ་ག་འདི་ཤེས་པ་ཡིན་ནོ། །

[Block 1670]
དེ་ལ་དེ་ཡང་སྦྱིན་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་དགེ་སློབ་མའི་བསླབ་པའོ། །

[Block 1671]
འདིར་ཉམས་པ་ཉིད་སླར་སྦྱིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1672]
དེ་ནི་དགེ་སློང་གི་སྦོམ་པོའོ༌[^1153]ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ༌[^1154]ནི་བསྟེན་པའི༌[^1155]ཕྱིར་གཞན་ལ་ཁས་བླངས་པ་ནི་དགེ་སློང་ལ་སྦོམ་པོའི་ལྟུང་བྱེད་ཅེས་བྱ་བའོ། །

[Block 1673]
འདི་མན་ཆད་འོག་ནས་མདོ་ལས་བསྟན་པའི༌[^1156]ཕྱིར་གཞན་ལ་བསྒོ་ན་ཞེས་བྱ་བ་ཡན་ཆད་ནི་སྦོམ་པོའི་དབང་དུ་བྱས་པར་རིག་པར་བྱའོ། །

[Block 1674]
འདིར་ཡང་གཞུང་ནི། དགོན་པ་པ་སྡིག་ཅན་གྱིས་ལོར་མ་ལོན་པ༌[^1157]ལ་ཁྱོད་བསྙེན་པར་རྫོགས་ནས་རིང་པོར་མ་ལོན་གྱིས་མི་ཚངས་པར་སྤྱད་ཀྱང་དེས་ལྟུང་བར་མི་འགྱུར་རོ་ཞེས་ཅོ་དྲིས་ཏེ། དེས་དེ་བསྟེན་པ་དང་བསྟེན་པ་དེ་ལ་འགྱོད་པ་སྐྱེས་སོ། །

[Block 1675]
དེས་དེ་མི་འདོད་བཞིན་དུ་བརྩལ་བ་དང་། དེ་བདག་ཕམ་པར་མ་གྱུར་ཏམ་སྙམ་དུ་འགྱོད་པ་སྐྱེས་སོ། །

[Block 1676]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཕམ་པའི་ལྟུང་བར་མི་འགྱུར་ཏེ། ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བའོ། །

[Block 1677]
འདིར་ཡང་ངེས་པར་ཁས་བླངས་པ་ལ་སྦོམ་པོའི་ལྟུང་བར་འགྱུར་བ་སྟེ། བླང་བ་མ་ཡིན་པ་ཉིད་ལ་བསྩལ་བ༌[^1158]ལ་ངེས་པར་མི༌[^1159]འདོན་པ་ལས༌[^1160]འདིར་བཟུང་བ་ཡོད་ལ་ཕམ་པར་འགྱུར་བ་ཡོད་པས་མེད་པ་ལ་སྐྱོན་མེད་པ་ཉིད་ལའོ། །

[Block 1678]
མ་ཆུད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བསྟེན་པར་བྱ་བ༌[^1161]སྦོམ་པོ་སྟེ། སྟེན་པར་བྱེད་པ་ལ་རུང་བ་མ་ཆུད་པ་ནི་མི་མཉམ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1679]
ཆུད་པར་བྱ་བའི་ཕྱིར་རྨ་ཉེད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཟག་བྱེད་དུ་ཆུད་པར་བྱའོ་སྙམ་ནས་དེའི་ཆེད་དུ་རྨའི་སྒོ་སྦལ་བར་བྱེད་ན་ཡང་སྦོམ་པོའོ། །

[Block 1680]
སྐྲག་པ་དང་ངོ་ཚ་བས་ཀུན་དུ་འདོད་ཆགས་མ་སྐྱེས་ནའོ་ཞེས་བྱ་བ་ནི་སྐྲག་པ་དང་ངོ་ཚ་བ་ཡོད་པ་ལ་སྦོམ་པོར་འགྱུར་རོ། །

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
--- END BLOCKS ---
