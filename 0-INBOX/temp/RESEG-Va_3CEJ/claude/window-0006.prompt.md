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

[Block 216 [VERSE]]
གལ་ཏེ་འདོད་པ་ཚོལ་བྱེད་ཅིང་། །
འདུན་པ་སྐྱེས་པའི་ལུས་ཅན་ཏེ།
འདོད་པ་དེ་དག་མ་འབྱོར་ན། །
ཟུག་རྔུས་ཟུག་བཞིན་གནོད་པར་འགྱུར། །

[Block 217]
ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 218]
གཟུགས་ཀྱི་གནོད་པ་གང་ཞེ་ན། ཡོངས་སུ་འགྱུར་བ་སྐྱེད་པའོ། །

[Block 219]
གཞན་དག་ན་རེ་གཟུགས་སུ་རུང་བ་ནི་ཐོགས་པའོ་ཞེས་ཟེར་རོ། །

[Block 220]
འོ་ན་ནི་རྡུལ་ཕྲ་རབ་གཟུགས་མ་ཡིན་པར་འགྱུར་ཏེ། གཟུགས་སུ་མེད་པའི་ཕྱིར་རོ། །

[Block 221]
རྡུལ་ཕྲ་རབ་ཀྱི་གཟུགས་གཅིག་པུ་ལོགས་ཤིག་ཏུ་གྱུར་པ་ནི་མེད་པ་ཉིད་དོ། །

[Block 222]
འདུས་པ་ལ་གནས་པ་དེ་ལ་ནི་གཟུགས་སུ་རུང་བ་ཉིད་དོ། །

[Block 223]
འོ་ན་ནི་འདས་པ་དང་མ་འོངས་པ་གཟུགས་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 224]
དེ་ཡང་གཟུགས་སུ་ཡོད་ཟིན་པ་དང་། གཟུགས་སུ་ཡོད་པར་འགྱུར་བ་དང་། དེ་དང་རིགས་མཐུན་པའི་ཕྱིར་གཟུགས་ཡིན་ཏེ་བུད་ཤིང་བཞིན་ནོ། །

[Block 225]
འོ་ན་ནི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གཟུགས་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 226]
དེ་ཡང་རྣམ་པར་རིག་བྱེད་ལ་གཟུགས་སུ་ཡོད་པའི་ཕྱིར་གཟུགས་སུ་ཡོད་པར་འགྱུར་ཏེ། ཤིང་ལྗོན་པ་གཡོས་པས་གྲིབ་མ་གཡོ་བ་བཞིན་ནོ། །

[Block 227]
འགྱུར་བ་མེད་པའི་ཕྱིར་མ་ཡིན་ཏེ། རྣམ་པར་རིག་བྱེད་ལོག་ན་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཡང་ལྡོག་པར་འགྱུར་ཏེ། ཤིང་ལྗོན་པ་མེད་ན་གྲིབ་མ་མེད་པ་བཞིན་ནོ། །

[Block 228]
གཞན་དག་ན་རེ་རྟེན་གྱི་འབྱུང་བ་ལ་གཟུགས་སུ་ཡོད་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 229]
དེ་ལྟ་ན་འོ་ན་ནི་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་ཡང་རྟེན་གཟུགས་སུ་ཡོད་པའི་ཕྱིར་གཟུགས་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 230]
ཉེ་བར་བཀོད་པ་འདི་ནི་མི་མཐུན་པ་ཡིན་ཏེ། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་འདི་ནི་ཤིང་ལྗོན་པ་ལ་གྲིབ་མ་ཉིད་དང་། ནོར་བུ་ལ་འོད་ཉིད་བཞིན་དུ་འབྱུང་བ་རྣམས་ལ་བརྟེན་ནས་འཇུག་གོ། །

[Block 231]
[^94]

[Block 232]
མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་ནི་དེ་ལྟར་མིག་ལ་སོགས་པ་ལ་བརྟེན་ནས་འཇུག་པ་མ་ཡིན་ཏེ། དེ་དག་ནི་དེ་དག་གི་སྐྱེ་བའི་རྒྱུ་མཚན་ཙམ་ཡིན་པ༌[^95]འབའ་ཞིག་ཙམ་དུ་ཟད་པས་སོ། །

[Block 233]
ཤིང་ལྗོན་པ་ལ་བརྟེན་ནས་གྲིབ་མ་དང་། མར་མེ་ལ་བརྟེན་ནས་འོད་འཇུག་གོ་ཞེས་བྱ་བ་འདི་ནི་རེ་ཞིག་བྱེ་བྲག་ཏུ་སྨྲ་བ་མ་ཡིན་ཏེ། གྲིབ་མ་ལ་སོགས་པ་ཁ་དོག་གི་རྡུལ་ཕྲ་རབ་རྣམས་སོ་སོ་རང་གི་འབྱུང་བ་བཞི་ཚན་ལ་བརྟེན་པ་ཉིད་དུ་ཁས་ལེན་པའི་ཕྱིར་རོ། །

