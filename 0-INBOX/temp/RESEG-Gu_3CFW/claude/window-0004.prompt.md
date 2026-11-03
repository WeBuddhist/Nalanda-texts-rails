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
ལན་གསུམ་བཟླས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་ཞག༌[^139]ལན་གསུམ་དུ་བཟླས་པས་ཤེ་ན། དེའི་ཕྱིར་གདིང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཏིང་ངོ་ཞེས་བྱ་བའི་སྔགས་འདི་མཚོན་པ་ཙམ་མོ། །

[Block 142]
དགེ་སློང་རེ་རེའི་མདུན་དུ་འདུག་སྟེ་བཏིང་ངོ་ཞེས་གོ༌[^140]བར་བྱ་བ་ནི་དགེ་སློང་དགེ་སློང་གི་མདུན་དུ་འདུག་སྟེ་བཏིང་ངོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་འདི་ཡང་སྔགས་ཀྱི་མཚོན་པ་ཙམ་ཡིན་ནོ། །

[Block 143]
ཅིའི་ཕྱིར་ཡང་དེ་གདིང་བ༌[^141]ལྟར་ལྷན་ཅིག་ཉིད་ཀྱིས་དགེ་འདུན་ལ་ཞུ་བར་མི་བྱ་ཞེ་ན། བྱེ་བྲག་ཏུ་ཆེར་འབྱུང་བ་ཉིད་གྲུབ་པ་ཡོད་མོད་ཅེས་བྱ་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 144]
གཞན་གྱིས་ནི་ལེགས་པར་བཏིང་ངོ་། །ཤིན་ཏུ་བཏིང༌[^142]ངོ་། །འདི་ལ་རྙེད་པ་དང་ཕན་ཡོན་གང་ཡོད་པའི༌[^143]བདག་གི་ཡིན་ནོ་ཞེས་སོ་ཞེས་བྱ་བ་ནི་གང་གི་མདུན་དུ་གནས་པའི་གདིང་བ་པོས་བཏིང་ངོ་ཞེས་བྱ་བ་ཞུས་པ་དེ་ནི་འདིར་གཞན་ནོ། །

[Block 145]
འདི་ལ་རྗེས་སུ་ཡི་རང་བ་ནི་ཉམས་སུ་མྱོང་བ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སོ་སོར་ཉམས་སུ་མྱོང་བ་དེ་ནི་བཏིང་བའི་བྱེད་པ་འདི་བསྐྱེད་པ་ཉིད་དེ།[^144] དེ་བཞིན་དུ་སོ་སོར་ཉམས་སུ་མྱོང་བར་མ་བྱས་པ་ཉིད་འཐོབ་སྟེ། འདི་ལ་རྗེས་སུ་ཡི་རང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 146]
འདིར་གཞུང་ནི་མ་མོ་ལས།

[Block 147]
དེ་ཐོས་ནས་ལེགས་པར་བཏིང་ངོ་། །ཤིན་ཏུ་བཏིང་ངོ་ཞེས་རྗེས་སུ་ཡི་རང་བར་བྱེད་པ་དེ་དག་གིས་ཀྱང་གཏན་པ་བཏིང་བར་བརྗོད་པར་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 148]
གང་གིས་དེའི་རྗེས་སུ་ཡི་རང་བར་བྱེད་པ་དེ་ནི་ལས་ཉམས་སུ་མྱོང་བ་དང་འདྲ་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་མངོན་སུམ་དུ་གྱུར་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་བཏིང་བའི་ཕྱིར་ཚོགས་པ་བྱིན་པས་སོ༌[^145]ཞེས་དོན་གྱིས་ཤེས་པའོ། །

[Block 149]
གདིང་བ་པོའི་ཕྱིར་བཏིང་བའི་ཆོས་གོས་དེ་ཇི་ལྟར་ཡོངས་སུ་བརྐྱང་བའི་ཆོ་ག་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དུས་དུས་སུ་བསང་བར༌[^146]བྱ་བསྲང་བར་བྱ་སྤྲུག་པར་བྱའོ། །

[Block 150]
ཁྱིམ་དུ་བ་ཅན་དང་རྡུལ་ཅན་དུ་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 151]
རྒྱལ་པོའི་ཕོ་བྲང་དུ་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 152]
དེ་དང་བྲལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་དང་ཞེས་བྱ་བ་ནི་ཆོས་གོས་སྲ་བརྐྱང་ངོ་། །ཁྱེར་ཏེ་གཞན་དུ་འགྲོ་བར་མི་བྱའོ། །

[Block 153]
མི་གཙང་བའི༌[^147]སྐྱབས་སུ་འཇུག་པར་མི་བྱའོ། །

