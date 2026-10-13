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
[Block 701]
དེ་ལས་མཐའ་གཉིས་སྤངས་ནས་ཞུགས་པའི་ལན༌[^537]འདི་ཡང་ཕྱིན་ཅི་ལོག་ཉིད་དུ་འགྱུར་ལ། གང་གི་ཚེ་རིགས་པས་དཔྱད་ན་དངོས་པོ་རྣམ་པ་ཐམས་ཅད་དུ་མེད་ན་དེའི་ཚེ་དེའི་ཡུལ་རྟག་པ་དང་ཆད་པར་ཡོངས་སུ་བརྟགས་པས༌[^538]ཡང་དག་པའི་ལྟ་བ་མ་ཡིན་ནོ་ཞེས་འཐད་དོ། །

[Block 702]
གང་ཡང་ཡང་དག་པའི་ལྟ་བ་མ་ཡིན་པ་དེ་ནི་ངེས་པར་སྤང་བར་བྱ་ལ། དེ་སྤོང་བའི་ཐབས་ཀྱང་རང་བཞིན་ཁས་མ་བླངས་པ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། དངོས་པོ་བཀག་པས་མྱ་ངན་ལས་འདས་པར་འགྲོ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིར་ཐར་པར༌[^539]འདོད་པ་རྣམས་ཀྱིས་ཁས་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 703]
འདིར་སྨྲས་པ། བདག་དང་བདག་གི་བའི་རྣམ་པ་ནི་འཇིག་ཚོགས་སུ་ལྟ་བ་ལ། གང་གི་ཚེ་བདག༌[^540]ཉིད་དུ་དམིགས་པ་དེ་ཉིད་རྟག་པ་དང་ཆད་པའི་མཐར་ཡོངས་སུ་བརྟགས་པ་ལས་མཐར་འཛིན་པའི་ལྟ་བ་སྐྱེད་ལ། དེ་ཡང་སྤང་བྱ་ལ་ཆོས་ཙམ་ནི་རྟག་པ་དང་ཆད་པའི་ལྟ་བར་མི་དམིགས་སོ་ཞེས་བྱ་སྟེ། དེས་ན་གལ་ཏེ་ཡང་ཕུང་པོ་རྣམས་མྱ་ངན་ལས་འདས་ནས་སླར་མི་འཇུག་ན། དེ་ལྟ་ན་ཡང་ལྟ་བ་དེ་ནི་ཆད་པར་ལྟ་བ་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 704]
འོ་ན་འཇིག་ཚོགས་སུ་ལྟ་བ་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་ལ་བདག་དང་བདག་གི་བའི་རྣམ་པར་དམིགས༌[^541]ལ། དེ་ལྟ་ན་ཡང་མུ་སྟེགས་བྱེད་ཀྱིས་བརྟགས་པའི་བདག་གི་རྣམ་པར་དམིགས་བཞིན་པ་ན་དེའི་དབང་གིས་འདུ་བྱེད་རྣམས་ལ་ཡང་བདག་གི་བའི་རྣམ་པར་དམིགས་པས་འཇུག་གོ། །

[Block 705]
འོ་ན་འདི་ཡང་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་ལ་དམིགས་པར་འགྱུར་གྱི། ཁྱད་པར་ནི་འདི་དག་སྟེ། གང་དུ་དེ་དག་ལ་བདག་དང་བདག་གི་བའི་རྣམ་པར་དམིགས་ནས་ཡོངས་སུ་འཛིན་ཅིང་དེ་ལས་ཀྱང་མཐར་འཛིན་པར་ལྟ་བས་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་དེ་ཉིད་ལ་རྟག་པ་དང་ཆད་པའི་རྣམ་པས་དམིགས་སོ་ཞེས་བྱའོ། །

[Block 706]
གལ་ཏེ་ཡང་འཇིག་ཚོགས་སུ་ལྟ་བ་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་ལ་དམིགས་སོ་ཞེས་བྱ་བ། དེ་ལྟར་ན་ཡང་འདི་དེའི་རང་བཞིན༌[^542]མི་དམིགས་ལ། འོན་ཀྱང་དེ་དག་ལས༌[^543]བདག་ཏུ་སྒྲོ་བཏགས་ནས་དམིགས་ཏེ། འདི་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་ལ་སྒྲོ་བཏགས་པའོ་ཞེས་བྱའོ། །

