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
[Block 246]
དེ་ཡང་དབྱེ་ན་ཚོར་བའི་ཚོགས་དྲུག་སྟེ། མིག་གི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་ནས། ཡིད་ཀྱི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བའི་བར་རོ། །

[Block 247 [HEADING]]
##### འདུ་ཤེས་ཀྱི་ཕུང་པོ། ^1-1-3-3-0

[Block 248]
འདུ་ཤེས་ནི། མཚན་མར་འཛིན་པའི་བདག་ཉིད་དོ། །

[Block 249]
གང་སྔོན་པོ་དང་། སེར་པོ་དང་། རིང་པོ་དང་། ཐུང་ངུ་དང་། ཕོ་དང་། མོ་དང་། མཛའ་བཤེས་དང་། མཛའ་བཤེས་མ་ཡིན་པ་དང་། བདེ་བ་དང་། སྡུག་བསྔལ་བ༌[^101]ལ་སོགས་པའི་རང་བཞིན་གྱི་ཁྱད་པར་ལ་མཚན་མར་འཛིན་པ་དེ་ནི་འདུ་ཤེས་ཀྱི་ཕུང་པོའོ། །

[Block 250]
དེ་ཡང་དབྱེ་ན་འདུ་ཤེས་ཀྱི་ཚོགས་དྲུག་སྟེ། ཚོར་བ་བཞིན་ནོ། །

[Block 251 [HEADING]]
##### འདུ་བྱེད་ཀྱི་ཕུང་པོ། ^1-1-3-4-0

[Block 252]
འདུ་བྱེད་ཕུང་པོ་བཞི་ལས་གཞན། །གཟུགས་དང་། ཚོར་བ་དང་། འདུ་ཤེས་དང་། རྣམ་པར་ཤེས་པ་དང་ཕུང་པོ་བཞི་ལས་གཞན་པའི་འདུ་བྱེད་རྣམས་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོའོ། །

[Block 253]
བཅོམ་ལྡན་འདས་ཀྱིས་མདོ་ལས།

[Block 254]
སེམས་པ༌[^102]ཚོགས་དྲུག་གོ་ཞེས་གསུངས་པ་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ནི་ལས་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་མངོན་པར་འདུ་བྱ་བ་ལ་གཙོ་བོ་ཡིན་ནོ། །

[Block 255]
དེ་ཉིད་ཀྱི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས། འདུས་བྱས་མངོན་པར་འདུ་བྱེད་དེ། དེ་ལྟ་བས་ན་འདུ་བྱེད་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ཞེས༌[^103]གསུངས་སོ། །

[Block 256]
དེ་ལྟ་མ་ཡིན་ན་སེམས་ལས་བྱུང་བ་ལྷག་མ་རྣམས་དང་ལྡན་པ་མ་ཡིན་པ་རྣམས་ཕུང་པོར༌[^104]འདུས་པའི་ཕྱིར་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བའི་བདེན་པ་ཉིད་དུ་མི་འགྱུར་བས་ཡོངས་སུ་ཤེས་པ་དང་སྤང་བར་ཡང༌[^105]མི་འགྱུར་རོ། །

[Block 257]
བཅོམ་ལྡན་འདས་ཀྱིས་ནི། ཆོས་གཅིག་མངོན་པར་མ་ཤེས་ཤིང་ཡོངས་སུ་མ་ཤེས་པར་ཡང་སྡུག་བསྔལ་གྱི་མཐར་བྱེད་པར་ང་མི་སྨྲའོ་ཞེས་གསུངས་ལ། དེ་བཞིན་དུ་མ་སྤངས་པར་ཡང་ཞེས་གསུངས་ཏེ། དེ་ལྟ་བས་ན༌[^106]གདོན་མི་ཟ་བར་དེ་དག་འདུ་བྱེད་ཀྱི་ཕུང་པོར་བསྡུས་པར་ཁས་བླང་བར་བྱའོ། །

[Block 258 [HEADING]]
##### ཆོས་ཀྱི་སྐྱེ་མཆེད་དང་ཆོས་ཀྱི་ཁམས། ^1-1-3-5-0

[Block 259]
དེ་གསུམ། ཚོར་བ་དང་། འདུ་ཤེས་དང་། འདུ་བྱེད་ཀྱི་ཕུང་པོ་དག་སྟེ། སྐྱེ་མཆེད་དང་། ཁམས་རྣམ་པར་གཞག་པ་ནི། རྣམ་རིག་བྱེད་མིན་དང་།

[Block 260 [VERSE]]
འདུས་མ་བྱས་རྣམས་བཅས་པ་ནི། །
ཆོས་ཀྱི་སྐྱེ་མཆེད་ཁམས་ཞེས་བྱ། །

