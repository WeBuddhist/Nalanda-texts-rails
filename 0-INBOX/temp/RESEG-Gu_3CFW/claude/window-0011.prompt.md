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
[Block 386]
འདིར་གཞུང་ནི། ཕྲན་ཚོགས་དག་ལས་དེ་ནས་བརྩམས་ཏེ་ངེས་པ་མ་ཡིན་ཞེས་བྱ་བའི་བར་དུ་འདི༌[^359]དྲངས་པའོ། །

[Block 387]
ལ་བ་དང་དེ་ལྟ་བུ་དག་ནི་བཙོངས༌[^360]ཏེའོ་ཞེས་བྱ་བ་ནི་བགོ་བཤའ་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 388]
མི་བཤིགས་པ༌[^361]ཉིད་དོ་ཞེས་བྱ་བ་ནི་དེ་ལས་གཞན་པའི་གོས་བཞིན་དུ་མི་བཤིགས་པ༌[^362]ཉིད་ཡིན་ནོ། །

[Block 389]
རྙེད་པ་བགོ་བ་ལ་ལྔ་བྱའོ། །

[Block 390]
རྙེད་པ་བགོ་བ་ལ་བྱ་བ་ལྔ་བྱ་བ་དེ༌[^363]དག་གང་ཞེ་ན། དེའི་ཕྱིར་དེར་རྙེད་པ་འགོད་པར༌[^364]འགྱུར་གྱི་དེར༌[^365]ཁྱེད་ཅག་གིས་ཚོགས་པར་བྱའོ་ཞེས་དགེ་འདུན་ལ་བརྗོད་པར་བྱ་བ་དང་། གཎྜཱི་བརྡུང་བ་དང་། ཚུལ་ཤིང་བྲིམ་པ༌[^366]དང་། བགྲང་བ་དང་། སོ་སོའི་སྐལ་བ་བྲིམ༌[^367]པའོ། །

[Block 391]
ཐ་མ་ཡན་ཆད་བྱེད་པ་ཉིད་ན་འོངས་པ་དབང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྙེད་པ་འགོད་པའི་དུས་སུ་བྱ་བ་ལྔ་པོ་དེ་དག་གི་གཞན་དེ་སྲིད་དུ་བྱ་བ་ཉིད་ལ་འོངས་པ་ལ་བརྟེན་པ་ཉིད་དོ། །

[Block 392]
རེ་ཞིག་འདིར་དབང་བྱེད་པ་ཉིད་ལ་ལྔ་པོ་འདིར་ངེས་པ་ལ་དབང་དུ་བྱ་བ་ཉིད་ཡིན་ནམ་འོན་ཏེ་ཅི་ཡང་མ་ཡིན་སྙམ་དུ་མི་ཤེས་པའི་བློ་ཅན་དག་ལ་གསུངས་པ་ནི། དེའི་ཕྱིར་མཇུག་ཏུ་ཕྱིན་པ་ཉིད་ནི་མི་དབང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡོངས་སུ་རྫོགས་པ་ལ་ལྔ་པོ་མི་དབང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 393]
དེ་ནི༌[^368]རྙེད་པ་ཆུང་ངུ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ལྔ་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེའི་ནི་རྙེད་པ་ཆུང་ངུ་ལ་ཡང་བྱའི་རྙེད་པ་ཆེན་པོ་འབའ་ཞིག་ལ་བྱ་བར་མ་ཟད་དོ། །

[Block 394]
རྙེད་པའི་བྱ་བ་དེར་ཞུགས་ནས་སོང་བ་ཉིད་ཡིན་ཡང་མི་དབང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དབྱར་གནས་པ་ལ་སོགས་པའི་ལས་གང་གིས་རྙེད་པ་འགྲིམ་པར་བྱེད་པའི་བྱ་བ་དེར་ཞུགས་པར་གྱུར་ན། གཙུག་ལག་ཁང་གི་མཚམས་ལས་འདས་ཏེ་སོང་བ་ཡང་རྙེད་པ་དེ་མི་འོས་པ་མ་ཡིན་ནོ། །

[Block 395]
དེའི་ཕྱིར་འགྲོ་བས་ནོད་པ༌[^369]བཅོལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་རྙེད་པ་དེ་འོས་པ་དེ་བས་ན་འགྲོ་བས་རང་གི་སྐལ་བ་མནོད་པ་གཞན་ལ་བཅོལ་བར་བྱའོ། །

