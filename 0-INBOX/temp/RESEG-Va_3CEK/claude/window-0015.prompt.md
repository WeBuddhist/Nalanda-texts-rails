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
[Block 526 [HEADING]]
### ཐུབ་པའི་གསུམ། ^1-36-0

[Block 527]
མདོ་ལས་ཐུབ་པའི་ནི་གསུམ་སྟེ། ཐུབ་པའི་ལུས་དང་། ཐུབ་པའི་ངག་དང་། ཐུབ་པའི་ཡིད་ཡོད༌[^372]དོ་ཞེས་གསུངས་པ་དེ་ལ།

[Block 528 [VERSE]]
མི་སློབ་ལུས་ངག་ལས་ཡིད་ཉིད། །
ཐུབ་པའི་གསུམ་སྟེ་གོ་རིམས་བཞིན། །

[Block 529]
མི་སློབ་པའི་ལུས་དང་ངག་གི་ལས་དག་ནི་ཐུབ་པའི་ལུས་དང་ངག་ཡིན་ནོ། །

[Block 530]
མི་སློབ་པའི་ཡིད་ཁོ་ན་ཡིད་ཀྱི་ཐུབ་པ་ཡིན་ཏེ། ཡིད་ཀྱི་ལས་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། སེམས་ནི་དོན་དམ་པར་ཐུབ་པ་ཡིན་ལ། དེ་ནི་ལུས་དང་ངག་གི་ལས་དག་གི་སྒོ་ནས་རྗེས་སུ་དཔག་པར་བྱ་བ་ཡིན་ནོ་ཞེས་གྲག་གོ། །

[Block 531]
གཞན་ཡང་ལུས་དང་ངག་གི་ལས་དག་ནི་སྤོང་བའི་རང་བཞིན་ཡིན་གྱི་སེམས་ལ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མེད་པའི་ཕྱིར་ཡིད་ཀྱི་ལས་ནི་མ་ཡིན་ནོ། །

[Block 532]
ཐུབ་པའི་ཡང་སྤོང་བའི་དོན་གྱིས་ཡིན་ཏེ། དེའི་ཕྱིར་ཡིད་ཉིད༌[^373]སྤོང་བ་ལ་ཐུབ་པ་ཞེས་བྱའོ། །

[Block 533]
ཅིའི་ཕྱིར་མི་སློབ་པ་ཁོ་ན་ཡིན་གྱི་གཞན་ནི་མ་ཡིན་ཞེ་ན། དགྲ་བཅོམ་པ་ནི་ཉོན་མོངས་པའི་བརྗོད་པ་ཐམས་ཅད་མེད་པས་དོན་དམ་པར་ཐུབ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 534 [HEADING]]
### གཙང་བྱེད་གསུམ། ^1-37-0

[Block 535]
མདོ་ལས་ལུས་གཙང་བྱེད་དང་ངག་གཙང་བྱེད་དང་ཡིད་གཙང་བྱེད་དང་། གཙང་བྱེད་གསུམ་གསུངས་པ་དེ་ནི།

[Block 536 [VERSE]]
[^374]ལེགས་སྤྱད་གསུམ་པོ་ཐམས་ཅད་ནི། །
གཙང་བྱེད་རྣམ་པ་གསུམ་ཡིན་ནོ། །

[Block 537]
ལུས་ཀྱི་ལེགས་པར་སྤྱད་པ་ཐམས་ཅད་ནི་ལུས་གཙང་བྱེད་ཡིན་ནོ། །

[Block 538]
ངག་དང་ཡིད་ཀྱི་ལེགས་པར་སྤྱད་པ་ཐམས་ཅད་ནི་ངག་དང་ཡིད་ཀྱི༌[^375]གཙང་བྱེད་ཡིན་ཏེ། དུས་རེ་ཞིག་དང་གཏན་དུ་ཉེས་པར༌[^376]སྤྱད་པའི་ཉོན་མོངས་པའི་དྲི་མ་སྤོངས་པའི༌[^377]ཕྱིར་རོ། །

