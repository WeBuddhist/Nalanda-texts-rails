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
འབྲེལ་པ་ནི་རྣམ་པ་གཉིས་ཏེ་ལྡན་པ་དང་འདུ་བའོ། །

[Block 562]
དེ་ཡང་མེ་དང་དུ་བ་དང་བ་ལང་དང་རྭ་ལྟ་བུའོ་ཞེས་སོ། །

[Block 563 [HEADING]]
#### ལྡན་པ། ^2-4-1-0

[Block 564]
དེ་ལ་རེ་ཞིག །ལྡན་པའི་རྟོགས་པ་གྲུབ་པ་མེད། །ལྡན་པ་མངོན་པར་མ་ཤེས་ཀྱང་མེད་ན་མི་འབྱུང་བ་འབའ་ཞིག་ཙམ་གྱི་དྲན་པ་ལས་ཀྱང་མཐོང་བའི་ཕྱིར་རོ། །

[Block 565]
མི་རྟོགས་པར་བྱེད་པ་ལ་འབྲེལ་པ་མ་བཟུང་ན་ནི་གཞལ་བྱ་གསལ་བར་བྱེད་པའི་རྒྱུ་མཚན་དུ་རིགས་པ་མ་ཡིན་ནོ།[^445] །

[Block 566]
ཤེས་པའི་རྒྱུ་ཉིད་ལས་དེའི་ཤེས་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 567]
དེ་ལ་ཡང་ལྡན་པ་བར་གྱི་མེ་མེད་པའི་རྒྱུ་མཚན་ཡིན་ན་ནི་མེ༌[^446]ཡང་དུ་བའི་ཤེས་པའི་རྒྱུར་ཐལ་བར་འགྱུར་ཏེ། ལྡན་པ་ནི། གཉིས་དང་ལྡན་ཕྱིར། གཉིས་ཀ་ཡང་གསལ་བར་བྱེད་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 568]
ལྕགས་གོང་དང་སོལ་མེའི་གནས་སྐབས་སུ༌[^447]དུད་པ་མེད་པའི་མེ་ཡང་མཐོང་བ་ཡིན་ནོ། །

[Block 569]
གལ་ཏེ་དམིགས་ཀྱིས་བསལ་བས་གཅིག་ནི་གཏན་ཚིགས་སུ་མི་འགྱུར་ཏེ། ཐེ་ཚོམ་ཅན་ནི་གཏན་ཚིགས་མ་ཡིན་ནོ་ཞེས་དམིགས་ཀྱིས་བསལ་བ་ཡོད་པས་ན༌[^448]དེ་ལས་མེའི་རྒྱུ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 570]
མེ་དུ་བ༌[^449]དང་གདོན་མི་ཟ་བར་ལྡན་པ་ནི་མ་ཡིན་ཞིང་། དུ་བ༌[^450]ནི་གདོན་མི་ཟ་བར་མེ་དང་ངོ་ཞེ་ན། དེ་ཡང་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཐ་དད་མིན། ཕྱིར་ཞེས་པ་ནི་ཚིག་གི་ལྷག་མའོ། །

[Block 571]
ལྡན་པ་ནི་ཐ་དད་པ་མ་ཡིན་ཏེ། དེ་ནི་གཅིག་ལ་ཇི་ལྟ་བ་བཞིན་དུ་གཉིས་པ་ལ་ཡང་ཡིན་པའི་ཕྱིར་གཅིག་རྒྱུ་མ་ཡིན་པར་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 572]
ལན་ཅིག་གི༌[^451]འབྲེལ་པ་མ་ཟིན་ན་ནི་རྒྱུ་འཇལ་བར་བྱེད་པ་མི་འཐད་ན་ཡང་འདིའི་འཁྲུལ་པ་ཉིད་གང་ལས་རྣམ་པར་དཔྱོད། གང་མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པའི་ལྟར་ན་ནི་འདིར་གཉིས་ཀ་ནི་མ་ཡིན་གྱི་གདོན་མི་ཟ་བར་གཅིག་ཁོ་ན་རྒྱུ་ཡིན་ནོ་ཞེས་འཐད་པ་ཡིན་ནོ། །

