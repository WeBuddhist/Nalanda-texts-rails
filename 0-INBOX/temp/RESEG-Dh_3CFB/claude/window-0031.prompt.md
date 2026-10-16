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
མེད་པ་སྟེ་ནུས་པ་མེད་པ་ནི་ཇི་ལྟར་རྒྱུ་མཚན་དུ་འགྱུར། དངོས་པོའི་དེ་ཉིད་ནི་བྱ་བ་བྱེད་པའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1087]
དེ་བས་ན་འདས་པ་དང་མ་འོངས་པའི་ལས་འགགས་པ་དང་ངོ་བོ་མ་ཐོབ་པ་ཅན་གྱི་རྒྱུ་མཚན་མ་ཡིན་ནོ། །

[Block 1088]
བསལ་བ་ལ་སོགས་པ་གཞན་དག་ཀྱང་མི་འདོད་པའི་ཕྱིར། དེ་དག་ནི་རྒྱུ་མཚན་མེད་པ་ཅན་དུ་འགྱུར་རོ། །

[Block 1089]
དེ་ལྟར་ན་རིགས་ཀྱང་གྲུབ་པ་མ་ཡིན་ཏེ། དེ་ནི་ཤེས་པ་དང་བརྗོད་པ་དག་གི་མཚན་ཉིད་དུ་འདོད་པའི་ཕྱིར་རོ། །

[Block 1090]
གལ་ཏེ་ནུས་པ་འཚེད་པ་པོ་ལ་སོགས་པའི་སྒྲའི་རྒྱུ་མཚན་མིན༌[^902]གྱི་ལས་དང་སྤྱི་ནི་མ་ཡིན་ཞེ་ན། རྗེས༌[^903]འགྲོ་མེད་ཕྱིར་ནུས་པའང་མིན། །འཚེད་པ་པོ་ལ་སོགས་པ་དག་གི་ནུས་པ་ཞེས་བྱ་བ་གཞན་ཅུང་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། འདི་ཉིད་ནི་འཚེད་པ་ལ་སོགས་པའི་དོན་གྱི་བྱ་བ་ལས་ཉེ་བར་སྦྱོར་བ་ཡིན་པས་ན་རྫས་ནི་ཉེ་བར་སྦྱོར་བ་མ་ཡིན་པར་ཐལ་བའི་ཕྱིར་རོ། །

[Block 1091]
གལ་ཏེ་དེ་ནི་དེའི་ཉེ་བར་སྦྱོར་བ་ཡིན་ནོ་ཞེ་ན། ད་ནི་ནུས་པ་ཅི་ཞིག་བྱ་སྟེ། ནུས་པ་ལ་ཉེ་བར་སྦྱོར་བའི་ཕྱིར། ནུས་པ་གཞན་ཐ་དད་པ་ཁས་ལེན་ན་ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར། རྫས་ཁོ་ན་ཉེ་བར་སྦྱར་བ༌[^904]ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1092]
དེས་ནི་ནུས་པ་ལ་ཉེ་བར་སྦྱོར་ན་དོན་གྱི་བྱ་བ་ཁོ་ན་ལ་ཉེ་བར་སྦྱོར་བ་ཅིའི་ཕྱིར་དེ་ལྟར་མི་འདོད་དེ། བར་དུ་ནུས་པ་དོན་མེད་པས་ཅི་ཞིག་བྱ། དེ་བས་ན་ནུས་པ་ཞེས་བྱ་བ་ནི་དེའི་འབྲས་བུ་ཅན་གྱི་རྫས་ཁོ་ན་ཡིན་ནོ། །

[Block 1093]
དེ་ཡང་རྗེས་སུ་འགྲོ་བ༌[^905]མེད་ཕྱིར་ཏེ། དེ་ལ་རྗེས་སུ་འགྲོ་བ་ཅན་གྱི་སྒྲར་མི་འགྱུར་རོ། །

[Block 1094 [VERSE]]
གལ་ཏེ་འཚེད་པོ༌[^906]སོགས་སྤྱི་ཡིན། །
དང་པོར་དེ་ནི་ཡོད་ཉིད་སོགས། །
བཞིན་དུ་བསལ་འགྱུར་ཅི་སྟེ་མིན། །
ཁྱད་པར་མེད་ཕྱིར་ཕྱིས་མི་འགྱུར། །

