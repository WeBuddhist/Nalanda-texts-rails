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
འདི་དག་ལམ་དུ་སོང་བས་ཀྱང་རྗེས་སུ་ཁུར་བ་ཡང་རིགས་སོ། །

[Block 1122]
འདི་གཉིས་ལ་ཡང་མཚོན་པར་བྱེད་པའི་རྟགས་འདིར་ཡང་ཡོད་དེ། དེའི་ཕྱིར་འདིར་གཞུང་ནི་བསོད་སྙོམས་པ་ཞིག་མཉན་ཡོད་དུ་བསོད་སྙོམས་ལ་ཞུགས་པ་ན། དེར་མཆིལ་ལྷམ་མེད་པས་རྐང་པ་དག་ལ་སེར་ཁ་བྱུང་བ་ཁྱིམ་བདག་གིས་མཐོང་ནས་དེས་དེ་ལ་སྨྲས་པ། འཕགས་པ་ཁྱོད་ལ་མཆིལ་ལྷམ་དག་མེད་དམ། མེད་དོ། །

[Block 1123]
ཚུར་ཤེག༌[^944]དང་སྦྱིན་དུ་གཞུག༌[^945]གོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 1124]
ཅི་ཡང་རུང་བའི་མཆིལ་ལྷམ་གནས་མལ་བསྐྱང་བའི་དོན་དུ་མཐའ་ཁོབ༌[^946]དག་ཏུ་བཅང་བར་བྱ་བའམ་ཞེ་ན། དེའི་ཕྱིར་ཆིག་རིམ་མོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆིག་རིམ་གང་ལ་ཡོད་པ་དེ་ནི་ཆིག་རིམ་གཅིག་པའོ། །

[Block 1125]
དེ་ཡང་འདིར་མཐིལ་ཆིག་པའི༌[^947]རིམ་ཅན༌[^948]ནམ་རིམ་པ་གཅིག༌[^949]ལ་གནས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1126]
སྡོགས་པ༌[^950]གཞུག་པས་བཅོས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཟད་པ་ཉིད་ལ་ནི་རིམ་པ་གཞན་སྡོགས་པ༌[^951]གཞུག་པར་འོས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་སུ་ཞིག་སྡོགས་པ༌[^952]གང་ཞིག་གིས་བྱས་པ་དེ་སློབ་མའི་དོན་དུ་ངེས་པ་འདིར༌[^953]རིག་པར་བྱའོ། །

[Block 1127]
དེའི་དོན་དུ་གསལ་བར་བྱ་བའི་ཕྱིར་བརྗོད་པར་བྱ་སྟེ། རིམ་པ་གཞན་ནི་མི་རུང་ངོ་ཞེས་བྱ་བ་ནི་སྡོགས་པ༌[^954]རིམ་པ་གཞན་གཞུག་པས་བཅོས་པར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1128]
འདིར་གཞུང་ནི། གལ་ཏེ་རྡོལ་ན་སྡོགས་པ༌[^955]བཅུག༌[^956]སྟེ་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1129]
རྡོལ་ན་ཞེས་བྱ་བ་ནི༌[^957]བུ་གུ༌[^958]བྱུང་ནའོ། །

[Block 1130]
ཁྱིམ་པས་ཐ༌[^959]ན་གོམ་པ་བདུན༌[^960]དུ་བགོས་ན་རིམ་པ་མང་ཡང་རུང་ངོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། ཉེ་བ༌[^961]འཁོར་ཁྱིམ་པས་ཐ་ན་གོམ་པ་བདུན་བགོས་པར་གྱུར་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1131]
རུང་བ་ཙམ་གྱི་དོན་ཉིད་དུ་དེ་དང་སྦྱར་བའི་དབང་དུ་ལེན་པ་ནི། མི་རུང་བ་བླངས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། མི་རུང་བ་ཞེས་བྱ་བ་ནི་བླངས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱོར༌[^962]རོ། །

