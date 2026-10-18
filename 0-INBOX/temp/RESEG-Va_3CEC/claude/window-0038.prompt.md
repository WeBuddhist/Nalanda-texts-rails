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
[Block 1331]
སྐད་ཇི་ལྟ་བ་བཞིན་དུ་འཇུག་པས་ཆོས་སྟོན་ཅེས་བྱ་བ་ནི་སོ་སོའི་སྒྲ་དང་སྐད་ལ་སོགས་པ་དང་མཐུན་པར་བྱས་ནས་ཆོས་སྟོན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1332]
ཐེག་པ་གཞན་མི་ཉན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་མི་ཉན་ཞིང་དེར་མི་བསྔོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1333]
ལྷའི་རྣ་བ་མངོན་པར་ཤེས་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ། །

[Block 1334 [HEADING]]
### སེམས་མངོན་སུམ་པ། ^3-3-0

[Block 1335]
སེམས་མངོན་སུམ་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཕ་རོལ་གྱི་སེམས་ཤེས་པའི་མངོན་པར་ཤེས་པ་མི་ཟད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1336]
སྔོན་གྱི་མཐའི་སེམས་ཤེས་པ་དང་ཞེས་བྱ་བ༌[^1137]ནི་འདས་པའི་དུས་ཀྱི་སེམས་ཅན་རྣམས་ཀྱི་སེམས་ཅི་དང་ཅི་ལྟ་བུར་གྱུར་པ་ཤེས་པའོ། །

[Block 1337]
ཕྱི་མའི་མཐའི་སེམས་ཤེས་ཞེས་བྱ་བ་ནི་མ་འོངས་པའི་དུས་ཀྱི་སེམས་ཅན་རྣམས་ཀྱི་སེམས་ཅི་དང་ཅི་ལྟ༌[^1138]བུར་འགྱུར་བ༌[^1139]ཤེས་པའོ། །

[Block 1338]
ད་ལྟར་བྱུང་བའི་སེམས་ཤེས་ཞེས་བྱ་བ་ནི་ད་ལྟར་བྱུང་བའི་སེམས་ཅན་རྣམས་ཀྱི་སེམས་ཅི་དང་ཇི་ལྟ་བུར༌[^1140]ཤེས་པའོ། །

[Block 1339 [HEADING]]
#### འདས་པའི་དུས་ཀྱི་སེམས་ཤེས་པ། ^3-3-1-0

[Block 1340]
འདས་པའི་དུས་ཀྱི་སེམས་ཤེས་པ་རྒྱས་པར་བསྟན་པའི་ཕྱིར། དེ་འདས་པའི་སེམས་ཤེས་པས་སེམས་ཅན་རྣམས་ཀྱི་སྔོན་གྱི་རྒྱུ་ལས་བྱུང་བའི་སེམས་ལ་འཇུག་ཅེས་བྱ་བ་ལ་སོགས་པ༌[^1141]གསུངས་ཏེ། སེམས་ཅན་རྣམས་ཀྱི་སེམས་སྔོན་འདས་པའི་ཐམས་ཅད་ཤེས་ཏེ། སྔོན་འདས་པའི་སེམས་དེ་དག་ལས་ད་ལྟར་དང་ཕྱི་མའི་སེམས་འབྱུང་བས་སྔོན་གྱི་རྒྱུ་ལས་བྱུང་བའི་སེམས་ཞེས་བྱ་སྟེ། [^1142]དེ་ཤེས་པ་ནི་སེམས་ལ་འཇུག་པའོ། །

[Block 1341]
དེ་ཡང་ཇི་ལྟར་ཤེས་ཤེ་ན། དེའི་ཕྱིར་སེམས་ཅན་དེའི་སེམས་འདི་ནི་རྒྱ་ཆེའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སེམས་ཅན་འདིའི་སེམས་སྔོན་དགེ་བ་དང་མི་དགེ་བ་ལ་སོགས་པ་ཤས་ཆེན་པོ་སྤྱོད་སྤྱོད་པའི་རྒྱུ་འམ། འབྲིང་པོ་སྤྱོད་སྤྱོད་པ་འམ། ཆུང་ངུར་སྤྱོད་པའི་རྒྱུས་ད༌[^1143]འདི་ལྟར་གྱུར་ཏོ་ཞེས་སེམས་ཀྱི་རྒྱུ་རྣམས་ཤེས་པ་ལ་བྱའོ། །