[Block 1095]
ཅི་སྟེ་ཡང་འཚེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་སྤྱི་འགའ་ཞིག་ཡོད་པ་ཡིན་ན་ཡོད་པའི་དོན་ལ་འཕྲོད་པ་འདུ་བ་དེ་ནི་རེས་འགའ་བ་ཉིད་མ་ཡིན་པའི་ཕྱིར། དེ་ནི་དང་པོ་ཉིད་ན་ཡོད་པ་ཉིད་ལ་སོགས་པ་བཞིན་དུ་བསལ་བར་འགྱུར་རོ། །

[Block 1096]
དོན་ལ་འཕྲོད་པ་འདུ་བའི་ཆོས་ཅན་གྱི་སྤྱི་ཇི་སྙེད་པ་དེ་དག་ནི་འདིའི་སྐྱེ་བ་དང་ལྷན་ཅིག་ཏུ་འཕྲོད་པ་འདུ་བ་དག་ཡིན་ནོ་ཞེས་བྱ་བའི་གཞུང་ཡིན་ནོ། །

[Block 1097]
[^907]དེ་ལས་འདས་པ་དེ་ནི་ཁྱད་པར་མེད་པའི་ཕྱིར། [^908]ཕྱིས་ཀྱང་དེ་དང་འཕྲོད་པ་འདུ་བར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 1098]
དེ་དང་འབྲེལ་པའི་རང་བཞིན་དང་མི་མཐུན་པའི་ཕྱིར། དེ་ནི་དེའི་དང་པོར་ཡོད་པ་མ་ཡིན་ལ་དེ་ཉིད་ཀྱང་རང་བཞིན་དུ་གནས་པ་འདིའི་ཕྱིར། འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ནི་རྟོགས་པར་དཀའོ། །

[Block 1099]
བྱ་བ་ཕན་འདོགས་ལྟོས་བསལ་བྱེད།[^909] །

[Block 1100 [VERSE]]
ཡིན་ཡང་འགྱུར་མེད་ལྟོས་པ་མེད། །
འདི་ནི་ཕུལ་བྱུང་ཡོད་ན་ཡང་། །
སྐད་ཅིག་ཉིད་ཕྱིར་བྱ་གང་ལས། །

[Block 1101]
གལ་ཏེ་ཕན་འདོགས་པར་བྱེད་པའི་ལས་ལ་ལྟོས༌[^910]ནས་རྫས་ཀྱི་འཚེད་པ་པོ་ཉིད་ལ་བསལ་བར་བྱེད་པ་ཡིན་ནོ་ཞེ་ན། རང་བཞིན་བརྟེན་པ་འདི་ནི་ཕུལ་དུ་དབྱུང་དུ་མེད་པའི་ཕྱིར་ཁྱད་པར་དུ་བྱེད་པ་མེད་པ་ལ་ལྟོས་པ་ཅི་ཞིག་ཡོད། ཕུལ་དུ་དབྱུང་དུ་ཡོད་ན་ཡང་ལས་ནི་སྐད་ཅིག་མ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1102]
སྐད་ཅིག་རེ་རེ་ལ་ཕུལ་དུ་དབྱུང་བའི་རང་བཞིན་དུ་གྱུར་པ་གཞན་དང་གཞན༌[^911]འབྱུང་བའི་ཕྱིར། དེ་ཡང་སྐད་ཅིག་མར་འགྱུར་རོ། །

[Block 1103]
དེ་བས་ན་རང་གི་སྐྱེ་བའི་གནས་འཇིག་པ་ཅན་གྱི་བྱ་བ་གང་ལས་གང་ལ་ལྟོས་པ་བསལ་བར་བྱེད་པར་འགྱུར། འོ་ན་ད་ནི་ཇི་ལྟར་དངོས་པོ་གཅིག་ཡོད་པ་མ་ཡིན་ན། དངོས་པོ་ནི་ཤེས་པ་དང་སྒྲ་དག་གི་རྗེས་སུ་འགྲོ་བ་ཅན་ལ་འཇུག་པར་འགྱུར། དཔེར་ན་འཚེད་པ་པོ་ལ་སོགས་པ་དག་ལ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1104]
དེ་ཉིད་ལ་འདི་ཞེས་སེམས་པ་མ་ཡིན་ནམ། ཇི་ལྟར་དེ་དག་ལ་ཡང་ཡིན་ཞེ་ན། ཇི་ལྟར་དེ་དག་ལ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་དེ་དག་དཔྱད་ཟིན་ཏོ། །

