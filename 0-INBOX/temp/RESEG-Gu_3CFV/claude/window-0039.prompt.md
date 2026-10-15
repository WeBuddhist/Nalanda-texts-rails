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
གལ་ཏེ་བྲུ་བ་ཚ་བར་གྱུར་ན། དེ་ལ་ནང་པར་གྱི་དུས་སུ་ཁ་ཟས་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ལ༌[^849]ཁ་ཟས་ནང་པར་ཁྱེའུ་སུས་ཀྱི་དུས་སུ་སྦྱིན་པར་བྱའོ། །

[Block 1367]
གལ་ཏེ་དྲོ་ཀར་ཡང་ན་དེའི་ཚེ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་དྲོ་ཀར་ཡང་བཀྲེས་པར་གྱུར་ན། དེའི་ཚེ་ཡང་དེ་ལ༌[^850]དྲོ་ཟན་སྦྱིན་པར་བྱའོ། །

[Block 1368]
བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་ཉལ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1369]
བཟློག་པའི་ངོ་བོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེའི་ཐ་མར་ཞེས་བྱ་བའི་མཐར་ཇི་ལྟར་རིགས་པར་བཀའ་བསྒོ་བ་ཉེ་བར་བརྩམས་པའི་བསླབ་པའི་གཞིར་གཏོགས་པ་སྤྱིའི་ཆོ་ག་ལ་ཉེ་བར་གནས་པ་ལ་ལྟོས་ན་གང་ལ་ལྟ་བར་གྱུར་པ་མི་འདོར་བའི་ལྟུང་བྱེད་ཅེས་བྱ་བ་འདིའི་བྱེ་བྲག་བརྗོད་པ༌[^851]ཡིན་ཏེ། དེའི་ཕྱིར་ཇི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་བར་དུ་གཅོད༌[^852]པའི་ཆོས་སུ་གསུངས་པ་གང་ཡིན་པ་དེ་དག་བསྟེན་ཀྱང་བར་དུ་གཅོད་པར་མི་འགྱུར་ཏེ། དེ་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས༌[^853]བསྟན་པ་བདག་གིས་ཤེས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པར་འཇུག་པའི་ཚིག་མི་གཏོང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་ཞིག་གསུངས་པ་འཇུག་པའི་ཚིག་ཉིད་མི༌[^854]གཏོང་བ་ཞེས་བྱ་བའི༌[^855]དོན་ཏོ། །

[Block 1370]
བར་དུ་གཅོད་པའི་ཆོས་རྣམས་ནི་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་སུ་རིག་པར་བྱའོ། །

[Block 1371]
འདིར་སོགས་པའི་སྒྲ༌[^856]ནི་ལྟ་བ་དང་འབྲེལ་པ་གཞན་རྣམས་ལ་ཡང་ཉེ་བར་བསྡུས་པའི་དོན་ཏོ། །

[Block 1372]
ལྟ་བ་དང་འབྲེལ་པ་ཐམས་ཅད་ལ་ཆོ་ག་འདི་འཇུག་པ་སྟེ། དེ་རྣམས་ཐམས་ཅད་ལོག་པའི་ལམ་དུ་རྟོགས་པར་འགྱུར་བ༌[^857]ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1373]
དེ་ལ་གསོལ་བས་སྨད་པ་ཉིད་བྱ་ཞིང་དེའི་འོག་ཏུའོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ༌[^858]ནི་ལས་ཀྱི་མཐའ་མི་གཏོང་བ་ལ་ལྟུང་བྱེད་དེ། འགྱུར་བ་ནི་སྨད་པ་ཉིད་འདི་གསོལ་པའི་ལས་ཀྱི་འོག་ཏུ་བྱའོ། །

[Block 1374]
དེ་ལ་སྨད་པ་ཉིད་དུ་བྱས་པས་མི་གཏོང་བར་འགྱུར་ན་དེའི་འོག་ཏུ་ཕངས་པར༌[^859]བྱེད་པར༌[^860]རིག་པར་བྱའོ། །

[Block 1375]
འདི་ནི་སྐྲོད་པས་སྨད་པ་ཉིད་ལ་རྣམ་པར་གཞག་པ་སྨད་པ་ཉིད་དུ་བྱེད་པ་སྤངས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 1376]
ལྟ་བར་གྱུར་པ་མི་གཏོང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1377]
སྤངས་པའི་རྗེས་སུ་ཕྱོགས་པའི་ལྟུང་བྱེད་ལ་བྱེད་པ་པོ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱའོ། །གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེ་སྐད་སྨྲས་པ༌[^861]སྤངས་པའི་ཕྱིར་བཅོས་པ་ཉིད་མ་བྱས་པའི་དགེ་སློང་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་འདི༌[^862]ལྟར་བདག་ཇི་སྲིད་དུ་བར་དུ་གཅོད་པའི་ཕྱིར་མི་ནུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་འདིར་དེ་ཉིད་སྨྲས་པའོ། །