[Block 707]
དགེ་སློང༌[^544]ངམ་བྲམ་ཟེ་གང་ཅུང་ཟད་བདག་གོ་ཞེས་ཡང་དག་པར་རྗེས་སུ་ལྟ་བ༌[^545]ལས་ཡང་དག་པར་རྗེས་སུ་མཐོང་བ་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་འདི་ཉིད་མཐོང་ངོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ། དེ་ལས་ཐ་དད་པའི་ནང་གི་བྱེད་པའི་སྐྱེས་བུ་ཉིད་མ་གྲུབ་བོ་ཞེས་བྱ་བའི་དོན་དུའོ། །

[Block 708]
དེའི་ཕྱིར་འཇིག་ཚོགས་སུ་ལྟ་བས་བདག་ཁོ་ན་ལ་དམིགས་སོ། །

[Block 709]
གང་ཡང་བདག་གི་དབང་དུ་གྱུར་པའི་ཕྱིར། འདུ་བྱེད་རྣམས་ལ་བདག་གི་བའི་རྣམ་པར་དམིགས་ལ། དེའི་ཕྱིར་མཐར་འཛིན་པར་ལྟ་བ་ཡང་རྟག་པ་དང་ཆད་པའི་རྣམ་པས་འཇུག་བཞིན་པ་ན། བདག་དང་བདག་གི་བ་ལ་དམིགས་ཀྱི་གཞན་དུ་མ་ཡིན་ནོ། །

[Block 710]
དེ་ཉིད་ཀྱིས་ན་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ། ཀུན་དགའ་བོ་བདག་ཡོད་དོ་ཞེ་ན་ཕ་རོལ་པོའི་རྟག་པ་ཞེས་བྱ་ལ། བདག་མེད་དོ་ཞེ་ན་ཕ་རོལ་པོའི་ཆད་པར་རོ་ཞེས་སོ། །

[Block 711]
འདིར་སྨྲས་པ། གལ་ཏེ་འགའ་ཞིག་ཆོས་ཙམ་ལ་རྟག་པ་ཞེས་རྟོགས་ན། ཅི་དེ་ནི་རྟག་པར་ལྟ་བར་འགྱུར་རམ་འོན་ཏེ་མ་ཡིན། །གལ་ཏེ་རེ་ཞིག་རྟག་པར་ལྟ་བར་དེ་འདོད་ན། དེ་མི་རུང་སྟེ། འཇིག་ཚོགས་སུ་ལྟ་བ་ཆོས་ཙམ་ལ་དམིགས་ཤིང་གང་ལ་མཐར་འཛིན་པར་ལྟ་བ་འཇུག་པ་ནི་མེད་ལ། མཐར་འཛིན་པར་ལྟ་བ་སྤངས་ནས་གཞན་རྟག་པའི་རྣམ་པར་འཇུག་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 712]
ལྟ་བ་ཉིད་མེད་ན་ཡང་རྟག་པས་ཆོས་ཙམ་མཐོང་བ་ཁ་ན་མ་ཐོ་བ་མེད་པར་འགྱུར་རོ། །

[Block 713]
འདུས་བྱས་ཐམས་ཅད་མི་རྟག་ཅེས་བྱ་བའི་ཚིག་ལས་རྟག་པ་ཉིད་དུ་ལྟ་བ་ཕྱིན་ཅི་ལོག་པའོ་ཞེ་ན། གལ་ཏེ་དེར་འཛིན་པ་ཕྱིན་ཅི་ལོག་ན། ཇི་ལྟར་འདི་ཉོན་མོངས་པའི་དམིགས་པར་འགྱུར། ཇི་སྲིད་དུ་འདོད་ཆགས་པ་དེ་སྲིད་དུ་སྡུག་པའི་རྣམ་པར་དམིགས་པར་བྱེད།[^546] ཞེ་སྡང་མི་སྡུག་པའི་རྣམ་པར་རོ། །

[Block 714]
ང་རྒྱལ་ཁེངས་པའི་རྣམ་པར་རོ། །

[Block 715]
མི་ཤེས་པའི་རྣམ་པར་ནི་མ་རིག་པའོ། །

[Block 716]
ཡིད་གཉིས་ཀྱི་རྣམ་པར་ནི་ཐེ་ཚོམ་མོ། །

