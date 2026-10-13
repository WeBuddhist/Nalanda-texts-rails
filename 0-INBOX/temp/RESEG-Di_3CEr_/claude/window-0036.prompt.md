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
ཐ་དད་ལས་གཞན་ཉིད་དུ་རྗོད་པར་བྱེད༌[^974]ན་ནི་འགལ་བ་ཉིད་དུ་འགྱུར་ན་འོན་ཀྱང་། དེ་བཞིན་མིན།[^975] དེ་ནི་ཁོ་ན་ཞིག༌[^976]སྒྲུབ་པའི་འགལ་བ་ཉིད་ཡིན་ཏེ། [^977]བཟློག་པ་སྒྲུབ་པར་བྱེད་བའི་ཕྱིར་རོ། །

[Block 1262]
གྲུབ་པའི་མཐའ་དང་འགལ་བའི་ཕྱིར་ཞེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1263]
གང་ལ་སྐབས་སུ་བབ་པ༌[^978]དེ་གཏན་ལ་དབབ་པའི་ཕྱིར་ཉེ་བར་འགོད་པ་ནི་སྐབས་དང་མཚུངས་པ་སྟེ། དཔེར་ན་བདག་ནི་རྟག་པ་ཡིན་ཏེ། ལུས་ལས་གཞན་མ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1264]
འདིར་ཡང་ལུས་ལས་གཞན་མ་ཡིན་པ་ཉིད་ལས་བདག་སྤྱོད་པ་ནི་མ་ཡིན་ཏེ་འདི་ལྟར། མ་ངེས་པར་འགྱུར། གང་གི་ཕྱིར་འདི་ལྟར་རྟག་པ་ནམ་མཁའ་ལ་སོགས་པ་དང་། མི་རྟག་པ་བུམ་པ་ལ་སོགས་པ་གཉིས་ཀ་ལ་ལུས་ལས་གཞན་མ་ཡིན་པ་ཉིད་མཐོང་བ་དེའི་ཕྱིར་ཅི་འདི་རྟག་པ་ཡིན་ནམ། འོན་ཏེ་མི་རྟག་པ་ཡིན་ཞེས་དཔྱོད་པར་བྱེད་དོ། །

[Block 1265]
དེའི་ཕྱིར་འདི་མ་ངེས་པ་ལས་ཐ་དད་དུ་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1266]
བསྒྲུབ་བྱ་དང་ཁྱད་པར་མེད་པས་སྒྲུབ་པའི༌[^979]ཕྱིར་བསྒྲུབ་བྱ་དང་མཚུངས་པ་སྟེ། དཔེར་ན་སྒྲ་རྟག་སྟེ་རེག་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་བློ་བཞིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1267]
འདིར་ཡང་སྒྲ་ལ་རེག་པར་བྱ་བ་མ་ཡིན་པའི་གཏན་ཚིགས་གྲུབ་པའི་ཕྱིར།[^980] མ་གྲུབ་མིན། གང་དེར་གཏན་ཚིགས་མ་གྲུབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 1268]
གང་ལས་བསྒྲུབ་བྱ་དང་ཁྱད་པར་མེད་པ་ཉིད་ཀྱིས་བསྒྲུབ་བྱ་དང་མཚུངས་པར་འགྱུར། འོན་ཀྱང་འདིར་དཔེ་བསྒྲུབ་བྱ་དང་མཚུངས་པར་འགྱུར་རོ། །

[Block 1269]
གཞན་དུ་རྟོག་པར་བྱེད་དེ། དཔེ་གང་ལ་བསྒྲུབ་བྱས་ཁྱད་པར་དུ་མ་བྱས་པའི་གཏན་ཚིགས་དེ་བསྒྲུབ་བྱ་དང་ཁྱད་པར་མེད་པ་ཡིན་ནོ་ཞེས་ཡང་དག་པར་བརྟག་དཔྱད་བྱེད་པ་ནི་གཞི་མཐུན་པ་རྣམས་འབྲུ་མང་པོ་པའོ། །

