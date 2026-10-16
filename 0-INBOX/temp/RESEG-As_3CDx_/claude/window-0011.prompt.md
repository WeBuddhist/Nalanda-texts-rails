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
[Block 386 [HEADING]]
###### སངས་རྒྱས་ཀྱི་སྐུ་གསུམ་གྱི་ཡུལ་ཡོངས་སུ་མ་ཆད་པའི་ཡོན་ཏན། ^3-2-2-2-18-0

[Block 387]
དེའི་འོག་ཏུ་སངས་རྒྱས་ཀྱི་སྐུ་གསུམ་གྱི་ཡུལ་ཡོངས་སུ་མ་ཆད་པའི་ཡོན་ཏན་གྱིས་ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པར་བསྟན་པའི་དབང་དུ་མཛད་ནས། མཐའ་དང་དབུས་མེད་པའི་སངས་རྒྱས་ཀྱི་ས་མཉམ་པ་ཉིད་དུ༌[^290]ཐུགས་སུ་ཆུད་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། མཐའ་དང་དབུས་མེད་པ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཉིད་ཀྱི༌[^291]ཁྱད་པར་ཏེ། སྐུ་གསུམ་གྱི་བདག་ཉིད་ཀྱི༌[^292]སངས་རྒྱས་ཐོག་མ་དང་། ཐ་མ་དང་། བར་དང་། ཉལ་བ་རྣམས་སོ། །

[Block 388]
དེ་དག་གིས་ནི་སངས་རྒྱས་ཀྱི་ཞིང་སྟེ་སངས་རྒྱས་ཀྱི་ཞིང་ཐམས་ཅད་དུ་སྐུ་གསུམ་གྱི་ཡུལ་དུ་ཐ་དད་པ་མེད་པའི་དངོས་པོས་མཉམ་པ་ཉིད་དུ་བཞུགས་པའི་ཕྱིར་སངས་རྒྱས་ཀྱི་སྐུ་གསུམ་གྱི་ཡུལ་ཡོངས་སུ་མ་ཆད་པའི་ཡོན་ཏན་དང་ལྡན་པ་ཡིན་ཏེ། དེས་ཀྱང་ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 389 [HEADING]]
###### འཁོར་བའི་མཐའི་བར་དུ་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པ་དང་བདེ་བ་མཛད་པར་ཉེ་བར་གནས་པའི་ཡོན་ཏན། ^3-2-2-2-19-0

[Block 390]
དེའི་འོག་ཏུ༌[^293]འཁོར་བའི་མཐའི་བར་དུ་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པ་དང་བདེ་བ་མཛད་པར་ཉེ་བར་གནས་པའི་ཡོན་ཏན་གྱིས་ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པར་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཆོས་ཀྱི་དབྱིངས་ཀྱིས་ཀླས་པ༌[^294]ཞེས་བྱ་བ་གསུངས་ཏེ། ཆོས་ཀྱི་དབྱིངས་ཤིན་ཏུ་རྣམ་པར་དག་པ་འཁོར་བ་ཇི་སྲིད་པར་གནས་པ་དང་། དེའི་རྒྱུ་མཐུན་པ་མདོའི་སྡེ་ལ་སོགས་པའི་ཆོས་རྣམས་འདུལ་བའི་དུས་ཇི་ལྟ་བ་བཞིན་དུ་བཅོམ་ལྡན་འདས་བཞུགས་པའི་ཚེ༌[^295]དང་། ཡོངས་སུ་མྱ་ངན་ལས་འདས་པའི་དུས་ན་ཡང་གནས་པའི་ཕྱིར་འཁོར་བའི་བར་དུ་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པ་དང་བདེ་བ་མཛད་པའི་ཉེ་བར་གནས་པའི་ཡོན་ཏན་དང་ལྡན་པ་ཡིན་ཏེ། དེས་ཀྱང་ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 391 [HEADING]]
###### མི་ཟད་པའི་ཡོན་ཏན། ^3-2-2-2-20-0

[Block 392]
དེའི་འོག་ཏུ་མི་ཟད་པའི་ཡོན་ཏན་གྱིས༌[^296]ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པར་བསྟན་པའི་དབང་དུ་མཛད་ནས། ནམ་མཁའི་ཁམས་ཀྱི་མཐས་གཏུགས་པ་དེ་ཞེས་བྱ་བ་གསུངས་ཏེ། ནམ་མཁའ་དང་འདྲ་བའི་ཆོས་ཀྱི་དབྱིངས་ལ་རྣམ་པར་བཀོད་པའི་ཡོན་ཏན་རྣམས་ཀྱི་མཐའ་མེད་པས་ན་འཁོར་བ་ཇི་སྲིད་པའི་བར་དུ་ཆོས་ཀྱི་དབྱིངས་ཀྱིས་འགྲོ་བ་མཐའ་དག་གི་དོན་མཛད་པའི་རྒྱུན་མི་འཆད་པར་སྦྱོར་བས་ཡོན་ཏན་མི་ཟད་པའི་ཕྱིར་མི་ཟད་པའི་ཡོན་ཏན་དང་ལྡན་པ་ཡིན་ཏེ། དེས་ཀྱང་ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 393 [HEADING]]
##### ཡན་ལག་བཞིས་ཕུན་སུམ་ཚོགས་པ་གཉིས། ^3-2-2-3-0

