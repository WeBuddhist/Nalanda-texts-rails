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
[Block 526]
དེ་དང་ལྷན་ཅིག་རྣམ་པར་གཞག་པ་དེ་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་དམ་བླང་བར་བྱ་བ་ཉིད་གང་ཡིན་པ་སྟེ། དེ་ཉིད་ནི༌[^465]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཤི་བ་དེ་དང་བུ་ལོན་དེད་པ་དང་། བུ་ལོན་འཇལ་བར་ལྷན་ཅིག་གང་ཞིག་གནས་པ་དེ་ལ་འདིར་དགེ་སློང་རྣམས་ཀྱིས་གཞལ་བར་བྱ་བའམ། བསླང་བར༌[^466]བྱ་བ་ཉིད་དེ་དེ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 527]
གང་ཞིག་དེས་བུ་ལོན་པའི་དྲུང་ནས་བླངས་པ་དེ་བུ་ལོན་ཆགས་པ་ལ་སྦྱིན་པའོ། །

[Block 528]
ཀཱཪྵཱ་པ་ཎ་རྣམས་དབུལ་བར་བྱའོ་ཞེས་བྱ་བས་ཀཱཪྵཱ་པ་ཎ་རྣམས་བཟུང་བ་དེ་རྣམས་ཉིད་གཞལ་བར་བྱའོ། །

[Block 529]
རས་ཡུག་ཆེན་བླངས་ཏེ་རིན་སྦྱིན་པར་བྱའོ་ཞེས་འཐམས་པ༌[^467]ལ་ནི་རིན་སྦྱིན་པར་བྱའི་རས་ཡུག་ཆེན་དངོས་སྦྱིན་པར་མི་བྱ་བ་དང་། ཐ་ག་པ་ལ་རས་ཡུག་ཆེན་གྱི་དོན་དུ་རྒྱུ་སྤུན་གཏད་པ་ལས་ནི་རས་ཡུག་ཆེན་བླང་བར་བྱའི། [^468]རྒྱུ་སྤུན་བླང་བར་མི་བྱ་བ་ལྟ་བུའོ། །

[Block 530]
འདིར་གཞུང་ནི། དགེ་སློང་གིས་ཕྲ་བ་བསླངས་པ་དང་། དེ་ན་རེ་འཕགས་པ་དག་བདག་གིས་དེ་ལ་སྦོམ་པོ་དབུལ་བར༌[^469]བགྱི་བ་ལགས་སོ་ཞེས་ཟེར་ནས།[^470] བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་དག་དགེ་སློང་ཤི་བ་ཅི་འདྲ་བ་གཏད་པ་དེ་འདྲ་བ་བསླང་བར༌[^471]བྱའོ་ཞེས་གསུངས་པ་དེ་ནི་ཐ༌[^472]སྙད་ཀྱི་ཆོ་གས་ངེས་པར་དེ་བླང་བ་མ་ཡིན་ནོ། །

[Block 531]
དེའི་ཕྱིར་འདིར་འབད་པར་མི་བྱ་སྟེ། དེ་ནི་འབད་པའི་གནས་མ་ཡིན་ནོ་སྙམ་པ་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 532]
གལ་ཏེ་ཐ་སྙད་ཙམ་སློབ་པ་དེའི་ཕྱིར་འདིར་མདོར་བྱས་སོ། །

[Block 533]
དེ་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ལ་བུ་ལོན་ཆགས་པ་ཉིད་དུ་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་ཤི་བ་ལ་བུ་ལོན་ཆགས་པ༌[^473]དེས། དེའི་དོན་ལས་མ་དག་པ་བྱས་པར་འདི་ལ་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ཀྱིས༌[^474]གཞལ་བར་བྱ་བ་ཉིད་ནི་མ་ཡིན་ནོ༌[^475]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 534]
ལག་གི་བླས་དཀོན་མཆོག་གི་བླངས་པ་ཉིད་ཡིན་ཞེ༌[^476]ན་དེའི་ཕྱིར༌[^477]ཇི་སྙེད་པ་དེ་སྙེད་མཉམ་པར་བསབ་བོ༌[^478]ཞེས་བྱ་བ་ན།[^479] སངས་རྒྱས་ལ་སོགས་པ་དཀོན་མཆོག་རྣམས་ཀྱི་དཀོར་ནི་དཀོན་མཆོག་གིའོ། །

