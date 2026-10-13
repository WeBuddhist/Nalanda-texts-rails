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
སླར་ཡང་ཅི་ཁོ་བོའི་འདོད་པ་རྣམ་པར་ཤེས་པ་ཕྱི་རོལ་ལ་དམིགས་པ་ཡིན་ལ། རྣམ་པར་ཤེས་པ་ཉིད་ཁོ་བོ༌[^112]མི་འདོད་ན། ཅིའི་ཕྱིར་ཕྱི་རོལ་ལ་དམིགས་པར་བྱེད་པ་པོ་ཉིད་ཁོ་བོའི་འདོད་པ་ཡིན། འཇིག་རྟེན་པའི་ཐ་སྙད་ཁོ་བོས་ཁས་བླངས་ལ་དེའི་ཡུལ་དང་རྣམ་པར་ཤེས་པ་ཡང་འཇིག་རྟེན་པས་ཤེས་ཀྱི་ཁོ་བོས་ནི་མ་ཡིན་ནོ། །

[Block 142]
ཁྱོད་ཀྱིས་ཀྱང་ཁོ་བོ་ཅག་དང་འབྲེལ་བའི་འཇིག་རྟེན་པའི་དོན་འདི་སེལ་བར་མི་ནུས་སོ། །

[Block 143]
དེ་ལ་ཅི་འཇིག་རྟེན་པ་ལ་སེམས་དང་སེམས་ལས་བྱུང་བ་དམིགས་པ་དང་བཅས་པ་མ་གྲུབ་པས། དེ་ལས་དམིགས་པས་བསྐྱེད་པའི༌[^113]སེམས་དང་སེམས་ལས་བྱུང་བ་དམིགས་པ་མེད་ན་དེ་མེད་པས་བདག་མེད་ན་ངར་འཛིན་པ་མེད་པར་གྲུབ་བོ། །

[Block 144]
ཁོ་བོས་དེ་ལྟར་ཁས་མ་བླངས་སོ་ཞེ་ན། སླར་ཡང་ཅི་དངོས་པོ་འདི་དག་འཇིག་རྟེན་པ་ལ་མ་གྲུབ་པས་གང་ཞིག་ཁྱོད་ཀྱང་ཁས་མི་ལེན་ནམ། འདི་དག་ནི་འཇིག་རྟེན་པ་ལ་གྲུབ་ལ། འོན་ཀྱང་འཇིག་རྟེན་རྨོངས་པས་ཕྱིན་ཅི་ལོག་ཇི་ལྟ་བ་དེ་ལྟ་བར་འཇུག་པར་འགྱུར་རོ་ཞེས་ཁོ་བོ་སྨྲའོ། །

[Block 145]
དེའི་ཕྱིར་འཇིག་རྟེན་པའི་འདི་དག་ཀྱང་ཁོ་བོས༌[^114]ཁས་མི་ལེན་ནོ་ཞེ་ན། སྨྲས་པ། འདིར་དོན་རྟོགས་པ་པོ་རྣམས་ཀྱི་དོན་རྟོགས་པ་འཛིན་པ༌[^115]ལས་སམ་བསྟན་བཅོས་ལས་འགྱུར་གྲང་། དེ་ལ་རེ་ཞིག་འཇིག་རྟེན་པ་ཁྱོད་ལ་ཚད་མ་མ་ཡིན་ལ། བསྟན་བཅོས་ལས་ཁས༌[^116]བླངས་པའི་དོན་ཀྱང་གཞན་ལ་བསྒྲུབ་པར་ནུས་པ་མེད་ལ། དེའི་ཕྱིར་ཁྱོད་དང་མཚུངས་པའི་སྐྱེ་བོའི་སྒྲའི་རྗེས་སུ་ཁྱོད་འཇུག་པའི༌[^117]རིགས་ཀྱི་མཁས་པ་ནི་མ་ཡིན་ནོ། །

[Block 146]
མཁས་པ་ནི་འཐད་པ་དང་བཅས་པའི་བསྟན་བཅོས་ཀྱི་ཚད་མ་བརྗོད་པས་སམ། འཇིག་རྟེན་པ་ལས་སོ། །

