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
[Block 666 [HEADING]]
##### སེམས་བྱུང་རྣམ་ལྔ། ^2-2-2-1-0

[Block 667]
སེམས་ལས་བྱུང་བ་རྣམས་ཞེས་བརྗོད་པ་སེམས་ལས་བྱུང་བ་དེ་དག་གང་ཞེ་ན། སེམས་བྱུང་རྣམ་ལྔ་སྟེ། ས་མང༌[^265]ལ་སོགས་ཐ་དད་ཕྱིར། །འདི་ལྟ་སྟེ། ས་མང་པོ༌[^266]དག་དང་། དགེ་བའི་ས་མང་པོ་པ་རྣམས་དང་། ཉོན་མོངས་པའི་ས་མང་པོ་པ་རྣམས་དང་། མི་དགེ་བའི་ས་མང་པོ་པ་རྣམས་དང་། ཉོན་མོངས་པ་ཆུང་ངུའི་ས་པ་རྣམས་སོ། །

[Block 668 [VERSE]]
ཚོར་དང་སེམས་པ་འདུ་ཤེས་དང་། །
འདུན༌[^267]དང་རེག་དང་བློ་གྲོས་དྲན། །
ཡིད་ལ་བྱེད་དང་མོས་པ་དང་། །
ཏིང་ངེ་འཛིན་སེམས་ཐམས་ཅད་ལ། །

[Block 669]
དེ་ལ་ཚོར་བ་ནི་བཤད་ཟིན་ཏོ། །

[Block 670]
སེམས་པ་ནི་སེམས་མངོན་པར་འདུ་བྱེད་པའོ། །

[Block 671]
འདུ་ཤེས་ནི་བརྗོད་ཟིན་ཏོ། །

[Block 672]
འདུན་པ་ནི་བྱེད་འདོད་པའོ། །

[Block 673]
རེག་པ་ནི་ཡུལ་དང་དབང་པོ་དང་རྣམ་པར་ཤེས་པ་འདུན་པ༌[^268]ལས་སྐྱེས་པའི་རེག་པའོ། །

[Block 674]
བློ་གྲོས་ནི་ཤེས་རབ་སྟེ། ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པའོ། །

[Block 675]
དྲན་པ་ནི་དམིགས་པ་མ་བརྗེད༌[^269]པའོ། །

[Block 676]
ཡིད་ལ་བྱེད་པ་ནི་སེམས་ཀྱི་འཇུག་པའོ། །

[Block 677]
མོས་པ་ནི་འདོད་པའོ། །

[Block 678]
ཏིང་ངེ་འཛིན་ནི་སེམས་རྩེ་གཅིག་པ་ཉིད་དོ། །

[Block 679]
འདི་དག་ནི་ས་ཐམས་ཅད་ལ་འབྱུང་ངོ་། །

[Block 680 [VERSE]]
དད་དང་བག་ཡོད་ཤིན་ཏུ་སྦྱངས། །
བཏང་སྙོམས་ངོ་ཚ་ཤེས་ཁྲེལ་ཡོད། །
རྩ་བ་གཉིས་རྣམ་མི༌[^270]འཚེ་དང་། །
བརྩོན་འགྲུས་རྟག་ཏུ་དགེ་ལ་འབྱུང་། །

[Block 681]
དེ་ལ་དད་པ་ནི་སེམས་དང་བའོ། །

[Block 682]
བག་ཡོད་པ་ནི་དགེ་བའི་ཆོས་རྣམས་བསྒོམ་པ་སྟེ། དེ་དག་ལ་གཅེས་སུ་འཛིན་པས་ཀུན་དུ་སྲུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 683]
ཤིན་ཏུ་སྦྱངས་པ་ནི་སེམས་ལས་སུ་རུང་བ་ཉིད་དོ། །

[Block 684]
བཏང་སྙོམས་ནི་སེམས་མཉམ་པ་ཉིད་དང་སེམས༌[^271]ལྷུན་གྱིས་གྲུབ་པ་ཉིད་དོ། །

