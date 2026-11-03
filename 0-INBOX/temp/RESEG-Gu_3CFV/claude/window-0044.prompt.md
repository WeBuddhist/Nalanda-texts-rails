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
[Block 1541]
རང་གི་ལ་མི་གནོད་ན་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དགེ་འདུན་ནམ་མཆོད་རྟེན་གྱི་སྦ་བར་བྱ་བ་ལ་བདག་ཉིད་ཀྱི་དོན་ལ་མི་སྦ་བར་ཁྱེར་བ་དང་མ་ཁྱེར་བར་གནོད་པར་གྱུར་ན་ནི་དེ་ལྟ་བུ་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1542]
རང་གི་ལ་ཞེས་བྱ་བ་ནི་ཆོས་དང་ལྡན་པ་དེའི་འོ། །

[Block 1543]
གང་ཞིག་མེད་པར་ལུས་གནས་པའམ་ཆོས་སྒྲུབ་པ༌[^961]ལ་གནོད་པར་འགྱུར་བ་རྨོངས་པའི་ཡོ་བྱད་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 1544]
དགེ་འདུན་གྱིས་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་དེར་དགེ་སློང་རྣམས་ཀྱིས་དགེ་འདུན་གྱི༌[^962]མི་ཟད་པའི་གཏེར་རྣམས་ཁྱེར་བ་དང་། དེ་དག་གི་ལྷུང་བཟེད་དང་ཆོས་གོས་དང་འཁྱམས་ནས་སྐབས་དེ་དགེ་སློང་དག་གིས་བཅོམ་ལྡན་འདས་ལ་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་ལྟར་མི་བྱ་སྟེ་གང་ཟག་ནི་ཕོངས་པར་འགྱུར་གྱི་དགེ་འདུན་ནི་མི་འགྱུར་བས་དེའི་ཕྱིར་དགེ་སློང་གིས་དང་པོར་རང་གི་ལྷུང་བཟེད་དང་ཆོས་གོས་བསྐུར་བར༌[^963]བྱ་ཞིང་གལ་ཏེ་བསྲུང་བར་ནུས་ན་ཕྱིས་དགེ་འདུན་གྱི་ལ་ཡང་འབད་པར་བྱའོ། །

[Block 1545]
མཆོད་རྟེན་གྱི་ལ་ཡང་ཞེས་བྱ་བ་ནི་དེ་ཡང་གང་དུ་སྦས་ནས་འགྲོ་བ་ཀློག་པ་ལས་དེར་གསུངས་པ་རིང་བ་ཉིད་ཀྱི་ཕྱིར་འདིར་མ་བརྟགས་སོ། །

[Block 1546]
བྱེད་པར་གྱུར་པ་གང་གིས་སྦས་ནས་སམ་ཁྱེར་ཏེ་འགྲོ་ཞེ་ན། དེའི་ཕྱིར་དད་པ་ཅན་གྱིས་ཏེ་འདི་པའི་རབ་ཏུ་བྱུང་བ་མ་ཡིན་པ་ལ་འདི་བཟུང་བ་ཞེས་བྱ་བ་འོག་ནས་ཤེས་པར་བྱའོ། །

[Block 1547]
དགེ་ཚུལ་གྱིས་སོ་ཞེས་བྱ་བ་ནི་སྡོམ་པ་ཉིད་ལ་དད་པས་དེའི་གནས་ལས་མཐའ་ཡས་པར་བྱས་པ་ཉིད་འདིས་ནི་དད་པ་ཅན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 1548]
མེད་ན་རང་གིས་སོ་ཞེས་བྱ་བ་ནི། དེ་གཉིས་གཅིག་ཀྱང་མེད་ན་རང་གིས་སྦས་སམ་ཁྱེར་ཏེ་འགྲོ་བར་བྱའོ། །

[Block 1549]
དེར་བསྐོ་བར་བྱ་བ་ནི། སྦ་བ་དང་བསྐུར་བར་བྱ་སྟེ་འཛིན་པར་སྦྱོར་བའོ། །

