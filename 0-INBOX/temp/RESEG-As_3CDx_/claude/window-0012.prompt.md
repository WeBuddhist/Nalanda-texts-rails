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
[Block 421 [HEADING]]
###### **ཐབས།** ^3-2-2-3-3-2-0

[Block 422]
ཐབས་ནི། སྤྱོད་པ་ཐམས་ཅད༌[^308]དང་ལྡན་པའི་བློ་མངའ་བ་ཞེས་གསུངས་པས་བསྟན་ཏེ། དགའ་ལྡན་གྱི་གནས་སུ་སྐྱེ་བ་ལ་སོགས་པ་ཀུན་དུ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 423 [HEADING]]
###### **ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ།** ^3-2-2-3-3-3-0

[Block 424]
ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་ནི་ཆོས་ཤེས་པ་ལ་ནེམ་ནུར་མི་མངའ་བ་ཞེས་གསུངས་པས་བསྟན་ཏེ། འཇིག་རྟེན་གྱི་ཆོས་རྣམས་ཐོག་མ་ཉིད་དུ་སོ་སོར་རིག་པའི་ཕྱིར༌[^309]ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་ཉིད་ཡིན་ནོ། །

[Block 425 [HEADING]]
###### **ངོ་བོ་ཉིད།** ^3-2-2-3-3-4-0

[Block 426]
ངོ་བོ་ཉིད་ནི་རྣམ་པར་མ་བརྟགས་པའི་སྐུ་མངའ་བ༌[^310]ཞེས་གསུངས་པས་བསྟན་ཏེ། ཉོན་མོངས་པའི་རྣམ་པར་རྟོག་པ་ཐམས་ཅད་ལས་མ་བྱུང་བའི་ཕྱིར་ཏེ། དེ་ནི་དེའི་བདག་གི་སྦྱོར་བས་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 427 [HEADING]]
###### གཞན་གྱི་སྦྱོར་བ། ^3-2-2-3-4-0

[Block 428]
ཡན་ལག་བཞི་པ་ནི་གཞན་གྱི་སྦྱོར་བ་སྟེ།

[Block 429]
མདོ་ལས།

[Block 430]
བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཀྱི་ཡེ་ཤེས་ཡང་དག་པར་བླངས་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ་བྱང་ཆུབ་སེམས་དཔས་ཡེ་ཤེས་རྣམས་རང་གི་ཡེ་ཤེས་སུ་ཡང་དག་པར་བླངས་པའི་ཕྱིར་རོ། །

[Block 431]
ཡེ་ཤེས་ཡང་དག་པར་བླངས་པ་དེ་ནི་རྣམ་པ་གསུམ་སྟེ། ཁས་ལེན་པ་དང་། འགྲུབ་པ་དང་། རྟོགས་པ་བསྟན་པའོ། །

[Block 432 [HEADING]]
###### **ཁས་ལེན་པ།** ^3-2-2-3-4-1-0

[Block 433]
དེ་ལ་ཁས་ལེན་པ་ནི། སངས་རྒྱས་ཀྱི་གནས་པ་གཉིས་སུ་མེད་པ་དམ་པའི་ཕ་རོལ་ཏུ་བྱོན་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་སངས་རྒྱས་སུ་འགྱུར་བའི་ཆོས་ཀྱི་སྐུ་དང་གཅིག༌[^311]པ་ཉིད་དུ་ཁས་ལེན་པའི་ཕྱིར་རོ། །

[Block 434 [HEADING]]
###### **འགྲུབ་པ།** ^3-2-2-3-4-2-0

[Block 435]
འགྲུབ་པ་ནི་དེ་བཞིན་གཤེགས་པ་མ་འདྲེས་པའི་རྣམ་པར་ཐར་པ་མཛད་པའི་ཡེ་ཤེས་ཀྱི་མཐར་བྱོན་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་དང་སྤངས་པ་ཐ་དད་པ་མེད་པ་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 436 [HEADING]]
###### **རྟོགས་པ།** ^3-2-2-3-4-3-0

