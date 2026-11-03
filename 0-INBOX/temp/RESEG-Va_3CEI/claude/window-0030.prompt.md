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
[Block 1051 [HEADING]]
###### **ད་ལྟར་ངས་བསྟན་པའི་ཆོས་ལུགས།** ^4-2-10-1-4-3-0

[Block 1052]
ང་ཡང་ཆོས་ལུགས་འདི་ལ་བརྟེན་ཏེ། ཐམས་ཅད་ཀྱི་ཆོས་ཀྱང་དེའོ་ཞེས་བསྟན་པ་སྟེ། སངས་རྒྱས་ཉག་གཅིག་ལ་སྣ་ཚོགས་མཁྱེན་པའི་སྟོབས་མངའ་བས་སེམས་ཅན་གྱི་དབང་པོ་སྣ་ཚོགས་མཁྱེན་ཅིང་ཡེ་ཤེས་ཀྱི་སྟོབས༌[^1053]ཤིན་ཏུ་མོས་པ་མཁྱེན་ཏེ་མོས་པའི༌[^1054]ནི་སྤྱོད་པ་ལ་མོས་པའོ། །

[Block 1053]
ཁམས་སྣ་ཚོགས་མཁྱེན་པའི་སྟོབས་མངའ་བས་རང་བཞིན་མཁྱེན་ཏེ། རིགས་མ་ངེས་པའི་ཁམས་སུ་གཏོགས་པ་མོས་པ་བསྐྱེད་པའི་ཕྱིར་སྔར་ཐེག་པ་གསུམ་ཐབས་ཙམ་དུ་གསུངས་ནས། ཕྱིས་མཐར་ཕྱིན་པའི་ཐེག་པ༌[^1055]གསུངས་ཏེ། སོ་སོའི་སྐྱེ་བོ༌[^1056]དག་སངས་རྒྱས་ཀྱི་ཐེག་པ་གཅིག་ཐོབ་པ་དང་རྣམ་པ༌[^1057]ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་མདོ་ལས་ཐེག་པ་གཅིག་ལས༌[^1058]བརྩམས་ཏེ་ཐམས་ཅད་མཁྱེན་པའི་མཐའི་བར་དུ་གསུངས་སོ། །

[Block 1054 [HEADING]]
###### འཛིན་པ་རྣམ་གཉིས་བསྩལ་བ། ^4-2-10-1-5-0

[Block 1055]
མདོ་ལས་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་ཐེག་པ་གཉིས་སུ་གདགས་པ་ཡང་མེད་ན་གསུམ་དུ་ལྟ་ཅི་སྨོས་ཞེས་པའི་བར་དུ་ནི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་གཉིས་པ་ཡང་མེད་ན་ཉན་ཐོས་ཀྱི་ཐེག་པ་གསུམ་པ་ཡོད་པ་ལྟ་ཅི་སྨོས་ཞེས་བསྟན་པ་སྟེ། མདོ་ལས་རའི་ཤིང་རྟ་དང་རི་དགས་ཀྱི་ཤིང་རྟ་དང་། གླང་པོ་ཆེའི་ཤིང་རྟ་འདོད་པའི་ཕྱིར་མེ་འབར་བའི་གྲོང་ཁྱེར་ལས་བྱུང་བ་ནི་ཐེག་པ་གཉིས་བསལ་བར༌[^1059]ཟད་ཀྱི་གླང་པོ་ཆེའི་ཐེག་པ་ཡང་བསལ་བ་མ་ཡིན་ཏེ་དེ་བས་ནི༌[^1060]འདི་ལ་ཐེག་པ་གཉིས་ཀྱི་མྱ་ངན་ལས་འདའ་བ་དང་མཐར་ཕྱིན་པ་མེད་དོ་ཞེས་གསུངས་སོ། །

