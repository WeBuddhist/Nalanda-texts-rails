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
[Block 141]
དཀྱིལ་འཁོར་ཉིད་ཀྱང་སའི་ཆ་མཉམ་པ་ལ། བྱི་དོར་བྱས་ཏེ་མེ་ཏོག་བཀྲམ་པ་འདི་ནི་མེ་ཏོག་གི་དཀྱིལ་འཁོར་རོ། །

[Block 142]
ཆག་ཆག་བཏབ་སྟེ་སོ་སོའི་གནས་སུ་དྲིའི་ཐིག་ལེ་བྱས་པ་ལ། རས་ལ་སོགས་པ་ལ་ཁ་དོག་དང་དབྱིབས་དང་རྒྱན་དང་ལྡན་པའི་སྐུ་བྲིས་ཏེ། ལྷག་པར་གནས་པ་བྱས་ནས་སོ་སོའི་གནས་སུ་བཀོད་པ་འདི་ནི་སྐུའིའོ། །

[Block 143]
ཡི་གེ་དང་ཕྱག་མཚན་དུ་བྱ་བའང་ཅི་རིགས་པའོ། །

[Block 144]
རྡུལ་ཚོན་གྱི་དཀྱིལ་འཁོར་ཡང་སའི་ཆ་མཉམ་པ་ལ་ཐིག་བཏབ་སྟེ། དཀར་པོ་ལ་སོགས་པའི་ཚོན་རིན་པོ་ཆེ་ལས་བྱུང་བའམ། འབྲུ་ལས་བྱུང༌[^53]བའམ། སའི་ཁམས་ལས་བྱུང་བ་བྱིན་གྱིས་བརླབས་ཏེ། དེས་མ་འདྲེས་ཤིང་སྐྱོན་དང་བྲལ་བ་བྲིས་ལ། སྐུ་གསུང་ཐུགས་གང་ཡང་རུང་བའི་ལྷ་བཀོད་དེ། དེར་དབང་བསྐུར་བ་འདི་ནི་དཀྱིལ་འཁོར་དུ་ཤེས་པར་བྱའོ། །

[Block 145]
དཀྱིལ་འཁོར་དེར་འཇུག་པའང་ཇི་ལྟར་འཇུག་ཅེ་ན།

[Block 146 [VERSE]]
དེར་འཇུག་པ་ནི་རྣམ་པ་གཉིས། །
སློབ་དཔོན་དང་ནི་སློབ་མའོ། །

[Block 147]
ཞེས་པ་དཀྱིལ་འཁོར་དུའང་ལྷའི་འཁོར་ལོ་ཡོངས་སུ་རྫོགས་པར་བྱས་ཏེ། དང་པོར་སློབ་དཔོན་འཇུག་པར་བྱའོ། །

[Block 148]
དེའང་དང་པོར་སེམས་བསྐྱེད་པ་དང་། ཁྲུས་བྱ་བ་དང་། གསོལ་བ་གདབ་པ་དང་། གནང་བ༌[^54]ནོད་པ་དང་། ཕྱག་འཚལ་བ་དང་། མཆོད་པ་དང་། བསྟོད་པ་དང་། སྡིག་པ་བཤགས་པ་དང་། སྡོམ་པ་གཟུང་བ་དང་། རྗེས་སུ་ཡི་རང་བ་དང་། བསྐུལ་བ་དང་། གསོལ་བ་གདབ་པ་དང་། སྐྱབས་སུ་འགྲོ་བ་དང་། སྨོན་ལམ་གདབ་པ་དང་། སྲས་སུ་བྱ་བ་དང་། བྱང་ཆུབ་སེམས་བསྡུ་བ༌[^55]དང་། གནང་བ་ནོད་པ༌[^56]ལ་སོགས་པ་འདིས་དང་པོར་བདག་ཉིད་འཇུག་པར་བྱའོ། །

