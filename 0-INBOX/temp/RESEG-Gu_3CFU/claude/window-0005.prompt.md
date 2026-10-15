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
དགེ་ཚུལ་ཉིད་དུ་ཁས་བླངས་པ་ལ་རྒྱུན་དང་རབ་ཏུ་ཆད་པ་དག་སྐྱབས་སུ་འགྲོ་བ་དང༌[^142]དགེ་ཚུལ་ཉིད་དུ་ཁས་ལེན་པའོ། །

[Block 177]
དེ་ལ་ཐ་མ་རབ་ཏུ་ཆད་པ་ནི་དོན་གཞན་ལ་རྗེས་སུ་འགྲོ་བ་སྟེ། བདག་དགེ་ཚུལ་ཞེས་བྱ་བར་སློབ་དཔོན་གྱིས་གཟུང་དུ་གསོལ་ཞེས་བྱ་བ་རྣམ་པ་གཉིས་སུ་བྱས་ཏེ། [^143]གསུམ་ཉིད་དུ་ངེས་པ་ཡིན་ནོ། །

[Block 178]
བརྗོད་པ་མ་རྫོགས་པ་ཉིད་ལ་ཅིའི་ཕྱིར་ཆ་གསུམ་པ་ལ་འདི་ལ་འཇུག་པ་ལ་གྲུབ་པ་ཉིད་འབྱུང་བ་ཡིན་ཏེ། གང་ཞིག་སླར་བྱས་སོ་ཞེས་བྱ་བ་སྟེ། མཚམས་གཅད་པ༌[^144]ལ་སོགས་པ་ཐམས་ཅད་ལ་ཆོ་ག་འདི་བལྟ་བར་བྱའོ། །

[Block 179]
དེ་ལྟར་ན་གསང་སྟེ་སྟོན་པ་ལས༌[^145]གསང་སྟེ་བསྟན་པ་མ་རྫོགས་པ་ལ་སློབ་དཔོན་ཉིད་དང་། དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་སྒྲུབ་པའི་དུས་འདི་ལ་ལས་བྱེད་པ་འདི་ལྟ་བུ་ཞེས་བྱ་བས་སོ། །

[Block 180]
གནས་སྦྱིན་པ་དང་ཀློག་པ་པོ་དག་ལ་དུས་གང་གི་ཚེ་ན་ཞེས་བྱ་བ་ཤེས་པ་མ་ཡིན་ཏེ། གནས་སྦྱིན་པ་དང་ཀློག་པ་པོ་དག་གི་ཚད་ལ་མི་གནས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 181]
དེ་ལ་ཅི་ཙམ་གྱིས་འདི་དག་ལ་སློབ་དཔོན་ཉིད་དུ་བྱ་བ་ཉིད་བཤད་པར་བྱའོ། །

[Block 182]
གནས་སྦྱིན་པ་ནི་ཞག་གཅིག་གནས་ཉིད་ཀྱི་ཕྱིར་ཉེ་བར་གནས་པ་མཐར་ཐུག་པས༌[^146]ཞེས་བྱ་བའོ།

[Block 183]
[^147] །ཞག་གཅིག་ཅེས་བྱ་བ་ནི་ཉིན་མོ་དང་མཚན་མོ་གཅིག་ནི་ཞག་གཅིག་སྟེ། གནས་ཀྱི་སློབ་དཔོན་ལ་གནས་པའི་སླད་དུ་གནས་ཉིད་ཀྱི༌[^148]གང་ཞིག་ཉེ་བར་གནས་པ་ལ་མཐར་ཐུག་པ་ཉིད་གནས་སྦྱིན་པ་མཐར་ཐུག་པའོ། །

[Block 184]
དེ་ལྟར་ཡང་གཞུང་ལས་གནས་ཀྱི་སློབ་དཔོན་ནི་གང་ཡིན་ཞེ་ན། གང་ཞིག་ཉེ་བར་མཚན་མོ་གཅིག་ཀྱང་གནས་པ་ནས༌[^149]གནས་སུ་འགྱུར་ཞེས་བྱ་བའོ། །

[Block 185]
འདི་ནས་བརྩམས་ཏེ་འདི་ལ་ཡོངས་སུ་རྫོགས་པའི་ངོ་བོ་ཉིད་ཚུ་རོལ་དུ་ནི་རེག་པ་ཙམ་མི་འགྲོ་བའི་མཐར་ཐུག་པ་མ་བྱས་པ་ཉིད་ཀྱིས་ཡིད་ལ་ངེས་པར་འབྲེལ་བཞིན་པ་ངེས་པའི་གྲངས་སུ་འགྲོ་བར་འོས་པ་མ་ཡིན་ནོ། །

