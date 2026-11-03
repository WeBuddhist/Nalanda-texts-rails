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
[Block 316]
ནན་ཏུར་གྱི་ལས་འདི་ལྟ་བུ་མི་བྱའོ་ཞེས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་བརྩོན་པ་ཤས་ཆེན་པོས་བསྒྲུབ་པར་བྱ་བ་དང་། ལྡོག་པར་བྱ་བ་དང་། ཇི་སྲིད་དུ་བཟོད་པར་བྱ་བ་ཞེས་བྱ་བ་ཐམས་ཅད་དུ་འདི་རྗེས་སུ་འབྲེལ་པར་རིག་པར་བྱའོ། །

[Block 317]
བྱས་ན་བཟོད་པར༌[^221]བྱའོ་ཞེས་བྱ་བ་ནི་ནན་ཏུར་གྱི་ལས་བྱས་པ་ལ། ཨེ་མའོ་དགེ་འདུན་གྱིས་འདི་ལ་བཟོད་པར་བྱ་ཞེས་བྱའོ།[^222] །སྤོ་བ་དང་གཞི་ནས་སྤོ་བར་བྱ་བ་དང་། མགུ་བར་བྱ་བ་དང་། གཞི་ནས་མགུ་བར་བྱ་བ་དང་། དབྱུང་བར་འདོད་པའི་གནས་ལ་ཨེ་མའོ་དགེ་འདུན་གྱིས་འདི་ལ་སྤོ་བ༌[^223]ལ་སོགས་པ་བཞི་པོ་སྦྱིན་པར་བྱ་ཞིང་དབྱུང་བར་འདོད་པ་ལ་ཨེ་མའོ་ཕྱུང་ཤིག༌[^224]ཅེས་བྱ་བའོ། །

[Block 318]
དེས་ཀྱང་འདི་ལ་དེ་བྱས་ཏེ༌[^225]ཞེས་བྱ་བ་ལ་དེས་ཀྱང་ཞེས་བྱ་བ་ནི་གནས་སོ། །

[Block 319]
དེ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་དང་ཆོས་གོས་ཀྱི་ལས་ལ་སོགས་པའོ། །

[Block 320]
འདི་ལ་ནི་གནས་པ་ལ་བྱའོ། །

[Block 321]
ཞུ་བ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི་ཞུ་བ་གཅིག་ཏུ་དོར་ནས་སོ། །

[Block 322]
བསྙེན་པར་རྫོགས་ནས་ལོ་བཅུ་མ་ལོན་པར་མཁན་པོ་ཉིད་དང་གནས་ཉིད་དང་རང་མི་གནས་པར་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་ནས་གང་ཞིག་ལོ་བཅུ་མ་ལོན་པར་དེས་འདི་གསུམ་མི་བྱའོ། །

[Block 323]
བསྙེན་པར་རྫོགས་ནས་ལོ་བཅུ་ལོན་པས་ཀྱང་འོག་ནས་འབྱུང་བ་དག་ལས་ལྷན་ཅིག༌[^226]སྦྱར་བ་གང་དང་ཡང་མི་ལྡན་པས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་གང་ཞིག་འོག་ནས་འཆད་པར་འགྱུར་བའི་ཡན་ལག་ལྔ་དང་ལྡན་པའི་ལྷན་ཅིག་སྦྱར་བ་རྣམས་ནི་དེ་རྣམས་ལས་གང་ཡང་རུང་བ་དག་ཅིག་གིས་ཀྱང་ཡང་དག་པར་ལྡན་པ་འོས་པ་སྟེ། གཞན་ནི་མ་ཡིན་ཞེས་བྱ་བར་དགོངས་པའོ། །

