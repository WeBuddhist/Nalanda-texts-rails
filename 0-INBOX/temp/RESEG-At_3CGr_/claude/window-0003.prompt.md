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
[Block 106]
དེ་ལ་ཕུང་པོ་ལྔ་པོ་དེ་དག་ལ་ཡང་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་པར་ཡང་ཡང་དག་པར་རྗེས་སུ་བལྟའོ་ཞེས་བྱ་བ་ནི་གོང་དུ་བསྟན་པ་ལྟར་དངོས་པོ་དང་། མཐའ་དང་། དེ་ལ་དམིགས་པ་གསུམ་བསྟན་པས་མཐོང་ལམ་གྱི་དམིགས་པ་བསྟན་པའོ། །

[Block 107]
ཚིག་དོན་ནི་འགྲེལ་པ་ནས་གསལ་ལོ། །

[Block 108 [HEADING]]
###### དམིགས་པ་དེ་ལ་འཇུག་པའི་རྣམ་པ། ^3-2-1-3-2-0

[Block 109]
དམིགས་པ་དེ་ལ་རྣམ་པ་གང་གིས་ཞུགས་ན་ཡང་དག་པར་རྗེས་སུ་ལྟ་བ༌[^32]ཕྱིན་ཅི་མ་ལོག་པར་ལྟ་བར༌[^33]འགྱུར་བ་ཡིན་ཞེ་ན། གཟུགས་སྟོང་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 110]
འདི་ལ་ཡང་གསུམ་སྟེ། རྣམ་པ་སོ་སོའི་མཚན་ཉིད་དང་། གྲངས་ངེས་པ་དང་། གོ་རིམས་ངེས་པའོ། །

[Block 111 [HEADING]]
###### **དང་པོ་རྣམ་པ་སོ་སོའི་མཚན་ཉིད།** ^3-2-1-3-2-1-0

[Block 112]
དེ་ལ་དང་པོ་ནི་གསལ་ལོ། །

[Block 113 [HEADING]]
###### **གྲངས་ངེས་པ།** ^3-2-1-3-2-2-0

[Block 114]
གྲངས་ངེས་པ་ནི་འདིར་སྙིང་པོའི་དོན་བཤད་པ་ཡིན་ལ། སྙིང་པོའི་དོན་གྱི་གཙོ་བོ་ཡང་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་ཡིན་ནོ། །

[Block 115]
རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་ཡང་ཟབ་མོའི་དོན་བརྒྱད་ཀྱིས་བསྡུས་ཏེ། དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་དང་། རྣམ་པར་ཐར་པའི་སྒོ་སྟོང་པ་ཉིད་ཡིན་ལ། སྟོང་པ་དང་མཚན་མ་མེད་པ་གཉིས་ཀྱིས་ཀྱང་རང་གི་ངོ་བོས་སྟོང་པ་དང་། སྤྱིའི་ངོ་བོས་སྟོང་པ་གཉིས་བཤད་པས་ལྟ་བའི་དབང་དུ་བྱས་ནས་དེ་གཉིས་སུ་སྟོང་པ་ཉིད་ཀྱི་དོན་ཐམས་ཅད་འདུས་པ་ཡིན་པས་དེ་བཤད་དོ། །

[Block 116]
མཚན་ཉིད་མེད་པ་ནི་རྒྱུ་མཚན་དང་བྲལ་བ་སྟེ། རྒྱུ་ཡང་འབྲས་བུ་ལ་ལྟོས་ནས་རྒྱུར་འཇོག་པ་ཡིན་ལ། དེ་ཡང་ཀུན་ནས་ཉོན་མོངས་པ་རྒྱུ་འབྲས་དང་། རྣམ་པར་བྱང་བའི་རྒྱུ་འབྲས་གཉིས་སུ་འདུས་པ་ཡིན་པས་མ་སྐྱེས་པ་མ་འགགས་པ་དྲི་མ་མེད་པ་དྲི་མ་དང་བྲལ་བ་མེད་པ་སྟེ། རིམ་པ་བཞིན་ནོ། །

[Block 117]
སྨོན་པ་མེད་པ་ནི་འབྲས་བུ་ལ་སྨོན་པའི་ཡུལ་གཉིས་ཏེ། སྐྱོན་དང་བྲལ་བ་དང་ཡོན་ཏན་དང་ལྡན་པར་སྨོན་པའོ། །

[Block 118]
དེ་གཉིས་དང་བྲལ་བ་ནི་སྨོན་པ་མེད་པའོ། །

[Block 119]
དེས་ན་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་གྱི་རང་བཞིན་ལ། དགག་བྱ་བརྒྱད་བཀག་པའི་རྣམ་པ་ཡང་བརྒྱད་ཁོ་ནར་ངེས་སོ། །