[Block 396]
ཁས་བླངས་པ་དང་ལྡན་པས་མ་མནོས་ན་བསབ་པར༌[^370]བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། མནོད་དོ་ཞེས་དེ་ལྟར་དམ་བཅའ་བར༌[^371]བྱེད་ཅིང་གལ་ཏེ་རྙེད་པ་མ་མནོས་ན་དེའི་ཚེ་རང་གི་སྒོ་ནས་བསབ་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 397]
རྙེད་པ་ཆུང་ངུ་ལ་པ་ན་ལྔ་ལ་སོགས་པའོ་ཞེས་བྱ་བ་ནི། རྙེད་པ་ཆུང་ངུ་ལ་ཡང་གལ་ཏེ་མངོན༌[^372]པར་ཁས་བླངས་པ་དང་ལྡན་པ་མ་མནོས་ན་བགོ་སྐལ་མ་ཤ་ཀ་ལྔ་འམ་དེ་ལས་ལྷག་པ་ཡིན་ན་དེ་ལ༌[^373]བསབ་པར་བྱ་བ་ཉིད་ཡིན་པའོ། །

[Block 398]
མ་བཅོལ་ན་མནོད་པར༌[^374]མི་བྱའོ། །

[Block 399]
སློབ་དཔོན་ནམ་མཁན་པོའི་ནི་མནོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་མ་བཅོལ་ཡང་རྙེད་པ་མནོད་པར་བྱའོ། །

[Block 400]
ཡིད་གཅུགས༌[^375]པའི་གནས་ཀྱི་དོན་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ཡིད་གཅུགས༌[^376]པའི་གནས་སུ་གྱུར་པ་གང་ཡིན་པ་དེའི་དོན་དུ་མ་བཅོལ་ཡང་མནོད་པར་བྱ་སྟེ། སློབ་དཔོན་དང་མཁན་པོར་གྱུར་པ་ཉིད་ལ་མནོད་པར་བྱའོ། །

[Block 401]
རང་གི་ཕྱོགས་དང་མཐུན་པ་མ་ཡིན་པའི་དོན་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བྱེ་བའི་ཕྱོགས་སུ་སོང་བའི་དོན་དུ་ཡང་མནོད་པར༌[^377]མི་བྱའོ། །

[Block 402]
དེ་ནི་གནས་མལ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། གནས་མལ་གནོད༌[^378]པར་བྱ་བ་ཉིད་ལ་ཡང་དེ་མ་བཅོལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པར་རྟོགས་པར་བྱའོ། །

[Block 403]
འདིར་གཞུང་ནི།

[Block 404]
གནས་མལ་གྱི་གཞུང་ཞུ་བ་ལས།

[Block 405]
ཡིད་གཅུགས༌[^379]གནས་ཀྱི་དོན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་གང་གིས་བཅོལ་བ་གང་དུ་ཡང་ཡིད་ཆེས་པའི་དོན་དུ་གྱུར་པ་སྟེ། དེའི་ཕྱིར་མངོན་དུ་ཕྱོགས་པར་གྱུར་པའི་དོན་ལ་གནས་མལ་མནོད་པར༌[^380]བྱའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། ཁས་བླངས་པས་ཁས་མ་བླངས་པ་ལ༌[^381]ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེར་དོན་དེ་ཙམ་དུ་གསུངས་སོ། །

[Block 406]
རྙེད་པ་ལ་ཡང་སྦྱོར་བ༌[^382]འདི་རྙེད་པ་མ་ཡིན་པར་འབྲེལ་བ་ལ་ཡང་འདིར་ཡང་ཞེས་བྱ་བ་དེ་ལྟར་སྨོས་སོ། །

[Block 407]
ཟས་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་མ་བཅོལ་ན་མནོད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^383]རིག་པར་བྱ་བ་སྟེ། འདིར་གཞུང་ནི། འདུལ་བྱེད་དག་ལས་ཐ་སྙད་འདི་ཡིན་ནོ། །

