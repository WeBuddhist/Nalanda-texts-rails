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
[Block 1856 [VERSE]]
ཐམས་ཅད་ཅིག་ཅར་ཐོས་ན༌[^1354]ཡང་། །
དུས་ཀྱི་ཐ་དད་མི་རུང་ངོ་། །

[Block 1857]
ཡན་ལག་གཞན་ལ་ལྟོས་པ་མེད་པར་ཡང་ཡན་ལག་གཅིག་ཁོ་ན་ལ་ངག་གི་དོན་གྲུབ་པའི་ཕྱིར། ངག་གི་ཡན་ལག་དུ་མ་ཉིད་ཉམས་པར་མ་གྱུར་ཅིག་སྙམ་པས་ཅིག་ཅར་ཡན་ལག་ཐམས་ཅད་ཐོས་པར་འདོད་ན། དེའི་ཚེ་ཡང་དུས་ལ་སྡོད་པ་མི་རིགས་པ་ཁོ་ན་ཡིན་ཏེ། ཡན་ལག་གཅིག་རྟོགས་པའི་དུས་ཉིད་ན་ཐམས་ཅད་ཐོས་པའི་ཕྱིར་རོ། །

[Block 1858]
རིམ༌[^1355]བཞིན་དུ་ཐོས་པ་ཡིན་ན་ཡང་དོན་ཐ་དད་པ་དང་ལྡན་པ་དག་ནི་གཅིག་ཉིད་ལས་དེའི་དོན་གྲུབ་པའི་ཕྱིར། གཞན་ནི་དོན་མེད་པ་ཅན་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ།[^1356] །ཅིག་ཅར་ཐོས་ན་ཡང་དོན་ཐ་དད་པ་དག་ལ་མཐོང་བའི་ནུས་པ་མེད་པ་ཅན་དག་གི་དོན་དང་ལྡན་པ་ཉིད་ཀྱང་མི་འགྲུབ་པོ། །གལ་ཏེ་ཚོགས་པ་རྣམས་ཀྱི་དོན་མཐོང་བའི་ཕྱིར་སྐྱོན་མེད་དོ་ཞེ་ན། མ་ཡིན་ཏེ། ཐ་དད་པ་ལ་ཡོད་པ་མ་ཡིན་པའི་ངོ་བོའི་ཚོགས་པ་ལ་ཡང༌[^1357]མི་སྲིད་པའི་ཕྱིར་དང་། དོན་གཞན་མི་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1859]
རེ་ཞིག་སྒྲ་སྐྱེ་བར་སྨྲ་བ་ལ་སྐྱོན་འདི་ཉིད་ཡོད་པ་མ་ཡིན་ཏེ། སོ་སོར་ནུས་པ་མེད་པའི་ཡན་ལག་རྣམས་ཀྱང་ཕན་འདོགས་པའི་ཁྱད་པར་ལས་ཕུལ་དུ༌[^1358]བྱུང་བ་དང་ལྡན་པའི་འབྲས་བུའི་ཁྱད་པར་ལས་ཉེ་བར་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 1860]
ཡན་ལག་རེ་རེ་ནུས་པ་ཡོད་པ་ཡིན་ན་ཡང་གཞན་དུ་རྟོགས་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 1861]
ཅི་སྟེ་ཡང་དག་གཅིག་ཁོ་ན་ཡིན་ལག་མེད་པ་ཅན༌[^1359]ཡིན་ན། དེ་ལ།

[Block 1862 [VERSE]]
གཅིག་ཉིད་ནི༌[^1360]ཡང་ཐ་དད་མེད། །
གོ་རིམས་འཛིན་པ་མི་སྲིད་ཕྱིར། །
དུས་ཐ་དད་ཉིད་མི་རུང་ངོ་། །

[Block 1863]
གཅིག་ལ་ནི་གོ་རིམས་བཞིན་དུ་རྟོགས་པ་མི་རིགས་ཏེ། གཟུང་བ་དང་མ་བཟུང་བ་དག་ཐ་དད་པ་མེད་པས་བཟུང་བ་དང་མ་གཟུང་བ༌[^1361]མེད་པའི་ཕྱིར་རོ། །

