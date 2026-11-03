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
[Block 4131]
གཞན་གྱིས༌[^2865]ཚེས་བཅོ་ལྔ་ལ་དགེ་སློང་བཟུང་ན་དེ་ལ་དགེ་འདུན་གྱིས་འདི་བདག་ཅག་གི་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་ཡིན་གྱི་ཐོང་ཤིག༌[^2866]ཅེས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། གཞན་གྱིས་ཞེས་བྱ་བ་ནི། རྒྱལ་པོ་ལ་སོགས་པའོ། །

[Block 4132]
དེ་ལ་ཞེས་བྱ་བ་ནི་གཞན་ལ་བརྗོད་པར་བྱའོ། །

[Block 4133]
གང་གིས་དགེ་སློང་བཟུང་བར་གྱུར་པ་དེ་ལ་མངོན་སུམ་དུའམ་འཕྲིན་པ་བཏང་སྟེ། དེར་རང་གིས་སམ་ཐམས་ཅད་ཀྱིས་མ་བཏང་བ་དང་མ་བཏང་བར་འགྱུར་བ་མ་ཡིན་ཏེ། ཕོ་ཉའི་ཁ་ནས༌[^2867]སྨྲ་བ་གང་ཡིན་པ་དང་། རང་གིས༌[^2868]ཁ་ནས་སྨྲ་བ་གང་ཡིན་པ་འདི་གཉིས་ཀའི་བསྡུ་བ་ལ་དགོངས་ནས། དེ་ལྟར༌[^2869]ཉེ་བར་བཏགས་པའོ། །

[Block 4134]
མ་བཏང་ན་བདག་ཅག་འདི་དང་ལྷན་ཅིག་བྱ་བ་ཅུང་ཞིག་ཡོད་དོ་ཞེས་སྔ་མ་དང་བཅས་ཏེའོ་ཞེས་བྱ་བ་ལ། སྔ་མ་དང་བཅས་ཏེ་ཞེས་བྱ་བ་ནི་མདོ་སྔ་མ་དེས། ཐོང་ཤིག༌[^2870]ཅེས་སྨོས་པའི་ཚིག་སྔ་མ་དེ་དག༌[^2871]དང་བཅས་ཏེ། བདག་ཅག་དགེ་སློང་འདི་དང་ལྷན་ཅིག་བྱ་བ་ཅུང་ཟད་ཅིག་ཡོད་དོ་ཞེས་བྱ་བ་འདི་ལྟར་གཞན་ལ་བརྗོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4135]
དེ་ལྟ་ན་ཡང་དཀྱིལ་འཁོར་པར་བྱའོ་ཞེས་བྱ་བ་ནི། ཚིག་གཉིས་པ་བརྗོད་ཀྱང་མ་བཏང་ན་དེའི་ཚེ་དགེ་འདུན་གྱིས་དཀྱིལ་འཁོར་དུ་གསོ་སྦྱོང་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4136]
དེ་བཏང་བའི་ཕྱིར་སྔར་མི་འབད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི།[^2872] གཞན་གྱིས་བཟུང་བའི་དགེ་སློང་དེ་བཏང་བའི་ཕྱིར་རོ། །

[Block 4137]
འཕྲིགས་པས། མི་མཐུན་པ་ཉིད་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། མཚམས་ཀྱི་ནང་ན་དགེ་སློང་དངོས་སུ་འཁོད་པར་ཤེས་པ་རྣམས་ཀྱི་ངེས་པ་རྣམས་ཁོ་ནས་དགེ་སློང་རྣམས་ཡོད་ན། གང་ཞིག་མ་འོངས་པ་ཞེས་པ་ལས་མི་མཐུན་པ་ཉིད་ཀྱིས་ཉེས་པར་འགྱུར་བ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི། འདི་ལྟར་མཐོང་ངམ་ཐོས་པས་མི་མཐུན་པ༌[^2873]ཉིད་ཀྱིས་ཉེས་པར་འགྱུར་བ་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 4138]
ཐ་དད་པ་ཉིད་དུ་འདོད་པས་མངོན་པར་བརྟགས་ཏེ་ལས་བྱེད་ན་ཉེས་པ་སྦོམ་པོའོ་ཞེས་བྱ་བ་ལ། ཐ་དད་པ་ཉིད་དུ་འདོད་པས་ཞེས་བྱ་བ་ནི། ངེས་པའམ་འཕྲིགས་པ་མ་ལྷགས་པ་རྣམས་ཐ་དད་པ་ཉིད་དུ་འདོད་པས་མ་འོངས་ཀྱང་སླའོ་སྙམ་དུ་སེམས་ཤིང་དེ་བས་ན་ཐག་རིང་པོ་ན་འཁོད་ཅིག༌[^2874]སྙམ་པའོ། །

