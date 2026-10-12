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
བསམ་པ་དང་ལྷག་པའི་བསམ་པ་གང་གིས༌[^215]བསྡུས། བསམ་པ་ནི་གཡོ་མེད་པ་དང་སྒྱུ་མེད་པས་བསྡུས་པའོ། །

[Block 387]
ལྷག་པའི་བསམ་པ་ནི་དེ་ལ་མ་ཆགས་པ་དང་ཁྱད་པར་དུ་འགྲོ་བས་བསྡུས་སོ། །

[Block 388]
བཞི་པོ་དེ་དག་གང་གིས་བསྡུས།[^216] ཆོས་བརྒྱད་ཀྱིས་བསྡུས་ཏེ། གཡོ་མེད་པ་ནི་དྲང་པོ་དང་གསལ་བས་བསྡུས་པའོ། །

[Block 389]
སྒྱུ་མེད་པ་ནི་བཅོས་མ་མ་ཡིན་པ་དང་བསམ་པ་དག་པས་བསྡུས་སོ། །

[Block 390]
དེ་ལ་མ་ཆགས་པ་ནི་སེམས་མ་གོང་བ་དང་བརྩོན་འགྲུས་མ་གོང་བས་བསྡུས་སོ། །

[Block 391]
ཁྱད་པར་དུ་འགྲོ་བ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱིས་བསྡུས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཆོས་བརྒྱ་ཉི་ཤུ་རྩ་བརྒྱད་ཀྱིས་བསྡུས་ཏེ་རྒྱས་པར་མདོ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 392]
གཞན་ཡང་འཕགས་པ་ཆོས་ཡང་དག་པར་སྡུད་པའི་མདོ་ལས་ཀྱང་འདི་སྐད་དུ། ཡོན་ཏན་ཁྱད་པར་ཅན་འདོད་པ་ནི་ལྷག་པའི་བསམ་པའོ། །

[Block 393]
ལྷག་པའི་བསམ་པ་ནི་སྲོག་ཆགས་འབྱུང་པོ་རྣམས་ལ་ངེས་པའོ། །

[Block 394]
སེམས་ཅན་ཐམས་ཅད་ལ་བྱམས་པའོ། །

[Block 395]
འཕགས་པ་ཐམས་ཅད་ལ་གུས་པའོ། །

[Block 396]
འཇིག་རྟེན་པ་རྣམས་ལ་སྙིང་བརྩེ་བའོ། །

[Block 397]
བླ་མ་ལ་རིམ་གྲོ་བྱེད་པའོ། །

[Block 398]
སྐྱབས་དང་དཔུང་གཉེན་དང་གླིང་མེད་པ་དང་མགོན་མེད་པའི་མགོན་དང་སྐྱབས་དང་དཔུང་གཉེན་དང་གླིང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། རྒྱ་ཆེར་དེ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 399]
གཞན་ཡང་མདོ་དེ་ལས་བྱང་ཆུབ་སེམས་དཔའ་བསམ་པ་དག་པ་ལ་ནི་ནམ་མཁའ་དང་རྩིག་པ་དང་ཤིང་དང་ཆུ་བོ་དང་ནགས་ཚལ་ལ་སོགས་པ་དག་ལས་ཀྱང་ཆོས་འབྱུང་ལ། རང་ཉིད་ཀྱི་སྤྱོད་པ་ཉིད་ལས་ཀྱང་གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་འབྱུང་ངོ་ཞེས་གསུངས་སོ། །

[Block 400]
གཞན་ཡང་འཕགས་པ་བློ་གྲོས་མི་ཟད་པའི་མདོ་ལས་ཀྱང་། བཙུན་པ་ཤ་ར་དྭ༌[^217]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ལྷག་པའི་བསམ་པ་མི་ཟད་པ་ཡིན་ཏེ། དེ་ཅིའི་ཕྱིར་ཞེ་ན། དགེ་བའི་རྩ་བ་ཐམས་ཅད་ལྷག་པར་དམིགས་པའི་ཕྱིར་རོ། །

