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

[Block 1196 [HEADING]]
### ངེས་པའི་ཚིག། ^4-4-0

[Block 1197]
ངེས་པའི་ཚིག་བལྟ་བར་བྱ་སྟེ། རེ་ཞིག་ཐམས་ཅད་ཀྱི་སྤྱིའི་ངེས་པའི་ཚིག་ནི་ཕ་རོལ་ཏུ་སོང་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། འཇིག་རྟེན་པ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་ཀྱི་སྦྱིན་པ་ལ་སོགས་པ་ཐམས་ཅད་ཀྱི་མཆོག་ཏུ་ཕྱིན་པས་དེས་ན་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 1198]
སོ་སོའི་ནི་རྒྱུའི་དུས་ན་སེར་སྣ་མ་བཅོམ་པར་སྦྱིན་པ་གཏོང་བར་མི་བྱེད་པའི་ཕྱིར་དང་། འབྲས་བུའི་དུས་ན་ནི་དབུལ་བ་ལུས༌[^773]འཛིན་པར་བྱེད་པའི་ཕྱིར་དང་། ལོངས་སྤྱོད་ཆེན་པོ་དང་། བསོད་ནམས་ཀྱི་ཚོགས་སྦྱིན་པར་བྱེད་པས་སྦྱིན་པའོ། །

[Block 1199]
རྒྱུའི་དུས་ན་འཆལ་པའི་ཚུལ་ཁྲིམས་ཞི་བར་བྱེད་པ་དང་། འབྲས་བུའི་དུས་ན་ངན་འགྲོ་ཞི་བར་བྱེད་པ་དང་། བདེ་འགྲོ་དང་ཏིང་ངེ་འཛིན་ཐོབ་པར་བྱེད་པས་ཚུལ་ཁྲིམས་སོ། །

[Block 1200]
དེ་བཞིན་དུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ཀྱི་ངེས་པའི་ཚིག་ཇི་ལྟར་རིགས་པ་བཞིན་དུ་སྦྱར་བར་བྱ་སྟེ། བདག་དང་གཞན་དག་ལ་བདེ་བར་བྱེད་པས་ཞེས་བྱ་བ་ལ་བདག་ཉིད་ངན་འགྲོ་དང་། ཁོན༌[^774]དུ་འཛིན་པ་དང་། ཁྲོ་བ་ལ་སྦྱོར་བར་མི་བྱེད་ཅིང་། ཕ་རོལ་དག་ཀྱང་བདེ་བར་བྱེད་དེ། དེ་དག་ལ་སྡུག་བསྔལ་སྐྱེད་པར་མི་བྱེད་དོ། །

[Block 1201 [HEADING]]
### བསྒོམ་པ་རྣམ་པ་ལྔ། ^4-5-0

[Block 1202]
བསྒོམ་པ་རྣམ་པ་ལྔར་བལྟ་བར་བྱ་སྟེ་ཞེས་བྱ་བ༌[^775]དེ་ལ་ཀུན་ཏུ་སྤྱོད་པ་ལ་སྦྱོར་བ་ནི་ཀུན་ཏུ་སྤྱོད་པ་ལ༌[^776]བསྒོམ་པའོ། །

[Block 1203]
བྱ་བ་སྒྲུབ་པ༌[^777]བསྒོམ་པ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་མཛད་པ་ཤིན་ཏུ་སྦྱངས་པ་འབད་པ་མེད་པ་མངའ་བས་ཀུན་ཏུ་སྤྱོད་པ་མེད་བཞིན་དུ་ཡང་སངས་རྒྱས་རྣམས༌[^778]ཀྱི་སྐུའི་གནས་སྐབས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་སེམས་ཅན་རྗེས་སུ་བཟུང་བའི་ཕྱིར་བྱ་བ་སྒྲུབ་པ༌[^779]འབྱུང་བར་འགྱུར་བའོ། །

[Block 1204]
དེ་ལྟ་བུ་རེ་ཞིག་བསྒོམ་པའོ། །

[Block 1205]
དེ་སྙེད་ཀྱི་དུས་སྐད་ཅིག་མ་གཅིག་ཏུ་ཞེས་བྱ་བ་ལ། གང་དེ་ལྟ་བུའི་གྲངས་མེད་པ་གསུམ་ལ་སོགས་པའི་ཚད་ཀྱི་དུས་སྐད་ཅིག་མ་གཅིག་ཏུ་བྱས་ལ། དེ་ལྟ་བུའི་སྐད་ཅིག་མས་ཇི་སྲིད་བྱང་ཆུབ་པར་གྱུར་པ་དེ་སྲིད་ཀྱི་དུས་སུ་སྐད་ཅིག་རེ་རེ་ལ་བདག་གི༌[^780]ལུས་ཞེས་བྱ་བ་ལ་སོགས་པ་རྩ་བའི་གཞུང་གི་རྗེས་སུ་འབྲངས་ནས་བལྟ་བར་བྱ་སྟེ་གོ་སླའོ། །