[Block 4139]
འདིར་ལས་ཞེས་སྨོས་པའི་འདུག་པར༌[^2875]གཏོགས་པ་དང་རྗེས་སུ་མཐུན་པའི་ལས་སུ་བྱ་བ་ལ། ཚོགས་པའི་ཡན་ལག་མ་ཡིན་པ་དེ་ཡོངས་སུ་བཅད་པའི་དོན་དུ༌[^2876]ཚིག་འདིའོ། །

[Block 4140]
འདི་ནི་དགེ་འདུན་གྱི་དབྱེན་ལ་འདུ་བའི་སྐབས་སུ་དགེ་འདུན་ལྷག་མ་གང་ཡིན་པ་དེའི་སྐབས་སུ་གཏོགས་པའི་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 4141]
རྟོག་པ་ཉིད་ན་ཐེ་ཚོམ་ཟ་འམ་ངེས་པར་འབྱེད་པ་ལ་ནི་ཉེས་པའི་བྱེད་པ༌[^2877]མི་འབྱུང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ལྟར་ཡང་འདིར་གཞུང་ནི། ཅི་གང་དག་མ་ལྷགས་པ་དེ་དག་མེད་པར་བདག་ཅག་གིས་གསོལ་བ་བྱས་ཏེ། གསོ་སྦྱོང་བྱ་བ་དང་སོ་སོར་ཐར་པའི་མདོ་འདོན་པ༌[^2878]གདོན་དུ་རུང་ངམ་འོན་ཏེ་མི་རུང་། དེ་དག་མེད་པར་བདག་ཅག་གིས་དགག་དབྱེ་བྱར་རུང་ངམ་འོན་ཏེ་མི་རུང་སྙམ་དུ་རྟོག་པ་ཉིད་ན་ཐེ་ཚོམ་ཟའམ་ཉེས་པ་དེ་དག་མེད་པར་བདག་ཅག་གིས་གདོན་པ་དང་། དགག་དབྱེའི་བར་དག་བྱར་རུང་ངོ༌[^2879]ཞེས་ངེས་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ལ་ནི་ཉེས་པའི་བྱེད་པ་མི་འབྱུང་བ་མ་ཡིན་ཏེ། ཇི་སྲིད་དུ་འདོན་པ་དང་། དགག་དབྱེ་བྱེད་པའི་བར་དག་ཏུ་མི་མཐུན་པའི་ཉེས་པ་ཁོ་ནར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 4142]
དེ་བཞིན་དུ་འདིར་འདི་ནི་ལས་ཐམས་ཅད་ཀྱི་དབང་དུ་བྱས་པ་ཁོ་ན་ཡིན་པས་སྤྱིར་མདོར་བྱས་སོ། །

[Block 4143]
བསམ་པ་ཐག་པ་ནས་ཡོངས་སུ་བཙལ་ཞིང༌[^2880]གོབ་ལོབ་མ༌[^2881]བྱས་ན་དག་པའི་བྱེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གང་ཞིག་མ་འོངས་པ་ན་དགེ་སློང་དག་འབྱུང་བར་ཤེས་ནས་གལ་ཏེ་ལྷག་པའི་བསམ་པས་དེ་རྣམས་ལ་སློང་བར་བྱེད་ན། དེ་ནས་འདི་དག་གཅིག་པུས་མ་ཐོབ་པ་ལ་ལས་བྱེད་པས། དེ་རྣམས་ལ་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་ཉིད་དང་། མ་དག་པ་ཉིད་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 4144]
རུང་བ་ཙམ་དུ་གྱུར་པ་བསམ་པ་ཐག་པ་ནས་མ་ཡིན་པ་ཡོངས་སུ་བཙལ་ཞིང་དག་པའི་བྱེད་པ་མ་ཡིན་ཏེ། དེར་གཏོགས་པ་རྣམས་ལ་མི་མཐུན་པའི་ཉེས་པར་འགྱུར་རོ། །

