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
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ལ་མི་དམིགས་ཞེས་བྱ་བ་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་དམིགས་པ་ལ་ཉེ་བར་གནས་ཏེ། འདི་ལྟ་སྟེ་ཆོས་སོ། །

[Block 352]
བརྒྱལ་བར་གྱུར་པ་དེ་ལ་ནི་དམིགས་པ་མེད་དེ། དེའི་ཕྱིར་འདི་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཉིད་དུ་མི་རུང་ངོ་། །ཉིང་མཚམས་སྦྱོར་བ་སྦྲེལ་ཟིན་པ་ཞེས་བྱ་བ་ནི་བདག་གི་ལུས་རབ་ཏུ་ཐོབ་པའོ། །

[Block 353]
དེ་ནས༌[^226]གཞན་ཞེས་བྱ་བ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མ་ཡིན་པ་ནི་གཞན་པ་སྟེ། གཞན་རྣམ་པར་ཤེས་པ་དྲུག་པོ་རྣམས་ནི་གནས་སོ་སོར་ངེས་པ་དང་གཡོ་བའི་ཕྱིར་རོ། །

[Block 354]
ཇི་ལྟར་མིག་གི་རྣམ་པར་ཤེས་པ་གནས་སོ་སོར་ངེས་པ་ཡིན་པ་བཞིན་དུ་རྣ་བའི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་ལྷག་མ་རྣམས་ཀྱི་ཡང་རྣ་བ་ལ་སོགས་པ་དབང་པོ་གཟུགས་ཅན་རྣམས་ནི་རྟེན་ཡིན་ནོ། །

[Block 355]
དེས་ན་གལ་ཏེ་རྣམ་པར་ཤེས་པ་དེ་དག་གི་རང་རང་གི་གནས་བླངས་པར་གྱུར་ལ། རྣམ་པར་ཤེས་པ་དེ་རྣམས་འགགས་པར་གྱུར་པ་ན་ཐོབ་པའི་མིག་ལ་སོགས་པ་རྣམས་རུལ་པར་འགྱུར་རོ། །

[Block 356]
ཇི་ལྟར༌[^227]ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མ་ཡིན་པའི་རྣམ་པར་ཤེས་པ་དང་མིང་དང་གཟུགས་མདུང་ཁྱིམ་ལྟར་གཅིག་ལ་གཅིག་བརྟེན་པའི༌[^228]ཚུལ་གྱིས་འཇུག་པ་གང་ཡིན་པ་དེ་ཡང་མི་རུང་ངོ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་མི་རུང་བ་བསྟན་པར་བྱ་སྟེ། ཇི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་རྣམ་པར་ཤེས་པའི་རྐྱེན་གྱིས་མིང་དང་གཟུགས། མིང་དང་གཟུགས་ཀྱི་རྐྱེན་གྱིས་ཀྱང་རྣམ་པར་ཤེས་པ་ཞེས་གསུངས་པ་དེ་ལ། རྣམ་པར་ཤེས་པའི་རྐྱེན་གྱིས་མིང་སྟེ། རྣམ་པར་ཤེས་པའི་ཚོགས་སོ། །

[Block 357]
དེ་ནི་གཟུགས་ཅན་མ་ཡིན་པའི་ཕུང་པོ་བཞི༌[^229]ཡིན་པར་བརྗོད་དོ། །

[Block 358]
གཟུགས་ནི་ནུར་ནུར་པོའོ། །

[Block 359]
མིང་དང་གཟུགས་ཀྱི་རྐྱེན་གྱིས་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་དེ་ལ། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལས་གཞན་གང་ཡང་མ་ཡིན་ཏེ། གང་དེ་ནི་མིང་དང་གཟུགས་ལ་བརྟེན་ནས་སྐད་ཅིག་མ་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་རྒྱུན༌[^230]མི་འཆད་པར་འཇུག་གོ། །

[Block 360]
རྣམ་པར་ཤེས་པ་གཞན་གྱི༌[^231]ཟས་སུ་མི་རུང་སྟེ་ཞེས་བྱ་བ་དེ་བསྟན་པར་བྱ་སྟེ། ཟས་ནི་བཞིར་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ཏེ། ཁམ་གྱི་ཟས་དང་། རེག་པ་དང་། ཡིད་ལ་སེམས་པ་དང་། རྣམ་པར་ཤེས་པའིའོ། །

[Block 361]
དེ་ལ་ཁམ་གྱི༌[^232]ཟས་ནི་ཞུ་བར་གྱུར་པ་ན་སྟེ། ཞུ་བར་གྱུར་པ་ན་གང་གི་ཕྱིར་རྟེན་ལ་ཕན་འདོགས་པར་བྱེད་པའོ། །

