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
[Block 1156]
གསུམ་པ་ནི་རྣམ་པར་སྨིན་པ་ལས་བྱུང་བས་འདུ་ཤེས་གཅིག་པ་དག་ཡིན་ནོ། །

[Block 1157]
གཟུགས་མེད་པ་གསུམ་པོ་ནི་མདོ་ལས་ཇི་སྐད༌[^427]འབྱུང་བ་སྟེ། དེ་ལྟར་ན། དེ་དག་ནི་རྣམ་པ༌[^428]གནས་པ་བདུན་ཡིན་ནོ། །ཅིའི་ཕྱིར་ལྷག་མ་རྣམ་པར་ཤེས་པ་མ་ཡིན་ཞེ་ན། འདི་ལྟར། ལྷག་མ། དེ་འཇོམས་བྱེད་ལྡན། ལྷག་མ་གང་ཞིག་ཅེ་ན། ངན་འགྲོ་རྣམས་དང་། བསམ་གཏན་བཞི་པ་དང་། སྲིད་པའི་རྩེ་མོའོ། །

[Block 1158]
འདི་དག་ན་རྣམ་པར་ཤེས་པ་འཇོམས་པར་བྱེད་པ་དག་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1159]
དེ་ལ་ངན་སོང་ན་ནི་འཇོམས་པར་བྱེད་པ་སྡུག་བསྔལ་གྱི་ཚོར་བའོ། །

[Block 1160]
བསམ་གཏན་བཞི་པ་ན་ནི་འདུ་ཤེས་མེད་པ་པའོ། །

[Block 1161]
སྲིད་པའི་རྩེ་མོ་ན་ནི་འགོག་པའི་སྙོམས་པར་འཇུག་པའོ། །

[Block 1162 [HEADING]]
#### སེམས་ཅན་གྱི་གནས་དགུ། ^3-1-3-0

[Block 1163]
རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་པོ་ཇི་སྐད་བཤད་པ་དེ་དག་དང་། སྲིད་རྩེ་དང་།

[Block 1164 [VERSE]]
འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས། །
སེམས་ཅན་གྱི་ནི་གནས་དགུར་བཤད། །

[Block 1165]
འདི་དག་ཏུ་སེམས་ཅན་རྣམས་རང་དགའ་བས་ཀུན་དུ་གནས་སོ། །

[Block 1166]
མི་འདོད་བཞིན་གནས་ཕྱིར་གཞན་མིན། །ངན་སོང་དག་ཏུ་ནི་སེམས་ཅན་རྣམས་མི་འདོད་བཞིན་དུ་ལས་ཀྱི་སྲིན་པོས་ཀུན་དུ་གནས་སུ་འཇུག་གོ། །

[Block 1167]
མདོ་གཞན་ལས་ནི་རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་ཞེས་གསུངས།

[Block 1168]
གཞན་ལས་ནི། གནས་པ་དག་ནི་ཡང་བཞི་སྟེ། རྣམ་པར་ཤེས་པ་གཟུགས་སུ་ཉེ་བར་འགྲོ་བ་དང་། ཚོར་བར་ཉེ་བར་འགྲོ་བ་དང་། འདུ་ཤེས་སུ་ཉེ་བར་འགྲོ་བ་དང་། འདུ་བྱེད་དུ་ཉེ་བར་འགྲོ་བའོ། །

[Block 1169]
དེ་དག་གི་རང་བཞིན་ཅི་ཞེ་ན། ཟག་པ༌[^429]དང་བཅས་པའི་ཕུང་པོ་བཞི། དེ་དག་ཀྱང་། རང་གི་ས་པ་ཉིད། ས་གཞན་དུ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། གནས་པ་ནི་རྟེན་པ་མ༌[^430]ཡིན་ན་སྐལ་བ་མི་མཉམ་པའི་ས་པའི༌[^431]ཕུང་པོ་དག་ནི་རྣམ་པར་ཤེས་པ་སྲིད་པའི་དབང་གིས་མི་རྟེན་པའི་ཕྱིར་རོ། །

[Block 1170]
ཅིའི་ཕྱིར་རྣམ་པར་ཤེས་པ་ལ་རྣམ་པར་ཤེས་པ་ཞེས་མི་བྱ་ཞེ་ན། དཔེར་ན་རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་བཞིན་ནོ། །

[Block 1171]
བདུན་ལ་རིགས་ཏེ། དེ་ལ་བྱེ་བྲག་མེད་པར་ནི་སྐྱེ་བའི་སྐྱེ་མཆེད་ཀྱིས་བསྡུས་པའི་ཕུང་པོ་དག་ལས༌[^432]མངོན་པར་དགའ་བ་དང་བཅས་པའི་རྣམ་པར་ཤེས་པ་འཇུག་ན༌[^433]རྣམ་པར་ཤེས་པ་ལ་རྣམ་པར་ཤེས་པ་གནས་པ་ཞེས་བྱའོ། །

[Block 1172]
སོ་སོར་དབྱེ་ན་ནི་ཇི་ལྟར་གཟུགས་ལ་སོགས་པ་ཀུན་ནས་ཉོན་མོངས་པར་བྱེད་པ་ཡིན་པ་ལྟར། རྣམ་པར་ཤེས་པ་འབའ་ཞིག་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་རྣམ་པར་ཤེས་པ་གནས་པ་བཞི་དག་ཏུ། རྣམ་ཤེས་འབའ་ཞིག་གནས་པར་མ་བཤད་དོ། །

