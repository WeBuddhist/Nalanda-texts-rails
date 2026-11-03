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
[Block 1786]
གཞན་ཡང་སྐྱེས་བུ་སྙན་དངགས་བྱེད་པའི་ཕྱིར། །སྐྱེས་བུ་ཐམས་ཅད་སྙན་དངགས་བྱེད་པར་འགྱུར་ལ། མི་བྱེད་ན་འགའ་ཞིག་ཀྱང་མི་བྱེད་པ་དེ་དང་འདྲ་བར་དེ་ལྟར་ན་རིག་པ་དེ་དག་ནི་སྔ་ན་མེད་པ་ཡིན་ནོ། །

[Block 1787]
སྔགས་བྱེད་པའི་སྒྲུབ་པར་བྱེད་པ་དང༌[^1308]བྲལ་བ་དག་སྔགས་མི་བྱེད་པ་ནི་བདེན་ན། ཚོགས་པ་དེ་ཡང་འགའ་ཞིག་ལ་ཡང་མ་མཐོང་སྟེ། སྐྱེས་བུ་རྣམས་ནི་ཆོས་མཚུངས་པ་ཅན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1788]
འདིར་སྔགས་ཞེས་བྱ་བ་བདེན་པ་ལ་སོགས་པ་དང་ལྡན་པའི་ཚིག་དང་དམ་བཅས་པ་ལས་གཞན་ཅུང་ཟད་ཀྱང་མེད་དོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1789]
དེ་དག་ཀྱང་སྐྱེས་བུ་འགའ་ཞིག་ལ་མཐོང་ངོ་། །སྐྱེས་བུ་ཐམས་ཅད་དེ་དང་བྲལ་བ་ཡིན་པ་དེ་ལྟ་ཡང་ངེས་པ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ཡོད་པ་ལ་འགལ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1790]
ལྐོག་ཏུ་གྱུར་པའི་རང་བཞིན་ཅན་དག་ལས་མི་དམིགས་པའི་ངེས་པའི་གཏན་ཚིགས་མ་ཡིན་ནོ། །

[Block 1791]
དྲན་པ་དང་བློ་དང་སོ་སོར་རིག་པ་དང་བདེན་པ་དང་ནུས་པ་ཐམས་ཅད་ལ་འགྱུར་བ་ཡང་མ་ཡིན་ནོ། །

[Block 1792]
དེ་སྒྲུབ་པར་བྱེད་པའི་ཡང་དག་པའི་མན་ངག་གི་ཁྱད་པར་འདྲ་བར་ཡོན་ཏན་གཞན་སྒྲུབ་པར་བྱེད་པ་དག་ཀྱང་ཡོད་པར་འགྱུར་རོ། །

[Block 1793]
ཡོད་དུ་ཟིན་ཀྱང་ཐམས་ཅད་མཐོང་བར་ནུས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1794]
དེ་ཉིད་ཀྱི་ཕྱིར་མ་མཐོང་བ་ལ་བསྙོན་དུ་མེད་དོ། །

[Block 1795]
སྐྱེས་བུ་རྣམས་ཡོན་ཏན་འགའ་ཞིག་བསྐྱེད་པར་འདོད་པ་ལ་ཡང་འགལ་བར་བྱེད་པ་མེད་དོ།[^1309] །གནོད་པར་བྱ་བ་མ་མཐོང་བས་གནོད་པར་བྱ་བ་དང་གནོད་པར་བྱེད་པ་ངོ་བོ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1796]
དེས་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་འགོག་པ་ལ་སོགས་པའི་ལན་ངེས་པར་བརྗོད་པ་ཡིན་ནོ། །

