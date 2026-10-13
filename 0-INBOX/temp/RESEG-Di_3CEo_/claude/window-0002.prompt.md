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
[Block 71]
ཡང་འདུས་བྱས་དེ་དག་ཉིད། གང་དག་ཟག་བཅས་ཉེར་ལེན་པའི། །ཕུང་པོ་འང་དེ་དག །[^36]དེ་དག་ཉེ་བར་ལེན་པ་དག་ནི་ཉོན་མོངས་པ་རྣམས་ཏེ། དཔེར་ན་རྩྭ་དང་སྦུན་པའི་མེ་བཞིན་ནམ། དེ་དག་ལ་རག་ལུས་པའི་ཕྱིར་རྒྱལ་པོའི་མི་བཞིན་ནོ། །

[Block 72]
ཡང་ན་དེ་དག་ལས་ཉེ་བར་ལེན་པ་རྣམས་འབྱུང་བས་ཉེ་བར་ལེན་པའི་ཕུང་པོ་རྣམས་ཏེ། མེ་ཏོག་དང་འབྲས་བུའི་ཤིང་ལྗོན་པ་བཞིན་ནོ། །

[Block 73]
ཟག་པ་དང་བཅས་པའི་ཆོས་དེ་དག་ཉིད། འཐབ༌[^37]བཅས་ཀྱང་ཞེས་བརྗོད་དོ། །

[Block 74]
འཐད་པ༌[^38]ནི་ཉོན་མོངས་པ་རྣམས་ཏེ། བདག་དང་གཞན་ལ་གནོད་པའི་ཕྱིར་རོ། །

[Block 75]
དེ་དག་གིས་རྒྱས་པར་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་འཐབ་བཅས་དག་སྟེ།

[Block 76 [VERSE]]
ཟག་པ་དང་བཅས་པ་བཞིན་ནོ། །
སྡུག་བསྔལ་ཀུན་འབྱུང་འཇིག་རྟེན་དང་། །
ལྷ་གནས་སྲིད་པའང་དེ་དག་ཡིན། །

[Block 77]
འཕགས་པ་རྣམས་དང་མི་མཐུན་པའི་ཕྱིར་སྡུག་བསྔལ་ལོ། །

[Block 78]
འདི་ལས་སྡུག་བསྔལ་ཀུན་འབྱུང་བས་ན་ཀུན་འབྱུང་ངོ་། །སྐད་ཅིག་རེ་རེར་འཇིག་པས་ན་འཇིག་རྟེན་ནོ། །

[Block 79]
འདི་ལ་ལྟ་བ་རྒྱས་པར་འགྱུར་བའི་སྒོ་ནས་གནས་པས༌[^39]ན་ལྟ་བའི་གནས་སོ། །

[Block 80]
སྡུག་བསྔལ་ནི་ཀུན་འབྱུང་ལས་འབྱུང་པའི་ཕྱིར་སྲིད་པའོ། །

[Block 81]
དེ་ལྟར་ན་འདི་དག་ནི་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་ཀྱི་རྣམ་གྲངས་དོན་དང་མཐུན་པ་དག་གོ། །

[Block 82 [HEADING]]
### ཕུང་པོ་ལྔ། ^1-7-0

[Block 83 [HEADING]]
#### གཟུགས་ཀྱི་ཕུང་པོ། ^1-7-1-0

[Block 84]
གཟུགས་ལ་སོགས་པ་ཕུང་པོ་ལྔ། །ཞེས་གསུངས་ཏེ། དེ་ལ།

[Block 85 [HEADING]]
##### དབང་པོ་ལྔ། ^1-7-1-1-0

[Block 86 [VERSE]]
གཟུགས་ནི་དབང་པོ་ལྔ་དང་དོན། །
ལྔ་དང་རྣམ་རིག་བྱེད་མིན་ཉིད། །

[Block 87]
དབང་པོ་ལྔ་ནི་མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་ཀྱི་དབང་པོ་རྣམས་དང་། དོན་ལྔ་ནི་མིག་ལ་སོགས་པ་དབང་པོ་དེ་དག་ཉིད་ཀྱི་ཡུལ་གང་དག་ཡིན་པ་གཟུགས་དང་། སྒྲ་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་རྣམས་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྟེ། དེ་སྙེད་ཅིག་ནི་གཟུགས་ཀྱི་ཕུང་པོའོ། །

