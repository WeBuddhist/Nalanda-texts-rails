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
[Block 2136]
དེའི་འོག་ཏུ་བཤད་པའི་འགྲེས༌[^1479]ནི་སྟོང་པ་ཞེས་བྱ་བར་སོ་སོར་བརྟག༌[^1480]པར་བྱའོ་ཞེས་བྱའོ། །

[Block 2137]
སྟོང་པ་ཉིད་ཀྱི་ལྷག་མཐོང་མངོན་པར་འཕེལ་བའི་དུས་ན་ནི་ཅི་ནས་ཀྱང་དེ་ལྟར་སོ་སོར༌[^1481]བརྟགས་ནས། སེམས་གཡེང་བར་མི་འགྱུར་བ་དེ་ལྟར་སོ་སོར་བརྟག༌[^1482]པར་བྱ་སྟེ་ཞེས་བྱའོ། །

[Block 2138]
སྟོང་པ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་གྱི་དུས་ན་ནི་སེམས་མི་གཡེང་བ་དང་ལྡན་པས་ཆོས་གང་མངོན་སུམ་དུ་བྱ་བའི་ཆོས༌[^1483]དེ་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་སྟེ་ཞེས་བྱའོ། །

[Block 2139]
དེ་བཞིན་ཉིད་ཐོབ་པའི་དུས་ན་ནི་དེས་ཡང་དག་པར་རྗེས་སུ་མ་མཐོང་བས་མངོན་སུམ་དུ་མི་བྱེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནས་ལྡན་པ་ཡང་མ་ཡིན་མི་ལྡན་པ་ཡང་མ་ཡིན་པར་མཐོང་ངོ་ཞེས་བྱ་བའི་མཐའ་ལ་ཐུག་པའི་བར་གྱི་གཞུང་གིས་བསྟན་ཏེ། དམིགས་པར་བྱ་བ་དང་། དམིགས་པར་བྱེད་པ་མཉམ་པས་མཉམ་པ་རྣམ་པར་མི་རྟོག་པ་ཉིད་དུ་བསྟན་པའོ། །

[Block 2140]
དེས་ཆོས་དེ་ཡང་དག་པར་རྗེས་སུ་མ་མཐོང་བས་མངོན་སུམ་དུ་མི་བྱེད་དོ་ཞེས་བྱ་བ་ནི། ཆོས་མ་མཐོང་བ་ཉིད། དེའི༌[^1484]མངོན་སུམ་དུ་མི་བྱེད་པའི་རྒྱུའོ། །

[Block 2141]
གལ་ཏེ་མཐོང་ན་དེ་ལྟ༌[^1485]ན་ནི་མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 2142]
འོ་ན་མངོན་སུམ་བྱས་ན་ཉེས་པ་ཅིར་འགྱུར་ཞེ་ན། དེས་ཉན་ཐོས་ལྟར་ཡང་དག་པའི་མཐའ༌[^1486]མངོན་སུམ་དུ་བྱས་པར་འགྱུར་རོ། །

[Block 2143]
དེ་ལྟ་ན་ནི་དེའི་རྣམ་པར་གྲོལ་བ་ལ་སྦྱོར་བར་ཡང་འགྱུར་རོ། །

[Block 2144]
ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སྟོང་པ་ཉིད་ལ་གནས་ལ་སྟོང་པ་ཉིད་མངོན་སུམ་དུ་ཡང་མི་བགྱིད་པ་ལགས་ཞེས་བྱ་བ་ལ། སྟོང་པ་ཉིད་ནི་ཆོས་གང་མངོན་སུམ་དུ་བྱ་བ་དེ་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་ཞེས་བྱ་བའི་གནས་སུ་བསྟན་ཏོ། །

[Block 2145]
ཡང་ཆོས་དེ་ཡང་དག་པར་རྗེས་སུ་མ་མཐོང་བས་མངོན་སུམ་དུ་མི་བྱེད་དོ་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་མངོན་སུམ་དུ་མི་བྱེད་པ་བསྟན་ཏོ། །