[Block 1342]
སེམས་ཅན་འདིའི་དབང་པོ་རྣམས་ནི་སྦྱིན་པའི་རྣམ་པའི་རྒྱུ་དང་ལྡན་ཞེས་བྱ་བ་ལ་སེམས་ཅན་རྣམས་ཀྱི་དད་པ་ལ་སོགས་པའི་དབང་པོ་རྣམས་སྔོན་སྦྱིན་པ་སྤྱོད་སྤྱོད་པའི་རྒྱུ་དང་ལྡན་ཏེ། སྦྱིན་པའི་རང་བཞིན་ནི་ཤས༌[^1144]ཆེའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1343]
རྣམ་པ་ནི་དེའི་རང་བཞིན་ནམ། དེའི་ཤས་ཆེ་བ་ལ་བྱ་སྟེ། དེ་བཞིན་དུ་ཚུལ་ཁྲིམས་ལ་སོགས་པ་འོག་མ་རྣམས་ལ་ཡང་སྦྱར་རོ། །

[Block 1344]
སེམས་ཅན་འདི་ནི་རྒྱུའི་སྟོབས་ཅན་ཏེ་དགེ་བའི་རྩ་བའི་རྒྱུའི་རྒྱུན་འདི་དག་ལྡན་ན་སེམས་ཅན་དེ་སྦྱོར་བའི་རྒྱུས་རིགས་དམའ་བར་སྐྱེས་སོ་ཞེས་བྱ་བ་ནི་སྔོན་གྱི་སེམས་ཀྱི་རྒྱུ་རྣམ་པ་སྣ་ཚོགས་པ་ཤེས་པ་སྟོན་ཏེ། སྔོན་གྱི༌[^1145]དགེ་བའི་རྒྱུ་མཐུན་པ༌[^1146]ཆེན་པོ་སྤྱད་པས་དགེ་བའི་རྩ་བའི་རྒྱུའི་རྒྱུན༌[^1147]དེ་དག་དང་ལྡན་པར་ཡང་ཤེས། སེམས་ཅན་དེ་ཉིད་ལུས་དང་ངག་གི་སྒོ་ནས་རིགས་ཆུང་ངུར་སྐྱེ་བའི་རྒྱུ༌[^1148]ལས་ངན་པ་སྤྱད་པའི་རྒྱུས་རིགས་ཆུང་ངུར་སྐྱེས་པ་ཡང་ཤེས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1345 [HEADING]]
#### མ་འོངས་པའི་སེམས་ཅན་གཞན་གྱི་སེམས་ཤེས་པ། ^3-3-2-0

[Block 1346]
མ་འོངས་པའི༌[^1149]སེམས་ཅན་གཞན་གྱི་སེམས་ཤེས་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་ཕྱི་མའི་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1347]
སེམས་ཅན་འདི་དག༌[^1150]ད་ལྟར་གྱི་སྦྱིན་པའི་རྒྱུ་ནི་མ་འོངས་པའི་དུས་ན་འདིའི་ཚུལ་ཁྲིམས་གྱི་རྒྱུར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པས་རྒྱུ་དང་འབྲས་བུ་མ་གྲགས་ཤིང་མི་མཐུན་པ་རྣམས་ལས་ཀྱང་རྒྱུ་དང་འབྲས་བུར༌[^1151]འགྱུར་བ་ཤེས་པ་བསྟན་ཏེ། ཡོད་ནི་སྦྱིན་པའི་རྒྱུས་མ་འོངས་པའི་དུས་ན་ཡང་སྦྱིན་པ་དང་ལྡན་པར་འགྱུར་བའི་རིགས༌[^1152]ལས་སྦྱིན་པའི་ཚེ་ཡང་མི་འཇིགས་པའི་སྦྱིན་པ་ལ་སོགས་པ་ཚུལ་ཁྲིམས་ཀྱི་རང་བཞིན་ཡོད་པས༌[^1153]ཚུལ་ཁྲིམས་ཀྱི་རྒྱུར་འགྱུར་བ་ཤེས་པ་ལ་བྱའོ། །