[Block 234]
གྲིབ་མ་དང་འོད་དེ་དག་ལ་བརྟེན་པ་ཉིད་ཡིན་ཡང་རྣམ་པར་རིག་བྱེད༌[^96]མ་ཡིན་པའི་རྟེན་འབྱུང་བ་ཆེན་པོ་དག་འགགས་ཀྱང༌[^97]འགག་པར་ཁས་ལེན་པའི་ཕྱིར་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་དེ་ལྟར་བརྟེན་པར་མི་རུང་ངོ་། །དེའི་ཕྱིར་དེ་ནི་ལན་དུ་མི་རུང་ངོ་། །གཞན་དག་ནི་འདི་ལ་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་རྟེན་ནི་ཐ་དད་དུ་གྱུར་པ་སྟེ། ཁ་ཅིག་ནི་གཟུགས་སུ་རུང་བ་སྟེ་མིག་ལ་སོགས་པའོ། །

[Block 235]
ལ་ལ་ནི་གཟུགས་སུ་མི་རུང་བ་སྟེ་ཡིད་དོ། །

[Block 236]
རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་འདྲ་བར་ཐལ་བ་མེད་དོ། །

[Block 237]
དེའི་ཕྱིར༌[^98]གཟུགས་སུ་ཡོད་པས་ན་གཟུགས་སོ་ཞེས་བྱ་བ་འདི་ནི་འཐད་པ་ཡིན་ནོ་ཞེས་ལན་འདེབས་སོ། །

[Block 238 [HEADING]]
###### སྐྱེ་མཆེད་དང་ཁམས་རྣམ་པར་གཞག་པ། ^1-1-3-1-7-0

[Block 239]
གཟུགས་ཀྱི་ཕུང་པོའི་ངོ་བོ་ཉིད་བསྟན་པ་གང་དག་ཡིན་པ།

[Block 240 [VERSE]]
དབང་དོན་དེ་དག་ཁོ་ན་ལ། །
སྐྱེ་མཆེད་དང་ནི་ཁམས་བཅུར་འདོད། །

[Block 241]
སྐྱེ་མཆེད་རྣམ་པར་གཞག་པ༌[^99]ནི་སྐྱེ་མཆེད་བཅུ་སྟེ། མིག་གི་སྐྱེ་མཆེད་དང་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ནས། ལུས་ཀྱི་སྐྱེ་མཆེད་དང་རེག་བྱའི་སྐྱེ་མཆེད་ཀྱི་བར་ཡིན་ནོ། །

[Block 242]
ཁམས་རྣམ་པར་གཞག་པ་ནི་དེ་དག་ཉིད་ཁམས་བཅུ་སྟེ། མིག་གི་ཁམས་དང་། གཟུགས་ཀྱི་ཁམས་ནས། ལུས་ཀྱི་ཁམས་དང་རེག་བྱའི་ཁམས་ཀྱི་བར་ཡིན་ནོ། །

[Block 243]
གཟུགས་ཀྱི་ཕུང་པོ་དང་། དེའི་སྐྱེ་མཆེད་དང་། ཁམས་རྣམ་པར་གཞག་པ་བཤད་ཟིན་ཏོ། །

[Block 244 [HEADING]]
##### ཚོར་བའི་ཕུང་པོ། ^1-1-3-2-0

[Block 245]
ཚོར་བ་ལ་ལོགས༌[^100]པ་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་ཚོར་བ་མྱོང་བ། མྱོང་བ་རྣམ་པ་གསུམ་ནི་ཚོར་བའི་ཕུང་པོ་སྟེ། བདེ་བ་དང་། སྡུག་བསྔལ་བ་དང་། སྡུག་བསྔལ་ཡང་མ་ཡིན་བདེ་བ་ཡང་མ་ཡིན་པའོ། །

[Block 246]
དེ་ཡང་དབྱེ་ན་ཚོར་བའི་ཚོགས་དྲུག་སྟེ། མིག་གི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་ནས། ཡིད་ཀྱི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བའི་བར་རོ། །

[Block 247 [HEADING]]
##### འདུ་ཤེས་ཀྱི་ཕུང་པོ། ^1-1-3-3-0

[Block 248]
འདུ་ཤེས་ནི། མཚན་མར་འཛིན་པའི་བདག་ཉིད་དོ། །

[Block 249]
གང་སྔོན་པོ་དང་། སེར་པོ་དང་། རིང་པོ་དང་། ཐུང་ངུ་དང་། ཕོ་དང་། མོ་དང་། མཛའ་བཤེས་དང་། མཛའ་བཤེས་མ་ཡིན་པ་དང་། བདེ་བ་དང་། སྡུག་བསྔལ་བ༌[^101]ལ་སོགས་པའི་རང་བཞིན་གྱི་ཁྱད་པར་ལ་མཚན་མར་འཛིན་པ་དེ་ནི་འདུ་ཤེས་ཀྱི་ཕུང་པོའོ། །

[Block 250]
དེ་ཡང་དབྱེ་ན་འདུ་ཤེས་ཀྱི་ཚོགས་དྲུག་སྟེ། ཚོར་བ་བཞིན་ནོ། །
--- END BLOCKS ---
