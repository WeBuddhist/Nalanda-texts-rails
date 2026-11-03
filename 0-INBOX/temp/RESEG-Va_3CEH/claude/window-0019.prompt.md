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
[Block 666]
འདོད་པའི་ཁམས་ལ་སོགས་པ་ཞེས་བྱ་བ་སྔ་མ་བཞིན་ཏེ། སྩོགས་པ༌[^477]སྨོས་པས༌[^478]ནི་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་བསྡུའོ། །

[Block 667 [HEADING]]
#### མཚན་མར་སྣང་བར་འགྱུར་བའི་རྣམ་པར་རྟོག་པ། ^2-11-5-0

[Block 668]
མཚན་མར་སྣང་བར་འགྱུར་བའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ལ། མིག་ལ་སོགས་པའི་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་དེའི་མཚན་མར་སྣང་བར་གང་འགྱུར་བ་སྟེ། མཚན་མར་སྣང་བར་འགྱུར་བའི་བདག་ཉིད་ཀྱི་རྣམ་པར་རྟོག་པའོ། །

[Block 669]
དེ་ལྟ་བས་ན་འདི་དག་གི་ཡང་དག་པ༌[^479]ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པའི་རྒ་བ་ལ་སོགས་པ་གང་གིས་དེ་དང་དེའི་གནས་སྐབས་སུ་འགྱུར་བ་སྐྱེད་པར་བྱེད་པའོ། །

[Block 670 [HEADING]]
#### གཞན་གྱིས་བསྟན་པའི་རྣམ་པར་རྟོག་པ། ^2-11-6-0

[Block 671]
གཞན་གྱིས་བསྟན་པའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ནི་གང་གཞན་གྱིས་བསྟན་པའོ། །

[Block 672]
ཡང་དེ་ནི་རྣམ་པ་གཉིས་ཏེ། དམ་པ་མ་ཡིན་པའི་ཆོས་ཉན་པའི་རྗེས་སུ་འགྲོ་བ་དང་དམ་པའི་ཆོས་ཉན་པའི་རྗེས་སུ་འགྲོ་བའོ། །

[Block 673]
དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཆོས་རྣམས་ལ་རྣམ་པར་རྟོག་པ་ནི་ཆོས་ཉན་པའི་རྗེས་སུ་འགྲོ་བ་སྟེ། དགེ་བ་རྣམས་དང་མི་དགེ་བ་རྣམས་ཞེས་བྱ་བ༌[^480]འདི་ལྟར་བསྡུ་བར་བྱའོ། །

[Block 674 [HEADING]]
#### ཚུལ་བཞིན་མ་ཡིན་པའི་རྣམ་པར་རྟོག་པ། ^2-11-7-0

[Block 675]
ཚུལ་བཞིན་མ་ཡིན་པའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ལ། དེ་ཡང་དམ་པ་མ་ཡིན་པའི་ཆོས་མཉན་པ༌[^481]ལས་བྱུང་བའོ། །

[Block 676]
འདི་ལས་ཕྱི་རོལ་པ་རྣམས་ཀྱིས༌[^482]ཞེས་བྱ་བ་ནི་མུ་སྟེགས་པ་རྣམས་སོ། །

[Block 677 [HEADING]]
#### ཚུལ་བཞིན་གྱི་རྣམ་པར་རྟོག་པ། ^2-11-8-0

[Block 678]
ཚུལ་བཞིན་གྱི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ལ། དེ་ཡང་དམ་པའི་ཆོས་ཉན་པ༌[^483]ལས་བྱུང་བ་སྟེ། ཆོས་འདི་པ་རྣམས་ཞེས་བྱ་བ་ནི་སངས་རྒྱས༌[^484]རྣམས་སོ། །

[Block 679 [HEADING]]
#### མངོན་པར་ཞེན་པའི་རྣམ་པར་རྟོག་པ། ^2-11-9-0

[Block 680]
མངོན་པར་ཞེན་པའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ནི་གང་ཚུལ་བཞིན་མ་ཡིན་པའི་ཡིད་ལ་བྱེད་པའི་རྒྱུ་ལས་བྱུང་བ་སྟེ། བདག་ཏུ་ལྟ་བ་ལ་བརྟེན་པ་མདོ་ལས་བསྟན་པའི་ལྟ་བ་དྲུག་ཅུ་རྩ་གཉིས་སུ་གཏོགས་པ་དང་མཚུངས་པར་ལྡན་པའི་རྣམ་པར་རྟོག་པ་གང་ཡིན་པའོ། །

[Block 681 [HEADING]]
#### རྣམ་པར་གཡེང་བའི་རྣམ་པར་རྟོག་པ། ^2-11-10-0

[Block 682]
རྣམ་པར་གཡེང་བའི་རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་རྣམ་པར་རྟོག་པ་བཅུ༌[^485]གང་ཡིན་པའོ། །

[Block 683 [HEADING]]
##### དངོས་པོ་མེད་པའི་མཚན་མའི་རྣམ་པར་གཡེང་བ། ^2-11-10-1-0

[Block 684]
དེ་ལ་དངོས་པོ་མེད་པའི་མཚན་མའི་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ནི་དངོས་པོ་མེད་པ་ཉིད་མཚན་མ་སྟེ། རྣམ་པར་གཡེང་བའོ་ཞེས་བྱས་ནས་སོ། །

[Block 685]
ཡང་རྣམ་པར་གཡེང་བ་དེའི་གཉེན་པོ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་གཞུང་ལས།