[Block 147]
འཐད་པ་མེད་པ༌[^118]ཚིག་ཙམ་གྱི་བསྟན་བཅོས་ཚད་མར་བྱེད་ན་བསྟན་བཅོས་ཐམས་ཅད་ཚད་མར་འགྱུར་རོ། །

[Block 148]
དེའི་ཕྱིར་ཕྱི་རོལ་གྱི་དམིགས་པ་ལ་མི་ལྟོས་པའི་སེམས་དང་སེམས་ལས་བྱུང་བ་ནི་མེད་དོ། །

[Block 149]
རིགས་པས་དཔྱད་ན་ཕྱི་རོལ་གྱི་དམིགས་པ་མི་སྲིད་ལ། དེའི་ཕྱིར་ཕྱི་རོལ་གྱི་དོན་ལ་མི་ལྟོས་པར་སེམས་དང་སེམས་ལས་བྱུང་བ་ཁོ་ན་ཁས་བླང་བར་བྱའོ་ཞེ་ན། ཇི་ལྟར་ཁྱོད་ཀྱིས༌[^119]དཔྱད་པས་ཕྱི་རོལ་གྱི་དམིགས་པ་མི་སྲིད་ལ། དེ་བཞིན་དུ་ཁོ་བོས་དཔྱད་ན་སེམས་དང་སེམས་ལས་བྱུང་བ་ནི༌[^120]སྲིད་པའི་ཕྱིར། ཕྱི་རོལ་གྱི་དམིགས་པ་བཞིན་དུ་སེམས་དང་སེམས་ལས་བྱུང་བ་ཡོད་པ་ཉིད་རྣམ་པ་ཐམས་ཅད་དུ་གཏང་བར༌[^121]བྱོས་ཤིག །

[Block 150]
སླར་ཡང་གཞན་ཞིག་གིས༌[^122]སྨྲས་པ། རྣམ་པར་ཤེས་པ་ཐམས་ཅད་དམིགས་པ་དང་བཅས་པ་མ་ཡིན་ལ། གལ་ཏེ་ཡང་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་དམིགས་པ་དང་བཅས་པར་འགྱུར་ན། མོ་གཤམ་གྱི་བུ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་མི་འབྱུང་སྟེ། དམིགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 151]
འོ་ན་མོ་གཤམ༌[^123]གྱི་བུ་ཞེས་པའི་མིང་འདི་ཉིད་འདིའི་རྣམ་པར་ཤེས་པའི་དམིགས་པར་ཡོད་པ་མ་ཡིན་ནམ། དེ་ཅི་འདིའི་དམིགས་པ་མེད་དོ་ཞེས་སྨྲ། འདི་ནི་ཡོད་པ་མ་ཡིན་ཏེ། མོ་གཤམ་གྱི་བུའི་སྒྲ་ཐོས་པ་ན་གལ་ཏེ་འདིའི་མིང་ཉིད་མོ་གཤམ་གྱི་བུ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པའི་དམིགས་པར་འགྱུར་ན། དེའི་ཚེ་མོ་གཤམ༌[^124]གྱི་བུ་མེད་དོ་ཞེས་པ་ན་དེ་ཉིད་ཀྱི་མིང་ཡང་མེད་པར་འགྱུར་ན། དེ་ལྟ་བུ་ནི་མ་ཡིན་ནོ། །

[Block 152]
དེའི་ཕྱིར་འདིའི་མིང་ཉིད་ལ་དམིགས་པས་མ་ཡིན་ནོ། །ངེས་པར་རྣམ་པར་ཤེས་པ་འདིའི་དམིགས་པ་ཅི་ཞིག །

[Block 153]
རྣམ་པར་ཤེས་པ་འདི་ནི་དངོས་པོ་མེད་པ་ལ་དམིགས་པའོ། །

[Block 154]
མོ་གཤམ་གྱི་བུ་ནི་དངོས་པོ་མེད་པ་སྟེ། དེ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་འདི་ནི་དངོས་པོ་མེད་པ་ལ་དམིགས་པར་འགྱུར་རོ། །

