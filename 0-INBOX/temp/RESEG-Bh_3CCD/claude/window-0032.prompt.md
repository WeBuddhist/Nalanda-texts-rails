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
རང་རིག༌[^782]པ་ཡིན་ན་བེམས་པོ་ཉིད་དུ་ཇི་ལྟར་འགྱུར་ཞེས་ཕན་ཚུན་འགལ་བའོ། །

[Block 1122]
མེ་དང་དུ་བ་བཞིན་དུ་བདག་དང་རྟགས་དག་གི་འབྲེལ་པ་ཡིན་ན་དེ་ཡང་ཆོས་ལ་སོགས་པའི་བྱ་བ་རྟོགས་པར་བྱེད་པ་འབྱུང་བས་རྟོགས་པར་བྱ་བ་རྒྱུར་འགྱུར་བ་བདག་འགོག་པར་ཐལ་བར་འགྱུར་ཏེ། འབྲས་བུ་འབྱུང་བས་རྒྱུ་རྣམས་ཉམས་པར་འགྱུར་བའི་ཕྱིར་བདག་མེད་བདག༌[^783]ཅེས་རིགས་པ་པ་དང་བྱེ་བྲག་སྨྲ་བ་རྣམས་ལ་ལན་ནོ། །

[Block 1123 [HEADING]]
###### **འཇིག་རྟེན་རྒྱང་པན་པ།** ^1-5-3-3-1-3-0

[Block 1124]
འཇིག་རྟེན་རྒྱང་པན་པས་ནི་མངོན་སུམ་ཁོ་ན་ཚད་མ་ཡིན་གྱི་རྗེས་སུ་དཔག་པ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1125 [VERSE]]
ལག་པ་རེག་པས་ལོང་བ་ཡིས།[^784] །
དཀའ་བའི་ལམ་དུ་རྒྱུག་པ་ན། །
རྗེས་སུ་དཔག་པ་གཙོར་གྱུར་ལ། །
ལྟུང་བ་དག་ནི་དཀོན་པ་མིན། །

[Block 1126 [VERSE]]
འབད་པས་དོན་ནི་རྗེས་དཔག་པ། །
མཁས་པ་མཇལ་བར༌[^785]སྤྲོ་རྣམས་ཀྱི། །
ཤིན་ཏུ་མཁས་པ༌[^786]གཞན་རྣམས་ཀྱིས། །
རྣམ་པ་གཞན་དུ་སྒྲུབ་པར་བྱེད། །

[Block 1127]
དེ་བས་ན་རྗེས་སུ་དཔག་པ་མེད་དོ། །

[Block 1128]
གང་མངོན་སུམ་གྱིས་ཉེ་བར་དམིགས་པ་དེ་ཡོད་དོ། །

[Block 1129]
[^787]ཇི་སྐད་དུ།

[Block 1130 [VERSE]]
ཇི་སྲིད་འཚོ་བར་བདེ་ཚོལ་ཞིང་། །
ཤི་ནས་འབྱུང་བ་ཁྱོད་ལ་མེད། །
ཐལ་བར་འགྱུར་བའི་འཆི་བ་ལ། །
སླར་ཡང་འབྱུང་བ་ག་ལས་འགྱུར། །

[Block 1131]
ཞེས་འབྱུང་ངོ་། །

[Block 1132]
དེ་བཞིན་དུ་འབྱུང་བ་ཆེན་པོ་བཞི་འགྱུར་བ་ལས་སྣ་ཚོགས་འདི་དག་སོ་སོར་སྣང་བ་ཡིན་གྱི་སེམས་པ༌[^788]ཞེས་བྱ་བ་གཞན་གང་ཡང་མེད་དེ། [^789]གང་གི་ལོངས་སྤྱོད་དང་ཐར་པ་བསྒྲུབ་པར་བྱ་བའི་ཕྱིར། རྗེས་སུ་དཔག་པ་ཚད་མ་ཉིད་ཡིན་ནོ།[^790] །

