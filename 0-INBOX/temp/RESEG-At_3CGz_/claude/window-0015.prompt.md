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
ཐམས་ཅད་ཡོད་པར་སྨྲ་བའི༌[^284]སྡེ་པའི་འདུལ༌[^285]བ་འཛིན་པ་བཙུན་པ་ཆོས་སྐྱོབ་དང་། བཙུན་པ་དབྱངས་སྒྲོགས༌[^286]དང་། བཙུན་པ་དབྱིག་བཤེས༌[^287]དང་། བཙུན་པ་སངས་རྒྱས་ལྷ་དང་། བཙུན་པ་བསམ་རྫོགས་དང་། མཁས་པ་ཆེན་པོ་ནོར་གྱི་རྩ་ལག་དང་། གནས་བརྟན་ཡོན་ཏན་འོད་དང་། བཙུན་པ་ཤཱཀྱ་འོད་ལ་སོགས་པ་དག་ན་རེ། རྣམ་པ་བཅུས་བསྙེན་པར་རྫོགས་ཏེ། རང་བྱུང་བས་ནི་སངས་རྒྱས་དང་རང་སངས་རྒྱས་སོ། །

[Block 527]
ངེས་པར་འཇུག་པ་ནི་རྟེན་ལྔ་པའོ། །

[Block 528]
དགེ་སློང་ཚུར་ཤོག་ཅེས་པས་ནི་གྲགས་པ་ལ་སོགས་པའོ། །

[Block 529]
སྟོན་པར་ཁས་བླངས་པས་ནི་འོད་སྲུངས་ཆེན་པོ་ལ་སོགས་པའོ། །

[Block 530]
དྲི་བས་མཉེས་པ༌[^288]ནི་ལེགས༌[^289]སྦྱིན་ལ་སོགས་པའོ། །

[Block 531]
བླ་མའི་ཆོས་ཁས་བླངས་པ་ནི་སྐྱེ་དགུའི་བདག་མོ་ཆེན་མོའོ། །

[Block 532]
ཕོ་ཉས་ནི་ཆོས་སྦྱིན་ནོ། །

[Block 533]
འདུལ་བ་འཛིན་པ་མ་གཏོགས་པ་ལྔས་ནི་མཐའ་འཁོབ་པའོ། །

[Block 534]
བཅུའི་ཚོགས་ཀྱིས་ནི་དབུས་ཀྱི་མི་རྣམས་ཏེ་སྐྱབས་སུ་འགྲོ་བ་ལན་གསུམ་བཟླས༌[^290]པས་ནི་སྡེ་བཟང་དྲུག་ཅུའི་ཚོགས་བསྙེན་པར༌[^291]རྫོགས་པར་བྱས་སོ་ཞེས་ཟེར་རོ། །

[Block 535]
དགེ་སློང་ནི་བཞི་སྟེ། མིང་གི་དགེ་སློང་དང་། ཁས་འཆེ་བའི་དགེ་སློང་དང་། སློང་བས་ན་དགེ་སློང་དང་། ཉོན་མོངས་པ་འཇོམས་པའི་དགེ་སློང་ངོ་། །དིང་སང་གི་དུས་ན་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པའི་དགེ་སློང་ནི་ཤིན་ཏུ་དཀོན་ཏེ། སློབ་དཔོན་ཞི་བ་ལྷའི་ཞལ་ནས།

[Block 536]
བསྟན་རྩ་དགེ་སློང་ཉིད་ཡིན་ཏེ། །དགེ་སློང་ཉིད་ཀྱང་དཀའ་བར་གནས། །ཞེས་གསུངས་པས། དགེ་སློང་བསླབ་པ་ལ་རྨ་བྱུང་བ། ཉམས་པ་རལ་བ་ནག་ནོག་ཅན་དུ་གྱུར་པ་དང་། ཞིག་པ་དང་མ་ཚང་བར་གྱུར་པའི་དགེ་སློང་བས་ནི་དགེ་བསྙེན་རྣམ་པར་དག་པ་ཐེག་པ་ཆེན་པོའི་སྣོད་དུ་བསྔགས་སོ་ཞེས་བླ་མ་དག་ཆེད་ཆེར་གསུང་ངོ་། །

[Block 537 [HEADING]]
## སྡོམ་པ། ^5-0

[Block 538]
ཡང་བཤད་པར་བྱ་སྟེ། སྡོམ་པ་ཞེས་བྱ་བ་ནི་འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱི་རྒྱུན་འགོག་ཅིང་སྡོམ་པའོ། །

