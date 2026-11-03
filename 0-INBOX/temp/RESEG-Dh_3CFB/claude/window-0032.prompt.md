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
སྐྱེད་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ཉིད་དངོས་པོ་ཡིན་ལ་སྐྱེད་པར་བྱེད་པ་དེ་ཡང་གཞན་ལ་མེད་པའི་ཕྱིར། གཞན་གྱིས་བསྐྱེད་པར་མི་འགྱུར་རོ། །

[Block 1122]
གལ་ཏེ་དེ་ནི་སྐྱེད་པར་བྱེད་པའི་རང་བཞིན་གང་ཡིན་པ་དེ་ནི་གཞན་གྱིར་ཡང་འགྱུར་ན། དེའི་རང་བཞིན་དེས་དེ་ལ་ཐ་དད་པར་མི་འགྱུར་བའི་ཕྱིར། རང་བཞིན་གྱིས་རྗེས་སུ་འགྲོ་བ་ཡོད་དོ་ཞེ་ན།

[Block 1123 [VERSE]]
གལ་ཏེ་བདག་ཉིད་གཅིག་པ་ཡིས། །
དུ་མ་འབྲས་བུ་གཅིག་བྱེད་ན། །
བདག་ཉིད་གཅིག་ལའང་དེ་ཡོད་ཕྱིར། །
ལྷན་ཅིག་བྱེད་པ་དོན་མེད་འགྱུར། །

[Block 1124]
གལ་ཏེ་རང་བཞིན་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར། དུ་མ་གཅིག་བྱེད་པ་ཡིན་ན་དེ་དག་གི་ཐ་དད་པ་མེད་པའི་རང་བཞིན་དེ་ནི་གཅིག་ཉེ་ཡང་ཡོད་པས་རྒྱུ་དང་མ་བྲལ་བའི་ཕྱིར། གཅིག་ཀྱང་སྐྱེད་པར་བྱེད་པར་འགྱུར་རོ། །

[Block 1125]
འདི་ལྟར།

[Block 1126 [VERSE]]
ཐ་དད་མེད་པའི་ངོ་བོ་དེ། །
བྱེད་མིན་ཁྱད་པར་རྣམས་དང་བྲལ། །

[Block 1127]
ཐ་དད་པ་མེད་པའི་རང་བཞིན་དེ་ལ་དེ་ནི༌[^923]གཞན་གྱིས༌[^924]ཁྱད་པར་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1128]
ཁྱད་པར་ཡོད་ན་ཐ་དད་པ་མེད་པ་ཉམས་པའི་ཕྱིར་རོ། །

[Block 1129]
དེ་ཡང་དེ་ལ་ཡང་ཡོད་པས་གཅིག་གནས་པ་ལ་ཡང་དེའི་བྲལ་བ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1130]
ཁྱད་པར་གང་ཡིན་པ་དེ་དག་ནི་ལྷན་ཅིག་གནས་པའི་ངེས་པ་མེད་པའི་ཕྱིར་བྲལ་བར་འགྱུར་རོ། །

[Block 1131]
དེ་དག་སྐྱེད་པར་བྱེད་པར་འདོད་པ་ཡང་མ་ཡིན་ཏེ། ལྷན་ཅིག་བྱེད་པ་དག་ནི་རང་བཞིན་གཅིག་པ་ཉིད་ཀྱིས་བསྐྱེད་པ་ཉིད་དུ་ཁས་བླངས་པའི་ཕྱིར་རོ། །

[Block 1132]
དེ་བས་ན་སྐྱེད་པར་བྱེད་པ་གནས་པའི་ཕྱིར་དང་། གནས་པ་མེད་པ་ནི་སྐྱེད་པར་བྱེད་པ་ཉིད་མ་ཡིན་པའི་ཕྱིར། གནས་པ་གཅིག་གིས་ཀྱང་འབྲས་བུ་བསྐྱེད་པར་འགྱུར་བ་ཞིག་ན༌[^925]འགྱུར་བ་ཡང་མ་ཡིན་ནོ། །

[Block 1133]
དེ་བས་ན། གཅིག་དང་བྲལ་བ་འབྲས་མེད་ཕྱིར། ཁྱད་པར་རྣམས་ལས་དེ་དག་འབྱུང་། །ལྷན་ཅིག་བྱེད་པ་དུ་མའི་ཐུན་མོང་དུ་གྱུར་པའི་འབྲས་བུ་དེ་ནི་ཁྱད་པར་གཅིག་དང་བྲལ་ན་ཡང་མི་འགྱུར་ཞིང་ཁྱད་པར་ཐམས་ཅད་དང་མ་བྲལ་བ༌[^926]དག་ལ་ཡང་འགྱུར་ཏེ། མ་བྲལ་ན་ཡང་ཐ་དད་པ་མེད་པའི་ངོ་བོ་ཡང་མ་ཡིན་ནོ། །

