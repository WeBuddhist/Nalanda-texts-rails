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
[Block 2171]
དེ་སྐད་དུ་བརྗོད་པའི་དགོངས་པ་ཡང་བསྟན་ཟིན་ཏོ། །

[Block 2172]
དེའི་ཕྱིར།

[Block 2173 [VERSE]]
ཡོད་ལ་རྣམ་རྟོག་དེར་འགྱུར་ཏེ། །
བྱ་བ་དངོས་དང་འབྲེལ་ཕྱིར་རོ། །

[Block 2174]
ཡོད་པ་ནི་གདོན་མི་ཟ་བར་སྐྱེ་བ༌[^1547]དང་ལྡན་པ་ལ་རག་ལས་པ་ཡིན་ནོ། །

[Block 2175]
དེ་ཡང་རང་བཞིན་ཉིད་ཡིན་ཏེ། རང་བཞིན་མེད་པ་ནི་བྱ་བ་འགའ་ཞིག་དང་ཡང་འབྲེལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2176]
བྱ་བ་ཞེས་བྱ་བ་ནི་དེ་ལྟ་བུའི་རང་བཞིན་དུ་སྐྱེད་པར་བྱེད་པ་ཡིན་ན་དེ་རང་བཞིན་མེད་པར་ཇི་ལྟར་འགྱུར། །ད་ནི་རི་བོང་གི་རྭ་མེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཇི་ལྟར་ཐ་སྙད་དུ་བྱེད་པ་ཡིན། རི་བོང་གི་རྭ་ནི་ཅུང་ཟད་ཡོད་དོ་ཞེས་མི་བརྗོད་ཀྱི། འོན་ཀྱང་འདི་ལྟར་འདི་མེད་དོ་ཞེས་ཡོད་པ་འགོག་པར་བྱེད་པ་ཉིད་ཡིན་ནོ། །

[Block 2177]
གཞན་ཡང་རྣམ་པ་འགའ་ཞིག་གིས་ཐ་སྙད་འདོགས་པ་པོས་དེ༌[^1548]འདི་ལྟར་བྱ་བ་དང་ལྡན་པ་བཞིན་དུ་སྒྲོ་བཏགས་ནས༌[^1549]སྟོན་པར་བྱེད་ཀྱི་དེ་ནི་དེ་ལྟར་མ་ཡིན་ནོ། །

[Block 2178]
དེ་ལ་དེ་ཁོ་ན་ཉིད་ནི་དོན་ཐམས་ཅད་ཀྱིས་དབེན་པ་ཡིན་གྱི། ངོ་བོ་འགའ་ཞིག་དང་ལྡན་པ་ནི་མ་ཡིན་ནོ། །

[Block 2179]
དེ་ལྟ་བུའི་འཇིག་པ་ནི་མ་ཡིན་ཏེ། དངོས་པོ་ནི་དེའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2180]
གལ་ཏེ་འཆད་པ་པོ་དག་གིས་དེ་སྐད་དུ་དེ་ཡང་བཤད་ཀྱི༌[^1550]བདག་ཉིད་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 2181]
དེའི་ཚེ་ཅུང་ཞིག་ཏུ་ཡང་མི་འགྱུར་རོ་ཞེས་བྱ་བ་འདོད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2182]
དེ་བས་ན་བདག་ཉིད་དངོས་པོའི་རང་བཞིན་ལ་དེ་ཉིད་དང་གཞན་ཉིད་ཅེས་བྱ་བའི་རྣམ་པར་རྟོག་པ་གཉིས་ལས་འདས་པ་མ་ཡིན་ན། [^1551]དེ་ཁོ་ན་ཉིད་མ་ཡིན་པའི་རང་བཞིན་ནི་གཞན་ཉིད་ཡིན་ནོ། །

[Block 2183]
གཟུགས་དང་རོ་དག་ཀྱང་ཕན་ཚུན་གཞན་ཉིད་དུ་གྱུར་པ་ནི་གཞན་ཉིད་མ་ཡིན་པ་ལྟ་བུའོ། །

[Block 2184]
གལ་ཏེ་རང་བཞིན་ལ་རག་ལུས་པ་མེད་པ་ནི་གཞན་ཉིད་ཡིན་ནོ་ཞེ་ན། རག་ལུས་པ་ཞེས་བྱ་བ་འདི་གང་ཡིན། གང་གིས་དེར་ཡང་མི་འགྱུར་བ་དང་། རང་བཞིན་གཞན་དུའང་མི་འགྱུར། གལ་ཏེ་སྐྱེ་བ་ཡིན་ནོ་ཞེ་ན། རྒྱུ་དང་འབྲས་བུ་ཐམས་ཅད་ཕན་ཚུན་བརྗོད་པར་བྱ་བ་ཉིད་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 2185]
དེ་ལྟར་ན་ཐམས་ཅད་ལ་ཐམས་ཅད་རྣམ་པ་འགའ་ཞིག་གིས་ཉེ་བར་སྦྱོར་བའི་ཕྱིར་འགའ་ཞིག་ཀྱང་གཞན་དུ་མི་འགྱུར་རོ། །

