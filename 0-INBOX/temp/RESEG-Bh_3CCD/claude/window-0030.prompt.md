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
[Block 1051 [VERSE]]
གཙོ་བོ་ཡོད་དང་གཅིག་པ་ཉིད། །
དོན་ལྡན་ཉིད་དང་དེ་ལས་གཞན། །
གཞན་དོན་ཉིད་དང་དུ་མ་དང་།
བྲལ་བ་དང་ནི་མ་བྲལ་ཉིད། །

[Block 1052 [VERSE]]
ལྷག་མའི་སྐབས་དང་བྱེད་མིན་ཉིད། །
དོན་ནི་གཙོ་བོ་བཅུ་རུ་བཤད། །

[Block 1053 [VERSE]]
ཕྱིན་ཅི་ལོག་པའི་བྱེ་བྲག་ལྔ་ཡིན་ཏེ། །
བྱེད་པ་མ་ཚང་བས་ནི་མི་ནུས་པ། །
དབྱེ་བ་ཉི་ཤུ་རྩ་བརྒྱད་ཅན་ཞེས་བྱ། །
དགའ་བ་དགུ་དང་དངོས་གྲུབ་རྣམ༌[^737]བརྒྱད་དོ། །

[Block 1054]
ཞེས་མདོར་བསྟན་པའོ། །

[Block 1055]
རྒྱས་པར་བསྟན་པ་ཡང་མུན་པ་དང་གཏི་མུག་དང༌[^738]གཏི་མུག་ཆེན་པོ་དང་། མུན་པ་ཐིབས་པོ་དང་། ཤིན་ཏུ་མུན་ནག་ཐིབས་པོ་ཞེས་ཕྱིན་ཅི་ལོག་པ་ལྔའོ། །

[Block 1056]
མིག་དང་རྣ་བ་དང་སྣ་དང་ལྕེ་དང་ལུས་མ་ཚང་བ་དང་། ངག་དང་ལག་པ་དང་རྐང་པ་དང་བཤང་སྒོ་དང་། གསང་བའི་དབང་པོ་མ་ཚང་བ་དང་།[^739] ཡིད་མ་ཚང་བ་སྟེ་བཅུ་གཅིག་གོ། །

[Block 1057]
དགའ་བ༌[^740]དང་དངོས་གྲུབ་མ་ཚང་བས་བློ་དྲུག་པ་ནི་བཅུ་བདུན་ནོ། །

[Block 1058 [VERSE]]
རྟོག་པ་སྒྲ་དང་ཁ་དོག་འཛིན་པ་དང་། །
སྡུག་བསྔལ་སེལ་བ་གསུམ་སྟེ་བཤེས་གཉེན་ཕྲད། །
སྦྱིན་པ་དད་དང་དངོས་གྲུབ་རྣམ༌[^741]བརྒྱད་དོ། །

[Block 1059]
ཞེས་འབྱུང་བས་སོ། །

[Block 1060]
ལྷག་པའི་ལྷ་ལས་འབྱུང་བ་དང་། འབྱུང་བ་ལྷག་པ་ལས་འབྱུང་བ་དང་ལྷག་པའི་ནང་གི་བདག་ཉིད་ལས་འབྱུང་བ་དེ་སེལ་བས་དངོས་གྲུབ་གསུམ་ནི་དགའ་བ་དག༌[^742]གོ། །

[Block 1061]
ཕྲ་བ་ལ་སོགས་པའི་མཚན་ཉིད་དངོས་གྲུབ་བརྒྱད་དང་ནི་དགའ་བ་དགུའོ། །

[Block 1062]
ཚིག་གི་དོན་དྲུག་ཅུ་གང་གི་ཚེ་སྐྱེས་བུས་བྱེ་བྲག་ཏུ་མཐོང་ན་དེའི་ཚེ་གྲོལ་བའོ། །

[Block 1063]
དེ་ཡང་ཚད་མས་ངེས་པར་བྱ་བ་ཡིན་ཏེ། མངོན་སུམ་དང་། རྗེས་སུ་དཔག་པ་དང་། ཡིད་ཆེས་པའི་ཚིག་སྟེ་ཚད་མ་གསུམ་མོ། །

