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
ཇེ་མཐོ་ཇེ་མཐོར་ཞེས་བྱ་བ་ནི་སྐྱེས་ཤིང་སྐྱེས་པ་ནའོ། །

[Block 142]
ཡང་ན་མཐོ་བའི་རིགས་དེ་ལས་བྱང་ཆུབ་སེམས་དཔའ་མཐོ་བར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 143]
སྐྱེ་བ་ཞེས་བྱ་བ་ནི་འབྱུང་བར་འགྱུར་བའོ། །

[Block 144]
ཡོངས་སུ་བཟུང་བ་ནི་ཐོབ་པར་བྱས་པའོ། །

[Block 145]
གྲགས་སོ༌[^76]ཞེས་བྱ་བ་ནི་མངོན་སུམ་དུ་མ་གྱུར་བའི་ཚིག་གོ། །

[Block 146]
དེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 147]
སྐྱེས་པའི་ལས་ནི་རུམ་སྐྱེད་པ་དང་། མིང་གདགས་པ་དང་། ཁ་ཟས་སྦྱིན་པ་དང་། གཙུག་ཕུད་བྱ་བ་དང་། ཚངས་སྐུད་གདགས་པ༌[^77]དང་། གཙུག་ཕུད་བཅིང་བ་དང་། སྐ་རགས་བཅིང་བ་ལ་སོགས་པ་གཟུང༌[^78]ངོ་། །སྦྱངས་པ་རིམ་པ༌[^79]བཞིན་དུ་བྱས་པ་ནི་གོ་རིམས་བཞིན་དུ་བྱས་པའོ། །

[Block 148]
མངོན་པར་སྐྱེས་པ་ཞེས་བྱ་བ་ནི་མངོན་པར་འཕེལ་བ་ནའོ། །

[Block 149]
རང་བཞིན་གྱིས་ཡིད་གཞུངས་པ་ནི་ངོ་བོ་ཉིད་ཀྱིས་ཡིད་གཞུངས་པའོ། །

[Block 150]
མགོན་སྐྱབས་ཀྱི་ཁྱད་པར་ནི་མགོན་སྐྱབས་ཀྱི་སྦྱོར་བའོ། །

[Block 151]
ཆེད་ཆེར་འཛིན་པ་ཉིད་ལྟ་བ་ཡིན་ཏེ། ཤེས་པ་ལ་གཅིག་ཏུ་ལྟ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 152]
ལེ་ལོ་ནི་སྙོམ་ལས་ཏེ། དེ་མེད་པ་ནི་ལེ་ལོ་མེད་པ་སྟེ། རིང་པོར་མ་ཐོགས༌[^80]པས་ཞེས་བྱ་བའི༌[^81]དོན་ཏོ། །

[Block 153]
རིག་པའི༌[^82]གནས་བཅོ་བརྒྱད་ནི་འདི་ལྟ་སྟེ། རོལ་མོ་དང་། འཁྲིག་ཐབས་དང་། འཚོ་ཚིས་དང་། གྲངས་ཅན་དང་། སྒྲ་དང་། གསོ་བའི་དཔྱད་དང་། བཟོ་དང་། འཕོང་དཔྱད༌[^83]དང་། གཏན་ཚིགས་ཀྱི་སྦྱོར་བ་དང་། རྣལ་འབྱོར་དང་། ཐོས་ཤིང་དྲན་པ་དང་། སྐར་མའི་དཔྱད༌[^84]དང་། རྩིས་དང་། མིག་འཕྲུལ་དང་། སྔོན་གྱི་རབས་དང་། དེ་བཞིན་དུ་བྱེ་བྲག་པ་དང་། དོན་གྱི་ཕྲེང་བ༌[^85]དང་། རིག་པའི་བསྟན་བཅོས་དང་། ཡོངས་སུ་བརྟགས༌[^86]པའོ། །

[Block 154]
དེ་བཞིན་དུ་ཡང་བདག་གི་རིགས་ཞེས་བྱ་བ་ནི་བྲམ་ཟེའི་རིགས་ལ་གནས་པ་ལས་མ་འདས་པ་སྟེ། མི་འགལ་བ་ནི་བྲམ་ཟེའི་གནས་པ་ལས་མ་འཁྲུལ་པའོ། །