[Block 2186]
འདིས་བརྗོད་པར་བྱ་བ་ཉིད་མ་ཡིན་པ་དེ་ལྟར་ན་ཡང་རྒྱུ་དང་འབྲས་བུའི་ངོ་བོ་ཉིད་སྒྲ་གཞན་གྱིས་བསྟན་པར་འགྱུར་རོ། །

[Block 2187]
དོན་གཞན་ཐ་དད་པ་ནི་མ་ཡིན་ཏེ། རང་བཞིན་གྱི་རྗེས་སུ་འགྲོ་བ་ཉིད་མ་ཡིན་པ་ཉིད་གཞན་ཉིད་ཡིན༌[^1552]པར་སྨྲའོ། །

[Block 2188]
དེ་ཡང་རང་བཞིན་དང་ལྡན་པ་གཞན་དང་གཞན་དུ་ཡོད་པ་དེ་ལྟར་ན་གཞན་ཉིད་ཡིན་ནོ། །

[Block 2189]
དེའི་སྐྱེ་བའི་མཚན་ཉིད་ཀྱི༌[^1553]རང་བཞིན་གྱི་རག་ལས་པ༌[^1554]ལས་རག་ལུས་པ་གཞན་ཡང་ཡོད་པ་མ་ཡིན་ཏེ། རག་ལུས་པ་མེད་པའི་འཁྲུལ་པ་ལ་འགལ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2190]
དེ་དང་ཆོས་ཐ་དད་པས་གཞན་ཉིད་ཡིན་ནོ། །

[Block 2191]
གལ་ཏེ་ཤེས་པས་བྱས་པའི་རག་ལུས་པ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟར་ནི་འགྱུར་ན་གང་རྟོགས་པ་མེད་ན་མི་འབྱུང་བའི་ཤེས་པ་གང་ཡིན་པ་དེས་རྟོགས་པ༌[^1555]ལ་ངེས་པར་དེ་སྣང་བའི་ཕྱིར་དེ་དེའི་ངོ་བོ་མ་ཡིན་དུ་ཟིན་ཀྱང་། བརྗོད་པར་བྱ་བ་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ནི་བདག་ཉིད་རང་མེད་པ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2192]
དེ་ཉིད་ནི་སྣང་བ་གང་ཡིན་པ་དེའི་རང་བཞིན་ཡིན་ནོ། །

[Block 2193]
རང་བཞིན་དང་ལྡན་པ་ཉིད་ཡིན་ན་འདི་དེ༌[^1556]དང་འདྲ་བར་སྣང་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར། སྣང་དུ་རུང་བ་མི་སྣང་ན་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 2194]
མི་སྣང་བ་ཉིད་ཡིན་ན་ཡང་དེའི་ངོ་བོ་ཤེས་པ་མ་ཡིན་པ་དེ་ལྟར་ན་གང་གང་ལ་རག་ལུས་པ་ཤེས་པ་ཡིན། གང་ལ་རག་ལུས་པ་ཤེས་པ་ཅན་གང་ཡིན་པ་དེའི་རང་བཞིན་སྣང་བ་ནི་ཉམས་པ་མ་ཡིན་ཏེ། སྔོན་པོ་ལ་སོགས་པ་སྣང་བ་ལ་རག་ལུས་པའི་ཤེས་པ་ཅན་དག་བཞིན་ནོ། །

[Block 2195]
དེ་ལ༌[^1557]དོན་དེ་ཉེ་བ་གང་ཡིན། གང་གིས་དེ་ལ་བདག་མེད་པའི་ངོ་བོར་རྟོགས་པར་འགྱུར་བ་ན།[^1558] བདག་ཉིད་སོ་སོར་ཉེ་བར་གནས་སོ། །

[Block 2196]
དེ་ལྟར་ན་ནི་ཤིན་ཏུ་ཐལ་བར་འགྱུར་རོ། །

[Block 2197]
གལ་ཏེ་རྟོགས་པར་འགྱུར་བ་དེ༌[^1559]དག་གི་ཉེ་བར་ལེན་པ་ཅན་ཡིན༌[^1560]ནོ་ཞེ་ན། ཉེ་བར་ལེན་པའི་དོན་འདི་གང་ཡིན། རྒྱུ་དང་འབྲས་བུའི་ངོ་བོ་ཡང་མ་ཡིན་ཏེ། ཁས་མི་ལེན་པའི་ཕྱིར་རོ། །

[Block 2198]
ཁས་ལེན་ན་ཡང་རྒྱུ་དང་འབྲས་བུ་དག་ཕན་ཚུན་རྟོགས་པ་ཉེ་བར་འཇོག་པ་ཅན་དག་མ་ཡིན་ནོ། །

