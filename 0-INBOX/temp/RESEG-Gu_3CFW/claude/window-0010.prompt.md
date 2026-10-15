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
[Block 351]
ཕྱོགས་གང་དུ་ཞེ་ན། དེའི་ཕྱིར་འོག༌[^331]རོལ་གྱི་སུམ་ཆའི་དང་པོར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འོག་རོལ་ཞེས་བྱ་བ་ནི་རྐང་པའི་མཐའ་ལོགས་སུ་སུམ་ཆའི་གང་ཡིན་པ་དེའི་དང་པོ་དང་དབུས་དང་ཐ་མར་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 352]
གླེགས་བུ་གཅིག་པ་བྱིན་གྱིས་བརླབ་པར༌[^332]མི་བྱའོ་ཞེས་བྱ་བ་ནི་གདིང་བ་སྟེ་མ་མོ་ལས་འདུག་པ་འདི་ནི་འདིར་གདིང་བའོ། །

[Block 353]
གཡན་པ་དགབ་པ༌[^333]དེ་དང་ལྡན་པས་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་དང་ལྡན་པས་ཞེས་བྱ་བ་ནི་གཡན་པའོ། །

[Block 354]
དེ་ཞག་ལྔ་འམ་དྲུག་ཅིང་སྦྱང་བར་བྱའོ། །

[Block 355]
སྲིན་བལ་གྱི་དང་། བལ༌[^334]གྱི་དང་། ཤ་ནའི་དང་། ཟར་མའི་རུང་ངོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མ་སྨོས་པའི་ཕྱིར་བསམ་པའི་བྱེ་བྲག་གོ་བར་བྱེད་ནུས་པ་མེད་པའི་ཕྱིར་ཆོས་གོས་གསུམ་པོ་ཉིད་ཀྱིས་ཀྱང་ཆོས་གོས་ལྷག་པ་ཉིད༌[^335]ཀྱང་རིག་པར་བྱའོ། །

[Block 356]
སྲོག་ཆགས་ཀྱི་ཡན་ལག་རྣམས་བྱུང་བ་ཉིད་ཀྱི་ཕྱིར་ཀོ་ལྤགས་ལ་སོགས་པ་བཞིན་དུ་མི་རུང་བ་ཉིད་དུ་དོགས་པ་ལ། སྲིན་བལ་གྱི་དང་བལ་གྱི་དག་ཅེས་སྨོས་སོ། །

[Block 357]
ཤ་ནའི་དང༌[^336]ཟར་མའི་རུང་བ་དག་ལ་ནི་རྩུབ་པར་གྱུར་པའི་ཕྱིར་གསོ་མ་དག་གོས་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 358]
སྣམས༌[^337]སུ་མ་བྱས་པ་དང་གསོ་མ་ནི་མི་རུང་ངོ་ཞེས་བྱ་བ་ནི། དཔག་བསམ་གྱི་ཤིང་ལས་བྱུང་བའི་གོས་ལ་སོགས་པ་དང་། གསོ་མ་ལ་སོགས་པའི་གོས་ནི་མི་རུང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 359]
སྤང་པའི་ཞུ་བ་ལས་ཉེས་བྱས་བྱེད་པ་ཉིད་ཀྱི༌[^338]མི་རུང་བའི་ཁོངས་སུ་གང་ཞིག་མ་གཏོགས་པ་ལ་གོ་རིམས་བྱེད་པ་དེ་འདིར༌[^339]བསྡུས་པའོ། །

[Block 360]
སྐྲ་ལས་བྱས་པ་དང་གཅེར་བུ་པ་དང་བྱ་འུག་པ་བ་ཡང་དག་པར་ལེན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་མི་རུང་ངོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདིར་སོ་སོར་ཡང་དག་པར་ལེན་པའི་སྒྲ་མངོན་པར་འབབ་བོ། །

[Block 361]
སྐྲའི་ལ་བ་ཡང་དག་པར་ལེན་པ་དང་། །གཅེར་བུ་པ་ཡང་དག་པར་ལེན་པ་དང་། བྱ་འུག་པ་པ༌[^340]ཡང་དག་པར་ལེན་པ་དང་ནི་མི་རུང་ངོ་། །འདིར་གཞུང་ནི།

