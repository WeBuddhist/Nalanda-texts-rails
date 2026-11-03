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
བསམས་པ་ནི་བསམས་པ་ལ་ཞུགས་པའོ། །

[Block 387]
ཡོད་བཞིན་དུ་ཞེས་བྱ་བ་ནི་ལྡན་བཞིན་དུའོ། །

[Block 388]
ཚང་བ་ཞེས་བྱ་བ་ནི་མ་ལུས་པའོ། །

[Block 389]
ཚང་བ་ཞེས་སྨོས་པ་ནི་གཞན་དག་འདི་ལྟར་མ་གྱུར་པའི་ཕྱིར་ཏེ། ལ་ལ་ཡན་ལག་མ་ཚང་བ་ལས་ནི་ཡོངས་སུ་གཏོང་བ་དང་ལྡན་པ་ཡིན་ནོ་ཞེས་མི་འཛིན་པས་སོ། །

[Block 390]
ལུས་ནི་འཇིག་པའི་བདག་ཉིད་པས་ལུས་སོ། །

[Block 391]
ཅི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཅིའི་རྒྱུས་སོ། །

[Block 392]
གཞན་ལ་ཞེས་བྱ་བ་ནི་གཞན་དག་གི་སྟེ་ཤའོ། །

[Block 393]
བཙལ་བ་ནི་བསླང་བར་བྱ་བའོ། །

[Block 394]
དེ་ཞེས་བྱ་བ་ནི་སློབ་མས་ཀྱང་ངོ་། །གཏོལ་མེད་ཅེས་བྱ་བ་ནི་གློ་བུར་དུ་རྙེད་དམ་མི་རྙེད་མ་ངེས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 395]
གང་གི་ཕྱིར་བདག་གི་དགོས་པ་ཞེས་བྱ་བ་ནི་རྙེད་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 396]
དགོས་པ་མི་འགྲུབ་སྲིད་ཅེས་བྱ་བ་ནི་བྱ་བ་མི་འགྲུབ་ཅིང་འཇིག་པར་འགྱུར་ཞེས་བྱའོ། །

[Block 397]
གཉིས་སུ་ན་ཞེས་བྱ་བ་ནི་གཞན་ཡང་ངོ་། །བདག་མེད་ཅེས་བྱ་བ་ནི་བདག་དང་བྲལ་བའོ། །

[Block 398]
འཇིག་ལ་ཞེས་བྱ་བ་ནི་འཇིག་པའི་ངོ་བོ་ཉིད་ཡིན་པས་སོ། །

[Block 399]
སྙིང་པོ་མེད་པ་ནི་སྙིང་པོ་མེད་པའི་བདག་ཉིད་དེ་ཆུ་ཤིང་གི་སྡོང་པོ་ལྟ་བུའོ། །

[Block 400]
སྡུག་བསྔལ་ཞེས་བྱ་བ་ནི་གནོད་པ་སྣ་ཚོགས་ཀྱི་གཞིར་གྱུར་པ་ཡིན་པས་སྡུག་བསྔལ་ལོ། །

[Block 401]
དྲིན་མེད་ཅེས་བྱ་བ་ནི་གང་ཕན་པ་བྱས་པ་གང་ཡིན་པ་དེ་ཡང་འཇིག་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 402]
རྟག་ཏུ་ཞེས་བྱ་བ་ནི་དུས་ཐམས་ཅད་དུའོ། །

[Block 403]
མི་གཙང་བ་ནི་ཕྱིས་དང་། གཅིན་དང་། མཆིལ་མ་ལ་སོགས་པ་འཛག་པའི་ཕྱིར་མི་གཙང་བའོ། །

[Block 404]
ལུས་ནི་ལུས་སོ། །

[Block 405]
གཞན་ལ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དོན་དུའོ། །

[Block 406]
ཕན་ཐོགས་པར་གྱུར་པ་ནི་ཉེ་བར་སྦྱོར་བར་གྱུར་པའོ།[^164] །དགའ་བར་མི་འགྱུར་བ་ནི༌[^165]དགའ་བར་གྱུར་པའོ། །

