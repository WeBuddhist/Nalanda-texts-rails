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
[Block 36]
རིགས་པའི་སྟོབས་ཀྱིས༌[^31]འདིའི་དོན་ནི་གང་ཞིག་འཇིག་རྟེན་གྱི་ཐ་སྙད་ལ་ཀུན་རྫོབ་ཀྱི་སྒྲས་བརྗོད་ལ། དེ་ནི་འདི་ལྟར་གང་འཇིག་རྟེན་གྱི་ཐ་སྙད་འདི་ནི་འཇིག་རྟེན་ཀུན་རྫོབ་སྟེ། དེ་ནི་དེ་ཁོ་ན་ཉིད་མ་ཡིན་ནོ་ཞེས་འཕགས་པ་ཁོ་ན་གསུངས་པར༌[^32]རིགས་ལ། ཐ་སྙད་དང་ཀུན་རྫོབ་ཀྱི་སྒྲ་དག་ཀྱང་རྣམ་གྲངས་ཉིད་དེ། དེ་ལ་སྐྱོན་མེད་དོ། །

[Block 37]
དེ་སྐད་དུ་མདོ་ལས།

[Block 38]
ཀུན་རྫོབ་ཀྱི་བདེན་པ་གང་ཞེ་ན། ཇི་སྲིད་དུ་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཡི་གེ་དང་སྐད་ཀྱིས་སྟོན་པའོ། །ཞེས་སོ། །

[Block 39]
ཡང་ན་ཅི་ཞིག་ལ་འདིར་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཅེས༌[^33]བྱ་ཞེ་ན། དེ་ལ་རེ་ཞིག་བུད་ཤིང་ལ་བརྟེན་ནས་མེ་བཞིན་དུ་ཕུང་པོ་ལ་བརྟེན་ནས་བརྟགས་པའི་གང་ཟག་ལ་འཇིག་རྟེན་ཞེས་བརྗོད་དོ། །

[Block 40]
དེ་ཡང་ཕྱིན་ཅི་ལོག་དང་ཕྱིན་ཅི་མ་ལོག་པ་ཉིད་ཀྱིས༌[^34]རྣམ་པ་གཉིས་སོ། །

[Block 41]
དེ་ལ་དབང་པོ་ཉམས་པའི་རབ་རིབ་ཅན་ལ་སོགས་པ་ཕྱིན་ཅི་ལོག་ཡིན་ལ། ཕྱིན་ཅི་མ་ལོག་པ་ནི་དབང་པོ་མ་ཉམས་པ༌[^35]རབ་རིབ་ཅན་ལ་སོགས་པ་ལས་གཞན་པའོ། །

[Block 42]
འདི་ཉིད་ཁོ་ན་ཡང་འདིར་འཇིག་རྟེན་པའི་སྒྲས་བརྗོད་ཀྱི། ཅིག་ཤོས་ནི་མ་ཡིན་ཏེ། འཇིག་རྟེན་པ་ཁོ་ན་ལ་རྣམ་པ་ཚད་མ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 43]
འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་གསུངས་པ་ཡང་གཞན་གྱི་ཁོང་དུ་ཆུད་པར་འདོད་པའི་དངོས་པོ་ཀུན་ནས་རྟོགས་པའི་དངོས་པོ་སྣ་ཚོགས་པ་གཞན་གྱི་རྒྱུད་ལ་རྟོག་པ༌[^36]འཇུག་པར་བྱེད་པ་ལ་ཐ་སྙད་ཅེས་བརྗོད་དོ། །

[Block 44]
འཇིག་རྟེན་པའི་ཐ་སྙད་ནི་འཇིག་རྟེན་ཐ་སྙད་དེ། ཇི་ལྟར་འཇིག་རྟེན་པ་རྟོགས་པར་འདོད་པའི་དོན་ཕན་ཚུན་དུ་རྟོགས་པར་བྱེད་པའམ། ཤེས་པར་འདོད་པའི་དོན་ཁོང་དུ་ཆུད་པའོ། །

