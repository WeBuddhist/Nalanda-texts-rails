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
[Block 491]
དེ་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་དེའི་ལས་ཁྱད་པར་ཅན་ནོ། །

[Block 492]
ལས་ཁྱད་པར་ཅན་དེས་ངོ་མཚར་བ་དེ་ནི་སྤྱོད་པ་ཁྱད་པར་ཅན་ངོ་མཚར་རོ། །

[Block 493]
དེ་བས་ན་མྱ་ངན་དང་སྡུག་བསྔལ་ནི་མྱ་ངན་དང་སྡུག་བསྔལ་ཏེ། མྱ་ངན་ནི་བླ་མ་སྡུག་པ་དང་བྲལ་བས་སོ། །

[Block 494]
སྡུག་བསྔལ་ནི་མྱ་ངན་གྱིས༌[^218]ཀུན་ནས་བསླང་བ་སྟེ། ལུས་དང་སེམས་ཀྱི་སྡུག་བསྔལ་ལོ། །

[Block 495]
དེ་གཉིས་ཀྱི་ཤུགས་ཀྱིས་ཡང་དག་པར་བསྐྱེད་པའོ། །

[Block 496]
བཏང་བ་ནི་སྤངས་པ་སྟེ། གང་གི་མྱ་ངན་དང་སྡུག་བསྔལ་གྱི་ཤུགས་བཏང་བ་གང་ཡིན་པ་དེ་ནི་མྱ་ངན་དང་སྡུག་བསྔལ་གྱི་ཤུགས་བཏང་བའོ། །

[Block 497]
ཀྱེ་མའོ་སྡུག་བསྔལ་ཞེས་བྱ་བའི་ཚིགས༌[^219]བཅད་ཕྱེད་ཀྱི་བྱེད་པས་ནི་ཤེས་རབ་ཀྱི་དབང་དུ་བྱས་ཏེ། སེམས་ཅན་ལ་བརྩེ་བའི་སྙིང་རྗེའི་བསམ་པ་དང་། དེ་ལ་ཆགས་པ་མེད་པའི་ཤེས་རབ་སྟེ། དེ་གཉི་ག་བྱང་ཆུབ་ཀྱི་རྩ་བ་སྟེ། དེ་བས་ནི་འདི་དང་པོར་སྨོས་པས་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 498]
གཞན་གྱི་ཞེས་བྱ་བ་འདི་ནི་གཉིས་པོ༌[^220]འདི་ཡིན་ཏེ། དེའི་དབང་དུ་བྱས་ནས། གཉིས་པའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་དོན་དམ་པ་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དམ་པ་རྣམས་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སྙིང་རྗེ་དང་ལྡན་པ་ནི་ངོ་མཚར་གྱི་བྱ་བ་ཡིན་ཏེ། ངོ་མཚར་དུ་བྱས་པར་གྱུར་པས་སོ། །

[Block 499]
གཞན་གྱི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་མ་ཡིན་པ་རྣམས་ཀྱིའོ། །

[Block 500]
ཨེ་མའོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་འདིའི་ཕྱེད་ཀྱིས་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྦྱོར་བ་དང་། བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 501]
འོག་མ་ཕྱེད་ཀྱིས་ནི་དེའི་འབྲས་བུ་སྨིན་པ་ཡིན་ནོ། །

[Block 502]
ཕྱག་གི་གནས་ཞེས་བྱ་བ་ནི་རྟེན་དུ་གྱུར་པའོ། །

[Block 503]
དེ་ནས་རང་བཞིན་ཞི་བ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་བྱང་ཆུབ་སེམས་དཔའ་བདག་གི་རྒྱུད་རབ་ཏུ་སྟོན་ཏོ། །

[Block 504]
རང་བཞིན་ཞི་བ་ཉིད་ནི་ས་བཞིན་དུ་བརྟན་པ༌[^221]ཡིན་ཏེ། མི་བཟོད་པ་མེད་པའི་རྒྱུས་སོ། །

[Block 505]
མི་བཟོད་པ་མེད་པ་འདིས་ནི་མྱུར་དུ་བྱེད་པ་སྟོན་པ་ཡིན་ནོ། །

[Block 506]
སྐྱོན་དུ་གྱུར་པ་ཡིན་པས་དང་པོ་དེའི་སྡུག་བསྔལ་སྐྱེ་བ་ནི་མེད་དོ། །