[Block 120]
དེ་ནི་གྲངས་ངེས་པའོ། །

[Block 121 [HEADING]]
###### **གོ་རིམས་ངེས་པ།** ^3-2-1-3-2-3-0

[Block 122]
གོ་རིམས་ངེས་པ་ནི་མདོ་སྡེ་ཐམས་ཅད་དུ་བདེ་བར་གཤེགས་པས་སྟོང་པ་ཉིད་ཀྱི་རྣམ་པར་ཐར་པ་སྔོན་ལ་བསྟན་ལ། དེ་ནས་མཚན་མ་མེད་པ་ཐ་མར་སྨོན་པ་མེད་པའོ། །

[Block 123]
འདིར་དེ་ཉིད་ཀྱིས་ངེས་པ་ཡིན་ནོ། །

[Block 124]
སངས་རྒྱས་ཀྱི་ལྟ་བ་དང་། སྤྱོད་པ་དང་འབྲས་བུ་གསུམ་རིམ་གྱིས་སྐྱེ་ལ། དེ་གསུམ་ལ་ཞེན་པའི་གཉེན་པོ་གསུམ་རིམ༌[^34]བཞིན་དུ་བསྟན་ལ་གྲངས་ངེས་པ་དེ་ཉིད་ཀྱིས་གོ་རིམས་ཀྱང༌[^35]ངེས་སོ། །

[Block 125]
དེས་ན་མདོ་འདིའི་བཤད་བྱ་གཙོ་བོ་ཡང་ཟབ་པའི༌[^36]དོན་བརྒྱད་པོ་འདི་ཉིད་ཡིན་ནོ་ཞེས་དྲི་མ་མེད་པའི་བཤེས་གཉེན་གྱིས་བཤད་དོ། །

[Block 126 [HEADING]]
###### རྣམ་པ་དེས་རྣམ་པར་བལྟས་པའི་འབྲས་བུ། ^3-2-1-3-3-0

[Block 127]
ད་ནི་དམིགས་པ་དེ་ལ་རྣམ་པ་འདི་བརྒྱད་ཀྱི་སྒོ་ནས་རྣམ་པར་བལྟས་པའི་འབྲས་བུ་ཤེས་པའི་སྣང་བ་ཇི་ལྟ་བུ་སྐྱེ་བ་དེ་བསྟན་པའི་ཕྱིར། ཤཱ་རིའི་བུ་དེ་ལྟ་བས་ན་དེའི་ཚེ་སྟོང་པ་ཉིད་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དེ་ལྟ་བས་ན་ཞེས་བྱ་བ་ནི་ཇི་སྐད༌[^37]གསུངས་པའི་རྣམ་པ་རྣམས་ཀྱིས་དམིགས་པ་དེ་ལ་རྣམ་པར་བལྟས་པ་ནའོ། །

[Block 128]
དེའི་ཚེ་ནི་དེའི་དུས་ན་སྟེ། རྣམ་པར་བལྟས་པའི་དུས་ནའོ། །

[Block 129]
འབྲས་བུ་ཅི་འབྱུང་ཞེ་ན། སྟོང་པ་ཉིད་ལ་གཟུགས་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྟེ། སྟོང་པ་ཉིད་མཐོང་བ་ལ་གཟུགས་ལ་སོགས་པ་ཡང་དག་པར་མི་དམིགས་པའི་ཤེས་པ་སྐྱེ་བའོ། །

[Block 130]
དེས་ན་དམིགས་པ་དེ་ལ་རྣམ་པ་འདི་བརྒྱད་ཀྱི་སྒོ་ནས་གོམས་པར་བྱས་པ་ལ་སྟོང་པ་ཉིད་དུ་སྣང་བའི་ཤེས་པ་འདི་འདྲ་བ་སྐྱེས་པ་ནི་མཐོང་བའི་ལམ་གྱི་འབྲས་བུ་ཡིན་ནོ་ཞེས་བསྟན་པའོ། །

[Block 131 [HEADING]]
##### དགོས་པ་ཡོངས་སུ་གྲུབ་པའི་དམིགས་པ། ^3-2-1-4-0

[Block 132 [HEADING]]
###### བསྒོམ་ལམ། ^3-2-1-4-1-0

[Block 133]
དེ་ལྟར་མཐོང་ལམ་སྐྱེས་པ་ལ། བསྒོམ་ལམ༌[^38]སྐྱེ་བས་དེ་སྟོན་པ་ནི། ཤཱ་རིའི་བུ་དེ་ལྟ་བས་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། འགྲེལ་པ་ན་གསལ་ལོ། །

