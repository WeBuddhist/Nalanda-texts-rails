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
[Block 1051]
རྟོགས༌[^919]པའི་ཡེ་ཤེས་ཀྱི་ཕྱིར་ཞི་བའི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་དབང་པོ་མ་ཞི་ཞིང་ཆགས་པར་འགྱུར་བའི་རྒྱུའི་ཆོས་རྣམས་རང་བཞིན་གྱིས་མ་བྱུང་མ་སྐྱེས་པར་རྟོགས་པས༌[^920]དེ་ལ་མ་གཡེངས་པའི་ཕྱིར་ཞི་བའི་རྣམ་པ་སྟེ། ཞི་བའི་རང་བཞིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1052]
མི་རྒོད་པའི་ཕྱིར་རབ་ཏུ་ཞི་བའི་རྣམ་པ་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་ལྟར་རྒོད་པར་བྱ་བའི་ཡུལ་མེད་པས་ན་རབ་ཏུ་ཞི་བའི་རྣམ་པའོ། །

[Block 1053]
ཁེངས་པ་མ་ཡིན་པའི་ཕྱིར་ཤིན་ཏུ་སྦྱངས་པའི་རྣམ་པའོ་ཞེས་བྱ་བ་ལ། [^921]ཉོན་མོངས་པ་རྣམས་མ་སྤངས་པ་ནི་ཁེངས་པ་སྟེ། ཉོན་མོངས་པ་མ་སྤངས་པ་མ་ཡིན་པ་ནི་ཁེངས་པ་མ་ཡིན་པའོ། །

[Block 1054]
དེ་བས་ན་ཤིན་ཏུ་སྦྱངས་པའི་རྣམ་པ་སྟེ། ཉོན་མོངས་པ་དག་པའི་རྣམ་པའམ།[^922] ཉོན་མོངས་པ་དུལ་བའི་རྣམ་པ་ཞེས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1055]
རྣམ་པར་མི་གཡེངས་པའི་ཕྱིར་དབང་པོ་དགའ་བའི་རྣམ་པ་ཞེས་བྱ་བ་ནི་སེམས་གཡེངས་པ་ལས་དབང་པོ་འཁྲུག་པར༌[^923]འགྱུར་གྱི། སེམས་ཡུལ་ལ་སོགས་པ་ལ་མ་གཡེང་སྟེ།[^924] ཏིང་ངེ་འཛིན་དུ་གྱུར་པ་ལས་ཞི་ཞིང་དགའ་བར་འགྱུར་བས་ན་དབང་པོ་དགའ་བའི་རྣམ་པའོ། །

[Block 1056]
མི་ཉམས་པའི་ཕྱིར་བརྟུལ་ཞུགས་ཀྱི་རྣམ་པ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་བརྟུལ་ཞུགས་གང་བླངས་པ་དེ་མ་ཞིག་མ་ཉམས༌[^925]རང་བཞིན་གཞན་དུ་མ་གྱུར་པས་ན་བརྟུལ་ཞུགས་ཀྱི་རྣམ་པ་ཞེས་བྱའོ། །

[Block 1057]
འདོད་པའི་ཕྱིར་ངེས་པའི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་དགའ་བ་དང་ལྡན་པ་དེ་ཐམས་ཅད་ཀྱིས་ཡིད་དུ་འོང་ཞིང་འདོད་པས་འགྱུར་བས་ན་ངེས་པའི་རྣམ་པ་སྟེ། ཡིད་དུ་འོང་བའི་རྣམ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1058]
བཀའ་བློ་བདེ་བའི་ཕྱིར་ཐོས་པའི་རྣམ་པ་ཞེས་བྱ་བ་ནི་ཇི་སྐད་བསྒོ་བ་བཞིན་ཉན་དུ་བཏུབ་པ་ནི་བཀའ་བློ་བདེ་བ་སྟེ། དེ་བས་ན་ཐོས་པའི་རྣམ་པའོ། །

[Block 1059]
ཐོས་པའི་རྣམ་པ་ཞེས་བྱ་བ་ནི་ཇི་སྐད་བསྒོ་བ་བཞིན་དུ་ཉན་དུ་བཏུབ་པའི་རང་བཞིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1060]
སེམས་ལས་སུ་རུང་བའི་ཕྱིར་ཉེ་བར་ཞི་བའི་རྣམ་པའོ་ཞེས་བྱ་བ་ལ། ཞུམ་པ་དང་རྒོད་པ་སྤངས་པ་ནི་སེམས་ལས་སུ་རུང་བའི་རྣམ་པའོ། །

