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
[Block 176]
དབང་པོའི་བློ་རྣམས་ནི་རང་གི་དོན་ཙམ་འཛིན་པར་བྱེད་པ་ཡིན་པའི༌[^123]ཕྱིར། །ཁྱད་པར་རྣམས་དང་ལྷན་ཅིག་ཏུ་སྦྱོར་བ་ནི་མི་འཐད་དོ། །

[Block 177]
འདི་ནི་འདིའི་སྤྱི་ཡིན་ཞིང་རྫས་ལ་སོགས་པ་རྣམས་དང་འབྲེལ་པའོ་ཞེས་དང་གི་དོན་གཉིས་ངེས་པར་བཟུང་ནས་དེ་བཞིན་དུ་བརྟག་པར་བྱའོ། །

[Block 178]
དེ་ཡང་དྲན་པ་ལ་སོགས་པ༌[^124]ཡིན་པའི་ཕྱིར་འདི་ལ་ཡིད་ཀྱི་བློས་ཁྱད་པར་དུ་བྱས་ལ༌[^125]འཐད་པ་ཁོ་ན་སྟེ། གཞན་དུ་ན་དྲི༌[^126]མངར་རོ་ཞེས་འཛིན་པ་ཡང་མངོན་སུམ་དུ་འགྱུར་ལ། དེ་ལྟར་འགྱུར་བར་ཡང་མི་རིགས་ཏེ། ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར་དུ༌[^127]བྱ་བ་དག་དབང་པོ་ཐ་དད་ཀྱི་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 179]
གལ་ཏེ་ཡང་རྫས་གཅིག་པས༌[^128]དབང་པོ་དུ་མའི་གཟུང་བྱ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟ་ན་ནི་གཅིག་མིན་ཏེ་གཟུགས་ལ་སོགས་པ་བཞིན་དུ་དུ་མར་འགྱུར་རོ། །

[Block 180]
གཟུགས་ལ་སོགས་པ་ལ་ནི་དབང་པོ་དུ་མས་གཟུང་བར་བྱ་བའི་གཅིག་ཉིད་གང་དུ༌[^129]མཐོང་ངོ་། །གཅིག་མིན་གཟུགས་སོགས་ཀྱང་གཅིག་འགྱུར། །གལ་ཏེ་དབང་པོ་དུ་མའི་གཟུང་བྱ་ཡིན་ཀྱང་ཐ་མི་དད་པར་འདོད་ན་ནི་གཟུགས་ལ་སོགས་པ་ཡང་རྫས་བཞིན་གཅིག་ཉིད་དུ་འགྱུར་རོ། །

[Block 181]
མཐོང་ཞེ་ན། དེ་དག་གལ་ཏེ་འདི་ལྟར་དབང་པོ་ཐ་དད་ཀྱང་ཡུལ་རྫས་ལ་ཤེས་པ་ཐ་མི་དད་པ་ནི༌[^130]མཐོང་བ་ཁོ་ན་སྟེ། ཡོད་པ་ཉིད་དང་ཡོན་ཏན་ཉིད་དག་ལྟ་བུའོ། །

[Block 182]
དེ་བས༌[^131]གཟུགས་ལ་སོགས་པ་ལ་གཅིག་ཉིད་དང་དུ་མ་ཉིད་དུ་ཐལ་བར་མི་འགྲུབ་བོ་ཞེ་ན། ཤེས་པ་ཐ་མི་དད་པ་འདི་ལྟ་བུ་ནི་མཐོང་ན། འོན་ཀྱང་དེ་དབང་པོ་ལས་མིན། དེ་དབང་པོའི་སྒོ་ནས་དབང་པོ་གཞན་གྱི་ཡུལ་ཤེས་པ་ནི་མ་ཡིན་ནོ། །གང་གི་ཕྱིར་ཞེ་ན། དབང་གཞན་དོན་མེད་འགྱུར་ཕྱིར་རོ། །

[Block 183]
གལ་ཏེ་དབང་པོ་གཞན་གྱི་ཡུལ་ལ་ཡང་དབང་པོ་གཞན་གྱིས་འཛིན་ནུས་པར་འདོད་ན་ནི་གཟུགས་ལ་སོགས་པ་ལ་དབང་པོ་དུ་མ་བརྟགས་པ༌[^132]དོན་མེད་པར་འགྱུར་རོ། །