[Block 324]
དེ་ལྟ་ན་ཡང་ཇི་སྐད་དུ་གསུངས་པ། ཆོས་ལྔ་པོ་གཞན་རྣམས་ཀྱིས་ཀྱང་ཡང་དག་པར་ལྡན་པས་ཞེས་བྱ་བ་འདིར་འདི་དང་འདི་རྣམས་གཞན་གྱིས་ཀྱང་ཞེས་བྱ་བའི་བསྡུས་པ་རྣམ་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཏེ། འོན་ཀྱང་རེ་ཞིག་འདི་རྣམས་ཀྱིས་ཀྱང་བྱ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་རྣམས་ཀྱིས་ཀྱང་གཞན་དག་གིས་ཞེས་བྱ་བ་གང་ཡང་རུང་བ་ཅིག༌[^227]གིས་ཞེས་བྱ་བའི་རྣམ་པར་སོ་སོར་རྟོག༌[^228]པའོ། །

[Block 325]
འདི་ཅིའི་ཕྱིར་ཞེ་ན་ལྔ་པོ་འདི་རྣམས་ཐམས་ཅད་མེད་པའི་ཕྱིར་དེ་ནི་གཞན་ལའོ། །

[Block 326]
ལྔ་པོ་དང་པོ་ལ་ནི་ལོ་བཅུ་ཉིད་ཡན་ལག་ཏུ་སྨྲ་ཏེ།[^229] བསྙེན་པར་རྫོགས་ཤིང་ལོ་བཅུ་ལོན་པས་ཡིན་ཞེས་བྱ་བས་ནི་ལོ་བཅུ་ལོན་པ་ཉིད་ཡན་ལག་ཏུ་གསུངས་སོ། །

[Block 327]
དེ་བས་ན་འདི་ལོ་བཅུ་ལོན་པ་ཉིད་གྱིས་ཚིག་དང་པོ་ཕྱི་མ་ཐམས་ཅད་ཀྱི་ཡུལ་ཡོངས་སུ་འཛིན་པ་འདི་ཞེས་བྱ་བ་གྲགས་པའི་དོན་དུའོ། །

[Block 328]
འདུལ་བ་ནི་དོན་ཉིད་གནས་པ༌[^230]སྟེ། ལོ་བཅུ་ལོན་པ་ཡོད་པ་ལ་མཁན་པོ་བྱེད་པ་ལ་སོགས་པ་ལ་རྒྱུ་ཡིན་ཏེ། ལྷག་མ་དེར་ཁྱད་པར་དུ་གྱུར་པ་ཉིད་གལ་ཏེ་ཡོད་པ་ཁྱད་པར་ཉིད་དང་བཅས་པ་ནི་མཆོག་གི་ཆོ་གའོ། །

[Block 329]
གལ་ཏེ་མིན་ན་འདི་ཙམ་ལ་འདིར་བསྟེན་པར་བྱའོ། །

[Block 330]
ཇི་ལྟར་སློབ་པ་ཉིད་ལ་སོགས་པའི་ཁྱད་པར་ལ་འདའ་བ་ཉིད་དེ་བཞིན་དུ་ལོ་བཅུ་ལོན་ནས་འདུལ་བའི་དོན་ལ་གནས་པ་འདི་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 331]
ད་ནི་ལྷན་ཅིག་སྦྱར་བ་དེ་རྣམས་བརྗོད་པར་བྱ་སྟེ། ནད་གཡོག་དང་འགྱོད་པ་བསལ་བ་དང་སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་སྤང་བ་དང་གནས་མངོན་པར་མི་དགའ་བ་དོར་བ་དག་ལ་བྱེད་དམ་བྱེད་དུ་འཇུག་ནུས་པའོ་ཞེས་བྱ་བ་ནི་འགྱོད་པ་བསལ་བར་བྱེད་པའི་ནུས་པའི་ཚིག་གིས་འདུལ་བའི་དོན་ལ་གནས་པ་བསྟན་པའོ། །

[Block 332]
སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་སྤང་བ་ཞེས་བྱ་བའི་ཚིག་གིས་ཆོས་མངོན་པ་ལ་མཁས་པ་ཉིད་ལའོ། །