[Block 535]
དེ་བླངས་པ་ནི་འདིས་བཟུང་བ་སྟེ། དེ་བས་ན་དཀོན་མཆོག་གི་བླངས་པ་ཉིད་དེ། དེའི་དངོས་པོ་ནི་དེ་སྙེད་མཉམ་པར་བསབ་པར་བྱའོ། །

[Block 536]
དེའི་ཇི༌[^480]སྙེད་པ་ལས་ཞེས་བྱ་བ་ནི་དཀོན་མཆོག་གི་ཇི་སྙེད་པ་ལས་དེ་དང༌[^481]འབྲེལ་བ་བླངས་པ་ཉིད་ནི་མཉམ་པར་བསབ་སྟེ། དེ་སྙེད་པའི་དཀོན་མཆོག་ལ་ཆ་མཉམ་པར་བྱ་སྟེ་མཉམ་པར་བསབ་པར་བྱ་སྟེ། [^482]འོན་ཀྱང་གལ་ཏེ་ཐ་དད་པར་བྱེད་པ་དེ་དགེ་འདུན་གྱི་ནི་མཆོད་རྟེན་གྱིར་བྱེད། མཆོད་རྟེན་གྱི་ནི་དགེ་འདུན་གྱིར་བྱེད་དེ་དེ་བཞིན་དུ་ཆོས་ཀྱི་ཡང་འདྲེས་པར་བྱེད་ན་ལྷུང་བཟེད་དང་ཆོས་གོས་ལས་ཆ་གསུམ་དུ་བྱས་ཏེ་ཞེས་བྱ་བ་གསུངས་སོ་ཞེ་ན། འོན་ཀྱང་བདེན་མོད་ཀྱི་དེ་ལྟར་འདིས་དཀོན་མཆོག་གི་བླངས་པར་མི་འགྱུར་བ་ཡིན་ཏེ། གང་གི་ཕྱིར་རང་གི་འདོད་པ་བྱས་པས་གཞན་དང་འབྲེལ་བ་ལ་གཞན་དག་ལ་སྟེར་བ་ནི་མ་ཡིན་ནོ། །

[Block 537]
དེ་ནི་སྦྱིན་བདག་ཏུ་མི་འགྱུར་ཏེ། མཉམ་པར་བསབ་པ་ཉིད་འདི་ཤེས་པར་བྱེད་པ་ལ་དེ་ཉིད་འདིའི་དགོངས་པས་རྣམ་པར་གནས་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་མ་བླངས་པ་ལ་སྦྱིན་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 538]
ཡིན་ན་ཞེས་བྱ་བ་སྨོས་པ་གང་ཡིན་པ་དེ་ཡང་དྲང་སྲོང་གི་ཡེ་ཤེས་ཀྱིས་ཐ་སྙད་མ་ཡིན་ནོ། །

[Block 539]
རབ་ཏུ་གྲགས་པ་ཅན་གྱིས་ཀྱང་སྡུག་བསྔལ་ཏེ། དེ་ལྟ་བུར་གྱུར་པ་ལས་བསལ་བར་ཤེས་པའོ། །

[Block 540]
དེ་བས་ན་འདི་ལྟ་བུའི་དབང་བརྩན༌[^483]ཁོ་ན་དེ་རྣམ་པར་གནས་པ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 541]
གང་ཞིག་འདིར་ཇི་སྲིད་དུ་བླངས་པ་དེ་སྲིད་དུ་ཆ་གསུམ་བྱའོ། །