[Block 686]
བྱང་ཆུབ་སེམས་དཔའ་ཉིད་ཡོད་བཞིན་དུ་ཞེས་བྱ་བ་སྟེ། ཡོད་ཅེས་སྨོས་པས་ནི་བྱང་ཆུབ་སེམས་དཔའ་སྟོང་པ་ཉིད་ཀྱི་བདག་ཉིད་དུ་ཡོད་པའོ། །

[Block 687]
འདི་ལྟར་བསྟན་ཏེ། གང་ལས་བསྟན་པ་ཉིད༌[^486]བདག་ཉིད་ཡོད་པ་དེ་ནི་སྟོང་པ་ཉིད་ཀྱི་བདག་ཉིད་དོ་ཞེས་བྱ་བའོ། །

[Block 688 [HEADING]]
##### དངོས་པོའི་མཚན་མའི་རྣམ་པར་གཡེང་བ། ^2-11-10-2-0

[Block 689]
དངོས་པོའི་མཚན་མའི་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ནི་དངོས་པོ་ཉིད་ནི་རྣམ་པར་གཡེང་བའི་མཚན་མ་སྟེ།

[Block 690]
དེའི་གཉེན་པོ་ནི་ཡང་གཞུང་དེ་ཉིད་ལས།

[Block 691]
བྱང་ཆུབ་སེམས་དཔའ་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་ངོ་ཞེས་བྱ་བ་སྟེ། ཀུན་ཏུ་བརྟགས་པ་དང་། གཞན་གྱི་དབང་གི་བདག་ཉིད་ཅན་གྱི་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་ངོ་ཞེས་བྱ་བར་དགོངས་སོ། །

[Block 692 [HEADING]]
##### སྒྲོ་འདོགས་པའི་རྣམ་པར་གཡེང་བ། ^2-11-10-3-0

[Block 693]
སྒྲོ་འདོགས་པའི་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ལ།

[Block 694]
དེའི་གཉེན་པོར་ནི་ཡང་གཞུང་དེ་ཉིད་ལས།

[Block 695]
གཟུགས་ནི་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་སྟེ། ཀུན་ཏུ་བརྟགས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 696 [HEADING]]
##### སྐུར་པ་འདེབས་པའི་རྣམ་པར་གཡེང་བ། ^2-11-10-4-0

[Block 697]
སྐུར་པ་འདེབས་པའི་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ལ།

[Block 698]
དེའི་གཉེན་པོ་འདི་ཡང་གཞུང་དེ་ཉིད་ལས།

[Block 699]
སྟོང་པ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ། ཆོས་ཉིད་ཀྱི་ངོ་བོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 700 [HEADING]]
##### གཅིག་པུ་ཉིད་དུ་རྣམ་པར་གཡེང་བ། ^2-11-10-5-0

[Block 701]
གཅིག་པུ་ཉིད་དུ་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ལ། དེའི་གཉེན་པོའི་གཞུང་ནི་གཟུགས་ཀྱི་སྟོང་པ་ཉིད་གང་ཡིན་པ་དེ་གཟུགས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ། གལ་ཏེ་གཞན་གྱི་དབང་དང་ཡོངས་སུ་གྲུབ་པ་དག་གཅིག་ཡིན་ན་དེས་ན་གཞན་གྱི་དབང་ཡང་ཡོངས་སུ་གྲུབ་པ་བཞིན་དུ་དམིགས་པ་རྣམ་པར་དག་པར་འགྱུར་རོ། །

[Block 702 [HEADING]]
##### ཐ་དད་པ་ཉིད་དུ་རྣམ་པར་གཡེང་བ། ^2-11-10-6-0

[Block 703]
ཐ་དད་པ་ཉིད་དུ་རྣམ་པར་གཡེང་བ་ཞེས་བྱ་བ་ལ། དེའི་གཉེན་པོའི་གཞུང་ནི་གཟུགས་ནི་སྟོང་པ་ཉིད་ལས་གཞན་པ་ཡང་མ་ཡིན་ཏེ། གཟུགས་ཉིད་སྟོང་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྟེ། གང་གི་ཕྱིར་དེ་དག་ཐ་དད་པ་ཡིན་ན་ཆོས་ལས་ཆོས༌[^487]ཉིད་ཐ་དད་པ་ཉིད་དུ་འགྱུར་ན། ཐ་དད་པ་ཉིད་དུ་འགྱུར་བ་ནི་མི༌[^488]རུང་བ་མ་ཡིན་ཏེ། མི་རྟག་པའི་མི་རྟག་པ་ཉིད་བཞིན་ནོ། །

[Block 704]
ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ཡོངས་སུ་བཟུང་ནས་གཟུགས་ཉིད་སྟོང་པ་ཉིད་དོ། །

[Block 705]
སྟོང་པ་ཉིད་གཟུགས་སོ་ཞེས་བྱ་བ་སྟེ། གང་ཀུན་ཏུ་བརྟགས་པ༌[^489]དེའི་ངོ་བོ་ཉིད་མེད་པ་དེ་ནི་སྟོང་པ་ཉིད་ཡིན་ལ། གང་སྟོང་པ་ཉིད་ཡིན་པ་དེ་ནི་དེའི་ངོ་བོ་ཉིད་མེད་པ་ཡིན་གྱི། ཇི་ལྟར་གཞན་གྱི་དབང་དང་ཡོངས་སུ་གྲུབ་པ་དག་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
