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
[Block 421 [VERSE]]
མདོར་བསྡུ་བ་ནི་འདི་ཡིན་ནོ། །
ཉོན་མོངས་ཅན་མིན་མཐོང་སྤང་མིན། །
གཟུགས་མིན་དྲུག་པ་མིན༌[^162]སྐྱེས་མིན།[^163] །

[Block 422]
ཉོན་མོངས་པ༌[^164]ཅན་མ་ཡིན་པ་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་ཅུང་ཟད་ཀྱང་མེད་ལ། གཟུགས་ཀྱང་མ་ཡིན་ནོ། །

[Block 423]
སོ་སོའི་སྐྱེ་བོ་ཉིད་ནི་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་ལུང་དུ་མ་བསྟན་པ་ཡིན་ཏེ། དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པ་དང་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཀྱང་དེ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 424]
ལུས་དང་ངག་གི་ལས་ནི་གཟུགས་ཡིན་ནོ། །

[Block 425]
དེ་ལྟ་བས་ན་དེ་དག་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་མ་ཡིན་ཏེ། བདེན་པ་དག་ལ་ལོག་པར་མི་རྟོག་པའི་ཕྱིར་རོ། །

[Block 426]
དྲུག་པ་མ་ཡིན་པ་ལས་སྐྱེས་པ་ནི་དབང་པོ་ལྔ་ལས་སྐྱེས་པ་གང་ཡིན་པ་སྟེ། དེ་ཡང་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་མེད་དོ། །

[Block 427 [HEADING]]
#### ལྟ་བ། ^1-18-17-0

[Block 428]
ལྟ་བ་ནི་དུ། ལྟ་བ་མ་ཡིན་པ་ནི་དུ་ཞེ་ན། མིག་དང་ཆོས་ཀྱི་ཁམས་ཕྱོགས་ནི། ལྟ་བ་ཡིན་ཏེ། དེ་དག་གང་ཞེ་ན། སྨྲས་པ། རྣམ་པ་བརྒྱད། འཇིག་ཚོགས་ལ་ལྟ་བ་ལ་སོགས་པ་ལྟ་བ་ལྔ་པོ་དག་དང་། འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་དང་། སློབ་པའི་ལྟ་བ་དང་། མི་སློབ་པའི་ལྟ་བ་དང་། ཆོས་ཀྱི་ཁམས་རྣམ་པ་བརྒྱད་པོ་འདི་དག་ནི་ལྟ་བ་ཡིན་ནོ། །

[Block 429]
ལྷག་མ་ནི་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 430]
དེ་ལ་འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཤེས་རབ་དགེ་བ་ཟག་པ་དང་བཅས་པའོ། །

[Block 431]
སློབ་པའི་ཟག་པ་མེད་པའི་ལྟ་བ་ནི་སློབ་པའིའོ། །

[Block 432]
མི་སློབ་པའི་ནི་མི་སློབ་པའིའོ། །

[Block 433]
ཡང་ཅིའི་ཕྱིར་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་མཚུངས་པར་ལྡན་པ་ཁོ་ན་ལ་འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་ཞེས་བྱ་ཞེ་ན། འདི་ལྟར།

[Block 434 [VERSE]]
རྣམ་ཤེས་ལྔ་དང་མཚུངས་སྐྱེས་བློ། །
ངེས་རྟོགས༌[^165]མེད་ཕྱིར་ལྟ་བ༌[^166]ཡིན། །

[Block 435]
རྟོག་པར་བྱེད་པ་ནི་ལྟ་བ་ཡིན་ཏེ། ངེས་པར་སེམས་པ་ལ་ཞུགས་པ་དག་ཡིན་ན། རྣམ་པར་ཤེས་པ་ལྔ་དང་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 436]
དེ་ཉིད་ཀྱི་ཕྱིར་ཤེས་རབ་ཉོན་མོངས་པ་ཅན་ནམ། ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ༌[^167]གཞན་ཡང་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 437]
འོ་ན་མིག་ཀྱང་རྟོག་པར་བྱེད་པ་ཉིད་མེད་ན་ཇི་ལྟར་ལྟ་བ་མ༌[^168]ཡིན་ཞེ་ན། གཟུགས་ལ་ལྟ་བའི་དོན་གྱིས་ཏེ། གང་གི་ཕྱིར། མིག་གིས༌[^169]གཟུགས་རྣམས་མཐོང་། གལ་ཏེ་མིག་གིས་གཟུགས་རྣམས་མཐོང་བར་གྱུར་ན། རྣམ་པར་ཤེས་པ་གཞན་དང་ལྡན་པས་ཀྱང་མཐོང་བར་འགྱུར་རོ་ཞེ་ན། མིག་ཐམས་ཅད་ཀྱིས་མཐོང་བ་ནི་མ་ཡིན་པ་ཉིད་དོ། །

