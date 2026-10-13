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
ཚེ་དང་ལྡན་པ་ཀུན་དགའ་བོ་རེག་པའི་སྐྱེ་མཆེད་དྲུག་པོ་ཟད་པ་དང་། འདོད་ཆགས་དང་བྲལ་བ་དང་། འགགས་པ་དང་། ཉེ་བར་ཞི་བ་དང་། ནུབ་པར་གྱུར་པ་འདི་ལས་གཞན་པའི་སྤྲོས་པས་སྤྲོས་པར་བྱེད་པ་ཡོད་དམ་ཞེས་པ་དང་། ཡོད་པ་དང་མེད་པ་ཞེས་པའི་སྤྲོས་པས་སྤྲོས་པར་བྱེད་དམ་ཞེས་པ་ནས། ཚེ་དང་ལྡན་པ་ཀུན་དགའ་བོ་སྐྱེ་མཆེད་དྲུག་ནི་སྤྲོས་པའོ། །

[Block 1297]
སྐྱེ་མཆེད་དྲུག་འགག་པ༌[^932]ལས་སྤྲོས་པ་མེད་པའོ་ཞེས་པའི་བར་དུ་མྱ་ངན་ལས་འདས་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་སོ། །

[Block 1298]
དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཀྱི་དབང་གིས་ན་དོན་དམ་པའོ། །

[Block 1299]
འཇིག་རྟེན་པའི་ཤེས་པའི་དབང་གིས་ཀྱང་ཀུན་རྫོབ་བོ་ཞེས་གནས་སོ། །

[Block 1300]
དེ་ཉིད་ཀྱིས་ན།

[Block 1301 [HEADING]]
### ཚིགས་བཅད་རེ་དགུ་པ། ^1-68-0

[Block 1302 [VERSE]]
འཇིག་རྟེན་པ་ཡི་ཆོས་བསྟན་མི་ཉམས་ཤིང་། །
ཡང་དག་ཉིད་དུ་ནམ་ཡང་ཆོས་བསྟན་མེད། །
དེ་བཞིན་གཤེགས་པས་གསུངས་པ་མ་རིག༌[^933]པས། །
དེས་ན་དྲི་མེད་བརྗོད་པ་འདི་ལ་སྐྲག །

[Block 1303]
དེས་ན་སྐྲག་ཅེས་པ་ལ། དེས་ནའི་སྒྲ་ནི་ཇི་སྐད་དུ་སྨོས་པའི་རིགས་པ་དང་ལུང་གིས་དཔྱད་པ་རྣམས་ཏེ། འཇིག་རྟེན་པའི་ཐོག་མར་བལྟ་བར་བྱ་སྟེ། དེས་ན་འཇིག་རྟེན༌[^934]པའི་ཞེས་བྱ་སྟེ། འདིར་ཚིགས་སུ་བཅད་པ་སྡེབས་པའི༌[^935]ངོར་འཇུག་པས་རིམ་པ་འཆོལ་བར་བལྟ་བར་བྱའོ། །

