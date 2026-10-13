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
དམྱལ་བ་དང་།

[Block 1122 [VERSE]]
གླིང་དབྱེ་བ་ལས་དེ་ཉི་ཤུ། །
གནས་རྣམས་ཞེས་བྱ་བ་ཚིག་ལྷག་མའོ། །

[Block 1123]
དམྱལ་བ་ཆེན་པོ་བརྒྱད་དེ། ཡང་སོས་དང་། ཐིག་ནག་དང་། བསྡུས་འཇོམས་དང་། ངུ་འབོད་དང་། ངུ་འབོད་ཆེན་པོ་དང་། ཚ་བ་དང་། རབ་ཏུ་ཚ་བ་དང་། མནར་མེད་པ་དང་། གླིང་བཞི་དང་། ཡི་དགས་དང་། དུད་འགྲོ་ཞེས་བྱ་བ་གནས་ཉི་ཤུ་པོ་འདི་དག་འདོད་པའི་ཁམས་སོ། །

[Block 1124]
འདོད་པའི་ཁམས་འདིའི་གོང་མའི་གནས་དག་བཅུ་བདུན་ནི། གཟུགས་ཁམས་ཡིན། ཇི་ལྟར་ཡིན་ཞེ་ན། དེར་སོ་སོ་ཡི།

[Block 1125 [VERSE]]
བསམ་གཏན་ས་ནི་གསུམ་པ་ཡིན། །
བཞི་པས་ནི་བརྒྱད་པ་ཡིན། །

[Block 1126]
ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལ་བསམ་གཏན་དང་པོ་ན་ནི་ཚངས་རིས་རྣམས་དང་། ཚངས་པའི་མདུན༌[^416]ན་འདོན་རྣམས་དང་། ཚངས་ཆེན་རྣམས་སོ། །

[Block 1127]
གཉིས་པ་ན་ནི་འོད་ཆུང་རྣམས་དང་། ཚད་མེད་འོད་རྣམས་དང་། འོད་གསལ་རྣམས་སོ། །

[Block 1128]
གསུམ་པ་ན་ནི་དགེ་ཆུང་རྣམས་དང་། ཚད་མེད་དགེ་རྣམས་དང་། དགེ་རྒྱས་རྣམས་སོ། །

[Block 1129]
བཞི་པ་ན་ནི་སྤྲིན་མེད་འོད་རྣམས་དང་། བསོད་ནམས་སྐྱེས་རྣམས་དང་། འབྲས་བུ་ཆེ་རྣམས་དང་། མི་ཆེ་བ་རྣམས་དང་། མི་གདུང་བ་རྣམས་དང་། གྱ་ནོམ་སྣང་རྣམས་དང་། ཤིན་ཏུ་མཐོང་རྣམས་དང་། འོག་མིན་རྣམས་ཞེས་བྱ་བ་གནས་བཅུ་བདུན་པོ་འདི་དག་ནི་གཟུགས་ཀྱི་ཁམས་སོ། །

[Block 1130 [VERSE]]
གཟུགས་མེད་ཁམས་ན་གནས་མེད་དོ། །
སྐྱེ་བ་ལས་ནི་རྣམ་པ་བཞི། །

[Block 1131]
འདི་ལྟ་སྟེ། ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་དང་། རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་དང་། ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་དང་། འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་སྐྱེ་མཆེད་དོ། །

[Block 1132]
དེར་ནི་རིས་དང་སྲོག་ལ་ཡང་། །སེམས་ཀྱི་རྒྱུད་ནི་རྟེན༌[^417]ཡིན། ཁམས་གསུམ་པོ༌[^418]བཤད་པ་གང་ཡིན་པ།

[Block 1133 [VERSE]]
དེར་ནི་དམྱལ་སོགས་འགྲོ་བ་ལྔ། །
རང་གི་མིང་གིས་བསྟན་དེ་དག །

[Block 1134]
གང་གིས་ན་དེ་དག༌[^419]ཁམས་གསུམ་དག་ཏུ་ཞེས་བྱ་བ་ལ། ཅི་འགྲོ་བ་ལ་མ་གཏོགས་པའི་ཁམས་དག་ཅིག་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། ཁམས་རྣམས་ནི་དགེ་བ་དང་། ཉོན་མོངས་པ་ཅན་དང་། སྣོད་དང་།

[Block 1135]
སྲིད་པ་བར་མ་པའི་རང་བཞིན་དག་ཀྱང་ཡིན་ནོ། །ཡང་འགྲོ་བ་ལྔ་པོ་དག་གང་ཡིན་པ་དེ་དག །

