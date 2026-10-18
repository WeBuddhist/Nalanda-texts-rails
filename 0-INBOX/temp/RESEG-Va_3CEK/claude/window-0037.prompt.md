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
[Block 1296]
ཡོན་ཏན་བཞི་དང་ལྡན་པའི་ཚུལ་ཁྲིམས་དེ་ནི་རྣམ་པར་དག་པ་ཡིན་ནོ། །

[Block 1297]
བཟློག་པ་ནི་རྣམ་པར་མ་དག་པ་ཡིན་ནོ། །ཇི་ལྟར་ན་ཡོན་ཏན་བཞི་དང་ལྡན་པ་ཡིན་ཞེ་ན། ཚུལ༌[^915]ཁྲིམས་དེ་རྒྱུས་འཕེན་མ་བྱུང་།[^916] །དེ་ཡི་གཉེན་པོ་ཞི་ལ་བརྟེན།[^917] །རེ་ཞིག་འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱིས་འཕེན་མ་བྱུང་བ་ནི་ཇི་སྐད་དུ་བཤད་པས་འཕེན་མ་བྱུང་བ་ཡིན་ནོ། །

[Block 1298]
འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱི་རྒྱུས་འཕེན་མ་བྱུང་བ་ནི་ཆགས་པ་ལ་སོགས་པ་ཉོན་མོངས་པ་དང་། ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་ཀྱིས་འཕེན་མ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 1299]
འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱི་གཉེན་པོ་ལ་བརྟེན་པ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་བརྟེན་པའི༌[^918]ཕྱིར་རོ། །

[Block 1300]
ཞི་བ་ལ་བརྟེན་པ༌[^919]ནི་སྐྱེ་བའི་ཁྱད་པར་ལ་མི་བརྟེན་གྱི་མྱ་ངན་ལས་འདས་པར་ཡོངས་སུ་བསྔོས་པའི་ཕྱིར་རོ། །

[Block 1301]
གཞན་དག་ན་རེ་རྒྱུ་ལྔ་སྟེ། ལས་ཀྱི་ལམ་དངོས་ཀྱིས་རྣམ་པར་དག་པ་ཡིན་པ་དང་། ཉེར་བསྡོགས༌[^920]དག་གིས་རྣམ་པར་དག་པ་དང་། རྣམ་པར་རྟོག་པ་རྣམས་ཀྱིས་འཕེན་མ་བྱུང་བ༌[^921]དང་། དྲན་པས་ཡོངས་སུ་བཟུང་བ་དང་། མྱ་ངན་ལས་འདས་པར་ཡོངས་སུ་བསྔོས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1302]
གཞན་དག་ན་རེ་ཚུལ་ཁྲིམས་ནི་རྣམ་པ་བཞི་སྟེ། འཇིགས་པའི་ཚུལ་ཁྲིམས་ནི་འཚོ་བ་མེད་པ་དང་། ཚིགས་སུ་བཅད་པ་མེད་པ་དང་ཆད་པ་དང་། ངན་འགྲོས་འཇིགས་ནས་སྲུང་བ་གང་ཡིན་པའོ། །

[Block 1303]
ལེགས་སུ་སྨོན་པའི་ཚུལ་ཁྲིམས་ནི་སྲིད་པ་དང་། ལོངས་སྤྱོད་དང་། བཀུར་སྟི་ལ་ཆགས་ནས་སྲུང་བ་གང་ཡིན་པའོ། །

[Block 1304]
བྱང་ཆུབ་ཀྱི་ཡན་ལག་གི་རྗེས་སུ་མཐུན་པའི་ཚུལ་ཁྲིམས་ནི་ཡང་དག་པའི་ལྟ་བ་ཅན་རྣམས་ཐར་པའི་དོན་དུ་སྲུང་བ་གང་ཡིན་པའོ། །

[Block 1305]
ཡོངས་སུ་དག་པའི་ཚུལ་ཁྲིམས་ནི་དྲི་མ་མེད་པའི་ཕྱིར་ཟག་པ་མེད་པའི་ཚུལ་ཁྲིམས་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1306]
ཚུལ་ཁྲིམས་རྫོགས་སོ།། །།

