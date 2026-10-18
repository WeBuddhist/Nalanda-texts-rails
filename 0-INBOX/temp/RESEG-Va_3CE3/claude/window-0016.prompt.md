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
[Block 561]
ཚིག་བཅུ་གཉིས་པ་ལ། ཆོས་ཐམས་ཅད་སྒྱུ་མ་དང་། སྨིག་རྒྱུ་ལ་སོགས་པ་དང་མཚུངས་པར་སོ་སོར་བརྟགས་ན་གང་ལ་བྱིང་བ་འམ་སྐྲག་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ།། །།

[Block 562 [HEADING]]
##### རྣམ་པར་མི་རྟོག་པ་ཡིད་ལ་བྱེད་པའི་འབྲས་བུ། ^1-1-7-3-0

[Block 563]
བམ་པོ་བཅུ་བདུན་པ། དེ་ལྟར་རེ་ཞིག་རྣམ་པར་མི་རྟོག་པ་ཡིད་ལ་བྱེད་པ་བསྟན་ནས། དེའི་འོག་ཏུ་ཡིད་ལ་བྱེད་པ་དེ་དག་གི་འབྲས་བུ་སྟོན་ཏེ། དེའི་ཚེ་འདི་ནི་གཟུགས་ཞེས་བགྱི་བར་གཟུགས་ལ་མི༌[^344]འཛིན་ཅིང་མི་ལེན་མི་གནས་ཏེ། མངོན་པར་ཞེན་པར་མི་བགྱིད་ལ། འདོགས་པར་མི་བགྱིད་དོ་ཞེས་བྱ་བ་ནི་འཛིན་པའི་རིགས་པ༌[^345]བསྟན་པའི་ཕྱིར་ཚིག་ལྔ་སྨོས་ཏེ། ཐོག་མར་འདུ་ཤེས་ཀྱིས་མི་འཛིན་ཏོ། །

[Block 564]
དེའི་འོག་ཏུ་ཡིད་ཀྱིས་མི་ལེན་ཏོ། །

[Block 565]
དེའི་འོག་ཏུ་ཤེས་རབ་ཀྱིས་གནས་པར་མི་བྱེད་དོ། །

[Block 566]
དེའི་འོག་ཏུ་ལྟ་བས་མངོན་པར་ཞེན་པར་མི་བྱེད་དོ། །

[Block 567]
དེའི་འོག་ཏུ་ཚིག་གིས་གཞན་དག་ལ་འདོགས་པར་མི་བྱེད་དོ། །དེ་ཅིའི་སླད་དུ་ཞེ་ན། བཅོམ་ལྡན་འདས་འདི་ལྟར་གཟུགས་ནི་མ་སྐྱེས་པ་སྟེ། གཟུགས་ཀྱི་མ་སྐྱེས་པ་གང་ལགས་པ་དེ་གཟུགས༌[^346]ལགས་སོ། །

[Block 568]
དེ་ལྟར་ན་གཟུགས་དང་མ་སྐྱེས་པ་དེ་གཉིས་སུ་མ་མཆིས་ཏེ། གཉིས་སུ་བགྱིར་མ་མཆིས་སོ། །དེ་ཅིའི་སླད་དུ་ཞེ་ན། བཅོམ་ལྡན་འདས་འདི་ལྟར་མ་སྐྱེས་པ་ནི་གཅིག་པ༌[^347]མ་ལགས་མང་པོ་མ་ལགས་ཞེས་བྱ་བ་ལ། གཟུགས་མ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་མ་སྐྱེས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 569]
གཟུགས་ཀྱི་མ་སྐྱེས་པ་གང་ལགས་པ་དེ་གཟུགས་མ་ལགས་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་དེའི་མ་སྐྱེས་པ་ཞེས་བྱ་བ་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་ཀུན་བརྟགས་པའི་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་མ་ཡིན་པའོ། །

