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
[Block 351 [HEADING]]
###### **མིའི་རྒྱལ་པོའི་འཁོར།** ^4-1-5-5-4-4-0

[Block 352]
མདོ་ལས་ལུས་འཕགས་མོའི་བུ་མ་སྐྱེས་དགྲ་དང་ཐབས་ཅིག་གོ་ཞེས་པ་ནི་མིའི་རྒྱལ་པོའི་འཁོར་བསྟན་ཏེ་རྒྱལ་པོ་སྨོས་པ་ནི་གཙོ་བོས་བསྡུས་པའི༌[^398]ཕྱིར་ཏེ། མ་སྐྱེས་དགྲའི་གླེང་གཞི་ནི་མ་བཙས་པའི་སྔ་རོལ་ཏུ་ཕ་བསད་པའི་བསམ་པ་དང་བཅས་པའི་ཕྱིར་མ་སྐྱེས་པར་ཕའི་དགྲར་གྱུར་པ་སྟེ། དེས་ཕ་བསད་པ་དེ་ཉན་ཐོས་པའི་གཞུང་དུ་སྡིག་པ་བཤགས་པས་སེམས་ཅན་དམྱལ་བར་ཕོ་ལོང་བརྡབས་པ་ཙམ་ཞིག་སྐྱེས་ཏེ། ཕྱིས་རང་སངས་རྒྱས་ཀྱི་འབྲས་བུ་ཐོབ་པར༌[^399]ཡང་འཆད་ཐེག་པ་ཆེན་པོ་ལས་ནི་ཆོས་ཟབ་མོ་རྟོགས་པའི་བཤགས་པས་སེམས་ཅན་དམྱལ་བར་མ་ལྷུང་བར་ཡང་འཆད་དེ། ཞིབ་ཏུ་མྱ་ངན་ལས་འདས་པ་ཆེན་པོའི་མདོ་ལས་གསུངས་པ་བཞིན་ནོ། །

[Block 353 [HEADING]]
###### འཁོར་བཞི། ^4-1-5-5-5-0

[Block 354]
མདོ་ལས་ཡང༌[^400]དེའི་ཚེ་བཅོམ་ལྡན་འདས་འཁོར་བཞིས་བསྐོར་ཏེ། མཆོད་པ་དང་རིམ་གྲོ་བྱས་ཞེས་པའི་བར་དུ་ནི་འཁོར་ཕུན་སུམ་ཚོགས་པ༌[^401]བཞིར་ཕྱེ་བ་ལ། གསུམ་ནི་བསྟན་ཟིན། འདི་བཞི་པ་སྟེ། འཁོར་བཞི་ལ་བདུད་དང་ཚངས་པ་དང་། དགེ་སློང་དང་བྲམ་ཟེའི་འཁོར་ཞེས་ཀྱང་འཆད། ཡང་འཁོར་རྣམ་པ་བཞི་སྟེ། ཉན་ཐོས་པའི་འཁོར་ཤཱ་རིའི་བུ་དང་། བྱང་ཆུབ་སེམས་དཔའ་བྱམས་པ་ལྟ་བུ་ཆོས་གླེང་བའི་འཁོར་དང་། དབང་པོ་སྨིན་པ་དེ་ཆོས་རྟོགས་པའི༌[^402]འཁོར་དང་། དགེ་བའི་རྒྱུ་ལ་སོགས་པའི་འཁོར་དང་། མ་འོངས་པ་ན་ཆུད་པར་འགྱུར་བའི་འཁོར་རོ། །

[Block 355]
ཡང་འཁོར་བཞི་སྟེ། དགེ་སློང་དང་། དགེ་སློང་མ་དང་། དགེ་བསྙེན་དང་། དགེ་བསྙེན་མའི་འཁོར་རོ། །

[Block 356 [HEADING]]
#### ཆོས་བཤད་པར་བྱེད་པའི་དུས། ^4-1-6-0