[Block 45]
དེ་བཞིན་དུ་དོན་དེ་ལ་བརྗོད་བྱ་རྗོད་བྱེད་ཀྱི༌[^37]འབྲེལ་པ་དང་། ཤེས་བྱ་ཤེས་བྱེད་དུ་རྣམ་པར་འཇོག་པར་བྱེད་ཅིང་། དུས་གཞན་དུ་ཡང་ཐ་སྙད་ཀྱི་གདམས་པ་མི་འཆད་པའི༌[^38]དོན་དུ་དེ་ལ་འདི་ལྟར༌[^39]རྗོད་བྱེད་དང་བརྗོད་བྱ་དང་། ཤེས་པ་དང་ཤེས་བྱའི་མཚན་ཉིད་ཅན་གྱི་དོན་ཕྱིན་ཅི་ལོག་ཙམ་གྱིས་ཉེ་བར་བསྐྱེད་པའི་བདག་ཉིད་ཀྱི་དངོས་པོ་ལ་ཐ་སྙད་ཅེས་བརྗོད་ཀྱི། བྱེད་པ་པོའི་ཚོགས་པ་གཅིག་དང་འབྲེལ་པ་ནི་མ་ཡིན་ནོ། །

[Block 46]
དེ་ཉིད་ཀྱང་འཇིག་རྟེན་པ་བདེན་པར་འདོད་པའི་ཕྱིར་འཇིག་རྟེན་པའི་ཐ་སྙད་ཀྱི་བདེན་པ་ཞེས་བྱ་སྟེ་གཅིག་གོ། །

[Block 47]
རེ་ཞིག་འདི་དག་འཇིག་རྟེན༌[^40]པ་ཕྱིན་ཅི་ལོག་གི་ཤེས་པའི་དབང་ལས་བདེན་པ་ལ། ཕྱིན་ཅི་མ་ལོག་པའི་དབང་ལས་དོན་དམ་པའི་བདེན་པ་རྣམ་པར་གཞག༌[^41]གོ། །

[Block 48]
སླར་ཡང་ཅི་དེ་ཕྱིན་ཅི་མ་ལོག་པའི་ཤེས་པ་ཡིན། གང་དུ་ཡང་དག་པ་མ་ཡིན་པས་སྒྲོ་འདོགས་པར་མི་བྱེད་པའོ། །

[Block 49]
ཡང་ཅི་ཡང་དག་པ་མ་ཡིན་པས༌[^42]སྒྲོ་འདོགས་པར་མི་བྱེད་པ་ཡིན། དེ་ནི་ཇི་ལྟར་གནས་པའི་ཆོས་ཀྱི་རང་བཞིན་ལ་དམིགས་པའོ། །

[Block 50]
སླར་ཡང་ཅི་འདི་ནི་ཆོས་རྣམས་ཀྱི་ཡང་དག་པ་ཇི་ལྟ་བར་གནས་པའི་རང་བཞིན་ཡིན། མ་བྱས་པའོ། །

[Block 51]
ཡང་ཅི་མ་བྱས་པ་ཡིན། རྒྱུ་དང་རྐྱེན་གྱིས་མ་བསྐྱེད་པའོ། །

[Block 52]
འདི་ནི་བརྡར་བཏགས་པའི་མིང་ཡིན་ནམ་ཅི་མ་ཡིན་ཏེ། འཇིག་རྟེན་པ་ཡང་མ་བྱས་པ་ཉིད་ལ་རང་བཞིན་ཞེས་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 53]
འདི་ལྟར་འཇིག་རྟེན་པ་འགའ་ཞིག་འགའ་ཞིག༌[^43]ཏུ་བསླུ་བའི་ཐ་སྙད་དམིགས་པ་ན་འདིའི་ཐ་སྙད་འདི་ནི་བྱས་པ་སྟེ། རང་བཞིན་མ་ཡིན་པའོ་ཞེས་སྨྲ་བའོ། །

[Block 54]
དེ་བཞིན་དུ་སྒྱུ་མའི་སྐྱེས་བུ་དམིགས་པ་ན་སྐྱེས་བུ་འདི་ནི་བྱས་པའོ་ཞེས་བརྗོད་དེ། རང་བཞིན་མ་ཡིན་པ་ཞེས་བྱའོ། །

[Block 55]
དེ་བཞིན་དུ་འཇིག་རྟེན་དུ་རང་བཞིན་ཞེས་བྱ་བ་མ་བྱས་པ་ལ་བརྗོད༌[^44]དོ། །

[Block 56]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཕྱིར་བྱས་པ་ཉིད་དུ་ཡོད་པའི་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པའི་དོན་ཀྱང་བསླུ་བར་སོ་སོར་སྣང་བའོ་ཞེས་བྱ་སྟེ། གང་ཞིག་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པ་འདི་དག་ཉེ་བར་དམིགས་པའི་རང་བཞིན་དེ་ནི་བྱས་པ་སྟེ། བྱས་པའི་ཕྱིར་རང་བཞིན་དུ་མི་འགྱུར་རོ། །

