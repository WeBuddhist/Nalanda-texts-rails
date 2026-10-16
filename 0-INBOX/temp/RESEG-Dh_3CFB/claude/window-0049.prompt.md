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
དེ༌[^1247]བས་ན་སྒྲ་དང་དོན་དག་གི་འབྲེལ་པ་ནི་རང་བཞིན་ཅན་མ་ཡིན་ནོ། །

[Block 1717]
དེའི་བསམ་པ་ཅན་གྱི་སྦྱོར་བ་ལས་བྱུང་བའམ། མངོན་པར་གསལ་བའི་སྒྲ་ནི་དེར་འཁྲུལ་པ་མེད་པའི་ཕྱིར་འདིའི་འབྲེལ་པ་ནི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 1718]
འབྱུང་བའམ་མངོན་པར་གསལ་བ་དེ་ཡང་འཁྲུལ་པ་མེད་པ་ལ་བརྟེན་པའི་སྐྱེས་བུས་བྱས་པའི་ཕྱིར་འབྲེལ་པ་ནི་སྐྱེས་བུས་བྱས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1719]
དེའི་སྒོ་ནས་སྒྲ་རྣམས་ནི་དོན་རྟོགས་པ་ལ་ངེས་པ་ཡིན་པ་དེ་ལྟ་ན། སྐྱེས་བུས་མ་བྱས་པ་ཉིད་ཡིན་ན་ཡང་དེ་ཉིད་འཁྲུལ་པ་ཡིན་ནོ། །

[Block 1720 [VERSE]]
བྱེད་པ་པོ་རྣམས་མི་དྲན༌[^1248]ཕྱིར། །
སྐྱེས་བུས་མ་བྱས་ཀྱང་འདོད་ལོ། །

[Block 1721]
གང་འདི་རིག་བྱེད་པའི་ངག་སྐྱེས་བུས༌[^1249]མ་བྱས་པ་ཉིད་དུ་ཡང་འདོད་དེ།

[Block 1722 [VERSE]]
བྱེད༌[^1250]པོ་མི་དྲན་པའི་ཕྱིར་རོ། །
འདི་ལའང་རྗེས་སུ་བརྗོད་པ་ཡོད། །
དེ་ལྟར་ངན་པ་མུན་ཁྱབ་བྱེད། །

[Block 1723]
རེ་ཞིག་དེ་ཉིད་ཤེས་རབ་འཆལ་པ་དེ༌[^1251]འདྲ་བ་ཇི་ལྟར་སྐྱེ་སྙམ་པས་ཁོ་བོ་ཅག་གི་སེམས་ངོ་མཚར་དང་རྗེས་སུ་བརྩེ་བ་དང་བཅས་པ༌[^1252]ཡིན་ནོ། །

[Block 1724]
དེ་ལ་གཞན་ཡང་རྗེས་སུ་རྗོད་པར་བྱེད་པས་སྲིད་པ་བརྩེ་བ་མེད་པས་གནོད་པ་ཅན་གྱི་ངན་པ་མུན་ཁྱབ་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1725]
སྲོག་ཆགས་ཕན་པ་འདོད་པ་སླུ་བར་བྱེད་པ་ལ་ཉེས་པ་ཅི་ཞིག་ཡོད། འདི་ལྟར་བདེ་བར་གཤེགས་པ་དག་གིས་སྔགས་རྣམས་བྱེད་པ་པོ་བརྒྱད་པ་ལ་སོགས་པ་དག་དང་། གཟེགས་ཟན་པ་དག་གིས་དབྱིག་གི་སྙིང་པོ་ཅན་དྲན་པ་མ༌[^1253]ཡིན་ནོ། །

[Block 1726]
གལ་ཏེ་དེ༌[^1254]དག་གི་དེ་ལོག་པར་སྨྲ་བ་ཡིན་ནོ་ཞེ་ན། ད་ནི་དེ་ལྟར་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་ན་གང་སྐྱེས་བུས་བྱས་པ་ཡིན། གང་གི་ཚེ་འདི་ལྟར་གཞོན་ནུ་འབྱུང་བ་ཅན་ལ་སོགས་པ་བདག་གམ་གཞན་རྩོམ་པ་པོ་ཡིན་པར༌[^1255]སྟོན་པ་སྤོང་བར་བྱེད་པར་འགྱུར་རོ། །

