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
[Block 1016]
གཉིས་ཀ་ལ་མི་ལྟོས་པ་ཉིད་བྱུང་བ་ནི་གནས་བཅས་པ་འཇིག་པའི་རྒྱུ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ།[^729] གཉིས་ཀ་ལ་ཞེས་བྱ་བ་ནི་གནས་དང་གནས་པར་ལྡན་པ་དག་ལའོ། །

[Block 1017]
ཅིག་ཅར་རམ་རིམ་གྱིས་མི་ལྟོས་པ་ཉིད་དུ་བྱུང་བ་ཉིད་དོ། །

[Block 1018]
བཅས་པ་ནི་གནས་བཟུང་བ་ལས་ཉམས་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 1019]
མི་ལྟོས་པ་ཉིད་དུ་གྱུར་པ་གཅིག་ལ་རེ་ཞིག་རྟེན་ལ་རྗེས་སུ་འཇུག་པ་སྟེ། ཇི་སྲིད་དུ་གཞན་མི་ལྟོས་པ་ཉིད་དུ་གྱུར་པ་ཞེས་བྱ་བའོ། །

[Block 1020]
གང་ཞིག་གནས་དང་གནས་པ་ཉིད་དུ་ཁས་བླངས་པ་འདི་ནི་འཁོར་དང་འབྲེལ་པ་སྟེ། གཅིག་ལ་ལྟོས་པ་དང་བཅས་པ་ཉིད་ལ་འཁོར་དང་འབྲེལ་བ་དང་བྲལ་བ་ཉིད་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་འདི་ནི་འདིར་རྣམ་པར་གཞག་པའོ། །

[Block 1021]
མཁན་པོ་མ་ཡིན་པ་དག་ཚོགས་ན་འདོད་པས་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་སྲིད་དུ་གསུངས་པ། མཁན་པོ་ཉེ་བར་གནས་པ་ལ་གནས༌[^730]ལ་ཞུ་བར་མི་བྱའོ་ཞེས་བྱ་བ་འདི་ལ་དེ་བསྟན་པའོ། །

[Block 1022]
མེད་པས་འཁོར་དང༌[^731]འབྲེལ་པ་ཁས་བླངས་པ་ལ་ལྟོས་པ་དང་བཅས་པ་ཉིད་དོ་ཞེས་བྱ་བའོ། །

[Block 1023]
མཁན་པོ་ལ་བརྟེན་པའི་གནས་ལས་གནས༌[^732]གཞན་རྣམས་ནི་མཁན་པོ་མ་ཡིན་པའོ། །

[Block 1024]
ཚོགས་པར་གྱུར་པ་ནི་ཚོགས་པ་སྟེ། དེས་ནི་ཚོགས་པ་ཡོད་པ་ལ་མངོན་པར་འདོད་པའི་གནས་ཀྱིས་གནས་པ་ལ་འཇུག་པའོ། །

[Block 1025]
གང་ཞིག་འདི་ལ་ཞུ་བ་བྱེད་པ་དེ་ལ་གནས་པས་གནས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1026]
དེ་དང་ན་ནི་དེ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་མཁན་པོར་རྟོག་པའི༌[^733]གནས་དེ་དང་ཚོགས་ནའོ། །

[Block 1027]
དེ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་མཁན་པོ་དེ་ཉིད་ཀྱིས་ཏེ། འདི་ལ་རེས་བྱས་པ་དང་རེས་མི་བྱ་བ་མེད་དོ། །

[Block 1028]
མཁན་པོ་མཐོང་མ་ཐག་ཏུ་སྟན་ལས་ལྡང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། མཁན་པོ་ནི་དཔེ་ཙམ་སྟེ་གནས་གཞན་དག་མཐོང་ན་ཡང་ཆོ་ག་འདི་གཞག་པའི་ཕྱིར་རོ། །

[Block 1029]
གཙུག་ལག་ཁང་དེ་ན་གནས་པས་ཉིན་པར་ལན་གསུམ་འགྲོ་བར་བྱའོ། །

[Block 1030]
གལ་ཏེ་དགོན་པ་ན་འདུག་ན་རྒྱང་གྲགས་ཙམ་ན་ཉིན་རེ་ལན་རེའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་རྒྱང་གྲགས་ལ་དགོན་པ་དེ་ཡོད་ན་དེ༌[^734]གང་དུ་གནས་པ༌[^735]ཡོད་པ་དེར་ཉི་མ་རེ་རེར་འོངས་ཏེ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1031]
རྒྱང་གྲགས་ལྔ་ཡོད་ན་ཞག་ལྔ་འམ་དྲུག་བཅིང༌[^736]ངོ་། །དཔག་ཚད་ཕྱེད་དང་གསུམ་དག་ན་གསོ་སྦྱོང་གི་ཚེའོ་ཞེས་བྱ་བ་ནི་འདིའི་འོག་ཏུ་མཚམས་གཅིག་པ་ཉིད་མེད་པའི་ཕྱིར་གནས་ཉིད་ལ་མེད་པར་རིག་པར་བྱའོ། །

