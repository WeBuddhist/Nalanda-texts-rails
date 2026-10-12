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
[Block 246]
སེམས་དེ་ནི་ཉོན་མོངས་པ་ཐམས་ཅད་དང་མ་འདྲེས་པར་སྐྱེས་སོ། །

[Block 247]
ཐེག་པ་གཞན་ལ་འདོད་པ་མེད་པས་སེམས་དེ་ནི་མ་འབྲེལ་བར་སྐྱེས་སོ། །

[Block 248]
ཕས་ཀྱི་རྒོལ་བ་ཐམས་ཅད་ཀྱིས་མི་འཕྲོགས་པས་སེམས་དེ་ནི་སྲ་བར་སྐྱེས་སོ། །

[Block 249]
སེམས་དེ་ནི་བདུད་ཐམས་ཅད་ཀྱིས་མི་ཕྱེད་པར་སྐྱེས་སོ། །

[Block 250]
དགེ་བའི་རྩ་བ་ཐམས་ཅད་ཡང་དག་པར་སྒྲུབ་པས་སེམས་དེ་བརྟན་པར་སྐྱེས་སོ། །

[Block 251]
འདུས་བྱས་ཐམས་ཅད་མི་རྟག་པར་ཤིན་ཏུ་རིག་པས་སེམས་དེ་ནི་རྟག་པར་སྐྱེས་སོ། །

[Block 252]
སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཡང་དག་པར་སྡུད་པས་སེམས་དེ་ནི་མི་གཡོ་བར་སྐྱེས་སོ། །

[Block 253]
ལོག་པར་སྒྲུབ་པ་ཐམས་ཅད་དང་བྲལ་བས་སེམས་དེ་ནི་མི་བརྫི་བར༌[^121]སྐྱེས་སོ། །

[Block 254]
མི་བསྐྱེད་པས་སེམས་དེ་ནི་རྟག་པར་སྐྱེས་སོ། །

[Block 255]
གཉེན་པོ་མེད་པས་སེམས་དེ་ནི་དཔེ་མེད་པར་སྐྱེས་སོ། །

[Block 256]
ཆོས་ཐམས་ཅད་འབིགས་པས་སེམས་དེ་ནི་རྡོ་རྗེ་ལྟ་བུར་སྐྱེས་སོ། །

[Block 257]
བསོད་ནམས་ཀྱི་ཚོགས་ཚད་མེད་པ་བསགས་པས་སེམས་དེ་ནི་མུ་མེད་པར་སྐྱེས་སོ། །

[Block 258]
སེམས་ཅན་ཐམས་ཅད་ལ་སེམས་དེ་ནི་མཉམ་པར་སྐྱེས་སོ། །

[Block 259]
རང་བཞིན་གྱིས༌[^122]ཀུན་ནས་ཉོན་མོངས་པ་མེད་པས་སེམས་དེ་ནི་རྣམ་པར་དག་པར་སྐྱེས་སོ། ། ཤེས་རབ་ཀྱི་འོད་གསལ་བའི་ཕྱིར་སེམས་དེ་ནི་དྲི་མ་མེད་པར་སྐྱེས་སོ། །

[Block 260]
ལྷག་པའི་བསམ་པ་མ་བོར་བར་སེམས་དེ་ནི་ཤིན་ཏུ་ངེས་པར་སྐྱེས་སོ། །

[Block 261]
བྱམས་པ་ནམ་མཁའ་དང་མཉམ་ཞིང་མཚུངས་པས་ན་སེམས་དེ་ནི་ཡངས་པར་སྐྱེས་སོ། །

[Block 262]
སེམས་ཅན་ཐམས་ཅད་གོ་འབྱེད་པས་སེམས་དེ་ནི་རྒྱ་ཆེ་བར་སྐྱེས་སོ། །

[Block 263]
སེམས༌[^123]ཆགས་པ་མེད་པའི་ཡེ་ཤེས་ལ་བཏང་བས་སེམས་དེ་ནི་སྒྲིབ་པ་མེད་པར་སྐྱེས་སོ། །

[Block 264]
སྙིང་རྗེ་ཆེན་པོ་རྒྱུན་མ་ཆད་པས་ན་སེམས་དེ་ནི་ཐམས་ཅད་ཀྱི་རྗེས་སུ་སོང་བར་སྐྱེས་སོ། །