[Block 149]
དེ་ནས་ཕྱིས་སློབ་མ་འཇུག་པ་བརྩམ་པར་བྱ་སྟེ། སྨོན་ལམ་བཏབ་པའི་རྗེས་ལ་བུར་བྱས་ཏེ།[^57] གནས་ཀུན་བྱིན་གྱིས་བརླབ་པ་དང་། །མཆོད་པ་དབུལ་བ་དང་། གདམས་ངག་བྱ་བ་དང་། ཆུ་བླུད་པ་དང་། བཀའ་བསྒོ་བ་དང་། ཡེ་ཤེས་དབབ་པ་དང་། མེ་ཏོག་དོར་བ་དང་། མིག་དབྱེ་བ་དང་། དཀྱིལ་འཁོར་བལྟ་བ་དང་། དེ་ཁོ་ན་ཉིད་བསྟན་པར་བྱ་བ་ལ་སོགས་པ་འདི་ནི་སློབ་མ་འཇུག་པའི་རིམ་པའོ། །

[Block 150]
འདི་དག་གིའང་སྔོན་དུ་བྱ་བའི་རིམ་པ་གང་ཡིན་ཞེ་ན།

[Block 151 [VERSE]]
དང་པོར་སའི་ཆོ་ག་དང་། །
སྟ་གོན་ཚོགས་ནི་བྱེ་བྲག་སྟེ། །

[Block 152]
བསྙེན་པ་སྤྱིའི་སྔོན་དུའོ། །ཞེས་པ་འདི་ནི་མདོར་བསྟན་པའོ། །

[Block 153]
སའི་ཆོ་ག་གང་དང་གང་ཡིན་ཞེ་ན།

[Block 154 [VERSE]]
དང་པོར་བརྟག་དང་བསླང་བ༌[^58]དང་། །
བྱིན་དང་མ་བྱིན་བརྟག་པ་དང་། །
སྦྱང་དང་བྱིན་བརླབ༌[^59]གཟུང་དང་བསྲུང་། །

[Block 155]
ཞེས་པའོ།

[Block 156]
[^60] །དང་པོར་བརྟག་པ་ནི་སྟེང་དང་འོག་ཏུ་སྟེ། ལས་གང་དང་རྗེས་སུ་མཐུན་པའི་ཁ་དོག་དང་དབྱིབས་དང་ཚད་དང་ལས་དང་མཚན་ཉིད་རྟོག་པ་འདི་ནི་ས་བརྟག་པའོ། །

[Block 157]
དེ་ནས་མཎྜལ་བྱི་དོར་བྱས་ཏེ་དཀྱིལ་འཁོར་གྱི་ལྷ་དང་སའི་ལྷ་མོ་དང་ཕྱོགས་སྐྱོང་ལ་སོགས་པ་ལ་གཏོར་མ་བྱིན་ནས་ལས་བཅོལ་བ་འདི་ནི་ས་བསླང་བའོ། །

[Block 158]
དེའི་ནུབ་མོ་རྨི་ལམ་དང་ཆུ་དང་མེ་ལ་རྟོག་པ༌[^61]དང་རོ་ལ་རྟོག་པ་འདི་ནི་བྱིན་ནམ་མ་བྱིན་བརྟག་པའོ། །

[Block 159]
སྔགས་དང་ཕྱག་རྒྱ་དང་བསམ་གཏན་དང་། རྫས་ལ་སོགས་པས་རིན་པོ་ཆེ་ཁ་དོག་སྣ་ཚོགས་པའམ། ཡི་གེའམ་རང་བཞིན་མེད་པར་བྱེད་པ་འདི་ནི་ས་སྦྱང་བའི་རིམ་པའོ། །

[Block 160]
དེ་ལ༌[^62]རླུང་དང་ཆུ་དང་ས་གཞི་རི་རབ་དང་བཅས་པ་ཁ་དོག་སྣ་ལྔ་དང་ལྡན་པ། གཞི་རིན་པོ་ཆེ་སྣ་ལྔ་ལས་གྲུབ་པར་བྱེད་པ་འདི་ནི་བྱིན་གྱིས་བརླབ༌[^63]པའོ། །

