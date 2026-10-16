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
ཞེས་བྱ་བ་ནི་མཐུན་པའི་ཟས་ཀྱིས་མ་བཟློག་པ༌[^588]དང་། མི་མཐུན་པའི་ཟས་བསྟན་པས༌[^589]ནི་སྨན་མི་ཐོགས་པ༌[^590]ཞེས་བྱ་བ་ཡིན་ཏེ། ངལ་བའི་འབྲས་བུ་ཉི་ཚེར་ཟད་དེ། དེ་ལྟར་ནད་ཉེ་བར་ཞི་བར་མི་འགྱུར་རོ། །

[Block 1052]
དེ་ལྟར་དཔེ་བསྟན་ནས་དཔེ་བསྒྲུབ་པར་བྱ་བ་དེ་བསྟན་པའི་ཕྱིར། སྦྱིན་ལ་ཞུགས་པ་བདག་གི༌[^591]སྡུག་བསྔལ་འདི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། །དཔྱད་ཀྱིས་སློན་པར༌[^592]རབ་ཏུ་མི་འགྱུར་དོགས། །ཞེས་བྱ་བ་ནི་ཕན་པར་བསྟན་པའི་དཔྱད་ཀྱིས་གསོ་བའི་ཡུལ་དུ་མི་འགྱུར་བའོ། །

[Block 1053]
དེ་བསྒྲུབ་པའི༌[^593]ཕྱིར་ཁྱོད་ཀྱིས༌[^594]ཕན་པ་བསྟན་པའང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་བསྟན་པ་ཡིན་ཏེ། ཕན་པ་བསྟན་པ་ཡང་མི་ཉན་པར་ཞེས་བྱ་བ་ནི་ཕན་འདོགས་པའི་གདམས་ངག༌[^595]མི་སྒྲུབ་པའོ། །

[Block 1054]
སེམས་ཞེས་བྱ་བ་ནི་སྦྱིན་པར་འདོད་པའི་ཡིད་དོ། །

[Block 1055]
ནད་དང་འདྲ་བ་ནི་དེའི་སྦྱིན་པའི་སེམས་ཏེ། སེམས་ལ་གནས་པར་གྱུར་པས་དེའི་སྒྲར་བརྗོད་དེ།

[Block 1056 [VERSE]]
ཇི་ལྟར་སྒྲ་འབྱིན་ཞེས་བྱ་བ་དེ་བཞིན་ནོ། །
ནོར་ནི་འཁོར་གསུམ་ཁྱད་པར་རྒྱུ་ཡིན་ཏེ། །

[Block 1057]
ཞེས་བྱ་བའི་ཚིག་གང་སྔར་བསྟན་པ་དེ་ལས་འདི་བརྩམས་པ་ཡིན་ཏེ། །སྦྱིན་པ་སྡིག་པར་འགྱུར་ཞེས་གང་སྨྲས་ཤིང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་དེ་སྦྱིན་པ་སྡིག་པར་འགྱུར་ཞེས་གང་སྨྲས་པ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་སྨྲས་པ་ཡིན་ཞེ་ན། ནོར་ནི་འཁོར་གསུམ་གྱི་རྒྱུ་ཡིན་ཏེ། སྦྱིན་པས་ཆུད་ཟོས་པར་འགྱུར་ཞིང་དེའི་རྒྱུས་ཆོས་ཀྱང་ཉམས་པར་འགྱུར་ལ། ནོར་ཡང་ཆོས་ཀྱི་ཁྱད་པར་རྒྱུ་ཡིན་ཞེས་བྱ་བ་ཡིན་ཏེ། ནོར་ནི་འཁོར་གསུམ་གྱི་རྒྱུ་ཡིན་ནོ་ཞེས་བཤད་པར་གྱུར་པའོ། །

[Block 1058]
གལ་ཏེ་སྦྱིན་པ་སྡིག་ཡིན་ན་ནི་གཞན་དུ་ན་ནོར་ཇི་ལྟར་སྡིག་པར་འགྱུར་བ་མ་ཡིན་ཏེ། སྦྱིན་པ་ནི་ཆོས་མ་ཡིན་པར་བཤད་པས་སོ། །

[Block 1059]
གཏེར་དུ་སྦས་པའམ། འཇིག་པར་འགྱུར་བ་དེ་ཆོས་སུ་འགྱུར་རོ་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར། དེ་ནི་གཏེར་སྦས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་སྨོས་པ་ཡིན་ནོ། །

[Block 1060]
དེ་བས་ན་ཉེ་བར་ལོངས་སྤྱོད་པས་ན་ཆོས་ཀྱི་རྒྱུར་གྱུར་པ་ཡིན་ཏེ། ཀུན་ཏུ་འཛིན་པ་ནི་མ་ཡིན་ནོ། །

