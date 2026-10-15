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
[Block 421]
དེ་ལ་གལ་ཏེ་ཡང་འདི་ལ་ཆོས་ཉིད་མངོན་པར་ཤེས་པ་ཉིད་ཀྱི་ཕྱིར་དང་སྔོན་གྱི་གནས་ཤེས་པ་ཉིད་ཀྱིས་འཇུག་པ་ལ་ལྟ་བའི་ཕྱིར་དང་དཀའ་བ་ཆུང་ངུའི་རིག་པ་བསྟེན་པས་འོང་བ་ཕུན་སུམ་ཚོགས་པས་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པ་ཡོངས་སུ་ཤེས་པར་འགྲུབ་པར་འགྱུར་ཏེ། དེ་ལྟར་ན་ཡང༌[^284]ཡོངས་སུ་གདུལ་བར༌[^285]བྱ་བའི་དོན་དུ་གནས་ལ་གནས་པར་བྱའོ། །

[Block 422]
གང་གི་ཕྱིར་སྡུག་བསྔལ་བའི་ཐ་སྙད་ནི་འདུལ་བ༌[^286]ཉིད་དང་བཅས་པའི་དངོས་པོ་སྔོན་གྱི་རང་བཞིན་འཕྲོག༌[^287]པའི་ཕྱིར་རོ། །

[Block 423]
དགྲ་བཅོམ་པ་རྣམས་ལ་ནི་སྔོན་གྱི་རང་བཞིན་འཕྲོག་པ་ཐོས་པ་ཡིན་ཏེ། དགྲ་བཅོམ་པ་ལ་ལ་ཞིག་ནི་མཆོང་ཞིང་མཆོང་ཞིང་ཆུ་བོ་རྣམས་ལས་རྒལ་བར༌[^288]གྱུར་པ་དང་། ཚེ་དང་ལྡན་པ་པི་ལིན་དའི་བུས་གང་གཱའི་ལྷ་མོ་ལ་རླངས་མ་འདུག་ཤིག༌[^289]ཅེས་བྱ་བ་བརྗོད་པར་གྱུར་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 424]
གཞན་ཡང་འདིར་ནི་འདུལ་བ་ཡོངས་སུ་ཤེས་པར་ཅི་ནས་ཀྱང་བྱ་བ་མ་ཡིན་ཏེ། དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་དང་། མང་བ་དང་ཕྲ༌[^290]མོ་དང་། [^291]གཅིག་ན་མི་གནས་པ་ལྟ་བ་དང་འབད་པ་རྣམས་ལ་བར་ཆད་མང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 425]
གང་གི་ཕྱིར་གནས་སྐབས་ནི་རྣམ་པ་སྣ་ཚོགས་པ་ཡིན་ནོ། །

[Block 426]
འདི་ལྟ་སྟེ་བཙུན་པ་གལ་ཏེ་དེ་གསུམ་རིག་པ་ལོ་གསུམ་ལོན་པ་དྲི་མ་གསུམ་རབ་ཏུ་སྤངས་པ་ཡིན་ལ། དེ་ཡང་ཆོས་ལྔ་དང༌[^292]ཡང་དག་པར་ལྡན་པར་མ་གྱུར་ན་དེས་ཀྱང་མི་གནས་པ་ལ་ལྗོངས་རྒྱུ་ཞིང་མཆི་བར་མི་བགྱི་འམ། ཉེ་བ་འཁོར་མི་བྱའོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 427]
རིང་པོ་ནས་རིང་པོར་འདི་ནི་སྤོང་བར་མཛོད་ཅིག་ཅེས་བྱ་བ་ཡོངས་སུ་བཅས་པ་བསྒྲུབ་པའི་དོན་དུ་འདིས་འདུལ་བ་ལ༌[^293]གནས་པ་ཡང་བསྲུང་བར་བྱ་བ་སྟེ། གང་ཞིག་ལྷག་པར་སྤྱོད་པས་གཞན་དག་ལ་དང་བ་མ་ཡིན་པ་སྐྱེ་བར་འགྱུར་བ་དེ་ཡོངས་སུ་སྤང་བའི་དོན་དུ་བསླབ་པ་རྣམས་ལ་དོན་བྱས་པ་དང་འདི་ལ་གུས་པ་དང་ལྡན་པ་ཞེས་བྱ་བ་གུས་པ་བསྐྱེད་པའི་དོན་དང་། བསྟན་པ་གནས་པའི་དོན་དུ་གྲགས་པ་ཉིད་ལ་སོགས་པ་མི་འདའ་བར་འགྲོ་བར་འགྱུར་རོ། །