[Block 539]
དེ་ལྟར་བསྟན་པ་འདི་ནི་ལོག་པའི་ཐུབ་པ་དང་གཙང་སྦྲ་ལ་མོས་པ་རྣམས་དཀར་བའི༌[^378]ཕྱིར་རོ། །

[Block 540 [HEADING]]
### ཉེས་པར་སྤྱད་པ་དང་ལེགས་པར་སྤྱད་པ། ^1-38-0

[Block 541]
[^379]ཉེས་པར་སྤྱད་པ་གསུམ་གསུངས་པ་དེ་ལ།

[Block 542 [VERSE]]
ལུས་ཀྱི་ལ་སོགས་མི་དགེ་བ། །
ཉེས་པར་སྤྱད་པ་གསུམ་དུ་འདོད། །

[Block 543]
ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་མི་དགེ་བ་ནི་རིམ་པ་བཞིན་དུ་ལུས་དང་ངག་དང་ཡིད་ཀྱི་ཉེས་པར་སྤྱོད་པ་ཡིན་ནོ། །

[Block 544]
བརྣབ་སེམས་ལ་སོགས་ལས་མིན་ཡང་།[^380] །ཡིད་ཀྱི་ཉེས་སྤྱད་རྣམ་གསུམ་མོ། །

[Block 545]
ལས་ཀྱི་རང་བཞིན་མ་ཡིན་པ་ཡང་ཡིད་ཀྱི་ཉེས་པར་སྤྱད་པ༌[^381]རྣམ་པ་གསུམ་ཡོད་དེ། སེམས་པ་ལས་དོན་གཞན་དུ་གྱུར་པ་བརྣབ་སེམས་དང་། གནོད་སེམས་དང་། ལོག་པར་ལྟ་བའོ། །

[Block 546]
དཔེས་སྟོན་པ་རྣམས་ན་རེ་ཆེད་དུ་བསམ་པར་བྱ་བའི་མདོ་ལས་གསུངས་པའི་ཕྱིར་བརྣབ་སེམས་ལ་སོགས་པ་ཁོ་ན་ཡིད་ཀྱི་ལས་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 547]
དེ་ལྟ་ན་ནི་ལས་དང་ཉོན་མོངས་པ་དག་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 548]
གལ་ཏེ་ཉོན་མོངས་པ་འགའ་ཞིག་ལས་སུ་གྱུར་ན་ཡང་ཅིར་འགྱུར། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་མདོ་དང་འགལ་བའི་ཕྱིར་དེ་ནི་མེད་དེ། མདོ་ལས་ནི་དེའི་སྒོ་ནས་སེམས་པ་ཞུགས་པའི་ཕྱིར་དེ་དག་གིས༌[^382]དེ་སྟོན་པར་བྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 549]
ལུས་དང་ངག་དང་ཡིད་ཀྱི་སྤྱོད་པ་སྨད་པ་ནི་འབྲས་བུ་ཡིད་དུ་མི་འོང་བ་ཡིན་པའི་ཕྱིར་ཉེས་པར་སྤྱད་པ་ཡིན་ནོ། །

[Block 550]
བཟློག་པ་ལེགས་པར་སྤྱད་པ་ཡིན། །ཉེས་པར་སྤྱད་པ་ལས་བཟློག་པ་ནི་ལེགས་པར་སྤྱད་པ་ཡིན་པར་འདོད་དེ། ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་དགེ་བ་དང་། བརྣབ་སེམས་མེད་པ་དང་། གནོད་སེམས་མེད་པ་དང་། ཡང་དག་པའི་ལྟ་བ་རྣམས་སོ། །

[Block 551]
ཕ་རོལ་ལ་ཕན་འདོགས་པ་དང་གནོད་པ་བྱ་བའི་བསམ་པ་མེད་པར་ན་ཇི་ལྟར་ན༌[^383]ཡང་དག་པའི་ལྟ་བ་དང་ལོག་པའི་ལྟ་བ་དག་དགེ་བ་དང་མི་དགེ་བ་ཉིད་ཡིན་ཞེ་ན། དེའི་རྩ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 552 [HEADING]]
### ལས་ཀྱི་ལམ་བཅུ། ^1-39-0

