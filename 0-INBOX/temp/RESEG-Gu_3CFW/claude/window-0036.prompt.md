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
[Block 1261]
འདི་དང་པོ་བྱས་ཏེ་སིངས་པོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1262]
དེ༌[^1092]དུས་སུ་རུང་བ་ཉིད་ཡིན་ན་ཐུན་ཚོད་ཀྱི་མཐའ་ཡིན་ནོ༌[^1093]ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་བཏུང་བའི་རྫས་དེའོ། །

[Block 1263]
གཞན་ཉིད་ཡིན་ན་དེའི་གང་ཡིན་པའོ་ཞེས་བྱ་བ་ནི་བཏུང་བའི་རྫས་དེ་དུས་སུ་རུང་བ་ལས་གཞན་པ་དུས་མ་ཡིན་པར་རུང་བ་ཉིད་ཡིན་ན་གང་ཞིག་རྫས་དེའི་མཐར་ཐུག་པ་བཏུང་བ་དེ་ལ་ཐུན་ཚོད་ཀྱི་མཐའ་གཞན་བཟའ་བར་བྱ་བ་ལ་དུས་གང་གི་ཚེ་བཟའ་བར་བྱ་བ་ཉིད་སྐྱེས་པར་འགྱུར་བ་དེའི་ཚེ༌[^1094]བཟའ་བའི་ཕྱིར་དུས་མ་ཡིན་པར་བཏུང་བའི་རྫས་ལ་དུས་ཐམས་ཅད་པ་ཉིད་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1264]
བྱིན་གྱིས་བརླབས་པའི་ཕྱིར་ནི་ཐུན་ཚོད་དུ་རུང་བ་ཉིད་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1265]
ཁ་ཅིག་ན་རེ་མ་གྱུར༌[^1095]ན་དེ་ཡིན་གྱི་གྱུར་ན་གང་ཚུན་ཆད་དེ་ཡིན་པའོ་ཞེས་ཟེར་རོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་བཏུང་བའི་རྫས་ཀྱི་མཐའ་ཡིན་པ་དེ་ཉིད་བཏུང་བ་ལ་ཞེས་གང་སྨོས་པ་དེ་གཅིག་ཏུ་ངེས་པར་རྣམ་པར་གནས་པ་མ་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། འདི་ལྟར་ངོ་བོ་ཉིད་མ་གྱུར་ན་དེ་ལྟུང་བའི༌[^1096]མཐའ་ཡིན་གྱི། གྱུར་ན་སྐད་ཅིག་གང་ཚུན་ཆད་ཀྱི་འོག་ཏུ་ངོ་བོ་ཉིད་དུ་གྱུར་པའི་སྐད་ཅིག་དེ་ཉིད་བཏུང་བའི་མཐའ་ཡིན་པར་ཤེས་པར་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 1266]
དེ་ནི་མ་ཡིན་ཏེ་དུས་ལྷག་པ་ལ་བརྟེན་ན་མི་འཆགས་པར་འགྱུར་བའི་ཕྱིར་དང་། དེ་འབྱུང་བར་འགྱུར་བ་ཕལ་པ་རྣམས་ཀྱི་བགྲོད་པ༌[^1097]མ་ཡིན་པའི་ཕྱིར་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ཉིད་མ་ཡིན་པར་འགྱུར་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་གྱུར་ན་གང་ཚུན་ཆད་དེ་ཡིན་པའོ་ཞེས་ཟེར་བ་ནི། དེ་ནི༌[^1098]མ་ཡིན་ཏེ། དུས་ལྷག་པ་ལ་བརྟེན་ན་མི་འཆགས་པར་འགྱུར་བའི་ཕྱིར་ཏེ། གང་ལས་བཏུང་བར་གྱུར་པར་འགྱུར་ན། དེའི་ཕྱིར་དུས་ལྷག་པ་ལ་བྱིན་གྱིས་བརླབ་པ་བརྟེན་པའི་བྱིན་གྱིས་བརླབ་པ་མི་འཆགས་པ་སྟེ། འདིར་དེ་ཙམ་གྱི་དུས་ལས་མ་གནང་བ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་འདི་ཐོབ་པའོ། །