[Block 333]
གནས་མངོན་པར་མི་དགའ་བ་དོར་བའི་ཚིག་གིས་བསམ་པར་ཤེས༌[^231]པ་ཉིད་དང་ངག་འཛིན་པ་ཉིད་ལ་ཡང་ངོ་། །འདིར་བྱེད་དུ་འཇུག་པའི་སྒྲས་ནི་མི་ནུས་པས་ཀྱང་བྱེད་པ་ཞེས་བྱ་བ༌[^232]ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 334]
འོན་ཀྱང་གདུལ༌[^233]བྱའི་དབང་གིས་ཤེས་པར་བྱ་བ་ཉིད་ཡོད་པ་ལ་གཞན་འཇུག་པ་ལ་བྱ་བར་འགྲོ་བར་ནུས་པ་ཉེ་བར་བཟུང་བ་ཉིད་དོ། །

[Block 335]
དེ་ལྟར་ན་འདིར་ཤིན་ཏུ་འདའ་བར་བྱ་བ་མ་ཡིན་པའི་བྱེད་དུ་འཇུག་པའི༌[^234]དོན་འདུལ་བ་ལ་གནས་པ་ཉིད་ལ་ཤིན༌[^235]ཏུ་འདའ་བར་བྱེད་པ་མེད་པར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 336]
སློབ་པ་ཉིད་ཡན་ཆད་ལྔ་པ་ཉིད་མ་ཡིན་པ་ལ་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཉིད་དང་མང་དུ་ཐོས་པ་ཉིད་དང་སྦྱར་རོ་ཞེས་བྱ་བ་ལ། སློབ་པ་ཉིད་དང་མི་སློབ་པ་ཉིད་ཅེས་བྱ་བ་འདི་ལས་ཡན་ཆད་གང་ལྷན་ཅིག་ཏུ་བརྗོད་པའི་ལྔ་པ་མ་ཡིན་པ་ཉིད༌[^236]འདི་ལྟ་སྟེ། དད་པ་དང་ཚུལ་ཁྲིམས་ལ་སོགས་པ་ལས་གཞན་པའི་ལྷན་ཅིག་སྦྱར་བ་རྣམས་ཏེ། ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཉིད་དང་མང་དུ་ཐོས་པ་ཉིད་དང་བཅས་པ་སྦྱར་བར་རིག་པར་བྱའོ། །

[Block 337]
ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཉིད་དང་མང་དུ་ཐོས་པ་ཉིད་དག་དང་བཅས་པ་ལྔ་པའོ། །

[Block 338]
འདིར་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཉིད་ནི་ཚུལ་ཁྲིམས་འཆལ་པ་དང་ལྷན་ཅིག་ཏུ་གནས་པ་མི་རིགས་པས་ཁྱད་པར་ཅན་ཏེ། གང་གིས་འདི་དགེའོ་ཞེས་བྱ་བར་བསམ་པར༌[^237]བྱེད་པ་དེ་རིག་པར་བྱའོ། །

[Block 339]
སླར་མང་དུ་ཐོས་པ་ཉིད་ནི་ལྷན་ཅིག་སྦྱར་བ་གང་ལ་སྡེ་སྣོད་རྣམས་འཛིན་པ་ཡོད་པ་དེ་ལ་དེའི་མི་མཐུན་པའི་ཕྱོགས་སུ་གྱུར་པ་ཕ་རོལ་གྱི་གཙོ་བོ་ལ་སོགས་པ་དང་། དངོས་པོ་དང་ཚིག་དང་ངག་ལ་སོགས་པའི་ཡན་ལག་རྣམས་དང་། ཚིགས་སུ་བཅད་པ་རྣམ་པར་བསགས་པ་ལ་སོགས་པ་རྣམས་དང་། བཞད་གད་དང་སྔོན་བྱུང་བ་ལ་སོགས་པ་རྣམས་ལ་མངོན་པར་ཤེས་པ་ཉིད་གང་ལ་ཡོད་པ་མ་ཡིན་པ་དེ་སྡེ་སྣོད་རྣམས་འཛིན་པར་རྟོགས་པར་བྱའོ། །

[Block 340]
སྡེ་སྣོད་མངོན་པར་ཤེས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་དང་། འདུལ་བ་དང་། མ་མོ་མངོན་པར་ཤེས་པ་ཉིད་དང་། ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཉིད་དང་མང་དུ་ཐོས་པ་ཉིད་དང་སྦྱར་ནས་ལྔའོ། །