[Block 1307 [HEADING]]
#### བསྒོམ་པ། ^1-71-3-0

[Block 1308]
མཉམ་པར་གཞག་པའི་དགེ་བ་ནི་སྒོམ༌[^922]པའོ། །

[Block 1309]
མཉམ་པར་གཞག་པ་ཞེས་བྱ་བ་འདི་ཅི༌[^923]ཞིག་ཅེ་ན། ཏིང་ངེ་འཛིན་གྱི་རང་བཞིན་དང་། དེ་དང་ལྷན་ཅིག་འབྱུང་བ་གང་ཡིན་པའོ། །

[Block 1310]
འདི་ཅིའི་ཕྱིར་བསྒོམ་པ་ཞེས་བྱ་ཞེ་ན། སེམས་ལ་སྒོ་ཕྱིར་རོ། །

[Block 1311]
མཉམ་པར་མ༌[^924]བཞག་པའི་དགེ་བ་དེ་ནི་རྒྱུད་ཡོན་ཏན་རྣམས་ཀྱིས་དེའི་བདག་ཉིད་དུ་བྱེད་པའི་ཕྱིར་སེམས་ལ་ཤིན་ཏུ་སྒོ་བར་བྱེད་པ་ཡིན་ཏེ། མེ་ཏོག་རྣམས་ཀྱིས་ཏིལ་ལ་བསྒོས་པ་བཞིན་ནོ། །

[Block 1312]
རེ་ཞིག་སྦྱིན་པས་ནི་ལོངས་སྤྱོད་ཆེན་པོར་འགྱུར་རོ་ཞེས་བཤད་ན། ཡང་ན༌[^925]ཚུལ་ཁྲིམས་དང་བསྒོམ་པས༌[^926]ཅིར་འགྱུར་ཞེ་ན།

[Block 1313 [VERSE]]
མཐོ་རིས་དོན་དུ་ཚུལ་ཁྲིམས་དང་། །
འབྲལ་བའི་དོན་དུ་བསྒོམ་གཙོའི་ཕྱིར། །

[Block 1314]
སྦྱིན་པ་ཡང་མཐོ་རིས་ཀྱི་དོན་དུ་ནི་འགྱུར་མོད་ཀྱི་ཚུལ་ཁྲིམས་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1315]
ཚུལ་ཁྲིམས་ཀྱིས་ཀྱང་འབྲལ་བར་མི༌[^927]འགྱུར་མོད་ཀྱི་བསྒོམ་པ་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1316 [HEADING]]
#### ཚངས་པའི་བསོད་ནམས། ^1-71-4-0

[Block 1317]
མདོ་ལས་གང་ཟག་བཞི་ནི་ཚངས་པའི་བསོད་ནམས་སྐྱེད་དོ་ཞེས་གསུངས་པ། ཚངས་པའི་བསོད་ནམས་གང་ཞིག་ཡིན་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ། མཚན་མ༌[^928]རྣམ་པར་སྨིན་པ་ཅན་གྱི་ལས་ཀྱི་ཚད་ཤེས་པར་བྱ་བའི་ཕྱིར་བཤད་པ་གང་ཡིན་པའོ་ཞེས་ཟེར་རོ། །

[Block 1318]
སྔོན་གྱི་སློབ་དཔོན་རྣམས་ན་རེ།

[Block 1319 [VERSE]]
བསྐལ་པར་མཐོ་རིས་དག༌[^929]གནས་ཕྱིར། །
བཞི་ཡི་ཚངས་པའི་བསོད་ནམས་ཡིན། །

[Block 1320]
ཞེས་ཟེར་ཏེ། བསོད་ནམས་ཇི་ཙམ་གྱིས་ན་བསྐལ་པར་མཐོ་རིས་སུ་དགའ་བར་གནས་པར་འགྱུར་བ་འདི་ནི་ཚངས་པའི་བསོད་ནམས་ཡིན་ཏེ། ཚངས་པའི་མདུན་ན་འདོན་པ་རྣམས་ཀྱི་ཚེ་བསྐལ་པར་ཐུབ་པའི་ཕྱིར་རོ། །

