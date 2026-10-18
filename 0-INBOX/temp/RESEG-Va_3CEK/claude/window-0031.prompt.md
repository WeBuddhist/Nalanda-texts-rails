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
[Block 1086]
གལ་ཏེ་མ་ལ་སྦྱོར་བ་བྱས་ནས་གཞན་བསད་ན་ཡང་མཚམས་མེད་པར་མི་འགྱུར་ལ་མ་མ་ཡིན་པ་ལ་སྦྱོར་བ་བྱས་ནས་མ་བསད་ན་ཡང་མཚམས་མེད་པར༌[^784]འགྱུར་ཏེ། མ་ཁྲིའུའི་འོག་ན་འདུག་པ་བསད་པ་དང་། ཁྲུས་པའི་བུས་སྦྲང་བུ་ལ་སྦྱོར་བ་བྱས་པས་ཕ་བསད་པ་དཔེར་བྱའོ། །

[Block 1087]
མཚོན་ཐབས་གཅིག་གིས་མ་དང་གཞན་ཞིག་ཀྱང༌[^785]བསད་ན་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་གཉིས་ཡིན་ལ། རྣམ་པར་རིག་བྱེད་ནི་མཚམས་མེད་པ་ཁོ་ན་ཡིན་ཏེ། ལས་དེ་སྟོབས་ཆེ་བའི་ཕྱིར་རོ། །

[Block 1088]
བཙུན་པ་དབྱངས་སྒྲོགས་ན་རེ་རྡུལ་ཕྲ་རབ་བསགས་པ་ཡིན་པའི་ཕྱིར་རྣམ་པར་རིག་བྱེད་ཀྱང་རྣམ་པ་གཉིས་སོ་ཞེས་ཟེར་རོ། །

[Block 1089]
དགྲ་བཅོམ་པ་མ་ཡིན་པའི་འདུ་ཤེས་ཀྱིས་དགྲ་བཅོམ་པ་བསད་ན་ཡང་མཚམས་མེད་པར་འགྱུར་ཏེ། འདི་གསད༌[^786]དོ་སྙམ་དུ་རྟེན་ངེས་པར་བཟུང་བའི་ཕྱིར་རོ། །

[Block 1090]
གང་ཞིག་གིས་ཕ་དགྲ་བཅོམ་པ་བསད་ན་ཡང་དེ་ལ་མཚམས་མེད་པ་ནི་གཅིག་ཁོ་ནར་འགྱུར་ཏེ། རྟེན་གཅིག་པའི་ཕྱིར་རོ། །

[Block 1091]
སོང་ལ་སྐྲ་ཅན་ལ་ཁྱོད་ཀྱིས་ནི་མཚམས་མེད་པ་གཉིས་བྱས་ཏེ། ཕ་གསད་པ༌[^787]གང་ཡིན་པ་དང་། གང་ཡང་དགྲ་བཅོམ་པ་གསད་པའོ༌[^788]ཞེས་སྨྲོས་ཤིག་ཅེས་བྱ་བའི་རྟོགས་པ་བརྗོད་པ༌[^789]འདི་ཇི་ལྟ་བུ་ཞེ་ན། རྒྱུ་གཉིས་ཀྱིས་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1092]
ཡང་ན་སྒོ་གཉིས༌[^790]ནས་སྤྱོས་པ་ཡིན་ནོ། །

[Block 1093]
དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བས་གདོན་མི་ཟ་བར་མཚམས་མེད་པར་འགྱུར་རམ་ཞེ་ན། བགྲོད༌[^791]པར་སེམས་པ་ལ་ནི་འགྱུར་གྱི། སངས་རྒྱས་བརྡེག་པར་སེམས་པ་ལའང༌[^792]མིན། །གལ་ཏེ་དགྲ་མ་ཆོམས་པའི་ཚེ་བསྣུན༌[^793]ལ་བསྣུན༌[^794]པའི་འོག་ཏུ་དགྲ་བཅོམ་པར་གྱུར་ན། བསྣུན༌[^795]འོག་དགྲ་བཅོམ་པ་ལ་མིན། །མཚམས་མེད་པར་འགྱུར་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དེས་ནི་དེ་ལ་སྦྱོར་བ་མ༌[^796]བྱས་སོ། །

[Block 1094]
ཅི་མཚམས་མེད་པའི་སྦྱོར་བ་བྱས་ཏེ། དེ་ཡང་མ༌[^797]བཟློག་པར་འདོད་ཆགས་དང་བྲལ་བའི་འབྲས་བུ་འཐོབ་པར་འགྱུར༌[^798]ཞེ་ན།

