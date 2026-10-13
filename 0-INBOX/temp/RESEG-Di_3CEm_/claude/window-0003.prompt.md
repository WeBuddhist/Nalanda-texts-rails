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
[Block 106 [HEADING]]
#### ལུས་ཀྱི་ཕྱག་བྱ་བ། ^2-1-1-0

[Block 107]
དེ་ལ་ལུས་ཀྱི་ཕྱག་བྱ་བ་ནི། ཞིང་གི་རྡུལ་སྙེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྟེ། སངས་རྒྱས་ཀྱི་ཞིང་གི་རྡུལ་སྙེད་ཀྱི་ལུས་ཀྱིས་ཕྱག་བྱ་བའོ། །

[Block 108]
སྙེད་ཅེས་བྱ་བ་ནི་དཔེའི་རྣམ་གྲངས་ཏེ། ཕྱོགས་བཅུ་དུས་གསུམ་དུ་གཤེགས་པའོ༌[^32]སངས་རྒྱས་ཀྱི་ཞིང་ཇི་སྙེད་ཀྱི་ལུས་རབ་ཏུ་བཏུད་པས་ཕྱག་བྱ་བའོ། །

[Block 109]
རྒྱལ་བ་ཀུན་ལ་རབ་ཏུ་ཕྱག་འཚལ་ལོ། །ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པའི་དགྲ་དང་བདུད་ལས་རྒྱལ་བས་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་རྒྱལ་བ་ཞེས་བྱ་སྟེ། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ།

[Block 110 [VERSE]]
སྡིག་པའི་ཆོས་རྣམས་ལས་རྒྱལ་བས། །
ཉེར་འགྲོ་ང་ནི་རྒྱལ་བ་ཡིན། །

[Block 111]
ཞེས་གསུངས་པ་ལ་སོགས་པའོ། །

[Block 112]
དེ་ལྟར་དུས་གསུམ་དུ་གཤེགས་པའི་རྒྱལ་བ་ཐམས་ཅད་ལ་ཕྱག་བྱའོ། །

[Block 113]
བཅོམ་ལྡན་འདས་གཅིག་ལ་སེམས་ཀྱིས་དམིགས་པ་ན། གཞན༌[^33]ལ་མ་ཁྱབ་པར་འགྱུར་རོ་སྙམ་པ་ལ། རྒྱལ་བ་ཐམས་ཅད་ཡིད་ཀྱིས་མངོན་སུམ་དུ། །ཞེས་བྱ་བ་བཤད་དོ། །

[Block 114]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་རེ་རེ་ཞིང་ཡང་མངོན་སུམ་དུ་བསམ་པའི་དོན་ཏོ། །

[Block 115]
བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་སྟོབས་དག་གིས། །ཞེས་བྱ་བ་ལ། བཟང༌[^34]པོ་ནི་དགེ་བའོ། །

[Block 116]
བཟང་པོ་ཡང་ཡིན་ལ་སྤྱོད་པ་ཡང་ཡིན་པས་ན་བཟང་པོ་སྤྱོད་པ་སྟེ། བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 117]
དེར་སྨོན་པའི་སྨོན་ལམ་ཡིན་པས་ན་སྨོན་ལམ་ཞེས་བྱའོ། །

[Block 118]
དེའི་སྟོབས་ཀྱིས་ཉོན་མོངས་པ་ལ་སོགས་པས་ཟིལ་གྱིས་མི་ནོན་ཅིང་མི་མཐུན་པའི་ཕྱོགས་བཅོམ་པས་ན་སྟོབས་དག་གིས་ཞེས་བྱ་བ་སྟེ། རྣམ་པ་གཞན་ལས་ནི་འདི་ལྟ་བུའི་བྱེད་པ་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 119 [HEADING]]
#### ཡིད་ཀྱིས་ཕྱག་བྱ་བ། ^2-1-2-0

