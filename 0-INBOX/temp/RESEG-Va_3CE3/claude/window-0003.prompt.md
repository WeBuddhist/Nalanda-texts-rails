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
[^84]ཁྲག་འཁྲུགས་པ༌[^85]དང་བྲལ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་དང་། ལས་དང་རྣམ་པར་སྨིན་པའི་དབང་གིས་ཁྲག་འཁྲུགས་དང་རྣམ་པར་གཡེང་བར་གྱུར་པ་གང་ཡིན་པ་དེ༌[^86]དག་དང་བྲལ་བར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 107]
ཆགས་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པའི་ཆགས་པ་དང་། ལས་ཀྱི་སྒྲིབ་པའི་ཆགས་པ་དང་། རྣམ་པར་སྨིན་པའི་སྒྲིབ་པའི་ཆགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 108]
ངག༌[^87]གི་ལམ་གྱི་སྒྲ་ཡང་དག་པར་ཆད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ངག་གི་ཐ་སྙད་ཀྱི་བདག་ཉིད་ཀྱི་སྒྲ་རྣམས་ཡང་དག་པར་ཆད་པའི་ཕྱིར་རོ། །

[Block 109]
དེ་བཞིན་ཉིད་ལས་མ་གཡོས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ཀྱི་རང་གི་ངོ་བོ་ཉིད་ལས་རྣམ་པར་མ་གཡོས་པའི་ཕྱིར་རོ། །

[Block 110]
ཇི་ལྟ་བ་བཞིན་དུ་མ་སྐྱེས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རིགས་པར་མ་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 111]
ཁེངས་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཁེངས་པ་ཞེས་བྱ་བ་ཉེ་བའི་ཉོན་མོངས་པ་འམ། ཉོན་མོངས་པའི་རྣམ་པར་རྟོག་པ་ལས་གྱུར་པའི་ཁེངས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 112]
བྱེད་པ་པོ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་བྱེད་པ་པོ་ཞེས་བྱ་བ་གང་ཟག་གམ་དབང་ཕྱུག་ལ་སོགས་པ་མི་མཐུན་པའི་རྒྱུ་རྣམས་སམ། རྒྱུ་དང་རྐྱེན་གྱི་ཆོས་རྣམས་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ། །

[Block 113]
མཉམ་པ་ཉིད་ལས་མི་འདའ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ལ༌[^88]མཉམ་པ་ཉིད་ལས་མི་འདའ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 114]
ང་ཡིར་འཛིན་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྲེད་པས་བདག་གིར་འཛིན་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 115]
འགྲོ་བ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་བདེ་འགྲོ་དང་། ངན་འགྲོའི་དབང་གིས་སྐྱེ་བ་གཞན་དུ་འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 116]
གནས་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་གནས་པའི༌[^89]མཚན་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 117]
སྐྱེ་བ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་མེད་པ་ལས་བྱུང་བའི༌[^90]མཚན་ཉིད་ཀྱི་སྐྱེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 118]
དབུགས་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཉམ་ཆུང་བའི་ཕྱིར་སྟོབས་མེད་པའོ། །

[Block 119]
ཆོས་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་རྣམ་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 120]
ནམ་མཁའ་དང་མཉམ་པ་ཉིད་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ནམ་མཁའ་དང་མཉམ་པས་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ། །

[Block 121]
ཟད་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་མི་རྟག་པ་ཉིད་ཀྱི་མཚན་ཉིད་ཀྱི་ཟད་པ་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 122]
ཡེ་ཤེས་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཤེས་བྱའི་དངོས་པོ་མེད་པས་མཚན་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 123]
རྒྱུ་མེད་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་རྒྱུའི་མཚན་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 124]
འཇིགས་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་རྣམ་པར་འཇིག་པའི་མཚན་ཉིད་འཇིགས་པ༌[^91]མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 125]
མདོག་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ལ་མདོག་མེད་ཅིང་འོད་མེད་པས་མི་སྣང་བའི་ཕྱིར་རོ། །

[Block 126]
དྲན་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་དྲན་པར་བྱེད་པའི་ཤེས་པའི་སྤྱོད་ཡུལ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 127]
བོད་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་མིང་གི་སྤྱོད་ཡུལ་མ་ཡིན་པའི་ཕྱིར་ཏེ། མིང་ནི་བོད་པའོ། །

[Block 128]
ཆོས་རྣམས་ལ་སྤྲོ་བ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་གཡོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 129]
སྟུག་པོ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྟུག་པོར་རྣམ་པར་རྟོག་པ་ལོག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 130]
རྣམ་པར་བསྒྲུབ་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་འདུ་བྱེད་རྣམ་པར་དགོད་པ༌[^92]ལ་རྣམ་པར་བསྒྲུབ་པ་ཞེས་བྱ་བ་སྟེ། དེ་མེད་པའི་ཕྱིར་རོ། །