[Block 2146]
དེ་ལ་གནས་ཀྱང་དེ་མངོན་སུམ་དུ་ཡང་མི་བྱེད་ཅེས་བྱ་བ་འདི་ཇི་ལྟར་ཤེས་པར་རུང་ཞེས་ཞུས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་དགོངས་པ་སྔ་མའི་དབང་གིས་འགྱུར་བ་བསྟན་པ། རབ་འབྱོར་གང་གི་ཚེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པའི་སྟོང་པ་ཉིད་ལ་སོ་སོར་རྟོག་པ་ན་མངོན་སུམ་དུ༌[^1487]སོ་སོར་མི་རྟོག་གོ་ཞེས་བྱ་བ་སྟེ། སྟོང་པ་ཉིད་བསྒོམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགོངས་པ་སྔ་མ་ཉིད་ཀྱིས། ཉན་ཐོས་འགོག་པ་མངོན་སུམ་དུ་བྱའོ་སྙམ་པའི་བསམ་པ་ལྟ་བུར། སྟོང་པ་ཉིད་མངོན་སུམ་དུ་བྱའོ་སྙམ་པའི་དགོངས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་ལ་མི་མངའ་སྟེ། སྟོང་པ་ཉིད་བསྒོམ་པར་བྱའོ་སྙམ་པ་ནི་རབ་ཏུ་མཐུན་པར་བྱའོ་སྙམ་དུ་དགོངས་པ་ཉིད་ཡིན་ནོ། །

[Block 2147]
དེ་བས་ན་ཕྱིས་ཀྱང་བསྒོམ་པ༌[^1488]འབའ་ཞིག་ཡིན་གྱི་མངོན་སུམ་དུ་བྱེད་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2148]
དེ་བས་ན་འདི་ནི་ཡོངས་སུ་འདྲིས་པར་བྱ་བའི་དུས་ཡིན་གྱི་འདི་ནི་མངོན་སུམ་དུ་བྱ་བའི་དུས་མ་ཡིན་ནོ་ཞེས་བྱ་བར་རྟོག་གོ་ཞེས་བྱ་བ་གསུངས་ཏེ། གང་སྟོང་པ་ཉིད་ལ་ཡོངས་སུ་འདྲིས་པར་ཡང་བྱེད་ལ། མངོན་སུམ་དུ་ཡང་མི་བྱེད་པ་དེ་ནི་ཡོངས་སུ་འདྲིས་པའི་ཤེས་པ་ཉིད་ཀྱི་མཐུ་ཡིན་ནོ། །

[Block 2149]
མཉམ་པར་མ་བཞག་པ་ཉིད་དུ་སེམས་དམིགས༌[^1489]ལ་འདོགས་ཏེ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་འདྲིས་པའི་ཤེས་པ་ཞེས་བྱ་བ་རང་བཞིན་གྱི༌[^1490]སེམས་ཡིན་གྱི། དེ་མཉམ་པར་བཞག་པ་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་སྐད་ཅིག་དེའི་ཚེ་ཞི་གནས་ནི་མེད་དོ། །

[Block 2150]
ཞི་གནས་མེད་པས་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་མི་འབྱུང་ངོ་ཞེས་སྟོན་ཏོ། །

[Block 2151 [HEADING]]
##### དུས་དང་དུས་མ་ཡིན་པ་ཤེས་པ། ^1-2-7-9-0

[Block 2152]
ད་ནི་ཡོངས་སུ་འདྲིས་པའི་ཤེས་པ། དུས་དང་དུས་མ་ཡིན་པ་ཤེས་པ་སྟོན་ཏེ་འདི་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དུས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2153]
སྐྱེས་བུ་དཔའ་བོའི་དཔེ་དང་། བྱའི་དཔེ་དང་། འཕོང་གི༌[^1491]སློབ་དཔོན་གྱི་དཔེ་དག་ཀྱང་གཞུང་དང་སྦྱར་ཏེ་གཟུང་བར་བྱའོ། །

[Block 2154]
བཅོམ་ལྡན་འདས་ངོ་མཚར་ཏོ། །

[Block 2155]
བདེ་བར་གཤེགས་པ་ངོ་མཚར་ཏོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་དུ་མཐོང་བ་རྣམས་པར༌[^1492]མ་དོར་སེམས་ཞུམ་པའི་རྒྱུས། ཏིང་ངེ་འཛིན་གསུམ་བསྒོམ་ཞིང་ཉན་ཐོས་དང་རང་བྱང་ཆུབ་ཏུ་ལྟུང་བར་མ་གྱུར་པ་སྟེ། ངོ་མཚར་ཆེའོ་ཞེས་གསོལ་པའོ། །

[Block 2156 [HEADING]]
##### སེམས་ཞུམ་པར་མི་འགྱུར་བའི་རྒྱུ། ^1-2-7-10-0

[Block 2157]
རབ་འབྱོར་འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་མ་བཏང་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པས། བཅོམ་ལྡན་འདས་ཀྱིས་འདིར་སེམས་ཞུམ་པར་མི་འགྱུར་བའི་རྒྱུ་སྟོན་ཏོ། །

