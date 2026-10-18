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
དབང་པོ་ལྔ་པོ་མིག་དང་རྣ་བ་དང་། །སྣ་དང་། ལྕེ་དང་། ལུས་ཀྱི་དབང་པོ་རྣམས་དང་། དོན་ལྔ་པོ་མིག་ལ་སོགས་པ་རྣམས་དེ་དག་ཉིད་ཀྱི་ཡུལ་གང་དག་ཡིན་པ་གཟུགས་དང་། སྒྲ་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་རྣམས་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྟེ་དེ་སྙེད་ཅིག་ནི་གཟུགས་ཀྱི་ཕུང་པོའོ། །

[Block 107 [HEADING]]
###### དབང་པོ་ལྔ། ^1-1-3-1-1-0

[Block 108]
དེ་ལ་གཟུགས་ལ་སོགས་པ་འདི་དག་སྨོས་པ་གང་དག་ཡིན་པ།

[Block 109 [VERSE]]
དེ་དག་རྣམས་ཀྱི་རྣམ་ཤེས་རྟེན། །
མིག་ལ་སོགས་གཟུགས་དང༌[^55]བ་རྣམས། །

[Block 110]
གཟུགས་དང་། སྒྲ་དང་། དྲི་དང་། རོ་དང་། རེག་བྱའི་རྣམ་པར་ཤེས་པ་རྣམས་ཀྱི་རྟེན་དུ་གྱུར་པ་གཟུགས་དང་བའི་བདག་ཉིད་ལྔ་པོ་གང་དག་ཡིན་པ་དེ་དག་ནི་གོ་རིམས་བཞིན་དུ་མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་དག་ཡིན་པར་རིག་པར་བྱ་སྟེ། བཅོམ་ལྡན་འདས་ཀྱིས་ཇི་སྐད་དུ་དགེ་སློང་མིག་ནི་ནང་གི་སྐྱེ་མཆེད་དེ། འབྱུང་བ་ཆེན་པོ་བཞི་དག་རྒྱུར་བྱས་པ་གཟུགས་དང་བའོ་ཞེས་རྒྱས་པར་གསུངས་པ་ལྟ་བུའོ། །

[Block 111]
ཡང་ན་མིག་ལ་སོགས་པ་འདི་དག་སྨོས་པ་གང་དག༌[^56]ཡིན་པ།

[Block 112 [VERSE]]
དེ་དག་རྣམས་ཀྱི་རྣམ་ཤེས་རྟེན། །
མིག་ལ་སོགས་གཟུགས་དང་བ་རྣམས། །

[Block 113]
མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་རྟེན་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ།

[Block 114]
དེ་ལྟར་བཤད་ན་རབ་ཏུ་བྱེད་པ་ལས།

[Block 115]
མིག་གི་དབང་པོ་གང་ཞེ་ན། མིག་གི་རྣམ་པར་ཤེས་པའི་རྟེན་གཟུགས་དང་བའོ་ཞེས་རྒྱས་པར་འབྱུང་བའི་གཞུང་དང་ཡང་མཐུན་པར་འགྱུར་རོ། །

[Block 116]
དབང་པོ་ལྔ་དག་བཤད་ཟིན་ཏོ། །

[Block 117 [HEADING]]
###### དོན་ལྔ། ^1-1-3-1-2-0

[Block 118 [HEADING]]
###### **གཟུགས་ཀྱི་སྐྱེ་མཆེད།** ^1-1-3-1-2-1-0

[Block 119]
དོན་ལྔ་བཤད་པར༌[^57]བྱ་སྟེ། དེ་ལ་རེ་ཞིག །གཟུགས་རྣམ་གཉིས་དང་། ཁ་དོག་དང་། དབྱིབས་སོ། །

[Block 120]
དེ་ལ་ཁ་དོག་ནི་རྣམ་པ་བཞི་སྟེ། སྔོན་པོ་ལ་སོགས་པའོ། །

