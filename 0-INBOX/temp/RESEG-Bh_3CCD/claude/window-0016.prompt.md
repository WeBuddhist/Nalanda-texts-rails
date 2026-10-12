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
[Block 561 [HEADING]]
##### སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད། ^1-2-1-2-0

[Block 562]
དེ་དག་ཐམས་ཅད་ཀྱི་རྩ་བ་ནི་བཅོམ་ལྡན་འདས་མ་ཕྱི་མོའི་ཡི་གེ་བཞི་བཅུ་རྩ་དགུ་པའོ། །

[Block 563]
དེ་ཡི་ཡང་རྩ་བ་ནི་ལྟེ་བའི་འོག་འོད་གསལ་བའི་གནས་ལས་བྱུང་བ་སྲོག་ཅེས་བྱ་བའི་རླུང་ངོ་། །ཇི་སྐད་དུ།

[Block 564 [VERSE]]
ནམ་མཁའི་རླུང་ནི་ལུས་ལ་འབྱུང་བ་སྟེ། །
ཡང་དག་བརྗོད་པས་དབྱངས་ནི་ཁར་ཕྱིན་པ། །
གནས་གཞན་དག་ཏུ་རབ་ཏུ་ཕྱེ་བས་ན། །

[Block 565]
ཡི་གེ་ཉིད་དུ་གྱུར་པ་གང་ཡིན་དེ་སྒྲ་ཡིན། །

[Block 566 [VERSE]]
དེ་ནི་ཚངས་པའི་ཡི་གེ་དག་བྱེད་མཆོག །
ཕུགས་ན་གནས་པར་ཡང་དག་བྲམ་ཟེས་འདོད། །
དེ་ནི་ཡང་དག་རབ་ཏུ་སྦྱོར་གྱུར་ན། །
ངེས་ལེགས་མངོན་པར་མཐོ་བས་སྐྱེས་བུར་སྦྱོར། །

[Block 567]
ཞེས་སོ། །

[Block 568]
དེ་བས་ན་སྲོག་དེ་ཉིད་སྙིང་ལ་སོགས་པའི་གནས་བརྒྱད་ལ་རིག་པས༌[^387]དབྱངས་དང་གསལ་བྱའི་སྡེ་ཚན་རྣམས་སྐྱེད་པར་བྱེད་དོ། །

[Block 569]
ཇི་སྐད་དུ། ཡི་གེ་རྣམས་ཀྱི་གནས་བརྒྱད་དེ།

[Block 570 [VERSE]]
བྲང་དང་མགྲིན་པ་མགོ་དེ་བཞིན། །
ལྕེ་ཡི་རྩ་བ་སོ་དང་ནི། །
སྣ་དང་མཆུ་དང་རྐན་དག་གོ། །

[Block 571]
ཞེས་འབྱུང་ངོ་། །

[Block 572]
གནས་བརྒྱད་པོ་དེ་དག་ལས་སྡེ་ཚན་བརྒྱད་སྐྱེ་བར་འགྱུར་ཏེ་དབྱངས་ཀྱི་སྡེ་ཀ་ལ༌[^388]སོགས་པ་མའི་བར་དུ་སྡེ་ཚན་ལྔ་དང་བར་ན་གནས་པ་དང་དྲོད་ཀྱི་ཡི་གེའི༌[^389]སྡེ་ཚན་གཉིས་ཏེ། རྣམ་པར་ཤེས་པ་ཚོགས་བརྒྱད་རྣམ་པར་དག་པའི་ངོ་བོ་ཡིན་ཞེས་བར་དུའོ། །

[Block 573]
དེ་ལས་ཀྱང་ཚིགས༌[^390]རྣམས་ནི་བ་ལང་དང་རྟ་ལ་སོགས་པའི་སྒྲ་འབྱུང་ངོ་། །དེ་རྣམས་ལས་ཀྱང་ངག་སྐྱེ་བ་ཡིན་ཏེ། དཔེར་ན་ཀྱེ་ལྷས་བྱིན་བ་དཀར་མོ་དབྱུག་པས་རྡུངས༌[^391]ཤིག །ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 574]
དེ་རྣམས་ཀྱང་ངག་ཆེན་པོར་འགྱུར་ཏེ། དཔེར་ན་འདི་སྐད་བདག་གིས་ཐོས་པའི་དུས་གཅིག་ན་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 575]
ངག་ཆེན་པོ་ལས་ཀྱང་བསྟན་བཅོས་རྩོམ་པ་དང་། གར་གྱི་བསྟན་བཅོས་དང་། རབ་ཏུ་བྱེད་པ་དང་། རླུང་དང་ལུང་བསྟན་པ་དང་། རྟོག་གེ་དང་། གྲངས་ཅན་པ་དང་། མཆོད༌[^392]འོས་དང་། ཕྱུགས་ཀྱི་བདག་པོ་པ་དང་། རིགས་པ་པ་དང་། ཁྱད་པར་པ་དང་། དཔྱོད་པ་པ་དང་། བདེ་བར་གཤེགས་པ་ལ་སོགས་པའི་བསྟན་བཅོས་དང་། འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་བྱེ་བྲག་གིས༌[^393]རྣམ་པ་དྲུག་ཏུ་བྱུང་བ་དེ་དག་ཐམས་ཅད་ཀྱི་རྒྱུར་གྱུར་པ་ནི་ཕྱི་མོའི་ཡི་གེ་ཁོ་ནའོ། །