[Block 134 [HEADING]]
###### སངས་རྒྱས་ཀྱི་སའི་སྤོང་བ་ཆེ་བ། ^3-2-1-4-2-0

[Block 135]
དེའི་རྗེས་ཐོགས་སུ་བར་ཆད་མེད་པའི་ལམ་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་སྐྱེ་བ་ཡིན་པ་ལས་དེ་མ་བསྟན་པར་སངས་རྒྱས་ཀྱི་སའི་སྤོང་བ་ཆེ་བ་སྟོན་པ་ནི་བསྒོམ་ལམ་གྱི༌[^39]སྒྲིབ་པ་གཉིས་སྤངས་པ་ལ་སྤོང་བ་ཆེ་བར་འདོད་པ་ན། དེ་ནི་བསྒོམ་ལམ༌[^40]དང་འབྲེལ་པར་ཤེས་པར་བྱ་བའི་དོན་དུ་བསྒོམ་ལམ༌[^41]གྱི་རྗེས་ལ་བསྟན་ཏོ། །

[Block 136]
དེ་ཡང་འདིར་སྤོང་པ་ནི་ལན་ཅིག༌[^42]ཡིན་ནོ། །

[Block 137]
དེ་ནི་སེམས་ལ་སྒྲིབ་པ་མེད་དེ་ཞེས་བྱ་བ་ནས་མཐར་ཕྱིན་ཏོའི་བར་གོ་སླའོ། །

[Block 138]
བར་ཆད་མེད་པའི་ལམ་བསྟན་པའི་ཕྱིར་དུས་གསུམ་དུ་རྣམ་པར་ཞེས་བྱ་བ་ནས་བརྟེན་ནས་ཞེས་བྱ་བའི་བར་རོ། །

[Block 139]
སངས་རྒྱས་ཐམས་ཅད་ཅེས་བྱ་བ་ལ༌[^43]འདིར་སངས་རྒྱས་ནི་ཡིན་ལ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ནི་མ་ཡིན་ནོ་ཞེས་འབྱུང་བ་ནས། ས་བཅུའི་ཁྱད་པར་གྱི་ལམ་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 140]
དེའི་ལམ་ན༌[^44]རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ཡིན་པར་འགྲེལ་པ་ནས་གསལ་བར་བཤད་དོ། །

[Block 141]
འདིར་ནི་མདོ་ལས་རྟོགས་པ་ཆེ་བ་དང་སེམས་དཔའ་ཆེ་བ་གཉིས་གཙོར་བསྟན་པའི་ཞར་ལ་བར་མ་ཆོད་པའི་རྒྱུ་འདི་ཡང་ཞར་བྱུང་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 142 [HEADING]]
###### རྟོགས་པའི་བདག་ཉིད། ^3-2-1-4-3-0

[Block 143]
དེ་ལྟར་སྤངས་པའི་བདག་ཉིད་བསྟན་ནས། རྟོགས་པའི་བདག་ཉིད་རྣམ་པ་གཉིས་བསྟན་པའི་ཕྱིར་བླ་ན་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། དེ་ལ་གཉིས་ཏེ། ཇི་སྙེད་ཡོད་པ་མཁྱེན་པ་དང་ཇི་ལྟར༌[^45]མཁྱེན་པ་སྟེ། སེམས་དཔའ་ཆེ་བ་དང་རྟོགས་པ་ཆེ་བ་གཉིས་ཡིན་པས་ལན་གཉིས་སུ་གཞག་པ་ཡིན་ནོ། །

[Block 144 [HEADING]]
###### **ཇི་སྙེད་ཡོད་པ་མཁྱེན་པ།** ^3-2-1-4-3-1-0

[Block 145]
དེ་ལ་བླ་ན་མེད་པ་ཞེས་བྱ་བས་ནི་དམིགས་པར་བྱ་བའི་ཡུལ་དང་། དེ་རྗེས་སུ་སྒྲུབ་པའི་རྒྱུ་དང་། འབྲས་བུ་ཐོབ་པ་བླ་ན་མེད་པ་སྟེ། དེ་གསུམ་གྱིས་ནི་ཇི་སྙེད་མཁྱེན་པའི་ཡེ་ཤེས་བསྟན་པ་ཡིན་ཏེ། དེ་གསུམ་དང་ལྡན་པས་ཤེས་བྱའི་དངོས་པོ་ཐམས་ཅད་སྐྱུ་རུ༌[^46]ར་ལག་མཐིལ་དུ་བཞག་པ༌[^47]ལྟར་མཁྱེན་པའོ། །
--- END BLOCKS ---