[Block 121]
གཞན་དག་ནི་དེའི་བྱེ་བྲག་གོ། །

[Block 122]
དབྱིབས་ནི་རྣམ་པ་བརྒྱད་དེ། རིང་པོ་ལ་སོགས་པ་ནས་ཕྱ་ལེ་བ༌[^58]མ་ཡིན་པ་ལ་ཐུག་པའོ། །

[Block 123]
ཡང་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དེ་ཉིད། རྣམ་པ་ཉི་ཤུ་ཞེས་བྱ་སྟེ། འདི་ལྟ་སྟེ། སྔོན་པོ་དང་། སེར་པོ་དང་། དཀར་པོ༌[^59]དང་། དམར་པོ༌[^60]དང་། རིང་པོ་དང་། ཐུང་ངུ་དང་། ལྷམ་པ་དང་། ཟླུམ་པོ་དང་། མཐོན་པོ་དང་། དམའ་བ་དང་། ཕྱ་ལེ་བ་དང་། ཕྱ་ལེ་བ༌[^61]མ་ཡིན་པ་དང་། སྤྲིན་དང་། དུ་བ་དང་། རྡུལ་དང་། ཁུག་རྣ་དང་། གྲིབ་མ་དང་། ཉི་མ་དང་། སྣང་བ་དང་། མུན་པའོ། །

[Block 124]
ཁ་ཅིག་ནི་ནམ་མཁའ་ལ༌[^62]ཁ་དོག་གཅིག་དང་རྣམ་པ་ཉི་ཤུ་རྩ་གཅིག་ཏུ་འདོན་ཏོ། །

[Block 125]
དེ་ལ་ཕྱ་ལེ་བ་ནི་དབྱིབས་མཉམ༌[^63]པའོ། །

[Block 126]
ཕྱ་ལེ་བ་མ་ཡིན་པ་ནི་དབྱིབས་མི་མཉམ་པའོ། །

[Block 127]
[^64]ཁུག་རྣ་ནི་ལྷོ་བུར་རོ། །

[Block 128]
ཉི་མ་ནི་ཉི་མའི་འོད་དོ། །

[Block 129]
སྣང་བ་ནི་ཟླ་བ་དང་སྐར་མ་དང་མེ་དང་སྨན་དང་ནོར་བུ་རྣམས་ཀྱི་འོད་དག་གོ། །

[Block 130]
གྲིབ་མ་ནི་གང་ན་གཟུགས་རྣམས་སྣང་བའོ། །

[Block 131]
དེ་ལས༌[^65]བཟློག་པ་ནི་མུན་པའོ། །

[Block 132]
ལྷག་མ་ནི་བརྡ་ཕྲད་པར་སླ་བས་རྣམ་པར་མ་ཕྱེ་བའོ།[^66] །གཟུགས་ཀྱི་སྐྱེ་མཆེད་ཁ་དོག་ཏུ་ཡོད་ལ་དབྱིབས་སུ་མེད་པ་ཡང་ཡོད་དེ། སྔོན་པོ་དང་། སེར་པོ་དང་། དམར་པོ་དང་། དཀར་པོ་དང་། གྲིབ་མ་དང་། ཉི་མ་དང་། སྣང་བ་དང་། མུན་པ་ཞེས་བྱའོ།[^67] །དབྱིབས་སུ་ཡོད་ལ་ཁ་དོག་ཏུ་མེད་པ་ཡང་ཡོད་དེ། རིང་པོ་ལ་སོགས་པའི་ཕྱོགས་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་ཀྱི་ངོ་བོ་ཉིད་དོ། །

[Block 133]
གཉི་གར་ཡོད་པ་ཡང་ཡོད་དེ། གཟུགས་ཀྱི་སྐྱེ་མཆེད་ལྷག་མའོ། །