[Block 184]
གལ་ཏེ་འདི་ལྟར་གཟུགས་ལ་སོགས་པ་ཐ་དད་དུ་ཡོད་པའི་ཕྱིར་དབང་པོ་གཅིག་གིས་འཛིན་པར་མི་ནུས་སོ་ཞེ་ན། དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ།[^133] །

[Block 185]
ཅིའི་ཕྱིར་ཞེ་ན། དབང་པོས་ནི་རང་ཡུལ་ཐ་དད་ཀྱང་འཛིན་ནུས། རང་གི་ཡུལ་ལ་ནི་སྔོན་པོ་ལ་སོགས་པའི་ཐ་དད་པ་དང་། །གྲངས་ལ་སོགས་པའི་ཐ་དད་པ་ལ་ཡང་འཛིན་པར་ནུས་པ༌[^134]ལ་ཁྱོད་ཀྱིས་ནི་ཐ་དད་ཀྱང༌[^135]དབང་པོས་འཛིན་ནུས་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 186]
གལ་ཏེ་གྲངས་ལ་སོགས་པའི་ཐ་དད་ལ༌[^136]འཛིན་པ་ནི་དབང་པོ་གཞན་གྱི་ཡུལ་ལ་འཛིན་པ་མ་ཡིན་ནོ། །

[Block 187]
དབང་པོ་གཞན་གྱི་ཡུལ་ཉིད་ནི་གཟུགས་ལས་ཐ་དད་པའི་རེག་བྱ་ལྟ་བུ་སྟེ། དེ་མིག་གིས་གང་ཙུག་བཟུང་།[^137] གང་དག་གལ་ཏེ་རེག་པའི་རྫས་མིག་གིས་འཛིན་ན་ནི་དབང་པོ་གཞན་གྱིས༌[^138]ཡུལ་ཡང་མིག་གིས༌[^139]རང་གི་ཡུལ་ཡིན་ནོ། །

[Block 188]
གསལ་བར་ཁས་བླངས་པའི་ཕྱིར་ཐ་དད་ཀྱང་སྔོན་པོ་ལ་སོགས་པ་བཞིན་དུ་རེག་པ་ལ་སོགས་པ་ཡང༌[^140]མིག་གིས་འཛིན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དང་། ཐ་དད་པ་ཉིད་ནི་དབང་པོ་དུ་མས་གཟུང་བར་བྱ་བའི་རྒྱུ་མཚན་ཡིན། [^141]ཅིས་ན་དབང་པོ་གཞན་གྱི་ཡུལ་མི་འཛིན། གང་ཡང་དོན་ཐ་མི་དད་པ་ལ་ཡང་དབང་པོ་དུ་མས་འཛིན་པར་འགྱུར། གཟུགས་ལ་སོགས་པ་སོ་སོ་ལ་ཡང་། དབང་པོ་ཀུན་གྱིས་འཛིན་པར་འགྱུར། དེ་རྫས་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 189]
དེ་ལྟར་ན་ཡང༌[^142]གཟུགས་ལ་སོགས་པ་ཡང་དབང་པོ་གཅིག་གི༌[^143]གཟུང་བྱ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 190]
ཉེས་པ་དེ་དག་ནི་ཡོད་པ་མ་ཡིན་ཏེ། གཟུགས་ལ་སོགས་པ་དེ་དག་ལ་རང་རང་གི་བྱེ་བྲག་ངེས་པ་ཡོད་པ་ཡིན་ལ། དེ་མེད་པའི་ཕྱིར་དབང་པོའི་བློ་སྔོན་པོ་ལ་མི་འཁྲུལ་ལོ་ཞེ་ན། ཅི་ཡང་དེ་དག་གི་ངེས་པ་ཉིད་དེ་ཅི་ལྟ་བུ་ཞིག །གང་ལ་གཟུགས་ཉིད་མེད་པ་དེ་མིག་གིས་གཟུང་བར་བྱ་བ་ཡིན་ལ་དེ་བཞིན་དུ་རེག་བྱ་ལ་སོགས་པ་རྣམས་ཀྱི་རང་རང་གི་ཡུལ་ལ་ངེས་པ་ཉིད་ཡིན་ནམ། དེ་ལྟ་ན་ནི་མིག་གི་རེག་བྱ་ཚོགས་པ༌[^144]ལའང་འཇུག །རྫས་སོགས་ལ་མིན། རྫས་དང་གྲངས་ལ་སོགས་པ་དང་ལས་རྣམས་ལ་གཟུགས་ཉིད་དང་རེག་བྱ་ཉིད་མེད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 191]
མིག་དང་རེག་པ་དག་གིས་དེ་དག་འཛིན་པར་མི་འགྱུར་རོ། །

