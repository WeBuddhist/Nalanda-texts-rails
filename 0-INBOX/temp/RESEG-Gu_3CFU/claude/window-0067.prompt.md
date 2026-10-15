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
[Block 2346]
མཚམས་གཞན་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཉེས་པ་མེད་པ་ཉིད་དོ། །

[Block 2347]
ཤོ་གམ་དྲལ་བ་ན་ཡང་ཞེས་བྱ་བ་དང་རྗེས་སུ་སྦྱར་རོ། །

[Block 2348]
མཚམས་གཞན་དུ་ཞེས་བྱ་བ༌[^1619]ཤོ་གམ་གྱི་བྱ་བ་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བ་ཡོད་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2349]
ཤོ་གམ་གྱི་གནས་ནས་ཐོབ་པའི་སྤོང་བའི་བདག་ཉིད་ཅན་དྲལ་བའི༌[^1620]བསམ་པ་མེད་པ་ལ་རྐུ་བའི་སེམས་ཞེས་བྱ་བ་འདི་ལ་འདི་བརྗོད་པའོ། །

[Block 2350]
བསྒོ་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཤོ་གམ་དྲལ་ན་ཞེས་བྱ་བར་སྦྱར་ཏེ། ས་གང་ཞིག་ལ་ཤོ་གམ་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་དེས་མི་འགྲོ་བ་ལ་ཐད་ཀར་དེ་ལས་འདའ་བར་བྱེད་པའམ་སོ་སོར་བཟློག་པ་ལ་ས་མ་ཐོབ་པ་ཉིད་ལ་གཞན་གྱིས་འགྲོ་བའམ་བཟློག་པ་ཞེས་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 2351]
ལམ་གཞན་སྟོན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ཤོ་གམ་དྲལ་བའི་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཤོ་གམ་གྱི་ས་ལ་འགྲོ་བའི་ལམ་གཞན་ནས་འགྲོ་བའམ་ཕྱིར་བཟློག་པར་བྱ་བའམ་ཐད་ཀར་འགྲོ་བ་ལས་ས་མ་ཐོབ་པ་ཉིད་ལ་ཤོ་གམ་གྱི་ས་ལ་འགྲོ་བ་ལས༌[^1621]ལམ་གཞན་ནས་འགྲོ་བ་འམ་ཕྱིར་བཟློག་པ་ལ་ཞེས་བྱ་བ་འདི་འདིར་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 2352]
ཐབས་ཀྱིས་བརྗོད་ན་ཕྲ་མོར་རོ་ཞེས་བྱ་བ༌[^1622]བསྒོ་བ་དང་ལམ་གཞན་སྟོན་པ་དེ་གཉིས་ཀའི༌[^1623]དངོས་སུ་མི་བྱེད་པར་ཐབས་ཀྱིས་བརྗོད་པ་ཡིན་པ་དེ་ནི་ཟུར་གྱིས་སྨྲ་བ་སྟེ། དངོས་སུ་བརྗོད་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལྟ་བུར་གྱུར་པ་ཕྲ་མོ་སྟེ། ཤིན་ཏུ་ཡང་བའི་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2353]
ལམ་གོལ་བ་ནི་ལམ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་དུ་ལམ་མ༌[^1624]ཡིན་པས་བརྐུས་པ་ལ་ཤོ་གམ་གྱི་སར་འགྲོ་བའི་ལམ་ཡིན་པས་འདའ་བར་བྱེད་པ་ལ་སྐྱོན་དང་བྲལ་བ་ཉིད་དང་འགྲིབ་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2354]
ཁ་དང་ཚེམ་བུ་ནི་སྐུངས་གཞན་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྒྲོ་བ་དག་ལ་སོགས་པའི་སྐུངས་གཞན་གྱིས༌[^1625]རྐུ་བའམ་འདའ་བར་བྱེད་ན་ཉེས་པར་འགྱུར་བ་དེ་བཞིན་དུ་ཁ་དང་ཚེམ་བུའི་ནང་དང་བར་དུ་བཅུག་སྟེ་རྐུ་འམ་འདའ་བར་བྱེད་ན་ཡང་ཉེས་པར་འགྱུར་རོ། །

[Block 2355]
ལུས་ཀྱི་ཁོངས་སུ་གཏོགས་པ་ཉིད་ཀྱི༌[^1626]ཕྱིར་འདི་ནི་ལུས་སུ་གྱུར་པ་སྟེ། གོས་ཀྱི་ཁོངས་སུ་གཏོགས་པ་ཉིད་ཀྱི་ཕྱིར་གོས་ཡིན་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2356]
དེ་བས་ན་ཉེས་པ་མེད་པ་ཉིད་དང་འགྲིབ་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2357]
འདིར་གཞུང་ནི་ཁས་རྐུ་ན་མཐའི་ལྟུང་བར་འགྱུར་རོ། །