[Block 261]
དེ་ལྟར་ན་རྫས་བདུན་པོ་དེ་དག་ནི་ཆོས་ཀྱི་སྐྱེ་མཆེད་དང་། ཆོས་ཀྱི་ཁམས་ཞེས་བྱའོ། །

[Block 262 [HEADING]]
##### རྣམ་པར་ཤེས་པའི་ཕུང་པོ། ^1-1-3-6-0

[Block 263]
རྣམ་ཤེས་སོ་སོར་རྣམ་རིག་པ། །ཡུལ་དང་ཡུལ་ལ་སོ་སོར་རྣམ་པར་རིག་ཅིང་དམིགས་པ་ནི་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་ཞེས་བྱའོ། །

[Block 264]
དེ་ཡང་རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་སྟེ། མིག་གི་རྣམ་པར་ཤེས་པ་ནས། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་བར་རོ། །

[Block 265]
རྣམ་པར་ཤེས་པའི་ཕུང་པོ་བསྟན་པ་གང་ཡིན་པ༌[^107]དེ་སྐྱེ་མཆེད་རྣམ་པར་གཞག་པ་ནི། ཡིད་ཀྱི་སྐྱེ་མཆེད་ཀྱང་དེ་ཡིན། ཁམས་རྣམ་པར་གཞག་པ་ཡང་དེ་དག་ཉིད། ཁམས་བདུན་དག་ཏུའང་འདོད་པ་སྟེ། བདུན་གང་ཞེ་ན། རྣམ་པར་ཤེས་པ་དྲུག་དང་ཡིད། །མིག་གི་རྣམ་པར་ཤེས་པའི་ཁམས་ནས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་། ཡིད་ཀྱི་ཁམས་ཀྱི་བར་རོ། །

[Block 266]
དེ་ལྟར་ན་འདིར་ཕུང་པོ་ལྔ་དང་། སྐྱེ་མཆེད་བཅུ་གཉིས་དང་། ཁམས་བཅོ་བརྒྱད་དུ་བསྟན་པར་འགྱུར་ཏེ། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མ་གཏོགས་པ་གཟུགས་ཀྱི་ཕུང་པོའི་སྐྱེ་མཆེད་བཅུ་དང་། ཁམས་བཅུ་དག་གོ། །

[Block 267]
ཚོར་བ་ལ་སོགས་པ་ཕུང་པོ་གསུམ་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་། འདུས་མ་བྱས་དག་ནི་ཆོས་ཀྱི༌[^108]སྐྱེ་མཆེད་དང་། ཆོས་ཀྱི་ཁམས་སོ། །

[Block 268]
རྣམ་པར་ཤེས་པའི་ཕུང་པོ་ནི་ཡིད་ཀྱི་སྐྱེ་མཆེད་དང་། རྣམ་པར་ཤེས་པའི་ཁམས་དྲུག་དང་། ཡིད་ཀྱི་ཁམས་སོ། །

[Block 269]
རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་ནི་རྣམ་པར་ཤེས་པའི་ཕུང་པོར་བཤད་པ་མ་ཡིན་ནམ། ཡང་དེ་དག་ལས་གཞན་པ་ཡིད་ཀྱི་ཁམས་དེ་གང་ཞེ་ན། གཞན་ནི་གང་ཡང་མེད་དོ། །

[Block 270]
འོ་ན་ཅི་ཞེ་ན། དྲུག་པོ་དེ་དག །

[Block 271 [VERSE]]
ཉིད་ལས་འདས་མ་ཐག་པ་ཡི། །
རྣམ་ཤེས་གང་ཡིན་དེ་ཡོད༌[^109]དོ། །

[Block 272]
རྣམ་པར་ཤེས་པ་གང་དང་གང་འགགས་མ་ཐག་པ་དེ་ཉིད་ནི་ཡིད་ཀྱི་ཁམས་ཞེས་བྱ་སྟེ། དཔེར་ན་བུ་དེ་ཉིད་གཞན་གྱི་ཕར་འགྱུར་བ་དང་། འབྲས་བུ་དེ་ཉིད་གཞན་གྱི་ས་བོན་ཡིན་པ་ལྟ་བུའོ། །

[Block 273]
དེ་ལྟ༌[^110]ན་འོ་ན་ནི་རྣམ་པར་ཤེས་པའི་ཁམས་དྲུག་དང་ཡིད་ཀྱི་ཁམས་རྣམས་གཅིག་གི་ནང་དུ་གཅིག་འདུས་པའི་ཕྱིར་རྫས་སུ་ན་ཁམས་བཅུ་བདུན་ནམ་བཅུ་གཉིས་སུ་འགྱུར་ན་ཅིའི་ཕྱིར་ཁམས་བཅོ་བརྒྱད་དུ་རྣམ་པར་གཞག་ཅེ་ན། དེ་ལྟའང་ཡིན་མོད་ཀྱི། འོན་ཀྱང་།

