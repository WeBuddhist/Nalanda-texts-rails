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
ཞེས་འབྱུང་ངོ་། །གཞན་ཡང་རྟོག་པ༌[^894]དང་ལྡན་པའི་ཕྱིར་ཐར་པར་མི་འགྱུར་ཏེ། གང་གི་བྱ་བའི་ཕྱོགས་ནི་མེ༌[^895]མཆོད་པ་དང་། ཁ་དོན༌[^896]དང་ཁྲུས་ལ་སོགས་པ་དང་ལྡན་པའི་ཕྱིར་ཏེ་རྟོག་པ་དང་བཅས་པའོ། །

[Block 1262]
ཐམས་ཅད་འདོར་བའི་རང་བཞིན་ནི་མི་རྟོག་པ་སྟེ་ཐར་པའོ། །

[Block 1263]
དེ་བས་ན༌[^897]རྟོག་པ་དང་བཅས་པའི་ལམ་གྱིས་མི་རྟོག་པའི་ཐར་པ་ཐོབ་པར་མི་འགྱུར་ཏེ། རྒྱུ་མི་འདྲ་བའི་ཕྱིར་རོ། །

[Block 1264]
[^898]ནས་ཀྱི་ས་བོན་ལས་སཱ་ལུའི་འབྲས་བུ་མི་འབྱུང་བ་བཞིན་ནོ། །

[Block 1265]
དེ་བས་ན་རྟོག་པ་ཐམས་ཅད་ཡོངས་སུ་སྤངས་པའི་ཏིང་ངེ་འཛིན་གྱིས་རྟག་ཏུ་དྲི་མ་མེད་པ་ཟག་པ་མེད་ཅིང་རྣམ་པར་མི་རྟོག་པའི་ཐར་པ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1266]
དེ་བས་ཁྱེད་ཅག་གི་བྱ་བའི་ཕྱོགས་སུ་འབྲས་བུ་གང་ཡང༌[^899]ཐོབ་པར་མི་འགྱུར་རོ་ཞེས་དཔྱོད་པ༌[^900]པ་རྣམས་ཀྱིས་གཙང་སྦྲ་ལ་སོགས་པ་ངལ་བ་དོན་མེད་དུ་འགྱུར་རོ། །

[Block 1267]
ཇི་སྐད་དུ།

[Block 1268 [VERSE]]
ཁྲུས་ཀྱིས་དགེ་འདོད་རིགས་ཀྱིས་བརྙས་པ་དང་། །
རིག་བྱེད་ཚད་མར་བྱེད་པ་ཁ་ཅིག་ཡོད། །
སྡིག་པ་ཟད་ཕྱིར་དཀའ་ཐུབ་ལ་བརྟེན་པ། །
བློ་མེད་རྣམས་ཀྱི༌[^901]བླུན་པོའི་རྟགས་ལྔའོ། །

[Block 1269]
ཞེས་བྱ་བའི་ཕྱོགས་ཀྱི་དཔྱོད་པ་པ་རྣམས་ལ་ལན་ནོ། །

[Block 1270]
ཡེ་ཤེས་ཀྱི་ཕྱོགས་སུ་ཡང་ཆོས་གོས་ལ་སོགས་པ་འཛིན་པ་ནི་འགལ་བའོ། །

[Block 1271]
རིག་བྱེད་ཀྱི་མཐའ་གསང་བར་སྨྲ་བ་བྲམ་ཟེ་རྣམས་ཀྱི་ཐམས་ཅད་འདོར་བའི་ཡེ་ཤེས་ཅན་གྱི་ཕྱོགས་སུ་ཆོས་གོས་འཛིན་པ་དང་། གཙུག་ཕུད་འཛིན་པ་དང་། དབྱུག་པ་གསུམ་པ༌[^902]དང་། ཐིག་ལེ་གསུམ༌[^903]སྤྲས་པ་དང་། ཀྲྀཥྞ་ས༌[^904]རའི་པགས་པ་གྱོན་པ་དང་། ཡུལ་ནས་ཡུལ་དུ་འཁྱམ་པ༌[^905]ལ་སོགས་པ་ནི་འགལ་བའོ། །

