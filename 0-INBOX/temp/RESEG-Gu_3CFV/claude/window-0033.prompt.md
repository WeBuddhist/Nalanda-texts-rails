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
གླང་པོ་ཆེ་ལ་སོགས་པ་རྣམས་ལ་གོ་བསྐོན་པ་ཉིད་ནི་སྟ་གོན་བྱས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 1157]
ཤིང་རྟ་བཤམས་པ༌[^698]དང་རྒྱལ་མཚན་བསྒྲེང་བ་དང་། གཞུ་བདུངས་པ༌[^699]དང་། མདའ་མདའུ་ཅན་བདར་བ་དང་རལ་གྲི་ཕྱུང་བ་ཉིད་ལ་སོགས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1158]
གཉི་ག་ལ་ཡང་ཞེས་བྱ་བ་ནི་དངོས་གཞི་དང་སྦྱོར་བ་ལའོ། །

[Block 1159]
ཅི་འདིར་དངོས་གཞི་ལ་ཞེས་བྱ་བ་བདུན་ལྟུང་བའི་མཚན་མ་ཉིད་ཀྱིས་དངོས་གཞི་བརྗོད་པ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་རེག་པ་དང་བཤམ་པ་དཀྲུག་པ་དང་ལྟ་བའི༌[^700]ཕྱིར་འཕགས་ཤིང་ཉེ་འཁོར་གྱི་མཐའ་ལས་འདས་ཏེ་མཐོང་བ་ལྟ་བུ་ནི་དངོས་གཞི་དག་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རིན་པོ་ཆེ་སྨོས་པ་ཞེས་བྱ་བས་མཚོན་ཆ་ལ་རེག་པའི་ལྟུང་བ་གང་ཡིན་པ་དེ་ནི་འཆད་པར་འགྱུར་ཏེ། དེ་ལས་ཡུལ་གཞན་ཡིན་པ་དེ་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པར་བྱའོ། །

[Block 1160]
འདིར་བཤམས་པ༌[^701]ནི་གནས་ནས་འཕོ་བར་རྣམ་པར་གནས་པ༌[^702]ཡིན་ནོ། །

[Block 1161]
དཀྲུགས༌[^703]པས་ཞེས་བྱ་བ་ནི་ལྟ་བའི་དོན་དུ་དཀྲུགས་ནས་ཉེ་འཁོར་གྱི་མཐའ་ལས་འདས་པ་གང་ཡིན་པ་དེར་ལྟ་བའི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1162]
དགེ་སློང་གིས་གླང་པོ་ཆེ་གོ་བསྐོན་པ་བཤམ་པར་བྱེད་ཅེས་བྱ་བ་ནི་ཁ་ཅིག་གིས་གླང་པོ་ཆེ་དང་རྟ་དང་ཤིང་རྟ་དང་རྐང་ཐང་རྣམས་ལ་བཤམ་པ་ཐོབ་པར་བརྗོད་པ་ཡིན་ནོ། །

[Block 1163]
གཞན་དུ་ཡང་གླང་པོ་ཆེའི་ཚོགས་ལ་ལྟ་བའི་ཕྱིར་ཉེ་བར་འགྲོ་བར་བྱེད་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 1164]
དགེ་སློང་གིས་གླང་པོ་ཆེ་གོ་བསྐོན་པ་ལ་རེག་ན་ཞེས་བྱ་བ༌[^704]གསུངས་པ་ཡིན་ནོ། །

[Block 1165]
ལྟ་བ་དང་རེག་པ་དག་ལ་གཉི་ག་ལ་ཡང་སྦྱོར་བ་ཞེས་བྱ་བ་འདི་གཉིས༌[^705]བསྡུས་པའོ། །

[Block 1166]
མ་ཆས་པ་ཉིད་ལ་ནི་ན་སྨད་པ་ཉིད་དོ་ཞེས་བྱ་བའི་གཡུལ་ལ་མངོན་པར་དགའ་བ་ཉིད་མ་ཡིན་པ་ལའོ། །

[Block 1167]
དེ་བས་ན་འདིར་དམག་ལ་ཞེས་བྱ་བ་རྟོགས་པ་ཡིན་ནོ། །

[Block 1168]
བསླབ་པའི་གཞི་གསུམ་པོ་དག་ལས་གཡུལ་ངོའི་ཕྱིར་མ་ཆས་པ༌[^706]ཉིད་ལ་ནི་དམག་གི་དངོས་གཞིའི་གནས་སུ་ནི༌[^707]ཉེས་བྱས་ལ། ཉེས་བྱས་ཀྱི་གནས་སུ་ནི་ཉེས་བྱས་ཕྲ་མོར་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ལ་འདི་བྱེད་པའོ། །

