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
དེ་གཉིས་ལས་གང་བྱུང་བའི་བདེ་བ་ནི་སྦྱིན་པ་དང་བཀུར་སྟིའི་བདེ་བའོ། །

[Block 1122]
དེས་བྱས་པ་ནི་སྦྱིན་པ་དང་བཀུར་སྟིས་བདེ་བ་བྱས་པའོ། །

[Block 1123]
བསླང་བ་ནི་དེ་ལྟར་དཀའ་བ་ལྟ་ཞིག་ཅེས་བྱ་བ་ལ། བདག་ནི་རེ་ཞིག་འདྲིས་པ་ལ༌[^631]སློང་བར་མི་སྤྲོ་ན། མ་འདྲིས་པ་ལའང་སློང་བར་བྱེད་པ་དེ་དག་ནི་རེ་ལྟ་ཞིག་དཀའ་སྙམ་པ་སྟེ། དེ་བས་ན་དཀའ་བ་ལྟ་ཞིག་བྱའོ། །

[Block 1124]
སྦྱིན་པ་དྲགས་པ་ཞེས་བྱ་བ་ལ། སྦྱིན་པ་དྲགས་པ་ཉིད་ཀྱི་ཉེས་དམིགས་ཀྱིས་ཉམས་པར་སྟོན་པ་ཡིན་ཏེ། རྐུན་པོས་མ་ཁྱེར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་སོ། །

[Block 1125]
ཞུགས་པ་ནི་ཞུགས་པ་ཉིད་ཡིན་ཏེ། སྦྱིན་པ་དེ་ལ་རྗེས་སུ་ཆགས་པ་སྟེ་སྦྱིན་པ་ལ་ཞུགས་པའི་ཆགས་པ་སྟེ། བྱམས་པས་བསྐྱོད་པའོ། །

[Block 1126]
དེ་བས་ཁྱོད་ལ་ཕན་ཕྱིར་ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ཀྱིས་སྦྱིན་པ་དྲགས་པའི་རྒྱུས་ནོར་ཟད་པ་དང་། མ་བྱིན་པ་ལས་ནི་འབྲེལ་པར་བཤད་དེ། དེ་གཉི་གའི་དཔེ་བསྟན་པའི་ཕྱིར་སྨྲས་པ། ཆུང་ངུ་གོད་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་འདི་སྨོས་པ་ཡིན་ཏེ། རྟག་ཏུ་ཞེས་བྱ་བ་ནི་རྒྱུན་ཏུའོ། །

[Block 1127]
ཆུང་ངུ་གོད་ཀྱང་ཞེས་བྱ་བ་ལ། ཀྱང་གི་སྒྲས་ནི་མང་པོ་སྤྱད་པ༌[^632]ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1128]
གང་གིས༌[^633]དུས་རྟག་ཏུ་བྱས་པ་ཡང་གྲོག༌[^634]མཁར་ལྟར་མཐོན་པོར་བྱས་པའོ། །

[Block 1129]
དར་བར་འདོད་པས་བསྡམ་པ་བྱས་ན་ལེགས། ། ཞེས་བྱ་བ་འདིས་ནི་ཟད་ཅིང་གོད་པའི་ལམ་ཞེས་བྱ་བ་བསྟན་པ་ཡིན་ནོ། །

[Block 1130]
མ་རབས་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་མི་བྱེད་པའོ། །

[Block 1131]
སྦྱིན་པར་བྱེད་པ་ནི་འཕགས་པ་ཉིད་དེ། ཚིགས་བཅད་འོག་ནས་སྨོས་པས་གང་ཐོབ་པའི་རྒྱུ་འདི་ལས་གང་ཐོབ་པར་འདོད་པ་ནི་མ་རབས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1132]
འདི་ལྟར་གྱུར་ཀྱང་གལ་ཏེ་མ་བྱིན་ན། །ཞེས་བྱ་བའི་ལན་ནི། བདག་ལ་མེད་ཀྱང་རུང་ཞེས་བྱ་བ་འདིའི་དོན་ཏེ། གང་ཡང་སྔོན་གྱི་འབྱོར་པ་བཟང་པོ་ཐོབ་པར་འགྱུར། །ཞེས་བྱ་བ་འདི་ཇི་ལྟར་སྦྱིན་པ༌[^635]བྱིན་པ་འཕགས་པ་ཉིད་དེ།[^636] དེས་ན་དེ་མ་རབས་སུ་བསྒྲུབ་པའི་ཕྱིར། སློང་བའི་སྡུག་བསྔལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་དོ། །

[Block 1133]
སློང་བ་ཉིད་ཤི་བ་ཡིན་པས་སློང་བ་ཤི་བ་དང་འདྲའོ། །

[Block 1134]
དེའི་གཉེན་པོའི་ལམ་ནི་ནོར་ཐོབ་པ་དང་ནོར་རྙེད་པའོ། །