[Block 1727]
དེ་ལ་གལ་ཏེ་སྤོང་བ༌[^1256]ལ་ཁས་བླངས་པས་གནོད་པ་ཡིན་ནོ་ཞེ་ན། འདི་ཉིད་ཁས་བླངས་པའི་ཡན་ལག་མ་ཡིན་ནམ། གང་ལ་གནོད་པ་ཡིན་ན། [^1257]དེ་གཞན་ལ་ཡང་མཚུངས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1728]
གལ་ཏེ་དེའི་འདོད་པ་ཉིད་ཡིན་པའི་ཕྱིར་སྐྱོན་མེད་དོ་ཞེ་ན། འདིའི་འདོད་པའི་འདི་ཚད་མ་མེད་པ་ཅན་གང་ལས་ཐོག་མ་ནས་ཡོད་པར་འགྱུར་ན། གློ་བུར་དུ་འཛིན་པ་ཅན་འདི་ལ་ཡང་འགའ་ཞིག་ཏུ་སྒྲུབ་པར་བྱེད་པ་ལ་ལྟོས་པས་ཅི་ཞིག་བྱ། གང་གིས་སྐྱེས་བུས་བྱས་པ་དང་སྐྱེས་བུས་མ་བྱས་པ་དཔྱོད་པས་བདག་ཉིད་དུབ་པར་བྱེད།[^1258] དེ་ཉིད་འདོད་པའི་ཕྱིར་ཁས་མ་བླངས་པས་གནོད་པ་མེད་པར་འདོད་པ་དེ་ལས་གཞན་པ་ལ་ཡང་མཚུངས་པའི་ཕྱིར་ཀླན་ཀ་བཙལ་དུ་མེད་དོ། །

[Block 1729]
ཕུལ་དུ་བྱུང་བ་མཐོང་བ་མེད་པ་ཅན་འདི་ཡང་དག་རྣམས་རྣམ་པ་དེ་ལྟ་བུར་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་གྲུབ་པར་བྱེད་པའམ། འབྲས་བུའི་ཆོས་རྣམས་འགའ་ཞིག་ལ་ཕུལ་དུ་བྱུང་བར་ཁས་ལེན་པ་དེ་ལྟར་ན། འདིའི་འཇུག་པ་རིགས་པ་མེད་པ་ཅན་ཁོ་ན་ཡིན་ནོ། །

[Block 1730]
བྱེད་པའི་ཡང་དག༌[^1259]པའི་མན་ངག་རྒྱུན་ཆད་པ་ཅན་གྱིས་བྱས་པ་ཡང་མཐོང་ངོ་། །གལ་ཏེ་འབད་རྩོལ་དང་ལྡན་པས་དམིགས་པ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1731]
གཞན་ལ་ཡང་མི་དམིགས་པ་དང་དམིགས་པ་གཞན་གྱིས་བསྟན་པ་ཡིད་ཆེས་པར་བྱ་བ་མ་ཡིན་པ་ལས་ངེས་པར་རིགས་པ་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1732]
བདག་ཉིད་ཀྱིས་བྱས་པ་དག་ལ་ཡང་བསྙོན་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1733]
ངེས་པ་ལ་བརྟེན་པར་མི་ནུས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1734 [VERSE]]
ཇི་ལྟར་སྐྱེས་བུ་འདི་གཞན་ལས། །
ཐོས་མེད་པར་འདི་ཡི་གེ་དང་། །
ཚིག་བཀོད་པ་འདི་བརྗོད༌[^1260]ནུས་མེད། །
དེ་ལྟར་གཞན་ལའང་ཞེས་འགའ་སྨྲ། །

[Block 1735]
གང་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་མིན༌[^1261]ན། གང་སྐྱེས་བུས་བྱས་པ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་ཉིད་ལན་ཡིན་ནོ། །

[Block 1736]
དེ་ལྟར་ན་གཞུང་བཀོད་པ་གཞན་དག་ཏུ།

[Block 1737 [VERSE]]
སྤེལ་བ་ཡི་ནི་གཞུང་གཞན་ཡང་། །
མན་ངག་མེད་པར་གཞན་རྣམས་ཀྱིས། །
བརྗོད་པ༌[^1262]ཅི་མཐོང་ན་གང་གིས། །
དེ་ཡང་དེ་ལྟར་རྗེས་མི་དཔོགས། །

