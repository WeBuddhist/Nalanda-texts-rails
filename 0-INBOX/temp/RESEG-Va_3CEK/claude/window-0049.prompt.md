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
ཆོས་གང་མ་སྐྱེས་པ་དེ་ནི་མ་འོངས་པ་ཡིན་ནོ། །

[Block 1717]
གང་སྐྱེས་ལ་མ་ཞིག་པ་དེ་ནི་ད་ལྟར་བྱུང་བ་ཡིན་ནོ། །

[Block 1718]
གང་ཞིག་པ་དེ་ནི་འདས་པ༌[^1263]ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་མི་འགྲུབ་པ་ཅི་ཞིག་ཡོད། འདིར་དེ་ཉིད་བརྗོད་པར་བྱ་དགོས་ཏེ། གལ་ཏེ་ཇི་ལྟར་ད་ལྟར་གྱི་རྫས་སུ་ཡོད་པ་དེ་བཞིན་དུ། འདས་པ་དང་མ་འོངས་པ་ལ༌[^1264]ཡང་ཡོད་ན་ནི། དེ་བཞིན་དུ། ཡོད་ན་ཅིའི་ཕྱིར་མ་སྐྱེས་ཤིག །[^1265]ཆོས་དེའི་རང་གི་ངོ་བོ་ཁོ་ནར་ཡོད་ན་ནི༌[^1266]ཇི་ལྟར་ན་མ་སྐྱེས་པ་ཞེས་བྱ་བའམ། ཞིག་པ་ཞེས་བྱ་བ་འདི་འགྲུབ་པར་འགྱུར། གང་ཞིག་མེད་པས་མ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི༌[^1267]སྔོན་ཅི་ཞིག་མ་བྱུང་བར་འགྱུར།[^1268] གང་ཞིག་མེད་པས་ཞིག་པ་ཞེས་བྱ་བ་ཡང་ཕྱིས་ཅི་ཞིག་མེད་དེ། དེ་ལྟ་བས་ན་གལ་ཏེ་མ་བྱུང་བ་ལས་བྱུང་བ་དང་། བྱུང་ནས་ཀྱང་ཡང་མི་འབྱུང་བར་མི་འདོད་ཕན་ཆད་དུས་གསུམ་རྣམ་པ་ཐམས་ཅད་དུ་མི་འགྲུབ་བོ། །

[Block 1719]
གང་ཡང་འདུ་བྱེད་ཀྱི་མཚན་ཉིད་དང་ལྡན་པའི་ཕྱིར་རྟག་པ་ཉིད་དུ་ཐལ་བར་མི་འགྱུར་རོ་ཞེས་སྨྲས་པ་དེ་ཡང་སྐྱེ་བ་དང་། འཇིག་པ་དག་མི་རུང་བའི་ཕྱིར་ཚིག་ཙམ་སྟེ། ཆོས་དེ་རྟག་པ༌[^1269]ཡང་ཡོད་ལ་མི་རྟག་པ་ཡང་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་གི་ལུགས་འདི་ནི་སྔོན་མ་བྱུང་བ་ཡིན་ནོ། །

[Block 1720]
ཡང་སྨྲས་པ།

[Block 1721 [VERSE]]
རང་བཞིན་ཡང་ནི་རྟག་ཏུ་ཡོད། །
དངོས་པོ་ཡང་ནི་རྟག་མི་འདོད། །
རང་བཞིན་ལས་ཀྱང་དངོས་མི་གཞན། །
དབང་ཕྱུག་ཐ་སྙད་ཡིན་པར་གསལ། །

[Block 1722 [HEADING]]
#### གསུངས་ཕྱིར་ཞེས་སྨྲས་པ། ^2-22-5-0

[Block 1723]
གང་ཡང་གསུངས་ཕྱིར་ཞེས་སྨྲས་པ། །ཁོ་བོ་ཅག་ཀྱང་འདས་པ་དང་མ་འོངས་པ་ཡོད་དོ་ཞེས་སྨྲས་ཏེ། [^1270]སྔོན་བྱུང་བ་གང་ཡིན་པ་དེ་ནི་འདས་པ་ཡིན་ལ། རྐྱེན་ཡོད་ན་འབྱུང་བར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་མ་འོངས་པ་ཡིན་ནོ་ཞེས་དེ་ལྟར་བྱས་ནས་ཡོད་དེ༌[^1271]ཞེས་བྱའི། རྫས་སུ་ནི་མ་ཡིན་ནོ། །

