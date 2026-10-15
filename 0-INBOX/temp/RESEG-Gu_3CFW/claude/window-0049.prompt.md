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
[Block 1716]
འདི་ལྟར་བསོད་སྙོམས་ལ་དེ་སྐད་གསུངས་པ་ཡིན་མོད་ཀྱི་གཞན་ལ་ཡང་དེ་རུང་བར་གནང་བས་དེ་རིགས་པར༌[^1491]བྱའོ། །

[Block 1717]
ལྟ་བ་དང་ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་དག་ལས་བླངས་པ་གཞན་གོ་རིམས་བཞིན་ལ་སྦྱིན་པ་དང་། འཚོ་བར་བྱེད་པ་ལྷག་མ་ཁམ་གཅིག་ཡན་ཆད་ལེན་པ་དང་ཟ་བ་ནི་དད་པས་སྦྱིན་པར་བྱ་བ་ཆུད་གསོན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གོ་རིམས་བཞིན་ལ་ཞེས་བྱ་བ་ནི༌[^1492]ལྟ་བ་ཕུན་སུམ་ཚོགས་པ་ལས་བླངས་པ་ལྟ་བ་ཉམས་པ་ལ་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་ལས་བླངས་པ་ཚུལ་ཁྲིམས་འཆལ་པ་ལ་སྦྱིན་པ་ལ་ནི་དཔེ་ཙམ་དུ་ཟད་དེ། མཆོག་ལས་བླངས་པ་མཆོག་མ་ཡིན་པ་ལ་ཡང་སྦྱིན་པ་ཞེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པར་རེག་པར༌[^1493]བྱའོ། །

[Block 1718]
མཆོག་དང་མཆོག་མ་ཡིན་པ༌[^1494]ནི་འདི་ལྟར་ཤེས་པར་བྱ་སྟེ། ཏིང་ངེ་འཛིན་ཐོབ་པ་ནི་མ་ཐོབ་པ་བས་མཆོག་གོ། །

[Block 1719]
འཕགས་པ་ནི་མ་འཕགས་པ་མ༌[^1495]ཡིན་པས་སོ། །

[Block 1720]
ཆོས་ཀྱི་ཚོགས་རབ་ཏུ་འཕེལ་བའི་བྱང་ཆུབ་སེམས་དཔའི༌[^1496]སོ་སོའི་ཡང༌[^1497]ཉན་ཐོས་ལས་སོ། །

[Block 1721]
དེ་ལྟར་འཛམ་བུའི་གྲིབ་མ་ལ་བཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཤཱཀྱ་ཐུབ་པའི་དབང་དུ་མཛད་ནས་གསུངས་པ་ནི་དེ་ལ་ཕུལ་བས་བསོད་ནམས་ཆེས་མང་དུ་འཕེལ་བར་འགྱུར་གྱི་དགྲ་བཅོམ་པ་བྱེ་བ་རྣམས་ལ་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 1722]
ཁམ་གཅིག་ཡན་ཆད་ཅེས་བྱ་བ་ནི་འདིར་ཡན་ཆད་ཀྱི་སྒྲ་དང་རབ་ཏུ་འབྲེལ་བར་རིག་པར་བྱ་སྟེ། ཁམ་གཅིག་ཡན་ཆད་ཅེས་བྱ་བའོ། །

[Block 1723]
ཁམ་གཅིག་ཡན་ཆད་ཟ་བ་ནི་འཚོ་བར་བྱེད་པ་ཙམ་ལས་ལྷག་པར་ལན་པ༌[^1498]དང་། ཟ་བ་ནི་དད་པས་སྦྱིན་པར་བྱེད་པ་ཆུད་གསོན་པ༌[^1499]ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1724]
ཕ་མ་དང་ནད་པ་དང་རབ་ཏུ་བྱུང་བར་འདོད་པ་དང་སྦྲུམ་པ་དག་དང་། གདུལ་བ་དང་འདོད་པས་བསོད་སྙོམས་ལ་རེག་པ་དང༌[^1500]ཁྱིམ་པ་འོངས་པ་ལ་ནི་དེ་ལས་བགོ་བཤའ་བྱའོ། །ཞེས་བྱ་བ་ནི་དེ་བསོད་སྙོམས་ཆུད་ཟོས་པར་བྱེད་པ་དེ་ལས་དད་པས་སྦྱིན་པར་བྱ་བ་ཆུན་གསོན་པའི༌[^1501]ཚིག་ཏུ་རིག་པར་མི་བྱའོ། །

