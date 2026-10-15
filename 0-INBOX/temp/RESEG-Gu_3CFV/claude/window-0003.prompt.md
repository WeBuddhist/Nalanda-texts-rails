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
[Block 106]
ཐམས་ཅད་ཀྱི་ནད་པ་བལྟ་བར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^77]དེའི་ཁང་བུའི་གནས་སུ་ཉེ་བར་འགྲོ་བ་ན་གསར་བུའམ་རྒན་པོ་འགའ་ཞིག་གིས་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 107]
ཅི་འགྲེང་སྟེ་བལྟ་བར་བྱ་བ་འམ་ཞེ་ན་མ་ཡིན་ཏེ་དེའི་ཕྱིར་འདུག་སྟེའོ། །

[Block 108]
དེར་སྟན་ཐོགས་ཏེ་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེར་ཞེས་བྱ་བ་ནི་ནད་པ་ལྟ་བ་ལའོ། །

[Block 109]
ནད་པའི་ནད་གཡོག་གིས༌[^78]དེར་སྟན་དག་བཤམ་པར་བྱའོ། །

[Block 110]
མཁན་པོའམ་སློབ་དཔོན་དགེ་བའི་ཕྱོགས་ལ་འགྲོ་ན་གལ་ཏེ་གཞན་གྱིས༌[^79]དགེ་བའི་ཕྱོགས་མི་འཕེལ་ན་ཕྱི་བཞིན་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^80]གལ་ཏེ་མ་ཡིན་ན་གཞན་དུ་ཞེས་བྱ་བའོ། །

[Block 111]
དེའི་ཕྱི་བཞིན་འགྲོ་བ་མ་གཏོགས་པར་ཀློག་པའམ་གདམས་ངག་གམ་རྗེས་སུ་བསྟན་པ་བརྩམས་པ་ལས་སོ་སོར་ཉེ་བར་འདུག་པར་གྱུར་པ་ལ་འདིར་སློབ་དཔོན་ནམ་མཁན་པོ་སྨོས་པའོ། །

[Block 112]
གལ་ཏེ་མ་ཡིན་ན་གཞན་དུ་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པར་བྱའོ། །

[Block 113]
དེ་བས་གནས་ཀྱི་སློབ་དཔོན་དང་ཀློག་པའི་སློབ་དཔོན་དག་ལས་གཞན་པའི་སློབ་དཔོན་འདིར་སྨོས་པ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 114]
དེའི་ཕྱིར་རང་གི་སྟན་བསྐུར་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཕྱིར་ཞེས་བྱ་བ་ནི་མཁན་པོའམ་སློབ་དཔོན་གྱི་ཕྱིར་རོ། །

[Block 115]
འགྲོ་བ་མ་ཞུས་པར་མི་བསྐུར་རོ་ཞེས་བྱ་བ་ནི། བདག་ཉིད་ཀྱང་ཕྱི་བཞིན་འགྲོ་བར་འགྱུར་བ་འདི་ལྟར་མ་ཞུས་པར་བསྐུར་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 116]
དེ་རང་ཉིད་ཀྱིས་བསྐུར་རོ་ཞེས་བྱ་བ༌[^81]ནི་དེ་ཞེས་བྱ་བ་ནི་རང་ཉིད་ཀྱིས་བསྐུར་བར་བསྟན་ནོ། །

[Block 117]
བླ་གབ༌[^82]མེད་པར་ཆོས་ཉན་པ་ན་རླུང་དང་ཆར་བྱུང་བ་ན་བསྡུ་བར་བྱའོ། །

[Block 118]
རྒན་པོ་རྣམས་ཀྱིས་ནི་རང་གིས་མི་ནུས་ན་གཞོན་ནུ་རྣམས་དང་ལྷན་ཅིག༌[^83]བརྗེ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞོན་ནུ་རྣམས་ཀྱི་གནས་མལ་གང་ཡིན་པ་དེ་ནི་ཡང་བའི་ཕྱིར་རྒན་པོ་རྣམས་ཀྱིས་བསྐུར་བར་བྱའོ། །