[Block 155]
སླར་ཁྱོད་ཀྱི་དམིགས་པའི་དོན་ཅི་ཞིག་ཡིན། སྨྲས་པ། རྣམ་པར་ཤེས་པ་ལ་རང་གི་རྣམ་པར༌[^125]གཏོད་པའི་དོན་ནི་དམིགས་པའི་དོན་ཏོ་ཞེ་ན། གལ་ཏེ་དེ་ལྟ༌[^126]ན་མོ་གཤམ་གྱི་བུ་མོ་གཤམ་གྱི་བུ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་ལ་རྣམ་པར༌[^127]གཏོད་དམ་ཅི་གལ་ཏེ་གཏོད་ན་དེའི་ཚེ་དངོས་པོ་མེད་པའི་རྣམ་པ་དང་རྗེས་སུ་འབྲེལ་པའི་རྣམ་པར་ཤེས་པ་དངོས་པོའི་རང་བཞིན་དུ་མི་འཐད་པས་དེ་འདི་དག་ནི་འགའ༌[^128]ལ་འགལ་བའི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་དུས་གཅིག་ལ་གཅིག་ཏུ་མེད་པའི་ཕྱིར་རོ། །

[Block 156]
དངོས་པོ་དང་དངོས་པོ་མེད་པར་འགྱུར་ན་ཡང་། རྣམ་པར་ཤེས་པ་གཉིས་སུ་ཇི་ལྟར་མི་འགྱུར། དེ་དག་མུན་པ་དང་སྣང་བ་དག་གཅིག༌[^129]པ་མེད་པ་བཞིན་ནོ། །

[Block 157]
སྔོན་པོའི་རྣམ་པར་རྟོག་པའི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་སྔོན་པོ་ཡིན་པ་ལྟར། [^130]དངོས་པོ་མེད་པ་རྟོགས་པའི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་དངོས་པོ་མེད་པར༌[^131]རིགས་སོ། །

[Block 158]
དེ་ལྟར༌[^132]ན་དངོས་པོ་མེད་པ་དང་རྣམ་པ་དག་འགལ་བས་འདི་ནི་མོ་གཤམ་གྱི་བུ་བཞིན་དངོས་པོ་ཉིད་དུ་མི་འགྱུར་ཏེ། སྔོན་པོའི་རྣམ་པའི་རྣམ་པར་ཤེས་པ་སྔོན་པོའི་རྣམ་པ་དང་འགལ་བའི་དཀར་པོ་བཞིན་ནོ། །

[Block 159]
དམིགས་པ་དང་རྣམ་པས་དབེན་པའི་རྣམ་པར་ཤེས་པ་མེད་པ༌[^133]ན་གང་ཞིག་ངོ་བོ་ཐ་དད་པའི་རྣམ་པར་འཇོག་པར་བྱེད། ཅི་ངེས་པར་དམིགས་པའི་རྣམ་པ་ཙམ་ཞིག་ཁོ་ན་རྣམ་པར་ཤེས་པའམ། གལ་ཏེ་དེ་ལྟར་གྱུར་ན་དེའི་ཚེ་དམིགས་པ་ཉིད་རྣམ་པར༌[^134]ཤེས་པར་འགྱུར་རོ། །

[Block 160]
དེ་ནི་དམིགས་པ་ཁོ་ན་རྣམ་པར་ཤེས་པ་མ་ཡིན་ལ། འོན་ཀྱང་དམིགས་པའི་རྣམ་པ་ཡོངས་སུ་གཅོད་པའི་རང་བཞིན་ནོ། །

[Block 161]
དེ་ཉིད་ཀྱིས་ན་རྣམ་པར་ཤེས་པ་དང་དམིགས་པ་དག་རྣམ་པ་མཚུངས་མོད་ཀྱི། དམིགས་པ་ནི་རྣམ་པར་ཤེས་པ་མ་ཡིན་ཏེ། ཡོངས་སུ་གཅད་པར༌[^135]བྱ་བའི་རང་བཞིན་ཡིན་པ་དང་། ཡོངས་སུ་གཅོད་པ་པོ་མ་ཡིན་པའི་ཕྱིར། དམིགས་པར་བྱེད་པ་པོ་ཡང་དམིགས་པ་མ་ཡིན་ཏེ། ཡོངས་སུ་གཅད་པར༌[^136]བྱ་བའི་རང་བཞིན་མ་ཡིན་པའི་ཕྱིར་དང་། ཡོངས་སུ་གཅོད་པའི་རང་བཞིན་གྱི་ཕྱིར་རོ། །