[Block 1304]
དེས་ན་འདིའི་དོན་ཀྱང་གང་གི་ཕྱིར་ཇི་སྐད་དུ་སྨོས་པའི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་བཤད་པར། བརྫུན་པ་སླུ་བའི༌[^936]ཆོས་ཅན་ཙམ་བྱིས་པའི་སྐྱེ་བོའི་བློའི་སྤྱོད་ཡུལ། རྨི་ལམ་དང་སྒྱུ་མ་དང་དྲི་ཟའི་གྲོང་ཁྱེར་གྱི་རྣམ་པ་ཅན་དེའི་རང་བཞིན་གྱི་ལས་ཀྱི་འབྲས་བུ་ཀུན་ནས་ཉོན་མོངས་པ་ཅན་དང་རྣམ་པར་བྱང་བ་འཆིང་བ་དང་གྲོལ་བའི་རྒྱུ་མཚན་འཇིག་རྟེན་པའི་ཐ་སྙད་དུ་ཡོད་པ་ཉིད་དུ་འདོད་པ་དེས་ན་དེའི་ཕྱིར། འཇིག་རྟེན་པ་ཡི་ཆོས་བསྟན་མི་ཉམས་ཤིང་། ཐ་སྙད་པ་ཉིད་ལ་ཇི་ལྟ་བའི་དོན་ཡིན་པའི་ཕྱིར་ཇི་ལྟར་གནས་པ་ཕྱིན་ཅི་མ་ལོག་པར་འཇིག་རྟེན་པའི་དངོས་པོ་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་བརྗོད་ལ། དེ་ཉིད་བརྗོད་བྱ༌[^937]ལས་རིམ་གྱིས་དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པའི་རྒྱུའི་ཕྱིར་ཡང་། འཇིག་རྟེན་པ་ཡི་ཆོས་བསྟན་མི་ཉམས་ཤིང་ངོ་། །འཇིག་རྟེན་པའི་ཆོས་བསྟན་པ་ཡང་དངོས་པོ་གང་ཅུང་ཟད་ཀྱི་རང་བཞིན་ཁས་མ་བླངས་པས། སྟོན་པ་དང་བསྟན་བྱ་དང་སྟོན་པ་པོ་རྣམས་རང་བཞིན་གྱིས་མ་གྲུབ་པའི་ཕྱིར། ཡང་དག་ཉིད་དུ་ནམ་ཡང་ཆོས་བསྟན་མེད། །དེ་བཞིན་གཤེགས་པས་ཆོས་འགའ་ཞིག་ཡང་དག་པར་དམིགས་ནས་ཉེ་བར་སྟོན་པར་མི་འགྱུར་ལ། དེས་ན་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་ཡོངས་སུ་མི་རྟོག་པས༌[^938]འདི་ནི་བདེན་ནོ་ཞེས་པར་མངོན་པར་ཞེན་པ་ཡོངས་སུ་བཏང་ནས་གནས་པའི་རྣལ་འབྱོར་པ་ངེས་པར་མྱ་ངན་ལས་འདས་པ་ལ་གཞོལ་བར་འགྱུར་རོ། །

[Block 1305]
དེ་ལྟར་ན་འདི་ནི་བདེན་པ་གཉིས་ལ་བརྟེན་ནས་ལས༌[^939]ཡོད་པའི་ཕྱིར་དང་རྟོག་པ་མེད་པའི་ཕྱིར་རྣལ་འབྱོར་པ་རྣམས་ཀྱི་མྱ་ངན་ལས་འདས་པ་གྲུབ་པ་ཡང་ཅུང་ཟད་ཀྱང་མི་ཉམས་ལ། གྲོལ་བ་ཡང་བདེ་བླག་ཁོ་ནར་མྱུར་དུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1306]
གལ་ཏེ་ཡང་རང་བཞིན་མེད་པ་ལ་ཕྱིན་ཅི་ལོག་པ་རྣམས་ཀྱིས་དེ་ཡོངས་སུ་མ་ཤེས་པས་རང་བཞིན་མེད་པ་ལ་དངོས་པོའི་རྒྱུ་མཚན་གྱིས་ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་སུ་འཇུག་ལ། ཕྱིན་ཅི་མ་ལོག་པ་རྣམས་རང་བཞིན་མེད་པ་མཐོང་བ་ལས་ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་ལས་ལོག་ནས་རྣམ་པར་བྱང་བ་ཡང་བསྐྱེད་དོ། །

[Block 1307]
དེ་ཅི་སླར་ཡང་འདིར་བརྗོད་པ་ལ་དེ་སྐྲག་པས་འཇིག་རྟེན་པ་རང་བཞིན་དང་བཅས་པར་སྨྲ་བ་ལ་བརྟེན། སྐྱོན་དང་ལྡན་པར༌[^940]བརྗོད་པ་ནི་སྤང་བར་རིགས་ལ། བརྗོད་པ་འདི་ནི་སྐྱོན་དང་ལྡན་པ་མ་ཡིན་ནོ། །

