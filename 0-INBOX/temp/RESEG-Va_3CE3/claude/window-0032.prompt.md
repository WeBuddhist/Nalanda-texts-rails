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
[Block 1121]
ད་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་གཟུགས་ལ་སོགས་པ་བཞིན་དུ་རྣམ་གྲངས་བཅུ་གཉིས་ཀྱིས་བསྟན་ཏེ། སེམས་ཅན་སྐྱེ་བ་མ་མཆིས་པའི་སླད་དུ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་སྐྱེ་བ་མེད་པའི་མཚན་ཉིད་ཀྱིས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་མཚན་ཉིད་མེད་པར་བལྟ་བར་བྱའོ། །

[Block 1122]
དེ་ལ་སེམས་ཅན་སྐྱེ་བ་མ་མཆིས་པའི་སླད་དུ་ཞེས་བྱ་བ་ནས། མཐོང་བ་པོ་སྐྱེ་བ་མ་མཆིས་པའི་སླད་དུ་ཞེས་བྱ་བའི་བར་དུ་ནི་གང་ཟག་ལ་བདག་མེད་པ་ལ་དགོངས་པའོ། །

[Block 1123]
གཟུགས་སྐྱེ་བ་མ་མཆིས་པའི་སླད་དུ་ཞེས་བྱ་བ་ནས་སངས་རྒྱས་ཀྱི་ཆོས་སྐྱེ་བ་མ་མཆིས་པའི་སླད་དུ་ཞེས་བྱ་བའི་བར་དུ་ནི་ཆོས་ལ་བདག་མེད་པ་ལ་དགོངས་པའོ། །

[Block 1124]
མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་མ་མཆིས་པ་ནི་རྟོགས་པ་མེད་པའོ། །

[Block 1125]
སེམས་ཅན་སྟོབས་དང་མི་ལྡན་པའི་སླད་དུ་ཞེས་བྱ་བ་ནི་ཉམ་ཆུང་བའམ་ཤེས་རབ་ཀྱི་སྟོབས་མེད་པའོ། །

[Block 1126]
ཆོས་བླུན་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1127]
དེ་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་བདག་ཉིད་ཆེ་ཞིང་རྒྱ་ཆེ་བ་ཐོས་ནས་གནས་བརྟན་ཤཱ་རིའི་བུ་དད་པ་སྐྱེས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཕྱིར་ཞུ་བ་རྣམ་པ་བཞི་བརྩམས་པ། བྱང་ཆུབ་སེམས་དཔའི་འཆི་འཕོ་དང་སྐྱེ་བ་དང་། ཡང་དག་པར་ཞུགས་པའི་དུས་ཀྱི་ཚད་དང་། བསྙེན་བཀུར་བྱས་པའི་དེ་བཞིན་གཤེགས་པའི་ཚད་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་སྤྱད་པའི་དུས་ཀྱི་ཚད་དོ། །

[Block 1128]
སྐབས་དེ་ཉིད་དུ་དམ་པའི་ཆོས་སྤོང་བའི་གཏམ་གྱི་སྐབས་དབྱེའོ།[^797] །དེ་ནས་ཡང་སྐབས་དེ་ཉིད་དུ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་མོས་པར་དཀའ་བའི་སྐབས་ཕྱེའོ། །

[Block 1129]
དེ་ནས་ཡང་མོས་པར་དཀའ་བ་དེ་བསྟན་པའི་ཕྱིར་བཅོམ་ལྡན་འདས་གང་དེ་ལྟར་མོས་པར་དཀའ་བའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དེ་ཇི་ཙམ་དུ་ཟབ་པ་ལགས་ཞེས་བྱ་བས་ཟབ་པའི་ཞུ་བ་ཞུས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་མ་བཅིངས་མ་གྲོལ་བར་བཤད་པ་དང་། རྣམ་པར་དག་པ་བཤད་པ་དང་། ཀུན་དུ་མཐའ་ཡས་པ་བཤད་པ་དང་། ཆགས་པ་དང་མ་ཆགས་པ་བཤད་པ་སྟེ། བཤད་པ་རྣམ་པ་བཞིའི་སྐབས་ཕྱེའོ། །

[Block 1130 [HEADING]]
##### མ་བཅིངས་མ་གྲོལ་བར་བཤད་པ། ^1-2-3-1-0

[Block 1131]
དེ་ལ་རབ་འབྱོར་གཟུགས་མ་བཅིངས་མ་གྲོལ་ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་གནས་སྐབས༌[^798]གང་ཡོངས་སུ་གྲུབ་པའི་ཆོས་ཉིད་ཀྱི་གཟུགས་སུ་སྣང་བ་དེ་འཁོར་བའི་གནས་སྐབས༌[^799]ན། དུས་དེ་སྲིད་དུ་ལས་དང་ཉོན་མོངས་པ་དང་། རྣམ་པར་སྨིན་པའི་བཅིང་བ༌[^800]ཐམས་ཅད་ཀྱིས་མ་བཅིངས་པས་མ་བཅིངས་ཞེས་བྱའོ། །