[Block 1133]
གལ་ཏེ་འབྱུང་བ་ཆེན་པོ་ཡོངས་སུ་གྱུར་པ་མཚུངས་པ་ཡིན་ན་ཡང་། གཡོ་བ་ཉིད་དང༌[^791]མི་གཡོ་བ་ཉིད་མི་རིགས་སོ་ཞེ༌[^792]ན། དེ་ལ་ཡང་སྨྲས་པ་ངེས་པ་ཅན་གྱི་འབྲུ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་ཆང་གིས་ཇི་ལྟར༌[^793]མྱོས་པའི་ནུས་པ་དེ་བཞིན་དུ་ཕ་དང་མ་ལས་སྐྱེས་པའི་ལུས་ཀྱི་གོང་བུའི་སེམས་ཀྱི་ནུས་པ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1134]
ཤིང་ལ་སོགས་པའི་དངོས་པོ་རྣམས་དེ་ལྟར་མ་སྐྱེས་པས་སེམས་པ་མེད་དོ། །

[Block 1135]
འབྱུང་བ་ཆེན་པོ་ཡོངས་སུ་གྱུར་པ་ནི་མཚུངས་པ་ཁོ་ནའོ། །

[Block 1136]
དེ་ཡང་མི་རིགས་ཏེ། འབྱུང་བ་ཆེན་པོ་ནི་བེམས་པོ་དང་སེམས་པ་ནི་བེམས་པོ་མ་ཡིན་པས་ཤེས་པ༌[^794]དེ་དག་ནི་ཕན་ཚུན་རྒྱུ་གཅིག་པ་ནི་མི་རིགས་སོ། །

[Block 1137]
རྒྱུ་མཚུངས་པ་ཡིན་པས་ཐམས་ཅད་སེམས་པ༌[^795]ཉིད་དུ་འགྱུར་བའམ་སེམས་པ༌[^796]མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1138]
རྒྱུ་མེད་ན་རྟག་ཏུ་ཡོད་པའམ་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1139]
ཇི་སྐད་དུ།

[Block 1140 [VERSE]]
རྒྱུ་མེད་གཞན་ལ་ལྟོས༌[^797]མེད་ཕྱིར། །
རྟག་ཏུ་ཡོད་པའམ་མེད་པར་འགྱུར། །
དངོས་པོ་ཡི་ནི་ལྟོས་པ་ལས། །
བརྒྱ་ལ་ཉིད་དུ་འབྱུང་བར་འགྱུར། །

[Block 1141 [VERSE]]
དོན་གཞན་རྒྱུ་མཚན་ཅན་ཉིད་ནི། །
ཆོས་དེ་གཞན་པ་ཉིད་དུ་འགྱུར། །
ཕྱི་ནས༌[^798]འབྱུང་བ་རྒྱུ་མེད་ཉིད། །
འབྲས་བུ་ངེས་པ་ཅན་མི་འགྱུར། །

[Block 1142]
ཞེས་གསུངས་པས་སོ། །

[Block 1143]
སེམས་པ༌[^799]དང་འབྱུང་བ་ཆེན་པོ་རྣམས་ནི་ཐ་དད་མེད་ཅིང་ཐ་དད་མེད༌[^800]པའི་རྒྱུ་ཅན་ནོ། །

[Block 1144]
གལ་ཏེ་འབྱུང་བ་ཆེན་པོ་ལས་ཐ་དད་པ་བདག་གིས་སེམས་པ༌[^801]ཁས་མ་བླངས་ཏེ། འོན་ཀྱང་དེའི་རང་བཞིན་དེ་རྣམས་ཡིན་ཞེས་ཟེར་བ་ན། འདི་ཡང་བདེན་པ་མ༌[^802]ཡིན་ཏེ། སེམས་དང༌[^803]འབྱུང་བ་ཆེན་པོ་དག་ནི་ཐ་དད་པའི་ཚད་མའི་ཡུལ་ཅན་ཡིན༌[^804]པའི་ཕྱིར་རོ། །

