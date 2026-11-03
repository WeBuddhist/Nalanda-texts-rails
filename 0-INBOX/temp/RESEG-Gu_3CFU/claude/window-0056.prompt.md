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
[Block 1961]
འོ་ན་སྦྱིན་པར་བྱ་བ་ཉིད་མ་ཡིན་ན༌[^1364]ལོག་པ་ལ་འདའ་བར་བྱེད་པ་འདི་ཡོད་པ་མ་ཡིན་ཞེས་བྱ་བར༌[^1365]རིག་པར་བྱའོ། །

[Block 1962]
རྣམ་པར་གཞག་པའི་དབང་གིས་འདི་སྦྱིན་པ་ཉིད་དོ། །

[Block 1963]
གང་དུ་འདའ་བར་བྱེད་པ་མཐོང་བར་སྒོ་ཆེ་གེ་མོར་ཞུགས་པ་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པའི་རྣམ་པར་གཞག་པར་བྱས་པར་འགྱུར་བ་དེ་ལ་སྦྱིན་པ་ཉིད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1964]
མི་ལ་གལ་ཏེ་བརྡས་ནི་དེ་གྲུབ་པ་ནའོ་ཞེས་བྱ་བ་ལ་མི་རྐུ་བ་ནི་རྣམ་པ་མང་དུ་འགྱུར་ཏེ་མི་འདོད་བཞིན་དུ་དཀྲིས་པ༌[^1366]དང་གཞག་པ་དག་གིས་སོ། །

[Block 1965]
འཇིག་པའི་རྒྱུ་མཚན་གྱིས་སམ་ཀུན་དུ་རྒྱུ་བས་རྣམ་པར་རྨོངས་པར་གྱུར་པ་ལ་ཡང་སྔགས་དང་སྨན་དག་གིས་སོ། །

[Block 1966]
བཅིངས་པ་ལ་ཡང་བཀྲོལ་བས་སོ། །

[Block 1967]
གཉིད་ཀྱིས་ལོག་པ་ལ་ཡང་མ་ཚོར་བའི་འཕེན་པས་སོ། །

[Block 1968]
གསོད་པ་ཉེ་བར་རྩོལ་བ༌[^1367]ཡང་འཆི་བདག་དང་ལྷན་ཅིག་ཏུའམ་འཆི་བདག་གིས་ཞེས་བྱ་བ༌[^1368]ཁྱད་པར་འདིའོ། །

[Block 1969]
མི་ལ་ནི་གལ་ཏེ་བརྡས་བརྐུ༌[^1369]བའོ། །

[Block 1970]
དེ༌[^1370]གྲུབ་པ་ནི་བརྡ་གྲུབ་པ་ཉིད་རྐུ་བའོ། །

[Block 1971]
འདི་ལྟར་གཞུང་ལས།

[Block 1972]
མི་རྐུ་བ་རྣམ་པ་གསུམ་པོ་ཡུལ་ཕྱོགས་དང་། མཚན་མ་དང་། བརྡས་སོ། །

[Block 1973]
རང་གི་འདོད་པས་རབ་ཏུ་རྒྱུ་བ་གྲོལ་བ་ཕྲད་པ་ནི་དེ་འདིར་རྐུ་བ༌[^1371]ཉིད་ཀྱིས་མངོན་པར་འདོད་པའོ། །

[Block 1974]
འདིར་འདུན་ས་ལ་སོགས་པའི་ཡུལ་ཕྱོགས་བརྗོད་དོ། །

[Block 1975]
མཚན་མ་ནི་རྟགས་ཏེ་སྐྲ་དང་ཁ་སྤུ་བྲེགས་ཏེ་རིང་པོ་མ་ལོན་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1976]
བརྡ་ནི་སྔ་དྲོ་ལ་སོགས་པའོ། །

[Block 1977]
ཡུལ་ཕྱོགས་ལ་སོགས་པ༌[^1372]གསུམ་པོ་འདི་རྣམས་ལ་དོན་ཐ་དད་པ་ཉིད་ཡོད་ཀྱང་། སྔ་དྲོ་ལ་སོགས་པའི་ཁྱད་པར་མངོན་པར༌[^1373]མཚོན་པར་དཀའ་བས་ཏེ། དེ་བས་ན་སྤྱིར་བརྡའི་སྒྲས་བརྗོད་པའོ། །