[Block 1206]
རིམ་པ་དེ་ལྟ་བུ་ཉིད་ཀྱིས་བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ལ་གནས་ཀྱི་བར་དེ་སྲིད་དུ་དེ་ལྟ་བུའི་ཚུལ་ཁྲིམས་ལ་སོགས་པའི་སེམས་གཅིག་ཉིད་སྐྱེད་པར་བྱེད་པ་ཉིད་དོ། །

[Block 1207]
སྟོང་གསུམ་གྱི་སྟོང་ཆེན་པོའི་འཇིག་རྟེན་གྱི་ཁམས་མེས་ཡོངས་སུ་གང་བ༌[^781]སྐད་ཅིག་རེ་རེ་ལ་སྤྱོད་ལམ་བཞི་བྱེད་ཅིང་ཡོ་བྱད་ཐམས་ཅད་དང་མི་ལྡན་པ༌[^782]ཡང་ཞེས་བྱ་བ་ལ། འདིས་ནི་གནས་མེད་ཅིང་ཡོ་བྱད་ཐམས་ཅད་དང་མི་ལྡན་པ་ཉིད་བསྟན་ཏོ། །

[Block 1208]
ངེས་པར་བྱས་པའི་སྒྲིབ་པ་ཐམས་ཅད་ཀྱང་བཤིག་པར་འགྱུར་ན་ཞེས་བྱ་བ་ནི་ངེས་པར་བཤིག་པ་ཙམ་གྱིས་རྣམ་པར་སྨིན་པར་མི་ནུས་པར་འདོད་པའོ། །

[Block 1209]
ཡང་ན་ངན་འགྲོར་འགྲོ་བའི་གཉེན་པོ་ཉིད་ཡིན་པའི་ཕྱིར་བསམ་པ་རྒྱ་ཆེན་པོ༌[^783]ཉིད་ནི་མི་ངོམས་པའི་བསམ་པའོ། །

[Block 1210]
འདི་ལྟར་དེ་དག་ཉིད་རྒྱུན་རིང་པོར་ཡང་མི་འདོར་བའི་བསམ་པ་དེ་ཡོད་པས་ན་རྒྱུན་རིང་པོའི་བསམ་པ་སྟེ། རྒྱུན་རིང་དུ་ཞེས་བྱ་བ་ནི་དུས་རིང་དུའོ། །

[Block 1211]
དོན་ལྷག་མ་ནི་གོ་སླའོ། །

[Block 1212 [HEADING]]
### ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལུས་རྣམ་པར་གཞག་པ་དང་རབ་ཏུ་དབྱེ་བ། ^4-6-0

[Block 1213 [HEADING]]
#### སྦྱིན་པ། ^4-6-1-0

[Block 1214]
ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལུས་རྣམ་པར་གཞག་པ་དང་། རབ་ཏུ་དབྱེ་བ་བསྟན་པ་དེ་བཤད་པར་བྱ་སྟེ། གང་གི་ཕྱིར་སྦྱིན་པ་རྣམ་པ་གསུམ༌[^784]ཡིན་ཞེ་ན། ཆོས་ཀྱི་སྦྱིན་པ་ལ་སོགས་པ་སྟེ། འདི་ལྟར་ཆོས་ཀྱི་སྦྱིན་པ་ནི་གཞན་གྱི་དགེ་བའི་རྩ་བ་ཉེ་བར་བརྟན་པར་བྱེད་པའོ། །

[Block 1215]
ཟང་ཟིང་གི་སྦྱིན་པ་ནི་འདིའི་ལུས་བརྟན་པར་བྱེད་པའོ། །

[Block 1216]
མི་འཇིགས་པའི་སྦྱིན་པ་ནི་དེ་ཉིད་ཀྱི་སེམས་བརྟན་པར་བྱེད་པ་སྟེ། དེའི་ཕྱིར་རྒྱུ་དེས་ན་སྦྱིན་པ་རྣམ་པ་གསུམ་དུ་བསྟན་ཏོ། །

[Block 1217 [HEADING]]
#### ཚུལ་ཁྲིམས། ^4-6-2-0