[Block 1132]
གང་ཞིག་རིམ་པ་གཅིག་པ་བྱ་སྟེ་བཅང་བར་བྱའོ༌[^963]ཞེས་བྱ་བ་ནི་རིམ་པ་དག་ལ་དགེ་སློང་གིས་བདག་ཏུ་བྱས་པ་དེའི་འདི༌[^964]བསྡུས་པའོ། །

[Block 1133]
རུང་བ་ཙམ་གྱིས་དོན་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དེར་རུང་བ་དང་ཇི་སྙེད་པར་གྱུར་པ་དེ་ཙམ་གྱིས་དོན་ཉིད་ཡོད་པ་དང་། མེད་པ་དང་ལྷག་པར་གྱུར་པ་དང་མི་རུང་བའི་བསྩགས་པར༌[^965]གྱུར་པ་དོགས་པ༌[^966]ལ་དེའི་སྦྱོར་བའི་དབང་གིས་རུང་བ་དང་འབྲེལ་བ་འབྱོར་བ་བླངས་པ་སྟེ། རུང་བ་མ་ཡིན་པའི་དངོས་པོ་ལ་བདག་གིར༌[^967]བྱ་བ་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1134]
ཁྲ་བོ་བཀྲ་བ་དག་མི་བཅང་ངོ་ཞེས་བྱ་བ་ནི་འདི་མན་ཆད་ནས་འོག་གི༌[^968]མདོ་ལས་སྒེག་རྫས་སུ་གྱུར་པ་གཞན་དག་ཀྱང་ངོ་ཞེས་འབྱུང་བ་ཡན་ཆད་མཆིལ་ལྷམ་དག་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 1135]
ལུག་རུ་ལྟ་བུ་དག་བཅང་བར་མི་བྱའོ། །

[Block 1136]
ཨ་ཤྭད་ཐ༌[^969]དང་ཀ་ར་བཱི་རའི་འདབ་མ་ལྟ་བུ་དག་མི་བཅང་ངོ་། །གསེར་དང་དངུལ་གྱིས་སྤྲས་པ་དག་མི་བཅང་ངོ་། །ཐྲིག་ཐྲིག༌[^970]ཟེར་བ་དག་མི་བཅང་ངོ་། །ཀྲོག་ཀྲོག་ཟེར་བ་དག་མི་བཅང་ངོ་། །ཏུག་ཏུག་ཟེར་བ་དག་མི་བཅང་ངོ་། །ཐྲིག་ཐྲིག་ཟེར་བ་དག་མི་བཅང་ངོ་ཞེས་བྱ་བ་ནི་ཐྲིག་ཐྲིག༌[^971]ཟེར་བ་དག་མི་བཅང་ངོ་། །ཀྲོག་ཀྲོག་ཟེར་བ་དག་མི་བཅང་ངོ་ཞེས་བྱ་བའི་ཚིག་གཉིས་སོ། །

[Block 1137]
དེ་ལས་གཞན་པའི་ཏུག་ཏུག་ཟེར་བ་དག་མི་བཅང་ངོ་། །ཐྲིག་ཐྲིག་ཟེར་བ་དག་མི་བཅང་ངོ་ཞེས་བྱ་བའི་ཚིག་གཉིས་བསྡུ་བར་བྱས་སོ། །

[Block 1138]
དེ་ལ་སྒེག་རྫས་ཐམས་ཅད་བཀག་པའི་གཙོ་བོ་ཉིད་འདིར་རྣམ་པར་གནས་པ་ཡིན་ཏེ། དེ་བས་ན་གཉིས་ཀ༌[^972]བསྡུས་པའོ། །

[Block 1139]
སྒེག་རྫས་སུ་འགྱུར་བ༌[^973]གཞན་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་སྒེག་རྫས་ཐམས་ཅད་དགག་པའི་གཙོ་བོ་ཉིད་དུ་འདིར་རྣམ་པར་གནས་པ་དེ་བས་ན་མདོ་འདི་ཡིན་ནོ། །