[Block 192]
གལ་ཏེ་དེ་ལྟ་ན་ནི་གང་ལ་གཟུགས་ཉིད་ཡོད་པ་དེ་མིག་གི་གཟུང་བྱ་ཡིན་ནོ། །

[Block 193]
དེ་ལྟ་བས་ན་རེག་བྱ་ལ་སོགས་པ་ཡང་དེ་བཞིན་དུ་ངེས་པ་ཉིད་ཀྱིས༌[^145]ཁྱད་པར་ཡོད་པ་ཡིན་ནོ། །

[Block 194]
དེ་བཞིན་དུ་གཟུགས་ལ་སོགས་པ༌[^146]མེད་པའི་ཕྱིར་རོ། །

[Block 195]
རྫས་ལ་སོགས་པ་ལ་ངེས་པ་མེད་པར་འགྱུར་རོ་ཞེ་ན། དེ་ལྟ་ན་ནི་མདོ་དང་ཡང་འགལ་ཏེ། དེ་མེད་པའི་ཕྱིར་མི་འཁྲུལ་ལོ་ཞེས་གཟུགས་ཉིད་ལ་སོགས་པ་ནི་སྒྲ་ལ་སོགས་པ༌[^147]ལ་མེད་པས་མི་འཁྲུལ་བར་བརྗོད་ཀྱི། གཟུགས༌[^148]ལ་སོགས་པ༌[^149]ཡོད་པའི་སྒོ་ནས་ནི་མ་ཡིན་ནོ། །

[Block 196]
དེ་དག་ནི་རིགས་པ་དང་ཡང་མི་འཚམ་སྟེ། དབང་པོ་གཞན་གྱི་མེད་པ་ལ་སོགས་པར་བརྟགས་ནས་གཟུང་བ་ནི་གཟུང་བ་མ་ཡིན་ན། གཟུང་བས་སྟོང་པ་དེ་ཇི་ལྟར་གཟུགས་ཉིད་ལ་སོགས་པས་སྦྱོར་བར་བྱ་སྟེ།[^150] གལ་ཏེ་རྒྱུ་མེད་པར་འཛིན་པ་མེད་པའོ་ཞེ་ན། དེའི་ཕྱིར་གཟུགས་ལ་སོགས་པའི་རང་གི་ཡུལ་ལ་ངེས་པ་ཉིད་ནི་སྦྱོར་བར་མི་བྱ་བ་ཉིད་དོ། །

[Block 197]
གལ་ཏེ་འདི་ལྟར་རྫས་ལ་སོགས་པ་ལ་ཐ་མི་དད་པར་འཛིན་པ༌[^151]མཐོང་བ་དེ་ཇི་ལྟ་ཞེ་ན། གཞན་གྱི་ཡུལ། མིག་ནི་རེག་པར་བྱ་བ་དག་ལས་ཐ་དད་པའི་ཡུལ་ལ་དམིགས་པ་སྟེ། གཞན་ཉིད་དང་ལྷན་ཅིག་རྒྱུ་བའི་སྤྱིའི་ཡུལ་ལ་ཐ་མི་དད་དུ་འཛིན་པའི་དྲན་པའི་ཤེས་པ་སྐྱེས་པ་ཡིན་གྱི། གཟུགས་ལ་སོགས་པ་གཟུང་བ་ནི་མ་ཡིན་ཏེ། དེའི་བློ་མེད་པའི་ཕྱིར་རོ། །

[Block 198]
དེ་བཞིན་དུ་ཁྱད་པར༌[^152]མེད་པའི་ཕྱིར་དབང་པོ་རང་རང་གིས་ཡུལ་ཐ་དད་ལ་དམིགས་ཤིང་དོན་གཞན་རྣམ་པར་གཅད་པའི་ཡུལ་ལ་ཐ་མི་དད་ཀྱི་བློ་སྐྱེས་པ་ནི་ཐམས་ཅད་དུ་ཡིད་ཀྱི་ཤེས་པ་ཡིན་གྱི་ཡོད་པ་ཉིད་དང་ཡོན་ཏན་ཉིད་དག་ལས་སྐྱེས་པའི་མངོན་སུམ་ནི་མ་ཡིན་ཏེ། དེ་ཉེ་བར་མ༌[^153]མཚོན་པའི་ཕྱིར་རོ། །

