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
[Block 1156 [VERSE]]
དོན་གཅིག་ཡིན་ནའང་མ་རྨོངས་དང་། །
ཐབས་མང་དཀའ་བ༌[^641]མེད་ཕྱིར་དང་། །
དབང་པོ་རྣོན་པོའི་དབང་བྱས་པས། །
སྔགས་ཀྱི་བསྟན་བཅོས་ཁྱད་པར་འཕགས། །

[Block 1157]
ཞེས༌[^642]ཤེས་རབ་ཀྱི༌[^643]ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཐེག་པ་བས་གསང་སྔགས་ཀྱི་ཐེག་པ་ཁྱད་པར༌[^644]དུ་འཕགས་སོ་ཞེས་བྱ་བ་ནི་གཞུང་ལུགས་སོ། །

[Block 1158]
འདི་ལྟར་དོན་དམ་པའི་བྱང་ཆུབ་ཀྱི་སེམས་དངོས་ཕྱིན་ཅི་མ་ལོག་པ་དེ་ནི་གསང་སྔགས་ཀྱི་སྒོའི་སྤྱད་པ་སྤྱོད་པའི་བྱང་ཆུབ་སེམས་དཔས་བསྐྱེད་པར་བྱའོ། །

[Block 1159]
འོན་ཀྱང་འདིར་ནི་དེ་ལྟ་བུའི་གཞུང་གི་དོན་ནི་བདག་གིས༌[^645]མ་བརྗོད་དོ། །

[Block 1160]
འདིར་ནི་བསྐྱེད་པའི་རིམ་པ་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའི་ཚོགས་གཉིས་བསགས་པའི་ཐབས་ཅུང་ཞིག་རྩ་བར་ཡང་བཀོད་ཅིང་འདིར་ཡང་རྩ་བ་ལ་བརྟེན་པ་ཙམ་ཞིག་བྲི་བར༌[^646]བྱའོ། །

[Block 1161]
དེ་ལྟ་བུའི་གསང་སྔགས་ཀྱི་ལུགས་ཀྱིས་ཐུན་མོང༌[^647]མ་ཡིན་པའི་ཚོགས་གཉིས་མྱུར་དུ་རྫོགས་པར་བྱའོ་སྙམ་དུ་བསམས་ནས། སྔགས་མཐུ་ཉིད་ལས་བྱུང་བ་ཡི། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨྲས་ཏེ། སྔགས་མཐུ་ཞེས་པ་ནི་སྤྱིར་གཟུངས་ཀྱི་ཆོ་ག་ཐམས་ཅད་ཀྱང་བྱ་བའི་རྒྱུད་ཡིན་པས་གཟུངས་ལ་སོགས་པའི་སྔགས་རྒྱུད་ཐམས་ཅད་ནས་འབྱུང་བའི་སྔགས་ཀྱི་བཟླས་བརྗོད་ཀྱི་ནུས་པས་དངོས་གྲུབ་འབྱུང་སྟེ། དེ་གང་ཞེ་ན། ཞི་དང་རྒྱས་ལ་སོགས་པ་ཡི། །ཞེས་པ་དབང་དང་མངོན་སྤྱོད་ཀྱི་ཆོ་ག་རྣམ་པ་བརྒྱད་དོ། །

[Block 1162]
བུམ་པ་བཟང་གྲུབ་ལ་སོགས་པ། །གྲུབ་ཆེན་བརྒྱད་ཅེས་པ་ནི་འདི་ལྟར་བུམ་པ་བཟང་པོ་དང་། རྐང་མགྱོགས་དང་། རལ་གྲི་དང་། མངག་གཞུག་པ་དང་། ས་འོག་དང་། མི་སྣང་བ་དང་། དཔག་བསམ་གྱི་ཤིང་དང་། རྒྱལ་སྲིད་རྣམས་སོ། །