[Block 1134]
འབྲས་བུ་ནི་འགའ་ཞིག་ལས་བྱུང་བའི་ཆོས་ཅན་མི་འགྱུར་བ་གང་ཡིན་པ་དེ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1135]
ཐ་དད་པ་མེད་པའི་ངོ་བོ་གཅིག་གནས་པ་ལ་ཡང་བྲལ་བ་ཉིད་ཡོད་པ་མ་ཡིན་ལ་མ་བྲལ་བ་དེ་ལ་ཡང་མེད་ན་དེ་སྐྱེད་པར་བྱེད་པའི་བདག་ཉིད་མ་ཡིན་པར་སྟོན་པར་བྱེད་དོ། །

[Block 1136]
གང་ཚོགས་པ་དང་བྲལ་པ་དང་འདྲ་བ་དེ་ཉིད་ལས་སྐྱེ་བ་དེ་ལ་ཡོད་ན་ངེས་པ་ཡོད་པར་འགྱུར་གྱི། དེ་ལས་གཞན་ལས་སྐྱེ་བར་རྟོག་ན་ནི་ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1137]
དེ་བས་ཁྱད་པར་སྐྱེད་པར་བྱེད་པ་ཡིན་གྱི་སྤྱི་ནི་མ་ཡིན་ནོ། །

[Block 1138]
དེའི་ཕྱིར༌[^927]དེ་ཁོ་ན་དངོས་པོ་ཡིན་ནོ། །

[Block 1139]
འདི་ལྟར།

[Block 1140 [VERSE]]
དོན་བྱེད་ནུས་པ་གང་ཡིན་པ། །
དེ་ཉིད་དོན་དམ་པར་ཡོད་པའོ། །

[Block 1141]
དངོས་པོ་དང་དངོས་པོ་མེད་པའི་མཚན་ཉིད་ནི་གང་དོན་བྱེད་པར་རུང་བ་ཉིད་དང༌[^928]མི་རུང་བ་ཉིད་ཅེས་བྱ་བ་འདི་ཉིད་འཆད་པར་འགྱུར་རོ། །

[Block 1142 [VERSE]]
དོན་བྱེད་ནུས་པར་རུང་བའི་དོན། །
དེ་ཡང་རྗེས་འགྲོ་མེད་གང་ཞིག །
རྗེས་འགྲོ་དེ་ལས་འབྲས་ཡོད་མིན། །

[Block 1143]
དེ་བས་སྤྱི་ཐམས་ཅད་ནི་དོན་བྱེད་པར་རུང་བ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ།[^929] ། དངོས་པོ་མེད་པ་ཡིན་ལ། དངོས་པོ་ནི་ཁྱད་པར་ཁོ་ན་ཡིན་ཏེ། དེ་ཁོ་ན་ཉིད་ལས་དེ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1144]
འོན་ཀྱང་རང་བཞིན་གྱི་རྗེས་སུ་འགྲོ་བ་མེད་པས་གཅིག་གི་སྐྱེད་པར་བྱེད་པའི་ངོ་བོ་གཞན་ལ་མེད་པའི་ཕྱིར། སྐྱེད་པར་བྱེད་པར་མི་འགྱུར་བའམ།[^930] སྐྱེད་པར་བྱེད་པ༌[^931]ཡིན་ན་ཐ་དད་པ་ཁྱད་པར་མེད་པའི་ཕྱིར།

[Block 1145 [VERSE]]
ཐམས་ཅད་བསྐྱེད་པ་པོར་འགྱུར་རོ། །
དེ་ནི་མ་ཡིན་ཏེ་འདི་ལྟར།
བདག་དེ་ཤིན་ཏུ་ཐ་དད་ཀྱང་། །
འགའ་ཞིག་རྒྱུ་ཡིན་གཞན་པ་མིན། །

[Block 1146]
རང་བཞིན་འདི་ཡིན་གཅིག་གི་སྐྱེད་པར་བྱེད་པའི་བདག་ཉིད་ལས་ཐམས་ཅད་ཐ་དད་པར་གྱུར་པ་ན་མཚུངས་པར་སྐྱེད་པར་བྱེད་པའམ། འགའ་ཞིག་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེར་འགྱུར་ན། ཇི་ལྟར་དེ་དག་ལ་ཁྱད་པར་ཡོད་པར་མི་འགྱུར། དེ་བས་ན་ཐ་དད་པའི་ཁྱད་པར་ཡོད་ན་ཡང་འགའ་ཞིག་ལས་བདག་ཉིད་ཕུལ་དུ་བྱུང་བ་ཡིན་པའི་ཕྱིར། འགའ་ཞིག་སྐྱེད་པར་བྱེད་པ་ཡིན་པ་གཞན་མ་ཡིན་པ་དེ་ནི་དེའི་རང་བཞིན་ཡིན་ཏེ། གཞན་གྱི་མ་ཡིན་ནོ། །