[Block 1378]
དེ་སྐད་སྨྲ་བ་ཉིད་ཕྱིར་བཅོས་པ་ཉིད་མ་བྱས་པ་ཞེས་བྱ་བ་ནི། རྗེས་སུ་ཕྱིར་བཅོས་པ་ཉིད་མ་བྱས་པ་མི་གཏོང་བ་ཉིད་ཅེས་བྱ་བ་སྟེ། སྤངས་པ་ཉིད་ཀྱིས་བཟོད་པ་གསོལ་བ་ཉིད་མ་བྱས་པའོ་ཞེས་བྱ་བ་རྣམ་པར་འབྱེད་པ་ལས་སོ། །

[Block 1379]
དེ་བཞིན་དུ་ལྟ་བ་མ་བཏང་བའི་ལྟུང་བ་མ་བཤགས་པ་ཡང་ཁ་ན་མ་ཐོ་བ་འདི་འབྱུང་བའི་རྒྱུ་མ་ཡིན་ཏེ། འོན་ཀྱང་བླངས་པ་ཉིད་དོ། །

[Block 1380]
མ་བཏང་བ་དང་མ་བཤགས་པ་འདི་དག་སྨོས་པ་ནི་མ་བླངས་པ་ནི་ཁ་ན་མ་ཐོ་བ་འདི་མི་སྐྱེད་པའོ། །

[Block 1381]
མེད་པ་དག་ལ་བླངས་པ་ཉིད་ལ་སྤང་བར་བྱ་བ་ཉིད་སྐྱེ་བ་འབྱུང་བ་ཡིན་ནོ། །

[Block 1382]
དེ་ལྟར་ཡང་བཏང་བའི་མ་བཤགས་པ་ཉིད་ལ་ཁ་ན་མ་ཐོ་བ་འདི་མི་བསྐྱེད་པ་ཡིན་ནོ། །

[Block 1383]
དེ་ལྟ་བས་ན་འདིར་མ་བཏང་བ་ཉིད་ནི་མ་བྱས་པ་ཉིད་དོ། །

[Block 1384]
ལྟ་བ་བརྟེན་པ་མི་གཏོང་བ་ཉིད་དང་ལྟུང་བྱེད་ལ་ནི་མ་བྱས་པ་ཉིད་དོ། །

[Block 1385]
དགེ་སློང་ལའོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ་རྫོགས་པ་ལ་གང་དུ་ཡིན་ཞེ་ན། འདིར་རབ་ཏུ་བྱུང་བ་ཉིད་རྣམ་པར་གཅད་པའི༌[^863]དོན་དུ་ཁྱིམ་པ་འམ་ཕྱི་རོལ་པའི་རབ་ཏུ་བྱུང་བ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1386]
སྨོན་ལམ་དང་ལས་འདི་དག་ལ་ཡུལ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རྣམ་པར་གཅོད་པ་འདི་ཡང་འདིར་རྣམ་པ་གཞན་ལ་ནི་མི་འདོད་པ་ཉིད་ཀྱི་ཕྱིར་རྣམ་པ་གཞན་རྗེས་སུ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 1387]
ཀུན་དུ་སྤྱོད་པ་གང་ལ་དེ་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ལུང་འབོགས་པ༌[^864]དང་དམིགས་ཀྱིས་དྲི་བ་དང་། གནས་དང་རྗེས་སུ་སྟོན་པ་དང་གདམས་ངག་སྦྱིན་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་སོ་སོར་སྦྱིན་པའི་སྒྲ་ལས་མངོན་པར་སྦྱོར་བར་བྱའོ། །

[Block 1388]
ལྟ་བ་སྨྲ་ནའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་དགེ་སློང་གིས༌[^865]སྤངས་པའི་དྲུང་དུ་ལྟ་བ་སྨྲ་ན་ལོངས་སྤྱོད་ལས་བྱུང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1389]
ཟང་ཟིང་གི་ལོངས་སྤྱོད་བྱེད་ནའོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་དང་ཆོས་གོས་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞི་ཕྱི་མའི་ཚིག་གོ། །

[Block 1390]
འདི་ལ་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་འདུག་པ་ཉིད་དག་ལ་འདིར་ཐོབ་པ་ལ་བསྡུས་པ་འདི་ཡིན་ནོ། །

[Block 1391]
བསྙེན་བསྐུར༌[^866]བདག་གིར་བྱེད་ནའོ། །

[Block 1392]
གནས་སུ་ལྷན་ཅིག་ཉལ་ན་ཡང་ངོ་ཞེས་བྱ་བ་སྟེ། དུས་ནམ་གྱི་ཚེ་ལྷན་ཅིག་ཏུ་ཉལ་ཞེ་ན། དེའི་ཕྱིར་མཐར་རོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1393]
གང་གི་མཐར་ཞེ་ན་དེའི་ཕྱིར་མཚན་མོའི་འོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་སྐབས་འདི་ལ་འདུག་པ་འདིའི་ཡོངས་སུ་རྫོགས་པར་འགྱུར་བ་ཉིད་དོ། །