[Block 542]
ལྷག་མ་ནི་དགེ་འདུན་ཉིད་ལ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 543]
དེ་ཡང་དེ་ཉིད་ཀྱི་ཕྱིར་གཟུང་བར༌[^484]དཀའ་བས་ཞེས་བྱ་བ་མཐོང་ངོ་། །དེ་ནི་གཟུང་བར༌[^485]དཀའ་བ༌[^486]འདིས་ལྷག་པར་ཕུལ་བ་ལ་སྐྱོན་ཡོན་ཡང་མེད་དེ། དེ་བས་ན་ཐམས་ཅད་བླངས་པ་ལ་བགོ་བཤའ་བྱེད་པ་ཞེས་བྱའོ། །

[Block 544]
ལག་གི་བླས༌[^487]ཞེས་སྨོས་པ༌[^488]ནི་འདིར་མཚོན་པ་ཙམ་དུ་རིག་པར་བྱའོ། །

[Block 545]
གཞན་དུ་ཡང་འདིས་དཀོན་མཆོག་གསུམ་གྱི་དཀོར་བླངས་ཤིང་ཁྱེར་བ་གཉིས་ཡིན་ནོ་སྙམ་དུ་ཤེས་ནས། དེའི་དཀོར་ལ་ཡང་འབུལ་བར་རིགས་པའི༌[^489]ཕྱིར་རོ། །

[Block 546]
ནད་གཡོག་དང་བཅས་པ་ཉིད་ཡིན་ན་ཡོ་བྱད་དྲུག་པོ་དེ་བདག༌[^490]དབང་བ་ཉིད་ཡིན་པས་བྱིན་གྱིས་བརླབ་པར་མི་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་དབང་བ་ཉིད་ཡིན་པས་ཞེས་བྱ་བ་ནི་དེ༌[^491]ནད་གཡོག་དེ་དབང་བ་ཉིད་ཡིན་པས་དགེ་སློང་རྣམས་ཀྱིས་བྱིན་གྱིས་མི་བརླབ་པར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 547]
དེའི་རབ་དང་འབྲིང་དང་ཐ་མ་དང་བཅས་པ་ལས་སོ་ཞེས་བྱ་བ་ནི་དེ་ལ་ཁ་ཅིག་ནི་དགེ་སློང་གི་ཡོ་བྱད་དང་འཚོ་བའི་ཡོ་བྱད་རབ་ལས་སྦྱིན་པར་བྱའོ། །

[Block 548]
ཁ་ཅིག་ནི་འབྲིང་། ཁ་གཅིག༌[^492]ནི་ཐ་མ་དང་ལྡན་པའོ། །

[Block 549]
གསུམ་པོ་འདི་དང་བཅས་པ་དྲུག་པོ་སྦྱིན་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 550]
དུ་མ་ཉིད་ཡིན་ན་ཐུན་མོང་ངོ་ཞེས་བྱ་བ་ནི་ནད་གཡོག་གཉིས་སམ་གསུམ་མམ༌[^493]མང་པོ་ཉིད་ཡིན་ན། ཡོ་བྱད་དྲུག་པོ་དེ་དག་གི་ཐུན་མོང་ཉིད་ཡིན་ནོ། །

[Block 551]
དེའི་དོན་དུ་སོང་བ་ཉིད་ཡིན་ལ་ནད་པ་ཤི་ན་སྦྱིན་པར་བྱ་བ་ཉིད་ཅེས་བྱ་བ་ལ། དེའི་དོན་དུ་ཞེས་བྱ་བ་ནི་ནད་པ་དེའི་དོན་དུའོ། །

[Block 552]
བཅས་པ་ཉིད་ཡིན་ན་ཞེས་བྱ་བ་ནི། གལ་ཏེ་ནད་པའི་དོན་དུ་ནད་གཡོག་དང་བཅས་པར་འགྱུར་བ་དེ་ལྟ་བས་ན་ཡང་ཡོ་བྱད་དྲུག་པོ་འདི་སྦྱིན་པར་བྱ་བ་ཉིད་ཡིན་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 553]
དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 554]
དེ་དག་ལ་སོགས་པ་འདིར་བསྙེན་པར་མ་རྫོགས་པ་ལ་ཐམས་ཅད་འོས་པ་ཉིད་ཅེས་བྱ་བའི་མཐར་ཐུག་པ་གསུངས་པའོ། །