[Block 428]
གཞན་དུ་ན་གང་ཞིག༌[^294]འདས་པར་གྱུར་ན་བསྟན་པ་ཉམས་པ་གྲུབ་པ་ཡིན་ནོ། །

[Block 429]
དེ་བས་ན་འདིར་ཇི་ལྟར་གསུམ་རིག་པ་ཡང་མ་གནང་བ་བཞིན་དུ་གཞན་པ་ཡང་དེ་ཁོ་ན་བཞིན་ནོ། །

[Block 430]
གནས་པའི༌[^295]སྐབས་སོ།། །།

[Block 431]
རབ་ཏུ་འབྱུང་བའི་ཕྱིར་ཉེ་བར་འོངས་པ་ལ་མུ་སྟེགས་ཅན་མ་ཡིན་ནམ་ཞེས་དྲི་བར་བྱ་ཞིང་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དག་གིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། དྲི་བར་བྱ་ཞིང་ཞེས་བྱ་བས༌[^296]ནི་མཁན་པོས་སོ། །

[Block 432]
འདྲི་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ཡོངས་སུ་གྱུར་པ་ལ་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་འདི་དང་འབྲེལ་པའོ། །

[Block 433]
བསྙེན་པར་རྫོགས་པར་བྱེད་པ་རྣམས་ཁོ་ནས་དྲི་བ་འདི་ཡིན་ཏེ་གང་ཞིག་གསང་སྟེ་སྟོན་པས་དེ་ལ་དེ་ངེས་པར་སྦྱར་བའི་ཕྱིར་རོ། །

[Block 434]
ཤཱཀྱ་དང་མེ་པ་རལ་པ་ཅན་མ་གཏོགས་པ་སེམས་མགུ་བར་མ་གྱུར་པའི་མུ་སྟེགས་ཅན་རབ་ཏུ་དབྱུང་བ༌[^297]དང་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། ཤཱཀྱ་དང་མེ་པའི་རིགས་ཅན་དག་ལ་ངེས་པར་བཅོམ་ལྡན་འདས་ཀྱིས་ངེས་པར་འདི་དག་གིས་སྒྲུབ་པ་སྙིང་པོར་བྱེད་པ་ལ་བདེན་པར་བསྒྲུབ་པ་ཡིན་ཏེ། བཅོས་མས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཅུང་ཟད་བཟང་བ་སྐལ་བ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 435]
གང་དུ་འདི་གནང་བ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 436]
བདག་གིས་གཉེན་འདུན་རྣམས་ལ་གཉེན་ཉིད་ཡོངས་སུ་སྤང་བ་བདག་གིས་སྦྱིན་པར་བྱ་ཞེས་བྱ་བ་གང་ཞིག་གསུངས་པ་དེར་གཉེན་འདུན་ཉིད་མ་མཐོང་བ་འདི་རྣམས་ལ་བདེན་པར་བསྒྲུབ་པ་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བ་བཅོམ་ལྡན་འདས་ཀྱིས་མཁྱེན་པ་ཡིན་ཏེ། དེ་བས་ན་གཉེན་འདུན་གྱི་རྒྱུ་མཚན་ཡོངས་སུ་སྤང་བ་སྦྱིན་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 437]
འདིར་མེ་པ་ནི་བདེན་པར་མེའི་བསྙེན་བཀུར་བྱེད་པའི་ལས་ལ་འཇུག་པ་ཡིན་ཏེ། དེའི་བསམ་པ་ཡོངས་སུ་དག་པ་ལ་འཇུག་བཞིན་པ་བཟུང་བ་ཞེས་བྱ་བ་རིག་པར་བྱ་སྟེ། དེ་ལྟར་གྱུར་པ་ལ་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་མེད་མི་སྲིད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 438]
བཀོལ་བ་དེ་ནི་མུ་སྟེགས་ཅན་དང་ཤཱཀྱ་ལ་སོགས་པའི་མཇུག༌[^298]གི་མུ་སྟེགས་ཅན་བཀོལ་བའོ་ཞེས་བྱ་བ་ལ་མགུ་བར་མ་གྱུར་པའི་མུ་སྟེགས་ཅན་གྱི་མཐའ་ཅན་ལ༌[^299]གཏོགས་པ་སྟེ་ཞེས་བྱ་བའི་སྒྲ་ལས་ཐོག་མར་མུ་སྟེགས་ཅན་གྱི་སྒྲ་སྤངས་ནས་སེམས་མགུ་བར་མ་གྱུར་པ་སྤངས་ཏེ། ཤཱཀྱ་དང་མེ་པ་རལ་པ་ཅན་མུ་སྟེགས་པ་ཞེས་བྱ་བ་འདི་ནི་མགུ་བར་མ་གྱུར་པའི་སྒྲ་དང་པོ་མུ་སྟེགས་ཅན་གྱི་སྒྲའི་ཐ་མར་སྤངས་ཏེ། གང་ཞིག་འདི་ཁྱོད་མ་ཡིན་ནམ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་འདི་ནི་མིང་དུ་བཏགས་པར་རིག་པར་བྱའོ། །