[Block 1140]
བོལ་ཀོ་བ་ཅན་ནི་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ནི་སྒེག་རྫས་སུ་གཏོགས་པ་མ་ཡིན་པར་ཤེས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1141]
སྣ་དང་རྟིང་པའི་སྦུབས་ཅན་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མཆིལ་ལྷམ་སྣའི་སྦུབས་ཅན་ཞེས་བྱ་བ་ནི་རྐང་པའི་སྣའི་སྦུབས་ཅན་ནོ། །

[Block 1142]
རྟིང་པ༌[^974]ནི་རྟིང་པའོ། །

[Block 1143]
འདིར་གཞུང་ནི། དགེ་སློང་རྣམས་བྱ་རྒོད་ཕུང་པོའི་རི་ལ་འཛེགས་པ༌[^975]ན་རྐང་པའི་སྣ་དག་དྲུད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ནས། [^976]སྣ་སྦུབས་ཅན་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་དང་། འབབས་པ་ན༌[^977]རྟིང་པ་དག་དྲུད་ནས་རྟིང་པ་སྦུབས་ཅན་བཅང་བར་བྱའོ་ཞེས༌[^978]གསུངས་པ་ཡིན་ནོ། །

[Block 1144]
ཁ་ཆུ་ཆུས་བྱུང་ངོ་ཞེས་བྱ་བ་ནི་ཕལ་ཆེར་ཐམས་ཅད་རྐང་པ་འགེབས་པར༌[^979]བྱེད་པ་མཆིལ་ལྷམ་འདི་བཅང་བར་རིག་པར་བྱའོ། །

[Block 1145]
ལྷམ་ཡུ་ཆད་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་བཅང་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1146]
ལྷམ་ཡུ་ཆད་ཀྱང་ལས་ལྷམ་གྱི༌[^980]རྣམ་པ་གཞན་འབྱུང་བ་ཡོད་པ་ཡིན་ཏེ། དེ་བས་ན་མཆིལ་ལྷམ་དང་ཁ་ཆུ་ཆུས་བྱུང་ངོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 1147]
འདིར་གཞུང་ནི། གང་གི་ཚེ་ཀླུའི་རྒྱལ་པོ་སོག་མ་མེད་ཀྱིས་སེར་བ་དང་བ༌[^981]པའི་ཚེ། །ཐོག་གི་ཆར་རྣམས་འབབ་པ་དེའི་ཚེ་རྩ་སྣ་རྣམས་ཀྱང་དུག་དང་བཅས་པ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1148]
དེར་དགེ་སློང་རྣམས་འཆག་པར་བྱ་བའི་དགེ་སློང་རྣམས་ལ་རྨ་བྱུང་བར་གྱུར་པ་དང་འགྲོ་མ་ཤེས་པར་གྱུར་ཏེ། [^982]བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ།[^983] ཁ་ཆུ་ཆུས་བྱུང་བཅང་བར་བྱའོ། །

[Block 1149]
ལྷམ་ཡུ་ཆད་ཀྱང་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་དང་། མཆིལ་ལྷམ་ཉིད་འདི་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བྱང་ཕྱོགས་སུ་འདི་ལྟ་བུས་གྲགས་པའོ། །

[Block 1150]
འདིར་ཁ་ཅིག༌[^984]མཆིལ་ལྷམ་གྱི་ཚིག་བྱེད་བཞིན་པ་ཁ་ཆུ༌[^985]ཆུས་བྱུང་བ་དང་མཆིལ་ལྷམ་བཅང་བར་བྱ༌[^986]ཞེས་བྱ་བ་དེ་ཀླུའི་ཁ་ཆུའི་ཆུ་ལས་བྱུང་བ༌[^987]རྒྱུ་མཚན་ལས་སྐྱེས་པ་ཉིད་ཀྱི་ཕྱིར་དང་དེ་ལས་སྐྱེས་པའི་ཕྱིར་དང་འཇིག་རྟེན་པས་བསྐྱེད་པའི་ཕྱིར་ཞེས་བྱ་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 1151]
རྣམ་པ་གཞན་བསྟན་པར་བྱས་པར་གྱུར་ཅིག་ཅེས༌[^988]བྱ་བ་ལྷམ་ཡུ་ཆད་རྗེས་སུ་གནང་བའོ། །