[Block 1724]
ད་ལྟར༌[^1272]བཞིན་དུ་ཡོད་དོ་ཞེས་དེ་སྐད་དུ་ཟེར། གཞན་དུ་ན་ཇི་ལྟར་ཡོད། འདས་པ་དང་མ་འོངས་པའི་བདག་ཉིད་དུ་ཡོད་མོད། གལ་ཏེ་རྟག་ཏུ་ཡོད་ན་དེ་ཇི་ལྟར་འདས་པ་དང་མ་འོངས་པ་ཞེས་བྱ་བ་དེ་ཉིད་ཉེ་བར་གནས་སོ། །

[Block 1725]
དེ་ལྟ་བས་ན་བཅོམ་ལྡན་འདས་ཀྱིས་རྒྱུ་དང་འབྲས་བུ་ལ་སྐུར་པ་འདེབས་པའི་ལྟ་བ་དགག་པའི་ཕྱིར་སྔོན་བྱུང་བའི༌[^1273]རྒྱུ་དང་། ཕྱིས་འབྱུང་བར་འགྱུར་བའི་འབྲས་བུ་སྔོན་བྱུང་བ་ཉིད་དང་འབྱུང་བར་འགྱུར་བ་ཉིད་དུ་ཤེས་པར་བྱ་བར་འདས་པ་ཡོད་དོ། །

[Block 1726]
མ་འོངས་པ་ཡོད་དོ་ཞེས་གསུངས་པར་ཟད་དོ། །

[Block 1727]
ཡོད་ཅེས་བྱ་བའི་སྒྲ་ནི་ཚིག་གི་སྒྲ༌[^1274]ཡིན་པའི་ཕྱིར་ཏེ། དཔེར་ན་སྨྲ་བ་པོ་མར་མེ་སྔ་མ་མེད་པ༌[^1275]ཡོད་དོ། །

[Block 1728]
ཕྱིས་མེད་པ་ཡོད་དོ་ཞེས་སྨྲས་པ༌[^1276]དང་། ཡང་དཔེར་ན་མར་མེ་དེ༌[^1277]ཤི་བ་ནི་ཡོད་མོད་ཀྱི་ཁོ་བོས་ནི་མ་བསད་དོ་ཞེས་འཛེར་བ་དེ་བཞིན་དུ་འདས་པ་དང་། མ་འོངས་པ་ཡང༌[^1278]ཡོད་དོ་ཞེས་གསུངས་ཀྱི། དེ་ལྟ་མ་ཡིན་ན་འདས་པ་དང་མ་འོངས་པ་མི་འགྲུབ་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 1729]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་ཀུན་དུ་རྒྱུ་དབྱུག་ཐོགས་ཐོར་ཚུགས་ཅན་རྣམས་ཀྱི་དབང་དུ་མཛད་ནས། ལས་འདས་པ་དང་། ཟད་པ་དང་། འགོག་པ༌[^1279]དང་། བྲལ་བ་དང་། རྣམ་པར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་ཡོད་དོ་ཞེས་གང་གསུངས་པ་ཇི་ལྟ་བུ། [^1280]ཅི་དེ་དག་ལས་དེ་སྔོན་བྱུང་བ་ཉིད་དུ་མི་འདོད་པར་གྱུར་ཏམ། དེ་ལས་ནི་རྒྱུད་དེ་ལས༌[^1281]དེས་ཀུན་དུ་དྲངས་པར༌[^1282]འབྲས་བུ་བསྐྱེད་པའི༌[^1283]མཐུ་ཡོད་པ་ལས་དགོངས་ཏེ་གསུངས་པ་ཡིན་ནོ། །

[Block 1730]
དེ་ལྟ་མ་ཡིན་ཏེ། རང་གི་ངོ་བོ་ཁོ་ནར་ཡོད་ན་འདས་པ༌[^1284]འགྲུབ་པར་མི་འགྱུར་རོ། །

[Block 1731]
དེ་ནི་གདོན་མི་ཟ་བར་དེ་ལྟ་བུ་ཡིན་པར་ཤེས་པར་བྱ་སྟེ།

[Block 1732]
འདི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་དོན་དམ་པ་སྟོང་པ་ཉིད་ཀྱི་མདོ་ལས།

[Block 1733]
མིག་ནི་སྐྱེ་བ་ན་ཡང་གང་ནས་ཀྱང༌[^1285]མི་འོང་ལ། འགག་པ་ན་ཡང་གང་དུ་ཡང་སོགས་པར་མི་འགྱུར་རོ། །