[Block 154]
བླ་གབ༌[^148]མེད་པར་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་དག་གཉིས་ཀ་ལ་ཡང་ཁྱེར་ཏེ་ཞེས་བྱ་བར་སྦྱར་བའི་ཚིག་གོ། །

[Block 155]
གང་དུ་དེ་ཁྱེར་ཏེ་འགྲོ་བ་དང་གནས་པ་བཀག་པ་དེར་དེ་ལས་བཞག་པ་ཡང་བཀག་པར་ཤེས་པར་བྱའོ། །

[Block 156]
འདིང་བར༌[^149]བྱེད་པ་པོ་ལས༌[^150]གཞན་གྱིས་གཞག་པ་དང་། འཆང་བ་དང་ཁྱེར་བར་མི་བྱའོ་ཞེས་བྱ་བ་དེ་ཡང་འདིས་བྱས་པ་རིག་པར་བྱའོ། །

[Block 157]
གདིང་བ་དེ་ཇི་ལྟར་བརྐྱང་བ་བཤད་ཟིན་ཏོ། །

[Block 158]
[^151]

[Block 159]
ད་ནི་དབྱུང་བ་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དབྱུང་བ་ནི་རྣམ་པ་གཉིས་ཏེ། རང་འཇུག་པ་དང་བྲལ་བ༌[^152]དང་བཅོས་མའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་དབྱུང་བར་གྱུར་པ་ན་རང་འཇུག་པ་སྟེ། གཏན་པ༌[^153]དབྱུང་བ་འགྲུབ་པར་འགྱུར་བ་དེ་རང་ཉིད་ཀྱིས་བྱེད་རྒྱུ་མེད་པར་འཇུག་པར་ཉེ་བར་འགྲོ་བཞིན་པའོ། །

[Block 160]
འཇུག་པ་ཇི་ལྟར་འགྲུབ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རང་འཇུག་པ་དང་འབྲལ་བ་ནི་གཏན་པས་མཚམས་གཞན་དུ་ཕྱིན་པ་དང་། བྱིན་གྱིས་རློབ་པར་བྱེད་པ་མེད་པར་མཚམས་ཀྱི་ནང་དུ་སྐྱ་རེངས་འཆར་བ་དང་། དེའི་དཀྱིལ་འཁོར་གྱི་ཁོངས་སུ་གཏོགས་པ་འཆད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་སྐབས༌[^154]གསུམ་པོ་འདི་དག་ལ་འབྱུང་སྟེ། གཏན་པ་མཚམས་ཀྱི་གནས་གཞན་དུ་ཕྱིན་པ་དང་། མཚམས་གང་དུ་དེ་བཏིང་བའི་མཚམས་དེར་བྱིན་གྱིས་རློབ་པར་བྱེད་པའི་དགེ་སློང་ཐམས་ཅད་མ་ལུས་པ་མེད་པ་དེར་སྐྱ་རེངས་ཤར་བ་དང་། བྱིན་གྱིས་རློབ་པར༌[^155]བྱེད་པའི་དགེ་འདུན་གྱི་མཚམས་ཀྱི་དཀྱིལ་འཁོར་གྱི་ཁོངས་སུ་གཏོགས་པ་དེ་དག་གང་ལ་རྒྱུན་ཆད་པའི་གནས་སྐབས་ནའོ། །

[Block 161]
དབྱར་གྱི་གནས་ཀྱི་རྗེས་སུ་འཇུག་པར་གྱུར་པའི་གཏན་པ་གདིང་བ༌[^156]གང་ཡིན་པའོ། །

[Block 162]
གང་གི་ཕྱིར་ཇི་ལྟར་དེའི་ཞིང་ལས་གཞན་པའི་གནས་སུ་མི་འབྱུང་བ༌[^157]དེ་བཞིན་དུ་དབྱུང་བ་ཡང་ཞིང་གཞན་དུ་གནས་པ་ཉིད་ན༌[^158]འཇིག་པར་འགྱུར་བའོ། །

[Block 163]
དེ་ལས་ཐམས་ཅད་ལ་བག་ཡངས་སུ་གནས་པ་གང་ཡིན་པ་དེ་ཉིད་དང་། དེའི་ཕྱིར་བྱིན་གྱིས་རློབ་པར་བྱེད་པ་མེད་པར་འདི་ལ་རྒྱུན་གཅོད་པར་བྱེད་པ་དེ་ལ་འབྲལ་བའི་སྤང་བ་ཉིད་དེར་ཞིང་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་ཇི་ལྟར་མི་འབྱུང་བ་དེ་བཞིན་དུ་འཇིག་པའོ། །

[Block 164]
དེ་རྣམས་ལ་འདིའི་རྒྱས་པ་ཉིད་གང་ཡིན་པ་དེ་ལ་ཡང་དེ་རྣམས་ལ་འདི་འཇིག་པ་སྟེ། གང་ཞིག་དཀྱིལ་འཁོར་གྱི་ཁོངས་སུ་གཏོགས་པ་དེས་རྣམ་པར་རྒྱུན་ཆད་པའོ། །

