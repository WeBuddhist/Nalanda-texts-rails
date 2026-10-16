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
འདིས་ནི་ཡོངས་སུ་བཅོམ་པས་ཕོངས་པ༌[^666]ཉིད་དུ་བསྟན་ཏོ། །

[Block 1157]
དེ་ལྟར་ཕོངས་པ་ལ་ནོར་གྱི་སེར་སྣའི་ཡ་རབས་སུ་ཞིག་བསྟན་པར༌[^667]བྱེད་དེ་ནོར་སྦྱིན་པ་ཉིད་ལ་སུ་ཞིག་འདི་ལྟར་སེར་སྣ་བྱེད་པའོ། །

[Block 1158]
ད་ནི་དེའི་རྒྱུ་བསྟན་པའི་ལམ་ལས་བརྩམས་ཏེ། བརྒྱ་བྱིན་ཁྱོད་ཀྱིས་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདིའོ། །

[Block 1159]
གཉེན་པ་ནི་བདག་ཉིད་ཀྱི་ཉེ་དུ་ལྟ་བུ་སྟེ། ཅིའི་ཕྱིར་ན་ཕན་པ་སྨྲས་པས་སོ། །

[Block 1160]
དེ་བས་ལམ་མིན་ཞེས་བྱ་བ་ལ། སྦྱིན་པའི་ལམ་མ་ཡིན་པ་ནི་སྦྱིན་པ་མ་ཡིན་པ་སྟེ། སྨྲས་པ་ཕན་པ་མ་ཡིན་པ་བསྟན་ཅིང་བསྒྲུབས་པས་ནི་ཁྲོ་བ་ཡོངས་སུ་འཛིན་པའི་ཕྱིར། ཁྱོད་ཀྱི་ཐུགས་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 1161]
མཐུན་པའི་ཕྱོགས་ཉིད་བགྲོད་པར་དཀའ་བའོ། །

[Block 1162]
ངོ་བོ་ཉིད་ཀྱི༌[^668]སྦྱིན་པ་ནི་ངོ་བོ་ཉིད་ཀྱིས་སྦྱིན་པའོ། །

[Block 1163]
ངོ་བོ་ཉིད་ཀྱི༌[^669]སྦྱིན་པའི་མི་མཐུན་པའི་ཕྱོགས་ནི་སྦྱིན་པ་མ་ཡིན་པ་ངོ་བོ་ཉིད་ཀྱིས་མི་མཐུན་པའོ། །

[Block 1164]
བགྲོད་དཀའ་བ་ནི་སྡུག་བསྔལ་གྱིས༌[^670]བགྲོད་དཀའ་བའི་ཕྱིར་རོ། །

[Block 1165]
གཞུག་པ་ནི་འགྲོ་བའོ། །

[Block 1166]
སླ་བ་ཞེས་བྱ་བ་ནི་འབད་པ་ཆུང་ངུས་སོ། །

[Block 1167]
འབྱོར་པ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་ནི༌[^671]གོས་དང་། རྒྱན་དང་། ཡོ་བྱད་དང་། མལ་ཆ་ལ་སོགས་པ་གཟུང༌[^672]ངོ་། །བང་མཛོད་ཡོངས་སུ་གང་བ་དང་ཞེས་བྱ་བ་འདི་གཉིས་ཀྱིས་ནི་གང་སོགས་ཤིང་འདུ༌[^673]བ་དེ་བསྟན་ཏོ། །

[Block 1168]
གང་སོགས་པ་དེའི་དབང་དུ་བྱས་ནས། ལེགས་པར་བྱེད་ཅིང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ལེགས་པར་བྱེད་པ་ནི་ཇི་ལྟར་བྱ་བ་དེ་བཞིན་དུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1169]
རླབས་ཆེ་བཾ་ནི་རེ་རེ་ལ་ཡང་ལས་ཀྱི་མཐའ་མང་པོ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1170]
རྣམ་པ་སྣ་ཚོགས་པ་ནི་ཞིང་རྨེད་པ་དང་ཚོང་ལ་སོགས་པ་སྟེ། ཞིང་གི་རྣམས་ནི་སྣ་ཚོགས་པས་སོ། །