[Block 1550]
དེར་བསྐོ་བ་ཡང་འདི་དང་ཤིན་ཏུ་ཞན་པ་ཉིད་ཀྱི་ཕྱིར་འགྲོ་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 1551]
བྲལ་ན་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་འདིར་བྲལ་ན་སྦས་པའམ་ཁྱེར་བ་དེ་ཉིད་དུ་སྦྱིན་པའོ། །

[Block 1552]
བྲུ་བ་ཡང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྦས་ཏེ་ཁྱེར་ནས་འགྲོ་བ་དེ་བཞིན་དུ་དད་པ༌[^964]ཅན་ནམ། དགེ་ཚུལ་གྱིས་བྲུ་བའོ། །

[Block 1553]
ཇི་སྲིད་དུ་དེ་གཉིས་མེད་ན་རང་གིས་སོ། །

[Block 1554]
མི་མ་ཡིན་པའི་གནས་ན་གནས་ཏེ་དེ་དག་གི་བསོད་ནམས་ཀྱིས་བྱུང་བ་རིན་པོ་ཆེའི་རང་བཞིན་གྱི༌[^965]ས་གཞི་དང་ཐེམ་སྐས་ལ་སོགས་པ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་དེ་དང་འདྲ་བའི་འཇིག་རྟེན་སྒྲུབ་པར་བྱེད་པའི་བསོད་ནམས་ནི་འདིར་རིག་པར་བྱ་སྟེ་གཞན་རྣམས་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1555]
ཟན་གྱི་ཕྱིར་སྣོད་གཞན་མེད་ན་རིན་པོ་ཆེ་ལ་སོགས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་ཕྲན་ཚེགས་དག་ལས་སྐྱོན་མེད་པའི་རིན་པོ་ཆེའི་རང་བཞིན་ལས་བྱས་པའོ། །

[Block 1556]
ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་ནི་མི་མ་ཡིན་པའི་གནས་ན་གལ་ཏེ་དེ༌[^966]དག་གི་བསོད་ནམས་ཀྱིས་བྱུང་བའི་དེ་རྣམས་ཀྱི། རིན་པོ་ཆེའི་རང་བཞིན་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བའི་རྗེས་བསྙེག་པའི་ཕྱིར་རོ། །

[Block 1557]
འདུག་པའི་ཕྱིར་གནས་མལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་ནི་སྐྱོན་མེད་པའི་ཞེས་བྱ་བ་ལ༌[^967]སོགས་པ་འདི་མེད་པ་ལ་གཞན་མེད༌[^968]ན་ཞེས་བྱ་བ་ལ་སོགས་པའི་རྗེས་བསྙེག་པའི་ཕྱིར་རོ། །

[Block 1558]
འདིར་གཞུང་ནི་ཀོ་ལྤགས་ཀྱི་གཞི་ལས།

[Block 1559]
དགེ་སློང་དག་ལྷ་དང་ཀླུའི་གནས་དག་ཏུ་འགྲོ་བ་ན་དེར་རིན་པོ་ཆེའི་རང་བཞིན་གྱི༌[^969]གདན་རྣམས་རྙེད་པར་གྱུར་ཏེ། དེ་རྣམས་ལ་འདུག་པར་མི་བྱེད་ཅིང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་དག་ནི་སེམས་ཅན་དེ་རྣམས་ཀྱི༌[^970]བསོད་ནམས་ལས་བྱུང་བ་ཡིན་པས་དེ་རྣམས་ལ་འདུག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1560]
གལ་ཏེ་ཡང་གཞན་ལ་མེད་པ་ཞེས་བྱ་བ་འདིར་མི་འདོད་ན་དེ་ལྟར་ཡང་འདི་ནི་རིགས་པར༌[^971]གྱུར་པ་སྟེ། དེ་བས་ན་བརྟེན་པའོ། །

