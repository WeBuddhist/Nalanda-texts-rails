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
[Block 3326]
དགེ་སློང་ཞེས་བྱ་བ་འདི་ལ་འདིར་དགེ་སློང་རྣམས་ཀྱིས་ཞེས་བྱ་བ་ཡོངས་སུ་གྱུར་པ་ལ་བྱེད་པ་པོ་ཉིད་ཀྱི་ཚིག་གིས་འབྲེལ་ཏོ་སྙམ་དུ་ཤུགས་ཀྱིས་རྟོགས་པའོ། །

[Block 3327]
མི་བྱེད་ན་འདུག་པའི་ཕྱིར་ཞུས་ཏེ་དེ་ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། མི་བྱེད་ན་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་སྟན་ལ་འདུག་པར་མ་བྱས་པ་ལ། འདི་ལ་དེས་འདུག་པ་ལ་ངེས་པར་སྦྱར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3328]
མཐོང་མ་ཐག་ཏུ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དེའོ། །

[Block 3329]
དེ་ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གིས་སོ། །

[Block 3330]
ཞུས་ཏེ་ཞེས་བྱ་བ་ནི་གནང་ན་སྟན་དེ་ལ་འདུག་པར་བྱ་སྟེ། དགེ་སློང་མས་ཞེས་བྱ་བའི་དོན་གྱིས་རྟོགས་པར་བྱའོ། །

[Block 3331]
བླ་མར་གྱུར་པ་ལ་བརྙས་ཐབས་བྱེད་པའི་ལྟུང་བྱེད་གསུམ་མོ།། །།

[Block 3332]
གང་ལ་འཁྲུག་ལང་ཡལ་བར་དོར་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མ་རྣམས་ཀྱིས་རྩོད་པ་མཐུ་ཡོད་བཞིན་དུ་ཉེ་བར་ཞི་བར་མི་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉེ་བར་ཞི་བར༌[^2175]བྱ་བའི་མཐུ་ཡོད་བཞིན་དུ་རྩོད་པ་ཉེ་བར་ཞི་བར་མི་བྱེད་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདི་བསྒྲུབ་པར་འགྱུར་རོ། །

[Block 3333]
གལ་ཏེ་གང་གི་ཚེ་དེའི་འོག་ཏུ་མ་བྲལ་བ་ཉིད་ལ་དེའི་སེམས་ལ་དེ་དང་འབྲེལ་པ་རྣམ་པར་ངེས་པའམ། བསམ་པ་བཏང་ནས་ཡང་བསམ་པ་གཞན་བསྐྱེད་པ་ལྟུང་བ་ཐམས་ཅད་ཀྱི་བསམ་པ་མ་བཏང་བ་ཉིད་ལ། ལྟུང་བ་གཅིག་པ་ཉིད་ཀྱི༌[^2176]བསམ་པ་དོར་ནས་སླར་ཡང་མངོན་པར་བསྟེན་པ༌[^2177]ལ་ལྟུང་བྱེད་གཞན་བསྐྱེད་པར་འགྱུར་རོ། །

[Block 3334]
འཁྲུག་ལོང་ཡལ་བར་དོར་བའི་ལྟུང་བྱེད་དོ། །

[Block 3335]
གང་ལ་བློ་མཐུན་པར་མི་བྱེད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཞག་ལོན་པའི་མི་འདུན་པ་སྦྱིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉི་མ་སྔ་མ་གཞན་ལ་འདུན་པ་ཕུལ་བ་དེ་ཉིད་དུ་ཡང་ཡོད་པས། འདུན་པ་སྔ་མ་དེ་གང་གི༌[^2178]ཕྱིར་བདག་གིས་དང་དུ་མ་བླངས་པས་ཡང་ཅིའི་ཕྱིར། ད་ལྟར་འདུན་པ་ཕུལ་བ་དེ་བདག་གིས་མ་བླངས་སོ་ཞེས་ཟེར་ཞིང་ཞག་ལོན༌[^2179]པའི་འདུན་པ་སྦྱིན་པའོ། །

[Block 3336]
ཕྱིས་ཉི་མ་གཞན་ལ་འདུན་པ་སྦྱིན་པ་ལ་ཞེས་བྱ་བ་འདིས་བྱེ་བྲག་པ་ཉིད་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 3337]
ལས་གང་ལ་སྦྱིན་པ་ཉིད་དེ། དེའི་ཚེ་ལས་མ་བྱས་པ་ཉིད་ལ་མདུན་དུ་དེའི་ལས་བྱ་བའི་དོན་སླར་བསྡུས་པའི་རྣམ་པ་འདི་ལ་གོ་སྐབས་སོ། །

[Block 3338]
དེ་ལྟར་འདིར་གླེང་གཞི་ནི་སྦོམ་དགའ་མོ་ལ་དགེ་སློང་མ་རྣམས་ཀྱིས་འཕགས་མ་དགེ་སློང་མའི་དགེ་འདུན་འཚོགས༌[^2180]ཀྱིས་ཚུར་ཤོག་ཅིག་ཅེས་བྱས་པ་དང་། དེས་སྨྲས་པ་ཆོས་བཞིན་དུ་བྱེད་པའི་ལས་ལ་འདུན་པ་འབུལ་ལོ། །