[Block 507]
མགོན་པོ་འདིས་ནི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་འདིས་ནི་འགྲོ་བའི་དགྲ་དང་བདུད་འདི་གཉིས༌[^222]ཏེ།

[Block 508 [VERSE]]
དེ་གཉིས་ཀྱི་བྱེ་བྲག་དང་ལྡན་པའོ། །
གཞན་གྱིས་ཕམ་གྱིས་དོགས་པའི་བདུད་དག་ཀྱང་། །

[Block 509]
ཞེས་བྱ་བ་ཡིན་ཏེ། བདུད་ཀྱང་གཞན་གྱིས་ཕམ་དུ་དོགས་པ་སྐྱེ་བར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་གཞན་གྱིས་ཕམ་དུ་དོགས་པའོ། །

[Block 510]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྐྱབས་སུ་གྱུར་པ་ཞེས་བྱ་བ༌[^223]འདི་ནི་བསྟན༌[^224]པའོ། །ཇི་ལྟར་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྐྱབས་ཡིན་ཞེ་ན། ཐུགས་རྗེ་ཤིན་ཏུ་རླབས་ཆེ་བ་དང་། སྙིང་སྟོབས་དཔག་ཏུ་མེད་པས་སོ། །

[Block 511]
སྙིང་སྟོབས་དཔག་ཏུ་མེད་པ་ནི་ཤེས་རབ་དཔག་ཏུ་མེད་པའོ། །

[Block 512]
དེ་གཉི་གའི་སྦྱོར་བ་དོན་ཇི་ལྟ་བ་བཞིན་ཡོད་པས་བྱང་ཆུབ་སེམས་དཔའ་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་དོན་ཇི་ལྟ་བ་ཉིད་དོ། །

[Block 513]
སློབ་མ་ཞེས་སྨོས་པ་ནི་མི་དག་བཟུང་སྟེ། དེ་ན་གཞན་མི་དག༌[^225]མེད་པས་སོ། །

[Block 514]
དྲི་ཟ་དང་གནོད་སྦྱིན་ཞེས་བྱ་བ་ནི་གཤོལ་མདའ་འཛིན་པ་ལ་སོགས་པའི་རིའི་བར་དག་ལ་གནས་པས་སོ། །

[Block 515]
ཀླུ་ཞེས་སྨོས་པས༌[^226]ནི། འདི་ནས་འོག་ན་གནས་པའི་སྦྲུལ་གཟུང༌[^227]ངོ་། །སུམ་ཅུ་རྩ་གསུམ་གྱི་བདག་པོ་ཞེས་སྨོས་པས་རི་རབ་ལ་གནས་པ་རྣམས་གཟུང་ངོ་། །དེ་དག་གིས༌[^228]སྐུ་གདུང་གི་སྟེང་དུ་ས་གཞི་ཐམས་ཅད་གཡོགས་པར་གྱུར་པ་སྟེ།[^229] ཕྲེང་བ་ལ་སོགས་པ་སྨོས་པས་ནི་གོས་དང་ཡོ་བྱད་རྣམས་གཟུང༌[^230]ངོ་། །རྒྱན་ཞེས་སྨོས་པས༌[^231]ནི་ཡོ་བྱད་དེ། དྲི་ཞིམ་པོའི་ཡོ་བྱད་དང་། གོས་ཀྱི་ཡོ་བྱད་དང་། ཕྲེང་བ་དང་། གོས་དང་། རྒྱན་དང་། རྒྱན་གྱི་ཡོ་བྱད་རྣམས་སོ། །

[Block 516]
ཙནྡན་གྱི་ཕྱེ་མ་ནི་དྲི་ཞིམ་པོའི་ཡོ་བྱད་དོ། །

[Block 517]
དེ་ལ་སོགས་པ་འཇིག་རྟེན་པ་རྣམས་ཀྱིས་མངོན་པར་མཆོད་དེ།[^232] མཆོད་པའི་ཡོ་བྱད་རྣམས་ཀྱིས་དེ་ཉིད་དུ་སློབ་མ་ལ་སོགས་པས་མཆོད་པ་བྱས་པའོ། །

[Block 518]
རབ་ཏུ་དད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་མ་དད་པ་རྣམས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 519]
དད་པ་སྐྱེད་པ་རྣམས་ཀྱིས་ནི༌[^233]དགའ་བ་སྐྱེད་པ་ཞེས་པ་ནི། དད་པ་རྣམས་ཕྱིར་ཞིང་ཉེ་བར་འགྲོ་བར་བྱ་བའི་ཕྱིར་བསྟན་པར་བྱའོ། །