[Block 1169]
རྒྱལ་པོ་འམ་ཆོམ་རྐུན་པའི་གྲོང་དུ་རྐྱེན་དེ་ལྟ་བུ་མ་གཏོགས་པར་འདིར་ཞུགས་པར་བྱ་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 1170]
མི་རུང་བ་དང་རྗེས་སུ་མི་མཐུན་པའི་རྒྱལ་པོའི་ནང་དུ་ཉེ་བར་འགྲོ་བའོ། །

[Block 1171]
སྤྱོད་ཡུལ་ནི་རྣམ་པ་ལྔ་སྟེ། འབྲོག་དང་ཇི་སྲིད་དུ་རྒྱལ་པོའི་ཉེ་འཁོར་ཞེས་བྱ་བ་འདི་ཡང་འདིར་ལུང་དུ་རིག་པར་བྱའོ། །

[Block 1172]
གླང་པོ་ཆེ་དང་རྟ་དང་བྱ་གག་དང་བྱ་ལ་བ་ཀ་དང་། བྱ་བར་ཏ་ཀ་དང་། སྐྱེས་པ་དང་བུད་མེད་འཐབ་པ་ལ་སོགས་པ་བྱ་བ་དང་། བྱེད་དུ་གཞུག་པ་དང་བལྟ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས་ལྷག་མ་དབང་དུ་བྱེད་པ་ནི་འདི་ཡིན་ཏེ། དེ་བས་ན་གཡུལ་ངོའི་ཡན་ལག་ཏུ་གྱུར་པ་གླང་པོ་ཆེ་ལ་སོགས་པ་རྣམས་ནི་འདིར་མི་གཟུང༌[^708]ངོ་། །དཔུང་གི་ཡན་ལག་ཉམས་སུ་མྱོང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1173]
ཅི་ཞིག་བྱས་ན་རྡེག་པའི༌[^709]ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རྙོག་པ་ཅན་གྱི་སེམས་ཉིད་ཀྱིས་དགེ་སློང་ཕ་རོལ་ལ་ལུས་སམ་དེས་འཕངས་པའམ་དེ་དང་འབྲེལ་པ་དག་གིས༌[^710]ཡང་རུང་བ་ཐ་ན་རྐང་པའི་མཐེ་བོའམ།[^711] ཡུངས་ཀར་རམ་རྩྭ༌[^712]དག་གིས་བརྡེགས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྙོག་པ་ཅན་གྱི༌[^713]སེམས་ཀྱིས་དགེ་སློང་ཕ་རོལ་ལ་ཞེས་བྱ་བ་ནི་ཕྱི་མ་གསུམ་པོ་རྣམས་ལའོ། །

[Block 1174]
རེག་ནའོ་ཞེས་བྱ་བ་ནི། བརྡེགས་ནའོ་ཞེས་བྱ་བ་རྗེས་སུ་བསྒྲུབ་པ་བཤད་པའོ། །

[Block 1175]
རེག་ནའོ་ཞེས་བྱ་བ་ནི་མཐར་ཐུག་པའི་ཚིག་གོ། །

[Block 1176]
རྗེས་སུ་བསྒྲུབ་པ་འདི་ལ་འདི་བསྒྲུབ་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1177]
འདིར་མངོན་པར་ཞེན་པ་དང་ཁྲོས་པ་དང་དྲག་པོར་གྱུར་པ་དང་ཡིད་མི་བདེ་བ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 1178]
ཉེ་བའི་ཉོན་མོངས་པ་གཞན་གྱིས་ཀྱང་སྦྱིན་པ་ལ་ཁ་ན་མ་ཐོ་བ་ཉམས་པས༌[^714]འདིར་བསྐྱེད་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1179]
དེ་བས་ན་རྙོག་པའི་དངོས་པོ་ལ་བརྟེན་པའོ། །གང་གིས་བརྡེགས་པ༌[^715]ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ལུས་སམ་དེས་འཕངས་པའམ་དེ་དང་འབྲེལ་པ་དག་གིས་སོ། །

[Block 1180]
ལུས་སམ་དེས་འཕངས་པའམ་དེ་དང་འབྲེལ་པ་དག་གིས་སོ༌[^716]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1181]
འདིར་འགའ་ཞིག་ཏུ་ནི་ཤིན་ཏུ་ཡང་མ་ཆད་པ་ལ་ན་སྨད་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུ་གསུངས་པ་ནི་གང་ཡང་རུང་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཐ་ན་རྐང་པའི་མཐེ་བོ་ལ་སོགས་པ་གྲངས་ཇི་ལྟ་བ་བཞིན་དུའོ། །

[Block 1182]
ལུས་ལ་སོགས་པ་རྣམས་ཀྱི་མཐར་ཐུག་པ་ལ་ཡང་དག་པར་རིག་པར་བྱའོ། །གང་ལ་བརྡེགས་པར༌[^717]ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟུང་བ་འབྱིན་པ་པོ་ཡང་དགེ་སློང་ཡིན་ཏེ། དེར་བདག་ཉིད་ལ་ཡང་བརྡེགས་པ་ལ་ཞེས་བྱ་བ་ཐོབ་པའོ། །

