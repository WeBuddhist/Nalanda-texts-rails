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
[Block 141]
རང་བཞིན་ནི་གོ་རིམས་བཞིན་དུ།

[Block 142 [VERSE]]
སྲ་གཤེར་དྲོ་ཉིད་གཡོ་རྣམས་ཏེ། །
སྲ་བ་ནི་སའི་ཁམས་སོ། །
གཤེར་བ་ནི་ཆུའི་ཁམས་སོ། །
དྲོ་བ་ནི་མེའི་ཁམས་སོ། །

[Block 143]
གཡོ་བ་ནི་རླུང་གི་ཁམས་སོ། །

[Block 144]
འདིས་འབྱུང་བའི་ཡུལ་གཞན་དུ་སྐྱེད་པའི་ཕྱིར་གཡོ་བར༌[^58]བྱེད་དེ། སྒྲོན་མ་གཡོ་བ་བཞིན་དུ་གཡོ་བ་ཡིན་ནོ། །

[Block 145]
ཡང་ས་ལ་སོགས་པ་དང་སའི་ཁམས་ལ་སོགས་པ་ལ་བྱེ་བྲག་ཅི་ཡོད་ཅེ་ན།

[Block 146 [VERSE]]
འཇིག་རྟེན་གྱི་ནི་ཐ་སྙད་དུ། །
ཁ་དོག་དབྱིབས་ལས་ཞེས་བརྗོད། །

[Block 147]
འདི་ལྟར་ས་སྟོན་པ་ན༌[^59]ཁ་དོག་དང་དབྱིབས་སྟོན་པར་བྱེད་དོ། །

[Block 148]
ས་ལ་ཇི་ལྟ་བ་དེ་བཞིན་དུ། ཆུ་མེ་ཡང་ངོ་། །འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་ཁ་དོག་དང་དབྱིབས་ཉིད་ལ་བརྗོད་དོ། །

[Block 149]
རླུང་ཚོགས་ཁམས་ཉིད་ཡིན། རླུང་གི་ཁམས་གང་ཡིན་པ་དེ་ཉིད་ལ་འཇིག་རྟེན་ན་རླུང་ཞེས་འདོགས་སོ། །

[Block 150]
དེ་དང་འདྲ་བའང་ཡིན། ཁ་དོག་དང་དབྱིབས་ཀྱང་ངོ་། །ཇི་ལྟར་རླུང་ཚོགས་སྔོན་པོ་རླུང་ཚོགས་ཟླུམ་པོ་ཞེས་ཟེར་བ་བཞིན་ནོ། །

[Block 151]
འདི་ཡང་གཟུགས་སུ་རུང་བས་གཟུགས་ཀྱི་ཕུང་པོ་ཞེས་བྱ་བར་བརྗོད་དོ། །

[Block 152]
གཟུགས་སུ་རུང་བ་ནི་གནོད་པའོ། །

[Block 153]
ཐོགས་པའོ་ཞེས་ཁ་ཅིག་གིའོ། །

[Block 154]
གཟུགས་ཀྱི་ཕུང་པོའི་ངོ་བོ་ཉིད་བསྟན་པ་གང་དག་ཡིན་པ།

[Block 155 [VERSE]]
དབང་དོན་དེ་དག་ཁོ་ན་ལ། །
སྐྱེ་མཆེད་དང་ནི་ཁམས་བཅུར་འདོད། །

[Block 156]
སྐྱེ་མཆེད་རྣམ་པར་གཞག་པ༌[^60]ནི་སྐྱེ་མཆེད་བཅུ་སྟེ། མིག་གི་སྐྱེ་མཆེད་དང་། གཟུགས་ཀྱི་སྐྱེ་མཆེད་ནས། ལུས་ཀྱི་སྐྱེ་མཆེད་དང་། རེག་བྱའི་སྐྱེ་མཆེད་ཀྱི་བར་ཡིན་ནོ། །

[Block 157]
ཁམས་རྣམ་པར་གཞག་པ་ནི་དེ་དག་ཉིད་བཅུ་སྟེ། མིག་གི་ཁམས་དང་གཟུགས་ཀྱི་ཁམས་ནས་ལུས་ཀྱི་དང་རེག་བྱའི་ཁམས་ཀྱི་བར་ཡིན་ནོ། །

[Block 158]
གཟུགས་ཀྱི་ཕུང་པོ་བཤད་ཟིན་ཏོ། །

[Block 159 [HEADING]]
#### ཚོར་བའི་ཕུང་པོ། ^1-7-2-0

[Block 160]
དེ་ལ་ཚོར་བ་མྱོང་བ། མྱོང་བ་རྣམ་པ་གསུམ་ནི་ཚོར་བའི་ཕུང་པོ་སྟེ། བདེ་བ་དང་། སྡུག་བསྔལ་དང་། སྡུག་བསྔལ་ཡང་མ་ཡིན་བདེ་བ་ཡང་མ་ཡིན་པའོ། །

[Block 161]
དེ་ཡང་དབྱེ་ན་ཚོར་བའི་ཚོགས་དྲུག་སྟེ། མིག་གི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་ནས་ཡིད་ཀྱི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་བར་རོ། །

[Block 162 [HEADING]]
#### འདུ་ཤེས་ཀྱི་ཕུང་པོ། ^1-7-3-0

[Block 163]
འདུ་ཤེས་ནི་མཚན་མར་འཛིན་པའི་བདག་ཉིད་དོ། །