[Block 1725]
ཁམ་ཆངས༌[^1502]གཅིག་ཟ་བ་པོ་རྣམ་པར་མི་བཅད་པར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི། འགའ་ཞིག་ཏུ་མིད་པ༌[^1503]ལ་ཡང་ཁམ་ཆངས༌[^1504]གཅིག་ཟ་བ་པོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1726]
འདིར་གཞུང་ནི་ཅི་ནས་ཀྱང༌[^1505]ལྷག་མར་མ་གྱུར་པའི་ཁམ་ཆངས༌[^1506]གཅིག་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1727]
བཟའ་བའི་ཕྱིར་ཉེ་བར་དུད་འགྲོ་ལ་ཡང་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི། ཁམ་ཆངས༌[^1507]གཅིག་གཞག་པ་དེའོ། །

[Block 1728]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་ཟོས་ནས༌[^1508]དུད་འགྲོ་ལ་ཁམ་གཅིག་མི་གཞག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1729]
བཟའ་བའི་ཕྱིར་ཉེ་བར་གཞག་པ་ལས་མ་རྫོགས་པར་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། མ་རྫོགས་པར་ཞེས་བྱ་བ་ནི་ཟས་མ་རྫོགས་པ་ལའོ། །

[Block 1730]
དད་པས་སྦྱིན་པར་བྱ་བ་དེ་ཉིད་ཀྱིས་མགྲོན་དུ་བོས་པ་ལ་ཡང་མི་བྱའོ། །

[Block 1731]
ལྷུང་བཟེད་ཀྱི་གཞི་ནི་ལྷག་མ་ཟ་བ་རྣམས་ལ་ཅི་བདེར་བྱའོ། །

[Block 1732]
གཉུག་མར་གནས་པ་རྣམས་ལ་གཏོར་མ་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་ན་གཉུག་མར་གནས་པ༌[^1509]མི་མ་ཡིན་པའི་གནས་པ་རྣམས་ལ་འབད་པས་དེ༌[^1510]སྦྱིན་པ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 1733]
དེ་དག་གི་ཆོ་གའི་རྗེས་སུ་འབྲངས་པས་སྔ་རོལ༌[^1511]ལ་སོགས་པར་རོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་གཉུག་མར་གནས་པ་དེ་དག་གི་ཆོ་གའི་རྗེས་སུ་འབྲང་བས་སྔ་དྲོ་ལ་སོགས་པས༌[^1512]གཏོར་མ་སྦྱིན་པར་བྱ་བའི་དོན་ཏོ། །

[Block 1734]
ཆོ་ག་ཐ་དད་པ་ཉིད་ཡིན་ན་ཐ་དད་པར་རོ་ཞེས་བྱ་བ་ནི། གང་དུ་ཁ་ཅིག་ཆོ་ག་ཡང་གཞན་ཡིན་ལ། ཁ་ཅིག༌[^1513]གི་ཆོ་ག་ཡང་གཞན་ཡིན་ན་དེར་ཆོ་ག་དེ་རྣམས་ཐམས་ཅད་སོ་སོར་སྦྱིན་པར་བྱ་བ་ཞེས་བྱ་བའི༌[^1514]དོན་ཏོ། །

[Block 1735]
ཨ་མྲ་རུས་པ་མ་ཆགས་པ་དག་གི་གནས་སྐབས་སུ་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཟེ་འབྲུ་ཆགས་པ་ཉིད་ཀྱི༌[^1515]སྨན་པ་རྣམས་ལ་རྗེས་སུ་གནང་བ་གང་ཡིན་པ་དེ་ལ་ནི་འདི་ལས་ལྷག་པར་འགྱུར་བ་མ་ཡིན་ཏེ། དེའི་ཚེ་ཟེ་འབྲུ་ཆགས་པ་ཉིད་ལ་ངེས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1736]
དང་པོ་ཉིད་དུ་ཟེ་འབྲུ་ལས་རུས་པ་མ་ཆགས་པ་སྒྲུབ་པའི༌[^1516]ཕྱིར་དེ་བས་ན་མ་སྦྱར་རོ། །

[Block 1737]
རྩ་བ་དང་སྡོང་བུ་དང་འདབ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་དང་བཅའ་བར༌[^1517]བྱ་བ་དང་། འབྲས་ཆན་དང་ཟན་དྲོན་དང་འདེ་གུ༌[^1518]དང་ཤ་དང་། སྣུམ་ཁུར་དང་འོ་མ་དང་ཞོ་དང་མར་དང༌[^1519]ཉ་ཤ་དང་ཤ་སྐམ་དག་ནི་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཚོད་མ་ཉིད་དུ་ཡང་ཤ་ལ་སོགས་པས་བཟའ་བའི་དོན་དུ་ཞེས་བྱ་བ་ནི་བསྟན་པའི་ཕྱིར་ཉ་ཤ་དང་ཤ་སྐམ་དག་བཟུང་བའོ། །

[Block 1738]
སྔ་མ་ལ་ནི་ཤའིའོ། །

[Block 1739]
འདིར་འོ་མ་ལ་སོགས་པ་ནི་ཚོད་མ་དག་བསྟན་ཏོ། །