[Block 1864]
རིམ་བཞིན་དུ་ངག་རྟོགས་པ༌[^1362]ཡང་མཐོང་སྟེ། ངག་ཐམས་ཅད་ཀྱི་ཐ་སྙད་དང་ཐོས་པ་དང་འདྲེན་པའི་དུས་སུ་མིག་ཏུ་མཚུངས་པ་སྐད་ཅིག་མ་དུ་མ་ཅན་གྱི་གོ་རིམས་ཀྱིས་ཡོངས་སུ༌[^1363]རྫོགས་པའི་ཕྱིར་རོ། །

[Block 1865]
ཡི་གེའི་ངོ་བོ་ལ་མ་རེག་པ་ཅན་དང་བློ་གཅིག་ལ་སྣང་བ་ཅན་གྱི་སྒྲའི་བདག་ཉིད་ནི་མི་སྣང་པའི་ཕྱིར་ཏེ། ཡི་གེའི་གོ་རིམས་ཀྱིས་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 1866]
དེ་ཁྱད་པར་མེད་པ་ཡིན་ན་ཡང་ངག་གི་ཁྱད་པར་གོ་རིམས་བཞིན་དུ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར། ངག་གོ་རིམས་དང་ལྡན་པ་རྟོགས་པ་ཡིན་ནོ། །

[Block 1867]
ཡི་གེའི་གོ་རིམས་ཀྱི༌[^1364]ཕན་བཏགས་པ་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར་དང་། གང་ཇི་ལྟར་ཡང་རུང་བ་དེ་དག་རབ་ཏུ་སྦྱར་བ་དག་གིས་སམ།[^1365] ཡི་གེ་མེད་པ་དག་གིས་ཀྱང་ངག་རྟོགས་པར་འགྱུར་རོ། །

[Block 1868]
གོ་རིམས་དང་ལྡན་པ་དེ་དག་གིས་གོ་རིམས་མེད་པ་ལ་ཕན་འདོགས་པ་མི་རུང་བའི་ཕྱིར་དང་། གོ་རིམས་མེད་པར་རྗོད་པར༌[^1366]མི་ནུས་པ་ཉིད་ཀྱི་ཕྱིར་དང་། རྣམ་པ་གཞན་མེད་པའི་ཕྱིར་རོ། །

[Block 1869]
ངག་ལ་ཡི་གེ་དག་ཡོད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1870]
གལ་ཏེ་སྒྲའི་ངོ་བོ་གཅིག་པོ་དེ་ཉིད་ནི་གསལ་བྱེད་ཀྱི་གོ་རིམས་ཀྱི་དབང་གིས་གོ་རིམས༌[^1367]དང་ལྡན་པ་དང་། ཡི་གེའི་རྣམ་པར་དབྱེ་བ་དང་ལྡན་པར་སྣང་ངོ་ཞེ་ན། གསལ་བྱེད་གོ་རིམས་དང་ལྡན་པས་གསལ་བྱ་གོ་རིམས་མེད་པ་སྤངས་ཟིན་ཏེ། གསལ་བ་དང་གསལ་བ་མ་ཡིན་པ་འགལ་བའི་ཕྱིར་རོ། །

[Block 1871]
ངག་ཡི་གེ་དང་ཆ་མེད་པ་ཅན་ཡིན་ན་མ་ལུས་པར་ཐོས་པ་མེད་པར་ངག་མཉན་པར་མི་འགྱུར་ཏེ། གཅིག་ལ་ཆ་མེད་པའི་ཕྱིར་རོ། །

[Block 1872]
ཡང་འགའ་ཞིག་ཀྱང་ཆ་མེད་པ་མཉན་པར༌[^1368]མི་འགྱུར་རོ། །