[Block 1308]
ཡོན་ཏན་དང་ལྡན་ན་ཡང་བརྗོད་པ་ལ་བརྟེན་པར་རིགས་ན། རང་བཞིན་དང་བཅས་པར་སྨྲ་བ་ནི་ཡོན་ཏན་དང་ལྡན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། དེ་ལ་འཇིག་རྟེན་པ་འདི་དག༌[^941]རང་བཞིན་སྨྲ་བ་སྤངས་ནས་རང་བཞིན་དང་བཅས་པར་སྨྲ་བ་ལ་ཇི་ལྟར༌[^942]ཞེ་ན། སྨྲས་པ། དངོས་པོ་ཇི་ལྟར་སྨྲས་པ་རྣམས་མི་སྲིད་པ་ཉིད་ཀྱིས། ཇི་སྐད་སྨོས་པའི་བརྗོད་པ་སྤངས་ནས་གནས་པས་འཇིག་རྟེན་པ་དངོས་པོའི༌[^943]ལྟ་བ་ལ་མི་གནས་ཤིང་ཕྱིན་ཅི་ལོག་ཇི་ལྟ་བར་གནས་སོ། །

[Block 1309]
འོ་ན་དེ་བཞིན་གཤེགས་པ་ཉི་མའི་གསུང་གི་འོད་ཟེར་གསལ་བར་སྣང་བས་ན་འཇིག་རྟེན་པ་རྣམས་ཀྱི༌[^944]ཕྱིན་ཅི་ལོག་པར་མི་རིགས་སོ། །

[Block 1310]
བདེན་ཏེ་གལ་ཏེ་འཇིག་རྟེན་པ་ལ་ཤེས་རབ་ཀྱི་མིག་ཡོད་ན་རིགས་ཀྱི་མ་རིག་པས་ལྡོངས་པའི་འཇིག་རྟེན་པས་ཇི་ལྟ་བའི་དེ་བཞིན་གཤེགས་པའི་གསུང་ལས་ཁོང་དུ་ཆུད་པར་ཇི་ལྟར་འགྱུར། དེ་མ་རྟོགས་པས་གདོན་མི་ཟ་བར་འཇིགས་པ་མ་ཡིན་པའི་གནས་ལ་སྐྲག་པར་འགྱུར་རོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1311 [VERSE]]
དེ་བཞིན་གཤེགས་པས་གསུངས་པ་མ་རིག་པས། །
དེས་ན་དྲི་མེད་བརྗོད་པ་འདི་ལ་སྐྲག །

[Block 1312]
ཅེས་པ་ལ། ཇི་ལྟར་བུད་ཤིང་ལ་བརྟེན་ནས་མེ་འབྱུང་ལ། སྤྲིན་ལ་བརྟེན་ནས་ཆར་པའོ་ཞེས་པ་ནི་འདིར་རྒྱུའི་དོན་ཏོ། །

[Block 1313]
དེ་བཞིན་དུ་གསུངས་པ་མ་རིག་པས་ཤེས་པ་འདིར་ཡང་ཀྟའི་རྐྱེན་གྱིས་རྒྱུའི་དོན་ཏོ། །

[Block 1314]
ཇི་སྐད་དུ་གསུངས་པའི་ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདེན་པ་ལ་མི་མཁས་པའི་སྐྱེ་བོས་དེ་བཞིན་གཤེགས་པས་གསུངས་པ་མི་ཤེས་ལ། མི་ཤེས་པས་གདོད་མ་ནས་ཞི་བ་སྐྱེ་བ་མེད་པའི་ཆོས་བསྟན་པ་ལ་ངེས་པར་སྐྲག༌[^945]པར་འགྱུར་རོ། །

[Block 1315]
དེ་ཡང་གདོད་མ་ནས་ཞི་བ་མ་སྐྱེས་པའི་ཆོས་བསྟན་པའི་རྣམ་པར་དབྱེ་བ་མི་མཐོང་ཞིང་། ཇི་ལྟར་ཉེ་བར་དམིགས་བཞིན་པའི་བདག་དང་བདག་གི་བའི་ཆོས་ཀྱི་དངོས་པོ་སེམས་ལ་བཞག་ནས། བདག་ནི་མེད་པར་གྱུར་ཏ་རེ་ཞེས་བྱིས་པ་དག་དྲི་མེད་ཀྱི་བརྗོད་བྱ་ལ་སྐྲག་པར་འགྱུར་རོ། །