[Block 362]
རེག་པའི་ཟས་ནི་ཡུལ་དང་ལྡན་པ་སྟེ། གཟུགས་ལ་སོགས་པའི་ཡུལ་རྣམས་མཐོང་བ་ཙམ་ཉིད་ཀྱིས་རྟེན་ལ་ཕན་འདོགས་པ་སྐྱེད༌[^233]པའོ། །

[Block 363]
ཡིད་ལ་སེམས་པའི་ཟས་ནི་བསམ་པ་དང་ལྡན་པ་ན་སྟེ། གང་གི་ཕྱིར་བསམ་པས་རྟེན་ལ་ཕན་འདོགས་པ་འབྱུང་བ་སྟེ། སྐོམ་པས་གདུངས་པ་ཆུ་མཐོང་བས་མ་ཤི་བ་བཞིན་ནོ། །

[Block 364]
རྣམ་པར་ཤེས་པའི་ཟས་ནི་ཉེ་བར་ལེན་པ་དང་ལྡན་པ༌[^234]སྟེ། གང་གིས་དེ་བླངས་པ་ཉིད་ཀྱིས་རྟེན་གནས་པ་སྟེ། དེ་ལས་གཞན་དུ་ན་ཤི་བའི་རོ་བཞིན་དུ་རུལ་པར་འགྱུར་རོ། །

[Block 365]
དེ་ལྟ་བས་ན་རྟེན་ལ་ཕན་འདོགས་པར་བྱེད་པའི་ཕྱིར་རྣམ་པར་ཤེས་པའི་ཟས་ཉིད་ནི་ཁས་བླང་བར་བྱའོ། །

[Block 366]
དེ་ལ་རེག་པའི་ཟས་ནི་རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་གང་ཡིན་པའིའོ། །

[Block 367]
ཡིད་ལ་སེམས་པའི་ཟས་ནི་ཡིད་ཀྱིས་བསམས་པའིའོ། །

[Block 368]
གཞན་པ་རྣམ་པར་ཤེས་པའི་ཟས་ཉིད་དུ་བསྟན་པ་གང་ཡིན་པ་ནི་སེམས་མེད་པའི་གཉིད་དང་། བརྒྱལ་བ་དང་། འགོག་པ་ལ་སྙོམས་པར་ཞུགས་པ་ན་རྣམ་པར་ཤེས་པ་དྲུག་ནི་འགག་པར༌[^235]འགྱུར༌[^236]ན། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མེད་ན་ལུས་བླངས་པ་མི་འདྲུལ་བར་བྱེད་པ་གཞན་གང་ཡིན། དེ་ལྟར་མཉམ་པར་མ་བཞག་པའི་ཉིང་མཚམས་སྦྱོར་བའི་འབྲེལ་པ་བསྟན་ཏོ། །

[Block 369 [HEADING]]
###### མཉམ་པར་བཞག་པའི་ཉིང་མཚམས་སྦྱོར་བ། ^1-5-1-3-2-0

[Block 370]
མཉམ་པར་བཞག་པའི་ཡང་ཇི་ལྟར་མི་རུང་བ་དེ་བསྟན་པར་བྱ་སྟེ། འདི་ནི་ཉོན་མོངས་པ་ཅན་གྱི་རྣམ་པར་ཤེས་པས་ཉིང་མཚམས་སྦྱོར་ཞིང་སྦྲེལ་ཏེ། མཉམ་པར་བཞག་པའི་ས་ལ་ཉོན་མོངས་པ་ཅན་དང་། མཉམ་པར་མ་བཞག་པས་ཉིང་མཚམས་སྦྱོར་ཞིང་སྦྲེལ་ཏོ། །

[Block 371]
ཉོན་མོངས་པ་ཅན་ཞེས་བྱ་བ་ནི་དེའི་ས་པའི་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཅན་ཏེ། དེའི་ས་པའི་ཉོན་མོངས་པ་ནི་ཏིང་ངེ་འཛིན་གྱི་རོ་མྱང་བ་གང་ཡིན་པའོ། །

[Block 372]
དེའི་ཉོན་མོངས་པ་ཅན་གྱི་སེམས་ནི་མཉམ་པར་བཞག་པའི་ས་པ་ཉིད་ཀྱི་དང་། མཉམ་པར་མ་བཞག་པའི་སེམས་སོ། །

[Block 373]
མཉམ་པར་མ་བཞག་པའི་ས་འདི་ནས་ཤི་འཕོས་པ་ན་ཤི་འཕོས་པའི་སེམས་གང་ཡིན་པ་དེ་དེའི་ས་པ་དང་ཕྲད་པར་གང་གིས་ཇི་ལྟར་འགྱུར།[^237] དེས་ན་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ངེས་པར་ཁས་བླང་བར་བྱ་སྟེ། གང་ལ་ཐོག་མ་མེད་པ་ནས་ས་དེའི་སེམས་ཀྱི་བག་ཆགས་ཡོད་དེ། བག་ཆགས་གང་ལས་སེམས་དེ་ཀུན་ཏུ་རྒྱུ་བ་དེས་ཉིང་མཚམས་སྦྱོར་ཞིང་སྦྲེལ་ཏོ། །