[Block 1105]
དེ་བས་ན་ཅིའི་ཕྱིར་དེ་དག་རྒྱུ་མཚན་མེད་པ་ཅན་དུ་མི་འགྱུར། རྒྱུ་མཚན་མེད་པ་ཅན་ནི་མ་ཡིན་ནོ། །

[Block 1106]
འོ་ན་ཅི་ཡིན་ཞེ་ན། ཕྱི་རོལ་གྱི་དེ་ཉིད་ནི་རྒྱུ་མཚན་མ་ཡིན་ཏེ། འདི་ལྟར་བདག་ཉིད་ཇི་ལྟ་བའི་བག་ཆགས་རབ་ཏུ་སད་པ་ལས་རྣམ་པར་རྟོག་པ་སྐྱེ་བ་དེ་ལས་སྒྲ་དག་འབྱུང་བ་ཡིན་གྱི། རྣམ་པར་རྟོག་པ་དང་བརྗོད་པ་དག༌[^912]ནི་དངོས་པོ་ཡོད་པ་ཉིད་ལ་བརྟེན་པ་ཡང་མ་ཡིན་ནོ་ཞེས་དེ༌[^913]ནི་མང་དུ་དཔྱད་ཟིན་ཏོ། །

[Block 1107]
བདག་ཉིད་ཀྱི་གཞུང་ལུགས་ཇི་ལྟ་བ་བཞིན་གྱི་བག་ཆགས་ཀྱི་དབང་གིས་འགལ་བའི་ངོ་བོ་གཅིག་ཏུ་བསྡུས་པས་གཞན་དང་གཞན༌[^914]མཐོང་བ་ན་ཡང་རྗེས་སུ་འགྲོ་བ་ཅན་དེ་དག་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1108]
དེ་ལ་དེའི་རྒྱུའི་རང་བཞིན་འགའ་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། ཕན་ཚུན་འགལ་བ་ནི་གཅིག་ལ་ཅིག་ཅར་གནས་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1109]
འོ་ན་ནི་མ་ངེས་པར་འགྱུར་བ་དེ་རྒྱུ་མཚན་མེད་པར་ཡོད་པ་ནི་འགའ་ཞིག་ཏུ་ཡོད་པ་དང་འགའ་ཞིག་ཏུ་མེད་པ་ཞེས་བྱ་བར་ངེས་པར་འོངས་པ་མ་ཡིན་ནོ། །

[Block 1110]
དེ་དག་རྒྱུ་མཚན་མེད་པ་ཅན་ནི་མ་ཡིན་ཏེ། བག་ཆགས་ཀྱི་ཁྱད་པར་རྒྱུ་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1111]
ཕྱི་རོལ་དེ་ལྟ་བུར་གྱུར་པ་སྣང་བ༌[^915]ཡང་མ་ཡིན་ནོ་ཞེས་སྨྲས་ཀྱི། ཡོད་པ་མ་ཡིན་གྱི༌[^916]དེ་ལ་མི་འགྱུར་བ་ནི་མ་ཡིན་ཏེ། རྨི་ལམ་དང་རབ་རིབ་ཅན་དག་གིས་དམིགས་པའི་དོན་དང་དངོས་པོ་མེད་པ་དང་། གཞུང་ལུགས་ཀྱི་བག་ཆགས་ཀྱིས་སྒྲོ་བཏགས་པའི་ངོ་བོ་ཁྱད་པར་ཅན་དག་ལ་དེ་ལྟ་བུའི་རྟོག་པ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1112]
དེ་དག་ནི་ཡོད་པ་མ་ཡིན་པ་དེ་དག་ལ་སྐྱེ་བའི་ཕྱིར་ཐམས་ཅད་ལ་རྣམ་པ་ཐམས་ཅད་དུ་མ་ཡིན་ཏེ། རྣམ་པར་དབྱེ་བ་ཉིད་ཀྱིས་དེ་ལྟར་དམིགས་པ་དག་ལ༌[^917]རྣམ་པར་རྟོག་པའི་ཕྱིར་རོ། །