[Block 1797]
དེ་ལ་དེ་སྒྲུབ་པར་བྱེད་པའི་ཡང་དག་པའི་མན་ངག་མེད་པ་ཅན་འདི་ཅི་འདྲ་བ་གཞན་དག་ཀྱང་དེ་ལྟ་བུར༌[^1310]གྱུར་པ་ཡིན་ན། དེ་ལྟ་བུར་གྱུར་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རིགས་པ་ཡིན་གྱི་ཤེས་པར་བྱེད་པ་མ་མཐོང་བ་ཅན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཡང་མ་ཡིན་ཏེ། ཡོད་དུ་ཟིན་ཀྱང་འབྲས་བུ་རྩོམ་པ་མེད་པ་སྲིད་པའི་ཕྱིར་དང་། རང་བཞིན་གྱིས་བསྐལ་པ་རྣམས་ནི་མཐོང་བར་མི་ནུས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1798]
དེ་བས་ན་འདོན་པར་བྱེད་པ་ཡིན་པའི༌[^1311]ཕྱིར། འདོན་པར༌[^1312]བྱེད་པ་ནི་འདོན་པར་བྱེད་པ་གཞན་སྔོན་དུ་སོང་བ་ཅན་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འཁྲུལ་པ་ཡིན་ཏེ། བྷ་ར་ཏ་འདོན་པར༌[^1313]བྱེད་པ་ལ་ཡང་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1799]
རིག་བྱེད་ཀྱི༌[^1314]ཁྱད་པར་དུ་བྱས་པའི་ཕྱིར་སྐྱོན་མེད་པ་མ་ཡིན་ནམ་ཞེ་ན། རིག་བྱེད་འདོན་པར༌[^1315]བྱེད་པ་ལ་ཕུལ་དུ་བྱུང་བ་ཡང་ཅི་ཞིག་ཡོད་ན་གང་གིས་རྣམ་པ་གཞན་གྱིས་འདོན་པར་མི་ནུས་པ་ཡིན། མི་མཐུན་པའི་ཕྱོགས་དང་ཁྱད་པར་འགལ་བ་མེད་པ་འདི་ལས་གཏན་ཚིགས་ལྡོག་པར་བྱེད་པ་མ་ཡིན་ཏེ། འགལ་བ་མེད་པ་དག་ནི་གཅིག་ལ་སྲིད་པའི་ཕྱིར་རོ། །

[Block 1800]
གལ་ཏེ་ད་ལྟར་རྣམས་འདོན་པར་བྱེད་པའི་ཕྱིར་རོ་ཞེ་ན། དེའི་ལན་ནི་བཤད་ཟིན་ཏོ། །

[Block 1801]
གལ་ཏེ་མ་མཐོང་བའི་ཕྱིར་རོ་ཞེ་ན། འདི་ལ་ཡང་སྤངས་ཟིན་ཏོ། །

[Block 1802]
མ་མཐོང་བ་ཙམ་ཡང་མེད་པར་གོ་བར་བྱེད་པ་མ་ཡིན་པའི་ཕྱིར་འཁྲུལ་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1803]
དེ་བས་ན་ཁྱད་པར་ཕུལ་དུ་བྱུང་བ་ལ་བརྟེན་པ༌[^1316]མ་ཡིན་པའི༌[^1317]ཕྱིར། མ་བཟུང་བ་དང་མཚུངས་པ་ཡིན་ནོ། །

[Block 1804]
གང་ཅུང་ཞིག་རིག་བྱེད་འདོན་པར་བྱེད་པ་དེ་ཐམས་ཅད་ནི་རིག་བྱེད་འདོན་པ་གཞན་སྔོན་དུ་སོང་བ་ཅན་ཡིན་ནོ་ཞེས་བྱ་བའི་ཁྱབ་པ་ཡང་འགྲུབ་པ་མ་ཡིན་ཏེ། ཐམས་ཅད་དེ་ལྟ་བུའི་ངོ་བོར་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1805]
དེའི་རྒྱུ་མཚན་ཅི་འདྲ་བ་མཐོང་བ་དེ་ནི་དེ་ལྟར་ཡིན་ནོ་ཞེས་བྱ་བར་འགྱུར་ལ། ཁྱད་པར་མཐོང་བ་དེ་དོར་ཞིང་དེའི་རྒྱུ་མཚན་ཅན་ཉིད་ཀྱིས་སྤྱི་སྨོས་པ་ནི་བསྲེག་ཟ་སྒྲུབ་པ༌[^1318]ལ་རྫས་སྔོན་པོ་དང་འདྲ་བར་འཁྲུལ་པ་ཉིད་ཡིན་ནོ། །

[Block 1806]
འདིས་འདོད་ཆགས་ལ་སོགས་པ་ནི་གྲུབ་པར༌[^1319]བྱེད་པ་ལ་ཚིག་ལ་སོགས་པ་དག་གསལ་བ་ཡིན་ནོ། །

[Block 1807]
འདོན་པར་བྱེད་པ་འདི་འདོན་པར་བྱེད་པ་སྔོན་དུ་སོང་བ༌[^1320]ཅན་སྒྲུབ་པ་ཡིན་པར་ཡང་བླ་སྟེ།

