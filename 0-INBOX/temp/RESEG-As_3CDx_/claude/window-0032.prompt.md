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
དེ་དག་གི་གནས་གང་ཞེ་ན། ཀུན་གཞིའི༌[^895]རྣམ་པར་ཤེས་པ་དང་། ཉོན་མོངས་པ་ཅན་གྱི༌[^896]ཡིད་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་གནས་ནི་གཉིས་ཏེ། ས་བོན་གྱི་གནས་ནི་ཀུན་གཞིའི༌[^897]རྣམ་པར་ཤེས་པ་ཉིད་དོ། །

[Block 1122]
དེ་མ་ཐག་པའི་གནས་ནི་ཡིད༌[^898]དོ། །

[Block 1123]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་གནས་ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཀྱང་ཡིན་ཏེ། འདི་ལྟར་དེ་མ་འགགས་ན་རྣམ་པར་རིག་པའི་འཆིང་བ་མི་འགྲོལ༌[^899]ལ། འགགས་ན་དེ་འགྲོལ་བའི་ཕྱིར་རོ། །

[Block 1124]
སྒོ་ལྔའི་རྣམ་པར་ཤེས་པའི་གནས་ནི་གསུམ་སྟེ། དབང་པོ་ནི་ལྷན་ཅིག་བྱུང་བའི་གནས་སོ། །

[Block 1125]
ཡིད་ནི་དེ་མ་ཐག་པའི་གནས་སོ། །

[Block 1126]
ས་བོན་ཐམས་ཅད་པ་ལུས་ལེན་པར་བྱེད་པ་རྣམ་པར་སྨིན་པར་བསྡུས་པ་ཀུན་གཞིའི༌[^900]རྣམ་པར་ཤེས་པ་ནི་ས་བོན་གྱི་གནས་སོ། །

[Block 1127 [HEADING]]
###### དམིགས་པ། ^4-2-1-1-3-0

[Block 1128]
དེ་དག་གི་དམིགས་པ་གང་ཞེ་ན། ཀུན་གཞིའི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ནང་གི་ལེན་པ་དང་། ཕྱི་རོལ་སྣོད་ཡོངས་སུ་མ་ཆད་པའོ། །

[Block 1129]
ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཀྱི་དམིགས་པ་ནི་ཀུན་གཞི་ལ་བདག་གོ་སྙམ་དུ་དམིགས་པའོ། །

[Block 1130]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ནི་ཆོས་ཐམས་ཅད་དེ། དེ་ཡང་རང་བཞིན་གྱི་ཡུལ་དང་། རང་དང་། སྤྱིའི་མཚན་ཉིད་དང་། དུས་གསུམ་དང་སྐད་ཅིག་གི༌[^901]རྒྱུན་གྱིས་བསྡུས་པ་དག༌[^902]གོ། །

[Block 1131]
སྒོ་ལྔའི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ནི་ཐམས་ཅད་ཀྱང་ད་ལྟར་བྱུང་བའི་དུས་དང་། སྐད་ཅིག་གཅིག་གིས་བསྡུས་པ་རང་གི་མཚན་ཉིད་ཤ་སྟག་སྟེ། དེ་ལ་མིག་གི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ནི་གཟུགས་བསྟན་དུ་ཡོད་ལ་ཐོགས་པ་དང་བཅས་པའོ། །

[Block 1132]
རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་ཀྱི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ནི་སྒྲ་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་བསྟན་དུ་མེད་ལ་ཐོགས་པ་དང་བཅས་པ་དག་གོ། །

[Block 1133 [HEADING]]
###### གྲོགས། ^4-2-1-1-4-0

[Block 1134]
དེ་དག་གི་གྲོགས་གང་ཞེ་ན། སེམས་ལས་བྱུང་བའི་ཆོས་དེ་དག་དང་། ལྷན་ཅིག་འབྱུང་ཞིང་མཚུངས་པར་ལྡན་པ་རྣམས་སོ། །

[Block 1135 [HEADING]]
###### ལས། ^4-2-1-1-5-0

