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
[Block 1856]
ལྟག་སྤྱོད་རྣམས་ལ་ནི༌[^1475]སྐྱོན་ལན་དུའོ། །

[Block 1857]
འདིས་ཕྱོགས་སྔ་མ་དག་སྒྲུབ་བྱེད་མ་ཡིན་པ་ཉིད་དུ་ཤེས་པར་མི་ནུས་སོ། །

[Block 1858]
དེ་ལ།

[Block 1859 [HEADING]]
### ཕྲད་པ་དང་མ་ཕྲད་པར་མཚུངས་པ། ^6-1-0

[Block 1860 [VERSE]]
ཕྲད་དང་མ་ཕྲད་དག་དང་དུས། །
གསུམ་ལ་རྟགས་སུ་བརྗོད་འདོད་མིན། །
ཕྲད་དང་མ་ཕྲད་རྟགས་བརྗོད་དེས།[^1476] །
མ་ཚང་གཏན་ཚིགས་རྗེས་མཐུན་ཡིན། །

[Block 1861]
དཔེར་ན་རྩོལ་བ་ལས་བྱུང་བའི་ཕྱིར་སྒྲ་མི་རྟག་གོ་ཞེས་གཏན་ཚིགས་ཀྱི་དཔེ་བརྗོད་པ་ལས་གལ་ཏེ་གཏན་ཚིགས་འདི་བསྒྲུབ༌[^1477]བྱ་དང་ཕྲད་ནས་སྒྲུབ་པར་བྱེད་ན་ནི་བསྒྲུབ་བྱ་དང་ཁྱད་པར་མེད་པར་འགྱུར་ཏེ། རླུང༌[^1478]གི་ཆུ་རྒྱ་མཚོ་དང་ཕྲད་པ་བཞིན་ནོ། །

[Block 1862]
མ་གྲུབ་པ་མ་ཡིན་ཏེ། གྲུབ་པ་དང་ཕྲད་ན་ནི་བསྒྲུབ་བྱ་གྲུབ༌[^1479]ཟིན་ནས་འདི་གང་གི༌[^1480]གཏན་ཚིགས་ཡིན། ཅི་སྟེ་མ་ཕྲད་ན་ནི་མ་ཕྲད་པས་གཏན་ཚིགས་མ་ཡིན་པ་རྣམས་དང་ཁྱད་པར་མེད་པའི་ཕྱིར་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་དེ་ལྟར་ཕྲད་པ་དང་མ་ཕྲད་པར་མཚུངས་པ་ཡིན་ནོ། །

[Block 1863 [HEADING]]
### གཏན་ཚིགས་མ་ཡིན་པ་མཚུངས་པ། ^6-2-0

[Block 1864]
དུས་གསུམ་ལ་ཡང་མི་འདོད་པར་བརྗོད་དེ།[^1481] གལ་ཏེ་གཏན་ཚིགས་བསྒྲུབ་བྱ་ལས་སྔར་སྒྲུབ་པར་བྱེད་ན་ནི་བསྒྲུབ་བྱའམ་གྲུབ༌[^1482]ན་འདི་གང་གི༌[^1483]གཏན་ཚིགས་ཡིན། ཅི་སྟེ་ཕྱི་ནས་བསྒྲུབས༌[^1484]ན་ནི་མ་གྲུབ་པའི་ཕྱིར་གཏན་ཚིགས་མ་ཡིན་ནོ། །

[Block 1865]
དེ་སྟེ་ཅིག་ཅར་བ་གཏན་ཚིགས་ཡིན༌[^1485]ནི། གཏན་ཚིགས་བཞིན་དུ་ཡོད་པ་དེ་སྒྲུབ་མི་དགོས་ཏེ། གླང་གི་རྭ་གཡས་གཡོན་བཞིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1866]
དེ་ལྟར་གཏན་ཚིགས་མ་ཡིན་པ་མཚུངས་པ་ཡིན་ནོ། །

[Block 1867]
དེ་དག་ནི་མ་ཚང་བའི་གཏན་ཚིགས་ཉིད་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 1868]
གང་གི་ཕྱིར་ཞེ་ན། རིགས་པ་དང་མི་ལྡན་པའི་དཔེ་བརྗོད་ཀྱི་གཏན་ཚིགས་ཐམས་ཅད་བསལ་བའི༌[^1486]ཕྱིར་རོ། །

