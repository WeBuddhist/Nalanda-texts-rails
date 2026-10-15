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

[Block 1091]
དེ་ནས་དེ་མ་ཐག་ཏུ་སྔར་སོང་སྟེ་ཕྱག་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ནས་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་བྱ་བ་བསྒྲུབ་པའི༌[^775]རྗེས་ལ་སྟེ། མཆོད་རྟེན་ལ་ཕྱག་བྱ་བ་ནི་ངེས་པའོ། །

[Block 1092]
གནས་པ་བདེ་བས༌[^776]སྔར་ལུས་ཀྱི་བྱ་བ་བསྒྲུབས་ནས་ཞེས་བྱ་བ་འདི་ལས་ཤིན་ཏུ་སྔར་གནས་ལ་རྟོགས་པར་བྱའོ། །

[Block 1093]
གདོང་རྣམ་པར་དག་པས་ཕྱག་བྱེད་པ་ལ་འདོད་པར་བྱ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1094]
གཞན་དུ་ན༌[^777]གནས་པ་ལ་ཕོངས་པ་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 1095]
འདག་རྫས་དང་སོ་ཤིང་དབུལ་ལོ་ཞེས་བྱ་བ༌[^778]ཤེས་པར་བྱ་བ་ཡང་མ་ཡིན་ཏེ། ནད་པ་ལ་སོགས་པ་ལ་གནང་བ་སྦྱིན༌[^779]པའི་ཕྱིར་རོ། །

[Block 1096]
བསྙུན་གསོལ་ལོ། །

[Block 1097]
འདག་རྫས་དང་སོ་ཤིང་དབུལ་ལོ། །

[Block 1098]
ཚང་མང་བལྟས་ཏེ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་གིས་དེར་བཟའ་བ་དང་བཏུང་བ་ཉེ་བར་བརྟགས་ཏེ་དེ༌[^780]བརྗོད་པ་ལའོ། །

[Block 1099]
དགའ་བ་བསྟབས་པ་ཉིད་དུ་ཡིད་ལ་བྱའོ་ཞེས་བྱ་བ་ནི་བརྗོད་པ་ལ་གང་དུ་འདི་དགའ་བ་ཡང་དག་པར་སྟོན་པར་བྱེད་པའི་དགའ་བ་དེ་ལ་དབུལ་བར་བགྱིའོ་ཞེས་བྱ་བས་དེ་ལྟར་ཡིད་ལ་བྱེད་པའོ། །

[Block 1100]
ལྷུང་བཟེད་བཀྲུ་བར་བྱའོ། །

[Block 1101]
གལ་ཏེ་བསོད་སྙོམས་པ་ཞིག་ཡིན་ན་གསིལ་བྱེད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་སྒྲ་སི༌[^781]ལི་ལི་བྱེད་པ་གསིལ་བྱེད་དེ་གཉིས་པའི་མིང་ཅན་ལ་བཀུར་བར་བྱའོ། །

[Block 1102]
གསིལ་བྱེད་དེ་སྐྲ༌[^782]བྱེད་པས་ན་གསིལ་བྱེད་དོ། །

[Block 1103]
གལ་ཏེ་དགོས་པ་ཡོད་ན་ཆུ་ཚགས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་བཀྲུ་བར་བྱའོ་ཞེས་བྱ་བ་དང་འབྲེལ་ལོ། །

[Block 1104]
སླར་དོགས་པ༌[^783]ནི་དུས་གཅིག་ཏུ་ཕྱི་རོལ་ཉིད་དུ་བཟའ་བར་བྱ་བར་འགྱུར་རོ། །

[Block 1105]
གལ་ཏེ་དེ་ཡང་ཡིན་ན་ཞུ་བར་བྱའོ། །

[Block 1106]
གལ་ཏེ་བཟོད་ཅིང་འདོད་ན་དེ་ཉིད་དང་ལྷན་ཅིག་ཏུ་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་གནས་པ་དེ་ཡང་བསོད་སྙོམས་པར་གྱུར་ན་དེ་ནས་བསོད་སྙོམས་ལ་འཇུག་པའི་དོན་དུ་བཟོད་ཅིང་ལྷན་ཅིག་འཇུག་པ་དག་གིས་སོ། །

[Block 1107]
འདི་ལ་མངོན་པར་འདོད་པ་ཅི་ཞིག་ཅེས་བྱ་བ་ངེས་པར་ཤེས་པའི་དོན་དུ་འདྲི་བ་ནི་གལ་ཏེ་བཟོད་ན་ཞེས་བྱ་བ་ལ། གནམ༌[^784]ལ་གནས་པ་དང་ལྷན་ཅིག་ཏུ་ཞུགས་ན༌[^785]མངོན་པར་འདོད་ན་དེ་ཉིད་ནི་གནས་དང་ལྷན་ཅིག་ཏུ་འཇུག་པ་སྟེ། ཉམ་ང་བ་ལ་སོགས་པར་མདུན་དུ་འགྲོ་བར་བྱའོ། །