[Block 401]
ཐ་ན་གང་བྱང་ཆུབ་སེམས་དཔའ་གང་ཅི་སེམས་པ་དེ་ཐམས་ཅད་དགེ་བའི་བསམ་པ་ལས་ལྷག་པའི་བསམ་པས་དམིགས་པར་འགྱུར་ཏེ། ས་ནས་སར་བཞག་པའི་ཕྱིར་འཕོ་བ་ནི་ལྷག་པའི་བསམ་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་། [^218]ཡང་བཙུན་པ་ཤ་ར་དྭ༌[^219]ཏིའི་བུ་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ལྷག་པའི་བསམ་པ་མི་ཟད་པའོ་ཞེས་གསུངས་སོ། །

[Block 402]
འདི་སྐད་དུ་བསྟན་པར་འགྱུར་ཏེ། འདི་ལྟར་ས་གཞི་བཟང་པོ་ལས་ནགས་ཚལ་དང་ལོ་ཏོག་ཕུན་སུམ་ཚོགས་པ་སྐྱེ་བ་བཞིན་དུ། ཚུལ་ཁྲིམས་བཟང་པོའི་ས་གཞི་ལས་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་སྐྱེ་ཞིང་འཕེལ་བར་འགྱུར་རོ་ཞེས་ཤེས་པར་འགྱུར་རོ། །

[Block 403]
འདིར་འདི་དཔྱད་དོ། །

[Block 404]
སྨོན་པ་བྱང་ཆུབ་ཀྱི་སེམས་དང་འཇུག་པ་བྱང་ཆུབ་ཀྱི་སེམས་དེ་གཉིས་ཀྱི་དོན་ལ། སྔོན་གྱི་མཁས་པ་ཆེན་པོ་རྣམས་དང་། ད་ལྟར་གྱི་མཁས་པ་ཆེན་པོ་དག་རྣམ་པ་དུ་མར་འཆད་དེ། དེ་དག་གི་འདོད་པ་དེ་དག་ལ་བདག་གི་བློ་འཕྲོ་བར་ནུས་མོད་ཀྱི་ཡི་གེ་མངས་པར་འགྱུར་བས་གཞག་གོ། །

[Block 405]
འདི་གཉིས་ཀྱི་དོན་མདོ་ཉིད་ན་གསལ་བར་གསུངས་ཏེ།

[Block 406]
སྡོང་པོ་བཀོད་པའི་མདོ་ལས།

[Block 407]
རིགས་ཀྱི་བུ་སེམས་ཅན་གང་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ༌[^220]དེ་དག་ཀྱང་དཀོན་ནོ། །

[Block 408]
དེ་བས་ཀྱང་གང་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ཆས་པའི་སེམས་ཅན་དེ་དག་ནི་ཤིན་ཏུ་དཀོན་ནོ་ཞེས་གསུངས་སོ། །

[Block 409]
སློབ་དཔོན་ཞི་བ་ལྷའི་ཞལ་ནས་ཀྱང་། བྱང་ཆུབ་ཀྱི་སེམས་དེ་ནི་རྣམ་པ་གཉིས་ཏེ། བྱང་ཆུབ་ཏུ་སྨོན་པའི་སེམས་དང་། བྱང་ཆུབ་ཏུ་འཇུག་པའི་སེམས་སོ་ཞེས་བསླབ་པ་ཀུན་ལས་བཏུས་པ་ལས་གསུངས་པ་དང་། སྤྱོད་འཇུག་ལས་ཀྱང་།

[Block 410 [VERSE]]
འགྲོ་བར༌[^221]འདོད་དང་འགྲོ་བ་ཡི། །
བྱེ་བྲག་ཇི་ལྟར་ཤེས་པ་ལྟར། །
དེ་བཞིན་མཁས་པས་འདི་ཉིད༌[^222]ཀྱི། །
བྱེ་བྲག་རིམ་བཞིན་ཤེས་པར་བྱ། །

