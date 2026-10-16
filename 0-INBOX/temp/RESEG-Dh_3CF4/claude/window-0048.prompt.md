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
གསུམ་པ་ནི༌[^956]ཕུན་སུམ་ཚོགས་པ་ཡིན་ན་ནི་སྦྱིན་པ་ཕུན་སུམ་ཚོགས་པར་འགྱུར༌[^957]ཏེ། དེ་ལ་ལེན་པ་པོ་ཡོན་ཏན་མེད་པའི་དབང་དུ་བྱས་ནས། སྐྱེ་དགུ་རྣམས་ལ་གནོད་པ་གང་དང་གང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 1682]
སྦྱིན་པ་པོ་དང་སྦྱིན་པའི་དབང་དུ་བྱས་ནས། རྒྱལ་སྲིད་དཔལ་འདི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 1683]
དེ་ལས་སྐྱེ་དགུ་ལ་ཕན་པའི་དབང་དུ་བྱས་ནས། རྒྱལ་སྲིད་དཔལ་འདི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་དང་པོའོ། །

[Block 1684]
དེ་བས་བདག་གི་ཤ་སྦྱིན་སྩོལ་བའི་ཞེས་བྱ་བ་ནི་སྦྱིན་བའི༌[^958]དངོས་པོའི་དབང་དུ་བྱས་པ་སྟེ། བདག་གི་ཤ་སྦྱིན་པར་སྩོལ་བ་ཐོང་ཤིག་ཅེས་བྱ་བ་ནི་རང་གི་ཤ་སྦྱིན་པ་ལ་སྩོལ་བ༌[^959]ནི་རང་གི་ཤ་སྦྱིན་པ་ལ་སྩོལ་བའོ།[^960] །བདག་གི༌[^961]ཤ་སྦྱིན་པར་སྩོལ་བ་ཉིད་ནི་བདག་གི་ཤ་སྦྱིན་པར་སྩོལ་བ་སྟེ། ངེས་པར་བཟུང་བ༌[^962]ནི་སྩོལ་བ་དང་གཏོང་བ་དང༌[^963]སྦྱིན་པ་རབ་ཏུ་དགག་པ་སྟེ། རང་གི་ཤ་སྦྱིན་པ་ནི་ངེས་པར་བཟུང༌[^964]བའོ། །

[Block 1685]
གཞན་གྱི་ཤ་སྦྱིན་པ་ནི་དགག་པ་མ་ཡིན་ནོ། །

[Block 1686]
འདིས་ནི་འདི་ལྟར་སྟོན་པ་ཡིན་ཏེ། གལ་ཏེ་འདི་ལྟར་སྦྱིན་པར་བྱ་བ་ཡིན་ན་ནི་དགྲ་ལ་སོགས་པ་སྦྱིན་པར་བྱ་བ་སྟེ། གལ་ཏེ་ངེས་པར་ཤ་ཉིད་སྦྱིན་པར་བྱའོ་ཞེ་ན། གཞན་དག་གི་ཤ་ཉིད་སྦྱིན་པར་བྱ་སྟེ། འདི་ཉིད་ངེས་པར་བཟུང༌[^965]བའོ། །

[Block 1687]
སྨྲས་པ། ལོག་པའི་ལམ་དུ་ཡིད་དམ༌[^966]བཅས་པ་ཞེས་སྨོས་ཏེ། ལམ་མ་ཡིན་པ་ལ་ངེས་པར་བྱས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1688]
[^967]དུ་ཞེས་བྱ་བ་ནི་རྒྱུའི་དོན་ཏོ། །

[Block 1689]
ལོག་པའི་ལམ་དུ་ཡིད་དམ༌[^968]བཅས་པ༌[^969]ཉིད་བསྒྲུབ་པའི༌[^970]ཕྱིར་སྐྱེས་བུ་དཔའ་བོ་ཁྱོད་ཀྱི་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 1690]
མི་བཟོད་པ་ནི་དང་དུ་ལེན་པར་མི་ནུས་པ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། ཁྱོད་ཀྱི་མཐུས་བསྐྱབས༌[^971]ཞེས་བྱ་བ་ནི།[^972] ཁྱོད་ཀྱི་མཐུས་བསྐྱབ་པའི་ཕྱིར་མི་བཟོད་དོ། །