[Block 4145]
བཙལ་བ་དང་། བོད་པ་དང་མཐོན་པོར་འདུག་སྟེ། ཕྱོགས་སུ་བལྟ་བ་དག་གིས་ནི་དེ་ཡིན་ཞེས་བྱ་བ་ནི། རྣམ་པ་དེ་གསུམ་གྱི་རིགས་ཀྱིས་ནི་ཡོངས་སུ་བཙལ་བ་ཉིད་ཡིན་ཏེ། དེ་འདིར་མངོན་པར་འདོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4146]
འདིར་བཙལ་བ་ཞེས་བྱ་བ་ནི་ཕྱོགས་དེ་དང་དེ་རྣམས་སུ་བྱུལ་བའོ། །

[Block 4147]
བོད་པ་ཞེས་བྱ་བ་ནི་སྐད་ཀྱིས་བོད་པའོ། །

[Block 4148]
མཐོན་པོར་འདུག་སྟེ་ཕྱོགས་སུ་བལྟ་བ་ཞེས་བྱ་བ་ནི་ས་ཕྱོགས་མཐོན་པོར་འགྲེང་སྟེ་མིག་རྒྱང་གིས་ཕྱོགས་ཕྱོགས་སུ་བལྟ་བར་བྱའོ། །

[Block 4149]
དེ་གསུམ་ལ་ཡང་གོ་རིམས་བཞིན་དུ་བྱ་སྟེ།

[Block 4150]
དང་པོ་རྗེས་བཙལ་བར་བྱའོ། །

[Block 4151]
བཙལ་བས་མ་རྙེད་ན་བོད་པར༌[^2882]བྱའོ། །

[Block 4152]
དེས་ཀྱང་མ་རྙེད་ན་ཕྱོགས་ཆེས་མཐོན་པོར་འགྲེང་སྟེ། ཕྱོགས་བཞིར་བལྟ་བར་བྱའོ། །

[Block 4153]
དེ་བཞིན་དུ་འདིར་འདི་འཇུག་པ་རིགས་པའི་ངོ་བོའོ། །

[Block 4154]
འདིར་གཞུང་ནི་རྣམ་པ་གཉིས་དག་ལ་སྟེ།

[Block 4155]
ཇི་སྐད་དུ་ཞུ་བ་ལས།

[Block 4156]
བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་གྲོང་མཐའ་བ་མ་ལགས་པ་དགོན་པ་ན་གནས་པ་དེ་རྣམས་ཐམས་ཅད་གསོ་སྦྱོང་གི་གནས་གཅིག་ཏུ་འདུ་བར་བྱའོ་ཞེས་བཀའ་སྩལ་ནས། གལ་ཏེ་དེ་རྣམས་མི་གདའ་ན་བཅལ་བར༌[^2883]བགྱི་ཞིང་གལ་ཏེ་དེ་རྣམས་མ་རྙེད་ན་བོད་པར་བགྱིའོ། །

[Block 4157]
གལ་ཏེ་དེ་རྣམས་ཀྱིས་མ་ཐོས་ན་གསོ་སྦྱོང་བགྱིའོ་ཞེས་བགྱི་བའམ། ཉེ་བར་འཁོར་བྱས༌[^2884]ཞེས་བྱའོ་ཞེས་གསུངས་པ་དང་། འོག་མ་ཤོས་ཀྱིས་གཞུང་ནི་ཕྱོགས་བཞིར་བལྟས་ཏེ། གསོ་སྦྱོང་ཞེས་གསུངས་པ་ཡིན་ནོ་ཞེས༌[^2885]བྱ་བ་འདི་ནི་ས་ཕྱོགས་མཐོན་པོར་གནས་ཏེ་བརྟག་པར་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སུ་འབྲངས་ནས་སོ། །

