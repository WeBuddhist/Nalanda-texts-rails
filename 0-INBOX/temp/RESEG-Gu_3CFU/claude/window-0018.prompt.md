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
[Block 631]
སྲོགས་ཆགས༌[^448]ཀྱི་ཆེད་ནི་འདིར་རྨ་ལ་གནས་པའི་སྲོག་ཆགས་རྣམས་ལ་དགོངས་པར་རིགས་པ༌[^449]ཡིན་ཏེ། ཤིག་ལ་སོགས་པའི་དགོངས་པ་ནི་མ་ཡིན་ནོ། །

[Block 632]
འདི་ལ་ཡང་རྨའི་ཆེད་ཉིད་ཀྱི་ནང་དུ་བསྡུས་པ༌[^450]ཉིད་དེའི་ཕྱིར་མ་བཟུང་ངོ་། །བྱིན་པའི་སྤུ་བྲེག་པ་ཡང་དེའི་ཕྱིར་མ་ཡིན་པར་བྱེད་དུ་མི་གཞུག་གོ་ཞེས་བྱ་བ་ལ། དེའི་ཕྱིར་མ་ཡིན་པ་ནི་རྨའི་ཕྱིར་མ་ཡིན་པའོ། །

[Block 633]
བྱིན་པའི་སྤུ་བྲེག་པ་ནི་ཡན་ལག་གི་སྤུའོ། །

[Block 634]
ལུས་གཞན་གྱི་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མདོམས༌[^451]དང་བྱིན་པ་དག་ལས་གཞན་པའི་ལུས་ནི་མགྲིན་པ་མན་ཆད་གང་ཞིག་ལུས་ཀྱི་ཐ་སྙད་དེ་ལ༌[^452]ཡང་སྤུ་བྲེག་པའི་ལས་འདི་བཀག་པའོ། །

[Block 635]
དེ་བས་ན་འདིར་སྐྲ་དང་ཁ་སྤུ་དག་ལ་ཡང་བྱ་བ་ཉིད་བཀག་པ་མ་ཡིན་ནོ། །

[Block 636]
སྣའི་སྤུ་བྲེག་པ་ལ་ནི་ཚིག་ཡོད་དེ་དེའི་ཕྱིར་གྲགས་པ་ལ་ཡིད་ཆེས་པའོ། །

[Block 637]
འདིར་མ་མོའི་གཞུང་ལས་སྐྲ་དང་ཁ་སྤུ་མ་གཏོགས་པ་དེ་ལས་གཞན་པའི་ཡན་ལག་དང་ཉིང་ལག་རྣམས་ཀྱི་སྤུ་བྲེག་པར་མི་བྱའོ། །

[Block 638]
གང་ཞིག་འབྲེག་པར་གྱུར་ན་ཉེས་བྱས་ཀྱི་ལྟུང་བར་འགྱུར་རོ་ཞེས་འབྱུང་ངོ་། །སེན་མོ་སྤུ་གྲིའི་སོ་ལྟ་བུ༌[^453]འམ་སྟེའུའི་ཁ་ལྟ་བུར་བྲེག་པར་བྱའོ། །

[Block 639]
དེ་དག་སྤྱིལ་བར་མི་བྱའོ། །

[Block 640]
དྲི་མ་བསལ་བའི་ཕྱིར་བྲུད་པར་བྱའོ། །

[Block 641]
ཆོས་གོས་གྱོན་བཞིན་དུ་སྐྲ་དང་ཁ་སྤུ་བྲེག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བླ་གོས་ལ་འདིར་གཟུང་བར་བྱའི། མཐང་གོས་ལ་ནི་མ་ཡིན་ནོ། །

[Block 642]
མཐང་གོས་ཐམས་ཅད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 643]
དེ་བས་ན་ཆོས་གོས་དང་བླ་གོས་དག་ཉིད་ལ་སྟེ། འདིར་རྙིང་པ་དུས་གཞན་དུ་སྟེང་དུ་བགོས་པ་ལ་རིགས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིར་བཀག་པའི་རྒྱུ་མཚན་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 644]
སྐྲ་བཟེད་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་སྐྲ་བཟེད་པའི་གོས་བཅང་བར་བྱ་སྟེ། དོན་དེ་ཉིད་ལ་གང་དགོས་པའོ། །