[Block 1738]
དེ༌[^1263]ལྟར་བ་རྣམས་མན་ངག་མེད་པར་ཀློག་པར་མི་ནུས་པ་ལས་གཞན་དུ་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་ཀྱི་རྟེན་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1739]
དེ་ནི་གཅིག་གིས་བརྩམས་པའི་གཞུང་གཞན་ལ་ཡང་གཞན་གྱི་དང་མཚུངས་སོ། །

[Block 1740]
དེའི་རྗེས་སུ་འབྲངས་ནས་ཐམས་ཅད་དེ་ལྟར་རྗེས་སུ་དཔོག་པ་ཡིན་པའམ། འགའ་ཞིག་ཀྱང་མ་ཡིན་ནོ། །

[Block 1741]
དེ་ནི་དེ་ལྟར་མི་འདོད་པ་ཉིད་ཀྱི་ཕྱིར། ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་འདོད་པ་ནི་དེའི་རྟེན་ཉིད་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 1742]
གཞན་ཡང་།

[Block 1743 [VERSE]]
རིག༌[^1264]གང་གང་ལས་གྲུབ་པ་དེས། །
རྒྱུ་མ་མཐོང་བ་ཅན་གཞན་ཡང་། །
བྱེ་བྲག་མེད་པར་མེ་ཤིང་བཞིན། །
དེ་ལས་འགྱུར་བར་ཡང་དག་ཤེས། །

[Block 1744]
རྒྱུ་མ་མཐོང་བའི་ཕྱིར་རྒྱུ་མེད་པ་ཅན་ཞེས་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1745]
དངོས་པོ་རྒྱུ་མ་མཐོང་བ་ཅན་ཡིན་ན་ཡང་དེ་ལས་གཞན་པ་དག་གི་རང་བཞིན་ཐ་དད་པ་ཉམས་སུ་མྱོང་བ་མེད་པར་དེ་ལྟ་བུའི་རྣམ་པ་ཡང་དག་པར་རྗེས་སུ་དཔོག་པར་འགྱུར་རོ། །

[Block 1746]
རྒྱུའི་ངོ་བོ་ལོག་ཏུ་ཟིན་ཀྱང་དེའི་ངོ་བོ་ལོག་པ་མ་ཡིན་ན་ནི་འབྲས་བུའི་ཆོས་ལས་འདས་པའི་ཕྱིར། དེ་ལས་འགྱུར་བ་མེད་པས་ན་ཅུང་ཞིང་དེ་ལྟར་བརྗོད་པར་བྱ་བ་མ་ཡིན་པའམ། ངོ་བོ་བྱེ་བྲག་བསྟན་པར་བྱ་བ་ཡིན་ན་ནི་ད༌[^1265]གང་གིས་རྒྱུ་དེའི་རྗེས་སུ་བྱེད་པར་འགྱུར། [^1266]གང་ཞིག་འདོད་པ་དང་མི་འདོད་པ༌[^1267]ཕྱིན་ཅི་ལོག་ཏུ་མི་འགྱུར་རོ། །

[Block 1747]
རྒྱུའི་རང་བཞིན་ལྡོག་པ་ལས་ཀྱང་དངོས་པོ་རྣམས་ཐ་དད་པ་མེད་པ་ཡིན་ནོ།[^1268] །ཐ་དད་པ་དེ་ནི་གློ་བུར་པར་འགྱུར་བའི་ཕྱིར་འགའ་ཞིག་ཏུ་ཡང་ལྡོག་པར་མི་འགྱུར་རོ། །

[Block 1748]
དེ་བས་ན་རང་བཞིན་གང་ལས་སྐྱེ་བ་ཅན་དུ་མཐོང་བ་གང་ཡིན་པ་དེ་ནི་གཞན་ལ་ཡང་ཐ་དད་པར་མི་བྱེད་པ་ན་ཤིང་དང་མེ་བཞིན་དུ་རང་བཞིན་བདག་ཉིད་ཀྱིས་དེའི་འབྲས་བུ་ཉིད་ལས་འདས་པ་མ་ཡིན་ནོ། །

