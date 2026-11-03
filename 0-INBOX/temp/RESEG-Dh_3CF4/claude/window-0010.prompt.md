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
[Block 351]
གང་གི་ཕྱིར་ཞེས་བྱ་བ་ནི་གང་གི་རྒྱུས་སོ། །

[Block 352]
འདི་འདྲའི་ཞེས་བྱ་བ་ནི་བུ་ཟ་བར་འདོད་པ་དེའི་ལས་སྟོན་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 353]
ལས་ནི་བྱ་བའོ། །

[Block 354]
ཀྱང་གི་སྒྲ་ནི་སྲིད་པ་ཉིད་དོ། །

[Block 355]
བྱེད་པ་ནི་བྱེད་པར་གྱུར་པའོ། །

[Block 356]
རྩོལ་བ་དེ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་གནས་པ་དང་། འབད་པ་དང་འཇུག་པའོ། །

[Block 357]
བདག་ལ་བྱམས་པ་ནི་བདག་ལ་དགའ་བའོ། །

[Block 358]
འདི་ཞེས་བྱ་བ་ནི་ཉེ་བར་སྟོན་པ་ཡིན་ནོ། །

[Block 359]
དགྲ་ནི་ཤ་ཁོན་ཅན་ནོ། །

[Block 360]
སུ་ཞིག་ཅེས་བྱ་བ་ཇི་ལྟར་ཞེས་པའོ། །

[Block 361]
འཕེལ་བར་བྱེད་པ་ནི་སྐྱེད་པར་བྱེད་པའོ། །

[Block 362]
ཡོད་ཅེས་བྱ་བ་ནི་འོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 363]
དེ་བས་ན་ཞེས་བྱ་བ་ནི་དེའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། བུ་ཟ་བར་འདོད་པ་དེ་བས་ན་ཚོལ༌[^147]ཅིག་པའོ། །

[Block 364]
མྱུར་དུ་ཞེས་བྱ་བ་ནི་རིངས་པར་རོ། །

[Block 365]
ཚོལ༌[^148]ཅིག་པ་ནི་བཙལ་བ་སྟེ། དེས་བུ་ཟ་བར་མི་འགྱུར་བ་དེ་ལྟར་ཚོལ༌[^149]ཅིག་པའོ། །

[Block 366]
གང་ཞིག་ནས་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཡོང་ངོ་། ། འདི་ཞེས་བྱ་བ་ནི་སྟག་མོའོ། །

[Block 367]
བཀྲེན་པའི༌[^150]སྡུག་བསྔལ་ནི་ཞེས་བྱ་བ་ནི༌[^151]འདོད་པའི་ཚོལ༌[^152]བའོ། །

[Block 368]
བསལ་བ༌[^153]ནི་གསོ་བའོ། །

[Block 369]
རྒྱུ་ནི་རྒྱུ་ཉིད་དོ། །

[Block 370]
ཇི་ལྟར་མོ་བདག་དང་ཕྲུ་གུ༌[^154]རྣམས་མ་རུང་བར་མི་འགྱུར་བར་ཞེས་བྱ་བ་ནི་སྟག་མོ་དང་ཕྲུ་གུ༌[^155]གཉིས་ཏེ། བུ་དང་བདག་ཉིད་མ་རུངས་པར༌[^156]མ་གྱུར་པ་ཞེས་བྱ་བ་ནི་འཆི་བར་མ་གྱུར་པའོ། །

[Block 371]
དགག་པ༌[^157]གཉིས་སྨོས་པ་ནི་དོན་གྱི་རང་བཞིན་སྨོས་པར་བྱེད་པ་སྟེ། འཆི་བ་ཉིད་ཀྱིས་འཆི་བར་མི༌[^158]འགྱུར་བའོ། །

[Block 372]
མོ་བདག་ལ་གནོད་པ་ནི་བུ་བསད་པའི་སྡིག་པས་འཇིག་རྟེན་ཕ་རོལ་དུ་ངན་སོང་དུ་འགྲོ་བའོ། །

[Block 373]
བདག་ཀྱང་འདི་ཞེས་བྱ་བ་འདིས་ནི་བྱང་ཆུབ་སེམས་དཔའ་རང་གི་ལུས་ཀྱི་སྦྱིན་པ་ཡིན་པ་ལ་བསམས་ནས་སྨྲས་པའོ། །

[Block 374]
དེས་ཞེས་བྱ་བ་ནི་སློབ་མའོ། །

[Block 375]
དེ་བཞིན་དུ་བགྱིའོ་ཞེས་ནས་སོ། །

[Block 376]
དེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ལས་དེའོ། །

[Block 377]
མཉན་ཏེ་ཞེས་བྱ་བ་ནི་མཉན་ནས་སོ། །

[Block 378]
དེའི་ཟས་ཞེས་བྱ་བ་ནི་སྟག་མོ་དང་སྦྱར་རོ། །

[Block 379]
ཚོལ་བ༌[^159]ནི་བཙལ་བའོ། །

[Block 380]
འབད་པ་ནི་ནན་ཏན༌[^160]ཏེ། དེ་བྱས་པར་གྱུར་ཏོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 381]
དེ་ནས་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པའོ། །

[Block 382]
བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱིར་སེམས་དཔས༌[^161]ན་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 383]
[^162]སློབ་མ་དེ་ཞེས་བྱ་བ་ནི་མ་ཕམ་པའོ། །

[Block 384]
སྙད༌[^163]བཏགས་ཏེ་ཞེས་བྱ་བའི་དོན་དང་ལྡན་པར་བྱས་ཏེའོ། །

[Block 385]
བཏང་བ་ནི་གཞན་དུ་བཏང་བའོ། །

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
--- END BLOCKS ---
