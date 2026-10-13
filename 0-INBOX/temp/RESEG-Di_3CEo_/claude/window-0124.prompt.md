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
[Block 4341 [HEADING]]
#### ཟད་པར་བཅུ། ^8-3-4-0

[Block 4342]
ཟད་པར་བཅུའོ། །

[Block 4343]
བར་ཆད་མེད་པར་ཟད་པར་རྒྱས་པར་བྱེད་པའི་ཕྱིར། ཟད་པར་གྱི་སྐྱེ་མཆེད་ནི་བཅུ་སྟེ། ཟད་པར་ས་དང་ཆུ་དང་། མེ་དང་། རླུང་དང་། སྔོན་པོ་དང་། སེར་པོ་དང་། དམར་པོ་དང་། དཀར་པོ་དང་། ཟད་པར་ནམ་མཁའ་དང་། རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་དོ། །

[Block 4344]
དེ་རྣམས་ལས།

[Block 4345]
བརྒྱད་མ་ཆགས།

[Block 4346]
དང་པོ་བརྒྱད་ནི། མ་ཆགས་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 4347]
བསམ་གཏན་མཐའ་ན།[^1661]

[Block 4348]
བཞི་པ་ནའོ། །

[Block 4349]
སྤྱོད་ཡུལ་ནི། འདོད་པ། འདི་དག་གི་དམིགས་པ་ནི། འདོད་པ་ན་སྤྱོད་པའི་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དོ། །

[Block 4350]
གཉིས་ནི་གཟུགས་མེད་དག །ཟད་པར་གྱི་སྐྱེ་མཆེད་ཐ་མ་གཉིས་ནི་གཟུགས་མེད་པ་དག་པ་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 4351]
སྤྱོད་ཡུལ་རང་གི་ཕུང་པོ་བཞི། །འགོག་པའི་རྣམ་པར་ཐར་པ་མ་གཏོགས་པ་རྣམ་པར་ཐར་པ་ལ་སོགས་པ་དེ་དག་ཐམས་ཅད་ནི་སོ་སོའི་སྐྱེ་བོ་དང་འཕགས་པའི་སྐྱེ་བོ་དང་འཕགས་པའི༌[^1662]རྒྱུད་ལ་ཡོད་པ་དག་པ་པ་ཡིན་ནོ། །

[Block 4352]
འདི་དག་ལས།

[Block 4353]
འགོག་པ་བཤད་ཟིན། འགོག་པའི་རྣམ་པར་ཐར་པ་འདི་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 4354]
ལྷག་མ་ནི། འདོད་ཆགས་བྲལ་དང་སྦྱོར་བས་འཐོབ། །འགོག་པ་ལས་གཞན་པའི་རྣམ་པར་ཐར་པ་ལ་སོགས་པའི༌[^1663]འདོད་ཆགས་དང་བྲལ་བས་འཐོབ་པ་ཡང་ཡིན་ལ། སྦྱོར་བ་ལས་བྱུང་བ་དག་ཀྱང་ཡིན་ཏེ།

[Block 4355 [VERSE]]
འདྲིས་པ་དང་མ་འདྲིས་པའི་ཕྱིར་རོ། །
གཟུགས་མེད་ཅེས་བྱ་ཁམས་གསུམ་གྱི། །
རྟེན་ཅན་ལྷག་མ་མི་ལས་སྐྱེ། །

[Block 4356]
གཟུགས་མེད་པའི་རྣམ་པར་ཐར་པ་དང་། གཟུགས་མེད་པའི་ཟད་པར་དག་ནི་ཁམས་གསུམ་པའི་རྟེན་ཅན་དག་གོ། །

[Block 4357]
ལྷག་མ་མིའི་རྟེན་ཅན་ཁོ་ནའོ། །

[Block 4358 [HEADING]]
### ཁམས་གཉིས་སུ་གཟུགས་མེད་དང་བསམ་གཏན་སྐྱེ་བ། ^8-4-0

[Block 4359]
ཇི་ལྟར་ན་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ཏུ་གཟུགས་མེད་པ་དང་། བསམ་གཏན་གྱི་ཁྱད་པར་སྐྱེ་ཞེ་ན།

[Block 4360 [VERSE]]
ཁམས་གཉིས་དག་ཏུ་གཟུགས་མེད་པ། །
རྒྱུ་དང་ལས་ཀྱི་སྟོབས་ཀྱིས་སྐྱེ། །

[Block 4361]
རྒྱུའི་སྟོབས་ཀྱིས་ནི་ཉེ་བ་དང་ཡང་དང་ཡང་དུ་གོམས་པ་ལ་སོགས་པ་ལས་སོ། །

[Block 4362]
ལས་ཀྱི་སྟོབས་ཀྱིས་ནི་ས་གོང་མ་པའི་ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཉེ་བར་གནས་པའི་ཕྱིར་རོ། །