[Block 1136 [VERSE]]
ཉོན་མོངས་ཅན་མིན་ལུང་བསྟན་མིན། །
སེམས་ཅན་ཞེས་བྱ་བར་སྲིད་མིན། །

[Block 1137]
འགྲོ་བ་ལྔ་ནི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཉིད་དོ། །

[Block 1138]
དེ་ལྟ་མ་ཡིན་ན་འགྲོ་བ་འཆོལ་བར་འགྱུར་རོ། །

[Block 1139]
སེམས་ཅན་ཞེས་བྱ་བ་ཉིད༌[^420]ཡིན་ཡང་སྲིད་པ་བར་མའི་རང་བཞིན་ནི༌[^421]མ་ཡིན་ནོ། །

[Block 1140 [HEADING]]
#### རྣམ་པར་ཤེས་པ་གནས་པ་བདུན། ^3-1-2-0

[Block 1141]
འགྲོ་བ་ལྔ་པའི་ཁམས་གསུམ་འདི་ཉིད་དུ།

[Block 1142 [VERSE]]
ལུས་དང་འདུ་ཤེས་ཐ་དད༌[^422]དང་། །
ལུས་ཐ་དད་ཅིང་འདུ་ཤེས་གཅིག །
བཟློག་དང་ལུས་དང་འདུ་ཤེས་གཅིག །
གཟུགས་ཅན་མ་ཡིན་གསུམ་པོ་དག །
རྣམ་ཤེས་གནས་པ་བདུན།

[Block 1143]
རིམ་པ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 1144]
མདོ་ལས།

[Block 1145]
སེམས་ཅན་དུས༌[^423]ཐ་དད་ཅིང་འདུ་ཤེས་ཐ་དད་པ་དག་ཀྱང་ཡོད་དོ།[^424] །

[Block 1146]
འདི་ལྟ་སྟེ། མི་རྣམས་དང་ལྷ་ཁ་ཅིག་གོ། །

[Block 1147]
དེ་ཡང་འདོད་པ་ན་སྤྱོད་པ་རྣམས་དང་། བསམ་གཏན་དང་པོ་པ་དང་པོར་བྱུང་བ་མ་གཏོགས་པ་རྣམས་སོ། །

[Block 1148]
སེམས་ཅན་གཟུགས་ཅན་ལུས་ཐ་དད་ཅིང་འདུ་ཤེས་གཅིག་པ་དག་ཀྱང་ཡོད་དེ། འདི་ལྟ་སྟེ༌[^425]ཚངས་རིས་ཀྱི་ལྷ་གང་དག་དང་པོར་བྱུང་བ་དེ་དག་གོ། །

[Block 1149]
དེ་དག་ཐམས་ཅད་ནི་འདི་སྙམ་དུ་བདག་ཅག་ནི་ཚངས་པ་འདིས་ཕྱུང་ངོ་སྙམ་དུ་ཤེས་པར་འགྱུར་ལ། ཚངས་པ་ཡང་འདི་དག་ནི་བདག་གིས་ཕྱུང་ངོ་སྙམ་དུའོ། །

[Block 1150]
སེམས་ཅན་གཟུགས་ཅན་ལུས་གཅིག་ཅིང་འདུ་ཤེས་ཐ་དད་པ་དག་ཀྱང་ཡོད་དེ། འདི་ལྟ་སྟེ་འོད་གསལ་གྱི་ལྷ་རྣམས་སོ། །

[Block 1151]
འདིར་ནི་མཐའ་སྨོས་པས་བསམ་གཏན་གཉིས་པ་མཐའ་དག་སྨོས་པར་རིག་པར་བྱའོ། །

[Block 1152]
སེམས་ཅན་གཟུགས་ཅན་ལུས་གཅིག་ཅིང་འདུ་ཤེས་གཅིག་པ་དག་ཀྱང་ཡོད་དེ། འདི་ལྟ་སྟེ་དགེ་རྒྱས་ཀྱི་ལྷ་རྣམས་སོ། །

[Block 1153]
འདུ་ཤེས་གཅིག་པ་དག་ཅེས་བྱ་བ་ནི་བདེ་བར་འདུ་ཤེས་པ་དག་གོ། །

[Block 1154]
དེ་ལ་བསམ་གཏན་དང་པོ་ནི་ཉོན་མོངས་པ་ཅན་གྱི་འདུ་ཤེས་སུ་འདུ་ཤེས་གཅིག་པ་དག་ཡིན་ནོ། །

[Block 1155]
གཉིས་པ༌[^426]ནི་དགེ་བས་འདུ་ཤེས་ཐ་དད་པ་དག་ཡིན་ནོ། །

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
--- END BLOCKS ---