[Block 161]
དེའི་སྟེང་དུ་བདག་ཉིད་འདུག་པ་དང་། གཞལ་ཡས་ཁང་བསྐྱེད་པ་དང་། ལྷ་བསྐྱེད་པ་དང་། སྤྱན་དྲང་བ་དང་། དགུག་པ་དང་། མཆོད་པ་དགྲམ་པ་དང་། མཆོད་པ་དབུལ་བ་དང་། རྫས་ཁྱད་པར་ཅན་གཞན་དགྲམ་པ་དང་། རྣལ་འབྱོར་པ་སོ་སོར༌[^64]གནས་པ་དང་། མེ་ཏོག་གི་ཚོམ་བུ་དང་། གདན་དང་། དབང་བླང་བ་དང་། སྙོམས་པར་འཇུག་པ་དང་། གསོལ་བ་གདབ་པ་དང་། བཀའ་བསྒོ་བ་དང་། ཐོག་ཕུབ་པ་ལ་སོགས་པ་འདི་ནི་ས་གཟུང་བའི་རིམ་པའོ། །

[Block 162]
གཞན་ཡང་སྔགས་དང་ཕྱག་རྒྱ་ལ་སོགས་པའི་སྦྱོར་བས་འཁོར་ལོ་དང་། རྡོ་རྗེ་དང་། རིན་པོ་ཆེ་དང་། རལ་གྲི་དང་། རྒྱ་གྲམ་དང་། ཕུར་བུ་དང་། མེའི་ཁང་པ་བྱེད་པ་འདི་ནི་ས་བསྲུང་བའི་རིམ་པའོ། །

[Block 163]
སྟ་གོན་གྱི་ཆོ་ག་ཞེས་བྱ་བ་འདི་ཡང་གང་ཡིན་དུ་ཡོད་ཅེ་ན།

[Block 164 [VERSE]]
ས་ཡི་ལྷ་དང་དཀྱིལ་འཁོར་ལྷ། །
སློབ་མ་བུམ་པ་ལ་སོགས་པ། །
ཇི་ལྟར་སྟ་གོན་བྱ་བ་དང་། །

[Block 165]
ཞེས་པ་ནི་དང་པོར་སའི་ལྷ་མོ་སྟ་གོན་ལ་གནས་པ་ནི་གདན་བྱ་བ་དང་། ལྷ་མོ་སྦྲན་པ་དང་། བལྟ་བ་དང་། བྱིན་གྱིས་བརླབ་པ་དང་། མཆོད་པ་དབུལ་བ་དང་། གསོལ་བ་གདབ་པ་དང་། གནང་བ་སྟེར་བ་དང་། ཐིམ་པ་དང་། ས་གཞི་འོད་དུ༌[^65]འབར་བ་འདི་ནི་སའི་ལྷ་མོ་སྟ་གོན་ལ་གནས་པའི་རིམ་པའོ། །

[Block 166]
ཐིག་ལེ་བྱ་བ་དང་། ལྷ་བསྐྱེད་པ་དང་། ལྷ་སྤྱན་དྲང་བ་དང་། བསྟིམ་པ་དང་། དབང་བསྐུར་བ་དང་། བྱིན་གྱིས་བརླབ་པ༌[^66]དང་། མཆོད་པ་དབུལ་བ་དང་། བསྟོད་པ་བྱ་བ་དང་། གསོལ་བ་གདབ་པ་དང་། གནང་བ་སྟེར་བ་དང་། བསྡུ་བའམ༌[^67]གཤེགས་པ་འདི་ནི་དཀྱིལ་འཁོར་གྱི་ལྷ་སྟ་གོན་ལ་གནས་པའོ། །

