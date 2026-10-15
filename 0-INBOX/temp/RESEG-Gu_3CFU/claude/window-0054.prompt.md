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
[Block 1891]
བཏུས་པ་རྣམས་ཀྱི༌[^1315]ཚོགས་ནི་ཕུང་པོའོ། །

[Block 1892]
སྤྱིངས་པ་ལ་ནི་གནས་ཀྱི་སྟེང་ནས་རྫས་ཀྱི་སྟེང་ན༌[^1316]བྱིང་ནའོ་ཞེས་བྱ་བ་ནི་བརྐུ་བར་བྱ་བའི་རྫས་ཀྱི་གནས་ནི་ཆུ་ལ་སོགས་པ་གང་ཡིན་པའོ། །

[Block 1893]
དེའི་སྟེང་ནི་གང་ཞིག་སྟེང་གི་ཡ༌[^1317]མཐའ་ཆའི་སྟེང་རིམ་མོ། །

[Block 1894]
དེའི་སྤྱིངས་པའི་ལྟུང་བ་རྐུ་བཞིན་པའི་རྫས་ལ་ནི་བྱིང་བ་ཉིད་ལ་ནི་སྟེང་གང་ཞིག་ཡ་བླའི་ཆའི་སྟེང་རིམ་དེའི་བྱིང་བ་ལས༌[^1318]འཕོ་བའོ། །

[Block 1895]
གནས་གཞན་དུ་བྱིང་བ་ལ་ནི་འཕོ་བ་མ་ཡིན་ནོ། །

[Block 1896]
འདིར་འཕོ་བ་ནི་འཕོ་བའོ། །

[Block 1897]
དེ་ལས་སྟེང་གི་ཆ་ནི་སྟེང་ན་ཡོད་པའི་སྟེང་གི་མཚམས་ཞེས་བྱ་བ་འདིས་ཤེས་པ་རྫས་མ་ལུས་པ་འདའ་བ་ནི་འཕོ་བའོ། །

[Block 1898]
དེ་བས་ན་བུ་ག་ལ་གནས་གཞན་ཉིད་ཡོད་ཀྱང་འདའ་བར་བྱེད་པ་ཉིད་ལ་གནས་ཀྱི་སྟེང་ནས་རྫས་ཀྱི་སྟེང་ན༌[^1319]བྱིང་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1899]
དེར་ཕྱིར་དབྱུང་ངོ་སྙམ་པའི་བློ་གྲོས་གང་ཡིན་པ་ནི་བསྐུར་བའི༌[^1320]འོ་ཞེས་བྱ་བ་ནི་བྱིང་བ་ལ་ཕྱིས་བརྐུ་བར་བྱའོ་ཞེས་བྱ་བ་འདིར་བློ་གྲོས་ཀྱི་ངེས་པ་གང་ཡིན་པ་དེ༌[^1321]ལ་ནི་གནས་ཀྱི་སྟེང་ནས་རྫས་ཀྱི་སྟེང་འཕོ་བ་ཞེས་བྱ་བ་ནི་རིགས་པ་མ་ཡིན་ཞེས་བྱ་བ་གང་ཞིག་གིས་འདོད་པ་དེའི་བློ་བཟློག་པའི་ཕྱིར་མདོ་འདི་ཡིན་ཏེ། གང་གི་ཕྱིར་གལ་ཏེ་རྐུ་བའི་སེམས་ཡང་དག་པར༌[^1322]མ་སྐྱེས་པ་འདིར་འཇུག་པ་ཡིན་ན་བྱིང་བ་ཉིད་འཕོ་བ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 1900]
རྐུ་སེམས་ཡང་དག་པར༌[^1323]སྐྱེས་པ་ཉིད་ཀྱིས་རྣམ་པ་འདི་ལྟ་བུ་རྣམས་ལ་འཇུག་པའོ། །

[Block 1901]
དེ་བས་ན་འདིར་རྐུ་བ༌[^1324]ནི་བསྐུར་བའི༌[^1325]དོན་ཡིན་གྱི། ཀུན་ནས་ཆད་པའི་དོན་དུ་ནི་མ་ཡིན༌[^1326]ཞེས་བྱ་བའོ། །