[Block 1561]
བཞོན་པས༌[^972]འགྲོ་བར་བྱའོ། །

[Block 1562]
ཆོས་དང་ལྡན་པའི་ཆོས་ཉིད་ཀྱི་དབང་ཉིད་ཀྱིས་སོ། །

[Block 1563]
དེ་ལ་ཡང་ཆ་སྒེག་པ་དང་ལྡན་པ་ཉིད་ཀྱིས་མི་བྱའོ། །

[Block 1564]
རྒས་པ་དང་ན་བ་དག་ལས་གཞན་པས་མི་བྱ་བ་ནི་ཀོ་ལྤགས་ཀྱི་ཕྲན་ཚེགས་རྣམས་ལས་འདི་སྐད་ཅེས་གསུངས་ཏེ། ཆོས་ཉན་དུ་གཞུག་པའི་ཕྱིར་རིན་པོ་ཆེ་ལས་བྱས་པའི་སེང་གེའི་ཁྲི་ལ་མི༌[^973]རྟག་པས་ཉེན་པར་གྱུར་པའི་ཡིད་ལ་བྱེད་པས་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ཆོས་བསྒྲག་པའི་དོན་དུ་ཞེས་བྱ་བ་ནི་འདིར༌[^974]འདུག་ཅིང་ཉན་པ་པོ་རྣམས་ལ་ཆོས་བསྒྲགས་པར༌[^975]བྱའོ་ཞེས་བྱ་བའི་དོན་ལ་བརྟེན་ནས་གནས་མལ་གྱི་བསླབ་པའི་གཞི་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1565]
དེ་ལ་སོགས་པའི་རྫས་ཀྱང་ཞེས་བྱ་བའི་མཐའ་ཅན་འདིར་དྲངས༌[^976]པའོ། །

[Block 1566]
འདིར་གཞུང་ནི་དེ་ནས་ཁྱིམ་བདག་མགོན་མེད་ཟས་སྦྱིན་གྱིས་ཐོས་ནས་རིན་པོ་ཆེ་སྣ་བཞི་ལས་བྱས་པའི་སེང་གེའི་ཁྲི་བཤམས་པ་དང་དགེ་སློང་དེ་དག་དེ་ལ་མི་འཁོད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། འདུ་བྱེད་ཐམས་ཅད་མི་རྟག་གོ་སྙམ་དུ༌[^977]བསམས་ནས་དེ་ལ་འདུག་ནས་ཆོས་བཤད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1567]
ཁྱིམ་དུ་དེ་བཤམས་པ་དང་གསེར་དང་དངུལ་གྱིས་སྤྲས་པ་དྲིལ་བུ་གཡེར་ཁ་གཤིབས་པའི༌[^978]གོས་དག་ལ་ཁྱིམ་པའི་ཡིན་ནོ་སྙམ་དུ་ཤེས་པར་བྱས་ནས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲ་ནི་མི་རྟག་པས་ཉེན་པར་གྱུར་པ༌[^979]ཡིད་ལ་བྱེད་པས་འདུག་པར་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སྙེག་པའི་ཕྱིར་རོ་སྙམ་དུ་ཤེས་པར་བྱས་ནས་ཞེས་བྱ་བ་ནི་ཁྱིམ་པའི་ཡིན་ནོ་སྙམ་དུ་ཤེས་པར་བྱས་ནས་སོ། །

[Block 1568]
འདིར་གཞུང་ནི་བྲམ་ཟེ་དང་ཁྱིམ་བདག་དད་པ་ཅན་རྣམས་ཀྱིས་ཁྱིམ་གྱི་ནང་དུ་གསེར་གྱིས་སྤྲས་པ་གསེར་གྱི་དྲིལ་བུ་གཡེར་ཁས་གཤིབས་པའི་གོས་དག་བཤམས་པ་དང་། དགེ་སློང་དག་དེ་ལ་མི་འཁོད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། འདུ་བྱེད་ཐམས་ཅད་མི་རྟག་གོ་སྙམ་དུ་བསམས་ཏེ། སྦྱིན་པ་པོ་རྣམས་ཀྱིས་སྦྱིན་པར་བྱ་བའི་ཆོས་རྣམས་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པར༌[^980]བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1569]
དེ་ལ་ནོར་བུས་སྤྲས་པ་གསེར་དང་དངུལ་གྱིས་བརྒྱན་པ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་སེང་གེའི་ཁྲི་དེ་ལའོ། །

