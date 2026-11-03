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
འདི་དཔྱད་པར་བྱ་སྟེ། ལུས་དང་ལྕེའི་དབང་པོ་གཉིས་ཅིག་ཅར་དུ་ཡུལ་དང་ཕྲད་ན་རྣམ་པར་ཤེས་པ་གང་སྔར་སྐྱེ་ཞེ་ན། གང་གི་ཡུལ་ཤས༌[^79]ཆེ་བའོ། །

[Block 177]
ཡུལ་མཉམ་པ་དང་ཕྲད་ན་ནི་ལྕེའི་རྣམ་པར་ཤེས་པ་སྔར་སྐྱེ་སྟེ། ཟ་བར་འདོད་པས་རྒྱུད་གཏད་པའི་ཕྱིར་རོ། །

[Block 178]
དབང་པོ་ལྔ་དང་། དོན་ལྔ་དང་། དེ་དག་ལ་ཇི་ལྟར་འཛིན་པ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 179 [HEADING]]
###### རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ། ^1-1-3-1-4-0

[Block 180]
ད་ནི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་བསྙད་པར་བྱ་བ་དེ་བརྗོད་པར་བྱ་སྟེ།

[Block 181 [VERSE]]
གཡེངས་དང་སེམས་མེད་པ་ཡི་ཡང་། །
དགེ་དང་མི་དགེའི༌[^80]རྗེས་འབྲེལ་གང་། །
འབྱུང་བ་ཆེ་རྣམས་རྒྱུར་བྱས་པ། །
དེ་ནི་རྣམ་རིག་བྱེད་མིན༌[^81]བརྗོད། །

[Block 182]
སེམས་གཡེངས་པ་ཞེས་བྱ་བ་ནི་དེ་ལས་གཞན་པའི་སེམས་ཀྱི་ཡང་ཡིན་པའོ། །

[Block 183]
སེམས་མེད་པའི་ཡང་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་མེད་པ་དང་། འགོག་པའི་སྙོམས་པར་འཇུག་པའི་ཡང་ཡིན་པའོ། །

[Block 184]
ཡང་ཞེས་བྱ་བའི་སྒྲས་ནི་མ་གཡེངས་པ་སེམས་དང་བཅས་པའི་ཡང་ཡིན་ནོ་ཞེས་བྱ་བར་མངོན་ནོ། །

[Block 185]
དགེ་དང་མི་དགེ་ཞེས་བྱ་བ་ནི་དགེ་ལེགས་དང་དགེ་ལེགས་མ་ཡིན་པའོ། །

[Block 186]
རྗེས་འབྲེལ་གང་ཞེས་བྱ་བ་ནི་རྒྱུན་ཏོ། །

[Block 187]
ཐོབ་པའི་རྒྱུན་ཡང་འདི་ལྟ་བུ་ཡོད་པས་བྱེ་བྲག་ཏུ་བྱ་བའི་ཕྱིར། འབྱུང་བ་ཆེ་རྣམས་རྒྱུར་བྱས་པ། །ཞེས་བྱ་བ་བརྗོད་དོ། །

[Block 188]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་རྒྱུར་བྱས་པའི་དོན་ནི་རྒྱུའི་དོན་ཏོ།[^82] །སྐྱེད་པ་ལ་སོགས་པ་རྒྱུའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 189]
དེ་ནི་རྣམ་རིག་བྱེད་མིན་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བའི་སྒྲ་ནི་དེའི་མིང་ཤེས་པར་བྱ་བའི་ཕྱིར་ཏེ། གཟུགས་དང་བྱེད་པའི་རང་བཞིན་ཡིན་ཡང་རྣམ་པར་རིག་བྱེད་བཞིན་དུ་གཞན་དག་ལ་རྣམ་པར་རིག་པར་བྱེད་པ་མ་ཡིན་པས་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའོ། །