[Block 553]
ཉེས་པར་སྤྱད་པ་དང་། ལེགས་པར་སྤྱད་པར་བཤད་པ་གང་དག་ཡིན་པ།

[Block 554 [VERSE]]
དེ་ལས་ཆེ་ལོང་བསྡུས་ནས་ནི། །
དགེ་དང་མི་དགེ་ཅི་རིགས་པར། །
ལས་ཀྱི་ལམ་ནི་བཅུར་གསུངས་སོ། །

[Block 555]
ཉེས་པར་སྤྱད་པ་དང་། ལེགས་པར་སྤྱད་པ་དེ་དག་ཉིད་བས༌[^384]ཆེ་ལོང་བསྡུས་ཏེ་ཅི་རིགས་པར་མདོ་ལས་ལས༌[^385]ཀྱི་ལམ༌[^386]བཅུར་གསུངས་ཏེ། དགེ་བ་རྣམས་ནི་ལེགས་པར་སྤྱད་པ་དག་ལས་སོ། །

[Block 556]
མི་དགེ་བ་རྣམས་ནི་ཉེས་པར་སྤྱད་པ་དག་ལས་སོ། །

[Block 557]
འདིར་ཉེས་པར་སྤྱད་པ་ཅི་ཞིག་གམ། ལེགས་པར་སྤྱད་པ་ཅི་ཞིག་མ་བསྡུས་ཤེ་ན། རེ་ཞིག་མི་དགེ་བའི་ལས་ཀྱི་ལམ་རྣམས་སུ་ནི་ལུས་ཀྱི་ཉེས་པར་སྤྱད་པའི་ཕྱོགས་སྦྱོར་བ་དང་མཇུག༌[^387]དང་། ཉོན་མོངས་པ༌[^388]ཅན་གཞན་ཡང་མ་བསྡུས་ཏེ། དེ་ནི་ཤིན་ཏུ་རགས་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 558]
ལུས་ཀྱི་ཉེས་པར་སྤྱད་པ་གཞན་དག་འཚོ་བ་དང་ལོངས་སྤྱོད་དང་། ཆུང་མ་རྣམས་དང་འབྲལ་བར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་དེ་དང་འབྲལ་བར་བྱ་བའི་ཕྱིར་ལས་ཀྱི་ལམ་དུ་བཤད་དོ། །

[Block 559]
ངག་གི་ཉེས་པར་སྤྱད་པ་ཡང་ཚབས་པོ་ཆེ་གང་ཡིན་པ་དེ་ཁོ་ན་ཉིད་ཀྱི་ཕྱིར་ལས་ཀྱི་ལམ་དུ་བཤད་དོ། །

[Block 560]
ཡིད་ཀྱི་ཉེས་པར་སྤྱད་པའི་ཕྱོགས་སེམས་པ་ཡང་མ་བསྡུས་སོ། །

[Block 561]
དགེ་བ་ལ་ཡང་ལུས་ཀྱི་ལེགས་པར་སྤྱད་པའི་ཕྱོགས་སྦྱོར་བ་དང་མཇུག་དང་། མྱོས་པར་འགྱུར་བ་ལ་སོགས་པ་སྤོང་བ་དང་། སྦྱིན་པ་དང་། མཆོད་སྦྱིན་ལ་སོགས་པ་མ་བསྡུས་སོ། །

[Block 562]
ངག་གི་ལེགས་པར་སྤྱད་པའི་ཡང་སྙན་པར་སྨྲ་བ་ལ་སོགས་པ་མ་བསྡུས་སོ། །

[Block 563]
ཡིད་ཀྱི་ལེགས་པར་སྤྱད་པའི་ཡང་སེམས་པ་མ་བསྡུས་སོ། །

[Block 564 [HEADING]]
### ལས་ཀྱི་ལམ་རྣམ་པར་རིག་བྱེད་དང་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ། ^1-40-0

[Block 565]
ལས་ཀྱི་ལམ་དེ་རྣམས་ལས།
--- END BLOCKS ---