[Block 1270]
ཐམས་ཅད་དུ་ནི་འཐོབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 1271]
ཁས་བླངས་ནས་ཀྱང་གཏན་ཚིགས་མ་གྲུབ་པ་སྟེ། འདི་བསྒྲུབ་བྱ་དང་ཁྱད་པར་མེད་པའི་དཔེ་ནི་མ་ཡིན་ནོ། །

[Block 1272]
འོན་ཀྱང་འདི་ལྟར་ངག་འདུས་པ་ལ་ཡིན་ནོ། །

[Block 1273]
དེའི་ཕྱིར་མ་གྲུབ་པ་འབའ་ཞིག་མ་ཡིན་གྱི་གཏན་ཚིགས་ལྟར་སྣང་བ་ཡང་ཡིན་ནོ། །

[Block 1274]
དེ་ལྟར་ཞེ་ན། ཆོས་གང་གཏན་ཚིགས་ཉིད་དུ་ཉེ་བར་བསྟན་པ་དེ་ཆོས་ཅན་ལ་མ་གྲུབ་པའམ། རྒོལ་བ་དང་ཅིག་ཤོས་ལས་མ་གྲུབ༌[^981]པའམ། ཐེ་ཚོམ་ཟ༌[^982]ན་ཡང་ངོ་། །དུས་ལས་ནུར་ནས་བརྗོད་པ་ནི་དུས་ལས༌[^983]འདས་པ་སྟེ། དཔེར་ན་སྒྲ་མི་རྟག་སྟེ། བུམ་པ་བཞིན་ནོ་ཞེས་བརྗོད་པ་ལ་གཏན་ཚིགས་མ་བརྗོད་དོ་ཞེས་སྨྲས་པ་དང་བྱས་པའི་ཕྱིར་རོ་ཞེས་བརྗོད་པ་ལྟ་བུའོ། །

[Block 1275]
འདི་ཡང་མ་ཚང་བ་བརྗོད་པའམ། ངེས་པར་བྱ་བའི༌[^984]དོན་དུ་ཕྱིས་རྗོད་པར་བྱེད་པ་ཡིན་ཡང་རུང་ཕྱིས༌[^985]གཉིས་ཀ་ཡང་གཏན་ཚིགས་ལྟར་སྣང་བར་མི་སྦྱོར་རོ། །

[Block 1276]
ཅིའི་ཕྱིར་མ་ཚང་བ༌[^986]བསྒྲུབ་བྱ་གྲུབ་པའི༌[^987]ཕྱིར། གལ་ཏེ་རེ་ཞིག་མ་ཚང་བ་བརྗོད་པ་ལྟར་ན་ནི་དེ་ཉུང་བ༌[^988]ཡིན་པའི་ཕྱིར་མ་ཚང་བ་ཡིན་པས་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་གཏན་ཚིགས་ལྟར་སྣང་བ་མ་ཡིན་ནོ། །

[Block 1277]
གལ་ཏེ་ངེས་པར་བྱ་བའི་དོན་དུ་ཕྱིས་རྗོད་པར་བྱེད་ན་ནི་དེ་ལྟ༌[^989]ན་གཏན་ཚིགས་ཀྱི་མཚན་ཉིད་དུ་འཐད་པ་ཉིད་ཀྱི༌[^990]བསྒྲུབ་བྱ་གྲུབ་པ་ཡིན་གྱི་གཏན་ཚིགས་ལྟར་སྣང་བ་མ་ཡིན་ནོ། །