[Block 4363]
གཟུགས་ཀྱི་ཁམས་སུ་བསམ་གཏན་རྣམས། །དེ་དག་དང་ཆོས་ཉིད་ཀྱིས་ཀྱང་། གཟུགས་ཀྱི་ཁམས་སུ་ནི་བསམ་གཏན་རྒྱུ་དང་། ལས་ཀྱི་སྟོབས་དེ་དག་དང་། ཆོས་ཉིད་ཀྱིས་ཀྱང་སྐྱེ་སྟེ། [^1664]འཇིག་པའི་ཚེ་ལྟ་བུའོ། །

[Block 4364 [HEADING]]
### སྟོན་པའི་དམ་ཆོས་གནས་པ། ^8-5-0

[Block 4365]
དམ་པའི་ཆོས་འདི་ཇི་སྲིད་ཅིག༌[^1665]ཏུ་གནས་ཤེ་ན།

[Block 4366 [VERSE]]
སྟོན་པའི་དམ་ཆོས་རྣམ་གཉིས་ཏེ། །
ལུང་དང་རྟོགས་པའི་བདག་ཉིད་དོ། །

[Block 4367]
ལུང་ནི་མདོ་སྡེ་ལ་སོགས་པ་གསུམ་མོ། །

[Block 4368]
རྟོགས་པ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་རྣམས་སོ། །

[Block 4369 [VERSE]]
དེ་འཛིན་བྱེད་པ་སྨྲ་བྱེད་དང་། །
སྒྲུབ་པར༌[^1666]བྱེད་པ་ཁོ་ན་ཡིན། །
ལུང་ནི་འཛིན་པར་བྱེད་པ།
སྨྲ་བར་བྱེད་པ་དག་གོ། །

[Block 4370]
རྟོགས་པར་བྱེད་པ་ནི་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 4371]
དེ་བས་ན་འདི་དག་གནས་པའི་བར་དུ་དམ་པའི་ཆོས་ཀྱང་གནས་སོ། །

[Block 4372 [HEADING]]
### མངོན་པའི་ཆོས་བཤད་ཚུལ་དང་བག་ཡོད་གདམས་པ། ^8-6-0

[Block 4373]
མངོན་པ་འདི་ཉིད་སྟོན་པས་བཤད་དམ་ཞེ་ན།

[Block 4374 [VERSE]]
བདག་གིས་མངོན་པའི་ཆོས་འདི་ཕལ་ཆེར་ནི། །
ཁ་ཆེ་བྱེ་བྲག་སྨྲ་བའི་ཚུལ་གྲུབ་བཤད། །
ཉེས་པར་ཟིན་གང་དེ་འདིར་བདག་གིས་ཉེས། །
དམ་ཆོས་ཚུལ་ལ་ཚད་མ་ཐུབ་རྣམས་ཡིན། །

[Block 4375 [VERSE]]
སངས་རྒྱས་དང༌[^1667]དེའི་སྲས་རྣམས་ཀྱང་ངོ་།[^1668] །
སྟོན་པ་འཇིག་རྟེན་མིག་ནི་ཟུམ་གྱུར་ཅིང་། །
དཔང་གྱུར་སྐྱེ་བོ་ཕལ་ཆེར་ཟད་པ་ན། །
དེ་ཉིད་མ་མཐོང་རང་དགར་གྱུར་པ་ཡིས།[^1669] །

[Block 4376 [VERSE]]
ངན་རྟོག་རྣམས་ཀྱིས་བསྟན་པ་འདི་དཀྲུགས་སོ། །
རང་བྱུང་རང་བྱུང་བསྟན་པ་གཅེས༌[^1670]འཛིན་རྣམས། །
མཆོག་ཏུ་ཞིར་གཤེགས་འགྲོ་མགོན་མེད་པ་ན། །
འདོམས་མེད་ཡོན་ཏན་འཇོམས་པར་བྱེད་པ་ཡི། །

[Block 4377 [VERSE]]
དྲི་མས་དགའ་མགུར་དེང་སང༌[^1671]འདི་ན་སྤྱོད། །
དེ་ལྟར་ཐུབ་པ་དག་གི་བསྟན་པ་ནི། །
ལྐོག་མར་སྲོག་ཕྱིན་འདྲ་དང་དྲི་མ་རྣམས། །
སྟོབས་དང་ལྡན་པའི་དུས་སུ་རིག་ནས་ནི། །
ཐར་པ་འདོད་པ་དག་གིས་བག་ཡོད་གྱིས། །

[Block 4378]
སྙོམས་པར་འཇུག་པ་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་བརྒྱད་པ་རྫོགས་སོ།། །།

[Block 4379 [HEADING]]
## གང་ཟག་བསྟན་པ། ^9-0

[Block 4380 [HEADING]]
### འདི་ལས་གཞན་ལ་ཐར་པ་མེད་པ། ^9-1-0
--- END BLOCKS ---