[Block 57]
དེ་ལྟ་ན་ཡང་བྱས་པའི་རང་བཞིན་དུ་ཞོག་ཤིག༌[^45]ཅེ་ན། དེ་ནི་དེ་ལྟར་མ་ཡིན་ཏེ། དངོས་པོ་བྱས་པ་མ་ཡིན་པ་མེད་ལ་གང་ཞིག་གི་རང་བཞིན་ནོ་ཞེས་པའི་མིང་ཡིན་པར་འགྱུར་ན། ཇི་ལྟར་གནས་པའི་རང་བཞིན་དུ་ཕྱིན་ཅི་མ་ལོག་པའི་ཤེས་པས་དམིགས་པར་འགྱུར་གྲང་ན། དེ་ཡང་མེད་ལ། དེ་མེད་ན་ཡུལ་མེད་པས་ཤེས་པ་སྐྱེ་བ་མེད་དོ་ཞེས་བྱ་སྟེ། ཅིའི་ཕྱིར་ཡང་དག་པའི་དོན་དུ་སྒྲོ་འདོགས། གང་ཡང་འདི་ནི༌[^46]ཡང་དག་པའི་སྒྲོ༌[^47]བཏགས་པ་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ལ་ལྟོས་ཏེ། འཇིག་རྟེན་གྱི་ཐ་སྙད་ལ་བརྟེན་ནས་དོན་དམ་པའི་བདེན་པ་ཞེས་བརྗོད་ལ། དེ་ཡང་མཚན་མ་མེད་པའི་ཕྱིར་བརྗོད་བྱ་རྗོད་བྱེད་དང་ཤེས་བྱ་ཤེས་བྱེད་ཀྱི་ཐ་སྙད་མེད་དོ། །

[Block 58]
ཇི་སྐད་དུ་མདོ་ལས།

[Block 59]
དོན་དམ་པའི་བདེན་པ་གང་ཞེ་ན། གང་ལ་སེམས་ཀྱི་རྒྱུ་བ་ཡང་མེད་ན་ཡི་གེ་རྣམས་ལྟ་ཅི་སྨོས་ཞེས་སོ། །

[Block 60]
དེ་ལྟར་བདེན་པ་གཉིས་རྣམ་པར་གཞག་པ་ལ། གལ་ཏེ་དོན་དམ་པའི་བདེན་པ་བསྟན་པའི་དབང་དུ་བྱས་ནས་གནས་པ་ལ་སོགས་པར་བསྟན༌[^48]བརྟགས་ནས་བརྗོད་ན་དེའི་ཚེ། དེ་བཞིན་གཤེགས་པའི་གསུང་དོན་མེད་པར་འགྱུར་བས་མི་རིགས་སོ་ཞེས་པའི༌[^49]བརྩད་པ་རིགས་པར་འགྱུར་ལ་གནས་པ་ལ་སོགས་པས་བསྟན་པའི་ཡུལ་ནི་འདི་མ་ཡིན་ནོ། །

[Block 61]
འོན་ཀྱང་འཇིག་རྟེན་གྱི་ཐ་སྙད་དུའོ། །

[Block 62]
དེའི་ཕྱིར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་མཐུས༌[^50]གནས་པ་ལ་སོགས་པ་ཉེ་བར་བསྟན། [^51]གཞན་གྱི་རྐྱེན་ལ་མི་ལྟོས་པའི་ཡེ་ཤེས་ལ་ལྟོས་ནས་མ་ཡིན་ནོ། །

[Block 63]
དེའི་ཡེ་ཤེས་ནི་རང་བཞིན་ཡུལ་ཡིན་པའི་ཕྱིར་ནི་ཆོས་ཐམས་ཅད་མྱ་ངན་ལས་འདས་པ་དང་ཁྱད་པར་མེད་པ༌[^52]དེ་གནས༌[^53]ལ་སོགས་པ་ཉེ་བར་དམིགས་ཤིང་། ཁོ་བོ་ཅག་གནས་པ་ལ་སོགས་པ་འགེགས་པར་བྱེད་པ༌[^54]ལུང་གིས་གནོད་པ་གོ་སྐབས་ག་ལ་ཡོད་ཅེས་བྱ་སྟེ། ལུང་གིས༌[^55]བརྩད་པ་རིགས་པ་མ་ཡིན་ལ། ཇི་ལྟར་གནས་པ་དང་སྐྱེ་བ་དང་འཇིག་པ་སེལ་བ་ཡང་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་བརྗོད་པ་ལ་ལུང་གིས་གནོད་པར་མི་ནུས་སོ། །

