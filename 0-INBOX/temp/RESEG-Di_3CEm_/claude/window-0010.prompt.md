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
[Block 351]
ཏིང་འཛིན༌[^205]སྟོབས་ཞེས་བྱ་བ་ནི་སྟོབས་དང་བྱེད་པའི་ཏིང་ངེ་འཛིན་ཏེ༌[^206]བསམ་གཏན་ནོ། །

[Block 352]
དེའི་མཐུས་འགྲོ་བ་ཐམས་ཅད་ཀྱི༌[^207]དོན་བྱ་བའི་ཕྱིར་མངོན་པར་ཤེས་པ་ལ་སོགས་པའི་ཡོན་ཏན་སྡུད་པ་ལ་མི་ཐོགས་པ་དེ་ནི་ཏིང་ངེ་འཛིན་གྱི་སྟོབས་སོ། །

[Block 353]
བྱང་ཆུབ་སྟོབས་རྣམས་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་པ་སྟེ། དེ་ཐོབ་པར་བྱེད་པ་ནི་སྟོབས་སོ། །

[Block 354]
ཡང་དག་སྒྲུབ་པར༌[^208]བྱེད་ཅེས་བྱ་བ་ནི་དེའི་ཚོགས་སྒྲུབ་པའོ། །

[Block 355 [HEADING]]
#### གཉེན་པོ། ^2-8-13-0

[Block 356]
གཉེན་པོ་སྟེ་རྣམ་པ་བཅུ་གསུམ་པའོ། །

[Block 357]
དེ་ཡང་མི་མཐུན་པའི་ཕྱོགས༌[^209]ལས་དང་ཉོན་མོངས་པ་དང་བདུད་ཀྱི་སྟོབས་རྣམས༌[^210]འཇོམས་པ་སྟེ་རྣམ་པ་གསུམ་མོ། །དེ་ཡང་གང་ཞེ་ན། ལས་ཀྱི་སྟོབས་རྣམས་ཡོངས་སུ་དག་བྱེད་ཅིང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དགེ་བ་དང་མི་དགེ་བ་དང་མི་གཡོ་བའི་ལས་རྣམས་དམིགས་ཀྱིས་མ༌[^211]ཕྱེ་བས་ན་ལས་དེ་ཡང་རྣམ་པ་གསུམ་མོ། །

[Block 358]
དེ་ལ་མི་དགེ་བའི་ལས་ཀྱིས་གདོན་མི་ཟ་བར་མྱོང་བར་གྱུར་པ་ནི་ངན་སོང་གསུམ་དུ་འབྲས་བུ་སྨིན་པར་འགྱུར་བའི་སྟོབས་ཏེ། དེ་སྦྱོང་བ་ནི་སྨན་པ་ལ་སོགས་པའི་མཐུས་སྐྱུགས་པ་ལྟ་བུ་སྟེ། འདི་སྐད་དུ།

[Block 359 [VERSE]]
མ་རུང་བ༌[^212]ཡི་ལས་བྱས་པ། །
བདག་གིས་འགྱོད་པས་བསྲབས༌[^213]པར་འགྱུར། །
བཤགས་ནས་བསྡམས་པ་བྱས་ན༌[^214]ནི། །
དེ་དག་རྩ་ནས་འདོན་པར༌[^215]བཤད། །

[Block 360]
གཉེན་པོའི་སྟོབས་ཀྱིས་ཀྱང་ཀུན་དུ་འབྱུང་བར་བྱེད་དེ།[^216] དཔེར་ན་མཛའ་བོའི་བུ་མོས་མ་ལ་བརྙས་པའི་རྒྱུས༌[^217]མི་དགེ་བའི་ལས་ནི་ཞིང་གི༌[^218]ཁྱད་པར་གྱིས་ཚེ་འདི་ཉིད་ལ་འབྲས་བུ་རྣམ་པར་སྨིན་པར་གྱུར་ཀྱང་འབྲས་བུ༌[^219]ཅུང་ཞིག་སྨིན་ནས་དེའི་བསམ་པའི་ཁྱད་པར་གྱིས་སེམས་ཅན་གྱི་དོན་དུ་སྨོན་ལམ་དང་སེམས་བསྐྱེད་པས་མ་ལུས་པར་ཤིན་དུ་རྩ་བ་ནས་ཕྱུང་ནས་བཅོམ་མོ། །

