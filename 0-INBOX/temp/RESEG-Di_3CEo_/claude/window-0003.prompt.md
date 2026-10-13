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
གཞན་ནི་སེམས་ཅན་དུ་སྟོན་པ་མ་ཡིན་པའོ། །

[Block 107]
གཞན་དུ་ཡང་སྒྲ་ཐམས་ཅད་གཉིས་གཉིས་སུ་བསྡུས་པའི་ཕྱིར་སྒྲ་ནི་རྣམ་པ་བཞི་རུ་བརྗོད་དོ།[^45] །

[Block 108]
སྒྲ་ནི་བཤད་ཟིན་ཏོ། །

[Block 109]
རོ་ནི་རྣམ་དྲུག །མངར་བ་དང་། སྐྱུར་བ་དང་། ལན་ཚྭ་བ༌[^46]དང་། ཚ་བ་དང་། ཁ་བ་དང་། བསྐ་བའི༌[^47]བྱེ་བྲག་གིས་སོ། །

[Block 110]
དྲི་རྣམ་བཞི། དྲི་ཞིམ་པ་དང་། དྲི་ང་བ་གཉིས་ལ། མཉམ་པ་དང་། མི་མཉམ་པའི་ཕྱིར་རོ། །

[Block 111]
རེག་བྱ་བཅུ་གཅིག་བདག་ཉིད་དོ། །

[Block 112]
འབྱུང་བ་བཞི་དག་དང་། འཇམ་པ་ཉིད་དང་། རྩུབ་པ་ཉིད་དང་། ལྕི་བ་ཉིད་དང་། ཡང་བ་ཉིད་དང་། གྲང་བ་དང་། བཀྲེས་པ་དང་། སྐོམ་པའོ། །

[Block 113]
དེ་ལ་འབྱུང་བ་རྣམས་ནི་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 114]
འཇམ་པ་ཉིད་ནི་མཉན་པའོ། །

[Block 115]
རྩུབ་པ་ཉིད་ནི་ཧྲུད་ཧྲུད་པོའོ།[^48] །

[Block 116]
ལྕི་བ་ཉིད་ནི་གང་གིས་ན་དངོས་པོ་རྣམས་འཇལ་བར་བྱེད་པའོ། །

[Block 117]
བཟློག་པ་ནི་ཡང་བ་ཉིད་དོ། །

[Block 118]
གྲང་བ་ནི་དྲོ་བ་འདོད་པར་བྱེད་པའོ། །

[Block 119]
བཀྲེས་པ་ནི་ཟས་འདོད་པར་བྱེད་པའོ། །

[Block 120]
སྐོམ་པའི༌[^49]བཏུང་བ་འདོད་པར་བྱེད་པའོ། །

[Block 121]
རྒྱུ་ལས་འབྲས་བུ་བརྟགས་པའི༌[^50]ཕྱིར་ཏེ། དཔེར་ན། སངས་རྒྱས་རྣམས་ནི་འབྱུང་བ་བདེ། །ཞེས་བྱ་བ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 122 [HEADING]]
##### རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ། ^1-7-1-3-0

[Block 123]
རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གང་ཞེ་ན།

[Block 124 [VERSE]]
གཡེངས་དང་སེམས་མེད་པ་ཡི་ཡང་། །
དགེ་དང་མི་དགེ་རྗེས་འབྲེལ་གང་། །
འབྱུང་བ་ཆེ་རྣམས་རྒྱུར་བྱས་པ། །
དེ་ནི་རྣམ་རིག་བྱེད་མིན་བརྗོད། །

[Block 125]
སེམས་གཡེངས་པ་ཞེས་བྱ་བ་ནི་དེ་ལས་གཞན་པའི་སེམས་པའི་ཡང་ཡིན་པའོ།[^51] །

[Block 126]
སེམས་མེད་པའི་ཡང་ཞེས་བྱ་བ་ནི། །འདུ་ཤེས་མེད་པ་དང་འགོག་པའི་སྙོམས་པར་འཇུག་པའི་ཡང་ཡིན་པའོ། །

[Block 127]
ཡང་ཞེས་བྱ་བའི་སྒྲས་ནི་མ་ཡེངས་པ༌[^52]དང་སེམས་དང་བཅས་པའི་ཡང་ཡིན་ནོ་ཞེས་བྱ་བར་ཡང་མངོན་ནོ། །

[Block 128]
དགེ་བ་དང་མི་དགེ་བ་ཞེས་བྱ་བ་ནི་དགེ་ལེགས་དང་དགེ་ལེགས་མ་ཡིན་པའོ། །

[Block 129]
རྗེས་འབྲེལ་གང་ཞེས་བྱ་བ་ནི་རྒྱུན་ཏོ། །

