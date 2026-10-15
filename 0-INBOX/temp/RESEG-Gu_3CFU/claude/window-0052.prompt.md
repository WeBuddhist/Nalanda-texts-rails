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
[Block 1821]
ཇི་སྟེ་དོན་མ་རྟོགས་པའི་བདག་པོས་ཀྱང་གང་ཞིག་བདག་པོ་མེད་པ་ཉིད་ནི་དཔེར་ན་སུས་ཀྱང་བདག་ཏུ་མ་བྱས་པའི་དགོན་པ་ལ་གནས་པའི་གཏེར་ལ་ཇི་ལྟར་སྒྲུབ་ཅེ་ན། བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་ཀྱི༌[^1272]རྫས་རྐུས་པ༌[^1273]བཞིན་དུ་དེ་ལ་མ་བྱིན་པར་ལེན་པ་མེད་དེ། [^1274]བདག་ཏུ་མ་བྱས་པ་ཉིད་ཀྱི༌[^1275]ཕྱིར་རོ། །

[Block 1822]
ཇི་སྟེ་རྐུ་སེམས་སྐྱེད་པར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 1823]
འདིར་དངོས་གཞིའི་ཆོ་ག་ལ༌[^1276]གཏོགས་པའི་ཡན་ལག་རྣམས་ལ་མིའི་འགྲོ་བ་པ༌[^1277]ཡོངས་སུ་གཟུང་བར་བྱ་བ་འདིས་སྤང་བའི་དོན་དུ་སྦྱར་བའོ། །

[Block 1824]
དེའི་འདུ་ཤེས་ཀྱིས་ཞེས་བྱ་བ་ལ་དེ་ལ་བདག་པོ་མེད་པའི་གཏེར་གྱི་འདུ་ཤེས་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1825]
བྱེ་བྲག་འདི་དང་ལྡན་པ་རྣམས་ལ་འདི་ནི་སྦོམ་པོ་སྟེ། བདག་པོ་མེད་པའི་གཏེར་ལ་བདག་པོ་དང་བཅས་པའི་འདུ་ཤེས་ཀྱིས་མིར་གྱུར་པའི་བདག་པོས་སམ་གཞན་གྱིས་ཀྱང་སྦོམ་པོ་ཉིད་དོ། །

[Block 1826]
འདིར་ལས་འདི་ལ་ཤིན་ཏུ་མཆོག་ཉིད་ཀྱི་ཕྱིར་མ་ཤ་ཀ་ལྔ༌[^1278]ལ་སོགས་པ་མ་ཚང་བ་ཉིད་ཀྱི་ཕྱིར༌[^1279]གཏེར་ལ་བདག་པོ་ཉིད་མེད་པའི་འདུ་ཤེས་ཀྱིས་དང་། བདག་པོ་དང་བཅས་པ་ཉིད་ཀྱི་འདུ་ཤེས་ལ་ཡང་བདག་པོ་མི་མ་ཡིན་པའམ། མིའི་བདག་པོས་ཀྱང་སྦོམ་པོ་བྱས་པ་ལས་དམན་པའི་ཕྱིར་ཉེས་བྱས་སོ། །

[Block 1827]
རང་གིའོ་ཞེས་བྱ་བ་ནི་རང་གི་རྫས་མ༌[^1280]ཤ་ཀ་ལྔ༌[^1281]ལ་སོགས་པ་རྐུ་སེམས་ཀྱིས་དེར་འདུ་ཤེས་པས་རྐུའམ་རྐུར་བཅུག་པ་དང་། མངགས་པས་དང་ལྟུང་བ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 1828]
དེར་འདུ་ཤེས་པ་ཞེས་བྱ་བའི་ཚིག་དེ་སྐབས་འདིར་ནི་རང་གི་འདུ་ཤེས་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 1829]
དེ་ལྟར་ཡང་གཞུང་ནི། དེའི་ཕྱིར་དགེ་སློང་གིས་རང་གི་ལྷུང་བཟེད་དང་ཆོས་གོས་ཀྱང་རྐུ་སེམས་ཀྱིས་བླང་བར་མི་བྱའོ། །