[Block 394]
ཡང་རྣམ་གྲངས་གཞན་དུ་ན་བཅོམ་ལྡན་འདས་ཀྱི་ཡོན་ཏན་གྱི་ཁྱད་པར་རྣམ་པ་ཉི་ཤུ་རྩ་གཅིག་པོ་དེ་དག་གིས་ནི་བཅོམ་ལྡན་འདས་ཀྱི་ཡེ་ཤེས་དང་སྤངས་པ་བླ་ན་མེད་པ་གཉིས་ཀྱིས༌[^297]རང་གི་དོན་ཕུན་སུམ་ཚོགས་པ་དང་། བདག་དང་གཞན་གྱི་སྦྱོར་བ་གཉིས་ཀྱིས་གཞན་གྱི༌[^298]དོན་ཕུན་སུམ་ཚོགས་པ་སྟེ། ཡན་ལག་བཞིས་ཕུན་སུམ་ཚོགས་པ་གཉིས་བསྟན་ཏོ། །

[Block 395 [HEADING]]
###### ཡེ་ཤེས་བླ་ན་མེད་པ། ^3-2-2-3-1-0

[Block 396]
དེ་ལ་ཡན་ལག་དང་པོ་ནི་ཡེ་ཤེས་བླ་ན་མེད་པ་སྟེ་མདོ་ལས།

[Block 397]
ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། བློས་ཐུགས་སུ་ཆུད་པར་བྱ་བ་ཇི་སྙེད་པ་ཡོད་པ་དེ་སྙེད་དུ་ཐུགས་སུ་ཆུད་པའི་ཕྱིར་རོ། །

[Block 398]
དེ་ཡང་རྣམ་པ་བཞི་སྟེ། ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་ཉིད་དང་། དོན་ཟབ་མོ་ཐུགས་སུ་ཆུད་པའི་བློ་ཉིད་དང་། ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་ཉིད་དྲི་མ་མེད་པ་དང་། ལེགས་པར་ཐུགས༌[^299]སུ་ཆུད་པའི་བློ་ཉིད་བླ་ན་མེད་པའོ། །

[Block 399 [HEADING]]
###### **ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་ཉིད།** ^3-2-2-3-1-1-0

[Block 400]
དེ་ལ་ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་ཉིད་ནི། ཀུན་དུ་སྤྱོད་པ་གཉིས་མི་མངའ་བ་ཞེས་གསུངས་པས་བསྟན་ཏེ། ནང་དང་ཕྱིའི་སྐྱེ་མཆེད་ཀྱི་མཚན་མ་ཀུན་དུ་མི་སྤྱོད་པའི་ཕྱིར་རོ། །

[Block 401 [HEADING]]
###### **དོན་ཟབ་མོ་ཐུགས་སུ་ཆུད་པའི་བློ་ཉིད།** ^3-2-2-3-1-2-0

[Block 402]
དོན་ཟབ་མོ་ཐུགས་སུ་ཆུད་པའི་བློ་ཉིད་ནི། མཚན་ཉིད་མེད་པའི་ཆོས་ལ་མཆོག་ཏུ་གཞོལ་བར་མཛད་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། ཆོས་བདག་མེད་པ་ལ་མཆོག་ཏུ་གཞོལ་བའི་ཕྱིར་རོ། །

[Block 403 [HEADING]]
###### **ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་ཉིད་དྲི་མ་མེད་པ།** ^3-2-2-3-1-3-0

[Block 404]
ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་ཉིད་དྲི་མ་མེད་པ་ནི། སངས་རྒྱས་ཀྱི་གནས་པས་གནས་པ་ཞེས་བྱ་བས༌[^300]བསྟན་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་གནས་པ་ལས་ཡང་དག་པར་འདས་པའི་ཕྱིར་རོ། །

[Block 405 [HEADING]]
###### **ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་ཉིད་བླ་ན་མེད་པ།** ^3-2-2-3-1-4-0

[Block 406]
ལེགས་པར་ཐུགས་སུ༌[^301]ཆུད་པའི་བློ་ཉིད་བླ་ན་མེད་པ་ནི། སངས་རྒྱས་ཐམས་ཅད་དང་མཉམ་པ་ཉིད་བརྙེས་པ༌[^302]ཞེས་བྱ་བས་བསྟན་ཏེ། སངས་རྒྱས་ཐམས་ཅད་དང་ཁྱད་པར་མེད་པའི་ཕྱིར་ཏེ། དེ་ནི་ཡེ་ཤེས་བླ་ན་མེད་པས་རང་གི་དོན་ཕུན་སུམ་ཚོགས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 407 [HEADING]]
###### སྤངས་པ་བླ་ན་མེད་པ། ^3-2-2-3-2-0