[Block 1163]
སོགས་པ༌[^648]ཞེས་པ་ནི་མིག་སྨན་དང་། རི་ལུ་དང་། ནམ་མཁའ་ལ་འཕུར་བ་དང་། འབྲུའི་ཆར་འབེབས་པ༌[^649]དང་། ཡུངས་ཀར་བསྒྲུབས༌[^650]ནས་གཟུགས་སྣ་ཚོགས་བྱེད་པ་དང་། པྲ་ཕབ་ནས་མངོན་པར་ཤེས་པ་བསྐྱེད་པ་དང་། རྫུ་འཕྲུལ་ལ་སོགས་པ་བརྒྱུད༌[^651]ནས་རྗེས་སུ་གཟུང་བ་དང་ཚར་གཅད་པའི་ལས་ཀྱི་དངོས་གྲུབ་ཇི་སྙེད་ཅིག་འབྱུང་བ་དེ་དག་ནི་བཟླས༌[^652]བརྗོད་དང་ཏིང་ངེ་འཛིན་གྱིས་ཞི་བ་དང་རྒྱས་པ་དང་། དབང་དང་མངོན་སྤྱོད་དང་། འཇིག་རྟེན་གྱི་དངོས་གྲུབ་ཆེན་པོ་བརྒྱད་ལ་སོགས་པ་དག་བསྒྲུབས་ནས་འབད་པ་མེད་པར་མྱུར་དུ་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་གཉིས་རྫོགས་པར་བྱེད་དོ། །

[Block 1164]
དེ་ལྟ་བུའི་དངོས་གྲུབ་འབད་པ་མེད་པར་མྱུར་དུ་འབྱུང་བའི་གསང་སྔགས་ཀྱི་ཐེག་པ་ཞེས་པ་དེ་གང་ཡིན་ཞེ་ན། བྱ་བ་སྤྱོད་སོགས་རྒྱུད་ཅེས་བྱ་བ་དང་། བྱ་བའི་རྒྱུད་དང་། སྤྱོད་པའི་རྒྱུད་དང་། རྟོག་པའི་རྒྱུད་དང་། གཉི་གའི་རྒྱུད་དང་། རྣལ་འབྱོར་གྱི་རྒྱུད་དང་། རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་དང་། རྣལ་འབྱོར་བླ་ན་མེད་པའི་རྒྱུད་རྣམས་སོ། །

[Block 1165]
དེ་ཡང་རྒྱུད་དེ་དག་ནི་རེ་རེ་ཞིང་ཡང་དཔག་ཏུ་མེད་དེ། [^653]དེ་ཡང་དཔལ་ཡེ་ཤེས་རྡོ་རྗེ་ཀུན་ལས་བཏུས་པའི་རྒྱུད་ཆེན་པོ་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ་རྒྱུད་སོ་སོའི་གྲངས་གསུངས་ཏེ། བྱ་བའི་རྒྱུད་སྟོང་ཕྲག་བཞིའོ། །

[Block 1166]
སྤྱོད་པའི་རྒྱུད་སྟོང་ཕྲག་བརྒྱད་དོ། །

[Block 1167]
རྟོག་པའི་རྒྱུད་སྟོང་ཕྲག་བཞིའོ། །

[Block 1168]
གཉིས་ཀའི་རྒྱུད་སྟོང་ཕྲག་དྲུག་གོ། །

[Block 1169]
རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་སྟོང་ཕྲག་བཅུ་གཉིས་ཏེ། དེ་དག་རྒྱས་པར་བྱས་ན་གྲངས་མེད་དོ་ཞེས་གསུངས་སོ། །

[Block 1170]
དེ་ལ་བྱ་བའི་རྒྱུད་ནི་གཟུངས་ཐམས་ཅད་དང་། རིག་པ་མཆོག་དང་། གར་མཁན་མཆོག་དང་། རབ་ཏུ་གྲུབ་པར་བྱེད་པ་དང་། དཔུང་བཟངས་དང་། འཇམ་དཔལ་གྱི་རྩ་བའི་རྒྱུད་ཆེན་པོ་དང་། འཇམ་དཔལ་གསང་བའི་རྒྱུད་དང་། རྡོ་རྗེ་གཙུག་ཏོར་དང་། ཨ་མོ་གྷ་པཱ་ཤ་དང་། རྣམ་པར་རྒྱལ་བའི་རྒྱུད་ཆེན་པོ་ལ་སོགས་པ་སྟོང་ཕྲག་བཞི་བཞུགས་སོ། །

[Block 1171]
སྤྱོད་པའི་རྒྱུད་ནི་རྣམ་པར་སྣང་མཛད་མངོན་པར་བྱང་ཆུབ་པའི་རྒྱུད་དང་། ལག་ན་རྡོ་རྗེ་དབང་བསྐུར་བའི་རྒྱུད་ལ་སོགས་པ་རྒྱུད་སྡེ་སྟོང་ཕྲག་བརྒྱད་བཞུགས་སོ། །

