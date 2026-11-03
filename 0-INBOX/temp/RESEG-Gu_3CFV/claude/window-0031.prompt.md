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
འདིར་གཞུང་ནི་དགེ་སློང་འགའ་ཞིག༌[^654]གཅེར་བུ་པ་ལ་རང་གི་སུག་པ་ནས་བཟའ་བ་དང་བཅའ་བ་སྩལ་ལ་ལྟུང་བར་ཡང་མི་འགྱུར་བ་འགའ་ཞིག༌[^655]མཆིས་སམ། ཡོད་དེ་ཉེ་དུ་ལ་བྱིན་པ་དང་། རབ་ཏུ་བྱུང་བ་ལ་ལྟོས་པ་དང་ནད་པ་ལ་བྱིན་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1087]
དེ་ཇི་ལྟ་བུར་གྱུར་པ་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རྟགས་འདི་དང་རབ་ཏུ་བྱུང་བ་འདི་མེད་པའི་གཅེར་བུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་རྟགས་འདི་མེད་པའི་རྟགས་ཙམ་གྱི་རབ་ཏུ་བྱུང་བ་གང་ཡིན་པ་དེ་སྟེ་རབ་ཏུ་བྱུང་བ་མ་ཡིན་པ་དང་རྟགས་འདི་ལ་རབ་ཏུ་བྱུང་བ་ལ་ཉམས་པ་ཉིད་དུ་འགྱུར་བ་ཡིན་ཏེ།

[Block 1088]
དང་པོ་འདི་པའི་རབ་ཏུ་བྱུང་བ་ནི་གཅེར་བུ་པ་ཉིད་དོ། །

[Block 1089]
དེ་བས་ན་གཅེར་བུ་པ་ཞེས་བྱ་བ་འདི་ལས་འདི་པའི་རབ་ཏུ་བྱུང་བ་མ་ཡིན་པར་དགག་པ་གྲུབ་པ་ཉིད་དོ། །ཅི་ཞིག་ལྟ་བུར་གྱུར་པའི་གཅེར་བུ་པ་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ལུས་སམ་ལུས་དང་འབྲེལ་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཅི་ཞིག་ཅེས༌[^656]བྱ་བ་འདི་ལ་རང་གིས་བྱིན་ན་ཞེས་བྱ་བ་གསུངས་ན་དེ་ལ་གང་བྱིན་ན་ཞེ་ན། དེའི་ཕྱིར་བཅའ་བར་བྱ་བ་དང་བཟའ་བར་བྱ་བ་དག་གི༌[^657]ཞེས་བྱ་བ་སྨོས་སོ། ། ཅི་རྣམ་པ་གང་ཡང་རུང་བ་ཞིག་གམ་ཞེ་ན། དེའི་ཕྱིར་རུང་བ་དག་གོ་ཞེས་བྱ་བ༌[^658]སྨོས་སོ། །

[Block 1090]
དེ་དག་སུ་ལ་རུང་བ་ཞེ་ན། དེའི་ཕྱིར་རང་དང་དེ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་ཞེས་བྱ་བ་ནི་ལྟུང་བའི་ཚིག་གོ། །

[Block 1091]
དེ་ལ་ཞེས་བྱ་བ་ནི་ཡང་དག་པར་བྱིན་པར་བྱ་བ་གཅེར་བུ་པ་ལའོ། །

[Block 1092]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 1093]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་གཅེར་བུ་པའམ་གཅེར་བུ་མ་ལ་བཅའ་བར་བགྱི་བ་དང་བཟའ་བར་བགྱིར༌[^659]རུང་བ་མ་ལགས་པར་སྩོལ་ན་ལྟུང་བ་ཅིར༌[^660]འགྱུར། ཉེས་བྱས་སོ། །

[Block 1094]
གལ་ཏེ་དེ་ལ་རུང་བ་མ་ལགས་པ་དེ་འདྲ་བའི་བཅའ་བར་བགྱི་བ་དང་། བཟའ་བར་བགྱི་བ་སྩལ་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1095]
གང་ཞིག་དེ་ལ་མ་ཡིན་ཞེས་བྱ་བ་འོག་མའི་དྲི་བ་ལས་གསུངས་ན་སྔ་རོལ་དུ་དགེ་སློང་ལ་མི་རུང་བ་གང་ཡིན་པ་དེ་བཟུང་བ་ཞེས་བྱ་བ་ངེས་པའོ། །ཅི་དོན་གང་ཡང་རུང་བའི་ཕྱིར་སྦྱིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་དང་དབྲལ་བ་ཉིད་ཀྱི་ཕྱིར་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་སྟེ། [^661]འདིར་གཞུང་ནི་སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་དང་དབྲལ་བར་འདོད་པ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1096]
ཅི་ཞིག་རྗེས་སུ་བསྒྲུབ་ན་གཅེར་བུ་པ་ལ་སྦྱིན་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རང་གིས་བྱིན་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1097]
མི་རུང་བ་དག་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་རང་དང་དེ་ལ་མི་རུང་བའི་བཅའ་བ་དང་བཟའ་བ་དག་སྦྱིན་པ་ལ་ནི་ཉེས་བྱས་ཏེ། འདི་དག་སྦྱིན་དུ་འཇུག་ན་ཤིན་ཏུ་ན་སྨད་པ་ཉིད་དེ་འདི༌[^662]ནི་མཚོན་པ་ཙམ་ཡིན་ནོ། །

