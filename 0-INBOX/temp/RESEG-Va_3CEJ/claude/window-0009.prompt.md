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
ཕྲ་བ་ནི་ཡིད་ལས་བྱུང་བའོ། །

[Block 317]
ཡང་ན་ས་ལས་རིག་པར་བྱའོ་ཞེས་སོ། །

[Block 318]
བཙུན་པ་ན་རེ་ནི་གཟུགས་རགས་པ་ནི་དབང་པོ་ལྔས་གཟུང་བར་བྱ་བའོ། །

[Block 319]
གཞན་ནི་ཕྲ་བའོ། །

[Block 320]
ངན་པ་ནི་ཡིད་དུ་མི་འོང་བའོ། །

[Block 321]
གྱ་ནོམ་པ་ནི་ཡིད་དུ་འོང་བའོ། །

[Block 322]
རིང་བ་ནི་ཡུལ་མི་སྣང་བ་ཅན་ནོ། །

[Block 323]
ཉེ་བ་ནི་ཡུལ་སྣང་བ་ཅན་ནོ། །

[Block 324]
འདས་པ་ལ་སོགས་པ་ནི་རང་གི་མིང་གིས་བསྟན་པའི་ཕྱིར་ཏེ། ཚོར་བ་ལ་སོགས་པ་ཡང་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 325]
དེ་དག་གིས་རིང་བ་དང་ཉེ་བ་ཉིད་ནི་དེ༌[^124]རྟེན་གྱི་དབང་གིས་སོ། །

[Block 326]
རགས་པ་དང་ཕྲ་བ་ཉིད་ནི་སྔ་མ་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 327 [HEADING]]
#### སྐྱེ་མཆེད་ཀྱི་དོན། ^1-2-2-0

[Block 328]
སེམས་དང་སེམས་ལས༌[^125]བྱུང་བ་རྣམས་སྐྱེ་བའི་སྒོའི་དོན་ནི་སྐྱེ་མཆེད་ཀྱི་དོན་ཏེ། ངེས་པའི་ཚིག་ཏུ་ན་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་སྐྱེ་བ་མཆེད་པར་བྱེད་པས་སྐྱེ་མཆེད་རྣམས་ཏེ། རྒྱས་པར་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 329 [HEADING]]
#### ཁམས་ཀྱི་དོན། ^1-2-3-0

[Block 330]
རིགས་ཀྱི་དོན་ནི་ཁམས་ཀྱི་དོན་ཏེ། དཔེར་ན་རི༌[^126]འགའ་ཞིག་ལ་ལྕགས་དང་ཟངས་དང་དངུལ་དང་གསེར་ལ་སོགས་པ་རིགས་མང་པོ་དག་ཡོད་པ་ལ་ཁམས་ཞེས་བརྗོད་པ་དེ་བཞིན་དུ་རྟེན་དང་རྒྱུད་གཅིག་ལ་རིགས་བཅོ་བརྒྱད་དག་ཡོད་པ་ལ་ཁམས་བཅོ་བརྒྱད་ཅེས་བྱའོ། །

[Block 331]
དེ་ལ་འབྱུང་གནས་དག་ནི་རིགས་ཞེས་བྱ་བ་ནི༌[^127]མིག་ལ་སོགས་པ་འདི་དག་གང་གི་འབྱུང་གནས་ཡིན་ཞེ་ན། རང་གི་རིགས་ཀྱི་ཡིན་ཏེ། སྐལ་བ༌[^128]མཉམ་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 332]
འདུས་མ་བྱས་ཁམས་མ་ཡིན་པར་འགྱུར་རོ་ཞེ་ན། འོ་ན་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས༌[^129]ཡིན་ནོ། །

[Block 333]
གཞན་དག་ན་རེ་ཆོས་བཅོ་བརྒྱད་པོ་དག༌[^130]རིགས་ཀྱི་རང་བཞིན་ནོ་ཞེ་ན།[^131] ཁམས་བཅོ་བརྒྱད་ཅེས་བྱ་བས་ཁམས་ཞེས་བྱ་བའི་སྒྲ་འདི་ནི་རིགས་ཀྱི་ཚིག་ཡིན༌[^132]ཞེས་ཟེར་རོ། །

[Block 334 [HEADING]]
#### ཕུང་པོ་རྣམས་ཀྱི་རྣམ་པ་གཞན། ^1-2-4-0