[Block 685]
ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་ནི་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 686]
རྩ་བ་གཉིས་ནི་ཆགས་པ་མེད་པ་དང་། ཞེ་སྡང་མེད་པ་དག་གོ། །

[Block 687]
གཏི་མུག་མེད་པ་ཡང་ཡོད་མོད་ཀྱི་དེ་ཡང་ཤེས་རབ་སྟེ། ས་མང་པོ་པར་བཤད་དོ། །

[Block 688]
རྣམ་པར་མི་འཚེ་བ་ནི་རྣམ་པར་ཐོ་མི་འཚམས༌[^272]པའོ། །

[Block 689]
བརྩོན་འགྲུས་ནི་དགེ་བ་ལ་སེམས་མངོན་པར་སྤྲོ་བའོ། །

[Block 690]
འདི་དག་ནི་དགེ་བའི་སེམས་ཐམས་ཅད་ལ་འབྱུང་བའོ། །

[Block 691 [VERSE]]
རྨོངས་དང་བག་མེད་ལེ་ལོ་དང་། །
མ་དད་པ་དང་རྨུགས་དང་རྒོད། །
ཉོན་མོངས་ཅན་ལ་རྟག་ཏུ་འབྱུང་། །

[Block 692]
དེ་ལ་རྨོངས་པ་ནི་མི་ཤེས་པ་དང་མི་གསལ་བའོ། །

[Block 693]
བག་མེད་པ་ནི་བག་ཡོད་པའི་མི་མཐུན་པའོ། །

[Block 694]
ལེ་ལོ་ནི་བརྩོན་འགྲུས་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་སོ། །

[Block 695]
མ་དད་པ་ནི་དད་པའི་མི་མཐུན་པའོ། །

[Block 696]
རྨུགས་པ་ནི་སེམས་ལས་སུ་མི་རུང་བའོ། །

[Block 697]
རྒོད་པ་ནི་སེམས་རྣམ་པར་མ་ཞི་བ་སྟེ། འདི་དག་ནི་ཉོན་མོངས་པ་ཅན་གྱི་སེམས་ཐམས་ཅད་ལ༌[^273]འབྱུང་ངོ་། །མི་དགེ་ལ་ནི་ཁྲེལ་མེད་དང་། །ངོ་ཚ་མེད་པའོ། །

[Block 698]
དེ་དག་གི་མཚན་ཉིད་ནི་འོག་ནས་འཆད་དོ། །

[Block 699]
ཁྲོ་བ་དང་།

[Block 700 [VERSE]]
ཁོན་དུ་འཛིན་དང་གཡོ་དང་ནི། །
ཕྲག་དོག་འཚིག་འཆབ་སེར་སྣ་དང་། །
སྒྱུ༌[^274]དང་རྒྱགས་དང་རྣམ༌[^275]འཚེ་ནི། །
ཉོན་མོངས་ཆུང་ངུའི་ས་པ་རྣམས།

[Block 701]
འདི་དག་ནི་མ་རིག་པ་ཙམ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བ་དང་། ཡིད་ཀྱི་ས་པ་ཁོ་ན་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་ཉོན་མོངས་པ་ཆུང་ངུའི་ས་པར་བརྗོད་དོ། །

[Block 702]
འདི་དག་གི་རྒྱས་པར་བཤད་པ་ནི་ཕྱིས་འཆད་དོ། །

[Block 703 [HEADING]]
##### སེམས་གང་ལ་སེམས་ལས་བྱུང་བ་དུ་ཞིག་འབྱུང་བ། ^2-2-2-2-0

[Block 704]
སེམས་གང་ཞིག་ལ་སེམས་ལས་བྱུང་བ་དུ་ཞིག་གདོན་མི་ཟ་བར་འབྱུང་བ༌[^276]བརྗོད་པར་བྱ་སྟེ། རེ་ཞིག་འདོད་པ་ན་སྤྱོད་པའི་སེམས་ནི་རྣམ་པ་ལྔ་སྟེ་དགེ་བ་ལ་སོགས་པའོ། །

[Block 705]
དེ་ལ།
--- END BLOCKS ---
