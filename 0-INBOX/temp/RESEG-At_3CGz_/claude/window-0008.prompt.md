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
སྙིང་རྗེ་ཆེན་པོ་བསགས་པས་དེ་ནི་རྩ་བ་བརྟན་པར་སྐྱེས་སོ། །

[Block 282]
དེ་ནི་དགའ་བ་ཆེན་པོ་བསགས་ཏེ་མགུ་བ་དང་མོས་པ་དང་མཆོག་ཏུ་དགའ་བ་ལ་གནས་པར་སྐྱེས་སོ། །

[Block 283]
དེ་ནི་བཏང་སྙོམས་ཆེན་པོ་གནས་པ་སྟེ་བདེ་བ་དང་སྡུག་བསྔལ་གྱིས༌[^130]མི་བསྒུལ་བར་སྐྱེས་སོ། །

[Block 284]
དེ་ནི་སངས་རྒྱས་ཀྱི་བྱིན་གྱི་རླབས༌[^131]ཀྱིས་བརླབ་པར༌[^132]སྐྱེས་སོ། །

[Block 285]
དཀོན་མཆོག་གསུམ་གྱི་རིགས་རྒྱུན་མི་བཅད་པའི་ཕྱིར་ཚུལ་རྒྱུན་མི་འཆད་པར་སྐྱེས་སོ། །

[Block 286]
དེ་ནི་ཕྱོགས་བཅུའི་སངས་རྒྱས་ཀྱི་ཞིང་ཐམས་ཅད་ཀྱི་འཁོར་དུ་རབ་ཏུ་གྲགས་པར་སྐྱེས་སོ། །

[Block 287]
བཙུན་པ་ཤ་ར་དྭ༌[^133]ཏིའི་བུ་ཐམས་ཅད་མཁྱེན་པའི་སེམས་འདི་འདྲ་བ་ལ། ཟད་པ་གང་ཡང་ཡོད་དམ། སྨྲས་པ། རིགས་ཀྱི་བུ་དེ་ནི་མ་ཡིན་ཏེ། གང་ཐམས་ཅད་མཁྱེན་པའི་སེམས་འདི་ལྟ་བུ་ཟད་པར་འདོད་པ་ནི་ནམ་མཁའ་ཟད་པར་འདོད་དོ། །

[Block 288]
བློ་གྲོས་མི་ཟད་པས་སྨྲས་པ། བཙུན་པ་ཤ་ར་དྭ༌[^134]ཏིའི་བུ་དེ་བཞིན་དུ་ཐམས་ཅད་མཁྱེན་པའི་སེམས་དེ་ནི་མི་ཟད་པ་སྟེ། བྱང་ཆུབ་ཀྱི་སེམས་དེ་ནི་དེའི་རྩ་བར་སྐྱེས་པས་ན་དེའི་ཕྱིར་དེ་ནི་མི་ཟད་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 289]
ཡང་མདོ་དེ་ཉིད་ལས་བསམ་པ་དེ་ནི་མ་བྱས་པས་ན་བཅོས་མ་མ་ཡིན་པའོ། །

[Block 290]
གཡོ་བ་མེད་པས་ན་མ་བྱས་པའོ། །

[Block 291]
རབ་ཏུ་རྟོགས་པས་གཡོ་བ་མེད་པའོ། །

[Block 292]
སྒྱུ་མེད་པས་རབ་ཏུ་རྟོགས་པའོ། །

[Block 293]
སྒྱུ་མེད་པས་རབ་ཏུ་དྲང་བའོ།[^135] །

[Block 294]
དག་པས༌[^136]སྒྱུ་མེད་པའོ། །

