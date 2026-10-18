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
[Block 1156]
རེ་ཞིག༌[^754]ལྷག་པའི་བསམ་པ་དག་པ་དེ་དག༌[^755]ཉིད་ཀྱི་མཚན་ཉིད་གང་ཡིན། གང་གིས་དེ་དག་ཡོངས་སུ་བཟུང་བ་ཡིན་ཞེ་ན། གང་གི་རྗེས་ཐོགས་སུ་ཚིགས་སུ་བཅད་པ་དག་གིས་དེའི་མཚན་ཉིད་སྟོན་པར་བྱེད་དེ། དེ་ལ་རེ་ཞིག་མོས་པས་སྤྱོད་པའི་ས་ལ་ཚོགས་ལེགས་པར་བསགས་པ་དང་། དཀར་པོའི་ཆོས་རྣམས་ཀུན་རྫོགས་པ༌[^756]ཉིད་དོ། །

[Block 1157]
བཟོད༌[^757]རྣོན་ཐོབ་དང་ཞེས་བྱ་བ་ནི་ཆུང་ངུ་ལ་སོགས་པ་བཟོད་པ༌[^758]རྣམ་པ་གསུམ་ལས་བཟོད་པའི་མཆོག་ལ་གནས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1158 [HEADING]]
#### དམིགས་པ། ^4-1-1-0

[Block 1159]
གང་ལ་དམིགས་ནས་དག་པར་འགྱུར་བ་དེ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཐེག་ཆེན་ལ་ཞེས་བྱ་བ་སྟེ། གང་དུ་ཞེ་ན། ཟབ་ཅིང་རྒྱ་ཆེ་བསྟན་པ་ལའོ། །

[Block 1160]
དེ་ཉིད་ནི་རང་གི་ཐེག་པ་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིའོ། །

[Block 1161]
དེ་ལ་བཟོད་པ༌[^759]ནི་ཆོས་བདག་མེད་པའོ། །

[Block 1162]
རྒྱ་ཆེ་བ་ནི་ནམ་མཁའ་མཛོད་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 1163 [HEADING]]
#### ཡིད་ལ་བྱེད་པ། ^4-1-2-0

[Block 1164]
ཡིད་ལ་བྱེད་པ་ཇི་ལྟ་བུས་རྣམ་པར་དག་པ་དེ་བསྟན་པའི་ཕྱིར་གལ་ཏེ་རྟོག་པ་ཙམ་དུ་ཆོས་ཐམས་ཅད་རྟོགས་པ་དེའི་ངོ་བོ་ཉིད་དེ་བསྟན་པར་བྱ་སྟེ། འདོད་པ་དང་ནི་མོས་པ་དག །དག་པ་བསམ་པ་དག་པ་ཉིད་ཡིན་ནོ། །

[Block 1165]
དེ་ལ་འདོད་པ་ནི་མངོན་པར་འདོད་པའོ། །

[Block 1166]
མོས་པ་ནི་དད་པའོ། །

[Block 1167 [HEADING]]
#### རྟགས། ^4-1-3-0

[Block 1168]
དེའི་རྟགས༌[^760]གང་ཡིན་པ་དེ་བསྟན་པར་བྱ་སྟེ། སྔ་ལ་སོགས༌[^761]སུ་ནི་ཐོག་མར་བསམ་པ་དག་པའོ། །

[Block 1169]
དེར་ཞེས་བྱ་བ་ནི་བསམ་པ་དག་པ་དེར་སངས་རྒྱས་རྣམས་ནི་མཐོང་བར་འགྱུར་བ་སྟེ། དེ་ནི་རྟགས་སོ། །

[Block 1170]
ཆོས་ཀུན་ཞེས་བྱ་བ་ནི་མཉམ་པར་གཞག་པའི་དུས་སོ། །

[Block 1171 [HEADING]]
#### ཕན་ཡོན། ^4-1-4-0

[Block 1172]
དེའི་ཕན་ཡོན་གང་ཡིན་པ་དེ་བསྟན༌[^762]པར་བྱ་སྟེ། དེ་ལ་གནས་པ་ནི་བྱང་ཆུབ་ཉེ་བར་རྟོགས་གྱུར་ནས་ཏེ། དེ་ཐོབ་པར་བྱེད་པའི་ཐབས་རྙེད་པས་ཚེགས་མེད་པར་འཐོབ་པར་འགྱུར་བའོ། །