[Block 717]
འཇིག་ཚོགས་སུ་ལྟ་བ་ནི་བདག་དང་བདག་གི་བར་འཇུག་པའོ། །

[Block 718]
ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་ནི་དམན་པ་ལ་མཆོག་གི་རྣམ་པར་རོ། །

[Block 719]
ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ནི་རྒྱུ་མེད་པ་དང་ལམ་མ་ཡིན་པ་ལ་རྒྱུ་དང་ལམ་གྱི་རྣམ་པར་འཇུག་པའོ་ཞེས་བྱ་བས་སོ། །

[Block 720]
རེ་ཞིག་དེ་དག་རྟག་པའི་རྣམ་པར་མི་དམིགས་སོ་ཞེས་བྱ་སྟེ། སུ་ཞིག་དེའི་རྣམ་པར་དམིགས་པ༌[^547]ཡོད། ཡང་ན་མཐར་འཛིན་པའི་ལྟ་བའི་ཞེས་ཡོངས་སུ་རྟོག་ན་དེ་ལྟ་ན་འདི་ལྟར་བདག་གི་བའི་རྣམ་པ་མ་ཡིན་པའི་ཆོས་ཙམ་ལ་དམིགས་པ་ཡང་མཐར་འཛིན་པར་ལྟ་བའོ་ཞེས་ཡོངས་སུ་ཤེས་སོ། །

[Block 721]
གལ་ཏེ་ཡང་དེ་ནི་དེ་ལྟར༌[^548]ན་དེའི་ཚེ་མྱ་ངན་ལས་འདས་པའི་ཆོས་ཙམ་ཡང་ཆད་པའི་ཕྱིར་ཆད་པར་ལྟ་བ་སྟེ། ཅི་ལྟར་མཐར་འཛིན་པར་ལྟ་བར་མི་འགྱུར། གཞན་ཡང་དེའི་རྣམ་པ་མ་ཡིན་པའི་ཆོས་ཙམ་ལ་དེའི་རྣམ་པར་སྒྲོ་འདོགས་པས་ལོག་པར་རྟོགས་པ་ལས་ཉོན་མོངས་པ་རྣམས་འཇུག་པར་འགྱུར་རོ། །

[Block 722]
དེ་ལ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དངོས་པོ་རང་བཞིན་མེད་པ་སྟེ་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 723]
དེ་དག་ལ་རང་བཞིན་དུ་གང་ཞིག་ཁོང་དུ་ཆུད་པ་དེ་ནི་གཙོ་བོ་ཕྱིན་ཅི་ལོག་གི་བདག་པོ་མ་རིག་པ་ཞེས་བརྗོད་དོ། །

[Block 724]
གཞན་དུ་ན་གལ་ཏེ་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ཡོད་བཞིན༌[^549]པའི་ངོ་བོར་གྱུར་ན། དེ་ངེས་པར་དེ་ཁོ་ན་ཉིད་ལ་དམིགས་པའི་འཕགས་པའི་ལམ་གྱིས་དམིགས་པར་འགྱུར་ལ། དངོས་པོའི་རང་གི་མཚན་ཉིད་ལ་དམིགས་པའི་རྣམ་པ་འཕགས་པའི་ལམ་ལ་མི་སྲིད་ལ། བཅུ་དྲུག་ལས་གཞན་དྲི་མེད་རྣམ་པ་མེད། །ཅེས༌[^550]བསྟན་བཅོས༌[^551]ལས་སོ། །

[Block 725]
དེའི་ཕྱིར་མ་རིག་པས་ཀུན་ཏུ་བརྟགས་པའི་དངོས་པོ་རྣམས་ཡོད་པ་ཉིད་དེ་ཁོ་ན་ཉིད་མ་ཡིན་ནོ་ཞེས་སོ། །

[Block 726]
དེ་ལྟར་དངོས་པོའི་རྣམ་པར་འཇུག་པས་དེ་ཁོ་ན་ཉིད་མ་རྟོགས་པའི་ཕྱིར་དེ་ཁོ་ན་ཉིད་མ་ཤེས་པར་འཇུག་གོ་ཞེས་རྣམ་པར་གཞག་གོ། །