[Block 1869]
གང་ཞིག་འདིར་མ་ཕྲད་པ་ཙམ་ཆོས་མཐུན་པས་གཏན༌[^1487]ཚིགས་ཀྱི་མཚན་ཉིད་མཚུངས་པར་འགྱུར་བ་ག་ལ་རིགས། རིགས་སུ་ཟིན་གྱིས་ཀྱང་གཏན་ཚིགས་མ་ཡིན་པས་འགྱུར་བ་ཡིན་ནོ། །

[Block 1870]
དེ་བཞིན་དུ་སྔར་རྟགས་ཀྱིས༌[^1488]སྒྲུབ་པར་བྱེད་ན་ཐ་སྙད་ཙམ་མ་དམིགས་པའི་ཕྱིར་སྒྲུབ་བྱེད་མ་ཡིན་ནོ་ཞེས་པ་ལ་ཡང་ངོ་། ། རང་ལ་གནོད་པའི་ཉེས་པར་འགྱུར་བ་ནི་འདིར་དགག་པ༌[^1489]ལའང་མཚུངས་པའི་ཕྱིར་རོ། །

[Block 1871]
དེ་ལྟར་ན་རེ་ཞིག་དང༌[^1490]བློའི་གཏན་ཚིགས་དག་ལ་བསྒྲུབ་པར༌[^1491]བྱ་བའི་གཏན་ཚིགས་ཀྱི་མཚན་ཉིད་གསུམ་མ་ཚང་བ་ལྟར་སྣང་བ་ཡིན་ནོ། །

[Block 1872]
དོན་རྟོགས་མ་གྲུབ་ལྟར་སྣང་ཡིན། །གང་གི་ཚེ་དོན་གཏན་ཚིགས་ཡིན་པ་དེའི་ཚེ་ནི་ཚིག༌[^1492]ལས་ཡིན་པ་མ་བཀག་པའི་ཕྱིར་དེ་དོན་ལ་མ་གྲུབ༌[^1493]ལྟར་སྣང་བ་ཉིད་དེ། ཆོས་ཐམས་ཅད་ཀྱི་གཏན་ཚིགས་རིགས་པ་མ་ཡིན་པས་བསལ་བའི་ཕྱིར་སྔ་མ་བཞིན་ནོ། །

[Block 1873]
གཏན་ཚིགས་གཉིས་ཀའི་ལྟར་ན་ཡང་དོན་བསྒྲུབ་པར་བྱ་བ་ལ་དེ་དག་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་མ་ཡིན་པའི་ཕྱིར་དེ་དག་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1874]
རིགས་སུ་ཆུད༌[^1494]མོད་ཀྱང་སེལ་བར་བྱེད་པའི་རང་བཞིན་གྱིས་སུན་འབྱིན་དུ་འགྱུར་རོ། །

[Block 1875 [HEADING]]
### རྟག་པ་མཚུངས་པ། ^6-3-0

[Block 1876 [VERSE]]
རྟག་བརྗོད་མི་རྟག་པ་རྗེས་འགྲོ། །
དེ་དག་མི་རྟག་པར་ནུས་མིན། །
ཕྱོགས་ཀྱི་སྐྱོན་དང་རྗེས་མཐུན་འགྲོ།[^1495] །

[Block 1877]
དཔེར་ན་སྒྲ་མི་རྟག་ཅེས་བྱ་བ་ལ་དེའི་རྟག་པའི་རྟག་པ་དང་སྦྱོར་བར་འགྱུར་ཏེ། ཆོས་རྣམས་ཀྱི་རང་བཞིན་གང་འཐོབ་པ་མི་འདོར་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1878]
དེ་ལྟ་བས་ན་རྟག་པ་ཉིད་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་ལྟ་བུ་སྟེ། དེ་དག་ཉིད་ནི་བརྟགས༌[^1496]པ་དང་མཚུངས་པའི་ལྟག་ཆོད༌[^1497]ཡིན་ནོ། །

[Block 1879]
འདི་ནི་དམ་བཅའ་བའི་སྐྱོན༌[^1498]ལྟར་སྣང་བའོ། །

[Block 1880]
མི་རྟག་པ་ཉིད་གཏན་ནས་ཞེན་པའི་ཕྱིར་དེ་ལ་མི་རྟག་པ་ལས་གཞན་ཡང༌[^1499]རྟག་པའི་འཇུག་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1881]
དངོས་པོ་དེ་ཉིད་མ་བྱུང་བ་ལས་བྱུང་བར་གྱུར་པ་ནི་མི་རྟག་པའོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1882]
གནས་སྐབས་དེ་ཡང་མི་རྟག་པ་ཉིད་དོ་ཞེས་དངོས་པོའི་རྐྱེན་གྱིས་བརྗོད་པར་བྱ་སྟེ། འབྲས་བུ་ཉིད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 1883 [HEADING]]
### མ་བརྗོད་པ་མཚུངས་པ། ^6-4-0

