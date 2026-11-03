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
[Block 281]
དཔེར་ན་ནམ་མཁའ་ནི་དུས་འདི་ལ་འོངས་སོ་བྱུང་ངོ་ཞེས་བྱ་བའམ། སོང་ངོ་འགགས་སོ་ཞེས་བྱ་བ་འམ། གནས་པའི་སྐད་ཅིག་གི་དབང་གིས༌[^209]གནས་སོ་ཞེས༌[^210]བྱ་བར་བརྗོད་དུ་མི་རུང་སྟེ། ཐེག་པ་ཆེན་པོ་ཡང་དེ་བཞིན་ནོ། །

[Block 282]
དཔེར་ན་ནམ་མཁའ་ནི་སྔོན་གྱི་དུས་དེ་ན་བྱུང་ངོ་། ། ཕྱི་མའི་དུས་དེ་ན་འབྱུང་བར་འགྱུར་རོ། །

[Block 283]
བར་གྱི་དུས་དེ་ན་ཡོད་དོ་ཞེས་བརྗོད་པར་མི་ནུས་ཏེ། ཐེག་པ་ཆེན་པོ་ཡང་དེ་བཞིན་ནོ་ཞེས་དེའི་རིམ་གྱིས་འགྲེས་གསུམ་གྱིས་བསྟན་ཏོ། །

[Block 284]
དེ་ནས་གནས་བརྟན་གྱིས་སྨྲས་པའི་འགྲེས༌[^211]ཉིད་ལ། བཅོམ་ལྡན་འདས་ཀྱིས་མངོན་པར་དགྱེས་པར་མཛད་ནས་སྔར་བཤད་པའི་རིམ་གྱིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པའི་ཆོས་རྣམས་རྣམ་པར་སྨིན་པའི་བདག་ཉིད་དུ་གྱུར་པ་ཆོས༌[^212]ཀྱི་སྐུས་བསྡུས་པ་དང་། ཐེག་པ་ཆེན་པོ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 285]
ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སོགས་པས་དེ་ལྟར་ཐེག་པ་ཆེན་པོ་བསྟན་ནས་དེའི་འོག་ཏུ་གནས་བརྟན་གྱིས༌[^213]ལྷ་དང་། མི་དང་། ལྷ་མ་ཡིན་དུ་བཅས་པའི་འཇིག་རྟེན་ཟིལ་གྱིས་མནན་ནས། ཐེག་པ་དེ་ངེས་པར་འབྱུང་བར་འགྱུར་ཏེ་ཞེས་བྱ་བ་དང་། ཐེག་པ་དེ་ནམ་མཁའ་དང་མཉམ་པ་སྟེ་ཞེས་བྱ་བ་དང་། བཅོམ་ལྡན་འདས་འདི་ལྟ་སྟེ་དཔེར་ན་ནམ་མཁའ་ནི་སེམས་ཅན་གྲངས་མ་མཆིས་ཚད་མ་མཆིས། དཔག་ཏུ་མ་མཆིས་པ་རྣམས་ཀྱི་གོ་འབྱེད་དོ་ཞེས་བྱ་བ་དང་། འོང་བའམ། འགྲོ་བ་མི་དམིགས་ཞེས་བྱ་བ་དང་། སྔོན་གྱི་མཐའ་འམ། [^214]ཕྱི་མའི་མཐའ་མི་དམིགས་ཞེས་བྱ་བ་ཚིག་ལྔ་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས། རབ་འབྱོར་གང་ཡང་ཁྱོད་ཀྱིས་འདི་སྐད་དུ་ཐེག་པ་དེ་ནི་ལྷ་དང་མི་དང་། ལྷ་མ་ཡིན་དུ་བཅས་པའི་འཇིག་རྟེན་ཟིལ་གྱིས་མནན་ནས་ངེས་པར་འབྱུང་བར་འགྱུར་ཞེས་སྨྲས་པ་ནི་ཞེས༌[^215]བྱ་བ་ལ་སོགས་པས་ཚིག་དེ་དག་སོ་སོར་སྨོས་ཏེ། དེ་དག་རྒྱ་ཆེར་བསྟན་ཏོ། །

[Block 286 [HEADING]]
##### འཇིག་རྟེན་ཟིལ་གྱིས་མནན་ནས་ངེས་པར་འབྱུང་བ། ^1-1-6-1-0

