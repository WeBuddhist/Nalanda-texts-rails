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
[Block 386]
འདུ་ཤེས་ཀྱིས་རབ་ཏུ་ཕྱེ་བ་ནི་གཟུགས་མེད་པ་གསུམ་མོ། །

[Block 387]
འདུ་བྱེད་ཙམ་གྱིས་རབ་ཏུ་ཕྱེ་བ་ནི་སྲིད་པའི་རྩེ་མོ་སྟེ། འདི་དག་ནི་རྣམ་པར་ཤེས་པ་གནས་པ་ཡིན་ལ། དེ་དག་ལ་རྣམ་པར་ཤེས་པ་གནས་སོ་ཞེས་ཕུང་པོའི་གོ་རིམས་ཞིང་དང་ས་བོན་གྱི་གོ་རིམས་ལྟ་བུར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 388]
དེ་ཉིད་ཀྱི་ཕྱིར་ཕུང་པོ་རྣམས་ནི་ལྔ་སྟེ་མི་ཉུང་མི་མང་ངོ་། །གང་གི་ཕྱིར་འདི་དག་ནི་ཆེས་རགས་པ་དང་། ཀུན་ནས་ཉོན་མོངས་པའི་གོ་རིམས་ཀྱི་རྒྱུ་དང་ཟས་དང་ཚོད་མ་ལྟ་བུ་དང་། དེ་དག་གི༌[^151]ཁམས་གཉིས་རབ་ཏུ་ཕྱེ་བའི་གོ་རིམས་ཀྱི་རྒྱུ་དེ་ཉིད་ཀྱི་ཕྱིར༌[^152]ཚོར་བ་དང་འདུ་ཤེས་དག་ནི་འདུ་བྱེད་རྣམས་ལས་ལོགས་ཤིག་ཏུ་ཕུང་པོར་བྱས་སོ། །

[Block 389 [HEADING]]
#### མིག་ལ་སོགས་པའི་ཁམས་དང་སྐྱེ་མཆེད་དྲུག་གི་གོ་རིམས། ^1-2-6-0

[Block 390]
མིག་ལ་སོགས་པའི་ཁམས་དང་སྐྱེ་མཆེད་དྲུག་གི་གོ་རིམས་བརྗོད་པར་བྱ་སྟེ། དེའི་དབང་ཉིད་ཀྱིས༌[^153]ན་དེའི་ཡུལ་དང་རྣམ་པར་ཤེས་པ་རྣམས་ཀྱི་གོ་རིམས་སུ་འགྱུར་རོ། །

[Block 391]
དྲུག་པོ་དེ་དག་ལས།

[Block 392]
ད་ལྟའི་དོན་ཕྱིར་དང་པོར་ལྔ། །མིག་ལ་སོགས་པ་ལྔའི་ཡུལ་ནི་ད་ལྟར་ཡིན་པའི་ཕྱིར་སྔར་སྨོས་སོ། །

[Block 393]
ཡིད་ཀྱི་ཡུལ་མ་ངེས་པ་ཅན་ཡིན་ཏེ། ཁ་ཅིག་གི་ཡུལ་ནི་ད་ལྟར་ཡིན་པ་ནས། ཁ་ཅིག་གི་ཡུལ་ནི་དུས་གསུམ་དང་དུས་མ་ཡིན་པའི་བར་ཡིན་ནོ། །

[Block 394 [VERSE]]
འབྱུང་བ་ལས་གྱུར་དོན་ཕྱིར་བཞི། །
དང་པོར་ཞེས་བྱ་བར་སྙེགས་སོ། །

[Block 395]
ལྔ་རྣམས་ལས་ཀྱང་བཞིར༌[^154]སྔར་སྨོས་པ་ནི་ཡུལ་འབྱུང་བ་ལས་གྱུར་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 396]
ལུས་ཀྱི་ཡུལ་ནི་མ་ངེས་ཏེ། རེས་འགའ་ནི་འབྱུང་བ་དག་ཡིན་ལ། རེས་འགའ་ནི་འབྱུང་བ་ལས་གྱུར་པ་དག་ཡིན་ནོ། །

[Block 397 [VERSE]]
རེས་འགའ་ནི་གཉི་ག་ཡིན་ནོ། །
གཞན་ནི་ཆེས་རིང་མྱུར་འཇུག་ཕྱིར། །

[Block 398]
ལྷག་མ་ནི་ཅི་རིགས་པར་ཆེས་རྒྱང་རིང་བ་དང་མྱུར་བར་འཇུག་པས་གཞན་པས་སྔར་སྨོས་ཏེ། མིག་དང་རྣ་བའི་ཡུལ་རྒྱང་རིང་བའི་ཕྱིར་གཉིས་པས་དེ་དག་སྔར་སྨོས་སོ། །