[Block 199]
མངོན་སུམ་གྱིས་གཟུང་ངོ་སྙམ་པའི་ང་རྒྱལ་དེ་དག་ནི་རྟོག་གེ་ངན་པ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 200]
ཡུལ་དེ་མཚུངས་པར་འདོད་ཅེ་ན། འདི་ལྟར་འགྱུར་ཏེ་ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར་དུ་བྱ་བ་དག་ནི་དབང་པོའི་ཡུལ་དུ་མཚུངས་པར་ཁས་བླང་པར༌[^154]བྱ་སྟེ། དེ་མི་འཛིན་པ་ནི་དེའི་བློ་མེད་པའི་ཕྱིར་རོ་ཞེ་ན་དེ་ལྟ༌[^155]ཡིན་ན་ནི། མི་འདོད་པ་ལའང༌[^156]ཐལ་བར་འགྱུར། །གལ་ཏེ་གཉིས་ཀ་དབང་པོའི་གཟུང་བྱ་ཉིད་དུ་མཚུངས་པ་ཡིན་ན་ནི། རྫས་དང་ཡོན་ཏན་དང་ལས་དག་རྫས་དང་ལྡན་པ་ཡིན་པའི་ཕྱིར་ཡོད་པ་ཉིད་བཞིན་རྫས་དབང་པོ་ཐམས་ཅད་པར་འགྱུར་རོ། །

[Block 201]
དེ་བཞིན་དུ་རྫས་གཅིག་དང་ལྡན་པའི་ཕྱིར་རྫས་ཡོད་པ་ཉིད་མ་ཡིན་པ་བཞིན་དབང་པོ་ཐམས་ཅད་པ་ཡིན་པའི་ཕྱིར་ཡོད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 202]
གལ་ཏེ་རྫས་ལ་ཞུགས་པའི་ཡོད་པ་ནི་རྫས་གཅིག་པོ་དེ་དང་ལྡན་པར་བརྗོད་དོ་ཞེ་ན། མ་ཡིན་ཏེ་ཐ་དད་པ་མེད་པའི་ཕྱིར་ཡོད་པ་དང་ཐ་མི་དད་པ་ཡིན་ནོ། །

[Block 203]
ཐམས་ཅད་དུ་ཡོད་པ་ལ་རྫས་ལ་སོགས་པ་དགག་པར་བྱ་བ་ནི་མ་ཡིན་ཏེ། དེ་སྐད་དུ་ཡང་།

[Block 204]
ལས་དང་ཡོན་ཏན་ལ་ཡོད་ཕྱིར། །ཡོད་པ་ལས་མིན་ཡོན་ཏན་མིན། །ཞེས་བརྗོད་དོ། །

[Block 205]
གལ་ཏེ་ཡང་རྫས་ལ་ཞུགས་པ་རྫས་ཉིད་གཅིག་ཡིན་གྱི་གཞན་ལ་ཞུགས༌[^157]པ་རྫས་གཅིག་མ་ཡིན་ནོ་ཞེས་ཟེར་བ་ནི་རྫས་ཐ་དད་དུ་འགྱུར་རོ། །

[Block 206]
གང་གི་ཚེ་མིག་གིས་མངོན་སུམ་གྱིས་མི་དྲོའོ༌[^158]ཞེས་འཛིན་པ་དེའི་ཚེ་རེག་བྱ་ཡང་མིག་གི་གཟུང་བྱར་འགྱུར་རོ། །

