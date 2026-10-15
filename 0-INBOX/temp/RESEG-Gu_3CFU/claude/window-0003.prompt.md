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
ཕྱི་མ་ནི་བཅུ་རྣམས་ལའོ། །

[Block 107]
རྣམ་པ་གང་གིས་ཤེས༌[^92]ཤེ་ན། ཁས་བླངས་པའི་ཚུལ་གྱིས་ཏེ། འདི་དང་འདི་ལས་བཟློག་པར་བགྱིད་ཅེས་བྱ་བ་ཡིན་གྱི། འདི་དང་འདི་ཁྱེད་ཀྱིས་བྱིན་པ་དེ་ནི་བསྲུང་བར་བགྱི་ཞེས་བྱ་བ་དེ་མ་ཡིན་ནོ། །

[Block 108]
རང་གིས་དགེ་བསྙེན་ཉིད་དུ་ཉེ་བར་བསྒྲུབས་ནས་དགེ་འདུན་ལ་ཞུ་བའི་དགེ་སློང་ལ་གཏད་པར་བྱའོ་ཞེས་བྱ་བ་སྟེ། རང་གིས་ཞེས་བྱ་བ་ནི་སྐབས་འདི་ཉིད་ཀྱི་ཕྱིར་མཁན་པོས་སོ། །

[Block 109]
གང་གི་ཕྱིར་དེ་ནི་རབ་ཏུ་འབྱུང་བ་ལ་སྐབས་བྱས་པའོ། །

[Block 110]
དེ་རང་ཉིད་ཀྱིས་དགེ་བསྙེན་དུ་ཉེ་བར་བསྒྲུབས་ནས་ནི་དགེ་བསྙེན་གྱི་སྡོམ་པ་བྱིན་ནས་སོ། །

[Block 111]
གང་ཞིག་དེ་རབ་ཏུ་འབྱུང་བ༌[^93]ལ་ལྟོས་པ་ལ་དགེ་འདུན་ལ་ཞུ་བའི་དགེ་སློང་དེ་ལ་འདི་ནི་ཞུ་བ་མཛོད་ཅིག་ཅེས་བྱ་བས་གཏད་པར་བྱའོ། །

[Block 112]
དགེ་སློང་དང་འབྲེལ་པས་འདི་བྱ་བ་ཉིད་ནི་སྐྱེས་པས་སོ། །

[Block 113]
འདི་ནི་མཁན་པོ་ཉིད་ཀྱིས་རང་དོན་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་རབ་ཏུ་བསྟན་པའི་དོན་དུ་བདག་གི་དོན་གྱི་ཚིག་གོ། །

[Block 114]
གསོལ་བ་ལ་སོགས་པའི་ལས་ཀྱི་བདག་ཉིད་ཅན་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་བསྙེན་པར་རྫོགས་པ་མ་བྱས་པས་ཀྱང་དགེ་འདུན་ལ་རབ་ཏུ་འབྱུང་བ་ལ་ལྟོས་པ་འདི་ལ་ཞུ་བ་ནི་འགལ་བ༌[^94]མ་ཡིན་ཏེ་ཞེས་བྱ་བའི་རྣམ་པར་རྟོག་པ་འདི་རྣམ་པར་གསལ་བའི༌[^95]དོན་དུ་དགེ་སློང་ལ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 115]
དེ་ལྟར་ཡང་གཞུང་ལས་དེའི་འོག་ཏུ་དགེ་སློང་ལ་གསོལ་བ་གདབ་པར་བྱའོ། །

[Block 116]
གང་ཞིག་འདི་ལ་ཞུ་བར་བྱེད་པས་ཅི་ཞིག་བྱ་ཞེ་ན། ཞུ་བར་བྱེད་པ་པོས་ད༌[^96]ཅི་ཡོངས་སུ་དག་གམ་ཞེས་དྲིས་ནས་དག་ན་ཞུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གཏོད་པར་བྱེད་པའི་མཁན་པོ་ལ་དྲིས་ནས་དག་པར་གྱུར་ན་རབ་ཏུ་འབྱུང་བ༌[^97]ལྟོས་པས་ཞུ་བར་བྱའོ། །