[Block 1136]
དེ་དག་གི་ལས་གང་ཞེ་ན། མདོར་བསྡུ་ན་རྣམ་པ་བཞི་སྟེ། སྣོད་རྣམ་པར་རིག་པ་དང་། གནས་རྣམ་པར་རིག་པ་དང་། བདག་གོ་སྙམ་དུ་རྣམ་པར་རིག་པ་དང་། ཡུལ་རྣམ་པར་རིག་པའོ། །

[Block 1137]
དེ་ལ་དང་པོ་གཉིས་ནི་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པའི་ལས་ཡིན་ཏེ། དེ་ནི་རྟག་ཏུ་དམིགས་པ་རྣམ་པ་གཉིས་པའི༌[^903]ཕྱི་རོལ་གྱི་སྣོད་རྣམ་པ་ཡོངས་སུ་མ་ཆད་པ༌[^904]དང་། ནང་གི་ལེན་པ་རྣམ་པར་རིག་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1138]
གསུམ་པ་ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཀྱི་ལས་ཡིན་ཏེ། དེ་ནི་འཆིང་བར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1139]
ཐ་མ་ནི་འཇུག་པའི་རྣམ་པར་ཤེས་པ་དྲུག་གི་ལས་ཡིན་ཏེ། དེ་དག་ནི་དམིགས་པ་རྣམ་པར་རིག་པར་བྱེད་པས་ཉེ་བར་གནས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1140]
འཇུག་པའི་རྣམ་པར་ཤེས་པ་རྣམས་ཀྱི་ལས་ཀྱང་རབ་ཏུ་དབྱེ་ན་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ལས་ནི་རང་དང་གཞན་གྱི་ཡུལ་གྱི་དམིགས་པ་རྣམ་པར་རིག་པར་བྱེད་པ་དང་། རང་དང་སྤྱིའི་མཚན་ཉིད་རྣམ་པར་རིག་པར་བྱེད་པ་དང་། དུས་གསུམ་རྣམ་པར་རིག་པར་བྱེད་པ་དང་། སྐད་ཅིག་གི་རྒྱུན་རྣམ་པར་རིག་པར་བྱེད་པ་དང་། དགེ་བ་དང་མི་དགེ་བའི་ཆོས་རྣམས་དང་ལས་རྣམ་པར་འཇུག་ཅིང་རྗེས་སུ་འཇུག་པར་བྱེད་པ་དང་། དེ་ལས་གཞན་པའི་རྣམ་པར་ཤེས་པའི་ཚོགས་རྣམས་ཀྱི༌[^905]སྡུག་པ་དང་མི་སྡུག་པའི་འབྲས་བུ་ཡང་ཡོངས་སུ་འཛིན་ཏེ། དེའི་རྒྱུ་ལས་བྱུང་བ་རྒྱུ་མཐུན་པ་ཀུན་ནས་སློང་བའི་ཕྱིར་རོ། །

[Block 1141]
དེ་དག་ནི་རྣམ་པར་ཤེས་པའི་ཚོགས་གཞན་དག་དང་ཐུན་མོང་དང་ཐུན་མོང་མ་ཡིན་པའི་ལས་ཡིན་ནོ། །

[Block 1142]
ཡང་དེ་ལས་གཞན་པའི་རྣམ་པར་ཤེས་པའི་ཚོགས་རྣམས་ལས་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་ཁྱད་པར་དུ་གྱུར་པའི་ལས་ནི་རྣམ་པ་བཅུ་བཞི་སྟེ། དམིགས་པ་ལ་རྣམ་པར་རྟོག་པ་དང་། དམིགས་པ་ལ་ཉེ་བར་སེམས་པ་དང་། ར་རོ་བར་བྱེད་པ་དང་། སྨྱོ་བར་བྱེད་པ་དང་། གཉིད་ལོག་པར་བྱེད་པ་དང་། སད་པར་བྱེད་པ་དང་། བརྒྱལ་བར་བྱེད་པ་དང་། བརྒྱལ་བ་ལས་སངས་པར་བྱེད་པ་དང་། ལུས་དང་ངག་གི་ལས་འཇུག་པར་བྱེད་པ་དང་། འདོད་ཆགས་ལས་བྲལ༌[^906]བ་ལས་ཡོངས་སུ་ཉམས་པར་བྱེད་པ་དང་། དགེ་བའི་རྩ་བ་རྣམས་རྒྱུན་མི་འཆད་པར་བྱེད་པ་དང་། དགེ་བའི་རྩ་བ་རྣམས་མཚམས་སྦྱོར་བར་བྱེད་པ་དང་། འཆི་འཕོ་དང་སྐྱེ་བར་བྱེད་པའོ། །