[Block 119]
རྒན་པོ་རྣམས་ཀྱི་ནི་ལྕི་བ་ཉིད་ཀྱི༌[^84]ཕྱིར་གཞོན་ནུ་རྣམས་ཀྱིས་བསྐུར་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 120]
མཐུན་པ་དང་མཐུན་པར་གཞག་པར་བྱའོ་ཞེས་བྱ༌[^85]བ་ནི་གང་གིས་གང་མཐུན་པ་དང་མཐུན་པ༌[^86]དེ་ཉིད་དང་ལྷན་ཅིག་ཏུ་དེ་གཞག་པར་བྱའི་མི་མཐུན་པ་དང་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 121]
གཙུག་ལག་ཁང་གཞན་དུ་གདན་ཆ་དང་རྫས་བརྙན་བསྐུར་བར་བྱའོ་ཞེས་བྱ་བ་ལ་དང་གི་སྒྲ་ནི་བརྙན་བསྐུར་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་བའི་དོན་དུའོ། །

[Block 122]
འདིར་རྫས་ནི་མཆོད་པའི་དབང་དུ་བྱས་ཏེ་བལྟ་བར་བྱའོ། །

[Block 123]
ཅི་ཞིག་ངེས་པ་ཉིད་དུ་བསྐུར་བར་བྱའམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་གལ་ཏེ་ཆར་འབབ་པ་དང་འབབ་དུ་དོགས་པ་མེད་ནའོ། །

[Block 124]
གལ་ཏེ་ལམ་ཁར་རླུང་དང་ཆར་བྱུང་ན་ཤིང་ལྗོན་པའམ་རྩིག་དྲུང་དུ་བཅེར༌[^87]བར་བྱའོ་ཞེས་སྨོས་ཏེ། རྩིག་པའི་ཞེས་བྱ་བ་ནི་དྲུང་དུའོ། །

[Block 125]
རྫས་ངན་པ་གཅིག་གིས་གཡོགས་པར༌[^88]བྱའོ། །

[Block 126]
གཙུག་ལག་ཁང་དུ་ཕྱིན་ནས་རྫས་རྣམས་ནི་བསྐམ་པར་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་ཁྱིམ་བདག་གཅིག་ལ་གཙུག་ལག་ཁང་གཉིས་ཡོད་དེ། དགོན་པ་པ་དང་གྲོང་མཐའ་པ་སྟེ། དགེ་སློང་དགོན་པ་པ་རྣམས་ཀྱིས་གྲོང་མཐའ་པའི་གཙུག་ལག་ཁང་ནས་གོས་དག་དང་གནས་མལ་གཡར་བ་དང་། དགེ་སློང་གྲོང་མཐའ་པ་དག་གིས་མ་སྟེར་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་བརྙན་པར་བྱའོ། །

[Block 127]
ཁ་དོག་སྣ་ཚོགས་པའི་གོས་རྣམས་ནི་ཆར་བབ་ན་ཉམས་པར་འགྱུར་རོ། །

[Block 128]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གལ་ཏེ་ཆར་པ་འབབ་པའམ་འབབ་ཏུ་དོགས་ན་བརྙན༌[^89]པར་མི་བྱའོ། །

[Block 129]
གལ་ཏེ་ལམ་ཀར་ཆར་འབབ་ན་ཤིང་ལྗོན་པའི་དྲུང་དུ་གནས་པར་བྱའོ། །

[Block 130]
གཙུག་ལག་ཁང་དུ་སོང་ནས་གོས་རྣམས་བསྐམ་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 131]
མེ་ཤོར་རམ་ཆུ་བྱུང་ན་དགེ་འདུན་གྱི་ཡང་གདོན་པར༌[^90]བྱའོ་ཞེས་བྱ་བ་ནི་གནས་མལ་གྱི་ཕྱིར་འདི་བརྗོད་པ་སྟེ། སྐྱེད་པའི༌[^91]དབང་གིས་འདི་ཡང་དག་པར་བསྟེན༌[^92]པའོ། །

