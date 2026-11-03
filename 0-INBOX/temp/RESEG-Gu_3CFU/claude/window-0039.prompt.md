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
[Block 1366]
ཕྲན་ཚེགས་ལས་ཆོ་ག་གཉིས་པ་འདི་འདྲ་བ་ནས༌[^970]དྲངས་པའོ། །

[Block 1367]
ལེན་པ་ཉིད་ན་ཡང་སྐྱེའོ་ཞེས་བྱ་བ་ནི་སྡོམ་པ་ཡང་དག་པར་ལེན་པ་ཉིད་ལ་དེའི་ཚེ་ན་མཚན་གྱུར་ན་ཡང་སྡོམ་པ་སྐྱེ་བ་ཉིད་ཡིན་ནོ། །

[Block 1368]
འདིར་གཞུང་ནི་བསྙེན་པར་རྫོགས་པར་འཚལ་བའི་མཚན་གྱུར་ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱི་འམ་བསྙེན་པར་མ་རྫོགས་ཞེས་བགྱི། བཀའ་སྩལ་པ། བསྙེན་པར་རྫོགས་ཞེས་བྱ་སྟེ། དགེ་སློང་མས་ནི་དགེ་སློང་རྣམས་ལས་བསྙེན་པར་རྫོགས་པ་དགེ་སློང་མའི་དངོས་པོ་ཡོངས་སུ་བཙལ་བར་བྱ་བའི་ཕྱིར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1369]
འདི༌[^971]ཕོའི་མཚན་གྱུར་པ་ནི་དཔེ་ཙམ་དུ་ཟད་དོ། །

[Block 1370]
གཞན་དུ་ཆོ་ག་འདི་ལ་ཤིན་ཏུ་དོགས་པ་དང་བྲལ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1371]
བསྙེན་པར་རྫོགས་པར་གྱུར་པའི་གནས་སྐབས་ཅན་འདི་ནི་བསྙེན་པར་རྫོགས་པར་ལྟ་བ་གཟུང་བ་སྟེ། ཡོངས་སུ་གྱུར་པའི་སྔ་རོལ་དུ་དགེ་སློང་ཙམ་བསྡུས་པ་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 1372]
དེ་དང་ལྡན་པའི་ལྟར་མཁན་པོ་མེད་པ་ཉིད་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། དེ་དང་ལྡན་པའི་ཞེས་བྱ་བ༌[^972]ནི་མཁན་པོ་དང་ལྡན་པ་ལ་དེའི་སྡོམ་པ་སྐྱེ་བ་ལྟར་མཁན་པོ་མེད་པ་ཉིད་ལ་ཡང་སྡོམ་པ་སྐྱེ་བ་ཡིན་ནོ། །

[Block 1373]
དེ་བསྙེན་པར་མ་རྫོགས་པ་ཉིད་ཡིན༌[^973]ཡང་ངོ་ཞེས་བྱ་བ་ནི་མཁན་པོ་དེ་བསྙེན་པར་རྫོགས་པ་ཉིད་ཡིན་ན་ཡང་མཁན་པོ་དང་ལྡན་པའི་སྡོམ་པ་སྐྱེ་བ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1374]
དེ་དགེ་སློང་ཉིད་མ་ཡིན་པར་ཤེས་ན་ནི་མི་སྐྱེའོ་ཞེས་བྱ་བ་ནི་ཡང་དག་པར་ལེན་པར་བྱེད་པ་པོས་མཁན་པོ་དེ་བསྙེན་པར་མ་རྫོགས་པ་ཉིད་དམ་ཉམས་པ་ཉིད་ཡིན་པས་དགེ་སློང་ཉིད་མ་ཡིན་པར་ཤེས་ནས་ནི་མཁན་པོ་དང་ལྡན་པའི་སྡོམ་པ་མི་སྐྱེ་བ་ཁོ་ནའོ། །

[Block 1375]
འདིར་གཞུང་ནི་བསྙེན་པར་རྫོགས་པར་འཚལ་བ་མཁན་པོ་རྐུ་ཐབས་སུ་གནས་པས་བསྙེན་པར་རྫོགས་པར་བགྱིད་ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱིའམ། བསྙེན་པར༌[^974]མ་རྫོགས་ཞེས་བགྱི། བཀའ་སྩལ་པ། གལ་ཏེ་བདག་གི་མཁན་པོ་རྐུ་ཐབས་སུ་གནས་པ་ཡིན་ནོ་ཞེས་ཤེས་ན་ནི་བསྙེན་པར་མ༌[^975]རྫོགས་པར་ཤེས་པར་བྱའོ། །