[Block 411]
ཞེས་གསུངས་སོ། །

[Block 412]
ཡང་སློབ་དཔོན་གྱི་ཞལ་ནས། དེ་ལ་སྨོན་པའི་སེམས་ནི་ངས་སངས་རྒྱས་སུ་འགྱུར་བར་བྱའོ་ཞེས་སྨོན་པ་ལས་སྐྱེས་པའོ་ཞེས་བསླབ་པ་ཀུན་ལས་བཏུས་པ་ལས་གསུངས་སོ། །

[Block 413]
དེ་བས་ན་འབྲས་བུ་རྫོགས་པའི་བྱང་ཆུབ་ཡུལ་དུ་བྱེད་ཅིང་དམིགས་པ་ནི་སྨོན་པའི་སེམས་ཡིན་ཏེ། ཇི་སྐད་དུ་མགོན་པོ་བྱམས་པས་ཀྱང་།

[Block 414]
སེམས་བསྐྱེད་པ་ནི་གཞན་དོན་ཕྱིར། །ཡང་དག་རྫོགས་པའི་བྱང་ཆུབ་འདོད། །ཅེས་མངོན་པར་རྟོགས་པའི་རྒྱན་ལས་གསུངས་སོ། །

[Block 415]
ལམ་གྱི་ཆོས་ཡུལ་དུ་བྱེད་ཅིང་དམིགས་པ་ནི་འཇུག་པའི་སེམས་ཡིན་ཏེ། མགོན་པོ་བྱམས་པའི་ཞལ་ནས།

[Block 416 [VERSE]]
རང་གཞན་དོན་དང་དེ་ཉིད་དོན།[^223] །
མཐུ་དང་རང་གི༌[^224]སངས་རྒྱས་ཀྱི། །
ཞིང་དང་སེམས་ཅན་ཡོངས་སྨིན་དང་། །
བདུན་པ་བྱང་ཆུབ་མཆོག་ཡིན་ནོ། །

[Block 417]
ཞེས་མདོ་སྡེ་རྒྱན་ལས་གསུངས་སོ། །

[Block 418]
དེ་བས་ན་བྱང་ཆུབ་ཀྱི་སེམས་དེ་ཉིད་རྒྱུའི་དུས་དང་། འབྲས་བུའི་དུས་ཐམས་ཅད་དུ་དེ་ཉིད་ཡིན་ཏེ། གནས་སྐབས་ཀྱི་བྱེ་བྲག་གིས་དེ་ལྟར་འགྱུར་རོ། །

[Block 419]
དེ་ཡང་མགོན་པོ་བྱམས་པའི་ཞལ་ནས་རྒྱས་པར་བཤད་དེ། ཇི་སྐད་དུ།

[Block 420 [VERSE]]
དེ་ཡང་ས་གསེར་ཟླ་བ་མེ།[^225] །
གཏེར་དང་རིན་ཆེན་འབྱུང་གནས་མཚོ། །
རྡོ་རྗེ་རི་སྨན་བཤེས་གཉེན་དང་། །
ཡིད་བཞིན་ནོར་བུ་ཉི་མ་ཀླུ།[^226] །

[Block 421 [VERSE]]
རྒྱལ་པོ་མཛོད་དང་ལམ་པོ་ཆེ། །
བཞོན་པ་བཀོད་མའི་ཆུ་དང་ནི། །
སྒྲ་སྙན་ཆུ་བོ་སྤྲིན་རྣམས་ཀྱིས། །
རྣམ་པ་ཉི་ཤུ་རྩ་གཉིས་སོ། །

[Block 422]
ཞེས་གསུངས་སོ། །

[Block 423]
དེ་ལ་གཉིས་ནི་རྒྱུའི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 424]
བཅུ་བདུན་ནི་ལམ་གྱི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 425]
གསུམ༌[^227]ནི་འབྲས་བུའི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །
--- END BLOCKS ---
