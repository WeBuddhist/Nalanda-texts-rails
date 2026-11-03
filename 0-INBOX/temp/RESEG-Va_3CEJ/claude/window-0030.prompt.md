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
ཟག་པ་མེད་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་དག་ཡིན་ནོ། །

[Block 1052]
སྡུག་བསྔལ་གྱི་དབང་པོ་ནི་དགེ་བ་དང་མི་དགེ་བ་ནི་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 1053]
ལུང་དུ་མ་བསྟན་པ་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་ཡིན་ནོ། །

[Block 1054]
དད་པ་ལ་སོགས་པ་ཟག་པ་དང་བཅས་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 1055]
ཟག་པ་མེད་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་དག་ཡིན་ནོ། །

[Block 1056]
གཞན་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 1057 [HEADING]]
##### དགེ་བ་དང་མི་དགེ་བ། ^2-1-4-4-0

[Block 1058]
དུ་ནི་དགེ་བ་དག་ཡིན། དུ་ནི་མི་དགེ་བ་དག་ཡིན་ཞེ་ན། རེ་ཞིག་གཅིག་ཏུ་དགེ་བ་བརྒྱད། །དད་པ་ལ་སོགས་པ་ལྔ་དང་། ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ལ་སོགས་པ་གསུམ་མོ། །

[Block 1059]
ཡིད་མི་བདེ་བ་རྣམ་གཉིས། དགེ་བ་ཡང་ཡིན་མི་དགེ་བ་ཡང་ཡིན་ནོ། །

[Block 1060]
ཡིད་དང་ཚོར༌[^463]གཞན་ནི། རྣམ་གསུམ། དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་དག་གོ། །

[Block 1061]
གཞན་ནི་རྣམ་པ་གཅིག །གཞན་དེ་ཡང༌[^464]ཞེ་ན། མིག་ལ་སོགས་པ་དང་།

[Block 1062]
བརྒྱད་པ་སྲོག་སྟེ། དེ་དག་ནི་ལུང་དུ་མ་བསྟན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1063 [HEADING]]
##### ཁམས་གང་དུ་གཏོགས་པ། ^2-1-4-5-0

[Block 1064]
དབང་པོ་འདི་རྣམས་ལས་དབང་པོ་གང་ཞིག་ཁམས་གང་དུ་གཏོགས་ཤེ་ན། དྲི་མེད་མ་གཏོགས་འདོད་པར་གཏོགས། །རེ་ཞིག་གཅིག་ཏུ་ཟག་པ་མེད་པ་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ལ་སོགས་པ་གསུམ་མ་གཏོགས་པའི་དབང་པོ་རྣམས་ནི་འདོད་པ་དང་ལྡན་པར་རིག་པར་བྱ་སྟེ། དེ་ནི་ལྡན་པ་མ་ཡིན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1065]
ཕོ་མོའི་དབང་དང་སྡུག་བསྔལ་དག །མ་གཏོགས་གཟུགས་གཏོགས། དྲི་མ་མེད་པ་ཡང་མ་གཏོགས་ཞེས་བྱ་བར་སྦྱར་ཏེ། སྡུག་བསྔལ་དག་ཅེས་བྱ་བ་ནི་སྡུག་བསྔལ་བ༌[^465]དང་ཡིད་མི་བདེ་བ་དག་གོ། །

[Block 1066]
གཟུགས་ཀྱི་ཁམས་དེ་ན་འཁྲིག་པའི་ཆོས་ཀྱི་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་དང་། མི་མཛེས་པར་བྱེད་པའི་ཕྱིར་ཕོ་དང་མོའི་དབང་པོ་དག་མེད་དོ། །

[Block 1067]
ད་ནི་ཇི་ལྟར་ན་དེ་དག་ཕོ་ཞེས་བྱ། ག་ལས་འབྱུང་། མོ་ཚངས་པ་ཉིད་བྱེད་པར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་གནས་མ་ཡིན་ཞིང་སྐབས་མེད་དེ་གནས་མེད་དོ། །

[Block 1068]
[^466]ཕོ་གང་ཡིན་པ་དེ་ནི་གནས་ཡོད་དོ། །ཞེས་གསུངས་ཏེ། ཕོའི་ངོ་བོར༌[^467]གཞན་འདོད་པའི་ཁམས་ན་ཕོ་རྣམས་ལ་ཡོད་པ་གང་ཡིན་པ་ནི་ཡོད་དོ། །

[Block 1069]
ལུས་དང་བའི་ཕྱིར་དང་། མི་དགེ་བ་མེད་པའི་ཕྱིར་སྡུག་བསྔལ་གྱི་དབང་པོ་མེད་དོ། །

[Block 1070]
རྒྱུ་ཞི་གནས་ཀྱིས་བརླན་པའི་ཕྱིར་དང་། ཀུན་ནས་མནར་སེམས་ཀྱི་གཞི་མེད་པའི་ཕྱིར་ཡིད་མི་བདེ་བའི་དབང་པོ་མེད་དོ། །

[Block 1071]
གཟུགས་ཅན་དང་། བདེ་བ་འམ་མ་གཏོགས་གཟུགས་མེད་གཏོགས། །ཕོ་དང་མོའི་དབང་པོ་དག་དང་། བདེ་བ་དག་དང་དྲི་མ་མེད་པ་ཡང་མ་གཏོགས་ཞེས་བྱ་བར་སྦྱར་རོ། །ཅི་ཞིག་ལུས་ཤེ་ན། ཡིད་དང་སྲོག་དང་བཏང་སྙོམས་ཀྱི་དབང་པོ་དག་དང་། དད་པ་ལ་སོགས་པ་ལྔ་པོ་དེ་དག་ནི་གཟུགས་མེད་པ་དང་ལྡན་པར་འདོད༌[^468]དོ། །