[Block 1376]
གལ་ཏེ་མི་ཤེས་ན་ནི་བསྙེན་པར་རྫོགས་ཞེས་བྱའོ། །

[Block 1377]
སྔོན་ལྟུང་བ་བྱུང་བའམ་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 1378]
དང་པོར་ཡེངས་པ་ཁྱིམ་པའི་མཁན་པོས༌[^976]ཤེས་པར་བྱའོ། །

[Block 1379]
འོ་ན་མཁན་པོ་མེད་པ་ཉིད་ལ་ཡང་སྡོམ་པ་སྐྱེ་ན། དེ་བས་ན་ཇི་ལྟར་ཤེས་བཞིན་དུ་འདི་ལ་དགེ་སློང་མ་ཡིན་པ་ཉིད་དུ་མི་འགྱུར་བ་གང་གི་ཕྱིར་མི་ལྡན་པ༌[^977]ཤེས་པའི་བསམ་པ་གྱུར་པ་དང་ཚུལ་ཁྲིམས་ལ་མ་གུས་པའི་བསམ་པར་འགྱུར་རོ། །

[Block 1380]
ཚུལ་ཁྲིམས་ལ་དོན་དུ་མི་གཉེར་བར་འགྱུར་རོ༌[^978]ཞེས་བྱ་བ་དེའི་ཕྱིར་འདི་སྐྱེའོ་ཞེ་ན། དེ་མ་ཡིན་ཏེ། མཁན་པོ་ཉིད་མ་ཡིན་པ་ཇི་སྲིད་དུ་ཤེས་ན་དེའི་ཕྱིར་འདིར་སྐྱེ་བ་ལ་འགལ་བ་མེད་པ་གང་ཞིག་མཁན་པོ་ཉིད་བསྙེན་པར་རྫོགས་པ་མ་ཡིན་པ་ལ་སྡོམ་པ་སྐྱེ་བར་བརྗོད་པ་དེ་ནི་དགེ་འདུན་གྱི་དབང་དུ་མཛད་ན། དགེ་འདུན་གྱིས་བསྙེན་པར་རྫོགས་པ་ཉིད་མ་ཡིན་པ་ཤེས་བཞིན་པ་ལ་སྐྱེ་བ་ཡིན་གྱི། བསྙེན་པར་རྫོགས་པར་ལྟ་བས་ནི་མ༌[^979]ཡིན་ཞེས་བྱ་བའོ། །

[Block 1381]
དེའི་ཕྱིར་སྤོང་བ་ལ་ཡང་མི་སྐྱའོ་ཞེས་བྱ་བ་ལ་སྡོམ་པའི་སྒོ་ཉིད་ཀྱི་ཕྱིར་མཁན་པོ་ལ་དེའི་ཕྱིར་དབུལ་ཞིང་ཕྱིར་སྤོང་བར་བྱེད་ན་དེ་ལ་ཡང་སྡོམ་པ་མི་སྐྱེའོ། །

[Block 1382]
འདིར་གཞུང་ནི་བསྙེན་པར་རྫོགས་པར་བགྱིད་པ་ནི་སླར་མཁན་པོ་སྤོང་བར་བགྱིད་ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱིའམ། བསྙེན་པར་མ་རྫོགས་ཞེས་བགྱི། བཀའ་སྩལ་པ། བསྙེན་པར་མ་རྫོགས་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1383]
དེ་གཉིས་ཀྱི་མིང་མ་བརྗོད་ན། ཡང་མི་སྐྱེའོ་ཞེས་བྱ་བ་ནི་ཞིང་དང་མཁན་པོ་འདི་དག་ལ་ཡང་དག་པར་ལེན་པར་བྱེད་པ་འམ། ལས་བྱེད་པ་དག་གིས་མཚན་མ་བརྗོད་ན་སྡོམ་པ་སྐྱེ་བར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 1384]
དགེ་འདུན་གྱི་ན་ཡང་དེའི་སྐྱེ་གནས་ཀྱིས༌[^980]མི་སྐྱེའོ་ཞེས་བྱ་བ་ནི་ཡང་དག་པར་ལེན་པར་བྱེད་པའམ་ལས་བྱེད་པ་དག་ལས་གང་ཡང་རུང་བས་དགེ་འདུན་གྱི་མཚན་མ་བརྗོད་ན་ཡང་དེའི་སྐྱེ་གནས་ཀྱིས་ཞེས་བྱ་བ་དགེ་འདུན་གྱི་སྐྱེ་གནས་དེའི་རིགས་ཀྱི་སྡོམ་པ་ལ་སྐྱེ་བ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1385]
འདིར་གཞུང་ནི་ཡང་དག་པར་ལེན་པར་བྱེད་པའི་ཕྱིར་ནི་གང་ཟག་གསུམ་ནི་བསྙེན་པར་མ་རྫོགས་པ་ཡིན་ཏེ། བདག་ཉིད་ཀྱི་མིང་མི་བརྗོད་པ་དང་། མཁན་པོའི་མིང་མི་བརྗོད་པ་དང་། བསྙེན་པར་རྫོགས་པ་ཡང་མི་ཤེས་པའོ་ཞེས་གསུངས་པའོ། །