[Block 295]
གསལ་བས་གྱ་གྱུ་མེད་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གསུངས་ཏེ། མདོ་དེ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 296]
དེ་ལྟ་བུའི་ཐུན་མོང་མ་ཡིན་པའི་སེམས། འཇིག་རྟེན་ཐམས་ཅད་ལས་མངོན་པར་འཕགས་པའི་སེམས། སེམས་ཅན་ཐམས་ཅད་མ་བཏང་བའི་སེམས་དེ་ནི་ས་ཆེན་པོ་ལ་རབ་ཏུ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱིས་དེ་ཉིད་སྦྱངས་ཤིང་དག་པར་བྱས། དེ་མ་ཉམས་པར་བྱས་ཤིང་བསྲུངས། དེ་ས་ནས༌[^137]སར་སྤེལ་ཏེ། དེ་ནི་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་ཐུགས་ཡིན་པས་དེ་བསྐྱེད་ཕན་ཆད་བྱང་ཆུབ་སེམས་དཔའ་དེ་ལ་བསྟན་པ་ལ་དགའ་བའི་ལྷས་བསྲུང་བ་དང་། འཆི་བའི་དུས་སུ་ཡིད་དགའ་བར་འཆི་བ་དང་། བར་མ་དོ་དང་མའི་མངལ་དང་བུ་ཆུང་གི་དུས་སུ་ཡང་ལྷ་དག་གིས༌[^138]བསྲུང་བ་དང་། དགེ་བའི་རྩ་བ་ཐམས་ཅད་ཆུད་མི་ཟ་བ་དང་། སེམས་བསོད་ནམས་ཀྱི་རྒྱུན་དང་ལྡན་པ་ཡིན་ཏེ།

[Block 297]
སློབ་དཔོན་ཞི་བའི་ལྷས་སྤྱོད་འཇུག་ལས།

[Block 298 [VERSE]]
དགེ་བ་གཞན་ཀུན་ཆུ་ཤིང་བཞིན་དུ་ནི། །
འབྲས་བུ་སྨིན་ནས་ཟད་པར་འགྱུར་བ་ཉིད། །
བྱང་ཆུབ་སེམས་ཀྱི་ལྗོན་ཤིང་རྟག་པར་ཡང་། །
འབྲས་བུ་མི་ཟད་རབ་ཏུ་འཕེལ་བར་འགྱུར། །

[Block 299]
ཞེས་གསུངས་སོ། །

[Block 300]
དེ་བས་ན་བྱང་ཆུབ་ཀྱི་སེམས་དེ་མི་ཟད་པས་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་གྱི་ཆོས་ཐམས་ཅད་དང་། འབྲས་བུ་སངས་རྒྱས་ཀྱི་སའི་ཆོས་ཐམས་ཅད་མི༌[^139]ཟད་པ་ཡིན་ནོ། །

[Block 301]
དེ་བས་ན་དུས་དེར་སེམས་དེ་ལྟ་བུ་སྐྱེས་པས༌[^140]ན།

[Block 302 [VERSE]]
དེ་ལྟར་སྨོས་པའི༌[^141]སེམས་དག་ནི། །
བསྐྱེད་པའི་ཡོན་ཏན་གང་ཡིན་པ། །

[Block 303]
ཞེས་བྱ་བ་སྨྲས་ཏེ། དེ་ལྟ་བུའི་སེམས་དེའི་ཕན་ཡོན་སྨྲ་བར་འདོད་ནས། དེ་ནི་སྡོང་པོ༌[^142]བཀོད་པའི་མདོ་ལས་འཕགས་པ་བྱམས་པས་ནོར་བཟངས༌[^143]ལ་འདི་སྐད་དུ་བཤད་དེ། རིགས་ཀྱི་བུ་བྱང་ཆུབ་ཀྱི་སེམས་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཀྱི་ས་བོན་ལྟ་བུའོ། །

[Block 304]
འགྲོ་བ་ཐམས་ཅད་ཀྱི་ཆོས་དཀར་པོ་རྣམ་པར་འཕེལ་བར་བྱེད་པས་ཞིང་ལྟ་བུའོ། །

[Block 305]
འཇིག་རྟེན་པ་ཐམས་ཅད་རྟེན་པས་ས་ལྟ་བུའོ། །

