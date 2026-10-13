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
[Block 3116]
གང་གི་ཚེ་ཁམས་ལས་ཡང་དག་པར་འདས་པ་དེའི་ཚེ་ཡོངས་སུ་ཤེས་པའི་མིང་འཐོབ་པོ། །

[Block 3117 [HEADING]]
#### ཡོངས་སུ་ཤེས་པ་དུ་མ་དང་ལྡན་པ། ^5-18-1-0

[Block 3118]
གང་ཞིག་ཡོངས་སུ་ཤེས་པ་དུ་མ༌[^1226]དང་ལྡན་ཞེ་ན།

[Block 3119 [VERSE]]
གཅིག་མིན་མཐོང་ལ་གནས་པ་ནི། །
ལྔ་ཡི་བར་དང་ཡང་དག་ལྡན། །

[Block 3120]
རེ་ཞིག་སོ་སོའི་སྐྱེ་བོ་ནི་མི་ལྡན་པ་ཁོ་ནའོ། །

[Block 3121]
འཕགས་པ་ཡང་ཀུན་འབྱུང་ལ༌[^1227]ཆོས་ཤེས་པའི་བཟོད་པ་ལ་གནས་པའི་བར་རོ། །

[Block 3122]
ཀུན་འབྱུང་ལ་ཆོས་ཤེས་པ་ནི་གཅིག་དང་ལྡན་ནོ། །

[Block 3123]
ཀུན་འབྱུང་ལ་རྗེས་སུ་ཤེས་པ་ནི་གཉིས་དང་ལྡན་ནོ། །

[Block 3124]
འགོག་པ་ལ་ཆོས་ཤེས་པ་ནི་གསུམ་དང༌[^1228]ལྡན་ནོ། །

[Block 3125]
འགོག་པ་ལ་རྗེས་སུ་ཤེས་པ་ནི་བཞི་དང་ལྡན་ནོ། །

[Block 3126]
ལམ་ལ་ཆོས་ཤེས་པ་ནི་ལྔ་དང་ལྡན་ནོ། །

[Block 3127 [VERSE]]
བསྒོམ་ལ་གནས་པ་དྲུག་གམ༌[^1229]ནི། །
གཅིག་གམ་ཡང་ན་གཉིས་དང་ངོ་། །

[Block 3128]
དྲུག་གིས་ནི་ཇི་སྲིད་དུ་འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་མ་ཐོབ་པའམ། དེ་ལས་ཡོངས་སུ་ཉམས་པའོ། །

[Block 3129]
སྔོན་ནམ་ཕྱིས་འདོད་པ་ལ་འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་པ་ནི་གཅིག་གིས་སོ། །

[Block 3130]
དགྲ་བཅོམ་པ་ཉིད་ཐོབ་ན༌[^1230]ཡང་གཅིག་ཁོ་ན་དང་ངོ་། །གཟུགས་ན་སྤྱོད་པའི་ཀུན་ནས་དཀྲིས་པས་ཡོངས་སུ་ཉམས་ན་དེ་ཡང་གཅིག་གོ། །

[Block 3131]
གཟུགས་ཀྱི་འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་པ་ན་གཉིས་དང་ངོ་། །གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཀུན་ནས་དཀྲིས་པས་ཡོངས་སུ་ཉམས་པ་ཡང་གཉིས་ཁོ་ན་དང་ངོ་། །ཡང་ཅིའི་ཕྱིར་ཕྱིར་མི་འོང་བ་དང་དགྲ་བཅོམ་པ་དག་གི་ཡོངས་སུ་ཤེས་པ་གཅིག་ཁོ་ནར་རྣམ་པར་གཞག་ཅེ་ན། འདི་ལྟར།

[Block 3132 [VERSE]]
ཁམས་ལས་འདོད་ཆགས་བྲལ་བ་དང་། །
འབྲས་བུ་ཐོབ་ཕྱིར་དེ་དག་བསྡོམས། །

[Block 3133]
ཡོངས་སུ་ཤེས་པ་རྣམས་སྡོམ་ཞིང་གཅིག་ཏུ་རྣམ་པར་འཇོག་པ་ནི་རྒྱུ་གཉིས་ཀྱིས་ཡིན་ལ། ཕྱིར་མི་འོང་བ་དང་དགྲ་བཅོམ་པ་དག་ལ་འདི་གཉིས་ཀ་ཡོད་པས་དེའི་ཕྱིར་ཡོངས་སུ་ཤེས་པ་ནི་གཅིག་ཅེས་བྱའོ། །

[Block 3134 [HEADING]]
#### ཡོངས་སུ་ཤེས་པ་གཏོང་བ་དང་འཐོབ་པ། ^5-18-2-0

[Block 3135]
ཡང་གང་ཞིག་གིས་ཡོངས་སུ་ཤེས་པ་དུ་ཞིག་གིས་གཏོང་ངམ་འཐོབ་ཅེ་ན།