[Block 1095 [VERSE]]
མཚམས་མེད་སྦྱོར་བ་བྱས་པ་ལ། །
འདོད་ཆགས་བྲལ༌[^799]འབྲས་མི་སྲིད་དོ། །

[Block 1096]
ཅིའི་ཕྱིར་ཞེ་ན། བསམ་པ་ཤིན་ཏུ་འགལ་བའི་ཕྱིར་རོ། །

[Block 1097]
ལས་ཀྱི་ལམ་གཞན་གྱི་སྦྱོར་བ་བྱས་ནས་འཕགས་པའི་ལམ་སྐྱེས་པ་ལ་ནི་ཡང་ལས་ཀྱི་ལམ་མི་སྐྱེ་སྟེ། རྟེན་དེ་དང་ཤིན་ཏུ་འགལ་བའི་ཕྱིར་རོ། །

[Block 1098 [HEADING]]
### ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་ཆེན་པོ། ^1-63-0

[Block 1099]
མཚམས་མེད་པའི་ལས་འདི་དག་ལས་ཐམས་ཅད་ཀྱི་ནང་ན་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་ཆེན་པོ་གང་ཡིན་ཞེ་ན།

[Block 1100 [VERSE]]
དགེ་འདུན་དབྱེ༌[^800]ཕྱིར་བརྫུན་སྨྲ་བ། །
ཁ་ན་མ་ཐོ་རབ་ཆེར༌[^801]འདོད། །

[Block 1101]
གང་ཞིག་ཆོས་དང་ཆོས་མ་ཡིན་པ་ཤེས་བཞིན་དུ་དགེ་འདུན་དབྱེ་བའི་ཕྱིར་བརྫུན་དུ་སྨྲ་ན་ལོག་པར་སྟོན་པའི་ཕྱིར་ཉེས་པར་སྤྱོད་པ་ཐམས་ཅད་ཀྱི་ནང་ན་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་རབ་ཏུ་ཆེ་བ་ཡིན་ནོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་ཆོས་ཀྱི་སྐུ་ལ་བསྣུན༌[^802]པའི་ཕྱིར་དང་། འཇིག་རྟེན་རྣམས་ཀྱི་མཐོ་རིས་དང་བྱང་གྲོལ་གྱི་ལམ་གྱི༌[^803]བར་དུ་གཅོད་པར་བྱེད་པའི་ཕྱིར་ཏེ། དགེ་འདུན་དབྱེ༌[^804]ན་ཇི་སྲིད་དུ་སླར་མ་དུམ༌[^805]གྱི་བར་དུ་འཇིག་རྟེན་ངེས་པ་ལ་འཇུག་པ་དང་། འབྲས་བུ་འཐོབ་པ་དང་། འདོད་ཆགས་དང་བྲལ་བ་དང་། ཟག་པ་ཟད་པར་བྱ་བ་རྣམས་ལ་བགེགས༌[^806]སུ་གྱུར་པ་ཡིན་ཞིང་། བསམ་གཏན་དང་ཀློག་པ་དང་ཁ་ཏོན་དང་སེམས་པའི་ལས་རྣམས་ཀྱང་མི་འཇུག་ཅིང་། ལྷ་དང་ཀླུ་དང་མིར་བཅས་པའི་འགྲོ་བ་ཡང་འཁྲུགས་པ་དང་། ཡིད་མི་བདེ་བ་དང་། རང་དབང་མེད་པ་དང་། དྲན་པ་ཉམས་པར་འགྱུར་ལ། འདི་ལྟར་འདིའི་རྣམ་པར་སྨིན་པ་ཡང་བསྐལ་པ་གཅིག་ཏུ་མནར་མེད་པར་སྐྱེ་བ་ཡིན་ནོ། །

[Block 1102]
མཚམས་མེད་པ་ལྷག་མ་རྣམས་ལས་ནི་གོ་རིམས་བཞིན་དུ་ལྔ་པ་དང་གསུམ་པ་དང་དང༌[^807]པོ་རྣམས་ཆེས་ལྕི་བ་ཡིན་ཏེ། ཕ་གསོད་པ་ནི་ཐམས་ཅད་ཀྱི་ནང་ན་ཡང་བ་ཡིན་ནོ། །