[Block 186]
ཀློག་པ་ནི༌[^150]ཚིགས་སུ་བཅད་པ་གཅིག་ལན་གསུམ་བཟླས་ནའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དང་ཉེ་བར་ཀློག་པའི་བསམ་པས་ཚིགས་སུ་བཅད་པ་གཅིག་ལན་གསུམ་དུ་བཟླས་པ་དེ་ནི་ཀློག་པའི་སློབ་དཔོན་ནོ། །

[Block 187]
དེ་ལྟར་ན་ཀློག་པའི་མཐར་ཐུག་པའོ། །

[Block 188]
དེ་ལྟར་ཡང་གཞུང་ལས།

[Block 189]
ཀློག་པའི་སློབ་དཔོན་གང་ཞེ་ན། གང་ཞིག་དང་ཉེ་བར་རྐང་པ་བཞིའི་ཚིགས་སུ་བཅད་པ་ཡང་ལན་གསུམ་བཟླས་ནས་འཛིན་པར་འགྱུར་ཞེས་བྱ་བའོ། །

[Block 190]
དེ་བས་ན་འདིར་དྲང་སྲོང་གི་གཞུང་གི་དགོངས་པ་འདི་མཚོན་པ་ཡིན་ནོ། །

[Block 191]
ཀློག་པའི་སློབ་དཔོན་གྱིས་བརྗོད་པའི་ཀློག་པ་པོའི་རྗེས་སུ་བརྗོད་པ་ནི་འཛིན་པའོ། །

[Block 192]
ལན་ཅིག་བརྗོད་པ་ལ་རེག་པ་ཙམ་མ་རྫོགས་པའི་ངོ་བོའི་ཀློག་པ་ཡིད་ལ་ངེས་པར་འབྲེལ་པ་ཡིན་ནོ། །

[Block 193]
ལན་གསུམ་དུ་བརྩམས་ནས་མཐར་ཐུག་པར་འགྲོ་བ་དང་འདྲ་བར་རྒྱུན་བཞིན་དུ་མཚོན་པ་ཡིན་ནོ། །

[Block 194]
དེ་བས་ན་ཀློག་པའི་མཐར་ཐུག་པ་འདི་རིགས་པ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 195]
སློབ་དཔོན་རིན་ཆེན་སེང་གེས་གསུངས་པ། མ་ཐུ་རའི་ཀློག་པ་རྣམས་ནི་འདི་ལྟ་བུར་གྱུར་པ་སྟེ། འདི་ལྟར་མཐོང་བའི་ཕྱིར་རོ། །

[Block 196]
དེས་ནི་མདོ་འདི་བརྩམས་སོ། །

[Block 197]
འདི་ལྟར་རིགས་པ་མ༌[^151]ཡིན་ཏེ། གང་གི་ཕྱིར་གང་ཞིག་འདི་གཞུང་ལ་མ་ལྟོས་པར་མདོ་བྱེད་པ་ཡིན་ནོ། །

[Block 198]
དེ་ལ་འཐད་པ་སྨྲས་པ། འདི་ནི་རིགས་པ་མེད་པར་མདོ་ཙམ་ཉིད་དུ་ཉེ་བར་འབྲེལ་བ་སྟེ། དེ་བས་ན་ངེས་པར་འདི་འགའ་ཞིག་ཏུ་འདི་ལྟ་བུའི་ངོ་བོའི་དྲང་སྲོང་གིས་མཛད་པ་འབྱུང་བ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 199]
ཀློག་པའི་བསམ་པ་མེད་པས་བརྗོད་པ་ནི་ཀློག་པ་ཉིད་མ་ཡིན་ཏེ། [^152]ཀློག་པའི་བསམ་པ་མེད་པས༌[^153]གང་ཞིག་བརྗོད་པ་ནི་ཀློག་པ་ཉིད་དུ་མི་འགྱུར་ཏེ། དཔེར་ན་ཁ་ཏོན་བྱེད་པ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 200]
གོམས་པར་བྱ་བའི་བསམ་པས་ཀློག་པ་ལ་ཐ་སྙད་འདི་གྲགས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 201]
དེ་ལྟ༌[^154]བས་ན་འདིར་སློབ་དཔོན་ཉིད་ལ་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 202]
དེ་གཉིས་ལ་གཞན་དུ་ཉེ་བར་མི་བརྗོད་དོ་ཞེས་བྱ་བ་སྟེ། །དེ་གཉིས་ནི་མཁན་པོ་དང་སློབ་དཔོན་དག་གོ། །