[Block 1316]
བརྗོད་པར་བྱ་བའི་ཕྱིར་བརྗོད་པ་སྟེ་བཤད་པའི་དོན་ལ་བརྗོད་པ་ཞེས་བརྗོད་དེ། བསྟན་བཞིན་པའི་ཕྱིར་རོ། །

[Block 1317]
བརྗོད་པ་དེ་ཡང་མཚན་མ་མེད་པའི་ཕྱིར་དྲི་མ་མེད་པའོ། །

[Block 1318]
མི་གསལ་བ་མངོན་སུམ་མ་ཡིན་པ་ཞེས་བྱའོ། །འོ་ན་དྲི་མེད་བརྗོད་བྱ་འདི་ལ་སྐྲག །

[Block 1319]
ཅེས་པ་འདིར། འཇིགས་པའི༌[^946]རྒྱུ་ནི་འབྱུང་ཁུངས་སོ། །ཞེས་པས་འདིར་འབྱུང་ཁུངས་ལ་བརྟེན་ནས་ལྔ་པར་འགྱུར་རོ། །

[Block 1320]
མ་ཡིན་ཏེ་ཀྟའི་རྐྱེན་གྱིས་རྒྱུའི་དོན་གསུངས་པས་ཤེ༌[^947]ན། མ་ཡིན་ཏེ་དོན་གཞན་ཡིན་པའི་ཕྱིར་ཏེ། དྲི་མ་མེད་པའི་བརྗོད་བྱ་ཉིད་ལ་སྲོག་ཆགས་རྣམས་སྐྲག་པས་སོ། །

[Block 1321]
བརྗོད་བྱ་ཅིའི་ཕྱིར་ན་རྒྱུར་འགྱུར། དེ་ལས་སྐྲག་པས་སོ། །

[Block 1322]
དེ་ལ་འཇིགས་པའི་རྒྱུ་ཅི་ཞེ་ན། མ་རྟོགས་པ་རྒྱུར་ཀྟའི་རྐྱེན་གྱིས་བརྗོད་ལ། དེའི་ཕྱིར་འཇིགས་པའི་རྒྱུ་ཉིད་ནི་མ་རྟོགས་པ་རྒྱུ་མཚན་ནོ། །

[Block 1323]
དྲི་མ༌[^948]མེད་པའི་བརྗོད་བྱ་འཇིགས་པའི་རྒྱུའོ་ཞེས་པས༌[^949]ཡང་། གལ་ཏེ་དྲི་མ་མེད་པའི་བརྗོད་པ་འཇིགས་པའི་རྒྱུར་འགྱུར་ན་ལྔ་པར་འགྱུར་ལ། འདི་ནི་འཇིགས་པའི་རྒྱུ་མ་ཡིན་ཏེ། འཇིགས་པ་མ་ལུས་པ་ལས་ལྡོག་པའི་རྒྱུའི་ཕྱིར་རོ། །

[Block 1324]
དེ་ཉིད་ཀྱིས༌[^950]ན་གསུངས་པ།

[Block 1325]
རིན་པོ་ཆེ་ཕྲེང་བ་ལས།

[Block 1326 [VERSE]]
སྡུག་བསྔལ་ཐམས་ཅད་ཟད་བྱེད་ཆོས། །
ཐོས་པས་རྟོགས་པ་མི་ལྡན་པ། །
སྐྲག་འགྱུར་ཡོངས་སུ་མ་ཤེས་པས། །
འཇིགས་མིན་གནས་ལ་འཇིགས་པར་འགྱུར། །

[Block 1327 [VERSE]]
འདི་དག་ཐམས་ཅད་མི་འབྱུང་བའི། །
མྱ་ངན་འདས་པས་དེ་མི་འཇིགས། །
འདིར་སྨོས་པ་ཡི་དངོས་མེད་ལ། །
ཅི་ཡིས་དེ་ལ་དེ་འཇིགས་བྱེད། །