[Block 1172]
རྟོག་པའི་རྒྱུད་ནི་སྒྲོལ་མ་འབྱུང་བའི་རྒྱུད་དང་། དམ་ཚིག་གསུམ་བཀོད་པའི་རྒྱལ་པོ་དང་། རྟོག་པ་ཀུན་ལས་བཏུས་པ་ལ་སོགས་པ་རྒྱུད་སྡེ་སྟོང་ཕྲག་བཞི་བཞུགས་སོ། །

[Block 1173]
གཉིས་ཀའི་རྒྱུད་ནི་སྒྱུ་འཕྲུལ་དྲ་བ་དང་། པདྨ་གར་གྱི་དབང་ཕྱུག་ལ་སོགས་པ་རྒྱུད་སྡེ་སྟོང་ཕྲག་དྲུག་བཞུགས་སོ། །

[Block 1174]
དེ་ལ་རྣལ་འབྱོར་གྱི་རྒྱུད་ནི་ཏ་ཏ་ཏྭཱ་སཾ་གྲ་ཧ་དང་། དཔལ་མཆོག་དང་པོ་དང་། འཇིག་རྟེན་གསུམ་ལས་རྣམ་པར་རྒྱལ་བ་དང་། ཡང་ཡོ་ག་རྣམ་པར་རྒྱལ་བ་དང་། རྡོ་རྗེ་རྩེ་མོ་ལ་སོགས་པ་གྲངས་མེད་དོ། །

[Block 1175]
དེ་ལ་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ནི་དཔལ་གསང་བ་འདུས་པར་བཤད་རྒྱུད་དང་བཅས་པ་དང་། ཟླ་གསང་ཐིག་ལེ་དང་། གཤིན་རྗེའི་གཤེད་ནག་པོ་དང་། དཔལ་མཆོག་དང་པོ་དང་། ལྷ་ཐམས་ཅད་འདུས་པ་དང་། ཐམས་ཅད་གསང་བ་དང་། འདུལ་བ་དོན་ཡོད་པ་དང་། ཡེ་ཤེས་རྡོ་རྗེ་ཀུན་ལས་བཏུས་པ་དང་། རྣམ་པར་སྣང་མཛད་སྒྱུ་འཕྲུལ་དང་། ནམ་མཁའ་དང་མཉམ་པ་ཆུང་ངུ་དང་། གཉིས་སུ་མེད་པ་རྣམ་པར་རྒྱལ་བའི་རྒྱུད་དང་། རྡོ་རྗེ་གཙུག་ཏོར་རྒྱུད་ལ་སོགས་པ་རྒྱུད་སྡེ་སྟོང་ཕྲག་བཅུ་གཉིས་ཏེ་རྒྱས་པར་བྱ་ན་གྲངས་མེད་དོ། །

[Block 1176]
རྣལ་འབྱོར་བླ་ན་མེད་པའི་རྒྱུད་ནི་དཔལ་ནམ་མཁའ་དང་མཉམ་པ་འབུམ་པ་ཆེན་པོ་འཁོར་ལོ་སྡོམ་པ་དང་། རྡོ་རྗེ་མཁའ་འགྲོ་དང་། རྡོ་རྗེ་གདན་བཞི་པ་དང་། མ་ཧཱ་མཱ་ཡཱ་དང་། སངས་རྒྱས་མཉམ་སྦྱོར་དང་། སངས་རྒྱས་ཐོད་པ་དང་། དགྱེས་པའི་རྡོ་རྗེ་འབུམ་ཕྲག་ལྔ་པ་ལ་སོགས་པ་རྒྱུད་སྡེ་སྟོང་ཕྲག་བཅུ་བཞི༌[^654]བཞུགས་ཏེ་རྒྱས་པར་བྱས་ན༌[^655]གྲངས་མེད་དོ། །

[Block 1177]
དེ་ལྟར་རྒྱུད་སྡེ་རེ་རེ་ཞིང་ཡང་གྲངས་མེད་པས་ན་གསང་སྔགས་ཀྱི་ཐེག་པ་ནི་ཤིན་ཏུ་རྒྱས་ཤིང་མཐར་ཐུག་པ་མེད་པ་ཡིན་ནོ། །