[Block 134]
གཞན་དག་ན་རེ། སྔོན་པོ་ལ་སོགས་པ་དང༌[^68]རིང་པོ་ལ་སོགས་པར་ཡོངས་སུ་ཆད་པར༌[^69]སྣང་བས་ན་ཉི་མ་དང་། སྣང་བ་ཁོ་ན་ཁ་དོག་ཏུ་ཡོད་དོ་ཞེས་ཟེར་རོ། །ཇི་ལྟར་ན་རྫས་གཅིག་ལ་གཉི་གར་ཡོད་ཅེ་ན། དེ་ལ་གཉི་ག་མངོན་པའི་ཕྱིར་ཏེ། ཡོད་པ་འདི་ནི་ཤེས་པའི་དོན་ཡིན་གྱི་ཡོད་པའི་དོན་ནི་མ་ཡིན་ནོ། །

[Block 135]
འོ་ན་ནི་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་ལའང་ཐལ་བར་འགྱུར་རོ། །

[Block 136]
གཟུགས་ཀྱི་སྐྱེ་མཆེད་བཤད་ཟིན་ཏོ། །

[Block 137 [HEADING]]
###### **སྒྲ།** ^1-1-3-1-2-2-0

[Block 138]
སྒྲ་ནི་རྣམ་པ་བརྒྱད་ཡོད་དེ། [^70]ཟིན་པ་དང་མ་ཟིན་པའི་འབྱུང་བ་ཆེན་པོའི་རྒྱུ་ལས་བྱུང་བ་སེམས་ཅན་དང་། སེམས་ཅན་མ་ཡིན་པར་སྟོན་པ་སྟེ་རྣམ་པ་བཞིའོ། །

[Block 139]
དེ་ཡང་ཡིད་དུ་འོང་བ་དང་ཡིད་དུ་མི་འོང་བའི་བྱེ་བྲག་གིས་རྣམ་པ་བརྒྱད་དུ་འགྱུར་རོ། །

[Block 140]
དེ་ལ་ཟིན་པའི་འབྱུང་བ་ཆེན་པོའི་རྒྱུ་ལས་བྱུང་བ་ནི་འདི་ལྟ་སྟེ། ལག་པ་དང་ངག་གི་སྒྲ་ལྟ་བུའོ། །

[Block 141]
མ་ཟིན་པའི་འབྱུང་བ་ཆེན་པོའི་རྒྱུ་ལས་བྱུང་བ་ནི་འདི་ལྟ་སྟེ། རླུང་དང་། ནགས་ཚལ་དང་། ཆུའི་སྒྲ་ལྟ་བུའོ། །

[Block 142]
སེམས་ཅན་དུ་སྟོན་པ་ནི༌[^71]ངག་གི་རྣམ་པར་རིག་བྱེད་ཀྱི་སྒྲའོ། །

[Block 143]
གཞན་ནི་སེམས་ཅན་དུ་སྟོན་པ་མ་ཡིན་པའོ། །

[Block 144]
གཞན་དག་ན་རེ་ཟིན་པ་དང་། མ་ཟིན་པའི་འབྱུང་བ་ཆེན་པོའི་རྒྱུ་ལས་བྱུང་བའི་སྒྲ་ཡང་ཡོད་དེ། དཔེར་ན་ལག་པ་དང་རྫ་རྔ་ཕྲད་པ་ལས་སྐྱེས་པ་ལྟ་བུའོ་ཞེས་ཟེར་ཏེ། [^72]དེ་ནི་འདི་ལྟར་ཁ་དོག་གི་རྡུལ་ཕྲ་རབ་གཅིག་ལས་བྱུང་བ་བཞི་ཚན་གཉིས་རྒྱུར་བྱས་པར་མི་འདོད་པ་དེ་བཞིན་དུ་མི་འདོད་པར་བྱའོ། །

[Block 145]
སྒྲ་བཤད་ཟིན་ཏོ། །
--- END BLOCKS ---
