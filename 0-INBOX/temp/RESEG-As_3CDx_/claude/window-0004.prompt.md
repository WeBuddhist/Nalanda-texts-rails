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
[Block 141 [HEADING]]
##### ཁ་དོག་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-1-0

[Block 142]
དེ་ལ་དང་པོ་ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། རིན་པོ་ཆེ་སྣ་བདུན་མཆོག་ཏུ་འབར་བ་བཀོད་པ་འཇིག་རྟེན་གྱི་ཁམས་དཔག་ཏུ་མེད་པ་རྒྱས་པར་འགེངས་པའི་འོད་ཟེར་ཆེན་པོ་རབ་ཏུ་འབྱུང་བ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 143]
དེ་ལ་རིན་པོ་ཆེ་སྣ་བདུན་ཞེས་བྱ་བ་ནི་གསེར་དང་། དངུལ་དང་། བཻ་ཌཱུཪྻ་དང་། སྤུག་དང་། རྡོའི་སྙིང་པོ༌[^109]དང་། མུ་ཏིག་དམར་པོ་དང་། ཀེ་ཀེ་རུའོ། །

[Block 144]
མཆོག་ཏུ་འབར་བ་ཞེས་བྱ་བ་ནི་རིན་པོ་ཆེ་སྣ་བདུན་པོ་དེ་དག་ཉིད་ཁ་དོག་མཆོག་ཏུ་འབར་བའོ། །

[Block 145]
ཡང་ན་གཞལ་མེད་ཁང་ཆེན་པོའི་ཁྱད་པར་དེ་ཉིད་རིན་པོ་ཆེ་སྣ་བདུན་པོ་དེ་དག་གི་ཁ་དོག་མཆོག་ཏུ་འབར་བ་ལ་ཡང་བྱའོ། །

[Block 146]
བཀོད་པ་ཞེས་བྱ་བ་ནི་རྒྱན་གྱི་ཁྱད་པར་གཞན་ཏེ། གཞལ་མེད་ཁང་ཆེན་པོ་དེ་ཉིད་རྒྱན་གྱི་ཁྱད་པར་གཞན་དང་ཡང་ལྡན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 147]
འཇིག་རྟེན་གྱི་ཁམས་དཔག་ཏུ་མེད་པ་རྒྱས་པར་འགེངས་པའི་འོད་ཟེར་ཞེས་བྱ་བ་ནི་དེ་ལྟར་མཆོག་ཏུ་འབར་བ་དེ་ལས་འོད་ཟེར་གང་དག་བྱུང་བས་ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་དཔག་ཏུ་མེད་པ་དག་སྣང་བས་ཁྱབ་པར་བྱེད་པའོ། །

[Block 148]
ཆེན་པོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་འཇིག་རྟེན་གྱི་ཁམས་དཔག་ཏུ་མེད་པ་རྒྱས་པར་འགེངས་པའི་འོད་ཟེར་དེ་དག་ཆེ་བ་ཡིན་ཏེ། དེ་ལྟར་ན་འོད་ཟེར་དེ་དག་ནི་འཇིག་རྟེན་གྱི་ཁམས་དཔག་ཏུ་མེད་པར་རྒྱས་པར་འགེངས་པ་ཡང་ཡིན་ལ། འོད་ཟེར་ཆེན་པོ་ཡང་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 149]
རབ་ཏུ་འབྱུང་བ་ཞེས་བྱ་བ་ནི་གཞལ་མེད་ཁང་ཆེན་པོ་དེ་ཉིད་ལས༌[^110]འོད་ཟེར་ཆེན་པོ་དེ་དག་རབ་ཏུ་འབྱུང༌[^111]ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། ཚིག་དེ་ཉིད་ཀྱིས་ནི་ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 150 [HEADING]]
##### དབྱིབས་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-2-0