[Block 645]
འདི་སྐྲ་རྣམས་སོ་སོར་འཛིན་པས་ན༌[^454]སྐྲ་བཟེད་དོ་ཞེས་བྱ་བ་ནི༌[^455]ངེས་པའི་ཚིག་གོ། །

[Block 646]
འདི་ཅིའི་ཕྱིར་གོས་ཞེས་བརྗོད་ཅེ་ན། གོས་འདི་སྐྲ་བཟེད་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བས་བྱིན་གྱིས་བརླབ༌[^456]པའི་སྔགས་ལས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 647]
བགོ་བའི་དོན་དུ་སླར་འདི་ཇི་ལྟར་རྣམ་པར་ཤེས་ཤེ་ན། སླར་དེ་ཉིད་དུ་སྐྲ་རྣམས་ཉེ་བར་བཅང་བའི་དོན་དུ་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 648]
མེད་ན་རྔུལ་གཟན་གྱིས་སོ་ཞེས་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 649]
རྔུལ་གཟན་དུ་སྐྲ་བྲེག་པ་ནི་མ་བཀག་པའོ། །

[Block 650]
མེད་ན་རྔུལ་གཟན་གྱིས་སོ་ཞེས་བྱ་བ་ནི་སྐྲ་བཟེད་པའི་གོས་མེད་ན་རྔུལ་གཟན་གྱོན་པས་སྐྲ་དང་ཁ་སྤུ་དག་བྲེག་པར་བྱའོ། །

[Block 651]
བཏིང་བར་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྐྲ་དང་ཁ་སྤུ་དག་བྲེག་པར་མི་བྱའོ། །

[Block 652]
འདིར་གླེང་གཞི་ལ་ཡང་དང་པོ་ཉིད་དུ་སེན་མོ་བྲེག་པ་ཞེས་བྱ་བའི་ཐ་མར་གཞུང་ནི་འདི་ཡིན་ཏེ། གང་དུ་དགེ་འདུན་ཕྱག་དར་འཕྱག་པར་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་འདི་ནི་གཙུག་ལག་ཁང་གི༌[^457]དབང་དུ་བྱས་པ་ཡིན་ནོ། །

[Block 653]
རྒན་པོ་དང་ནད་པ་དང་རླུང་དང་ཉི་མ་དང་ཆར་པ་དག་ལ་ཁྱམས་ལ་སོགས་པར་བྲེག་ཏུ་གཞུག་པར༌[^458]བྱའོ། །

[Block 654]
ཕྱོགས་དེར་བྱི་དོར་བྱའོ། །

[Block 655]
བྱི་དོར་བྱ་བ་ནི་སྐྲ་མེད་པ་ཉིད་དང་ཆུ་མེད་པ་ཉིད་དང་།

[Block 656 [VERSE]]
དེ་ཇི་ལྟར་བསྒྲུབ་པ༌[^459]དེ་ལྟར་བྱའོ། །
སྐྲ་ནི་ཕྱག་དར་ཁྲོད་དུ་དོར། །

[Block 657]
ཞེས་བྱ་བ་ནི་ཕྱག་དར་ཁྲོད་ཀྱི་ཕྱོགས་སུའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 658]
སེན་མོ་བཅས༌[^460]ཡང་དེ་བཞིན་ནོ། །ཞེས་བྱ་བ་ནི་བཏིང་བར་ཡང༌[^461]མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་འདྲེ་བ༌[^462]འདི་ཡིན་ནོ། །

[Block 659]
སྐྲ་བཟེད་ལ་མཁས་པ་མཛེས་པར་བྱེད་པར་འགྱུར་བས་ལས་བྱ་བར་འགྱུར་རོ། །

[Block 660]
དེ་བས་ན་འདིར་བཅད་པ་ནི་གང་དུ་དགེ་འདུན་ཕྱག་དར་འཕྱག་པར༌[^463]མི་བྱའོ་ཞེས་བྱ་བ་འདི༌[^464]ལས་འདའ་བ་ཉིད་དམ་ས་ལ་བྱི་དོར་བྱ་བ་ཉིད་དོ། །

[Block 661]
སྐྲ་དང་ཁ་སྤུ་བྲེག་པ་སྤང་བ༌[^465]འདི་ལ་མི་སྲིད་པར་རིག་པར་བྱའོ། །