[Block 1873]
ཡི་གེ་མ་ལུས་པ་ལེགས་པར་བྱས་པ་དང་ལྡན་པའི་བློ་ཐ་མས་ངག་ངེས་པར་གཟུང་ངོ་ཞེས་བྱ་བ་ཡང་ལོག་པ་ཡིན་ཏེ། ཡི་གེའི་ངོ་བོ་ལ་མ་རེག་པ་དེ་ལ་འགའ་ཞིག་ཀྱང་འགའ་ཞིག༌[^1369]གི་ཚེ་རྟོགས་པ་མེད་པའི་ཕྱིར་དང་། ཡི་གེ་རྣམས་ཀྱང་གོ་རིམས་མེད་པར་རྟོགས་པ་མེད་པའི་ཕྱིར་གང་ལས་ངག་ཅེས་བྱ་བ་གོ་རིམས་མེད་པ་བློ་གཅིག་གིས་གཟུང་བར་བྱ་བ་ཡིན། ཡི་གེ་ཐ་མ་རྟོགས་པ་ལས་ཕྱིས་ཀྱང་སྒྲའི་བདག་ཉིད་ཆ་མེད་པ་གཞན་ཉེ་བར་རྟོགས་པ་མ་ཡིན་ཏེ། སྨྲ་བ་པོ་བདག་ཉིད་འདིས་ཀྱང་ངེས་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1874]
གལ་ཏེ་འདི་ལྟར་བློ་ཐ་མལ་སྒྲ་ཆ་ཤས་རྫོགས་པ་ཡན་གར་བ་སྣང་བར་འགྱུར་ན། ལེགས་པར་འགྱུར་བ་དེ་ལྟར་ན་དགེ་བ་འདོད་པས་རྨོངས་པའི་བློ་ཅན་རྨི་ལམ་བཞིན་དུ་སྤྱོད་དོ། །

[Block 1875]
ཚིག་དང་ངག་དྲན་པར་གྱུར་པ་དག་ལ་ཡང་ཡི་གེའི་གོ་རིམས་ཀྱི་ཁྱད་པར་ངེས་པར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 1876]
བློ་གོ་རིམས་མེད་པ་ཅན་དག་ལ་སྔ་ཕྱི་མེད་པའི་ཕྱིར། དེས་བྱས་པའི་ཚིག་དང་ངག་གི་ཁྱད་པར་དེ་དག༌[^1370]ཁྱད་པར་མེད་པར་འགྱུར་རོ། །

[Block 1877]
ཡི་གེའི༌[^1371]གོ་རིམས་མེད་པ་ཅན་གྱི་སྒྲའི་ངོ་བོ་གཞན་མ་མཐོང་ངོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1878]
ཡོད་ན་ཡང་དེ་མི་རྟག་པའམ་རྟག་པར་འགྱུར་གྲང༌[^1372]ན། གལ་ཏེ་མི་རྟག་པ་ཡིན་ན་ནི། རྩོལ་བ་ལས་བྱུང་མི་རྟག་ན། དེ་ཅི་སྐྱེས་བུས་བྱས་པ་མིན། །མི་རྟག་པ་ནི་གདོན་མི་ཟ་བར་འགའ་ཞིག་ལས་སྐྱེ་བ་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 1879]
དེ་ལྡན་པར་ཡོད་པ་ཉིད་གློ་བུར་བ་ཡིན་ན་ཡུལ་ལ་སོགས་པ་ངེས་པར་མི་འགྱུར་རོ་ཞེས་བཤད་ཟིན་ཏེ། [^1373]དེ་ཡང་འབད་རྩོལ་གྱིས་འཕངས་པ་བྱེད་པའི་ཡོན་ཏན་དང་བྲལ་བ་མ་ཡིན་པ་ཅན་དག་ལ་མཐོང་བ་གཞན་དུ་མ་མཐོང་ངོ་། །དེ་ལྟར་རྒྱུའི་ཆོས་མཐོང་བའི་སྐྱེས་བུའི་བྱ་བ་ཉིད་ནི་རྒྱུ་ཡིན་པ་དེ་བས་ན་སྐྱེས་བུས་བྱས་པར་འགྱུར་རོ། །

