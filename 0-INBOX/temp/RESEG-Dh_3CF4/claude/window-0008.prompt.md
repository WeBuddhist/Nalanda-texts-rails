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
རི་སུལ་ནི་རིའི་སྨན་ལྗོངས་དང་། ཕུག་དང་ཚང་ཚིང་དང་བཅས་པའོ།[^133] །གནས་ཤིང་སྤྱོད་པ་ནི་སྤྱོད་ཅིང་འདུག་པའོ། །

[Block 282]
དེ་ནས་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པའོ། །

[Block 283]
རིའི་ཁྲོད་ནི་རིའི་ཁྲོད་དེ་སུལ་དག་གོ། །

[Block 284]
དེ་ན་ནི་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་ནའོ། །

[Block 285]
སྟག་མོ་ནི་སྟག་མོ་ཉིད་དོ། །

[Block 286]
ཕྲུ་གུ༌[^134]འབྲངས་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི་བཙས་པར་གྱུར་པའོ། །

[Block 287]
བཙས་པའི་ནད་ཀྱིས་སྡུག་བསྔལ་བ་ཉིད་ནི་ཉོན་མོངས་པའོ། །

[Block 288]
སྐྱོན་ནི་དེའི་སྐྱོན་གྱིས་ལྟོགས་ཤིང་དེས་ཤིན་ཏུ་གཟིར་བའི་སྡུག་བསྔལ་གྱི་དབང་དུ་གྱུར་ཏེའོ། །

[Block 289]
སྤྱོད་པ་ཉམས་པར་གྱུར་ཞེས་བྱ་བ་ནི་འགྲོ་བ་ཉམས་པ་སྟེ་མི་ནུས་པར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 290]
མཐོང་བ་ནི་ཤེས་པའོ། །

[Block 291]
གང་ལ་མིག་ཟུང་ཡོད་པ་དེ་ནི་མིག་གཉིས་ལྟ་བའོ། །

[Block 292]
ལྟ་བ་ནི་མིག་གོ། །

[Block 293]
གཉིས་ནི་ཟུང་ངོ་། །ཞན་པར༌[^135]གྱུར་པ་ནི་མིག་ཕུགས་སུ་ཞུགས་པའོ། །

[Block 294]
བཀྲེས་པ་ནི་ཟ་བར་འདོད་པའོ། །

[Block 295]
ལྟོ་བ་ནི་གསུས་པ་སྟེ་རབ་ཏུ་རྙོང་བ་ནི་རབ་ཏུ་ཞུམ་པར་གྱུར་པ་སྟེ། བཙས་པའི་ནད་ཀྱིས་ལྟོ་རབ་ཏུ་ཞུམ་པར་གྱུར་པའོ། །

[Block 296]
ཁ་ཟས་ཞེས་བྱ་བ་ནི་བཟའ་བ༌[^136]བཞིན་དུ་མཐོང་བར་གྱུར་པས་སོ། །

[Block 297]
དེ་གང་ཡིན་ཞེ་ན། ཕྲུ་གུ༌[^137]དེ༌[^138]ཤིན་ཏུ་གཞོན་པའི་གཟུགས་ཅན་ནོ། །

[Block 298]
བདག་གི་ཞེས་བྱ་བ་ནི་རང་གིའོ། །

[Block 299]
བུ་ཞེས་བྱ་བ་ནི་རང་ལས་སྐྱེས་པའོ། །

[Block 300]
མ་ཞེས་བྱ་བ་ནི་འཛིན་པའོ། །

[Block 301]
ཡིད་གཅུགས་འཇིགས་མེད་ཅེས་བྱ་བ་ནི་དོགས་པ་མེད་པར་རོ། །

[Block 302]
ནུ་ཞོ་ནི། ནུ་མ་ནས་འོང་བའོ། །

[Block 303]
འདོད་ཕྱིར་ཞེས་བྱ་བ་ནི་སྲེད་པ་སྟེ། འཐུང་བར་འདོད་པའོ། །

[Block 304]
ལྷགས་པ་ཞེས་བྱ་བ་ནི་ཉེ་བར་ཕྱིན་པའོ། །

[Block 305]
སྟག་སྐད་ཅེས་བྱ་བ་ནི་སྐད་རྩུབ་པའོ། །

[Block 306]
ཉེར་ཉེར་སྐད་འབྱིན་ཅིང་ཞེས་བྱ་བ་ནི་སྒྲའི་ཁྱད་པར་ལས་བྱ་བ་ཡིན་ཏེ། འཇིགས་སུ་རུང་བས་བསྡིགས་པ་དང་སྐྲོད་པའོ། །

[Block 307]
གཞན་གྱི༌[^139]ཞེས་བྱ་བ་ནི། ཕ་རོལ་གྱིའོ། །

[Block 308]
བཞིན་ཞེས་བྱ་བ་ནི། དཔེས་ཉེ་བར་འཇལ་བའོ། །

[Block 309]
བྱང་ཆུབ་སེམས་དཔས་སྟག་མོ་དེ་མཐོང་ནས། །བརྟན་ཡང་སྙིང་རྗེའི་དབང་གྱུར་བས། །ཞེས་བྱ་བ་ནི་བརྩེ་བའི་དབང་དུ་གྱུར་པས་འདར་བར་གྱུར་པའོ། །ཅིའི་ཕྱིར་འདར་ཞེ་ན། གཞན་གྱི་སྡུག་བསྔལ་གྱིས་སོ། །ཇི་ལྟར་འདར་ཞེ་ན། ས་གཡོས་པའི་ལྗོན་ཤིང་ལྟ་བུར་རོ། །

[Block 310]
ས་ནི་འབྱུང་བའི་རྟེན་ནོ། །

[Block 311]
ལྗོན་ཤིང་ནི་ཤིང་སྟེ། ཇི་ལྟར་ས་གཡོས་པ༌[^140]ན། ཤིང་འགུལ་བ་དེ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་གཞན་གྱི་སྡུག་བསྔལ་གྱིས་འདར་རོ་ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 312]
བདག་གི་སྡུག་བསྔལ༌[^141]ཞེས་བྱ་བ་ནི་རང་གི་སྡུག་བསྔལ་ཆེན་པོ་ལ་ཡང་བརྟན་པས་ཡི་ཆད་པ་དང་། སྒྱིད་ལུག་པ་སྤངས་པ་ཡིན་ནོ། །

[Block 313]
སྙིང་རྗེའི་བདག་ཉིད་ཅེས་བྱ་བ་ནི་སྙིང་རྗེའི་བདག་ཉིད་དུ་གྱུར་པའོ། །

[Block 314]
གཞན་གྱི་ཞེས་བྱ་བ་ནི་ཕ་རོལ་གྱིའོ། །

[Block 315]
ཆུང་ངུ་ནི་ཅུང་ཟད་ཙམ་གྱིས་ཀྱང་ངོ་། །སྡུག་བསྔལ་ནི་ཕོངས༌[^142]པའོ། །

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
--- END BLOCKS ---