[Block 341]
འདུལ་བ་ལས་གསུངས་ཏེ། མདོ་སྡེ་འཛིན་པ་དང་། འདུལ་བ་འཛིན་པ་དང་མ་མོ་འཛིན་པའོ། །

[Block 342]
མདོ་སྡེ་ལ་གསལ་བ་དང་། འདུལ་བ་ལ་གསལ་བ་དང་། མ་མོ་ལ་གསལ་བའོ། །

[Block 343]
མདོ་སྡེ་ལ་མཁས་པ་དང་། འདུལ་བ་ལ་མཁས་པ་དང་། མ་མོ་ལ་མཁས་པའོ། །

[Block 344]
མདོ་སྡེ་ལ་རིག་པ་དང་། འདུལ་བ་ལ་རིག་པ་དང་མ་མོ་ལ་རིག་པ་ཞེས་བྱའོ། །

[Block 345]
དེ་ལ་མདོ་སྡེ་ལ་སོགས་པ་བཟུང་བ་མི་བརྗེད་པ་ནི་འཛིན་པའོ། །

[Block 346]
འདི་ནི་སྡེ་སྣོད་གསུམ་ཡིན་ཏེ། གཅིག་ཏུ་གནས་པ་ལ་གནས༌[^238]ལ་མཐོང་བས་འདྲེས་པར་གནས་པའོ། །

[Block 347]
དེ་ལྟར་གནས་པ་འདི་ལ་གང་ཞིག་མ་འདྲེས་པ་ཡོངས་སུ་དཔྱོད་པར་ནུས་པ་འདི་ནི་མཁས་པ་ཉིད་དོ། །

[Block 348]
ལུང་དང་རིགས་པ༌[^239]དག་གིས་མདོ་སྡེ་ལ་སོགས་པ་སྦྱོར་བ་འདི་ནི་རིག་པ་ཉིད་དོ། །

[Block 349]
དེ་ལྟར་སྦྱར་བས་གང་ཞིག་གཞན་ལ་སྟོན་པར་ནུས་པ་འདི་ནི་གསལ་བ་ཉིད་དོ། །

[Block 350]
མི་བརྗེད་པ་དང་ལྷན་ཅིག་ཏུ་འདི་ཐམས་ཅད་མངོན་པར་ཤེས་པ་ཉིད་ཅེས་བྱ་བ་སྤྱིར་མངོན་པར་ཤེས་པའི་ཚིག་གིས་གསུངས་སོ། །

[Block 351]
དེ་དག་འཛིན་དུ་འཇུག་ནུས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་རྣམས་མངོན་པར་མི་ཤེས་པ་ལ་དེ་རྣམས་ལ༌[^240]འཛིན་དུ་འཇུག་ཅིང་གོ་བར་བྱེད་ནུས་པ་ཡིན་ནོ། །

[Block 352]
དེ་བས་ན་སྡེ་སྣོད་མངོན་པར་ཤེས་པའི་ཚིག་འདི་ཁྱད་པར་ཉིད་ལ་རིག་པར་བྱའོ། །

[Block 353]
ལྷག་པའི་ཚུལ་ཁྲིམས་དང་སེམས་དང་ཤེས་རབ་ལ་སློབ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། སློབ་པའི་དངོས་པོ་ནི་སློབ་པ་ཉིད་དེ་གཉིས་ལྡན་གྱིས་གཅིག་དང་ལྡན་པའི་དངོས་པོའོ། །

[Block 354]
ལྷག་པའི་ཚུལ་ཁྲིམས་ཀྱི་ཚིག་གིས་འདུལ་བའི་ལུགས་ཐམས་ཅད་གཟུང་བ་ཡིན་ནོ། །

[Block 355]
ལྷག་པའི་སེམས་ཀྱི་ཚིག་གིས་ནི་བསམ་གཏན་རྣམས་སོ།[^241] །ལྷག་པའི་ཤེས་རབ་ཀྱི་ཚིག་གིས་ནི་བདེན་པ་མཐོང་བའི་གོམས་པ་ལའོ། །
--- END BLOCKS ---