[Block 357]
མདོ་ལས་གདོན་མི་ཟ་བར༌[^403]བསྟན་པ་ཆེན་པོ་ཞེས་བྱ་བ་ཆོས་ཀྱི་གཞུང་མདོ་སྡེ་ཤིན་ཏུ་རྒྱས་པ་ཆེན་པོ། །བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་གདམས་པ། སངས་རྒྱས་ཐམས་ཅད་ཀྱིས༌[^404]ཡོངས་སུ་ཟིན་པ་བཤད་པར་བཞེད་དེ༌[^405]ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཆོས་བཤད་པར་བྱེད་པའི༌[^406]དུས་དེ་ཡང་རྣམ་པ་གསུམ་སྟེ། སྔར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་ཐེག་པ་ཆེན་པོ་མཐའ་ཡས་གདོན་མི་ཟ་བ་བསྟན་པ་ཞེས་བྱ་བའི་ཆོས་ཀྱི་གཞུང་བསྟན། འོག་ཏུ་ཉན་ཐོས་པ་རྣམས་ཀྱི་ཆེད་དུ་ཐེག་པ་གཅིག་པུ་བསྟན་པ་དང་། གཞན་གྱི་དོན་དུ་ལུང་དང་རིགས་པས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་ཐེག་པ་གཅིག་པུ༌[^407]བསྟན། དེའི་འོག་ཏུ་བདག་གི་དོན་དུ་སྤྱོད་པ་དང་། འབྲས་བུ་བསྟན། གསུམ་དུ་སྔར་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན། འོག་ཏུ་ཆོས་ཀྱི་མཐུ་བསྟན་པའི་ཕྱིར་གདོན་མི་ཟ་བར་བྱ་བས་མདོ་འདི་བསྟན་ཏོ། །

[Block 358]
ཐེག་པ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་དོན་རྣམ་པ་དྲུག་སྟེ། ཐེག་པ་རྣམ་པ་གཉིས་ལས་འདས་པ་དང་། སངས་རྒྱས་ཀྱི་སར་འདིས་ཕྱིན་པར་བྱེད་པ་དང་། སངས་རྒྱས་ཀྱི་ཐེག་པ༌[^408]པས་ཐེག་པ་ཆེན་པོ་ཡིན་པ་དང་། སྡུག་བསྔལ་ཆེན་པོ་ཞི་བར་བྱེད་ཅིང་བདེ་བ་ཆེན་པོ་སྦྱིན་པར་བྱེད་པ་དང་། འཕགས་པ་སྤྱན་རས་གཟིགས་ལ་སོགས་ཏེ་སྐྱེས་བུ་ཆེན་པོ་རྣམས་ཀྱི་ཐེག་པ་ཡིན་པ་དང་། ཆོས་རྣམས་ཀྱི་མཐར་ཐུག་པར་བྱེད་པའི་ཕྱིར་ཐེག་པ་ཆེན་པོ་བསྡུས་པ་ལས་ཀྱང་ཐེག་པ་ཡང་ཡིན་ལ་ཆེན་པོ་ཡང་ཡིན་པས་ཐེག་པ་ཆེན་པོའོ། །

[Block 359]
འདིས་འདེགས་པར་བྱེད་པའི་ཕྱིར་ཐེག་པའོ། །

[Block 360]
ཆེན་པོ་ནི་རྣམ་པ་བདུན་དང་ལྡན་པའི་ཕྱིར་ཆེན་པོ་སྟེ། སྤྱད་ཡུལ་དང་། སེམས་དང་ཡེ་ཤེས་དང་བརྩོན་འགྲུས་དང་ཐབས་དང་། ཐོབ་པ་དང་། ལས་ཆེན་པོའི་ཕྱིར་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 361]
མཐའ་ཡས༌[^409]གདོན་མི་ཟ་བར་བསྟན་པ་ཞེས་པ་ནི་མདོ་སྡེ་འདིའི་རྣམ་གྲངས་ཀྱི་མིང་སྟེ་འདིའི་འགྲེལ་པ་ལས་མདོ་སྡེའི་མིང་གི་རྣམ་གྲངས་བཅུ་བདུན་ཡོད་དེ། མདོ་སྡེ་འདི་བྱང་ཆུབ་སེམས་དཔའ་ཐེག་པ་ཆེན་པོ་སྤྱོད་པ་རྣམས་ལ་བཤད་པས༌[^410]མཐའ་ཡས་གདོན་མི་ཟ་བའི་དོན་ཏོ། །