[Block 1171]
དར་བར་གྱུར་པ་ཞེས་བྱ་བ་ནི་བརྟན་པ་དང་གནས་པར་གྱུར་པ་སྟེ། གནས་པར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་འཇིག་རྟེན་ན་དར༌[^674]བར་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཡིན་ཏེ། འཇིག་རྟེན་དབང་ཕྱུག་དབང་དུ་གྱུར་པ་ཞེས་བྱ་བ་ནི་གང་གིས་འཇིག་རྟེན་གྱི་དབང་ཕྱུག་གི༌[^675]དབང་དུ་གྱུར་པ་སྟེ། སེམས་ཅན་འཇིག་རྟེན་པ་རྣམས་བཀའ་བཞིན་དུ་བྱེད་པར་བསྟན་ཏོ། །

[Block 1172]
བདག་གི་བློ་ཡིས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ། རང་གི་བློས༌[^676]ལྕོགས་པ་ནི་བདག་གི་བློས༌[^677]ལྕོགས་པའོ། །

[Block 1173]
དེས་མཉམ་པར་གཞག་པ༌[^678]ནི་མ་ཡེངས༌[^679]པའམ། ཡང་དག་པར་ཁྱབ་པར་བྱས་པའོ། །

[Block 1174]
ལས་དང་ཡོན་ཏན་གྱི་དབང་དུ་བྱས་པ་སྟེ། དེ་ཡང་གྲགས་པའི་རྗེས་སུ་མཐུན་པར་འགྱུར་བའི་འཇིག་རྟེན་པས་རབ་ཏུ་བསྔགས་པ་ནི་རིགས་མཐོ་བའམ་གྲགས་པ་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 1175]
དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། ལས་དང་རིགས་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 1176]
འགྲན་ཟླ་ཟིལ་མནན་ཏེ་ཞེས་བྱ་བ་ནི་དགྲའི་ཕྱོགས་ལས་བརྩམས་པའོ། །

[Block 1177]
སྐྱེ་བོ་རྣམས་ནི་ཞར་ལ་གྲོགས་བཙལ་ནས། །ཞེས་བྱ་བ་ནི་ཐ་མལ་པ་རྣམས་ལས་བརྩམས་པའོ། །

[Block 1178]
ཞར་ལ་ཞེས་བྱ་བ་ནི་ཕན་ཚུན་འདུད་ཅིང་ཕྱག་འཚལ་བའོ། །

[Block 1179]
མཛའ་བོར་བཅས་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^680]ནི་གྲོགས་པོའི་ཕྱོགས་ལས་བརྩམས་པའོ། །

[Block 1180]
རྒྱལ་པོ་ལས་ཀྱང་ཞེས་བྱ་བ་ནི་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་རྒྱུ་ཉིད་དུ་བསྟན་ཏེ། དེས་ཡོངས་སུ་བསྲུང་བའི་ཕྱིར་རོ། །

[Block 1181]
དཔལ་གྱིས་འཁྱུད་གྱུར་ན་ཞེས་བྱ་བ་ཡིན་ཏེ། འདི་ལྟར་ཡོངས་སུ་གཏོང་བ་ཅན་ནི་འབྱོར་པ་དང་བདེ་བ་ཡིན་ཏེ། འདི་ནི་ཉེ་བར་ལོངས་སྤྱོད་པའོ། །

[Block 1182]
སྡོམ་ཞིང་མི་གཡེང་གནས་པ་ཞེས་བྱ་བ་ལ་སྡོམ་པ་ནི་སྦྱིན་པ་ལས་ལྡོག་པའོ། །

[Block 1183]
མི་གཡེང་བ་ནི་ཉེ་བར་ལོངས་སྤྱོད་པ་ལས་ལྡོག་པའོ། །

