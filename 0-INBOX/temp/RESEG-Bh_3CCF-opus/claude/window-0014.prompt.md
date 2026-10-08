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
[Block 491]
[^100]: བཀྲུ་བར་བྱ་བར་ ༼སྣར། པེ།༽ བཀྲུ་བར་

[Block 492]
[^101]: གསང་བ་ ༼སྣར། པེ།༽ བསད་བ་

[Block 493]
[^102]: སྣོད་ ༼སྣར། པེ།༽ ནང་

[Block 494]
[^103]: རང་བཞིན་གྱིས་ ༼སྣར། པེ།༽ རང་བཞིན་གྱི་

[Block 495]
[^104]: འདི་ ༼སྣར། པེ།༽ ནི་

[Block 496]
[^105]: བའི་ ༼སྣར། པེ།༽ བར་

[Block 497]
[^106]: དི་བ་ ༼སྣར། པེ།༽ དི་པ་

[Block 498]
[^107]: ཐ་མར་ ༼སྣར། པེ།༽ མཐའ་མར་

[Block 499]
[^108]: གསད་པའི་ ༼སྣར། པེ།༽ བསད་པའི་

[Block 500]
[^109]: རྣམས་བཏོན་ཏོ།།

[Block 501]
༼སྣར། པེ།༽ རྣམས་གཏོན་ཏེ་

[Block 502]
[^110]: བརླབས་པའི་ ༼སྣར། པེ།༽ བསླབས་པའི་

[Block 503]
[^111]: དཔྱད་པར་ ༼སྣར། པེ།༽ བཅད་པར་

[Block 504]
[^112]: བྱ་བའོ། ༼པེ།༽ བྱའོ།

[Block 505]
[^113]: ཛ་ ༼སྣར། པེ།༽ ཛི་

[Block 506]
[^114]: བཀྲི་བར་ ༼སྣར། པེ།༽ དཀྲི་བར་

[Block 507]
[^115]: བསམས་པའི་ ༼སྣར། པེ།༽ བསམ་པའི་

[Block 508]
[^116]: བསྒྲུབ་ ༼སྣར། པེ།༽ སྒྲུབ་

[Block 509]
[^117]: ལུས་སྤོ་ ༼སྣར། པེ།༽ ལུས་པོ་

[Block 510]
[^118]: སྤོ་ ༼པེ།༽ པོར་

[Block 511]
[^119]: སྡུད་ ༼སྣར། པེ།༽ བསྡུད་

[Block 512]
[^120]: བཏབ་པར་ ༼སྣར། པེ།༽ བཏང་བར་

[Block 513]
[^121]: གཞག་པར་ ༼སྣར། པེ།༽ བཞག་པར་

[Block 514]
[^122]: གཞག་ ༼སྣར། པེ།༽ བཞག་

[Block 515]
[^123]: ལ་སོགས་པ་ ༼སྣར། པེ།༽ ལ་སོགས་

[Block 516]
[^124]: ལས་ ༼སྣར། པེ།༽ ལ་

[Block 517]
[^125]: དང་ ༼སྣར། པེ།༽ པདྨ་

[Block 518]
[^126]: བྱ་ ༼པེ།༽ བྱ་བ་

[Block 519]
[^127]: གཟུང་ ༼སྣར། པེ།༽ བཟུང་

[Block 520]
[^128]: བརླབ་པར་ ༼སྣར།༽ བརླབས་པར་ ༼པེ།༽ རླབས་

[Block 521]
[^129]: གནང་བ་ ༼སྣར། པེ།༽ སྣང་བ་

[Block 522]
[^130]: འཚམ་ ༼སྣར། པེ།༽ མཚམ་

[Block 523]
[^131]: ཆོས་ཉིད་ ༼སྣར། པེ།༽ ཆོས་

[Block 524]
[^132]: དེ་བཞིན་དུ་ ༼སྣར། པེ།༽ དེ་བཞིན་

[Block 525]
[^133]: ཉི་ ༼སྣར། པེ།༽ ཉིད་

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
--- END BLOCKS ---