[Block 362]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་བསྟན་པ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་གཟུང༌[^411]བ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་གསང་བ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་ཡོན་ཏན་གྱི་མཛོད། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་མན་ངག་གི་གནས། དེ་བཞིན་གཤེགས་པ་རྣམས་བསྐྱེད༌[^412]པ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་དབྱིངས། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་རིང་བསྲེལ་བསྟན་པར་བྱེད་པ། ཐབས་མཁས་པས་ཐེག་པ་གཅིག་སྟོན་པ། བླ་ན་མེད་པའི་གནས་དམ་པའི་ཆོས་པུཎྜ་རཱི་ཀ་ཞེས་བྱ་བ་ཆོས་རྣམས་ཀྱི་དམ་པའོ། །

[Block 363]
འགྲེལ་པ་ལས་མཐའ་ཡས་གདོན་མི་ཟ་བར་བསྟན་པ་ཞེས་པ་ནི་ཚིག་དང་དོན་རྫོགས་པ་མིང་གི་རྣམ་གྲངས་བཅུ་བདུན་ཏེ། ཆོས་ཀྱི་སྒོ་མོ་འདིས༌[^413]ཆོས་ཀྱི་སྒོ་མོ་ཟབ་མོ་གཞན༌[^414]ཡང་སྟོན་པར་བྱེད་དོ། །

[Block 364]
འཆད་པའི་ལུང༌[^415]དང་བཤད་པའི་འབྲས་བུ་གཉི་ག་ཡང་མཐའ་ཡས་པའི་ཕྱིར་རོ། །

[Block 365]
སེམས་ཅན་རྣམས་ཀྱི་རང་བཞིན་མཐའ་ཡས་པའི་ཕྱིར་ཆོས་རྣམས་ཀྱང་མཐའ་ཡས་སོ། །

[Block 366 [VERSE]]
ཆོས་མཐའ་ཡས་པའི་ཕྱིར་དོན་ཡང་མཐའ་ཡས་སོ། །
དོན་མཐའ་ཡས་པ་ནི་ཆོས་གཅིག་བསྐྱེད༌[^416]པའོ། །
ཆོས་གཅིག་ནི་མཚན་མ་མེད་པའི་ཆོས་ཏེ།
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་གནས་པར་བྱ་བའོ། །

[Block 367]
དེ་ཉིད་ཡང་དག་པ་སྟེ། བྱམས་པ་དང་སྙིང་རྗེར་ལྡན་པ། སེམས་ཅན་རྣམས་སྡུག་བསྔལ་གྱི་ས་གནས༌[^417]འདྲེན་པ། བདེ་བའི་གནས་སུ་འཇོག་པའོ། །

[Block 368]
རིགས་ཀྱི་བུ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་མཐའ་ཡས་པའི་ཆོས་ཀྱི་སྒོ་དེ་གཅིག་བསྒྲུབས་པས༌[^418]མྱུར་དུ་བླ་ན་མེད་པའི་བྱང་ཆུབ་འཐོབ༌[^419]པོ། ། འདི་ལྟ་སྟེ་དཔེར་ན་ས་བོན་གཅིག་བསྐྱེད་པས༌[^420]བརྒྱ་སྟོང་མང་པོ་བསྐྱེད་པར༌[^421]འགྱུར་རོ། །

[Block 369]
བརྒྱ་སྟོང་མང་པོ་ལས་ཀྱང་དེ་བཞིན་དུ་བསྐྱེད༌[^422]དེ་མཐའ་ཡས་པར་འགྱུར་བ་བཞིན། མདོ་སྡེ་འདི་ཡང་དེ་བཞིན་ཏེ། ཆོས་གཅིག་གིས་དོན་བརྒྱ་སྟོང་གྲངས་མེད་པ་བསྐྱེད་དོ། །

[Block 370]
དོན་དེ་ལས་ཀྱང་དེ་བཞིན་དུ་མང་དུ་བསྐྱེད་པས༌[^423]དོན་མཐའ་ཡས་མུ་མེད་པར་འགྱུར་བའི་ཕྱིར་མདོ་སྡེ་འདི་ཡང་མཐའ་ཡས་གདོན་མི་ཟ་བར་བསྟན་པ་ཞེས་བྱའོ། །

