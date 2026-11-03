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
གཞན་ཡང་དོན་རྣམ་པ་གསུམ་གྱིས་དགའ་བ་ཐོབ་པོ། །སངས་རྒྱས་ལས་ཐོས་ནས་སེམས་རབ་ཏུ་བདེ་ཞིང་བདུད་མ་ཡིན་པར་རྟོགས་པ༌[^1430]དགའ་བ་དང་། ཡང་དག་པ་གཅིག་ཐོབ་པས༌[^1431]སྔ་མ་གསུམ་པོ་ཐབས་ཙམ་དུ་བསྟན་པར་ཤེས་པས་དགའ་བ་དང་། སངས་རྒྱས་ཀྱིས༌[^1432]དགྲ་བཅོམ་པ་བརྒྱ་ཕྲག་ཕྱེད་དང་བཅུ་གསུམ་ཡང་སངས་རྒྱས་སུ་ལུང་བསྟན་པ་ཐོས་པས་དགའ་བ་ཐོབ་པས།[^1433]

[Block 1682 [HEADING]]
###### **ཅིའི་ཕྱིར་དགའ་བ།** ^4-3-4-1-1-2-0

[Block 1683]
མདོ་ལས་དེ་ཅིའི་སླད་དུ་ཞེས་པ་ནས་ཡོངས་སུ་གདུང་བར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ནི་ཅིའི་ཕྱིར་དགའ་བ་བསྟན་ཏེ། དེ་ལ་ཡང་རྣམ་པ་བཞིའོ། །

[Block 1684]
ཆོས་ཆེན་པོ་ལས་ཉམས་པས་གདུང་བར་གྱུར་པ་དང་། ཐེག་པ་ཆུང་ངུས་བཏོན་པས༌[^1434]འགྱོད་པ་དང་། ཐོས་པས༌[^1435]མྱ་ངན་ཟད་པས་དགའ་བ་དང་སངས་རྒྱས་ཀྱི་སྲས་རྣམས་བྱང་ཆུབ་ཐོབ་པར་རྟོགས་པའོ། །

[Block 1685 [HEADING]]
###### **ཆོས་ཆེན་པོ་ཉམས་པས་གདུང་བར་གྱུར་པ།** ^4-3-4-1-1-2-1-0

[Block 1686]
འདི་ནི་ཆོས་ཆེན་པོ་ཉམས་པས་གདུང་བར་གྱུར་པ་བསྟན་པ་སྟེ། བདག་ཅག་གིས་སྔོན་བྱང་ཆུབ་སེམས་དཔའ་ལ་ལུང་བསྟན་པ་ཐོས་ཀྱང་ལུང་བསྟན་པ་མ་ཐོབ་པོ་སྙམ་ནས་གདུང་བར་གྱུར་པ་དང་། དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་དང་གཟིགས་པ་ལས་ཉམས་པས་གདུང་བར་གྱུར་ཏོ། །

[Block 1687 [HEADING]]
###### **ཐེག་པ་ཆུང་ངུས་བཏོན་པས་འགྱོད་པ།** ^4-3-4-1-1-2-2-0

[Block 1688]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་ཤེ་དག༌[^1436]གིས་སྤྱོད་དོ་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆུང་ངུས་བཏོན་པས༌[^1437]འགྱོད་པ༌[^1438]བསྟན་པ་སྟེ།

[Block 1689 [VERSE]]
འདི་ལ་ཡང་རྣམ་པ་གཉིས་སོ། །
ཆུང་ངུས་གནས་པས་འགྱོད་པ་དང་།
ལོག་པར་གྱུར་པས་འགྱོད་པའོ། །

[Block 1690]
ཆོས་ཀྱི་དབྱིངས་ནི་གང་ཟག་ལ་བདག་མེད་པ༌[^1439]ཡང་དག་པ་ཉིད་དེ། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་དང་བདག་ཅག་ཞུགས་པར་མཚུངས་ན་ཅིའི་སླད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་བདག་ཅག་ཐེག་པ་ཆུང་ངུས་བཏོན་སྙམ་དུ༌[^1440]འགྱོད་དོ། །

[Block 1691]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་དེ་སྙམ་དུ་སེམས་སོ་ཞེས་པའི་བར་དུ་ནི་འདིར་བདག་འགྱོད་པ་བསྟན་ཏེ། ནོངས་ཞེས་བྱ་བ་ནི་སྡིག་པ་ལ་བྱའོ།[^1441] །མདོ་ལས་ཅིའི་སླད་དུ་ཞེས་པ་ནས་བཏོན༌[^1442]པར་འགྱུར་ཞིག་ན་ཞེས་པའི་བར་དུ་ནི་ཅིའི་ཕྱིར་ཞེས་བྱ་བ་བསྟན་ཏེ། དེ་ཡང་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་བརྩམས་པའི་རྒྱུ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་མངོན་པར་ཤེས་པ་དང་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པའོ། །

