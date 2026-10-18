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

[Block 1126]
པ་ཡིན་ནོ། །

[Block 1127]
འདིའི་འགྲོ་བ་རབ་ཏུ་བསྔགས་པ༌[^827]ཡིན་པས་ན་བདེ་འགྲོ་སྟེ། ལྷ་དང་མིའི་ནང་དུ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1128]
འགྲོ་བ་དེ་དག་ཏུ་ཡང་རྒྱལ་རིགས་དང་བྲམ་ཟེ་དང་ཁྱིམ་བདག་གི་རིགས་ཤིང་སཱ་ལ་ཆེན་པོ་ལྟ་བུར་སྐྱེ་བ་ཡིན་གྱི་རིགས་དམའ་བར་ནི་མི་སྐྱེའོ། །

[Block 1129]
འདིའི་དབང་པོ་རྣམས་མ་ཚང་བས་ན་དབང་པོ་མ་ཚང་བའོ། །

[Block 1130]
དབང་པོ་ཚང་བས་ན་དབང་པོ་ཚང་བ་སྟེ། དབང་པོ་མ་ཚང་བ་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1131]
ཕོ་ཁོ་ནར་འགྱུར་གྱི་མོར་ཡང་མི་འགྱུར་ན་ཟ་མ་ལ་སོགས་པར་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། སྐྱེ་བ་ཐམས་ཅད་དུ་ཡང་ཚེ་རབས་དྲན་པར་འགྱུར་རོ། །

[Block 1132]
ནུར་བས་ན་ལྡོག་པའོ། །

[Block 1133]
ནུར་བ་མེད་པས་ན་མི་ལྡོག་པ་སྟེ། ལྡོག་པ་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་སྟེ། སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པའི་དོན་དུ་སྡུག་བསྔལ་གྱི་རྣམ་པ་ཐམས་ཅད་དང་། ལོག་པར་སྒྲུབ་པ་ཐམས་ཅད་ཀྱིས་སྐྱོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1134]
འཇིག་རྟེན་ན༌[^828]ཟོང་གིས་མ་ཉོས་པའི་བྲན་ཞེས་བརྗོད་པ་གང་ཡིན་པ་དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་ཡིན་ཏེ། བདག་ཉིད་ཆེན་པོ་དེ་དག་ནི། །འབྱོར་པའི་མཆོག་ཁྱད་པར་ཅན་ཐམས་ཅད་བརྙས༌[^829]ཀྱང་ཐུགས་རྗེའི་གཞན་གྱི་དབང་དུ་གྱུར་པའི་ཕྱིར་བདག་ཉིད་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དྲུང་དུ་ཁྱི་དང་འདྲ་བར་ང་རྒྱལ་མེད་པར་གནས་ཏེ། སེམས་ཅན་ཐམས་ཅད་ཀྱིས་བརྙས་གནོད་བྱས་པ་ཐམས་ཅད་བཟོད་ཅིང་ངལ་བ་དང་མནགས་པ་ཐམས་ཅད་ཀྱང་ཉམས་སུ་ལེན་པ་ཡིན་ནོ། །

[Block 1135 [HEADING]]
### མཚན་རྣམ་པར་སྨིན་པ་ཅན་གྱི་ལས། ^1-68-0

[Block 1136]
མཚན་རྣམ་པར་སྨིན་པ་ཅན་གྱི་ལས་སུ་བཤད་པ་གང་ཡིན་པ།

[Block 1137 [VERSE]]
དེ་ནི་འཛམ་གླིང༌[^830]ཕོར་གྱུར་ཉིད། །
མངོན་སུམ་སངས་རྒྱས་ལ་སེམས་པ། །
བསམས་པ་ལས་བྱུང་བསྐལ་པ་བརྒྱ། །
ལུས་པ་དག་ཏུ་འཕེན་པར་བྱེད། །