[Block 1032]
གནས་པ་ཆད་པས་གཅད་པར༌[^737]འོས་པ་ཆད་པས་མི་གཅད་པར༌[^738]མི་བྱའོ། །

[Block 1033]
ཆད་པ་ནི་ལྔ་སྟེ། གཏམ་དྲི་བར་མི་བྱེད་པ་དང་། གདམས་ངག་མི་སྦྱིན་པ་དང་། བསྙེན་བཀུར་དང་ཆོས་དང་ཟང་ཟིང་དག་གིས༌[^739]ལོངས་སྤྱོད་དུ་མི་གཞུག་པ་དང་། དགེ་བའི་ཕྱོགས་བརྩམས་པ་རྒྱུན་གཅད༌[^740]པ་དང་། གནས་དགག་པར་བྱའོ། །

[Block 1034]
མ་དད་པ་དང་། ལེ་ལོ་ཅན་དང་། བཀའ་བློ་མི་བདེ་བ་དང་། མ་གུས་པ་དང་། སྡིག་པའི་གྲོགས་བྱེད་པ་ལ་དེ་དག་འོས་པ་ཉིད་དོ། །

[Block 1035]
ཆད་པས་བཅད་པ་གཞན་གྱིས་ལེན་པར་བྱེད་པ་ལ་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ན་ཡང་བྱེད་བཞིན་པ་ལ་གལ་ཏེ་འདི་བཟོད་པར་བྱེད་པ་ལ་གུས་པ་མི་བྱེད་ན་དེ་ལ་ཅི་ཞིག་བྱ་ཞེ་ན། དེའི་ཕྱིར༌[^741]གུས་པར་མི་བྱད་ན་དྲང་པོར་བྱ་བའི་ཕྱིར་དགེ་སློང་ཤེས་གཉེན༌[^742]ཅན་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བུ་ལས་ཤེ་ན། དེའི་ཕྱིར་བཤེས་གཉེན་ཅན་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་དེ་དྲང་བར་བྱ་བའི་ཕྱིར་མཁས་པ་དེ་ལའོ།[^743] །རྒྱུ་བཏང་བ་བཟོད་པར་གསོལ་བར་བྱེད་པ་ལ་བཟོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་རྒྱུ་མཚན་གང་ཞིག་ཆད་པས་བཅད་པ་དེ་ཡོངས་སུ་དོར་བ་ལ་བཟོད་པའོ། །

[Block 1036]
དེ་ལྟ་ཉིད་དུ་ཡང་མ་ཡིན་ཏེ་འོན་ཀྱང་བཟོད་པར་བྱེད་པ་ལའོ། །

[Block 1037]
མི་འོས་པ་ཆད་པས་གཅད་པར༌[^744]མི་བྱའོ། །

[Block 1038]
འོས་པ་ལ་མི་བཟོད་པར་མི་བྱའོ། །

[Block 1039]
མི་འོས་པ་ལ་བཟོད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རྣམ་པ་ཐམས་ཅད་དུའོ། །

[Block 1040]
མི་བྱེད་པ་ཉིད་ཡིན་ན་གནས་ཁང་ནས་བསྐྲད་པར་བྱའོ། །

[Block 1041]
དགེ་ཚུལ་ལ་ནི་ཆུ་ཚགས་དང་རིལ་བ་སྤྱི་བླུགས༌[^745]མཐང་གོས་དང་བཅས་པའི་བླ་གོས་ཀྱང་བྱིན་ཏེའོ། །

[Block 1042]
གལ་ཏེ་བསྙེན་པར་རྫོགས་པར་འདོད་པ་ཞིག་ཡིན་ན་ཡོ་བྱད་ལྔའོ་ཞེས་བྱ་བ་ནི་བྱིན་ཏེ་བསྐྲད་པར་བྱའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 1043]
ཆུ་ཚགས་ནི་སྔར་ཉིད་དུ་བརྗོད་པའི་དྲུང་ཞེས༌[^746]བྱ་བ་བརྗོད་པ་ཡིན་ཏེ། ཆོས་གོས་གསུམ་དང་གདིང་བ་དང་ལྷུང་བཟེད་དང་ཞེས༌[^747]བྱ་བ་ལྔའོ། །

