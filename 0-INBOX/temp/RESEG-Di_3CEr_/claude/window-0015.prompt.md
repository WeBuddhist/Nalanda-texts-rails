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
[Block 526]
ཆོས་ཀྱི་དོན་དུ་མ་ཡོད་པ་ལ་དུ་བས་གོ་བར་བྱ་བའི་ཆ༌[^418]ནི་གང་ཡིན། དུ་བ་ཡང་གང་གི་ཆ་ནས་གསལ་བར་བྱེད་ཅེས་ནི་མ་བསྟན་ཏོ། །

[Block 527 [HEADING]]
### རིགས་པ་ཅན། ^2-3-0

[Block 528]
རིགས་པ་ཅན་རྣམས་ན་རེ་དེ་སྔོན་དུ་སོང་བ་ཅན་གྱི་རྗེས་སུ་དཔག་པ་ནི་རྣམ་པ་གསུམ་སྟེ། སྔ་མ་དང་ལྡན་པ༌[^419]དང་། ལྷག་མ་དང་ལྡན་པ་དང་། སྤྱིར་མཐོང་བ་ཅན་ནོ་ཞེས་ཟེར་རོ། །

[Block 529 [HEADING]]
#### མངོན་སུམ་སྔོན་དུ་འགྲོ་བ། ^2-3-1-0

[Block 530]
དེ་ལ་རེ་ཞིག་མངོན་སུམ་སྔོན་དུ་འགྲོ་བ་ནི་རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར། འབྲེལ་པ་དབང་པོའི་གཟུང་བྱ་མིན། །རྟགས་དང་རྟགས་ཅན་གྱི་འབྲེལ་པ་ནི་དབང་པོའི་ཤེས་པའི་ཡུལ་ཡང་མ་ཡིན་ལ་རྟགས་དང་རྟགས་ཅན་མངོན་སུམ་པའང་མ་ཡིན་ན་དེ་མངོན༌[^420]དུ་སོང་བ་ཅན་ནི་རྗེས་སུ་དཔག་པའོ་ཞེས་གང་གིས་འགྱུར། ཇི་ལྟར་ན་རྗོད་པར་བྱེད། སྔ་མ་དང་ལྡན་པ་ཞེས་བྱ་བ་འདི་ལ་སྔ་མ་དང་མཚུངས་པས་ན་སྔ་མ་ལྟ་བུའོ་ཞེས་ལྟ་བུའི་སྒྲར་འགྱུར་བའམ། འདི་ལ་སྔ་མའི་ཆོས་ཡོད་པས་ན་དེ་དང་ལྡན་པའོ་ཞེས་ལྡན་པའི་སྒྲར་འགྱུར་གྲང་ན། དེ་ལས་ཅིར་འགྱུར། ཐམས་ཅད་སྲིད་ཕྱིར་ལྟ་བུར་མིན། །ཐམས་ཅད་ཅེས་བྱ་བ་ནི་རྗེས་སུ་དཔག་པས་འབྲེལ་པ་འཛིན་པ་ཉམས་སུ་མྱོང་བ་བཞིན་དུ་ཕྱིས་ཀྱང་རྟགས་ཀྱིས༌[^421]རྗེས་སུ་དཔག་པར་བྱ་བ་འཛིན་པར་བྱེད་དོ། །

[Block 531]
དེའི་གཅིག་སྔོན་དུ་སོང་བ་ལྟ་བུའོ་ཞེས་ནི༌[^422]བརྗོད་པར་མི་བྱའོ། །

[Block 532]
འབྲེལ་པ་གཞན་ལས་ཀྱང་འདི་སྔོན་མ་ལྟར་ན་ཞེས་འཛིན་ལ། དེས་མ་མཐོང་བའི་ཕྱིར་དང་། མ་མཐོང་བའི་རྗེས་སུ་དཔག་པ་ཉིད་ལ་ལྟ་བུའི་སྒྲ་སྦྱར་བར་མི་བྱའོ། །

[Block 533 [HEADING]]
#### སྔ་མ་དང་ལྡན་པ། ^2-3-2-0

[Block 534]
འཁྲུལ་བའི་ཕྱིར་ན་ལྡན་པ་མིན། །ལྡན་པར་བྱེད་པ་ནི་རིགས༌[^423]ན། །

[Block 535]
སྔར་འདི་རུ་ཡོད་དོ་ཞེས་འབྲས་བུ་སྔ་མ་དང་ལྡན་པར་བྱེད་ན་ནི་ཡུལ་དེ་ཤེས་པ་ཡང་སྔ་མ་དང༌[^424]ལྡན་པར་འགྱུར་ལ། རྒྱུ་ལ་འབྲས་བུ་ཤེས་པར་བྱེད་པ་དེ་ལྟར་ནི༌[^425]འཁྲུལ་པའི་ཕྱིར་ཚད་མ་མ་ཡིན་ནོ། །