[Block 1740]
འབྲས་ཆན༌[^1520]ལ་སོགས་པས་ནི་བཟའ་བ་དག་བསྟན་ཏོ། །

[Block 1741]
རྩ་བ་ལ་སོགས་པས་ནི་བཅའ་བ་དག་བསྟན་ཏོ། །

[Block 1742]
གསོ་མ་དང་ཡུངས་ཀར་དང་རྩ་བ་དང་། སྡོང་བུ་དང་འདབ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་ལ་སོགས་པའི་ཐུག་པ་དག་བསྟེན་པར༌[^1521]བྱ་བ་དག་མ་ཡིན་པར་དོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། འདི་དག་སྨན་ཉིད་ཀྱི་སྐབས་ཡིན་མོད་ཀྱི། འཚོ་བ་ཙམ་གྱི་དོན་དུ་གཞན་ལ་ཡང་སྦྱར་བ་དེ་བས་ན་བྱེ་བྲག་མེད་པར་སྨོས་སོ། །

[Block 1743]
སིལ་བུ་དག་ལས་རྐྱལ་པར་བླུགས་པ་འདི་ཡང་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1744]
ཆུས་ཀྱང་སྦངས་ནས་འཚག་ཏུ་འགྱུར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། ལྷག་མར་གྱུར་པ་དེས་འོ་མ་ལ་སོགས་པ་ཚོད་མའི་རྣམ་པ་གང་ཡང་རུང་བས་སྦངས་ནས༌[^1522]རྣམ་པ་གང༌[^1523]རུང་བས༌[^1524]ན་སྦངས་ནས༌[^1525]ཡང་འཚག་ཏུ་འགྱུར་བ་ཉིད་བསྟན་ཏོ། །

[Block 1745]
རྐྱལ་པར་བླུགས་ན་ནི་མི་རུང་བ་མ་ཡིན་ནོ། །

[Block 1746]
སྣོད་དུ་ཟན་བཟར་རུང་ངོ་། །ཡོལ་གོར༌[^1526]རོ། །

[Block 1747]
རྡོ་ལས་བྱས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ཟས་བཟར་རུང་བའོ། །

[Block 1748]
ཟས་བྱས་པར་ཡང་ངོ་། །ལྕགས་ཀྱི་ལྷུང་བཟེད་ལ་སོགས་པ་བཞིན་བཀྲུས་ཏེའོ། །

[Block 1749]
བཀྲུ་བཤལ་ནི་གནས་པའི་ལས་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འོ་ན་ལྷུང་བཟེད་ལ་དེ་སྨོས་ཏེ། དེ་ཉིད་ལ་ནི་འདི་ལ་དཔེ་གཉིས་ཀྱིས་གྲུབ་པོ་ཞེ་ན། དེ་ལྟར་ནི་མ་ཡིན་ཏེ། གྲུབ་པ་ལ་ངོས༌[^1527]ཀྱི་ཚིག་ནི་སྐྱོན་ཡིན་ཏེ། འདི་ལ་ཤིན་ཏུ་གསལ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1750]
ཟོས་ནས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། ལྷག་མ་མ་ཡིན་པ་ལ་ལྷུང་བཟེད་བཀྲུ་བ་ལ་སོགས་པ་རིགས་པ་ཡིན་ཏེ། དེ་ཟློག༌[^1528]པའི་དོན་དུ་འདིའོ། །

[Block 1751]
འདིར་གཞུང་ནི་མཁན་པོ་དང་སློབ་དཔོན་དག་གི་སྣོད་དག་གནས་པ་དག་གིས༌[^1529]བཀྲུས་ཏེ་དབུལ་བར་བྱའོ། །

[Block 1752]
ཟོས་ནས་ཀྱང་གནས་པ་དག་གིས༌[^1530]སྣོད་དང་བྱ་མ་བུམ་བཀྲུས་ཏེ་བསྐུར་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1753]
གཞན་དང་ལྷན་ཅིག་སྣོད་གཅིག་ཏུ་བཟའ་བར་མི་བྱའོ། །

[Block 1754]
ལམ་དུ་སྣོད་དག་མེད་ན་བཟའ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་དུ་ཕོངས་པའི་ཕྱིར་མེད་ན། རིམ་གཅིག་གི་ཕྱིར་ཟ་བ་དེ་ལ་ནི་མེད་པ་མ་ཡིན་ཏེ། ཡོད་པ་དང་མེད་པའི་རྣམ་པར་གཞག་པ་ནི་འབྲས་བུའི་དུས་ལ་ལྟོས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1755]
དེ་ལྟ་བས་ན་འདིར་ཡང་དེ་བྱས་པས་ཤེས་པར་མི་བྱའོ། །
--- END BLOCKS ---