[Block 2199]
གལ་ཏེ་ཤེས་པ་ཉིད་ཀྱི་དེ་མེད་ན་མི་འབྱུང་བ་ཉེ་བ༌[^1561]ཡིན་ནོ་ཞེ་ན། དེ་ཉིད་རག་ལུས་པ་མེད་པ་མེད་པར་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བརྗོད་པ་མ་ཡིན་ནམ། རྒྱུ་དང་འབྲས་བུ་མ་ཡིན་པ་དག་ལ་ནི་རག་ལུས་པ་ཅུང་ཟད་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 2200]
གང་རྟོགས་པ་མེད་ན་མི་འབྱུང་བའི་ཤེས་པ་གང་ཡིན་པ་ཞེས་བྱ་བ་འདིའི་ཤེས་པ་ཡང་ཡོད་པར་འགྱུར་ན། རྣམ་པར་ཤེས་པ་ལ་རང་གི་ངོ་བོ་མ་ཡིན་པ་དང་འདྲེས་པ་མེད་པར་སྣང་བ་གང་ཡིན་པ་དེ་ནི་ཤེས་པ་ཅུང་ཞིག་ཀྱང་མ་ཡིན་ནོ། །

[Block 2201]
དེ་མེད་པའི་ཕྱིར་དོན་གྱི་ངོ་བོ་བརྗོད་པར་བྱ་བ་མ་ཡིན་པའི་མཚན་ཉིད་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 2202]
དེ་བས་ན་དོན་དམ་པར་ཡོད་པ༌[^1562]ཉིད་ཀྱིས་དེ་ཉིད་གཞན་ཉིད་ལ་བརྟེན་པར་འགྱུར་རོ། །

[Block 2203]
གང་གི་དངོས་པོ་འཇིག་པའི་ངང་ཚུལ་ཅན་ནི་ཅིར་ཡང་མི་འགྱུར་བ་དེས་ནི། མེད་པར་འགྱུར་ཞེས་བརྗོད་པ་ན། དངོས་འགྱུར་མིན་ཞེས་བྱ་བ་ཡིན། །གལ་ཏེ་འདིས་དངོས་པོ་མེད་པར་འགྱུར་རོ། །ཞེས་བརྗོད་པ་དེ་ལྟར་ན་ཡང་དངོས་པོར་མི་འགྱུར་རོ། །ཞེས་བྱ་བ་བསྟན་པར་འགྱུར་རོ། །

[Block 2204]
དེ་ལྟར་ན་དེ་ལོག་པར་འགྱུར་ཏེ། དགག་པ་སྒྲུབ་པ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2205]
དེ་ཉིད་ཀྱི་ཕྱིར་འདི་འཇིག་པ་ལ་རྒྱུ་ཅུང་ཟད༌[^1563]ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2206]
དེ་ལྟར་ན།

[Block 2207 [VERSE]]
གལ་ཏེ་བྱ་བ་ཅུང་ཟད་ཅིག །
ཡོད་ན་གཞན་ལ་ལྟོས་འགྱུར་ན། །
དངོས་གང་ཅུང་ཞིག་མི་བྱེད་ལ། །
ཅི་ཕྱིར༌[^1564]འགའ་ཞིག་གིས་ལྟོས་འགྱུར། །

[Block 2208]
བྱ་བ་ཡོད་ན་བྱེད་པར་འགྱུར་ཏེ། དངོས་པོ་འཇིག་པའི་ངང་ཚུལ་ཅན་ལ་བྱ་བ་ཅུང་ཟད་ཀྱང་མེད་དོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2209]
དེ་བས་ན་འཇིག་པའི་རྒྱུ་ཞེས་བྱ་བ་དེ་ནི་དངོས་པོ་ལ་ཅུང་ཞིག་ཀྱང་མི་བྱེད་པ་དེ་ལྟར་ན་ཅུང་ཞིག་མི་བྱེད་པ་ལ་ལྟོས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2210]
དེ་ནི་དངོས་པོ་ཕུལ་དུ་བྱུང་བ་སྐྱེ་བ་མེད་པ་ཅན་དེའི་གནས་སྐབས་ཅན༌[^1565]ཉིད་ཇི་ལྟར་ན་འཇིག་པ་ཞེས་བྱ། ཕུལ་དུ་བྱུང་བ་སྐྱེ་བ་ཡིན་ན་ཡང་དེ་ཉིད་དེའི་ཕུལ་དུ་བྱུང་བ་སྐྱེ་བ་ཞེས་བྱ་བ་མ་ཡིན་ནམ། དེ་ཇི་ལྟར་ན་འཇིག་པ་ཞེས་བྱ། དེས་ན་དེའི་གནས་སྐབས་ཅན་འདི་འཇིག་པ་ཞེས་བྱ་བ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