[Block 437]
རྟོགས་པ༌[^312]མཐའ་དང་དབུས་མེད་པའི་སངས་རྒྱས་ཀྱི༌[^313]མཉམ་པ་ཉིད་ཐུགས་སུ་ཆུད་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། དེ་གཉི་གའི་གནས་དེ་བཞིན་ཉིད་ཆོས་ཀྱི་དབྱིངས་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 438]
ཆོས་ཀྱི་དབྱིངས་རྟོགས་པ་དེ་ཡང་ཆོས་ཀྱི་དབྱིངས་ཀྱིས་ཀླས་པ་ཞེས་གསུངས་པས་ཉན་ཐོས་རྣམས་ལས༌[^314]ཁྱད༌[^315]དུ་འཕགས་པ་བསྟན་ཏེ། ཉན་ཐོས་ནི་ཡོངས་སུ་མྱ་ངན་ལས་འདའི། ཆོས་ཀྱི་དབྱིངས་ཀྱིས་ཀླས་པ་དེ་ནི་ནམ་མཁའི་ཁམས་ཀྱི་མཐས་གཏུགས་པ་ཡིན་ཏེ། དཔེར་ན་ནམ་མཁའ་ནི་འཇིག་པའི་དུས་སམ་ཆགས་པའི་དུས་ན༌[^316]ཡང་ཟད་པ་མེད་པ་དེ་བཞིན་དུ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱང་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པའི་དུས་སམ། ཡོངས་སུ་མྱ་ངན་ལས་འདས་པའི་དུས་ན་ཡང་། འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ལ་མི་གནས་པའི་ཕྱིར་ཉན་ཐོས་རྣམས་ལས་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་ཏེ་དེ་ནི་དེའི་གཞན་གྱི་སྦྱོར་བས་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 439 [HEADING]]
##### དངོས་པོ་བསྡུ་བའི་སྒོ་ནས་རྣམ་གྲངས་གཞན། ^3-2-2-4-0

[Block 440]
དངོས་པོ་བསྡུ་བའི་སྒོ་ནས་ཡང་རྣམ་གྲངས་གཞན་ཏེ། དེ་བཞིན་གཤེགས་པའི་ཕུན་སུམ་ཚོགས་པ་ནི་འདིར་རྣམ་པ་ཉི་ཤུ་རྩ་གཅིག་ཏུ་བསྟན་ཏེ། ཐུགས་ཕུན་སུམ་ཚོགས་པ་དང་། གསུང་ཕུན་སུམ་ཚོགས་པ་དང་། སྐུ་ཕུན་སུམ་ཚོགས་པ་མྱ་ངན་ལས་འདས་པ་མཚན་ཉིད་མེད་པ་དང་། བཞུགས་པ་ཕུན་སུམ་ཚོགས་པ་སྟོང་པ་ཉིད་དང་། སོ་སོར་རྟོག་པས༌[^317]བཞུགས་པ་དང་། ཡོན་ཏན་ཡོངས་སུ་འཛིན་པ་ཕུན་སུམ་ཚོགས་པ་དང་། དྲིས་པ་ལུང་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་དང་། རབ་ཏུ་རྒོལ་བ་ཟིལ་གྱིས་གནོན་པ་ཕུན་སུམ་ཚོགས་པ་དང་། ཞིང་ཡོངས་སུ་དག་པ་ཕུན་སུམ་ཚོགས་པ་དང་། གནས་ཕུན་སུམ་ཚོགས་པ་དང་། སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པ་དང་། སྤྲུལ་པ་ཕུན་སུམ་ཚོགས་པ་དང་། བསྟན་པ་ཕུན་སུམ་ཚོགས་པ་དང་། སེམས་ཅན་གྱི་སྤྱོད་པ་རྗེས་སུ་འཇུག་པ་ཕུན་སུམ་ཚོགས་པ་དང་། ཐམས་ཅད་དུ་འགྲོ་བའི་ལམ་གྱི༌[^318]གདམས་ངག་ཕུན་སུམ་ཚོགས་པ་དང་། ཕན་པ་གནོད་པ་ལ་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་དང་། གཞི་ཕུན་སུམ་ཚོགས་པ་དང་། མི་མཐུན་པ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་དང་། ཆོ་འཕྲུལ་གྱི་རྣམ་པར་རོལ་པ་ཕུན་སུམ༌[^319]ཚོགས་པ་དང་། ཡོན་ཏན་མི་ཟད་པ་ཕུན་སུམ་ཚོགས་པ་དང་། བདག་གི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་དང་། མྱ་ངན་ལས་འདས་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 441]
ཕུན་སུམ་ཚོགས་པ་རྣམ་པ༌[^320]ཉི་ཤུ་རྩ་གཅིག་པོ་དེ་དག་ཀྱང་མདོ་ལས།

[Block 442]
ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནས། ནམ་མཁའི་ཁམས་ཀྱི༌[^321]མཐས་གཏུགས་པ་ཞེས་བྱ་བ་གསུངས་པའི་བར་གྱི་ཚིག་ཉི་ཤུ་རྩ་གཅིག་དང་གོ་རིམ༌[^322]བཞིན་དུ་སྦྱར་ཏེ། ཚིག་གི་དོན་ལ་སོགས་པ་ནི་རྣམ་གྲངས་དག་གིས་ལུགས༌[^323]བཞིན་དུ་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 443]
ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 444 [HEADING]]
#### འཁོར་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-0