[Block 287]
རབ་འབྱོར་གལ་ཏེ་འདོད་པའི་ཁམས་དེ་བཞིན་དུ་གྱུར་ཏེ། མ་ནོར་བ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་ཇི་སྐད་བསྟན་པར་འགྱུར་ཞེ་ན། གལ་ཏེ་འདོད་པའི་ཁམས་ལ་སོགས་པ་ཆོས་ཐམས་ཅད་ཀུན་བརྟགས་པ་དང་ཡང་དག་པ་མ་ཡིན་པ་མ་ཡིན་ཏེ། ཡོངས་སུ་གྲུབ་པ་དེ་ཁོ་ན་ཉིད་ཀྱི་ངོ་བོ་ཞིག་ཡིན་དུ་ཟིན་ན་ཐེག་པ་ཆེན་པོ་འདི་དེ་དག་ལས་ངེས་པར་འབྱུང་བར་མི་འགྱུར་ཞིང་། དེ་དག་ཡོངས་སུ་སྤོང་བར་མི་འགྱུར་བ་ཞིག་ན་འདི་ལྟར་ཆོས་དེ་དག་ཐམས་ཅད༌[^216]ཀུན་བརྟགས་པ་སྟེ། ཡང་དག་པ་མ་ཡིན་པས། དེའི་ཕྱིར་ཐེག་པ་ཆེན་པོ་འདི་དེ་དག་ཡོངས་སུ་སྤོང་བར་འགྱུར་རོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 288]
རབ་འབྱོར་གལ་ཏེ་འདོད་པའི་ཁམས་དེ་བཞིན་དུ་གྱུར་ཏེ། མ་ནོར་བ་དང་། གཞན་མ་ཡིན་པ་དང་། ཕྱིན་ཅི་མ་ལོག་པ་དང་། དེ་ཁོ་ན་དང་། ཡང་དག་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གལ་ཏེ་འདོད་པའི་ཁམས་དངོས་པོ་ཡོད་པར་གྱུར་ཏེ་དངོས་པོ་མེད་པ་མ་ཡིན་ན་ཞེས་བྱ་བར་སྦྱར་ཏེ། གལ་ཏེ་འདོད་པའི་ཁམས་ཡོད་པར་གྱུར་ཏེ་མེད་པ་མ་ཡིན་ན་ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་དང་། བདེན་པའི་མཚན་ཉིད་དང་། འདུས་མ་བྱས་ཀྱི་མཚན་ཉིད་དང་། རྣམ་པ་གསུམ་གྱིས་ཡོད་པ་ཉིད་དུ་འགྱུར་ཏེ། དེ་ལ་དེ་བཞིན་དུ་གྱུར་པ༌[^217]དང་། མ་ནོར་བ་དང་། གཞན་མ་ཡིན་པ་ཞེས་བྱ་བ་ཚིག་གསུམ་གྱིས་ནི་ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 289]
ཕྱིན་ཅི་མ་ལོག་པ་དང་། དེ་ཁོ་ན་དང་། ཡང་དག་པ་དང་། བདེན་པ་དང་། ཇི་ལྟ་བ་བཞིན་དུ་ཞེས་བྱ་བ་ཚིག་ལྔས་ནི་བདེན་པ་བསྟན་ཏོ། །

[Block 290]
རྟག་པ་དང་། བརྟན་པ་དང་། ཐེར་ཟུག་དང་། མི་འགྱུར་བའི་ཆོས་ཅན་ཞེས་བྱ་བ་ཚིག་བཞིས་ནི་འདུས་མ་བྱས་ཀྱི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 291]
[^218]

[Block 292]
དེ་ལ་ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་ནི་རྣམ་པ་གསུམ་སྟེ། མི་འཇིགས་པར་ཡོངས་སུ་གྲུབ་པ་དང་། ཕྱིན་ཅི་མ་ལོག་པར༌[^219]ཡོངས་སུ་གྲུབ་པ་དང་། མི་འགྱུར་བར་ཡོངས་སུ་གྲུབ་པའོ། །

[Block 293]
དེ་ལ་དེ་བཞིན་དུ་གྱུར་ཞེས་བྱ་བས་ནི་མི་འཇིགས་པར་ཡོངས་སུ་གྲུབ་པ་བསྟན་ཏོ། །

