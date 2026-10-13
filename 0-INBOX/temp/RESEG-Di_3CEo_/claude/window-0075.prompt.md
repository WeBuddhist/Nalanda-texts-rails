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
[Block 2626]
སྦྱིན་པ་ལས་བྱུང་བ་བཤད་ནས། ཚུལ་ཁྲིམས་ལས་བྱུང་བ་བརྗོད་པར་བྱ་སྟེ།

[Block 2627 [VERSE]]
འཆལ་པའི་ཚུལ་ཁྲིམས་མི་དགེའི་གཟུགས། །
དེ་སྤོང་ཚུལ་ཁྲིམས་རྣམ་གཉིས་སོ། །

[Block 2628]
རྣམ་པར་རིག་བྱེད་གང་སྤོང་བར་བྱེད་པ་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པས་སྤོང་བ་གང་ཡིན་པའོ། །

[Block 2629]
ཚུལ་ཁྲིམས་ནི་འཆལ་པའི་ཚུལ་ཁྲིམས་ཁོ་ན་སྤོང་བ་འབའ་ཞིག་མ་ཡིན་གྱི། འོན་ཀྱང་སངས་རྒྱས་ཀྱིས་ནི་བཅད་པ༌[^1047]ཡང་། རང་བཞིན་གྱི༌[^1048]འཆལ་བའི་ཚུལ་ཁྲིམས་མ་ཡིན་པ་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་བཅད་པ་དུས་མ་ཡིན་པའི་ཟས་ལ་སོགས་པ་གང་དག་ཡིན་པ་དེ་དག་སྤོང་བ་རྣམ་པ་གཉིས་ཀྱང་ཚུལ་ཁྲིམས་ཡིན་ནོ། །

[Block 2630]
ཚུལ་ཁྲིམས་མདོར་བཤད་ཟིན་ཏོ། །

[Block 2631 [VERSE]]
རྣམ་དག་ཡོན་ཏན་བཞི་ལྡན་ནོ། །
ཚུལ་ཁྲིམས་དེའི་རྒྱུས་འཕེན༌[^1049]མ་བྱུང་།[^1050] །
 དེའི་གཉེན་པོ་དང་བཞི་ལ་བརྟེན། །

[Block 2632]
འཆལ་བའི་ཚུལ་ཁྲིམས་ཀྱིས་ཇི་སྐད་བཤད་པའི་ཕན༌[^1051]མ་བྱུང་བའོ། །

[Block 2633]
འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱི༌[^1052]རྒྱུས་ཕན༌[^1053]མ་བྱུང་བ་ནི་ཆགས་པ་ལ་སོགས་པས་ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པས་ཕན༌[^1054]མ་བྱུང་བས༌[^1055]སོ། །

[Block 2634]
འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱི་གཉེན་པོ་ལ་བརྟེན་པ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 2635]
ཞི་བ་ལ་བརྟེན་པ་ནི་མྱ་ངན་ལས་འདས་པར་ཡོངས་སུ་བསྔོ་བའི་ཕྱིར་རོ། །

[Block 2636]
ཚུལ་ཁྲིམས་རྫོགས་སོ།། །།

[Block 2637 [HEADING]]
##### བསྒོམ་པ། ^4-3-14-3-0

[Block 2638]
མཉམ་པར་གཞག་པའི་དགེ་བ་ནི། །བསྒོམ་པའོ། །

[Block 2639]
མཉམ་པར་གཞག་པ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་གྱི་རང་བཞིན་དང་ལྷན་ཅིག་འབྱུང་བའོ། །

[Block 2640]
འདི་ཅིའི་ཕྱིར༌[^1056]བསྒོམ་པ་ཞེས་བྱ་ཞེ་ན། སེམས་ལ་བསྒོ༌[^1057]ཕྱིར་རོ། །

[Block 2641]
མཉམ་པར་གཞག་པའི་དགེ་བ་དེ་ནི་རྒྱུད་ཡོན་ཏན་རྣམས་ཀྱིས་དེའི་བདག་ཉིད་དུ་བྱེད་པའི་ཕྱིར་སེམས་ལ་ཤིན་ཏུ་བསྒོ་བར༌[^1058]བྱེད་པ་ཡིན་ནོ། །

[Block 2642]
རེ་ཞིག་སྦྱིན་པས་ནི་ལོངས་སྤྱོད་ཆེན་པོར་འགྱུར་རོ་ཞེས་བཤད་ན་ཚུལ་ཁྲིམས་དང་བསྒོམ་པས་ཅིར་འགྱུར་ཞེ་ན།

[Block 2643 [VERSE]]
མཐོ་རིས་དོན་དུ་ཚུལ་ཁྲིམས་དང་། །
འབྲལ་བའི་དོན་དུ་བསྒོམ་གཙོའི་ཕྱིར། །