[Block 408]
འགོད་པ་དང་མ་བྱིན་པར་ལེན་པར་གཏོགས་པ་འདི་ཡང་གཞན་གྱི་ཚིག་གི་སྐབས་མེད་པའི་ཕྱིར་ཏེ། [^384]མ་བཅོལ་ན་མནོད་པར་མི་བྱའོ་ཞེས༌[^385]བྱ་བ་དེ་ཙམ་ཞིག་དེར་དོན་གསུངས་སོ། །

[Block 409]
དེ་ཐམས་ཅད་ལ་མ་བཅོལ་བ་ཉིད་ལ་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིར་རྣམ་པར་གཞག་པ་དེའི་ཕྱིར་ཐམས་ཅད་དེ་འདིར་སྦྱར་བར་བྱའོ། །

[Block 410]
གཞན་གྱི་དོན་དུ་མནོད་པར་ཕ་རོལ་ལ་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་ཡང་མནོད་པར་བྱ་སྟེ། ཟས་གཅིག་པུ་ནི་མ་ཡིན་ནོ། །

[Block 411]
འདིར་གཞུང་ནི་འདུལ་བྱེད་དག་ལས།

[Block 412]
ཐ་སྙད་འདི་འགྱོད་པ༌[^386]གཅིག་པུ་ལས་སྐབས་མེད་པར་བྱ་བའི་ཕྱིར་ཟས་མནོད་པ་ལས་གླེང་གཞི་དེ་ལས་བྱེད་པའོ། །

[Block 413]
ཐ་སྙད་ལ་ནི་ཟས་མནོད་པ་མ་ཡིན་ཏེ། མནོད་པར་བྱེད་པས་གཞན་ལ་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ཙམ་ཞིག་གསུངས་ཏེ་གཞན་དུ༌[^387]མནོད་པར་བྱ་བ་ལ་ཆོ་ག་འདི་རྣམ་པར་གཞག་པར་བྱ་བ་སྟེ། དེ་ལྟར་ན་བྱེ་བྲག་ལ་མ་བརྟེན་པའོ། །

[Block 414]
མི་དབང་བས་ནང་དུ་ཞུགས་ཏེ་མི་བྱའོ་ཞེས་བྱ་བ་ནི། རྙེད་པ་མི་དབང་བས་གང་དག་དབང་བ་དེ་དག་གི་ནང་དུ་ཞུགས་ཏེ་སྐལ་བ་མནོད་པར་མི་བྱའོ། །

[Block 415]
འདིར་གཞུང་ནི། དེ་ལྟ་བས་ན་དགེ་སློང་གི་གཞན་གྱི་རྙེད་པར་འཇུག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 416]
འདིར་དཔེ་གཞན་ཡང་ཚེ་དང་ལྡན་པ་ཉེ༌[^388]དགའ་མགྲོན་དུ་མ་བོས་པས་ཟས་ཟོས་ནས་རས་ཡུག་ཆེན་མནོས་པ་བཞིན་ནོ། །

[Block 417]
དབང་བ་གཅིག་ཉིད་ཀྱིས་ཤིན་ཏུ་མང་པོ་ཐོབ་པ་ལ་མི་དབང་བའི་རྒྱུར་འགྱུར་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། གང་ཟག་གང་དེ་དག་ལ་འདིར་ལུང་ནི་རྒན་ཞུགས་དེ་གཉིས་འདི་སྙམ་དུ་བདག་ཅག་གཉིས་ལས་རས་ཡུག་ཆེན་བརྒྱ་ཇི་ལྟར་འབྱུང་བར་འགྱུར་ཏེ། གཞན་ནས་འཇུག་ཏུ་གཞུག་པར་བྱའོ་སྙམ་དུ་སེམས་པ་དེ་བསལ་བའི་དོན་དུ་དེ་ཡིན་ཏེ། གང་ཞིག་དེད་དཔོན་གྱིས༌[^389]དགེ་འདུན་གྱི་ཕྱིར་གཙུག་ལག་ཁང་དུ་རྙེད་པ་མང་པོ་བསྐུར་བ་ནས་གཙུག་ལག་ཁང་དེ་ན་དགེ་སློང་གཅིག་པུ་ཞིག་གནས་པ་དེ་འགྱོད་པས་མི་ལེན་པ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་དེ་ནི་དེ་ན་གང་གནས་པ་དེའི་ཕྱིར་ཡིན་ནོ་ཞེས་རྗེས་སུ་གནང་བའི་བར་དུ་གསུངས་པ་དེ་ནི་དཔེ་གཞན་ཡིན་ནོ། །