[Block 1044]
བསྙེན་པར་རྫོགས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡོ་བྱད་ལྔ་པོ་དང་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 1045]
སེང་གེ་ལྟར་གྱ་ཚོམ༌[^748]མི་བྱའོ། །

[Block 1046]
གནོད་པར་འགྱུར་བའི་ཁྲིམས་སུ་བྱ་བ་མི་བཅའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་དུ་གྱུར་པའི་དགེ་སློང་རྣམས་ཀྱིས་སོ། །

[Block 1047]
ཁའི་གནས་པ་ཉིད་ནི་མ་བཀྲུས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མཚན་མོ་གནས་པ་ལས་ལངས་ནས་སོ་ཤིང་ངམ་གཞན་གྱིས་ཁ་སྦྱངས་ཀྱི་བར་དུ་རེ་ཞིག་གཞན་ལ་ཕྱག་དང་བཟའ་བ་ལ་སོགས་པ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདི་ལ་འདིས༌[^749]སྟོན་པའོ། །

[Block 1048]
འདི་ལ་གཞུང་ནི་དགེ་སློང་གིས་སོ་ཤིང་མ་བོར་བར་བསོད་སྙོམས་བཟའ་བར་མི་བྱའོ། །

[Block 1049]
དེ་ཉིད་ལ་ནི་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་དང་། གླེང་གཞི་ལས་ཇི་སྐད་དུ་བྱིན་ལེན་མ་བྱས་པར་ཁ་ཟས་ཉེ་བར་གནས་པ་བཀག་པ་ལ་བརྟེན་པ་འདི་གསུངས་པ་ཡིན་ནོ། །

[Block 1050]
ཁའི་དྲི་མ་མ་བསལ་བར་ཁ་ཟས་ཀྱི་ཕྱོགས་ཉིད་ལ་ཁྱེད་ཅག་གིས་འདའ་བར་བྱེད་པ་དེ༌[^750]ཞེས་བྱ་བ་འདི་ལའོ། །

[Block 1051]
དེ་ལྟར་ན་གནས་འཇུག་པ་བསྟན་པའོ། །

[Block 1052]
གཞུང་ནི་ལྡང་བྱེད་འདི་ལ་ལྷན་ཅིག་གནས་པ་དང་། ཉེ་གནས་ཀྱིས་ནང་པར་སྔར་ལངས་ཏེ་ཤམ་ཐབས་ཟླུམ་པོར་བགོས་ནས་སོ་ཤིང་བོར་ཏེ་མཚམས་ཀྱི་ནང་གི༌[^751]མཆོད་རྟེན་ལ་ཕྱག་འཚལ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་ཡོངས་སུ་དག་པར་བྱ་བ་ཉིད་དེའི་ཕྱིར་སོ་ཤིང་བོར་ནས་ཞེས་བྱ་བ་འདིར་ཚིག་གོ། །

[Block 1053]
དེའི་ཕྱིར་མདོ་འདི་སྨོས་ཏེ། སོ་ཤིང་དབེན་པར་དོར་རོ་ཞེས་བྱ་བའོ།

[Block 1054]
[^752] །འདི་ནི་རྗེས་སུ་མཐུན་པ་མ་ཡིན་ཏེ། དེ་བས་ན་ཁའི་དྲི་མ་དག་པའི་དོན་དུ་འདི་ལ་བརྟེན་པར་བྱ་བ་ཉིད་དོ། །ཇི་ལྟར་དོར་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་བཤང་གཅི་བྱ་བ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ་དབེན་པ་ཉིད་དུའོ། །

[Block 1055]
ལོངས་སྤྱད་དུ་རུང་བའི་ཤིང་ངམ་རྩིག་པའི་དྲུང་དུ་མི་དོར་རོ་ཞེས་བྱ་བ་ལ། དྲུང་དུ་ཞེས་བྱ་བ་ནི་ཉེ་བ་ལ་བྱ་སྟེ། གང་དུ་སྐྱེས་བུ་ཆེན་པོའི་དུས་ཐམས་ཅད་གནས་པ་དེ་ནི་འདིར་ཉེ་བར་ལོངས་སྤྱད་པར་བྱ་བ༌[^753]སྟེ། དེར་སོ་ཤིང་དོར་བ་ལ་སོགས་པ་མི་བྱ་ཞེས་བྱ་བའི༌[^754]དོན་ཏོ། །
--- END BLOCKS ---