[Block 361]
དེ་ལ་སེམས་ཅན་གྱི་དོན་དུ་སྨོན་ལམ་དང་སེམས་བསྐྱེད་པ་ཇི་ལྟར༌[^220]ཞེ་ན། སྨྲས་པ། འདི་ལྟར་གང་འགྲོ་བའི་སེམས་ཅན་ཐམས་ཅད་ཀྱིས་འདི་ལྟར་བདག་བཞིན་དུ་མ་ལ་བརྙས་པའི་ལས་བྱས་པ་དེ་དག་ཐམས་ཅད་བདག་ཉིད་ཀྱི་མགོ་ལ་འཁོར་ལོ༌[^221]བསྐོར་བའི་སྡུག་བསྔལ་གྱི༌[^222]ཕུང་པོ་ཆེན་པོ་མཚམས་མེད་པ་རྣམས་ནམ་འཁོར་བའི་མཐའི་བར་དུ་བདག་གིས་མྱོང་བར་གྱུར་ལ། སེམས་ཅན་གཞན་སུས་ཀྱང་མྱོང་བར་མ་གྱུར་ཅིག་ཅེས་སེམས་བསྐྱེད་པའོ། །

[Block 362]
རྟེན་གྱི་སྟོབས་ཀྱིས་ཀྱང་ཇི་ལྟར་ཆེད་དུ་བརྗོད་པའི་སྡེ་ལས།

[Block 363]
[^223] འཕོ་བར་འདོད་པའི་ལྷའི་བུ་གཞན་ཞིག་བཙོག་པ༌[^224]ཕག་གི་མངལ་དུ་སྐྱེ་བར་ངེས་པའི་ལས་ཀྱི་འབྲས་བུ་མངོན་པར་གྱུར་ནས། གསུམ་ལ་སྐྱབས་སུ་སོང་བ་ཙམ་གྱིས་ཐམས་ཅད་སྦྱངས་ཏེ་སུམ་ཅུ་རྩ་གསུམ་གནམ་གྱི་ལྷ་ལས་ཤི་འཕོས་ནས་དགའ་ལྡན་གནས་སུ༌[^225]སྐྱེས་སོ། །

[Block 364]
ཆོས་ཐམས་ཅད་ལ་བདག་མེད་པར་རྟོགས་པས་ཀྱང་ཤིན་ཏུ་རྩ་བ་ནས་འབྱུང་བར་འགྱུར་ཏེ། འདི་སྐད་དུ་ལས་ཀྱི་སྒྲིབ་པ་སོ་སོར་སྦྱོང་བའི་མདོ་ལས་ཀྱང་འདི་ལྟ་སྟེ། དགེ་སློང་གཞན་ཞིག་གིས༌[^226]མི་ཚངས་པར་སྤྱོད་པ་དང་། མ༌[^227]བསད་པའི་ཕས་ཕམ་པ་གཉིས་བྱུང་ནས་འགྱོད་དེ་མི་དགའ་བས་ཡིད་གདུངས་ཏེ་སྨྱོན་པ༌[^228]བཞིན་དུ་གཙུག་ལག་ཁང་ནས་གཙུག་ལག་ཁང་གཞན་དུ། གྲོང་ནས་གྲོང་གཞན་དུ། ཚོང་དུས་ལ་སོགས་པར་སོང་ནས་སྡིག་པ་དེ་དག་འགྲོ་བ་ཐམས་ཅད་ཀྱི་མདུན་དུ་འཆགས་ཏེ། ཨེ་མའོ་བདག་ཉམས་སོ། །

[Block 365]
བདག་ཉམས་སོ། །ཞེས་ཕྱི་ཕྱིར་སྨྲས་པ་སྟེ།[^229] སྡིག་པ༌[^230]བཤགས་པའི་དཀྲུགས༌[^231]ཤིང་གིས་དྲུང༌[^232]ནས་ཇི་ཙམ་ནས༌[^233]ལས་དེ་བསྲབས་པར་གྱུར་ཀྱང་། དེའི་ཕྱིར་དེ་ཤིན་ཏུ་སེམས་ལ་གདུང་ཞིང་འདུག་པ་དེ་ལ་མངོན་པར་ཤེས་པ་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་གཞན་ཞིག་གིས་ཟབ་མོའི༌[^234]ཆོས་ཇི་ལྟ་ཇི་ལྟ་བར་བཤད་དེ། གང་གིས་དེའི་སྡིག་པ་ཐམས་ཅད་ཀྱི༌[^235]ཐམས་ཅད་དུ་རྩ་བ་ནས་ཕྱུང༌[^236]ནས་ཆོས་ཐམས་ཅད་བདག་མེད་པར་རྟོགས་ནས་མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པར་གྱུར་ཏོ། །