[Block 438]
འོ་ན་ཅི་ཞེ་ན། རྟེན་བཅས་རྣམ་པར་ཤེས་པ་དང་བཅས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 439]
གང་གི་ཚེ་རྣམ་པར་ཤེས་པ་དང་བཅས་པར་གྱུར་པ་དེའི་ཚེ་མཐོང་ངོ་། །དེ་ལྟ༌[^170]ན་འོ་ན་ནི་མིག་ལ་བརྟེན་པའི་རྣམ་པར་ཤེས་པ་དེ་ཁོ་ནས་མཐོང་བར་འགྱུར་རོ་ཞེ་ན། དེ་ལ་བརྟེན་པའི་རྣམ་ཤེས་མིན། །མཐོང་ངོ་ཞེས་ངེས་པར་བྱ་བའི་ནུས་པ་ནི་མེད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 440 [VERSE]]
གང་ཕྱིར་བར་དུ་ཆོད་པ་ཡི། །
གཟུགས་ནི་མཐོང་བ་མིན་ཕྱིར་ལོ། །

[Block 441]
གང་གི་ཕྱིར་རྩིག་པ་ལ་སོགས་པས་བར་དུ་ཆོད་པའི་གཟུགས་མི་མཐོང་ངོ༌[^171]ཞེས་གྲག་གོ། །

[Block 442]
གལ་ཏེ་རྣམ་པར་ཤེས་པས་མཐོང་བར་གྱུར་ན་དེ་ནི་ཐོགས་པ༌[^172]མེད་པའི་ཕྱིར་རྩིག་པ་ལ་སོགས་པ་ལ་ཡང་ཐོགས་པ་མེད་པས་གཟུགས་བསྒྲིབས་པ་ཡང་མཐོང་བར་འགྱུར་རོ། །

[Block 443]
མཐོང་བ་ཡང་མ་ཡིན་ཏེ། དེ་བས་ན་རྣམ་པར་ཤེས་པས་མི་མཐོང་ངོ་། །ཇི་ལྟར་ཡང་མིག་གིས་མཐོང་བ་དེ་བཞིན་དུ་རྣ་བས་ཐོས་སོ། །

[Block 444]
སྣས་ཚོར་རོ། །

[Block 445]
ལྕེས་མྱོང་ངོ་། །ལུས་ཀྱིས་རེག་གོ། །

[Block 446]
ཡིད་ཀྱིས་རྣམ་པར་ཤེས་སོ། །

[Block 447]
ཅི་མིག་གཅིག་གིས་གཟུགས་རྣམས་མཐོང་ངམ། འོན་ཏེ་གཉིས་ཀས་ཤེ༌[^173]ན། འདི་ལ་ངེས་པ་མེད་དེ།

[Block 448 [VERSE]]
མིག་ནི་གཉིས་ཀ་དག་གིས་ཀྱང་། །
མཐོང་སྟེ་གསལ་བར་མཐོང་ཕྱིར་རོ། །

[Block 449]
མིག་ནི་གཉིས་ཀས་ཀྱང་མཐོང་སྟེ། གཉིས་ཀ་ཕྱེ་ན་གསལ་བ་རབ་ཏུ་མཐོང་བར་འགྱུར་རོ། །

[Block 450]
རྟེན་རྣམ་པར་ཆད་པས་རྣམ་པར་ཆད་པ་མཐོང་བ་ཡང་མེད་དེ། རྣམ་པར་ཤེས་པ་ནི༌[^174]ཡུལ་ན་མི་གནས་པའི་ཕྱིར་རོ། །