[Block 1902]
འདིར་གཞུང་ནི། དགེ་སློང་གིས་ཟོང་སྤྱིང་བའི༌[^1327]ཕྱིར་ཁྲི་ལས་ལྡང་བར་བྱེད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1903]
བཤལ་བ་ལ་ནི་ངོས་ཀྱི་གཞིའི་མཚམས་ལས་ངོས་ཅིག་ཤོས་འདས་ནའོ་ཞེས་བྱ་བ་ནི་བརྐུ་བར་བྱ་བའི་རྫས་ལ་ཕྱོགས་ཀྱི་ཆ་གང་ཞིག་གིས་བཤལ་བའི་ཕྱོགས་ཀྱི་ཆ་དེ་ལ་ངོས་གང་ཞིག་ཐ་མའི་ངོས་ཙམ་དུ་གྱུར་པ་ཆ་མེད་པའི་ཆ་དེའི་རྟེན་གང་ཡིན་པ་ལ་སོགས་པ་དེའི་གནས་ཀྱི་བདག་ཉིད་ཅན་གྱི་ཆ་དེའི་མཚམས་གང་ཞིག་ཆ་དེ་ལས་རྫས་བསྐུར་བར༌[^1328]བྱ་བ་དེ་འདས་པ་གང་ཞིག་ཆ་གང་ཡང་རུང་བས་མ་ཡིན་ནོ། །

[Block 1904]
འོན་ཀྱང་ངོས་གཞན་གྱིས་ཏེ་ངོས་གང་ཞིག་གི་གཞི་འདི་སྟེ་མཚམས་བརྗོད་པ་དེའི་རྗེས་སུ་གྱུར་པའི་ངོས་ཀྱིས་བཤལ་བ་ལ་གཞིའི་སྟེང་གི་ཆ་ལ་གཞིའི་སྟེང་གི་ཆས་ཉེ་བར་ཁྲིད་པ་ལ་རྐུ་བའོ། །

[Block 1905]
གལ་ཏེ་དེས་ས་དེ་འདས་པར་གྱུར་ན་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མེད་པར༌[^1329]སྨོས་པས་ཕྱོགས་ལས་ཕྱི་རོལ་ཏུ་རྫས་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 1906]
གལ་ཏེ་དེས་ས་དེ་འདས་པར་གྱུར་ན་ཞེས་བྱ་བ་སྟེ། དེ་བས་ན་འདིར་བསྐུར་བ་གདགས༌[^1330]པར་བྱའོ། །

[Block 1907]
ཁྱབ་པའི་ཁོངས་སུ་གཏོགས་པའི་དེ་དང་ལྡན་པ་ཉིད་ལ་བསྐུར་བར༌[^1331]བྱ་བའི་རྫས་དེ་ཕྱོགས་ཅི་ཙམ་ཁྱབ་པ་དེའི་ཁོངས་སུ་བསྡུས་པའི་མཚམས་ཀྱི་ཆ་ལ་ངོས་གཞན་གྱིས་བཤལ་ནས་འདས་པ་ནི་བརྐུས་པ་མ་ཡིན་ཞེས་སྟོན་པ་ཁྱབ་པའི་ཁོངས་སུ་གཏོགས་པའི་དེ་དང་ལྡན་པ་ཉིད་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྐུ་བཞིན་པའི་རྫས་དེས་ཕྱོགས་ཇི་ཙམ་ཁྱབ་པ་དེའི་ཁོངས་སུ་གཏོགས་པའི་ཆའི་མཐའ་དང་ལྡན་པ་ཉིད་དུ་གྱུར་པ་ལ་གང་ཞིག་ཁྱབ་པའི་ཁོངས་སུ་གཏོགས་པའི་ཆའི་མཚམས་དེ་ལས་ངོས་གཞན་གྱིས་འདས་ནས་བཤལ་བས་བརྐུས་པ་མ་ཡིན་ནོ། །