[Block 294]
མ་ནོར༌[^220]ཞེས་བྱ་བས་ནི་ཕྱིན་ཅི་མ་ལོག་པར་ཡོངས་སུ་གྲུབ་པ་བསྟན་ཏོ། །

[Block 295]
གཞན་མ་ཡིན་ཞེས་བྱ་བས་ནི་མི་འགྱུར་བར་ཡོངས་སུ་གྲུབ་པ་བསྟན་ཏོ། །

[Block 296]
བདེན་པའི་མཚན་ཉིད་ཀྱང་རྣམ་པ་ལྔ་སྟེ། ཕྱིན་ཅི་མ་ལོག་པའི་མཚན་ཉིད་ནི་དཔེར་ན་སྨིག་རྒྱུ་ལ་ཆུར་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་མེད་པ་ལྟ་བུ་སྟེ། དེ་ནི་ཕྱིན་ཅི་མ་ལོག་པ་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 297]
ངོ་བོ་ཉིད་ཀྱི་མཚན་ཉིད་ནི་དཔེར་ན་སྒྱུ་མ་ལ་ངོ་བོ་ཉིད་མེད་པའི་དངོས་པོ་ལྟ་བུ་སྟེ། དེ་ནི་དེ་ཁོ་ན་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 298]
ཡོད་པའི་མཚན་ཉིད་ནི་དཔེར་ན་སྐྲ་ཤད་འཛིངས་པ་ལ་སོགས་པ་ལ་ཡོད་པ་མ་ཡིན་པའི་མཚན་ཉིད་དུ་གྱུར་པ་མེད་པ་ལྟ་བུ་སྟེ། དེ་ནི་ཡང་དག་པ་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 299]
མི་སླུ་བའི་མཚན་ཉིད་ནི་དཔེར་ན་ཟླ་བ་གཉིས་སུ་གྱུར་པ་ལ་སོགས་པར་འཁྲུལ་པའི་མཚན་ཉིད་མེད་པ་ལྟ་བུ་སྟེ། དེ་ནི་བདེན་པ་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 300]
རིགས་པའི་མཚན་ཉིད་ནི་དཔེར་ན་རྟག་པ༌[^221]དང་། བདེ་བ་དང་། བདག་ལ་སོགས་པ་འཐད༌[^222]པ་དང་བྲལ་བར་གྱུར་པ་མེད་པ་ལྟ་བུ་སྟེ། དེ་ནི་ཇི་ལྟ་བ་བཞིན་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 301]
འདུས་མ་བྱས་ཀྱི་མཚན་ཉིད་ནི་རྣམ་པ་བཞི་སྟེ། སྐྱེ་བ་དང་། འགག་པ་མེད་པའི་མཚན་ཉིད་ནི་འདི་ལྟ་སྟེ། རྟག་པ་ཞེས་གསུངས་པའོ། །

[Block 302]
རྟག་ཏུ་གནས་པའི་མཚན་ཉིད་ནི་འདི་ལྟ་སྟེ། བརྟན་པ་ཞེས་གསུངས་པའོ། །

[Block 303]
[^223]འཆད་པ་མེད་པའི༌[^224]མཚན་ཉིད་ནི་འདི་ལྟ་སྟེ། ཐེར་ཟུག་ཅེས་གསུངས་པའོ། །

[Block 304]
[^225]འགྱུར་བ་མེད་པའི༌[^226]མཚན་ཉིད་ནི་འདི་ལྟ་སྟེ། མི་འགྱུར་བའི་ཆོས་ཅན་ཞེས་གསུངས་པའོ། །

[Block 305]
རབ་འབྱོར་དེའི་ཕྱིར་འདོད་པའི་ཁམས་ནི་ཀུན་བརྟགས་པ། རྣམ་པར་བསྒྲུབ་པ༌[^227]ཚིག་གིས་བསྟན་པ་ཞེས་བྱ་བ་ལ། བརྟགས་པ་ཞེས་བྱ་བ༌[^228]ནི་བདེན་པ་མ་ཡིན་པའི་ཕྱིར་ཀུན་བརྟགས་པ་མ་ཡིན་པ་ཉིད་དུ༌[^229]བསྟན་ཏོ། །