[Block 371]
ཡང་ན་མདོ་སྡེ་འདི་མཆོག་གམ་དམ་པ་ཞེས་བྱ་སྟེ། སྡེ་སྣོད་གསུམ་གྱི་ནང་ནས་མཛོད་འདི༌[^424]དམ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 372]
ཡང་མདོ་སྡེ་འདི་ཐེག་པ་ཆེན་པོ་ཤིན་ཏུ་རྒྱས་པ་ཆེན་པོ་གདོན་མི་ཟ་བའི་སྒོ་ཡིན་ཏེ། སེམས་ཅན་རྣམས་ཀྱི་དབང་པོ་དང་མཐུན་པར་འཛིན་པའི་ཕྱིར་འཛིན་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 373]
ཡང་འདི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་གདམས་པའི་ཆོས་ཏེ། དབང་པོ་སྨིན་པ༌[^425]རྣམས་ལ་སྣོད་བཞིན་དུ་ཆོས་སྟོན་པས་ཐེག་པ་རྣམ་གཉིས་སུ་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 374]
ཡང་འདི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས༌[^426]ཡོངས་སུ་གཟུང་བ༌[^427]སྟེ། གནས་གཞན་མེད་པའི་ཕྱིར་རོ། །

[Block 375]
ཡང་འདི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་གསང་བའི་ཆོས་ཏེ། ཆོས་འདི་ཤིན་ཏུ་ཟབ་པའི་ཕྱིར་སངས་རྒྱས་ཉག་གཅིག་གི༌[^428]མཁྱེན་པ་སྟེ། གསང་བ་ནི་མཛོད་ཅེས་པའི་དོན་ཏོ། །

[Block 376]
ཡང་འདི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་ཡོན་ཏན་གྱི་མཛོད་དེ། བསོད་ནམས་དང་ཏིང་ངེ་འཛིན་ལ་སོགས་པའི་མཛོད་ཡིན་པའི་ཕྱིར་རོ།། །།

[Block 377]
དམ་པའི་ཆོས་པུཎྜ་རཱི་ཀའི་འགྲེལ་པ། བམ་པོ་གཉིས་པ། ཡང་འདི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་གསང་བའི་གནས་ཏེ། དབང་པོ་མ་སྨིན་ཅིང་སྣོད་དུ་མ་གྱུར་པ་རྣམས་ལ༌[^429]སྦྱིན་པར་བྱ་བ་མ་ཡིན་པའོ། །

[Block 378]
ཡང་འདི་དེ་བཞིན་གཤེགས་པ་རྣམས་བསྐྱེད་པ༌[^430]སྟེ། ཆོས་ཀྱི་སྒོ་འདི་ཐོས་པས་སྤྲུལ་པ་དང་རྫོགས་ལོངས་སྤྱོད་པའི་སྐུ་ཐོབ་པར་བྱེད་པའོ། །

[Block 379]
ཡང་འདི་དེ་བཞིན་གཤེགས་པ༌[^431]རྣམས་ཀྱི་དབྱིངས་ཏེ། ཆོས་འདིས་བླ་ན་མེད་པའི་བྱང་ཆུབ་འགྲུབ་པར་བྱེད་ཀྱི་མདོ་སྡེ་གཞན་གྱིས༌[^432]མ་ཡིན་པས་དེ་བཞིན་གཤེགས་པའི་ཆོས་ཀྱི་སྐུ་དང་ཡེ་ཤེས་སྟོན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 380]
ཡང་འདི༌[^433]དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་ཆོས་ཀྱི་སྐུ་སྟེ། ཆོས་ཀྱིས༌[^434]སྒྲིབ་པ་སྦྱོང་བར༌[^435]བྱེད་པའི་ཕྱིར་རོ། །

[Block 381]
ཡང་འདི༌[^436]དུས་གསུམ་གྱི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་རིང་བསྲེལ་བསྟན་པར་བྱེད་པ་སྟེ། དེ་ཡང་དེ་བཞིན་གཤེགས་པའི་ཡོན་ཏན་དང་ཆོས་ཀྱི་སྐུ་འདིའི་ནང་ནས་སྟོན་པའི་ཕྱིར་རོ། །

[Block 382]
ཡང་འདི་ཐབས་མཁས་པ་སྟེ། ཆོས་ཀྱི་དོན་འདི་ལ་བརྟེན་པས་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བའོ། །