[Block 1138]
བྱང་ཆུབ་སེམས་དཔའ་ནི་འཛམ་བུ་གླིང་ཁོ་ནར་མཚན་རྣམ་པར་སྨིན་པ་ཅན་གྱི་ལས་འཕེན་པར་བྱེད་ཀྱི་གཞན་དུ་ནི་མ་ཡིན་ཏེ། འཛམ་བུའི་གླིང་པ་རྣམས་བློ་རྣོ་བའི་ཕྱིར་རོ། །

[Block 1139]
ཕོ་ཁོ་ནས་འཕེན་གྱི་མོས་ནི་མ་ཡིན་ནོ། །

[Block 1140]
སྟོན་པ་མངོན་སུམ་དུ་གྱུར་པ་དང་། སངས་རྒྱས་ལ་དམིགས་པའི་སེམས་པ༌[^831]ཁོ་ནས་བསྐལ་པ་བརྒྱ་ལུས་པའི་ཚེ་འཕེན་གྱི་མང་པོ་ལུས་པའི་ཚེ་ནི་མ་ཡིན་ནོ། །

[Block 1141]
ལས་དེ་ཡང་བསམས་པ་ལས་བྱུང་བ་ཡིན་གྱི་ཐོས་པ་ལས་བྱུང་བ་ཡང་མ་ཡིན་ལ་བསྒོམས་པ་ལས་བྱུང་བ་ཡང་མ་ཡིན་ནོ། །

[Block 1142]
བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པས་ནི་བརྩོན་འགྲུས་སྤྱད་པས༌[^832]བསྐལ་པ་དགུ་བསྡུམས་ཏེ། བསྐལ་པ་དགུ་བཅུ་རྩ་གཅིག་ལུས་པའི་ཚེ་འཕངས་སོ། །

[Block 1143]
དེ་ཉིད་ཀྱི་ཕྱིར་གྲོང་དཔོན་ངས་འདི་ནས་བཟུང་སྟེ། བསྐལ་པ་དགུ་བཅུ་རྩ་གཅིག་གི་བར་དུ་ཡང་དག་པར་རྗེས་སུ་དྲན་ཏེ། ཟས་སྨིན་པ་སྟེར་བར་བྱ་བའི་ཕྱིར་ཁྱིམ་འགའ་ལ་ཡང་མི་བདེ་བ་འམ། གནོད་པར་གྱུར་པ༌[^833]གང་ཡིན་པ་དེ་ནི་མངོན་པར་མི་མཁྱེན་ཏོ་ཞེས་གསུངས་ཏེ། དེ་ཚུན་ཆད་རང་བཞིན་གྱིས་ཚེ་རབས་དྲན་པའི་ཕྱིར་རོ། །

[Block 1144]
སྔོན་གྱི་སློབ་དཔོན་རྣམས་ན་རེ་བསྐལ་པ་དང་པོ་ཚར་ཕྱིན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཁོ་ནས་སྐྱོན་བཞི་པོ་འདི་དག་ནི་བཟློག་པར་བྱེད་པ།[^834] ཡོན་ཏན་གཉིས་པོ༌[^835]ནི་འཐོབ་བོ་ཞེས་ཟེར་རོ། །

[Block 1145]
མཚན་དེ་དག་ཀྱང་རེ་རེའང་བསོད་ནམས་བརྒྱ་ལས་སྐྱེས། བསོད་ནམས་ཀྱི་ནི༌[^836]ཚད་ཇི་ཙམ་ཞེ་ན། [^837]ཁ་ཅིག་ན་རེ་བྱང་ཆུབ་སེམས་དཔའ་ཉེ་བ་མ་གཏོགས་པ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ལོངས་སྤྱོད་ཀྱི་འབྲས་བུ་ཅན་ཇི་སྙེད་པ་དེ་ཙམ་མོ་ཞེས་ཟེར་རོ། །

[Block 1146]
གཞན་དག་ན་རེ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ལས་ཀྱི་དབང་གིས་སྟོང་གསུམ་འཆགས་པ་ཇི་སྙེད་ཙམ་མོ་ཞེས་ཟེར་རོ། །