[Block 1218]
ཚུལ་ཁྲིམས་ཀྱང་རབ་ཏུ་གནས་པའི་ཚུལ་ཁྲིམས་ནི་སྡོམ་པའི་ཚུལ་ཁྲིམས་ཏེ། ལྷག་མ་གཉིས་པོ་དག་གི་དོན་གྱི་གནས་ཡིན་པའི་ཕྱིར་ཏེ། འདི་ལྟར་སྡོམ་པ་ལ་གནས་པའི་དགེ་བའི་ཆོས་སྡུད་པའི་ཚུལ་ཁྲིམས་ཀྱིས་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་དང་། བྱང་ཆུབ་མངོན་པར་སྒྲུབ་པས་རྟེན་དུ་གྱུར་པ་ཉིད་དང་། སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་ཀྱིས་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པས་རྟེན་དུ་གྱུར་པའོ། །

[Block 1219 [HEADING]]
#### བཟོད་པ། ^4-6-3-0

[Block 1220]
བཟོད་པ་ཡང་གནོད་པར་བྱེད་པ་ལ་ཇི་མི་སྙམ་པའི་བཟོད་པ་ནི་གང་གཞན་གྱིས་གནོད་པ་བྱེད་པ་ལ་ཁྲོ་བ༌[^785]རབ་ཏུ་སྤོང་བ༌[^786]ཉིད་དོ། །

[Block 1221]
དེའི་དབང་གིས་འཁོར་བའི་སྡུག་བསྔལ་དང་དུ་ལེན་པའི་བཟོད་པ་སྟེ། གང་གི་སྟོབས་ཀྱིས་འཁོར་བའི་སྡུག་བསྔལ་གང་ཡིན་པ་དེས་ལྡོག་པར་མི་འགྱུར་བའོ། །

[Block 1222]
ཆོས་ལ་ངེས་པར་རྟོགས་པའི༌[^787]བཟོད་པ་ནི་ཡང་ཆོས་གང་ལ་ངེས་པར་བརྟག་པ༌[^788]དེ་ལ་འདོད་པ་སྟེ། དེ་ཡང་བཤད་མ་ཐག་པའི་བཟོད་པ་གཉིས་པོ་དག་གི་རྟེན་དུ་གྱུར་པའོ། །

[Block 1223 [HEADING]]
#### བརྩོན་འགྲུས། ^4-6-4-0

[Block 1224]
བརྩོན་འགྲུས་ཀྱི་ལུས་ཀྱང་རྣམ་པ་གསུམ༌[^789]དུ་གཞག་སྟེ།

[Block 1225]
འདི་ལྟར༌[^790]བཅོམ་ལྡན་འདས་ཀྱིས༌[^791]མདོ་སྡེ་གཞན་དག་ལས།

[Block 1226]
བརྟན་པ་དང་ལྡན་པ་པ༌[^792]དང་། བརྩོན་འགྲུས་དང་ལྡན་པ་དང་། སྤྲོ་བ་ཅན་དང་། ཕ་རོལ་གནོན་པ་བརྟན་པ་དང་། བླངས་པ་མི་འདོར་ཞིང་ཞེས་གསུངས་པའི་ཚིག་དེ་དག་བརྩོན་འགྲུས་ཀྱི་ལུས་རྣམ་པར་གཞག་པ་གསུམ་དང་སྦྱར་བར་བྱའོ། །

[Block 1227]
དེ་ལ་གོ་ཆའི་བརྩོན་འགྲུས་ནི་བརྟན་པ་དང་ལྡན་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1228]
དང་པོར་སྦྱོར་བའི་བརྩོན་འགྲུས་ནི་བརྩོན་འགྲུས་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 1229]
སྦྱོར་བའི་དུས་སུ་མི་ཞུམ་པ་དང་། མི་འཁྲུགས་པ་དང་། ཆོག་པར་མི་འཛིན་པ་ཞེས་བྱ་བ་དག་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་སྤྲོ་བ་ཅན་དང་། ཕ་རོལ་གནོན་པ་བརྟན་པ་དང་། བླངས་པ་མི་འདོར་བ་ཞེས་བྱ་བ་འདི་དག་གིས་བསྟན་པ་ཡིན་ནོ། །

[Block 1230]
གང་གི་ཕྱིར་གང་དག༌[^793]དང་པོར་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་དོན་དུ་བརྟན་པ་དང་ཡང་ལྡན་ལ། སྦྱོར་བའི་དུས་སུ་བརྩོན་འགྲུས་དང་ལྡན་དུ་ཟིན་ཀྱང་སེམས་ཞུམ་པར་གྱུར་ན་མ་ཡིན་པས་དེ་ལྟ་བས་ན་དེའི་གཉེན་པོར་སྤྲོ་བ་ཅན་ཏེ། གང་སེམས་སྤྲོ་བ་དང་ལྡན་པ་དེ་སེམས་ཞུམ་པར་མི་འགྱུར་ཏེ། ཞུམ་པ་ནི་འདིར་སེམས་འགོང་བའི་བདག་ཉིད་དུ་འདོད་དོ། །
--- END BLOCKS ---