[Block 1830]
གལ་ཏེ་དགེ་སློང་གིས་རང་གི༌[^1282]ལྷུང་བཟེད་དང་ཆོས་གོས་ཀྱང་རྐུ་སེམས་ཀྱིས༌[^1283]ལེན་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1831]
རང་གི་ལ་གཞན་གྱིས་ཡོངས་སུ་བཟུང་བར་འདུ་ཤེས་པ་ཡང་སྦོམ་པོ་ཁོ་ན་སྟེ། འདི་ལས་འདི་ལ་རྐུ་སེམས་ཤིན་ཏུ་ལྕི་བའི་ཕྱིར་རོ། །

[Block 1832]
དེ་ལྟར་ཡང་གཞུང་ནི། དགེ་སློང་དག་མ་ཕམ་པ་མི་གཏི་མུག་ཅན་འདི་ནི་རང་གི་ཆོས་གོས་རྙང་རྙིང་དག་གིས་ཉེས་པ་སྦོམ་པོའི་ལྟུང་བ་འབྱུང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1833]
རང་གི་ལ་གཞན་གྱིས་ཡོངས་སུ་བཟུང་བར་འདུ་ཤེས་པ་ལ་སྦོམ་པོ་ཁོ་ན་སྟེ། རང་གི་ལ་གཞན་གྱིར་འདུ་ཤེས་པ་དང་ཡོངས་སུ་མ་བཟུང་བ་ལ་མ་བཟུང༌[^1284]བར་འདུ་ཤེས་པར་ཅེས་པ༌[^1285]ནི་ལྟུང་བ་ལ་འདྲ་བའི་ཕྱིར་རོ། །

[Block 1834]
དེ་བཞིན་དུ་ཡོངས་སུ་མ་བཟུང་བ་ལ་ཡོངས་སུ་མ་བཟུང་བར་འདུ་ཤེས་པའམ། ཡོངས་སུ་བཟུང་བ་དང་བཅས་པར་འདུ་ཤེས་པ་ལ་ཡང་སྦོམ་པོ་ཁོ་ནའོ། །

[Block 1835]
འགྲོ་བ་གཞན་གྱིར༌[^1286]རོ་ཞེས་བྱ་བ་ནི་མིའི་འགྲོ་བ་ལས་གཞན་པའི་འགྲོ་བ་གང་ལ་ཡོད་པ་གང་ཡིན་པ་དེ་ནི་འགྲོ་བ་གཞན་ཏེ་རང་གི་ཞེས་བྱ་བ་འཇུག་གོ། །

[Block 1836]
འགྲོ་བ་གཞན་ལ་གནས་པ་མིའི་འགྲོ་བ་པར་ཡོངས་སུ་འཛིན་པ་ལ་འདི་དང་བྲལ་བའི་དངོས་གཞིའི་ཡན་ལག་ཡོད་དུ་ཟིན་ཀྱང་སྦོམ་པོ་སྟེ། དེར་འདུ་ཤེས་པས་སོ༌[^1287]ཞེས་བྱ་བ་འདི་ལ་འདིར་འགྲོ་བ་གཞན་དུ་ཤེས་པས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1837]
འདིར་གཞུང་ནི། དེ་འདི་སྙམ་དུ་གལ་ཏེ་བྱའི་རྐུའི་མིའི་ནི་མ་ཡིན་ནོ་སྙམ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 1838]
མི་མ་ཡིན་པའི་འགྲོ་བ་པ་དང་འབྲེལ་བའི་འདུ་ཤེས་ཀྱིས་ནི་འགྲོ་བ་གཞན་དང་འབྲེལ་པ་ལ་སྦོམ་པོ་ཁོ་ན་སྟེ། ཤིན་ཏུ་མཆོག་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1839]
བདག་གིར་མ་བྱས་པར་སྦ་བ་དང་ཆུད་གཟན་པ་དང་ཟིན་པ་བཏང་བ་ལ་སོགས་པས་བྲལ་བར་བྱེད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བདག་གིར་མ་བྱས་པར་སྦ་བ༌[^1288]ལ་སོགས་པ་གང་ཞིག་བྲལ་བར་བྱེད་ན་ཡང་དེར་སྦོམ་པོའོ། །