[Block 306]
རྣམ་པར་བསྒྲུབས་པ༌[^230]ཞེས་བྱ་བ༌[^231]ནི་གཞན་གྱི་དབང་གིས་བཀོད་པའི་ཕྱིར་ཡང་དག་པ་མ་ཡིན་པ༌[^232]ཀུན་བརྟགས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 307]
ཚིག་གིས་བསྟན་པ་ཞེས་བྱ་བས་ནི་ཀུན་རྫོབ་ཡིན་པའི་ཕྱིར་བརྗོད་པར་བྱ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 308]
དངོས་པོ་མེད་པ་སྟེ། དངོས་པོ་ཡོད་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་མེད་པ་སྟེ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 309]
ལྷ་དང་། མི་དང་། ལྷ་མ་ཡིན་དུ་བཅས་པའི་འཇིག་རྟེན་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གསུམ་སྟེ། ལྷ་མ་ཡིན་སྨོས་པས་ནི་འོག་གི་འཇིག་རྟེན་བསྟན་ཏོ། །

[Block 310]
མི་སྨོས་པས་ནི་བར་གྱི་འཇིག་རྟེན་བསྟན་ཏོ། །

[Block 311]
ལྷ་སྨོས་པས་ནི་གོང་མའི་འཇིག་རྟེན་བསྟན་ཏོ། །

[Block 312]
འགྲེས་འདི་ལ་ཡང་ཁམས་གསུམ་པོ་དག་དང་། ཕུང་པོ་རྣམས་དང་། སྐྱེ་མཆེད་རྣམས་དང་། རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་དང་། འདུས་ཏེ་རེག་པའི་ཚོགས་དྲུག་དང་། ཚོར་བའི་ཚོགས་དྲུག་དང་། ཁམས་དྲུག་དང་། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཡན་ལག་བཅུ་གཉིས་པ་དང་། དེ་བཞིན་ཉིད་དང་། མ་ནོར་བ་དེ་བཞིན་ཉིད་དང་། གཞན་མ་ཡིན་པའི༌[^233]དེ་བཞིན་ཉིད་དང་། ཆོས་དང་། ཆོས་ཀྱི་དབྱིངས་དང་། ཆོས་གནས་པ་ཉིད་དང་། ཆོས་སྐྱོན་མེད་པ་ཉིད་དང་། ཡང་དག་པའི་མཐའ་དང་། བསམ་གྱིས་མི་ཁྱབ་པའི་དབྱིངས་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དང་། སྟོང་པ་ཉིད་ཐམས་ཅད་དང་། བྱང་ཆུབ་ཀྱི་ཕྱོགས་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པའི་མཐའ་ལ་ཐུག་པ་རྣམས་དང་། རིགས་ཀྱི་སའི་ཆོས་ལ་སོགས་པས༌[^234]སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་མཐའ་ལ་ཐུག་པ་རྣམས་དང་། རིགས་ཉིད་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་མཐའ་ལ་ཐུག་པ༌[^235]རྣམས་དང་། སེམས་བསྐྱེད་པ་ཐམས་ཅད་དང་། རྡོ་རྗེ་ལྟ་བུའི་ཡེ་ཤེས་དང་། སྐྱེས་བུ་ཆེན་པོའི་མཚན་རྣམས་དང་། འོད་དང་། ཡན་ལག་དྲུག་ཅུ་དང་ལྡན་པའི་དབྱངས་དང་། ཆོས་ཀྱི་འཁོར་ལོ་དང་། སེམས་ཅན་རྣམས་དང་། འདི་དག་བསྟན་ཏོ། །

[Block 313]
དེ་ལ་ཡན་ལག་དྲུག་ཅུ་དང་ལྡན་པའི་དབྱངས་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་གསང་བའི་མདོ་ལས།