[Block 1880 [VERSE]]
རྟག་ཉིད་ཡིན་ནའང་རྟག་པ་ནི། །
དམིགས་འགྱུར་སྒྲིབ་གཡོགས་མེད་ཕྱིར་རོ། །

[Block 1881]
ཅི་སྟེ་སྒྲའི་ངོ་བོ་ཉིད་དེ་རྟག་པ་དང་དམིགས་པའི་རང་བཞིན་ཅན་དུ་འགྱུར་ན་དེའི་རང་བཞིན་དེ་ནི་འགའ་ཞིག་གི་ཚེ་ཡང་ཉམས་པ་མེད་པའི་ཕྱིར་རྟག་ཏུ་དམིགས་པར་འགྱུར་རོ། །

[Block 1882]
གལ་ཏེ་ནུས་པ་འགའ་ཞིག་ལས་ཀྱང་འཕོ་བ་མེད་པ་དེ་ལྟར་ན་རྟག་པར་གྱུར༌[^1374]ཏེ། ཤེས་པ་བསྐྱེད་པ་དེའི་ནུས་པ་བསྐྱེད་པ་བདག་ཉིད་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་དང་། དོན་གཞན་དུ་གྱུར་པ་ནི་སྔར་བཀག་ཟིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1883]
དམིགས་པའི་བདག་ཉིད་ཅན་དེ་ལ་ཡང་དམིགས་པའི་སྒྲིབ་གཡོགས་སུ་གྱུར་པ་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ཡོད་དུ་ཟིན་ཀྱང་དེའི་བདག་ཉིད༌[^1375]ཉམས་པ་མེད་པར་ནུས་པ་ཟིལ་གྱིས་མནན་པར་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1884]
དེ་ལ་ཕུལ་དུ་བྱུང་བ་བསྐྱེད་པར་མི་ནུས་ན་ནི་ཅུང་ཞིག་བྱེད་པ་ཞེས་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1885]
ཅུང་ཞིག་མི་བྱེད་ན་ཡང་དག་ལ་སྒྲིབ་པར་བྱེད་པའམ། གཞན་ཞེས་བྱ་བ་དེ་ནི་མང་དུ་དཔྱོད༌[^1376]ཟིན་ཏོ། །

[Block 1886]
བུམ་པ་ལ་སོགས་པ་དག་ལ་རྩིག་པ་ལ་སོགས་པ་དག་གིས་ཕུལ་དུ་བྱུང་བ་སྐྱེད་པར་བྱེད་པའམ་ཉམས་པ་ཅི་ཞིག་བྱེད་ན་གང་གིས་སྒྲིབ་པར་འདོད་ཅེ་ན། དེ་དག་འགའ་ཞིག་གི་ཕུལ་དུ་བྱུང་བ་བྱེད་པ་ཡིན་པར་ནི་མི་སྨྲའི། འོན་ཀྱང་བུམ་པའི་སྐད་ཅིག་མ་ཐམས་ཅད་དབང་པོའི་ཤེས་པའི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 1887]
ཕན་ཚུན་འདུས་པ་ཡུལ་དང་དབང་པོ་དང་སྣང་བ་རྣམས་ནི་གཅིག་ལ་གཅིག༌[^1377]གིས་ཁྱད་པ༌[^1378]ཅན་གྱི་སྐད་ཅིག༌[^1379]མ་གཞན་བསྐྱེད་པའི་ཕྱིར་རྣམ་པར་ཤེས་པའི་རྒྱུ་ཡིན་ཏེ། ཕན་གདགས་པར་བྱ་བ་མ་ཡིན་པའི་ལྟོས་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1888]
ནུས་པའི་རང་བཞིན་ཅན་རྟག་ཏུ་སྐྱེད་པར་བྱེད་པའམ། སྐྱེད་པར་མི་བྱེད་པའམ། གཞན་ཐམས་ཅད་དུ་འགྱུར་རོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1889]
དེ་དག་ཀྱང་ཐོགས་པར་བྱེད་པ་གཞན་གྱི་བར་མ་ཆོད་པར་ཕན་ཚུན་དུ་འདོགས་པར་བྱེད་པ་ཡིན་ཏེ། བར་དུ་གཅོད་པ་མེད་པ་ཅན་གྱི་ཡུལ་རུང་བ་ཉིད་ཀྱི་ལྷན་ཅིག་བྱེད་པ་ཅན་ཉིད་ཀྱིས་དེ་དག་ཕན་ཚུན་དུ་ཕུལ་དུ་བྱུང་བ་བསྐྱེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1890]
བར་ཆད་ཡོད་ན་ནི་རྒྱུ་མེད་པ་ནུས་པའི་སྐད་ཅིག་མ་གཞན་མི་བསྐྱེད་པའི་ཕྱིར། རྣམ་པར་ཤེས་པ་མི་བསྐྱེད་པ་ཡིན་ནོ། །