[Block 117]
བཙུན་པ་དགོངས་སུ་གསོལ། མིང་འདི་ཞེས་བགྱི་བ་འདི་རབ་ཏུ་འབྱུང་བ༌[^98]ཉིད་ལ་ལྟོས་པས་གོས་དཀར་པོ་འཛིན་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ཀྱིས་ཞུ་བར་བྱའོ་ཞེས་བྱ་བ་གང་ཞིག༌[^99]གཞན་གྱི་ཚིག་དེ་ནི་གཞན་གྱི་བྱ་བས་འདི་འཇུག་པའི་ཕྱིར་རང་གི་དོན་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 118]
ཇི་ལྟར་འདིར་མཁན་པོས་བུ་དང་འདྲ་བར་འཇུག་པ་ལ་རང་གི་དོན་ཉིད་མ་ཡིན་པ་དེ་བཞིན་དུ་འདི་ལའོ། །

[Block 119]
ཇི་ལྟར་ན་གནས་པའི་དགེ་འདུན་ལ་ཞུ་བར་བྱ་ཞེས་ཤེས་པར་བྱ་ཞེ་ན། ཐམས་ཅད་འདུས་པ་ལ་ཡང་རུང་། གནས་ཁང་སོ་སོ་ན་འཁོད་པ་ལ་ཡང་རུང་ངོ་ཞེས་བྱ་བ་སྨྲས་ཏེ།[^100] སོ་སོར་ཡོངས་སུ་བགྲང་བ་ཉིད་ཀྱིས་ཞེས་བྱ་བ་འདིའི་འགྲེལ་པ་ནི་གནས་ཁང་སོ་སོ་ན་ཞེས་བྱ་བའོ། །

[Block 120]
གང་གི་ཡོངས་སུ་བགྲང་བ་ནི་གནས་ཁང་ཁྱད་པར་རོ། །

[Block 121]
གང་རྣམས་ཀྱི་སྔོན་དུ་ཞུ་བར་བྱེད་པ་དེ་རྣམས་ཀྱི་ཆོ་ག་གང་ཞིག་དེ་བསྟན་པའི་ཕྱིར། ཐམས་ཅད་ཀྱིས་གལ་ཏེ་ཡོངས་སུ་དག་ནའོ། །

[Block 122]
[^101]བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་སྨྲས་ཏེ། གལ་ཏེ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཞེས་བྱ་བའི་དོན་ཏེ། ཞུ་བར་བྱེད་པའི་དུས་ཕྱི་མ་ལ་རབ་ཏུ་འབྱུང་བ༌[^102]ཉིད་ལ་ལྟོས་པའོ།[^103] །མཁན་པོར་གསོལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བླང་བའི་སྔགས་ཀྱིས་མཁན་པོས་འདི་ལ་གཙུག་ཕུད༌[^104]མ་གཏོགས་པ་སྐྲ་དང་ཁ་སྤུ་བྲེག་པར་བྱའོ་ཞེས་བྱ་བའོ། །

[Block 123]
མཁན་པོ་ཉིད་ཀྱིས་ལྷག་པར་གནས་ནས་གང་ཞིག་འབྲེག་མཁན་གྱི་བྱ་བ་དེ༌[^105]ཡང་དག་པར་བསྟན་པའི་དོན་དུ་བྲེག་པར་བྱའོ་ཞེས་བྱ་བ་ནི། བདག་པོའི་དོན་གྱི་ཚིག་གོ། །

[Block 124]
མཁན་པོ་ཉིད་ཀྱིས་འདིར་རང་གིས་བྱའོ་ཞེས་བྱ་བ་འདི་ལྟར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཏེ། བརྒྱུད་ནས་བྱེད་དུ་བཅུག་པ་ནི་བྱེད་དུ་བཅུག་པ་ཡིན་པར་ཡང་ཤེས་པར་བྱ་བ་མ་ཡིན་པའོ།[^106] །དོན་དང་དོན་ཉིད་ཀྱི་ཕྱིར་འཇུག་པའོ། །