[Block 207]
དེའི་ཕྱིར་ཡོད་པ་ཉིད་དང་ཡོན་ཏན་ཉིད་བཞིན་དབང་པོ་ཐ་དད་ཀྱི་གཟུང་བྱ་ཉིད་ཡིན་ཡང་རྫས་ཐ་མི་དད་དོ་ཞེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 208]
གལ་ཏེ་དེ་ལྟར་དབང་པོ་ཐ་དད་ཀྱི་གཟུང་བྱ་ཡིན་པའི་ཕྱིར་ཡང་གཞན་ཉིད་དུ་སྨྲ་བ་ཡིན་ན་ནི། མ་ངེས་དབང་པོ་གཅིག་གི་གཟུང་བྱ་ལ་ཡང་རྫས་དང་ཡོན་ཏན་དང་ལས་ཀྱི་ཐ་དད་དང་། སྔོན་པོ་ལ་སོགས་པའི་ཐ་དད༌[^159]མཐོང་སྟེ། དབང་པོ་ཐ་དད་མེད་ཀྱང་སྔོན་པོ་ལ་སོགས་པའི་ཐ་དད་དུ་འཛིན་པ་མཐོང་ངོ་། །གང་ཞིག་གང་མེད་ཀྱང་འབྱུང་བ་དེ་ནི་དེའི་རྒྱུ་མ་ཡིན་པའི་ཕྱིར་དབང་པོ་ཐ་དད་ནི་གཞན་ཉིད་ཀྱི་རྒྱུ་མ་ཡིན་ནོ་ཞེ་ན། དེ་ནི་གཞན་དུ་བརྗོད། དབང་པོ་ཐ་དད་ཀྱི་གཟུང་བྱ་ཡིན་པའི་ཕྱིར་ཞེས་པས་ནི་དུ་མ་ཉིད་དུ་བརྗོད་པ་ཡིན་གྱི། དབང་པོ་གཅིག་གི་གཟུང་བྱ་ཡིན་པའི་ཕྱིར་གཅིག་ཏུ་མ་ཡིན་ན་གང་ལས་མ༌[^160]ངེས་པར་འགྱུར། དབང་པོ་ཐ་དད་ཀྱི་གཟུང་བྱ་ཡིན་པ་ཁོ་ནས་དུ་མ་ཉིད་བརྗོད་པ་ནི་མ་ཡིན་གྱི། འོན་ཀྱང་དུ་མ་ཉིད་ཁོ་ན་ཡིན་པའི་ཕྱིར་མ་ངེས་པ་མ་ཡིན་ནོ། །

[Block 209]
དབང་པོ་ཐ་དད་མེད་ཀྱང་ཞེས་གང་བརྗོད་པ་འདིས། ཐམས་ཅད་བསྒྲུབ་བྱར་བརྗོད་མ་ཡིན། །དབང་པོ་ཐམས་ཅད་ཀྱི་ཐ་དད་ལས་དུ་མར་བརྗོད་པ་ནི་མ་ཡིན་ཏེ། གང་དབང་པོ་ཐ་དད་པ་དེ་དུ་མ་ཁོ་ནའོ་ཞེས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 210]
བློ་ཐ་དད་ཀྱང་གཞན་གྱི་རྒྱུ་ཡིན་པས་ནི༌[^161]མི་འགེགས༌[^162]སོ། །

[Block 211]
གཞན་ཡང་བློ་དབང་ཐ་དད་ལས་ཐ་དད། །གང་ལ་གཅིག་ཡིན་གཞན་དུ་ན། །དབང་པོ་ཡང་ཐ་དད་བློ་ཡང་ཐ་དད་པ་ལས་གཞན་ཉིད་དུ་མི་བརྗོད་པར་འགྱུར་རོ། །

[Block 212]
དབང་པོ་ཡང་ཐ་དད་བློ་ཡང་ཐ་དད་པ་དེ་ལ་ནི་གཅིག་ཉིད་ཡིན་ནོ་ཞེས་པའི་གོ་སྐབས་མེད་དོ། །

[Block 213]
དེ་དག་གི་ཡོན་ཏན་ལ་སོགས་པ་ལ་མངོན་སུམ་གྱིས༌[^163]ཤེས་པ་སྐྱེ་བ་ལ་ཡང་གསལ་བར་རིག་པར་བྱའོ། །

[Block 214]
དེ་དག་གིས་ནི་རང་གི་རྟེན་དང་འབྲེལ་བའི་སྒོ་ནས་གཞི་ལ་སོགས་པ་དང་ཕྲད་པ་ཉིད་བརྗོད་པ་ཡིན་ཏེ། དེ་ལྟ་ན་ཡང་ཐམས་ཅད་དུ་ཕྲད་པ་ལས་ཤེས་པ་སྐྱེ་བ་ནི་མ་ཡིན་ནོ་ཞེས་རིགས་པ་ཅན་གྱིས་མངོན་སུམ་བརྟགས་པར་ཇི་ལྟ་བ་བཞིན་དུ་བརྗོད་ཟིན་ཏོ། །

[Block 215]
དེའི་ཕྱིར་བྱེ་བྲག་པའི་མངོན་སུམ་ནི་སྒྲུབ་པར་དཀའོ། །
--- END BLOCKS ---