[Block 408]
ཡན་ལག་གཉིས་པ་སྤངས་པ་བླ་ན་མེད་པ་སྟེ། མདོ་ལས་སྒྲིབ་པ་མེད་པའི་རྟོགས་པ་ཐུགས་སུ་ཆུད་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། རྟོགས་པར་བྱ་བ་ཇི་སྙེད་ཡོད་པ་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 409]
དེ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཉོན་མོངས་པའི་སྒྲིབ་པ་མི་མངའ་བས༌[^303]རྟོགས་པ་དང་། དེ་དག་ལ་རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་མི་མངའ་བས་རྟོགས་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པ་མི་མངའ་བས་རྟོགས་པའོ། །

[Block 410 [HEADING]]
###### **ཉོན་མོངས་པའི་སྒྲིབ་པ་མི་མངའ་བས་རྟོགས་པ།** ^3-2-2-3-2-1-0

[Block 411]
དེ་ལ་ཉོན་མོངས་པའི་སྒྲིབ་པ་མི་མངའ་བས་རྟོགས་པ་ནི། ཕྱིར་མི་ལྡོག་པའི་ཆོས་དང་ལྡན་པ་སྤྱོད་ཡུལ་གྱིས་མི་འཕྲོགས་པ་ཞེས་གསུངས་པའི་ཚིག་གཉིས་ཀྱིས་བསྟན་ཏེ། མ་འོངས་པའི་དུས་སུ་ཡང་སྤངས་པ་དེ་ཡོངས་སུ་ཉམས་པ་དང་། ད་ལྟར་ཉོན་མོངས་པ་མི་འབྱུང་བའི་ཕྱིར་ཏེ་གོ་རིམ༌[^304]བཞིན་ནོ། །

[Block 412 [HEADING]]
###### **རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་མི་མངའ་བས་རྟོགས་པ།** ^3-2-2-3-2-2-0

[Block 413]
དེ་དག་ལ་རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་མི་མངའ་བས་རྟོགས་པ་ནི། བསམ་གྱིས་མི་ཁྱབ་པ༌[^305]རྣམ་པར་འཇོག་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། སྐུ་བསམ་གྱིས་མི་ཁྱབ་པ་རྣམ་པར་འཇོག་པའི་ཕྱིར་རོ། །

[Block 414 [HEADING]]
###### **ཤེས་བྱའི་སྒྲིབ་པ་མི་མངའ་བས་རྟོགས་པ།** ^3-2-2-3-2-3-0

[Block 415]
ཤེས་བྱའི་སྒྲིབ་པ་མི་མངའ་བས་རྟོགས་པའི༌[^306]དུས་གསུམ་ལ་མཉམ་པ་ཉིད་ཚར་ཕྱིན་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། དུས་གསུམ་ལ་ཆགས་པ་མེད་ཅིང་ཐོགས་པ་མེད་པར་ཡེ་ཤེས་མཉམ་པ་ཉིད་ཚར་ཕྱིན་པའི་ཕྱིར་ཏེ། དེ་ནི་སྤངས་པ་བླ་ན་མེད་པས་རང་གི་དོན་ཕུན་སུམ་ཚོགས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 416 [HEADING]]
###### བདག་གིས་སྦྱོར་བ། ^3-2-2-3-3-0

[Block 417]
ཡན་ལག་གསུམ་པ་ནི་བདག་གིས་སྦྱོར་བ༌[^307]སྟེ་མདོ་ལས་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་དུ་ཞུགས་པའི་སྐུ་དང་ལྡན་པ་ཞེས་གསུངས་པས་བསྟན་ཏེ། སེམས་ཅན་དཔག་ཏུ་མེད་པའི་དོན་མཛད་པའི་ཕྱིར་རོ། །

[Block 418]
ཞུགས་པའི་སྐུ་དེ་ནི་རྣམ་པ་བཞི་སྟེ། དགོས་པ་དང་། ཐབས་དང་། ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་དང་། ངོ་བོ་ཉིད་ཀྱིས་བསྟན་ཏོ། །

[Block 419 [HEADING]]
###### **དགོས་པ།** ^3-2-2-3-3-1-0

[Block 420]
དེ་ལ་དགོས་པ་ནི་ཆོས་ཐམས་ཅད་ལ་ཐེ་ཚོམ་མེད་པའི་མཁྱེན་པ་མངའ་བས་ཞེས་གསུངས་པས་བསྟན་ཏེ། ཐེ་ཚོམ་ཐམས་ཅད་བཅད་པའོ། །

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
--- END BLOCKS ---