[Block 1808 [VERSE]]
རྣམ་ཀུན་ཐོག་མེད་གྲུབ་འགྱུར་བ། །
དེ་ལྟར་སྐྱེས་མིན་རྟེན་ཅན་མིན། །
དེའི་ཕྱིར༌[^1321]སྐྱེས་བུས་མ༌[^1322]བྱས་ཉིད། །
གཞན་ཡང་མི་མིན༌[^1323]རྟེན་ཅན་འགྱུར། །

[Block 1809 [VERSE]]
སྐྱེས་བུ་བདག་ཉིད་ཀྱིས་བརྟགས་ནས་སམ། །
གཞན་ལས་འདོན་པར་བྱེད་པ་ན། །
བྱེད་པའི་བྱ་བ་མེད་པ་ཅན། །

[Block 1810]
དེ་དག་གི་སྒྲ་རང་ཉིད་སྒྲོགས་པར་བྱེད་པ་མ་ཡིན་ན་གང་གིས་ན་སྐྱེས་བུས་མ་བྱས་པར་འགྱུར། གལ་ཏེ་སྐྱེས་བུ་རྣམས་ཀྱི་ཐོག་མ་ཉིད་ཡོད་པར་འགྱུར་ན། །སྐྱེས་བུས་མ་བྱས་པ་ལ་ཡང་འགྱུར་རོ། །

[Block 1811]
དེའི་ཚེ་ཡང་གཞན་སྔོན་དུ་སོང་བ་ཅན་མི་འགྲུབ་སྟེ། འདོན་པར་བྱེད་པ་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 1812]
དེའི་དང་པོ་འདོན་པར་བྱེད་པ་ནི་བྱེད་པ་པོ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1813]
དེ་བས་ན་འདི་ནི་བྱིས་པ་ས་རྡུལ་གྱི་རྩེད་མོ་ལ་སོགས་པ་དང་འདྲ་བར་སྔ་མ་སྔ་མ་མཐོང་བས་འཇུག་པ་ཡིན་པས་ན། སྐྱེས་བུའི་ཐ་སྙད་ཐོག་མ་མེད༌[^1324]ཅན་དུ་འགྱུར་གྱི། སྐྱེས་བུས་མ་བྱས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1814]
ཐོག་མ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་ན་ནི། ད་ཤིན༌[^1325]ཏུ་མང་པོ་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་ནོ། །

[Block 1815]
དེ་ལྟར་ན།

[Block 1816 [VERSE]]
ཀླ་ཀློ་ལ་སོགས་ཐ་སྙད་དང་། །
མེད་པར་སྨྲ་བའི་ཚིག་རྣམས་ནི། །
ཐོག་མེད་ཕྱིར་ན་དེ་བཞིན་འགྱུར། །
སྔོན་ལེགས་བྱས་པའི་རྒྱུན་ཕྱིར་རོ། །

[Block 1817]
ཀླ་ཀློ་ལ་སོགས་པའི་ཐ་སྙད་མ་བག་མར་ལེན་པ་ལ་སོགས་པ་དང་། འདོད་པའི་དགའ་སྟོན་ལ་སོགས་པ་དང་། མེད་པར་སྨྲ་བའི་ཚིག་སྔ་ན་མེད་པ་དང་། འཇིག་རྟེན་ཕ་རོལ་ལ་སོགས་པ་ལ་སྐུར་བར་བྱེད་པ་དག་ཐོག་མ་མེད་པ་ཅན་ཡིན་ནོ། །

[Block 1818]
དེ་དག་ནི་གཞན་གྱིས་ལེགས་པར་མ་བསྒོས་ན་འཇུག་པར་མི་འགྱུར་རོ། །

[Block 1819]
བདག་ཉིད་ཀྱིས་སྤོབས་པས་བཀོད་པའི་བརྡ་བྱེད་པ་ཅན་དག་ཀྱང་དོན་ཇི་ལྟར་ཐོས་པ་བཞིན་དུ་རྣམ་པར་རྟོག་པས་བསྡུས་པའི་སྒོ་ནས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 1820]
དེ་ནི་འགའ་ཞིག་ལས་ཅུང་ཟད་འོངས་པ་ཡིན་ནོ་ཞེས་སྟོན་པར་བྱེད་པ་གཅིག་ནི་རྒྱུན་གྱིས་མེད་པའི་ཕྱིར། གཞན་སྔོན་དུ་སོང་བ་ཅན་མ་ཡིན་ནོ་ཞེས་བརྗོད་དེ། ཕལ་ཆེར་འཇིག་རྟེན་གྱི་ཐ་སྙད་དག་ཇི་ལྟར་མཐོང་བ་བཞིན་དུ་འཇུག་པ་ཅན་ཏེ། ཡང་དག་པ༌[^1326]ལོག་པར་འཇུག་པ་ཅན་དག་ཡིན་ནོ། །