[Block 1178]
འདི་ལྟར་ཡི་དགས་ཁ་ནས་མེ་འབར་བའི་གཟུངས་དང་། རྨ་བྱ་ཆེན་མོའི་གཟུངས་ལ་སོགས་པ་གཟུངས་མ་ལུས་པ་ཐམས་ཅད་ཀྱང་བྱ་བའི་རྒྱུད་ཡིན་ནོ་ཞེས་བླ་མ་དག་གསུང་ངོ་།[^656] །གསུངས་པའི་ཞེས་པ་ནི་ཇི་ལྟར་གསུངས་ཤེ་ན། འདི་སྐད་དུ།

[Block 1179 [VERSE]]
གལ་ཏེ་གསང་སྔགས་སྤྱོད་འདོད་པས། །
དེ་ཚེ་སློབ་དཔོན་དབང་བསྐུར་ཕྱིར། །

[Block 1180]
ཞེས་གསུངས་ཏེ། འདི་ལྟར་གལ་ཏེ་བྱ་བའི་རྒྱུད་ལ་སོགས་པའི་གསང་སྔགས་ཀྱི་ཐེག་པ་ལ་སྤྱོད་པར་འདོད་པ་ཡིན་ན་ནི་སློབ་དཔོན་གྱི་དབང་བསྐུར་བ་ཞེས་བྱ་བ་བུམ་པའི་དབང་ཐོབ་པར་མ་བྱས་པར་སྨོན་པ་དང་འཇུག་པའི་སེམས་བསྐྱེད་པ་ཙམ་ལ་ལྟོས་པར༌[^657]མི་བྱ་སྟེ། གསང་སྔགས་རང་ཉིད་ལེན་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1181]
དེ་ཡང་རྒྱུད་ལས།

[Block 1182 [VERSE]]
སློབ་དཔོན་མཉེས་པར་མ་བྱས་ཤིང་། །
དབང་རྣམས་ཐོབ་པར༌[^658]མ་བྱས་པར། །
ཉན་པ་ལ་སོགས་རྩོམ་པ་ཡང་། །
འབྲས་བུ་མེད་པ་ཉིད་དུ་འགྱུར། །

[Block 1183]
ཞེས་གསུངས་པ་དང་།

[Block 1184]
ཡང་རྒྱུད་ལས།

[Block 1185]
དབང་བསྐུར་རྗེས་གནང་མེད་པར་ཡང་། །གསང་སྔགས་རང་ཉིད་ལེན་པར་བྱེད། །

[Block 1186]
ཅེས་གསུངས་ཏེ། དཀྱིལ་འཁོར་དུ་འཇུག་པ་དང་། དབང་བསྐུར་བ་དང་། བླ་མ་དེ་ཉིད་ཀྱི་རྗེས་སུ་གནང་བ་མ་བྱས་པར་ཐེག་པ་ཆེན་པོའི༌[^659]མདོ་སྡེའི་དོན་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལམ་གྱི་ཆོ་ག་ལ་བརྟེན་ནས་གཟུངས་ཀྱི་ཆོ་ག་བྱེད་པ་དང་། གཞན་ཡང་རྗེ་བཙུན་སྒྲོལ་མ་ལ་སོགས་པའི་སྒྲུབ་ཐབས་དག་མཉན་ནས་བསྒོམ་པ༌[^660]དང་། བཟླས་པ་དང་། སྦྱིན་སྲེག༌[^661]དང་། གཏོར་མ་དང་། དཀྱིལ་འཁོར་ལ་སོགས་པ་བྱེད་པ་ནི་གསང་སྔགས་རང་ཉིད་ལོན་པ་ཡིན་ཏེ། དཀྱིལ་འཁོར་དུ་འཇུག་པ་དང་། དབང་བསྐུར་བ་བྱས་ཏེ། སློབ་དཔོན་གྱིས་འདི་སྐད་དུ་ཁྱོད་ཀྱི་ལྷ་ནི་འདི་ཡིན་ནོ། །

[Block 1187]
བཟླས་པ་འདི་བྱ་དགོས་སོ་ཞེས་རྗེས་སུ་གནང་བ་མ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 1188]
དེ་བས་ན་རྒྱུད་ལས།