[Block 439]
གང་དུ་བཀོལ་བ་ཞེས་བྱ་བ་བརྗོད་པ་དེར་ཁྱོད་ནི་མ་ཡིན་ནམ་ཞེས་བྱ་བ་རབ་ཏུ་འབྱུང་བའི་ཕྱིར་ཉེ་བར་འོངས་པ་ལ་ཁྱོད་མུ་སྟེགས་ཅན་མ་ཡིན་ནམ་ཞེས་དྲི་བར་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་པོ་རྣམས་ཀྱིས་ཀྱང་རབ་ཏུ་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་འདི༌[^300]བརྗོད་པར་རྟོགས་པར་བྱའོ། །

[Block 440]
འདི་ནས་བརྩམས་ཏེ་འདི་ཉིད་ལ་རབ་ཏུ་བྱུང་བའི༌[^301]གཞི་དང༌[^302]ཕྲན༌[^303]ཚེགས༌[^304]ལ་བརྟེན་པ་རྣམས་ལ་ཕྱོགས་བྱས་པ་རྣམས་སོ། །

[Block 441]
སེམས་མགུ་བར་གྱུར་པ་རྣམས་ཀྱིས་ཇི་ཙམ་གྱིས་མུ་སྟེགས་ཅན་བརྗོད་པར་བྱ་ཞེས་བྱ་བ་མ་ལུས་པ་ཤེས་པའི་དོན་དུ། དཀོན་མཆོག་རྣམས་ཀྱི་བསྔགས་པ་དང་། མུ་སྟེགས་ཅན་རྣམས་ཀྱི་བསྔགས་པ་མ་ཡིན་པ་ཡང་དག་པར་བརྗོད་པ་ནི༌[^305]མི་གཡོ་བ་ཉིད་ནི་སེམས་མགུ་བར་གྱུར་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྲོ་བར་མི་བྱེད་པས་ན་མི་གཡོ་བ་སྟེ། མི་གཡོ་བའི་དངོས་པོ་ནི་མི་གཡོ་བ་ཉིད་དོ། །

