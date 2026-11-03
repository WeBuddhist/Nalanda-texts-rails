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
[^612]མང་དུ་ཐོས་པ་ཞེས་སྨོས་པ་ནི་ད་ལྟར་བྱུང་བའི་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །

[Block 1087]
ཆོ་རིགས་དང་དུལ་བ་ཞེས་སྨོས་པ་ནི་འདས་པའི་ཚུལ་ཁྲིམས་དང་དུལ་བ་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུའོ། །

[Block 1088]
འདས་པའི་སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ནི་སྦྱོར་བ༌[^613]ཕུན་སུམ་ཚོགས་པ་ཉིད་དོ། །ཤེས་པ་ཞེས་བྱ་བས་ནི་འདས་པའི་ཚེའི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུའོ། །

[Block 1089]
འདི་དག་གིས་དྲེགས་པ་མེད་དེ་ཞེས་པ༌[^614]སྒྱུ་རྩལ་དུ་མ་དང་སྐད་ཀྱི་རྣམ་པ༌[^615]ཤེས་ཀྱང་ངོ་། ། འདི་དག་ནི་གོང་དུ་བཤད་པའི་སྦྱིན་པའི་ཁྱད་པར་གྱི་དོན་ནོ། །

[Block 1090]
གློ་བུར་བ་ཐམས་ཅད་ལ་ཞེས་བརྩམས་ཏེ། སྦྱིན་པ་པོའི་གཙོ་བོར་གྱུར་པ་དེ་རྒྱུ་དེས་ན་འཇིག་རྟེན་ལ་ཕན་པའི་ཕྱིར་ཞུགས་པའོ། །

[Block 1091]
སེར་སྣ་ལ་སོགས་པའི་ཉེས་པས་ཟིལ་གྱིས་མ་ནོན་པ་ཞེས་བྱ་བ་ལ། འདིར་སོགས་པའི་སྒྲ་ནི་ཆགས་པ་དང་། ཕྲག་དོག་དང་། །ཞེ་སྡང་ལ་སོགས་པ་སྟེ། སྦྱིན་པའི་བགེགས་ཀྱི་རྒྱུར་གྱུར་པས་ཉེས་པ་ཞེས་སྨོས་སོ། །

[Block 1092]
འདོད་པའི་དོན་འབྱོར་ཐེ་ཚོམ་མེད་གྱུར་པས། །ཞེས་བྱ་བ་ལ། བྱིན་པ་དེ་ནི་འདོད་པའི་དོན་ནོ། །

[Block 1093]
མ་བྱིན་པ་དེ་ནི་ཐེ་ཚོམ་སྟེ། དེ་མེད་པ་ཡིན་པའི་ཕྱིར་འདོད་པའི་དོན་འབྱོར་ཐེ་ཚོམ་མེད་པའོ། །

[Block 1094]
དེ་བས་སློང་ཞེས་ངེས་པར་ཞེས་བྱ་བ་ལ། ནོར་གང་སློང་བ་དེ་ནི་སློང་ཞེས་ངེས་པར་སྨྲས་སོ། །གང་གི་ཕྱིར་ཞེ་ན། སྨྲས་པ། དེའི་སེམས་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཆགས་པའི་སྐབས་མེད་པར་བྱས་པ་སྟེ། སེམས་ཅན་གྱི་དོན་ལ་ཆགས་པས་སོ། །

[Block 1095]
ཤིན་ཏུ་མི་བཟད་ནོར་མིན་ཞེས་བྱ་བ་ལ། མི་བཟད་པ་ནི་དྲག་པའོ། །

[Block 1096]
དེ་རབ་ཏུ་མང་པོར་གྱུར་པའི་ཕྱིར་ཤིན་ཏུའོ། །

[Block 1097]
གཞན་མང་པོ་གཞན་དག་སྟེ། ནོར་མ་ཡིན་པ་དག་ལས་ཀྱང་ནོར་མ་ཡིན་པ་འདི་ཤིན་ཏུ་མི་བཟད་ནོར་མིན་པའོ། །

[Block 1098]
དེ་ལྟར་བསགས་པ་དང་། བསྲུང་བ་གཉིས་ཀྱི་དུས་ན་ཡང་ཉེས་པ་ཆེན་པོར་གྱུར་པས་ན་ཕུང་ཁྲོལ་ལམ་ནོར་བ་ཡིན་པར་བཤད་དོ། །

[Block 1099]
རྒྱུ་རྐྱེན་མེད་པར་མྱུར་དུ་ཆུད་ཟ་བའི། །ཞེས་བྱ་བ་ལ་བར་དུ་གཅོད་པའི་ཉེས་པ་ཡིན་པས་ནའོ། །

[Block 1100]
མྱུར་དུ་ཞེས་བྱ་བ་ནི་ཡུན་མི་རིང་བར་རོ། །

