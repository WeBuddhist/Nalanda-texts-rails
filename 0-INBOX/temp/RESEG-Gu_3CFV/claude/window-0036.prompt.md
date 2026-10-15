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
ཕྱོགས་དེ་ལས་གཞན་དུ་ནི་ལྟུང་བ་མེད་ཅེས་བྱ་བའི་དོན་འདི་བསྒྲུབ་པའི་དོན་དུའོ། །

[Block 1262]
འོ་ན་འདི་ལྟར་སྣང་བ་དང་བཅས་པ་ཉིད་ལ་ཕྱོགས་གཅིག་ཏུ་སྣང་བ་དང་བྲལ་བའི་ཕྱོགས་ལ་སྣང་དུ་རུང་བ་ཉིད་ཡོད་དོ་ཞེ་ན། བདེན་མོད་ཀྱི་འོན་ཀྱང་འདི་ནི་ལོངས་སྤྱོད་ཅན་གྱི་ཡོ་ལང་སྤང་བའི་ཕྱིར་ཡིན་གྱི། ལྟ་བའི་ཕྱིར་བཀག་པ་ནི་མ་ཡིན་ནོ། །

[Block 1263]
འདིར་གླེང་གཞི་ནི་གཙོ་བོ་མ་ཡིན་ཏེ། ཟླ་བ་དང་ཉི་མ་དག་ལས་སྤང་བ་མ་ཡིན་པ་ཉིད་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 1264]
ཉལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཉིད་ལོག་པ་ལས་འདའ་བར་བྱ་སྟེ། དེ་ཉལ་ན་མཚན་མོའི་མཐར་ནི་དངོས་གཞིར་འགྱུར་བའི་ཉེས་བྱས་སོ། །

[Block 1265]
མདུན་རོལ་དུ་ནི་སྦྱོར་བར་འགྱུར་བའི་ཞེས་བྱ་བ་འདི་འདིར་རྟོགས་པར་བྱའོ། །ཅི་རྣམ་པ་ཐམས་ཅད་ཉིད་ཀྱིས་དེ་ལྟ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ནད་པ་དང་། ནད་གཡོག་གི་དབང་ཉིད་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ནད་པའི་དབང་ཉིད་དང་ནད་གཡོག་གི་དབང་ཉིད་ཀྱིས་དེར་ཉལ་བ་ནི་མ་གཏོགས་སོ། །

[Block 1266]
འདི་ལ་ཁ་ཅིག་ནི་ལྟུང་བྱེད་ཅེའོ་ཞེས་བྱ་བ་ནི་འདིར་སྣང་བ་དང་བཅས་པའི་ཁྱིམ་གྱི་ཕྱོགས་སུ་ཉལ་བ་འདི་ལ་འདུལ་བ་འཛིན་པ་ཁ་ཅིག་ནི་ལྟུང་བྱེད་དུ་འདོད་དོ། །

[Block 1267]
དེ་ནི་མི་རིགས་ཏེ་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག༌[^781]ཏུ་ཉལ་ན་ཞེས་སྨོས་པ་ཡིན་ཏེ། དེ་བས་ན་དགེ་སློང་གིས་སྣང་བ་དང་བཅས་པའི་གནས་སུ་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་ཉལ་བར་མི་བྱའོ། །

[Block 1268]
ཉལ་ན་ལྟུང་བྱེད་དོ། །

[Block 1269]
འདིར་གཞུང་ནི་ཀློག་པ་ཁ་ཅིག་ལས་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་ཉལ་བ་འདི་ལ་དེའི་འོག་ཏུ་ལྟུང་བྱེད་བཅའ་བར་མཛད་དེ། འདིར་སྣང་བ་དང་བཅས་པར་འཇུག་པ་འདི་ལ་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་ཉལ་བ་བསྡུས་པ་ནི་མ་ཡིན་ཏེ། རིགས་ཐ་དད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1270]
འདིར་ལྟུང་བྱེད་རྣམས་མི་རིགས་པས་འདི་དང་འབྲེལ་པའི་ལྟུང་བྱེད་དུ་རྣམ་པར་གཞག་པར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 1271]
ཉལ་བ་མ་ཡིན་པ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདི་དག་ཐམས་ཅད་བསླབ་པའི་གཞི་རྣམས་ལ་དང་པོར་ཉལ་བ་དང་། བསླབ་པའི་གཞི་རྣམས་ལ་ཉལ་བ་མ་ཡིན་པ་ལས་གཞན་པའི་སྤྱོད་ལམ་ལ་ནི་ཕྱེད་ཉིད་ནི་ན་སྨད་པ་བྱེད་པ་ཉིད་དོ། །