[Block 1840]
སྦ་བ་ཞེས་བྱ་བ་ནི་འདིར་འདམ་རྫབ་ཏུ་གཞུག་པ་ལ་སོགས་པར་བསྟན་ཏོ། །

[Block 1841]
ཆུད་གཟན་པ་ཞེས་བྱ་བ་ནི་བསྲེག་པ་དང་གཅད་པ༌[^1289]དང་བྲལ་བའི༌[^1290]བདག་ཉིད་ཀྱིས༌[^1291]ཆུད་ཟོས་པའོ། །

[Block 1842]
ཟིན་པ་བཏང་བ་ཞེས་བྱ་བ་ནི་རི་དགས་དང་ཉ་དག་ལ་སོགས་པ་རླུབས་དང་རྡོས་ལ་སོགས་པས་ཟིན་པ་དག་དེའི་ཡང་འདྲ་བ་ཉིད་ཀྱི་ཕྱིར་འདི་ལྟ་བུའི་རིགས་ཅན་གཞན་ལ་དཔེ་ཉིད་རྣམ་པར་གནས་ཞེས་བྱ་བ་བྱེ་བྲག་མེད་པར་ཉེ་བར་འབྲེལ་པའོ། །

[Block 1843]
འདིར་རྣམ་པ་གཞན་ཡང་བཅིང་བ་དང་བྲལ་བ༌[^1292]དང་སྐྲོད་པ་དང་གསོད་པ་ལ་སོགས་པ་ཡོད་པ་ཡིན་ཏེ། དེ་རྣམས་ལ་ཁོངས་སུ་བསྡུ་བའི་ཕྱིར་སོགས་པའི་སྒྲའོ། །

[Block 1844]
རྐུའམ་རྐུར་བཅུག་པ་དག་ལ་རྐུ་སེམས་ཀྱིས་ཞེས་བྱ་བ་འདིར་དངོས་གཞིའི་ཆོ་ག་ལ་གཏོགས་པ་འབའ་ཞིག་གི་ཡན་ལག་འདི་མེད་པའོ། །

[Block 1845]
དེ་བས་ན་མངགས་པས་ཀྱང་མ་བྱིན་པའོ། །

[Block 1846]
མ་ཤ་ཀ་ལྔ་ལ་སོགས་པའོ། །

[Block 1847]
མིའི་འགྲོ་བ༌[^1293]པས་ཡོངས་སུ་བཟུང་བ་ལ་དེའི་འདུ་ཤེས་ཀྱིས་ཞེས་བྱ་བའི་ཁྱད་པར་དེ་དང་ལྡན་པའི་ཆོ་ག་འདི་ལ་སྦོམ་པོ་འདི་རིག་པར་བྱའོ། །

[Block 1848]
གཞན་ལ་ཡང་དེའི་རྗེས་སུ་འབྲངས་པས་རྟོགས་པར་བྱའོ། །

[Block 1849]
གཞན་གྱི༌[^1294]འགྲོ་བ་པ་དང་འབྲེལ་པའི་འདུ་ཤེས་ཀྱིས་མིའི་འགྲོ་བ་པ་དང་འབྲེལ་པ་བྲལ༌[^1295]བར་བྱེད་ན་སྦོམ་པོའི་བྱེད་པ་དམན་པའི་ཕྱིར་ཉེས་བྱས་སོ། །