[Block 3339]
བྱ་བ་དེ་ཡང་མ་བྱས་སོ། །

[Block 3340]
ཡང་ཕྱི་དེ་ཉིན་ཕར་དགེ་སློང་མའི་དགེ་འདུན་འདུས་ནས་སྦོམ་དགའ་མོ་ལ་སྦྲན་པ་དང་། དེ་འོང་དུ་མ་བཏུབ་ནས་དགེ་སྐོས་མོས་ཅི་འཕགས་མ་འདུན་པ་འབུལ་མི་འདོད་དམ་ཞེས་སྨྲས་པ་དང་། དེས་སྨྲས་པ་ཁོ་མོས་འདུན་པ་ཕུལ་ཟིན་ཏོ། །

[Block 3341]
ནམ་ཕུལ་ཉི་མ་སྔ་མ་ལའོ། །

[Block 3342]
འཕགས་མས་ཞག་ལོན་པའི་འདུན་པ་འབུལ་དུ་རུང་ངམ། དེས་སྨྲས་པ་ཆག་གམ་རྡུལ་ཏམ༌[^2181]ཅི་ཉེས༌[^2182]ཞེས་ཟེར་བ་ལས་བཅས་པ་ཡིན་ནོ། །

[Block 3343]
བློ་མཐུན་པར་མི་བྱེད་པའི་ལྟུང་བྱེད་དོ། །

[Block 3344]
བློ་མཐུན་པ་ལ་རྩེ་བར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར། ལྕི་བའི་ཆོས་ལ་འདས་པའི་ལྟུང་བྱེད་གསུམ་དང་། ལྕི་བའི་ཆོས་དང་འབྲེལ་པའི་ལྟུང་བྱེད་ཆོས་ལས་འདས་པ་ཞེས་བྱ་བའི་ལྟུང་བྱེད་འོག་མ་བཞི་པོ་སྟེ། དེ་རྣམས་ཀྱི་དང་པོ་ནི་ཟླ་བ་ཕྱེད་ཕྱེད་ཅིང་དགེ་སློང་རྣམས་ལས་གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་དག་ཉམས་སུ་མྱོང་བར་མི་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་གི་ཉིན་མོ་གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་ཉམས་སུ་མྱོང་བར་བྱས་པ་ཉིད་དོ། །

[Block 3345]
དེ་བས་ན་གསོ་སྦྱོང་གི་ཉིན་མོ་ལས་འདས་ན་ཁ་ན་མ་ཐོ་བ་འདི་སྐྱེད༌[^2183]པའོ། །

[Block 3346]
རྐྱེན་བྱུང་ན་སོ་སོར་ཉམས་སུ་མྱོང་བར་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 3347]
ཉམས་སུ་མྱོང་བ་ནི་ལས་ཉིད་མ་ཡིན་པ་མ་ཡིན་ནོ། །

[Block 3348]
གསོ་སྦྱོང་གི་དུས་ཀྱང་འདིའི་དུས་སོ། །

[Block 3349]
དེ་ལྟ་བས་ན་འདིར་ཉི་མ་འཆར་བའི་དུས་ལས་འདའ་བར་བྱེད་ན་འདས་པ་ཞེས་བྱ་བ་འདི་ལ་ན་སྨད་པ་འཇུག་གོ། །

[Block 3350]
[^2184]

[Block 3351]
གཉིས་པ་ནི་གང་ལ་དགེ་སློང་དག་མེད་པར་གསོ་སྦྱོང་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྟེ། དགེ་སློང་མའི་དགེ་འདུན་གྱིས་སྔར་དགེ་འདུན་ལས་འདུན་པའི་གསོ་སྦྱོང་བླངས་ནས་འཚོགས་པ༌[^2185]སྒྲུབ་པར༌[^2186]མི་བྱེད་པ་དེ་ནི་འདིར་གསོ་སྦྱོང་བྱེད་པ་ལ་ཡན་ལག་ཏུ་རྣམ་པར་གཞག་པ་དེ་བས་ན༌[^2187]ཚོགས་པ་སྒྲུབ་པར་མི་བྱེད་པ་དེ་ནི་འདིར་དགེ་སློང་དག་མེད་པར་གསོ་སྦྱོང་བྱེད་པར་རིག་པར་བྱའོ། །

[Block 3352]
འདི་ན༌[^2188]འདིར་ལྕི་བའི་ཆོས་དང་འབྲེལ་པའི་ཆོས་ལས་འདས་པའི་ཁ་ན་མ་ཐོ་བའོ། །

[Block 3353]
འདིར་གླེང་གཞི་ལས་དགེ་སློང་མ་ཁྱོད་ཀྱིས་དགེ་སློང་དག་མེད་པར་གསོ་སྦྱོང་དག་བྱས་པ་བདེན་ནམ་ཞེས་གསུངས་པ་དང་ཡང་དགེ་སློང་མ་གང་དགེ་སློང་མེད་པར་གསོ་སྦྱོང་བྱེད་ན་ལྟུང་བྱེད་དོ་ཞེས་མདོ་ལས་གསུངས་པ་ཡིན་ནོ། །

