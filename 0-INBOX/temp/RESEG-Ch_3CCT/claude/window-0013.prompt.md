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
[Block 456 [VERSE]]
འདིའི་རྫས་ཀྱང་གང་ཡིན་ཞེ་ན། །
རྒྱུ་ལ་བྱང་ཆུབ་སེམས་ཡིན་ཏེ། །
རྟེན་མེད་རྫས་རྣམས་ཀུན་དང་བྲལ། །

[Block 457]
ཞེས་པ་ནི་གོ་སླའོ། །

[Block 458 [VERSE]]
གང་གིས་གང་ལ་མི་གཡོ་བར། །
དེ་ཉིད་ལ་དམིགས་དགོས་པ་ཡིན། །

[Block 459]
ཞེས་པ་ནི་གང་གིས་རྟོག་པ་ཐམས་ཅད་སྤངས་ཏེ། མི་རྟོག་པའི་ཤེས་པ་འདི་ལ་ཡང་དང་ཡང་དུ་སེམས་གཏོད་པ་ནི་འདིའི་དགོས་པའོ། །གང་གིས་གང་ལ་གནས་པ་འདིའི་རྟགས་ཀྱང་གང་ཞིག་ཡིན་ཞེ་ན། ནམ་མཁའ་བཞིན་དང་མྱུར་བ་དང་། དལ་དང་མི་གཡོ་ལ་སོགས་རྟགས། ཞེས་པ་ལས་དང་པོ་པ་ལ་བརྟེན་པ༌[^215]གཞན་འགགས་ཏེ་སྟེང་གི་ནམ་མཁའ་བཞིན་དུ་འགྱུར་རོ། །

[Block 460]
ཁ་ཅིག་ལ་ནི་སྨིག་རྒྱུ་བཞིན། །ཞེས་པ་མྱུར་ལ་རྟོག་པ་མེད་པ་འབྱུང་ངོ་། །ཁ་ཅིག་ལ་ནི་དལ་བ་དང་མི་གཡོ་བ་ལ་རྟོག་པ་མེད་པར་འབྱུང་བ་འདི་ནི་རྟགས་སོ། །

[Block 461]
སློབ་པ་སྨིག་རྒྱུ༌[^216]ལ་སོགས༌[^217]དང་། འདར་དང་རྡུལ་དང་འཕྱར་བ་དང་།

[Block 462 [VERSE]]
རྟག་ཏུ་བདེ་བ་ཁ་བ་འདྲ། །
འདི་ལ་སོགས་པའི་རྟགས་རྣམས་འབྱུང་། །

[Block 463]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 464 [VERSE]]
མཛུབ་མོས་ཟླ་བསྟན༌[^218]ཇི་བཞིན་དུ། །
རྒྱལ་བའི་བཀའ་ནི་དོན་གྱི་བརྡ། །

[Block 465]
ཞེས་པ་མིང་དང་ཚིག་དང༌[^219]ཡི་གེའི་རྣམ་པ་འདི་ནི་བརྡ་ཙམ་གྱི་སྒོ་ནས་དོན་སྟོན་པར་བྱེད་པ་ཡིན་ཏེ། དཔེར་ན་མཛུབ་མོས་ཟླ་བ་བསྟན་པ་བཞིན་ནོ། །

[Block 466]
འདི་ལ་ནུས་པའང་ཇི་ཞིག་ཡོད་ཅེས་དྲིས་པ་དང་།

[Block 467 [VERSE]]
རབ་ཏུ་དགའ་ནས་ཆོས་ཀྱི་སྤྲིན། །
རྗེས་ཐོབ་སྔོན་བཞིན་ཡེ་ཤེས་སྐྱེ། །

[Block 468]
ཞེས་པ་ནི་སློབ་པའི་དབང་དུ་ཟུང་དུ་འཇུག་པའི་ཚུལ་གྱིས་ཡེ་ཤེས་བརྟན་པ་དང་ཡུན་རིང་པར་བྱེད་ལ། དེའི་རྗེས་ལ་སྐྱེ་བའི་རྟོག་པ་ཡང་དང་ཡང་དུ་ཟིལ་གྱིས་གནོན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 469 [VERSE]]
གོང་ནས་གོང་དུ་ཕྱིན་ནས་ནི། །
འོག་མའི་ས་ལ་གནས་མི་འགྱུར། །
རང་གི་ས་ཡི༌[^220]རྟོག་པ་སྤོང་། །
གོང་མའི་ས་ལ་མངོན་དུ་ཕྱོགས། །

[Block 470]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 471 [VERSE]]
གང་ཞིག་སྤྲོས་པ་ཀུན་བྲལ་བའི། །
མན་ངག་བླང་དང་སྦྱིན་པར་ནུས། །

[Block 472]
ཞེས་པ་ནི་གོ་སླའོ། །

[Block 473 [VERSE]]
འདི་ལ་གནས་པའི་རྣལ་འབྱོར་པས། །
བླ་མེད་ཚོགས་ཀྱི་འཁོར་ལོ་ལྡན། །
གང་དུ་བླ་མེད་རྣལ་འབྱོར་ནི། །
རྣལ་འབྱོར་མཆོག་ཏུ་འགྱུར་བ་ཡིན། །

[Block 474 [VERSE]]
དངོས་སུ་མཆོག་གི་དངོས་གྲུབ་བདག །
བདེ་གཤེགས་རབ་འབྱམས་དཔག་མེད་ཀྱི། །
བཀའ་ལ་དབང་བསྐུར༌[^221]དམ་པ་ཡིན། །

[Block 475]
ཞེས་པ་འདི་ནི་ཚོགས་གང་དང་། འབྲེལ་པ་དང་རྣལ་འབྱོར་གང་དང་འབྲེལ་པ་དང་། རྒྱུད་གང་དང་འབྲེལ་པ་དང་། དེ་དག་གི་གོ་རིམས་ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་ཏོ། །