[Block 1278]
གཏན་ཚིགས་ཀྱི་གནས་སུ་ཡོད་བཞིན་པ་དེ་གཏན་ཚིགས་ལྟར་སྣང་བའི་མཚན་ཉིད་མ་ཡིན་པའི་ཕྱིར་འདི་གཏན་ཚིགས་ལྟར་སྣང་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1279 [HEADING]]
#### བྱེ་བྲག་པ་རྣམས་ཀྱི་གཏན་ཚིགས་ལྟར་སྣང་བ། ^3-4-3-0

[Block 1280]
བྱེ་བྲག་པ་རྣམས་ཀྱི་གཏན་ཚིགས་ལྟར་སྣང་བ་ནི་གསུམ་སྟེ། མ་གྲུབ་པ་དང་། མ་བསྟན་པ་དང་། ཡོད་པ་མ་ཡིན་པར་ཐེ་ཚོམ་ཟའོ་ཞེས་བྱ་བའི་གཏན་ཚིགས་ལས་སོ་ཞེས་ཟེར་རོ། །

[Block 1281]
མ་གྲུབ་པ་ནི་རེ་ཞིག་གཏན་ཚིགས་ལྟར་སྣང་བ་མ་ཡིན་ནོ། །

[Block 1282]
འདི་ལྟར་དཔེ་ལ་མེད་པའམ། མ་གྲུབ་པའི་དོན་ཉིད་ཡིན་ཡང་རུང་སྟེ། གཏན་ཚིགས་ཀྱི་དོན་དུའོ་ཞེས་བྱ་བ་ནི་འམ་ཞེས་རྣམ་པར་རྟག༌[^991]པའི་སྒྲ་ཡིན་ནོ། །

[Block 1283]
དེ་ལྟ་ན་ནི་དཔེ་ལ་རབ་ཏུ་གྲུབ་པ་ཡིན་ནོ། །

[Block 1284]
ཅི་སྟེ་ཡང་བསྒྲུབ་པར་བྱ་བ་ཉིད་མ་གྲུབ་པར་བརྗོད་དོ་ཞེ་ན། དེ་ལྟ་ན་ནི་གཏན་ཚིགས་ཀྱི་དོན་དུ་འགལ་བར་འགྱུར། གྲུབ་པ་སྔོན་དུ་འགྲོ་བ་ཅན་ལས་བསྟན་པར་བྱའོ་ཞེས་བྱ་བ་འདི་ལ་ནི་འབྲེལ་པའི་དུས་ན་རབ་ཏུ་གྲུབ་པའོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1285]
ཡོད་པ་མ་ཡིན་པ་ནི་མེད་ལ་ཐེ་ཚོམ་ཡང་མ་ཡིན་ནོ། །

[Block 1286]
རྭ་ཅན་ཉིད་ནི་གྲུབ་པ༌[^992]ཡིན་པའི་ཕྱིར་གྲུབ་པར་བྱས་ནས་དེ་ལ་དཔེར་བརྗོད་པ། གལ་ཏེ་རྭ་ཅན་ཡིན་ན་ནི་རྟའམ་བ་ལང་གཅིག་ཡིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1287]
ཅི་སྟེ་ཡང་ཡོད་པ་མ་ཡིན་པའི་གཏན་ཚིགས་ནི་ཡོད་པ་མ་ཡིན་པ་སྟེ་ཡིད་གཉིས་ཅན་གྱི་གཏན་ཚིགས་ནི་ཐེ་ཚོམ་དུ་འགྱུར་རོ་ཞེ་ན། རེ་ཞིག་ཡོད་པ་མ་ཡིན་པའི་གཏན་ཚིགས་མ་ཡིན་ཏེ། ཡོད་པ་མ་ཡིན་པ་ཙམ་ནི་མི་རྟོགས་སོ། །

[Block 1288]
དེ་ལྟར་ཡོད་པ་མ་ཡིན་པ་ཙམ་ཤེས་པར་འགྱུར་བ་ནི་མེད་ཀྱི་འོན་ཀྱང་བཟློག་པ་ཡིན་ནོ། །