[Block 1103]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་ཉེས་པ་གསུམ་གྱི་ནང་ན་ཡིད་ཀྱི་ཉེས་པ་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་ཆེན་པོར་གསུངས་པ་དང་། ཡང་ལོག་པར་ལྟ་བ་ནི་ཁ་ན་མ་ཐོ་བ་དམ་པ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། མཚམས་མེད་པ་རྣམས་ངེས་པར་མཛད་ནས་ནི་དགེ་འདུན་གྱི་དབྱེན་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་ཆེན་པོར་གསུངས་ལ།

[Block 1104]
ལས་གསུམ་ངེས་པར་མཛད་ནས་ནི་ཡིད་ཀྱི་ཉེས་པ་གསུངས།

[Block 1105]
ལྟ་བ་རྣམས་ངེས་པར་མཛད་ནས་ནི་ལོག་པར་ལྟ་བ་གསུངས་པའམ། ཡང་ན་རྣམ་པར་སྨིན་པ་རྒྱ་ཆེ་བ་དང་། སྐྱེ་བོ་ཕལ་པོ་ཆེ་འཆི་བ་དང་། དགེ་བའི་རྩ་བ་ཀུན་དུ་གཅོད་པའི་དབང་དུ་མཛད་ནས་གོ་རིམས་བཞིན་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 1106 [HEADING]]
### ལེགས་པར་སྤྱད་པ་རྣམས་ལས་འབྲས་བུ་རབ་ཏུ་ཆེ་བ། ^1-64-0

[Block 1107]
ལེགས་པར་སྤྱད་པ་རྣམས་ལས་འབྲས་བུ་རབ་ཏུ་ཆེ་བ་གང་ཡིན་ཞེ་ན། འཇིག་རྟེན་པའི༌[^808]དགེ་བ་ལ། སྲིད་རྩེའི་སེམས་པ༌[^809]འབྲས་རབ༌[^810]ཆེ། །ལས་དགེ་བ་ལ་ནི་ཐམས་ཅད་ཀྱི་ནང་ན་སྲིད་པའི་རྩེ་མོའི་སེམས་པ་འབྲས་བུ་རབ་ཏུ་ཆེ་བ་ཡིན་ཏེ། དེའི་རྣམ་པར་སྨིན་པ་ནི་བསྐལ་པ་བརྒྱད་ཁྲིར་རབ་ཏུ་ཞི་བ་ཡིན་ནོ། །

[Block 1108]
རྣམ་པར་སྨིན་པའི་འབྲས་བུའི་དབང་དུ་བྱས་ནས་དེ་སྐད༌[^811]བཤད་ཀྱི། བྲལ་བའི་འབྲས་བུའི་དབང་དུ་བྱས་ནས་ནི་ཐམས་ཅད་ཀྱི་ནང་ན་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་སེམས་པ༌[^812]འབྲས་བུ་ཆེ་བ་ཡིན་ཏེ། ཀུན་དུ་སྦྱོར་བ་ཐམས་ཅད་གཏན་དུ་གཏུགས་པ་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1109]
དེ་ཉིད་ཀྱི་ཕྱིར་འཇིག་རྟེན་པའི་ཞེས་བཤད་དོ། །

[Block 1110 [HEADING]]
### མཚམས་མེད་པ་དང་ཆ་འདྲ་བ། ^1-65-0

[Block 1111]
ཅི་མཚམས་མེད་པ་རྣམས་ཁོ་ནས་དམྱལ་བ་དག་ཏུ་གདོན་མི་ཟ་བར་སྐྱེ་བར་འགྱུར་རམ། འོན་ཏེ་གཞན་དག་གིས་ཀྱང་སྐྱེ་བར་འགྱུར་ཞེ་ན། མཚམས༌[^813]མེད་པ་དང་ཆ༌[^814]འདྲ་བ་རྣམས་ཀྱིས་ཀྱང་གདོན་མི་ཟ་བར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1112]
གཞན་དག་ན་རེ་བར་ཆད་མེད་པ༌[^815]ཁོ་ནར་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1113]
དེ་དག་ཀྱང་གང་ཞེ་ན། སྨྲས་པ།

[Block 1114 [VERSE]]
མ་དགྲ་བཅོམ་མ་སུན་བྱས་དང་། །
བྱང་ཆུབ་སེམས་དཔའ་དེས་གནས་དང་། །
སློབ་པ་གསོད་དང་དགེ་འདུན་གྱི། །
འདུ་བའི་སྒོ་ནི་འཕྲོགས་པ༌[^816]དག །

