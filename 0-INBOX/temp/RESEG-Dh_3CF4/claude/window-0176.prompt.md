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
[Block 6161]
འདུས་བྱས་ཀྱི་མཚན་ཉིད་བཞི་ནི་སྐྱེ་བ་དང་། གནས་པ་དང་། རྒ་བ་དང་མི་རྟག་པའོ། །

[Block 6162]
མི་རྟ་གླང་ཆེན་ཤིང་རྟ་མང་པོ་ཞེས་བྱ་བ་ནས་བརྩམས་པའི་ཚིགས་བཅད་ཐམས་ཅད་ཀྱིས་ནི་འཆི་བ་མི་ཟློགས་པ་ཉིད་ལས་བརྩམས་ནས་སོ། །

[Block 6163]
ཚིགས་བཅད་འདི་དག་གི་དོན་ནི་འདི་ཡིན་ཏེ། མི་དང་། དུད་འགྲོ་དང་། ལྷ་དང་། ལྷ་མ་ཡིན་གྱི་འགྲོ་བ་ལ་གནས་པས་ཀྱང་འཆི་བ་ལས་མི་ཟློགས་པ༌[^3953]ཉིད་དུ་བསྟན་ཏོ། །

[Block 6164]
དམྱལ་བ་རྣམས་སུ་ནི་དེའི་བསམ་པའི་སྐབས་མེད་པའི་ཕྱིར། དམྱལ་བ་འདིར་མ་སྨོས་སོ། །

[Block 6165]
དེ་ལྟར་རེ་ཞིག་ཚིགས་བཅད་འདི་དག་གི་ཁྱད་པར་ནི་འདི་ལྟར་སྣང་སྟེ། ཁྱད་པར་གཞན་ནི་གང་ཡང་མེད་དོ། །

[Block 6166]
མི་རྟ་གླང་ཆེན་ཤིང་རྟ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་ནི་དགྲ་གཞན་དག་ནི་ཐུབ་པར་ནུས་ཀྱི། འཆི་བདག་གི་དགྲ་ལས་ནི་རྒྱལ་བར་མི་ནུས་སོ་ཞེས་པའི་དོན་ཏོ། །

[Block 6167]
རྟ་དང་གླང་ཆེན་རྐང་ཐང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་ནི་དམག་གིས་ཡོངས་སུ་བསྲུངས་ན། དགྲ་དག་ལས་ནི་ཐར་པར་འགྱུར་གྱི། འཆི་བདག་གི་དགྲ་ལས་ནི་དམག་གིས་ཐར་བར་མི་འགྱུར་ར་ཞེས་པའི་དོན་ཏེ། [^3954]དེ་བཞིན་དུ་ཚིགས་བཅད་གཞན་དག་ལ་ཡང་བྱེ་བྲག་དེ་ལྟར་བརྗོད་པར་བྱའོ། །

[Block 6168]
གད་པ་ཆེན་པོའི་ངོས་དྲལ་རྒྱལ་བར་གྱུར་པ་ཡི། །ཞེས་བྱ་བ་ནི་ཆུ་བོའི་ངོགས་ཀྱི་གད་པ་ལས་རྒྱལ་བའོ། །

[Block 6169]
རྩེ་མེ་ཉིད་འབར་བ་ཡིན་པས་རྩེ་མེ་འབར་བའོ། །

[Block 6170]
ཁྲོས་པའི་རླུང་གིས་རྩེ་མེ་འབར་བ་དེ་ནི་ཁྲོས་པའི་རླུང་གིས་རྩེ་མེ་འབར་བའོ། །

[Block 6171]
འབྲུག་སྒྲ་དྲག་པོས་དཀྲུགས་པ༌[^3955]གང་ཡིན་པ་དེ་ནི་འབྲུག་སྒྲ་དྲག་པོས་དཀྲུགས་པའོ། །

[Block 6172]
ནད་དང་དགའ་བའི༌[^3956]མཆེ་བ་གཙིགས་པའི་ཁ་གདངས་པ་གང་ཡིན་པ་དེ་ནི་ཁ་གདངས་ནད་དང་རྒ་བའི་མཆེ་བ་གཙིགས་པ་ཉིད་དོ། །