[Block 1328 [VERSE]]
ཐར་པ་བདག་མེད་ཕུང་པོ་མེད། །
འདི་འདྲའི་ཐར་པ་ལ་ཡང་དགའ། །
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་རྣམས། །
འདི་ལྟ་བུ་དེས་ཅི༌[^951]མི་དགའ། །

[Block 1329]
ཞེས་སོ། །

[Block 1330]
དེ་ཉིད་ཀྱིས་ན་འཇིགས་པའི་རྒྱུ་ཉིད་དུ་མ་ཡིན་པར་ཤེས་པར་བྱ་བའི་ཕྱིར། དྲི་མ་མེད་པའི་བརྗོད་པ་ཡུལ་མ་ཡིན་པར་བསྟན་ཏོ་ཞེས་ཤེས་པར་བྱའོ། །

[Block 1331]
གང་ཡང་འདི་སྙམ་དུ་སེམས་ཏེ། སྒྲའི་མཚན་ཉིད་ལ་མངོན་པར་ཞེན་པ་སྤང་བའི་དོན་དུ་སློབ་དཔོན་གྱི་བསམས་བཞིན༌[^952]དུ་ཟུར་ཆག་པའི་སྒྲའི་སྦྱོར་བ་བྱས་སོ་ཞེས་པ་དེ་མི་འཐད་དེ། །གལ་ཏེ་སྒྲའི་མཚན་ཉིད་བོར་ནས་བརྗོད་པས་དེས་མངོན་པར་ཞེན་པ་དང་བྲལ་ནས་སྒྲའི་མཚན་ཉིད་ལོགས་སུ་བོར་བའི་བརྗོད་པ་ལ༌[^953]མངོན་པར་ཞེན་པ་འབྱུང་བར་འགྱུར་ལ། དེ་ལྟར་ཡང་མ་ཡིན་ནོ། །

[Block 1332]
ཡང་ཇི་ལྟ་དེ་ལྟར་སྒྲའི་སྦྱོར་བ་བྱེད་ན། དེའི་ཚེ་ཚིག་ལྷུག་པ་ལ་ཡང་མངོན་པར་ཞེན་པ་སྤོང་བའི༌[^954]ཕྱིར་སྦྱོར་བ་མཛད་པར༌[^955]འགྱུར་ན། དེ་ཡང་མ་མཛད་ལ། དེའི་ཕྱིར་མཚན་ཉིད་མི་དྲན་པ་ཉིད་སྲིད་ཀྱི་མཚན་ཉིད་ལ་མངོན་པར་ཞེན་པ་སྤོང་བས་ནི་ཡིན་ནོ། །

[Block 1333]
ཐབས་གཞན་གྱིས་དེའི་མངོན་པར་ཞེན་པ་སྤོང་བར་བྱེད་པ་མེད་པ་མ་ཡིན་ལ། དེའི་ཕྱིར་སློབ་དཔོན་ནི་ནམ་ཡང་ཟུར་ཆག་པའི་སྒྲའི་སྦྱོར་བ་མི་མཛད་དོ། །

[Block 1334]
འོ་ན་རེ་ཞིག་འགྲོ་བ༌[^956]མི་འགྲོ་ཞིང་། །ཞེས་པ་ལ་སོགས་པ་ཟུར་ཆག་པའི་སྒྲའི་སྦྱོར་བ་མཐོང་བ་མ་ཡིན་ནམ་ཞེ་ན། འདི་ནི་ཟུར་ཆག་པའི་སྒྲ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་བཟློག་པ་ནི་མང་པོའོ་ཞེས་པས་འདི་ནི། ས་མཐའི༌[^957]རི་མཐའ་ཉེ་བར་གཟུང་བ་རྟགས་དང་སྐྱེས་བུ་དང་། །

[Block 1335 [VERSE]]
ཀ་ལ་ཧལ་དབྱངས་ཡིག་བྱེད་པོ་ཡ་ང་ཉ། །
བསྟན་བཅོས་བྱེད་པས་འདི་དག་བཟློག་པ་སྟེ། །
དེས་ཀྱང་མང་པོ་འགྲུབ་པར་འགྱུར་ཞེས་བྱ། །
--- END BLOCKS ---