[Block 407]
མཁས་པ་ནི་རྟོགས་པའོ། །

[Block 408]
བདག་ནི་བདེ་བ་ལ་ཆགས༌[^166]ཞེས་བྱ་བ་ནི་རང་གི་བདེ་བ་ལ་ཞེན་པའོ། །

[Block 409]
གཞན་གྱི་སྡུག་བསྔལ་ཡལ་བར་འདོར་བ་ནི་ཐ་མལ་པར༌[^167]འདུག་པ་ཉིད་དོ། །

[Block 410]
མཐུ་མེད་དམ་ཞེས་བྱ་བ་ནི། སྤྲོ་བ་ཉམས་པའོ། །

[Block 411]
དམ་ཞེས་བྱ་བའི་སྒྲ་ནི་རྣམ་པ་གཉི་གར་བརྟག་པའོ། །

[Block 412]
གཞན་གྱི་སྡུག་བསྔལ་ཞེས་བྱ་བ་ནི་དེ་གཞན་ལ་སྡུག་བསྔལ་ཡོད་པ་སྟེ། འདི་ལྟར་གཞན་དག་སྡུག་བསྔལ་བས་སྡུག་བསྔལ་བ་དག་ལ་བདེ་བ་མེད་དོ། །

[Block 413]
ནུས་པ་ཡོད་བཞིན་དུ་ཞེས་བྱ་བ་ནི་སྐྱེས་བུའི་བྱེད་པ་སྟེ། འདི་ལྟར་ལུས་ཡོངས་སུ་གཏོང་བའོ། །

[Block 414]
ཅི་སྟེ་ཞེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་ཡལ་བར་འདོར་བར་བྱེད་ཅེས་བྱ་བ་ཡིན་ནོ། །

[Block 415]
ནུས་པ་ཡོད་བཞིན་ཞེས་བྱ་བ་ནི་ལྡན་པ་སྟེ་སྐྱེས་བུའི་བྱེད་པའོ། །

[Block 416]
བདག་གིས་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱིས་སོ། །

[Block 417 [VERSE]]
གལ་ཏེ་ཡལ་བོར་ཞེས་བྱ་བ་སྟེ། །
གལ་ཏེ་ཐ་མལ་པར་བདག་འདུག་ནའོ། །

[Block 418]
གསོད་པའི་དགྲ་ནི་ཕས་ཀྱི་དགྲ་སྟེ་གསོད་པར་འདོད་པའོ། །

[Block 419]
སྡུག་བསྔལ་བྱིང་བ་ཞེས་བྱ་བ་ནི་ཕོངས་པར་བྱིང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 420]
སྡིག་པ༌[^168]བྱས་པ་བཞིན་ཞེས་བྱ་བ་ནི་བདག་གིས་ཏེ་ཕྱི་ནས་ཡིད་ལ་གཅགས་པའི་ཕྱིར་རོ། །

[Block 421]
བདག་གི་སེམས་ནི་རང་གི་སེམས་སོ། །

[Block 422]
དེ་འགྱོད་པའི་མེ་དེས་སེམས་ཀུན་ཏུ་ཚིག་པ་ཡིན་ཏེ། ཇི་ལྟ་བུ་ཞེ་ན། འདི་ལྟར་མེ་ཆེན་པོས་འདམ་བུའམ་རྩྭ་དག་ཚིག་པ་ཡིན་ནོ། །

[Block 423]
དེ་བས་ཞེས་བྱ་བ་ནི་དེའི་ཕྱིར་རོ། །

[Block 424]
བསྲུང་བར་བྱ་བ་ནི་བསྲུང་བའོ། །

[Block 425]
ལུས་ཞེས་བྱ་བ་ལ། ཀ་ཞེས་བྱ་བའི་སྒྲ་ངན་པར་བསྟན་ཏོ། །
--- END BLOCKS ---