[Block 1386]
ལས་བྱེད་པ་པོའི་ཕྱིར་ནི་གཞུང་འདི་ཡིན་ཏེ། མཁན་པོ་དང་བསྙེན་པར་རྫོགས་པར༌[^981]འཚལ་བ་དང་དགེ་འདུན་དང་གསུམ་གྱི་མིང་བརྗོད་པར༌[^982]མི་བགྱིད་ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱིའམ༌[^983]བསྙེན་པར་མ་རྫོགས་ཞེས་བགྱི། བཀའ་སྩལ་པ། བསྙེན་པར་མ་རྫོགས་ཞེས་བྱའོ༌[^984]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1387]
སོ་སོར་ཉེ་བར་གནས་པ་མ་ཡིན་པ་ནི༌[^985]འདི་ཡིན་ཏེ། གང་ཞིག་འདིར་གཟུང་བར་བྱས་པ་ཉིད་ཀྱིས༌[^986]ཡང་དག་པར་ལེན་པ་པོའི་བདག་ཉིད་ཀྱི་མིང་བརྗོད་པའོ། །

[Block 1388]
འདི་ནི་དགེ་འདུན་གྱི་སོ་སོར་ཉེ་བར་གནས་པ་སྟེ། རྗེས་སུ་བཟུང་བ་པོ་མ་ཡིན་པ་ཉིད་ཀྱིས༌[^987]གང་ཞིག་དགེ་འདུན་གྱི་འདི༌[^988]མཚན་ནས་མ་བརྗོད་པའོ། །

[Block 1389]
གང་ཞིག་ལས་བྱེད་པ་པོས་ཡང་དག་པར་བླངས་པ་དེའི་ཡུལ་ཉིད་ཁས་བླངས་པས་དེ་མི་བྱེད་པའོ། །

[Block 1390]
གང་ཞིག་དགེ་འདུན་དང་དགེ་འདུན་དུ་བྱེད་པ་པོའི་ཁས་བླངས་པས༌[^989]དེ་མི་བྱེད་པའོ། །

[Block 1391]
གང་ཞིག་མཁན་པོ་ལ་ལས་བྱེད་པ་པོས་མིང་མ་བརྗོད་པ་དེ་ཡང་དགེ་འདུན་དུ་བྱེད་པ་པོ་ཉིད་ལ་ཁས་བླང་བར༌[^990]བྱ་བ་སྟེ། གང་གི་ཕྱིར་ལས་གང་ལ་དེར་དགེ་འདུན༌[^991]བྱེད་པ་པོ་ཉིད་དུ་རིག་པར་བྱ་སྟེ། དེ་ལས་གཞན་པའི་ལས་དེ་བྱེད་པའོ། །

[Block 1392]
མཁན་པོ་ལ་ཡང་དག་པར་ལེན་པ་པོས་མིང༌[^992]བརྗོད་པ་གང་ཡིན་པ་དེ་ལས་གང་ལ་བྱེད་པ་མཁན་པོ་དང་བཅས་པ་དེ་ལ་དེའི་ཡུལ་ཉིད་ཀྱིས་སོ་སོར་ཉེ་བར་གནས་པའོ། །

[Block 1393]
དེ་བས་ན་འདི་རྣམས་ཀྱི་མཚན་ནས་མ་བརྗོད་པར་སྡོམ་པ་མི་སྐྱེའོ། །

[Block 1394]
ཁྱིམ་པ་དང་མུ་སྟེགས་ཅན་གྱི་རྒྱལ་མཚན་ལ་ཡང་མི་སྐྱེའོ་ཞེས་བྱ་བ་ནི་རྒྱལ་མཚན་ཅན་དང༌[^993]སོ་སོར་ཡོངས་སུ་རྫོགས་པ་སྟེ། ཁྱིམ་པའི་རྒྱལ་མཚན་ཅན་དང་མུ་སྟེགས་ཀྱི་རྒྱལ་མཚན་ཅན་ལ་ཞེས་བྱ་བའོ། །