[Block 2158]
འདི་ལ་ཡང་འགྲེས་བདུན་ཏེ། དམ་པ་མ་ཡིན་པའི་ཆོས་ལ་འཇུག་པའི་འགྲེས་དང་། དམིགས་པར་ལྟ་བའི༌[^1493]འགྲེས་དང་། སེམས་ཕྱིན་ཅི་ལོག་གི་འགྲེས་དང་། གང་ཟག་དང་ཆོས་སུ་རྣམ་པར་རྟོག་པའི་འགྲེས་དང་། མཚན་མའི་འགྲེས་དང་། སྨོན་ལམ་གྱི་འགྲེས་དང་། བྱང་ཆུབ་སེམས་དཔའ་ལ་དྲི་བའི་འགྲེས་སོ། །

[Block 2159 [HEADING]]
###### དམ་པ་མ་ཡིན་པའི་ཆོས་ལ་འཇུག་པའི་འགྲེས། ^1-2-7-10-1-0

[Block 2160]
དེ་ལ་སེམས་ཅན་འདི་དག་ནི་དམ་པ་མ་ཡིན་པའི་ཆོས་ལ་དམ་པར་འདུ་ཤེས་པས་བསླུས་པར་གྱུར་པ་དག་སྟེ། བདག་གིས་སེམས་ཅན་མི་ཤེས་པ་དེ་དག་ཡོངས་སུ་གཏང་བར༌[^1494]མི་བྱའོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དག་གིས་སྙིང་རྗེ་མངོན་པར་བསྐྱེད་དེ། སེམས་ཅན་ཐམས་ཅད་མི་གཏོང་བར༌[^1495]ཡིད་ལ་བྱེད་པའི་རྒྱུས། བར་མ་དོར་ཞུམ་པར་མི་འགྱུར་ཞིང་། ཡང་དག་པའི་མཐའ་མངོན་སུམ་དུ་མི་བྱེད་པ་ནི་འགྲེས་དང་པོའོ། །

[Block 2161 [HEADING]]
###### དམིགས་པར་ལྟ་བའི་འགྲེས། ^1-2-7-10-2-0

[Block 2162]
སེམས་ཅན་འདི་དག་ནི་ཡུན་རིང་པོ་ནས་བདག་དང་། སེམས་ཅན་ལ་སོགས་པར་དམིགས་པར་ལྟ་བར་སྤྱོད་སྤྱོད་པ་དག་སྟེ། དེ་དག་གི་ལྟ་བ་དེ་བདག་གིས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་ཆོས་བཤད་པས་སྤང་བར༌[^1496]བྱའོ་སྙམ་དུ་སེམས་བསྐྱེད་པའི་དབང་གིས་ཞུམ་པར་མི་འགྱུར་བ་ནི་འགྲེས་གཉིས་པའོ། །

[Block 2163 [HEADING]]
###### སེམས་ཕྱིན་ཅི་ལོག་གི་འགྲེས། ^1-2-7-10-3-0

[Block 2164]
སེམས་ཅན་འདི་དག་ནི་ཡུན་རིང་པོ་ནས་རྟག་པ་དང་། བདེ་བ་དང་སྡུག་པ་དང་། བདག་ཏུ་འདུ་ཤེས་པས་ཕྱིན་ཅི་ལོག་རྣམ་པ་བཞིས་སེམས་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་དག་སྟེ། བདག་གིས་དེ་དག་དེ་ལས་བཟློག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འགྲེས་གསུམ་པའོ། །

[Block 2165 [HEADING]]
###### གང་ཟག་དང་ཆོས་སུ་རྣམ་པར་རྟོག་པའི་འགྲེས། ^1-2-7-10-4-0

[Block 2166]
སེམས་ཅན་འདི་དག་ནི་ཡུན་རིང་པོ་ནས། སེམས་ཅན་དུ་རྣམ་པར་རྟོག་པ་དང་། གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་སུ་རྣམ་པར་རྟོག་པ་ལ༌[^1497]སྤྱོད་སྤྱོད་པ་དག་སྟེ། དེ་དག་གི་དོན་དུ་བདག་གིས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས། སྟོང་པ་ཉིད་ཀྱི་ཆོས་བཤད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བཞི་པའོ། །

[Block 2167 [HEADING]]
###### མཚན་མའི་འགྲེས། ^1-2-7-10-5-0

