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
[Block 771 [HEADING]]
### སྒྱུ་མ་ལ་སོགས་པའི་དཔེ་བརྒྱད། ^2-16-0

[Block 772]
བཅོམ་ལྡན་འདས་ཀྱིས་དོན་ཅི་ལས༌[^530]དགོངས་ནས་ཡོད་པ་མ་ཡིན་པའི་སྒྱུ་མ་ལ་སོགས་པའི་དཔེ་བརྒྱད་བསྟན་ཅེ་ན། དེ་བསྟན་པར་བྱའོ། །

[Block 773 [HEADING]]
#### སྒྱུ་མའི་དཔེ། ^2-16-1-0

[Block 774]
དེ་ལ་རེ་ཞིག་སྒྱུ་མའི་དཔེ་ནི་ནང་གི་བདག་ཉིད་ཅན་གྱི་སྐྱེ་མཆེད་དྲུག་པོ་མིག་ལ་སོགས་པ་རྣམས་ཀྱི་གཉེན་པོ་སྟེ་གང་གི་ཕྱིར་སྒྱུ་མའི་གླང་པོ་བཞིན་དུ་དེ་དག་ཡོད་པ་མ་ཡིན་ན་ཡང་ཉེ་བར་དམིགས་པ་ཉིད་དུ་བལྟ་བར་བྱའོ་ཞེས་སྟོན་ཏོ། །

[Block 775 [HEADING]]
#### སྨིག་རྒྱུའི་དཔེ། ^2-16-2-0

[Block 776]
སྨིག་རྒྱུའི་དཔེས་ཀྱང་གང་གི་ཕྱིར་སྣོད་ཀྱི་འཇིག་རྟེན་དེ་རྣམས་ཀྱང་དེ་དང་མཚུངས་པའི་ཕྱིར་སྨིག་རྒྱུ་བཞིན་ཏེ། ཡོད་པ་མ་ཡིན་ན་ཡང་གདུངས་པའི་དབང་གིས་ཆུར་དམིགས་པ་བཞིན་ནོ། །

[Block 777 [HEADING]]
#### རྨི་ལམ་གྱི་དཔེ། ^2-16-3-0

[Block 778]
གཟུགས་ལ་སོགས་པའི༌[^531]ཉེ་བར་སྤྱོད་པའི་གཉེན་པོ་ནི་རྨི་ལམ་གྱི་དཔེས་ཏེ། དེས་ན་རྨི་ལམ་བཞིན་དུ་གཟུགས་ལ་སོགས་པ་འདི་དག་ཡོད་པ་མ་ཡིན་ན་ཡང་དེ་ལས་བྱུང་བའི་འདོད་པ་དང་མི་འདོད་པའི་ཉེ་བར་སྤྱོད་པ༌[^532]ཡང་དེ་བཞིན་དུ་བསྟན་ཏོ། །

[Block 779 [HEADING]]
#### གཟུགས་བརྙན་གྱི་དཔེ། ^2-16-4-0

[Block 780]
ལུས་ཀྱི་ལས་ཀྱི་གཉེན་པོར་གཟུགས་བརྙན་གྱི་དཔེ་འདྲ་བར་ཉེ་བར་བསྟན་ཏེ། དེས་ན་ལུས་ཀྱི་ལས་དགེ་བ་དང་། མི་དགེ་བ་ལ་བརྟེན་ནས་དེ་ལས་གཞན་པའི་གཟུགས་ཀྱི་གཟུགས་བརྙན་འབྱུང་ངོ་ཞེས་སྟོན་ཏོ། །

[Block 781 [HEADING]]
#### བྲག་ཅའི་དཔེ། ^2-16-5-0

[Block 782]
ངག་གི་ལས་ཀྱི་གཉེན་པོར་ནི་བྲག་ཅ༌[^533]དཔེ་བསྟན་ཏེ། ངག་གི་ལས་ཀྱི་རྒྱུ་ཉིད་ལས་ངག་གི་ལས་ཀྱི་འབྲས་བུ་བྲག་ཅ་ལྟ་བུ་ཉིད་དུ་དེས་བསྟན་ཏོ། །

[Block 783 [HEADING]]
#### ཡིད་ཀྱི་ལས། ^2-16-6-0

[Block 784 [HEADING]]
##### མཉམ་པར་མ་བཞག་པའི་ས་པ། ^2-16-6-1-0