[Block 2358]
ཚེམ་བུས་རྐུ་ན་མཐའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2359]
རྐུ་སེམས་དང་བྲལ་ན་མཐའི་མཐར་ཐུག་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་རྐུ་སེམས་ཀྱི་སྦྱོར་བ་དང་དེ་མེད་པར་བརྣོགས་པ་ལ་སྦྱོར་བའི་ལྟུང་བ་ཙམ་ལ་དེ་བསྐྱེད་པའོ། །

[Block 2360]
དངོས་གཞིའི་ལྟུང་བ་ཙམ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་འདི་ནི་བྱེད་པའོ། །

[Block 2361]
ཡོངས་སུ་རྫོགས་པའི་དུས་སུ་རྐུ་སེམས་ཉིད་བསལ་བ་ལ་མཐར་ཐུག་པ་དང་དངོས་གཞི་ལ་རྗེས་སུ་འགྲུབ་པ་ཉིད་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2362]
སྦྱོར་བ་ལ་དེ་མེད་ན་དེ་མ་བྱས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། སྦྱོར་བ་ལ་ཞེས་བྱ་བ་ནི་སྦྱོར་བའི་གནས་སྐབས་ལའོ། །

[Block 2363]
དེ་མེད་ན་ཞེས་བྱ་བ་ནི་རྐུ་སེམས་དེ་མེད་ལ་རྫས་བཟུང་བའི་དུས་སུ་འདི་ཡོད་པས་ཐ་མ་དང་དངོས་གཞི་ལ་བྱས་པ་ཉིད་ཁོ་ནའོ། །

[Block 2364]
གང་དུ་རྐུ་སེམས་མེད་པར་སྦྱོར་བ་མཐར་ཐུག་པ་ནི་རྐུ་སེམས་ཀྱི་སྦྱོར་བའི་ལྟུང་བ་ཉིད་ལ་དེར་སྒྲུབ་པ་ཡིན་གྱི་དངོས་གཞིའི་ལྟུང་བ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་འདི་བརྗོད་པའོ།[^1627] །འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་ཆོས་གོས་ཀྱི་གདང་ལས་ཆོས་གོས་ལེན་པའི་སྔ་རོལ་དུ་རྐུ་སེམས་བྱུང༌[^1628]ལ་ཕྱིས་ནི་རང་གི་འདུ་ཤེས་ཀྱིས་བླངས་ན་ལྟུང་བ་ཅིར་འགྱུར། སྔར་ནི་ཉེས་པ་སྦོམ་པོར་རོ། །

[Block 2365]
ཕྱིས་ནི་ལྟུང་བ་མེད་དོ། །

[Block 2366]
སྔར་རང་གི་འདུ་ཤེས་ཀྱིས་ལེན་ལ་ཕྱིས་རྐུ་སེམས་ཀྱིས་རྐུ་ན་ལྟུང་བ་ཅིར་འགྱུར། སྔར་ནི་ལྟུང་བ་མེད་དོ། །

[Block 2367]
ཕྱིས་ནི་ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2368]
རང་གི་འདུ་ཤེས་ཡོད་པ་ལ་རྐུ་སེམས་ཉེ་བར་གཞག་པའི་དབང་དུ་མཛད་ནས་འདིར་ཉེས་པ་སྦོམ་པོར་རོ་ཞེས༌[^1629]གསུངས་སོ་ཞེས་རྣམ་པར་གནས་སོ། །

[Block 2369]
སྤྲིང་ཡིག་ལ་སོགས་པས་ནི་ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདོད་པ་ཞེས་བྱ་བ་ངེས་པའི་ཚིག་ལས་ལག་ཡིག་དང་རྒྱའི་ཡི་གེ་རྣམས་ཀྱིས་འགྲིམ་པ༌[^1630]ཐོབ་པ་ལ་འདི་ནི་རྩོམ་པའོ། །

[Block 2370]
འདིར་གཞུང་ནི་སྤྲིང་ཡིག་དང་ལག་ཡིག་རྣམས་སམ། ལག་རྩིས་ཀྱིས་རྐུ་ན་རིན་ཐང་བརྩི་བར་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ཏེ། རྣམ་པ་གང་ཡང་རུང་བས་རྐུ་ན་ཡང་ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2371]
རྗེས་སུ་བསྒྲུབ་པའི་སྐབས་སྨྲས་ནས། ད་ནི་མཐར་ཐུག་པའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། ནན་ཁུགས༌[^1631]དང་དངན་འཐེན་ཡང་མ་བརྐུས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། ནན་ཁུགས༌[^1632]ཀྱིས་རྐུ་བ་གང་ཡིན་པ་སྦྱིན་པར་བྱ་བ་ལ་གཅིག་པ་ན་ཡང་གང་ཡིན་པ་འདི་ནི་རྐུ་བ་མ་ཡིན་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 2372]
འདི་ལ་ཡང་ཁྱད་པར་མེད་པར་བརྗོད་པ་རྣམས་ལ་ཆོམ་རྐུན་པས་རྐུ་བ་བཞིན་དུ་ཁོངས་སུ་བསྡུ་བར་རིག་པར་བྱའོ། །