[Block 1692]
བསྡད་པ་ནི་རེ་བའི་དོན་ཏེ་དེ་བས་ན་བདག་ཅག་གིས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་རྒྱུར་གྱུར་པ༌[^1443]རེ་བའི་སེམས་ཀྱིས་བསྡད་ན་ནི་ཐེག་པ་ཆེན་པོའི་ཆོས་ལ་བཏོན་པར༌[^1444]འགྱུར་བ་ཞིག་ན༌[^1445]བདག་ཅག་ལ་རེ་བ་མེད་པས་ན་ཐེག་པ་ཆེན་པོ་ལ་དགོད་པར་མ་གྱུར་ཏོ་སྙམ་དུ༌[^1446]འགྱོད་དོ། །

[Block 1693]
བྱང་ཆུབ་ཀྱི་སེམས་ལ་རྣམ་པ་གསུམ་སྟེ།[^1447] འདུས་བྱས་ལས་སྐྱེ་བ་དང་། བྱང་ཆུབ་ཚོལ་བ་དང་སེམས་ཅན་ལ་ཤིན་ཏུ་དགོངས་པའོ། །

[Block 1694]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་དགྲ་བཅོམ་པ་ཐོབ་པོ་ཞེས་པའི་བར་དུ་ནི་ཤིན་ཏུ་འགྱོད་པ་བསྟན་ཏེ། [^1448]བཅོམ་ལྡན་འདས་ཀྱིས་ལྡེམ་པོ་ངག་ཏུ་གསུངས་པ་ན་མ་རིག་པ༌[^1449]ནས་ཐབས་ཙམ་དུ་བསྟན་པ་ཐོས་མ་ཐག་ཏུ་གཟུང་བ་དང་། བསྒོམས་པ་དང་། བསམས་པ་དང་། ཡིད་ལ་བྱས་པས་ཐེག་པ་ཆེན་པོ་ལ་མ་བཀོད་པ་ནི་བདག་ཅག་གིས་ནོངས་སོ་སྙམ་དུ༌[^1450]འགྱོད་པར་གྱུར་ཏོ། །

[Block 1695 [HEADING]]
###### **ཐོས་ནས་མྱ་ངན་ཟད་པས་དགའ་བ།** ^4-3-4-1-1-2-3-0

[Block 1696]
དེ་ལ་ཐོས་ནས་མྱ་ངན་ཟད་པས་དགའ་བ་ནི་སྔོན་ཐེག་པ་ཆེན་པོའི་རྣམ་པར་གྲོལ་བ་ལ་སྐལ་བ་མེད་སྙམ་དུ་འཛིན་ཏེ། དེ་བཅོམ་ལྡན་འདས་ལ༌[^1451]ཐེག་པ་ཆུང་ངུ་གཉིས་ངེས་པའི་དོན་མ་ཡིན་ཏེ། སངས་རྒྱས་ཀྱི་བྱང་ཆུབ་ལ་སྐལ་བ་ཡོད་པར་རྟོགས་པས་མྱ་ངན་ཟད་ནས་དགའ་བ་དང་བསིལ་བ་ཐོབ་པར༌[^1452]གྱུར་ཏོ། །

[Block 1697]
དེ་ལྟར་ཐེ་ཚོམ་མེད་པས་བདེ་བ་དང་བསིལ་བར་གྱུར་ཏོ། །

[Block 1698 [HEADING]]
###### **སངས་རྒྱས་ཀྱི་སྲས་རྣམས་བྱང་ཆུབ་ཐོབ་པར་རྟོགས་པ།** ^4-3-4-1-1-2-4-0

[Block 1699]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཀྱི་སྲས་ཐུ་བོ་ཞེས་པ་ནས་ཡོངས་སུ་གདུང་བ་དང་བྲལ་ལོ་ཞེས་པའི་བར་དུ་ནི་སངས་རྒྱས་ཀྱི་སྲས་རྣམས་བྱང་ཆུབ་ཐོབ་པར་རྟོགས་པ་བསྟན་པ་སྟེ། འཕགས་པའི་ཡེ་ཤེས་ཐོབ་ཅིང་སངས་རྒྱས་ཀྱི་ཐུགས་ལས་བྱུང་བས་སྲས་ཐུ་བོའོ། །

[Block 1700]
སོ་སོའི་སྐྱེ་བོ་ལས་གཞན་པ་ནི་ཐུགས་ལས་བྱུང་བའོ། །

[Block 1701]
ཆོས་ཀྱི་གསུང་རབ་ལས་བྱུང་བས་ཞལ་ནས་སྐྱེས་པའོ། །

[Block 1702]
ཆོས་ཀྱི་རྗེས་སུ་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་ནི་ཆོས་ལས་སྐྱེས་པའོ། །

[Block 1703]
ཆོས་ཀྱི་སྐུའི་རྗེས་སུ་དེ་དང་འདྲ་བའི་ཆོས་ཐོབ་པ་ནི་ཆོས་ཀྱི་སྤྲུལ་པའོ། །

[Block 1704]
ཆོས་ཀྱི་ཉེ་མཚམས་ཆོས་ཀྱིས་གྲུབ་པ་ནི་ཟག་པ་མེད་པའི་ཆོས་རིན་པོ་ཆེ་ལ་ལོངས་སྤྱོད་པ་སྟེ། ཆོས་ནི་ཆོས་དཀོན་མཆོག་དང་འཕགས་པའི་ནོར་བདུན་ནོ། །