[Block 1272]
ཉལ་བ་མ་ཡིན་པ་ལ་ཤིན་ཏུ་མ་ཆོག་པ་ཉིད་དེ་སྣང་བ་དང་གཉིད་འདའ་བར་བྱེད་པ་དང་མཚན་མོའི་མཐའ་ནི་ཉེས་བྱས་སོ། །

[Block 1273]
བསྙེན་པར་མ་རྫོགས་པ་དང་བཅས་པའི་དགེ་སློང་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 1274]
བསྙེན་པར་མ་རྫོགས་པ་ལ་སོགས་པ་དང་ལྷན་ཅིག་ཏུ་ཉལ་བ་ལ་ལྟུང་བྱེད་དུ་མི་འགྱུར་ཏེ། ཉལ་བ་བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་ལ་ཉལ་བའི་ཚིག་འདི་ནི་འདིར་གཞུང་ངོ་། །གང་གི་ཕྱིར་འདུག་པ་ལ་ནི་ཉལ་བའི་ཚིག་འཇུག་པ༌[^782]ཡིན་ཏེ། རྨི་ལམ་དུ་གཉིས་པོ་ཡང་འདིར་ཡན་ལག་དང་ཡན་ལག་ཅན་དུ་གྱུར་པ་མངོན་པར་འདོད་པ་སྟེ། དེ་ལྟར་ཡང་བུད་མེད་དང་ལྷན་ཅིག་ཏུ་ཉལ་བ་ལ་ནི་དབུགས་ཕྱུང་བ་དགེ་སློང་ཡིད་བརྟན་པ་མི་འཇོག་པར་གློས་འབེབས་སམ། གཉིད་ལོག་པར་བྱེད་ན་ཞེས་བྱ་བའི་ཡན་ལག་གཉིས་གསུངས་སོ། །

[Block 1275]
ཉིན་མོ་ཐ་དད་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ཡང་ཕྱེད་ཉིད་དེ་ཞེས་བྱ་བའི༌[^783]རྗེས་སྙེག༌[^784]པའི་ཕྱིར་ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 1276]
ཉིན་མོའི་འཇུག་པ་ལ་དེའི་རིགས་དང་མི་ལྡན་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་འདིར་ཉེས་པ་དང་ལྡན་པ་ཉིད་ཤེས་པའོ། །

[Block 1277]
སྣང་བ་ལ་ཡང་འདིར་ནི་ཉི་མའི་སྣང་བ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1278]
གང་གི་ཕྱིར་མཚན་མོ་ཉི་མའི་སྣང་བ་མེད་པས་སོ། །

[Block 1279]
དེ་བས་ན་འདིས་ཉིན་མོ་ཡང་སྣང་བ་དང་བཅས་པར༌[^785]ཉལ་བས༌[^786]ལྟུང་བ་བསྟན་པར་འགྱུར་རོ། །

[Block 1280]
འཇུག་པ་འདི་གང་དེ་དང་འདྲ་བ་ཉིད་ནི་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་ཏུ་ཉལ་བ་དང་བུད་མེད་དང་ལྷན་ཅིག་ཏུ་ཉལ་བའོ། །