[Block 1908]
གང་གི་ཕྱིར་འདི་ལྟར་མ་ལུས་པ་ལ་རྐུ་བ་བསྒྲུབ་པ་མ་ཡིན་ཏེ། འོན་ཀྱང་དུམ་བུ་ཕྱི་མ་ལས་ཕྲད་པ་བསྒྲུབ་པའི་ཆ་ཤས་འདོད་པར་གྱུར་པ་ཉིད་ཀྱིས་རྐུ་བར་གྱུར་པ་རྣམས་ལ་ཚོགས་པའི་ངོ་བོ་ལ་སོ་སོ་ཉིད་ཀྱིས༌[^1332]རྐུ་བ་བསྐྱེད་པ་མ་ཡིན་ཏེ། ཚོགས་པའི་ངོ་བོ་ཉིད་ཀྱིས་བརྟེན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1909]
དེ་ལྟར་ཡང་དགེ་སློང་གིས་ཡོ་བྱད་ལྕི་བ་ཤིན་ཏུ་ཐག་རིང་པོར་བཤལ་ཏེ་བརྐུས༌[^1333]ཀྱང་མཐའི་ལྟུང་བར་མི་འགྱུར་བ་མཆིས་སམ་ཡོད་དེ། དགེ་སློང་གིས༌[^1334]ཡོ་བྱད་ལྕི་བའི་ངོས་གཅིག་ཁོ་ན་ནས་བཟུང་སྟེ་ཤིན་ཏུ་ཐག་རིང་པོར་བཤལ་ཀྱང་ངོས་ཅིག་ཤོས་གནས་དེ་ནས་མ་འདས་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 1910]
དེའི་མཚན་ཉིད་ནི་གྱོང་གྲུགས་དང་གས་པ་དང་བྲིས་པ་དང་། ཁ་དོག་གཞན་དང་བར་མཚམས་དང་བར་ཆད་དག་གོ་ཞེས་བྱ་བ་ལ། མཚམས་དེའི་མཚན་ཉིད་ནི་བདག་ཉིད་དེའི་མཚན་ཉིད་དོ། །

[Block 1911]
གང་དུ་བཅད་པ་བརྗོད་པར་བྱ་བའོ། །

[Block 1912]
གྱོང་དྲུགས༌[^1335]ཞེས་བྱ་བ་ནི་གྱོང་བ་བཟུང་བའོ། །

[Block 1913]
གས་པ་ཞེས་བྱ་བ་ནི་གས་པ་བཟུང་བའོ། །

[Block 1914]
བྲིས་པ་ཞེས་བྱ་བ་ནི་ཡི་གེ་བྲིས་པ་བཟུང་བའོ། །

[Block 1915]
ཁ་དོག་གཞན་བྱ་བ་ནི་ཁ་དོག་གཅིག་ལས་གཞན་པ་གང་ཡིན་པ་དེ་ནི་ཁ་དོག་གཞན་ཏེ་དེ་ནི་མཚམས་གཞན་པའོ། །

[Block 1916]
བར་མཚམས་ཀྱི་ཚིག་གི་ནི་རེ་ལྡེ་ལ་སོགས་པ་རབ་ཏུ་ཤེས་པར་གྱུར་པའི་བར་མཚམས་བཟུང་བའོ། །

[Block 1917]
བར་ཆད་ནི་རྣམ་པ་གཉིས་ཏེ། ཤིན་ཏུ་གྱུར་པ་དང་། ས་ཕྱོགས་གཞན་ལ་རྩོམ་པར་གྱུར་པའོ། །

[Block 1918]
ས་ཕྱོགས་གཞན་དེ་ལས་མཐོང་བ་ཉིད་དུ་དེ་རྩོམ་པར་གྱུར་པ་གང་གིས་འདི་རྩོམ་པར་གྱུར་པའི་ས་ཕྱོགས་གཞན་དེ་ན་ཞུགས་པའོ། །

[Block 1919]
ཤིན་ཏུ་གྱུར་པ་ནི་ཤིན་ཏུའམ། གཞན་ཞིང་ལ་སོགས་པ་ངོས་གཅིག་ཏུ་གྱུར་པའི་ས་ཕྱོགས་ལ་ཞུགས་པ་མ་ཡིན་པ་དང་། ངོས་གཞན་དུ་གྱུར་པ་ལ་ནི་གསུམ་པ་མ་ཡིན་པའོ། །

[Block 1920]
དེ་བས་ན་དེ་དག་གིས་དབུས་སུ་བརྐོས༌[^1336]པའི་ས་ལ་དབྱིག་གུས་བཞག་པའོ། །

