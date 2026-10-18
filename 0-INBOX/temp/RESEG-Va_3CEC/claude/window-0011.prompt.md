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
[Block 386]
ཐོས་པ་ཉུང་བ་ལ་ཆོས་ཀྱི་ནན་ཏན་བྱེད༌[^363]ཅེས་བྱ་བས་ཉོན་མོངས་པའི་གཉེན་པོ༌[^364]བསྩགས་པ་བསྟན་ཏེ། །ཐོས་པ༌[^365]ལ་མི་དགའ་བས་ཅུང་ཟད་ཐོས་པ་ནི་ཐོས་པ༌[^366]ཉུང་བའོ། །

[Block 387]
ཆོས་ཀྱི་ནན་ཏན་བྱེད་ཅེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་རྣམས་བསྒོམས༌[^367]ཤིང་སྒྲུབ་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 388]
དེ་ནི་འདི་སྐད་དུ་ཉན་ཐོས་ལྟར་ཐོས་པ་མི་མང་བར་ཐོས༌[^368]པ་ཅུང་ཟད་ཅིག་གིས་ཆོས་ཀྱི་ནན་ཏན་བྱེད་དོ་ཞེས་བསྟན་པའོ། །

[Block 389 [HEADING]]
###### **སངས་རྒྱས་མཉེས་པར་བྱེད་པ།** ^1-1-3-4-1-2-0

[Block 390]
སངས་རྒྱས་མཉེས་པར་བྱེད་པ༌[^369]ཡང་རྣམ་པ་གཉིས་ཏེ། ཆོས་ཉིད་ཀྱིས་མཉེས་པར་བྱེད་པ་དང་། ཟང་ཟིང་གིས་མཉེས་པར་བྱེད་པའོ། །

[Block 391 [HEADING]]
###### **ཆོས་ཉིད་ཀྱིས་མཉེས་པར་བྱེད་པ།** ^1-1-3-4-1-2-1-0

[Block 392]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་ཡང་རིམ་གྲོ་དང་ཞེས་བྱ་བས་ཆོས་ཉིད་ཀྱིས༌[^370]མཉེས་པར་བྱེད་པ་བསྟན་ཏེ། མ་རིག་པའི་གཉིད་ལས་སད་ཅིང་ཤེས་བྱ་ཐམས་ཅད་ཐུགས་སུ་ཆུད་པས་ན་སངས་རྒྱས་སོ། །

[Block 393 [HEADING]]
###### **ཟང་ཟིང་གིས་མཉེས་པར་བྱེད་པ།** ^1-1-3-4-1-2-2-0

[Block 394]
བདུད་བཞི་བཅོམ་པས་ན༌[^371]བཅོམ་ལྡན་འདས་ཏེ། དེས་ཇི་སྐད་དུ་བསྟན་པའི་བཀའ་ལུང་དང་བསླབ་པའི་ཚིག་ལས་འདའ་བར་མི་བྱེད་པ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་རིམ་གྲོར་བྱེད་པ་དང་། བསྙེན་བཀུར་བྱེད་པ་ཞེས་བྱ་བས་ཟང་ཟིང་གིས་མཉེས་པར༌[^372]བྱེད་པ་བསྟན་ཏེ། བསྐལ་པ་བརྒྱའི་བར་དུ་ཕྱག་འཚལ་བ་དང་། བསྐོར་བ༌[^373]དང་ཆོས་གོས་ལ་སོགས་པ༌[^374]བསྙེན་བཀུར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 395]
ཞུམ་པ་མེད་ཅེས་བྱ་བ་ནི་མཉེས་པ་རྣམ་པ་གཉིས་བྱེད་པ་ལ་སེམས་སྤྲོ་ཞིང་། སྤ་གོང༌[^375]བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 396]
དེས་ནི་མདོར་ན་གང་ལ། གང་། གང་གིས་མཉེས་པར་བྱེད་པ་བསྟན་ཏེ། གང་ལ་མཉེས་པར་བྱེད་པ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལའོ། །

[Block 397]
གང་ནི་རིམ༌[^376]གྲོ་བྱེད་པ་དང་བཀུར་སྟིས་སོ། །