[Block 120]
ད་ནི་ཡིད་ཀྱིས་ཕྱག་བྱ་བ་སྟེ། རྡུལ་གཅིག་སྟེང་ན་རྡུལ་སྙེད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 121]
རྡུལ་གཅིག་གི་སྟེང་དུ་རྡུལ་སྙེད་ཀྱི་སངས་རྒྱས་རྣམ་པ༌[^35]ཞེས་བྱ་བ་ནི་ཁྱད་པར་དུ་མ་སྨོས་པའི་ཕྱིར་ཕྱོགས་བཅུ་དུས་གསུམ་དུ་གཤེགས་པའི་སངས་རྒྱས་རྣམས་ཀྱི་ཞིང་གི་རྡུལ་སྙེད་ཀྱིས༌[^36]བདེ་བར་གཤེགས་པ་རྣམས་སོ། །

[Block 122]
སངས་རྒྱས་སྲས་ཀྱི་དབུས་ན་བཞུགས་པ་དག །ཅེས་བྱ་བ་ནི་རེ་རེ་ཞིང་ཡང་བྱང་ཆུབ་སེམས་དཔའ་གྲངས་མེད་པའི་ཚོགས་ཀྱི་དབུས་ན་བཞུགས་པའོ། །

[Block 123]
རྡུལ་གཅིག་གི་སྟེང་དུ་ཇི་ལྟར་བསམས་པ་དེ་བཞིན་དུ་ཐམས་ཅད་དུ༌[^37]བསམ་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 124]
དེ་ལྟར་ཆོས་ཀྱི་དབྱིངས་རྣམས་མ་ལུས་པ། །ཞེས་བྱ་བ་བཤད་དེ། ཆོས་ཀྱི་དབྱིངས་ནི༌[^38]ཐམས་ཅད་དུ་ཁྱབ་པར་བྱེད་པའི་ཕྱིར་ནམ་མཁའི་མཐས་ཀླས་པ་ཐམས་ཅད༌[^39]ཡང་རྡུལ་གཅིག་གི་སྟེང་ན་རྡུལ་སྙེད་ཀྱི་སངས་རྒྱས་རེ་རེ་ལ་ཡང་བྱང་ཆུབ་སེམས་དཔའ་གྲངས་མེད་པའི་ཚོགས་ཀྱིས་ཀུན་ནས་བསྐོར་བ་རྣམས་ཀྱིས་གང་ཞིང་བར་མཚམས་མེད་པར་ཁྱབ་པར་ཡིད་ཀྱིས་མོས་པར་བྱའོ། །

[Block 125]
ལུས་དང་ངག་གི་ལས་རྣམས༌[^40]ཡིད་ཀྱིས་བསྐྱེད་པས་ན་བར་དུ་ཡིད་ཀྱི༌[^41]ལས་བཤད་དོ། །

[Block 126 [HEADING]]
#### ངག་གིས་ཕྱག་བྱ་བ། ^2-1-3-0

[Block 127]
ད་ནི་ངག་གིས་ཕྱག་བྱ་བ་ནི། དེ་དག་བསྔགས་པ་མི་ཟད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 128]
དེ་དག་ཅེས་བྱ་བ་ནི་ཇི་ལྟར་མོས་པར་བྱ་བ་དག་གོ། །

[Block 129]
མཐར་ཡང་འགོད་པ་མེད་པས་ན་དེ་མི་ཟད་པའོ། །

[Block 130]
བསྔགས་པ་རྒྱ་མཚོ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་རྒྱ་མཚོ་སྟེ། དེ་དག་གི་བསྔགས་པ་རྒྱ་མཚོ་བཞིན་མི་ཟད་པའོ། །

[Block 131]
བསྔགས་པ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་གྱི་རྣམ་གྲངས་སོ། །

[Block 132]
རྒྱ་མཚོ་ཞེས་བྱ་བ་ནི་མང་པོའི་དོན་དུ་རིག་པར་བྱའོ། །

[Block 133]
དབྱངས་ཀྱི་ཡན་ལག་རྒྱ་མཚོའི་སྒྲ་ཀུན་གྱིས། །ཞེས་བྱ་བ་ལ། ཡན་ལག་ཅེས་བྱ་བ་ནི་ཡོན་ཏན་གྱི༌[^42]རྣམ་གྲངས་སོ། །ཇི་ལྟ་ཞེ་ན། འདི་ལྟ་སྟེ།

[Block 134]
ཉན་ཐོས་ཀྱི་ཐེག་པ་ལས།