[Block 131]
ཉོན་མོངས་པ་མེད་པའི་ཕྱིར༌[^93]ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པའི་ཉོན་མོངས་པ་དང་། རྣམ་པར་རྟོག་པའི་ཉོན་མོངས་པ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 132]
འབྲས་བུ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་འབྲས་བུའི་ཆོས་རྣམས་ལ་འབྲས་བུའི་རྣམ་པ་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 133]
ཕུང་པོ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་དང་། ལས་དང་རྣམ་པར་སྨིན་པའི་ཕུང་པོ་རྣམས་མེད་པའི་ཕྱིར་རོ། །

[Block 134]
རྒ་བ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་གནས་པ་ལས་གཞན་དུ་འགྱུར་བའི་མཚན་ཉིད་ཀྱི༌[^94]རྒ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 135]
སྤྱོད་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་འགྲོ་བ་དང་། འོང་བའི་སྤྱོད་པ་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 136]
སྡིགས་པ༌[^95]མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་རྣམ་པར་འཚེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 137]
ངར་འཛིན་པ་མི་དམིགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ལྟ་བའི་བདག་ཉིད་དང་། ང་རྒྱལ་གྱི་བདག་ཉིད་ཀྱི་ངར་འཛིན་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 138]
གང་གིས༌[^96]ཐ་སྙད་འདོགས་པ་དང་། གང་གིས་བརྗོད་པ་དང་། གང་གིས་བསྟན་པ་ཞེས་བྱ་བ་ནི་སྨྲ་བའི་ཆོས་སོ། །

[Block 139]
གང་གིས་རྟོགས་པར༌[^97]བྱེད་པ་དང་། གང་གིས་མཐོང་བ་ཞེས་བྱ་བ་ནི་ཉན་པ་པོའི་ཆོས་སོ། །

[Block 140]
གང་གིས་ཐ་སྙད་འདོགས་ཞེས་བྱ་བ་ནི་གང་འཕགས་པ་རྣམས་དང་། འཕགས་པ་མ་ཡིན་པ་རྣམས་ཀྱིས༌[^98]མཐོང་བ་དང་། ཐོས་པ་དང་། བྱེ་བྲག་ཕྱེད་པ་དང་། རྣམ་པར་ཤེས་པའི་དབང་དང་། མ་མཐོང་བ་དང་། མ་ཐོས་པ་དང་། བྱེ་བྲག་མ་ཕྱེད་པ་དང་། རྣམ་པར་མ་ཤེས་པའི་དབང་སྟེ། ཐ་སྙད་བཅུ་དྲུག་གི་དབང་གིས་བརྗོད་དོ། །

[Block 141]
གང་གིས་བརྗོད་ཅེས་བྱ་བ་ནི་བུམ་པ་དང་། སྣམ་བུ་དང་བ་གླང་དང་། རྟ་ལ་སོགས་པའི་མིང་བརྗོད་པའི་དབང་གིས་བརྗོད་པའོ། །

[Block 142]
གང་གིས་སྟོན་པ་ཞེས་བྱ་བ་ནི་རིང་པོ་དང་ཐུང་ངུ་དང་། དཀར་ཤམ་དང་། སྔོ་བསངས༌[^99]དང་། སྔོན་པོ་དང་། སེར་པོ་ལ་སོགས་པའི་ཡོན་ཏན་བསྟན་པའི་དབང་གིས་བརྗོད་དོ། །

[Block 143]
ཉན་པ་པོ་ཡང་རྗེས་སུ་དག་པའི༌[^100]དབང་གིས་དོན་རྗེས་སུ་རྟོགས་པར༌[^101]བྱེད་པ་སྟེ། གང་གིས་རྟོགས་པ༌[^102]ཞེས་བྱ་བ་ནི་རྗེས་སུ་དཔག་པའི་དབང་གིས་བརྗོད་དོ། །

[Block 144]
གང་གིས་མཐོང་བ་ཞེས་བྱ་བ་དེ་ནི་མངོན་སུམ་གྱི༌[^103]དོན་མཐོང་བའི་དབང་གིས་བརྗོད་དོ། །

[Block 145]
སྒྲ་གང་ལ་ཡང་ཐོགས་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་བརྗོད་པ་ཐམས་ཅད་ལ་དོན་དམ་པ་ཚོལ་བར་འགྱུར་བའོ། །
--- END BLOCKS ---