[Block 520]
གནས་ནི་གནས་སུ་གྱུར་པ་སྟེ། དད་པ་དང༌[^234]དགེ་བའི་ཆོས་སྐྱེ་བའི་གནས་ཡིན་པས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་གནས༌[^235]ཏེ། གནས་དེ་དག་ལ་དད་པར་བྱའོ། །

[Block 521]
དེ་ལྟར་གནས་དེ་ལ་དད་པར་བྱས་ནས་ཆོས་ལ་རིམ་གྲོ་བསྐྱེད་ཅིང་ཆོས་མཉན་པར་བྱས་ཏེ་རབ་ཏུ་བྱེད་པ་སྒྲུབ་པ་དང་། ངོ་བོ་ཉིད་ཁྱད་པར་ཅན་སྒྲུབ་པ་ལ་འབད་དེ་གནས་པར་བྱའོ་ཞེས་པ་ཡིན་ནོ། །

[Block 522]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་ཀྱི་མདོ་དང་མཐུན་པའི་རྒྱ་ཆེར་བཤད་པ་ལས་སྟག་མོའི་སྐྱེས་པའི་རབས་ཏེ་དང་པོའོ།། །།

[Block 523 [HEADING]]
## ཡུལ་ཤི་བི་པའི་སྐྱེས་པའི་རབས། ^2-0

[Block 524]
དཔག་ཏུ་མེད་པའི་དུས་ནས་གོམས་པ་ནི་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་དུ་གོམས་པར་བྱས་པའོ། །

[Block 525]
བསོད་ནམས་ཀྱི་ལས་བྱས༌[^236]ཤིང་འདྲིས་པ་ཞེས་བྱ་བ་ནི་སྦྱིན་པའི་རྒྱུ་མཐུན་པ་དང་རྣམ་པར་སྨིན་པའི་ནུས་པའི་འབྲས་བུ༌[^237]ཡིན་ཏེ། བསོད་ནམས་ཀྱི་ལས་བརྟག་པ༌[^238]དང་གུས་པར་བྱེད་པའི་སྦྱོར་བ་གཉིས་ཀྱིས་ནི་དོན་གཉིས་འགྲུབ་པ་ཡིན་ནོ། །

[Block 526]
རྟག་ཏུ་སྦྱོར་བས་ནི་བསོད་ནམས་ཀྱི་ལས་རྒྱུ་མཐུན་པའི་འབྲས་བུ་སྦྱོར་བ་ཡིན་ཏེ། རྟག་པར་བྱེད་པའི་བག་ཆགས་ཀྱིས་ཕྱིས་ཀྱང་བསོད་ནམས་ཀྱི་བྱ་བ་མངོན་པར་བསྒྲུབ་པ༌[^239]ཡིན་པའི་ཕྱིར་རོ། །

[Block 527]
གུས་པར་བྱ་བའི་སྦྱོར་བས་ནི་བསོད་ནམས་ཀྱི་ལས་རྒྱ་ཆེར་སོགས་ཤིང་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་སྦྱིན་པའི་ངེས་པར་འབྱུང་བར་འགྱུར་རོ། །

[Block 528]
དེ་ཡང་བསོད་ནམས་ཀྱི་ལས་གོམས་ཤིང་འདྲིས་པར་བྱས་པ་སྟེ། དཔག་ཏུ་མེད་པའི་དུས་ནས་གོམས་པར་བྱས་པས༌[^240]སོ། །

[Block 529]
བསོད་ནམས་ཞེས་སྨོས་པས༌[^241]ནི་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཟུང་ངོ་། །དེ་བས་ན་དེ་ཉིད་ཀྱིས༌[^242]རྒྱལ་པོ་ཉིད་དུ་གྱུར་པ་ཡིན་ཏེ། བསོད་ནམས་ཀྱི་འབྲས་བུའི་སྟོབས་ཀྱིས་སོ། །

[Block 530]
རྒྱལ་པོ་དག༌[^243]གི་བུ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་རང་གི་སྐྱེ་བོ་བཞིན་དུ་སྐྱེ་དགུ་སྐྱོང་བར་གྱུར་པའོ། །
--- END BLOCKS ---