[Block 155]
སྒྱུ་རྩལ་རྣམས་ཞེས་བྱ་བ་ནི་སྒྱུ་རྩལ་མཐའ་དག་སྟེ། སྙན་ངག་དང་། གླུ་དབྱངས་དང་། གླེགས་འདྲ་མཁན་དང་། འཐབ་མོ་དང་། རོལ་མོ་དང་། མཚན་མ་དང་། མེ་ཏོག་གི་ལས་ཀྱི་སྦྱོར་བ་དང་། དམག་གི༌[^87]བཀོད་པ་དང་། རྩིས་དང་། གཡོས་ཀྱི་ལས་དང་། བུད་མེད་ཀྱི་མཚན་ཉིད་དང་། སྐྱེས་པའི་མཚན་ཉིད་དང་། གར་དང་། ཚོང་དང་། ཤིང་འཇོག་པ་དང་། འདྲི་བ་དང་། རྩིག་པའི་ལས་དང་། རི་མོའི་ལས་དང་། སོག་ལེའི་ལས་དང་། ཁྱིམ་ས་བརྟག་པའི་མཚན་ཉིད་དང་། མལ་སྟན་གྱི༌[^88]མཚན་ཉིད་དང་། [^89]རིན་པོ་ཆེ་བརྟག་པ་དང་། སྐུ་གཟུགས་ཀྱི་མཚན་ཉིད་དང་། གླང་པོ་ཆེ་བརྟག་པ་དང་། བཞད་གད་དང་། བྲོ་གར་དང་། ལུས་ཀྱི་བསྐུ་མཉེ༌[^90]དང་། ལྟས་ཤེས་པ་དང་། ཧོ་ར་ཛྙཱ་ན་ནོར་སྒྱུར་མཁན་དང་། གཏེར་ཤེས་པ་དང་། མཆོད་སྦྱིན་གྱི་ཆོ་ག་ཤེས་པ་དང་། མཚོན་ཆ་བརྟག་པ་དང་། ལུགས་ཀྱི་བསྟན་བཅོས་ཤེས་པ་དང་། མིག་འཕྲུལ་ཤེས་པ་དང་། བཞོན་པ་དང་ལྷན་ཅིག་སྤྱོད་པ་དང་། དེ་ལ་སོགས་པའི་སྒྱུ་རྩལ་དྲུག་ཅུ་རྩ་བཞིའོ། །

[Block 156]
རང་གི་རིགས་ནི་བྲམ་ཟེའི་རིགས་སོ། །

[Block 157]
སློབ་དཔོན་དམ་པའི་གོ་འཕང་ནི་སློབ་དཔོན་དམ་པའི་གོ་འཕང་སྟེ།

[Block 158 [VERSE]]
དམ་པའི་ཁྱད་པར་ཐོབ་པར་གྱུར་ཞེས་པའོ། །
རིག་བྱེད་ཤེས་ལ་བྱ་བ་སྨོས་ཏེ།
དེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 159]
རིག་བྱེད་ཤེས་ལ་ཞེས་བྱ་བ་དེ་ཚངས་པ་ཤེས་པའོ། །

[Block 160]
ཚངས་པ་བཞིན་ཞེས་བྱ་བ་ནི་ཚངས་པ་བཞིན་གྱུར་པའོ། །

[Block 161]
རྒྱལ་པོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཡུལ་ན་གནས་པའི་རྒྱལ་པོ་བཞིན་དུ་སྐྱེ་དགུ་རྣམས་ལ་མཛེས་པ་ཡིན་ཏེ། བཀུར་བ་ནི་ཞེ་ས་དང་མཆོད་པ་མང་པོས་སོ། །

[Block 162]
གནས་ནི་སྣོད་དུ་གྱུར་པའོ། །