[Block 125]
དེ་བས་ན་དོན་བསྒྲུབ་པ༌[^107]ལ་འཇུག་པ་མི་སྣང་བའོ། །

[Block 126]
དེ་ལ་མཁན་པོའི་བསྒོ་བ་ལ་ནི་མི་སྡོད་པར་སྐྲ་དང་ཁ་སྤུ་བྲེགས་པ་གཞན་གྱི་བསྒྲུབ༌[^108]པ་ལ་སླར་མཁན་པོས་འདི་ལ་འཇུག་པར་བྱ་ཞེས་བྱ་བ་ཤེས་པར་བྱ་བ་མ་ཡིན་པའོ།[^109] །གཙུག་ཕུད་མ་གཏོགས་པ་ཞེས་བྱ་བ་ནི་གཙུག་ཕུད་ལས་གཞན་ནོ། །

[Block 127]
ཁ་སྤུ་བྲེག་པ་ལ་ཡང་ཇི་ལྟར་འདི་ལ་གཟུགས་མི་སྡུག་པའི་བློ་དེ་ལྟར་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་འདི་ངེས་པ་ཡིན་ནམ། མ་ཡིན་ཞེས་བྱ་བའི་དྲི་བས་གསོལ་བའི་དོན་དུ་འདི་གཞག་པའོ། །

[Block 128]
གཙུག་ཕུད་བྲེག་གོ་ཞེས་དྲིས་ནས་སྟེར་ན་དེའོ་ཞེས་བྱ་བ་སྟེ། གཙུག་ཕུད་བྲེག་གམ་ཞེས་དྲིས་པར་གྱུར་པའི་རབ་ཏུ་བྱུང་བར་བྱ་བས་གལ་ཏེ་སྟེར་བར་གྱུར་ན་དེ་ནས་སྟེར་བ་ལ་གཙུག་ཕུད་བྲེག་པར་བྱ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་འཇུག་གོ། །

[Block 129]
དེ་ལྟར་སྐྲ་དང་ཁ་སྤུ་བྲེགས་པས་ཁྲུས་བྱའོ་ཞེས་བྱ་བ་ནི་དུས་དང་རྗེས་སུ་མཐུན་པའི་ཆུས་སོ། །

[Block 130]
ཁྲུས་ཀྱི་རྗེས་ཀྱི་དུས་ལ་མཁན་པོས་གོས་ངུར་སྨྲིག་དག༌[^110]སྦྱིན་པར་བྱའོ། །

[Block 131]
དེས་ཀྱང་མཁན་པོའི་རྐང་པ་གཉིས་ལ་གཏུགས་ཏེ་བླང་བར་བྱའོ། །

[Block 132]
དེ་ནས་རང་གི༌[^111]དེ་ལ་མཁན་པོས་བསྐོན་པར་བྱའོ། །

[Block 133]
བསྐོན་པ་ན་ཟ་མ་དང་མ་ནིང་དང་མཚན་མེད་པ་དང་མཚན་གཉིས་པ་ཉིད་ཀྱི་སྐྱོན་ཡོངས་སུ་སྤང་བའི་དོན་དུ་མཚན་མ་ཚོར་བར་བརྟག༌[^112]གོ། །

[Block 134]
གཅེར༌[^113]བུར་བྱས་ནས་ནི་མ་ཡིན་ཏེ་འོན་ཀྱང་མ་ཚོར་བར་རོ། །

[Block 135]
ཇི་ལྟར་འདིས་བདག་གི་མཚན་མ་མཐོང་ངོ་སྙམ་དུ་ཤེས་པར་མི་འགྱུར་བར་རོ། །

[Block 136]
ཁས་བླངས་པས་མཁན་པོའི་ལས་འདིའོ། །

[Block 137]
ཡིད་ཆེས་པའི་དགེ་སློང་གཞན་གྱིས་ཀྱང་བྱས་པས་ནི་གོ་ཆོད་པའོ། །