[Block 151]
དེ་ལྟར་ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། དེའི་དབྱིབས་ཅི་འདྲ་ཞེ་ན། དེའི་ཕྱིར་དབྱིབས་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། གནས་ཐ་དད་པ་ཤིན་ཏུ་རྣམ་པར་ཕྱེ་བ་མཐའ་ཡས་པར་རྣམ་པར་གནས་པ་ཞེས་གསུངས་ཏེ། དེའི་དབྱིབས་ནི་གནས་ཐ་དད་པ་ཤིན་ཏུ་རྣམ་པར་ཕྱེ་བ། མཐའ་ཡས་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ།[^112] །དེ་ལ་གནས་ཐ་དད་པ་ཞེས་བྱ་བ་ནི་གཅིག་ཏུ་ཟད་པ་མ་ཡིན་གྱི་གནས་ཀྱི་བྱེ་བྲག་ཐ་དད་པ་རྣམ་པ་སྣ་ཚོགས་མང་དུ་ཡོད་པའི་དོན་ཏོ། །

[Block 152]
ཤིན་ཏུ་རྣམ་པར་ཕྱེ་བ་ཞེས་བྱ་བ་ནི་བློ་སྔོན་དུ་བཏང་ནས་ཆ་རྣམ་པར་བཞག་པས་བརྒྱན་པའོ། །

[Block 153]
ཇི་ལྟར་སེམས་ཡོངས་སུ་དག་པའི་རང་བཞིན་གྱི་སངས་རྒྱས་ཀྱི་ཞིང་བློ་སྔོན་དུ་བཏང་ནས་ཆ་རྣམ་པར་གཞག་པ་སྲིད་པར་འགྱུར་ཞེ་ན། དེ་ནི་ཕྱི་རོལ་གྱི་བསྒྲུབ་པས༌[^113]ཡོངས་སུ་གྲུབ་པ་མ་ཡིན་གྱི། བཅོམ་ལྡན་འདས༌[^114]སྔོན་བྱང་ཆུབ་སེམས་དཔར་གྱུར་པ་ན་མངོན་པར་འདུ་བྱེད་པ་དང་བཅས་པས་འཇུག་པའི་ཤེས་རབ་ཀྱི་རྣམ་པ་ལ་དཔྱོད་པའི་ཚེ་སྨོན་ལམ་གྱི་དབང་གིས༌[^115]དེ་དེ་ལྟར་མངོན་པར་འདུས་བྱས་པའི་དབང་གིས་ན་དེ་ལྟར་སྤྲོས་པ་མེད་པ་ལྷུན་གྱིས་གྲུབ་པའི་གནས་སྐབས་ན་ཡང་ཆ་རྣམ་པར་གཞག་པའི་རྣམ་པར་རིག་པ་འབྱུང་བའི་ཕྱིར་རྣམ་པར་རིག་པ་ནི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་ཡང་སྣང་སྟེ་འགལ་བ་མེད་དོ། །

[Block 154]
མཐའ་ཡས་པར་ཞེས་བྱ་བ་ནི་གྲངས་མཐའ་ཡས་པ་དང་། ཡུལ་མཐའ་ཡས་པའོ། །

[Block 155]
རྣམ་པར་གནས་པ་ཞེས་བྱ་བ་ནི་ཁྱད་པར་དུ་འཕགས་པར་གནས་པའམ། རྣམ་པ་སྣ་ཚོགས་སུ་གནས་པའམ། འབྱམ༌[^116]ཀླས་པར་གནས་པའི་དོན་ཏེ་དེ་ནི་དབྱིབས་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 156 [HEADING]]
##### ཚད་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-3-0

[Block 157]
དེ་ལྟར་དབྱིབས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། དེའི་ཚད་ཇི་ཙམ་ཞེ་ན། དེའི་ཕྱིར་ཚད་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། རྒྱ་ཡོངས་སུ་མ་ཆད་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེའི་ཚད་ནི་རྒྱ་འདི་ཙམ་ཞེས་ཚད་གཟུང༌[^117]དུ་མེད་པའི་ཕྱིར་རོ། །

[Block 158]
དེ་ལ་རྒྱ་ཞེས་བྱ་བ་ནི་ཐ་གྲུའི་ཁྱོན་ནོ། །