[Block 573 [VERSE]]
མེ་དང་ལྡན་པའི་དུ་བ་ནི། །
ཆ་འགའ་ཞིག་ལས་མ་ཡིན་པས། །
དུ་བའི་ཐམས་ཅད་གོ་བྱེད་དམ། །
མེ་ཡི་བསལ་བའམ༌[^452]གོ་བྱར་འགྱུར། །

[Block 574]
ལྡན་པའི་འབྲེལ་པ་ལྟར་ན་ནི། །མེའི་རྣོ་བ་དང་གསལ་བ་ལ་སོགས་པའི་བྱེ་བྲག་རྣམས་ཀྱང་ཐོབ་པར་འགྱུར་ཏེ། ཐམས་ཅད་ཀྱི་བདག་ཉིད་ཀྱིས་ལྡན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 575]
དེ་བཞིན་དུ་ཡང་དུ་བའི་རྫས་ལ་སོགས་པ་ཙམ་བཟུང་བའི་བདག་ཉིད་དེ་ནས་ཀྱང་མེ༌[^453]རྟོགས་པར་བྱེད་པར་འགྱུར་ཏེ། དེ་རྫས་ལ་སོགས་པའི་དངོས་པོ་དང་ལྡན་པ་མ་ཡིན་པ་ནི་མ་ཡིན་ནོ། །

[Block 576]
ཇི་ལྟར་ལྡན་པ་ལ་སྐྱོན་ཡོད་པ། དེ་བཞིན་དུ༌[^454]བ་ལ་སོགས་པའང་། དེ་ལ་ཡང་བ་ལང་ར་ཅན་ཡང་མ་ཡིན་ལ༌[^455]ཡང་ན་སེར་ཟལ་ལ་སོགས་པའི་བྱེ་བྲག་ཀྱང་རྫས་ཉིད་ལ་སོགས་པའི་སྤྱིས་གོ་བར་འགྱུར་རོ། །

[Block 577]
དེ་ལྟར་དོན་གཅིག་ལ་འདུ་བ་ལ་འདུ་བ་མི་འཐད་པར་བརྗོད་དོ། །

[Block 578]
འགལ་བ་ཡང་ནི་སྲིད་པའི་ཕྱིར། །ཇི་ལྟར་སྲིད་པ་ལྟར་བརྗོད་པར་བྱ་སྟེ། གང་དུ་མངོན་དུ་མ་གྱུར་པའི་འབྱུང་བ་ཡང་རྟགས་དང་རྟགས་ཅན་དུ་བརྗོད་པར་བྱའོ། །

[Block 579]
དེ་བཞིན་དུ་མངོན་དུ་གྱུར་པ་ལ་ཡང་བྱེ་བྲག་དང༌[^456]སྤྱིས་ཕན་ཚུན་རྟགས་དང་རྟགས་ཅན་དུ་བརྗོད་པར་བྱ་སྟེ། དེ་ཆ་འགའ་ཞིག་གི་སྒོ་ནས་འགལ་བ་ནི་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 580]
ཡང་བརྗོད་པ།

[Block 581 [VERSE]]
རྟགས་ཀྱི་སྤྱི་གཞན་རྟགས་མིན་ཞིང་། །
བྱེ་བྲག་རྣམས་ཀྱང་རྟགས་ཅན་མིན། །
གཞན་གྱི་ལྟར་ན་ཐམས་ཅད་ནས། །
གོ་བྱ་གོ་བྱེད་དུ་ཡང་འགྱུར། །

[Block 582]
ཞེས་བྱ་བ་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 583]
ལྡན་པ་རྗེས་སུ་དཔོག་པར་བྱེད་པའི་རྒྱུ་ཡིན་ན་ནི་དཔག་པར་བྱ་བ་ལྡན་པ་ཙམ་རྟོགས་པར་ཐལ་བར་འགྱུར་ཏེ། གཞན་དུ་ན་རྟགས་ལ་རྟགས་ཅན་ཤེས་པའི་ནུས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 584]
དེ་བཞིན་དུ་འདུ་བ་ལ་སོགས་པ་ལ་ཡང་བརྗོད་པར་བྱའོ། །