[Block 445]
ཇི་ལྟ་བུ་དག༌[^324]དང་བཞུགས་ཤེ་ན། འཁོར་ཕུན་སུམ་ཚོགས་པ་དག་སྟེ། དེ་ལ་འཁོར་ཕུན་སུམ་ཚོགས་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པ་དང་། བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 446 [HEADING]]
##### ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-1-0

[Block 447]
དེ་ལ་དང་པོར་ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཉན་ཐོས་ཀྱི་དགེ་འདུན་ཚད་མེད་པ་ཐམས་ཅད་ཀྱང་ཅང་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 448]
དེ་ལ་ཅིའི་ཕྱིར་ཉན་ཐོས་ཀྱི་འཁོར་ཐོག་མར་སྨོས་ཤེ་ན། དེ་ནི་ཐེག་པ་ཆེན་པོ་ལ་ཐེ་ཚོམ་ཟ་བ་རྣམས་ཀྱི་ཐེ་ཚོམ་བསལ་བ་དང་། བྱང་ཆུབ་སེམས་དཔའ༌[^325]མ་ངེས་པའི་རིགས་ཅན་རྣམས་ཀྱི་རྐྱེན་ཉེ་བར་བསྒྲུབ་པ་དང་། ཉན་ཐོས་རྣམ་པར་དག་པ་རྣམས་ཀྱི་ང་རྒྱལ་སྤང་བ་དང་། འཁོར་དང་རྒྱུ་བ་རྣམས་ཀྱི་འཁོར་དེ་དག་གདུལ་བ་དང་། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཉན་ཐོས་དག་ལ་གུས་པ་བསྐྱེད་པར་བྱ་བའི་ཕྱིར་ཏེ། བྱང་ཆུབ་སེམས་དཔས་ཀྱང་ཉན་ཐོས་རྣམས༌[^326]ལ་མི་གུས་པར་མི་བྱའོ་ཞེས་གསུངས་པས་ན་དེའི་ཕྱིར་གཞན་དག་དེ་ལ་གུས་པ་བསྐྱེད་པའི་ཕྱིར་དེ་དག་གི་ཡོན་ཏན་ཐོག༌[^327]མར་བརྗོད་པའོ། །

[Block 449]
འོ་ན་གནས་དེ་ནི་ཤིན་ཏུ་རྣམ་པར་དག་ཅིང་དབང་སྒྱུར་བའི་རྣམ་པར་རིག་པའི་མཚན་ཉིད་ཡིན་ནོ་ཞེས་གསུངས་ན། དེ་ནི་ཉན་ཐོས་རྣམས་ཇི་སྲིད་པར་གྱུར་ཏེ་འགལ་ལོ། །ཇི་ལྟར་འགལ་ཞེ་ན། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་དང་ལྟ་བ་མཐུན་པའི་རྐྱེན༌[^328]དུ་འགྱུར་རོ་ཞེ༌[^329]ན། གལ་ཏེ་ཉན་ཐོས་རྣམས་ཀྱིས་ཀྱང་བྱང་ཆུབ་སེམས་དཔའ་དག་བཞིན་དུ་གནས་ཏེ་མཐོང་ངོ་ཞེས་སྨྲ་ན་ནི་འགལ་བར་ཡང་འགྱུར་གྲང༌[^330]ན། དེ་དག་དེ་ན་གནས་སུ་ཟིན་ཀྱང་དེ་མཐོང་བར་འགྱུར་བའི་འདུ་བྱེད་དང་བྲལ་བའི་ཕྱིར་དམུས་ལོང་དང་འདྲ་བར་འབྱོར་པ་དེ་ལྟ་བུ་དེ་མི་མཐོང་བས་འགལ་བ་མེད་དོ། །

[Block 450]
དཔེར་ན་གསེར་ལ་སོགས་པ་ལ་སོལ་བ་ལ་སོགས་པར་མཐོང་བ་དང་འདྲ་སྟེ། རང་གི་འདུ་བྱེད་ཀྱི་དབང་གིས་གཞན་དུ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 451]
ཡང་ན་ཅུང་ཟད་ཅིག་མཐོང་ན་ཡང་སངས་རྒྱས་ཀྱི༌[^331]བྱིན་གྱི་རླབས༌[^332]ཀྱིས་མཐོང་བར་ཟད་ཀྱི་རང་གི་འདུ་བྱེད་ཀྱི་དབང་གིས་མཐོང་བ་མ་ཡིན་པས་འགལ་བ་མེད་དོ། །