[Block 442]
དེའི་དོན་དུ་དེ་དང་མི་ལྡན་པ་དེ་དགེ་བསྙེན་ཉིད་དུ་བྱས་པའི་མཐའ་ཅན་དེ་ལ་དགེ་འདུན་གྱི་ལས་ཀྱིས་གནས་པ་བྱིན་ལ་ཟླ་བ་བཞིར་གནས་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་དོན་དུ་ཞེས་བྱ་བ་ནི་སེམས་མགུ་བར་གྱུར་པ་ཉིད་ཀྱི་དོན་དུའོ། །

[Block 443]
དེ་དང་མི་ལྡན་པ་ཞེས་བྱ་བ་ནི་སེམས་མགུ་བར་གྱུར་པ་དང་ལྡན་པའོ། །

[Block 444]
དེ་ཞེས་བྱ་བ་ནི་མུ་སྟེགས་ཅན་ནོ། །

[Block 445]
དགེ་བསྙེན་ཉིད་དུ་བྱས་པའི་མཐའ་ཅན་ཞེས་བྱ་བ་ནི་དགེ་བསྙེན་ཉིད་དུ་བྱས་པའི་མཐའ་ཅན་གྱི་ཆོ་ག་འདི་ལ་བྱས་པས་ན་དགེ་བསྙེན་ཉིད༌[^306]དུ་བྱས་པའི་མཐའ་ཅན་ནོ། །

[Block 446]
དེ་ལྟར་གྱུར་པ་དེ་ལ་གསོལ་བ་དང་བཞིའི་ལས་ཀྱིས༌[^307]དགེ་འདུན་གྱིས་གནས་པ༌[^308]བྱིན༌[^309]ལ་ཟླ་བ་བཞིར་གནས་པར་བྱའོ། །

[Block 447]
གནས་པ་བྱིན་པ་ལ། དེའི་ཟན་ནི་དགེ་འདུན་ལས་སོ། །

[Block 448]
གོས་ནི་མཁན་པོ་ལས་སོ། །

[Block 449]
ལས་སུ་བསྐོ་བ་ནི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 450]
རབ་ཏུ་བྱུང་བའི་ཕྱིར་ཉེ་བར་འོངས་པ་ལ་ལོ་བཅོ་ལྔ་ལོན་ནམ་ཞེས་དྲི་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མཁན་པོས་སོ། །

[Block 451]
མ༌[^310]ལོན་པ་བྱ་རོག་སྐྲོད་མི་ནུས་པ་དང་། ནུས་པ་ལོ་བདུན་མ་ལོན་པ་རབ་ཏུ་དབྱུང་བར༌[^311]མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལོ་བཅོ་ལྔ་མ་ལོན་པ་མི་ནུས་པ་དང་ལོ་བདུན་མ་ལོན་པ་ནུས་པ་གཉིས་པོ་འདི་དག་རབ་ཏུ་འབྱུང་བར༌[^312]མི་བྱའོ་ཞེས་བྱ་བ་མང་པོའི་ཚིག་ཅིའི་དོན་དུ་ཡིན་ཞེ་ན། ཞུ་བ་པོས་འདི་ནི་མ་དག་གོ་ཞེས་བྱ་བར་ཤེས་ནས་ཞུ་བར་བྱ་བ་མ་ཡིན་ལ། དགེ་འདུན་གྱིས་གནང་བར་བྱ་བ་མ་ཡིན་ཏེ། དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་ཐོབ་པའི་དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་བསྒྲུབ་པར་བྱ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཉེ་བར་བསྡུ་བའི་དོན་དུའོ། །