[Block 1143]
སྒོ་ལྔའི་རྣམ་པར་ཤེས་པ་རྣམས་ཀྱི་ལས་ནི་མདོར་བསྡུ་ན་རྣམ་པ་དྲུག་ཏུ་བལྟ་བར་བྱ་སྟེ། རང་གི་ཡུལ་རྣམ་པར་རིག་པར་བྱེད་པ་དང་། རང་གི་མཚན་ཉིད་རྣམ་པར་རིག་པར་བྱེད་པ་དང་། ད་ལྟར་གྱི་དུས་རྣམ་པར་རིག་པར་བྱེད་པ་དང་། སྐད་ཅིག་གཅིག་གི་རྣམ་པར་རིག་པར་བྱེད་པ་དང་། རྣམ་པ་གཉིས་ཀྱིས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་རྗེས་སུ་འཇུག་སྟེ། དགེ་བའི༌[^907]དང་ཉོན་མོངས་པ་ཅན་གྱི་རྗེས་སུ་འཇུག་པ་དང་། ལས་ཀུན་ནས་སློང་བའི་རྗེས་སུ་འཇུག་པ་དང་། སྡུག་པ་དང་མི་སྡུག་པའི་འབྲས་བུ་ཡོངས་སུ་འཛིན་པར་བྱེད་པའོ། །

[Block 1144 [HEADING]]
###### ཀུན་གཞིའི་རྣམ་པར་ཤེས་པའི་ཡོད་པ་ཉིད། ^4-2-1-1-6-0

[Block 1145]
དེ་ལ་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པའི་ཡོད་པ་ཉིད་དང་། རབ་ཏུ་དབྱེ་བ་ཇི་ལྟར་རིག་པར་བྱ་ཞེ་ན། ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ༌[^908]ཡོད་པ་ཉིད་ནི་རྣམ་པ་བརྒྱད་ཀྱིས༌[^909]ཁོང་དུ་ཆུད་པར་བྱས་ལ། དེའི་རབ་ཏུ་དབྱེ་བ་ནི་འཇུག་པ་དང་། ལྡོག་པ་རྣམ་པར་གཞག་པས་རིག་པར་བྱའོ། །

[Block 1146]
དེ་ལ་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པའི་ཡོད་པ་ཉིད་རྣམ་པ་བརྒྱད་ཀྱིས་ཁོང་དུ་ཆུད་པར་བྱ་བ༌[^910]གང་ཞེ་ན། འདི་ལྟ་སྟེ་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་མེད་ན་ལུས་ལེན་པ་མི་སྲིད་པ་དང་།

[Block 1147]
དང་པོ་འཇུག་པ་མི་སྲིད་པ་དང་། གསལ་བར་འཇུག་པ་མི་སྲིད་པ་དང་། ས་བོན་ཉིད་མི་སྲིད་པ་དང་། ལས་མི་སྲིད་པ་དང་། ལུས་ཀྱི་ཚོར་བ་མི་སྲིད་པ་དང་། སེམས་མེད་པའི་སྙོམས་པར་འཇུག་པ་མི་སྲིད་པ་དང་། རྣམ་པར་ཤེས་པའི་འཆི་འཕོ་མི་སྲིད་པས་སོ། །

[Block 1148 [HEADING]]
###### **ལུས་ལེན་པ་མི་སྲིད་པ།** ^4-2-1-1-6-1-0