[Block 1348]
རྣམ་པ་གང་དག་འབྱུང་བ་ཞེས་བྱ་བ་ནི་རྒྱུ་དང་རྐྱེན་དེ་དག་ལས་འབྲས་བུ་གང་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1349]
དེའི་སེམས་ལ་འཇུག་པ༌[^1154]ཤེས་པ༌[^1155]དང་། ཆོས་ཀྱི་སྣོད་དུ་གྱུར་པ་ཇི་སྙེད་པ་དེ་སྙེད་དུ་ཆོས་སྟོན་ཏོ་ཞེས་བྱ་བ་ནི་ཕ་རོལ་གྱི་སེམས་ཤེས་པར་བྱ་ཞིང་ཆོས་ཀྱི་སྣོད་ལ་ཆོས་བསྟན་པར་བྱ་བ་ཇི་སྙེད་པ་སེམས་ཤེས་པའི་མངོན་པར་ཤེས་ལ༌[^1156]ཡང་དེ་སྙེད་དེ། དེ་དག་ཤེས་ནས་ཆོས་བསྟན་པའང་དེ་སྙེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1350]
མདོར་ན་ཤེས་པར་བྱ་བའི་ཡུལ༌[^1157]ཟད་མི་ཤེས་པས་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དེ་ཡང་ཟད་མི་ཤེས་སོ་ཞེས་བྱ་བར་བསྟན་ཏོ། །

[Block 1351]
དེའི་འབྲས་བུ་ཡོད་པར་ཆོས་སྟོན་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གང་འདུལ་བར་བྱ་བའི་ཕྱིར་ཆོས་བསྟན་པའི་སེམས་ཅན་དེ་དག་ཀྱང་ཆོས་བསྟན་པ་དེས་ཐུལ་བར་གྱུར༌[^1158]ཏེ། དོན་མེད་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1352 [HEADING]]
#### ད་ལྟར་གྱི་དུས་ཀྱི་སེམས་ཅན་གྱི་སེམས་ཤེས་པ། ^3-3-3-0

[Block 1353]
ད་ལྟར་གྱི་དུས་ཀྱི་སེམས་ཅན་གྱི་སེམས་ཤེས་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་ད་ལྟར་བྱུང་བའི་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1354]
འདོད་ཆགས་དང་བཅས་པའི་སེམས་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། སེམས་ཅན་འདིའི་སེམས་ནི་འདོད་ཆགས་དང་བཅས་པ་ཡིན། སེམས་ཅན་འདིའི་སེམས་ནི་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་ཞེས་ཤེས་པའོ། །

[Block 1355]
ཉོན་མོངས་པ་དང་བཅས་པ་དང་། ཉོན་མོངས་པ་དང་བྲལ་བ་ཞེས་བྱ་བ་ནི་སྤྱིར་ཉོན་མོངས་པ་དང་བཅས་པ་དང་། [^1159]ཉོན་མོངས་པ་དང་བྲལ་བར་ཤེས་པའོ། །

[Block 1356]
བསྡུས་པ་དང་རྣམ་པར་གཡེངས་པ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་ལ་རྩེ་གཅིག་ཏུ་བསྡུས་པ་དང་། རྩེ་གཅིག་ཏུ་མ་བསྡུས་པས་ཏེ་གཡེངས་པ་ཤེས་པའོ། །

[Block 1357]
བྱིང་བ་དང་རབ་ཏུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་གཉིད་དང་རྨུགས་པ་ལ་སོགས་པས་སེམས་ནོན་པ་དང་མ་ནོན་པ་ཤེས་པའོ། །

[Block 1358]
རྣམ་པར་ཞི་བ་དང་རྣམ་པར་མ་ཞི་བ་ནི་ཏིང་ངེ་འཛིན་མ་ཐོབ་པ་དང་ཐོབ་པའོ། །

[Block 1359]
ཆུང་ངུ་དང་ཡངས་པ་དང༌[^1160]ཆེན་པོར་གྱུར་པ་དང་། ཚད་མེད་པའི་སེམས་ཞེས༌[^1161]བྱ་བ་ལ་ཆུང་ངུ་ནི་འདོད་པའི་ཁམས་ཀྱི་སེམས་ཅན་གྱི་སེམས་ལ་བྱ་སྟེ། བསམ་གཏན་ལ་སོགས་པ་བསམ་པ་རྒྱ་ཆེན་པོ་མེད་ཅིང་དམིགས་པ་ཆུང་པའི་ཕྱིར་རོ། །