[Block 1267]
ཐོབ་པ་དེ་དང་མི་འཆགས་པ་མེད་པ་ལ་ཤེས་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཀྱི༌[^1099]ཕྱིར་འབྱུང་བར་འགྱུར་བ་ལ་ཐ་མལ་པ་རྣམས་ལ་བྱིན་གྱིས་བརླབ་པ༌[^1100]མ་ཡིན་པ་ཉིད༌[^1101]ཐལ་བར་འགྱུར་རོ། །

[Block 1268]
གང་གི་ཕྱིར་གང་ཞིག་འབྱུང་བར་འགྱུར་བ་དེ་ནི་ཐ་མལ་པ་དང་། མ་ཐོབ་པ་རྣམས་ལ་མ་འོངས་པའི་ཤེས་པའི་ནུས་པས་བགྲོད་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1269]
དེ་ལྟ་བས་ན་དེ་མི་ཤེས་པའི་ཕྱིར་ཡོངས་སུ་གཟུང་བར༌[^1102]བྱ་བའི་དུས་གང་ཡིན་པ་དེ་མི༌[^1103]ཤེས་པས། དེས་ན་བྱིན་གྱིས་བརླབ་པར༌[^1104]བྱ་བ་ཉིད་བཏུང་བ་ལ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1270]
ཐུན་ཚོད་ཉིད་ཀྱིས་ཀྱང་མདུན་རོལ་དུ་ཐུན་ཚོད་ཀྱི་ཐ་མ་ལས་འགའ་ཞིག་ལས་ཡོངས་སུ་གཟུང་བར༌[^1105]འགྱུར་རོ། །

[Block 1271]
འདིར་རོ་དང་ཕྱེ་མ་སྦྱར་བའི་བཏུང་བ་དག་འདུས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདིར་ཞེས་བྱ་བ་ནི་ཐུན་ཚོད་དུ་རུང་བ་རྣམས་ལའོ། །

[Block 1272]
རོ་དང་ཕྱེ་མ་སྦྱར་བའི་བཏུང་བ་ལ་ཡང་ཐུན་ཚོད་དུ་རིག་པར༌[^1106]བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1273]
སྨན་རྩབས་ཤིན་ཏུ་སླ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཐུན་ཚོད་དུ་རུང་བའི་བཏུང་བ་དག་ཏུ་འདུས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1274]
སྨན་རྩབས་ཞེས་བྱ་བ་དེ་ཇི་ལྟ་བུ་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེ་ནི༌[^1107]རྩ་བ་ལ་སོགས་པའི་སྨན་བཀུས་པ༌[^1108]སྐྱུར་པོ༌[^1109]ཞེས་བྱ་བ་སྨོས་ཏེ། ཐུན་ཚོད་དུ་རུང་བ་བསྟན་ནས། [^1110]དེའི་ཕྱིར་ཞུན་མར་དང་། འབྲུ་མར་དང་། སྦྲང་རྩི་དང་བུ་རམ་གྱི་སྦུ་བ་དག་ནི་ཞག་བདུན་པའོ། །

[Block 1275]
བུ་རམ་དང་ཧྭགས་དང་། ལི་ཁ་ར་ལ་སོགས་པ་ཐམས་ཅད་ནི་བུ་རམ་གྱི་སྦུ་བ་ཉིད་ཀྱིས་འཕངས་སོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་བདག་གླང་བུ་ལྟ་བུས་དགེ་སློང་ཟན་ཆད་པ་རྣམས་ཀྱིས་དུས་མ་ལགས་པར་ཅི་ཞིག་འཚལ་དུ་རུང་ཞེས་ཞུས་ན། བུ་རམ་དང་། ཞུན་མར༌[^1111]དང་། ཧྭགས་དང་། ལི་ཁ་ར་དག་དང་། བཏུང་བ་དག་གོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་ལས་འདི་ལྟར་ཤེས་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1276]
བདུད་རྩི་ནི་ཞུན་མར་དང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བཟའ་བར་བྱ་བ་ཉིད་དང་ཞག་བདུན་པ་ཉིད་ཀྱི་ཕྱིར་ཏེ། ཞུན་མར་གྱི་རྣམ་པ་ཉིད་བསྟན་པའི་ཕྱིར་དེ་ལྟར་འདི་སྨོས་ཏེ། འདིར་གཞུང་ནི། ཞུ་བ་ལས་སོ། །