[Block 159]
ཡོངས་སུ་མ་ཆད་པ་ཞེས་བྱ་བ་ནི་དེའི་རྒྱ་འདི་ཙམ་ཞེས་ཚད་གཟུང༌[^118]དུ་མེད་པའོ། །

[Block 160]
ཡང་ན་རྒྱ་ཆེ་ཞེས་བྱ་བ་ནི་ཐ་གྲུའི་ཁྱོན་མ་ཡིན་གྱི། ཤར་ཕྱོགས་ལ་སོགས་པའི་ཕྱོགས་ཆ་སྟེ། ཕྱོགས་ཆ་ཐ་དད་པའི་ཆ་ཡོངས་སུ་བཅད་མི་ནུས་པའི་རྒྱ་ཡོངས་སུ་མ་ཆད་པ་ཞེས་བྱ་སྟེ། དེ་ནི་ཚད་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 161 [HEADING]]
##### ཡུལ་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-4-0

[Block 162]
དེ་ལྟར་ཚད་ཕུན་སུམ༌[^119]ཚོགས་པ་བསྟན་ནས་ཡོངས་སུ་མ་ཆད་པ་དེ་ཁམས་གསུམ་པར་གཏོགས་པ་ཞིག་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཕྱིར་ཡུལ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཁམས་གསུམ་པ་ལས་ཡང་དག་པར་འདས་པའི་སྤྱོད་ཡུལ་ཞེས་བྱ་བ་གསུངས་ཏེ། གནས་ཕུན་སུམ་ཚོགས་པ་དེ་ཉིད་ཁམས་གསུམ་པ་ལས་ཡང་དག་པར་འདས་པའི་སྤྱོད་ཡུལ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 163]
དེ་ལ་སྤྱོད་ཡུལ་ཞེས་བྱ་བ་ནི་གནས་སམ་ཡུལ་ལ་བྱ་སྟེ། དངོས་སུ་ན་གཞལ་མེད་ཁང་ཆེན་པོ་དེ་ཉིད་ཡིན་པར་བལྟའོ། །

[Block 164]
དེ་བས་ན་སྤྱོད་ཡུལ་དེ་ཉིད་ཁམས་གསུམ་པ་ལས་ཡང་དག་པར་འདས་པ་ཡིན་ཏེ། དེ་ནི་སྤྱོད་ཡུལ་ཡང་ཡིན་ལ་ཁམས་གསུམ་པ་ལས་ཡང་དག་པར་འདས་པ་ཡང་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །དེ་ཅིའི༌[^120]ཕྱིར་ཞེ་ན། ཁམས་གསུམ་པ་ནི་རང་གི་ས་པའི་སྲེད་པ་དག་གིས་བདག་གིར༌[^121]བྱས་པ་ཡིན་པས་དམིགས་པ་དང་མཚུངས་པར་ལྡན་པའི་སྒོ་ནས་བརྟས་པར༌[^122]འགྱུར་བ་དང་དེའི་རྣམ་པར་སྨིན་པ་ཡིན་གྱི། སྤྱོད་ཡུལ་དེ་ནི་ཁམས་གསུམ་པའི་སྲེད་པ༌[^123]དག་གིས་བདག་གིར་བྱས་པ་མ་ཡིན་པས་དམིགས་པ་དང་མཚུངས་པར་ལྡན་པའི་སྒོ་ནས་བརྟས་པར༌[^124]འགྱུར་བ་ཡང་མ་ཡིན་ལ། རྣམ་པར་སྨིན་པའི་ས་ལས་ཡང་དག་པར་འདས་པའི་ཕྱིར་དེ་ནི་རྣམ་པར་སྨིན་པ་ཡང་མ་ཡིན་ཏེ། མྱ་ངན་ལས་འདས་པ་དང་འདྲ་བས་ན་དེའི་ཕྱིར་ཁམས་གསུམ་པ་ལས་ཡང་དག་པར་འདས་པ་ཞེས་བྱ་སྟེ་དེ་ནི་ཡུལ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 165 [HEADING]]
##### རྒྱུ་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-5-0