[Block 1101]
དེ་ལ་མི་ཐོགས་པའི་ཚུལ་གང་ཡང༌[^616]ཡོད་པ་དེ་ནི་རྒྱུ་རྐྱེན་མེད་པར་མྱུར་དུ་ཆུད་ཟ་བ༌[^617]ཞེས་བྱ་བ་ཡིན་ཏེ། འདིས་ནི་ལེགས་པར་བསྲུངས༌[^618]བཞིན་དུ་ཡང་འཇིག་པ༌[^619]དང་། མྱུར་དུ་འཇིག་པར་བཤད་དོ། །

[Block 1102]
ཆགས་པའི་གཞི་ཡིན་པའི་ཕྱིར། དེས་ན་ངན་འགྲོའི་གྲོགས་སུ་གྱུར་པ་ཡིན་ཏེ། ངན་འགྲོའི་ལམ་གྱི་དེད་དཔོན་ཞེས་བྱ་བའི་དོན་ཏེ། [^620]ཇི་ལྟར་དེད་དཔོན་གྱིས༌[^621]ལམ་དུ་འཇུག་པ་རྣམས་ཀྱི༌[^622]གྲོགས་བྱེད་པར་གྱུར་པ་དེ་བཞིན་དུའོ། །

[Block 1103]
བདག་དང་གཞན་གྱི་འབྱོར་པ་ཐོབ་ཅེས་བྱ་བ་ལ། གཞན་གྱི་འབྱོར་པ་ཐོབ་པ་ནི་མཐོང་བའི་ཆོས་ལ་སློང་བ་རྣམས་ཀྱི་དབུལ་བ་འཇིག་པའི་ཕྱིར་རོ། །

[Block 1104]
བདག་གི་འབྱོར་པ་ཐོབ་པ་ནི་ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྒྱུར་གྱུར་པས་སོ། །

[Block 1105]
དོན་དང་མཐུན་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་འདོད་པའི་དོན་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། འདོད་པའི་དོན་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1106]
སློང་བས་བསླང་ཞེས་ངེས་པར་སྨྲས་པ་ལ་སོགས་པ་འདིས་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1107]
ཕོངས་པ་རྣམས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིས་ནི་དངོས་གཞི་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1108]
འཇིག་རྟེན་དག་ན་ནོར་ནི་ཕལ་ཆེར་ཡང་། །ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདིས་ནི་མཇུག་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། [^623]དེས་ན་སྦྱིན་པའི་སྔ་རོལ་ན་ཡིད་བདེ་བར་འགྱུར་བ་དང་། སྦྱིན་པའི་ཚེ་ན་དང་བ་དང་། ཐ་མར་བྱིན་ནས་ཀྱང་རྗེས་སུ་དགའ་བར་བྱའོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་གང་བསྟན་པ་དེ་དང་ཡང་འཐད་པ་ཉིད་དོ། །

[Block 1109]
ཇི་ལྟར་འདོད་པ་བཞིན་ཞེས་བྱ་བ་ལ་གང་གི་ཚེ་གང་སློང་བ་དེའི་ཚེ་དེ་བྱིན་པ་ཡིན་ཏེ། དེ་བས་ན་ཇི་ལྟར་འདོད་པ་བཞིན་ཞེས་བྱ་བ་འདིས་ནི་དུས་དང་མཐུན་པའི་སྦྱིན་པ་བསྟན་ཏོ། །

[Block 1110]
ཉོན་མ༌[^624]མོངས་པར་ཞེས་བྱ་བ་ལ་ངོར་ལྟ་བ་དང་སྦྱིན་པ་དམན་པ་དང་ལྡན་པ་མི་སྦྱིན་པ་སྟེ། དེས་ན་བུ་ལྟ་བུ་ལ་ཕན་པའི་ཆེད་དུ་དགག་པ་ཡིན་ཏེ། འདིས་ནི་ཡུན་རིང་བའི་བདེ་བའི་རྒྱུར་གྱུར་པ་བཤད་དོ། །

[Block 1111]
གུས་པ་ཁྱད་པར་ཅན་གྱིས་བརྒྱན། །ཞེས་བྱ་བ་ནི་བཀུར་སྟིའི་སྦྱིན་པའོ། །

[Block 1112]
རླབས་ཆེ་བས་ཞེས་བྱ་བ་ནི་རྒྱ་ཆེ་བའོ། །

[Block 1113]
ཀུན་ཏུ་ཞེས་བྱ་བ་ནི་ཕྱོགས་སུ་མ་ལྷུང་བར་བསྟན་པའོ། །

[Block 1114]
ཡོན་ཏན་འདི་དག་དང་ལྡན་པས་ན་དེ་ཉིད་སྦྱིན་པ་རླབས་པོ་ཆེའོ། །