[Block 165]
དེའི་ཕྱིར་མ་ལྟ་བུའི་ཚིག་དྲུག་ནི་སྦྱོར་བས་འགྲོ་བ་དང་། ངེས་པར་འབྱེད་པ་དང་། མཐར་ཐུག་པར་གྱུར་པ་དང་། ཞིག་པར་གྱུར་པ་དང་། བསམ་པའི་རྒྱུན་ཆད་པ་དང་། མཚམས་ལས་འདའ་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དག་ནི་དེའི༌[^159]དཀྱིལ་འཁོར་གྱི་ཁོངས་སུ་གཏོགས་པ་ཆད་པ་ཞེས་བྱ་བ་དེའི་བྱེ་བྲག་ཏུ་བཤད་པར་གྱུར་པ་དག་ཡིན་ནོ། །

[Block 166]
ད་ནི་དེ་བཤད་པར་བྱ་སྟེ་དེའི་ཕྱིར་དེ་ལ་དེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཟག་གང་དེ་རྣམ་པར་རྒྱུན་ཆད་པའི་རྒྱུ་མཚན་སྤྱོད་པ་བྱེད་པ་དེ་བས་ན་འདིར་དེ་ལ་དེའི་དཀྱིལ་འཁོར་གྱི་ཁོངས་སུ་གཏོགས་པ་རྣམ་པར་རྒྱུན་ཆད་པ་ལ་སོ་སོར་དབྱུང་བ་ཡང་དག་པར་གནས་པའོ། །

[Block 167]
དགེ་འདུན་ཐམས་ཅད་ལ་ནི་དེ་རྣམ་པར་མི་གཞག་སྟེ་དེ་ལྟར༌[^160]སྔ་མ་རྣམས་ལའོ། །

[Block 168]
དེའི་ཕྱིར་མཚམས༌[^161]འདས་པ་ན་དེ་འགྲུབ་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཞེས་བྱ་བ་ནི་རྣམ་པར་འཆད༌[^162]པའོ། །ཅི་གང་ཡང་རུང་བས་མཚམས་ལས་འདས་ན་འམ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཕྱིར་ཕྱིར་མི་འོང་བའི་སེམས་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡང་ཕྱིར་འོང་བར་བྱའོ་སྙམ་དུ་གནས་པའི་སེམས་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 169]
མཚམས་ཀྱི་ཕྱི་རོལ་དུ་དེ་སྐྱེས་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོན་པ་ཉིད་ན་ཕྱིར་མི་འོང་བར་ངེས་པའི་སེམས་དེ་སྐྱེས་ན་ཡང་། དེའི་ཚེ་རྣམ་པར་འཆད་པར་འགྱུར་བ་འདི་འགྲུབ་པའོ། །

[Block 170]
ཆོས་གོས་བྱ་བའི་བསམ་པས་རྗེས་སུ་འབྲེལ་བ་མེད་ན་དེའི་ཚེ་ཉིད་ནའོ། །

[Block 171]
ཡོད་ན་བྱེད་པར་འགྱུར་པ་ཉིད་ཆད་ནའོ། །

[Block 172]
ཆོས་གོས་བྱའོ༌[^163]སྙམ་པའི་བསམ་པ་ཡོད་ནའོ། །

[Block 173]
དཀྱིལ་འཁོར་དེ་དང་འབྲེལ་བར་གྱུར་པ་དང་། ལྷག་མ་དང་བཅས་པར་གྱུར་པ་དང་། རྣམ་པར་ཆད་པ་ལ་ཡོངས་སུ་མ་བཏང་བར་གྱུར་པའོ། །

[Block 174]
གལ་ཏེ་འདིས་འབྲེལ་པ་ལ་རྗེས་སུ་འགྲོ་བ་ཉིད་གཅིག་པར་གྱུར་པ༌[^164]མེད་པར་གྱུར་པ་དེ་ཉིད་ཀྱི་ཚེ། མཚམས་ལས་འདའ་བར༌[^165]བྱེད་པས་སླར་མི་འོང་བའི་སེམས་སྐྱེས་པའི་དུས་དག་ཉིད་དུ་རྣམ་པར་འཆད་པར་འགྱུར་བ་དེ་འགྲུབ་བོ། །