[Block 1135]
དེས་དེའི་སྡུག་བསྔལ་གསོ་བར་བྱེད་དེ་སྡུག་བསྔལ་ནི་དབུལ་བའི་སྡུག་བསྔལ་ལོ། །

[Block 1136]
དེ་ཡིས་ཕོངས་པ་ནི་སློང་བ་ཤི་བ་དང་འདྲ་བ་ཉིད་ཀྱིས་སོ། །

[Block 1137]
སེར་བས་བསྣུན་པར་བྱེད་པ་ནི་མ་རབས་ཏེ། སློང་བ་ཤི་བ་དང་འདྲ་བ་འཛིན་པ་ལ་ཡང་མེད་ཅེས་བྱ་བའི་སེར་བས་རྡེག་པར་བྱེད་པས༌[^637]སོ། །

[Block 1138]
གང་རྡེག་པར་བྱེད་པ་དེ་ནི་མ་རབས་ཏེ། ཁྱད་པར་དུ་ཡང་ཡ་རབས་གཟི་བྱིན་ཅན་གྱིས་དེ་རྡེག་པར་བྱེད་པ་ནི་མ་ལགས༌[^638]སོ། །

[Block 1139]
དེ་ལྟར་རེ་ཞིག་འདིའི་མ་རབས་བསྒྲུབས༌[^639]ནས། གང་ཞིག་ཐོབ་ཕྱིར་སེར་སྣ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་ཕྱེད་པོ་དེའི་དོན་བསྒྲུབ་པའི༌[^640]ཕྱིར།[^641] སློང་བས་བརྡུངས༌[^642]ནས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 1140]
གཞན་ལ་ཕན་པ་ལ་ཞུགས་པ་ལ་ཅི་སོགས་པར་བྱེད་དམ་ཞེས་པ་སྟེ། སྔ་ན་མེད་པའི་རིན་པོ་ཆེ་ལ་སོགས་པ་བདག་ལ་མེད་ཀྱང་རུང་བ༌[^643]སྟེ།

[Block 1141 [VERSE]]
དེ་བདག་གི་སེམས་འདི་ལྟར་འདིས་བསྒྲུབ་པའོ། །
གང་ཞིག་ཐོབ་ཕྱིར་སེར་སྣའི་སེམས་བྱུང་བ། །

[Block 1142]
ཞེས་བྱ་བ་འདིས་བསྒྲུབ་པའི༌[^644]ཕྱིར། སློང་བས་གདུངས་ཤིང་ཞེས་བྱ་བའི་དོན་དེ་སེར་སྣའི་སེམས་ཀྱིས་སློང་བའི་བདེ་བ་མི་བསྒྲུབ༌[^645]ཅིང་སྔ་ན་མེད་པ་སོགས་པ་ནི་མི་རིགས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1143]
གང་ཞིག་ཐོབ་པའི་ཕྱིར་སེར་སྣའི་སེམས་བྱུང་བ་ན། [^646]ད་ནི་སྐྱེས་པ་ལ་ཡང་མི་རིགས་པའི་དབང་དུ་བྱས་ནས་གང་གིས་སེར་སྣའི་སྐྱོན་ཞེས་བྱ་བའི་ཚིགས་བཅད་བཤད་དོ། །

[Block 1144]
གང་གིས་སེར་སྣའི་སྐྱོན་ནི་འཕེལ་འགྱུར་ཞིང་། །ཞེས་བྱ་བ་ལ། སེར་སྣ་ནི་གཞན་གྱི་ཕུན་སུམ་ཚོགས་པ་ལ་མི་བཟོད་པ་སྟེ།

[Block 1145 [VERSE]]
དེས་ནི་སྙིང་རྗེ་མེད་པར་བསྟན་ཏེ། །
གཏོང་བའི་སེམས་ཀྱང་སྐྱེ་བར་མི་འགྱུར་བ། །

[Block 1146]
ཞེས་བྱ་བ་ལ་ཆགས་པའི་གཉེན་པ༌[^647]ནི་གཏང་བའི༌[^648]སེམས་ཏེ། ཡོངས་སུ་སྐྱེ་བ་ཞེས་བྱ་བ་འདིས་ནི་ཤེས་རབ་རྣམ་པར་འཕེལ་བར་བྱེད་པ་སྟེ། ཤེས་རབ་ཀྱིས་ནི་ཕན་པ་མེད་པ༌[^649]ངོ་བོ་ཉིད་ཀྱིས་ཡོངས་སུ་སྤྱོད་པའི་ཕྱིར་རོ། །

[Block 1147]
གཏང་བའི༌[^650]སེམས་སྐྱེ་བ་དེ་དང་སྦྱིན་པ་སྟེ། སྐྱེས་ན་ཡང༌[^651]ཞེས་བྱ་བའི་དོན་ཏེ་མ༌[^652]སྐྱེས་པ་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། དེ་ཡོངས་སུ་གཟུང་བར༌[^653]སྙད་བཏགས་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གཟུང་བ༌[^654]ཉིད་སྙད་བཏགས་པ༌[^655]སྟེ་སྙད་བཏགས་པ་ནི་སྒྲིབ་པའི་ཆོས་སོ། །