[Block 1113]
ཁོ་བོ༌[^918]ཅག་གིས་འདིར་རང་བཞིན་གྱིས་ཀྱང་ཤེས་པ་གཅིག་གི་འབྲས་བུ་ཅན་འགའ་ཞིག་ངོ་བོ་ཉིད་ཐ་དད་པའི་ཕྱིར་ཞེས་བྱ་བ་ཅུང་ཞིག་བསྟེན༌[^919]ཏོ། །

[Block 1114]
གཞན་ཡང་།

[Block 1115 [VERSE]]
ཐ་དད་མཚུངས་པ་ཡིན་ན་རིགས། །
ཉེ་བ་གང་གིས་འགའ་ཞིག་ལ། །
རབ༌[^920]འཇུག་གཞན་ལ་མིན་དེ་ཉིད། །
སྒྲ་དང་ཤེས་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 1116]
ཞེས་བྱ་བ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 1117 [VERSE]]
གལ་ཏེ་ལྡོག་པ་སྤངས་པ་ཡི། །
དངོས་པོའི་རྗེས་འགྲོ་གཞན་ཡོད་མིན། །
གཅིག་གི་འབྲས་བུ་གཞན་གྱིར་ནི། །
མི་འགྱུར་ཤིན་ཏུ་ཐ་དད་ཕྱིར། །

[Block 1118]
གལ་ཏེ་ལྡོག་པ་མ་གཏོགས་པར་རྗེས་སུ་འགྲོ་བ་ཅན་གྱི་རང་བཞིན་འགའ་ཞིག་གིས་དངོས་པོ་དེ་དག་སྟོང་པ་ཡིན་ནོ། །

[Block 1119]
[^921]མང་པོ་དེ་དག་ནི་འབྲས་བུ་གཅིག་ཏུ༌[^922]མི་འགྱུར་རོ། །

[Block 1120]
དེའི་སྐྱེད་པར་བྱེད་པའི་རང་བཞིན་གང་ཡིན་པ་དེ་ནི་གཞན་ལ་མེད་ཅིང་ཡོད་པ་གང་ཡིན་པ་དེ་ནི་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་ཏེ། ལྡོག་པ་ནི་རང་བཞིན་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1121]
སྐྱེད་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ཉིད་དངོས་པོ་ཡིན་ལ་སྐྱེད་པར་བྱེད་པ་དེ་ཡང་གཞན་ལ་མེད་པའི་ཕྱིར། གཞན་གྱིས་བསྐྱེད་པར་མི་འགྱུར་རོ། །

[Block 1122]
གལ་ཏེ་དེ་ནི་སྐྱེད་པར་བྱེད་པའི་རང་བཞིན་གང་ཡིན་པ་དེ་ནི་གཞན་གྱིར་ཡང་འགྱུར་ན། དེའི་རང་བཞིན་དེས་དེ་ལ་ཐ་དད་པར་མི་འགྱུར་བའི་ཕྱིར། རང་བཞིན་གྱིས་རྗེས་སུ་འགྲོ་བ་ཡོད་དོ་ཞེ་ན།

[Block 1123 [VERSE]]
གལ་ཏེ་བདག་ཉིད་གཅིག་པ་ཡིས། །
དུ་མ་འབྲས་བུ་གཅིག་བྱེད་ན། །
བདག་ཉིད་གཅིག་ལའང་དེ་ཡོད་ཕྱིར། །
ལྷན་ཅིག་བྱེད་པ་དོན་མེད་འགྱུར། །

[Block 1124]
གལ་ཏེ་རང་བཞིན་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར། དུ་མ་གཅིག་བྱེད་པ་ཡིན་ན་དེ་དག་གི་ཐ་དད་པ་མེད་པའི་རང་བཞིན་དེ་ནི་གཅིག་ཉེ་ཡང་ཡོད་པས་རྒྱུ་དང་མ་བྲལ་བའི་ཕྱིར། གཅིག་ཀྱང་སྐྱེད་པར་བྱེད་པར་འགྱུར་རོ། །

[Block 1125]
འདི་ལྟར།
--- END BLOCKS ---
