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
[Block 1541 [HEADING]]
###### གླིང། ^1-2-5-17-7-0

[Block 1542]
གླིང་བཞིན་དུ་ཁོ་ར་ཁོར་ཡུག་ཏུ་ཡོངས་སུ་ཆད་པའི་རྣམ་པར་ཆོས་འཆད་པའི་བསམ་པ་ནི་གླིང་ངོ་། །

[Block 1543 [HEADING]]
###### ཡོངས་སུ་འདྲེན་པ། ^1-2-5-17-8-0

[Block 1544]
སེམས་ཅན་རྣམས་ལ་སྙིང་རྗེ་ཆེན་པོས་མྱ་ངན་ལས་འདས་པར་འདྲེན་པའི་ཆོས་འཆད་པའི་བསམ་པ་ནི་ཡོངས་སུ་འདྲེན་པའོ། །

[Block 1545 [HEADING]]
###### རྟེན། ^1-2-5-17-9-0

[Block 1546]
མདོར་ན་འགྲོ་བའི་གནས་བརྒྱད་ཅུ་རྩ་ལྔ་ཉེ་བར་གཟུང༌[^1081]ནས་སོ་སོར་རྟོག་པའི་བསམ་པ་ནི་རྟེན་དུ་འགྱུར་རོ་ཞེས་གཞུང་གི༌[^1082]གོ་རིམས་སོམོ།[^1083] །བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་ཆོས་ཐམས་ཅད་འདྲེ་བ་མ་མཆིས་པ༌[^1084]ལགས་ཞེས་བྱ་བ་ནི་འཁོར་བའི་དུས་ན་ཀུན་བརྟགས་པ་དང་། ཡོངས་སུ་གྲུབ་པ་གཉིས་གང་གི་ཚེ་གཅིག་ཏུ་གྱུར་ཏེ་ཐ་དད་པ་མ་ཡིན་པར་གནས་པ་དེའི་ཚེ་དེ་གཉིས་ཐ་དད་པ་མེད་པར་གནས་པ་ནི༌[^1085]འདྲེས་པ་ཞེས་བྱའོ། །

[Block 1547]
གང་གི་ཚེ་ཆོས་ཀྱི་དབྱིངས་ཤིན་ཏུ་རྣམ་པར་དག་པའི་རྒྱུ་མཐུན་པ་ཉན་པ་དང་བསམ་པ་དང་སྒོམ་པ་ལ་སོགས་པའི་མཐུས་རིམ་གྱིས་གནས་གྱུར་པ་ན། ཡོངས་སུ་གྲུབ་པ་དང་ཀུན་བརྟགས་པ་གཉིས་ཐ་དད་པར་གྱུར་ཅིང་ཤིན་ཏུ་རྣམ་པར་དག་པ་དྲི་མ་མེད་པའི་ངོ་བོ་ཉིད་དུ་གནས་པར་གྱུར་པ་དེའི་ཚེ། འདྲེས་པ་མེད་པ་ཞེས་བྱའོ། །

[Block 1548]
འབྲེལ་པ་མེད་པ་དང་། སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པ༌[^1086]ལ་སོགས་པ་ཡང་དེ་ཉིད་ཀྱི༌[^1087]རྣམ་གྲངས་སུ་གཏོགས་པའོ། །

[Block 1549]
གཟུགས་ཀྱི་ཕ་རོལ་གང་ཡིན་པ་དེ་ནི་གཟུགས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་གཟུགས་ཀྱི་མཚན་ཉིད་སྤངས་པའི་ཕྱིར་གཟུགས་ཀྱི་ཕ་རོལ་དུ་གྱུར་པ་ཡིན་ཏེ། དེ་བས་ན་གཟུགས་ཀྱི་ཕ་རོལ་དུ་གྱུར་པ་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་ཀུན་བརྟགས་པའི་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 1550]
རབ་འབྱོར་གཟུགས་ཇི་ལྟ་བར་ཆོས་ཐམས་ཅད་ཀྱང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ཐམས་ཅད་ཀྱང་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་དེ་སྐད་གསུངས་ཀྱི། མངོན་པར་འབྲེལ་བའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 1551]
བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ་ཉིད་དུ་མི་འགྱུར་ལགས་སམ་ཞེས་བྱ་བ་ནི་ཅི་ལས་དགོངས་ཤེ་ན། གལ་ཏེ་ཆོས་ཐམས་ཅད་གཟུགས་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 1552]
འོ་ན་ནི་གཟུགས་མངོན་པར་རྟོགས་པ་ཉིད་ཀྱིས་ཆོས་ཐམས་ཅད་མངོན་པར་རྟོགས་པར་འགྱུར་ཏེ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་འགྱུར་རོ་ཞེས་དགོངས་པའོ། །