[Block 3136 [VERSE]]
ལ་ལ་གཅིག་གཉིས་ལྔ་དང་དྲུག །
གཏོང་སྟེ་འཐོབ་པ་ལྔ་ཡིན༌[^1231]ནོ། །

[Block 3137]
དགྲ་བཅོམ་པ་ཉིད་དམ་འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་པས་ནི་གཅིག་གཏོང་ངོ་། །ཕྱིར་མི་འོང་བའི་གཟུགས་ཀྱི་འདོད་ཆགས་དང་བྲལ༌[^1232]བ་ཞིག་འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་ན་ཡོངས་སུ་ཤེས་པ་གཉིས་གཏོང་ངོ་། །འདོད་ཆགས་དང་བྲལ་བ་སྔོན་དུ་འགྲོ་བ་ལམ་ལ་རྗེས་སུ་ཤེས་པ་ནི་ལྔ་གཏོང་ངོ་། །མཐར་གྱིས་པ་འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བར་བྱེད་པས་ནི་ཡོངས་སུ་ཤེས་པ་དྲུག་གཏོང་ངོ་། །དེ་བཞིན་དུ་ཐོབ་པ་ཡང་ལ་ལ་ནི་ཡོངས་སུ་ཤེས་པ༌[^1233]ཁོ་ན་གཅིག༌[^1234]ཐོབ་སྟེ། གང་ལ་ལ་ཞིག་གིས་སྔོན་མེད་པ་ཐོབ་པའོ། །

[Block 3138]
ལ་ལ་ནི་གཉིས་ཏེ། གང་ཞིག་གཟུགས་མེད་པའི་ཁམས་ལས་འདོད་ཆགས་དང་བྲལ་བ་འབའ་ཞིག་ལས་ཡོངས་སུ་ཉམས་པའོ། །

[Block 3139]
ཁ་ཅིག་གིས་ནི་དྲུག་སྟེ། གང་ཞིག་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ལས་ཡོངས་སུ་ཉམས་པའོ། །

[Block 3140]
ལྔ་ཐོབ་པ་ནི་འགའ་ཡང་མེད་པ་ཉིད་དོ། །

[Block 3141]
ཕྲ་རྒྱས་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་ལྔ་པའོ།། །།

[Block 3142 [HEADING]]
## ལམ་དང་གང་ཟག་བསྟན་པ། ^6-0

[Block 3143 [HEADING]]
### མཐོང་བའི་ལམ་དང་བསྒོམ་པའི་ལམ་ཇི་ལྟར་སྐྱེ་བ། ^6-1-0

[Block 3144]
ཇི་སྐད་དུ་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པའི་མིང་འཐོབ་པོ་ཞེས་བཤད་པ་དེ་ཡང་།

[Block 3145 [VERSE]]
དབེན་པ་མཐོང་བ་བསྒོམས་པ་ལས། །
ཉོན་མོངས་སྤངས་པ་ཞེས་བཤད་པ། །

[Block 3146]
དེ་ལ་ཡང་།

[Block 3147 [VERSE]]
བསྒོམ་པའི་ལམ་ནི་རྣམ་གཉིས་ཏེ། །
མཐོང་བ་ཞེས་བྱ་ཟག༌[^1235]པ་མེད། །

[Block 3148]
བསྒོམ་པའི་ལམ་ནི་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའོ།[^1236] །

[Block 3149]
མཐོང་བའི་ལམ་ནི་འཇིག་རྟེན་ལས་འདས་པ་ཁོ་ནའོ། །

[Block 3150 [HEADING]]
#### བདེན་པ་བཞི། ^6-1-1-0

[Block 3151]
བདེན་པ་མཐོང་བ་ལས་ཞེས་བརྗོད་དེ། དེ་དག་ཀྱང་། བདེན་པ་དག་ནི་བཞིར་བཤད་དོ། །གང་དུ་བཤད་ཅེ་ན།

[Block 3152]
ཆོས་ཟག་པ་དང་བཅས་པ་དང་། །ཟག་པ་མེད་པ༌[^1237]བསྟན་པར་རོ། །

[Block 3153]
དེར་གང་བཤད་པའི་རིམ་པ་ཅི་དེ་ཁོ་ན་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ་འོན་ཀྱང་།

[Block 3154 [VERSE]]
སྡུག་བསྔལ་ཀུན་འབྱུང་དེ་བཞིན་དུ། །
འགོག་དང་ལམ་སྟེ་དེ་ལྟར་ན། །

[Block 3155]
དེ་དག་གི་རིམ་པ་ནི་འདི་ཡིན་ཏེ། རང་གི་ངོ་བོ་ནི་སྔར་ཇི་སྐད་བཤད་པ་ཁོ་ན་བཞིན་ནོ། །
--- END BLOCKS ---