[Block 1884 [VERSE]]
སྔར་བརྗོད་གཏན་ཚིགས་མེད་པ་ཡིས། །
བསྒྲུབ་བྱ་མེད་པར་ཐལ་བར་འགྱུར། །

[Block 1885]
ཡང༌[^1500]བརྗོད་པ་མཚུངས། དཔེར་ན་སྔར་བཞིན་བྱས་པ་ལ་གལ་ཏེ་གཏན་ཚིགས་འདི་ལས་མི་རྟག་པ་ཡིན་ན་སྔར་བརྗོད་པ་དེ་དག་མེད་དེ། གཏན་ཚིགས་མེད་པའི་ཕྱིར་མི་རྟག་པར་བསྒྲུབ༌[^1501]མི་ནུས་སོ་ཞེས་བྱ་བ་ནི་མ་བརྗོད་པ་མཚུངས་པའོ། །

[Block 1886]
འདི་ལ་ཡང་། སྒྲོ་བཏགས་ནས། སྨྲ་པོའི་ངག་གིས་སྒྲུབ་པར་བྱེད། །མ་གྲུབ་ལྟར་སྣང་། དོན་ལ་ནི་སྔར་སྨྲ་བ་པོ༌[^1502]རང་ལ་རྗེས་སུ་དཔག་པར་བྱ་བའི་ངེས་པ་སྐྱེས་པ་བཞིན་གཞན་ལ་ངེས་པ་བསྐྱེད་པར་འདོད་པས། དོན་དེ་གཞན་ལ་བརྗོད་པ་དེ་མེད་པ་ལ་མ་གྲུབ་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1887]
གཞན་ལ་ནི་སྨྲ་བ་པོའི་ཚིག་གིས་དོན་སྒྲུབ་པ་ལ་སྨྲ་བ་ལས་སྔར་སྒྲོ་བཏགས་ནས། དེ་མེད་པ༌[^1503]ལས་དོན་མ་གྲུབ་པར་རྩོད་པ་ཡིན་ནོ། །

[Block 1888]
དེས་ན་དེ་དག་ནི་མ་གྲུབ་པ་ལྟར་སྣང་བའོ། །

[Block 1889]
ཡང་ན་ཉུང༌[^1504]ལྟར་སྣང་། བརྗོད་པ་ལས་སྔར་སྒྲུབ་བྱེད་ནའོ། །

[Block 1890]
བརྗོད་པ་ལས་སྔར་སྒྲུབ་བྱེད་ཡིན་པར་ལྷག་པར་སྒྲོ་བཏགས་པའི་ཕྱིར་གཏན་ཚིགས་མ་ཚང་བར་ལྟར་སྣང་བའོ། །

[Block 1891]
གྲུབ་པའི༌[^1505]དུས་ན་ནི་གཏན་ཚིགས་མ་བརྗོད་ན་གཏན་ཚིགས་མ་ཚང་བར་འགྱུར་ན་འདི་ནི་མ་བརྗོད་པ་ལས་སྔར་སྒྲུབ་པར་མི་བྱེད་དོ། །

[Block 1892]
འདིར་གཏན་ཚིགས་ཀྱི་དོན་མ་ལུས་པ་མེད་པར་བརྩད་པའི་ཕྱིར་དཔེ་བརྗོད་མ་ཚང་བ༌[^1506]ལྟར་སྣང་བ་ཉིད་དུ་ཡང་རིག་པར་བྱའོ། །

[Block 1893 [HEADING]]
### མ་སྐྱེས་པ་མཚུངས་པ། ^6-5-0

[Block 1894]
བརྗོད་པ་ལས་སྔར་རྟགས་མིན་ཕྱིར། །མ་གྲུབ་པ་དང་འགལ་བའི་ངག །

[Block 1895]
མ་སྐྱེས་པ་མཚུངས། དཔེར་ན་སྔར་བཞིན་བྱས་པ་ལ་གལ་ཏེ་འདི་ལྟར་བརྗོད་པ་ལས་སྔར་སྒྲ་བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་མ་ཡིན་པས༌[^1507]འགྱུར་རོ། །
--- END BLOCKS ---