[Block 536]
རྒྱུ་ཡོད་ན༌[^426]བདེན་དུ་ཆུག་ན་ཡང་གེགས་སྲིད་པའི་ཕྱིར་དང་། རྒྱུ་གཞན་མ་ཚོགས་པ་སྲིད་པའི་ཕྱིར་འབྲས་བུ་མི་འབྱུང་བ་སྲིད་པ་ཡིན་ནོ། །

[Block 537]
དེ་ལྟར༌[^427]ན་རེ་ཞིག་སྔ་མ་དང་ལྡན་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 538 [HEADING]]
#### ལྷག་མ་དང་ལྡན་པ། ^2-3-3-0

[Block 539]
ལྷག་ལྡན་ལ༌[^428]ཡང་ལྟ་བུར་རམ། །ལྷག་མ་ལྟ་བུར་ཞེས་ཡང་གལ་ཏེ་དེ༌[^429]ལྟ་བུར་བྱེད་ན་ནི་མངོན་སུམ་ཕྱི་མ༌[^430]དང་ཡུལ་མཚུངས་པའི་ཤེས་པ་དེ་ཡང་ལྷག་མ་ལྟ་བུ༌[^431]ཞེས་འགྱུར་ལ། དེ་ཡང་འཁྲུལ་པའི་ཕྱིར་ཚད་མ་མ་ཡིན་ཏེ། གཟུགས་མཚུངས་པ་ཙམ་གྱིས་རོ་མཚུངས་པར་འགྱུར་བའི་ངེས་པ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 540]
དེ་ལྟར་ན་ལྷག་མ་ལྟ་བུའོ་ཞེས་ལྟ་བུའི་སྒྲར་ཡང་སྦྱར་བར་མི་བྱའོ། །

[Block 541 [VERSE]]
འབྲེལ་གཞན་ལས་ཀྱང་རྟོགས་མི་འགྱུར། །
ལྷག་མ་དང་ལྡན་ལས་འགྱུར་མིན། །

[Block 542]
གང་རྒྱུ་ལྷག་མ་དང་ལྡན་པས་ལྷག་མ་དང་ལྡན་པ་ཡིན་ན་ནི་དེའི་ཤེས་པ་ཡང་ལྷག་མ་དང་ལྡན་པར་འགྱུར་ལ། དེ་ལྟར༌[^432]ཡང་འབྲས་བུ་མ་བཟུང་བ༌[^433]མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་བཟུང་ནས་རྒྱུ་རྗེས་སུ་དཔོག་པ་མེད་པར་འགྱུར་ན་དེ་ཡང་མཐོང་བ་ཡིན་ནོ། །

[Block 543]
དེ་བཞིན་དུ་བྱས་པ་ལ་སོགས་པ་ལས་མི་རྟག་པ་ལ་སོགས་པ་རྗེས་སུ་དཔོག་པར་ཡང་འགྱུར་རོ། །

[Block 544]
སྔར་ཇི་ལྟ་བར་བརྗོད་པའི་རྗེས་དཔག་རྣམས་ལ་ཡང་འབྲེལ་པ་རྟོགས་པར་མི་འགྱུར་ཞིང་། །འབྲེལ་གཞན་ལས་ཀྱང་རྟོགས་མི་འགྱུར། །ཞེས་བརྗོད་པར་བྱ་སྟེ། ཕྱི་མ་ལ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 545]
རྒྱུ་ཉིད་ལ་སོགས་པའི་འབྲེལ་པ་ཅན་གྱིས་འབྲས་བུ་ལ་སོགས་པའི་རྣམ་པ་ཅན་གྱི་ཤེས་པ་སྐྱེ་བ་རྗེས་སུ་དཔོག་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 546]
འབྲེལ་པ་ཅན་ཉིད་ཙམ་གྱི་སྒོ་ནས་རྟགས་དང་རྟགས་ཅན་གྱི་ཤེས་པ་སྐྱེ་བ་དང་། རྣམ་པ་ཐམས་ཅད་དུ་བདག་ཉིད་ཐམས་ཅད་ཀྱིས་རྒྱུ་དང་འབྲས་བུ་གཟུང་བའི་ཕྱིར་རོ། །

[Block 547]
དེ་ལྟར་ན་སྔ་མ་དང་ལྡན་པ་དང་ལྷག་མ་དང་ལྡན་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 548]
ཕྱིར་མཐོང་བ་ལའང་དེ་བཞིན་དུའོ། །