[Block 1072]
གཞན་དག་ནི་མེད་དོ། །

[Block 1073 [HEADING]]
##### སྤང་བར་བྱ་བ་དང་སྤང་བར་བྱ་བ་མ་ཡིན་པ། ^2-1-4-6-0

[Block 1074]
དབང་པོ་དུ་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་དག་ཡིན། དུ་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ཡིན། དུ་ནི་སྤང་བར་བྱ་བ་མ་ཡིན་པ་དག་གི༌[^469]ཡིན་ཞེ་ན། ཡིད་དང་ཚོར་བ་གསུམ་རྣམ་གསུམ། །ཚོར་བ་གསུམ་གང་ཞེ་ན། བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་རྣམས་སོ། །

[Block 1075]
གཉིས་ཀྱིས་སྤང་བྱ་ཡིད་མི་བདེ། །ཡིད་མི་བདེ་བ་ནི་མཐོང་བ་དང་བསྒོམ་པ་དང་གཉིས་ཀྱིས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1076]
དགུ་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །ཞེས་བྱ་བའི་སྐབས་ཡིན་ཏེ། མིག་ལ་སོགས་པ་དང་།

[Block 1077]
བརྒྱད་པ་སྲོག་དང་། སྡུག་བསྔལ་གྱི་དབང་པོ་ནི་བསྒོམས་པས༌[^470]སྤང་བར་བྱ་བ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 1078]
ལྔ་པོ་ནི། སྤང་བར་བྱ༌[^471]མིན་ཡང་། དད་པ་ལ་སོགས་པ་ལྔ་ནི་ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ་ཡིན་པའི་ཕྱིར་བསྒོམས་པས༌[^472]སྤང་བར་བྱ་བ་དག་ཀྱང་ཡིན་ལ། སྤང་བར་བྱ་བ་མ་ཡིན་པ་དག་ཀྱང་མ༌[^473]ཡིན་ནོ། །

[Block 1079]
གསུམ་མིན། ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ལ་སོགས་པ་གསུམ་ནི་ཟག་པ་མེད་པའི་ཕྱིར་སྤང་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་དེ། ཉེས་པ་མེད་པ་ནི་སྤང་བར་འོས་པ་མ་ཡིན་ནོ། །

[Block 1080]
རྣམ་པའི་བྱེ་བྲག་བཤད་ཟིན་ཏོ། །

[Block 1081 [HEADING]]
#### རྙེད་པ། ^2-1-5-0

[Block 1082]
ད་ནི་རྙེད་པ༌[^474]དཔྱད་པར་བྱ་སྟེ། ཁམས་གང་དུ་དང་པོ་ཉིད་དུ་དབང་པོ་རྣམ་པར་སྨིན་པ་དུ་ཞིག་རྙེད་ཅེ་ན། འདོད་པར་དང་པོར་རྣམ་སྨིན་གཉིས། །རྙེད་དེ། ལུས་ཀྱི་དབང་པོ་དང་། སྲོག་གི་དབང་པོའོ། །

[Block 1083]
དེ་དག་ཀྱང་། རྫུས་ཏེ་སྐྱེ་བས་མིན། རྫུས་ཏེ་སྐྱེ་བ་བཀག་པས་སྒོ་ང་ལས་སྐྱེ་བ་དང་། མངལ་ལས༌[^475]སྐྱེ་བ་དང་། དྲོད་གཤེར་ལས་སྐྱེ་བ་དག་གིས་རྙེད་པར་རིག་པར་བྱའོ། །

[Block 1084]
ཅིའི་ཕྱིར་ཡིད་དང་བཏང་སྙོམས་ཀྱིས༌[^476]དབང་པོ་དག་མ་ཡིན་ཞེ་ན། དེ་གཉིས་ནི་ཉིང་མཚམས་སྦྱོར་བའི་ཚེ་གདོན་མི་ཟ་བར་ཉོན་མོངས་པ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1085]
ཡང་རྫུས་ཏེ་སྐྱེ་བ་དག་གིས་དུ་ཞིག་འཐོབ་ཅེ་ན། དེ་ཡིས་དྲུག་གམ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མཚན་མ་མེད་པ་ཞིག་ཡིན་ན་སྟེ།[^477] འདི་ལྟར་བསྐལ་པ་དང་པོ་པ་རྣམས་ལྟ་བུའོ། །

[Block 1086]
དྲུག་གང་ཞེ་ན། མིག་དང་རྣ་བ་དང་སྣ་དང་ལྕེ་དང་ལུས་དང་སྲོག་གི་དབང་པོ་རྣམས་སོ། །

[Block 1087]
བདུན་ནམ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མཚན་གཅིག་པ་ཞིག་ཡིན་ན་སྟེ། འདི་ལྟར་ལྷ་ལ་སོགས་པ་དག་ནའོ། །

[Block 1088]
བརྒྱད་ཅེས་བྱ་བ་ནི་གལ་ཏེ་མཚན་གཉིས་པ་ཞིག་ཡིན་ནའོ། །

[Block 1089]
ཅི་རྫུས་ཏེ་སྐྱེ་བ་ཡང་མཚན་གཉིས་པ༌[^478]ཡོད་དམ་ཞེ་ན། ངན་སོང་དག་ན་ཡོད་དོ། །

[Block 1090]
རེ་ཞིག་འདོད་པའི་ཁམས་ན་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །
--- END BLOCKS ---