[Block 366]
ངན་སོང་ཐམས་ཅད་ཀྱི་ཉེས་པ་ཐམས་ཅད་ཀྱི་ཐེ་ཚོམ་སེལ་བ་དང་། སྒྲིབ་པའི་ཆོས་ཐམས་ཅད་སྦྱོང་བ༌[^237]ནི་ཟབ་མོའི་ཆོས་ལ་མོས་པ་འདི་ཡིན་ཏེ། འདི་བཞིན་དུ་མོས་པར་བྱོས་ཤིག་ཅེས་གསུངས་སོ།[^238] །

[Block 367]
ཇི་ལྟར་འཕགས་པ་དེ་བཞིན་གཤེགས་པའི་མཛོད་ཀྱི་མདོ་ལས་ཀྱང་། འོད་སྲུངས༌[^239]གང་ཞིག་གི༌[^240]ཕ་ཡང་ཡིན་ལ་རང་སངས་རྒྱས་ཀྱང་ཡིན་པ་དེ་འཚོ་བ་དང་བྲལ་ན་འདི་ནི་སྲོག་གཅོད་པའི་ནང་ན་མཆོག་གོ། །

[Block 368]
མ་བྱིན་པར་ལེན་པའི་མཆོག་ནི་འདི་ལྟ་སྟེ། དཀོན་མཆོག་གསུམ་གྱིས༌[^241]དཀོར་རྐུ་བའོ། །

[Block 369]
འདོད་པས་ལོག་པར་གཡེམ་པའི་མཆོག་ནི་འདི་ལྟ་སྟེ། མ་ཡང་ཡིན་ལ་དགྲ་བཅོམ་མ༌[^242]ཡང་ཡིན་པ་ལ་ཉལ་བའོ། །

[Block 370]
བརྫུན་དུ་སྨྲ་བའི་མཆོག་ནི་འདི་ལྟ་སྟེ། དེ་བཞིན་གཤེགས་པ་ལ་སྐུར་བའོ། །

[Block 371]
ཕྲ་མའི་ནང་ན་མཆོག་ནི་འདི་ལྟ་སྟེ། དགེ་འདུན་གྱི་དབྱེན་བྱེད༌[^243]པའོ། །

[Block 372]
ཚིག་རྩུབ་མོའི་ནང་ན་མཆོག་ནི་འདི་ལྟ་སྟེ། འཕགས་པ་རྣམས་ལ་འཕྱ་བའོ། །

[Block 373]
ཚིག་ཀྱལ་པའི༌[^244]ནང་ན་མཆོག་ནི་འདི་ལྟ་སྟེ། ཆོས་འདོད་པ་རྣམས་རྣམ་པར་གཡེང་བར་བྱེད་པའོ། །

[Block 374]
ཆགས་པའི་མཆོག་ནི་འདི་ལྟ་སྟེ། ཡང་དག་པར་སོང་བ་དང་ཡང་དག་པར་ཞུགས་པ་རྣམས་ཀྱི་རྙེད་པ་འཕྲོག་པར་སེམས་པའོ། །

[Block 375]
ངན་སེམས་ཀྱི་ནང་ན་མཆོག་ནི་འདི་ལྟ་སྟེ། འཕགས་པ་རྣམས་ལ་མི་བརྟེན༌[^245]པའོ། །

[Block 376]
ལོག་པར་ལྟ་བའི་ནང་ན་མཆོག་ནི་འདི་ལྟ་སྟེ། ལྟ་བ་ལ་ཤིན་དུ་ཞེན་པའོ། །