[Block 398]
གང་གིས་ན་ཞུམ་པ་མེད་པའི་སེམས་ཀྱིས་སོ། །

[Block 399]
མདོ་གཞན་དག་ལས་རང་སངས་རྒྱས་གཞན་ལ་མ་མཉན་པར་རང་གི་བློས་ཆོས་རྟོགས་པ༌[^377]དང་། སངས་རྒྱས་འཇིག་རྟེན་དུ་མི༌[^378]འབྱུང་བའི་ཚེ་རང་སངས་རྒྱས་འབྱུང་ངོ་ཞེས་བཤད་པ་ཡང་རང་སངས་རྒྱས་ཟག་པ་མེད་པའི་ཆོས་མངོན་པར་རྟོགས་པའི༌[^379]ཚེ་གཞན་གྱི་ལུང་ལ་མི་བརྟེན་པ་དང་། རང་སངས་རྒྱས་ཀྱི་འབྲས་བུ་ཐོབ་ནས། གདོད་སངས་རྒྱས་མི་བཞུགས་པ་ན་འབྱུང་བ་ལ་བྱའི། འདིར་ནི་དང་པོ་སློབ་ཅིང་ཚོགས་བསོག་པ༌[^380]ལ་བྱ་བས་ཉེས་པ་མེད་དོ། །

[Block 400 [HEADING]]
###### **རིགས།** ^1-1-3-4-1-3-0

[Block 401]
རིགས་ཀྱང་རྣམ་པ་གསུམ་སྟེ། ང་རྒྱལ་སྤྱོད་པའི་རིགས་དང་། སྙིང་རྗེ་ཆུང་བའི་རིགས་དང་། ཉོན་མོངས་པ་ཆུང་བའི་རིགས་སོ། །

[Block 402 [HEADING]]
###### **ང་རྒྱལ་སྤྱོད་པའི་རིགས།** ^1-1-3-4-1-3-1-0

[Block 403]
ང་རྒྱལ་སྤྱོད་པའི་རིགས་ཀྱང་རྣམ་པ་གཉིས་ཏེ། དབང་པོ་འབྲིང་དང་། སྦྱོར་བ་དམ་པ་ལ་གནས་པའོ། །

[Block 404 [HEADING]]
###### **དབང་པོ་འབྲིང།** ^1-1-3-4-1-3-1-1-0

[Block 405]
དབང་པོ་བར་མ་ཞེས་བྱ་བས་དབང་པོ་འབྲིང་བསྟན༌[^381]ཏེ། དབང་པོ་རྣམ་པ་གསུམ་སྟེ།[^382] རབ་དང་བར་མ་དང་ཐ་མའོ། །

[Block 406]
རང་སངས་རྒྱས་རྣམས་ནི་དབང་པོ་བར་མ་སྟེ། དབང་པོ་འབྲིང་གི་རིགས་ཅན་ནོ། །

[Block 407 [HEADING]]
###### **སྦྱོར་བ་དམ་པ་ལ་གནས་པ།** ^1-1-3-4-1-3-1-2-0

[Block 408]
རྟག་ཏུ་རབ་ཏུ་འབྱུང་བ་ལ་གཞོལ་ཞེས་བྱ་བས་སྦྱོར་བ་དམ་པ་ལ་གནས་པ་བསྟན་ཏེ། རྟག་ཏུ་ནི་དུས་ཐམས་ཅད་དོ། །

[Block 409]
ཇི་སྐད༌[^383]དུ་བཅོམ་ལྡན་འདས་ཀྱིས༌[^384]བཤད་པ། སྐྲ་དང་ཁ་སྤུ་བྲེགས་གོས་ངུར་སྨྲིག་བགོས་ཏེ། ཡང་དག་པར་དད་པས་ཁྱིམ་ནས་ཁྱིམ་མེད་པར་རབ་ཏུ་བྱུང་ཞེས་གསུངས་པས་ནི་རབ་ཏུ་བྱུང་བ་ལ་གཞོལ་བའོ། །