[Block 163]
སྐྱེ༌[^91]དགུ་རྣམས་ནི་དོན་སྤྱོད་པ་སྟེ། སྤྲིན་ལས་ཆར་བབ་པ་ལྟ་བུ་ཡིན་ཏེ། བརྒྱ་བྱིན་ནི་མིག་སྟོང་ལྡན་ནོ། །

[Block 164]
མངོན་སུམ་ནི་མངོན་སུམ་ཉིད་དོ། །ཤེས་འདོད་རྣམས་ནི་ཤེས་པར་འདོད་པའི་སློབ་མ་རྣམས་སོ། །

[Block 165]
དོན་སྤྱོད་ནི་ཕན་པར་འདོད་པ་སྟེ། ཇི་ལྟར་བུའི་ཕ་ལྟ་བུར་རོ། །

[Block 166]
དེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 167]
སྐལ་བ་དང་ཡོན་ཏན་ཞེས་བྱ་བ་ནི་སྐལ་བ་དང་ཡོན་ཏན་ཏེ། སྐལ་བ་དང་ཡོན་ཏན་ཉིད་ཁྱད་པར་དུ་གྱུར་པ་ཡིན་པའི་ཕྱིར་སྐལ་བ་དང་ཡོན་ཏན་ཁྱད་པར་དུ་གྱུར་པའོ། །

[Block 168]
དེ་ཡང་དག་པར་སོགས་པ་ཡིན་པས་སྐལ་བ་དང་ཡོན་ཏན་ཁྱད་པར་དུ་གྱུར་པ་དང་ལྡན་པའོ། །

[Block 169]
སྐལ་བ་ནི་བསོད་ནམས་སོ། །

[Block 170]
ཡོན་ཏན་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གོ། །

[Block 171]
ཁྱད་པར་ནི་ལྷག་པའོ། །

[Block 172]
ལྡན་པ་ནི་མངོན་དུ་བྱས་པའོ། །

[Block 173]
རྙེད་པ་ནི་དབྱིག་དང་གསེར་ལ་སོགས་པའོ། །

[Block 174]
བཀུར་སྟི་ནི་མཆོད་པའོ། །

[Block 175]
ཆེན་པོ་ནི་མང་པོ་སྟེ་མང་པོའི་སྒྲ་ནི་རེ་རེ་ལ་སྦྱར་ན་རྙེད་པ་ཆེན་པོ་དང་བཀུར་སྟི་ཆེན་པོའོ། །

[Block 176]
གྲགས་པ་ནི་སྙན་པར་གྲགས་པའོ། །

[Block 177]
ཁྱད་པར་ནི་ཁྱད་པར་དུ་འཕགས་པ་སྟེ་བྱུང་བར་གྱུར་ཏེ་ཞེས་བྱ་བ་ནི་བྱུང་ངོ༌[^92]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 178]
བྱང་ཆུབ་སེམས་དཔའ་དེའི་བློ་ནི་སེམས་སོ། །

[Block 179]
ཆོས་ལ་གོམས་པ་ཞེས་བྱ་བ་ལ་ཆོས་ནི་རྣམ་པ་གཉིས་ཏེ། ཁྱིམ་ན་གནས་པའི་ཆོས་དང་། མངོན་པར་འབྱུང་བའི་ཆོས་སོ། །

[Block 180]
ཁྱིམ་ན་གནས་པའི་ཆོས་ལ༌[^93]གོམས་ཤིང་བསྒོམས་པར་གྱུར་ཀྱང་དེ་རྙེད་པ་ལ་སོགས་པ་དེ་ལ་མངོན་པར་དགའ་བར་མ་གྱུར་ཏེ། རབ་ཏུ་བྱུང་བ་དང་འདྲིས་པར་བྱས་པ་ཞེས་བྱ་བ་རབ་ཏུ་བྱུང་བ་ལ་འདྲིས་པར་བྱས་པས་ནི། བྱང་ཆུབ་སེམས་དཔའ་དེ་རབ་ཏུ་བྱུང་བ་ལ་དགའ་ཞིང་། དེ་ལ་དགའ་བར་མ་གྱུར་པ་ནི།
--- END BLOCKS ---