[Block 362]
དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 363]
མུ་སྟེགས་ཅན་གྱི་རྒྱལ་མཚན་གསུམ་པོ་གཅེར་བུ་པ་ཉིད་དང་། བྱ་འུག་པ་པ་ཉིད་དང་། སྐྲའི་ལ་བ་འཆང་བར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 364]
མུ་སྟེགས་ཅན་གྱི་རྒྱལ་མཚན་གསུམ་པོ་དག་མ་གཏོགས་པ་དེ་ལས་གཞན་པའི་མུ་སྟེགས་ཀྱི༌[^341]རྒྱལ་མཚན་འཆང་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 365]
ཡང་དག་པར་བླང་བ་མངོན་དུ་གཏོང་བས་འཆང་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 366]
དེ་ལ་སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི་སྐྲ་ལས་བྱས་པ་དང་། གཅེར་བུ་དང་། བྱ་འུག་པ་པ་ཡང་དག་པར་ལེན་པ་དེ་ལ་ནི་དགེ་འདུན་གྱི་དབྱེན་གྱི་ཕྱོགས་སུ་གཏོགས་པའི་ཉེས་པ་སྦོམ་པོར་གྱུར་པར་རིག་པར་བྱའོ། །

[Block 367]
གཞན་བསྟེན་པ་ནི་དེའི་འོ་ཞེས་བྱ་བ་ནི་གསུམ་པོ༌[^342]དག་ལས་གཞན་པའི་ཡང་དག་པར་བླང་བ་སྔོན་དུ་བཏང་བས་བསྟེན་པ་ནི་བསྟེན་དུ་རུང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 368]
ཡང་དག་པར་བླང་པ་སྔོན་དུ་བཏང་བའི་བསྟེན་པ་ལ་ནི་ཉེས་བྱས་ཏེ་ད་བས་ན་དེའི་འདི་བྱེད་པའོ། །

[Block 369]
ཐམས་ཅད་དུ་མུ་སྟེགས་ཀྱི་རྒྱལ་མཚན་འཆང་བ་དེ་དག་དག་པ་དང་གྲོལ་བར་འཛིན་པས་འཆང་ན་ནི་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 370]
འདིར་ཡང་དག་པར་བླང་བ་ལ་ཐ་དད་པ་ཉིད་ཡིན་ཏེ། སྦྱོར་བ་གྲུབ་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 371]
དེ་ལ་ཡང་འདིར་སྦོམ་པོ་ཉིད་དུ་ལོགས་ཤིག་ཏུ་གསུངས་པས་གལ་ཏེ་འདིར་དག་པ་དང་གྲོལ་བ་ཉིད་ལས་འདིས༌[^343]ཞེས་བྱ་བ་ལ་སྦོམ་པོའོ་ཞེས་དེའི་རྗེས་སུ་འབྲང་བར་རྟོགས་པར་བྱའོ། །

[Block 372]
སྐྲ་འབལ་བ་དང་། ལོ་མ་གྱོན་པ་དང་། གཡང་གཞིའི་སྨད་གཡོགས་སྟོད་གཡོགས་དང་བཅས་པས༌[^344]འཚོ་བ་དང་། གསོ་རས་དང་ཡན་ལག་གི་སྦུབས་དང་གོས་ཐམས་ཅད་སྔོ་བ་དང་། གདེངས༌[^345]ཀ་ལྟ་བུ་དང་ཁ་ཚར་རིང་པོ་དང་། རལ་ཀ༌[^346]དང་གཙུག་གཏོར༌[^347]དང་མགོ་དཀྲི་བ་དང་། ར་ཕྱར་དང་རྔ་བལ་གྱི་སྣམ་བུ་དང་། མུ་སྟེགས་ཅན་གྱི་རྒྱལ་མཚན་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་མི་རུང་ངོ་ཞེས་སྦྱར་རོ། །

[Block 373]
གསོ་རས་ཞེས་བྱ་བ་ནི་འདབ་མ་ལས་མ་བྱས་པའི་གོས་ཞེས་བྱ་བ་ནི་རྒྱ་གར་བ་རྣམས་འདོད་དོ། །