[Block 1189 [VERSE]]
གསང་སྔགས་རང་ཉིད་ལེན་པ་ནི། །
འགྲོ་བ་དམྱལ་བ་འབའ་ཞིག་སྟེ། །
སྔགས་ཀྱང་འགྲུབ་པར་མི་འགྱུར་ཞིང་། །
ལུས་ཉོན་མོངས་པ་ཁོ་ནར་ཟད། །

[Block 1190]
ཅེས་གསུངས་སོ། །

[Block 1191]
དེ་དག་ནི་གསུངས་པའི་ཚིག་གི་དོན་ཡིན་ཏེ། རྒྱུད་ཐམས་ཅད་དང་། སྔོན་གྱི་སློབ་དཔོན་ཐམས་ཅད་དང་། ད་ལྟ༌[^662]ཉིད་ཀྱི་བླ་མ་མ་ལུས་པས་འདི་སྐད་དུ་གསུངས་ཞེས་པའོ། །

[Block 1192]
ཡང་ན་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་ལྷའི་པྲ་ཕབ་པ་དང་། རྨི་ལམ་དག་ཏུ་གང་ཟག་འདི་ནི་སྐྱེ་བ་སྔ་མ་ལ་གསང་སྔགས་སྤྱོད་སྤྱོད་པ་དག་ཡིན་ནོ་ཞེས་ཟེར་ན། དེས་བླ་མ་ཡོངས་སུ་མཉེས་པར་བྱས་ལ་བྱིན་གྱིས་བརླབ་པ་བྱས་ཏེ། འདི་ལྟར་སྒྲུབས༌[^663]ཤིག་ཅེས་གནང་བ་བྱིན་ལ། སྒྲུབ་པའི་ཆོ་གའི་ཐབས་སྦྱིན་པར་བྱའོ། །

[Block 1193]
ཆོ་ག་དེ་ཡང་འདི་ཡིན་ཏེ། འཕགས་པ་དམ་ཚིག་གསུམ་བཀོད་པའི་ཆོ་ག་དང་། བཅོམ་ལྡན་འདས་ནོར་བུ་རྒྱས་པའི་གཞལ་མེད་ཁང་གི་ཆོ་ག་དང་། བཅོམ་ལྡན་འདས་སྨན་གྱི་བླ་བཻ་ཌཱུརྱའི་འོད་ཀྱི་རྒྱལ་པོའི་ཆོ་གས་སྡིག་པ་སྦྱོང་བ་དང་། ཚོགས་བསགས་པ་བྱས་ལ་ལྟས་བཟང་པོ་བྱུང་བ་ན་གང་ཟག་དེས་གསང་སྔགས་ཀྱི་ཐེག་པ་ལ་འཇུག་པར་གནང་གི་འདི་ལྟར་སྐྱེ་བ་སྔ་མ་ལ་གསང་སྔགས་སྤྱད་པ་མ་ཡིན་པ་དང་། ཡང་ན་གསུམ་ལ་སྐྱབས་སུ་འགྲོ་བ་དང་། སྨོན་པ་བྱང་ཆུབ་ཀྱི་སེམས་བསྐྱེད་པ་དང་། འཇུག་པ་བྱང་ཆུབ་ཀྱི་སེམས་བསྐྱེད་པ་བྱས་པ་ཙམ་ལ་ནི་གསང་སྔགས་བསྟན་པ་དང་། དེས་བསྒྲུབ་པ་དང་བལྟ་བ་དང་མཉན་པ༌[^664]བྱ་བར་མ་གནང་སྟེ། འཇུག་པའི་ལམ་སོ་སོ་བ་ཡིན་པ་དང་། ཐེག་པ་དག་ནི་རྣམ་པར་ཐར་པ་བསྲེ་བར་མི་བྱ་བ་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས༌[^665]གང་ཟག་གི༌[^666]དབང་པོ་དང་ཁམས་དང་བག་ལ་ཉལ་མཁྱེན་པས༌[^667]ཐེག་པའི་ལམ་སོ་སོར་གསུངས་པ་ཡིན་ནོ། །

[Block 1194]
དེ་བས་ན་རྩ་བ་ནས་སྨྲས་པ་དེ་ལྟ་བས་ན།

[Block 1195 [VERSE]]
གལ་ཏེ་གསང་སྔགས་སྤྱོད་འདོད་པས། །
དེ་ཚེ་སློབ་དཔོན་དབང་བསྐུར༌[^668]ཕྱིར། །
--- END BLOCKS ---