[Block 1321]
སྡེ་པ་གཞན༌[^930]ལས་ཀྱང་།

[Block 1322 [VERSE]]
ཚངས་པའི་བསོད་ནམས་བསྐྱེད་པ་ནི། །
བསྐལ་པར་མཐོ་རིས་དགའ་བར་གནས། །
ཞེས་ཚིགས་སུ་བཅད་དེ་འབྱུང་ངོ་། །
ཟང་ཟིང་གི་སྦྱིན་པ་བཤད་ཟིན་ཏོ། །

[Block 1323 [HEADING]]
#### ཆོས་ཀྱི་སྦྱིན་པ། ^1-71-5-0

[Block 1324]
ཆོས་ཀྱི་སྦྱིན་པ་བརྗོད་པར་བྱ་སྟེ། དེས༌[^931]སྨྲས་པ།

[Block 1325 [VERSE]]
ཆོས་སྦྱིན་ཉོན་མོངས་ཅན་མིན་པས། །
མདོ་སོགས་ཡང་དག་ཇི་བཞིན་སྟོན། །

[Block 1326]
ཆོས་ཀྱི་སྦྱིན་པ་ནི་མདོ་ལ་སོགས་པ་ཉོན་མོངས་པ༌[^932]ཅན་མ་ཡིན་པས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་སྟོན་པའོ། །

[Block 1327]
དེའི་ཕྱིར་གང་དག་ཆོས་ལོག་པར་འཆད་པར་བྱེད་པའམ། སེམས་ཉོན་མོངས་པ༌[^933]ཅན་རྙེད་པ་དང་བཀུར་སྟི་དང་། གྲགས་པ་འདོད་པས་ཆད་པ༌[^934]དེ་དག་ནི་བདག་ཉིད་ཀྱི་བསོད་ནམས་ཆེན་པོ་ཉམས་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1328]
བསོད་ནམས་བྱ་བའི་གཞིར༌[^935]བྱེ་བྲག་གིས་དགེ་བ་རྣམ་པ་གསུམ་བཤད་ཟིན་ཏོ། །

[Block 1329]
[^936]

[Block 1330 [HEADING]]
### ཆ་མཐུན་དགེ་བ་གསུམ། ^1-72-0

[Block 1331 [VERSE]]
བསོད་ནམས་མྱ་ངན་འདས་པ་དང་། །
ངེས་འབྱེད་ཆ་མཐུན་དགེ་རྣམས༌[^937]གསུམ། །

[Block 1332 [HEADING]]
#### བསོད་ནམས་ཀྱི་ཆ་དང་མཐུན་པ། ^1-72-1-0

[Block 1333]
བསོད་ནམས་ཀྱི་ཆ་དང་མཐུན་པ་ནི་རྣམ་པར་སྨིན་པ་ཡིད་དུ་འོང་བ་ཅན་གང་ཡིན་པའོ། །

[Block 1334 [HEADING]]
#### ཐར་པའི་ཆ་དང་མཐུན་པ། ^1-72-2-0

[Block 1335]
ཐར་པའི་ཆ་དང་མཐུན་པ་ནི་གང་སྐྱེས་ན་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཆོས་སུ་ནམ༌[^938]འགྱུར་བ་སྟེ། གང་ལ་འཁོར་བའི་ཉེས་དམིགས་དང་། བདག་མེད་པ་དང་། དམྱལ་བ༌[^939]ལས་འདས་པའི་ཡོན་ཏན་བརྗོད་པའི་གཏམ་ཐོས་ནས་སྤུ་ཟིང་ཞེས་བྱེད་པ་དང་། མཆི་མ་འཁྲུག་ཅེས་བྱེད་པ་དེ་ལ་ནི་ཐར་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་ཡོད་པར་ཤེས་པར་བྱ་སྟེ། དབྱར་མྱུ་གུ་སྐྱེ་བ་ལས་ན་གཡུལ་གྱི་གསེབ་ན་ས་བོན་ཡོད་པར་ཤེས་པ་བཞིན་ནོ། །
--- END BLOCKS ---