[Block 88]
དེ་ལ་གཟུགས་ལ་སོགས་པའི་དོན་གང་འདི་དག་སྨོས་པ། དེ་དག་རྣམས་ཀྱི་རྣམ་ཤེས་རྟེན། །མིག་ལ་སོགས༌[^40]གཟུགས་དང་རྣམས། གཟུགས་དང་སྒྲ་དང་། དྲི་དང་། རོ་དང་། རེག་བྱའི་རྣམ་པར་ཤེས་པ་རྣམས་ཀྱི་རྟེན་དུ་གྱུར་པའི་གཟུགས་དང་བའི་བདག་ཉིད་ལྔ་པོ་གང་དག་ཡིན་པ་དེ་དག་ནི་རིམ་པ་བཞིན་དུ་མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་དག་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 89]
དབང་པོ་ལྔ་བཤད་ཟིན་ཏོ། །

[Block 90 [HEADING]]
##### དོན་ལྔ། ^1-7-1-2-0

[Block 91]
དོན་ལྔ་བཤད་པར་བྱ་སྟེ། གཟུགས་རྣམ༌[^41]གཉིས་དང་། ཁ་དོག་དང་དབྱིབས་སོ། །

[Block 92]
ཡང་དེ་ཉིད། རྣམ་ཉི་ཤུ་ཞེས་བྱ་སྟེ། འདི་ལྟ་སྟེ། སྔོན་པོ་དང་། སེར་པོ་དང་། དམར་པོ་དང་། དཀར་པོ་དང་། རིང་པོ་དང་། ཐུང་ངུ་དང་། ལྷམ་པ་དང་། ཟླུམ་པོ་དང་། མཐོན་པོ་དང་། དམའ་བ་དང་། ཕྱ་ལེ་བ༌[^42]དང་། ཕྱ་ལེ་བ་མ་ཡིན་པ་དང་། སྤྲིན་དང་། དུ་བ་དང་། རྡུལ་དང་། ཁུག་རྣ་དང་། གྲིབ་མ་དང་། ཉི་མ་དང་། སྣང་བ་དང་། མུན་པའོ། །

[Block 93]
དེ་ལ་ཕྱ་ལེ་བ་ནི་དབྱིབས་མཉམ་པའོ། །

[Block 94]
ཕྱ་ལེ་བ་མ་ཡིན་པ་ནི་དབྱིབས་མི་མཉམ་པའོ། །

[Block 95]
ཁུག་རྣ་ནི་ལྷོ་བུར་རོ། །

[Block 96]
ཉི་མ་ནི་ཉི་མའི་འོད་དོ། །

[Block 97]
སྣང་བ་ནི་ཟླ་བ་དང་སྐར་མ་དང་། མེ་དང་སྨན་དང་ནོར་བུ་རྣམས་ཀྱི་འོད་དག་གོ། །

[Block 98]
གྲིབ་མ་ནི་གང་ན་གཟུགས་རྣམས་སྣང་པའོ། །

[Block 99]
བཟློག་པ་ནི་མུན་པའོ། །

[Block 100]
ལྷག་མ་ནི་བརྡ་ཕྲད་པར་སླ་བས་རྣམ་པར་མ་ཕྱེའོ། །

[Block 101]
སྒྲ་ནི་རྣམ་པ་བརྒྱད་ཡོད་དེ། [^43]ཟིན་པ་དང་མ་ཟིན་པའི་འབྱུང་བ་ཆེན་པོའི་རྒྱུ་ལས་བྱུང་བ་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པར་ཏེ་རྣམ་པ་བཞིའོ། །

[Block 102]
དེ་ཡང་ཡིད་དུ་འོང་བ་དང་ཡིད་དུ་མི་འོང་བའི་བྱེ་བྲག་གིས་རྣམ་པ་བརྒྱད་དུ་འགྱུར་རོ། །

[Block 103]
དེ་ལ་ཟིན་པའི་འབྱུང་བ་ཆེན་པོའི་རྒྱུ་ལས་བྱུང་བ་ནི༌[^44]ལག་པ་དང་ངག་གི་སྒྲའོ། །

[Block 104]
མ་ཟིན་པའི་འབྱུང་བ་ཆེན་པོའི་རྒྱུ་ལས་བྱུང་བ་ནི་རླུང་དང་ནགས་ཚལ་དང་ཆུ་བོའི་སྒྲའོ། །

[Block 105]
སེམས་ཅན་དུ་སྟོན་པ་ནི་ངག་གི་རྣམ་པར་རིག་བྱེད་ཀྱི་སྒྲའོ། །

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
--- END BLOCKS ---