[Block 785]
ཡིད་ཀྱི་ལས་ནི་རྣམ་པ་གསུམ་སྟེ་མཉམ་པར་བཞག་པའི་ས་པ་དང་། ཐོས་པའི་རྗེས་སུ་འགྲོ་བ་དང་། འདོད་པ་ན་སྤྱོད་པ་དང་། [^534]དེ་ལ་མཉམ་པར་མ་བཞག་པའི་ས་པ་གང་ཡིན་པའི་གཉེན་པོར་མིག་ཡོར་ལྟ་བུ་ཉིད་ཅེས་བསྟན་ཏེ། དེས་ནི་མིག་ཡོར་ལྟ་བུར་ཞེས་བྱ་བ༌[^535]ཡིད་ཀྱི་ལས་ཀྱི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 786 [HEADING]]
##### མཉམ་པར་གཞག་པའི་ས་པ། ^2-16-6-2-0

[Block 787]
མཉམ་པར་གཞག་པའི་ས་པའི་ཡིད་ཀྱི་ལས་ཀྱི་གཉེན་པོར་ནི་ཆུ་ཟླའི་དཔེ་སྟེ། དེས་ནི་མཉམ་པར་གཞག་པའི་ས་པས༌[^536]ཡིད་ཀྱི་ལས་ནི་ཆུའི་ཟླ་བ་དང་འདྲའོ་ཞེས་བསྟན་ཏོ། །

[Block 788 [HEADING]]
##### ཐོས་པའི་རྗེས་སུ་འགྲོ་བ། ^2-16-6-3-0

[Block 789]
ཐོས་པའི་རྗེས་སུ་འགྲོ་བའི་ཡིད་ཀྱི་ལས་ཀྱི་གཉེན་པོར་ནི་སྤྲུལ་པའི་དཔེ་སྟེ། དེ་ལ་ཐོས་པའི་རྗེས་སུ་འགྲོ་བ་ནི་ཐོས་པ་དང་བསམ་པས་བསྒོས་པའོ། །

[Block 790]
དེས་ནི་ཐོས་པའི་རྗེས་སུ་འགྲོ་བའི་ཡིད་ཀྱི་འཇུག་པ་ནི་སྒྱུ་མ་དང་འདྲ་བའོ༌[^537]ཞེས་བསྟན་ཏོ། །

[Block 791 [HEADING]]
### ཇི་ལྟར་མདོ་ལས་འབྱུང་བ་དང་རྗེས་སུ་མཐུན་པ། ^2-17-0

[Block 792]
ངོ་བོ་ཉིད་གསུམ་གྱི་མཚན་ཉིད་ཀྱི་ཆོས་ཀྱི་ཆོས་ཉིད་དེ་དག་ཇི་ལྟར་མདོ་ལས་འབྱུང་བ་དང་རྗེས་སུ་མཐུན་པར་འགྱུར་བ་ཡིན་ཞེ་ན། ད་ནི་དེ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཚངས་པས་ཞུས་པ་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་ཅི་ལས་དགོངས་ཏེ། དེ་བཞིན་གཤེགས་པས༌[^538]འཁོར་བ་ཡང་མ་དམིགས་མྱ་ངན་ལས་འདས་པ་ཡང་མ་དམིགས་ཞེས་བསྟན་ཞེས་བྱ་བ་གང་། འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ཉིད་བྱེ་བྲག་མེད་པ་ལས་དགོངས་ནས་བསྟན་ཞེས་བྱ་བ་སྟེ། གཞན་གྱི་དབང་ནི་འཁོར་བ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་དེ་མྱ་ངན་ལས་འདས་པར་འགྱུར་བས་སོ། །

[Block 793]
ཀུན་ཏུ་བརྟགས་པའི་ཆོས་ནི་དེ་མྱ་ངན་ལས་འདས་པ་ཡང་མ་ཡིན་ཏེ་འཁོར་བ་ཡིན་ནོ། །

[Block 794]
དེས་ན་གཅིག་པ་ཉིད་དུ་བརྗོད་པར་མི་ནུས་པར་གཟིགས་ནས་གཅིག་ཉིད་དུ་ཞུགས་པའི་བྱེ་བྲག་གི་ངོ་བོ་མེད་པས་འཁོར་བ་ཡང་མི༌[^539]དམིགས་ལ་མྱ་ངན་ལས་འདས་པ་ཡང་མི༌[^540]དམིགས་ཞེས་བྱ་བ་ནི་དེ་ལས༌[^541]དགོངས་ནས་དེར་གསུངས་པ་ཡིན་ནོ། །

