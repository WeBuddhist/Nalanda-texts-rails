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
[Block 3396 [VERSE]]
ངན་སོང་དུ་འགྲོ་བ་རྣམས་སོ། །
མིར་འགྲོ་བས་ན་མིར་འགྲོ་བས་ཏེ།
མིའི་ནང་དུ་འགྲོ་བ་རྣམས་སོ། །

[Block 3397]
ལྷར་འགྲོ་བས༌[^1942]ན་ལྷར་འགྲོ་བ་སྟེ། ལྷའི་ནང་དུ་འགྲོ་བ་རྣམས་སོ། །

[Block 3398]
དེ་དག་གི་རྣམ་པར་ཤེས་པ་ནི་གྲངས་བཞིན་དུ་རྐང་པ་དང་། ལྟེ་བ་དང་། སྙིང་གར་འགག་གོ། །

[Block 3399]
ཡང་མི་སྐྱེ་བས་ན་མི་སྐྱེ་བ་སྟེ། དགྲ་བཅོམ་པ་དག་གོ། །

[Block 3400]
དེ་དག་གི་རྣམ་པར་ཤེས་པ༌[^1943]སྙིང་ཁར་འགག་གོ། །

[Block 3401]
གཞན་དག་ན་རེ་སྤྱི་བོར༌[^1944]ཞེས་ཟེར་རོ། །

[Block 3402]
དེ་དག་ཏུ་ལུས་ཀྱི་དབང་པོ་འགག་པའི་ཕྱིར་རོ། །

[Block 3403]
འཆི་བའི་ལུས་ཀྱི་དབང་པོ་ནི་རྡོ་ལེབ་བསྲེགས་པའི་ཐོག་ཏུ་ཆུས་བཏབ་པ་ཞུམ་པར་འགྱུར་བ༌[^1945]བཞིན་དུ་རྐང་པ་ལ་སོགས་པར་ནུབ་པར་འགྱུར་རོ། །

[Block 3404 [HEADING]]
#### གནད་འཆད་པ། ^3-1-15-0

[Block 3405]
གནད་འཆད་པའི་ཚོར་བས་ཉེན་པའི་སྲོག་ཆགས་རྣམས་ནི་ཕལ་ཆེར་དེ་ལྟ་དེ་ལྟར་རིམ་གྱིས༌[^1946]འཆི་བར་འགྱུར་རོ། །

[Block 3406]
གནད་གཅོད་པ་ནི་ཆུ་ལ༌[^1947]སོགས་ཀྱིས་ལུས་ཀྱི་ཕྱོགས་འགའ་ཞིག་ཉམས་ན་འཆི་བར་འགྱུར་བ་དེ་དག་ནི་གནད་རྣམས་ཞེས་བྱའོ། །

[Block 3407]
དེ་དག་ཀྱང་ཆུ་དང་མེ་དང་རླུང་གི་ཁམས་རྣམས་ལས་གང་ཡང་རུང་བ་ཞིག་དྲག་ཏུ་འཁྲུགས་པར་གྱུར་པ་མཚོན་ཆ་ཐམས་ཅད་བདར༌[^1948]བས་བཏབ་པ་དང་འདྲ་བས་ཚོར་བ་མི་བཟད་པ་དག་གིས་བཅད་པ་ལྟ་བུ་ཡིན་གྱི། དེ་དག་ཤིང་གཅོད་པ་ལྟ་བུར་ནི་མ་ཡིན་ནོ། །

[Block 3408]
ཡང་ན་བཅད་པ་དང་འདྲ་བར་ཡང་གཡོ་བ་མེད་པས་ན་བཅད་པ་ཞེས་བྱའོ། །ཅིའི་ཕྱིར་སའི་ཁམས་ཀྱི༌[^1949]མ་ཡིན་ཞེ་ན། སྐྱོན་བཞི་པ་མེད་པའི་ཕྱིར་ཏེ། རླུང་དང་མཁྲིས་པ་དང་བད་ཀན་རྣམས་ནི་སྐྱོན་གསུམ་ཡིན་པ༌[^1950]དེ་དག་གི་གཙོ་བོ་ནི་ཅི་རིགས་པར་ཆུ་དང་མེ་དང་རླུང་གི་ཁམས་དག་ཡིན་ནོ། །

[Block 3409]
གཞན་དག་ན་རེ་སྣོད་ཀྱི་འཇིག་རྟེན་འཇིག་པ་དང་ཆོས་མཐུན་པས་སོ་ཞེས་ཟེར་རོ། །