[Block 1145]
དཔེར་ན་དབང་པོའི་མངོན་སུམ་གྱིས༌[^805]འདི་ཉིད་དུ་སོ་སོར་སྣང་བ་ནི༌[^806]འབྱུང་བ་ཆེན་པོའོ། །

[Block 1146]
རང་རིག་པའི་མངོན་སུམ་གྱིས་བདག་ཉིད༌[^807]དུ་སོ་སོར་སྣང་བ་ནི་སེམས་པ་ཉིད་དོ། །

[Block 1147]
འདི་ཉིད་དང་བདག་ཉིད་དབང་པོ་དང་རང་རིག་པའི་མངོན་སུམ་གྱི་ཚད་མ་དག་དང་གཞལ་བྱ་རྣམས་ཕན་ཚུན་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 1148]
ཆོས་རྣམས་ཀྱི་འདི་ཉིད་ཁོ་ན་དབྱེ་བའམ་དབྱེ་བའི་རྒྱུ་སྟེ། གང་འགལ་བའི་ཆོས་དང་ལྡན་པའམ་རྒྱུའི་དབྱེ་བའོ། །

[Block 1149]
དེ་ལྟར་ན་བདེ་བར་གཤེགས་པ༌[^808]ཁྱེད་རྣམས་ལ་དངོས་པོ་གཅིག་ལ་ནི་ཚད་མ་ཐ་དད་པ་འཇུག་པར་མཐོང་ངོ་། །འདི་ལྟ་སྟེ། དངོས་པོ་ཉིད་དང་སྐད་ཅིག་མ་དག་བཞིན་ནོ། །

[Block 1150]
དཔེར་ན་མངོན་སུམ་ཡན་ལག་ཐམས་ཅད་དང་ལྡན་པ་མ་ཉམས་པའི་དངོས་པོ་ངེས་པར་བྱས་པའམ། སླར་ཡང་དེ་ཉིད་དུ་རྗེས་སུ་དཔག་པས་སྐད་ཅིག་མའི་ངོ་བོར་དཔག་པར༌[^809]བྱ་བ་དེ་བཞིན་དུ་འབྱུང་བ་དང་སེམས་པའི༌[^810]བདག་ཉིད་ཅན་དབྱེར་མེད་པའི་དངོས་པོ་ཅན༌[^811]ལ་ཡང་དབང་པོའི་མངོན་སུམ་དང་རང་རིག་པའི་མངོན་སུམ་འཇུག་པར་འགྱུར་ཞེ་ན། སྨྲས་པ་དབྱེར་མེད་པའི་དངོས་པོ་མངོན་སུམ་གྱིས་ཡོངས་སུ་གཅོད་པ་ཡིན་ཏེ། འོན་ཀྱང་ཡུལ་གང་དུ་གང་ལ་ཐེ་ཚོམ་ཡོད་པ་དེ་དག་ཏུ་འཇལ་བ་པོ་དེའི་འཁྲུལ་པ་ཙམ་ཡང་སྤང་བར་བྱ་བའི་ཕྱིར་རྗེས་སུ་དཔག་པ་འཇུག་པར་འགྱུར་ཏེ། དཔེར་ན་དངོས་པོ་རྟག་པར་སྨྲ་བའི༌[^812]སྐད་ཅིག་མ་ཡིན་པ་ཉིད་ཀྱིའོ། །

[Block 1151]
ཁྱེད་ཅག་ལ་ཡང་འཁྲུལ་པ་གང་ཡང་མི་དགོས་ཏེ། གང་བཟློག་པར་བྱ་བའི་ཕྱིར་ཚད་མ་གཞན་བཙལ་བར་བྱ་སྟེ། སེམས་པ༌[^813]ཉིད་འབྱུང་བ་ཆེན་པོའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1152]
དེའི་ཕྱིར་དབྱེར་མེད་པའི་དངོས་པོ་ལ་ཐ་དད་པའི་ཚད་མ་འཇུག་པར་མཐོང་བའི་ཕྱིར་སེམས་པ་ཐ་དད་པ་ཡོད་པ་ཁོ་ནའོ། །