[Block 576 [HEADING]]
###### སྔགས་ཀྱི་བཏུ་བ། ^1-2-1-2-1-0

[Block 577]
དེ་ལ་སྔགས་ཐམས་ཅད་བཏུ་བས་ན་སྔགས་ཀྱི་བཏུ་བ་སྟེ་ཕྱི་མོའོ། །

[Block 578]
དེ་ནི་སྤྲོ་བའི་རིམ་པས་སྔགས་བཏུ་བའོ། །

[Block 579]
བསྡུ་བའི་རིམ་པས་ཀྱང་འདི་ལྟ་སྟེ། ཨ་ལ་སོགས་པ་ནས་ཧའི་བར་དུ་སྡེ་ཚན་བརྒྱད་པ་དང་པོའི་ཡི་གེ་རྣམས་ཀྱིས་བསྡུས་པ་ཡིན་ཏེ། ཨ་ཀ་ཙ་ཊ་ཏ་པ་ཡ་ཤའོ། །

[Block 580]
དེ་དག་ཀྱང་འབྱུང་བའི་ཡི་གེ་བཞི་ལ་བསྡུས་པས་ཨ་ཀ་ཡ༌[^394]ཤའོ། །

[Block 581]
དེ་དག་ཀྱང་གསུམ་དུ་བསྡུས་པ་ལས་ཨ་ཀ་ཡའོ། །

[Block 582]
དེ་རྣམས་ཀྱང་ཡི་གེ་གསུམ་དུ་འགྱུར་ཏེ། དེ་ལ་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡི་གེ་ཨ། འདོད་ཆགས་ཀྱི་ས་བོན་ཡི་གེ་ཨ་ཡའོ།[^395] །

[Block 583]
ཐབས་ཀྱི་ངོ་བོ་ཉིད་ཀྱི་ཡི་གེ་ཀ་ཡོངས་སུ་གྱུར་པའི་ཐུགས་ཀྱི་རྡོ་རྗེའི་ས་བོན་ཡི་གེ་ཧཱུཾ་ངོ་། །གཉིས་ཀ་སྙོམས་པར་ཞུགས་པའི་མཚན་ཉིད་ཡི་གེ་ཡ་ཡོངས་སུ་གྱུར་པ་གཏི་མུག་རྡོ་རྗེའི་ས་བོན་ཡི་གེ་ཨཱའོ། །

[Block 584]
དེ་རྣམས་ཁམས་གསུམ་དང་། སྲིད་པ་གསུམ་དང་། སྐུ་གསུམ་དང་། ཡེ་ཤེས་གསུམ་དང་། རྩ་གསུམ་དང་། རྫས་གསུམ་དང་། སེམས་དཔའ་གསུམ་དང་། དེ་བཞིན་གཤེགས་པ་གསུམ་དང་། ལྷ་མོ་གསུམ་དང་། དཀྱིལ་འཁོར་གསུམ༌[^396]གྱི་ངོ་བོ་ཉིད་བུད་མེད་དང་སྐྱེས་པ་དང་མ་ནིང་དང་། ཐབས་དང་ཤེས་རབ་དང་གཉིས་ཀ་སྙོམས་པར་ཞུགས་པ་དང་། ཟླ་བ་དང་། ཉི་མ་དང་། མེ་དང་། ཉིན་མོ་དང་། མཚན་མོ་དང་། མཚམས་ཀྱི་རང་བཞིན་ཡི་གེ་གསུམ་སྐྱེ་བར་འགྱུར་ཏེ། དེ་ཡང་ཕན་ཚུན་ཡི་གེ་ཨོཾ་ཨཱཿལ་ཞུགས་པ་དང་། ཨཱཿཧཱུཾ་ལ་ཞུགས་པ་དང་། ཧཱུཾ་ཐིག་ལེ་དང་བཅས་པ་ལ་དམིགས་ཏེ། ཐིག་ལེ་ནི་ཟླ་ཚེས་ལ་ཐིམ་པ་དང་། ཟླ་ཚེས་མགོ་བོ་ལ་ཐིམ་པ་དང་། མགོ་བོ་ཧ་ལ་ཐིམ་པ་དང་། ཧ་ཞབས་བསྐྱེད༌[^397]ལ་ཐིམ་པ་དང་། ཞབས་བསྐྱེད༌[^398]ཐུང་ངུ་ཨ་རུ་གྱུར་པས་ངག་མ་ལུས་པའི་ངོ་བོ་ཉིད་གནས་པར་འགྱུར་རོ་ཞེས་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་ཀྱིས་ཁྱབ་པའི་སྔགས་ཀྱི༌[^399]བཏུ་བའོ། །