[Block 1108]
བསོད་པ་དེ་ལ་བདར་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་བསོད་སྙོམས་བསོད་པ་ཞིག་རྙེད་ན༌[^786]འདི་ལ་ཕུལ་ཅིག་ཅེས་བྱ་བས་དེ་ལ་བསྔོ་བར་བྱའོ། །

[Block 1109]
གལ་ཏེ་མ་འགྲོགས་ན་ཞེས་བྱ་བ་ནི་ཞུགས་པའོ། །

[Block 1110]
འོངས་ནས་བསྟན༌[^787]པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསོད་སྙོམས་ལའོ། །ཇི་ལྟ་བུར་དབུལ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཆེས་མཆོག་ཏུ་གྱུར་པའི་དབུལ༌[^788]བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཟའ་བ་དང་བཅའ་བར༌[^789]གྱུར་པ་དེ་ནི་གནས་ལ་འདི་བཞེས་ཤིག༌[^790]ཅེས་དབུལ་ཞིང་བསྟབས་པར་བྱའོ། །

[Block 1111]
དེས་ཐམས་ཅད་ལ་ཚོད་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་སོ། །

[Block 1112]
ཆུ་སྣོད་དགང་བར་བྱའོ། །

[Block 1113]
དུས༌[^791]བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བཟའ་བའི་དུས་ལའོ། །

[Block 1114]
ཟན་ཟོས་ནས་ལྷུང་བཟེད་ལ་སོགས་པ་བཀྲུ་བར་བྱའོ། །

[Block 1115]
དེ་དག་གཞག་པར་བྱའོ། །

[Block 1116]
མཆོད་རྟེན་ལ་ཕྱག་འཚལ་བ་ན་འདག་རྫས་དང་ཆུ་ལ་སོགས་པ་དབུལ་ལོ། །

[Block 1117]
རྐང་པ་བཀྲུ་བར་གཏོགས་པ་ལ་ནན་ཏན་བྱའོ། །

[Block 1118]
མལ་དང་སྟན་བཤམ་པར༌[^792]བྱའོ། །

[Block 1119]
ཤམ་ཐབས་ཀྱི་གཟན་དབུལ་བར་བྱའོ། །

[Block 1120]
ཤམ་ཐབས་བླང་བར་བྱའོ། །

[Block 1121]
རྐང་པའི་ཆུ་དང་རྟེན་དང་ཆོལ་ཟངས་དབུལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། རྐང་པའི་ཞེས་བྱ་བའི་སྒྲ་ནི་ཆུ་དང༌[^793]རྟེན་དག་གིས་སོ་སོར་མངོན་པར་འབྲེལ་པ་སྟེ། རྐང་པའི་ཆུ་ལ་སོགས་པ་དབུལ་བར་བྱ་བ་ནི་རྐང་པ་བཀྲུ་བའི་ཆུ་དང་རྟེན་དང་ཆོལ་ཟངས༌[^794]རྣམས་དབུལ་བར་བྱ་བའོ།[^795] །མཆིལ༌[^796]ལྷམ་གཉིས་ཕྱིའོ། །

[Block 1122]
སྒྲུབ་པར་བྱེད་པ་ཉིད་དུ་མ་བསྒོས་པར་ཕྱག་མ༌[^797]ཐོགས་པ་མཐོང་ན་ལས་ཆུང་བར་བྱའོ། །

[Block 1123]
གོས་འཚེམ་པ་ཉིད་དུ་མ་བསྐོས་པར་ཁས༌[^798]ཐོགས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མཐོང་ནས་ལས་ཆུང་བར་བྱའོ་ཞེས་བྱ་བ་རྗེས་སུ་སྦྱར་རོ། །

[Block 1124]
སྒྲུབ་པར་བྱེད་པ་ཉིད་དུ་བསྐོས་པའམ་གོས་འཚེམ་པ་ཉིད་དུ་བསྐོས་པ༌[^799]ལས་ཆུང་བར་མ་བྱས་ཀྱང་སྐྱོན་མེད་དོ། །

[Block 1125]
རུང་བར་བྱ་བ་དང་སྔོ་ཆུང་ངུ༌[^800]བརྔ་བ་དང་མེ་ཏོག་དང་འབྲས་བུ་བཏོགས་པ་དང་། སོ་ཤིང་ཉེ་བར་བསྒྲུབ་པ་ལ་སོགས་པ་ལ་ཡང་དགེ་ཚུལ་བསྐོའོ་ཞེས་བྱ་བ་ནི་གནས་ཀྱི་སླད་དུ་བྱའོ་ཞེས་བྱ་བ་དོན་གྱིས་ཤེས་སོ། །
--- END BLOCKS ---