[Block 1056]
འགྲེལ་པ་ལས་ཐེག་པ་གཉིས་མེད་པ་ནི་ཐེག་པ་གཉིས་ཀྱི་མྱ་ངན་ལས་འདའ་བ་མེད་པ་སྟེ། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཉག་གཅིག་གིས་མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་བརྙེས་ཏེ། ཡེ་ཤེས་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པའི་མཐར་ཕྱིན་པས་མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 1057]
དེ་ཡང་དངོས་པོ་གསུམ་ཡོངས་སུ་རྫོགས་ཏེ་ཐེག་པ་གཉིས་པ་ལྟར་བརྟགས་ཏེ་འགོག་པ་ལ་ལྟོས་པ༌[^1061]མ་ཡིན། ཡེ་ཤེས་ཆེན་པོའི་ཆོས་ཀྱི་སྐུ་ཡོད་པ་མ་ཡིན། མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ཡོད་པ་མ་ཡིན་ཏེ། སངས་རྒྱས་ཀྱི་ཐེག་པ་འབའ་ཞིག་ལ་མངའོ། །

[Block 1058]
འགྲེལ་པ་ལས་ལུང་བསྟན་པའི་ནང་ནས་དོན་རྣམ་པ་དྲུག་གིས་ཆོས་གང་བསྟན་པ་ལ་སོགས་པ་དོན་རྣམ་པ་ལྔ་བསྟན་པ་ལ།[^1062] ཆོས་གང་ལ་སོགས་པ་ཞེས་བྱ་བ་ནི་མ་ཐོས་པ་ཐོས་པར་བྱ་བ་སྟེ། སྔོན་མ་བྱུང་བའི་ཆོས་བསྟན་ནས་ཐོས་པར་བྱེད་པའོ། །

[Block 1059]
ཆོས་གང་དག་ཅེས་བྱ་བ་ནི་སྣ་ཚོགས་བསྒྲུབ་པར་བཤད་པ་དང་། རྒྱུ་དང་གཞི་རྣམ་པ་ཐ་དད་པ་བསྟན༌[^1063]པ་དང་། དམིགས་པ་དང་ངེས་པའི་ཚིག་གིས་ཐབས་ལ་མཁས་པ་བསྟན་པའོ། །

[Block 1060]
ཆོས་ཇི་ལྟ་བུ་ཞེས་བྱ་བ་ནི༌[^1064]གང་ལ་བརྟེན་ཞེ་ན་བྱ་བའི་དོན་ཆེན་པོ་གཅིག་གི་ཕྱིར་ཞེས་སྨོས་པའོ། །

[Block 1061]
ཆོས་ཀྱི་མཚན་ཉིད་ཇི་ལྟ་བུ་ཞེས་པ་ནི་ཐེག་པ་གཅིག་ལ་གནས་ནས་སེམས་ཅན་གྱི་དབང་པོ་ཇི་ལྟ་བ་བཞིན་དུ་སངས་རྒྱས་ཀྱི་རང་བཞིན་ཡོད་དེ། སངས་རྒྱས་ཀྱི་ཆོས་ལ་གནས་པའོ། །

[Block 1062]
ཇི་ལྟ་བུའི་རང་བཞིན་ཞེས་པ༌[^1065]ནི་ཐེག་པ་གཉིས་ཀྱི་རང་བཞིན་བསལ་ཏེ། ཐེག་པ་གཅིག་གི༌[^1066]རང་བཞིན་འབའ་ཞིག་གོ་ཞེས་སྨོས་པ་དེ་དག་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཆོས་ཀྱི་སྐུ་མཉམ་པའོ། །

[Block 1063 [HEADING]]
##### ཐེ་ཚོམ་རྣམ་བཞི་བསྩལ་བ། ^4-2-10-2-0

[Block 1064]
མདོ་ལས་འོན་ཀྱང་དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནས་ཚེའི་རྙོག་མ༌[^1067]ལ་བྱུང་ན་ཞེས་པའི་བར་དུ་ནི་འདིར་ཡང་དག་པའི་མཚན་ཉིད་བསྟན་པ་སྟེ། འདི་མན་ཆད་ཐེ་ཚོམ་རྣམ་པ་བཞི་འགྲེལ་པ་ལས་དོན་རྣམ་པ་ལྔས༌[^1068]སྟོན་ཏེ། ཐེ་ཚོམ་རྣམ་པ་བཞི་གང་ཞེ་ན་ནམ་ཞིག་སྟོན་པར་འགྱུར་བ་དང་། ང་རྒྱལ་གྱི་དབང་དུ་གྱུར་པ༌[^1069]ཇི་ལྟར་ཤེས་པ་དང་། བསྟན་པའི་སྣོད་དུ་ཇི་ལྟར་འགྱུར་བ༌[^1070]དང་ཇི་ལྟར་ན་བརྫུན༌[^1071]དུ་མི་འགྱུར་བ་དང་བཞིའོ། །