[Block 130]
ཐོབ་པའི་རྒྱུན་ཡང་འདི་ལྟ་བུ་ཡོད་པས་བྱེ་བྲག་ཏུ་བྱ་བའི་ཕྱིར། འབྱུང་བ་ཆེ་རྣམས་རྒྱུར་བྱས་པ། །ཞེས་བྱ་བ་བརྗོད་དོ། །

[Block 131]
རྒྱུར་བྱས་པའི་དོན་ནི་རྒྱུའི་དོན་ཏེ། སྐྱེད་པ་ལ་སོགས་པའི་རྒྱུའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 132]
དེ་ནི་རྣམ་རིག་བྱེད་མིན་ཞེས་བྱ་བ་ལ་དེ་ནི་ཞེས་བྱ་བའི་སྒྲ་ནི་དེའི་མིང་ཤེས་པར་བྱ་བའི་ཕྱིར༌[^53]ཏེ། གཟུགས་དང་བྱེད་པའི་རང་བཞིན་ཡིན་ཡང་རྣམ་པར་རིག་བྱེད་བཞིན་དུ་གཞན་ལ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའོ། །

[Block 133]
བརྗོད་ཅེས་བྱ་བ་ནི་སློབ་དཔོན་གྱི་ཚིག་ཡིན་པར་སྟོན་པའོ། །

[Block 134]
མདོར་ན་རྣམ་པར་རིག་བྱེད་དང་ཏིང་ངེ་འཛིན་ལས་བྱུང་བའི་གཟུགས་དགེ་བ་དང་མི་དགེ་བ་ནི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའོ། །

[Block 135 [HEADING]]
##### འབྱུང་བ་ཆེན་པོ། ^1-7-1-4-0

[Block 136 [VERSE]]
འབྱུང་བ་ཆེ་རྣམས་རྒྱུར༌[^54]བྱས་པ། །
ཞེས་གསུངས་པ་དེ་དག་གང་ཞེ་ན།
འབྱུང་བ་དག་ནི་ས་ཁམས་དང་། །
ཆུ་ཁམས༌[^55]མེ་ཁམས༌[^56]རླུང་ཁམས་རྣམས། །

[Block 137]
དེ་དག་ནི་རང་གི་མཚན་ཉིད་འཛིན་པ་དང་། རྒྱུར་བྱས་པའི་གཟུགས་དང་འཛིན་པའི་ཕྱིར་ཁམས་དག་གོ། །

[Block 138]
འདི་དག་གཟུགས་གཞན་ཐམས་ཅད་ཀྱི་རྟེན་ཉིད་དུ་རགས་པའི་ཕྱིར་ཆེན་པོ་ཉིད་དོ། །

[Block 139]
ཡང་ན་དེ་ལས་བྱུང་བའི་རང་བཞིན་ས་དང་། ཆུ་དང་། མེ་དང་རླུང་གི་ཕུང་པོ་དེ་དག་བྱ་བ་ལ་ཤས་ཆེ་བ་དག་ལ་དེ་རྣམས་ཆེན་པོར་གནས་པའི་ཕྱིར་རོ། །

[Block 140]
ཡང་ཁམས་དེ་དག་གི་ལས་གང་ཡང་དག་པར་འགྲུབ། རང་བཞིན་དག་ནི་ཅི་ཞེ་ན། འཛིན་པ་ལ་སོགས་ལས་སུ་འགྲུབ། །ཅེས་བྱ་བ་སྨོས་ཏེ། འདི་དག་ནི་གོ་རིམས་བཞིན་དུ་འཛིན་པ་དང་། སྡུད་པ༌[^57]དང་། སྨིན་པར་བྱེད་པ་དང་། རྒྱས་པར་བྱེད་པའི་ལས་ཡང་དག་པར་སྒྲུབ་པོ། །རྒྱས་པར་བྱེད་པ་ཡང་འཕེལ་བ་དང་། རྒྱས་པར་བྱེད་པའོ། །

[Block 141]
རང་བཞིན་ནི་གོ་རིམས་བཞིན་དུ།

[Block 142 [VERSE]]
སྲ་གཤེར་དྲོ་ཉིད་གཡོ་རྣམས་ཏེ། །
སྲ་བ་ནི་སའི་ཁམས་སོ། །
གཤེར་བ་ནི་ཆུའི་ཁམས་སོ། །
དྲོ་བ་ནི་མེའི་ཁམས་སོ། །

[Block 143]
གཡོ་བ་ནི་རླུང་གི་ཁམས་སོ། །

[Block 144]
འདིས་འབྱུང་བའི་ཡུལ་གཞན་དུ་སྐྱེད་པའི་ཕྱིར་གཡོ་བར༌[^58]བྱེད་དེ། སྒྲོན་མ་གཡོ་བ་བཞིན་དུ་གཡོ་བ་ཡིན་ནོ། །

[Block 145]
ཡང་ས་ལ་སོགས་པ་དང་སའི་ཁམས་ལ་སོགས་པ་ལ་བྱེ་བྲག་ཅི་ཡོད་ཅེ་ན།
--- END BLOCKS ---