[Block 1098]
འདིར་གཞན་ལ་ཡང་དངོས་གཞི་མ་ཡིན་པར་བྱས་པ་སྦྱིན་པ་ཐམས་ཅད་དུ་སྦྱིན་པར་བྱས་ལ་གོས་ལ་སོགས་པ་ལ་ཉེས་བྱས་སུ་རྟོགས་པར་བྱའོ། །

[Block 1099]
སྦྱིན་དུ་འཇུག་ན་ཡང་ངོ་། །རང་གིས་ཞལ་ཏ་བྱས་ནའོ་ཞེས་བྱ་བ་ནི་རང་གིས་ལུས་སམ་དེ༌[^663]འབྲེལ་པ་ལ་མི་རུང་བའི་བཅའ་བ་དང་བཟའ་བ་དག༌[^664]ལ་ཉེས་བྱས་སོ། །

[Block 1100]
དེ་ལ་གཅེར་བུ་པ་ལ་ཡོངས་སུ་འཚོལ་བར་བྱེད་ན་ཉེས་བྱས་སོ། །

[Block 1101]
མངོན་གསུམ༌[^665]དུ་སྦྱིན་པ་ལ་འདི་དང་འབྲེལ་པ་མ་ཡིན་ནོ། །

[Block 1102]
རང་གིས་ཞལ་ཏ་བྱས་ན་སྦྱིན་དུ་འཇུག་པ་ལ་དེ་དང་འབྲེལ་པ་ཉིད་ལ་གུས་པ་ཉིད་དུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 1103]
དེ་བས་ན་རང་གིས་ཞལ་ཏ་བྱས་ནས་སྦྱིན་དུ་འཇུག་པའི་དབང་དུ་བྱས་ནས་ཉེས་བྱས་འདི་བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 1104]
བགོ་བཤའ་བྱེད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བགོ་བཤའ་བྱེད་པའི་ངོ་བོས་བཅའ་བ་དང་བཟའ་བ་དག་ལ་ལུས་སམ་དེ་དང་འབྲེལ་པ༌[^666]ལས་གཞན་དུ་ཉེས་བྱས་སོ། །

[Block 1105]
གང་ཞིག་སློང་བ་འབྲས་བུ་དང་བཅས་པའི་ངོ་བོ་གཞན་དུ་འཇོག་པ་གདོལ་པ་བཞིན་དུ་དེ་སྦྱིན་པས་ན་དེ་ལ་ཉེས་པ་མེད་དོ། །

[Block 1106]
བགོ་བཤའ་བྱ་བའི་ཚུལ་གྱིས་འདིར་ཡོངས་སུ་ཚོལ་བར༌[^667]བྱེད་པར་འགྱུར་བ་ཉིད་ཡོད་པ་ཡིན་ནོ། །

[Block 1107]
དེ་བས་ན་འདིར་ཉེས་པ་མེད་པ་ཉིད་མེད་དོ། །

[Block 1108]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་གཅིག་ཏུ་བགོ་བཤའ་བྱ་སྟེ་ཟ་ན་ཉེས་བྱས་སོ། །

[Block 1109]
གཞན་གྱིས༌[^668]རང་གི་དོན་དུ་བགོ་བཤའ་བྱེད་དུ་འཇུག་པ་ལ་ཉེས་བྱས་ལས་ཤིན་ཏུ་ན་སྨད་པ་ཉིད་ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1110]
མི་རུང་བའི་བཟའ་བར་བྱ་བ་དང་བཅའ་བར་བྱ་བ་དག་ལ་མདོ་སྔ་མ་དག་གིས་ཤེས་པར་བྱའོ། །

[Block 1111]
གཅེར་བུ་པ༌[^669]ལ་སྦྱིན་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1112]
གང་དུ་དམག་ལ་ལྟ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གཡུལ་ལ་རྣམ་པར་དགའ་བའི་དམག་ལ་ལྟ་བའི་དོན་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཞུགས་པ་ལ་ཞེས་བྱ་བ་དང་འབྲེལ་ལོ། །