[Block 1395]
འདིར་ནི་འབྲུ་མང་པོ་ཅན་གྱི་བསྡུ་བའོ། །

[Block 1396]
ཁྱིམ་པའི་རྒྱལ་མཚན་གང་ལ་ཡོད་པ་དང་མུ་སྟེགས་ཀྱི་རྒྱལ་མཚན་གང་ལ་ཡོད་པ་དེར་ནི་ཁྱིམ་པའི་རྒྱལ་མཚན་ཅན་དང་མུ་སྟེགས་ཅན་གྱི་རྒྱལ་མཚན་ཅན་ཞེས་བྱ་བའོ། །

[Block 1397]
རྒྱལ་མཚན་འདི་གང་འཛིན་པ་དག་ལ་སྡོམ་པ་མི་སྐྱེ་སྟེ། འདིར་རྒྱལ་མཚན་ནི་ཆ་བྱད་དོ། །

[Block 1398]
སྒྲེན་མོ་དང༌[^994]འཁྲུགས་པ་དང་མཚན་དུག་མ་ལ་ཡང་མི་སྐྱེའོ་ཞེས་བྱ་བ་ལ༌[^995]སྡོམ་པ་མི་སྐྱེའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 1399]
ཡང་དག་པར་བླངས་པ་ལས་སྒྲེན་མོར་གྱུར་པ་མུ་སྟེགས་ཅན་གྱི་རྒྱལ་མཚན་ཞེས་བྱ་བ་འདི་ཉིད་ཀྱིས་བསྡུས་པའི་ཕྱིར། སྒྲེན་མོའི་ཚིག་ནི་དོན་གཞན་ཅན་རབ་ཏུ་དོར་ནས་སེམས་རབ་ཏུ་བཟུང་བ་ཉིད་གནས་སྐབས་དེ་ལ་དེའི་ཕྱིར་སྡོམ་པ་མི་སྐྱེའོ། །

[Block 1400]
འཁྲུགས་པ་ཉིད་ཀྱིས་དེ་ལ་བརྟན་པ་ཉིད་མེད་པ་དེ་ལ་ཡང་སྡོམ་པ་མི་སྐྱེའོ། །

[Block 1401]
འདིར་མཚན་དུག་མའི་གཞུང་ནི། རེ་ཞིག་མཚན་དུག་མ་ཞིག་བཙུན་པ་རྣམས་ཀྱིས་བསྙེན་པར་རྫོགས་པར་བགྱིད་ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱིའམ་བསྙེན་པར་མ་རྫོགས་ཞེས་བགྱི། བཀའ་སྩལ་པ། བསྙེན་པར༌[^996]རྫོགས་ཞེས་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་རྣམས་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1402]
མཚན་དུག་མ་ནི་སྔར་གང་དང་མཉམ་པར་སྦྱོར་བས་སྐྱེས་པ་འཆི་བའོ། །

[Block 1403]
རྒྱུ་ལས་བཟློག་པའི་ཆད་པ་ཁས་མི་ལེན་པ་གནས་ནས་ཕྱུང་བ་ལ་ཡང་མི་སྐྱེའོ་ཞེས་བྱ་བ་ནི་ལྟ་བ་དང་བཅས་པ་དྲི་བ༌[^997]དང་བྲལ་བ་ཞེས་བྱ་བའི་བསམ་པ་ཅན་ལ་སྡོམ་པ་སྐྱེའོ། །

[Block 1404]
དེ་བས་ན་ལྟུང་བ་མ་མཐོང་བ་ལ་སོགས་པའི་རྒྱུ་གང་གིས་གནས་ནས་དབྱུང་བའི་ལས་བྱས་པ་རྒྱུ་དེ་ལས་བཟློག་པ༌[^998]ལ་སོགས་པ་དེ་ཁས་མི་ལེན་པ་ལ་ཡང་སྡོམ་པ་མི་སྐྱེའོ། །

[Block 1405]
འདིར་གནས་ནས་ཕྱུང་བ་སྨོས་པ་ནི་དཔེ་ཙམ་དུ་ཟད་ཀྱི། སྨད་པ་ཐམས་ཅད་ལ་ཡང་ཆོ་ག་འདི་ཡིན་ཏེ། འཐབ་མོ་བྱེད་པ་ལ་སོགས་པའི་བསམ་པ་ཅན་ལ་ཡང་མི་བཟློག་པའི་བསམ་པ་ཅན་ཉིད་ཀྱི་ཕྱིར་རོ། །
--- END BLOCKS ---
