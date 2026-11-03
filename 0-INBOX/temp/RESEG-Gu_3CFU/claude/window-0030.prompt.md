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

[Block 1056]
དེའི་ཚད་ནི་སོར་བཅུ་གཉིས་མན་ཆད་སོར་བརྒྱད་ཡན་ཆད་དོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་སོ་ཤིང་ལའོ། །

[Block 1057]
སོར་བརྒྱད༌[^755]ཡན་ཆད་ཅེས་བྱ་བ་ནི་ཡན་ཆད་ཀྱི་སྒྲ་དང་འདིར་མཚམས་སྦྱར་བ་སྟེ། སོར་བཅུ་གཉིས་ནས་བརྩམས་ཏེ་ཇི་སྲིད་དུ་སོར་བརྒྱད་ཉིད་ནི་འདིའི་ཚད་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1058]
བད་ཀན་མང་བ་ནི་མེད་ན༌[^756]སོར་བཞི་ལས་ལྷག་པ་ཡན་ཆད་དོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་སོར་བཞི་ལས་ལྷག་པ་ཡན་ཆད་ཀྱི་ཚད་དེ་སྲིད་དུ་འབྱུང་བ་ལ་སྔ་མའི་ཚད་ཀྱིས༌[^757]སོ་ཤིང་ལ་བད་ཀན་མང་བའི་སོ་ཤིང་གི་ཚད་དོ། །

[Block 1059]
འདིར་གཞུང་ནི་བར་ནི་དབུས་ཏེ་འོན་ཀྱང་བད་ཀན་མང་བ་གང་ཡིན་པ་ནི༌[^758]དེ་རྣམས་ཀྱིས་ནི་སོ་ཤིང་སོར་བཞི་པ་མ་གཏོགས་པར་ཡང་དོར་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1060]
གནས་ཁང་དུ་ཆོལ་ཟངས་ཀྱི་ནང་དུ་སོ་ཤིང་དོར་བ་ལ་མི་རིགས་པ་མེད་དོ་ཞེས་བྱ་བ་ལ། དོར་བ་ལ་ཞེས་བྱ་བ་ནི་སྐབས་ཉིད་ཀྱི་ཕྱིར་སོ་ཤིང་དོར་བ་ལའོ། །

[Block 1061]
དེ་ལ་ཝ་ཁ་ཡང་མི་དབེན་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་འདིར་སོ་ཤིང་དོར་བ་ལ་ཝ་ཁར་སྦས་ཏེ། དབེན་པ་ཉིད་དུ་གྲུབ་པ་ཁོ་ན་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1062]
དེར་ཁྲུ་གང་ཁོར་ཡུག་ཏུ་རྣམ་པ་དེ་ལྟ་བུ་བྱར་རུང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་ཝ་ཁར་རོ། །

[Block 1063]
དེ་ལྟ་བུ་བྱར་རུང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སོ་ཤིང་དོར་བའི་རིགས་ཅན་ཀྱི་རྐང་པ་བཀྲུ་བ་ལ་སོགས་པའི་བྱ་བ་ཉིད་ལའོ། །

[Block 1064]
ཁྲུ་གང་ཁོར་ཡུག་ཏུ་རུང་བ་ཉིད་དེ་ཁྲུ་གང་ཁོར་ཡུག་ལས་གཞན་དུ་སོ་ཤིང་དོར་བ་ལ་སོགས་པ་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1065]
དེའི་རྗེས་ལ་ལྕེ་བཞར་བར་བྱའོ། །

[Block 1066]
ལྕེ་བཞར༌[^759]ཉེ་བར་གཞག་པར་བྱའོ། །

[Block 1067]
དེའི་ཞེས་བྱ་བ་ནི་ལྕེ་བཞར་དོན་ལའོ། །

[Block 1068]
ལྕེ་བཞར་བར་བྱ༌[^760]ཞེས་བྱ༌[^761]ནི་བཞར་བར་བྱེད་པའི་ཁབ་ཀྱི་རྫས་ཏེ་རྫས་གང་ཞིག་ཁབ་བྱེད་པར༌[^762]གན་དང་ཟངས་དང་ལྕགས་དང་ཁར་བ༌[^763]རྣམས་ཀྱིས་ཏེ། དེའི་རང་བཞིན་ལས་བྱས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1069]
དོན་འདི་ལ་སོ་ཤིང་གི་ཚལ་པས་ཀྱང་རུང་ངོ་ཞེས་བྱ་བ་ལ། དོན་འདི་ལ་ཞེས་བྱ་བ་ནི་ལྕེ་བཞར་བའི་དོན་ལའོ། །

[Block 1070]
དེ་མི་རྣོ་བར་བྱ་བའི་ཕྱིར་གཅིག་གིས་གཅིག་དྲུད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། གཅིག་གིས་གཅིག་ཅེས་བྱ་བ་ནི་ཕན་ཚུན་དུའོ། །

[Block 1071]
དེ་ཞེས་བྱ་བ་ནི་སོ་ཤིང་འཆའ་བ་ལའོ། །