[Block 166]
དེ་ལྟར་ཡུལ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། གལ་ཏེ༌[^125]ཁམས་གསུམ་པའི་སྲེད་པ་དག་གིས་བདག་གིར་མ་བྱས་པ་དང་རྣམ་པར་སྨིན་པའི་ས་ལས་འདས་པའི་ཕྱིར་དེའི་རྣམ་པར་སྨིན་པ་ཡང་མ་ཡིན་ཏེ། མྱ་ངན་ལས་འདས་པ་དང་འདྲ་བ་ཡིན་ན། དེ་ལྟ་ན་དེ༌[^126]མྱ་ངན་ལས་འདས་པ་དང་འདྲ་བར་རྒྱུ་མེད་པའི་སྐྱོན་དུ་འགྱུར་རོ། །

[Block 167]
ཅི་སྟེ་རྒྱུ་ཅན་ཞིག་ཡིན་ན་ནི་ཁམས་གསུམ་པའི་སྤྱོད་ཡུལ་དུ་འགྱུར་བས་དེའི་རྒྱུ་ཁམས་གསུམ་པ་ལས་གཞན་པ་འགའ་ཞིག་བརྗོད་དགོས་སོ་ཞེ་ན། དེའི་ཕྱིར་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། འཇིག་རྟེན་ལས་འདས་པ་དེའི་བླ་མའི་དགེ་བའི་རྩ་བ་ལས་བྱུང་བ་ཞེས་གསུངས་སོ། །

[Block 168]
དེ་ལ་འཇིག་རྟེན་ལས་འདས་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་སོ། །

[Block 169]
དེའི་བླ་མའི་དགེ་བའི་རྩ་བ༌[^127]ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་དེའི་རྗེས་ལས་ཐོབ་པ་དག་པ་འཇིག་རྟེན་པའི་ཡེ་ཤེས་དེ༌[^128]ཉིད་དགེ་བའི་རྩ་བ་ཡིན་ནོ། །

[Block 170]
ལས་བྱུང་བ་ཞེས་བྱ་བ་ནི་དག་པ་འཇིག་རྟེན་པའི་ཡེ་ཤེས་ཀྱི༌[^129]དགེ་བའི་རྩ་བ་དེ་ལ་གནས་ཕུན་སུམ་ཚོགས་པར་སྣང་བའི་རྣམ་པར་རིག་པ་དེ་བྱུང་བ་སྟེ། དག་པ་འཇིག་རྟེན་པའི་ཡེ་ཤེས་དེ་ཉིད་གནས་ཕུན་སུམ་ཚོགས་པའི་རྣམ་པར་རིག་པར་སྣང་བའི་དོན་ཏོ། །

[Block 171]
དེ་བས་ན་དེ་ནི་རྒྱུ་མེད་པ་ཡང་མ་ཡིན་ལ་དབང་པོ་ལ་སོགས་པ་རྒྱུ་མི་མཐུན་པ་ལས་བྱུང་བ་ཡང་མ༌[^130]ཡིན་ནོ། །

[Block 172]
གལ་ཏེ་དེ་ལྟ་ན་ཡང་རྣམ་པར་མི་རྟོག་པའི་རྗེས་ལས་ཐོབ་པ་དག་པ་འཇིག་རྟེན་པའི་ཆོས་དེ་ཁམས་གསུམ་པ་ལས་ཡང་དག་པར་འདས་པའི་རྣམ་པར་སྨིན་པའི་རྒྱུར་ཇི་ལྟར་འགྱུར་ཞེ་ན། དེ་ནི་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཞེས་མི་བྱའི་དེ་ལས་གཞན་གང་འབྱུང་བ་ལ་ལྟོས༌[^131]ནས་རྒྱུ་ཞེས་བརྗོད་པ་ཙམ་དུ་ཟད་དེ། དཔེར་ན་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་ནས་ལམ་ལ་རྗེས་སུ་ཤེས་པའི་བར་གྱི་ཚོགས་བཅུ་དྲུག་པོ་དག་ལས་འཇིག་རྟེན་པའི་ཆོས་ཀྱི་མཆོག་འབྱུང་བ་དང་འདྲའོ། །