[Block 410]
འདིས་དགེ་སློང་གི་ཕུན་སུམ་ཚོགས་པ་རྣམ་པ་བཞི་བསྟན་ཏེ། ཆ་ལུགས་ཕུན་སུམ་ཚོགས་པ་དང་། ལས་ཕུན་སུམ་ཚོགས་པ་དང་། བསམ་པ་ཕུན་སུམ་ཚོགས་པ་དང་། གནས་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 411 [HEADING]]
###### **ཆ་ལུགས་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-4-1-3-1-2-1-0

[Block 412]
དེ་ལ་སྐྲ་དང་ཁ་སྤུ་བྲེགས་ཏེ་གོས་ངུར་སྨྲིག་བགོས་ཞེས་བྱ་བས་ཆ་ལུགས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ཆ་ལུགས་འདི་ནི་ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་དང་། མི་མཐུན་པ་ཡིན་པས་ཁྱིམ་ན་གནས་པའི་ཆ་ལུགས་ལས་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 413 [HEADING]]
###### **ལས་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-4-1-3-1-2-2-0

[Block 414]
ཡང་དག་པར་ཞེས་བྱ་བས་ལས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། གསོལ་བ་དང་བཞིའི་ལས་ཀྱིས་རབ་ཏུ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 415 [HEADING]]
###### **བསམ་པ་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-4-1-3-1-2-3-0

[Block 416]
དད་པས་ཞེས་བྱ་བས་བསམ་པ༌[^385]ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། རྒྱལ་པོ་དང་རྐུན་པོའི་འཇིགས་པས་རབ་ཏུ་བྱུང་བ་ནི་མ་ཡིན་གྱི། དད་པས་རབ་ཏུ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 417 [HEADING]]
###### **གནས་ཕུན་སུམ་ཚོགས་པ།** ^1-1-3-4-1-3-1-2-4-0

[Block 418]
ཁྱིམ་ནས་ཁྱིམ་མེད་པར་རབ་ཏུ་བྱུང་ཞེས་བྱ་བས་གནས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ཁྱིམ་ན་གནས་པ་རྣམས་ཀྱི་གནས་རབ་ཏུ་མི་བཟད་པ་དེ་བཏང་ནས་ཁྱིམ་མེད་པའི་ཤིང་དྲུང་ལ་སོགས་པ་ལ་གནས་པས་སོ། །

[Block 419 [HEADING]]
###### **སྙིང་རྗེ་ཆུང་བའི་རིགས།** ^1-1-3-4-1-3-2-0

[Block 420]
སྙིང་རྗེ་ཆུང་བའི་རིགས་ཀྱང་རྣམ་པ་གཉིས་ཏེ། བདག་འབའ་ཞིག་གི་དོན་ལ་འཇུག་པ་དང་། གཞན་གྱི་དོན་མི་བྱེད་པའོ། །

[Block 421 [HEADING]]
###### **བདག་འབའ་ཞིག་གི་དོན་ལ་འཇུག་པ།** ^1-1-3-4-1-3-2-1-0

[Block 422]
དེ་ལ་དོན་ཉུང་ཞེས་བྱ་བས་བདག༌[^386]འབའ་ཞིག་གི་དོན་ལ་འཇུག་པ་བསྟན་ཏེ། བདག་ཞི་བར་བྱ་བ་དང་། གྲོལ་བར་བྱ་བ་དང་། མྱ་ངན་ལས་འདས་པར་བྱ་བ་ཙམ་ལས་བྱ་བ་གཞན་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 423 [HEADING]]
###### **གཞན་གྱི་དོན་མི་བྱེད་པ།** ^1-1-3-4-1-3-2-2-0

[Block 424]
བྱེད་པ་ཉུང་ཞེས་བྱ་བས་གཞན་གྱི་དོན་མི་བྱེད་པ་བསྟན་ཏེ། གཞན་ཞི་བར་བྱ་བ་དང་། མྱ་ངན་ལས་འདས་པར་བྱ་བ་ལ་མི་འབད་པར་བྱ་བས༌[^387]སོ། །

[Block 425 [HEADING]]
###### **ཉོན་མོངས་པ་ཆུང་བའི་རིགས།** ^1-1-3-4-1-3-3-0
--- END BLOCKS ---