[Block 727]
མ་རིག་པས་ཀུན་དུ་བརྟགས་པའི་དངོས་པོ་ལ་འདོད་ཆགས་ཀྱིས་སྡུག་པའི་རྣམ་པར་དམིགས་ལ། ཞེ་སྡང་གིས་མི་སྡུག་པའི་རྣམ་པར་རོ། །

[Block 728]
ང་རྒྱལ་གྱིས་ཁེངས་པའི་རྣམ་པར་རོ། །

[Block 729]
ཐེ་ཚོམ་གྱིས་ཡིད་གཉིས་སུའོ། །

[Block 730]
འཇིག་ཚོགས་ཀྱིས་བདག་དང་བདག་གི་བའི་རྣམ་པར་རོ། །

[Block 731]
མཐར་འཛིན་གྱིས་རྟག་པ་དང་ཆད་པའི་རྣམ་པར་རོ། །

[Block 732]
ལོག་པར་ལྟ་བས་མེད་པའི་རྣམ་པར་རོ། །

[Block 733]
ལྟ་བ་མཆོག་ཏུ་འཛིན་པས་དམན་པ་ལ་མཆོག་གི་རྣམ་པར་རོ། །

[Block 734]
ལམ་གྱི་རྣམ་པས་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པའོ་ཞེས་དེ་ལྟར་ཉོན་མོངས་པ་ཐམས་ཅད་མ་རིག་པས་ཡོངས་སུ་བརྟག་པའི༌[^552]ཕྱིན་ཅི་ལོག་གི་དངོས་པོ་ཉིད་ལ་དེ་དག་ཞེན་པས་སྒྲོ་བཏགས་ནས་འཇུག་ལ། དེ་ཉིད་ཀྱིས་ན། རྨོངས་མེད་ཅིག་ཤོས་སྐྱེ་བ་མེད། །ཅེས་བྱ་བས་མ་རིག་པའི་རྒྱུ་ཅན་དུ་ཉོན་མོངས་པ་ཐམས་ཅད་རྣམ་པར་གཞག་གོ། །

[Block 735]
རྨོངས་པ་སྤངས་པ་ལས་ཐམས་ཅད་མ་ལུས་པར་སྤོང་གི་གཞན་དུ་མ་ཡིན་ཏེ། དེ་དག་མ་རིག་པ་དང་ལྷན་ཅིག་འབྲེལ་བའི་ཕྱིར། ཇི་སྐད་དུ་འཕགས་པ་ལྷས།

[Block 736]
མ་རིག་ཀུན་དུ་གནས་པ་ནི། །ཇི་ལྟར་ལུས་ལ་ལུས་དབང་གིས། །

[Block 737]
དེ་ཕྱིར་ཀུན་ཀྱང་རྨོངས་པ་ཡིས།[^553] །ཉོན་མོངས་པས་དེ་འདིར་བསྣུན་ནོ། །ཞེས་བཤད་དོ། །

[Block 738]
གང་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ་གསུངས་པ། ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་འདི་ཉིད་ལ་བདག་ཅེས་ཡང་དག་པར་རྗེས་སུ་མཐོང་ངོ་ཞེས་བྱ་བའི་མདོ་དེ་ཡང་མཐར་འཛིན་པར་ལྟ་བ་དང་། འཇིག་ཚོགས་སུ་ལྟ་བ་དང༌[^554]ལྷན་ཅིག་ཏུ་གཞི་གཅིག་ལ་དམིགས་པར་འཐད་དོ་ཞེས་ཤིན་ཏུ་ངེས་པར༌[^555]སྒྲུབ་པའོ། །

[Block 739]
དེ་ལས་ཀྱང་འདི་ཤིན་ཏུ་འཐད་པས་དངོས་པོར་ཡོད་ན་ཡང་དེས་ན་གཉིས༌[^556]ཀ་ཁས་བླང་ངོ་ཞེས་བྱ་བར་འགྱུར་རོ་ཞེས་སོ། །

[Block 740]
འདིར་སྨྲས་པ། གལ་ཏེ་དངོས་པོ་ཡོད་ཀྱང་དེ་ལྟ་ན་ཡང་དེའི་རྟག་པ་དང་མི་རྟག་པ་དག་མེད་པས་ཐེར་ཟུག་པ་དང་རྒྱུན་ཆད་པར་ལྟ་བར་ཐལ་བ་མ་ཡིན་པ་ཇི་ལྟར་ཞེ་ན། གསུངས་པ།
--- END BLOCKS ---