[Block 274 [VERSE]]
དྲུག་པའི་རྟེན་ནི་རབ་བསྒྲུབ༌[^111]ཕྱིར། །
ཁམས་ནི་བཅོ་བརྒྱད་དག་ཏུ་འདོད། །

[Block 275]
རྣམ་པར་ཤེས་པའི་ཁམས་ལྔ་པོ་དག་གི་རྟེན་ལྔ་ནི་མིག་གི་ཁམས་ལ་སོགས་པ་ཡིན་ན་དྲུག་པོ༌[^112]ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་ཀྱི་རྟེན་ནི་གཞན་མེད་དེ། [^113]དེའི་ཕྱིར་དེའི་རྟེན་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར་ཡིད་ཀྱི་ཁམས་བསྟན་ཏོ། །

[Block 276]
དེ་ལྟར་ན་རྟེན་དང་བརྟེན་པ་དང་དམིགས་པ་དྲུག་ཚན་རྣམ་པར་གཞག་པས་ཁམས་བཅོ་བརྒྱད་དག་ཏུ་འགྱུར་རོ། །

[Block 277]
འོ་ན་ནི་དགྲ་བཅོམ་པའི་སེམས་ཐ་མ་ཡིད་མ་ཡིན་པར་འགྱུར་ཏེ། དེ་གང་གིས་མཚུངས་པ་དེ་མ་ཐག་པ་འདས་པར་འགྱུར་བ་དེ་ནི་མེད་དོ་ཞེ་ན། དེ་ཡང་ཡིད་ཀྱི་ངོ་བོར་གནས་པའི་ཕྱིར་ན་མ་ཡིན་ཏེ། རྒྱུ་གཞན་མ་ཚང་བའི་ཕྱིར་རྣམ་པར་ཤེས་པ་ཕྱི་མ་མི་སྐྱེ་བར་ཟད་དོ། །

[Block 278 [HEADING]]
#### བསྡུ་བ། ^1-1-4-0

[Block 279]
དེ་ལ་ཕུང་པོ་དག་གིས་ནི་འདུས་བྱས་ཐམས་ཅད་བསྡུས་སོ། །

[Block 280]
ཉེ་བར་ལེན་པའི་ཕུང་པོ་དེ༌[^114]དག་གིས་ནི་ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་བསྡུས་སོ། །

[Block 281]
སྐྱེ་མཆེད་དང་ཁམས་དག་གིས་ནི་ཆོས་ཐམས་ཅད་བསྡུས་སོ། །

[Block 282]
མདོར་བསྡུ་ན་ཕུང་པོ་དང་ནི་སྐྱེ་མཆེད་དང་། ཁམས་གཅིག་གིས་ནི་ཐམས་ཅད་བསྡུས་པར་ཤེས་པར་བྱ་སྟེ། གཟུགས་ཀྱི་ཕུང་པོ་དང་ཡིད་ཀྱི་སྐྱེ་མཆེད་དང་ཆོས་ཀྱི་ཁམས་ཀྱིས་ཆོས་རྣམས༌[^115]ཐམས་ཅད་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 283]
བསྡུ་བ་དེ་ནི་གང་དང་གང་ནས་འབྱུང་ཡང་རུང་། རང་གི་ངོ་བོ་ཉིད་ཀྱིས་ཏེ། གཞན་གྱི་དངོས་པོས་ནི་མ་ཡིན་པར་རིག་པར་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། གཞན་གྱི་དངོས་དང་མི་ལྡན་ཕྱིར། །ཆོས་ནི་གཞན་གྱི་དངོས་པོ་དང་མི་ལྡན་ནོ། །

[Block 284]
དེ་ལྟ་བས་ན་གང་དང་མི་ལྡན་པ་དེ་ཉིད་ཀྱིས་བསྡུས་པར་ནི་མི་རུང་སྟེ། དཔེར་ན་མིག་གི་དབང་པོ་ནི་གཟུགས་ཀྱི་ཕུང་པོ་དང་། མིག་གི་སྐྱེ་མཆེད་དང་། ཁམས་དག་དང་། སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་བའི་བདེན་པ་དག་གིས་བསྡུས་ཏེ། དེ་དག་གི༌[^116]ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 285]
དེ་དག་གི༌[^117]ངོ་བོ་དང་མི་ལྡན་པའི་ཕྱིར་ཕུང་པོ་ལ་སོགས་པ་གཞན་དག་གིས་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