[Block 570]
དེ་ལྟར་ན་གཟུགས་དང་མ༌[^348]སྐྱེས་པ་དེ་གཉིས་སུ་མ་མཆིས་ཏེ། གཉིས་སུ་བགྱིར་མ་མཆིས་པ་ལགས༌[^349]སོ་ཞེས་བྱ་བས་ཅི་བསྟན་ཞེ་ན། དེ་ལ་གཟུགས་མ་སྐྱེས་པ་ཞེས་བྱ་བའི་ཚིག་གིས་ནི་ཡོངས་སུ་གྲུབ་པ་མ་སྐྱེས་པའི་ངོ་བོ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 571]
གཟུགས་ཀྱི་མ་སྐྱེས་པ་གང་ལགས་པ་དེ་གཟུགས་མ་ལགས་ཞེས་བྱ་བ་འདིས་ནི་མི་སྐྱེ་བ་ལ་ཀུན་བརྟགས་པའི་མཚན་ཉིད་མེད་པར་བསྟན་པ་ཡིན་ཏེ་དེ་ལྟར་ཆོས་ཉིད་ཀྱི་གཟུགས་མི་སྐྱེ་བའི་ངོ་བོ་ཉིད་ཡིན་པ་དང་མི་སྐྱེ་བ་ཡང་ཆོས་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་གཟུགས་ཞེས་བྱ་བ་དང་མ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི་གཅིག་པ་ཉིད་དེ་ཐ་དད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 572]
མ་སྐྱེས་པ་ནི་གཅིག་མ་ལགས་མང་པོ་མ་ལགས་ཞེས་བྱ་བ་ལ་མ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་དེ་དེ༌[^350]ལ་ནི་གཅིག་གམ༌[^351]གཉིས་ཤེའམ། གསུམ་ཞེས་བྱ་བའི་གྲངས་ཀྱི་བྱེ་བྲག་ཡོད་པ་མ་ཡིན་ཏེ་དེ་བས་ན་མི་སྐྱེ་བ་ལ་བྱེ་བྲག་མེད་པའི་ཕྱིར་ཡོངས་སུ་གྲུབ་པའི་ཚེ་གཟུགས་ལ་སོགས་པ་ཐམས་ཅད་ཀྱང་རང་བཞིན་གཅིག་ཏུ་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 573]
དེ་ལྟ་བས་ན། གཟུགས་ཀྱི་མ་སྐྱེས་པ་གང་ལགས་པ་དེ་གཟུགས་མ་ལགས་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་ཀྱི་སྐྱེ་བ་མེད་པའི་ཆོས་ཉིད་གང་ཡིན་པ་དེ་ཀུན་བརྟགས་པའི་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 574]
བཅོམ་ལྡན་འདས་འདི་ལྟར་དེ་བཞིན་ཉིད་ནི་མ་སྐྱེས་པ་སྟེ༌[^352]དེ་བཞིན་ཉིད་ཀྱི་མ་སྐྱེས་པ་གང་ལགས་པ་དེ་དེ་བཞིན་ཉིད་མ་ལགས་ཏེ། དེ་ལྟར་ན་དེ་བཞིན་ཉིད་དང་། མ་སྐྱེས་པ་དེ་གཉིས་སུ་མ་མཆིས་ཏེ་གཉིས་སུ་བགྱིར་མ་མཆིས་པ་ལགས་སོ༌[^353]ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་དྲི་མ་དང༌[^354]བཅས་པ་དང་དྲི་མ་མེད་པ་བཟུང་ནས་སྦྱར་བར་བྱའོ། །

