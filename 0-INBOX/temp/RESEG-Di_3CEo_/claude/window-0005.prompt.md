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

[Block 181]
དེ་ལྟ༌[^63]ན་འོ་ན་ནི་རྣམ་པར་ཤེས་པའི་ཁམས་དྲུག་དང་། ཡིད་ཀྱི་རྣམ་ཤེས་གཅིག་གི་ནང་དུ་གཅིག་འདུས་པའི་ཕྱིར་རྫས་སུ་ན་ཁམས་བཅུ་བདུན་ནམ་བཅུ་གཉིས་སུ་འགྱུར་རོ། །

[Block 182]
དེ་ལྟ་འང་ཡིན་མོད་ཀྱི་འོན་ཀྱང་།

[Block 183 [VERSE]]
དྲུག་པའི་རྟེན་ནི་རབ་བསྒྲུབ་ཕྱིར། །
ཁམས་ནི་བཅོ་བརྒྱད་དག་ཏུ་འདོད། །

[Block 184]
རྣམ་པར་ཤེས་པའི་ཁམས་ལྔ་པོ་དག་གི་རྟེན་ལྔ་ནི་མིག་གི་ཁམས་ལ་སོགས་པ་ཡིན་ན༌[^64]

[Block 185]
དྲུག་པ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་ཀྱི་རྟེན་ནི་གཞན་མེད་དོ། །

[Block 186]
དེའི་ཕྱིར་རྟེན་རབ་ཏུ་བསྒྲུབ་པའི་ཆེད་དུ་ཡིད་ཀྱི་ཁམས་བསྟན་ཏོ། །

[Block 187]
དེ་ལྟར་ན་རྟེན༌[^65]དང་བརྟེན་པ་དང་དམིགས་པ་དྲུག་ཚན༌[^66]རྣམ་པར་གཞག་པས་ཁམས་བཅོ་བརྒྱད་དུ་འགྱུར་རོ། །

[Block 188 [HEADING]]
### བསྡུ་བ། ^1-8-0

[Block 189]
དེ་ལ་ཕུང་པོ་དེ༌[^67]དག་གིས་ནི་འདུས་བྱས་ཐམས་ཅད་བསྡུས༌[^68]སོ། །

[Block 190]
ཉེ་བར་ལེན་པའི་ཕུང་པོ་དག་གིས་ནི་ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་བསྡུས་སོ། །

[Block 191]
སྐྱེ་མཆེད་དང་ཁམས་དག་གིས་ནི་ཆོས་ཐམས་ཅད་བསྡུས་སོ། །

[Block 192]
མདོར་བསྡུ་ན། ཕུང་པོ་དང་ནི་སྐྱེ་མཆེད་དང་། །ཁམས་གཅིག་གིས་ནི་ཐམས་ཅད་བསྡུས་པར་ཤེས་པར་བྱ་སྟེ། གཟུགས་ཀྱི་ཕུང་པོ་དང་། ཡིད་ཀྱི་སྐྱེ་མཆེད་དང་། ཆོས་ཀྱི་ཁམས་ཀྱིས་ཆོས་ཐམས་ཅད་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 193]
བསྡུ་བ་དེ་དག་ནི་གང་དང་གང་ནས་འབྱུང༌[^69]ཡང་རུང་། རང་གི་ངོ་བོ་ཉིད་ཀྱིས་ཏེ། གཞན་གྱི༌[^70]དངོས་པོས་ནི་མ་ཡིན་པར་རིག་པར་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། གཞན་གྱི་དངོས་དང་མི་ལྡན་ཕྱིར། །ཆོས་ནི་གཞན་གྱི་དངོས་པོ་དང་མི་ལྡན་པའི་ཕྱིར་རོ། །

[Block 194]
དེ་ལྟ་བས་ན་གང་དང་མི་ལྡན་པ་དེ་ཉིད་ཀྱིས་བསྡུས་པར་ཡང་མི་རུང་ངོ་། །མིག་དང་། རྣ་བ་དང་སྣ་དག་གཉིས་གཉིས་ཡོད་པའི་ཕྱིར་ཁམས་ཉི་ཤུ་རྩ་གཅིག་ཏུ་འགྱུར་བ་མ་ཡིན་ནམ་ཞེ་ན། [^71]མི་འགྱུར་ཏེ། གང་གི་ཕྱིར།

[Block 195 [VERSE]]
མིག་ལ་སོགས་པ་གཉིས་མོད་ཀྱི། །
རིགས་དང་སྤྱོད་ཡུལ་རྣམ་པར་ཤེས། །
འདྲ་བའི་ཕྱིར་ན་ཁམས་གཅིག་ཉིད། །