[Block 1705]
སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^1453]ཇི་ལྟར་ཆོས་ལ་ལོངས་སྤྱོད་པ་དང་འདྲ་བར་བདག༌[^1454]ཀྱང་ཆོས་ཀྱི་ནོར་ལ་ལོངས་སྤྱོད་པར་བྱའོ་ཞེས་པའི་དོན་ཏོ། །

[Block 1706]
སངས་རྒྱས་ཀྱི་སྲས་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གྱི་སྐྱོན་དང་བཅས་པ་མི་གཙང་བའི་མངལ་ནས་སྐྱེས་པ་ལས་བཟློག་པའོ། །

[Block 1707]
ཐུགས་ལས་བྱུང་བ༌[^1455]ནི་ཕ་མའི་ཁུ་བ་མི་གཙང་བ་ལས་འབྱུང་བ་མ་ཡིན་པར་བསྟན་པའོ། །

[Block 1708]
ཞལ་ནས་སྐྱེས་པ་ནི་ཆོས་མ་ཡིན་པའི་འདོད་ཆགས་ལས་འབྱུང་བ་མ་ཡིན་པར་བསྟན་པའོ། །

[Block 1709]
ཆོས་ལས་སྐྱེས་པ་ནི་ཆོས་ཀྱི་སྐུའི་རིགས་འཚོབ་པ༌[^1456]བསྟན་པ་སྟེ། ཇི་ལྟར་བྲམ་ཟེ་དག་རིགས་འཚོབ་པ་བཞིན་ནོ། །

[Block 1710]
ཆོས་ཀྱི་སྤྲུལ་པ་ནི་ཆོས་ཀྱི་ནོར་ལ་ལོངས་སྤྱོད་པ་སྟེ་ཇི་ལྟར་འཇིག་རྟེན་ན་ཕའི་ནོར༌[^1457]ལ་བུ་དག་སྤྱོད་པ་བཞིན་ནོ། །

[Block 1711 [HEADING]]
###### ཚིགས་སུ་བཅད་དེ་བཟླས་པ། ^4-3-4-1-2-0

[Block 1712]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་ཞེས་པ་ནས། ཐེག་པ་མཆོག་འདིར་བདག་ནི་ཡོངས་སྨིན་མཛད། །ཅེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིགས༌[^1458]བཅད་ཀྱིས་བསྟན་ཏེ། ཚིགས་བཅད་ཉི་ཤུ་རྩ་ཕྱེད་དང་དྲུག་ལ་རྣམ་པ་གཉིས་ཏེ། ཐོག་མའི་ཚིག་ཕྱེད་དང་གསུམ་གྱིས་ནི་གླེང་བ་བསྟན་ཏོ། །

[Block 1713]
ཚིགས་བཅད་ཉི་ཤུ་རྩ་གསུམ་གྱིས་ནི་བཤད་པ་བསྟན་ཏོ། །

[Block 1714 [HEADING]]
###### **གླེང་བ།** ^4-3-4-1-2-1-0

[Block 1715 [HEADING]]
###### **ཐེ་ཙོམ་མེད་པས་རབ་ཏུ་དགའ་བ།** ^4-3-4-1-2-1-1-0

[Block 1716]
གླེང་པ་བསྟན་པ་ལ་ཡང༌[^1459]གཉིས་ཏེ། ཐོག་མའི་ཚིག་གཅིག་གིས་ནི་ཐེ་ཙོམ་མེད་པས་རབ་ཏུ་དགའ་བ༌[^1460]བསྟན་ཏོ། །

[Block 1717]
ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས༌[^1461]ནི་ཐེ་ཙོམ་དང་མྱ་ངན་ཟད་པས་ངོ་མཚར་དུ་གྱུར་པ་བསྟན་ཏོ། །

[Block 1718 [HEADING]]
###### **ཐེ་ཙོམ་དང་མྱ་ངན་ཟད་པས་ངོ་མཚར་དུ་གྱུར་པ།** ^4-3-4-1-2-1-2-0

[Block 1719]
[^1462]བདེ་བར་གཤེགས་པའི་གསུང་དེ་ངོ་མཚར༌[^1463]གྱུར། །ཞེས་པ་ནས། གསུང་ཐོས་པ་ཡིས་ཐམས་ཅད་མེད་པར་གྱུར། །ཞེས་པའི་བར་དུ་ཐེ་ཙོམ་དང་མྱ་ངན་ཟད་པས་ངོ་མཚར་དུ་གྱུར་པ་བསྟན་ཏོ། །

[Block 1720]
སྔོན་ཐེག་པ་ཆེན་པོ་མ་ཐོས་པ༌[^1464]ཐེ་ཚོམ་དང་མྱ་ངན་དུ་འགྱུར་བ༌[^1465]ལས་ད་ཐེག་པ་ཆེན་པོ་ཐོས་པས་ཐེ་ཙོམ་དང་མྱ་ངན་སློས་པ༌[^1466]བསལ་ཞེས་སྨོས་སོ། །
--- END BLOCKS ---