[Block 549]
དེ་ཡང་རྒྱུ་འབྲས་ཀྱི་འབྲེལ་པ་ཉིད་ལས་ཡུལ་ལ་ཤིན་ཏུ་ལྐོག་ཏུ་གྱུར་པ་ལས་འཇལ་བར་བརྗོད་པས་ནའོ། །

[Block 550]
རྗེས་དཔག་གི་ཤེས་པ་ཐམས་ཅད་ཀྱི་ཚད་མའི་གཞལ་བྱ་ལ། [^434]འབྲས་བུ་གཞན་མ་ཉིད་མི་ཐོབ།[^435] །འབྲས་བུ་མེད་པར་ཚད་མར་འགྲོ་བ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། བྱེད་པ་པོ་དང་ལས་ཀྱི་བྱ་བ་དང་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 551]
རྟགས་ཤེས༌[^436]ཚད་མ་ཡིན་ཞེ་ན། འདི་སྙམ་དུ་རྟགས་ཀྱི༌[^437]ཤེས་པ་ཚད་མ་ལ་རྗེས་དཔག་གི་ཤེས་པ་ཚད་མའི་འབྲས་བུའོ་ཞེ་ན། དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 552]
དེ་ཡང་ཡུལ་ཐ་དད་ལས་ནི་མ་ཡིན་ཏེ། འདིར་ཡུལ་གཞན་ལ་ཚད་མར་འགྱུར་ཞིང་གཞན་ལ་འབྲས་བུར་འགྱུར་བ་ནི༌[^438]ཡོད་པ་མ་ཡིན་ནོ་ཞེས་སྔར་བརྗོད་ཟིན་ཏོ། །

[Block 553]
རྟགས་ཀྱི་ཤེས་པ་ཚད་མ༌[^439]ཡིན་པའི་ལྟ་ན་ནི། རྣམ་པར་དབྱེ་བའང་འགྲུབ་མི་འགྱུར། །གང་རྗེས་སུ་དཔག་པ་ནི་སྔ་མ་ལྡན་པ་དང་ལྷག་མ་དང༌[^440]ལྡན་པའོ་ཞེས་རྟགས་ཅན་གྱི་དབྱེ་བས༌[^441]དེ་དག་འགྲུབ་པར་མི་འགྱུར་ཏེ། རྟགས་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 554]
གང་ཡང་སྔ་མ་དང་ལྡན་པའི་རྗེས་སུ་དཔག་པ་ཁོ་ན་རྣམ་པ་གསུམ་དུ་འགྱུར་ཏེ། དུས་གསུམ་ལ་འཛིན་པའི་ཕྱིར་རོ་ཞེས་པའི་ངེས་པར་བཟུང་བ་དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ།[^442] །

[Block 555]
རྗེས་དཔག་ཐམས་ཅད་དུས་གསུམ་གྱི་ཡུལ་ལ་འཇུག་སྟེ། དུས་གསུམ་པ་ཅན་ནོ་ཞེས་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 556]
དེ་ལྟ་བུའོ་ཞེས་པའི་ཕྱོགས་ལ་ནི་འབྲེལ་པ་བསྟན་པ་མེད་པའི་ཕྱིར་རྣམ་པ་གསུམ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 557]
དེ་ལ་དེ་ལྟ་བུའི་རྗེས་དཔག་ཀྱང་བཀག་པ་ཡིན་ནོ། །

[Block 558 [HEADING]]
### བྱེ་བྲག་པ། ^2-4-0

[Block 559]
བྱེ་བྲག་པ་རྣམས་ན་རེ་འདི་ནི་འདིའི་འབྲས་བུ་དང་རྒྱུ་དང་འབྲེལ་པ་དང་དོན་གཅིག་ལ་འདུ་བ༌[^443]དང་འགལ་བ་ཅན་ནོ་ཞེས་བྱ་བ་དེ་དག་ནི་རྟགས་ལས་བྱུང་བའོ་ཞེས་ཟེར་རོ། །

[Block 560]
དེ་ལ་རེ་ཞིག་སྔར། རྒྱུ་ལས་འབྲས་བུ་གྲུབ་པ་མེད། །རིགས་པ༌[^444]ཅན་གྱི་རྗེས་དཔག་དགག་པའི་སྐབས་སུ་སྔ་མ་དང་ལྡན་པ་དང་ཕྱི་མ་དང་ལྡན་པའོ་ཞེས་བྱ་བ་འདི་ལ་རྒྱུས་འབྲས་བུ་རྗེས་སུ་དཔོག་པའི་གཏན་ཚིགས་མེད་དོ་ཞེས་བརྗོད་དོ། །

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
--- END BLOCKS ---