[Block 575]
བཅོམ་ལྡན་འདས་འདི་ལྟར་གཟུགས་ནི་མི་རྟག་པ་སྟེ་གཟུགས་ཀྱི་འགྲིབ་པ་གང་ལགས་པ་དེ་གཟུགས༌[^355]མ་ལགས་ཏེ། དེ་ལྟར་ན་གཟུགས་དང་འགྲིབ་པ་དེ་གཉིས་སུ་མ་མཆིས་ཤིང༌[^356]གཉིས་སུ་དབྱེར༌[^357]མ་མཆིས་པ་ལགས༌[^358]སོ། །དེ་ཅིའི་སླད་དུ་ཞེ་ན། བཅོམ་ལྡན༌[^359]འདི་ལྟར་འགྲིབ་པ་ནི་གཅིག་མ་ལགས་མང་པོ་མ་ལགས་པའི་སླད་དུ་སྟེ།[^360] དེའི་སླད་དུ་གཟུགས་ཀྱི་འགྲིབ་པ་གང་ལགས་པ༌[^361]དེ་ནི་གཟུགས་མ་ལགས་སོ་ཞེས་བྱ་བ་ལ་མེད་པའི་དོན་ནི་མི་རྟག་པའི་དོན་ཏོ༌[^362]ཞེས་འབྱུང་བའི་ཕྱིར། གཟུགས་མི་རྟག་པ་ཞེས་བྱ་བ་ནི་གཟུགས་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 576]
གཟུགས་ཀྱི་འགྲིབ་པ་གང་ལགས་པ་དེ་གཟུགས་མ་ལགས་ཞེས་བྱ་བ་ནི་འདི་ལྟར་གཟུགས་མེད་པ་ལ་ཀུན་བརྟགས་པའི་རྣམ་པ་ནི་འགྱུར་བའི་ཕྱིར་འགྲིབ་པ་ཞེས་བྱ་སྟེ་བརྟགས་པའི་གཟུགས་ཀྱི་འགྲིབ་པ་གང་ཡིན་པ༌[^363]ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་མ་ཡིན་ནོ། །

[Block 577]
དེ་ལྟར་ན་གཟུགས་དང་འགྲིབ་པ་དེ་གཉིས་སུ་མ་མཆིས་ཤིང་གཉིས་སུ་བགྱིར་མ་མཆིས་ཞེས་བྱ་བ་ནི་གཟུགས་དང་འགྲིབ་པ་གཉི་ག་ཡང་བརྟགས་པ་ཡིན་པས་མེད་པའི་ཕྱིར་གཅིག་ཁོ་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 578]
བཅོམ་ལྡན་འདས་འདི་ལྟར་འགྲིབ་པ་ནི་གཅིག་མ་ལགས་མང་པོ་མ་ལགས་ཞེས་བྱ་བ་ནི་འགྲིབ་པ་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར། སྒྱུ་མའི་གཟུགས་བཞིན་དུ་དོན་དམ་པར༌[^364]གྲངས་ཀྱི་བྱེ་བྲག་མེད་དོ། །

[Block 579]
དེ་བས་ན་བརྟགས་པའི་རང་བཞིན་ཐམས་ཅད་ནི་དངོས་པོ་མེད་པའི་རང་བཞིན་དུ་གཅིག་པ༌[^365]ཉིད་དོ། །

[Block 580]
དེ་ལྟ་བས་ན་གཟུགས་ཀྱི་འགྲིབ་པ་གང་ལགས་པ་དེ་གཟུགས་མ་ལགས་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་གཟུགས་ཀྱི་འགྲིབ་པ༌[^366]དེ་ཆོས་ཉིད་ཀྱི་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 581]
བཅོམ་ལྡན་འདས་དེ་བཞིན་ཉིད་ནི་མི་རྟག་པ་སྟེ། དེ་བཞིན་ཉིད་ཀྱི་འགྲིབ་པ་གང་ལགས་པ་དེ༌[^367]དེ་བཞིན་ཉིད་མ་ལགས་ཞེས་བྱ་བ་འདི་ལ་ཡང་དྲི་མ་དང་བཅས་པ་དང་། དྲི་མ་མེད་པའི་བྱེ་བྲག་གིས་སྦྱར་བར་བྱའོ། །

[Block 582]
འདི་ལྟར་སྔར་དྲི་མ་དང་བཅས་པར་གྱུར་པ་ལས་ཕྱིས་དྲི་མ་མེད་པར་འགྱུར་ཏེ་དེའི་ཕྱིར་མི་རྟག་པའོ། །