[Block 1072]
མི་རྣོ་བས་སོ་དང་ལྕེ་དང་རྣ་བ་དྲུད་བཞར་བྱའོ། །

[Block 1073]
དལ་གྱིས་མ་ཡིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དལ་གྱིས་དྲུད་ཅེས༌[^764]བྱ་བའི་དོན་ཏོ། །

[Block 1074]
དེ་དག་གིས༌[^765]ཤ་ལ༌[^766]མི་གནོད་པར་རོ་ཞེས་བྱ་བ་ནི་སོ་དང་རྙིལ་ལ་སོགས་པ་ལའོ། །

[Block 1075]
སོ་དང་ལྕེ་གཉིས་ཀྱི་དྲུད་བཞར་གྱི་ཕྱོགས་ཁའི་དྲི་མས་གོས་པ་མ་བཀྲུས་སམ་སས་མ་བསྐུས་པ༌[^767]མི་དོར་རོ་ཞེས་བྱ་བ་ནི་སོ་ཤིང་དང་དྲུད་བཞར་དོར་རོ་ཞེས་བྱ་བ་འདི་དང་འབྲེལ་ལོ། །

[Block 1076]
ཆུ་མེད་ན་སོ་དང་ལྕེ་གཉིས་ཀྱི་དྲུད་བཞར་སས་མ་བསྐུས་པར་རོ། །

[Block 1077]
དྲུད་བཞར་ནི་སླར་འདི་དག་ལ་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་སོ་ཤིང་དང་ཚལ་པའོ། །

[Block 1078]
སྒྲ་མ་བྱས་པར༌[^768]མི་དོར་རོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་གསུངས་པ་གཉིས་དོར་ཏེ་འདི་ནི་དཔེ་ཡིན་ནོ།[^769] །སྒྲ་མ་བྱས་པར་སོ་དང་ལྕེ་དག་གི༌[^770]དྲུད་བཞར་ཏེ། འདིས་གཞན་ཡང་མཚོན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1079]
གང་ཞིག་དཔེས་མཚོན་པ་དེ་སྟོན་པར་བྱེད་པ་ནི་བཤང་བ་དང་གཅི་བ་དང་མཆིལ་མ་དང་སྣབས་དང་སྐྱུགས་པ་དང་རླུགས་པ་དང་གཞན་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། མཆིལ་མ་ཡིན་ལ་སྐྱུགས་པ་མ་ཡིན་པ་ནི་འདི་ལྟ་སྟེ། དཔེར་ན་སྣའི་བཤལ་སྨན་ལྟ་བུའོ། །

[Block 1080]
ཕྱོགས་ཞེས་བྱ་བ་ནི་སོ་ཤིང་ལའོ། །

[Block 1081]
གཙོ་བོ་ཉིད་ཀྱི་ཕྱིར་དོར་རོ། །

[Block 1082]
ཇི་ལྟར་ཟོས་པ་དེ་བཞིན་དུ་ཐུར་དུ་རླུགས་པ་ལྟ་བུའོ། །

[Block 1083]
དེ་བས་ན་མཆིལ་མ་དང་བཤང་བ་བརྗོད་པ་ཡོད་ཀྱང་སྐྱུགས་པ་དང་རླུགས་པའི་ཚིག་གོ། །

[Block 1084]
བཤང་བ་ལ་སོགས་པ་གཞན་དོར་བར་བྱ་བ་ཐམས་ཅད་ཉེ་བར་བསྡུ་བའི་དོན་དུ་ཀྱང་ངོ་ཞེས་བྱ་བའི་ཚིག་གོ། །

[Block 1085]
དེ་ལས་བྱི་དོར་འབྱུང་བ་བཞིན་དུ་འདག་རྫས༌[^771]དང་ལས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་སོ་ཤིང་དོར་བ་ལས་སོ། །

[Block 1086]
འདག་རྫས་དང་ལྕི་བ་ལས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་འབྱུང་བའོ། །

[Block 1087]
འདིར་གཞུང་ནི་སོ་ཤིང་མ་རྙེད་ན་བ་གླང༌[^772]གི་ལྕི་བ་དང་འདག་རྫས་ཀྱིས་ཁ་སྦྱང་བར་བྱའོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 1088]
སོ་ཤིང་དོར་བ་དེ་མ་ཐག་ཏུ་བྱ་བ་གང་གིས་བསྒྲུབས་ནས་དེ་ལ༌[^773]ཕྱག་བྱའོ། །

[Block 1089]
གནས་པས་སྒྲུབ་པའི་དབང་དུ་བྱས་ཏེ་དེ་ནས་ཀྱི་སྒྲ་ནི་དབང་དུ་བྱ་བའི་དོན་ཏེ་རྗེས་ཀྱི་དོན་མ་ཡིན་ནོ། །

[Block 1090]
འདིའི་འོག་ཏུ་གནས་པས་བསྒྲུབ་པ༌[^774]དབང་དུ་བྱས་པར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