[Block 1734]
དེ་ལྟ་བས་ན་དགེ་སློང་དག་མིག་ནི་མ་བྱུང་བ་ལས་འབྱུང་ཞིང་བྱུང་ནས་ཀྱང་སླར་འཇིག་པར་འགྱུར་རོ་ཞེས་གསུངས་ཏེ། གལ་ཏེ་མ་འོངས་པའི་མིག་ཅིག་ཡོད་པར་གྱུར་ན་མ་བྱུང་བ་ལས་འབྱུང་ངོ་ཞེས་གསུངས་པར༌[^1286]མི་འགྱུར་རོ། །

[Block 1735]
གལ་ཏེ་ད་ལྟར་གྱི་དུས་སུ་མ་བྱུང་བ་ལས་འབྱུང་ངོ་ཞེ་ན་མི་རུང་སྟེ། དུས་ནི་དངོས་པོ་ལས་དོན་གཞན་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1736]
འོན་ཏེ་རང་གི་མཚན་ཉིད་དུ་མ་བྱུང་བ་ལས་འབྱུང་ངོ་ཞེ་ན་ནི་མ་འོངས་པའི་མིག་མེད་དོ་ཞེས་བྱ་བ་འདི་གྲུབ་པ་ཡིན་ནོ། །

[Block 1737 [HEADING]]
#### རྣམ་པར་ཤེས་པ་གཉིས་ལ་བརྟེན་ནས་སྐྱེ་བ། ^2-22-6-0

[Block 1738]
གང་ཡང་རྣམ་པར་ཤེས་པ་ནི་གཉིས་ལ་བརྟེན་ནས་སྐྱེ་བའི་ཕྱིར་རོ་ཞེས་སྨྲས་པ་ནི་རེ་ཞིག་འདིར་ཡིད་དང་ཆོས་རྣམས་ལ་བརྟེན་ནས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་སྐྱེ་བ་གང་ཡིན་པ་དེ་ཇི་ལྟར་ཡིད་སྐྱེད་པར་བྱེད་པའི་རྐྱེན་ཡིན་པ་དེ༌[^1287]ལྟར་ཆོས་རྣམས་ཀྱང་དེ་དང་འདྲའམ། འོན་ཏེ་ཆོས་རྣམས་དམིགས་པ་ཙམ་ཞིག་ཡིན་ཞེས་བྱ་བ་འདི་དཔྱད་པར་བྱ་སྟེ། རེ་ཞིག་གལ་ཏེ་ཆོས་རྣམས་སྐྱེད་པར༌[^1288]བྱེད་པའི་རྐྱེན་ཡིན་ནོ་ཞེ་ན་ནི་ཇི་ལྟར་ན་མ་འོངས་པ་བསྐལ་པ་སྟོང་ན་འབྱུང་བར་འགྱུར་བའམ། ཡང་ན་མི་འབྱུང་བ་གང་ཡིན་པ་དེ་ད༌[^1289]ལྟར་གྱི་རྣམ་པར་ཤེས་པ་བསྐྱེད་པར་འགྱུར། མྱ་ངན་ལས༌[^1290]འདས་པ་ཡང་འཇུག་པ་ཐམས་ཅད་དང་འགལ་བའི་ཕྱིར་སྐྱེད་པར་བྱེད་པ་ཡིན་པར་མི་འཐད་དོ། །

[Block 1739 [HEADING]]
#### མེད་པ་ཡང་དམིགས་པ། ^2-22-7-0

[Block 1740]
འོན་ཏེ་ཆོས་རྣམས་དམིགས་པ་ཙམ་ཞིག་ཡིན་ནོ་ཞེ་ན་ནི་འདས་པ་དང་མ་འོངས་པ་ཡང་དམིགས་པ་ཡིན་ནོ་ཞེས་སྨྲའོ། །

[Block 1741]
གལ་ཏེ་མེད་པ་ཇི་ལྟར་དམིགས་པ་ཡིན་ན་ཞེ།[^1291] ད་ནི་འདིར་དེ་ཇི་ལྟར་ན་དམིགས་པ་ཡིན་པ་དེ་ལྟར་ཡོད་དོ་ཞེས་སྨྲའོ། །

[Block 1742]
དེའི༌[^1292]ཇི་ལྟར་ན་དམིགས་པ་ཡིན་ཞེ་ན། བྱུང་བར་གྱུར་པ་དང་། འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་སྟེ། འདས་པའི་གཟུགས་སམ། ཚོར་བ་དྲན་པ་ན་ཡོད་དོ་ཞེས་བྱ་བར་ནི་སུ་ཡང་མི་ལྟའོ། །