[Block 1152]
འདིར་དོན་ཐ་དད་པ་ཡང་ཡོད་དེ་རྣམ་པ་གཞན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1153]
སུ་ཞིག་ལ་ཅུང་ཟད་བདེ་བ་བྱེད་པ་ཞེས་བྱ་བ་འདི༌[^989]ཡང་འདིར་རྗེས་སུ་གནང་བའི་དོན་ཏོ། །

[Block 1154]
ཆུ་ལ་ཆབ་རོམ་འཆགས་པའི་ཡུལ་དུ་ནི་ཞྭ་དང་ལྷམ་སྒྲོག་གུ་ཅན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡུལ་གང་དུ་ཆུ་ལ་ཆབ་རོམ་འཆགས་པའི་ཆུ་ཡུལ་གང་ན་ཡོད་པ་དེ་ལ་ནི་འདི་དག་བཅང་བར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1155]
དོན་འདི་ལ་མངོན་པར་བརྟེན་པ་ཡང་གཞན་ཡང་མེད་པའི་ཕྱིར་དང་འདིར་ལྷག་པའི་རིགས་པའི་ངོ་བོ་མེད་པའི་ཕྱིར་རིགས་པའི་ངོ་བོའི་དོན་ལ་དྲང་བ་བསྐྱབ་པའི་དོན་དུ་ཤེས་པར་བྱའོ། །

[Block 1156]
དུས་གཞན་གྱི་ཚེ་ན་འབབ་པ་གཞན་སྦྱིན་པའི་ཕྱིར་དང་འབབ་པ་ལྷགས་པ༌[^990]དང་བྲལ་ན་དབྱར་གྱི་གོས་རས་ཆེན་བཞིན་དུ་ཞེས་བྱ་བ་འདི་ལྟ་བུ་ཆུ་མེད་པའི་ཕྱིར་གཞག་པར་བྱའོ། །

[Block 1157]
ནད༌[^991]གསོ་བའི་དོན་དུ་ནི་འདི་དག་ནི་ཉེ་བར་དགོས་པའོ། །

[Block 1158]
བཅས་པའི་ཁ་ན་མ་ཐོ་བ་ཐམས་ཅད་རྗེས་སུ་གནང་བས་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 1159]
བླ་མའི་དྲུང་དུ་མཆིལ་ལྷམ་བགོ་བ་བསྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་ཉིད་ཀྱི་སྤྱན་སྔར་མཆིལ་ལྷམ་གྱོན་ཞིང་འཆག་པའི༌[^992]དགེ་སློང་སྨད་པ་ན་དགེ་སློང་དག་ལ་ཡང་ཚུལ་དེ་ཉིད་སྨད་པ་ཡིན་པས་དེའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 1160]
སེང་གེ་དང་སྟག་དང་གུང་དང་། གླང་པོ་ཆེ་ཅང་ཤེས་དང་རྟ་ཅང་ཤེས་ཀྱི་ཡན་ལག་ཅུང་ཟད་ཀྱང༌[^993]ལུས་ལ་གདགས་པར་མི་བྱ་བ་ཉིད་དེ༌[^994]ཞེས་བྱ་བ་ལ་ཅུང་ཟད་ཀྱང་ཞེས་བྱ་བ་ཡང་འདིར་གཞུང་ནི། ཕྲན་ཚེགས་དག་ལས་སེང་གེ་དང་དེ་ལས་གཞན་པའི་རི་དྭགས་གཏུམ་པོ་རྣམས་ལ་ཡང་འདིར་བསྙེགས་པའོ། །
--- END BLOCKS ---