[Block 1891]
དེ་བས་ན་སྔར་བྱུང་བའི་ནུས་པ་འགགས་པའི་ཕྱིར། རྩིག་པ་ཡོད་ན་གཞན་སྐྱེ་བར་འདོད་པ་རྒྱུ་མེད་པས་མི་སྐྱེ་བའི་ཕྱིར་རྒྱུ་དང་བྲལ་བས༌[^1380]ཤེས་པ་མི་སྐྱེ་བ་དེ་ལྟར་ན་རྩིག་པ་ལ་སོགས་པ་ལ་སྒྲིབ་གཡོགས་ཞེས༌[^1381]བྱའོ། །

[Block 1892]
སྔར་རུང་བ་ལ་གེགས་བྱེད་པའི་ཕྱིར་ནི༌[^1382]མ་ཡིན་ཏེ། དེའི་རང་བཞིན་ལས་མ༌[^1383]འཕོས་པའི་ཕྱིར་རོ། །

[Block 1893]
ཡང་ན་དངོས་པོ་སྐད་ཅིག་མ་རྣམས་ཕན་ཚུན་ཕན་འདོགས་པ་ཡོད་དུ་ཟིན་ཀྱང་། ཐམས་ཅད་ཤེས་པ་མ་ཡིན་པས། །རྒྱུ་དང་རྐྱེན་གྱི་ནུས་པ་བསམ་གྱིས་མི་ཁྱབ་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1894]
དེ་བས་ན་གལ་ཏེ་དབང་པོ་དང་ཡུལ་གྱི་བར་ན་གནས་པའི་སྒྲིབ་གཡོགས་ངེས་དེ་ལ་རྣམ་པར་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་དང་ཤིན་ཏུ་མི་མཐུན་པའི་བྱེ་བྲག་གིས་ཕུལ་དུ་བྱུང་བ༌[^1384]ཅན་དུ་བྱེད༌[^1385]ཟིན་ཀྱང་། སྒྲིབ་གཡོགས་ཀྱི་བྱེ་བྲག་གིས་སྒྲ་ལ་སོགས་པ་མཉན་པ་གསལ་བ་དང་མི་གསལ་བ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1895]
དེ་ལྟ་མ་ཡིན་ན་འགའ་ཞིག་ལ་ཡང་ཐག་ཉེ་བ་ཡིན་དུ་ཟིན་ཀྱང་ཅུང་ཞིག་མེད་པ༌[^1386]ཐག་ཉེ་བ་མ་ཡིན་པ་དང་མཚུངས་པའི་ཕྱིར། འདིའི་འདི་ཞེས་ཉེ་བར་སྦྱར་བ་ནི་རྣམ་པར་རྟོག་པས་སྤྲུལ་པ་ཉིད་ཡིན་གྱི། དངོས་པོ་ལ་བརྟེན་པ་ཅན་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