[Block 1553]
བཅོམ་ལྡན་འདས་གཟུགས་ཀྱི་ཕ་རོལ་ན་རྣམ་པར་རྟོག་པ༌[^1088]གང་ཡང་མ་མཆིས་སོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཟུགས་ཀྱི་ཕ་རོལ་དུ་གྱུར་པ་དེ་བཞིན་ཉིད་ལ་གཟུགས་སུ་རྣམ་པར་རྟོག་པར་གྱུར༌[^1089]ན། གཟུགས་ཀྱི་ཕ་རོལ་རྟོགས་པས་ཆོས་ཐམས་ཅད་རྟོགས་པར་མི་འགྱུར་གྱི། གཟུགས་རྟོགས་པ་ཙམ་དུ་ཟད་པར་འགྱུར་བ་ཞིག་ན། འདི་ལྟར་དེ་བཞིན་ཉིད༌[^1090]ཡིན་པས། གཟུགས་ཀྱི་ཕ་རོལ་ལ་གཟུགས་སུ་རྣམ་པར་རྟོག་པ་མེད་དེ། [^1091]དེའི་ཕྱིར་དེ་ཙམ་ཞིག་རྟོགས་པས་ཆོས་ཐམས་ཅད་རྟོག་པར་འགྲུབ་བོ། །

[Block 1554]
གླིང་ལྟ་བུའི་ཆོས་རྣམས་མཐོང་བའི་ཕྱིར་གླིང་ངོ་། །གཟུགས་ནི་སྔོན་གྱི་མཐའ་དང་ཕྱི་མའི་མཐའ་ཡོངས་སུ་ཆད་པའོ་ཞེས་བྱ་བ་ནི་གཟུགས་ནི་སྔོན་གྱི་མཐར་དོན་དམ་པར་ནམ་ཡང་མ་བྱུང་། ཕྱི་མའི་མཐར་ཡང་དོན་དམ་པར་ནམ་ཡང་འབྱུང་བར་འགྱུར་བ་མ་ཡིན་ཏེ། དུས་ཐམས་ཅད་དུ་མེད་པའི་ཕྱིར་རོ། །

[Block 1555]
རབ་འབྱོར་ཆོས་ཐམས་ཅད་གྱི་སྔོན་གྱི་མཐའ་དང་ཕྱི་མའི་མཐའ་ཡོངས་སུ་ཆད་པ་གང་ཡིན་པ་དེ་ནི་ཞི་བའོ། །

[Block 1556]
དེ་ནི་གྱ་ནོམ་པའོ་ཞེས་བྱ་བ་ནི་དུས་སྟོང་པ་ཉིད་ཀྱི་ཕྱིར་ཆོས་ཐམས་ཅད༌[^1092]དམིགས་སུ་མེད་པ་གང་ཡིན་པ་དེ་ནི༌[^1093]དོན་དམ་པ་སྟེ་དེ་རིགས་པའོ༌[^1094]ཞེས་སྟོན་ཏོ། །

[Block 1557]
གཟུགས་ནི་ནམ་མཁའི་ཚུལ་ཅན་ནོ་ཞེས་བྱ་བ་ནི་དོན་དམ་པའི་གཟུགས་ནི་ནམ་མཁའ་བཞིན་དུ་གོས་པ་མེད་ཅིང་འགྱུར་བ་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1558]
གཟུགས་ཀྱི་སྟོང་པ་ཉིད་ནི་འགྲོ་བ་དང་། འོང་བ་མེད་པའོ་ཞེས་བྱ་བ་ནི་གཟུགས་ཀྱི་སྟོང་པ་ཉིད་རྣམ་པར་རྟོག་པ་དང་བཅས་པའི་ཚེ་ཡང་གར་ཡང༌[^1095]མི་འགྲོའོ། །

[Block 1559]
ཕྱིས་རྣམ་པར་མི་རྟོག་པའི་ཚེ་ཡང་གང་ནས་ཀྱང་མ་འོངས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1560]
རབ་འབྱོར་ཆོས་ཐམས་ཅད་ནི་སྟོང་པ་ཉིད་ཀྱི་ཚུལ་ཅན་ཏེ་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1561]
དེ་དག་ནི་ཚུལ་དེ༌[^1096]ལས་མི་འདའོ་ཞེས་བྱ་བ་ནི་ཆོས་དེ་དག་ངོ་བོ་ཉིད་དེ་མི་འདོར་ཞེས་བྱ་བའོ། །

[Block 1562]
སྐྱེ་བ་མེད་པ་དང༌[^1097]དངོས་པོ་མེད་པའི་ཚུལ་ཅན་ནོ་ཞེས་བྱ་བ་ནི་རྒྱུ་དང་རྐྱེན་གྱི་མཐུས་མ་སྐྱེས་ཤིང་མ་བྱུང་བ་དང་། ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བ་མེད་པའི་ཕྱིར་དངོས་པོ་མེད་པའོ། །

[Block 1563]
ཆོས་ཐམས་ཅད་ནི་མཐའ་ཡས༌[^1098]པ་ཞེས་བྱ་བ་ནི་འཇིག་པ་མེད་པའི་ཕྱིར་མཐའ་ཡས་པའོ། །

[Block 1564]
ཚད་མེད་པའི་ཕྱིར་ཀུན་དུ་མཐའ་ཡས་པའོ། །

[Block 1565]
ཡང་ན་རྟག་པ་དང་ཆད་པ་མེད་པའི་ཕྱིར་མཐའ་ཡས་པའོ། །