[Block 1272]
དང་པོ་དམ་པའི་རྣལ་འབྱོར་ལ་གནས་པའི་བརྟུལ་ཞུགས་པ་རྣམས་ཀྱིས་དེ་དག་ཐམས་ཅད་སྤྱོད་པ་ནི་ཆོས་གོས་ལ་སོགས་པས་དེ་ཁོ་ཉིད༌[^906]ཐོབ་པ་མ་ཡིན་ཏེ་སྤྲོས་པ་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 1273]
སྤྲོས་པ་མེད་པའི་རྒྱུས་སྤྲོས་པ༌[^907]མེད་པའི་འབྲས་བུ་བསྐྱེད་པ་ཡིན་གྱི་སྤྲོས་པ་དང་བཅས་པ༌[^908]ནི་མ་ཡིན་ནོ། །

[Block 1274]
ཇི་སྐད་དུ།

[Block 1275 [VERSE]]
གཞན་རྐྱེན་མེད་ཅིང་ཞི་བ་སྟེ། །
སྤྲོས་པ་དག་གིས་མ་སྤྲོས་པ། །
ཐ་དད་དོན་མིན་རྣམ་མི་རྟོག །
འདི་ནི་ཡང་དག་མཚན་ཉིད་དོ། །

[Block 1276]
ཞེས་འབྱུང་ངོ་། །དེའི་ཕྱིར་རང་གི་ཕྱོགས་ཁས་བླངས་པ་མ་གྲུབ་སྟེ་ཚད་མ་མེད་པའི་ཕྱིར་རོ། །

[Block 1277]
གཞན་ཡང་དེ་རྣམས་ཀྱི་ཕྱོགས་ནི་སྣ་ཚོགས་ཀྱི་ངོ་བོ་དངོས་པོ་ཐམས་ཅད་གང་སྣང་བ་དེ་ནི་ཚངས་པ་ཉིད་ཁོ་ནའོ། །

[Block 1278]
དཔེར་ན་བུམ་པ་དང་རེ་ལྡེ་ལ་སོགས་པ་ཕྱི་རོལ་དུ་སྣང་བ་གང་ཡིན་པ་དེ་དག༌[^909]རྣམ་པར་དཔྱོད་པ༌[^910]ན་རང་གཟུགས་སུ་ཡོད་པ་མ་ཡིན་ཏེ་སྣང་བ་གུད་ན༌[^911]མེད་པའི་ཕྱིར་རོ། །

[Block 1279]
སྣང་བ་ཡང་བདག་ཉིད་ཀྱིས་ཡོད་ཀྱི་འདི་ཉིད་ཀྱིས་ནི་རིག་པ་མ་ཡིན་ནོ། །

[Block 1280]
བདག་ཉིད་དང་འདི་ཉིད་ཅེས་ཕན་ཚུན་འགལ་བའོ། །

[Block 1281]
དེའི་ཕྱིར་སྣང་བར་གྱུར་པའི་བདག་ཉིད་ཀྱིས་བསྡུས་པའི་དངོས་པོ་སྣང་བ་གང་ཡིན་པ་དེ་ཉིད་ཚངས་པ་ཉིད་དོ། །

[Block 1282]
རྟག་ཏུ་དགའ་བའི་བདག་ཉིད་བག་ཆགས་སྣ་ཚོགས་དང་བཅས་པ་དེ་ཉིད་ཀྱི་དབྱེ་བ་འདི་དག་གོ། །

[Block 1283]
ཇི་སྐད་དུ། ཚངས་པའི་ཚུལ་ནི་དགའ་བ་སྟེ། །ཞེས་བྱ་བ་ལ་སོགས་པ་འབྱུང་ངོ་ཞེས་ཚངས་པས༌[^912]སྨྲ་བ་རྣམས་ཀྱི་རང་གི་ཕྱོགས་ཏེ་དེ་མི་རིགས་པ་ནི་ཚད་མ་མེད་པའི་ཕྱིར་རོ། །

[Block 1284]
ཚངས་པ་ཉིད་ཡོད་པའི་ཚད་མ་མཐོང་བའོ། །

[Block 1285]
རེ་ཞིག་མངོན་སུམ་ཡང་མ་ཡིན་ཏེ་མི་རྟོག་པའི་ཕྱིར་རོ། །

[Block 1286]
ཚངས་པའི་སྣ་ཚོགས་པ་ཉིད་ནི་རྣམ་པར་རྟོག་པས་འཇོག་པར་བྱ་བས་སོ། །