[Block 399]
དེ་གཉིས་ལས་ཀྱང་མིག་ནི་ཆེས་རྒྱང་རིང་པོ་ལ་འཇུག་སྟེ། ཆུ་ཀླུང༌[^155]རྒྱང་རིང་པོ་ནས་མཐོང་ཡང་དེའི་སྒྲ་མི་ཐོས་པས་དེའི་ཕྱིར་དེ་སྔར་སྨོས་སོ། །

[Block 400]
སྣ་དང་ལྕེ་ནི་རྒྱང་རིང་པོ་ལ་འཇུག་པ་མེད་མོད་ཀྱི། དེ་གཉིས་ལས་ཀྱང་སྣ་ནི་ཆེས་མྱུར་བར་འཇུག་པའི་ཕྱིར་སྔར་སྨོས་ཏེ། ཟས་ལྕེ་དང་མ་ཕྲད་པ་ཉིད་ཀྱི་དྲི་འཛིན་པའི་ཕྱིར་རོ། །

[Block 401]
ཡང་ན་ཇི་ལྟར་གནས་བཞིན་རིམ། །ཡང་ན་ལུས་འདི་ལ་མིག་གི་རྟེན་ནི་དང་པོ་ན་གནས་སོ། །

[Block 402]
དེའི་འོག་ན་ནི་རྣ་བའི་འོ། །

[Block 403]
དེའི་འོག་ན་ནི་སྣའིའོ། །

[Block 404]
དེའི་འོག་ན༌[^156]ནི་ལྕེའིའོ། །

[Block 405]
ལུས་ཀྱི་ནི་ཕལ་ཆེར་དེའི་འོག་ནའོ། །

[Block 406]
ཡིད་ནི་དེ་དག་ལ་བརྟེན་པ༌[^157]དང་ཡུལ་ན་མི་གནས་པའི་ཕྱིར་ཏེ། དེ་དག་གི་གོ་རིམས་ནི་ཇི་ལྟར་གནས་པ་བཞིན་ཡིན་ནོ། །

[Block 407 [HEADING]]
#### གཅིག་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དང་གཅིག་ཆོས་ཀྱི་སྐྱེ་མཆེད། ^1-2-7-0

[Block 408]
ཡང་ཅིའི་ཕྱིར་གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་པའི་སྐྱེ་མཆེད་བཅུ་པོ་དག་ལས་གཅིག་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དུ་བརྗོད་ལ། ཐམས་ཅད་ཀྱང་ཆོས་ཀྱི་རང་བཞིན་ཡིན་ན་གཅིག་ཆོས་ཀྱི་སྐྱེ་མཆེད་ཅེས་བྱ་ཞེ་ན། སྨྲས་པ།

[Block 409 [VERSE]]
བྱེ་བྲག་དོན་དང་གཙོ་བོའི་ཕྱིར། །
ཆོས་མང་བ་དང་མཆོག་བསྡུས་ཕྱིར། །
གཅིག་ནི་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དང་། །
གཅིག་ནི་ཆོས་ཞེས་བྱ་བར་བརྗོད། །

[Block 410]
བྱེ་བྲག་གི་དོན་ཅི་ལྟ༌[^158]བུ་ཞེ་ན། ཅི་ནས་ཀྱང་ཡུལ་དང་ཡུལ་ཅན་ཉིད་དུ་རྣམ་པར་གཞག་པའི་སྒོ་ནས་བཅུ་པོ་འདི་དག་གི༌[^159]སོ་སོར་སྐྱེ་མཆེད་ཉིད་ཡིན་གྱི་སྤྱིར་ནི་མ་ཡིན་ནོ་ཞེས་རྟོགས་པར་བྱ་བ་ཡིན་ལ། མིག་ལ་སོགས་པ་བྱེ་བྲག་ཏུ་བྱས་པ་དག་གིས་ནི་གང་མིག་ལ་སོགས་པར་ནི་མིང་མ་བཏགས་ལ་གཟུགས་ནི་ཡིན་པ་དེ་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དུ་ཤེས་པར་འགྱུར་བས་འདིའི་མིང་གཞན་མ་བརྗོད་དོ། །

[Block 411]
ཡང་ན་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ནི་ཐོགས་པ་དང་བཅས་པ་ཡིན་པའི་ཕྱིར་ལག་པ་ལ་སོགས་པའི་འདུས་ཏེ་རེག་པ་དག་གིས་རེག་ན་གཟུགས་སུ་རུང་བ་དང་། བསྟན་དུ་རུང་བའི་ཕྱིར་ཏེ། འདི་ནི་འདི་ནའོ། །

[Block 412]
ཆེ་གེ་མོ་ཞིག་ནའོ་ཞེས་བརྟག་ཏུ་རུང་བའི་ཕྱིར་རོ། །

[Block 413]
འཇིག་རྟེན་ན་ཡང་དེ་གཟུགས་སོ་ཞེས་གྲགས་ཀྱི་གཞན་དག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 414]
བྱེ་བྲག་གི་དོན་ཉིད་ཀྱིས་གཅིག་ནི་ཆོས་ཀྱི་སྐྱེ་མཆེད་དུ་བཤད་ཀྱི༌[^160]ཐམས་ཅད་ནི་མ་ཡིན་ནོ། །