[Block 539]
དེ་ཡང་འདི་ལྟར་གང་ལས་འཐོབ་པ་དང་། ཇི་ལྟར་འཐོབ་པ་དང་། སྡོམ་པ་བླང་བའི་དུས་དང་། ཇི་ལྟར་བླང་བ་དང་། ཇི་ལྟར་གཏོང་བ་དང་། དེའི་རང་བཞིན༌[^292]དང་། ལྟུང་བ་འབྱུང་བའི་རྒྱུ་དང་། ལྟུང་བ་མི་འབྱུང་བའི་རྒྱུ་དང་། ལྟུང་བ་ལས་ལྡང་བའོ།[^293] །

[Block 540 [HEADING]]
### གང་ལས་འཐོབ་པ། ^5-1-0

[Block 541]
གང་ལས་འཐོབ་ཅེས་པ་ལ་སོགས་པའི་དོན་ནི་འདུལ་བ་འཛིན་པ་ལ་དྲི་བ་དང་། གཞུང་དག་བལྟ་བར་བྱའོ། །

[Block 542 [HEADING]]
### ཇི་ལྟར་གཏོང་བ། ^5-2-0

[Block 543]
ཇི་ལྟར་གཏོང་ཞེ་ན། སོ་སོར༌[^294]ཐར་པའི་སྡོམ་པ་གཏོང་བའི་རྒྱུ་ནི་མང་སྟེ། མི་བརྡ་ཕྲད་པའི་དྲུང་དུ་བསླབ་པའི་གཞི་རྣམས་བསམ་པ་ཐག་པ་ནས་ཕུལ་བ་དང་། རིས་མཐུན་པ་བཏང་བ་དང་། ཕམ་པའི་ཉེས་པ་བྱུང་བ་དང་། མཚན་གཉིས་དུས་གཅིག་ཏུ་བྱུང་བ་དང་། དགེ་བའི་རྩ་བ་ཆད་པའོ། །

[Block 544]
ཅིའི་ཕྱིར་སྡོམ་པ་དེ་གཏོང་བའི་རྒྱུ་ཡིན་ཞེ་ན། ཡང་དག་པར་གཏང་བའི༌[^295]སེམས༌[^296]སྐྱེས་པ་དང་། རྟེན་བོར་བ་དང་། ལྟུང་བའི་རྒྱུ་གང་ཡང་རུང་བ་སྐྱེས་པ་དང་། རྟེན་ཉམས་པ་དང་། གཞི་ཆད་པའོ། །

[Block 545]
ཡང་འདུལ་བ་འཛིན་པ་ལ་ལ་ན་རེ། ལྟུང་བ་གཅིག་བྱུང་བས་ཐམས་ཅད་གཏོང་བར༌[^297]འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 546]
ཁ་ཅིག་དམ་པའི་ཆོས་ནུབ་པའི་དུས་སུ་གཏོང་ངོ་ཞེས་སོ། །

[Block 547]
ཐམས་ཅད་ཡོད་པར་སྨྲ་བའི་འདུལ་བ་འཛིན་པ་དག་ནི་འདི་སྐད་དུ་ལྟུང་བ་གཅིག་བྱུང་བས་ལྷག་མ་མི་གཏོང་སྟེ། དེ་ལ་སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་གཉིས་ཀ་ཡོད་དེ། མི་ཞིག་ལ་ནོར་ཡང་ཡོད་ལ་བུ་ལོན་ཡང་ཆགས་པ་བཞིན་ནོ། །

[Block 548]
ལྟུང་བ་དེ་བཤགས་ན་དེ་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཡིན་གྱི། སྡོམ་པ་མེད་པ་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 549]
མཚན་གྱུར་པ་ནི་སྔོན་མེད་པའི་སྡོམ་པ་ཡང་མི་གཏོང་ལ། ཐོབ་ཟིན་པ་ཡང་གཏོང་བར་མི་འགྱུར་རོ། །

[Block 550]
དམ་པའི་ཆོས་ནུབ་པ་ན་ཡང་དེ་བཞིན་ནོ། །

[Block 551]
ཚེ་འཕོས་པས་གཏོང་བ་ཡང་འདི་ལྟར་ལུས་མི་འདྲ་བ་དང་དེར་སྦྱོར་བ་མ་བྱས་པ་དང་། སྡོམ་པ་མི་དྲན་པའི་ཕྱིར་རོ། །