[Block 1132]
ཕྱིས་ཀྱང་ཡོངས་སུ་གྲུབ་པའི་གནས་སྐབས་ན་གྲོལ་བ་མེད་པའི་ཕྱིར་མ་གྲོལ་བ་ཞེས་བྱའོ། །

[Block 1133]
ཀུན་བརྟགས་པ་ཉིད་ལ་ནི་བཅིངས་པ་དང་གྲོལ་བ་ཞེས་བརྗོད་ཀྱི་ནམ་མཁའ་བཞིན་དུ་ཅིས་ཀྱང་མ་གོས་པ་འགྱུར་བ་མེད་པའི་ཆོས་ཉིད་ཀྱི་གཟུགས་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1134]
དེ་བས་ན་གཟུགས་དངོས་པོ་མེད་པའི་རང་བཞིན་ནི་གཟུགས་སོ་ཞེས་བྱ་བ་གསུངས་ཏེ། ཀུན་བརྟགས་པའི་གཟུགས་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་ཞེས་བྱ་བའི་ཐ༌[^801]ཚིག་གོ། །

[Block 1135]
དེ་བཞིན་དུ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་བར་གྱི་ཆོས་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1136]
ཡང་མ་བཅིངས་མ་གྲོལ་བ་འདི་ཉིད་གསལ་བར་བྱ་བའི་ཕྱིར་དུས་གསུམ་དང་སྦྱར་ཏེ་བསྟན་པ། རབ་འབྱོར་གཟུགས་ཀྱི་སྔོན་གྱི་མཐའ་མ་བཅིངས་མ་གྲོལ་བ་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་འཁོར་བ་ན་དྲི་མ་དང་བཅས་པ་མ་དག་པའི་གནས་སྐབས་ལ་སྔོན་གྱི་མཐའ་ཞེས་བྱའོ། །

[Block 1137]
ད་ལྟར་དག་པ་དང་མ་དག་པའི་གནས་སྐབས་ལ་ད་ལྟར་བྱུང་བ་ཞེས་བྱའོ། །

[Block 1138]
ཕྱིས་དག་པའི་གནས་སྐབས་ལ་ཕྱི་མའི་མཐའ་ཞེས་བྱའོ། །

[Block 1139]
སྔོན་གྱི་མཐའ་དངོས་པོ་མེད་པའི་རང་བཞིན་ནི་གཟུགས་སོ་ཞེས་བྱ་བས་ནི་དུས་གསུམ་ཆར་དུ་ཡང་མི་འགྱུར་བར་གནས་པའི་མཚན་ཉིད་ནི་དེ་བཞིན་ཉིད་ཡིན་ནོ་ཞེས་སྟོན་ཏེ། [^802]ཆོས་ཉིད་ནི་དུས་ལས་རྣམ་པར་གྲོལ་བའི་མཚན་ཉིད་མ་ཡིན་པར་བསྟན་ཏོ། །

[Block 1140 [HEADING]]
#### རྣམ་པར་དག་པ་བཤད་པ། ^1-2-4-0

[Block 1141]
དེ་ལྟར་མ་བཅིངས་མ་གྲོལ་བར་བཤད་པས་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་མེད་པར་བསྟན་ནས་ཡང་ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བ་མེད་པར་བསྟན་པའི་ཕྱིར་རྣམ་པར་དག་པ་བཤད་པར་བརྩམས་པ། གཟུགས་རྣམ་པར་དག་པ་གང་ཡིན་པ་དེ་ནི་འབྲས་བུ་རྣམ་པར་དག་པའོ་ཞེས་བྱ་བ་ནི།[^803] དེ་ལ་གཟུགས་ལ་སོགས་པ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་མཐར་ཐུག་པའི་ཆོས་རྣམས་ལ་བཅིངས་པ་མེད་པས་ཀུན་ནས་ཉོན་མོངས་པ་མེད་དོ། །

[Block 1142]
ཀུན་ནས་ཉོན་མོངས་པ་མེད་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་རྣམ་པར་དག་པའོ། །

[Block 1143]
ངོ་བོ་ཉིད་ཀྱིས་རྣམ་པར་དག་པའི་ཕྱིར་རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་ཀྱང་མེད་དེ། རང་བཞིན་གྱིས་རྣམ་པར་དག་པ་ལ་ནི་དོན་དམ་པར་རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་ཅི་ཡང་མི་བྱེད་དོ། །