[Block 1749 [VERSE]]
དེ་ལ་འབྲས་མཚུངས་མཐོང་བའི་ཕྱིར། །
ཁྱད་པར་དག་ནི་མ་བསྟན་པར། །
གཏན་ཚིགས་རབ་ཏུ་སྤྲོས་པ་དག །
དེ་དག་ཐམས་ཅད་འཁྲུལ་པ་ཡིན། །

[Block 1750]
དཔེར་ན་ཐོག་མར་འདྲོན་པོས༌[^1269]གཏང་བའི་མེ་ཉིད་ཀྱང་འདྲོན་པོས༌[^1270]བཏང་བའི་མེ་ཉིད་ཡིན་པའི་ཕྱིར། མེ་གཞན་སྔོན་དུ་སོང་བ་ཅན་ཡིན་གྱིས།[^1271] གཙུབ་ཤིང་གཙུབས་པ་སྔོན་དུ་སོང་བ་ཅན་ནི་མ་ཡིན་ཏེ། དེ་མ་ཐག་པའི་མེ་བཞིན་ནོ། །

[Block 1751]
ཇི་ལྟར་ན་འདྲོན༌[^1272]པོས་བཏང་བའི་མེ་ཡང་འཁྲུལ་པ་ཡིན་ཏེ། མེ་ལས་བྱུང་བའི་ནུས་པ་ལ་བརྟེན་ནས་མེའི་རྒྱུ་གཞན་སྤོང་བར་བྱེད་དོ། །

[Block 1752]
གལ་ཏེ་མེ་མེད་པར་ཡང་འགྱུར་ན་ནི་གཞན་དག་ལ་ཡང་འགྱུར་རོ་ཞེ་ན། དེ་ལ་མེ་ཉིད་དང་ཅིག་ཤོས་ལས་བྱུང་བ་དག་ལ་གནོད་པར་བྱ་བ་དང་གནོད་པར་བྱེད༌[^1273]པ་མེད་པས༌[^1274]མེ་ལས་བྱུང་བ་ཉིད་ནི་གཞན་དག་ལ་ཡང་འགྱུར་བ། དེ་ལྟར་ན་ཆོས་གཉིས་དག་དོན་གཅིག་ལ་སྲིད་པའི་ཕྱིར། འདྲོན་པོས༌[^1275]བཏང་བའི་མེའམ། དོན་གཞན་ནི་གཅིག་ལ། སོ་སོར་ངེས་པར་འགྱུར་བ་མེད་པས་ན་འཁྲུལ་པར་དོགས་པ་ཡིན་ནོ། །

[Block 1753]
ཕན་ཚུན་ཐ་དད་པ་ཅན་གྱི་ཆོས་གཉིས༌[^1276]འཇུག་པ་དེ་ཡང་ཕྱིའི༌[^1277]དངོས་པོ་ལ་འགལ་བ་མེད་དོ། །ཞེས་བརྗོད་པར་བྱ་བའི་གནས་སྐབས་ཐ་དད་པ་ཅན་གྱི་ཁྱད་པར་ནི་མ་ཡིན་ཏེ། ཆ་མེད་པའི་བདག་ཉིད་ལས༌[^1278]དེ་ཉིད་དང་དེ་ཉིད་མ་ཡིན་པ་འགལ་བའི་ཕྱིར་རོ། །

[Block 1754]
འདྲོན་པོས༌[^1279]བཏང་བའི་མེ་ལ་མེ་དང་ཅིག་ཤོས་ཀྱིས་བསྐྱེད་པ་ནི་གནོད་བྱ་དང་གནོད་བྱེད༌[^1280]མ་ཡིན་ཏེ། དེ་ནི་མེས་བསྐྱེད་པ་མེད་པར་མི་སྲིད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1755]
དེ་ལྟ་བུར་གྱུར་པའི་འདྲོན༌[^1281]པོས་བཏང་བའི་མེ་མེ་ལས་བྱུང་བ་ཞེས་བྱ་བར་ནི་འགྱུར་གྱི། ཐམས་ཅད་ནི་མ་ཡིན་ཏེ། དེ་ལ་ཁྱད་པར་སྤོང་བར་བྱེད་པར་མི་ནུས་པའི་ཕྱིར་དང་། ཁྱད་པར་ཡོད་པ་ཅན་གྱི་དེའི་གནས་སྐབས་ཅན་ཉིད་ལ་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