[Block 1821]
ཐོག་མའི་བསྐལ་པ་པ་རྣམས་ལ་མཐོང་བ་ཉིད་མེད་པར་ཐ་སྙད་རྣམས་ལ་ཕྱིས་འཇུག་པར་འགྱུར་བར་འདོད་པ་མ་ཡིན་ནམ་མ་ཡིན་ཏེ། ལེགས་པར་བྱས་པ་གཞན་གྱིས་བསྒོས་པས་དེ་དག་གིས༌[^1327]ནི་རྐྱེན་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་སད་པའི་ཕྱིར་རོ། །

[Block 1822]
གལ་ཏེ་ཐམས་ཅད་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་འགྱུར་རོ་ཞེ་ན།

[Block 1823 [VERSE]]
དེ་འདྲའི་སྐྱེས་བུས་མ་བྱས་ཉིད། །
གྲུབ་ནའང་ཡོན་ཏན་ཅི་ཞིག་འགྱུར། །

[Block 1824]
རྣམ་པ་གང་གིས་མི་སླུ་བའི་ཕྱིར། སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་འདོད་ན་དེ་ནི་ཐོག་མ་མེད་པ་ཉིད་ཅན་དུ༌[^1328]ཡིན་པའི་ཕྱིར། སླུ་བར་བྱེད་པ་ལ་ལ༌[^1329]དག་ལ་ཡང་ཡོད་པས་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་ཀྱིས་ཅི་ཞིག་བྱ། རིག་བྱེད་ཀྱི་ངག་དག་ཁོ་ན་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་ན་ཡང་། དོན་ནི་འདུས་བྱས་ཁྱད་པར་རྣམས། །མཐོང་ཕྱིར་ཐེ་ཚོམ་དག་ཀྱང་ཡིན། གལ་ཏེ་སྐྱེས་བུས་བྱས༌[^1330]མ་བྱས་པ་ཉིད་ཡིན༌[^1331]ཡང་དེའི་དོན་གྱིས༌[^1332]སྤོབས་པ་སོ་སོར་ངེས་པ་བསྐྱེད་པར་འགྱུར་བ་ན་ཡིད་ཆེས་པར་འགྱུར་རོ། །

[Block 1825]
ཇི་ལྟར་འདོད་པ་བཞིན་དུ་སྒྲོ་འདོགས་པ་དང་སྐུར་པ་འདེབས་པ་དག་གིས་ངེས་པར་བརྗོད་པ་དང་དཔྱོད་པ་པ་ལ་སོགས་པ་དག་གིས་རིག་བྱེད་ཀྱི་ངག་རྣམས་ཐ་དད་པར་བྱེད་པར་མཐོང་ངོ་། །དོན་དེ་རྣམས་དེ་དག་མི་འཐད་པར་འགྱུར་བ་མ་ཡིན་ཏེ། དོན་ལ་འཇུག་པ་བརྡ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་དང་། ངག་གཅིག་ལ་ཡང་རྣམ་པར་རྟོག་པ་དུ་མ་སྲིད་པའི་ཕྱིར་དང་། རང་བཞིན་དང་རྐྱེན་རྣམས་ཀྱི་དོན་དུ་མར་བརྗོད་པའི་ཕྱིར་དང་། གྲོགས༌[^1333]སུ་ཟིན་ཀྱང་གཅིག་ཉིད་དུ་ཁས་མི་ལེན་པའི་ཕྱིར་དང་། མ་གྲགས་པའི་མང་བ་ཉིད༌[^1334]ཕྱིར་དང་། དེའི་དོན༌[^1335]སྐྱེས་བུས་བསྟན་པ་ལ་རག་ལུས་པའི་ཕྱིར་དང་། དེས་བསྟན་པ༌[^1336]ནི་དེའི་འདོད་པའི་རྗེས་སུ་འཇུག་པའི་ཕྱིར། རིག་བྱེད་ཀྱི་ངག་གི་དོན་རྣམས་ངེས་པ་ཁོ་ན་ཡིན་ནོ། །
--- END BLOCKS ---