[Block 335 [HEADING]]
##### ཕུང་པོ་རྣམས་བཏགས་པའི་ཡོད་པ། ^1-2-4-1-0

[Block 336]
གལ་ཏེ་སྤུངས་པའི་དོན་ཕུང་པོའི་དོན་ཡིན་ན༌[^133]ཕུང་པོ་རྣམས་བཏགས་པའི༌[^134]ཡོད་པར་འགྱུར་ཏེ། རྫས་སུ༌[^135]མ་འདུས་པ་ཡིན་པའི་ཕྱིར་སྤུངས་པ་དང་གང་ཟག་བཞིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། རྫས་ཀྱི་རྡུལ་ཕྲ་རབ་གཅིག་པུ་ཡང་ཕུང་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 337]
དེ་ལྟ་ན་གཅིག་པུ་ལ་སྤུངས་པ་ཉིད་མེད་པས་སྤུངས་པའི་དོན་ནི་ཕུང་པོའི་དོན་ཏོ་ཞེས་བརྗོད་པར་མི་བྱའོ། །

[Block 338]
གཞན་དག་ན་རེ། བྱ་བའི་ཁུར་ཁྱེར་བའི་དོན་ནམ། ཡོངས་སུ་ཆད་པའི་དོན་ནི་ཕུང་པོའི་དོན་ཏེ། འདི་ལྟར་སྨྲ་བ་པོ་དབུལ་བར་བྱ་བའི་ཕུང་པོ་གསུམ་དག་ཏུ་དབུལ་བར་བྱའོ་ཞེས་སྨྲ་བ་བཞིན་ནོ་ཞེས་ཟེར་ཏེ། དེ་ནི་མདོ་དང་འགལ་ལོ། །

[Block 339]
མདོ་ལས་ནི་སྤུངས་པའི་དོན་ཁོ་ནར་གསུངས་ཏེ། གཟུགས་གང་ཅི་ཡང་རུང་བ་འདས་པའམ། མ་འོངས་པའམ་ཞེས་རྒྱས་པར་གསུངས་སོ། །

[Block 340]
དེར་ནི་གཟུགས་འདས་པ་ལ་སོགས་པ༌[^136]སོ་སོར་ཕུང་པོ་ཉིད་ཡིན་པར་ཤེས་ཏེ། གཟུགས་འདས་པ་ལ་སོགས་པ་འདི་ཐམས་ཅད་རེ་རེ་ཞིང་གཟུགས་ཀྱི་ཕུང་པོ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟར་ནི་ཤེས་པར་མི་ནུས་ཏེ། དེ་ཐམས་ཅད་གཅིག་ཏུ་བསྡུས་ནས་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 341]
དེ་ལྟ་བས་ན་གཟུགས་ཀྱི་ཕུང་པོ་དག་ནི་སྤུངས་པ་བཞིན་དུ་བཏགས་པའི་ཡོད་པ་ཡིན་ནོ། །

[Block 342]
དེ་ལྟ་ན་སྐྱེ་མཆེད་གཟུགས་ཅན་རྣམས་ཀྱང་བཏགས་པའི་ཡོད་པར་འགྱུར་ཏེ། མིག་ལ་སོགས་པའི་རྡུལ་ཕྲ་རབ་མང་པོ་ནི་སྐྱེ་བའི་སྒོར་གྱུར་པའི་ཕྱིར་རོ་ཞེ་ན། མ་ཡིན་ཏེ་ཚོགས་པ་རྣམས་རེ་རེ་ནས་རྒྱུའི་ངོ་བོར་གྱུར་པའི་ཕྱིར་རམ། ཡུལ་ལྷན་ཅིག་བྱེད་པ་ཡིན་པའི་ཕྱིར་དབང་པོ་ལས༌[^137]ལོགས་ཤིག་ཏུ་སྐྱེ་མཆེད་དུ་ཡང་མི་འགྱུར་རོ། །

[Block 343]
བྱེ་བྲག་ཏུ་བཤད་པ་ཆེན་པོ༌[^138]ལས་ནི། གལ་ཏེ་ཆོས་མངོན་པ་པ་ཞིག་ཕུང་པོ་བཏགས་པའི་ཡོད་པར་ལྟ་ན་ནི་དེ་རྡུལ་ཕྲ་རབ་ཁམས་གཅིག་དང་། སྐྱེ་མཆེད་གཅིག་དང་། ཕུང་པོ་གཅིག་གི་ཕྱོགས་ཡིན་ནོ་ཞེས་སྨྲའོ། །