[Block 452]
དགེ་ཚུལ་གཅིག་ལས་ལྷག་པ་ཉེ་བར་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་ཚུལ་གཉིས་ལས་ལྷག་པར༌[^313]ཉེ་བར་གཞག་པ་མ་ཡིན་པ་ལ་གཉིས་པ་ལ་རབ་ཏུ་བྱུང་བ་ལ་ཡང་ཐལ་བ་དེ་བསལ་བའི༌[^314]དོན་དུ། གལ་ཏེ་སོ་སོར་རབ་ཏུ་འབྱུང་བར་མི་འདོད་ན་རབ་ཏུ་བྱུང༌[^315]ལ་རྒན་པ་བསྙེན་པར་རྫོགས་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཉིས་ཀ་རབ་ཏུ་དབྱུང་བའི་དོན་དུ་བདག་ཅག་གིས་གནས་གཅིག་ཏུ་རབ་ཏུ་འབྱུང་བར༌[^316]བྱའོ་ཞེས་བྱ་བ་འདི་ལྟར་ངེས་ནས་འོངས་པ་དག་ལ་གལ་ཏེ་སོ་སོ་ནི་སོ་སོར་རབ་ཏུ་དབྱུང་བར་མི་འདོད་ན་དེ་ནས་གཉིས་ཀ་རབ་ཏུ་ཕྱུང་ནས་གཅིག་ལས་ལྷག་མར་གྱུར་པ་བསྙེན་པར་རྫོགས་པར་བྱའོ། །

[Block 453]
གལ་ཏེ་མ་ལོན་ན་གཞན་ལ་རེ་ཞིག་གནས་པའི་དོན་དུ་གཏད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ལོ་ཉི་ཤུ་མ་ལོན་ན་དེ་ནས་དགེ་སློང་གཞན་ལ་ཉེ་བར་གནས་པའི་དོན་དུ་གཏད་པར་བྱའོ། །

[Block 454]
ཉེ་བར་གནས་པའི་དོན་དུ་གང་ལ་གཏད་པ་དེས༌[^317]ནི་དེ་དབྲོག་པར་མི་བྱའོ་ཞེས་བྱ་སྟེ། གང་ཞིག་གཏད་པ་དེས་འདི་ལ་བསྙེན་པར་རྫོགས་པར་བྱའོ། །

[Block 455]
མི་སྟེར་བ་ལ་མཐུས་བཀུག་སྟེའོ་ཞེས་བྱ་བ་ལ་གང་གི་ཕྱིར་ཆོ་ག་འདིའི་དོན་དུ་གཞན་ལ་ཉེ་བར་གནས་པས་སྦྱིན་པ་སྟེ་ཐམས་ཅད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 456]
དེ་བས་ན་དབྲོག་པ་མ་ཡིན་ནོ། །

[Block 457]
བཀོལ་བ་བྲན་ནོ་ཞེས་བྱ་བ་ནི་བཀོལ་བ་ཞེས་བྱ་བའི་མིང་འདིས་ཁྱོད་བྲན་མ་ཡིན་ནམ་ཞེས་བྱ་བ་ལ་སོགས་པའི་མིང་ཅན་བྲན་དང་འབྲེལ་བ་ལ་སོ་སོར་ཉེ་བར་གཞག་པའོ། །

[Block 458]
དེ་བས་ན་མིང་བསྟན་པ་འདི་ལ་གང་ཞིག་ལྡན་པ་ཁས་ལེན་པར་བྱེད་པ་དེ་དོན་ཇི་ལྟར་ཡོངས་སུ་གྱུར་ཀྱང་གནས་ཇི་ལྟ་བར་ཡང་དག་པར་གནས་པ་ཡིན་ནོ། །

[Block 459]
འདིར་ནི་ངག་ཀྱང་འདི་བསྐྱེད་པ༌[^318]ཡིན་ཏེ། ཁྱོད་ནི་བྲན་མ་ཡིན་ནམ་ཞེས་བྱ་བར༌[^319]རབ་ཏུ་འབྱུང་བའི༌[^320]དོན་དུ་ཉེ་བར་འོངས་པ་ལ་དྲི་བར་བྱའོ། །

[Block 460]
བསྙེན་པར་རྫོགས་པར་བྱེད་པ་རྣམས་ཀྱང་བྲན་ལས་རབ་ཏུ་དབྱུང་བ་མ་ཡིན་པ་དང་བསྙེན་པར་རྫོགས་པར་བྱ་བ་མ་ཡིན་པ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