[Block 190]
བརྗོད་ཅེས་བྱ་བ་ནི་སློབ་དཔོན་གྱི་ཚིག་ཡིན་པར་སྟོན་པའོ། །

[Block 191]
མདོར་ན་རྣམ་པར་རིག་བྱེད་དང་ཏིང་ངེ་འཛིན་ལས་བྱུང་བའི་གཟུགས་དགེ་བ་དང་མི་དགེ་བ་ནི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའོ། །

[Block 192 [HEADING]]
###### འབྱུང་བ་ཆེན་པོ་བཞི། ^1-1-3-1-5-0

[Block 193]
འབྱུང་བ་ཆེ་རྣམས་རྒྱུར་བྱས་པ། །ཞེས་སྨྲས་པ་དེ་དག་གང་ཞེ་ན། འབྱུང་བ་དག་ནི་སའི་ཁམས་དང་། ཆུ་དང་མེ་དང་རླུང་གི༌[^83]ཁམས་རྣམས་ཞེས་བྱ་བ་སྟེ། བཞི་པོ་དེ་དག་ནི་རང་གི་མཚན་ཉིད་དང་རྒྱུར་བྱས་པའི་གཟུགས་འཛིན་པའི་ཕྱིར་ཁམས་དག་གོ། །

[Block 194]
འབྱུང་བ་ཆེན་པོ་བཞི་རྣམས་ཞེས་བྱ་བ་ནི་འདི་དག་གཟུགས་གཞན་ཐམས་ཅད་ཀྱི་རྟེན་ཉིད་དུ་རིགས་པའི་ཕྱིར་ན་ཆེན་པོ་ཉིད་དོ། །

[Block 195]
ཡང་ན་ས་དང་ཆུ་དང་མེ་དང་རླུང་གི་ཕུང་པོ་དེ་དག་བྱ་བ་ལ་ཤས༌[^84]ཆེ་བ་དེ་དག་ལ་དེ་རྣམས་ཆེན་པོར་གནས་པའི་ཕྱིར་རོ། །

[Block 196]
ཡང་ཁམས་དེ་དག་གི་ལས་ནི༌[^85]གང་དུ་ཡང་དག་པར་འགྲུབ། རང་བཞིན་ནི་ཅི་ཞེ་ན། འཛིན་པ་ལ་སོགས་ལས་སུ་གྲུབ། །ཅེས་བྱ་བ་སྨོས་ཏེ། ས་དང་ཆུ་དང་མེ་དང་རླུང་གི་ཁམས་འདི་དག་ནི་གོ་རིམས་བཞིན་དུ༌[^86]འཛིན་པ་དང་སྡུད་པ་དང་སྨིན་པར་བྱེད་པ་དང་རྒྱས་པར་བྱེད་པའི་ལས་དག་ཏུ་གྲུབ་བོ། །

[Block 197]
རྒྱས་པར་བྱེད་པ་ནི་འཕེལ་བ་དང་རྒྱས་པར་བྱེད་པར་རིག་པར་བྱ་སྟེ། འདི་དག་ནི་དེ་དག་གི་ལས་ཡིན་ནོ། །

[Block 198]
རང་བཞིན་ནི་གོ་རིམས་བཞིན་དུ། སྲ་གཤེར་དྲོ་ཉིད་གཡོ་བ་རྣམས་ཏེ། སྲ་བ་ནི་སའི་ཁམས་སོ། །

[Block 199]
གཤེར་བ་ནི་ཆུའི་ཁམས་སོ། །

[Block 200]
དྲོ་བ་ནི་མེའི་ཁམས་སོ། །

[Block 201]
གཡོ་བ་ནི་རླུང་གི་ཁམས་སོ། །