[Block 1061]
དེ་བས་ན་ཉེ་བར་ཞི་བའི་རྣམ་པ་སྟེ། ཞུམ་པ་དང་རྒོད་པ་མེད་པའི་རང་བཞིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1062]
ལས་ལེགས་པར་བྱས་པའི་ཕྱིར་དགའ་བའི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་ལས་དགེ་བ་བྱས་པའི་ཕྱིར་རྣམ་པ་སྟེ། སེམས་མི་དགའ་བ་མེད་པའི་རྣམ་པའོ། །

[Block 1063]
ཁ་ན་མ་ཐོ་བ་མེད་པའི་ཕྱིར་མི་འགྱོད་པའི་རྣམ་པ་ཞེས་བྱ་བ་ནི་སྡིག་པ་མ་བྱས་པའི་ཕྱིར་མི་འགྱོད་པའི་རྣམ་པ་སྟེ། སྡིག་པའི་རྒྱུས་མ་འོངས་པ་ན་འདི་འདྲ་བར་འགྱུར་རོ་ཞེས་གདུང་བ་མེད་པའོ། །

[Block 1064]
མ་གཡོས་པའི་ཕྱིར་ཤིན་ཏུ་གནས་པའི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་མི་མཐུན་པའི་ཕྱོགས་ལ་སོགས་པས་མ་གཡོས་པའི་ཕྱིར་ཤིན་ཏུ་གནས་པའི་རྣམ་པ་སྟེ། བརྟེན་པའི༌[^926]རྣམ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1065]
མི་གནས་པའི་ཕྱིར་མ་གཡོས་པའི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་མཚན་མ་དང་དངོས་པོ་ལ་མི་གནས་པས་མ་གཡོས་པའི་རྣམ་པ་སྟེ། མཚན་མ་རྣམས་ཀྱི་དབང་དུ་མི་འགྱུར་བའི་རང་བཞིན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1066]
ཐུལ་བར་དཀའ༌[^927]བས་བསྙེན་པར༌[^928]དཀའ་བ་ཞེས་བྱ་བ་ནི་བདུད་དང་ཕས་ཀྱི་རྒོལ་བ་རྣམས་ཀྱིས་ཐུལ་བར་དཀའ་བ༌[^929]བསྙེན་དཀའ་བའི་རྣམ་པ་སྟེ། དེ་དག་གིས་ཟིལ་གྱིས་མི་ནོན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1067]
ཆུད་མི་ཟ་བའི་ཕྱིར་དོན་གྱི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་དོན་རྟོགས་ཤིང་ཐོབ་པའི་དངོས་པོ་ཉམས་པར་མི་འགྱུར་བས་ན་དོན་གྱི་རྣམ་པའོ། །

[Block 1068]
མ་ནོར་བ་དེ་བཞིན་ཉིད་ཀྱི་ཕྱིར་བདེན་པའི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་འཕགས་པའི་བདེན་པ་བཞི་དང་མཐུན་པའི་ཕྱིར་བདེན་པའི་རྣམ་པའོ། །

[Block 1069]
དེ་བྱེད་པའི་ཕྱིར་དེ་ཁོ་ནའི་རྣམ་པའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བའི་སྒྲ་ནི་དེ་ཁོ་ན་ཉིད་ལ་བྱ་སྟེ། དེ་ཁོ་ན་ཉིད་སྒྲུབ་པའམ་རྟོགས་པར༌[^930]བྱེད་པའི་ཕྱིར་དེ་ཁོ་ནའི་རྣམ་པའོ། །

[Block 1070]
སྟོབས་ཀྱི་ཕྱིར་སྤྲོ་བའི་རྣམ་པའོ་ཞེས་བྱ་བ་ལ། སྤྲོ་བ་ཉིད་མཐུ་དང་ལྡན་ཏེ་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་ཉམས་པར་མི་འགྱུར་བ་ལ་སྟོབས་ཞེས་བྱ་སྟེ། དེ་ལྟར་སྟོབས་ཀྱི་ཕྱིར་སྤྲོ་བའི་རྣམ་པ་སྟེ། སྤྲོ་བའི་མཐུ་དང་ལྡན་པའི་རྣམ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1071]
མི་བརྫི་བའི༌[^931]ཕྱིར་སྟོབས་ཀྱི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་དད་པའི་སྟོབས་ལ་སོགས་པ་ལ། མ་དད་པ་ལ་སོགས་པས་མི་བརྫི་བའི༌[^932]ཕྱིར་སྟོབས་ཀྱི་རྣམ་པའོ། །

[Block 1072]
སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཅེས་བྱ་བ་ལ་སོགས་པས།[^933] སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་རྫོགས་པར་བྱ་བ་ཚོལ་བས་མི་སྐྱོ་བའི་ཕྱིར། སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའི་རྣམ་པའོ། །

[Block 1073]
དགའ་བ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1074 [HEADING]]
### མཉམ་པར་གནས་པ། ^2-4-0