[Block 2168]
སེམས་ཅན་འདི་དག་ནི་ཡུན་རིང་པོ་ནས་མཚན་མ་ལ་སྤྱོད་སྤྱོད་པ་བུད་མེད་དང་། སྐྱེས་པ༌[^1498]ལ་སོགས་པའི་མཚན་མ་དང་། གཟུགས་ལ་སོགས་པ་ཆོས་རྣམས་ཀྱི་མཚན་མ་དག་ལ་སྤྱོད་སྤྱོད་པ་དག་སྟེ། དེ་དག་གི་དོན་དུ་བདག་གིས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས། མཚན་མ་མེད་པའི་ཆོས་བཤད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ལྔ་པའོ། །

[Block 2169 [HEADING]]
###### སྨོན་ལམ་གྱི་འགྲེས། ^1-2-7-10-6-0

[Block 2170]
དེ་བཞིན་དུ་སེམས་ཅན་འདི་དག་ནི་ཡུན་རིང་པོ་ནས་སྨོན་ལམ་ལ་སྤྱོད་སྤྱོད་པ། བརྒྱ་བྱིན་དང་། ཚངས་པ་དང་། འཇིག་རྟེན་སྐྱོང་བ་ལ་སོགས་པའི་དོན་དང་། གཟུགས་བཟང་པོ་ལ་སོགས་པའི་ཆོས་རྣམས་ཀྱི་དོན་དུ་སྨོན་ལམ་འདེབས་པ་དག་སྟེ། དེ་དག་གི་དོན་དུ་བདག་གིས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་སྨོན་པ་མེད་པའི་ཆོས་བཤད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དྲུག་པའོ། །

[Block 2171 [HEADING]]
###### བྱང་ཆུབ་སེམས་དཔའ་ལ་དྲི་བའི་འགྲེས། ^1-2-7-10-7-0

[Block 2172]
བྱང་ཆུབ་སེམས་དཔའ་ལ་དྲི་བ་ལ་ཡང་། གལ་ཏེ་དེ་དག་གིས་དེ་སྐད་དྲིས་པ་ལ་སྟོང་པ་ཉིད་དང་། མཚན་མ་མེད་པ་དང་། སྨོན་པ་མེད་པ་དང་། མངོན་པར་འདུ་བྱ་བ་མེད་པ་དང་། སྐྱེ་བ་མེད་པ་དང་། དངོས་པོ་མེད་པ་དག །དེ་ལྟར་ཁྱོད་ཀྱིས་ལེགས་པར་བསྒོམ་པར་བྱའོ་ཞེས་དེ་དག་ཉིད་བཟུང༌[^1499]ནས་ལན་འདེབས་ན། ལུང་བསྟན་པ་ཡིན་ནོ་ཞེས་བྱ་བར་རིག་པར་བྱ་སྟེ། ཡོངས་སུ་འདྲིས་པ་ཤེས་པའི་མཚན་ཉིད་རབ་ཏུ་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 2173]
གལ་ཏེ་དེ་དག་གིས་དེ་སྐད་དུ་དྲིས་པ་ལ་སྟོང་པ་ཉིད་སྒོམ་པ་ལ་སོགས་པ་སྤོང་ཞིང་། དེ་དག་བསྒོམ་པར༌[^1500]མི་བྱ་སྟེ། དེ་དག་མཐོང༌[^1501]ལ་རྣམ་པ་གཞན་དུ་མི་རྟག་པ་ལ་སོགས་པར༌[^1502]བསྒོམ་པར་བྱའོ་ཞེས་ལན་འདེབས་ན། ལུང་བསྟན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 2174 [HEADING]]
##### ཕྱིར་མི་ལྡོག་པའི་ས། ^1-2-7-11-0

[Block 2175]
དེ༌[^1503]ལྟར་ཕྱིར་མི་ལྡོག་པའི་བྱང་ཆུབ་སེམས་དཔས༌[^1504]ཕྱིར་མི་ལྡོག་པའི་ས་ནོན་པ་ལྟར་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ས་བརྒྱད་པ་ཐོབ་པ༌[^1505]ཕྱིར་མི་ལྡོག་པར་འགྱུར༌[^1506]ཏེ། ས་བརྒྱད་པ་ཐོབ་པ་དེ་བཞིན་དུ་དེ་དག་ལེགས་པར་ཡོངས་སུ་འདྲིས་པར་བྱས་ནས་བསྲབས་པའི༌[^1507]ས་ནོན་པ་མ་ཡིན་ཏེ། དེ་ཙམ་དུ་ཡོངས་སུ་སྨིན་པ་མ་ཡིན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