[Block 135]
བཅོམ་ལྡན་འདས་ཀྱི་དབྱངས་ནི་ཡན་ལག་ལྔ་དང་ལྡན་ཞེས་འབྱུང་བ་དང་། ཐེག་པ་ཆེན་པོ་ལས་ཡན་ལག་དྲུག་ཅུ་དང་ལྡན་ལ། ཡན་ལག་སྟོང་ཕྲག་བཅུ་དྲུག་དང་ལྡན་པ།[^43] །ཚད་མེད་པའི་ཡན་ལག་དང་ལྡན་ཞེས་འབྱུང་སྟེ། དེ་ལྟར་ཡོན་ཏན་ལྔ་ལ་སོགས་པ་དང་ལྡན་པར་རིག་པར་བྱའོ། །

[Block 136]
[^44]

[Block 137 [HEADING]]
### མཆོད་པ། ^2-2-0

[Block 138 [HEADING]]
#### བླ་ན་ཡོད་པའི་མཆོད་པ། ^2-2-1-0

[Block 139]
ད་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་དེ་དག་ལ་བླ་ན་ཡོད་པ་དང་བླ་ན་མེད་པའི་མཆོད་པ་རྣམ་པ་གཉིས་ལས་བླ་ན་ཡོད་པའི་ཚིགས་སུ་བཅད་པ་གཉིས་ཏེ། མེ་ཏོག་དམ་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 140]
མེ་ཏོག་ལ་སོགས་པ་དམ་པ་གང་ཡིན་པ་དེ་དག་ནི་མེ་ཏོག་དམ་པ་དང་། ཕྲེང་བ་དམ་པ་དང་། སིལ་སྙན་དམ་པ་དང་། བ་དན་དང་། ཙན་དན་དང་། གུར་གུམ་ལ་སོགས་པའི་བྱུག་པ་དམ་པ་དང་། གདུགས་དམ་པ་དང་། མར་མེ་དམ་པ་དང་། བདུག་པ་དམ་པ་དང་། ན་བཟའ་དམ་པ་དང་། སྤོས་སྣ་ཚོགས་སྦྱར་བའི་དྲི་དམ་པ་དང་། ཙན་དན་དང་། གུར་གུམ་དང་། ག་བུར་དང་། ཨ་ག་རུ༌[^45]ལ་སོགས་པའི་ཕྱེ་མའི་ཕུར་མ་རི་རབ་དང་མཉམ་པ་རྣམས་ཀྱིས་སོ། །

[Block 141]
ཁྱད་པར་ཅན་གྱི་རྒྱན་མཆོག་ཐམས་ཅད་ཀྱིས། །ཞེས་བྱ་བ་ལ་རྒྱན་མཆོག་ཅེས་བྱ་བ་ནི་མང་པོའི་རྣམ་གྲངས་སོ། །

[Block 142]
ལྷ་དང་མིའི་རྣམ་པ་ཐམས་ཅད་དང་ལྡན་པའི་དམ་པ་རྣམས་ཀྱིས་རྒྱལ་བ་དེ་དག་ཐམས་ཅད་ལ་མཆོད་པར་བགྱིའོ། །

[Block 143 [HEADING]]
#### བླ་ན་མེད་པའི་མཆོད་པ། ^2-2-2-0

[Block 144]
ད་ནི་བླ་ན་མེད་པའི་མཆོད་པ༌[^46]བཤད་པར་བྱ་སྟེ། མཆོད་པ་གང་རྣམས་བླ་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྟེ། བླ་ན་མེད་པའི་མཆོད་པ་རྒྱ་ཆེ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་གྱི་མཐུ་ལས་སྐྱེས་པ་སངས་རྒྱས་ཀྱི་ཞིང་ཐམས་ཅད་དུ་ཁྱབ་པར་ཆོས་ཀྱི་དབྱིངས་དམ་པས་རྒྱལ་བ་དེ་དག་ཀུན་ལ་བདག་གི་བསམ་པས་སོ།[^47] །

[Block 145]
བཟང་པོ་སྤྱོད༌[^48]ལ་དད་པའི་སྟོབས་དག་གིས། །ཞེས་བྱ་བ་ནི་བཟང་པོ་སྤྱོད་པ་ལ་མོས་པ་དང་། དད་ཅིང་ངེས་པར་ཡིད་ཆེས་པ་དེའི་སྟོབས་ཀྱིས་སོ། །
--- END BLOCKS ---