[Block 1075]
མཉམ་པ་ཉིད་ལ་གནས་པར་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་གཞན་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བཏང་སྙོམས་མི་ཟད་པ་ཡང་དགའ་བ་མི་ཟད་པ་ལ་སོགས་པ་བཤད་པའི་ཚུལ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 1076]
དེ་ཡང་རྣམ་པ་གཉིས་ཀྱི༌[^934]ཚུལ་དུ་ཤེས་པར་བྱ་སྟེ། བསྟན་པའི་ཚུལ་དང་བཤད་པའི་ཚུལ་ལོ། །

[Block 1077 [HEADING]]
#### བསྟན་པའི་ཚུལ། ^2-4-1-0

[Block 1078]
དེ་ལ་བསྟན་པའི་ཚུལ་ནི། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བཏང་སྙོམས་རྣམ་པ་གསུམ་སྟེ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། དུས་དང་དུས་མ་ཡིན་པ་ལ་བཏང་སྙོམས་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་བསྟན་ཏོ། །

[Block 1079]
དེ་མན་ལྷག་མ་ཐམས་ཅད་ཀྱིས༌[^935]བཤད་པའི་ཚུལ་བསྟན་ཏོ། །

[Block 1080]
ཉོན་མོངས་པ་ལ་བཏང་སྙོམས་པ་ནི་ཆགས་པར་འགྱུར་བ་དང་། ཁྲོ་བར་འགྱུར་བའི་ཡུལ་གཉི་ག་ལ་མཚུངས་པར་ལྟ་བའོ། །

[Block 1081]
བདག་དང་གཞན་བསྲུང་བའི་བཏང་སྙོམས་ནི་བདག་གི་སེམས་ཀྱི་རྒྱུད་འཁྲུག་ཅིང་གདུང་བར༌[^936]མི་འགྱུར་བ་དང་། གཞན་གྱི་སེམས་ཀྱི་རྒྱུད་འཁྲུག་པར་མི་འགྱུར་བར་བཏང་སྙོམས་པའོ། །

[Block 1082]
དུས་དང་དུས་མ་ཡིན་པ་ལ་བཏང་སྙོམས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དུས་དང་སྣོད་དུ་སྦྱར་ལ། དུས་ཁ་ཅིག་ཏུ་སྣོད་ལ་ལ་ལ་ཆོས་མི་བཤད་ཅིང་མི་སྒྲུབ་པ་བཏང་སྙོམས་སུ་འདོར་བའོ། །

[Block 1083 [HEADING]]
#### བཤད་པའི་ཚུལ། ^2-4-2-0

[Block 1084 [HEADING]]
##### ཉོན་མོངས་པ་ལ་བཏང་སྙོམས་པ། ^2-4-2-1-0

[Block 1085]
ཉོན་མོངས་པ་ལ་བཏང་སྙོམས་པའི་མཚན་ཉིད་གང་ཡིན་པ་རྒྱ་ཆེར་བསྟན་པའི་ཕྱིར། དེ་ལ་ཉོན་མོངས་པ་ལ་བཏང་སྙོམས་པ་གང་ཞེ་ན༌[^937]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1086]
བསྟི་སྟང་དུ་བྱས་པས་མ་ཐོས་པར༌[^938]སེམས་པ་དང་། བསྟི་སྟང་དུ༌[^939]མ་བྱས་པས་དམས་པར་སེམས་པ་ནི་ཉོན་མོངས་པ་སྟེ། བསྟི་སྟང་དུ་བྱས་ཀྱང་མཐོས་པར་མི་སེམས་ལ་བསྟི་སྟང་དུ་མ་བྱས་ཀྱང་དམས་པར་མི་སེམས་པ་ནི་ཉོན་མོངས་པ་ལ་བཏང་སྙོམས་པ་སྟེ། ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 1087]
རྙེད་པ་རློམ་སེམས་མེད་ཅེས་བྱ་བ་ནི་ཆོས་གོས་དང་ལྷུང་བཟེད་ལ་སོགས་པ་རྙེད་ཀྱང་རྙེད་དོ་ཞེས་རློམ་སེམས་མེད་པའོ། །

[Block 1088]
སྙན་པ་ནི་བདག་གི་ཡོན་ཏན་ནོ། །

[Block 1089]
མི་སྙན་པ་ནི་སྐྱོན་བརྗོད་པའོ། །

[Block 1090]
བསྔགས་པ་ལ་ཆོས་ཉིད་རབ་ཏུ་གནས་ཞེས༌[^940]བྱ་བ་ལ། བསྔགས་པ་ནི་ཡོན་ཏན་དངོས་སུ་བརྗོད་པའོ། །
--- END BLOCKS ---