[Block 1394]
གཞན་གྱིས་སྤྲུལ་ན་ཡང་ཞེས་བྱ་བ་ནི་འདི་ཆོས་རྣམ་པར་གཏན་ལ་དབབ་པ་ལས་རྟོགས་པ་ཡིན་ཏེ། འདི་དང་ལྷན་ཅིག་ཏུ་ཉེ་བར་གནས་པའི་བྱེད་པ་པོ་ཡོ་བྱད་ཉེ་བར་བསྡུ་བའོ། །

[Block 1395]
དེ་དང་འདྲ་བའི་ཆུ་དང་སོ་ཤིང་ལ་སོགས་པ་དེ་དང་ལྷན་ཅིག་ཏུ་འདུ་འཛི་བྱེད་ན་ཕྱིན་ཅི་ལོག་ཏུ་རིག་པར་བྱའོ། །

[Block 1396]
ཕེབས་པར་སྨྲ་བ་དང་སྨོས་འདྲིན་དག་ལ་དེར་གཏོགས་པའི་གཙོ་བོ་ཉིད་དུ་བྱེད་པ་ནི་འདུ་འཛིར་གྱུར་པ་ཉིད་དོ། །

[Block 1397]
གཞན་དག་ལ་ནི་ཉེས་བྱས་སུ་རྟོགས་པར་རིག་པར་བྱའོ། །

[Block 1398]
ཅི་རྣམ་པ་ཐམས་ཅད་དུ་གཞན་གྱིས་སྤྲུལ་པ་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ནད༌[^867]དང་ལྟ་བ་དང་བྲལ་བར་འདོད་པའི་དོན་གྱིས་ནི་མ་གཏོགས་སོ་ཞེས༌[^868]སྨོས་ཏེ། ནད་པར་གཏོགས་པ་དེའི་དོན་དང་ལྟ་བ་དང་བྲལ་བར་གཏོགས་པའི་དོན་གྱིས་སྤྲུལ་པ་གང་ཡིན་པ་དེ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བའི༌[^869]དོན་ཏོ། །

[Block 1399]
ཚུལ་ཁྲིམས་འཆལ་པ་ལ་ཅི་ཞིག་བསྒྲུབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་བླང་བའི་རྣམ་པར་གཞག་པ་ལས་འདའ་བར་བྱ་བ་ཞེས་བྱ་བ་དེ་ལ་ཁ་ན་མ་ཐོ་བ་རྣམ་པར་གཞག་གོ། །

[Block 1400]
དེ་བས་ན་དེ་ལ་ཚུལ་ཁྲིམས་འཆལ་བའི་ཕྱིར་འདིར་འཇུག་པ་ཐོབ་པ་ཡིན་ནོ། །

[Block 1401]
དེ་ལྟར་ཡང་ཤིན་ཏུ་ཚུལ་ཁྲིམས་འཆལ་བ་མཁན་པོ་དང་སློབ་དཔོན་དག་ལ་ཉེ་བར་གནས་པར་བྱ་བ་ཉིད་དུ་གསུངས་སོ། །

[Block 1402]
ཚུལ་ཁྲིམས་འཆལ་བའི་ལྕི་བ་ཉིད་ཡོངས་སུ་སྤོང་བའི་དོན་དུ་སོ་སོར་བསྐོར་བར་བྱའོ། །

[Block 1403]
སྤངས་པའི་རྗེས་སུ་ཕྱོགས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1404]
དེ་དག་ལ་གཞམ་པ༌[^870]དང་ལས་ཀྱིས༌[^871]མི་བསྒོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་འདིས་གང་ཞིག་ལྟ་བ་དང་འབྲེལ་པ་རྣམས་ལ་ཆོ་ག་འདི་བྱ་བ་ཉིད་དུ་བསྟན་པ་དེ་ནི་དགེ་ཚུལ་ཡོད་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་འདི་ལ་གལ་ཏེ་དགེ་སློང་གི་ཁོངས་སུ་སྡུད༌[^872]ན། དེ་ལ་ལས་ཀྱི་མཐའ་ལ་མི་གཏོང་ན་དེའི་ཚེ་ཇི་ལྟར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ལྟོས་ནས་བརྗོད་པར་བྱ་སྟེ། ཚིག་དེ་ཉིད་ལ་ཞུགས་པ་མི་གཏོང་ན། དགེ་ཚུལ་བསྙིལ་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚིག་དེ་ཉིད་ཞུགས་པ་དེ་ལྟར་བདག་གིས༌[^873]ཇི་སྲིད་བར་དུ་གཅོད་པའི་ཕྱིར་ནུས་པ་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གང་ལ་ཡོད་པ་དེ་ནི་ཚིག་དེ་ཉིད་ལ་ཞུགས་པའོ། །

[Block 1405]
དེའི་དངོས་པོ་མི་གཏོང་ན་དགེ་ཚུལ་དེ་བསྙིལ་བར་བྱའོ། །
--- END BLOCKS ---
