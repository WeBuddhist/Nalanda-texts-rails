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
[Block 281 [VERSE]]
བསམ་གཏན་གཏོགས་པའི་དགེ་བ་ནི། །
ས་འཕོས་ཉམས་པ་དག་གིས་གཏོང་། །

[Block 282]
བསམ་གཏན་དུ་གཏོགས་པའི་དགེ་བ་ཐམས་ཅད་ནི་རྒྱུ་གཉིས་ཀྱིས་གཏོང་སྟེ། གོང་མ༌[^220]འོག་ཏུ་སྐྱེ་བ་སྟེ་ས་འཕོས་པ་ལས་སམ། སྙོམས་པར་འཇུག་པ་ལས་ཡོངས་སུ་ཉམས་པ་ལས་སོ། །

[Block 283]
རིས་མཐུན་པ་བཏང་བ་ལས་ཀྱང་ཅུང་ཟད་གཏོང་བར་འགྱུར་རོ། །

[Block 284]
ཇི་ལྟར་གཟུགས་སུ་གཏོགས་པའི་དགེ་བས་འཕོ་བ་དང་། ཡོངས་སུ་ཉམས་པ་དག་གིས་གཏོང་བ་ལྟར། །

[Block 285 [VERSE]]
དེ་བཞིན༌[^221]གཟུགས་མེད་གཏོགས་འཕགས་པ། །
འབྲས་བུ་ཐོབ་སྦྱངས་ཉམས་པ་ལས། །

[Block 286]
དགེ་བ་ཟག་པ་མེད་པ་ནི༌[^222]རྒྱུ་གསུམ་གྱིས་གཏོང་བར་འགྱུར་ཏེ། འབྲས་བུ་ཐོབ་པ་ལས་ནི་ལམ་སྔ་མ་གཏོང་བར་འགྱུར་རོ། །

[Block 287]
དབང་པོ་སྦྱངས་པ་ལས་ནི་དབང་པོ་རྟུལ་པོའི་ལམ་མོ། །

[Block 288]
ཡོངས་སུ་ཉམས་པ་ལས་ནི་ལམ་གོང་མ་འབྲས་བུའམ་འབྲས་བུ་ཁྱད་པར་ཅན་ཏེ། རེ་ཞིག་སྡོམ་པ་རྣམས་ནི་དེ་ལྟར་གཏོང་ངོ་། །

[Block 289 [HEADING]]
#### སྡོམ་པ་མ་ཡིན་པ་འཆད་པ། ^1-20-3-0

[Block 290 [VERSE]]
སྡོམ་མིན་སྡོམ་པ་ཐོབ་པ་དང་། །
ཤིང༌[^223]དང་མཚན་ཉིད་བྱུང་བ་ལས། །

[Block 291]
སྡོམ་པ་མ་ཡིན་པ་ནི་རྒྱུ་གསུམ་གྱིས་འཆད་དེ། སྡོམ་པ་ཐོབ་པ་ལས་ནི་གལ་ཏེ་སྡོམ་པ་ཡང་དག་པར་བླངས་པ་ལས་སམ། རྒྱུ་དང་རྐྱེན་གྱི་སྟོབས་ཀྱིས་ཏིང་ངེ་འཛིན་ཐོབ་པས་བསམ་གཏན་གྱི་སྡོམ་པ་ཐོབ་ན་གཉེན་པོ་སྟོབས་དང་ལྡན་པའི་ཕྱིར་དེས་སྡོམ་པ་མ་ཡིན་པ་འཆད་པར་འགྱུར་རོ། །

[Block 292]
ལུས་བོར་བའི་ཕྱིར་ཤི་བ་དང་། རྟེན་ཉམས་པའི་ཕྱིར་མཚན་ཉིད༌[^224]བྱུང་བ་ལས་འདོར་བར་འགྱུར་རོ། །

