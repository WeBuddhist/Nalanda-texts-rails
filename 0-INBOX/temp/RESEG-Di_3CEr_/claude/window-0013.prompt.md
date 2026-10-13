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
[Block 456]
རང་གི་ཆོས་ཀྱི་འབྲེལ་པར་ནི། །བརྗོད་པར་མི་བྱའོ། །

[Block 457]
གཞན་མ་བརྗོད་པ་ནི་དེ་ལྟར་རྗེས་སུ་དཔག་པར་བྱ་བ་མ་ཡིན་ཏེ། འོན་ཀྱང་། དོན་སྨོས་ཕྱིར། མེ་འདི་ལ་ཞེས་སྨྲས་པའི་དོན་དང་འབྲེལ་པར་བརྗོད་པར་འགྱུར་བའི་ཡིན་ནོ་ཞེ་ན། སྔར་བརྗོད་པའི་འཐད་པས་དེ་ནི་དུད་པས་རྗེས་སུ་དཔག་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར། །གཏན་ཚིགས་འདི་དང་འབྲེལ་པ་མིན། །གང་གི་ཕྱིར་དུད་པ་ལས་མ་གཏོགས་པ༌[^374]མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་ཉིད་ནི་བསྟན་པར་བྱ་བ་མ་ཡིན་ཏེ། འདི་ལྟར་མེ་ཉིད་ལའོ། །

[Block 458]
ཉེས་པ་དེ་དག་ནི་མེད་དེ། གང་གི་ཕྱིར་མེ་དུད་པ་དང་ལྡན་པའི་ས་ཕྱོགས་དང་མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་བསྟན་པར་བྱ་བ་མ་ཡིན་ཡང་དེ་རྗེས་སུ་དཔག་བྱར་བྱེད་པ་དེ་བཞིན་དུ་འབྲེལ་བ་ལ་ཡང་འགྱུར་རོ་ཞེ་ན། རྣམ་གཞག་དེ་ནི་སྤང་བ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 459 [VERSE]]
རྟགས་ཀྱི་འཁྲུལ་བ་མེད་པ་ནི། །
ཆོས་ལས་གཞན་དུ་སྟོན་པར་བྱེད། །
དེར་གྲུབ་དེ་དང་ལྡན་པ་ཡི། །
ཆོས་ཅན་གོ་བར་བྱ་བ་ཡིན། །

[Block 460]
གང་མེ་དང་དུད་པ་མེད་ན་མི་འབྱུང་བའི་འབྲེལ་པ་དེ་གཞན་དུ་བསྟན་པར་བྱས་ནས་ཡུལ་གཞན་དུ་དུད་པ་དེ་འབའ་ཞིག་ཙམ་མཐོང་ཡང་གང་ན་དུད་པ་ཡོད་པ་དེ་ན་མེ་ཡོད་དོ།[^375] །

[Block 461]
མེ་དང་ལྡན་པར་གྲུབ་པ་སྟོན་པར་བྱེད་དོ། །

[Block 462]
དེ་ལྟ་མ་ཡིན་ན་ས་ཕྱོགས་གཞན་དུ་བསྒྲུབ་བྱ་དང་དུད་པ་མེད་ན་མི་འབྱུང་བ་བྱེ་བྲག་ཏུ་བསྟན་པར་མི་ནུས་སོ། །

[Block 463]
གཞི་ཐུན་མོང་བ་ཉིད་དུ་བསྟན་པ་སྟེ་གང་ན་དུད་པ་ཡོད་པ་དེ་ན་མེ་ཡོད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 464]
དེའི་ཕྱིར་གཏན་ཚིགས་ཆོས་ལས་གཞན་དུ་མི་འཁྲུལ་པར་བསྟན་པ་དེ་ལྟར་འཐད་པ་ཡིན་གྱི། ཆོས་ཙམ་ཡང་བསྒྲུབ་པར་བྱ་བ་མ་ཡིན་ལ་འབྲེལ་པ་ཡང་མ་ཡིན་ནོ། །

[Block 465 [HEADING]]
#### ཆོས་ལ་དཔྱད་པ་གཞན། ^2-1-8-0

[Block 466 [VERSE]]
རྟགས་ཀྱི་རྗེས་སུ་བསྟན་བྱ་བའི། །
ཆོས་ལ་དཔྱད་པ་གཞན་ཡང༌[^376]འཇུག །

[Block 467]
རྟགས་དང་ཆོས་དང་ཆོས་ལ་མི་འཁྲུལ་པ་ཡོད་པ་ཡིན་པ་བསྟན་པར་བྱ་སྟེ། དེ་དང་ལྡན་པའི་ཆོས་ཅན་དུ་གྲུབ་པ་དེའི།