[Block 583]
དེ་ལྟར་མི་རྟག་པའི་དེ་བཞིན་ཉིད་ལ་གཟུགས་ཀྱི་དེ་བཞིན་ཉིད། [^368]ཚོར་བའི་དེ་བཞིན་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པའི་འགྲིབ་པ་དེ་ཡོངས་སུ་གྲུབ་པའི་དེ་བཞིན་ཉིད་མ་ཡིན་ནོ་ཞེས་སྦྱར་བར་བྱའོ། །

[Block 584]
གང་ཡང་འདི་སྐད་དུ་བཅོམ་ལྡན་འདས་གཟུགས་ཞེས་བགྱི་བ་འདི་ནི་གཉིས་སུ་མ་མཆིས་པའི་གྲངས་སུ་བགྱིས་པའོ་ཞེས་བྱ་བ་ལ་གཉིས་སུ་མེད་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་དེ་དོན་དམ་པའོ། །

[Block 585]
དོན་དམ་པ་དེའི་གྲངས་སུ་བྱ་བ་ནི་འདི་ལྟ་སྟེ་གཟུགས་དང་ཚོར་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་བྱས་པའོ། །

[Block 586]
དེས་ཅི་བསྟན་ཞེ་ན་དོན་དམ་པ་གཅིག་ཁོ་ན་སྟེ་གཉིས་སུ་མེད་པ་ལ། [^369]ཆོས་ཉིད་ཀྱི་གཟུགས། ཆོས་ཉིད་ཀྱི་ཚོར་བ། ཆོས་ཉིད་ཀྱི་འདུ་ཤེས། ཆོས་ཉིད་ཀྱི་འདུ་བྱེད། ཆོས་ཉིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་དོན་དམ་པ་གཅིག་སྟེ་གཉིས་སུ་མེད་པ་ལ་རྣམ་པ་མང་པོར་ཕྱེ་ནས་བསྟན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 587]
དེ་ནས་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུས་ཚེ་དང་ལྡན་པ་རབ་འབྱོར་ལ་འདི་སྐད་ཅེས་སྨྲས་སོ་ཞེས་པ་འདི་གང་དང་སྦྱར་ཞེ་ན། གང་རྣམ་པར་མི་རྟོག་པ༌[^370]ཡིད་ལ་བྱེད་པའི་འབྲས་བུ་བསྟན་མ་ཐག་པ་ལ་གནས་བརྟན་རབ་འབྱོར་གྱིས་འགྲེས་བཞི་བསྟན་ཏེ། བཅོམ་ལྡན་འདས་གང་གི་ཚེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་ཅིང་ཆོས་དེ་དག་ལ་འདི་ལྟར་ཉེ་བར་རྟོག་པ་དེའི་ཚེ་གཟུགས་ལ་མི་འཛིན་ཅིང་མི་ལེན་མི་གནས་ཏེ་མངོན་པར་ཞེན་པར་མི་བགྱིད་ཅེས་བྱ་བ་ནི་གཅིག་གོ། །

[Block 588]
གཟུགས་ཀྱི་མ་སྐྱེས་པ་གང་ལགས་པ་དེ་གཟུགས་མ་ལགས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གཉིས་པའོ། །

[Block 589]
གཟུགས་ཀྱི་འགྲིབ་པ་གང་ལགས་པ་དེ་གཟུགས་མ་ལགས་ཞེས་བྱ་བ་ནི་གསུམ་པའོ། །

[Block 590]
གཟུགས་ཞེས་བགྱི་བ་འདི་ནི་གཉིས་སུ་མ་མཆིས་པའི་གྲངས་སུ་བགྱིས་པ་ལགས་སོ༌[^371]ཞེས་བྱ་བ་ནི་བཞི་པའོ། །