[Block 377]
མི་དགེ་བ་བཅུའི་ལས་ཀྱི་ལམ་འདི་དག་ཐམས་ཅད་ནི་ཁ་ན་མ་ཐོ་བ་ཆེན་པོ་སྟེ། འོད་སྲུངས་གལ་ཏེ་སེམས་ཅན་འགའ་ཞིག་གིས་ཁ་ན་མ་ཐོ་བ་ཆེན་པོ་མི་དགེ་བ༌[^246]བཅུའི་ལས་ཀྱི་ལམ་འདི་དག་དང་ལྡན་པར་གྱུར་པ་དེས་དེ་བཞིན་གཤེགས་པས་རྒྱུ་དང་རྐྱེན་དུ་ལྡན་པའི་ཆོས་བཤད་པ་ལ་ཞུགས་ནས། འདི་ལ་བདག་གམ། སེམས་ཅན་ནམ། འཚོ་བའམ། གང་ཟག་གམ། བྱེད་པའམ། སོ་སོར་མྱོང་བར་བྱེད་པ་གང་ཡང་མེད་དེ། དེ་བས་ན་ཆོས་ཐམས་ཅད་ནི་མ་བྱས་པ། མངོན་པར་འདུས་མ་བྱས་པ། སྒྱུ་མའི་ཆོས་ཉིད་ཉོན་མོངས་པ་མེད་པ། རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པ་ལ་འཇུག་ཅིང་།[^247] ཐོག་མ་ནས་རྣམ་པར་དག་པའི་ཆོས་ཐམས་ཅད་ལ་མངོན་པར་དད་ཅིང་ཤིན་ཏུ་མོས་པའི་སེམས་ཅན་དེ་ནི་ངན་སོང་དུ་འགྲོ་བར་ངས་མ་སྨྲས༌[^248]སོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ཉོན་མོངས་པ་རྣམས་ལ་ཕུང་པོའི་དངོས་པོ་མེད་དེ། ཉོན་མོངས་པ་ཐམས་ཅད་ནི་བྱུང་ནས་ཞིག་སྟེ་མེད་པར་འགྱུར་རོ། །

[Block 378]
རྒྱུ་དང་རྐྱེན་འདུས་ནས་ཚོགས་ཤིང་སྐྱེ་ལ། [^249]སྐྱེས་མ་ཐག་ཏུ་ཡང་འགག་པར་འགྱུར་རོ། །

[Block 379]
བཅོམ་ལྡན་འདས་གང་སེམས་བསྐྱེད་པ་ཞི་བ་དེ༌[^250]བཞིན་དུ་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱང་ཞི་བར་གྱུར་ཅིང་། གང་འདི་བཞིན་དུ་ཤིན་ཏུ་མོས་པ་དེ་ནི་ནམ་ཡང་སྡིག་པའི་རྒྱུར་མི་འགྱུར་ཏེ། གང་གི་ཕྱིར་སྒྲིབ་པ་མེད་པ་ལ་སྡིག་པར་འགྱུར་བའི་གནས་མེད་ཅིང་སྐབས་མེད་དོ་ཞེས་གསུངས་སོ། །

[Block 380]
དེ་ལྟར་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་མངོན་དུ་བྱས་ན་ཉེས་པ་ཐམས་ཅད་ཀྱི་རྒྱུར་གྱུར༌[^251]པའི་མི་དགེ་བ་ཤིན་ཏུ་འབྱང་བར༌[^252]འགྱུར་ཏེ། ཇི་སྐད་དུ་འཕགས་པ་ཨུ་པཱ་ལིས་དྲིས་པའི་མདོ་ལས་གསུངས་པ་དེ་སྟེ་བྱང་ཆུབ་སེམས་དཔའ་སྔ་དྲོ་ཉེས་པ་བྱུང་ན་ཉི་མ་གུང་ལ་བྱང་ཆུབ་ཀྱི་སེམས་མངོན་དུ་བྱས་ན་དེའི་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་མཐའ་ཡས་པར་རིག་པར་བྱའོ། །

[Block 381]
དེ་བཞིན་དུ་ཉི་མ་གུང་ལ་ཉེས་པ་བྱུང་ན་ཕྱི་དྲོ་བྱང་ཆུབ་ཀྱི་སེམས་མངོན་དུ་བྱས་ན་དེའི་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་མི་ཟད་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 382]
དེ་ལས་ཡང་གསུངས་པ། རིགས་ཀྱི་བུ་བྱང་ཆུབ་ཀྱི་སེམས་ནི་ཉེས་བྱས་ཐམས་ཅད་སྲེག་པའི་བསྐལ་པའི་མེ་ལྟ་བུར་འགྱུར་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 383]
སུམ་བརྒྱ་པ་ལས་གསུངས༌[^253]པ། རབ་འབྱོར་རིགས་ཀྱི་བུའམ་རིགས་ཀྱི་བུ་མོ་གང་གིས་འདི་ལྟ་བུའི་མདོ་སྡེ་འཆང་བ་དང་། འཛིན་པ་དང་། ཀློག་པ༌[^254]དང་། ཀུན་ཆུབ་པར་བྱེད་པ་དེ་ལ་ཡོངས་ཀྱིས་བརྙས་པར་འགྱུར་ཤིན་ཏུ་ཡོངས་ཀྱིས་བརྙས་པར་འགྱུར་རོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། གང་སེམས་ཅན་དེ་དག་གིས་ཚེ་རབས་སྔ་མ༌[^255]ལ་མི་དགེ་བའི་ལས་བྱས་ཏེ། གང་ངན་སོང་དུ་སྐྱེ་བར་འགྱུར་བ་དེ་དག་ཚེ་འདི་ལ༌[^256]ཡོངས་ཀྱིས༌[^257]བརྙས་པས་ཚེ་རབས་སྔ་མའི་ལས་མི་དགེ་བ་དེ་དག་འབྱང་བར༌[^258]འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བཤད་དོ། །