[Block 64]
དེ་བཞིན་དུ་ཡོད་པ་དང་མེད་པ་དང་དམན་པ་དང་མཉམ་པ་དང་ཁྱད་པར་ཅན་སེལ་བ་ལ་ཡང་གནོད་པར་མི་ནུས་སོ། །

[Block 65]
དེ་ལ་ཡོད་ཅེས་བརྗོད་པ་ནི། གང་ཡོད་པ་འདི་ལྟ་སྟེ། ད་ལྟར་བའི་ཕུང་པོ་དང་། ཁམས་དང་། སྐྱེ་མཆེད་རྣམས་སམ། འདུས་བྱས་རྣམས་སོ། །

[Block 66]
མེད་པ་ཞེས་བརྗོད་པ་ནི་གང་མེད་པ་སྟེ། འདི་ལྟར་གང་འདས་པ་དང་། མ་འོངས་པའི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་རྣམས་སམ་འདུས་མ་བྱས་སོ། །

[Block 67]
ཡང་ཇི་ལྟར་ན་གནས་པ་ལ་སོགས་པ་བཀག་པ་ཉིད་ཀྱིས་དེ་རྣམས་སེལ་བར་འགྱུར། དེ་སྐད་དུ་ཡང་རྩ་བའི་རབ་བྱེད་བདུན་པར།

[Block 68 [VERSE]]
སྐྱེ་དང་གནས་དང་འཇིག་པ་ཡི། །
འདུས་བྱས་གྲུབ་པ་ཡོད་མ་ཡིན། །
འདུས་བྱས་རབ་ཏུ་མ་གྲུབ་ན། །
འདུས་མ་བྱས་དེ་ཇི་ལྟར་འདོད། །

[Block 69]
ཅེས་བྱ་སྟེ། འདུས་བྱས་རྣམས་ནི་དུས་གསུམ་གྱིས་རྣམ་པར་གནས་ལ་འདུས་བྱས་མེད་ན་དུས་གསུམ་ག་ལ་ཞིག །དེ་ལ་ད་ལྟར་བའི་དུས་མེད་པས་དངོས་པོ་མེད་ལ། འདས་པ་དང་། མ་འོངས་པ་མེད་པས་དངོས་པོ་མེད་པ་ཡང་མེད་དོ། །

[Block 70]
དེའི་ཕྱིར་དངོས་པོ་འདི་གཉིས་ཀྱང་གནས་ལ་སོགས་པ་མེད་བཞིན་དུ་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་གསུངས་སོ། །

[Block 71]
ཇི་ལྟར་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་གནས་པ་ལ་སོགས་པ་མ་གྲུབ༌[^56]ལ། དེ་བཞིན་དུ་དམན་པ་དང་མཉམ་པ་དང་ཁྱད་པར་ཅན་རྣམས་ཀྱང་ངོ་། །དེ་ལ་དམན་པ་ནི་ཁྱད་པར་ཅན་མ་ཡིན་པ་སྟེ། འདི་ལྟ་སྟེ་ཉོན་མོངས་པའོ། །

[Block 72]
ཁྱད་པར་ཅན་ནི་དགེ་བ་སྟེ། འདི་ལྟ་སྟེ་དགེ་བ་ལ་སོགས་པའོ། །

[Block 73]
མཉམ་པ་ནི་བར་མ་སྟེ་ལུང་དུ༌[^57]མ་བསྟན་པ་འདི་ལྟ་སྟེ། མིག་ལ་སོགས་པ་རྣམས་སོ་ཞེས་བྱ་བའོ། །

[Block 74]
འདི་དག་ནི་ཉེ་བར་བསྟན་པ་ཙམ་སྟེ། འདི་ལྟར་ཁྱད་པར་ཐམས་ཅད་འདིར་གནས་པ་ལ་སོགས་པ་མ་གྲུབ་པས་མ་གྲུབ་པར་ཁོང་དུ་ཆུད་པར་བྱ་བ་ཐ་སྙད་ཀྱི་དབང་གིས་བརྗོད་པས་ལུང་གི་གནོད་པ་སྤང་བར་བྱའོ། །

[Block 75]
ངང་གི་སྒྲའི་དོན་ལ་འམ་གྱི་སྒྲའོ། །
--- END BLOCKS ---