[Block 3410]
ལྷ་དག་གི་ནང་ན་ནི་གནད་འཆད་པ་མེད་མོད་ཀྱི། འོན་ཀྱང་ལྷའི་བུ་འཆི་བའི་ཆོས་ཅན་ལ་ནི་ཉེ་བའི་སྔ༌[^1951]ལྟས་ལྔ་འབྱུང་བར་འགྱུར་ཏེ། གོས་རྣམས་དང་རྒྱན་རྣམས་ལས་སྒྲ་ཡིད་དུ་མི་འོང་བ་འབྱུང་བར་འགྱུར་རོ། །

[Block 3411]
ལུས་ཀྱི་འོད་ཆུང་བར་འགྱུར། ཁྲུས་བྱས་པའི་ཆུའི་ཐིགས་པ་དག་ལུས་ལ་ཆགས་པར་འགྱུར། གཡོ་བའི་བདག་ཉིད་ཅན་ཡང་བློ་ཡུལ་གཅིག་ལ་གནས་པར་འགྱུར། མིག་གཉིས་འཛུམས་པ་དང་འབྱེད་པ་དག་སྲིད་པར་འགྱུར་ཏེ། དེ་དག་ནི་འཁྲུལ་པ་ཅན་ཡིན་ནོ། །

[Block 3412]
འཆི་བའི་ལྟས་ལྔ་ལས་ནི་མི་འདའ་སྟེ། གོས་དྲི་མ་ཅན་དུ་འགྱུར། མེ་ཏོག་ཕྲེང་རྙིངས་པར་འགྱུར། མཆན་ཁུང་གཉིས་ནས་རྔུལ་འབྱུང་བར་འགྱུར། ལུས་ལས༌[^1952]དྲི་ང་བ་དག་འབྱུང་བར་འགྱུར། ལྷའི་བུ་རང་གི་སྟན་ལ་མི་དགའ་བར་འགྱུར་བའོ། །

[Block 3413 [HEADING]]
#### ཚོགས་གསུམ། ^3-1-16-0

[Block 3414]
སེམས་ཅན་གྱི་འཇིག་རྟེན་འདི་དེ༌[^1953]ལྟར་སྐྱེ་བ་དང་། གནས་པ་དང་འཆི་འཕོ་བ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་ཚོགས་གསུམ་དུ་བཞག་སྟེ། ཚོགས་གསུམ་ནི་ཡང་དག་པ་ཉིད་དུ་ངེས་པའི་ཚོགས་དང་། ལོག་པ་ཉིད་དུ་ངེས་པའི་ཚོགས་དང་། མ་ངེས་པའི་ཚོགས་སོ། །

[Block 3415 [HEADING]]
##### ཡང་དག་པ་ཉིད་དུ་ངེས་པའི་ཚོགས། ^3-1-16-1-0

[Block 3416]
དེ་ལ་འཕགས་དང་མཚམས་མེད་བྱེད་པ་དག་ཡང་དག་ལོག་པ་ཉིད་དུ་ངེས། །ཡང་དག་པ་ཉིད་གང་ཞེ་ན། མདོ་ལས་གང་འདོད་ཆགས་གཏན་ནས་སྤངས་པ་དང་། ཞེ་སྡང་གཏན་ནས་སྤངས་པ་དང་། གཏི་མུག་གཏན་ནས་སྤངས་པ་དང་། ཉོན་མོངས་པ་ཐམས་ཅད་གཏན་ནས་སྤངས་པ་ཉིད་ནི་ཡང་དག་པ་ཉིད་དོ་ཞེས་འབྱུང་ངོ་། །འཕགས་པ་རྣམས་གང་ཞེ་ན། གང་དག་ལ་ཟག་པ་མེད་པའི་ལམ་སྐྱེས་པའོ། །

[Block 3417]
སྡིག་པའི་ཆོས་ལས་རིང་དུ་སོང་བས་ན་འཕགས་པ་རྣམས་ཏེ། གཏན་དུ་འབྲལ་བའི༌[^1954]ཐོབ་པ་རྙེད་པའི་ཕྱིར་རོ། །

[Block 3418]
དེ་དག་ནི་ཉོན་མོངས་པ་ཟད་པར་ངེས་པའི་ཕྱིར་ཡང་དག་པ་ཉིད་དུ་ངེས་པ་དག་ཡིན་ནོ། །