[Block 196]
དེ་ལ་རིགས་འདྲ་བ་ནི་གཉིས་ཀ་མིག་གི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 197]
སྤྱོད་ཡུལ་འདྲ་བ་ནི་གཉིས་ཀའི་ཡུལ་གཟུགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 198]
རྣམ་པར་ཤེས་པ་འདྲ་བ་ནི་གཉིས་ཀ་མིག་གི་རྣམ་པར་ཤེས་པ་གཅིག་གི་རྟེན་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན་མིག་གི་ཁམས་ནི་གཅིག་པ་ཉིད་དོ། །

[Block 199]
དེ་བཞིན་དུ་རྣ་བ་དང་། སྣ་དག་ལ་ཡང་སྦྱོར་བར༌[^72]བྱའོ། །

[Block 200]
མཛེས་བྱའི་ཕྱིར་ན་གཉིས་བྱུང་ངོ་། །མིག་ལ་སོགས་པའི་ཁམས་གཅིག་པ་ཉིད་ཡིན༌[^73]ཡང་རྟེན་མཛེས་པར་བྱ་པའི་ཕྱིར་གཉིས་བྱུང་ངོ་། །ཕུང་པོ་དང་། ཁམས་དང་སྐྱེ་མཆེད་དག་བཤད་ཟིན་ཏོ། །

[Block 201 [HEADING]]
### ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ཀྱི་དོན། ^1-9-0

[Block 202]
ཕུང་པོ་དང་། ཁམས་དང་སྐྱེ་མཆེད་ཀྱི་དོན་གང་ཡིན་པ་འདིར་བརྗོད་པར་བྱ་སྟེ།

[Block 203 [VERSE]]
སྤུངས་དང་སྐྱེ་སྒོ་རིགས་ཀྱི་དོན། །
ཕུང་པོ་སྐྱེ་མཆེད་ཁམས་རྣམས་ཡིན། །
སྤུངས་པའི་དོན་ནི་ཕུང་པོའི་དོན་ཏོ། །

[Block 204]
སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་སྐྱེ་བའི་སྒོའི་དོན་ནི་སྐྱེ་མཆེད་ཀྱི་དོན་ཏོ། །

[Block 205]
རིགས་ཀྱི་དོན་ནི་ཁམས་ཀྱི་དོན་ཏོ། །

[Block 206]
རིགས་ཀྱང་འབྱུང་གནས་སོ། །

[Block 207 [HEADING]]
### ཕུང་པོ་ལ་སོགས་པའི་སྒོ་ནས་བསྟན་པ་རྣམ་པ་གསུམ། ^1-10-0

[Block 208]
ཡང་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ཕུང་པོ་ལ་སོགས་པའི་སྒོ་ནས་བསྟན་པ་རྣམ་པ་གསུམ་རྩོམ་པར་མཛད་ཅེ་ན། སྨྲས་པ། གདུལ་བྱ་རྣམས་ཀྱི།

[Block 209 [VERSE]]
རྨོངས་དབང་འདོད་རྣམས་གསུམ་གྱི་ཕྱིར། །
ཕུང་པོ་ལ་སོགས་གསུམ་བསྟན་ཏོ། །

[Block 210]
སེམས་ཅན་རྣམས་ཀྱི་རྨོངས་པ་ནི་རྣམ་པ་གསུམ་སྟེ། ཁ་ཅིག་སེམས་ལས་བྱུང་བ་རྣམས་ལ་རིལ་པོའི༌[^74]བདག་ཏུ་འཛིན་པས་རྨོངས་སོ། །

[Block 211]
ཁ་ཅིག་ནི་གཟུགས་ཁོ་ན་ལའོ། །

[Block 212]
ཁ་ཅིག་ནི་གཟུགས་དང་སེམས་དག་ལའོ། །

[Block 213]
དབང་པོ་དག་ཀྱང་རྣམ་པ་གསུམ་སྟེ། དབང་པོ་རྣོན་པོ་དང་། འབྲིང༌[^75]དང་། རྟུལ༌[^76]པོའི་ཕྱིར་རོ། །

[Block 214]
འདོད་པ་ཡང་རྣམ་པ༌[^77]གསུམ་སྟེ། བསྡུས་པ་དང་། བར་མ་དང་། རྒྱ་ཆེན་པོ་འདོད་པའི་ཕྱིར་ཏེ། དེ་དག་ལ་གོ་རིམས་བཞིན་དུ་ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་གསུམ་བསྟན་ཏེ༌[^78]ཞེས་གྲག་གོ། །

[Block 215 [HEADING]]
### ཚོར་བ་དང་འདུ་ཤེས་ལོགས་ཤིག་ཕུང་པོར་གཞག་པ། ^1-11-0
--- END BLOCKS ---