[Block 1065 [HEADING]]
###### ནམ་ཞིག་སྟོན་པར་འགྱུར་བ། ^4-2-10-2-1-0

[Block 1066]
སྐབས་འདིར་ཐེ་ཚོམ་དང་པོ་བསལ་བ༌[^1072]བསྟན་ཏེ། འགྲེལ་པ་ལས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ནམ་ཞིག་གི༌[^1073]དུས་ན་ཐབས་ཙམ་དུ་བསྟན་པ་སྟོན་པར་འགྱུར་བ་དང་། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ནམ་ཞིག་གི་དུས་ན་སྔར་ཐེག་པ་གཉིས་ཐབས་ཙམ་དུ་བསྟན་ཏེ། ཕྱིས་ཐེག་པ་གཅིག་པ་ཡང་དག་པ་བསྟན་པར་འགྱུར་ཞེས་སྨོས་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། སྔར་རྙོག་པ་ལྔའི་དུས༌[^1074]བྱུང་བ་བསྟན་པ་དང་། ཕྱིས་ཅིའི་ཕྱིར་བསྟན་པ་སྟེ་རྙོག་པ་ལ་ཡང་རྣམ་པ་ལྔའོ། །

[Block 1067 [HEADING]]
###### **རྙོག་པ་ལྔའི་དུས་བྱུང་བ་བསྟན་པ།** ^4-2-10-2-1-1-0

[Block 1068]
མིང་བསྟན་པ་དང་། མཚན་ཉིད་བསྟན་པ་དང་གཉེན་པོ་དང་བཞག་པ་དང་གཟུགས་དང་གཅིག་གིས་གཅིག་བསྡུ་བ་དང་ལྔའོ། །

[Block 1069 [HEADING]]
###### **མིང་བསྟན་པ།** ^4-2-10-2-1-1-1-0

[Block 1070]
དེ་ལ་མིང་བསྟན་པ་ནི་རྙོག་པ་སྟེ། རྙོག་ཅེས་བྱ་བ་ནི་དྲི་མའང༌[^1075]མི་གཙང་བའི་དོན་ཏོ། །

[Block 1071]
དཔེར་ན་ཁ་ཟས་མི་གཙང་བ་དྲི་མ་ཅན་ནི་བཙོག་པ༌[^1076]སྟེ་རྙོག་པ་ཞེས་བྱའོ། །

[Block 1072]
མདོར་ན་བསྐལ་པ་སྐྱེ་བའི་ཚེ་བསྐལ་པ་གསུམ་ནི་བགས་གྱིས༌[^1077]དམས། ཉོན་མོངས་པ་ནི་ཁད་ཀྱིས༌[^1078]བསྲབས་ཏེ། སེམས་ཅན་དག་དགེ་བ་ལ་ཕྱོགས་ཤིང་ལོག་པར་ལྟ་བ་ཉུང་བས་ཚེའི་དབང་པོ་ནི་ཕྱི་ཕྱིར་རིང་། བཟང་ཞིང་ལེགས་པ་ནི་ཕྱི་ཕྱིར་སྐྱེ་བ་དང་སེམས་ཅན་སྡུག་བསྔལ་བ་མེད་ཅིང་སངས་རྒྱས་སྤྲུལ་པ་འཇིག་རྟེན་དུ་མ་བྱུང་བའི་དུས་ནི་གཙང་མ་ཞེས་བྱའོ། །

[Block 1073]
སངས་རྒྱས་སྤྲུལ་པ་འཇིག་རྟེན་དུ་བྱུང་ན་བསྐལ་པ་འགྲིབ་པའི་དུས༌[^1079]འབྱུང་དུ་ཉེ་སྟེ། བསྐལ་པ་ཆུང་ངུ་གསུམ་ཡང་བགས་ཀྱིས༌[^1080]འབྱུང་། ཉོན་མོངས་པ་ཡང་ཕྱི་ཕྱིར་སྐྱེ། སེམས་ཅན་ཡང་ཉེས་པ་ལ་དགའ་ཞིང་ལྟ་བ་ལ་ཕྱི་ཕྱིར་ཞེན་པ་དང་། ཚེའི་དབང་པོ་ཕྱིར་ཞིང་ཐུང་བ་དང་། ཕྱི་ཕྱིར་ཞིང་ངན་ལ་བཙོག༌[^1081]པའི་དུས་ནི་རྙོག་པ་ཞེས་བྱའོ། །