[Block 1921]
འདིར་བར་ཆད་ཀྱི་ཚིག་གིས་ནི་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 1922]
རེ་ལྡེ་ལ་སོགས་པས་བར་དུ་བཅད་པ་རྣམས་ལ་བར་མཚམས་ཀྱི་ཚིག་གིས་ནི༌[^1337]ཁ་དོག་གཞན་དང་ལྡན་པ་འམ་གཞན་ལ་ཁ་དོག་གཞན་གྱི་ཚིག་གིས་ཏེ། གང་དུ་ཆད་པ་བརྗོད་པར་བྱ་བ་དེ་ཙམ་གྱི༌[^1338]དགོངས་པ་ནི་མདོ་འདི་ཡིན་གྱི། མ་ལུས་པའི་དགོངས་པ་ཅན་ནི་མ་ཡིན་ནོ། །

[Block 1923]
འདི་ལ་བརྗོད་པར་བྱ་བ་ཉིད་ནི་གཞན་དུ་ཡིན་ཞེ་ན། དབུས་སུ་གནས་པའི་སྐྱེ་བའི་རྒྱུན་ལའོ། །

[Block 1924]
དེར་ནི་དེ་ཉིད་ད་ལྟར་ཡང་གནས་འདི་ཞེས་བྱ་བ་བློའི་སྐབས་ཡོད་དེ། བཟློག་པའི་དོན་དུ་གནས་དེ་ལ་གནས༌[^1339]ཀྱི་སྐྱེ་བའི་རྒྱུན་ལ་ཡོད་པ་ཉིད་དེ་གང་གི་ཕྱིར་ད་ལྟར་ཡང་གནས་དེ་ཉིད་ཅེས་བྱ་བའི་བློའི་སྐབས་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1925]
སྲོག་ཆགས་ལ་ནི་རྩིབ་མ་ལ་སོགས་པ་ཐ་དད་པ་བརྟག༌[^1340]ཏུ་རུང་བ་རྣམས་བར་ཆད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྲོག་ཆགས་ལ་ནི་རྩིབ་མ་ལ་སོགས་པ་གང་རྣམས་ལ་ཐ་དད་པར་རྟག་ཏུ་རུང་བ་རྩིབ་མ་ལ་སོགས་པའོ། །

[Block 1926]
དེ་རྣམས་ཀྱི་བར་ཉིད་དེ་བར་ཆད་ནི་ངེས་པ་སྟེ། འདི་རྣམས་ལ་སོ་སོར་གནས་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1927]
སོགས་པའི་སྒྲས་ནི་སོ་དང་སྣས་བར་དུ་བཅད་པ་བཟུང་བའོ། །

[Block 1928]
སོག་ཆགས༌[^1341]ལ་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་སྲོག་ཆགས་ཀྱི་ལུས་ཀྱི་བདག་ཉིད་ལ་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་དུ༌[^1342]གནས་ཀྱང་གཅིག་པ་ཉིད་ཅེས་བྱ་བའི་དོགས་པ་བཟློག་པའི་དོན་དུའོ།[^1343] །ཤ་དང་ཁྲག་ཉིད་ཉེ་བར་བརྟགས་པ་ཉིད་ལ་འདིའི་ཐ་དད་པར་བརྟག༌[^1344]ཏུ་རུང་བ་ཉིད་ཀྱི་ཕྱིར་རྩིབ་མ་ལ་སོགས་པ་རྣམས་ཉིད་ལ་གནས་པ་ཉིད་ཡིན་ཏེ་སྟོབས་ཆུང་བ་ཉིད་ལ་མ་ཡིན་ནོ། །

[Block 1929]
འདི་རྣམས་ཀྱི་ལུས་ཀྱི་བདག་ཉིད་ཀྱི་གནས་ལ་ཆ་ཤས་ཉིད་ཀྱི་ཕྱིར་སོ་སོར་གནས་པ་ཉིད་ཤེས་པར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1930]
དེས་ན་རྩིབ་མ་ཞིག་གཅིག་གི༌[^1345]ཕྱོགས་ནས་རྩིབ་མ་ཐ་དད་པར་བརྟག༌[^1346]ཏུ་རུང་བ་ཉིད་གཞན་གྱི་བར་དུ་སྤོས་ན་བརྐུས་པ་ཉིད་དུ་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