[Block 175]
འོན་ཏེ་མེད་པར་གྱུར་ན་གང་གི་ཚེ་ཆོས་གོས་བྱ་བའི་བསམ་པས་རྗེས་སུ་འབྲེལ་པ་ཆད་པར༌[^166]གྱུར་པ་དེའི་ཚེ། རྣམ་པར༌[^167]ཆད་པར་གྱུར་པ་དེ་རྗེས་སུ་འགྲུབ་པར་འགྱུར་རམ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཕྱིར་ཕྱིར་འོང༌[^168]ན་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཏན་པ་བཏིང་བའི་མཚམས་སུ་ཕྱིར་འོང༌[^169]ན་ཡང་ཆོས་གོས་བྱེད་པར་འགྱུར་བའི་བསམ་པ་ཉིད་རྒྱུན་ཆད་པར་གྱུར་ན་དེའི་ཚེ་རྣམ་པར་ཆད་པར་འགྱུར་རོ། །

[Block 176]
ཕྱིར༌[^170]འོངས་ན་ཡང་རྣམ་པར་ཆད་པར༌[^171]འདི་ཞེས་བྱ་བ་དེའི་ཕྱིར་དབྱུང་བས་འགྲུབ་པར་མི་བྱའོ་སྙམ་དུ་འགའ་ཞིག་འདོད་པར་འགྱུར་བ་དེའི་དོན་དུ་མདོ་འདི་ཡིན་ནོ། །

[Block 177]
ཕྱིར་འོངས་པ་ཉིད་ལ་ཡང་བྱེད་པར་འགྱུར་བ་ཉིད་ཆད་ནའོ་ཞེས་གང་སྨོས་པ་དེ་ལ་དབྱུང་བ༌[^172]ཉིད་ཡོད་པར་འགྱུར་རོ། །

[Block 178]
བྱེད་པར་འགྱུར་བའི་མཐར་ཐུག་པ་དང་། བརྩམས་པ་ཞིག་པ་དང་། བསམ་པའི་རྒྱུན་ཆད་པ་གསུམ་ལ་དེ་གནས་སོ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་བྱའོ་སྙམ་དུ་བསམས་པ་གང་ཡིན་པ་དེ་མཐར་ཐུག་པར་འགྱུར་བ་སྟེ། དེའི་རེ་བ་ཆད་པ་དང་། བརྩམས་པ་ཞིག་པར་གྱུར་བ་དང་བསམ་པའི་རྒྱུན་ཆད་པར་གྱུར་པ་ཞེས་བྱ་བ་གསུམ་པོ་དེ་ལ་བྱེད་བཞིན་པ་ཉིད་དུ་དེ་ལ་རྣམ་པར་ཆད་པ་གནས་པའོ། །

[Block 179]
ཡིད་གཉིས་ནི་ངེས་པས་འབྱིན་པར་བྱེད་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་ཕྱིར་མི་འོངས་བའི༌[^173]སེམས་ཀྱི་བདག་ཉིད་ཅན་གཏན་པ༌[^174]དབྱུང་བ་སྒྲུབ་པར་བྱེད་པའི་ངེས་པར་སྨོས་པ་དེ་དང་འདྲ་བར་ཡིད་གཉིས་ནི་ཅི་ཞིག་འོང་བར་བྱ་བའམ། འོན་ཏེ་ཕྱིར་འོང་བར་མི་བྱ་སྙམ་པ་དེ་ལྟ་བུའི་སེམས་གཅིག་ཏུ་མ་ངེས་པར་མཚམས་ལས་འདའ་ཞིང་འགྲོ་བ་དང་། མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོན་པ་ན་དེ་ལྟ་བུའི་སེམས་བསྐྱེད་པས་ཀྱང་རྣམ་པར་ཆད་པ་འགྲུབ་པར་འགྱུར༌[^175]རོ། །

[Block 180]
ཇི་ལྟར་འབྲེལ་བ་མེད་པ་ལ་རབ་ཏུ་དབྱེ་བར་གྱུར་པར༌[^176]འདི་ལ་ཆོས་གོས་བྱའོ་སྙམ་པའི་ངེས་པ་གང་ཡིན་པ་འབྲེལ་བ་མེད་པར་དབྱུང་བ་འགྲུབ་པར་བྱེད་པ་མ་གསུངས་པ་དེ་བཞིན་དུ། འདི་ལྟ་བུའི་བློ་ཅི་ཆོས་གོས་བྱ་བའམ་འོན་ཏེ་ཆོས་གོས་མི་བྱ་སྙམ་དུ་དེ་ལྟ་བུའི་སེམས་གཅིག་ཏུ་མ་ངེས་པས་མཚམས་ལས་འདའ་ཞིང་འགྲོ་བ་དང་། མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོན་པ་ན་དེ་ལྟ་བུའི་སེམས་སྐྱེས་པས་ཀྱང་ཆོས་གོས་བྱ་བའི་བསམ་པས་འབྲེལ་བ་མེད་པར་འགྲུབ་པར་འགྱུར་རོ༌[^177]ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