[Block 1978]
བརྡ་གང་ཡིན་པ་འདི་བྱས་པ་གང་གི་ཚེ་ཁྱོད་ཀྱི་ཁོ་བོ་འདི་དང་འདི་ལྟ་བུར་མཐོང་བ་དེའི་ཚེ་ཁྱོད་ཁོ་བོའི་གན་དུ་ཤོག་ཅེས་བྱ་བ་ལྟ་བུ་སྟེ། གང་གི་ཚེ་བརྡ་དེ་གྲུབ་པ་དེའི་ཚེ་མི་དེ་བརྐུས་པར་རིག་པར་བྱའོ། །

[Block 1979]
འདི་དང་རྣམ་པ་གཞན་རྣམས་ལ་ཡང་མཚན་ཉིད་ཀྱི་རྗེས་སུ་འབྲང་བས་རྐུ་བ་རྟོགས་པར་བྱའོ། །

[Block 1980]
གཏེར་བཞིན་དུ་གསང་སྔགས་ཀྱིས་དྲང་བར་བྱ་བ་ལ་སྣང་བར་གྱུར་ནའོ། །

[Block 1981]
ཕྱི་བཞིན་དུ་འབྲང་བ་དང་ནང་བྱན་བྱེད་པ་མེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1982]
གལ་ཏེ་དེ་ལྟར་ན་བྱ་སྤར་བ་ནའོ་ཞེས་བྱ་བ་ནི་འདིར་གལ་ཏེ་བྱ་སྤར་ཏེ་བརྐུ་བར༌[^1374]བྱེད་ནའོ། །

[Block 1983]
དེའི་ཚེ་བྱ་སྤར་ན་བརྐུས་པ་ཁོ་ན་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1984]
འདིར་གཞུང་ནི། དགེ་སློང་བྱ་སྤར་ཏེ་རྐུ་བར་བྱེད་ན་བྱའི་རིན་ཐང་བརྩི་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1985]
སྤར་བ་ན་ཞེས་བྱ༌[^1375]འདི་ནི་རྐུ་བའི་ཁྱད་པར་ཏེ། དེ་ལྟར་སྤར་ནས་རྐུ་བར་བྱེད་ཅེས་བྱ་བའི་དོན་འདི་འགྲུབ་པར་འགྱུར་རོ། །

[Block 1986]
སྤང་བ་ཐམས་ཅད་ནི་མཚམས་གཞན་དུ་འགྲོ་བ་སྟེ། དེ་བས་ན་དེའི་རྐུ་བ་ཉིད་ནི་འདིར་དཔེ་ཡིན་ནོ། །

[Block 1987]
བྱའི་ཚིག་ནི་རྫས་རྣམས་ཐམས་ཅད་ལ་ཆོ་ག་འདི་རྟོགས་པར་བྱའོ། །

[Block 1988]
དུད་འགྲོ་བཏགས་པ་ནི་བཀྲོལ་ནའོ་ཞེས་བྱ་བ་ནི་དུད་འགྲོ་བཏགས་པ་རྐུ་བ་ནི་བཀྲོལ་བ་ན༌[^1376]བརྐུས་པ་ཡིན་ནོ། །

[Block 1989]
འདིས་ནི་དགེ་སློང་གིས༌[^1377]རི་དགས་རླུབས་སུ་ཆུད་པ་ཕྱུང་ན་རི་དགས་ཀྱི་རིན་ཐང་བརྩི་བར་བྱའོ། །

[Block 1990]
དགེ་སློང་གིས༌[^1378]ཉ་དོལ་ལ་ཐོགས་པ་ཕྱུང་ན་ཉའི་རིན་ཐང་བརྩི་བར་བྱའོ་ཞེས་གསུངས་པ་རྣམས་ནི་དེ་ལ་འདི་བསྡུས་པ་ཡིན་ནོ། །