[Block 1566]
ལུས་མེད་པའི་ཕྱིར་ཀུན་དུ་མཐའ་ཡས་པའོ། །

[Block 1567]
དབྲི་བ་དང་བསྣན་པ་མེད་པའི་ཚུལ་ཅན་ཞེས་བྱ་བ་ནི་ཡོད་པ་ལ་སྐུར་པ་མི༌[^1099]འདེབས་པའི་ཕྱིར་དབྲི་བ་མེད་པའོ། །

[Block 1568]
མེད་པ་ལ་སྒྲོ་མི་འདོགས་པའི་ཕྱིར་བསྣན་པ་མེད་པའོ། །

[Block 1569]
འོང་བ་དང་འགྲོ་བ་མེད་པ་ཞེས་བྱ་བ་ནི་གང་ནས་ཀྱང་མ་འོངས་པའི༌[^1100]ཕྱིར་འོང་བ་མེད་པའོ། །

[Block 1570]
གང་དུ་ཡང་མི་འགྲོ་བའི་ཕྱིར་འགྲོ་བ་མེད་པའོ། །

[Block 1571]
བླང་བ་དང་དོར་བ་མེད་པའི་ཚུལ་ཅན་ཞེས་བྱ་བ་ནི་ལས་ཀྱི་ཚེ་ནི་བླང་བ་མེད་པའོ། །

[Block 1572]
རྣམ་པར་སྨིན་པའི་ཚེ་ནི་དོར་བ་མེད་པའོ། །

[Block 1573]
ཕྲད་པ་མེད་པ་དང་འབྲལ་བ་མེད་པ་དང་། འདྲེ་བ་མེད་པ་དང་། མི་འདྲེ་བ་མེད་པའི་ཚུལ་ཅན་ཞེས་བྱ་བ་ནི་རྣམ་པར་རྟོག་པའི་ཚེ་ཡང་ཀུན་བརྟགས་པ་དེ་བཞིན་ཉིད་དང་ལྷན་ཅིག་ཕྲད་པ་མེད་ལ། རྣམ་པར་མི་རྟོག་པའི་ཚེ་ཡང་ཕྱིས་འབྲལ་བ་མེད་པའོ། །

[Block 1574]
དེ་བཞིན་དུ་འདྲེ་བ་དང་མི་འདྲེ་བ་ཡང་སྦྱར་རོ། །

[Block 1575]
འདོད་ཆགས་བརྩལ་བས་དབེན་པའི་རང་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་ཀྱིས་དབེན་པའི་ཕྱིར། འདོད་ཆགས་ལ་སོགས་པ་བརྩལ་བ་མེད་པ་སྟེ། འདོད་ཆགས་ལ་སོགས་པའི་རྟགས་རྣམས་དང་། འདོད་ཆགས་ལ་སོགས་པ་སྤྱོད་པའི་རྟགས་རྣམས་དང་། འདོད་ཆགས་ལ་སོགས་པའི་རྒྱུ་རྣམས་དང་། འདོད་ཆགས་ལ་སོགས་པའི་དམིགས་པ་རྣམས་དང་། འདོད་ཆགས་དང་འདོད་ཆགས་མེད་པ་ལ་སོགས་པའི་ཆོས་རྣམས་ནི་སེམས་ལས་བྱུང་བ་ཡིན་ཏེ། དེའི་ཕྱིར་གོ་ཆ་དེ་ནི་གཟུགས་དང་འབྲེལ་པ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1576]
གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ཤིན་ཏུ་མེད་པའི་ཕྱིར་ཆོས་དེ་རྣམས་མཚན་མར་བཟུང་སྟེ་གོ་ཆ་འདིས་བགོས་པ་ནི་མ་ཡིན་གྱི། མཚན་མ་མེད་པའི་གོ་ཆ་ཡིན་ནོ་ཞེས་བསྟན་པའོ། །

[Block 1577]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ས་མཚམས་བཅད་དེ་སེམས་ཅན་གྱི་དོན་དུ་གོ་ཆ་བཙལ་བ༌[^1101]མ་ལགས་སོ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་འདི་སྙེད་ཅིག་མྱ་ངན་ལས་འདའ་འོ༌[^1102]ཞེས་བྱ་བར་ཡོངས་སུ་ངེས་པའི་མཚམས་བཅད་པ་གང་ཡང་མེད་དོ། །

[Block 1578]
སུས་ཀྱང་བསྒོམ་པར་མི་བགྱིའོ༌[^1103]ཞེས་བྱ་བ་ནི་བྱེད་པ་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 1579]
གང་དུ་བསྒོམ་པར་མི་བགྱི་ཞེས་བྱ་བ་ནི་ཆོས་གང་ལས༌[^1104]བསྒོམ་པར་བྱ་བ་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1580]
ཇི་ལྟར་ཡང་བསྒོམ་པར་མི་བགྱི་ཞེས་བྱ་བ་ནི་བསྒོམ་པའི་ཡིད་ལ་བྱེད་པ་ཡང་མ་མཐོང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