[Block 1184]
ཡང་ན་མི་གཡེང་བ་ནི་རྒྱལ་པོ་ལ་སོགས་པའི་ཆད་པའི་ལས་ཀྱིས་སོ། །

[Block 1185]
དེ་ལ་མ་རབས་འགྱུར་བ་ཞེས་བྱ་བ་ནི་གང་དེ་ལྟར་བསྟན་པ་སྟེ། འཕགས་པས་མ་རབས་ཆོས་བྱ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེའི་ལན་གྱིས་བསྟན་པ་ཡིན་ནོ། །

[Block 1186]
འབྱོར་པ་མེད་པར་ཞེས་བྱ་བ་ལ། འབྱོར་པ་མེད་བཞིན་དུ་སྟེ། བདག་གི༌[^681]དོན་ཞེས་བྱ་བ་ལས་བརྩམས་པའོ། །

[Block 1187]
གང་ཞིག་ཅེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་གཉིས་བསྟན་པ་ལས་འཇིག་རྟེན་པ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 1188]
གཞན་གྱི་དོན་ལས་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདི་ནི་འཇིག་རྟེན་པའི་དབང་དུ་བྱས་པ་སྟེ། བདག་གི་དོན་ཆེད་ཆེར་འཛིན་པའོ། །

[Block 1189]
གཞན་གྱི་དོན་ཆེད་ཆེར་མི་འཛིན་པ་དེས་ཀྱང་སྦྱིན་དགོས་པ་ཡིན་ཏེ། དེ་ཅིའི་ཕྱིར་ཞེ་ན། འདིས་ནི་ལོངས་སྤྱོད་ཆོག་པ་མེད་པས་སོ། །

[Block 1190]
དེས་ནི་མཐོང་བའི་ཆོས་ཀྱིས་བདེ་བ་བསྟན་ནས་མཐོ་རིས་ཐོབ་མི་འགྱུར་ཞེས་བྱ་བ་ནི༌[^682]འཇིག་རྟེན་ཕ་རོལ་གྱི་བདེ་བའོ། །

[Block 1191]
ཅིའི་ཕྱིར་མཐོང་བའི༌[^683]ཆོས་ཉིད་ལ་བསོད་ནམས་སུ་མི་འགྱུར་ཞེ་ན། སྦྱིན་པའི་འབྲས་བུ་ནི་འབྱོར་པ་ཡིན་པས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1192]
སེར་སྣ་ལ་སོགས་ཞེས་བྱ་བ་འདིའི་དོན་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་དབང་དུ་བྱས་པ་སྟེ། གང་གི་ཕྱིར་དེ་ནི་ཉོན་མོངས་པ༌[^684]སྤོང་བ་ལ༌[^685]འབད་པས་སོ། །

[Block 1193]
འབྱོར་པ་དེའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཕུན་སུམ་ཚོགས་པའི་རྒྱུའི་ཕྱིར་རོ། །

[Block 1194]
གང་ཞིག་སྐྱེ་ཤིས་ཉེན་པའི་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདིས་ནི་བྱང་ཆུབ་སེམས་དཔའི་དབང་དུ་བྱས་པ་སྟེ་རྒ་བ་དང་ཤི་བ་ཞེས་བྱ་བ་ལ། གཉིས་ཁོ་ན་སྨོས་པས་ནི་ནད་ནི་ངེས་པར་འབྱུང་བའི་ཕྱིར་ལ། སྐྱེ་བ་ནི་མ་བཤད་ཀྱང་གྲུབ་པའི་ཕྱིར་འདི་ལྟར་བསྟན་ཏོ། །

[Block 1195]
བདག་ཀྱང་གཏོང་བྱེད་ཅིང་ཞེས་བྱ་བ་འདིས་ནི་སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་ལ་འཇུག་པའི་མཚན་ཉིད་བསྟན་ཏོ། །
--- END BLOCKS ---