[Block 1850]
དེ་བཞིན་དུ་མི་མ་ཡིན་པའི་འགྲོ་བ་པ་དེ་འབྲེལ་པ་ལ་མིའི་འགྲོ་བ་པ་དང་འབྲེལ་བའི་འདུ་ཤེས་ཀྱིས་འབྲལ་བར༌[^1296]བྱེད་ཀྱང་ཉེས་བྱས་སོ། །

[Block 1851]
མ་ཆོག་པ་ཉིད་ལ་གང་དང་དེ་འབྲེལ་པ་ལ་གང་དང་འབྲེལ་བའི་འདུ་ཤེས་ཀྱིས་སྦོམ་པོའི་བྱེད་པ་དམན་པའི་ཕྱིར་ཉེས་བྱས་སོ། །

[Block 1852]
གཞན་གྱིས་ཡོངས་སུ་མ་བཟུང་བ་ཉིད་ཀྱི༌[^1297]འདུ་ཤེས་ཀྱིས་ཉེས་བྱས་སོ། །

[Block 1853]
ཡོངས་སུ་བཟུང་བ་དང་བཅས་པའམ་ཡོངས་སུ་མ་བཟུང་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 1854]
བྲལ་བར་བྱེད་པའི་འདུ་ཤེས་མེད་པའི་ཕྱིར་བྲལ་བར་བྱེད་པའི་འདུ་ཤེས་ཅན་ལ་འདིར་ལྟུང་བར་བྱས་པ་ཉིད་དོ། །

[Block 1855]
དཔེར་ན་གཞན་ལ་རྐུ་སེམས་ཀྱིས་དེའི་ཁྱད་པར་དུ་བྱས་པ་ཉིད་ལ་ཡན་ལག་གཞན་རྣམས་ཞེས་བྱ་བའོ། །

[Block 1856]
[^1298]འདིར་གཉིས་ཀ་རྣམ་པར་བྲལ་བར་བྱེད་པ་ལས་ཡོངས་སུ་བཟུང་བ་དང་བཅས་པའི་འདུ་ཤེས་ཡོད་པ་ལ་རྣམ་པར་ལྡང་བ་སྟེ། གསོད་པའི་བློ་དང་སྙིང་རྗེའི་སེམས་ཀྱིས་ཞེས་བྱ་བའོ། །

[Block 1857]
དེ་ལ་སྙིང་རྗེའི་སེམས་ཀྱིས་འདི་བྱེད་པ་ལ་ཉེས་བྱས་ཏེ་ཞེས་བྱ་བར་འཆད་པར་འགྱུར་རོ། །

[Block 1858]
ལྷག་མ་གསོད་པའི་བློས་ཆོ་ག་འདི་བྱེད་པ་ལ་རྣམ་པར་ཞུགས་པར་རིག་པར་བྱའོ། །

[Block 1859]
སྙིང་རྗེ་དང་ལྡན་པའི་སེམས་ཀྱིས་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ལ། ཡོངས་སུ་བཟུང་བ་དང་བཅས་པའི་འདུ་ཤེས་ཡོད༌[^1299]པ་ལ་བཟུང་བ་བཏང་བ་ལ་སོགས་པས་གཞན་གྱི་དོན་དང་བྲལ་བར་བྱེད་པ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 1860]
སྔར་བྱས་ན་ཕྱིར་བཅོས་མ་བྱས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་དེ་ན་བུད་མེད་ནི་མང་སྐྱེས་པ་ནི་ཉུང་ངོ་ཞེས་སྔར་སྦྲན་པའི་ལོ༌[^1300]རྒྱུས་དབུལ་བའི་ཕྱིར་བཅོས་པ་སྟེ། གང་དུ་ཕྱིར་བཅོས་པ་རྐུན་པོ་རྣམས་ཕྱིར་བཟློག་པ་ལ་སོགས་པ་བྱེད་པ་དེ་ལ་དང་པོ་ནི་རྩོམ་པ་བྱས་པ་མེད་པར་མི་འགྱུར་རོ། །
--- END BLOCKS ---