[Block 1147]
གཞན་དག་ན་རེ་དེའི་ཚད་ནི་སངས་རྒྱས་ཁོ་ནས་མཁྱེན་པར་ཟད་དོ་ཞེས་ཟེར་རོ། །

[Block 1148 [HEADING]]
### སངས་རྒྱས་ཇི་སྙེད་ཅིག་ལ་བསྙེན་བཀུར་བྱས་པ། ^1-69-0

[Block 1149]
ཡང་བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔར༌[^838]གྱུར་པ་ན་སངས་རྒྱས་ཇི་སྙེད་ཅིག་ལ་བསྙེན་བཀུར་བྱས་ཤེ་ན། བསྐལ་པ་གྲངས་མེད་པ་དང་པོ་ལ་ནི་སངས་རྒྱས་བདུན་ཁྲི་ལྔ་སྟོང་ལ་བསྙེན་བཀུར་བྱས་སོ། །

[Block 1150]
གཉིས་པ་ལ་ནི་བདུན་ཁྲི་དྲུག་སྟོང་ལ་བསྙེན་བཀུར་བྱས་སོ། །

[Block 1151]
གསུམ་པ་ལ་ནི་བདུན་ཁྲི་བདུན་སྟོང་ལ་བསྙེན་བཀུར་བྱས་སོ། །

[Block 1152]
བསྐལ་པ་གྲངས་མེད་པ་གང་གི༌[^839]ཐ་མར་སངས་རྒྱས་གང་ཞིག་བྱུང་བར་གྱུར་ཞེ༌[^840]ན། བཟློག་པའི་གོ་རིམས་ཀྱིས༌[^841]གོ་རིམས་བཞིན་དུ།

[Block 1153 [VERSE]]
རྣམ་གཟིགས་མར་མེ་རིན་ཆེན་གཙུག །
གྲངས་མེད་གསུམ་གྱི་ཐ་མར་བྱུང་། །

[Block 1154]
ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་རིན་ཆེན་གཙུག་ཏོར་ཅན་གྱི་ཚེ་ནི་བསྐལ་པ་གྲངས་མེད་པ་དང་པོ་རྫོགས་སོ། །

[Block 1155]
བཅོམ་ལྡན་འདས་མར་མེ་མཛད་ཀྱི་ཚེ་ནི་གཉིས་པ་རྫོགས་སོ། །

[Block 1156]
དེ་བཞིན་གཤེགས་པ་རྣམ་པར་གཟིགས་ཀྱི་ཚེ་ནི་གསུམ་པ་རྫོགས་སོ། །

[Block 1157]
དེ་དག༌[^842]ཐམས་ཅད་ཀྱི་དང་པོ་ཤཱཀྱ་ཐུབ་པ་ཡིན། སྔོན་ཤཱཀྱ་ཐུབ་པ་ཞེས་བྱ་བ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་གང་ལ་བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔར་གྱུར་པའི་ཚེ་བདག་ཀྱང་འདི་འདྲ་བའི་རྣམ་པ་ཁོ་ནར་སངས་རྒྱས་པར་ཤོག་ཤིག༌[^843]ཅེས་དང་པོར་སྨོན་ལམ་བཏབ་པ་བྱུང་སྟེ། དེ་ཡང་འདི་བཞིན་དུ་རྩོད་པའི་དུས་ཁོ་ན་ལ་བྱུང་ལ། དེའི་བསྟན་པ་ཡང་ལོ་སྟོང་གི་མཐའི་བར་དུ་གནས་པར་གྱུར་ཏོ། །

[Block 1158 [HEADING]]
### ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པ། ^1-70-0

[Block 1159]
ཡང་བྱང་ཆུབ་སེམས་དཔའ་གནས་སྐབས་གང་དག་ཏུ༌[^844]ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་ཡོངས་སུ་རྫོགས་པར་བྱེད་ཅེ་ན།

[Block 1160 [VERSE]]
ཀུན་ལ་ཐམས་ཅད་སྙིང་རྗེ་ཡིས། །
སྦྱིན་པར་བྱེད་པས་སྦྱིན་པ་རྫོགས། །
--- END BLOCKS ---