[Block 1991]
བཀྲོལ་བ་ཉིད་ལས་རིན་ཐང་བརྩི་བ་ལ་རིམ་པ་ཡོངས་སུ་བཟུང་བས་བཀྲོལ་བ་ཉིད་འདིར་རྐུ་བ་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 1992]
བརྟོད་པ༌[^1379]དང་ཁྱུ་ལས་བཀར་བ༌[^1380]གཉིས་ནི་མི་སྣང་བར་གྱུར་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་ལ། བརྟོད་པ༌[^1381]དང་ཁྱུ་ལས་བཀར་བས་དུད་འགྲོའི་བྱ་བ་ནི་མི་སྣང་བ་ཉིད་འདི་ལ་བརྐུས་པའོ། །

[Block 1993]
གལ་ཏེ་འདི་ལ་དེར་བདག་པོ་འམ་དེ་དང་འདྲ་བ་ཡོད་ན་ཕྱི་བཞིན་འབྲང་བ་འཕྲོག་བཞིན་པ་འདི་ལའམ། ཕྱིར་འགྲོ་བཞིན་པ་མ་ཡིན་པ་དེ་ལ་རྩེ་གཅིག་དེའི་གནས་ལས་མི་སྣང་བ་ཉིད་དོ། །

[Block 1994]
འོན་ཏེ་ཡོད་པ་མ་ཡིན་ན་མ་བཀྲོལ་བ་ལའམ༌[^1382]དེ་ལ་རྩེ་གཅིག་པ་ལ་གལ་ཏེ་ཁྱུ་ན་གནས་པ་ལ་བརྟོད་པ༌[^1383]དང་ཁྱུ་ལས་བཀར་བས༌[^1384]ཁྱུའི་མཐའ་མ་ཚང་བས་མི་སྣང་བ་ཉིད་དོ། །

[Block 1995]
གལ་ཏེ་གཅིག་པུ་མ་ཡིན་ན་གནས་དེ་ལས་མི་བསྐྱོད་ན་དེ་ནས་མི་སྣང་བ་ཉིད་ནི་རྐུ་བ་ཞེས་བྱ་བ༌[^1385]འདི་རིགས་པར༌[^1386]རྟོགས་པར་བྱའོ། །

[Block 1996]
གནས་མ་ངེས་པ་ཉིད་ཀྱི་ཕྱིར་དང་རབ་ཏུ་རྒྱུ་བ་མི་གནས་པ་ཉིད་ཀྱིས་གྲོལ་བའི་དུད་འགྲོ་ལ་གནས་ཀྱི་ཐ་མ་འདི་ལ་སྤོ་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1997]
དེ་ཡང་འདི་ལ་འདི་རྣམ་པར་གནས་ནས་ཏེ་གང་ཞིག་སྟོབས་ཀྱི་བདག་ཉིད་བརྟན་པའི་ཕྱིར་དེའི་ཚེ་མི་ནུས་པའམ། འཇིགས་པས་ཀྱང་འཇུག་པ་དེ་བས་ན་དེ་ལྟ་བུར་གྱུར་པའི་དུད་འགྲོའི་འདི་ལ་བཟུང་བར་རྟོགས་པར་བྱའོ། །

[Block 1998]
དེ་བས་ན་གཞན་དུ་ཡང་འདི་ལྟ་བུར་གྱུར་པའི་སྲོག་ཆགས་ལ་རྣམ་པར་གཞག་པས་འདི་ལ་དཔེ་ཉིད་དོ། །

[Block 1999]
འདིར་གཞུང་ནི། མིག་ལམ་དུ་སྣང་བར་མ་གྱུར་ན་བརྐུས་ཞེས་བྱ་བའོ། །ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2000]
གསང་སྔགས་དག་གིས་འདྲེན་པ་ནི་སྣང་བ་ནའོ་ཞེས་བྱ་བ་ནི་གསང་སྔགས་རྣམས་ཀྱིས་གཏེར་ལ་སོགས་པ་འདྲེན་པ་ན་གཏེར་ལ་སོགས་པ་སྣང་བ་ན་བརྐུས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