[Block 1064]
དེ་ལ་མངོན་སུམ་གྱིས༌[^743]དེ་ཁོ་ན་ཉིད་ཉི་ཤུ་རྩ་གསུམ་ངེས་པར་བྱ་བ་སྟེ། སོ་སོའི་ཡུལ་རྣམས་ལ་རྟོག་པ༌[^744]ནི་མངོན་སུམ་ཡིན་ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 1065]
རང་བཞིན་ནི་ཡོན་ཏན་གསུམ་གྱི་བདག་ཉིད་དེ༌[^745]རྗེས་སུ་དཔག་པས་ངེས་པར་བྱ་བ་སྟེ། ལྐོག་ཏུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1066]
སྐྱེ་བ་དང་ཚེ་དང་ལོངས་སྤྱོད་ནི་སྤྱིར་མཐོང་བའི་རྗེས་སུ་དཔག་པས་སོ། །

[Block 1067]
ཐར་པ་ལ་སོགས་པ་ཤིན་ཏུ་ལྐོག་ཏུ་གྱུར་པ་རྣམས་ལ་ཡིད་ཆེས་པའི་ཚིག་གིས་སོ། །

[Block 1068]
དེ་ལྟར་ཚད་མ་དང་བཅས་པ་འཆིང་བ་དང་གྲོལ་བའི༌[^746]ཐ་སྙད་ཀྱི་རྒྱུར་གྱུར་པ་གྲངས་ཅན་གྱི་གཞུང་ལ༌[^747]འདོད་དོ། །

[Block 1069]
དེ་ལ་སྨྲས་པ། རེ་ཞིག་དང་པོ་དེ་ཁོ་ན་ཉིད་ཉི་ཤུ་རྩ་ལྔ་མེད་དེ། ཡིད་དང་བློ་དང་ང་རྒྱལ་གཅིག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1070]
འདིར་ནི་ཕྱིའི་དོན་བདག་གིས་རྟོགས་སོ་ཞེས་ངེས་པར་བྱས་པ་ཙམ་གྱིས་བློ་དང་ང་རྒྱལ་དག་ཡིད་ལས་ཐ་དད་པ་མ་ཡིན་ནོ། །

[Block 1071]
ཡིད་ཁོ་ན་བདག་གིས་རྟོགས་སོ་ཞེས་ངེས་པ་དང་བདག་ཉིད་དུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1072]
ལ་ལ་སྨྲ་བ་ནི་རྟོག་པར་བྱེད་པ་ཡིད་ཡིན་ནོ་ཞེས་མི་རིགས་ཏེ། ཁྱད་པར་གྱི་བདག་ཉིད་རྣམ་པར་རྟོག་པ༌[^748]ནི་སྤྱིའི་བདག་ཉིད་ངེས་པ་ལ་འདུས་པའི་ཕྱིར་རོ། །

[Block 1073]
དངོས་པོའི་བྱེ་བྲག་མ་ངེས་པས་རྣམ་པར་རྟོག་པ་མི་འབྱུང་ངོ་། །བདག་གིས་རྟོགས་པ་དང་བདག་རྟོགས་པ་པོ་ཞེས་ཁྱད་པར་ནི་ངེས་པ་ལས་ཐ་དད་མ་ཡིན་ཏེ། ཡིད་ནི་ཐམས་ཅད་ངེས་པར་བྱེད་པའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1074]
གང་གི་ཕྱིར་ཤེས་པ་ནི་ལྡོག་པ༌[^749]དུ་མ་དང་ལྡན་པ། ལྡོག་པ་གང་གིས་བརྟགས་པ་དེའི་བདག་ཉིད་དེ་ཡིན་ནོ། །

[Block 1075]
ང་རྒྱལ་མ་ཡིན་པ་ལས་ལོག་པ་དེ་ཉིད་ང་རྒྱལ་དུ་བསྟན་པ་དང་། རྣམ་པར་མི་རྟོག་པ་ལྡོག་པ་ལས་དེ་ཉིད་རྣམ་པར་རྟོག་པ་ཡིན་ཞེས་ཡིད་གཅིག་པུ་ཁོ་ན་ཡིན་གྱི་བློ་དང་ང་རྒྱལ་མེད་དོ། །