[Block 1281]
དེ་ལྟ༌[^787]བས་ན་འདིར་ཡང་ཉིན་མོ་ཡང་ལྟུང་བ་བསྐྱེད་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 1282]
ཕལ་ཆེར་གཡོགས་པ་དང་བསྐོར་བ་ནི་གནས་ཀྱི་མཐའ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་སླར་གཡོགས་པ་དང་གང་ཞིག་སླར་བསྐོར་བ་འདི་ནི་གནས་ཀྱི་མཐའ་ཡིན་ནོ། །

[Block 1283]
དེ་ཡང་ཐམས་ཅད་པས་དམན་པའི་གནས་དང་འདིའི་ཕྱོགས་གཅིག་མ་གཡོགས་པ་གང་ཡིན་པ་དེ་ཡང་གནས་ཉིད་དོ། །

[Block 1284]
ཅུང་ཟད་གཡོགས་ཤིང་ཐམས་ཅད་དུ་བསྐོར་བ་ལ་གཡོགས་པ་ལ༌[^788]ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིས་བྱས་པར་རིག་པར་བྱའོ། །

[Block 1285]
གནས་ནི་རྣམ་པ་བཞི་སྟེ་ཐམས་ཅད་གཡོགས་ཤིང་ཐམས་ཅད་བསྐོར་བ་དང་། ཕལ་ཆེར་གཡོགས་ཤིང་ཐམས་ཅད་བསྐོར་བ་དང་། གང་ཞིག་ཐམས་ཅད་གཡོགས་ཤིང་ཕལ་ཆེར་བསྐོར་བ་ནི་བསྒོ་བཅུ་པའམ་སྒོ༌[^789]བཅུ་གཉིས་པ་དང་། ཕལ་ཆེར་གཡོགས་ཤིང་ཐམས་ཅད་བསྐོར་བ་ཁྱམས་ངོས་བཞི་པ་དང་། གང་ཞིག་ཕལ་ཆེར་གཡོགས་ཤིང་ཕལ་ཆེར་བསྐོར་བ་ཁྱམས་ངོས་གསུམ་པའམ་འཁོར་གྱི་ཁྱམས་ལྟ་བུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1286]
གང་གིས་ངོས་བཞི་ལ་ཡང་བསྐོར་བ་དང་འབྲེལ་པའི་ངོས་ཡོད་པ་དབུས་ན་མེད་པ་དེ་ནི༌[^790]ཁྱམས་ངོས་བཞི་པའོ། །

[Block 1287]
གང་གིས་ངོས་གསུམ་དང་དབུས་སུ་ངོས་གཅིག་གིས་གཡོགས་པ་ལ་བསྐོར་བ་མེད་པ་དེ་ནི་ཁྱམས་ངོས་གསུམ་པའོ། །

[Block 1288]
ད་ལྟ༌[^791]བས་ན་རྣམ་པ་བཞི་པོ་འདི་བསྡུ་བའི་ཕྱིར༌[^792]མཐར་ཐུག་ན་ཞེས་སྨོས་སོ། །

[Block 1289]
དེའི་སྒོའི་ངོས་དང་འབྲེལ་པའི་ཉེ་འཁོར་གྱི་གནས་སུ་གྱུར་པ་ནི་དེའི་ཁོངས་སུ་གཏོགས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། སྒོ་ཡོད་པ་དེའི་གནས་སུ་གྱུར་པ་ནི་འབྲེལ་པ་སྟེ། དེའི་ཉེ་འཁོར་གང་ཡིན་པ་དེ་ལ་དེའི་གནས་སུ་གྱུར་པ་ཉིད་ནི་གཅིག་ཏུ་གྱུར་པ་ཉིད་དོ། །

[Block 1290]
གནས་དེས་ཀུན་ནས་ཡོངས་སུ་བསྐོར་བའི་ཁྱམས་རིམ་པ་གསུམ་པ་ལ་ངོས་གཡོགས་པ་གང་ཡིན་པ་དེ་ལྟ་བུར་གྱུར་པ་ནི་ཉེ་འཁོར་རོ། །

[Block 1291]
དེ་ལ་འདི་དང་ལྷན་ཅིག་གཅིག༌[^793]པ་ཉིད་ནི་གཅིག་པར་གྱུར་པ་ཉིད་དུ་ཤེས་པར་བྱ་བ་ཡང་མ་ཡིན་ནོ། །