[Block 164]
གང་སྔོན་པོ་དང་སེར་པོ་དང་། རིང་པོ་དང་། ཐུང་ངུ་དང་། ཕོ་དང་། མོ་དང་། མཛའ་བཤེས་དང་། མཛའ་བཤེས་མ་ཡིན་པ་དང་། བདེ་བ་དང་། སྡུག་བསྔལ་བ་ལ་སོགས་པའི་རང་བཞིན་གྱི་ཁྱད་པར་ལ་མཚན་མར་འཛིན་པ་དེ་ནི་འདུ་ཤེས་ཀྱི་ཕུང་པོའོ། །

[Block 165]
དེ་ཡང་དབྱེ་ན་འདུ་ཤེས་ཀྱི་ཚོགས་དྲུག་སྟེ་ཚོར་བ་བཞིན་ནོ། །

[Block 166 [HEADING]]
#### འདུ་བྱེད་ཀྱི་ཕུང་པོ། ^1-7-4-0

[Block 167]
འདུ་བྱེད་ཕུང་པོ་བཞི་ལས་གཞན། །གཟུགས་དང་། ཚོར་བ་དང་། འདུ་ཤེས་དང་། རྣམ་པར་ཤེས་པ་ལས་གཞན་པའི་འདུ་བྱེད་རྣམས་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོའོ། །

[Block 168]
དེ་གསུམ། ཚོར་བ་དང་། འདུ་ཤེས་དང་། འདུ་བྱེད་ཀྱི་ཕུང་པོ་དག་སྟེ། སྐྱེ་མཆེད་དང་། ཁམས་རྣམ་པར་གཞག་པ་ནི། རྣམ་རིག་བྱེད་མིན་དང་།

[Block 169 [VERSE]]
འདུས་མ་བྱས་རྣམས་བཅས་པ་ནི། །
ཆོས་ཀྱི་སྐྱེ་མཆེད་ཁམས་ཞེས་བྱ། །

[Block 170]
དེ་ལྟར་རྫས་བདུན་པོ་འདི་དག་ནི་ཆོས་ཀྱི་སྐྱེ་མཆེད་དང་། ཆོས་ཀྱི་ཁམས་ཞེས་བྱའོ། །

[Block 171 [HEADING]]
#### རྣམ་པར་ཤེས་པའི་ཕུང་པོ། ^1-7-5-0

[Block 172]
རྣམ་ཤེས་སོ་སོར་རྣམ་རིག་པ། ཡུལ་དང་ཡུལ་ལས་སོ༌[^61]སོར་རྣམ་པར་རིག་ཅིང་དམིགས་པ་ནི་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་ཞེས་བྱའོ། །

[Block 173]
དེ་ཡང་རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་སྟེ། མིག་གི་རྣམ་པར་ཤེས་པ་ནས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་བར་རོ། །

[Block 174]
སྐྱེ་མཆེད་རྣམ་པར་གཞག་པ་ལ། ཡིད་ཀྱི་སྐྱེ་མཆེད་ཀྱང་དེ་ཡིན། ཁམས་རྣམ་པར་གཞག་པ་ནི། ཁམས་བདུན་དག་ཏུ་འོད༌[^62]འདོད་པ་སྟེ། །བདུན་གང་ཞེ་ན། རྣམ་པར་ཤེས་པ་དྲུག་དང་ཡིད། །མིག་གི་རྣམ་པར་ཤེས་པའི་ཁམས་ནས། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་ཡིད་ཀྱི་ཁམས་ཀྱི་བར་རོ། །

[Block 175]
དེ་ལྟར་ན་ཕུང་པོ་ལྔ་དང་། སྐྱེ་མཆེད་བཅུ་གཉིས་དང་། ཁམས་བཅོ་བརྒྱད་བསྟན་པར་འགྱུར་ཏེ། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མ་གཏོགས་པ་གཟུགས་ཀྱི་ཕུང་པོ་ནི་སྐྱེ་མཆེད་བཅུ་དང་ཁམས་བཅུ་དག་གོ། །

[Block 176]
ཚོར་བ་ལ་སོགས་པ་ཕུང་པོ་གསུམ་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་། འདུས་མ་བྱས་དག་ནི་ཆོས་ཀྱི་སྐྱེ་མཆེད་དང་ཆོས་ཀྱི་ཁམས་སོ། །

[Block 177]
རྣམ་པར་ཤེས་པའི་ཕུང་པོ་ནི་ཡིད་ཀྱི་སྐྱེ་མཆེད་དང་། རྣམ་པར་ཤེས་པའི་ཁམས་དྲུག་དང་། ཡིད་ཀྱི་ཁམས་སོ། །

[Block 178]
རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་ནི་རྣམ་པར་ཤེས་པའི་ཕུང་པོར་བཤད་པ་མ་ཡིན་ནམ། ཡང་དེ་དག་ལས་གཞན་པའི་ཡིད་ཀྱི་ཁམས་དེ་དག་གང་ཞེ་ན། གཞན་ནི་གང་ཡང་མ་ཡིན་ཏེ། དེ་དག་ཉིད།

[Block 179 [VERSE]]
དྲུག་པོ་འདས་མ་ཐག་པ་ཡི། །
རྣམ་ཤེས་གང་ཡིན་དེ་ཡིད་དོ། །

[Block 180]
རྣམ་པར་ཤེས་པ་གང་འགགས་མ་ཐག་པ་དེ་ཉིད་ནི་ཡིད་ཀྱི་ཁམས་ཞེས་བྱ་སྟེ། དཔེར་ན་བུ་ཉིད་ཕར་འགྱུར་བ་དང་། འབྲས་བུ་དེ་ཉིད་གཞན་གྱི་ས་བོན་ཡིན་པ་ལྟ་བུའོ། །
--- END BLOCKS ---