[Block 374]
གཟུགས་མེད་པའི་ཁམས་སུ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི། གཟུགས་ལས་གྲོལ་བའོ། །

[Block 375]
ཉོན་མོངས་པ་ཅན་གྱི་སེམས་དང་དགེ་བའི་སེམས་ཞེས་བྱ་བ་ནི་ཏིང་ངེ༌[^238]འཛིན་གྱི༌[^239]རོ་མྱང་བ་ཉིད་དོ། །

[Block 376]
ས་བོན་མེད་ཅིང་གཞི་མེད་པ་ཞེས་བྱ་བ་ནི་རྒྱུ་མེད་པ་ཉིད་དང་རྐྱེན་མེད་པ་ཉིད་དོ། །

[Block 377]
དོན་གཞན་ཡང་རྒྱུ་མེད་པའི་ཕྱིར་གང་ལས་འབྱུང་བར་འགྱུར། གཞི་མེད་ན་གང་ལ་བརྟེན༌[^240]ཏེ་འཇུག་པར་འགྱུར་ན་སེམས་དེ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་རྣམ་པར་ཤེས་པས་ཡོངས་སུ་གཟུང་བའི༌[^241]རང་གི་ས་བོན་ལས་འབྱུང་བར་འགྱུར་ཏེ། དེ་ལ་བརྟེན་ནས་དེ་ཉིད་ཀྱི་རྒྱུན་རབ་ཏུ་འཇུག་པར་འགྱུར་རོ། །

[Block 378]
དེ་ཉིད་ན་འཇིག་རྟེན་ལས་འདས་པའི་སེམས་མངོན་དུ་བྱེད་པའི་ཚེ། དེ་མ་ཡིན་པ་གཞན་འཇིག་རྟེན་པའི་སེམས་མེད་པར་གྱུར་པས་དེའི༌[^242]འགྲོ་བ་ལྡོག་པ་ཉིད་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་འབད་པ་མེད་པར་ཕུང་པོ་ལྷག་མ་མེད་པར༌[^243]མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་འགྱུར་བ་ཞིག་ན། དེ་ཡང་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མེད་ན་མ་ཡིན་པས་དེ་ལྟར་ཡང་མི་འགྲུབ་བོ། །

[Block 379]
འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་སྐྱེ་མཆེད་དུ་སྐྱེས་པ་རྣམས་ཀྱང་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་པའི་འཇིག་རྟེན་ལས་འདས་པའི་སེམས་མངོན་དུ་བྱེད་པ་ན། གང་གི་ཕྱིར་སེམས་དེ་ནི་གསལ་པོར་འཇུག་པ་ཡིན་ལ། འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་སྐྱེ་མཆེད་ཀྱི་ནི་མི་གསལ་བ་ཡིན་ནོ། །

[Block 380]
དེས་ན་གསལ་བར་འཇུག་པའི་སེམས་ལ་གནས་ནས་འཇིག་རྟེན་ལས་འདས་པའི་སེམས༌[^244]མངོན་དུ་བྱེད་དེ་འཇིག་རྟེན་ལས་འདས་པའི་སེམས་གཅིག་པུ་དེའི་གཞིར༌[^245]འགྲོ་བ་གཉིས་མི་རུང་ངོ་། །འཇིག་རྟེན་པའི་ས་དེ་དག་ནི་ས་གཞན་དུ་སྐྱེས་པའི་ས་གཞན་པའི་སེམས་མངོན་དུ་བྱེད་པ་འགྲོ་བ་གཉི་གའི་རྟེན་དུ༌[^246]མི་རིགས་ལ། ཕུང་པོ་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདས་པའི་གཞིར་ཡང་སེམས་དེ་ནི་མི་རུང་ངོ་། །དེའི་ཕྱིར་འགྲོ་བ་གསུམ་པོ་དེ་དག་ཀྱང་གཞིའི་ངོ་བོར་མི་རིགས་པས་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མེད་ན་སེམས་དེ་གང་ལ་བརྟེན་པར་འགྱུར། འཇིག་རྟེན་ལས་འདས་པའི་སེམས་དེ་ལེགས་པར་བྱ་བ་བྱེད་པའམ། ཉེས་པར་བྱ་བ་བྱེད་པ་འཆི་འཕོ་བ་ན་ལུས་སྨད་དམ་སྟོད་ནས་དྲོད་ཡལ་བར་འགྱུར་བའང་མི་རུང་སྟེ་ཞེས་བྱ་བ་ལ་དེ་ལེགས་པར་བྱ་བ་བྱེད་པ་དང་། ཉེས་པར་བྱ་བ་བྱེད་པའི་ལུས་ཀྱི་སྨད་དང་སྟོད་ནས་དྲོད་ཡལ་བར་འགྱུར་ཏེ། འདི་ལྟར་ལེགས་པར་བྱ་བ་བྱེད་པ་ནི་སྨད་ནས་སོ། །