[Block 293]
མཚོན༌[^225]དང་རྒྱ་མི་བྱ་བའི་བསམ་པ་ཐག་པ་ནས་བོར་དུ་ཟིན་ཀྱང་སྡོམ་པ་མེད་པར་སྡོམ་པ་མ་ཡིན་པ་འཆད་པ་མེད་དེ། གཞི་ཡོངས་སུ་སྤངས་ཀྱང་སྨན་མེད་པར་ནད་རྙིང་མི་བཟློག་པ༌[^226]བཞིན་ནོ། །

[Block 294]
སྡོམ་པ་མ་ཡིན་པ་ཅན་གང་ཞིག་བསྙེན་གནས་ཀྱི་སྡོམ་པ་ནོད་ན་ཅི་འདི་སྡོམ་པ་དེ་ལས་ཡང་སྡོམ་པ་མ་ཡིན་པར་འགྱུར་རམ། འོན་ཏེ་སྡོམ་པ་ཡང་མ་ཡིན་སྡོམ་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་པ་ཞིག་ཏུ་འགྱུར་ཞེ་ན། ཁ་ཅིག་ན་རེ་གཏན་དུ་གཏོང་བའི་བསམ་པ་མེད་པའི་ཕྱིར་སྡོམ་པ་མ་ཡིན་པར་འགྱུར་ཏེ། ལྕགས་ཀྱི་ཐུ་ལུམ་འབར་བ་ཡང་སྔོན་པོར་འགྱུར་བ་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 295]
གཞན་དག་ན་རེ་དེ་ཐོབ་པ༌[^227]ནི་རྣམ་པར་རིག་བྱེད་ལ་རག་ལུས་པའི་ཕྱིར་སྦྱོར་བ་མི་བྱེད་ན་མི་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 296 [HEADING]]
#### སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་མ་གཏོགས་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གཏོང་བ། ^1-20-4-0

[Block 297]
ཡང་སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་མ་གཏོགས་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཇི་ལྟར་གཏོང་ཞེ་ན།

[Block 298 [VERSE]]
བར་མ་ཤུགས་བླངས་བྱ་བ་དང་། །
དོན་ཚེ་རྩ་བ་ཆད་པ་ལས། །

[Block 299]
རབ་ཏུ་དང་བ་དང་། ཉོན་མོངས་པའི་ཤུགས་གང་གིས་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ༌[^228]འདི་འཕངས་པ་དེ་ཆད་པ༌[^229]དེ་ཡང་རྣམ་པར་འཆད་པར་འགྱུར་ཏེ། རྫ་མཁན་གྱི་འཁོར་ལོ་དང་། མདའི་འགྲོས་བཞིན་ནོ། །

[Block 300]
གལ་ཏེ་ཡང་དག་པར་བླངས་པ་འདིས་ཆོག་གོ་ཞེས་ཡང་དག་པར་ལེན་པ་གཏོང་ན་ཀུན་དུ་བླངས་པ་བཏང་བ་ལས་ཀྱང་རྣམ་པར་འཆད་པར་འགྱུར་རོ། །

[Block 301]
ཇི་ལྟར་བླངས་པ་བཞིན་མ་བྱས་པའི་བྱ་བ་རྣམ་པར་འཆད་པ༌[^230]ལས་ཀྱང་རྣམ་པར་འཆད་པར་འགྱུར་རོ། །

[Block 302]
དོན་རྣམ་པར་འཆད་པ་ལས་ཀྱང་རྣམ་པར་འཆད་པར་འགྱུར་རོ། །

[Block 303]
དོན་གང་ཞེ་ན། མཆོད་རྟེན་དང་། ཀུན་དགའ་ར་བ་དང་། གཙུག་ལག་ཁང་དང་། མལ་ཆ་དང་། སྟན་དང་། གོས༌[^231]དང་། རྒྱ་ལ་སོགས་པའི་དངོས་པོའོ། །

[Block 304]
ཚེ་ཆད་པ་ལས་ཀྱང་འཆད་པར་འགྱུར་རོ། །

[Block 305]
དགེ་བའི་རྩ་བ་རྣམས་འཆད་པ༌[^232]ལས་ཀྱང་རྣམ་པར་འཆད་པར་འགྱུར་ཏེ། གང་གི་ཚེ་དགེ་བའི་རྩ་བ་རྣམས་ཀུན་དུ་གཅོད་པར་རྩོམ་པ་ནའོ། །

