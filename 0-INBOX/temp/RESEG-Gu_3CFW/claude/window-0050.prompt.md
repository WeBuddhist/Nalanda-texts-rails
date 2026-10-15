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

[Block 1756]
འདིར་སུ་དང་ལྷན་ཅིག་ཏུ་བཟའ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་དང་ངོ་། །གཞན་གྱི་ལག་བཏེག༌[^1531]ནས་རང་གིས་གཞུག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ་རང་གིས་ཞེས་བྱ་བ་ནི་ལག་པའོ། །

[Block 1757]
དགེ་ཚུལ་དང་ནི་འོག་མ་བཞིན་ནོ། །

[Block 1758]
མི་ལྡན་ན་ལྷན་ཅིག་ཏུའོ་ཞེས་བྱ་བ་ནི་གཞན་ཉིད་མི་ལྡན་ན་གང་ཞིག་འདིར་རུང་བར་བྱེད་པ་ལ་བྱ་བ་བཅངས་ཏེ་སྦྱིན་པར་གལ་ཏེ་རྐྱེན་གྱི་དབང་གིས་འདིར་བྱ་བར་མི་རིགས་ན། དེ་ནས༌[^1532]ལམ་དུ་སྣོད་གཞན་མེད་ན་དགེ་ཚུལ་དང་ལྷན་ཅིག་ཏུ་བཟའ་བར་བྱ་བའི་དོན་ཏོ། །

[Block 1759]
རབ་ཏུ་བྱུང་བ་ཉིད་ཀྱིས༌[^1533]འདི་ལ་རིགས༌[^1534]མཐུན་པར་ཡོད་པ༌[^1535]དེ་བས་ན་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་དུ་སྨད་པ་མ་ཡིན་ནོ། །

[Block 1760]
འདིར་གཞུང་ནི་དགེ་ཚུལ་དག་ལ་སྣོད་དག་མེད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་དག་ལ་བཅངས་ཏེ་ལག་ཏུ་སྦྱིན་པར་བྱའོ། །

[Block 1761]
ལམ་དུ་འཇིགས་པ་དང་བཅས་ཤིང་འགྲོན་པ་དག་ཀྱང་ཐལ་ལམ་ཟས་བཅང་དུ་མི་རུང་ན་ལྷུང་བཟེད་བྱིན་གྱིས་བརླབས་པ་མི་གཏོང་བར༌[^1536]དེ་དག་དང་ལྷན་ཅིག་བཟའ་བར་བྱའོ༌[^1537]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1762]
གཡོག་རྣམས་ལ་བཅངས་ཏེ་སྦྱིན་ནོ། །

[Block 1763]
ཉེ་དུ་བཅུགས་པས་གསོལ་ན་ཐམས་ཅད་དུ་དབེན་པའི་ཕྱོགས་སུའོ་ཞེས་བྱ་བ་ནི། བཅུགས་པས་ལྷན་ཅིག་བཟའ་བར་གསོལ་ན་དེའི་ལམ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི། གནས་ཐམས་ཅད་དུ་ཡང་དབེན་པའི་ཕྱོགས་སུ་ལྷན་ཅིག་བཟའ་བར་བྱའོ། །

[Block 1764]
དེ་གཉིས་ལ༌[^1538]བྱིན་ལེན་བྱས་པ་འཇིག་པ་དང་བྱིན་ལེན་མ་བྱས་པ་དང་འདྲེས་པ༌[^1539]བསྲུང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེ་གཉིས་ཞེས་བྱ་བ་ནི་སྣོད་དག་ལའོ། །

[Block 1765]
གང་ཞིག་འདིར་དགེ་ཚུལ་དང་ཉེ་དུ་དེ༌[^1540]གཉིས་དང་དེ་དག་དང་ལྷན་ཅིག་བགོ་བར་བྱ་སྟེ། གང་ཡང་ཉེ་དུ་དང་ལྷན་ཅིག་བྱིན་གྱིས་བརླབས་ཏེའོ། །