[Block 1149]
དེ་ལ་ཇི་ལྟར་ན༌[^911]ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་མེད་ན་ལུས་ལེན་པ་མི་སྲིད་པར་འགྱུར་ཞེ་ན། རྒྱུ་རྣམ་པ་ལྔ་སྟེ། འདི་ལྟ་སྟེ་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་ནི། སྔོན་ལས་མངོན་པར་འདུ་བྱས་པའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་པས་དེས་ལུས་ལེན་པར་བྱེད་ཀྱི་འཇུག་པའི་རྣམ་པར་ཤེས་པ་རྣམས་ནི་ད་ལྟར་གྱི་རྐྱེན་ལས་བྱུང་བ་ཡིན་པས་དེ་དག་ནི་ལུས་ལེན་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ནི་རྒྱུ་དང་པོ་ཡིན་ནོ། །

[Block 1150]
གཞན་ཡང་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་ནི་ལུང་དུ་མ་བསྟན་པ་ཡིན་པས་དེས་ལུས་ལེན་པར་བྱེད་པ་ཡིན་གྱི་འཇུག་པའི་རྣམ་པར་ཤེས་པ་རྣམས་ནི་དགེ་བ་དང་མི་དགེ་བར་སྣང་བས་དེ་དག་ནི་ལུས་ལེན་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ནི་རྒྱུ་གཉིས་པ་ཡིན་ནོ། །

[Block 1151]
གཞན་ཡང་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་ནི་ལུང་དུ་མ་བསྟན་པ་རྣམ་པར་སྨིན་པས་བསྡུས་པའི་རིགས་ཡིན་པས་དེས་ལུས་ལེན་པར་བྱེད་པ་ཡིན་གྱི། འཇུག་པའི་རྣམ་པར་ཤེས་པ་རྣམས་ལ་ནི་ལུང་དུ་མ་བསྟན་པ་རྣམ་པར་སྨིན་པས་བསྡུས་པའི་རིགས་གང་ཡིན་པ་དེ་ནི༌[^912]དམིགས་པས། དེ་དག་ནི་ལུས་ལེན་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ནི་རྒྱུ་གསུམ་པ་ཡིན་ནོ། །

[Block 1152]
གཞན་ཡང་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་ནི་ལུས་ཐམས་ཅད་ལ་ཁྱབ་པར་གནས་པས། དེས་ལུས་ལེན་པར་བྱེད་པ་ཡིན་གྱི། འཇུག་པའི་རྣམ་པར་ཤེས་པ་རྣམས་ནི་གནས་ངེས་པ་ལས་སོ་སོར་འབྱུང་སྟེ། དེ་ལ་རྣམ་པར་ཤེས་པ་གནས་གང་དང་གང་ནས་འབྱུང་བ་དེ་ཉིད་དེས་ཟིན་པར་འགྱུར་གྱི། གནས་གང༌[^913]ནས་རྣམ་པར་ཤེས་པ་མ་བྱུང་བའི་གནས་དེ་མ་ཟིན་པས། དེ་དག་ནི་ལུས་ལེན་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ནི་རྒྱུ་བཞི་པ༌[^914]ཡིན་ནོ། །

[Block 1153]
གཞན་ཡང་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་ནི་དང་པོའི་ལེན་པའི་སྐད་ཅིག་མའི་རྒྱུན་གྱིས་ལུས་ཅིག་ཅར་ལེན་པ་ཡིན་གྱི། འཇུག་པའི་རྣམ་པར་ཤེས་པ་རྣམས་ནི་ལན་འགའ་འབྱུང་ཞིང་ལན་འགའ་མི་འབྱུང་བས་གལ་ཏེ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མེད་ན་ཡང་དང་ཡང་དུ་ལུས་ལེན་པའི་སྐྱོན་དུ་འགྱུར་ཏེ། དེ་ནི་རྒྱུ་ལྔ་པ་ཡིན་ནོ། །