[Block 1147]
དངོས་པོའི་རང་བཞིན་དག་ནི་ཅིའི་ཕྱིར་མེ་ནི་སྲེག་པར་བྱེད་པའམ། དྲོ་བ་ཡིན་གྱི། ཆུ་མ་ཡིན་ཞེས་བརྒལ་ཞིང་བརྟག་པར་འོས་པ་མ་ཡིན་གྱི། རང་བཞིན་འདི་གང་ལས་ཞེས་བྱ་བ་དེ་ཙམ་དུ་འགྱུར་ཏེ། རྒྱུ་མེད་པ་ཅན་ལྟོས་པ་མེད་པ་ནི་ངེས་པ་མེད་པས་ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1148]
དེ་བས་ན་རང་བཞིན་ནི་འདིའི་རང༌[^932]གི་རྒྱུ་ལས་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1149]
དེ་ཡང་དེ་བསྐྱེད་པའི་བདག་ཉིད་དེ། གཞན་ལས་ཞེས་བྱ་བའི་རྒྱུའི་བརྒྱུད་པ་ཐོག་མ་མེད་པ་ཅན་ཡིན་ནོ། །

[Block 1150]
ཐ་དད་པ་དག་གི་འགའ་ཞིག་རྒྱུ་ཡིན་གྱི་གཞན་ནི་མ་ཡིན་ཏེ། རང་བཞིན་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་འདི་ལ་གནོད་པ་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 1151]
ཐ་དད་མིན་ན་ཡང་ཅིག་ཅར་སྐྱེ་འཇིག་འགྱུར། རང་བཞིན་ལ་ཐ་དད་པ་མེད་པ་ཉིད་ཀྱི་ཕྱིར། རང་གི་བདག་ཉིད་བཞིན་དུ་སྣ་ཚོགས་པའི་རྣམ་པར་དབྱེ་བ་སྐྱེ་བ་དང་གནས་པ་དང་འགག་པ་ལ་སོགས་པར་མི་འགྱུར་རོ། །

[Block 1152]
དེ་ལྟར་ཐ་དད་པ་མེད་པ་ཉེ་བར་མཚོན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1153]
ཐ་དད་པ་དང་ཐ་དད་པ་མེད་པའི་མཚན་ཉིད་འདི་ནི་རྣམ་པ་གཅིག་ལ་ཡང་ལྡོག་པ་དང་ལྡོག་པ་མེད་པ་ཡིན་ཏེ། བདག་ཉིད་གཅིག་ལ་འགལ་བ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 1154]
ཐ་དད་དེས་ཀྱང་དེ་ལྟར་མིན། །རྣམ་པ་ཐམས་ཅད་ཀྱི༌[^933]ཐ་དད་པ་མེད་པར་སྨྲ་བ་མ་ཡིན་ན་གང་གིས་དེ་ལྟར་འགྱུར། འདི་ནི་བདག་ཉིད་འགའ་ཞིག་ཀྱང་ཐ་དད་པ་མེད་པ་དང་ཐ་དད་པ་ཞེས་བྱ་བ་ཐ་དད་པའི་ཕྱིར་ལྷན་ཅིག་སྐྱེ་བ་ལ་སོགས་པ་མ་ཡིན་ནོ། །

[Block 1155]
དེ་ལྟར་ན་ནི།

[Block 1156]
[^934]གཅིག་གི༌[^935]འཇིག་ན་གནས་པ་ཡི། །བདག་ཉིད་གང་ཡིན་དེ་དེའི་མིན། །

[Block 1157]
གནས་པ་དང་གནས་པ་མ་ཡིན་པ་དག་ནི་རྟེན་གྱི་བདག་ཉིད་གཅིག་ཡིན་ན་ཐ་དད་པ་ཅན་གྱིས༌[^936]ཆོས་གཞན་ཅི་ཞིག་ཡོད། དེ་ལྟར་ན་འགའ་ཞིག་ཏུ་ཡང་སྣ་ཚོགས་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 1158]
དོན་དག་རྣམ་པ་ཐམས་ཅད་དུ་ཐ་དད་པའམ་ཐ་དད་པ་མེད་པ་ཉིད་དུ་ཁས་བླངས་པའི་ཕྱིར། མི༌[^937]འགའ་ཞིག་འདོད་པར་མི་འགྱུར་ཞིང་། དངོས་པོ་ཡང་མ་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1159]
དེ་བས་ན་འདི་ནི་གྲུབ་པ་དང་བདེ་བ་གཅིག་པ་མ་ཡིན་ཏེ། དངོས་པོ་ཐ་དད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1160]
དེས་སྤྱི་ཁྱད་པར་བློར་མི་འགྱུར། །དེ་བས་ན་དོན་གཞན་འདི་ནི་ལྟོས་པ་མེད་པ་ཡིན་ཏེ། མ་བསྐྱེད་པ་ཉིད་ཀྱི་ཕྱིར་འདིའི་སྤྱིའམ་ཁྱད་པར་ཅན་ཞེས་བྱ་བའི་སྒྲ་རིགས་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