[Block 795]
དེ་བཞིན་དུ་ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ཉིད་ནི་ཀུན་ནས་ཉོན་མོངས་པ་ཉིད་དོ། །

[Block 796]
ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ནི་རྣམ་པར་བྱང་བ་ཉིད་དོ། །

[Block 797]
གཞན་གྱི་དབང་ནི་དེ་དག་གཉི་གའི་བདག་ཉིད་མ༌[^542]ཡིན་པ་ཉིད་དེ། དེ་ལ་དགོངས༌[^543]ནས་ཆོས་མངོན་པའི་མདོ་ལས་ཆོས་ནི་གསུམ་སྟེ། ཀུན་ནས་ཉོན་མོངས་པའི་ཆར་གཏོགས་པ་དང་། རྣམ་པར་བྱང་བའི་ཆར་གཏོགས་པ་དང་། དེ་གཉི་གའི་ཆར་གཏོགས་པའོ་ཞེས་བྱ་བ་བསྟན་པ་ཡིན་ནོ། །

[Block 798]
དེ་ཡང་གསེར་གྱི་སྙིང་པོ་ཅན་གྱི་སའི་དཔེས་བསྟན་ཏེ། དེ་ལ་ས་ཁོང་ན་གསེར་ཡོད་པ་ཞེས་བྱ་བ་ནི་གསེར་གྱི་ས་བོན་ནོ། །

[Block 799]
སའི་ཁམས་ནི་སྲ་བ་ཉིད་དོ། །

[Block 800]
ས་ནི་ཉེ་བར་རྟེན་པའི་གཟུགས་སའི་ཁ་དོག་གང་ཡིན་པ་སྟེ། དེ་ལ་གསུམ་པོ་དེ་དག་ཉེ་བར་དམིགས་པ་ཡིན་ནོ། །

[Block 801]
གསེར་ནི་ས་ཉིད་དུ་སྣང་བའོ། །

[Block 802]
དེའི་གསེར་ཉིད་དུ་ཤེས་པ་ནི་ཕྱིས་འབྱུང་བར་འགྱུར་ཏེ། གང་གི་ཚེ་མེ་དང་འཕེལ་བར༌[^544]གྱུར་པ་ན། གསེར་ཉིད་དུ་དམིགས་པར་འགྱུར་བ༌[^545]སྟེ། དེས་ན་དེ་ཡོད་པ་ཉིད་དུ་གྲུབ་པར་འགྱུར་རོ། །

[Block 803 [HEADING]]
### དོན་གྱི་ཚིགས་སུ་བཅད་པ། ^2-18-0

[Block 804]
དོན་གྱི་ཚིགས་སུ་བཅད་པ་ནི།

[Block 805 [VERSE]]
ཇི་ལྟར་ཆོས་རྣམས་ཡོད་མིན་ཞིང་། །
ཇི་ལྟར་རྣམ་པ་དུ་མར་སྣང་། །
ཞེས་བྱ་བ་ལ་གོ་རིམས་བཞིན་དུ།
དེ་བཞིན་ཆོས་དང་ཆོས་མེད་མིན། །

[Block 806]
ཞེས་བྱ་བ་དང་སྦྱར་ཏེ། རྒྱུ་གང་གིས་གང་གི་ཕྱིར་མེད་པ་དེས་ན་ཆོས་རྣམས་ཡོད་པ་མ་ཡིན་ཞིང་གང་གི་ཕྱིར་སྣང་བ་དེས་ན་ཆོས་མེད་པ་ཡང་མ་ཡིན་ཏེ། ཆོས་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 807]
དེས་ན།

[Block 808 [VERSE]]
དེ་བཞིན་ཆོས་དང་ཆོས་མེད་མིན། །
གཉིས་སུ་མེད་པ་གཉིས་སུ་བསྟན། །

[Block 809]
ཆ་རེས་ཞེས་བྱ་བ་སྟེ་མཐའ་གཅིག་གིས་སོ། །

[Block 810]
མེད་པ་དང་ཡོད་པ་ཞེས་བྱ་བ་ནི་དངོས་པོ་དང་དངོས་པོ་མེད་པའོ། །
--- END BLOCKS ---