[Block 1154]
དེ་ལྟར་ན་ད་ལྟར་གྱི་རྐྱེན་ལས་བྱུང་བ་དང་། དགེ་བ་དང་མི་དགེ་བ་ཡིན་པ་དང་། རྣམ་པར་སྨིན་པའི་རིགས་མ་ཡིན་པ་དང་། གནས་ངེས་པ་དང་། ཡང་དང་ཡང༌[^915]ལུས་ལེན་པའི་སྐྱོན་དུ་འགྱུར་བས་ཀྱང་གལ་ཏེ་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་མེད་ན་ལུས་ལེན་པ་མི་སྲིད་པས་སྐྱོན་དུ་འགྱུར་བས། དེའི་ཕྱིར་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་ཡོད་པར་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 1155 [HEADING]]
###### **དང་པོ་འཇུག་པ་མི་སྲིད་པ།** ^4-2-1-1-6-2-0

[Block 1156]
ཇི་ལྟར་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་མེད་ན་དང་པོར་འཇུག་པར་མི་སྲིད་པར་འགྱུར་ཞེ་ན། ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་ཡོད་ན་འཇུག་པའི་རྣམ་པར་ཤེས་པ་རྣམས་དང་། ལྷན་ཅིག་གི་དངོས་པོས་འཇུག་ཅིང་རྣམ་པར་ཤེས་པ་གཉིས་སམ་གསུམ་མམ། བརྒྱད་ཅར་ལྷན་ཅིག་འབྱུང་བར་འགྱུར་བ་དེ་མི་འདོད་པས་ཀུན་གཞི་ཡང་མེད་ལ། འཇུག་པའི་རྣམ་པར་ཤེས་པ་དྲུག་ཀྱང་ལྷན་ཅིག་མི་འབྱུང་ཞིང་གང་ཡང་རུང་བ་སྔ་ཕྱིར་རིམ་གྱིས་འབྱུང་ངོ་ཞེས་ཟེར་བ་དེ་མི་རུང་སྟེ། གང་གི་ཚེ་རྣམ་པར་ཤེས་པ་དྲུག་ཅར་གྱི་རྐྱེན་དུས་གཅིག༌[^916]ཁོ་ནར་ཉེ་བར་གནས་པར་གྱུར་པའི་ཚེ།

[Block 1157]
དང་པོ་གཅིག༌[^917]འབྱུང་ཞིང་གཞན་ཡང་རིམ་གྱིས་འབྱུང་ཞེས་བྱར་རྐྱེན་ཚོགས་པར་འདྲ་བས་མི་རུང་སྟེ། རྣམ་པར་ཤེས་པ་རྣམས་ལྷན་ཅིག་འབྱུང་བས་ན་དེའི་ཕྱིར་ཡང་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་ཡོད་པར་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 1158 [HEADING]]
###### **གསལ་བར་འཇུག་པ་མི་སྲིད་པ།** ^4-2-1-1-6-3-0

[Block 1159]
ཇི་ལྟར་ན་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་མེད་ན་གསལ་བར་འཇུག་པ་མི་སྲིད་པར་འགྱུར་ཞེ་ན། ཀུན་གཞི་མེད་ན་རྣམ་པར་ཤེས་པ་ལྷན་ཅིག་གི་དངོས་པོས་འཇུག་པ་ཡང༌[^918]མེད་པས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ད་ལྟར་གྱི་ཡུལ་ལ་གསལ་བར་འཇུག་ཅེས་བྱའོ། །

[Block 1160]
མིག་ལ་སོགས་པ་ད་ལྟར་གྱི་ཡུལ་ལ་གསལ་བར་འཇུག་པ་དང་། དུས་གཅིག༌[^919]ཏུ་འགྱུར་བས་མི་རུང་བའི་རིགས་ནས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ད་ལྟར་གྱི་ཡུལ་ལ་གསལ་བར་འཇུག་པས་ལྷན་ཅིག་གི་དངོས་པོས་འཇུག་པ་ཡོད་པས་ན༌[^920]དེའི་ཕྱིར་ཡང་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་ཡོད་པར་ཁོང་དུ་ཆུད་པར་བྱའོ། །
--- END BLOCKS ---