[Block 4158]
ཞུ་བ་ལས་རྣམ་པ་འདི་གང་ཞིག་མ་གསུངས་པ་དེ་ནི་ཆུད་ཟོས་པར་མཐོང་བ་ཡིན་ནོ། །

[Block 4159]
གསོ་སྦྱོང་གི་གཞི་ལས་མཐུན་པའི་གསོ་སྦྱོང་གི་ཚོགས་པའི་སྐབས་སོ། །

[Block 4160]
གསོ་སྦྱོང་བྱའོ། །

[Block 4161]
ཟླ་བ་ཕྱེད་ཕྱེད་ཀྱི་ཚེས་བཅོ་ལྔ་ལའོ། །

[Block 4162]
སོ་སོར་ཐར་པའི་མདོ་གདོན་པས་སོ་ཞེས་བྱ་བ་ནི། གང་ཞིག་ཚེས་བཅུ་བཞི་དང་བཅོ་ལྔ་པ་ཉིད་ལ་འདི་མཚན་མོ་གཅིག་གིས་མ་ཆོག་པས་དེར་དེ་རིང་ཉིད་དུ་ཚེས་བཅོ་ལྔ་ཞེས་བྱ་བ༌[^2886]སྟེ། གསོ་སྦྱོང་བྱེད་པ་དེ་བས་ན་བཅུ་བཞི་པ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 4163]
གང་ཞིག་མདོ་ལས་གསོ་སྦྱོང་ནི་གཉིས་ཏེ། བཅུ་བཞི་པ་དང་། བཅོ་ལྔ་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4164]
དེ་ནི་འདིར་འགལ་བ་མེད་དོ། །

[Block 4165]
དེ་ཉིད་ལ་འདི་བསྟན་པར་བྱས་པའོ། །

[Block 4166]
མཚན་མོ་གཅིག་ཆད་པ་དང་། གཞན་དུ་གསོ་སྦྱོང་ཞེས་བྱ་བ་འདིས་བསྟན་པའི་དོན་དུ་ཟླ་བ་ངོ་དེའི་ཚེས་གྲངས་གང་ལ་མཐར་ཐུག་པ་ལ༌[^2887]དེང་དགེ་འདུན་གྱི་གསོ་སྦྱོང་བཅུ་བཞི་པ་ལགས་ཏེ། བདག་དགེ་སློང་མིང་འདི་ཞེས་བགྱི་བའི་གསོ་སྦྱོང་བཅུ་བཞི་པ་ལགས་པས་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 4167]
དེ་ཡང་མཚན་མོ་གཅིག་ཆད་པས་དེ་གསོ་སྦྱོང་ཞེས་བྱ་བ་བསྟན་པའི་དོན་དུའོ། །

[Block 4168]
ཟླ་བ་ཕྱེད་ཕྱེད་ཅེས་བྱ་བའི་ལན་གཉིས་སུ་སྨྲ་བ་ནི་འདིར་ཟླ་བ་ཕྱེད་ཕྱེད་ཅེས་བྱ་བའི་དོན་དུའོ། །

[Block 4169]
སོ་སོར་ཐར་པའི་མདོ་གདོན་པས་སོ་ཞེས་བྱ་བ་ནི། འདིར་གསོ་སྦྱོང་གིས་ཚུལ་ཁྲིམས་གསོ་བར་བྱེད་པ་ཡོད་པས། དེ་དག་བཙལ་བའི་ཕྱིར་སོ་སོར་ཐར་པའི་མདོ་གདོན༌[^2888]པས་སོ། །

[Block 4170]
དྲན་པ་ཙམ་གྱིས་བྱས་པ་དང་། མ་བྱས་པ་ལ་སོ་སོར༌[^2889]བརྟག་པའོ། །
--- END BLOCKS ---
