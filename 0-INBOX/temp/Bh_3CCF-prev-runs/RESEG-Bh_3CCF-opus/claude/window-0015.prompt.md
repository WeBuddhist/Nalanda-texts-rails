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
[^134]: དེ་དག་ནི་ ༼སྣར། པེ།༽ དེ་དག་གི་

[Block 527]
[^135]: པ་བཟའ་བ་ ༼སྣར། པེ།༽ པའི་དམ་པ་

[Block 528]
[^136]: བསྒྲུབས་པས་ ༼སྣར། པེ།༽ བསྒྲུབ་པས་

[Block 529]
[^137]: གཟུད་དོ། ༼པེ།༽ གཟུགས་སོ།

[Block 530]
[^138]: གཟུང་མ་ ༼སྣར།༽ བཟུང་ལ་ ༼པེ།༽ གཟུང་ལ་

[Block 531]
[^139]: གསད་པ་ ༼སྣར། པེ།༽ བསད་པ་

[Block 532]
[^140]: ལེན་པ་ ༼སྣར། པེ།༽ ལེན་པར་

[Block 533]
[^141]: ཕྱི་རོལ་གྱི་ ༼པེ།༽ ཕྱི་རོལ་གྱིས་

[Block 534]
[^142]: ཀྱིས་ ༼སྣར། པེ།༽ ཀྱི་

[Block 535]
[^143]: རྒྱན་གྱིས་ ༼སྣར། པེ།༽ བརྒྱན་གྱི་

[Block 536]
[^144]: གནས་པར་ ༼སྣར། པེ།༽ གནས་པས་

[Block 537]
[^145]: གཞག་པར་ ༼སྣར། པེ།༽ བཞག་པར་

[Block 538]
[^146]: རིགས་ ༼སྣར། པེ།༽ རིག་

[Block 539]
[^147]: བྱ་བ་ནི་ ༼སྣར། པེ།༽ བྱ་བ་

[Block 540]
[^148]: གྱུར་ཏེ། ༼སྣར། པེ།༽ གྱུར་ཏོ།

[Block 541]
[^149]: དྲེགས་པ་ ༼སྣར། པེ།༽ དྲེག་པ་

[Block 542]
[^150]: རྣམ་པར་ ༼སྣར། པེ།༽ རྣམ་

[Block 543]
[^151]: སྩོལ་བ་ ༼པེ།༽ བསྩོལ་བ་

[Block 544]
[^152]: མེད་པའི་ཡང་བླ་ན་མེད་ ༼སྣར། པེ།༽ མེད་

[Block 545]
[^153]: སློབ་དཔོན་གྱི་ ༼སྣར། པེ།༽ སློབ་དཔོན་གྱིས་

[Block 546]
[^154]: སྩོལ་བས་ ༼སྣར། པེ།༽ རྩོལ་བས་

[Block 547]
[^155]: བླུགས་ ༼པེ།༽ བླུག་

[Block 548]
[^156]: བསམས་ ༼པེ།༽ བསམ་

[Block 549]
[^157]: པ་ ༼སྣར། པེ།༽ པས་

[Block 550]
[^158]: རྡོ་རྗེ་ཡང་ ༼སྣར། པེ།༽ རྡོ་རྗེ་

[Block 551]
[^159]: མནན་པའི་ ༼སྣར། པེ།༽ གནས་པའི་

[Block 552]
[^160]: བཞུགས་པ་ན་ ༼སྣར། པེ།༽ བཞུགས་པ་

[Block 553]
[^161]: བྱེད་ ༼སྣར།༽ འབྱེད་

[Block 554]
[^162]: རྡོ་རྗེའི་ ༼སྣར། པེ།༽ རྡོ་

[Block 555]
[^163]: ཞལ་སྔ་ནས་ ༼སྣར། པེ།༽ ཞལ་སྔ་

[Block 556]
[^164]: ཞིང་ཞུས་ཏེ་གཏན་ལ་ཕབ་པ། ༼སྣར།༽ ཞིང་གཏན་ལ་ཕཕབ་པ་བཀྲ་ཤིས ༼པེ།༽ ཞིང་གཏན་ལ་ཕཕབ་པ་མངྒཱལཾ།
--- END BLOCKS ---