[Block 383]
སངས་རྒྱས་ནས་ཀྱང་ལྷ་དང་མི་ལ་སོགས་པའི་སེམས་ཅན་རྣམས་ལ་ཐེག་པ་རྣམ་པ་ལྔའི་ཆོས་ཀྱིས༌[^437]བྱང་ཆུབ་ཐོབ་པའི་ཡེ་ཤེས་དང་ཐབས་སྟོན་པའི་ཕྱིར་རོ། །

[Block 384]
ཡང་འདི་ཐེག་པ་གཅིག་པོ་སྟོན་པས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་ངོ་བོ་ཉིད་སྟོན་པ་ཡིན་གྱི། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ས་ནི་ཡང་དག་པའི་མཐའ་མ་ཡིན་ནོ། །

[Block 385]
ཡང་འདི་དོན་དམ་པའི་གནས་ཏེ། ཆོས་འདི་དེ་བཞིན་གཤེགས་པའི་ཆོས་ཀྱི་སྐུ༌[^438]ཡང་དག་པའི་གནས་ཏེ། ཆོས་ཀྱི་སྐུ་ཉིད་དམ་པ་ཡིན་པའི་ཕྱིར་དམ་པའི་གནས་ཞེས་བྱའོ། །

[Block 386]
ཡང་འདི་དམ་པའི་ཆོས་པདྨ་དཀར་པོ་ཞེས་པ་ནི་འགྲེལ་པ་ལས་རྣམ་པ་གཉིས་ཏེ། ཆུ་ལས་བྱུང་བའི་དོན་དང་། ཁ་འབྱེད་པའི༌[^439]དོན་ཏོ། །

[Block 387]
ཆུ་ལས་བྱུང་བ་ཡང་དོན་རྣམ་པ་གཉིས་ཏེ། ཐེག་པ་རྣམ་པ་གཉིས་ཀྱི་ཆུ་རྙོག་པ་ཅན་ལས་བྱུང་སྟེ། ཅིག་ཅར་ཆུད་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཉིད་པདྨོ་དང་འདྲ་བར་རྙོག་པ་དང་བྲལ་ཞིང་ཆོས་ཉིད་བརྟན་པའི༌[^440]ཚུལ་ཐེག་པ་གཅིག་པུའི་གཞུང་རྟོགས་ཞེས་པའི་དོན་སྟོན་ཏོ། །

[Block 388]
ཡང་ན་ཐེག་པ་རྣམ་པ་གཉིས་ཆུ་རྙོག་པ་ཅན་གྱི་ནང་ནས་བྱུང་སྟེ་དེ་བཞིན་གཤེགས་པའི་འཁོར་ཆེན་པོར་ཞུགས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་པདྨོའི་གདན་ལ་བཞུགས་ཤིང་མཐའ་ཡས་གདོན་མི་ཟ་བའི་ཡེ་ཤེས་རྣམ་པར་དག་པའི་སྤྱོད་ཡུལ་དེ་བཞིན་གཤེགས་པའི་གསང་བའི༌[^441]མཛོད་རྟོགས་པ་བཞིན་ཉན་ཐོས་པ་རྣམས་ཀྱིས་ཀྱང་རིམ་གྱིས་ལུང་ཡང་དག་པ་དང་། གཞུང་དང་སྤྱོད་པ་དང་འབྲས་བུ་ལ་ཞུགས་ཞེས་པའི་དོན་ཏོ། །

[Block 389]
ཡང་འདི་བླ་ན་མེད་པའི་ཆོས་ཀྱི་སྒོ་སྟེ། ཕུན་སུམ་ཚོགས་པ༌[^442]ཐམས་ཅད་སྡུད༌[^443]པའི་ཕྱིར་རོ། །

[Block 390]
སྡུད་པ་ནི་མཐའ་ཡས་པའི་མིང་དང་ཚིག་དང་འབྲུའི་ཚོགས་ཐམས་ཅད་སྡུད༌[^444]པའི་ཕྱིར་བླ་ན་མེད་པ་སྟེ། བཤད་པ་དང་བཤད་པར་བྱ་བའི་ཆོས་ཐམས་ཅད་འདིར་འདུས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