[Block 1153]
ཆང་གིས་མྱོས་པ་བཞིན་ཞེས་དཔེ་ནི་དོན་དང་མི་ལྡན་པ་སྟེ། ལྷན་ཅིག་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 1154]
གང་གི་ཚེ་ཆང་གི་རྫས་མྱོང་བར་མི་བྱེད་པ་ན་དེའི་ཚེ་མྱོས་པའི་ནུས་པ་ག་ལ་ཡོད་དེ། །ཆང་གིས་མྱོས་པར་གྱུར་པ་ན་ཡང་ལུས་ཀྱི་ནང་དུ་ཐིམ་པས་མྱོང་བའི་ནུས་པ་གཅིག་ཏུ་སྣང་གི་ཆང་ནི་མ་ཡིན་ཞེས་ལྷན་ཅིག་དམིགས་པ་མེད་དོ། །

[Block 1155]
དེ་བཞིན་དུ་ཡང་འབྱུང་བ་དང་སེམས་པ་དག་ལ་མེད་དོ། །

[Block 1156]
དཔེར་ན་ལུས་མེད་པས་ཀྱང་ཕྲ་བའི་ལུས་དང་ལྡན་པའི་སེམས་པ༌[^814]ཡོད་པ་ཉིད་དོ། །

[Block 1157]
སེམས་དང་ལྡན་པ་ནི༌[^815]ལུས་ཐམས་ཅད་དུ་མཐོང་ངོ་། །གཟུགས་མེད་པའི་ཁམས་ལ་ཡང་ཏིང་ངེ་འཛིན་གྱི་ལུས་མེད་པར་མི་འབྱུང་བའོ། །

[Block 1158]
གཞི་དང་གཞི་ཅན་གྱི་འབྲེལ་པ་ནི་ལུས་དང་།

[Block 1159 [VERSE]]
སེམས་དག་ལ་འབྲེལ་པ་རིགས་པ་ཉིད་དོ། །
གཞི་འཇིག་པས་གཞི་ཅན་འཇིག་པར༌[^816]མ་མཐོང་སྟེ།
ཤིང་བཅད་པས་བྱ་རོག་བཅད་པ་མ་མཐོང་ངོ་། །

[Block 1160]
གལ་ཏེ་དེ་ལྟ་ཡིན་ན་གསོན་པ་དང་འཆི་བའི་ཐ་སྙད་ཇི་ལྟར་འགྱུར་ཞེ་ན། སྨྲས་པ། ཐོག་མ་མེད་པའི་དུས་ནས་སྲེད་པ་དང་མ་རིག་པའི་བག་ཆགས་ཀུན་འབྱུང་གི་བདེན་པའི་རྣམ་གྲངས་ཅན་གྱི་དབང་གིས་སྲོག་དང་དབང་པོའི་ཚོགས་གཡོ་བར་གྱུར་པས་ཚེ་གནས་པར་བྱེད་པའི་ལས་ཀྱི་དབང་གིས་ཕུང་པོ་ཟ་མ་ཏོག་གི་ནང་དུ་ཇི་སྲིད་རྣམ་པར་ཤེས་པ་གནས་པ་དེ་སྲིད་གསོན་པོ་ཡིན་ཞེས་ཐ་སྙད་འབྱུང་ངོ་། །ཚེ་གནས་པར་བྱེད་པའི་ལས་འགོག་པས་སྲོག་ལ་སོགས་པའི་འཁོར་ལོ་འཛད་པས༌[^817]འཆིའོ་ཞེས་འཇིག་རྟེན་དུ་གྲགས་སོ། །
--- END BLOCKS ---