[Block 1115 [VERSE]]
མཚམས་མེད་པ་དང་ཆ་འདྲ་སྟེ། །
ལྔ་པ་མཆོད་རྟེན་འཇིག་པ་ཡིན། །

[Block 1116]
ལྔ་པོ་འདི་དག་ནི་གོ་རིམས་བཞིན་དུ་མཚམས་མེད་པ་ལྔ་དང་ཆ་འདྲ་བ་ཡིན་ཏེ། གལ་ཏེ་མི་ཚངས་པར་སྤྱོད་པས་མ་དགྲ་བཅོམ་མ་སུན༌[^817]པར་བྱེད་པ་དང་། ངེས་པར་རྟོགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་གསོད་པ་དང་། སློབ་པ་གསོད་པ་དང་། དགེ་འདུན་གྱི་ཞལ་དུ་འདུ་བའི་སྒོ་འཕྲོགས་པ༌[^818]དང་། མཆོད་རྟེན་འཇིག་པར་བྱེད་པའོ། །

[Block 1117 [HEADING]]
### དུས་གསུམ་པོ་དག་ཏུ་ཤིན་ཏུ་བགེགས་བྱེད་པ། ^1-66-0

[Block 1118]
རྣམ་པར་སྨིན་པ་དང་བཅས་པའི་ལས་གཞན་ཡང་དུས་གསུམ་པོ་དག་ཏུ་ཤིན་ཏུ་བགེགས་བྱེད༌[^819]དེ། གསུམ་པོ་གང་དག་ཏུ་ཞེ་ན།

[Block 1119 [VERSE]]
བཟོད་དང་ཕྱིར་མི་འོང་དགྲ་བཅོམ། །
འཐོབ་པ་ལས་བགེགས༌[^820]ཤིན་ཏུ་བྱེད། །

[Block 1120]
རྩེ་མོ་ལས་བཟོད་པ་ཐོབ་པ་ལ་ནི་དེའི་རྣམ་པར་སྨིན་པའི་ས་ལས་འདའ་བའི་ཕྱིར་ངན་སོང་བའི་ལས་རྣམས་བགེགས༌[^821]བྱ་བའི་ཕྱིར་ཉེ་བར་གནས་ཏེ། དཔེར་ན་མི་ཞིག་ཡུལ་འདོར་བར་བྱེད་པ་ལ་བུ་ལོན་པ་དག་ལྡང་བ་བཞིན་ནོ། །

[Block 1121]
དེ་བཞིན་དུ་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་འཐོབ་པ་ལ་ནི། འདོད་པ་ན་སྤྱོད་པའི་ལས་རྣམས་བགེགས༌[^822]བྱ་བའི་ཕྱིར་ཉེ་བར་གནས་ཏེ། མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ནི་མ་གཏོགས་སོ། །

[Block 1122]
དེ་བཞིན་དུ་དགྲ་བཅོམ་པ་ཉིད་ཐོབ་པ༌[^823]ལ་ནི་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ལས་རྣམས་བགེགས༌[^824]བྱ་བའི་ཕྱིར་ཉེ་བར་གནས་སོ། །

[Block 1123 [HEADING]]
### གང་ནས་བྱང་ཆུབ་སེམས་དཔའ་ཡིན་པ། ^1-67-0

[Block 1124]
བྱང་ཆུབ་སེམས་དཔའ་གསད་པ་ཞེས་བཤད་པ་གང་ཡིན་པ། གང་ནས་བྱང་ཆུབ་སེམས་དཔའ་ཡིན། །གང་ན་གཟུང༌[^825]སྟེ་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བརྗོད་པར་བྱ། གང་ནས་མཚན་གྱི་ལས་བྱེད་པ་གང་ཕན་ཆད་ནས་མཚན་རྣམ་པར་སྨིན་པར་འགྱུར་བའི་ལས་རྣམས་བྱེད་པར་རྩོམ་པ་དེའི་ཚེ་ངེས་པར་རྟོགས་པ་ཡིན་ནོ། །ཇི་ལྟ་ཞེ་ན། དེ་ནི་དུས་དེ་ཕན་ཆད་རྟག་ཏུ་ཡང་།[^826] །

[Block 1125 [VERSE]]
བདེ་འགྲོར་རིགས་མཐོར་སྐྱེ་དབང་ཚང་། །
ཕོར་འགྱུར་ཚེ་རབས་དྲན་མི་ལྡོག །
--- END BLOCKS ---