[Block 552]
དེ་དག་ནི་སློབ་དཔོན་ནོར་གྱི་རྩ་ལག་གི་རྗེས་སུ་འབྲངས༌[^298]ནས་བཤད་པའོ། །

[Block 553]
གཞུང་དེ་མ་ཡིན་པའི་ལུགས་མང་དུ་ཡོད་མོད་ཀྱི་འདིར་གཞག་གོ། །

[Block 554 [HEADING]]
### དེའི་རང་བཞིན། ^5-3-0

[Block 555]
རང་བཞིན་ཡང་འདུལ་བའི་གཞུང་དག་དང་། རང་རང་སྡེ་པའི་འདུལ་བ་འཛིན་པ་ལ་དྲི་བར་བྱའོ། །

[Block 556 [HEADING]]
### ལྟུང་བ་འབྱུང་བའི་རྒྱུ། ^5-4-0

[Block 557]
ལྟུང་བ་འབྱུང་བའི་རྒྱུ་ནི་གཉིས་ཏེ། བྱ་བ་མི་བྱེད་པ་དང་། མི་བྱ་བ་བྱེད་པའོ། །

[Block 558]
ཡང་བཞི་སྟེ། མི་ཤེས་པ་དང་། མ་གུས་པ་དང་། བག་མེད་པ་དང་། ཉོན་མོངས་པ་ཆེ་བའོ། །

[Block 559 [HEADING]]
### ལྟུང་བ་མི་འབྱུང་བའི་རྒྱུ། ^5-5-0

[Block 560]
ལྟུང་བ་མི་འབྱུང་བའི་རྒྱུ་ནི་ལྔ་སྟེ། དབང་པོ་རྣམས་ཀྱི་སྒོ་བསྡམས་ཏེ། འདུག་པ་དང་། ཟས་ཀྱི་ཚོད་རིག་པ་དང་། ནམ་གྱི་ཆ་སྟོད་དང་ཆ་སྨད་ལ་མི་ཉལ་བ༌[^299]རྣལ་འབྱོར་ལ་བརྩོན་པ་དང་། ཤེས་བཞིན་དུ་སྤྱོད་པ་དང་། དྲན་པ་དང་ལྡན་པ་དང་། བག་ཡོད་པ་དང་། ཁ་ན་མ་ཐོ་བ་ཆུང་ངུ་ལའང་འཇིགས་པར་བལྟ་བ་དང་། ཚུལ་བཞིན་དུ་སེམས་པ་ནི་རྒྱུ་དང་པོའོ། །

[Block 561]
དགེ་སྦྱོང་གི་ཚུལ་ཤས་ཆེར་ལྟ་བ་དང་། སྟོན་པ་དང་། ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་དང་། བསྟན་པ་ལ་དགའ་བའི་ལྷ་དག་དང་། སྐྱེ་བོ་མཁས་པ་དང་། འཇིག་རྟེན་པ་དག་གིས་སྨད་པར༌[^300]འགྱུར་རོ་སྙམ་པ་དང་། བདག་ཉིད་ལ་དཔྱས༌[^301]ནས་ངོ་ཚ་བ་དང་། ཁྲེལ་ཡོད་པ་ནི་རྒྱུ་གཉིས་པའོ། །

[Block 562]
དོན་ཉུང་བ་བྱ་བ་ཉུང་བ། ལས་ཀྱི་མཐའ་ཉུང་བ་ནི་རྒྱུ་གསུམ་པའོ། །

[Block 563]
ཁྱིམ་པ་དང་རབ་ཏུ་བྱུང་བ་དང་མི་འདྲེ་བར་གནས་པ་དང་ལྟུང་བ་དང་ལྟུང་བ་མ་ཡིན་པ་ལ་མཁས་པ་དང་དགེ་བའི་ཕྱོགས་ལ་བརྩོན་པ་ནི་རྒྱུ་བཞི་པའོ། །

[Block 564]
ལས་དང་པོ་པ་དང་སྨྱོས་པ༌[^302]དང་གཉིད་ལོག་པ་དང་། སེམས་འཁྲུགས་པ༌[^303]དང་། ཚོར་བས་ཉེན་པ་ནི་རྒྱུ་ལྔ་པའོ། །

[Block 565 [HEADING]]
### ལྟུང་བ་ལས་ལྡང་བ། ^5-6-0
--- END BLOCKS ---