[Block 1113]
བསོད་སྙོམས་ལ་སོགས་པའི་དོན་དུ་བྱུང་བས་དམག་ལ་ལྟ་བར་བྱེད་ན་ཡང་ལྟུང་བྱེད་དོ། །ཅི་རྒྱུ་མཚན་གང་ཡང་རུང་བས་བལྟའོ་ཅོག་ལའམ་ཞེ་ན། དེའི་ཕྱིར་རྒྱལ་པོ་དང་བཙུན་མོ་དང་གཞོན་ནུ་དང་ཞང་བློན༌[^670]དང་ཁྲོམ་གྱི་རུ་སྣ་དང་། གྲོང་རྡལ་གྱི་མི་དང་ལྗོངས་ཀྱི་མིས༌[^671]བཀུག་པ་དང་བར་ཆད་བྱུང་བའི་དབང་ཉིད་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་སྟེ། འདི་རྣམས་ཀྱིས་ཀྱང་བརྗོད་དེ་བར་དུ་གཅོད་པའི་རྒྱུ་མཚན་ལ་ཉེ་བར་ལྟུང་བ་དོར་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1114]
སྟོབས་ཀྱིས་བཟུང་ནས་ཁྱེར་བ་ནི་བར་དུ་གཅོད་པ་ཉེ་བར་ལྟུང་བ་ལ་ཁོངས་སུ་བསྡུས༌[^672]པར་རིག་པར་བྱའོ། །

[Block 1115]
ཉེ་བར་འཚེ་བ་དང་དགེ་འདུན་ནམ་གང་ཟག་གམ་མཆོད་རྟེན་ལ་སོགས་པ་ལ་བར་དུ་གཅོད་པ་ཉིད་ནི་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1116]
རྗེས་སུ་བསྒྲུབ་པ་གང་ལ་ལྟུང་བ་འདི་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འཕགས་པའི་ཉེན་ཀོར་གྱི་མཐའ་ལས་འདས་ཏེ་མཐོང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་གང་ན་འཕགས་པའི་གནས་དེའི་ཉེ་འཁོར་གང་ཡིན་པ་དེའི་མཐའ་གང་ཡིན་པ་དེ་ལས་འདས་ཏེ་མཐོང་བ་ཆོས་གོས་ཀྱི་ཉེན་ཀོར་གང་ཡིན་པ་དེ་ནི་འདིར་ཉེན་ཀོར་དུ་རིགས་པ་ཡིན་ནོ། །

[Block 1117]
གྲོང་དང་འབྲེལ་པ་དོར་ནས་འདིར་ཐོགས་པ་དང་བཅས་པའི་ཁྱིམ་བཞིན་དུ་མ་བསྒྲིབས་པ་ལ་ཉེས་པ་མེད་པ་ལྟར། དགེ་སློང་གླང་པོ་ཆེའི་ཚོགས་ལྟ་བའི་ཕྱིར་འགྲོ་ན་ཇི་སྲིད་དུ་མིག་གིས་མ་མཐོང་གི་བར་དུ་ནི་ཉེས་བྱས་སོ། །

[Block 1118]
མིག་གིས་མཐོང་བར་གྱུར་ན་ནི་ལྟུང་བྱེད་དོ། །

[Block 1119]
དེ་བཞིན་དུ་རྟའི་ཚོགས་དང་ཤིང་རྟའི༌[^673]ཚོགས་དང་རྐང་ཐང་གི་ཚོགས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟུང་བ་བསྟན་པ་ལ་མཐོང་བ་ཙམ་ལ་དངོས་གཞིར་གསུངས་སོ། །

[Block 1120]
དེའི་སྔ་རོལ་དུ་ཉེན་ཀོར་གྱི༌[^674]མཐའ་མ་ལས་མ་འདས་པར་དེའི་དོན་དུ་འཇུག་པ༌[^675]ལ་དེའི་བཞིན་བསྒྱུར་བ་ཙམ་གྱིས་མཐོང་བ་ལ་ནི་ཉེས་བྱས་སུ་གཏོགས་པར་བྱའོ། །

[Block 1121]
དམག་ལ་ལྟ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1122]
གང་དུ་དམག་གི་ནང་དུ་གནས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེ་དག་མེད་པར་དེར་ཉིན་མཚན་གཉིས་ལས་ལྷག་པར་འདུག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དག་མེད་པར་ཞེས་བྱ་བ་ནི་རྒྱལ་པོ་ལ་སོགས་པས་བཀུག་པ་དང་བར་ཆད་ཉེ་བར་བྱུང་བའི་དབང་ཉིད་དོ། །

[Block 1123]
དེར་ཞེས་བྱ་བ་ནི་གཡུལ་ལ་མངོན་པར་དགའ་བའི་དམག་ལའོ། །

[Block 1124]
ཉིན་མཚན་གཉིས་ལས་ཞེས་བྱ་བ་ནི་ཉིན་མོ་དང་མཚན་མོ༌[^676]དག་ལའོ། །

[Block 1125]
དེ་ལས་གང༌[^677]དུ་ལྷག་པར་འདུག་ནའོ་ཞེས་བྱ་བ་འདི་ནི་ཉིན་མཚན་དག་གོ། །
--- END BLOCKS ---