[Block 2644]
སྦྱིན་པ་ཡང་མཐོ་རིས་ཀྱི་དོན་དུ་འགྱུར་མོད་ཀྱི། ཚུལ་ཁྲིམས་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2645]
ཚུལ་ཁྲིམས་ཀྱིས་ཀྱང་འབྲལ་བར་འགྱུར་མོད་ཀྱི་བསྒོམ་པ་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2646]
མདོ་ལས་གང་ཟག་བཞི་ནི་ཚངས་པའི་བསོད་ནམས་འབྱུང་བར་གསུངས་པ་གང་ཞེ་ན།

[Block 2647 [VERSE]]
བསྐལ་པར་མཐོ་རིས་དགའ་གནས་ཕྱིར། །
བཞི་ཡིས་ཚངས་པའི་བསོད་ནམས་ཡིན། །

[Block 2648]
བསོད་ནམས་ཇི་ཙམ་གྱིས་ན་བསྐལ་པར་མཐོ་རིས་སུ་དགའ་བར་གནས་པར་འགྱུར་བ་འདི་ནི་ཚངས་པའི་བསོད་ནམས་ཡིན་ནོ། །

[Block 2649]
ཟང་ཟིང་གི་སྦྱིན་པ་བཤད་ཟིན་ཏོ། །

[Block 2650 [HEADING]]
##### ཆོས་སྦྱིན། ^4-3-14-4-0

[Block 2651 [VERSE]]
ཆོས་སྦྱིན་ཉོན་མོངས་ཅན་མིན་པས། །
མདོ་སོགས་ཡང་དག་ཇི་བཞིན་སྟོན། །

[Block 2652]
ཆོས་ཀྱི་སྦྱིན་པ་ནི་མདོ་ལ་སོགས་པ་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ཇི་ལྟ་བ་བཞིན་སྟོན་པའོ། །

[Block 2653 [HEADING]]
#### བསོད་ནམས་དང་མྱ་ངན་འདས་པ་དང་ངེས་འབྱེད་ཆ་མཐུན་གྱི་དགེ་བ། ^4-3-15-0

[Block 2654]
བསོད་ནམས་བྱ་བའི་གཞི་རྣམ་པ་གསུམ་བཤད་ནས། ཡང་།

[Block 2655 [VERSE]]
བསོད་ནམས་མྱ་ངན་འདས་པ་དང་། །
ངེས་འབྱེད་ཆ་མཐུན་དགེ་རྣམ་གསུམ། །

[Block 2656]
བསོད་ནམས་ཀྱི་ཆ་དང་མཐུན་པ་ནི་རྣམ་པར་སྨིན་པ་ཡིད༌[^1059]དུ་འོང་བ་ཅན་གང་ཡིན་པའོ། །

[Block 2657]
ཐར་པའི་ཆ་དང་མཐུན་པ་ནི་གང་སྐྱེས་ནས༌[^1060]ངེས་པར་མྱ་ངན་ལས་འདའ་བའི་ཆོས་སུ་འགྱུར་རོ། །

[Block 2658]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ནི་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 2659 [HEADING]]
#### ཡིག་འབྲུ་དང་རྒྱ་ལ་སོགས་པ། ^4-3-16-0

[Block 2660]
འཇིག་རྟེན་ན་ཡིག་འབྲུ་དང་། རྒྱ༌[^1061]དང་། བགྲང་བ་དང་། སྙན་དངག་དང་། གྲངས་ཞེས་བྱ་བ་གང་ཡིན་པ་འདི་དག་གི་རང་བཞི་ན་ཅི་ཞེ་ན།

[Block 2661 [VERSE]]
རིགས་པས༌[^1062]རབ་ཏུ་བཅུག་པའི་ལས། །
རྣམ་གསུམ་ཀུན་སློང་བཅས་པ་ནི། །
ཡིག་འབྲུ་རྒྱ༌[^1063]དང་བགྲངས་བཅས་པའི། །
སྙན་དངག་གྲངས་ཏེ་གོ་རིམས་བཞིན། །

[Block 2662]
རིགས་པས་བཅུག་པ་ཞེས་བྱ་བ་ནི་ཐབས་ཀྱི་བྱེ་བྲག་གིས་བཅུག་པའོ། །

[Block 2663]
ལས་རྣམ་གསུམ་ཞེས་བྱ་བ་ནི། ལུས་དང་། ངག་དང་། ཡིད་ཀྱི་ལས་སོ། །

[Block 2664]
དེ་ལ་རེ་ཞིག་ཡིག༌[^1064]འབྲུ་དང་། རྒྱ་ནི་ལུས་ཀྱི་ལས་རིགས་པས་རབ་ཏུ་བཅུག་པ་ཀུན་ནས་སློང་བ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2665]
བགྲང་བ་དང་སྙན་ངག་ནི་ངག་གི་ལས་ཏེ། དེ་ལྟ་ན་དེ་དག་ནི་ཕུང་པོ་ལྔའི་རང་བཞིན་ཡིན་ནོ། །
--- END BLOCKS ---