[Block 1148]
ཡང་ན་གྱ་གྱུའོ། །

[Block 1149]
ཡོངས་སུ་གཟུང་བར༌[^656]སྙད་བཏགས་པ་མི་ལྟོགས་པར་ནི་ཡོངས་སུ་གཟུང་བར༌[^657]སྙད་བཏགས་པའི་རང་བཞིན་ནོ། །

[Block 1150]
དེ་གང་ཞེ་ན། ཕོངས་པ་སྟེ། འདིས་རྣམ་པར་བཅོམ་པ་ཡིན་པས་ཕོངས་པ་ཉིད་ལས་ཡོངས་སུ་གཟུང་བར་སྙད་བཏགས་པ༌[^658]ཉིད་དོ། །

[Block 1151]
ཡོངས་སུ་གཟུང་བའི༌[^659]ཚུལ་ཉིད་དུ་གནས་པས་བཅོམ་ཞེས་བྱ་བའི་དོན་ཏེ། ཕོངས་པའི་རྒྱུ་ཡིན་པས་རྒྱུ་ལ་འབྲས་བུ་བཏགས་པའོ། །

[Block 1152]
ཕོངས་པ་དེ་ཉིད་བསྒྲུབ་པར༌[^660]འདོད་པས། གློག་ནི་འགྱུ་བ་བཞིན་དུ་ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་སོ། །

[Block 1153]
གློག་ནི་འགྱུ་བ་བཞིན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྐད་ཅིག་གིས་འཇིག་ཅིང་མི་རྟག་པར་བསྟན་ཏེ། རང་ཉིད་རྣམ་པར་འཇིག་པའི་ཕྱིར་རོ། །

[Block 1154]
ཐུན་མོང་ཞེས་བྱ་བ་འདིས་ནི་ལྔའི་ཐུན་མོང་དུ་གྱུར་པ་སྟེ། འདིས་ནི་རྣམ་པར་འཇིག་པའི་རྒྱུས་འཇིག༌[^661]པའི་ཕྱིར་ཏེ་འབྲལ་བའི་མི་རྟག་པ་བསྟན་ཏོ། །

[Block 1155]
ཕོངས་པ་དུ་མའི་རྒྱུ་ཞེས་བྱ་བ་ནི༌[^662]སྔར་བསྟན་པའི་ཕོངས་པ་ཞེས་བྱ་བ་ད་ཉིད་བསྟན་ཏེ། ཕོངས་པའི་རྒྱུ་ཞེས་བྱ་བ་ནི་བསགས་པ་དང་འཇིག༌[^663]པའི་དུས་སུ་བསྲུང་བ་དང་། གྲང་བ་དང་། ཚ་བ་དང་། གསད་པ༌[^664]དང་། བཅིང་བ་དང་། བརྡེག་པ་ལ་སོགས་པ་ཕོངས་པའི༌[^665]རྒྱུའོ། །

[Block 1156]
འདིས་ནི་ཡོངས་སུ་བཅོམ་པས་ཕོངས་པ༌[^666]ཉིད་དུ་བསྟན་ཏོ། །

[Block 1157]
དེ་ལྟར་ཕོངས་པ་ལ་ནོར་གྱི་སེར་སྣའི་ཡ་རབས་སུ་ཞིག་བསྟན་པར༌[^667]བྱེད་དེ་ནོར་སྦྱིན་པ་ཉིད་ལ་སུ་ཞིག་འདི་ལྟར་སེར་སྣ་བྱེད་པའོ། །

[Block 1158]
ད་ནི་དེའི་རྒྱུ་བསྟན་པའི་ལམ་ལས་བརྩམས་ཏེ། བརྒྱ་བྱིན་ཁྱོད་ཀྱིས་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདིའོ། །

[Block 1159]
གཉེན་པ་ནི་བདག་ཉིད་ཀྱི་ཉེ་དུ་ལྟ་བུ་སྟེ། ཅིའི་ཕྱིར་ན་ཕན་པ་སྨྲས་པས་སོ། །

[Block 1160]
དེ་བས་ལམ་མིན་ཞེས་བྱ་བ་ལ། སྦྱིན་པའི་ལམ་མ་ཡིན་པ་ནི་སྦྱིན་པ་མ་ཡིན་པ་སྟེ། སྨྲས་པ་ཕན་པ་མ་ཡིན་པ་བསྟན་ཅིང་བསྒྲུབས་པས་ནི་ཁྲོ་བ་ཡོངས་སུ་འཛིན་པའི་ཕྱིར། ཁྱོད་ཀྱི་ཐུགས་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །
--- END BLOCKS ---