[Block 138]
བྱས་པ་ཞེས་བྱ་བ་ཉིད་ནི་མཁན་པོ་ཉིད་ཀྱིས་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 139]
སྐྱབས་སུ་འགྲོ་བར་རྩོམ་པས་རབ་ཏུ་འབྱུང་བ་ཉེ་བར་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བདག་མིང་འདི་ཞེས་བགྱི་བ་ཇི་སྲིད་དུ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པ་དེ་ལ། ཇི་སྲིད་དུ་ཚོགས་རྣམས་ཀྱི་མཆོག །ཇི་སྲིད་དུ་རབ་ཏུ་འབྱུང་བ༌[^114]ཉིད་ཀྱི་རྟགས་ཡང་དག་པར་ལེན་ཏོ་ཞེས་བྱ་བའི་སྔགས་འདིས་མཁན་པོས་སྐྱབས་སུ་འགྲོ་བར་བརྩམས་པས་རབ་ཏུ་འབྱུང་བ་ཉེ་བར་བསྒྲུབ་པར་བྱའོ། །

[Block 140]
སྐྱབས་སུ་འགྲོ་བ་དང་པོར་གྱུར་པ་མེད་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 141]
འོ་ན་འདི་ནི་སྡོམ་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་འདི་ལ་སྐྱབས་སུ་འགྲོ་བར་རྩོམ་པ་ཉིད་ཀྱི་དོན་ཅི་ཞིག་ཡིན་ཞེས་བྱ་བ་ཁ་ཅིག་སྨྲ་ན་དེ་ནི་ཡང་དག་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་རབ་ཏུ་བྱུང་བ་ཉིད་ཅེས་བྱ་བ་ནི་ངེས་པར་ཞུགས་པ་ཉིད་ཡོངས་སུ་དོར་བ་སྟེ། ཟག་པ་དང་བཅས་པའི་དངོས་པོ་ཐམས་ཅད་ལ་མངོན་པར་མི་དགའ་བ་དེ་ལ་ངེས་པར་ཞུགས་པའོ། །

[Block 142]
དེ་བས་ན་འཁོར་བ་ལ་རྒྱབ་ཏུ་ཕྱོགས་པ་ནི་ངེས་པར་ཞུགས་པ་ཡོངས་སུ་དོར་བ་མ་ལུས་པའོ། །

[Block 143]
མྱ་ངན་ལས་འདས་པ་ལ་བརྟེན་པ་མེད་པར་འཁོར་བ་ལ་རྒྱབ་ཀྱིས་ཕྱོགས་པ་གྲུབ་པ་མ་ཡིན་ཏེ། དེ་བས་ན་སྡོམ་པ་བཞིན་དུ་འདིར་ཡང་མྱ་ངན་ལས་འདས་པའི་བསམ་པ་རབ་ཏུ་བསྒྲུབ་པར་བྱའོ། །

[Block 144]
དེ་བས་ན་འདིར་ཡང་སྐྱབས་སུ་འགྲོ་བ་རྩོམ་པ་ཉིད་དོ། །

[Block 145]
ཁ་ཅིག་ནི་རབ་ཏུ་བྱུང་བ་ཉིད་ཉེ་བར་བླང་བའི་སྔགས་ལ་རབ་ཏུ་བྱུང་བ་ཉིད་ཀྱི་རྟགས་ཡང་དག་པར་བླང་བར་བགྱི་ཞེས་བྱ་བ་འདིའི་མདུན་དུ་བདག་ནི་དགེ་ཚུལ་དུ་མཁན་པོས་གཟུང་དུ་གསོལ་ཞེས་བྱ་བ་འདོན་པ་ཡིན་ནོ་ཞེ་ན། དེ་ནི་རིགས་པ་མ་ཡིན་ཏེ། རབ་ཏུ་སྐྱེས་པ་ལ་སླར་རབ་ཏུ་སྐྱེས་པ༌[^115]མེད་པ་ཉིད་ཀྱི་ཕྱིར་དང་། ཡང་དག་པར་བླངས་པ་ལ་ཡང་དག་པར་བླང་བ༌[^116]མི་འཐད་པའི་ཕྱིར་དང་། སློབ་དཔོན་གྱིས་སྔགས་ལ་ཡང་གདོན་པར་བྱ་བ་ཉིད་མི་འཐད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