[Block 476 [VERSE]]
ཕྱི་དང་ནང་དང་གསང་བ་དང་། །
མཐར་ཐུག་བཤད་པ་རྣམ་པ་བཞི། །
དབང་བཞི་རྫོགས་པའི་གང་ཟག་ལ། །
ཚུལ་བཞིན་སོ་སོར་སྦྱིན་པར་བྱ། །

[Block 477 [VERSE]]
ལས་བཞིའི་ཐབ་ཁུང་སྲེག་པ་དང་། །
སྙིང་ནང་ལྷ་ལ་དབུལ་བ་དང་། །
བུད་མེད་བྷ་གར་བསྟེན་པ་དང་། །
ལྟེ་བའི་འཁོར་ལོ་སྦྱོར་བྱེད་པ། །

[Block 478 [VERSE]]
སྦྱིན་སྲེག་རྣམ་པ་བཞི་པོའང་། །
ཚུལ་བཞིན་རིམ་པ་བཞི་དང་སྦྱར། །
བཟོད་པ་འབྲིང་དང་ཆོས་མཆོག་བར། །
དང་པོ་དང་ནི་བཅུ་པའི་བར། །

[Block 479 [VERSE]]
ས་ཡི་ཁྱད་ནི༌[^222]བགྲོད་པ་སྟེ། །
ལུས་དང་ངག་ཡིད་རྟོག་པ་སྤོང་། །
ཐོབ་པ་འབྲས་བུ་མངོན་བྱེད་པ། །
དབང་བཞི་ལ་ནི་གོ་རིམས་བཞིན། །

[Block 480]
ཞེས་པ་འདི་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ།། །།

[Block 481 [HEADING]]
## གྲོལ་བར་བྱེད་པའི་ལམ། ^2-0

[Block 482]
དེ་ལྟར་སྨིན་པར་བྱེད་པ་རྒྱས་པར་བཤད་ནས། ད་ནི་གྲོལ་བར་བྱེད་པའི་ལམ་བཤད་པར་བྱ་སྟེ། གྲོལ་བར་བྱེད་པའི་ལམ་ཡང་གང་ཡིན་དུ་ཞིག་ཅེ་ན།

[Block 483 [VERSE]]
གྲོལ་བའི་ལམ་ནི་རྣམ་པ་གཉིས། །
བསྐྱེད་པ་དང་ནི་རྫོགས་པའོ། །

[Block 484]
ཞེས་པ་གང་ཞིག་གང་ལས་གྲོལ་བར་འདོད་པ་དེའི་ལམ་ནི་བསྐྱེད་པའི་རིམ་པ་དང་། རྫོགས་པའི་རིམ་པའོ། །

[Block 485]
དེ་གཉིས་ཀྱིས་ཅི་བྱེད་ཅེ་ན། འདི་ལྟར་རགས་པ་དང་ཕྲ་བའི་རྣམ་པར་རྟོག་པ་ལྡོག་པར་བྱེད་དོ། །

[Block 486]
བསྐྱེད་པའང་དུ་ཞིག་ཅིའི་ཕྱིར་ཞེ་ན།

[Block 487 [VERSE]]
གང་ཞིག་བསྐྱེད་པའི་སྦྱོར་བ་ལ། །
ངོ་བོ་དང་ནི་རྣམ་དབྱེ་དང་། །
ངེས་པའི་ཚིག་དང་རྣམ་གྲངས་དང་། །
ཆོས་རྣམ་གྲངས༌[^223]དང་ལྡན་པ་དང་། །

[Block 488 [VERSE]]
གཞན་སེལ་གླེང་གཞི་དམིགས་པ་དང་། །
རྒྱུ་དང་དུས་དང་འབྲས་བུ་དང་། །
སྔོན་འགྲོ་རྟེན་གྱི་གང་ཟག་དང་། །
གནས་དང་གྲོགས་དང་སེམས་གཟུང་དང་། །

[Block 489 [VERSE]]
གོམས་པའི་ཚད་དང་མཐར་ཕྱིན་ཚད། །
དངོས་གྲུབ་གང་དང་འབྲེལ་པ་དང་། །
རྟོག་པ་སྤོང་ཞིང་ས་བོན་གསོ། །
འདི་ནི་བསྐྱེད་པའི་རིམ་པའོ། །

[Block 490]
ཞེས་བྱ་བ་ལ་སོགས་པ་མདོར་བསྟན་ནས་ད་ནི་རང་རང་གི་ཡན་ལག་བཤད་པ། ངོ་བོ་ཞེས་བྱ་བ་འདི་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 491 [VERSE]]
བསྐྱེད་པའི་རིམ་པའི་ངོ་བོ་ནི། །
རགས་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན། །

[Block 492]
ཞེས་པ་རགས་པའི་སྐུ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་གང་ཡིན་པ༌[^224]དེ་བསྐྱེད་པའི་རིམ་པའི་ངོ་བོའོ། །

[Block 493]
གཞན་དུ་ནི༌[^225]ངོ་བོ་ཉིད་ཡིན་པ་དང་མ་ཡིན་པ་དང་ཐེ་ཚོམ་ཟ་བ་ལ་སོགས་པའི་ཉེས་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 494]
འདི་ལ་དབྱེ་བ་ནི་དུ་ཞིག་ཅེ་ན།

[Block 495 [VERSE]]
བསྐྱེད་པ་རྣམ་པ་གཉིས་ཡིན་ཏེ། །
སྦྱང་བྱ་དང་ནི་སྦྱོང་བྱེད་དོ། །
--- END BLOCKS ---