[Block 1061]
ཉེ་བར་ལོངས་སྤྱོད་པར་འདོད་པའི་ཚུལ་དང་། འདོད་པའི་རྒྱུར་ནོར་གྱི་དབང་དུ་བྱས་པ་མ་ཡིན་ཞིང་ཆོས་ཀྱི་རྒྱུ་ཡང་མ་ཡིན་ཏེ། བར་དུ་གཅོད་པར་བྱེད་པས་སོ། །

[Block 1062]
གཏེར་སྦས་ཞེས་བྱ་བ་ནི་ནོར་གཏེར་དུ་སྦས་ན་ཅི་ཞིག་ཆོས་ཀྱི་རྒྱུར་གྱུར་ཞེས་པའོ། །

[Block 1063]
འོན་ཏེ་འཇིག་པ་སྟེ་འཇིག་པ་ནི་རྐུན་པོ་ལ་སོགས་པ་རྣམ་པ་ལྔས་སོ། །

[Block 1064]
མངོན་སྟོན་ཕྲོགས་པར་གྱུར་པ་ནི་མངོན་སུམ་དུའོ། །

[Block 1065]
རྐུན་མ་སྨོས་པས་རྒྱལ་པོ་ལ་སོགས་པ་བཟུང༌[^596]སྟེ། ལྔ་པོ་དེ་དག་ཀྱང་མ་བྱིན་པར་ལེན་པར་ཆོས་མཐུན་པས་སོ། །

[Block 1066]
དེ་ལྟར་ལྔ་དང་ཐུན་མོང་དུ་གྱུར་པ་ཡིན་པས་འཇིག་པར་བསྟན་ཏོ། །

[Block 1067]
གང་གོང་དུ་བསྟན་པའི།

[Block 1068 [VERSE]]
སྦྱིན་པ་ཚུལ་མིན་མི་བྱེད་ལེན་པ་པོ། །
ཞེས་བྱ་བ་དག་གི་ལན༌[^597]བསྟན་པའི་ཕྱིར།
ནོར་སྦྱིན་པ་ནི་དམྱལ་བར་འགྲོ་བ་དང་། །

[Block 1069]
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 1070]
དེ་བསྒྲུབ་པའི༌[^598]ཕྱིར། །ཁྱོད་ཀྱི་ཚིག་དེ་གཞན་དུ་མ་གྱུར་ཅིག །ཅེས་བྱ་བའི་ཚིགས་བཅད་བསྟན་པའོ། །

[Block 1071]
ཕན་པར་འདོད་པ་བཞིན་བརྟན་པར༌[^599]བྱ་བའི་ལག་པ་བརྐྱང་སྟེ་ཞེས་བྱ་བ་ནི༌[^600]ཕན་ཞིང་བརྟན་པའི་ལག་པས་སོ། །

[Block 1072]
ཕན་པར་སྨྲས་ན་ཡང་ལེགས་པར་རྟོགས་ལ་གང་དུ་དགའ་བར་སོང་ཤིག་པ་སྟེ། སྦྱིན་པ་ལས་ལོག་པར་གྱིས་ཤིག་པའོ། །

[Block 1073]
བརྫུན་དུ་སྨྲས་ན་ཡང་ལེགས་པར་རྟོགས་ལ་གང་དུ་དགའ་བ་དེར་སོང་ཤིག་པ་སྟེ། སྦྱིན་པ་ལ་འཇུག་པར་གྱིས་ཤིག་པའོ། །

[Block 1074]
དེ་གཉིས་ཀྱིས་ཅིར་འགྱུར་ཞེ་ན། དེ་སྨྲས་པ། ཕན་པར་སྨྲས་པ་འདི་ལེགས་པར་རྟོགས་ལ་གལ་ཏེ་སྦྱིན་པ་ལས་ལྡོག་ན་ནི་བདེ་བ་དང་ལྡན་པ་ཡིན་ཏེ། གུས་བཅས་དྲན་པར་གྱིས་ཞེས་པའོ། །

[Block 1075]
གལ་ཏེ་བརྫུན་དུ་སྨྲས་ན་ཡང་ལེགས་པར་རྟོགས་ལ་སྦྱིན་པ་ལས་མ་ལོག་ན་ནི་འགྱོད་བཞིན་ང་ནི་དྲན་པར་བྱས་སོ༌[^601]ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 1076]
གང་སྔར་བསྟན་པའི་བརྫུན་དུ་སྨྲས་པ་ལ་ལེགས་པར་རྟོགས་ལ་སྦྱིན་པ་ལས་མ་ལོག་པ་ནི། འགྱོད་བཞིན་ང་ནི་དྲན་པར་བྱོས། །ཞེས་བྱ་བ་དེའི་ལན་བརྩམ་པའི༌[^602]ཕྱིར། ཕོངས་པ་རྣམས་ཀྱིས་བག༌[^603]སྤོབས་ཏེ་བསླངས་པ་ལ། ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདི་ཡིན་ནོ། །