[Block 1289]
དེ་ལ་རྭ་ཅན་ལས་ནི་རྟ་མ་ཡིན་གྱི། ཤེས་པ་སྐྱེའི། དེའི་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1290]
དེའི་ཕྱིར་བཟློག་པ་བསྒྲུབ་པའི༌[^993]ཕྱིར་འགལ་བ་ཉིད་ཡིན་ནོ། །

[Block 1291]
དོགས་པ་ཅན་གྱི་གཏན་ཚིགས་ནི་ཐེ་ཚོམ་དུ་བརྗོད་པར་བྱའོ། །

[Block 1292]
མ་ཚང་བརྗོད་པ་ཡིན། རྭ་ཅན་ཡིན་པའི་ཕྱིར་བ་ལང་ངོ་ཞེས་བྱ་བ་དེ་དག་ཉིད་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་ནི་མ་ཡིན་གྱི་འདི་ལྟར་ཐུན་མོང་མ་ཡིན་པ་ཡང་སྟེ༌[^994]དཔེར་ན་རྫས་དྲུག་ལ་རྣ་བས་གཟུང་བར་བྱ་བ་ཉིད་དེ་ནི་ཐམས་ཅད་ལ་མེད་པ་སྟེ་ཡུལ་དུ་མ་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་སོ། །

[Block 1293]
གལ་ཏེ་བྱེ་བྲག་གཉིས་ཀ་ལ་མཐོང་བའི་ཕྱིར་དེ་སྤྱི་ཉིད་ཡིན་ཏེ། བསྒྲེང་བ་བཞིན་ནོ་ཞེ་ན། དེ་མི་རིགས་ཏེ་གང་བཟློག་པ་མེད་པ་དེ་ནི་དེ་ལྟར་སྣང་བའོ། །

[Block 1294]
རྫས་གཅིག་དང་ལྡན་པ་ཡིན་པའི་ཕྱིར་ཐེ་ཚོམ་དུ་མི་འགྱུར་ཆུག་ནས་ལ་སོགས་པ་ལ་ཐེ་ཚོམ་ཡིན་ནོ། །

[Block 1295]
འདི་ཐམས་ཅད་ལས་ལོག་པ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 1296]
དེའི་ཕྱིར་རྣམ་པ་ཀུན་ལ་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་གཞན་ཐུན་མོང་མ་ཡིན་པ་ཉིད་ནི་མི༌[^995]བརྗོད་དོ། །

[Block 1297]
དེ་བཞིན་དུ་འགལ་བ་དང་མ་ངེས་པའི་མཐའ་ཅན་དུ་མ་བརྗོད་དོ།[^996] །

[Block 1298]
ཇི་སྐད་དུ་ས་ལ་སོགས་པ་འདུས་ནས་ལུས་པོ་བརྩམས་པར་བརྗོད་པ་ལ་ཅི་རང་རང་གི་རིགས་སུའམ་ཞེས་ཐེ་ཚོམ་དུ་འགྱུར་ཏེ། ལྔའི༌[^997]རྟགས་དམིགས་པའི་ཕྱིར་དང་། རིགས་མི་མཐུན་གྱི་རྩོམ་པ༌[^998]བཀག་པའི་ཕྱིར་རོ་ཞེས་སོ། །

[Block 1299]
ཐེ་ཚོམ་གྱི་མདོ་དེ་ཙམ་གྱིས་མི་ཆོག་གོ་ཞེས་བརྗོད་དོ། །

[Block 1300]
འདིར་ཡང་སྤྱིར་མངོན་སུམ་པ་ལས༌[^999]ཡང་ཨུཏྤ་ལའི་དཀར་པོ་ལས་ཡོན་ཏན་ཉིད་དང་བརྟེན་པ་ཉིད་དང་ཡོན་ཏན་མེད་པ་ཉིད་རྣམས་ལ་ངེས་པར་མཐོང་གི་ཐེ་ཚོམ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