[Block 1360]
ཡངས་པ་དང་རྒྱ་ཆེན་པོ་ནི་གཟུགས་ཡོད་པ་རྣམས་ཀྱི་སེམས་ཅན་རྣམས་ཀྱི་སེམས་ལས༌[^1162]བྱ་སྟེ། དེ་དག་གི་བསམ་པ་རྒྱ་ཆེ་ཞིང་བསམ་གཏན་དང་པོ་ལ་སོགས་པ་དམིགས་པ་ཆེན་པོ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1361]
ཚད་མེད་པ་ནི་གཟུགས་མེད་པའི་ཁམས་ཀྱི་སེམས་ལ་བྱ་སྟེ། ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ་སོགས་པའི་སྙོམས་པར་འཇུག་པ་ཚད་མེད་པ་རྣམས་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 1362]
རང་གི་སེམས་སྒྲིབ་པ༌[^1163]འམ་གཞན་གྱི་སེམས་བསྒྲིབ་པར༌[^1164]མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་བདག་གི་སེམས་ལ་རབ་རིབ་དང་ཐོགས་པ་མེད་པས་བསྒྲིབ་པར༌[^1165]མི་འགྱུར་བ་དང་། གཞན་གྱིས༌[^1166]སེམས་ཤེས་པར་བྱ་བ་ཉིད་ཀྱང་གསལ་བར་ཤེས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1363]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་བསྒྲིབ་པར༌[^1167]མི་འགྱུར་ཞེ་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1364]
དེའི་སེམས་ཀྱི་རྒྱུན་ནི་ཡེ་ཤེས་ཀྱིས་རིག་ཅེས་བྱ་བ་ལ་སོགས་པ་ལ། བྱང་ཆུབ་སེམས་དཔའི་ཕ་རོལ་གྱི་སེམས་ཤེས་པའི་སེམས་ཀྱི་རྒྱུན་དེ་ཡེ་ཤེས་དང་ལྡན་པ་འམ། ཡེ་ཤེས་ཀྱིས་བསྟངས་པ་འམ། ཡེ་ཤེས་རང་བཞིན་དུ་གྱུར་པས༌[^1168]ཕ་རོལ་གྱི་སེམས་རིག་པའི་ཕྱིར་བསྒྲིབ་པར༌[^1169]མི་འགྱུར་རོ་ཞེས་གོང་དུ་སྨོས་པ་དང་སྦྱར་རོ། །

[Block 1365]
དེ་བཞིན་དུ་དྲན་པ་ལ་སོགས་པ་འོག་མ་རྣམས་དང་ཡང་སྦྱར་བར་བྱ་སྟེ།[^1170] དྲན་པ་ལ་སོགས་པ་ནི་གོང་དུ་བཤད་པ་བཞིན་དུ་བལྟའོ།[^1171] །དྲི་མ་མེད་པ་ནི་གློ་བུར་གྱི་དྲི་མ་དང་མ་འདྲེས་པའི་ཕྱིར་རོ། །

[Block 1366]
འོད་གསལ་བ་ནི་རང་བཞིན་གྱིས་དག་པའི༌[^1172]རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1367]
ཁ་ན་མ་ཐོ་བ་མེད་པ་ནི་སྡིག་པའི་ཆོས་དང་མ་འདྲེས་པས་སོ། །

[Block 1368]
མི་བརླང་པ་ནི་ཞེ་སྡང་སྤངས་པའོ།[^1173] །ཉོན་མོངས་པ་མེད་པ་ནི་ཉོན་མོངས་པར་འགྱུར་བའི་ཆོས་གང་གིས་ཀྱང་ཉོན་མོངས༌[^1174]པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1369]
རྙོག་པ་མེད་པ་ནི༌[^1175]སྒྲིབ་པར་འགྱུར་བའི་ཆོས་ཐམས་ཅད་སྤངས་པའི་ཕྱིར་རོ། །

[Block 1370]
ཆོས་ཐམས་ཅད་སྣང་བས༌[^1176]རིག་པ་ནི་ཤེས་པར་བྱ་བའི་དངོས་པོ་ཐམས་ཅད་མངོན་སུམ་དུ་རྟོག་པའི༌[^1177]ཕྱིར་རོ། །
--- END BLOCKS ---