[Block 1173]
བསམ་པ་དག་པ་གང་ཡིན་པ་དང་། རྒྱུ་ཅི་འདྲ་བ་དང་། ཇི་ལྟ་བུའི་བཟོད་པ་དང་། དམིགས་པ་གང་ཡིན་པ་དང་། ཇི་ལྟ་བུའི་ཡིད་ལ་བྱེད་པ་དང་། རྟགས་གང་ཡིན་པ་དེ་ཚིགས་སུ་བཅད་པ་དེ་དག་གིས་བསྟན་ཏེ། དེ་དག་ནི་ལྷག་པའི་བསམ་པ་དག་པའི་ལུས་རྣམ་པར་གཞག་པའོ། །

[Block 1174]
ཆུད་ཟ་བའི་རྒྱུ༌[^763]འཆལ་པའི་ཤེས་རབ་ཅེས་བྱ་བ་ལ། དེ་ལ་ཤེས་རབ་འཆལ་པའི༌[^764]ནི་ཕྱིན་ཅི་ལོག་ཏུ་འཛིན་པ་སྟེ། ཇི་ལྟར་མུ་སྟེགས་པ་ལྟ་བུའོ། །

[Block 1175]
དེས་ཀྱང་དེ་ཆུད་ཟ་བར་འགྱུར་རོ། །

[Block 1176]
ལྷག་མའི་དོན་ནི་གོ་སླ་བའོ།[^765] །

[Block 1177 [HEADING]]
### གྲངས་རྣམ་པར་གཞག་པ། ^4-2-0

[Block 1178]
མི་མཐུན་པའི་ཕྱོགས་དང་། གཉེན་པོས་གྲངས་རྣམ་པར་གཞག་པ་དང་། སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཡང་དག་པར་འགྲུབ་པའི་གཞིའི་གནས་ཀྱིས་ཞེས་བྱ་བ་སྟེ། སངས་རྒྱས་ཐམས་ཅད་ཀྱི་ཆོས་རྣམས་ཀྱི་རྒྱུའི་དངོས་པོས་ནི་རྣམ་པར་གཞག་པའི་རྣམ་གྲངས་གཉིས་པ་སྟེ། དེའི་ཕྱིར་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལས་ལྷག་པ་ཡང་མ་ཡིན་ཞིང་ཆད་པ་ཡང་མ་ཡིན་པ་སྟེ། རྣམ་པར་གཡེང་བ་མེད་པ་ལ་བརྟེན་ནས་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་རྟོགས་པར་འགྱུར་བས་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་བརྟེན་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་དེ་ཁོ་ན་ཉིད་རྟོགས་པར་འགྱུར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1179]
འདི་དག་གི༌[^766]དོན་ལྷག་མ་ནི་གོ་སླ་བའོ།[^767] །གང་གི་ཕྱིར་རྣམ་པར་གཞག་པའི་རྒྱུ་གསུམ་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྨིན་པར་བྱ་བ་དང་རྗེས་སུ་མཐུན་པས་ཞེས་བྱ་བ་སྟེ། སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྨིན་པར་བྱ་བ་ཉིད་ལ་རྗེས་སུ་མཐུན་པའི་ཕྱིར་ན་འདི་ལྟར་དྲུག་ཏུ་འགྱུར་ཏེ། དེའི་ཕྱིར་ན་ཡང་དྲུག་ཏུ་རྣམ་པར་གཞག་གོ། །

[Block 1180]
སེམས་མཉམ་པར་གཞག་པ་རྣམས་མཉམ་པར་གཞག་པར་བྱ་བའི་ཕྱིར་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 1181]
སེམས་མཉམ་པར་གཞག་པ་རྣམས་རྣམ་པར་ཐར་པར་བྱ་བའི་ཕྱིར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཡོངས་སུ་སྨིན་པར་བྱེད་པས་སོ། །

[Block 1182]
གདམས་པར་བྱ་བ་རྣམས་ཞེས་བྱ་བ་ནི་གདམས་ངག་སྦྱིན་པར་བྱའོ༌[^768]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1183 [HEADING]]
### ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གི་མཚན་ཉིད། ^4-3-0