[Block 1691]
འཇིག་རྟེན་ཞེས་བྱ་བ་ནི་ག་ལས་ཤེ་ན། དེ་བསྒྲུབ་པའི༌[^973]ཕྱིར་གཉིས་པའི་དོན་ཏོ། །

[Block 1692]
ཕུང་བར་བྱེད་པ་ལ་མཁས་པ་ནི་མཁས་པ་སྟེ། འཇིག་རྟེན་ཕུང་ཞིང་གནོད་པར་བྱེད་པ་ལའོ། །

[Block 1693]
དེ་ཡང་གནོད་པ༌[^974]ནི་སྐྱེ་བ་གཞན་དུ་དུས་མཐའ་མེད་པར་ངན་སོང་གནོད་པའོ། །

[Block 1694]
ཕུང་བར་བྱེད་པ་ལ་མཁས་པ་དེས་ཚུལ་གྱིས་ཞེས་སྨྲས༌[^975]སོ། །

[Block 1695]
ཁྱོད་ཀྱི་ཤ་དང་ཁྲག་སློང་བའི་ཚུལ་གྱིས་སོ། །

[Block 1696]
ཚུལ་མིན་སྐྱེ་དགུ་ཞེས་བྱ་བ་ནི་དེས་ཕུང་བ་ནི་གང་གི་ཕྱིར་སྐྱེ་དགུ་རྣམས་རྒུད་པར་འགྱུར་བའོ། །

[Block 1697]
ཡང་ན་ཚུལ་མིན་སྐྱེ་དགུ་ནི་ཁྱོད་ཀྱི་མཐུས་བསྐྱབས་པའི་འཇིག་རྟེན་མི་བཟོད་ཅིང་ཁྱོད་དང་བྲལ་བར་མི་བཟོད་པའོ། །

[Block 1698]
དེ་ལྟར་ཐབས་འདིས་སྐྱེ་དགུ་ཚུལ་མ་ཡིན་པར་ཕུང་བར་འདོད་པའོ། །

[Block 1699]
ད་ནི་རང་ཉིད་ཀྱི་ཤ་ཉིད་གཏང་བར་བྱའོ་ཞེས་འདིས་ངེས་པར་གཟུང་བ་སྐབས་དང་བཅས་པས་ཤ་ནི་གཞན་གྱི་སྦྱིན་པར་བྱའོ་ཞེས་འདིས་འདོད་པ་ཡིན་ཏེ། དེས་ན་བློན་པོ་ལ་སོགས་པས་ངེས་པར་བཟུང་བ༌[^976]དོན་མེད་པར་མཐོང་བ་སྟེ། མཆོད་སྦྱིན་ཚེན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་སྨོས་སོ། །

[Block 1700]
ཚིལ་དང་ཞག་ལ་སོགས་པའི་བཟའ་བ་གང་ཡིན་པ་དེ་ནི་ཚིལ་དང་ཞག་ལ་སོགས་པའོ། །

[Block 1701]
འདིས་ནི་སྦྱིན་པའི་དངོས་པོའི༌[^977]གྱ་ནོམ་པ་བསྟན་ཏོ། །

[Block 1702]
སུམ་ཅུ་རྩ་གསུམ་ཞེས་བྱ་བ་འདིས་ན༌[^978]ལེན་པ་པོ་བསྟན་ཏོ། །

[Block 1703]
བསྲེགས་པ༌[^979]ཞེས་བྱ་བ་ནི་མེ་ལ་བསྲེགས་པའི་ཕྱིར་ཏེ་གུས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 1704]
མགུ་ཞེས་བྱ་བ་འདིས་ནི་ལེན་པ་རྗེས་སུ་འཛིན་པ་ཉིད་དུ་བསྟན༌[^980]ཏོ། །