[Block 452]
ཡང་ན་དེ་དག་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་ཤ་སྟག་སྟེ། ཉན་ཐོས་ཀྱི་ཆ་བྱད་དང་མིང་གིས་འདུལ་བའི་དབང་གི་ཕྱིར་དེ་ན་གནས་པ་ཡིན་པས་འགལ་བ་མེད་དོ། །

[Block 453]
དེ་ལ་ཉན་ཐོས་ཀྱི་དགེ་འདུན་ཞེས་བྱ་བ་ལ། ཉན་ཐོས་ཞེས་བྱ་བའི་ཚིག་གི་དོན་ནི་ཉན་ཅིང་སྒྲོགས་པས་ན་ཉན་ཐོས་ཞེས་བྱའོ། །

[Block 454]
དགེ་འདུན་ཞེས་བྱ་བའི་ཚིག་གི་དོན་ནི་མང་པོ་འདུས་པ་སྟེ། དེ་ཡང་ཚུལ་ཁྲིམས་མཐུན་པ་དང་། ལྟ་བ་མཐུན་པ་དང་། འཚོ་བ་མཐུན་པ་དང་། སྤྱོད་པ་མཐུན་པའི་ཕྱིར་བདུད་ལ་སོགས་པས་མི་ཕྱེད་པས་ན་དགེ་འདུན་ཞེས་བྱའོ། །

[Block 455]
ཚད་མེད་པ་ཞེས་བྱ་བ་ནི་གྲངས་ཚད་མེད་པ་དང་། ཡོན་ཏན་ཚད་མེད་པའོ།[^333] །དེ་ལ་གྲངས་ཚད་མེད་པ་ནི་བགྲང་བ་ལས་ཡང་དག་པར་འདས་པའི་ཕྱིར་རོ། །

[Block 456]
ཡོན་ཏན་ཚད་མེད་པ་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་ཐམས་ཅད་ཀྱང་ཅང་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་ལ་ཅང་ཤེས་པ་ཞེས་བྱ་བ་ནི་བསླབ་པ་རྣམས་དང་འགལ་བར་མི་བྱེད་པ་སྟེ། དམུ༌[^334]རྒོད་མ་ཡིན་པའི་ཕྱིར་རྟ་ཅང་ཤེས་ལྟ་བུའོ། །

[Block 457]
ཡང་རྣམ་པ་གཅིག་ཏུ༌[^335]ན་ཅང་ཤེས་པ་ཞེས་བྱ་བ་ནི་མི་འཇིགས་པ་སྟེ། འཇིགས་པ་མེད་པའི་ཕྱིར་མདོ་ལས་ཅང་ཤེས་པ་རྣམ་པ་ལྔར་གསུངས་ཏེ། ལྕེ་འབབ་པ་ལ་སོགས་པ་བག་ཚ་བ་འབྱུང་བར་དོགས་པ་མེད་པས་ཁྱུ་མཆོག་ཅང་ཤེས་དང་། འཐབ་མོའི་འཇིགས་པ་མེད་པས་གླང་པོ་ཆེ་དང་། རྟ་ཅང་ཤེས་དང་། གཞན་གྱིས༌[^336]གནོད་པར་བྱེད་པའི་འཇིགས་པ་མེད་པས་སེང་གེ་ཅང་ཤེས་དང་། འཆི་བའི་འཇིགས་པ་མེད་པས་དགྲ་བཅོམ་པ་ཅང་ཤེས་སོ། །

[Block 458]
མདོར་ན་བག་ཚ་བ་ནི་རྣམ་པ་བཞི་སྟེ། སྡུག་བསྔལ་གྱི་བག་ཚ་བ་དང་། འཇིགས་པའི་བག་ཚ་བ་དང་། འཇིག་རྟེན་གྱི་ཆོས་ཀྱི༌[^337]བག་ཚ་བ་དང་། མི་ཤེས་པས་བག་ཚ་བའོ། །

[Block 459]
དགྲ་བཅོམ་པ་ལ་ནི་བག་ཚ་བ་དེ་དག་མེད་པས་བདེ་བ་ཐོབ་པ་དང་། མི་སྐྲག་པ་ཐོབ་པ་དང་། མི་འཇིགས་པ་ཐོབ་པ་དང་། དབུགས༌[^338]དབྱུང་བ་ཐོབ་པ་ཞེས་བྱ་སྟེ་གོ་རིམ༌[^339]བཞིན་ནོ། །

[Block 460]
དེ་ལ་མྱ་ངན་དང་། སྨྲེ་སྔགས་འདོན་པ་དང་། སྡུག་བསྔལ་བ་དང་། ཡིད་མི་བདེ་བ་རྣམས་མྱ་ངན་མེད་པའི་ཕྱིར་སྡུག་བསྔལ་གྱི་བག་ཚ་བ་མེད་དོ། །
--- END BLOCKS ---