[Block 468 [VERSE]]
ཆོས་དོན་དུ་མ་གཏན་ཚིགས་ཀྱིས། །
རྣམ་པ་ཐམས་ཅད་དུ་རྟོགས༌[^377]མིན། །
གང་དང་འབྲེལ་པ་ཡོངས་བཅད་ནས། །
ཆོས་གཞན་དང་བྲལ་ཐོབ་པར་བྱེད། །

[Block 469]
དཔེར་ན་མེ་ལ་འབར་བ་དང་རྣོ་བ་ལ་སོགས་པ་དུ་མ་ཡོད་ཀྱང་དུད་པས་བྱེ་བྲག་དེ་གོ་བར་མི་བྱེད་དེ་འཁྲུལ་པའི་ཕྱིར་རོ། །

[Block 470]
གང་དང༌[^378]རྗེས་སུ་འབྲེལ་པ་དེ་ལས་གཞན་པ་ནི་མེ་མ་ཡིན་ཏེ། རྫས་ཉིད་དང་ཡོན་ཏན་ཉིད་ལ་སོགས་པ་དེ་དག་གིས༌[^379]རྫས་མ་ཡིན་པ་ལ་སོགས་པ་ལས་ལོག་པ་ཙམ་འབའ་ཞིག་ཐོབ་པར་བྱེད་པ་སྟེ། དཔེར་ན་མེས་མེ་ཡིན་པ་ལས་ལོག་པའི་རང་དང་འབྲེལ་པ་ཙམ་ཐོབ་པར་བྱེད་པ་དེ་བཞིན་དུ་འདི་ཡང་མེ་མ་ཡིན་པ་ཐམས་ཅད་ལ་མ་མཐོང་བ་ཉིད་གཞན་ལ་ནི་མཐོང་བ་ཡིན་ནོ། །

[Block 471 [VERSE]]
ཡོན་ཏན་དྲི་དང་དྲི་བསུང་སོགས།[^380] །
དེ་ཡི་བྱེ་བྲག་གི་རིམ་པས། །
རྫས་མིན་ལ་སོགས་རྣམ་བཅད་ནས། །
ཨུཏྤ་ལ་སོགས་རེ་རེ་རྟོགས། །

[Block 472]
དེ་ལ་ཡོན་ཏན་ཉིད་ཀྱིས་རྫས་མ་ཡིན་པ་ལས་ལོག་པ་དང་། དྲི་ཉིད་ཀྱིས་སའི་རྫས་མ་ཡིན་པ་ལས་ལོག་པ་དང་། དྲི་བསུང་བ་ཉིད་ཀྱིས་དྲི་ང་བའི་སྤྱི་ལས་ལོག་པ་དང་། དྲི་བསུང་བའི་བྱེ་བྲག་གིས་ཨུཏྤ་ལ་མ་ཡིན་པ་ལ་སོགས་པ་ལས་ལོག་པ་རེ་རེ་རྟོགས་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 473]
དེ་ལྟ་མ་ཡིན་ན་ནི།

[Block 474 [VERSE]]
གལ་ཏེ་མཐོང་བ་བཞིན་གཏན་ཚིགས། །
སྒྲུབ་པའི་སྒོ་ནས་འཇུག་པ༌[^381]ནི། །
ཐམས་ཅད་རྟོགས་པར་མི་འགྱུར་བའམ།[^382] །
ཡང་ན་ཐམས་ཅད་རྟོགས་པར་འགྱུར། །

[Block 475]
གལ་ཏེ་ཡང་དཔེར་ན་མེ་ལ་དུད་པ་མཐོང་བ་བཞིན་དུ་ཕྱིས་ཀྱི་ཚེ་ཡང་འཇུག་པར་བྱེད་ན་ནི་ནམ་ཡང་རྟོགས་པར་མི་འགྱུར་ཏེ། དཔེར་ན་མེ་མཐའ་དག་ལ་མ་མཐོང་བ་བཞིན་དུ་མེ་འདི་ཡང་མི་རྟོགས་པར་འགྱུར་རོ། །

[Block 476]
གལ་ཏེ་ཇི་ལྟར་མཐོང་བ་བཞིན་དུ་རྟོགས་པར་བྱེད་ན་ནི་གསལ་བ་དང་རྣོ་བ་ལ་སོགས་པའི་བྱེ་བྲག་རྣམས་ཀྱང་རྟོགས་པར་འགྱུར་རོ། །

[Block 477]
གལ་ཏེ་མེ་མ་ཡིན་པ་རྣམ་པར་བཀག་སྟེ་སྤྱིའི་ཚུལ་གྱིས་འཇུག་པར་བྱེད་ན་ནི་དེའི་ཕྱིར་སྒྲུབ་པའི་སྒོ་ནས་འཇུག་པ་ལ་ཡང་ཚུལ་དེ་ཉིད་བལྟའོ་ཞེས་ཤེས་པར་བྱའོ། །

