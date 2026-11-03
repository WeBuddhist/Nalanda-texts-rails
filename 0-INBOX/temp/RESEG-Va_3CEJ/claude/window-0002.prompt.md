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
[Block 71 [HEADING]]
#### འདུས་བྱས་ཀྱི་ཆོས་རྣམས། ^1-1-2-0

[Block 72]
ལམ་མ་གཏོགས་པ་འདུས་བྱས་རྣམས། །ཟག་བཅས་ཞེས་གང་སྨྲས་པའི་འདུས་བྱས་དེ་དག་གང་ཞེ་ན།

[Block 73 [VERSE]]
འདུས་བྱས་ཆོས་རྣམས་དེ་དག་ཀྱང་། །
གཟུགས་ལ་སོགས་པ་ཕུང་པོ་ལྔ། །

[Block 74]
གཟུགས་ཀྱི་ཕུང་པོ་དང་། ཚོར་བའི་ཕུང་པོ་དང་། འདུ་ཤེས་ཀྱི་ཕུང་པོ་དང་། འདུ་བྱེད་ཀྱི་ཕུང་པོ་དང་། རྣམ་པར་ཤེས་པའི་ཕུང་པོ་ཞེས་བྱ་བ་དེ་དག་ནི་འདུས་བྱས་ཀྱི་ཆོས་རྣམས་སོ། །

[Block 75]
རྐྱེན་རྣམས་འདུས་ཤིང་ཕྲད་ནས་བྱས་པ་དག་ནི་འདུས་བྱས་རྣམས་ཏེ། རྐྱེན་གཅིག་གིས་བསྐྱེད་པ་ནི་འགའ་ཡང་མེད་དོ། །

[Block 76]
དེ་དང་རིགས་མཐུན་པའི་ཕྱིར་མ་འོངས་པ་དག་ལ༌[^46]ཡང་མི་འགལ་ཏེ་འོ་མ་དང་ཤིང༌[^47]བཞིན་ནོ། །

[Block 77 [HEADING]]
##### འདུས་བྱས་ཀྱི་ཆོས་ཀྱི་རྣམ་གྲངས། ^1-1-2-1-0

[Block 78 [VERSE]]
དེ་དག་ཉིད་དུས་གཏམ་གཞི་དང་། །
ངེས་པར་འབྱུང་བ་གཞི༌[^48]དང་བཅས། །

[Block 79]
དེ་དག་ཉིད་ནི་འདུས་བྱས་ཀྱི་ཆོས་རྣམས་སོ། །

[Block 80]
སོང་བ་དང་འགྲོ་བ་དང་འགྲོ་བར་འགྱུར་བའི་ཕྱིར་རམ། མི་རྟག་པ་ཉིད་ཀྱིས་ཟ་བའི་ཕྱིར་དུས་རྣམས་སོ། །

[Block 81]
གཏམ་ནི་ངག་གོ། །

[Block 82]
དེའི་གཞི་ནི་མིང་སྟེ། དོན་དང་བཅས་པའི་གཞི་སྨོས་པའི་ཕྱིར་ན་འདུས་བྱས་ནི་གཏམ་གྱི་གཞི་ཞེས་བྱའོ། །

[Block 83]
དེ་ལྟ་མ་ཡིན་ན་རབ་ཏུ་བྱེད་པ་ལས།

[Block 84]
གཏམ་གྱི་གཞི་རྣམས་ནི་ཁམས་བཅོ་བརྒྱད་ཀྱིས་བསྡུས་སོ་ཞེས་འབྱུང་བའི་གཞུང་དང་འགལ་བར་འགྱུར་རོ། །

[Block 85]
གདོན་མི་ཟ་བར་འབྱུང་བ་ནི་ངེས་པར་འབྱུང་བ་སྟེ། འདུས་བྱས་ཐམས་ཅད་ཀྱི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 86]
དེ་འདི་དག་ལ་ཡོད་པས་ངེས་པར་འབྱུང་བཅས་དག་གོ། །

[Block 87]
རྒྱུ་དང་བཅས་པའི་ཕྱིར་གཞི་དང་བཅས་པ་དག་སྟེ། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ༌[^49]གཞི་ཞེས་བྱ་བའི་སྒྲ་ནི་རྒྱུའི་ཚིག་ཡིན་ལོ།[^50] དེ་ལྟར་ན་དེ་དག་ནི་འདུས་བྱས་ཀྱི་ཆོས་ཀྱི་རྣམ་གྲངས་དག་ཡིན་ནོ། །