[Block 202]
འདིས་འབྱུང་བའི་རྒྱུན་ཡུལ་གཞན་དུ་སྐྱེད༌[^87]བའི་ཕྱིར་གཡོ་བར་བྱེད་དེ། སྒྲོན་མ༌[^88]གཡོ་བ་བཞིན་དུ་གཡོ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 203]
རབ་ཏུ་བྱེད་པ་དག་དང་མདོ་སྡེ་ལས་རླུང་གི་ཁམས་གང་ཞེ་ན། ཡང་བ་ཉིད་དོ་ཞེས་གསུངས་ལ།

[Block 204]
རབ་ཏུ་བྱེད་པ་དག་ལས།

[Block 205]
ཡང་བ་ཉིད་དེ་རྒྱུར་བྱས་པའི་གཟུགས་ཞེས་ཀྱང་བཤད་དོ། །

[Block 206]
དེའི་ཕྱིར་གཡོ་བའི་རང་བཞིན་གྱི་ཆོས་གང་ཡིན་པ་དེ་ནི་རླུང་གི་ཁམས་ཤེས་པ་སྟེ། འདིའི་རང་བཞིན་ལས་ཀྱིས༌[^89]གསལ་བ་ཡིན་ནོ། །

[Block 207]
ས་ལ་སོགས་པ་དང་། སའི་ཁམས་ལ་སོགས་པ་ལ་བྱེ་བྲག་ཅི་ཡོད་ཅེ་ན།

[Block 208 [VERSE]]
འཇིག་རྟེན་གྱི་ནི་ཐ་སྙད་དོ། །
[^90]ཁ་དོག་དབྱིབས་ལ་ས་ཞེས་བརྗོད། །

[Block 209]
འདི་ལྟར་ས་སྟོན་པ་ན་ཁ་དོག་དང་དབྱིབས་སྟོན་པར་བྱེད་དོ། །

[Block 210]
ས་ལ་ཇི་ལྟ་བ་དེ་བཞིན་དུ། ཆུ་མེ་ཡང་ངོ་། །འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་ཁ་དོག་དང་དབྱིབས་ཉིད་ལ་བརྗོད་དོ། །

[Block 211]
རླུང་ཚོགས་ཁམས་ཉིད་ཡིན། རླུང་གི་ཁམས་གང་ཡིན་པ་དེ་ཉིད་ལ་འཇིག་རྟེན་ན་རླུང་ཞེས་འདོགས་སོ། །

[Block 212]
དེ་དང་འདྲ་བའང་ཡིན། ཇི་ལྟར་འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་ཁ་དོག་དང་དབྱིབས་ལ་ས་ཞེས་བརྗོད་པ་དེ་བཞིན་དུ་རླུང་ལ་ཡང་རླུང་སྔོན་པོ་རླུང་ཟླུམ་པོའོ་ཞེས་བརྗོད་དོ། །

[Block 213 [HEADING]]
###### གཟུགས་སུ་རུང་བ། ^1-1-3-1-6-0

[Block 214]
ཅིའི་ཕྱིར་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་བར་འདི་གཟུགས་ཀྱི་ཕུང་པོ་ཞེས་བྱ་ཞེ་ན། གཟུགས་སུ་རུང་བའི་ཕྱིར་ཏེ།[^91] བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་དག་གཟུགས་སུ་ཡོད་ཅིང་གཟུགས་སུ་རུང་བས། དེའི་ཕྱིར་གཟུགས་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ཞེས་བྱའོ། །ཅིས༌[^92]གཟུགས་སུ་རུང་ཞེ་ན། ལག་པའི་འདུས་ཏེ་རེག་པས་ན༌[^93]རེག་ན་ཡང་གཟུགས་སུ་རུང་ངོ་ཞེས་རྒྱས་པར་གསུངས་པ་ལྟ་བུའོ། །

[Block 215]
གཟུགས་སུ་རུང་ཞེས་བྱ་བ་ནི་གནོད་པར་བྱར་རུང་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ་འདི་ལྟར་དོན་གྱི་སྡེ་ཚན་དག་ལས།
--- END BLOCKS ---