[Block 344]
འོན་ཏེ་མི་ལྟ་ན་ནི་དེ༌[^139]རྡུལ་ཕྲ་རབ་ཁམས་གཅིག་དང་། སྐྱེ་མཆེད་གཅིག་དང་། ཕུང་པོ་གཅིག་ཡིན་ནོ་ཞེས་སྨྲའོ་ཞེས་འབྱུང་ངོ་། །ཕྱོགས་ཡིན་ཡང་ཕྱོགས་ཅན་ཡིན༌[^140]བཞིན་དུ་ཉེ་བར་འདོགས་པ་ཡང་ཡོད་དེ། དཔེར་ན་རས་ཡུག་གི་ཕྱོགས་གཅིག་ཚིག་པ་ལ་རས་ཡུག་ཚིག་གི༌[^141]ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 345 [HEADING]]
##### ཕུང་པོ་ལ་སོགས་གསུམ་བསྟན་པ། ^1-2-4-2-0

[Block 346]
ཡང་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས༌[^142]ཕུང་པོ་ལ་སོགས་པའི་སྒོ་ནས་སྟོན་པ་རྣམ་པ་གསུམ་རྩོམ་པར་མཛད་ཅེ་ན། སྨྲས་པ། གདུལ་བ་རྣམས་ཀྱི། །

[Block 347 [VERSE]]
རྨོངས་དབང་འདོད་རྣམས་གསུམ་གྱི་ཕྱིར། །
ཕུང་པོ་ལ་སོགས་གསུམ་བསྟན་ཏོ། །
རྣམ་པ་གསུམ་ནི་རྣམ་གསུམ་མོ། །

[Block 348]
སེམས་ཅན་རྣམས་ཀྱི་རྨོངས་པ་ནི་རྣམ་པ་གསུམ་སྟེ། ཁ་ཅིག་ནི་སེམས་ལས་བྱུང་བ་རྣམས་ལ་རིལ་པོའི་བདག་ཉིད་དུ་འཛིན་པས་རྨོངས་སོ། །

[Block 349]
ཁ་ཅིག་ནི་གཟུགས་ཁོ་ན་ལའོ། །

[Block 350]
ཁ༌[^143]ཅིག་ནི་གཟུགས་དང་སེམས་དག་ལའོ། །

[Block 351]
དབང་པོ་དག་ཀྱང་རྣམ་པ་གསུམ་སྟེ། དབང་པོ་རྣོན་པོ་དང་། འབྲིང་དང་། རྟུལ་པོའི་ཕྱིར་རོ། །

[Block 352]
འདོད་པ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཚིག་བསྡུས་པ་དང་། བར་མ་དང་། རྒྱ་ཆེན་པོ་འདོད་པའི་ཕྱིར་ཏེ། དེ་དག་ལ་གོ་རིམས་བཞིན་དུ་ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་དང་གསུམ་བསྟན་ཏོ༌[^144]ཞེས་གྲག་གོ། །

[Block 353 [HEADING]]
##### ཚོར་བ་དང་འདུ་ཤེས་ལོགས་ཤིག་ཕུང་པོར་བཞག་པ། ^1-2-4-3-0

[Block 354]
ཡང་ཅིའི་ཕྱིར་སེམས་ལས་བྱུང་བ་གཞན་རྣམས་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོ་གཅིག་ཏུ་བསྡུས་ལ་འདུ་ཤེས་དང་ཚོར་བ་དག་ནི་ལོགས་ཤིག་ཏུ་ཕུང་པོར་བྱས་ཤེ་ན། སྨྲས་པ།

[Block 355 [VERSE]]
རྩོད་པའི་རྩ་བར་གྱུར་པ་དང་། །
འཁོར་བའི་རྒྱུ་ཕྱིར་རིམ་རྒྱུའི་ཕྱིར། །
སེམས་བྱུང་རྣམས་ལས་ཚོར་བ་དང་། །
འདུ་ཤེས་ལོགས་ཤིག་ཕུང་པོར་བཞག །
--- END BLOCKS ---