[Block 3354]
དགེ་སློང་མའི་ཚིག་འདི་ནི་རིགས་ཀྱི་དགོངས་པ་ཅན་ཡིན་ནོ། །

[Block 3355]
གསུམ་པ་ནི་གང་ལ་དགེ་སློང་མེད་པའི་གནས་སུ་དབྱར་གནས་པར༌[^2189]ཁས་ལེན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མེད༌[^2190]པའི་གནས་ཞེས་བྱ་བ༌[^2191]ནི། གང་ལ་ལས་རྣམས་ཐམས་ཅད་མི་བྱེད་པའོ་ཞེས་བྱ་བའོ།

[Block 3356]
[^2192] །འདིའི་རྣམ་པར་འབྱེད་པ་ནི་གང་ན་ལས་གཅིག་ཀྱང་མི་ཤེས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3357]
གནས་གང་ན་རང་བཞིན་དུ་གནས་པའི་དགེ་སློང་བཞི་ཡན་ཆད་གནས་ཤིང་ལས་བྱེད་པ་མེད་པ་དེ་ནི་དེ་ལས་འདིས་བྱས་སོ།[^2193] །འདིའི་དོན་ནི་གསོ་སྦྱོང་དང་། གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་དག་ལས་མ་ཉམས་པ་དང་། ལྕི་བའི་ཆོས་རྣམས་བཟུང་བ་ཉིད་དོ། །

[Block 3358]
དེ་ལྟ་བུར་གྱུར་པའི་དགེ་སློང་རྣམས་ལ་འདི་ཙམ་ཉིད་ལ་གཉིས་པོ་འདི་བསྒྲུབ་པ་ཞེས་བྱ་བ་འདི་ཡོངས་སུ་བཟུང་བའོ། །

[Block 3359]
གང་ཞིག་དབྱར་གནས་པར༌[^2194]གྱུར་པ་ལ་གནས་པ་མི་རིགས་པ་དང་། བུད་མེད་ཀྱི་ཚོགས་ལ་བརྟེན་པ་མེད་པས་འདུག་པ་མི་རིགས་པ་ཞེས་བྱ་བ་འདིར་ལྕི་བའི་ཆོས་བཟུང་བ་ལ་ཀུན་ནས་བརྟེན་པ་འདི་ནི་གནས་ཡིན་ནོ། །

[Block 3360]
བཞི་པ་ནི་གང་ལ་དབྱར་གནས་པས་གཉིས་ཀའི་དགེ་འདུན་ལ་གནས་གསུམ་གྱིས་དགག་དབྱེ་མི་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགག་དབྱེའི་ཉིན་མོ་ལས་འདས་པ་ལས་ཁ་ན་མ་ཐོ་བ་ནི་གསོ་སྦྱོང་དང་འདྲའོ། །

[Block 3361]
ལྕི་བའི་ཆོས་ལས་འདས་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 3362]
ད་འདི་མན་ཆད་ནི་གཞན་ལ་གནོད་པར་བྱེད་པའི་ལྟུང་བྱེད་གསུམ་སྟེ། [^2195]དེ་རྣམས་ཀྱི་དང་པོ་ནི་གང་ཞེ་ན་དབུལ་པོ་སྲ་བརྐྱང་སྦྱོར་དུ་བཅུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་འདིར་སྦྱིན་པ་དང་སྦྱོར་དུ་འཇུག་པ་དང་། བསོད་ནམས་ལྷག་པར་སྦྱོང་པའི་སྒོ་ནས་གཉིས་ཀའི་དོན་དུ་སྲ་བརྐྱང་སྦྱོར་དུ་འཇུག་ན་བྱས་སམ་བྱེད་དུ་འཇུག་ན་ཐོབ༌[^2196]ན་དངོས་གཞིའོ། །

[Block 3363]
མདུན་རོལ་དུ་ནི་ཉེས་བྱས་སོ། །

[Block 3364]
གཞན་ལ་ཡང་ཆོས་གོས་གཏན་པའི་ཟོང་ཙམ་དགེ་འདུན་གྱི་དོན་དུ་དབུལ་པོ་སྦྱོར་དུ་བཅུག་ན༌[^2197]ཡང་ལྟུང་བྱེད་དོ།[^2198] །ཆོས་གོས་གཏན་པ་ཞེས་བྱ་བ་ནི་འདིར་དཔེ་ཙམ་དུ་རྣམ་པར་གནས་པར་གྱུར་པར་རིག་པར༌[^2199]བྱ་སྟེ་མ་ཆོག་པ་ལ་ནི་ཉེས་པས༌[^2200]སོ། །

[Block 3365]
དུ་མ་སྦྱོར་དུ་བཅུག་པ་ལ་ནི་རེ་རེ་ལས་ཁ་ན་མ་ཐོ་བ་རེ་རེར་འགྱུར་རོ། །
--- END BLOCKS ---