[Block 585]
སྒྱུ་འཕྲུལ་དྲ་བ་ལས་ཀྱང་།

[Block 586 [VERSE]]
ཨ་ནི་ཡིག་འབྲུ་ཀུན་གྱི་མཆོག །
དོན་ཆེན་ཡི་གེ་དམ་པ་སྟེ། །
ཁོང་ནས་འབྱུང་བ་སྐྱེ་བ་མེད། །
ཚིག་ཏུ་བརྗོད་པ་སྤངས་པ་སྟེ། །

[Block 587 [VERSE]]
བརྗོད་པ་ཀུན་གྱི་རྒྱུ་ཡི་མཆོག །
ཚིག་ཀུན་རབ་ཏུ་གསལ་བར་བྱེད། །

[Block 588]
ཅེས་འབྱུང་ངོ་། །རྡོ་རྗེ་དཀྱིལ་འཁོར་གྱི་རྒྱན་ལས་ཀྱང་།

[Block 589 [VERSE]]
སྙིང་གི་དཀྱིལ་ན་མི་ཤིགས་པའི། །
འབར་བའི་མར་མེ་དག་དང་མཚུངས། །
ཡི་གེ་དམ་པ་ཕྲ་བ་ནི། །
ཨ་ནི་ཁྱབ་བདག་གཙོ་བོར་གནས། །

[Block 590]
ཞེས་འབྱུང་ངོ་། །

[Block 591]
གང་ལས་འབྱུང་བ་དང་ཐིམ་པ་དེ་ནི་ཡི་གེ་ཨ་སྟེ། དེའི་རྒྱུ་ཅན་སྔགས་ཐམས་ཅད་ཡིན་པས་བཏུ་བ་ཡང་དེ་ཁོ་ན་ཉིད་ཀྱིས་ཁྱབ་པའོ། །

[Block 592]
གང་གི་ཚེ་མ་ནིང་གི་བཟླས་པའི་དུས་སུ་ལྟེ་བར་ཐིམ་པར་གྱུར་པ་དེའི་ཚེ་འགྲོ་བ་དང་འོང་བ་དང་བྲལ་བ་དང་། [^400]འོད་གསལ་བ་ཉིད་སྔགས་ཐམས་ཅད་སྐྱེད་པར་བྱེད་པའི་རྒྱུ་ཡིན་པས་དེ་ཉིད་ལས་བཏུ་བར་བྱའོ། །

[Block 593]
བཏུ་བ་ནི་རྣམ་པ་གསུམ་སྟེ། གང་གི་ཕྱིར་ཕྱི་མོའི་ཡི་གེ་དང་ཨ་དང་འོད་གསལ་བ་ཉིད་དེ། སྤྲོས་པ་དང་སྤྲོས་པ་མེད་པ་དང་ཤིན་ཏུ་སྤྲོས་པ་མེད་པའི་ཕྱིར་སྤྱོད་པ་བཞིན་ཞེས་བཏུ་བའོ། །

[Block 594 [HEADING]]
###### སྔགས་ཀྱི་དོན། ^1-2-1-2-2-0

[Block 595]
སྔགས་ཀྱི་དོན་ཞེས་བྱ་བ་ནི་ཡི་གེ་ཨོཾ་གྱི་དོན་ནི་རྣམ་པར་སྣང་མཛད་དོ། །

[Block 596]
ཨཱཿའི་དོན་ནི་སྣང་བ་མཐའ་ཡས་སོ། །

[Block 597]
ཡི་གེ་ཧཱུཾ་གི་དོན་ནི་མི་བསྐྱོད་པའོ། །

[Block 598]
སྭཱ་དང་ཧཱ་དག་གི་དོན་ནི་རིན་ཆེན་འབྱུང་ལྡན་དང་དོན་ཡོད་གྲུབ་པའོ། །

[Block 599]
དེ་བཞིན་དུ་གཞན་རྣམས་ཀྱི་བརྗོད་པར་བྱ་བའི༌[^401]དོན་ལ་བརྟེན༌[^402]ཏེ་རང་རང་གི་ལྷའི་བདག་ཉིད་ཀྱི་དོན་བརྟག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 600 [HEADING]]
###### སྔགས་ཀྱི་བརྡ། ^1-2-1-2-3-0
--- END BLOCKS ---