[Block 415]
གཞན་ཡང་འདིར་ཚོར་བ་ལ་སོགས་པ་ཆོས་མང་པོ་རྣམས་བསྡུས་ཏེ། དེའི་ཕྱིར་ཆོས་ཀྱི་སྒྲར་སྤྱིར་རྗོད་པར༌[^161]བྱེད་དོ། །

[Block 416]
ཆོས་ཀྱི་མཆོག་མྱ་ངན་ལས་འདས་པ༌[^162]དེ་ཡང་དེར༌[^163]བསྡུས་ཏེ་གཞན་དག་ཏུ༌[^164]ནི་མ་ཡིན་ནོ། །

[Block 417]
གཞན་དག་ན་རེ་རྣམ་པ་ཉི་ཤུའི་རིག༌[^165]པའི་ཕྱིར་དང་། ཤའི༌[^166]དང་ལྷའི༌[^167]དང་འཕགས་པའི་ཤེས་རབ་དང་མིག་གསུམ་གྱི་སྤྱོད་ཡུལ་ཡིན་པའི་ཕྱིར་གཅིག་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དུ་བསྟན་ཏོ་ཞེས་ཟེར་རོ། །

[Block 418 [HEADING]]
#### ཕུང་པོ་དང་སྐྱེ་མཆེད་དང་ཁམས་གཞན་དག་བསྡུ་བ། ^1-2-8-0

[Block 419]
མདོ་དག་ལས་ཕུང་པོ་དང་སྐྱེ་མཆེད་དང་ཁམས་ཞེས་བྱ་བ་གཞན་དང་གཞན་དག་ཀྱང་དམིགས་ན། ཅི་དེ་རྣམས་འདི་དག་ཉིད་ཀྱིས་བསྡུས་སམ། འོན་ཏེ་ཐ་དད་པ་ཞིག་ཡིན་པར་རིག་པར་བྱ་ཞེ་ན། འདི་དག་ཉིད་ཀྱིས་བསྡུས་ཀྱི་ཐ་དད་པ་ནི་མེད་དེ་དེ་ལ་རེ་ཞིག །

[Block 420 [HEADING]]
##### ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི། ^1-2-8-1-0

[Block 421 [VERSE]]
ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་དག །
གང་རྣམས་ཐུབ་པས་གསུངས་དེ་དག །
ཚིག་གམ་མིང་ཡིན་དེ་དག་ནི། །
གཟུགས་དང་འདུ་བྱེད་དག་ཏུ་འདུས། །

[Block 422]
གང་དག་གི་ལྟར་ན་སངས་རྒྱས་ཀྱི་གསུང་ཚིག་གི་རང་བཞིན་ཡིན་པ་དེ་དག་གི་ལྟར་ན་དེ་དག་ནི་གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 423]
གང་དག་གི་ལྟར་ན་མིང་གི་རང་བཞིན་ཡིན་པ་དེ་དག་གི་ལྟར་ན་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 424]
ཡང་ཆོས་ཀྱི་ཕུང་པོའི་ཚད་ཇི་ཙམ་ཞེ་ན། ཁ་ཅིག་བསྟན་བཅོས་ཚད་ཅེས་ཟེར། །ཁ་ཅིག་ན་རེ་དེ་ནི་ཆོས་ཀྱི་ཕུང་པོ་ཞེས་བྱ་བ་བསྟན་བཅོས་མངོན་པའི་ཚད་ཙམ་མོ་ཞེས་ཟེར་ཏེ། དེ་ནི་ཤློ་ཀ་དྲུག་སྟོང་ངོ་། །ཡང་གཞན་དག་ན་རེ། ཕུང་པོ་ལ་སོགས་གཏམ་རེ་ཡིན། །ཞེས་ཟེར་ཏེ། ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་དང་། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་དང་། བདེན་པ་དང་། ཟས་དང་། བསམ་གཏན་དང་། ཚད་མེད་པ་དང་། གཟུགས་མེད་པ་དང་། རྣམ་པར་ཐར་པ་དང་། ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་དང་། ཟད་པར་གྱི་སྐྱེ་མཆེད་དང་། བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་དང་། མངོན་པར་ཤེས་པ་དང་། སོ་སོ་ཡང་དག་པར་རིག་པ་དང་། སྨོན་ནས་ཤེས་པ་དང་། ཉོན་མོངས་པ་མེད་པ་ལ་སོགས་པའི་གཏམ་རྒྱུད་རེ་རེ་ནི་ཆོས་ཀྱི་ཕུང་པོའོ༌[^168]ཞེས་ཟེར་རོ། །

[Block 425 [VERSE]]
སྤྱོད་པ་རྣམས་ཀྱི་གཉེན་པོར་ནི། །
ཆོས་ཀྱི་ཕུང་པོ་མཐུན་པར་གསུངས། །
--- END BLOCKS ---