[Block 1076]
ལས་ཀྱི་དབང་པོ་རྣམས་ཀྱང་གུད་ན་མེད་དེ། དེ་རྣམས་ལུས་ཀྱི་དབང་པོ་ལ་འདུས་པའི་ཕྱིར་རོ། །

[Block 1077]
གང་འདི་ལྟར་སྨྲ་བའི་ཚིག་དང་། ལེན་པ་དང་། འགྲོ་བ་དང་། འདོར་བ་དང་། དགའ་བ་ལྔ་པོའི་དབྱེ་བས༌[^750]ནི་མི་རིགས་ཏེ། མ་ཁྱབ་པ་དང་ཐལ་ཆེས་པར་འགྱུར་རོ། །

[Block 1078]
གང་གི་ཕྱིར་རྐང་པ་མེད་པ་སྦྲུལ་ལ་སོགས་པ་རྣམས་ཀྱི་འགྲོ་བ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1079]
སོ་དང་མིག་གི་རྫི་མ༌[^751]དག་ལྡང་པ་དང་། བཙུམ་པ་དང་། ཕྱེ་བ༌[^752]ལས་ཡོད་པས་ལས་ཀྱི་དབང་པོར་ཐལ་བར་འགྱུར་རོ། །

[Block 1080]
གཞན་ཡང་དུར་བའི་མཆི་མས་དུར་མོ་མངལ་ལེན་པའི་ཕྱིར་མཆི་མ་ཡང་ལས་ཀྱི་དབང་པོར་ཐལ་བར་འགྱུར་རོ། །

[Block 1081]
དེ་བས་ལས་ཀྱི་དབང་པོ་རྣམས་ནི་མེད་དོ། །

[Block 1082]
རང་བཞིན་ཡང་ནི་དེ་ཁོ་ན་ཉིད་གུད་པ་མ་ཡིན་ཏེ། དེ་ཙམ་ལས་ཀྱང་ཐམས་ཅད་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1083]
སྐྱེས་བུ་ཡང་ཚད་མས་མ་གྲུབ་པས་ངོ་བོ་ཉིད་མེད་དེ། དེའི་མཐོང་བ་ལ་སོགས་པའི་བྱ་བའི་འབྲེལ་པ་ཇི་ལྟར་འཐད་དོ། །

[Block 1084]
[^753]

[Block 1085]
དེ་ལྟར་གྲངས་ཕྱོགས་གཅིག་པ་མ་གྲུབ་པས་ངེས་པ་མེད་དོ། །

[Block 1086]
དེའི་ཕྱིར་ན་ཕུང་པོ༌[^754]ལྔ་ལས་དངོས་པོ་གང་ཡང་མེད་དོ། །

[Block 1087]
རང་བཞིན་བེམས་པོ་ཡིན་པས་བྱ་བ་ཇི་ལྟར་བྱེད། བེའུ་འོ་མས༌[^755]སྐྱེད་པ་ཡིན་ཞེས་མི་རིགས་ཏེ། དེ་ལ་གང་གི་ཕྱིར་བའི་སེམས་ཀྱིས་འོ་མ་སྦྱིན་པ་ལ༌[^756]འཇུག་པ་ཡིན་གྱི་འོ་མ་ནི་མ་ཡིན་ནོ། །

[Block 1088]
དཔེར་ན་བ་མི་འདོད་ན་རང་གི་བེའུ་ལ་ཡང་མི་སྟེར་བའི་ཕྱིར་རོ། །

[Block 1089]
དེའི་ཕྱིར་སེམས་དང་ལྡན་པ་ཁོ་ན་ལ་འཇུག་པ་དང་ལྡོག་པའོ། །

[Block 1090]
གང་གི་ཕྱིར་སྐྱེས་བུས་མི་བྱེད་དོ་ཞེས་ཁྱེད་ཅག་འདོད་པས་བྱ་བ་ཐམས་ཅད་གང་ལས་འབྱུང་། དེ་ལྟར་སྐྱེས་བུ༌[^757]མེད་དེ་དམིགས་པའི་མཚན་ཉིད་དང་ལྡན་པ་མི་དམིགས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