[Block 1277]
ཞག་བསྐོལ་ཞིང༌[^1112]བཙགས་པ་དག་ནི་འབྲུ་མར་དང་མར་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ཡང་། དེའི་ཚེ་དེ་རྣམས་ཡིན་པར་བྱིན་ལེན་བྱས་པ་རྣམས་ནི་འབྲུ་མར་གྱི་རྣམ་པ་ཉིད་ལས་སྐྱེས་པ་ཉིད་དོ། །

[Block 1278]
འདིར་གཞུང་ནི། ཞག་རྣམ་པ་ལྔ་པོ་འདི་དག་ནི་དུས་མ་ཡིན་པར་བསྐོལ། དུས་མ་ཡིན་པར་བཙགས། དུས་མ་ཡིན་པར་བྱིན་ལེན་བྱས། དུས་མ་ཡིན་པར་བྱིན་གྱིས་བརླབས༌[^1113]ན་ཡང་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ། །

[Block 1279]
དུས་སུ་བསྐོལ་དུས་སུ་བཙགས། དུས་སུ་བྱིན་ལེན་བྱས་ཤིང་དུས་མ་ཡིན་པར་བྱིན་གྱིས་བརླབས་ན་ཡང་ལོངས་སྤྱད་པར་མི་བྱའོ། །

[Block 1280]
དུས་སུ་བསྐོལ་དུས་སུ་བཙགས་དུས་སུ་བྱིན་ལེན་བྱས། དུས་སུ་བྱིན་གྱིས་བརླབས་ན་འབྲུ་མར་ཉིད་དུ་ལོངས་སྤྱད་པས་ཞག་བདུན་པས་ཡོངས་སུ་ལོངས༌[^1114]སྤྱད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1281]
གང་ཞིག་འདིར་བསྐོལ་བ་དང་བཙགས་པ་ཉིད་ནི་ཁས་ལེན་པར་བྱེད་པ་དེ་བས་ན་འདིར་དོན་འདི་རྙེད༌[^1115]པའོ། །

[Block 1282]
འདིར་དེ་དག་ལ་དུས་མ་ཡིན་པར་བྱས་པ་ཉིད་ལ་བཟའ་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་དུ་ཤེས་པར་བྱ་བ༌[^1116]ཡིན་ནོ། །

[Block 1283]
དུས་མ་ཡིན་པ༌[^1117]འམ་དུས་སུ་འདི་དག་བྱས་པ་ལ་དུས་མ་ཡིན་པར་བྱིན་གྱིས་བརླབས་པ་ཉིད་ལ་བཟའ་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་འདིར་དོན་དེའོ། །

[Block 1284]
བྱིན་ལེན་བྱེད་པ་ལ་ཡང་ཚུལ་འདི་ཉིད་དོ། །

[Block 1285]
འདིར་གནས་སྐབས་དང་འབྲེལ་པའི་བྱེ་བྲག་ནི་འདི་ཡིན་ནོ། །

[Block 1286]
བྱིན་ལེན་འདི་ལ་བསྐོལ་བ་དང་། བཙགས་པ་ལྟར་དུས་མ་ཡིན་པར་བྱིན་གྱིས་བརླབས་པ་ལ་གནས་སྐབས་ཉིད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1287]
ཞག་རྣམ་པ་ལྔ་ཞེས་གསུངས་པ་དེ་དག་ལ༌[^1118]ནི་ངེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1288]
འདི་རྣམས་ཉིད་ལ་འབྲུ་མར་དང་འདྲ་བ་ཉིད་ཡིན་ནམ་འོན་ཏེ་འདྲ་བ་ཉིད་མ་ཡིན་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར་དགོས་པ༌[^1119]བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཉ་དང་རི་བོང་གི་དང་ཆུ་སྲིན་བྱིས་པ་གསོད་ཀྱི་དང་། དོམ་གྱི་དང་ཕག་གིའོ། །