[Block 167]
ཁྲུས་བྱ་བ་ལ་སོགས་པ་གོང་མ་བཞིན་ཏེ། སྐུད་པ་སྦྱིན་པ་དང་། སོ་ཤིང་དོར་བ་དང་། ཆོས་བཤད་པ་དང་། ཀུ་ཤ་སྦྱིན་པ་དང་། རྨི་ལམ་བརྟག་པ་དང་། ངན་ན་སྤོགས་པ་ནི་གོང་མ་ལས་ཤེས་པར་བྱ་སྟེ། འདི་ནི་སློབ་མ་སྟ་གོན་ལ་གནས་པའོ། །

[Block 168 [VERSE]]
བུམ་པ་སྟ་གོན་ཆོ་ག་ཡང་། །
རྒྱུ་དང་ཚད་དང་དབྱིབས་དང་ནི། །

[Block 169]
ཞེས་པ་བྱིན་གྱིས་བརླབས་པ༌[^68]དང་། །ལྷ་བསྐྱེད་པ་དང་། དགུག་གཞུག་བྱ་བ་དང་། དབང་བསྐུར་བ་དང་། མཆོད་པ་དང་། བསྟོད་པ་དང་། གསོལ་བ་གདབ་པ་དང་། རྫས་བསྒྲུབ་པའོ། །

[Block 170]
ནང་པར་སྔར་ནི་བློ་ཅན་ལངས། །མཚན་ཉིད་ཀུན་དང་ལྡན་པ་ཡི།[^69] །

[Block 171 [VERSE]]
སྐུད་པ་བྱིན་གྱིས་བརླབ་བྱ་སྟེ། །
དང་པོར་ནམ་མཁར་ཐིག་གདབ་སྟེ། །
དེ་ནས་ས་ལ་ཐིག་གདབ་པོ། །
དེ་རྗེས་ཚོན་རྣམས་བྱིན་བརླབས་ནས། །

[Block 172]
དཀྱིལ་འཁོར་སྡུ་གུར༌[^70]བྲི་བར་བྱ། །ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 173]
རྟགས་ཀྱང་གང་དང་གང་ལ་བརྟག་ཅེ་ན། །

[Block 174 [VERSE]]
ཀུ་ཤ་སོ་ཤིང་སྐུད་པ་དང་། །
དབབ་དང་དྲི་དང་མེ་ཏོག་དོར། །
འདི་ནི་རྟགས་ཀྱི་རྣམ་པ་སྟེ། །
མཁས་པ་ཡིས་ནི་བརྟག་པར་བྱ། །

[Block 175]
ཞེས་པ་དང་པོར་རྨི་ལམ་བརྟག་པ༌[^71]དང་སོ་ཤིང་ལ་འཇུག་པ་དང་། དངོས་གྲུབ་བརྟག་པ་དང་། སྐུད་པ་ལས་ནི་ཆད་པ་དང་མ་ཆད་པ་བརྟག་པའོ། །

[Block 176]
དབབ་པ་ནི་འདར་བ་དང་འཕར་བ་དང་། སྨྲ་བ་ལ་བརྟག་པའོ། །

[Block 177]
དྲི་བ་ནི་དཀར་པོ་ལ་སོགས་པ་བརྟག་པའོ། །

[Block 178]
མེ་ཏོག་ནི་སྐུའི་སྟོད་དང་སྨད་དང་གཙོ་བོ་དང་འཁོར་ལ་ཕོག་པ༌[^72]དང་མ་ཕོག་པ༌[^73]བརྟག་པའོ། །

[Block 179]
བརྡ་ཡང་གང་ཡིན་ཞེ་ན།

[Block 180 [VERSE]]
བུམ་པའི་དབང་དང་ལྡན་རྣམས་ཀྱིས། །
ལྔ་བསྡུས་ཕྱག་རྒྱ་བསྟན་པར་བྱ། །
--- END BLOCKS ---