[Block 1144]
དེ་བས་ན་ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བ་རྣམ་པར་མི་རྟོག་པ་ཡང་བྱིས་པ་རྣམས་ཀྱིས་བརྟགས་པ་ཉིད་དེ་ཡོངས་སུ་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 1145]
དེ་ལྟར་རྣམ་པ་གཅིག་གིས་མོས་པར་དཀའ་བ་བསྟན་ནས། ཡང་རྣམ་པར་དག་པའི་ཕྱིར་མོས་པར་དཀའ་བ་བསྟན་པ། དེ་ལ་གཟུགས་རྣམ་པར་དག་པ་གང་ཡིན་པ་དེ་ཉིད་འབྲས་བུ་རྣམ་པར་དག་པའོ་ཞེས་བྱ་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། བྱང་ཆུབ་ཀྱི་ཕྱོགས་ལ་སོགས་པ་རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་ཀྱི་འབྲས་བུར་གྱུར་པ་རྣམ་པར་དག་པ་ཞེས་བྱ་བ་གུད་ན་གང་ཡང་མེད་ཀྱི་གང་ཆོས་ཉིད་ཀྱི་གཟུགས་ཡོངས་སུ་གྲུབ་པ་ངོ་བོ་ཉིད་དུ་གྱུར་པ་རྟག་ཏུ་གནས་པ་རྣམ་པར་དག་པ་དེ་ཉིད་འབྲས་བུར་གྱུར་པའི་རྣམ་པར་དག་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1146]
དེ་བཞིན་དུ་ཆོས་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1147]
དེ་ལྟར་རྣམ་པར་དག་པའི་ངོ་བོ་ཉིད་བསྟན་ནས། དེའི་འོག་ཏུ་ཆོས་ཐམས་ཅད་ཀྱི་རྣམ་པར་དག་པ་ཡང་གཅིག་པའི་བདག་ཉིད་དེ་ཐ་དད་པ་མ་ཡིན་པར་བསྟན་པ། གཟུགས་རྣམ་པར་དག་པ་གང་ཡིན་པ་དེ་ཉིད་འབྲས་བུ་རྣམ་པར་དག་པའོ། །

[Block 1148]
འབྲས་བུ་རྣམ་པར་དག་པ་གང་ཡིན་པ་དེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་དག་པའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་དག་པ་གང་ཡིན་པ་དེ་གཟུགས་རྣམ་པར་དག་པའོ་ཞེས་བྱ་བ་སྟེ། དེ་ལ་གཟུགས་ཀྱི་ཆོས་ཉིད་ཀྱི་གནས་སྐབས་ལ༌[^804]ནི་གཟུགས་རྣམ་པར་དག་པ་ཞེས་བྱའོ། །

[Block 1149]
མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བ་ཡང་དག་པའི༌[^805]གནས་སྐབས་ལ་ནི་འབྲས་བུ་རྣམ་པར་དག་པ་ཞེས་བྱའོ། །

[Block 1150]
ཆོས་ཀྱི་སྐུའི་གནས་སྐབས་ལ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་དག་པ་ཞེས་བྱའོ། །

[Block 1151]
དེ་ལ་གཟུགས་རྣམ་པར་དག་པའི་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་འབྲས་བུ་རྣམ་པར་དག་པ་སྟེ། རྣམ་པར་གྲོལ་བའོ། །

[Block 1152]
རྣམ་པར་གྲོལ་བ་གང་ཡིན་པ་དེ་ཉིད་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་དག་པ་སྟེ་ཆོས་ཀྱི་སྐུའོ། །

[Block 1153]
ཆོས་ཀྱི་སྐུ་གང་ཡིན་པ་དེ་ཉིད་གཟུགས་རྣམ་པར་དག་པ་སྟེ། དེ་བཞིན་ཉིད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1154]
དེ་བས་ན་དེ་བཞིན་ཉིད་དང་། རྣམ་པར་གྲོལ་བ་དང་ཆོས་ཀྱི་སྐུ་ནི་དོན་དམ་པར་ཐ་དད་པ་མེད་དེ་གཅིག་གོ། །

[Block 1155]
དེ་བཞིན་དུ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་རྣམ་པར་དག་པའི་བར་དུ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1156]
དེ་ལྟར་ཆོས་ཐམས་ཅད་ཀྱི་རྣམ་པར་དག་པ་གཅིག་གོ་ཞེས་མཇུག་བསྡུས་ཏེ་བསྟན་པ། དེ་ལྟར་ན་གཟུགས་རྣམ་པར་དག་པ་དང་། འབྲས་བུ་རྣམ་པར་དག་པ་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་དག་པ་ནས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་བར་དུ་རྣམ་པར་དག་པ་འདི་དག་ནི་གཉིས་སུ་མེད་དེ་གཉིས་སུ་བྱར་མེད༌[^806]སོ་སོ་མ་ཡིན་ཐ་མི་དད་དོ་ཞེས་བྱ་བ་སྟེ། གཅིག་པའི་ཕྱིར་གཉིས་སུ་མེད་པའོ། །

[Block 1157]
ཐ་དད་དུ་དབྱེ་མི་ནུས་པའི་ཕྱིར་གཉིས་སུ་བྱར་མེད་པའོ། །

[Block 1158]
བྱེ་བྲག་མེད་པའི་ཕྱིར་སོ་སོ་མ་ཡིན་པའོ། །

[Block 1159]
བར་ཆད་མེད་པའི་ཕྱིར་རམ་རྟག་པའི་ཕྱིར་ཐ་མི་དད་པའོ། །

[Block 1160]
དེ་ལྟར་ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་དང་ཐུན་མོང་བའི་འབྲས་བུ་རྣམ་པར་དག་པ་བསྟན་ཏོ། །
--- END BLOCKS ---