[Block 1570]
དེ་ལྟ་བུའི་གོས་དག་ལ་འདུག་པ་འདི་ནི་དེའུ་རེ་མི་རྟག་པས་ཉེན་པར་གྱུར་པ་ཡིན་ནོ་སྙམ་པའི་ཡིད་ལ་བྱེད་པས་འདུག་པར་བྱའོ། །

[Block 1571]
འདི་ལྟར་སེང་གེའི་ཁྲིའི་ཆོ་ག་ལ་གྲུབ་པ་མེད་དེ་དངོས་སུ་ཡང་བྱེ་བྲག་འདི་ལ་ཁྱད་པར་གྱི་གཞུང་ཡོད་པ་མ་ཡིན་ཏེ། འདི་བསྟན་པའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 1572]
དེ་དག་གྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སེང་གེའི་ཁྲི་ལ་གོས་རྣམ་པ་དེ་ལྟ་བུ་བཤམས་པ་དེ༌[^981]དག་གོ། །

[Block 1573]
ཁྱིམ་པ་དང་དགེ་ཚུལ༌[^982]མེད་ན་སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་ལ་སྟོན་པའི་འདུ་ཤེས་ཉེ་བར་གཞག་པ་རྣམས་ཀྱིས་ཆོས་དང་ལྡན་པའི་དོན་གྱི་དབང་ཉིད་ཀྱིས་རེག་པ་ལ་མི་རུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདིར་རིན་པོ་ཆེ་ཡང་སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་བརྗོད་པར་འདོད་པའོ། །

[Block 1574]
དེའི་རྫས་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་དེའི་རྫས་དང་རྒྱན་ལ་སོགས་པ་ལ་ཡང་ངོ་། །རྒྱན་གདགས་པ་བརྟེན་པར༌[^983]མི་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་དེ་ལྟ་བས་ན་དགེ་སློང་གིས་རྒྱན་དང་རྐང་རྒྱན་གདགས་པར་མི་བྱའོ། །

[Block 1575]
འདོགས་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ། །

[Block 1576]
དེ་བཞིན་དུ་ཚོན་སྣ༌[^984]ལྔའི་སྔགས་སྐུད་གདགས་པར་མི་བྱའོ། །

[Block 1577]
འདོགས་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་བྱ་བའི་བར་དུ༌[^985]གསུངས་པ་ཡིན་ནོ། །

[Block 1578]
རྒྱན་འདོགས་པ་འདི་ལ་རྒྱན་དེ༌[^986]ཐམས་ཅད་ནི༌[^987]དཔེ་ཙམ་ཡིན་གྱི་འདི་ཐམས་ཅད་བཅང་བར་བྱ༌[^988]བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་སྟོན་པར་བྱེད་པའོ། །

[Block 1579]
འདི་ནི་རང་བཞིན་གྱི་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་མ་ཡིན་ཏེ། དེ་བས་ན་དེ་བསྲུང་བའི་དོན་དུ་སྲུང༌[^989]སྐུད་འདི༌[^990]ཚོན་ལྔའི་རང་བཞིན་ཅན་ནི་མི་བྱ་བར༌[^991]ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1580]
ཕྲན་ཚེགས་དག་ལས་དེ་ལ་སོགས་པ་འདིར་རུང་བ་ཞེས་བྱ་བའི་ཕྱིར་མཐར༌[^992]འདི་དྲངས༌[^993]པའོ། །
--- END BLOCKS ---