[Block 591]
འགྲེས་བཞི་པོ་འདི་དག་ཉེ་བར་བཟུང༌[^372]ནས་དེ་ལས་རྒྱ་ཆེར་བསྟན་པ་ཉན་འདོད་པའི་ཕྱིར་གནས་བརྟན་ཤཱ་རིའི་བུས་དྲི་བ་དྲིས་སོ་ཞེས་བྱ་བ་དེ་ལྟ་བུར་སྦྱར་རོ། །

[Block 592 [HEADING]]
###### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་ཅིང་ཉེ་བར་རྟོག་པ། ^1-1-7-3-1-0

[Block 593]
དེ་ལ་འགྲེས་དང་པོ་ལ། བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་ཅིང་འདི་ལྟར་ཉེ་བར་རྟོག་སྟེ་ཞེས་བྱ་བ་ཚིག༌[^373]གསུམ་ཉེ་བར་བཟུང་ནས་དྲི་བ་གསུམ་དྲིས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་གང་ཉེ་བར་རྟོག་པ་ནི་གང་ཞེས་བྱ་བའོ། །

[Block 594]
དེ་དག་གོ་རིམས༌[^374]བཞིན་དུ་བཤད་པར་བྱ་སྟེ། བྱང་ཆུབ་ཉིད༌[^375]སེམས་དཔའ་སྟེ་དེའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱའོ་ཞེས་བྱ་བ་ལ་བྱང་ཆུབ་ཅེས་བྱ་བ་ནི་ཆོས་ཀྱི་སྐུ་ལ་བྱའོ། །

[Block 595]
སེམས་ཅན་ཐམས་ཅད་ཀྱང་ཆོས་ཀྱི་སྐུའི་བདག་ཉིད་དེ་དེ་བས་ན་བྱང་ཆུབ་སེམས་དཔའ་ཡང་བྱང་ཆུབ་ཀྱི་བདག་ཉིད་ཁོ་ནའོ། །

[Block 596]
དེ་ལྟ་བས་ན་བྱང་ཆུབ་ཀྱི་ངོ་བོ་ཉིད་ནི་སེམས་དཔའ་ཡིན་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 597]
དེ་ལྟར་ན་སེམས་ཅན་ཐམས་ཅད་ཀྱང་བྱང་ཆུབ་སེམས་དཔར་མི་འགྱུར་རམ་ཞེ་ན། སྤྱིར་གླེང་བ༌[^376]ལ་ཁྱད་པར་དུ་བརྗོད་པར་འདོད་པས་ཁྱད་པར་དུ་བྱང་ཆུབ་དང་འབྲེལ་བའི་སེམས་དཔའ་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བས་འདི་ལ་ཉེས་པ་མེད་དོ། །

[Block 598]
དེ་ལས་གཞན་པའི་སེམས་ཅན་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་མི་ཚོལ་ཞིང་དེའི་དོན་མི་སྒྲུབ་པ་རྣམས་ནི་བྱང་ཆུབ་དང་འབྲེལ་བ་གང་ཡང་མེད་པའི་ཕྱིར་འདི༌[^377]ནི་ཁྱད་པར་དུ་བྱང་ཆུབ་དང་འབྲེལ་བའི་སེམས་དཔའ་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱའོ། །

[Block 599]
དེ་བས་ན་འདིའི་སྤྱོད་པ་ཁྱད་པར་ཅན་ཡང་སྟོན་ཏེ། བྱང་ཆུབ་དེས་ཀྱང་ཆོས་ཐམས་ཅད་ཀྱི་རྣམ་པ༌[^378]ཤེས་ཏེ་ཆོས་དེ་དག་ལ་མངོན་པར་ཞེན་པ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པས་ནི་ཤེས་ཏེ་དོན་དམ་པར་ནི་མངོན་པར་ཞེན་པ་མེད་དོ། །

[Block 600]
རྣམ་པ་གང་དག་དང་། རྟགས་གང་དག་དང་། མཚན་མ་གང་དག་གིས་ཞེས་བྱ་བ་ལ་རྣམ་པ་གང་གིས་ཞེས་བྱ་བ་ནི་བསྟན་པའོ། །
--- END BLOCKS ---