[Block 6173]
མི་སྡུག་པ་དང་། འཇིགས་པའི་གདོན་གང་ཡིན་པ་དེ་ནི་མི་སྡུག་པ་དང་འཇིགས་པའི་གདོན་ནོ། །

[Block 6174]
དམ་དུ་འཛིན་པ་གང་ཡིན་པ་དེ་ནི་དམ་དུ་འཛིན་པའོ། །

[Block 6175]
སྙེམས་པའི་མཐུ་རྩལ༌[^3957]ནི་རབ་ཏུ་སྙེམས་པའི་མཐུ་རྩལ་ཏེ། རབ་ཏུ་སྙེམས་པའི་མཐུ་རྩལ་རྒུད་པ༌[^3958]གང་ཡིན་པ་དེ་དག་ནི་རབ་ཏུ་སྙེམས་པའི༌[^3959]མཐུ་རྩལ་ཉམས་པར་འགྱུར་བའོ། །

[Block 6176]
མཆོད་པར་འདོད་པ་དང་། གནོད་པ་ནི་མཆོད་འདོད་གནོད་པའོ། །

[Block 6177]
དེ་དག་མཆོད་འདོད་གནོད་བྱེད་ནི། མཆོད་པར་བྱ་བ་དང་། གནོད་པ་བྱེད་པའི་ཆེད་དུ་འོངས་ཤིང་ལྷགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 6178]
ཞི་བར་ནུས་པ་ནི་དེ་སེལ་བར་བྱེད་པའོ། །

[Block 6179]
དཀའ་ཐུབ་བདེ་ལེགས་ཞེས་བྱ་བ་ལ། དང༌[^3960]གི་སྒྲ་ནི་རིགས་པ་ཡང་བསྡུ་བའོ། །

[Block 6180]
སྒྱུ་མ་མཁན་ཞེས་བྱ་བ་ནི་མིག་འཕྲུལ༌[^3961]ལ་མཁས་པའོ། །

[Block 6181]
མང་པོ་འདུས་པ་ནི་སྐྱེ་བོ་མང་པོའི་ཚོགས་སོ། །

[Block 6182]
སླུ་བར༌[^3962]ནུས་ཞེས་བྱ་བ་ནི་གང་གིས་རྨོངས་པར་བྱེད་པ་ཡིན་པས་སླུ་བར༌[^3963]ནུས་པ་སྟེ། རྟ་དང་གླང་པོ་ཆེ་ལ་སོགས་པ་སྐྱེ་བོ་རྣམས་ཀྱིས་མཐོང་བའི་སྒྱུ་མ༌[^3964]བྱས་པའོ། །

[Block 6183]
དཀའ་ཐུབ་ཉིད་མཐུ་ཡིན་པས་དཀའ་ཐུབ༌[^3965]མཐུའོ། །

[Block 6184]
གྲུབ་པ་རྣམས་ཀྱི་གསང་སྔགས་ནི་གསང་སྔགས་གྲུབ་པའོ། །

[Block 6185]
དཀའ་ཐུབ་ཀྱི་མཐུ་དང་གསང་སྔགས་གྲུབ་པ་ནི་དཀའ་ཐུབ་ཀྱི༌[^3966]མཐུའོ། །

[Block 6186]
ཁ་ཅིག་ཏུ་ནི་གསང་སྔགས་གྲུབ་པས་ཞེས་ཀྱང་བརྗོད་དེ། དཀའ་ཐུབ་ཀྱི་མཐུ་གྲུབ་པ་ནི། དཀའ་ཐུབ་ཀྱི་མཐུ་གྲུབ་པ་སྟེ། དཀའ་ཐུབ་ཀྱི་མཐུས་གསང་སྔགས་གྲུབ་པ་ནི་དཀའ་ཐུབ་ཀྱི་མཐུའོ། །

[Block 6187]
ཆོས་ཕྱིར་བདག་བློ་བསམ༌[^3967]མཐར་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་བློས་སོ། །