[Block 662]
དེ་འདོད་ཆགས་དང་བྲལ་བ་མ་ཡིན་ན་དགེ་སློང་མས་འདི་ཞལ་ཏ་མ་བྱས་པར་སྐྱེས་པས་སྐྲ་མི་བྲེག་གོ་ཞེས་བྱ་བ་ལ། འདི་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་འདོད་ཆགས་དང་བྲལ་བ་མ་ཡིན་པ་ཞེས་བྱ་བའོ། །

[Block 663]
གལ་ཏེ་འདོད་ཆགས་དང་བྲལ་བར་གྱུར་ན་ལྟུང་བ་མེད་དེ་ཞེས་བྱ་བའི་གཞུང་འདི་ལ་བྲེག་པར་བྱའོ་ཞེས་བྱ་བ་བྲེག་པ༌[^466]ཉིད་འདིར་འདི་ལྟ་བུའི་ཚིག་གོ། །

[Block 664]
དེ་ནས་སྐྱེ་དགུའི་བདག་མོ་གཽ་ཏ་མ་ཆེན་པོ་ཤཱཀྱའི་དགེ་སློང་མ་བརྒྱ་ཕྲག་དང་ལྷན་ཅིག་ཏུ་རང་ཉིད་ཀྱིས་སྐྲ་བྲེགས་ཏེ། གོས་ངུར་སྨྲིག་གྱོན་ནས་ཞེས་བྱ་བ་སྐྲ་བྲེག་པ་གསུངས༌[^467]ལ། དེ་བཞིན་དུ་གཽ་ཏ་མ་ཁྱོད་ཀྱིས་མགོ་བོ་རྣམས་མཛེས་པར་གྱིས་ཤིག་ཅེས་བྱ་བ་མགོ་བོ་ཉིད་དུ་བརྗོད་པའི་ཕྱིར་སྐྲ་རྣམས་རིང་བ་ཉིད་ཀྱིས་གཞན་གྱིས་བྲེག་པ་ལ་རྒྱུ་མཚན་དང་བཅས་པ་འདི་བརྗོད་པའོ། །

[Block 665]
གཞན་དུ་ནི་ཐ་སྙད་དེ་འདོད་ཆགས་དང་མ་བྲལ་བའི་དགེ་སློང་མ་ནི་དགེ་སློང་མས་ཞལ་ཏ་མ་བྱས་པས་སྐྲ་མི་བྲེག་གོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 666]
ཀུན་ཏུ་ཆགས་པར་གྱུར་ན་ཞལ་ཏ་བྱེད་པ་མོས་རྗེས་སུ་བསྟེན་པར༌[^468]བྱའོ། །

[Block 667]
དྲན་པ་ཉེ་བར་ཞོག་ཅིག །ཅི་རྣག་གི་ལུས་འདི་ལ་སྙིང་པོ་ཡོད་དམ་ཞེས་སོ་ཞེས་བྱ་བ་ལ། ཀུན་ཏུ་ཆགས་པར་གྱུར་ན་ཞེས་བྱ་བ་ནི་འབྲེག་མཁན་ལ་དགེ་སློང་མ༌[^469]དེའོ། །

[Block 668]
འབྲེག་མཁན་ལ་ནི་མ་དང་སྲིང་མོ་དང་བུ༌[^470]མོའི་འདུ་ཤེས་ཉེ་བར་ཞོག་ཅིག་ཅེས་སོ་ཞེས་བྱ་བ་ལ། ཀུན་དུ་ཆགས་པར་གྱུར་པ་ལ་ཞལ་ཏ་མོས་མ་ལ་སོགས་པའི་འདུ་ཤེས་ཉེ་བར་ཞོག་ཅིག་ཅེས་བྱ་བ་ལ༌[^471]ཡང་དག་པར་རྗེས་སུ་བསྟན་པར་བྱའོ། །

[Block 669]
དེ་བྱས་ནས་ཁྲུས་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་དེ་ཞེས་བྱ་བ་ནི་སྐྲ་དང་ཁ་སྤུ་བྲེག་པ་ལའོ། །

[Block 670]
ཡང་ན་ཡན་ལག་ལྔའི་ཁྲུས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་ན་ཞེས་བྱ་བའི་སྒྲ་ནི་ཆོ་ག་གཞན་བསྟན་པའི་དོན་ཏོ། །
--- END BLOCKS ---