[Block 1743]
འོ་ན་ཅི་ཞེ་ན། བྱུང་བར་གྱུར་ཏོ་ཞེས་བྱ་བར་ལྟའོ།[^1293] །ཡང་ཇི་ལྟར་ད་ལྟར་གྱི་གཟུགས་ཉམས་སུ་མྱོང་བ་དེ་ལྟར་འདས་པ་ཡང་དྲན་ནོ། །

[Block 1744]
མ་འོངས་པ་ཇི་ལྟར་ད་ལྟར་དུ་འགྱུར་བ་དེ་ལྟ་བུ་ནི་སངས་རྒྱས་རྣམས་ཀྱིས་མཁྱེན་ཏོ། །

[Block 1745]
གལ་ཏེ་ཡང༌[^1294]དེ་དེ་བཞིན་དུ་ཡོད་དོ་ཞེ་ན་ནི་ད་ལྟར༌[^1295]དུ་འགྱུར་རོ། །

[Block 1746]
འོན་ཏེ་མེད་དོ་ཞེ་ན་ནི་མེད་པ་ཡང་དམིགས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པ་ཡིན་ནོ། །

[Block 1747]
གལ་ཏེ་དེ་ཉིད་སིལ་བུ་ཡིན་ནོ་ཞེ་ན་མ་ཡིན་ཏེ། སིལ་བུ་ལ་མི་འཛིན་པའི་ཕྱིར་རོ། །

[Block 1748]
གལ་ཏེ་ཡང་དེ་ནི་གཟུགས་དེ་ཁོ་ན་ཡིན་ཏེ། རྡུལ་ཕྲ་རབ་ཏུ་གྱེས་པ་འབའ་ཞིག་ཏུ་ཟད་དོ་ཞེ་ན། དེ་ལྟ་ན་ནི་རྡུལ་ཕྲ་རབ་རྣམས་རྟག་པར་འགྱུར་ཏེ། དེ་ལྟ་ན་རྡུལ་ཕྲ་རབ་བསགས་པ་དང་གྱེས་པ་ཙམ་དུ་འགྱུར་གྱི་ཅུང་ཟད་ཀྱང་སྐྱེ་བ་ཡང་མེད་ལ་འགག་པ་ཡང་མེད་པས་འཚོ་བྱེད་ཀྱི་རྩོད་པ་བླངས་པ་ཡིན་ནོ། །

[Block 1749]
མིག་ནི་ནམ༌[^1296]སྐྱེ་བ་ན་ཡང་གང་ནས་ཀྱང་མི་འོང་ཞེས་རྒྱས་པར་གསུངས་པའི་མདོ་ཡང་བོར་བར་འགྱུར་རོ། །

[Block 1750]
ཚོར་བ་ལ་སོགས་པ་རྡུལ་ཕྲ་རབ་བསགས་པ་མ་ཡིན་པ་རྣམས་ཀྱང་ཇི་ལྟར་ན་སིལ་བུ་ཉིད་ཡིན། དེ་དག་ཀྱང་ཇི་ལྟར་བྱུང་ཞིང་ཉམས་སུ་མྱོང་བ་དྲན་ཏེ། གལ་ཏེ་ཡང་དེ་དག་དེ་བཞིན་དུ་ཡོད་དོ་ཞེ་ན་ནི་རྟག་པར་འགྱུར་རོ། །

[Block 1751]
འོན་ཏེ་མེད་དོ་ཞེ་ན་ནི། མེད་པ་ཡང་དམིགས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པ་ཡིན་ནོ། །

[Block 1752]
གལ་ཏེ་མེད་པ་ཡང་དམིགས་པ་ཡིན་ན་སྐྱེ་མཆེད་བཅུ་གསུམ་པ་ཡང་དམིགས་པ་ཡིན་པར་འགྱུར་རོ། །

[Block 1753]
འོ་ན་སྐྱེ་མཆེད་བཅུ་གསུམ་པ་མེད་དོ་སྙམ་པའི་རྣམ་པར་ཤེས་པ་འདིའི་དམིགས་པ་ཅི་ཞིག་ཡིན། མིང་དེ་ཉིད་དམིགས་པ་ཡིན་ནོ། །

[Block 1754]
དེ་ལྟ༌[^1297]ནི་འོ་ན་མིང་དེ༌[^1298]ཉིད་མེད་དོ་ཞེས་བྱ་བར་རྟོགས་པར་འགྱུར་རོ། །

[Block 1755]
གང་ཞིག་སྒྲའི་སྔ་ན་མེད་པ་ལ་དམིགས་པ་དེའི་དམིགས་པ་ཡང་ཅི་ཞིག་ཡིན། སྒྲ་ཁོ་ན་ཡིན་ནོ། །
--- END BLOCKS ---