[Block 1115]
ནོར་དང་འབྲུ་དང་རིན་པོ་ཆེ་དང་ཡོ་བྱད་ཀྱི་རྣམ་པ་བཞི་སྨོས་པ་ནི་ཡང་དག་པར་ཐ་སྙད་དང་། བསགས་པར་བྱ་བ་དང་ཡོངས་སུ་ལོངས་སྤྱད་པ་འདི་དག་འཇིག་རྟེན་ན་ཡོངས་སུ་གཟུང་བའི༌[^625]དངོས་པོ་སྟེ། དེ་བས་ན་བཞི་པོ་ཉིད་སྨོས་སོ། །

[Block 1116]
སྦྱིན་པ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་སྔོན་གྱི་དུས་ནས་བྱེད་པས་ཀྱང་ངོ་། །སློང་བའི་ཚིག་སྨྲ་མ་ཕོད་དེ། བདག་གི་ཞོ་ཤས་འཚོ་བ་ཞེས་བྱ་བ་ནི་རྐུན་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1117]
དེ་སྟེ་བདག་སྐལ་བ་ཆུང་བའི་སྐྱོན་གྱིས་མཐོ་བར་གྱུར་པ་ཞེས་བྱ་བ་ལ། བདག་སྐལ་བ་ཆུང་བའི་སྐྱོན་གྱིས་ཞེས་བྱ་བ་བདག་གི་སྐལ་བ་ཆུང་བའི་སྐྱོན་ནི་དབུལ་བ་འབྱུང་བའི་ལས་དང་། ལོངས་སྤྱོད་པའི༌[^626]བར་དུ་གཅོད་པར་གྱུར་པ་ཞེས་པ་སྟེ། མཐོང་བར་གྱུར་པ་དེའི་དབང་དུ་བྱས་ནས་སོ། །

[Block 1118]
ནོར་རྣམས་ངོ་ནི་མི་རྟག་པར། །ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་དང་པོའི་ཕྱེད་འདིས་ནི་མི་རྟག་པར་བརྟགས་ཏེ། སེམས་མི་གདུང་བར་བསྟན་ཏོ། །

[Block 1119]
ཚིག་རྐང་འོག་མ་གཉིས་ཀྱིས་ནི་སློང་བ་རྣམས་ལ་ལྟོས་ཏེ་ཡིད་གདུངས་པར་བསྟན་ཏོ། །

[Block 1120]
དེ་བསྒྲུབ་པའི༌[^627]ཕྱིར། སྦྱིན་པ་དང་བཀུར་སྟི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་སྟེ། སྦྱིན་པ༌[^628]དང་བཀུར་སྟིས་ཡུན་རིངས༌[^629]བདེ་བྱས་པ་ཞེས་བྱ་བ་ལ། སྦྱིན་པ༌[^630]དང་བཀུར་སྟི་ནི་སྦྱིན་པ་དང་བཀུར་སྟིའོ། །

[Block 1121]
དེ་གཉིས་ལས་གང་བྱུང་བའི་བདེ་བ་ནི་སྦྱིན་པ་དང་བཀུར་སྟིའི་བདེ་བའོ། །

[Block 1122]
དེས་བྱས་པ་ནི་སྦྱིན་པ་དང་བཀུར་སྟིས་བདེ་བ་བྱས་པའོ། །

[Block 1123]
བསླང་བ་ནི་དེ་ལྟར་དཀའ་བ་ལྟ་ཞིག་ཅེས་བྱ་བ་ལ། བདག་ནི་རེ་ཞིག་འདྲིས་པ་ལ༌[^631]སློང་བར་མི་སྤྲོ་ན། མ་འདྲིས་པ་ལའང་སློང་བར་བྱེད་པ་དེ་དག་ནི་རེ་ལྟ་ཞིག་དཀའ་སྙམ་པ་སྟེ། དེ་བས་ན་དཀའ་བ་ལྟ་ཞིག་བྱའོ། །

[Block 1124]
སྦྱིན་པ་དྲགས་པ་ཞེས་བྱ་བ་ལ། སྦྱིན་པ་དྲགས་པ་ཉིད་ཀྱི་ཉེས་དམིགས་ཀྱིས་ཉམས་པར་སྟོན་པ་ཡིན་ཏེ། རྐུན་པོས་མ་ཁྱེར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་སོ། །

[Block 1125]
ཞུགས་པ་ནི་ཞུགས་པ་ཉིད་ཡིན་ཏེ། སྦྱིན་པ་དེ་ལ་རྗེས་སུ་ཆགས་པ་སྟེ་སྦྱིན་པ་ལ་ཞུགས་པའི་ཆགས་པ་སྟེ། བྱམས་པས་བསྐྱོད་པའོ། །
--- END BLOCKS ---