[Block 384]
ཁ་ཅིག་འདི་སྐད་དུ་སྡིག་པའི་ལས་ཆུང་ངུ་དང་འབྲིང་པོ་དག་ནི་བཤགས་པ་ལ་སོགས་པའི་མཐུས་བྱང་བར༌[^259]འགྱུར་གྲང་ན། མཚམས་མེད་པ་ལ་སོགས་པ་ལྕི་བ་རྣམས་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་འབྱང་བ༌[^260]ཇི་ལྟར་འགྱུར་ཞེས་ཟེར་བ་དེ༌[^261]དག་ཀྱང་ཡོད་དོ། །

[Block 385]
དེའི་ལན་དུ་མ་སྐྱེས་དགྲ་ལ་སོགས་པས་མཚམས་མེད་པ་བྱས་པས་བསམ་པ་ཆུང་ངུ་དང་འབྲིང་པོ་དང་ཆེན་པོའི་རིམ་པས་མནར་མེད་པར་བསྐལ་པ་ཆུང་ངུའམ་ཉུང་ངུའམ་ཕྱེད་དུ་གནས་པར་འགྱུར་བ་ལས་དེ་དག་ཕྱིས་ཤིན་ཏུ་འགྱོད་པའི་མེས་གདུངས་པའི་སེམས་ཀྱིས་འགྱོད་ནས་བཤགས་པའི་མཐུས༌[^262]ལས་དེ་བསྲབས་པར་གྱུར་ཏེ། གང་ཕོ་ལོང་བརྡབས་པའི་དུས་ཙམ་དུ་སྡུག་བསྔལ་གྱི་འབྲས་བུ་མྱོང་བར་གྱུར་ཏོ་ཞེས་གསུངས་ན་དེ་ཅི་དེ་ཙམ་གྱིས་ཀྱང་ལས་རྣམས་ཤིན་ཏུ་རྩ་བ་ནས་འབྱུང་བར་མི་འགྱུར་བ་མ་ཡིན་ཏེ་འགྱུར་རོ། །

[Block 386]
ཅི་སོག་མ་གཅིག་ཆོད་པས་སོག་མ་ཀུན་བརྡབས་པར་འགྱུར་རམ། གང་གསུངས་པ།

[Block 387 [VERSE]]
བསྐལ་པ་བརྒྱ་དག་སྙེད་དུ་ཡང་། །
ལས་རྣམས་ཆུད་ཟར་མི་འགྱུར་ཏེ། །
ཚོགས་དང་དུས་དང་ལྡན་པ་ན། །
ལུས་ཅན་རྣམས་ལ་འབྲས་བུར་སྨིན། །

[Block 388]
ཞེས་བྱ་བ༌[^263]ལ་སོགས་པ་དེ་ཇི་ལྟར་ཤེས་པར་བྱ་ཞེ་ན། རྣམ་པར་འགྱོད་པ་ལ་སོགས་པ་སྤྱོད་པའི་མཐུས་ལས་གང་དག༌[^264]མངོན་པར་མ་སྦྱངས་ཤིང་བསྲབས་པར་མ་བྱས་པ་དེ་དག་ནི་བཤད་པའི་ཆོས་འདི་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 389]
དེ་ལྟར་ཡང་གསུངས་པ།

[Block 390 [VERSE]]
མི་ཤེས་པས་ནི་སྡིག་པ་ཆུང་བྱས་འོག་ཏུ་འགྲོ། །
མཁས་པས་ཉེས་པ་ཆེ་བྱས་ཀྱང་ནི་ཡང༌[^265]བར་འགྱུར། །
བསྒོངས་པའི་ལྕགས་ནི་ཆུང་ཡང་ཆུ་ཡི་འོག་ཏུ་འབྱིངས།[^266] །
དེ་ཉིད་སྣོད་དུ་བྱས་ན་ཆེ་ཡང་སྟེང་ན་འཕྱོ། །
--- END BLOCKS ---