[Block 418]
བྱེ་བ་ནི་ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་དག་ཏུ་སོང་བ་དགེ་འདུན་གྱི་རྙེད་པ་མི་དབང་ངོ་ཞེས་བྱ་བ་ནི། ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་ཐ༌[^390]དད་པ་རྣམས་ལ་ཆོས༌[^391]ཀྱི་ཕྱོགས་དོར་ནས་སོང་བ་གང་ཡིན་པ་དེ་དགེ་འདུན་གྱི་རྙེད་པ་མི་དབང་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 419]
དེའི་དུས་ཀྱི་རྙེད་པ་ལ་ནི་ཆེས་རིང་དུ་གནས་ན་གནས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེའི་དུས་ཀྱི་ཞེས་བྱ་བ་ནི་དབྱར་གནས་པ་ལ་སོགས་པའི་དོན་དུས་དེར་རོ། །

[Block 420]
དེ་ནི་འདིར་སྐབས་དང་མཐུན་པ་ཐ་དད་པ་ཉིད་ཀྱི་དོན་ཞེས་བྱ་བ༌[^392]སྨོས་སོ། །

[Block 421]
འདིར་བརྗོད་པ་ཡང་བབས་པ་དང་ཤི་བར་གྱུར་པ་གཉིས་ལ་ཡང་མི་འོས་པ་ཉིད་ཀྱི་དོགས་པ་ཡོད་པར་འགྱུར་བ་དེ་བས་ན་དེའི་ཕྱིར་བརྗོད་པར་བྱ་སྟེ། བབས་པ་དང་ཤི་བར་གྱུར་པ་གཉིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་འདི་གཉིས་ཀྱང་ཆེས་རིང་དུ་གནས་པ་ཡིན་ན༌[^393]དེའི་དུས་ཀྱི་རྙེད་པ་དབང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 422]
ཤི་བའི་ཕྱིར་འདི་སྨོས་པ་ལ་དགོས་པ་ཅི་ཡོད་ཅེ་ན། གལ་ཏེ་སུ་ཞིག་ལ་ཕུལ་ནས་ཤི་ན་བུ་ལོན་འདི་ལ་ཡོད་པའམ། ཉེ་བར་གནས་པས་ཡོ་བྱད་དྲུག་པོ་མ་ཐོབ་ན་དེ་ལ་སྦྱིན་པར་བྱའོ། །

[Block 423]
གལ་ཏེ་མ་ཡིན་ན་གང་རྣམས་ཀྱིས་དེ་ནི༌[^394]ཤི་བའི་ཡོ་བྱད་ལ་དབང་བ་ཉིད་དེ་དེ༌[^395]རྣམས་ལ་འདིར་རྙེད་པ་ཞེས་བྱ་བ་འདི་བསྟན་པའོ། །

[Block 424]
རྙེད་པ་ནི་ཇི་ལྟར་རྣམ་པར་ངེས་པར་བྱེད་པ་ལྟར་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་ནི། གཙུག་ལག་ཁང་འདི་ན་གནས་པའི་དགེ་སློང་རྣམས་ཀྱིས་གནས་མལ་དང་བསོད་སྙོམས་ལ་སོགས་པ་འདི་ལོངས་སྤྱོད་པར་བྱའོ་ཞེའམ། དེ་ན་གནས་པའི་རྟེན་པ༌[^396]ལ་རྐང་པའི་མར་བསྐུ་བ་ལ་སྦྱར་བར་བྱའོ། །

[Block 425]
སྨན་གྱི་རིན་ལ་སོགས་པ་དང་ཞེས་བྱ་བ་འདིར་སྤྲོས་པ་མ་བྱས་ཏེ། སྤྲོས་པ་མ་བྱས་པ་ནི་གནས་ཁང་ལ་སོགས་པ་དགེ་སློང་གི་དབང་དུ་མཛད་ནས་རྙེད་པ་གནང་བ་ལ་དེ་ལྟ་བུར་གྱུར་པ་ཉིད་ཀྱིས་ལོངས་སྤྱད༌[^397]པར་བྱའོ། །
--- END BLOCKS ---