[Block 88 [HEADING]]
##### ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་ཀྱི་རྣམ་གྲངས། ^1-1-2-2-0

[Block 89]
ཡང་འདུས་བྱས་དེ་དག་ཉིད། གང་དག་ཟག་བཅས་ཉེར་ལེན་པའི། །ཕུང་པོའང་དེ་དག །འདིས་ཅི་ཞིག་གྲུབ་པར་འགྱུར་ཞེ་ན། ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་གང་དག་ཡིན་པ་དེ་དག་ནི་ཕུང་པོ་ཡང་ཡིན་ནོ།[^51] །ཕུང་པོ་དག་ཁོ་ན་ཡིན་ལ་ཉེ་བར་ལེན་པའི་ཕུང་པོ་མ་ཡིན་པ་དག་ཀྱང་ཡོད་དེ། འདུ་བྱེད་ཟག་པ་མེད་པ་རྣམས་སོ། །

[Block 90]
དེ་ལ་ཉེར་བར་ལེན་པ་དག་ནི་ཉོན་མོངས་པ་རྣམས་སོ། །

[Block 91]
དེ་དག་ལས་བྱུང་བའི་ཕྱིར་ཉེ་བར་ལེན་པའི་ཕུང་པོ་དག་སྟེ། དཔེར་ན་རྩྭ་དང་སོག་མའི་མེ་བཞིན་པ་འམ། དེ་དག་ལ་རག་ལུས་པའི་ཕྱིར་རྒྱལ་པོའི་མི་བཞིན་ནོ། །

[Block 92]
ཡང་ན་དེ་དག་ལས་ཉེ་བར་ལེན་པ་རྣམས་འབྱུང་བས་ཉེ་བར་ལེན་པའི་ཕུང་པོ་རྣམས་ཏེ། མེ་ཏོག་དང་འབྲས་བུའི་ཤིང་ལྗོན་པ་བཞིན་ནོ། །

[Block 93]
ཟག་པ་དང་བཅས་པའི་ཆོས་དེ་དག་ཉིད། འཐབ་བཅས་ཀྱང་ཞེས་བྱའོ། །

[Block 94]
འཐབ་པ་ནི་ཉོན་མོངས་པ་རྣམས་ཏེ། བདག་དང་གཞན་ལ་གནོད་པའི་ཕྱིར་རོ། །

[Block 95]
དེ་དག་གིས་རྒྱས་པར་བྱས་པའི་ཕྱིར་འཐབ་བཅས་དག་སྟེ་ཟག་པ་དང་བཅས་པ་བཞིན་ནོ། །

[Block 96 [VERSE]]
སྡུག་བསྔལ་ཀུན་འབྱུང་འཇིག་རྟེན་དང་། །
ལྷ༌[^52]གནས་སྲིད་པའང་དེ་དག་ཡིན། །

[Block 97]
འཕགས་པ་རྣམས་དང་མི་མཐུན་པའི་ཕྱིར་སྡུག་བསྔལ་ལོ། །

[Block 98]
འདི་ལས༌[^53]སྡུག་བསྔལ་ཀུན་འབྱུང་བས་ཀུན་འབྱུང་བའོ། །

[Block 99]
འཇིག་པས་ན༌[^54]འཇིག་རྟེན་ནོ། །

[Block 100]
འདི་ལ་ལྟ་བས་རྒྱས་པར་འགྱུར་བའི་སྒོ་ནས་གནས་པས་ན་ལྟ་བའི་གནས་སོ། །

[Block 101]
འབྱུང་བས་ན་སྲིད་པ་སྟེ། དེ་ལྟར་ན་འདི་དག་ནི་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་ཀྱི་རྣམ་གྲངས་དོན་དང་མཐུན་པ་དག་གོ། །

[Block 102 [HEADING]]
#### གཟུགས་ལ་སོགས་པ་ཕུང་པོ་ལྔ། ^1-1-3-0

[Block 103]
གཟུགས་ལ་སོགས་པ་ཕུང་པོ་ལྔ། །ཞེས་སྨྲས་པ་དེ་ལ།

[Block 104 [HEADING]]
##### གཟུགས་ཀྱི་ཕུང་པོ། ^1-1-3-1-0

[Block 105 [VERSE]]
གཟུགས་ནི་དབང་པོ་ལྔ་དང་དོན། །
ལྔ་དང་རྣམ་རིག་བྱེད་མིན་ཉིད། །

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
--- END BLOCKS ---