[Block 1289]
དེ་དག་ནི༌[^1120]ནད་པ་ལ་ཕལ་ཆེར་སྦྱོར་བར་བྱེད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕལ་ཆེར་ཞེས་བྱ་བ་ནི་ལན་ཤིན་ཏུ་མང་བའོ། །

[Block 1290]
རྒྱུ་དེས་ཉེ་བར་ཞི་བར་བྱེད་པའི་ན་བ་རྣམས་ལ་ཕལ་ཆེར་འཇིག་རྟེན་ལ་གྲགས་པའི་ཕྱིར་རོ། །

[Block 1291]
སོས་པ་ཉིད་ནི་དེ་དག་ནད་པའི་ཕྱིར་སློང་ན་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་རྣམས་ལ་ནི་ནད་སོས་པས་བཅང་བར་མི་བྱའོ་ཞེས་བྱ་བ་དེ་འདིས་བྱས་པར་རིག་པར་བྱའོ། །

[Block 1292]
དེ་ཡང་དེ་ལྟ་བུར་གྱུར་པ་ཉིད་ཀྱིས་འདི་རྣམས་དང་མི་མཐུན་པ་ཉིད་ཀྱི༌[^1121]ཕྱིར་རིག་པར་བྱའོ། །

[Block 1293]
རྒྱུ་མེད་པར་ན་བ་ཞེས་བྱ་བ་གང་ལ་ཞག་གིས་གནོད་པའི་ནད༌[^1122]དེ་ལ་སྙམ་དུ་ཤུགས་ཀྱིས་རྟོགས༌[^1123]པར་བྱའོ། །

[Block 1294]
དགེ་སློང་གི་ཚིག་ཀྱང་འདིར་འདོན་པ་ཡིན་ཏེ། གླེང་གཞིའི་མཐའ་མའི་ཞག་ལ་དེར་མཚོན་པར༌[^1124]གྱུར་པ་སྨོས་པར་རྣམ་པར་གནས་པ་ཡིན་ཏེ། ཁྱིམ་པ་ནད་པ་ལ་ཡང་སྦྱིན་པར་རིག་པའི༌[^1125]ཕྱིར། དེ་བས་ན་འདིར་ཉེ་བར་མ་བསྡུས་སོ། །

[Block 1295]
དེ་མེད་ན་སྨན་ཁང་དུའོ་ཞེས་བྱ་བ་ནི། སློང་བ་ནི་མེད་ན་དགེ་འདུན་གྱི་སྨན་ཁང་དུ་གཞག་པར་བྱའོ། །

[Block 1296]
སྨན་ཁུ་དང་མིག་སྨན་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་།[^1126] སོས་པ་ཉིད་ན་དེ་དག་ནད་པའི་ཕྱིར་སློང་ན་སྦྱིན་ནོ་ཞེས་བྱ་བ་དང་། དེ་མེད་ན་སྨན་ཁང་དུ་གཞག་གོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1297]
ད་ནི་བཞི་པ་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་འཚོ་བའི་བར་དུ་བཅང་བ་ནི་རྩ་བ་དང་། སྡོང་བུ་དང་འདབ་མ་དང་། མེ་ཏོག་དང་འབྲས་བུ་ཟས་ཀྱི་དོན་དུ་ཁྱབ་པར་བྱེད་པ་མ་ཡིན་པའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1298]
ཁ་ཟས་ཀྱི་དོན་དུ་ཁྱབ་པར་བྱེད་པ་མ་ཡིན་པ་དེ་དག་འཚོ་བའི་བར་དུ་བཅང་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1299]
དེ་ལ་རྩ་བ་དག་གང་ཞེ་ན་འདི་ལྟ་སྟེ་གླ་སྒང་དང་ཤུ་དག་དང་། ཡུང་བ་དང་། སྒེའུ་གཤེར་དང་བོང་ང་དཀར་པོ་དག་གོ། །

[Block 1300]
སྡོང་བུ་དག་གང་ཞེ་ན། ཙན་དན་དང་། སྦྱི་མོ་དང་ཤུག་པ་དང་སྲེ་ཏྲེས༌[^1127]དང་། ཐང་ཤིང་དང་སྐྱེར་པ་དག་གོ། །
--- END BLOCKS ---