[Block 1766]
ལྷུང་བཟེད་བྱིན་གྱིས་བརླབས་ཏེ་ལག་པ་དག་བསྙལ་དུ་བཅུག་ནས་སོ་ཞེས་བྱ་བ་ལ། དེ་ནི་དོན་གྱིས་ཐོབ་པར་རིག་པར་བྱ་སྟེ། དེའི་ཕྱིར་འདི་དོན་གྱིས་བརྗོད་པའོ། །

[Block 1767]
འདིར་ཉེ་དུ་རྣམས་ལ་ལག་པ་བསྙལ་དུ་བཅུག་པ་འདིར་གཞུང་ནི་ཕྱོགས་དབེན༌[^1541]པར་འདུག་སྟེ། ལག་པ་དག་བསྙལ་དུ་བཅུག་ནས་སྣོད་མི་བཏང་བར་བཟའ་བར་བྱའོ།[^1542] །འདི་ལ་འགྱོད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1768]
མཆིལ་ལྷམ་དང་བཅས་བཞིན་དུ་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གསོ་བའི་དོན་ཉིད་མ་གཏོགས་པར་རང་བཞིན་གྱི༌[^1543]ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་མ་ཡིན་པ་ལྷག་མ་ཐམས་ཅད་ལ་ཞེས་བྱ་བ་འདིས། ནད་པ་མཆིལ་ལྷམ་དང་བཅས་པ༌[^1544]ལ་བཟའ་བ་ཡོངས་སུ་ཐོབ་པ་ལ་བྱེ་བྲག་ཏུ་སྨོས་པ་ནི། ནད་པས་ནི་མནན་ཏེའོ་ཞེས་བྱ་བ་ལ། མཆིལ་ལྷམ་ཕུད་པའི་སྟེང་དུ་མནན་པར་རིག་པར་བྱའོ། །

[Block 1769]
འདིར་ནད་པ་ཞེས་བྱ་བ་ནི་ནད་པ་གང་ལ་རྐང་པ་ས་ལ་གཞག་ན་མི་འཕྲོད་པ་དེ་ནད་པ་ཡིན་ནོ་སྙམ་དུ་དོན་གྱིས་ཤེས་པར་བྱའོ། །

[Block 1770]
སྒྲེན་མོ་དང་གོས་གཅིག་པས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མི་ན་བར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1771]
ནད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ལ། འདིར་ནད་པའི་ཚད་ནི་མི་ནུས་པ་ལ་བྱ་སྟེ། དེ་ལྟ་བས་ན་མི་ནུས་པ་ལ་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 1772]
དེ་གཡོག་དག་གིས་སྐྱོར་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ནད་པ་དེའོ། །

[Block 1773]
འདིར་གཞུང་ནི། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྒྲེན་མོས་བཟའ་བར་མི་བྱའོ། །

[Block 1774]
ནད་པས་སྦྱོར་བར་མི་བཟོད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ནད་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 1775]
དེ་གཡོགས༌[^1545]གོས་ཀྱིས་སྐྱོར་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1776]
ནུས་ན་རྔུལ་གཟན་ལ་བརྟེན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་པས་ནུས་ན། ཆོས་གོས་སྟེང་མ་མེད་པར་བཟའ་བར་མི་བྱ་སྟེ། འདི་ལ་ཆོ་ག་འདི་སྙམ་དུ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 1777]
གསང་བའི་ཕྱོགས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ནད་པས་ནུས་ན་འཁོར་གསུམ་ཁེབས་པའི་མཐར་ཐུག་པའི་ཤམ་ཐབས་ལ་བརྟེན་པར་བྱ་སྟེ། གཉིས་ཀར་གཏོགས་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། འདིར་གཞུང་ནི་འཁོར་གསུམ་ཁེབས་པའི་ཚད་འདིས་ཕྱག་འཚལ་བ་ན་འོག་མའི་ཆ་སྦ་བར་བྱ་བའམ་ཉེ་བར༌[^1546]འཁོར་གང་ཞིག་གོས་དག་འཁོར་གསུམ་ཁེབས་པ་ཞེས་བྱ་བ་འདིའི་རྗེས་སུ་འབྲངས་ནས་ཤེས་པར་བྱའོ། །

[Block 1778]
ཟས་ཀྱི༌[^1547]ཕྱིར་འདུག་པས་འདིའམ་འདི་ནས་བྱིན་ཅེས་འདྲི་མ་མཁན་ལ༌[^1548]བསྒོ་བར་མི་བྱའོ། །