[Block 1287]
དེ་ལྟ་ན་གཞན་ཡང་རྟོག་པ་དང་བཅས་པའང་མངོན་སུམ་མ་ཡིན་ནམ། ཇི་སྐད་དུ།

[Block 1288 [VERSE]]
དང་པོ་མཐོང་བའི་ཤེས་ཡོད་དེ། །
རྟོག་པ་ཐམས་ཅད་རྣམ་བྲལ་བ། །
བྱིས་པ་ལྐུགས་པ་དང་འདྲ་བའི།[^913] །
ཤེས་པ་དག་པའི་དངོས་ལས་བྱུང་། །

[Block 1289 [VERSE]]
དེ་ལས་གཞན་པའི་དངོས་པོ་ནི། །
སྐྱེས༌[^914]སོགས་ཆོས་བཅས་གང་གིས་ནི། །
བློ་ཡིས་རྟོགས་པ༌[^915]དེ་ཉིད་ཀྱང་། །
མངོན་སུམ་ཉིད་དུ་འདོད་པ་ཡིན། །

[Block 1290]
ཞེས་འབྱུང་ངོ་། །

[Block 1291]
དེ་ལ་སྨྲས་པ།

[Block 1292]
དང་པོ་མི་རྟོག་པ་ཁོ་ན་ཚད་མ་ཡིན་ཏེ། གང་གི་རང་གི་མཚན་ཉིད་ཀྱི༌[^916]དོན་གྱི་བྱ་བ་བྱེད་ནུས་པ་ཡུལ་དང་རྒྱུ་ཡིན་པ་དེ་ཉིད་མི་རྟོག་པ་ཚད་མའོ། །

[Block 1293]
དེ་ཉིད་ཀྱིས་བྱ་བ་བྱས་པའི་ཕྱིར་གཞན་ནི༌[^917]བརྟགས་པ་ལ་བརྟག་པ༌[^918]དང་མཚུངས་པ་དོན་མེད་པ༌[^919]ནི་ཚད་མ་མ་ཡིན་ནོ། །

[Block 1294]
དོན་དང་ཕྲད་པར་བྱེད་པ་ནི་མ་ཡིན་ཏེ། བསྟན་པའི་དོན་ལ་སྐྱེས་བུ༌[^920]འཇུག་པ་ན་དེ་ཐོབ་པས་ཚད་མའི་བྱ་བ་དེ་ཉིད་དུ་རྫོགས་སོ། །

[Block 1295]
དེ་ལྟ་བུའི་མཚན་ཉིད་དང་པོ་ཁོ་ན་ལ་ཡོད་ཀྱི།

[Block 1296]
གཉིས་པ་ལ་མ་ཡིན་ནོ། །

[Block 1297]
དེའི༌[^921]ཕྱིར་མི་རྟོག་པའི་བདག་ཉིད་མངོན་སུམ་གྱི་ནི་དེ་ཡུལ་མ་ཡིན་ནོ། །

[Block 1298]
གང་གི་ཡུལ་ཡིན་པ་དེ་ནི་ཚད་མ་མ་ཡིན་ནོ་ཞེས་ཚངས་པ་ཉིད་ལ་ཡོད་པ་ལ་མངོན་སུམ་མི་འཇུག་གོ། །

[Block 1299]
རྗེས་སུ་དཔག་པ་ཡང་དེ་བཞིན་ཏེ་གང་གི་ཕྱིར་རྗེས་སུ་དཔག་པ་ནི་རྟགས་དང་རྟགས༌[^922]ཅན་གྱི་འབྲེལ་པ་སྔོན་དུ་འགྲོ་བར་འཇུག་པར༌[^923]འགྱུར་ཏེ། དུ་བ་དང་མེ་བཞིན་ནོ། །

[Block 1300]
ཚངས་པ་དེའི་འབྲས་བུར་གྱུར་པའི་རྟགས་གང་ཡང་མ༌[^924]མཐོང་སྟེ། གང་གིས་དེ་མཐོང་བ་མེད་པར་མི་འབྱུང་བས་རྟགས་ཅན་དུ་གྱུར་པ་ཚངས་པ་ཉིད་དཔག་པར་བྱའོ། །
--- END BLOCKS ---