[Block 306]
དེ་ལྟར་ན་རྒྱུ་དེ་དྲུག་གིས་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གཏོང་བར་འགྱུར་རོ། །

[Block 307 [HEADING]]
#### འདོད་གཏོགས་དགེ་བ་གཟུགས་མིན་གཏོང་བ། ^1-20-5-0

[Block 308 [VERSE]]
འདོད་གཏོགས་དགེ་བ་གཟུགས་མིན་ནི། །
རྩ་ཆད་གོང་དུ་སྐྱེས་པ་ལས། །

[Block 309]
འདོད་པ་ན་སྤྱོད་པའི་དགེ་བ་གཟུགས་ཅན་མ་ཡིན་པའི་རང་བཞིན་ནི་རྒྱུ་གཉིས་ཀྱིས་གཏོང་སྟེ།[^233] དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པའམ། གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་སུ་སྐྱེ་བ་ལས་སོ། །

[Block 310 [HEADING]]
#### ཉོན་མོངས་པ་ཅན་གཟུགས་མིན་རྣམ་པར་ཉམས་པ། ^1-20-6-0

[Block 311 [VERSE]]
ཉོན་མོངས་པ་ཅན་གཟུགས་མིན་ནི། །
གཉེན་པོ་སྐྱེས་པས་རྣམ༌[^234]ཉམས་འགྱུར། །

[Block 312]
ཉོན་མོངས་པ་ཅན་གཟུགས་ཅན་མ་ཡིན་པའི་རང་བཞིན་ཁམས་གསུམ་པ་ཐམས་ཅད་ནི་གཉེན་པོ་སྐྱེས་པས་རྣམ་པར་ཉམས་པར་འགྱུར་ཏེ། ཉེ་བའི་ཉོན་མོངས་པའི་རྣམ་པ་གང་གིས༌[^235]སྤོང་བའི་ལམ་གང༌[^236]ཡིན་པ་དེས་འདི་འཁོར་དང་བཅས་པ་ཡོངས་སུ་སྤོང་བར་བྱེད་ཀྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 313 [HEADING]]
### སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་ཡོད་པའི་སེམས་ཅན། ^1-21-0

[Block 314]
ཡང་སྡོམ་པ་མ་ཡིན་པ་ནི་སེམས་ཅན་གང་དག་ལ་ཡོད། སྡོམ་པ་ནི་གང་དག་ལ་ཡོད་ཅེ་ན།

[Block 315 [VERSE]]
ཟ་མ་མ་ནིང་སྒྲ་མི་སྙན། །
མཚན་གཉིས་མ་གཏོགས་མི་རྣམས་ལ། །

[Block 316]
སྡོམ་མིན། སྡོམ་པ་མ་ཡིན་པ་ནི་མིའི་འགྲོ་བ་ཁོ་ན་ལ་ཡོད་ཀྱི་གཞན་དག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 317]
དེ་ལ་ཡང་ཟ་མ་དང༌[^237]མ་ནིང་དང་མཚན་གཉིས་པ་དང་བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་ནི་མ་གཏོགས་སོ། །

[Block 318]
སྡོམ་པའང་དེ་བཞིན་ལ། ལྷ་ལའང་། སྡོམ་པ་ཡང་ཇི་སྐད་བཤད་པ་མ་གཏོགས་པ་མི་རྣམས་དང་། ལྷ་རྣམས་ལ་ཡོད་པས་འགྲོ་བ་གཉིས་ན་སྡོམ་པ་ཡོད་དོ། །

[Block 319]
ཟ་མ་ལ་སོགས་པ་ལ་སྡོམ་པ་མེད་དོ་ཞེས་བྱ་བ་ཇི་ལྟར་ཤེས་ཤེ་ན། མདོ་དང་འདུལ་བ་ལས་ཏེ།

[Block 320]
མདོ་ལས།
--- END BLOCKS ---