[Block 6188]
མངོན་དུ་བྱུང་ནས་ཞེས་བྱ་བ་ནི་གསལ་བར་སྟོན་པའོ། །

[Block 6189]
སླར་ཡང་མི་སྣང་འགྱུར་ཞེས་བྱ་བ་ནི་མིག་ལམ་དུ་མི་སྣང་བར་གྱུར་པའོ། །

[Block 6190]
བར་བར་མཁའ་ལ་འགྲོ་ཞིང༌[^3968]ཞེས་བྱ་བ་ནི། མི་སྣང་བར་འགྲོ་བ་ལས་ཀྱང་ནམ་མཁའ་ལ་འགྲོ་བའོ། །

[Block 6191]
ས་འོག་ནུབ་པ་ཞེས་བྱ་བ་ནི། ཐོགས་པ་དང་བཅས་པ་ལ་ཐོགས་བ་མེད་པར་འགྲོ་བའོ། །

[Block 6192]
མངོན་དུ་བྱུང་ནས་སླར་ཡང་མི་སྣང་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི་སྤྲུལ་པའི་རྫུ་འཕྲུལ་བསྟན་ཏོ། །

[Block 6193]
བར་བར་མཁའ་ལ་འགྲོ་ཞིང་བར་བར་ས་འོག་ནུབ། །ཅེས་བྱ་བ་འདིས་ནི་འགྲོ་བའི་རྫུ་འཕྲུལ་བསྟན་ཏོ། །

[Block 6194]
གསང་སྔགས་རྣམས་ཀྱི་མཐུ་ནི་གསང་སྔགས་ཀྱི་མཐུའོ། །

[Block 6195]
གསང་སྔགས༌[^3969]ཀྱི་མཐུས་བྱས་པའི་སྟོབས་ནི་གསང་སྔགས་ཀྱི་མཐུ་སྟོབས་སོ། །

[Block 6196]
རྣམ་པ་སྣ་ཚོགས་པའི་གསང་སྔགས་ཀྱི་མཐུ་སྟོབས་གང་ཡིན་པ་དེ་དག་ནི་གསང་སྔགས་ཀྱི་མཐུ་སྟོབས་རྣམས་སོ། །

[Block 6197]
ང་རྒྱལ་བདོ་བའི་བློ་ཅན་ཞེས་བྱ་བ་ནི་ལྷ་དང་ལྷ་མ་ཡིན་གྱི་དམག་ཚོགས་སོ། །

[Block 6198]
ཁྲོས་པ་མ་མཆིས་ཞེས་བྱ་བ་འདིས་ནི་གང་སྔར་བསྟན་པའི་བདག་ཉིད་ཕུང་བྱེད་པ་སུ་ཞིག་གིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་དེའི་དོན་མ་ཡིན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6199]
བྱམས་པ་མ་མཆིས་ཞེས་བྱ་བ་འདིས་ནི་གང་སྔར་བསྟན་པའི་ང་ལ་ཅུང་ཟད་དོགས་པའམ་ཞེས་བྱ་བའི་ཚིགས་བཅད་དོན་དེ་མེད་པ་ཉིད་དུ་སྟོན་ཏེ། [^3970]དེ་ལྟར༌[^3971]ན་ཅིའི་ཕྱིར་འགྲོ༌[^3972]ཞེ་ན། སྨྲས་པ། ཆོས་ཀྱི་དོན་དུ་འགྲོ་ཞེས་བྱ་བ་ཡིན་ཏེ། གང་དུ་འགྲོ་ཞེ་ན། ནགས་སུའོ། །ཇི་ལྟར་འགྲོ་ཞེ་ན། ངེས་པར་རོ། །

[Block 6200]
གལ་ཏེ་འཆི་བདག་འོང་བར་གྱུར་ན་ཡང་། ཇི་ལྟར་ལོག་པར་སྤྱོད་པ༌[^3973]ནི་ཆོས་མ་ཡིན་པའི་བདག་ཉིད་དེ། རྗེས་སུ་གདུངས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