[Block 1779]
ནད་པས༌[^1549]འཕྲོད་པ་ལ༌[^1550]ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ནད་པས་ནད་པ་ལ་འཕྲོད་པ་ལ་ཁམས་སྙོམས་པར་འགྱུར་བའི་ཟས་འདི་བྱིན་ཅིག་ཅེས་མི་ནུས་པ་ལ། འདིར་རྣམ་པར་གནས་པའོ། །

[Block 1780]
འདིར་གཞུང་ནི་ནད་པ་ལ་གལ་ཏེ་ཁམས་སྙོམས་པར་འགྱུར་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 1781]
གཞུང་ཁ་ཅིག་ལས་དེའི༌[^1551]དཔེ་བསྟན་པའི་ཕྱིར། དཔེར་ན་དྲོད་ཆུང་བས་ཚོས་པ་དང་། དྲོད་ཆེ་བས་རློན་པ་ལྟ་བུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གོ་བར་བྱ་བ་ལ་ཞེས་བྱ་བ་དེ་གོ་བར་བྱེད་པ་ལ་ཞུ་བར་འགྱུར་བ་ལ་ཐ་དད་དུ་ཉེ་བར་གནས་པའོ། །

[Block 1782]
བདག་ཉིད་ལ་ནད་པའི་འདུ་ཤེས་དང་། ཟས་ལ་སྨན་གྱི་འདུ་ཤེས་ཉེ་བར་གཞག་སྟེ། བཟའ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། བདག་ཉིད་ལ་ཞེས་བྱ་བ་ནི་རང་ལའོ། །

[Block 1783]
འདི་ནི་མ་མོ་ལས།

[Block 1784]
མར་དང་ཆུ་དང་པོར་བྱས་ཏེ། དེ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པས་སོ། །

[Block 1785]
དྲན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་ངོ་། །ཟས་ལ་ཉེ་བར་གཞག་སྟེ་བཟའ་བར་བྱའོ། །

[Block 1786]
ཇི་ལྟར་ཞེ་ན་དེའི་ཕྱིར་འབྱུང་བ་དང་འདྲ་བ་དང་འགྱུར་བ་དང་ཕྱིར་རྒོལ་བ་ཉིད་དང་རྒྱུ་མཐུན་པ་དང་བརྟེན་པ་དང༌[^1552]རྣམ་པ་དང་བཙལ་བ་དང་། གཞན་ལ་རག༌[^1553]ལས༌[^1554]པ་ཉིད་དང་། སོ་སོར་འགྲོ་བ་དག་གི༌[^1555]མི་མཐུན་པ་ཉིད་དུ་གཞག་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འབྱུང་བ་ལ་སོགས་པ་རྣམ་པ་བཅུ་པོ་དེ་དག་གི་ཟས་ལས་མི་མཐུན་པའི་དྲན་པ་ཉེ་བར་གཞག་སྟེ། བཟའ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1787]
དེ་ལ་འབྱུང་བ་ཞེས་བྱ་བ་ནི་ཟས་ནི་མི་གཙང་བ་དང་། ལུད་པ་ལ་སོགས་པ་དག་ལས་འབྱུང་བའོ། །

[Block 1788]
འདྲ་བ་ཞེས་བྱ་བ་ནི་འདི་ལྟ་སྟེ། འབྲས་ཆན་ནི་སྲིན་བུ་དང་འདྲ་ལ། ཕྱེ་དག་ནི་རུས་ཕྱེ་དང་འདྲ་བ་ལ་སོགས་པའོ། །

[Block 1789]
འགྱུར་བ་ཞེས་བྱ་བ་ནི་ཟས་ཟོས་ན་བད་ཀན་དང་སྣབས་དང་རྣག་དང་ཁྲག་ལ་སོགས་པར་འགྱུར་བའོ། །

[Block 1790]
ཕྱིར་ཞེས་བྱ་བ་ནི་ཟས་ཀྱི༌[^1556]ཕྱིར་རྒོལ་བ་རྣམས་དང་རྗེས་སུ་འབྲེལ་བ་སྟེ།
--- END BLOCKS ---