[Block 451]
ཅི་མིག་ལ་སོགས་པ་རྣམས་ཡུལ་དང་ཕྲད་པ་ཞིག་གམ། འོན་ཏེ་མ་ཕྲད་པ་ཞིག་ཡིན་ཞེ་ན། །མིག་དང་ཡིད་དང་རྣ་བ་ནི། །ཡུལ་དང་མ་ཕྲད། འདི་ལྟར་གཟུགས་རྒྱང་རིང་པོ་ནས༌[^175]མཐོང་ཞིང་མིག་དང་ཕྲད་པའི་མིག་སྨན་མི་མཐོང་ངོ་། །སྒྲ་རྒྱང་རིང་པོ་ནས་ཐོས་སོ། །

[Block 452]
ཡིད་ནི་གཟུགས་ཅན་མ་ཡིན་པའི་ཕྱིར་ཕྲད་པ་ཉིད་དུ་མི་ནུས་སོ། །

[Block 453]
ལྷག་མ་སྣ་དང་། ལྕེ་དང་། ལུས་ཞེས་བྱ་བ། གསུམ་གཞན་དུ། ཡུལ་དང་ཕྲད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 454]
ཡང་ཅི་མིག་ལ་སོགས་པ་དག་གིས་བདག་ཉིད་ཀྱི་ཚད་དང་མཉམ་པའི་དོན་ལ་འཛིན་ཏམ། འོན་ཏེ་མཉམ་པའམ་མི་མཉམ་པ་ཞིག་ལ་འཛིན་ཅེ་ན། རེ་ཞིག་གང་དག་ཡུལ་དང་ཕྲད་པར་བཤད་པ། སྣ་ལ་སོགས་པ་གསུམ་པོ་དེ་རྣམས་ཀྱིས་ནི། ཡུལ་ནི་མཉམ་པར༌[^176]འཛིན་པར་འདོད། །དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ཇི་སྙེད་པ་དེ་སྙེད་ཀྱི་ཡུལ་གྱི་རྡུལ་ཕྲ་རབ་རྣམས་དང་ཕྲད་ནས་རྣམ་པར་ཤེས་པ་བསྐྱེད་དོ། །

[Block 455]
མིག་དང་རྣ་བ་དག་གིས་ནི་མ་ངེས་སོ། །

[Block 456]
ཡིད་ནི་ལུས་ཅན་མ་ཡིན་པས་ཚད་ཡོངས་སུ་མ་ཆད་པས་མི་དཔྱོད་དོ། །

[Block 457]
ད་ནི་གང་འདི་དག་རྣམ་པར་ཤེས་པའི་ཁམས་དྲུག་བཤད་པ་ཇི་ལྟར་དེ་དག་གི་ཡུལ་ད་ལྟར་བ་དང་དུས་གསུམ་ཡིན་པ་ལྟར་རྟེན་ཀྱང་དེ་ལྟ་བུ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ཏེ། ཐ་མའི་རྟེན་འདས། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་རྟེན་ནི་འགགས༌[^177]མ་ཐག་པའི་ཡིད་དོ། །

[Block 458]
ལྔ་རྣམས་ནི། དེ་དག་ལྷན་ཅིག་སྐྱེས་པའང་ཡིན། །དེ་ལ་མིག་གི་རྣམ་པར་ཤེས་པའི་ལྷན་ཅིག་སྐྱེས་པའི་རྟེན་ནི་མིག་ནས་ལུས་ཀྱི་རྣམ་པར་ཤེས་པའི་བར་དུ་ཡང་ལུས་ཡིན་ལ།[^178] དེ་དག་གི༌[^179]འདས་པའི་རྟེན་ཡིད་ཡིན་ནོ། །

[Block 459]
ཡང་རྣམ་པར་ཤེས་པ་ནི་གཉིས་ཀ་ལ་རག་ལུས་ཏེ་སྐྱེ་ན༌[^180]ཅིའི་ཕྱིར་མིག་ལ་སོགས་པ་ཁོ་ན་ལ་བརྟེན་ཅེས་བྱ་བའི་གཟུགས་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ་ཞེ་ན།

[Block 460 [VERSE]]
དེ་དག་གྱུར་པས་འགྱུར་ཉིད་ཕྱིར། །
བརྟེན་ནི༌[^181]མིག་ལ་སོགས་པ་ཡིན། །
--- END BLOCKS ---