[Block 3419]
ཐར་པའི་ཆ་དང་མཐུན་པ་ཐོབ་པ་ཡང་གདོན་མི་ཟ་བར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི༌[^1955]ཆོས་ཅན་ཡིན་ན་ཅིའི་ཕྱིར་ཡང་དག་པ་ཉིད་དུ་ངེས་པ་དག་མ་ཡིན་ཞེ་ན། དེ་དག་ནི་ལོག་པ་ཉིད་དུ་ཡང་ངེས་པར་འགྱུར་ལ། དེ་དག་ཇི་ལྟར་དེ་ལྟར་ཐོགས་ན་སྲིད་པ་ལན་བདུན་པ་ལ་སོགས་པ་ལྟར་དུས་ངེས་པར་ཡང་དག་པ་ཉིད་དུ་ངེས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 3420 [HEADING]]
##### ལོག་པ་ཉིད་དུ་ངེས་པའི་ཚོགས། ^3-1-16-2-0

[Block 3421]
ལོག་པ་ཉིད་གང་ཞེ་ན། དམྱལ་བ་རྣམས་དང་། དུད་འགྲོ་དང་། ཡི་དགས་ཏེ། འདི་ནི་ལོག་པ་ཉིད་ཅེས་བྱའོ། །

[Block 3422]
དེ་ལ་མཚམས་མེད་པ་བྱེད་པ་རྣམས་ནི་དམྱལ་བར་ངེས་པའི་ཕྱིར་ལོག་པ་ཉིད་དུ་ངེས་པ་དག་ཡིན་ནོ། །

[Block 3423 [HEADING]]
##### མ་ངེས་པའི་ཚོགས། ^3-1-16-3-0

[Block 3424]
ངེས་པ་དེ་དག་ལས་གཞན་པ་ནི་མ་ངེས་པའོ་ཞེས་བྱ་བར་གྲུབ་སྟེ། དེ་དག་ནི་རྐྱེན་ལ་ལྟོས་ན་གཉི་ག་ལ་བརྟེན་པ༌[^1956]ཉིད་དང་། གཉི་ག་ལ་མི་བརྟེན་པ་ཉིད་ཀྱང་ཡིན་ནོ། །

[Block 3425]
སེམས་ཅན་གྱི་འཇིག་རྟེན་བཤད་ཟིན་ཏོ། །

[Block 3426]
[^1957]

[Block 3427 [HEADING]]
### སྣོད་ཀྱི་འཇིག་རྟེན། ^3-2-0

[Block 3428]
ད་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་བཤད་པར་བྱ་སྟེ།

[Block 3429 [HEADING]]
#### སྣོད་ཀྱི་འཇིག་རྟེན་གནས་པ། ^3-2-1-0

[Block 3430 [HEADING]]
##### རླུང་གི་དཀྱིལ་འཁོར། ^3-2-1-1-0

[Block 3431 [VERSE]]
དེ་ལ་སྣོད་ཀྱི་འཇིག་རྟེན་གྱི། །
གནས་པར་འདོད་པའི་འོག་དག་གི། །
རླུང་གི་དཀྱིལ་འཁོར་རྔམས་སུ་ནི། །
ས་ཡ་དྲུག་འབུམ་གྲངས་མེད་དོ། །

[Block 3432]
སྟོང་གསུམ་གྱི་སྟོང་ཆེན་པོའི་འཇིག་རྟེན་གྱི་ཁམས་ནི་འདི་ལྟར་གནས་པར་འདོད་དེ། འདི་ལྟ་སྟེ། སེམས་ཅན་རྣམས་ཀྱི་ལས་ཀྱི་དབང་གིས་འོག་ན་ནམ་མཁའ་ལ་བརྟེན་པའི་རླུང་གི་དཀྱིལ་འཁོར་མངོན་པར་འགྲུབ་སྟེ། དེའི་རྔམས་སུ་ནི་དཔག་ཚད་ས་ཡ་དྲུག་འབུམ་མོ། །

[Block 3433]
རྒྱར་ནི་གྲངས་མེད་དེ། འདི་ལྟར་གང་ཚན་པོ་ཆེ་ཆེན་པོའི་རྡོ་རྗེས་ཀྱང་གཞིག་པར་མི་ནུས་པར་སྲ་བ་ཡིན་ནོ། །

[Block 3434 [HEADING]]
##### ཆུ་དང་གསེར་གྱི་དཀྱིལ་འཁོར། ^3-2-1-2-0

[Block 3435]
དེའི་སྟེང་ན།
--- END BLOCKS ---