[Block 1074]
ལྔ་ཞེས་པ་ནི་གྲངས་བསྟན་པའོ། །

[Block 1075 [HEADING]]
###### **མཚན་ཉིད་བསྟན་པ།** ^4-2-10-2-1-1-2-0

[Block 1076]
དེ་ལ་མཚན་ཉིད་བསྟན་པ་ནི་འགྲེལ་པ་ལས་ད་ལྟར་གྱི་མི་རྣམས་རབ་ཏུ་ཚེ་ཐུང་སྟེ་ལོ་བརྒྱ་ལས་མི་འདའ་བ་ནི་ཚེའི་རྙོག་པ་ཞེས་བྱ་སྟེ། ཀུན་གཞིའི༌[^1082]རྣམ་པར་ཤེས་པ་ལ་བག་ཆགས་ཀྱི་རྣམ་པས་ལས་ཐ་དད་པར་གྱུར་པ་ནི་ཚེའི་དབང་པོའི་མཚན་ཉིད་དོ། །

[Block 1077]
དགེ་བའི་ལས་ཀྱི་འབྲས་བུའི་མཐུ་ཞན་པར་གྱུར་ཏེ། ཚེའི་དབང་ཕྱི་ཕྱིར༌[^1083]ཐུང་བར་གྱུར་བ་ནི་སྲོག་གཅོད་པའི་ལས་ཀྱི་དབང་གིས༌[^1084]གྱུར་ཏོ། །

[Block 1078]
སེམས་ཅན་གང་ཕ་མར༌[^1085]མི་ཤེས་པ་དང་དགེ་སྦྱོང་དང་བྲམ་ཟེ་དང་བླ་མར༌[^1086]མི་ཤེས་པ་དང་། ཆོས་མི་ཤེས་པ་དང་། འཇིག་རྟེན་འདི་དང་འཇིག་རྟེན་ཕ་རོལ་ལས་ཀྱི་རྣམ་པར་སྨིན་པས་མི་འཇིགས་མི་སྐྲག་པ་དང་། སྦྱིན་པ་མི་བྱེད་བསོད་ནམས་མི་བྱེད་ཅིང་། ཚུལ་ཁྲིམས་མི་བསྲུང་བ༌[^1087]སྟེ། མདོར་ན་སྡིག་པ་བྱེད་ཅིང་དགེ་བ་མེད་པ་ནི་སེམས་ཅན་གྱི་རྙོག་པ་ཞེས་བྱའོ། །

[Block 1079]
སེམས་ཅན་གང་ཆོས་མ་ཡིན་པ་ལ་ཆགས་པ་མཚོན་ཆ་དང་། སེམས་ཅན་ལ་གནོད་པར་འགྱུར་བའི་ཡོ་བྱད་སྦྱིན་པ་དང་། འཐབ་ཅིང་རྩོད་པ་ལ་དགའ་བ་དང་། བརྫུན་དང་གཡོ་སྒྱུ་བྱེད་པ་དང་། ལོག་པའི་ཆོས་འཛིན་ཅིང་དགེ་བའི་ཆོས་མ་ཡིན་པ་སྤྱོད་པ་ནི་ཉོན་མོངས་པའི་རྙོག་པ་ཞེས་བྱ་སྟེ། ལྟ་བ་ལྔ་མ༌[^1088]གཏོགས་པ༌[^1089]ཉོན་མོངས་པ་ཐམས་ཅད་དང་ཉེ་བའི་ཉོན་མོངས་པ་ཐམས་ཅད་ནི་ཉོན་མོངས་པའི་རྙོག་པའི་མཚན་ཉིད་ཅེས་བྱའོ། །