[Block 162]
དེའི་ཕྱིར་དམིགས་པའི་རྣམ་པ་ཙམ་ནི་རྣམ་པར་ཤེས་པ་མ་ཡིན་ནོ། །

[Block 163]
དམིགས་པའི་རྣམ་པར་ཤེས༌[^137]པ་ལས་ཐ་དད་པ་ཡང་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་དམིགས་པའི་རྣམ་པ་ལས་ཐ་དད་པའི་རྣམ་པར་ཤེས་པའི་ངོ་བོ་མེད་དོ། །

[Block 164]
དེའི་ཕྱིར་དངོས་པོ་མེད་པ་རྗེས་སུ་བྱེད་པས་བསྐྱེད་པའི་རྣམ་པར་ཤེས་པ་ནི་དངོས་པོ་མེད་པ་དང་རྣམ་པ་དག་འགལ་བས་དངོས་པོ་ལས་ལོག༌[^138]ནས་རྣམ་པར་ཤེས་པ་དངོས་པོ་མེད་པར་འགྱུར་རོ། །

[Block 165]
རྣམ་པར་ཤེས་པ་དངོས་པོ་མེད་པ༌[^139]ན་ཡང་མོ་གཤམ་གྱི་བུ་ནི་དངོས་པོ་མེད་པའོ་ཞེས་ཇི་སྐད་བརྗོད་དོ།[^140] །གཞན་ཡང་རྣམ་པར་ཤེས་པ་འདི་ནི་སྐྱེ་བ་ལས་སྔོན་རོལ་དུ་ཅིའི་ངོ་བོ་ཡང་མ་ཡིན་ལ། དེ་ཡང་ཡུལ་གྱི་རྣམ་པ་མ་བཟུང་བས༌[^141]སྐྱེ་བ་ཐོབ་པར་མི་བྱེད་དོ། །

[Block 166]
དེའི་ཚེ་ཅིའི་ངོ་བོ་ཡང་མ་ཡིན་པ་འདི༌[^142]ལ་འཛིན་པས་སྐྱེ་བ་བསྒྲུབ་པར་བྱོས་ཤིག །དངོས་པོ་མེད་པ་ལ་དམིགས་པས་དངོས་པོ་མེད་པའི་རྣམ་པ་ཐོབ་པ་ནི་སྐྱེ་བ་དང་ཤིན་ཏུ་འགལ་བའི་གནས་སྐབས་ཐོབ་པར་འགྱུར་ལ། མ་སྐྱེས་པས་དངོས་པོ་མེད་པ་ལ་འཛིན་པར་རྟོགས་པ༌[^143]ཡང་རིགས་པ༌[^144]མ་ཡིན་ནོ། །

[Block 167]
ཡང་ན་ངེས་པར༌[^145]འདིས་དངོས་པོ་མེད་པ་ལ་དམིགས་པ་ཉིད་དུ་རྟོག་པར་བྱེད་ན། དེའི་སྐྱེ་བ་ལས་སྔ་རོལ་གྱི་གནས་སྐབས་ཉིད་ལ་བརྟག་པར་བྱ་ན། མ་སྐྱེས་པའི་གནས་སྐབས་སུ་དངོས་པོ་མེད་པ་དང་རྣམ་པ་འགལ་བའི་ཕྱིར་རོ། །

[Block 168]
ཡང་ན་གནས་སྐབས་དེ་ན་དམིགས་པ་ལ་འཛིན་པར་བྱེད༌[^146]ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་དངོས་པོ་མེད་པ་ལ་དམིགས་པ་པོ་ཉིད་ནི་མི་འདོད་ལ། སྨོས་པའི་སྐྱོན་ཡོད་པའི་ཕྱིར་ན་གནས་སྐབས་གཞན་ཡང་ཐོབ་པ་པ༌[^147]མ་ཡིན་ནོ། །