[Block 1184]
སྦྱིན་པ་ལ་སོགས་པ་རྣམས་མཚན་ཉིད་གང་དང་ལྡན་པས་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་འཐོབ་ཅེ་ན། གང་གི་ཕྱིར་འཇིག་རྟེན་པ་དང་ཉན་ཐོས་ལ་སོགས་པ་དག་ལ་ཡང་སྦྱིན་པ་ལ་སོགས་པ་ཡོད་པས་དེས༌[^769]ན་འདི་དག་གི་མཚན་ཉིད་ངེས་པར་བརྗོད་པར་བྱ་སྟེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གི་མཚན་ཉིད་ལ་གནས་དམ་པ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་བྱང་ཆུབ་ཀྱི་སེམས་གནས་པ༌[^770]ཡིན་པའི་ཕྱིར་རོ། །

[Block 1185]
དངོས་པོ་དམ་པ་ཞེས་བྱ་བ་ནི་ཕྱི་དང་ནང་གི་བདག་ཉིད་མཐའ་དག་ཀུན་དུ་སྤྱོད་པ་ནི་གཞན་ཡོད་པ་མ་ཡིན་ལ། བྱང་ཆུབ་སེམས་དཔའ་ནི་འདིར་དངོས་པོ་མཐའ་དག་ཡོངས་སུ་སྤྱོད་པ་ཡིན་ནོ། །

[Block 1186]
ཆེད་དུ་བྱ་བ་དམ་པ་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་གང་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པ་དང་། བདེ་བའི་ཆེད་དུ་བྱེད་པའོ། །

[Block 1187]
ཐབས་ལ་མཁས་པ་དམ་པ་ཞེས་བྱ་བ་ནི་འདིར་འཁོར་གསུམ་ཡོངས་སུ་དག་པའི་ཐབས་ལ་མཁས་པས་ཡོངས་སུ་བཟུང་བ༌[^771]སྟེ། སྦྱིན་པར་བྱ་བར་ཡང་མ་ཡིན། སྦྱིན་པ་པོར་ཡང་མ་ཡིན་ལ། ལེན་པ་པོར་ཡང་རྟོག་པར་མི་བྱེད་པའོ། །

[Block 1188]
དེ་ལྟར་ན་སྦྱིན་པ་ལ་སོགས་པ་རྣམས་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱིས་ཡོངས་སུ་ཟིན་པར་གྱུར་པའོ། །

[Block 1189]
ཡོངས་སུ་བསྔོ་བ་དམ་པ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་སྦྱིན་པ་ལ་སོགས་པ་རྣམས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ཡོངས་སུ་བསྔོ་བའོ། །

[Block 1190]
རྣམ་པར་དག་པ་དམ་པ་ཞེས་བྱ་བ་ནི་གང་གིས་གང་གི་ཚེ་སངས་རྒྱས་སུ་འགྱུར་བ་ཉིད་ཀྱི་སྦྱིན་པ་ལ་སོགས་པ་རྣམས་ཏེ། དེ་ཡང་ཉོན་མོངས་པའི་སྒྲིབ་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ༌[^772]དག་ལས་རྣམ་པར་གྲོལ་བ་ཀུན་ཏུ་སྒྲུབ་པར་གྱུར་པའོ། །

[Block 1191]
སྦྱིན་པ་གང་ཡིན་པ་དེ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་དེ་ཡིན་ནམ། ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་ཡིན་པ་དེ་སྦྱིན་པ་ཡང་དེ་ཡིན་ནམ་ཞེས་དྲིས་པའི་ཕྱོགས་དེ་བསྟན་པར་བྱ་སྟེ། སྦྱིན་པ་གང་ཡིན་པ་དེ་ཕ་རོལ་ཏུ་ཕྱིན་པ་མ་ཡིན་པ་ནི་གང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དང་བྲལ་བའོ། །

[Block 1192]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཡིན་ལ་སྦྱིན་པ་མ་ཡིན་པ་ནི་ཚུལ་ཁྲིམས་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གིས་ཡོངས་སུ་བསྡུས་པའོ། །

[Block 1193]
སྦྱིན་པ་ཡང་ཡིན་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་ཡིན་པ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གིས་བསྡུས་པའི་སྦྱིན་པའོ། །

[Block 1194]
སྦྱིན་པ་ཡང་མ་ཡིན་པ་རོལ་ཏུ་ཕྱིན་པ་ཡང་མ་ཡིན་པ་ནི་ཚུལ་ཁྲིམས་ལ་སོགས་པ་དྲུག་པོ་དེ་དག་དང་བྲལ་བའོ། །

[Block 1195]
དེ་བཞིན་དུ་མུ་བཞི་པོ་ཐམས་ཅད་ལ་བལྟ་བར་བྱའོ། །
--- END BLOCKS ---