[Block 306]
དབུལ་བ་ཐམས་ཅད་ཡང་དག་པར་འཇོམས་པས་རྣམ་ཐོས་ཀྱི་བུ་ལྟ་བུའོ། །

[Block 307]
བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཡོངས་སུ་བསྲུང་བས༌[^144]ཕ་ལྟ་བུའོ། །

[Block 308]
དོན་ཐམས་ཅད་ཡང་དག་པར་སྒྲུབ་པས་ཡིད་བཞིན་གྱི་ནོར་བུའི་རྒྱལ་པོ་ལྟ་བུའོ། །

[Block 309]
བསམ་པ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་པས་བུམ་པ་བཟང་པོ་ལྟ་བུའོ། །

[Block 310]
ཉོན་མོངས་པའི་དགྲ་ཐམས་ཅད་ཕམ་པར་བྱེད་པས་མདུང་ཐུང་ལྟ་བུའོ། །

[Block 311]
ཚུལ་བཞིན་མ་ཡིན་པའི་ཡིད་ལ་བྱེད་པ་རབ་ཏུ་འགེབས་པས༌[^145]གོ་ཆ་ལྟ་བུའོ། །

[Block 312]
ཉོན་མོངས་པའི་མགོ་ལྟུང་བར་བྱེད་པས་རལ་གྲི་ལྟ་བུའོ། །

[Block 313]
ཉོན་མོངས་པའི་ཤིང་གཅོད་པར་བྱེད་པས་སྟ་རེ་ལྟ་བུའོ། །

[Block 314]
འཚེ་བ་ཐམས་ཅད་ལས་སྐྱོབ་པས་མཚོན་ཆ་ལྟ་བུའོ། །

[Block 315]
འཁོར་བའི་ཆུ་བོའི་ནང་ནས་སྟེང་དུ་འབྱིན་པས་མཆིལ་པ་ལྟ་བུའོ། །

[Block 316]
སྒྲིབ་པས་ཁེབས་པ་ཐམས་ཅད་འཐོར་བར་བྱེད་པས༌[^146]རླུང་གི་དཀྱིལ་འཁོར་ལྟ་བུའོ། །

[Block 317]
བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་དང་སྨོན་ལམ་ཐམས་ཅད་མདོར་བསྡུས་པས་མདོར་བསྟན་པ་ལྟ་བུའོ། །

[Block 318]
ལྷ་དང་མི་དང་ལྷ་མ་ཡིན་དང་བཅས་པའི་འཇིག་རྟེན་ཐམས་ཅད་ལ་མཆོད་རྟེན་ལྟ་བུ་སྟེ། རིགས་ཀྱི་བུ་དེ་ལྟར་བྱང་ཆུབ་ཀྱི་སེམས་ནི་ཡོན་ཏན་དེ་དང་ཡོན་ཏན་གྱི་བྱེ་བྲག་ཚད་མེད་པ་གཞན་དང་ཡང་ལྡན་ནོ་ཞེས་གསུངས་ཏེ། དེ་བཞིན་དུ་རབ་ཏུ་བཤད་དོ། །

[Block 319]
དེ་བཞིན་དུ་ཁྱིམ་བདག་དཔའ་སྦྱིན་གྱིས༌[^147]ཞུས་པའི་མདོའི་ཚིག་འོག་ན་བཀོད་པ་ཡང་འདིར་དྲང་བར་བྱའོ། །

[Block 320]
གཞན་མདོ་དུ་མ་དང་། འཕགས་པ་ཀླུ་སྒྲུབ་དང་། སློབ་དཔོན་ཞི་བའི་ལྷ་ལ་སོགས་པས་ཀྱང་ཕན་ཡོན་མང་དུ་གསུངས་པ་ཡོད་ཀྱང་འདིར་ཡི་གེ་མངས་པའི་འཇིགས་པས་མ་བཀོད་དོ། །
--- END BLOCKS ---