[Block 314]
ཇི་སྐད་དུ་ཞི་བའི་བློ་གློས་གཞན་ཡང་དེ་བཞིན་གཤེགས་པའི་གསུང་ཡན་ལག་རྣམ་པ་དྲུག་ཅུ་དང་ལྡན་པ༌[^236]འབྱུང་སྟེ། མཉེན་པ་དང་། འཇམ་པ་དང་། ཡིད་དུ་འོང་བ་དང་། ཡིད་དུ་འཐད་པ་དང་། དག་པ་དང་། དྲི་མ་མེད་པ་དང་། གསལ་བ་དང་། སྙན་ཅིང་འཇེབས་པ་དང་། མཉན་པར་འོས་པ་དང་། མི་ཚུགས་པ་དང་། སྙན་པ་དང་། དུལ་བ་དང་། མི་རྩུབ་པ་དང་། མི་བརླང་བ་དང་། རབ་ཏུ་དུལ་བ་དང་། རྣར་སྙན་པ་དང་། ལུས་སིམ་པར་བྱེད་པ་དང་། སེམས་ཚིམ་པར་བྱེད་པ་དང་། སྙིང་དགའ་བར་བྱེད་པ་དང་། དགའ་བ་སྐྱེད༌[^237]པ་དང་། ཡོངས་སུ་གདུང་བ་མེད་པ་དང་། ཀུན་ཤེས་པར་བྱེད་པ༌[^238]དང་། རྣམ་པར་རིག་པར་བྱ་བ་དང་། རྣམ་པར་གསལ་བ་དང་། དགའ་བར་བྱེད་པ་དང་། མངོན་པར་དགའ་བར་བྱེད་པ་དང་། ཀུན་ཤེས་པར་བྱེད་པ་དང་། རྣམ་པར་རིག་པར་བྱེད་པ་དང་། རིགས་པ་དང་། འབྲེལ་པ་དང་། ཟློས་པའི་སྐྱོན་མེད་པ་དང་། སེང་གེའི་སྒྲའི་ཤུགས་དང་། གླང་པོ་ཆེའི་སྒྲ་སྐད་དང་། འབྲུག་གི་སྒྲ་དབྱངས་དང་། ཀླུའི་དབང་པོའི་སྒྲ་དང་། དྲི་ཟིའི་གླུ་དབྱངས་དང་། བྱ་ཀ་ལ་པིང་ཀའི་སྒྲ་དབྱངས་བསྒྲགས་པ༌[^239]དང་། ཚངས་པའི་སྒྲ་དབྱངས་བསྒྲགས་པ༌[^240]དང་། ཤང་ཤང་ཏེའུའི་སྒྲ་དབྱངས་སུ་གྲགས་པ༌[^241]དང་། ལྷའི་དབང་པོའི་སྒྲ་དབྱངས་ལྟར་སྙན་པ་དང་། རྔའི་སྒྲ་དང་། མ་ཁེངས་པ་དང་། མི་དམའ་བ་དང་། སྒྲ་དབྱངས༌[^242]ཐམས་ཅད་ཀྱི་རྗེས་སུ་ཞུགས་པ་དང་། ཚིག་ཟུར་ཆག༌[^243]མེད་པ་དང་། མ་ཚང་བ་མེད་པ་དང་། མ་ཞུམ་པ་དང་། མི་ཞན་པ་དང་། རབ་ཏུ་དགའ་བ་དང་། ཁྱབ་པ་དང་། ཆུབ་པ་དང་། རྒྱུན་ཆགས་པ་དང་། འབྲེལ་པ་དང་། སྒྲ་ཐམས་ཅད་རྫོགས་པར་བྱེད་པ་དང་། དབང་པོ་ཐམས་ཅད་ཚིམ་པར་བྱེད་པ་དང་། མ་སྨད་པ་དང་། མི་འགྱུར་བ་དང་། མ་བརྟབས་པ་དང་། འཁོར་ཀུན་ཏུ་གྲགས་པ་དང་། རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པ་ཞེས༌[^244]གསུངས་པ་ལྟ་བུའོ། །

[Block 315]
དེ་ལ་གཉེན་པོ༌[^245]ནི་ཁམས་དང་། དགེ་བའི་རྩ་བ་ཐམས་ཅད་ཉེ་བར་སྟོན་པའི་ཕྱིར་རོ། །

[Block 316]
འཇམ་པ་ནི་ཚེ་འདི་ཉིད་ལ་བདེ་བ་ལ་རེག་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 317]
ཡིད་དུ་འོང་བ་ནི་དོན་བཟང་པོའི་ཕྱིར་རོ། །

[Block 318]
ཡིད་དུ་འཐད་པ་ནི་ཚིག་འབྲུ་བཟང་པོའི་ཕྱིར་རོ། །

[Block 319]
དག་པ་ནི་འཇིག་རྟེན་ལས་འདས་པ་བླ་ན་མེད་པའི་རྗེས་ལ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 320]
དྲི་མ་མེད་པ་ནི་ཉོན་མོངས་པའི་བག་ལ་ཉལ་དང་། བག་ཆགས་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