[Block 1080]
ཆོས་མ་ཡིན་པའི་འདོད་ཆགས་ཀྱི་མཚོན་ཆ་ལ་སོགས་པ་བྱིན་ཏེ་གསོད་དུ་བཅུག་པ་དང་། ནོར་རྫས་ལ་ཆགས་ཏེ་མཚོན་ཆ་བྱིན་པས་འཐབ་ཅིང་རྩོད་པའི་གཞིར་གྱུར་པ་དང་། གཞན་ཡང་སྡིག་པ་མི་དགེ་བའི་ཆོས་སུ་གཏོགས་པ་ཉོན་མོངས་པ་དང་། ཉེ་བའི་ཉོན་མོངས་པ་བག་ཆགས་ཀྱི་དབང་གིས་ཉོན་མོངས་པ་སྐྱེ་བ་དང་། འཇིག་རྟེན་ན་དམ་པའི་ཆོས་ནུབ་སྟེ། ནམ་གཟུགས་བརྙན་ཙམ་ལ་སྤྱད་པ་ལོག་པར་ལྟ་བ་སྐྱེས་པ་ནི་ལྟ་བའི་རྙོག་པ་ཞེས་བྱའོ། །

[Block 1081]
མུ་སྟེགས་ཅན་ངན་པར་ལྟ༌[^1090]བ་མང་དུ་བྱུང་སྟེ། མུ་གེའི་བསྐལ་པ་དང་ནད་ཀྱི་བསྐལ་པ་དང་། མཚོན་གྱི་བསྐལ་པ་བྱུང་བ་ནི་བསྐལ་པའི་རྙོག་པ་ཞེས་བྱའོ། །

[Block 1082 [HEADING]]
###### **གཉེན་པོ།** ^4-2-10-2-1-1-3-0

[Block 1083]
དེ་ལ་གཉེན་པོ་ནི་སྤྱོད་པ་ལས་གཉེན་པོ༌[^1091]བསྟན་ཏེ། འགྲེལ་པ་ལས་གྲུབ་པའི་མཐའ་རྣམ་པ་བཞི་དང་། རྙོག་པ་ལྔར་སྦྱར་རོ། །

[Block 1084]
གྲུབ་པའི་མཐའ་བཞི་ནི་འཇིག་རྟེན་གྱི་གྲུབ་པའི་མཐའ་དང་། དབང་པོ་སོ་སོའི་གྲུབ་པའི་མཐའ་དང་། གཉེན་པོའི་གྲུབ་པའི་མཐའ་དང་། དོན་དམ་པའི་གྲུབ་པའི་མཐའོ། །

[Block 1085]
དེ་ལ་བསྐལ་པའི་རྙོག་པ་དང་སེམས་ཅན་གྱི་རྙོག་པའི་གཉེན་པོ་ནི་འཇིག་རྟེན་གྱི་གྲུབ་པའི་མཐའོ། །

[Block 1086]
ཚེའི་རྙོག་པའི་གཉེན་པོ་ནི་དབང་པོ་སོ་སོའི་གྲུབ་པའི་མཐའོ། །

[Block 1087]
ཉོན་མོངས་པའི་རྙོག་པ་དང་། ལྟ་བའི་རྙོག་པའི་གཉེན་པོ་ནི་གཉེན་པོའི་གྲུབ་པའི་མཐའོ། །

[Block 1088]
གྲུབ་པའི་མཐའ༌[^1092]གསུམ་གྱིས༌[^1093]རྙོག་པ་ལྔ་བཅོམ་ནས་དོན་དམ་པར་ཞུགས་ཏེ་ཡང་དག་པ་ཉིད་ནི་རིག་པའོ། །

[Block 1089 [HEADING]]
###### **གཟུགས་པ་དང་གཞིག་པ།** ^4-2-10-2-1-1-4-0

[Block 1090]
དེ་ལ་གཟུགས་པ་དང་གཞིག་པ་ནི་དྲིས་པ། ཅིའི་ཕྱིར་རྙོག་པ་ལྔ་ལས་མི་མང་མི་ཉུང་ཞེ་ན། ལན་བཏབ་པ། སེམས་ཅན་ལ་རྣམ་པ་གཉིས་ཏེ། སྡིག་པ་སྤྱོད་པ་ཁྱིམ་པ་སྐྱེ་བོ༌[^1094]དང་ལོག་པར་ལྟ་བ་སྟེ་རབ་ཏུ་བྱུང་བའི་མུ་སྟེགས་ཅན་ནོ། །
--- END BLOCKS ---