[Block 1183]
དེའི་ཕྱིར་གསུངས་པ་ནི་ཕ་རོལ་ལ་ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ནོ། །

[Block 1184]
འོག་མ་གསུམ་པ་ལ་ཡང་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པའི་གསུམ་ལ་བཟའ་བ་དང་། གནས་ངན་ལེན༌[^718]འཆབ་པ་དང་ཟན་གཅོད་དུ་འཇུག་པ༌[^719]ཞེས་བྱ་བ་བསླབ་པའི་གཞི་རྣམས་ལས་དགེ་སློང་ཕ་རོལ་པོ་ལ་ཡང་འདི་བལྟ་བར་བྱའོ། །

[Block 1185]
ཅི༌[^720]བརྡེག་པ་ཡོད་པ་ལ་གཞན་དེའི་འབྲས་བུར་གྱུར་པ་སྒྲུབ་པ༌[^721]ལ་ཡིན་ནམ་འོན་ཏེ་བརྡེགས་པ་ཁོ་ན་ལ་ཡིན་ཞེ་ན། [^722]དེའི་ཕྱིར་རེག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བརྡེག་པའི་བདག་ཉིད་ཅན་གྱི་རྗེས་སུ་བསྒྲུབ་པ་ཡོད་པ་ལ་རེག་པ་བསྒྲུབ་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་ལྟུང་བྱེད་གཅིག་ཏུ་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་བརྡེག་སྤྱད་རེ་རེ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོར་མོ་ལ་སོགས་པའི་བརྡེག་སྤྱད་ཇི་སྙེད་ཀྱིས་རེག་པར་གྱུར་པ་དེ་སྙེད་ཀྱི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1186]
མ་ཕོག་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་སོར་མོ་ལ་སོགས་པ་བརྡེག་སྤྱད་དག་གིས་མ་ཕོག་ན་ཉེས་བྱས་སོ། །

[Block 1187]
བརྡེག་པར་བྱ་བ་གཞན་ཡིན་ལ། གཞན་ལ་བརྡེག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སེམས་བརྡེག་པར་བྱ་བ་ཉིད་ལ་རང་གི༌[^723]ལུས་ལ་བརྡེག་པ་འདི་བཀག་པའོ། །

[Block 1188]
འདིར་གཞུང་ནི་དེ་ལྟ་བས་ན་དགེ་སློང་གིས་བརྡེག་པར་བྱ་བ་གཞན་ཡིན་ལ། གཞན་ལ་བརྡེག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1189]
ཀ་བ་ལ་བརྡེག་པར་མི་བྱའོ། །

[Block 1190]
རྩིག་པ་དང་། ས་དང་ཤིང་ལྗོན་པ་དང་གཞན་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཕྲན་ཚེགས་རྣམས་ལ་འབྲས་བུ་ལ་སོགས་པ་དེ་དབབ་པའི་དོན་དུ་འདིར་བརྡེག་པ་སྟེར་བ་ལ་སོགས་པ་འབྱུང་པོའི་ཚོགས་འཇིག་པའི་ཆོ་ག་ལ་དེ་ཁོངས་སུ་འདུས་པ་ཞེས་བྱ་བ་གཞན་འགོག་པ་ནི་འདིའི་ཡུལ་ལོ། །

[Block 1191]
བུད་ཤིང་གི་དོན་དུ་ཤིང་ལྗོན་པ་དང་། མཎྜལ་གྱི་དོན་དུ་ས་བརྡུང་བ་ལ༌[^724]སོགས་པ་འདི་ལྟ་བུ་ལ་ཡང་། ཅི་འདིས་བཀག་པ་ཉིད་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ་ཞེས་བསྟན་པ་ནི་བརྡེག་པ་སྟེར་བའི་སྦོམ་པོ་ལ་འཇུག་པ་ལ་འདི་བཀག་པ་ཡིན་གྱི་གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1192]
དེ་ལྟར་ཡང་ཚེ་དང་ལྡན་པས་རི་ཤིང་གཤེགས་པ་འཇུག་པ༌[^725]འབྱུང་བར་འགྱུར་རོ། །

[Block 1193]
བརྡེག་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1194]
གང་དུ་གཟས་པའི་ལྟུང་བྱེད་ཅེས་བྱ་བ་འདི་ལ་རྙོག་པ་ཅན་གྱི་སེམས་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་ནས་གཟས་པ་ནའོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་མཐའ་མ་ལ་ལྟོས་ནས་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་བརྡེག་པར་གཟས་པ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་འདིར་གཅིག་ཉིད་དུ་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་རྫས་རེ༌[^726]རེ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོར་མོ་ལ་སོགས་པའི་རྫས་ཇི་སྙེད་གཟས་པ་དེ་སྙེད༌[^727]ཀྱི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1195]
གཟས་པའི་ལྟུང་བྱེད་དོ།། །།
--- END BLOCKS ---