[Block 203]
ཉེ་བར་ཀློག་པའི་ཚིག་ནི་ཉེ་བར་ཀློག་པའོ། །

[Block 204]
ཚེ་དང་ལྡན་པ་དང་བཙུན་པ་དང་གནས་བརྟན་གྱི་ཉེ་བར་ཀློག་པ་རྣམས་ཀྱིས་ཉེ་བར་ཀློག་པར་བྱས་པ༌[^155]ཡིན་ནོ། །

[Block 205]
ཉེ་བར་ཀློག་པ་མེད་པ༌[^156]འདི་དག་གི་མིང་གཟུང་བ༌[^157]ལ་རྒན་རིམས་ཉེ་བར་ཀློག་པ་མེད་པའི་མིང་གཟུང་བར་མི་བྱ་ཞེས་བྱ་བ་འདི་ཉིད་ཀྱིས་བཀག་པར་རིགས་པར༌[^158]བྱའོ། །

[Block 206]
སློབ་དཔོན་ནི་སློབ་དཔོན༌[^159]ཉིད་ཀྱིས་བརྗོད་པར་བྱའོ། །

[Block 207]
མཁན་པོ་ཡང་མཁན་པོ་ཉིད་དོ་ཞེས་བྱ་བའོ། །

[Block 208]
དེ་ལྟར་གཞན་ལ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མཁན་པོ་དང་སློབ་དཔོན་དག་ལས་གཞན་པའི་གང་ཟག་ལ་མཁན་པོ་དང་སློབ་དཔོན་གྱི་སྒྲ་དག་གིས་ཉེ་བར་བརྗོད་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 209]
དོན་གྱི་སླད་དུ་མཚན་ནས་སྨོས་ཏེ་ཞེས་བྱ་བ་དང་བཅས་པར་མ་སྨྲས་པར་མཁན་པོའི་མིང་མི་གཟུང་ངོ་ཞེས་བྱ་བ་སྟེ། བཅས་པར་ཞེས་བྱ་བ་ནི་མཁན་པོའི་གཟུང་བས་སོ། །

[Block 210]
དོན་གྱི་སླད་དུ་མཚན་ནས་སྨོས་ཏེ་ཞེས་བྱ་བའི་ངག་འདི་དག་དང་བཅས་པས་མཁན་པོའི་མིང་གཟུང་བར་བྱ་སྟེ། ཚིག་འདི་མ་བརྗོད་པར་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 211]
དེ་ཡང་འདི་ལ་དེ་མ་ཐག་པ་དང་བཅས་པར་བྱེད་པ་ཚིག་གང་ལ་འདི་ནི་འཇུག་པ་ལོག་པ་ཞེས་བྱ་བའི་བློའོ། །

[Block 212]
དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་སྒྲུབ་པའི་ཆོ་གའོ།། །།

[Block 213]
དགེ་འདུན་ལས་བསྙེན་པར་རྫོགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རབ་ཏུ་འབྱུང་བ་དང་དགེ་ཚུལ་ཉིད་དུ་ཁས་ལེན་པ་ལྟར་གང་ཟག་ལས་ནི་མ་ཡིན་ཏེ། [^160]འོན་ཀྱང་དགེ་འདུན་ལས་བསྙེན་པར་རྫོགས་པར་བྱའོ། །

[Block 214]
མཁན་པོ་ཉིད་དུ་ཕྱོགས་པར་གྱུར་པས་ལས་བྱེད་པ་དང་གསང་སྟེ་སྟོན་པའི་དགེ་སློང་ལ་གསོལ་བ་གདབ་པར་བྱའོ་ཞེས་བྱ་བ་སྟེ། མཁན་པོ་ཉིད་དུ་ཕྱོགས་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པ་ལ་མཁན་པོ་ཉིད་ཀྱིས་སོ་སོར་ཉེ་བར་གནས་པའོ། །

[Block 215]
གསོལ་བ་གདབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གསོལ་བ་གདབ་པའོ། །
--- END BLOCKS ---