[Block 1173]
ཡང་ཅི་རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་གྱིས༌[^434]བཞི་བསྡུས་སམ། འོན་ཏེ་བཞིས་བདུན་བསྡུས་ཤེ་ན། བདུན་གྱིས་བཞི་ཡང་མ་ཡིན་ལ། བཞིས་ཀྱང་བདུན་མ་ཡིན་ནོ། །

[Block 1174]
བསྡུ་ན་མུ༌[^435]བཞི་ཡིན་ནོ། །

[Block 1175]
བདུན་གྱིས་བསྡུས་ལ་བཞིས་མ་ཡིན་པ་ཡང་ཡོད་དེ༌[^436]ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་སྟེ། མུ་དང་པོ་ནི་བདུན་དག་ཏུ་རྣམ་པར་ཤེས་པ་གང་ཡིན་པའོ། །

[Block 1176]
གཉིས་པ་ནི་ངན་སོང་རྣམས་དང་། བསམ་གཏན་བཞི་པ་རྣམས་དང་། སྲིད་པའི་རྩེ་མོ་ན་རྣམ་པར་ཤེས་པ་མ་གཏོགས་པའི་ཕུང་པོ་རྣམས་སོ། །

[Block 1177]
གསུམ་པ་ནི་བདུན་དག་ཏུ་ཕུང་པོ་བཞི་རྣམས་སོ། །

[Block 1178]
བཞི་པ་ནི་ངན་སོང་དག་གི་རྣམ་པར་ཤེས་པའོ། །

[Block 1179 [HEADING]]
#### སྐྱེ་གནས་བཞི། ^3-1-4-0

[Block 1180]
འགྲོ་བ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་ཐ་དད་པའི་ཁམས་གསུམ་བཤད་པ་གང་ཡིན་པ།

[Block 1181 [VERSE]]
དེར་ནི་སྒོ་ང་ལས་སྐྱེས་སོགས། །
སེམས་ཅན་སྐྱེ་གནས་བཞི་དག་ཏུ། །

[Block 1182]
རིག་པར་བྱ་སྟེ། སྒོ་ང་ལས་སྐྱེས་པའི་དང་། མངལ་ལས་སྐྱེས་པའི་དང་། དྲོད་གཤེར་ལས་སྐྱེས་པའི་དང་། རྫུས་ཏེ་སྐྱེས་པའི་སྐྱེ་གནས་སོ། །

[Block 1183]
འདིར་སེམས་ཅན་རྣམས་འཆོལ་བར་འགྱུར་ཞིང་སྐྱེ་བ་ཐུན་མོང་བའི་ཕྱིར་འདྲེ་བར་འགྱུར་བས་སྐྱེ་གནས་སོ། །

[Block 1184]
ཡང་འགྲོ་བ་གང་ན་སྐྱེ་གནས་དུ་ཞིག་ཡོད་ཅེ་ན། སྨྲས་པ།

[Block 1185 [VERSE]]
མི་དང་དུད་འགྲོ་རྣམ་པ་བཞི། །
དམྱལ་བ་རྣམས་དང་ལྷ་རྣམས་དང་། །
སྲིད་པ་བར་མ་རྫུས་ཏེ་སྐྱེ། །

[Block 1186]
མི་དང་དུད་འགྲོ་དག་རྣམ་པ་བཞི་ཅི་རིགས་པར་བརྗོད་པར་བྱའོ། །

[Block 1187]
དམྱལ་བ་དང་། སྲིད་པ་བར་མ་དང་། ལྷ་ཐམས་ཅད་རྫུས་ཏེ་སྐྱེའོ། །

[Block 1188 [VERSE]]
ཡི་དགས་མངལ་ནས་སྐྱེ་བ་འང༌[^437]ཡིན། །
རྫུས་ཏེ་སྐྱེ་བ་དག་ཀྱང་ཡིན་ནོ། །

[Block 1189 [HEADING]]
#### སྲིད་པ་བར་མ། ^3-1-5-0

[Block 1190]
སྲིད་པ་བར་མ་ཞེས་བྱ་བ་དེ་ཅི་ཞེ་ན།

[Block 1191 [VERSE]]
འདིར་གང་སྐྱེ་དང་འཆི་བ་ཡི། །
སྲིད་པའི་བར་དུ་འབྱུང་བའོ། །

[Block 1192]
འགྲོ་བའི་བར་མ་ཡིན་པའི་ཕྱིར་སྲིད་པའི་བར་མའོ། །

[Block 1193]
ཇི་ལྟར་ན་འདི་སྐྱེས་པ་ཡང་ཡིན་ལ། འབྱུང་བ༌[^438]ཡང་མ་ཡིན་ཞེ་ན།

[Block 1194 [VERSE]]
བགྲོད་པའི་ཡུལ་དུ་མ་ཕྱིན་ཕྱིར། །
སྲིད་པ་བར་མ་བྱུང་བ་མིན། །

[Block 1195]
སོན་པ་ནི་བྱུང་བ་ཡིན་ན་འདི་ཡང༌[^439]བགྲོད་པར་བྱ་བའི་ཡུལ་དུ་སོན་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་བྱུང་བ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
