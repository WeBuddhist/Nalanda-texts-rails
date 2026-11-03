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
[Block 316]
འདར་བར་གྱུར་པ་ཞེས་བྱ་བ་ནི་གནོད་པར་གྱུར་པའོ། །

[Block 317]
དེ་ཞེས་བྱ་བ་ནི་དེའི་ཕྱིར་རོ། །

[Block 318]
རྨད་དོ་ཞེས་བྱ་བ་ནི་ངོ་མཚར་རོ་ཞེས་བྱ་བའོ།

[Block 319]
[^143] །དེ་ནས་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པའོ། །

[Block 320]
བྱང་ཆུབ་སེམས་དཔའ་བརྟབས་ཤིང་རིངས་པའི་ཚིག་གང་ཡིན་པ་དེ་ནི་རིངས་རིངས་སྐད་དུ་སྨྲ་བའི་ཚིག་བཟླས་པ་སྟེ། ཇི་ལྟ་བུ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 321]
རང་བཞིན་ཁྱད་པར་ཅན་གསལ་བ་ཞེས་བྱ་བ་ལ་རང་བཞིན་ནི་ངོ་བོ་ཉིད་དོ། །

[Block 322]
ཁྱད་པར་ཅན་ནི་དམ་པའོ། །

[Block 323]
གསལ་བར་སྟོན་པ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་སྟོན་པའོ། །

[Block 324]
སྙིང་རྗེ་ནི་བརྩེ་བའོ། །

[Block 325]
དབང་གིས་ཞེས་བྱ་བ་ནི་སྤྲོ་བས་སོ། །

[Block 326]
ཚིག་གི༌[^144]འབྲུ་ཞེས་བྱ་བ་ནི་ཡི་གེའོ། །

[Block 327]
གསལ་བ་ཞེས་བྱ་བ་ནི་སེམས་མ་འཁྲུལ་པའོ། །

[Block 328]
སློབ་མ་ནི་མ་ཕམ་པའོ། །

[Block 329]
སྨྲས་པ་ནི་བསྟན་པའོ། །

[Block 330]
བུ་བུ་ཞེས་བྱ་བ་ནི་རྟག་པར་ཟློས་པའོ། །

[Block 331]
འཁོར་བ་ནི་འཁོར་བར་བྱེད་པས་ན་འཁོར་བའོ། །

[Block 332]
ཡོན་ཏན་མེད་པ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་ཕྱིར་རྒོལ་བར་གྱུར་པས་སོ། །

[Block 333]
ལྟོས་ཞེས་བྱ་བ་ནི་ལྟོས་ཤིག་ཅེས་པའོ། །

[Block 334]
གཅན་གཟན་མོ་ཞེས་བྱ་བ་ནི་གཅན་གཟན་གྱི་རིགས་སོ། །

[Block 335]
བྱམས་པ་ནི་བརྩེ་ཞིང་དགའ་བ་དང་རྗེས་སུ་འབྲེལ་པའོ། །

[Block 336]
མཚམས་ནི་རྣམ་པར་གནས་པའོ། །

[Block 337]
འདས་པ་ནི་བརྒལ་བའོ། །

[Block 338]
བདག་གི་བུ་ཞེས་བྱ་བ་ནི་རང་གི་བུའོ། །

[Block 339]
འདི་སྐད་བསྟན་ཏེ། བྱམས་པའི་མཚམས་སུ་བྱས་པ་སྟེ། སྟག་མོ་གང་ཡིན་པ་དེས་འདས་པར་བྱས་ཞེས་པའོ། །

[Block 340]
ཨེ་མ་ཞེས་པ་ནི་ངོ་མཚར་དུ་གྱུར་པའོ། །

[Block 341]
ཀྱི་ཧུད་ཅེས་བྱ་བ་ནི་སྐྱོ་བ་དང་རྗེས་སུ་བརྩེ་བས་སོ། །

[Block 342]
ཀྱི་ཧུད་ཅེས་བྱ་བ༌[^145]ནི། དཀའ་བས་སོ། །

[Block 343]
བདག་ལ་བྱམས་པ་ནི་བདག་ལ་དགའ་བའོ། །

[Block 344]
མི་བཟད་དོ་ཞེས་བྱ་བ་ནི་སྙིང་རྗེ་མེད་པའོ། །

[Block 345]
གང་གི་ཕྱིར་ཞེས་བྱ་བ་ནི་གང་གིས་སོ། །

[Block 346]
མ་ནི་སྐྱེད་པར་བྱེད་པའོ། །

[Block 347]
ཡང་གི་སྒྲ་ནི་སྲིད་པའི་ཚུལ་ལོ། །

[Block 348]
བུ་ནི་བུའོ། །

[Block 349]
བཟའ་བ༌[^146]ནི་ཟ་བའོ། །

[Block 350]
འདོད་པ་ནི་མངོན་པར་འདོད་པའོ། །

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
--- END BLOCKS ---