[Block 169]
གལ་ཏེ་ཡང་མོ་གཤམ་གྱི་བུ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པས་དངོས་པོ་མང་པོ༌[^148]ལ་དམིགས་པར་འགྱུར་ན། དེ་ལྟ་ན་སྔོན་པོའི་སྒྲ་ལ་མ་ལྟོས་པར་སྔོན་པོའི་རྣམ་པའི་རྣམ་པར་ཤེས་པ་བཞིན་མོ་གཤམ་གྱི་བུའི་སྒྲ་ལ་མ་ལྟོས་པར་དོན་རྟོགས་ལ་རག་ན་རྟོགས་པ་ནི་མེད་དོ། །

[Block 170]
རྒྱུ་མཚན་གྱི་སྒོ་ཅན་གྱི་རྣམ་པར་ཤེས་པ་དེ་ནི་རྒྱུ་མཚན་མེད་པར་འཇུག་པར་མི་ནུས་སོ། །

[Block 171]
གལ་ཏེ་རྒྱུ་མཚན་ལས་གཞན༌[^149]ཡང་རྣམ་པར་ཤེས་པ་འཇུག་ན། ཕུང་པོ་ལྷག་མ་མེད་པའི་མྱ་ངན་ལས་འདས་པ་ལ་ཡང་འཇུག་པར་འགྱུར་རོ། །

[Block 172]
སྐྱེ་བ་ལོག་པས་མི་འཇུག་གོ་ཞེ་ན། མཚན་མ་མེད་པ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་སྐྱེ་བ་ལྡོག་པར་མི་འགྱུར་རོ། །

[Block 173]
ཉོན་མོངས་པ་ལོག་ན་ལས་ལྡོག་པར་འགྱུར་བས་སྐྱེ་བ་མི་ལེན་ནོ་ཞེ་ན། གལ་ཏེ་ལས་དང་ཉོན་མོངས་པའི་རྒྱུ་ཅན་གྱི་རྣམ་པར་ཤེས་པ་དེ་ལྟར་མ་གྱུར་ཀྱང་། ཟག་པ་མེད་པའི་རྣམ་པར་ཤེས་པ་མྱ་ངན་ལས་འདས་པའི་དམིགས་པ་ལ་རྟག་ཏུ་འཇུག་པར་འགྱུར་རོ། །

[Block 174]
རིགས་པས་ནི་གང་ཞིག་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པ་ལ་མཚན་མ་འགའ་ཡང་མི་དམིགས་ལ་མཚན་མ་མེད་པས་རྣམ་པར་ཤེས་པ་མི་འཇུག་གོ་ཞེས་བྱའོ། །

[Block 175]
དེ་ཉིད་ཀྱིས༌[^150]འདིར་སྟོང་པ་ཉིད་དུ་སྨྲ་བས་ཆོས་ཐམས་ཅད་སེལ་བ་ལ་རྗེས་སུ་སྒྲུབ་པར་བྱེད་ལ། ཆོས་ཐམས་ཅད་དངོས་པོ༌[^151]མེད་པའི་ངོ་བོ་ཉིད་ལ་མཚན་མ་མི་དམིགས་པས་རྣམ་པར་ཤེས་པ་ལྡོག་གོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 176]
དེ་སྐད་དུ་ཡང་།

[Block 177 [VERSE]]
འཕགས་པས་བརྟེན་པ་འདི་ལྟ་བུ། །
དངོས་པོས་རྟོགས་པ་མ་ཡིན་ཞིང་། །
རྒྱུ་མཚན་མེད་པས༌[^152]རྣམ་ཤེས་ནི། །
ནམ་ཡང་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 178]
འཕགས་པ་ལྷས་ཀྱང་གསུངས་པ།

[Block 179 [VERSE]]
སྲིད་པའི་ས་བོན་རྣམ་པར་ཤེས། །
ཡུལ་ནི་དེ་ཡི་སྤྱོད་ཡུལ་ལ། །
མཐོང་བའི་ཡུལ་རྣམས་བདག་མེད་ཕྱིར། །
སྲིད་པའི་ས་བོན་འགག་པར་འགྱུར། །

[Block 180]
ཞེས་སོ། །
--- END BLOCKS ---