[Block 585]
གལ་ཏེ་འདིར་དུད་པས་མེའི་ཡོད་པ་ཙམ་གྲུབ་པ༌[^457]ནི་མ་ཡིན་ཏེ། དེ་སྒྲུབ་པའི༌[^458]ཕྱིར་རོ། །

[Block 586]
གང་ལ་དུད་པ་ཡོད་པའི་ས་ཕྱོགས་དེར་མེ་དང་ལྡན་ནོ་ཞེས་བསྒྲུབ་པར་བྱ་བ༌[^459]སྟེ། དེ་ལྟ་མ་ཡིན་ན་འདིར་ཞེས་པ་དོན་མེད་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 587]
དེ་ལྟར་ན་མེས་ཀྱང་དུད་པའམ་མེའི་རྣོ་བ་ལ་སོགས་པ་ལ༌[^460]ཡང་ཞེས་བྱ་བ་ཡང་མི་འབྱུང་ངོ་ཞེ་ན། དེ་ལྟར་ན་ནི་དམ་བཅའ་བའི་ཕྱོགས་གཅིག་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 588]
དེའི་ཕྱིར་གདོན་མི་ཟ་བར་རྟགས་དང་རྟགས་ཅན་ལྡན་པ་ལས་ནི་མ་ཡིན་གྱི། འོན་ཀྱང་མེད་ན་མི་འབྱུང་བ་ཁོ་ན་ལས་སོ། །

[Block 589]
ཡུལ་དང་དུས་ལ་ལྟོས་སུ་ཆུག །དེ་ནི་ཡུལ་ལ་ལྟོས་ཀྱང་མེད་ན༌[^461]མི་འབྱུང་བ་ཉིད་ཡིན་ཏེ། སྔར་ས་ཕྱོགས་སུ་མེ་མེད་ན་དུད་པ་མི་འབྱུང་བར་དམིགས་པའི་ཕྱིར་རོ། །

[Block 590]
དུས་ལ་ལྟོས་པའི་ཕྱོགས་ལ་ཡང་། །གཙུབ་ཤིང་གཙུབས་པའི༌[^462]གནས་སྐབས་ན། །

[Block 591]
ཇི་སྲིད་དུ་མེ་མེད་ཀྱི༌[^463]དུས་དེ་སྲིད་དུ་དུད་པ་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 592]
དེའི་ཕྱིར་དུད་པས་མེ་དཔོག་པའི་རྒྱུར་ལྡན་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 593 [HEADING]]
#### འདུ་བ། ^2-4-2-0

[Block 594]
འདུ་བ་ཡང་བ་ལང་གི་རྭ་ཡོད་པར་དཔོག་པའི་རྒྱུ་མ་ཡིན་ཏེ། མངོན་སུམ་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 595]
འབྲེལ་པ་ཡོད་དུ་ཟིན་ཀྱང་། རྒྱུ༌[^464]ནི་ཁོང་དུ་ཆུད་མི་འགྱུར། །འབྲེལ་པ་མ་དམིགས་པར་མངོན་པར་གསལ་བར་བྱེད་པ་ནི་མི༌[^465]འདོད་དོ། །

[Block 596]
འདུ་བ་ཡོད་དུ་ཟིན་ཀྱང་རྟོགས་པ་ནི་མེད་ན་མི་འབྱུང་བ་ཉིད་དམིགས་པ་ཁོ་ན་ལས་ཡིན་པའི་ཕྱིར། དེ་ཁོ་ན་རྒྱུ་ཡིན་ནོ། །

[Block 597 [HEADING]]
#### དོན་གཅིག་ལ་འདུ་བ། ^2-4-3-0

[Block 598]
དོན་གཅིག་ལ་འདུ་བ་ནི་རྣམ་པ་གཉིས་ཏེ། འབྲས་བུ་དང་འབྲས་བུ་གཞན་དང་། རྒྱུ་དང་རྒྱུ་གཞན་ནོ། །

[Block 599]
དེར་ཡང་དཔེར་ན་གཟུགས༌[^466]རེག་བྱ་ལྟ་བུ་དང་ལག་པ་དང་། རྐང་པ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 600]
འདི་ལ་ཡང་དེ་ཉིད་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