[Block 173]
ཡང་རྣམ་གྲངས་གཞན་དུ་ན་ཚིག་གི་དོན་དེ་འདི་ལྟར་ཡང་བཤད་དེ། འཇིག་རྟེན་ལས་འདས་པ་ཞེས་བྱ་བ་ནི་འཕགས་པ་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ལམ་མོ། །

[Block 174]
དེའི་བླ་མའི་དགེ་བའི་རྩ་བ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་དགེ་བའི་རྩ་བ་ཟག་པ་མེད་པ་ཉིད་དོ། །

[Block 175]
ལས་བྱུང་བ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་དགེ་བའི་རྩ་བ་དེའི་དབང་གིས༌[^132]རྣམ་པར་རིག་པ་དེ་ལྟ་བུ་སྣང་བ་ལ༌[^133]བྱ་སྟེ། དེ་ནི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 176 [HEADING]]
##### རང་བཞིན་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-6-0

[Block 177]
དེ་ལྟར་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས་དེའི་རང་བཞིན་ཅི་འདྲ་ཞེ་ན། དེའི་ཕྱིར་རང་བཞིན་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་མཛད་ནས་ཤིན་ཏུ་རྣམ་པར་དག་ཅིང་དབང་སྒྱུར་བའི་རྣམ་པར་རིག་པའི་མཚན་ཉིད་ཅེས་བྱ་བ་གསུངས་ཏེ། དེའི་རང་བཞིན་ནི་ཤིན་ཏུ་རྣམ་པར་དག་ཅིང་དབང་སྒྱུར་བའི་རྣམ་པར་རིག་པའི་མཚན་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 178]
དེ་ལ་ཤིན་ཏུ་རྣམ་པར་དག་ཅིང་ཞེས་བྱ་བ་ནི་གནས་ཕུན་སུམ་ཚོགས་པར་སྣང་བའི་རྣམ་པར་རིག་པ་དེ་ཉིད་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱི་བར་དུ་ཤིན་ཏུ་སྦྱང་བ༌[^134]བྱས་ཏེ། ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་དུ་རྟོག་པ་བསལ་ཞིང་གཟུང༌[^135]བ་དང་འཛིན་པ་རྣམ་པར་སྤངས་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་ཤིན་ཏུ་རྣམ་པར་དག་པ་ཡིན་ནོ། །

[Block 179]
དབང་སྒྱུར་བ་ཞེས་བྱ་བ་ནི་ཟད་པར་གྱི་སྐྱེ་མཆེད་ལ་སོགས་པ་གྲུབ་པའི་རྣལ་འབྱོར་པ་དངོས་པོ་རྣམས་ལ་འདོད་དགུར་དབང་སྒྱུར་བ་དང་འདྲ་བར་ཤིན་ཏུ་རྣམ་པར་དག་པའི་རྣམ་པར་རིག་པ་དེས་རྣམ་པར་རིག་པ་ཙམ་གྱི་སྤྱོད་ཡུལ་རྣམ་པར་རིག་པའི་ངོ་བོ་ཉིད་དེ་ལ་དགྱེས་དགུར་དབང་སྒྱུར་ཞིང་མངའ་མཛད་པའི་དོན་ཏོ། །

[Block 180]
རྣམ་པར་རིག་པའི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་གནས་ཀྱི་རྣམ་པ་ལྟ་བུར་སྣང་བ་དེ་ཉིད་ཀྱི་སེམས་ཀྱི་རྣམ་པར་རིག་པ་ཙམ་གྱི་མཚན་ཉིད་ཡིན་ཏེ། རྣམ་པར་རིག་པ་ལས༌[^136]གཞན་པའི་ཕྱི་རོལ་ན་རིན་པོ་ཆེ་ལ་སོགས་པའི་དངོས་པོ་གཞན་མེད་པའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