[Block 132]
གཞན་ལ་ཡང་ཆོ་ག་འདིས་སྦྱར་བ་སྟེ་དེ་བས་ན་ཁྱད་པར་མེད་པར་ཉེ་བར་བརྟགས་པའོ། །

[Block 133]
རང་གི་ལྷུང་བཟེད་དང་ཆོས་གོས་ཐོན་ཟིན་ནའོ་ཞེས་བྱ་བ་ནི་ཇེ་དང་པོར་རང་གི་ལྷུང་བཟེད་དང་ཆོས་གོས་གདོན་པར་བྱ་ཞིང་དེའི་འོག་ཏུ་དགེ་འདུན་གྱི་ཡང་གདོན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 134]
གང་ཟག་ནི༌[^93]ཕོངས་པར་འགྱུར་གྱི་དགེ་འདུན་ནི་མ་ཡིན་ཞེས་བྱ་བ་བྱས་ནས༌[^94]སོ། །

[Block 135]
བཏོན་ཟིན་པ་བསྲུང་བའི་ཕྱིར་དགེ་སློང་ཆེན་པོ་མི་ནུས་པ་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྟོབས་ཆུང་བ་ཉིད་ཀྱི་ཕྱིར་ལས་གཞན་ལ་མི་སྦྱར་ཞེས་པར་དགོངས་སོ། །

[Block 136]
མི་བཟོད་པ་ཉིད་དུ་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། མེ་དང་ཆུ་དག་མི་བཟོད་པ་ཉིད་ལ་གདོན་པའི་ཆེད་དུ་འཇུག་པར༌[^95]མི་བྱའོ། །

[Block 137]
གནས་མལ་གྱི་ལྟུང་བྱེད་དོ།། །།

[Block 138]
ཁྱིམ་གཞན་དུ་གདིང་བར་བྱས་པ་ཁྱིམ་བདག་ལ་དྲིས་པ་དེ་དོར་བར་བྱའོ་ཞེས་བྱ་བ་ལ་བྱས་པ་ཞེས་བྱ་བ་ནི་རང་གིས་སམ་བསྐོས་པས་སོ། །

[Block 139]
དགོན་པར་ཡང་ན་སློང་བར་བྱའོ་ཞེས་བྱ་བ་ནི། ཡང་ན་དོར་བར་བྱ་ཞེས་བྱ་བ་ལ་ཡང་ན་ཞེས་བྱ་བའི་སྒྲས་ནི་རྣམ་པར་རྟོག་པའི་དོན་ཏོ། །

[Block 140]
དེ་ནི་མགོའམ་མཇུག་བཟློག་པར་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་སློང་བར་བྱས་པ་ལའོ། །

[Block 141]
འདིར་གཞུང་ནི་དེ་རྣམས་སློང་བར་བྱེད་ན་ཉེས་དམིགས་དེ་ཉིད་དུ་འགྱུར་རོ། །

[Block 142]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། མགོའམ་མཇུག་བཟློག་པ་སློང་བར༌[^96]བྱས་ཏེ། འགྲོ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 143]
གོས་དག་བསྐམ་པའི་ཕྱིར་རྩྭ་གདིང་བ་ཡང་དོར་བར་བྱ་བ་ཉིད་དོ། །

[Block 144]
སློང་བ་ལ་དོར་བ་ཁས་ལེན་ན་སྦྱིན་ནོ་ཞེས་བྱ་བ་ལ། སྦྱིན་པ་ཞེས་བྱ་བ་ནི་གནང་བའི་རྩྭ༌[^97]རྣམས་སོ། །

[Block 145]
འཆག་ས་དག་ཏུ་རྐང་མཐིལ་གཉིས་ལ་རྩུབ་ན་རྩྭ༌[^98]དག་གདིང་བར་བྱའོ། །
--- END BLOCKS ---