[Block 478]
བྱེ་བྲག་གི་ཚུལ་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 479 [VERSE]]
གལ་ཏེ་སྤྱི་ལས་ཡིན་གྲང་ན། །
དེ་ནི་དེ་ལས་གཞན་དུ་འགྱུར། །
རྟེན་རྣམས་མ་མཐོང་བ་ཡི་ཕྱིར། །
ཐ་དད་མིན་གཅིག་མཐོང་མི་འགྱུར། །

[Block 480]
རེ་ཞིག་མེ་ལས་གཞན་པའི་མེ་ཉིད་ཅེས་པའི་སྤྱི་ནི༌[^383]ཡོད་པ་མ་ཡིན་ནོ། །

[Block 481]
ཡོད་དུ་ཆུག་ན་ཡང་དེ་མཐོང་བ་ནི་མི་སྲིད་དོ། །

[Block 482]
རྟེན་མཐའ་དག་མ་མཐོང་བའི་ཕྱིར་དུ་མ་རྣམས་ལས་གཉིས་ཉིད་ལ་སོགས་པའི་ཐུན་མོང་བ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 483]
གང་དག་སྤྱི་མཐོང་ཞིང་གཟུང་བ་པོ་ཡང་རྟེན་མ་བཟུང་བ་པོ་དང་མཚུངས་ཤིང་འདྲ་བར་འགྱུར་རོ། །

[Block 484]
གལ་ཏེ་རྟེན་གཅིག་བཟུང་བས་ཀྱང་ཐམས་ཅད་གཟུང་བ་ཡིན་ན་ནི། དེ་ཡང་རྟེན་བཞིན་དུ་དུ་མར་འགྱུར་རོ། །

[Block 485]
འདི་ལྟར་ཡང་རྗེས་སུ་དཔག་པར་བྱ་བ་ནི་ཆ་ཤས་ཅུང་ཟད་ཙམ་ལས་རྟོགས་པར་བྱ་སྟེ། ཆ་ཤས་འདི་ལྟ་བུའི་ཚུལ་ནས།

[Block 486 [VERSE]]
རྟགས་ཅན་ལ་ནི་མི་འགྱུར་ཞིང་། །
དེ་ཉིད་ཀྱི་ཆོས་དུ་མ་ནའང་། །
ཅིག་ཤོས་ཐོབ་པར་བྱེད་པ་ཡིན། །

[Block 487]
དུད་པ་ནི་ཆ་ཤས་འབའ་ཞིག་མེ་ལས༌[^384]མི་འཁྲུལ་བ་ཡིན་ནོ།[^385] །

[Block 488]
དུད་པ་ཉིད་དང་སྐྱ་བོ༌[^386]ཉིད་ལ་སོགས་པ་ནི། དེ་ཉིད་ཐོབ་པར་བྱེད་པ་ཡིན་གྱིས༌[^387]རྫས༌[^388]ཉིད་ལ་སོགས་པས་ནི་མ་ཡིན་ཏེ། འཁྲུལ་པའི་ཕྱིར་རོ། །

[Block 489]
ཡང་བརྗོད་པ་རྟགས་ཅན་གང་རྗེས་འབྲེལ་པ་ཡི། །

[Block 490 [VERSE]]
རྟགས་ཅན་དེ་འདིར་རྟོགས་བྱ་ཡིན། །
བྱེ་བྲག་རྟོགས་བྱ་མ་ཡིན་ཏེ། །
དེ་དག་ཉིད་ལས༌[^389]འཁྲུལ་ཕྱིར་རོ། །
རྟགས་ཅན་རྗེས་སུ་འབྲེལ་པའི༌[^390]དོན། །

[Block 491 [VERSE]]
རྟོགས་བྱ་རྟགས་ཅན་གྱི་བྱེ་བྲག །
མ་ཡིན་དེ་ལ་རྟོགས་པ་པོའི། །
རྟོགས་པ་རབ་ཏུ་འཁྲུལ་པའི་ཕྱིར། །

[Block 492]
ཞེས་བྱ་བ་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པ་དག་གོ། །

[Block 493 [HEADING]]
#### རྟགས་དང་རྟགས་ཅན་འབྲེལ་པ། ^2-1-9-0

[Block 494]
ཅི་སྟེ་འབྲེལ་པ་ནི་ཡང་དག་པར་འཕྲོད་པ་བཞིན་དུ་གཉིས་ཀ་དང་འབྲེལ་པ་ཡིན་པའི་ཕྱིར་རྟགས་ཅན་གྱི་ཆོས་རྟགས་ལ་ཡང་འགྱུར་རོ་ཞེ་ན།

[Block 495 [VERSE]]
དེ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། །
འབྲེལ་པ་གཉིས་ལ༌[^391]གནས་མོད་ཀྱང་། །
རྟགས་དང་རྟགས་ཅན་སྟོབས༌[^392]གཅིག་པ། །
རྟེན་དང་བརྟེན་པ་བཞིན་ཡིན་གྱི། །
--- END BLOCKS ---