[Block 381]
ཉེས་པར་བྱ་བ་བྱེད་པ་ནི་སྟོད་ནས་སོ། །

[Block 382]
དེ་ནས༌[^247]དེ་དག་ཀྱང་ཀུན་གཞི་རྣམ་པར་ཤེས་པས་ཡོངས་སུ་གཟུང་བར་མི་འདོད་ན། ལུས་དྲོད་ཡལ་བར་འགྱུར་བ་དེ་ཇི་ལྟར་ཡིན། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་དེས་གཟུང་བས་ནི་ལུས་འདོར་བར་བྱེད་པ་ན་སྨད་དམ་སྟོད་ནས་ཇི་ལྟར་རིགས་པས༌[^248]དྲོད་ཡལ་བར་འགྱུར་རོ། །

[Block 383]
འདོར་བར་འགྱུར་རོ། །

[Block 384 [HEADING]]
#### རྣམ་པར་བྱང་བ། ^1-5-2-0

[Block 385 [HEADING]]
##### འཇིག་རྟེན་པའི་རྣམ་པར་བྱང་བ། ^1-5-2-1-0

[Block 386]
ཇི་ལྟར་ན་འཇིག་རྟེན་པའི་རྣམ་པར་བྱང་བ་ཡང་མི་རུང་ཞེ་ན། དེ་བསྟན་པར་བྱ་སྟེ། འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བར་བྱ་བའི་ཕྱིར། རབ་ཏུ་སྦྱོར་བ་ན་འདོད་པ་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བའི་སེམས་དེ་ཡང་གཟུགས་ན་སྤྱོད་པའི་སེམས་དང་ལྷན་ཅིག་འབྱུང་བ་དང་འགག་པ་མེད་པའི་ཕྱིར་དེས་བསྒོས་པ་མེད་པ་གཟུགས་ན་སྤྱོད་པའི་སེམས་དེ་ས་བོན་མེད་པར་སྐྱེ་བ་ཉིད་ཡིན་པར་འགྱུར་ཏེ། གཟུགས་ན་སྤྱོད་པའི་སེམས་འདས་པ་ཚེ་རབས་དུ་མར་སེམས་གཞན་གྱིས་བར་དུ༌[^249]བཅད་པ་དེ་ཡང་འདས་པའི་ཕྱིར་མེད་པ་ཉིད་དེ། མཉམ་པར་གཞག་པའི་སེམས་དེའི་ས་བོན་ཉིད་དུ་མི་རུང་ངོ་། །དེའི་རྒྱུ་དེའི༌[^250]རྐྱེན་ཞེས་བྱ་བ་ནི། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་གནས་པའི་རང་གི་ས་བོན་ལས་བྱུང་བའོ། །

[Block 387]
སྦྱོར་བ་ལས་བྱུང་བའི་དགེ་བའི་སེམས་དེ་ནི་ནུས་པ་མེད་པ་མ་ཡིན་པས་བདག་པོའི་རྐྱེན་ནི་དེའི་ནུས་པ་ཡིན་པས། [^251]རྒྱུའི་རྐྱེན་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 388]
དེ་བས་ན་བདག་པོའི་རྐྱེན་ལས་འདོད་པ་ན་སྤྱོད་པའི་སེམས་དེ་འབྱུང་ངོ་། །དེ་བཞིན་དུ་འདོད་ཆགས་དང་བྲལ་བ་ལ་སོགས་པ་ལ་ཡང་སྦྱར་རོ། །

[Block 389 [HEADING]]
##### འཇིག་རྟེན་ལས་འདས་པའི་རྣམ་པར་བྱང་བ། ^1-5-2-2-0

[Block 390]
ཇི་ལྟར་འཇིག་རྟེན་ལས་འདས་པའི་རྣམ་པར་བྱང་བ་མི་རུང་ཞེ་ན། དེ་བསྟན་པར་བྱ་སྟེ། དེ་ནི་གཞན་གྱི་སྒྲ་ལ་བརྟེན་པ་དང་། སོ་སོ་རང་གི་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་ཞེས་བྱ་བ་ནི། སྒྲ་དང་མཚུངས་པར་ལྡན་པའམ། ཡིད་ལ་བྱེད་པའོ། །
--- END BLOCKS ---