[Block 2373]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་བཙུན་པ་རྐུ་བ་རྣམ་པ་དུ་མཆིས། ཉེ་བ་འཁོར་དྲུག་སྟེ། ནན་ཁུགས༌[^1633]ཀྱིས་རྐུ་བ་དང་། སྒྱུ་ཐབས་ཀྱིས་རྐུ་བ་དང་། གཏམས་པ་རྐུ་བ་དང་། ཕྱིར་བསབ་པ༌[^1634]རྐུ་བ་དང་། དངན་འཐེན་གྱིས༌[^1635]རྐུ་བ་དང་། ཆོས་རྐུ་བའོ། །

[Block 2374]
བཙུན་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གང་རྐུ་བ་དྲུག་པོ་འདི་རྣམས་གསུངས་ན་འདི་རྣམས་ཀྱི༌[^1636]ནང་ནས་དུ་ཞིག་མཐའི་ལྟུང་བར་འགྱུར། ཉེ་བ་འཁོར་ཆོས་རྐུ་བ་མ་གཏོགས་པ་གཞན་ཐམས་ཅད་ཀྱིས་མཐའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2375]
དེ་ལ་ཆོས་རྐུ་བ་ནི་ཉེས་པ་མེད་དེ། རྐུ་སེམས་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་དོན་གོ་བར་ཟད་དོ། །

[Block 2376]
སྒྱུ་ཐབས་ཀྱིས་རྐུ་བ་ནི་རྣམ་པ་གཉིས་ཏེ། ཆོམ་རྐུན་གྱིས་ལེན་པ་དང་། དོར་བྱེད་པའོ། །

[Block 2377]
དེ་ལ་ཆོམ་རྐུན་གྱིས་ལེན་པ་ནི་རྐུ་བ་ཉིད་ཡིན་པས་དོགས་པར་བྱ་བ་མེད་དོ། །

[Block 2378]
དོར་བྱེད་པ་ལ་ནི་སྦྱོར་བ་དོར་བྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་བརྐུས་པ་ཉིད་དུ་གྲགས་པའོ། །

[Block 2379]
གཏམས་པ༌[^1637]རྐུ་བ་ལ་ནི་གཏམས་པ༌[^1638]ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2380]
ཕྱིར་བསབ་པ་རྐུ་བ་ལ་ནི་སྔར་བརྙས་པ་དང་བསྐྱིས་པ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 2381]
ནན་ཁུགས༌[^1639]ཀྱིས་རྐུ་བ་ལ་ནི་དབང་གིས་མནན་ཞིང༌[^1640]ལེན་པ་སྟེ། དེའི་ཕྱིར་དེ་བརྐུས་པ༌[^1641]མ་ཡིན་ནོ་སྙམ་དུ་དོགས་པ་འགའ་ཡང་ཡོད་ལ། གང་ཞིག་དང་ན་འཐེན་གྱིས་རྐུ་བ་ཡང་དེ་ནི་མི་སྟེར་བ་ཙམ་དུ་ཟད་ཀྱིས་བརྐུས་པ་ནི་མ་ཡིན་ནོ་སྙམ་དུ༌[^1642]དོགས་པ་ཡོད་པས་དེ་བས་ན་བརྐུས་པ་ཉིད་དུ༌[^1643]བཏགས་པ་མ་ཡིན་ནོ། །

[Block 2382]
དོགས་པ་དེ་གཉིས་བསལ་བའི་ཕྱིར་མདོ་འདི་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 2383]
གནས་དང་བཅས་པ་དང༌[^1644]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྫས་གང་གནས་དང་ལྷན་ཅིག་ཏུ་བརྐུས་པ་དེ་ཡང་མ་བརྐུས་པ་མ་ཡིན་ཏེ༌[^1645]བརྐུས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2384]
རྫས་ཀྱི་གནས་ལས་མི་སེལ་བ་ཉིད་དུ་གང་དུ༌[^1646]གནས་ལ་སེལ་བར་བྱེད་པ་དེ་ནི་འདིར་གནས་དང་བཅས་པ་ལ་རྐུ་བར་རིག་པར་བྱའོ། །

[Block 2385]
འདིར་སྦྱོར་བ་དང་བྲལ་བ་ཉིད་ནི་དེ་གཉིས་ནི་དེ༌[^1647]ཉིད་དེ་གནས་དང༌[^1648]བཅས་པར་ཡང་བརྐུས་པ་ཉིད་ལ་བདག་པོ་ལ་རྫས་དང་སྦྱོར་བ་དྲལ་བ༌[^1649]ཉིད་ཀྱི་ཕྱིར་རོ། །
--- END BLOCKS ---