[Block 1292]
འདིར་ཚིག་ནི་ཉེ་འཁོར་དོར་ལ༌[^794]བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1293]
འདིར་དེའི་དོན་རྣམ་པར་གནས་པ་ཡིན་ཏེ། གཙུག་ལག་ཁང་གི་ཁྱམས་ཀྱི་ཕྱིར་འདི་གསུངས་པ་ཡིན་ཏེ། གནས་མ་ཡིན་པར་གྱུར་པ་ལ་ནི་གནས་ཉིད་རིགས་པ་མ་ཡིན་གྱི། ཉེ་འཁོར་དང་བཅས་པ་ཉིད་ལྷན་ཅིག་ཏུ་གནས་པ་ཉིད་འགྱུར་བ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་འདིར་འདི་རྣམ་པར་གཞག་པའོ། །

[Block 1294]
ཉེ་འཁོར་དུ་བཅས་པ་མ་ཡིན་པ་ཉིད་ལ་ཉེ་བར་བརྟེན་པ་ཉིད་ལ་ཡང་འདི་དང་གཞན་ཡོད་པ་ཡིན་ཏེ། གནས་ཐ་དད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1295]
ཁྱེར་གཞན་བར་དུ་མ་ཆོད་པ་སྒོ་དེ་དང་འབྲེལ་པ་ཡང་ཞེས་བྱ་བ་ནི་ཁྱེར་གཞན་ནི་གང་ཞིག་གནས་སུ་གྱུར་པ་འབྲེལ་པ་བར་དུ་མ་ཆོད་པ་ཁྱེར་ཏེ་དེ་ལ་ཁྱེར་གཞན་དང་མ་འདྲེས་པ་དེ་ལ་ཡང་གལ་ཏེ་ཡོད་ན་དེ་དང་འབྲེལ་པའི་སྒོ་གཞན་དུ་ཟིན་ཀྱང་དེ་དང་འབྲེལ་པ་ཉིད་ནི་གཅིག་པར་འགྱུར་བ་ཉིད་དེ། ཁྱེར་གཞན་དང་ལྷན་ཅིག་ཏུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1296]
ཉེ་འཁོར་གྱི་རྣམ་པ་ཉིད་ཀྱིས་འདི་ལ་དེ་དང་འབྲེལ་པ་ཉིད་ཤེས་པ་ཡིན་ཏེ་ཁྱེར་གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1297]
ཁྱེར་གཞན་གྱིས་བར་དུ་ཆོད་པ་ནི། གང་ཞིག་འདི་ལ་བར་དུ་ཆོད་པ་ཉིད་དེ་ལ་ཉེ་འཁོར་གྱི་རྣམ་པ་ཉིད་དོ། །

[Block 1298]
དེ་བས་ན་འདི་ལ་དེ་དང་འབྲེལ་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 1299]
ཉེ་འཁོར་དང་བཅས་པ་ནས་གནས་ཁང་ཙམ་གྱི་ཕ་རོལ་ན་ཐ་དད་པར་གྱུར་ཅིང་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ཉེ་འཁོར་དང་བཅས་པའི་གནས་ལ་ཚད་གང་ཡིན་པ་དེ་ཙམ་གྱི་བར་ནས་གཞན་ཐ་དད་པར་གྱུར་པ་གཅིག་གམ་དུ་མའི་གང་ཟག་གིས་ལྷག་པར་གནས་པ་ལ་དེ་དང་འབྲེལ་པ་ཉིད་ནི་མ་ཡིན་ལ་གནས་ངེས་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1300]
གཡོགས་པ་གཅིག༌[^795]ཆ་ཅན་བཀབ་པ་འདི་ཡིན་ཏེ་ཞེས་བྱ་བ་འདིར་ཧ་ཅང་ཐལ་བས་གནས་གཅིག༌[^796]ཉིད་དུ་རྟོགས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