[Block 374]
ཁ་ཆེ་བ་རྣམས་ནི། གསོ་མ་ལས་བྱས་པའི་གོས་སེང་སེང་པོའི་གོས་འདིའོ། །

[Block 375]
ཡན་ལག་གི་སྦུབས་ཞེས་བྱ་བ་ནི་ནུ༌[^348]མ་ལ་སོགས་པ་གཡོགས་པའི་གོས་སོ། །

[Block 376]
གོས་ཐམས་ཅད་སྔོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ།[^349] །འདིར་ཁ་ཅིག་ནི་ཐམས་ཅད་སེར་བ་དང་ཐམས་ཅད་དམར་བ་དག་ལ་ཡང་བཀག་གོ་ཞེས་ཟེར་ཏེ། འདི༌[^350]ནི་མི་རིགས་པ་སྟེ། དེ་གཡོགས་པ་ལ་མི་འདུན་པ༌[^351]ཉིད་དུ་མ་མཐོང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 377]
རལ་ག་ཞེས་བྱ་བ་ནི་ལྷམ་སྒྲོག་གུ་ཅན་གྱི་རྣམ་པའོ། །

[Block 378]
འདིས་ཤིང༌[^352]དཔུང་ཆད་རྗེས་སུ་གནང་བ་འགལ་བ་མེད་དེ་ཤིང༌[^353]དཔུང་ཆད་ནི་རྣམ་པ་གཞན་གྱི་ཕྱིར་རོ། །

[Block 379]
དཔེར་ན་ལྷམ་ཡུ་རིངས་ཀྱི་རྣམ་པ་ལས་ལྷམ་སྒྲོག་གུ་ཅན་གྱི་རྣམ་པ་ཅུང་ཟད་ཞན་པ་དང་འདྲའོ།[^354] །མགོ་དཀྲི་བ་ཞེས་བྱ་བ་ནི་གཙུག་ཏོར་མ་ཡིན་པ་དང་འདྲ་བ་ཡིན་ཏེ། དེ་ནི་རང་གི་སྒྲས་སྨོས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 380]
ར་ཕྱར༌[^355]ཞེས་བྱ་བ་ནི་ར་བལ་ལས་བྱས་པའི་ཕྱར་བའོ། །

[Block 381]
རྔ་བལ་གྱི་སྣམ་བུ་ཞེས་བྱ་བ་ནི་རྔ་མོའི་བལ་ལས་བྱས་པའི་སྣམ་བུའོ། །

[Block 382]
མུ་སྟེགས་ཀྱི་རྒྱལ་མཚན་ཡང་ཞེས་བྱ་བ་ལ། ཡང་གི་སྒྲས་ནི་མི་རུང་ངོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དེ་ལྟ་བས་ན༌[^356]སྐབས་སུ་རྫོགས་པ་རབ་ཏུ་བསྟན་པའི་དོན་དུའོ། །

[Block 383]
ལྷག་མ་བརྩམས་པ༌[^357]རྣམས་ལས་མུ་སྟེགས་ཀྱི་རྒྱལ་མཚན་འཛིན་པ་སྒྲུབ་པའི་དོན་དུ་ནི་དེའི་སྒྲའོ། །

[Block 384]
པུ་ས་ལའི་འདབ་མ་གང་དང་མར་མེའི་སྙིང་པོ་ཙམ་དེས་ཀྱང་སྙོམས་པར་བྱ་བའི་ཕྱིར་བགོ༌[^358]བཤའ་བྱའོ་ཞེས་བྱ་བ་ནི་བཟའ་བར་བྱ་བའི་ཟས་ནི་ཐ་ན་ཤིང་པུ་ས་ལའི་ལོ་མ་གང་ཙམ་དེས་དབང་བ་ཐམས་ཅད་ལ་སྙོམས་པར་བྱ་བའི་ཕྱིར་བགོ་བཤའ་བྱའོ། །

[Block 385]
གོས་ནི་ཐ་ན་མར་མེའི་སྙིང་པོ་ཙམ་དེས་ཀྱང་བགོ་བཤའ་བྱའོ། །

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
--- END BLOCKS ---