[Block 555]
རྫས་དེ་མི་དབང་བ་ལ་ནི་དེ༌[^494]མི་སྦྱིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དྲུག་པོ༌[^495]དེ་མི་སྦྱིན་པའོ། །

[Block 556]
ཁྱིམ་པ་ལ་སོགས་པ་རྣམས་ལ་ནད་གཡོག་གིས་བྱ་བ་ཉིད་ཀྱི་ཕྱིར་སྤྱི་ལ་བྱ་བར་བཀག་པའོ། །

[Block 557]
འདིར་གཞུང་ནི། བཙུན་པ་བྲོ་གཡོག་ཁྱིམ་པ་ལགས་ན། དེ་ལ་བྲོ་གཡོག་གི་ཆོས་གོས་བརྩལ་བར་བགྱིའམ། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཅུང་ཟད་ཀྱང་སྦྱིན་པར་མི་བྱ་སྟེ། དེ་བཞིན༌[^496]དུ་ནད་གཡོག་མ་དང་། དགེ་སློབ༌[^497]མ་དང་། དགེ་ཚུལ་མ་ལ་ཡང༌[^498]སྦྱིན་ནོ་ཞེས་རྒྱ་ཆེར་གསུངས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 558]
གངགང་ཡང༌[^499]མཚན་མི་མཐུན་པ་དག་འབའ་ཞིག་ཡོད་ན་མཚན་མཐུན་པ་དག་མེད་པ་དེར་མཚན་མི་མཐུན་པ་དག་ལ་ཡང་སྦྱིན་པར་བྱ་བ་ཉིད་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 559]
དེ་ལ་མཚན་མི་མཐུན་པ་དག་ལ་འོས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 560]
གཞན་དུ་གནས་པར་ཁས་བླངས་པ་ལ་མི་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ནད་གཡོག་གནས༌[^500]གཞན་དུ་གནས་པར་ཁས་བླངས་པ་ལ་ཡོ་བྱད་དྲུག་པོ་དག་མི་སྦྱིན་པར་མི་བྱ་ཞིང་སྦྱིན་པར་བྱ་སྟེ། འདི་དང་འདི་ལས་གཞན་དུ་གནས་པར་ཁས་བླངས་པ་ནི་མི་སྦྱིན་པའི་རྒྱུ་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 561]
འདི་ལ་བསྙེན་པར་མ་རྫོགས་པ་ནི་ཐམས་ཅད་དབང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སོ་སོར༌[^501]སྐལ་བའི་ཆ་འོས་པ་ཉིད་ཡིན་པའོ། །

[Block 562]
འདི་ཡང་འདི་ལ་སུམ་ཆ་འབྲི་བ་ལྟ་བུ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 563]
ནད་པས་སྨྲས་པས་བྱིན་པ་ཕྲི་བ་ཡང་ཇི་སྐད་སྨྲས་པ་བཞིན་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། ནད་པས་སྦྱིན་པ་སྨྲས་པ་ལ་གང་དེ་ལ་སྨྲས་པ་དེ་དེས་ཕྲི་བར་གྱུར་ཀྱང་ཇི་ལྟར་དེས་དེ༌[^502]ལ་སྨྲས་པ་དེ་ལྟར་ཁོ་ན་བཞིན་བྱ་དགོས་པར་རིག་པར་བྱའོ། །

[Block 564]
འདིར་གཞུང་ནི། འདུལ་བྱེད་དག་ལས་སྔར་ནད་པས་སྦྱིན་པ་དེ་བདག་ཉིད་ཤི་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དང་། དེ་ལྟ་བས་ན་འདི་ལ་མི་སྦྱིན་པ་མ་ཡིན་ནོ། །

[Block 565]
ནད་གཡོག་གིས་ཕྱིར་ཕྲི་ཡང་གང་ཞིག་དེས་སྨྲས་པ། གཞན་གྱི་ཕྱིར་ཡང་འདི་ལ་བྱེ་བྲག་མེད་པས་རྣམ་པར་གཞག་པའོ་ཞེས་གསུངས་པ་ཙམ་བསྡུས་པ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