[Block 1077]
དེས༌[^604]ན་ཕོངས་པ་རྣམས་ཀྱིས་བག་ཕབ་སྟེ་བསླངས་པ་གང་ཡིན་པ་དེ་ནི་ཕོངས་པ་རྣམས་ཀྱིས་བག་ཕབ་སྤོབས་ཏེ་བསླངས་པའོ།[^605] །མི་བཟད་པ་ཡང་ཡིན་ལ་མེ་ལྕེ་ཡང་ཡིན་པས་མི་བཟད་མེ་ལྕེ་འབར་བའོ། །

[Block 1078]
མི་བཟད་མེ་ལྕེ་འབར་བ་དེས་ཕོག་ནས་སྤྱིའུ་ཚུགས་སུ་ལྷུང་ཡང་ངོ་། །དེའི་བསོད་ནམས་ཀྱི་མཐུ་ཡིས་ཞེས་བྱ་བ་ནི༌[^606]གང་གི་བསོད་ནམས་ཀྱི་མཐུས༌[^607]ཞེ་ན། སྔོན་བྱས་པའི་སྟེ༌[^608]གང་གོང་དུ་བསྟན་པའི་བདག་གི་སྐལ་བའི་མཐུ་ལ་བརྟེན་པ་དང་། སྦྱིན་པ་ལ་ཡང༌[^609]ཉེས་དམིགས་མེད་པར་ཡང་ཤེས་པ་དང་། འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་ལས་ཀྱི་འབྲས་བུ་ལ་ཡིད་ཆེས་པའི་མཚན་ཉིད་ཀྱི་བསོད་ནམས་ད་ལྟར་བྱུང་བ་དང་། དེ་གཉི་གའི་བསོད་ནམས་ཀྱི་མཐུས༌[^610]སོ། །

[Block 1079]
བསོད་ནམས་ཁྱད་པར་ཅན་ལས་བྱུང་བའི་ཞེས་བྱ་བ་འདིས་ནི་གཉི་ག་བསྟན་ཏེ།

[Block 1080 [VERSE]]
དེས་ན་ཁྱད་པར་ཅན་ཞེས་སྨོས་སོ། །
ད༌[^611]ནི་ཆར་འབེབས་འབར་བར་བྱེད། །

[Block 1081]
ཅེས་བྱ་བ་ནི་འཕགས་པ་དེའི་རྫུ་འཕྲུལ་སྟོན་པ་ཡིན་ནོ། །

[Block 1082]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ཚོང་དཔོན་གྱི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 1083 [HEADING]]
## ཚོང་དཔོན་ཟིལ་གྱིས་མནོན་པའི་སྐྱེས་པའི་རབས། ^5-0

[Block 1084]
ཚུལ་ཁྲིམས་དང་གཏོང་བ་ལ་སོགས་པའི་ཚིག་འདི་དག་གིས་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་དང་མ་འོངས་པ་དང་། ད་ལྟར་གྱི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 1085]
གཏོང་བ་དང་ཚུལ་ཁྲིམས་རྣམ་པ་གཉིས་ནི་ད་ལྟར་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཏེ། སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་ཀྱི་མཚན་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1086]
[^612]མང་དུ་ཐོས་པ་ཞེས་སྨོས་པ་ནི་ད་ལྟར་བྱུང་བའི་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །

[Block 1087]
ཆོ་རིགས་དང་དུལ་བ་ཞེས་སྨོས་པ་ནི་འདས་པའི་ཚུལ་ཁྲིམས་དང་དུལ་བ་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུའོ། །

[Block 1088]
འདས་པའི་སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ནི་སྦྱོར་བ༌[^613]ཕུན་སུམ་ཚོགས་པ་ཉིད་དོ། །ཤེས་པ་ཞེས་བྱ་བས་ནི་འདས་པའི་ཚེའི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུའོ། །

[Block 1089]
འདི་དག་གིས་དྲེགས་པ་མེད་དེ་ཞེས་པ༌[^614]སྒྱུ་རྩལ་དུ་མ་དང་སྐད་ཀྱི་རྣམ་པ༌[^615]ཤེས་ཀྱང་ངོ་། ། འདི་དག་ནི་གོང་དུ་བཤད་པའི་སྦྱིན་པའི་ཁྱད་པར་གྱི་དོན་ནོ། །

[Block 1090]
གློ་བུར་བ་ཐམས་ཅད་ལ་ཞེས་བརྩམས་ཏེ། སྦྱིན་པ་པོའི་གཙོ་བོར་གྱུར་པ་དེ་རྒྱུ་དེས་ན་འཇིག་རྟེན་ལ་ཕན་པའི་ཕྱིར་ཞུགས་པའོ། །
--- END BLOCKS ---