[Block 1705]
གུས་པར་བྱིན་ཡང་ཞེས་བྱ་བ་ནི་མེ་ལ་མངོན་པར་བསྲེགས་པ་གུས་པ་མེད་པ་དེའི་གཉེན་པོ་ཡིན་ནོ། །

[Block 1706]
ཁྱོད་ཀྱིས༌[^981]ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པ་པོའི་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1707]
ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་འདིས་ནི་ཚིལ་དང་ཞག་ལ་སོགས་པ་ཞེས་བྱ་བ་བསྟན་པ་དེའི་གཉེན་པོ་སྦྱིན་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1708]
འདོད་མི་འགྱུར་ཞེས་བྱ་བ་འདིས་ནི་མགུ་བའི་མི་མཐུན་པའི་ཕྱོགས་བསྟན་ཏོ། །

[Block 1709]
མོད་ཀྱི་ཞེས་བྱ་བ་ནི་འོན་ཀྱང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1710]
ལྷའི་ཐུགས་ནི་བདག་ཅག་ལྟ་བུའི་སྐྱེ་བོས༌[^982]བཅོམ་པ་མ་ལགས་ཞེས་བྱ་བ་ནི་འདི་སྦྱིན་པར་བྱ། འདི༌[^983]ནི་སྦྱིན་པར་མི་བྱ་ཞེས་སོ། །

[Block 1711]
གལ་ཏེ་དེ་ལྟ་ན་ཅིའི་ཕྱིར་བདག་གི་ཤ་སྦྱིན་སྩོལ་བ་ཐོང་ཞེས་སྟོན་ཅེ་ན། དེའི་ལན་བསྟན་པའི་ཕྱིར། བདག་གི་དོན་དུ་གཅེས་པའི་སླད་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 1712]
རྐོ་ལོང་གསོལ་བར་གྱུར་ཏོ༌[^984]ཞེས་བྱ་བ་ནི་འདི་ལ་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བའི་རྐོ་ལོང་གསོལ་བར༌[^985]གྱུར་པའོ། །

[Block 1713]
དེ་ལྟར་འདས་པའི་ཚིག་དེས་ནི་དོན་མེད་པ་ཉིད་དུ་བསྟན་པ་སྟེ། རང་གི་ཤ་སྦྱིན་པའི་དབྱེ་བ་དང་ལྡན་པའོ། །

[Block 1714]
ད་ནི་རང་གི་ཤ་སྦྱིན་པ་མ་ཡིན་པ་ཉིད་ལས་བརྩམས་ཏེ། གནོད་སྦྱིན་ལྔ་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 1715]
ལྔ་པོ་ཞེས་བྱ་བ་ནི་ཉུང་བ་ཉིད་དོ། །

[Block 1716]
ཐམས་ཅད་ཅེས་བྱ་བ་ནི་དེའི་གཉེན་པོ་སྟེ༌[^986]མང་པོའོ། །

[Block 1717]
འདི་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་མཚན་ཉིད་ཀྱི་སྐྱེ་དགུ་ལ་ཕན་པར་འཇུག་པའི་མཚན་ཉིད་དེ། དེའི་གཉེན་པོའི༌[^987]འབངས་ཞེས་སྨོས་ཏེ། ཁྱད་པར་མེད་པས་བཟང་པོ་དང་། བར་མ་དང་། ཐ་མའི་འགྲོ་བ་དག་གོ། །

[Block 1718]
འདི་ལྟ་བུ་ཆོས་གང་གི་ལམ་ལགས༌[^988]ཞེས་བྱ་བ་ནི་སྔོན་མ་ཐོས་པའི་ཆོས་ཀྱི་ལམ་མོ། །

[Block 1719]
བདག་ཅག་ལ་ཞེས་བྱ་བ་ནི་བདག་གི་དོན་ནི༌[^989]དྲུག་པའོ། །

[Block 1720]
དེ་ལ་ཤ་དང་ཁྲག་ཅེས་བྱ་བ་དེ་ལ་ནི་འདི་དག་ལ་ཤ་དང་ཁྲག་ཡོད་བཞིན་དུ་ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་སོ། །
--- END BLOCKS ---