[Block 265]
ཡོངས་སུ་བསྔོ་བའི་ཆོ་ག་ཤེས་པས་ན་སེམས་དེ་ནི་རྒྱུན་མ་ཆད་པར་སྐྱེས་སོ། །

[Block 266]
ཐམས་ཅད་མཁྱེན་པས་རབ་ཏུ་སྟོན་པས་ན་སེམས་དེ་ནི་སྔོན་དུ་འགྲོ་བར་སྐྱེས་སོ། །

[Block 267]
ཐེག་པ་གཞན་ལ་མ་ཞུགས་པས་ན་སེམས་དེ་ནི་བལྟ་བར་འོས་པའོ། །

[Block 268]
དེ་ནི་སེམས་ཅན༌[^124]ཐམས་ཅད་ཀྱི༌[^125]བལྟར་མི་མཐོང་བར་སྐྱེས་སོ། །

[Block 269]
དེ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱིས་བརྒྱན་པར་སྐྱེས་སོ། །

[Block 270]
དེ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱིས་རབ་ཏུ་རྟོགས་ཏེ་སྐྱེས་སོ། །

[Block 271]
དེ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཀྱི་ས་བོན་དུ་སྐྱེས་སོ། །

[Block 272]
དེ་ནི་ཆོས་ཐམས་ཅད་ཀྱིས༌[^126]མི་ཤིགས༌[^127]པར་སྐྱེས་སོ། །

[Block 273]
དེ་ནི་བདེ་བའི་དངོས་པོ་ཐམས་ཅད་ཀྱི་གནས་སུ་སྐྱེས་སོ། །

[Block 274]
དེ་ནི་སྦྱིན་པའི་ཚོགས་ཀྱིས༌[^128]བསགས་ཏེ་སྐྱེས་སོ། །

[Block 275]
དེ་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཚོགས་ཀྱིས་སྨོན་ལམ་གྱི༌[^129]འཕགས་པར་སྐྱེས་སོ། །

[Block 276]
དེ་ནི་བཟོད་པའི་ཚོགས་ཀྱིས་བསྙེན་བཀུར་བར་སྐྱེས་སོ། །

[Block 277]
དེ་ནི་བརྩོན་འགྲུས་ཀྱི་ཚོགས་ཀྱིས་རྒྱལ་བར་དཀའ་བར་སྐྱེས་སོ། །

[Block 278]
དེ་ནི་བསམ་གཏན་གྱི་ཚོགས་ཀྱིས་ཞི་བའི་མཚན་ཉིད་དུ་སྐྱེས་སོ། །

[Block 279]
དེ་ནི་ཤེས་རབ་ཀྱི་ཚོགས་ཀྱིས་ཐོགས་པ་མེད་པར་སྐྱེས་སོ། །

[Block 280]
བྱམས་པ་ཆེན་པོ་བསགས་པས་དེ་ནི་གནོད་པ་མེད་པར་སྐྱེས་སོ། །

[Block 281]
སྙིང་རྗེ་ཆེན་པོ་བསགས་པས་དེ་ནི་རྩ་བ་བརྟན་པར་སྐྱེས་སོ། །

[Block 282]
དེ་ནི་དགའ་བ་ཆེན་པོ་བསགས་ཏེ་མགུ་བ་དང་མོས་པ་དང་མཆོག་ཏུ་དགའ་བ་ལ་གནས་པར་སྐྱེས་སོ། །

[Block 283]
དེ་ནི་བཏང་སྙོམས་ཆེན་པོ་གནས་པ་སྟེ་བདེ་བ་དང་སྡུག་བསྔལ་གྱིས༌[^130]མི་བསྒུལ་བར་སྐྱེས་སོ། །

[Block 284]
དེ་ནི་སངས་རྒྱས་ཀྱི་བྱིན་གྱི་རླབས༌[^131]ཀྱིས་བརླབ་པར༌[^132]སྐྱེས་སོ། །

[Block 285]
དཀོན་མཆོག་གསུམ་གྱི་རིགས་རྒྱུན་མི་བཅད་པའི་ཕྱིར་ཚུལ་རྒྱུན་མི་འཆད་པར་སྐྱེས་སོ། །
--- END BLOCKS ---
